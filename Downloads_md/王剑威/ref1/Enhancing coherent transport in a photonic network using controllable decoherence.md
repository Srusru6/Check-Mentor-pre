ARTICLE

Received 16 Jul 2015 | Accepted 8 Mar 2016 | Published 15 Apr 2016

DOI: 10.1038/ncomms11282

OPEN

# Enhancing coherent transport in a photonic network using controllable decoherence

Devon N. Biggerstaff<sup>1</sup>, René Heilmann<sup>2</sup>, Aidan A. Zecevik<sup>1</sup>, Markus Gräfe<sup>2</sup>, Matthew A. Broome<sup>1,†</sup>, Alessandro Fedrizzi<sup>1,3</sup>, Stefan Nolte<sup>2</sup>, Alexander Szameit<sup>2</sup>, Andrew G. White<sup>1</sup> & Ivan Kassal<sup>1</sup>

Transport phenomena on a quantum scale appear in a variety of systems, ranging from photosynthetic complexes to engineered quantum devices. It has been predicted that the efficiency of coherent transport can be enhanced through dynamic interaction between the system and a noisy environment. We report an experimental simulation of environment-assisted coherent transport, using an engineered network of laser-written waveguides, with relative energies and inter-waveguide couplings tailored to yield the desired Hamiltonian. Controllable-strength decoherence is simulated by broadening the bandwidth of the input illumination, yielding a significant increase in transport efficiency relative to the narrowband case. We show integrated optics to be suitable for simulating specific target Hamiltonians as well as open quantum systems with controllable loss and decoherence.

Recent research into photosynthetic antenna complexes has shown evidence of coherence in excitonic energy transport $^{1-4}$ , despite the noisy cellular environment in which such complexes are found. Indeed, environmental decoherence has been credited with increasing the efficiency of transport through these systems, an effect known as environment-assisted quantum transport (ENAQT) $^{5}$  or dephasing-assisted transport $^{6,7}$ . While ENAQT has been the subject of many theoretical studies—whether in the photosynthetic context $^{8-16}$  or in other nanoscale transport systems $^{17-20}$ —and despite its potential for improving transport in artificial quantum systems, it has so far never been directly observed.

ENAQT can be understood by considering a single excitation on a network of  $N$  coupled sites, governed by a tight-binding Hamiltonian<sup>5</sup>

$$
H = \sum_ {m = 1} ^ {N} \varepsilon_ {m} | m \rangle \langle m | + \sum_ {n <   m} ^ {N} V _ {m n} (| m \rangle \langle n | + | n \rangle \langle m |), \tag {1}
$$

where  $|m\rangle$  denotes the excitation being localized at site  $m$ ,  $\varepsilon_{m}$  the energy of that site and  $V_{mn}$  the coupling between sites  $m$  and  $n$ . Although ENAQT can occur on an ordered lattice where all the energies  $\varepsilon_{m}$  are equal[21], transport enhancement was first explained in disordered systems, which we consider here.

In most studies, ENAQT is about the efficiency of transport from a particular initial site to a particular target site, where the excitation is irreversibly trapped. In the case of a photosynthetic complex (Fig. 1a), trapping describes the transfer of excitons to a reaction center, where they drive charge separation. It can be modelled as irreversible coupling of the target site to a sink at rate  $\kappa$ . The efficiency is usually defined as the probability of finding the exciton in the sink after a certain time or, more commonly, in the long-time limit.

ENAQT occurs when adding decoherence increases the trapping probability above the fully coherent case. In general, decoherence results from coupling of a quantum system to inaccessible degrees of freedom. For example,

in photosynthetic antenna complexes, the energies of chromophores are coupled to molecular vibrations; tracing out this environment results in decoherence in the excitonic subspace.

ENAQT can be understood in several different ways: as suppression of destructive interferences, as bringing of neighbouring sites into resonance, or as transitions between otherwise-stationary eigenstates. The first of these interpretations starts from the fact that energetic disorder tends to localize the wavepacket through processes such as destructive interference or Anderson localization[22-24], thus preventing it from reaching the target. Adding decoherence diminishes these coherent processes, increasing the transport efficiency to the target. The second view is that decoherence—if it is in the site basis, as is often assumed—can be modelled as fluctuations of site energies. On that view, increasing fluctuations enhance site-to-site transfer by bringing neighbouring sites into transient resonance more frequently. The third approach is to note that the eigenstates of  $H$  are stationary in the absence of decoherence, making it difficult to reach the target if the initial and target sites differ in energy. Incoherent processes, however, permit transitions between the eigenstates of  $H$ , yielding greater mobility. Finally, in some specialized cases ENAQT can also be understood as an instance of a phonon antenna[25] or of momentum rejuvenation[26].

The earliest theoretical studies of ENAQT focused on the case where the decoherence takes the form of site-independent, Markovian, pure dephasing $^{5,6}$ . However, any form of decoherence, including non-Markovian ones $^{27,28}$ , can increase transport efficiency as long as it allows population transfer between otherwise-stationary eigenstates.

Here we use an integrated photonic simulator to demonstrate the first implementation of ENAQT. Our simulator was fabricated using femtosecond-laser direct writing, which allows waveguides to be drawn directly into glass using a focused, pulsed laser. This permits the creation of three-dimensional waveguide arrays, as well as precision and repeatability in engineering

![](images/4b4bc0d559bb236b7d0c84a90a9dcdc8a436849e84b846149cd567928701c345.jpg)  
Figure 1 | Environment-assisted quantum transport (ENAQT). (a) Photosynthetic antenna complexes are networks of chlorophylls that collect and transfer solar energy. A well-studied example is the Fenna-Matthews-Olson complex of green sulphur bacteria, here depicted as a network of seven sites that transports excitation energy from initial site 1 to target site 3 (adapted with permission from ref. 49). Simulations have suggested that this transport may be enhanced by decoherence $^{5-7}$ . (b) We simulate an instance of ENAQT on a lattice of four sites, with site 1 initially excited and site 3 the target. If the detuning  $\Delta \beta$  of site 4 equals  $C$ , one of the system eigenmodes has no occupancy at site 3 and cannot couple to the sink; by broadening the levels, decoherence breaks the condition  $\Delta \beta = C$ , allowing all eigenmodes to couple to the sink and thus increasing transport efficiency. (c) Our simulator consists of four coupled waveguides arranged as shown (cross-section). The sink is modelled with a large array of closely coupled waveguides that transport light away from the main four waveguides. At the central wavelength  $\lambda_0$ , waveguide 4 has propagation constant  $\beta + \Delta \beta$ , while the others have propagation constant  $\beta$ . (d) Theoretical expectation of transport enhancement for this system, as a function of simulation length  $z$  and decoherence strength  $\gamma$ . The red bar indicates the region explored experimentally.

![](images/25223937d967c4f371045ab4ad118c6908f76718196edf5f4d6b320ca3dc7c63.jpg)

![](images/d85675a0767fc31c491d6371236e47cbed112e078dee0023bf7e8357640605fb.jpg)

![](images/047def92bcc3486883fab3577a7c8865a7052bd8929703ae06d8f186fb70ca8a.jpg)

interactions $^{29-36}$ . We use control over the wavelength and bandwidth of the guided light to simulate effective decoherence, thereby enhancing transport efficiency.

# Results

Theoretical model. We simulate ENAQT in an array of coupled single-mode optical waveguides obeying the equation<sup>37,38</sup>

$$
i \frac {\partial}{\partial z} a _ {m} ^ {\dagger} (z) = \beta_ {m} a _ {m} ^ {\dagger} (z) + \sum_ {n \neq m} ^ {N} C _ {m n} a _ {n} ^ {\dagger} (z), \tag {2}
$$

where the light is propagating in the  $z$  direction,  $a_{m}^{\dagger}(z)$  is a creation operator for a photon in waveguide  $m$  at position  $z$ , and  $\beta_{m}$  and  $C_{mn}$  are the propagation constants of the waveguides and the couplings between them, respectively. The former are determined by the waveguides' refractive index profiles, while the latter also depend on the separations between them. Light propagation governed by this Schrödinger-like equation directly simulates evolution under  $H$ , with  $C_{mn}$  replacing  $V_{mn}$  and the  $\beta_{m}$  replacing  $\varepsilon_{m}$ . We can thus simulate different Hamiltonians by controlling the number, position and refractive indices of the waveguides.

The intrinsic stability of laser-written waveguide arrays renders decoherence challenging to simulate. One approach is to stochastically modulate the index of refraction along each waveguide $^{39}$ . Although every realization with a particular longitudinal index profile will be fully coherent, decoherence can be simulated by averaging over the recorded optical outputs from many realizations in post-processing. This approach was recently used to simulate decoherence-enhanced navigation of a maze $^{40}$ .

By contrast, we simulate decoherence by averaging over the results from a single array illuminated with many optical wavelengths. Although each individual wavelength propagates through the waveguide array coherently, effective decoherence can be achieved using broadband illumination and a single output intensity measurement that does not resolve wavelength. In other words, the wavelength degree of freedom is traced out yielding a partially mixed state. Similar approaches are well established in optics, where, for instance, thick birefringent quartz plates followed by wavelength-insensitive measurements have been used to decohere the polarization states of single photons[41,42].

As an example of our approach to simulating decoherence, we consider two uncoupled waveguides  $a$  and  $b$  that have a difference  $\Delta \beta$  in their propagation constants at a wavelength  $\lambda_0$ . As light propagates along the waveguides, it will accumulate a phase difference  $z\Delta \beta$  between them. Broadband illumination can then be seen to cause effective decoherence on a length scale comparable to the illumination coherence length. Any initial coherence  $\rho_{ab}$  between the waveguides will decay as

$$
\rho_ {a b} (z) = \rho_ {a b} (0) g ^ {(1)} \left(\frac {z \Delta \beta \lambda_ {0}}{2 \pi c}\right), \tag {3}
$$

where  $g^{(1)}(t)$  is the normalized first-order temporal correlation function of the light, which—being proportional to the Fourier transform of the spectrum—decays to zero faster for spectrally broader illumination. Because Markovian dephasing causes exponential decays of coherences, the dephasing in equation (3) is non-Markovian unless the light has a Lorentzian spectrum.

The overall strength  $\gamma$  of the decoherence can be quantified as the inverse of the optical coherence length,  $\gamma = \left(\frac{2\pi c}{\Delta\beta\lambda_0}\int_{-\infty}^{\infty}\left|g^{(1)}(\tau)\right|^2 d\tau\right)^{-1}$ , and is usually proportional to the full-width at half-maximum bandwidth  $\Delta \lambda$ . For a uniform

distribution centred at  $\lambda_0$

$$
\gamma = \frac {\Delta \beta \Delta \lambda}{2 \pi \lambda_ {0}}. \tag {4}
$$

In the case of coupled waveguides, wavelength dependence affects couplings in addition to the propagation constants. The resulting decoherence will therefore not only have characteristics of pure dephasing (as in equation (3)), but will also include off-diagonal terms. However, this kind of decoherence can also result in ENAQT. Indeed, the off-diagonal terms imply that our decoherence could, in principle, be used to simulate ENAQT in ordered systems $^{21}$ , but the effect would be weaker because of the absence of the pure-dephasing contribution when  $\Delta \beta = 0$ .

Experimental results. For our simulation, we chose the network of four sites shown in Fig. 1b because it is one of the smallest systems in which ENAQT is possible and because it can give significant enhancements even with relatively weak decoherence. We simulated this network using waveguides arranged as in Fig. 1c, where waveguide 1 was the input, waveguide 3 the target and the sink consisted of a long linear array of tightly coupled waveguides. The coupling between waveguides in this sink was significantly higher than between the four main waveguides, so that any light entering the sink from waveguide 3 was largely transported away[43-45]. The sink need only be long enough to prevent light reflected from the far end from returning into the main simulation waveguides.

We chose propagation constants and separations among the four main waveguides in order to best approximate the Hamiltonian corresponding to Fig. 1b,

$$
H = \left( \begin{array}{c c c c} \beta & C & 0 & 0 \\ C & \beta & C & 0 \\ 0 & C & \beta & C \\ 0 & 0 & C & \beta + \Delta \beta \end{array} \right), \tag {5}
$$

where all parameters depend on the wavelength  $\lambda$  of the input light. Due to their wide separations, couplings between non-neighbouring sites are negligible ( $< 5\%$  of neighbouring-site couplings). Our simulator is designed so that, at our central simulation wavelength  $\lambda_0$ ,

$$
\Delta \beta (\lambda_ {0}) = C (\lambda_ {0}). \tag {6}
$$

In this case, one of the eigenstates of  $H$  has no support on site 3,  $|\psi_{1}\rangle = (-1, -1,0,1) / \sqrt{3}$ , while the remaining three eigenstates all have substantial support on site 3. Because  $|\psi_{1}\rangle$  cannot couple to the sink—at least at  $\lambda_0$ —the maximum trapping efficiency at infinite time is  $\eta = 1 - \langle 1|\psi_1\rangle = 2 / 3$ .

Considering the wavelength dependence of  $H$  provides a different way to see the decohering effects of broadband illumination. Due to the dependence of  $\beta$  and  $C$  on the wavelength, equation (6) only holds at a particular wavelength  $\lambda_0$ . At other wavelengths,  $|\psi_1\rangle$  will have some support on waveguide 3 and thus be able to couple to the sink, increasing the efficiency above  $2/3$ , as shown in Fig. 1d. Unlike in other examples of ENAQT<sup>5</sup>, the efficiency increases monotonically with the strength of decoherence, meaning there is no optimal level of decoherence in this model.

On the basis of measurements of couplings and propagation constants in isolated pairs of waveguides (see Methods xsection), we selected the following design parameters:  $\Delta \beta = C = 1.0\mathrm{cm}^{-1}$ ,  $C_{\mathrm{trap}} = 1.5\mathrm{cm}^{-1}$ , and  $C_{\mathrm{sink}} = 1.75\mathrm{cm}^{-1}$  (Fig. 1c). Figure 2a shows numerical modelling of light propagation given these parameters. Although these were designed for a center wavelength of  $800\mathrm{nm}$ , variations in the implementation of the waveguide parameters resulted in equation 6 being satisfied at  $\lambda_0 = 792.5\mathrm{nm}$ .

![](images/1a72b1028717ae430b7cb3366ed7eec743d61f2ef8ca34c6ee268086d7adfff1.jpg)  
Figure 2 | Experimental setup and waveguide design. (a) Predicted dynamics of light in our waveguide array, as a function of  $z$ . The inset shows the predicted device output distribution for input at wavelength  $\lambda_0$ . The sink array is sufficiently long that light reflecting from the far boundary fails to couple back into the system waveguides during the simulation. (b) A fibre-coupled, tunable Ti:sapphire laser in quasi-cw mode undergoes polarization control (Pol) before it is imaged into the sample using a 15 mm focal-length aspheric lens. The output is imaged via a  $14 \times$  telescope onto a variable slit, which collectively measures the total intensity output from the system, bath or all the waveguides using a large-area power-meter (PM). Alternatively, the output can be imaged onto a CCD camera for alignment and diagnostics. (c) CCD images of the output after 15 cm when illuminated at  $\lambda_0 = 792.5$  nm and at 830 nm. As designed, the light in the system waveguides is evenly distributed at  $\lambda_0$  apart from the target site, which is dark. In contrast, the target site is much brighter at 830 nm, indicating that more light will couple into the sink—a sign of ENAQT.

![](images/6031f82acc1480695c4fe24b0f62b2c847b49324bd6b7fb1a288abec09efe558.jpg)

![](images/34efb6fffa1c5a000f4a8e435252de363ac479392a968f78890871c4b4264f0a.jpg)

![](images/b886877fc67ab0df5e94b64b2dd95f3c91d7310a3075c59be59ef8b479c62cf4.jpg)  
Figure 3 | Magnitude of observed ENAQT. (a) Transport efficiency—the portion of light that makes it to the sink—as a function of wavelength. The minimum efficiency at  $\lambda_0 = 792.5\mathrm{nm}$  is  $\eta = 0.636\pm 0.002$  slightly less than the theoretical infinite time limit of  $2 / 3$ . The error bars are s.d. caused by imperfect repeatability in coupling light into the sample and laser power fluctuations. (b) ENAQT—the relative increase in the efficiency over that at  $\lambda_0$  as a function of the optical bandwidth (top horizontal axis) and corresponding decoherence strength  $\gamma$  (bottom horizontal axis). The red points are obtained by averaging the measured efficiencies over a uniform broadband spectrum with width  $\Delta \lambda$  and centred at  $\lambda_0$ . The blue line represents the theoretical ENAQT, calculated based on the model in Fig. 1b and containing no free parameters (it is the cross-section of Fig. 1d along the red line segment). The shaded region represents possible ENAQT if  $\Delta \beta (\lambda_0)$  deviates from  $C(\lambda_0)$  by up to  $10\%$ .

![](images/702540db816cde52ac419793e9ecded55867afe4b56bdba05e56eeb281ed22b9.jpg)

Our experimental setup is shown in Fig. 2b. We measured the efficiency using narrowband light (less than  $1\mathrm{nm}$  bandwidth and always horizontally polarized for consistency) from a tunable Ti:sapphire laser (Spectra-Physics Tsunami) in quasi-cw mode (Fig. 2b). The output was imaged using a custom-built  $14\times$  magnifying telescope and the optical power was measured using a large-area power-meter after isolating either the system or sink waveguides using a variable slit. Examples of the output distribution are given in Fig. 2c, showing the significant difference between illumination at  $\lambda_0$  and an off-centre wavelength. Figure 3a shows the measured efficiency (fraction of light output in the sink modes) for wavelengths ranging from 745 to  $835\mathrm{nm}$ .

ENAQT—shown in Fig. 3b—is the average enhancement in efficiency over the spectral band of interest, relative to the efficiency at  $\lambda_0$ ,

$$
\mathrm {E N A Q T} = \frac {\left\langle \eta (\lambda) \right\rangle - \eta \left(\lambda_ {0}\right)}{\eta \left(\lambda_ {0}\right)}, \tag {7}
$$

where the average  $\langle \dots \rangle$  over  $\lambda$  is taken over the top-hat distribution on  $(\lambda_0 - \frac{1}{2}\Delta \lambda, \lambda_0 + \frac{1}{2}\Delta \lambda)$ . As predicted, it is an increasing function of the bandwidth, that is, of the decoherence strength  $\gamma$ . The highest ENAQT observed was  $(7.6 \pm 1.2)\%$  at a bandwidth of  $95\mathrm{nm}$ . We thus demonstrated that coherent transport in a coupled, statically disordered system can be enhanced through decoherence.

# Discussion

The theoretical prediction in Fig. 3b contains no free parameters. It is a simulation of the dynamics under the simulated Hamiltonian  $H$ , together with trapping from site 3 at the rate  $\kappa$ , discussed in Methods section, and pure dephasing between waveguide 4 and the other three waveguides at the rate  $\gamma$ . The disagreement between theory and experiment is small considering the number of possible contributing factors. These include the off-diagonal decoherence when the waveguides are coupled, the fact that the trapping is not perfectly exponential, errors in the measurements of the coupling constants, optical losses and error in satisfying equation 6. As an example, the shaded band in Fig. 3b represents the error that would arise if  $\Delta \beta (\lambda_0)$  deviated from  $C(\lambda_0)$  by up to  $10\%$ .

In our experiment, the magnitude of ENAQT was limited by the maximum achievable decoherence, which at  $\gamma = 0.02\mathrm{cm}^{-1}$  was small compared with the inverse of the propagation length. We were limited by two components of equation (4): the tunability of our laser limited  $\Delta \lambda$ , while  $\Delta \beta$  was limited (via equation (6)) by the need to keep  $C$  small enough to stay in the tight-binding approximation. These are not fundamental limitations, and future improvements that increase  $\gamma$  would result in significantly larger transport enhancement; as shown in Fig. 1d, the transport efficiency of this model can get arbitrarily close to 1 for sufficiently long propagation distances and decoherence strengths. Stronger decoherence would also allow ENAQT to be observed in networks that are less sensitive to decoherence than our model.

Our results demonstrate that integrated photonics is well-suited for simulating open quantum systems and capable of implementing a disordered target Hamiltonian with controllable loss. Using broadband excitation to introduce tunable levels of decoherence is the first technique to simulate an open-quantum system in a photonic architecture; previously, low intrinsic noise in photonic devices rendered decoherence difficult to realize in integrated optics, particularly without averaging over results from many different device realizations. Future work will determine the full range of decoherence processes that can be simulated in this way (for example, by modifying the illumination spectrum) as well as ways to extend it to enable the simulation of a greater range of open-quantum systems. Controllable decoherence will not only enhance photonic simulation, but will also permit photonic implementations of quantum-computational methods that take advantage of decoherence[46-48]. In addition, analogies with and extensions of our approach will aid in the experimental optimization of transport in other engineered quantum systems.

# Methods

Waveguide fabrication. The waveguides were fabricated in high-purity fused silica (Corning 7980) using a laser direct-write technique whereby Ti:sapphire laser pulses are tightly focused into the sample, which is then translated in three dimensions to yield continuous regions of positive refractive index change, which act as waveguides $^{30}$ . To obtain single-mode waveguides with the desired propagation and coupling characteristics, laser pulses of duration 150 fs, energy  $400\mu \mathrm{J}$ , central wavelength  $800\mathrm{nm}$  and repetition rate  $100\mathrm{kHz}$  were focused  $400\mu \mathrm{m}$  below the surface using a  $\times 40$  microscope objective and translated at  $75\mathrm{mm}\mathrm{min}^{-1}$  (for waveguides other than 4).

Permanent index changes result in the focus, yielding elliptical, vertically oriented, single-mode waveguides with modes  $\sim 17\times 19\mu \mathrm{m}$  in size at  $800\mathrm{nm}$ . Waveguide 3 and the sink waveguides are in a plane parallel to the surface, while angles of  $120^{\circ}$  between this plane and the other system waveguides minimize non-neighbour coupling. Because couplings between elliptical waveguides are dependent on angular orientation[29], we determined the couplings by writing pairs of waveguides oriented at the specified angles. Couplings as a function of separation were determined by writing the pairs at different separations and measuring the output intensities after a known propagation length when only one is optically excited.

The final waveguide separations were chosen to ensure that the tight-binding approximation is maintained, that  $C$  can be matched by  $\Delta \beta$ , that  $C_{\mathrm{sink}} > C_{\mathrm{trap}} > C$  and that the number of sink modes remains manageable. The system-sink population transfer can be modelled as a constant effective rate[43]  $\kappa = 2x^{2}(1 - x^{2})^{-1 / 2}$  if  $x\equiv C_{\mathrm{trap}} / C_{\mathrm{sink}}\ll 1$ . In our case, although  $x = 0.86$  meant

that the decay was not perfectly exponential, it was nevertheless effectively irreversible, considering that sufficiently many sink modes were present to prevent reflection from the far end and back into the main waveguides.

For waveguide 4, the writing translation speed was decreased in order to increase the propagation constant. In a pair of waveguides with mismatched propagation constants, the maximum power transfer depends only on the ratio  $\Delta \beta / C$ . We used this fact to determine the translation speed decrease necessary to set  $\Delta \beta = C$  at  $800\mathrm{nm}$ . Due to the measurement uncertainty (about  $8\%$ ) and day-to-day variability in the waveguide writing process, several waveguide arrays were written with slightly different writing speeds for waveguide 4 to ensure that one set would yield  $\Delta \beta = C$  in our desired wavelength range. In the best sample, the writing speed was decreased by  $12\%$ .

# References

1. Engel, G. S. et al. Evidence for wavelike energy transfer through quantum coherence in photosynthetic systems. Nature 446, 782 (2007).  
2. Panitchayangkoon, G. et al. Long-lived quantum coherence in photosynthetic complexes at physiological temperature. Proc. Natl Acad. Sci. USA 107, 12766 (2010).  
3. Collini, E. et al. Coherently wired light-harvesting in photosynthetic marine algae at ambient temperature. Nature 463, 644 (2010).  
4. Wong, C. Y. et al. Electronic coherence lineshapes reveal hidden excitonic correlations in photosynthetic light harvesting. Nat. Chem. 4, 396 (2012).  
5. Rebentrost, P., Mohseni, M., Kassal, I., Lloyd, S. & Aspuru-Guzik, A. Environment-assisted quantum transport. New J. Phys. 11, 033003 (2009).  
6. Plenio, M. B. & Huelga, S. F. Dephasing-assisted transport: quantum networks and biomolecules. New J. Phys. 10, 113019 (2008).  
7. Chin, A., Datta, A., Caruso, F., Huelga, S. & Plenio, M. Noise-assisted energy transfer in quantum networks and light-harvesting complexes. New J. Phys. 12, 065002 (2010).  
8. Mohseni, M., Rebentrost, P., Lloyd, S. & Aspuru-Guzik, A. Environment-assisted quantum walks in photosynthetic energy transfer. J. Chem. Phys. 129, 174106 (2008).  
9. Cao, J. & Silbey, R. J. Optimization of exciton trapping in energy transfer processes. J. Phys. Chem. A 113, 13825 (2009).  
10. Caruso, F., Chin, A. W., Datta, A., Huelga, S. F. & Plenio, M. B. Highly efficient energy excitation transfer in light-harvesting complexes: the fundamental role of noise-assisted transport. J. Chem. Phys. 131, 105106 (2009).  
11. Wu, J., Liu, F., Shen, Y., Cao, J. & Silbey, R. Efficient energy transfer in light-harvesting systems, I: optimal temperature, reorganization energy and spatial-temporal correlations. New J. Phys. 12, 105012 (2010).  
12. Hoyer, S., Sarovar, M. & Whaley, K. B. Limits of quantum speedup in photosynthetic light harvesting. New J. Phys. 12, 065041 (2010).  
13. Fassioli, F. & Olaya-Castro, A. Distribution of entanglement in light-harvesting complexes and their quantum efficiency. New J. Phys. 12, 085006 (2010).  
14. Wu, J., Silbey, R. J. & Cao, J. Generic mechanism of optimal energy transfer efficiency: a scaling theory of the mean first-passage time in exciton systems. Phys. Rev. Lett. 110, 200402 (2013).  
15. Cleary, L. & Cao, J. Optimal thermal bath for robust excitation energy transfer in disordered light-harvesting complex 2 of purple bacteria. New J. Phys. 15, 125030 (2013).  
16. León-Montiel, R., Kassal, I. & Torres, J. P. Importance of excitation and trapping conditions in photosynthetic environment-assisted energy transport. J. Phys. Chem. B 118, 10588 (2014).  
17. Semiao, F. L., Furuya, K. & Milburn, G. J. Vibration-enhanced quantum transport. New J. Phys. 12, 083033 (2010).  
18. Scholak, T., De Melo, F., Wellens, T., Mintert, F. & Buchleitner, A. Efficient and coherent excitation transfer across disordered molecular networks. Phys. Rev. E 83, 021912 (2011).  
19. Scholak, T., Wellens, T. & Buchleitner, A. Optimal networks for excitonic energy transport. J. Phys. B 44, 184012 (2011).  
20. Lim, J., Tame, M., Yee, K. H., Lee, J.-S. & Lee, J. Phonon-induced dynamic resonance energy transfer. New J. Phys. 16, 053018 (2014).  
21. Kassal, I. & Aspuru-Guzik, A. Environment-assisted quantum transport in ordered systems. New J. Phys. 14, 053041 (2012).  
22. Anderson, P. W. Absence of diffusion in certain random lattices. Phys. Rev. 109, 1492-1505 (1958).  
23. Lahini, Y. et al. Anderson localization and nonlinearity in one-dimensional disordered photonic lattices. Phys. Rev. Lett. 100, 013906 (2008).  
24. Segev, M., Silberberg, Y. & Christodoulides, D. N. Anderson localization of light. Nat. Photon. 7, 197-204 (2013).  
25. Huelga, S. F. & Plenio, M. B. Vibrations, quanta and biology. Contemp. Phys. 54, 181-207 (2013).  
26. Li, Y., Caruso, F., Gauger, E. & Benjamin, S. C. 'Momentum rejuvenation' underlies the phenomenon of noise-assisted quantum energy flow. New J. Phys. 17, 013057 (2015).  
27. Mohseni, M., Shabani, A., Lloyd, S. & Rabitz, H. Energy-scales convergence for optimal and robust quantum transport in photosynthetic complexes. J. Chem. Phys. 140, 035102 (2014).

28. Chen, X. & Silbey, R. J. Excitation energy transfer in a non-Markovian dynamical disordered environment: Localization, narrowing, and transfer efficiency. J. Phys. Chem. B 115, 5499 (2011).  
29. Szameit, A., Dreisow, F., Pertsch, T., Nolte, S. & Tünnermann, A. Control of directional evanescent coupling in fs laser written waveguides. Opt. Express 15, 1579 (2007).  
30. Szameit, A. & Nolte, S. Discrete optics in femtosecond-laser-written photonic structures. J. Phys. B 43, 163001 (2010).  
31. Marshall, G. D. et al. Laser written waveguide photonic quantum circuits. Opt. Express 17, 12546-12554 (2009).  
32. Owens, J. O. et al. Two-photon quantum walks in an elliptical direct-write waveguide array. New J. Phys. 13, 075003 (2011).  
33. Corrielli, G., Crespi, A., Della Valle, G., Longhi, S. & Osellame, R. Fractional Bloch oscillations in photonic lattices. Nat. Commun. 4, 1555 (2013).  
34. Poulios, K. et al. Quantum walks of correlated photon pairs in two-dimensional waveguide arrays. Phys. Rev. Lett. 112, 143604 (2014).  
35. Crespi, A. et al. Particle statistics affects quantum decay and Fano interference. Phys. Rev. Lett. 114, 090201 (2015).  
36. Boada, O., Novo, L., Sciarrino, F. & Omar, Y. Quantum walks in synthetic gauge fields with 3D integrated photonics. Preprint at http://arxiv.org/abs/1503.07172 (2015).  
37. Perets, H. B. et al. Realization of quantum walks with negligible decoherence in waveguide lattices. Phys. Rev. Lett. 100, 170506 (2008).  
38. Longhi, S. Quantum-optical analogies using photonic structures. *Laser Photon. Rev.* 3, 243 (2009).  
39. Levi, L., Krivolapov, Y., Fishman, S. & Segev, M. Hyper-transport of light and stochastic acceleration by evolving disorder. Nat. Phys. 8, 912-917 (2012).  
40. Caruso, F., Crespi, A., Ciriolo, A. G., Sciarrino, F. & Osellame, R. Fast escape from quantum mazes in integrated photonics. Preprint at http://arxiv.org/abs/1501.06438 (2015).  
41. Kwiat, P. G., Berglund, A. J., Altepeter, J. B. & White, A. G. Experimental verification of decoherence-free subspaces. Science 290, 498-501 (2000).  
42. Xu, J.-S. et al. Experimental investigation of classical and quantum correlations under decoherence. Nat. Commun. 1, 7 (2010).  
43. Longhi, S. Nonexponential decay via tunneling in tight-binding lattices and the optical Zeno effect. Phys. Rev. Lett. 97, 110402 (2006).  
44. Biagini, P. et al. Experimental demonstration of the optical Zeno effect by scanning tunneling optical microscopy. Opt. Express 16, 3762 (2008).  
45. Delanty, M., Rebic, S. & Twamley, J. Novel collective effects in integrated photonics. Eur. Phys. J. 66, 1 (2012).  
46. Kendon, V. & Tregenna, B. Decoherence can be useful in quantum walks. Phys. Rev. A 67, 042315 (2003).

47. Kendon, V. Decoherence in quantum walks-a review. Math. Struct. Comp. Sci. 17, 1169-1220 (2007).  
48. Verstraete, F., Wolf, M. M. & Cirac, J. I. Quantum computation and quantum-state engineering driven by dissipation. Nat. Phys. 5, 633-636 (2009).  
49. Lambert, N. et al. Quantum biology. Nat. Phys. 9, 10 (2013).

# Acknowledgements

D.N.B., A.A.Z., M.A.B., A.F., A.G.W. and I.K. were supported by Australian Research Council (ARC) Centres of Excellence for Engineered Quantum Systems (CE110001013) and Quantum Computation and Communication Technology (CE110001027). R.H., M.G., S.N. and A.S. thank the German Ministry of Education and Research (Center for Innovation Competence program, 03Z1HN31), the Deutsche Forschungsgemeinschaft (NO462/6-1, SZ 276/9-1, SZ 276/7-1) and the German-Israeli Foundation for Scientific Research and Development (1157-127.14/2011). A.F. and I.K. acknowledge ARC Discovery Early Career Researcher Awards (DE130100240 and DE140100433).

# Author contributions

I.K. developed the theory. D.N.B., I.K., A.F. and A.G.W. conceived the experiment. R.H., M.G. and A.S. designed and fabricated the integrated waveguides. D.N.B., A.A.Z., M.A.B. and R.H. performed the measurements and analysed the data. All authors contributed to writing the manuscript.

# Additional information

Competing financial interests: The authors declare no competing financial interests.

Reprints and permission information is available online at http://npg.nature.com/reprintsandpermissions/

How to cite this article: Biggerstaff, D. N. et al. Enhancing coherent transport in a photonic network using controllable decoherence. Nat. Commun. 7:11282 doi: 10.1038/ncomms11282 (2016).

![](images/fef5792b0113c604fb15da2ae99527b03262b2f576ba2fd8de6ebc5c9102a141.jpg)

This work is licensed under a Creative Commons Attribution 4.0 International License. The images or other third party material in this

article are included in the article's Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder to reproduce the material. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/