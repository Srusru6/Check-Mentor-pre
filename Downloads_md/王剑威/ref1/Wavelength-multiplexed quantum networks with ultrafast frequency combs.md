# Wavelength-multiplexed quantum networks with ultrafast frequency combs

Jonathan Roslund, Renné Medeiros de Araújo, Shifeng Jiang, Claude Fabre and Nicolas Treps*

Highly entangled quantum networks (cluster states) lie at the heart of recent approaches to quantum computing $^{1,2}$ . Yet the current approach for constructing optical quantum networks does so one node at a time $^{3-5}$ , which lacks scalability. Here, we demonstrate the single-step fabrication of a multimode quantum resource from the parametric downconversion of femtosecond-frequency combs. Ultrafast pulse shaping $^{6}$  is employed to characterize the comb's spectral entanglement $^{7,8}$ . Each of the 511 possible bipartitions among ten spectral regions is shown to be entangled; furthermore, an eigenmode decomposition reveals that eight independent quantum channels $^{9}$  (qumodes) are subsumed within the comb. This multicolour entanglement imports the classical concept of wavelength-division multiplexing to the quantum domain by playing upon frequency entanglement to enhance the capacity of quantum-information processing. The quantum frequency comb is easily addressable, robust with respect to decoherence and scalable, which renders it a unique tool for quantum information.

# Theoretical description

The use of photonic architectures to realize quantum networks is appealing because photons are immune from environmental disturbances, readily manipulated with classical tools and subject to high-efficiency detection[10,11]. We consider here the creation of non-classical continuous variable states with an optical parametric oscillator (OPO), in which a pump photon of frequency  $2\omega_0$  splits into a pair of lower-energy photons subject to energy conservation and the cavity resonance condition. The generation of a photon pair initiates a non-classical correlation between the cavity modes  $\omega_{-p}$  and  $\omega_p$ , where  $\omega_p = \omega_0 + p\cdot \omega_{\mathrm{FSR}}$ ,  $\omega_{\mathrm{FSR}}$  is the cavity-free spectral range and  $p$  is an integer. Given a sufficiently large phase-matching bandwidth, a frequency comb emerges from the cavity with all of the resonant photon pairs entangled independently. Quadripartite entangled states have been created efficiently in at least 15 of these resonant photon pairs[12]. When the downconversion is pumped by a comb that contains the frequencies  $2\omega_0 + p'\cdot \omega_{\mathrm{FSR}}$ , these photon pairs become interlinked through the introduction of frequency correlations beyond purely symmetric pair creation. Femtosecond pulse trains contain upwards of  $\sim 10^5$  individual frequency modes, and the simultaneous injection of all these modes into a nonlinear optical element induces an intricate network of both symmetric and asymmetric frequency correlations[13]. To access such states, a synchronously pumped optical parametric oscillator (SPOPO), which consists of an OPO driven by a femtosecond pulse train with a repetition rate matching the cavity-free spectral range, is exploited and creates correlations governed by the Hamiltonian

$$
\hat {H} = i \hbar g \sum_ {m, n} L _ {m, n} \hat {a} _ {m} ^ {\dagger} \hat {a} _ {n} ^ {\dagger} + h. c. \tag {1}
$$

where  $g$  regulates the overall interaction strength and  $\hat{a}_m^\dagger$  is the photon creation operator associated with a mode of frequency  $\omega_{m}$

The coupling strength between modes at frequencies  $\omega_{m}$  and  $\omega_{n}$  is dictated by the matrix  $L_{m,n} = f_{m,n} \cdot p_{m+n}$ , where  $f_{m,n}$  is the phase-matching function[14,15] and  $p_{m+n}$  is the pump spectral amplitude at frequency  $\omega_{m} + \omega_{n}$  (ref. 16).

Frequency entanglement. A femtosecond pulse train is produced with a mode-locked titanium-sapphire oscillator delivering  $\sim 140$  fs pulses, and its second harmonic serves to pump synchronously a below-threshold OPO, as detailed in Fig. 1. Homodyne detection coupled with ultrafast pulse shaping is then employed to characterize fully the quantum properties embedded in the frequency comb.

The quantum correlations generated in the comb are conveniently understood by initially considering only two discrete frequency bands. For this purpose, the pulse shaper removes all but the low (red) and high (blue) frequencies of the local oscillator (LO) spectrum, as shown in Fig. 1. The field quadrature components  $\hat{x}$  and  $\hat{p}$  of these two bands are measured with homodyne detection and the pulse shaper constructs on-demand, variance-based entanglement witnesses $^{17}$ . When either frequency band is considered alone, a quadrature-independent excess noise is observed (Fig. 2a), as found with a thermal state. The amplitude of the spectral sum, however, is squeezed (Fig. 2b), which is indicative of a strong intra-comb non-classical frequency correlation. A  $\pi$ -phase shift is then applied to the red frequency band with the pulse shaper, which reveals that the phase of the spectral difference is also squeezed (Fig. 2c). With these two measurements, the Duan inseparability criterion $^{18}$ $\langle (\hat{x}_{\mathrm{R}} + \hat{x}_{\mathrm{B}})^{2} \rangle + \langle (\hat{p}_{\mathrm{R}} - \hat{p}_{\mathrm{B}})^{2} \rangle = 0.94 \pm 0.03 < 2$  is fulfilled and indicates that the two frequency bands are, indeed entangled. In this symmetric configuration, the spectral bandwidth of the contributing pump is considerably narrower than either of the resultant bands, which reproduces the familiar situation of two-mode entanglement. In diagnosing these correlations, the pulse shaper has assumed the role of a traditional beam splitter, but in a frequency-dependent fashion. Moreover, the  $\hat{x}$  and  $\hat{p}$  conditional variances are inferred from Figs 2b,c. The product of these conditional variances is  $\Delta^2 x_{\mathrm{R|B}} \cdot \Delta^2 p_{\mathrm{R|B}} \simeq 0.58 \pm 0.21 < 1$ , which also satisfies the more stringent condition for Einstein-Podolsky-Rosen (EPR) entanglement between the spectral wings of the SPOPO output $^{19}$ .

Covariance matrix measurement. To characterize the intra-comb entanglement across the entire spectrum, the LO is divided into ten frequency bands of equal energy, as shown in Fig. 1, and the  $\hat{x}$ - and  $\hat{p}$ -quadrature noises for each spectral region and all possible pairs of regions are determined. The full covariance matrix is assembled from 55 individual homodyne measurements. Fluctuations and correlations that depart from the vacuum level are shown in Fig. 3a for the  $\hat{x}$  quadrature. A spectrally dependent distribution of excess noise is evident (diagonal blue peaks) with the preponderance of its occurrence in the spectral wings.

![](images/239df73b54f578f75f541808b93116a855ae80fbfd6cd152dc48c190341d7880.jpg)  
Figure 1 | Experimental layout for the creation and characterization of multimode frequency combs. A titanium-sapphire oscillator produces a 76 MHz train of  $\sim 140$  fs pulses centred at  $795~\mathrm{nm}$ . Its second harmonic synchronously pumps a below-threshold OPO, which consists of a  $2\mathrm{mm}$  bismuth borate (BIBO) crystal contained within a  $\sim 4\mathrm{m}$  ring cavity. The cavity output is analysed with homodyne detection, in which the spectral composition of the LO is manipulated with a 512 element programmable two-dimensional liquid-crystal modulator capable of independent amplitude and phase modulation[28]. The spectrum of the LO is divided into ten discrete bands of equal energy (enumerated on the figure), and the amplitude and phase of each band can be addressed individually. By varying the relative phase between the shaped LO and the SPOPO output, the  $\hat{x}$  and  $\hat{p}$  quadrature noises of the quantum state projected onto the LO mode are measured. SHG, second-harmonic generation.

![](images/06d205f47e00f1f62336b5676e7920ebe70228c8d6e1bea4f259ac5d910cc224.jpg)

![](images/a3b585db762ee19d72e4610b5f1b407c4a060e1a32625cec9bfb8dea5016e81f.jpg)

![](images/fbb6572def76c36879e1b22b855e70ae8bdec97da6da6e7cc208d13e69ad25af.jpg)  
Figure 2 | Assessment of Duan inseparability criteria with ultrafast pulse shaping. a, Phase-independent excess noise of  $\sim 3.4$  dB is present in both the high (blue) and low (red) frequency bands. b, The amplitude of the frequency band sum exhibits about  $-3.2$  dB of squeezing. c, The pulse shaper writes a  $\pi$ -phase shift between the spectral wings, and the phase of the difference also shows a squeezing level of about  $-3.3$  dB. Hence the Duan entanglement criterion is verified readily.

Concomitantly, the bulk of the frequency correlation occurs between the two opposing spectral wings (off-diagonal red peaks).

The inseparability of individual frequency bands from the conglomerate structure is probed with the positive partial transpose (PPT) criterion $^{20}$ , which is applied to all 511 possible frequency

band bipartitions. Every bipartition is entangled, and the degree of its inseparability is assessed by the magnitude of the corresponding Heisenberg inequality violation<sup>7</sup>. As seen in Fig. 3b (blue circles), the absence of any separable form implies that the SPOPO output constitutes a genuine ten-partite state<sup>9</sup>. Frequency bands diametrically opposed to the central wavelength are entangled the most strongly (Fig. 3b), whereas the partition that disconnects the two spectral wings from the remaining structure is the most weakly entangled. In the case of a solitary pump frequency, all of the partitions that possess a reflection symmetry about the central wavelength would not be entangled (for example, the largest PPT value in Fig. 3b). The entanglement of such structures demands asymmetric frequency correlations afforded upon the simultaneous downconversion of multiple pump frequencies.

Similarly, it is possible to consider EPR entanglement for each of these bipartitions. Upon doing so, 115 frequency bipartitions turn out to satisfy the more stringent condition for EPR entanglement as presented in Fig. 3b (red circles). Analogous to the PPT criterion, the bipartition that displays the strongest EPR entanglement corresponds to bisecting the spectrum at the central wavelength.

Modal decomposition. Although germane for quantum-information processing, the multipartite entanglement of the comb is an extrinsic characteristic as it depends upon a user-specified allocation of frequency bands. For example, even though a single-mode squeezed beam theoretically acquires multipartite character by dividing it with a beamsplitter, the state remains intrinsically single-mode $^{21}$ . An alternative theoretical description of the state is gleaned upon diagonalizing the interaction matrix  $L_{m,n}$  to reveal a frequency-decorrelated modal representation $^{16,22,23}$ . The ensuing basis of 'supermodes'  $\hat{S}_k$ , which are the eigenvectors of the interaction matrix  $L_{m,n}$ , permits rewriting the total Hamiltonian as a sum of single-mode squeezing Hamiltonians independently acting on each supermode:

$$
\hat {H} = i \hbar g \sum_ {k} \Lambda_ {k} \hat {S} _ {k} ^ {\dagger 2} + h. c. \tag {2}
$$

where  $\varLambda_{k}$  is the eigenvalue of  $L_{m,n}$  associated with the supermode  $\hat{S}_k$  and h.c. is the Hermitian conjugate. The eigenspectrum then

![](images/b3e2b544f9d343ae7231e0107b0df2b6770bca32d62704eb7a7857119af10bcf.jpg)

![](images/70fdcd76410d5f649bcdcb90d4969669a92299c49ec521d348e390ccc44932a6.jpg)  
Figure 3 | Frequency correlations of the quantum comb. a, Noise correlation matrix, defined as  $C_{i,j}^{x} = \langle x_{i}x_{j}\rangle / \sqrt{\langle x_{i}^{2}\rangle\langle x_{j}^{2}\rangle - \delta_{i,j}\langle x_{vacuum}^{2}\rangle / \langle x_{i}^{2}\rangle}$ , for the  $x$  quadrature. b, EPR (red) and PPT (blue) inseparability criteria for all 511 bipartite combinations of the ten spectral bands, ordered according to increasing EPR values. The black dotted line is taken to be the entanglement boundary for both tests. All 511 bipartitions possess a PPT value below the boundary, which indicates complete non-separability for the state. Additionally, 115 bipartitions satisfy the more stringent criterion for EPR entanglement.

![](images/e09f1d403cd6d38c132756a2b2971adda572f43276d020f26f2f050b82dd252a.jpg)  
Wavelength (nm)  
Figure 4 | Amplitude spectra and corresponding squeezing values and quadratures for the leading six experimental supermodes retrieved from the covariance matrix. The black trace is the approximate theoretical Hermite-Gauss form for the supermodes, where the appropriate spectral width is determined from the SPOPO above-threshold spectrum.

![](images/a3ef0904baf5e147aab4c965eec5722dfd469254851d4351d55a6f22552a227d.jpg)  
Wavelength (nm)

specifies the number of non-vacuum qumodes contained in the SPOPO output and their associated degree of non-classicality.

A set of eight orthonormal, independently squeezed modes is extracted from the covariance matrix (see Supplementary Information), which approximates the above-described supermodes. The spectral composition and squeezing level for the leading six modes are shown in Fig. 4. The squeezing quadrature

$(\hat{x}$  or  $\hat{p})$  is observed to alternate between successive modes, which is in agreement with theory<sup>16</sup>. To corroborate these modes, the retrieved structures of the leading four modes are written directly onto the pulse shaper. Squeezing is observed for each of these orthogonal modes, albeit in alternating quadratures. Thus, the SPOPO functions as an in situ optical network that consists of an assembly of independent OPOs and phase shifters.

The spectral composition of each experimental mode also displays generally good agreement with Hermite-Gauss polynomial forms, which approximate the predicted supermode structure<sup>16</sup>. However, the spectral width of each supermode increases with the mode index, as  $\Delta \lambda_{k} = \sqrt{2k + 1} \cdot \Delta \lambda_{0}$ , and the inability to resolve high-order modes with the fixed bandwidth of the LO accounts for the decrease in observed squeezing levels. Thus, the present observation of eight squeezed modes does not represent an inherent upper limit to the dimensionality of comb states, and with the adoption of broader bandwidth LO pulses, comb states that possess as many as  $\sim 100$  significantly squeezed modes are expected<sup>16</sup>.

# Discussion

The coexistence of multiple modes within a single beam provides a new type of universal quantum resource that can be used for the creation of quantum networks relevant to quantum computing $^{24}$ . In particular, the introduction of spectral selectivity in the detection process, which may be accomplished with pulse shaping, or more generally any variety of spectrally resolved homodyne detection, allows the synthesis of any linear combination of the individual squeezed modes. In this manner, the detection process actualizes a basis change that emulates a linear optical network in a manner analogous to that previously implemented in the spatial domain $^{25}$ . This spectrally resolved detection of the quantum comb has been demonstrated theoretically to be capable of creating the cluster structures requisite for measurement-based quantum computing $^{24}$ . Importantly, this does not necessitate a modification of the quantum resource, but only of the manner in which it is measured.

An alternative route towards high-dimensional entangled states has also been demonstrated recently $^{26}$ , which plays upon the fact that a frequency-domain squeezing interaction simultaneously creates a multimode time beam. Utilizing this intrinsic temporal entanglement of an OPO enables the creation of a specific type of linear chain cluster.

In conclusion, we have demonstrated parametrically generated ultrafast frequency combs to be a practical, compact source of massively entangled quantum states. The ability to create top-down multipartite entanglement among thousands of frequencies with a single nonlinear interaction provides an unprecedented capability. Additional nodes may then be incorporated into the quantum network by simply increasing the number of frequencies that participate in the nonlinear interaction, which does not require an expansion of the optical set-up. The network of quantum channels present in the ultrafast comb should find numerous applications in ultraprecise temporal metrology beyond the standard quantum limit[27] and spectrally resolved measurement-based quantum computing[24,25]. We anticipate that highly multimode photonic sources will become a versatile source for realizing cluster states and facilitating fundamental studies of quantum-information processing.

Received 18 June 2013; accepted 12 November 2013; published online 15 December 2013

# References

1. Menicucci, N. C. et al. Universal quantum computation with continuous-variable cluster states. Phys. Rev. Lett. 97, 110501 (2006).  
2. Weedbrook, C. et al. Gaussian quantum information. Rev. Mod. Phys. 84, 621-669 (2012).  
3. Yukawa, M., Ukai, R., van Loock, P. & Furusawa, A. Experimental generation of four-mode continuous-variable cluster states. Phys. Rev. A 78, 012301 (2008).

4. Aoki, T. et al. Quantum error correction beyond qubits. Nature Phys. 5, 541-546 (2009).  
5. Su, X. et al. Experimental preparation of eight-partite cluster state for photonic qumodes. Opt. Lett. 37, 5178-5180 (2012).  
6. Weiner, A. M. Femtosecond pulse shaping using spatial light modulators. Rev. Sci. Instrum. 71, 1929-1960 (2000).  
7. Van Loock, P. & Furusawa, A. Detecting genuine multipartite continuous-variable entanglement. Phys. Rev. A 67, 052315 (2003).  
8. Polycarpou, C., Cassemiro, K., Venturi, G., Zavatta, A. & Bellini, M. Adaptive detection of arbitrarily shaped ultrashort quantum light states. Phys. Rev. Lett. 109, 053602 (2012).  
9. Braunstein, S. L. & van Loock, P. Quantum information with continuous variables. Rev. Mod. Phys. 77, 513-577 (2005).  
10. Menicucci, N. C., Flammia, S. T. & Pfister, O. One-way quantum computing in the optical frequency comb. Phys. Rev. Lett. 101, 130501 (2008).  
11. Ukai, R. et al. Demonstration of unconditional one-way quantum computations for continuous variables. Phys. Rev. Lett. 106, 240504 (2011).  
12. Pysher, M., Miwa, Y., Shahrokhshahi, R., Bloomer, R. & Pfister, O. Parallel generation of quadripartite cluster entanglement in the optical frequency comb. Phys. Rev. Lett. 107, 030505 (2011).  
13. Pinel, O. et al. Generation and characterization of multimode quantum frequency combs. Phys. Rev. Lett. 108, 083601 (2012).  
14. Grice, W. P., U'Ren, A. B. & Walmsley, I. A. Eliminating frequency and space-time correlations in multiphoton states. Phys. Rev. A 64, 063815 (2001).  
15. Mosley, P. J. et al. Heralded generation of ultrafast single photons in pure quantum states. Phys. Rev. Lett. 100, 133601 (2008).  
16. Patera, G., Treps, N., Fabre, C. & de Valcarcel, G. J. Quantum theory of synchronously pumped type I optical parametric oscillators: characterization of the squeezed supermodes. Eur. Phys. J. D 56, 123-140 (2010).  
17. Hyllus, P. & Eisert, J. Optimal entanglement witnesses for continuous-variable systems. New J. Phys. 8, 51 (2006).  
18. Duan, L-M., Giedke, G., Cirac, J. I. & Zoller, P. Inseparability criterion for continuous variable systems. Phys. Rev. Lett. 84, 2722-2725 (2000).  
19. Bowen, W. P., Schnabel, R., Lam, P. K. & Ralph, T. C. Experimental investigation of criteria for continuous variable entanglement. Phys. Rev. Lett. 90, 043601 (2003).  
20. Simon, R. Peres-Horodecki separability criterion for continuous variable systems. Phys. Rev. Lett. 84, 2726-2729 (2000).

21. Treps, N., Delaubert, V., Maitre, A., Courty, J. M. & Fabre, C. Quantum noise in multipixel image processing. Phys. Rev. A 71, 013820 (2005).  
22. Opatrny, T., Korolkova, N. & Leuchs, G. Mode structure and photon number correlations in squeezed quantum pulses. Phys. Rev. A 66, 053813 (2002).  
23. Braunstein, S. L. Squeezing as an irreducible resource. Phys. Rev. A 71, 055801 (2005).  
24. Ferrini, G., Gazeau, J. P., Coudreau, T., Fabre, C. & Treps, N. Compact gaussian quantum computation by multi-pixel homodyne detection. New J. Phys. 15, 093015 (2013).  
25. Armstrong, S. et al. Programmable multimode quantum networks. Nature Commun. 3, 1026 (2012).  
26. Yokoyama, S. et al. Ultra-large-scale continuous-variable cluster states multiplexed in the time domain. Nature Photon. 7, 982-986 (2013).  
27. Lamine, B., Fabre, C. & Treps, N. Quantum improvement of time transfer between remote clocks. Phys. Rev. Lett. 101, 123601 (2008).  
28. Vaughan, J., Hornung, T., Feurer, T. & Nelson, K. Diffraction-based femtosecond pulse shaping with a two-dimensional spatial light modulator. Opt. Lett. 30, 323-325 (2005).

# Acknowledgements

This work is supported by the French National Research Agency project Qualite as well as the European Research Council starting grant Frecquam. C.F. is a member of the Institut Universitaire de France. J.R. acknowledges support from the European Commission through Marie Curie Actions.

# Author contributions

C.F. and N.T. developed and supervised the project. All authors designed the experiments. S.J. designed the optical cavity. J.R. and R.M.A. constructed the apparatus and performed the experiments. All authors contributed to the authorship of the manuscript.

# Additional information

Supplementary information is available in the online version of the paper. Reprints and permissions information is available online at www.nature.com/reprints. Correspondence and requests for materials should be addressed to N.T.

# Competing financial interests

The authors declare no competing financial interests.