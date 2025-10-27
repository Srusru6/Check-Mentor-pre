22. O. C. Velázquez, H. M. Lederer, J. L. Rombeau, Adv. Exp. Med. Biol. 427, 123-134 (1997).  
23. G. T. Furuta et al., J. Exp. Med. 193, 1027-1034 (2001).  
24. C. J. Kelly et al., Cell Host Microbe 17, 662-671 (2015).  
25. N. Terada, N. Ohno, S. Saitoh, S. Ohno, Histochem. Cell Biol. 128, 253-261 (2007).  
26. J. W. Collins et al., Nat. Rev. Microbiol. 12, 612-623 (2014).  
27. A. R. Wong, A. Clements, B. Raymond, V. F. Crepin, G. Frankel, MBio 3, e00250-11 (2012).  
28. C. Ma et al., Cell. Microbiol. 8, 1669-1686 (2006).  
29. J. P. Nougayrède, M. S. Donnenberg, Cell. Microbiol. 6, 1097-1111 (2004).  
30. Y. Y. Fan et al., Am. J. Physiol. Gastrointest. Liver Physiol. 309, G1-G9 (2015).  
31. I. Ahmed et al., Infect. Immun. 80, 3107-3121 (2012).

32. P. Chandrakesan et al., J. Biol. Chem. 285, 33485-33498 (2010).  
33. E. Caron et al., Curr. Opin. Microbiol. 9, 40-45 (2006).  
34. G. Frankel et al., Mol. Microbiol. 30, 911-921 (1998).  
35. A. Carreau, B. El Hafry-Rahbi, A. Matejuk, C. Grillon, C. Kieda, J. Cell. Mol. Med. 15, 1239-1253 (2011).  
36. M. G. Espey, Free Radic. Biol. Med. 55, 130-140 (2013).

# ACKNOWLEDGMENTS

We acknowledge the Host-Microbe Systems Biology Core (HMSB Core) at the University of California Davis School of Medicine for expert technical assistance with microbiota sequence analysis. The data reported in the manuscript are tabulated in the main paper and in the supplementary materials and are available in the National Center for Biotechnology Information BioSample database under

accession numbers SAMN05420840 through SAMN05420856. Work in A.J.B.'s laboratory was supported by Public Health Service Grants AI044170, AI096528, AI107393, and AI112949. Work in R.M.T.'s laboratory was supported by Public Health Service Grant AI098078. Work in S.E.W.'s laboratory was supported by Public Health Service Grant AI103248. C.A.L was supported by Public Health Service Grant AI112241. E.M.V. was supported by Public Health Service Grant OD010931.

# SUPPLEMENTARY MATERIALS

www.sciencemag.org/content/353/6305/1249/suppl/DC1

Materials and Methods

Figs. S1 to S12

Tables S1 and S2

References (37-52)

6 June 2016; accepted 5 August 2016

10.1126/science.aag3042

# REPORTS

# QUANTUM SIMULATION

# Site-resolved measurement of the spin-correlation function in the Fermi-Hubbard model

Maxwell F. Parsons, Anton Mazurenko, Christie S. Chiu, Geoffrey Ji, Daniel Greif, Markus Greiner*

Exotic phases of matter can emerge from strong correlations in quantum many-body systems. Quantum gas microscopy affords the opportunity to study these correlations with unprecedented detail. Here, we report site-resolved observations of antiferromagnetic correlations in a two-dimensional, Hubbard-regime optical lattice and demonstrate the ability to measure the spin-correlation function over any distance. We measure the in situ distributions of the particle density and magnetic correlations, extract thermodynamic quantities from comparisons to theory, and observe statistically significant correlations over three lattice sites. The temperatures that we reach approach the limits of available numerical simulations. The direct access to many-body physics at the single-particle level demonstrated by our results will further our understanding of how the interplay of motion and magnetism gives rise to new states of matter.

Quantum many-body systems exhibiting magnetic correlations underlie a wide variety of phenomena. High-temperature superconductivity, for example, can arise from the correlated motion of holes in an antiferromagnetic (AFM) Mott insulator (1, 2). It is possible to probe physical analogs of such systems using ultracold atoms in lattices, which introduce a degree of control that is not available in conventional solid-state systems (3, 4). Recent experiments exploring the Hubbard model with cold atoms are accessing temperatures where AFM correlations form but have only observed these correlations via measurements that were averages

Department of Physics, Harvard University, Cambridge, MA 02138, USA.

*Corresponding author. Email: mgreiner@g.harvard.edu

over inhomogeneous systems (5, 6). The recent development of site-resolved imaging for fermionic quantum gases (7-13) provides the ability to directly detect the correlations and fluctuations present in a fermionic quantum many-body state. As demonstrated in experiments with both bosons (14, 15) and fermions (12, 13, 16), microscopy gives access to the spatial variation in observables that occurs in an inhomogeneous system, yielding precise comparisons with theory. The low energy scales in cold-atom systems also allow for time-resolved observations of many-body dynamics, which typically occur on millisecond time scales. In bosonic systems, temporal and spatial resolution have been combined to observe strongly correlated quantum walks (17), to measure entanglement entropy (18), and to study the dynamics of magnetic correlations (19, 20).

Here, we report trap-resolved observations of magnetic correlations in a Fermi-lattice system. Fermionic atoms in a two-dimensional (2D) optical lattice can be well described by the Hubbard Hamiltonian, a simple model in which there is a competition between the nearest-neighbor tunneling energy  $t$  and the on-site interaction energy  $U$ . Despite the apparent simplicity of the Hubbard model, it has a rich phase diagram, containing, for example, the transition from a metal to a Mott insulator. AFM spin correlations begin to appear near half-filling when the temperature scale becomes comparable to the exchange energy, which in the strongly interacting regime is  $J = 4t^{2} / U$ . In the thermodynamic limit, what happens as the temperature is lowered further depends on the dimensionality of the system: In three dimensions, there is a finite-temperature phase transition to a state with long-range AFM order, whereas in two dimensions, such an order is prohibited by the Mermin-Wagner-Hohenberg theorem (21). Nonetheless, AFM correlations do arise, decaying exponentially with a correlation length  $\xi$  that diverges as the temperature goes to zero as  $\xi \simeq \exp (\alpha J / T)$ , where  $\alpha$  is of order unity (22). We use quantum gas microscopy to reveal precisely these correlations, which for our finite-size 2D system are expected to lead to long-range order at a finite temperature, where  $\xi$  becomes comparable to the system size.

Our experiments begin with a low-temperature, 2D gas of fermionic  $^6\mathrm{Li}$  atoms in a mixture of the two lowest hyperfine states  $(|\uparrow \rangle$  and  $|\downarrow \rangle$  as described in (12). By adjusting a magnetic bias field in the vicinity of the Feshbach resonance located at 832G, we set the s-wave scattering length to  $210a_{0}$ , where  $a_0$  is the Bohr radius (23). Using a 30-ms linear ramp, the atoms are adiabatically loaded into an isotropic, square optical lattice with a depth of  $s_0 = 7.7(5)E_r$ , where the recoil energy is  $E_{r} / h = 25.6\mathrm{kHz}$  with Planck constant  $h$ . We detect magnetic correlations by removing atoms in either spin state and measuring the resulting charge correlations with site-resolved imaging (24), as shown in Fig. 1. Because our imaging technique removes doubly occupied sites, both doubly occupied and unoccupied sites show up as empty sites after imaging. However, proper linear combinations of the different particle and

![](images/3534acb6f4420d87acf56dd3bd88a49857647b9bd59d9dd2b3deb90622f1336d.jpg)  
Fig. 1. Experimental technique for measuring spin correlations. (A) After loading the atoms into an optical lattice, we use a spin-removal technique to map the spin correlations onto charge correlations, which can then be detected using site-resolved imaging. The two spin states are denoted by green and orange balls. By driving cycling optical transitions for either spin state with the spin-removal beam, we can eject one spin state from the trap. We can then

![](images/deb889f8da9d4e64eec706c2dcbece6a2fc972ebc9c6645c15e5ddcf929c7e83.jpg)  
combine charge correlations measured in images where we remove each spin state and where no removal is performed to compute the local spin correlation (24). (B) A typical image where no atoms are removed. (C) A typical image with one of the spins removed. Atoms in doubly occupied sites are removed in both the spin-removal and imaging procedures as a result of light-assisted collisions.

![](images/bc372e0b154f09a90c36443996f31d7fc576b1106a7983e7d9eed6b7c049203f.jpg)

![](images/1261a00967b413d6725e3ce8fbcdcdd4609176836960d6115615dab35e0b08a6.jpg)  
Fig. 2. Local observation of density and spin correlations. (A to C) Spatial maps and azimuthally averaged profiles (mirrored about  $r = 0$  and corrected for ellipticity) of the detected density, nearest-neighbor correlator and diagonal next-nearest neighbor correlator for a cold (top) and hot (bottom) cloud. A combined fit determines the temperature  $T$  and chemical potential  $\mu$  (solid lines). (D) Green symbols show the nearest-neighbor correlator in the center of the cloud for samples prepared at different temperatures. Listed are the values of  $k_{B}T_{\mathrm{fit}} / t$  from fits of a numerical linked-cluster expansion to the radial profile and  $k_{B}T_{\mathrm{corr}} / t$  obtained by comparing the central correlator value to a quantum Monte Carlo

![](images/5a85d1a73640af5bf01e4df21f919412a8da63ec4c796028c1b2f4c7ab57e578.jpg)  
calculation at half-filling (solid line) (22). For the coldest data in (D) and (E) (squares), the NLCE theory error is too large for a fit, and we report only the QMC result. (E) An exponential fit to the correlator in the center of the cloud versus  $d$  allows us to extract the correlation length for data sets at three different temperatures, giving 0.24(9), 0.39(2), and 0.51(4) sites for decreasing temperature. The asterisk denotes the nearest-neighbor correlator value from the QMC calculation in (D) as  $T \to 0$ . Error bars on  $\overline{n}_{\mathrm{det}}(r)$  and  $C_d(r)$  are standard errors after averaging at least 20 sets of combined correlation maps and averaging azimuthally (24). All data shown are at  $U / t = 8.0(1)$ . Horizontal errors in (D) are fit errors.

![](images/66014747670542d91c78fd6d14b5cf2a62aeb81aab27232685a5014fb49e3b11.jpg)

![](images/037dbf157c0935d8a7e02d0022da2d19a4e5e0ae58329b41061c855c7efe6e0f.jpg)

hole correlators (measured both with and without spin-dependent removal) will account for the contribution to the signal from imperfect unity filling (24). From this, we determine the spin correlator (24)

$$
C _ {\mathrm {a}} (\mathbf {r}) = 4 \left(\left\langle S _ {\mathrm {r}} ^ {z} S _ {\mathrm {r} + \mathrm {a}} ^ {z} \right\rangle - \left\langle S _ {\mathrm {r}} ^ {z} \right\rangle \left\langle S _ {\mathrm {r} + \mathrm {a}} ^ {z} \right\rangle\right) \tag {1}
$$

Here,  $S_{\mathrm{r}}^{\sigma} = \frac{1}{2}(n_{\mathrm{r}}^{\uparrow} - n_{\mathrm{r}}^{\downarrow})$ , with  $n_{\mathrm{r}}^{\sigma}$  denoting the number of particles of spin  $\sigma$  on the site at  $\mathbf{r}$ . We take an average of  $C_{\mathrm{a}}(\mathbf{r})$  over all a where  $|\mathbf{a}| = d$  to obtain  $C_d(\mathbf{r})$ . The nearest-neighbor, diagonal next-nearest-neighbor, straight next-nearest-neighbor, etc., correlators are given by  $C_1(\mathbf{r})$ ,  $C_{1.4}(\mathbf{r})$ , and  $C_2(\mathbf{r})$ , etc. From images where neither spin was removed, we directly obtain a spatial map of the single-occupation probability  $\overline{n}_{\mathrm{det}}(\mathbf{r})$ , which also corresponds to the local moment  $C_0(\mathbf{r})$ .

After loading atoms into the lattice, we observe AFM correlations for nearest neighbors and diagonal next-nearest neighbors. These correlations are strongest in the cloud center, where the local chemical potential is set to approximately halffilling. The spatial maps  $\overline{n}_{\mathrm{det}}(\mathbf{r})$ ,  $C_1(\mathbf{r})$ , and  $C_{1.4}(\mathbf{r})$  for colder (top) and hotter (bottom) temperatures are shown in panels A, B, and C, respectively, of Fig. 2. For these data, the interaction is tuned to  $U / h = 6.82(10)\mathrm{kHz}$ , with  $t / h = 850(100)\mathrm{Hz}$  ( $U / t = 8.0(1)$ ). The chemical potential is tuned to approximately  $\mu = U / 2$  in the center of the cloud for the colder data by adjusting the atom number to maximize  $\overline{n}_{\mathrm{det}}$  in the center. In Fig. 2A, the suppression of  $\overline{n}_{\mathrm{det}}$  in the center of the cloud is caused by the formation of doubly occupied sites and indicates that the chemical potential in the center of the cloud slightly exceeds  $U / 2$ . To heat the cloud, we hold the atoms in the optical dipole trap for 4 s before loading the lattice. After heating, the maximum detected occupation decreases from 0.89(1) to 0.84(1), with a slight broadening of the density profile, whereas the largest magnitude of the nearest-neighbor correlator decreases from 0.154(3) to 0.052(6). In this regime, where the exchange energy is much smaller than both  $U$  and the bandwidth, an increase in temperature quickly saturates the entropy available in the spin degree of freedom while creating little entropy in the charge degree of freedom, making the nearest-neighbor correlator much more sensitive than the density to temperature changes. For the colder data, we observe significant negative correlations in  $C_{1.4}(\mathbf{r})$  away from half-filling, which requires further theoretical investigation.

We take azimuthal averages along the equipotentials of the underlying harmonic trap to obtain  $\overline{n}_{\mathrm{det}}(r)$  and  $C_d(r)$ . The resulting profiles are simultaneously fit to the results of a numerical linked-cluster expansion (NLCE) of the 2D Hubbard model under a local density approximation (LDA) (24-26). From these fits, we obtain a temperature  $k_{B}T / t = 0.54(7)$  and chemical potential  $\mu /U = 0.52(1)$  for the cooler data and  $k_{B}T / t = 1.53(18)$  and  $\mu /U = 0.33(1)$  for the hotter data. The excellent agreement with theory

![](images/69d8c968e8d7d6d2152660d0c8208e74f147333be0c751d7d17cdab16f963226.jpg)

![](images/9419b92c8b1cdb20771dbcfd95959eb5f481d3a7bfb988d36fa303147d79ac0c.jpg)

![](images/152ecc15c2862b0c13867a7e94397ab89d69b034b166113917e937859e405f0d.jpg)

![](images/2f845099ed2b4381db6b912bdebe91434500bcf1028e92a2f48f63427f9c4973.jpg)  
Fig. 3. Thermalization dynamics during lattice loading. (A) (Upper) Detected density.

![](images/f4b48d4190badc9484441c106713889489784f1e17e5f75246a7447fbf4be7ef.jpg)

![](images/9a293ab05e8bfe9081e8b038ea3bea07ebc41e1c928e960c02bec3e96d2a8b70.jpg)

(Lower) The nearest- and diagonal next-nearest-neighbor spin correlator. Both are measured at  $r_{\mathrm{max}}$  as a function of lattice loading time  $t_L$  where  $r_{\mathrm{max}}$  is the radius where  $\overline{n}_{\mathrm{det}}$  is maximized.

(B) Computed  $\chi_{\mathrm{red}}^2$  of simultaneous fits of the density and nearest-neighbor correlator profiles to NLCE data. A value  $\chi_{\mathrm{red}}^2 \approx 1$  indicates a good fit, consistent with our model, which assumes thermal equilibrium.  $\chi_{\mathrm{red}}^2$  settles to approximately 1 at a lattice loading time of  $20~\mathrm{ms}$ , indicated by the shaded region. (C) Sample profile fits for three different loading times.

provides a strong indication that the local density approximation and the assumption of thermal equilibrium are valid.

By evaporatively cooling further before lattice loading, we are able to prepare samples with even larger nearest-neighbor correlations. However, for this data, the NLCE theory error is too large away from half-filling for the fit to converge, owing to the low temperature. Because the averaged correlator in the center may not be at exactly half-filling, by comparing this value for the coldest data set to a quantum Monte Carlo (QMC) calculation at half-filling (22), we can determine an upper bound on the temperature. The correlator value of  $-0.190(8)$  gives  $k_{B}T / t < 0.45(2)$ , the lowest temperature reported for a Hubbard-regime cold-atom system. The QMC calculation predicts that the nearest-neighbor correlator settles as  $T\to 0$  to a value of  $-0.36$ ; our largest measured nearest-neighbor correlation is therefore  $53\%$  of the largest predicted value. In Fig. 2D, we plot our largest measured value of the correlator for samples prepared at different temperatures, the temperature derived from the NLCE fits where they converge ( $x$  axis), and the QMC upper bound.

We find very good agreement between our data and theoretical prediction, which is consistent with half-filling at the cloud center.

We see statistically significant antiferromagnetic correlations to distances of three sites, and the sign of every measured correlator value is consistent with antiferromagnetic ordering. Our ability to measure correlations at all length scales allows us to directly extract the correlation length (Fig. 2E). Samples are prepared at three different temperatures, with the atom number optimized to achieve half-filling in the center of the cloud. Values for the correlator are taken by averaging the spatial maps over a region in the center of the cloud with a six-site radius. To determine the correlation length, we perform an exponential fit of  $(-1)^{i}C_{d}$  in the center of the cloud versus  $d$  where  $i = 0$  (1) if  $d$  is such that the two sites are on the same (different) sublattice. The correlation lengths are 0.24(9), 0.39(2), and 0.51(4) sites for temperatures of  $k_{B}T / t = 1.53(18)$ , 0.54(7), and 0.45(2), respectively. The asterisk in Fig. 2, D and 2 shows the QMC prediction of -0.36 for the nearest-neighbor correlator at half-filling as  $T\rightarrow 0$ .

![](images/a39b679f17bd54112fce20e7d88c105df047094731dac13a0bc4f7a9ecc0fbbd.jpg)  
Fig. 4. Varying the interaction strength. Nearest-neighbor correlator at half-filling for varying scattering length. The top  $y$  axis gives computed values of  $U / t$  for each scattering length (24). The solid lines are isothermal theory curves from the NLCE theory.

Quantum gas microscopy also allows for a detailed study of the thermalization of the atomic cloud when loading into the lattice. We investigate the formation of spin correlations and the thermalization of the density distribution for different lattice loading times in Fig. 3. For these data the lattice is ramped on linearly with a varying duration  $t_{L}$ . We determine the radius  $r_{\mathrm{max}}$ , where  $\overline{n}_{\mathrm{det}}(r)$  is maximized. For a cloud in thermal equilibrium with  $r_{\mathrm{max}}$  not in the center of the cloud,  $r_{\mathrm{max}}$  corresponds to half-filling  $(\mu = U / 2)$ . Figure 3A shows  $\overline{n}_{\mathrm{det}}(r_{\mathrm{max}})$  and  $C_d(r_{\mathrm{max}})$  as a function of loading time. The detected density grows from 0.6 at very short loading times and settles at about 0.9 for  $t_{L} = 10$  ms. The loading time required for the density to settle also corresponds to the maximum absolute values for both the nearest-neighbor and diagonal next-nearest-neighbor spin correlators. The matching time scales suggest that the suppression of magnetic correlations at  $t_{L} < 10$  ms is caused by the low initial density and not by exchange dynamics. The density at short loading times is determined by the confinement of the optical dipole trap preceding the lattice loading (I2). For loading times larger than 10 ms, both  $(-1)^i C_d(r_{\mathrm{max}})$  and  $\overline{n}_{\mathrm{det}}(r_{\mathrm{max}})$  decay, consistent with heating. The faster decay of  $(-1)^i C_d(r_{\mathrm{max}})$  is further indication that the spin correlators are much more sensitive than the density to temperature in this regime of parameters.

We also study thermalization by fitting the data for different loading times to the NLCE theory and performing a reduced chi-squared  $(\chi_{\mathrm{red}}^{2})$  analysis. Figure 3B shows  $\chi_{\mathrm{red}}^2$  versus loading time, and Fig. 3C shows individual NLCE fits at  $t_L$  of  $0.4\mathrm{ms}$ $20~\mathrm{ms}$  and  $150~\mathrm{ms}$  from top to bottom. The value of  $\chi_{\mathrm{red}}^2$  settles to approximately 1 on a  $20 - \mathrm{ms}$  time scale, which is slightly longer than the settling times for the density and spin correlator. The value of  $\chi_{\mathrm{red}}^2$  remains near unity up to our largest loading times, showing that the density and spin-correlator distributions remain consistent with thermal equilibrium.

Whereas in Bose-Hubbard systems AFM correlations appear only in the Heisenberg limit  $U \gg t$ , Fermi-Hubbard systems exhibit AFM correlations at all  $U / t$ , with a maximum in the correlations occurring near  $U / t = 8$ . For large  $U / t$ , AFM correlations are suppressed because the exchange energy becomes small compared with the temperature. For  $U / t < 8$ , where the interaction energy is smaller than the bandwidth, charge fluctuations destroy the magnetic correlations. We study these effects by varying the scattering length for fixed  $t / h = 970(110) \mathrm{Hz}$ . In Fig. 4, we plot  $C_1(r_{\mathrm{max}})$  versus the scattering length, along with the predictions of the NLCE theory for three different temperatures. We show the calculated  $U / t$  from Wannier functions in the lowest band; for our parameters, corrections to this single-band approximation could play a role (27). The data show the expected dependence on  $U / t$  from the simple picture mentioned above. We also compare our data with theoretical isothermal curves at half-filling. In this comparison, additional factors should be considered. First, the atom number is fixed, so the chemical potential in the center of the cloud varies with  $U / t$ . Second, we anticipate the loading entropy to be approximately fixed, as opposed to the temperature, so the data are not expected to strictly follow a single isotherm. The comparison of data with the theory reflects differences between the thermodynamic preparation of atomic and conventional solid-state systems.

Our ability to observe the in situ, site-resolved distribution of spin correlations at all distances has enabled high-precision comparison with numerical studies and detailed verification that the atomic sample behaves in a manner consistent with thermal equilibrium. These experimental benchmarks on thermal equilibrium affirm our understanding of the entropy distribution, paving the way for the implementation of entropy redistribution techniques to achieve finite-system-size long-range order (28, 29). Implementation of such techniques would require precise trap-shaping protocols, which have been fruitfully demonstrated in bosonic quantum gas microscopes (30). Numerical simulations provide evidence that a pseudogap phase in the hole-doped 2D Hubbard model arises in conjunction with long-range AFM correlations (31) and should therefore be accessible in our experiment in the near future. At lower temperatures of  $k_{B}T / t\sim 0.03$  a d-wave superconductor is expected (32). Further thought is required to understand how the real-space observables that we can measure might shed light on these low-temperature phases. Beyond equilibrium physics, we could also exploit our ability to take temporally resolved snapshots of the correlations in a many-body wave function, allowing for in-depth studies of nonequilibrium physics beyond the capability of existing theoretical tools (33).

# REFERENCES AND NOTES

1. P. W. Anderson, Science 235, 1196-1198 (1987).  
2. P. Lee, N. Nagaosa, X.-G. Wen, Rev. Mod. Phys. 78, 17-85 (2006).

3. T. Esslinger, Annu. Rev. Condens. Matter Phys. 1, 129-152 (2010).  
4. I. Bloch, J. Dalibard, S. Nascimbène, Nat. Phys. 8, 267-276 (2012).  
5. D. Greif, T. Uehlinger, G. Jotzu, L. Tarruell, T. Esslinger, Science 340, 1307-1310 (2013).  
6. R. A. Hart et al., Nature 519, 211-214 (2015).  
7. E. Haller et al., Nat. Phys. 11, 738-742 (2015).  
8. L. W. Cheuk et al., Phys. Rev. Lett. 114, 193001 (2015).  
9. M. F. Parsons et al., Phys. Rev. Lett. 114, 213002 (2015).  
10. G. J. A. Edge et al., Phys. Rev. A 92, 063406 (2015).  
11. A. Omran et al., Phys. Rev. Lett. 115, 263001 (2015).  
12. D. Greif et al., Science 351, 953-957 (2016).  
13. L. W. Cheuk et al., Phys. Rev. Lett. 116, 235301 (2016).  
14. W. S. Bakr et al., Science 329, 547-550 (2010)  
15. J. F. Sherson et al., Nature 467, 68-72 (2010).  
16. E. Cocchi et al., Phys. Rev. Lett. 116, 175301 (2016).  
17. P. M. Preiss et al., Science 347, 1229-1233 (2015).  
18. R. Islam et al., Nature 528, 77-83 (2015).  
19. T. Fukuhara et al., Nature 502, 76-79 (2013).  
20. S. Hild et al., Phys. Rev. Lett. 113, 147205 (2014)  
21. N. D. Mermin, H. Wagner, Phys. Rev. Lett. 17, 1133-1136 (1966).  
22. T. Paiva, R. Scalettar, M. Randeria, N. Trivedi, Phys. Rev. Lett. 104, 066406 (2010).  
23. G. Zurn et al., Phys. Rev. Lett. 110, 135301 (2013).  
24. See the supplementary materials on Science Online.  
25. E. Khatami, M. Rigol, Phys. Rev. A 84, 053611 (2011).  
26. S. Chiesa, C. N. Varney, M. Rigol, R. T. Scalettar, Phys. Rev. Lett. 106, 035301 (2011).  
27. H. P. Buchler, Phys. Rev. Lett. 104, 090402 (2010).  
28. J.-S. Bernier et al., Phys. Rev. A 79, 061601 (2009).  
29. T.-L. Ho, Q. Zhou, Proc. Natl. Acad. Sci. U.S.A. 106, 6916-6920 (2009).  
30. P. Zupancic et al., Opt. Express 24, 13881-13893 (2016).  
31. A. Macridin, M. Jarrell, T. Maier, P. R. C. Kent, E. D'Azevedo, Phys. Rev. Lett. 97, 036401 (2006).  
32. E. Gull, O. Parcollet, A. J. Millis, Phys. Rev. Lett. 110, 216405 (2013).  
33. J. Eisert, M. Friesdorf, C. Gogolin, Nat. Phys. 11, 124-130 (2015).  
34. M. Boll et al., Science 353, 1257-1260 (2016).  
35. L. W. Cheuk et al., Science 353, 1260-1264 (2016).

# ACKNOWLEDGMENTS

We thank E. Khatami and M. Rigol for providing the NLCE calculations, as well as T. Paiva and N. Trivedi for the Quantum Monte Carlo calculations at half-filling. We also thank J. P. F. LeBlanc and E. Gull for providing additional data based on a dynamical cluster expansion, used for theory verification. We thank E. Demler, A. Eberlein, F. Grusdt, J. Hoffman, A. Kaufman, M. Kanasz-Nagy, M. Lemeshko, L. Tarruell, L. Cheuk, M. Nichols, K. Lawrence, M. Okan, H. Zhang, and M. Zwierlein for insightful discussions. Recently, antiferromagnetic correlations have been observed in the Munich lithium quantum gas microscope and the MIT potassium quantum gas microscope (34, 35). We acknowledge support from the Air Force Office of Scientific Research, the Multi-University Research Initiative, and NSF. D.G. acknowledges support from the Harvard Quantum Optics Center and the Swiss National Foundation. M.F.P., A.M., and C.S.C. acknowledge support from the NSF. The authors declare no competing financial interests.

# SUPPLEMENTARY MATERIALS

www.sciencemag.org/content/353/6305/1253/suppl/DC1

Supplementary Text

Figs. S1 to S6

Table S1

Reference (36)

13 May 2016; accepted 18 August 2016

10.1126/science.aag1430

This copy is for your personal, non-commercial use only.

Article Tools Visit the online version of this article to access the personalization and article tools: http://science.sciencemag.org/content/353/6305/1253

Permissions Obtain information about reproducing this article: http://www.sciencemag.org/about/permissions.dtl