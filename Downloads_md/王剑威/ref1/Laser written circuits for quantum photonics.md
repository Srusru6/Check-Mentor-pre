Abstract The femtosecond laser direct-writing (FLDW) of waveguide circuits in glasses has seen interest from a number of fields over the previous 20 years. It has evolved from a curiosity to a viable platform for the rapid prototyping of small scale circuits. The field of quantum information science has exploited this capability and in the process advanced the fabrication technique. In this review the technological aspects of the laser inscription method relevant to quantum information science will be discussed. A range of demonstrations which have been enabled by laser written circuits will be outlined; these include novel circuits, simulations, photon sources and detection. This places the FLDW technique among the few integrated optical platforms to have produced individually every component required for scalable quantum computation.

![](images/ee4733e142843ecec3623620738c1736b682fe263e2ee4cb2c6d8e4ae149efd7.jpg)

A

M3IΛR

# Laser written circuits for quantum photonics

Thomas Meany $^{1,2,*}$ , Markus Gräfe $^{3}$ , René Heilmann $^{3}$ , Armando Perez-Leija $^{3}$ , Simon Gross $^{1}$ , Michael J. Steel $^{1}$ , Michael J. Withford $^{1}$ , and Alexander Szameit $^{3}$

# 1. Introduction

Quantum information science promises to use inherently quantum mechanical phenomena to encode, process and transmit information. In seeking out a platform to build such an architecture photonics stands out as a desirable candidate due to the ease with which photons can be transmitted in existing communication networks. A photon's multiple degrees of freedom can be prepared in distinct states and manipulated using conventional optical components such as waveplates and beamsplitters. Furthermore, photons do not easily interact with one another or with the environment meaning that noise due to a quantum state interacting with its surroundings is virtually eliminated. However, quantum photonics places stringent demands on a number of system properties. Quantum circuits are typically composed of nested interferometric components which must be phase stable and the insertion loss of an optical circuit limits the transmission of a quantum communication channel. These properties, accompanied by the need to miniaturise circuits

to enable high density complex designs, have encouraged the on-chip integration of photonic quantum circuits.

High density optical circuit fabrication is achievable with conventional technologies readily integrated with standard CMOS fabrication techniques [1-4]. Silicon circuits are convenient as both photon sources and routing devices. Silicon's high nonlinearity makes it desirable for a range of on chip active devices [5,6] including photon pair generation [7]. Various groups have developed multiple photon pair sources on a single chip with reconfigurable routing architectures [8], variable delays [9] and reconfigurable entangled photon generation [10]. However, due to challenges in the deterministic production and detection of photons only small scale circuits have been demonstrated. To date most demonstrations consist of less than four photons and less than 15 detectors. Although this problem is currently being addressed [11, 12] large density circuits are currently unnecessary for these prototype device designs and other considerations determine the ideal platform for a given task. In particular, the high extraction efficiency of photons from

glass waveguide circuits has made them the most practical method for exploring a range of quantum photonic devices and concepts.

Politi et al. were the first to demonstrate a quantum circuit using on-chip waveguides [13]. This experiment utilised a silica-on-silicon planar lightwave circuit (PLC) for a number of reasons. One of the most convenient wavelengths for producing coincident pairs of identical photons is  $800\mathrm{nm}$  and this overlaps with the high efficiency region for silicon avalanche photodiodes. Hence transparency in this wavelength range is important. Furthermore, low index contrast waveguides have both a low transmission loss and excellent mode overlap with optical fibre meaning that the overall extraction efficiency of a circuit is high. However, with quantum information science still in its infancy, PLC fabrication places some limitations on circuit design. Although PLC circuits can be produced on a large scale with relative ease, they are not ideal for device prototyping. PLC design can be completed in a number of ways but in order to produce waveguide patterns either a chrome mask to selectively illuminate a photosensitive resist or alternatively electron beam lithography is needed. These processes are feasible but not ideal for rapid prototyping. In addition some waveguide orientations which require out of plane designs are not achievable using this process.

The femtosecond laser direct-write (FLDW) technique [14] is a very different way to produce glass waveguides which helps alleviate some of the constraints of PLC fabrication such as photomask design and lack of support for out of plane structures. The FLDW method uses the high peak powers available with ultrafast lasers to induce localised nonlinear absorption at a laser focus within a transparent substrate. The absorption of this energy can cause a refractive index change and, in the case where this is positive, waveguides can be formed by translating the substrate with respect to the focus. Unlike PLC fabrication, the FLDW technique is a one step process, requiring no masking procedure or cleanroom environment. This means that prototypes can be produced rapidly and iterative fabrication methods can be employed. Furthermore, the laser is easily focused at multiple depths inside the material enabling three dimensional waveguide circuits which are extremely challenging to produce using lithographic means. This allows the production of vertically coupled waveguide arrays for the study of photon correlations and novel 3D integrated waveguide circuits.

In this review we will detail the progress in the field of quantum information science enabled by laser inscribed circuits. These circuits have proved valuable due to the convenience of their manufacture and their three dimensional fabrication capability. We will outline the operation and development of quantum circuits and the different methods used for their operation. The three-dimensional capability afforded by the laser inscription process and the unique photonic lattice designs this has enabled will also be discussed. Finally we will outline the advances made in the integration of single photon sources and detectors in laser written circuits and the future progress which can be achieved in the area.

# 2. Background

# 2.1. Quantum information science

This section provides a brief theoretical background to elementary quantum information. For a more detailed introduction, the reader is referred to the excellent textbook by Gerry and Knight [15]. For more information on the design of optical quantum circuits and their applications the reader is referred to Kok and Lovett [16].

The quantum bit, or qubit, is the quantum analogue of the classical bit. However, rather than the fixed values of the classical bit of “0” and “1” the qubit can exist in a superposition of these states. The state of a single qubit can be described by the ket

$$
| \psi \rangle = \alpha | \mathbf {0} \rangle + \beta | \mathbf {1} \rangle , \tag {1}
$$

where  $|\mathbf{0}\rangle$  and  $|\mathbf{1}\rangle$  are physical states representing logical states denoted by bold numbering. Also  $\alpha$  and  $\beta$  are complex coefficients satisfying  $|\alpha|^2 + |\beta|^2 = 1$ , so that the state  $|\psi\rangle$  is normalised. A general  $n$ -qubit quantum system, represented by a  $2^n$  bitstring, can be defined as:

$$
| \psi \rangle = \sum_ {i = 0} ^ {2 ^ {n - 1}} c _ {i} | x _ {i} \rangle , \tag {2}
$$

where  $|x_i\rangle$  is the tensor product of  $n$  logical qubit states determined by the binary expansion of the integer  $x_i$ . For  $n = 3$  for example,  $|x_3\rangle = |\mathbf{0}\rangle \otimes |\mathbf{1}\rangle \otimes |\mathbf{1}\rangle$ . Generally, the tensor product operator  $\otimes$  can be omitted without confusion, and we will do so below. To ensure normalisation of the whole state, the complex coefficients  $c_i$  satisfy

$$
\sum_ {i = 0} ^ {2 ^ {n - 1}} \left| c _ {i} \right| ^ {2} = 1. \tag {3}
$$

Each extra qubit doubles the number of states which can be represented; this is core to the exponential scaling of computing power with only a polynomial increase in the required resources offered by quantum computing. It should be noted however that simply preparing a large number of qubits is not sufficient to produce a quantum computer capable of performing any practical operation (please refer to the textbook by Nielsen and Chuang for a detailed background [17] or alternatively the reader is also referred to an excellent lecture series in Ref. [18]). A method of preparing, manipulating and reading out the state of these qubits in a controlled manner is required. Furthermore, only a handful of algorithms have been proven to provide a computational speed up over the best known classical methods, the most well known being Shor's algorithm for efficient factorisation of large composites [19, 20].

Encoding a qubit using photons is straightforward and two of the most popular representations are polarisation

![](images/742ba15f4cc73cc0b9a962ef2b1d4052f5fa3b4d599759537cb5ca63305d966c.jpg)  
(a)

![](images/b593c218d6aebc4b2783ef5893a9749f8008d4ca3c8f1da55aeafcc1951cc2f7.jpg)  
(b)  
Figure 1 (a) The equivalence of single rail (polarisation) encoding and dual rail (spatial mode) encoding schemes. A polarising beamsplitter (PBS) separates the two polarisations and a half wave plate in one mode rotates the polarisation by 90 degrees resulting in two spatially distinct modes. (b) A conceptual layout of a CNOT gate which flips the state of a target qubit conditional on the state of a control qubit. It does so by producing a phase shift on one arm of a Mach-Zehnder interferometer in the path of the target qubit. When the control qubit is in the  $|1\rangle$  state (a photon occupying mode c-1) then a phase shift of  $\pi$  is imparted on one arm of the target qubit Mach-Zehnder which switches the photon into the opposite mode.

encoding and spatial mode encoding. In the case of polarisation encoding a qubit state can be represented by its polarisation orientation (horizontal or vertical):  $|\mathbf{0}\rangle = |1\rangle_H \otimes |0\rangle_V = |H\rangle$  or  $|\mathbf{1}\rangle = |0\rangle_H \otimes |1\rangle_V = |V\rangle$ . Note once more that the tensor product notation indicating the occupation number of each polarisation mode  $(1\rangle_H \otimes |0\rangle_V)$  makes the relevant Hilbert space very clear, but the more compact notation  $(|H\rangle)$  is usually preferable. A polarisation-encoded qubit in the state  $|\psi\rangle = \alpha |\mathbf{0}\rangle + \beta |\mathbf{1}\rangle$  can be transformed into spatial mode encoding by using a polarising beam-splitter and half wave plate (as shown in Fig. 1(a)). In this case the mode  $(a \text{ or } b)$  occupied by the photon corresponds to the logical state:  $|\mathbf{0}\rangle = |1\rangle_a \otimes |0\rangle_b$  or  $|\mathbf{1}\rangle = |0\rangle_a \otimes |1\rangle_b$ . The polarisation encoding scheme is often referred to as the "single rail" encoding scheme, since both logical states occupy the same spatial mode, while the spatial mode encoding scheme is referred to as "dual rail". It should be noted that in many articles which discuss dual rail encoding the modes which correspond to the logical zero are often omitted since they do not play an active role in the circuit operation.

It is clear that the encoding of photons is a relatively straightforward task. Furthermore, single qubit rotations are easily achieved using components such as waveplates and beamsplitters. However, in order to perform quantum computation a two qubit gate is a necessity. Such a gate is the controlled-NOT or CNOT gate which is shown in Fig. 1(b). If we represent states in the two-qubit space in

terms of the "computational basis"  $(|\mathbf{00}\rangle, |\mathbf{01}\rangle, |\mathbf{10}\rangle, |\mathbf{11}\rangle)$  then the gate performs the following operation:

$$
U _ {\mathrm {C N O T}} | \psi \rangle = \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{array} \right] \left[ \begin{array}{l} c _ {0} \\ c _ {1} \\ c _ {2} \\ c _ {3} \end{array} \right] = \left[ \begin{array}{l} c _ {0} \\ c _ {1} \\ c _ {3} \\ c _ {2} \end{array} \right], \tag {4}
$$

which flips the final two elements of the two-qubit state vector. This may be compared to the classical XOR gate where a target register is flipped conditional on the state of a control register. This is a challenging gate to implement using linear optics since a nonlinear phase shift is required between two modes of the circuit; a  $\pi$  phase shift must be induced by the single photon propagating in the control  $|1\rangle$  mode. Despite enormous progress in cavity quantum electrodynamics (CQED) [21, 22] a single photon nonlinearity sufficient to produce such a large phase shift has yet to be demonstrated. In 2001, a landmark paper by Knill et al. [23] outlined a means to perform efficient quantum computing using only linear optical elements. This method, referred to as linear optical quantum computing (LOQC) only requires single qubit operations to form a circuit if they are combined with projective measurement. The price to pay is that the gate is non-deterministic and only a small subset of the possible outputs from the circuit are used. In this proposal the nonlinear phase shift, or nonlinear sign  $(\mathrm{NS}_x)$ , required for a two-qubit operation is achieved through a measurement-induced nonlinearity where projective measurement, combined with two-photon interference results in a probabilistic but heralded gate operation.

Two-photon interference occurring at a beamsplitter is caused by a complete absence of "which path" information between particles occupying two input modes of the beamsplitter and results in the coalescence of particles in a particular mode. An ideal beamsplitter performs a unitary operation on a set of optical modes [24]. In the normal way, we introduce bosonic mode creation operators denoted by  $a_i^\dagger |n_i\rangle = \sqrt{n + 1} |(n + 1)_i\rangle$ , where  $n$  denotes the photon occupation number in a given mode  $i$ . In the Heisenberg picture, the beamsplitter transforms input mode creation operators  $(a_1^\dagger$  and  $a_2^\dagger)$  to output mode operators  $(b_1^\dagger$  and  $b_2^\dagger)$ ,

$$
a _ {1} ^ {\dagger} \rightarrow \frac {1}{\sqrt {2}} \left(b _ {1} ^ {\dagger} + \mathrm {i} b _ {2} ^ {\dagger}\right)
$$

$$
a _ {2} ^ {\dagger} \rightarrow \frac {1}{\sqrt {2}} \left(\mathrm {i} b _ {1} ^ {\dagger} + b _ {2} ^ {\dagger}\right). \tag {5}
$$

Therefore if we choose as an input state  $|1_11_2\rangle = |1\rangle_1|1\rangle_2$  representing a single incoming photon in each mode, we obtain the following output [25],

$$
\begin{array}{l} \left| \right. 1 _ {1} 1 _ {2} \left. \right\rangle = a _ {1} ^ {\dagger} a _ {2} ^ {\dagger} \left| \right. 0 _ {1} 0 _ {2} \left. \right\rangle\rightarrow \frac {1}{2} \left(b _ {1} ^ {\dagger} + i b _ {2} ^ {\dagger}\right)\left(i b _ {1} ^ {\dagger} + b _ {2} ^ {\dagger}\right)\left| \right. 0 _ {1} 0 _ {2} \left. \right\rangle \\ = \frac {\mathrm {i}}{\sqrt {2}} \left(| 2 _ {1} 0 _ {2} \rangle + | 0 _ {1} 2 _ {2} \rangle\right). \tag {6} \\ \end{array}
$$

This equation shows the output state is entangled since the state is no longer separable. This state is often generalised to the  $N$  photon state  $(|N0\rangle + |0N\rangle) / \sqrt{2}$  where  $N$  corresponds to the photon number occupation of one mode and the zero denotes a vacuum occupation (no photons present) of the other mode. This two-photon interference is caused by the beamsplitter introducing an indistinguishability between the possible paths of the photons [26]. This is in no way due to any first order interference occurring due to overlapping the photons at the beamsplitter, since single photons are mutually incoherent particles. This fact has been shown in an experiment by Pittman et al. where which-path interference can be observed for particles which do not overlap in anyway at the beamsplitter [27]. The implementation of basic two-qubit gates based on this scheme will be detailed in section 3.

# 2.2. Waveguide formation

A brief description of the underlying material interaction and modification process is the purpose of this section. For further detailed information the reader is directed to books [28, 29] on laser microfabrication.

Although there has been progress in developing integrated photonic circuits for quantum information and crucial circuit elements have been produced in isolation and in monolithic demonstrations, there is still a number of challenges facing integrated quantum photonics. One issue is the availability of photon sources and detection capabilities which must be interfaced with prototype circuits. Many bulk optical photon sources operate at  $800\mathrm{nm}$  and are then coupled into waveguide circuits to perform characterisations. These circuits therefore would ideally be transparent at  $800\mathrm{nm}$  and have a mode size closely matched to that of a single mode fibre. The waveguides formed through femtosecond laser direct write (FLDW) can be fabricated with a refractive index contrast and diameter closely resembling an optical fibre meaning that insertion losses are minimal. Lithographic fabrication requires a unique photomask for each new circuit design. Hence if a circuit design parameter needs to be tweaked very slightly, an entirely new mask must be fabricated which is time, labour and cost intensive. The FLDW technique offers an alternative fabrication mechanism whereby a circuit is drawn into a glass substrate using a laser focus rather than imprinted and etched using a photomask. A conceptual image of the fabrication process is shown in Fig. 2 where three dimensional regions of refractive index change are "drawn" inside a block of glass at the point of the laser focus. This fabrication method has evolved to become a commercially viable waveguide fabrication platform. This is demonstrated by significant investment in companies like Translume, Optoscribe and Femtoprint [30-32].

The FLDW technique was first demonstrated by Davis et al. who modified a transparent substrate using a short pulse laser [14]. Unlike the laser inscription of photosensitive glasses, which relies on single photon absorption

![](images/0c9673cf30e633124e824aa2cf847a539e64755f4cf0c3e3453fbde0b1cc01a1.jpg)  
Figure 2 A conceptual image of the laser inscription process. Using a short pulsed laser focused inside a glass substrate the refractive index can be changed. Translating the substrate with respect to the laser focus permits the fabrication of 3D waveguide circuits.

from high energy ultraviolet (UV) light [33], the FLDW technique relies on multiphoton absorption of photons with energies below the bandgap of the material. Multiphoton absorption processes are driven by the intense electric field at the focus of a short pulse laser and lead to a material modification. The advantage of this method is the fact that the energy deposition is localised at the focus since the material is otherwise transparent at the writing wavelength. This also means that virtually any transparent dielectric can be processed using the FLDW technique, including glasses, ceramics and even crystalline materials. However the morphology of the induced material modification can vary significantly depending on the material and exposure conditions. For instance in glasses, three different modification types can be produced [34]. At low pulse energies a smooth refractive index change, typically referred to as Type I modification, can be induced, which, if positive in sign, is ideal for low loss waveguides. At intermediate pulse energies, self-organised sub-wavelength nano-structures have been observed [35, 36]. These nano-structures are aligned perpendicular to the electric-field vector of the incident laser field and exhibit a strong birefringence. Pulse energies above the damage threshold lead to optical damage of the material or an explosive expansion localised to the focal volume that results in the formation of voids [37]. These modifications are characterised as Type II.

Common substrate materials for low loss waveguides are silicate glasses, either fused silica or multi-component silicates, like the ones typically used for television and mobile phone screens. Even though these materials are similar in structure, the origin of refractive index change can be considerably different, depending on whether they are processed in the athermal or thermal regime. In the athermal regime where the time span between successive laser pulses is considerably longer than the thermal diffusion time of the glass, which is typically of the order of microseconds, a pulse-by-pulse repetitive modification of the material occurs. In fused silica this leads to densification

and creation of colour centres [38]. In contrast, in BK7 (a multicomponent silicate glass,) an increase in polarisability was attributed to the increased refractive index [39]. As a result of the low pulse repetition rate ( $< 100\mathrm{kHz}$ ), slow translation speeds, typically in the order of tens of micrometres per second are required in order to obtain sufficient spatial overlap between individual modifications to create a continuous waveguide. In contrast, in the thermal regime, successive pulses arrive well below the thermal diffusion time of the material [40, 41]. Thus there is insufficient time between pulses for the heat to diffuse out of the focal volume and an accumulation of heat occurs. This results in local melting leading to densification [39] and diffusion of elements in multicomponent silicate glasses [42]. As a result of the high laser repetition rate, the sample can be translated at speeds of millimetres per second and thus the waveguide inscription is orders of magnitude quicker than in the athermal regime. Mode-matching between optical fibres and FLDW waveguides circuits is crucial for efficient coupling. In the athermal regime astigmatic beam shaping has to be employed to obtain circular waveguide modes that match well to optical fibres [43, 44]. In contrast, the isotropic heat diffusion of glass results in intrinsically circular waveguides in the athermal regime. Not every glass responds with an increase in refractive index upon exposure to femtosecond pulses, such as ZBLAN for instance [45, 46]. Nevertheless, low-loss waveguides can be created by inscribing a depressed cladding where multiple modifications are arranged around an unmodified waveguide core to form a cladding of lower refractive index [47, 48]. This has the advantage that the excellent bulk optical properties of the glass are preserved in the core.

Certain crystalline structures are commonly exploited in quantum information science for their second-order nonlinearity capable of producing pairs of coincident photons. These crystals' unique electro-optic and nonlinear properties originate from their lattice structure which is anisotropic and exhibits no centre of inversion. However, this tightly-packed crystalline structure means that producing waveguides through densification is difficult [49]. Despite this, modifications have been observed and direct modification of the material's refractive index is designated as Type I index modification [50-52]. The most common tactic employed to produce waveguides in crystalline materials is Type II modification which uses a pair of damaged structures, in close proximity, producing a stress field acting as a waveguide [49, 53, 54]. This has the benefit of leaving the waveguiding region undisturbed, therefore preserving the desirable nonlinear or electro-optic properties of the material [53]. Limitations on circuit size when using this technique are imposed by the substrate translation stages (limiting two dimensional translation) and the laser focusing conditions such as objective working distance and aberration compensation (limiting movement in the third dimension). Low magnification objectives are often used (20-40) permitting a working distance of several millimetres but due to spherical aberration induced by the surface of the glass substrate and the air boundary it is

necessary to compensated for focal elongation at differing depths in the sample [55, 56]. High magnification oil immersion objectives are sometimes preferred since they eliminate spherical aberration almost entirely but reduce working distances to sub-millimetre. Furthermore propagation and bend losses have to be considered when designing a FLDW circuit. Low loss waveguides exhibit losses on the order of  $0.1\mathrm{dB / cm}$  [57, 58] and bend radii below  $30~\mathrm{mm}$  with negligible loss have been demonstrated at a wavelength of  $1550~\mathrm{nm}$  [59, 60].

An alternative technique has also been used to produce waveguides in glass using a laser for quantum information applications [33]. This method uses a specialised substrate material with a photosensitive germanium doped region. The process selectively modifies the regions which are exposed to the laser and means that waveguide circuits can be drawn rather than imprinted using a lithographic mask. It should be noted however that this method does not permit three dimensional device designs as in the case of the FLDW technique.

# 3. Quantum circuit components

This section outlines the three dimensional circuit designs which have been enabled by the laser inscription process. We begin by outlining the building block of all integrated circuits, the beamsplitter and move on to single and two qubit gates realised in both polarisation and spatial mode encoding.

# 3.1. Single qubit gates

The FLDW technique allows one to draw a circuit without a photomask and therefore rapidly adjust and prototype circuit designs. This technique was initially applied to produce directional couplers for manipulating path encoded qubits by Marshall et al. showing that laser written circuits could offer equally high two-photon interference visibilities as their lithographically produced counterparts [61]. This experiment used coincident photons produced by spontaneous parametric downconversion (SPDC) to characterise laser inscribed waveguide directional couplers (shown in Fig. 3). Directional couplers are the integrated optic analog of a bulk optics beamsplitter and therefore a core building block for more advanced circuit designs. They operate by bringing two waveguides into close proximity such that their evanescent fields may overlap and exchange energy. In this way a beamsplitter with any reflectivity can be produced by varying the separation between two waveguides and the length over which they interact. SPDC is a popular means for producing pairs of photons sufficiently identical that they may exhibit two photon interference [62]. This occurs by a pump photon probabilistically annihilating and producing a pair of photons (referred to as the signal and idler) with lower energies. The resulting photons are

![](images/4cdd2e8057d631a709b49916437410727df6bbbf818d7cea8e2deb04eb64a794.jpg)  
Figure 3 The layout of the experiment conducted by Marshall et al. to study the feasibility of using FLDW waveguide circuits in quantum optics experiments [61]. A  $402\mathrm{nm}$  continuous wave laser is focused inside a BiBO crystal. Degenerate down converted photons at the wavelength of  $804\mathrm{nm}$  are selected using suitable  $3\mathrm{nm}$  bandpass filters. Photons are subsequently coupled into optical fibres and routed to the device under test and the outputs are monitored using avalanche photodiodes (APDs) [61].

produced with a range of wavevectors  $k$  and frequencies  $\omega$  according to the phase-matching condition,

$$
\Delta k = k _ {p} \left(2 \omega_ {0}\right) - k _ {s} \left(\omega_ {0}\right) - k _ {i} \left(\omega_ {0}\right), \tag {7}
$$

where  $p, s$  and  $i$  refer to the pump, signal and idler respectively [63, 64]. In the experiment by Marshall et al., a nonlinear crystal of bismuth triborate (BiBO) was used to produce pairs of photons which were entirely degenerate. These were then coupled into optical fibres and transmitted to the laser inscribed device under test while at the output a pair of detectors were used to register coincidence events as a function of the temporal delay of one photon with respect to the other. A sharp drop in coincidence events, known as a Hong-Ou-Mandel (HOM) dip [62], signals that the two photons are entirely indistinguishable in every degree of freedom and this can be seen in Fig. 4. This demonstrated that two-photon interference visibilities ( $>95\%$ ), comparable to bulk optical and lithographically produce waveguides, can be obtained using FLDW waveguides and displayed the potential of FLDW devices for experiments in quantum optics.

These single qubit elements can also be implemented on qubits encoded in polarisation and laser inscribed integrated wave plates have been formed. Laser inscribed waveguides often feature an elongation in one dimension originating from focal elongation caused by either spherical aberration or by self focusing due to Kerr lensing at

![](images/8ef29405de3f3fe305c6d8ead0d2e5d70e79df42afdfa71578d40a58689e8f67.jpg)  
Figure 4 Hong-Ou-Mandel interference measured in a laser inscribed directional coupler with a visibility of  $96\%$  [61].

![](images/29fdf7bafa413762c3ba92779ce72b56575d1588b04d38bbbe60c5553ddc7590.jpg)

![](images/3f847143abc838673dd4ea6fefc16f1da6a47bd91c9e003e425d228165fcf3f9.jpg)  
Figure 5 Method to perform integrated wave plate operations. (a) Reorientation of the waveguide's optical axis due to additional stress fields caused by a defect. (b) The azimuthal orientation determines the optical axis' rotation [69].

high intensities. Hence, the waveguides possess an inherent form birefringence in the range of  $10^{-6} - 10^{-4}$  [65-68]. This birefringence can be exploited to produce waveguide based polarisation components. Fernandes et al. have demonstrated a stress-induced birefringence which was sufficient to perform an on-chip quarter and half wave rotation by including stress formations surrounding the waveguide core [67, 68]. The angle of the fast and slow axes can thus be chosen by selecting the orientation of the stress rods with respect to the core (see Fig. 5). This technique was used by Heilmann et al. in demonstrating wave plate operations for single photons [69]. An alternative approach was used by Corrielli et al. by exploiting the intrinsic form birefringence of the waveguides induced in the writing process [70].

# 3.2. Two qubit gate

A step towards two qubit gates came with the demonstration by Sansoni et al. that FLDW circuits could also be

![](images/ff17efdab65f1fe0ee05448e7de7074157a019bc98fc020852b3d4f83f819628.jpg)  
Figure 6 The polarisation encoded CNOT experiment by Crespi et al. [71]. The input states of the device are prepared using SPDC in a BBO crystal (C), polarising beamsplitter cubes (PBS), wave plates (WP) and controllers (WPC). Degenerate photons are selected using interference filters (IF). Fibres (SMF) can be strained in polarisation controllers (PC) to induce birefringence and act as wave plates. The chip contains three partially polarising directional couplers (PPDC) which are designed to operate on both modes of the input target and control qubits at once. Characterisations of the circuits' operational fidelity are completed by performing process tomography at the output of the device while varying the temporal distinguishability of the photons using a delay line (DL) and measuring photocounts using single photon counting modules (SPCM) [71].

used for photons encoded in polarisation [66]. This experiment showed the preservation of polarisation entanglement through an FLDW beam splitter. Subsequently, Crespi et al. incorporated this encoding method with a demonstration of a partially polarising directional coupler to form a CNOT gate for polarisation encoded qubits (see Fig. 6) [71]. This scheme is built around a partially polarising beamsplitter (PPBS), a component which permits a different beamsplitting operation on the horizontal and vertical components of the optical mode. Such a component is challenging to reliably produce in integrated optics. It exploits waveguide birefringence to produce an evanescent coupling which is polarisation dependent. A laser written PPBS circuit was initially demonstrated by Fernandes et al. who used sub-wavelength modifications (referred to as nanogratings) to induce a large waveguide birefringence inducing a polarisation sensitive waveguide coupling. This birefringent technique has also been used to produce half and quarter wave plates [67]. The demonstration by Crespi et al. instead used an inherent small birefringence of the laser written waveguides caused by their elliptical shape to implement a PPBS. The circuit is dense since a qubit is contained in a single spatial mode while the PPBS operates on both polarisation modes of the qubit simultaneously. However, this circuit does not permit the on-chip preparation of polarisation encoded qubits, normally accomplished using wave plates. This issue has been recently addressed by Corrielli et al. and Heilmann et al. in demonstrations of integrated optical wave plates [69, 70]. This has shown the diverse range of optical functions enabling polarisation encoded circuit operations. It should also be noted that experiments have exploited an alternative UV laser writing method to form circuits for quantum information and have shown phase control and on-chip photon number resolving detection [33, 72, 73].

# 3.3. Heraldged gate - C-Phase Gate

Although progress in destructive gate operation is important, ultimately it is essential that the output of a circuit can be fed forward and used in successive operations. For this, ancillary photons which can herald the successful operation of a desired circuit are essential. Despite the progress in the design of polarisation encoded circuits an element essential in scalable quantum computing, heralded gate operation, was achieved using a dual rail or spatial encoding scheme [74]. In this work a number of four mode circuits are fabricated which are designed to implement a controlled phase or C-Phase gate, which imparts a  $\pi$  phase shift on a target qubit arm conditional on the state of a control qubit. This is similar to the CNOT gate but an additional feature of the C-Phase gate is that it requires additional ancillary photons to herald the successful operation of the circuit. In this way the output of the circuit can be fed forward into another processing device. The architecture of the circuit was first proposed by Knill [75]. The idea of the theoretical proposal, compared with the design for its subsequent experimental demonstration, is shown in Fig. 7. This circuit offers the potential of a heralded CNOT by acting as the nested nonlinear sign shift in an interferometric setup such as that shown in Fig. 1(b).

In this work it should be noted that a full demonstration of the heralded operation of the circuit was not possible due to the technical challenges imposed by limited access to four coincident single photons. Currently, it is not possible using spontaneous parametric down conversion to repeatably produce four single photons in four individual modes. This is due to both the stochastic nature of the emission process and the statistics of multiphoton generation, which result in an equal probability of generating four photons distributed across two modes as compared to being distributed across all four modes. These multiphoton terms combined with the low generation rates mean that while technically possible, it is still experimentally infeasible to perform such a demonstration of the complete circuit operation. Despite this, it is still possible to exploit a recently demonstrated coherent state characterisation to accurately measure the unitary operation this circuit performs[76]. The work by Meany et al. [74] then studied how the measured unitary compares to the optimal unitary by using two measures: a simple mode fidelity measure which judges how well the unitary corresponds to the ideal operation, and a process fidelity which takes into account how the unitary will ultimately implement the intended function. Using the latter approach it is possible to account for errors such as reduced heralding efficiency, which is distinct from the efficiency of generating an entangled output robustly. The comparison between the mode and process fidelity is contained in Fig. 8 where the results from fabricated waveguide circuits are overlaid with the predicted mode and process fidelities when circuit parameters such as beamsplitter reflectivity and relative phase are varied. This work is important for future design constraints and realistic operation conditions of waveguide circuits featuring fabrication errors such as the study of large scale circuitry reported by Mower et al. [77].

![](images/0bca333fdd9d97ef19d91de5510b10dbb4c9c6068d0e4c66cb2ae7d5be424dce.jpg)  
Figure 7 (a) The circuit for a hcz gate showing paths for ancillary photons  $A$  and  $B$  as well as the computational qubits; the control (target) photon is encoded across spatial paths  $C_0(T_0)$  representing  $|0\rangle$  and  $C(T)$  representing  $|1\rangle$ . The  $|0\rangle$ -modes do not interact in the gate; the four remaining modes undergo four beamsplitting operations with reflectivities  $R(\theta_n) = \cos^2(\theta_n)$ . The light-coloured side indicates the surface yielding a relative  $\pi$  phase change upon reflection. (b) The four interacting circuit modes modelled as a waveguide array, showing the crossover and optimal reflectivities for the BSs implemented using evanescent coupling [74].

![](images/d17cb9eca236910549936bc74a595bf066daaf9c04e4135973be4fcd9b9a26e7.jpg)

![](images/aec4475049857c0bda99fa67fc1956965b14aced411b53736aa4a9367c2203b5.jpg)

![](images/14b29ebbfa348f3f366a97bf032b5ac5b1913833c2084cbcbb9be3f82330dfbf.jpg)

![](images/198c75dc513dcb6384190fd1fc3767ffbb6ec2a2b174dc545d0559d21ad3d28a.jpg)  
Figure 8 Variation of the model mode fidelity  $F_{m}$  and process fidelity  $F_{p}$  with deviations  $\Delta$  from the ideal BS angles and internal phase shift. The ideal phase is zero and  $\Delta \phi_{N}$  represents any net extra phase introduced between beamsplitters. For the BSs  $\Delta$  is the variation from the ideal angle; the total reflectivity will be  $\cos^2 (\theta_{\mathrm{ideal}} + \Delta \theta)$ . In both cases  $\Delta$  is a length variation in the physical device. The top graphs show the fidelity when one  $\Delta$  parameter is varied and the rest are held at zero. The points shown represent the deviations found in the best experimentally-characterised circuit. Note that on this scale both the curves and points for BS1 and BS2 are indistinguishable. The bottom graphs show the fidelities for 2000 simulated instances of hcz gates with all  $\Delta$  parameters drawn randomly from Gaussian distributions with mean 0 and standard deviation  $\sigma_{\Delta}$ . The purple distribution has  $\sigma_{\Delta} = 0.1$ , which is similar in magnitude to most of the  $\Delta$  parameters from our best measured circuit; the green distribution has  $\sigma_{\Delta} = 0.05$  in order to show the fidelities achievable with a modest improvement in fabrication accuracy. The resulting green (purple) distributions have means of 0.994 (0.980) for  $F_{m}$  and 0.962 (0.863) for  $F_{p}$ . Note the logarithmic scale on the horizontal axes [74].

![](images/d49bc64c67d02660422b8d0d56cd3320d0903e4229e3b0f79b05cb1d4f9c3573.jpg)

# 4. Advanced circuit designs

As indicated from the previous section, the more intricate the circuits become, the more complex the gate operations which are achievable. These operations range from exotic state engineering to state verification and computational problems. Naturally, such tasks impose strict requirements on design accuracy. The FLDW technique provides precise fabrication adjustment and the ability to write almost arbitrary 3D geometries which enable compact structures.

In this section we focus on three topics that exploit complex waveguide geometries. Firstly we outline the boson sampling problem which is of interest since it strongly indicates that a currently achievable quantum computer may be superior to a classical one. Secondly we discuss a multiplexing device which allows the generation of multi-partite entangled W-states of high order. They can be exploited for various applications including the generation of genuine random numbers. Finally we describe an additional 3D circuit design which allows the multi-partite entanglement verification of the generated W-states. This device

also enables universal W-state generation. In this context we present a novel method to characterise this elaborate quantum network using only classical light.

# 4.1. Boson-sampling

Boson sampling is a computational problem that is believed to be exponentially hard by means of classical calculation but could be solved very efficiently using a quantum computer as pointed out by Aaronson and Arkhipov [78]. It requires neither nonlinearities nor a priori entanglement—as distinct from universal quantum computing. Starting with an  $m \times m$  device described by a unitary  $U$  and injecting  $n \leq m$  indistinguishable bosons into  $n$  different ports the task is to sample the bosons' output distribution, that is, to calculate the probabilities of finding the bosons in  $n$  various output ports. Due to bosons' non-classical interference [79] there is no known efficient classical sampling algorithm.

To obtain the probability for a certain output distribution one has to consider a  $n \times n$  submatrix  $\widetilde{U}$  of the unitary  $U$ . The desired probability is found from the permanent of this submatrix:  $P = |\mathrm{per}(\widetilde{U})|^2$ . The matrix permanent is related to the more familiar determinant in a simple fashion: all terms in the sum over matrix element products appear with a positive sign as opposed to the alternating sign that applies in the case of the determinant. Calculating either quantity from their definitions is a problem that scales factorially, and is thus considered computationally hard. For the determinant (which corresponds to the fermion sampling problem), standard matrix diagonalisation reduces the problem to cubic complexity, but no such simplification is known for the permanent. A quantum device is not believed to be more efficient in calculating individual matrix permanents than a classical computer, but it will be superior when sampling over the complete output distribution of a sufficient large system.

To illustrate the boson sampling problem, let us imagine a beam splitter (BS) with transmittivity  $t$  and reflectivity  $r$  ( $t^2 + r^2 = 1$ ) where two indistinguishable photons are injected into each input port. The probability  $P$  of having on photon in output channel 1 and another in channel 2 is exactly the boson sampling problem in that specific case. The probability is given by

$$
P = \left| \operatorname {p e r} \binom {t} {\mathrm {i} r} \quad t \right| ^ {2} = t ^ {2} - r ^ {2}. \tag {8}
$$

If we consider a symmetric BS with  $t^2 = r^2 = 1 / 2$  we find  $P = 0$ , consistent with our expectations for a Hong-Ou-Mandel interference experiment [79].

To study a nontrivial example of the boson sampling problem a multimode circuit was used by Tillmann et al. (as shown in Fig. 9 [80]). The importance of this proof of principle experiment was such that four research groups realised a version of it independently and within a very short timeframe. It was initially reported by Broome et al. by means of a  $6 \times 6$  fibre mode network [81] and by Spring et al. using a

![](images/0578247f7aeac19a3f6802f0c77b3fb8a481d1138112824bb6becfc66a6633c2.jpg)

![](images/aa55b0f9bff6524126ba878e0d36565c6c2db03a89b9f40f9e49f856b6cecece.jpg)  
Figure 9 Waveguide circuit and results of the experimental boson sampling. (Top) The circuit consists of five input channels (1 to 5), five output channels  $(1^{\prime}$  to  $5^{\prime}$ ) as well as eight BSs  $(\eta_{1}$  to  $\eta_{8})$  and eleven phase shifters  $(\varphi_{1}$  to  $\varphi_{11})$ . Three single photons have been coherently injected into any combination of input modes. Each output guide is connected to a single-photon detector, and joint-click events are detected by a home-built FPGA logic circuit. The waveguides' pitch at the facets is  $127~\mu \mathrm{m}$  and the chip has a total length of  $10~\mathrm{cm}$ . (Bottom) Experimentally measured (red) and theoretical (blue) three-photon probabilities for the ten possible output combinations when injecting photons into input modes 1, 2 and 4 yielding a fidelity of  $0.98 \pm 0.01$ . For more experimental results and details, see [80].

6 silica-on-silicon chip [82]. The Boson sampling was also implemented in another  $5 \times 5$  femtosecond laser-written chip [83]. There, a five-port interferometric structure was inscribed in borosilicate glass and and the phases as well as the transmission rates of the deployed directional couplers could be precisely controlled due to the flexibility of the FLDW technique. All implementations used up to three photons as input to their quantum circuits and obtained similar results verifying that indeed a simple quantum computer can efficiently sample a quantum network's bosonic output distribution. In the Tillman et al. experiment, a photonic network as depicted in Fig. 9 with five input and five output ports, consisting of eight BS with different splitting ratios and eleven phase shifters was inscribed into a ten centimetre long fused silica glass chip via the FLDW technique. On launching three indistinguishable photons into three distinct ports of the possible five, the device 'computes' all probabilities of finding the three photons in three various of the five output channels. The probability distribution is

acquired by means of three-photon coincidence detection between the output modes. Several input configurations have been realised of which Fig. 9 shows one example.

# 4.2. Generation of high-order W-states

One particular class of maximally multipartite entangled states are the so-called W-states, which have the remarkable property that their entanglement is robust against decoherence [84]. Originally introduced for three qubits, they were quickly generalised to  $N$  entangled eigenstates:

$$
\left| \mathrm {W} _ {N} \right\rangle = \frac {1}{\sqrt {N}} \sum_ {k = 1} ^ {N} \mathrm {e} ^ {\mathrm {i} \varphi_ {k}} \hat {a} _ {k} ^ {\dagger} | 0 \rangle , \tag {9}
$$

where  $\varphi_{k}$  is an arbitrary but fixed phase distribution. W-states have been proposed for a variety of applications like teleportation, secure communication, or genuine random number generation[85-87]. Nevertheless, their experimental realisation stopped at the order of  $N = 4$  [88]. One of the major reasons is the decoherent evolution with bulk optics which makes the generation of high-order W-states very challenging. Note, while W-states' entanglement is robust against decoherence, their generation is not.

A possible solution to create high-order W-states is to establish their generation on-chip. Integrated devices are intrinsically stable, thus preserving coherence. In line with this, Grafe et al. demonstrated that a femtosecond laser-written waveguide structure can be used to generate single photon W-states up to the order of  $N = 16$  [87]. The configuration they used to realise  $N = 8$  is shown in Fig. 10. It consists of seven integrated BS arranged in a cascade such that a single photon injected into input port 3 is coherently split at the first BS and again at the next two BSs and so on, and is finally coherently shared among all eight output channels. Figure 10 shows the count statistics for W-states of different order. As expected, a flat uniform probability distribution can be observed in all cases. This is quite distinct from the quantum walk distributions we discuss below.

Verification of the multipartite entanglement on the basis of state tomography is naturally extremely elaborate. Instead, it is possible to perform the verification by means of a unitary transformation that projects a W-state onto a single photon Fock state. Hence, the fidelity of the transformed state compared to the single photon Fock state gives a measure of the W-state's multipartite entanglement [89, 90]. In that vein, to prove the  $N$ -partite entanglement of a  $N$ -th order W-state the fidelity has to be greater than  $(N - 1) / N$ . That kind of unitary transformation is realised by the three-dimensional waveguide structure discussed in section 4.3. A fidelity of  $0.918 \pm 0.004$  was experimentally demonstrated confirming the presence of eight-partite entanglement [87].

Moreover, exploiting their intrinsic randomness and their flat eigenstate's probability distribution W-states are perfectly suited for genuine random number generation. Such generated random numbers pass all statistical tests

![](images/1716f829ed6c4be0a81de36208b74020c663dff0803f571fe95176b3700bd763.jpg)

![](images/20b42086e2dfc8e1031612ab8c6a7ea2a561bbef53891c982d85a56457a6510a.jpg)  
Figure 10 Generation of high-order photonic W-states on an integrated platform. (Top) A hierarchical network of 50/50 BS arranged in sequential stages transforms the single-photon (Fock) input states into W-states. The specific structure shown here is capable of efficiently producing any of the states  $|W_2\rangle$ ,  $|W_4\rangle$  and  $|W_8\rangle$ , depending on the choice of input port. (Bottom) Experimentally obtained probability distributions for W-states of different order. The standard deviations (from the uniform distribution) of the individual measurements are shown as horizontal bars [87].

provided by the National Institute of Standards and Technology (NIST) [87, 91]. The advantages of this scheme are the uniform probability distribution, which relegates any post-processing and the large number basis  $N$ , which enables a high generation bitrate. To put it simply, applying a W-state of  $N$ -th order is the same as rolling a  $N$ -sided quantum dice. Additionally, since the W-state creation is on-chip the random number generation benefits from the advantages of integrated photonic devices.

# 4.3. Multi-partite entanglement verification and novel device characterisation scheme

Using the 3D capability of the FLDW technique it becomes possible to verify the multipartite-entanglement of the produced W-states described in the previous section and to realise their generation independently from the input port.

In order to verify the entanglement of the  $|\mathrm{W}_N\rangle$  one can apply a unitary  $U$  which projects any state into a basis set of orthogonal W-states (varying in their phase distribution) by mapping each of them to one specific single-photon Fock state:  $|\mathrm{W}_N\rangle \rightarrow \hat{a}_N^\dagger |0\rangle$ . Of course the desired state must be one of the basis states. In that vein, the density matrix  $\rho$  of the desired state evolves to  $\widetilde{\rho} = U\rho U^{\dagger}$ , yielding the fidelity

$$
\mathcal {F} = \left\langle \mathrm {W} _ {N} \right| \rho \left| \mathrm {W} _ {N} \right\rangle = \left\langle \mathrm {W} _ {N} \right| U ^ {\dagger} U \rho U ^ {\dagger} U \left| \mathrm {W} _ {N} \right\rangle = \widetilde {\rho} _ {N N}. \tag {10}
$$

![](images/a7f06531d5ece4f5e663e983c5bf450d1b7b5af9aba94573ed4bc08062c3d594.jpg)  
Figure 11 (a) Verification device to prove multipartite entanglement of the W-state generation device's (Fig. 10) outcome when launching in single photons. The verification structure consists of twelve integrated 50/50 BSs projecting a W-state to a single waveguide output. (b) Setup for phase estimation. A laser beam is split into two fields providing different input combinations. Changing one arm's optical path, the resulting intensity oscillations are recorded by a CCD camera at the output. (c) Normalised intensity traces for all output guides when exciting input channels 1 (reference) and 8. The extrema of the oscillation in the reference channel are tagged by vertical blue lines. On the left: Intensity correlations of channel 4 respectively 7 with the reference channel. A Lissajous ellipse can be fitted and its rotation recorded to extract the particular phase [87].

Biseparable states satisfy the inequality  $\mathcal{F} \leq (N - 1) / N$  such that a violation is sufficient to verify  $N$ -mode entanglement in the state  $\rho$  [89,90]. In this specific case, the unitary transformation is achieved by the waveguide network presented in Fig. 11(a) which maps the output of the W-state generation device to one single output channel. It was experimentally demonstrated that indeed the photons emerge from one channel only with a fidelity of  $(91.8 \pm 0.4)\%$  violating the criterion above and thus verifying the eight-mode entanglement.

The verification device is itself a multiport interferometer which can only be realised using a 3D geometry. Its remarkable property is that it can be used to universally generate W-states by transforming a single photon state into a W-state independent of the chosen input channel:  $\hat{a}_l^\dagger |0\rangle \rightarrow |\mathrm{W}_8^{(l)}\rangle = \frac{1}{\sqrt{8}}\sum_{k = 1}^8\mathrm{e}^{\mathrm{i}\varphi_{k,l}}\hat{a}_k^\dagger |0\rangle$ . The phase distribution  $\varphi_{k,l}$  is determined by the choice of the input guide  $l$ . One has to consider a  $\pi /2$  phase jump for light in the reflection (tunnelled) channel of an integrated BS.

We now discuss how such networks can be characterised. The task is to ascertain the complex matrix elements  $U_{k,l} = |U_{k,l}| \mathrm{e}^{\mathrm{i}\varphi_{k,l}}$ , i.e., moduli  $|U_{k,l}|$  and the phases  $\varphi_{k,l} = \arg (U_{k,l})$  of the network's unitary  $U$ . Unfortunately, quantum process tomography becomes fairly impractical in the case of such complex systems [92]. An efficient

alternative is provided by a highly precise interferometric approach using classical light only [74, 93, 94]. While the moduli  $|U_{k,l}|$  are obtained by means of classical intensity measurements the phases  $\varphi_{k,l}$  are quantified by classical light interference. For experimental realisation, a laser beam is split into two components addressing different input configurations. As depicted in Fig. 11(b), the output intensity distribution is imaged onto a CCD camera. Channel 1 serves as a reference channel and its optical path was changed by slightly heating up the fibre via a warm breath. A Lissajous ellipse is fit to the correlations of the oscillations of each channel with respect to the reference channel and from the rotation one is able to extract the phases  $\varphi_{k,l}$  (see Fig. 11(c)) [94, 95]. This results in an overall gate fidelity of  $0.979 \pm 0.034$ . Note, the characterisation scheme does not need any highly precise delay stages. It uses classical light only, scales linearly with the network size and thus minimises the experimental effort while keeping highest accuracy of  $0.014\pi \ldots 0.008\pi$  corresponding to a resolution of  $\frac{\lambda}{140} \ldots \frac{\lambda}{250}$  in this example.

# 5. Quantum Random Walks

Classical one-dimensional random walks are defined in terms of probabilities for a classical particle to advance one step to the left or to the right within a discrete graph. In contrast, one-dimensional quantum random walks (QRW) are physical processes where single quantum particles simultaneously evolve in two permissible directions within a discrete graph [96].

As elucidated in the present review, integrated photonic systems are among the most advanced and auspicious schemes for the realisation of quantum circuits and quantum simulators. Along similar lines, it is not surprising that quantum random walks of single-photon as well as of correlated photon pairs are also possible using such integrated photonic configurations [97]. The aim of this section is to give an account of the realisation of unique photonic lattice designs which are based on integrated laser-written technology.

Our discussion starts by describing the realisation of a discrete quantum walk for entangled particles via networks of integrated polarization-maintaining beam splitters [98]. We then refer to the continuous QRW realisation of spatially extended Einstein-Podolsky-Rosen two-photon states, correlated and anti-correlated in their positions, which evolve in ordered and Anderson photonic lattices [99]. Finally, we give an overview on the observation of two-photon quantum walks in two dimensional waveguide arrays. These include an elliptical direct-written waveguide array [100] as well as an array in a Swiss cross lattice arrangement [101].

# 5.1. Two-particle Bosonic-Fermionic quantum walks using integrated photonics

In Ref. [98], Sansoni et al., report on the observation of discrete QRW of entangled particles via integrated photonic systems endowed with broken  $z$ -invariance [98].

![](images/e261e2d68e30b75c7cef168d839ba83dff36a1e4b0843d24d9b2a1b49d19c62c.jpg)  
Figure 12 Left picture shows a schematic of the network of directional couplers fabricated for implementing a four-step quantum walk. The color coding indicates the writing depth of the waveguides, which is varying from point to point. Right picture shows a 3D representation of the basic cell of the network, which acts as a Mach-Zehnder interferometer [98].

For the experiments, they created the discrete network of integrated beam-splitters illustrated in Fig. 12. The input biphoton states were generated using a  $\beta$ -barium borate crystal (BBO) cut for type-II non-collinear phase matching. This produces a two-particle polarization-entangled state,  $|\psi\rangle = (|H\rangle_A |V\rangle_B + \mathrm{e}^{\mathrm{i}\phi} |V\rangle_A |H\rangle_B)/\sqrt{2}$  [102]. In addition, through the use of a voltage controlled liquid crystal device, the relative phase  $\phi$  was tuned from 0 to  $\pi$  allowing the transformation of the initial state from the so-called triplet state,  $|\psi^{+}\rangle = (|H\rangle_A |V\rangle_B + |V\rangle_A |H\rangle_B)/\sqrt{2}$ , to the singlet state,  $|\psi^{-}\rangle = (|H\rangle_A |V\rangle_B - |V\rangle_A |H\rangle_B)/\sqrt{2}$ , of the Bell basis [103]. A remarkable fact elucidated through these experiments is that by sweeping the phase interval  $[0,\pi]$  it is possible to simulate quantum behaviour expected of bosonic  $(\phi = 0)$ , fermionic  $(\phi = \pi)$ , and anyonic  $(\phi \in (0,\pi))$  particles.

It is worth emphasising that the exploitation of the polarization degree of freedom is possible due to the excellent control over coplanar and non-coplanar waveguide inscription. In fact, for the experiments discussed here it was necessary to fabricate the waveguides at different planes in such a way that the polarization of the initial states was preserved.

For experimental demonstration, two-photon entangled states with  $\phi = 0,\pi$  , and  $\pi /2$  were injected into the system and the corresponding coincidence rates were measured at the output of the array. The results are depicted in Fig. 13.

For the case when the triplet state is coupled into the system, the correlation map exhibits the behaviour expected of bosonic particles, that is, both particles tend to bunch at the same output channel (see Fig. 13(a)). On the other hand, when the singlet state is coupled to the system, both particles separate and anti-bunching effects are observed. This particular case clearly indicates that the photon statistics correspond to that expected from fermionic particles which obey Pauli's exclusion principle [104]. In the optical context, this means that photons (behaving as fermions) cannot co-exist at the same output mode (Fig. 13(b)). The corre

![](images/b71c3b0b0af60b2f722701fbe034cd580de5d351855e488f753c062085775558.jpg)

![](images/3e4bbf5363ee7d01b659bab20a3c3c68214d23a4113bddfceba8120add860fd4.jpg)

![](images/592f0f9d1d7a7dd3b151a60716259a8c8bf3fa6b1e1b8c89084d9bc753bc61c7.jpg)  
Figure 13 Two-particle quantum walks: ideal (left) and measured (right) distributions of (a) bosonic, (b) fermionic and (c) anyonic (with  $\phi = \pi /2$ ) quantum walks [98].

lation map for the two-photon input state with  $\phi = \pi /2$  clearly exhibits that the output quantum statistics in fact evokes anyonic-like behaviour (Fig. 13(c)). Notably, these results open possibilities to explore particle statistics using bosons only.

# 5.2. Anderson localisation and co-localisation of Einstein-Podolsky-Rosen photon pairs on disordered photonic lattices

Following the original experiment by Hong, Ou, and Mandel [79], the presence of entanglement allows for observations of the quantum probability amplitude interference of two identical particles. In that vein a recent investigation demonstrated the role of entanglement of indistinguishable particles propagating through periodic and Anderson photonic lattices [99].

Anderson localisation (AL) is a particularly intriguing process associated with wave propagation in random structures, where the presence of disorder results in the absence of diffusion [105, 106] and a localisation of the wave function. Unlike conventional studies of AL, in the work by Di Giuseppe et al. [107], the behaviour of separable as well as spatially extended Einstein-Podolsky-Rosen (EPR) photon

![](images/24f3f42ea880b2e73c3052a16696f734e384968463e62b58199bcc796f4cf1c6.jpg)  
Figure 14 Experimental setup utilised for observing two-photon correlations in ordered and Anderson lattices. A pump laser beam incident on a nonlinear crystal generates entangled photon pairs in an EPR state that are coupled into the waveguide array using a lens  $\mathsf{L}_1$ . The photon pairs at the output of the photonic lattice are coupled to two identical planes  $x_{1}$  and  $x_{2}$  using lens  $\mathsf{L}_2$  and beam splitter BS. The coincidence rates are measured via single-photon detectors (SPCM). Inset shows actual picture of the photonic samples [99].

pairs in waveguide arrays endowed with controllable disorder were considered. Since the separable two-photon input state is fully classical, localisation of the pair around the injection site is observed. This changes when considering the two-photon EPR state

$$
\begin{array}{l} | \psi_ {\mathrm {E P R}} \rangle = \frac {1}{\sqrt {2 N}} [ | 2 _ {1}, 0 _ {2}, \dots , 0 _ {N} \rangle + | 0 _ {1}, 2 _ {2}, \dots , 0 _ {N} \rangle \\ + \dots + \left| 0 _ {1}, 0 _ {2}, \dots , 2 _ {N} \right\rangle ] \tag {11} \\ \end{array}
$$

where the indices refer to the lattice sites. In that vein the two photons are always coupled into the same waveguide with equal probability,  $1 / N$ . This state is thus, by definition, spatially extended. It is important to emphasise that in actual Anderson experiments it is strictly necessary to perform ensemble-averages in order to obtain meaningful experimental results [106]. This, however, is not the case when the quantum parallelism, inherent to the spatially wide spread applied EPR states, is taken into account. In other words, the quantum superposition principle precludes the need to perform the statistical averaging necessary to observe localisation.

In the experiments two-photon input states are prepared by optical SPDC and launched into the waveguide structures. Their output coincidences are measured via single-photon detectors. The experimental setup is illustrated in Fig. 14. Exploiting the FLDW technology three waveguide arrays of 101 sites were fabricated: a periodic, a weakly disordered, and a strongly disordered array. The randomness of the arrays is induced by changing the coupling coefficients of the photonic lattices by varying the interwaveguide separations, thus, giving rise to the so-called off-diagonal disorder [108]. This is in contrast to the case of diagonal disorder [106], where the inter-waveguide distances are identical whereas the propagation constants are randomised.

![](images/abacf07c26385401a0877ec262261e234ca55b400d47635de82a897499ce64ba.jpg)  
Figure 15 Observations of Anderson-like co-localisation (AcL) of spatially entangled EPR photon pairs in disordered waveguide arrays. Columns: Correlation function of a separable two-photon state in periodic and disordered waveguide arrays along (a) periodic, (b) weakly disordered, and (c) highly disordered arrays after propagation of  $L = 5$  cm. Rows: (i) Calculated and (ii) measured coincidence rate  $G^{(2)}(x_1,x_2)$  as well as (iii) single-photon contribution  $G^{(1)}(x_1,x_1)$  and (iv) distribution of the diagonals [99].

Coupling an EPR state into  $N = 20$  adjacent waveguides, different landscapes emerge as presented in Fig. 15. On the one hand,  $G^{(2)}(x_1,x_2)$  is not factorisable (Fig. 15(i,ii)). The two off-diagonal peaks in the periodic case imply that the photons emerge on opposite sides of the array, that is, they tend to anti-bunch even though the pairs were coupled into the same waveguides (Fig. 15(a),(i,ii)). In the disordered arrays  $G^{(2)}(x_1,x_2)$  becomes extended along the diagonal,  $x_{1} = x_{2}$ , but localises along the  $x_{1} = -x_{2}$  direction (Fig. 15(b,c). On the other hand the singles profile  $G^{(1)}(x_1,x_1)$  mirrors the extension of  $G^{(2)}$  along  $x_{1} = x_{2}$  axis. Finally, integrating  $G^{(2)}$  along the diagonal  $x_{1} = x_{2}$  yields the probability distribution of the distance between both photons. It is clearly shown in Fig. 15(c)(iv) this distance localises (Anderson co-localisation) in a highly disordered lattice such that both will bunch and emerge from identical sites which is in strong contrast to the periodic case. As a consequence the spatial correlations between the photon pairs at the output on average are congruent to those at the input.

# 5.3. Two-photon quantum walks of distinguishable and indistinguishable photon pairs in two-dimensional waveguide arrays

In an experiment by Owens et al. a waveguide chip containing a ring of evanescently coupled waveguides is used to explore photon correlations in continuously coupled waveguide arrays which contain no inherent boundaries

![](images/884f18ba5b9b65023a82ecbfc0400e6f8eddde9e647ca882699c351b7efc6bfd.jpg)

![](images/87dd13d37d49931bac663dd61b88f2a82e674669f07e0a84c6a73de35115bf3b.jpg)

![](images/4234f7137b4e628420941e7c65bfd8cb6ea55194bfe37801213fea545d49c0eb.jpg)

![](images/243c064a8c540b2e1ceb435451dc86d5193a4ac12ff35f591f11ea60bda0b771.jpg)  
Figure 17 (a) Swiss cross waveguide array.  $C^{(1)}$  represents the coupling coefficients between adjacent channels, while  $C^{(2)}$  is the coupling constant among the nearest neighbours of the central waveguide guide. (b) Schematic of the interface section of the photonic circuit. (c-f) Correlation maps for two input configurations: Top row is for inputting the two photons on the same plane in opposite corners (X1 and X4). (c) and (d) show the coincidence measurements corresponding to distinguishable and indistinguishable photon pairs, respectively. (e) is a numerical simulation and (f) the violations (V), both for the case of indistinguishable photons. The bottom row shows the corresponding results for inputting the two photons in different planes in adjacent corners (X1 and Y1) [101].

![](images/8908165307d47706b52d08d30376846df1922798b12846206b11b56ab09dfdf6.jpg)  
Figure 16 (a) Schematic representation of the integrated waveguide circuit and associated output. At the input the waveguides are equally spaced by  $127\mu \mathrm{m}$ . They then converge via a two-stage fan-in to their eventual elliptical configuration. The inset is a CCD image of the output. (b-d) Experimentally observed and theoretically anticipated correlation maps for nearest-neighbour single-photon excitations of channels 1 and 2. Photon coincidence counts were recorded at each of the 36 pairs of output channels in a  $20\mathrm{s}$  time window. The measured (top row) and predicted (bottom row) correlation matrices for (b) temporally distinguishable photon pairs  $\Gamma^{\mathrm{d}}$ , (c) temporally indistinguishable simultaneous walkers  $\Gamma^{\mathrm{i}}$  and (d) their difference  $\Gamma^{\mathrm{d}} - \Gamma^{\mathrm{i}}$  [100].

![](images/6a403800c12041bc29be8589e0c7bdda4679035a8134837dc43101749a03a611.jpg)

![](images/8157d1100023cd64f016a8fd3c0d18e21189b9646a65f70d3724d0b87351bf92.jpg)

(see Fig. 16(a)) [100]. First, photons were prepared in such a way that they exhibited a time delay larger than their coherence times, so that they were temporally distinguishable. In the second case, the time delay was removed to synchronise the photons allowing for simultaneous two-site excitations, inducing quantum interference among the multiple modes, yielding a Hong-Ou-Mandel type effect [79].

Quantum interference effects were demonstrated through measurements of the second order correlation function which gives the probability of simultaneously detecting one photon at site  $q$  and the other at site  $r$ :

$$
\Gamma_ {q, r} = \frac {1}{1 + \delta_ {q , r}} \left| U _ {q, m} (z) U _ {r, n} (z) + U _ {q, n} (z) U _ {r, m} (z) \right| ^ {2}, \tag {12}
$$

where  $m$  and  $n \neq m$  are the injection guides. Here,  $U_{l,s}(z)$  represents the probability amplitude for detecting a photon after a propagation distance  $z$  at site  $l$  while originally launched at channel  $s$ .

As the results presented in Fig. 16 show, distinguishability of the photons inhibits quantum interference [109, 110] since the correlation matrices clearly indicate that both pho

![](images/eeb385ec39983a28d6bf8d279f0bf68c12c7a8cc03d972020c2ee666634b5cc6.jpg)

![](images/eb2c2b594185b77c5a6c2f6c6369986ade2f28f02571dbfc94af5caf0327e6aa.jpg)

![](images/65ac31f62cdab9066a7f557833d0d31769ee570e3e34f2787c88211bdd470c4b.jpg)

![](images/12826836664fb9b1390410e9d2d6bd644381cc08e5907fe2a5a117c3d9ccc6aa.jpg)

![](images/8277646a563a9bd701698a589d77e7bc2aa7ad0fdec1af2c5997b88d6cb83a79.jpg)

![](images/5eb67ddbacbe6a3c8d6a359ad5e1e943f501bc2c4ce8540e29249228cd3aa426.jpg)

![](images/bd85d3a47427bc7c140a688f8ee05808910bcc2e4d0725d6d4a8aabee162a253.jpg)

![](images/44dd72660fa9114bf26db7daf5306af804971db44dbc3b0c8248ee32040d8890.jpg)

![](images/b3c5b13d5a301ef435121d525de2e31f680b0e44acf7cde5bff75c372d87dc84.jpg)

![](images/5b7c90159dc1d7ef5222dcdb841b8f5ac721ce274479d3c405b29e05cffe2e43.jpg)

tons always separate and emerge from different waveguides (channels 2 and 6) since they travel independently from each other (Fig. 16(b)). Conversely, for the case when the photons become indistinguishable this behaviour is less likely (see Fig. 16(c) & (d)). Additionally, some extra biphoton states appear, as there is a noticeable probability that both photons emerge together from either the second or the sixth waveguide, or even separately from waveguides 4 and 6, etc. Similar results are obtained when sending photons into next-nearest neighbouring sites.

Additionally, we describe the QRW of correlated photon pairs using a two dimensional array in the form of a "Swiss cross" arrangement [101]. This particular photonic network is illustrated in Fig. 17, where waveguides that have first order coupling in the horizontal (vertical) plane are denoted with  $X(Y)$ . The central waveguide has first order coupling in both the horizontal and vertical plane and is labelled as  $C$ .

In the experiment two different configurations for the input states were considered. In the first case, separable photons are launched into waveguides  $X1$  and  $X4$ . For the second case, photons are launched into waveguides located on orthogonal planes, that is, at sites  $X1$  and  $Y1$ . By varying the relative time delay between the input photons, their indistinguishability was controlled. The non-classical nature of the correlations is verified through the violations

of the inequality [111]  $V_{q,r} = \frac{2}{3} \cdot \sqrt{\Gamma_{q,q}^{\mathrm{cl}} \Gamma_{r,r}^{\mathrm{cl}}} - \Gamma_{q,r}^{\mathrm{cl}} < 0$ , with  $\Gamma^{\mathrm{cl}}$  referring to intensity correlations between classical beams.

The experimental correlation matrices obtained in the experiment are shown in Fig. 17. From those maps one can recognise four areas, two corresponding to correlated detections between the output waveguides lying on the same plane  $(\Gamma_{X1 - X4,X1 - X4};\Gamma_{Y1 - Y4,Y1 - Y4})$  and two for the waveguides on different planes  $(\Gamma_{X1 - X4,Y1 - Y4};\Gamma_{Y1 - Y4,X1 - X4})$ . The coincidence measurements unambiguously demonstrate that for the case of indistinguishable photons the observed behaviour cannot be attributed to independent, 1D, single photon QRWs, but rather is characteristic for a 2D QRW of two correlated photons. Different strengths of the violations observed for each individual waveguide pair reflect the fact that bunching is not equally likely, due to the variety of photon paths contributing to the quantum interference.

# 6. Progress towards integration

To date laser inscribed waveguides have been used to demonstrate all of the requirements for an integrated linear optical quantum computer, albeit in isolation. Heralded photon sources have been produced from laser inscribed waveguides [65], while detectors can be incorporated onto laser inscribed chips [72]. A large range of small scale circuits and simulations have been performed showing the practicality of using laser inscribed circuits for prototype devices. The next steps in the field will be to enhance the fabrication techniques and to then use this to incorporate additional functionality and complexity into device designs.

# 6.1. Sources and photon state engineering

In addition to producing circuits the FLDW technique has been shown to be useful both at the production and collection of heralded single photons. A heralded single photon source is a photon source which produces two photons simultaneously but stochastically: one of the photons is detected thus heralding the presence of the other photon. Properly engineered, a heralded photon source can be an excellent approximation to a true single photon source. Traditionally these coincident photons have been produced using nonlinear three wave mixing processes. However most quantum optics demonstrations requiring single photons have used a bulk optic source and collected the downconverted photons into optical fibres (as in Fig. 3). This approach is neither scalable nor efficient since overlapping multiple spatial modes on a crystal is challenging. In recent years, there has been substantial progress towards developing fully integrated single photon sources in a number of platforms, and using both quadratic and cubic nonlinearities (see [112-114] for several reviews in this area).

This strategy is also possible in the direct written waveguide platform. Recently, an FLDW waveguide in silica glass has been used to produce heralded photons through spon

![](images/c27a0627585641026dee8965aabc90c417aaf6ca86f9d6e6f5b4609471a9e896.jpg)  
Figure 18 A hybrid integrated circuit which incorporates linear components, manufactured using FLDW, to pump and spatially separate heralded single photons from four modes simultaneously [115].

taneous four wave mixing (SFWM) [65]. This relies on a  $\chi^{(3)}$  nonlinearity which is small in fused silica glass but is offset by the fact that the extraction efficiency of the waveguides are excellent. The intrinsic birefringence of the waveguide was used to accomplish the necessary phase-matching of the SFWM process. High purity heralded single photons were produced using this scheme, which points to the potential of producing multiple identical waveguides and pumping them simultaneously. However, an alternative approach is to exploit high efficiency waveguides in  $\chi^{(2)}$  nonlinear materials, such as periodically poled lithium niobate (PPLN), to produce photon pairs (see Fig. 18). The advantage of this is that by using periodic poling a phase matching condition can be fulfilled for a larger range of pump, signal and idler wavelengths. By hybrid interfacing PPLN directly with laser inscribed waveguide circuits it is possible to gain an advantage over using the two platforms in isolation [115]. PPLN is an excellent nonlinear material, yet it is not ideal for simple linear operations. The FLDW technique is excellent for low loss photon routing and linear devices like beamsplitters and wavelength demultiplexers (WDM). Since the optical modes are closely matched it is possible to efficiently couple light between PPLN proton exchanged waveguides and FLDW waveguides [115].

Waveguide processing is advancing and optimised structures for both the collection and transmission of light at  $800\mathrm{nm}$  and telecommunication wavelengths are progressing [115-117]. Additional chip density is possible by using novel three dimensional interaction regions to produce multimode transformations or to stack circuit elements vertically. One clear path toward increasing chip density is to increase the maximum obtainable refractive index contrast available when producing laser inscribed waveguides. The minimum bend radius is dependent on the refractive index contrast of a waveguide and hence by increasing this it is possible to reduce the minimum bending radius and

therefore structures like directional couplers can be produced with a smaller footprint. A minimum bend radius in silicon can be as small as a few hundred microns for refractive index contrasts of 0.5-1. In laser inscribed waveguides Eaton et al. have shown that it is possible to obtain refractive index contrasts up to  $2.2 \times 10^{-2}$  [59] compared with commonly reported values of  $0.5 \times 10^{-2}$  [118]. These values result in a minimum bend radius of a few mm which limits the minimum beamsplitter size since waveguides must fold in to and out of an evanescent coupling region. An alternative route to increasing circuit density and functionality is to incorporate functions such as detection and photon generation on chip. Significant progress has been made in this area using both a hybrid integration approach [115] and exploiting the inherent nonlinearity of silica waveguides [65]. By incorporating photon pair sources on chip a large reduction in overall resource requirements is achieved. Enhancing the photon generation efficiency could be achieved by reducing the effective mode area of the waveguide or using novel methods or substrates to enhance the nonlinearity of the material.

The relationship between the effective mode area,  $A_{\mathrm{eff}} = \frac{\pi}{4}\mathrm{MFD}^2$  and the nonlinear process efficiency is,

$$
\gamma = \frac {\omega n _ {2}}{c A _ {\text {e f f}}} \tag {13}
$$

where  $MFD$  is the mode field diameter,  $n_2$  is the nonlinear refractive index,  $\omega$  is the angular frequency of the light and  $c$  is the speed of light in vacuum. Measurements of the nonlinear refractive index in fused silica have found similar values in laser written waveguides of 30-90% of the bulk material of  $2.7 \times 10^{-20} \mathrm{~m}^2/\mathrm{W}$  dependent on the writing velocity [119]. Although it is important to note that these measurements did observe that  $n_2$  was much more strongly affected than the linear refractive index during laser processing.

Spring et al. have shown that the high extraction efficiency from laser written waveguides compensates for the lower production efficiency compared to other materials [65]. These source have even been scaled to multiple indistinguishable devices across a single chip [120]. Furthermore the nonlinearity of the amorphous  $\chi^{(3)}$  material can be enhanced using thermal poling methods to produce an effective second order nonlinearity from a third order nonlinearity [121, 122]. This process uses a high voltage applied across a sample while it is heated and once it cools to room temperature this electrostatic field is frozen into the material. The resulting  $\chi_{\mathrm{eff}}^{(2)}$  is related to  $\chi^{(3)}$  through  $\chi_{\mathrm{eff}}^{(2)} = 3\chi^{(3)}E_{\mathrm{fixed}}$ , where an electric field  $E_{\mathrm{fixed}}$  is frozen within the glass structure. This was initially applied to laser written waveguides by Corbari et al. and later an electro-optically tuned Mach-Zehnder was produced exploiting this technique [123, 124]. Thermal poling has been applied to laser written waveguides in Eagle-2000 glass and the results do show a higher nonlinearity that that of the bulk glass and of unmodified fused silica [124-126]. The electro-optic and optical nonlinearity could then potentially be exploited in a waveguide circuit composed of Eagle-2000 which has in

![](images/ad0257880152519b7090169e47328f0bdf31914367d9f2d238423891c1835eee.jpg)  
Figure 19 A 3D tunable circuit for multidimensional quantum metrology. One waveguide in the three path Mach-Zehnder interacts with the chip's surface meaning a phase shift applied through heat or otherwise can be sensed [139].

herently low insertion loss. By using glasses with a higher  $\chi^{(3)}$  the effective  $\chi_{\mathrm{eff}}^{(2)}$  will therefore be higher. Laser written waveguides have been produced in chalcogenide glasses, such as gallium lanthanum sulphide (GLS), with transmission losses as low as  $0.65~\mathrm{dB / cm}$  [127]. It has been shown that the nonlinearity of the modified material is preserved after illumination[128, 129]. Directional couplers and even waveguide Bragg gratings (WBG) have been fabricated in GLS showing the potential for quantum integrated circuit applications exploiting this material [130, 131]. By exploiting this material's nonlinear properties it would be possible to produce highly nonlinear waveguides capable of high efficiency heralded single photon generation. For many applications, narrow-band photons are required, which can be achieved in high Q resonances [11, 12, 132]. Waveguide Bragg grating structures have been produced using the FLDW technique [133, 134] as well as the laser writing and subsequent etching of high Q microcavities [135].

# 6.2. Reconfigurable circuits

One of the unique features of the laser inscription process is its potential for producing structures in three dimensions within a substrate. This can be exploited to produce waveguide interactions which are extremely challenging using two dimensional means. Three mode transformations have been produced in substrates using a single three mode evanescently coupled region [136, 137]. Furthermore it has been proposed theoretically and recently demonstrated that these devices could have potential in quantum metrology [138, 139]. Multimode interferometers can have multiple spatially separated photons injected into their input ports simultaneously which means a subset of the resulting fringes can be selected which contain maximally path entangled states of photons distributed across multiple arms. This advantage combined with the ease with which FLDW circuits can be used to both produce compact interaction regions and interact with the surface of a waveguide chip mean that useful multimode interference devices can be produced. The design of a circuit capable of interacting directly with the surface of a waveguide chip in shown in Fig. 19.

![](images/3db3d2cd79648f202170eb1fdf087d2f8be9977e4af35f47f9c8575d1e4489e7.jpg)  
Figure 20 Top: Sketch of the 1-to-8 optical integrated multiplexer consisting of three beam splitting stages. The output fields are fed into APDs. Bottom: Output click statistic of the above multiplexer for classical attenuated laser light (blue), as well as single-photon Fock-states (green). In the experiment, both input states yield a flat uniform output statistic provided by the high quality of the optical integrated device [140].

# 6.3. Integrated detection scheme

As explored in the present review, current advances in the fabrication techniques of photonic structures may allow for integration of the main components required for scalable photonic quantum sensors, quantum information processors, and possibly an on-chip quantum computer.

In order to exemplify the potential of integrated photonics structures in the area of quantum sensors, in this section we refer to an on-chip realisation of a single-photon counter device [140]. Such an approach is based on a divide-and-conquer technique in which incident photon fluxes encounter an engineered environment that causes the initial wave functions to evolve into a uniform superposition of states. Interestingly, the counting and characterisation of the photons were achieved through the click-statistics obtained from standard on-off detectors.

The equal splitting of the photon fields was achieved using an integrated discrete network of integrated 50/50 beam splitters yielding a total of  $N = 8$  output channels (see Fig. 20). In order to demonstrate the feasibility of this scheme, Heilmann and collaborators consider two limiting cases as input states for their experiments: 1) low-intensity laser light, which can be idealised as a quantum coherent state [15]; and 2) heralded single photons produced by spontaneous parametric down conversion, which approximately represents an ideal single-photon Fock state [15].

In the first scenario, classical coherent states  $|\psi_{\mathrm{in}}\rangle = |\alpha \rangle$  are expected to split into eight spatially separated coherent

states of equal amplitude,

$$
\left| \psi_ {\text {o u t}} \right\rangle = \left| - \alpha^ {\prime} \right\rangle \left| \mathrm {i} \alpha^ {\prime} \right\rangle \left| \alpha^ {\prime} \right\rangle \left| \mathrm {i} \alpha^ {\prime} \right\rangle \left| - \alpha^ {\prime} \right\rangle \left| \mathrm {i} \alpha^ {\prime} \right\rangle \left| - \alpha^ {\prime} \right\rangle \left| - \mathrm {i} \alpha^ {\prime} \right\rangle \tag {14}
$$

with  $-\alpha' = \alpha / \sqrt{8}$ . Accordingly, a perfect photon counting characterisation of such a state must yield a Poissonian photon number distribution [141]. Correspondingly, the click-statistics results in a binomial distribution of the counts [142]. Similarly, in case of a sub-(super-) Poissonian photon-number distribution, the click statistics are sub-(or super-) binomial [143, 144]. Owing to this one-to-one correspondence between actual photon-counts and click-statistics, it is possible to use the so-called  $Q_B$  parameter for quantifying the binomial character of the click-statistics. More specifically, superbinomial click statistics such as those of laser light are characterised by  $Q_B > 0$ , while genuine quantum entities, such as Fock states, necessarily feature  $Q_B < 0$  [142].

In a first set of experiments, the click measurements for the classical coherent state the extracted  $Q_B$  parameter was positive,  $Q_B = (1.712 \pm 00.26) \times 10^{-2}$ , confirming that indeed the click statistics is super-binomial as expected for a classical light source. In the second set of experiments, the device was used to characterise the fidelity of a heralded single-photon source based on spontaneous parametric down conversion. As in the previous case, the input single-photon state,  $|\psi_{\mathrm{in}}\rangle = a^{\dagger}|0\rangle$ , is spatially distributed and thus transformed according to the expression  $|\psi_{\mathrm{out}}\rangle = (-a_1^\dagger + \mathrm{i}a_2^\dagger + a_3^\dagger + \mathrm{i}a_4^\dagger - a_5^\dagger + \mathrm{i}a_6^\dagger - a_7^\dagger - \mathrm{i}a_8^\dagger)|0\rangle / \sqrt{8}$ , where  $a_l^\dagger$  represents the bosonic creation operators of the  $l$ -th waveguide mode. In this case, measurement data clearly demonstrates the non-classicality of the input state, with  $Q_B = (-2.002 \pm 0.049) \times 10^{-2} < 0$ .

Through these experiments, the authors introduce a new paradigm for integrated photon-number resolved measurements based on distributed sensing with multiplexed arrays of conventional on-off detectors. In addition, it was demonstrated that measuring the click statistics of the detector ensemble provides the means to determine the actual photon-counting statistics. Consequently, this technique can in principle be scaled to allow counting arbitrarily high numbers of incident photons, irrespective of the dead time and quantum efficiency of the individual detectors used.

# 7. Conclusion and outlook

This review has outlined the range of advances which have resulted from the use of femtosecond laser direct-written waveguides for quantum information science applications. This waveguide fabrication approach is well suited to the current state of the art in this application domain, since quantum information demonstrations demand low loss circuits which are transparent at visible wavelengths and can be rapidly prototyped. In addition the excellent mode

overlap between a single mode fibre and laser inscribed glass waveguides circuits mean interfacing waveguides with standard optical equipment is convenient. Universal quantum computing can be realised by means of a simple set of basic gates, which are CNOT-, Hadamard- and  $\pi /8$ -phase-gate, all of which have been demonstrated using laser inscribed waveguide circuits. Furthermore, due to the 3D capabilities of the FLDW technique more complex gate operations are feasible. In particular it has allowed the implementation of a range of simulations of condensed matter phenomena. In the future it is anticipated that the laser inscription technique will continue to be a valuable prototyping tool and particularly useful for novel 3D strutcutres.

The next steps for the laser inscription technique will be to increase the complexity of current circuit designs. This could be achieved in novel ways such as layering devices in three dimensions. Alternatively exotic glasses such as chalcogenides could be exploited to enable incorporation of nonlinear optical functions into conventional devices. Furthermore it should be possible to continue to include tunable elements into waveguide circuits, such as thermal phase shifters to produce reconfigurable circuits. Finally on chip detection should be possible by bringing waveguides close to the surface of the waveguide chip.

Acknowledgement. This research was conducted in part by the Australian Research Council Centre of Excellence for Ultrahigh bandwidth Devices for Optical Systems (CE110001018) and the Optofab node of the Australian National Fabrication Facility. TM acknowledges a fellowship from the Marie Sklodowska-Curie action "PICQUE" Grant No. 608062. SG acknowledges funding by a Macquarie University Research Fellowship (MQRF). This work was supported by the Marie Curie Actions within the Seventh Framework Programme for Research of the European Commission, under the Initial Training Network PICQUE, Grant No. 608062. The authors further gratefully acknowledge financial support from the German Ministry of Education and Research (Center for Innovation Competence program, Grant No. 03Z1HN31), the Thuringian Ministry for Education, Science and Culture (Research group Spacetime, Grant No. 11027-514), and the Deutsche Forschungsgemeinschaft (Grant No. NO462/6-1).

Received: 29 August 2014, Revised: 23 February 2015

Accepted: 27 March 2015

Published online: 23 July 2015

Key words: Quantum information, quantum computation, photonic integrated circuits, laser materials processing, waveguides.

![](images/e71785c541e2f73fc44d2971a23173a1340813eb9f847eb42b60b2f5da2b9b47.jpg)

Thomas Many graduated with a B.Sc. (1st) in Applied Physics and Electronics from the National University of Ireland, Galway in 2010. He undertook a Ph.D. in the Centre for Ultrahigh bandwidth Devices for Optical Systems (CUDOS) in Macquarie University and graduated in 2014. Thomas currently works as a Marie Curie Fellow in the Cambridge

research laboratory of Toshiba Research Europe on appli

cations of quantum optics and semiconductor physics. Visit www.laserwrittencircuits.com for more information about the state of the art in laser inscribed devices.

![](images/f1b741568873374e9343aef5cfc659804699265ccd6f7a3540255dd93f03d222.jpg)

Markus Gräfe received his Diploma degree at Friedrich-Schiller-Universität Jena (Germany) in 2012. He currently works as a Ph.D. student in the group of Professor Alexander Szameit at the Institute of Applied Physics Jena. His research fields are integrated optics and quantum photonics.

![](images/ad6bdd634d46d634a28c9eace95e80b78db160e9eb06133e20413f6a139cb5b2.jpg)

René Heilmann received his Diploma degree at Friedrich-Schiller-Universität Jena (Germany) in 2009. After two years working in R&D for a worldwide laser company he started as a Ph.D. student in the group of Professor Alexander Szameit at the Institute of Applied Physics Jena. His research fields are integrated optics and quantum photonics.

![](images/5e1a4a06c500f2a201ead4f99285c7b1a013c1115d518ad14aafe97fa5642621.jpg)

Armando Perez-Leija received his Ph.D. degree at the National Institute of Astrophysics, Optics, and Electronics, Puebla, Mexico. He spent from 2011-2013 as PostDoc at CREOL- The college of Optics and Photonics in the UCF (USA) in Professors's Christodoulides group. In 2013, he joined the group of Professor Alexander Szameit at the Friedrich-Schiller-Universität Jena (Germany).

![](images/737a3cd8d7cb7c0a9f3950def08ee2cb4dc76212991cf9667d6d35a0fe3af369.jpg)

Simon Gross received his M.Sc. degree in Microelectronics from the Vienna University of Technology, Austria and Ph.D. degree in Physics from Macquarie University, Australia in 2009 and 2013, respectively. He is research fellow at the MQ Photonics Research Centre and Centre for Ultrahigh Bandwidth De

vices for Optical Systems (CUDOS) at Macquarie University. His research interest are the application of ultrafast lasers to optical materials processing in particular laser direct-writing of photonic waveguide devices for telecommunication, sensing and astronomical applications. He is a member of the Australian Optical Society and the Optical Society of America and SPIE.

![](images/115496f73fbc5c842efa41b533628bd05a5d2b6f0ba29de2e6f229e02711cec4.jpg)

Michael J. Steel received a B. Sc. (Hons) and Ph.D. in nonlinear optical physics from the University of Sydney in 1993 and 1996 respectively. After conducting postdoctoral research in nonlinear optics and quantum optics, he spent seven years with RSoft Design Group, Inc. developing photonic design software including the widely-used photonic crystal tool Band-SOLVE. He is currently an Associate

Professor in Physics at Macquarie University. His research interest include nonlinear optics, both quantum and classical, nonlinear optoacoustics and nonreciprocal optics.

![](images/b49c3f76720803fc80fa12b6a44a4f309fe56877f7ba6935c2356ef373a4753a.jpg)

Michael J. Withford is a member of the MQ Photonics Research Centre, which includes  $>100$  members - staff and students. He also leads both the Macquarie University node of Australian Research Council (ARC) Centre of Excellence: Ultrahigh-bandwidth Devices for Optical Systems (CUDOS) and the OptoFab Node of the Australian National Fab

rication Facility. Prof. Withford holds several patents and has published over 100 refereed journal papers and several hundred conference papers. He is an Associate Editor for Optics Express and an OSA Fellow.

![](images/cb760536bb83978f777866e621858cf2b806b441e48e2f5e92bd00fc29338b05.jpg)

Alexander Szameit received his Physics Diploma and Ph.D. at the Friedrich-Schiller-Universität Jena (Germany) in 2004 and 2007, respectively. He spent from 2009-2011 as PostDoc at the Technion in Haifa (Israel) in Moti Segev's group and returned in 2011 as Assistant Professor to Jena. His research interests include integrated quantum photonics, light evolution in coupled

waveguide systems, and discrete nonlinear dynamics. He received several awards for his work, such as the dissertation prize of the German Physical Society, the Adolph Lomb Medal of the Optical Society of America, and the Rudolph Kaiser Prize for experimental physics.

# References

[1] W. Bogaerts, R. Baets, P. Dumon, V. Wiaux, S. Beckx, D. Taillaert, B. Luyssaert, J. Van Campenhout, P. Bienstman, and D. Van Thourhout, J. Lightw. Technol. 23, 401-412 (2005).  
[2] J. S. Orcutt, A. Khilo, C. W. Holzwarth, M. A. Popovic, H. Li, J. Sun, T. Bonifield, R. Hollingsworth, F. X. Kärtner, H. I. Smith, V. Stojanović, and R. J. Ram, Opt. Express 19, 2335-2346 (2011).  
[3] J. S. Orcutt, B. Moss, C. Sun, J. Leu, M. Georgas, J. Shainline, E. Zgraggen, H. Li, J. Sun, M. Weaver, S. Urošević, M. Popović, R. J. Ram, and V. Stojanović, Opt. Express 20, 12222-12232 (2012).  
[4] M. Wade and M. Popovic, Opt. Express 21, 10903-10916 (2013).  
[5] J. Leuthold, C. Koos, and W. Freude, Nat. Photon. 4, 535-544 (2010).  
[6] S. M. Hendrickson, A. C. Foster, R. M. Camacho, and B. D. Clader, J. Opt. Soc. Am. 31, 3193-3203 (2014).  
[7] J. E. Sharping, K. F. Lee, M. A. Foster, A. C. Turner, B. S. Schmidt, M. Lipson, A. L. Gaeta, and P. Kumar, Opt. Express 14, 12388-12393 (2006).  
[8] N. C. Harris, D. Grassani, A. Simbula, M. Pant, M. Galli, T. Baehr-Jones, M. Hochberg, D. Englund, D. Bajoni, and C. Galland, Phys. Rev. X 4, 041047 (2014).  
[9] H. Takesue, N. Matsuda, E. Kuramochi, W. J. Munro, and M. Notomi, Nat. Comm. 4, 1-7 (2013).

[10] J. W. Silverstone, D. Bonneau, K. Ohira, N. Suzuki, H. Yoshida, N. Iizuka, M. Ezaki, C. M. Natarajan, M. G. Tanner, R. H. Hadfield, V. Zwiller, G. D. Marshall, J. G. rarity, J. L. O'Brien, and M. G. Thompson, Nat. Photon. 8, 104-108 (2014).  
[11] F. Monteiro, A. Martin, B. Sanguinetti, H. Zbinden, and R. T. Thew, Opt. Express 22, 4371-4378 (2014).  
[12] C. Reimer, L. Caspani, M. Clerici, M. Ferrera, M. Kues, M. Peccianti, A. Pasquazi, L. Razzari, B. E. Little, S. T. Chu, D. J. Moss, and R. Morandotti, Opt. Express 22, 6535-6546 (2014).  
[13] A. Politi, M. J. Cryan, J. G. Rarity, S. Yu, and J. L. O'Brien, Science 320, 646-649 (2008).  
[14] K. M. Davis, K. Miura, N. Sugimoto, and K. Hirao, Opt. Lett. 21, 1729-1731 (1996).  
[15] C. C. Gerry and P. L. Knight, Introductory quantum optics (Cambridge University Press, 2005).  
[16] P. Kok and B. Lovett, Introduction to optical quantum information processing, 1st edition (Cambridge university press, 2010).  
[17] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information 10th Anniversary Edition, 10th anniversary edition (Cambridge university press, Cambridge, 2010).  
[18] S. Aaronson, http://www.scottaarson.com/blog/  
[19] P. Shor, Algorithms for quantum computation: discrete logarithms and factoring, in: Proceedings of the 35th Annual Symposium on Foundations of Computer Science, (IEEE Computer Society Press, Santa Fe, NM, 1994), 124-134.  
[20] A. Politi, J. C. F. Matthews, and J. L. O'Brien, Science 325, 1221 (2009).  
[21] D. Englund, A. Majumdar, M. Bajcsy, A. Faraon, P. Petroff, and J. Vuckovic, Phys. Rev. Lett. 108, 1-5 (2012).  
[22] V. Loo, C. Arnold, O. Gazzano, A. Lemaitre, I. Sagnes, O. Krebs, P. Voisin, P. Senellart, and L. Lanco, Phys. Rev. Lett. 109, 1-5 (2012).  
[23] E. Knill, R. Laflamme, and G. Milburn, Nature 409, 46-52 (2001).  
[24] A. Zeilinger, Am J. Phys. 49, 882 (1981).  
[25] H. Fearn and R. Loudon, J. Opt. Soc. Am. B 6, 917-927 (1989).  
[26] Z. Y. Ou, Phys. Rev. A 37, 1607-1619 (1988).  
[27] T. Pittman, D. Strekalov, A. Migdall, M. Rubin, A. Sergienko, and Y. Shih, Phys. Rev. Lett. 77, 1917-1920 (1996).  
[28] H. Misawa and S. Juodkazis (eds.), 3D Laser Microfabrication: Principles and Applications, 1 edition (Wiley-VCH Verlag GmbH & Co. KGaA, Weinheim, FRG., 2006).  
[29] R. Osellame, G. Cerullo, and R. Ramponi (eds.), Femtosecond Laser Micromachining photonic and microfluidic devices in transparent materials (Springer-Verlag, 2012).  
[30] N. Anscombe, Nat. Photon. 4, 22-23 (2010).  
[31] Y. Bellouard, A. Champion, B. Lenssen, M. Matteucci, A. Schaap, M. Beresna, C. Corbari, M. Gecevicius, P. Kazansky, O. Chappuis, M. Kral, R. Clavel, F. Barrot, J. M. Breguet, Y. Mabillard, S. Bottinelli, M. Hopper, C. Hoenninger, E. Mottay, and J. Lopez, Journal of Laser Micro/Nanoengineering 7, 1-10 (2012).  
[32] Optoscribe Ltd., 3D MMux Photonic Lantern, Tech. rep., Kirkton Campus, Livingston, West Lothian, 2014.

[33] B. J. Smith, D. Kundys, N. Thomas-Peter, P. G. R. Smith, and I. A. Walmsley, Opt. Express 17, 13516-13525 (2009).  
[34] K. Itoh, W. Watanabe, S. Nolte, and C. Schaffer, MRS bulletin 31, 620-625 (2006).  
[35] L. Sudrie, M. Franco, B. Prade, and A. Mysyrowicz, Opt. Commun. 191, 333-339 (2001).  
[36] Y. Shimotsuma, P. Kazansky, J. Qiu, and K. Hirao, Phys. Rev. Lett. 91, 247405 (2003).  
[37] E. N. Glezer, M. Milosavljevic, L. Huang, R. J. Finlay, T. H. Her, J. P. Callan, and E. Mazur, Opt. Lett. 22, 422 (1997).  
[38] J. Chan, T. Huser, S. Risbud, and D. Krol, Appl. Phys. A 76, 367-372 (2003).  
[39] D. J. Little, M. Ams, S. Gross, P. Dekker, C. T. Miese, A. Fuerbach, and M. J. Withford, J. Raman Spect. 42, 715-718 (2011).  
[40] C. Schaffer, J. Garcia, and E. Mazur, Appl. Phys. A 76, 351-354 (2003).  
[41] S. M. Eaton, M. L. Ng, J. Bonse, A. Mermillod-Blondin, H. Zhang, A. Rosenfeld, and P. R. Herman, Appl. Opt. 47, 2098–102 (2008).  
[42] S. Kanehira, K. Miura, and K. Hirao, Appl. Phys. Lett. 93, 023112 (2008).  
[43] G. Cerullo, R. Osellame, S. Taccheo, M. Marangoni, D. Polli, R. Ramponi, P. Laporta, and S. De Silvestri, Opt. Lett. 27, 1938-1940 (2002).  
[44] M. Ams, G. Marshall, D. Spence, and M. Withford, Opt. Express 13, 5676-5681 (2005).  
[45] S. Gross, M. Ams, G. Palmer, C. T. Miese, R. J. Williams, G. D. Marshall, A. Fuerbach, D. G. Lancaster, H. Ebendorff-Heidepriem, and M. J. Withford, Int. J. of Appl. Glass Sci. 3, 332–348 (2012).  
[46] S. Gross, D. G. Lancaster, H. Ebendorff-Heidepriem, T. M. Monro, A. Fuerbach, and M. J. Withford, Opt. Mat. Express 3, 574 (2013).  
[47] D. G. Lancaster, S. Gross, H. Ebendorff-Heidepriem, K. Kuan, T. M. Monro, M. Ams, A. Fuerbach, and M. J. Withford, Opt. Lett. 36, 1587 (2011).  
[48] A. G. Okhrimchuk, A. V. Shestakov, I. Khrushchev, and J. Mitchell, Opt. Lett. 30, 2248-2250 (2005).  
[49] F. Chen, and J. R. JV. de Aldana, Laser Photon. Rev. 8, 251-275 (2013).  
[50] L. Gui, B. Xu, and T. Chong, IEEE Photon. Technol. Lett. 16, 1337-1339 (2004).  
[51] A. Rodenas and A. K. Kar, Opt. Express 19, 17820-17833 (2011).  
[52] C. Miese, S. Gross, M. J. Withford, and A. Fuerbach, Opt. Mat. Express 5, 323 (2015).  
[53] J. Burghoff, C. Grebing, S. Nolte, and A. Tünnermann, Appl. Phys. Lett. 89, 081108 (2006).  
[54] J. Burghoff, S. Nolte, and A. Tünnermann, Appl. Phys. A 89, 127-132 (2007).  
[55] C. Hnatovsky, R. S. Taylor, E. Simova, V. R. Bhardwaj, D. M. Rayner, and P. B. Corkum, J. Appl. Phys. 98, 013517 (2005).  
[56] A. Jesacher, G. D. Marshall, T. Wilson, and M. J. Booth, Opt. Express 18, 656-661 (2010).  
[57] Y. Nasu, M. Kohtoku, and Y. Hibino, Opt. Lett. 30, 723-725 (2005).

[58] T. Meany, L. A. Ngah, M. J. Collins, A. S. Clark, R. J. Williams, B. J. Eggleton, M. J. Steel, M. J. Withford, O. Alibart, and S. Tanzilli, Laser Photon. Rev. 8, L42-L46 (2014).  
[59] S. M. Eaton, M. L. Ng, R. Osellame, and P. R. Herman, J. Non-Cryst. Solids 357, 2387-2391 (2011).  
[60] A. Arriola, S. Gross, N. Jovanovic, N. Charles, P. G. Tuthill, S. M. Olaizola, A. Fuerbach, and M. J. Withford, Opt. Express 21, 2978 (2013).  
[61] G. D. Marshall, A. Politi, J. C. F. Matthews, P. Dekker, M. Ams, M. J. Withford, and J. L. O'Brien, Opt. Express 17, 12546-12554 (2009).  
[62] C. K. Hong, Z. Y. Ou, and L. Mandel, Phys. Rev. Lett. 59, 2044-2046 (1987).  
[63] N. Boeuf, D. Branning, I. Chaperot, E. Dauler, S. Guearin, G. Jaeger, A. Muller, and A. Migdall, Opt. Eng. 39, 1016-1024 (2000).  
[64] R. Rangarajan, M. Goggin, and P. Kwiat, Opt. Express 17, 18920-18933 (2009).  
[65] J. Spring, P. S. Salter, B. J. Metcalf, P. C. Humphreys, M. Moore, N. Thomas-Peter, M. Barbieri, X. M. Jin, N. Langford, M. J. Booth, and I. A. Walmsley, Opt. Express 21, 5932-5935 (2013).  
[66] L. Sansoni, F. Sciarrino, G. Vallone, P. Mataloni, A. Crespi, R. Ramponi, and R. Osellame, Phys. Rev. Lett. 105, 200503 (2010).  
[67] L. A. Fernandes, J. R. Grenier, P. R. Herman, J. S. Aitchison, and P. V. S. Marques, Opt. Express 19, 18294-18301 (2011).  
[68] L. A. Fernandes, J. R. Grenier, P. R. Herman, J. S. Aitchison, and P. V. S. Marques, Opt. Express 20, 24103 (2012).  
[69] R. Heilmann, M. Gräfe, S. Nolte, and A. Szameit, Sci. Rep. 4, 4118 (2014).  
[70] G. Corrielli, A. Crespi, R. Geremia, R. Ramponi, L. Sansoni, A. Santinelli, P. Mataloni, F. Sciarrino, and R. Osellame, Nat Commun. 5, 4249 (2014).  
[71] A. Crespi, R. Osellame, R. Ramponi, L. Sansoni, I. Bongioanni, F. Sciarrino, G. Vallone, and P. Mataloni, Nat. Commun. 2, 556 (2011).  
[72] T. Gerrits, N. Thomas-Peter, J. C. Gates, A. E. Lita, B. J. Metcalf, B. Calkins, N. A. Tomlin, A. E. Fox, A. L. Linares, J. B. Spring, N. K. Langford, R. P. Mirin, P. G. R. Smith, I. A. Walmsley, and S. W. Nam, Phys. Rev. A 84, 60301 (2011).  
[73] B. Calkins, P. Mennea, and A. Lita, Opt. Express 21, 22657-22670 (2013).  
[74] T. Meany, M. Delanty, M. J. Steel, M. J. Withford, D. N. Biggerstaff, M. A. Broome, A. Fedrizzi, A. G. White, A. Gilchrist, and G. D. Marshall, arXiv:1502.03386 (2015).  
[75] E. Knill, Phys. Rev. A 66, 052306 (2002).  
[76] S. Rahimi-Keshari, M. A. Broome, R. Fickler, A. Fedrizzi, T. C. Ralph, and A. G. White, Opt. Express 21, 13450-13458 (2013).  
[77] J. Mower, N. C. Harris, G. R. Steinbrecher, and D. Englund; arXiv:1406.3255v3 (2014).  
[78] S. Aaronson and A. Arkhipov, The computational complexity of linear optics, in: Proceedings of the Forty-third Annual ACM Symposium on Theory of Computing, STOC '11 (ACM, New York, NY, USA, 2011), 333-342.

[79] C. K. Hong, Z. Y. Ou, and L. Mandel, Phys. Rev. Lett. 59, 2044-2046 (1987).  
[80] M. Tillmann, B. Dakic, R. Heilmann, S. Nolte, A. Szameit, and P. Walther, Nat Photon. 7, 540-544 (2013).  
[81] M. A. Broome, A. Fedrizzi, S. Rahimi-Keshari, J. Dove, S. Aaronson, T. C. Ralph, and A. G. White, Science 339, 794-798 (2013).  
[82] J. B. Spring, B. J. Metcalf, P. C. Humphreys, W. S. Kolthammer, X. M. Jin, M. Barbieri, A. Datta, N. Thomas-Peter, N. K. Langford, D. Kundys, J. C. Gates, B. J. Smith, P. G. R. Smith, and I. A. Walmsley, Science 339, 798-801 (2013).  
[83] A. Crespi, R. Osellame, R. Ramponi, D. J. Brod, E. F. Galvao, N. Spagnolo, C. Vitelli, E. Maiorino, P. Mataloni, and F. Sciarrino, Nat Photon. 7, 545-549 (2013).  
[84] W. Dür, G. Vidal, and J. I. Cirac, Phys. Rev. A 62, 062314 (2000).  
[85] J. Joo, Y. J. Park, S. Oh, and J. Kim, New J. Phys. 5, 136 (2003).  
[86] H. Yuan, J. Song, X. Y. Liu, S. Cheng, K. Hou, and L. F. Han, Int. J. Quant. Inform. 09, 607-614 (2011).  
[87] M. Gräfe, R. Heilmann, A. Perez-Leija, R. Keil, F. Dreisow, M. Heinrich, H. Moya-Cessa, S. Nolte, D. N. Christodoulides, and A. Szameit, Nat. Photon. 8, 791-795 (2014).  
[88] S. B. Papp, K. S. Choi, H. Deng, P. Lougovski, S. J. van Enk, and H. J. Kimble, Science 324, 764-768 (2009).  
[89] P. Lougovski, S. J. van Enk, K. S. Choi, S. B. Papp, H. Deng, and H. J. Kimble, New J. Phys. 11, 063029 (2009).  
[90] O. Gühne and G. Tóth, Physics Reports 474, 1-75 (2009).  
[91] A. Rukhin, J. Soto, J. Nechvatal, M. Smid, E. Barker, S. Leigh, M. Levenson, M. Vangel, D. Banks, A. Heckert, J. Dray, and S. Vo, A statistical test suite for random and pseudorandom number generators for cryptographic applications, Special publication, National Institute of Standards and Technology (U.S.), 2010.  
[92] A. G. White, A. Gilchrist, G. J. Pryde, J. L. O'Brien, M. J. Bremner, and N. K. Langford, J. Opt. Soc. Am. B 24, 172 (2007).  
[93] S. Rahimi-Keshari, M. A. Broome, R. Fickler, A. Fedrizzi, T. C. Ralph, and A. G. White, Opt. Express 21, 13450-13458 (2013).  
[94] R. Heilmann, M. Gräfe, S. Nolte, and A. Szameit, Science Bulletin 60, 96-100 (2015).  
[95] N. Bowditch, Memoirs Amer. Acad. of Arts and Sciences 3, 413-436 (1815).  
[96] Y. Aharonov, L. Davidovich, and N. Zagury, Phys. Rev. A 48, 1687-1690 (1993).  
[97] A. Peruzzo, M. Lobino, J. C. F. Matthews, N. Matsuda, A. Politi, K. Poulios, X. Q. Zhou, Y. Lahini, N. Ismail, K. Wörhoff, Y. Bromberg, Y. Silberberg, M. G. Thompson, and J. L. OBrien, Science 329, 1500-1503 (2010).  
[98] L. Sansoni, F. Sciarrino, G. Vallone, P. Mataloni, A. Crespi, R. Ramponi, and R. Osellame, Phys. Rev. Lett. 108, 010502 (2012).  
[99] G. Di Giuseppe, L. Martin, A. Perez-Leija, R. Keil, F. Dreisow, S. Nolte, A. Szameit, A. F. Abouraddy, D. N. Christodoulides, and B. E. A. Saleh, Phys. Rev. Lett. 110, 150503 (2013).  
[100] J. O. Owens, M. A. Broome, D. N. Biggerstaff, M. E. Goggin, A. Fedrizzi, T. Linjordet, M. Ams, G. D. Marshall,

J. Twamley, M. J. Withford, and A. G. White, New J. Phys. 13, 075003 (2011).

[101] K. Poulios, R. Keil, D. Fry, A. Meinecke Jasmin D., F. Matthews Jonathan C., A. Politi, M. Lobino, M. Grafe, M. Heinrich, S. Nolte, A. Szameit, and J. L. O'Brien, Phys. Rev. Lett. 112, 143604 (2014).

[102] P. G. Kwiat, K. Mattle, H. Weinfurter, A. Zeilinger, A. V. Sergienko, and Y. Shih, Phys. Rev. Lett. 75, 4337-4341 (1995).

[103] J. I. Cirac and P. Zoller, Phys. Rev. A 50, R2799-R2802 (1994).

[104] Y. S. Ra, M. C. Tichy, H. T. Lim, O. Kwon, F. Mintert, A. Buchleitner, and Y. H. Kim, New J. Phys. 16, 118003 (2014).

[105] P. W. Anderson, Phys. Rev. 109, 1492-1505 (1958).

[106] Y. Lahini, A. Avidan, F. Pozzi, M. Sorel, R. Morandotti, D. N. Christodoulides, and Y. Silberberg, Phys. Rev. Lett. 100, 013906 (2008).

[107] G. Di Giuseppe, L. Martin, A. Perez-Leija, R. Keil, F. Dreisow, S. Nolte, A. Szameit, A. Abouraddy, D. Christodoulides, and B. Saleh, Phys. Rev. Lett. 110, 150503 (2013).

[108] L. Martin, G. D. Giuseppe, A. Perez-Leija, R. Keil, F. Dreisow, M. Heinrich, S. Nolte, A. Szameit, A. F. Abouraddy, D. N. Christodoulides, and B. E. A. Saleh, Opt. Express 19, 13636-13646 (2011).

[109] L. Mandel, Opt. Lett. 16, 1882-1883 (1991).

[110] X. Y. Zou, L. J. Wang, and L. Mandel, Phys. Rev. Lett. 67, 318-321 (1991).

[111] Y. Bromberg, Y. Lahini, R. Morandotti, and Y. Silberberg, Phys. Rev. Lett. 102, 253904 (2009).

[112] A. Christ, A. Fedrizzi, H. Hübel, T. Jennewein, and C. Silberhorn, Parametric Down-Conversion, in: Single-Photon Generation and Detection—Physics and Applications, edited by A. Migdall, S. V. Polyakov, J. Fan, and J. C. Bienfang, (2013).

[113] A. McMillan, Y. P. Huang, B. Bell, A. Clark, P. Kumar, and J. Rarity, Four-Wave Mixing in Single-Mode Optical Fibers, in: Single-Photon Generation and Detection—Physics and Applications, edited by A. Migdall, S. V. Polyakov, J. Fan, and J. C. Bienfang, (2013).

[114] A. S. Clark, M. J. Collins, L. G. Helt, C. Xiong, K. Srinivasan, B. J. Eggleton, and M. J. Steel, Nonlinear optics for photonic quantum networks, in: All-Optical Signal Processing, edited by S. Wabnitz and B. J. Eggleton (Springer-Verlag, 2016), chap. 12.

[115] T. Meany, L. A. Ngah, M. J. Collins, A. S. Clark, R. J. Williams, B. J. Eggleton, M. J. Steel, M. J. Withford, and O. Alibart, Laser Photon. Rev. 8, L42-L46 (2014).

[116] S. M. Eaton, W. J. Chen, H. Zhang, R. Iyer, J. Li, M. Ng, S. Ho, J. Aitchison, and P. R. Herman, J. Lightwave Technol. 27, 1079-1085 (2009).

[117] T. Meany, S. Gross, N. Jovanovic, A. Arriola, M. J. Steel, and M. J. Withford, Appl. Phys. A 114, 113-118 (2013).

[118] G. D. Marshall, A. Politi, J. C. F. Matthews, P. Dekker, M. Ams, M. J. Withford, and J. L. O'Brien, Opt. Express 17, 12546-54 (2009).

[119] D. Blömer, A. Szameit, F. Dreisow, T. Schreiber, S. Nolte, and A. Tünnermann, Opt. Express 14, 2151-2157 (2006).

[120] J. B. Spring, P. Salter, P. Mennea, B. Metcalf, P. C. Humphreys, M. Moore, J. C. Gates, N. Thomsa-Peter, M. Barbieri, X. M. Jin, N. K. Langford, S. W. Kolthammer, P. G. Smith, M. Booth, B. J. Smith, and I. A. Walmsley, Quantum interference of multiple on-chip heralded sources of pure single photons, in: CLEO: Research in Optical Sciences, (OSA, Washington, D.C., 2014), p. QW1B.6.  
[121] M. Dussauze, T. Cremoux, F. Adamietz, V. Rodriguez, E. Fargin, G. Yang, and T. Cardinal, Int. J. Appl. Glass Science 3, 309-320 (2012).  
[122] G. Li, K. A. Winick, A. A. Said, M. Dugan, and P. Bado, Opt. Express 17, 9442-9453 (2009).  
[123] C. Corbari, J. D. Mills, O. Deparis, B. G. Klappauf, and P. G. Kazansky, Appl. Phys. Lett. 81, 1585 (2002).  
[124] G. Li, K. Winick, A. Said, M. Dugan, and P. Bado, Opt. Lett. 31, 739-741 (2006).  
[125] H. An, S. Fleming, B. W. McMillen, K. P. Chen, and D. Snake, Appl. Phys. Lett. 93, 061115 (2008).  
[126] H. L. An, A. Arriola, S. Gross, A. Fuerbach, M. J. Withford, and S. Fleming, Appl. Phys. Lett. 104, 021113 (2014).  
[127] B. McMillen, B. Zhang, K. P. Chen, A. Benayas, and D. Jaque, Opt. Lett. 37, 1418-1420 (2012).  
[128] M. Hughes, W. Yang, and D. Hewak, J. Opt. Soc. Am. B 26, 1370-1378 (2009).  
[129] J. E. McCarthy, H. T. Bookey, N. D. Psaila, R. R. Thomson, and A. K. Kar, Opt. Express 20, 1545-1551 (2012).  
[130] A. Ródenas, G. Martin, B. Arezki, N. Psaila, G. Jose, A. Jha, L. Labadie, P. Kern, A. Kar, and R. Thomson, Opt. Lett. 37, 392-394 (2012).  
[131] M. Li, S. Huang, Q. Wang, H. Petek, and K. P. Chen, Opt. Lett. 39, 693-696 (2014).

[132] M. Försch, J. Fürst, C. Wittmann, D. Strekalov, A. Aiello, M. V. Chekhova, C. Silberhorn, G. Leuchs, and C. Marquardt, Nat. Commun. 4, 1818 (2013).  
[133] G. D. Marshall, M. Ams, and M. J. Withford, Opt. Lett. 31, 2690-2691 (2006).  
[134] M. Ams, G. Marshall, P. Dekker, J. Piper, and M. Withford, Laser Photon. Rev. 3, 535-544 (2009).  
[135] J. Lin, S. Yu, Y. Ma, W. Fang, F. He, L. Qiao, L. Tong, Y. Cheng, and Z. Xu, Opt. Express 20, 10212 (2012).  
[136] T. Meany, M. Delanty, S. Gross, G. D. Marshall, M. J. Steel, and M. J. Withford, Opt. Express 20, 26895-26905 (2012).  
[137] N. Spagnolo, C. Vitelli, L. Aparo, P. Mataloni, F. Sciarrino, A. Crespi, R. Ramponi, and R. Osellame, Nat. Comm. 4, 1606 (2013).  
[138] N. Spagnolo, L. Aparo, C. Vitelli, A. Crespi, R. Ramponi, R. Osellame, P. Mataloni, and F. Sciarrino, Sci. Rep. 2, 862 (2012).  
[139] Z. Chaboyer, T. Meany, L. G. Helt, M. J. Withford, and M. J. Steel, Sci. Rep. 5, 9601 (2014).  
[140] R. Heilmann, J. Sperling, A. Perez-Leija, M. Gräfe, M. Heinrich, S. Nolte, W. Vogel, and A. Szameit, arXiv:1502.04932v1 (2015).  
[141] L. H. Louisell, Quantum statistical properties of radiation (John Wiley and Sons, Inc., 1973).  
[142] J. Sperling, W. Vogel, and G. S. Agarwal, Phys. Rev. Lett. 109, 093601 (2012).  
[143] J. Sperling, W. Vogel, and G. S. Agarwal, Phys. Rev. A 88, 043821 (2013).  
[144] T. J. Bartley, G. Donati, X. M. Jin, A. Datta, M. Barbieri, and I. A. Walmsley, Phys. Rev. Lett. 110, 173602 (2013).