# Experimental Greenberger-Horne-Zeilinger entanglement beyond qubits

Manuel Erhard $^{1,2\star}$ , Mehul Malik $^{1,2,3}$ , Mario Krenn $^{1,2}$  and Anton Zeilinger $^{1,2\star}$

Quantum entanglement is important for emerging quantum technologies such as quantum computation and secure quantum networks. To boost these technologies, a race is currently ongoing to increase the number of particles in multiparticle entangled states, such as Greenberger-Horne-Zeilinger (GHZ) states. An alternative route is to increase the number of entangled quantum levels. Here, we overcome present experimental and technological challenges to create a three-particle GHZ state entangled in three levels for every particle. The resulting qutrit-entangled states are able to carry more information than entangled states of qubits. Our method, inspired by the computer algorithm Melvin, relies on a new multi-port that coherently manipulates several photons simultaneously in higher dimensions. The realization required us to develop a new high-brightness four-photon source entangled in orbital angular momentum. Our results allow qualitatively new refutations of local-realistic world views. We also expect that they will open up pathways for a further boost to quantum technologies.

Entanglement is an important workhorse of quantum technologies today, with applications ranging from fault-tolerant quantum computation to device-independent quantum communication $^{1,2}$ . The entanglement of more than two quantum particles, commonly known as GHZ entanglement $^{3,4}$ , not only opened the door to the strongest test of local realism $^{6}$ , but also forms a key ingredient of such technologies. Since the discovery of GHZ entanglement, experimental research on multiparticle entanglement has mainly focused on two-dimensional quantum systems or qubits $^{7}$  with realizations in physical systems including ions $^{8}$ , photons $^{9-11}$  and superconducting circuits $^{12,13}$ . In all of these systems, various concepts and procedures for increasing the number of entangled two-level systems, that is, qubits, exist. For example, for photons, a particularly simple experimental scheme uses polarizing beam splitters in combination with post-selection to produce arbitrarily high numbers of photons entangled in a GHZ manner $^{14}$ . However, no experiment has been able to create entanglement that is simultaneously high-dimensional and multipartite. This is mainly because we lack a conceptual understanding of how to create such states experimentally. In part, it can also be attributed to the lack of technologies for manipulating high-dimensional quantum states experimentally. Going beyond qubit GHZ entanglement thus poses a considerable challenge; overcoming this would lead to exciting new applications for quantum technologies and fundamental tests of quantum mechanics, such as the recent theoretical results on GHZ-like contradictions of local realism in higher dimensions $^{15-18}$ .

Here we show the experimental realization of a multiparticle entangled state using the orbital angular momentum (OAM) of light, where all photons are genuinely entangled in a high-dimensional manner. In a recent experiment, we showed the generation of a  $(3,3,2)$  multiphoton entangled state, where two photons reside in a three-dimensional space while the third lives in a two-dimensional qubit space[19]. Contrary to expectation, going from the  $(3,3,2)$  state to a genuinely three-dimensional GHZ state was not a straightforward step but required intrinsically different methods. Our experimental scheme uses a new type of multiport that

operates coherently and simultaneously on three photons in three dimensions each, forming a 27-dimensional operational space. This is in contrast to the  $(3,3,2)$  experiment $^{19}$  and several recent experiments on multiphoton entanglement $^{20,21}$ , all of which use binary two-photon manipulation techniques. In fact, the experimental generation of a three-dimensional GHZ state necessitates the manipulation of more than two photons in a higher-dimensional space, as we show by exploiting a link between quantum experiments and graph theory $^{22,23}$  (see Supplementary Information). The design of our experiment was originally suggested by the computer algorithm Melvin, which was designed for finding new experimental techniques in quantum mechanics $^{5,24-26}$ . The multiport found by Melvin can be used as a fundamental element for the generation and manipulation of high-dimensional and multiphoton quantum states in general, allowing the creation of three-dimensional GHZ states of any particle number using deterministic photon sources (see Supplementary Information for details).

To meet the tight technological requirements set by the multiport, we developed a new high-brightness, high-dimensional four-photon source that coherently creates two photon pairs entangled in their OAM degree of freedom. With the types of multiphoton sources used in previous experiments $^{19,20}$ , the measurement time for our experiment is estimated to be years. To overcome this serious limitation, we addressed problems arising from nonlinear effects such as Kerr lensing, temperature drifts and grey-tracking to increase our source brightness by about two orders of magnitude compared with previous sources, in turn reducing the required measurement time to days rather than years. To verify genuine three-particle three-dimensional entanglement, we use an entanglement witness that relies on measurements of the state fidelity to bound its dimensionality. Additionally, we demonstrate violations of the Mermin inequality in every two-dimensional subspace of our three-dimensional GHZ state. Finally, we show that the quality of our state is sufficient for a genuine high-dimensional and multipartite experimental violation of local-realistic world views.

# Experiment

We choose the OAM of photons $^{27-30}$  as a physical carrier of information in our experiment. The OAM of photons spans, in principle, an infinite-dimensional, discrete state space and can thus easily encode three different quantum levels. Any three-dimensional, three-photon GHZ state can be written as:

$$
\frac {1}{\sqrt {3}} \left(| a \rangle_ {\mathrm {A}} | b \rangle_ {\mathrm {B}} | c \rangle_ {\mathrm {C}} + | \bar {a} \rangle_ {\mathrm {A}} | \bar {b} \rangle_ {\mathrm {B}} | \bar {c} \rangle_ {\mathrm {C}} + | \bar {\bar {a}} \rangle_ {\mathrm {A}} | \bar {\bar {b}} \rangle_ {\mathrm {B}} | \bar {\bar {c}} \rangle_ {\mathrm {C}}\right) \tag {1}
$$

The letters within the ket vectors  $|\cdot \rangle$  refer to the different OAM quanta of  $\ell \hbar$ , where  $x, \overline{x}$  and  $\overline{\overline{x}}$  can take on any OAM value with the restriction that they are mutually orthogonal. The capital letters (A, B, C) refer to different photons.

Conceptually, the experimental generation of a three-dimensional three-photon GHZ state works according to the scheme in Fig. 1. We start with two pairs of three-dimensionally entangled photon pairs as an entanglement resource. The multiport then combines and manipulates three of the four photons such that ultimately a genuine three-dimensional GHZ state is created. Physically, the multiport operates in a 27-dimensional space and combines various quantum effects such as a multimode Hong-Ou-Mandel (HOM) interference $^{31,32}$ , coherent multimode superposition projections and single-photon interference.

Formulated in more detail, the four-photon source ideally emits two indistinguishable and three-dimensionally entangled states coherently, reading

$$
\begin{array}{l} \left(\alpha \left| 0, 0 \right\rangle_ {\mathrm {A}, \mathrm {B}} + \beta \left| 1, - 1 \right\rangle_ {\mathrm {A}, \mathrm {B}} + \beta \left| - 1, 1 \right\rangle_ {\mathrm {A}, \mathrm {B}}\right) \\ \otimes \left(\alpha^ {\prime} | 0, 0 \rangle_ {\mathrm {C}, \mathrm {D}} + \beta^ {\prime} | 1, - 1 \rangle_ {\mathrm {C}, \mathrm {D}} + \beta^ {\prime} | - 1, 1 \rangle_ {\mathrm {C}, \mathrm {D}}\right) \tag {2} \\ \end{array}
$$

where the coefficients  $\alpha$ ,  $\beta$ ,  $\alpha'$  and  $\beta'$  describe the probability amplitudes of the terms emitted by the two nonlinear crystals (NL1 and NL2) typically given by the spiral bandwidth<sup>33</sup>. This results in nine possible combinations of the four probability amplitudes, as shown in Fig. 2b. Three out of four photons are now guided to the multiport.

We focus on cases in which each detector A, B, C and D detects exactly one of the four photons, comprising a four-fold detection event. The OAM parity-sorter $^{34,35}$  sorts incoming photons according to their parity (even/odd). Inserted between photon paths B and C, the OAM parity-sorter thus prevents joint four-photon probability amplitudes containing both even and odd OAM quanta emitted by the two NLs, as depicted in Fig. 2b. Now, only five joint probability amplitudes remain, each containing OAM modes with the same parity. For the generation of a two-dimensional GHZ state, a distinction according to parity is already sufficient. In the three-dimensional case, however, there is still the cross-correlation between the odd OAM probability amplitudes, as shown in Fig. 2b. The joint probability amplitude  $| - 1,1 \rangle_{\mathrm{AB}} \otimes |1, - 1 \rangle_{\mathrm{CD}}$  is suppressed by the multiport as it does not result in a four-fold detection (no amplitude in path A; see multiport transformations in Fig. 2c). Interestingly, the other cross-connection between  $|1, - 1 \rangle_{\mathrm{AB}} \otimes | - 1,1 \rangle_{\mathrm{CD}}$  is prevented by multimode HOM interference from two different crystals at the beam splitter, as shown in Fig. 3c. After these two steps through the multiport, we are left with three remaining links. These connections represent the three-dimensional GHZ state generated. The photon in path A is always in the  $| + \rangle = |0\rangle +| - 1\rangle$  state and can therefore be factorized from the other three photons B, C and D. This means that photon A is no longer entangled with the other three photons. The remaining probability amplitudes undergo a transformation according to the transformation rules imposed by the multiport. Thus, the final state created in paths B, C, D reads:

![](images/acb06ea20f7ac16c72f1b667d524e9480000298b83597f76df5b23f433212bad.jpg)  
Fig. 1 | Concept of three-dimensional GHZ entanglement creation. A high-brightness four-photon source creates two pairs of three-dimensionally entangled photons. The multiport transforms three incoming photons coherently and simultaneously in its 27-dimensional operational space. Simultaneous detection of one photon in each detector results in the creation of a three-dimensional GHZ state, as depicted at the top.

$$
\left| \psi \right\rangle = \alpha \alpha^ {\prime} | 2, 0, 0 \rangle + \beta \beta^ {\prime} | - 1, - 1, - 1 \rangle - \beta \beta^ {\prime} | 3, 1, 1 \rangle \tag {3}
$$

where  $\alpha, \alpha', \beta$  and  $\beta'$  are the coefficients describing the spiral bandwidth from the NLs according to equation (2). Setting  $\alpha = \beta = \alpha' = \beta'$  and renormalizing results in a three-dimensional three-photon GHZ state as described in equation (1).

If our experiment were to use the types of high-dimensional multiphoton sources used in previous experiments[19], the measurement time required to certify high-dimensional genuine multipartite entanglement in our three-dimensional GHZ state would be 3.5 years. To address this problem, we designed a new, ultrabright multimode four-photon source that compensates for several detrimental nonlinear effects to achieve an improvement of two orders of magnitude in four-photon count rates. Our source uses a high-power femtosecond laser that is frequency-doubled through second-harmonic generation and focused into two nonlinear crystals, NL1 and NL2 (see Fig. 2a and Supplementary Information for details). To ensure perfect temporal and spatial indistinguishability and high collection efficiency, we take into account the joint-spectral-amplitude properties of the down-converted photon pairs, Kerr lensing effects at both nonlinear crystals, high-power phase-matching temperature drifts within the crystals and grey-tracking due to ultraviolet absorption. We compensate for the Kerr lensing effect between the two crystals by using a specifically designed telescope that corrects for the nonlinear Kerr lens generated in NL1, as depicted in Fig. 2a. Furthermore, the phase-matching temperature of the periodically poled crystals changes as the pump power is increased. We automatically adjust the crystal temperatures to account for this drift, ensuring perfect phase-matching even at very high pump powers. Grey-tracking is avoided by periodically moving the crystals transverse to the pump beam with a period of  $2\mathrm{s}$ . Finally, 1-nm narrowband interferometric spectral filters ensure a high indistinguishability in the temporal domain. All of these changes enabled us to increase our multimode four-photon count rate 80-fold compared with our previous source[19] and thus reduced the required measurement time to 16 days.

The multiport forms the second main part of the experiment (purple hexagon in Fig. 2a). To ensure high-quality operation of

![](images/daa84bc2fac07ec129338720081583e04e288dad7fa7ad47eb0bd57fd025bef7.jpg)  
Fig. 2 | Experimental details and physical generation principle.

![](images/a14c11f5748fd0363d2717a640415ab27e97afe7ce95e0286294e519852d868c.jpg)

c Multiport transformations

$$
\left| \right. 1 \left. \right\rangle_ {\mathrm {A}} \rightarrow i \left| \right. 1 \left. \right\rangle_ {\mathrm {B}} - \left| \right. + \left. \right\rangle_ {\mathrm {A}}
$$

$$
| 1 \rangle_ {\mathrm {B}} \rightarrow | 1 \rangle_ {\mathrm {C}}
$$

$$
\left| \right. 1 \left. \right\rangle_ {\mathrm {C}} \rightarrow i \left| \right. - 1 \left. \right\rangle_ {\mathrm {C}}
$$

$$
\left| \right. 0 \left. \right\rangle_ {A} \rightarrow i \left| \right. 2 \left. \right\rangle_ {B}
$$

$$
\left. \right.\left| \right. 0 \left. \right\rangle_ {\mathrm {B}} \rightarrow i + \rangle_ {\mathrm {A}} - \left| \right. 0 \left. \right\rangle_ {\mathrm {B}} \left. \right.
$$

$$
| 0 \rangle_ {\mathrm {C}} \rightarrow i | 0 \rangle_ {\mathrm {C}}
$$

$$
\left. \right.\left| \right. - 1 \left. \right\rangle_ {\mathrm {A}} \rightarrow i \left| \right. 3 \left. \right\rangle_ {\mathrm {B}} \left. \right.
$$

$$
| - 1 \rangle_ {\mathrm {B}} \rightarrow | - 1 \rangle_ {\mathrm {C}}
$$

$$
| - 1 \rangle_ {\mathrm {C}} \rightarrow | + \rangle_ {\mathrm {A}} + i | 1 \rangle_ {\mathrm {B}}
$$

a, Experimental details. Two nonlinear periodically poled potassium titanyl phosphate (ppKTP) crystals (NL1 and NL2) are each used to generate a pair of photons entangled in three dimensions of their OAM. A specifically designed telescope system of lenses compensates for Kerr lensing effects between the two crystals. Each crystal is housed in a custom-built oven whose temperature  $(T)$  is automatically adjusted to account for drifts in the optimal phase-matching temperature as a result of high pump powers. Two polarizing beam splitters (PBS) deterministically separate the photon pairs generated in each crystal. Narrowband interference filters (IF) in each arm guarantee a high degree of indistinguishability in the temporal domain. Photons A, B and C enter the multiport (purple hexagon), which consists of a series of nested single-photon and two-photon interferometers. The OAM parity-sorter (green rectangle) interferometrically sorts incoming photons according to their OAM parity (even or odd). A reflection (R) in combination with an  $\ell = +2$  spiral phase-plate (SPP) is used in path A, before photons A and B are coherently recombined at a beam splitter (BS). Finally, a coherent-mode projection (CMP) projects photon A onto the superposition state  $|+ \rangle = |0\rangle + |-1\rangle$ , resulting in a three-dimensional GHZ-entangled state between photons B, C and D. DM, dichroic mirror; Det, detector; Lc, collimation lens; Lf, focusing lens; SHG, second-harmonic generation. b, Physical generation principle of a three-dimensional GHZ state. The nine possible joint probability amplitudes resulting from the tensor product of two pairs of three-dimensionally entangled photons  $(3 \times 3 = 9)$  are represented by the red, green and blue lines. In step 1, the OAM parity-sorter inserted in paths B and C prevents a four-fold detection event between even and odd terms. In step 2, the multiport further eliminates two cross-connections between two additional probability amplitudes. Finally, only three joint probability amplitudes corresponding to a three-dimensional GHZ-entangled state remain. c, Detailed mode transformations performed by the multiport on photons entering and leaving in paths A, B and C.

the multiport, all single and two-photon nested interferometers contained within it need to be interferometrically stable and have a high degree of spatial overlap to obtain multimode interference

with a high visibility. To ensure single-photon interference stability, the parity-sorter is actively stabilized with a piezo actuator. This also enables us to continuously switch its operation between a mode-independent 50/50 beam splitter and a mode-parity-sorter. The high spatial and temporal overlap of the multi-port interferometers is demonstrated experimentally with different measurements shown in Fig. 3. Multimode HOM interference from a single crystal is demonstrated in Fig. 3a, where a photon pair from NL1 in modes  $|0,0\rangle_{\mathrm{A,B}}$  results in the post-selected entangled state  $1 / \sqrt{2} (|0,2\rangle_{\mathrm{A,B}} - | - 2,0\rangle_{\mathrm{A,B}})$  after the beam splitter. As the path length difference before the beam splitter is varied, this state goes from being in a coherent superposition to a mixture of modes. At zero path length difference, the presence of high-visibility  $(97\pm 3.3\%)$  HOM interference between two-photon mode superpositions  $|0\rangle_{\mathrm{A}} + |2\rangle_{\mathrm{A}}$  and  $|0\rangle_{\mathrm{B}} + | - 2\rangle_{\mathrm{B}}$  confirms the presence of a coherent superposition. Single-mode  $(\ell = 0)$  HOM interference from two crystals is demonstrated by tuning the piezo actuator such that the parity-sorter is acting as a mode-independent beam splitter. The joint spectral amplitude of the two photon pairs introduces an additional element of distinguishability and leads to the observed HOM interference visibility of  $(88\pm 14)\%$  (see Fig. 3b and Supplementary Information for details). Of high importance to the GHZ state creation is the multimodal HOM interference in the OAM degree of freedom between two crystals, as displayed in Fig. 3c. Here, we show the suppression of the joint probability amplitude  $|1, - 1\rangle_{\mathrm{AB}}\otimes |-1,1\rangle_{\mathrm{CD}}$  by  $(83.5\pm 2.5)\%$  . This high visibility demonstrates the high indistinguishability between photon pairs created in two different NLs and the coherent operation of the multiport in a multiphoton and multimodal OAM regime.

# Experimental results

We use an entanglement-dimension witness $^{19}$  to verify that our three-photon state is indeed genuinely multipartite entangled in three dimensions. This approach is based on the idea that the overlap of an ideal three-dimensional GHZ state with any state from a lower-dimensional entanglement structure cannot exceed a certain maximum value. If our measured state exceeds this maximum fidelity, it is genuinely multipartite entangled in dimension three. The entanglement structure is defined according to the Schmidt rank vector (SRV) formalism $^{36}$ . Each number in the SRV corresponds to the entanglement dimensionality of one party with respect to the remaining two parties. Thus for the GHZ state, all three bi-partitions  $\{\mathrm{A|BC,B|AC,C|AB}\}$  are three-dimensionally entangled, giving  $\mathrm{SRV} = (3,3,3)$ . The maximum possible fidelity between a  $(3,3,3)$  state  $|\psi \rangle$  and any quantum state  $\chi$  with a smaller dimensionality structure, for example  $\chi \in (3,3,2)$ , is  $F_{\max} = \max_{\chi \in (i,j,k)}\mathrm{Tr}(\chi |\psi \rangle \langle \psi |)\leq 2 / 3$  for all permutations of  $(i,j,k)$  with  $i,j\leq 3$  and  $k\leq 2$ . Thus if the fidelity of our experimentally created state  $\rho$ ,  $F_{\exp} = \mathrm{Tr}(\rho |\psi \rangle \langle \psi |)$ , exceeds this bound  $F_{\max}$ , we have shown that we have indeed created a genuinely  $(3,3,3)$ -dimensionally entangled state.

The absolute values of the measured density matrix elements are depicted in Fig. 4a. The diagonal elements are simple projection measurements in the computational basis. However, each off-diagonal element is reconstructed from 64 consecutive two-dimensional subspace measurements. Hence, a total of 219 measurements are performed with spatial light modulators in combination with single-mode fibres to reconstruct the necessary density matrix elements (see Supplementary Information for details). In total, we observed 1,652 simultaneous four-photon 'click' events in 378 hours. Owing to the long measurement time and high powers used, we subtract accidental four-photon clicks between detectors (see Supplementary Information for details). From these data, we calculate the experimental fidelity to be  $F_{\mathrm{exp}} = (75.2 \pm 2.88)\%$ , which certifies with three standard deviations that the observed state is indeed genuinely three-dimensional and three-photon entangled. The error was calculated using a Monte Carlo simulation of the

![](images/228b0b7a46508064e0384916a419289790c569822421825cef355ffa68f05b08.jpg)  
a

![](images/79185c85f55d67445bec8d1859e52b592b52510493c17b28341754d666d7cfaf.jpg)

![](images/12d8b18efc4480fb5be8f73e69637f03ce1d357fcef5b99d9330f5cad67f3abd.jpg)  
b

![](images/bec01c25f01064f6433c36ed7ff832fb4b183c0fa39f5ac539e50d6b575af61f.jpg)

![](images/dc7e0432ad7f2f342cf1a1fa6c974f793732f797d0c81d1388965acc93e3fb64.jpg)  
c  
Fig. 3 | Multimode HOM interference in the multiport. a, Multimode HOM effect from a single crystal. The first interferometer is formed by PBS1 and the beam splitter. Here, the OAM parity-sorter transmits even OAM modes  $(|0\rangle_{\mathrm{B}})$ . The left interferometer arm includes a spiral phase-plate that transforms the state  $|0\rangle_{\mathrm{A}} \rightarrow |2\rangle_{\mathrm{A}}$ . To erase the 'which path' information, a coherent superposition of OAM modes is measured at detectors A and B (see inset). The observed HOM visibility is  $(97.9 \pm 3.3)\%$ . b, Four-photon HOM effect from two crystals for the Gaussian mode only. This two-photon interferometer is formed by the dichroic mirror and the OAM parity-sorter. The piezo actuator (P) is set such that the OAM parity-sorter acts as a mode-independent beam splitter. Thus, HOM interference for the  $\ell = 0$  mode can be observed. The presented visibility  $(88 \pm 14)\%$  shows a high degree of temporal and spatial indistinguishability between the two created photon pairs. c, Four-photon HOM effect from two crystals for the  $\ell$  modes  $+1$  and  $-1$ . All nested single- and two-photon interferometers and both crystals are involved in this measurement. Higher-order OAM modes  $(\ell = \pm 1)$  created in two different crystals interfere through the HOM effect. The observed HOM visibility of  $(83.5 \pm 2.5)\%$  demonstrates the quality of the developed photon source and multiport. All experimental data curves are fitted with an assumed Gaussian spectrum. Error bars indicate Poissonian noise in the photon-counting rate.

![](images/2369fcd637186e78ad095074ebb83116532e080384d9a7b7d6fc8d840a88aae4.jpg)

![](images/63365e7285c27af5d9ab9eba5c51996d9569f751547f394beda9799f9d84a85b.jpg)  
Fig. 4 | Experimental measurements and simultaneous GHZ violations in two-dimensional state subspaces. Measured density matrix elements for calculating the fidelity  $F_{\mathrm{exp}} = 75.2\%$  are depicted (elements not measured in the experiment are crossed out). This verifies genuine multipartite entanglement in (3, 3, 3) dimensions with three standard deviations. The non-flat distribution of the diagonal elements is expected from the initial states of the two entangled photon pairs. Furthermore,  $87.8\%$  of the detected counts of the diagonal elements are in the expected elements. The average coherence of the measured state is approximately  $81.7\%$ . Perfect coherence is indicated by empty bars. b-d, Three simultaneous GHZ violations in two-dimensional state subspaces. Experimental results for joint Pauli measurements XXX, YXY, YXY and XYY performed on each two-dimensional subspace of our three-dimensional state are shown. For a relative minus sign in the quantum state, we theoretically expect  $-1$  for the XXX measurement and  $+1$  for all other measurements, as shown in b and c. Without a relative phase (d) we expect a sign flip in the measurement results. Calculating the Mermin operator  $\mathcal{M}$  yields  $\mathcal{M}_{\mathrm{b}} = -2.47 \pm 0.33 (\mathbf{b})$ ,  $\mathcal{M}_{\mathrm{c}} = -3.37 \pm 0.32 (\mathbf{c})$  and  $\mathcal{M}_{\mathrm{d}} = 2.94 \pm 0.34 (\mathbf{d})$ , which are all above the local-realistic bound of 2. Errors are calculated using a Monte Carlo simulation with an underlying Poissonian distribution for the photon-counting rate.

![](images/a198d6b08823fe1473ff5f688bcf63ec610b1e282837289fd2e55418c4c14342.jpg)

![](images/4eed04d28d31765e441d9fff5fdab916a96a72a17857c3dac1d71384e8d99cb7.jpg)

![](images/e83964ba2fda0096a24173e4a5fb49fdc505c98040a178ce234f1ad7057e4832.jpg)

experiment with Poissonian counting statistics. One could, in principle, reduce the number of measurements through the use of more efficient witnesses that use measurements in mutually unbiased bases<sup>37</sup>. Unfortunately, these are difficult to realize in a lossless manner for complex photonic spatial modes.

In contrast to lower-dimensional entanglement structures, a genuinely (3, 3, 3)-entangled GHZ state enables us to simultaneously test for three different GHZ violations in every two-dimensional subspace of our state. To test for such violations, one measures the Mermin operator  $\langle \mathcal{M}\rangle = \langle \mathrm{XXX}\rangle -\langle \mathrm{YYX}\rangle -\langle \mathrm{YXY}\rangle -\langle \mathrm{XYY}\rangle^7$  whose value according to local-realistic theories is limited to  $|\mathcal{M}| = 2$ . Figure 4b-d shows the results of such tests performed in every two-dimensional subspace. We obtain values of the Mermin operators  $\mathcal{M}_{\mathrm{b}} = -2.47\pm 0.33$ ,  $\mathcal{M}_{\mathrm{c}} = -3.37\pm 0.32$  and  $\mathcal{M}_{\mathrm{d}} = 2.94\pm 0.34$ , which are all above the local-realistic bound of 2 (the subscripts refer to panels b, c and d in Fig. 4). Additionally, the experimental results show that the relative phases of our state are precisely as expected according to equation (3). One should note, however, that our test of local realism is not free of loopholes such as the fair-sampling assumption, as we use probabilistic mode filters and accidental subtraction to measure our state. The use of multi-outcome OAM measurement techniques[38] would allow one to address these limitations in future experiments.

In addition to two-dimensional GHZ violations, it is interesting to see how our experimentally generated state would perform in a truly high-dimensional and multisetting test of local realism<sup>39</sup>. Here, by inferring the quality of our generated state from our (limited) witness measurements, we discuss whether such a high-dimensional violation of local realism is possible in principle. The three criteria that determine the quality of our state are white noise, average coherence between the three probability amplitudes and weighting of the individual diagonal elements. From our experimental data,

we see that the ratio of the observed versus expected magnitudes of the off-diagonal elements of our state is  $81.7\%$  on average, which therefore quantifies the average coherence. Additionally,  $87.8\%$  of the detected counts in the diagonal elements are in the expected elements, indicating that the amount of white noise present in our state is  $12.2\%$ . We can then theoretically construct a density matrix  $\rho_{\mathrm{p}}$  which contains these three parameters, and calculate the expectation value for the generalized Mermin operator  $\mathcal{O}$  (ref. $^{39}$ ), which yields a result of  $\langle \mathcal{O} \rangle_{\rho_{\mathrm{p}}} = 6.26 \pm 0.25$  (details in the Supplementary Information). The limit for local-realistic theories is 6. It is therefore realistic that such an experiment can be carried out with our experimentally generated state. Of course, such a test would benefit from improvements in the four-photon counting rate through techniques such as custom periodically poled KTP crystals specifically designed to minimize spectral distinguishability $^{40}$ , used in combination with high-efficiency detectors. This would also allow one to circumvent accidental subtraction.

# Conclusion

In conclusion, we have shown an experimental realization of a three-particle GHZ state entangled in three dimensions. Our physical system comprises three photons entangled in their OAM. Remarkably, our experimental method for generating this state was found through the use of a computer algorithm called Melvin. The generation of this state required two technological milestones: a high-brightness, multimode four-photon source showing an improvement of two orders of magnitude in photon counting rates over state-of-the-art methods, and a new type of multiport that coherently operates in a 27-dimensional multimode space. Using our entangled state, we have demonstrated three simultaneous violations of the GHZ contradiction and showed the feasibility of a truly three-dimensional and multisetting GHZ test of local realism

with our developed technology. The concepts presented here show a clear pathway for enhancing future quantum technologies beyond the qubit regime. On the applications front, this work opens new opportunities for experimentally investigating multiparty quantum communication protocols in higher dimensions, which potentially offer increased information capacity and greater resistance to noise $^{41,42}$ . We expect that, in parallel, such states open an experimental pathway for reducing the complexity of quantum computing algorithms through the use of high-dimensional encoding $^{43}$ .

# Data availability

The data that support the plots within this paper and other findings of this study are available from the corresponding authors upon reasonable request.

Received: 11 October 2017; Accepted: 21 August 2018

Published online: 29 October 2018

# References

1. Shor, P. W. Fault-tolerant quantum computation. In Proc. 37th Conf. Foundations of Computer Science 56-65 (IEEE, 1996).  
2. Hillary, M., Bužek, V. & Berthiaume, A. Quantum secret sharing. Phys. Rev. A 59, 1829-1834 (1999).  
3. Greenberger, D. M., Horne, M. A. & Zeilinger, A. in Bell's Theorem, Quantum Theory and Conceptions of the Universe (ed. Kafatos, M.) 69-72 (Springer, The Netherlands, 1989).  
4. Greenberger, D. M., Horne, M. A., Shimony, A. & Zeilinger, A. Bell's theorem without inequalities. Am. J. Phys. 58, 1131-1143 (1990).  
5. Krenn, M., Malik, M., Fickler, R., Lapkiewicz, R. & Zeilinger, A. Automated search for new quantum experiments. Phys. Rev. Lett. 116, 090405 (2016).  
6. Einstein, A., Podolsky, B. & Rosen, N. Can quantum-mechanical description of physical reality be considered complete? Phys. Rev. 47, 777-780 (1935).  
7. Mermin, N. D. Extreme quantum entanglement in a superposition of macroscopically distinct states. Phys. Rev. Lett. 65, 1838-1840 (1990).  
8. Monz, T. et al. 14-qubit entanglement: creation and coherence. Phys. Rev. Lett. 106, 130506 (2011).  
9. Bouwmeester, D., Pan, J.-W., Daniell, M., Weinfurter, H. & Zeilinger, A. Observation of three-photon Greenberger-Horne-Zeilinger entanglement. Phys. Rev. Lett. 82, 1345-1349 (1999).  
10. Pan, J.-W., Bouwmeester, D., Daniell, M., Weinfurter, H. & Zeilinger, A. Experimental test of quantum nonlocality in three-photon Greenberger-Horne-Zeilinger entanglement. Nature 403, 515 (2000).  
11. Wang, X.-L. et al. Experimental ten-photon entanglement. Phys. Rev. Lett. 117, 210502 (2016).  
12. Kelly, J. et al. State preservation by repetitive error detection in a superconducting quantum circuit. Nature 519, 66-69 (2015).  
13. Song, C. et al. 10-qubit entanglement and parallel logic operations with a superconducting circuit. Phys. Rev. Lett. 119, 180511 (2017).  
14. Pan, J.-W. et al. Multiphoton entanglement and interferometry. Rev. Mod. Phys. 84, 777-838 (2012).  
15. Ryu, J., Lee, C., Zukowski, M. & Lee, J. Greenberger-Horne-Zeilinger theorem for  $N$  quids. Phys. Rev. A 88, 042101 (2013).  
16. Ryu, J. et al. Multisetting Greenberger-Horne-Zeilinger theorem. Phys. Rev. A 89, 024103 (2014).  
17. Lawrence, J. Rotational covariance and Greenberger-Horne-Zeilinger theorems for three or more particles of any dimension. Phys. Rev. A 89, 012105 (2014).  
18. Tang, W., Yu, S. & Oh, C. Multisetting Greenberger-Horne-Zeilinger paradoxes. Phys. Rev. A 95, 012131 (2017).  
19. Malik, M. et al. Multi-photon entanglement in high dimensions. Nat. Photon. 10, 248-252 (2016).  
20. Hiesmayr, B., De Dood, M. & Löffler, W. Observation of four-photon orbital angular momentum entanglement. Phys. Rev. Lett. 116, 073601 (2016).  
21. Zhang, Y. et al. Simultaneous entanglement swapping of multiple orbital angular momentum states of light. Nat. Commun. 8, 632 (2017).  
22. Krenn, M., Gu, X. & Zeilinger, A. Quantum experiments and graphs: multiparty states as coherent superpositions of perfect matchings. Phys. Rev. Lett. 119, 240403 (2017).  
23. Gu, X., Erhard, M., Zeilinger, A. & Krenn, M. Quantum experiments and graphs II: computation and state generation with probabilistic sources and linear optics. Preprint at https://arxiv.org/abs/1803.10736 (2018).  
24. Schlederer, F., Krenn, M., Fickler, R., Malik, M. & Zeilinger, A. Cyclic transformation of orbital angular momentum modes. New J. Phys. 18, 043019 (2016).

25. Babazadeh, A. et al. High-dimensional single-photon quantum gates: concepts and experiments. Phys. Rev. Lett. 119, 180510 (2017).  
26. Krenn, M., Hochrainer, A., Lahiri, M. & Zeilinger, A. Entanglement by path identity. Phys. Rev. Lett. 118, 080401 (2017).  
27. Allen, L., Beijersbergen, M. W., Spreeuw, R. & Woerdman, J. Orbital angular momentum of light and the transformation of Laguerre-Gaussian laser modes. Phys. Rev. A 45, 8185 (1992).  
28. Mair, A., Vaziri, A., Weihs, G. & Zeilinger, A. Entanglement of the orbital angular momentum states of photons. Nature 412, 313-316 (2001).  
29. Yao, A. M. & Padgett, M. J. Orbital angular momentum: origins, behavior and applications. Adv. Opt. Photonics 3, 161-204 (2011).  
30. Krenn, M., Malik, M., Erhard, M. & Zeilinger, A. Orbital angular momentum of photons and the entanglement of Laguerre-Gaussian modes. Philos. Trans. R. Soc. A 375, 20150442 (2017).  
31. Hong, C., Ou, Z.-Y. & Mandel, L. Measurement of subpicosecond time intervals between two photons by interference. Phys. Rev. Lett. 59, 2044-2046 (1987).  
32. Zhang, Y. et al. Engineering two-photon high-dimensional states through quantum interference. Sci. Adv. 2, e1501165 (2016).  
33. Miatto, F. et al. Bounds and optimisation of orbital angular momentum bandwidths within parametric downconversion systems. Eur. Phys. J. D 66, 1-6 (2012).  
34. Leach, J., Padgett, M. J., Barnett, S. M., Franke-Arnold, S. & Courtial, J. Measuring the orbital angular momentum of a single photon. Phys. Rev. Lett. 88, 257901 (2002).  
35. Erhard, M., Malik, M. & Zeilinger, A. A quantum router for high-dimensional entanglement. Quantum Sci. Technol. 2, 014001 (2017).  
36. Huber, M. & de Vicente, J. I. Structure of multidimensional entanglement in multipartite systems. Phys. Rev. Lett. 110, 030501 (2013).  
37. Bavaresco, J. et al. Measurements in two bases are sufficient for certifying high-dimensional entanglement. Nat. Phys. 14, 1032-1037 (2018).  
38. Mirhosseini, M., Malik, M., Shi, Z. & Boyd, R. W. Efficient separation of the orbital angular momentum eigenstates of light. Nat. Commun. 4, 2781 (2013).  
39. Lawrence, J. Mermin inequalities for perfect correlations in many-qutrit systems. Phys. Rev. A 95, 042123 (2017).  
40. Graffiti, F., Kundys, D., Reid, D. T., Branczyk, A. M. & Fedrizzi, A. Pure down-conversion photons through sub-coherence-length domain engineering. Quantum Sci. Technol. 2, 035001 (2017).  
41. Barreiro, J. T., Wei, T.-C. & Kwiat, P. G. Beating the channel capacity limit for linear photonic superdense coding. Nat. Phys. 4, 282-286 (2008).  
42. Sheridan, L. & Scarani, V. Security proof for quantum key distribution using qudit systems. Phys. Rev. A 82, 030301 (2010).  
43. Bocharov, A., Roetteler, M. & Svore, K. M. Factoring with qutrits: Shor's algorithm on ternary and metaplectic quantum architectures. Phys. Rev. A 96, 012306 (2017).

# Acknowledgements

We thank J. Lawrence, M. Huber, C. Brukner, A. Hochrainer, R. Fickler, T. Scheidl, F. Steinlechner and X. Gu for fruitful discussions. This work was supported by the Austrian Academy of Sciences (ÖAW), by the European Research Council (SIQS grant no. 600645 EU-FP7-ICT) and the Austrian Science Fund (FWF) with SFB F40 (FOQUS) and FWF project CoQuS no. W1210-N16. M.M. acknowledges support from the European Commission through a Marie Curie fellowship (OAMGHZ) and the joint Czech-Austrian project MultiQUEST (FWF I3053-N27), and the QuantERA ERA-NET Co-fund (FWF I3553-N36).

# Author contributions

The computer algorithm Melvin inspired an initial practical solution for the experiment. M.E. and M.M. performed the experiment. All authors analysed the data, discussed the results and wrote the manuscript. A.Z. initiated the research and supervised the project.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s41566-018-0257-6.

Reprints and permissions information is available at www.nature.com/reprints.

Correspondence and requests for materials should be addressed to M.E. or A.Z.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2018