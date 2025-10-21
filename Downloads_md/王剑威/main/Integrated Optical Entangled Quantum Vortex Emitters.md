# Integrated Optical Entangled Quantum Vortex Emitters

Jianwei Wang

jianwei.wang@pku.edu.cn

Peking University https://orcid.org/0000-0003-1313-9266

Jieshan Huang

Peking University https://orcid.org/0000-0002-6227-6155

Jun Mao

Peking University https://orcid.org/0000-0002-4043-2313

Xudong Li

Harvard University

Jingze Yuan

Yale University

Yun Zheng

Peking University

Chonghao Zhai

Peking University

Tianxiang Dai

Peking University https://orcid.org/0000-0001-9735-8006

Zhaorong Fu

Peking University https://orcid.org/0000-0002-6575-4589

Jueming Bao

Peking University

Yan Yang

Chinese Academy of Sciences https://orcid.org/0000-0002-0940-7013

Daxin Dai

Zhejiang University https://orcid.org/0000-0002-2769-3009

Yan Li

Peking University https://orcid.org/0000-0003-0607-3166

Qihuang Gong

Peking University https://orcid.org/0000-0003-4974-6244

Keywords:

Posted Date: August 13th, 2024

DOI: https://doi.org/10.21203/rs.3.rs-4680169/v1

License: © This work is licensed under a Creative Commons Attribution 4.0 International License. Read Full License

Additional Declarations: There is NO Competing Interest.

Version of Record: A version of this preprint was published at Nature Photonics on February 28th, 2025. See the published version at https://doi.org/10.1038/s41566-025-01620-5.

# Integrated Optical Entangled Quantum Vortex Emitters

Jieshan Huang $^{1,\S}$ , Jun Mao $^{1,\S}$ , Xudong Li $^{1,\S,\dagger}$ , Jingze Yuan $^{1,\S,\ddagger}$ , Yun Zheng $^{1}$ , Chonghao Zhai $^{1}$ , Tianxiang Dai $^{1}$ , Zhaorong Fu $^{1}$ , Jueming Bao $^{1}$ , Yan Yang $^{2}$ , Daoxin Dai $^{3}$ , Yan Li $^{1,4,5}$ , Qihuang Gong $^{1,4,5}$ , Jianwei Wang $^{1,4,5*}$

$^{1}$  State Key Laboratory for Mesoscopic Physics, School of Physics, Peking University, Beijing, 100871, China  
 $^{2}$  Institute of Microelectronics, Chinese Academy of Sciences, Beijing 100029, China

<sup>3</sup> State Key Laboratory for Modern Optical Instrumentation, College of Optical Science and Engineering, Ningbo Research Institute, International Research Center for Advanced Photonics, Zhejiang University, Hangzhou 310058, China

$^{4}$  Frontiers Science Center for Nano-optoelectronics & Collaborative Innovation Center of Quantum Matter, Peking University, Beijing, 100871, China  
 $^{5}$  Hefei National Laboratory, Hefei 230088, China

† present address: John A. Paulson School of Engineering and Applied Sciences, Harvard University, Cambridge, MA, USA.

† present address: Department of Electrical Engineering, Yale University, New Haven, CT, USA

$\S$  These authors contributed equally to this work.  $\star$  emails to: jww@pku.edu.cn

Quantum vortices of light carrying orbital angular momentum stand as essential resources for quantum photonic technologies. Recent advancements in integrated photonics offer the potential to create and control quantum vortices using fully integrated circuits, eliminating the needs for intricate free-space alignment, modulation, and stabilization of bulky optical elements. However, generating quantum vortices in planar optical waveguides and circuits poses challenges, owing to the complexities of confining and guiding twisted photons, and importantly, the difficulties in preparing quantum superposition and entanglement of vortex states. Here, we report entangled quantum vortex emitters leveraging programmable integrated nanophotonic circuits. These circuits enable the generation and arbitrary control of resilient vortex-entanglement in free space, coherently converting from on-chip path-entanglement by a chip-free space interfacing technology. The emitters are plug-and-play, enabling swift reconfiguration within mere microseconds. Validation of multidimensional genuine entanglement is achieved through quantum tomography and dimension witnesses. Our work demonstrates integrated quantum vortex devices that combine the versatility of on-chip processing quantum information with the robustness of transmitting quantum vortices in free space, opening new avenues for applications in quantum communication, quantum light detection and ranging, quantum computation and storage.

Quantum vortices embody ubiquitous singular phases in light and matter $^{1-3}$ . Particularly, optical vortices carrying orbital angular momentum (OAM) in light beams and single photons, exhibit distinctive helical phase structures $^{4-7}$ , enabling them to potentially encode a large amount of quantum information. Extensive efforts have been made to explore quantum entanglement of optical vortices, leading to many significant achievements, e.g., in strong violation of nonlocality $^{8,9}$ , large-quanta entanglement $^{10,11}$ , multi-photon multidimension entanglement $^{12,13}$ , multimode quantum storage $^{14,15}$ , high-capability quantum key distribution $^{16,17}$  and teleportation $^{18,19}$ .

The ongoing advancement of quantum technologies with optical vortex demands fully integrated, robust, and rapidly reconfigurable OAM devices $^{5-7}$ . Integrated photonics offers a promising avenue for generating and manipulating optical vortices as demanded. However, planar optical waveguides and circuits face challenges in confining and guiding OAM modes owing to the difficulty in maintaining helical phases in non-circularly symmetric waveguides $^{20-22}$ . This limitation thus hinders the direct generation of quantum entanglement of OAM modes in waveguides, particularly when intricate nonlinear-optical processes for OAM are imposed. Alternatively, the emerging technology of chip-free space interfacing, combines the versatility of photonic circuits in waveguides with the robustness of beam shaping in free space, presenting a promising solution. By this technology, integrated devices can precisely control phases and amplitudes, enabling the free-space formation of helical beams by emitting multiple tailored beams out of waveguides, eventually twisting the wavefront. Pioneering efforts have encompassed both passive and reconfigurable approaches for tailoring the emitted beams. For example, a single microring with multiple passive grating emitters was realised for classical OAM emitters $^{23,24}$ , OAM lasers $^{25-27}$ , and OAM combs $^{28-30}$ . Programmable integrated photonic devices $^{31,32}$  with multiple individually reconfigurable phase emitters were explored to shape beams or vortices in free space, for classical telecommunication and light detection and ranging $^{33-36}$ , and for quantum communication $^{37,38}$ . Moreover, on a single quantum chip, capabilities have been demonstrated for generating and manipulating multidimensional multiphoton entanglement $^{39-42}$  and processing quan

tum information $^{42-45}$ , whereas going beyond a single quantum chip out to free space, entanglement distribution and teleportation of polarised $^{46,47}$  and spatial modes $^{37}$  have been reported. Despite of the remarkable progress in reconfigurable light control in waveguide circuits and free-space light beam shaping, generating entanglement of vortex states in integrated optical devices still remains experimental challenging.

In this work, we report the first entangled vortex emitter in programmable integrated photonic circuits. This is achieved by demonstrating fully integrated optical chip-free space quantum interfaces, that can coherently convert the robust on-chip path-entanglement to the OAM-entanglement that can reliably transmit in free space. The integrated device can perform a Fourier transform on the waveguide modes at different positions to generate a transverse phase gradient and map this linear phase to helical phase, emitting the entangled vortices into free space. The device integrates all components for plug-and-play vortex-entanglement generation, and it allows arbitrary and rapid operating of five-mode OAM-entanglement by manipulating path-entanglement using universal multimode interferometers. The integrated entangled vortex devices, that can be further scaled up to a larger dimension and more vortices, can find many possible applications in practical quantum communication, quantum light detection and ranging, multimode quantum storage, and light-atom based quantum computing.

We propose a scheme of generating entangled quantum vortices. It first creates a multi-qudit path-entangled state<sup>42</sup> where every qudit is prepared across a number of  $m$  waveguiding paths or modes, and it then converts the state to a multi-qudit OAM-entangled state where every qudit has a topological charge of  $l$ . A coherent conversion of path-entanglement and OAM-entanglement is shown:

$$
\frac {1}{\sqrt {d}} \sum_ {m} | m \rangle^ {\otimes n} \rightarrow \frac {1}{\sqrt {d}} \sum_ {l} | l \rangle^ {\otimes n}, \{m, l \} \in \left[ - \frac {d - 1}{2}, \dots , 0, \dots \frac {d - 1}{2} \right] \tag {1}
$$

where  $|m\rangle$  is the logical basis of path-encoded quuds,  $|l\rangle$  is the logical basis of OAM-encoded quuds,  $n$  represents the number of quuds, and  $d$  is the local size of every qudit ( $d$  is chosen as an odd integer). This scheme allows the generation of an array of entangled vortices

![](images/b2d3440a7bc3baddc7a92686ec0a7fd41330ffcb9a444f44ef72cc71fc345ff7.jpg)

![](images/b0e40a50361ba4e8df4a89e9a5126582ba26183b1763d4d9ce403193dc4297f1.jpg)  
Figure 1 Generating quantum vortex entanglement with programmable integrated nanophotonics. (a), Optical microscope image of the entangled vortex chip. The chip based on silicon nanophotonics monolithically integrates an array of SFWM photon-pair sources, two sets of universal linear-optic circuits, and two path-to-OAM converters. One pair of degenerate photons (red colored) are generated in the integrated SFWM sources by externally dichromatic excitations (blue and purple colored), which are subsequently routed by a mesh of crosers, resulting in the preparation of path-encoding 5-dimensional Bell state. The linear-optic circuits having squarely nested Mach-Zehnder interferometers (MZIs) are fully reprogrammable, allowing arbitrary manipulations of the 5-dimensional path-entanglement. The two path-OAM converters, each of which consists of Fourier transform in a Rowland circle, phase compensation by an array of optical phase shifters, and linear-to-helical phase mapping by a circular grating, emit the entangled vortices to free-space for the entanglement detection. The chip is wire bounded (gold wires) for reconfigurable operations. (b) and (c), Scanning electron microscope (SEM) images for on-chip Rowland circle and circular grating structures. The Rowland circle is embedded in a free propagation region with 5 input and 16 output waveguides (see zoom-in insets), performing the Fourier transform on the path mode  $|m\rangle$  in the  $m$ -th input to the superimposed mode (indicated by the blue dashed line) with the transverse phase gradient of  $2\pi m j / N$  at the  $j$ -th output. The circular gratings implement linear-to-helical mapping, forming an helical wavefront  $e^{-il\phi}$  in free space. They are formed by concentrically etched gratings with a period of  $575\mathrm{nm}$  and a  $49\%$  duty cycle (see zoom-in inset). To reduce losses, tapering structures are used to connect single-mode waveguides with the Rowland circle and circular grating.

with a number of  $n$  vortices and a local size of  $d$ . Importantly, pathentanglement could be arbitrarily operated by universal linear-optic circuits, so that arbitrary OAM-entanglement can be generated with integrated optics, beyond any other possible approaches.

Figure 1 shows an integrated-optic device for generating and manipulating two-vortices entanglement possessing a local size of five, as an example. Five-dimensional path-entangled qudits are generated by coherently exciting spontaneous four-wave-mixing (SFWM) sources that produce two degenerated single photons (see Fig.S1) $^{39}$ . The path-qudits can be individually manipulated by five-mode universal linear-optic circuits $^{48}$ , yielding arbitrary operations of path-entanglement. One key device is the integrated path-to-OAM converter that works as the chip-free space interface, that can be considered as a fully integrated version of the bulk-optic mode sorter $^{49,50}$  that has been widely used for efficient OAM detection $^{51}$  and OAM entanglement generation $^{52}$ . Our integrated path-to-OAM converter includes three stages: i, Fourier transform in an on-chip Rowland circle $^{53}$ , that transforms the path mode  $|m\rangle$  at the  $m$ -th input waveg

uide (a total number of  $d$  inputs) to the superimposed mode with a transverse phase gradient of  $2\pi m j / N$  at the  $j$ -th output waveguides  $(j \in [0,1,\dots,N-1]$ , and  $N = 16$  is the number of outputs), see Fig.1b. ii, phase compensation that compensate phase distortions from fabrications using an array of individually tunable phase shifters (Fig.1a). iii, mapping from the transverse (linear) phase gradient to the angular (helical) phase gradient, by uniformly positioning the  $N$ -beams around a diffractive circular grating (Fig.1c) $^{54}$ . The emitted photon possesses a helical wavefront  $e^{-il\phi}$  ( $\phi$  is the azimuthal angle in the cylindrical coordinate system) in the far field, which essentially generating the vortex carrying  $|l\rangle$ -order OAM where  $l = m$ . That is being said, the path mode  $|m\rangle$  is exactly converted to the OAM mode  $|l\rangle$ . We implemented the path-OAM one-to-one conversion with entire quantum coherence, which is essential to the flexible realisation of superposition and entanglement of OAM states with integrated optics. By programming path-entanglement, the Fig.1 device allows generation of arbitrary two-vortices five-dimensional entanglement.

![](images/270ebfea54920681bdfca5e50578fc66880c8df8d4adc17ff4bce81f7e1b8aa7.jpg)

![](images/45082bfe2bdd4f3fdfbc0d9e20dcd15196f4453d3728c81e4f427b372327b575.jpg)

![](images/27efe1ec59bb4408a2c0395eaae08f0fe194f295aef9b540d9cc0e1a0b377913.jpg)

![](images/d76736ed8acd985e982106585a380f5c537449f540b7e78e91b36ee42d88798b.jpg)

![](images/67249db48732e2dfb9170796c94e5ce047302cfaf9b2379022100fd06cccb60f.jpg)  
Figure 2 Characterisations of the integrated-optical path-OAM interface. (a)-(d), Reconstructed near-field phase distributions of the circular grating using digital off-axis holography. Bright spots represent the emitted beams carrying phase gradient of  $2\pi m j / N$ . The gradient phases in (c) and (d) form the twisted phasefront  $e^{-il\phi}$  in far field. Colors represent phases and brightnesses represent light intensities. (e)-(h), Experimental path-input OAM-output matrices for two vortices (devices 1 and 2). The matrices are characterised in the computational Z-basis  $|k\rangle_{m / l}^{Z}$  and the superposition F-basis  $|k\rangle_{m / l}^{F} = \frac{1}{\sqrt{5}}\sum_{j}e^{i\frac{2\pi}{5}jk}|j\rangle_{m / l}$ , where  $k = \{0,\pm 1,\pm 2\}$ , and subscripts  $m,l$  represent the logical basis of path and OAM states. Colors in each grid of matrices represent measured crosstalk ratios. The crosstalk can be characterised by classical statistic fidelity,  $\mathrm{Fid}_c = (\sum_i\sqrt{p_iq_i})^2$ , where  $p_i$  and  $q_{i}$  are experimental and theoretical distributions.

![](images/26da353c0b5dee1bc06f96ed37894c14aca341a22bcfd60c14134da10efb1b57.jpg)

![](images/c001e56a57e7cf4d56cf3996e17384305f8c95d75dfbe4d6b842acc691bc022f.jpg)

![](images/3617178394dd8a9eeecccdd16bce4b3a341ec2e09477fe9e75d6e8c2a1d93ccf.jpg)

![](images/320e1e58ddb2d7fc704e4571b4bda7868b9c54703f25a40c44d3a2596b4d44be.jpg)

![](images/1525ebc1ef6ecb7bee26fb7dbe4e9110642c3b5789368151c0c5a2ba3e15920e.jpg)

![](images/012ab82bb2af183a67629ede0bc04cf591c2171fd446bf58e3f1f4da48436789.jpg)

![](images/3ac126988ab6df88f81e8fe4fc95d2559ce3be598166650931bc152ff04b885e.jpg)  
Figure 3 Interferometric measurement and reprogramming of OAM modes. (a), Interference patterns between an OAM eigenmode and a Gaussian beam. The OAM states are identified by the number and chirality of spiral arms. (b), Experimental and simulated far-field intensity patterns of generated OAM eigenmodes and OAM equal superposition modes. For example, the patterns in the white dashed boxes represent a superposition state of  $(| - 2\rangle_{l} + |1\rangle_{l}) / \sqrt{2}$ . (c), Coherent rotation of OAM superposition states, by swapping the internal phase  $\theta$  between the two OAM modes and all-five OAM modes. Points are experimental data (collected having a fixed projection in the SLM), and curves are fitting lines. Insets are captured and simulated patterns at different  $\theta$ . Contrast  $C$  is defined as  $(N_{\mathrm{max}} - N_{\mathrm{min}}) / (N_{\mathrm{max}} + N_{\mathrm{min}})$ , where  $N_{\mathrm{max}}$  and  $N_{\mathrm{max}}$  denote maximal and minimal power. (d), Dynamic reconfiguring of OAM states by operating the linear-optic circuits. They were driven by a sequence of square waves with a repetition rate of  $5\mathrm{kHz}$ , a duty cycle of  $20\%$ , and a delay of  $40\mu s$  between each. The rise-time, the time interval it takes the signal to go from  $10\%$  to  $90\%$  of its final intensity, is measured to be around  $7.0\mu s$ .

![](images/488feba88bc53fce0de4cf0368ff23cf8368dbc01be28236d0e56cbdb1306f18.jpg)

![](images/c3d52df590fcae49c502732d2f7605e97ea193c8758ac5fbad0dfe01e2bedd60.jpg)

![](images/417a37790165e622d2f89313615fce1ca631b7ac6acf9d87727a6cbd6a7e1eca.jpg)

![](images/a2e0cb4186d91fa5338dae606f05179ccb768793c3429534c443b79584a5eab5.jpg)  
Figure 4 Measurement and verification of multidimensional entanglement. Experimentally reconstructed density matrices: (a), path-path entangled state  $\rho_{\mathrm{path - path}}$ ; (b), OAM-path entangled state  $\rho_{\mathrm{oam - path}}$ ; (c), OAM-path entangled state  $\rho_{\mathrm{oam - oam}}$ . Quantum state tomographic measurements using the compress sensing techniques were implemented to reconstruct the density matrices. The  $\rho_{\mathrm{oam - oam}}$  in (c) was obtained by applying the measured transfer matrix  $M_2$  to the measured  $\rho_{\mathrm{oam - path}}$  in (b). Column heights represent the absolute values  $|\rho|$  while colors represent the phases  $|\operatorname{Arg}(\rho)|$ . Phases for matrix elements with  $|\rho_{ij}| \leq 0.01$  are not displayed for clarity. The quantum state fidelity  $\mathrm{Fid}_q$  is defined as  $(\mathrm{Tr}[\sqrt{\sqrt{\rho_0} \cdot \rho \cdot \sqrt{\rho_0}}])^2$ , where  $\rho_0$  and  $\rho$  are ideal and measured states. (d) and (e), Experimental results for the five-dimensional entanglement witness. The visibilities  $V_i^{a,b} = |\langle \sigma_i \otimes \sigma_i \rangle|$  where  $i \in \{x, y, z\}$  and  $\{a, b\} \in [-2, -1, 0, 1, 2]$ , are measured in the Pauli bases  $\{\sigma_x, \sigma_y, \sigma_z\}$  indicated by colored regimes. In (d) and (e), colored bars are experimental results, shaded areas represent error bars, and dashed boxes are theoretical values. The measured  $W$  values is estimated to be 27.(2), exceeding the upper bound of 25 for the four-dimensional entanglement (indicated by the orange line). Values in parentheses in (a)-(c) and error bars in (d) and (e) indicate  $\pm 1\sigma$  uncertainty, estimated from Poissonian photon statistics.

![](images/1c7cd3e11469147ad89aab475407909362b2b88446b3bbc43c48a2c29699ce23.jpg)

We first characterise the integrated-optic path-OAM converter. A digital off-axis holography $^{55,56}$  was used to read out the phase distributions of the emitted OAM light from the circle gratings (Fig.S3a). Figures 2a-d show the holography-measured phase-front distributions for the OAM beams before and after phase compensation. Random phase errors from fabrication have been well compensated, by individually optimising the optical phases in the long waveguides connecting Fourier transform and linear-helical mapping. For those  $l = \{0,1,2\}$ -order OAM modes shown in Figs.2b-d, their uniformly distributed helical phase gradient  $2\pi l / N$  are confirmed (also see linear fitting in Fig.S3b). Moreover, we characterise the modal crosstalk of the emitted OAM beams, by performing projective measurement at different OAM basis (i.e., the computational Z-basis and superposition F-basis) using a spatial light modulator (SLM), see Fig.S3c. An adaptive moment estimation optimiser was used to optimise the phases to further reduce modal crosstalk, including those from path-state preparation, to path-OAM conversion, and to OAM detection. Figures 2e-h report measured path-input OAM-output matrices for two vortices. Results show the matrices with a classical statistic fidelity of 0.97(2). Note that the setting of phase compensators is to be fixed after calibration, with no needs of further operations in the entanglement generation, manipulation and measurement.

Interferometric measurement is performed to classically characterise the generated OAM beams, by co-axis interfering with a Gaussian reference beam. Interference patterns for the OAM eigenmodes are shown in Fig.3a, from which the OAM changes  $l$  can be directly read out from the number and chirality of spiral arms. Experimental results are in good agreement with simulations, indicating the generation of high quality OAM beams by selective path-to-OAM conversion. The generated light in fact is vectorial vortex beam, where its polarization state is azimuthally polarized. The measurement of

OAM modes is decomposed to those with left-hand and right-hand polarization. In experiment, we detected the left-hand component of OAM states and entangled states. For the ease of reading, in this work, we define the  $l$  by interference patterns. Higher order OAM beams can be generated by shifting the on-chip phases (see Fig.S4).

To generate arbitrary OAM superposition states by controlling the integrated multimode unitary operators, we measured all two-mode superposition states in Fig.3b. Measured and simulated mode profiles are in good agreement. A continuous rotation of the OAM superposition state was measured by on-chip sweeping the internal phase  $\theta$  while keeping the projection basis. High-contrast quantum coherence is observed in Fig.3c. We also characterise the full-five-mode OAM superposition state of  $\sum_{l}e^{\frac{2\pi l}{5}\theta}|l\rangle$ . At the valleys of the interference fringe, it returns the Fourier superposition modes, whose orthogonality is imaged by interference patterns. Moreover, to demonstrate dynamic control of the OAM states, a sequence of square waves was applied to on-chip linear-optic circuits to rapidly reconfigure the generation of vortices switching between different modes. Experimental results in Fig.3d show a sequential excitation of the five OAM states, with a rise-time of about  $7.0\mu s$ .

We then characterise and certificate multidimensional entanglement. We reconstruct the initial path-path entangled state  $\rho_{\mathrm{path - path}}$  before conversion (see Fig.4a), and the OAM-path entangled state  $\rho_{\mathrm{oam - path}}$  (see Fig.4b), by performing the quantum state tomographic measurements. The OAM-path entanglement can be used for chip-to-chip multidimensional entanglement distributions, keeping one path-qudit on chip while transmitting another OAM-qudit through free space, and vice versa[37]. When reconstructing the OAM-OAM entanglement, the two entangled vortices that separately emit OAM photons, need to be simultaneously collected and locally measured. In our experiment setup, the field of view for a long working dis

tance objective lens is limited, so that the two vortices cannot be efficiently collected at the same time. We instead reconstructed the density matrix for OAM-OAM entangled state by leveraging the transfer matrices of path-OAM conversions. The measured transfer matrices  $(M_{1}$  and  $M_2)$  for the two channels of path-to-OAM conversion are provided in Fig.S6. Having that, the OAM-path entangled state  $\rho_{\mathrm{oam - path}}$  can be inferred from  $\rho_{\mathrm{path - path}}$  and  $M_{1}$  in Fig.S7, which is consistent with the tomography result in Fig.4b. Their compatibility confirms the validity of verifying OAM entanglement. Thus, by applying the  $M_2$  to the measured state  $\rho_{\mathrm{oam - path}}$ , it allows the reconstruction of density matrix for the entangled vortices. The  $\rho_{\mathrm{oam - oam}}$  result for OAM-OAM entangled state is reported in Fig.4c, and its the quantum state fidelity is estimated to be 0.87(6).

We characterised the entanglement dimension witness for multidimensional entangled states. The dimension witness observable  $W$  is defined as the sum of interference visibility in all two-dimensional subspaces<sup>11</sup>:

$$
W = \sum_ {a = 0} ^ {d - 2} \sum_ {b = a + 1} ^ {d - 1} \frac {V _ {x} ^ {a , b} + V _ {y} ^ {a , b} + V _ {z} ^ {a , b}}{N _ {a , b}}, \tag {2}
$$

where  $a$  and  $b$  represent the two subspaces,  $V_{i}^{a,b} = |\langle \sigma_{i}\otimes \sigma_{i}\rangle |,i = \{x,y,z\}$  are the interference visibilities measured in the Pauli bases, and  $N_{a,b}$  is a normalization factor. Figure 4d shows measured interference visibilities for all combinations of the Pauli measurements, taking the OAM-path entangled state as an example. In Fig.4e, we estimate the  $W$  values of 27.(2), exceeding the upper bound of 25 for the four-dimensional entanglement, thus successfully verifying the genuine five-dimensional entanglement.

In this work, we have successfully demonstrated entangled vortex emitters using programmable integrated photonics. This device combines the benefits of path-entanglement with universal control-lability and OAM-entanglement with high resilience in free space, allowing for the preparation, reprogramming, and modulation of various quantum vortex states. The size of vortices can be increased by optimising linear-optic circuits $^{39,48}$  and path-OAM converters, while the number of entangled vortices can be expanded through the adoption of multi-photon multidimension path-entanglement $^{42}$ . The reverse functionality of the OAM emitter can serve as an OAM receiver for entanglement detection, facilitating the connection of a chip-to-chip quantum system via free space $^{16,17}$  or OAM fiber $^{57,58}$ . As the integrated mode sorter, an efficient on-chip detection of OAM entanglement is possible $^{49,51}$ . In general, the utilization of chip-free space interfaces provides the potential to process quantum information on chip and control the transmission of quantum information beyond chips, which could find practical applications in quantum communication and networking $^{37,47}$ . When combined with high-speed modulation $^{59}$  and beam steering $^{34,35}$ , it could enable applications such as quantum light detection and ranging, quantum imaging and metrology. Furthermore, by emitting entangled vortices into free space, spatially-structured quantum light fields can be generated for quantum state storage $^{14,15}$ , and trapped ion quantum computing $^{60}$  with integrated optics.

# References

1. A. Mair, A. Vaziri, G. Weihs & A. Zeilinger. Entanglement of the orbital angular momentum states of photons. Nature 412, 313-316 (2001).  
2. J. Verbeeck, H. Tian & P. Schattschneider. Production and application of electron vortex beams. Nature 467, 301-304 (2010).  
3. A. Luski et al. Vortex beams of atoms and molecules. Science 373, 1105-1109 (2021).

4. L. Allen, M. W. Beijersbergen, R. J. C. Spreeuw & J. P. Woerdman. Orbital angular momentum of light and the transformation of Laguerre-Gaussian laser modes. Phys. Rev. A 45, 8185-8189 (1992).  
5. M. Erhard, M. Krenn & A. Zeilinger. Advances in high-dimensional quantum entanglement. Nat. Rev. Phys. 2, 365-381 (2020).  
6. Y. Shen et al. Optical vortices 30 years on: OAM manipulation from topological charge to multiple singularities. Light: Sci. & App. 8, 90 (2019).  
7. C. He, Y. Shen & A. Forbes. Towards higher-dimensional structured light. Light: Sci. & App. 11, 205 (2022).  
8. A. C. Dada, J. Leach, G. S. Buller, M. J. Padgett & E. Andersson. Experimental high-dimensional two-photon entanglement and violations of generalized Bell inequalities. Nat. Phys. 7, 677-680 (2011).  
9. S. Designolle et al. Genuine high-dimensional quantum steering. Phys. Rev. Lett. 126, 200404 (2021).  
10. R. Fickler et al. Quantum entanglement of high angular momenta. Science 338, 640-643 (2012).  
11. M. Krenn et al. Generation and confirmation of a  $(100 \times 100)$ -dimensional entangled quantum system. Proc. Natl. Acad. Sci. U.S.A. 111, 6243-6247 (2014).  
12. M. Malik et al. Multi-photon entanglement in high dimensions. Nat. Photon. 10, 248-252 (2016).  
13. M. Erhard, M. Malik, M. Krenn & A. Zeilinger. Experimental Greenberger-Horne-Zeilinger entanglement beyond qubits. Nat. Photon. 12, 759-764 (2018).  
14. D.-S. Ding et al. Quantum storage of orbital angular momentum entanglement in an atomic ensemble. Phys. Rev. Lett. 114, 050502 (2015).  
15. V. Parigi et al. Storage and retrieval of vector beams of light in a multiple-degree-of-freedom quantum memory. Nat. Commun. 6, 7706 (2015).  
16. A. Sit et al. High-dimensional intracity quantum cryptography with structured photons. Optica 4, 1006 (2017).  
17. G. Vallone et al. Free-space quantum key distribution by rotation-invariant twisted photons. Phys. Rev. Lett. 113, 060503 (2014).  
18. Y.-H. Luo et al. Quantum teleportation in high dimensions. Phys. Rev. Lett. 123, 070505 (2019).  
19. X.-M. Hu et al. Experimental high-dimensional quantum teleportation. Phys. Rev. Lett. 125, 230501 (2020).  
20. D. Zhang, X. Feng, K. Cui, F. Liu & Y. Huang. Generating in-plane optical orbital angular momentum beams with silicon waveguides. IEEE Photonics Journal 5, 2201206-2201206 (2013).  
21. S. Zheng & J. Wang. On-chip orbital angular momentum modes generator and (de)multiplexer based on trench silicon waveguides. Opt. Express 25, 18492-18501 (2017).  
22. J. Ni et al. Multidimensional phase singularities in nanophotonics. Science 374, eabj0039 (2021).  
23. X. Cai et al. Integrated compact optical vortex beam emitters. Science 338, 363-366 (2012).  
24. M. J. Strain et al. Fast electrical switching of orbital angular momentum modes using ultra-compact integrated vortex emitters. Nat. Commun. 5, 4856 (2014).  
25. P. Miao et al. Orbital angular momentum microlaser. Science 353, 464-467 (2016).  
26. Z. Zhang et al. Tunable topological charge vortex microlaser. Science 368, 760-763 (2020).  
27. J. Zhang et al. An InP-based vortex beam emitter with monolithically integrated laser. Nat. Commun. 9, 2652 (2018).

28. X. Lu et al. Highly-twisted states of light from a high quality factor photonic crystal ring. Nat. Commun. 14, 1119 (2023).  
29. Y. Liu et al. Integrated vortex soliton microcombs. Nat. Photon. (2024).  
30. B. Chen et al. Integrated optical vortex microcomb. Nat. Photon. (2024).  
31. W. Bogaerts et al. Programmable photonic circuits. Nature 586, 207-216 (2020).  
32. D. A. B. Miller. Self-configuring universal linear optical component. Photon. Res. 1, 1-15 (2013).  
33. N. K. Fontaine, C. R. Doerr & L. L. Buhl. Efficient multiplexing and demultiplexing of free-space orbital angular momentum using photonic integrated circuits in Optical Fiber Communication Conference (2012), OTu1I.2.  
34. J. Sun, E. Timurdogan, A. Yaacobi, E. S. Hosseini & M. R. Watts. Large-scale nanophotonic phased array. Nature 493, 195-199 (2013).  
35. J. Butow, J. S. Eismann, V. Sharma, D. Brandmüller & P. Banzer. Generating free-space structured light with programmable integrated photonics. Nat. Photon. 18, 243-249 (2024).  
36. S. SeyedinNavadeh et al. Determining the optimal communication channels of arbitrary optical systems using integrated photonic processors. Nat. Photon. 18, 149-155 (2024).  
37. Y. Zheng et al. Multichip multidimensional quantum networks with entanglement retrievalability. Science 381, 221-226 (2023).  
38. Y. Ding et al. High-dimensional quantum key distribution based on multicore fiber using silicon photonic integrated circuits. npj Quantum Inf. 3, 25 (2017).  
39. J. Wang et al. Multidimensional quantum entanglement with large-scale integrated optics. Science 360, 285-291 (2018).  
40. C. Vigliar et al. Error-protected qubits in a silicon photonic chip. Nat. Phys. 17, 1137-1143 (2021).  
41. J. Huang et al. Demonstration of hypergraph-state quantum information processing. Nat. Commun. 15, 2601 (2024).  
42. J. Bao et al. Very-large-scale integrated quantum graph photonics. Nat. Photon. 17, 573-581 (2023).  
43. J. Wang, F. Sciarrino, A. Laing & M. G. Thompson. Integrated photonic quantum technologies. Nat. Photon. 14, 273-284 (2020).  
44. J. M. Arrazola et al. Quantum circuits with many photons on a programmable nanophotonic chip. Nature 591, 54-60 (2021).  
45. N. Maring et al. A versatile single-photon-based quantum computing platform. Nat. Photon. 18, 603-609 (2024).  
46. J. Wang et al. Chip-to-chip quantum photonic interconnect by path-polarization interconversion. Optica 3, 407-413 (2016).  
47. D. Llewellyn et al. Chip-to-chip quantum teleportation and multi-photon entanglement in silicon. Nature Physics 16, 148-153 (2020).  
48. W. R. Clements, P. C. Humphreys, B. J. Metcalf, W. S. Kolthammer & I. A. Walmsley. Optimal design for universal multiport interferometers. Optica 3, 1460-1465 (2016).  
49. G. C. G. Berkhout, M. P. J. Lavery, J. Courtial, M. W. Beijersbergen & M. J. Padgett. Efficient sorting of orbital angular momentum states of light. Phys. Rev. Lett. 105, 153601 (2010).  
50. N. K. Fontaine et al. Laguerre-Gaussian mode sorter. Nature Communications 10, 1865 (2019).  
51. M. Mirhosseini, M. Malik, Z. Shi & R. W. Boyd. Efficient separation of the orbital angular momentum eigenstates of light. Nat. Commun. 4, 2781 (2013).  
52. R. Fickler et al. Interface between path and orbital angular momentum entanglement for high-dimensional photonic quantum information. Nat. Commun. 5, 4502 (2014).

53. X. Shen et al. Ultra-low-crosstalk silicon arrayed-waveguide grating (de)multiplexer with 1.6-nm channel spacing. *Laser & Photonics* Rev. **18**, 2300617 (2024).  
54. C. R. Doerr & L. L. Buhl. Circular grating coupler for creating focused azimuthally and radially polarized beams. Opt. Lett. 36, 1209-1211 (2011).  
55. J. W. Goodman & R. Lawrence. Digital image formation from electronically detected holograms. Appl. Phys. Lett. 11, 77-79 (1967).  
56. D. Zia, N. Dehghan, A. D'Errico, F. Sciarrino & E. Karimi. Interferometric imaging of amplitude and phase of spatial biphoton states. Nat. Photon. 17, 1009-1016 (2023).  
57. G. K. L. Wong et al. Excitation of orbital angular momentum resonances in helically twisted photonic crystal fiber. Science 337, 446-449 (2012).  
58. Z. Ma, P. Kristensen & S. Ramachandran. Scaling information pathways in optical fibers by topological confinement. Science 380, 278-282 (2023).  
59. C. Wang et al. Integrated lithium niobate electro-optic modulators operating at CMOS-compatible voltages. Nature 562, 101-104 (2018).  
60. K. K. Mehta et al. Integrated optical multi-ion quantum logic. Nature 586, 533-537 (2020).

# Acknowledgements

We thank L. Chen and B. Guan for useful discussions. We acknowledge support from the National Natural Science Foundation of China (nos. 12325410, 62235001, 11834010), the Innovation Program for Quantum Science and Technology (no. 2021ZD0301500), the National Key R&D Program of China (no. 2019YFA0308702), Beijing Natural Science Foundation (Z220008).

# Authors contributions:

J.W. conceived the project. J.H., J.M., X.L., and J.Y. equally contributed to this work. J.H. designed the entangled vortex chips. J.H., J.M., X.L., J.Y., Y.Z., C.Z., X.C., T.D., Z.F., and J.B., implemented the experiment. J.H., J.M., X.L., and J.Y. provided the simulations and performed the theoretical analysis. Y.Y., D.D., Y.L., Q.G., and J.W. managed the project. J.H., J.M., X.L., J.Y. and J.W. wrote the manuscript with input from all the authors. All the authors discussed the results and contributed to the manuscript.

# Competing interests:

The authors declare no competing interests.

# Data availability:

The data that support the findings of this study are available from the corresponding authors.

# Supplementary Files

This is a list of supplementary files associated with this preprint. Click to download.

- SupplementalMaterial.pdf