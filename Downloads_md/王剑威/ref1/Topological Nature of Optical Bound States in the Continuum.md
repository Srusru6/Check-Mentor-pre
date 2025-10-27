# Topological Nature of Optical Bound States in the Continuum

Bo Zhen, $^{1,*}$  Chia Wei Hsu, $^{1,2}$  Ling Lu, $^{1}$  A. Douglas Stone, $^{3}$  and Marin Soljacic $^{1}$

$^{1}$ Department of Physics, Massachusetts Institute of Technology, 77 Massachusetts Avenue, Cambridge, Massachusetts 02139, USA

$^{2}$ Department of Physics, Harvard University, 17 Oxford Street, Cambridge, Massachusetts 02138, USA

$^{3}$ Department of Applied Physics, Yale University, Post Office Box 208284, New Haven, Connecticut 06520, USA

(Received 20 August 2014; published 18 December 2014)

Optical bound states in the continuum (BICs) have recently been realized in photonic crystal slabs, where the disappearance of out-of-plane radiation turns leaky resonances into guided modes with infinite lifetimes. We show that such BICs are vortex centers in the polarization directions of far-field radiation. They carry conserved and quantized topological charges, defined by the winding number of the polarization vectors, which ensure their robust existence and govern their generation, evolution, and annihilation. Our findings connect robust BICs in photonics to a wide range of topological physical phenomena.

DOI: 10.1103/PhysRevLett.1.13.257401

PACS numbers: 78.67.-n, 42.70.Qs, 42.79.-e

Bound states in the continuum (BICs) are unusual solutions of wave equations describing light or matter: they are discrete and spatially bounded, but exist at the same energy as a continuum of states which propagate to infinity. Until recently, BICs were constructed through fine-tuning parameters in the wave equation [1-8] or exploiting the separability of the wave equation due to symmetry [9-13]. More recently, BICs in periodic extended structures (different from the original proposal of BICs [14]) that are both robust and not symmetry protected ("accidental") have been predicted [15-20] and experimentally realized [20]; the simplest such system is a periodic dielectric slab [20], which also has symmetry-protected BICs. Here we show that both types of BICs in such systems are vortex centers in the polarization direction of far-field radiation. The robustness of these BICs is due to the existence of conserved and quantized topological charges, defined by the number of times the polarization vectors wind around the vortex centers. Such charges can only be generated or annihilated by making large changes in the system parameters, and then only according to strict rules, which we derive and test numerically. Our results imply that laser emission based on such states will generate vector beams [21].

These BICs exist in photonics crystal slabs, which are dielectric slabs with a periodic modulation of refractive index at the wavelength scale [22] surrounded by air or a low-index medium. Photonic crystal slabs are used in many applications including surface-emitting lasers [23], photovoltaics [24], LEDs [25], and biosensing [26-28]. The periodic modulation alters the dispersion relation of light in the slabs and gives rise to photonic bands, analogous to electronic band structures in solids. In general, light can escape from the surface of the slab and propagate to the far field, but for a portion of the photonic band (that is "below the light line") light is perfectly confined to the slab by the generalized form of total internal reflection [22]. In contrast, modes above the light line appear generically as

resonances with finite lifetimes due to their coupling to the continuum of extended modes [29]. It has been known for some time that bound states with infinite lifetimes also exist above the light line at isolated high-symmetry wave vectors. This type of BIC arises from the symmetry mismatch between their mode profiles inside the photonic crystal and those of the external propagating modes (radiation continuum) [13,29-31]. Recently, a new type of BIC, unprotected by symmetry, has been found (both theoretically and experimentally) to exist at arbitrary wave vectors in bands above the light line in photonic crystal slabs [20]. These BICs occur accidentally when the relevant couplings to the continuum (see below) all vanish simultaneously. However, their existence does not require fine-tuning of system parameters; small changes in parameters simply shift the position of these special points along the band diagram. An intuitive understanding of why such BICs exist and are robust was previously lacking. Recently, an explanation based on accidental triangular symmetry of the radiating fields was proposed [32] but does not explain the robustness of these BICs and their occurrences in TE-like bands.

We now show that both types of BICs in photonic crystal slabs are vortex centers in the polarization direction of the far-field radiation. Using the Bloch theorem for photonic crystals [22], we write the electric field of a resonance as  $\mathbf{E}_{\mathbf{k}}(\pmb {\rho},z) = e^{i\mathbf{k}\cdot \pmb{\rho}}\mathbf{u}_{\mathbf{k}}(\pmb {\rho},z)$ , where  $\mathbf{k} = k_{x}\hat{x} +k_{y}\hat{y}$  is the two-dimensional wave vector,  $\pmb {\rho} = x\hat{x} +y\hat{y}$  is the in-plane coordinate,  $\mathbf{u}_{\mathbf{k}}$  is a periodic function in  $\pmb{\rho}$ , and  $z$  is the normal direction to the slab. While the fields inside the slab are periodically modulated, outside the slab each state consists of propagating plane waves and/or evanescent waves that decay exponentially away from the surface. For states above the light line (resonances), and wavelengths below the diffraction limit, the only nonzero propagating-wave amplitudes are the zero-order (constant in-plane) Fourier coefficients of  $\mathbf{u}_{\mathbf{k}}$ , given by  $\mathbf{c}(\mathbf{k}) = c_x(\mathbf{k})\hat{x} +c_y(\mathbf{k})\hat{y}$  [Fig. 1(a)]. Here,  $c_{x}(\mathbf{k}) = \hat{x}\cdot \langle \mathbf{u}_{\mathbf{k}}\rangle$

![](images/76b74349f796a391df12098ddfb58a8c5da99b4ad9e18d9a8d800a8aa20bde19.jpg)  
(a) Field decomposition

![](images/627b5d1bdd83867bd34e596112371d867f1c3229188048773fa63cfc4455e27c.jpg)  
(b) Polarization vortex

![](images/a6a7b3f64dc2581226d8013c09e007ab49be5110ea9508dde6b564cd4aba2048.jpg)  
(c) Topological charge,  $q$

![](images/7d478acb97e5c4308c043a2160cc76e0a798b670832aa6dee64c0f76b44b0c9b.jpg)  
FIG. 1 (color online). Stable bound states in the continuum as vortex centers of polarization vectors. (a) Schematics of radiation field decomposition for resonances of a slab structure. The spatially averaged Bloch part of the electric field  $\langle \mathbf{u}_{\mathbf{k}}\rangle$  is projected onto the  $x - y$  plane as the polarization vector  $\mathbf{c} = (c_x, c_y)$ . A resonance turns into a BIC if and only if  $c_x = c_y = 0$ . (b) Schematic illustration for the nodal lines of  $c_x$  (green) and of  $c_y$  (red) in a region of  $\mathbf{k}$  space near a BIC. The direction of vector  $\mathbf{c}$  (shown in arrows) becomes undefined at the nodal line crossing, where a BIC is found. (c) Two possible configurations of the polarization field near a BIC. Along a closed loop in  $\mathbf{k}$  space containing a BIC (loop goes in counterclockwise direction,  $1 \rightarrow 2 \rightarrow 3 \rightarrow 4$ ), the polarization vector either rotates by angle  $2\pi$  (denoted by topological charge  $q = +1$ ) or rotates by angle  $-2\pi$  (denoted by topological charge  $q = -1$ ). Different regions of the  $\mathbf{k}$  space are colored in four gray-scale colors according to the signs of  $c_x$  and  $c_y$ . In this way, a BIC happens where all four gray-scale colors meet, and charge  $q = +1$  corresponds to the color changing from white to black along the counterclockwise loop  $C$ , and charge  $q = -1$  corresponds to the color changing from black to white.

$c_{y}(\mathbf{k}) = \hat{y}\cdot \langle \mathbf{u}_{\mathbf{k}}\rangle$  , and the brackets denote the spatial average over one unit cell on any horizontal plane outside the slab. Note that  $\mathbf{c}(\mathbf{k})$  is the projection of  $\langle \mathbf{u}_{\mathbf{k}}\rangle$  onto the  $x - y$  plane; it points in the polarization direction of the resonance in the far field, so we refer to  $\mathbf{c}(\mathbf{k})$  as the "polarization vector."

A resonance turns into a BIC when the outgoing power is zero, which happens if and only if  $c_{x} = c_{y} = 0$ . In general,  $c_{x}$  and  $c_{y}$  are both complex functions of  $\mathbf{k}$ , and varying the wave vector components  $(k_{x}, k_{y})$  is not sufficient to guarantee a solution where  $c_{x} = c_{y} = 0$ . However, when the Hermitian system is invariant under the operation  $C_2^z T$ , implying that  $\epsilon(x, y, z) = \epsilon^*(-x, -y, z)$ , we show that  $c_{x}$  and  $c_{y}$  can be chosen to be real numbers simultaneously; in other words, the far field is linearly polarized (see Supplemental Material [33]). Here  $C_2^z$  is a  $180^\circ$  rotation operator around the  $z$  axis, and  $T$  is the time reversal operator. When the system also has up-down mirror symmetry  $(\sigma_z)$ , the outgoing waves on one side of the slab determine those on the other; for such Hermitian systems, BICs are stable because they correspond to the intersections between the nodal line of  $c_{x}$  and the nodal line of  $c_{y}$  in the  $k_{x} - k_{y}$  plane. Such a nodal intersection naturally causes a vortex in the polarization vector field centered on the BIC, as illustrated in Fig. 1(b), for the simplest case. Along the nodal line of  $c_{x}$  (or  $c_{y}$ ), the direction of  $\mathbf{c}(\mathbf{k})$  is along the  $y$  axis (or  $x$  axis), as illustrated in Fig. 1(b). As one encircles the nodal intersection (BIC) in the  $k_{x} - k_{y}$  plane

each component of the polarization vector flips sign as its nodal line is crossed so as to create a net circulation of  $\pm 2\pi$  in the polarization field. At the nodal intersection the polarization direction becomes undefined, since at the BIC there is zero emission into the far field. Conversely, one could say that BICs cannot radiate because there is no way to assign a far-field polarization that is consistent with neighboring  $\mathbf{k}$  points. Thus, robust BICs are only possible when there is vorticity in the polarization field.

Vortices are characterized by their topological charges. Here, the topological charge  $(q)$  carried by a BIC is defined as

$$
q = \frac {1}{2 \pi} \oint_ {C} d \mathbf {k} \cdot \nabla_ {\mathbf {k}} \phi (\mathbf {k}), \qquad q \in \mathbb {Z}, \qquad (1)
$$

which describes how many times the polarization vector winds around the BIC. Here,  $\phi (\mathbf{k}) = \arg [c_x(\mathbf{k}) + ic_y(\mathbf{k})]$  is the angle of the polarization vector, and  $C$  is a closed simple path in  $k$  space that goes around the BIC in the counterclockwise direction. The fields  $\mathbf{u_k}$  are chosen to be smooth functions of  $\mathbf{k}$ , so  $\phi (\mathbf{k})$  is differentiable in  $\mathbf{k}$  along the path. The polarization vector has to come back to itself after the closed loop, so the overall angle change must be an integer multiple of  $2\pi$ , and  $q$  must be an integer. Figure 1(c) shows examples of how the polarization vector winds around a BIC with charge  $q = +1$  and also around a BIC with charge  $q = -1$  along a loop  $C$  marked by  $1\rightarrow 2\rightarrow 3\rightarrow 4\rightarrow 1$ . Similar

definitions of winding numbers can be found in describing topological defects [34] of continuous two-dimensional spins, dislocations in crystals, and quantized vortices in helium II [35]. This formalism describing polarization vortices is also closely related to Berry phases in describing adiabatic changes of polarization of light [36,37] and Dirac cones in graphenes [38].

Lasing emission through BICs are naturally vector beams [21] (see Supplemental Material [33]), where the polarization of the outgoing beam has a spatial twist around the center. The order number of the vector beam is given by the topological charge of the BIC.

In the example of Fig. 2, we show the topological charges of BICs for a structure that has been experimentally realized in Ref. [20]. In this example, there are five BICs on the lowest-frequency TM-like band as shown in Fig. 2(a). Details about numerical simulation are provided in the Supplemental Material [33]. The mode profiles of the  $\mathbf{E}_z$  component for two BICs are shown in Fig. S1 showing localization in the  $z$  direction. We numerically calculate polarization vectors  $\mathbf{c}(\mathbf{k})$  [39], which reveal five vortices with topological charges of  $\pm 1$  at these five  $k$  points [Fig. 2(b)]. The BICs and their topological charges can also be identified from the nodal-line crossings and the gray-scale colors of  $c_x$  and  $c_y$  [Fig. 2(c)].

The winding number of the polarization vector along a closed path is given by the sum of the topological charges carried by all BICs enclosed within this path [34]. When system parameters vary continuously, the winding number defined on this path remains invariant, unless there are BICs crossing the boundary. Therefore, topological charge is a conserved quantity. This conservation rule leads to restrictions on the behaviors of BICs (see Supplemental Material [33]). For example, as long as the Hermitian system retains  $C_2^z T$  and  $\sigma_z$  symmetries (Fig. S2), a BIC can only be destroyed through annihilation with another BIC of the exact opposite charge, or through bringing it outside of the continuum (below the light line).

The conservation of topological charges allows us to predict and understand the behaviors of BICs when the parameters of the system are varied over a wide range. First, consider the lowest-frequency TM-like mode  $(\mathrm{TM}_1$  band) of a 1D-periodic structure in air shown in Fig. 3(a). This grating consists of a periodic array of dielectric bars with periodicity of  $a$ , width  $w = 0.45a$ , and refractive index  $n = 1.45$ . Its calculated band structure is shown in Fig. 3(b). When the thickness of the grating is  $h = 1.50a$ , there are two BICs on the  $k_x$  axis, as indicated by the radiative quality factor of the resonances [Fig. 3(c)]. The polarization vector  $\mathbf{c}(\mathbf{k})$ , also shown in Fig. 3(c), characterizes both BICs as carrying charges  $q = +1$ . When the grating thickness is decreased to  $h / a = 1.43$  (all other parameters fixed), the two BICs move towards the center of the Brillouin zone, meet at the  $\Gamma$  point, and deflect onto the  $k_y$  axis [Fig. 3(d)]. This is inevitable due to the conservation of the topological charges: annihilation cannot happen between two BICs of the same charge.

Annihilation of BICs is only possible when charges of opposite signs are present. This can be seen in the lowest-frequency TE-like band of the same structure [Figs. 3(e) and 3(f)]. When  $h / a = 1.04$ , there are two off-Γ BICs with charge -1 and a BIC with charge +1 at the Γ point [Fig. 3(e)]. As  $h / a$  decreases, the two -1 charges move to the center and eventually annihilate with the +1 charge, leaving only one BIC with charge  $q = -1$  [Fig. 3(f)].

Generation of BICs is also restricted by charge conservation, and can be understood as the reverse process of charge annihilation. We provide an example by considering the lowest-frequency TE-like mode in a photonic crystal slab of  $n = 3.6$  with a square lattice of cylindrical air holes of diameter  $d = 0.5a$  (Fig. S3(a) in the Supplemental Material [33]). As the slab thickness increases, BICs are generated at the  $\Gamma$  point. Each time, four pairs of BICs with exact opposite charges are generated, consistent with charge conservation and  $C_{4v}$  symmetry of the structure. With further increases of the slab thickness, the eight BICs move

![](images/89044f7525efd6b2c1dba6e3b5dd63af001519bd0046c8cfbe867866877bbe69.jpg)  
FIG. 2 (color online). Characterization of BICs using topological charges. (a) Calculated radiative quality factor  $Q$  of the  $\mathrm{TM}_1$  band on a square-lattice photonic crystal slab (as in Ref. [20]), plotted in the first Brillouin zone. Five BICs can be seen. (b) Directions of the polarization vector field reveal vortices with topological charges of  $\pm 1$  at each of the five  $k$  points. The area shaded in blue indicates modes below the light line and thus bounded by total internal reflection. (c) Nodal lines and gray-scale colors of the polarization vector fields [same coloring scheme as in Fig. 1(c)].

![](images/8a6016857737b71d328b0ce6237c9c24aa83ed4dde8261eb531dabb0759152e3.jpg)

![](images/8bb7d849f71ade3abfd0e4a56dc7a2b1368d7b7bc4d761041bc8920a2d1cd768.jpg)

![](images/505e149b0ebc3ca08ae58633a35d916cd2d4270a2a85bebe81758024f9abb68e.jpg)

![](images/7d3a206b696bbc36139707a303a1e0150b3d67f4fd7ebdfd6799c92576873b24.jpg)

![](images/f707d26a9bbabf1a1cf938da2d8f7d7d1cb00478171ef4e49cf1bd6e8ddbc186.jpg)  
FIG. 3 (color online). Evolution of BICs and conservation of topological charges. (a) Schematic drawing of a photonic crystal slab with one-dimensional periodicity in  $x$  and is infinitely long in  $y$ . (b) Calculated TM-like band structure along  $k_{x}$  axis and along  $k_{y}$  axis. The area shaded in yellow indicates the light cone, where there is a continuum of radiation modes in the surrounding medium. (c),(d) An example showing topological charges with the same sign bouncing off each other. As the slab thickness  $h$  decreases, the two BICs with charge  $+1$  move along the  $k_{x}$  axis, meet at the origin, and then deflect onto the  $k_{y}$  axis. This can be understood from the conservation of topological charges or from the evolution of nodal lines. (c),(d) An example of topological charge annihilation happening on the lowest-frequency TE-like band of the same structure with different slab thicknesses. As the slab thickness  $h$  decreases, two BICs with charge  $-1$  meet with a BIC with charge  $+1$  at the origin. These three BICs annihilate to yield one BIC with charge  $-1$ , as governed by charge conservation.

outward along high-symmetry lines and eventually go outside of the continuum (fall below the light line).

Although the examples discussed so far only show topological charges of  $\pm 1$ , other values of charges can be found in higher-frequency bands of the PhC or in structures with higher rotational symmetry. For example, Fig. S4 shows a stable BIC of charge  $-2$  at the  $\Gamma$  point arising from the double degeneracy of nodal lines caused by the  $C_{6v}$  symmetry of the system.

The symmetries of the system also restrict the possible values of topological charges, since the nodal curves must respect the point symmetry. BICs at  $\mathbf{k}$  points related by inplane point-group symmetries of the system (mirror reflections and rotations) have the same topological charges (see Supplemental Material [33]). Using a similar method, all possible charges at the  $\Gamma$  point on a nondegenerate band of any system with  $C_n$  symmetry are given in Table S1. This is consistent with all examples in this Letter. This table can be used to predict the charges in other systems of interest and to design high order vector beams.

In conclusion, we have demonstrated that BICs in photonic crystal slabs are associated with vortices in the polarization field and explained their robustness in terms of conserved topological charges. We derive the symmetries that constrain these charges and explain their generation, evolution, and annihilation. We conjecture that most robust BICs [9,12,13,16-20] will correspond to topological defects in appropriate parameter spaces. Our finding connects electromagnetic BICs to a wide range of physical phenomena including Berry phases around Dirac points [37,38], topological defects [34], and general vortex physics [35]. Optical BICs in photonic crystals have a wealth of applications. Lasing action can naturally occur at BIC states where the quality factor diverges. The angular (wave vector) tunability of the BICs makes them great candidates for on-chip beam steering [40]. Furthermore, photonic crystal lasers through BICs are naturally vector beams [41,42,43], which are important for particle accelerations, optical trapping, and stimulated emission depletion microscopy.

The authors thank Chong Wang, Scott Skirlo, David Liu, Fan Wang, Nicholas Rivera, Dr. Ido Kaminer, Dr. Homer Reid, Professor Xiaogang Wen, Professor Steven G. Johnson, and Professor John D. Joannopoulos for helpful discussions. This work was partly supported by the Army Research Office through the Institute for Soldier Nanotechnologies under Contract No. W911NF-07-D0001. B. Z., L. L., and M. S. were partly supported by Solid State Solar Thermal Energy Center (S $^3$ TEC), an Energy Frontier Research Center funded by the U.S. Department of Energy under Grant No. DE-SC0001299. L. L. was supported in part by the Materials Research Science and Engineering Center of the National Science Foundation (Grant No. DMR-0819762). A. D. S. was partly supported by NSF Grant No. DMR-1307632. B. Z. and C. W. H. contributed equally to this work.

*bozhen@mit.edu  
[1] J. von Neumann and E. Wigner, Phys. Z. 30, 465 (1929).  
[2] H. Friedrich and D. Wintgen, Phys. Rev. A 32, 3231 (1985).  
[3] E. N. Bulgakov and A. F. Sadreev, Phys. Rev. B 78, 075105 (2008).  
[4] M. I. Molina, A. E. Miroshnichenko, and Y. S. Kivshar, Phys. Rev. Lett. 108, 070401 (2012).  
[5] G. Corrielli, G. Della Valle, A. Crespi, R. Osellame, and S. Longhi, Phys. Rev. Lett. 111, 220403 (2013).  
[6] S. Weimann, Y. Xu, R. Keil, A. Miroshnichenko, A. Tünnermann, S. Nolte, A. Sukhorukov, A. Szameit, and Y. Kivshar, Phys. Rev. Lett. 111, 240403 (2013).  
[7] M. G. Silveirinha, Phys. Rev. A 89, 023813 (2014).  
[8] F. Monticone and A. Alù, Phys. Rev. Lett. 112, 213903 (2014).  
[9] D. V. Evans, M. Levitin, and D. Vassiliev, J. Fluid Mech. 261, 21 (1994).  
[10] S. P. Shipman and S. Venakides, Phys. Rev. E 71, 026611 (2005).  
[11] N. Moiseyev, Phys. Rev. Lett. 102, 167404 (2009).  
[12] Y. Plotnik, O. Peleg, F. Dreisow, M. Heinrich, S. Nolte, A. Szameit, and M. Segev, Phys. Rev. Lett. 107, 183901 (2011).  
[13] J. Lee, B. Zhen, S.-L. Chua, W. Qiu, J. D. Joannopoulos, M. Soljacic, and O. Shapira, Phys. Rev. Lett. 109, 067401 (2012).  
[14] BICs in the original proposal [1] are spatially bounded in all three dimensions and therefore integrable in the whole three-dimensional space. On the other hand, BICs in periodic extended structures are Bloch eigenstates: they are extended in the direction(s) where the system is periodic, but spatially confined in all other directions. Therefore, BICs in periodic extended structures are integrable within one unit cell instead of the whole space. These states, which are the focus of this Letter, are essentially resonances with zero linewidths and infinitely long lifetimes.  
[15] G. I. Stegeman, J. Appl. Phys. 47, 1712 (1976).  
[16] R. Porter and D. Evans, Wave Motion 43, 29 (2005).  
[17] D.C. Marinica, A.G. Borisov, and S.V. Shabanov, Phys. Rev. Lett. 100, 183902 (2008).  
[18] V. Liu, M. Povinelli, and S. Fan, Opt. Express 17, 21897 (2009).  
[19] C.W. Hsu, B. Zhen, S.-L. Chua, S.G. Johnson, J.D. Joannopoulos, and M. Soljačić, Light Sci. Appl. 2, e84 (2013).  
[20] C.W. Hsu, B. Zhen, J. Lee, S.-L. Chua, S.G. Johnson, J.D. Joannopoulos, and M. Soljačić, Nature (London) 499, 188 (2013).  
[21] Q. Zhan, Adv. Opt. Photonics 1, 1 (2009).  
[22] J. D. Joannopoulos, S. G. Johnson, J. N. Winn, and R. D. Meade, 2nd ed. Photonic Crystals: Molding the Flow of Light (Princeton University Press, Princeton, NJ, 2008).  
[23] K. Hirose, Y. Liang, Y. Kurosaka, A. Watanabe, T. Sugiyama, and S. Noda, Nat. Photonics 8, 406 (2014).

[24] D.-H. Ko, J.R. Tumbleston, L. Zhang, S. Williams, J.M. DeSimone, R. Lopez, and E.T. Samulski, Nano Lett. 9, 2742 (2009).  
[25] J. J. Wierer, A. David, and M. M. Megens, Nat. Photonics 3, 163 (2009).  
[26] N. Ganesh, W. Zhang, P. C. Mathias, E. Chow, J. A. N. T. Soares, V. Malyarchuk, A. D. Smith, and B. T. Cunningham, Nat. Nanotechnol. 2, 515 (2007).  
[27] A. A. Yanik, A. E. Cetin, M. Huang, A. Artar, S. H. Mousavi, A. Khanikaev, J. H. Connor, G. Shvets, and H. Altug, Proc. Natl. Acad. Sci. U.S.A. 108, 11 784 (2011).  
[28] B. Zhen, S.-L. Chua, J. Lee, A. W. Rodriguez, X. Liang, S. G. Johnson, J. D. Joannopoulos, M. Soljacic, and O. Shapira, Proc. Natl. Acad. Sci. U.S.A. 110, 13711 (2013).  
[29] S. Fan and J. D. Joannopoulos, Phys. Rev. B 65, 235112 (2002).  
[30] V. Pacradouni, W. Mandeville, A. Cowan, P. Paddon, J. Young, and S. Johnson, Phys. Rev. B 62, 4204 (2000).  
[31] T. Ochiai and K. Sakoda, Phys. Rev. B 63, 125107 (2001).  
[32] Y. Yang, C. Peng, Y. Liang, Z. Li, and S. Noda, Phys. Rev. Lett. 113, 037401 (2014).  
[33] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.113.257401 for (A) Numerical methods and setups; (B) Symmetry requirements for stable BICs; (C) BICs and vector beams; (D) Conservation of topological charges; (E) Example of charge -2; (F) BICs related to point group symmetries have the same topological charges; (G) Allowed charges at the center of the Brillouin zone. They are mostly providing detailed information, proofs, and examples for the claims made in the main text.  
[34] N. D. Mermin, Rev. Mod. Phys. 51, 591 (1979).  
[35] R. J. Donnelly, Quantized Vortices in Helium II (Cambridge University Press, Cambridge, England, 1991), Vol. 2.  
[36] M. Berry, J. Mod. Opt. 34, 1401 (1987).  
[37] L. Lu, J. D. Joannopoulos, and M. Soljacic, Nat. Photonics 8, 821 (2014).  
[38] J. L. Manes, F. Guinea, and M. A. H. Vozmediano, Phys. Rev. B 75, 155424 (2007).  
[39] A. F. Oskooi, D. Roundy, M. Ibanescu, P. Bermel, J. D. Joannopoulos, and S. G. Johnson, Comput. Phys. Commun. 181, 687 (2010).  
[40] Y. Kurosaka, S. Iwahashi, Y. Liang, K. Sakai, E. Miyai, W. Kunishi, D. Ohnishi, and S. Noda, Nat. Photonics 4, 447 (2010).  
[41] S. Iwahashi, Y. Kurosaka, K. Sakai, K. Kitamura, N. Takayama, and S. Noda, Opt. Express 19, 11 963 (2011).  
[42] K. Kitamura, K. Sakai, N. Takayama, M. Nishimoto, and S. Noda, Opt. Lett. 37, 2421 (2012).  
[43] K. Sakoda, Optical Properties of Photonic Crystals (Springer, New York, 2005), Vol. 80.