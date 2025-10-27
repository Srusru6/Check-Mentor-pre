# Zero-Index Bound States in the Continuum

Momchil Minkov,\* Ian A. D. Williamson, Meng Xiao, and Shanhui Fan\*  
Department of Electrical Engineering, and Ginzton Laboratory, Stanford University, Stanford, California 94305, USA

(Received 24 August 2018; published 27 December 2018)

Metamaterials with an effective zero refractive index associated with their electromagnetic response are sought for a number of applications in communications and nonlinear optics. A promising way that this can be achieved in all-dielectric photonic crystals is through the design of a Dirac cone at zero Bloch wave vector in the photonic band structure. In the optical frequency range, the natural way to implement this design is through the use of a photonic crystal slab. In the existing implementation, however, the zero-index photonic modes also radiate strongly into the environment due to intrinsic symmetry properties. This has resulted in large losses in recent experimental realizations of this zero-index paradigm. Here, we propose a photonic crystal slab with zero-index modes which are also symmetry-protected bound states in the continuum. Our approach thus eliminates the associated radiation loss. This could enable, for the first time, large-scale integration of zero-index materials in photonic devices.

DOI: 10.1103/PhysRevLett.121.263901

Recently, there has been a lot of interest in photonic metamaterials with a zero (effective) refractive index [1-4]. In such materials, all fields oscillate in spatial unison regardless of the shape and size of the sample, and the wavelength of light appears to be effectively infinite. This has been demonstrated to lead to a variety of interesting effects and possible applications, including tailoring the radiation phase [2], developing enhanced and directional light emitters [5-7], enhanced and directional transmission through bends, disorder, and subwavelength channels [8-12], cloaking [13], and enhanced optical nonlinearities [14-16].

In the visible or near-infrared wavelength range, zero-index response can be achieved starting from the plasmonic effects from free carriers [4], which, however, also come with a substantial material loss. Alternatively, Ref. [17] has shown that a zero-index effect can be achieved in a two-dimensional all-dielectric photonic crystal, whose band structure is designed to exhibit a Dirac-like dispersion in the vicinity of the  $\Gamma$  point at the Brillouin zone center. However, while a purely two-dimensional implementation of the idea of Ref. [17] has intrinsically zero loss, in the optical frequency the most natural way to implement the same concept is through the use of a photonic crystal slab structure consisting of a patterned dielectric slab surrounded by low-dielectric-constant materials. In this case, the  $\Gamma$  point lies in the light cone of the surrounding medium, which leads to substantial radiative losses. For example, the implementation of this concept in Ref. [18] reported a very large propagation loss of the order of  $1\mathrm{dB} / \mu \mathrm{m}$ . In Ref. [19], gold mirrors on each side of the slab were introduced to avoid that radiation, but this resulted in absorption losses of comparable magnitude. Finally, it has also been proposed that this issue could be mitigated through a dielectric reflector on one side of the slab [20],

but this significantly increases the complexity and footprint of the structure.

In this Letter, we overcome the problem of radiative losses by designing a PhC slab with effectively zero-index modes, which are also symmetry-protected bound states in the continuum (BIC) [21]. Consider a photonic crystal structure with two-dimensional periodicity, with a point-group symmetry that supports at least one two-dimensional irreducible representation. At the  $\Gamma$  point, suppose the crystal supports a singly degenerate state  $|s\rangle$  at a frequency  $\omega_{1}$ , and a pair of doubly degenerate states  $|p_x\rangle$  and  $|p_y\rangle$  belonging to the two-dimensional irreducible representation at a frequency  $\omega_{2}$ . Finally, suppose also an accidental degeneracy such that  $\omega_{1} = \omega_{2}$ . In the vicinity of the  $\Gamma$  point, using the  $k\cdot p$  method to first order, one can then show that the band structure of the crystal is described by an effective Hamiltonian [22],

$$
C _ {\mathbf {k}} = \left( \begin{array}{c c c} 0 & 0 & b _ {x} k _ {x} \\ 0 & 0 & b _ {y} k _ {y} \\ b _ {x} ^ {*} k _ {x} & b _ {y} ^ {*} k _ {y} & 0 \end{array} \right), \tag {1}
$$

where the  $b_{x}$  and  $b_{y}$  coefficients are given by an overlap integral between the  $|s\rangle$  and  $|p_{x / y}\rangle$  states and the "momentum" term, and  $|b_{x}| = |b_{y}|$ . Near the  $\Gamma$  point the band structure corresponding to such a Hamiltonian has two bands with Dirac-like linear dispersion, as well as a flat band. This is the same band structure as that of a zero-index material [23]. Despite the fact that the elementary cell of the photonic crystal is of comparable size to the free-space wavelength, it has been shown that an effective-medium theory can still formally be applied when the Bloch vector  $\mathbf{k}$  is close to zero, i.e., when the effective wavelength is

large [17-19,24]. Therefore, an effectively zero-index material can be created using a photonic crystal structure with an appropriate accidental degeneracy at the  $\Gamma$  point.

Based on the theory above, Ref. [17] achieved a zero-index material starting from a photonic crystal with a square lattice as described by the  $C_{4v}$  point group, which supports a single two-dimensional irreducible representation (denoted by  $E$ ). The difficulty arises, however, when implementing this strategy in the infrared or optical wavelength range using a photonic crystal slab geometry. This is because modes at the  $\Gamma$  point with a nonzero frequency lie in the radiation continuum, and, moreover modes belonging to the  $E$  irreducible representation necessarily couple to external plane waves [25,26]. As a result, the zero-index modes necessarily have significant intrinsic radiation loss, as observed experimentally in Ref. [18].

To overcome the difficulty associated with the radiation loss, here instead we consider a hexagonal lattice with a  $C_{6v}$  point group. The  $C_{6v}$  group has two distinct two-dimensional irreducible representations (denoted as  $E_1$  and  $E_2$ , respectively). For a photonic crystal slab with a  $C_{6v}$  symmetry, at the  $\Gamma$  point, modes that belong to the  $E_2$  irreducible representation do not couple to external plane waves; i.e., the modes are symmetry-protected bound states in the continuum. Moreover, any mode at the  $\Gamma$  point that belongs to a one-dimensional irreducible representation also does not couple to external plane waves. In this system, a nonradiative zero-index bound state in the continuum can be created by forcing an accidental degeneracy between modes in the  $E_2$  and the  $B_1$  or  $B_2$  irreducible representations, since the  $b_{x/y}$  coefficients in Eq. (1) in this case are nonzero [22].

We implement our proposal in the structure shown in Fig. 1(a), which consists of a hexagonal lattice of air holes with lattice period  $a$  in a silicon slab (dielectric permittivity  $\varepsilon_r = 12$ ) of thickness  $d = 0.5a$ . The holes have a daisylike shape that can be written in polar coordinates as  $r(\phi) = r_0 + r_d\cos(6\phi)$ , with  $r_0 = 0.35a$  and  $r_d = 0.08a$ . The dashed lines in the inset show the inner and outer radii,  $r_0 - r_d$ , and  $r_0 + r_d$ , respectively. Below we refer to this structure as a "daisy photonic crystal." We note that a standard PhC slab with circular holes already has all the required symmetries, but we could not attain an accidental degeneracy between modes in the  $E_2$  and  $B_{1/2}$  representations by tuning only the circular hole radius. In contrast, we could successfully achieve such accidental degeneracy in the daisy photonic crystal by tuning  $r_0$  and  $r_d$ . Further details regarding the way we designed this photonic crystal are provided in the Supplemental Material [27].

Figure 1(b) shows the band structure for the quasi-TM modes (more precisely, the antisymmetric modes with respect to reflection from the  $xy$  plane [28]) for this  $\mathrm{PhC}$ , computed using the guided-mode expansion method (GME) [29]. Panel (c) shows an enlargement over the region where a clear Dirac cone dispersion is visible, as well as a band that is relatively flat in the vicinity of the

![](images/a39027bc3751b3b2e6e1d4d63bffe0f1678b7ba7c86f64aec308f70b80b62398.jpg)

![](images/5975fd69658b099083ae4b2d061cb65ad4b391e5516a9df5f81526041c695f78.jpg)

![](images/8714ce06234159356fbbaa348403c36535fc061720df9f02c124e54921f84057.jpg)

![](images/4515f85c84d4467e6abab46418395e61b665291996abf3c5d289112f2f094327.jpg)  
FIG. 1. (a) Schematic of the photonic crystal slab. The inset shows the daisy hole shape with its inner and outer radii (dashed lines), as well as the in-plane elementary cell (solid line). (b) Photonic bands for the quasi-TM modes computed with GME. (c) Enlargement within the dashed lines of (b), with dots showing the modes computed with COMSOL. (d) Isofrequency contours in 2D reciprocal space for the top band of the dirac cone [blue band in (c)]. (e): Radiative quality factors for the three corresponding bands in (c).

![](images/9cf81a9c45d67dae6f3ed60c4e9aba24b14676cf4956e56cf02126150a952a45.jpg)

$\Gamma$  point. These results were also confirmed using COMSOL MULTIPHYSICS 5.3. Panel (d) shows the isofrequency contours for the high-frequency branch of the Dirac cone, and illustrates that the dispersion is highly isotropic around  $\Gamma$ . Finally, in panel (e) we show the quality factors (Q) associated with the radiative loss rates of the three photonic bands, computed both with GME and with COMSOL, and observe that the quality factors diverge at  $\Gamma$ , indicating that the states are fully bound. Note that the blue band has one additional BIC at a finite wave vector  $k$  along the  $\Gamma K$  direction, i.e.,  $k$  pointing in the  $x$  direction in panel (a). We note further that the  $Q$ 's of all bands diverge to infinity when they enter the region outside of the light cone [compare 1(c) and 1(e)].

To compute an effective index for the PhC slab, we use COMSOL to study the in-plane phase evolution of the

![](images/c2c43d2bca3480d4e954f7b729ec09ad52517a6e27f6eb30eb3f653e3f62ccf3.jpg)

![](images/01fbc13ba4fed0dedf930a378dc9d6b93eb6db081eb8b02a4f06b0bb2e455d80.jpg)  
FIG. 2. (a)-(c) Electric field  $\mathrm{Re}(E_z)$  in the center of the slab ( $z = 0$ ) for a plane-wave excitation from the left, with a wave vector along the  $y$  direction (ΓM), at reduced frequency  $\bar{\omega} = \omega a / (2\pi c) = 0.48$  (a), 0.486 (b), and 0.492 (c). (d) Phase of the electric field at the sampling points marked with black dots in panels (a)-(c). (e) Effective index computed from the slope of the phase evolution with position (dots), and from the Bloch band structure (line). (f) Group index and propagation loss of the Dirac-cone bands along the two crystallographic directions as a function of wavelength, assuming  $a = 760$  nm. The  $x$ -axis scale and range in panels (e) and (f) are the same. Plots as in (a)-(e) for ΓK are in the Supplemental Material [27].

![](images/712809ad88d3401a3a75b0e0ffd68c38321de0650b8a1579db0febf57421b3cb.jpg)

![](images/4e2151965e2adcc3f55377132b4d010d4d6c600ccbdb85e7b8f2a68d2eddb752.jpg)

electric field in a dielectric slab with a finite-length photonic crystal introduced in it, as shown in Fig. 2(a). In Figs. 2(a)-2(c), we show this for propagation along the  $\Gamma M$  direction, imposing periodic boundary conditions at  $x = \pm a / 2$ , and perfectly matched layer boundary conditions in the  $y$  and  $z$  directions. In  $z$ , these were placed at a distance of  $3a$  from each side of the slab. The excitation frequency in panel (b),  $\bar{\omega} = \omega a / (2\pi c) = 0.486$ , is very close to the frequency  $\omega_0$  at the tip of the Dirac cone, for which an effectively zero-index response is expected. Indeed, we see that the fields in all the elementary cells in the propagation direction oscillate in phase. In the case of panels (a) and (c), when the excitation frequency is detuned away from  $\omega_0$ , there is a slow evolution of the oscillation phase along the propagation direction. This is better illustrated in panel (d), where we plot the phase at equivalent reference points in each elementary cell that are related by translational symmetry [black dots in (a)-(c)]. We see that the phases vary linearly as a function of propagation distance. The refractive index  $n$  for a homogeneous material is such that the field evolution of a plane wave follows  $E_z(\rho) = E_z(0)e^{ink_0\rho}$ , where  $\rho$  is the distance along the propagation direction, and  $k_{0} = \omega /c$ . Analogously, an effective refractive index  $n_e$  can be extracted from the slope of the lines in Fig. 2(d), using the model  $E_z(y_0 + m\sqrt{3} a) = E_z(y_0)e^{in_e k_0 m\sqrt{3} a}$ , with  $m$  an integer. In panel (e), we plot the effective index obtained in this way, which agrees very well the effective index  $n_e' = ck / \omega_k$ , as obtained by directly examining the band structure as shown in Fig. 1(b). Therefore, the band

structure in Fig. 1(b) explains very well the field evolution behavior, including the zero-index behavior in a finite-sized photonic crystal structure.

In Fig. 2(f), we show the group index associated to the Dirac-cone bands,  $n_g = v_g / c$ , with the group velocity  $v_{g} = d\omega_{k} / dk$  computed numerically. Furthermore, to show the significance of our structure for potential applications in optical information processing, we set  $a = 760~\mathrm{nm}$ , such that the zero-index response is in the telecommunication band around wavelength  $\lambda = 1550~\mathrm{nm}$ , and we compute the theoretical loss in field intensity due to out-of-plane radiation per unit of propagation distance. For this, we compute the loss in units of decibel per millimeter (mm) as

$$
L \left[ \frac {\mathrm {d B}}{\mathrm {m m}} \right] = \frac {1 0}{\ln 1 0} \left(\frac {\omega_ {k}}{c} \frac {n _ {g}}{Q _ {k}}\right) \times 1 \mathrm {m m}, \tag {2}
$$

where  $Q_{k}$  is taken from Fig. 1(c). This quantity is shown in brown in panel (f) both for propagation along  $\Gamma M$  and  $\Gamma K$ . Results analogous to panels (a)-(e) but for the  $\Gamma K$  direction are shown in the Supplemental Material [27]. We stress that, because the modes are BICs at  $\Gamma$ , the losses go to zero at the zero-index frequency. Furthermore, it is noteworthy that the loss is smaller than  $10~\mathrm{dB / mm}$  i.e., 2 orders of magnitude smaller than the propagation loss experimentally reported in Refs. [18,19] over a wavelength bandwidth exceeding  $30~\mathrm{nm}$ , within which the effective index is  $|n_e| < 0.1$ . This shows that our structure is not only expected to have outstanding properties at the Dirac-cone

![](images/95f74d6061b1b6b04b614fff2a0d8cfc1a4bfe435087885b61a1ef14aaea8e6c.jpg)

![](images/dd948d5a8bf41ee4c43d2e59c37c8aa3519911cc6a80c3a6412cb0f697ffce0a.jpg)

![](images/6dee505ac375e40ff12f2377953799218fc2cc6ae264d7705631056129814a65.jpg)

![](images/ddfc284f1fd9f71c19b6718335b7e7204f512ebcd7f79edc48452a4fc476758e.jpg)

![](images/107c6e4f91537a4d1957406162dbdc94e87c093a0f873d14d6974435aeb2e9c9.jpg)  
FIG. 3. Electric field  $\mathrm{Re}(E_z)$  for a simulated triangular region of zero-index PhC slab surrounded by unpatterned slab. (a) 3D view and (b) cross section in the center of the slab for a dipole source excitation in the center of the PhC region (black dot), at frequency  $\bar{\omega} = 0.486$ . Arrows indicate the direction of the emitted waves. (c) Dipole-source excitation in the center of a homogeneous triangular region with relative permittivity and permeability  $\varepsilon_r = \mu_r = 10^{-6}$ . The simulated structure is infinite in the  $z$  direction. (d)-(f) Same as (a)-(c), but with a Gaussian wave packet excitation from below.

![](images/148bdca461b01e14e5db96127b4f9db716ec510e3b3f43fd833fb0385f4df1a6.jpg)

frequency, but it could also be relevant for broadband applications.

As a final set of demonstrations, we study the zero-index effect in a photonic crystal structure that is finite in all in-plane dimensions, and compare these effects to those of a homogeneous zero-index material. The plots in Figs. 3(a)–3(b) show the emission due to an electric dipole source placed in the middle of a triangular region of the PhC, surrounded by unpatterned silicon slab. The dipole frequency is at the Dirac point,  $\bar{\omega} = 0.486$ . As expected for zero-index propagation, all of the elementary cells of the PhC oscillate in phase, which leads to highly directional, collimated emission from the interfaces. This can be compared to panel 3(c), where we show a 2D simulation of a homogeneous triangular region with relative parameters  $\varepsilon_r = \mu_r = 10^{-6}$  surrounded by air. Panels 3(b) and 3(c) match very well qualitatively. One difference worth noting is the fact that a near-field pattern is imprinted on the outcoming waves in 3(b), but this pattern gradually disappears, resulting in a plane-wave wave front away from the interfaces. We also note that in panel 3(a), there is strong emission outside of the slab, but this is due to the

direct coupling of the source to radiative modes, as opposed to leakage of the Dirac-cone modes. To illustrate this point better, in panels 3(d)–3(e) we show the same structure, but now illuminated by a Gaussian beam in the slab waveguide on the lower side. The characteristics of the outgoing waves in the uniform slab regions are similar to that of panel 3(b), and match well the simulation of a homogeneous region shown in panel 3(f). The important difference to note here is that in this case there is very little radiation outside of the slab. Most radiation outside the slab occurs around the in-coupling interface, which arises from a small impedance mismatch between the two regions. In this case, the absence of radiation on top of the interior of the photonic crystal slab indicates that once the zero-index PhC mode is excited, it has negligible radiation losses to the environment, as expected from Figs. 1(e) and 2(f).

In conclusion, we have shown a way to completely eliminate the out-of-plane radiation for an experimentally accessible zero-index structure. Combined with the fact that this is an all-dielectric device, our result is a significant step in the direction of recent efforts to introduce zero-index materials in integrated photonics platforms [18,19]. Indeed, the large radiative losses have recently been identified as one of the main remaining challenges in that direction [30]. In our structure, the theoretically predicted losses go to zero at the Dirac-cone frequency, and, furthermore, for wavelengths in the  $1550\mathrm{nm}$  range, we estimate propagation loss as low as  $1\mathrm{dB / mm}$  and an index below 0.1 within a  $10\mathrm{nm}$  bandwidth. The presented photonic crystal is thus ideal for applications in linear and nonlinear optics and emission control at optical and near-infrared frequencies.

This work was supported by the Swiss National Science Foundation through Project No. P300P2_177721, by a Vannevar Bush Faculty Fellowship (Grant No. N00014-17-1-3030) from the U.S. Department of Defense, and by a MURI grant from the U.S. Air Force Office of Scientific Research (Grant No. FA9550-17-1-0002).

* mminkov@stanford.edu † shanhui@stanford.edu

[1] R. W. Ziolkowski, Phys. Rev. E 70, 046608 (2004).  
[2] A. Alù, M. G. Silveirinha, A. Salandrino, and N. Engheta, Phys. Rev. B 75, 155410 (2007).  
[3] N. Engheta, Science 340, 286 (2013).  
[4] I. Liberal and N. Engheta, Nat. Photonics 11, 149 (2017).  
[5] S. Enoch, G. Tayeb, P. Sabouroux, N. Guérin, and P. Vincent, Phys. Rev. Lett. 89, 213902 (2002).  
[6] P. Moitra, Y. Yang, Z. Anderson, I. I. Kravchenko, D. P. Briggs, and J. Valentine, Nat. Photonics 7, 791 (2013).  
[7] Z. Lin, A. Pick, and M. Loncar, and A. W. Rodriguez, Phys. Rev. Lett. 117, 107402 (2016).  
[8] M. Silveirinha and N. Engheta, Phys. Rev. Lett. 97, 157403 (2006).

[9] R. Liu, Q. Cheng, T. Hand, J.J. Mock, T.J. Cui, S.A. Cummer, and D.R. Smith, Phys. Rev. Lett. 100, 023903 (2008).  
[10] B. Edwards, A. Alù, M. E. Young, M. Silveirinha, and N. Engheta, Phys. Rev. Lett. 100, 033903 (2008).  
[11] B. Edwards, A. Al, M. G. Silveirinha, and N. Engheta, J. Appl. Phys. 105, 044905 (2009).  
[12] V. C. Nguyen, L. Chen, and K. Halterman, Phys. Rev. Lett. 105, 233908 (2010).  
[13] J. Hao, W. Yan, and M. Qiu, Appl. Phys. Lett. 96, 101109 (2010).  
[14] H. Suchowski, K. O'Brien, Z. J. Wong, A. Salandrino, X. Yin, and X. Zhang, Science 342, 1223 (2013).  
[15] M. Z. Alam, M. Z. Alam, I. D. Leon, and R. W. Boyd, Science 352, 795 (2016).  
[16] L. Caspani, R. P. M. Kaipurath, M. Clerici, M. Ferrera, T. Roger, J. Kim, N. Kinsey, M. Pietrzyk, A. Di Falco, V. M. Shalaev, A. Boltasseva, and D. Faccio, Phys. Rev. Lett. 116, 233901 (2016).  
[17] X. Huang, Y. Lai, Z. H. Hang, H. Zheng, and C. T. Chan, Nat. Mater. 10, 582 (2011).  
[18] D. I. Vulis, Y. Li, O. Reshef, P. Camayd-Munoz, M. Yin, S. Kita, M. Loncar, and E. Mazur, Opt. Express 25, 12381 (2017).  
[19] Y. Li, S. Kita, P. Muñoz, O. Reshef, D. I. Vulis, M. Yin, M. Loncar, and E. Mazur, Nat. Photonics 9, 738 (2015).  
[20] P. Muñoz, S. Kita, O. Mello, O. Reshef, D. I. Vulis, Y. Li, M. Loncar, and E. Mazur, Lossless integrated Dirac-cone metamaterials, Proceedings of the Conference on Lasers and

Electro-Optics (Optical Society of America, Washington, DC, 2016), p. JW2A.24, https://doi.org/10.1364/CLEO_AT.2016.JW2A.24.  
[21] C. W. Hsu, B. Zhen, A. D. Stone, J. D. Joannopoulos, and M. Soljačić, Nat. Rev. Mater. 1, 16048 (2016).  
[22] K. Sakoda, Opt. Express 20, 25181 (2012).  
[23] L.-G. Wang, Z.-G. Wang, J.-X. Zhang, and S.-Y. Zhu, Opt. Lett. 34, 1510 (2009).  
[24] Y. Wu, J. Li, Z.-Q. Zhang, and C. T. Chan, Phys. Rev. B 74, 085111 (2006).  
[25] T. Ochiai and K. Sakoda, Phys. Rev. B 63, 125107 (2001).  
[26] S. Fan and J. D. Joannopoulos, Phys. Rev. B 65, 235112 (2002).  
[27] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.121.263901 for the point-group symmetry considerations that lead us to the zero-index bound states in the continuum in a hexagonal-lattice photonic crystal slab and why we introduce daisy-shaped holes. Furthermore, we show field profiles of some of the Bloch eigenmodes, as well as of modes propagating in the  $\Gamma \mathrm{K}$  direction.  
[28] S. G. Johnson, S. Fan, P. R. Villeneuve, J. D. Joannopoulos, and L. A. Kolodziejski, Phys. Rev. B 60, 5751 (1999).  
[29] L. C. Andreani and D. Gerace, Phys. Rev. B 73, 235114 (2006).  
[30] D. I. Vulis, O. Reshef, P. Camayd-Munoz, and E. Mazur, Rep. Prog. Phys., 82 012001 (2018).