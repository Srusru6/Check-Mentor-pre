ARTICLE

DOI: 10.1038/s41467-017-01058-6

OPEN

# Entanglement of photons in their dual wave-particle nature

Adil S. Rab<sup>1</sup>, Emanuele Polino<sup>1</sup>, Zhong-Xiao Man<sup>2</sup>, Nguyen Ba An<sup>3</sup>, Yun-Jie Xia<sup>2</sup>, Nicolò Spagnolo<sup>1</sup>, Rosario Lo Franco<sup>4,5</sup> & Fabio Sciarrino<sup>1</sup>

Wave-particle duality is the most fundamental description of the nature of a quantum object, which behaves like a classical particle or wave depending on the measurement apparatus. On the other hand, entanglement represents nonclassical correlations of composite quantum systems, being also a key resource in quantum information. Despite the very recent observations of wave-particle superposition and entanglement, whether these two fundamental traits of quantum mechanics can emerge simultaneously remains an open issue. Here we introduce and experimentally realize a scheme that deterministically generates entanglement between the wave and particle states of two photons. The elementary tool allowing this achievement is a scalable single-photon setup which can be in principle extended to generate multiphoton wave-particle entanglement. Our study reveals that photons can be entangled in their dual wave-particle behavior and opens the way to potential applications in quantum information protocols exploiting the wave-particle degrees of freedom to encode qubits.

Quantum mechanics is one of the most successful theories in describing atomic-scale systems albeit its properties remain bizarre and counterintuitive from a classical perspective. A paradigmatic example is the wave-particle duality of a single-quantum system, which can behave like both particle and wave to fit the demands of the experiment's configuration<sup>1</sup>. This double nature is well reflected by the superposition principle and evidenced for light by Young-type double-slit experiments<sup>2, 3</sup>, where single photons from a given slit can be detected (particle-like behavior) and interference fringes observed (wave-like behavior) on a screen behind the slits. A double-slit experiment can be simulated by sending photons into a Mach-Zehnder interferometer (MZI) via a semitransparent mirror (beam-splitter)<sup>2, 3</sup>. A representative experiment with MZI, also performed with a single atom<sup>4</sup>, is the Wheeler's delayed-choice (WDC) experiment<sup>1, 5</sup>, where one can choose to observe the particle or wave character of the quantum object after it has entered the interferometer. These experiments rule out the existence of some extra information hidden in the initial state telling the quantum object which character to exhibit before reaching the measurement apparatus. Very recent quantum WDC experiments, using quantum detecting devices and requiring ancilla photons or post-selection, have then shown that wave and particle behaviors of a single photon can coexist simultaneously, with a continuous morphing between them<sup>6-13</sup>. Regarding the latter property, it is worth to mention that the classical concepts of wave and particle need a suitable interpretation in the context of quantum detection. Namely, the wave or particle nature of a photon is operationally defined as the state of the photon, respectively, capable or incapable to produce interference<sup>6</sup>. Along this work, we always retain this operational meaning in terms of two suitably defined quantum states.

When applying the superposition principle to composite systems, another peculiar quantum feature arises, namely the entanglement among degrees of freedom of the constituent particles (e.g., spins, energies, spatial modes, polarizations) $^{14, 15}$ .

Entanglement gathers fundamental quantum correlations among particle properties, which are at the core of nonlocality $^{16-20}$  and exploited as essential ingredient for developing quantum technologies $^{21-23}$ . Superposition principle and entanglement have been amply debated within classical-quantum border, particularly whether macroscopically distinguishable states (i.e., distinct quasiclassical wave packets) of a quantum system could be prepared in superposition states $^{24}$ . While superpositions of coherent states of a single quantum system (also known as "cat states" from the well-known Schrödinger's epitome) have been observed for optical or microwave fields starting from two decades ago $^{24-28}$ , the creation of entangled coherent states of two separated subsystems has remained a demanding challenge, settled only very recently by using superconducting microwave cavities and Josephson junction-based artificial atoms $^{29}$ . An analogous situation exists in the context of wave-particle duality where, albeit wave-particle superpositions of a photon have been reported $^{6-12}$ , entangled states of photons correlated in their wave-particle degrees of freedom are still unknown.

In this work we experimentally demonstrate that wave-particle entanglement of two photons is achievable deterministically. We reach this goal by introducing and doubling a scalable all-optical scheme which is capable to generate, in an unconditional manner, controllable single-photon wave-particle superposition states. Parallel use of this basic toolbox then allows the creation of multiphoton wave-particle entangled states.

# Results

Single-photon toolbox. The theoretical sketch of the wave-particle scheme for the single photon is displayed in Fig. 1. A photon is initially prepared in a polarization state  $|\psi_0\rangle = \cos \alpha |\mathrm{V}\rangle +\sin \alpha |\mathrm{H}\rangle$ , where  $|\mathrm{V}\rangle$  and  $|\mathrm{H}\rangle$  are the vertical and horizontal polarization states and  $\alpha$  is adjustable by a preparation half-wave plate (not shown in the figure). After crossing the preparation part of the setup of Fig. 1 (see Supplementary

![](images/9415563dd875a8a8534cbace1cd1f47e16177c4412019c9bff63d9bd7ef90686.jpg)  
Fig. 1 Conceptual figure of the wave-particle toolbox. A single photon is coherently separated in two spatial modes by means of a polarizing beam-splitter (PBS) according to its initial polarization state (in). A half-wave plate (HWP) is placed after the PBS to obtain equal polarizations between the two modes. One mode is injected in a complete Mach-Zehnder interferometer (MZI) with phase  $\phi_{1}$ , thus exhibiting wave-like behavior. The second mode is injected in a Mach-Zehnder interferometer lacking the second beam-splitter, thus exhibiting particle-like behavior (no dependence on  $\phi_{2}$ ). The output modes are recombined on two symmetric beam-splitters ( $BS_{4}, BS_{5}$ ), which can be removed to change the measurement basis. Detectors ( $D_{1}, D_{2}, D_{3}, D_{4}$ ) are placed on each final path ( $|1\rangle$ ,  $|2\rangle$ ,  $|3\rangle$ ,  $|4\rangle$ )

Notes 1 and 2 and Supplementary Fig. 1 for details), the photon state is

$$
\left| \psi_ {\mathrm {f}} \right\rangle = \cos \alpha | \text {w a v e} \rangle + \sin \alpha | \text {p a r t i c l e} \rangle , \tag {1}
$$

where the states

$$
\left| \text {w a v e} \right\rangle = e ^ {i \phi_ {1} / 2} \left(\cos \frac {\phi_ {1}}{2} | 1 \rangle - i \sin \frac {\phi_ {1}}{2} | 3 \rangle\right), \tag {2}
$$

$$
| \text {p a r t i c l e} \rangle = \frac {1}{\sqrt {2}} (| 2 \rangle + e ^ {i \phi_ {2}} | 4 \rangle),
$$

operationally represent the capacity (|wave>) and incapacity (|particle>) of the photon to produce interference $^{6, 11}$ . In fact, for the |wave> state the probability of detecting the photon in the path  $|n\rangle$  ( $n = 1, 3$ ) depends on the phase  $\phi_1$ : the photon must have traveled along both paths simultaneously (see upper MZI in Fig. 1), revealing its wave behavior. Instead, for the |particle> state the probability to detect the photon in the path  $|n\rangle$  ( $n = 2, 4$ ) is 1/2, regardless of phase  $\phi_2$ : thus, the photon must have crossed only one of the two paths (see lower MZI of Fig. 1), showing its particle behavior. Notice that the scheme is designed in such a way that  $|\mathrm{V}\rangle$  (|H>) leads to the |wave> (|particle>) state.

To verify the coherent wave-particle superposition as a function of the parameter  $\alpha$ , the wave and particle states have to interfere at the detection level. This goal is achieved by exploiting two symmetric beam-splitters where the output paths (modes) are recombined, as illustrated in the detection part of Fig. 1. The probability  $P_{n} = P_{n}(\alpha, \phi_{1}, \phi_{2})$  of detecting the photon along path  $|n\rangle$  ( $n = 1, 2, 3, 4$ ) is now expected to depend on all the involved parameters, namely

$$
P _ {1} = \mathcal {P} _ {\mathrm {c}} + \mathcal {I} _ {\mathrm {c}}, P _ {2} = \mathcal {P} _ {\mathrm {c}} - \mathcal {I} _ {\mathrm {c}}, P _ {3} = \mathcal {P} _ {\mathrm {s}} + \mathcal {I} _ {\mathrm {s}}, P _ {4} = \mathcal {P} _ {\mathrm {s}} - \mathcal {I} _ {\mathrm {s}}, \tag {3}
$$

where

$$
\mathcal {P} _ {\mathrm {c}} = \frac {1}{2} \cos^ {2} \alpha \cos^ {2} \frac {\phi_ {1}}{2} + \frac {1}{4} \sin^ {2} \alpha ,
$$

$$
\mathcal {P} _ {\mathrm {s}} = \frac {1}{2} \cos^ {2} \alpha \sin^ {2} \frac {\phi_ {1}}{2} + \frac {1}{4} \sin^ {2} \alpha , \tag {4}
$$

$$
\mathcal {I} _ {\mathrm {c}} = \frac {1}{2 \sqrt {2}} \sin 2 \alpha \cos^ {2} \frac {\phi_ {1}}{2}, \tag {4}
$$

$$
\mathcal {I} _ {\mathrm {s}} = \frac {1}{2 \sqrt {2}} \sin 2 \alpha \sin \frac {\phi_ {1}}{2} \sin \left(\frac {\phi_ {1}}{2} - \phi_ {2}\right).
$$

We remark that the terms  $\mathcal{I}_{\mathrm{c}}, \mathcal{I}_{\mathrm{s}}$  in the detection probabilities exclusively stem from the interference between the  $|\mathrm{wave}\rangle$  and  $|\mathrm{particle}\rangle$  components appearing in the generated superposition state  $|\psi_{\mathrm{f}}\rangle$  of Eq. (1). This fact is further evidenced by the appearance, in these interference terms, of the factor  $\mathcal{C} = \sin 2\alpha$ , which is the amount of quantum coherence owned by  $|\psi_{\mathrm{f}}\rangle$  in the basis  $\{| \mathrm{wave} \rangle, |\mathrm{particle} \rangle\}$  theoretically quantified according to the standard  $l_{1}$ -norm<sup>30</sup>. On the other hand, the interference terms  $\mathcal{I}_{\mathrm{c}}, \mathcal{I}_{\mathrm{s}}$  are always identically zero (independently of phase values) when the final state of the photon is: (i)  $|\mathrm{wave} \rangle$  ( $\alpha = 0$ ); (ii)  $|\mathrm{particle} \rangle$  ( $\alpha = \pi / 2$ ); (iii) a classical incoherent mixture  $\rho_{\mathrm{f}} = \cos^2 \alpha |\mathrm{wave} \rangle \langle \mathrm{wave}| + \sin^2 \alpha |\mathrm{particle} \rangle \langle \mathrm{particle}|$  (which can be theoretically produced by the same scheme starting from an initial mixed polarization state of the photon).

The experimental single-photon toolbox, realizing the proposed scheme of Fig. 1, is displayed in Fig. 2 (see Methods for more details). The implemented layout presents the advantage of being interferometrically stable, thus not requiring active phase stabilization between the modes. Figure 3 shows the experimental

results for the measured single-photon probabilities  $P_{n}$ . For  $\alpha = 0$ , the photon is vertically polarized and entirely reflected from the PBS to travel along path 1, then split at  $\mathrm{BS}_1$  into two paths, both leading to the same  $\mathrm{BS}_3$  which allows these two paths to interfere with each other before detection. The photon detection probability at each detector  $\mathrm{D}_n$  ( $n = 1, 2, 3, 4$ ) depends on the phase shift  $\phi_1$ :  $P_1(\alpha = 0) = P_2(\alpha = 0) = \frac{1}{2}\cos^2\frac{\phi_1}{2}$ ,  $P_3(\alpha = 0) = P_4(\alpha = 0) = \frac{1}{2}\sin^2\frac{\phi_1}{2}$ , as expected from Eqs. (3) and (4). After many such runs an interference pattern emerges, exhibiting the wave-like nature of the photon. Differently, if initially  $\alpha = \pi/2$ , the photon is horizontally polarized and, as a whole, transmitted by the PBS to path 2, then split at  $\mathrm{BS}_2$  into two paths (leading, respectively, to  $\mathrm{BS}_4$  and  $\mathrm{BS}_5$ ) which do not interfere anywhere. Hence, the phase shift  $\phi_2$  plays no role on the photon detection probability and each detector has an equal chance to click:  $P_1(\alpha = \frac{\pi}{2}) = P_2(\alpha = \frac{\pi}{2}) = P_3(\alpha = \frac{\pi}{2}) = P_4(\alpha = \frac{\pi}{2}) = \frac{1}{4}$ , as predicted by Eqs. (3) and (4), showing particle-like behavior without any interference pattern. Interestingly, for  $0 < \alpha < \pi/2$ , the photon simultaneously behaves like wave and particle. The coherent continuous morphing transition from wave to particle behavior as  $\alpha$  varies from 0 to  $\pi/2$  is clearly seen from Fig. 4a and contrasted with the morphing observed for a mixed incoherent wave-particle state  $\rho_{\mathrm{f}}$  (Fig. 4b). Setting  $\phi_2 = 0$ , the coherence of the generated state is also directly quantified by measuring the expectation value of an observable  $\sigma_x^{1234}$ , defined in the four-dimensional basis of the photon paths  $\{|1\rangle, |2\rangle, |3\rangle, |4\rangle\}$  of the preparation part of the setup as a Pauli matrix  $\sigma_x$  between modes (1, 2) and between modes (3, 4). It is then possible to straightforwardly show that  $\langle \sigma_x^{1234} \rangle = \operatorname{Tr}(\sigma_x^{1234}\rho_{\mathrm{f}}) = 0$  for any incoherent state  $\rho_{\mathrm{f}}$  while  $\sqrt{2}\langle \sigma_x^{1234} \rangle = \sin 2\alpha = C$  for an arbitrary state of the form  $|\psi_{\mathrm{f}}\rangle$  defined in Eq. (1). Insertion of beamsplitters  $\mathrm{BS}_4$  and  $\mathrm{BS}_5$  in the detection part of the setup (corresponding to  $\beta = 22.5^\circ$  in the output wave-plate of Fig. 2) rotates the initial basis  $\{|1\rangle, |2\rangle, |3\rangle, |4\rangle\}$  generating a measurement basis of eigenstates of  $\sigma_x^{1234}$ , whose expectation value is thus obtained in terms of the detection probabilities as  $\langle \sigma_x^{1234} \rangle = P_1 - P_2 + P_3 - P_4$  (see Supplementary Note 2). As shown in Fig. 4c, d, the observed behavior of  $\sqrt{2}\langle \sigma_x^{1234} \rangle$  as a function of  $\alpha$  confirms the theoretical predictions for both coherent  $|\psi_{\mathrm{f}}\rangle$  (Fig. 4c) and mixed (incoherent)  $\rho_{\mathrm{f}}$  wave-particle states (the latter being obtained in the experiment by adding a relative time delay in the interferometer paths larger than the photon coherence time to lose quantum interference, Fig. 4d).

Wave-particle entanglement. The above single-photon scheme constitutes the basic toolbox which can be extended to create a wave-particle entangled state of two photons, as shown in Fig. 2b. Initially, a two-photon polarization maximally entangled state  $|\Psi \rangle_{\mathrm{AB}} = \frac{1}{\sqrt{2}} (|\mathrm{VV}\rangle +|\mathrm{HH}\rangle)$  is prepared (the procedure works in general for arbitrary weights, see Supplementary Note 3). Each photon is then sent to one of two identical wave-particle toolboxes which provide the final state

$$
\left| \Phi \right\rangle_ {\mathrm {A B}} = \frac {1}{\sqrt {2}} \left(\left| \text {w a v e} \right\rangle \left| \text {w a v e} ^ {\prime} \right\rangle + \left| \text {p a r t i c l e} \right\rangle \left| \text {p a r t i c l e} ^ {\prime} \right\rangle\right), \tag {5}
$$

where the single-photon states  $|\mathrm{wave}\rangle$ ,  $|\mathrm{particle}\rangle$ ,  $|\mathrm{wave}'\rangle$ ,  $|\mathrm{particle}'\rangle$  are defined in Eq. (2), with parameters and paths related to the corresponding wave-particle toolbox. Using the standard concurrence<sup>14</sup>  $C$  to quantify the amount of entanglement of this state in the two-photon wave-particle basis, one immediately finds  $C = 1$ . The generated state  $|\Phi\rangle_{\mathrm{AB}}$  is thus a wave-particle maximally entangled state (Bell state) of two photons in separated locations.

![](images/736256038abe0c919e3c98ed17853a1ede871f39a0b1391d9beeb754c734a77e.jpg)

![](images/b49e039c3a1f9d0959cc203c94446b9c2eecdd267d04c64b7ade34335ae5cfa9.jpg)

![](images/37301781bd2cc20f6ff0ce3f9918f3b0483be39a8f48786e74b6b6a041bb7bed.jpg)  
Fig. 2 Experimental setup for wave-particle states. a Overview of the apparatus for the generation of single-photon wave-particle superposition. An heralded single-photon is prepared in an arbitrary linear polarization state through a half-wave plate rotated at an angle  $\alpha /2$  and injected into the wave-particle toolbox. b Overview of the apparatus for the generation of a two-photon wave-particle entangled state. Each photon of a polarization entangled state is injected into an independent wave-particle toolbox to prepare the output state. c Actual implemented wave-particle toolbox, reproducing the action of the scheme shown in Fig. 1. Top subpanel: top view of the scheme, where red and purple lines represent optical paths lying in two vertical planes. Bottom subpanel: 3-d scheme of the apparatus. The interferometer is composed of beam-displacing prisms (BDP), half-wave plates (HWP), and liquid crystal devices (LC), the latter changing the phases  $\phi_{1}$  and  $\phi_{2}$ . The output modes are finally separated by means of a polarizing beam-splitter (PBS). The scheme corresponds to the presence of  $\mathrm{BS}_4$  and  $\mathrm{BS}_5$  in Fig. 1 for  $\beta = 22.5^{\circ}$ , while setting  $\beta = 0$  equals to the absence of  $\mathrm{BS}_4$  and  $\mathrm{BS}_5$ . The same color code for the optical elements (reported in the figure legend) is employed for the top view and for the 3-d view of the apparatus. d Picture of the experimental apparatus. The green frame highlights the wave-particle toolbox

![](images/b9b4f6973314fd71502c545120637d5d924129fe8cc514c5a26519e42d88611e.jpg)

The output two-photon state is measured after the two toolboxes. The results are shown in Fig. 5. Coincidences between the four outputs of each toolbox are measured by varying  $\phi_{1}$  and  $\phi_{1}^{\prime}$ . The first set of measurements (Fig. 5a-d) is performed by setting the angles of the output wave-plates (see Fig. 2c) at  $\{\beta = 0, \beta' = 0\}$ , corresponding to removing both  $\mathrm{BS}_4$  and  $\mathrm{BS}_5$  in Fig. 1 (absence of interference between single-photon wave and particle states). In this case, detectors placed at outputs (1, 3) and  $(1', 3')$  reveal wave-like behavior, while detectors placed at outputs (2, 4) and  $(2', 4')$  evidence a particle-like one. As expected, the two-photon probabilities  $P_{nn'}$  for the particle detectors remain unchanged while varying  $\phi_{1}$  and  $\phi_{1}^{\prime}$ , whereas the  $P_{nn'}$  for the wave detectors show interference fringes. Moreover, no contribution of crossed wave-particle coincidences  $P_{nn'}$  is obtained, due to the form of the entangled state. The second set of measurements (Fig. 5e-h) is performed by setting the angles of the output waveplates at  $\{\beta = 22.5^\circ, \beta' = 22.5^\circ\}$ , corresponding to the presence of  $\mathrm{BS}_4$  and  $\mathrm{BS}_5$  in Fig. 1 (the presence of interference between single-photon wave and particle states). We now observe nonzero contributions across all the probabilities depending on the specific settings of phases  $\phi_{1}$  and  $\phi_{1}^{\prime}$ . The presence of entanglement in the wave-particle behavior is also assessed by measuring the quantity  $\mathcal{E} = P_{22'} - P_{21'}$  as a function of  $\phi_{1}$ , with

fixed  $\phi_1' = \phi_2 = \phi_2' = 0$ . According to the general expressions of the coincidence probabilities (see Supplementary Note 3),  $\mathcal{E}$  is proportional to the concurrence  $C$  and identically zero (independently of phase values) if and only if the wave-particle two-photon state is separable (e.g.,  $|\mathrm{wave}\rangle \otimes |\mathrm{wave}'\rangle$  or a maximal mixture of two-photon wave and particle states). For  $|\Phi\rangle_{\mathrm{AB}}$  of Eq. (5) the theoretical prediction is  $\mathcal{E} = (1/4)\cos^2(\phi_1/2)$ , which is confirmed by the results reported in Fig. 5i, j (within the reduction due to visibility). A further test of the generated wave-particle entanglement is finally performed by the direct measure of the expectation values  $\langle \mathcal{W}\rangle = \operatorname{Tr}(\mathcal{W}\rho)$  of a suitable entanglement witness<sup>31</sup>, defined in the  $(4\times 4)$ -dimensional space of the two-photon paths as

$$
\mathcal {W} = \mathbb {1} - 2 \left[ \sigma_ {x} ^ {1 2 3 4} \otimes \left(\sigma_ {x} ^ {1 2 3 4}\right) ^ {\prime} \right] - \left[ \sigma_ {z} ^ {1 2 3 4} \otimes \left(\sigma_ {z} ^ {1 2 3 4}\right) ^ {\prime} \right], \tag {6}
$$

where  $\mathbb{1}$  is the identity matrix,  $\sigma_x^{1234}$  has been defined previously, and  $\sigma_z^{1234}$  corresponds to applying a  $\sigma_z$  Pauli matrix between modes (1, 2) and between modes (3, 4). The measurement basis of  $\sigma_z^{1234}$  is that of the initial paths  $\{|1\rangle, |2\rangle, |3\rangle, |4\rangle\}$  exiting the preparation part of the single-photon toolbox. It is possible to show that  $\mathrm{Tr}(\mathcal{W}\rho_{\mathrm{s}})\geq 0$  for any two-photon separable state  $\rho_{s}$  of wave-particle states, so that whenever  $\mathrm{Tr}(\mathcal{W}\rho_{\mathrm{e}}) < 0$  the state  $\rho_{\mathrm{e}}$  is

![](images/36e165482668ddc511488ef7451ab9f52b7c6e0edebc3d38830b072b14542a86.jpg)

![](images/5787a6ab696b98fbb83b68ba056d75dfa6b9683dbb6a4adeeb9d41cb60be08e1.jpg)

![](images/0f528e6c4823517a0c3dc6b3b80ba8950693e5ed7858d71bfddd70be3d93d25f.jpg)

![](images/62b2c8c5555c6e4e126b0f5ebb31c06b5eb774ed53bbd96a3f8962e0c2920565.jpg)

![](images/fc04b89f9c8fb1f5cfc83c559d5f28617387c6a90a191e72396805809559e510.jpg)  
Fig. 3 Generation of wave-particle superposition with a single-photon state. a-d Measurements of the output probabilities  $P_{n}$  as a function of the phase  $\phi_{1}$ , for different values of  $\alpha$ . a Wave behavior  $(\alpha = 0)$ . b Particle behavior  $(\alpha = \pi /2)$ . c Coherent wave-particle superposition  $(\alpha = \pi /4)$ . d Incoherent mixture of wave and particle behaviors  $(\alpha = \pi /4)$ . Points: experimental data. Dashed curves: best-fit of the experimental data. Color legend: orange  $(P_{1})$ , green  $(P_{2})$ , purple  $(P_{3})$ , blue  $(P_{4})$ . e-h 3-d plots output probabilities  $P_{n}$  as a function of the phase  $\phi_{1}$  and of the angle  $\alpha$ . Points: experimental data. Surfaces: theoretical expectations. In all plots, error bars are standard deviation due to the Poissonian statistics of single-photon counting

![](images/eef3afed7ccb51d0c9a3fd6b4091d800d6745b0f3eb9f63397eaed1aca133484.jpg)

![](images/feca8f0daf15c1aee2addce25a64b8b407327cc871b041803920fe352c112bf9.jpg)

![](images/ae8c6c89c310285c58d518863b6a932502171a791729c935d3c59a0e0d040717.jpg)

![](images/2b36d2c296140c48aebf69a851943fa72aeb6051f8b820cfcbdf935e5787a7c5.jpg)

![](images/32c6275d798b8fc8ebfb4147361e2b1ffb21cc0d5743690ae135953a02456ef7.jpg)

![](images/a9e664f0087b5b09cb228ca5b120c690bc7cfc1e18d1e9557394cb4243bd72d4.jpg)  
Fig. 4 Evidence of the generation of wave-particle superpositions. a Probabilities  $P_{n}$  as a function of  $\alpha$  in the coherent case and b for an incoherent mixture. Color legend: orange (P1), green (P2), purple (P3), blue (P4). In a black triangles highlighted the position for wave behavior  $(\alpha = 0)$ , black circle for particle behavior  $(\alpha = \pi / 2)$  and black diamonds highlight the position for coherent wave-particle superposition behavior  $(\alpha = \pi / 4)$ . c Coherence measure  $\sqrt{2}\langle\sigma_x^{1234}\rangle$  as a function of  $\alpha$  in the coherent case and d for an incoherent mixture (the latter showing no dependence on  $\alpha$ ). Points: experimental data. Solid curves: theoretical expectations. Error bars are standard deviations due to the Poissonian statistics of single-photon counting

![](images/23d8d2270ace8498f745daff347b0d7f256b1657a97fb03f329c322ee5c1910d.jpg)

entangled in the photons wave-particle behavior (see Supplementary Note 3). The expectation values of  $\mathcal{W}$  measured in the experiment in terms of the 16 coincidence probabilities  $P_{nn'}$ , for the various phases considered in Fig. 5, are:  $\langle \mathcal{W} \rangle = -0.699 \pm 0.041$  ( $\phi_1 = \phi_1' = 0$ );  $\langle \mathcal{W} \rangle = -0.846 \pm 0.045$  ( $\phi_1 = \phi_1' = \pi$ );  $\langle \mathcal{W} \rangle = -0.851 \pm 0.041$  ( $\phi_1 = \pi$ ,  $\phi_1' = 0$ );  $\langle \mathcal{W} \rangle = -0.731 \pm 0.042$  ( $\phi_1 = 0$ ,  $\phi_1' = \pi$ ). These observations altogether

prove the existence of quantum correlations between wave and particle states of two photons in the entangled state  $|\Phi \rangle_{\mathrm{AB}}$

# Discussion

In summary, we have introduced and realized an all-optical scheme to deterministically generate single-photon wave-particle superposition states. This setup has enabled the observation of the

![](images/f6907806885b878722413c62f7ab84b1943d4db6ea07a1adaa921d11bb8be5e4.jpg)

![](images/b3768325d93e414e1e2d05b60bbb66a34da6083483afb19ec811107d5f89c027.jpg)

![](images/97833735542bd0ba3ab84a338fa481e15b32d2ed4739c1ab13ad7fc58eae092d.jpg)

![](images/5fbc74a855daead29532548ee864cf782ece2b954effd1f0373d751f8d15b8d9.jpg)

![](images/74b31cd89933bb20e5826090eeb892b3ae9a8b7e71e06958a610d8443c9e371d.jpg)

![](images/f497179e2bb3bed864f221a32480de0787d0b9c9bce258adf7f1e6f82b85045e.jpg)  
Fig. 5 Generation of wave-particle entangled superposition with a two-photon state. Measurements of the output coincidence probabilities  $P_{nn'}$  to detect one photon in output mode  $n$  of the first toolbox and one in the output mode  $n'$  of the second toolbox, with different phases  $\phi_1$  and  $\phi_1'$  ( $\phi_2 = \phi_2' = 0$ ). a-d,  $P_{nn'}$  measured with  $\{\beta = 0, \beta' = 0\}$ , corresponding to the absence of BS4 and BS5 in Fig. 1. a  $\phi_1 = 0$  and  $\phi_1' = 0$ . b  $\phi_1 = \pi$  and  $\phi_1' = 0$ . c  $\phi_1 = 0$  and  $\phi_1' = \pi$ . d  $\phi_1 = \pi$  and  $\phi_1' = \pi$ . e-h  $P_{nn'}$  measured with  $\{\beta = 22.5^\circ, \beta' = 22.5^\circ\}$ , corresponding to the presence of BS4 and BS5 in Fig. 1. e  $\phi_1 = 0$  and  $\phi_1' = 0$ . f  $\phi_1 = \pi$  and  $\phi_1' = 0$ . g  $\phi_1 = 0$  and  $\phi_1' = \pi$ . h  $\phi_1 = \pi$  and  $\phi_1' = \pi$ . White bars: theoretical predictions. Colored bars: experimental data. Orange bars:  $P_{nn'}$  contributions for detectors Dn and Dn linked to wave-like behavior for both photons (in the absence of BS4 and BS5). Cyan bars:  $P_{nn'}$  contributions for detectors Dn and Dn linked to particle-like behavior for both photons (in the absence of BS4 and BS5). Magenta bars:  $P_{nn'}$  contributions for detectors Dn and Dn linked to wave-like behavior for one photon and particle-like behavior for the other one (in absence of BS4 and BS5). Darker regions in colored bars correspond to 1 σ error interval, due to the Poissonian statistics of two-photon coincidences. i, j, Quantitative verification of wave-particle entanglement. i, P22'(blue) and P21'(green) and j, E = P22' - P21', as a function of  $\phi_1$  for  $\phi_1' = 0$  and  $\{\beta = 22.5^\circ, \beta' = 22.5^\circ\}$ . Error bars are standard deviations due to the Poissonian statistics of two-photon coincidences. Dashed curves: best-fit of the experimental data

![](images/6485ba88d4d8c66c1df81b9938e9eaa9be6160b3a248e0d6663ca727d8e98ea4.jpg)

![](images/6e2e26d7ba220ec246bb5971998de1ca5d775ace27146358188bbccb91492434.jpg)

![](images/f3fc70238c0dfe4daf77b183268f1626104baafed47ff24a2fc96c6ac462ce73.jpg)

![](images/2244ba23817dc63cca446244d5d749a65d11947816ea0c6f62dd4934b3f72f4e.jpg)

simultaneous coexistence of particle and wave character of the photon maintaining all its devices fixed, being the control only on the preparation of the input photon. Specifically, different initial polarization states of the photon, then transformed into which-way (path) states, reveal the wave-to-particle morphing economizing the employed resources compared with previous experiments with delayed choice $^{6-12}$ . The advantageous aspects of the single-photon scheme have then supplied the key for its straightforward doubling, by which we have observed that two photons can be cast in a wave-particle entangled state provided that suitable initial entangled polarization states are injected into the apparatus. We remark that powerful features of the scheme are flexibility and scalability. Indeed, a parallel assembly of  $N$  single-photon wave-particle toolboxes allows the generation of  $N$ -photon wave-particle entangled states. For instance, the GHZ-like state  $|\Phi_N\rangle = \frac{1}{\sqrt{2}}(|\mathrm{wave}_1,\mathrm{wave}_2,\dots,\mathrm{wave}_N\rangle + |\mathrm{particle}_1,\mathrm{particle}_2,\dots,\mathrm{particle}_N\rangle)$  is produced when the GHZ polarization entangled state  $|\Psi_N\rangle = \frac{1}{\sqrt{2}}(|\mathrm{V}_1\mathrm{V}_2\dots\mathrm{V}_N\rangle + |\mathrm{H}_1\mathrm{H}_2\dots\mathrm{H}_N\rangle)$  is used as input state.

$^{2}$ From the viewpoint of the foundations of quantum mechanics, our research brings the complementarity principle for wave-particle duality to a further level. Indeed, it merges this basic trait of quantum mechanics with another peculiar quantum feature such as the entanglement. In fact, besides confirming that a photon can live in a superposition of wave and particle behaviors when observed by quantum detection $^{11}$ , we prove that the manifestation of its dual behavior can intrinsically depend on the dual character of another photon, according to correlations ruled by quantum entanglement. Specifically, the coherent wave-particle behavior of a photon is quantum correlated to the measurement outcome of an apparatus, sensitive to the wave

particle behavior of another photon, placed in a region separated from it. Our work shows that this type of entanglement is possible for composite quantum systems. We finally highlight that the possibility to create and control wave-particle entanglement may also play a role in quantum information scenarios. In particular, it opens the way to design protocols which exploit quantum resources contained in systems of qubits encoded in wave and particle operational states.

# Methods

Experimental wave-particle toolbox. The implementation of the wave-particle toolbox exploits both polarization and path degrees of freedom of the photons. A crucial parameter is to obtain an implemented toolbox presenting high interferometric stability. This is achieved in the experiment by exploiting the scheme of Fig. 2, which presents an intrinsic interferometric stability due to the adoption of calcite crystals as beam-displacing prisms (see Supplementary Note 1). More specifically, all optical paths of the overall interferometer are transmitted by the same beam-displacing prisms and propagate in parallel directions, and are thus affected by the same phase fluctuations. Relative phases  $\phi_{1}$  and  $\phi_{2}$  (Fig. 2) within the interferometer are controlled by two liquid crystal devices, which introduce a tunable relative phase between polarization state  $|\mathrm{H}\rangle$  and  $|\mathrm{V}\rangle$  depending on the applied voltage. The parameter  $\alpha$  of Eq. (1) is set by an input half-wave plate, while the output half-wave plate at the detection stage rotates the measurement basis depending on its angle  $\beta$  ( $\beta = 0^{\circ}$  corresponds to the absence of  $\mathrm{BS}_4$  and  $\mathrm{BS}_5$ , while  $\beta = 22.5^{\circ}$  corresponds to the presence of  $\mathrm{BS}_4$  and  $\mathrm{BS}_5$ ). Both half-wave plates are controlled by a motorized stage. Hence, all the variable optical elements in the setup can be controlled via software.

Acquisition system. The output photons are detected by avalanche photodiode detectors, which are connected to an id800 Time to Digital Converter from ID Quantique that is employed to record the output single counts and two-photon coincidences. The photon source is a parametric down conversion source generating pairs of entangled photons. In the single particle experiment, one of the generated photon is directly detected and acts as a trigger, while the other photon is injected in the wave-particle toolbox. Two-photon coincidences are recorded between the output detectors of the toolbox and the trigger photon. In the two-

particle experiment, the two photons of the entangled pair are separately sent to two independent wave-particle toolboxes. Two-photon coincidences are then recorded between the output detectors of each toolbox. A dedicated LabVIEW routine allows simultaneous control of the optical elements and of the detection apparatus to obtain a fully automatized measurement process.

Data availability. The data sets generated during and/or analyzed during the current study are available from the corresponding author on reasonable request.

Received: 8 March 2017 Accepted: 13 August 2017

Published online: 13 October 2017

# References

1. Wheeler, J. A. & Zurek, W. H. Quantum Theory and Measurement (Princeton University Press, 1984).  
2. Ma, X. S., Kofler, J. & Zeilinger, A. Delayed-choice gedanken experiments and their realizations. Rev. Mod. Phys. 88, 015005 (2016).  
3. Walborn, S. P., Terra Cunha, M. O., Pádua, S. & Monken, C. H. Double-slit quantum eraser. Phys. Rev. A 65, 033818 (2002).  
4. Manning, A. G., Khakimov, R. I., Dall, R. G. & Truscott, A. G. Wheeler's delayed-choice gedanken experiment with a single atom. Nat. Phys. 11, 539-542 (2015).  
5. Jacques, V. et al. Experimental realization of Wheeler's delayed-choice gedanken experiment. Science 315, 966-968 (2007).  
6. Ionicioiu, R. & Terno, D. R. Proposal for a quantum delayed-choice experiment. Phys. Rev. Lett. 107, 230406 (2011).  
7. Roy, S., Shukla, A. & Mahesh, T. S. NMR implementation of a quantum delayed-choice experiment. Phys. Rev. A 85, 022109 (2012).  
8. Auccaise, R. et al. Experimental analysis of the quantum complementarity principle. Phys. Rev. A 85, 032121 (2012).  
9. Peruzzo, A., Shadbolt, P. J., Brunner, N., Popescu, S. & O'Brien, J. L. A quantum delayed choice experiment. Science 338, 634-637 (2012).  
10. Kaiser, F., Coudreau, T., Milman, P., Ostrowsky, D. B. & Tanzilli, S. Entanglement-enabled delayed choice experiment. Science 338, 637-640 (2012).  
11. Tang, J. S. et al. Realization of quantum Wheeler's delayed choice experiment. Nat. Photon. 6, 600-604 (2012).  
12. Shadbolt, P., Mathews, J. C. F., Laing, A. & O'Brien, J. L. Testing foundations of quantum mechanics with photons. Nat. Phys. 10, 278-286 (2014).  
13. Ma, X.-S. et al. Quantum erasure with causally disconnected choice. Proc. Natl Acad. Sci. 110, 1221-1226 (2013).  
14. Horodecki, R., Horodecki, P., Horodecki, M. & Horodecki, K. Quantum entanglement. Rev. Mod. Phys. 81, 865-942 (2009).  
15. Lo Franco, R. & Compagno, G. Quantum entanglement of identical particles by standard information-theoretic notions. Sci. Rep. 6, 20603 (2016).  
16. Brunner, N., Cavalcanti, D., Pironio, S., Scarani, V. & Wehner, S. Bell nonlocality. Rev. Mod. Phys. 86, 419-478 (2014).  
17. Hensen, B. et al. Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres. Nature 526, 682-686 (2015).  
18. Giustina, M. et al. Significant-loophole-free test of bell's theorem with entangled photons. Phys. Rev. Lett. 115, 250401 (2015).  
19. Shalm, L. K. et al. Strong loophole-free test of local realism. Phys. Rev. Lett. 115, 250402 (2015).  
20. Handsteiner, J. et al. Cosmic bell test: measurement settings from milky way stars. Phys. Rev. Lett. 118, 060401 (2017).  
21. Vedral, V. Quantum entanglement. Nat. Phys. 10, 256-258 (2014).  
22. Ladd, T. D. et al. Quantum computers. Nature 464, 45-53 (2010).  
23. Wang, X.-L. et al. Experimental ten-photon entanglement. Phys. Rev. Lett. 117, 210502 (2016).  
24. Haroche, S. Nobel lecture: controlling photons in a box and exploring the quantum to classical boundary. Rev. Mod. Phys. 85, 1083-1102 (2013).

25. Brune, M. et al. Observing the progressive decoherence of the "meter" in a quantum measurement. Phys. Rev. Lett. 77, 4887-4890 (1996).  
26. Ourjountsev, A., Jeong, H., Tualle-Brouri, R. & Grangier, P. Generation of optical 'Schrodinger cats' from photon number states. Nature 448, 784-786 (2007).  
27. Deleglise, S. et al. Reconstruction of non-classical cavity field states with snapshots of their decoherence. Nature 455, 510-514 (2008).  
28. Vlastakis, B. et al. Deterministically encoding quantum information using 100-photon Schrödinger cat states. Science 342, 607-610 (2013).  
29. Wang, C. et al. A Schrödinger cat living in two boxes. Science 352, 1087-1091 (2016).  
30. Streltsov, A., Adesso, G. & Plenio, M. B. Quantum Coherence as a Resource. Preprint at http://arxiv.org/abs/1609.02439 (2016).  
31. Gühne, O. & Toth, G. Entanglement detection. Phys. Rep. 474, 1-75 (2009).

# Acknowledgements

This work was supported by the ERC-Starting Grant 3D-QUEST (3D-Quantum Integrated Optical Simulation; grant agreement no. 307783, http://www.3dquest.eu) and by the Marie Curie Initial Training Network PICQUE (Photonic Integrated Compound Quantum Encoding, grant agreement no. 608062, funding Program: FP7-PEOPLE-2013-ITN, http://www.picque.eu). In this work Z.-X.M. and Y.-J.X. are supported by the National Natural Science Foundation of China under Grant Nos. 11574178 and 61675115, Shandong Provincial Natural Science Foundation, China under Grant No. ZR2016JL005, while N.B.A. is funded by the Vietnam National Foundation for Science and Technology Development (NAFOSTED) under project no. 103.01-2017.08.

# Author contributions

Z.-X.M., N.B.A., Y.-J.X. and R.L.F. devised the theoretical proposal. A.S.R., E.P., N.S. and F.S. designed and performed the experiment. R.L.F. and F.S. coordinated the project. All the authors discussed the results and contributed to the preparation of the manuscript.

# Additional information

Supplementary Information accompanies this paper at 10.1038/s41467-017-01058-6.

Competing interests: The authors declare no competing financial interests.

Reprints and permission information is available online at http://npg.nature.com/reprintsandpermissions/

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/dd022c9058641d2db6caa8f507bebbf263d420127242df5623ddf9d2e800a2a4.jpg)

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing,

adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2017