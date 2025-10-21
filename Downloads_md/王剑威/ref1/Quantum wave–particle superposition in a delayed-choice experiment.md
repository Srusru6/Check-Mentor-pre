# Quantum wave-particle superposition in a delayed-choice experiment

Kai Wang, Qian Xu, Shining Zhu and Xiao-song Ma

Wave-particle duality epitomizes the counterintuitive character of quantum physics. A striking illustration is the quantum delayed-choice experiment, which is based on Wheeler's classic delayed-choice gedanken experiment, but with the addition of a quantum-controlled device enabling wave-to-particle transitions. Here, we realize a quantum delayed-choice experiment in which we control the wave and the particle states of photons and particularly the phase between them, thus directly establishing the created quantum nature of the wave-particle. We generate three-photon entangled states and inject one photon into a Mach-Zehnder interferometer embedded in a 186-m-long two-photon Hong-Ou-Mandel interferometer. The third photon is sent 141 m away from the interferometers and remotely prepares a two-photon quantum gate according to independent active choices under Einstein locality conditions. We realize transitions between wave and particle states in both classical and quantum scenarios, and therefore tests of the complementarity principle that go fundamentally beyond earlier implementations.

Quantum mechanics predicts effects that are in conflict with our everyday perceptions of nature. This is no better illustrated than in the wave-particle duality, where a single quantum system can simultaneously exhibit distinct and mutually exclusive features of a particle and a wave, respectively<sup>1</sup>. Hidden-variable theory was proposed to reconcile this conflict between quantum and classical physics. To rule out certain hidden variable theory, Wheeler proposed the so-called delayed-choice gedanken experiment to exclude the possibility that input photons can 'know' the settings of the experiment and behave accordingly<sup>2,3</sup>. The basic concept of Wheeler's delayed-choice (WDC) experiment is shown in Fig. 1a. Single photons are injected into a Mach-Zehnder interferometer (MZI) consisting of two beamsplitters (BS1 and BS2), a phase shifter  $(\varphi)$  and mirrors. The choice of whether or not to insert BS2 into the MZI is made by an external observer, a quantum random number generator (QRNG) for example, and is delayed until after the input single photons pass through BS1 and hence enter into the MZI. The choice of inserting BS2 results in phase-dependent photon counts at the single-photon detectors (D1 and D2), which are manifestations of the wave properties of the input single photons entering the interferometer. In contrast, by removing BS2, the counts at D1 and D2 are independent of the phase  $\varphi$  and display anti-bunching behaviour when the coincidence counts between D1 and D2 are measured. This leads to a seemingly paradoxical situation: whether the input photons behave as a particle or a wave depends on the observer's delayed choice.

Wheeler's gedanken experiment has been realized with photons $^{4-7}$  and atoms $^{8}$  (for recent reviews, see refs.  ${}^{9,10}$ ). As the configuration of the WDC experiment is controlled by the QRNG bit value (0 or 1), one can only probe the wave, the particle or the classical mixture of these two properties. The complementary interplay between particle and wave is well captured by the complementarity inequality $^{11-13}$ . In 2011, Ioniciou and Terno proposed a quantum version of the delayed-choice experiment  $(\mathrm{QDC})^{14}$ , in which BS2 is substituted by a quantum-controlled beamsplitter that can be in a superposition of being present and absent, as shown in Fig. 1b.

The configuration of the interferometer through which the system photon (S) propagates is determined by the quantum state of the control photon (C) by interactions. One advantage of the QDC experiment is that the experimentalist can arbitrarily choose the temporal order of the measurements on photons S and C. The QDC proposal and experimental realizations thereof are closely related to the well-known quantum eraser concept proposed by Scully and Druhl<sup>15</sup>. Note that the coherence in a quantum-controlled beamsplitter has also been theoretically analysed using entropic uncertainty relation in a non-delayed-choice configuration<sup>16</sup>. Moreover, a recent experiment established an alternative route to continuously morphing between the wave and particle behaviour of photons, demonstrating that the superposition of the particle and wave states can be controlled for each of two photons, together with the degree of their wave-particle entanglement<sup>17</sup>.

The QDC concept invited broad experimental efforts across different systems $^{18-25}$ . Very recently, a device-independent casual modelling framework for delayed-choice experiments has been theoretically proposed $^{26}$ , within which conflicts between classical and quantum physics are certified through a dimension witness under assumptions. This proposal has subsequently been implemented in a series of independent experiments $^{27-29}$ . In all QDC experiments, photons C and S have to interact directly to facilitate the operation of the quantum-controlled gate, which therefore hinders the realization of the required relativistic separations between relevant events. Later, a novel version of the non-local quantum delayed-choice experiment was proposed with multiple entangled photons $^{30}$ . The authors found the incompatibility between hidden-variable theories that simultaneously satisfy the conditions of objectivity, determinism and local independence of hidden variables and quantum mechanics describing an entangled system $^{30}$ . Here we report an experimental realization of the non-local delayed-choice experiment, which goes beyond both the WDC $^{23}$  and the QDC proposals $^{14,30}$ , and all previous demonstrations, by showing the genuine quantum wave-particle superpositions. Our work ultimately enables novel aspects of wave-particle duality to be explored, in the form of controllable quantum superpositions of the wave and particle states.

![](images/47c72f8ebe37857a1830d295f7faeb384086e459b7f57a75ccc2dd1737b1ea6e.jpg)  
Fig. 1 | The evolution of delayed-choice experiments. a, Wheeler's delayed-choice experiment. The choice of inserting or removing the output beamsplitter (BS2) is made by a quantum random number generator (QRNG) and delayed until after the single photon has passed through BS1. b, Quantum delayed-choice experiment. In contrast to a, BS2 is now replaced with a quantum beamsplitter, the setting of which is determined by the superposition state of a control photon (C). c, Non-local quantum delayed-choice experiment. The setting of BS2 is decided by the correlations of a control (C) and an ancilla photon (A), emitted from an Einstein-Podolsky-Rosen (EPR) entangled photon-pair source. The polarization of photon A is randomly projected onto the  $|H\rangle / |V\rangle$  or  $|\alpha\rangle = \cos\alpha |H\rangle + \sin\alpha |V\rangle / |\alpha^{\perp}\rangle = \sin\alpha |H\rangle - \cos\alpha |V\rangle$  basis. This allows us to remotely prepare the quantum gate, BS2.

# Scheme of the non-local QDC experiment

The conceptual scheme of our experiment is shown in Fig. 1c. Three single photons are involved: the system photon (S) that is sent through the interferometer and an entangled photon pair consisting of a control (C) and an ancilla (A) photon. Replacing the control photon with an entangled pair enables us to overcome the limitations of WDC and QDC experiments, as it allows us to simultaneously realize quantum control via remote quantum gate preparation and the relativistic separation between the relevant events. This is the novel aspect enabled by the multi-photon system we use in our experiment.

The procedure of our experiment is as follows. First, we prepare input states:

$$
\left| \right. \psi_ {\mathrm {S C A}} ^ {\mathrm {i}} \left. \right\rangle = \left| \right. V \left. \right\rangle_ {\mathrm {S}} \otimes \frac {\left( \right.\left| \right. H V \left. \right\rangle + e ^ {i \delta} \mid V H \left. \right\rangle\left. \right) _ {\mathrm {C A}}}{\sqrt {2}} \tag {1}
$$

where  $|\psi_{\mathrm{SCA}}^{\mathrm{i}}\rangle$  is the initial state of photons S, C and A (as labelled in Fig. 1c),  $|H\rangle$  and  $|V\rangle$  are the horizontally and vertically polarized states of single photons, respectively, and  $\delta$  is the relative phase between the  $|HV\rangle$  and  $|VH\rangle$  terms in the entangled state of photons C and A. Second, we send photon S into the interferometer, in which the output beamsplitter is a Hadamard gate controlled by photon C. However, unlike the original QDC proposal<sup>14</sup>, where photon C is in a pure state ( $|H\rangle$  or  $|V\rangle$ , or their arbitrary superpositions), here photons C and A are entangled and the individual quantum state of photon C is a mixed state. The configuration of the interferometer for photon S does not depend on the quantum state of photon C, but on the correlation of photons C and A. This means that we can remotely prepare a two-photon quantum gate operating on photons

S and C by controlling and measuring photon A based on the final state of photons S, C and A:

$$
\left| \psi_ {\mathrm {S C A}} ^ {\mathrm {f}} \right\rangle = \frac {1}{\sqrt {2}} \left| \mathbf {p} \right\rangle_ {\mathrm {S}} | H \rangle_ {\mathrm {C}} | V \rangle_ {\mathrm {A}} + \frac {e ^ {i \delta}}{\sqrt {2}} \left| \mathbf {w} \right\rangle_ {\mathrm {S}} | V \rangle_ {\mathrm {C}} | H \rangle_ {\mathrm {A}} \tag {2}
$$

where  $|\mathbf{p}\rangle_{\mathrm{S}}$  and  $|\mathbf{w}\rangle_{\mathrm{S}}$  are the particle and wave states of photon S, respectively[14,30]. When photon S is in  $|\mathbf{p}\rangle_{\mathrm{S}} = \frac{1}{\sqrt{2}}(|H\rangle - e^{i\varphi}|V\rangle)$  it behaves as a particle and when it is in  $|\mathbf{w}\rangle_{\mathrm{S}} = e^{i\varphi / 2}(-i\sin \frac{\varphi}{2}|H\rangle + \cos \frac{\varphi}{2}|V\rangle)$  it behaves as a wave. Note that states  $|\mathbf{p}\rangle$  and  $|\mathbf{w}\rangle$  represent an operational way to describe the particle (no interference) and wave (interference) behaviour of the photon, and these two states are in general not orthogonal. Such operational definitions allow us to conveniently show the continuous morphing between the different wave-particle dual nature. We can probe the wave property, the particle property, classical mixture and quantum superpositions of these two properties by projecting photon A onto the basis  $|\alpha\rangle = \cos \alpha |H\rangle + \sin \alpha |V\rangle$ ,  $|\alpha^{\perp}\rangle = \sin \alpha |H\rangle - \cos \alpha |V\rangle$ ,  $\alpha \in \left[0, \frac{\pi}{2}\right]$ .

As shown in Fig. 1c, a QRNG generates a bit string of 0 or 1 to randomly choose a projection angle equal to  $\alpha$  or 0 for photon A. When the QRNG gives a bit value of 0, then the projection angle equals  $\alpha$ . For the sake of simplicity, from now on we only discuss the results of photon A being projected into  $|\alpha^{\perp}\rangle_{\mathrm{A}}$ . The complementary results of photon A being projected into  $|\alpha \rangle_{\mathrm{A}}$  are presented in the Supplementary Information. When photon A is projected into  $|\alpha^{\perp}\rangle_{\mathrm{A}}$ , photons S and C are in the state  $|\psi_{\mathrm{SC}}^{\mathrm{f}}\rangle = -\cos \alpha |\mathbf{p}\rangle_{S}|H\rangle_{C} + e^{i\delta}\sin \alpha |\mathbf{w}\rangle_{S}|V\rangle_{C}$  as derived from equation (2). The detailed derivations are provided in the Methods. Taking the trace over photon C gives a classical mixed state of photon S:

$$
\rho_ {\mathrm {S}} = \cos^ {2} \alpha | \mathbf {p} \rangle \langle \mathbf {p} | + \sin^ {2} \alpha | \mathbf {w} \rangle \langle \mathbf {w} | \tag {3}
$$

For this classical case, the probability of obtaining photon S in  $|H\rangle$  conditionally on projecting photon A into  $|\alpha^{\perp}\rangle$ ,  $P_{\mathrm{C}}(\varphi ,\alpha) = P_{\mathrm{S} = |H\rangle |A = |\alpha^{\perp}\rangle}(\varphi ,\alpha)$ , is a function of  $\varphi$  and  $\alpha$ :

$$
P _ {\mathrm {C}} (\varphi , \alpha , \delta) = \frac {1}{2} \cos^ {2} \alpha + \sin^ {2} \alpha \sin^ {2} \frac {\varphi}{2} \tag {4}
$$

Note that  $P_{\mathrm{C}}(\varphi, \alpha)$  does not depend on  $\delta$ , the phase between the wave and particle states, manifesting its classical nature. By scanning both  $\varphi$  and  $\alpha$ , we obtain the distribution of  $P_{\mathrm{C}}(\varphi, \alpha)$ .

Based on equation (2), by projecting photon A on  $|\alpha^{\perp}\rangle$  and C on  $| - \rangle$ , where  $|\pm \rangle = (|H\rangle \pm |V\rangle) / \sqrt{2}$  stand for the diagonally and anti-diagonally linear polarization states, respectively, we obtain the renormalized state of photon S:

$$
\left| \psi_ {\mathrm {S}} \right\rangle = C _ {\mathrm {S}} \left(\cos \alpha | \mathbf {p} \rangle + e ^ {i \delta} \sin \alpha | \mathbf {w} \rangle\right) \tag {5}
$$

which is a quantum superposition of  $|\mathbf{p}\rangle$  and  $|\mathbf{w}\rangle$  representing the superposition of the 'ability' and 'inability' to produce interference. Note that the normalized coefficient is  $C_{\mathrm{S}} = (1 - \sqrt{2}\cos \alpha \sin \alpha \cos \varphi \cos \delta)^{-1 / 2}$ . The resulting probability of obtaining photon S in  $|H\rangle$  conditionally on photon C in the state  $| - \rangle$  and photon A being in the state  $|\alpha^{\perp}\rangle$ ,  $P_{\mathrm{Q}}(\varphi ,\alpha ,\delta) = P_{\mathrm{S} = |H\rangle |C = | - \rangle ,A = |a^{\perp}\rangle}(\varphi ,\alpha ,\delta)$ , is

$$
\begin{array}{l} P _ {\mathrm {Q}} (\varphi , \alpha , \delta) = \left| C _ {\mathrm {S}} \right| ^ {2} \left[ \frac {1}{2} \cos^ {2} \alpha + \sin^ {2} \alpha \sin^ {2} \frac {\varphi}{2} \right. \tag {6} \\ + \sqrt {2} \cos \alpha \sin \alpha \sin \frac {\varphi}{2} \sin \left(\delta + \frac {\varphi}{2}\right) \bigg ] \\ \end{array}
$$

It is clear from equation (6) that  $P_{\mathrm{Q}}$  depends on the phase  $\delta$ , displaying its quantum nature.

![](images/ef13af14dfe45f62a837362eb9ccc8dcc159138ade576b822d8c4f0ac0307ecb.jpg)

![](images/e1c922075742a966d38a35ab1555faf14b912a94c9fd4efc189673a6e1b22408.jpg)  
Fig. 2 | Experimental configuration. a, Birds-eye view of the experiment. The experiment set-up is distributed over two laboratories in the Tangzhongying building at Nanjing University (Lab1 and Lab2), which are separated by a line-of-sight distance of about  $141\mathrm{m}$ . In Lab1, we generate the initial state  $\left|\psi_{\mathrm{SCA}}^{\mathrm{i}}\right\rangle$ . Photon S propagates through a MZI with a Hadamard gate (BS2 in Fig. 1c) controlled by the entanglement of photons C and A generated by the source (EPR). Photon A is sent to Lab2 through a 215-m-long optical fibre and its polarization is measured there. b, Experimental set-up. In Lab1, a source of polarization-entangled photon pairs generates photons A and C in BBO1 and a collinear photon-pair source generates photons S and T in BBO2. Photon S interferes with photon C on a PPBS with perfect transmission  $T_{\mathrm{h}}$  for horizontal polarization and transmission  $T_{\mathrm{v}} = 1/3$  for vertical polarization in both output modes after propagating through  $186\mathrm{m}$  fibre delays, HWPs and an SBC ( $\varphi$ ). Photon A is sent to Lab2, where random polarization rotation is implemented using an electro-optical modulator (EOM) controlled by a QRNG. All photons are detected by single-photon avalanche diodes (SPADs). See text for definitions of the components. c, Space-time diagram. We relativistically separate the interference events (I) of photon S with respect to the choice events and the polarization projection events (F, R, D) of photon A.

![](images/19dc10c6ed6a43763706cfdd88ad05331bd46d6f0c968d3ae2139459464135b8.jpg)

# A QDC experiment under Einstein's locality condition

In Fig. 2, we show our experiment in detail. The experiment setup is distributed over two laboratories (Lab1 and Lab2), which are connected with optical single-mode-fibre cables and electrical coaxial cables. In Lab1, femtosecond pulses (central wavelength of  $808\mathrm{nm}$ ) from a Ti:sapphire laser are upconverted to blue pulses (central wavelength of  $404\mathrm{nm}$ ). These blue pulses are used to generate four photons (photons S, C, A as defined in Fig. 1c and an additional trigger photon T) via type-II spontaneous parametric down-conversion in two  $\beta$ -barium borate (BBO) crystals placed in sequence<sup>31</sup>. Photons C and A are generated in BBO1, which is in the non-collinear configuration, and are in entangled states with tunable phase  $\delta$  (ref. <sup>32</sup>). Photons S and T are generated in BBO2, which is in the collinear configuration, and are in product states  $|VH\rangle_{\mathrm{ST}}$ . The detection of photon T projects photon S into a single-photon state. We couple all four photons into single-mode fibres for later manipulation and detection. Photon S is then sent through a  $186\mathrm{m}$  single-mode-fibre coil and is guided to the polarization MZI. The polarization MZI consists of one half-wave plate (HWP) orientated at an angle of  $22.5^{\circ}$ , a Soleil-Babinet compensator (SBC) and a quantum-controlled Hadamard (CH) gate. The SBC introduces a relative phase  $\varphi$  between the  $|H\rangle$  and  $|V\rangle$  states. The CH gate consists of two HwPs with their fast axes oriented at an angle of  $11.25^{\circ}$  and a controlled Pauli-Z (CZ) gate between them. The CZ gate is realized through three partially polarizing splitters (PPBS) and four HwPs<sup>33-35</sup>. To achieve a successful quantum CH gate, photons S and C have to arrive at the first PPBS simultaneously and interfere. Therefore, photon C is also passing through a  $186\mathrm{m}$  single-mode fibre. For the details on the  $186\mathrm{m}$  fibre Hong-Ou-Mandel interferometer<sup>36</sup>, see Supplementary Information.

The key advance in our experiment, compared to previous QDC demonstrations, is that we realize a QDC experiment with

To achieve this we separate in space the events of random choice deciding whether to project photon A into the  $|\alpha \rangle / |\alpha^{\perp}\rangle$  or  $|H\rangle / |V\rangle$  basis and the events marking photon S entering into, propagating through and exiting from the MZI. Such separation is obtained by guiding photon A through a single-mode fibre from Lab1 to Lab2, which are separated by a line-of-sight distance of  $\sim 141\mathrm{m}$ . In Lab2, we use an EOM controlled by a QRNG, which generates random bits to set, with approximately equal probability, the polarization-analysis basis for photon A to be  $|\alpha \rangle / |\alpha^{\perp}\rangle$  or  $|H\rangle / |V\rangle$ . All photons are filtered with interference filters (IF,  $3\mathrm{nm}$  bandwidth). Seven SPADs detect four photons in different spatial modes.

A space-time diagram of our experiment is presented in Fig. 2c. At the origin, we generate four photons in Lab1 (event G). Photons S and C are delayed in two 186-m-long fibres (930 ns delay in time) in Lab1 before entering the MZI. After that, photon S interferes in the MZI (event I) controlled by photon C. In addition, a delay of  $\sim 29$  ns is introduced for photons S and C by short fibres and free-space optics. Photon A is transmitted through a 215-m-long fibre (1,075 ns delay in time) to Lab2. The QRNG has a repetition rate of  $5\mathrm{MHz}$ , which means that the random bit and hence the settings of the EOM can change every 200 ns. The moment QRNG starts to generate a random bit is defined as event F (upon receiving a trigger signal). The electric signal of the QRNG is shaped with a discriminator and sent to the EOM (event R), which modulates the polarization state of photon A. We then analyse and detect the polarization of photon A (event D). The entire process between events R and D takes 88 ns. See Supplementary Information for details regarding timing. The events relating to the interference of photon S in the MZI are space-like separated from the choice events and the polarization-projection events affecting photon A. In Lab1, we measure various three-photon coincidence counts between photons

![](images/10ad5c46473b4fb7af4761942f2e47e2d40aba67903fc90e0c066ff43dd43c26.jpg)

![](images/7166e1f67ea7f814acfdeeb68876abcd85d2f06a6895328eb48b541b7a85507e.jpg)

![](images/51d1e10304d36fc713e29299738fdbcdd75efbfeffb1d866020162b55ca7871e.jpg)

![](images/d3059800600b35152eb264015013010a333e9af17c6447307c945eab275b5dc3.jpg)  
Fig. 3 | Continuous transitions between particle and wave states in both classical and quantum scenarios. a-c, The simulated ideal, theoretically expected and experimentally measured probabilities  $P_{\mathrm{C}}(\varphi ,\alpha)$  for a classical mixture of particle and wave states. These are obtained by scanning the phase  $\varphi$  of the MZI for photon S and the polarization rotation angle  $\alpha$  of photon A. d-f, The simulated ideal, theoretically expected and experimentally measured probabilities  $P_{\mathrm{Q}}(\varphi ,\alpha ,\delta)$  for a quantum coherent superposition of particle and wave states with  $\delta = 0$ . In c and f, we experimentally performed a two-dimensional (2D) scan with nine values of  $\alpha$  and 12 values of  $\varphi$ , equally distributed from 0 to  $\pi /2$  and 0 to  $2\pi$ , respectively. The intermediate values between each step are linearly interpolated and plotted accordingly. Error bars in c and f are derived from Poissonian statistics and range from 0.013 to 0.046 and 0.02 to 0.063, respectively.

![](images/52114f24fdd81eb85ff0211bf21471e4c1d7de15da0d381b3798ba871056b29a.jpg)

![](images/7e3bb432d306c25a0f45386efa93f94c3a8327dd3bc1bab3cd51a23905b0c159.jpg)

S, C and T. In Lab2, we perform polarization measurements on photon A and categorize the detection results according to the clicked detectors and bit value of the QRNG. Then, after the measurement results have been irreversibly recorded with single-photon detectors in the two respective labs, we compare the results of S-C-T with A to obtain the conditional probability of photon S. These space-time arrangements ensure our realization of a QDC experiment under strict Einstein locality.

# Characterization of quantum wave-particle superpositions

Photon S can be a particle or a wave, or a classical mixture of the two if we perform the corresponding measurements on photons C and A, as shown in equation (3). In Fig. 3a, we plot the ideal conditional probability of photon S exiting the polarization MZI in horizontal polarization as a function of the phase  $\varphi$  of the MZI and the polarization projection angle  $\alpha$  for photon A, as shown in equation (4). Here we assume that the correlation of the photon source and the visibility of interference are unity. At  $\alpha = 0$  or  $\pi /2$ , photon S behaves as a particle or a wave, respectively, and hence no or full interference is seen. For angles between 0 and  $\pi /2$ , photon S is in a classical mixed state of particle and wave. In this regime, the complementary principle is valid and can be quantitatively characterized by the complementarity inequality, as has been shown experimentally in the context of delayed-choice experiments[19,37,38]. In Fig. 3b,c, we show the expected and experimentally measured results, which agree well with each other. Note that the parameters used to calculate the probability distributions shown in Fig. 3b are based on the values obtained from independent experimental measurements. Comparing to Fig. 3a, there is noticeable visibility degradation, which is mainly due to experimental imperfections, as quantitatively explained in the Supplementary Information.

More intriguingly, photon S can be in a quantum superposition of its particle and wave states. As shown in equation (5), we can

probe this superposition by projecting photons C and A onto the  $|+ \rangle / | - \rangle$  and  $|\alpha \rangle / |\alpha^{\perp} \rangle$  bases, respectively. In Fig. 3d-f, we show the ideal, the theoretically expected and experimental results of the conditional probability of photon S exiting the polarization MZI in the horizontal polarization as a function of  $\varphi$  and  $\alpha$  (equation (6) with  $\delta = 0$ ), respectively. At  $\alpha = 0$  or  $\pi / 2$ , photon S behaves as a particle or a wave, which is the same as in the classical case. However, distinct and subtle interference effects appear between 0 and  $\pi / 2$ , which are the signatures of genuine quantum superpositions. For detailed analysis and comparisons between the classical and quantum cases, see Supplementary Information.

The most direct proof for the quantum nature of the wave-particle superposition is to show that the result is sensitive to the relative phase between the wave and particle states,  $\delta$  (equation (6)). For classical mixtures, no such dependence exists (equation (4)). To probe such phase dependence, we fix  $\alpha$  at  $\pi /4$ , and measure  $P_{\mathrm{C}}$  and  $P_{\mathrm{Q}}$  as functions of  $\varphi$  and  $\delta$ . The results are shown in Fig. 4a-c for the classical mixture between the wave and the particle states, which are insensitive to the phase  $\delta$ . On the other hand, we show the results for genuine quantum coherent superpositions between wave and particle states in Fig. 4d-f. We stress that in the classical case  $P_{\mathrm{C}}$  remains sensitive to  $\varphi$  (Fig. 4c), which means that the well-known complementarity inequality can be verified. However, verification of the complementarity inequality[11-13,19,37,38] is not sufficient for proving that wave and particle states exist in a quantum superposition state. This is the key insight provided by the present work.

In conclusion, we have realized a non-local QDC experiment with multiphoton entangled states. We have shown that a single photon can be a particle, a wave, a classical mixture of particle and wave as well as a quantum superposition of particle and wave. Its property depends on the choice of the correlation measurements of two other photons, even if that choice is made at a location and a

![](images/57d8d1db97585b01952cae5575578513eb2460040ab8365fcf35ef79ecf1b672.jpg)  
a

![](images/4cafdba6e0f3ae47cee5d6403c0e219a62860766c8f728906f64d6ad4084e176.jpg)  
b

![](images/39ab6f02865962e495931865cc7e930b215cc9f4dd494c74625eac9113d404fb.jpg)  
c

![](images/984c94b51372015e4538d4ee2958908fad90ed5a69aede64595801cb2822eb31.jpg)  
d  
Fig. 4 | Witnessing the wave-particle quantum superpositions. We fix  $\alpha$  at  $\pi /4$  and measure  $P_{\mathrm{C}}(\varphi ,\delta)$  and  $P_{\mathrm{Q}}(\varphi ,\delta)$  as functions of  $\varphi$  and  $\delta$ . a-c, The simulated ideal, theoretically expected and experimentally measured probabilities  $P_{\mathrm{C}}(\varphi ,\delta)$  for a classical mixture of particle and wave states. d-f, The simulated ideal, theoretically expected and experimentally measured probabilities  $P_{\mathrm{Q}}(\varphi ,\delta)$  for a quantum superposition of particle and wave states.  $P_{\mathrm{C}}(\varphi ,\delta)$  is independent of  $\delta$ , whereas  $P_{\mathrm{Q}}(\varphi ,\delta)$  is strongly dependent on  $\delta$ , manifesting the quantum nature of the superposition of wave-particle states. In c and f, we performed the 2D scan with nine values of  $\delta$  and 12 values of  $\varphi$ , which are equally distributed from  $-0.05\pi$  to  $-1.95\pi$  and 0 to  $2\pi$  respectively. The intermediate values between each step are linearly interpolated and plotted. Error bars in c and f are derived from Poissonian statistics and range from 0.02 to 0.043 and 0.02 to 0.074, respectively.

![](images/24e159b578eb2693e03b67fd3c546051bc5afc2cccc402f085b5a964f591e71b.jpg)  
e

![](images/54ece84e827e60a9901101bdd0e67ccc5b989fd23bb913ba15c8f63d3e921ede.jpg)  
f

time such that it is relativistically separated from the photon entering into, propagating through and exiting from the MZI. By doing so, we have a situation where no interaction between photon A, and photons S and C, not even a hypothetical one that would propagate with the speed of light, would allow photon A to determine the property of photon S. This is a strong constraint set by the theory of special relativity. Our work provides the realization of wave-particle quantum superposition and the implementation of a full QDC experiment under strict Einstein locality conditions.

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, statements of code and data availability and associated accession codes are available at https://doi.org/10.1038/s41566-019-0509-0.

Received: 25 January 2019; Accepted: 12 July 2019

Published online: 2 September 2019

# References

1. Bohr, N. The quantum postulate and the recent development of atomic theory. Nature 121, 580-590 (1928).  
2. Wheeler, J. A. in Mathematical Foundations of Quantum Theory (ed. Marlow, A. R.) 9-48 (Academic Press, 1978).  
3. Wheeler, J. A. & Zurek, W. H. Quantum Theory and Measurement (Princeton University Press, 1984).  
4. Alley, C. O., Jakubowicz, O. G. & Wickes, W. C. Results of the delayed-random-choice quantum mechanics experiment with light quanta. In Proceedings of the 2nd International Symposium on Foundations of Quantum Mechanics, 36 (Physical Society of Japan, 1986).  
5. Hellmuth, T., Walther, H., Zajonc, A. & Schleich, W. Delayed-choice experiments in quantum interference. Phys. Rev. A 35, 2532-2541 (1987).  
6. Baldzuhn, J., Mohler, E. & Martienssen, W. A wave-particle delayed-choice experiment with a single-photon state. Z. Phys. B 77, 347-352 (1989).  
7. Jacques, V. et al. Experimental realization of Wheeler's delayed-choice gedanken experiment. Science 315, 966-968 (2007).

8. Manning, A. G., Khakimov, R. I., Dall, R. G. & Truscott, A. G. Wheeler's delayed-choice gedanken experiment with a single atom. Nat. Phys. 11, 539-542 (2015).  
9. Shadbolt, P., Mathews, J. C. F., Laing, A. & O'Brien, J. L. Testing foundations of quantum mechanics with photons. Nat. Phys. 10, 278-286 (2014).  
10. Ma, X.-S., Kofler, J. & Zeilinger, A. Delayed-choice gedanken experiments and their realizations. Rev. Mod. Phys. 88, 015005 (2016).  
11. Greenberger, D. M. & Yasin, A. Simultaneous wave and particle knowledge in a neutron interferometer. Phys. Lett. A 128, 391-394 (1988).  
12. Jaeger, G., Shimony, A. & Vaidman, L. Two interferometric complementarities. Phys. Rev. A 51, 54-67 (1995).  
13. Englert, B.-G. Fringe visibility and which-way information: an inequality. Phys. Rev. Lett. 77, 2154-2157 (1996).  
14. Ionicioiu, R. & Terno, D. R. Proposal for a quantum delayed-choice experiment. Phys. Rev. Lett. 107, 230406 (2011).  
15. Scully, M. O. & Druhl, K. Quantum eraser: a proposed photon correlation experiment concerning observation and 'delayed choice' in quantum mechanics. Phys. Rev. A 25, 2208-2213 (1982).  
16. Coles, P. J., Kaniewski, J. & Wehner, S. Equivalence of wave-particle duality to entropic uncertainty. Nat. Commun. 5, 5814 (2014).  
17. Rab, A. S. et al. Entanglement of photons in their dual wave-particle nature. Nat. Commun. 8, 915 (2017).  
18. Peruzzo, A., Shadbolt, P., Brunner, N., Popescu, S. & O'Brien, J. L. A quantum delayed-choice experiment. Science 338, 634-637 (2012).  
19. Kaiser, F., Coudreau, T., Milman, P., Ostrowsky, D. B. & Tanzilli, S. Entanglement-enabled delayed-choice experiment. Science 338, 637-640 (2012).  
20. Tang, J.-S. et al. Realization of quantum Wheeler's delayed-choice experiment. Nat. Photon. 6, 600-604 (2012).  
21. Roy, S. S., Shukla, A. & Mahesh, T. S. NMR implementation of a quantum delayed-choice experiment. Phys. Rev. A 85, 022109 (2012).  
22. Auccaise, R. et al. Experimental analysis of the quantum complementarity principle. Phys. Rev. A 85, 032121 (2012).  
23. Xin, T., Li, H., Wang, B.-X. & Long, G.-L. Realization of an entanglement-assisted quantum delayed-choice experiment. Phys. Rev. A 92, 022126 (2015).  
24. Zheng, S.-B. et al. Quantum delayed-choice experiment with a beam splitter in a quantum superposition. Phys. Rev. Lett. 115, 260403 (2015).  
25. Liu, K. et al. A twofold quantum delayed-choice experiment in a superconducting circuit. Sci. Adv. 3, e1603159 (2017).  
26. Chaves, R., Lemos, G. B. & Pienaar, J. Causal modeling the delayed-choice experiment. Phys. Rev. Lett. 120, 190401 (2018).

27. Polino, E. et al. Device independent certification of a quantum delayed choice experiment. Preprint at https://arxiv.org/abs/1806.00211 (2018).  
28. Huang, H.-L. et al. Compatibility of causal hidden-variable theories with a delayed-choice experiment. Phys. Rev. A 100, 012114 (2019).  
29. Yu, S. et al. Realization of a causal-modeled delayed-choice experiment using single photons. Phys. Rev. A 100, 012115 (2019).  
30. Ioniciou, R., Jennewein, T., Mann, R. B. & Terno, D. R. Is wave-particle objectivity compatible with determinism and locality? Nat. Commun. 5, 3997 (2014).  
31. Zukowski, M., Zeilinger, A. & Weinfurter, H. Entangling photons radiated by independent pulsed sources. Ann. NY Acad. Sci. 755, 91-102 (1995).  
32. Kwiat, P. G. et al. New high-intensity source of polarization-entangled photon pairs. Phys. Rev. Lett. 75, 4337-4341 (1995).  
33. Langford, N. K. et al. Demonstration of a simple entangling optical gate and its use in Bell-state analysis. Phys. Rev. Lett. 95, 210504 (2005).  
34. Kiesel, N., Schmid, C., Weber, U., Ursin, R. & Weinfurter, H. Linear optics controlled-phase gate made simple. Phys. Rev. Lett. 95, 210505 (2005).  
35. Okamoto, R., Hofmann, H. F., Takeuchi, S. & Sasaki, K. Demonstration of an optical quantum controlled-not gate without path interference. Phys. Rev. Lett. 95, 210506 (2005).  
36. Hong, C. K., Ou, Z. Y. & Mandel, L. Measurement of subpicosecond time intervals between two photons by interference. Phys. Rev. Lett. 59, 2044-2046 (1987).  
37. Jacques, V. et al. Delayed-choice test of quantum complementarity with interfering single photons. Phys. Rev. Lett. 100, 220402 (2008).  
38. Ma, X.-S. et al. Quantum erasure with causally disconnected choice. Proc. Natl Acad. Sci. USA 110, 1221-1226 (2013).

# Acknowledgements

We thank J. Kofler and C. Brukner for helpful discussions, and M. Chen for taking the birds-eye-view photograph of the experiment. This research is supported by the National Key Research and Development Program of China (2017YFA0303700), the National Natural Science Foundation of China (grants nos. 11690032, 11674170 and 11621091), the National Science Foundation of Jiangsu Province (no. BK20170010), the programme for Innovative Talents and Entrepreneur in Jiangsu and the Fundamental Research Funds for the Central Universities.

# Author contributions

K.W., Q.X. and X.-s.M. designed and performed the experiment. K.W. and X.-s.M. analysed the data. K.W. and X.-s.M. wrote the manuscript with input from all authors. S.Z. and X.-s.M. supervised the project.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s41566-019-0509-0.

Reprints and permissions information is available at www.nature.com/reprints.

Correspondence and requests for materials should be addressed to X.-s.M.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2019

# Methods

The choice-dependent final state of photons S, C, A can be written as  $|\psi_{\mathrm{SCA}}^{\mathrm{f}}\rangle$  , where

$$
\begin{array}{l} \left| \psi_ {\mathrm {S C A}} ^ {\mathrm {f}} \right\rangle = \frac {1}{\sqrt {2}} \left[ \sin \alpha | \mathbf {p} \rangle_ {\mathrm {S}} | H \rangle_ {\mathrm {C}} + e ^ {i \delta} \cos \alpha | \mathbf {w} \rangle_ {\mathrm {S}} | V \rangle_ {\mathrm {C}} \right] \left| \alpha \right\rangle_ {\mathrm {A}} \\ + \frac {1}{\sqrt {2}} [ - \cos \alpha | \mathbf {p} \rangle_ {S} | H \rangle_ {C} + e ^ {i \delta} \sin \alpha | \mathbf {w} \rangle_ {S} | V \rangle_ {C} ] \tag {7} \\ \left| \alpha^ {\perp} \right\rangle_ {\mathrm {A}} \\ \end{array}
$$

and where we project photon C onto the  $|H\rangle /|V\rangle$  basis. On the other hand, if we project photon C onto the  $|+ \rangle /| - \rangle$  basis, the final state is in the form

$$
\begin{array}{l} \left| \psi_ {\mathrm {S C A}} ^ {\mathrm {f}} \right\rangle = \frac {1}{2} \left[ \left(\sin \alpha | \mathbf {p} \rangle_ {\mathrm {S}} + e ^ {i \delta} \cos \alpha | \mathbf {w} \rangle_ {\mathrm {S}}\right) | + \rangle_ {\mathrm {C}} \right. \\ + \left(\sin \alpha | \mathbf {p} \rangle_ {S} - e ^ {i \delta} \cos \alpha | \mathbf {w} \rangle_ {S} | - \rangle_ {C} | \right. \left| \alpha \right\rangle_ {A} \\ + \frac {1}{2} \left[ (- \cos \alpha | \mathbf {p} \rangle_ {S} + e ^ {i \delta} \sin \alpha | \mathbf {w} \rangle_ {S}) | + \rangle_ {C} \right. \\ - \left(\cos \alpha | \mathbf {p} \rangle_ {S} + e ^ {i \delta} \sin \alpha | \mathbf {w} \rangle_ {S}\right) | - \rangle_ {C} | \left. \alpha^ {\perp} \right\rangle_ {A} \\ \end{array}
$$

# Data availability

The data that support the plots within this paper and other findings of this study are available from the corresponding author upon reasonable request.