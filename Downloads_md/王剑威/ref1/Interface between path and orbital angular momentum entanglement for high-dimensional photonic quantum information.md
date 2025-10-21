ARTICLE

Received 24 Feb 2014 | Accepted 25 Jun 2014 | Published 30 Jul 2014

DOI: 10.1038/ncomms5502

# Interface between path and orbital angular momentum entanglement for high-dimensional photonic quantum information

Robert Fickler $^{1,2}$ , Radek Lapkiewicz $^{1,2}$ , Marcus Huber $^{3,4}$ , Martin P.J. Lavery $^{5}$ , Miles J. Padgett $^{5}$  & Anton Zeilinger $^{1,2}$

Photonics has become a mature field of quantum information science, where integrated optical circuits offer a way to scale the complexity of the set-up as well as the dimensionality of the quantum state. On photonic chips, paths are the natural way to encode information. To distribute those high-dimensional quantum states over large distances, transverse spatial modes, like orbital angular momentum possessing Laguerre Gauss modes, are favourable as flying information carriers. Here we demonstrate a quantum interface between these two vibrant photonic fields. We create three-dimensional path entanglement between two photons in a nonlinear crystal and use a mode sorter as the quantum interface to transfer the entanglement to the orbital angular momentum degree of freedom. Thus our results show a flexible way to create high-dimensional spatial mode entanglement. Moreover, they pave the way to implement broad complex quantum networks where high-dimensionally entangled states could be distributed over distant photonic chips.

The progress in technological developments over the last decades has enabled the realization of highly complex photonic quantum experiments<sup>1</sup>. A popular approach to increase the complexity of the set-up and the dimensionality of the observed system uses integration of optical elements on photonic chips. On these chips the most convenient way of encoding information is the path of the photons, which is inherently extendable to higher-dimensional systems<sup>2,3</sup>. Another possibility of encoding high-dimensional quantum information is the transverse spatial mode of light<sup>4</sup>. The fact that beams encoded with orbital angular momentum (OAM) can co-propagate along the same optical axes makes their use, especially over long distances, advantageous<sup>5-9</sup>. Various modes, such as OAM-carrying Laguerre-Gauss (LG)<sup>10,11</sup>, Ince-Gauss<sup>12</sup> and Bessel-Gauss<sup>13</sup>, have been used to demonstrate experimentally high-dimensionally entangled states and to implement quantum informational tasks. In a wide quantum network<sup>14</sup>, both degrees of freedom, local on-chip path encoding and long-distance bridging spatial modes, will have to be matched to each other. Recently, first experiments of an integrated OAM beam emitter demonstrated an interface between both fields, although not yet in the quantum regime<sup>15</sup>. In another approach, q-plates have been demonstrated to interface the OAM with the polarization of photons<sup>16,17</sup>.

In this Article we demonstrate a quantum interface between two approaches to high-dimensional photonic quantum information: path encoding for complex on-chip experiments and OAM carrying light modes to transmit the information over large distances. At the same time, we investigate a flexible way to create higher-dimensional OAM entanglement that does not rely on angular momentum correlation. The essential tool in our experiment is a mode sorter (MS) that was invented $^{18,19}$  to convert the OAM content of an incident light beam to lateral positions of the output beam. By using this device in reverse, different spatial positions can be transformed to the cylindrically symmetric LG modes. We demonstrate that a high-dimensional path-entangled state can be transferred to high-dimensional OAM entanglement with the help of the reversed MS.

# Results

Generation of OAM modes with a MS in reverse. Transverse spatial LG modes have a helical phase front  $e^{il\theta}$ , where  $l$  can take any integer value and represents the quanta of OAM each individual photon possesses<sup>20</sup>. If  $l \neq 0$ , such modes exhibit a vortex along the beam axis and show a ring-shaped intensity structure; consequently they are also called 'doughnut modes'. LG modes can be used to transmit more classical information<sup>5-9</sup> or realize a higher-dimensional quantum state<sup>11,21,22</sup>. To access the encoded information efficiently a MS was developed<sup>18,19</sup>, which consists of two freeform refractive optical elements that convert the OAM content of an incident light field to lateral positions of the output. The first element maps the azimuthal to the lateral coordinates. Thereby, the ring-shaped intensity is transferred to a straight intensity line and the  $l$ -dependent helical phase structure to a transverse phase gradient. The second element corrects for phase distortion due to optical path length differences. A lens after the second element Fourier-transforms the transverse phase gradient to specific spatial position, that is, finishes the sorting of the modes. Recently, the operation of the MS in reverse was demonstrated by converting a light field with a transverse phase gradient, which has been created with a spatial light modulator (SLM), into an LG mode<sup>23</sup>.

Here we investigate a different, simple way of using the MS operated in reverse as a source for OAM states. A narrow slit that diffracts the light is positioned in the focal plane of the lens (Fig. 1

![](images/676a7e8921a9aad0d8238d9ef62545c535e6594baba6f67ee4334be2e202703e.jpg)  
Figure 1 | Generation of OAM states from lateral position states. False colour images recorded with a CCD camera are shown for various OAM states up to the 10th order (white numbers). The distance between the lateral positions of the slit that generate integer OAM states was around  $150\mu \mathrm{m}$  for the shown images. In between these positions, fractional OAM modes are generated. The multiple ring structure indicates the creation of higher-order radial modes containing the same OAM. It may be suppressed by shortening the length of the slit. Inset: Sketch of the set-up, where light is diffracted through a movable slit (width  $\sim 100\mu \mathrm{m}$ ) positioned in the focal plane of a lens. It is transformed by two freeform refractive optical elements (MS—mode sorter in reverse) into different OAM states depending on the slit position (detailed description in the main text).

inset). Thus, behind the lens, a parallel beam emerges with a phase profile given by the position of the slit relative to the optical axis. That phase distribution can be adjusted to be a multiple of  $2\pi$  by adjusting the lateral position of the slit. A subsequent MS in reverse transforms the state's amplitude distribution into a circle and thus into an OAM state (Fig. 1 inset). A continuous lateral movement of the slit leads to integer OAM modes at multiples of  $2\pi$  and fractional OAM in intermediate positions (see Fig. 1 and Supplementary Movie 1). To define the lateral position states, we overfill the slit with a Gaussian beam. Hence, the specific parameters of the slit define the characteristics of the OAM state generated. The width of the slit was chosen such that it corresponds approximately to the diffraction-limited spot size of a beam being focused by the lens just before the MS. The height of the slit defines the radial characteristics, but is not specifically controlled and larger than the beam radius in our experiment. As height is mapped to the radius (logarithmically) of the OAM beam generated, this will result in an OAM state with a corresponding radial extent. Additionally, hard apertures are present in the optical elements of the MS (see the inset in Fig. 1), which lead to diffraction of the transformed beam. Both, the unrestricted slit height and the apertures, result in an observation of higher-order radial modes containing the same OAM. A similar effect has been used in an experiment where OAM-containing Bessel beams have been separated by the MS in their azimuthal and radial components[24]. With our simple approach we were able to create LG modes up to order  $l = \pm 10$ . The order of the generated modes was only limited by the size of the Gaussian laser beam used to illuminate the slit. Importantly, by using multiple slits superpositions of LG modes could also be generated[25] (Fig. 2).

To confirm that the generated annular-shaped modes have the correct helical phase, we modulate the generated modes with the

opposite-handed phase holograms displayed on a SLM and investigate the resulting mode. First, we image the modulated mode with a charge-coupled device (CCD) camera. The recorded modal structure shows an intensity along the beam axis that resembles a fundamental Gauss mode or higher-order radial mode containing no OAM (see three exemplary tests in Fig. 3a). In a second step, we unambiguously determine the OAM mode purity by adding a grating to the phase pattern on the SLM. We then couple the modulated first diffraction order into a single-mode fibre, thereby filtering higher-order components $^{10,26}$ . By additionally changing the phase holograms on the SLM, we are able to measure the efficiency with which the expected mode is generated and thereby the modal overlap between this mode and its neighbouring modes (see Fig. 3b). Similar to the overlap if the interface is used for sorting $^{18}$ , we find an average overlap of  $17 \pm 8\%$  between the closest neighbouring modes,  $5 \pm 4\%$  between the second closest neighbours and  $0.7 \pm 0.6\%$  between the third closest neighbouring modes. Note that this performance might be improved by a recently introduced version of the MS scheme $^{27}$ .

Interfacing high-dimensional path and OAM entanglement. After characterization of the reversed MS as an interface between the lateral position and OAM, we demonstrate its use in quantum optical experiments and transform a bipartite path-entangled state to an OAM-entangled state, even for higher-dimensional states. We create pairs of orthogonally polarized, path-entangled photons from position correlation in a spontaneous parametric

![](images/e534758255e15e4c91d31d072eaacdf8bd0cc39a4c83d226b9ef95a4de1a7633.jpg)  
Figure 2 | Creation of superpositions of OAM states. If a double or triple slit is placed in front of the MS (Fig. 1 inset) different superpositions of OAM modes are created (false colour images) depending on the slit dimensions and focusing parameters of the lens (see Methods). All imaged modes show reasonable qualitative agreement with the theoretical calculation of the expected superpositions (insets).

![](images/f7046686a41424ad703c69f06a9278c04f233cf9b907855af29057ac506a1c68.jpg)

![](images/8e81463211812d083a2e353680ccacf4f44922068cc3f9a1f12a40e0982bccc0.jpg)

![](images/7fa0cc53b6ed27a6675d2d4d99fda2583011792fc94433adafb47031e71983ac.jpg)  
a

down-conversion process $^{2,28,29}$  (Fig. 4a and Methods). By placing a triple slit directly behind (less than  $1\mathrm{mm}$ ) the crystal we filter out only three positions, which leads to an expected two-photon qutrit path-entangled state

$$
| \psi \rangle = a | S _ {1} \rangle_ {\mathrm {H}} | S _ {1} \rangle_ {\mathrm {V}} + e ^ {i \phi_ {1}} b | S _ {2} \rangle_ {\mathrm {H}} | S _ {2} \rangle_ {\mathrm {V}} + e ^ {i \phi_ {2}} c | S _ {3} \rangle_ {\mathrm {H}} | S _ {3} \rangle_ {\mathrm {V}}, \tag {1}
$$

where  $S_{1/2/3}$  denote the slit that both photons pass through and the subscripts H/V label their polarization. The amplitudes  $a$ ,  $b$  and  $c$  ( $a^2 + b^2 + c^2 = 1$ ) as well as the phases  $\phi_1$  and  $\phi_2$  are described by real numbers and depend on the pump beam behind each slit. Therefore, they are flexibly adjustable by modulating the intensity and phase of the pump beam. If only two slits are used a state is created that consists of the first two terms.

The slits are placed in the focal plane of a lens followed by the reversed MS, which leads to a transformation of the path entanglement to the OAM degree of freedom. Thus, the total transformation acts as an interface between the high-dimensional path and spatial mode entanglement (Fig. 4b). In our experiment the distance between the three (two) slits corresponds to the 0th,  $-3\mathrm{rd}$  and  $+3\mathrm{rd}$  order LG modes (0th and  $-3\mathrm{rd}$  order). We chose these three orders to reduce the earlier-demonstrated modal overlap of the MS to  $< 1\%$ . Hence the expected state can be written as

$$
| \psi \rangle = a | - 3 \rangle_ {\mathrm {H}} | - 3 \rangle_ {\mathrm {V}} + e ^ {i \phi_ {1}} b | 0 \rangle_ {\mathrm {H}} | 0 \rangle_ {\mathrm {V}} + e ^ {i \phi_ {2}} c | + 3 \rangle_ {\mathrm {H}} | + 3 \rangle_ {\mathrm {V}}, \tag {2}
$$

where  $-3, 0$  and  $3$  label the order of the mode or OAM quanta. The flexibility in adjusting the amplitudes, phases, OAM values and dimensionality of the state (via transmittance, positions and number of slits) implies a general method to custom-tailor high-dimensional OAM entanglement. To verify the OAM entanglement we split the transferred photon pair with a polarizing beam splitter and analyse each photon with a spatial mode filter. Again, we realize the filter by a combination of a phase hologram on the SLM and a single-mode fibre $^{10,26}$ . Single-photon detectors (avalanche diodes) together with a coincidence logic are used to register correlations between the two spatial modes of a pair (Fig. 4c).

Measuring high-dimensional OAM entanglement. We quantitatively demonstrate entanglement by using a simple, powerful entanglement witness that compares the extracted fidelity

![](images/434be12611cee036d14020d166db4caa42826c3d1777254bb252c8f5f8e51925.jpg)  
Figure 3 | Examination of the generated modes. (a) We use an SLM to modulate the generated mode (left side) with the opposite-handed phase hologram (phase modulation shown in grey scale, linearly from  $0 =$  black to  $2\pi =$  white). The resulting intensities (right side) resemble the expected fundamental Gauss mode with an on-axis intensity maximum. However, a reduction of the modulated Gauss mode quality can be seen for higher orders. (b) We quantify these results by additional modulation of each generated mode (from  $-3$ rd order, dark blue, to 3rd order, dark green) with phase holograms of all neighbouring modes and coupling to a single-mode fibre (filtering higher-order modes). Thereby, we are able to measure the purity of the generated modes. We find that the expected OAM modes of a specific order are generated depending on the particular slit positions with high efficiency (highest bar for each slit position). The overlap with direct neighbouring modes is around  $20\%$  , which decreases down to  $< 1\%$  for third neighbours. The varying relative power for different orders stems from the Gaussian mode shape of the laser, through which the slit was moved.  
b

![](images/91c51a75ed0833ecf25021fce6b121af43078ad691cd3f8d16606ad461464511.jpg)  
Figure 4 | Schematic of the experimental set-up to interface the high-dimensional path and OAM entanglement. (a) By pumping a non-linear crystal (ppKTP) with a 405-nm laser (blue) we create pairs of orthogonally polarized photons with 810 nm wavelength in a down-conversion process (red). A triple slit is placed directly behind the crystal. Both photons of a pair emerge together through one of the three slits. The final state is a superposition of the pair passing the three slits, hence the pair is entangled in the path. (b) A lens transforms the path entanglement to a transverse momentum entanglement, which is then transformed by the reversed mode sorter (black tube) to the OAM degree of freedom. (c) The OAM-entangled pair of photons is split by a polarizing beam splitter (PBS) and the vertically polarized photon is rotated by a half-wave plate (HWP) to the required polarization for phase modulation with the SLM. Each photon is filtered individually depending on its spatial mode, by a hologram displayed on a spatial light modulator (SLM) and by coupling to single-mode fibres (SMF). Avalanche photo-diode, single-photon detectors and a coincidence logic (brown box) are utilized to detect photon pairs and the observed correlations are subsequently analysed.

![](images/a10040633a7a396032de131684f501ea9d4e4dff171e4de4911b7e5f1725607a.jpg)  
Figure 5 | Coincidence measurements to confirm the two-dimensional OAM entanglement. With the hologram displayed on the SLM we measured for each observed photon the superposition  $|-3\rangle +e^{i\phi}|0\rangle$ , where  $\phi$  is an adjustable phase between  $0^{\circ}$  and  $360^{\circ}$ . We measured coincidence fringes for four different settings of the phase  $\phi_{1}$  of one photon while the phase  $\phi_{2}$  setting for the partner photon is scanned in steps of  $22.5^{\circ}$ . The lines show the best  $\sin^2$ -fits that lead to visibilities of  $\sim 90\%$ , confirming entanglement. For one setting  $(90^{\circ})$  the maximum is found to be significantly smaller than for the other phase settings. This might originate from a slight misalignment of the mode sorter. Error bars (if big enough to be seen) depict one sigma confidence with Poissonian count statistics assumed.

(overlap between an ideal state of equation (2) and the measured data) and the maximally expected fidelity for  $d$ -dimensional entangled states. If the measured fidelity exceeds the known bound for a  $d$ -dimensional entangled state, our results prove at least  $(d + 1)$ -dimensional entanglement (see Methods).

In a first experiment, we test for qubit entanglement by measuring correlations between the 0th order (Gauss mode) and the  $-3\mathrm{rd}$  order LG mode (Fig. 5). From the measured maxima and minima of these correlation fringes, the visibilities can be deduced. The highest fidelity calculated from the visibilities in all mutually unbiased bases was  $97 \pm 2\%$  with an ideal state where  $a = 0.54$  and  $b = 0.84$ . The maximum fidelity that would be achievable for separable states is  $71\%$ .

In addition to the results of the entanglement witness, we used the measurements shown in Fig. 5 to test for two-dimensional entanglement with the popular criterion of a CHSH-Bell inequality<sup>30</sup>. For local realistic theories the following bound holds:

$$
S _ {\mathrm {C H S H}} = \left| E (\alpha , \beta) - E \left(\alpha^ {\prime}, \beta\right) + E (\alpha , \beta^ {\prime}) + E \left(\alpha^ {\prime}, \beta^ {\prime}\right) \right| \leq 2, \tag {3}
$$

where  $\alpha$ ,  $\alpha'$ ,  $\beta$  and  $\beta'$  denote different measurement settings (phases of the measured superpositions) and  $E$  stands for the normalized expectation value for photon pairs to be found with this combination of modes. In our measurement we achieve a value of  $2.47 \pm 0.04$ , which violates the classical bound by more than 10 standard deviations (Poissonian count statistics assumed). Both results confirm our observation of two-dimensional entanglement.

In a second experiment we take advantage of all three implemented slits and test for OAM qutrit entanglement. Similar to earlier results $^{12,22}$ , the entanglement witness enables us to draw conclusions about the global dimensionality of the entanglement while restricting ourselves to qubit-subspace measurements. In our experiment this approach corresponds to the measurements of all visibilities in all two-dimensional subspaces that is for  $l$ -values of  $0/ - 3$ ,  $0/+3$  and  $-3/+3$ . The best statistical significance for genuine qutrit entanglement was found for an ideal state where  $a = c = 0.48$ ,  $b = 0.73$ . Here, the fidelity obtained from the measured visibilities is  $89 \pm 4\%$ , which exceeds the upper bound for any two-dimensional entangled state ( $77\%$ ) by more than three standard deviations. Note that in both cases (qubit and qutrit entanglement) no background subtraction has been applied. Also, the largest amplitude was found for the Gauss mode because it corresponds to the central slit where the pump intensity and thus the down-conversion rate is maximal.

# Discussion

Our set-up is not limited to qutrits but can be naturally extended to  $d$ -dimensional entanglement. A broader pump beam and a wider crystal in combination with a  $d$ -slits arrangement would lead to  $d$  possible paths and thus  $d$ -dimensional entanglement. A further way to increase the dimensionality of the path entanglement as well as the efficiency would be an arrangement with many integrated down-conversion crystals<sup>31</sup> in waveguide structures or fibre-coupled down-conversion crystals pumped in

parallel<sup>3</sup>. In that case the waveguides or a fibre groove array could replace the multiple slits. Furthermore, it has been shown recently that the MS works for up to 50 states<sup>32</sup> and that the MS can be improved to reduce the overlap between neighbouring modes<sup>27</sup>. These improvements in MS design suggest that our approach can be readily extended to higher qudit entanglement. Although outside of the scope of the present work, it will be interesting to further investigate the detected higher-order radial structures, their potential as an additional dimension to encode information and their relation to the slit height. In addition, a suppression of the additional rings, by adapting the shape of the slit and improving the MS performance, might be crucial for the efficient interconnection of waveguide structures over long distances.

In conclusion, we have shown that the MS in combination with a slit can be used, in reverse, to generate LG modes and their superpositions up to at least  $l = \pm 10$ . Using fast switching techniques for optical paths the method can increase the switching rate between different LG beams in classical information technologies or LG-mode-based quantum cryptography applications. In addition, our results demonstrate a flexible way to create high-dimensional OAM entanglement. Most importantly, they show a way to implement an quantum interface between two approaches to high-dimensional quantum information: path encoding in waveguide structures for scalable, complex photonic quantum circuits including arbitrary unitary operation for higher-dimensional states $^{1,3}$ , and OAM encoding to distribute those high-dimensional quantum states $^{5-9}$  in a broad quantum network scenario.

# Methods

Creation of path-entangled photons. To create correlated photons we used a cw  $405\mathrm{-nm}$  laser diode to pump a periodically poled potassium titanyl phosphate crystal  $(1\times 2\times 5\mathrm{mm}^3)$  with  $\sim 30\mathrm{mW}$  pump power. The pump beam diameter was  $\sim 1$  mm (FWHM), which leads to a broad region where the two orthogonally polarized photons (Type II down-conversion) with  $810\mathrm{nm}$  wavelength can be created. In the near-field of the crystal—directly behind it—the photons are correlated in the transverse spatial position[28,29], that is, if one photon is found to be at a specific transverse spatial location the partner photon will be found ideally at exactly the same location too. This stems from the down-conversion process itself, where the pump photon generates two down-converted photons at some transverse spatial position of the crystal. Because the actual location of the down-conversion process is not determined, that is, it can happen everywhere within the pump beam spread, the generated photon pairs are in a superposition of all possible positions. A double or triple slit placed behind the crystal selects only two or three lateral positions; thus the photon pairs that pass the slits are in a superposition of two or three locations. In other words, they are in path-entangled qubit or qutrit states. For the multi-slit arrangement, the slits had a width of  $150\mu \mathrm{m}$  and were separated by  $250\mu \mathrm{m}$ , which resemble the dimensions typically used for telecom-standard fibre arrays. A schematic of the set-up can be seen in Fig. 4a. The presented scheme is readily extendable to more than three-dimensional entanglement, by increasing the number of slits. Furthermore, our source could be directly connected to complex integrated waveguide structures.

Bipartite witness for  $d$ -dimensional entanglement. We develop a witness framework requiring only measurements in two-dimensional subspaces. From these subspace measurements we compute the fidelity  $F$  of the experimentally produced state with a specially chosen high-dimensional state. We then use the techniques developed below to bound the maximal overlap of states with a bounded Schmidt rank  $d$  and the chosen high-dimensional state. If the subspace measurements reveal a higher overlap than this bound, the production of at least  $d + 1$ -dimensional entanglement is proven.

Construction of the witness proceeds as follows. The Schmidt decomposition of the assumed high-dimensional state can be written as  $|\psi \rangle = \sum_{i=0}^{D-1} \lambda_i |ii\rangle$ , where  $i$  labels the different states (in our experiment the spatial modes),  $D$  denotes the dimension of the Hilbert space and the coefficients are chosen in a decreasing order, that is,  $\lambda_1 \geq \lambda_2 \geq (\ldots) \geq \lambda_d$  (in the main text  $\lambda_i$  corresponds to the amplitudes  $a$ ,  $b$  and  $c$ ). This choice has the advantage that  $\mathrm{Tr}(\rho |\psi\rangle\langle\psi|) = \sum_{i,j=0}^{D-1} \left(1 / \lambda_i \lambda_j\right)\langle ii|\rho|jj\rangle$ , where all appearing matrix elements can be determined by three visibility measurements in two-dimensional subspaces, the number of which scales as the square root of those required for a full-state tomography. We can now construct a witness for  $d$ -dimensional entanglement (Schmidt number witness) by comparing the two fidelities

$$
F = \operatorname {T r} (\rho | \psi \rangle \langle \psi |) \tag {4}
$$

and

$$
f _ {d} = \max  _ {\left| \phi_ {d} \right\rangle} \left| \left\langle \phi_ {d} \mid \psi \right\rangle \right| ^ {2} \tag {5}
$$

where  $\rho$  labels the density matrix related to our measurements and  $|\phi_d\rangle$  denotes states with a bounded Schmidt rank  $d$ . If equation  $F > f_{d}$  holds, the measurements cannot be explained by a  $d$ -dimensional entangled state; thus, the generated bipartite system was (at least) genuinely  $(d + 1)$ -dimensionally entangled.

Calculation of the maximal fidelity for  $d$ -entangled states proceeds in the following manner. The maximization in equation (5) runs over all states with at most  $d$ -dimensional entanglement (Schmidt rank  $d$ ). This maximal overlap between  $|\phi_d\rangle = \sum_{k,l=0}^{D-1}c_{kl}|kl\rangle$  and the guessed state  $|\psi\rangle$  (expressed in terms of the Schmidt coefficients) can be rewritten as

$$
\begin{array}{l} f _ {d} = \max  _ {| \phi_ {d} \rangle} \left| \left(\langle k l | \sum_ {k, l = 0} ^ {D - 1} c _ {k l} ^ {*}\right) \left(\sum_ {i = 0} ^ {D - 1} \lambda_ {i} | i i \rangle\right) \right| ^ {2} (6) \\ = \max  _ {| \phi_ {d} \rangle} \left| \sum_ {k, l, i = 0} ^ {D - 1} \langle k | i \rangle \langle l | i \rangle c _ {k l} ^ {*} \lambda_ {i} \right| ^ {2}. (7) \\ \end{array}
$$

By rearranging the terms and introducing the operator  $B = c_{kl}|k\rangle \langle l|$

$$
f _ {d} = \max  _ {| \phi_ {d} \rangle} \left| \operatorname {T r} \left(B ^ {\dagger} \sum_ {i = 0} ^ {D - 1} \lambda_ {i} | i \rangle \langle i |\right) \right| ^ {2} \tag {8}
$$

and the rank  $d$ -projector  $P_{d}B^{*} = B^{*}$  (which always exists if  $B^{*}$  is of rank  $d$ , as  $|\phi_d\rangle$  is of Schmidt rank  $d$ ), we get

$$
= \max  _ {| \phi_ {d} \rangle} \left| \operatorname {T r} \left(P _ {d} B ^ {\dagger} \sum_ {i = 0} ^ {D - 1} \lambda_ {i} | i \rangle \langle i |\right) \right| ^ {2}, \tag {9}
$$

and since the trace is invariant under cyclic permutations we can write

$$
f _ {d} = \max  _ {| \phi_ {d} \rangle} \left| \operatorname {T r} \left(B ^ {\dagger} \sum_ {i = 0} ^ {D - 1} \lambda_ {i} | i \rangle \langle i | P _ {d}\right) \right| ^ {2}. \tag {10}
$$

Using the Cauchy-Schwarz inequality for the Hilbert-Schmidt inner product (for the inner product  $\langle A,B\rangle \coloneqq \mathrm{Tr}(AB^{\dagger})$  it reads  $|\langle A,B\rangle |^{2}\leq \langle A,A\rangle \langle B,B\rangle)$  we get the inequality

$$
f _ {d} \leq \max  _ {\left| \psi_ {d} \right\rangle} \operatorname {T r} \left(B ^ {\dagger} B\right) \operatorname {T r} \left(P _ {d} \sum_ {i = 0} ^ {D - 1} \lambda_ {i} ^ {2} | i \rangle \langle i | P _ {d}\right). \tag {11}
$$

Because  $\mathrm{Tr}B^{\dagger}B = \sum_{k,l = 0}^{D - 1}c_{kl}c_{lk}^{*}\leq 1$  and choosing the obviously maximizing

$P = \sum_{i=0}^{d-1}|i\rangle\langle i|$  we get the upper bound for the fidelity of  $d$ -dimensional entangled states of

$$
f _ {d} \leq \sum_ {i = 0} ^ {d - 1} \lambda_ {i} ^ {2}. \tag {12}
$$

By choosing  $|\phi_d\rangle = \left(1\bigg{/}\sqrt{\sum_{i = 0}^{d - 1}\lambda_i^2}\right)\sum_{i = 0}^{d - 1}\lambda_i|i\rangle$  we find that  $f_{d}\geq \sum_{i = 0}^{d - 1}\lambda_{i}^{2},$  thus proving that our bound is indeed tight, that is,

$$
f _ {d} = \max  _ {| \phi_ {d} \rangle} | \langle \phi_ {d} | \psi \rangle | ^ {2} = \sum_ {i = 0} ^ {d - 1} \lambda_ {i} ^ {2}. \tag {13}
$$

The inequality for the witness of  $d$ -dimensional entanglement follows from the above. Hence, from the visibility measurements in all two-dimensional subspaces we can now reveal information about the global dimensionality of the bipartite entanglement. If the following inequality holds, we have proven that our measurement results can only be explained by an at least  $(d + 1)$ -dimensionally entangled state:

$$
\operatorname {T r} (\rho | \psi \rangle \langle \psi |) > \sum_ {i = 0} ^ {d - 1} \lambda_ {i} ^ {2} \tag {14}
$$

Note that although we have derived the proof by assuming a pure state the witness holds even for mixed states because they would only lower the bound (due to the convexity of the fidelity). Thus, the presented witness is a state-independent test for high-dimensional entanglement.

# References

1. O'Brien, J. L., Furusawa, A. & Vuckovic, J. Photonic quantum technologies. Nat. Photon. 3, 687-695 (2009).  
2. Rossi, A., Vallone, G., Chiuri, A., De Martini, F. & Mataloni, P. Multipath entanglement of two photons. Phys. Rev. Lett. 102, 153902 (2009).  
3. Schaff, C. et al. Scalable fiber integrated source for higher-dimensional path-entangled photonic quNits. Opt. Express 20, 16145-16153 (2012).  
4. Andrews, D. L. & Babiker, M. (eds.) The Angular Momentum of Light (Cambridge University Press, Cambridge, 2012).

5. Gibson, G. et al. Free-space information transfer using light beams carrying orbital angular momentum. Opt. Express 12, 5448-5456 (2004).  
6. Tamburini, F. et al. Encoding many channels on the same frequency through radio vorticity: first experimental test. New J. Phys. 14, 033001 (2012).  
7. Wang, J. et al. Terabit free-space data transmission employing orbital angular momentum multiplexing. Nat. Photon. 6, 488-496 (2012).  
8. Bozinovic, N. et al. Terabit-scale orbital angular momentum mode division multiplexing in fibers. Science 340, 1545-1548 (2013).  
9. Krenn, Mario. et al. Twisted light communication through turbulent air across Vienna. Preprint at http://arxiv.org/abs/1402.2602 (2014).  
10. Mair, A., Vaziri, A., Weihs, G. & Zeilinger, A. Entanglement of the orbital angular momentum states of photons. Nature 412, 313-316 (2001).  
11. Vaziri, A., Weihs, G. & Zeilinger, A. Experimental two-photon, three-dimensional entanglement for quantum communication. Phys. Rev. Lett. 89, 240401 (2002).  
12. Krenn, M. et al. Entangled singularity patterns of photons in Ince-Gauss modes. Phys. Rev. A 87, 012326 (2013).  
13. McLaren, M. et al. Entangled Bessel-Gaussian beams. Opt. Express 20, 23589-23597 (2012).  
14. Kimble, H. J. The quantum internet. Nature 453, 1023-1030 (2008).  
15. Cai, X. et al. Integrated compact optical vortex beam emitters. Science 338, 363-366 (2012).  
16. Marrucci, L., Manzo, C. & Paparo, D. Optical spin-to-orbital angular momentum conversion in inhomogeneous anisotropic media. Phys. Rev. Lett. 96, 163905 (2006).  
17. Nagali, E. et al. Quantum information transfer from spin to orbital angular momentum of photons. Phys. Rev. Lett. 103, 013601 (2009).  
18. Berkhout, G. C., Lavery, M. P., Courtial, J., Beijersbergen, M. W. & Padgett, M. J. Efficient sorting of orbital angular momentum states of light. Phys. Rev. Lett. 105, 153601 (2010).  
19. Lavery, M. P. J. et al. Refractive elements for the measurement of the orbital angular momentum of a single photon. Opt. Express 20, 2110-2115 (2012).  
20. Allen, L. et al. Orbital angular momentum of light and the transformation of Laguerre-Gaussian laser modes. Phys. Rev. A 45, 8185-8189 (1992).  
21. Dada, A. C., Leach, J., Buller, G. S., Padgett, M. J. & Andersson, E. Experimental high-dimensional two-photon entanglement and violations of generalized Bell inequalities. Nat. Phys. 7, 677-680 (2011).  
22. Krenn, M. et al. Generation and confirmation of a  $(100 \times 100)$ -dimensional entangled quantum system. Proc. Natl Acad. Sci. USA 111, 6243-6247 (2014).  
23. Lavery, M. P. J. et al. The Measurement and Generation of Orbital Angular Momentum Using an Optical Geometric Transformation (SPIE LASE. International Society for Optics and Photonics, 2013).  
24. Dudley, A. et al. Efficient sorting of Bessel beams. Opt. Express 21, 165-171 (2013).  
25. Berkhout, G. C., Lavery, M. P., Padgett, M. J. & Beijersbergen, M. W. Measuring orbital angular momentum superpositions of light by mode transformation. Opt. Lett. 36, 1863-1865 (2011).  
26. Leach, J. et al. Violation of a Bell inequality in two-dimensional orbital angular momentum state-spaces. Opt. Express 17, 8287-8293 (2009).

27. Mirhosseini, M., Malik, M., Shi, Z. & Boyd, R. W. Efficient separation of the orbital angular momentum eigenstates of light. Nat. Commun. 4, 2781 (2013).  
28. Edgar, M. P. et al. Imaging high-dimensional spatial entanglement with a camera. Nat. Commun. 3, 984 (2012).  
29. Moreau, P. A., Mougin-Sisini, J., Devaux, F. & Lantz, E. Realization of the purely spatial Einstein-Podolsky-Rosen paradox in full-field images of spontaneous parametric down-conversion. Phys. Rev. A 86, 010101 (2012).  
30. Clauser, J. F., Horne, M. A., Shimony, A. & Holt, R. A. Proposed experiment to test local hidden-variable theories. Phys. Rev. Lett. 23, 880-884 (1969).  
31. Harder, G. et al. An optimized photon pair source for quantum circuits. Opt. Express 21, 13975-13985 (2013).  
32. Lavery, M. P. J. et al. Efficient measurement of an optical orbital-angular-momentum spectrum comprising more than 50 states. New J. Phys. 15, 013024 (2013).

# Acknowledgements

We thank Sven Ramelow and Mario Krenn for fruitful discussions, Milan Mosonyi for helping with the proof of the witness and Otfried Gühne for giving valuable insight into the solution, by pointing out that the overlap in equation (13) was already proved (in a different way) in his PhD thesis. This work was supported by the Austrian Science Fund (FWF) through the Special Research Program (SFB) Foundations and Applications of Quantum Science (FoQuS; Project No. F4006-N16), and the European Community Framework Programme 7 (SIQS, collaborative project, 600645). RF and RL are supported by the Vienna Doctoral Program on Complex Quantum Systems (CoQuS, W1210-2). MH would like to acknowledge the MarieCurie IEF grant QuaCoCoS-302021. MPJL and MJP are supported by the EPSRC.

# Author contributions

RL and RF conceived the experiment. RF designed and built the experiment, collected and analysed the data. RL and MPJL participated in designing and building of the experiment. MH developed the entanglement witness. The project was supervised by MJP and AZ. All authors contributed to discussing the results and the writing of the manuscript.

# Additional information

Supplementary Information accompanies this paper at http://www.nature.com/naturecommunications

Competing financial interests: The authors declare no competing financial interests.

Reprints and permission information is available online at http://www.nature.com/reprints/index.html.

How to cite this article: Fickler, R. et al. Interface between path and orbital angular momentum entanglement for high-dimensional photonic quantum information. Nat. Commun. 5:4502 doi: 10.1038/ncomms5502 (2014).