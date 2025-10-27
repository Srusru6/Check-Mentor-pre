# ARTICLE OPEN

# High-dimensional optical quantum logic in large operational spaces

Poolad Imany  $^{1,2}$ , Jose A. Jaramillo-Villegas  $^{1,2,3}$ , Mohammed S. Alshaykh  $^{1,2}$ , Joseph M. Lukens  $^{4}$ , Ogaga D. Odele  $^{1,2}$ , Alexandria J. Moore  $^{1,2}$ , Daniel E. Leaird  $^{1,2}$ , Minghao Qi  $^{1,5}$  and Andrew M. Weiner  $^{1,2,5}$

The probabilistic nature of single-photon sources and photon-photon interactions encourages encoding as much quantum information as possible in every photon for the purpose of photonic quantum information processing. Here, by encoding high-dimensional units of information (qubits) in time and frequency degrees of freedom using on-chip sources, we report deterministic two-qudit gates in a single photon with fidelities exceeding 0.90 in the computational basis. Constructing a two-qudit modulo SUM gate, we generate and measure a single-photon state with nonseparability between time and frequency qubits. We then employ this SUM operation on two frequency-bin entangled photons—each carrying two 32-dimensional qubits—to realize a four-party high-dimensional Greenberger-Horne-Zeilinger state, occupying a Hilbert space equivalent to that of 20 qubits. Although high-dimensional coding alone is ultimately not scalable for universal quantum computing, our design shows the potential of deterministic optical quantum operations in large encoding spaces for practical and compact quantum information processing protocols.

npj Quantum Information (2019)5:59; https://doi.org/10.1038/s41534-019-0173-8

# INTRODUCTION

Quantum information processing has drawn massive attention due to its power in solving some crucial algorithms exponentially faster than their classical counterparts, as well as its ability to transmit information in a fully secure fashion, two capabilities looked to be combined in the emerging quantum internet. Among the platforms that can exhibit quantum behavior, optical states have the advantages of low decoherence and suitability for long-distance communications, yet the weak coupling of photons to their surroundings also makes it extremely difficult to manipulate the state of one photon based on the state of another. This operation, needed for a two-qubit gate, is probabilistic with standard linear optics and photon counting. Quantum gates have been demonstrated in a number of different photonic degrees of freedom, such as polarization, orbital angular momentum, time, and frequency, and to sidestep the challenges of probabilistic multiphoton interactions, encoding qubits in different degrees of freedom (DoFs) in a single photon has been demonstrated, where each DoF carries one qubit and, now, operations between different qubits can be made deterministic. This scheme allows encoding more quantum information in single photons, and can find use in stand-alone processing tasks or be subsequently incorporated into larger systems built on true photon-photon interactions, thus offering a potentially more efficient method for photonic quantum information processing. Even though in this case two- and three-qubit operations can be executed with unity success probability, each DoF contains only one qubit, and the number of a photon's DoFs are limited; thus the size of the Hilbert space in which these deterministic transformations can happen is fairly moderate (e.g., an eight

dimensional Hilbert space has been demonstrated by encoding three qubits in three different DoFs of a single photon<sup>10</sup>.

In this article, we take advantage of the high dimensionality in two particular DoFs of a single photon—namely, time and frequency, which are both compatible with fiber optical transmission—to encode one qudit in each DoF. We consider multiple time bins and frequency bins; as long as the frequency spacing between different modes  $(\Delta f)$  and the time-bin spacing  $(\Delta t)$  are chosen such that they exceed the Fourier transform limit (i.e.,  $\Delta f$ $\Delta t > 1$ ), we are able to manipulate the time and frequency DoFs independently in a hyper-encoding fashion, using concepts developed in time-division and wavelength-division multiplexing, respectively.[11,12] In other words, each time-frequency mode pair constitutes a well-defined entity, or plaquette,[11,12] which is sufficiently separated from its neighbors to provide stable encoding (Fig. 1). Alternatively, this can be understood by considering bandwidth-limited plaquettes with individual spectral linewidth  $\delta f$  (corresponding to temporal duration  $\sim 1 / \delta f$ ). These will not overlap in time-frequency space as long as the chosen bin separations satisfy  $\Delta f > \delta f$  and  $\Delta t > 1 / \delta f$ . Combined, then, these two equations yield the aforementioned condition  $\Delta f\Delta t > 1$ . An analogous process is at work in the advanced optical modulation formats gaining adoption in modern digital communications, where many bits are encoded in a single symbol via modulation of canonically conjugate quadratures.[13] Since our single photons can potentially be generated in a superposition of many time and frequency bins, multiple qubits can be encoded in each DoF, making our proposed scheme a favorable platform for deterministic optical quantum information processing on Hilbert spaces dramatically larger than previously demonstrated deterministic

![](images/cd783ca551a4cbef7d72678ef3d3fbb380e506a564bdb6cd22357820b26f00a5.jpg)  
Fig. 1 Illustration of the scheme. Two quuds encoded in  $d$  time bins and frequency bins in a single photon, going through a deterministic quantum process. The single photon can be encoded in an arbitrary superposition of different time and frequency bins; the unused time-frequency slots are shown with dashed circles. After the deterministic quantum process operates on the two-qudit state, the orientation of the time-frequency superpositions change to a new two-qudit state

qubit-based gates. Ultimately, the total number of DoFs carried by a single photon is limited, so one cannot increase the Hilbert space indefinitely by encoding in increasingly more properties within individual photons. The Hilbert space can be increased, though, by expanding the dimensionality within each DoF. While enabling only linear scaling of the Hilbert space with the number of modes,[14] and thereby not facilitating the exponential scaling required for fault-tolerant quantum computing, qudit encoding promises significant potential in the current generation of quantum circuits. It has been shown, for example, that two-qudit optical gates are useful in transmitting quantum states with higher information content per photon by means of qudit teleportation,[15] a task that requires two-qudit gates which can operate on the different degrees of freedom of a single photon[16,17]—precisely the functionality we demonstrate here.

# RESULTS

To enable the realization of all single-qudit unitaries, it is sufficient to demonstrate the generalized Pauli gates X (cyclic shift) and Z (state-dependent phase), which are universal for single-qudit operations, $^{5}$  and from which all  $d$ -dimensional Weyl operators can be constructed. $^{18}$  The Z gate applies a unique phase shift to each of the  $d$  basis states, which can be easily executed with a phase modulator and a pulse shaper in the time domain and frequency domain, respectively. Specifically, for the basis state  $|n\rangle$  ( $n = 0, 1, \ldots, d-1$ ), we have  $Z|n\rangle = \exp(2\pi i n / d)|n\rangle$  and  $X|n\rangle = |n \oplus 1\rangle$ , where  $\oplus$  denotes addition modulo  $d$ . An X gate in the frequency domain can be realized using a Z gate sandwiched between two high-dimensional DFT gates. Such a DFT operation has been recently demonstrated, $^{7}$  completing in principle the universal gate set for single-qudit frequency-domain operations. To complete the gate set in the time domain, we demonstrate the time-bin X gate presented in Fig. 2a, operating on time bins in three dimensions, a process which corresponds to state-dependent delay. Because the gate operates on each photon individually, we can simulate its performance with coherent states; the statistics of the input field have no impact on the principle of operation. Of course, to apply this gate in multiphoton quantum information processing, true single photons would need to be tested as well, the preparation or heralding of which is technically demanding and could introduce additional noise. However, as this noise is extrinsic to the gate itself, we focus on weak coherent states for initial characterization here. To test for the correct modal operation of this gate, we use a continuous-wave (CW) laser and prepare the desired weak coherent state by carving out three time bins  $\{|0\rangle_t, |1\rangle_t, |2\rangle_t\}$  using an intensity modulator and manipulating their relative phases with a phase modulator. The time bins are 3-ns wide with  $\Delta t = 6$ -ns center-to-center spacing. To perform the X operation, we need to separate the time bins  $|0\rangle_t$  and  $|1\rangle_t$  from  $|2\rangle_t$  and delay the route for time bins  $|0\rangle_t$  and  $|1\rangle_t$  by 3 bins (18 ns). We realize the necessary spatial separation between the time bins with a Mach-Zehnder modulator (MZM) switch. We emphasize that

while most MZM designs are one-port devices, with one of the two output paths terminated, this  $1 \times 2$  version permits access to both interferometer outputs, and accordingly it is in principle lossless—as required for a unitary operation. (In practice, of course, insertion loss reduces throughput, but it should be possible in the future to significantly reduce this loss through, e.g., on-chip integration.) After the path-dependent delay, another  $1 \times 2$  MZM, but operated in reverse, can be used to recombine the time bins deterministically as well. However, due to lack of equipment availability, in this proof-of-principle experiment we employ a  $2 \times 2$  fiber coupler for recombination, which introduces an additional 3-dB power penalty. To measure the gate output, we synchronize a single-photon detector and time interval analyzer with the generated time bins. The transformation matrix performed by the X gate when probed by single time bins yields a computational basis fidelity  $\mathcal{F}_{\mathrm{C}}$  of  $0.996 \pm 0.001$ , shown in Fig. 2b (see the Methods section). As such computational-basis-only measurements do not reflect the phase coherence of the operation, we next prepare superposition states as input and interfere the transformed time bins after the gate with a cascade of 1-bin and 2-bin delay unbalanced interferometers. In order to combat environmentally induced phase fluctuations, we stabilize both these interferometers and the X gate by sending a CW laser in the backwards direction and using a feedback phase control loop. We apply a phase of  $0$ ,  $\phi$ , and  $2\phi$  to the time-bins  $\left|0\rangle_{t}, \left|1\rangle_{t}\right.$  and  $\left|2\rangle_{t}\right.$ , respectively, with the phase modulator in the state preparation stage and sweep  $\phi$  from  $0$  to  $2\pi$ , obtaining the interference pattern shown in Fig. 2c. After subtraction of the background, we calculate a visibility of  $0.94 \pm 0.01$  from the maximum and minimum points, showing strong phase coherence (the ability to preserve and utilize coherent superpositions) between the time bins after the gate. If for concreteness we assume a channel model consisting of pure depolarizing (white) noise, $^{18}$  we can use this visibility to estimate the process fidelity  $\mathcal{F}_{\mathrm{P}}$ , finding  $\mathcal{F}_{\mathrm{P}} = 0.92 \pm 0.01$  for the X gate (see the Methods section). Given the ability to perform arbitrary one-qudit operations using combinations of X and Z gates, it follows that it is in principle possible to generate and measure photons in all mutually unbiased bases $^{19}$ —an essential capability for high-dimensional quantum key distribution (QKD) $^{20}$  which has been proven to offer greater robustness to noise compared with qubit-based QKD $^{21}$  and can enable significantly higher secret key rates over metropolitan-scale distances. $^{22}$

With this high-performance time-bin X gate in hand, we are then in a position to incorporate it into a frequency network to realize deterministic two-qudit gates, where the frequency DoF acts as the control and the time DoF is the target qudit. For this demonstration, instead of a weak coherent state, we utilize true single photons, heralded by detecting the partner photon of a frequency-bin entangled pair generated through spontaneous four-wave mixing in an on-chip silicon nitride microresonator. The time bins, defined by intensity modulation of the pump, couple into a microring resonator with a free spectral range (FSR)  $\Delta f =$

![](images/89901a6da9a325e9b9918f23c4e9f1eb73c301e6d42aa3c600db58f6f679d55a.jpg)  
b.

![](images/c28fbed77df35200e3dc66e9052223d8d1e953ec256174942d890d3905940a1d.jpg)  
Fig. 2 a Experimental setup of the state preparation, the X gate, and the state measurement. IM intensity modulator, PM phase modulator, MZM Mach-Zehnder modulator, PZT piezo-electric-phase shifter, SPD single-photon detector. The circle-shaped fibers indicate the delay; each circle is equivalent to one time-bin delay (6 ns). b The transformation matrix. c Counts measured after overlapping all three output time bins, for a time-bin superposition state input into the X gate. The blue errorbars are obtained from five measurements for each phase. The subtracted background was about 200 per 2 s

![](images/650200a342ac83aeb3412ca5e7293594552889d3263ea8557264cac73b18a7aa.jpg)

380 GHz and resonance linewidths  $\delta f\simeq 250\mathrm{MHz}$ , generating a biphoton frequency comb. The time-bin and frequency-bin entanglement of such sources have been proven recently.[23-26] As our time- and frequency-bins exceed the Fourier limit ( $\Delta f\Delta t = 2280$ ,  $\delta f\Delta t = 1.5$ ), our time-frequency entangled photons can be considered hyperentangled—that is, entangled in two fully separable DoFs. The signal and idler photons from the first three comb-line pairs are then selected and separated with a commercial pulse shaper, as shown in Fig. 3a. Now that the time bins and frequency bins are all generated in the state preparation stage, the idler photons are sent to a single-photon detector for heralding, and the signal photons are what carry the two quuds in the three time bins  $\{|0\rangle_{\mathrm{t}}, |1\rangle_{\mathrm{t}}, |2\rangle_{\mathrm{t}}\}$  and frequency bins  $\{|0\rangle_{\mathrm{f}}, |1\rangle_{\mathrm{f}}, |2\rangle_{\mathrm{f}}\}$ . This procedure lets us prepare any time-bin/frequency-bin product state  $|m\rangle_{\mathrm{t}}|n\rangle_{\mathrm{f}}$  ( $m, n = 0, 1, 2$ ) of the full computational basis set. In principle, we could also herald arbitrary time-frequency superposition states in this setup, by first sending the idler photon through a combination of time- or frequency-bin interferometers prior to detection in the temporal and spectral eigenbases. This more general case would permit the preparation of any two-qudit state and is an important area for further research.

As the first two-qudit gate, we demonstrate the controlled-increment (CINC) operation, where an X gate is applied to the time-bin qudit only when the frequency qudit is in the state  $|2\rangle_{\mathrm{f}}$ . This two-qudit gate along with arbitrary single-qudit gates [which, as noted above, can be formed from single-qudit X and Z operations] complete a universal set for any quantum operation.[27] To implement this gate, we separate  $|2\rangle_{\mathrm{f}}$  from the other two frequency bins with a dense wavelength-division multiplexing (DWDM) filter and route it to a time-bin X gate (Fig. 3a); no operation happens on the route of the other two frequency bins. The frequency bins are then brought back together with another DWDM with zero relative delay to complete the two-qudit gate operation. To measure the transformation matrix of this gate in the computational basis, we prepare the input state in each of the nine combinations of single time bins and frequency bins, using the first intensity modulator and the pulse shaper, respectively. We then record the signal counts in all possible output time-bin/ frequency-bin pairs, conditioned on detection of a particular idler

time-frequency mode, by inserting three different DWDMs in the path of the signal photons to pick different frequency bins. The measured transformation matrix is shown in Fig. 3b, with accidental-subtracted fidelity  $\mathcal{F}_C = 0.90 \pm 0.01$  (see the Methods section).

For the next step, we implement an even more complex operation, the SUM gate—a generalized controlled-NOT gate[28]—which adds the value of the control qudit to the value of the target qudit, modulo 3. In this gate, the time bins associated with  $|0\rangle_{\mathrm{f}}$  are not delayed, the time bins associated with  $|1\rangle_{\mathrm{f}}$  experience a cyclic shift by 1 slot, and the time bins corresponding to  $|2\rangle_{\mathrm{f}}$  go through a cyclic shift of 2 slots. To delay the time bins dependent on their frequencies, we induce a dispersion of  $-2\mathrm{ns.nm}^{-1}$  on the photons using a chirped fiber Bragg grating (CFBG); this imparts 6-ns (1-bin) and 12-ns (2-bin) delays for the temporal modes of  $|1\rangle_{\mathrm{f}}$  and  $|2\rangle_{\mathrm{f}}$ , respectively, as required for the SUM operation. However, this delay is linear—not cyclic—so that some of the time bins are pushed outside of the computational space, to modes  $|3\rangle_{\mathrm{t}}$  and  $|4\rangle_{\mathrm{t}}$ . Returning these bins to overlap with the necessary  $|0\rangle_{\mathrm{t}}$  and  $|1\rangle_{\mathrm{t}}$  slots can be achieved using principles identical to the time-bin X gate with a relative delay of three bins. The experimental setup is shown in Fig. 3a, where we use the same techniques as for the CINC gate to measure the transfer matrix shown in Fig. 3c, with  $\mathcal{F}_{\mathrm{C}} = 0.92 \pm 0.01$ . The fact that this SUM gate is implemented with quuds in a single step potentially reduces the complexity and depth of quantum circuits in algorithms that require an addition operation.[29] Lack of frequency shifting components in these gates can be confirmed by the small off-diagonal terms in Fig. 3b, c for which the input and output frequency bins differ.

To show the ability of our design to operate on large Hilbert spaces, we extend the dimensions of our quuds and encode two 16-dimensional quantum states in the time and frequency DoFs of a single photon. For this demonstration, as we want to use more time bins and set a smaller frequency spacing between modes, we use a periodically poled lithium niobate (PPLN) crystal as a broadband source of time-frequency entangled photons followed by a programmable pulse shaper to set the frequency spacing and linewidth, instead of a microring with fixed frequency spacing. (We note that, in principle, one could still use an integrated source

![](images/2b63a2a31b55d0b8ffdbae956199344a5c53b53cc3555fb1732b01fff633c5f3.jpg)

![](images/06cfb200f75c9a5318acbb53bccbeedbd96f96882a9b53337b4138f2fefab4f8.jpg)  
Fig. 3 a Experimental setup for the CINC and SUM gates. The MZM for the CINC gate is driven such that it separates the time bin  $|2\rangle_{\mathrm{t}}$  from time bins  $|0\rangle_{\mathrm{t}}$  and  $|1\rangle_{\mathrm{t}}$ . For the SUM gate, the MZM separates the time bins that fall outside of the computational space  $(|3\rangle_{\mathrm{t}}$  and  $|4\rangle_{\mathrm{t}})$  from the computational space time bins  $(|0\rangle_{\mathrm{t}}, |1\rangle_{\mathrm{t}}$  and  $|2\rangle_{\mathrm{t}}$ . DWDM dense wavelength-division multiplexer. b, c The experimental transformation matrix of the CINC and SUM gate, respectively. The accidents were subtracted in the transformation matrices, and the coincidence to accidents ratio was  $\sim 3.7$  in the CINC and  $\sim 3$  in the SUM case

![](images/86118b1f4cab5b382ddaddbc282e3e50e556964027330b2607d1573bde727038.jpg)

for these experiments by appropriately engineering a microring's FSR, bandwidth, and resonance linewidth to realize spectral and temporal spacings tighter than the integrated photon sources currently available to us.) In this experiment, we first shine a 773-nm CW laser on the PPLN crystal, generating entangled photons with a bandwidth of  $\sim 5\mathrm{THz}$ .<sup>30</sup> We then carve 16 time bins with a full width at half maximum of  $\sim 200$  ps and 1.2-ns spacing between them, to generate the time-bin quuds. Then, a pulse shaper is used to carve out the frequency of these entangled photons to generate sixteen 22-GHz-wide frequency bins on both the signal and idler side of the spectrum, each spaced by 75 GHz from each other. Now that we have 16-dimensional quuds in both time and frequency, we send a heralded signal photon into the same SUM-gate structure. We note that after the CFBG, the individual time bins will spread to  $\sim 350$  ps due to their now larger (22 GHz) linewidth. While not necessary in this proof-of-principle experiment, such spreading could be reduced either by using a smaller linewidth for our frequency modes (e.g., with a Fabry-Perot etalon), or by using a dispersive element with a step-wise frequency-dependent delay profile.<sup>31-33</sup> To verify the operation, we send in different input two-qudit states, chosen from one of 256 basis states, and measure the output after the gate. While this yields a total of  $256\times 256$  ( $2^{16}$ ) computational input/output combinations to test, we have no active frequency-shifting elements in the SUM gate to shift 75 GHz-spaced frequencies into each other, so we make the reasonable assumption that the frequency qudit remains unchanged through the operation. This is also enforced by the high extinction ratio of the pulse shaper ( $\sim 40$  dB), which blocks unwanted frequency bins. This allows us to focus on results in the sixteen  $16\times 16$  transfer matrices measured in Fig. 4a-p (a subset with a total of  $2^{12}$  input/output combinations). In each matrix, 16 different inputs with the

same frequency and different time bins are sent into the SUM gate, and the output time bins are measured. For this experiment, we use superconducting nanowire single-photon detectors (SNSPDs), which allow us to report our data without accidental subtraction. The average computational space fidelity for the whole process, with the assumption that frequencies do not leak into each other, can be calculated as  $\overline{\mathcal{F}}_C = 0.9589\pm 0.0005$ , which shows the high performance of our operation. This high fidelity benefits greatly from the high extinction ratio of the intensity modulator used to carve the time bins ( $\sim25$  dB). To show the coherence of our SUM gate, we use this setup to perform a SUM operation on a three-dimensional input state,  $|\psi\rangle_{\mathrm{in}} = \frac{1}{\sqrt{3}}\left(|0\rangle_{\mathrm{f}} + |1\rangle_{\mathrm{f}} + |2\rangle_{\mathrm{f}}\right)|0\rangle_{\mathrm{t}}$ , which results in a maximally nonseparable state[34] between time and frequency DoFs:  $|\psi\rangle_{\mathrm{out}} = \frac{1}{\sqrt{3}}\left(|00\rangle_{\mathrm{ft}} + |11\rangle_{\mathrm{ft}} + |22\rangle_{\mathrm{ft}}\right)$ . To quantify the dimensionality of this state, we use an entanglement certification measure called entanglement of formation ( $E_{\mathrm{of}}$ )[35,36] We experimentally obtain  $E_{\mathrm{of}} \geq 1.19 \pm 0.12$  ebits, where 1 ebit corresponds to a maximally nonseparable pair of qubits, while 1.585 ebits represents the maximum for two three-dimensional parties (see Methods); in exceeding the qubit limit, our state thus possesses true high-dimensional nonseparability.

One of the most crucial challenges toward optical quantum operations is the lack of on-demand photon sources. Therefore, it is interesting to consider our scheme for application to quantum communication and networking, for which operations with just a few qubits have potential impact. A gate very similar to the SUM gate is the XOR gate, which subtracts the control qudit from the target and is a requirement for qudit teleportation protocols.[15,37,38] Since teleportation of quantum states is possible using different degrees of freedom of an entangled photon pair,[165] a

![](images/bd8c136fafd82cf477b2f9e5bf16785b0c7f1c7ad9f6602eb3cf16e36ae646cf.jpg)

![](images/004de9b0b3e524b6be43f91a607dbf068477565c8c61dded968f75caad007ed0.jpg)

![](images/41cee4b23068375e1b30e40d7e4273de5273095f6407401546f04632a728b1cd.jpg)

![](images/4f2254cf01e13113750e5d95e01f9be502a4b9e674fee7620c73e6a55a76f574.jpg)

![](images/63e5728da77f88987c8a2e0c5c30584bdc4e46c2d6ed3d14397d1e126a5b7d99.jpg)

![](images/1e90c2971b6e2aec2eaa75773dc305c327ccab7563d3cb195ed14882314a6a66.jpg)

![](images/c1a7585d24d46c50e19abadfa416459c8627c62c850e6cffedbb1a96ef3373bd.jpg)

![](images/86d90a6f63b46cf720de212371297a8f96b0f062e9796eae157e3dc39e2e99dd.jpg)

![](images/f13b294633540a1758c5801a67ff86df0fc414668d3d4ed97f9f94f6c42b00e2.jpg)

![](images/b10906d6e2a0e9d069c6add76621ad9f18e9f2094b63dccde9b3e10f5602a068.jpg)

![](images/08093c94a8fff29488fe8147afc22c64923d8034ddc048e1865610936bab292d.jpg)

![](images/ccace3612994dc6abbb48a8e45f53873b43caf16e170d2ebe18d9c408060ccd3.jpg)

![](images/4a81f792c27be99bc8c730c1a7d3a1018886740f9bafa2f0cc04f1d879f7e20d.jpg)

![](images/95488c386137e140ef59fde6a409ef1c8d8d68599f6187c1b029751e763f5fb1.jpg)  
Fig. 4 a-p The transfer matrices corresponding to each possible time-bin output for each individual input time bin. Each matrix is specified for one frequency input, where the matched frequency output for different time bins is measured. In  $|m, n\rangle$  on the  $x$  and  $y$  axis,  $m$  indicates the frequency qudit and  $n$  is the time bin qudit. The computational space fidelity of each matrix is shown on top of it. Subtraction of accidents is not employed

![](images/2d1431db463ae753c2090976fb33eacd3ecce94f832822a42017a88e29d5ab12.jpg)

![](images/16255797692c46a27153e8c4dd1ff27552db496a733a8676f00c852ce8b1d216.jpg)

![](images/ed0260b68ce37f077d1cb53ede8c46f0692e7dd8cd6762f7322124a6e41d7b9e.jpg)

single-photon two-qudit gate in our time-frequency paradigm could be applied directly for teleporting high-dimensional states. Specifically, the XOR gate can be demonstrated by using positive dispersion and reconfiguring the switching in the SUM gate, or in the three-dimensional case, by simply relabeling the frequency bins  $|0\rangle_{\mathrm{f}} \rightarrow |2\rangle_{\mathrm{f}}$  and  $|2\rangle_{\mathrm{f}} \rightarrow |0\rangle_{\mathrm{f}}$  and performing the same process as the SUM operation. In addition, these two-qudit gates can be used for the purpose of beating the channel capacity limit for standard superdense coding for high-dimensional entangled states.[39] In such quantum communications applications for the two-qudit gates, a modest number of state manipulations brings significant value.

The demonstrated SUM gate can also be used to produce high-dimensional Greenberger-Horne-Zeilinger (GHZ) states. $^{40}$  GHZ

states consist of more than two parties, entangled with each other in a way that measurement of one party in the computational basis determines the state of all the other parties.41 It has been only recently that these states were demonstrated in more than two dimensions, where a three-dimensional three-party GHZ state was realized using the orbital angular momentum of optical states.40 Here, we take advantage of our SUM gate and the large dimensionality of time-frequency states to generate a four-party GHZ state with 32 dimensions in each DoF. We start from the state  $|\psi \rangle_{\mathrm{in}} = \frac{1}{\sqrt{32}} |0,0\rangle_{\mathrm{t}_s\mathrm{t}_i}\sum_{m = 0}^{31}|m,m\rangle_{\mathrm{f}_s\mathrm{f}_i},$  which means both signal and idler photons are initialized in the zero time-bin state and are maximally entangled in the frequency domain. Then, we operate deterministic SUM gates separately on both signal and idler photons, resulting in a four-party GHZ state of the form

![](images/bf1382f3d49fcd1094abb2ab6dcb00e803a9f08c0dadb16f9dddb62c9e35c363.jpg)  
Fig. 5 a Measurement of the four-party 32-dimensional GHZ state in the computational basis. The states  $|m,n\rangle$  shown on the signal and idler axes correspond to frequency-bin  $m$  and time-bin  $n$ . The large coincidence peaks exist only for states with the same time-bin and frequency-bin indices for both signal and idler (32 peaks). b, c Zoomed-in  $32\times 32$  submatrices of the matrix shown in a. Each submatrix shows coincidences for different signal and idler time bin indices for fixed signal and idler frequency bin indices. b Matched signal and idler frequency bins: large peak is observed for  $|16,16,16,16\rangle_{f_s,t_s,f_t_i}$ . c Unmatched signal and idler frequency bins. The small peak evident at  $|16,16,23,23\rangle_{f_s,t_s,f_t_i}$  reflects additional counts from multiphoton pair events at the time bins to which frequency bins  $|16\rangle_{f_s}$  and  $|23\rangle_{f_i}$  are shifted. The data are shown with accidents subtracted (coincidence to accidents ratio of  $\sim 4$ )

![](images/928fb95ec1b7ccb7611a61eebbae6b4010710ec566b4cb71142e7a7f96ef50be.jpg)

![](images/2e1d46d471629f344e45070218d7415703fef1cbd9597630170b14a3c0738479.jpg)

$|\psi\rangle_{\mathrm{out}} = \frac{1}{\sqrt{32}}\sum_{m=0}^{31}|m,m,m,m\rangle_{\mathrm{f}_{\mathrm{s}}\mathrm{t}_{\mathrm{s}}\mathrm{f}_{\mathrm{t}_{\mathrm{i}}}}$ . Since the initial state only consists of the zeroth time bins, the dispersion module does not shift any of the bins outside of the computational space; hence the interferometric structure used in the full SUM gate is not required when operating within this subspace. The GHZ state is measured in the computational basis (Fig. 5); the plot contains coincidences for all basis states in the set  $\{|m,n,k,l\rangle_{\mathrm{f}_{\mathrm{s}}\mathrm{t}_{\mathrm{s}}\mathrm{f}_{\mathrm{t}_{\mathrm{i}}}};0\leq m,n,k,l\leq 31\}$ . Only states whose four qubits match (i.e.,  $|m,m,m,m\rangle_{\mathrm{f}_{\mathrm{s}}\mathrm{t}_{\mathrm{s}}\mathrm{f}_{\mathrm{t}_{\mathrm{i}}}}$  have high counts, as expected for a GHZ state. Of course, full characterization of the state requires measurements in superposition bases as well,[42] but due to the additional insertion loss associated with superposition measurements in time and frequency using interferometers and phase modulators, respectively, we were unable to measure such projections. Remarkably, the demonstrated GHZ state resides in a Hilbert space equivalent to that of 20 qubits, an impressive 1,048,576 ( $32^4$ ) dimensions. We emphasize that the four parties of the demonstrated GHZ state are carried by only two photons, and hence cannot be used for genuine multi-partite GHZ applications such as demonstration of Bell's theorem without inequalities,[41] quantum secret sharing,[43] or open-destination teleportation.[44] However, the realization of such high-dimensional GHZ states indicates the potential of our time-frequency platform for quantum technologies such as near-term quantum computation and cluster-state generation.[33,45]

# DISCUSSION

Hyper-entangled time-frequency states, as opposed to other high-dimensional optical degrees of freedom like orbital angular

momentum, can be generated in integrated on-chip sources, which have gained tremendous attention in recent years due to their low cost, room temperature operation, compatibility with CMOS foundries and the ability to be integrated with other optical components. Pulse shapers,[46] phase modulators,[47] and switches[48] can all be demonstrated on a chip, and a series of DWDMs and delay lines can be used to realize the equivalent functionality of on-chip CFBG. In addition, demonstration of balanced and unbalanced interferometers on-chip eliminates the need for active stabilization, which is of considerable profit for the scalability of the scheme.[49] These contributions can potentially lead to combining these sources with on-chip components designed for manipulation of these states, realizing the whole process on an integrated circuit.

High-dimensional optical states $^{25,26,49-51}$  can open the door to deterministically carry out various quantum operations in relatively large Hilbert spaces, $^{52}$  as well as enable higher encoding efficiency in quantum communication protocols, such as quantum key distribution $^{22}$  and quantum teleportation. $^{16,53}$  We have demonstrated deterministic single- and two-qudit gates using the time and frequency degrees of freedom of a single photon for encoding—operating on up to 256 ( $2^{8}$ )-dimensional Hilbert spaces—and carried out these gates with a high computational-space fidelity. We have shown the application of such two-qudit gates in near-term quantum computation by using them to realize a GHZ state of four parties with 32 dimensions each, corresponding to a Hilbert space of more than one million modes. Such deterministic quantum gates add significant value to the photonic platform for quantum information processing and have direct application in, e.g., simulation of quantum many-body physics. $^{54-56}$

# METHODS

For the time-bin single-qudit X gate shown in Fig. 2, we split the experimental setup in three stages: state preparation, X gate operation, and state measurement. For the state preparation, we use an Agilent 81645A CW laser tuned to  $1553.9\mathrm{nm}$  and send it into an intensity modulator (~4-dB insertion loss) and phase modulator (~3-dB insertion loss), both manufactured by EOSpace, which are used to create the time bins and control their relative phases, respectively. To implement the X gate operation, we used an MZM with two complementary outputs (~4-dB insertion loss), also manufactured by EOSpace. We use a piezo-based fiberphase shifter (General Photonics FPS-001) to control the phase difference between the two paths following the MZM. Then a  $2\times 2$  fiber coupler is used to merge the branches. For the state measurement, we used 1-bin and 2-bin delay interferometers implemented with  $2\times 2$  fiber couplers and additional piezo-based fiber phase shifters. For the time-bin X gate and computational-basis measurements of three-dimensional two-qudit gates, gated InGaAs single-photon detectors (Aurea Technologies SPD_AT_M2) were used. For the rest of the measurements, we used superconducting nanowire single-photon detectors (Quantum Opus). To measure the arrival times of the photons on the single-photon detectors, a time-interval analyzer (PicoQuant HydraHarp 400) is used. The stabilization of the interferometers is done by sending a CW laser at  $1550.9\mathrm{nm}$  in the backward direction and feeding the output power into a computer-based feedback loop to maintain the phase. To stabilize the X gate, we use a similar scheme with an additional circulator at the input of the gate (not shown in the figures) to retrieve the optical power in the backward direction. The signals applied to the intensity modulators and phase modulator, as well as the trigger and synchronization signal of the single-photon detector and time interval analyzer, are generated by an electronic arbitrary waveform generator (Tektronix AWG7122B) and adjusted to the proper level by linear amplifiers.

To assess the performance of our one- and two-qudit quantum gates, we first focus on the computational-basis fidelity  $\mathcal{F}_C$  —one example of a so-called "classical" fidelity in the literature.[57] Defining  $|n\rangle$  ( $n = 0,1,\dots,N-1$ ) as the set of all computational basis states and  $|u_n\rangle$  as the corresponding output states for a perfect operation, we have the fidelity

$$
\mathcal {F} _ {C} = \frac {1}{N} \sum_ {n = 0} ^ {N - 1} p (u _ {n} | n) \tag {1}
$$

where  $p(u_n|n)$  is the probability of measuring the output state  $|u_n\rangle$  given an input of  $|n\rangle$ . In the operations considered here, the ideal output states  $|u_{n}\rangle$  are members of the computational basis as well, so there is no need to measure temporal or spectral superpositions in determination of  $\mathcal{F}_C$ . Given the measured counts, we retrieve the  $N$  conditional probability distributions via Bayesian mean estimation (BME),[58,59] where our model assumes that each set of count outcomes (after accidents subtruction) follows a multinomial distribution with to-be-determined probabilities; for simplicity, we take the prior distributions as uniform (equal weights for all outcomes). We then compute the mean and standard deviation of each value  $p(u_n|n)$  and sum them to arrive at  $\mathcal{F}_C$ . Specifically, if  $C_{u_n|n}$  signifies the counts measured for outcome  $u_{n}$ , and  $C_{\mathrm{tot}|n}$ , the total counts over all outcomes (both for a given input state  $|n\rangle$ ), BME predicts:

$$
p \left(u _ {n} \mid n\right) = \frac {1 + C _ {u _ {n} \mid n}}{N + C _ {\mathrm {t o t} \mid n}} \pm \sqrt {\frac {1 + C _ {u _ {n} \mid n} N + C _ {\mathrm {t o t} \mid n} - C _ {u _ {n} \mid n} - 1}{\left(N + C _ {\mathrm {t o t} \mid n}\right) ^ {2} N + C _ {\mathrm {t o t} \mid n} + 1}} \tag {2}
$$

where the standard deviation in the estimate is used for the error. Since the probabilities here each actually come from  $N$  different distributions, we estimate the total error in  $\mathcal{F}_C$  by adding these constituent errors in quadrature. Explicitly, we find  $\mathcal{F}_C = 0.996 \pm 0.001$  for the  $X$  gate,  $0.90 \pm 0.01$  for the CINC operation,  $0.92 \pm 0.01$  for the  $3 \times 3$  SUM gate, and  $\mathcal{F}_C = 0.9589 \pm 0.0005$  for the  $16 \times 16$  SUM gate. The reduction in  $\mathcal{F}_C$  for the two-qudit gates is due in large part to the fewer total counts in these cases, from our use of heralded single photons rather than a weak coherent state. As seen by the presence of  $N$  in the denominator of Eq. (2), even when  $C_{u_n|n} = C_{\mathrm{tot}|n}$ , the estimate  $p(u_n|n)$  is not unity unless  $C_{\mathrm{tot}|n} \gg N$ . In our experiments, the two-qudit tests have only  $\sim 100 - 300$  total counts per input computational basis state for the  $9 \times 9$  matrices (with  $N = 9$ ) and  $\sim 500 - 800$  counts per input state for the  $16 \times 16$  matrices (with  $N = 16$ ), thereby effectively bounding the maximum  $p(u_n|n)$  and, by extension, fidelity  $\mathcal{F}_C$ . This behavior is actually a strength of BME, though, as it ensures that we have a conservative estimate of the fidelity that is justified by the total amount of data acquired.[58]

While extremely useful for initial characterization, however, the computational-basis fidelity above provides no information on phase coherence. On the other hand, process tomography would offer a complete quantification of the quantum gate. Yet due to the challenging experimental complexity involved in quantum process tomography, here we choose a much simpler test which—while limited—nonetheless offers strong evidence for the coherence of our time-bin X gate. To begin with, note that all three-dimensional quantum processes can be expressed in terms of the nine Weyl operations<sup>60</sup>:

$$
U _ {0} = I = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right),
$$

$$
U _ {1} = X = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right),
$$

$$
U _ {2} = X ^ {2} = \left( \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{array} \right)
$$

$$
U _ {3} = Z = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & e ^ {\mathrm {i} \frac {2 \pi}{3}} & 0 \\ 0 & 0 & e ^ {- \mathrm {i} \frac {2 \pi}{3}} \end{array} \right),
$$

$$
U _ {4} = Z X = \left( \begin{array}{c c c} 0 & 0 & 1 \\ e ^ {\mathrm {i} \frac {2 \pi}{3}} & 0 & 0 \\ 0 & e ^ {- \mathrm {i} \frac {2 \pi}{3}} & 0 \end{array} \right), \tag {3}
$$

$$
U _ {5} = Z X ^ {2} = \left( \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & e ^ {\mathrm {i} \frac {2 \pi}{3}} \\ e ^ {- \mathrm {i} \frac {2 \pi}{3}} & 0 & 0 \end{array} \right)
$$

$$
U _ {6} = Z ^ {2} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & \mathrm {e} ^ {- \mathrm {j} \frac {2 \pi}{3}} & 0 \\ 0 & 0 & \mathrm {e} ^ {\mathrm {j} \frac {2 \pi}{3}} \end{array} \right),
$$

$$
U _ {7} = Z ^ {2} X = \left( \begin{array}{c c c} 0 & 0 & 1 \\ e ^ {- \mathrm {i} \frac {2 \pi}{3}} & 0 & 0 \\ 0 & e ^ {\mathrm {i} \frac {2 \pi}{3}} & 0 \end{array} \right),
$$

$$
U _ {8} = Z ^ {2} X ^ {2} = \left( \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & e ^ {- i \frac {2 \pi}{3}} \\ e ^ {i \frac {2 \pi}{3}} & 0 & 0 \end{array} \right)
$$

The quantum process itself is a completely positive map  $\mathcal{E},^{61}$  which for a given input density matrix  $\rho_{\mathrm{in}}$  outputs the state

$$
\rho_ {\text {o u t}} = \mathcal {E} \left(\rho_ {\text {i n}}\right) = \sum_ {m, n = 0} ^ {8} \chi_ {m n} \cup_ {m} \rho_ {\text {i n}} \cup_ {n} ^ {\dagger} \tag {4}
$$

The process matrix with elements  $\chi_{mn}$  uniquely describes the operation. The ideal three-bin X gate with process matrix  $\chi_{X}$  has only one nonzero value,  $[\chi_X]_{11} = 1$ . To compare to this ideal, we assume the actual operation consists of a perfect X gate plus depolarizing (white) noise.[18] In this case we have a total operation modeled as

$$
\rho_ {\text {o u t}} = \lambda U _ {1} \rho_ {\text {i n}} U _ {1} ^ {\dagger} + \frac {(1 - \lambda)}{3} \mathbb {I} _ {3} \tag {5}
$$

whose process matrix we take to be  $\chi_N = \lambda \chi_X + \frac{1 - \lambda}{9} \mathbb{I}_9$ , which can be calculated by using  $\mathbb{I}_3 = \frac{1}{3} \sum_{n=0}^{8} U_n \rho_{\mathrm{in}} \mathbf{U}_n^{\dagger}$ . If we then assume a pure input superposition state  $\rho_{\mathrm{in}} = |\psi_{\mathrm{in}}\rangle \langle \psi_{\mathrm{in}}|$ , where  $|\psi_{\mathrm{in}}\rangle \propto |0\rangle_t + e^{i\phi} |1\rangle_t + e^{2i\phi} |2\rangle_t$  and measure the projection onto the output  $|\psi_{\mathrm{out}}\rangle \propto |0\rangle_t + |1\rangle_t + |2\rangle_t$  (as in Fig. 2c),  $\lambda$  can be estimated from the interference visibility  $V$  as:

$$
\lambda = \frac {2 V}{3 - V} \tag {6}
$$

and the process fidelity is then given by:

$$
\mathcal {F} _ {\mathrm {P}} = \operatorname {T r} \left(\chi_ {X} \chi_ {N}\right) = \left[ \chi_ {N} \right] _ {1 1} = \frac {1 + 8 \lambda}{9} = \frac {1 + 5 V}{9 - 3 V} = 0. 9 2 \pm 0. 0 1 \tag {7}
$$

as discussed in the article.

To show the coherence of our SUM gate, we generate an input state in the signal photon which is in time-bin  $|0_{\mathrm{t}}\rangle$  and an equi-amplitude superposition in frequency  $|\psi \rangle_{\mathrm{in}} = \frac{1}{\sqrt{3}}\left(|0\rangle_{\mathrm{f}} + |1\rangle_{\mathrm{f}} + |2\rangle_{\mathrm{f}}\right)|0\rangle_{\mathrm{t}}$ . After passing

![](images/154e22c0abc87a2e62ab6723fbc867d9cffb7be315bc672790ac3e6762aa3aa4.jpg)

![](images/cb5bd6c0e7218a1102db81bb68f6573bcaa1cae0abe9e2e906ee8f2d7aa5dde1.jpg)

![](images/34a7a4cd2299816564b96c8eeb49b022d48f5122a33218a185819de03113bf01.jpg)  
Fig. 6 Measurement of a three-dimensional maximally nonseparable time-frequency state. a The experimental setup. SPDC spontaneous parametric down conversion, PS pulse shaper, IM intensity modulator, D and -D dispersion modules with  $+2\mathrm{ns.nm}^{-1}$  and  $-2\mathrm{ns.nm}^{-1}$ , respectively, PM phase modulator. The same time-bin and frequency-bin spacings (1.2 ns, 75 GHz) as the 16-dimensional SUM gate experiment are used for these measurements. We note that in this experiment, the IM was placed only on the signal photons' route to avoid its insertion loss on the idler photons. b Joint spectral intensity of the three-dimensional nonseparable state. The accidents were subtracted in this measurement, with a coincidence to accidents ratio of about 30. c Two-dimensional interference patterns showing the coherence between all three time-frequency modes of the state. The frequency-bin and time-bin phases are varied using PS1 and PM1, respectively. Both phases are swept together from 0 to  $\pi$ , for a total phase sweep from 0 to  $2\pi$ . The data are shown with accidents subtracted and coincidence to accidents ratio of about 1. Since projection of frequency bins 0 and 2 on an indistinguishable frequency bin undergoes more projection loss, the coincidences between modes 0 and 2 were measured in  $10\mathrm{min}$

![](images/e99ee40a122994f6a966f476e00bbdcc7c21cbdb6e6aa8ae0c1ae97c25a72002.jpg)

![](images/42f1097c389d463cc5ea40d82940fabc1f2fe9600a0630635cf72457391b3dc8.jpg)

this state through the SUM gate, the time-bin state of the photon is shifted based on the frequency, leaving us with a maximally non-separable state  $|\psi \rangle_{\mathrm{out}} = \frac{1}{\sqrt{3}}\left(|00\rangle_{\mathrm{ft}} + |11\rangle_{\mathrm{ft}} + |22\rangle_{\mathrm{ft}}\right)$ . We note that since we are starting with time-bin zero, the time bins will not fall out of the computational space; therefore, the interferometric structure is not needed for the SUM gate and a dispersion module alone can do the operation. This saves us the extra insertion loss of the interferometer, which is an important parameter due to the low photon pair rate on the detectors in this particular experiment. To measure the three-dimensional nonseparability in  $|\psi_{\mathrm{out}}\rangle$ , we must vary the phases of different signal frequency bins and time bins with a pulse shaper and phase modulator, respectively. To observe the effect of this phase sweep with our relatively slow single-photon detectors (with ~100 ps jitter), an indistinguishable projection of all three time bins and frequency bins should be created. In general, the time bins can be projected on an indistinguishable state by using a cascade of interferometers, as illustrated in Fig. 2a. However, in our specific experiment, it is simpler to use a dispersion module with opposite dispersion to that of the module used in the SUM gate to perform the same projection. The frequency bins are then projected on an indistinguishable state using a phase modulator and pulse shaper to mix the frequencies (Fig. 6a)—a technique used previously in ref. [26]. We note that our measurements on the signal photons are conditioned on heralding by idler frequency superposition states. To measure the interference between different signal frequency bins, the idler photons too have to be projected on an indistinguishable frequency bin using a phase modulator and pulse shaper (Fig. 6a). This projection guarantees that detection of an idler photon does not give us any information on the frequency of the signal photon. Here the phases of the idler frequency bins are held constant; only the phases of the signal frequency and time bins are varied. This is in contrast to experiments in ref. [26], where the phases of both signal and idler frequency bins were varied.

In our experiment, three-dimensional interference measurements were not possible since mixing all three frequencies together adds extra projection loss, which we cannot afford. Therefore, we vary the phases of different time bins and frequency bins to measure two-dimensional interference patterns between all three time bins and frequency bins

(Fig. 6c). Using the visibilities of these interference patterns along with a joint spectral intensity (JSI) measurement (Fig. 6b) can give us a lower bound on the amount of nonseparability present in our system by measuring entanglement of formation.[35,36] The JSI denotes the correlations between the time bins and frequency bins of a signal photon heralded by an idler photon in its computational basis. This measurement was done using the same experimental setup used in Fig. 6a, without the equipment used for sweeping the phase of different signal time bins and projection measurements. For this measurement, the idler photons were detected after PS1, and the signal photons were detected right after the SUM gate.

Having the JSI measurement and the two-dimensional interference visibilities in hand, we have all the data needed to calculate the entanglement of formation with the assumption of having only white noise in our system, which can be expressed as:

$$
E _ {\text {o f}} \geq - \log_ {2} \left(1 - \frac {B ^ {2}}{2}\right) \tag {8}
$$

where

$$
B = \frac {2}{\sqrt {| C |}} \left(\sum_ {\substack {(j, k) \in C \\ j <   k}} | \langle j, j | \rho | k, k \rangle | - \sqrt {\langle j , k | \rho | j , k \rangle \langle k , j | \rho | k , j \rangle}\right) \tag{9}
$$

Here,  $C$  is the number of indices  $(j,k)$  used in the sum. This measurement is useful when we do not have access to all the elements of the density matrix.  $\langle j,j|\rho |k,k\rangle$ $(j\neq k)$  elements indicate the coherence between modes  $j$  and  $k$ , and can be lower-bounded using the two-dimensional visibilities. The terms  $\langle j,k|\rho |j,k\rangle$  can be calculated using the elements of the JSI. Using these values, we measure  $E_{\mathrm{of}}\geq 1.19\pm 0.12$  ebits, which indicates greater than two-dimensional nonseparability in our two-party system, more than one standard deviation away from the threshold.

To generate the 32-dimensional four-party GHZ state, the signal and idler go through the same dispersion module  $(-2\mathrm{ns.nm}^{-1})$ . After

dispersion, the signal frequency bins farther away from the center of the spectrum are delayed more, but the idler frequency bins are delayed less as we move farther away from the center. In order to write the GHZ state in the form  $|\psi \rangle_{\mathrm{out}} = \frac{1}{\sqrt{32}}\sum_{m=0}^{31}|m,m,m,m\rangle_{\mathrm{f}_s,\mathrm{t}_i,\mathrm{f}_i,\mathrm{t}_i}$ , we label the signal time bins after dispersion 0 to 31 starting from earlier time bins (time bin 0 the earliest, time bin 31 the latest), while on the idlers, we label the time bins such that the earliest time bin is 31 and the latest time bin is 0. Another choice would be to send signal and idler through separate modules with equal but opposite dispersion, in which case we would use identical time labeling. To measure the state illustrated in Fig. 5, we individually measured coincidences for the 32 different settings of both signal and idler frequency bins (32 × 32 measurements). For each of these measurements, we used our event timer to assign signal and idler time bins for each coincidence, which results in a 32 × 32 submatrix for each signal-idler frequency setting. Therefore, we have 32<sup>4</sup> measurements in total. Two of the 32 × 32 time-bin submatrices are shown in Fig. 5b, c.

We use bulk switches, dispersion modules, pulse shapers, and phase modulators in out experiments, which have high insertion loss (switch: 3 dB, dispersion module: 3 dB, pulse shaper: 5 dB, phase modulator: 3 dB). Therefore, we use very bright entangled photons at the input in order to have reasonable coincidence counts on our detectors in our acquisition time. Using bright biphotons gives rise to multi-pair generation which leads to the relatively high accidental rate here.

# DATA AVAILABILITY

The data and analysis codes used in this study are available from the corresponding author on request.

# ACKNOWLEDGEMENTS

This work was funded in part by the National Science Foundation under award number 1839191-ECCS. We thank B.P. Williams for discussions on Bayesian estimation. We thank M. Hosseini, N. Lingaraju, and Nathan O'Malley for discussions. J.M.L. acknowledges support from a Wigner Fellowship at ORNL. A portion of this work was performed at Oak Ridge National Laboratory, operated by UT-Battelle for the U.S. Department of Energy under Contract No. DEAC05-00OR2275.

# AUTHOR CONTRIBUTIONS

P.I. initiated and developed the idea. P.I., J.A.J. and M.S.A. performed the experiments with help from D.E.L. P.I., J.A.J., J.M.L., M.S.A., O.D.O. and A.M.W. performed the theoretical work and analyzed the results. P.I. and A.J.M. analyzed the data to quantify the nonseparability in the system. M.Q. supervised the fabrication of the microring resonator. P.I., J.A.J., J.M.L., M.S.A., O.D.O. and A.M.W. prepared the manuscript. A.M.W. managed and supervised the project.

# ADDITIONAL INFORMATION

Competing interests: The authors declare no competing interests.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

# REFERENCES

1. Shor, P. W. Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. SIAM Review 41, 303-332 (1999).  
2. Kimble, H. J. The quantum internet. Nature 453, 1023-1030 (2008).  
3. Knill, E., Laflamme, R. & Milburn, G. J. A scheme for efficient quantum computation with linear optics. Nature 409, 46-52 (2001).  
4. Crespi, A. et al. Integrated photonic quantum gates for polarization qubits. Nat. Commun. 2, 566 (2011).  
5. Babazadeh, A. et al. High-dimensional single-photon quantum gates: concepts and experiments. Phys. Rev. Lett. 119, 180510 (2017).  
6. Humphreys, P. C. et al. Linear optical quantum computing in a single spatial mode. Phys. Rev. Lett. 111, 150501 (2013).  
7. Lu, H.-H. et al. Electro-optic frequency beam splitters and tritters for high-fidelity photonic quantum information processing. Phys. Rev. Lett. 120, 030502 (2018).  
8. Lu, H.-H. et al. A controlled-NOT gate for frequency-bin qubits. npj Quantum Information 5, 24 (2019).

9. Fiorentino, M. & Wong, F. Deterministic controlled-NOT gate for single-photon two-qubit quantum logic. Phys. Rev. Lett. 93, 070502 (2004).  
10. Kagalwala, K. H., Di Giuseppe, G., Abouraddy, A. F. & Saleh, B. E. A. Single-photon three-qubit quantum logic using spatial light modulators. Nat. Commun. 8, 739 (2017).  
11. Fang, W.-T. et al. On-chip generation of time-and wavelength-division multiplexed multiple time-bin entanglement. Opt. Express 26, 12912-12921 (2018).  
12. Humphreys, P. C. et al. Continuous-variable quantum computing in optical time-frequency modes using quantum memories. Phys. Rev. Lett. 113, 130502 (2014).  
13. Marin-Palomo, P. et al. Microresonator-based solitons for massively parallel coherent optical communications. Nature 546, 274-279 (2017).  
14. Cerf, N. J., Adami, C. & Kwiat, P. G. Optical simulation of quantum logic. Phys. Rev. A 57, R1477 (1998).  
15. Roa, L., Delgado, A. & Fuentes-Guridi, I. Optimal conclusive teleportation of quantum states. Phys. Rev. A 68, 022310 (2003).  
16. Boschi, D., Branca, S., De Martini, F., Hardy, L. & Popescu, S. Experimental realization of teleporting an unknown pure quantum state via dual classical and einstein-podolsky-rosen channels. Phys. Rev. Lett. 80, 1121 (1998).  
17. Sheng, Y.-B., Deng, F.-G. & Long, G. L. Complete hyperentangled-Bell-state analysis for quantum communication. Phys. Rev. A 82, 032318 (2010).  
18. Wilde, M. M. Quantum information theory. (Cambridge University Press, Cambridge, UK, 2013).  
19. Wootters, W. K. & Fields, B. D. Optimal state-determination by mutually unbiased measurements. Ann. Phys. 191, 363-381 (1989).  
20. Lukens, J. M., Islam, N. T., Lim, C. C. W. & Gauthier, D. J. Reconfigurable generation and measurement of mutually unbiased bases for time-bin quids. Appl. Phys. Lett. 112, 111102 (2018).  
21. Sheridan, L. & Scarani, V. Security proof for quantum key distribution using qudit systems. Phys. Rev. A 82, 030301 (2010).  
22. Islam, N. T., Lim, C. C. W., Cahall, C., Kim, J. & Gauthier, D. J. Provably secure and high-rate quantum key distribution with time-bin quids. Sci. Adv. 3, e1701491 (2017).  
23. Jaramillo-Villegas, J. A. et al. Persistent energy-time entanglement covering multiple resonances of an on-chip biphoton frequency comb. Optica 4, 655-658 (2017).  
24. Reimer, C. et al. Generation of multiphoton entangled quantum states by means of integrated frequency combs. Science 351, 1176-1180 (2016).  
25. Kues, M. et al. On-chip generation of high-dimensional entangled quantum states and their coherent control. Nature 546, 622-626 (2017).  
26. Imany, P. et al. 50-GHz-spaced comb of high-dimensional frequency-bin entangled photons from an on-chip silicon nitride microresonator. Opt. Express 26, 1825-1840 (2018).  
27. Brennen, G. K., Bullock, S. S. & O'Leary, D. P. Efficient circuits for exact-universal computations with quids. Quantum Info Comput. 6, 436-454 (2005).  
28. Wang, X., Sanders, B. C. & Berry, D. W. Entangling power and operator entanglement in qudit systems. Phys. Rev. A 67, 042323 (2003).  
29. Draper, T. G., Kutin, S. A., Rains, E. M. & Svore, K. M. A logarithmic-depth quantum carry-lookahead adder. Quantum Info Comput. 6, 351–369 (2006).  
30. Imany, P., Odele, O. D., Jaramillo-Villegas, J. A., Leaird, D. E. & Weiner, A. M. Characterization of coherent quantum frequency combs using electro-optic phase modulation. Phys. Rev. A 97, 013813 (2018).  
31. Li, L., Yi, X., Huang, T. X. H. & Minasian, R. A. Microwave photonic filter based on dispersion controlled spectrum slicing technique. *Electron. Lett.* **47**, 511 (2011).  
32. Li, L., Yi, X., Huang, T. X. H. & Minasian, R. A. Distortion-free spectrum sliced microwave photonic signal processor: analysis, design and implementation. Opt. Express 20, 11517-11528 (2012).  
33. Reimer, C. et al. High-dimensional one-way quantum processing implemented on d-level cluster states. Nat. Phys. 15, 148 (2019).  
34. Karimi, E. & Boyd, R. W. Classical entanglement? Science 350, 1172-1173 (2015).  
35. Martin, A. et al. Quantifying Photonic High-Dimensional Entanglement. Phys. Rev. Lett. 118, 110501 (2017).  
36. Tiranov, A. et al. Quantification of multidimensional entanglement stored in a crystal. Phys. Rev. A 96, 040303 (2017).  
37. Hu, X.-M. et al. Experimental multi-level quantum teleportation. arXiv preprint arXiv:1904.12249 (2019).  
38. Luo, Y.-H. et al. Quantum teleportation in high dimensions. arXiv preprint arXiv:1906.09697 (2019).  
39. Barreiro, J. T., Wei, T. C. & Kwiat, P. G. Beating the channel capacity limit for linear photonic superdense coding. Nat. Phys. 4, 282 (2008).  
40. Erhard, M., Malik, M., Krenn, M. & Zeilinger, A. Experimental Greenberger-Horne-Zeilinger entanglement beyond qubits. Nat. Photonics 12, 759-764 (2018).  
41. Pan, J. W., Bouwmeester, D., Daniell, M., Weinfurter, H. & Zellinger, A. Experimental test of quantum nonlocality in three-photon Greenberger-Horne-Zeilinger entanglement. Nature 403, 515-519 (2000).

42. Wang, X.-L. et al. 18-Qubit entanglement with six photons' three degrees of freedom. Phys. Rev. Lett. 120, 260502 (2018).  
43. Hillary, M., Bužek, V. & Berthiaume, A. Quantum secret sharing. Phys. Rev. A 59, 1829 (1999).  
44. Zhao, Z. et al. Experimental demonstration of five-photon entanglement and open-destination teleportation. Nature 430, 54-58 (2004).  
45. Pant, M., Towsley, D., Englund, D. & Guha, S. Percolation thresholds for photonic quantum computing. Nat. Commun. 10, 1070 (2019).  
46. Wang, J. et al. Reconfigurable radio-frequency arbitrary waveforms synthesized in a silicon photonic chip. Nat. Commun. 6, 5957 (2015).  
47. Wang, C. et al. Integrated lithium niobate electro-optic modulators operating at CMOS-compatible voltages. Nature 562, 101-104 (2018).  
48. Wang, C. et al. Monolithic lithium niobate photonic circuits for Kerr frequency comb generation and modulation. Nat. Commun. 10, 978 (2019).  
49. Wang, J. et al. Multidimensional quantum entanglement with large-scale integrated optics. Science 360, 285-291 (2018).  
50. Ikuta, T. & Takesue, H. Four-dimensional entanglement distribution over  $100\mathrm{km}$ . Sci. Rep. 8, 817 (2018).  
51. Malik, M. et al. Multi-photon entanglement in high dimensions. Nat. Photonics 10, 248-252 (2016).  
52. Erhard, M., Fickler, R., Krenn, M. & Zeilinger, A. Twisted photons: new quantum perspectives in high dimensions. Light Sci. Appl. 7, 17146 (2018).  
53. Bouwmeester, D. et al. Experimental quantum teleportation. Nature 390, 575-579 (1997).  
54. Lu, H.-H. et al. Simulations of subatomic many-body physics on a quantum frequency processor. arXiv Preprint arXiv:1810.03959 (2018).  
55. Sparrow, C. et al. Simulating the vibrational quantum dynamics of molecules using photonics. Nature 557, 660-667 (2018).  
56. Bernien, H. et al. Probing many-body dynamics on a 51-atom quantum simulator. Nature 551, 579-584 (2017).

57. De Greve, K. et al. Complete tomography of a high-fidelity solid-state entangled spin-photon qubit pair. Nat. Commun. 4, 2228 (2013).  
58. Blume-Kohout, R. Optimal, reliable estimation of quantum states. New J. Phys. 12, 043034 (2010).  
59. Williams, B. P. & Lougovski, P. Quantum state estimation when qubits are lost: a no-data-left-behind approach. New J. Phys. 19, 043003 (2017).  
60. Bertlmann, R. A. & Krammer, P. Bloch vectors for quuds. J. Phys. A Math. Theor. 41, 235303 (2008).  
61. O'Brien, J. L. et al. Quantum process tomography of a controlled-NOT gate. Phys. Rev. Lett. 93, 80502 (2004).  
62. Thew, R. T., Acin, A., Zbinden, H. & Gisin, N. Bell-type test of energy-time entangled qutrits. Phys. Rev. Lett. 93, 010503 (2004).

![](images/5d4807e3739471c7d6201d017a045b7d0a3ec1a3cea4b005b8a1050f8a331951.jpg)

Open Access This article is licensed under a Creative Commons

Attribution 4.0 International License, which permits use, sharing,

adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2019