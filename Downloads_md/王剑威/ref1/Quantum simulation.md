# Quantum simulation

I. M. Georgescu

CEMS, RIKEN, Saitama, 351-0198, Japan

S. Ashhab*

CEMS, RIKEN, Saitama, 351-0198, Japan

and Qatar Environment and Energy Research Institute, Doha, Qatar

Franco Nori†

CEMS, RIKEN, Saitama, 351-0198, Japan, Department of Physics, University of Michigan, Ann Arbor, Michigan 48109-1040, USA, and Department of Physics, Korea University, Seoul 136-713, Korea

(published 10 March 2014)

Simulating quantum mechanics is known to be a difficult computational problem, especially when dealing with large systems. However, this difficulty may be overcome by using some controllable quantum system to study another less controllable or accessible quantum system, i.e., quantum simulation. Quantum simulation promises to have applications in the study of many problems in, e.g., condensed-matter physics, high-energy physics, atomic physics, quantum chemistry, and cosmology. Quantum simulation could be implemented using quantum computers, but also with simpler, analog devices that would require less control, and therefore, would be easier to construct. A number of quantum systems such as neutral atoms, ions, polar molecules, electrons in semiconductors, superconducting circuits, nuclear spins, and photons have been proposed as quantum simulators. This review outlines the main theoretical and experimental aspects of quantum simulation and emphasizes some of the challenges and promises of this fast-growing field.

DOI: 10.1103/RevModPhys.86.153

PACS numbers: 03.65.-w, 03.67.Ac

# CONTENTS

I. Introduction 153  
II. The Problem 155  
III. Definitions 157  
IV. Digital and Analog Quantum Simulation 157  
A. Digital quantum simulation 158  
B. Analog quantum simulation 160  
C. Quantum-information-inspired algorithms for the classical simulation of quantum systems 161  
V. Resource Estimation and Fault Tolerance 161  
A. Resource estimation 161  
B.Decoherence and errors 163  
VI. Physical Realizations 164  
A. Atoms and ions 165  
B. Nuclear and electronic spins 167  
C. Superconducting circuits 168  
D. Photons 169  
E. Other systems 169  
F.Current state of the art 170  
VII. Applications 171  
A. Condensed-matter physics 171  
1.Hubbard model 171  
2. Spin models 171  
3.Quantum phase transitions 172  
4.Disordered and frustrated systems 174

5. Spin glasses 174  
6. Superconductivity 175  
7.Metamaterials 175  
8.Topological order 175

B. High-energy physics 176  
C.Cosmology 177  
D. Atomic physics 177  
E.Quantum chemistry 178  
F.Open quantum systems 178  
G.Quantum chaos 179  
H.Nuclear physics 179  
I. Interferometry 179  
J. Other applications 179

VIII. Concluding Remarks 179

Acknowledgments 180

References 180

# I. INTRODUCTION

Thirty years ago, in the early 1980s, it had become clear that simulating quantum mechanics was a very challenging problem (Manin, 1980; Feynman, 1982). One obvious difficulty is the large amount of computer memory needed to store the quantum state of a large physical system. This state is described by a number of parameters that grows exponentially with the system size (which is generally defined as the number of particles or degrees of freedom in the system). In particular, one needs to keep track of the probability amplitudes for all the possible classical configurations

TABLE I. Strengths and weaknesses of some of the proposed and demonstrated quantum simulators.  

<table><tr><td>Quantum simulator</td><td>Strength</td><td>Weakness</td></tr><tr><td>Neutral atoms</td><td>Scaling*</td><td>Individual control and readout</td></tr><tr><td>Trapped ions</td><td>Individual control and readout*</td><td>Scaling</td></tr><tr><td>Cavity arrays</td><td>Individual control and readout</td><td>Scaling</td></tr><tr><td>Electronic spins (quantum dots)</td><td>Individual control and readout,* tunability</td><td>Scaling</td></tr><tr><td>Superconducting circuits</td><td>Individual control and readout,* tunability</td><td>Scaling (some recent progress)</td></tr><tr><td>Photons (linear optics)</td><td>Flexibility*</td><td>Scaling</td></tr><tr><td>Nuclear spins (NMR)</td><td>Well-established, readily available technology*</td><td>Scaling, no individual control</td></tr></table>

*An asterisk means that the feature has been experimentally demonstrated. By scaling we mean controlling an array of at least a few tens of qubits. By individual control we refer to the ability of controlling and measuring each individual qubit. The weaknesses refer to the actual experimental implementations.

of the system. Furthermore, simulating the temporal evolution of the system requires a number of operations that also increases exponentially with the size of the system. This exponential explosion is unavoidable, unless approximation methods (e.g., Monte Carlo methods) are used. However, depending on the specifics of the problem under study, good approximations are not always available or they also face some limitations. Therefore, the simulation of quantum systems in general remains a hard task even for today's supercomputers.

A proposed solution to this problem came in the new type of computer envisaged by Richard Feynman (Feynman, 1982)—the quantum computer. In fact, as has become clear over the past three decades, a quantum computer promises to do much more than simulating quantum mechanics, and today quantum computation and quantum information theory are very active research fields [see, e.g., Nielsen and Chuang (2000), Schleich and Walther (2008), and Stolze and Suter (2008))]. Feynman realized at the time that a quantum machine would itself experience an exponential explosion, but with good consequences. The machine would have the capacity to contain an exponentially large amount of information without using an exponentially large amount of physical resources, thus making it a natural tool to perform quantum simulation. Despite the great importance of his insight, however, he was not very specific about how his proposed quantum mechanical computer was supposed to function or how the simulation itself would be realized, as can be seen from the following quote:

"Let the computer itself be built of quantum mechanical elements which obey quantum mechanical laws." (Feynman, 1982).

More than a decade later, it was shown (Lloyd, 1996) that a quantum computer (i.e., an ensemble of well-defined qubits that can be initialized, measured, and on which universal quantum gates can be performed) can indeed act as a universal quantum simulator. Here the word universal refers to the fact that, except for changes in the programs that it runs, the same machine is capable of tackling vastly different problems. However, a quantum computer (as defined above) is not necessarily required for implementing quantum simulation. Simpler quantum devices that mimic the evolution of other quantum systems in an analog manner could be used for this task (note that these are not universal simulators, but rather problem-specific machines). It is therefore expected that

practical quantum simulation will become a reality well before full-fledged quantum computers.

In recent years, the interest in quantum simulation has been growing rapidly, and the reason for this is twofold. First, there are a large number of potential applications of quantum simulation in physics, chemistry, and even biology. Second, the technologies required for the coherent control of quantum systems have matured enough to allow for the physical implementation of practical quantum simulation in the very near future. In fact, some proof-of-principle experiments on quantum simulation have already been realized [see, e.g., Greiner et al. (2002), Leibfried et al. (2002), Friedenauer et al. (2008), Neeley et al. (2009), Gerritsma et al. (2010), Kim et al. (2010), and Lanyon et al. (2010)].

Quantum simulation will provide a valuable tool that researchers from numerous fields will want to add to their toolbox of research methods. For instance, in condensed-matter physics, quantum simulation would allow the study of many difficult problems, such as quantum phase transitions, quantum magnetism, or high- $T_{c}$  superconductivity. Other potential application areas include high-energy physics, quantum chemistry, cosmology, and nuclear physics.

With the latest advances in the coherent manipulation of quantum systems (Ladd et al., 2010; Buluta, Ashhab, and Nori, 2011), such as atoms in optical lattices, trapped ions, nuclear spins, superconducting circuits, or spins in semiconductors, practical applications of quantum simulation can be expected in the coming years. Several research groups are now actively aiming at the experimental realization of quantum simulators with tens of qubits, which would be the first practical applications in which quantum computers outperform their classical counterparts.

There is by now a sizable literature on quantum simulation, especially papers published in the past decade. However, besides the brief overview of quantum simulators by Buluta and Nori (2009) and the specialized reviews focused on cold atoms (Jaksch and Zoller, 2005; Lewenstein et al., 2007; Bloch, Dalibard, and Nascimbene, 2012), ions (Blatt and Roos, 2012; Schneider, Porras, and Schaetz, 2012), photons (Aspuru-Guzik and Walther, 2012), superconducting circuits (Houck, Tureci, and Koch, 2012), and quantum chemistry (Kassal et al., 2011; Lu et al., 2012), a global review of the field is missing. Moreover, a comprehensive, pedagogic introduction to the subject would benefit researchers just entering the field, as well as those already working on

TABLE II. Potential applications of quantum simulators and the physical systems in which they could be implemented, along with relevant references. We note that this is not an exhaustive list.  

<table><tr><td colspan="2">Application</td><td>Proposed implementation</td></tr><tr><td colspan="3">Condensed-matter physics:</td></tr><tr><td></td><td>Hubbard models</td><td>Atoms (Jaksch et al., 1998; Greiner et al., 2002)*Ions (Deng, Porras, and Cirac, 2008)Polar molecules (Ortner et al., 2009)Quantum dots (Byrnes et al., 2008)Cavities (Greentree et al., 2006; Hartmann, Brandao, and Plenio, 2006;Angelakis, Santos, and Bose, 2007)</td></tr><tr><td></td><td>Spin models</td><td>Atoms (Jané et al., 2003; Garcia-Ripoll, Martin-Delgado, and Cirac, 2004, Simon et al., 2011; Struck et al., 2011)*Ions (Jané et al., 2003; Porras and Cirac, 2004b; Deng, Porras, and Cirac, 2005;Bermudez, Porras, and Martin-Delgado, 2009; Edwards et al., 2010; Lanyon et al., 2011*; Kim et al., 2011; Britton et al., 2012)*Cavities (Cho, Angelakis, and Bose, 2008a; Chen et al., 2010)Nuclear spins on diamond surface (Cai et al., 2013)Superconducting circuits (Tsokomos, Ashhab, and Nori, 2010)Electrons on helium (Mostame and Schützhold, 2008)</td></tr><tr><td></td><td>Quantum phase transitions</td><td>Atoms (Greiner et al., 2002)*Polar molecules (Capogrosso-Sansone et al., 2010; Pollet et al., 2010)Ions (Retzker et al., 2008; Friedenauer et al., 2008)*; Ivanov et al., 2009; Giorgi, Paganelli, and Galve, 2010NMR (Peng, Du, and Suter, 2005; Roumpos, Master, and Yamamoto, 2007; Zhang et al., 2008)Superconducting circuits (van Oudenaarden and Mooij, 1996)*</td></tr><tr><td></td><td>Spin glasses</td><td>DQS (Lidar and Biham, 1997)Superconducting circuits (Tsomokos, Ashhab, and Nori, 2008)</td></tr><tr><td></td><td>Disordered systems</td><td>Atoms (Schulte et al., 2005; Fallani et al., 2007*;Billy et al., 2008; Roati et al., 2008)*Ions (Bermudez, Martin-Delgado, and Porras, 2010)Superconducting circuits (Garcia-Ripoll, Solano, and Martin-Delgado, 2008)NMR (Álvarez and Suter, 2010; Banerjee et al., 2013)*</td></tr><tr><td></td><td>Frustrated systems</td><td>Ions (Porras and Cirac, 2006b; Kim et al., 2010)*Photons (Ma et al., 2011)*</td></tr><tr><td></td><td>High-TC superconductivity</td><td>DQS (Yamaguchi and Yamamoto, 2002)Quantum dots (Manousakis, 2002)</td></tr><tr><td></td><td>BCS pairing</td><td>NMR (Yang et al., 2006)*</td></tr><tr><td></td><td>BCS-BEC crossover</td><td>Atoms (Regal, Greiner, and Jin, 2004; Zwierlein et al., 2005)*</td></tr><tr><td></td><td>Metamaterials</td><td>Superconducting circuits (Rakhmanov et al., 2008)</td></tr><tr><td></td><td>Time-symmetry breaking</td><td>Superconducting circuits (Koch et al., 2010)</td></tr><tr><td></td><td>Topological order</td><td>Atoms (Aguado et al., 2008)Polar molecules (Micheli, Brennen, and Zoller, 2006)Linear optics (Lu et al., 2009)*Superconducting circuits (You et al., 2010)</td></tr></table>

*Experimental realizations.

quantum simulation and looking for a quick reference guide. Since quantum simulation is a subject of interest to a broad audience, this review attempts to provide a self-contained description of the current status of theoretical and experimental research on the subject. However, given the breadth of the topics touched by quantum simulation, not all technical details can be provided here, and the interested reader is directed to the relevant references instead.

The remainder of this review is organized as follows. Sections II-V discuss in some detail the basic theory. Readers interested only in the physical implementations of quantum simulation can concentrate on Sec. VI, while those interested in the applications of quantum simulation can concentrate on Sec. VII. Tables I-III provide quick reference guides for the content of Secs. VI and VII. In Sec. VIII

we discuss the challenges and prospects of quantum simulation.

# II. THE PROBLEM

"The rule of simulation that I would like to have is that the number of computer elements required to simulate a large physical system is only to be proportional to the space-time volume of the physical system. I don't want to have an explosion" (Feynman, 1982).

We consider a rather general quantum simulation problem, namely, that of finding the state of a quantum system

TABLE III. Continuation of Table II, but focused on applications other than condensed-matter physics. As in Table II, this is not an exhaustive list.  

<table><tr><td colspan="2">Application</td><td>Proposed implementation</td></tr><tr><td colspan="3">High-energy physics:</td></tr><tr><td></td><td>Lattice gauge theories</td><td>DQS (Byrnes and Yamamoto, 2006) 
Atoms (Büchler et al., 2005)</td></tr><tr><td></td><td>Dirac particles</td><td>Ions (Lamata et al., 2007; Casanova et al., 2010, 2011; Gerritsma et al., 2010; Rusin and Zawadzki, 2010) 
Atoms (Goldman et al., 2009; Hou, Yang, and Liu, 2009; Cirac, Maraner, and Pachos, 2010)</td></tr><tr><td></td><td>Nucleons</td><td>Photons (Semiao and Paternostro, 2012)</td></tr><tr><td colspan="3">Cosmology:</td></tr><tr><td></td><td>Unruh effect</td><td>Ions (Alsing, Dowling, and Milburn, 2005)</td></tr><tr><td></td><td>Hawking radiation</td><td>Atoms (Giovanazzi, 2005) 
Ions (Horstmann et al., 2010) 
Superconducting circuits (Nation et al., 2009)</td></tr><tr><td></td><td>Universe expansion</td><td>BEC (Fischer and Schützhold, 2004) 
Ions (Schützhold and Mostame, 2005; Menicucci, Olson, and Milburn, 2010)</td></tr><tr><td colspan="3">Atomic physics:</td></tr><tr><td></td><td>Cavity QED</td><td>Superconducting circuits (You and Nori, 2003; Wallraff et al., 2004)*</td></tr><tr><td></td><td>Cooling</td><td>Superconducting circuits (Grajcar et al., 2008); You and Nori, 2011)</td></tr><tr><td colspan="3">Open systems:</td></tr><tr><td></td><td></td><td>NMR (Tseng et al., 2000)* 
Ions (Piilo and Maniscalco, 2006; Barreiro et al., 2011)* 
Superconducting circuits (Li et al., 2013)*</td></tr><tr><td colspan="3">Chemistry:</td></tr><tr><td></td><td>Thermal rate calculations</td><td>DQS (Lidar and Wang, 1999)</td></tr><tr><td></td><td>Molecular energies</td><td>DQS (Aspiru-Guzik et al., 2005) 
Linear optics (Lanyon et al., 2010)* 
NMR (Du et al., 2010)*</td></tr><tr><td></td><td>Chemical reactions</td><td>DQS (Kassal et al., 2008) 
Quantum dots (Smirnov et al., 2007)</td></tr><tr><td colspan="3">Quantum chaos:</td></tr><tr><td></td><td></td><td>NMR (Weinstein et al., 2002)* 
Linear optics (Howell and Yeaze, 1999)</td></tr><tr><td colspan="3">Interferometry:</td></tr><tr><td></td><td></td><td>Ions (Leibfried et al., 2002; Hu, Feng, and Lee, 2012; Lau and James, 2012) 
Photons (Aaronson and Arkhipov, 2011; Broome et al., 2013*; Crespi et al., 2013; Spring et al., 2013; Tillmann et al., 2013)* 
Superconducting circuits (Zhou, Dong et al., 2008; Liao et al., 2010)</td></tr><tr><td colspan="3">Other applications:</td></tr><tr><td></td><td>Schrödinger equation</td><td>DQS (Boghosian and Taylor, 1998a)</td></tr><tr><td></td><td>Quantum thermodynamics</td><td>Superconducting circuits (Quan et al., 2006, 2007)</td></tr></table>

*Experimental realizations.

described by the wave function  $|\varphi \rangle$  at some time  $t$  and computing the value of some physical quantity of interest. Focusing for simplicity on time-independent Hamiltonians (denoted  $H$ ), the solution of the Schrödinger equation:

$$
i \hbar \frac {d}{d t} | \phi \rangle = H | \varphi \rangle \tag {1}
$$

is given by  $|\varphi(t)\rangle = \exp\{-i\hbar Ht\} |\varphi(0)\rangle$ . In order to compute  $|\phi(t)\rangle$  numerically, it is first necessary to discretize the problem such that it can be encoded in the computer memory. As mentioned earlier, the amount of memory required for representing quantum systems grows exponentially with the system size, and so does the number of operations required to simulate the time evolution. For instance, representing the state of  $N$  spin-1/2 particles requires  $2^{N}$  numbers (namely, the

complex probability amplitudes for the different spin configurations), and this is without including the particles' motional degrees of freedom. Calculating the time evolution of this system requires exponentiating a  $2^{N} \times 2^{N}$  matrix. We take as an example the standard "threshold"  $N = 40$  frequently cited in the literature (Lloyd, 1996; Cirac and Zoller, 2003; de Raedt et al., 2007; Friedenauer et al., 2008). This implies storing  $2^{40} \approx 10^{12}$  numbers for  $|\varphi\rangle$ . (For the moment, we will not worry about the Hamiltonian with its  $2^{40} \times 2^{40} \approx 10^{24}$  matrix elements, because for realistic physical problems the Hamiltonian has a very regular structure and just encoding it in the computer memory does not suffer from the exponential-explosion problem.) Assuming single precision, about  $\sim 3.2 \times 10^{13}$  bits, that is 4 TB (terabytes) are required to represent the spin state of 40 particles in a computer memory. In order to put this in perspective, the U.S. Library of

Congress has almost 160 TB of data. Double the number of spins, and  $\sim 3.8 \times 10^{25}$  bits (or  $5 \times 10^{12}$  TB) would be required. This is roughly  $10^{4}$  times more than the amount of information stored by humankind in 2007, which was estimated to be  $2.4 \times 10^{21}$  bits (Hilbert and Lopez, 2011).

Classical stochastic methods, namely, Monte Carlo algorithms (Suzuki, 1993), have been developed as a way of tackling the difficult problem of simulating large quantum systems. These methods allow the evaluation of phase space integrals for many-body problems in a time that scales polynomially with the number of particles. Such stochastic methods generally work well when the functions being integrated do not change sign (and ideally vary slowly with respect to the relevant variables), such that sampling the function at a relatively small number of points gives a good approximation to the integral of the function. For some quantum systems, especially fermionic and frustrated systems, the numerical evaluation of the integrals encounters the problem of sampling with nonpositive-semidefinite weight functions, which is the so-called sign problem (Troyer and Wiese, 2005). This results in an exponential growth of the statistical error, and hence the required simulation time, with the number of particles, which cancels the advantage of the Monte Carlo methods. Other methods of solving quantum many-body problems such as density functional theory, meanfield theories, many-body perturbation theories or Green's function-based methods, coupled clusters, etc. [see Thouless (1972), Zagoskin (1998), and Fetter and Walecka (2003)] have similar validity criteria that restrict their applicability to well-behaved systems.

# III. DEFINITIONS

The alternative simulation method initially proposed by Feynman, i.e., quantum simulation, can be loosely defined as simulating a quantum system by quantum mechanical means. This very general definition allows us to include three types of simulation:

- digital quantum simulation,  
- analog quantum simulation, and  
- quantum-information-inspired algorithms for the classical simulation of quantum systems.

These are discussed in some detail in the following sections.

By quantum simulator, we understand a controllable quantum system used to simulate or emulate other quantum systems [see, e.g., Buluta and Nori (2009)].

We denote the state of the simulated system by  $|\varphi \rangle$ . The system evolves from the initial state  $|\varphi (0)\rangle$  to  $|\varphi (t)\rangle$  via the unitary transformation  $U = \exp \{-i\hbar H_{\mathrm{sys}}t\}$ , where  $H_{\mathrm{sys}}$  is the Hamiltonian of the system. The quantum simulator is a controllable system: the initial state  $|\psi (0)\rangle$  can be prepared, the desired unitary evolution  $U^{\prime} = \exp \{-i\hbar H_{\mathrm{sim}}t\}$  with  $H_{\mathrm{sim}}$  being the controllable Hamiltonian of the simulator can be engineered, and the final state  $|\psi (t)\rangle$  can be measured. If a mapping between the system and the simulator [i.e., between  $|\varphi (0)\rangle$  and  $|\psi (0)\rangle$ , and between  $|\varphi (t)\rangle$  and  $|\psi (t)\rangle$ ] exists, then the system can be simulated. The basic

![](images/e7b350b11a2b88d668c68ad325eac0ed1ed6a5fb45ecece85d46557c06b43c53.jpg)  
FIG. 1 (color online). Schematic representation of a quantum system and a corresponding quantum simulator. The quantum state  $|\varphi(0)\rangle$  evolves to  $|\varphi(t)\rangle$  via the unitary transformation  $U = \exp\{-i\hbar H_{\mathrm{sys}}t\}$ . The quantum simulator evolves from the state  $|\psi(0)\rangle$  to  $|\psi(t)\rangle$  via  $U' = \exp\{-i\hbar H_{\mathrm{sim}}t\}$ . The simulator is designed such that there is a mapping between the simulator and the simulated system, in particular, the mappings  $|\varphi(0)\rangle \leftrightarrow |\psi(0)\rangle$ ,  $|\varphi(t)\rangle \leftrightarrow |\psi(t)\rangle$ , and  $U \leftrightarrow U'$ . While the simulated system may not be controllable (or not experimentally accessible in some cases), the quantum simulator is. Namely, the initial state  $|\psi(0)\rangle$  can be prepared, the unitary evolution  $U'$  can be engineered, and the final state  $|\psi(t)\rangle$  can be measured. The result of this measurement provides information about the simulated system. The colored arrows denote the controllable operations. The solid black arrows describe the time evolution of the system and the simulator. The dashed arrows indicate the correspondence between the quantum states of the simulator and the simulated system.

idea of quantum simulation is represented schematically in Fig. 1.

# IV. DIGITAL AND ANALOG QUANTUM SIMULATION

The advantage of quantum simulators over classical devices is that, being quantum systems themselves, they are capable of storing large amounts of information in a relatively small amount of physical space. For example, the storage capacity of  $N$  qubits is exponentially larger than that of  $N$  classical bits. Going back to the example given in Sec. III, the quantum state of  $N = 40$  spin-1/2 particles, which would require a 4 TB classical memory register, can be represented by a 40-qubit (i.e., 5-quantum-byte) register. If the time evolution of the simulator reproduces the time evolution of the simulated system, the desired final state can be obtained without the need for numerically exponentiating a  $2^{N} \times 2^{N}$  matrix. This sounds very promising, but the quantum simulation problem is not really solved unless the initial-state preparation, the implementation of the time evolution, and the measurement are realized using only polynomial resources. The importance of measurement must be stressed because the success of quantum simulation ultimately depends on the ability to extract useful information from the simulator. As discussed later, these are not easy tasks, even for quantum simulators.

# A. Digital quantum simulation

We consider the well-known circuit model for quantum computation (Nielsen and Chuang, 2000). The wave function  $|\varphi \rangle$  has to be encoded using the computational basis, i.e., as a superposition of binary bit strings. A very simple example is the simulation of spin-1/2 particles. Each particle is represented by a qubit: the spin-up state  $|\uparrow \rangle$  is encoded as the qubit state  $|1\rangle$ , and the spin-down state  $|\downarrow \rangle$  as  $|0\rangle$ . For example, the three-spin state  $|\varphi \rangle = |\uparrow \uparrow \downarrow \rangle$  is represented in the simulator by  $|\psi \rangle = |110\rangle$ .

In order to obtain  $|\psi(t)\rangle = \exp\{-i\hbar Ht\} |\psi(0)\rangle$ ,  $U = \exp\{-i\hbar Ht\}$  must be applied to the initial state. The complicated many-qubit unitary transformation  $U$  is implemented through the application of a sequence of single- and two-qubit gates (we will come back and discuss the decomposition of  $U$  into these simple gates shortly). Such a circuit-based quantum simulation recreating the evolution  $|\psi(0)\rangle \rightarrow |\psi(t)\rangle$  is usually referred to as digital quantum simulation (DQS). Some of the representative studies on DQS are Lloyd (1996), Wiesner (1996), Abrams and Lloyd (1997), Lidar and Biham (1997), Zalka (1998a, 1998b), Terhal and DiVincenzo (2000), Ortiz et al. (2001), Marzuoli and Rasetti (2002), Somma et al. (2002), Verstraete, Cirac, and Latorre (2009), and Raeisi, Wiebe, and Sanders (2012).

Since any unitary operation can be written in terms of universal quantum gates, it follows that in principle "anything" can be simulated, i.e., DQS is universal (Lloyd, 1996). However, it must be noted that not any unitary operation can be efficiently simulated (that is with polynomial resources) and, therefore, there are Hamiltonians that cannot be efficiently simulated in this way. Nevertheless, it is possible to efficiently simulate any finite-dimensional local Hamiltonian. This is particularly important since all local spin systems, and all Hamiltonians that can be efficiently mapped to such systems, are included in this class. In other words, although not all mathematically allowed Hamiltonians can be simulated efficiently, those that appear in most physical theories can be simulated efficiently. Note that finding an efficient decomposition in terms of universal gates can in itself be a difficult problem (Daskin and Kais, 2011). Furthermore, it must be stressed that the implemented unitary operation (i.e., that obtained from the decomposition into single- and two-qubit gates) is generally an approximation of the desired unitary evolution. In principle, this approximation can be made arbitrarily accurate (by refining the decomposition), but this comes at the cost of an ever-increasing number of gates.

Although DQS algorithms rely on applying a time-ordered sequence of gates, thus implementing a unitary evolution of the simulator, DQS is not restricted to recreating the temporal evolution of the simulated system. Applications of DQS also include obtaining certain properties of a given quantum system [e.g., phase estimation for computing eigenvalues of operators, particularly the Hamiltonian (Abrams and Lloyd, 1999; Aspuru-Guzik et al., 2005; H. Wang et al., 2010), or computing partition functions (Lidar and Biham, 1997)]. Moreover, according to Meyer (2002) it should also be possible to use quantum computers to simulate classical physics more efficiently [see also Sinha and Russer (2010) and Yung et al. (2010)].

In general, DQS consists of three steps: initial-state preparation  $|\psi (0)\rangle$ , unitary evolution  $U$ , and the final measurement. These steps are discussed in detail in Sec. IV.A [see also (Brown, Munro, and Kendon (2010)].

Initial-state preparation.-The first step of the simulation is to initialize the quantum register to the state  $|\psi(0)\rangle$ . In many cases the preparation of the initial state is difficult and an efficient algorithm may not be available. Fortunately, for particular cases of interest efficient state preparation is possible. For example, a method for generating a state that encodes the antisymmetrized many-particle state of fermions (including all the possible permutations), starting from an unsymmetrized state (e.g.,  $|000\dots 0\rangle$ ) with polynomial resources was given by Abrams and Lloyd (1997). The preparation of  $N$ -particle fermionic states of the following form:

$$
| \psi (0) \rangle = \prod_ {j = 1} ^ {N} b _ {j} ^ {\dagger} | \text {v a c} \rangle , \tag {2}
$$

where  $|\mathrm{vac}\rangle$  is the vacuum state and  $b_{j}^{\dagger}$  and  $b_{j}$  are the fermionic creation and annihilation operators, was discussed by Ortiz et al. (2001, 2002) and Somma et al. (2002, 2003). A quantum algorithm for the efficient preparation of physically realistic quantum states on a lattice (arbitrary pure or mixed many-particle states with an arbitrary number of particles) was proposed by Ward, Kassal, and Aspuru-Guzik (2009), while Kassal et al. (2008) showed that the most commonly used chemical wave functions can be efficiently prepared. A quantum algorithm for preparing a pure state of a molecular system with a given number  $m$  of electrons occupying a given number  $n$  of spin orbitals that exhibits polynomial scaling in  $m$  (regardless of  $n$ ) was proposed by Wang, Ashhab, and Nori (2009) (see Fig. 2). Wang, Ashhab, and Nori (2011) proposed a state-preparation algorithm that incorporates quantum simulation: the time evolution of the quantum system is simulated including the interaction with ancilla, i.e., auxiliary, qubits that can inject or absorb any specified amount of energy from the system, thus preparing any desired energy eigenstate.

$$
\begin{array}{c c} | \psi_ {T} (n, 1) \rangle & \begin{array}{c c} \hline X \\ \hline \end{array} \begin{array}{c c} \tilde {H} \\ \tilde {H} ^ {\prime} \end{array} \begin{array}{c c} | 0 \rangle \\ | 0 \rangle \\ \hline Q (n - 2, 1) \\ \hline \end{array} \\ & | 0 \rangle^ {\otimes (n - 2)} \end{array}
$$

FIG. 2. Initial-state preparation. Quantum circuit for the recursive procedure used to find an efficient gate sequence for preparing a given target state  $|\psi_T(n,1)\rangle$  of one electron occupying  $n$  possible orbitals. The procedure uses reverse engineering, where one considers the problem of transforming the target state to the initial state  $|0\rangle^{\otimes n}$ . This reverse problem allows an intuitive, systematic solution. Once the solution of this inverse problem is found, it can be inverted in order to prepare the target state  $|\psi_T(n,1)\rangle$  from the initial state  $|0\rangle^{\otimes n}$ . The unitary operations  $\tilde{H}$  and  $\tilde{H}^{\prime}$  can be calculated easily from the given target state: each one of them transforms the known state of the corresponding qubit to  $|0\rangle$ . The unitary operation  $Q(n - 2,1)$  transforms  $|\psi_T(n - 2,1)\rangle$  into  $|0\rangle^{\otimes (n - 2)}$ . Adapted from Wang, Ashhab, and Nori, 2009.

Unitary evolution. We now discuss in more detail how to obtain  $U$ . We assume that the Hamiltonian can be written as a sum of many terms that describe local interactions:

$$
H = \sum_ {l = 1} ^ {M} H _ {l}. \tag {3}
$$

Examples of Hamiltonians of this form include the Hubbard and Ising Hamiltonians. If  $[H_l, H_{l'}] = 0$  for all  $l$  and  $l'$ , then

$$
U = \prod_ {l} \exp \{- i \hbar H _ {l} t \}. \tag {4}
$$

In this case, the decomposition of  $U$  into a sequence of local gates is straightforward. Unfortunately, in most cases of practical interest  $[H_l, H_{l'}] \neq 0$  in general. As a result, when taken as a whole, the decomposition of  $U$  cannot be obtained efficiently using classical methods. An important step in this regard is breaking up the evolution time into a large number of small time steps of duration  $\Delta t$  each:

$$
U = \left(\exp \{- i \hbar H \Delta t \}\right) ^ {t / \Delta t}. \tag {5}
$$

There are approximations available for decomposing  $\exp\{-i\hbar H\Delta t\}$  into local gates. For example, the first-order Trotter formula [see, e.g., Nielsen and Chuang (2000), Ortiz et al. (2001), and Somma et al. (2002)] gives

$$
U (\Delta t) = e ^ {- i \hbar \sum_ {l} H _ {l} \Delta t} = \prod_ {l} e ^ {- i \hbar H _ {l} \Delta t} + \mathcal {O} ((\Delta t) ^ {2}). \tag {6}
$$

As a result, when  $\Delta t\rightarrow 0$

$$
U (\Delta t) \approx \prod_ {l} \exp \{- i \hbar H _ {l} \Delta t \}. \tag {7}
$$

The drawback of this approach is that high accuracy comes at the cost of very small  $\Delta t$  and therefore a very large number of quantum gates. Recent results have reemphasized the shortcomings of using this first-order Trotter formula (Brown, Clark, and Chuang, 2006; C. R. Clark et al., 2009; Whitfield, Biamonte, and Aspuru-Guzik, 2011), showing that higher-order decompositions can be more efficient [see, e.g., Dur, Bremne, and Briegel (2008)]. Recently quantum algorithms for simulating time-dependent Hamiltonian evolutions on a quantum computer have also been investigated (Wiebe et al., 2011). The topic was further discussed by Poulin et al. (2011), where it was shown that by using randomness it is possible to efficiently simulate local bounded Hamiltonians with arbitrary time dependence.

We now consider an example of constructing rather complex operations from simple quantum gates. Take the Hamiltonian

$$
H = \sigma_ {1} ^ {z} \otimes \sigma_ {2} ^ {z} \otimes \dots \otimes \sigma_ {N} ^ {z}, \tag {8}
$$

where  $\sigma_i^z$  is the Pauli matrix acting on spin (qubit)  $i$ . Throughout the paper we denote by  $\sigma_i^\alpha$ , with  $\alpha = x, y, z$ , the corresponding Pauli matrix acting on spin (qubit)  $i$ . The quantum circuit in Fig. 3 realizes the unitary transformation  $U = \exp\{-i\hbar Ht\}$  for  $N = 3$  (Nielsen and Chuang, 2000). It

![](images/2575388a7f7d132ee9d28f8f5b0e2d246fbdb0075cf90f2724991bb1b35a671f.jpg)  
FIG. 3. Quantum circuit for simulating the three-body Hamiltonian  $H = \sigma_1^z \otimes \sigma_2^z \otimes \sigma_3^z$ . The circuit contains six CNOT gates and utilizes a fourth, ancilla qubit (bottom line) in order to achieve the desired effective Hamiltonian. From Nielsen and Chuang, 2000.

is composed of six two-qubit (CNOT) gates and one single-qubit gate. Note that an ancilla qubit is used. Similar quantum circuits can be written for any product of Pauli matrices

$$
H = \bigotimes_ {l = 1} ^ {N} \sigma_ {l} ^ {\alpha}. \tag {9}
$$

Although the example above might look simple, the efficient simulation of a general many-body interaction Hamiltonian using two-body interactions is by no means easy (Bennett et al., 2002; Nielsen et al., 2002). This question has been thoroughly studied, and several methods have been developed [see, e.g., Dodd et al. (2002), Wang and Zanardi (2002), Wocjan, Janzing, and Beth (2002), Wocjan, Rotteler, Janzing, and Beth (2002a, 2002b), Bremner, Bacon, and Nielsen (2005), Hastings (2006), Berry et al. (2007), Bravyi et al. (2008), Dür, Bremne, and Briegel (2008), and Brown et al. (2011)], but it still remains a difficult problem. Moreover, note that ancilla qubits are required, which adds to the resource requirements (see Sec. V.B).

We now take a look at another example: the algorithm given by Aspuru-Guzik et al. (2005) for the calculation of molecular energies using a recursive phase-estimation algorithm. The quantum circuit is shown in Fig. 4. This procedure provides an arbitrarily accurate estimate of the energy, with the accuracy increasing with increasing number of iterations. The first iteration gives a rough estimate for the energy. This estimate is then used as a reference point for the next iteration, which

![](images/b158b44ca082662b2df14a441c4a9f4472b1b3a6752f858b3d983da54171c55e.jpg)  
FIG. 4. Quantum circuit for the calculation of molecular energies in Aspuru-Guzik et al. (2005). The circuit implements the recursive phase estimation algorithm. The first iteration gives the phase  $\varphi$  (which represents the molecular energy) to four bits of accuracy. Each subsequent iteration incorporates the previous estimate and increases the accuracy by one bit, i.e. reduces the uncertainty by a factor of 2. Here  $H$  denotes the Hadamard gate,  $QFT^{+}$  is the inverse quantum Fourier transform, and  $V_{k} = [\exp (-i2\pi \varphi_{k - 1})\hat{V}_{k - 1}]^{2}$ . Adapted from Aspuru-Guzik et al., 2005.

![](images/5bd0d0806a7aca9d3f09d71531203c892124398ce11257a403097184cbc54bc1.jpg)

![](images/ba9d480a860ca45fde791f3bf2f6f12d6bd998dfdc529771e50934a49246a061.jpg)  
FIG. 5. Quantum circuits (a) for the measurement of the quantity  $\langle U^{\dagger}V\rangle$  for two unitary operators  $U$  and  $V$ , and (b) for the measurement of the spectrum of a Hermitian operator  $\hat{Q}$ . Both algorithms use one ancilla qubit, which is initially prepared in the state  $| + \rangle = (|0\rangle + |1\rangle) / \sqrt{2}$ . The black dot represents a  $|1\rangle$ -controlled gate and the white dot a  $|0\rangle$ -controlled gate. Adapted from Somma et al., 2002.

yields a better estimate. The procedure is repeated until the desired precision is obtained.

So far, the literature has generally focused on the discrete evolution of a quantum system, but recently, continuous evolution has also been discussed (McKague, Mosca, and Gisin, 2009; Biamonte et al., 2011). Furthermore, it is usually assumed that there is no restriction in applying one- and two-qubit gates and that all qubits of the simulator can be individually addressed and measured. An interesting question is what Hamiltonians can be simulated under certain control constraints. For example, Kraus, Wolf, and Cirac (2007) discussed the class of Hamiltonians that can be simulated when one is restricted to applying translationally invariant Hamiltonians. They showed that if both local and nearest-neighbor interactions are controllable, then the simulation of interactions in quadratic fermionic and bosonic systems is possible. However, for spins this is still an open problem.

Measurement.-After obtaining  $|\psi(t)\rangle = U|\psi(0)\rangle$  via the unitary evolution, we need to perform the final measurement in order to extract the desired information. In general, for characterizing a quantum state, quantum state tomography (QST) (D'Ariano, Paris, and Sacchi, 2003) can be used. However, QST requires resources that grow exponentially with the size of the system, making it inefficient for large quantum systems. In order to avoid this problem, the direct estimation of certain physical quantities such as correlation functions or spectra of operators is more desirable than taking the long route through QST. A detailed discussion is given by Ortiz et al. (2001) and Somma et al. (2002).

We consider two examples. The first one refers to measurements of quantities that can be written in the form  $\langle U^{\dagger}V\rangle$ , where  $U$  and  $V$  are unitary operators. The measurement circuit is shown in Fig. 5. One ancilla qubit that is initially in the state  $| + \rangle = (|0\rangle + |1\rangle) / \sqrt{2}$  is needed. The desired quantity, i.e.,  $\langle U^{\dagger}V\rangle$ , is given by the expectation value  $\langle 2\sigma_{+}^{a}\rangle$  of the ancilla at the end of the simulation (here  $2\sigma_{+}^{a} = \sigma_{x}^{a} + i\sigma_{y}^{a}$ ). The

second example pertains to measuring the spectrum of a Hermitian operator  $\hat{Q}$ . Again, one ancilla qubit that is initially in the state  $| + \rangle = (|0\rangle + |1\rangle) / \sqrt{2}$  is needed, and the desired spectrum is obtained by analyzing the time dependence of  $\langle 2\sigma_{+}^{a}\rangle$ . The measurement circuit is shown in Fig. 5.

# B. Analog quantum simulation

"...there is to be an exact simulation, that the computer will do exactly the same as nature" (Feynman, 1982).

Another approach to simulating quantum systems by quantum mechanical means is analog quantum simulation (AQS), in which one quantum system mimics (emulates) another (Wei and Xue, 1997; Manousakis, 2002; Fischer and Schützhold, 2004; Porras and Cirac, 2004b; Smirnov et al., 2007; Zagoskin, Savel'ev, and Nori, 2007). The Hamiltonian of the system to be simulated  $H_{\mathrm{sys}}$  is directly mapped onto the Hamiltonian of the simulator  $H_{\mathrm{sim}}$ , which can be controlled at least to some extent:

$$
H _ {\text {s y s}} \leftrightarrow H _ {\text {s i m}}. \tag {10}
$$

This can be done if there is a mapping between the system and the simulator (Somaroo et al., 1999). Then  $|\varphi(0)\rangle$  can be mapped to  $|\psi(0)\rangle$  via an operator  $f(|\psi(0)\rangle = f|\varphi(0)\rangle)$ , and  $|\psi(t)\rangle$  can be mapped back to  $|\varphi(t)\rangle$  via  $f^{-1}$ . For Hamiltonians  $H_{\mathrm{sim}} = fH_{\mathrm{sys}}f^{-1}$ . Note that the simulator may only partly reproduce the dynamics of the system. The choice of the mapping depends on what needs to be simulated and on the capabilities of the simulator. In AQS one is usually emulating an effective many-body model of the simulated system. A controllable "toy model" of the system is used to reproduce the property of interest, e.g., the dynamics or ground state.

An important advantage of AQS is that it could be useful even in the presence of errors, up to a certain tolerance level. For example, one is sometimes interested in knowing whether a certain set of physical conditions leads to a given quantum phase transition. Even without having the full quantitative details, a qualitative answer can be quite valuable in this context. If the quantum simulator suffers from uncertainties in the control parameters, the phase transition under study could still be observed, hence providing the answer to the question of interest.

Finding the mapping in an AQS might, at first glance, look simpler than obtaining the most efficient gate decomposition for a given Hamiltonian in DQS. Sometimes the mapping is indeed straightforward, but this is not always the case, and quite often clever mappings have to be devised, sometimes involving additional externally applied fields or ancillary systems to mediate various interactions.

We now look at two examples of mappings between quantum systems and the corresponding simulators. The first is the Hamiltonian describing a gas of interacting bosonic atoms in a periodic potential

$$
H _ {\mathrm {s i m}} = - J \sum_ {i, j} \hat {a} _ {i} ^ {\dagger} \hat {a} _ {j} + \sum_ {i} \varepsilon_ {i} \hat {n} _ {i} + \frac {1}{2} U \sum_ {i} \hat {n} _ {i} (\hat {n} _ {i} - 1), \tag {11}
$$

where  $\hat{a}_i^\dagger$  and  $\hat{a}_i$  correspond to the bosonic creation and annihilation operators of atoms on the  $i$ th lattice site,  $\hat{n}_i = \hat{a}_i^\dagger \hat{a}_i$  is the atomic number operator counting the number of atoms on the  $i$ th lattice site, and  $\varepsilon_i$  denotes the energy offset of the  $i$ th lattice site due to an external confining potential. The coefficient  $J$  quantifies the hopping strength between lattice sites, and  $U$  quantifies the interaction strength between atoms occupying the same lattice site. This Hamiltonian has a similar form to the Bose-Hubbard Hamiltonian

$$
H _ {\mathrm {B H}} = - J \sum_ {i, j} \hat {b} _ {i} ^ {\dagger} \hat {b} _ {j} + \frac {1}{2} U \sum_ {i} \hat {n} _ {i} (\hat {n} _ {i} - 1) - \mu \sum_ {i} \hat {n} _ {i}, \tag {12}
$$

where  $J$  and  $U$  are the same as above, and  $\mu$  is the chemical potential. The analog simulation of the Bose-Hubbard model using atoms in optical lattices is therefore straightforward. However, in other situations one must rewrite  $H_{\mathrm{sim}}$  in order to obtain the mapping  $H_{\mathrm{sys}} \leftrightarrow H_{\mathrm{sim}}$ . For example, in the case of an array of Josephson junctions as in van Oudenaarden and Mooij (1996) the system is described by the quantum phase model, which can be connected to the Bose-Hubbard model via a mapping where the field operators  $\hat{a}_i$  are reformulated in terms of the amplitude and phase of the superconducting order parameter at different points in the circuit.

The second example of a mapping between a quantum system and its simulator is the trapped-ion simulation of the Dirac equation (Lamata et al., 2007; Gerritsma et al., 2010). The Dirac equation in  $(1 + 1)$  dimensions for a spin-  $1 / 2$  particle with rest mass  $m$  is

$$
i \hbar \frac {\partial \varphi}{\partial t} = H _ {D} \varphi = \left(c \hat {p} \sigma_ {x} + m c ^ {2} \sigma_ {z}\right) \varphi , \tag {13}
$$

where  $c$  is the speed of light,  $\hat{p}$  is the momentum operator, and  $\sigma_{x}$  and  $\sigma_{z}$  are the Pauli matrices. The Hamiltonian of a single trapped ion interacting with a bichromatic light field can be written as

$$
H _ {I} = 2 \eta \Delta \bar {\Omega} \sigma_ {x} \hat {p} + \hbar \Omega \sigma_ {z}, \tag {14}
$$

where  $\eta$  is the Lamb-Dicke parameter,  $\Delta$  is the spatial size of the ground-state wave function, and  $\bar{\Omega}$  is controlled via the intensity of the bichromatic light field. With the identifications  $c\equiv 2\eta \hat{\omega}\Delta$  and  $mc^2\equiv \hbar \Omega$ ,  $H_{I}$  has the same form as  $H_{D}$ . With this analogy, effects such as Zitterbewegung and the Klein paradox can be studied in a nonrelativistic quantum system (Gerritsma et al., 2010, 2011).

In the following sections the Hamiltonians of several proposed quantum simulators and those of the systems to be simulated are discussed in more detail and the relation in Eq. (10) will become clearer for each particular case.

The initial-state preparation and measurement in AQS have not been thoroughly discussed in the literature. Because the system and simulator are presumed to be very similar, it is expected that the preparation of the initial state can occur naturally in processes mimicking the natural relaxation of the simulated system to an equilibrium state. Moreover, directly

measuring some physical quantity of the simulator would yield information about its analog in the simulated system. In this sense, AQS has the additional advantage that physical quantities can be measured directly, without the need for computational manipulation of measurement results as in DQS. Nevertheless, both the initial-state preparation and measurement process in AQS will need to be studied in more detail as AQS becomes a widely used research tool.

# C. Quantum-information-inspired algorithms for the classical simulation of quantum systems

In an interesting recent development, classical numerical algorithms for the simulation of quantum many-body systems came out of research on quantum information theory. [For detailed studies on the subject, see, e.g., Verstraete and Cirac (2004), Verstraete, Porras, and Cirac (2004), and Vidal (2008)].

As discussed in Secs. II and IV, fully characterizing a quantum system requires an exponentially large number of parameters. It would be useful if many-particle states could be represented in such a way that some physical quantities could be classically calculated in a more efficient way. In order to achieve this goal, some techniques from quantum information theory have been used in recently developed algorithms. The first steps in this direction were taken by Verstraete and Cirac (2004) and Verstraete, Porras, and Cirac (2004) and thereafter a significant effort has been made to explore this idea. Using matrix product states and projected entangled-pair states one can simulate more efficiently infinite-size quantum lattice systems in one and two dimensions. This new class of algorithms makes it possible to simulate spin systems for longer times and to study physical phenomena which would have been inaccessible with previous methods. Moreover, these methods can be combined with Monte Carlo techniques. For more details we direct the interested reader to the two reviews (Verstraete, Murg, and Cirac, 2008; Cirac and Verstraete, 2009, and references therein). Another widely used stochastic method is the Metropolis algorithm. Its quantum version allows for direct sampling from the eigenstates of the Hamiltonian, overcoming in this way the sign problem (Temme et al., 2011).

# V. RESOURCE ESTIMATION AND FAULT TOLERANCE

# A. Resource estimation

Using a quantum simulator instead of a classical computer does not necessarily provide an efficient solution to the problem of simulating quantum systems. This is because it is not always easy to prepare the initial state, evolve it, and measure it with polynomial resources. The amount of physical resources (i.e., number of qubits, number of operations, number of steps, etc.) needed for the quantum simulation in the case of an  $N$ -body problem strongly depends on the type of problem and the particularities of the simulator. In this section, we review some results on the estimation of the required resources for some particular cases.

How many particles or qubits are needed to realize useful quantum simulations? The answer to this question depends on

![](images/348e77810349bd45bac4867cef91eb5bbd950591bb697f0be87614e163efc4fd.jpg)

![](images/b4223b6dea9ede27020d3733f115a34a652ce3e05cf78164e9a40574483c433e.jpg)  
FIG. 6. Resource requirements for the quantum simulation of the dynamics of  $N$  particles interacting through a pairwise potential, maintaining a relatively small error level. The chemical symbols are a guide to show what type of problem can be simulated with a given computation size. The vertical dashed lines represent the current limit of numerically exact quantum simulations on classical computers on a grid. From Kassal et al., 2008.

the type of simulation one wants to implement. As a general rule of thumb, it is sometimes said that in order to outperform classical computers quantum simulators require somewhere between 40 and 100 qubits (Buluta and Nori, 2009). However, there are some interesting applications that could be realized with fewer qubits. For instance, with ten or fewer qubits one could perform proof-of-principle simulations, including the simulation of frustrated spin systems (Porras and Cirac, 2006b; Kim et al., 2010; Ma et al., 2011; 2012), quantum chaos (Howell and Yeaze, 1999; Weinstein et al., 2002), some simple chemical reactions (Smirnov et al., 2007), Dirac particles (Bermudez, Martin-Delgado, and Solano, 2007; Lamata et al., 2007; Gerritsma et al., 2010), the Unruh effect (Alsing, Dowling, and Milburn, 2005; Nation et al., 2012), or anyons (Lu et al., 2009; You et al., 2010). (Note that these few-qubit simulations can in principle be readily performed on a present-day classical computer.) With a few tens of qubits, one could perform frustrated-spin simulations or molecular-energy calculations at the limits of present-day supercomputers.

There have been rather extensive studies on the resource estimation for DQS. The estimation of the requirements for simulating  $N$  particles interacting through a pairwise potential

has been performed by Kassal et al. (2008). The results are reproduced in Fig. 6. A discrete-variable representation of the wave function in an  $n$  qubit basis is used. Furthermore, a number  $m$  of ancilla qubits is required to represent the desired range of potential values with a certain precision, four of which give a reasonably high accuracy for the Coulomb potential. This gives a total of  $n(3N - 6) + 4m$  qubits. The Coulomb potential can be evaluated in  $\mathcal{O}(N^2 m^2)$  steps, so chemical dynamics could be simulated on a quantum computer in  $\mathcal{O}(N^2 m^2)$  steps, which is exponentially faster than known classical algorithms. However, from the data in Fig. 6, it follows that in order to outperform current classical computers at least 100 qubits and over 200 000 quantum gates per step would be required.

Compared with the studies on scaling with the system size, less attention has been paid in the literature to the scaling of required resources with desired accuracy. For example, if one considers a case where increasing the accuracy of the answer (i.e., the desired number of bits in the final answer) leads to an exponential increase in the number of quantum gates, it is not obvious that the quantum simulation can be called efficient. Indeed, it was pointed out by Brown, Clark, and Chuang (2006) that several current algorithms for quantum simulation exhibit poor scaling as a function of desired accuracy, even if they seem efficient based on the scaling with system size. One should also note here that, at first sight, one might think that making the step size smaller for the Trotter decomposition in DQS does not affect the total run time of the algorithm, because the gates can be implemented more quickly for small time steps. However, there is typically an overhead that is proportional to the number of gates that need to be implemented, and this number can increase rapidly with decreasing step size. The precision requirement in a given quantum simulation is therefore an important question for purposes of resource estimation.

Recently, the resource requirements (total number of physical qubits and computation time) for computing the ground state energy of the one-dimensional quantum transverse Ising model with  $N$  spin-1/2 particles, as functions of the system size and the numerical precision, were investigated by C. R. Clark et al. (2009). The quantum circuit was decomposed into fault-tolerant operations, and the total number of qubits and the total number of steps were estimated as functions of the desired precision. They found that the computation time grows exponentially with desired precision. In order to obtain polynomial scaling, new quantum simulation algorithms are needed. Alternatively, systems where the phase estimation algorithm can be implemented without the Trotter formula (C. R. Clark et al., 2009) could be used.

A related recent study (You, Geller, and Stancil, 2013) compared the resource requirements for two alternatives that could be used in fault-tolerant DQS: topologically protected surface codes and circuit models with quantum error correction. By analyzing the Ising model as a representative example, and using parameters that are relevant to present-day experiments, they concluded that surface codes are superior for quantum simulation.

Another example of resource estimation for a DQS implementation is given by Lanyon et al. (2010). The results are reproduced in Fig. 7, where the error in the ground state

![](images/bed40eb7f856367924e28cfae01644bdacf2cfe0a76867b4b5f33e6e28b2303f.jpg)

![](images/7d547f2e4ac8cd09d7e632b2cbb42cacb36f3bd4eb742eecb15c9c50dee0a3d4.jpg)  
FIG. 7 (color online). Trotter error analysis and gate count for a simulation of the hydrogen molecule using a DQS algorithm. (a) The calculated ground state energy of the hydrogen molecule as a function of the time step duration  $\Delta t$ . The horizontal lines indicate the bounds for  $\pm 10^{-4}E_{h}$  precision. (b) Total number of gates for a single construction of the approximate unitary as a function of  $\Delta t$ . From Lanyon et al., 2010.

energy as a function of the time step duration  $\Delta t$  is shown. The ground state energies were obtained via direct diagonalization on a classical computer. A precision of  $\pm 10^{-4}E_{h}$ , where  $E_{h}\approx 27.21\mathrm{eV}$ , is achieved for about 522 gates. The gate count includes both one- and two-qubit operations and the estimate does not take into consideration error correction for the qubits. An extended discussion of the resource estimation for such molecular energy simulations is provided by Whitfield, Biamonte, and Aspuru-Guzik (2011).

There has not been much work in the literature on resource estimation for AQS. However, it is sometimes stated that AQS has less stringent resource requirements in order to produce useful results that are intractable for classical computational methods. This statement does not necessarily imply that few particles are sufficient in order to obtain results in AQS, but rather that large numbers of particles could be collectively manipulated in AQS using a small number of controls. For example, Greiner et al. (2002) trapped hundreds of thousands of atoms using three laser beams.

# B. Decoherence and errors

Although quantum simulators are affected by the interactions with the environment in the same way as quantum computers, it is generally believed that the effects of decoherence are less dramatic. This is most clearly seen with AQS, where only limited precision (or just a qualitative answer) might be required. As a result, a few imperfections in an ensemble of particles performing AQS might not affect the overall behavior of the ensemble, such that the AQS might still produce useful results even in the presence of these imperfections. Moreover, it has been suggested that the decoherence of the simulator might be useful (Lloyd, 1996) as it could serve as a rough way of modeling the decoherence of the simulated system. A simple argument could go as follows: if the noise level that is naturally present in the simulator is lower than the noise level in the simulated system, then it is rather straightforward to artificially supplement noise in the simulator so that the combined noise in the simulator faithfully mimics that present in the simulated system. This idea has in fact been demonstrated recently in experiment (Li et al., 2013). More sophisticated methods of dealing with noise are also possible. Tseng et al. (2000) demonstrated, through calculations and a nuclear magnetic resonance (NMR) experiment, that in the quantum simulation of open systems it is possible to exploit the natural decoherence of the simulator by varying the choice of mapping between the simulated system and the simulator. In principle, one could characterize how decoherence affects a simulation. Then, by an appropriate choice of the mapping between the system and simulator, one can take advantage of the natural symmetries in order to modify the effective decoherence of the simulator. It was also suggested (Tseng et al., 2000) that it should be possible to simplify decoherence effects in a simulation within certain subspaces. Decoherence may also provide a useful tool for extracting information about a critical system (spectral structure or critical point of its quantum phase transition) as suggested by Cucchietti, Fernandez-Vidal, and Paz (2007). This idea was investigated in an NMR setting (Zhang et al., 2009) with the simulation of the Ising Hamiltonian.

Unfortunately, there are certain limitations and the inclusion of the simulator's decoherence in the simulation must be carefully considered. The interaction between the system and the environment could be qualitatively different from that between the simulator and its environment (Brown, 2007). For example, when simulating spin Hamiltonians with degenerate ground states using trapped ions, spontaneous emission of the ions drives the system to states outside the Hilbert space used in the system-simulator mapping (Brown, 2007). This shows that one should be cautious when trying to include decoherence in the simulation. First, one needs to understand how decoherence will affect the simulation and, whenever possible, find clever mappings in order to take advantage of the uncontrollable properties of the simulator. Second, one needs to pay attention to the way the system and simulator are described. It is therefore necessary to pay more attention to the role of errors in AQS than has been done so far in the literature. Note that the simulation of open quantum systems does not necessarily require the inclusion of the decoherence of the simulator (Schneider and Milburn, 2001; Piilo and Maniscalco, 2006).

The ideal situation therefore remains that uncontrollable errors should be minimized as much as possible.

Brown, Clark, and Chuang (2006) conducted a detailed study of the algorithm for finding the low-lying spectrum of a pairing Hamiltonian in an NMR implementation. Such simulations were found to be sensitive to systematic errors in the applied Hamiltonian and fault-tolerant implementations to be inefficient with respect to precision in the current Trotter approximation methods. Other studies have shown that for simulating the Schrödinger equation the minimization of amplitude errors would be required (Strini, 2002). Montangero (2004) found the two-qubit entanglement in a simulation of a dynamically localized system to be exponentially sensitive both to small changes of the Hamiltonian and to the locations of the chosen qubits. This sensitivity is due to the natural ordering introduced on the qubits by the coding of the simulated system. More recently, there have been studies (Dür, Bremne, and Briegel, 2008) on the effect of noise (timing errors in pairwise interactions and noisy pairwise interactions described by master equations of Lindblad form) in two-body interactions and local control operations used for the simulation of many-body interaction Hamiltonians.

Further problems may arise for each physical implementation. In this context, the specific limitations of each system should be considered in more detail. So far there are few studies investigating how the simulator's imperfections affect the quantum simulation [e.g., in trapped ions (Porras and Cirac, 2004b, 2006b; Buluta et al., 2008)].

Recently, the reliability, complexity, and efficiency of analog quantum simulations have been considered in more detail than in past studies (Hauke et al., 2012). Reliability refers to the need to ensure that the results of the simulation faithfully reflect the simulated system. Cross validation over a number of different physical systems could be used, and in this way the particular imperfections of each implementation could be ruled out as possible sources of error. However, this approach is limited as implementations in different systems are not always available. The quantum simulation results can also be validated against analytical and numerical predictions, but this is possible only for small systems. Complexity and/or efficiency refers to the requirement that the quantum simulator is able to solve problems that cannot be solved on a classical computer in polynomial time (i.e., the simulator is more efficient than a classical computer). Note that in the case of the quantum simulation of experimentally challenging problems (see Sec. VII) this is not a necessary requirement. Disorder, noise, and other imperfections might affect the reliability of the quantum simulation (Hauke et al., 2012). This issue is illustrated in the case of a disordered quantum spin chain where strong disorder introduces large errors.

# VI. PHYSICAL REALIZATIONS

The physical implementation of a quantum simulator requires a controllable quantum mechanical system. Any physical system that can be used as a quantum computer would also be a universal machine for DQS. Possible routes and experimental progress toward building a quantum computer have been thoroughly discussed in the last decade (Chen et al., 2007; Schleich and Walther, 2008; Stolze and Suter,

![](images/baf22c0dc3ed69f82a98e17d27ad9adf0de14a05652243e130093c59677c6f3b.jpg)  
FIG. 8 (color online). Different systems that could implement a specialized quantum simulator for the study of problems in condensed-matter physics. Examples of such analog quantum simulators include atoms, ions, photons, nuclear and electronic spins, as well as superconducting circuits. These systems could be designed such that they form one- or two-dimensional arrays of qubits that can be manipulated in different manners. They can be thought of as toy models of the magnified lattice structure of a "solid," with a magnification factor of a few orders of magnitude.

2008; Ladd et al., 2010; Buluta, Ashhab, and Nori, 2011 and references therein). However, a quantum system that is not a potential quantum computer could still implement AQs. For instance, the propagation of sound waves in a two-component Bose-Einstein condensate (BEC) was proposed for the study of cosmic inflation (Fischer and Schützhold, 2004), and a rotating Fermi gas could be used to understand nuclear physics phenomena (Georgescu et al., 2011). We will not discuss the physical realization of such highly specialized quantum simulators, but focus on a more widely studied design of a quantum simulator: quantum simulators for various models in condensed-matter physics. For many problems in this class, an array of qubits plus their controls (see Fig. 8) would make an ideal quantum simulator because it can be thought of as the simplified, magnified lattice structure of a "solid" that can be manipulated in a number of different ways in order to test various models. Each qubit resides in its own potential energy well and is used to encode a spin-  $1/2$  particle. The array is configurable in the sense that its dimensionality and geometry can be changed. Such an array could be realized, for example, with atoms in optical lattices (Greiner and Fölling, 2008), atoms in arrays of cavities (Greentree et al., 2006; Hartmann, Brandao, and Plenio, 2006; Angelakis, Santos, and Bose, 2007; Brandao, Hartmann, and Plenio, 2007), ions either in microtrap arrays (Chiaverini and Lybarger, 2008; R.J. Clark et al., 2009; Schmied, Wesenberg, and Leibfried, 2009) or in two-dimensional crystals (Porras and Cirac, 2006b), electrons in arrays of quantum dots (Manousakis, 2002; Byrnes et al., 2007, 2008), and so on. The desired evolution of the system would be induced by the simulator's control fields. This can

either directly realize the desired Hamiltonian (AQS) or reconstruct it out of elementary one- and two-qubit gates (DQS). The control can be applied individually or to the entire array. In Secs. VI.A-VI.F, we look at different physical systems and describe how the array and controls can be realized experimentally. For a recent review of the state-of-the-art capabilities of the physical systems that we consider here, see Ladd et al. (2010) and Buluta, Ashhab, and Nori (2011).

# A. Atoms and ions

Neutral atoms in optical lattices are very well suited for mimicking solid-state systems. Indeed, optical lattices provide the highly desirable properties of being easily tunable and essentially defect free. The optical potentials can be adjusted to allow the change of the geometry and dimensionality of the lattice [e.g., triangular lattice (Struck et al., 2011), kagome lattice (Liu et al., 2010), etc.]. Interestingly, the optical potential can be tuned in situ rather easily via the intensity, frequency, or phase of the applied lasers.

Since the first experiment on the simulation of the quantum phase transition from a superfluid to a Mott insulator using a cold atomic gas in an optical lattice (Greiner et al., 2002), there has been increasing interest in the study of condensed-matter physics with atoms in optical lattices. A theoretical review (Lewenstein et al., 2007) discusses in detail atoms in optical lattices as potential quantum simulators, providing various examples of quantum systems that could be simulated. Other reviews (Bloch, Dalibard, and Zwerger, 2008; Bloch, Dalibard, and Nascimbene, 2012) describe recent experimental progress.

Atoms in optical lattices are flexible systems with several controllable parameters: tunneling strength, on-site, nearest-neighbor, long-range and multiparticle interactions, nonuniform potentials, and coupling between internal quantum states. Furthermore, there are both bosonic and fermionic elements that can be used for quantum simulation with atoms in optical lattices. A rather general type of Hubbard Hamiltonian that can be realized in these systems is

$$
H = H _ {\text {h o p}} + H _ {\text {i n t e r a c t i o n}} + H _ {\text {p o t}} + H _ {\text {i n t e r n a l}}, \tag {15}
$$

where  $H_{\mathrm{hop}}$  describes the tunneling of atoms from one lattice site to another,  $H_{\mathrm{interaction}}$  is the interaction part,  $H_{\mathrm{pot}}$  combines all the effects of the nonuniform potentials felt by the atoms, and  $H_{\mathrm{internal}}$  describes coherent on-site transitions between the internal levels of the atoms.

A quantum simulation of the Mott insulator-superfluid phase transition in the Hubbard model can be realized by adjusting the depth of the optical lattice, which mainly modifies the tunneling strength and to a lesser extent modifies the on-site interaction strength, or by controlling the on-site interactions via Feschbach resonances (Lewenstein et al., 2007) (see Sec. VII.A.1 on the simulation of the Hubbard model).

By tuning interatomic interactions using Feshbach resonances, it is possible to investigate the crossover from a Bardeen-Cooper-Schrieffer (BCS) state of weakly attractive fermions to a BEC of tightly bound fermion pairs (Regal,

Greiner, and Jin, 2004; Zwierlein et al., 2005). The continuous tunability of the interaction strength also allowed access to the so-called unitarity regime (O'Hara et al., 2002), where the interaction strength is comparable to the Fermi energy, meaning that there is a single energy scale in the problem. This regime was previously inaccessible and served as one more example demonstrating the power of atoms as quantum simulators.

Using laser-assisted tunneling and lattice tilting, Simon et al. (2011) achieved the simulation of an antiferromagnetically coupled spin chain in an external magnetic field. In this simulation the occupation of lattice sites was mapped onto the spin states of a quantum magnet. In particular, a pair of neighboring lattice sites sharing a single particle is mapped onto a (static) spin-  $1/2$  particle in the quantum magnet. It should also be possible to utilize the intrinsic spins of atoms in optical lattices for this purpose. However, no such simulations have been performed to date.

Another recently emerging direction for quantum simulation using atomic gases is the simulation of artificial gauge fields (Dalibard et al., 2011). At a basic level, an overall rotation of the trapping potential can be used to simulate a magnetic field (for the orbital degree of freedom). More intricate techniques that rely on additional lasers have been devised in the past few years for the simulation of various types of gauge fields, allowing the observation of spin-orbit coupling in a BEC (Lin, Jimenez-Garcia, and Spielman, 2011).

Currently, addressing individual atoms in optical lattices is difficult because the separation between neighboring lattice sites is comparable to the best achievable focusing widths of laser beams (both typically being  $0.5 - 0.8\mu \mathrm{m}$ ), but recent progress suggests that there may be methods for overcoming this difficulty (Nelson, Li, and Weiss, 2007; Bakr et al., 2009, 2010; Wurtz et al., 2009; Sherson et al., 2010; Fuhrmanek et al., 2011; Gibbons et al., 2011; Weitenberg et al., 2011).

Atoms could also be used for DQS. One possible method for implementing conditional quantum operations on atoms in optical lattices (Jané et al., 2003) is schematically illustrated in Fig. 9. Two optical lattice potentials are applied to the atomic ensembles, one for each of the two internal atomic states (which represent the qubit states). The interaction between neighboring atoms is realized by displacing one of the lattices with respect to the other [Fig. 9(a)]. With a sufficiently large relative displacement of the two lattices, interactions between more distant atoms can be achieved. Moreover, thanks to their weak interaction with the environment, neutral atoms have long decay times of the order of seconds.

Alternative systems that can be used for quantum simulation include Rydberg atoms (Weimer et al., 2010) and polar molecules (Lewenstein, 2006; Micheli, Brennen, and Zoller, 2006). In the case of Rydberg atoms in optical lattices or magnetic traps the lattice spacing is  $\sim \mu \mathrm{m}$  or higher, allowing single-site addressability. Furthermore, dipole-dipole and van der Waals interactions offer a means for implementing effective spin-spin interactions.

With polar molecules (Pupillo et al., 2009) (see Fig. 10) microwave excitations, dipole-dipole interactions, and spin-rotation couplings provide a universal toolbox for effective spin models. The advantage of using polar molecules is that

![](images/ee5553ad83c80d5d02120efb828e369c630d5a86c1cfd2f708105004bb829924.jpg)

![](images/4adea6abb8d8439ffd8b3e80252c8fd7158fc5f559fd0f5e579bbd5962d3d83a.jpg)  
FIG. 9 (color online). Manipulation of atoms and ions as proposed by Jané et al. (2003). (a) Neutral atoms in a double optical potential: the interaction between neighboring atoms is realized by displacing one of the lattices with respect to the other. Shaded circles denote the state  $|1\rangle$  and white ones denote the state  $|0\rangle$ . (b) Ions in independent trapping potentials: the interaction between two neighboring ions is achieved by conditionally displacing the corresponding ions with a state-dependent force. Shaded circles denote the state  $|1\rangle$  and white ones denote the state  $|0\rangle$ . Adapted from Jané et al., 2003.

their large electric dipole moments produce strong dipole-dipole interactions that can be manipulated relatively easily via external dc and ac microwave fields. This control can be used to study strongly correlated systems. Furthermore, extended Hubbard models (Ortner et al., 2009), quantum phase transitions (Capogrosso-Sansone et al., 2010), and the supersolid phase in a triangular lattice (Pollet et al., 2010) could also be simulated with these systems.

Ions can be trapped by electric (or magnetic) fields, laser cooled and manipulated with high precision for realizing quantum simulation (Schatz et al., 2004, 2007; Blatt and Wineland, 2008; Johanning, Varon, and Wunderlich, 2009). In fact, one of the earliest theoretical studies on the physical implementation of quantum simulation dealt with trapped ions (Wineland et al., 1998). Both the internal energy levels and the vibrational modes of the trapped ions can be exploited for encoding quantum information. In contrast with neutral atoms, which interact weakly with each other, ions, being charged, interact rather strongly via Coulomb repulsion. This facilitates the implementation of two-qubit gates and the control of the qubit positions and motion. Ion qubits also have long coherence times of the order of seconds, and sequences of high-fidelity quantum gates have been demonstrated in experiment (Hanneke et al., 2009; Lanyon et al., 2011).

![](images/faf29cfc5d863100bc22b37f2e3db5cfc5b19ba598739289437fec32006b4df7.jpg)  
FIG. 10 (color online). Polar molecules trapped in a plane by an optical potential created by two counterpropagating laser beams with wave vectors indicated by the middle arrows. The dipoles are aligned perpendicular to the plane by a dc electric field, indicated by the left arrow. The right arrow represents the ac microwave field. From Pupillo et al., 2009.

The quantum states of trapped ions are typically manipulated by either resonantly driving transitions between different internal states of the ions or resonantly driving sideband transitions involving the internal states and the vibrational states of the ions in the external trapping potential. For example, the Hamiltonian describing the coupling between the internal and vibrational modes due to the laser driving at the red-sideband frequency can be written in the following form:

$$
H = i \hbar \eta \Omega \left[ \exp (i \varphi) \sigma_ {+} a - \exp (- i \varphi) \sigma_ {-} a ^ {\dagger} \right], \tag {16}
$$

where  $\Omega$  is the Rabi frequency of the transition between the internal states,  $\sigma_{+}$  and  $\sigma_{-}$  are the two-level atom transition operators,  $\eta$  is the Lamb-Dicke parameter (which is assumed to be small here),  $a^{\dagger}$  and  $a$  are the creation and annihilation operators of the vibrational mode, and  $\varphi$  is the laser phase. Using this Hamiltonian, as well as those corresponding to blue-sideband driving and to resonant driving of the ionic internal states, a variety of effective Hamiltonians for AQS or quantum gates for DQS can be realized. The high-fidelity one-, two-, and even three-qubit (Toffoli) gates implemented with trapped ions have resulted in the most advanced implementations of DQS to date (Barreiro et al., 2011; Lanyon et al., 2011). Analog quantum simulations of frustrated spin systems (Kim et al., 2010) and of relativistic single-particle motion (Gerritsma et al., 2011) have also been recently demonstrated.

Ions have generally been trapped using linear harmonic traps in quantum-simulation experiments to date. It is possible, however, to obtain different arrangements of many ions in anharmonic one-dimensional traps [long ion strings (Lin et al., 2009)], two-dimensional traps [planar crystals (Porras and Cirac, 2006b; Buluta et al., 2008; Biercuk et al., 2009) or arrays of microtraps (Chiaverini and Lybarger, 2008; R.J. Clark et al., 2009; Schmied, Wesenberg, and Leibfried,

![](images/3d74071a032eb21b8e796a62ed7ea6450555ad29e69b9f510917b28a390e598a.jpg)  
FIG. 11 (color online). Arrangement of electrodes for the realization of a bilayer honeycomb lattice. The microtrapping regions are shown as ellipsoids, while the locations of unwanted spurious microtraps are indicated with small spheres. From Schmied, Wesenberg, and Leibfried, 2009.

2009; Schmied et al., 2010; Lau and James, 2012)] or three-dimensional traps. It would also be possible to combine trapped ions with optical lattices as suggested by Schmied et al. (2008). With optimized electrode structures, various microtrap arrays where ions are arranged in different lattice configurations (see Fig. 11) can be constructed (Schmied, Wesenberg, and Leibfried, 2009, 2011). In fact a two-dimensional ion array was recently used to implement a quantum simulation of a spin system with hundreds of ions (Britton et al., 2012).

There are also alternative ways to generate two-qubit interactions between ions. One such possibility is to use a state-dependent displacement, which can be implemented by applying optical dipole forces (Blatt and Wineland, 2008). This method is particularly useful for ions trapped in different harmonic potentials (e.g., in arrays of microtraps), but in most of the experiments done to date it has been realized with ions in the same potential. In Fig. 9(b), the manipulation of ions in a one-dimensional array of microtraps is depicted schematically. Two-qubit interactions are usually realized with optical forces, but a method for laserless simulation (avoiding the problem of scattering) with ions in arrays of microtraps has been proposed by Chiaverini and Lybarger (2008) and recently demonstrated by Ospelkaus et al. (2011) and Timoney et al. (2011).

Atoms in cavity arrays (see Fig. 12) (Greentree et al., 2006; Hartmann, Brandao, and Plenio, 2006; Angelakis, Santos, and Bose, 2007; Brandao, Hartmann, and Plenio, 2007) could also be used as quantum simulators [see also Kimble (2008)]. This system provides an alternative way of simulating the Bose-Hubbard model and quantum phase transitions as well as spin models (Kay and Angelakis, 2008).

In the absence of atoms, the cavity array is described by the following Hamiltonian:

$$
H = \omega_ {c} \sum_ {R} \left(a _ {R} ^ {\dagger} a _ {R} + \frac {1}{2}\right) + 2 \omega_ {c} \alpha \sum_ {R, R ^ {\prime}} \left(a _ {R} ^ {\dagger} a _ {R ^ {\prime}} + \mathrm {H . c .}\right), \tag {17}
$$

![](images/56404f4c657910d9b84ecf88daab83597a6398cd3222cf654921ba3054e4a105.jpg)  
FIG. 12. A one-dimensional array of cavities with atoms trapped in the cavities. Photons can hop between the different cavities because of the overlap between the light modes in adjacent cavities. The atoms can be driven using externally applied lasers. The atoms and cavities form hybrid excitations (polaritons) that can hop between the different cavities and that effectively interact with each other. The polariton-polariton interaction strength can, for example, be tuned via the atom-cavity detuning. From Hartmann, Brandao, and Plenio, 2006.

where  $a_{R}^{\dagger}$  creates a photon in the cavity at site  $R$ ,  $\omega_{c}$  is the frequency of the relevant cavity mode, and  $\alpha$  is the intercavity coupling coefficient (Hartmann, Brandao, and Plenio, 2006). One now introduces an atom or ensemble of atoms in each cavity, and these atoms can be driven by external lasers. The atoms trapped in a cavity together with the photons in the same cavity form hybrid excitations called polaritons. The nonlinearity introduced by the atoms results in effective polariton-polariton interactions, which can be utilized for simulating, for example, the Mott-insulator-superfluid phase transition.

Arrays of cavities in an arbitrary geometry may be realized with photonic band gap cavities and toroidal or spherical microcavities coupled via tapered optical fibers (Greentree et al., 2006). However, these might be quite challenging to realize experimentally.

A recent proposal suggested measurement and feedback control as tools for realizing quantum simulation in atom-cavity systems (Vollbrecht and Cirac, 2009), while others considered the possibility of using atom-cavity systems for simulating the high-spin Heisenberg model (Cho, Angelakis, and Bose, 2008a) and the fractional quantum Hall effect (Cho, Angelakis, and Bose, 2008b). Arrays of cavities could also be used to study the quantum analog of Fabry-Pérot interferometers as suggested by Zhou, Dong et al. (2008).

# B. Nuclear and electronic spins

Nuclear spins manipulated by means of NMR have been among the first experimental systems to implement small quantum algorithms and quantum simulation (Peng et al., 2009; Peng and Suter, 2010; Li et al., 2011; Zhang et al., 2012). Nuclear spin qubits have long coherence times  $(>1\mathrm{s})$  and high-fidelity quantum gates and the coherent control of up to 12 qubits have been demonstrated.

In the presence of a strong magnetic field pointing along the  $z$  axis, the general form of the NMR Hamiltonian is

$$
H = - \hbar \gamma B \sum_ {i} I _ {i} ^ {z} + \sum_ {i > j} J _ {i j} I _ {i} ^ {z} I _ {j} ^ {z}, \tag {18}
$$

where  $\gamma$  is the gyromagnetic ratio,  $B$  is the magnetic field,  $I$  is the angular momentum operator, and  $J_{ij}$  are the spin-spin coupling coefficients (Chen et al., 2007). The different transitions between pairs of energy levels generally have distinct resonance frequencies, allowing the addressing of the individual transitions based on their frequencies. Using rf pulses, various one-, two- and possibly multiqubit gates can be implemented. The field of NMR benefits from very well-developed control techniques. However, it is not very flexible and its main disadvantage is the lack of scalability, one of the main reasons being the spectral crowding that occurs as the number of energy levels increases exponentially with increasing number of spins. Although in solid-state NMR the scalability drawback may be overcome to some extent, individual addressing and measurement would still be impractical. Nevertheless, nuclear spins provide a very good test bed for various small simulation problems and allow the implementation of both DQS and AQs. Furthermore, a recent proposal suggested that nuclear spins attached to a diamond surface and addressed through nitrogen-vacancy (NV) centers could offer an attractive route toward a large-scale quantum simulator for strongly correlated systems (Cai et al., 2013).

Another system that could be used for quantum simulation is electron spins in semiconductor quantum dots (Hanson and Awschalom, 2008). Quantum dots are semiconductor systems in which the excitations are confined in a very small region in one or two dimensions. If the region is roughly the same size as the wavelength of the charge carrier, the energy levels are quantized and the quantum dot becomes very similar to a real atom (and can therefore be referred to as an "artificial atom"). Moreover, quantum dots allow flexible control over the confinement potential and they can also be excited optically. Furthermore, quantum dots with large tunnel coupling can act as "artificial molecules." These features make electron spins in quantum dots particularly attractive for quantum simulation.

Quantum dots can be defined at fabrication or by applying bias voltages using electrodes placed above a two-dimensional electron gas. They can be designed to have certain characteristics and assembled in large arrays. The manipulation and readout can be done both electrically and optically.

![](images/ccb59fda1de9966fe710f7b9d8b768d423866b2c44ebe4b9b57eed9b3f50b45a.jpg)  
FIG. 13. An array of quantum dots realized by a metallic gate with an array of two different size holes placed on top of an  $\mathrm{Al}_x\mathrm{Ga}_{1 - x}$  As/GaAs heterostructure. A negative gate voltage is applied to this gate in order to create a potential for the two-dimensional electron gas that is otherwise free to move at the  $\mathrm{Al}_x\mathrm{Ga}_{1 - x}$  As/GaAs interface. This was one of the early theoretical proposals for AQs. From Manousakis, 2002.

State-of-the-art quantum-dot qubits now have long decay times of  $>1$  s (Amasha et al., 2008).

Arrays of quantum dots could be realized using two-dimensional mesh gates (Manousakis, 2002; Byrnes et al., 2008) (see Fig. 13). Alternatively, Byrnes et al. (2007) proposed that interfering acoustic waves could be used to form an analog of optical lattices in a two-dimensional electron gas, but this latter approach has the disadvantage of heating and complicated engineering. By adjusting the mesh-gate design and voltage, various lattice geometries could be created. Electron spins in quantum dots may provide an advantage over atoms in optical lattices due to the very low temperatures (relative to the Fermi temperature) that can be reached and the natural long-range Coulomb interaction. In a recent experiment, the predictions of the two-dimensional Mott-Hubbard model were tested for electrons in an artificial honeycomb lattice (Singha et al., 2011).

The Hamiltonian for an array of quantum dots is given by

$$
H = \sum_ {j = 1} ^ {n} \mu_ {B} g _ {j} (t) B _ {j} (t) \cdot S _ {j} + \sum_ {1 \leq j <   k \leq n} J _ {j k} (t) S _ {j} \cdot S _ {k}, \tag {19}
$$

where the first term is the energy due to an applied magnetic field  $B_{j}$ , and the second term is the exchange interaction energy, which is a result of virtual tunneling between the quantum dots. Here  $S_{j}$  is the spin of the electric charge quanta of the  $j$ th dot (Chen et al., 2007). The interactions between the qubits can be engineered by adjusting the gate voltages together with a careful choice of the mesh hole sizes and doping (Manousakis, 2002).

# C. Superconducting circuits

Superconducting circuits (You and Nori, 2005, 2011; Clarke and Wilhelm, 2008) can also be used as quantum simulators (see Fig. 14). Quantum information can be encoded in different ways: in the number of superconducting electrons on a small island, in the direction of a current around a loop, or in oscillatory states of the circuit. The circuit can be manipulated by applied voltages and currents (including both dc and microwave-frequency ac signals) and measured with high

![](images/e85e8ae29443c4339f50540e80879a539d664f40a22bee1f39664b4a3541090e.jpg)  
FIG. 14 (color online). Schematic diagram of an array of superconducting flux qubits (Ashhab et al., 2008). The T-shaped circuits are used to couple the flux qubits, while the  $\varphi$ -shaped circuits are used to read out the states of the qubits. The gaps represent tunnel junctions.

accuracy using integrated on-chip instruments. Although macroscopic in size, these circuits can display quantum behavior and can be seen as artificial atoms. The advantage over real atoms is that superconducting circuits can be designed and constructed to tailor their characteristic frequencies, interaction strengths, and so on. The frequencies can also be tuned in situ by adjusting an external parameter (typically an external magnetic field), and the coupling energy between two qubits can be turned on and off at will. Furthermore, superconducting circuits can be coupled to "cavities," which are actually electrical resonators (and the "photons" are, for the most part, electron-density oscillations). This setup is very useful for the study of electric-circuit analogs of cavity quantum electrodynamics (circuit QED) (You and Nori, 2005, 2011; Schoelkopf and Girvin, 2008).

State-of-the-art superconducting qubits have coherence times exceeding  $100\mu s$  (i.e., decoherence rates below  $10\mathrm{kHz}$ ), which is quite high considering that other energy scales in the circuit are typically in the range  $10\mathrm{MHz}-10\mathrm{GHz}$ . Individual control and measurement have been demonstrated (Mariantoni et al., 2011). Furthermore high-fidelity one-, two-, and three-qubit quantum gates have been demonstrated. With this level of control, DQS could be implemented in a superconducting circuit in the near future.

The Hamiltonian for  $N$  charge (flux) qubits biased at their symmetry points (which is optimal for quantum coherence) coupled capacitively (inductively) is

$$
H = - \sum_ {i = 1} ^ {N} \frac {\Delta_ {i}}{2} \sigma_ {i} ^ {z} - \sum_ {(i, j)} J _ {i j} \sigma_ {i} ^ {x} \sigma_ {j} ^ {x}, \tag {20}
$$

where  $\Delta_{i}$  is the level splitting and  $J_{ij}$  is the strength of the coupling between qubits  $i$  and  $j$ . It should be noted, however, that superconducting circuits have more than two energy levels, and these additional levels could also be utilized. Indeed, a recent experiment demonstrated AQS of a spin larger than 1/2 using this approach (Neeley et al., 2009).

As for scalability, circuits containing 512 qubits have been fabricated (Harris et al., 2010; Harris, 2012), although quantum coherence was not tested on these circuits in the same way that coherence is commonly tested in other experiments using small numbers of qubits. Furthermore, more than 200 superconducting resonators were recently fabricated on a single chip (Houck, Tureci, and Koch, 2012). If qubits are integrated into such a circuit, it could realize the proposal of atom-cavity arrays (or Jaynes-Cummings lattices), performed with artificial atoms and cavities (see Fig. 15). It has also been proposed that artificial gauge fields could be simulated with such circuits (Koch et al., 2010). A related study proposed an approach to universal quantum computation and simulation using the single-excitation subspace of an array of coupled superconducting qubits (Geller et al., 2012). Although unscalable, this approach may still enable a universal quantum simulation speedup relative to a present-day classical computer.

The fact that superconducting circuits can be produced in large numbers and "wired" together on a chip offers a rather straightforward way of realizing various lattice geometries.

![](images/07b1682b81b8330ffc3d9382c55c46aef109b75048b8e95ecaa8764b490a27cb.jpg)  
FIG. 15 (color online). A possible design for implementing the Jaynes-Cummings lattice using superconducting qubits. The colored strips are superconducting resonators and the dots are superconducting qubits. An effective particle-particle interaction is created by the qubit-cavity interactions. From Koch et al., 2010.

Examples include the Kitaev model on a honeycomb lattice (You et al., 2010), networks for simulating Anderson and Kondo models (Garcia-Ripoll, Solano, and Martin-Delgado, 2008), highly connected networks (Tsomokos, Ashhab, and Nori, 2008), and fractals (Tsokomos, Ashhab, and Nori, 2010).

# D. Photons

Photons can carry quantum information over long distances, hardly being affected by noise or decoherence. They naturally possess the ability to encode qubit states, e.g., in the polarization of the photon, and one-qubit gates can be easily realized with linear optical components. Although the difficulty in implementing two-qubit gates is a serious drawback for photonic systems in the context of quantum computation, there have been some notable achievements for quantum simulation using photons.

Photons have been used to calculate the possible fractional statistics of anyons using a six-photon graph state (Lu et al., 2009), to calculate the energy spectrum of the hydrogen molecule to 20 bits of precision (Lanyon et al., 2010), and to simulate frustrated spin systems (Ma et al., 2011). It has also been proposed that photons propagating or trapped inside materials doped with atoms that have suitable energy-level structures could be used for the simulation of Luttinger liquids (Angelakis et al., 2011) and relativistic field theories (Angelakis et al., 2013; Angelakis and Noh, 2013).

Recently, it was shown that the propagation of photons in a network of beam splitters is in general a computationally difficult task for classical computers even for a few tens of photons (Aaronson and Arkhipov, 2011), and corresponding experiments with up to four photons were performed (Broome et al., 2013; Crespi et al., 2013; Spring et al., 2013; Tillmann et al., 2013). However, with limited flexibility and scalability, it remains to be seen how far photon-based quantum simulation can go.

# E. Other systems

One of the systems that are being considered as candidate platforms for implementing quantum computation is  $NV$

centers in diamond (Ladd et al., 2010; Buluta, Ashhab, and Nori, 2011). Unlike other systems studied in the context of quantum computation, however,  $NV$  centers in diamond have not received much attention as potential quantum simulators, which might be due to difficulties in coupling the  $NV$  centers to each other and future scalability. Nevertheless, there have been recent studies attempting to alleviate these difficulties (Weimer, Yao, and Lukin, 2013).

Another system that could be used for the quantum simulation of condensed-matter physics is electrons trapped on the surface of liquid helium (Mostame and Schützhold, 2008). This setup could be used to simulate the Ising model. In principle it could be scaled up, but the control would be very difficult. A related system that was proposed recently to implement DQS is a chain of molecular nanomagnets controlled by external magnetic fields (Santini et al., 2011).

A rather unconventional example of a quantum simulator is a two-component BEC in which the propagation of sound waves could simulate some aspects of cosmic inflation (Fischer and Schützhold, 2004). Although such a quantum simulator would be limited to a narrow class of problems, it provides an alternative possibility for the simulation of such systems.

# F. Current state of the art

The above discussion of the physical systems that could implement quantum simulation is summarized in Table I, which lists the strengths and weaknesses of each potential quantum simulator, and in Fig. 16.

Currently only with neutral atoms in an optical lattice is it possible to perform quantum simulations with more than a few particles, and these systems can at present be considered the most advanced platform for AQS. Although individual control and readout is not yet available, recent progress in this

![](images/fb85632fa31e23ba7e2b465fe9aef2e7263ea16738df49976f6822a4e1ee4201.jpg)  
FIG. 16 (color online). One- or two-dimensional arrays of qubits and controls can be used to simulate various models in condensed-matter physics. Examples of such analog quantum simulators include (a) atoms in optical lattices (Jaksch and Zoller, 2005), (b) one-dimensional or (c) two-dimensional arrays of cavities (Greentree et al., 2006; Hartmann, Brandao, and Plenio, 2006); (d) ions in linear chains, (e) two-dimensional arrays of planar traps (Chiaverini and Lybarger, 2008), or (f) two-dimensional Coulomb crystals (Porras and Cirac, 2006b); (g) electrons in quantum dot arrays created by a mesh gate (Manousakis, 2002; Byrnes et al., 2008), (h) in arrays of superconducting circuits, or (i) trapped on the surface of liquid helium (Mostame and Schutzhold, 2008). The average distance between the atoms in optical lattices is less than  $1\mu \mathrm{m}$ . Cavity arrays based on photonic band gap cavities would also have submicron intersite separations. As for the inter-ion distances in ion trap arrays, they are about  $10 - 15\mu \mathrm{m}$  and about the same for two-dimensional Coulomb crystals. In arrays of quantum dots, the spacing between dots is about  $0.1\mu \mathrm{m}$ . In superconducting circuits, the distance between qubits is typically a few microns. In the case of electrons on helium the distance between neighboring sites would be about  $1\mu \mathrm{m}$ . These interqubit distances (from 0.1 to  $10\mu \mathrm{m}$ ) are to be compared with the far smaller average interatomic distances in solids, which are  $\leq 1$  nm. The systems shown above realize a one- or two-dimensional array of qubits which can be manipulated in different manners. The larger distances between qubits make quantum simulators more controllable and easier to measure. Therefore, they can be thought of as models of the magnified lattice structure of a solid, with a magnification factor of 2 to 4 orders of magnitude. From Buluta and Nori, 2009.

![](images/d895800e54d6fa7fbc95f1a95cbf7abc8755ab80217df029c1a4336042763cb6.jpg)

![](images/65fbcb30231ff02fd0c4c8548fd7505640bb30c543c1b15b0d58e546a212580b.jpg)

direction has been made and alternative approaches using Rydberg atoms or polar molecules are now being pursued. Meanwhile, recent experiments with trapped ions have demonstrated exotic quantum simulations beyond condensed-matter physics [e.g., Dirac particles (Lamata et al., 2007; Gerritsma et al., 2010) or the Klein paradox (Casanova et al., 2010; Gerritsma et al., 2011)] and superconducting circuits provide a way of studying intriguing quantum phenomena such as the dynamical Casimir effect (Johansson et al., 2010; Wilson et al., 2011; Lähteämäki et al., 2013).

With the current experimental state-of-the-art techniques, the most advanced DQS has been realized with trapped ions (Lanyon et al., 2011). In these experiments, simulations of various spin models with up to six spins have been demonstrated, with one experiment requiring sequences of more than 100 quantum gates. Since no error correction was used, the fidelity of the DQS implementation was somewhat lower than for the AQS implementation in the same system (Friedenauer et al., 2008). With error correction and improved control of laser intensity fluctuations, quantum simulations with  $>10$  qubits and hundreds of high-fidelity gates seem possible in the coming years. Moreover, the DQS approach allows the simulation of complex spin-spin interactions and could potentially be combined with AQS techniques.

# VII. APPLICATIONS

Quantum simulators will find numerous applications in diverse areas of physics and chemistry (Lanyon et al., 2010), and possibly even biology (Ghosh, Smirnov, and Nori, 2009, 2011a, 2011b). Quantum simulation leads to new results that cannot be otherwise simulated and also allows the testing of various theoretical models. In general, with a quantum simulator one could address problems that are either intractable on classical computers or experimentally challenging. Moreover, being quantum systems themselves, quantum simulators are able to provide more insight into quantum phenomena than classical simulators (e.g., the effects of decoherence and the transition from quantum to classical). In this section we discuss how different problems can be studied using the quantum simulators described in Sec. VI. While some problems are classically intractable (e.g., Hubbard models, spin frustration and disorder, lattice gauge theories, and quantum chemistry calculations), others can be treated classically (e.g., James-Cummings Hamiltonian and interferometry) but are discussed here as benchmarks for the progress of quantum simulation.

# A. Condensed-matter physics

The difficulty in solving quantum many-body problems is reflected in the open questions in condensed-matter physics. Among the best-known challenges in this field are understanding high- $T_{c}$  superconductivity and disordered and frustrated systems. In this section we discuss the quantum simulation of these problems.

# 1. Hubbard model

The Hubbard model is the simplest model of interacting particles on a lattice. However, for large numbers of particles

in more than one dimension, the model is difficult to treat using classical computers.

As discussed in Sec. VI.A, an AQS of the Bose-Hubbard model using atoms in optical lattices was proposed by Jaksch et al. (1998) and implemented by Greiner et al. (2002). Recent experiments on the subject include the realization of a Tonks-Girardeau gas in one dimension (Paredes et al., 2004) and the investigation of atoms trapped in a graphene-like lattice (Uehlinger et al., 2013). There have also been proposals to simulate this model with polar molecules (Ortner et al., 2009), trapped ions (Porras and Cirac, 2004a, 2006a; Deng, Porras, and Cirac, 2008) or atoms in arrays of coupled cavities (Brandao, Hartmann, and Plenio, 2007; Zhou, Dong et al., 2008; Zhou, Gong et al., 2008; Liao et al., 2010). The simulation of the Fermi-Hubbard model in quantum-dot arrays was proposed by Byrnes et al. (2007, 2008). The simulation of the Hubbard model with attractive interactions using atoms in optical lattices was discussed by Ho, Cazalilla, and Giamarchi (2009). Proposals for the AQS of the related Holstein model have also been put forward. These include simulations using polar molecules (Herrera and Krems, 2011; Herrera et al., 2013), ions (Stojanovic et al., 2012), and superconducting circuits (Mei et al., 2013).

The simulation of the Hubbard model has also been considered in the context of DQS. Somma et al. (2002) showed how to obtain the energy spectrum of the Fermi-Hubbard Hamiltonian:

$$
\begin{array}{l} H _ {H} = - \sum_ {(i, j); \sigma} \left[ t _ {x} \left(a _ {(i, j); \sigma} ^ {\dagger} a _ {(i + 1, j); \sigma} + a _ {(i + 1, j); \sigma} ^ {\dagger} a _ {(i, j); \sigma}\right) \right. \\ \left. + t _ {y} \left(a _ {(i, j); \sigma} ^ {\dagger} a _ {(i, j + 1); \sigma} + a _ {(i, j + 1); \sigma} ^ {\dagger} a _ {(i, j); \sigma}\right) \right] \\ + \tilde {U} \sum_ {(i, j)} n _ {(i, j); \uparrow} n _ {(i, j); \downarrow}, \tag {21} \\ \end{array}
$$

where  $t_x$  and  $t_y$  are the hopping matrix elements allowing fermions to move on the lattice. The first terms describe the kinetic energy, and the last term  $(\tilde{U})$  is the on-site repulsion potential energy. They explicitly gave the mapping between the operators of the Hubbard model and the DQS; the initialization, evolution, and measurement steps are described in detail. Note that the mapping between the fermionic operators and the Pauli matrices employs the Jordan-Wigner transformation. A possible implementation of DQS for the Holstein model was analyzed by Mezzacapo et al. (2012).

# 2. Spin models

Spin systems are typically described by Hamiltonians of the form

$$
H _ {X Y Z} = \sum_ {i = 1} ^ {N} \left[ J _ {x} \sigma_ {i} ^ {x} \sigma_ {i + 1} ^ {x} + J _ {y} \sigma_ {i} ^ {y} \sigma_ {i + 1} ^ {y} + J _ {z} \sigma_ {i} ^ {z} \sigma_ {i + 1} ^ {z} \right]. \tag {22}
$$

As mentioned in Sec. IV.A, along with the Hubbard Hamiltonian spin Hamiltonians can be simulated on a DQS. It is also worth noting that in certain limits the Hubbard model reduces to spin models.

![](images/6988ed43d9b14268693249fc87c38e4cafd024ca2bd797a727a2ffcb67eb432d.jpg)  
FIG. 17 (color online). Schematic diagram of a proposal for the simulation of anisotropic spin models using polar molecules trapped in an optical lattice: a two-dimensional square lattice with nearest-neighbor orientation-dependent Ising interactions. The effective interactions between the spins  $S_{1}$  and  $S_{2}$  of the molecules in their rovibrational ground states are generated with a microwave field  $E(t)$  inducing dipole-dipole interactions between the molecules with dipole moments  $D_{1}$  and  $D_{2}$ , respectively. From Micheli, Brennen, and Zoller, 2006.

The DQS implementation of various spin Hamiltonians with atoms in optical lattices or trapped ions was discussed by Jané et al. (2003). A recent trapped-ion experiment demonstrated the DQS of different spin Hamiltonians using sequences of elementary quantum gates (Lanyon et al., 2011).

The AQS of spin models is also possible. For instance, with trapped ions, an AQS for the Ising [Eq. (23)],  $XY$  [Eq. (22) with  $J_{z} = 0$ ], or  $XYZ$  [Eq. (22)] interactions can be realized using the collective vibrational modes (Porras and Cirac, 2004b). These interactions can be switched and tuned by lasers and by the choice of trapping conditions. This direction was pursued further by Deng, Porras, and Cirac (2005), Porras and Cirac (2005a, 2005b), Porras et al. (2008), Bermudez, Porras, and Martin-Delgado (2009), Lin, Monroe, and Duan (2011), and Korenblit et al. (2012) and put into practice in the experiments of Friedenauer et al. (2008), Edwards et al. (2010), Kim et al. (2010, 2011), Islam et al. (2011), and Britton et al. (2012). Earlier Milburn (1999) showed that the conditional displacement of the vibrational mode of trapped ions can be used to simulate nonlinear collective and interacting spin systems. Furthermore, spin chains and ladders can be investigated with atoms in optical lattices (Garcia-Ripoll, Martin-Delgado, and Cirac, 2004), and a scheme to realize the anisotropic XXZ [Eq. (22) with  $J_{x} = J_{y}\neq J_{z}]$  and isotropic XXX [Eq. (22) with  $J_{x} = J_{y} = J_{z}]$  Heisenberg spin Hamiltonians in an arbitrary array of coupled cavities was proposed by Cho, Angelakis, and Bose (2008a). Micheli, Brennen, and Zoller (2006) discussed the possibility of engineering Hamiltonians of spin lattice models with polar molecules stored in optical lattices (see Fig. 17). The spins are represented by single electrons of heteronuclear molecules. Using a combination of microwave excitation, dipole-dipole interactions, and spin-rotation couplings enables the realization of effective two-spin interactions with designable range, spatial anisotropy, and coupling strength.

![](images/b4ca94550820744cff4e4e316be37410efd237ed8b26f1ecc3d5cf9ecc2a9bc0.jpg)

![](images/bd513e4857f3056b7da33a90b2921e3d6780b5e430bb52bf72c3721fc1bd9823.jpg)

![](images/e8b08ab1b77c9d852a97e5e3ec3c0c247bb596e373069381c38ed52223305d55.jpg)

![](images/6a7c540789fb2e4ee25a94389d89fbc534b6734c7010cb96f7a8740eab916328.jpg)  
FIG. 18 (color online). Illustration of the experiment of Neeley et al. (2009), in which the states of a superconducting circuit were used to emulate a particle with spin  $s$ , up to  $s = 3/2$ . For simulating a spin  $s$ ,  $2s + 1$  quantum states of the circuit are used. For example, in (d) four of the circuit's quantum states are mapped onto the four quantum states of a spin-3/2 particle, while a fifth state was used in the experiment as a reference state for phase measurement. By applying carefully tuned microwave-frequency drive signals, the circuit can simulate the interaction between the spin and a magnetic field with arbitrary strength and direction. An analogy with a classical system (a soccer game), shown on the left side, can also be used to give a simple explanation of the redistribution of the population among the different energy levels in terms of players passing a ball among each other, with the goalkeeper serving as the anchor. From Nori, 2009.

![](images/7d76f461f6e96b74fb0f58ec154b88eb191cc6a67c1e9bec93e2254a12d5fa63.jpg)

![](images/9b89fac072ecc5f5846549db92c1cb529c9e1d1870ba9e1728f388c47cdce203.jpg)

![](images/aec42619fef1b49a8c4f6f676b42b6ba01e670bece592ab5914a8af7146439f0.jpg)

![](images/a4e49a94cbf6c442a60c41fac5e27c374e7424fb5015570db2ab51e85c67c801.jpg)

Recently, Tsokomos, Ashhab, and Nori (2010) proposed the simulation of spin and Hubbard models in higher or fractal dimensions with superconducting qubits and resonators. The ability to access arbitrary dimensions is made possible by the flexible connectivity, which derives from the flexibility in designing tunable couplers between superconducting qubits and resonators. Spin systems with  $s > 1/2$  can also be naturally realized using superconducting circuits, because these circuits generally have more than two quantum states that can be employed in the simulation. Neeley et al. (2009) demonstrated the emulation of the dynamics of single spins with principal quantum numbers  $s = 1/2$ , 1, and  $3/2$  (see Fig. 18). The antiferromagnetic Heisenberg model with long-range interactions can be realized with solid-state NMR (Roumpos, Master, and Yamamoto, 2007). Itinerant ferromagnetism can be studied in a two-component Fermi gas (Jo et al., 2009).

# 3. Quantum phase transitions

Having introduced the Hubbard model and spin models, we now discuss quantum phase transitions, especially in these models. Quantum phase transitions occur when one varies a

![](images/f0a51b56dbbe3173e0e171aec4bf9dca9a14c971f5493b6dd00430a580709c60.jpg)  
FIG. 19 (color online). Examples of analog quantum simulators of quantum phase transitions using (a) ultracold neutral atoms and (b) trapped ions. (a) The quantum phase transition from a superfluid to a Mott insulator phase realized by Greiner et al. (2002) using rubidium atoms trapped in an optical lattice. The ratio between the tunneling energy and the on-site interaction energy was controlled in Greiner et al. (2002) by adjusting the lattice potential depth, such that the quantum phase transition was observed. There are other alternative ways of simulating this quantum phase transition with arrays of cavities (Hartmann, Brandao, and Plenio, 2006), or arrays of Josephson junctions (van Oudenaarden and Mooij, 1996). (b) Magnetic quantum phase transition simulated by Friedenauer et al. (2008) using trapped calcium ions. The interactions between individual spins and an external magnetic field were simulated by coupling the internal levels (representing the spin-  $1/2$  states) with a resonant rf field, while the spin-spin interactions were simulated using a state-dependent optical dipole force implemented by a walking wave. From Buluta and Nori, 2009.

physical parameter at absolute zero temperature, when all thermal fluctuations have ceased. The transition describes an abrupt change in the ground state of the many-body system governed by its quantum fluctuations. Quantum phase transitions are an interesting and fundamental subject, but are difficult to investigate both by classical simulation and via experimental methods. Analog quantum simulators can help in understanding this purely quantum phenomenon, and the first steps in this direction have already been explored.

For example, the quantum phase transition from a superfluid to a Mott insulator phase, predicted by Fisher et al. (1989), was first observed in 2002 (Greiner et al., 2002) in an ensemble of atoms trapped in an optical lattice. The physical model is described by the Bose-Hubbard Hamiltonian given in Eq. (12). The phase transition is perhaps easiest to understand in the case of a unit filling factor, i.e., when there are as many particles as lattice sites. Deep in the superfluid phase, when  $J \gg \tilde{U}$ , delocalization minimizes the kinetic energy and the system is said to be in the weakly interacting regime [the ground state being approximately given by  $(\sum_{i}\hat{b}_{i}^{\dagger})^{N}|0\rangle$ , i.e., all the particles are in the single-particle ground state]. When  $\tilde{U} \gg J$ , the energy is minimized when the particles are distributed evenly among the lattice sites and the ground state is approximately given by  $\prod_{i}\hat{b}_{i}^{\dagger}|0\rangle$ . This state is sometimes called strongly correlated, and it corresponds to the Mott phase. By adjusting the lattice potential depth, the ratio between the tunneling energy  $J$  and the on-site interaction energy  $\tilde{U}$  can be controlled and brought to the point where the transition between the Mott insulator phase and the superfluid phase is induced. Then an abrupt change in the ground state of the system is observed (Greiner et al., 2002). A schematic

diagram of this quantum phase transition is illustrated in Fig. 19(a).

In quantum magnets, the transition from a paramagnet to an antiferromagnet was emulated using two trapped calcium ions by Friedenauer et al. (2008). The system is described by the quantum Ising model. The Hamiltonian for a chain (with two or more spins) is given by

$$
H _ {I} = - B _ {x} \sum_ {i} \sigma_ {i} ^ {x} + \sum_ {i <   j} J _ {i j} \sigma_ {i} ^ {z} \sigma_ {j} ^ {z}, \tag {23}
$$

where  $B_{x}$  is the magnetic field strength and  $J_{ij}$  are the spin-spin coupling coefficients. The first term, denoting the interactions of individual spins with an external magnetic field, is simulated by coupling the internal levels (representing the two spin-1/2 states) with a resonant rf field. The spin-spin interaction in the second term is simulated by a state-dependent optical dipole force, implemented by a walking wave formed by two perpendicular laser beams. When the strength of the spin-spin interaction is increased adiabatically (increasing  $J$  while keeping  $B_{x}$  constant), the system undergoes a transition from paramagnetic  $(|\rightarrow\rangle|\rightarrow\rangle\cdots|\rightarrow\rangle)$  to ferromagnetic  $(|\downarrow\rangle|\downarrow\rangle\cdots|\downarrow\rangle+\uparrow\rangle|\uparrow\rangle\cdots|\uparrow\rangle)$  or antiferromagnetic order  $(|\downarrow\rangle|\uparrow\rangle\cdots|\downarrow\rangle|\uparrow\rangle+\uparrow\rangle|\downarrow\rangle\cdots|\uparrow\rangle|\downarrow\rangle)$ . This is illustrated in Fig. 19(b). The same technique for realizing the spin-spin interaction, namely, the state-dependent force, can be applied for many ions in a string or ion array. Further experimental investigations in this direction have been performed by Kim et al. (2010) and Islam et al. (2011). A recent experiment demonstrated the quantum simulation of antiferromagnetic

spin chains using neutral atoms in an optical lattice (Simon et al., 2011).

# 4. Disordered and frustrated systems

Disordered systems appear in many difficult problems in condensed-matter physics such as transport, conductivity, spin glasses, and some models of high- $T_{c}$  superconductivity. They can exhibit characteristic phenomena that are not present in perfectly ordered systems. For example, the wave functions of particles can be localized in disordered media in spite of the presence of hopping terms in the Hamiltonian. This phenomenon can occur at the single-particle level by coherent backscattering from random impurities. Since the theoretical treatment of these problems is particularly challenging, several proposals for quantum simulation have been put forward.

The Fano-Anderson Hamiltonian can be studied using DQS. This idea was pursued theoretically and experimentally (with liquid-state NMR) by Negrevergne et al. (2005). The fermionic Fano-Anderson model in one dimension consists of an  $n$ -site ring with an impurity in the center. The fermions can hop between nearest-neighbor sites on the ring or between a site on the ring and the impurity (with matrix element  $V / \sqrt{n}$  for the latter). The Fano-Anderson Hamiltonian can be written as follows:

$$
H _ {\mathrm {F A}} = \sum_ {l = 0} ^ {n - 1} \varepsilon_ {k _ {l}} c _ {k _ {l}} ^ {\dagger} c _ {k _ {l}} + \epsilon b ^ {\dagger} b + V \left(c _ {k _ {0}} ^ {\dagger} b + c _ {k _ {0}} b ^ {\dagger}\right), \tag {24}
$$

![](images/6784301b9b2bdc22ad736de55738e6e399907efdc56a89e8db83ab39fc2ad363.jpg)  
FIG. 20 (color online). Spin configurations in a triangular lattice and their experimental signatures, simulated using the motional degrees of freedom of atoms trapped in an optical lattice, averaged over several experimental runs. The coupling parameters can be tuned to ferromagnetic (solid lines) or antiferromagnetic values (dashed lines), and these determine the resulting spin configuration. From Struck et al., 2011.

where the fermionic operators  $c_{k_l}^\dagger (c_{k_l})$  and  $b^{\dagger}(b)$  create (destroy) a spinless fermion in the conduction mode  $k_{l}$  and in the impurity, respectively. Note that in principle the Hamiltonian in Eq. (24) can be diagonalized exactly. Nevertheless, the experiment serves as a benchmark for the experimental progress of quantum simulators. Recently, the decoherence-induced localization of the size of spin clusters was investigated in an NMR quantum simulator (Álvarez and Suter, 2010). Thermal states of frustrated spin systems were also simulated recently using NMR (Zhang et al., 2012).

As for AQS, optical lattices have been used to experimentally realize a disordered system that may lead to the observation of a Bose glass phase (Fallani et al., 2007). In a recent experiment, the motional degrees of freedom of atoms trapped in an optical lattice were used to simulate ferromagnetic, antiferromagnetic, and frustrated classical spin configurations (Struck et al., 2011). A rich phase diagram with different types of phase transitions was observed. Figure 20 shows examples of spin configurations in a triangular lattice and their experimental signatures. Furthermore, theoretical and experimental studies have investigated possible routes toward Anderson-like localization of atomic BECs in disordered potentials (Schulte et al., 2005; Billy et al., 2008; Roati et al., 2008). A review focused on the simulation of disordered quantum systems with quantum gases has been given by Bouyer (2010). A chain of trapped ions could also be used to explore the physics of disordered quantum systems (Bermudez, Martin-Delgado, and Porras, 2010). Garcia-Ripoll, Solano, and Martin-Delgado (2008) proposed a mapping between superconducting circuits and the Hamiltonians describing magnetic impurities in conduction bands (Anderson and Kondo models). A recent experiment on a driven superconducting qubit (Gustavsson, Bylander, and Oliver, 2013), along with the appropriate mapping, exhibited an analog of universal conductance fluctuations, which are typically studied in the context of particle propagation in two-dimensional disordered media.

Geometric frustration refers to the situation in which the geometric properties of the crystal lattice forbid the simultaneous minimization of all the interaction energies acting in a given region (see Fig. 21). Well-known examples include the antiferromagnetic Ising model on a triangular lattice or the antiferromagnetic Heisenberg model on a kagome lattice. Frustrated antiferromagnets are materials whose quantum Monte Carlo simulation suffers from a severe sign problem. There have been studies on the AQS of frustrated spin models with trapped ions (Porras and Cirac, 2006b; Kim et al., 2010; Bermudez et al., 2011; Ivanov and Schmidt-Kaler, 2011), NMR (Peng et al., 2009), photons (Ma et al., 2011), and atoms in optical lattices [see Lewenstein et al. (2007) and references therein, Becker et al. (2010), Liu et al. (2010), and Struck et al. (2011)].

# 5. Spin glasses

Spin glasses typically occur when the interactions between spins are ferromagnetic for some bonds and antiferromagnetic for others, so the spin orientation cannot be uniform in space even at low temperatures, and the spin orientation can become random and almost frozen in time. Spin glasses can be

![](images/fe176faa740475b8554b1529532427e745acd2ac27b4a13e3dadfee3682be0e6.jpg)  
(a)

![](images/503d8d23c67e5a20728fb4231e89bd9c5456cf0bef4e21a5e9eedab8f7602c9d.jpg)  
(b)

![](images/7acbd46418b97ae41769436b8f183115bebb48ec9b7b4292457a50b292837402.jpg)  
(c)  
FIG. 21. An example of the simulation of the simplest case of spin frustration: (a) three antiferromagnetically coupled spins. This simulation was realized with (b) three ytterbium ions in a one-dimensional trap.  $J_{1}$  is the nearest-neighbor coupling and  $J_{2}$  is the next-nearest-neighbor coupling. (c) The expected form of the Ising interactions  $J_{1}$  and  $J_{2}$ , controlled through the laser detuning  $\tilde{\mu}$ , used to generate an optical spin-dependent force, is depicted. The three oscillation modes shown at the top of (c) are used as markers, as the parameter  $\tilde{\mu}$  is defined relative to their frequencies. From Kim et al., 2010.

efficiently simulated using DQS. Lidar and Biham (1997) and Lidar (2004) developed an algorithm for the construction of the Gibbs distribution of configurations in the Ising model. The algorithm can be applied to any dimension, to the class of spin-glass Ising models with a finite portion of frustrated plaquettes, to diluted Ising models, and to models with a magnetic field.

An analog approach to the simulation of spin glasses using magnetic impurities embedded in inert matrices, such as solid helium, was proposed by Lemeshko et al. (2013). A proposal for the analog simulation of the Lipkin-Meshkov-Glick model and complex quantum systems, such as Sherrington-Kirkpatrick spin glasses, using superconducting qubits in circuit QED was given by Tsomokos, Ashhab, and Nori (2008). Spin glasses could also be studied using Fermi-Bose mixtures in inhomogeneous and random optical lattices as suggested by Sanpera et al. (2004) and Ahufinger et al. (2005).

# 6. Superconductivity

The high-temperature superconductivity of compounds containing copper-oxide planes is still a puzzle that might be solved using large-scale simulations. The  $\mathrm{CuO}_2$  plane in a high- $T_{c}$  superconductor (Orenstein and Millis, 2000) can be simulated in an analog manner by an array of electrostatically defined quantum dots, as suggested by Manousakis (2002) in one of the early proposals for AQS. Moreover, the analog simulation of the  $t-J$  model was proposed by Yamaguchi and Yamamoto (2002). The  $t-J$  model describes strongly correlated fermions on a lattice and it is used in various attempts to

understand high-  $T_{c}$  superconductivity. Here  $t$  represents the size of the kinetic energy of a hole disrupting an antiferromagnet with spin-spin interaction energy  $J$ .

The study of BCS pairing in superconductors could be done using DQS. The general BCS pairing Hamiltonian has the following form:

$$
H _ {\mathrm {B C S}} = \sum_ {m = 1} ^ {N} \frac {\epsilon_ {m}}{2} \left(n _ {m} ^ {F} + n _ {- m} ^ {F}\right) + \sum_ {m, l = 1} ^ {N} V _ {m l} ^ {+} c _ {m} ^ {\dagger} c _ {- m} ^ {\dagger} c _ {- l} c _ {l}, \tag {25}
$$

where the fermionic  $c_m^\dagger (c_m)$  are creation (annihilation) operators,  $|m| = 1,2,\ldots ,N$  denotes all relevant quantum numbers, the number operator  $n_{\pm m}^{F} = c_{\pm m}^{\dagger}c_{\pm m}$ , and the matrix element  $V_{ml}^{+} = \langle m, - m|V|l, - l\rangle$ . A polynomial-time algorithm to model this BCS Hamiltonian was proposed by Wu, Byrd, and Lidar (2002) and Wang and Yang (2006) and a two-qubit version of the algorithm was experimentally realized using NMR (Yang et al., 2006).

In another direction related to the quantum simulation of superconductivity, several groups have observed signatures of the crossover between a BCS and a BEC superfluid as the strength of attractive interactions between fermionic particles is varied [see, e.g., Regal, Greiner, and Jin (2004), Zwierlein et al. (2005), and Lewenstein et al. (2007), and references therein].

# 7. Metamaterials

The behavior of tunable metamaterials (regular structures obtained from the periodic arrangement of mesoscopic building blocks) in the quantum regime can be seen as a quantum simulation of materials composed of regular atomic structures (Bliokh et al., 2008; Rakhmanov et al., 2008, 2010). One example of a quantum metamaterial is an infinite chain of identical qubits inside a resonator. Such a system offers new ways of controlling the propagation of electromagnetic fields, which are not available to standard materials.

# 8. Topological order

Anyons are two-dimensional particles whose quantum statistics are neither bosonic nor fermionic. Anyons have been used to describe two-dimensional systems such as sheets of graphene or the quantum Hall effect. Moreover, they have been proposed as media for implementing topological quantum computation (Kitaev, 2003). The fractional statistics of anyons in the Kitaev model (Kitaev, 2003) involving four-body interactions can be studied using AQs with cold atoms in optical lattices or alternatively using DQS (Han, Raussendorf, and Duan, 2007). The latter approach has been experimentally realized with linear optics (Lu et al., 2009). The Hamiltonian

$$
H _ {K} = - \sum_ {v} A _ {v} - \sum_ {p} B _ {p} \tag {26}
$$

is the sum of mutually commuting stabilizers  $A_v = \prod_{i \in v} \sigma_i^x$  and  $B_p = \prod_{i \in p} \sigma_i^z$ , where  $v$  runs over the vertices and  $p$  over the plaquettes (i.e., the small squares defined by four neighboring vertices) in a square lattice and the products involve the qubits

![](images/079d9450ca383dc498fd3dd1826ceac413f0b10cff1ae2a3e6cc53122a4d2627.jpg)  
FIG. 22 (color online). Schematic diagram of the basic building block of a Kitaev lattice, consisting of four superconducting charge qubits (labeled 1 to 4): (i) Qubits 1 and 2 are inductively coupled via a mutual inductance  $M$ ; (ii) qubits 1 and 3 are coupled via an  $LC$  oscillator; and (iii) qubits 1 and 4 are capacitively coupled via a mutual capacitance  $C_m$ . Inset: These three types of interqubit couplings are denoted as  $X$ ,  $Y$ , and  $Z$  bonds. From You et al., 2010.

surrounding the vertices or plaquettes (note that in this setup the qubits are placed at the centers of lines connecting neighboring vertices). In optical lattices the creation and manipulation of Abelian and non-Abelian anyons in topological lattice models can be realized using ancilla particles (Aguado et al., 2008). Furthermore, it is possible to construct a Kitaev honeycomb lattice with superconducting circuits (You et al., 2010) (see Fig. 22). Topological models have also been investigated by Freedman, Kitaev, and Wang (2002), Micheli, Brennen, and Zoller (2006), Brennen, Aguado, and Cirac (2009), Stanescu et al. (2009), Xue (2011), and Kitagawa (2012). The implementation of these proposals can also contribute to the development of topological quantum computation.

# B. High-energy physics

Another area for the application of quantum simulation that is already showing promising developments is high-energy physics. The study of relativistic quantum systems such as gauge fields or Dirac fermions with quantum simulators was first suggested by Boghosian and Taylor (1998b).

More recently, a mapping between the dynamics of the  $2 + 1$  Dirac oscillator and the Jaynes-Cummings model (in particular, in connection with trapped-ion experiments) was proposed by Bermudez, Martin-Delgado, and Solano (2007). Such mappings would allow the study of relativistic quantum mechanics described by the Dirac equation in a nonrelativistic quantum system. A method for simulating the Dirac equation in  $3 + 1$  dimensions for a free spin-  $1 / 2$  particle using a single trapped ion was proposed by Lamata et al. (2007). This simulation offers the possibility of studying effects such as Zitterbewegung and the Klein paradox. Zitterbewegung refers to the rapid oscillatory motion of a free particle obeying the

Dirac equation. Zitterbewegung has never been observed in its original form with free relativistic particles, but it has been simulated with a trapped ion (Gerritsma et al., 2010). A recent paper extended this work to the study of Zitterbewegung in a magnetic field (Rusin and Zawadzki, 2010) [see also K. Wang et al. (2010)]. The Klein paradox refers to the situation in relativistic quantum mechanics where a potential barrier of the order of the electron mass becomes nearly transparent for the electron. A quantum simulation of this phenomenon was recently implemented with trapped ions (Gerritsma et al., 2011). A proposal for a simulation using graphene was put forward by Katsnelson, Novoselov, and Geim (2006). Note that it is also possible to classically simulate the Zitterbewegung of a free Dirac electron in an optical superlattice (Dreisow et al., 2010). Dirac particles could also be investigated with neutral-atom quantum simulators (Goldman et al., 2009; Hou, Yang, and Liu, 2009; Braun, 2010; Cirac, Maraner, and Pachos, 2010; Witthaut, 2010; Casanova et al., 2011).

The simulation of gauge theories can be a very computationally intensive quantum many-body problem, and there have been several recent proposals for the quantum simulation of such theories. For example, several theoretical studies considered Abelian (Kapit and Mueller, 2011; Banerjee et al., 2012; Zohar, Cirac, and Reznik, 2012; Tagliacozzo, Celi, Zamora, and Lewenstein, 2013) and non-Abelian (Banerjee et al., 2013; Stannigel et al., 2013; Tagliacozzo, Celi, Orland, and Lewenstein, 2013; Zohar, Cirac, and Reznik, 2013) lattice gauge theories using neutral atoms. A review on the subject was given by Wiese (2013). There have also been related proposals using trapped ions (Casanova et al., 2011, 2012), cavity QED systems (Barrett et al., 2013), and superconducting circuits (Marcos et al., 2013; Pedernales et al., 2013). A recent experiment (Lähteenmäki et al., 2013) used a superconducting circuit to simulate a massless Klein-Gordon field with tunable speed of propagation, which was used to simulate the generation of photons in the dynamical casimir effect. Hauke et al. (2013) considered the possible simulation of the Schwinger model using a chain of trapped ions. The simulation of lattice gauge theories on a DQS was investigated by Byrnes and Yamamoto (2006). They gave the mapping between the operators in the lattice gauge Hamiltonian for the U(1), SU(2), and SU(3) (which is particularly important for quantum chromodynamics) lattice gauge theories and spin operators, and they showed that the algorithm is efficient. Another proposal for the DQS of field theories was given by Jordan, Lee, and Preskill (2012).

Atoms in optical lattices offer the possibility of realizing the AQS of ring-exchange models (Büchler et al., 2005; Tewari et al., 2006). Ring-exchange models describe elementary excitations in a solid, where, a ring of hard-core bosons collectively rotate like a ring around a central boson. The ring exchange Hamiltonian,

$$
H _ {\mathrm {R E}} = K \sum_ {\text {p l a q u e t t e s}} \left(b _ {1} ^ {\dagger} b _ {2} b _ {3} ^ {\dagger} b _ {4} + b _ {4} ^ {\dagger} b _ {3} b _ {2} ^ {\dagger} b _ {1} - n _ {1} n _ {2} - n _ {3} n _ {4}\right), \tag {27}
$$

can be realized using atoms with two internal states: one state trapped in a square lattice [see Fig. 23(a)] and described by the

![](images/6e3b932bc2ab89062eafbb9033a2e1231d78e7339307b6c7159df6bcbcf0adcc.jpg)  
(a)

![](images/bd2e3449b5fa3d1a5f96ce397faac5f6ea50658cd0d0b8bdb8605ebb04cf3169.jpg)  
FIG. 23. (a) Proposed setup for the simulation of ring-exchange models. The bosons (black dots) reside on a square lattice with the molecules (gray dots) at the centers of the plaquettes. Adapted from Buchler et al., 2005. (b) Simulation of compact U(1) lattice gauge theories. Dipolar bosons reside on the sites of the kagome lattice (black dots); the hexagonal dual lattice is the lattice formed by the centers of the corner-sharing triangles (gray dots). Adapted from Tewari et al., 2006.  
(b)

simple Bose-Hubbard model, and a second one trapped at the centers of the plaquettes. In trapped atomic gases a microscopic Hamiltonian can be implemented and its phase diagram can be studied experimentally via controlling the strength of the interaction terms (Büchler et al., 2005). Furthermore, with this system it is possible to simulate a certain class of strong coupling Hamiltonians, and in doing so, study exotic phases with strong correlations. By implementing a Hubbard model with an additional, strong nearest-neighbor interaction on certain two- or three-dimensional lattices (for example, a two-dimensional kagome lattice) the simulation of a U(1) lattice gauge theory would be possible (Tewari et al., 2006) [see Fig. 23(b)]. Noninteracting relativistic fermionic theories or topological insulators could also be investigated using these systems (Mazza et al., 2012).

Semiao and Paternostro (2012) proposed a quantum-circuit simulation of the state of a nucleon. This simulation could be implemented using a photonic network. Finally, we also note the possible simulation of the O(3) nonlinear sigma model using an array of superconducting and insulating spheres with electrons trapped in the insulating spheres, as discussed by Schützhold and Mostame (2005).

# C. Cosmology

Quantum simulation can also find applications in analog gravity or cosmology models. For example, acoustic waves in a two-component BEC can be used to investigate scalar fields within the curved space-time structure of an expanding universe (Fischer and Schützhold, 2004). The simulation can be performed by varying the interparticle coupling and/or expanding the condensate in a temporal ramp. This idea might be experimentally challenging but it opens up a new possible way to study cosmology. The study of the analog of cosmological particle creation with trapped ions was proposed by Schützhold et al. (2007), and more recently, the analog of quantum field effects in cosmological space-times was investigated by Menicucci, Olson, and Milburn (2010). There are also numerous similarities between the behavior of superfluid helium and cosmological phenomena, such as processes in the

early Universe, as discussed in detail by Volovik (2009). These similarities could be exploited, and a system of liquid helium could be used for the quantum simulation of problems in cosmology.

With analog models it is possible to test predicted phenomena that have not yet been observed in experiment. Examples include the possible observation of an Unruh-like effect (i.e., the observation by an accelerating observer of a thermal flux of particles in vacuum) using the phonon excitation of trapped ions (Alsing, Dowling, and Milburn, 2005) and the simulation of the Schwinger effect (i.e., the production of electron-positron pairs from the vacuum under the action of a strong electric field) with atoms in an optical lattice (Szpak and Schutzhold, 2011, 2012). Furthermore, analogs of Hawking radiation can be investigated with atoms (Giovanazzi, 2005), ions (Horstmann et al., 2010) and superconducting circuits (Nation et al., 2009), exciton-polariton superfluids in semiconductors (Gerace and Carusotto, 2012), or even with ultrashort pulses of light in microstructured optical fibers (Philbin et al., 2008) [see also (Nation et al. (2012)]. Recently it was demonstrated that Hawking radiation can be measured in a classical analog system, namely, water surface waves (Weinfurtner et al., 2011).

# D. Atomic physics

There is a deep analogy between natural atoms and the artificial atoms formed, for example, by electrons in small superconducting circuits (You and Nori, 2005, 2011). Both have discrete energy levels and exhibit coherent quantum oscillations between those levels. But whereas natural atoms are driven using visible or microwave photons that excite electrons from one state to another, the artificial atoms in the circuits are driven by currents, voltages, and microwave photons. The resulting electric and magnetic fields control the tunneling of electrons across Josephson junctions. The effects of those fields on the circuits are the analogs of the Stark and Zeeman effects in atoms. Differences between quantum circuits and natural atoms include how strongly each system couples to its environment (the coupling is weak for atoms and strong for circuits) and the energy scales of the two systems. In contrast with naturally occurring atoms, artificial atoms can be lithographically designed to have specific characteristics, such as a large dipole moment or particular transition frequencies. This tunability is an important advantage over natural atoms. Superconducting circuits can also be used for new types of masers, lasers, and single-photon generators (You et al., 2007). These circuits can provide analogs of sideband cooling and Sisyphus cooling (Grajcar et al., 2008; Nori, 2008) (see Fig. 24). Moreover, they can be used to test Bell inequalities (Ansmann et al., 2009), produce Schrödinger-cat states, study Landau-Zener-Stückelberg interferometry (Shevchenko, Ashhab, and Nori, 2010), and simulate the Einstein-Podolsky-Rosen experiment (You and Nori, 2005). Superconducting circuits have also been used to engineer selection rules and thus create combinations of selection rules that are not possible with natural atoms (Liu et al., 2005; Deppe et al., 2008; Harrabi et al., 2009; de Groot et al., 2010).

![](images/05451654cc2a5fc0c7afc68bdb1a6fddaf5904fa330f299fca328cf670fc35ec.jpg)  
FIG. 24 (color online). Sisyphus cooling and amplification in a superconducting circuit (Grajcar et al., 2008; Nori, 2008). The two energy levels of a superconducting qubit are shown as a function of the current applied to the circuit. The current in a nearby superconducting resonator drives the qubit, and a microwave drive signal is applied to the qubit. The cycle  $a \rightarrow b \rightarrow c \rightarrow d$  on the right side mimics Sisyphus cooling in atomic physics: the energy of emitted photons is higher than the energy of photons absorbed from the drive signal, causing a constant removal of energy from the resonator. In the analogy with Sisyphus in Greek mythology the current in the resonator plays the role of Sisyphus and the qubit plays the role of the rock. Sisyphus is constantly pushing the rock uphill (as can be seen in steps a and c), and the rock keeps going back to the bottom of the hill. The cycle  $e \rightarrow f \rightarrow g \rightarrow h$  on the left side represents the opposite scenario, Sisyphus amplification, where energy is constantly added to the resonator. Adapted from Nori, 2008.

One of the most important models in atomic physics and quantum optics is the Jaynes-Cummings Hamiltonian, which describes the interaction of a single quantized mode of the electromagnetic field with a two-level atom:

$$
H _ {\mathrm {J C}} = i \hbar g _ {0} \left(a ^ {\dagger} \sigma_ {-} - a \sigma_ {+}\right), \tag {28}
$$

where  $g_{0}$  is the atom-field coupling strength, the operators  $a^{\dagger}$  and  $a$  are the bosonic creation and annihilation operators, and  $\sigma_{+}$  and  $\sigma_{-}$  are the atomic raising and lowering operators.

The Jaynes-Cummings Hamiltonian can be realized with superconducting circuits (You and Nori, 2003, 2005, 2011; Wallraff et al., 2004; Schoelkopf and Girvin, 2008; Zueco et al., 2009).

# E. Quantum chemistry

Quantum simulators can also have an important contribution in quantum chemistry (Kassal et al., 2011). For example, an efficient algorithm for calculating the thermal rate constant was given by Lidar and Wang (1999). The algorithm involves the initialization of the DQS to an equal superposition of position eigenstates, followed by a unitary evolution that makes use of the quantum Fourier transform and finally, a sequence of measurements yielding the energy spectrum and eigenstates. The algorithm runs in polynomial time while any

exact classical simulation is bound to exhibit exponential scaling. Another example is the multiconfiguration self-consistent field wave-function-based quantum algorithm proposed by Wang et al. (2008) for obtaining the energy spectrum of a molecular system.

Moreover, a quantum computer could be used to simulate the static and dynamical chemical properties of molecules. Aspuru-Guzik et al. (2005) showed how to compute molecular energies using DQS and the required number of qubits was estimated (see also Fig. 4). The number of qubits scales linearly with the number of basis functions, and the number of gates grows polynomially with the number of qubits, so simulations with a few tens or a hundred qubits would already outperform classical computers. The simulation of chemical dynamics is also achievable in polynomial time (Kassal et al., 2008). The molecular energies of the hydrogen molecule have been calculated using a small photonic DQS (Lanyon et al., 2010). More recently, chemical reaction dynamics have been investigated using NMR DQS (Lu et al., 2011).

Using AQS it would be possible to simulate chemical reactions. Smirnov et al. (2007) proposed using the redistribution of electrons between semiconductor quantum dots to simulate the redistribution of electrons in a chemical reaction. They showed how a quantum dot with one electron can be considered an artificial hydrogen atom and a quantum dot containing four electrons can be viewed as an artificial oxygen atom. Depending on the tunnel coupling strengths, electron distribution, and shell structure, the dots can form both ionic-like and covalent-like bonds. Various reaction regimes and different reaction products can be obtained by varying the speed of voltage changes applied to the gates forming the quantum dots. This promises the modeling of various chemical reactions (Smirnov et al., 2007). Furthermore, a recent proposal suggests that chemical reactions can also be simulated with ultracold atoms in a waveguide (Torrontegui et al., 2011).

# F. Open quantum systems

Simulating the dynamics of open quantum systems is even more costly than that of closed quantum systems because solving the Lindblad equation requires quadratically more resources than solving the Schrödinger equation for the same physical system. Simulating open quantum systems with quantum simulators can be done in two ways. First, one could exploit the natural decoherence of the simulator, as first suggested by Lloyd (1996) and investigated experimentally by Tseng et al. (2000) (see also Sec. V.B). Second, it is also possible to simulate open quantum systems with closed quantum systems. A simulation of decoherence caused by classical noise that was artificially added to the control signal of a superconducting qubit was reported by Li et al. (2013). Piilo and Maniscalco (2006) theoretically showed that a driven harmonic oscillator can act as a quantum simulator for the non-Markovian damped harmonic oscillator. Other studies considered the Dicke model (Schneider and Milburn, 2001; Chen, Chen, and Liang, 2007), the open-system dynamics of a harmonic oscillator coupled to an artificially engineered reservoir (Lütkenhaus, Cirac, and Zoller, 1998; Maniscalco et al., 2004), or open quantum systems in thermal equilibrium

(Terraneo, Georgeot, and Shepelyansky, 2003). Weimer et al. (2011) discussed an open-system quantum simulator with Rydberg states of neutral atoms in an optical lattice. General methods for simulating the Markovian dynamics of open quantum systems have been investigated by Terhal and DiVincenzo (2000), Bacon et al. (2001), and Wang, Ashhab, and Nori (2011). A recent experiment with trapped ions demonstrated the possibility of engineering open-system dynamics using the dissipative preparation of entangled states (Barreiro et al., 2011). Another recent experiment simulated non-Markovian dynamics using a linear-optics setup (Chiuri et al., 2012).

# G. Quantum chaos

An application of DQS with a few qubits is the study of the dynamics of simple quantum maps (Schack, 1998; Terraneo, Georgeot, and Shepelyansky, 2003; Georgeot, 2004; Levi and Georgeot, 2004). For instance, the quantum baker's map, a prototypical example in quantum chaos, has an efficient realization in terms of quantum gates (Schack, 1998). The quantum baker's map has been experimentally realized in NMR (Weinstein et al., 2002) and with linear optics (Howell and Yeaze, 1999). Another example is the kicked Harper model (Levi and Georgeot, 2004). It has been shown that in some cases the quantum approach to the kicked Harper model can provide a polynomial gain as compared to classical algorithms. It should exhibit observable interesting behavior even with only eight qubits.

# H. Nuclear physics

In nuclear physics one must solve an  $N$ -body quantum problem. Even though  $N$  is not as large as in condensed-matter physics (in this case  $N$ , the atomic mass number, is smaller than 300), the calculation of the nuclear force is difficult and therefore nuclear physics simulations require significant computing power. Several phenomenological models have been developed, one of which is the superfluid model of the atomic nucleus. As suggested by Georgescu et al. (2011), this model could be simulated using an analog controllable system: a superfluid gas of fermionic atoms. Given the ease of rotating atomic clouds, this approach offers the possibility of studying the response of nuclei to increasing angular momentum with unprecedented control over the relevant parameters such as the interaction strength, particle number, external trapping potential, and rotation frequency. The reviews by Zinner and Jensen (2008, 2013) detail similarities between atomic nuclei and cold atomic gases, which could be utilized for designing quantum simulators of nuclei using atomic ensembles.

# I. Interferometry

Nonlinear interferometers were first investigated in trapped-ion experiments (Leibfried et al., 2002). This was among the first experimental realizations of quantum simulation. More recently, the study of Mach-Zehnder interferometry with an array of trapped ions was explored by Hu, Feng, and Lee (2012).

Boson sampling (Aaronson and Arkhipov, 2011) is another interferometry problem that is closely related to quantum simulation. Several recent experiments have demonstrated boson sampling using photons (Broome et al., 2013; Crespi et al., 2013; Spring et al., 2013; Tillmann et al., 2013), and Lau and James (2012) proposed an implementation using trapped ions.

Superconducting qubits can be used, for example, to perform Landau-Zener-Stückelberg interferometry (Shevchenko, Ashhab, and Nori, 2010) and Fano and Fabry-Pérot interferometry (Zhou, Dong et al., 2008; Ian, Liu, and Nori, 2010; Liao et al., 2010). These latter phenomena can be realized using quasi-one-dimensional open systems where photons are injected from one side and move toward the opposite side of the device. Along the way, the photons interact with either one or two qubits acting as tunable mirrors, controlled by changing the applied electric and/or magnetic fields on the qubits. These qubits, operating as tunable mirrors, can change the reflection and transmission coefficients of photons confined in waveguides.

# J. Other applications

Some recent topics in physics research, such as Majorana fermions (Casanova et al., 2011; You et al., 2011), graphene (Gibertini et al., 2009) or neutrino oscillations (Noh, Rodriguez-Lara, and Angelakis, 2012), are now discussed in the context of quantum simulation.

The possibility of simulating the Schrödinger equation on a DQS was first discussed in 1996 (Lloyd, 1996), with concrete algorithms given in 1998 (Boghosian and Taylor, 1998a), where a quantum lattice-gas model for the many-particle Schrödinger equation in  $d$  dimensions was proposed. More recently, the single-particle Schrödinger equation was considered by Benenti and Strini (2008), where it was shown that six to ten qubits would be sufficient for a simulation of the single-particle Schrödinger equation.

Another direction of interest is quantum heat engines, quantum Brownian motion (Hänggi, Marchesoni, and Nori, 2005; Hänggi and Marchesoni, 2009), and quantum thermodynamics (Maruyama, Nori, and Vedral, 2009). The quantum versions of the Carnot and other heat engines were discussed by Quan et al. (2007). A proposal for the implementation of a quantum heat engine assisted by a Maxwell demon with superconducting circuits was given by Quan et al. (2006).

There are many potential applications for quantum simulators in various fields of physics and chemistry. As mentioned at the beginning of this section, with quantum simulation one can address problems that are either classically intractable (such as the numerous examples from condensed-matter physics discussed above) or experimentally difficult or inaccessible (such as the examples from high-energy physics and cosmology). As practical quantum simulators become available, it is to be expected that more disciplines will want to add quantum simulation to their toolbox of research methods and many new applications will be uncovered.

# VIII. CONCLUDING REMARKS

Recent theoretical and experimental results on quantum simulation lead us to believe that practical quantum simulators

will be built in the near future. The demonstration of quantum simulations using more than a few tens of qubits would mark the point where quantum computers (whether digital or analog) surpass their classical counterparts, at least for certain applications. This would be a milestone for physics, computer science, and science in general.

However, there are still issues that must be addressed. From the experimental point of view, in all proposed quantum simulators improved controllability and scalability are required. With the exception of atoms in optical lattices, quantum simulators cannot yet handle large arrays of qubits. On the other hand, individual control and readout are difficult to realize for atoms in optical lattices, while for other systems that is not a problem. We note here that for some problems where bulk properties are of interest, individual control and measurement may not be required. It is also important to note that, as some recent experiments with trapped ions and superconducting qubits have demonstrated, even with a small-scale quantum simulator exciting physical phenomena could be explored.

From the theoretical point of view, further studies of decoherence and control would be very useful, especially the estimation of the experimental requirements for each quantum simulator. It is also of both theoretical and practical importance to investigate when and to what extent one can make use of the simulator's decoherence.

Quantum simulators would not only provide insights into new physical phenomena, but also help solve difficult quantum many-body problems. Moreover, theoretical and experimental progress in quantum simulation will also have a positive impact on the development of other fields such as adiabatic quantum computation (Farhi et al., 2001), measurement-based quantum computation (Raussendorf, Browne, and Briegel, 2003), topological quantum computation (Kitaev, 2003), and the theory of quantum computation (Vollbrecht and Cirac, 2008). For example, adiabatic quantum computation can be viewed as a special case of quantum simulation where the ground state of the simulated Hamiltonian encodes the solution to a computational problem. The ability to simulate various Hamiltonians could then be useful for realizing practical adiabatic quantum computation (Ashhab, Johansson, and Nori, 2006). Progress on the experimental implementation of quantum simulation would also be relevant for measurement-based quantum computation. For instance, ions in planar Coulomb crystals (Taylor and Calarco, 2008; Wunderlich, 2009) and atoms in optical lattices (Kay, Pachos, and Adams, 2006) have been proposed for implementing measurement-based quantum computation. The study of entanglement in many-body systems and its relation with quantum phase transitions (Amico et al., 2008) should also be mentioned as an exciting direction closely related to quantum simulation. Finally, the ability to incorporate nonphysical operations into quantum simulations of physical systems (Mezzacapo et al., 2012) could lead to new possibilities for studying quantum simulation and quantum systems in general.

Quantum simulation will profoundly impact physics research. It will provide a new tool for testing physical theories or predicting the behavior of physical systems in various possible conditions, in addition to allowing access to

new physical regimes that are currently beyond experimental reach. Even in the absence of a theory to be tested or realistically motivated conditions under which the behavior of a physical system is to be predicted, quantum simulators will also offer scientists a new realm of exploration. It might very well happen that unpredicted discoveries are made through the curiosity-driven experimentation with future quantum simulators.

# ACKNOWLEDGMENTS

We thank N. Lambert and P. Nation for useful comments on the manuscript. This work was partially supported by the ARO, the RIKEN iTHES Project, the MURI Center for Dynamic Magneto-Optics, the JSPS-RFBR Contract No. 12-02-92100, a Grant-in-Aid for Scientific Research (S), MEXT Kakenhi on Quantum Cybernetics, and the JSPS via its FIRST program.

# REFERENCES

Aaronson, S., and A. Arkhipov, 2011, Proceedings of the 43rd Annual ACM Symposium on Theory of Computing (ACM, New York), 333.  
Abrams, D., and S. Lloyd, 1997, Phys. Rev. Lett. 79, 2586.  
Abrams, D. S., and S. Lloyd, 1999, Phys. Rev. Lett. 83, 5162.  
Aguado, M., G. K. Brennen, F. Verstraete, and J. I. Cirac, 2008, Phys. Rev. Lett. 101, 260501.  
Ahufinger, V., L. Sanchez-Palencia, A. Kantian, A. Sanpera, and M. Lewenstein, 2005, Phys. Rev. A 72, 063616.  
Alsing, P., J. Dowling, and G. Milburn, 2005, Phys. Rev. Lett. 94, 220401.  
Álvarez, G. A., and D. Suter, 2010, Phys. Rev. Lett. 104, 230403.  
Amasha, S., K. MacLean, I. P. Radu, D. M. Zumbuhl, M. A. Kastner, M. P. Hanson, and A. C. Gossard, 2008, Phys. Rev. Lett. 100, 046803.  
Amico, L., R. Fazio, A. Osterloh, and V. Vedral, 2008, Rev. Mod. Phys. 80, 517.  
Angelakis, D.G., M. Huo, D. Chang, L.C. Kwek, and V. Korepin, 2013, Phys. Rev. Lett. 110, 100502.  
Angelakis, D. G., M. Huo, E. Kyoseva, and L. C. Kwek, 2011, Phys. Rev. Lett. 106, 153601.  
Angelakis, D. G., and C. Noh, 2013, arXiv:1306.2179.  
Angelakis, D. G., M. F. Santos, and S. Bose, 2007, Phys. Rev. A 76, 031805.  
Ansmann, M., et al., 2009, Nature (London) 461, 504.  
Ashhab, S., J. Johansson, and F. Nori, 2006, Phys. Rev. A 74, 052330.  
Ashhab, S., A. O. Niskanen, K. Harrabi, Y. Nakamura, T. Picot, P.C. de Groot, C.J.P.M. Harmans, J.E. Mooij, and F. Nori, 2008, Phys. Rev. B 77, 014510.  
Aspuru-Guzik, A., A.D. Dutoi, P.J. Love, and M. Head-Gordon, 2005, Science 309, 1704.  
Aspuru-Guzik, A., and P. Walther, 2012, Nat. Phys. 8, 285.  
Bacon, D., A. M. Childs, I. L. Chuang, J. Kempe, D. W. Leung, and X. Zhou, 2001, Phys. Rev. A 64, 062302.  
Bakr, W., J. Gillen, A. Peng, S. Fölling, and M. Greiner, 2009, Nature (London) 462, 74.  
Bakr, W. S., A. Peng, M. E. Tai, R. Ma, J. Simon, J. I. Gillen, S. Fölling, L. Pollet, and M. Greiner, 2010, Science 329, 547.  
Banerjee, D., M. Bogli, M. Dalmonte, E. Rico, P. Stebler, U.-J. Wiese, and P. Zoller, 2013, Phys. Rev. Lett. 110, 125303.

Banerjee, D., M. Dalmonte, M. Müller, E. Rico, P. Stebler, U.-J. Wiese, and P. Zoller, 2012, Phys. Rev. Lett. 109, 175302.  
Barreiro, J. T., M. Mueller, P. Schindler, D. Nigg, T. Monz, M. Chwalla, M. Hennrich, C. F. Roos, P. Zoller, and R. Blatt, 2011, Nature (London) 470, 486.  
Barrett, S., K. Hammerer, S. Harrison, T.E. Northup, and T.J. Osborne, 2013, Phys. Rev. Lett. 110, 090501.  
Becker, C., P. Soltan-Panahi, J. Kronjager, S. Doscher, K. Bongs, and K. Sengstock, 2010, New J. Phys. 12, 065025.  
Benenti, G., and G. Strini, 2008, Am. J. Phys. 76, 657.  
Bennett, C. H., J. I. Cirac, M. S. Leifer, D. W. Leung, N. Linden, S. Popescu, and G. Vidal, 2002, Phys. Rev. A 66, 012305.  
Bermudez, A., J. Almeida, F. Schmidt-Kaler, A. Retzker, and M. B. Plenio, 2011, Phys. Rev. Lett. 107, 207209.  
Bermudez, A., M. Martin-Delgado, and D. Porras, 2010, New J. Phys. 12, 123016.  
Bermudez, A., M. A. Martin-Delgado, and E. Solano, 2007, Phys. Rev. A 76, 041801.  
Bermudez, A., D. Porras, and M. A. Martin-Delgado, 2009, Phys. Rev. A 79, 060303.  
Berry, D.W., G. Ahokas, R. Cleve, and B.C. Sanders, 2007, Commun. Math. Phys. 270, 359.  
Biamonte, J., V. Bergholm, J. Whitfield, J. Fitzsimons, and A. Aspuru-Guzik, 2011, AIP Adv. 1, 022126.  
Biercuk, M. J., H. Uys, A. Vandevender, N. Shiga, W. M. Itano, and J. J. Bollinger, 2009, Quantum Inf. Comput. 9, 920 [http://dl.acm.org/citation.cfm?id=2012100].  
Billy, J., V. Josse, Z. Zuo, A. Bernard, B. Hambrecht, P. Lugan, D. Clement, L. Sanchez-Palencia, P. Bouyer, and A. Aspect, 2008, Nature (London) 453, 891.  
Blatt, R., and C. F. Roos, 2012, Nat. Phys. 8, 277.  
Blatt, R., and D. Wineland, 2008, Nature (London) 453, 1008.  
Bliokh, K. Y., Y. P. Bliokh, V. Freilikher, S. Savel'ev, and F. Nori, 2008, Rev. Mod. Phys. 80, 1201.  
Bloch, I., J. Dalibard, and S. Nascimbene, 2012, Nat. Phys. 8, 267.  
Bloch, I., J. Dalibard, and W. Zwerger, 2008, Rev. Mod. Phys. 80, 885.  
Boghosian, B. M., and W. Taylor, 1998a, Phys. Rev. E 57, 54.  
Boghosian, B. M., and W. Taylor, 1998b, Physica (Amsterdam) 120D, 30.  
Bouyer, P., 2010, Rep. Prog. Phys. 73, 062401.  
Brandao, F. G. S. L., M. J. Hartmann, and M. B. Plenio, 2007, arXiv:quant-ph/0702003.  
Braun, D., 2010, Phys. Rev. A 82, 013617.  
Bravyi, S., D. P. DiVincenzo, D. Loss, and B. M. Terhal, 2008, Phys. Rev. Lett. 101, 070503.  
Bremner, M. J., D. Bacon, and M. A. Nielsen, 2005, Phys. Rev. A 71, 052312.  
Brennen, G., M. Aguado, and J. Cirac, 2009, New J. Phys. 11, 053009.  
Britton, J. W., B.C. Sawyer, A.C. Keith, C.C.J. Wang, J.K. Freericks, H. Uys, M. J. Biercuk, and J. J. Bollinger, 2012, Nature (London) 484, 489.  
Broome, M. A., A. Fedrizzi, S. Rahimi-Keshari, J. Dove, S. Aaronson, T. C. Ralph, and A. G. White, 2013, Science 339, 794.  
Brown, K. L., S. De, V. M. Kendon, and W. J. Munro, 2011, New J. Phys. 13, 095007.  
Brown, K. L., W. J. Munro, and V. M. Kendon, 2010, Entropy 12, 2268.  
Brown, K. R., 2007, Phys. Rev. A 76, 022327.  
Brown, K. R., R. J. Clark, and I. L. Chuang, 2006, Phys. Rev. Lett. 97, 050504.  
Büchler, H. P., M. Hermele, S. D. Huber, M. P. A. Fisher, and P. Zoller, 2005, Phys. Rev. Lett. 95, 040402.

Buluta, I., S. Ashhab, and F. Nori, 2011, Rep. Prog. Phys. 74, 104401.  
Buluta, I. M., M. Kitaoka, S. Georgescu, and S. Hasegawa, 2008, Phys. Rev. A 77, 062320.  
Buluta, I. M., and F. Nori, 2009, Science 326, 108.  
Byrnes, T., N. Y. Kim, K. Kusudo, and Y. Yamamoto, 2008, Phys. Rev. B 78, 075320.  
Byrnes, T., P. Recher, N. Y. Kim, S. Utsunomiya, and Y. Yamamoto, 2007, Phys. Rev. Lett. 99, 016405.  
Byrnes, T., and Y. Yamamoto, 2006, Phys. Rev. A 73, 022328.  
Cai, J. M., A. Retzker, F. Jelezko, and M. B. Plenio, 2013, Nat. Phys. 9, 168.  
Capogrosso-Sansone, B., C. Trefzger, M. Lewenstein, P. Zoller, and G. Pupillo, 2010, Phys. Rev. Lett. 104, 125301.  
Casanova, J., J. Garcia-Ripoll, R. Gerritsma, C. Roos, and E. Solano, 2010, Phys. Rev. A 82, 020101.  
Casanova, J., A. Mezzacapo, L. Lamata, and E. Solano, 2012, Phys. Rev. Lett. 108, 190502.  
Casanova, J., C. Sabin, J. Leon, I. L. Egusquiza, R. Gerritsma, C. F. Roos, J. J. Garcia-Ripoll, and E. Solano, 2011, Phys. Rev. X 1, 021018.  
Chen, G., Z. Chen, and J. Liang, 2007, Phys. Rev. A 76, 055803.  
Chen, G., D. Church, B.-G. Englert, C. Henkel, B. Rohwedder, M. Scully, and M. S. Zubairy, 2007, Quantum computing devices: principles, designs and analysis (Chapman and Hall, London).  
Chen, Z., Z. Zhou, X. Shou, X. Zhou, and G. Guo, 2010, Phys. Rev. A 81, 022303.  
Chiaverini, J., and W. E. Lybarger, 2008, Phys. Rev. A 77, 022324.  
Chiuri, A., C. Greganti, L. Mazzola, M. Paternostro, and P. Mataloni, 2012, Sci. Rep. 2, 968.  
Cho, J., D. G. Angelakis, and S. Bose, 2008a, Phys. Rev. A 78, 062338.  
Cho, J., D. G. Angelakis, and S. Bose, 2008b, Phys. Rev. Lett. 101, 246809.  
Cirac, J., P. Maraner, and J. Pachos, 2010, Phys. Rev. Lett. 105, 190403.  
Cirac, J. I., and F. Verstraete, 2009, J. Phys. A 42, 504004.  
Cirac, J. I., and P. Zoller, 2003, Science 301, 176.  
Clark, C. R., T. S. Metodi, S. D. Gasster, and K. R. Brown, 2009, Phys. Rev. A 79, 062314.  
Clark, R. J., T. Lin, K. R. Brown, and I. L. Chuang, 2009, J. Appl. Phys. 105, 013114.  
Clarke, J., and F. K. Wilhelm, 2008, Nature (London) 453, 1031.  
Crespi, A., R. Osellame, R. Ramponi, D.J. Brod, E.F. Galvao, N. Spagnolo, C. Vitelli, E. Maiorino, P. Mataloni, and F. Sciarrino, 2013, Nat. Photonics 7, 545.  
Cucchietti, F. M., S. Fernandez-Vidal, and J. P. Paz, 2007, Phys. Rev. A 75, 032337.  
Dalibard, J., F. Gerbier, G. Juzeliūnas, and P. Öhberg, 2011, Rev. Mod. Phys. 83, 1523.  
D'Ariano, G.M., M.G.A. Paris, and M.F. Sacchi, 2003, Adv. Imaging Electron Phys. 128, 205.  
Daskin, A., and S. Kais, 2011, J. Chem. Phys. 134, 144112.  
de Groot, P. C., J. Lisenfeld, R. N. Schouten, S. Ashhab, A. Lupascu, C. J. P. M. Harmans, and J. E. Mooij, 2010, Nat. Phys. 6, 763.  
de Raedt, K., K. Michielsen, H. de Raedt, B. Trieu, G. Arnold, M. R. T. Lippert, H. Watanabe, and N. Ito, 2007, Comput. Phys. Commun. 176, 121.  
Deng, X.-L., D. Porras, and J. I. Cirac, 2005, Phys. Rev. A 72, 063407.  
Deng, X.-L., D. Porras, and J. I. Cirac, 2008, Phys. Rev. A 77, 033403.  
Deppe, F., M. Mariantoni, E. P. Menzel, A. Marx, S. S. K. Kakuyanagi, H. Tanaka, T. Meno, K. Semba, H. T. E. Solano, and R. Gross, 2008, Nat. Phys. 4, 686.

Dodd, J. L., M. A. Nielsen, M. J. Bremner, and R. T. Thew, 2002, Phys. Rev. A 65, 040301.  
Dreisow, F., M. Heinrich, R. Keil, A. Tünnermann, S. Nolte, S. Longhi, and A. Szameit, 2010, Phys. Rev. Lett. 105, 143902.  
Du, J., N. Xu, X. Peng, P. Wang, S. Wu, and D. Lu, 2010, Phys. Rev. Lett. 104, 030502.  
Dür, W., M. J. Bremne, and H. J. Briegel, 2008, Phys. Rev. A 78, 052325.  
Edwards, E., S. Korenblit, K. Kim, R. Islam, M. Chang, J. Freericks, G. Lin, L. Duan, and C. Monroe, 2010, Phys. Rev. B 82, 060412.  
Fallani, L., J. E. Lye, V. Guarrera, C. Fort, and M. Inguscio, 2007, Phys. Rev. Lett. 98, 130404.  
Farhi, E., J. Goldstone, S. Gutmann, J. Lapan, A. Lundgren, and D. Preda, 2001, Science 292, 472.  
Fetter, A. L., and J. D. Walecka, 2003, Quantum theory of many-particle systems (Dover Publications, New York).  
Feynman, R., 1982, Int. J. Theor. Phys. 21, 467.  
Fischer, U. R., and R. Schützhold, 2004, Phys. Rev. A 70, 063615.  
Fisher, M. P. A., P. B. Weichman, G. Grinstein, and D. S. Fisher, 1989, Phys. Rev. B 40, 546.  
Freedman, M., A. Kitaev, and Z. Wang, 2002, Commun. Math. Phys. 227, 587.  
Friedenauer, A., H. Schmitz, J. T. Glickert, D. Porras, and T. Schatz, 2008, Nat. Phys. 4, 757.  
Fuhrmanek, A., R. Bourgain, Y.R.P. Sortais, and A. Browaeys, 2011, Phys. Rev. Lett. 106, 133003.  
Garcia-Ripoll, J. J., M. A. Martin-Delgado, and J. I. Cirac, 2004, Phys. Rev. Lett. 93, 250405.  
Garcia-Ripoll, J. J., E. Solano, and M. A. Martin-Delgado, 2008, Phys. Rev. B 77, 024522.  
Geller, M. R., J. M. Martinis, A. T. Sornborger, P. C. Stancil, E. J. Pritchett, and A. Galiautdinov, 2012, arXiv:1210.5260.  
Georgeot, B., 2004, Phys. Rev. A 69, 032301.  
Georgescu, I. M., S. Ashhab, T. Nakatsukasa, and F. Nori, 2011 (unpublished).  
Gerace, D., and I. Carusotto, 2012, Phys. Rev. B 86, 144505.  
Gerritsma, R., G. Kirchmair, F. Zahringer, E. Solano, R. Blatt, and C. Roos, 2010, Nature (London) 463, 68.  
Gerritsma, R., B. P. Lanyon, G. Kirchmair, F. Zähringer, C. Hempel, J. Casanova, J. J. García-Ripoll, E. Solano, R. Blatt, and C. F. Roos, 2011, Phys. Rev. Lett. 106, 060503.  
Ghosh, P., A. Smirnov, and F. Nori, 2009, J. Chem. Phys. 131, 035102.  
Ghosh, P., A. Smirnov, and F. Nori, 2011a, Phys. Rev. E 84, 061138.  
Ghosh, P., A. Smirnov, and F. Nori, 2011b, J. Chem. Phys. 134, 244103.  
Gibbons, M. J., C. D. Hamley, C.-Y. Shih, and M. S. Chapman, 2011, Phys. Rev. Lett. 106, 133002.  
Gibertini, M., A. Singha, V. Pellegrini, M. Polini, G. Vignale, A. Pinczuk, L. N. Pfeiffer, and K. W. West, 2009, Phys. Rev. B 79, 241406.  
Giorgi, G., S. Paganelli, and F. Galve, 2010, Phys. Rev. A 81, 052118.  
Giovanazzi, S., 2005, Phys. Rev. Lett. 94, 061302.  
Goldman, N., A. Kubasiak, A. Bermudez, P. Gaspard, M. Lewenstein, and M. Martin-Delgado, 2009, Phys. Rev. Lett. 103, 035301.  
Grajcar, M., S. H. W. van der Ploeg, A. Izmalkov, E. Il'ichev, H.-G. Meyer, A. Fedorov, A. Shnirman, and G. Schon, 2008, Nat. Phys. 4, 612.  
Greentree, A. D., C. Tahan, J. H. Cole, and L. C. L. Hollenberg, 2006, Nat. Phys. 2, 856.  
Greiner, M., and S. Fölling, 2008, Nature (London) 453, 736.  
Greiner, M., O. Mandel, T. Esslinger, T. W. Hänsch, and I. Bloch, 2002, Nature (London) 415, 39.

Gustavsson, S., J. Bylander, and W. D. Oliver, 2013, Phys. Rev. Lett. 110, 016603.  
Han, Y.-J., R. Raussendorf, and L.-M. Duan, 2007, Phys. Rev. Lett. 98, 150404.  
Hanggi, P., and F. Marchesoni, 2009, Rev. Mod. Phys. 81, 387.  
Hanggi, P., F. Marchesoni, and F. Nori, 2005, Ann. Phys. (Berlin) 14, 51.  
Hanneke, D., J. P. Home, J. D. Jost, J. M. Amini, D. Leibfried, and D. J. Wineland, 2009, Nat. Phys. 6, 13.  
Hanson, R., and D. D. Awschalom, 2008, Nature (London) 453, 1043.  
Harrabi, K., F. Yoshihara, A. O. Niskanen, Y. Nakamura, and J. S. Tsai, 2009, Phys. Rev. B 79, 020507.  
Harris, R., 2012 (private communication).  
Harris, R. et al., 2010, Phys. Rev. B 82, 024511.  
Hartmann, M. J., F. G. S. L. Brandao, and M. B. Plenio, 2006, Nat. Phys. 2, 849.  
Hastings, M. B., 2006, Phys. Rev. B 73, 085115.  
Hauke, P., F.M. Cucchietti, L. Tagliacozzo, I. Deutsch, and M. Lewenstein, 2012, Rep. Prog. Phys. 75, 082401.  
Hauke, P., D. Marcos, M. Dalmonte, and P. Zoller, 2013, Phys. Rev. X 3, 041018.  
Herrera, F., and R. V. Krems, 2011, Phys. Rev. A 84, 051401.  
Herrera, F., K. W. Madison, R. V. Krems, and M. Berciu, 2013, Phys. Rev. Lett. 110, 223002.  
Hilbert, M., and P. Lopez, 2011, Science 332, 60.  
Ho, A. F., M. A. Cazalilla, and T. Giamarchi, 2009, Phys. Rev. A 79, 033620.  
Horstmann, B., B. Reznik, S. Fagnocchi, and J. I. Cirac, 2010, Phys. Rev. Lett. 104, 250403.  
Hou, J.-M., W.-X. Yang, and X.-J. Liu, 2009, Phys. Rev. A 79, 043621.  
Houck, A. A., H. E. Tureci, and J. Koch, 2012, Nat. Phys. 8, 292.  
Howell, J. C., and J. A. Yeaze, 1999, Phys. Rev. A 61, 012304.  
Hu, Y.-M., M. Feng, and C. Lee, 2012, Phys. Rev. A 85, 043604.  
Ian, H., Y.-X. Liu, and F. Nori, 2010, Phys. Rev. A 81, 063823.  
Islam, R., et al., 2011, Nat. Commun. 2, 377.  
Ivanov, P. A., S. S. Ivanov, N. V. Vitanov, A. Mering, M. Fleischhauer, and K. Singer, 2009, Phys. Rev. A 80, 060301.  
Ivanov, P. A., and F. Schmidt-Kaler, 2011, New J. Phys. 13, 125008.  
Jaksch, D., C. Bruder, J. I. Cirac, C. W. Gardiner, and P. Zoller, 1998, Phys. Rev. Lett. 81, 3108.  
Jaksch, D., and P. Zoller, 2005, Ann. Phys. (N.Y.) 315, 52.  
Jané, E., G. Vidal, W. Dür, P. Zoller, and J. Cirac, 2003, Quantum Inf. Comput. 3, 15.  
Jo, G.-B., Y.-R. Lee, J.-H. Choi, C. A. Christensen, T. H. Kim, J. H. Thywissen, D. E. Pritchard, and W. Ketterle, 2009, Science 325, 1521.  
Johanning, M., A. Varon, and C. Wunderlich, 2009, J. Phys. B 42, 154009.  
Johansson, J.R., G. Johansson, C.M. Wilson, and F. Nori, 2010, Phys. Rev. A 82, 052509.  
Jordan, S. P., K. S. M. Lee, and J. Preskill, 2012, Science 336, 1130.  
Kapit, E., and E. Mueller, 2011, Phys. Rev. A 83, 033625.  
Kassal, I., S.P. Jordan, P.J. Love, M. Mohseni, and A. Aspuru-Guzik, 2008, Proc. Natl. Acad. Sci. U.S.A. 105, 18681.  
Kassal, I., J.D. Whitfield, A. Perdomo-Ortiz, M.-H. Yung, and A. Aspuru-Guzik, 2011, Annu. Rev. Phys. Chem. 62, 185.  
Katsnelson, M. I., K. S. Novoselov, and A. K. Geim, 2006, Nat. Phys. 2, 620.  
Kay, A., and D. Angelakis, 2008, Europhys. Lett. 84, 20001.

Kay, A., J. K. Pachos, and C. S. Adams, 2006, Phys. Rev. A 73, 022310.  
Kimble, H. J., 2008, Nature (London) 453, 1023.  
Kim, K., M.-S. Chang, S. Korenblit, R. Islam, E. E. Edwards, J. K. Freericks, G.-D. Lin, L.-M. Duan, and C. Monroe, 2010, Nature (London) 465, 590.  
Kim, K., et al., 2011, New J. Phys. 13, 105003.  
Kitaev, A., 2003, Ann. Phys. (N.Y.) 303, 2.  
Kitagawa, T., 2012, Quantum Inf. Process. 11, 1107.  
Koch, J., A. A. Houck, K. L. Hur, and S. M. Girvin, 2010, Phys. Rev. A 82, 043811.  
Korenblit, S., et al., 2012, New J. Phys. 14, 095024.  
Kraus, C. V., M. M. Wolf, and J. I. Cirac, 2007, Phys. Rev. A 75, 022303.  
Ladd, T. D., F. Jelezko, R. Laflamme, Y. Nakamura, C. Monroe, and J. L. O'Brien, 2010, Nature (London) 464, 45.  
Lähteenmäki, P., G. S. Paraoanu, J. Hassel, and P. J. Hakonen, 2013, Proc. Natl. Acad. Sci. U.S.A. 110, 4234.  
Lamata, L., J. León, T. Schatz, and E. Solano, 2007, Phys. Rev. Lett. 98, 253005.  
Lanyon, B.P., et al., 2010, Nat. Chem. 2, 106.  
Lanyon, B.P. et al., 2011, Science 334, 57.  
Lau, H.-K., and D. F. V. James, 2012, Phys. Rev. A 85, 062329.  
Leibfried, D., et al., 2002, Phys. Rev. Lett. 89, 247901.  
Lemeshko, M., N. Y. Yao, A. V. Gorshkov, H. Weimer, S. D. Bennett, T. Momose, and S. Gopalakrishnan, 2013, Phys. Rev. B 88, 014426.  
Levi, B., and B. Georgeot, 2004, Phys. Rev. E 70, 056218.  
Lewenstein, M., 2006, Nat. Phys. 2, 309.  
Lewenstein, M., A. Sanpera, V. Ahufinger, B. Damski, A. Sen(De), and U. Sen, 2007, Adv. Phys. 56, 243.  
Li, J., et al., 2013, Nat. Commun. 4, 1420.  
Li, Z., M.-H. Yung, H. Chen, D. Lu, J.D. Whitfield, X. Peng, A. Aspuru-Guzik, and J. Du, 2011, Sci. Rep. 1, 88.  
Liao, J. Q., Z. R. Gong, L. Zhou, Y. X. Liu, C. P. Sun, and F. Nori, 2010, Phys. Rev. A 81, 042304.  
Lidar, D., and H. Wang, 1999, Phys. Rev. E 59, 2429.  
Lidar, D. A., 2004, New J. Phys. 6, 167.  
Lidar, D. A., and O. Biham, 1997, Phys. Rev. E 56, 3661.  
Lin, G.-D., C. Monroe, and L.-M. Duan, 2011, Phys. Rev. Lett. 106, 230402.  
Lin, G.-D., S.-L. Zhu, R. Islam, C. Monroe, and L.-M. Duan, 2009, Europhys. Lett. 86, 60004.  
Lin, Y., K. Jiménez-García, and I. B. Spielman, 2011, Nature (London) 471, 83.  
Liu, G., S. Zhu, S. Jiang, F. Sun, and W. M. Liu, 2010, Phys. Rev. A 82, 053605.  
Liu, Y.-X., J. Q. You, L. F. Wei, C. P. Sun, and F. Nori, 2005, Phys. Rev. Lett. 95, 087001.  
Lloyd, S., 1996, Science 273, 1073.  
Lu, C.-Y., W.-B. Gao, O. Gühne, X.-Q. Zhou, Z.-B. Chen, and J.-W. Pan, 2009, Phys. Rev. Lett. 102, 030502.  
Lu, D., N. Xu, R. Xu, H. Chen, J. Gong, X. Peng, and J. Du, 2011, Phys. Rev. Lett. 107, 020501.  
Lu, D., B. Xu, N. Xu, Z. Li, H. Chen, X. Peng, R. Xu, and J. Du, 2012, Phys. Chem. Chem. Phys. 14, 9411.  
Lütkenhaus, N., J. I. Cirac, and P. Zoller, 1998, Phys. Rev. A 57, 548.  
Ma, X., B. Dakic, W. Naylor, A. Zeilinger, and P. Walther, 2011, Nat. Phys. 7, 399.  
Ma, X., S. Dakic, B. Kropatsche, W. Naylor, Y. Chan, Z. Gong, L. Duan, A. Zeilinger, and P. Walther, 2012, arXiv:1205.2801.  
Manin, Y., 1980, Computable and Uncomputable (Sovetskoye Radio Press, Moscow) (in Russian).

Maniscalco, S., J. Piilo, F. Intravaia, F. Petruccione, and A. Messina, 2004, Phys. Rev. A 69, 052101.  
Manousakis, E., 2002, J. Low Temp. Phys. 126, 1501.  
Marcos, D., P. Rabl, E. Rico, and P. Zoller, 2013, Phys. Rev. Lett. 111, 110504.  
Mariantoni, M. et al., 2011, Science 334, 61.  
Maruyama, K., F. Nori, and V. Vedral, 2009, Rev. Mod. Phys. 81, 1.  
Marzuoli, A., and M. Rasetti, 2002, Phys. Lett. A 306, 79.  
Mazza, L., A. Bermudez, N. Goldman, M. Rizzi, M. A. Martin-Delgado, and M. Lewenstein, 2012, New J. Phys. 14, 015007.  
McKague, M., M. Mosca, and N. Gisin, 2009, Phys. Rev. Lett. 102, 020505.  
Mei, F., V. M. Stojanovic, I. Siddiqi, and L. Tian, 2013, Phys. Rev. B 88, 224502.  
Menicucci, N., S. Olson, and G. Milburn, 2010, New J. Phys. 12, 095019.  
Meyer, D., 2002, Phil. Trans. R. Soc. A 360, 395.  
Mezzacapo, A., J. Casanova, L. Lamata, and E. Solano, 2012, Phys. Rev. Lett. 109, 200501.  
Micheli, A., G. K. Brennen, and P. Zoller, 2006, Nat. Phys. 2, 341.  
Milburn, G., 1999, arXiv:quant-ph/9908037.  
Montangero, S., 2004, Phys. Rev. A 70, 032311.  
Mostame, S., and R. Schützhold, 2008, Phys. Rev. Lett. 101, 220501.  
Nation, P. D., M. P. Blencowe, A. J. Rimberg, and E. Buks, 2009, Phys. Rev. Lett. 103, 087004.  
Nation, P. D., J. R. Johansson, M. P. Blencowe, and F. Nori, 2012, Rev. Mod. Phys. 84, 1.  
Neeley, M., et al., 2009, Science 325, 722.  
Negrevergne, C., R. Somma, G. Ortiz, E. Knill, and R. Laflamme, 2005, Phys. Rev. A 71, 032344.  
Nelson, K. D., X. Li, and D. S. Weiss, 2007, Nat. Phys. 3, 556.  
Nielsen, M. A., M. J. Bremner, J. L. Dodd, A. M. Childs, and C. M. Dawson, 2002, Phys. Rev. A 66, 022317.  
Nielsen, M. A., and I. L. Chuang, 2000, Quantum computation and quantum information (Cambridge University Press, Cambridge, England).  
Noh, C., B. M. Rodriguez-Lara, and D. Angelakis, 2012, New J. Phys. 14, 033028.  
Nori, F., 2008, Nat. Phys. 4, 589.  
Nori, F., 2009, Science 325, 689.  
O'Hara, K., S. Hemmer, M. Gehm, S. Granade, and J. Thomas, 2002, Science 298, 2179.  
Orenstein, J., and A. J. Millis, 2000, Science 288, 468.  
Ortiz, G., J. E. Gubernatis, E. Knill, and R. Laflamme, 2001, Phys. Rev. A 64, 022319.  
Ortiz, G., J.E. Gubernatis, E. Knill, and R. Laflamme, 2002, Comput. Phys. Commun. 146, 302.  
Ortner, M., A. Micheli, G. Pupillo, and P. Zoller, 2009, New J. Phys. 11, 055045.  
Ospelkaus, C., U. Warring, Y. Colombe, K. R. Brown, J. M. Amini, D. Leibfried, and D. J. Wineland, 2011, Nature (London) 476, 181.  
Paredes, B., A. Widera, V. Murg, O. Mandel, S. Fölling, I. Cirac, G. Shlyapnikov, T. Hänsch, and I. Bloch, 2004, Nature (London) 429, 277.  
Pedernales, J. S., R. D. Candia, D. Ballester, and E. Solano, 2013, New J. Phys. 15, 055008.  
Peng, X., J. Du, and D. Suter, 2005, Phys. Rev. A 71, 012307.  
Peng, X., and D. Suter, 2010, Front. Phys. China 5, 1.  
Peng, X., J. Zhang, J. Du, and D. Suter, 2009, Phys. Rev. Lett. 103, 140501.  
Philbin, T.G., C. Kuklewicz, S. Robertson, S. Hill, F. Konig, and U. Leonhardt, 2008, Science 319, 1367.  
Piilo, J., and S. Maniscalco, 2006, Phys. Rev. A 74, 032303.

Pollet, L., J. D. Picon, H. P. Buchler, and M. Troyer, 2010, Phys. Rev. Lett. 104, 125302.  
Porras, D., and J. Cirac, 2004a, Phys. Rev. Lett. 93, 263602.  
Porras, D., and J. I. Cirac, 2004b, Phys. Rev. Lett. 92, 207901.  
Porras, D., and J. Cirac, 2005a, Laser Phys. 15, 88.  
Porras, D., and J. I. Cirac, 2005b, Proc. SPIE Int. Soc. Opt. Eng. 5833, 127.  
Porras, D., and J. I. Cirac, 2006a, Found. Phys. 36, 465.  
Porras, D., and J. I. Cirac, 2006b, Phys. Rev. Lett. 96, 250501.  
Porras, D., F. Marquardt, J. von Delft, and J. I. Cirac, 2008, Phys. Rev. A 78, 010101.  
Poulin, D., A. Qarry, R. Somma, and F. Verstraete, 2011, Phys. Rev. Lett. 106, 170501.  
Pupillo, G., A. Micheli, H. Buchler, and P. Zoller, 2009, Condensed Matter Physics with Cold Polar Molecules, Cold Molecules: Theory, Experiment, Applications (CRC Press, Boca Raton, FL).  
Quan, H. T., Y. X. Liu, C. P. Sun, and F. Nori, 2007, Phys. Rev. E 76, 031105.  
Quan, H. T., Y. D. Wang, Y. X. Liu, C. P. Sun, and F. Nori, 2006, Phys. Rev. Lett. 97, 180402.  
Raeisi, S., N. Wiebe, and B.C. Sanders, 2012, New J. Phys. 14, 103017.  
Rakhmanov, A. L., V. A. Yampol'skii, J. A. Fan, F. Capasso, and F. Nori, 2010, Phys. Rev. B 81, 075101.  
Rakhmanov, A. L., A. M. Zagoskin, S. Savel'ev, and F. Nori, 2008, Phys. Rev. B 77, 144507.  
Raussendorf, R., D. E. Browne, and H. J. Briegel, 2003, Phys. Rev. A 68, 022312.  
Regal, C. A., M. Greiner, and D. S. Jin, 2004, Phys. Rev. Lett. 92, 040403.  
Retzker, A., R. C. Thompson, D. M. Segal, and M. B. Plenio, 2008, Phys. Rev. Lett. 101, 260504.  
Roati, G., C. D'Errico, L. Fallani, M. Fattori, C. Fort, M. Zaccanti, G. Modugno, M. Modugno, and M. Inguscio, 2008, Nature (London) 453, 895.  
Roumpos, G., C. P. Master, and Y. Yamamoto, 2007, Phys. Rev. B 75, 094415.  
Rusin, T. M., and W. Zawadzki, 2010, Phys. Rev. D 82, 125031.  
Sanpera, A., A. Kantian, L. Sanchez-Palencia, J. Zakrzewski, and M. Lewenstein, 2004, Phys. Rev. Lett. 93, 040401.  
Santini, P., S. Carretta, F. Troiani, and G. Amoretti, 2011, Phys. Rev. Lett. 107, 230502.  
Schack, R., 1998, Phys. Rev. A 57, 1634.  
Schatz, T., A. Friedenauer, H. Schmitz, L. Petersen, and S. Kahra, 2007, J. Mod. Opt. 54, 2317.  
Schatz, T., D. Leibfried, J. Chiaverini, M. Barrett, J. Britton, B. Demarco, W. Itano, J. Jost, C. Langer, and D. Wineland, 2004, Appl. Phys. B 79, 979.  
Schleich, W. P., and H. Walther, 2008, Eds., Elements of Quantum Information (Wiley-VCH, Weinheim).  
Schmied, R., D. Leibfried, R. Spreeuw, and S. Whitlock, 2010, New J. Phys. 12, 103029.  
Schmied, R., T. Roscilde, V. Murg, D. Porras, and J. I. Cirac, 2008, New J. Phys. 10, 045017.  
Schmied, R., J. H. Wesenberg, and D. Leibfried, 2009, Phys. Rev. Lett. 102, 233002.  
Schmied, R., J. H. Wesenberg, and D. Leibfried, 2011, New J. Phys. 13, 115011.  
Schneider, C., D. Porras, and T. Schaetz, 2012, Rep. Prog. Phys. 75, 024401.  
Schneider, S., and G. Milburn, 2001, arXiv:quant-ph/0112042.  
Schoelkopf, R. J., and S. M. Girvin, 2008, Nature (London) 451, 664.

Schulte, T., S. Drenkelforth, J. Kruse, W. Ertmer, J. Arlt, K. Sacha, J. Zakrzewski, and M. Lewenstein, 2005, Phys. Rev. Lett. 95, 170411.  
Schützhold, R., and S. Mostame, 2005, JETP Lett. 82, 248.  
Schützhold, R., M. Uhlmann, L. Petersen, H. Schmitz, A. Friedenauer, and T. Schatz, 2007, Phys. Rev. Lett. 99, 201301.  
Semiao, F. L., and M. Paternostro, 2012, Quantum Inf. Process. 11, 67.  
Sherson, J. F., C. Weitenberg, M. Endres, M. Cheneau, I. Bloch, and S. Kuhr, 2010, Nature (London) 467, 68.  
Shevchenko, S., S. Ashhab, and F. Nori, 2010, Phys. Rep. 492, 1.  
Simon, J., W. S. Bakr, R. Ma, M. E. Tai, P. M. Preiss, and M. Greiner, 2011, Nature (London) 472, 307.  
Singha,A.,et al.,2011,Science 332,1176.  
Sinha, S., and P. Russer, 2010, Quantum Inf. Process. 9, 385.  
Smirnov, A., S. Savel'ev, L. Mourokh, and F. Nori, 2007, Europhys. Lett. 80, 67008.  
Somaroo, S., C. H. Tseng, T. F. Havel, R. Laflamme, and D. G. Cory, 1999, Phys. Rev. Lett. 82, 5381.  
Somma, R., G. Ortiz, J. E. Gubernatis, E. Knill, and R. Laflamme, 2002, Phys. Rev. A 65, 042323.  
Somma, R., G. Ortiz, E. Knill, and J. Gubernatis, 2003, Proc. SPIE Int. Soc. Opt. Eng. 5105, 96.  
Spring, J. B. et al., 2013, Science 339, 798.  
Stanescu, T.D., V. Galitski, J. Vaishnav, C.W. Clark, and S.D. Sarma, 2009, Phys. Rev. A 79, 053639.  
Stannigel, K., P. Hauke, D. Marcos, M. Hafezi, S. Diehl, M. Dalmonte, and P. Zoller, 2013, arXiv:1308.0528.  
Stojanovic, V. M., T. Shi, C. Bruder, and J. I. Cirac, 2012, Phys. Rev. Lett. 109, 250501.  
Stolze, J., and D. Suter, 2008, Quantum Computing (Wiley-VCH, Weinheim).  
Strini, G., 2002, Fortschr. Phys. 50, 171.  
Struck, J., C. Olschlager, R. L. Targat, P. Soltan-Panahi, A. Eckardt, M. Lewenstein, P. Windpassinger, and K. Sengstock, 2011, Science 333, 996.  
Suzuki, M., 1993, Ed., Quantum Monte Carlo Methods in Condensed Matter Physics (World Scientific, Singapore).  
Szpak, N., and R. Schützhold, 2011, Phys. Rev. A 84, 050101.  
Szpak, N., and R. Schützhold, 2012, New J. Phys. 14, 035001.  
Tagliacozzo, L., A. Celi, P. Orland, and M. Lewenstein, 2013, Nat. Commun. 4, 2615.  
Tagliacozzo, L., A. Celi, A. Zamora, and M. Lewenstein, 2013, Ann. Phys. (N.Y.) 330, 160.  
Taylor, J. M., and T. Calarco, 2008, Phys. Rev. A 78, 062331.  
Temme, K., T.J. Osborne, K.G. Vollbrecht, D. Poulin, and F. Verstraete, 2011, Nature (London) 471, 87.  
Terhal, B. M., and D. P. DiVincenzo, 2000, Phys. Rev. A 61, 022301.  
Terraneo, M., B. Georgeot, and D. L. Shepelyansky, 2003, Eur. Phys. J. D 22, 127.  
Tewari, S., V. Scarola, T. Senthil, and S. D. Sarma, 2006, Phys. Rev. Lett. 97, 200401.  
Thouless, D.J., 1972, The Quantum Mechanics of Many-Body Systems (Academic Press, New York).  
Tillmann, M., B. Dakić, R. Heilmann, S. Nolte, A. Szameit, and P. Walther, 2013, Nat. Photonics 7, 540.  
Timoney, N., I. Baumgart, M. Johanning, A.F. Varon, M.B. Plenio, A. Retzker, and C. Wunderlich, 2011, Nature (London) 476, 185.  
Torrontegui, E., A. Ruschhaupt, D. Gury-Odelin, and J. G. Muga, 2011, J. Phys. B 44, 195302.  
Troyer, M., and U.-J. Wiese, 2005, Phys. Rev. Lett. 94, 170201.

Tseng, C. H., S. Somaroo, Y. Sharf, E. Knill, R. Laflamme, T. F. Havel, and D. G. Cory, 2000, Phys. Rev. A 62, 032309.  
Tsokomos, D., S. Ashhab, and F. Nori, 2010, Phys. Rev. A 82, 052311.  
Tsomokos, D. I., S. Ashhab, and F. Nori, 2008, New J. Phys. 10, 113020.  
Uehlinger, T., G. Jotzu, M. Messer, D. Greif, W. Hofstetter, U. Bissbort, and T. Esslinger, 2013, Phys. Rev. Lett. 111, 185307.  
van Oudenaarden, A., and J. E. Mooij, 1996, Phys. Rev. Lett. 76, 4947.  
Verstraete, F., and J. I. Cirac, 2004, arXiv:cond-mat/0407066v1.  
Verstraete, F., J. I. Cirac, and J. I. Latorre, 2009, Phys. Rev. A 79, 032316.  
Verstraete, F., V. Murg, and J. I. Cirac, 2008, Adv. Phys. 57, 143.  
Verstraete, F., D. Porras, and J. I. Cirac, 2004, Phys. Rev. Lett. 93, 227205.  
Vidal, G., 2008, Phys. Rev. Lett. 101, 110501.  
Vollbrecht, K.G., and J.I. Cirac, 2008, Phys. Rev. Lett. 100, 010501.  
Vollbrecht, K. G. H., and J. I. Cirac, 2009, Phys. Rev. A 79, 042305.  
Volovik, G. E., 2009, The Universe in a Helium Droplet (Oxford University Press, New York).  
Wallraff, A., D. I. Schuster, A. Blais, L. Frunzio, R.-S. Huang, J. Majer, S. Kumar, S. M. Girvin, and R. J. Schoelkopf, 2004, Nature (London) 431, 162.  
Wang, A. M., and X. Yang, 2006, Phys. Lett. A 352, 304.  
Wang, H., S. Ashhab, and F. Nori, 2009, Phys. Rev. A 79, 042335.  
Wang, H., S. Ashhab, and F. Nori, 2011, Phys. Rev. A 83, 062317.  
Wang, H., S. Kais, A. Aspuru-Guzik, and M. R. Hoffmann, 2008, Phys. Chem. Chem. Phys. 10, 5388.  
Wang, H., L.-A. Wu, Y.-X. Liu, and F. Nori, 2010, Phys. Rev. A 82, 062303.  
Wang, K., T. Liu, M. Feng, W. Yang, and K. Wang, 2010, Phys. Rev. A 82, 064501.  
Wang, X., and P. Zanardi, 2002, Phys. Rev. A 65, 032327.  
Ward, N. J., I. Kassal, and A. Aspuru-Guzik, 2009, J. Chem. Phys. 130, 194105.  
Wei, H., and X. Xue, 1997, arXiv:quant-ph/9702050.  
Weimer, H., M. Müller, H.P. Buchler, and I. Lesanovsky, 2011, Quantum Inf. Process. 10, 885.  
Weimer, H., M. Müller, I. Lesanovsky, P. Zoller, and H. Buchler, 2010, Nat. Phys. 6, 382.  
Weimer, H., N. Y. Yao, and M. D. Lukin, 2013, Phys. Rev. Lett. 110, 067601.  
Weinfurtner, S., E. Tedford, M. Penrice, W. Unruh, and G. Lawrence, 2011, Phys. Rev. Lett. 106, 021302.  
Weinstein, Y.S., S. Lloyd, J.V. Emerson, and D.G. Cory, 2002, Phys. Rev. Lett. 89, 157902.  
Weitenberg, C., M. Endres, J. F. Sherson, M. Cheneau, P. Schauss, T. Fukuhara, I. Bloch, and S. Kuhr, 2011, Nature (London) 471, 319.  
Whitfield, J. D., J. Biamonte, and A. Aspuru-Guzik, 2011, Quantum Inf. Process. 10, 885.  
Wiebe, N., D. W. Berry, P. Hoyer, and B. C. Sanders, 2011, J. Phys. A 44, 445308.  
Wiese,U.-J.,2013,arXiv:1305.1602.  
Wiesner, S., 1996, arXiv:quant-ph/9603028.  
Wilson, C., G. Johansson, A. Pourkabirian, J. Johansson, T. Duty, F. Nori, and P. Delsing, 2011, Nature (London) 479, 376.  
Wineland, D., C. Monroe, W. Itano, B. King, D. Leibfried, C. Myatt, and C. Wood, 1998, Phys. Scr. T76, 147.

Withthaut, D., 2010, Phys. Rev. A 82, 033602.  
Wocjan, P., D. Janzing, and T. Beth, 2002, Quantum Inf. Comput. 2, 117.  
Wocjan, P., M. Rotteler, D. Janzing, and T. Beth, 2002a, Phys. Rev. A 65, 042309.  
Wocjan, P., M. Rotteler, D. Janzing, and T. Beth, 2002b, Quantum Inf. Comput. 2, 133.  
Wu, L.-A., M. Byrd, and D. Lidar, 2002, Phys. Rev. Lett. 89, 057904.  
Wunderlich, H. W. C., 2009, Phys. Rev. A 79, 052324.  
Würtz, P., T. Langen, T. Gericke, A. Koglbauer, and H. Ott, 2009, Phys. Rev. Lett. 103, 080404.  
Xue, Z.-Y., 2011, Europhys. Lett. 93, 20007.  
Yamaguchi, F., and Y. Yamamoto, 2002, Superlattices Microstruct. 32, 343.  
Yang, X., A. M. Wang, F. Xu, and J. Du, 2006, Chem. Phys. Lett. 422, 20.  
You, H., M. R. Geller, and P. C. Stancil, 2013, Phys. Rev. A 87, 032341.  
You, J. Q., Y. X. Liu, C. P. Sun, and F. Nori, 2007, Phys. Rev. B 75, 104516.  
You, J. Q., and F. Nori, 2003, Phys. Rev. B 68, 064509.  
You, J. Q., and F. Nori, 2005, Phys. Today 58, No. 11, 42.  
You, J. Q., and F. Nori, 2011, Nature (London) 474, 589.  
You, J. Q., X.-F. Shi, X. Hu, and F. Nori, 2010, Phys. Rev. B 81, 014505.  
You, J.Q., Z.D. Wang, W. Zhang, and F. Nori, 2011, arXiv:1108.3712.  
Yung, M.-H., D. Nagaj, J. D. Whitfield, and A. Aspuru-Guzik, 2010, Phys. Rev. A 82, 060302.  
Zagoskin, A., S. Savel'ev, and F. Nori, 2007, Phys. Rev. Lett. 98, 120503.  
Zagoskin, A. M., 1998, Quantum Theory of Many-Body Systems: Techniques and Applications (Springer, New York).  
Zalka, C., 1998a, Fortschr. Phys. 46, 877.  
Zalka, C., 1998b, Proc. R. Soc. A 454, 313.  
Zhang, J., F. M. Cucchietti, C. M. Chandrashekar, M. Laforest, C. A. Ryan, M. Ditty, A. Hubbard, J. K. Gamble, and R. Laflamme, 2009, Phys. Rev. A 79, 012305.  
Zhang, J., X. Peng, N. Rajendran, and D. Suter, 2008, Phys. Rev. Lett. 100, 100501.  
Zhang, J., M.H. Yung, R. Laflamme, A. Aspuru-Guzik, and J. Baugh, 2012, Nat. Commun. 3, 880.  
Zhou, L., H. Dong, Y.-X. Liu, C. P. Sun, and F. Nori, 2008, Phys. Rev. A 78, 063827.  
Zhou, L., Z. R. Gong, Y.-X. Liu, C. P. Sun, and F. Nori, 2008, Phys. Rev. Lett. 101, 100501.  
Zinner, N. T., and A. S. Jensen, 2008, J. Phys. Conf. Ser. 111, 012016.  
Zinner, N. T., and A. S. Jensen, 2013, J. Phys. G 40, 053101.  
Zohar, E., J. I. Cirac, and B. Reznik, 2012, Phys. Rev. Lett. 109, 125302.  
Zohar, E., J. I. Cirac, and B. Reznik, 2013, Phys. Rev. Lett. 110, 125304.  
Zueco, D., F. Galve, S. Kohler, and P. Hanggi, 2009, Phys. Rev. A 80, 042303.  
Zwierlein, M. W., J. R. Abo-Shaeer, A. Schirotzek, C. H. Schunck, and W. Ketterle, 2005, Nature (London) 435, 1047.