# ORIGINAL ARTICLE

# Unscrambling light—automatically undoing strong mixing between modes

Andrea Annoni<sup>1</sup>, Emanuele Guglielmi<sup>1</sup>, Marco Carminati<sup>1</sup>, Giorgio Ferrari<sup>1</sup>, Marco Sampietro<sup>1</sup>, David AB Miller<sup>2</sup>, Andrea Melloni<sup>1</sup> and Francesco Morichetti<sup>1</sup>

Propagation of light beams through scattering or multimode systems may lead to the randomization of the spatial coherence of the light. Although information is not lost, its recovery requires a coherent interferometric reconstruction of the original signals, which have been scrambled into the modes of the scattering system. Here we show that we can automatically unscramble optical beams that have been arbitrarily mixed in a multimode waveguide, undoing the scattering and mixing between the spatial modes through a mesh of silicon photonics tuneable beam splitters. Transparent light detectors integrated in a photonic chip are used to directly monitor the evolution of each mode along the mesh, allowing sequential tuning and adaptive individual feedback control of each beam splitter. The entire mesh self-configures automatically through a progressive tuning algorithm and resets itself after significantly perturbing the mixing, without turning off the beams. We demonstrate information recovery by the simultaneous unscrambling, sorting and tracking of four mixed modes, with residual cross-talk of  $-20\mathrm{dB}$  between the beams. Circuit partitioning assisted by transparent detectors enables scalability to meshes with a higher port count and to a higher number of modes without a proportionate increase in the control complexity. The principle of self-configuring and self-resetting in optical systems should be applicable in a wide range of optical applications.

Light: Science & Applications (2017) 6, e17110; doi:10.1038/Isa.2017.110; published online 1 December 2017

Keywords: optical processing; photonic integrated circuits; silicon photonics; tuneable photonic devices

# INTRODUCTION

When a coherent light beam passes through an optical object, interference from scattering or different paths can distort the beam. Strong diffuse scatterers $^{1,2}$  and even simple multimode fibres or waveguides $^{3,4}$  can generate complex speckle patterns from simple beams, giving rise to strong scrambling of multiple beams and scrambling any information on these beams $^{5}$ . Historically, for beams of the same wavelength and polarization, an efficient approach for the separation of these beams and channels optically has not been available. This problem is worse if the characteristics of the optical object are not known, and becomes even more severe if the object changes over time.

If the object is measured interferometrically or if some global feedback algorithm is used, the input field required for a desired output field can be calculated $^{1,2,4}$ . A spatial light modulator can set up any one such input field from an input beam, but it cannot simultaneously construct multiple arbitrary overlapping input fields from multiple inputs. In few mode optical fibres or waveguides, specific modes can be separated based on their symmetries and/or different phase velocities $^{6-10}$ , and signals in well-defined modes can be interchanged or switched $^{11,12}$ . However, for arbitrary orthogonal input beams and/or for beams that couple or scatter during the propagation

due to imperfections or bends, such approaches cannot generally separate the resulting complex superpositions of output guided modes. Though information can be recovered by coherent detection together with analogue-to-digital conversion and digital electronic multiple input multiple output (MIMO) processing[13,14], these approaches require complex digital circuits with associated power, speed and capacity limits.

In waveguides where the loss is essentially the same in all the different propagating modes, in principle, the scattering between the modes can be undone with a unitary linear processor (or, in practice, a processor with uniform loss across all channels). A triangular mesh of  $2 \times 2$  tuneable beam splitters (Figure 1a) is a well-known architecture for the implementation of arbitrary unitary operations[15] (see Supplementary Note 1 for discussion of other meshes). While such meshes were successfully implemented in integrated photonics for quantum applications[16-18], progressive self-configuring algorithms[19-22] were not yet available, leading to the use of time-consuming global calibration and optimization algorithms. Self-configuration of a triangular mesh has been recently demonstrated, though that demonstration was limited to automatic coupling of one input beam and to the rerouting of a single signal through an optical switching matrix[23].

![](images/d098189a04eb0c7fe69b3eb5d6a80d048314c43198ad0a11b645fb2d9b6cbd4f.jpg)

![](images/21fc93734a3ff3181bf66e079a929f1761d10606d0d1e4894f070d11caa723b6.jpg)

![](images/bd9b7868b6d11ae0778404aa9821862f32a4b4f917ec2e5e2122ecdf50ad4459.jpg)  
Figure 1 Self-configuring mode unscrambler integrated in a silicon photonic chip. (a) Schematic concept of an  $N \times N$  ( $N = 4$ ) triangular mesh of tuneable beam splitters implementing any arbitrary transformation on  $N$ -dimensional input vectors. Transparent detectors at the output port of each beam splitter monitor the evolution of the optical field  $\mathbf{E}_{m,k}$  along the entire mesh enabling local control operation on each beam splitter individually. (b) Guided-wave implementation of the mesh through a lattice of two-port cascaded MZIs realizing the tuneable beam splitters controlled through a pair of integrated phase shifters. (c) Silicon photonic four-mode unscrambler consisting of six thermally actuated MZIs individually monitored by transparent CLIPP detectors. Mode scrambling is induced on chip through a multimode waveguide section (mode mixer). Self-configuration and stabilization of the circuit is performed through a CMOS ASIC (d) bridged to the silicon chip, which is connected to an FPGA controller.

![](images/a2cd91fa0336eb383abe89f3087c68cf8668fd570f05bc9327f937a1c77ffa3c.jpg)

Here we demonstrate that strong mixing between modes can be undone all-optically, automatically and without any advance knowledge of the mixing object's details; furthermore, our approach can adapt to changes in the mixing object in real time. We explicitly demonstrate the separation and reconstruction of four optical beams after these beams were completely and arbitrarily mixed in a multimode waveguide. We use a silicon photonic mesh architecture<sup>15</sup> with built-in transparent contactless integrated photonic probe (CLIPP) detectors<sup>24</sup> and progressive self-configuring algorithms<sup>19-22</sup> to demonstrate simultaneous unscrambling, sorting and tracking of the four beams, and information recovery from four mixed mode-division-multiplexed (MDM) channels. We also then strongly perturb the guide so that the channels are completely mixed again, and demonstrate the automatic recovery of the mode separation.

# MATERIALS AND METHODS

# Self-configuration of the mesh

An  $N \times N$  triangular array or mesh of  $N(N - 1) / 2$  tuneable  $2 \times 2$  beam splitters ( $S_{m,k}$ ) is connected according to the mesh and photodetector topology shown in Figure 1a<sup>19</sup>. This mesh enables the factorization of an arbitrary  $N \times N$  unitary transformation, described by the transmission matrix  $\mathbf{H}_{\mathrm{mesh}}$ , into a sequence of simple  $2 \times 2$  unitary

transformations $^{15,20}$ . The evolution of the optical field  $\mathbf{E}$  along the mesh is given by

$$
\mathbf {E} _ {m, k + 1} = \mathbf {T} _ {m, k} \mathbf {E} _ {m, k} = \mathbf {T} _ {m, k} \mathbf {T} _ {m, k - 1} \mathbf {E} _ {m, k - 1} = \prod_ {q = 0} ^ {k - 1} \mathbf {T} _ {m, k - q} \mathbf {E} _ {m, 1} \tag {1}
$$

and can be described by the product of  $N \times N$  transmission matrices  $\mathbf{T}_{m,k}$  associated with each beam splitter  $S_{m,k}$  where  $m = 1,2,\ldots N - 1$  is the progressive index of the mode reconstructed at the output port  $\mathrm{Out}_m$  and  $k = 1,2,\ldots N - m$  is the  $k$ -th step performed to extract the  $m$ -th mode (see also Ref. 20 for an equivalent statement of this mathematics). In this notation,  $\mathbf{E}_{m,k}$  is a four-element vector indicating the optical fields contained in the four waveguides of the mesh at the input of stage  $(m,k)$ , as indicated in Figure 1a. Here we mean a vector in the linear algebra sense, which is technically in a mathematical Hilbert space rather than in a geometrical space. Inside the mesh, a given original input 'mode' is represented by such a vector of amplitudes in all four waveguides, and, as such, it could also be referred to as a 'supermode' of the four guides. Each matrix  $\mathbf{T}_{m,k}$  is an  $N \times N$  matrix  $(4 \times 4$  in Figure 1a) constructed by starting with an identity matrix and then replacing the elements  $T_{ij}$  ( $i,j = N - k,N - k + 1$ ) with the elements of the  $2 \times 2$  matrix  $\mathbf{T}_{BS}$  of the tuneable beam splitter

$S_{m,k}$  given, for example, by

$$
\mathbf {T} _ {B S} = - j \mathrm {e} ^ {j \frac {\phi_ {2}}{2}} \left( \begin{array}{c c} - \sin \frac {\phi_ {2}}{2} & \mathrm {e} ^ {j \phi_ {1}} \cos \frac {\phi_ {2}}{2} \\ \cos \frac {\phi_ {2}}{2} & \mathrm {e} ^ {j \phi_ {1}} \sin \frac {\phi_ {2}}{2} \end{array} \right) \tag {2}
$$

where  $\phi_{1}$  and  $\phi_{2}$  are controllable phase shifts (in Equation (2), subscripts  $m,k$  are omitted for notational simplicity). Each beam splitter  $S_{m,k}$  modifies only the components  $N - k$  and  $N - k + 1$  of the field vector  $\mathbf{E}_{m,k}$ , leaving the other  $N - 2$  components unchanged. Importantly, at each stage of the mesh, a single transparent light detector (placed on either the waveguide  $N - k$  or  $N - k + 1$ ) enables us to follow the (super)mode evolution throughout the entire mesh without impairing the operation of the mesh itself.

To illustrate the self-configuration procedure, consider a first beam shining on the mesh inputs, and hence generating a vector  $\mathbf{E}_{11}$  of coherent input beam amplitudes at the input ports. To output all of this beam power at port Out<sub>1</sub>, the beam splitters  $S_{11}, S_{12}$  and  $S_{13}$  are progressively adjusted to cancel out the power at the embedded detectors<sup>19-21</sup>. Independent of the relative amplitudes and phases in the input ports, all power from the input vector  $\mathbf{E}_{11}$  is automatically combined into one output beam. Mathematically, we can consider this to be a progressive multiplication<sup>20</sup> by matrices  $\mathbf{T}_{11}, \mathbf{T}_{12}$  and  $\mathbf{T}_{13}$  that generates vectors  $\mathbf{E}_{12}, \mathbf{E}_{13}$  and  $\mathbf{E}_{14}$ , constructing an overall matrix  $\mathbf{M}_1$ , and progressively combining these amplitudes into the first element of  $\mathbf{E}_{14}$ . Since unitary operators preserve orthogonality, if we now shine a second beam with an orthogonal input vector of amplitudes into the mesh, none of that beam appears in port Out<sub>1</sub>. Hence, all of the second beam will pass through the transparent photodetectors into beamsplitters  $S_{21}$  and  $S_{22}$ , giving the vector of amplitudes  $\mathbf{E}_{21}$  in the lower three guides; those beamsplitters can then be similarly automatically aligned to couple all of the second beam to port Out<sub>2</sub>, implementing an additional matrix  $\mathbf{M}_2$ . Configuring each  $m$ -th diagonal row of the mesh, which is associated with the mode reconstruction matrix

$$
\mathbf {M} _ {m} = \prod_ {k = 0} ^ {N - m - 1} \mathbf {T} _ {m, N - m - k} \tag {3}
$$

we can separate any arbitrary set of four orthogonal input vectors to the four output ports  $\mathrm{Out}_1$ ,  $\mathrm{Out}_2$ ,  $\mathrm{Out}_3$  and  $\mathrm{Out}_4$ , formally implementing an arbitrary unitary transform[20]. Note that such training does not require any calibration of the phase shifters inside the mesh, and can be completed automatically and progressively in one algorithmic pass through the set of beamsplitters.

Here we described turning on the training beams one by one, with the second beam specifically not turned on until the row of beamsplitters  $S_{11}$ ,  $S_{12}$  and  $S_{13}$  is fully configured; similar procedures were conducted for further beams and beamsplitter rows. Indeed, such a separated training may always be required when working with simple continuous beams and for related progressive algorithms that can run based on detectors only at the output ports[19,22]. If, however, the beams of interest are not mutually coherent, and if we can put an identifying 'key' on each such training beam, such as a small modulation at a different frequency or 'tone' for each beam, then the entire configuration process can be run simultaneously with all beams on at once[19].

# Design and technology of the silicon photonic mode unscrambler

To demonstrate on-chip mode unscrambling, a silicon-photonic  $4\times 4$  triangular array of six Mach-Zehnder Interferometers (MZIs) was fabricated on a 220-nm silicon-on-insulator platform through a LETI-ePIXfab multi-project-wafer run (Figure 1b and 1c) $^{25}$ . Tuneable beam

splitters are realized using thermally actuated balanced MZIs, with  $40-\mu \mathrm{m}$  long directional couplers (300 nm waveguide spacing in the coupling region) and  $120-\mu \mathrm{m}$  long arms spaced by  $20\mu \mathrm{m}$ . Titanium nitride integrated heaters, with width and length of 1 and  $100\mu \mathrm{m}$ , respectively, are used to control the phase shifts  $\phi_{1}$  and  $\phi_{2}$  of the MZIs, providing  $\pi$ -phase-shift with an electrical power consumption of  $\sim 10\mathrm{mW}$  and a response time of less than  $10~\mu \mathrm{s}$ .

The optical power is locally monitored on chip by transparent CLIPP detectors integrated at the lower output port of each MZI (see Supplementary Note 2 and Supplementary Fig. S1). In the CLIPP detector $^{24}$ , surface-state absorption $^{26-28}$  in the silicon waveguide gives photoconduction that can be detected capacitively, giving a subbandgap all-silicon photodetector for high-sensitivity measurement of light power in the waveguide without introducing any appreciable loss, reflection or phase perturbation in the optical field. The CLIPPs detectors consist of two  $20\mu \mathrm{m} \times 50\mu \mathrm{m}$  electrodes that are mutually spaced by  $100\mu \mathrm{m}$  and are fabricated using the same metal layer as that used for the heaters and that is placed above the optical waveguides at the distance of  $\sim 600\mathrm{nm}$  from the Si core. At a wavelength of  $1550\mathrm{nm}$ , the expected metal loss is on the order of  $0.1\mathrm{dBcm}^{-1}$ ; this is more than one order of magnitude below the waveguide propagation loss  $(1.7\mathrm{dBcm}^{-1})$  and results in a negligible loss of  $0.001\mathrm{dB}$  expected for the CLIPP $^{24}$ . The absence of any relevant absorption implies that the CLIPP monitors the power without introducing any differential absorption in the mesh paths, thus preserving the (super) mode orthogonality. Gold metal strips connect the thermal actuators and the CLIPPs to the  $100\mu \mathrm{m} \times 100\mu \mathrm{m}$  contact pads, where wire-bonding of the photonic chip to the external electronic circuit is performed. Experimentally, we were not able to observe any significant difference between the loss of a waveguide integrating up to 10 CLIPPs with respect to a reference waveguide (with no CLIPPs) with the same length.

Four spatially decoupled input beams (modes A, B, C and D) are injected into the silicon chip through an array of four single mode fibres, which are vertically coupled to the silicon waveguides through a commercial four-channel glass transposer (Figure 1d). The four modes are coupled to the photonic chip through two arrays of input and output grating couplers that are mutually spaced by  $127\mu \mathrm{m}$ . Mode scrambling is intentionally induced on chip with an integrated mode mixer consisting of a straight multimode waveguide section with four single mode input/output waveguides. The design of the mode mixer was optimized to reduce the loss (see Supplementary Note 3) because loss would impair the orthogonality of the modes, thus affecting the mode reconstruction performed by the MZI mesh. The multimode waveguide is  $180 - \mu \mathrm{m}$  long and  $10 - \mu \mathrm{m}$  wide, and the single-mode input/output waveguides are linearly tapered up to a width of  $2\mu \mathrm{m}$ .

This mode mixer can be represented by a matrix  $\mathbf{H}$  that maps any vector of each input in modes A, B, C or D in Figure 2a to a resulting vector of field amplitudes at the single-mode waveguide outputs that form the inputs to the mesh. To verify the strong mixing generated by the multimode waveguide, we separately checked an identical standalone mode mixer (fabricated onto the same chip), showing that at a wavelength of  $1525\mathrm{nm}$ , each input mode is scrambled at the output ports with  $\sim 25\%$  power distribution (Supplementary Fig. S2) and with an excess insertion loss lower than  $0.7\mathrm{dB}$ . The integrated mixer provides almost constant mode power coupling across a wavelength range of several tens of nanometres, with negligible differential group delay among the different modes. This situation emulates the mode scrambling that may occur in short links of a few-mode fibre[29] (see 'Results and discussion: On-chip MDM channel unscrambling' section).

![](images/e5c80deb515e290fce96bd46446269d773c287987c6ff2de76b58a209e64f760.jpg)

![](images/78025a3a05c94c034b256912b5e7eff364008966637d53b1a0e50b34aa75f15d.jpg)  
Figure 2 On-chip unscrambling of optical modes. (a) Mixed modes are reconstructed at the output port of the  $4 \times 4$  silicon photonic mesh by sequentially tuning the MZI beam splitters. To reconstruct the first mode ( $m = 1$ , Mode D) at port Out $_1$ , the first row of the mesh ( $\mathbf{M}_1$ ) is configured by progressively nulling the light intensity at the lower output arms of MZI  $S_{11}$ ,  $S_{12}$  and  $S_{13}$ , where a CLIPP detector is integrated (b). (c) Normalized power of Mode D measured by CLIPP1 integrated after  $S_{11}$ . Depending on the initial MZI biasing ( $S_{11}^{\prime}$ ), convergence to different equivalent solutions  $S_{11}^{\prime}$  (local minima of the map) may be achieved.

![](images/e9170c9885ccb7733239407212014020f05e83da206c1a5d91f19869a0e792f1.jpg)

The on-chip attenuation of the MZI mesh (excluding the mode mixer) is less than  $1\mathrm{dB}$ , with  $\sim 0.5\mathrm{dB}$  arising from the silicon waveguide propagation loss and the remaining  $0.5\mathrm{dB}$  due to the excess insertion loss of the directional couplers used in the tuneable beam splitters. To avoid on-chip differential losses as well as to balance all interferometric paths of the mesh, folded waveguide sections are added between the different stages of the mesh. All bends throughout the circuits have a curvature radius of  $20\mu \mathrm{m}$ , allowing very low reflections and negligible bending losses. The circuit footprint, including metal routing and contact pads, is  $3.7\mathrm{mm} \times 1.4\mathrm{mm}$ .

# Electronic platform for tuning and locking

For simultaneous read-out of all the CLIPPs integrated in the photonic circuit, a custom-designed multi-channel CMOS ASIC realized in a  $0.35\text{-}\mu \mathrm{m}$  AMS CMOS process was bridged to the silicon photonic chip and mounted on the same printed circuit board (Figure 1d) $^{30,31}$ . The ASIC contains a low-noise front-end amplifier followed by a fully integrated lock-in system for the extraction of the in-phase and quadrature components of the light-dependent waveguide impedance $^{24}$ . The ASIC has four parallel read-out channels, with each channel featuring an  $8\times$  input multiplexer to address up to a total of 32 CLIPPs.

When the input modes A, B, C and D are simultaneously coupled into the chip, the CLIPP detectors can identify the power associated with each mode regardless of the presence of other concurrent modes injected at other input ports and scrambled by the mode mixer. To enable mode discrimination, each mode is labelled with a weak 'key' or pilot tone before being coupled to the silicon chip. In previous studies, we have demonstrated that such a labelling operation can be performed without affecting the quality of the signals $^{32,33}$ .

Sinusoidal tones with  $5\%$  peak-to-peak relative intensity are generated through external MZI lithium niobate modulators biased at the linear working point (3 dB attenuation). The tone frequency  $f_{\mathrm{q}} = \{4\mathrm{kHz},7\mathrm{kHz},10\mathrm{kHz},11\mathrm{kHz}\}$  of the  $q$ -th mode ( $q = \mathrm{A}$ ,  $\mathrm{B}$ ,  $\mathrm{C}$ ,  $\mathrm{D}$ )

was suitably chosen to avoid mutual overlap of the overtones that can be generated by the non-perfectly linear response of the modulators. Different tone waves (for example, square waves) as well as different biasing points of the modulator could also be used to reduce the loss associated with tone generation, but such tones would require a more careful selection of the tone frequencies in order to avoid mutual overlaps. To identify the  $q$ -th mode, the CLIPPs are demodulated twice, first at the read-out frequency  $f_{\mathrm{e}}$  around which the CLIPP sensitivity to optical power variations is maximized ( $\sim 100\mathrm{kHz}$  in the reported experiments, see Supplementary Note 1), and then at the frequency  $f_{q}$  of the mode to be monitored (see Supplementary Note 4 and Supplementary Fig. S3). Second demodulation at a frequency different from  $f_{q}$  produces a very low crosstalk signal (lower than  $-50\mathrm{dB}$ ), which is mainly due to the noise level of the electronic front-end[31,33].

The four output signals from the ASIC are acquired and conditioned by a customized field programmable gate array (FPGA)-based electronic platform and are digitally demodulated at the frequencies  $f_{q}$  and processed by tuneable infinite impulse response filters (down to  $4\mathrm{Hz}$  bandwidth) to identify the power level of each mode. The FPGA drives the 12 heaters of the silicon photonic chip to tune and lock the 6 MZIs to the desired working points. In the experiments, the system was set to perform the CLIPP read-out in  $50~\mathrm{ms}$ , allowing an automatic 2D scan of each MZI  $(30\times 30$  pixel map, as in Figure 2c) in  $\sim 45$  s and automated full reconfiguration of the mesh (starting from unbiased MZIs) in  $\sim 15$  s. Once the mesh is configured, tracking of time-varying mixed modes can be performed on a time scale of a few hundred milliseconds. By following the design rules and electronic read-out optimization strategies provided in other specific contributions[31,34], the CLIPP read-out time can be reduced by two orders of magnitude, while maintaining a sensitivity better than  $-20\mathrm{dBm}$ , thus enabling the tracking of mode mixing variations occurring within a millisecond range.

# Experimental set-up for on-chip unscrambling of MDM channels

A detailed schematic of the experimental set-up employed for the demonstration of on-chip unscrambling of MDM channels is shown in Figure 3. The four channels encoded on modes  $\{\mathrm{A},\mathrm{B},\mathrm{C},\mathrm{D}\}$  are generated by using a common laser source with an emission wavelength of  $1525\mathrm{nm}$  that is intensity modulated at a data rate of  $10\mathrm{Gbit}s^{-1}$ , according to a  $2^{31}-1$  on-off keying pseudo random bit sequence (PRBS) using a commercial  $\mathrm{LiNbO_3}$  Mach-Zehnder modulator. After amplification through an erbium-doped fibre amplifier (EDFA), the modulated signal is divided by a  $1\times 4$  fibre optic splitter. The four data streams are de-correlated using coils of standard single-mode fibres of different lengths, introducing relative delays ( $>10~\mu s$ ) that are much greater than the signal coherence length. Variable optical attenuators (VOAs) are employed to equalize the channel optical power to  $0\mathrm{dBm}$  at the input of the silicon photonic circuit. Polarization controllers (PCs) enable the selection of the transverse electric (TE) polarization at the output of the glass transposer (see Figure 1d) in order to optimize the coupling efficiency of each channel with the optical waveguides. At the output ports of the circuit, the transmitted signals are amplified by an EDFA followed by a filter ( $0.3\mathrm{nm}$  bandwidth) that is added to reduce the off-band amplified spontaneous emission noise. A VOA is used to control the received power at the input of the photodetector in order to perform the BER and eye diagram measurements.

# Light-induced perturbation of the mode mixer

To modify the scrambling process responsible for the mode mixing, the integrated mode mixer was exposed to an intense light beam generated by a fibre-coupled laser source, emitting light at  $980\mathrm{nm}$  with a maximum power  $P = 20$  dBm. A lensed fibre with a spot area  $A$  of  $\sim 3\mu \mathrm{m}^2$  at the focal distance is used to irradiate the mode mixer from the top with an intensity of  $\sim 3.3\mathrm{MWcm}^{-2}$ . Because the spot size  $A$  is much smaller than the mode-mixer size (see Supplementary Note 2), only a small portion of the device is directly exposed to the light beam. To estimate the density of free carriers  $N$  generated in the device, we assume uniform absorption of the light across the core layer. Neglecting the reflection at the air/silica/silicon interfaces, the carrier density is governed by the following rate Equation

$$
\frac {\mathrm {d} N}{\mathrm {d} t} = \frac {\alpha P}{A h v} - \frac {N}{\tau} \tag {4}
$$

where  $\alpha$  is the silicon absorption coefficient at  $980\mathrm{nm}$  ( $\alpha \sim 100\mathrm{cm}^{-1}$ ) and  $h\nu$  is the photon energy (1.26 eV). In silicon waveguides, the free carrier lifetime  $\tau$  typically ranges from a fraction of a nanosecond to

several tens of nanoseconds $^{35}$ . Assuming  $\tau = 1$  ns, the steady-state carrier density  $N = \alpha P\tau / Ah\nu$  is estimated to be on the order of  $2 \times 10^{18} \mathrm{~cm}^{-3}$ .

# RESULTS AND DISCUSSION

# Sorting out mixed modes

To illustrate the reconstruction of modes scrambled by propagation through the mode mixer, in the example of Figure 2a, the first row of the mesh  $(\mathbf{M}_1)$  is progressively configured to have the optical mode D reconstructed at Out<sub>1</sub>. In this experiment, all four input modes, which share the same optical wavelength  $\lambda_0 = 1525\mathrm{nm}$ , are switched on, keyed by modulation tones (see Supplementary Note 4 and Supplementary Fig. S3) and injected into the silicon chip with the same power of 0 dBm.

First, MZI  $S_{11}$  (see Figure 2b) is tuned to cancel out the power associated with mode D at the lower output port where CLIPP1 is integrated. The map presented in Figure 2c shows the intensity of mode D versus the phases  $(\phi_1, \phi_2)$  (see Figure 2b) of  $S_{11}$  as measured directly by CLIPP1. The thermal phase shifters are initially set to a non-zero value, such as  $S_{11}^{\mathrm{i}}(\pi, \pi)$ , in order to be able to either increase or decrease the phase shift during the tuning operation. Once convergence to a local minimum  $S_{11}^{\mathrm{f}}$  is achieved, the procedure is sequentially repeated through the subsequent stages  $S_{12}$  and  $S_{13}$ . After the tuning of each beam splitter in the first row of the mesh  $(\mathbf{M}_1)$ , the powers of the sorted mode D and of the concurrent modes A, B and C were measured at port Out  $_1$  over a wavelength range of  $20\mathrm{nm}$  around  $\lambda_0$ . As shown in Figure 4, although this mesh configuration process leads to a progressive increase in the output power of the reconstructed mode at Out  $_1$  (Figure 4a  $_4$ ), the crosstalk associated with each concurrent mode does not decrease monotonically as this configuration progresses (Figure 4a  $_1 - 4a_3$ ). For instance, the transmitted power of mode C (Figure 4a  $_3$ ) reaches a minimum after the tuning of  $S_{11}$  and  $S_{12}$ , yet the minimization of the overall crosstalk from all the concurrent modes results in an increased transmission of mode C after the tuning of the last stage  $S_{13}$ . This indicates that in practice, the mesh configuration cannot necessarily be reliably achieved using only the information provided by external detectors coupled at the output ports, because convergence issues due to local minima can arise, at least if the mesh is not quite perfect. Thus, although an algorithm based only on the overall output powers may work (see the progressive algorithms using only output detectors in Ref. 19 Appendix B and in Ref. 22 and the global algorithms in Ref. 14), approaches with embedded detectors may offer faster and more robust convergence,

![](images/9dc733543651eadf9c99ee98d52fb16356c88eca41d073d57f9ae0721e45f03c.jpg)  
Figure 3 Experimental setup used for the demonstration of all-optical unscrambling of mixed MDM channels.

![](images/2bbe8a179c6359b80109fe3b340e90ddad642aa83da47ae7b2fc7f46947265b2.jpg)  
a

![](images/24d3d12c5dde8c13ac6a5bf488951280255448ec63299678c8aec0d9f92b950d.jpg)

![](images/830fa170328a824cae218706080be576dc1f7afcf7702f721db776c0d07c74ea.jpg)

![](images/0632b8daf033707cf58f5cbdf289641bb3c62d8c7468b33b3126137584b567d1.jpg)

![](images/91d4c05ca7850d0056f0b3dbc8621aefd59be621713ae95741e3cc626c620b59.jpg)  
b  
Figure 4 (a) Mesh configuration makes the transmission of the mode reconstructed at port  $\mathrm{Out}_1$  progressively increase  $a_4$ , while the crosstalk due to the concurrent modes A  $a_1$ , B  $a_2$  and C  $a_3$  reduces. (b) Reconstruction of mode A  $b_1$ , mode B  $b_2$ , mode C  $b_3$ , and mode D  $b_4$  at port  $\mathrm{Out}_1$  can be achieved with less than  $-20$  dB residual crosstalk of the three concurrent modes over a bandwidth of  $\sim 10$  nm.

![](images/045a9b7f89ae0c5879e20a5968c1d16cd32824db6b9732bbbf7424e26c9ec738.jpg)

![](images/139cbbc032f59b4d10e952dd6debe63de1077e9cae6ca97f02cf50be945aef62.jpg)

![](images/74102a925ee2523fee70401117fd47e664328016fe2724630dbb7598871624e4.jpg)

in addition to the ability to configure the mesh when all input modes are present simultaneously.

Any input mode can be reconstructed at any output port with similar performance. For instance, Figure 4b shows that by properly setting  $\mathbf{M}_1$ , mode reconstruction at port  $\mathrm{Out}_1$  for any particular chosen input is achieved with less than  $-20\mathrm{dB}$  residual crosstalk of the concurrent modes over a wavelength range of  $\sim 10\mathrm{nm}$ . More generally, the mesh transmission matrix

$$
\mathbf {H} _ {\text {m e s h}} = \prod_ {m = 1} ^ {N - 1} \mathbf {M} _ {N - m} \tag {5}
$$

can be configured to give any desired permutation of inputs to outputs, as in a switching matrix. In other words, the overall matrix of the system  $|\mathbf{H}_{\mathrm{mesh}}\mathbf{H}|^2$  that describes the power transmission of the input modes {A, B, C, D} to the output ports of the mesh, can be chosen to take the form of a generic permutation matrix. This means that not only can the mesh perform an inversion of the H matrix, but the reconstructed modes can also be sorted or switched arbitrarily at the output ports. Figure 5 shows the measured light power at the output ports {Out<sub>1</sub> Out<sub>2</sub>, Out<sub>3</sub>, Out<sub>4</sub>} for several configurations of the full mesh. In all considered cases, the power of the concurrent channels is more than 20 dB below the power of the reconstructed mode (crosstalk data are reported in Supplementary Fig. S4).

Incidentally, we note that this performance is achieved even though the intensity split ratio of the directional couplers of the MZIs is quite far from the ideal 50:50 condition (we estimate  $\sim 72\%$  coupling in the fabricated device at  $1525\mathrm{nm}$  wavelength). Numerical simulations show that an optical crosstalk lower than  $-25\mathrm{dB}$  is maintained up to a split ratio of  $\sim 0.75$ , thus implying that no significant performance degradation occurs for relative deviations as large as  $50\%$  from the ideal condition (see Supplementary Note 5 and Supplementary Fig. S5). Recent approaches may allow yet further performance

optimization even with such imperfect directional couplers $^{22,36}$  and/or with broadband couplers $^{37}$ .

# On-chip MDM channel unscrambling

To demonstrate the recovery of the information encoded in the optical modes undergoing the mixing process, we injected four data channels (see Figure 6a) that were all at a wavelength of  $1525\mathrm{nm}$ , on separate fibres to form the inputs A, B, C and D. When the mesh is not configured, mode mixing results in deep time variations in the spectrum of the optical signal measured at the device output  $(\mathrm{Out}_1$  in Figure 6b) due to the coherent beating of the four spectrally overlapped channels. In contrast, the spectrum of the reconstructed channel exhibits only a tiny frequency-domain ripple due to the residual  $-20\mathrm{dB}$  crosstalk of the three concurrent channels. The mode mixing leads to the complete closure of the signal eye diagram (insets of Figure 6b), which is effectively restored after mode unscrambling. The panels in Figure 6c show the eye diagrams of each reconstructed channel at port  $\mathrm{Out}_1$  and do not show any deterioration as more concurrent channels are switched on. Bit error rate (BER) measurements (Figure 6d) show a power penalty  $< 2\mathrm{dB}$  at a BER of  $10^{-9}$  as additional channels are turned on.

The MZI mesh can also self-configure automatically to track modes that are mixed by a time-varying scrambling process. The integrated mode mixer was deliberately perturbed by shining a 980-nm-wavelength light beam with an intensity of  $3.3\mathrm{MWcm}^{-2}$  on it (see Figure 7a). Absorption of this light in the silicon of the mode mixer generates free carriers with a density of  $\sim 10^{18}\mathrm{cm}^{-3}$ , and leads to local changes in the refractive index, arising both from free carrier dispersion (blueshift) and thermal (redshift) effects[35]. These changes affect the self-imaging process along the multimode silicon waveguide[38] and modify the mode mixer behaviour (Figure 7b). When the 980-nm beam was off (Figure 7b $_1$ ), the mesh was configured to a reference state where a given channel (A) is reconstructed at one output port  $(\mathrm{Out}_1)$ . With the 980-nm beam

![](images/046b495e8a1d0aa67d287b3924170c2e024c3117cd2b2b12c9038137fe0ac7f8.jpg)

![](images/7dbf9bab2c437bbab88a671371f18234a590ad56dae9808c116a85a3f9991622.jpg)

![](images/8821fddf062f4c1a48f454ce360e70832f21158304dad39a51d30ccf3e124ef0.jpg)

![](images/7bbe8f2277008d1e7b8bb64e1bf9a030cf058e5ad5e4f6b2c54c91c490a04949.jpg)  
Figure 5 On-chip mode sorting. The mesh transmission matrix  $\mathsf{H}_{\mathrm{mesh}}$  can be configured in order to sort the reconstructed modes  $\{\mathsf{A},\mathsf{B},\mathsf{C},\mathsf{D}\}$  arbitrarily at the output ports  $\{\mathrm{Out}_1,\mathrm{Out}_2,\mathrm{Out}_3,\mathrm{Out}_4\}$  of the mesh according to any  $4\times 4$  permutation power transmission matrix  $\mathsf{I}\mathsf{H}_{\mathrm{mesh}}\mathsf{H}^2$ . Given the mode scrambling introduced by the mode mixer  $\mathsf{H}$ , spreading the power of the input modes almost equally in the input waveguides of the mesh (a), panels (b-f) show the normalized light power at the output ports of the mesh, when it is configured to extract the modes in the follow order: (b) A, B, C, D; (c) D, C, B, A; (d) D, C, B, A; (e) C, A, D, B; (f) C, B, A, D.

![](images/1d47e652a09d21e5f9675fdb66208ceddc7ab52401ff4da359e69e4f2ff91f34.jpg)

![](images/ce498bd9c49b116bc9543cf6337546861fb0a258300ab810d9920638af54b616.jpg)

on, the mode mixer (Figure  $7\mathrm{b}_2$ ) is sufficiently perturbed to completely impair mode reconstruction if the mesh is not adaptively configured. Figure  $7\mathrm{b}_3$  shows that the eye diagram of the output channel is successfully recovered after the automatic reconfiguration of the mesh. Notably, this mode reconstruction is performed without any knowledge of the perturbation introduced in the mode mixer.

Transparency to the modulation format is one of the main advantages of performing MDM unscrambling directly in the optical domain. Therefore, we do not expect any significant performance degradation if more advanced modulation formats are employed where both the amplitude and the phase of the signals are modulated. Regarding the optical bandwidth, the realized device provides less than  $-20\mathrm{dB}$  residual crosstalk over a bandwidth of  $\sim 10\mathrm{nm}$ , thus posing no significant limitations to the bandwidth of the optical signals that can be manipulated. The tuning strategy itself, which is based on channel labelling with low frequency pilot tones, is inherently independent of the bandwidth and modulation format of the mixed channels, which could indeed have different bandwidths and modulation formats.

Arbitrarily mixed modes can be unscrambled by the proposed mesh, provided that no significant differential mode group delay

(DMGD) is accumulated in the mixing channel. This means that the mesh can operate on channels coupled into near degenerate modes (or mode groups) of a multimode fibre propagating with the same group velocity. Because the mesh cannot compensate for an accumulated DMGD, information can be effectively recovered only when the DMGD is a small fraction of the bit time duration ( $< 5\%$ ). This situation reflects for instance the case of intradatacentre optical connections, where the length of optical links typically ranges from few tens of metres to a maximum length of  $1 - 2\mathrm{km}^{39}$ . Low values of DMGD have been demonstrated in coupled-core fibres  $(3.14\mathrm{ps}\mathrm{km}^{-1})^{40}$  and in cascaded FMFs ( $< 1.7\mathrm{ps}\mathrm{km}^{-1})^{41}$ , enabling almost DMGD-free propagation across more than  $2\mathrm{km}$  at  $10\mathrm{Gsym}\mathrm{s}^{-1}$ , or  $500\mathrm{m}$  at  $40\mathrm{Gsym}\mathrm{s}^{-1}$ .

# CONCLUSION

We have demonstrated all-optical mode reconstruction, unscrambling and sorting in a silicon photonic circuit using a self-reconfiguring interferometric mesh. Because each mesh element (tuneable beam splitter) is locally monitored and feedback-controlled by transparent detectors, the progressive self-configuration of the mesh is reduced to a repeated two-degrees-of-freedom problem independently of the

![](images/355a3b8f60cc418f8ef9bc0722c29bd114e7e3b54f60af12e18a38caf89f9bdb.jpg)

![](images/d10ff6d7cd7cd377dbbbf19bc90094ab9c08a0184f09bddfa135ef2ab204ab1f.jpg)

![](images/72b3a4e8556790fe51c3b008f23ed30165bcbf3cf94a3bee01701e853ceefe09.jpg)

![](images/6704216bcefd62009a9ff4f9a6f1d5914f4ea1a3329eba966f901b2940f2aa40.jpg)  
Figure 6 On-chip unscrambling of MDM optical channels. (a) Information encoded in four scrambled  $10\mathrm{Gbit}s^{-1}$  intensity modulated MDM channels is recovered after mode reconstruction performed by the silicon photonic mesh. (b) As a consequence of mode mixing, the spectrum of the four mixed channels (black curves) exhibits deep time-varying oscillations, which disappear after mode reconstruction (mode A, blue curves). Displayed curves refer to 10 successive measurements taken at output port  $\mathrm{Out}_1$ . The corresponding time domain signals are shown in the eye diagrams in the insets. Eye diagram (c) and BER (d) measurements (port  $\mathrm{Out}_1$ ) demonstrate that information encoded in each channel can be retrieved with a very small power penalty independent of the number of mixed modes.

![](images/1a60ef79a4f84735101f039a5206df81435816708656504f8ce6fe97bd6dffe5.jpg)

![](images/9c3fa8bfc50c05b4c682cb92333d4d34a196118bfac66571b393c05994fc4a0e.jpg)  
Figure 7 Reconstruction of modes scrambled by time-varying mixing. (a) A light source  $(980\mathrm{nm})$  is used to perturb the mode mixer integrated in the silicon chip in order to modify the relative amplitude and phase of the mixed modes. (b) After configuring the mesh to reconstruct channel A at port Out1 (reference state,  $\mathbf{b}_1$ ), the 980-nm source is switched on to modify the mode mixing, thus impairing mode reconstruction at the mesh output (perturbed state,  $\mathbf{b}_2$ ). In the track mode  $\mathbf{b}_3$ , the mesh adaptively self-configures by controlling each MZI through a local feedback loop, in order to automatically compensate against time-varying mixing of the modes.

![](images/8073c62d07a9e8dbf76947a548b85428933ae19318fe19e91d9bf0c54d7e67bc.jpg)  
980 nm ON

![](images/70f3f181e3598f7070bf8b3fcf698d377b9b94881839fc1d3b69759ea9520a95.jpg)

port-count of the mesh. This feature enables the implementation of simple, accurate and robust control of arbitrarily large meshes for the manipulation of a large number of modes $^{20}$ .

For implementation on existing silicon photonic platforms, the practical limit to the mesh scalability is neither the physical size of the mesh, nor the complexity of the tuning and locking algorithm, because meshes with more than one thousands tuneable splitters and handling several tens of modes could be realized and controlled. Power consumption of thermal actuators and propagation loss of the silicon waveguide is the main barrier to scalability to a very large number of modes (see the Supplementary Information for a quantitative analysis). This overall concept of transparent on-chip monitoring and adaptive feedback control of elementary photonic elements can be extended to arbitrary mesh topologies, such as the topologies that have been recently proposed to implement programmable photonic processors $^{18,42-45}$ .

Mode unscrambling on a photonic chip can also be exploited to improve the performance of recently proposed silicon photonics devices for the manipulation of MDM optical channels $^{6-11}$ , where a one-by-one mapping of the modes of single-mode waveguides to predetermined modes of multimode waveguides is performed. In these examples, no mode coupling in the multimode waveguide is considered, but in reality, mode mixing could be induced by sharp bending, waveguide crossing, as well as fabrication imperfections. Mode unscramblers, such as the one proposed in this work, are thus required to mitigate these effects, which are difficult to predict at design time, and which potentially also vary in time in uncooled photonic chips because of the different temperature sensitivities of the different guided modes.

While our demonstration architecture is capable of implementing any unitary (that is, loss-less) linear function between inputs and outputs, architectural extensions allow this approach to implement non-unitary linear operations also. In applications where mode mixing must be tracked with a control system that neither reaches the end of

its range (endless) nor needs to reset (resetless) to avoid communication interruptions, endless phase shifters $^{46}$  could be integrated in the tuneable beam splitters of the mesh, though necessarily at the cost of an increasing complexity of the photonic circuit. Likewise, more complex meshes would be required to unscramble optical modes that have experienced mode-dependent loss and large DMGD. For instance, it has been shown that two unitary processors as described here can be used to undo the scattering between the modes even when the losses in the modes differ substantially from each other $^{45}$ .

The approach presented here can also be extended to other semiconductor photonics platforms, such as InP, where modes are not easily separable because of the similarity of their phase velocities $^{12}$  and where the CLIPP operation has also been successfully demonstrated $^{47}$ . We expect that this approach will find use in mode (de)multiplexers $^{6-8}$ , multimode switches $^{9}$  mode converters $^{10}$ , switchable mode exchangers $^{11}$  and other programmable photonic processors $^{18,42-44}$  for applications in a variety of different fields, such as telecommunications, imaging, sensing, secrecy, and quantum information processing $^{5}$ .

# CONFLICT OF INTEREST

The authors declare no conflict of interest.

# AUTHOR CONTRIBUTIONS

FM conceived the experiments and supervised the work. AA designed the photonic chip and performed the experiments. EG developed the firmware and performed the experiments; MC designed and tested the electronic platform; GF designed the CMOS ASIC; MS supervised the implementation of the electronic platform; AA, FM and AM analysed the data; FM, AM and DM wrote the manuscript.

# ACKNOWLEDGEMENTS

The research leading to these results received funding from the European Union's Seventh FP7 Programme (Grant agreement No. 323734, BBOI), from the European Union's H2020 Programme (Grant No. 688172, STREAMS), from Fondazione Cariplo (Grant No. 2016-0881, ACTIO) and by Multidisciplinary University Research Initiative grant (Air Force Office of Scientific Research, FA9550-12-1-0024). This work was (partially) performed at Polifab, the micro- and nanofabrication facility of Politecnico di Milano (www.polifab.polimi.it). The authors acknowledge F Zanetto for assistance with measurements.

1 Vellekoop IM, Mosk AP. Focusing coherent light through opaque strongly scattering media. Opt Lett 2007; 32: 2309-2311.  
2 Mosk AP, Lagendijk A, Lerosey G, Fink M. Controlling waves in space and time for imaging and focusing in complex media. Nat Photonics 2012; 6: 283-292.  
3 Ryf R, Fontaine NK. Space-division multiplexing and MIMO processing. In: Zhou X, Xie CJ editors. Enabling Technologies for High Spectral-Efficiency Coherent Optical Communication Networks. John Wiley & Sons, Inc. 2016; pp 547-608.  
4 Ploschner M, Tyc T, Cizmár T. Seeing through chaos in multimode fibres. Nat Photonics 2015; 9: 529-535.  
5 Miller DAB. Sorting out light. Science 2015; 347: 1423-1424.  
6 Luo LW, Ophir N, Chen CP, Gabrielli LH, Poitras CB et al. WDM-compatible mode-division multiplexing on a silicon chip. Nat Commun 2014; 5: 3069.  
7 Driscoll JB, Chen CP, Grote RR, Souhan B, Dadap JI et al. A 60 Gb s $^{-1}$  MDM-WDM Si photonic link with  $<0.7$  dB power penalty per channel. Opt Express 2014; 22: 18543-18555.  
8 Dai DX, Wang J, Chen ST, Wang SP, He SL. Monolithically integrated 64-channel silicon hybrid demultiplexer enabling simultaneous wavelength- and mode-division-multiplexing. Laser Photonics Rev 2015; 9: 339-344.  
9 Stern B, Zhu XL, Chen CP, Tzuang LD, Cardenas J et al. On-chip mode-division multiplexing switch. Optica 2015; 2: 530-535.  
10 Heinrich M, Miri MA, Stützer S, El-Ganainy R, Nolte S et al. Supersymmetric mode converters. Nat Commun 2014; 5: 3698.  
11 Sun CL, Yu Y, Chen GY, Zhang XL. Integrated switchable mode exchange for reconfigurable mode-multiplexing optical networks. Opt Lett 2016; 41: 3257-3260.

12 Melati D, Alippi A, Melloni A. Reconfigurable photonic integrated mode (de)multiplexer for SDM fiber transmission. Opt Express 2016; 24: 12625-12634.  
13 Ryf R, Randel S, Gnauck AH, Bolle C, Sierra A et al. Mode-division multiplexing over 96 km of few-mode fiber using coherent  $6 \times 6$  MIMO processing. J Lightwave Technol 2012; 30: 521-531.  
14 Arik SÖ, Kahn JM. Direct-detection mode-division multiplexing in modal basis using phase retrieval. Opt Let 2016; 41: 4265-4268.  
15 Reck M, Zeilinger A, Bernstein HJ, Bertani P. Experimental realization of any discrete unitary operator. Phys Rev Lett 1994; 73: 58-61.  
16 Carolan J, Harrold C, Sparrow C, Martin-Lopez E, Russell NJ et al. Universal linear optics. Science 2015; 349: 711-716.  
17 Crespi A, Osellame R, Ramponi R, Brod DJ, Galvão EF et al. Integrated multimode interferometers with arbitrary designs for photonic boson sampling. Nat Photonics 2013; 7:545-549.  
18 Harris NC, Steinbrecher GR, Prabhu M, Lahini Y, Mower J, et al. Quantum transport simulations in a programmable nanophotonic processor. Nat Photonics 2017; 11: 447-452.  
19 Miller DAB. Self-aligning universal beam coupler. Opt Express 2013; 21: 6360-6370.  
20 Miller DAB. Self-configuring universal linear optical component. Photonics Res 2013; 1: 1-15.  
21 Miller DAB. Reconfigurable add-drop multiplexer for spatial modes. Opt Express 2013; 21: 20220-20229.  
22 Miller DAB. Perfect optics with imperfect components. Optica 2015; 2: 747-750.  
23 Ribeiro A, Ruocco A, Vanacker L, Bogaerts W. Demonstration of a  $4 \times 4$ -port universal linear circuit. Optica 2016; 3: 1348-1357.  
24 Morichetti F, Grillanda S, Carminati M, Ferrari G, Sampietro M et al. Non-invasive on-chip light observation by contactless waveguide conductivity monitoring. IEEE J Sel Top Quantum Electron 2014; 20: 292-301.  
25 Morichetti F, Annoni A, Grillanda S, Peserico N, Carminati M et al. 4-Channel All-Optical MIMO Demultiplexing on a Silicon Chip. Proceedings of Optical Fiber Communication Conference; 20-22 March 2016; Anaheim, California United States. Optical Society of America: Anaheim, California, USA 2016.  
26 Baehr-Jones T, Hochberg M, Scherer A. Photodetection in silicon beyond the band edge with surface states. Opt Express 2008; 16: 1659-1668.  
27 Chen H, Luo XS, Poon AW. Cavity-enhanced photocurrent generation by  $1.55\mu \mathrm{m}$  wavelengths linear absorption in a p-i-n diode embedded silicon microring resonator. Appl Phys Lett 2009; 95: 171111.  
28 Grillanda S, Morichetti F. Light-induced metal-like surface of silicon photonic waveguides. Nat Commun 2015; 6: 8182.  
29 Fontaine NK, Doerr CR, Mestre MA, Ryf R, Winzer P et al. Space-Division Multiplexing and All-Optical MIMO Demultiplexing Using a Photonic Integrated Circuit. Proceedings of National Fiber Optic Engineers Conference; 4-8 March 2012; Los Angeles, California, USA. Optical Society of America: Los Angeles, California, USA 2012.  
30 Grillanda S, Carminati M, Morichetti F, Ciccarella P, Annoni A et al. Non-invasive monitoring and control in silicon photonics using CMOS integrated electronics. Optica 2014; 1: 129-136.  
31 Ciccarella P, Carminati M, Ferrari G, Bianchi D, Grillanda S et al. Impedance-sensing CMOS chip for noninvasive light detection in integrated photonics. IEEE Trans Circuit Syst II 2016; 63: 929-933.  
32 Grillanda S, Morichetti F, Peserico N, Ciccarella P, Annoni A et al. Non-invasive monitoring of mode-division multiplexed channels on a silicon photonic chip. J Lightwave Technol 2015; 33: 1197-1201.  
33 Annoni A, Guglielmi E, Carminati M, Grillanda S, Ciccarella P et al. Automated routing and control of silicon photonic switch fabrics. IEEE J Sel Top Quantum Electron 2016; 22: 3600408.  
34 Carminati M, Annoni A, Morichetti F, Guglielmi E, Ferrari G et al. Design guidelines for contactless integrated photonic probes in dense photonic circuits. J Lightwave Technol 2017; 35: 3042-3049.  
35 Lin Q, Painter OJ, Agrawal GP. Nonlinear optical phenomena in silicon waveguides: Modeling and applications. Opt Express 2007; 15: 16604-16644.  
36 Wilkes CM, Qiang X, Wang J, Santagati R, Paesani S et al. 60 dB high-extinction auto-configured Mach-Zehnder interferometer. Opt Lett 2016; 41: 5318-5321.  
37 Halir R, Cheben P, Luque-González JM, Sarmiento-Merenguel JD et al. Ultra-broadband nanophotonic beamsplitter using an anisotropic sub-wavelength metamaterial. *Laser Photonics* Rev 2016; 10: 1039-1046.  
38 Bruck R, Vynck K, Lalanne P, Mills B, Thomson DJ et al. All-optical spatial light modulator for reconfigurable silicon photonic circuits. Optica 2016; 3: 396-402.  
39 Zhou X, Liu H, Urata R. Datacenter optics: requirements, technologies, and trends. Chin Opt Lett 2017; 15: 120008.  
40 Hayashi T, Tamura Y, Hasegawa T, Taru T. Record-low spatial mode dispersion and ultra-low loss coupled multi-core fiber for ultra-long-haul transmission. J Lightwave Technol 2017; 35: 450-457.  
41 Randel S, Ryf R, Gnauck A, Mestre MA, Schmidt C et al. Mode-Multiplexed  $6 \times 20$ -GBd QPSK Transmission over 1200-km DGD-Compensated Few-Mode Fiber. Proceedings of National Fiber Optic Engineers Conference; 4-8 March 2012; Los Angeles, California, USA. Optical Society of America: Los Angeles, California, USA 2012.  
42 Clements WR, Humphreys PC, Metcalf BJ, Kolthammer WS, Walmsley IA. Optimal design for universal multiport interferometers. Optica 2016; 3: 1460-1465.  
43 Shen YC, Harris NC, Skirlo S, Prabhu M, Baehr-Jones T et al. Deep learning with coherent nanophotonic circuits. Nat Photonics 2017; 11: 441-446.

44 Capmany J, Gasulla I, Pérez D. Microwave photonics: The programmable processor. Nat Photonics 2015; 10: 6-8.  
45 Miller DAB. Establishing optimal wave communication channels automatically. J Lightwave Technol 2013; 31: 3987-3994.  
46 Doerr CR. Proposed architecture for MIMO optical demultiplexing using photonic integration. IEEE Photonics Technol Lett 2011; 23: 1573-1575.  
47 Melati D, Carminati M, Grillanda S, Ferrari G, Morichetti F et al. Contactless integrated photonic probe for light monitoring in indium phosphide-based devices. IET Optoelectron 2015;9:146-150.

![](images/5a4c93c55033cea4af6a6dcb56cd38da62ebe5df9a512259c5ef33a732e962ce.jpg)

This work is licensed under a Creative Commons Attribution 4.0 International License. The images or other third party material in this

article are included in the article's Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder to reproduce the material. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/

$\langle \widehat{\mathbb{C}}\rangle$  The Author(s) 2017

Supplementary Information for this article can be found on the Light: Science & Applications' website (http://www.nature.com/lsa).