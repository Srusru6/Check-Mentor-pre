# Integrated optical entangled quantum vortex emitters

Received: 3 July 2024

Accepted: 10 January 2025

Published online: 28 February 2025

![](images/0a7de2df2716b9b5a159bde3128744d7c086904cfc496163fb56bed9e4b8098b.jpg)

Check for updates

Jieshan Huang  $^{1,12}$ , Jun Mao  $^{1,12}$ , Xudong Li  $^{1,10,12}$ , Jingze Yuan  $^{1,11,12}$ , Yun Zheng  $^{1}$ , Chonghao Zhai  $^{1}$ , Tianxiang Dai  $^{1,2}$ , Zhaorong Fu  $^{1}$ , Jueming Bao  $^{1}$ , Yan Yang  $^{3}$ , Daoxin Dai  $^{4,5}$ , Yan Li  $^{1,6,7,8,9}$ , Qihuang Gong  $^{1,6,7,8,9}$  & Jianwei Wang  $^{1,6,7,8,9}$

Quantum vortices of light carrying orbital angular momentum stand as essential resources for quantum photonic technologies. Recent advancements in integrated photonics offer the potential to create and control quantum vortices using fully integrated circuits, eliminating the need for intricate free-space alignment, modulation and the stabilization of bulky optical elements. However, generating quantum vortices in planar optical waveguides and circuits poses challenges, owing to the complexities of confining and guiding twisted photons and, importantly, the difficulties in preparing the quantum superposition and entanglement of vortex states. Here we report the realization of entangled quantum vortex emitters, leveraging programmable integrated nanophotonic circuits. These circuits enable the generation and arbitrary control of resilient vortex entanglement in free space, coherently transitioning from on-chip-created path entanglement. This capability is facilitated by a chip-to-free-space interfacing quantum technology that combines reprogrammable integrated quantum photonics with advanced classical free-space beam structuring. The emitters operate in a plug-and-play manner, enabling swift reconfiguration within microseconds. Validation of multidimensional genuine entanglement is achieved through quantum tomography and measurement of the dimension witness. Our work demonstrates integrated quantum vortex devices that combine the versatility of the on-chip processing quantum information with the robustness of transmitting quantum vortices in free space, opening new avenues for applications in quantum communication, quantum light detection and ranging, and quantum computation and storage.

Quantum vortices embody ubiquitous singular phases in light and matter $^{1-3}$ . In particular, optical vortices carrying orbital angular momentum (OAM) in light beams and single photons exhibit distinctive helical-phase structures $^{4-6}$ , enabling them to potentially encode a large amount of quantum information. Extensive efforts have been made to explore the quantum entanglement of optical vortices, leading to many important achievements, for example, in strong violation of nonlocality $^{7,8}$ , large-quanta entanglement $^{9,10}$ ,

multiphoton multidimension entanglement $^{11,12}$ , multimode quantum storage $^{13,14}$ , high-capability quantum key distribution $^{15,16}$  and teleportation $^{17,18}$ .

The ongoing advancement of quantum technologies with optical vortices demands fully integrated, robust and rapidly reconfigurable OAM devices $^{5,6}$ . Integrated photonics offers a promising avenue for generating and manipulating optical vortices as demanded. However, planar optical waveguides and circuits face challenges in

A full list of affiliations appears at the end of the paper.  $\boxtimes$  e-mail: dxdai@zju.edu.cn; jww@pku.edu.cn

Table 1 | Comparison of silicon-based integrated photonic entangled photon-pair sources using various degrees of freedom  

<table><tr><td>Integrated entangled photon sources</td><td>Dimensionality</td><td>Programmability</td><td>Photon rates (Hz)</td><td>Fidelity</td><td>Verification</td><td>Applications</td></tr><tr><td>① Path entanglement57</td><td>2</td><td>Full</td><td>30</td><td>0.83(2)</td><td>CHSH, QST</td><td>Fundamental, QIP</td></tr><tr><td>② Path entanglement37</td><td>15</td><td>Partial</td><td>2,000</td><td>0.81(1)</td><td>CGLMP, QST</td><td>Fundamental, QIP</td></tr><tr><td>③ Polarization entanglement58</td><td>2</td><td>No</td><td>800</td><td>0.962(7)</td><td>CHSH, QST</td><td>QKD</td></tr><tr><td>④ Time-bin entanglement59</td><td>2</td><td>No</td><td>7</td><td>0.910(7)</td><td>QST</td><td>QKD</td></tr><tr><td>⑤ Frequency entanglement60</td><td>3</td><td>Partial</td><td>620</td><td>0.857(2)</td><td>CHSH, QST</td><td>QKD, QIP</td></tr><tr><td>⑥ Spatial mode entanglement35</td><td>3</td><td>Full</td><td>50</td><td>0.912(7)</td><td>CGLMP, QST</td><td>QKD, QIP</td></tr><tr><td>⑦ OAM entanglement (this work)</td><td>5</td><td>Full</td><td>200</td><td>0.87(6)</td><td>QST, witness</td><td>QKD, QIP, OAM-atom</td></tr></table>

Integrated entangled photon sources:  $①$  path-entangled qubits $^{57}$ ,  $②$  path-entangled qubits $^{37}$ ,  $③$  polarization-entangled qubits $^{58}$ ,  $④$  time-bin-entangled qubits $^{59}$ ,  $⑤$  frequency-entangled qubits $^{60}$ ,  $⑥$  spatial-mode-entangled qubits $^{35}$  and  $⑦$  OAM-entangled qubits in this work. Dimensionality refers to the local size of each photon, with a qubit having a dimensionality of two and a qudit having a dimensionality greater than two. Programmability denotes the ability to reconfigure devices and circuits to generate various entangled states. Photon rates are indicated by the twofold coincidence counts. State fidelity represents the degree of overlap between the generated state and its theoretical counterpart, subject to variations in the definition of state fidelity, where the values in parentheses specify the uncertainty of the measured fidelity. Entanglement can be verified through experimental violation of the Clauser-Horne-Shimony-Holt (CHSH) inequality for qubit systems or the Collins-Gisin-Linden-Massar-Popescu (CGLMP) inequality for qudit systems, the implementation of quantum state tomography (QST) and the measurement of an entanglement dimension witness. Various potential applications for different entangled states are outlined, including the investigation of fundamental physics such as the nonlocality test, quantum key distribution (QKD) and quantum information processing (QIP). OAM-entangled devices have the potential to enable multimode quantum memory and light-atom-based quantum computing.

confining and guiding OAM modes due to the difficulty in maintaining helical phases in non-circularly symmetric waveguides $^{19-21}$ . This limitation thus hinders the direct generation of the quantum entanglement of OAM modes in waveguides, particularly when intricate nonlinear-optical processes for OAM are imposed. Alternatively, the emerging technology of chip-to-free-space interfacing combines the versatility of photonic circuits in waveguides with the robustness of beam shaping in free space, presenting a promising solution. With this technology, integrated devices can precisely control phases and amplitudes, enabling the free-space formation of helical beams by emitting multiple tailored beams out of waveguides, eventually twisting the wavefront. Pioneering efforts have encompassed both passive and reconfigurable approaches for tailoring the emitted beams. For example, a single microring with multiple passive grating emitters has been realized for classical OAM emitters $^{22,23}$ , OAM lasers $^{24,25}$  and OAM combs $^{26-28}$ . Programmable integrated photonic devices $^{29,30}$  with multiple individually reconfigurable phase emitters have been explored to shape beams or vortices in free space, for classical telecommunication and light detection and ranging $^{31-34}$  and for quantum communication $^{35,36}$ . Moreover, on a single quantum chip, capabilities have been demonstrated for generating and manipulating multidimensional multiphoton entanglement $^{37-39}$  and the processing of quantum information $^{40-42}$ , whereas going beyond a single quantum chip out to free space, entanglement distribution and the teleportation of polarized $^{43,44}$  and spatial modes $^{35}$  have been reported. Despite the remarkable progress made in reconfigurable light control in waveguide circuits and free-space light-beam shaping, generating the entanglement of vortex states in integrated optical devices remains experimentally challenging. Table 1 summarizes the silicon-based integrated entangled photon-pair sources that have been demonstrated across various degrees of freedom, excluding the OAM entanglement source.

Here we demonstrate entangled quantum vortex emitters with programmable integrated photonic circuits. This achievement is realized through the demonstration of a fully integrated optical chip-to-free-space quantum interface, coherently converting robust on-chip path entanglement into OAM entanglement that can reliably transmit in free space. The integrated device performs a Fourier transform on the waveguide modes at different positions to generate a transverse phase gradient and then maps the linear phase to a helical phase, emitting the entangled vortices into free space. The device integrates all components for the generation of plug-and-play vortex entanglement, and it enables the arbitrary and rapid operation of

five-mode OAM entanglement by manipulating path entanglement using universal multimode interferometers. The integrated entangled vortex devices can be scaled up to generate more vortices in larger dimensions. The conceptual advancement of chip-to-free-space quantum interfacing not only enables the generation of vortex entanglement with integrated optics but also opens new avenues for practical quantum communication, quantum light detection and ranging, multimode quantum storage and light-atom-based quantum computing applications.

We propose a scheme of generating entangled quantum vortices. It first creates a multi-qudit path-entangled state $^{39}$  where every audit is prepared across a number of  $m$  waveguiding paths or modes, and it then converts the state to a multi-qudit OAM entangled state where every audit has a topological charge of  $l$ . A coherent conversion of path entanglement and OAM entanglement is shown in equation (1):

$$
\frac {1}{\sqrt {d}} \sum_ {m} | m \rangle^ {\otimes n} \rightarrow \frac {1}{\sqrt {d}} \sum_ {l} | l \rangle^ {\otimes n}, \{m, l \} \in \left[ - \frac {d - 1}{2}, \dots , 0, \dots \frac {d - 1}{2} \right], \tag {1}
$$

where  $|m\rangle$  is the logical basis of path-encoded qudits,  $|l\rangle$  is the logical basis of OAM-encoded qudits,  $n$  represents the number of qudits and  $d$  is the local size of every qudit ( $d$  is chosen as an odd integer). This scheme enables the generation of an array of entangled vortices with a number of  $n$  vortices and a local size of  $d$ . Importantly, path entanglement could be arbitrarily operated by universal linear-optic circuits, so that arbitrary OAM entanglement can be generated with integrated optics, beyond any other possible approaches.

Figure 1 shows an integrated-optic device for generating and manipulating the entanglement of two vortices with a local size of five, as an example. Five-dimensional path-entangled quuds are generated by coherently exciting spontaneous four-wave-mixing (SFWM) sources that produce two degenerate single photons (Supplementary Fig. 1) $^{37}$ . The path quuds can be individually manipulated using five-mode universal linear-optic circuits $^{45}$ , yielding arbitrary operations of path entanglement. One key device is the integrated path-to-OAM converter that works as the chip-to-free-space interface, which can be considered as a fully integrated version of the inverse mode sorter using discrete bulk optics $^{46,47}$  that has been used widely for efficient OAM detection $^{48}$  and the generation of OAM entanglement $^{49}$ . Our integrated path-to-OAM converter includes three stages: (1) Fourier transform in an on-chip Rowland circle $^{50}$ , which transforms the path mode  $|m\rangle$  at the  $m$ th input waveguide (a total number of  $d$  inputs) to the superimposed

![](images/0515a4d2ed3a84f4159aa3c8c1224b176d4a55f02bd5d276920f47a5466a2b71.jpg)

![](images/f52b7643ad41079d144234db50c211c4f1bece63816924157b8763fdb6b88b7d.jpg)  
Fig.1|Generating quantum vortex entanglement with programmable integrated nanophotonics. a, Optical microscope image of the entangled vortex chip. The chip, based on silicon nanophotonics, monolithically integrates an array of SFWM photon-pair sources, two sets of universal linear-optic circuits and two path-to-OAM converters. Pairs of degenerate single photons (shown as red-coloured sphere-and-arrow combinations), generated in the integrated SFWM sources from external dichromatic excitations (coloured blue and purple), are subsequently routed by a mesh of crossers, resulting in the preparation of a path-encoding five-dimensional Bell state. The linear-optic circuits with squarely nested Mach-Zehnder interferometers are fully reprogrammable, enabling the arbitrary manipulation of the five-dimensional path entanglement. The two path-to-OAM converters, each of which involves Fourier transform in a Rowland circle (of inner circle radius  $r$  and outer circle radius  $R$ ), phase compensation by an array of optical phase shifters and linear-to-helical phase mapping via a

![](images/451e82d7db6014748ebd5bca71abde9990c37ce64638d7cdfee899fb27f74876.jpg)  
circular grating, emit the entangled vortices to free space for the detection of entanglement. The chip is wire-bound (gold wires) for reconfigurable operations. b,c, Scanning electron microscope images of the on-chip Rowland circle (b) and circular grating (c) structures. In b, the Rowland circle is embedded in a free-propagation region with five input and 16 output waveguides (see the expanded images in the left and right insets, respectively), performing the Fourier transform on the path mode  $|m\rangle$  in the mth input to the superimposed mode (indicated by the blue dashed line) with the transverse phase gradient of  $2\pi m j / N$  at the jth output. In c, the circular gratings implement linear-to-helical mapping, forming a helical wavefront  $e^{-i\phi}$  in free space. They are formed by concentrically etched gratings with a period of 575 nm and a 49% duty cycle (see the expansion in the inset), designed to facilitate the vertical emission of beams and optimize emission efficiency. To reduce losses, tapering structures are used to connect single-mode waveguides with the Rowland circle and circular grating.

mode with a transverse phase gradient of  $2\pi m j / N$  at the  $j$ th output waveguides  $(j \in [0,1,\dots,N-1]$ , where  $N = 16$  is the number of outputs), as shown in Fig. 1b. (2) Phase compensation, which compensates phase distortions from fabrication using an array of individually tunable phase shifters (Fig. 1a). (3) Mapping from the transverse (linear) phase gradient to the angular (helical) phase gradient, by uniformly positioning the  $N$  beams around a diffractive circular grating (Fig. 1c) $^{51}$ . The emitted photon possesses a helical wavefront  $e^{-il\phi}$  ( $\phi$  is the azimuthal angle in the cylindrical coordinate system) in the far field, which essentially generates the vortex carrying  $|l\rangle$ -order OAM where  $l = m$ . That is, the path mode  $|m\rangle$  is converted exactly to the OAM mode  $|l\rangle$ . We used the inverse of the OAM sorter $^{51}$  developed in classical optics as the path-to-OAM converter, and operated it in a fully quantum-coherent region so as to flexibly prepare the superposition and entanglement

of OAM states with integrated optics. By programming the path entanglement, the device shown in Fig. 1 enables the generation of arbitrary two-vortex five-dimensional entanglement. Details regarding the device design and fabrication are provided in the Methods.

We first characterized the integrated-optic path-to-OAM converter. Digital off-axis holography $^{52,53}$  was used to read out the phase distributions of the emitted OAM light from the circle gratings (Supplementary Fig. 5a). Figure 2a-d shows the holography-measured phase-front distributions for the OAM beams before and after phase compensation. Random phase errors from fabrication were well compensated, by individually optimizing the optical phases in the long waveguides that connect Fourier transform and linear-helical mapping. For the  $l = \{0,1,2\}$ -order OAM modes shown in Fig. 2b-d, their uniformly distributed helical phase gradient  $2\pi l / N$  was confirmed

![](images/b0f3da5ee31ce027fad9e2b91a6f45b6749cbb718eaf7757f5279e7230907f5e.jpg)  
a  
Before compensation

![](images/d2b6c352088baf3e05394bfe3e20bdd2aacdd14e33d1dcfb3d65810a10b387f2.jpg)  
b  
After compensation

![](images/faa5b9dfc0deb6e7b6ce59ea6ee6de9d671d45cc89f55c0316af548cd83ae6a0.jpg)  
C  
After compensation

![](images/c27401ef136c158520295aeb8bdee9b465c27d685a2f1a62ca17a6e8e7cbe8d8.jpg)  
d  
After compensation

e  
Z basis (device 1)  
Fig. 2 | Characterization of the integrated optical path-to-OAM interface.  
![](images/fa117e7ce7ed47c40c105b35d9440bdaa4d11ddd156c73e6e7f7824e6201f1c5.jpg)  
a-d, Digital off-axis holography images of the reconstructed near-field phase distributions of the circular grating before (a) and after (b-d) phase compensation. Bright spots represent the emitted beams carrying a phase gradient of  $2\pi m j / N$ . In c and d, the gradient phases form the twisted phase front  $e^{-i\phi}$  in the far field. Colours represent the phases and brightnesses represent the light intensities. e-h, Experimental path-input OAM-output matrices for two vortices (devices 1 (e,f) and 2 (g,h)). The matrices are

![](images/d4dc8f57d3e2271e0d311230377bcbfbddbd2f4e7775e3430206436f2453978c.jpg)  
f  
$F$  basis (device 1)

g  
Z basis (device 2)  
![](images/bf622db2d608a172fad6f0f42c8f0ca5df91e6c47837686238a80ef6b06afcd0.jpg)  
characterized in the computational  $Z$  basis  $|k\rangle_{m / l}^{Z}(\mathbf{e},\mathbf{g})$  and the superposition  $F$  basis  $|k\rangle_{m / l}^{F} = \frac{1}{\sqrt{5}}\sum_{j}e^{i\frac{2\pi}{5}jk}|j\rangle_{m / l}(\mathbf{f},\mathbf{h})$ , where  $k = \{0,\pm 1,\pm 2\}$  and subscripts  $m$  and  $l$  represent the logical basis of the path and OAM states, respectively. The colours in each matrix grid represent the measured cross-talk ratios. The cross-talk can be characterized via the classical statistic fidelity,  $\mathrm{Fid_c} = \left(\sum_i\sqrt{p_iq_i}\right)^2$ , where  $p_i$  and  $q_i$  are the experimental and theoretical distributions, respectively.

![](images/730ab74faf651dbd1c8c1a22cd17c179ca5bf3494526931b66e732ea6f61a9a2.jpg)  
h  
$F$  basis (device 2)

(also shown by the linear fitting in Supplementary Fig. 5b). Moreover, we characterized the modal cross-talk of the emitted OAM beams by performing projective measurements at different OAM bases (that is, the computational  $Z$  basis and the superposition  $F$  basis) using a spatial light modulator (see Supplementary Fig. 5c). An adaptive moment estimation optimizer was used to optimize the phases to further reduce modal cross-talk, including those from path-state preparation, path-to-OAM conversion and OAM detection. Figure 2e–h shows the measured path-input OAM-output matrices for two vortices. The results show that the matrices have a classical statistic fidelity of 0.97(2). Note that the setting of the phase compensators is to be fixed after calibration, with no need for further operation during the entanglement generation, manipulation and measurement. Furthermore, the near-field images reported in Fig. 2a–d show the presence of higher-order modes. This stems from the spatial discretization of the 16 waveguides transmitting light fields from the Fourier transform unit to the circular grating, leading to the generation of higher-order OAM harmonic modes. In our experiment, we effectively filtered out high-order modes in the far field to ensure high-fidelity OAM entanglement, albeit at the expense of introducing additional losses. This OAM harmonics effect can be mitigated through optimization of the angularly distributed spot size and the number of sampling spots. Detailed analysis and discussion are provided in Supplementary Note 5.

To confirm the successful generation and manipulation of superposition vortex states and entangled vortex states, we implemented both classical and quantum characterizations, which rely on the detection of bright photon flux and single photons, respectively. For classical characterization, we used high-photon-flux laser light to capture the spatial mode distribution of OAM and OAM superposition states as well as interferometric patterns, which were recorded using an infrared CCD (charge-coupled device) camera—the results are reported in Fig. 3 and the interferometric measurement set-up is shown in Supplementary

Fig. 6a. For quantum characterization, we performed full quantum state tomography and entanglement witness measurements to validate the entangled vortex states. This involved detecting single-photon statistics and correlations using superconducting single-photon detectors—the results are shown in Fig. 4 and the experimental set-up is illustrated in Supplementary Fig. 3. When pumped using pulsed light with an average power of  $20\mathrm{mW}$ , we estimated that the device emits OAM-OAM entangled photon pairs at a rate of approximately  $200\mathrm{Hz}$ , primarily influenced by the path-to-OAM converters with a  $10.54\mathrm{dB}$  loss. Detailed characterization of the losses in various components of the circuit, in the free-space OAM projective measurement system and the estimation of the rate are provided in Supplementary Note 4.

Interferometric measurements were performed to classically characterize the generated OAM beams, by co-axis interfering with a Gaussian reference beam. The interference patterns for the OAM eigenmodes are shown in Fig. 3a, from which the OAM changes  $l$  can be read directly from the number and chirality of the spiral arms. The experimental results are in good agreement with the simulations, indicating the generation of high-quality OAM beams via selective path-to-OAM conversion. These generated beams in fact are vector vortex beams, where their polarization state is azimuthally polarized (see Supplementary Note 1 and Supplementary Fig. 4). The measurement of OAM modes is decomposed to those with left-hand and right-hand polarization. During experiments, we detected the left-hand component of OAM states and entangled states. For the ease of reading, in this work, we define  $l$  by the interference patterns. Higher-order OAM beams can be generated by shifting the on-chip phases (see Supplementary Fig. 6b).

To generate arbitrary OAM superposition states by controlling the integrated multimode unitary operators, we measured all two-mode superposition states in Fig. 3b. The measured and simulated mode profiles are in good agreement. A continuous rotation of the OAM superposition state was measured via on-chip sweeping of the internal

![](images/11c4588a4200c63a683753d4619291ba16c208f3eaa8881dd29b1970fbfa5d58.jpg)

![](images/d5bcebdce25f89e06e9720d2c92837f0f17f8385efa57d2e4fd8aa64f418422c.jpg)  
Fig. 3 | Interferometric measurement and reprogramming of OAM modes. a, Interference patterns between an OAM eigenmode and a Gaussian beam. The OAM states are identified by the number and chirality of the spiral arms. Sim, simulated; Exp, experimental. b, Experimental and simulated far-field intensity patterns of the generated OAM eigenmodes and OAM equal superposition modes. For example, the patterns in the white dashed boxes represent a superposition state of  $(| - 2\rangle_{l} + |1\rangle_{l}) / \sqrt{2}$ . c, Coherent rotation of OAM superposition states, by swapping the internal phase  $\theta$  between the two OAM modes and all five OAM modes. Points denote the experimental data (collected

![](images/3e3d81a2f6c749b184b8225b31c47f3860c5a432da30d8fdfceea89010c7b065.jpg)

![](images/4be153f32309746832e865ff977fade328e081975c13256a54de425e9c55617e.jpg)  
with a fixed projection in the spatial light modulator), and the green curves are fitting lines. The insets show the captured and simulated patterns at different  $\theta$  values. The contrast  $(C)$  is defined as  $(N_{\mathrm{max}} - N_{\mathrm{min}}) / (N_{\mathrm{max}} + N_{\mathrm{min}})$ , where  $N_{\mathrm{max}}$  and  $N_{\mathrm{min}}$  denote the maximal and minimal power, respectively. d, Dynamic reconfiguring of the OAM states by operating the linear-optic circuits. They were driven using a sequence of square waves with a repetition rate of  $5\mathrm{kHz}$ , a duty cycle of  $20\%$  and a delay of  $40~\mu \mathrm{s}$  between each one. The rise time, that is, the time interval that it takes the signal to go from 10 to  $90\%$  of its final intensity, is measured to be around  $7.0~\mu \mathrm{s}$ .

phase  $\theta$  while keeping the projection basis. High-contrast quantum coherence is observed in Fig. 3c. We also characterized the full-five-mode OAM superposition state of  $\sum_{l}e^{\frac{2\pi l}{5}\theta}|l\rangle$ . At the valleys of the interference fringe, it returns the Fourier superposition modes, whose orthogonality is imaged by the interference patterns. Moreover, to demonstrate dynamic control of the OAM states, a sequence of square waves was applied to the on-chip linear-optic circuits to rapidly reconfigure the generation of vortices switching between different modes. The experimental results in Fig. 3d show sequential excitation of the five OAM states, with a rise time of about  $7.0~\mu s$ .

We then characterized and certificated multidimensional entanglement. We reconstructed the initial path-path entangled

state  $\rho_{\mathrm{path - path}}$  before conversion (see Fig. 4a) and the OAM-path entangled state  $\rho_{\mathrm{OAM - path}}$  (see Fig. 4b) by performing quantum state tomographic measurements. The OAM-path entanglement can be used for chip-to-chip multidimensional entanglement distributions, keeping one path-qudit on the chip while transmitting another OAM-qudit through free space, and vice versa[35]. When reconstructing the OAM-OAM entanglement, the two entangled vortices that separately emit OAM photons need to be simultaneously collected and locally measured. In our experiment set-up, the field of view for a long-working-distance objective lens is limited, such that the two vortices cannot be efficiently collected at the same time (the simultaneous detection of two vortex beams is achievable by optimizing the chip design and the measurement set-up—see Methods). We here

![](images/fe6538ae43aea0a4c04c3882fa430b5cc67aede3edcc6fe66c539bf1829c389d.jpg)

![](images/a562937c84015beffc06c1be0bb098ef0996f0ef457e04102b3d70646b7ae0a9.jpg)

![](images/029187a8770e0edd93f3b1982981bce98a807cec026d553e46d4f3da30aa700f.jpg)

![](images/9bb3897ffa3cd9ff0208a8806e6ec7a972c88553b856975813902e9979802693.jpg)  
Fig. 4 | Measurement and verification of multidimensional entanglement. a-c, Experimentally reconstructed density matrices for the path-path entangled state  $\rho_{\mathrm{path - path}}$  (a), the OAM-path entangled state  $\rho_{\mathrm{OAM - path}}$  (b) and the OAM-OAM entangled state  $\rho_{\mathrm{OAM - OAM}}$  (c). Quantum state tomographic measurements using the compress sensing techniques were implemented to reconstruct the density matrices. The  $\rho_{\mathrm{OAM - OAM}}$  in c was obtained by applying the measured transfer matrix  $M_2$  to the measured  $\rho_{\mathrm{OAM - path}}$  in b. Column heights represent the absolute  $|\rho|$  values, whereas the colours represent the  $|\mathrm{Arg}(\rho)|$  phases. Phases for matrix elements with  $|\rho_{ij}|\leq 0.01$  are not shown for clarity. The quantum state fidelity  $\mathrm{Fid}_q$  is defined as  $(\mathrm{tr}[\sqrt{\sqrt{\rho_0}\rho\sqrt{\rho_0}}])$ , where  $\rho_0$  and  $\rho$  are the ideal and measured states, respectively. The values in parentheses indicate  $\pm 1\sigma$  uncertainty, estimated from Poissonian photon statistics. d,e, The visibility  $V(\mathbf{d})$  and  
dimension witness  $W(\mathbf{e})$  results measured for the five-dimensional entanglement witness of the OAM-path entangled state. In  $\mathbf{d}$ , the visibilities  $V_{i}^{a,b} = |\langle \sigma_{i}\otimes \sigma_{i}\rangle |$  where  $i\in \{x,y,z\}$  and  $\{a,b\} \in [-2, - 1,0,1,2]$ , are measured in the Pauli bases  $\{\sigma_x,\sigma_y,\sigma_z\}$ , which are indicated by the purple, pink and blue backgrounds, respectively. The yellow-shaded bars denote the experimental results, the teal-shaded areas represent the error bars and the dashed boxes indicate the theoretical values. In  $\mathbf{e}$ , the measured  $W$  value (indicated by the top of the teal column) is estimated to be 27.(2), which exceeds the upper bound of 25 for four-dimensional entanglement (as indicated by the orange line); the dashed box also indicates the theoretical value. The error bars indicate  $\pm 1\sigma$  uncertainty, estimated from Poissonian photon statistics.

![](images/32b2807dbc178a3d5efca123db4ed9ccc23f460e31d5e9ba66afa5bdf43f00ac.jpg)

instead reconstructed the density matrix for the OAM-OAM entangled state by leveraging the transfer matrices for path-to-OAM conversions. The measured transfer matrices  $(M_{1}$  and  $M_2)$  for the two channels of path-to-OAM conversion are provided in Supplementary Fig. 11. From this, the OAM-path entangled state  $\rho_{\mathrm{OAM - path}}$  can be inferred from  $\rho_{\mathrm{path - path}}$  and  $M_{1}$  in Supplementary Fig. 12, which is consistent with the tomography result in Fig. 4b. Their compatibility confirms the validity of verifying OAM entanglement. Thus, by applying  $M_2$  to the measured state  $\rho_{\mathrm{OAM - path}}$ , it enables the reconstruction of the density matrix for the entangled vortices. The  $\rho_{\mathrm{OAM - OAM}}$  result for the OAM-OAM entangled state is shown in Fig. 4c, and the quantum state fidelity of this is estimated to be 0.87(6). The degradation in state fidelity from path entanglement to OAM entanglement can be attributed to various factors, including inaccuracies and losses in the projection measurements and the experimental set-up (see Supplementary Note 6).

We characterized the entanglement dimension witness for multidimensional entangled states. The dimension witness observable  $(W)$  is defined as the sum of interference visibilities in all two-dimensional subspaces<sup>10</sup>:

$$
W = \sum_ {a = 0} ^ {d - 2} \sum_ {b = a + 1} ^ {d - 1} \frac {V _ {x} ^ {a , b} + V _ {y} ^ {a , b} + V _ {z} ^ {a , b}}{N _ {a , b}}, \tag {2}
$$

where  $a$  and  $b$  represent the two subspaces,  $V_{i}^{a,b} = |\langle \sigma_{i}\otimes \sigma_{i}\rangle |, i = \{x,y,z\}$  are the interference visibilities measured in the Pauli bases and  $N_{a,b}$  is a normalization factor. Figure 4d shows the measured interference visibilities for all combinations of the Pauli measurements, taking the OAM-path entangled state as an example. In Fig. 4e, we estimated the  $W$  value to be 27.(2), which exceeds the upper bound of 25 for

four-dimensional entanglement, thus successfully verifying the genuine five-dimensional entanglement.

In this work, we have successfully demonstrated entangled vortex emitters using programmable integrated photonics. This device combines the benefits of path entanglement with universal controllability and OAM entanglement with high resilience in free space, enabling the preparation, manipulation and modulation of various quantum vortex states. This demonstration of integrated entangled vortex emitters is the result of the collaborative development of integrated quantum photonics $^{40}$  and classical free-space beam-structuring technologies in silicon photonics $^{31-34}$ . The integration of these advanced technologies, along with the intricate preparation, manipulation, conversion and measurement of path and OAM quantum states, establishes the foundation for our work.

In the future, the capability of the device to emit vortices with a higher dimensionality per photon could be enhanced via optimization of the linear-optic circuits $^{37,45}$  and path-to-OAM converters. The number of entangled vortices can be increased by incorporating multiphoton multidimensional path-entanglement techniques $^{39}$ . The reverse functionality of the OAM emitter can serve as an integrated OAM receiver or mode sorter $^{46,48}$  for entanglement detection, facilitating the connection of a chip-to-chip quantum system via free space $^{15,16}$  or an OAM fibre $^{54,55}$ . Enhancing the OAM conversion efficiency is crucial for practical applications and hinges on advancements in integrated photonics (see Supplementary Notes 4 and 5). In a broader context, interfacing free space thorough controllable integrated quantum photonic circuits is vital for a range of practical quantum applications. The adoption of chip-to-free-space interfaces offers the potential to process quantum information on a chip and regulate the transmission of quantum information beyond the chip, which could find practical

applications in quantum communication and networks $^{35,44}$ . When combined with high-speed modulation and beam steering $^{32,33}$ , this could enable applications such as quantum light detection and ranging, quantum imaging and metrology. Furthermore, by emitting entangled vortices into free space, spatially structured quantum light fields can be generated for quantum state storage $^{13,14}$  and trapped-ion quantum computing with integrated optics $^{56}$ .

# Online content

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41566-025-01620-5.

# References

1. Mair, A., Vaziri, A., Weihs, G. & Zeilinger, A. Entanglement of the orbital angular momentum states of photons. Nature 412, 313-316 (2001).  
2. Verbeeck, J., Tian, H. & Schattschneider, P. Production and application of electron vortex beams. Nature 467, 301-304 (2010).  
3. Luski, A. et al. Vortex beams of atoms and molecules. Science 373, 1105-1109 (2021).  
4. Allen, L., Beijersbergen, M. W., Spreeuw, R. J. C. & Woerdman, J. P. Orbital angular momentum of light and the transformation of Laguerre-Gaussian laser modes. Phys. Rev. A 45, 8185-8189 (1992).  
5. Erhard, M., Krenn, M. & Zeilinger, A. Advances in high-dimensional quantum entanglement. Nat. Rev. Phys. 2, 365-381 (2020).  
6. Shen, Y. et al. Optical vortices 30 years on: OAM manipulation from topological charge to multiple singularities. Light Sci. Appl. 8, 90 (2019).  
7. Dada, A. C., Leach, J., Buller, G. S., Padgett, M. J. & Andersson, E. Experimental high-dimensional two-photon entanglement and violations of generalized Bell inequalities. Nat. Phys. 7, 677-680 (2011).  
8. Designolle, S. et al. Genuine high-dimensional quantum steering. Phys. Rev. Lett. 126, 200404 (2021).  
9. Fickler, R. et al. Quantum entanglement of high angular momenta. Science 338, 640-643 (2012).  
10. Krenn, M. et al. Generation and confirmation of a  $(100 \times 100)$ -dimensional entangled quantum system. Proc. Natl Acad. Sci. USA 111, 6243-6247 (2014).  
11. Malik, M. et al. Multi-photon entanglement in high dimensions. Nat. Photon. 10, 248-252 (2016).  
12. Erhard, M., Malik, M., Krenn, M. & Zeilinger, A. Experimental Greenberger-Horne-Zeilinger entanglement beyond qubits. Nat. Photon. 12, 759-764 (2018).  
13. Ding, D.-S. et al. Quantum storage of orbital angular momentum entanglement in an atomic ensemble. Phys. Rev. Lett. 114, 050502 (2015).  
14. Parigi, V. et al. Storage and retrieval of vector beams of light in a multiple-degree-of-freedom quantum memory. Nat. Commun. 6, 7706 (2015).  
15. Sit, A. et al. High-dimensional intricacy quantum cryptography with structured photons. Optica 4, 1006-1010 (2017).  
16. Vallone, G. et al. Free-space quantum key distribution by rotation-invariant twisted photons. Phys. Rev. Lett. 113, 060503 (2014).  
17. Luo, Y.-H. et al. Quantum teleportation in high dimensions. Phys. Rev. Lett. 123, 070505 (2019).  
18. Hu, X.-M. et al. Experimental high-dimensional quantum teleportation. Phys. Rev. Lett. 125, 230501 (2020).  
19. Zhang, D., Feng, X., Cui, K., Liu, F. & Huang, Y. Generating in-plane optical orbital angular momentum beams with silicon waveguides. IEEE Photonics J. 5, 2201206 (2013).

20. Zheng, S. & Wang, J. On-chip orbital angular momentum modes generator and (de)multiplexer based on trench silicon waveguides. Opt. Express 25, 18492-18501 (2017).  
21. Ni, J. et al. Multidimensional phase singularities in nanophotonics. Science 374, eabj0039 (2021).  
22. Cai, X. et al. Integrated compact optical vortex beam emitters. Science 338, 363-366 (2012).  
23. Strain, M. J. et al. Fast electrical switching of orbital angular momentum modes using ultra-compact integrated vortex emitters. Nat. Commun. 5, 4856 (2014).  
24. Miao, P. et al. Orbital angular momentum microlaser. Science 353, 464-467 (2016).  
25. Zhang, Z. et al. Tunable topological charge vortex microlaser. Science 368, 760-763 (2020).  
26. Lu, X. et al. Highly-twisted states of light from a high quality factor photonic crystal ring. Nat. Commun. 14, 1119 (2023).  
27. Liu, Y. et al. Integrated vortex soliton microcombs. Nat. Photon. 18, 632-637 (2024).  
28. Chen, B. et al. Integrated optical vortex microcomb. Nat. Photon. 18, 625-631 (2024).  
29. Bogaerts, W. et al. Programmable photonic circuits. Nature 586, 207-216 (2020).  
30. Miller, D. A. B. Self-configuring universal linear optical component. Photonics Res. 1, 1-15 (2013).  
31. Fontaine, N., Doerr, C. & Buhl, L. Efficient multiplexing and demultiplexing of free-space orbital angular momentum using photonic integrated circuits. In Optical Fiber Communication Conference Paper OTu11.2 (Optica Publishing Group, 2012).  
32. Sun, J., Timurdogan, E., Yaacobi, A., Hosseini, E. S. & Watts, M. R. Large-scale nanophotonic phased array. Nature 493, 195-199 (2013).  
33. Bütow, J., Eismann, J. S., Sharma, V., Brandmüller, D. & Banzer, P. Generating free-space structured light with programmable integrated photonics. Nat. Photon. 18, 243-249 (2024).  
34. SeyedinNavadeh, S. et al. Determining the optimal communication channels of arbitrary optical systems using integrated photonic processors. Nat. Photon. 18, 149-155 (2024).  
35. Zheng, Y. et al. Multichip multidimensional quantum networks with entanglement retrievability. Science 381, 221-226 (2023).  
36. Ding, Y. et al. High-dimensional quantum key distribution based on multicore fiber using silicon photonic integrated circuits. npj Quantum Inf. 3, 25 (2017).  
37. Wang, J. et al. Multidimensional quantum entanglement with large-scale integrated optics. Science 360, 285-291 (2018).  
38. Huang, J. et al. Demonstration of hypergraph-state quantum information processing. Nat. Commun. 15, 2601 (2024).  
39. Bao, J. et al. Very-large-scale integrated quantum graph photonics. Nat. Photon. 17, 573-581 (2023).  
40. Wang, J., Sciarrino, F., Laing, A. & Thompson, M. G. Integrated photonic quantum technologies. Nat. Photon. 14, 273-284 (2020).  
41. Arrazola, J. M. et al. Quantum circuits with many photons on a programmable nanophotonic chip. Nature 591, 54-60 (2021).  
42. Maring, N. et al. A versatile single-photon-based quantum computing platform. Nat. Photon. 18, 603-609 (2024).  
43. Wang, J. et al. Chip-to-chip quantum photonic interconnect by path-polarization interconversion. Optica 3, 407-413 (2016).  
44. Llewellyn, D. et al. Chip-to-chip quantum teleportation and multi-photon entanglement in silicon. Nat. Phys. 16, 148-153 (2020).  
45. Clements, W. R., Humphreys, P. C., Metcalf, B. J., Kolthammer, W. S. & Walmsley, I. A. Optimal design for universal multiport interferometers. Optica 3, 1460-1465 (2016).  
46. Berkhout, G. C. G., Lavery, M. P. J., Courtial, J., Beijersbergen, M. W. & Padgett, M. J. Efficient sorting of orbital angular momentum states of light. Phys. Rev. Lett. 105, 153601 (2010).

47. Fontaine, N. K. et al. Laguerre-Gaussian mode sorter. Nat. Commun. 10, 1865 (2019).  
48. Mirhosseini, M., Malik, M., Shi, Z. & Boyd, R. W. Efficient separation of the orbital angular momentum eigenstates of light. Nat. Commun. 4, 2781 (2013).  
49. Fickler, R. et al. Interface between path and orbital angular momentum entanglement for high-dimensional photonic quantum information. Nat. Commun. 5, 4502 (2014).  
50. Shen, X. et al. Ultra-low-crosstalk silicon arrayed-waveguide grating (de)multiplexer with 1.6-nm channel spacing. Laser Photon. Rev. 18, 2300617 (2024).  
51. Doerr, C. R. & Buhl, L. L. Circular grating coupler for creating focused azimuthally and radially polarized beams. Opt. Lett. 36, 1209-1211 (2011).  
52. Goodman, J. W. & Lawrence, R. W. Digital image formation from electronically detected holograms. Appl. Phys. Lett. 11, 77-79 (1967).  
53. Zia, D., Dehghan, N., D'Errico, A., Sciarrino, F. & Karimi, E. Interferometric imaging of amplitude and phase of spatial biphoton states. Nat. Photon. 17, 1009-1016 (2023).  
54. Wong, G. K. L. et al. Russell excitation of orbital angular momentum resonances in helically twisted photonic crystal fiber. Science 337, 446-449 (2012).  
55. Ma, Z., Kristensen, P. & Ramachandran, S. Scaling information pathways in optical fibers by topological confinement. Science 380, 278-282 (2023).

56. Mehta, K. K. et al. Integrated optical multi-ion quantum logic. Nature 586, 533-537 (2020).  
57. Silverstone, J. W. et al. Qubit entanglement between ring-resonator photon-pair sources on a silicon chip. Nat. Commun. 6, 7948 (2015).  
58. Miloshevsky, A. et al. CMOS photonic integrated source of broadband polarization-entangled photons. Opt. Quantum 2, 254-259 (2024).  
59. Zhang, X. et al. Integrated silicon nitride time-bin entanglement circuits. Opt. Lett. 43, 3469-3472 (2018).  
60. Mahmudlu, H. et al. Fully on-chip photonic turnkey quantum source for entangled qubit/qudit state generation. Nat. Photon. 17, 518-524 (2023).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

© The Author(s), under exclusive licence to Springer Nature Limited 2025

$^{1}$ State Key Laboratory for Mesoscopic Physics, School of Physics, Peking University, Beijing, China.  $^{2}$ Department of Electrical and Electronic Engineering, The University of Hong Kong, Hong Kong, China.  $^{3}$ Institute of Microelectronics, Chinese Academy of Sciences, Beijing, China.  $^{4}$ State Key Laboratory for Modern Optical Instrumentation, College of Optical Science and Engineering, Ningbo Research Institute, International Research Center for Advanced Photonics, Zhejiang University, Hangzhou, China.  $^{5}$ Intelligent Optics & Photonics Research Center, Jiaxing Research Institute, Zhejiang University, Jiaxing, China.  $^{6}$ Frontiers Science Center for Nano-optoelectronics & Collaborative Innovation Center of Quantum Matter, Peking University, Beijing, China.  $^{7}$ Peking University Yangtze Delta Institute of Optoelectronics, Nantong, China.  $^{8}$ Collaborative Innovation Center of Extreme Optics, Shanxi University, Taiyuan, China.  $^{9}$ Hefei National Laboratory, Hefei, China.  $^{10}$ Present address: John A. Paulson School of Engineering and Applied Sciences, Harvard University, Cambridge, MA, USA.  $^{11}$ Present address: Department of Electrical Engineering, Yale University, New Haven, CT, USA.  $^{12}$ These authors contributed equally: Jieshan Huang, Jun Mao, Xudong Li, Jingze Yuan.  $\times$  e-mail: dxdai@zju.edu.cn; jww@pku.edu.cn

# Methods

# Device design

The integrated SFWM photon-pair sources are designed using 1.2-cm-long silicon waveguides with a cross-section of  $220 \times 450\mathrm{nm}$  (height  $\times$  width, respectively), where the phase-matching condition for the FWM process is closely met. In each SFWM source, the two generated degenerate single photons are bunched together. We conducted reverse Hong-Ou-Mandel (RHOM) interference to separate the two Fock photons. Supplementary Figure 1a illustrates the structure, which comprises two sources embedded in a Mach-Zehnder interferometer, resulting in an output state as follows:  $|\Psi\rangle = \cos \phi |\psi\rangle_{\mathrm{bunching}} + \sin \phi |\psi\rangle_{\mathrm{splitting}}$ , where the phase  $\phi$  is a tunable phase between the two sources,  $|\psi\rangle_{\mathrm{bunching}} = (|2\rangle_{\mathrm{t}}|0\rangle_{\mathrm{b}} - |0\rangle_{\mathrm{t}}|2\rangle_{\mathrm{b}})/\sqrt{2}$  and  $|\psi\rangle_{\mathrm{splitting}} = |1\rangle_{\mathrm{t}}|1\rangle_{\mathrm{b}}$  denote the bunching and anti-bunching biphoton states, respectively,  $|1\rangle$  and  $|2\rangle$  are the photon number states,  $|0\rangle$  is the vacuum state and the subscripts  $t$  and  $b$  refer to the top and bottom modes, respectively. Supplementary Figure 1c shows the measured anti-bunching term of the RHOM fringe. A high contrast  $C = 0.99(1)$  of the RHOM fringe was measured, where the contrast  $C$  is defined as  $(N_{\mathrm{max}} - N_{\mathrm{min}}) / (N_{\mathrm{max}} + N_{\mathrm{min}})$ , and  $N_{\mathrm{max}}$  and  $N_{\mathrm{min}}$  denote the maximal and minimal photon counts, respectively. By setting the phase to  $\phi = \pi/2$ , we enable the creation of a biphoton state in the two output modes of each source.

The path-OAM conversion in Fig. 1 involves the following components: a Fourier transform based on a Rowland circle, phase compensation using an array of phase shifters and linear-to-helical phase mapping via a circular grating. The Rowland circle is designed with a radius of  $65\mu \mathrm{m}$  (see the scanning electron microscope image in Fig. 1b) and comprises a free-propagation region that connects five input and 16 output waveguides. Within the Rowland circle, the input light imparts a linear phase gradient of  $2\pi m j / 16$  (where  $j = 1,2,\ldots 16$  denotes the output positions) onto the 16 outputs under a second-order approximation. This linear transverse phase gradient is dictated by the input state  $|m\rangle$ , where  $m = \{-2, -1,0,1,2\}$  signifies the input positions. We utilized three-dimensional finite-difference time-domain simulations to optimize the design of the Rowland circle. The simulation results show a distribution of 16 output intensities with a coefficient of variation (CV) of  $4.8\%$ , whereas experimental near-field measurements yielded a CV of  $11.7\%$  (see Supplementary Fig. 2b). Discrepancies between the simulation and experimental results could stem from fabrication errors and variations in the coupling efficiency across different regions of the circular grating. On the basis of our simulation findings, when the CV is less than  $15\%$ , the cross-talk induced by variations in the 16 output intensities can be disregarded (see Supplementary Fig. 2d), indicating that our devices meet this criterion adequately. Supplementary Figure 2c illustrates the simulated phase distributions of the 16 output spots for the  $l = 1$ -order OAM state, demonstrating a linear phase distribution that aligns with the OAM order. In addition, the circular gratings were engineered to vertically emit light beams at a wavelength of approximately  $1,550~\mathrm{nm}$ . These diffractive gratings were constructed using  $70~\mathrm{nm}$  shallow-etched waveguides with a period of  $575~\mathrm{nm}$  and a  $49\%$  duty cycle, meticulously designed to achieve phase matching through finite-difference time-domain simulations. The measured phase distributions are presented in Fig. 2 and Supplementary Fig. 5b.

# Device fabrication

We fabricated the integrated optical vortex entanglement devices using complementary metal-oxide-semiconductor (or CMOS) processes. The device was fabricated on a 200-mm silicon-on-insulator wafer comprising a 3-μm-thick buried oxide layer and a 220-nm-thick top silicon layer. To define the device patterns, we used a 248 nm deep-ultraviolet (DUV) photolithography process. Initially, a thin layer of positive photoresist was spun onto the wafer, and DUV lithography was used to delineate the full etching and shallow etching structures. The deep

etching structures, reaching a depth of  $220\mathrm{nm}$ , were responsible for forming the waveguides and free-propagation regions. On the other hand, the shallow etching structures, with a depth of  $70\mathrm{nm}$ , shaped the circular gratings and input/output gratings. These patterns were subsequently transferred to the silicon layer via a double inductively coupled plasma etching process. Subsequently, a  $1 - \mu \mathrm{m}$ -thick layer of cladding oxide  $(\mathrm{SiO}_2)$  was deposited via plasma-enhanced chemical vapour deposition (PECVD). This was followed by the deposition of a  $10\mathrm{-nm}$ -thick Ti glue layer, a  $20\mathrm{-nm}$ -thick TiN barrier layer, an  $800\mathrm{-nm}$ -thick AlCu alloy layer and a  $20\mathrm{-nm}$ -thick TiN anti-reflective layer. These layers were patterned using DUV lithography and etching to shape the electrodes (transmission lines typically with a width of  $10\mu \mathrm{m}$ ). An additional  $50\mathrm{nm}$  TiN layer was deposited using PECVD and patterned via DUV lithography and etching to create the resistive thermal-optic phase shifters (with a cross-section of  $50\mathrm{nm} \times 1\mu \mathrm{m}$  (height  $\times$  width, respectively)). Finally, a thin oxide layer was deposited via PECVD to safeguard the device. Pad windows were then opened for wire bonding by eliminating the deposited oxide layer and the TiN layer above the AlCu. An optical microscope image of the entangled vortex chip is shown in Fig. 1a, whereas scanning electron microscope images showing the on-chip Rowland circle and circular grating structures are provided in Fig. 1b,c.

# Measurement of optical vortex states in free space

The detection of OAM states and OAM entanglement was conducted using an off-chip system. This measurement set-up involved collecting the emitted beams using a high-numerical-aperture objective lens and performing standard OAM state analysis, which included two spatial light modulators, two apertures and two single-mode fibre couplers. As the state of polarization of the emitted OAM beams is azimuthally polarized, a combination of quarter-wave plates and polarizers was used to select the left- or right-hand polarized component of the OAM states and entangled states. The experimental set-up for the detection and measurement of entangled vortex states is shown in Supplementary Fig. 3.

On our current integrated devices, the two vortex emitters were designed and fabricated with a separation distance of  $1.3\mathrm{mm}$ . To capture and analyse one of the vortex beams, we used one  $\times 20$ , 2-cm long-working-distance objective lens along with free-space bulk optical components (see Supplementary Fig. 3). The rationale behind choosing this objective lens was to avert any potential collision with the bonded wires on the chip (for accessing electronic controls for quantum state manipulations). Using an objective lens with a long working distance and a large magnification led to the limited field of view. This means that a single lens was inadequate for efficiently capturing both vortex beams simultaneously. Moreover, the limited space between the two vortex emitters posed challenges in positioning two such objective lenses to capture both vortices effectively. In our experiment, the entanglement properties of the generated vortex beams can be characterized by individually detecting the two vortex states (see main text). However, for future practical quantum information applications, for example, quantum communications and networks, the efficient and simultaneous collection of two or more vortex beams is necessary.

We here discuss several potential solutions to address this issue for future implementations. First, advanced optoelectronic packaging that can eliminate the need for bonded wires in a more compact manner can obviate the need for long-working-distance objective lenses. In this case, replacing a single lens with an array of lens, which is already practical, enables the simultaneous detections of two or even multiple vortex beams. Moreover, redesigning the chip layout is an alternative approach. With the current chip layout shown in Fig. 1, the two vortex emitters are positioned on the same side of the chip, leaving insufficient space between them to accommodate two adjacent objective lenses for light collection simultaneously. In future layout designs, separating the two vortex emitters spatially to opposite sides of the chip with a

large space in between will enable the utilization of two distinct objective lenses for reception. Furthermore, in our current experiment, vortex beams are emitted vertically from the chip into free space and analysed using bulk-optic systems. This chip-to-free-space interface is also compatible with optical fibres. This means that the emitted OAM beams can be collected using fibres such as ring-core and OAM fibres, as demonstrated in previous studies[54,55]. Leveraging these fibres can circumvent the limitations associated with using objective lenses, enabling the simultaneous collection of multiple vortex beams. This approach could potentially provide solutions for chip-OAM fibre-chip systems for applications in quantum communications and quantum networking.

# Data availability

The main data that support the findings of this study are available within the Article and its Supplementary Information. Any additional data are available from the corresponding authors upon reasonable request.

# Code availability

The analysis codes will be made available from the corresponding authors upon reasonable request.

# Acknowledgements

We thank L. Chen and B. Guan for useful discussions. We acknowledge support from the Academic Divisions of the Chinese Academy of Sciences (no. 2020-XX02-B-026), the National Natural Science Foundation of China (nos. 12325410, 62235001, 11834010 and 12134001), the Innovation Program for Quantum Science and

Technology (no. 2021ZD0301500), the National Key R&D Program of China (no. 2019YFA0308702) and the Beijing Natural Science Foundation (Z220008).

# Author contributions

J.W. conceived the project. J.H., X.L., D.D. and J.W. designed the entangled vortex chips. J.H., J.M., X.L., J.Y., Y.Z., C.Z., X.C., T.D., Z.F. and J.B. carried out the experiments. J.H., J.M., X.L. and J.Y. performed the simulations and carried out the theoretical analysis. Y.Y., D.D., Y.L., Q.G. and J.W. managed the project. J.H., J.M., X.L., J.Y. and J.W. wrote the manuscript with input from all authors. All of the authors discussed the results and contributed to the manuscript.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41566-025-01620-5.

Correspondence and requests for materials should be addressed to Daoxin Dai or Jianwei Wang.

Peer review information Nature Photonics thanks Lorenzo Marrucci and Qiwen Zhan for their contribution to the peer review of this work.

Reprints and permissions information is available at www.nature.com/reprints.