# Hybrid discrete- and continuous-variable quantum information

Ulrik L. Andersen $^{1\star}$ , Jonas S. Neergaard-Nielsen $^{1}$ , Peter van Loock $^{2}$  and Akira Furusawa $^{3}$

Research in quantum information processing has followed two different directions: the use of discrete variables (qubits) and that of high-dimensional, continuous-variable Gaussian states (coherent and squeezed states). Recently, these two approaches have been converging in potentially more powerful hybrid protocols.

By harnessing quantum superposition and entanglement, it is possible to design new, and potentially more powerful, types of communication and computation. But despite the significant experimental progress in controlling the quantum states of various microscopic systems, the implementation of a fully fault-tolerant and scalable quantum computer is still a major challenge.

Many physical platforms, including photons, ions, atoms, solid state and superconducting devices, and nuclear magnetic resonance $^{1}$ , are being explored with the view of constructing a quantum computer. But, irrespective of the physical implementation, quantum information processing (QIP) comes in two different types, depending on the degree of freedom, or observable, used to encode information. If the observable is discrete in nature (that is, its eigenvalues are discretized), we talk about discrete-variable (DV) QIP (ref. 2), (see Box 1). And if the observable has a continuum of eigenvalues, we refer to continuous-variable (CV) QIP (refs 3-5) (see Box 2). This is in a way similar to classical information processing, where the two types of encoding are known as digital and analog information processing.

Recently, progress has been made towards bridging the two approaches, with the aim of realizing protocols that overcome the intrinsic individual limitations. The integration of DV and CV technologies in unified hybrid systems (by which we mean the simultaneous use of discrete and continuous variables as opposed to hybrid physical systems) has advanced both theoretically and experimentally, and the aim of this Progress Article is to highlight some of these results.

# Generation of non-Gaussian states

A prerequisite for universal QIP is the generation of a restricted set of quantum states. Some systems possess only a DV description of their quantum state—for instance, the case for the spin of a single particle. However, for most systems, including the broad category of harmonic oscillators, a CV description exists. Among them there are two classes of pure quantum states that play a pivotal role in QIP: Gaussian and non-Gaussian states, referring to the statistics of the state's wavefunction or Wigner function. Gaussian states are relatively easy to produce and manipulate using standard optical technology such as lasers, parametric amplifiers (or squeezers), beam splitters and homodyne detectors. This enables linear transformations of continuous quantum quadratures, thereby mapping Gaussian states onto other Gaussian states.

In recent years, this technology has been extended to the microwave regime. Using superconducting degenerate and nondegenerate parametric amplifiers, microwave squeezed and CV entangled states have been generated and characterized with homodyne detection for state tomography. In addition to the generation of squeezing of the field quadratures, demonstrations of the squeezing of the CV collective spin observables of an atomic ensemble have been reported, and similar proposals exist for solid state materials[9,10]. In the past decade, there has been significant interest in the generation and manipulation of the position and momentum CV states of mechanical oscillators. This has led to numerous proposals and a single experiment on generating mechanically squeezed and entangled states by exploiting the Gaussian coupling between a field mode and the mechanics[11,12].

To produce a pure non-Gaussian state or, in general, an arbitrary quantum state, the standard CV toolbox consisting of linear Gaussian transformation and homodyne detection is insufficient. It is, however, possible to enter the non-Gaussian regime by hybridizing DV and CV technologies. There are basically two approaches to the formation of non-Gaussian states of an oscillator: by enabling a strong, deterministic coupling to a finite-level (discretized) matter system or by a probabilistic measurement-induced interaction using a finite-level discretized energy detector (photon counter).

Deterministic generation of non-Gaussian states. The interaction between a CV oscillator and a DV two-level system can be described by the Jaynes-Cummings interaction. The simplest non-Gaussian state produced by this interaction is the single-photon state; each time the two-level system is excited, it will decay and emit a single flying photon into a travelling field mode. If a single field mode is strongly coupled to the two-level system—usually enabled by placing the systems inside a high-  $Q$  cavity—the photon will be harvested by that mode with high probability. This has been demonstrated in a number of experiments<sup>13</sup>, but a complete state characterization by means of Wigner function reconstruction has been realized only in a few experiments, mainly in the microwave regime<sup>14-16</sup>, but recently also in the optical regime with atomic ensembles<sup>17</sup>.

In the microwave domain, extremely high coupling strength can be reached using a superconducting phase qubit near a microstrip cavity. Furthermore, the coupling can be controlled by detuning the cavity in and out of resonance with the field<sup>18</sup>. Using

# Box 1 | Discrete variables.

Binary digits of information can be represented by orthogonal eigenstates of observables of a single quantum system such as the polarization of a photon (a), the spin of an electron (b), or the current of a superconducting loop (c). In QIP, one can also use superpositions of eigenstates:

$$
| \psi \rangle = c _ {0} | 0 \rangle + c _ {1} | 1 \rangle
$$

The information encoded in this quantum state (qubit) is given by the complex amplitudes  $c_{0}$  and  $c_{1}$ , and it can be represented and visualized on the Bloch sphere (d). The computational basis set  $\{|0\rangle, |1\rangle\}$  is discrete. A projective measurement is described by a two-component projector such that in each measurement the number of outcomes (eigenvalues) is two. Physically, such measurements are realized, for example, by a Stokes parameter (polarization) measurement (e) or a Stern-Gerlach apparatus, both of which ideally project along any orthogonal basis. A universal two-component projector can be used to implement a measurement-induced nonlinearity and fully characterize a state in the two-dimensional Hilbert space.

Universal quantum computation requires the implementation of a finite set of gates comprising single-qubit and two-qubit operations. One example of a complete set is  $\{\hat{U}_{\mathrm{H}},\hat{U}_{\mathrm{PG}},\hat{U}_{\mathrm{CNOT}}\}$

where  $\hat{U}_{\mathrm{H}}$  and  $\hat{U}_{\mathrm{PG}}$  are the single-qubit Hadamard and rotation gates, respectively, and  $\hat{U}_{\mathrm{CNOT}}$  is the two-qubit-controlled NOT gate. For some physical systems, these gates are relatively simple to implement. For others, such as optics, the two-qubit gate is particularly challenging.

![](images/76c530aa7b4227feccc655a58d681dd6cbae61ff8e6dcadda1189138d0f97e3c.jpg)

![](images/5855dc6af924911e07ae798c1f9a294b1176f45d61e0d50f7fd741463b01dd42.jpg)  
d Qubit Bloch sphere

![](images/d47433108a9c3bf4e90a786f68143c360cfb462562f4d3b2b333460280f9132e.jpg)  
a Photon polarization  
b Electron spin  
e Stokes parameter detection

![](images/05cc89c63b7aabc2a861afa7a4068cbe108e079a85ca5cc85f767da30567051e.jpg)  
c Loop current

![](images/670f7746f2524f011faf433889dc5e6d547f72fce84a0ff626ed93fda7f6152a.jpg)

such a strong and controlled coupling, higher-order Fock states $^{19}$ , as well as Fock state superpositions of several photons $^{20}$ , have been deterministically generated and characterized by quantum state tomography on a chip in a cryogenic environment. Similar multi-photon Fock states have been generated through quantum non-demoliation measurement of a stationary microwave field by employing the strong coupling and subsequent measurements of flying Rydberg atoms $^{14}$  (Fig. 1a).

Another non-Gaussian state of the harmonic oscillator is the so-called Schrödinger cat state, which is defined as superpositions of coherent states with opposite phase,  $|\alpha \rangle \pm |\neg \alpha \rangle$  (ref. 21), where  $\alpha$  is the coherent-state amplitude. Such states have been deterministically realized in the motional state of a trapped ion through the application of a sequence of Raman laser pulses and the interaction with its spin degree of freedom[22]. Cat states have also been generated by entangling a standing CV microwave field with a flying Rydberg atom, followed by a projective DV measurement of the atom[14,23], and through a strong, dispersive interaction with a superconducting transmon qubit[24]. In the latter experiment, impressive cat sizes of up to 111 photons were created, and the complexity was further enhanced by producing three- and four-component cat states (Fig. 1b).

In addition to the coupling of two-level systems to the CVs of the electromagnetic field and the vibrational mode of ions, recently there has also been significant progress in understanding and implementing the coupling of a two-level system to the continuous position and momentum variables of a solid mechanical oscillator. In a pioneering experiment it was shown that by strongly coupling a superconducting phase qubit to a ground-state-cooled mechanical oscillator, it was possible to coherently read out the state of the oscillator and, furthermore, to generate a single excitation (single-phonon Fock state) of the oscillator[25] (Fig. 1c). Various other approaches enabling a strong coupling of a two-level system (for example, a quantum dot[26], a nitrogen-vacancy centre in diamond[27], an atom[28] and a two-level defect[29]) to a mechanical oscillator have been proposed, and some recent preliminary steps have been realized[30,31]. These schemes promise the creation of arbitrary

superposition states, including the cat state, which in principle can be mapped onto the electromagnetic field $^{32}$ . This might well be the future route to deterministic generation of non-Gaussian states for QIP.

Probabilistic generation of non-Gaussian states. Even without a deterministic coupling to a discrete level system, it is possible to probabilistically do intricate modifications at the individual quantum level of the state of a harmonic oscillator. Such transformations, which are in general non-Gaussian, can be implemented through projective measurements of a discrete spectrum operator. This approach is very common—particularly in the optical domain, where low-noise single-photon detectors are readily available.

Negative Wigner functions of an optical field mode were first observed for a single photon conditionally prepared by the detection of its twin from a photon pair created in a spontaneous parametric down-conversion (SPDC) process in a nonlinear crystal[33]. The same method was used to implement the addition of a photon to a coherent state that was seeded into one mode of the SPDC (ref. 34). The reverse of this photon-addition process, photon subtraction, can be easily implemented by detection of a photon after a weakly reflecting beamsplitter, as was demonstrated in several experiments where the subtraction was applied to an initial squeezed vacuum state[35-38]. Interest in this particular state arose from the recognition[39] that such states are close-to-ideal approximations to Schrödinger cat states with small amplitudes  $\alpha$ , also known as kitten states.

The range of possible conditional operations can be expanded by detecting additional photons (with either multiple or photon-number-resolving detectors) as shown for higher-number Fock states $^{40,41}$  and kitten states $^{42-44}$ . It can be expanded even further by preceding the photon detection by a phase-space displacement. This changes the simple Fock state projection into a projection consisting of a superposition of multiple photon number components whose coefficients are controlled by the amplitude and phase of the displacement (Fig. 1d). Applications include generation of arbitrary superpositions of vacuum and a single $^{45-47}$  or multiple photons $^{48,49}$  and kitten-state

# Box 2 | Continuous variables.

As an alternative to the standard finite-level encoding, one can use the eigenstates  $\{|x\rangle\}$  of a continuous-valued operator  $\hat{x}$ . This operator—and its conjugate,  $\hat{p}$ —could be represented by the amplitude and phase quadratures of a field mode (a), the collective spin variables of an atomic ensemble (b) or the position and momentum of a mechanical oscillator (c). An arbitrary quantum state in this basis is

$$
| \psi \rangle = \int_ {- \infty} ^ {\infty} \psi (x) | x \rangle d x
$$

where the information is now encoded in the complex wavefunction  $\psi (x)$  or, more generally, in a quasi-distribution over phase space known as the Wigner function  $W(x,p)$  (d). Traditional CV QIP uses Gaussian states such as coherent, squeezed and Einstein-Podolsky-Rosen entangled states (also known as two-mode squeezed states)—these have Gaussian wavefunctions and Wigner functions.

A measurement of the basis states is done with a continuous projector, which for optical and microwave fields can be implemented with a homodyne detector (e) and for an atomic ensemble by the Faraday polarization rotation of light, which is proportional to the collective spin. With a set of such measurements, it is possible to perform a complete tomography of any quantum state.

One universal set of gates for CV computation is  $\{\hat{U}_{\mathrm{F}},\hat{U}_{\mathrm{Z}},\hat{U}_{\mathrm{PG}},$ $\hat{U}_{\mathrm{SUM}}\}$  , with the single-mode Gaussian gates  $\hat{U}_{\mathrm{F}}$  (Fourier

transform) and  $\hat{U}_{\mathrm{Z}}$  (displacement), the single-mode non-Gaussian cubic phase gate  $\hat{U}_{\mathrm{PG}}$ , and the two-mode Gaussian SUM gate  $\hat{U}_{\mathrm{SUM}}$ . Whereas the Gaussian transformations are typically easy to implement in a CV system, universality is attained only by including the technically challenging non-Gaussian transformations.

![](images/b53ea5b57bdf28d64288b51a5881be679c680c731a8b0c6a0cd31ade52ded576.jpg)  
a EM field

![](images/8032b68c7470f2d17af4e94815e0cffd2105ed87f20287b0947fde8fb45b1847.jpg)  
b Spin ensemble

![](images/30124b9f0973e7832790dd34d23d4ba2321346a773af13d21f4da7f31d5b13f7.jpg)  
C Mechanical oscillator

![](images/a8c3573e6cd7c98c9c97555a99b3fa4cbd2bdaa6b864a94418be37077078b99c.jpg)  
d Wigner function

![](images/16c36df36f15f4518b1ea5ef084182829ee0982d7e23bc36c61f6720f5bde6a3.jpg)  
e Homodyne detector

superpositions $^{50}$ . Complex quantum states can alternatively be created by a different probabilistic hybrid technique, namely conditional homodyne detection on already prepared non-Gaussian states $^{51,52}$  (Fig. 1e).

The applications of these operations are not limited to single-mode light fields. By using phase-space displacement or non-local photon subtraction or addition on various initial two-mode states, different kinds of entangled, non-Gaussian states—such as non-local kittens $^{53}$  and hybrid CV/DV entangled states $^{54-56}$ —have also been generated.

Finally, projective photon number measurements can also induce non-Gaussian states of CV material systems when applied to scattered light. This has been proposed for massive mechanical oscillators[57,58] and experimentally demonstrated for atomic spin ensembles[59,60], even with negative Wigner functions[61] (Fig. 1f). Many of the techniques outlined above that have been developed for purely optical implementations could equivalently be applied to prepare highly interesting states of material systems.

# Hybrid protocols

Let us discuss a few examples of ways in which QIP could make use of these hybrid techniques. Applications include fundamental tasks such as quantum teleportation, entanglement distillation, error correction or testing Bell inequalities. Ultimately, these techniques could enable the realization of scalable quantum communication and universal, fault-tolerant quantum computation.

Hybrid quantum teleportation. The elementary quantum communication protocol is quantum teleportation $^{62}$ —the transfer of arbitrary quantum states using shared entanglement and classical communication; and the most obvious hybrid approach to quantum teleportation is CV quantum teleportation $^{63}$  of DV states or DV quantum teleportation of CV states. In the optical domain, the former can be, in principle, straightforwardly applied on any quantum states, including single-photon-based qubits. This teleporter possesses the great advantage of being deterministic while using solely linear components. However, the price to pay

is the intrinsically limited performance: perfectly faithful and deterministic teleportation of an arbitrary state can be attained only in the limit of an unphysical, infinite degree of Gaussian entanglement. Deterministic CV teleportation of DV states has recently been demonstrated on photonic qubits $^{64}$ , and also for a cat state $^{65}$ .

The converse quantum teleporter, using DV entanglement and DV operations to transfer a CV state, requires breaking up a high-dimensional CV state into states of smaller dimension and performing correspondingly many individual DV teleportations $^{66}$ . In contrast to the standard CV teleporter, the optical DV teleporter can reach fidelities of  $100\%$ . However, its efficiency is fundamentally limited by the probabilistic nature of qubit Bell measurements with linear transformations $^{67}$ . Only by the use of nonlinear, non-Gaussian transformations or additional non-Gaussian ancillary states can the teleporter become (near-)deterministic. However, we note that the efficiency of the Bell measurement can also be made more efficient using—once again—a hybrid approach where the states undergo a CV squeezing transformation before DV photon counting measurements $^{68}$ .

Quantum teleportation nicely illustrates what an optical hybrid approach does: it can exchange an otherwise probabilistic, linear-optical qubit teleporter with a fully deterministic device, possibly at the expense of the transfer fidelity; and it can make use of a potentially high-fidelity transfer of a CV state, at the expense of a non-unit success probability. This new level of versatility is, of course, even greater when matter systems are included, as the light-matter interactions offer an alternative way of performing efficient Bell measurements. In fact, using atomic ensembles or two-level emitters, such hybrid light-matter teleportations have already been proposed for long-distance quantum communication[69] and, on a small scale, experimentally demonstrated[70,71].

Hybrid entanglement distillation. For quantum communication based on the distribution of entangled states, such as in a quantum repeater, it is desirable to initially prepare and distribute optical entanglement with high efficiency. Since the CV Gaussian

![](images/a45f450962bbeca9ace161f904973a2ca892960f0939db92a2038e604fe00bc3.jpg)

![](images/db0ab3916d3c0bb66d86edfe649a3a9f590f45cacd58e27e4a21ea9f7876ec66.jpg)

![](images/3754a0cf7bf0bd0276120dde3393696816bde734929766bf035282a392e7c72d.jpg)

![](images/7cf58189275e3f4e70eac7c36d4247e808659535a696975bd66eb0716c91b07f.jpg)

![](images/9f5b53d396215fa9f5ba7cea9f3179ee9b33fdc81c1f4a4471bdb381daa2752a.jpg)

![](images/1b9aff04c8961067876b9cfe36124d0cc34978894e507c1b71e1460519bf277e.jpg)

![](images/12567a25d04ef7736985fe967ea044f04550f9df607943336aa7f21ea2b3ed6c.jpg)  
Figure 1 | Examples of non-Gaussian state generation in various systems. a, Schrödinger cat and Fock states of a microwave cavity field induced by the detection of dispersively coupled Rydberg atoms $^{14}$ . b, Three- and four-component cat states of a microwave cavity field coupled to a superconducting transmon qubit $^{24}$ . c, Population exchange of a single excitation between a superconducting phase qubit and a piezoelectric mechanical oscillator cooled to its ground state $^{25}$ . d, Arbitrary Fock state superpositions of an optical mode through spontaneous parametric down-conversion and coherent-state injected photon detectors $^{48}$ . e, Squeezed Schrödinger cat state of an optical mode induced by conditional homodyne detection on a two-photon Fock state $^{52}$ . f, Single excitation of the collective spin state of 3,000 atoms heralded by detection of a single photon that has interacted with the atomic ensemble $^{61}$ . Figure reproduced from: a, ref. 14; c, ref. 25; d, ref. 48; e, ref. 52; f, ref. 61, all Nature Publishing Group. Panel b reproduced from ref. 24, AAAS.

![](images/ff89804d26c466f0302bdd816b07f20e2eadb01c3a226fe4e48166a257838422.jpg)

![](images/9fa25b98c68e5a34b9a15ee8429e26050cc8a6bc70ec2d9beec4e86a09487190.jpg)

entangled states can be produced in an unconditional fashion, they may serve as a deterministic source of shared entanglement. However, Gaussian entanglement is very sensitive to photon losses; hence, entanglement distillation will be absolutely necessary. Solely using CV Gaussian operations does not allow the distillation of high-quality Gaussian entanglement from low-quality, noisy Gaussian entanglement $^{72-74}$ , but by introducing local non-Gaussian elements, such as photon subtraction (by photon counting), the entanglement of the state can be effectively enhanced $^{75-78}$  and the process can be further improved using squeezing, displacements and atomic memories $^{79-82}$ . Another prominent method for CV entanglement distillation and error correction is the heralded, noiseless linear amplifier (NLA; refs 83,84), which has been realized in different settings $^{85-88}$ .

All these methods involve the distillation of CV Gaussian entanglement using DV measurements. The reverse scenario—detecting errors of DV states using CV homodyne measurements—has been proposed in the case of cat state purification $^{89,90}$  and distillation of lossy DV Bell states $^{91}$ . The latter scheme is effectively implementing the NLA by means of homodyne measurements

and classical data filtering. Moreover, homodyne detection can also facilitate the production of DV entanglement between a pair of atoms; exploiting a dispersive Jaynes-Cummings type of interaction, a bright coherent state can get entangled with two atoms at two different locations, which in turn can be measured with a homodyne detector to herald an atom-atom entangled state at a distance with a relatively high rate $^{92}$ . An alternative approach to the formation of atom-atom entanglement, but also using homodyne detection, is to employ a CV Bell measurement and continuous feedback to perform an entanglement swap experiment of DV atomic qubits $^{93}$ .

Hybrid quantum computing. Examples of gates leading to universal quantum computing for DV and CV logical encoding are given in Boxes 1 and 2, and these approaches might benefit from hybridization. For example, the non-Gaussian single-mode cubic phase gate required for CV computing can be realized by introducing DV projectors and conditional squeezing operations[94-96]. The alternative to circuit-based quantum computing is the measurement-based approach exploiting entangled cluster

states $^{97,98}$ . This also benefits from hybridization, where Gaussian cluster states perform the computation using DV non-Gaussian projectors (Fig. 2). In contrast to CV quantum computing, the two-qubit gate for DV quantum computing based on light is difficult to realize deterministically. Measurement-induced approaches to the CNOT gate tend to suffer from massive overhead requirements, and deterministic schemes based on giant material nonlinearities are very challenging, although important progress is being made $^{99}$ . However, it has been shown theoretically that by combining a relatively weak cross-Kerr nonlinearity with a CV homodyne measurement, it is possible to realize a quantum non-demolition measurement which in turn can be used to implement a near-deterministic DV CNOT gate with much fewer resources than would otherwise be possible $^{100,101}$ .

There is yet another approach to hybrid quantum computing, in which the quantum information itself is a hybrid between DV and CV. Here the information is encoded in a macroscopic qubit consisting of a discrete superposition of CV coherent states—a cat state as introduced previously. Universal quantum computation can be executed using a measurement-induced approach where gates are implemented through teleportation $^{102,103}$  and different gates are realized by the usage of different types of entangled states $^{104,105}$ . Such a teleportation circuit operating on a set of binary coherent states was recently demonstrated $^{106}$ . A simplified, but highly probabilistic approach has also been put forward $^{107}$  and proof-of-principle implementations of both the Hadamard $^{108}$  and the phase-shift gate $^{109}$  have been realized. All these experiments on cat-state computing were performed in the optical regime, but could potentially also be realized in the microwave regime with high fidelity or on phononic modes of mechanical oscillators or ions. Some of the complications of the cat-state protocol can be circumvented by encoding the information in a hybrid DV/CV entangled cat state $^{110}$ . Moreover, by extending the cat qubit to include four different coherent state phases $^{111}$  or by encoding it into several modes $^{112}$ , the qubit becomes more robust against losses; also a universal set of gates can be realized by tailoring a specific Hamiltonian using circuit QED (ref. 113).

Hybrid Bell tests. The falsification of hidden local variable theories $^{114}$  through the violation of Bell's inequality has so far been hampered by the difficulty in measuring entangled states distributed over large distances with high efficiency. A solution could be the use of a hybrid detection strategy alternating between a DV photon-counting measurement and a CV homodyne measurement $^{115}$ . The benefit would arise from the near-ideal detection efficiency of the homodyne detector, which reduces the requirement on the transmission and photon-counting efficiencies. However, there seems to be a trade-off between the required efficiencies and the complexity of the entangled state generation. For instance, the photon counting efficiency can be very low for a highly complex state $^{116}$ , while being challengingly high for an easily producible W state $^{117,118}$ . As an alternative, it is possible to make an asymmetric Bell test that involves atom-photon entanglement and hybrid photonic measurements $^{119,120}$ . As the atom can be detected with near-ideal efficiency, the efficiency threshold for the DV photonic measurement can be fairly low, and can again be traded against a higher complexity in state generation. Finally we note that by using an entangled cat state it is possible to violate Bell's inequality with purely CV homodyne measurements, albeit under some experimentally challenging conditions $^{121}$ .

# Outlook

Until recently, the boundary between DV and CV QIP platforms has been very sharp. This is no longer the case, thanks to recent advances in combining the technologies of the two approaches, which has led to theoretical proposals and experimental implementations

![](images/05f664d7afa6fa481238db7e15ee321899605bf2c2e4ef8cc016e2f647d11cf2.jpg)  
Figure 2 | Measurement-based quantum computation using two-dimensional lattices corresponding to offline-prepared, multi-mode cluster states. The lattices are built from single-mode states through Gaussian two-mode interactions (squeezers and beam-splitter-like operations; thick red lines). Arbitrary multi-mode states (three modes; the vertically oriented input and output modes in gold) can be processed by individually measuring all the modes (thin grey lines) except for the output and feedforwarding the measurement results (thin gold arrows). Quantum and classical (feedforward) information evolve from left to right. Top: some of the Gaussian squeezed single-mode states of the cluster are replaced by non-Gaussian single-mode states; all measurements are Gaussian homodyne detections. Bottom: some of the Gaussian detectors (red) are replaced by non-Gaussian detectors (for example, photon counters); all initial single-mode states are Gaussian squeezed states, and hence the entire cluster state is Gaussian. Universal operations—that is, arbitrary output states—can be achieved either way, through CV measurements on non-Gaussian states or arbitrary measurements on Gaussian states. For arbitrarily long computations, the accumulation of errors caused, for example, by finite squeezing must be suppressed by means of some form of quantum error correction.

of new promising QIP protocols. Most of the demonstrations so far are proof-of-principle experiments lacking high-fidelity

operation, efficiency and scalability. To advance the field, a deeper understanding of the present limitations is needed. Still, the field is very young, and we might have scratched only the surface of a much larger and richer field.

Received 15 January 2014; accepted 24 June 2015; published online 1 September 2015

# References

1. Ladd, T. D. et al. Quantum computers. Nature 464, 45-53 (2010).  
2. Nielsen, M. A. & Chuang, I. L. Quantum Computation and Quantum Information (Cambridge Univ. Press, 2000).  
3. Braunstein, S. L. & van Loock, P. Quantum information with continuous variables. Rev. Mod. Phys. 77, 513-577 (2005).  
4. Andersen, U. L., Leuchs, G. & Silberhorn, C. Continuous-variable quantum information processing. *Laser Photon. Rev.* 4, 337-354 (2010).  
5. Weedbrook, C. et al. Gaussian quantum information. Rev. Mod. Phys. 84, 621-669 (2012).  
6. Castellanos-Beltran, M. A., Irwin, K. D., Hilton, G. C., Vale, L. R. & Lehnert, K. W. Amplification and squeezing of quantum noise with a tunable Josephson metamaterial. Nature Phys. 4, 929-931 (2008).  
7. Eichler, C. et al. Observation of two-mode squeezing in the microwave frequency domain. Phys. Rev. Lett. 107, 113601 (2011).  
8. Esteve, J., Gross, C., Weller, a., Giovanazzi, S. & Oberthaler, M. K. Squeezing and entanglement in a Bose-Einstein condensate. Nature 455, 1216-1219 (2008).  
9. Rudner, M. S., Vandersypen, L. M. K., Vuletic, V. & Levitov, L. S. Generating entanglement and squeezed states of nuclear spins in quantum dots. Phys. Rev. Lett. 107, 206806 (2011).  
10. Bennett, S. et al. Phonon-induced spin-spin interactions in diamond nanostructures: Application to spin squeezing. Phys. Rev. Lett. 110, 156402 (2013).  
11. Aspelmeyer, M., Kippenberg, T. J. & Marquardt, F. Cavity optomechanics. Rev. Mod. Phys. 86, 1391 (2014).  
12. Palomaki, T. A., Teufel, J. D., Simmonds, R. W. & Lehnert, K. W. Entangling mechanical motion with microwave fields. Science 342, 710-713 (2013).  
13. Eisaman, M. D., Fan, J., Migdall, A. L. & Polyakov, S. V. Invited review article: Single-photon sources and detectors. Rev. Sci. Instrum. 82, 071101 (2011).  
14. Deleglise, S. et al. Reconstruction of non-classical cavity field states with snapshots of their decoherence. Nature 455, 510-514 (2008).  
15. Eichler, C. et al. Experimental state tomography of itinerant single microwave photons. Phys. Rev. Lett. 106, 220503 (2011).  
16. Mallet, F. et al. Quantum state tomography of an itinerant squeezed microwave field. Phys. Rev. Lett. 106, 220502 (2011).  
17. Bimbard, E. et al. Homodyne tomography of a single photon retrieved on demand from a cavity-enhanced cold atom memory. Phys. Rev. Lett. 112, 033601 (2014).  
18. Law, C. K. & Eberly, J. H. Arbitrary control of a quantum electromagnetic field. Phys. Rev. Lett. 76, 1055-1058 (1996).  
19. Hofheinz, M. et al. Generation of Fock states in a superconducting quantum circuit. Nature 454, 310-314 (2008).  
20. Hofheinz, M. et al. Synthesizing arbitrary quantum states in a superconducting resonator. Nature 459, 546-549 (2009).  
21. Yurke, B. & Stoler, D. Generating quantum mechanical superpositions of macroscopically distinguishable states via amplitude dispersion. Phys. Rev. Lett. 57, 13-16 (1986).  
22. Monroe, C., Meekhof, D. M., King, B. E. & Wineland, D. J. A. "Schrodinger cat" superposition state of an atom. Science 272, 1131-1136 (1996).  
23. Brune, M. et al. Observing the progressive decoherence of the "meter" in a quantum measurement. Phys. Rev. Lett. 77, 4887-4890 (1996).  
24. Vlastakis, B. et al. Deterministically encoding quantum information using 100-photon Schrodinger cat states. Science 607, 607-610 (2013).  
25. O'Connell, A. D. et al. Quantum ground state and single-phonon control of a mechanical resonator. Nature 464, 697-703 (2010).  
26. Wilson-Rae, I., Zoller, P. & Imamoglu, a. Laser cooling of a nanomechanical resonator mode to its quantum ground state. Phys. Rev. Lett. 92, 075507 (2004).  
27. Rabl, P. et al. Strong magnetic coupling between an electronic spin qubit and a mechanical resonator. Phys. Rev. B 79, 041302 (2009).  
28. Hammerer, K. et al. Strong coupling of a mechanical oscillator and a single atom. Phys. Rev. Lett. 103, 063005 (2009).  
29. Ramos, T., Sudhir, V., Stannigel, K., Zoller, P. & Kippenberg, T. J. Nonlinear quantum optomechanics via individual intrinsic two-level defects. Phys. Rev. Lett. 110, 193602 (2013).  
30. Ovartchaiyapong, P., Lee, K. W., Myers, B. a. & Jayich, A. C. B. Dynamic strain-mediated coupling of a single diamond spin to a mechanical resonator. Nature Commun. 5, 4429 (2014).

31. Teissier, J., Barfuss, A., Appel, P., Neu, E. & Maletinsky, P. Strain coupling of a nitrogen-vacancy center spin to a diamond mechanical oscillator. Phys. Rev. Lett. 113, 020503 (2014).  
32. Stannigel, K., Rabl, P., Sorensen, A. S., Zoller, P. & Lukin, M. D. Optomechanical transducers for long-distance quantum communication. Phys. Rev. Lett. 105, 220501 (2010).  
33. Lvovsky, A. I. et al. Quantum state reconstruction of the single-photon Fock state. Phys. Rev. Lett. 87, 050402 (2001).  
34. Zavatta, A., Viciani, S. & Bellini, M. Quantum-to-classical transition with single-photon-added coherent states of light. Science 306, 660-662 (2004).  
35. Wenger, J., Tualle-Brouri, R. & Grangier, P. Non-Gaussian statistics from individual pulses of squeezed light. Phys. Rev. Lett. 92, 153601 (2004).  
36. Ourjoumtsev, A., Tualle-brouri, R., Laurat, J. & Grangier, P. Generating optical Schrödinger kittens for quantum information processing. Science 312, 83-86 (2006).  
37. Neergaard-Nielsen, J. S., Nielsen, B. M., Hettich, C., Mølmer, K. & Polzik, E. S. Generation of a superposition of odd photon number states for quantum information networks. Phys. Rev. Lett. 97, 083604 (2006).  
38. Wakui, K., Takahashi, H., Furusawa, A. & Sasaki, M. Photon subtracted squeezed states generated with periodically poled  $\mathrm{KTiOPO_4}$ . Opt. Express 15, 3568-3574 (2007).  
39. Dakna, M., Anhut, T., Opatrny, T., Knöll, L. & Welsch, D.-G. Generating Schrödinger-cat-like states by means of conditional measurements on a beam splitter. Phys. Rev. A 55, 3184-3194 (1997).  
40. Ourjoumtsev, A., Tualle-Brouri, R. & Grangier, P. Quantum homodyne tomography of a two-photon Fock state. Phys. Rev. Lett. 96, 213601 (2006).  
41. Cooper, M., Wright, L., Soller, C. & Smith, B. Experimental generation of multi-photon Fock states. Opt. Express 21, 5311-5317 (2013).  
42. Takahashi, H. et al. Generation of large-amplitude coherent-state superposition via ancilla-assisted photon subtraction. Phys. Rev. Lett. 101, 233605 (2008).  
43. Gerrits, T. et al. Generation of optical coherent-state superpositions by number-resolved photon subtraction from the squeezed vacuum. Phys. Rev. A 82, 031802(R) (2010).  
44. Namekata, N. et al. Non-Gaussian operation based on photon subtraction using a photon-number-resolving detector at a telecommunications wavelength. Nature Photon. 4, 655-660 (2010).  
45. Lvovsky, A. I. & Mlynek, J. Quantum-optical catalysis: Generating nonclassical states of light by means of linear optics. Phys. Rev. Lett. 88, 250401 (2002).  
46. Resch, K., Lundeen, J. S. & Steinberg, A. Quantum state preparation and conditional coherence. Phys. Rev. Lett. 88, 113601 (2002).  
47. Babichev, S. A., Ries, J. & Lvovsky, A. I. Quantum scissors: Teleportation of single-mode optical states by means of a nonlocal single photon. Europhys. Lett. 64, 1-7 (2003).  
48. Bimbard, E., Jain, N., MacRae, A. & Lvovsky, A. I. Quantum-optical state engineering up to the two-photon level. Nature Photon. 4, 243-247 (2010).  
49. Yukawa, M. et al. Generating superposition of up-to three photons for Yukawa's equation. Opt. Express 21, 5529-5535 (2013).  
50. Neergaard-Nielsen, J. S. et al. Optical continuous-variable qubit. Phys. Rev. Lett. 105, 053602 (2010).  
51. Babichev, S. A., Brezger, B. & Lvovsky, A. I. Remote preparation of a single-mode photonic qubit by measuring field quadrature noise. Phys. Rev. Lett. 92, 047903 (2004).  
52. Ourjoumtsev, A., Jeong, H., Tuelle-Brouri, R. & Grangier, P. Generation of optical 'Schrodinger cats' from photon number states. Nature 448, 784-786 (2007).  
53. Ourjountsev, A., Ferreyrol, F., Tuelle-Brouri, R. & Grangier, P. Preparation of non-local superpositions of quasi-classical light states. Nature Phys. 5, 189-192 (2009).  
54. Jeong, H. et al. Generation of hybrid entanglement of light. Nature Photon. 8, 564-569 (2014).  
55. Morin, O. et al. Remote creation of hybrid entanglement between particle-like and wave-like optical qubits. Nature Photon. 8, 570-574 (2014).  
56. Andersen, U. L. & Neergaard-Nielsen, J. S. Heralded generation of a micro-macro entangled state. Phys. Rev. A 88, 022337 (2013).  
57. Paternostro, M. Engineering nonclassicality in a mechanical system through photon subtraction. Phys. Rev. Lett. 106, 183601 (2011).  
58. Galland, C., Sangouard, N., Piro, N., Gisin, N. & Kippenberg, T. J. Heralded single-phonon preparation, storage, and readout in cavity optomechanics. Phys. Rev. Lett. 112, 143602 (2014).  
59. Christensen, S. L. et al. Toward quantum state tomography of a single polariton state of an atomic ensemble. New J. Phys. 15, 015002 (2013).  
60. Haas, F., Volz, J., Gehr, R., Reichel, J. & Esteve, J. Entangled states of more than 40 atoms in an optical fiber cavity. Science 344, 180-183 (2014).  
61. McConnell, R., Zhang, H., Hu, J., Cuk, S. & Vuletic, V. Entanglement with negative Wigner function of almost 3,000 atoms heralded by one photon. Nature 519, 439-442 (2015).

62. Bennett, C. H. et al. Teleporting an unknown quantum state via dual classical and Einstein-Podolsky-Rosen channels. Phys. Rev. Lett. 70, 1895-1899 (1993).  
63. Braunstein, S. L. & Kimble, H. J. Teleportation of Continuous Quantum Variables. Phys. Rev. Lett. 80, 869-872 (1998).  
64. Takeda, S., Mizuta, T., Fuwa, M., van Loock, P. & Furusawa, A. Deterministic quantum teleportation of photonic quantum bits by a hybrid technique. Nature 500, 315-318 (2013).  
65. Lee, N. et al. Teleportation of nonclassical wave packets of light. Science 332, 330-333 (2011).  
66. Andersen, U. L. & Ralph, T. C. High-fidelity teleportation of continuous-variable quantum states using delocalized single photons. Phys. Rev. Lett. 111, 050504 (2013).  
67. Calsamiglia, J. & Lutkenhaus, N. Maximum efficiency of a linear-optical Bell-state analyzer. Appl. Phys. B 72, 67-71 (2001).  
68. Zaidi, H. a. & van Loock, P. Beating the one-half limit of ancilla-free linear optics bell measurements. Phys. Rev. Lett. 110, 260501 (2013).  
69. Duan, L.-M., Lukin, M. D., Cirac, J. I. & Zoller, P. Long-distance quantum communication with atomic ensembles and linear optics. Nature 414, 413-418 (2001).  
70. Sherson, J. F. et al. Quantum teleportation between light and matter. Nature 443, 557-560 (2006).  
71. Yuan, Z.-S. et al. Experimental demonstration of a BDCZ quantum repeater node. Nature 454, 1098-1101 (2008).  
72. Eisert, J., Scheel, S. & Plenio, M. B. Distilling Gaussian states with Gaussian operations is impossible. Phys. Rev. Lett. 89, 137903 (2002).  
73. Fiurasek, J. Gaussian transformations and distillation of entangled Gaussian states. Phys. Rev. Lett. 89, 137904 (2002).  
74. Giedke, G. & Ignacio Cirac, J. Characterization of Gaussian operations and distillation of Gaussian states. Phys. Rev. A 66, 032316 (2002).  
75. Opatrný, T., Kurizki, G. & Welsch, D.-G. Improvement on teleportation of continuous variables by photon subtraction via conditional measurement. Phys. Rev. A 61, 032302 (2000).  
76. Ourjountsev, A., Dantan, A., Tualle-Brouri, R. & Grangier, P. Increasing entanglement between Gaussian states by coherent photon subtraction. Phys. Rev. Lett. 98, 030502 (2007).  
77. Takahashi, H. et al. Entanglement distillation from Gaussian input states. Nature Photon. 4, 178-181 (2010).  
78. Kurochkin, Y., Prasad, A. S. & Lvovsky, a. I. Distillation of the two-mode squeezed state. Phys. Rev. Lett. 112, 070402 (2014).  
79. Zhang, S. & van Loock, P. Local Gaussian operations can enhance continuous-variable entanglement distillation. Phys. Rev. A 84, 062309 (2011).  
80. Fiurasek, J. Improving entanglement concentration of Gaussian states by local displacements. Phys. Rev. A 84, 012335 (2011).  
81. Tipsmark, A., Neergaard-Nielsen, J. S. & Andersen, U. L. Displacement-enhanced entanglement distillation of single-mode-squeezed entangled states. Opt. Express 21, 6670-6680 (2013).  
82. Datta, A. et al. Compact continuous-variable entanglement distillation. Phys. Rev. Lett. 108, 060502 (2012).  
83. Ralph, T. C. & Lund, A. P. in AIP Conference Proceedings (ed. Lvovsky, A.) 155-160 (AIP, 2009).  
84. Ralph, T. C. Quantum error correction of continuous-variable states against Gaussian noise. Phys. Rev. A 84, 022339 (2011).  
85. Xiang, G. Y., Ralph, T. C., Lund, A. P., Walk, N. & Pryde, G. J. Heralded noiseless linear amplification and distillation of entanglement. Nature Photon. 4, 316-319 (2010).  
86. Ferreyrol, F. et al. Implementation of a nondeterministic optical noiseless amplifier. Phys. Rev. Lett. 104, 123603 (2010).  
87. Zavatta, A., Fiurášek, J. & Bellini, M. A high-fidelity noiseless amplifier for quantum light states. Nature Photon. 5, 52-60 (2010).  
88. Usuga, M. A. et al. Noise-powered probabilistic concentration of phase information. Nature Phys. 6, 767-771 (2010).  
89. Suzuki, S., Takeoka, M., Sasaki, M., Andersen, U. L. & Kannari, F. Practical purification scheme for decohered coherent-state superpositions via partial homodyne detection. Phys. Rev. A 73, 042304 (2006).  
90. Brask, J. B., Rigas, I., Polzik, E., Andersen, U. L. & Sørensen, A. S. Hybrid long-distance entanglement distribution protocol. Phys. Rev. Lett. 105, 160501 (2010).  
91. Blandino, R., Walk, N., Lund, A. P. & Ralph, T. C. Channel purification via continuous-variable quantum teleportation with Gaussian post-selection. Preprint at http://arXiv.org/abs/1408.6018 (2014).  
92. van Loock, P. et al. Hybrid quantum repeater using bright coherent light. Phys. Rev. Lett. 96, 240501 (2006).  
93. Hofer, S. G., Vasilyev, D. V., Aspelmeyer, M. & Hammerer, K. Time-continuous bell measurements. Phys. Rev. Lett. 111, 170404 (2013).  
94. Gottesman, D., Kitaev, A. & Preskill, J. Encoding a qubit in an oscillator. Phys. Rev. A 64, 012310 (2001).  
95. Lloyd, S. & Braunstein, S. L. Quantum computation over continuous variables. Phys. Rev. Lett. 82, 1784-1787 (1999).

96. Marek, P., Filip, R. & Furusawa, A. Deterministic implementation of weak quantum cubic nonlinearity. Phys. Rev. A 84, 053802 (2011).  
97. Raussendorf, R. & Briegel, H. J. A one-way quantum computer. Phys. Rev. Lett. 86, 5188-5191 (2001).  
98. Menicucci, N. et al. Universal quantum computation with continuous-variable cluster states. Phys. Rev. Lett. 97, 110501 (2006).  
99. Chang, D. E., Vuletic, V. & Lukin, M. D. Quantum nonlinear optics photon by photon. Nature Photon. 8, 685-694 (2014).  
100. Nemoto, K. & Munro, W. J. Nearly deterministic linear optical controlled-NOT gate. Phys. Rev. Lett. 93, 250502 (2004).  
101. Spiller, T. P. et al. Quantum computation by communication. New J. Phys. 8, 30 (2006).  
102. Jeong, H., Kim, M. & Lee, J. Quantum-information processing for a coherent superposition state via a mixed entangled coherent channel. Phys. Rev. A 64, 052308 (2001).  
103. van Enk, S. J. & Hirota, O. Entangled coherent states: Teleportation and decoherence. Phys. Rev. A 64, 022313 (2001).  
104. Ralph, T. C., Gilchrist, A., Milburn, G., Munro, W. J. & Glancy, S. Quantum computation with optical coherent states. Phys. Rev. A 68, 042319 (2003).  
105. Lund, A. P., Ralph, T. C. & Haselgrove, H. L. Fault-tolerant linear optical quantum computing with small-amplitude coherent states. Phys. Rev. Lett. 100, 030503 (2008).  
106. Neergaard-Nielsen, J. S., Eto, Y., Lee, C.-w., Jeong, H. & Sasaki, M. Quantum tele-amplification with a continuous-variable superposition state. Nature Photon. 7, 439-443 (2013).  
107. Marek, P. & Fiurasek, J. Resources for universal quantum-state manipulation and engineering. Phys. Rev. A 79, 062321 (2009).  
108. Tipsmark, A. et al. Experimental demonstration of a Hadamard gate for coherent state qubits. Phys. Rev. A 84, 050301(R) (2011).  
109. Blandino, R., Ferreyrol, F., Barbieri, M., Grangier, P. & Tualle-Brouri, R. Characterization of a  $\pi$ -phase shift quantum gate for coherent-state qubits. New J. Phys. 14, 013017 (2012).  
110. Lee, S.-W. & Jeong, H. Near-deterministic quantum teleportation and resource-efficient quantum computation using linear optics and hybrid qubits. Phys. Rev. A 87, 022326 (2013).  
111. Leghtas, Z. et al. Deterministic protocol for mapping a qubit to coherent state superpositions in a cavity. Phys. Rev. A 87, 042315 (2013).  
112. Glancy, S., Vasconcelos, H. & Ralph, T. C. Transmission of optical coherent-state qubits. Phys. Rev. A 70, 022317 (2004).  
113. Mirrahimi, M. et al. Dynamically protected cat-qubits: A new paradigm for universal quantum computation. New J. Phys. 16, 045014 (2014).  
114. Bell, J. S. On the Einstein Podolsky Rosen paradox. Physics 1, 195-200 (1964).  
115. Ji, S.-W., Kim, J., Lee, H.-W., Zubairy, M. & Nha, H. Loophole-free Bell test for continuous variables via wave and particle correlations. Phys. Rev. Lett. 105, 170404 (2010).  
116. Quintino, M. T., Araújo, M., Cavalcanti, D., Santos, M. F. & Cunha, M. T. Maximal violations and efficiency requirements for Bell tests with photodetection and homodyne measurements. J. Phys. A 45, 215308 (2012).  
117. Lagaout, A., Björk, G. & Andersen, U. L. Realistic limits on the nonlocality of an N-partite single-photon superposition. Phys. Rev. A 84, 062127 (2011).  
118. Chaves, R. & Brask, J. B. Feasibility of loophole-free nonlocality tests with a single photon. Phys. Rev. A 84, 062110 (2011).  
119. Sangouard, N. et al. Loophole-free Bell test with one atom and less than one photon on average. Phys. Rev. A 84, 052122 (2011).  
120. Teo, C. et al. Realistic loophole-free Bell test with atom-photon entanglement. Nature Commun. 4, 2104 (2013).  
121. García-Patron, R. et al. Proposal for a loophole-free Bell test using homodyne detection. Phys. Rev. Lett. 93, 130409 (2004).

# Acknowledgements

The authors gratefully acknowledge support from the Danish Council for Independent Research (Sapere Aude programmes under FTP and FNU), the Lundbeck Foundation, the Villum Foundation Young Investigator Programme, the Federal Ministry for Education and Research in Germany (Q.com), ERA-NET CHISTERA (Hipercom), the Ministry of Education, Culture, Sports, Science and Technology of Japan (PDIS - Project for Developing Innovation Systems, GIA - Grant-in-Aid for Scientific Research, and APSA - Advanced Photon Science Alliance), Universities Denmark, and Japan Society for the Promotion of Science.

# Additional information

Reprints and permissions information is available online at www.nature.com/reprints. Correspondence should be addressed to U.L.A.

# Competing financial interests

The authors declare no competing financial interests.