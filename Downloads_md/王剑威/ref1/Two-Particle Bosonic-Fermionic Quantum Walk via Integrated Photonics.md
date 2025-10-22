# Two-Particle Bosonic-Fermionic Quantum Walk via Integrated Photonics

Linda Sansoni, $^{1}$  Fabio Sciarrino, $^{1,2,*}$  Giuseppe Vallone, $^{1,3}$  Paolo Mataloni, $^{1,2}$  Andrea Crespi, $^{4,5}$  Roberta Ramponi, $^{4,5}$  and Roberto Osellame $^{4,5}$

$^{1}$ Dipartimento di Fisica, Sapienza Università di Roma, Piazzale Aldo Moro, 5, I-00185 Roma, Italy  
 $^{2}$ Istituto Nazionale di Ottica, Consiglio Nazionale delle Ricerche (INO-CNR), Largo Enrico Fermi, 6, I-50125 Firenze, Italy  
 $^{3}$ Department of Information Engineering, University of Padova, I-35131 Padova, Italy  
 $^{4}$ Istituto di Fotonica e Nanotechnologie, Consiglio Nazionale delle Ricerche (IFN-CNR), Piazza Leonardo da Vinci, 32, I-20133 Milano, Italy  
 $^{5}$ Dipartimento di Fisica, Politecnico di Milano, Piazza Leonardo da Vinci, 32, I-20133 Milano, Italy (Received 26 October 2011; published 5 January 2012)

Quantum walk represents one of the most promising resources for the simulation of physical quantum systems, and has also emerged as an alternative to the standard circuit model for quantum computing. Here we investigate how the particle statistics, either bosonic or fermionic, influences a two-particle discrete quantum walk. Such an experiment has been realized by exploiting polarization entanglement to simulate the bunching-antibunching feature of noninteracting bosons and fermions. To this scope a novel three-dimensional geometry for the waveguide circuit is introduced, which allows accurate polarization independent behavior, maintaining remarkable control on both phase and balancement.

DOI: 10.1103/PhysRevLett.108.010502

PACS numbers: 03.67.Ac, 42.50.-p, 42.79.Gn

In the framework of quantum information processing, quantum walk has attracted much attention in the last few years [1]. Quantum walk is an extension of the classical random walk: a walker on a lattice "jumping" between different sites with a given probability. The features of the quantum walker are interference and superposition which lead to a nonclassical dynamic evolution. Two different cases may be considered: discrete- and continuous-time quantum walks [2]. The properties of these two walks have shown several similarities [3]; however, the discrete quantum walk exhibits a higher flexibility due to the possibility of tailoring the quantum coin properties to investigate different dynamic scenarios [4,5]. By endowing the walker with quantum properties, many new interesting effects appear: quantum walks allow the speed-up of search algorithms [6] and the realization of universal quantum computation [1]. Moreover it has been recently shown that quantum walks with a large number of sites exhibit a highly nontrivial dynamics, including localization and recurrence [7,8]. Within this scenario, a possible application is in the investigation on biophysical systems, like the energy transfer process within photosynthesis [9].

Single-particle quantum walks yield an exponential computational gain with respect to classical random walks; it can be noted that they have an exact mapping to classical wave phenomena and therefore they can be implemented using purely classical resources. On the other hand, quantum walks of more than one indistinguishable particle can provide an additional computational power that scales exponentially with the resources employed. This could be used to improve simulation performances in complex tasks, e.g., the graph isomorphism problem [10]. However, they need quantum resources to be

implemented, since classical theory no longer provides a sufficient description.

Different experimental implementations of single-particle quantum walks were performed with trapped atoms [11], ions [12,13], energy levels in NMR schemes [14], photons in waveguide structures [15], and in a fiber loop configuration [4,5]. Very recently quantum walks of two identical photons have been performed [16,17]. However, up to now no experimental demonstration on how the particle statistics, either bosonic or fermionic, influences a two-particle quantum walk has been reported.

In this work, we report on the implementation of a discrete quantum walk for entangled particles. By changing the symmetry of entanglement we can simulate the quantum dynamics of the walks of two particles with bosonic or fermionic statistics. These results are made possible by the adoption of novel geometries in integrated optical circuits fabricated by femtosecond laser pulses, which preserve the indistinguishability of the two polarizations as well as provide high phase accuracy and stability. In the discrete quantum walk the walker is represented by a quantum particle—such as an electron, atom or photon—with an additional degree of freedom spanning a two-dimensional space and named the “quantum coin.” At any given time the particle may be in a superposition of the two basis states, up  $(|U\rangle)$  or down  $(|D\rangle)$ , representing the two “coin faces” [Fig. 1(a)]. The quantum coin state directs the motion of the particle and the stochastic evolution by a unitary process. A key difference with the classical case is that the many possible paths of the quantum walker may exhibit interference, leading to a very different probability distribution of finding the walker at a given location.

![](images/a17d87fc40bb7ba388d9d530deb455ac2f9b0db9586a8cbff6074493a96e468b.jpg)  
FIG. 1 (color online). (a) Unidimensional quantum walk: depending on the result of the coin toss the walker moves upward  $(U)$  or downward  $(D)$ . (b) Scheme of an array of beam splitters (BSs) for a four-step quantum walk. Vertical dashed lines indicate the steps  $T$  of the quantum walk and the horizontal stripes represent the position  $|j\rangle$  of the walker. In an array with an even (odd) number of steps the output ports  $J$  are grouped into the even (odd) final positions  $|j\rangle$  of the walker. (c) Different behaviors of bosons and fermions on a BS.

Indeed, the evolution of the walk can be described with the step operator  $E = \sum_{j}|j - 1\rangle \langle j|\otimes |U\rangle \langle U| + |j + 1\rangle \times \langle j|\otimes |D\rangle \langle D|$ , where  $|j - 1\rangle \langle j|$  and  $|j + 1\rangle \langle j|$  stand for the operators which move the particle in the lower and higher position of the lattice, respectively. The coherent action of the step operator  $E$  and coin tossing leads to entanglement between the position and the internal degree of freedom. After several steps, the counterintuitive profile of the quantum walk probability distribution emerges as a result of quantum interference among multiple paths.

More complex distributions arise when two particles are injected into the same quantum walk. An important development is the combination in the same platform of quantum walk and entangled states [18,19]. In this case both the initial and final state of the walkers are entangled states and, depending on the entanglement symmetry, different final distributions may be observed. As previously proposed in Ref. [18], entangled states of two particles can be exploited to carry out bosonic-fermionic quantum walks: by changing the symmetry of the entangled state we can simulate the quantum walk of two particles with integer or semi-integer spin [20]. The fermionic and bosonic behaviors drastically influence the dynamics of their quantum walk on the line.

The simulation of single-particle quantum walks on a line can be implemented using single photon states, beam splitters, phase shifters, and photodetectors [21,22]. The quantum dynamics is achieved by an array of balanced beam splitters (BSs) as shown in Fig. 1(b), each vertical line of beam splitters representing a step of the quantum walk. Horizontal stripes represent the position  $|j\rangle$  of the walker. If a photon, at time  $T$  and in the stripe  $j$ , is incident downward  $|D\rangle$  (upward  $|U\rangle$ ) on the BS we can represent its state as  $|j,D\rangle_T$  ( $|j,U\rangle_T$ ). The transition from time  $T$  to time  $T + 1$  is given by the BS

operator  $|j, D\rangle_T \rightarrow \frac{1}{\sqrt{2}}(|j - 1, D\rangle_{T + 1} - |j + 1, U\rangle_{T + 1}),$ $|j, U\rangle_T \rightarrow \frac{1}{\sqrt{2}}(|j + 1, U\rangle_{T + 1} + |j - 1, D\rangle_{T + 1})$ . This operation simultaneously implements the coin (precisely the Hadamard coin)

$$
C = \frac {1}{\sqrt {2}} \left( \begin{array}{c c} 1 & 1 \\ 1 & - 1 \end{array} \right)
$$

and the step operator  $E$ . Note that, if the particle starts at position  $|j = 0\rangle$ , at even (odd) times it will occupy only even (odd) positions. Referring to Fig. 1(b), for a walk with  $T^{*}$  steps, the relation between the probabilities of photons emerging from one of the  $N = 2T^{*}$  outputs of the BS array  $(P_{J}^{\mathrm{BS}})$  and the final position of the walker  $(p_j^{\mathrm{walk}})$  is:

$$
p _ {- T ^ {*}} ^ {\text {w a l k}} = P _ {1} ^ {\text {B S}},
$$

$$
p _ {- T ^ {*} + 2 k} ^ {\text {w a l k}} = P _ {2 k} ^ {\mathrm {B S}} + P _ {2 k + 1} ^ {\mathrm {B S}}, \quad k = 1, \dots , T ^ {*} - 1 \tag {1}
$$

$$
p _ {T ^ {*}} ^ {\text {w a l k}} = P _ {2 T ^ {*}} ^ {\text {B S}}.
$$

Provided that all the optical devices used in the walk are polarization insensitive, the polarization degree of freedom may be exploited to entangle the photons injected into the BS arrays. Moreover by changing the entangled state from a symmetric one, such as the triplet, into an antisymmetric one, the singlet, it is possible to mimic the quantum dynamics of two noninteracting bosonic and fermionic particles [see Fig. 1(c)]. It must be noted that the experimental realization of such a network of BSs is exceedingly difficult with bulk optics, even for a small number of steps, since it requires a quadratically growing number of elements. Furthermore, for correct operation of the quantum walk, the phase introduced by the optical paths, passing from each beam splitter to the following, must be controlled and stable.

Our approach exploits an integrated waveguide architecture, which allows us to concentrate a large number of optical elements on a small chip and to achieve intrinsic phase stability due to the monolithic structure. In a waveguide implementation BSs are replaced by directional couplers (DCs), i.e., structures in which two waveguides, brought close together for a certain interaction length, couple by evanescent field.

To realize the integrated optical circuits we adopted the femtosecond laser writing technology [23,24]. Briefly, nonlinear absorption of focused femtosecond pulses is exploited to induce permanent and localized refractive index increase in transparent materials. Waveguides are directly fabricated in the bulk of the substrate by translation of the sample at constant velocity with respect to the laser beam, along the desired path. Since it is a single-step and maskless process, this technique allows rapid and cost-effective prototyping of new devices. Furthermore, it has intrinsic three-dimensional possibilities which have indeed been exploited in this work.

In previous work we have demonstrated that femtosecond laser technology can produce high-quality waveguides

able to support polarization entangled photon states [25,26]. In these femtosecond laser written waveguides, birefringence is low and does not significantly affect the coherence of the photons. Anyway, the guided modes for the two polarizations are still slightly different [as shown in Fig. 2(a)] and this results in a residual polarization dependence in the properties of the fabricated DCs. In fact, the coupling coefficient depends on the overlap integral between the two guided mode profiles and is indeed quite sensitive to even small differences in the mode dimensions [27]. When several devices are cascaded, as in the case of a DC array for implementing a quantum walk, small differences in the splitting ratios accumulate and in the end affect the indistinguishability of the two polarizations.

The three-dimensional capabilities of the present technology can be exploited to tailor the polarization behavior of the DCs. We have fabricated several DCs with the waveguides lying on planes at different angles  $\theta$  with

![](images/33106ea71c3ae0c694392bbac67a9dfb88d44f395058753a3363d884269dc836.jpg)  
a)

![](images/39f54ff1b2a6e70eacd9cb90adf8846580672b2b8c71b876ef5dad4f390c04af.jpg)

![](images/2503b106949f7131d6dd6b41a131a046e6600b7c37c8af19f55d454daa24ae4c.jpg)

![](images/dab6e607053ee7c231c8b7ea3357cf8e1c98a453e3703aa0b7fe2764e3d8e875.jpg)  
c)

![](images/a0d2b6ffb7e485a2eb254ff17d0259b65390c81b5dcb90dcab2dc7c231d19266.jpg)  
FIG. 2 (color online). Integrated optical circuits. (a) Measured intensity profile for the guided modes with polarization  $V$  and  $H$ , at  $806~\mathrm{nm}$  wavelength. The  $1 / e^2$  dimensions are reported. (b) Ratio of the estimated coupling coefficient for polarization  $V(C_V)$  and polarization  $H(C_H)$  in directional couplers fabricated with different angles  $\theta$  between the waveguides (see inset), but fixed interaction length  $3\mathrm{mm}$  and distance  $(11\mu \mathrm{m})$ . The fitting line is a guide to the eye. (c) Schematic of the network of directional couplers fabricated for implementing a four-step quantum walk. The color coding indicates the writing depth of the waveguides, which is varying from point to point. (d) 3D representation of the basic cell of the network, which acts as a Mach-Zehnder interferometer.

![](images/5931554407e0b9533cb4b12bd671f436195f852c05c5f4e13391cbe207e7b248.jpg)

respect to the horizontal [see inset of Fig. 2(b)], but fixed interaction length and spacing between the waveguides. It can be observed that the ratio between the measured coupling coefficients for the two polarizations  $(C_V$  and  $C_H)$  depends on  $\theta$ , as shown in Fig. 2(b). In particular there exists an angle for which the ratio between the two coefficients is unitary; i.e., the coupler becomes polarization insensitive. In order to realize an experimental implementation of a discrete quantum walk with photons, we fabricated a network of DCs, all realized with the tilted geometry described above, where the two waveguides are brought at  $11\mu \mathrm{m}$  distance, at an angle of  $62^{\circ}$ , in the interaction region, thus guaranteeing the polarization independence. The length of the interaction region is chosen as  $L = 2.1\mathrm{mm}$  in order to obtain a balanced splitting ratio.

In the interaction region the two waveguides are at different depths in the glass. To connect one coupler to the following, we designed a structure where the waveguides continuously vary the depth, as shown with the color codes in Fig. 2(c). The basic cell of the network, depicted in Fig. 2(d), acts as a Mach-Zehnder interferometer. For the correct operation of the quantum walk all the interferometers present in the network must be phase balanced. This is intrinsically achieved with the highly symmetric three-dimensional geometry implemented in the network [Figs. 2(c) and 2(d)]. The two central waveguides of the structure start with an initial separation of  $250\mu \mathrm{m}$  to couple the device with a single-mode fiber array, while at the output the waveguides are separated by  $70~\mu \mathrm{m}$ . The whole chip is  $32\mathrm{mm}$  long.

To carry out and characterize the different quantum walks we adopted the experimental apparatus reported in Fig. 3. Different single photon and two-photon states were injected into the network of DCs. The singlet-triplet transition within the Bell basis was performed by applying a  $\pi$  shift in the phase  $\phi$  of the state  $\frac{1}{\sqrt{2}}(|H\rangle_A|V\rangle_B + e^{i\phi}|V\rangle_A|H\rangle_B)$  through rotations of half- and quarter-wave plates (see Fig. 3). Fine phase adjustment was performed by a voltage liquid crystal (LC) device intercepting mode  $k_{A}$ .

The output of the integrated device is collected by a suitable telescope, split through a bulk beam splitter and then coupled to two multimode fibers (MMFs). By independently translating the MMFs on the arms  $C$  and  $D$  we select the output ports to detect, respectively  $I$  and  $J$ , and measure the single photon signals  $\mathcal{S}_C(I)$  and  $\mathcal{S}_D(J)$  and two-photon coincidences  $\mathcal{C}_{CD}(I,J)$ .

As a first measurement we characterized the quantum walk circuit with single photons injected in either mode  $k_{A}$  or  $k_{B}$ . By measuring the output signals  $S_{C}(I)$  we obtained the single-particle distributions. In order to demonstrate the polarization insensitivity of our device, we repeated this measurement by injecting light in different polarization states—horizontal, vertical, diagonal and antidiagonal—always observing very similar distributions [28].

![](images/1e7464c5bc95297be94543077818811eed2b38693f4537193c5620bd193bf6d7.jpg)  
FIG. 3 (color online). The experimental setup can be divided into three parts. (i) The source: polarization entangled photon pairs at wavelength  $\lambda = 806\mathrm{nm}$  generated via spontaneous parametric down conversion in a  $1.5\mathrm{mm}\beta$  -barium borate crystal (BBO) cut for type-II noncollinear phase matching, pumped by a cw diode laser with power  $P = 50~\mathrm{mW}$  [35]. Wave plates (WPs) allow generation of any single photon state and the Bell states. A delay line is inserted to control the temporal superposition of the photons, which are injected into the integrated device through single-mode fibers (SMFs). Interference filters determine the photon bandwidth  $\Delta \lambda = 6\mathrm{nm}$ . (ii) Integrated quantum walk circuit realized by ultrafast laser writing technique (see inset on the left). (iii) Measuring apparatus: the chip output is divided by a beam splitter (BS) and magnified through a set of two lenses. The photons coupled to multimode fibers (MMFs) are then delivered to single photon counting modules. The MMFs are mounted on motorized translation stages in order to select an arbitrary combination of two output ports and measure two-photon coincidences. Polarization controllers (PCs) are used before the chip to compensate for the polarization rotations induced by the fibers.

Each experimental distribution was compared with the expected one by the similarity  $S = (\sum_{i,j} \sqrt{D_{ij}D_{i,j}^{\prime}})^2 / \sum_{i,j} D_{ij} \sum_{i,j} D_{ij}^{\prime}$ , which is a generalization of the classical fidelity between two distributions  $D$  and  $D^{\prime}$ . The mean value over the tested input polarization states is  $S_{1\mathrm{ph}} = 0.992 \pm 0.002$ .

As a second step we injected two-photon entangled states. The distribution of the triplet and singlet states  $|\Psi^{+}\rangle$  ( $\phi = 0$ ) and  $|\Psi^{-}\rangle$  ( $\phi = \pi$ ) emerging from the quantum walk was reconstructed by measuring the coincidence counts  $C_{CD}(I,J)$  for each combination of the indices  $I$  and  $J$ . The measured bosonic and fermionic distributions compared with the expected ones are reported in Figs. 4(a) and 4(b) for  $|\Psi^{+}\rangle$  and  $|\Psi^{-}\rangle$ . As done for the measurements on the single photon quantum walk, we plotted the probability distributions for the walkers to be in the final positions  $i$ ,  $j$  of the quantum walk, which is related to the probability of photons to emerge from the output ports  $I$  and  $J$  of the BS array [28].

In Fig. 4 we observe how the particle symmetry affects the quantum walks. Note that some of the diagonal elements of the fermionic two-particle walk are nonzero both in the theoretical and experimental distribution. Indeed Fig. 4 reports the probability distribution of the walk positions and not of the physical spatial modes. In fact, the expected probability to measure two fermions over the same output spatial mode is vanishing [28].

![](images/c3a8d7bbaf62bacbfc2f42060bc9aa800254ec057d49fd609f8835ede74d64bc.jpg)

![](images/5d513fe5c77ed385d4a4a74f27d58d5a9b8a3429a493c6c14e72e427d6c59b06.jpg)

![](images/2e99f71a6538ac5d8eaf5ed0e63df2f19cf4a59d2bb4c0881bd5c05b9e766624.jpg)  
FIG. 4 (color online). Two-particle quantum walks: ideal (left) and measured (right) distributions of (a) bosonic, (b) fermionic and (c) anyonic (with  $\phi = \pi /2$ ) quantum walks.

Furthermore, by considering a generic phase  $\phi$  (different from 0 and  $\pi$ ), it is possible to simulate the behavior of the quantum walk of two anyons, particles with a non-semi-integer spin that represent a generalization of fermions and bosons [29]. Precisely, the entangled state  $|\Psi^{\phi}\rangle = \frac{1}{\sqrt{2}}(|H\rangle_{A}|V\rangle_{B} + e^{i\phi}|V\rangle_{A}|H\rangle_{B})$  simulates two anyons characterized by creation operators satisfying  $c_{i}c_{j} = e^{i\phi}c_{j}c_{i}$  and  $c_{i}c_{j}^{\dagger} = e^{i\phi}c_{j}^{\dagger}c_{i} + \delta_{ij}$ . These systems exhibit both bunching and antibunching behaviors (i.e., diagonal and off-diagonal elements in the final distribution). As a further measurement, we therefore prepared some anyonic states  $|\Psi^{\phi}\rangle$ , in particular, with  $\phi = \frac{\pi}{4}$ ,  $\frac{\pi}{2}$ ,  $\frac{3}{4}\pi$ , and measured the output probabilities. In Fig. 4(c) the distribution for  $\phi = \frac{\pi}{2}$  is reported as an example of an anyonic behavior.

The experimental data can be compared with the theoretical distributions by the similarity obtaining  $S_{\mathrm{bos}} = 0.982 \pm 0.002$  and  $S_{\mathrm{fer}} = 0.973 \pm 0.002$  for the bosonic and fermionic quantum walk and  $S_{\mathrm{any}}^{\pi /4} = 0.987 \pm 0.002$ ,  $S_{\mathrm{any}}^{\pi /2} = 0.988 \pm 0.001$  and  $S_{\mathrm{any}}^{3\pi /4} = 0.980 \pm 0.002$  for the anyonic quantum walks with  $\phi = \frac{\pi}{4}, \frac{\pi}{2}, \frac{3}{4}\pi$ , respectively. The obtained results are in good agreement with the expected behaviors.

In conclusion, we presented the behavior of a discrete quantum walk based on an integrated array of symmetric,

polarization insensitive, directional couplers in which two-photon polarization entangled states are injected. Exploiting the different statistics of singlet and triplet entangled states, such a scheme allowed us to simulate how symmetric and antisymmetric particles travel through the quantum walk.

The insensitivity to photon polarization, high accuracy in the phase control and intrinsic scalability of the integrated multi-DC network presented in this work, pave the way to further advanced investigations on complexity physics phenomena. For instance, by introducing suitable static and dynamic disorder in the walk it would be possible to simulate the interruption of diffusion in a periodic lattice, like Anderson localization [30-33], and the noise-assisted quantum transport effect[9,34].

This work was supported by EU-Project CHISTERA-QUASAR, FIRB-Future in Ricerca HYTEQ and PRIN 2009.

Note added.-Recently, the simulation of quantum statistics with entangled photons within a continuous quantum walk was reported online [36].

*Corresponding author. fabio.sciarrino@uniroma1.it

[1] A.M. Childs, Phys. Rev. Lett. 102, 180501 (2009).  
[2] J. Kempe, Contemp. Phys. 44, 307 (2003).  
[3] F.W. Strauch, Phys. Rev. A 74, 030301 (2006).  
[4] A. Schreiber et al., Phys. Rev. Lett. 104, 050502 (2010).  
[5] A. Schreiber et al., Phys. Rev. Lett. 106, 180403 (2011).  
[6] V. Potocek et al., Phys. Rev. A 79, 012325 (2009).  
[7] M. Stefanak, I. Jex, and T. Kiss, Phys. Rev. Lett. 100, 020501 (2008).  
[8] Y. Lahini et al., Phys. Rev. Lett. 105, 163905 (2010).  
[9] M. Mohseni et al., J. Chem. Phys. 129, 174106 (2008).  
[10] J. K. Gamble et al., Phys. Rev. A 81, 052313 (2010).

[11] M. Karski et al., Science 325, 174 (2009).  
[12] H. Schmitz et al., Phys. Rev. Lett. 103, 090504 (2009).  
[13] F. Zahringer et al., Phys. Rev. Lett. 104, 100503 (2010).  
[14] C. A. Ryan et al., Phys. Rev. A 72, 062317 (2005).  
[15] H.B. Perets et al., Phys. Rev. Lett. 100, 170506 (2008).  
[16] A. Peruzzo et al., Science 329, 1500 (2010).  
[17] J.O. Owens et al., New J. Phys. 13, 075003 (2011).  
[18] Y. Omar et al., Phys. Rev. A 74, 042304 (2006).  
[19] P. K. Pathak and G. S. Agarwal, Phys. Rev. A 75, 032351 (2007).  
[20] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.108.010502 for details about the equivalence between entangled states and the bosonic and fermionic quantum walk.  
[21] H. Jeong, M. Paternostro, and M. S. Kim, Phys. Rev. A 69, 012310 (2004).  
[22] P.P. Rohde et al., New J. Phys. 13, 013001 (2011).  
[23] R. R. Gattass and E. Mazur, Nature Photon. 2, 219 (2008).  
[24] G. Della Valle et al., J. Opt. A 11, 049801 (2009).  
[25] L. Sansoni et al., Phys. Rev. Lett. 105, 200503 (2010).  
[26] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.108.010502 for more details about the chip fabrication and single photon characterization.  
[27] A. Szameit et al., Opt. Express 15, 1579 (2007).  
[28] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevLett.108.010502 for more details about the output probabilities.  
[29] F. Wilczek, Phys. Rev. Lett. 48, 1144 (1982).  
[30] P. Anderson, Phys. Rev. 109, 1492 (1958).  
[31] P. Torma, I. Jex, and W.P. Schleich, Phys. Rev. A 65, 052110 (2002).  
[32] J.P. Keating et al., Phys. Rev. A 76, 012315 (2007).  
[33] Y. Yin, D.E. Katsanos, and S.N. Evangelou, Phys. Rev. A 77, 022302 (2008).  
[34] F. Caruso et al., Phys. Rev. A 83, 013811 (2011).  
[35] P. Kwiat et al., Phys. Rev. Lett. 75, 4337 (1995).  
[36] J.C.F. Matthews et al., arXiv:1106.1166.