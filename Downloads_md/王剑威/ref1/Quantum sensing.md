# Quantum sensing

C. L. Degen*

Department of Physics, ETH Zurich, Otto Stern Weg 1, 8093 Zurich, Switzerland

F. Reinhard†

Walter Schottky Institut and Physik-Department, Technische Universität München, Am Coulombwall 4, 85748 Garching, Germany

P. Cappellaro

Research Laboratory of Electronics and Department of Nuclear Science & Engineering, Massachusetts Institute of Technology, 77 Massachusetts Avenue, Cambridge, Massachusetts 02139, USA

(published 25 July 2017)

"Quantum sensing" describes the use of a quantum system, quantum properties, or quantum phenomena to perform a measurement of a physical quantity. Historical examples of quantum sensors include magnetometers based on superconducting quantum interference devices and atomic vapors or atomic clocks. More recently, quantum sensing has become a distinct and rapidly growing branch of research within the area of quantum science and technology, with the most common platforms being spin qubits, trapped ions, and flux qubits. The field is expected to provide new opportunities—especially with regard to high sensitivity and precision—in applied physics and other areas of science. This review provides an introduction to the basic principles, methods, and concepts of quantum sensing from the viewpoint of the interested experimentalist.

DOI: 10.1103/RevModPhys.89.035002

# CONTENTS

I. Introduction

A. Content

II. Definitions

A. Quantum sensing  
B. Quantum sensors

III. Examples of Quantum Sensors

A. Neutral atoms as magnetic field sensors

1. Atomic vapors  
2. Cold atomic clouds

B. Trapped ions  
C. Rydberg atoms  
D. Atomic clocks

E. Solid-state spins: Ensemble sensors

1. NMR ensemble sensors  
2. NV center ensembles

F. Solid-state spins: Single-spin sensors

G. Superconducting circuits

1. SQUID  
2. Superconducting qubits

H. Elementary particle qubits

1. Muons  
2. Neutrons

I. Other sensors

1. Single electron transistors  
2. Optomechanics

* degenc@ethz.ch  
friedemann@quantum-minigolf.org  
$\ddagger$  pcappell@mit.edu

3. Photons 9

IV. The Quantum Sensing Protocol 9

A.Quantum sensor Hamiltonian 9

1. Internal Hamiltonian 10  
2. Signal Hamiltonian 10  
3. Control Hamiltonian 10

B. The sensing protocol 10

C. First example: Ramsey measurement 11  
D.Second example: Rabi measurement 12  
E. Slope and variance detection 12

1. Slopedetection (linear detection) 12  
2. Variance detection (quadratic detection) 12

V. Sensitivity 12

A. Noise 13

1. Quantum projection noise 13  
2.Decoherence 13

3. Errors due to initialization and qubit manipulations 14  
4.Classical readout noise 14

a. Single shot readout 14  
b. Averaged readout 14  
c. Total readout uncertainty 15

B. Sensitivity 15

1. Signal-to-noise ratio 15  
2. Minimum detectable signal and sensitivity 15

a. Slope detection 15  
b. Variance detection 15

3. Signal integration 15

C. Allan variance 16  
D.Quantum Cramér-Rao bound for parameter estimation 16

VI. Sensing of ac Signals 17

A. Time-dependent signals 17

B. Ramsey and echo sequences 17

C. Multipulse sensing sequences 18

1. Carr-Purcell (CP) and periodic dynamical decoupling sequences 18  
2.Lock-in detection 19  
3. Other types of multipulse sensing sequences 19  
4.ac signals with random phase 19  
5.ac signals with random phase and random amplitude 20

D. Wave form reconstruction 20

E. Frequency estimation 20

1. Dynamical decoupling spectroscopy 20  
2.Correlation sequences 20  
3. Continuous sampling 21

VII. Noise Spectroscopy 21

A. Noise processes 21  
B. Decoherence, dynamical decoupling, and filter functions 22

1.Decoherence function  $\chi$  22  
2.Filter function  $Y$  22  
3. Dynamical decoupling 22

C. Relaxometry 23

1. Basic theory of relaxometry 23  
2.  $T_{1}$  relaxometry 24  
3.  $T_{2}^{*}$  and  $T_{2}$  relaxometry 24  
4. Dressed state methods 25

VIII. Dynamic Range and Adaptive Sensing 25

A. Phase estimation protocols 26

1.Quantum phase estimation 26  
2. Adaptive phase estimation 27  
3. Nonadaptive phase estimation 27  
4. Comparison of phase estimation protocols 28

B. Experimental realizations 28

IX. Ensemble Sensing 28

A. Ensemble sensing without entanglement 28  
B.Heisenberg limit 28

C. Entangled states 29

1. GHZ and N00N states 29  
2. Squeezing 30  
3. Parity measurements 30  
4. Other types of entanglement 30

X. Sensing Assisted by Auxiliary Qubits 31

A.Quantum logic clock 31  
B.Storage and retrieval 31  
C.Quantum error correction 31

XI.Outlook 32

Acknowledgments 33  
Appendix Table of Symbols 33  
References 34

# I. INTRODUCTION

Can we find a promising real-world application of quantum mechanics that exploits its most counterintuitive properties? This question has intrigued physicists ever since quantum theory development in the early twentieth century. Today, quantum computers (Deutsch, 1985; DiVincenzo, 2000) and quantum cryptography (Gisin et al., 2002) are widely believed to be the most promising ones.

Interestingly, however, this belief might turn out to be incomplete. In recent years a different class of applications has emerged that employs quantum mechanical systems as

sensors for various physical quantities ranging from magnetic and electric fields, to time and frequency, to rotations, to temperature and pressure. "Quantum sensors" capitalize on the central weakness of quantum systems, their strong sensitivity to external disturbances. This trend in quantum technology is curiously reminiscent of the history of semiconductors: here, too, sensors—for instance light meters based on selenium photocells (Weston, 1931)—have found commercial applications decades before computers.

Although quantum sensing as a distinct field of research in quantum science and engineering is quite recent, many concepts are well known in the physics community and have resulted from decades of development in high-resolution spectroscopy, especially in atomic physics and magnetic resonance. Notable examples include atomic clocks, atomic vapor magnetometers, and superconducting quantum interference devices. What can be considered as "new" is that quantum systems are increasingly investigated at the single-atom level, that entanglement is used as a resource for increasing the sensitivity, and that quantum systems and quantum manipulations are specifically designed and engineered for sensing purposes.

The focus of this review is on the key concepts and methods of quantum sensing, with particular attention to practical aspects that emerge from nonideal experiments. As quantum sensors we will consider mostly qubits—two-level quantum systems. Although an overview over actual implementations of qubits is given, the review will not cover any of those implementations in specific detail. It will also not cover related fields including atomic clocks or photon-based sensors. In addition, theory will be considered only up to the point necessary to introduce the key concepts of quantum sensing. The motivation behind this review is to offer an introduction to students and researchers new to the field and to provide a basic reference for researchers already active in the field.

# A. Content

The review starts by suggesting some basic definitions for "quantum sensing" and by noting the elementary criteria for a quantum system to be useful as a quantum sensor (Sec. II). The next section provides an overview of the most important physical implementations (Sec. III). The discussion then moves on to the core concepts of quantum sensing, which include the basic measurement protocol (Sec. IV) and the sensitivity of a quantum sensor (Sec. V). Sections VI and VII cover the important area of time-dependent signals and quantum spectroscopy. The remaining sections introduce some advanced quantum sensing techniques. These include adaptive methods developed to greatly enhance the dynamic range of the sensor (Sec. VIII) and techniques that involve multiple qubits (Secs. IX and X). In particular, entanglement-enhanced sensing, quantum storage, and quantum error correction (QEC) schemes are discussed. The review then concludes with a brief outlook on possible future developments (Sec. XI).

There have already been several reviews that covered different aspects of quantum sensing. Excellent introductions into the field are the review by Budker and Romalis (2007) and the book by Budker and Kimball (2013) on atomic vapor

magnetometry, and the paper by Taylor et al. (2008) on magnetometry with nitrogen-vacancy centers in diamond. Entanglement-assisted sensing, sometimes referred to as "quantum metrology," "quantum-enhanced sensing," or "second generation quantum sensors," is covered by Bollinger et al. (1996) and Giovannetti, Lloyd, and Maccone (2004, 2006, 2011). In addition, many excellent reviews covering different implementations of quantum sensors are available; these are noted in Sec. III.

# II. DEFINITIONS

# A. Quantum sensing

Quantum sensing is typically used to describe one of the following:

(I) Use of a quantum object to measure a physical quantity (classical or quantum). The quantum object is characterized by quantized energy levels. Specific examples include electronic, magnetic or vibrational states of superconducting or spin qubits, neutral atoms, or trapped ions.  
(II) Use of quantum coherence (i.e., wavelike spatial or temporal superposition states) to measure a physical quantity.  
(III) Use of quantum entanglement to improve the sensitivity or precision of a measurement, beyond what is possible classically.

Of these three definitions, the first two are rather broad and cover many physical systems. This even includes some systems that are not strictly "quantum." An example is classical wave interference as it appears in optical or mechanical systems (Novotny, 2010; Faust et al., 2013). The third definition is more stringent and a truly quantum definition. However, since quantum sensors according to definitions I and II are often close to applications, we will mostly focus on these definitions and discuss them extensively in this review. While these types of sensors might not exploit the full power of quantum mechanics, as for type-III sensors, they already can provide several advantages, most notably operation at nanoscales that are not accessible to classical sensors.

Because type-III quantum sensors rely on entanglement, more than one sensing qubit is required. A well-known example is the use of maximally entangled states to reach a Heisenberg-limited measurement. Type-III quantum sensors are discussed in Sec. X.

# B. Quantum sensors

In analogy to the DiVincenzo criteria for quantum computation (DiVincenzo, 2000), a set of four necessary attributes is listed for a quantum system to function as a quantum sensor. These attributes include three original DiVincenzo criteria as follows:

(1) The quantum system has discrete, resolvable energy levels. Specifically, we assume it to be a two-level system (or an ensemble of two-level systems) with a lower energy state  $|0\rangle$  and an upper energy state  $|1\rangle$

![](images/9fe1a940e4eab755ec9a2d5cfc95b4c6469c063279793e3ad09a268bc5653ee8.jpg)  
FIG. 1. Basic features of a two-state quantum system.  $|0\rangle$  is the lower energy state and  $|1\rangle$  is the higher energy state. Quantum sensing exploits changes in the transition frequency  $\omega_0$  or the transition rate  $\Gamma$  in response to an external signal  $V$ .

![](images/a1b9a570c89d22d0b3e4a2b9fa8e237a188b3412c35a4edd3589747d7dea35ca.jpg)

that are separated by a transition energy  $E = \hbar \omega_0$  (see Fig. 1).<sup>1</sup>

(2) It must be possible to initialize the quantum system into a well-known state and to read out its state.  
(3) The quantum system can be coherently manipulated, typically by time-dependent fields. This condition is not strictly required for all protocols; examples that fall outside of this criterion are continuous-wave spectroscopy or relaxation rate measurements.

The focus on two-level systems (1) is not a severe restriction because many properties of more complex quantum systems can be modeled through a qubit sensor (Goldstein, Lukin, and Cappellaro, 2010). The fourth attribute is specific to quantum sensing:

(4) The quantum system interacts with a relevant physical quantity  $V(t)$ , such as an electric or magnetic field. The interaction is quantified by a coupling or transduction parameter of the form  $\gamma = \partial^q E / \partial V^q$  which relates changes in the transition energy  $E$  to changes in the external parameter  $V$ . In most situations the coupling is either linear ( $q = 1$ ) or quadratic ( $q = 2$ ). The interaction with  $V$  leads to a shift of the quantum system's energy levels or to transitions between energy levels (see Fig. 1).

Experimental realizations of quantum sensors can be compared by some key physical characteristics. One characteristic is to what kind of external parameter(s) the quantum sensor responds to. Charged systems, like trapped ions, will be sensitive to electrical fields, while spin-based systems will mainly respond to magnetic fields. Some quantum sensors may respond to several physical parameters.

A second important characteristic is a quantum sensor's "intrinsic sensitivity." On the one hand, a quantum sensor is expected to provide a strong response to wanted signals, while on the other hand, it should be minimally affected by unwanted noise. Clearly, these are conflicting requirements. In Sec. V, we will see that the sensitivity scales as

$$
\text {s e n s i t i v i t y} \propto \frac {1}{\gamma \sqrt {T _ {\chi}}}, \tag {1}
$$

where  $\gamma$  is the above transduction parameter and  $T_{\chi}$  is a decoherence or relaxation time that reflects the immunity of the quantum sensor against noise. In order to optimize the sensitivity,  $\gamma$  should be large (for example, by the choice of an appropriate physical realization of the sensor) and the decoherence time  $T_{\chi}$  must be made as long as possible. Strategies to achieve the latter are discussed at length in the later sections of this review.

# III. EXAMPLES OF QUANTUM SENSORS

We now give an overview of the most important experimental implementations of quantum sensors, following the summary in Table I.

# A. Neutral atoms as magnetic field sensors

Alkali atoms are suitable sensing qubits fulfilling the definitions in Sec. II (Kitching, Knappe, and Donley, 2011). Their ground state spin, a coupled angular momentum of electron and nuclear spin, can be both prepared and read out optically by the strong spin-selective optical dipole

transition linking their  $s$ -wave electronic ground state to the first  $(p$ -wave) excited state.

# 1. Atomic vapors

In the simplest implementation, a thermal vapor of atoms serves as a quantum sensor for magnetic fields (Kominis et al., 2003; Budker and Romalis, 2007). Held in a cell at or above room temperature, atoms are spin polarized by an optical pump beam. Magnetic field sensing is based on the Zeeman effect due to a small external field orthogonal to the initial atomic polarization. In a classical picture, this field induces coherent precession of the spin. Equivalently, in a quantum

TABLE I. Experimental implementations of quantum sensors.  

<table><tr><td>Implementation</td><td>Qubit(s)</td><td>Measured quantity(ies)</td><td>Typical frequency</td><td>Initialization</td><td>Readout</td><td>\( Type^a \)</td></tr><tr><td colspan="7">Neutral atoms</td></tr><tr><td>Atomic vapor</td><td>Atomic spin</td><td>Magnetic field, rotation, time/frequency</td><td>dc-GHz</td><td>Optical</td><td>Optical</td><td>II, III</td></tr><tr><td>Cold clouds</td><td>Atomic spin</td><td>Magnetic field, acceleration, time/frequency</td><td>dc-GHz</td><td>Optical</td><td>Optical</td><td>II, III</td></tr><tr><td colspan="7">Trapped ion(s)</td></tr><tr><td></td><td>Long-lived electronic state</td><td>Time/frequency</td><td>THz</td><td>Optical</td><td>Optical</td><td>II, III</td></tr><tr><td></td><td>Vibrational mode</td><td>Rotation</td><td>MHz</td><td>Optical</td><td>Optical</td><td>II</td></tr><tr><td colspan="7">Rydberg atoms</td></tr><tr><td></td><td>Rydberg states</td><td>Electric field</td><td>dc, GHz</td><td>Optical</td><td>Optical</td><td>II, III</td></tr><tr><td colspan="7">Solid-state spins (ensembles)</td></tr><tr><td>NMR sensors</td><td>Nuclear spins</td><td>Magnetic field</td><td>dc</td><td>Thermal</td><td>Pick-up coil</td><td>II</td></tr><tr><td>\( NV^b \) center ensembles</td><td>Electron spins</td><td>Magnetic field, electric field, temperature, pressure, rotation</td><td>dc-GHz</td><td>Optical</td><td>Optical</td><td>II</td></tr><tr><td colspan="7">Solid-state spins (single spins)</td></tr><tr><td>P donor in Si</td><td>Electron spin</td><td>Magnetic field</td><td>dc-GHz</td><td>Thermal</td><td>Electrical</td><td>II</td></tr><tr><td>Semiconductor quantum dots</td><td>Electron spin</td><td>Magnetic field, electric field</td><td>dc-GHz</td><td>Electrical, optical</td><td>Electrical, optical</td><td>I, II</td></tr><tr><td>Single \( NV^b \) center</td><td>Electron spin</td><td>Magnetic field, electric field, temperature, pressure, rotation</td><td>dc-GHz</td><td>Optical</td><td>Optical</td><td>II</td></tr><tr><td colspan="7">Superconducting circuits</td></tr><tr><td>\( SQUID^c \)</td><td>Supercurrent</td><td>Magnetic field</td><td>dc-GHz</td><td>Thermal</td><td>Electrical</td><td>I, II</td></tr><tr><td>Flux qubit</td><td>Circulating currents</td><td>Magnetic field</td><td>dc-GHz</td><td>Thermal</td><td>Electrical</td><td>II</td></tr><tr><td>Charge qubit</td><td>Charge eigenstates</td><td>Electric field</td><td>dc-GHz</td><td>Thermal</td><td>Electrical</td><td>II</td></tr><tr><td colspan="7">Elementary particles</td></tr><tr><td>Muon</td><td>Muon spin</td><td>Magnetic field</td><td>dc</td><td>Radioactive decay</td><td>Radioactive decay</td><td>II</td></tr><tr><td>Neutron</td><td>Nuclear spin</td><td>Magnetic field, phonon density, gravity</td><td>dc</td><td>Bragg scattering</td><td>Bragg scattering</td><td>II</td></tr><tr><td colspan="7">Other sensors</td></tr><tr><td>\( SET^d \)</td><td>Charge eigenstates</td><td>Electric field</td><td>dc-MHz</td><td>Thermal</td><td>Electrical</td><td>I</td></tr><tr><td>Optomechanics</td><td>Phonons</td><td>Force, acceleration, mass, magnetic field, voltage</td><td>kHz-GHz</td><td>Thermal</td><td>Optical</td><td>I</td></tr><tr><td>Interferometer</td><td>Photons, (atoms, molecules)</td><td>Displacement, refractive index</td><td>...</td><td></td><td></td><td>II, III</td></tr></table>

$^{\mathrm{a}}$ Sensor type refers to the three definitions of quantum sensing in Sec. II.A.  
$^{\mathrm{b}}$ NV: nitrogen vacancy.  
cSQUID: superconducting quantum interference device.  
$^{\mathrm{d}}$ SET: single electron transistor.

picture, it drives spin transitions from the initial quantum state to a distinct state, which can be monitored by a probe beam, e.g., via the optical Faraday effect. Despite their superficial simplicity, these sensors achieve sensitivities in the range of  $100\mathrm{aT} / \sqrt{\mathrm{Hz}}$  (Dang, Maloof, and Romalis, 2010) and approach a theory limit of  $< 10\mathrm{aT} / \sqrt{\mathrm{Hz}}$ , placing them on par with superconducting quantum interference devices (SQUIDs) as the most sensitive magnetometers to date. This is owing to the surprising fact that relaxation and coherence times of spins in atomic vapors can be pushed to the second to minute range (Balabas et al., 2010). These long relaxation and coherence times are achieved by coating cell walls to preserve the atomic spin upon collisions and by operating in the spin exchange relaxation-free (SERF) regime of high atomic density and zero magnetic field. Somewhat counterintuitively, a high density suppresses decoherence from atomic interactions, since collisions occur so frequently that their effect averages out, similar to motional narrowing of dipolar interactions in nuclear magnetic resonance (Happer and Tang, 1973). Vapor cells have been miniaturized to a few  $\mathrm{mm}^3$  small volumes (Shah et al., 2007) and have been used to demonstrate entanglement-enhanced sensing (Fernholz et al., 2008; Wasilewski et al., 2010). The most advanced application of vapor cells is arguably the detection of neural activity (Livanov et al., 1978; Jensen et al., 2016), which has found use in magnetoencephalography (Xia et al., 2006). Vapor cells also promise complementary access to high-energy physics, detecting anomalous dipole moments from coupling to exotic elementary particles and background fields beyond the standard model (Smiciklas et al., 2011; Pustelny et al., 2013; Swallows et al., 2013).

# 2. Cold atomic clouds

The advent of laser cooling in the 1980s spawned a revolution in atomic sensing. The reduced velocity spread of cold atoms enabled sensing with longer interrogation times using spatially confined atoms, freely falling along specific trajectories in vacuum or trapped.

Freely falling atoms have enabled the development of atomic gravimeters (Kasevich and Chu, 1992; Peters, Chung, and Chu, 1999) and gyrometers (Gustavson, Bouyer, and Kasevich, 1997; Gustavson, Landragin, and Kasevich, 2000). In these devices an atomic cloud measures acceleration by sensing the spatial phase shift of a laser beam along its freely falling trajectory.

Trapped atoms have been employed to detect and image magnetic fields at the microscale, by replicating Larmor precession spectroscopy on a trapped Bose-Einstein condensate (Vengalattore et al., 2007) and by direct driving of spin-flip transitions by microwave currents (Ockeloen et al., 2013) or thermal radiofrequency noise in samples (Fortagh et al., 2002; Jones et al., 2003). Sensing with cold atoms has found application in solid-state physics by elucidating current transport in microscopic conductors (Aigner et al., 2008).

Arguably the most advanced demonstrations of entanglement-enhanced quantum sensing (definition III) have been implemented in trapped cold atoms and vapor cells. Entanglement, in the form of spin squeezing (Wineland et al., 1992), has been produced by optical nondestructive

measurements of atomic population (Appel et al., 2009; Leroux, Schleier-Smith, and Vuletic, 2010a; Louchet-Chauvet et al., 2010; Schleier-Smith, Leroux, and Vuletic, 2010b; Bohnet et al., 2014; Cox et al., 2016; Hosten, Engelsen et al., 2016) and atomic interactions (Esteve et al., 2008; Riedel et al., 2010). It has improved the sensitivity of magnetometry devices beyond the shot-noise limit (Sewell et al., 2012; Ockeloen et al., 2013) and has increased their bandwidth (Shah, Vasilakis, and Romalis, 2010).

# B. Trapped ions

Ions, trapped in vacuum by electric or magnetic fields, have equally been explored as quantum sensors. The most advanced applications employ the quantized motional levels as sensing qubits for electric fields and forces. These levels are strongly coupled to the electric field by dipole-allowed transitions and sufficiently (MHz) spaced to be prepared by Raman cooling and read out by laser spectroscopy. The sensor has a predicted sensitivity of  $500\mathrm{nV / m / \sqrt{Hz}}$  or  $1\mathrm{yN} / \sqrt{\mathrm{Hz}}$  for the force acting on the ion (Maiwald et al., 2009; Biercuk et al., 2010). Trapped ions have been extensively used to study electric field noise above surfaces (Brownnutt et al., 2015), which could arise from charge fluctuations induced by adsorbents. Electrical field noise is a severe source of decoherence for ion traps and superconducting quantum processors (Labaziewicz et al., 2008) and a key limiting factor in ultrasensitive force microscopy (Kuehn, Loring, and Marohn, 2006; Tao and Degen, 2015).

Independently, the ground state spin sublevels of ions are magnetic-field-sensitive qubits analogous to neutral atoms discussed previously (Maiwald et al., 2009; Kotler et al., 2011; Baumgart et al., 2016). Being an extremely clean system, trapped ions have demonstrated sensitivities down to  $4.6\mathrm{pT} / \sqrt{\mathrm{Hz}}$  (Baumgart et al., 2016) and served as a test bed for advanced sensing protocols such as dynamical decoupling (Biercuk et al., 2009; Kotler et al., 2011) and entanglement-enhanced sensing (Leibfried et al., 2004). Recently, trapped ions have also been proposed as rotation sensors, via matter-wave Sagnac interferometry (Campbell and Hamilton, 2017). Their use in practical applications, however, has proven difficult. Practically all sensing demonstrations have focused on single ions, which, in terms of absolute sensitivity, cannot compete with ensemble sensors such as atomic vapors. Their small size could compensate for this downside in applications such as microscopy, where high spatial resolution is required. However, operation of ion traps in close proximity to surfaces remains a major challenge. Recent work on large ion crystals (Arnold et al., 2015; Drewsen, 2015; Bohnet et al., 2016) opens however the potential for novel applications to precise clocks and spectroscopy.

# C. Rydberg atoms

Rydberg atoms, atoms in highly excited electronic states, are remarkable quantum sensors for electric fields for a similar reason as trapped ions: In a classical picture, the loosely confined electron in a highly excited orbit is easily displaced by electric fields. In a quantum picture, its motional states are coupled by strong electric dipole transitions and experience

strong Stark shifts (Herrmann et al., 1986; Osterwalder and Merkt, 1999). Preparation and readout of states is possible by laser excitation and spectroscopy.

As their most spectacular sensing application, Rydberg atoms in vacuum have been employed as single-photon detectors for microwave photons in a cryogenic cavity in a series of experiments that was highlighted by the Nobel prize in physics in 2012 (Nogues et al., 1999; Gleyzes et al., 2007; Haroche, 2013). Their sensitivity was recently improved by employing Schrödinger cat states to reach a level of  $300\mathrm{nV} / (\mathrm{m} / \sqrt{\mathrm{Hz}})$  (Facon et al., 2016).

Recently, Rydberg states have become accessible in atomic vapor cells (Kübler et al., 2010). They have been applied to sense weak electric fields, mostly in the GHz frequency range (Sedlacek et al., 2012; Fan et al., 2015), and have been suggested as a candidate for a primary traceable standard of microwave power.

# D. Atomic clocks

At first sight atomic clocks, qubits with transitions so insensitive that their level splitting can be regarded as absolute and serve as a frequency reference, do not seem to qualify as quantum sensors since this very definition violates criterion (4). Their operation as clocks, however, employs identical protocols as the operation of quantum sensors, in order to repeatedly compare the qubit's transition to the frequency of an unstable local oscillator and subsequently lock the latter to the former. Therefore, an atomic clock can be equally regarded as a quantum sensor measuring and stabilizing the phase drift of a local oscillator. Vice versa, quantum sensors discussed previously can be regarded as clocks that operate on purpose on a bad, environment-sensitive clock transition in order to measure external fields.

Today's most advanced atomic clocks employ optical transitions in single ions (Huntemann et al., 2016) or atomic clouds trapped in an optical lattice (Takamoto et al., 2005; Hinkley et al., 2013; Bloom et al., 2014). Interestingly, even entanglement-enhanced sensing has found use in actual devices, since some advanced clocks employ multiqubit quantum logic gates for readout of highly stable but optically inactive clock ions (Schmidt et al., 2005; Rosenband et al., 2008).

# E. Solid-state spins: Ensemble sensors

# 1. NMR ensemble sensors

Some of the earliest quantum sensors have been based on ensembles of nuclear spins. Magnetic field sensors have been built that infer field strength from their Larmor precession, analogous to neutral atom magnetometers described previously (Packard and Varian, 1954; Waters and Francis, 1958; Kitching, Knappe, and Donley, 2011). Initialization of spins is achieved by thermalization in an externally applied field, readout by induction detection. Although the sensitivity of these devices  $(10\mathrm{pT} / \sqrt{\mathrm{Hz}})$  (Lenz, 1990) is inferior to their atomic counterparts, they have found broad use in geology, archaeology, and space missions thanks to their simplicity and robustness. More recently, nuclear magnetic resonance (NMR) sensor probes have been developed for in situ and

dynamical field mapping in clinical magnetic resonance imaging (MRI) systems (Zanche et al., 2008).

Spin ensembles have equally served as gyroscopes (Woodman, Franks, and Richards, 1987; Fang and Qin, 2012), exploiting the fact that Larmor precession occurs in an independent frame of reference and therefore appears frequency shifted in a rotating laboratory frame. In the most advanced implementation, nuclear spin precession is read out by an atomic magnetometer, which is equally used for compensation of the Zeeman shift (Kornack, Ghosh, and Romalis, 2005). These experiments reached a sensitivity of  $5 \times 10^{-7} \mathrm{rad} / (\mathrm{s} / \sqrt{\mathrm{Hz}})$ , which is comparable to compact implementations of atomic interferometers and optical Sagnac interferometers.

# 2. NV center ensembles

Much excitement has recently been sparked by ensembles of nitrogen-vacancy centers (NV centers), electronic spin defects in diamond that can be optically initialized and read out. Densely doped diamond crystals promise to deliver "frozen vapor cells" of spin ensembles that combine the strong (electronic) magnetic moment and efficient optical readout of atomic vapor cells with the high spin densities achievable in the solid state. Although these advantages are partially offset by a reduced coherence time ( $T_{2} < 1$  ms at room temperature, as compared to  $T_{2} > 1$  s for vapor cells), the predicted sensitivity of diamond magnetometers [250 aT/( $\sqrt{\mathrm{Hz}}/\mathrm{cm}^{-3/2}$ )] (Taylor et al., 2008) or gyroscopes  $[10^{-5}(\mathrm{rad/s})/( \sqrt{\mathrm{Hz}}/\mathrm{mm}^{3/2})]$  (Ajoy and Cappellaro, 2012; Ledbetter et al., 2012) would be competitive with their atomic counterparts.

Translation of this potential into actual devices remains challenging, with two technical hurdles standing out. First, efficient fluorescence detection of large NV ensembles is difficult, while absorptive and dispersive schemes are not easily implemented (Le Sage et al., 2012; Jensen et al., 2014; Clevenson et al., 2015). Second, spin coherence times are reduced 100-1000 times in high-density ensembles owing to interaction of NV spins with parasitic substitutional nitrogen spins incorporated during high-density doping (Acosta et al., 2009). As a consequence, even the most advanced devices are currently limited to  $\sim 1\mathrm{pT} / \sqrt{\mathrm{Hz}}$  (Wolf et al., 2015) and operate several orders of magnitude above the theory limit. As a technically less demanding application, NV centers in a magnetic field gradient have been employed as spectrum analyzer for high-frequency microwave signals (Chipaux et al., 2015).

While large-scale sensing of homogeneous fields remains a challenge, micrometer-sized ensembles of NV centers have found application in imaging applications, serving as detector pixels for microscopic mapping of magnetic fields. Most prominently, this line of research has enabled imaging of magnetic organelles in magnetotactic bacteria (Le Sage et al., 2013) and microscopic magnetic inclusions in meteorites (Fu et al., 2014), as well as contrast-agent-based magnetic resonance microscopy (Steinert et al., 2013).

# F. Solid-state spins: Single-spin sensors

Readout of single spins in the solid state, a major milestone on the road toward quantum computers, has been achieved by

both electrical and optical schemes. Electrical readout has been demonstrated with phosphorus dopants in silicon (Morello et al., 2010) and electrostatically defined semiconductor quantum dots (Elzerman et al., 2004). Optical readout was shown with single organic molecules (Wrachtrup et al., 1993a, 1993b), optically active quantum dots (KROUTvar et al., 2004; Atature et al., 2007; Vamivakas et al., 2010), and defect centers in crystalline materials including diamond (Gruber et al., 1997) and silicon carbide (Christle et al., 2015; Widmann et al., 2015). In addition, mechanical detection of single paramagnetic defects in silica (Rugar et al., 2004) and real-time monitoring of few-spin fluctuations (Budakian et al., 2005) have been demonstrated.

Among all solid-state spins, NV centers in diamond have received by far the most attention for sensing purposes. This is in part due to the convenient room-temperature optical detection, and in part due to their stability in very small crystals and nanostructures. The latter permits use of NV centers as sensors in high-resolution scanning probe microscopy (Chernobrod and Berman, 2005; Balasubramanian et al., 2008; Degen, 2008), as biomarkers within living organisms (Fu et al., 2007), or as stationary probes close to the surface of diamond sensor chips. Quantum sensing with NV centers has been considered in several recent focused reviews (Rondin et al., 2014; Schirhagl et al., 2014).

Single NV centers have been employed and/or proposed as sensitive magnetometers (Balasubramanian et al., 2008; Degen, 2008; Maze et al., 2008; Taylor et al., 2008; Cole and Hollenberg, 2009), electrometers (Dolde et al., 2011), pressure sensors (Doherty et al., 2014), and thermometers (Hodges et al., 2013; Kucsko et al., 2013; Neumann et al., 2013; Toyli et al., 2013), using the Zeeman, Stark, and temperature shifts of their spin sublevels. The most advanced nanosensing experiments in terms of sensitivity have employed near-surface NV centers in bulk diamond crystals. This approach has enabled sensing of nanometer-sized voxels of nuclear or electronic spins deposited on the diamond surface (Mamin et al., 2013; Staudacher et al., 2013; Loretz et al., 2014; Sushkov, Lovchinsky et al., 2014; DeVience et al., 2015; Shi et al., 2015; Lovchinsky et al., 2016), of distant nuclear spin clusters (Shi et al., 2014), and of 2D materials (Lovchinsky et al., 2017). Other applications included the study of ballistic transport in the Johnson noise of nanoscale conductors (Kolkowitz et al., 2015), phases, and phase transitions of skyrmion materials (Dovzhenko et al., 2016; Dussaux et al., 2016), as well as of spin waves (Wolfe et al., 2014; van der Sar et al., 2015), and relaxation in nanomagnets (Schafer-Nolte et al., 2014; Schmid-Lorch et al., 2015).

Integration of NV centers into scanning probes has enabled imaging of magnetic fields with sub-100 nm resolution, with applications to nanoscale magnetic structures and domains (Balasubramanian et al., 2008; Maletinsky et al., 2012; Rondin et al., 2012), vortices and domain walls (Rondin et al., 2013; Tetienne et al., 2014, 2015), superconducting vortices (Pellicione et al., 2016; Thiel et al., 2016), and mapping of currents (Chang et al., 2017).

NV centers in  $\sim 10$ -nm-sized nanodiamonds have also been inserted into living cells. They have been employed for particle tracking (McGuinness et al., 2011) and in vivo temperature measurements (Kucsko et al., 2013; Neumann

et al., 2013; Toyli et al., 2013) and could enable real-time monitoring of metabolic processes.

# G. Superconducting circuits

# 1. SQUID

The SQUID is simultaneously one of the oldest and one of the most sensitive types of magnetic sensor (Jaklevic et al., 1965; Clarke and Braginski, 2004; Fagaly, 2006). These devices, interferometers of superconducting conductors, measure magnetic fields with a sensitivity down to  $10\mathrm{aT} / \sqrt{\mathrm{Hz}}$  (Simmonds, Fertig, and Giffard, 1979). Their sensing mechanism is based on the Aharonov-Bohm phase imprinted on the superconducting wave function by an encircled magnetic field, which is read out by a suitable circuit of phase-sensitive Josephson junctions.

From a commercial perspective, SQUIDs can be considered the most advanced type of quantum sensor, with applications ranging from materials characterization in solid-state physics to clinical magnetoencephalography systems for measuring small ( $\sim 100$  fT) stray fields of electric currents in the brain. In parallel to the development of macroscopic (mm-cm) SQUID devices, miniaturization has given birth to submicron sized "nanoSQUIDs" with possible applications in nanoscale magnetic, current, and thermal imaging (Vasyukov et al., 2013; Halbertal et al., 2016). Note that because SQUIDs rely on spatial rather than temporal coherence, they are more closely related to optical interferometers than to the spin sensors discussed previously.

SQUIDs have been employed to process signals from the dc up to the GHz range (Mück, Welzel, and Clarke, 2003; Hatridge et al., 2011), the upper limit being set by the Josephson frequency. Conceptually similar circuits, dedicated to amplification of GHz frequency signals, have been explored in great detail in the past decade (Castellanos-Beltran et al., 2008; Bergeal et al., 2010; Ho Eom et al., 2012; Macklin et al., 2015). Arguably the most widely studied design is the Josephson parametric amplifier, which has been pushed to a nearly quantum-limited input noise level of only a few photons and is now routinely used for spectroscopic single shot readout of superconducting qubits (Vijay, Slichter, and Siddiqi, 2011).

# 2. Superconducting qubits

Temporal quantum superpositions of supercurrents or charge eigenstates have become accessible in superconducting qubits (Nakamura, Pashkin, and Tsai, 1999; Martinis et al., 2002; Vion et al., 2002; Wallraff et al., 2004; Clarke and Wilhelm, 2008). Being associated with large magnetic and electric dipole moments, they are attractive candidates for quantum sensing. Many of the established quantum sensing protocols to be discussed in Secs. IV-VII have been implemented with superconducting qubits. Specifically, noise in these devices has been thoroughly studied from the sub-Hz to the GHz range, using Ramsey interferometry (Yoshihara et al., 2006; Yan et al., 2012), dynamical decoupling (Nakamura, Pashkin, and Tsai, 2002; Ithier et al., 2005; Yoshihara et al., 2006; Bylander et al., 2011; Yan et al., 2013), and  $T_{1}$  relaxometry (Astafiev et al., 2004; Yoshihara et al., 2006). These studies have been extended

to discern charge from flux noise by choosing qubits with a predominant electric (charge qubit) or magnetic (flux qubit) dipole moment, or by tuning bias parameters in situ (Bialczak et al., 2007; Yan et al., 2012). Operating qubits as magnetic field sensors, very promising sensitivities  $(3.3\mathrm{pT} / \sqrt{\mathrm{Hz}}$  for operation at  $10\mathrm{MHz}$ ) were demonstrated (Bal et al., 2012). Extending these experiments to the study of extrinsic samples appears simultaneously attractive and technically challenging, since superconducting qubits have to be cooled to temperatures of only a few tens of millikelvin.

# H. Elementary particle qubits

Interestingly, elementary particles have been employed as quantum sensors long before the development of atomic and solid-state qubits. This somewhat paradoxical fact is owing to their straightforward initialization and readout, as well as their targeted placement in relevant samples by irradiation with a particle beam.

# 1. Muons

Muons are frequently described as close cousins of electrons. Both particles are leptons, carry an elementary charge, and have a spin that can be employed for quantum sensing. Sensing with muons has been termed "muon spin rotation"  $(\mu \mathrm{SR})$ . It employs antimuons  $(\mu^{+})$  that are deterministically produced by proton-proton collisions, from decay of an intermediate positive pion by the reaction  $\pi^{+} \rightarrow \mu^{+} + \nu_{\mu}$ . Here parity violation of the weak interaction automatically initializes the muon spin to be collinear with the particle's momentum. Readout of the spin is straightforward by measuring the emission direction of positrons from the subsequent decay  $\mu^{+} \rightarrow e^{+} + \nu_{e} + \bar{\nu}_{\mu}$ , which are preferably emitted along the muon spin (Brewer and Crowe, 1978; Blundell, 1999).

Crucially, muons can be implanted into solid-state samples and serve as local probes of their nanoscale environment for their few microseconds long lifetime. Larmor precession measurements have been used to infer the intrinsic magnetic field of materials. Despite its exotic nature, the technique of  $\mu \mathrm{SR}$  has become and remained a workhorse tool of solid-state physics. In particular, it is a leading technique to measure the London penetration depth of superconductors (Sonier, Brewer, and Kiefl, 2000).

# 2. Neutrons

Slow beams of thermal neutrons can be spin polarized by Bragg reflection on a suitable magnetic crystal. Spin readout is feasible by a spin-sensitive Bragg analyzer and subsequent detection. Spin rotations (single qubit gates) are easily implemented by application of localized magnetic fields along parts of the neutron's trajectory. As a consequence, many early demonstrations of quantum effects, such as the direct measurement of Berry's phase (Bitter and Dubbers, 1987), have employed neutrons.

Sensing with neutrons has been demonstrated in multiple ways. Larmor precession in the magnetic field of samples has been employed for three-dimensional tomography (Kardjilov et al., 2008). Neutron interferometry has put limits on the

strongly coupled chameleon field (Li et al., 2016). Ultracold neutrons have been employed as a probe for gravity on small length scales in a series of experiments termed "qBounce." These experiments exploit the fact that suitable materials perfectly reflect the matter wave of sufficiently slow neutrons so that they can be trapped above a bulk surface by the gravity of Earth as a "quantum bouncing ball" (Nesvizhevsky et al., 2002). The eigenenergies of this anharmonic trap depend on gravity and have been probed by quantum sensing techniques (Jenke et al., 2011, 2014).

The most established technique, neutron spin echo, can reveal materials properties by measuring small (down to  $\mathrm{neV}$ ) energy losses of neutrons in inelastic scattering events (Mezei, 1972). Here the phase of the neutron spin, coherently precessing in an external magnetic field, serves as a clock to measure a neutron's time of flight. Inelastic scattering in a sample changes a neutron's velocity, resulting in a different time of flight to and from a sample of interest. This difference is imprinted in the spin phase by a suitable quantum sensing protocol, specifically a Hahn echo sequence whose  $\pi$  pulse is synchronized with passage through the sample.

# I. Other sensors

In addition to the many implementations of quantum sensors already discussed, three further systems deserved special attention for their future potential or for their fundamental role in developing quantum sensing methodology.

# 1. Single electron transistors

Single electron transistors (SETs) sense electric fields by measuring the tunneling current across a submicron conducting island sandwiched between a tunneling source and drain contacts. In the "Coulomb blockade regime" of sufficiently small (typically  $\approx 100\mathrm{nm}$ ) islands, tunneling across the device is allowed only if charge eigenstates of the island lie in the narrow energy window between the Fermi level of source and drain contact. The energy of these eigenstates is highly sensitive to even weak external electric fields, resulting in a strongly field-dependent tunneling current (Kastner, 1992; Yoo et al., 1997; Schoelkopf, 1998). SETs have been employed as scanning probe sensors to image electric fields on the nanoscale, shedding light on a variety of solid-state phenomena such as the fractional quantum Hall effect or electron-hole puddles in graphene (Ilani et al., 2004; Martin et al., 2008). In a complementary approach, charge sensing by stationary SETs has enabled readout of optically inaccessible spin qubits such as phosphorus donors in silicon (Morello et al., 2010) based on counting of electrons (Bylander, Duty, and Delsing, 2005).

# 2. Optomechanics

Phonons, discrete quantized energy levels of vibration, have recently become accessible at the "single-particle" level in the field of optomechanics (O'Connell et al., 2010; Aspelmeyer, Kippenberg, and Marquardt, 2014), which studies high-quality mechanical oscillators that are strongly coupled to light.

While preparation of phonon number states and their coherent superpositions remains difficult, the devices built to achieve these goals have shown great promise for sensing applications. This is mainly due to the fact that mechanical degrees of freedom strongly couple to nearly all external fields, and that strong optical coupling enables efficient actuation and readout of mechanical motion. Specifically, optomechanical sensors have been employed to detect minute forces  $(12\mathrm{zN} / \sqrt{\mathrm{Hz}})$  (Moser et al., 2013), acceleration  $(100\mathrm{ng} / \sqrt{\mathrm{Hz}})$  (Krause et al., 2012; Cervantes et al., 2014), masses  $(2\mathrm{yg} / \sqrt{\mathrm{Hz}})$  (Chaste et al., 2012), magnetic fields  $(200\mathrm{pT} / \sqrt{\mathrm{Hz}})$  (Forstner et al., 2014), spins (Rugar et al., 2004; Degen et al., 2009), and voltage  $(5\mathrm{pV} / \sqrt{\mathrm{Hz}})$  (Bagci et al., 2014). While these demonstrations have remained at the level of classical sensing in the sense of this review, their future extension to quantum-enhanced measurements appears most promising.

# 3. Photons

While this review does not discuss quantum sensing with photons, due to the breadth of the subject, several fundamental paradigms have been pioneered with optical sensors including light squeezing and photonic quantum correlations. These constitute examples of quantum-enhanced sensing according to our definition III.

Squeezing of light, the creation of partially entangled states with phase or amplitude fluctuations below those of a classical coherent state of the light field, has been proposed (Caves, 1981) and achieved (Slusher et al., 1985) long before squeezing of spin ensembles (Wineland et al., 1992; Hald et al., 1999). Vacuum squeezed states have meanwhile been employed to improve the sensitivity of gravitational wave detectors. In the GEO gravitational wave detector, squeezing has enhanced the shot-noise limited sensitivity by  $3.5\mathrm{dB}$  (LIGO Collaboration, 2011); in a proof-of-principle experiment in the LIGO gravitational wave detector, the injection of  $10\mathrm{dB}$  of squeezing lowered the shot noise in the interferometer output by approximately  $2.15\mathrm{dB}$ $(28\%)$  (Aasi et al., 2013), equivalent to an increase by more than  $60\%$  in the power stored in the interferometer arm cavities. Further upgrades associated with advanced LIGO could bring down the shot noise by  $6\mathrm{dB}$ , via frequency dependent squeezing (Oelker et al., 2016).

In addition, quantum correlations between photons have proven to be a powerful resource for imaging. This has been noted very early on in the famous Hanbury Brown-Twiss experiment, where bunching of photons is employed to filter atmospheric aberrations and to perform "superresolution" measurements of stellar diameters smaller than the diffraction limit of the telescope employed (Hanbury Brown and Twiss, 1956). While this effect can still be accounted for classically, a recent class of experiments has exploited nonclassical correlations to push the spatial resolution of microscopes below the diffraction limit (Schwartz et al., 2013). Vice versa, multiphoton correlations have been proposed and employed to create light patterns below the diffraction limit for superresolution lithography (Boto et al., 2000; D'Angelo, Chekhova, and Shih, 2001). They can equally improve image contrast rather than resolution by a scheme known as "quantum illumination" (Lloyd, 2008; Tan et al., 2008;

Lopaeva et al., 2013). Here a beam of photons is employed to illuminate an object, reflected light being detected as the imaging signal. Entangled twins of the illumination photons are conserved at the source and compared to reflected photons by a suitable joint measurement. In this way, photons can be certified to be reflected light rather than noise, enhancing imaging contrast. In simpler schemes, intensity correlations between entangled photons have been employed to boost contrast in transmission microscopy of weakly absorbing objects (Brida, Genovese, and Berchera, 2010) and the reduced quantum fluctuations of squeezed light have been used to improve optical particle tracking (Taylor et al., 2013).

The most advanced demonstrations of entanglement-enhanced sensing have been performed with single photons or carefully assembled few-photon Fock states. Most prominently, these include Heisenberg-limited interferometers (Holland and Burnett, 1993; Mitchell, Lundeen, and Steinberg, 2004; Walther et al., 2004; Higgins et al., 2007; Nagata et al., 2007). In these devices, entanglement between photons or adaptive measurements are employed to push sensitivity beyond the  $1 / \sqrt{N}$  scaling of a classical interferometer where  $N$  is the number of photons (see Sec. IX).

# IV. THE QUANTUM SENSING PROTOCOL

In this section, we describe the basic methodology for performing measurements with quantum sensors. Our discussion will focus on a generic scheme where a measurement consists of three elementary steps: the initialization of the quantum sensor, the interaction with the signal of interest, and the readout of the final state. Phase estimation (Shor, 1994; Kitaev, 1995) and parameter estimation (Braunstein and Caves, 1994; Braunstein, Caves, and Milburn, 1996; Goldstein, Lukin, and Cappellaro, 2010) techniques are then used to reconstruct the physical quantity from a series of measurements. Experimentally, the protocol is typically implemented as an interference measurement using pump-probe spectroscopy, although other schemes are possible. The key quantity is then the quantum phase picked up by the quantum sensor due to the interaction with the signal. The protocol can be optimized for detecting weak signals or small signal changes with the highest possible sensitivity and precision.

# A. Quantum sensor Hamiltonian

For the following discussion, we assume that the quantum sensor can be described by the generic Hamiltonian

$$
\hat {H} (t) = \hat {H} _ {0} + \hat {H} _ {V} (t) + \hat {H} _ {\text {c o n t r o l}} (t), \tag {2}
$$

where  $\hat{H}_0$  is the internal Hamiltonian,  $\hat{H}_V(t)$  is the Hamiltonian associated with a signal  $V(t)$ , and  $\hat{H}_{\mathrm{control}}(t)$  is the control Hamiltonian. We assume that  $\hat{H}_0$  is known and that  $\hat{H}_{\mathrm{control}}(t)$  can be deliberately chosen so as to manipulate or tune the sensor in a controlled way. The goal of a quantum sensing experiment is then to infer  $V(t)$  from the effect it has on the qubit via its Hamiltonian  $\hat{H}_V(t)$ , usually by a clever choice of  $\hat{H}_{\mathrm{control}}(t)$ .

# 1. Internal Hamiltonian

$\hat{H}_0$  describes the internal Hamiltonian of the quantum sensor in the absence of any signal. Typically, the internal Hamiltonian is static and defines the energy eigenstates  $|0\rangle$  and  $|1\rangle$ ,

$$
\hat {H} _ {0} = E _ {0} | 0 \rangle \langle 0 | + E _ {1} | 1 \rangle \langle 1 |, \tag {3}
$$

where  $E_0$  and  $E_1$  are the eigenenergies and  $\omega_0 = E_1 - E_0$  is the transition energy between the states  $(\hbar = 1)$ . Note that the presence of an energy splitting  $\omega_0 \neq 0$  is not necessary, but it represents the typical situation for most implementations of quantum sensors. The qubit internal Hamiltonian may contain additional interactions that are specific to a quantum sensor, such as couplings to other qubits. In addition, the internal Hamiltonian contains time-dependent stochastic terms due to a classical environment or interactions with a quantum bath that are responsible for decoherence and relaxation.

# 2. Signal Hamiltonian

The signal Hamiltonian  $\hat{H}_V(t)$  represents the coupling between the sensor qubit and a signal  $V(t)$  to be measured. When the signal is weak (which is assumed here)  $\hat{H}_V(t)$  adds a small perturbation to  $\hat{H}_0$ . The signal Hamiltonian can then be separated into two qualitatively different contributions

$$
\hat {H} _ {V} (t) = \hat {H} _ {V _ {\parallel}} (t) + \hat {H} _ {V _ {\perp}} (t), \tag {4}
$$

where  $\hat{H}_{V_{\parallel}}$  is the parallel (commuting, secular) and  $\hat{H}_{V_{\perp}}$  the transverse (noncommuting) components, respectively. The two components can quite generally be captured by

$$
\hat {H} _ {V _ {\parallel}} (t) = \frac {1}{2} \gamma V _ {\parallel} (t) \left\{ \right.\left| \right. 1 \left. \right\rangle \langle 1 \left. \right| - \left| \right. 0 \left. \right\rangle \langle 0 \mid \left. \right\}, \tag {5}
$$

$$
\hat {H} _ {V _ {\perp}} (t) = \frac {1}{2} \gamma \left\{V _ {\perp} (t) | 1 \rangle \langle 0 | + V _ {\perp} ^ {\dagger} (t) | 0 \rangle \langle 1 | \right\},
$$

where  $V_{\parallel}(t)$  and  $V_{\perp}(t)$  are functions with the same units of  $V(t)$ .  $\gamma$  is the coupling or transduction parameter of the qubit to the signal  $V(t)$ . Examples of coupling parameters include the Zeeman shift parameter (gyromagnetic ratio) of spins in a magnetic field, with units of  $\mathrm{Hz / T}$ , or the linear Stark shift parameter of electric dipoles in an electric field, with units of  $\mathrm{Hz / (Vm^{-1})}$ . Although the coupling is often linear, this is not required. In particular, the coupling is quadratic for second-order interactions (such as the quadratic Stark effect) or when operating the quantum sensor in variance detection mode (see Sec. IV.E.2).

The parallel and transverse components of a signal have distinctly different effects on the quantum sensor. A commuting perturbation  $\hat{H}_{V_{\parallel}}$  leads to shifts of the energy levels and an associated change of the transition frequency  $\omega_0$ . A noncommuting perturbation  $\hat{H}_{V_{\perp}}$ , by contrast, can induce transitions between levels, manifesting through an increased transition rate  $\Gamma$ . Most often, this requires the signal to be time dependent (resonant with the transition) in order to have an appreciable effect on the quantum sensor.

An important class of signals are vector signal  $\vec{V} (t)$ , in particular, those provided by electric or magnetic fields. The

interaction between a vector signal  $\vec{V}(t) = \{V_x, V_y, V_z\}(t)$  and a qubit can be described by the signal Hamiltonian

$$
\hat {H} _ {V} (t) = \gamma \vec {V} (t) \cdot \hat {\vec {\sigma}}, \tag {6}
$$

where  $\vec{\sigma} = \{\sigma_x,\sigma_y,\sigma_z\}$  is a vector of Pauli matrices. For a vector signal, the two signal functions  $V_{\parallel}(t)$  and  $V_{\perp}(t)$  are

$$
V _ {\parallel} (t) = V _ {z} (t),
$$

$$
V _ {\perp} (t) = V _ {x} (t) + i V _ {y} (t), \tag {7}
$$

where the  $z$  direction is defined by the qubit's quantization axis. The corresponding signal Hamiltonian is

$$
\hat {H} _ {V} (t) = \gamma \operatorname {R e} [ V _ {\perp} (t) ] \hat {\sigma} _ {x} + \gamma \operatorname {I m} [ V _ {\perp} (t) ] \hat {\sigma} _ {y} + \gamma V _ {\parallel} (t) \hat {\sigma} _ {z}. \tag {8}
$$

# 3. Control Hamiltonian

For most quantum sensing protocols it is required to manipulate the qubit either before, during, or after the sensing process. This is achieved via a control Hamiltonian  $\hat{H}_{\mathrm{control}}(t)$  that allows implementing a standard set of quantum gates (Nielsen and Chuang, 2000). The most common gates in quantum sensing include the Hadamard gate and the Pauli  $X$  and  $Y$  gates, or equivalently a set of  $\pi /2$  and  $\pi$  rotations (pulses) around different axes. Advanced sensing schemes employing more than one sensor qubit may further require conditional gates, especially controlled-NOT gates to generate entanglement, swap gates to exploit memory qubits, and controlled phase shifts in quantum phase estimation. Finally, the control Hamiltonian can include control fields for systematically tuning the transition frequency  $\omega_0$ . This capability is frequently exploited in noise spectroscopy experiments.

# B. The sensing protocol

Quantum sensing experiments typically follow a generic sequence of sensor initialization, interaction with the signal, sensor readout, and signal estimation. This sequence can be summarized in the following basic protocol, which is also sketched in Fig. 2:

(1) The quantum sensor is initialized into a known basis state, for example,  $|0\rangle$  
(2) The quantum sensor is transformed into the desired initial sensing state  $|\psi_0\rangle = \hat{U}_a|0\rangle$ . The transformation can be carried out using a set of control pulses represented by the propagator  $\hat{U}_a$ . In many cases,  $|\psi_0\rangle$  is a superposition state.  
(3) The quantum sensor evolves under the Hamiltonian  $\hat{H}$  [Eq. (2)] for a time  $t$ . At the end of the sensing period, the sensor is in the final sensing state

$$
| \psi (t) \rangle = \hat {U} _ {H} (0, t) | \psi_ {0} \rangle = c _ {0} | \psi_ {0} \rangle + c _ {1} | \psi_ {1} \rangle , \tag {9}
$$

where  $\hat{U}_H(0,t)$  is the propagator of  $\hat{H}$ ,  $|\psi_1\rangle$  is the state orthogonal to  $|\psi_0\rangle$ , and  $c_{0}, c_{1}$  are complex coefficients.

![](images/da65c212d4aa9849128eab1fbda2d512458c31267fa5f636280a9cbec3681a9d.jpg)  
FIG. 2. Basic steps of the quantum sensing process.

(4) The quantum sensor is transformed into a superposition of observable readout states  $|\alpha \rangle = \hat{U}_b|\psi (t)\rangle = c_0^\prime |0'\rangle +c_1^\prime |1'\rangle$ . For simplicity we assume that the initialization basis  $\{|0\rangle ,|1\rangle \}$  and the readout basis  $\{|0^{\prime}\rangle ,|1^{\prime}\rangle \}$  are the same and that  $\hat{U}_b = \hat{U}_a^\dagger$ , but this is not required. Under these assumptions, the coefficients  $c_{0}^{\prime}\equiv c_{0}$  and  $c_{1}^{\prime}\equiv c_{1}$  represent the overlap between the initial and final sensing states.  
(5) The final state of the quantum sensor is read out. We assume that the readout is projective, although more general positive-operator-valued-measure (POVM) measurements may be possible (Nielsen and Chuang, 2000). The projective readout is a Bernoulli process that yields an answer "0" with probability  $1 - p'$  and an answer "1" with probability  $p'$ , where  $p' = |c_1'|^2 \propto p$  is proportional to the measurable transition probability

$$
p = 1 - \left| c _ {0} \right| ^ {2} = \left| c _ {1} \right| ^ {2} \tag {10}
$$

that the qubit changed its state during  $t$ . The binary answer is detected by the measurement apparatus as a physical quantity  $x$ , for example, as a voltage, current, photon count, or polarization.

Steps 1-5 represent a single measurement cycle. Because step 5 gives a binary answer, the measurement cycle needs to be repeated many times in order to gain a precise estimate for  $p$ :

(6) Steps 1-5 are repeated and averaged over a large number of cycles  $N$  to estimate  $p$ . The repetition can be done by running the protocol sequentially on the same quantum system, or in parallel by averaging over an ensemble of  $N$  identical (and noninteracting) quantum systems.

Step 6 provides only one value for the transition probability  $p$ . While a single value of  $p$  may sometimes be sufficient to estimate a signal  $V$ , it is in many situations convenient or required to record a set of values  $\{p_k\}$ :

(7) The transition probability  $p$  is measured as a function of time  $t$  or of a parameter of the control Hamiltonian, and the desired signal  $V$  is inferred from the data record  $\{p_k\}$  using a suitable procedure.

More generally, a set of measurements can be optimized to efficiently extract a desired parameter from the signal Hamiltonian (see Sec. VIII). Most protocols presented in the following implicitly use such a strategy for gaining information about the signal.

Although this protocol is generic and simple, it is sufficient to describe most sensing experiments. For example, classical continuous-wave absorption and transmission spectroscopy can be considered as an averaged variety of this protocol. Also, the time evolution can be replaced by a spatial evolution to describe a classical interferometer.

To illustrate the protocol, we consider two elementary examples, one for detecting a parallel signal  $V_{\parallel}$  and one for detecting a transverse signal  $V_{\perp}$ . These examples will serve as the basis for the more refined sequences discussed in later sections.

# C. First example: Ramsey measurement

The first example is the measurement of the static energy splitting  $\omega_0$  (or equivalently, a static perturbation  $V_{\parallel}$ ). The canonical approach for this measurement is a Ramsey interferometry measurement (Lee, Kok, and Dowling, 2002; Taylor et al., 2008):

(1) The quantum sensor is initialized into  $|0\rangle$  
(2) Using a  $\pi / 2$  pulse, the quantum sensor is transformed into the superposition state

$$
\left| \psi_ {0} \right\rangle = | + \rangle \equiv \frac {1}{\sqrt {2}} (| 0 \rangle + | 1 \rangle). \tag {11}
$$

(3) The superposition state evolves under the Hamiltonian  $\hat{H}_0$  for a time  $t$ . The superposition state picks up the relative phase  $\phi = \omega_0 t$ , and the state after the evolution is

$$
| \psi (t) \rangle = \frac {1}{\sqrt {2}} (| 0 \rangle + e ^ {- i \omega_ {0} t} | 1 \rangle), \tag {12}
$$

up to an overall phase factor.

(4) Using a second  $\pi /2$  pulse, the state  $|\psi (t)\rangle$  is converted back to the measurable state

$$
| \alpha \rangle = \frac {1}{2} \left(1 + e ^ {- i \omega_ {0} t}\right) | 0 \rangle + \frac {1}{2} \left(1 - e ^ {- i \omega_ {0} t}\right) | 1 \rangle . \tag {13}
$$

(5) The final state is read out. The transition probability is

$$
\begin{array}{l} p = 1 - | \langle 0 | \alpha \rangle | ^ {2} \\ = \sin^ {2} \left(\omega_ {0} t / 2\right) = \frac {1}{2} \left[ 1 - \cos \left(\omega_ {0} t\right) \right]. \tag {14} \\ \end{array}
$$

By recording  $p$  as a function of time  $t$ , an oscillatory output ("Ramsey fringes") is observed with a frequency given by  $\omega_0$ . Thus, the Ramsey measurement can directly provide a measurement of the energy splitting  $\omega_0$ .

# D. Second example: Rabi measurement

The second elementary example is the measurement of the transition matrix element  $|V_{\perp}|$ :

(1) The quantum sensor is initialized into  $|\psi_0\rangle = |0\rangle$  
(3) In the absence of the internal Hamiltonian  $\hat{H}_0 = 0$  the evolution is given by  $\hat{H}_{V_{\perp}} = \frac{1}{2}\gamma V_{\perp}\sigma_{x} = \omega_{1}\sigma_{x},$  where  $\omega_{1}$  is the Rabi frequency. The state after evolution is

$$
\left| \psi (t) \right\rangle = | \alpha \rangle = \frac {1}{2} \left(1 + e ^ {- i \omega_ {1} t}\right) | 0 \rangle + \frac {1}{2} \left(1 - e ^ {- i \omega_ {1} t}\right) | 1 \rangle . \tag {15}
$$

(5), (6) The final state is read out. The transition probability is

$$
p = 1 - \left| \langle 0 | \alpha \rangle \right| ^ {2} = \sin^ {2} \left(\omega_ {1} t / 2\right). \tag {16}
$$

In a general situation where  $\hat{H}_0 \neq 0$ , the transition probability represents the solution to Rabi's original problem (Sakurai and Napolitano, 2011),

$$
p = \frac {\omega_ {1} ^ {2}}{\omega_ {1} ^ {2} + \omega_ {0} ^ {2}} \sin^ {2} \left(\sqrt {\omega_ {1} ^ {2} + \omega_ {0} ^ {2}} t\right). \tag {17}
$$

Hence, only time-dependent signals with frequency  $\omega \approx \omega_0$  affect the transition probability  $p$ , a condition known as resonance. From this condition it is clear that a Rabi measurement can provide information not only on the magnitude  $V_{\perp}$ , but also on the frequency  $\omega$  of a signal (Fedder et al., 2011; Aiello, Hirose, and Cappellaro, 2013).

# E. Slope and variance detection

A central objective of quantum sensing is the detection of small signals. For this purpose, it is advantageous to measure the deviation of the transition probability from a well-chosen reference point  $p_0$ , which we refer to as the bias point of the measurement, corresponding to a known value of the external signal  $V_{0}$  or reached by setting some additional parameters in the Hamiltonian under the experimenter's control. The quantity of interest is then the difference  $\delta p = p - p_0$  between the probability measured in the presence and absence of the signal, respectively. Experimentally, the bias point can be adjusted by several means, for example, by adding a small detuning to  $\omega_0$  or by measuring the final state  $|\psi (t)\rangle$  along different directions.

# 1. Slope detection (linear detection)

The Ramsey interferometer is most sensitive to small perturbations  $\delta V$  around  $V_{0} = \omega_{0} / \gamma$  when operated at the point of maximum slope where  $p_0 = 0.5$ , indicated by the filled red dot in Fig. 3(a). This bias point is reached when  $\omega_0 t = k\pi /2$ , with  $k = 1,3,5,\ldots$ . Around  $p_0 = 0.5$ , the transition probability is linear in  $\delta V$  and  $t$ ,

$$
\begin{array}{l} \delta p = \frac {1}{2} \left[ 1 - \cos \left(\omega_ {0} t + \gamma \delta V t\right) \right] - \frac {1}{2} \\ \approx \pm \frac {1}{2} \gamma \delta V t, \tag {18} \\ \end{array}
$$

where the sign is determined by  $k$ .

![](images/8fa864c3a19cc29d9d0564b6fbf720360146eb2c22b101df9b8c45b5e077c3dc.jpg)  
FIG. 3. Transition probability  $p$  for a Ramsey experiment as a function of the signal  $V$  picked up by the sensor. (a) Slope detection: The quantum sensor is operated at the  $p_0 = 0.5$  bias point (filled red circle). A small change in the signal  $\delta V$  leads to a linear change in the transition probability  $\delta p = \delta \phi / 2 = \gamma \delta V t / 2$  (empty red circle). The uncertainty  $\sigma_p$  in the measured transition probability leads to an uncertainty in the estimated signal  $V_{\mathrm{min}}$  (gray shade). (b) Variance detection: The quantum sensor is operated at the  $p_0 = 0$  bias point (filled blue square). A small change in the signal  $\delta V$  leads to a quadratic change  $\delta p = \delta \phi^2 / 4 = \gamma^2 \delta V^2 t^2 / 4$  (empty blue square). The information on the sign of  $\delta V$  is lost. The experimental readout error  $\sigma_p$  translates into an uncertainty in the estimated signal  $V_{\mathrm{min}}$ , according to the slope or curvature of the Ramsey fringe (gray shade).

Note that slope detection has a limited linear range because phase wrapping occurs for  $|\gamma \delta Vt| > \pi / 2$ . The phase wrapping restricts the dynamic range of the quantum sensor. Section VIII discusses adaptive sensing techniques designed to extend the dynamic range.

# 2. Variance detection (quadratic detection)

If the magnitude of  $\delta V$  fluctuates between measurements so that  $\langle \delta V\rangle = 0$ , readout at  $p_0 = 0.5$  will yield no information about  $\delta V$ , since  $\langle p\rangle \approx p_0 = 0.5$ . In this situation, it is advantageous to detect the signal variance by biasing the measurement to a point of minimum slope  $\omega_0t = k\pi$ , corresponding to the bias points  $p_0 = 0$  and 1 [filled blue square in Fig. 3(b)]. If the interferometer is tuned to  $p_0 = 0$ , a signal with variance  $\langle \delta V^2\rangle = V_{\mathrm{rms}}^2$  gives rise to a mean transition probability that is quadratic in  $V_{\mathrm{rms}}$  and  $t$  (Meriles et al., 2010),

$$
\begin{array}{l} \delta p = p = \left\langle \frac {1}{2} [ 1 - \cos \left(\omega_ {0} t + \gamma \delta V t\right) ] \right\rangle \\ \approx \frac {1}{4} \gamma^ {2} V _ {\mathrm {r m s}} ^ {2} t ^ {2}. \tag {19} \\ \end{array}
$$

This relation holds for small  $\gamma V_{\mathrm{rms}}t\ll 1$  . If the fluctuation is Gaussian, the result can be extended to any large value of  $\gamma V_{\mathrm{rms}}t$

$$
p = \frac {1}{2} \left[ 1 - \exp \left(- \gamma^ {2} V _ {\mathrm {r m s}} ^ {2} t ^ {2} / 2\right) \right]. \tag {20}
$$

Variance detection is especially important for detecting ac signals when their synchronization with the sensing protocol is not possible (Sec. VI.C.4), or when the signal represents a noise source (Sec. VII).

# V. SENSITIVITY

The unprecedented level of sensitivity offered by many quantum sensors has been a key driving force of the field. In

this section, we quantitatively define the sensitivity. We start by discussing the main sources of noise that enter a quantum sensing experiment and derive expressions for the signal-to-noise ratio (SNR) and the minimum detectable signal, i.e., the signal magnitude that yields unit SNR. This will lead us to a key quantity of this paper: the sensitivity  $v_{\mathrm{min}}$  defined as the minimum detectable signal per unit time. In particular, we find in Sec. V.B.2 that  $v_{\mathrm{min}}$  is

$$
v _ {\min } \approx \frac {\sqrt {2 e}}{\gamma C \sqrt {T _ {\chi}}} \tag {21}
$$

for slope detection and

$$
v _ {\min } \approx \frac {\sqrt {2 e}}{\gamma \sqrt {C} \sqrt [ 4 ]{T _ {\chi} ^ {3}}} \tag {22}
$$

for variance detection, where  $T_{\chi}$  is the sensor's coherence time,  $C \leq 1$  is a dimensionless constant quantifying readout efficiency, and  $e$  is Euler's number [see Eqs. (43) and (45)]. In the remainder of the section signal averaging and the Allan variance are briefly discussed, and a formal definition of sensitivity by the quantum Cramér-Rao bound (QCRB) is given.

# A. Noise

Experimental detection of the probability  $p$  will have a nonzero error  $\sigma_p$ . This error translates into an error for the signal estimate, which is determined by the slope or curvature of the Ramsey fringe (see Fig. 3). In order to calculate SNR and sensitivity, it is therefore important to analyze the main sources of noise that enter  $\sigma_p$ .

# 1. Quantum projection noise

Quantum projection noise is the most fundamental source of uncertainty in quantum sensing. The projective readout during step 5 of the quantum sensing protocol (Sec. IV.B) does not directly yield the fractional probability  $p \in [0 \cdots 1]$ , but one of the two values 0 or 1 with probabilities  $1 - p$  and  $p$ , respectively. In order to precisely estimate  $p$ , the experiment is repeated  $N$  times and the occurrences of 0 and 1 are binned into a histogram [see Fig. 4(a)]. The estimate for  $p$  is then

$$
p = \frac {N _ {1}}{N}, \tag {23}
$$

where  $N_{1}$  is the number of measurements that gave a result of 1. The uncertainty in  $p$  is given by the variance of the binomial distribution (Itano et al., 1993),

$$
\sigma_ {p, \text {q u a n t u m}} ^ {2} = \frac {1}{N} p (1 - p). \tag {24}
$$

The uncertainty in  $p$  therefore depends on the bias point  $p_0$  of the measurement. For slope detection, where  $p_0 = 0.5$ , the uncertainty is

$$
\sigma_ {p, \text {q u a n t u m}} ^ {2} = \frac {1}{4 N} \quad \text {f o r} p _ {0} = 0. 5. \tag {25}
$$

Thus, the projective readout adds noise of order  $1 / (2\sqrt{N})$  to the probability value  $p$ . For variance detection, where ideally

![](images/b605a80788b285d0271c8fa181c199b7ea5978f706cc5379fb3e093ab1d61509.jpg)  
FIG. 4. Illustration of the sensor readout.  $N$  measurements are performed producing  $\{x_{j}\}_{j = 1,\dots,N}$  readings on the physical measurement apparatus. The readings  $\{x_{j}\}$  are then binned into a histogram. (a) Ideal readout. Only two values are observed in the histogram,  $x_{|0\rangle}$  and  $x_{|1\rangle}$ , which correspond to the qubit states  $|0\rangle$  and  $|1\rangle$ . All  $\{x_{j}\}$  can be assigned to 0 or 1 with  $100\%$  fidelity. (b) Single shot readout. Most  $\{x_{j}\}$  can be assigned, but there is an overlap between histogram peaks leading to a small error. (c) Averaged readout.  $\{x_{j}\}$  cannot be assigned. The ratio between 0 and 1 is given by the relative position of the mean value  $\bar{x}$  and the error is determined by the histogram standard deviation  $\sigma_{x}$ .  $R$  is the ratio of readout and projection noise, and  $C$  is an overall readout efficiency parameter that is explained in the text.

$p_0 = 0$ , the projection noise would in principle be arbitrarily low. In any realistic experiment, however, decoherence will shift the fringe minimum to a finite value of  $p$ , where Eq. (25) holds up to a constant factor.

# 2. Decoherence

A second source of error includes decoherence and relaxation during the sensing time  $t$ . Decoherence and relaxation cause random transitions between states or random phase pickup during coherent evolution of the qubit (for more detail, see Sec. VII). The two processes lead to a reduction of the observed probability  $\delta p$  with increasing sensing time  $t$ ,

$$
\delta p _ {\text {o b s}} (t) = \delta p (t) e ^ {- \chi (t)}, \tag {26}
$$

where  $\delta p(t)$  is the probability that would be measured in the absence of decoherence [see Eqs. (18) and (19)].  $\chi(t)$  is a phenomenological decoherence function that depends on the noise processes responsible for decoherence (see Sec. VII.B.1). Although the underlying noise processes may be very complex,  $\chi(t)$  can often be approximated by a simple power law,

$$
\chi (t) = (\Gamma t) ^ {a}, \tag {27}
$$

where  $\Gamma$  is a decay rate and typically  $a = 1, \ldots, 3$ . The decay rate can be associated with a decay time  $T_{\chi} = \Gamma^{-1}$  that equals the evolution time  $t$ , where  $\delta p_{\mathrm{obs}} / \delta p = 1 / e \approx 37\%$ . The decay time  $T_{\chi}$ , also known as the decoherence time or relaxation time depending on the noise process, is an important figure of merit of the qubit, as it sets the maximum possible evolution time  $t$  available for sensing.

# 3. Errors due to initialization and qubit manipulations

Errors can also enter through the imperfect initialization or manipulations of the quantum sensor. An imperfect initialization leads to a similar reduction in the observed probability  $\delta p_{\mathrm{obs}}$  as with decoherence

$$
\delta p _ {\text {o b s}} = \beta \delta p, \tag {28}
$$

where  $\beta < 1$  is a constant factor that describes the reduction of the observed  $\delta p_{\mathrm{obs}}$  as compared to the ideal  $\delta p$ . Contrary to the case of decoherence, this reduction does not depend on the sensing time  $t$ . Errors in qubit manipulations can cause many effects, but will typically also lead to a reduction of  $\delta p$ . A more general approach, considering, e.g., faulty initialization through a density matrix approach, is briefly discussed in the context of quantum limits to sensitivity (see Sec. V.D). In addition, the observed probability is sometimes reduced by the control sequence of the sensing protocol, for example, if there is no one-to-one mapping between the initialization, sensing, and readout basis (steps 2 and 4 in the protocol). Since  $\beta$  is a constant of time, we assume  $\beta = 1$  in the following for reasons of simplicity.

# 4. Classical readout noise

A final source of error is the classical noise added during the readout of the sensor. Two situations can be distinguished, depending on whether the readout noise is small or large compared to the projection noise. We denote them as the "single shot" and "averaged" readout regimes, respectively. Because of the widespread inefficiency of quantum state readout, classical readout noise is often the dominating source of error.

# a. Single shot readout

In the single shot regime, classical noise added during the readout process is small. The physical reading  $x$  produced by the measurement apparatus will be very close to one of the two values  $x_{|0\rangle}$  and  $x_{|1\rangle}$ , which would have been obtained in the ideal case for the qubit states  $|0\rangle$  and  $|1\rangle$ , respectively. By binning the physical readings  $x_{j}$  of  $j = 1,\dots ,N$  measurements into a histogram, two peaks are observed centered at  $x_{|0\rangle}$  and  $x_{|1\rangle}$ , respectively [see Fig. 4(b)]. However, compared to the ideal situation [Fig. 4(a)], the histogram peaks are broadened and there is a finite overlap between the tails of the peaks. To obtain an estimate for  $p$ , all  $x_{j}$  are assigned to either 0 or 1 based on a threshold value  $x_{T}$  chosen roughly midway between  $x_{|0\rangle}$  and  $x_{|1\rangle}$ ,

$$
N _ {0} = \text {n u m b e r o f m e a s u r e m e n t s} x _ {j} <   x _ {T}, \tag {29}
$$

$$
N _ {1} = \text {n u m b e r o f m e a s u r e m e n t s} x _ {j} > x _ {T}, \tag {30}
$$

where  $p = N_1 / N$ . Note that the choice of the threshold is not trivial; in particular, for an unbiased measurement,  $x_{T}$  depends itself on the probability  $p$ .

Because of the overlap between histogram peaks, some values  $x_{j}$  will be assigned to the wrong state. The error introduced due to wrong assignments is

$$
\sigma_ {p, \text {r e a d o u t}} ^ {2} = \frac {1}{N} \left[ \kappa_ {0} \left(1 - \kappa_ {0}\right) p + \kappa_ {1} \left(1 - \kappa_ {1}\right) (1 - p) \right], \tag {31}
$$

where  $\kappa_0$  and  $\kappa_{1}$  are the fractions of measurements that are erroneously assigned. The actual values for  $\kappa_{0,1}$  depend on the exact type of measurement noise and are determined by the cumulative distribution function of the two histogram peaks. Frequently, the peaks have an approximately Gaussian distribution such that

$$
\kappa_ {0} \approx \frac {1}{2} \left[ 1 + \operatorname {e r f} \left(\frac {\left| x _ {| 0 \rangle} - x _ {T} \right|}{\sigma_ {x}}\right) \right], \tag {32}
$$

and likewise for  $\kappa_{1}$ , where  $\operatorname{erf}(x)$  is the Gauss error function. Moreover, if  $\kappa \equiv \kappa_{0} \approx \kappa_{1} \ll 1$  are small and of similar magnitude,

$$
\sigma_ {p, \text {r e a d o u t}} ^ {2} \approx \frac {\kappa}{N}. \tag {33}
$$

# b. Averaged readout

When the classical noise added during the quantum state readout is large, only one peak appears in the histogram and the  $x_{j}$  can no longer be assigned to  $x_{|0\rangle}$  or  $x_{|1\rangle}$ . The estimate for  $p$  is then simply given by the mean value of  $x$ ,

$$
p = \frac {\bar {x} - x _ {| 0 \rangle}}{x _ {| 1 \rangle} - x _ {| 0 \rangle}} = \frac {1}{N} \sum_ {j = 1} ^ {N} \frac {x _ {j} - x _ {| 0 \rangle}}{x _ {| 1 \rangle} - x _ {| 0 \rangle}}, \tag {34}
$$

where  $\bar{x} = (1 / N)\sum x_{j}$  is the mean of  $\{x_{j}\}$ . The standard error of  $p$  is

$$
\sigma_ {p, \text {r e a d o u t}} ^ {2} = \frac {\sigma_ {x} ^ {2}}{\left(x _ {| 1 \rangle} - x _ {| 0 \rangle}\right) ^ {2}} = \frac {R ^ {2}}{4 N}, \tag {35}
$$

where  $|x_{|1\rangle} - x_{|0\rangle}|$  is the measurement contrast and

$$
R \equiv \frac {\sigma_ {p , \text {r e a d o u t}}}{\sigma_ {p , \text {q u a n t u m}}} = \frac {2 \sqrt {N} \sigma_ {x}}{\left| x _ {| 1 \rangle} - x _ {| 0 \rangle} \right|} \tag {36}
$$

is the ratio between classical readout noise and quantum projection noise.

As an example, we consider the optical readout of an atomic vapor magnetometer (Budker and Romalis, 2007) or of NV centers in diamond (Taylor et al., 2008). For this example,  $x_{|0\rangle}$  and  $x_{|1\rangle}$  denote the average numbers of photons collected per readout for each state. The standard error is (under suitable experimental conditions) dominated by shot noise  $\sigma_x \approx \sqrt{\bar{x}}$ . The readout noise parameter becomes

$$
R \approx \frac {2 \sqrt {\bar {x}}}{| x _ {| 1 \rangle} - x _ {| 0 \rangle |} = \frac {2 \sqrt {1 - \epsilon / 2}}{\epsilon \sqrt {x _ {| 1 \rangle}}} \approx \frac {2}{\epsilon \sqrt {x _ {| 1 \rangle}}}, \tag {37}
$$

where  $\epsilon = |1 - x_{|0\rangle} / x_{|1\rangle}|$  is a relative optical contrast between the states  $0 < \epsilon < 1$ , and the last equation represents the approximation for  $\epsilon \ll 1$ .

# c. Total readout uncertainty

The classical readout noise  $\sigma_{p,\mathrm{readout}}$  is often combined with the quantum projection noise  $\sigma_{p,\mathrm{quantum}}$  to obtain a total readout uncertainty,

$$
\begin{array}{l} \sigma_ {p} ^ {2} = \sigma_ {p, \text {q u a n t u m}} ^ {2} + \sigma_ {p, \text {r e a d o u t}} ^ {2} \\ \approx (1 + R ^ {2}) \sigma_ {p, \text {q u a n t u m}} ^ {2} \approx \frac {\sigma_ {p , \text {q u a n t u m}} ^ {2}}{C ^ {2}} = \frac {1}{4 C ^ {2} N}, \tag {38} \\ \end{array}
$$

where  $C = 1 / \sqrt{1 + R^2} \approx 1 / \sqrt{1 + 4\kappa}$  is an overall readout efficiency parameter (Taylor et al., 2008).  $C \leq 1$  describes the reduction of the signal-to-noise ratio compared to an ideal readout ( $C = 1$ ); see Fig. 4. We will in the following use Eq. (38) to derive the SNR and minimum detectable signal.

# B. Sensitivity

# 1. Signal-to-noise ratio

The SNR for a quantum sensing experiment can be defined as

$$
\mathrm {S N R} = \frac {\delta p _ {\text {o b s}}}{\sigma_ {p}} = \delta p (t) e ^ {- \chi (t)} 2 C \sqrt {N}, \tag {39}
$$

where  $\delta p_{\mathrm{obs}}$  is given by Eq. (26) and  $\sigma_p$  is given by Eq. (38). To further specify the SNR, the change in probability  $\delta p$  can be related to the change in signal  $\delta V$  as  $\delta p = \delta V^q |\partial_V^q p(t)|\propto (\gamma t\delta V)^q$ , with  $q = 1$  for slope detection and  $q = 2$  for variance detection (see Fig. 3). In addition, the number of measurements  $N$  is equal to  $T / (t + t_{\mathrm{m}})$ , where  $T$  is the total available measurement time and  $t_\mathrm{m}$  is the extra time needed to initialize, manipulate, and read out the sensor. The updated SNR becomes

$$
\mathrm {S N R} = \delta V ^ {q} \left| \partial_ {V} ^ {q} p (t) \right| e ^ {- \chi (t)} 2 C \left(t _ {\mathrm {m}}\right) \frac {\sqrt {T}}{\sqrt {t + t _ {\mathrm {m}}}}, \tag {40}
$$

where  $C(t_{\mathrm{m}})$  is a function of  $t_{\mathrm{m}}$  because the readout efficiency often improves for longer readout times.

# 2. Minimum detectable signal and sensitivity

The sensitivity is defined as the minimum detectable signal  $v_{\mathrm{min}}$  that yields unit SNR for an integration time of 1 s ( $T = 1$  s),

$$
v _ {\min } ^ {q} = \frac {e ^ {\chi (t)} \sqrt {t + t _ {\mathrm {m}}}}{2 C \left(t _ {\mathrm {m}}\right) \left| \partial_ {V P} ^ {q} p (t) \right|} \propto \frac {e ^ {\chi (t)} \sqrt {t + t _ {\mathrm {m}}}}{2 C \left(t _ {\mathrm {m}}\right) \gamma^ {q} t ^ {q}}. \tag {41}
$$

Equation (41) provides clear guidelines for maximizing the sensitivity. First, the sensing time  $t$  should be made as long as possible. However, because the decay function  $\chi(t)$  exponentially penalizes the sensitivity for  $t > T_{\chi}$ , the optimum sensing time is reached when  $t \approx T_{\chi}$ . Second, the sensitivity can be optimized with respect to  $t_{\mathrm{m}}$ . In particular, if  $C(t_{\mathrm{m}})$  does improve as  $C \propto \sqrt{t_{\mathrm{m}}}$ , which is a typical situation when operating in the averaged readout regime, the optimum choice is  $t_{\mathrm{m}} \approx t$ . Conversely, if  $C$  is independent of  $t_{\mathrm{m}}$ , for example,

because the sensor is operated in the single shot regime or because readout resets the sensor,  $t_{\mathrm{m}}$  should be made as short as possible. Finally,  $C$  can often be increased by optimizing the experimental implementation or using advanced quantum schemes, such as quantum logic readout.

We now evaluate Eq. (41) for the most common experimental situations:

# a. Slope detection

For slope detection,  $p_0 = 0.5$  and  $\delta p(t) \approx \frac{1}{2}\gamma Vt$  [Eq. (18)]. The sensitivity is

$$
v _ {\min } = \frac {e ^ {\chi (t)} \sqrt {t + t _ {\mathrm {m}}}}{\gamma C \left(t _ {\mathrm {m}}\right) t}. \tag {42}
$$

Note that the units of sensitivity are then typically given by the units of the signal  $V$  to be measured times  $\mathrm{Hz}^{-1/2}$ . Assuming  $t_{\mathrm{m}} \ll t$ , we can find an exact optimum solution with respect to  $t$ . Specifically, for a Ramsey measurement with an exponential dephasing  $e^{-\chi(t)} = e^{-t/T_2^*}$ , the optimum evolution time is  $t = T_2^* / 2$  and

$$
v _ {\min } = \frac {\sqrt {2 e}}{\gamma C \sqrt {T _ {2} ^ {*}}} \quad \text {f o r} t = \frac {1}{2} T _ {2} ^ {*}. \tag {43}
$$

This corresponds to Eq. (21) highlighted in the introduction to this section.

# b. Variance detection

For variance detection,  $\delta p\approx \frac{1}{4}\gamma^{2}V_{\mathrm{rms}}^{2}t^{2}$  [Eq. (19)]. The sensitivity is

$$
v _ {\min } = \left[ \frac {2 e ^ {\chi (t)} \sqrt {t + t _ {\mathrm {m}}}}{C \left(t _ {\mathrm {m}}\right) \gamma^ {2} t ^ {2}} \right] ^ {1 / 2}. \tag {44}
$$

In the limit of  $t_{\mathrm{m}} \approx 0$  and  $t \approx T_{\chi}$ , this expression simplifies to

$$
v _ {\min } = \frac {\sqrt {2 e}}{\gamma \sqrt {C} \sqrt [ 4 ]{T _ {\chi} ^ {3}}}, \tag {45}
$$

which corresponds to Eq. (22) highlighted in the introduction of the section. Thus, variance detection profits more from a long coherence time  $T_{\chi}$  than slope detection (but is, in turn, more vulnerable to decoherence). Alternatively, for the detection of a noise spectral density  $S_V(\omega)$ , the transition probability is  $\delta p \approx \frac{1}{2}\gamma^2 S_V(\omega)T_{\chi}$  [see Eqs. (84) and (98)] and

$$
S _ {v _ {\min }} (\omega) \approx \frac {e}{\gamma^ {2} C \sqrt {T _ {\chi}}}. \tag {46}
$$

# 3. Signal integration

Equations (44)-(46) refer to the minimum detectable signal per unit time. By integrating the signal over longer measurement times  $T$ , the sensor performance can be improved. According to Eq. (40), the minimum detectable signal for an arbitrary time  $T$  is  $V_{\min}^q (T) = v_{\min}^q /\sqrt{T}$ . Therefore, the

minimum detectable signal for slope and variance detection, Eqs. (42) and (45), respectively, scale as

$$
V _ {\min } (T) = v _ {\min } T ^ {- 1 / 2} \quad \text {f o r s l o p e d e t e c t i o n ,} \tag {47}
$$

$$
V _ {\min } (T) = v _ {\min } T ^ {- 1 / 4} \quad \text {f o r v a r i a n c e d e t e c t i o n .} \tag {48}
$$

The corresponding scaling for the spectral density is  $S_{V_{\min}} = S_{v_{\min}} T^{-1/2}$ . Note that variance detection improves only  $\propto T^{1/4}$  with the integration time, while slope detection improves  $\propto T^{1/2}$ . Hence, for weak signals with long averaging times  $T \gg T_{\chi}$ , variance detection is typically much less sensitive than slope detection. As discussed in Sec. VIII, adaptive sensing methods can improve on these limits.

# C. Allan variance

Sensors are typically also characterized by their stability over time. Indeed, while the sensitivity calculation suggests that one will always improve the minimum detectable signal by simply extending the measurement time, slow variations affecting the sensor might make this impossible. These effects can be quantified by the Allan variance (Allan, 1966) or its square root, the Allan deviation. While the concept is based on a classical analysis of the sensor output, it is still important for characterizing the performance of quantum sensors. In particular, the Allan variance is typically reported to evaluate the performance of quantum clocks (Hollberg et al., 2001; Leroux, Schleier-Smith, and Vuletic, 2010b).

Assuming that the sensor is sampled over time at constant intervals  $t_s$  yielding the signal  $x_j = x(t_j) = x(jt_s)$ , the Allan variance is defined as

$$
\sigma_ {X} ^ {2} (\tau) = \frac {1}{2 (N - 1) t _ {s} ^ {2}} \sum_ {j = 1} ^ {N - 1} \left(x _ {j + 1} - x _ {j}\right) ^ {2}, \tag {49}
$$

where  $N$  is the number of samples  $x_{j}$ . One is typically interested in knowing how  $\sigma_X^2$  varies with time, given the recorded sensor outputs. To calculate  $\sigma_X^2 (t)$  one can group the data in variable-sized bins and calculate the Allan variance for each grouping. The Allan variance for each grouping time  $t = mt_{s}$  can then be calculated as

$$
\sigma_ {X} ^ {2} \left(m t _ {s}\right) = \frac {1}{2 (N - 2 m) m ^ {2} t _ {s} ^ {2}} \sum_ {j = 1} ^ {N - 2 m} \left(x _ {j + m} - x _ {j}\right) ^ {2}. \tag {50}
$$

The Allan variance can also be used to reveal the performance of a sensor beyond the standard quantum limit (SQL) (Leroux, Schleier-Smith, and Vuletic, 2010b), and its extension to and limits in quantum metrology were recently explored (Chabuda, Leroux, and Demkowicz-Dobrzański, 2016).

# D. Quantum Cramér-Rao bound for parameter estimation

The sensitivity of a quantum sensing experiment can be more rigorously considered in the context of the Cramér-Rao bound applied to parameter estimation. Quantum parameter estimation aims at measuring the value of a continuous

parameter  $V$  that is encoded in the state of a quantum system  $\rho_{V}$ , via its interaction with the external signal we want to characterize. The estimation process consists of two steps: in the first step, the state  $\rho_{V}$  is measured; in the second step, the estimate of  $V$  is determined by data processing the measurement outcomes.

In the most general case, the measurement can be described by a POVM  $\mathcal{M} = \{E_x^N\}$  over the  $N$  copies of the quantum system. The measurement yields the outcome  $x$  with conditional probability  $p_N(x|V) = \mathrm{Tr}[E_x^{(N)}\rho_V^{\otimes N}]$ .

With some further data processing, we arrive at the estimate  $v$  of the parameter  $V$ . The estimation uncertainty can be described by the probability  $P_N(v|V) \coloneqq \sum_x p_{\mathrm{est}}^{(N)}(v|x)p_N(x|V)$ , where  $p_{\mathrm{est}}^{(N)}(v|x)$  is the probability of estimating  $v$  from the measurement outcome  $x$ . We can then define the estimation uncertainty as  $\Delta V_N \coloneqq \sqrt{\sum_v[v - V]^2P_N(v|V)}$ . Assuming that the estimation procedure is asymptotically locally unbiased,  $\Delta V_N$  obeys the so-called Cramér-Rao bound

$$
\Delta V _ {N} \geq 1 / \gamma \sqrt {F _ {N} (V)}, \tag {51}
$$

where

$$
\begin{array}{l} F _ {N} (V) := \sum_ {x} \frac {1}{p _ {N} (x | V)} \left(\frac {\partial p _ {N} (x | V)}{\partial V}\right) ^ {2} \\ = \sum_ {x} \frac {1}{\operatorname {T r} \left[ E _ {x} ^ {(N)} \rho_ {V} ^ {\otimes n} \right]} \left(\frac {\partial \operatorname {T r} \left[ E _ {x} ^ {(N)} \rho_ {V} ^ {\otimes n} \right]}{\partial V}\right) ^ {2} \tag {52} \\ \end{array}
$$

is the Fisher information associated with the given POVM measurement (Braunstein and Caves, 1994).

By optimizing Eq. (51) with respect to all possible POVMs, one obtains the QCRB (Helstrom, 1967; Holevo, 1982; Braunstein and Caves, 1994; Braunstein, 1996; Paris, 2009; Goldstein, Lukin, and Cappellaro, 2010)

$$
\Delta V _ {N} \geq \frac {1}{\gamma \sqrt {\max  _ {\mathcal {M} ^ {(N)}} \left[ F _ {N} (V) \right]}} \geq \frac {1}{\gamma \sqrt {N \mathcal {F} (\rho_ {V})}}, \tag {53}
$$

where the upper bound of  $\max_{\mathcal{M}^{(N)}}[F_N(V)]$  is expressed in terms of the quantum Fisher information  $\mathcal{F}(\rho_V)$ , defined as

$$
\mathcal {F} \left(\rho_ {V}\right) := \operatorname {T r} \left[ \mathcal {R} _ {\rho_ {V}} ^ {- 1} \left(\partial_ {V} \rho_ {V}\right) \rho_ {V} \mathcal {R} _ {\rho_ {V}} ^ {- 1} \left(\partial_ {V} \rho_ {V}\right) \right], \tag {54}
$$

with

$$
\mathcal {R} _ {\rho} ^ {- 1} (A) := \sum_ {j, k: \lambda_ {j} + \lambda_ {k} \neq 0} \frac {2 A _ {j k} | j \rangle \langle k |}{\lambda_ {j} + \lambda_ {k}} \tag {55}
$$

being the symmetric logarithmic derivative written in the basis that diagonalizes the state  $\rho_{V} = \sum_{j}\lambda_{j}|j\rangle \langle j|$

A simple case results when  $\rho_{V}$  is a pure state, obtained from the evolution of the reference initial state  $|0\rangle$  under the signal Hamiltonian  $|\psi_V\rangle = e^{-i\hat{H}_Vt} |0\rangle$ . Then the QCRB is a simple uncertainty relation (Helstrom, 1967; Holevo, 1982; Braunstein and Caves, 1994; Braunstein, 1996),

$$
\Delta V _ {N} \geq \frac {1}{2 \gamma \sqrt {N} \Delta H}, \tag {56}
$$

where  $\Delta H \coloneqq \sqrt{\langle H^2 \rangle - \langle H \rangle^2}$ . Note that the scaling of the QCRB with the number of copies  $N^{-1/2}$  is a consequence of the additivity of the quantum Fisher information for tensor states  $\rho^{\otimes N}$ . This is the well-known SQL. To go beyond the SQL, one then needs to use entangled states (see Sec. IX)—in particular, simply using correlated POVMs is not sufficient. Thus, to reach the QCRB, local measurements and at most adaptive estimators are sufficient, without the need for entanglement.

While the quantum Fisher information (and the QCRB) provide the ultimate lower bound to the achievable uncertainty for optimized quantum measurments, the simpler Fisher information can be used to evaluate a given measurement protocol, as achievable within experimental constraints.

Consider, for example, the sensing protocols described in Sec. IV. For the Ramsey protocol, the quantum sensor state after the interaction with the signal  $V$  is given by

$$
\rho_ {1 1} (V, t) = \frac {1}{2}, \quad \rho_ {1 2} (V, t) = - \frac {i}{2} e ^ {- i \gamma V t} e ^ {- \chi (t)}. \tag {57}
$$

Here  $e^{-\chi(t)}$  describes decoherence and relaxation as discussed with Eq. (26). If we assume to perform a projective measurement in the  $\sigma_x$  basis,  $\{|\pm\rangle\} = (1/\sqrt{2})(|0\rangle \pm |1\rangle)$ , giving the outcome probabilities  $p(x_{\pm}|V) = \langle \pm |\rho(V)|\pm \rangle$ , the Fisher information is

$$
F = \sum_ {x} \frac {1}{p (x | V)} \left[ \partial_ {V} p (x | V) \right] ^ {2} = \frac {t ^ {2} \cos^ {2} (\gamma V t) e ^ {- 2 \chi}}{1 - e ^ {- 2 \chi} \sin^ {2} (\gamma V t)}. \tag {58}
$$

The Fisher information thus oscillates between its minimum, where  $\gamma Vt = (k + 1 / 2)\pi$  and  $F = 0$ , and its optimum, where  $\gamma Vt = k\pi$  and  $F = t^2 e^{-2\chi}$ . The uncertainty in the estimate  $\delta V = 1 / \gamma \sqrt{NF}$  therefore depends on the sensing protocol bias point. In the optimum case  $F$  corresponds to the quantum Fisher information and we find the QCRB

$$
\Delta V _ {N} = \frac {1}{\gamma \sqrt {N \mathcal {F}}} = \frac {e ^ {\chi}}{\gamma t \sqrt {N}}. \tag {59}
$$

Depending on the functional form of  $\chi(t)$ , we can further find the optimal sensing time for a given total measurement time. Note that if we remember that  $N$  experiments will take a time  $T = N(t + t_m)$ , and we add inefficiency due to the sensor readout, we can recover the sensitivity  $v_{\mathrm{min}}$  of Eq. (42).

Similarly, we can analyze more general protocols, such as variance detection of random fields, simultaneous estimation of multiple parameters (Baumgratz and Datta, 2016), or optimized protocols for signals growing over time (Pang and Jordan, 2016).

# VI. SENSING OF ac SIGNALS

So far we have implicitly assumed that signals are static and deterministic. For many applications it is important to extend sensing to time-dependent signals. For example, it may be

required to detect the amplitude, frequency, or phase of an oscillating signal. More broadly, one may be interested in knowing the wave form of a time-varying parameter or reconstructing a frequency spectrum. A diverse set of quantum sensing methods has been developed for this purpose that are summarized in the following two sections.

Before discussing the various sensing protocols in more detail, it is important to consider the type of information that one intends to extract from a time-dependent signal  $V(t)$ . In this Sec. VI, we assume that the signal is composed of one or a few harmonic tones and our goal is to determine the signal's amplitude, frequency, phase, or overall wave form. In the following Sec. VII, we will discuss the measurement of stochastic signals with the intent of reconstructing the noise spectrum or measuring the noise power in a certain bandwidth.

# A. Time-dependent signals

As measuring arbitrary time-dependent signals is a complex task, we first focus on developing a basic set of ac sensing protocols, assuming a single-tone ac signal given by

$$
V \left(t ^ {\prime}\right) = V _ {\mathrm {p k}} \cos \left(2 \pi f _ {\mathrm {a c}} t ^ {\prime} + \alpha\right). \tag {60}
$$

This signal has three basic parameters, including the signal amplitude  $V_{\mathrm{pk}}$ , the frequency  $f_{\mathrm{ac}}$ , and the relative phase  $\alpha$ . Our aim is to measure one or several of these parameters using suitable sensing protocols.

Signal detection can be extended to multitone signals by summing over individual single-tone signals,

$$
V \left(t ^ {\prime}\right) = \sum_ {m} V _ {\mathrm {p k}, m} \cos \left(2 \pi f _ {\mathrm {a c}, m} t ^ {\prime} + \alpha_ {m}\right), \tag {61}
$$

where  $V_{\mathrm{pk},m}$ ,  $f_{\mathrm{ac},m}$ , and  $\alpha_{m}$  are the individual amplitudes, frequencies, and phases of the tones, respectively.

# B. Ramsey and echo sequences

To illustrate the difference between dc and ac sensing, we reexamine the Ramsey measurement from Sec. IV.C. The corresponding pulse diagram is given in Fig. 5(a). This protocol is ideally suited to measure static shifts of the transition energy. But is it also capable of detecting dynamical variations? In order to answer this question, one can inspect the phase  $\phi$  accumulated during the sensing time  $t$  due to either a static or a time-dependent signal  $V(t)$ ,

$$
\phi = \int_ {0} ^ {t} \gamma V \left(t ^ {\prime}\right) d t ^ {\prime}. \tag {62}
$$

For a static perturbation, the accumulated phase is simply  $\phi = \gamma Vt$ . For a rapidly oscillating perturbation, by contrast, phase accumulation is averaged over the sensing time, and  $\phi = \gamma \langle V(t') \rangle t \approx 0$ . To answer our question, the Ramsey sequence will be sensitive only to slowly varying signals up to some cutoff frequency  $\approx t^{-1}$ .

Sensitivity to alternating signals can be restored by using time-reversal ("spin-echo") techniques (Hahn, 1950). To illustrate this, we assume that the ac signal goes through

![](images/afc0a7ee9b9390333142ec3277bc8560fe5d3e69118c104dbb12fe97924d95c8.jpg)

![](images/6c2edc81fd294ce65d66b3480edb1b6e146f89ffb5edd7212bacf612c06d0803.jpg)

![](images/d43c59610751888c0a08ef2aac7e31857247b4499005a713d76d73f4c6b5e88e.jpg)

![](images/f55e5066b9a5c87d399abfa10f273669cffee7bcf2c9c3731891961800456de6.jpg)  
FIG. 5. Pulse diagrams for dc and ac sensing sequences. Narrow blocks represent  $\pi /2$  pulses and wide blocks represent  $\pi$  pulses, respectively.  $t$  is the total sensing time and  $\tau$  is the interpulse delay. (a) Ramsey sequence. (b) Spin-echo sequence. (c) CarrPurcell (CP) multipulse sequence. (d) PDD multipulse sequence.

exactly one period of oscillation during the sensing time  $t$ . The Ramsey phase  $\phi$  due to this signal is zero because the positive phase buildup during the first half of  $t$  is exactly canceled by the negative phase buildup during the second half of  $t$ . However, if the qubit is inverted at time  $t / 2$  using a  $\pi$  pulse [see Fig. 5(b)], the time evolution of the second period is reversed, and the accumulated phase is nonzero,

$$
\phi = \int_ {0} ^ {t / 2} \gamma V (t ^ {\prime}) d t ^ {\prime} - \int_ {t / 2} ^ {t} \gamma V (t ^ {\prime}) d t ^ {\prime} = \frac {2}{\pi} \gamma V _ {\mathrm {p k}} t \cos \alpha . \tag {63}
$$

# C. Multipulse sensing sequences

The spin-echo technique can be extended to sequences with many  $\pi$  pulses. These sequences are commonly referred to as multipulse sensing sequences or multipulse control sequences and allow for a detailed shaping of the frequency response of the quantum sensor. To understand the ac characteristics of a multipulse sensing sequence, we consider the phase accumulated for a general sequence of  $n\pi$  pulses applied at times  $0 < t_{j} < t$ , with  $j = 1,\dots,n$ . The accumulated phase is given by

$$
\phi = \int_ {0} ^ {t} \gamma V \left(t ^ {\prime}\right) y \left(t ^ {\prime}\right) d t ^ {\prime}, \tag {64}
$$

where  $y(t^{\prime}) = \pm 1$  is the modulation function of the sequence that changes sign whenever a  $\pi$  pulse is applied (Fig. 6). For a harmonic signal  $V(t^{\prime}) = V_{\mathrm{pk}}\cos (2\pi f_{\mathrm{ac}}t^{\prime} + \alpha)$  the phase is

$$
\begin{array}{l} \phi = \frac {\gamma V _ {\mathrm {p k}}}{2 \pi f _ {\mathrm {a c}}} [ \sin (\alpha) - (- 1) ^ {n} \sin (2 \pi f _ {\mathrm {a c}} t + \alpha) \\ + 2 \sum_ {j = 1} ^ {n} (- 1) ^ {j} \sin (2 \pi f _ {\mathrm {a c}} t _ {j} + \alpha) ] \\ = \gamma V _ {\mathrm {p k}} t W \left(f _ {\mathrm {a c}}, \alpha\right). \tag {65} \\ \end{array}
$$

This defines for any multipulse sequence a weighting function  $W(f_{\mathrm{ac}},\alpha)$ . For composite signals consisting of several harmonics with different frequencies and amplitudes, Eq. (61), the accumulated phase simply represents the sum of individual

![](images/33d7825f82076655c97012c21bd210e63518717ff796b25859007da79450471d.jpg)

![](images/75ef6d1359b664a63db5a22a6057110133c3171e916e8ed3725c2e45b0e6425c.jpg)

![](images/84214712cc68d6cc172c6fc060280976fe33fa9ae1686c109dfbf58cd2fefeb0.jpg)

![](images/8b96cad3222dbccf97a13c453b783c0b7fad3ee765d56776fb0402a1a7fed126.jpg)

![](images/064ce57c070b4019da458ad9163b10747b7a109ce022198fb95eca99c255cd06.jpg)  
FIG. 6. Modulation and weight functions of a  $CP$  multipulse sequence. (a)  $CP$  multipulse sequence. (b) Signal  $V(t')$ , modulation function  $y(t')$ , and "rectified" signal  $V(t') \times y(t')$ . The accumulated phase is represented by the area under the curve. (c) Weight function  $\bar{W}^2(f_{\mathrm{ac}})$  associated with the modulation function.  $k$  is the harmonic order of the filter resonance.

tone amplitudes multiplied by the respective weighting functions.

# 1. Carr-Purcell (CP) and periodic dynamical decoupling sequences

The simplest pulse sequences used for sensing have been initially devised in NMR (Slichter, 1996) and have been further developed in the context of dynamical decoupling (DD) (Viola and Lloyd, 1998). They are composed of  $n$  equally spaced  $\pi$  pulses with an interpulse duration  $\tau$ . The most common types are Carr-Purcell (CP) pulse trains (Carr and Purcell, 1954) [Fig. 5(c)] and periodic dynamical decoupling (PDD) sequences (Khodjasteh and Lidar, 2005) [Fig. 5(d)].

For a basic CP sequence,  $t_j = [(2j - 1) / 2]\tau$ , and the weighting function is (Taylor et al., 2008; Hirose, Aiello, and Cappellaro, 2012)

$$
W _ {\mathrm {C P}} \left(f _ {\mathrm {a c}}, \alpha\right) = \frac {\sin \left(\pi f _ {\mathrm {a c}} n \tau\right)}{\pi f _ {\mathrm {a c}} n \tau} \left[ 1 - \sec \left(\pi f _ {\mathrm {a c}} \tau\right) \right] \cos (\alpha + \pi f _ {\mathrm {a c}} n \tau). \tag {66}
$$

Similarly, for a PDD sequence,  $t_j = j\tau$  and

$$
W _ {\mathrm {P D D}} \left(f _ {\mathrm {a c}}, \alpha\right) = \frac {\sin \left(\pi f _ {\mathrm {a c}} n \tau\right)}{\pi f _ {\mathrm {a c}} n \tau} \tan \left(\pi f _ {\mathrm {a c}} \tau\right) \sin \left(\alpha + \pi f _ {\mathrm {a c}} n \tau\right). \tag {67}
$$

Because of the first (sinc) term, these weighting functions resemble narrow-band filters around the center frequencies  $f_{\mathrm{ac}} = f_k = k / (2\tau)$ , where  $k = 1,3,5,\ldots$  is the harmonic order. In fact, they can be rigorously treated as filter functions that filter the frequency spectrum of the signal  $V(t)$  (see Sec. VII). For large pulse numbers  $n$ , the sinc term becomes very peaked and the filter bandwidth  $\Delta f \approx 1 / (n\tau) = 1 / t$  (full width at half maximum) becomes very narrow. The narrowband filter characteristics can be summed up as follows [see Fig. 5(c)],

$$
f _ {k} = k / (2 \tau) \quad \text {c e n t e r f r e q u e n c i e s}, \tag {68}
$$

$$
\Delta f \approx 1 / t = 1 / (n \tau) \quad \text {b a n d w i d t h}, \tag {69}
$$

$$
W _ {\mathrm {C P}} (\alpha) = \frac {2}{\pi k} (- 1) ^ {k - 1 / 2} \cos (\alpha)
$$

$$
W _ {\mathrm {P D D}} (\alpha) = - \frac {2}{\pi k} \sin (\alpha) \quad \text {p e a k t r a n s m i s s i o n .} \tag {70}
$$

The advantage of the CP and PDD sequences is that their filter parameters can be easily tuned. In particular, the pass-band frequency can be selected via the interpulse delay  $\tau$ , while the filter width can be adjusted via the number of pulses  $n = t / \tau$  (up to a maximum value of  $n \approx T_2 / \tau$ ). The resonance order  $k$  can also be used to select the pass-band frequency; however, because  $k = 1$  provides the strongest peak transmission, most reported experiments used this resonance. The time response of the transition probability is

$$
\begin{array}{l} p = \frac {1}{2} [ 1 - \cos (W (f _ {\mathrm {a c}}, \alpha) \gamma V _ {\mathrm {p k}} t) ] \\ = \frac {1}{2} \left[ 1 - \cos \left(\frac {2 \gamma V _ {\mathrm {p k}} t \cos \alpha}{k \pi}\right) \right], \tag {71} \\ \end{array}
$$

where the last expression represents the resonant case  $(f_{\mathrm{ac}} = k / 2\tau)$  for CP sequences [Fig. 7(b)].

# 2. Lock-in detection

The phase  $\phi$  acquired during a CP or PDD sequence depends on the relative phase difference  $\alpha$  between the ac signal and the modulation function  $y(t)$ . For a signal that is in phase with  $y(t)$ , the maximum phase accumulation occurs, while for an out-of-phase signal  $\phi = 0$ .

This behavior can be exploited to add further capabilities to ac signal detection. Kotler et al. (2011) showed that both quadratures of a signal can be recovered, allowing one to perform lock-in detection of the signal. Furthermore, it is possible to correlate the phase acquired during two subsequent multipulse sequences to perform high-resolution spectroscopy of ac signals (see Sec. VI.E).

![](images/def2c376df029e546b7fb810d88d0029992dfa96c0504fa3c9babb062dc8fdd2.jpg)  
FIG. 7. Transition probability  $p(t)$  as a function of phase accumulation time  $t$ . (a) Ramsey oscillation [Eq. (14)]. (b) ac signal with fixed amplitude and optimum phase [Eq. (71)]. (c) ac signal with fixed amplitude and random phase [Eq. (75)]. (d) ac signal with random amplitude and random phase [Eq. (76)]. (e) Broadband noise with  $\chi = \Gamma t$  [Eq. (83)].

# 3. Other types of multipulse sensing sequences

Many varieties of multipulse sequences have been conceived with the aim of optimizing the basic CP design, including improved robustness against pulse errors, better decoupling performance, narrower spectral response and sideband suppression, and avoidance of signal harmonics.

A systematic analysis of many common sequences was given by Cywinski et al. (2008). One preferred is the  $XY4$ ,  $XY8$ , and  $XY16$  series of sequences (Gullion, Baker, and Conradi, 1990) owing to their high degree of pulse error compensation. A downside of  $XY$  type sequences are signal harmonics (Loretz et al., 2015) and the sidebands common to CP sequences with equidistant pulses. Other recent efforts include sequences with nonequal pulse spacing (Zhao, Wrachtrup, and Liu, 2014; Casanova et al., 2015; Ajoy et al., 2017) or sequences composed of alternating subsequences (Albrecht and Plenio, 2015). A Floquet spectroscopy approach to multipulse sensing (Lang, Liu, and Monteiro, 2015) and a protocol to achieve optimal band-limited control (Frey et al., 2017) have also been proposed.

# 4.ac signals with random phase

Often the multipulse sequence cannot be synchronized with the signal or the phase  $\alpha$  cannot be controlled. Then incoherent averaging leads to phase cancellation  $\langle \phi \rangle = 0$ . In this case, it is advantageous to measure the variance of the phase  $\langle \phi^2 \rangle$  rather than its average  $\langle \phi \rangle$ . (Although such a signal technically represents a stochastic signal, which will be considered in more detail in the next section, it is more conveniently described here.)

For a signal with fixed amplitude but random phase, the variance is

$$
\langle \phi^ {2} \rangle = \gamma^ {2} V _ {\mathrm {r m s}} ^ {2} t ^ {2} \tilde {W} ^ {2} \left(f _ {\mathrm {a c}}\right), \tag {72}
$$

where  $V_{\mathrm{rms}} = V_{\mathrm{pk}} / \sqrt{2}$  is the rms amplitude of the signal and  $\bar{W}^2 (f_{\mathrm{ac}})$  is the average over  $\alpha = 0,\dots,2\pi$  of the weighting functions,

$$
\bar {W} ^ {2} \left(f _ {\mathrm {a c}}\right) = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} W ^ {2} \left(f _ {\mathrm {a c}}, \alpha\right) d \alpha . \tag {73}
$$

For the CP and PDD sequences, the averaged functions are given by

$$
\bar {W} _ {\mathrm {C P}} ^ {2} (f _ {\mathrm {a c}}) = \frac {\sin^ {2} (\pi f _ {\mathrm {a c}} n \tau)}{2 (\pi f _ {\mathrm {a c}} n \tau) ^ {2}} [ 1 - \sec (\pi f _ {\mathrm {a c}} \tau) ] ^ {2},
$$

$$
\bar {W} _ {\mathrm {P D D}} ^ {2} \left(f _ {\mathrm {a c}}\right) = \frac {\sin^ {2} \left(\pi f _ {\mathrm {a c}} n \tau\right)}{2 \left(\pi f _ {\mathrm {a c}} n \tau\right) ^ {2}} \tan \left(\pi f _ {\mathrm {a c}} \tau\right) ^ {2}, \tag {74}
$$

and the peak transmission at  $f_{\mathrm{ac}} = k / 2\tau$  is  $\bar{W}^2 = 2 / (k\pi)^2$ . The time response of the transition probability is (Kotler et al., 2013)

$$
\begin{array}{l} p (t) = \frac {1}{2} [ 1 - J _ {0} (\sqrt {2} \bar {W} (f _ {\mathrm {a c}}) \gamma V _ {\mathrm {r m s}} t) ] \\ = \frac {1}{2} \left[ 1 - J _ {0} \left(\frac {2 \sqrt {2} \gamma V _ {\mathrm {r m s}} t}{k \pi}\right) \right], \tag {75} \\ \end{array}
$$

where  $J_0$  is the Bessel function of the first kind and the second equation reflects the resonant case [Fig. 7(c)].

# 5. ac signals with random phase and random amplitude

If the amplitude  $V_{\mathrm{pk}}$  is not fixed, but slowly fluctuating between different measurements, the variance  $\langle \phi^2 \rangle$  must be integrated over the probability distribution of  $V_{\mathrm{pk}}$ . A particularly important situation is a Gaussian amplitude fluctuation with an rms amplitude  $V_{\mathrm{rms}}$ . In this case, the resonant time response of the transition probability is

$$
p (t) = \frac {1}{2} \left[ 1 - \exp \left(- \frac {\bar {W} ^ {2} \gamma^ {2} V _ {\mathrm {r m s}} ^ {2} t ^ {2}}{2 k ^ {2}}\right) I _ {0} \left(\frac {\bar {W} ^ {2} \gamma^ {2} V _ {\mathrm {r m s}} ^ {2} t ^ {2}}{2 k ^ {2}}\right) \right], \tag {76}
$$

where  $I_0$  is the modified Bessel function of the first kind [Fig. 7(d)].

# D. Wave form reconstruction

The detection of ac fields can be extended to the more general task of sensing and reconstructing arbitrary time-dependent fields. A simple approach is to record the time response  $p(t)$  under a specific sensing sequence, such as a Ramsey sequence, and to reconstruct the phase  $\phi(t)$  and signal  $V(t)$  from the time trace (Balasubramanian et al., 2009). This approach is, however, limited to the bandwidth of the sequence and by readout dead times.

To more systematically reconstruct the time dependence of an arbitrary signal, one may use a family of pulse sequences that forms a basis for the signal. A suitable basis is Walsh dynamical decoupling sequences (Hayes et al., 2011), which apply a  $\pi$  pulse every time the corresponding Walsh function (Walsh, 1923) flips its sign. Under a control sequence with  $n$ $\pi$  pulses applied at the zero crossings of the nth Walsh function  $y(t^{\prime}) = w_{n}(t^{\prime} / t)$ , the phase acquired after an acquisition period  $t$  is

$$
\phi (t) = \gamma \int_ {0} ^ {t} V \left(t ^ {\prime}\right) y \left(t ^ {\prime}\right) d t ^ {\prime} = \gamma V _ {n} t, \tag {77}
$$

which is proportional to the  $n$ th Walsh coefficient  $V_{n}$  of  $V(t')$ . By measuring  $N$  Walsh coefficients (by applying  $N$  different sequences) one can reconstruct an  $N$ -point functional approximation to the field  $V(t')$  from the  $N$ th partial sum of the Walsh-Fourier series (Magesan et al., 2013; Cooper et al., 2014),

$$
V _ {N} \left(t ^ {\prime}\right) = \sum_ {n = 0} ^ {N - 1} V _ {n} w _ {n} \left(t ^ {\prime} / t\right), \tag {78}
$$

which can be shown to satisfy  $\lim_{N\to \infty}V_N(t') = V(t')$ . A similar result can be obtained using different basis functions, such as Haar wavelets, as long as they can be easily implemented experimentally (Xu et al., 2016).

An advantage of these methods is that they provide protection of the sensor against dephasing, while extracting the desired information. In addition, they can be combined with compressive sensing techniques (Candes, Romberg, and Tao, 2006; Magesan, Cooper, and Cappellaro, 2013; Puentes et al., 2014) to reduce the number of acquisitions needed to reconstruct the time-dependent signal. The ultimate metrology limits in wave form reconstruction have also been studied (Tsang, Wiseman, and Caves, 2011).

# E. Frequency estimation

An important capability in ac signal detection is the precise estimation of frequencies. In quantum sensing, most frequency estimation schemes are based on dynamical decoupling sequences. These are discussed in the following. Fundamental limits of frequency estimation based on the quantum Fisher information were considered by Pang and Jordan (2016).

# 1. Dynamical decoupling spectroscopy

A simple approach for determining a signal's frequency is to measure the response to pulse sequences with different pulse spacings  $\tau$ . This is equivalent to stepping the frequency of a lock-in amplifier across a signal. The spectral resolution of dynamical decoupling spectroscopy is determined by the bandwidth of the weighting function  $W(f_{\mathrm{ac}},\tau)$ , which is given by  $\Delta f\approx 1 / t$  [see Eq. (69)]. Because  $t$  can be made only as long as the decoherence time  $T_{2}$ , the spectral resolution is limited to  $\Delta f\approx 1 / T_2$ . The precision of the frequency estimation, which also depends on the signal-to-noise ratio, is directly proportional to  $\Delta f$ .

# 2. Correlation sequences

Several schemes have been proposed and demonstrated to further narrow the bandwidth and to perform high-resolution spectroscopy. All of them rely on correlation-type measurements where the outcomes of subsequent sensing periods are correlated.

The first method is illustrated in Fig. 8(a) in combination with multipulse detection. The multipulse sequence is subdivided into two equal sensing periods of duration  $t_a = t / 2$

![](images/e1c42ccb9e45c92beb0d31c2fd4c0484f30a1eaabc5c505e2b529cb62fd4e77e.jpg)  
FIG. 8. Correlation spectroscopy. (a) ac signal  $V(t')$ . (b) Correlation sequence. Two multipulse sequences are interrupted by an incremented delay time  $t_1$ . Because the multipulse sequences are phase sensitive, the total phase accumulated after the second multipulse sequence oscillates with  $f_{\mathrm{ac}}t_1$ . The maximum  $t_1$  is limited by the relaxation time  $T_1$ , rather than the typically short decoherence time  $T_2$ . (c) Continuous sampling. The signal is periodically probed in intervals of the sampling time  $t_s$ . The frequency can be estimated from a sample record of arbitrary duration, permitting an arbitrarily fine frequency resolution.

that are separated by an incremented free evolution period  $t_1$ . Since the multipulse sequence is phase sensitive, constructive or destructive phase build-up occurs between the two sequences depending on whether the free evolution period  $t_1$  is a half multiple or full multiple of the ac signal period  $T_{\mathrm{ac}} = 1 / f_{\mathrm{ac}}$ . The final transition probability therefore oscillates with  $t_1$  as

$$
\begin{array}{l} p \left(t _ {1}\right) = \frac {1}{2} \left\{1 - \sin [ \Phi \cos (\alpha) ] \sin [ \Phi \cos (\alpha + 2 \pi f _ {\mathrm {a c}} t _ {1}) ] \right\} \\ \approx \frac {1}{2} \left\{1 - \Phi^ {2} \cos (\alpha) \cos \left(\alpha + 2 \pi f _ {\mathrm {a c}} t _ {1}\right) \right\}, \tag {79} \\ \end{array}
$$

where  $\Phi = \gamma V_{\mathrm{pk}}t / k\pi$  is the maximum phase that can be accumulated during either of the two multipulse sequences. The second equation is for small signals where  $\sin \Phi \approx \Phi$ . For signals with random phase, Eq. (79) can be integrated over  $\alpha$  and the transition probability simplifies to

$$
p \left(t _ {1}\right) \approx \frac {1}{2} \left\{1 - \frac {\Phi^ {2}}{2} \cos \left(2 \pi f _ {\mathrm {a c}} t _ {1}\right) \right\}. \tag {80}
$$

Since the qubit is parked in  $|0\rangle$  and  $|1\rangle$  during the free evolution period, relaxation is no longer governed by  $T_{2}$ , but by the typically much longer  $T_{1}$  relaxation time (Laraoui and Meriles, 2013). In this way, a Fourier-limited spectral resolution of  $\Delta f\sim 1 / T_1$  is possible. The resolution can be further enhanced by long-lived auxiliary memory qubits (see Sec. X) and resolution improvements by 2-3 orders of magnitude over dynamical decoupling spectroscopy have been demonstrated (Pfender et al., 2016; Rosskopf et al., 2016; Zaiser et al., 2016). The correlation protocol was further shown to eliminate several other shortcomings of multipulse sequences, including signal ambiguities resulting from the multiple frequency windows and spectral selectivity (Boss et al., 2016).

# 3. Continuous sampling

The second approach is the continuous sampling of a signal, illustrated in Fig. 8(b). The output signal can then be Fourier

transformed to extract the undersampled frequency of the original signal. Because continuous sampling no longer relies on quantum state lifetimes, the Fourier-limited resolution can be extended to arbitrary values and is limited only by total experiment duration  $T$ , and ultimately the control hardware. The original signal frequency can then be reconstructed from the undersampled data record using compressive sampling techniques (Nader, Björsell, and Händel, 2011). Continuous sampling has recently led to the demonstration of  $\mu \mathrm{Hz}$  spectral resolution (Boss et al., 2017; Schmitt et al., 2017).

# VII. NOISE SPECTROSCOPY

In this section, we discuss methods for reconstructing the frequency spectrum of stochastic signals, a task commonly referred to as noise spectroscopy. Noise spectroscopy is an important tool in quantum sensing, as it can provide much insight into both external signals and the intrinsic noise of the quantum sensor. In particular, good knowledge of the noise spectrum can help the adoption of suitable sensing protocols (such as dynamical decoupling or quantum error correction schemes) to maximize the sensitivity of the quantum sensor.

Noise spectroscopy relies on the systematic analysis of decoherence and relaxation under different control sequences. This review focuses on two complementary frameworks for extracting noise spectra. The first concept is that of "filter functions," where the phase pick-up due to stochastic signals is analyzed under different dynamical decoupling sequences. The second concept, known as "relaxometry," has its origins in the field of magnetic resonance spectroscopy and is closely related to Fermi's golden rule.

# A. Noise processes

For the following analysis we assume that the stochastic signal  $V(t)$  is Gaussian. Such noise can be described by simple noise models, such as a semiclassical Gaussian noise or the Gaussian spin-boson bath. In addition, we assume that the autocorrelation function of  $V(t)$ ,

$$
G _ {V} (t) = \left\langle V \left(t ^ {\prime} + t\right) V \left(t ^ {\prime}\right) \right\rangle , \tag {81}
$$

decays on a time scale  $t_c$  that is shorter than the sensing time  $t$ , such that successive averaging measurements are not correlated. The noise can then be represented by a power spectral density (Biercuk, Doherty, and Uys, 2011),

$$
S _ {V} (\omega) = \int_ {- \infty} ^ {\infty} e ^ {- i \omega t} G _ {V} (t) d t, \tag {82}
$$

that has no sharp features within the bandwidth  $\Delta f \approx 1 / t$  of the sensor. The aim of a noise spectroscopy experiment is to reconstruct  $S_V(\omega)$  as a function of  $\omega$  over a frequency range of interest.

Although this section focuses on Gaussian noise with  $t_c \lesssim t$ , the analysis can be extended to other noise models and correlated noise. When  $t_c \gg t$ , the frequency and amplitude of  $V(t)$  are essentially fixed during one sensing period and the formalism of ac sensing can be applied (see Sec. VI.C). A rigorous derivation for all ranges of  $t_c$ , but

especially  $t_c \approx t$ , is given by Cummings (1962). More complex noise models, such as  $1/f$  noise with no well-defined  $t_c$ , or models that require a cumulant expansion beyond a first-order approximation on the noise strength can also be considered (Bergli and Faoro, 2007; Ban, Kitajima, and Shibata, 2009). Finally, open-loop control protocols have been introduced (Cywinski, 2014; Paz-Silva and Viola, 2014; Barnes et al., 2016; Norris, Paz-Silva, and Viola, 2016) to characterize stationary, non-Gaussian dephasing.

# B. Decoherence, dynamical decoupling, and filter functions

There have been many proposals for examining decoherence under different control sequences to investigate noise spectra (Faoro and Viola, 2004; Almog et al., 2011; Yuge, Sasaki, and Hirayama, 2011; Young and Whaley, 2012). In particular, dynamical decoupling sequences based on multipulse protocols (Sec. VI.C) provide a systematic means for filtering environmental noise (Álvarez and Suter, 2011; Biercuk, Doherty, and Uys, 2011; Kotler et al., 2011). These have been implemented in many physical systems (Bylander et al., 2011; Bar-Gill et al., 2012; Yan et al., 2012, 2013; Dial et al., 2013; Kotler et al., 2013; Muhonen et al., 2014; Yoshihara et al., 2014; Romach et al., 2015). A brief introduction to the method of filter functions is presented in the following.

# 1. Decoherence function  $\chi(t)$

Under the assumption of a Gaussian, stationary noise, the loss of coherence can be captured by an exponential decay of the transition probability with time  $t$ ,

$$
p (t) = \frac {1}{2} \left(1 - e ^ {- \chi (t)}\right), \tag {83}
$$

where  $\chi (t)$  is the associated decay function or decoherence function that was already discussed in the context of sensitivity (Sec. V). Quite generally,  $\chi (t)$  can be identified with an rms phase accumulated during time  $t$

$$
\chi (t) = \frac {1}{2} \phi_ {\mathrm {r m s}} ^ {2} \tag {84}
$$

according to the expression for variance detection, Eq. (20).

Depending on the type of noise present, the decoherence function shows a different dependence on  $t$ . For white noise, the dephasing is Markovian and  $\chi(t) = \Gamma t$ , where  $\Gamma$  is the decay rate. For Lorentzian noise centered at zero frequency the decoherence function is  $\chi(t) = (\Gamma t)^3$ . For a generic  $1/f$ -like decay, where the noise falls of  $\propto \omega^a$  (with  $a$  around unity), the decoherence function is  $\chi(t) = (\Gamma t)^{a+1}$  (Cywinski et al., 2008; Medford et al., 2012) with a logarithmic correction depending on the ratio of total measurement time and evolution time (Dial et al., 2013). Sometimes, decoherence may even need to be described by several decay constants associated with several competing processes. A thorough discussion of decoherence is presented in the recent review by Suter and Álvarez (2016).

# 2. Filter function  $Y(\omega)$

The decoherence function  $\chi(t)$  can be analyzed under the effect of different control sequences. Assuming the control sequence has a modulation function  $y(t)$  (see Sec. VI.C), the

decay function is determined by the correlation integral (de Sousa, 2009; Biercuk, Doherty, and Uys, 2011)

$$
\chi (t) = \frac {1}{2} \int_ {0} ^ {t} d t ^ {\prime} \int_ {0} ^ {t} d t ^ {\prime \prime} y \left(t ^ {\prime}\right) y \left(t ^ {\prime \prime}\right) \gamma^ {2} G _ {V} \left(t ^ {\prime} - t ^ {\prime \prime}\right), \tag {85}
$$

where  $G_V(t)$  is the autocorrelation function of  $V(t)$  [Eq. (81)]. In the frequency domain the decay function can be expressed as

$$
\chi (t) = \frac {2}{\pi} \int_ {0} ^ {\infty} \gamma^ {2} S _ {V} (\omega) | Y (\omega) | ^ {2} d \omega , \tag {86}
$$

where  $|Y(\omega)|^2$  is the so-called filter function of  $y(t)$ , defined by the finite-time Fourier transform

$$
Y (\omega) = \int_ {0} ^ {t} y \left(t ^ {\prime}\right) e ^ {i \omega t ^ {\prime}} d t ^ {\prime}. \tag {87}
$$

[Note that this definition differs by a factor of  $\omega^2$  from the one by Biercuk, Doherty, and Uys (2011)]. Thus, the filter function plays the role of a transfer function, and the decay of coherence is captured by the overlap with the noise spectrum  $S_V(\omega)$ .

To illustrate the concept of filter functions we reconsider the canonical example of a Ramsey sensing sequence. Here the filter function is

$$
| Y (\omega) | ^ {2} = \frac {\sin^ {2} (\omega t / 2)}{\omega^ {2}}. \tag {88}
$$

The decoherence function  $\chi(t)$  then describes the "free-induction decay"

$$
\chi (t) = \frac {2}{\pi} \int_ {0} ^ {\infty} \gamma^ {2} S _ {V} (\omega) \frac {\sin^ {2} (\omega t / 2)}{\omega^ {2}} d \omega \approx \frac {1}{2} \gamma^ {2} S _ {V} (0) t, \tag {89}
$$

where the last equation is valid for a spectrum that is flat around  $\omega \lesssim \pi /t$ . The Ramsey sequence hence acts as a simple sinc filter for the noise spectrum  $S_V(\omega)$ , centered at zero frequency and with a low-pass cutoff frequency of approximately  $\pi /t$ .

# 3. Dynamical decoupling

To perform a systematic spectral analysis of  $S_V(\omega)$ , one can examine decoherence under various dynamical decoupling sequences. Specifically, we inspect the filter functions of periodic modulation functions  $y_{n_c,\tau_c}(t)$ , where a basic building block  $y_{1}(t)$  of duration  $\tau_{c}$  is repeated  $n_c$  times. The filter function of  $y_{n_c,\tau_c}(t)$  is given by

$$
\begin{array}{l} Y _ {n _ {c}, \tau_ {c}} (\omega) = Y _ {1, \tau_ {c}} (\omega) \sum_ {k = 0} ^ {n _ {c} - 1} e ^ {i \tau_ {c} k} \\ = Y _ {1, \tau_ {c}} (\omega) e ^ {- i \left(n _ {c} - 1\right) \omega \tau_ {c} / 2} \frac {\sin \left(n _ {c} \omega \tau_ {c} / 2\right)}{\sin \left(\omega \tau_ {c} / 2\right)}, \tag {90} \\ \end{array}
$$

where  $Y_{1,\tau_c}(\omega)$  is the filter function of the basic building block. For large cycle numbers,  $Y_{n_c,\tau_c}(\omega)$  presents sharp peaks at multiples of the inverse cycle time  $\tau_c^{-1}$ , and it can be approximated by a series of  $\delta$  functions.

Two specific examples of periodic modulation functions include the CP and PDD sequences considered in Sec. VI.C, where  $\tau_{c} = 2\tau$  and  $n_c = n / 2$ . The filter function for large pulse numbers  $n$  is

$$
\begin{array}{l} \left| Y _ {n, \tau} \right| ^ {2} \approx \sum_ {k} \frac {2 \pi}{(k \pi) ^ {2}} \operatorname {s i n c} [ (\omega - \omega_ {k}) t / 2 ] ^ {2} \\ \approx \sum_ {k} \frac {2 \pi}{(k \pi) ^ {2}} t \delta (\omega - \omega_ {k}), \tag {91} \\ \end{array}
$$

where  $\omega_{k} = 2\pi \times k / (2\tau)$  are resonances with  $k = 1,3,5,\ldots$  [note that these expressions are equivalent to the filters of Eq. (74) found for random phase signals].

The decay function can then be expressed by a simple sum of different spectral density components,

$$
\begin{array}{l} \chi (t) = \frac {2}{\pi} \int_ {0} ^ {\infty} \gamma^ {2} S _ {V} (\omega) \sum_ {k} \frac {2 \pi}{(k \pi) ^ {2}} t \delta (\omega - \omega_ {k}) d \omega \\ = \frac {4 t}{\pi^ {2}} \sum_ {k} \frac {\gamma^ {2} S _ {V} \left(\omega_ {k}\right)}{k ^ {2}}. \tag {92} \\ \end{array}
$$

This result provides a simple strategy for reconstructing the noise spectrum. By sweeping the time  $\tau$  between pulses the spectrum can be probed at various frequencies. Since the filter function is dominated by the first harmonic ( $k = 1$ ), the frequency corresponding to a certain  $\tau$  is  $1 / (2\tau)$ . For a more detailed analysis the contributions from higher harmonics as well as the exact shape of the filter functions have to be taken into account. The spectrum can then be recovered by spectral decomposition (Álvarez and Suter, 2011; Bar-Gill et al., 2012).

The filter analysis can be extended to more general dynamical decoupling sequences. In particular, Zhao, Wrachtrup, and Liu (2014) considered periodic sequences with more complex building blocks, and Cywiński et al. (2008) considered aperiodic sequences such as the Uhrig dynamical decoupling sequence.

# C. Relaxometry

An alternative framework for analyzing relaxation and coherence was developed in the field of magnetic resonance spectroscopy and is commonly referred to as relaxometry (Abragam, 1961). The concept was later extended to the context of qubits (Schoelkopf et al., 2003). The aim of relaxometry is to connect the spectral density  $S_V(\omega)$  of a noise signal  $V(t)$  to the relaxation rate  $\Gamma$  in first-order kinetics  $\chi(t) = \Gamma t$ . Relaxometry is based on first-order perturbation theory and Fermi's golden rule. The basic assumptions are that the noise process is approximately Markovian and that the noise strength is weak, such that first-order perturbation theory is valid. Relaxometry has found many applications in magnetic resonance and other fields, especially for mapping high-frequency noise based on  $T_1$  relaxation time measurements (Kimmich and Anoardo, 2004).

# 1. Basic theory of relaxometry

To derive a quantitative relationship between the decay rate  $\Gamma$  and a noise signal  $V(t)$ , we briefly revisit the elementary formalism of relaxometry (Abragam, 1961). In the first step,  $V(t)$  can be expanded into Fourier components,

$$
V (t) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} d \omega \left\{V (\omega) e ^ {- i \omega t} + V ^ {\dagger} (\omega) e ^ {i \omega t} \right\}, \tag {93}
$$

where  $V(\omega) = V^{\dagger}(-\omega)$ . Next we calculate the probability amplitude  $c_{1}$  that a certain frequency component  $V(\omega)$  causes a transition between two orthogonal sensing states  $|\psi_0\rangle$  and  $|\psi_1\rangle$  during the sensing time  $t$ . Since the perturbation is weak, perturbation theory can be applied. The probability amplitude  $c_{1}$  in first-order perturbation theory is

$$
\begin{array}{l} c _ {1} (t) = - i \int_ {0} ^ {t} d t ^ {\prime} \langle \psi_ {1} | \hat {H} _ {V} (\omega) | \psi_ {0} \rangle e ^ {i (\omega_ {0 1} - \omega) t ^ {\prime}} \\ = - i \left\langle \psi_ {1} \right| \hat {H} _ {V} (\omega) \left| \psi_ {0} \right\rangle \frac {e ^ {i \left(\omega_ {0 1} - \omega\right) t} - 1}{i \left(\omega_ {0 1} - \omega\right)}, \tag {94} \\ \end{array}
$$

where  $\hat{H}_V(\omega)$  is the Hamiltonian associated with  $V(\omega)$  and  $\omega_{01}$  is the transition energy between states  $|\psi_0\rangle$  and  $|\psi_1\rangle$ . The transition probability is

$$
\begin{array}{l} \left| c _ {1} (t) \right| ^ {2} = \left| \langle \psi_ {1} \mid \hat {H} _ {V} (\omega) \mid \psi_ {0} \rangle \right| ^ {2} \left(\frac {\sin [ (\omega_ {0 1} - \omega) t / 2 ]}{(\omega_ {0 1} - \omega) / 2}\right) ^ {2} \\ \approx 2 \pi | \langle \psi_ {1} | \hat {H} _ {V} (\omega) | \psi_ {0} \rangle | ^ {2} t \delta \left(\omega_ {0 1} - \omega\right), \tag {95} \\ \end{array}
$$

where the second equation reflects that, for large  $t$ , the sinc function approaches a  $\delta$  function peaked at  $\omega_{01}$ . The associated transition rate is

$$
\frac {\partial \left| c _ {1} (t) \right| ^ {2}}{\partial t} \approx 2 \pi \left| \langle \psi_ {1} \mid \hat {H} _ {V} (\omega) \mid \psi_ {0} \rangle \right| ^ {2} \delta \left(\omega_ {0 1} - \omega\right). \tag {96}
$$

This is Fermi's golden rule expressed for a two-level system that is coupled to a radiation field with a continuous frequency spectrum (Sakurai and Napolitano, 2011).

This transition rate is due to a single frequency component of  $\hat{H}_V(\omega)$ . To obtain the overall transition rate  $\Gamma$ , Eq. (96) must be integrated over all frequencies,

$$
\begin{array}{l} \Gamma = \frac {1}{\pi} \int_ {0} ^ {\infty} d \omega 2 \pi | \langle \psi_ {1} | \hat {H} _ {V} (\omega) | \psi_ {0} \rangle | ^ {2} \delta \left(\omega_ {0 1} - \omega\right) \\ = 2 | \langle \psi_ {1} | \hat {H} _ {V} (\omega_ {0 1}) | \psi_ {0} \rangle | ^ {2} \\ = 2 \gamma^ {2} S _ {V _ {0 1}} \left(\omega_ {0 1}\right) | \langle \psi_ {1} | \sigma_ {V} / 2 | \psi_ {0} \rangle | ^ {2}, \tag {97} \\ \end{array}
$$

where in the last equation  $S_{V_{01}}$  is the spectral density of the component(s) of  $V(t)$  that can drive transitions between  $|\psi_0\rangle$  and  $|\psi_1\rangle$ , multiplied by a transition matrix element  $|\langle \psi_1|\sigma_V / 2|\psi_0\rangle|^2$  of order unity that represents the operator part of  $\hat{H}_V = V(t)\sigma_V / 2$  [see Eq. (5)].

Equation (97) is an extremely simple, yet powerful and quantitative relationship: the transition rate equals the spectral density of the noise evaluated at the transition frequency, multiplied by a matrix element of order unity (Abragam, 1961; Schoelkopf et al., 2003). The expression can also be interpreted in terms of the rms phase  $\phi_{\mathrm{rms}}$ . According to

TABLE II. Summary of noise spectroscopy methods.  $|\pm \rangle = (|0\rangle \pm |1\rangle) / \sqrt{2}$ .  

<table><tr><td>Method</td><td>Sensing states {|ψ0&gt;, |ψ1&gt;}</td><td>Sensitive to V∥ at frequency</td><td>Sensitive to V⊥ at frequency</td><td>Frequency tunable via</td></tr><tr><td>Ramsey</td><td>{|+&gt;, -}</td><td>0</td><td>...a</td><td>...</td></tr><tr><td>Spin echo</td><td>{|+&gt;, -}</td><td>1/t</td><td>...a</td><td>...</td></tr><tr><td>Dynamical decoupling</td><td>{|+&gt;, -}</td><td>πk/τ, with k = 1, 3, ...</td><td>...a</td><td>Pulse spacing τ, resonance order k</td></tr><tr><td>T1relaxometry</td><td>{|0&gt;, |1&gt;}</td><td>...</td><td>ω0</td><td>Static control field</td></tr><tr><td>Dressed states (resonant)</td><td>{|+&gt;, -}</td><td>ω1</td><td>...a</td><td>Drive field amplitude ω1</td></tr><tr><td>Dressed states (off resonant)</td><td>{|+&gt;, -}</td><td>ωeff ≈ Δω</td><td>...a</td><td>Detuning Δω</td></tr></table>

${}^{a}$  Also affected by  ${T}_{1}$  relaxation.

Eq. (84),  $\phi_{\mathrm{rms}}^2 = 2\chi(t) = 2\Gamma t$ , which in turn yields (setting  $|\langle \psi_1|\sigma_V / 2|\psi_0\rangle|^2 = \frac{1}{4}$ )

$$
\phi_ {\mathrm {r m s}} ^ {2} = \gamma^ {2} S _ {V _ {0 1}} \left(\omega_ {0 1}\right) t. \tag {98}
$$

The rms phase thus corresponds to the noise integrated over an equivalent noise bandwidth of  $1 / (2\pi t)$ .

The relation between the transition rate  $\Gamma$  and the spectral density can be further specified for vector signals  $\vec{V}$ . In this case the transition rate represents the sum of the three vector components of  $V_{j}$ , where  $j = x, y, z$ ,

$$
\begin{array}{l} \Gamma = 2 \sum_ {j = x, y, z} | \langle \psi_ {1} | \hat {H} _ {V _ {j}} (\omega_ {j}) | \psi_ {0} \rangle | ^ {2} \\ = 2 \sum_ {j = x, y, z} \gamma^ {2} S _ {V _ {j}} (\omega_ {j}) | \langle \psi_ {1} | \hat {\sigma} _ {j} | \psi_ {0} \rangle | ^ {2}, \tag {99} \\ \end{array}
$$

where  $S_{V_j}(\omega_j)$  is the spectral density of  $V_j$ ,  $\omega_j$  is a transition frequency that reflects the energy exchange required for changing the state, and  $\hat{\sigma}_j$  are Pauli matrices. Note that if  $\{|\psi_0\rangle ,|\psi_1\rangle \}$  are coherent superposition states,  $V_{x}$  and  $V_{y}$  represent the components of  $V_{\perp}$  that are in phase and out of phase with the coherence, rather than the static components of the vector signal  $\vec{V}$ .

Relaxation rates can be measured between any set of sensing states  $\{|\psi_0\rangle ,|\psi_1\rangle \}$ , including superposition states. This gives rise to a great variety of possible relaxometry measurements. For example, the method can be used to probe different vector components  $V_{j}(t)$  [or commuting and noncommuting signals  $V_{\parallel}(t)$  and  $V_{\perp}(t)$ , respectively] based on the selection of sensing states. Moreover, different sensing states typically have vastly different transition energies, providing a means to cover a wide frequency spectrum. If multiple sensing qubits are available, the relaxation of higher-order quantum transitions can be measured, which gives additional freedom to probe different symmetries of the Hamiltonian.

An overview of the most important relaxometry protocols is given in Table II and Fig. 9. They are briefly discussed in the following.

# 2.  $T_{1}$  relaxometry

$T_{1}$  relaxometry probes the transition rate between states  $|0\rangle$  and  $|1\rangle$ . This is the canonical example of energy relaxation. Experimentally, the transition rate is measured by initializing the sensor into  $|0\rangle$  at time  $t' = 0$  and inspecting  $p = |\langle 1|\alpha \rangle|^2$

at time  $t' = t$  without any further manipulation of the quantum system [see Fig. 9(a)]. The transition rate is

$$
\left(T _ {1}\right) ^ {- 1} = \frac {1}{2} \gamma^ {2} S _ {V _ {\perp}} \left(\omega_ {0}\right), \tag {100}
$$

where  $T_{1}$  is the associated relaxation time and  $S_{V_{\perp}} = S_{V_x} + S_{V_y}$ . Thus,  $T_{1}$  relaxometry is sensitive only to the transverse component of  $\vec{V}$ . Because  $T_{1}$  can be very long, very high sensitivities are in principle possible, assuming that the resonance is not skewed by low-frequency noise (Joas et al., 2017; Stark et al., 2017). By tuning the energy splitting  $\omega_0$  between  $|0\rangle$  and  $|1\rangle$ , for example, through the application of a static control field, a frequency spectrum of  $S_{V_{\perp}}(\omega)$  can be recorded (Kimmich and Anoardo, 2004). For this reason and because it is experimentally simple,  $T_{1}$  relaxometry has found many applications. For example, single-spin probes have been used to detect the presence of magnetic ions (Steinert et al., 2013), spin waves in magnetic films (van der Sar et al., 2015), high-frequency magnetic fluctuations near surfaces (Myers et al., 2014; Rosskopf et al., 2014; Romach et al., 2015), and single molecules (Sushkov et al., 2014).  $T_{1}$  relaxometry has also been applied to perform spectroscopy of electronic and nuclear spins (Hall et al., 2016). In addition, considerable effort has been invested in mapping the noise spectrum near superconducting flux qubits by combining several relaxometry methods (Bialczak et al., 2007; Lanting et al., 2009; Bylander et al., 2011; Yan et al., 2013).

# 3.  $T_{2}^{*}$  and  $T_{2}$  relaxometry

$T_{2}^{*}$  relaxometry probes the transition rate between the superposition states  $|\pm \rangle = (|0\rangle \pm e^{-i\omega_{0}t}|1\rangle) / \sqrt{2}$ . This

![](images/e91abd31df47a1d0ec056fbb5edbbe95e7fa97cbcb577d24d9be83458fbfdb47.jpg)

![](images/4f73875c1611cf832b0d23f616671ee4c88b8daf827bfa61487c5e9fa307daaa.jpg)

![](images/eccf765fed14f27c6dbf0b5af0bbbec281484a0db6522fbace083c5d6ef3ab39.jpg)  
FIG. 9. Common relaxometry protocols. (a)  $T_{1}$  relaxometry. (b)  $T_{2}^{*}$  relaxometry. (c) Dressed state relaxometry. Narrow black boxes represent  $\pi / 2$  pulses and the gray box in (c) represents a resonant or off-resonant drive field.

corresponds to the free-induction decay observed in a Ramsey experiment [Fig. 9(b)]. The associated dephasing time  $T_{2}^{*}$  is given by

$$
\left(T _ {2} ^ {*}\right) ^ {- 1} = \frac {1}{4} \gamma^ {2} S _ {V _ {\perp}} \left(\omega_ {0}\right) + \frac {1}{2} \gamma^ {2} S _ {V _ {\parallel}} (0), \tag {101}
$$

where  $S_{V_{\parallel}} = S_{V_z}$  [see also Eq. (89)]. The transverse  $S_{V_{\perp}}$  term in Eq. (101) involves a "bit flip" and the parallel  $S_{V_{\parallel}}$  term involves a "phase flip." Because a phase flip does not require energy, the spectral density is probed at zero frequency. Since  $S_V(\omega)$  is often dominated by low-frequency noise,  $S_{V_{\parallel}}(0)$  is typically much larger than  $S_{V_{\perp}}(\omega_0)$  and the high-frequency contribution can often be neglected. Note that Eq. (101) is exact only when the spectrum  $S_{V_{\parallel}}(\omega)$  is flat up to  $\omega \sim \pi / t$ .

$T_{2}^{*}$  relaxometry can be extended to include dephasing under dynamical decoupling sequences. The relevant relaxation time is then usually denoted by  $T_{2}$  rather than  $T_{2}^{*}$ . Dephasing under dynamical decoupling is more rigorously described by using filter functions (see Sec. VII.B.2).

# 4. Dressed state methods

Relaxation can also be analyzed in the presence of a resonant drive field. This method is known as "spin locking" in magnetic resonance (Slichter, 1996). Because of the presence of the resonant field the degeneracy between  $|\pm \rangle$  is lifted and the states are separated by the energy  $\hbar \omega_{1}$ , where  $\omega_{1} \ll \omega_{0}$  is the Rabi frequency of the drive field. A phase flip therefore is no longer energy conserving. The associated relaxation time  $T_{1\rho}$  is given by

$$
\left(T _ {1 \rho}\right) ^ {- 1} \approx \frac {1}{4} \gamma^ {2} S _ {V _ {\perp}} \left(\omega_ {0}\right) + \frac {1}{2} \gamma^ {2} S _ {V _ {\parallel}} \left(\omega_ {1}\right). \tag {102}
$$

By systematically varying the Rabi frequency  $\omega_{1}$ , the spectrum  $S_{V_{\parallel}}(\omega_1)$  can be recorded (Loretz, Rosskopf, and Degen, 2013; Yan et al., 2013). Because  $\omega_{1} \ll \omega_{0}$ , dressed states provide useful means for covering the medium frequency range of the spectrum (see Fig. 10). In addition, since dressed state relaxometry does not require sweeping a static control field for adjusting the probe frequency, it is more versatile than standard  $T_{1}$  relaxometry.

Dressed state methods can be extended to include off-resonant drive fields. Specifically, if the drive field is detuned by  $\Delta \omega$  from  $\omega_0$ , relaxation is governed by a modified relaxation time

$$
(T _ {1 \rho}) ^ {- 1} \approx \gamma^ {2} \frac {1}{4} \left[ 1 + \frac {\Delta \omega^ {2}}{\omega_ {\text {e f f}} ^ {2}} \right] S _ {V _ {\perp}} (\omega_ {0}) + \frac {1}{2} \frac {\omega_ {1} ^ {2}}{\omega_ {\text {e f f}} ^ {2}} \gamma^ {2} S _ {V _ {\parallel}} (\omega_ {\text {e f f}}), \tag {103}
$$

where  $\omega_{\mathrm{eff}} = \sqrt{\omega_1^2 + \Delta\omega^2}$  is the effective Rabi frequency. A detuning therefore increases the accessible spectral range toward higher frequencies. For a very large detuning the effective frequency becomes similar to the detuning  $\omega_{\mathrm{eff}}\approx \Delta \omega$  and the drive field enters only as a scaling factor for the spectral density. Detuned drive fields have been used to map the  $1 / f$  noise spectrum of transmon qubits up to the GHz range (Slichter et al., 2012).

![](images/9f49d8d02e7f929175de8821bf1912379b0f0d44db215263fa14103eb085a6d2.jpg)  
FIG. 10. Typical spectral range of noise spectroscopy protocols. Scales refer to the quantum sensors discussed in Sec. III.

# VIII. DYNAMIC RANGE AND ADAPTIVE SENSING

"Adaptive sensing" refers to a class of techniques addressing the intrinsic problem of limited dynamic range in quantum sensing: The basic quantum sensing protocol cannot simultaneously achieve high sensitivity and measure signals over a large amplitude range.

The origin of this problem lies in the limited range of values for the probability  $p$ , which must fall between 0 and 1. For the example of a Ramsey measurement,  $p$  oscillates with the signal amplitude  $V$  and phase wrapping occurs once  $\gamma V t$  exceeds  $\pm \pi / 2$ , where  $t$  is the sensing time. Given a measured transition probability  $p$ , there is an infinite number of possible signal amplitudes  $V$  that can correspond to this value of  $p$  (see top row of Fig. 11). A unique assignment hence requires a priori knowledge that  $V$  lies within  $\pm \pi / (2\gamma t)$ , or within half a Ramsey fringe, of an expected signal amplitude. This defines a maximum allowed signal range,

$$
V _ {\max } = \frac {\pi}{\gamma t}. \tag {104}
$$

The sensitivity of the measurement, on the other hand, is proportional to the slope of the Ramsey fringe and reaches its optimum when  $t \approx T_2^*$ . The smallest detectable signal is approximately  $V_{\mathrm{min}} \approx 2 / \gamma C \sqrt{T_2^*T}$ , where  $T$  is the total measurement time and  $C$  is the readout efficiency parameter [see Eqs. (43) and (47)]. The dynamic range is then given by the maximum allowed signal divided by the minimum detectable signal,

$$
\mathrm {D R} = \frac {V _ {\max}}{V _ {\min}} = \frac {\pi C \sqrt {T}}{2 \sqrt {T _ {2} ^ {*}}} \propto \sqrt {T}. \tag {105}
$$

Hence, the basic measurement protocol can be applied only to small changes of a quantity around a fixed known value, frequently zero. The protocol does not apply to the problem of determining the value of a large and a priori unknown quantity. Moreover, the dynamic range improves only with the square root of the total measurement time  $T$ .

![](images/87df6d3a817a3ad8ce09c366f648e470125293a63334d2e09cd9a20af86062bd.jpg)  
FIG. 11. High dynamic range sensing. A series of measurements with different interrogation times  $t$  is combined to estimate a signal of interest. The shortest measurement (lowest line) has the largest allowed signal  $V_{\mathrm{max}}$  and provides a coarse estimate of the quantity, which is subsequently refined by longer and more sensitive measurements. Although the  $p(V)$  measured in a sensitive measurement (top line) can correspond to many possible signal values, the coarse estimates allow one to extract a unique signal value  $V$ .

# A. Phase estimation protocols

Interestingly, a family of advanced sensing techniques can efficiently address this problem and achieve a dynamic range that scales close to  $\mathrm{DR} \propto T$ . This scaling is sometimes referred to as another instance of the Heisenberg limit, because it can be regarded as a  $1 / T$  scaling of sensitivity at a fixed  $V_{\mathrm{max}}$ . The central idea is to combine measurements with different sensing times  $t$  such that the least sensitive measurement with the highest  $V_{\mathrm{max}}$  yields a coarse estimate of the quantity of interest, which is subsequently refined by more sensitive measurements (Fig. 11).

In the following we discuss protocols that use exponentially growing sensing times  $t_m = 2^m t_0$ , where  $m = 0, 1, \dots, M$  and  $t_0$  is the smallest time element (see Fig. 11). Although other scheduling is possible, this choice allows for an intuitive interpretation: subsequent measurements estimate subsequent digits of a binary expansion of the signal. The maximum allowed signal is then set by the shortest sensing time  $V_{\mathrm{max}} = \pi / \gamma t_0$ , while the smallest detectable signal is determined by the longest sensing time  $V_{\mathrm{min}} \approx 2 / \gamma C \sqrt{t_M T}$ . Because  $T \propto t_M$  due to the exponentially growing interrogation times, the dynamic range of the improved protocol scales as

$$
\mathrm {D R} \propto \frac {\sqrt {t _ {M} T}}{t _ {0}} \propto T. \tag {106}
$$

This scaling is obvious from an order-of-magnitude estimate: adding an additional measurement step increases both precision and measurement duration  $t$  by a factor of 2, such that precision scales linearly with total acquisition time  $T$ . We now discuss three specific implementations of this idea.

# 1. Quantum phase estimation

All three protocols can be considered variations of the phase estimation scheme depicted in Fig. 12(a). The scheme was originally put forward by Shor (1994) in the seminal proposal of a quantum algorithm for prime factorization and was interpreted by Kitaev (1995), as a phase estimation algorithm.

The original formulation applies to the problem of finding the phase  $\phi$  of the eigenvalue  $e^{2\pi i\phi}$  of a unitary operator  $\hat{U}$ , given a corresponding eigenvector  $|\psi\rangle$ . This problem can be generalized to estimating the phase shift  $\phi$  imparted by passage through an interferometer or exposure to an external field. The algorithm employs a register of  $N$  auxiliary qubits ( $N = 3$  in Fig. 12) and prepares them into a digital representation  $|\phi\rangle = |\phi_1\rangle |\phi_2\rangle \dots |\phi_M\rangle$  of a binary expansion of

![](images/2b63c4593dc49219c4fc848ff28aed9fc8c1babc8922c5eecac9eedd057a48f4.jpg)  
(a) Quantum phase estimation

![](images/315037e76ff77b6c40b904adb747fdcb51989cd4e266f1d6b3c8502d9d5e4472.jpg)  
(b) Adaptive

![](images/5c7d454e1115ddf06a87bbd472d2338160476f1494d18df5e844f76e44dc754f.jpg)  
FIG. 12. Phase estimation algorithms. (a) Quantum phase estimation by the inverse quantum Fourier transform, as it is employed in prime factorization algorithms (Shor, 1994; Kitaev, 1995). (b) Adaptive phase estimation. Here the quantum Fourier transform is replaced by measurement and classical feedback. Bits are measured in ascending order, subtracting the lower digits from measurements of higher digits by phase gates that are controlled by previous measurement results. (c) Nonadaptive phase estimation. Measurements of all digits are fed into a Bayesian estimation algorithm to estimate the most likely value of the phase.  $H$  represents a Hadamard gate,  $R(\Phi)$  a  $Z$  rotation by the angle  $\Phi$ , and  $U$  the propagator for one time element  $t_0$ . The boxes labeled by "x" represent readouts.  
(c) Non-adaptive (Bayesian)

$\phi = \sum_{m=1}^{M} \phi_m 2^{-m}$  by a sequence of three processing steps as follows:

(1) State preparation: All qubits are prepared in a coherent superposition state  $| + \rangle = (|0\rangle + |1\rangle) / \sqrt{2}$  by an initial Hadamard gate. The resulting state of the full register can then be written as

$$
\frac {1}{\sqrt {2 ^ {M}}} \sum_ {j = 0} ^ {2 ^ {M} - 1} | j \rangle_ {M}, \tag {107}
$$

where  $|j\rangle_M$  denotes the register state in binary expansion  $|0\rangle_M = |00\dots 0\rangle$ ,  $|1\rangle_M = |00\dots 1\rangle$ ,  $|2\rangle_M = |00\dots 10\rangle$ , etc.

(2) Phase encoding: The phase of each qubit is tagged with a multiple of the unknown phase  $\phi$ . Specifically, qubit  $m$  is placed in state  $(|0\rangle + e^{2\pi i 2^m} \phi |1\rangle) / \sqrt{2}$ . Technically, this can be implemented by exploiting the backaction of a controlled- $\hat{U}^{2^m}$  gate that is acting on the eigenvector  $\psi$  conditional on the state of qubit  $m$ . Since  $\psi$  is an eigenvector of  $\hat{U}^j$  for arbitrary  $j$ , this action transforms the joint qubit-eigenvector state as

$$
\begin{array}{l} \frac {1}{\sqrt {2}} \left(| 0 \rangle + | 1 \rangle\right) \otimes | \psi \rangle \\ \rightarrow \frac {1}{\sqrt {2}} (| 0 \rangle + e ^ {2 \pi i 2 ^ {m} \phi} | 1 \rangle) \otimes | \psi \rangle . \tag {108} \\ \end{array}
$$

Here the backaction on the control qubit  $m$  creates the required phase tag. The state of the full register evolves to

$$
\frac {1}{\sqrt {2 ^ {M}}} \sum_ {j = 0} ^ {2 ^ {M} - 1} e ^ {2 \pi i \phi j / 2 ^ {M}} | j \rangle . \tag {109}
$$

In quantum sensing, phase tagging by backaction is replaced by the exposure of each qubit to an external field for a time  $2^{m}t_{0}$  (or passage through an interferometer of length  $2^{m}l_{0}$ ).

(3) Quantum Fourier transform: In the last step, an inverse quantum Fourier transform (QFT) (Nielsen and Chuang, 2000) is applied to the qubits. This algorithm can be implemented with polynomial effort [i.e., using  $\mathcal{O}(M^2)$  control gates]. The QFT recovers the phase  $\phi$  from the Fourier series (109) and places the register in state

$$
| \phi \rangle = | \phi_ {1} \rangle | \phi_ {2} \rangle \dots | \phi_ {M} \rangle . \tag {110}
$$

A measurement of the register directly yields a digital representation of the phase  $\phi$ . To provide an estimate of  $\phi$  with  $2^{-M}$  accuracy,  $2^{M}$  applications of the phase shift  $\hat{U}$  are required. Hence, the algorithm scales linearly with the number of applications of  $\hat{U}$  which in turn is proportional to the total measurement time  $T$ .

Quantum phase estimation is the core component of Shor's algorithm, where it is used to compute discrete logarithms with polynomial time effort (Shor, 1994).

# 2. Adaptive phase estimation

While quantum phase estimation based on the QFT can be performed with polynomial time effort, the algorithm requires two-qubit gates, which are difficult to implement experimentally, and the creation of fragile entangled states. This limitation can be circumvented by an adaptive measurement scheme that reads the qubits sequentially, feeding back the classical measurement result into the quantum circuit (Griffiths and Niu, 1996). The scheme is illustrated in Fig. 12(b).

The key idea of adaptive phase estimation is to first measure the least significant bit of  $\phi$ , represented by the lowest qubit in Fig. 12(b). In the measurement of the next significant bit, this value is subtracted from the applied phase. The subtraction can be implemented by classical unitary rotations conditioned on the measurement result, for example, by controlled  $R(\pi / j)$  gates as shown in Fig. 12(b). This procedure is then repeated in ascending order of the bits. The QFT is thus replaced by measurement and classical feedback, which can be performed using a single qubit sensor.

In practical implementations (Higgins et al., 2007), the measurement of each digit is repeated multiple times or performed on multiple parallel qubits. This is possible because the controlled-  $U$  gate does not change the eigenvector  $\psi$ , so that it can be reused as often as required. The Heisenberg limit can be reached only if the number of resources (qubits or repetitions) spent on each bit are carefully optimized (Berry et al., 2009; Said, Berry, and Twamley, 2011; Cappellaro, 2012). Clearly, most resources should be allocated to the most significant bit, because errors at this stage are most detrimental to sensitivity. The implementation by Bonato et al. (2016), for example, scaled the number of resources  $N_{m}$  linearly according to

$$
N _ {m} = G + F (M - 1 - m) \tag {111}
$$

with typical values of  $G = 5$  and  $F = 2$ .

# 3. Nonadaptive phase estimation

Efficient quantum phase estimation can also be implemented without adaptive feedback, with the advantage of technical simplicity (Higgins et al., 2009). A set of measurements  $\{x_{j}\}_{j = 1,\dots,N}$  (where  $N > M$ ) is used to separately determine each unitary phase  $2^{m}\phi$  with a set of fixed, classical phase shifts before each readout. This set of measurements still contains all the information required to extract  $\phi$ , which can be motivated by the following arguments: given a redundant set of phases, a postprocessing algorithm can mimic the adaptive algorithm by postselecting those results that have been measured using the phase most closely resembling the correct adaptive choice. From a spectroscopic point of view, measurements with different phases correspond to Ramsey fringes with different quadratures. Hence, at least one qubit of every digit will perform its measurement on the slope of a Ramsey fringe, allowing for a precise measurement of  $2^{m}\phi$  regardless of its value.

The phase  $\phi$  can be recovered by Bayesian estimation. Every measurement  $x_{j} = \pm 1$  provides information about  $\phi$ , which is described by the a posteriori probability

$$
p \left(\phi \mid x _ {j}\right), \tag {112}
$$

the probability that the observed outcome  $x_{j}$  stems from a phase  $\phi$ . This probability is related to the inverse conditional probability  $p(x_{l}|\phi)$ , the excitation probability describing Ramsey fringes, by Bayes's theorem. The joint probability distribution of all measurements is obtained from the product

$$
p (\phi) \propto \prod_ {j} p (\phi | x _ {j}), \tag {113}
$$

from which the most likely value of  $\phi$  is picked as the final result (Nusran, Ummal, and Dutt, 2012; Waldherr et al., 2012). Here, too, acquisition time scales with the significance of the bit measured to achieve the Heisenberg limit.

# 4. Comparison of phase estimation protocols

All of these variants of phase estimation achieve a  $\mathrm{DR} \propto T$  scaling of the dynamic range. They differ, however, by a constant offset. Adaptive estimation is slower than quantum phase estimation by the QFT since it trades spatial resources (entanglement) into temporal resources (measurement time). Bayesian estimation in turn is slower than adaptive estimation due to additional redundant measurements.

Experimentally, Bayesian estimation is usually simple to implement because no real-time feedback is needed and the phase estimation can be performed a posteriori. Adaptive estimation is technically more demanding since real-time feedback is involved, which often requires dedicated hardware (such as field-programmable gate arrays or a central processing unit) for the fast decision making. Quantum phase estimation by the QFT, finally, requires many entangled qubits.

# B. Experimental realizations

The proposals of Shor (1994), Kitaev (1995), and Griffiths and Niu (1996) were followed by a decade where research toward Heisenberg-limited measurements has focused mostly on the use of entangled states, such as the  $N00N$  state (see Sec. IX). These states promise Heisenberg scaling in the spatial dimension (number of qubits) rather than time (Lee, Kok, and Dowling, 2002; Giovannetti, Lloyd, and Maccone, 2004, 2006) and have been studied extensively for both spin qubits (Bollinger et al., 1996; Leibfried et al., 2004, 2005; Jones et al., 2009) and photons (Fonseca, Monken, and Pdua, 1999; Edamatsu, Shimizu, and Itoh, 2002; Mitchell, Lundeen, and Steinberg, 2004; Walther et al., 2004; Nagata et al., 2007; Xiang et al., 2011).

Heisenberg scaling in the temporal dimension has shifted into focus with an experiment published in 2007, where adaptive phase estimation was employed in a single-photon interferometer (Higgins et al., 2007). The experiment was subsequently extended to a nonadaptive version (Higgins et al., 2009). Shortly after, both variants were translated into protocols for spin-based quantum sensing (Said, Berry, and Twamley, 2011). Meanwhile, high-dynamic-range protocols have been demonstrated on NV centers in diamond using both nonadaptive implementations (Nusran, Ummal, and Dutt, 2012; Waldherr et al., 2012) and an adaptive protocol based on quantum feedback (Bonato et al., 2016). As a final remark, we note that a similar performance,  $1 / T$  scaling and an increased dynamic range, may be achieved by weak measurement protocols, which

continuously track the evolution of the phase over the sensing sequence (Shiga and Takeuchi, 2012; Kohlhaas et al., 2015).

# IX. ENSEMBLE SENSING

Up to this point, we mainly focused on single qubit sensors. In the following two sections, quantum sensors consisting of more than one qubit will be discussed. The use of multiple qubits opens up many additional possibilities that cannot be implemented on a single qubit sensor.

This section considers ensemble sensors where many (usually identical) qubits are operated in parallel. Apart from a gain in readout sensitivity, multiple qubits allow for the implementation of second-generation quantum techniques, including entanglement and state squeezing, which provide a true quantum advantage that cannot be realized with classical sensors. Entanglement-enhanced sensing has been pioneered with atomic systems, especially atomic clocks (Giovannetti, Lloyd, and Maccone, 2004; Leibfried et al., 2004). In parallel, state squeezing is routinely applied in optical systems, such as optical interferometers (LIGO Collaboration, 2011).

# A. Ensemble sensing without entanglement

Before discussing entanglement-enhanced sensing techniques, we briefly consider the simple parallel operation of  $M$  identical single-qubit quantum sensors. This implementation is used, for example, in atomic vapor magnetometers (Budker and Romalis, 2007) or solid-state spin ensembles (Wolf et al., 2015). The use of  $M$  qubits accelerates the measurement by a factor of  $M$ , because the basic quantum sensing cycle (steps 1-5 of the protocol in Fig. 2) can now be operated in parallel rather than sequentially. Equivalently,  $M$  parallel qubits can improve the sensitivity by  $\sqrt{M}$  per unit time.

This scaling is equivalent to the situation where  $M$  classical sensors are operated in parallel. The scaling can be seen as arising from the projection noise associated with measuring the quantum system, where it is often called the SQL (Braginskii and Vorontsov, 1975; Giovannetti, Lloyd, and Maccone, 2004) or shot-noise limit. In practice, it is sometimes difficult to achieve a  $\sqrt{M}$  scaling because instrumental stability is more critical for ensemble sensors (Wolf et al., 2015).

For ensemble sensors such as atomic vapor magnetometers or spin arrays, the quantity of interest is more likely the number density of qubits, rather than the absolute number of qubits  $M$ . That is, how many qubits can be packed into a certain volume without deteriorating the sensitivity of each qubit? The sensitivity is then expressed per unit volume  $(\propto \mathrm{m}^{-3 / 2})$ . The maximum density of qubits is limited by internal interactions between the qubits. Optimal densities have been calculated for both atomic vapor magnetometers (Budker and Romalis, 2007) and ensembles of NV centers (Taylor et al., 2008; Wolf et al., 2015).

# B. Heisenberg limit

The standard quantum limit can be overcome by using quantum-enhanced sensing strategies to reach a more fundamental limit where the uncertainty  $\sigma_{p}$  [Eq. (25)] scales as  $1 / M$ . This limit is also known as the Heisenberg limit.

Achieving the Heisenberg limit requires reducing the variance of a chosen quantum observable at the expense of the uncertainty of a conjugated observable. This in turn requires preparing the quantum sensors in an entangled state. In particular, squeezed states (Caves, 1981; Wineland et al., 1992; Kitagawa and Ueda, 1993) were proposed early on to achieve the Heisenberg limit and thanks to experimental advances have recently shown exceptional sensitivity (Hosten, Engelsen et al., 2016).

The fundamental limits of sensitivity (quantum metrology) and strategies to achieve them have been discussed in many reviews (Giovannetti, Lloyd, and Maccone, 2004, 2006; 2011; Paris, 2009; Wiseman and Milburn, 2009) and they are not the subject of our review. In the following, we focus on the most important states and methods that have been used for entanglement-enhanced sensing.

# C. Entangled states

# 1. GHZ and N00N states

To understand the benefits that an entangled state can bring to quantum sensing, the simplest example is given by Greenberger-Horne-Zeilinger (GHZ) states. The sensing scheme is similar to a Ramsey protocol; however, if  $M$  qubit probes are available, the preparation and readout pulses are replaced by entangling operations (Fig. 13).

We can thus replace the procedure in Sec. IV.C with the following:

(1) The quantum sensors are initialized into  $|0\rangle \otimes |0\rangle \otimes \dots$ $\otimes |0\rangle \otimes |0\rangle \equiv |00\dots 0\rangle$  
(2) Using entangling gates, the quantum sensors are brought into the GHZ state  $|\psi_0\rangle = (|00\cdots 0\rangle + |11\cdots 1\rangle) / \sqrt{2}$ .  
(3) The superposition state evolves under the Hamiltonian  $\hat{H}_0$  for a time  $t$ . The superposition state picks up an enhanced phase  $\phi = M\omega_0t$ , and the state after the evolution is

$$
| \psi (t) \rangle = \frac {1}{\sqrt {2}} \left(| 0 0 \dots 0 \rangle + e ^ {i M \omega_ {0} t} | 1 1 \dots 1 \rangle\right). \tag {114}
$$

(4) Using the inverse entangling gates, the state  $|\psi (t)\rangle$  is converted back to an observable state,  $|\alpha \rangle = [ \frac{1}{2} (e^{iM\omega_0t} + 1)|0_1\rangle +\frac{1}{2} (e^{iM\omega_0t} - 1)|1_1\rangle ]|0\dots 0\rangle_{2.M}.$

(5) The final state is read out (only the first quantum probe needs to be measured in the case above). The transition probability is

$$
\begin{array}{l} p = 1 - | \langle 0 | \alpha \rangle | ^ {2} \\ = \frac {1}{2} [ 1 - \cos (M \omega_ {0} t) ] = \sin^ {2} (M \omega_ {0} t / 2). \tag {115} \\ \end{array}
$$

![](images/8ae1818b784f432c71cab11da7f0566cb9127ef5c2bab9ab034af6f3bfeca325.jpg)  
FIG. 13. Left: Ramsey scheme. Right: entangled Ramsey scheme for Heisenberg-limited sensitivity

![](images/de918d7d0bd5b39c51696c6c161d7be62d8ccd142a3acefdaf03fe42c33ef2f3.jpg)

Comparing this result with that obtained in Sec. IV.C, we see that the oscillation frequency of the signal is enhanced by a factor  $M$  by preparing a GHZ state, while the shot noise is unchanged, since we still measure only one qubit. This allows using an  $M$ -times shorter interrogation time or achieving an improvement of the sensitivity (calculated from the QCRB) by a factor  $\sqrt{M}$ . While for  $M$  uncorrelated quantum probes the QCRB of Eq. (59) becomes

$$
\Delta V _ {N, M} = \frac {1}{\gamma \sqrt {N \mathcal {F}}} = \frac {e ^ {\chi}}{\gamma t \sqrt {M N}}, \tag {116}
$$

for the GHZ state, the Fisher information reflects the state entanglement to give

$$
\Delta V _ {N, \mathrm {G H Z}} = \frac {1}{\gamma \sqrt {N} \mathcal {F} _ {\mathrm {G H Z}}} = \frac {e ^ {\chi}}{\gamma M t \sqrt {N}}. \tag {117}
$$

Heisenberg-limited sensitivity with a GHZ state was demonstrated using three entangled Be ions (Leibfried et al., 2004).

Unfortunately, the  $\sqrt{M}$  advantage in sensitivity is usually compensated by the GHZ state's increased decoherence rate (Huelga et al., 1997), which is an issue common to most entangled states. Assuming, for example, that each probe is subjected to uncorrelated dephasing noise, the rate of decoherence of the GHZ state is  $M$  time faster than for a product state. Then the interrogation time also needs to be reduced by a factor  $M$  and no net advantage in sensitivity can be obtained. This has led to the quest for different entangled states that could be more resilient to decoherence.

Similar to GHZ states,  $N00N$  states have been conceived to improve interferometry (Lee, Kok, and Dowling, 2002). They were first introduced by Yurke (1986) in the context of neutron Mach-Zender interferometry as the fermionic "response" to the squeezed states proposed by Caves (1981), for Heisenberg metrology. Using an  $M$ -particle interferometer, one can prepare an entangled Fock state,

$$
\left| \psi_ {N 0 0 N} \right\rangle = \left(\left| M \right\rangle_ {a} \left| 0 \right\rangle_ {b} + \left| 0 \right\rangle_ {a} \left| M \right\rangle_ {b}\right) / \sqrt {2}, \tag {118}
$$

where  $|N\rangle_{a}$  indicates the  $N$ -particle Fock state in spatial mode  $a$ . Already for small  $M$ , it is possible to show sensitivity beyond the standard quantum limit (Kuzmich and Mandel, 1998). If the phase is applied only to mode  $a$  of the interferometer, the phase accumulated is then

$$
\left| \psi_ {N 0 0 N} \right\rangle = \left(e ^ {i M \phi_ {a}} | M \rangle_ {a} | 0 \rangle_ {b} + | 0 \rangle_ {a} | M \rangle_ {b}\right) / \sqrt {2}, \tag {119}
$$

that is,  $M$  times larger than for a one-photon state. Experimental progress has allowed one to reach "high  $N00N$ " (with  $M > 2$ ) states (Mitchell, Lundeen, and Steinberg, 2004; Walther et al., 2004; Monz et al., 2011) by using strong nonlinearities or measurement and feed forward. They have been used not only for sensing but also for enhanced lithography (Boto et al., 2000). Still,  $N00N$  states are very fragile (Bohmann, Sperling, and Vogel, 2015) and they are afflicted by a small dynamic range.

# 2. Squeezing

Squeezed states are promising for quantum-limited sensing as they can reach sensitivity beyond the standard quantum limit. Squeezed states of light were introduced by Caves (1981) as a mean to reduce noise in interferometry experiments. One of the most impressive applications of squeezed states of light (Walls, 1983; Schnabel et al., 2010; LIGO Collaboration, 2011) has been the sensitivity enhancement of the LIGO gravitational wave detector (Aasi et al., 2013), obtained by injecting vacuum squeezed states in the interferometer.

Squeezing has also been extended to fermionic degrees of freedom (spin squeezing) (Kitagawa and Ueda, 1993) to reduce the uncertainty in spectroscopy measurements of ensemble of qubit probes. The Heisenberg uncertainty principle bounds the minimum error achievable in the measurement of two conjugate variables. While for typical states the uncertainty in the two observables is on the same order, it is possible to redistribute the fluctuations in the two conjugate observables. Squeezed states are then characterized by a reduced uncertainty in one observable at the expense of another observable. Thus, these states can help improve the sensitivity of quantum interferometry, as demonstrated by Wineland et al. (1992, 1994). Similar to GHZ and  $N00N$  states, a key ingredient to this sensitivity enhancement is entanglement (Sørensen and Mølmer, 2001; Wang and Sanders, 2003). However, the description of squeezed states is simplified by the use of a single collective angular-momentum variable.

The degree of spin squeezing can be measured by several parameters. For example, from the commutation relationship for the collective angular momentum  $\Delta J_{\alpha}\Delta J_{\beta} \geq |\langle J_{\gamma}\rangle|$ , one can naturally define a squeezing parameter

$$
\xi = \Delta J _ {\alpha} / \sqrt {| \langle J _ {\gamma} \rangle / 2}, \tag {120}
$$

with  $\xi < 1$  for squeezed states. To quantify the advantage of squeezed states in sensing, it is advantageous to directly relate squeezing to the improved sensitivity. This may be done by considering the ratio of the uncertainties on the acquired phase for the squeezed state  $\Delta \phi_{sq}$  and for the uncorrelated state  $\Delta \phi_0$  in, e.g., a Ramsey measurement. The metrology squeezing parameter, proposed by Wineland et al. (1992), is then

$$
\xi_ {R} = \left| \frac {\left| \Delta \phi \right| _ {s q}}{\left| \Delta \phi \right| _ {0}} \right| = \frac {\sqrt {N} \Delta J _ {y} (0)}{| \langle J _ {z} (0) \rangle |}. \tag {121}
$$

Early demonstrations of spin squeezing were obtained by entangling trapped ions via their shared motional modes (Meyer et al., 2001), using repulsive interactions in a Bose-Einstein condensate (Esteve et al., 2008), or partial projection by measurement (Appel et al., 2009). More recently, atomlight interactions in high-quality cavities have enabled squeezing of large ensembles atoms (Gross et al., 2010; Leroux, Schleier-Smith, and Vuletic, 2010a; Louchet-Chauvet et al., 2010; Schleier-Smith, Leroux, and Vuletic, 2010a; Bohnet et al., 2014; Cox et al., 2016; Hosten, Engelsen et al., 2016) that can perform as atomic clocks beyond the standard quantum limit. Spin squeezing can also be implemented in qubit systems (Sinha et al., 2003; Cappellaro and Lukin, 2009; Bennett et al., 2013; Auccaise et al., 2015) following the original proposal by Kitagawa and Ueda (1993).

In this context, a simple quantum sensing scheme, following the procedure in Sec. IV.C, could be constructed by replacing step 2 with the preparation of a squeezed state, so that  $|\psi_0\rangle$  is a squeezed state. The state is prepared by evolving a reference (ground) state  $|0\rangle$  under a squeezing Hamiltonian, such as the one-axis  $H_{1} = \chi J_{z}^{2}$  or two-axis  $H_{1} = \chi (J_{x}^{2} - J_{y}^{2})$  squeezing Hamiltonians. Then during the free evolution (step 3) an enhanced phase can be acquired, similar to what happens for entangled states. The most common sensing protocols with squeezed states forgo step 4 and directly measure the population difference between states  $|0\rangle$  and  $|1\rangle$ . However, imperfections in this measurement limit the sensitivity, since achieving the Heisenberg limit requires single-particle state detection. While this is difficult to obtain for large qubit numbers, recent advances show great promise (Zhang et al., 2012; Hume et al., 2013) (see also the next section on alternative detection methods). A different strategy is to more closely follow the sensing protocol for entangled states and refocus the squeezing (reintroducing step 4) before readout (Davis, Bentsen, and Schleier-Smith, 2016).

# 3. Parity measurements

A challenge in achieving the full potential of multiqubit enhanced metrology is the widespread inefficiency of quantum state readout. Metrology schemes often require single qubit readout or the measurement of complex, many-body observables. In both cases, coupling of the quantum system to the detection apparatus is inefficient, often because strong coupling would destroy the very quantum state used in the metrology task.

To reveal the properties of entangled states and to take advantage of their enhanced sensitivities, an efficient observable is the parity of the state. The parity observable was first introduced in the context of ion qubits (Bollinger et al., 1996; Leibfried et al., 2004) and it referred to the excited or ground state populations of the ions. The parity has become widely adopted for the readout of  $N00N$  states, where the parity measures the even and/or odd number of photons in a state (Gerry and Mimih, 2010). Photon parity measurements are as well used in quantum metrology with squeezed states. While the simplest method for parity detection would be via single-photon counting, and recent advances in superconducting single-photon detectors approach the required efficiency (Natarajan, Tanner, and Hadfield, 2012), photon numbers could also be measured with single-photon resolution using quantum nondemolition techniques (Imoto, Haus, and Yamamoto, 1985) that exploit nonlinear optical interactions. Until recently, parity detection for atomic ensembles containing more than a few particles was out of reach. However, recent breakthroughs in spatially resolved (Bakr et al., 2009) and cavity-based atom detection (Schleier-Smith, Leroux, and Vuletic, 2010b; Hosten, Krishnakumar et al., 2016) enabled atom counting in mesoscopic ensembles containing  $M \gtrsim 100$  atoms.

# 4. Other types of entanglement

The key difficulty with using entangled states for sensing is that they are less robust against noise. Thus, the advantage in sensitivity is compensated by a concurrent reduction in coherence time. In particular, it was demonstrated that for

frequency estimation, any nonzero value of uncorrelated dephasing noise cancels the advantage of the maximally entangled state over a classically correlated state (Huelga et al., 1997). An analogous result can be proven for magnetometry (Auzinsh et al., 2004).

Despite this limitation, nonmaximally entangled states can provide an advantage over product states (Ulam-Orgikh and Kitagawa, 2001; Shaji and Caves, 2007). Optimal states for quantum interferometry in the presence of photon loss can, for example, be found by numerical searches (Huver, Wildfeuer, and Dowling, 2008; Lee et al., 2009).

Single-mode states have also been considered as a more robust alternative to two-mode states. Examples include pure Gaussian states in the presence of phase diffusion (Genoni, Olivares, and Paris, 2011), mixed Gaussian states in the presence of loss (Aspachs et al., 2009), and single-mode variants of two-mode states (Maccone and Cillis, 2009).

Other strategies include the creation of states that are more robust to the particular noise the system is subjected to (Goldstein et al., 2011; Cappellaro et al., 2012) or the use of entangled ancillary qubits that are not quantum sensors themselves (Demkowicz-Dobrzanski and Maccone, 2014; Dür et al., 2014; Kessler et al., 2014; Huang, Macchiavello, and Maccone, 2016). These are considered in Sec. X.

# X. SENSING ASSISTED BY AUXILIARY QUBITS

In the previous section we considered potential improvements in sensitivity derived from the availability of multiple quantum systems operated in parallel. A different scenario arises when only a small number of additional quantum systems is available, or when the additional quantum systems do not directly interact with the signal to be measured. Even in this situation, however, "auxiliary qubits" can aid in the sensing task. Although auxiliary qubits—or more generally, additional quantum degrees of freedom—cannot improve the sensitivity beyond the quantum metrology limits, they can aid in reaching these limits, for example, when it is experimentally difficult to optimally initialize or read out the quantum state. Auxiliary qubits may be used to increase the effective coherence or memory time of a quantum sensor, either by operation as a quantum memory or by enabling quantum error correction.

In the following we discuss some of the schemes that have been proposed or implemented with auxiliary qubits.

# A. Quantum logic clock

Clocks based on optical transitions of an ion kept in a high-frequency trap exhibit significantly improved accuracy over more common atomic clocks. Single-ion atomic clocks currently detain the record for the most accurate optical clocks, with uncertainties of  $2.1 \times 10^{18}$  for a  $^{87}\mathrm{Sr}$  ensemble clock (Nicholson et al., 2015) and  $3.2 \times 10^{18}$  for a single trapped  $^{171}\mathrm{Yb}$  (Huntemann et al., 2016).

The remaining limitations on optical clocks are related to their long-term stability and isolation from external perturbations such as electromagnetic interference. These limitations are even more critical when such clocks are based on a string of ions in a trap, because of the associated unavoidable electric

field gradients. Only some ion species, with no quadrupolar moment, can then be used, but not all of them present a suitable transition for laser cooling and state detection beside the desired, stable clock transition. To overcome this dilemma, quantum logic spectroscopy was introduced (Schmidt et al., 2005). The key idea is to employ two ion species: a clock ion that presents a stable clock transition (and represents the quantum sensor) and a logic ion (acting as an auxiliary qubit) that is used to prepare, via a cooling transition, and read out the clock ion. The resulting "quantum logic" ion clock can thus take advantage of the most stable ion clock transitions, even when the ion cannot be efficiently read out, thus achieving impressive clock performance (Hume, Rosenband, and Wineland, 2007; Rosenband et al., 2007, 2008). Advanced quantum logic clocks may incorporate multi-ion logic (Tan et al., 2015) and use quantum algorithms for more efficient readout (Schulte et al., 2016).

# B. Storage and retrieval

The quantum state  $|\psi \rangle$  can be stored and retrieved in the auxiliary qubit. Storage can be achieved by a SWAP gate (or more simply two consecutive C-NOT gates) on the sensing and auxiliary qubits, respectively (Rosskopf et al., 2016). Retrieval uses the same two C-NOT gates in reverse order. For the example of an electron-nuclear qubit pair, C-NOT gates have been implemented both by selective pulses (Pfender et al., 2016; Rosskopf et al., 2016) and using coherent rotations (Zaiser et al., 2016).

Several useful applications of storage and retrieval have been demonstrated. The first example includes correlation spectroscopy, where two sensing periods are interrupted by a waiting time  $t_1$  (Laraoui and Meriles, 2013; Rosskopf et al., 2016; Zaiser et al., 2016). The second example includes a repetitive (quantum nondemolition) readout of the final qubit state, which can be used to reduce the classical readout noise (Jiang et al., 2009).

# C. Quantum error correction

Quantum error correction, or QEC (Shor, 1995; Nielsen and Chuang, 2000), aims at counteracting errors during quantum computation by encoding the qubit information into redundant degrees of freedom. The logical qubit is thus encoded in a subspace of the total Hilbert space (the code) such that each error considered maps the code to an orthogonal subspace, allowing detection and correction of the error. Compared to dynamical decoupling schemes, qubit protection covers the entire noise spectrum and is not limited to low-frequency noise. On the other hand, qubit protection can typically only be applied against errors that are orthogonal to the signal, because otherwise the signal itself would be "corrected." In particular, for vector fields, quantum error correction can be used to protect against noise in one spatial direction while leaving the sensor responsive to signals in the orthogonal spatial direction. Thus, quantum error correction suppresses noise according to spatial symmetry and not according to frequency.

The simplest code is the three-qubit repetition code, which corrects against one-axis noise with depth one (that is, it can

correct up to one error acting on one qubit). For example, the code  $|0\rangle_{L} = |000\rangle$  and  $|1\rangle_{L} = |111\rangle$  can correct against a single qubit flip error. Note that (Ozeri, 2013; Dur et al., 2014) equal superpositions of these two logical basis states are also optimal to achieve Heisenberg-limited sensitivity in estimating a global phase (Bollinger et al., 1996; Leibfried et al., 2004). While this seems to indicate that QEC codes could be extremely useful for metrology, the method is hampered by the fact that QEC often cannot discriminate between signal and noise. In particular, if the signal to be detected couples to the sensor in a similar way as the noise, the QEC code also eliminates the effect of the signal. This compromise between error suppression and preservation of signal sensitivity is common to other error correction methods. For example, in dynamical decoupling schemes, a separation in the frequency of noise and signal is required. Since QEC works independently of noise frequency, distinct operators for the signal and noise interactions are required. This imposes an additional condition on a QEC code: the quantum Fisher information (Giovannetti, Lloyd, and Maccone, 2011; Lu, Yu, and Oh, 2015) in the code subspace must be nonzero.

Several situations for QEC-enhanced sensing have been considered. One possible scenario is to protect the quantum sensor against a certain type of noise (e.g., single qubit, bit flip, or transverse noise), while measuring the interaction between qubits (Dür et al., 2014; Herrera-Martí et al., 2015). More generally, one can measure a many-body Hamiltonian term with a strength proportional to the signal to be estimated (Herrera-Martí et al., 2015). Since this can typically be achieved only in a perturbative way, this scheme still leads to a compromise between noise suppression and effective signal strength.

The simplest scheme for QEC is to use a single good qubit (unaffected by noise) to protect the sensor qubit (Ticozzi and Viola, 2006; Arrad et al., 2014; Kessler et al., 2014; Hirose and Cappellaro, 2016). In this scheme, which was recently implemented with NV centers (Unden et al., 2016), the qubit sensor detects a signal along one axis (e.g., a phase) while being protected against noise along a different axis (e.g., against bit flip). Because the "good" ancillary qubit can protect only against one error event (or, equivalently, suppress the error probability for continuous error), the signal acquisition must be periodically interrupted to perform a corrective step. Since the noise strength is typically much weaker than the noise fluctuation rate, the correction steps can be performed at a much slower rate compared to dynamical decoupling. Beyond single qubits, QEC was also applied to  $N00N$  states (Bergmann and van Loock, 2016). These recent results hint at the potential of QEC for sensing which has just about begun to be explored.

# XI. OUTLOOK

Despite its rich history in atomic spectroscopy and classical interferometry, quantum sensing is an excitingly new and refreshing development advancing rapidly along the sidelines of mainstream quantum engineering research. Like no other field, quantum sensing has been uniting diverse efforts in science and technology to create fundamental new opportunities and applications in metrology. Input has been

coming from traditional high-resolution optical and magnetic resonance spectroscopy, to the mathematical concepts of parameter estimation, to quantum manipulation and entanglement techniques borrowed from quantum information science. Over the last decade, and especially in the last few years, a comprehensive toolset has been established that can be applied to any type of quantum sensor. In particular, these allow operation of the sensor over a wide signal frequency range, can be adjusted to maximize sensitivity and dynamic range, and allow discrimination of different types of signals by symmetry or vector orientation. While many experiments so far made use of single qubit sensors, strategies to implement entangled multiqubit sensors with enhanced capabilities and higher sensitivity are just beginning to be explored.

One of the biggest attractions of quantum sensors is their immediate potential for practical applications. This potential is partially due to the immense range of conceived sensor implementations, starting with atomic and solid-state spin systems and continuing to electronic and vibrational degrees of freedom from the atomic to the macroscale. In fact, quantum sensors based on SQUID magnetometers and atomic vapors are already in everyday use and have installed themselves as the most sensitive magnetic field detectors currently available. Likewise, atomic clocks have become the ultimate standard in time keeping and frequency generation. Many other and more recent implementations of quantum sensors are just starting to make their appearance in many different niches. Notably, NV centers in diamond have started conquering many applications in nanoscale imaging due to their small size.

What lies ahead in quantum sensing? On the one hand, the range of applications will continue to expand as new types and more mature sensor implementations become available. Taking the impact quantum magnetometers and atomic clocks had in their particular discipline, it can be expected that quantum sensors will penetrate much of the 21st century technology and find their way into both high-end and consumer devices. Advances with quantum sensors will be strongly driven by the availability of "better" materials and more precise control, allowing their operation with longer coherence times, more efficient readout, and thus higher sensitivity.

In parallel, quantum sensing will profit from efforts in quantum technology, especially quantum computing, where many of the fundamental concepts have been developed, such as dynamical decoupling protocols, quantum storage, and quantum error correction, as well as quantum phase estimation. Vice versa, quantum sensing has become an important resource for quantum technologies as it provides much insight into the "environment" of qubits, especially through decoherence spectroscopy. A better understanding of decoherence in a particular implementation of a quantum system can help the adoption of strategies to protect the qubit and guide the engineering and materials development. The border region between quantum sensing and quantum simulation, in addition, is becoming a fertile playground for emulating and detecting many-body physics phenomena. Overall, quantum sensing has the potential to fundamentally transform our measurement capabilities, enabling higher sensitivity and precision, new measurement types, and covering atomic up to macroscopic length scales.

# ACKNOWLEDGMENTS

The authors thank Jens Boss, Dmitry Budker, Kevin Chang, Kristian Cujia, Lukasz Cywinski, Simon Gustavsson, Sebastian Hofferberth, Dominik Irber, Fedor Jelezko, Renbao Liu, Luca Lorenzelli, Tobias Rosskopf, Daniel Slichter, Jorg Wrachtrup, and Jonathan Zopes for helpful comments and discussions. C.L.D. acknowledges funding from the DIADEMS Program No. 611143 of the European Commission, the Swiss National Science

Foundation Project Grant No. 200021_137520, the Swiss National Science Foundation NCCR QSIT, and Eidgenossische Technische Hochschule Zurich Research Grant ETH-03 16-1. F.R. acknowledges funding from the Deutsche Forschungsgemeinschaft via Emmy Noether Grant No. RE 3606/1-1. P.C. acknowledges funding from the U.S. Army Research Office through MURI Grants No. W911NF-11-1-0400 and No. W911NF-15-1-0548 and by the NSF PHY0551153 and PHY1415345.

# APPENDIX TABLE OF SYMBOLS

This Appendix contains Table III, which is a list of symbols.

TABLE III. Frequently used symbols.  

<table><tr><td>Quantity</td><td>Symbol</td><td>Unit</td></tr><tr><td>Readout efficiency</td><td>C</td><td>0 ≤ C ≤ 1</td></tr><tr><td>Dynamic range</td><td>DR</td><td>...</td></tr><tr><td>ac signal: frequency</td><td>fac</td><td>Hz</td></tr><tr><td>Multipulse sensing: bandwidth</td><td>Δf</td><td>Hz</td></tr><tr><td>Hamiltonian</td><td>H(t)</td><td>Hz</td></tr><tr><td>Internal Hamiltonian</td><td>H0</td><td></td></tr><tr><td>Signal Hamiltonian</td><td>HV(t)</td><td></td></tr><tr><td>Commuting part</td><td>HV||(t)</td><td></td></tr><tr><td>Noncommuting part</td><td>HV⊥(t)</td><td></td></tr><tr><td>Control Hamiltonian</td><td>Hcontrol(t)</td><td></td></tr><tr><td>Number of qubits in ensemble; other uses</td><td>M</td><td>...</td></tr><tr><td>Multipulse sensing: filter order</td><td>k</td><td>...</td></tr><tr><td>Multipulse sensing: number of pulses</td><td>n</td><td>...</td></tr><tr><td>Number of measurements</td><td>N</td><td>...</td></tr><tr><td>Transition probability</td><td>p</td><td>p ∈ [0···1]</td></tr><tr><td>Bias point</td><td>p0</td><td></td></tr><tr><td>Change in transition probability</td><td>δp = p - p0</td><td></td></tr><tr><td>Signal spectral density</td><td>SV(ω)</td><td>Signal squared per Hz</td></tr><tr><td>Sensing time</td><td>t</td><td>s</td></tr><tr><td>Signal autocorrelation time</td><td>tc</td><td>s</td></tr><tr><td>Total measurement time</td><td>T</td><td>s</td></tr><tr><td>Relaxation or decoherence time</td><td>TX</td><td>s</td></tr><tr><td>T1relaxation time</td><td>T1</td><td></td></tr><tr><td>Dephasing time</td><td>T2*</td><td></td></tr><tr><td>Decoherence time</td><td>T2</td><td></td></tr><tr><td>Rotating frame relaxation time</td><td>T1ρ</td><td></td></tr><tr><td>Signal</td><td>V(t)</td><td>Varies</td></tr><tr><td>Parallel signal</td><td>V||(t) = Vz(t)</td><td></td></tr><tr><td>Transverse signal</td><td>V⊥(t) = [Vx2(t) + Vy2(t)]1/2</td><td></td></tr><tr><td>Vector signal</td><td>V(t) = {Vx, Vy, Vz} (t)</td><td></td></tr><tr><td>rms signal amplitude</td><td>Vrms</td><td></td></tr><tr><td>ac signal amplitude</td><td>Vpk</td><td></td></tr><tr><td>Minimum detectable signal amplitude</td><td>Vmin</td><td></td></tr><tr><td>Per unit time</td><td>vmin</td><td>Unit signal per second</td></tr><tr><td>Multipulse sensing: weighting function</td><td>W(fac, α), W(fc), etc.</td><td>...</td></tr><tr><td>Physical output of quantum sensor</td><td>x, xj</td><td>Varies</td></tr><tr><td>Multipulse sensing: modulation function</td><td>y(t)</td><td>...</td></tr><tr><td>Multipulse sensing: filter function</td><td>Y(ω)</td><td>Hz-1</td></tr><tr><td>ac signal: phase</td><td>α</td><td>...</td></tr><tr><td>Coupling parameter</td><td>γ</td><td>Hz per unit signal</td></tr><tr><td>Decoherence or transition rate</td><td>Γ</td><td>s-1</td></tr><tr><td>Quantum phase accumulated by sensor</td><td>φ</td><td>...</td></tr></table>

(Table continued)

TABLE III. (Continued)  

<table><tr><td>Quantity</td><td>Symbol</td><td>Unit</td></tr><tr><td>rms phase</td><td>φrms</td><td>···</td></tr><tr><td>Pauli matrices</td><td>ˆσ = {ˆx,ˆy,ˆz}</td><td></td></tr><tr><td>Uncertainty of transition probability</td><td>σp</td><td>···</td></tr><tr><td>Due to quantum projection noise</td><td>σp,quantum</td><td></td></tr><tr><td>Due to readout noise</td><td>σp,readout</td><td></td></tr><tr><td>Multipulse sequence pulse delay</td><td>τ</td><td>s</td></tr><tr><td>Transition frequency</td><td>ω0</td><td>Hz</td></tr><tr><td>Rabi frequency</td><td>ω1</td><td>Hz</td></tr><tr><td>Effective Rabi frequency</td><td>ωeff</td><td>Hz</td></tr><tr><td>Decoherence function</td><td>χ(t)</td><td>···</td></tr><tr><td>Basis states (energy eigenstates)</td><td>{|0&gt;,|1&gt;}</td><td>···</td></tr><tr><td>Superposition states</td><td>{|+&gt;,-&gt;}</td><td>···</td></tr><tr><td>Sensing states</td><td>{|ψ0&gt;,|ψ1&gt;}</td><td>···</td></tr></table>

# REFERENCES

Aasi, J., et al., T. L. S. Collaboration, 2013, Nat. Photonics 7, 613.  
Abragam, A., 1961, The Principles of Nuclear Magnetism, International Series of Monographs on Physics (Clarendon Press, Oxford).  
Acosta, V. M., et al., 2009, Phys. Rev. B 80, 115202.  
Aiello, C. D., M. Hirose, and P. Cappellaro, 2013, Nat. Commun. 4, 1419.  
Aigner, S., L.D. Pietra, Y. Japha, O. Entin-Wohlman, T. David, R. Salem, R. Folman, and J. Schmiedmayer, 2008, Science 319, 1226.  
Ajoy,A.,andP.Cappellaro,2012,Phys.Rev.A85,042305.  
Ajoy, A., Y.-X. Liu, K. Saha, L. Marseglia, J.-C. Jaskula, U. Bissbort, and P. Cappellaro, 2017, Proc. Natl. Acad. Sci. U.S.A. 114, 2149.  
Albrecht, A., and M. B. Plenio, 2015, Phys. Rev. A 92, 022340.  
Allan, D., 1966, Proc. IEEE 54, 221.  
Almog, I., Y. Sagi, G. Gordon, G. Bensky, G. Kurizki, and N. Davidson, 2011, J. Phys. B 44, 154006.  
Álvarez, G. A., and D. Suter, 2011, Phys. Rev. Lett. 107, 230501.  
Appel, J., P.J. Windpassinger, D. Oblak, U.B. Hoff, N. Kjargaard, and E.S. Polzik, 2009, Proc. Natl. Acad. Sci. U.S.A. 106, 10960.  
Arnold, K., E. Hajiyev, E. Paez, C. H. Lee, M. D. Barrett, and J. Bollinger, 2015, Phys. Rev. A 92, 032108.  
Arrad, G., Y. Vinkler, D. Aharonov, and A. Retzker, 2014, Phys. Rev. Lett. 112, 150801.  
Aspachs, M., J. Calsamiglia, R. Muñoz Tapia, and E. Bagan, 2009, Phys. Rev. A 79, 033834.  
Aspelmeyer, M., T. J. Kippenberg, and F. Marquardt, 2014, Rev. Mod. Phys. 86, 1391.  
Astafiev, O., Y. A. Pashkin, Y. Nakamura, T. Yamamoto, and J. S. Tsai, 2004, Phys. Rev. Lett. 93, 267007.  
Atature, M., J. Dreiser, A. Badolato, and A. Imamoglu, 2007, Nat. Phys. 3, 101.  
Auccaise, R., A.G. Araujo-Ferreira, R.S. Sarthour, I.S. Oliveira, T.J. Bonagamba, and I. Roditi, 2015, Phys. Rev. Lett. 114, 043604.  
Auzinsh, M., D. Budker, D.F. Kimball, S.M. Rochester, J.E. Stalnaker, A.O. Sushkov, and V.V. Yashchuk, 2004, Phys. Rev. Lett. 93, 173002.  
Bagci, T., et al., 2014, Nature (London) 507, 81.  
Bakr, W. S., J. I. Gillen, A. Peng, S. Folling, and M. Greiner, 2009, Nature (London) 462, 74.  
Bal, M., C. Deng, J.-L. Orgiazzi, F. Ong, and A. Lupascu, 2012, Nat. Commun. 3, 1324.  
Balabas, M. V., T. Karaulanov, M. P. Ledbetter, and D. Budker, 2010, Phys. Rev. Lett. 105, 070801.

Balasubramanian, G., et al., 2008, Nature (London) 455, 648.  
Balasubramanian, G., et al., 2009, Nat. Mater. 8, 383.  
Ban, M., S. Kitajima, and F. Shibata, 2009, Phys. Lett. A 373, 3614.  
Bar-Gill, N., L. Pham, C. Belthangady, D. Le Sage, P. Cappellaro, J. Maze, M. Lukin, A. Yacoby, and R. Walsworth, 2012, Nat. Commun. 3, 858.  
Barnes, E., M. S. Rudner, F. Martins, F. K. Malinowski, C. M. Marcus, and F. Kuemmeth, 2016, Phys. Rev. B 93, 121407.  
Baumgart, I., J.-M. Cai, A. Retzker, M. B. Plenio, and C. Wunderlich, 2016, Phys. Rev. Lett. 116, 240801.  
Baugratz, T., and A. Datta, 2016, Phys. Rev. Lett. 116, 030801.  
Bennett, S. D., N. Y. Yao, J. Otterbach, P. Zoller, P. Rabl, and M. D. Lukin, 2013, Phys. Rev. Lett. 110, 156402.  
Bergeal, N., F. Schackert, M. Metcalfe, R. Vijay, V. E. Manucharyan, L. Frunzio, D. E. Prober, R. J. Schoelkopf, S. M. Girvin, and M. H. Devoret, 2010, Nature (London) 465, 64.  
Bergli, J., and L. Faoro, 2007, Phys. Rev. B 75, 054515.  
Bergmann, M., and P. van Loock, 2016, Phys. Rev. A 94, 012311.  
Berry, D. W., B. Higgins, S. Bartlett, M. Mitchell, G. Pryde, and H. Wiseman, 2009, Phys. Rev. A 80, 052114.  
Bialczak, R.C., et al., 2007, Phys. Rev. Lett. 99, 187006.  
Biercuk, M.J., A.C. Doherty, and H. Uys, 2011, J. Phys. B 44, 154002.  
Biercuk, M. J., H. Uys, J. W. Britton, A. P. VanDevender, and J. J. Bollinger, 2010, Nat. Nanotechnol. 5, 646.  
Biercuk, M. J., H. Uys, A. P. VanDevender, N. Shiga, W. M. Itano, and J. J. Bollinger, 2009, Nature (London) 458, 996.  
Bitter, T., and D. Dubbers, 1987, Phys. Rev. Lett. 59, 251.  
Bloom, B.J., T.L. Nicholson, J.R. Williams, S.L. Campbell, M. Bishop, X. Zhang, W. Zhang, S.L. Bromley, and J. Ye, 2014, Nature (London) 506, 71.  
Blundell, S.J., 1999, Contemp. Phys. 40, 175.  
Bohmann, M., J. Sperling, and W. Vogel, 2015, Phys. Rev. A 91, 042332.  
Bohnet, J.G., K. Cox, M. Norcia, J. Weiner, Z. Chen, and J.K. Thompson, 2014, Nat. Photonics 8, 731.  
Bohnet, J. G., B. C. Sawyer, J. W. Britton, M. L. Wall, A. M. Rey, M. Foss-Feig, and J. J. Bollinger, 2016, Science 352, 1297.  
Bollinger, J. J., W. M. Itano, D. J. Wineland, and D. J. Heinzen, 1996, Phys. Rev. A 54, R4649.  
Bonato, C., M. S. Blok, H. T. Dinani, D. W. Berry, M. L. Markham, D. J. Twitchen, and R. Hanson, 2016, Nat. Nanotechnol. 11, 247.  
Boss, J. M., K. Chang, J. Armijo, K. Cujia, T. Rosskopf, J. R. Maze, and C. L. Degen, 2016, Phys. Rev. Lett. 116, 197601.

Boss, J. M., K. Cujia, J. Zopes, and C. L. Degen, 2017, Science 356, 837.  
Boto, A. N., P. Kok, D. S. Abrams, S. L. Braunstein, C. P. Williams, and J. P. Dowling, 2000, Phys. Rev. Lett. 85, 2733.  
Braginskii, V. B., and Y. I. Vorontsov, 1975, Sov. Phys. Usp. 17, 644.  
Braunstein, S. L., 1996, Phys. Lett. A 219, 169.  
Braunstein, S. L., and C. M. Caves, 1994, Phys. Rev. Lett. 72, 3439.  
Braunstein, S. L., C. M. Caves, and G. J. Milburn, 1996, Ann. Phys. (N.Y.) 247, 135.  
Brewer, J. H., and K. M. Crowe, 1978, Annu. Rev. Nucl. Part. Sci. 28, 239.  
Brida, G., M. Genovese, and I. R. Berchera, 2010, Nat. Photonics 4, 227.  
Brownnutt, M., M. Kumph, P. Rabl, and R. Blatt, 2015, Rev. Mod. Phys. 87, 1419.  
Budakian, R., H. J. Mamin, B. W. Chui, and D. Rugar, 2005, Science 307, 408.  
Budker, D., and D.F.J. Kimball, 2013, Optical Magnetometry (Cambridge University Press, Cambridge, UK).  
Budker, D., and M. Romalis, 2007, Nat. Phys. 3, 227.  
Bylander, J., T. Duty, and P. Delsing, 2005, Nature (London) 434, 361.  
Bylander, J., S. Gustavsson, F. Yan, F. Yoshihara, K. Harrabi, G. Fitch, D. G. Cory, and W. D. Oliver, 2011, Nat. Phys. 7, 565.  
Campbell, W. C., and P. Hamilton, 2017, J. Phys. B 50, 064002.  
Candés, E. J., J. K. Romberg, and T. Tao, 2006, Commun. Pure Appl. Math. 59, 1207.  
Cappellaro, P., 2012, Phys. Rev. A 85, 030301(R).  
Cappellaro, P., G. Goldstein, J. S. Hodges, L. Jiang, J. R. Maze, A. S. Sorensen, and M. D. Lukin, 2012, Phys. Rev. A 85, 032336.  
Cappellaro, P., and M. D. Lukin, 2009, Phys. Rev. A 80, 032311.  
Carr, H. Y., and E. M. Purcell, 1954, Phys. Rev. 94, 630.  
Casanova, J., Z. Wang, J. F. Haase, and M. B. Plenio, 2015, Phys. Rev. A 92, 042304.  
Castellanos-Beltran, M. A., K. D. Irwin, G. C. Hilton, L. R. Vale, and K. W. Lehnert, 2008, Nat. Phys. 4, 929.  
Caves, C. M., 1981, Phys. Rev. D 23, 1693.  
Cervantes, F.G., L. Kumanchik, J. Pratt, and J.M. Taylor, 2014, Appl. Phys. Lett. 104, 221111.  
Chabuda, K., I.D. Leroux, and R. Demkowicz-Dobrzański, 2016, New J. Phys. 18, 083035.  
Chang, K., A. Eichler, J. Rhensius, L. Lorenzelli, and C. L. Degen, 2017, Nano Lett., 17, 2367.  
Chaste, J., A. Eichler, J. Moser, G. Ceballos, R. Rurali, and A. Bachtold, 2012, Nat. Nanotechnol. 7, 301.  
Chernobrod, B. M., and G. P. Berman, 2005, J. Appl. Phys. 97, 014903.  
Chipaux, M., L. Toraille, C. Larat, L. Morvan, S. Pezzagna, J. Meijer, and T. Debuisschert, 2015, Appl. Phys. Lett. 107, 233502.  
Christle, D. J., A. L. Falk, P. Andrich, P. V. Klimov, J. U. Hassan, N. Son, E. Janzon, T. Ohshima, and D. D. Awschalom, 2015, Nat. Mater. 14, 160.  
Clarke, J., and A. I. Braginski, 2004, The SQUID handbook (Wiley-VCH, Weinheim).  
Clarke, J., and F. K. Wilhelm, 2008, Nature (London) 453, 1031.  
Clevenson, H., M. E. Trusheim, C. Teale, T. Schrder, D. Braje, and D. Englund, 2015, Nat. Phys. 11, 393.  
Cole, J., and L. Hollenberg, 2009, Nanotechnology 20, 495401.  
Cooper, A., E. Magesan, H. Yum, and P. Cappellaro, 2014, Nat. Commun. 5, 3141.  
Cox, K.C., G.P. Greve, J.M. Weiner, and J.K. Thompson, 2016, Phys. Rev. Lett. 116, 093602.

Cummings, F. W., 1962, Am. J. Phys. 30, 898.  
Cywinski, L., 2014, Phys. Rev. A 90, 042307.  
Cywiński, L., R. M. Lutchyn, C. P. Nave, and S. DasSarma, 2008, Phys. Rev. B 77, 174509.  
Dang, H. B., A. C. Maloof, and M. V. Romalis, 2010, Appl. Phys. Lett. 97, 151110.  
D'Angelo, M., M. V. Chekhova, and Y. Shih, 2001, Phys. Rev. Lett. 87, 013602.  
Davis, E., G. Bentsen, and M. Schleier-Smith, 2016, Phys. Rev. Lett. 116, 053601.  
Degen, C. L., 2008, Appl. Phys. Lett. 92, 243111.  
Degen, C. L., M. Poggio, H. J. Mamin, C. T. Rettner, and D. Rugar, 2009, Proc. Natl. Acad. Sci. U.S.A. 106, 1313.  
Demkowicz-Dobrzanski, R., and L. Maccone, 2014, Phys. Rev. Lett. 113, 250801.  
de Sousa, R., 2009, "Electron spin as a spectrometer of nuclear-spin noise and other fluctuations," in *Electron Spin Resonance and Related Phenomena in Low-Dimensional Structures*, edited by M. Fanciulli (Springer, Berlin/Heidelberg), pp. 183-220.  
Deutsch, D., 1985, Proc. R. Soc. A 400, 97.  
DeVience, S. J., et al., 2015, Nat. Nanotechnol. 10, 129.  
Dial, O., M. Shulman, S. Harvey, H. Bluhm, V. Umansky, and A. Yacoby, 2013, Phys. Rev. Lett. 110, 146804.  
DiVincenzo, D. P., 2000, Fortschr. Phys. 48, 771.  
Doherty, M. W., et al., 2014, Phys. Rev. Lett. 112, 047601.  
Dolde, F., et al., 2011, Nat. Phys. 7, 459.  
Dovzhenko, Y., F. Casola, S. Schlotter, T. X. Zhou, F. Bttner, R. L. Walsworth, G. S. D. Beach, and A. Yacoby, 2016, arXiv:1611.00673.  
Drewsen, M., 2015, Physica B (Amsterdam) 460, 105.  
Dür, W., M. Skotiniotis, F. Frowis, and B. Kraus, 2014, Phys. Rev. Lett. 112, 080801.  
Dussaux, A., et al., 2016, Nat. Commun. 7, 12430.  
Edamatsu, K., R. Shimizu, and T. Itoh, 2002, Phys. Rev. Lett. 89, 213601.  
Elzerman, J. M., R. Hanson, L. H. Willems van Beveren, B. Witkamp, L. M. K. Vandersypen, and L. P. Kouwenhoven, 2004, Nature (London) 430, 431.  
Esteve, J., C. Gross, A. Weller, S. Giovanazzi, and M. K. Oberthaler, 2008, Nature (London) 455, 1216.  
Facon, A., E.-K. Dietsche, D. Grosso, S. Haroche, J.-M. Raimond, M. Brune, and S. Gleyzes, 2016, Nature (London) 535, 262.  
Fagaly, R. L., 2006, Rev. Sci. Instrum. 77, 101101.  
Fan, H., S. Kumar, J. Sedlacek, H. Kbler, S. Karimkashi, and J. P. Shaffer, 2015, J. Phys. B 48, 202001.  
Fang, J., and J. Qin, 2012, Sensors 12, 6331.  
Faoro, L., and L. Viola, 2004, Phys. Rev. Lett. 92, 117905.  
Faust, T., J. Rieger, M. J. Seitner, J. P. Kotthaus, and E. M. Weig, 2013, Nat. Phys. 9, 485.  
Fedder, H., F. Dolde, F. Rempp, T. Wolf, P. Hemmer, F. Jelezko, and J. Wrachtrup, 2011, Appl. Phys. B 102, 497.  
Fernholz, T., H. Krauter, K. Jensen, J. F. Sherson, A. S. Sørensen, and E. S. Polzik, 2008, Phys. Rev. Lett. 101, 073601.  
Fonseca, E. J. S., C. H. Monken, and S. Pdua, 1999, Phys. Rev. Lett. 82, 2868.  
Forstner, S., E. Sheridan, J. Knittel, C. L. Humphreys, G. A. Brawley, H. Rubinsztein-Dunlop, and W. P. Bowen, 2014, Adv. Mater. 26, 6348.  
Fortagh, J., H. Ott, S. Kraft, A. Gunther, and C. Zimmermann, 2002, Phys. Rev. A 66, 041604.  
Frey, V. M., S. Mavadia, L. M. Norris, W. de Ferranti, D. Lucarelli, L. Viola, and M. J. Biercuk, 2017, arXiv:1704.02050.

Fu, C.-C., H.-Y. Lee, K. Chen, T.-S. Lim, H.-Y. Wu, P.-K. Lin, P.-K. Wei, P.-H. Tsao, H.-C. Chang, and W. Fann, 2007, Proc. Natl. Acad. Sci. U.S.A. 104, 727.  
Fu, R. R., et al., 2014, Science 346, 1089.  
Genoni, M. G., S. Olivares, and M. G. A. Paris, 2011, Phys. Rev. Lett. 106, 153603.  
Gerry, C. C., and J. Mimih, 2010, Contemp. Phys. 51, 497.  
Giovannetti, V., S. Lloyd, and L. Maccone, 2004, Science 306, 1330.  
Giovannetti, V., S. Lloyd, and L. Maccone, 2006, Phys. Rev. Lett. 96, 010401.  
Giovannetti, V., S. Lloyd, and L. Maccone, 2011, Nat. Photonics 5, 222.  
Gisin, N., G. Ribordy, W. Tittel, and H. Zbinden, 2002, Rev. Mod. Phys. 74, 145.  
Gleyzes, S., S. Kuhr, C. Guerlin, J. Bernu, S. DelÉglise, U. Busk Hoff, M. Brune, J.-M. Raimond, and S. Haroche, 2007, Nature (London) 446, 297.  
Goldstein, G., P. Cappellaro, J.R. Maze, J.S. Hodges, L. Jiang, A.S. Sorensen, and M.D. Lukin, 2011, Phys. Rev. Lett. 106, 140502.  
Goldstein, G., M. D. Lukin, and P. Cappellaro, 2010, arXiv:1001.4804.  
Griffiths, R., and C.-S. Niu, 1996, Phys. Rev. Lett. 76, 3228.  
Gross, D., Y.-K. Liu, S. T. Flammia, S. Becker, and J. Eisert, 2010, Phys. Rev. Lett. 105, 150401.  
Gruber, A., A. Drabenstedt, C. Tietz, L. Fleury, J. Wrachtrup, and C. v. Borczyskowski, 1997, Science 276, 2012.  
Gullion, T., D. B. Baker, and M. S. Conradi, 1990, J. Magn. Reson. 89, 479.  
Gustavson, T. L., P. Bouyer, and M. A. Kasevich, 1997, Phys. Rev. Lett. 78, 2046.  
Gustavson, T. L., A. Landragin, and M. A. Kasevich, 2000, Classical Quantum Gravity 17, 2385.  
Hahn, E. L., 1950, Phys. Rev. 80, 580.  
Halbertal, D., et al., 2016, Nature (London) 539, 407.  
Hald, J., J. L. Srensen, C. Schori, and E. S. Polzik, 1999, Phys. Rev. Lett. 83, 1319.  
Hall, L. T., P. Kehayias, D. A. Simpson, A. Jarmola, A. Stacey, D. Budker, and L. C. L. Hollenberg, 2016, Nat. Commun. 7, 10211.  
Hanbury Brown, R., and R. Q. Twiss, 1956, Nature (London) 178, 1046.  
Happer, W., and H. Tang, 1973, Phys. Rev. Lett. 31, 273.  
Haroche,S.,2013,Rev.Mod.Phys.85,1083.  
Hatridge, M., R. Vijay, D. H. Slichter, J. Clarke, and I. Siddiqi, 2011, Phys. Rev. B 83, 134501.  
Hayes, D., K. Khodjasteh, L. Viola, and M. J. Biercuk, 2011, Phys. Rev. A 84, 062323.  
Helstrom, C. W., 1967, Phys. Lett. A 25, 101.  
Herrera-Martí, D.A., T. Gefen, D. Aharonov, N. Katz, and A. Retzker, 2015, Phys. Rev. Lett. 115, 200501.  
Herrmann, P.P., J. Hoffnagle, N. Schlumpf, V.L. Telegdi, and A. Weis, 1986, J. Phys. B 19, 1271.  
Higgins, B. L., D. W. Berry, S. D. Bartlett, M. W. Mitchell, H. M. Wiseman, and G. J. Pryde, 2009, New J. Phys. 11, 073023.  
Higgins, B. L., D. W. Berry, S. D. Bartlett, H. M. Wiseman, and G. J. Pryde, 2007, Nature (London) 450, 393.  
Hinkley, N., J. A. Sherman, N. B. Phillips, M. Schioppo, N. D. Lemke, K. Beloy, M. Pizzocaro, C. W. Oates, and A. D. Ludlow, 2013, Science 341, 1215.  
Hirose, M., C. D. Aiello, and P. Cappellaro, 2012, Phys. Rev. A 86, 062320.  
Hirose, M., and P. Cappellaro, 2016, Nature (London) 532, 77.  
Hodges, J. S., N. Y. Yao, D. Maclaurin, C. Rastogi, M. D. Lukin, and D. Englund, 2013, Phys. Rev. A 87, 032118.

Ho Eom, B., P. K. Day, H. G. LeDuc, and J. Zmuidzinas, 2012, Nat. Phys. 8, 623.  
Holevo, A., 1982, Probabilistic and Statistical Aspects of Quantum Theory (North-Holland, Amsterdam).  
Holland, M. J., and K. Burnett, 1993, Phys. Rev. Lett. 71, 1355.  
Hollberg, L., et al., 2001, IEEE J. Quantum Electron. 37, 1502.  
Hosten, O., N. J. Engelsen, R. Krishnakumar, and M. A. Kasevich, 2016, Nature (London) 529, 505.  
Hosten, O., R. Krishnakumar, N.J. Engelsen, and M.A. Kasevich, 2016, Science 352, 1552.  
Huang, Z., C. Macchiavello, and L. Maccone, 2016, Phys. Rev. A 94, 012101.  
Huelga, S.F., C. Macchiavello, T. Pellizzari, A.K. Ekert, M.B. Plenio, and J.I. Cirac, 1997, Phys. Rev. Lett. 79, 3865.  
Hume, D. B., T. Rosenband, and D. J. Wineland, 2007, Phys. Rev. Lett. 99, 120502.  
Hume, D. B., I. Stroescu, M. Joos, W. Muessel, H. Strobel, and M. K. Oberthaler, 2013, Phys. Rev. Lett. 111, 253001.  
Hunteumann, N., C. Sanner, B. Lipphardt, C. Tamm, and E. Peik, 2016, Phys. Rev. Lett. 116, 063001.  
Huver, S. D., C. F. Wildfeuer, and J. P. Dowling, 2008, Phys. Rev. A 78, 063828.  
Ilani, S., J. Martin, E. Teitelbaum, J.H. Smet, D. Mahalu, V. Umansky, and A. Yacoby, 2004, Nature (London) 427, 328.  
Imoto, N., H. A. Haus, and Y. Yamamoto, 1985, Phys. Rev. A 32, 2287.  
Itano, W.M., J.C. Bergquist, J.J. Bollinger, J.M. Gilligan, D.J. Heinzen, F.L. Moore, M.G. Raizen, and D.J. Wineland, 1993, Phys. Rev. A 47, 3554.  
Ithier, G., et al., 2005, Phys. Rev. B 72, 134519.  
Jaklevic, R. C., J. Lambe, J. E. Mercereau, and A. H. Silver, 1965, Phys. Rev. 140, A1628.  
Jenke, T., P. Geltenbort, H. Lemmel, and H. Abele, 2011, Nat. Phys. 7, 468.  
Jenke, T., et al., 2014, Phys. Rev. Lett. 112, 151105.  
Jensen, K., N. Leefer, A. Jarmola, Y. Dumeige, V. Acosta, P. Kehayias, B. Patton, and D. Budker, 2014, Phys. Rev. Lett. 112, 160802.  
Jensen, K., et al., 2016, Sci. Rep. 6, 29638.  
Jiang, L., et al., 2009, Science 326, 267.  
Joas, T., A.M. Waeber, G. Braunbeck, and F. Reinhard, 2017, arXiv:1702.06710.  
Jones, J. A., S. D. Karlen, J. Fitzsimons, A. Ardavan, S. C. Benjamin, G. A. D. Briggs, and J. J. L. Morton, 2009, Science 324, 1166.  
Jones, M. P. A., C. J. Vale, D. Sahagun, B. V. Hall, and E. A. Hinds, 2003, Phys. Rev. Lett. 91, 080401.  
Kardjilov, N., I. Manke, M. Strobl, A. Hilger, W. Treimer, M. Meissner, T. Krist, and J. Banhart, 2008, Nat. Phys. 4, 399.  
Kasevich, M., and S. Chu, 1992, Appl. Phys. B 54, 321.  
Kastner, M. A., 1992, Rev. Mod. Phys. 64, 849.  
Kessler, E. M., I. Lovchinsky, A. O. Sushkov, and M. D. Lukin, 2014, Phys. Rev. Lett. 112, 150802.  
Khodjasteh, K., and D. A. Lidar, 2005, Phys. Rev. Lett. 95, 180501.  
Kimmich, R., and E. Anoardo, 2004, Prog. Nucl. Magn. Reson. Spectrosc. 44, 257.  
Kitaev, A. Y., 1995, arXiv:quant-ph/9511026.  
Kitagawa, M., and M. Ueda, 1993, Phys. Rev. A 47, 5138.  
Kitching, J., S. Knappe, and E. Donley, 2011, IEEE Sens. J. 11, 1749.  
Kohlhaas, R., A. Bertoldi, E. Cantin, A. Aspect, A. Landragin, and P. Bouyer, 2015, Phys. Rev. X 5, 021011.  
Kolkowitz, S., et al., 2015, Science 347, 1129.  
Kominis, K., T. W. Kornack, J. C. Allred, and M. V. Romalis, 2003, Nature (London) 422, 596.

Kornack, T. W., R. K. Ghosh, and M. V. Romalis, 2005, Phys. Rev. Lett. 95, 230801.  
Kotler, S., N. Akerman, Y. Glickman, A. Keselman, and R. Ozeri, 2011, Nature (London) 473, 61.  
Kotler, S., N. Akerman, Y. Glickman, and R. Ozeri, 2013, Phys. Rev. Lett. 110, 110503.  
Krause, A. G., M. Winger, T. D. Blasius, Q. Lin, and O. Painter, 2012, Nat. Photonics 6, 768.  
Kroutvar, M., Y. Ducommun, D. Heiss, M. Bichler, D. Schuh, G. Abstreiter, and J. J. Finley, 2004, Nature (London) 432, 81.  
Kübler, H., J. P. Shaffer, T. Baluktsian, R. Löw, and T. Pfau, 2010, Nat. Photonics 4, 112.  
Kucsko, G., P. C. Maurer, N. Y. Yao, M. Kubo, H. J. Noh, P. K. Lo, H. Park, and M. D. Lukin, 2013, Nature (London) 500, 54.  
Kuehn, S., R. F. Loring, and J. A. Marohn, 2006, Phys. Rev. Lett. 96, 156103.  
Kuzmich, A., and L. Mandel, 1998, Quantum and Semiclassical Optics: Journal of the European Optical Society Part B 10, 493 [http://stacks.iop.org/1355-5111/10/i=3/a=008].  
Labaziewicz, J., Y. Ge, D. R. Leibrandt, S. X. Wang, R. Shewmon, and I. L. Chuang, 2008, Phys. Rev. Lett. 101, 180602.  
Lang, J. E., R. B. Liu, and T. S. Monteiro, 2015, Phys. Rev. X 5, 041016.  
Lanting, T., et al., 2009, Phys. Rev. B 79, 060509.  
Laraoui, A., and C. A. Meriles, 2013, ACS Nano 7, 3403.  
Ledbetter, M. P., K. Jensen, R. Fischer, A. Jarmola, and D. Budker, 2012, Phys. Rev. A 86, 052116.  
Lee, H., P. Kok, and J. P. Dowling, 2002, J. Mod. Opt. 49, 2325.  
Lee, T.-W., S.D. Huver, H. Lee, L. Kaplan, S.B. McCracken, C. Min, D.B. Uskov, C.F. Wildfeuer, G. Veronis, and J.P. Dowling, 2009, Phys. Rev. A 80, 063803.  
Leibfried, D., M. D. Barrett, T. Schaetz, J. Britton, J. Chiaverini, W. M. Itano, J. D. Jost, C. Langer, and D. J. Wineland, 2004, Science 304, 1476.  
Leibfried, D., et al., 2005, Nature (London) 438, 639.  
Lenz, J., 1990, Proc. IEEE 78, 973.  
Leroux, I. D., M. H. Schleier-Smith, and V. Vuletic, 2010a, Phys. Rev. Lett. 104, 073602.  
Leroux, I. D., M. H. Schleier-Smith, and V. Vuletic, 2010b, Phys. Rev. Lett. 104, 250801.  
Le Sage, D., K. Arai, D.R. Glenn, S.J. DeVience, L.M. Pham, L. Rahn-Lee, M.D. Lukin, A. Yacoby, A. Komeili, and R.L. Walsworth, 2013, Nature (London) 496, 486.  
Le Sage, D., L. M. Pham, N. Bar-Gill, C. Belthangady, M. D. Lukin, A. Yacoby, and R. L. Walsworth, 2012, Phys. Rev. B 85, 121202.  
LIGO Collaboration, 2011, Nat. Phys. 7, 962.  
Li, K., et al., 2016, Phys. Rev. D 93, 062001.  
Livanov, M., A. Kozlov, A. Korinevski, V. Markin, and S. Sinel'nikova, 1978, Dokl. Akad. Nauk SSSR 238, 253 [http://europepmc.org/abstract/MED/620639].  
Lloyd, S., 2008, Science 321, 1463.  
Lopaeva, E. D., I. Ruo Berchera, I. P. Degiovanni, S. Olivares, G. Brida, and M. Genovese, 2013, Phys. Rev. Lett. 110, 153603.  
Loretz, M., J. M. Boss, T. Rosskopf, H. J. Mamin, D. Rugar, and C. L. Degen, 2015, Phys. Rev. X 5, 021009.  
Loretz, M., S. Pezzagna, J. Meijer, and C. L. Degen, 2014, Appl. Phys. Lett. **104**, 033102.  
Loretz, M., T. Rosskopf, and C. L. Degen, 2013, Phys. Rev. Lett. 110, 017602.  
Louchet-Chauvet, A., J. Appel, J.J. Renema, D. Oblak, N. Kjaergaard, and E.S. Polzik, 2010, New J. Phys. 12, 065032.  
Lovchinsky,I.,et al.,2016,Science 351,836.

Lovchinsky,I.,et al.,2017,Science 355,503.  
Lu, X., S. Yu, and C. H. Oh, 2015, Nat. Commun. 6, 7282.  
Maccone, L., and G. D. Cillis, 2009, Phys. Rev. A 79, 023812.  
Macklin, C., K. OBrien, D. Hover, M. E. Schwartz, V. Bolkhovsky, X. Zhang, W. D. Oliver, and I. Siddiqi, 2015, Science 350, 307.  
Magesan, E., A. Cooper, and P. Cappellaro, 2013, Phys. Rev. A 88, 062109.  
Magesan, E., A. Cooper, H. Yum, and P. Cappellaro, 2013, Phys. Rev. A 88, 032107.  
Maiwald, R., D. Leibfried, J. Britton, J. C. Bergquist, G. Leuchs, and D. J. Wineland, 2009, Nat. Phys. 5, 551.  
Maletinsky, P., S. Hong, M. S. Grinolds, B. Hausmann, M. D. Lukin, R. L. Walsworth, M. Loncar, and A. Yacoby, 2012, Nat. Nanotechnol. 7, 320.  
Mamin, H. J., M. Kim, M. H. Sherwood, C. T. Rettner, K. Ohno, D. D. Awschalom, and D. Rugar, 2013, Science 339, 557.  
Martin, J., N. Akerman, G. Ulbricht, T. Lohmann, J. H. Smet, K. von Klitzing, and A. Yacoby, 2008, Nat. Phys. 4, 144.  
Martinis, J., S. Nam, J. Aumentado, and C. Urbina, 2002, Phys. Rev. Lett. 89, 117901.  
Maze, J. R., et al., 2008, Nature (London) 455, 644.  
McGuinness, L. P., et al., 2011, Nat. Nanotechnol. 6, 358.  
Mück, M., C. Welzel, and J. Clarke, 2003, Appl. Phys. Lett. 82, 3266.  
Medford, J. and L. Cywinski, C. Barthel, C.M. Marcus, M.P. Hanson, and A.C. Gossard, 2012, Phys. Rev. Lett. 108, 086802.  
Meriles, C. A., L. Jiang, G. Goldstein, J. S. Hodges, J. Maze, M. D. Lukin, and P. Cappellaro, 2010, J. Chem. Phys. 133, 124105.  
Meyer, V., M. A. Rowe, D. Kielpinski, C. A. Sackett, W. M. Itano, C. Monroe, and D. J. Wineland, 2001, Phys. Rev. Lett. 86, 5870.  
Mezei,F.,1972,Z.Phys.255,146.  
Mitchell, M. W., J. S. Lundeen, and A. M. Steinberg, 2004, Nature (London) 429, 161.  
Monz, T., P. Schindler, J. T. Barreiro, M. Chwalla, D. Nigg, W. A. Coish, M. Harlander, W. Hansel, M. Hennrich, and R. Blatt, 2011, Phys. Rev. Lett. 106, 130506.  
Morello, A., et al., 2010, Nature (London) 467, 687.  
Moser, J., J. Guttinger, A. Eichler, M. J. Esplandiu, D. E. Liu, M. I. Dykman, and A. Bachtold, 2013, Nat. Nanotechnol. 8, 493.  
Muhonen, J. T., et al., 2014, Nat. Nanotechnol. 9, 986.  
Myers, B. A., A. Das, M. C. Dartialh, K. Ohno, D. D. Awschalom, and A. C. B. Jayich, 2014, Phys. Rev. Lett. 113, 027602.  
Nader, C., N. Björsell, and P. Händel, 2011, Signal Processing 91, 1347.  
Nagata, T., R. Okamoto, J. L. O'Brien, K. Sasaki, and S. Takeuchi, 2007, Science 316, 726.  
Nakamura, Y., Y. Pashkin, and J. Tsai, 1999, Nature (London) 398, 786.  
Nakamura, Y., Y. Pashkin, and J. Tsai, 2002, Phys. Rev. Lett. 88, 047901.  
Natarajan, C. M., M. G. Tanner, and R. H. Hadfield, 2012, Supercond. Sci. Technol. 25, 063001.  
Nesvizhevsky, V. V., et al., 2002, Nature (London) 415, 297.  
Neumann, P., et al., 2013, Nano Lett. 13, 2738.  
Nicholson, T. L., et al., 2015, Nat. Commun. 6, 6896.  
Nielsen, M. A., and I. L. Chuang, 2000, Quantum computation and quantum information (Cambridge University Press, Cambridge/New York).  
Nogues, G., A. Rauschenbeutel, S. Osnaghi, M. Brune, J.M. Raimond, and S. Haroche, 1999, Nature (London) 400, 239.  
Norris, L. M., G. A. Paz-Silva, and L. Viola, 2016, Phys. Rev. Lett. 116, 150503.  
Novotny, L., 2010, Am. J. Phys. 78, 1199.

Nusran, M., M. M. Ummal, and M. V. G. Dutt, 2012, Nat. Nanotechnol. 7, 109.  
Ockeloen, C.F., R. Schmied, M.F. Riedel, and P. Treutlein, 2013, Phys. Rev. Lett. 111, 143001.  
O'Connell, A. D., et al., 2010, Nature (London) 464, 697.  
Oelker, E., T. Isogai, J. Miller, M. Tse, L. Barsotti, N. Mavalvala, and M. Evans, 2016, Phys. Rev. Lett. 116, 041102.  
Osterwalder, A., and F. Merkt, 1999, Phys. Rev. Lett. 82, 1831.  
Ozeri, R., 2013, arXiv:1310.3432.  
Packard, M., and R. Varian, 1954, Phys. Rev. 93, 939.  
Pang, S., and A. N. Jordan, 2016, arXiv:1606.02166.  
Paris, M. G. A., 2009, Int. J. Quantum. Inform. 07, 125.  
Paz-Silva, G. A., and L. Viola, 2014, Phys. Rev. Lett. 113, 250501.  
Pelliccione, M., A. Jenkins, P. Ovartchaiyapong, C. Reetz, E. Emmanouilidou, N. Ni, and A. C. B. Jayich, 2016, Nat. Nanotechnol. 11, 700.  
Peters, A., K. Y. Chung, and S. Chu, 1999, Nature (London) 400, 849.  
Pfender, M., N. Aslam, H. Sumiya, S. Onoda, P. Neumann, J. Isoya, C. Meriles, and J. Wrachtrup, 2016, arXiv:1610.05675.  
Puentes, G., G. Waldherr, P. Neumann, G. Balasubramanian, and J. Wrachtrup, 2014, Sci. Rep. 4, 4677.  
Pustelny, S., et al., 2013, Ann. Phys. (Berlin) 525, 659.  
Riedel, M. F., P. Böhi, Y. Li, T. W. Hänsch, A. Sinatra, and P. Treutlein, 2010, Nature (London) 464, 1170.  
Romach, Y., et al., 2015, Phys. Rev. Lett. 114, 017601.  
Rondin, L., J. P. Tetienne, T. Hingant, J. F. Roch, P. Maletinsky, and V. Jacques, 2014, Rep. Prog. Phys. 77, 056503.  
Rondin, L., J. P. Tetienne, S. Rohart, A. Thiaville, T. Hingant, P. Spincelli, J. F. Roch, and V. Jacques, 2013, Nat. Commun. 4, 2279.  
Rondin, L., J. P. Tetienne, P. Spinicelli, C. dal Savio, K. Karrai, G. Dantelle, A. Thiaville, S. Rohart, J. F. Roch, and V. Jacques, 2012, Appl. Phys. Lett. 100, 153118.  
Rosenband, T., et al., 2007, Phys. Rev. Lett. 98, 220801.  
Rosenband, T., et al., 2008, Science 319, 1808.  
Rosskopf, T., A. Dussaux, K. Ohashi, M. Loretz, R. Schirhagl, H. Watanabe, S. Shikata, K.M. Itoh, and C.L. Degen, 2014, Phys. Rev. Lett. 112, 147602.  
Rosskopf, T., J. Zopes, J.M. Boss, and C.L. Degen, 2016, arXiv:1610.03253.  
Rugar, D., R. Budakian, H. J. Mamin, and B. W. Chui, 2004, Nature (London) 430, 329.  
Said, R. S., D. W. Berry, and J. Twamley, 2011, Phys. Rev. B 83, 125410.  
Sakurai, J. J., and J. Napolitano, 2011, Modern quantum mechanics (Addison-Wesley, Reading, MA).  
Schafer-Nolte, E., L. Schlipf, M. Ternes, F. Reinhard, K. Kern, and J. Wrachtrup, 2014, Phys. Rev. Lett. 113, 217204.  
Schirhagl, R., K. Chang, M. Loretz, and C. L. Degen, 2014, Annu. Rev. Phys. Chem. 65, 83.  
Schleier-Smith, M. H., I. D. Leroux, and V. Vuletic, 2010a, Phys. Rev. A 81, 021804.  
Schleier-Smith, M. H., I. D. Leroux, and V. Vuletic, 2010b, Phys. Rev. Lett. 104, 073604.  
Schmid-Lorch, D., T. Haberle, F. Reinhard, A. Zappe, M. Slota, L. Bogani, A. Finkler, and J. Wrachtrup, 2015, Nano Lett. 15, 4942.  
Schmidt, P., T. Rosenband, C. Langer, W. Itano, J. Bergquist, and D. Wineland, 2005, Science 309, 749.  
Schmitt, S., et al., 2017, Science 356, 832.  
Schnabel, R., N. Mavalvala, D. E. McClelland, and P. K. Lam, 2010, Nat. Commun. 1, 121.  
Schoelkopf, R.J., 1998, Science 280, 1238.

Schoelkopf, R.J., A.A. Clerk, S.M. Girvin, K.W. Lehnert, and M.H. Devoret, 2003, "Qubits as spectrometers of quantum noise," in Quantum Noise in Mesoscopic Physics, edited by Y.V. Nazarov (Springer Netherlands, Dordrecht), pp. 175-203.  
Schulte, M., N. Lorch, I.D. Leroux, P.O. Schmidt, and K. Hammerer, 2016, Phys. Rev. Lett. 116, 013002.  
Schwartz, O., J. M. Levitt, R. Tenne, S. Itzhakov, Z. Deutsch, and D. Oron, 2013, Nano Lett. 13, 5832.  
Sedlacek, J. A., A. Schwettmann, H. Kbler, R. Lw, T. Pfau, and J. P. Shaffer, 2012, Nat. Phys. 8, 819.  
Sewell, R.J., M. Koschorreck, M. Napolitano, B. Dubost, N. Behbood, and M.W. Mitchell, 2012, Phys. Rev. Lett. 109, 253605.  
Shah, V., S. Knappe, P. D. D. Schwindt, and J. Kitching, 2007, Nat. Photonics 1, 649.  
Shah, V., G. Vasilakis, and M. V. Romalis, 2010, Phys. Rev. Lett. 104, 013601.  
Shaji, A., and C. M. Caves, 2007, Phys. Rev. A 76, 032111.  
Shi, F., X. Kong, P. Wang, F. Kong, N. Zhao, R. Liu, and J. Du, 2014, Nat. Phys. 10, 21.  
Shi, F., et al., 2015, Science 347, 1135.  
Shiga, N., and M. Takeuchi, 2012, New J. Phys. 14, 023034.  
Shor, P. W., 1994, in Proceedings of the 35th Annual Symposium on Foundations of Computer Science, pp. 124-134.  
Shor, P. W., 1995, Phys. Rev. A 52, R2493.  
Simmonds, M., W. Fertig, and R. Giffard, 1979, IEEE Trans. Magn. 15, 478.  
Sinha, S., J. Emerson, N. Boulant, E. M. Fortunato, T. F. Havel, and D. G. Cory, 2003, Quantum Inf. Process. 2, 433.  
Slichter, C.P., 1996, Principles of Magnetic Resonance (Springer-Verlag, Berlin), 3rd ed.  
Slichter, D. H., R. Vijay, S. J. Weber, S. Boutin, M. Boissonneault, J. M. Gambetta, A. Blais, and I. Siddiqi, 2012, Phys. Rev. Lett. 109, 153601.  
Slusher, R. E., L. W. Hollberg, B. Yurke, J. C. Mertz, and J. F. Valley, 1985, Phys. Rev. Lett. 55, 2409.  
Smiciklas, M., J. M. Brown, L. W. Cheuk, S. J. Smullin, and M. V. Romalis, 2011, Phys. Rev. Lett. 107, 171604.  
Sonier, J. E., J. H. Brewer, and R. F. Kiefl, 2000, Rev. Mod. Phys. 72, 769.  
Sorensen, A. S., and K. Mølmer, 2001, Phys. Rev. Lett. 86, 4431.  
Stark, A., N. Aharon, T. Unden, D. Louzon, A. Huck, A. Retzker, U. L. Andersen, and F. Jelezko, 2017, arXiv:1706.04779.  
Staudacher, T., F. Shi, S. Pezzagna, J. Meijer, J. Du, C. A. Meriles, F. Reinhard, and J. Wrachtrup, 2013, Science 339, 561.  
Steinert, S., F. Ziem, L. T. Hall, A. Zappe, M. Schweikert, N. Gutz, A. Aird, G. Balasubramanian, L. Hollenberg, and J. Wrachtrup, 2013, Nat. Commun. 4, 1607.  
Sushkov, A. O., I. Lovchinsky, N. Chisholm, R. L. Walsworth, H. Park, and M. D. Lukin, 2014, Phys. Rev. Lett. 113, 197601.  
Sushkov,A.O.,et al.,2014,Nano Lett.14,6443.  
Suter, D., and G. A. Álvarez, 2016, Rev. Mod. Phys. 88, 041001.  
Swallows, M. D., T. H. Loftus, W. C. Griffith, B. R. Heckel, E. N. Fortson, and M. V. Romalis, 2013, Phys. Rev. A 87, 012102.  
Takamoto, M., F.-L. Hong, R. Higashi, and H. Katori, 2005, Nature (London) 435, 321.  
Tan, S.-H., B. I. Erkmen, V. Giovannetti, S. Guha, S. Lloyd, L. Maccone, S. Pirandola, and J. H. Shapiro, 2008, Phys. Rev. Lett. 101, 253601.  
Tan, T. R., J. P. Gaebler, Y. Lin, Y. Wan, R. Bowler, D. Leibfried, and D. J. Wineland, 2015, Nature (London) 528, 380.  
Tao, Y., and C. L. Degen, 2015, Nano Lett. 15, 7893.

Taylor, J. M., P. Cappellaro, L. Childress, L. Jiang, D. Budker, P. R. Hemmer, A. Yacoby, R. Walsworth, and M. D. Lukin, 2008, Nat. Phys. 4, 810.  
Taylor, M. A., J. Janousek, V. Daria, J. Knittel, B. Hage, BacherHans-A., and W. P. Bowen, 2013, Nat. Photonics 7, 229.  
Tetienne, J. P., et al., 2014, Science 344, 1366.  
Tetienne, J. P., et al., 2015, Nat. Commun. 6, 6733.  
Thiel, L., D. Rohner, M. Ganzhorn, P. Appel, E. Neu, B. Muller, R. Kleiner, D. Koelle, and P. Maletinsky, 2016, Nat. Nanotechnol. 11, 677.  
Ticozzi, F., and L. Viola, 2006, Phys. Rev. A 74, 052328.  
Toyli, D. M., C. F. de las Casas, D. J. Christie, V. V. Dobrovitski, and D. D. Awschalom, 2013, Proc. Natl. Acad. Sci. U.S.A. 110, 8417.  
Tsang, M., H. M. Wiseman, and C. M. Caves, 2011, Phys. Rev. Lett. 106, 090401.  
Ulam-Orgikh, D., and M. Kitagawa, 2001, Phys. Rev. A 64, 052106.  
Unden, T., et al., 2016, Phys. Rev. Lett. 116, 230502.  
Vamivakas, A.N., C.-Y. Lu, C. Matthiesen, Y. Zhao, S. Flt, A. Badolato, and M. Atatre, 2010, Nature (London) 467, 297.  
van der Sar, T., F. Casola, R. Walsworth, and A. Yacoby, 2015, Nat. Commun. 6.  
Vasyukov, D., et al., 2013, Nat. Nanotechnol. 8, 639.  
Vengalattore, M., J. M. Higbie, S. R. Leslie, J. Guzman, L. E. Sadler, and D. M. Stamper-Kurn, 2007, Phys. Rev. Lett. 98, 200801.  
Vijay, R., D. H. Slichter, and I. Siddiqi, 2011, Phys. Rev. Lett. 106, 110502.  
Viola, L., and S. Lloyd, 1998, Phys. Rev. A 58, 2733.  
Vion, D., A. Aassime, A. Cottet, P. Joyez, H. Pothier, C. Urbina, D. Esteve, and M. Devorett, 2002, Science 296, 886.  
Waldherr, G., J. Beck, P. Neumann, R. Said, M. Nitsche, M. Markham, D. J. Twitchen, J. Twamley, F. Jelezko, and J. Wrachtrup, 2012, Nat. Nanotechnol. 7, 105.  
Wallraff, A., D. I. Schuster, A. Blais, L. Frunzio, R. S. Huang, J. Majer, S. Kumar, S. M. Girvin, and R. J. Schoelkopf, 2004, Nature (London) 431, 162.  
Walls, D. F., 1983, Nature (London) 306, 141.  
Walsh, J. L., 1923, Am. J. Math. 45, 5.  
Walther, P., J.-W. Pan, M. Aspelmeyer, R. Ursin, S. Gasparoni, and A. Zeilinger, 2004, Nature (London) 429, 158.  
Wang, X., and B.C. Sanders, 2003, Phys. Rev. A 68, 012101.  
Wasilewski, W., K. Jensen, H. Krauter, J. J. Renema, M. V. Balabas, and E. S. Polzik, 2010, Phys. Rev. Lett. 104, 133601.  
Waters, G. S., and P. D. Francis, 1958, J. Sci. Instrum. 35, 88.  
Weston, E., 1931, "Exposure Meter," U.S. Patent 2016469.  
Widmann, M., et al., 2015, Nat. Mater. 14, 164.  
Wineland, D. J., J. J. Bollinger, W. M. Itano, and D. J. Heinzen, 1994, Phys. Rev. A 50, 67.

Wineland, D. J., J. J. Bollinger, W. M. Itano, F. L. Moore, and D. J. Heinzen, 1992, Phys. Rev. A 46, R6797.  
Wiseman, H., and G. Milburn, 2009, Quantum measurement and control (Cambridge University Press, Cambridge, England).  
Wolf, T., P. Neumann, K. Nakamura, H. Sumiya, T. Ohshima, J. Isoya, and J. Wrachtrup, 2015, Phys. Rev. X 5, 041001.  
Wolfe, C. S., V. P. Bhallamudi, H. L. Wang, C. H. Du, S. Manuilov, R. M. Teeling-Smith, A. J. Berger, R. Adur, F. Y. Yang, and P. C. Hammel, 2014, Phys. Rev. B 89, 180406.  
Woodman, K., P. Franks, and M. Richards, 1987, Journal of Navigation 40, 366.  
Wrachtrup, J., C. von Borczyskowski, J. Bernard, M. Orrit, and R. Brown, 1993a, Nature (London) 363, 244.  
Wrachtrup, J., C. von Borczyskowski, J. Bernard, M. Orrit, and R. Brown, 1993b, Phys. Rev. Lett. 71, 3565.  
Xia, H., A. B.-A. Baranga, D. Hoffman, and M. V. Romalis, 2006, Appl. Phys. Lett. 89, 211104.  
Xiang, G. Y., B. L. Higgins, D. W. Berry, H. M. Wiseman, and G. J. Pryde, 2011, Nat. Photonics 5, 43.  
Xu, N., F. Jiang, Y. Tian, J. Ye, F. Shi, H. Lv, Y. Wang, J. Wrachtrup, and J. Du, 2016, Phys. Rev. B 93, 161117.  
Yan, F., J. Bylander, S. Gustavsson, F. Yoshihara, K. Harrabi, D. G. Cory, T. P. Orlando, Y. Nakamura, J.-S. Tsai, and W. D. Oliver, 2012, Phys. Rev. B 85, 174521.  
Yan, F., S. Gustavsson, J. Bylander, X. Jin, F. Yoshihara, D. G. Cory, Y. Nakamura, T. P. Orlando, and W. D. Oliver, 2013, Nat. Comms. 4, 2337.  
Yoo, M. J., T. A. Fulton, H. F. Hess, R. L. Willett, L. N. Dunkleberger, R. J. Chichester, L. N. Pfeiffer, and K. W. West, 1997, Science 276, 579.  
Yoshihara, F., K. Harrabi, A.O. Niskanen, Y. Nakamura, and J.S. Tsai, 2006, Phys. Rev. Lett. 97, 167001.  
Yoshihara, F., Y. Nakamura, F. Yan, S. Gustavsson, J. Bylander, W. Oliver, and J.-S. Tsai, 2014, Phys. Rev. B 89, 020503.  
Young, K. C., and K. B. Whaley, 2012, Phys. Rev. A 86, 012314.  
Yuge, T., S. Sasaki, and Y. Hirayama, 2011, Phys. Rev. Lett. 107, 170504.  
Yurke, B., 1986, Phys. Rev. Lett. 56, 1515.  
Zaiser, S., T. Rendler, I. Jakobi, T. Wolf, S. Lee, S. Wagner, V. Bergholm, T. Schulte-herbruggen, P. Neumann, and J. Wrachtrup, 2016, Nat. Commun. 7, 12279.  
Zanche, N. D., C. Barmet, J. A. Nordmeyer-Massner, and K. P. Pruessmann, 2008, Magn. Reson. Med. 60, 176.  
Zhang, H., R. McConnell, S. Cuk, Q. Lin, M. H. Schleier-Smith, I. D. Leroux, and V. Vuletic, 2012, Phys. Rev. Lett. 109, 133603.  
Zhao, N., J. Wrachtrup, and R. B. Liu, 2014, Phys. Rev. A 90, 032319.