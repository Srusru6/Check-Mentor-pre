# Spawning rings of exceptional points out of Dirac cones

Bo Zhen $^{1*}$ , Chia Wei Hsu $^{1,2*}$ , Yuichi Igarashi $^{1,3*}$ , Ling Lu $^{1}$ , Ido Kaminer $^{1}$ , Adi Pick $^{1,4}$ , Song-Liang Chua $^{5}$ , John D. Joannopoulos $^{1}$  & Marin Soljacic $^{1}$

The Dirac cone underlies many unique electronic properties of graphene $^{1}$  and topological insulators, and its band structure—two conical bands touching at a single point—has also been realized for photons in waveguide arrays $^{2}$ , atoms in optical lattices $^{3}$ , and through accidental degeneracy $^{4,5}$ . Deformation of the Dirac cone often reveals intriguing properties; an example is the quantum Hall effect, where a constant magnetic field breaks the Dirac cone into isolated Landau levels. A seemingly unrelated phenomenon is the exceptional point $^{6,7}$ , also known as the parity–time symmetry breaking point $^{8-11}$ , where two resonances coincide in both their positions and widths. Exceptional points lead to counter-intuitive phenomena such as loss-induced transparency $^{12}$ , unidirectional transmission or reflection $^{11,13,14}$ , and lasers with reversed pump dependence $^{15}$  or single-mode operation $^{16,17}$ . Dirac cones and exceptional points are connected: it was theoretically suggested that certain non-Hermitian perturbations can deform a Dirac cone and spawn a ring of exceptional points $^{18-20}$ . Here we experimentally demonstrate such an ‘exceptional ring’ in a photonic crystal slab. Angle-resolved reflection measurements of the photonic crystal slab reveal that the peaks of reflectivity follow the conical band structure of a Dirac cone resulting from accidental degeneracy, whereas the complex eigenvalues of the system are deformed into a two-dimensional flat band enclosed by an exceptional ring. This deformation arises from the dissimilar radiation rates of dipole and quadrupole resonances, which play a role analogous to the loss and gain in parity–time symmetric systems. Our results indicate that the radiation existing in any open system can fundamentally alter its physical properties in ways previously expected only in the presence of material loss and gain.

Closed and lossless physical systems are described by Hermitian operators, which guarantee realness of the eigenvalues and a complete set of eigenfunctions that are orthogonal to each other. On the other hand, systems with open boundaries<sup>7,21</sup> or with material loss and gain<sup>9-17,19</sup> are non-Hermitian<sup>6</sup>, and have non-orthogonal eigenfunctions with complex eigenvalues where the imaginary part corresponds to decay or growth. The most drastic difference between Hermitian and non-Hermitian systems is that the latter exhibit exceptional points (EPs) where both the real and the imaginary parts of the eigenvalues coalesce. At an EP, two (or more) eigenfunctions collapse into one so the eigenspace no longer forms a complete basis, and this eigenfunction becomes orthogonal to itself under the unconjugated 'inner product'<sup>6,7</sup>. To date, most studies of the EP and its intriguing consequences concern parity-time symmetric systems that rely on material loss and gain<sup>9-17,19</sup>, but EPs are a general property that require only non-Hermiticity. Here, we show the existence of EPs in a photonic crystal slab with negligible absorption loss and no artificial gain. When a Dirac-cone system has dissimilar radiation rates, the band structure is altered abruptly to show branching features with a ring of EPs. We

provide a complete picture of this system, ranging from an analytic model and numerical simulations to experimental observations; taken together, these results illustrate the role of radiation-induced non-Hermiticity that bridges the study of EPs and the study of Dirac cones.

We start by showing that non-Hermiticity from radiation can deform an accidental Dirac point into a ring of EPs. First, consider a two-dimensional photonic crystal (Fig. 1a inset), where a square lattice (periodicity  $a$ ) of circular air holes (radius  $r$ ) is introduced in a dielectric material. This is a Hermitian system, as there is no material gain or loss and no open boundary for radiation. By tuning a system parameter (for example,  $r$ ), one can achieve accidental degeneracy between a quadrupole mode and two degenerate dipole modes at the  $\Gamma$  point (centre of the Brillouin zone), leading to a linear Dirac dispersion due to the anti-crossing between two bands with the same symmetry[4,22]. The accidental Dirac dispersion from the effective Hamiltonian model (see equation (1) below with  $\gamma_{\mathrm{d}} = 0$ ) is shown as solid lines in Fig. 1a, agreeing with numerical simulation results (symbols). In the effective Hamiltonian we do not consider the dispersionless third band (grey line) owing to symmetry arguments (Supplementary Information section I), although this third band cannot be neglected in certain calculations, including the Berry phase and effective medium properties[23].

Next, we consider a similar, but open, system: a photonic crystal slab (Fig. 1b inset) with finite thickness  $h$ . With the open boundary, modes within the radiation continuum become resonances because they radiate by coupling to extended plane waves in the surrounding medium. Non-Hermitian perturbations need to be included in the Hamiltonian to account for the radiation loss. To the leading order, radiation of the dipole mode can be described by adding an imaginary part  $-i\gamma_{\mathrm{d}}$  to the Hamiltonian, while the quadrupole mode does not radiate owing to its symmetry mismatch with the plane waves[24]. Specifically, at the  $\Gamma$  point the system has  $C_2$  rotational symmetry (invariant under  $180^{\circ}$  rotation around the  $z$  axis), and the quadrupole mode does not couple to the radiating plane wave because the former has a field profile  $E(\boldsymbol{r})$  that is even under  $C_2$  rotation,  $E(\boldsymbol{r}) = \hat{O}_{C_2}E(\boldsymbol{r})$ , whereas the latter is odd,  $E(\boldsymbol{r}) = -\hat{O}_{C_2}E(\boldsymbol{r})$ . The effective Hamiltonian is

$$
H _ {\text {e f f}} = \left( \begin{array}{c c} \omega_ {0} & v _ {g} | \boldsymbol {k} | \\ v _ {g} | \boldsymbol {k} | & \omega_ {0} - i \gamma_ {\mathrm {d}} \end{array} \right) \tag {1}
$$

with complex eigenvalues

$$
\omega_ {\pm} = \omega_ {0} - i \frac {\gamma_ {\mathrm {d}}}{2} \pm v _ {g} \sqrt {\left| \boldsymbol {k} \right| ^ {2} - k _ {c} ^ {2}} \tag {2}
$$

where  $\omega_0$  is the frequency at accidental degeneracy,  $\nu_{\mathrm{g}}$  is the group velocity of the linear Dirac dispersion in the absence of radiation,  $|\pmb{k}|$  is the magnitude of the in-plane wavevector  $(k_x,k_y)$ , and  $k_{\mathrm{c}}\equiv \gamma_{\mathrm{d}} / 2\nu_{\mathrm{g}}$ . Here, one of the three bands is decoupled from the other two and is not included in equation (1) (see Supplementary Information section II). In equation (2), a ring defined by  $|\pmb{k}| = k_{\mathrm{c}}$  separates the  $k$  space

![](images/7a2ea40abc1b7242cc3360a9fb9136cead2dd9c5bf309a864a15bb8422097675.jpg)

![](images/2a31ed348c1c7e5c150b939c01447146037e5f0e08835dd6fba19d0aa1b366c5.jpg)

![](images/f36adb29ad4343c805b2c365ef3dd8a64ec0496523e4ff8f335fe0997a2b6bf3.jpg)

![](images/17be0070187f98b64915b511d58191fdea1f327574960ba9714a86ef1e5c74d1.jpg)  
Figure 1 | Accidental degeneracy in Hermitian and non-Hermitian photonic crystals. a, Band structure of a two-dimensional photonic crystal consisting of a square lattice of circular air holes. Tuning the radius  $r$  leads to accidental degeneracy between a quadrupole band and two doubly degenerate dipole bands, resulting in two bands with linear Dirac dispersion (red and blue) and a flat band (grey). b, c, The real (b) and imaginary (c) parts of the eigenvalues of an open, and therefore non-Hermitian, system: a photonic crystal slab with finite thickness,  $h$ . By tuning the radius, accidental degeneracy in the real part can be achieved, but the Dirac dispersion is deformed owing to the non-Hermiticity. The analytic model predicts that the

![](images/4002fad0aebd66c2bb5404ed95b4979e93ddb311d8ad777e491035645b80fe60.jpg)

![](images/d0d3cddde161e30dfb6d21f8d66044c0f9959fd1237e0f02ee6b68adc675e473.jpg)

into two regions: inside the ring  $(|\pmb{k}| < k_{\mathrm{c}})$ ,  $\operatorname{Re}(\omega_{\pm})$  are dispersionless and degenerate; outside the ring  $(|\pmb{k}| > k_{\mathrm{c}})$ ,  $\operatorname{Im}(\omega_{\pm})$  are dispersionless and degenerate. In the vicinity of  $k_{\mathrm{c}}$ ,  $\operatorname{Im}(\omega_{\pm})$  and  $\operatorname{Re}(\omega_{\pm})$  exhibit square-root dispersion (also known as branching behaviour) inside and outside the ring, respectively. Exactly on the ring  $(|\pmb{k}| = k_{\mathrm{c}})$ , the two eigenvalues  $\omega_{\pm}$  are degenerate in both real and imaginary parts; meanwhile, the matrix  $H_{\mathrm{eff}}$  becomes defective with an incomplete eigenspace spanned by only one eigenvector  $(1, -i)^{\mathrm{T}}$  that is orthogonal to itself under the unconjugated 'inner product', given by  $\pmb{a}^{\mathrm{T}}\pmb{b}$  for vectors  $\pmb{a}$  and  $\pmb{b}$ . This self-orthogonality is the definition of EPs; hence, here we have not just one EP, but a continuous ring of EPs. We call it an exceptional ring.

Figure 1b, c shows the complex eigenvalues of the photonic crystal slab structure calculated numerically (symbols), which closely follow the analytic model of equation (2) shown as solid lines in the figure. In Supplementary Fig. 1, we show that the two eigenvectors indeed coalesce into one at the EP, which is impossible in Hermitian systems (also see Supplementary Information section III). When the radius  $r$  of the holes is tuned away from accidental degeneracy, the exceptional ring and the associated branching behaviour disappear, as shown in Supplementary Fig. 2. Several properties of the photonic crystal slab contribute to the existence of this exceptional ring. Owing to periodicity, one can probe the dispersion from two degrees of freedom,  $k_{x}$  and  $k_{y}$ , in just one structure. The open boundary provides radiation loss, and the  $C_2$  rotational symmetry differentiates the radiation loss of the dipole mode and of the quadrupole mode.

We can rigorously show that the exceptional ring exists in realistic photonic crystal slabs, not just in the effective Hamiltonian model. Our proof is based on the unique topological property of EPs: when the system parameters evolve adiabatically along a loop encircling an EP, the two eigenvalues switch their positions when the system returns to its initial parameters $^{7,21,25}$ , in contrast to the typical case where the two eigenvalues return to themselves. Using this property, we numerically

real (imaginary) part of the eigenvalue stays as a constant inside (outside) a ring in the wavevector space, indicating two flat bands in dispersion, with a ring of exceptional points (EPs) where both the real and the imaginary parts are degenerate. The orange shaded regions correspond to the inside of the ring. In the upper panels of a-c, solid lines are predictions from the analytic model and symbols are from numerical simulations: red squares represent the band connecting to the quadrupole mode at the centre; blue circles represent the band connecting to the dipole mode at the centre; and grey crosses represent the third band that is decoupled from the previous two due to symmetry. The three-dimensional plots in the lower panels are from simulations.

show, in Supplementary Fig. 3 and Supplementary Information section IV, that the complex eigenvalues always switch their positions along every direction in the  $k$  space, and therefore prove the existence of this exceptional ring. As opposed to the simplified effective Hamiltonian model, in a real photonic crystal slab, the EP may exist at a slightly different magnitude of  $k$  and for a slightly different hole radius  $r$  along different directions in the  $k$  space, but this variation is small and negligible in practice (Supplementary Information section V).

To demonstrate the existence of the exceptional ring in such a system, we fabricate large-area periodic patterns in a  $\mathrm{Si}_3\mathrm{N}_4$  slab ( $n = 2.02$  in the visible spectrum, thickness  $180\mathrm{nm}$ ) on top of  $6\mu \mathrm{m}$  of silica ( $n = 1.46$ ) using interference photolithography[24]. Scanning electron microscope (SEM) images of the sample are shown in Fig. 2a, featuring a square lattice (periodicity  $a = 336\mathrm{nm}$ ) of cylindrical air holes with radius  $109\mathrm{nm}$ . We immerse the structure into an optical liquid with a specified refractive index that can be tuned; accidental degeneracy in the Hermitian part is achieved when the liquid index is selected to be  $n = 1.48$ . We perform angle-resolved reflectivity measurements (set-up shown in Fig. 2b) between  $0^{\circ}$  and  $2^{\circ}$  along the  $\Gamma \rightarrow \mathrm{X}$  direction and the  $\Gamma \rightarrow \mathrm{M}$  direction, for both s and p polarizations. Details of the sample fabrication and the experimental setup can be found in Supplementary Information section VI. The measured reflectivity for the relevant polarization is plotted in the upper panel of Fig. 2c, showing good agreement with numerical simulation results (lower panel), with differences coming from scattering due to surface roughness, inhomogeneous broadening, and the uncertainty in the measurements of system parameters. The complete experimental result for both polarizations is shown in Supplementary Fig. 4; the third and dispersionless band shows up in the other polarization, decoupled from the two bands of interest.

The peaks of reflectivity (dark red colour in Fig. 2c) follow the linear Dirac dispersion; this feature disappears for structures with different radii that do not reach accidental degeneracy (experimental results in

![](images/3bfb024b8dacd7c937778762f4c2216fb76cfccceb8928ef3b3a707dad2fdbdb.jpg)  
a

![](images/e7c043e30c083a9d3f4871d07a30d000d5b40de16ef2ffe7bce45f2b2e0fbd94.jpg)

![](images/7131256d4de365344adfc4cbfa33d98beb30b09ecc534ced7f125a174309ef4f.jpg)

![](images/03f1fc370f43f61dcfa2cf7d5fdcf6f582c6cf60a6edda8a5467cd8a2293ad7e.jpg)  
b

![](images/bc056cd6a5feaff1be6f1bc75ae152cc796dcccc48c248d617362c5208e23eaa.jpg)  
Figure 2 | Experimental reflectivity spectrum and accidental Dirac dispersion. a, SEM images of the photonic crystal samples: side view (upper panel) and top view (lower panel). b, Schematic drawing of the measurement set-up. Linearly polarized light from a super-continuum source is reflected off the photonic crystal slab ('sample') immersed in an optical liquid, and collected by a spectrometer (SP). The incident angle  $\theta$  is controlled using a precision rotating stage. BS, beam splitter. c, Reflectivity spectrum of the sample measured experimentally (upper panel) and calculated numerically (lower panel) along the  $\Gamma \rightarrow \mathrm{X}$  and the  $\Gamma \rightarrow \mathrm{M}$  directions. The peak location of reflectivity reveals the Hermitian part of the system, which forms Dirac dispersion due to accidental degeneracy. In the lower panel, white solid lines  
Frennnnne, 00220

![](images/c025800eebf8aff54dfdf45eb0299dcc91f8c50248a4d40c481432bc5e8cd5c8.jpg)

![](images/9ed9c5710b451f697f992ba5396f22ef580760e5234f5f99f0da04ca060fb979.jpg)

Supplementary Fig. 5). Note that the reflection peaks do not follow the real part of the complex eigenvalues of the Hamiltonian; in fact they follow the eigenvalues of the Hermitian part of the Hamiltonian, even though the Hamiltonian is non-Hermitian. To understand this, we consider a more general two-by-two Hamiltonian of a coupled resonance system  $H$  and separate it into a Hermitian part  $A$  and an anti-Hermitian part  $-iB$  ( $A$  and  $B$  are both Hermitian)

$$
H = \underbrace {\left( \begin{array}{c c} \omega_ {1} & \kappa \\ \kappa & \omega_ {2} \end{array} \right)} _ {A} - \underbrace {i \left( \begin{array}{c c} \gamma_ {1} & \gamma_ {1 2} \\ \gamma_ {1 2} & \gamma_ {2} \end{array} \right)} _ {i B} \xrightarrow {\text {e i g e n v a l u e s}} \left( \begin{array}{c c} \omega_ {+} & 0 \\ 0 & \omega_ {-} \end{array} \right) \tag {3}
$$

As before, we use  $\omega_{\pm}$  to denote the complex eigenvalues of the Hamiltonian  $A - iB$ . Physically, matrix  $A$  describes a lossless system, and matrix  $-iB$  adds the effects of loss. In  $B$ , the diagonal elements are loss rates (in our system, they come primarily from radiation), and the off-diagonal elements arise from overlap of the two radiation patterns, also known as external coupling of resonances via the continuum. Modelling the reflectivity using temporal coupled-mode theory (TCMT), we show that when matrix  $B$  is dominated by radiation, the reflection peaks occur near the eigenvalues  $\Omega_{1,2}$  of the Hermitian part  $A$  and are independent of the anti-Hermitian part  $-iB$  (see Supplementary Information section VII and Supplementary Fig. 6 for details). Therefore, the linear Dirac dispersion observed in the measured data of Fig. 2c (dark red) indicates that we have successfully achieved accidental degeneracy in the eigenvalues of the Hermitian part, consistent with the simplified model in equation (1). In Supplementary Fig. 8b, we plot the values of  $\Omega_{1,2}$  extracted from the

indicate the real part of the eigenvalues; spectra and eigenvalues at three representative angles (marked by dashed lines and circles) are shown in d. d, Three line cuts of reflectivity  $R$  from simulation results. Also shown are the complex eigenvalues (open circles) calculated numerically. At large angles  $(0.8^{\circ})$ , the two resonances are far apart, so the reflectivity peaks (red arrows) are close to the actual positions of the complex eigenvalues. However, at small angles  $(0.3^{\circ}, 0.1^{\circ})$ , the coupling between resonances cause the resonance peaks (red arrows) to have much greater separations in frequency compared to the complex eigenvalues. The black arrows mark the dips in reflectivity that correspond to the coupled-resonator induced transparency (CRIT, see text for details).

reflectivity data through a more rigorous data analysis using TCMT (described below); the linear dispersion is indeed observed. We note that when there is substantial non-radiative loss or material gain in the system, the reflection peaks no longer follow the eigenvalues of the Hermitian part (see Supplementary Information section VIII and Supplementary Fig. 7).

The real part of the complex eigenvalues of the Hamiltonian,  $\mathrm{Re}(\omega_{\pm})$  , behave very differently from the reflectivity peaks. Simulation results (solid white lines in the lower panel of Fig. 2c) show  $\mathrm{Re}(\omega_{\pm})$  is dispersionless at small angles with a branch-point singularity around  $0.31^{\circ}$  -consistent with the feature predicted by the simplified Hamiltonian in equation (2). In Fig. 2d, we compare the reflectivity spectra from simulations (with peaks indicated by red arrows) with the corresponding complex eigenvalues at three representative angles  $(0.8^{\circ}$  in blue,  $0.31^{\circ}$  in green and  $0.1^{\circ}$  in magenta). At  $0.31^{\circ}$  , the two complex eigenvalues are degenerate, indicating an EP; however, the two reflection peaks do not coincide since they represent the eigenvalues of only the Hermitian part of the Hamiltonian, which does not have degeneracy here. The dip in reflectivity between the two peaks (marked as black arrows in Figs 2 and 3) is the coupled-resonator-induced transparency (CRIT) that arises from the interference between radiation of the two resonances26, similar to electromagnetically induced transparency.

Qualitatively, the peak locations of the measured reflectivity spectrum reveal the eigenvalues of the Hermitian part,  $A$ , and the linewidths of the peaks reveal the anti-Hermitian part,  $-iB$ ; diagonalizing  $A - iB$  yields the eigenvalues  $\omega_{\pm}$ , as illustrated in equation (3). To be more quantitative, we use TCMT and account for both the direct

![](images/775b1bb8d107cc8636890de3534a09fb9e332373e4fed4f108857717606d0885.jpg)

![](images/ac1d53cf6b15caded636ef7977ef74d3ca332818322e8c74f75c45ecdb1e2b86.jpg)

![](images/4afb46ede0fd1ed44b365e06bbc18fe60dfecd9d178137296aa4712d944a719f.jpg)  
Figure 3 | Experimental demonstration of an exceptional ring. a, Examples of reflection spectrum  $R$  from the sample at three different angles (0.8° blue, 0.3° green and 0.1° magenta, solid lines) measured with s-polarized light along the  $\Gamma \rightarrow \mathrm{X}$  direction (same setup as in numerical simulations shown in Fig. 2d), fitted with the TCMT expression (equation (S20) in Supplementary Information) (black dashed lines). At each angle, the positions of the complex eigenvalues extracted experimentally are shown as open circles. b, Complex eigenvalues extracted experimentally (symbols), with comparison to numerical simulation results (dashed lines) for both the real part (left panel) and the

![](images/f025d5d124e727bbd07999d17e749a4b6ede0b0af79e67adbc8f44760bc211cf.jpg)

![](images/d71c4ef2e45a60f1891c2c3fafd9badbe8ca9c7042c42bbb2995900f7a5b2d5b.jpg)

![](images/edb0f7b13dd6908ed9cfc3ced7b98b6fbd34c5079db6ab151afa24250dc4f878.jpg)

![](images/4b9cac8d4ac5f94a97fc9ff7b0491f6fd62d3c66285d3ade71d9ce9ce42d9153.jpg)

(non-resonant) and the resonant reflection processes including nearby resonances; the expression for reflectivity is given in Supplementary Information equation (S20), with the full derivation given in Supplementary Information section IX. Fitting the reflectivity curves with the TCMT expression gives us an accurate estimate of the matrix elements and the eigenvalues; this procedure is the same as our approach in ref. 27 except that here we additionally account for the coupling between resonances[28]. Figure 3a compares the fitted and the measured reflectivity curves at three representative angles (with more comparison in Supplementary Fig. 8a); the excellent agreement shows the validity of the TCMT model. Underneath the reflectivity curves, we show the complex eigenvalues. The difference between numerically calculated reflectivity (Fig. 2d) and experimental results (Fig. 3a) stems from the non-radiative decay channels in our system, mostly due to scattering loss from the surface roughness[24].

Repeating the fitting procedure for the reflectivity spectrum measured at different angles, we obtain the dispersion curves for all complex eigenvalues, which are plotted in Fig. 3b. Along both directions in  $k$  space  $(\Gamma \rightarrow \mathrm{X}$  and  $\Gamma \rightarrow \mathrm{M})$ , the two bands of interest (shown in blue and red) exhibit the EP behaviour predicted in equation (2): for  $|\pmb{k}| < k_{\mathrm{c}}$  the real parts are degenerate and dispersionless; for  $|\pmb{k}| > k_{\mathrm{c}}$  the imaginary parts are degenerate and dispersionless; for  $|\pmb{k}|$  in the vicinity of  $k_{\mathrm{c}}$  branching features are observed in the real or imaginary part. In Fig. 3c, we plot the eigenvalues on the complex plane for both the  $\Gamma \rightarrow \mathrm{X}$  and  $\Gamma \rightarrow \mathrm{M}$  directions. We can see that in both directions, the two eigenvalues approach each other and become very close at a certain  $k$  point, which is a clear signature of the system being very close to an EP.

We have shown that non-Hermiticity arising from radiation can significantly alter fundamental properties of the system, including the band structures and the density of states; this effect becomes most

imaginary part (right panel). Red squares and dashed lines are used for the band with zero radiation loss at the  $\Gamma$  point, blue circles and dashed lines for the band with finite radiation loss at the  $\Gamma$  point, and grey crosses and dashed lines for the third band decoupled from the previous two owing to symmetry. The orange shaded regions correspond to the inside of the ring. c, Positions of the eigenvalues (red and blue dashed lines) approach and become very close to each other (indicated by the two brown arrows), demonstrating near-EP features in different directions in the momentum space and the existence of an exceptional ring.

prominent near EPs. The photonic crystal slab described here provides a simple-to-realize platform for studying the influence of EPs on light-matter interaction, such as for single particle detection $^{21}$  and modulation of quantum noise. The two-dimensional flat band can also provide a high density of states and therefore high Purcell factors. The strong dispersion of loss in the vicinity of the  $\Gamma$  point can improve the performance of large-area single-mode photonic crystal lasers $^{29}$ . The deformation into an exceptional ring is a general phenomenon that can also be achieved with material gain or loss and for Dirac points in other lattices $^{19,20}$ . Further studies could advance the understanding of the connection between the topological property of Dirac points $^{30}$  and that of EPs $^{25}$  in general non-Hermitian wave systems, and our method could go beyond photons to phonons, electrons and atoms.

# Received 2 April; accepted 29 June 2015.

# Published online 9 September 2015.

1. Castro Neto, A. H., Guinea, F., Peres, N. M. R., Novoselov, K. S. & Geim, A. K. The electronic properties of graphene. Rev. Mod. Phys. 81, 109-162 (2009).  
2. Rechtsman, M. C. et al. Strain-induced pseudomagnetic field and photonic landau levels in dielectric structures. Nature Photon. 7, 153-158 (2013).  
3. Tarruell, L., Greif, D., Uehlinger, T., Jotzu, G. & Esslinger, T. Creating, moving and merging Dirac points with a Fermi gas in a tunable honeycomb lattice. Nature 483, 302-305 (2012).  
4. Huang, X., Lai, Y., Hang, Z. H., Zheng, H. & Chan, C. Dirac cones induced by accidental degeneracy in photonic crystals and zero-refractive-index materials. Nature Mater. 10, 582-586 (2011).  
5. Moitra, P. et al. Realization of an all-dielectric zero-index optical metamaterial. Nature Photon. 7, 791-795 (2013).  
6. Moiseyev, N. Non-Hermitian Quantum Mechanics (Cambridge Univ. Press, 2011).  
7. Rotter, I. A non-Hermitian Hamilton operator and the physics of open quantum systems. J. Phys. A 42, 153001 (2009).  
8. Bender, C. M. & Boettcher, S. Real spectra in non-Hermitian Hamiltonians having PT symmetry. Phys. Rev. Lett. 80, 5243-5246 (1998).  
9. Rüter, C. E. et al. Observation of parity-time symmetry in optics. Nature Phys. 6, 192-195 (2010).

10. Chong, Y., Ge, L. & Stone, A. D. PT-symmetry breaking and laser-absorber modes in optical scattering systems. Phys. Rev. Lett. 106, 093902 (2011).  
11. Regensburger, A. et al. Parity-time synthetic photonic lattices. Nature 488, 167-171 (2012).  
12. Guo, A. et al. Observation of PT-symmetry breaking in complex optical potentials. Phys. Rev. Lett. 103, 093902 (2009).  
13. Lin, Z. et al. Unidirectional invisibility induced by PT-symmetric periodic structures. Phys. Rev. Lett 106, 213901 (2011).  
14. Peng, B. et al. Parity-time-symmetric whispering-gallery microcavities. Nature Phys. 10, 394-398 (2014).  
15. Liertzer, M. et al. Pump-induced exceptional points in lasers. Phys. Rev. Lett. 108, 173901 (2012).  
16. Hodaei, H., Miri, M.-A., Heinrich, M., Christodoulides, D. N. & Khajavikhan, M. Parity-time-symmetric microring lasers. Science 346, 975-978 (2014).  
17. Feng, L., Wong, Z. J., Ma, R.-M., Wang, Y. & Zhang, X. Single-mode laser by parity-time symmetry breaking. Science 346, 972-975 (2014).  
18. Berry, M. Physics of nonhermitian degeneracies. Czech. J. Phys. 54, 1039-1047 (2004).  
19. Makris, K., El-Ganainy, R., Christodoulides, D. & Musslimani, Z. H. Beam dynamics in PT symmetric optical lattices. Phys. Rev. Lett. 100, 103904 (2008).  
20. Szameit, A., Rechtsman, M. C., Bahat-Treidel, O. & Segev, M. PT-symmetry in honeycomb photonic lattices. Phys. Rev. A 84, 021806 (2011).  
21. Cao, H. & Wiersig, J. Dielectric microcavities: model systems for wave chaos and non-Hermitian physics. Rev. Mod. Phys. 87, 61-111 (2015).  
22. Sakoda, K. Proof of the universality of mode symmetries in creating photonic Dirac cones. Opt. Express 20, 25181-25194 (2012).  
23. Chan, C., Hang, Z. H. & Huang, X. Dirac dispersion in two-dimensional photonic crystals. Adv. Optoelectron. 2012, 313984 (2012).  
24. Lee, J. et al. Observation and differentiation of unique high-Q optical resonances near zero wave vector in macroscopic photonic crystal slabs. Phys. Rev. Lett. 109, 067401 (2012).  
25. Dembowski, C. et al. Experimental observation of the topological structure of exceptional points. Phys. Rev. Lett 86, 787-790 (2001).

26. Hsu, C.W., DeLacy, B.G., Johnson, S.G., Joannopoulos, J. D. & Soljacic, M. Theoretical criteria for scattering dark states in nanostructured particles. Nano Lett. 14, 2783-2788 (2014).  
27. Hsu, C.W. et al. Observation of trapped light within the radiation continuum. Nature 499, 188-191 (2013).  
28. Suh, W., Wang, Z. & Fan, S. Temporal coupled-mode theory and the presence of non-orthogonal modes in lossless multimode cavities. IEEE J. Quantum Electron. 40, 1511-1518 (2004).  
29. Chua, S.-L., Lu, L., Bravo-Abad, J., Joannopoulos, J. D. & Soljacic, M. Larger-area single-mode photonic crystal surface-emitting lasers enabled by an accidental Dirac point. Opt. Lett. 39, 2072-2075 (2014).  
30. Lu, L., Joannopoulos, J. D. & Soljacic, M. Topological photonics. Nature Photon. 8, 821-829 (2014).

Supplementary Information is available in the online version of the paper.

Acknowledgements We thank T. Savas for fabrication of the samples, and F. Wang, Y. Yang, N. Rivera, S. Skirlo, O. Miller and S. G. Johnson for discussions. This work was partly supported by the Army Research Office through the Institute for Soldier Nanotechnologies under contract nos W911NF-07-D0004 and W911NF-13-D-0001. B.Z., L.L. and M.S. were partly supported by S3TEC, an Energy Frontier Research Center funded by the US Department of Energy under grant no. DE-SC0001299. L.L. was supported in part by the Materials Research Science and Engineering Center of the National Science Foundation (award no. DMR-1419807). I.K. was supported in part by Marie Curie grant no. 328853-MC-BSiCS.

Author Contributions All authors discussed the results and made critical contributions to the work.

Author Information Reprints and permissions information is available at www.nature.com/reprints. The authors declare no competing financial interests. Readers are welcome to comment on the online version of the paper. Correspondence and requests for materials should be addressed to B.Z. (bozhen@mit.edu) and C.W.H. (chiawei.hsu@yale.edu).