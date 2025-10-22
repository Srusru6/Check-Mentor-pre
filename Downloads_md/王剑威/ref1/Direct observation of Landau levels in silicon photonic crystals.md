# Direct observation of Landau levels in silicon photonic crystals

Received: 6 June 2023

Accepted: 20 March 2024

Published online: 23 April 2024

![](images/87b07e3c8aa7e17224a4c586094a3e92451a1592d58a2491da56cc67c3d3f24f.jpg)

Check for updates

Maria Barsukova  $^{1,6}$ , Fabien Grise  $^{2,6}$ , Zeyu Zhang  $^{1,6}$ , Sachin Vaidya  $^{1,3}$ , Jonathan Guglielmon $^{1}$ , Michael I. Weinstein $^{4}$ , Li He  $^{5}$ , Bo Zhen  $^{5}$ , Randall McEntaffer  $^{2}$  & Mikael C. Rechtsman  $^{1}$

When electrons are confined to a two-dimensional plane and are subjected to an out-of-plane magnetic field, they move in circular cyclotron orbits as a result of the Lorentz force. In the quantum domain, this cyclotron motion is quantized, and as a consequence, the energy spectrum of the electrons splits into discrete, highly degenerate states called Landau levels. These flat bands are the origin of the integer and fractional quantum Hall effects<sup>1,2</sup>. Although photons do not experience the Lorentz force because they do not carry charge, they can be made to experience 'pseudomagnetic fields'<sup>3,4</sup> as a result of periodicity-breaking strain. In this work, we experimentally observe photonic Landau levels that arise due to a strain-induced pseudomagnetic field in a silicon photonic crystal slab. The Landau levels are dispersive (that is, they are not flat bands) due to the distortion of the unit cell by the strain. We employ an additional strain of a different form that induces a pseudoelectric potential to flatten them. By acting akin to cavities that are delocalized across space, flat bands such as these have the potential to strongly enhance light-matter interaction as a result of the photonic structure. The analytical framework that we develop here for understanding the effects of inhomogeneous strain in photonic crystals via gauge fields can help to guide the design of multiscale non-periodic photonic structures.

Although light may respond to external magnetic fields when propagating in magneto-optical materials, this response is typically very weak. An approach was put forward for emulating magnetic behaviour in photonic systems (while maintaining reciprocity) by inhomogeneously constraining a photonic lattice<sup>4</sup>. This implementation was based on an idea proposed for electrons in graphene, where a strain pattern imposed on the lattice would introduce an effective gauge field at the Dirac point, causing electrons to behave as though there were a strong field present, even in the absence of a real magnetic field<sup>3</sup>. The effect was later demonstrated by directly observing Landau levels in graphene bubbles, where a strain corresponding to an enormous pseudomagnetic field of 300 T was imposed<sup>5</sup>. Since the original photonic experiment, Landau

levels were also proposed and observed in twisted optical cavities<sup>6</sup>, exciton-polariton condensates<sup>7</sup> and mechanical systems<sup>8-10</sup>. Moreover, there have been a number of theoretical proposals for how Landau levels may be used in the context of photonics that are intrinsically distinct from the electronic case<sup>11,12</sup>.

Here we directly observe Landau levels in two-dimensional silicon photonic crystal slabs in the nanophotonic domain (Fig. 1 shows a schematic of the associated strain and the effect on the photonic crystal band structure). Moreover, we go beyond purely pseudomagnetic effects and demonstrate that strains corresponding to pseudoelectric fields act to flatten the Landau levels that inherit dispersion from the form of the pseudomagnetic strain. There are several key

$^{1}$ Department of Physics, The Pennsylvania State University, State College, PA, USA.  $^{2}$ Department of Astronomy & Astrophysics, The Pennsylvania State University, State College, PA, USA.  $^{3}$ Department of Physics, Massachusetts Institute of Technology, Cambridge, MA, USA.  $^{4}$ Department of Applied Physics and Applied Mathematics and Department of Mathematics, Columbia University, New York, NY, USA.  $^{5}$ Department of Physics and Astronomy, University of Pennsylvania, Philadelphia, PA, USA.  $^{6}$ These authors contributed equally: Maria Barsukova, Fabien Grise, Zeyu Zhang.  $^{\text{e}}$ -mail: mcrworld@psu.edu

![](images/806aeef6f08ae3ea855500a239fae309f290f11367b980bca87a33a405117992.jpg)

![](images/33daa2be880786e467b274ab4c5958e696643e7d05afcdd2de54fd76fd3c7469.jpg)

![](images/d39fc2893d51da89d5ae4c43af0716b7c1baf8477ec4f2bde3c5bb19ef6e7cb2.jpg)  
Fig. 1 | Schematic illustrating the effect of strain on the Dirac cone. The data are obtained from equation (1). a,b, Unstrained (a) and strained (b) honeycomb lattice. The purple arrows indicate the direction of deformation of the lattice. c, Band structure in the vicinity of the Dirac cone in the unstrained case corresponding to a. d, Strain results in the spectrum breaking up into Landau levels that are spaced as  $\sqrt{n}$ , where  $n$  is an integer. Here  $\Delta \omega$  is the difference in frequency between the zeroth and first Landau levels,  $\omega_{\mathrm{D}}$  is the Dirac frequency and  $(k_x, k_y)$  is the in-plane Bloch wavevector.

![](images/026b10efead5208c77b8ebe39939621ccada2f908916b470cf070064834ccbee.jpg)

differences and advantages of pseudomagnetism in photonic crystals compared with previous realizations of photonic pseudomagnetism. Photonic crystals are known to enhance light-matter interaction via cavity modes and flat bands $^{13,14}$ ; recent work has shown that such flat bands strongly enhance the interaction between photonic and electronic states, resulting in an increase in Smith-Purcell radiation by orders of magnitude $^{15}$ . A similar mechanism also holds promise for potential applications in nanophotonic scintillators used in particle accelerators, as well as for medical imaging $^{16}$ . Moreover, because Landau-gauge eigenstates are one-dimensional waveguide-like states (since they are confined in all dimensions but one, unlike Bloch states of two-dimensional photonic crystals), and have a low group velocity, they may be used for slow-light applications $^{17}$ . Importantly, in the photonic crystal case, flat-band enhancement is generated as a result of the lattice itself, rather than separately from the constituent sites. In contrast, for systems composed of individual, isolated guiding or resonant elements $^{4,7}$ , lattice effects are not leveraged because strong enhancement would occur even in a single site. Second, besides having unit cells that are an order of magnitude smaller, photonic crystals can, in practice, have much larger system sizes compared with previous realizations (millions versus hundreds of unit cells), and can be realized with a smaller loss in the silicon platform. Since Landau-level degeneracy scales with the system size and the linewidth increases with loss, photonic crystals allow for increased degeneracy and improved spectral resolution of the levels.

Further, since photonic crystals do not have an associated tight-binding theory, the original theoretical framework relating strain to pseudomagnetism is not directly applicable, necessitating a new understanding; the appropriate effective Hamiltonians and strain-dependent emergent parameters for two-dimensional photonic crystals were derived in our previous theoretical work $^{18}$ , and are extended to the slab geometry here (two-dimensional slab embedded in three-dimensional space). Our establishment of a new analytical method of understanding and describing aperiodicity in photonic crystals (that is, using pseudomagnetic fields) will be useful in their

optimization for many different functions; this has traditionally been approached by using direct brute-force numerical optimization[19-21].

Our starting point is a photonic crystal structure consisting of rounded triangular air holes in a silicon slab[22] that rests on a silica substrate. The holes form an underlying honeycomb pattern with  $C_{6v}$  symmetry. As a result, this lattice hosts Dirac points at the  $\mathbf{K}$  and  $\mathbf{K}'$  points in the Brillouin zone[23-25]. As these Dirac points lie below the light line of a vacuum, they are not detectable via free-space excitation. To allow radiative coupling from outside the slab, we introduce a small period-doubling perturbation by changing the size of some of the holes (Supplementary Section 2). This makes the unit cell of the lattice rectangular, and the band structure is folded such that the Dirac cone resides along the  $k_{x}$  axis and lies above the light line of vacuum. Importantly, we choose our period doubling in a way that respects inversion symmetry and thus will not cause the Dirac cone to be gapped. A scanning electron microscopy (SEM) image of the structure is shown in Fig. 2a; the period-doubled unit cell is shaded in purple.

We numerically compute the band structure (in the transverse-electric polarization) using the guided-mode expansion method as implemented in the open-source software package LEG-UME $^{26}$ . Figure 2b shows the linearly dispersing transverse-electric-like bands that exhibit a Dirac point at  $\mathbf{K}$ , with frequency  $\omega_{\mathrm{D}} = 0.318(2\pi ca^{-1})$ . Here  $a$  is the lattice constant of the underlying hexagonal lattice structure and  $c$  is the speed of light. The period-doubling procedure very slightly changes the Dirac frequency (Supplementary Section 2).

Next, we introduce a strain pattern in our structure by deforming the lattice (Fig. 2c). Here the term strain refers not to a strain induced by a physically applied stress but to the deformation of the dielectric pattern that is directly etched into the silicon. The specific strain pattern is achieved by mapping every point  $(x,y,z)$  to  $(x,y + a(\kappa x)^2,z)$ , where  $\kappa$  is the strength of the strain. This deformation breaks the periodicity in the  $x$  direction, but retains periodicity along the  $y$  direction. The spatial-scale separation ensured by the assumption of small and slowly varying strain, that is,  $\kappa a\ll 1$ , allows us to develop a multiple-scale variant of degenerate perturbation theory to expand the eigenstates and eigenvalues of the strained system. The eigenstates are—to a leading order in  $\kappa$ —a slow spatial modulation of the degenerate Bloch modes associated with the Dirac point of the unstrained  $(\kappa = 0)$  structure.

The resulting effective Hamiltonian, which incorporates the strain, is given by

$$
\mathcal {H} _ {\mathrm {e f f}} = E _ {\mathrm {D}} \sigma_ {0} + v _ {\mathrm {D}} \left[ \left(- \mathrm {i} \frac {\partial}{\partial x}\right) \sigma_ {1} + \left(- \mathrm {i} \frac {\partial}{\partial y} + \frac {4 a b _ {*} \kappa^ {2}}{v _ {\mathrm {D}}} x\right) \sigma_ {2} \right], \tag {1}
$$

where  $E_{\mathrm{D}} = (\omega_{\mathrm{D}} / c)^{2}$ ;  $\sigma_0, \sigma_1$  and  $\sigma_2$  are Pauli matrices; and  $\nu_{\mathrm{D}} = 0.915a^{-1}$  and  $b_* = 0.606a^{-2}$  are two parameters calculated from the modes of the unstrained structure at energy  $E_{\mathrm{D}}$ . Supplementary Section 3 provides a detailed derivation, where explicit expressions for  $b_*$  and  $\nu_{\mathrm{D}}$  in terms of the eigenstates of the periodic structure are displayed. We note that the effective Hamiltonian displayed in equation (1) is directly derived from the continuum theory of photonic crystals; this is fundamentally different from previous work<sup>3</sup> based on the tight-binding approximation. Our approach extends the methods from another work<sup>18</sup> to the three-dimensional setting of the slab geometry, where the vectorial nature of the electromagnetic fields plays a role.

Equation (1) corresponds to a two-dimensional Dirac Hamiltonian describing massless spin-1/2 relativistic particles under a constant (pseudo)magnetic field pointing in the out-of-plane direction, where the magnetic field has a strength of  $B_{\mathrm{eff}} = 4ab \cdot \kappa^2 / v_{\mathrm{D}}$  and is described by a vector potential in the Landau gauge. The discrete energies that are eigenvalues of the Hamiltonian in equation (1) for an electron are known as Landau levels. The energy eigenvalue of the nth level is proportional to  $\sqrt{|n|}$ , where  $n$  is an integer. Analogously, for our photonic crystal slabs, the frequency eigenvalues of the electromagnetic eigenmodes

![](images/27c2ad323efd83480c510a4218c8a6d022e27637fd27aa6501244354532426cf.jpg)

![](images/001b3b860edcedabb4eadb3c533de3ba4eae3861eabe889937ec750d1e295ada.jpg)  
Fig. 2 | Unstrained and strained photonic crystals and their calculated band structures. a, SEM image of the unstrained periodic photonic crystal. The primitive unit cell is highlighted in red and the period-doubled unit cell, in purple;  $a$ , the lattice constant, is indicated in white. b, Simulated band structure for the unstrained structure, based on the primitive unit cell, showing a Dirac point for the transverse-electric-like modes. The colour of the bands indicates

![](images/70e6e0d6604db6d335e95b1ee7e2c5942f97d43e5873b26d590eea2b64de7d8d.jpg)

![](images/5840c277ddd17336c69e23886cd86589a482c72b9d50c757c9c2fa8a13b6f9f6.jpg)  
the quality factors of the states. c, SEM image of the strained pattern, in which the strain causes the loss of periodicity in the  $x$  direction. The  $y$ -periodic unit cell of the strained pattern is highlighted in purple. d, Simulated band structure for the strained pattern  $(\kappa = 0.0632a^{-1})$ , showing the emergence of Landau levels in the vicinity of the Dirac frequency. Only the first 11 Landau levels ( $n = -5$  to 5) are shown.

are, to the first order in  $\kappa$ , proportional to  $\sqrt{|n|}$  and can be expressed as  $\omega_{n} = \omega_{\mathrm{D}} \pm (c^{2}v_{\mathrm{D}} / \sqrt{2}\omega_{\mathrm{D}})\sqrt{B_{\mathrm{eff}}|n|}$ , where  $n$  is an integer.

To corroborate our analytical results given in equation (1), we also perform numerical simulations of the strained structure using the guided-mode expansion method. The strain is implemented in a dielectric profile that spans 199 period-doubled unit cells in the  $x$  direction. Due to the preservation of lattice periodicity along the  $y$  direction,  $k_{y}$  is conserved and the frequencies of bands can be plotted as functions of  $k_{y}$  (Fig. 2d). Here we observe the splitting of the spectrum near the Dirac point into discrete Landau levels due to the strain-induced pseudomagnetic field, where the spacing of these levels is proportional to  $\sqrt{|n|}$  for a fixed value of  $\kappa$ .

To demonstrate the formation of Landau levels in such a system, we use electron-beam lithography to fabricate both periodic and strained patterns in a silicon slab  $(\varepsilon = 12.11)$  on top of a silica substrate  $(\varepsilon = 2.25)$ . Methods provide a detailed description of the fabrication methods. Figure 2a,c shows the SEM images of the fabricated structures. The structure shown in Fig. 2a has a periodicity of  $2a = 980$  nm along the  $x$  direction.

To experimentally characterize the photonic bands of these structures, we perform angle- and frequency-resolved reflection measurements. The samples are illuminated by a tunable continuous-wave laser (Keysight 81606A) with a wavelength range of  $\lambda = 1.45 - 1.65\mu \mathrm{m}$  ( $\pm 1.5$  pm absolute-wavelength-resolution accuracy) and a laser linewidth coherence control of  $10\mathrm{kHz}$ . We measure the iso-frequency contours of the fabricated photonic crystal slabs using back-focal-plane imaging. We then extract the Landau-level band structures by observing the photonic crystal resonances at a fixed  $k_{x}$  corresponding to the location of the Dirac point of the unstrained structure (although  $k_{x}$  is no longer a good momentum for the strained structure, a slowly varying strain primarily mixes nearby  $k_{x}$ , and hence, the Landau-level eigenstates are expected to strongly couple to the  $k_{x}$  value of the Dirac point of the unstrained structure). Supplementary Section 1 provides details of the experimental setup. All of the Landau-level states that we observe in the present work reside in the bulk; the corresponding edge states are helical because the system preserves time-reversal symmetry, and could be realized and out-coupled by introducing an appropriate confining potential.

That said, there is no sharp conceptual distinction between the bulk and edge states, particularly in the Landau gauge, since the latter can be thought of as bulk states that have been shifted into the gaps between the Landau levels by the confining potentials.

Figure 3a shows the bands of the unstrained structure, obtained by back-focal-plane imaging, where we clearly observe linearly dispersing bands near the Dirac point. We note that a very small gap is observed at the Dirac point; for graphene, any breaking of inversion symmetry necessarily gaps the Dirac point. Inevitably, a small symmetry-breaking term due to imprecision in fabrication is present and responsible for the observed gap. Supplementary Section 4 shows that the breaking of inversion symmetry affects the zeroth Landau level much more than the other levels.

Next, we measure the bands of the strained photonic crystal slabs described above and find the emergence of discrete Landau levels (Fig. 3b). Although the effective theory predicts that the Landau levels should be flat, we see that they are dispersive in both simulation (Fig. 2d) and experiment (Fig. 3b), that is, the bands are concave-up. This arises due to the fact that by adding strain, the unit cell is locally distorted as a function of  $x$ . This distortion effectively adds a parabolic potential to the Hamiltonian (that is,  $H \approx x^2 \sigma_0$ ), which, in turn, causes the dispersion of the Landau-level bands. Supplementary Section 5 provides a detailed explanation.

According to the effective theory (equation (1)), the  $n = 0$  level should be at the centre of all the Landau levels. However, due to the aforementioned inversion-symmetry breaking, this level is slightly shifted away from the centre (Supplementary Section 4). As a result, we use a new reference frequency of  $\omega_0' = \frac{1}{2} (\omega_{-1} + \omega_1)$  as the Dirac frequency to calculate the Landau-level spacings, defined as  $\omega_{n} - \omega_{0}'$ . In Fig. 3c, we compare the theoretically and experimentally obtained level spacings at  $k_{y} = 0$  under different strain strengths (characterized by  $\kappa$ ) and observe good agreement between the two. From the experimental data, we also calculate the normalized quantity  $|\omega_{n} - \omega_{0}'| / (\kappa \sqrt{|n|})$ , which should be a constant for all the Landau levels. We again observe good agreement between the experiment and the theoretically predicted value of 0.0823(2πc) (Fig. 3d). In Fig. 3c,d, the theoretical plots (solid lines) are directly obtained from analytical predictions, and have no free parameters.

![](images/e4e7f4643070fa1ddd2a0d4cbf57dc931897e456a2d927834fa1f7897c1a2905.jpg)

![](images/f702559933fdf76daab2b4cc750327ecaded4100e923529e36fee7c982103035.jpg)

![](images/824a034d75bda2ea209094066726ea4bb33462d8aedd85ed638999164394ec66.jpg)  
Fig. 3 | Observation of Landau levels in the spectrum of a strained photonic crystal. a, Experimentally measured band structure of the unstrained honeycomb pattern, showing the Dirac point in the vicinity of  $\omega_{\mathrm{D}} = 0.32(2\pi ca^{-1})$ . b, Measured band structure for the strained pattern. The uniform pseudomagnetic field created by the strain causes the Dirac point to split into sets of discrete Landau levels. Here  $\kappa = 0.0632a^{-1}$ , as in the numerical results shown in Fig. 2d. c, Landau-level energy spacing  $(\Delta \omega_{n,0} = \omega_{n} - \omega_{0}^{\prime})$  is a linear

![](images/f4f647aff40102aadea9a0e7496559131ac8abfae542fdf67e8cac153da1c654.jpg)  
function of strain strength  $\kappa$ . Note that the data used in  $\mathbf{c}$  were taken from a different sample from those of  $\mathbf{b}$ .  $\mathbf{d}$ , Landau levels lie at energies proportional to  $\sqrt{|n|}$ ; this behaviour is captured by plotting the dimensionless quantity  $\frac{|\omega_n - \omega_0'|}{\sqrt{|n|}\kappa}$  for each Landau level, including six different samples of different strain strengths  $\kappa$ . The error bars in  $\mathbf{c}$  and  $\mathbf{d}$  are defined by the linewidth of the relevant Landau level. In both  $\mathbf{c}$  and  $\mathbf{d}$ , the solid lines are the theoretical predictions with no free parameters.

From Fig. 3b, it is clear that as  $n$  decreases, the range of  $k_{y}$  values over which the  $n$ th Landau level is observed becomes smaller. This can be intuitively understood as arising from the interaction of the Landau-level states with other states that reside towards the far left and right sides of the sample. These states rise in energy as one moves away from the sample centre along the  $x$  direction. Equation (1) shows that the Landau-level states are harmonic oscillator eigenstates centred at  $x = k_{y} / B_{\mathrm{eff}}$ , with spatial widths of  $\Delta x_{n} = \sqrt{(2|n| + \delta_{0,n}) / 2B_{\mathrm{eff}}}$ . As  $k_{y}$  increases, the Landau-level centre translates and the tail of the Landau level eventually interacts with the states mentioned above, leading to an increased linewidth (Supplementary Section 3 provides additional details).

The fact that the  $x$  position of the Landau-level state linearly varies with  $k_{y}$  leads to another clear observable: when the input beam is moved from left to right in real space along the  $x$  direction, the Landau-level states at increasing  $k_{y}$  are selectively excited and therefore appear more clearly in the band structure. We directly observe this effect (Fig. 4a-c): when the input beam is on the left side of the sample (that is,  $x < 0$ ), we see that the modes on the left side of the band structure ( $k_{y} < 0$ ) are more strongly excited, but as the input beam moves rightwards, we observe that the modes on the right side of the band structure are increasingly excited.

To further study the relationship between  $x$  and  $k_{y}$ , we extract the boundary in  $k_{y}$  space between the modes that are excited and those that are not excited. For input beams positioned to the left of centre, we extract the right boundary, and for input beams positioned to the right of centre, we extract the left boundary. The boundary values differ from the effective excitation centres by an overall offset, which we remove by fitting the data to a line and subtracting the intercept (one for the left-boundary data and one for the right-boundary data; Supplementary Section 3). Using this procedure, we obtain the relationship between the Landau-level horizontal position and the vertical

momentum  $k_{y}$ . The linear relationship between these (Fig. 4d) evidences the direct proportionality between the Landau-level positions and  $k_{y}$ . Supplementary Video1 shows the evolution of the relative excitation of the Landau-level states as the beam moves from left to right.

We next turn our attention to the mitigation of the Landau-level dispersion. As explained earlier, equation (1) predicts flat Landau levels. However, in simulations and experiments, the Landau levels exhibit quadratic dispersion as  $k_{y}$  is varied. As shown in another work[18], it is possible to mitigate this dispersion by introducing an additional strain profile, which induces a pseudoelectric potential. Specifically, we add a cubic term to the deformation such that the point  $(x,y,z)$  is mapped to  $(x + a\beta (\kappa x)^3,y + a(\kappa x)^2,z)$ . The parameter  $\beta$  controls the strength of this additional strain in the  $x$  direction. A schematic of the strained structure, which induces both pseudomagnetic and pseudoelectric fields, is shown in Fig. 5a (Supplementary Section 5 provides additional details). The reason why the pseudoelectric field counters the Landau-level dispersion, to the leading order, can be explained as follows. To the leading order, the form of the pseudoelectric field gives rise to a potential  $V_{\mathrm{eff}} = 3a\beta m\kappa^3 x^2\sigma_0$  (to be added to equation (1)), which is similar to that which creates the dispersion in the first place (here  $m = -3.28a^{-2}$  is a parameter calculated entirely from the states of the periodic structure). Since the spatial positions of the Landau-level eigenstates grow linearly with  $k_{y}$ , a quadratic potential in  $x$  is equivalent to a parabolic dispersion in  $k_{y}$ . An appropriate choice of the field strength (and sign) will then counteract the original dispersion induced by the strain associated with the pseudomagnetic field.

By appropriately choosing  $\beta$ , the quadratic dispersion of the Landau levels can be mitigated, leading to nearly flat bands. We note that each Landau level requires a different value of  $\beta$  to counteract its dispersion. Supplementary Section 5 provides more details. Figure 5b shows the numerical simulations of the flattened Landau levels for a structure with pseudomagnetic and pseudoelectric fields induced by a strain with  $\kappa = 0.0632a^{-1}$  and  $\beta = 0.0364$ . Here the  $n = 0$  level is targeted, but other

![](images/4336b3f8dab51fa624606cf813242627406f91d6bcb6de7aed687b6c604247c6.jpg)

![](images/82c7c471bf990dc43831eea48be9053df9dc82d08407f8e2f4c5f5b2007580e7.jpg)

![](images/eea3c5efeb24ff67527b58b31ec9766f1a0fe02e16ef59c35c4d5ec05bba985a.jpg)

Fig. 4 | Landau levels are excited at increasing  $k_{y}$  in the band structure as the input beam moves from left to right through the sample. a-c, Experimental band structures showing the excitation of Landau levels when the beam is injected at  $x = -20\mu \mathrm{m}$  (a),  $x = 0\mu \mathrm{m}$  (b) and  $x = 20\mu \mathrm{m}$  (c). d, Centre of Landau-level excitation in  $k_{y}$  plotted against the position of the input beam  $x$ . The error  
![](images/eed157681e7a424baf78d88e18181bbd6f00f789e572c70d41bb5a084cf371c3.jpg)  
bars are defined by the uncertainty in edge position (Supplementary Section 3). The linear relationship is characteristic of Landau-level eigenstates in the Landau gauge. The solid line represents the theoretical prediction, with no free parameters.

![](images/084be176a853916c16c06f62b1444535dc7e6ed00e24bc5700d91205f4665096.jpg)

Fig. 5|Introduction of a pseudoelectric potential acts to flatten the Landau-level bands. a, Schematic depicting the strain profile that produces the pseudoelectric potential used to mitigate the Landau-level dispersion.  
![](images/8b854e36ce11c6bcef28e6050d07864ee12d69813f434986b2f957912e4b398e.jpg)  
b, Simulated band structure with  $\kappa = 0.0632a^{-1}$  and  $\beta = 0.0364$ , where the Landau level  $n = 0$  is predicted to be flattened. c, Experimental data for  $\kappa = 0.0632a^{-1}$  and  $\beta = 0.0364$ , showing the flattening of the Landau levels.

![](images/0a1ef7b04aa3dd3521bca5c0f2f19a81ad0540f71374f1aadc72c8d049768a7d.jpg)

levels are also evidently flatter. Figure 5c shows the experimental data for a strained structure with the same values of  $\kappa$  and  $\beta$  given above, where a good agreement is observed between theory and experiment.

In conclusion, we have directly observed Landau levels in the spectra of two-dimensional silicon photonic crystal slabs. As in graphene, the Landau-level energies are proportional to  $\sqrt{|n|}$ , where  $n$  is an integer. The Landau-level bands are found to be dispersive, which can be explained by a distortion of the unit cell as a result of the strain. We further showed that this dispersion can be mitigated by adding an additional strain that induces a position-dependent pseudoelectric field (that is, a potential). Landau levels constitute a new methodology for generating flat bands and thus enhancing light-matter interactions, which is distinct from standard slow light or cavity enhancement, because a flat band essentially acts as a 'cavity everywhere in space'. This realization in an on-chip photonic crystal slab geometry potentially opens the door to the use of photonic strain engineering in metasurfaces, since large angles can be accessed due to the subwavelength scale of the sites. The realization of optical pseudomagnetism prompts several new questions and directions of enquiry, including whether Landau-level flat bands (or other spectral features of aperiodic photonic

crystals more generally) can be used to enhance the light-matter coupling more efficiently than conventional photonic crystal flat bands or other points of high degeneracy (such as Van Hove singularities); the exploration of the nature of wave-mixing processes such as four-wave mixing among Landau levels, given that the Landau-level eigenstates are fundamentally different from Bloch modes, being localized in at least one direction; the interplay between disorder and pseudomagnetism in this nanophotonic context; and whether the square-root structure of the eigenvalue spacing can lead to different properties associated with an entangled pair or frequency-comb generation. More broadly, the framework of pseudomagnetism gives an analytical handle on aperiodic photonic structures, allowing for a new approach to design devices and better understanding of their behaviour.

# Online content

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41566-024-01425-y.

# References

1. Tsui, D. C., Stormer, H. L. & Gossard, A. C. Two-dimensional magnetotransport in the extreme quantum limit. Phys. Rev. Lett. 48, 1559 (1982).  
2. Klitzing, K., Dorda, G. & Pepper, M. New method for high-accuracy determination of the fine-structure constant based on quantized Hall resistance. Phys. Rev. Lett. 45, 494 (1980).  
3. Guinea, F., Katsnelson, M. I. & Geim, A. Energy gaps and a zero-field quantum Hall effect in graphene by strain engineering. Nat. Phys. 6, 30-33 (2010).  
4. Rechtsman, M. C. et al. Strain-induced pseudomagnetic field and photonic Landau levels in dielectric structures. Nat. Photon. 7, 153-158 (2013).  
5. Levy, N. et al. Strain-induced pseudo-magnetic fields greater than 300 Tesla in graphene nanobubbles. Science 329, 544-547 (2010).  
6. Schine, N., Ryou, A., Gromov, A., Sommer, A. & Simon, J. Synthetic Landau levels for photons. Nature 534, 671-675 (2016).  
7. Jamadi, O. et al. Direct observation of photonic Landau levels and helical edge states in strained honeycomb lattices. Light Sci. Appl. 9, 144 (2020).  
8. Abbaszadeh, H., Souslov, A., Paulose, J., Schomerus, H. & Vitelli, V. Sonic Landau levels and synthetic gauge fields in mechanical metamaterials. Phys. Rev. Lett. 119, 195502 (2017).  
9. Brendel, C., Peano, V., Painter, O. J. & Marquardt, F. Pseudomagnetic fields for sound at the nanoscale. Proc. Natl Acad. Sci. USA 114, E3390-E3395 (2017).  
10. Peri, V., Serra-Garcia, M., Ilan, R. & Huber, S. D. Axial-field-induced chiral channels in an acoustic Weyl system. Nat. Phys. 15, 357-361 (2019).  
11. Schomerus, H. & Halpern, N. Y. Parity anomaly and Landau-level lasing in strained photonic honeycomb lattices. Phys. Rev. Lett. 110, 013903 (2013).  
12. Lledó, C., Carusotto, I. & Szymanska, M. Polariton condensation into vortex states in the synthetic magnetic field of a strained honeycomb lattice. SciPost Phys. 12, 068 (2022).  
13. Li, J., White, T. P., OàFaolain, L., Gomez-Iglesias, A. & Krauss, T. F. Systematic design of flat band slow light in photonic crystal waveguides. Opt. Express 16, 6227-6232 (2008).  
14. Jukić, D., Buljan, H., Lee, D.-H., Joannopoulos, J. D. & Soljacic, M. Flat photonic surface bands pinned between Dirac points. Opt. Lett. 37, 5262-5264 (2012).  
15. Yang, Y. et al. Photonic flatband resonances for free-electron radiation. Nature 613, 42-47 (2023).  
16. Roques-Carmes, C. et al. A framework for scintillation in nanophotonics. Science 375, eabm9293 (2022).

17. Baba, T. Slow light in photonic crystals. Nat. Photon. 2, 465-473 (2008).  
18. Guglielmon, J., Rechtsman, M. C. & Weinstein, M. I. Landau levels in strained two-dimensional photonic crystals. Phys. Rev. A 103, 013505 (2021).  
19. Men, H., Lee, K. Y., Freund, R. M., Peraire, J. & Johnson, S. G. Robust topology optimization of three-dimensional photonic-crystal band-gap structures. Opt. Express 22, 22632-22648 (2014).  
20. Vuckovic, J., Loncar, M., Mabuchi, H. & Scherer, A. Optimization of the Q factor in photonic crystal microcavities. IEEE J. Quantum Electron. 38, 850-856 (2002).  
21. Bendsoe, M. P. & Sigmund, O. Topology Optimization: Theory, Methods, and Applications (Springer Science & Business Media, 2003).  
22. Barik, S., Miyake, H., DeGottardi, W., Waks, E. & Hafezi, M. Two-dimensionally confined topological edge states in photonic crystals. New J. Phys. 18, 113013 (2016).  
23. Neto, A. C., Guinea, F., Peres, N. M., Novoselov, K. S. & Geim, A. K. The electronic properties of graphene. Rev. Mod. Phys. 81, 109 (2009).  
24. Fefferman, C. L. & Weinstein, M. I. Honeycomb lattice potentials and Dirac points. J. Am. Math. Soc. 25, 1169-1220 (2012).  
25. Lee-Thorp, J. P., Weinstein, M. I. & Zhu, Y. Elliptic operators with honeycomb symmetry: Dirac points, edge states and applications to photonic graphene. Arch. Rational Mech. Anal. 232, 1-63 (2019).  
26. Minkov, M. et al. Inverse design of photonic crystals through automatic differentiation. ACS Photonics 7, 1729-1741 (2020).  
27. Bender, C. M. & Orszag, S. A. Advanced Mathematical Methods for Scientists and Engineers I: Asymptotic Methods and Perturbation Theory Vol. 1 (Springer Science & Business Media, 1999).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

© The Author(s), under exclusive licence to Springer Nature Limited 2024

# Methods

# Device fabrication and characterization

We employed a silicon-on-insulator wafer (SOITEC) with a thickness of  $220 \pm 10$  nm and a silica layer with a thickness of  $2,000 \pm 50$  nm. A single wafer was used for all the development, prototyping and device fabrication, and was characterized before being diced in  $2 \times 2$  cm $^2$  squares. A 25-point scan was performed using a Woollam M-2000XF-193 spectroscopic ellipsometer. The device layer was verified to be within specifications at an average of  $217.7 \pm 0.5$  nm. Each die used in this work was similarly processed: a  $2\mathrm{min}$ $\mathrm{O}_2$  plasma was performed using a Samco AQ-2000 plasma cleaner for surface preparation. A dehydration bake at  $184^{\circ}\mathrm{C}$  was performed for  $1\mathrm{min}$  and then the positive resist ZEON ZEP520A was diluted at a 2:1 ratio in anisole and was spin coated. A 2,500 r.p.m. speed yielded a consistent 300-nm-thick resist layer, which was necessary due to etching requirements. The resist was then baked at  $184^{\circ}\mathrm{C}$  for  $3\mathrm{min}$  before the sample was loaded into the electron-beam lithography tool.

Patterns were generated and fractured using a  $0.2\mathrm{nm}$  grid resolution, a beam step size of  $10.0\mathrm{nm}$ , a main-field size of  $200.00\times 200.00\mu \mathrm{m}^2$  and a subfield size of  $3.26\times 3.26\mu \mathrm{m}^2$ . The shape detection method was used with smooth shape filling and appropriate field overlaps. Field ordering was fixed, and we used fixed subfields as the method for feature sorting in the field. This meant that a typical  $1\times 1\mathrm{mm}^2$  sample with an  $\sim 25\%$  coverage could be written in about  $14\mathrm{min}$  at a dose of  $225~{\mu\mathrm{C}}~\mathrm{cm}^{-2}$ . The electron-beam tool, Raith EBPG5200, was run at  $100\mathrm{keV}$  and we used a beam current of  $20\mathrm{nA}$ , giving a beam-spot size of about  $15\mathrm{nm}$ . After exposure, the samples were developed for  $3\mathrm{min}$  in  $n$ -amyl-acetate followed by a  $1\mathrm{min}$  isopropanol rinse before being dried using a nitrogen gun. The substrates were etched in an inductively coupled plasma etch tool, a Plasma-Therm Versalock 700, using a mixture of  $\mathrm{SF}_6$  and  $\mathrm{C_4F_8}$  to allow for high selectivity for silicon. We aimed at a slight overetching of silicon to ensure that the oxide layer would be revealed. The remaining resist was stripped using  $\mathrm{O}_2$  plasma. Characterization of the different samples was carried out using a field-emission SEM Gemini G500 instrument and a Bruker Dimension Icon atomic force microscope. Supplementary Fig. 2 shows a high-resolution SEM image of the fabricated strained structure obtained at  $1\mathrm{kV}$ .

# Data availability

Data are available from the corresponding author upon reasonable request.

# Acknowledgements

We gratefully acknowledge funding support from the Office of Naval Research MURI program under agreement no. N00014-20-1-2325; the Air Force Office of Scientific Research MURI program under agreement no. FA9550-22-1-0339; and the Kaufman and Packard foundations under grant nos. KA2020-114794 and 2017-66821, respectively. This research was also supported in part by National Science Foundation grants DMS-1620422 (M.C.R.), DMS-1620418 (M.I.W.), DMS-1908657 (M.I.W.) and DMS-1937254 (M.I.W.), as well as Simons Foundation Math + X Investigator Award no. 376319 (M.I.W.). We acknowledge the Nanofabrication Lab within the Materials Research Institute at Penn State and the help of M. Labella, as well as seed funding from the Center for Nanofabricated Optics at Penn State University. F.G. thanks GenlSys, particularly R. McCay for his help in optimizing the fracturing of the electron-beam patterns. M.B. thanks S. Mukherjee and A. Cerjan for fruitful discussions in the early stages of the project and help with numerical optimization.

# Author contributions

M.B. built the experimental setup and carried out all the experimental observations, with advice from L.H., B.Z. and M.C.R. M.B. and F.G. developed the device designs with input from Z.Z., S.V., J.G., R.M. and M.C.R. F.G. carried out the device fabrication. Z.Z. carried out the numerical and analytical calculations with input from J.G., M.B., S.V., M.I.W. and M.C.R. All authors contributed to writing the manuscript. M.C.R. supervised the project.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41566-024-01425-y.

Correspondence and requests for materials should be addressed to Mikael C. Rechtsman.

Peer review information Nature Photonics thanks the anonymous reviewers for their contribution to the peer review of this work.

Reprints and permissions information is available at www.nature.com/reprints.