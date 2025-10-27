# Programmable photonic circuits

https://doi.org/10.1038/s41586-020-2764-0

Received: 17 March 2020

Accepted: 10 July 2020

Published online: 7 October 2020

Check for updates

Wim Bogaerts $^{1,2}$ , Daniel Pérez $^{3,4}$ , José Capmany $^{3,4}$ , David A. B. Miller $^{5}$ , Joyce Poon $^{6,7}$ , Dirk Englund $^{8}$ , Francesco Morichetti $^{9}$  & Andrea Mellon $^{9}$

The growing maturity of integrated photonic technology makes it possible to build increasingly large and complex photonic circuits on the surface of a chip. Today, most of these circuits are designed for a specific application, but the increase in complexity has introduced a generation of photonic circuits that can be programmed using software for a wide variety of functions through a mesh of on-chip waveguides, tunable beam couplers and optical phase shifters. Here we discuss the state of this emerging technology, including recent developments in photonic building blocks and circuit architectures, as well as electronic control and programming strategies. We cover possible applications in linear matrix operations, quantum information processing and microwave photonics, and examine how these generic chips can accelerate the development of future photonic circuits by providing a higher-level platform for prototyping novel optical functionalities without the need for custom chip fabrication.

Photonic integrated circuits (PICs) have recently become an established and powerful technology that supports many applications $^{1,2}$ . Like electronic integrated circuits, PICs are implemented on the surface of a chip, but they manipulate light instead of electrical signals, using on-chip optical waveguides, beam couplers, electro-optic modulators, photodetectors and lasers. Whereas electronic circuits are good at digital computations, photonics circuits are good at transporting and processing analogue information. Therefore, today PICs are mostly used in fibre-optic communications, but they are also useful in various applications in which light has an important role, such as chemical, biological or spectroscopic sensors, metrology, and classical and quantum information processing. Because most photonic circuits are tailored for one of these applications, they are called application-specific photonic integrated circuits (ASPICs) and, given that the flow of light is essentially fixed, they can be very compact and power-efficient.

Programmable PICs are based on the idea that the flow of light on the chip can be manipulated at run-time, for example, by electrically controlling tunable beam couplers connected by optical waveguides<sup>3</sup>. This way, light is distributed and spatially rerouted under software control. These chips can implement various linear functions by interfering signals along different paths, and they can define programmable wavelength filters<sup>3</sup>, which are essential building blocks for communication or sensor applications and for the manipulation of microwave signals in the optical domain<sup>4,5</sup>. When scaling up such meshes of connected waveguides, the interferences can perform linear optical computations, such as real-time matrix-vector products<sup>6-8</sup>. These are essential operations in quantum information processing<sup>9-12</sup>, neuromorphic computing and artificial intelligence<sup>6,7</sup>, and we are already seeing rapid development of programmable PIC technologies in these applications. As in electronics, programmability makes it possible to (re)configure the functionality at run-time, which lowers the economic and technological barriers to using the circuit and provides a path to upgradability.

In conventional optics, a system with even a few interferometric elements becomes difficult to line up, in terms of both space and wavelength. However, we can now fabricate complex interferometric systems on a chip, with architectures and algorithms for programming, stabilization and control. Some of these systems even allow self-configuration, adapting the circuit in real time to the optical problem being solved, without high-level calculations $^{8,13,14}$ . This combination of complex circuits and control techniques is opening the field of programmable photonics.

Here, we summarize recent developments in this emerging field. We start by explaining the core concepts of waveguide meshes and how they route light and perform analogue matrix and filtering operations. We then look at the necessary technologies for such photonic circuits. Because programmable PICs are more generic than ASPICs, they can be deployed in various applications, but there are some fields in which their unique capability to perform matrix and parallel operations is especially valuable. Based on this, we look at the future potential of programmable photonics.

# Mesh architectures and algorithms

In programmable photonic integrated circuits, the flow of light is controlled by waveguides connected in a mesh using  $2 \times 2$  blocks, or 'analogue gates', the on-chip equivalent of free-space optical beam splitters. The mesh connectivity determines the possible functions of the programmable circuit, and how it can be configured. Some architectures enable arbitrary matrix operations $^{4-6,8,12-31}$ , and can even automatically adapt to changing problems $^{8,13,14,29-32}$ .

We can separate waveguide meshes into two broad classes: (1) forward-only, where the light flows from one side of the mesh to the other $^{7,8,12,14,32,33}$  and (2) recirculating, where light can also be routed in loops and even back to the input ports $^{3,5,18,23}$ . Both architectures use the

<sup>1</sup>IMEC, Department of Information Technology, Ghent University, Ghent, Belgium. <sup>2</sup>Center of Nano- and Biophotonics, Ghent University, Ghent, Belgium. <sup>3</sup>Universitat Politecnica València, ITEAM Research Institute, Valencia, Spain. <sup>4</sup>Pronics, Programmable Photonics, Valencia, Spain. <sup>5</sup>Ginzton Laboratory, Stanford University, Stanford, CA, USA. <sup>6</sup>Max Planck Institute of Microstructure Physics, Halle, Germany. <sup>7</sup>Edward S. Rogers Department of Electrical and Computer Engineering, University of Toronto, Toronto, Canada. <sup>8</sup>Research Laboratory of Electronics, Massachusetts Institute of Technology, Cambridge, MA, USA. <sup>9</sup>Dipartimento di Elettronica, Informazione e Bioingegneria, Politecnico di Milano, Milan, Italy. <sup>e</sup>e-mail: wim.bogaerts@ugent.be

![](images/eb1f175fe4bfef08c0dd4d40cb0424c2aecb826f327292fd33db1b909f70a21d.jpg)  
Fig.1 | Universal  $2 \times 2$  optical gates. a, A  $2 \times 2$  optical gate mixes the modulated optical waves  $a_1$  and  $a_2$  from two input waveguides, controlling both the power coupling  $\kappa$  and the phase delay  $\Delta \phi$  of the output waves  $b_1$  and  $b_2$ . b, The gate can  
be tuned between 'bar' and 'cross' states.  $\mathbf{c} - \mathbf{e}$ , The gate can be implemented as a circuit with two degrees of freedom,  $p_1$  and  $p_2$ , such as an MZI with two optical phase shifters, or a tunable coupler with an additional phase shifter.

same building blocks: waveguides,  $2 \times 2$  couplers, and optical phase shifters that form the analogue optical gates.

# The basic block: a  $2 \times 2$  analogue optical gate

A  $2 \times 2$  optical gate projects the light from two input waveguides onto two output waveguides as a linear combination, as shown in Fig. 1. If all elements are lossless, this corresponds to a unitary transformation. The most common on-chip implementation is a Mach-Zehnder interferometer (MZI), shown in Fig. 1c, d, which needs at least two adjustable parameters  $p_1$  and  $p_2$  to independently control the power splitting  $\kappa$  and the relative phase delay  $\Delta \phi$ . This can be achieved with two optical phase shifters placed in different locations within the MZI (Fig. 1c, d). When the two fixed couplers in the MZI have a perfect 50:50 split ratio<sup>30,34</sup>, all coupling ratios from  $0\%$  (bar) to  $100\%$  (cross) are possible (Fig. 1b). An alternative  $2 \times 2$  gate combines a controllable coupler and one phase shifter<sup>35</sup> (Fig. 1e). These gates work for light flows in both the forward and backward directions. The  $2 \times 2$  gate is the key building block for the different mesh architectures that we discuss next.

# Forward-only meshes

In forward-only mesh networks, light flows in one direction, interfering in  $2 \times 2$  gates at every stage. This architecture allows a simple progressive setup—for example, based on minimizing or maximizing power on photodetectors—and in some cases self-configures to specific problems and self-stabilizes its operation $^{8,14,29-32,36}$ .

Figure 2a shows an example of a simple mesh with five waveguides entering a triangular mesh with 'diagonal lines' that can each be configured into a self-aligning beam coupler $^{29}$ . When coherent light is injected into the input waveguides of a  $2 \times 2$  gate,  $p_1$  and  $p_2$  can be sequentially adjusted so that the beams in the lower output waveguide fully cancel out. In Fig. 2a we adjust MZI11 to minimize the power onto detector D11, routing all the light into the upper output waveguide. We repeat this for MZI12, MZI13 and MZI14, thus combining all the light from waveguides 1-5 into output 1. This self-configuring algorithm works for any combination of amplitudes and phases in the input waveguides, and it can run in a repeating loop for real-time adaptation to varying inputs $^{8,14,29,31}$ .

We can cascade additional diagonal lines to perform more complex functions, essentially implementing any linear transformation matrix between inputs and outputs $^{8,29,33}$ . Detectors D11-D14 in Fig. 2a need to be almost transparent, passing most of the power to the next 'layer' of the circuit. Each successive layer can then be configured sequentially (see ref. $^{37}$  for a detailed discussion). Mathematically, amplitude

vectors, which are injected by adjusting the power and phase of the optical modes at the input ports, correspond to the rows of the desired matrix $^{30}$ . Physically, orthogonal input beams could be separated automatically by modulating unique tones on those beams that are then picked up by the corresponding detectors $^{31}$ .

There are alternative architectures of  $2 \times 2$  optical gates. A 'binary tree' architecture (Fig. 2d) can also be used as an adaptive beam coupler $^{29,32}$ . A rectangular architecture $^{12}$ , such as the one in Fig. 2e, also implements an arbitrary unitary matrix, and there are other architectures that we do not cover in this Review $^{38-40}$ . Although more compact than a triangular one, the rectangular architecture does not support the convenient self-configuration, but progressive configuration is still possible with embedded detectors $^{32,41}$ . Otherwise, additional optical circuits are needed to configure or calibrate the circuit $^{32,42,43}$ . For any of these meshes, once the circuit elements are calibrated, arbitrary settings can be programmed directly.

# Recirculating meshes

Recirculating meshes consist of waveguide loops coupled by  $2 \times 2$  optical gates, forming a regular two-dimensional (2D) grid. The loops can route light in any direction through the mesh, allowing us to program a full scattering matrix between all the waveguide ports. Compared to forward-only meshes, these meshes allow delays of discrete lengths (whole number of segments) to implement interferometric and resonant wavelength filters[5,44].

The loops can be connected in different topologies, including square $^{5}$ , hexagonal $^{44}$ , triangular $^{35}$  and alternative geometries $^{23}$ , as shown in Fig. 3. When evaluating these topologies $^{3}$  against integration metrics (such as footprint or gates per area) or functional metrics (such as reconfiguration capability, losses and the choice of filter periodicity), a hexagonal mesh is particularly attractive, especially because all ports can be used as input or output interchangeably. The mesh can be configured as a forward-only mesh (although with more gates) or it can be programmed as both a finite- and an infinite-impulse-response wavelength filter $^{44}$ . The number of unit cells in the mesh determines the number and type of functions that can be programmed. A larger mesh is more flexible but also induces higher optical losses. Figure 3d-f illustrates a two-cavity ring filter in a seven-cell hexagonal mesh. The free spectral range (FSR; the frequency spacing between two resonances) is inversely proportional to the optical roundtrip length, so we want the rings to be as small as possible. As an example, when each of the 'segments' in the mesh has an optical path length of  $\sim 1\mathrm{mm}$ , the

![](images/c9479e8f085af2ccef75ab7d64f5fe032e447b6845e144fde9c9160f009e773f.jpg)  
a Cascaded diagonal line  $\rightarrow$  triangular unitary

![](images/cdde89804fbd21bf825383fadd9921fe0cfd60d4491af92c68e36d7802fa9247.jpg)  
d Binary tree

![](images/fbbf437d54b71e69a2d4dc5a1ca1464b62fa7744fa7de47ab8a4b66e96839b2e.jpg)

![](images/8ba89c55fa3c489fd9f62918057dcc2f9208419ccba14ec01240ce32f3751957.jpg)

![](images/7bbb61140b52f361d77c09d9f3224e95c0092db4d5b478b6d34644c6f0508850.jpg)  
Fig.2|Forward-only meshes of  $2\times 2$  optical gates. a, Triangular  $5\times 5$  unitary circuits consisting of four diagonal lines of  $2\times 2$  optical gates (MZI11-MZI41) with transparent photodetectors (D11-D41) and one output waveguide. b, Four-channel diagonal-line mode 'unscrambler' with transparent detectors  
e Rectangular unitary  
(contactless integrated photonic probes, CLIPP). Image adapted from ref.  $^{31}$ , Springer Nature. c, Large-scale example with 26 input channels  $^{6,15}$ . Image adapted from ref.  $^{15}$ , Springer Nature. d, Binary-tree self-aligning beam couplers. e, Rectangular unitary architecture.

largest FSR possible in a hexagonal mesh would be  $\sim 50\mathrm{GHz}$ , which suits radiofrequency applications.

Because of the feedback loops, recirculating meshes cannot always be self-configuring (that is, adjusting themselves without external calculations), but they can be configured through pre-characterization or optimization methods<sup>13</sup>.

# Generic programmable photonics

Both forward-only and recirculating waveguide meshes can form the core of a generic programmable photonic circuit as in Fig. 4a. These structures are analogous to a field-programmable gate array (FPGA) in electronics $^{3,45}$ . Besides the core, a programmable PIC needs a set of input/output optical signal ports. Additionally, we foresee the introduction of dedicated high-performance blocks to perform specialized (electro-)optical functions, such as light sources, high-speed modulators, detectors, optical amplifiers, long delay lines and high-quality filters, depending on the application. The core waveguide mesh will then interconnect those blocks and will be able to be programmed to emulate some of those functions, such as delay lines or wavelength filters, but not necessarily at the same performance level as dedicated blocks.

# The technology stack

In practice, to make large waveguide meshes work, we also need driver and monitor electronics, control loops, configuration software, as well as conveniently packaged optical and microwave interfaces—all of which are supported by a development kit for engineers who want to

integrate a programmable PIC. This technology stack (Fig. 4) is similar to that of programmable electronics, but with additional photonic functions.

# PIC technology

The heart of the programmable circuit is the photonic chip, which can be fabricated in a variety of technology platforms $^{1,2,46,47}$ . To accommodate a large number of building blocks, these need to be compact $^{48}$ , so the most promising platforms are those that have a high refractive index contrast; for example, silicon photonics $^{1,46}$ , silicon nitride photonics $^{47}$  and indium phosphide PICs $^{2}$ . These technologies rely on wafer-scale manufacturing similar to electronic fabrication processes.

The optical waveguide losses are of the order of  $0.1 - 1\mathrm{dBcm}^{-1}$  depending on the materials and processing quality, which are systematically improving. This translates into  $50\%$  attenuation over  $3 - 30\mathrm{cm}$ .

At present, most PIC technologies support only a single layer of optical waveguides, restricting connections to a single plane and giving inherently 2D circuit architectures. Multilayer three-dimensional (3D) architectures can increase circuit complexity, flexibility and performance, and reduce footprint. Demonstrated multilayer Si photonic platforms have added integrated silicon nitride (SiN) $^{46,49-51}$  or amorphous silicon layers $^{52}$ , where waveguides can vertically route light using low-loss adiabatic tapers. Such layers allow waveguide crossings with ultralow loss and cross-talk $^{49}$ .

# Phase shifters and tunable couplers

The key building blocks – the tunable  $2 \times 2$  coupler and the phase shifter (Fig. 1)—require low optical insertion loss and low electrical power

![](images/b8f245da6130b2a9f6cd978c60d8911aa357856d9bb8829de9d6706a09ce493b.jpg)

![](images/e1b8ddc44e77871e9095df0b82c713b5859ee4348c13b6ca421fed52ba630443.jpg)

![](images/0e20eaf37fd00534fe7b83c902e01e77af7c32998f5e079ccc14bda2493ed3d9.jpg)

![](images/8a014cc30487c376f1c137a32104eaf9a5225635548d2850f547a086f9a21353.jpg)

![](images/3b00223d856b8d4a753c1a941626d8caa04a92ab11925cdf40a1af1d1f42602a.jpg)

![](images/07e1bb907c461e745e07dcb58770c90a5604c0847183d2cc2a5eeb27d85d7d43.jpg)

![](images/5487d083d658209a5df4023bb4d9eacc24e1e4e75fb8fc5aba0f8546dc0f634d.jpg)  
Fig. 3 | Recirculating waveguide meshes. a-c, Recirculating waveguide meshes can be based on square cells $^5$  (a), hexagonal cells $^{44}$  (b) and triangular cells $^{35}$  (c). Photographs reproduced from ref. $^5$ , OSA Publishing (a), ref. $^{44}$ ,

![](images/2dad37f25fa12dfa68d46e40a238c8fb4859313a744b86c741f2bfbb443d8c58.jpg)  
Springer Nature (b) and ref.  $^{35}$ , OSA Publishing (c). d-f, Double-ring add/drop wavelength filter programmed in a hexagonal mesh (d), the equivalent circuit (e) and a transmission measurement for different couplings  $\kappa_{1},\kappa_{2}$  and  $\kappa_{3}(\mathbf{f})$

![](images/56bd7a96003dc0850b249a52568aa4eb8fc70ee564da7e9e4f81197739c656bb.jpg)

consumption. In recirculating meshes, the elements should also have a short optical path length, allowing the synthesis of large-FSR filters. Today, most programmable photonic circuits use electrically driven heaters to induce a thermo-optic phase shift[53,54]. Such thermal tuners are easy to use, but each of them dissipates several milliwatts of electrical power (in silicon), has a time constant of  $10 - 100\mu \mathrm{s}$  and can have thermal cross-talk that needs to be compensated[55]. Faster tuners can use free carriers in semiconductors[56,57], but they have much higher optical losses; furthermore, their loss depends on the induced phase shift, which destroys the basic 'unitary' function of the gate. Research on improved or alternative approaches to phase shifters is very active. Such approaches include the use of materials with high thermo-optic coefficient[58], piezoactuators[59,60], liquid crystals[61,62], Pockels effect in perovskites[63-65] or polymers[66], and micro-electromechanical systems (MEMS)[67,68]. Non-volatile actuators, which maintain their state without an 'always-on' control signal, are also interesting. Examples include memristors[69], phase-change materials[70,71] and mechanically latched MEMS[72]. The  $2\times 2$  gates that contain these actuators are the primary source of loss in the circuit, with values of  $-0.05 - 0.2$  dB per gate. Technological improvements and better designs are reducing these values, as required for scaling up the circuits.

# Monitors and control loops

With hundreds of thousands of possible optical paths, we need to know where the light is on the chip so we can control the actuators. Photodetectors embedded immediately after $^{14,72}$  or even inside $^{73,74}$  each tunable element can directly track the path of light $^{75}$ . To minimize the optical losses, such monitor photodetectors should be as transparent as possible. Approaches include waveguide taps $^{14,76}$ , in-line photodetectors $^{72,77}$  and measuring the absorption that is already present in the waveguides $^{72-74}$

With such monitor signals we can operate the circuit as a self-configuring beam coupler $^{14,29,74}$  or implement self-calibration

algorithms $^{8,31,37}$ . Elementary tunable cells with integrated monitors allow the use of very simple local control loops that do not need a centralized control system, similar to reflexes in the human nervous system—for example, keeping a  $2 \times 2$  gate at a specific working point or stabilizing the wavelength of a filter circuit. The feedback loops can be implemented using analogue electronics $^{75}$ , digital electronics or software $^{14}$ .

In large programmable PICs, many optical signals can propagate in the same waveguides but on different wavelengths, polarizations or directions. To disentangle these signals in a monitor detector, we can use some form of labelling $^{8,31,36}$ , such as low-amplitude modulation tones at unique frequencies $^{8,31}$ . A dithering tone can also be applied to each actuator to disentangle their effect on the signal.

Monitors on the edge of the circuit can use non-transparent detectors with higher sensitivity, bandwidth and signal-to-noise ratio $^{6,36}$ , but they provide only limited insight into the internal distribution of light inside the mesh. Forward-only meshes can be fully configured with external monitors, using specific algorithms for continuous adaptation $^{8,29,30,32,36,41}$ . However, as circuits are scaled up, it becomes harder to control thousands of actuators using a handful of edge detectors. This leads to advanced non-convex global optimization algorithms $^{7,11,13}$  which require a centralized electronic control system. The optimal trade-off between the number of monitors and the complexity of the control depends on the architecture (for example, forward-only versus recirculating) and its partitioning.

# Electronics, radiofrequency components and packaging

Controlling thousands of actuators and monitors requires a substantial amount of electronics, in a combination of analogue (simple reflex-like control loops) and digital (global control) circuits. The actuators need high-resolution digital-to-analogue converters with sufficient precision. Alternatively, we could drive 'slow' actuators with direct

Fig. 4 | Technology stack for programmable photonic circuits.  
![](images/079da8f9cb76a432a0f2c6237f033ea3320f16f43aed754ffc7b375a74502284.jpg)  
Programmable photonic integrated circuits require several functional layers. a, The photonic chip has a programmable mesh of photonic gates connected to control electronics, optical fibres and high-speed modulators and detectors to translate between the optical and microwave domains. b, The photonic chip is

digital pulse-width modulation $^{62,78}$ . Likewise, monitor readout requires analogue-to-digital conversion circuitry. We also need programmable control logic 'above' such low-level driver electronics; this can be achieved using microcontrollers, FPGAs or digital signal processors (DSPs) operating on their own or connected to a computer through USB or ethernet.

These electronics need to be physically interfaced with the photonics chip. Photonic-electronic integration on the same chip offers the closest integration $^{79-81}$ , but currently such monolithic integration always incurs trade-offs (waveguide losses, limited choice in transistor nodes) that limit scaling to large programmable PICs. For this reason, hybrid integration approaches, in which electronics and photonics are fabricated on separate chips, are still the most practical. Traditional wire-bonding on the edge of the chip cannot easily scale up to  $>1,000$  wires, so approaches based on flip-chipping (Fig. 4b), interposers or 3D stacking are the most promising long-term solutions $^{82,83}$ . Multiplexing techniques such as row-column addressing of actuators can reduce the number of wires $^{84}$ .

Photonic waveguides support a very large signal bandwidth, which is why they are used for high-speed communications. To encode high-speed, radiofrequency signals (digital or analogue) onto an optical carrier, we can use high-speed electro-optic modulators with bandwidths exceeding 50 GHz (refs.  ${}^{57,85}$ ). The conversion of modulated optical signals to radiofrequency waves is handled by integrated photodetectors $^{85,86}$ . These modulators and photodetectors provide the input and output ports for microwave signals that are then processed on the optical chip $^{3-5,87}$ . Such filter functions programmed in the waveguide mesh must have a sufficiently large FSR to capture the entire radiofrequency bandwidth; for this purpose, the optical path lengths in the

packaged together with analogue and digital driver electronics, taking into account thermal and mechanical constraints and requirements on the hermeticity and electromagnetic compatibility (EMC). c, Software algorithms and programming layers give the user access to the photonic functionality. RF, radiofrequency. Image adapted from ref.  $^{106}$ , IEEE.

mesh need to be kept short (for example, an optical 'segment' length of  $1\mathrm{mm}$  in a hexagonal mesh for an FSR of 50 GHz).

High-speed radiofrequency interfaces require specialized substrates, connectors and well designed stripline waveguides[82,83,88]. Because such programmable PICs may also need thousands of electrical control lines and multiple optical fibre connections, packaging is a nontrivial part of the necessary technology stack.

# Amplifiers and light sources

The large waveguide meshes of programmable PICs will accumulate higher optical losses than more compact, specialized circuits. On-chip amplifiers could compensate such losses, either inside the waveguide mesh or on the edge. When combined with a waveguide cavity, such amplifiers can form a programmable laser, or their nonlinear behaviour can enable all-optical signal processing $^{89}$ .

Not all technology platforms include gain elements. III-V semiconductor platforms allow gain $^{2}$ , but integration of III-V amplifiers in silicon photonics is challenging, and most current silicon photonic circuits use external light sources. Amplifiers can be bonded on the silicon $^{90}$ , and recent studies show the long-term potential of direct epitaxy $^{91}$ . Techniques like microtransfer printing $^{92}$  allow placement of amplifiers in cavities, and bonding on the back side of the silicon-on-insulator wafer $^{93}$  gives additional flexibility, enabling arbitrary placement of III-V material relative to Si features.

# Programming algorithms and routing

Configuring thousands of actuators for flexible and powerful applications requires programming algorithms and automated methods. Some forward-only meshes can be progressively configured for different

![](images/7069b61fac57de65979db0e4bf7acae21226385fccf5d280d51ab9095d40b991.jpg)  
Fig. 5|Applications for programmable photonic circuits. Microwave signals can be transported over fibre and processed in the optical domain for xDSL and 5G applications $^{106}$ . Optical sensor systems can be used in construction,  
automotive, security and medical environments, such as for optical coherence tomography (OCT) or frequency-modulated continuous wave (FMCW) LiDAR. Image adapted from ref. 106, IEEE.

linear transformations $^{29,37}$  or layered self-configuring meshes $^{30,37}$ . For over-dimensional meshes with built-in redundancy, in which multiple configurations can result in the same functionality, these algorithms need to be generalized.

Recirculating architectures (which are generally over-diminished) require new layers of programming. Two broad classes of such programming techniques are 'black box' optimization methods $^{13,94,95}$  (for example, machine learning) and synthesis techniques. Optimization methods can operate directly on the hardware and do not necessarily require calibration. Synthesis techniques first deduce the desired mesh configuration and then apply that to the actuators; this requires periodic calibration to assess the operating point of each element $^{94}$ . Calibration data can be used in the synthesis process itself, for example, to minimize the cost function for routing light through the mesh $^{13,94,95}$  or to compose delay lines with a specific dispersion $^{87}$ .

Programming strategies can also leverage excess capacity to incorporate redundancy and self-healing $^{3,95,96}$ . Even with imperfect fabrication and defective elements, the mesh architecture and the software layer together can form a reliable system.

As photonic circuits become programmable, the growing development community will need a programming infrastructure around the photonic and electronic hardware, such as development kits and an application programming interface. Just as an electronic FPGA is described in its own language (VHDL), programmable PICs might require their own descriptive language. With high-level programming capabilities comes the possibility of defining reusable routines for operating programmable PICs. As in electronics, reusable blocks of code can drastically shorten development time and lead to true photonic-electronic systems-on-chip.

# Applications

Photonic chips differ from electronic chips in their basic operation and in the functions that they can efficiently execute. We therefore expect the two types of chips to be complementary: we do not anticipate using photonic circuits for the digital computations at which electronics

excel, but rather for communications, sensing and broadband analogue signal processing.

Programmable photonic chips are naturally more generic and flexible than custom-designed circuits. Of course, this programmability is only useful if these chips can be used in more than one setting[97]. PIC development has mainly been driven by high-speed communication (both telecom and data centres) but other applications, such as sensing and information processing, are being explored. As in electronics, we expect different modes in which programmable PICs will fit into the ecosystem:

- Full-custom ASPICs are today the most commonplace photonic chips. Like electronic application-specific integrated circuits (ASICs), they offer optimum performance for the desired function, but they take a long time to develop, and make economic sense only if the performance or fabrication volume justifies the cost. Still, even in such applications, programmable PICs could accelerate the development in early prototyping. However, like FPGAs in electronics, programmable PICs will always have a larger footprint, higher power consumption and higher optical losses than specialized ASPICs.  
- Combining programmable photonics with ASPICs can lead to hybrid chips in which a programmable core is embedded inside a custom ASPIC. Reuse of these cores (and their control logic) can shorten the development time of an ASPIC, just like reusable intellectual-property blocks in complex electronic chips. These hybrid chips have the same manufacturing pipeline as ASPICs, but adding programmability can make them more flexible.  
- Programmable and self-configuring PICs can be used for applications that require adaptation to problems that change in real time, such as adaptive sensing, alignment to changing external optical conditions, and mode-unscrambling. In this case, they open application areas beyond those of fixed ASPICs.

These different scenarios can be found in many application domains, some of which are illustrated in Fig. 5.

# Linear vector-matrix products

The optical field at the output of a reconfigurable waveguide mesh is a linear combination of the signals at the input ports. Such a linear

# Quantum information processing and artificial neural networks

Programmable waveguide meshes can be configured to execute any linear transformation between sets of input and output waveguides $^{8}$ , acting as a matrix operator that performs real-time calculations in the short time that the light requires to traverse the circuit. Such operations are key in artificial neural networks, so a programmable PIC can act as an accelerator for artificial intelligence and deep-learning applications $^{6,7}$ . The same linear operations are also at the core of photonic quantum computing. Here, the quantum information is represented by quantum states of light propagating through the  $\mathrm{PIC}^{100}$ . A popular scheme encodes a quantum bit (qubit) as a single photon in a superposition of two waveguides ('rails') $^{9}$ .

Deep learning and quantum information processing need more functional elements than linear circuits: a nonlinear response is required to implement either a neural 'activation function' or a two-qubit operation. Both deep learning and quantum computing are seeing a rapid co-development of algorithms and hardware. Although a lack of sufficient error correction still prevents general-purpose quantum computing, noisy intermediate-scale

quantum (NISQ) processors $^{116}$  have attained 'quantum supremacy', outperforming classical computers at certain tasks $^{117}$ . NISQ devices will have to be proved to be useful in practical applications. One such scheme is quantum machine learning $^{118}$ , which promises to process large datasets vastly faster than classical computers.

One way to implement quantum machine learning parallels classical photonic deep neural network accelerators (Box 1 Figure): stages of linear waveguide meshes are connected by activation layers, but these activation layers must have strong coherent (reversible) nonlinearities $^{119}$ . In such a 'quantum optical neural network' (QONN), the task of programming an NISQ computer reduces to training the phases in the waveguide mesh through supervised learning on input and output quantum states. The QONN can be taught to perform a range of quantum information processing tasks, including a new approach to quantum optical state compression and reinforcement learning. Recently, a QONN overcame the challenge $^{120}$  of programming a one-way quantum repeater $^{119}$ .

![](images/5f1e2e3d928cf92960c0969af043e23d492bc7feef7aa6551af863a7fcca31f2.jpg)  
Box1 Figure | Quantum optical neural network based on programmable photonics. Such a network, implementing the matrix operations  $W_{1}$ ,  $W_{2}$  and  $W_{3}$ , is fed by single photons and nonlinear activation (for example, nonlinear  
materials or atomic nonlinearities). The final state may be measured to complete a quantum computation or passed into a quantum network.

transformation is mathematically described as a multiplication of a vector (the input signals) with a matrix (the mesh), which is executed in real time by propagating light through the circuit<sup>8</sup>. Such matrix operations can be used in signal processing<sup>36,89</sup> and hashing operations<sup>98,99</sup>, but are also essential in emerging fields like quantum information processing<sup>9,15,100</sup> and artificial neural networks<sup>6,7</sup> (see Box 1).

The matrix can also be used as a switching network in optical communication, as a (de)multiplexer/(un)scrambler for different modes travelling over an optical fibre<sup>31</sup>, or even (when used in pairs) to find the optimal orthogonal communication channels through a linear system<sup>28</sup>.

# Microwave photonics

In microwave photonics, high-frequency electrical signals are processed in the optical domain by modulating them on an optical carrier. Photonic circuits for microwave applications<sup>4</sup> are mostly ASPICs implementing filtering<sup>101</sup>, waveform generation<sup>102</sup>, reconfigurable delay lines<sup>103</sup> or frequency measurements<sup>104</sup>. These functions can all be implemented in generic recirculating waveguide meshes<sup>3,5</sup>. For

instance, the meshes in Fig. 3a can be used as a Hilbert transformer, a delay line, a notch or bandpass radiofrequency filter, a temporal differentiator or integrator, a frequency converter and a programmable delay line $^{5,105}$ . These functions are essential to scale down equipment for next-generation 5G wireless systems $^{106}$  and radiofrequency systems for aerospace, where photonic chips can reduce power consumption and weight. Several applications of microwave photonics are illustrated in Fig. 5.

# Optical beamforming

Developments in optical beamforming are being driven strongly by LiDAR (light detection and ranging) $^{107}$  technology. A beam of light can be constructed using an array of small optical 'antennas' by carefully controlling the phase and amplitude in each antenna $^{108}$ . This requires a large number of independent tuners, as in generic programmable circuits. Whereas a generic programmable PIC could serve some simple beamforming applications, the performance requirements (for example, optical loss and power consumption) will probably dictate the use

# Review

of dedicated circuits. However, optical beamforming can also be used in reverse, coupling a distorted incoming field into a single waveguide $^{109}$ . A self-aligning beam coupler $^{29}$  can be used in both directions to align itself automatically and adaptively between a source and a target $^{110}$ .

# Sensing applications

Light can be used to sense a wide variety of phenomena through changes in absorption, phase or wavelength response. PICs form an effective sensor platform for transducers (for example, detecting biomolecules $^{111}$ ), on-chip spectrometers $^{112}$ , readouts for fibre Bragg gratings, laser Doppler vibrometers $^{113}$ , optical coherence tomography and frequency-modulated continuous-wave LiDAR receivers. Many of these could be implemented on a generic programmable PIC, and specialized sensor readout circuits could become a primary application space. Using the generic chip as the transducer is less likely, because the sensing mechanism often requires specialized geometries, chemistry or functionalization on chip.

# Perspectives

Programmable PICs have the potential to change the way in which people use coherent light to manipulate information. Decades ago, programmable electronics went through a similar evolution with microprocessors, FPGAs and DSPs, and it was no longer necessary to design a custom chip to perform a certain function. Instead, an ecosystem arose around off-the-shelf programmable electronics, which made it possible to build products much faster, more cheaply and with lower error margins[114]. Photonics is already following the electronics model with foundry-based manufacturing[46,47]. Programmable PICs, when available on an industrial scale, can take that further, shortening the lead time for photonic chips from months to days, eliminating substantial non-recurrent engineering costs and shifting product development from hardware to software[97]. This can bring PICs within reach of the creative community of 'makers', who are innovating with low-cost programmable electronics and additive manufacturing[115]. As in electronics, where discrete elements, ASICs and programmable integrated circuits coexist, we expect a photonic ecosystem in which discrete optics, ASPICs and programmable PICs provide their own set of solutions. Although photonic and electronic circuits are both chip-based technologies, they are fundamentally different. One key consideration is scaling: the size of photonic building blocks and the number integrated on a single chip are fundamentally limited by the refractive index contrast of the materials. With silicon photonics, we are already approaching the density limit of -1 million components per square centimetre, but there is still a huge space to explore in photonic design complexity.

Photonic circuits and electronic circuits are complementary. Because photonic circuits are analogue circuits, programmability in photonics will apply to different functions from those in programmable electronics. This also means that the abstraction layers that have been devised for electronics will need to be reimagined for programmable photonics. This opens up additional research fields in the higher levels of abstraction, on top of standard hardware, and presents opportunities to establish a certain level of standardization to help designers define and simulate functionality, irrespective of the photonic hardware vendor.

# Summary

We have introduced the emerging field of programmable PICs. Today, with application-specific PICs already deployed in a variety of applications, an opportunity arises to develop general-purpose programmable PICs. To this end, a complete technology stack is needed to complement photonics with electronics, packaging and various software layers. These concepts are already being tested for specialized applications in quantum information processing and neural networks, but general-purpose hardware could be useful for a variety of other

applications because its reconfigurability can drastically shorten product development, and its ability to adapt to changing problems opens up possibilities for functional optical systems.

1. Chen, X. et al. The emergence of silicon photonics as a flexible technology platform. Proc. IEEE 106, 2101-2116 (2018).  
2. Smit, M., Williams, K., & van der Tol, J. Past, present, and future of InP-based photonic integration. APL Photonics 4, 050901 (2019).  
3. Capmany, J. & Perez, D. Programmable Integrated Photonics (Oxford Univ. Press, 2020). The first book on the subject of programmable photonics gives a detailed overview of the fundamental principles, architectures and potential applications.  
4. Marpaung, D., Yao, J. & Capmany, J. Integrated microwave photonics. Nat. Photon. 13, 80-90 (2019).  
5. Zhuang, L., Roeloffen, C. G. H., Hoekman, M., Boller, K. & Lowery, A. J. Programmable photonic signal processor chip for radiofrequency applications. Optica 2, 854-859 (2015).  
6. Shen, Y. et al. Deep learning with coherent nanophotonic circuits. Nat. Photon. 11, 441-446 (2017).  
7. Harris, N. C. et al. Linear programmable nanophotonic processors. Optica 5, 1623-1631 (2018). One of the largest-scale demonstrations of a programmable photonic circuit, using a silicon photonics forward-only mesh that maps 26 input modes onto 26 output modes, for use in deep learning and quantum information processing.  
8. Miller, D. A. B. Self-configuring universal linear optical component. Photon. Res. 1, 1-15 (2013). This foundational paper in the field of programmable photonics is the first to bring together waveguide meshes with self-configuration algorithms that require no active computation, including the concept of the self-aligning beam coupler.  
9. Carolan, J. et al. Universal linear optics. Science 349, 711-716 (2015).  
10. Harris, N. C. et al. Large-scale quantum photonic circuits in silicon. Nanophotonics 5, 456-468 (2016).  
11. Notaros, J. et al. Programmable dispersion on a photonic integrated circuit for classical and quantum applications. Opt. Express 25, 21275-21285 (2017).  
12. Clements, W. R., Humphreys, P. C., Metcalf, B. J., Kolthammer, W. S. & Walmsley, I. A. An optimal design for universal multiport interferometers. Optica 12, 1460-1465 (2016).  
13. Perez-Lopez, D. Programmable integrated silicon photonics waveguide meshes: optimized designs and control algorithms. IEEE J. Sel. Top. Quantum Electron. 26, 8301312 (2020).  
14. Ribeiro, A., Ruocco, A., Vanacker, L. & Bogaerts, W. Demonstration of a  $4 \times 4$ -port universal linear circuit. Optica 3, 1348-1357 (2016).  
15. Harris, N. C. et al. Quantum transport simulations in a programmable nanophotonic processor. Nat. Photon. 11, 447-452 (2017).  
16. Mennea, P. L. et al. Modular linear optical circuits. Optica 5, 1087-1090 (2018).  
17. Taballione, C. et al.  $8 \times 8$  programmable quantum photonic processor based on silicon nitride waveguides. In Frontiers in Optics, JTu3A.58 (Optical Society of America, 2018). A demonstration of an  $8 \times 8$  forward-only programmable linear circuit in silicon nitride that benefits from the notably low optical losses of this material and is therefore attractive for linear quantum operations on single photons.  
18. Perez, D. et al. Silicon photonics rectangular universal interferometer. Laser Photonics Rev. 11, 1700219 (2017).  
19. Xie, Y. et al. Programmable optical processor chips: toward photonic RF filters with DSP-level flexibility and MHz-band selectivity. *Nanophotonics* 7, 421-454 (2017). A comprehensive overview of the various ways in which a programmable photonic circuit can be used to process microwave signals, and on how this type of circuit is transitioning from custom ASPICs to generic programmable PICs.  
20. Hall, T. J. & Hasan, M. Universal discrete Fourier optics RF photonic integrated circuit architecture. Opt. Express 24, 7600-7610 (2016).  
21. Dyakonov, V. I. et al. Reconfigurable photonics on a glass chip. Phys. Rev. Appl. 10, 044048 (2018).  
22. Shokraneh, F., Geoffroy-Gagnon, S., Nezami, M. S. & Liboiron-Ladouceur, O. A single layer neural network implemented by a  $4 \times 4$  MZI-based optical processor. IEEE Photonics J. 11, 4501612 (2019).  
23. Lu, L., Zhou, L. & Chen, J. Programmable SCOW mesh silicon photonic processor for linear unitary operator. Micromachines 10, 646 (2019).  
24. Qiang, X. et al. Large-scale silicon photonics implementing arbitrary two-qubit processing. Nat. Photon. 12, 534-539 (2018).  
25. Wang, J. et al. Multidimensional quantum entanglement with large-scale integrated optics. Science 360, 285-291 (2018).  
26. Schaeff, C., Polster, R., Huber, M., Ramelow, S. & Zeilinger, A. Experimental access to higher-dimensional entangled quantum systems using integrated optics. Optica 2, 523-529 (2015).  
27. Shad bolt, P. J. et al. Generating, manipulating and measuring entanglement and mixture with a reconfigurable photonic circuit. Nat. Photon. 6, 45-49 (2012).  
28. Miller, D. A. B. Waves, modes, communications, and optics: a tutorial. Adv. Opt. Photonics 11, 679 (2019).  
29. Miller, D. A. B. Self-aligning universal beam coupler. Opt. Express 21, 6360-6370 (2013).  
30. Miller, D. A. B. Perfect optics with imperfect components. Optica 2, 747-750 (2015).  
31. Annoni, A. et al. Unscrambling light—automatically undoing strong mixing between modes. Light Sci. Appl. 6, e17110 (2017). Early demonstration of a forward-only programmable mesh used to unmix different modes in a waveguide, implementing integrated transparent detectors that measure the light intensity in the waveguide without inducing additional optical loss.  
32. Pai, S. et al. Parallel programming of an arbitrary feedforward photonic network. IEEE J. Sel. Top. Quantum Electron. 25, 6100813 (2020).

33. Reck, M., Zeilinger, A., Bernstein, H. J. & Bertani, P. Experimental realization of any discrete unitary operator. Phys. Rev. Lett. 73, 58-61 (1994).  
34. Wang, M., Alves, A. R., Xing, Y. & Bogaerts, W. Tolerant, broadband tunable  $2 \times 2$  coupler circuit. Opt. Express 28, 5555-5566 (2020).  
35. Pérez-López, D., Gutierrez, A. M., Sánchez, E., DasMahapatra, P. & Capmany, J. Integrated photonic tunable basic units using dual-drive directional couplers. Opt. Express 27, 38071 (2019).  
36. Choutagunta, K., Roberts, I., Miller, D. A. B. & Kahn, J. M. Adapting Mach-Zehnder mesh equalizers in direct-detection mode-division-multiplexed links. J. Light. Technol. 38, 723-735 (2020).  
37. Miller, D. A. B. Analyzing and generating multimode optical fields using self-configuring networks. Optica 7, 794-801 (2020).  
38. Morizur, J.-F. et al. Programmable unitary spatial mode manipulation. J. Opt. Soc. Am. A 27, 2524 (2010).  
39. Labroille, G. et al. Efficient and mode selective spatial mode multiplexer based on multi-plane light conversion. Opt. Express 22, 15599-15607 (2014).  
40. Tanomura, R., Tang, R., Ghosh, S., Tanemura, T. & Nakano, T. Robust integrated optical unitary converter using multiport directional couplers. J. Light. Technol. 38, 60-66 (2020).  
41. Miller, D. A. B. Setting up meshes of interferometers - reversed local light interference method. Opt. Express 25, 29233 (2017).  
42. Li, H. W. et al. Calibration and high fidelity measurement of a quantum photonic chip. New J. Phys. 15, 063017 (2013).  
43. Cong, G. et al. Arbitrary reconfiguration of universal silicon photonic circuits by bacteria foraging algorithm to achieve reconfigurable photonic digital-to-analog conversion. Opt. Express 27, 24914 (2019).  
44. Pérez, D. et al. Multipurpose silicon photonics signal processor core. Nat. Commun. 8, 1-9 (2017). The first experimental demonstration of a recirculating waveguide mesh with seven unit cells that can be programmed to perform more than a hundred different functions.  
45. Pérez, D., Gasulla, I. & Capmany, J. Field-programmable photonic arrays. Opt. Express 26, 27265 (2018).  
46. Rahim, A., Spuesens, T., Baets, R. & Bogaerts, W. Open-access silicon photonics: current status and emerging initiatives. Proc. IEEE 106, 2313-2330 (2018).  
47. Munoz, P. et al. Foundry developments toward silicon nitride photonics from visible to the mid-infrared. IEEE J. Sel. Top. Quantum Electron. 25, 8200513 (2019).  
48. Teng, M. et al. Miniaturized silicon photonics devices for integrated optical signal processors. J. Light. Technol. 38, 6-17 (2020).  
49. Sacher, W. D. et al. Monolithically integrated multilayer silicon nitride-on-silicon waveguide platforms for 3-D photonic circuits and devices. Proc. IEEE 106, 2232-2245 (2018).  
50. Baudot, C. et al. Developments in 300mm silicon photonics using traditional CMOS fabrication methods and materials. In 2017 IEEE Int. Electron Devices Meeting, 765-768 (IEEE, 2017).  
51. Fahrenkopf, N. M. et al. The AIM photonics MPW: a highly accessible cutting edge technology for rapid prototyping of photonic integrated circuits. IEEE J. Sel. Top. Quantum Electron. 25, 8201406 (2019).  
52. Chiles, J. et al. Multi-planar amorphous silicon photonics with compact interplanar couplers, cross talk mitigation, and low crossing loss. APL Photonics 2, 116101 (2017).  
53. Van Campenhout, J., Green, W. M. J., Assefa, S. & Vlasov, Y. A. Integrated NiSi waveguide heaters for CMOS-compatible silicon thermo-optic devices. Opt. Lett. 35, 1013-1015 (2010).  
54. Masood, A. et al. Comparison of heater architectures for thermal control of silicon photonic circuits. In Proc. 10th Int. Conference on Group IV Photonics 83-84 (IEEE, 2013).  
55. Milanizadeh, M., Aguiar, D., Melloni, A. & Morichetti, F. Canceling thermal cross-talk effects in photonic integrated circuits. J. Light. Technol. 37, 1325-1332 (2019).  
56. Soref, R. A. & Bennett, B. R. Electrooptical effects in silicon. IEEE J. Quantum Electron. 23, 123-129 (1987).  
57. Reed, G.T., Mashanovich, G., Gardes, F.Y. & Thomson, D.J. Silicon optical modulators. Nat. Photon. 4, 518-526 (2010); corrigendum 4, 660 (2010).  
58. Memon, F. A. et al. Silicon oxycarbide platform for integrated photonics. J. Light. Technol. 38, 784-791 (2020).  
59. Jin, W., Polcawich, R. G., Morton, P. A. & Bowers, J. E. Piezoelectrically tuned silicon nitride ring resonator. Opt. Express 26, 3174-3187 (2018).  
60. Hosseini, N. et al. Stress-optic modulator in TriPlex platform using a piezoelectric lead zirconate titanate (PZT) thin film. Opt. Express 23, 14018 (2015).  
61. De Cort, W., Beeckman, J., Claes, T., Neyts, K. & Baets, R. Wide tuning of silicon-on-insulator ring resonators with a liquid crystal cladding. Opt. Lett. 36, 3876-3878 (2011).  
62. Xing, Y. et al. Digitally controlled phase shifter using an SOI slot waveguide with liquid crystal infiltration. IEEE Photonics Technol. Lett. 27, 1269-1272 (2015).  
63. Abel, S. et al. Large Pockels effect in micro- and nanostructured barium titanate integrated on silicon. Nat. Mater. 18, 42-47 (2019).  
64. Desiatov, B., Shams-Ansari, A., Zhang, M., Wang, C. & Lončar, M. Ultra-low-loss integrated visible photonics using thin-film lithium niobate. Optica 6, 380 (2019).  
65. Alexander, K. et al. Nanophotonic Pockels modulators on a silicon nitride platform. Nat. Commun. 9, 3444 (2018).  
66. Leuthold, J. et al. Silicon-organic hybrid electro-optical devices. IEEE J. Sel. Top. Quantum Electron. 19, 114-126 (2013).  
67. Errando-Herranz, C. et al. MEMS for photonic integrated circuits. IEEE J. Sel. Top. Quantum Electron. 26, 8200916 (2020).  
68. Quack, N. et al. MEMS-enabled silicon photonic integrated devices and circuits. IEEE J. Quantum Electron. 56, 8400210 (2020).  
69. Hoessbacher, C. et al. The plasmonic memristor: a latching optical switch. Optica 1, 198 (2014).  
70. Rios, C. et al. Integrated all-photonic non-volatile multi-level memory. Nat. Photon. 9, 725-732 (2015).

71. Wuttig, M., Bhaskaran, H. & Taubner, T. Phase-change materials for non-volatile photonic applications. Nat. Photon. 11, 465-476 (2017).  
72. Morichetti, F. et al. Non-invasive on-chip light observation by contactless waveguide conductivity monitoring. IEEE J. Sel. Top. Quantum Electron. 20, 292-301 (2014).  
73. Jayatilleka, H., Shoman, H., Chrostowski, L. & Shekhar, S. Photoconductive heaters enable control of large-scale silicon photonic ring resonator circuits. Optica 6, 84-91 (2019).  
74. Grillanda, S. et al. Non-invasive monitoring and control in silicon photonics using CMOS integrated electronics. Optica 1, 129 (2014).  
75. Annoni, A. et al. Automated routing and control of silicon photonic switch fabrics. IEEE J. Sel. Top. Quantum Electron. 22, 169-176 (2016).  
76. Dumais, P. et al. Silicon photonic switch subsystem with 900 monolithically integrated calibration photodiodes and 64-fiber package. J. Light. Technol. 36, 233-238 (2018).  
77. Chen, H., Luo, X. & Poon, A. W. Cavity-enhanced photocurrent generation by  $1.55\mu \mathrm{m}$  wavelengths linear absorption in a p-i-n diode embedded silicon microring resonator. Appl. Phys. Lett. 95, 171111 (2009).  
78. Ribeiro, A. & Bogaerts, W. Digitally controlled multiplexed silicon photonics phase shifter using heaters with integrated diodes. Opt. Express 25, 29778 (2017).  
79. Zimmermann, L. et al. BiCMOS silicon photonics platform. In Optical Fiber Communication Conference Th4E-5 (Optical Society of America, 2015).  
80. Orcutt, J. S. et al. Nanophotonic integration in state-of-the-art CMOS foundries. Opt. Express 19, 2335-2346 (2011).  
81. Stojanovic, V. et al. Monolithic silicon-photonic platforms in state-of-the-art CMOS SOI processes. Opt. Express 26, 13106 (2018).  
82. Carroll, L. et al. Photonic packaging: transforming silicon photonic integrated circuits into photonic devices. Appl. Sci. 6, 426 (2016).  
83. Patterson, D., De Sousa, I. & Archard, L.-M. The future of packaging with silicon photonics. Chip Scale Rev. 21, 1-10 (2017).  
84. Ribeiro, A., Declercq, S., Khan, U., Wang, M. & Van Iseghem, L. Column-row addressing of thermo-optic phase shifters for controlling large silicon photonic circuits. IEEE J. Sel. Top. Quantum Electron. 26, 6100708 (2020).  
85. Pantouvaki, M. et al. Active components for 50 Gb/s NRZ-OOK optical interconnects in a silicon photonics platform. J. Light. Technol. 35, 631-638 (2017).  
86. Chen, H. et al. 100-Gbps RZ data reception in 67-GHz Si-contacted germanium waveguide p-i-n photodetectors. J. Light. Technol. 35, 722-726 (2017).  
87. Pérez, D., Gasulla, I. & Capmany, J. Toward programmable microwave photonics processors. J. Light. Technol. 36, 519-532 (2018).  
88. Zoldak, M., Halmo, L., Turkiewicz, J. P., Schumann, S. & Henker, R. Packaging of ultra-high speed optical fiber data interconnects. In Opt. Fibers and Their Applications 2017 10325, 10325OR (International Society for Optics and Photonics, 2017).  
89. Willner, A. E., Khaleghi, S., Chitgarha, M. R. & Yilmaz, O. F. All-optical signal processing. J. Light. Technol. 32, 660-680 (2014).  
90. Ramirez, J. M. et al. III-V-on-silicon integration: from hybrid devices to heterogeneous photonic integrated circuits. IEEE J. Sel. Top. Quantum Electron. 26, 6100213 (2020).  
91. Liu, A. Y. & Bowers, J. Photonic integration with epitaxial III-V on silicon. IEEE J. Sel. Top. Quantum Electron. 24, 6000412 (2018).  
92. Zhang, J. et al. Transfer-printing-based integration of a III-V-on-silicon distributed feedback laser. Opt. Express 26, 8821-8830 (2018).  
93. Thiessen, T. et al. Back-side-on-BOX heterogeneously integrated III-V-on-silicon O-band distributed feedback lasers. J. Light. Technol. 38, 3000-3006 (2020).  
94. López, A., Perez, D., DasMahapatra, P. & Capmany, J. Auto-routinging algorithm for field-programmable photonic gate arrays. Opt. Express 28, 737-752 (2020).  
95. Chen, X., Stroobant, P., Pickavet, M. & Bogaerts, W. Graph representations for programmable photonic circuits. J. Light. Technol. https://ieeexplore.ieee.org/document/9056549 (2020).  
96. Zand, I. & Bogaerts, W. Effects of coupling and phase imperfections in programmable photonic hexagonal waveguide meshes. Photon. Res. 8, 211-218 (2020).  
97. Bogaerts, W. & Rahim, A. Programmable photonics: an opportunity for an accessible large-volume PIC ecosystem. IEEE J. Sel. Top. Quantum Electron. 26, 1-17 (2020). A simple techno-economic analysis of how general-purpose programmable photonic circuits can reduce the cost of prototyping photonics applications.  
98. Dubrovsky, M., Ball, M. & Penkovsky, B. Optical proof of work. Preprint at https://arxiv.org/abs/1911.05193 (2019).  
99. Paquot, Y., Schroeder, J., Pelusi, M. D. & Eggleton, B. J. All-optical hash code generation and verification for low latency communications. Opt. Express 21, 23873 (2013).  
100. Wang, J., Sciarrino, F., Laing, A. & Thompson, M. G. Integrated photonic quantum technologies. Nat. Photon. 14, 273-284 (2019).  
101. Norberg, E. J., Guzzon, R. S., Parker, J. S., Johansson, L. A. & Coldren, L. A. Programmable photonic microwave filters monolithically integrated in InP-InGaAsP. J. Light. Technol. 29, 1611-1619 (2011).  
102. Wang, J. et al. Reconfigurable radio-frequency arbitrary waveforms synthesized in a silicon photonic chip. Nat. Commun. 6, 5957 (2015).  
103. Burla, M. et al. On-chip CMOS compatible reconfigurable optical delay line with separate carrier tuning for microwave photonic signal processing. Opt. Express 19, 21475 (2011).  
104. Liu, L. et al. Photonic measurement of microwave frequency using a silicon microdisk resonator. Opt. Commun. 335, 266-270 (2015).  
105. Perez-Lopez, D., Sanchez, E. & Capmany, J. Programmable true-time delay lines using integrated waveguide meshes. J. Light. Technol. 36, 4591-4601 2018.  
106. Novak, D. et al. Radio-over-fiber technologies for emerging wireless systems. IEEE J. Quantum Electron. 52, 060031 (2016).  
107. Behroozpour, B., Sandborn, P. A. M., Wu, M. C. & Boser, B. E. Lidar system architectures and circuits. IEEE Commun. Mag. 55, 135-142 (2017).  
108. Heck, M. J. R. Highly integrated optical phased arrays: photonic integrated circuits for optical beam shaping and beam steering. *Nanophotonics* 6, 93-107 (2017).  
109. Van Acoleyen, K. Efficient light collection and direction-of-arrival estimation using a photonic integrated circuit. Photonics 24, 933-935 (2012).

# Review

110. Miller, D. A. B. Establishing optimal wave communication channels automatically. J. Light. Technol. 31, 3987-3994 (2013).  
111. Luan, E., Shoman, H., Ratner, D. M., Cheung, K. C. & Chrostowski, L. Silicon photonic biosensors using label-free detection. Sensors 18, 3519 (2018).  
112. Subramanian, A. Z. et al. Silicon and silicon nitride photonic circuits for spectroscopic sensing on-a-chip. Photon. Res. 3, B47-B59 (2015).  
113. Li, Y. et al. Six-beam homodyne laser Doppler vibrometry based on silicon photonics technology. Opt. Express 26, 3638 (2018).  
114. Trimmerger, S. M. Three ages of FPGAs: a retrospective on the first thirty years of FPGA technology. Proc. IEEE 103, 318-331 (2015).  
115. Mohomed, I. & Dutta, P. The age of DIY and dawn of the maker movement. Mob. Comput. Commun. Rev. 18, 41-43 (2015).  
116. Preskill, J. Quantum computing in the NISQ era and beyond. Quantum 7, 79 (2018).  
117. Arute, F. et al. Quantum supremacy using a programmable superconducting processor. Nature 574, 505-510 (2019).  
118. Biamonte, J. et al. Quantum machine learning. Nature 549, 195-202 (2017).  
119. Steinbrecher, G.R., Olson, J.P., Englund, D. & Carolan, J. Quantum optical neural networks. npj Quantum Inf. 5, 60 (2019).  
120. Matto, F. M., Epping, M. & Lütkenhaus, N. Hamiltonians for one-way quantum repeaters. Quantum 2, 75 (2018).

Acknowledgements D.A.B.M. acknowledges support from the Air Force Office of Scientific Research (AFOSR) under award number FA9550-17-1-0002. D.E. acknowledges support from AFOSR award FA9550-16-1-0391 and Air Force Research Laboratory award

FA8750-16-2-0141. W.B. acknowledges the European Research Council (ERC) for support through consolidator grant number 725555 (PhotonicSWARM) and the European H2020 programme for project grant 780283 (MORPHIC). J.C. and D.P. acknowledge the European Research Council (ERC) for support through advanced grant number 741415 (UMWPCHIP), Proof of Concept Grant 859927 (FPPAs) and Spanish Grant Juan de la Cierva. F.M. and A.M. acknowledge the European Commission for support through H2020 grant number 829116 (Super-Pixels) and Polifab, Politecnico di Milano for supporting the review of technology aspects.

Author contributions W.B. coordinated the work on this Review, and all authors contributed to the writing and editing.

Competing interests The authors declare no competing interests.

# Additional information

Correspondence and requests for materials should be addressed to W.B.

Peer review information Nature thanks Daniel Brunner, Michael Steel and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permissions information is available at http://www.nature.com/reprints.

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

$\odot$  Springer Nature Limited 2020