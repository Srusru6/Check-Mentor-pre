ARTICLE

Received 23 Jun 2011 | Accepted 26 Oct 2011 | Published 29 Nov 2011

DOI: 10.1038/ncomms1570

# Integrated photonic quantum gates for polarization qubits

Andrea Crespi $^{1,2}$ , Roberta Ramponi $^{1,2}$ , Roberto Osellame $^{1,2}$ , Linda Sansoni $^{3}$ , Irene Bongioanni $^{3}$ , Fabio Sciarrino $^{3,4}$ , Giuseppe Vallone $^{3,5}$  & Paolo Mataloni $^{3,4}$

The ability to manipulate quantum states of light by integrated devices may open new perspectives both for fundamental tests of quantum mechanics and for novel technological applications. However, the technology for handling polarization-encoded qubits, the most commonly adopted approach, is still missing in quantum optical circuits. Here we demonstrate the first integrated photonic controlled-NOT (CNOT) gate for polarization-encoded qubits. This result has been enabled by the integration, based on femtosecond laser waveguide writing, of partially polarizing beam splitters on a glass chip. We characterize the logical truth table of the quantum gate demonstrating its high fidelity to the expected one. In addition, we show the ability of this gate to transform separable states into entangled ones and vice versa. Finally, the full accessibility of our device is exploited to carry out a complete characterization of the CNOT gate through a quantum process tomography.

Incorporating the laws of quantum mechanics in data storage, processing and transmission may unleash new possibilities for information processing, ranging from quantum communication to quantum sensing, metrology, simulation and computing $^{1-4}$ . In the last few years photonic quantum technologies have been adopted as a promising experimental platform for quantum information science $^{3}$ . The realization of complex optical schemes consisting of many elements requires the introduction of waveguide technology to achieve desired scalability, stability and miniaturization of the device. Recently, silica waveguide circuits on silicon chips have been employed in quantum applications to realize stable interferometers for two-qubit entangling gates $^{5}$ . Such approach with qubits encoded into two photon optical paths, representing the logical basis  $\{|0\rangle, |1\rangle\}$ , yielded the first demonstration of an integrated linear optical controlled-NOT (CNOT) gate. In addition, quantum walk on a chip $^{6,7}$  and enhanced quantum sensitivity in phase-controlled interferometers have been demonstrated with the same technology $^{8-11}$ . However, many quantum information processes and sources of entangled photon states are based on the polarization degree of freedom $^{4,12}$ , which allows one to implement quantum operations without the need of path duplication and thus with the simplest and most compact circuit layout. Up to now, integrated devices able to efficiently guide and manipulate polarization-encoded photonic qubits are still lacking $^{13}$ .

Femtosecond laser waveguide writing has been emerging as a powerful tool in the rapidly advancing field of quantum photonics[14]. This technique, which was first introduced by Davis et al. in 1996 (ref. 15), exploits nonlinear absorption of focused femtosecond pulses to induce permanent and localized refractive index increase in transparent materials. Waveguides are directly fabricated in the bulk of the substrate by translation of the sample at constant velocity with respect to the laser beam, along the desired path. This maskless and single-step technique allows fast and cost-effective prototyping of new devices, potentially exploiting also three-dimensional geometries impossible to obtain with conventional lithography. Several devices, from simple Y-splitters[16] to increasingly complex ones[17-19], have been demonstrated with applications ranging from telecommunications to integrated biosensing[20,21]. This technique is capable of producing high-quality waveguides with low birefringence, which are indeed suited for the propagation of polarization-encoded qubits, as we recently reported in refs 22,23, where a polarization-insensitive directional coupler has been demonstrated.

Here we report on the first integrated photonic CNOT gate for polarization-encoded qubits and on the complete characterization of its quantum behaviour. The demonstration of this quantum gate has been made possible by the fabrication in a glass chip of integrated devices acting as partially polarizing beam splitters (PPBSs). Precisely, we show that femtosecond laser writing enables direct inscription of directional couplers with fine and independent control on the splitting ratio for the horizontal (H) and vertical (V) polarizations.

# Results

Directional couplers as partially polarizing beam splitters. Directional couplers are the integrated optical analogue of bulk beam splitters (BSs) and are thus fundamental building blocks of quantum optical circuits. In these devices (see the schematic representation in Fig. 1a) two distinct waveguides are brought close together for a certain propagation length, called interaction length, so that the two propagating modes become coupled through evanescent field overlap. In analogy to bulk BSs, reflectivity and transmissivity ratios of the directional coupler can be conveniently defined: when light is launched into port IN1 (Fig. 1a),  $R = P_{\mathrm{OUT1}} / (P_{\mathrm{OUT1}} + P_{\mathrm{OUT2}})$  and  $T = 1 - R = P_{\mathrm{OUT2}} / (P_{\mathrm{OUT1}} + P_{\mathrm{OUT2}})$ , respectively ( $P$  indicates the optical power); the symmetry of the device guarantees that the same relations hold when light is launched

into port IN2, by simply inverting the two indices. Optical power transfer from one waveguide to the other follows a sinusoidal law with the interaction length, whose oscillation period (beating period) depends upon the coupling coefficient of the two guided modes according to coupled mode theory[24]. If some waveguide birefringence is present, the coupling coefficient, and hence the beating period, can be different for the two polarizations (Fig. 1b). With high birefringence waveguides, this aspect has been exploited to implement polarizing beam splitters for telecom applications[25].

However, high birefringence waveguides are not suitable for the propagation of polarization-encoded qubits as they would cause decoherence between the photons typically generated by parametric down conversion, which are characterized by a large bandwidth  $\Delta \lambda > 1\mathrm{nm}$ . The optimal waveguides for a polarization-based quantum gate would therefore need to find the best compromise on the birefringence value, which should be low enough to preserve the coherence between photons, and high enough to enable polarization-dependent processing. Such compromise is found in femtosecond laser written waveguides in a borosilicate glass. In fact, thanks to their low birefringence, these waveguides allow to propagate polarization-encoded qubits without any perturbation and also to achieve practically polarization-insensitive devices, as demonstrated in refs 22,23. However, in this work we demonstrate that the same waveguides are also capable of performing polarization-based processing of the qubits. In fact, if sufficiently long interaction lengths, covering a few beating periods, are implemented in directional couplers, it is possible to strongly enhance the difference in the polarization behaviour of the device. This approach, as shown in Figure 1b, allows to finely tailor the splitting ratios for the two polarizations and enables us to realize integrated PPBSs for the first time.

Integrated quantum gates for polarization-encoded qubits. We will now demonstrate how this technology can be exploited to realize quantum optical gates. In the polarization-encoding approach, a generic qubit  $\alpha |0\rangle +\beta |1\rangle$  is implemented by a coherent superposition of H and V polarization states,  $\alpha |H\rangle +\beta |V\rangle$ , of single photons. To achieve universal quantum computation, single qubit transformations together with a two-qubit gate are sufficient[26]. One-qubit logic gates are straightforwardly implemented by using birefringent waveplates. The most commonly exploited two-qubit gate is the CNOT that flips the target qubit (T) depending on the state of the control one (C). The CNOT action is described by a unitary transformation acting on a generic superposition of two qubit quantum states. In the computational basis  $\{|00\rangle ,|01\rangle ,|10\rangle ,|11\rangle \}$  for the systems C and T, the matrix associated to the CNOT is:

$$
\mathcal {U} _ {C N O T} = \left( \begin{array}{l l l l} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{array} \right). \tag {1}
$$

A striking feature of this gate is given by the ability to entangle and disentangle qubits. Precisely, the input states  $|\pm \rangle_{\mathrm{C}}|0\rangle_{\mathrm{T}}$  and  $|\pm \rangle_{\mathrm{C}}|1\rangle_{\mathrm{P}}$  where  $|\pm \rangle = \frac{1}{\sqrt{2}}(|0\rangle \pm |1\rangle)$ , evolve into the following output states  $|\Phi^{\pm}\rangle = \frac{1}{\sqrt{2}}(|0\rangle_{\mathrm{C}}|0\rangle_{\mathrm{T}} \pm |1\rangle_{\mathrm{C}}|1\rangle_{\mathrm{T}})$  and  $|\Psi^{\pm}\rangle = \frac{1}{\sqrt{2}}(|0\rangle_{\mathrm{C}}|1\rangle_{\mathrm{T}} \pm |1\rangle_{\mathrm{C}}|0\rangle_{\mathrm{T}})$ , respectively, which are the so-called Bell states. Photonic two-qubit gates need an interaction between the two photons that carry the information, and this would suggest that a strong optical nonlinearity is required. However, it was demonstrated that scalable quantum computing is possible by using only linear optical circuits, mainly consisting of beam splitters[28]. The most simple scheme to implement the polarization CNOT exploits three PPBSs with suitable polarization-dependent transmissivities[29,30].

![](images/605e07c992a7bed8c3aae5dd1154a84cd5c6271e84e348bcd0078186b6234a48.jpg)  
Figure 1 | Partially polarizing directional couplers. (a) Schematic representation of a waveguide directional coupler; IN1 and IN2 are the input ports, whereas OUT1 and OUT2 are the output ports of the device. (b) H (squares) and V (triangles) polarization transmissions of directional couplers with different interaction lengths, based on slightly birefringent waveguides. First, the  $0 - 2\mathrm{mm}$  interaction length range was investigated to evaluate the beating length difference between the two polarizations; the interval of interest to obtain the required PPDCs was estimated to be in the  $5.6 - 8.2\mathrm{mm}$  range, which was consequently explored. Transmission for  $0\mathrm{mm}$  interaction length is non-zero, because some coupling already occurs in the curved portions of the approaching/departing waveguides. Error bars indicate fabrication reproducibility.

![](images/52fabf3a3a3049e3125165ea1897047461d91eced59ec4eb87d40b3a50fd03a1.jpg)

The two-photon interaction occurs by a Hong-Ou-Mandel effect $^{31}$  in a single PPBS, whereas the other two PPBSs operate as compensators. Up to now such a scheme has been experimentally implemented only using bulk optics $^{32-35}$  or fibre couplers $^{36}$ . The integrated CNOT gate is achieved by the optical scheme given in the inset of Figure 2: it consists of a first partially polarizing directional coupler (PPDC1), with transmissivities  $T_{H}^{(1)} = 0$  and  $T_{V}^{(1)} = \frac{2}{3}$  for horizontal and vertical polarization, respectively, where target and control qubits interfere, followed by two other directional couplers (PPDC2 and PPDC3), with  $T_{H}^{(2,3)} = \frac{1}{3}$  and  $T_{V}^{(2,3)} = 1$ , where the horizontal and vertical polarization contributions are balanced. In this scheme, the following correspondence between logical qubits and physical states holds:  $|0\rangle_{\mathrm{C}} \equiv |V\rangle_{\mathrm{C}}$ ,  $|1\rangle_{\mathrm{C}} \equiv |H\rangle_{\mathrm{C}}$ ,  $|0\rangle_{\mathrm{I}} \equiv |A\rangle_{\mathrm{T}}$ ,  $|1\rangle_{\mathrm{T}} \equiv |D\rangle_{\mathrm{T}}$  where  $|A\rangle = \frac{1}{\sqrt{2}}(|H\rangle + |V\rangle)$  and  $|D\rangle = \frac{1}{\sqrt{2}}(|H\rangle - |V\rangle)$ . The CNOT operation succeeds with probability  $P = \frac{1}{9}$ .

The PPDCs have been fabricated by the femtosecond laser waveguide writing technique above described. To calibrate the fabrication parameters, several directional couplers have been produced with different interaction lengths ranging from  $0\mathrm{mm}$  to  $2\mathrm{mm}$  and from  $5.6\mathrm{mm}$  to  $8.2\mathrm{mm}$  (see Fig. 1). The distance between the two waveguides in the interaction region was kept constant at  $7\mu \mathrm{m}$ . It can be observed that for an interaction length  $L_{1} \simeq 7.4\mathrm{mm}$  a device with  $T_{H} = 0$  and  $T_{V} = \frac{2}{3}$  is obtained, fulfilling the requirements for PPDC1, whereas a length  $L_{2} \simeq 7\mathrm{mm}$  provides  $T_{H} = \frac{1}{3}$  and  $T_{V} = 1$  and can be adopted for PPDC2 and PPDC3. Several CNOTs have been fabricated according to the schematic of Figure 2 (inset) with slightly different interaction lengths around the values of  $L_{1}$  and  $L_{2}$  to take into account possible fabrication imperfections. The footprint of each integrated CNOT is  $500\mu \mathrm{m} \times 3\mathrm{cm}$ . After characterization with a classical laser source, the devices providing the best estimated performance have been selected. The device used in the experiments has the following parameters:  $\overline{T}_{H}^{(1)} < 1\%$ ,  $\overline{T}_{V}^{(1)} = (64 \pm 1)\%$ ,  $\overline{T}_{H}^{(2)} = (43 \pm 1)\%$ ,  $\overline{T}_{V}^{(2)} = (98 \pm 1)\%$ ,  $\overline{T}_{H}^{(3)} = (27 \pm 1)\%$ , and  $\overline{T}_{V}^{(3)} = (93 \pm 1)\%$ . To improve the robustness and stability of the device, single-mode fibre arrays have been permanently bonded to the input and output ports.

Quantum measurements. As a first quantum experiment we determined the truth table of the device operated as a CNOT gate. On this purpose we used the experimental setup represented in Figure 2. Temporal superposition of photon wavepackets in PPDC1 was

obtained by acting on the delay line. Then we injected into the chip the four computational basis states  $|0\rangle_{\mathrm{C}}|0\rangle_{\mathrm{T}}$ ,  $|0\rangle_{\mathrm{C}}|1\rangle_{\mathrm{T}}$ ,  $|1\rangle_{\mathrm{C}}|0\rangle_{\mathrm{T}}$  and  $|1\rangle_{\mathrm{C}}|1\rangle_{\mathrm{T}}$  and measured the probability of detecting each of them at the output. The obtained truth table is reported in Figure 3a. The average measured fidelity of the logical basis has been calculated as  $\mathrm{F} = 0.940 \pm 0.004$ . We can compare this value with the expected fidelity of the device  $\overline{\mathcal{F}} = 0.975 \pm 0.007$ , estimated by taking into account the measured transmissivities of the PPDCs. We attribute the discrepancy between the experimental and expected fidelities mainly to a partial distinguishability of photon wavepackets and non-perfect compensation of the rotation of the polarization in the single-mode optical fibres.

As already mentioned, the CNOT can also be exploited as an entangling gate. We experimentally verified this behaviour by injecting into the device the states  $\{\left|\pm \rangle_{\mathrm{C}}|0\rangle_{\mathrm{T}},\left|\pm \rangle_{\mathrm{C}}|1\rangle_{\mathrm{T}}\}$  and measuring a set of observables to obtain a tomographic reconstruction of the density matrices of the output states. As expected the action of the CNOT converts the separable states into the maximally entangled Bell states. We report in Figure 3b one of the reconstructed density matrices and in Figure 3c the probabilities to generate the different Bell states. The fidelities of the output density matrices compared with those of the corresponding Bell states are  $\mathcal{F}_{|\Phi^{+}\rangle} = 0.930\pm 0.014$ $\mathcal{F}_{|\Psi^{+}\rangle} = 0.939\pm 0.008$ $\mathcal{F}_{|\Phi^{-}\rangle} = 0.900\pm 0.006$ $\mathcal{F}_{|\Psi^{-}\rangle} = 0.877\pm 0.011$  with average value  $\mathcal{F}_{\mathrm{Bell}} = 0.912\pm 0.005$  .We also checked that the CNOT gate can be adopted to discriminate the four Bell states. Indeed, the four entangled states  $|\Psi^{\pm}\rangle ,|\Phi^{\pm}\rangle$  are transformed into four orthogonal separable states, which can be easily discriminated, as shown in Figure 3d. The discrimination probability is  $0.877\pm 0.007$  slightly lower than the previous fidelities due to imperfections in the entanglement source.

To provide a full characterization of the quantum device we carried out a quantum process tomography $^{37}$ , first experimentally demonstrated for a CNOT gate in ref. 38. This requires preparing the photons in a complete set of input basis states, and characterizing the output. A generic quantum process  $\mathcal{E}$  acting on a two-qubit density matrix  $\rho$ , can be expressed as  $\mathcal{E}(\rho) = \sum_{m,n=0}^{15} \chi_{mn} \Gamma_m \rho \Gamma_n^\dagger$  where the operators  $\Gamma_m$  are defined as tensor products of Pauli matrices  $\{\Gamma_m \equiv \sigma_i \otimes \sigma_j\}$ ,  $i,j = 0,\dots,3$ ,  $m = 0,\dots,15$ . The matrix  $\chi_{mn}$  contains all the information of the process. We reconstructed the  $16 \times 16$  matrix  $\chi_{\mathrm{exp}}$  shown in Figure 4. The process fidelity $^{39}$  (see Methods) with the ideal CNOT gate was measured as  $\mathcal{F}_{\mathrm{exp}} = 0.906 \pm 0.003$ .

![](images/ee353ce4680fe133ddde9bb19cbd4c383bddc569abd96e06cb3fb4178f5d0661.jpg)  
Figure 2 | Experimental setup. Sketch of the experimental setup that can be conceptually divided into three parts. The first part is the source: photon pairs at wavelength  $\lambda = 806\mathrm{nm}$  are generated via spontaneous parametric down conversion in a  $1.5\mathrm{mm}\beta$  -barium borate crystal (C) cut for type-II non-collinear phase matching, pumped by a CW diode laser with power  $P = 50\mathrm{mW}$  (ref. 27). Photon polarization states are prepared by using polarizing beam splitters (PBSs) and waveplates (WPs). A delay line (DL) is inserted to control the temporal superposition of the photons, which are then coupled to single mode fibres (SMFs) and injected into the integrated CNOT gate. Interference filters (IFs) determine the photon bandwidth  $\Delta \lambda = 6\mathrm{nm}$ . The second part shows the integrated CNOT for polarization-encoded qubits (see inset) realized by ultrafast laser writing technique. The final part represents the analysis apparatus: the polarization state of qubits emerging from the chip is analyzed by standard analysis setups (WP + PBS). Photons are then delivered to single photon counting modules (SPCM) through multimode fibres (MMFs) and coincidences between the two channels are measured. Polarization controllers (PCs) are used before and after the CNOT device to compensate polarization rotations induced by the fibres. A waveplate controller (WPC) drives the motorized waveplates to automatize the measurements.

# Discussion

We reported on the integration of partially polarizing beam splitters on a glass chip, enabling the demonstration of the first integrated photonic CNOT gate based on polarization encoding. From the fabrication point of view this work shows the capability of femtosecond laser microfabrication to produce also polarization-sensitive waveguide devices, thus further enriching the portfolio of applications that can be addressed by this simple and flexible fabrication technique. It is important to note that the polarization sensitivity/insensitivity of the directional coupler can be selected by acting on geometrical parameters and not on physical properties of the waveguides[22,23]. This enables simple and flexible designs of complex integrated quantum devices, where polarization-sensitive and polarization-insensitive processing can be easily cascaded. This work represents a major step towards the development of integrated photonic technology, which could provide a viable solution for quantum information processing and paves the way to the integration of a wealth of polarization-based quantum algorithms. Future research will be devoted to the on-chip implementation of both preoriented and tunable waveplates to integrate also one-qubit gates. The present results open new perspectives towards joint integrated handling of hybrid quantum states based on different degrees of freedom of light[40-45], such as polarization, path and orbital angular momentum. This would significantly improve the computational power of a quantum device.

The capability to process polarization-entangled photons could also benefit the quantum simulation field. As an example, exploiting the different statistics of singlet and triplet polarization-entangled states, it is possible to simulate how symmetric and antisymmetric particles travel through a quantum walk $^{7,23}$ , paving the way to advanced investigations on complexity physics phenomena.

# Methods

Chip fabrication and characterization. Waveguides were micromachined in borosilicate glass substrate (Corning EAGLE2000, Corning Inc) using a commercial HighQLaser FemtoREGEN femtosecond laser, which provides 400 fs pulses at  $960\mathrm{kHz}$  repetition rate. For the waveguide fabrication pulses with  $240\mathrm{nJ}$  energy were focused  $170\mu \mathrm{m}$  under the glass surface, using a 0.6 numerical aperture microscope objective whereas the sample was translated at a constant speed of  $20\mathrm{mm~s^{-1}}$  by high precision, three-axis air-bearing stages (Aerotech FiberGlide 3D, Aerotech Inc). The guided mode at  $806\mathrm{nm}$  is slightly elliptical, measuring

![](images/5055a818a3d67f7cacf7fe65d801dcf81854a3b0c544cdaba6f6a45189075a8e.jpg)  
a

![](images/6584d221dc6b48267564554919a3b4f051f4462484cfd66b66dedaba2df5fb10.jpg)  
b

![](images/49952be62d8d1e922db87c73a8b17fd681696f1631951f7f333449cda40b621a.jpg)  
C

![](images/0ec2e8af26243d17b837e5bb107f53c68bba0ce3afe212d9c28ca7c8f3e7d317.jpg)  
d  
Figure 3 | Truth table and entanglement generation. (a) Measured truth table. (b) Experimental tomographic reconstruction of the Bell state  $|\Phi^{+}\rangle$  obtained by injecting the separable state  $| + 0\rangle$  in the CNOT. (c) Measured probabilities of the output Bell states corresponding to the different input separable states. (d) Measured probabilities of the output separable states corresponding to the different input Bell states.

$8\mu \mathrm{m}\times 9\mu \mathrm{m}$ . Measured propagation losses are  $0.8\mathrm{dBcm}^{-1}$  and coupling losses to single mode fibres about  $1.3\mathrm{dB}$  per facet. Birefringence of these waveguides is on the order of  $\mathrm{B} = 7\times 10^{-5}$ , as characterized in ref. 22. For the curved segments in the directional couplers composing the integrated CNOT a  $30\mathrm{mm}$  bending radius was adopted, which gives  $< 1$  dB of additional bending losses on the whole device.

Quantum process tomography. The full characterization of a quantum device is provided by quantum process tomography $^{37}$ . Following the procedure adopted in ref. 39, we performed the quantum process tomography of our device and reconstructed the associated  $\chi$  matrix. The experimental setup is the same one

![](images/2a5a6ae08b6f006c25a41e6237c6ef935d08b8eff129029fbf54fac2cca8d0ed.jpg)  
a  
b

![](images/a91f4bd9c72696d8d298c49c868fc568c96114e84772b8c986d22b75c70bdf45.jpg)  
Figure 4 | Process matrix measurement. (a) Ideal  $\chi_{CNOT}$  and (b) experimental  $\chi_{\mathrm{exp}}$  matrices (real part) obtained from the quantum process tomography of the CNOT gate. Imaginary part of  $\chi_{\mathrm{exp}}$  is negligible.  $X, Y$  and  $Z$  correspond to Pauli matrices  $\sigma_1, \sigma_2$  and  $\sigma_3$ , respectively.

adopted in the previous measurements (see Fig. 2): we prepared 16 different input states and measured the projections of the output states on the set  $\{|ij\rangle\}$ , where  $i,j = H,V,D,A,R,L$ , that is, horizontal, vertical, diagonal, antidiagonal, righthanded and lefthanded polarization, using standard polarization analysis setups. The obtained  $\chi$  matrix is reported in Figure 4. To evaluate the quality of the acquired data we calculated the process fidelity<sup>39</sup> as

$$
\mathcal {F} _ {\exp} = \frac {\operatorname {T r} \left[ \sqrt {\sqrt {\chi_ {\exp}} \chi_ {C N O T} \sqrt {\chi_ {\exp}}} \right] ^ {2}}{\operatorname {T r} \left[ \chi_ {\exp} \right] \operatorname {T r} \left[ \chi_ {C N O T} \right]}, \tag {2}
$$

where  $\chi_{CNOT}$  is the process matrix of the ideal CNOT gate.

# References

1. Ladd, T. D. et al. Quantum computers. Nature 464, 45-53 (2010).  
2. O'Brien, J. L., Furusawa, A. & Vuckovic, J. Photonic quantum technologies. Nat. Photon. 3, 687-695 (2009).  
3. Kok, P. et al. Linear optical quantum computing with photonic qubits. Rev. Mod. Phys. 79, 135-174 (2007).  
4. Ursin, R. et al. Entanglement-based quantum communication over  $144\mathrm{km}$ . Nat. Phys. 3, 481-486 (2007).  
5. Politi, A., Cryan, M. J., rarity, J. G., Yu, S. & O'Brien, J. L. Silica-on-silicon waveguide quantum circuits. Science 320, 646-649 (2008).  
6. Peruzzo, A. et al. Quantum walks of correlated photons. Science 17, 1500-1503 (2010).  
7. Matthews, J. C. F. et al. Simulating quantum statistics with entangled photons: a continuous transition from bosons to fermions. Preprint at <http://arXiv.org/abs/1106.1166> (2011).  
8. Politi, A., Matthews, J. C. F. & O'Brien, J. L. Shor's quantum factoring algorithm on a photonic chip. Science 325, 1221 (2009).  
9. Smith, B. J., Kundys, D., Thomas-Peter, N., Smith, P. G. R. & Walmsley, I. A. Phase-controlled integrated photonic quantum circuits. Opt. Express 17, 13516-13525 (2009).  
10. Laing, A. et al. High-fidelity operation of quantum photonic circuits. Appl. Phys. Lett. 97, 211109 (2010).  
11. Matthews, J. C. F. et al. Manipulation of multiphoton entanglement in waveguide quantum circuits. Nat. Photon. 3, 346-350 (2009).  
12. Walther, P. et al. Experimental one-way quantum computing. Nature 434, 169-176 (2005).  
13. Politi, A., Matthews, J., Thompson, M. & O'Brien, J. Integrated quantum photonics. IEEE J. Sel. Top. Quant. Electron. 15, 1673-1684 (2009).  
14. Marshall, G. D. et al. Laser written waveguide photonic quantum circuits. Opt. Express 17, 12546-12554 (2009).  
15. Davis, K. M. et al. Writing waveguides in glass with a femtosecond laser. Opt. Lett. 21, 1729-1731 (1996).  
16. Homoelle, D. et al. Infrared photosensitivity in silica glasses exposed to femtosecond laser pulses. Opt. Lett. 24, 1311-1313 (1999).  
17. Gattass, R. R. & Mazur, E. Femtosecond laser micromachining in transparent materials. Nat. Photon. 2, 219-225 (2008).  
18. Della Valle, G., Osellame, R. & Laporta, P. Micromachining of photonic devices by femtosecond laser pulses. J. Opt. A 11, 013001-013018 (2009).  
19. Osellame, R. et al. Femtosecond writing of active optical waveguides with astigmatically shaped beams. J. Opt. Soc. Am. B 20, 1559-1567 (2003).  
20. Eaton, S. M. et al. Telecom-band directional coupler written with femtosecond fiber laser. IEEE Phot. Technol. Lett. 18, 2174-2176 (2006).  
21. Osellame, R. et al. Femtosecond laser microstructuring: an enabling tool for optofluidic lab-on-chips. Laser Phot. Rev. 5, 442-463 (2011).  
22. Sansoni, L. et al. Polarization entangled state measurement on a chip. Phys. Rev. Lett. 105, 200503 (2010).  
23. Sansoni, L. et al. Two-particle bosonic-fermionic quantum walk via 3D integrated photonics. Preprint at <http://arXiv.org/abs/1106.5713> (2011).  
24. Yariv, A. Coupled-mode theory for guided-wave optics. IEEE J. Quantum Electron. 9, 919-933 (1973).  
25. Kiyat, I., Aydinli, A. & Dagli, N. A compact silicon-on-insulator polarization splitter. IEEE Phot. Technol. Lett. 17, 100-102 (2005).  
26. Nielsen, M. & Chuang, I. Quantum Computation and Quantum Information, Cambridge University Press, 2000.  
27. Kwiat, P. G. et al. New high-intensity source of polarization-entangled photon pairs. Phys. Rev. Lett. 75, 4337-4341 (1995).  
28. Knill, E., Laflamme, R. & Milburn, G. J. A scheme for efficient quantum computation with linear optics. Nature 409, 46-52 (2001).  
29. Ralph, T. C., Langford, N. K., Bell, T. B. & White, A. G. Linear optical controlled-NOT gate in the coincidence basis. Phys. Rev. A 65, 062324 (2002).  
30. Hofmann, H. F. & Takeuchi, S. Quantum phase gate for photonic qubits using only beam splitters and postselection. Phys. Rev. A 66, 024308 (2002).  
31. Hong, C. K., Ou, Z. Y. & Mandel, L. Measurement of subpicosecond time intervals between two photons by interference. Phys. Rev. Lett. 59, 2044 (1987).  
32. Kiesel, N., Schmid, C., Weber, U., Ursin, R. & Weinfurter, H. Linear optics controlled-phase gate made simple. Phys. Rev. Lett. 95, 210505 (2005).  
33. Okamoto, R., Hofmann, H. F., Takeuchi, S. & Sasaki, K. Demonstration of an optical quantum controlled-NOT gate without path interference. Phys. Rev. Lett. 95, 210506 (2005).  
34. Langford, N. K. et al. Demonstration of a simple entangling optical gate and its use in bell-state analysis. Phys. Rev. Lett. 95, 210504 (2005).  
35. O'Brien, J. L. et al. Demonstration of an all-optical quantum controlled-NOT gate. Nature 426, 264-267 (2003).  
36. Clark, A. S. et al. All-optical-fiber polarization-based quantum logic gate. Phys. Rev. A 79, 030303(R) (2009).  
37. Chuang, I. L. & Nielsen, M. A. Prescription for experimental determination of the dynamics of a quantum black box. J. Mod. Opt. 44, 2455-2467 (1997).  
38. O'Brien, J. L. et al. Quantum process tomography of a controlled- NOT gate. Phys. Rev. Lett. 93, 080502 (2004).

39. Bongioanni, I., Sansoni, L., Sciarrino, F., Vallone, G. & Mataloni, P. Experimental quantum process tomography of non trace-preserving maps. Phys. Rev. A 82, 042307 (2010).  
40. Rossi, A., Vallone, G., Chiuri, A., De Martini, F. & Mataloni, P. Multipath entanglement of two photons. Phys. Rev. Lett. 102, 153902 (2009).  
41. Chiuri, A. et al. Hyperentangled mixed phased Dicke states: optical design and detection. Phys. Rev. Lett. 105, 250501 (2010).  
42. Gao, W.- B. et al. Experimental realization of a controlled-NOT gate with four-photon six-qubit cluster states. Phys. Rev. Lett. 104, 020501 (2010).  
43. Nagali, E. et al. Optimal quantum cloning of orbital angular momentum photon qubits through Hong-Ou-Mandel coalescence. Nat. Photon. 3, 720-723 (2009).  
44. Nagali, E. et al. Experimental optimal cloning of four-dimensional quantum states of photons. Phys. Rev. Lett. 105, 073602 (2010).  
45. Barreiro, J. T., Wei, T.-C. & Kwiat, P. G. Beating the channel capacity limit for linear photonic superdense coding. Nat. Phys. 4, 282-286 (2008).

# Acknowledgements

This work was supported by PRIN 2009: Circuiti Integrati per l'Informazione Quantistica, FIRB-Furto in Ricerca HYTEQ, ERA-Net CHISTERA-QUASAR.

# Author contributions

A.C., R.R., R.O., L.S., F.S., G.V., and P.M. conceived and designed the integrated CNOT gate for polarization qubits. A.C., R.R., R.O. fabricated the integrated CNOT chip and

performed the characterization measurements in the classical regime. L.S., I.B., F.S., G.V., PM carried out the characterization measurements in the quantum regime. All authors discussed the results and participated in the manuscript preparation.

# Additional information

Supplementary Information accompanies this paper at http://www.nature.com/naturecommunications

Competing financial interests: A.C., R.R., R.O., L.S., F.S., G.V. and P.M. are listed as inventors on an Italian patent pending application (PD2011A000140) entitled 'Porta logica in ottica integrata per qubit quantistici codificati in polarizzazione e relativo metodo di realizzazione ed utilizzo' dealing with the implementation of an integrated optics quantum logic gate according to the results presented in this paper.

Reprints and permission information is available online at http://npg.nature.com/reprintsandpermissions/

How to cite this article: Crespi, A. et al. Integrated photonic quantum gates for polarization qubits. Nat. Commun. 2:566 doi: 10.1038/ncomms1570 (2011).

License: This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivative Works 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-nd/3.0/