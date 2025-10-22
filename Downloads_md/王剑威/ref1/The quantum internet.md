# The quantum internet

H. J. Kimble

Quantum networks provide opportunities and challenges across a range of intellectual and technical frontiers, including quantum computation, communication and metrology. The realization of quantum networks composed of many nodes and channels requires new scientific capabilities for generating and characterizing quantum coherence and entanglement. Fundamental to this endeavour are quantum interconnects, which convert quantum states from one physical system to those of another in a reversible manner. Such quantum connectivity in networks can be achieved by the optical interactions of single photons and atoms, allowing the distribution of entanglement across the network and the teleportation of quantum states between nodes.

In the past two decades, a broad range of fundamental discoveries have been made in the field of quantum information science, from a quantum algorithm that places public-key cryptography at risk to a protocol for the teleportation of quantum states<sup>1</sup>. This union of quantum mechanics and information science has allowed great advances in the understanding of the quantum world and in the ability to control coherently individual quantum systems<sup>2</sup>. Unique ways in which quantum systems process and distribute information have been identified, and powerful new perspectives for understanding the complexity and subtleties of quantum dynamical phenomena have emerged.

In the broad context of quantum information science, quantum networks have an important role, both for the formal analysis and the physical implementation of quantum computing, communication and metrology $^{2-5}$ . A notional quantum network based on proposals in refs 4, 6 is shown in Fig. 1a. Quantum information is generated, processed and stored locally in quantum nodes. These nodes are linked by quantum channels, which transport quantum states from site to site with high fidelity and distribute entanglement across the entire network. As an extension of this idea, a 'quantum internet' can be envisaged; with only moderate processing capabilities, such an internet could accomplish tasks that are impossible in the realm of classical physics, including the distribution of 'quantum software'.

Apart from the advantages that might be gained from a particular algorithm, there is an important advantage in using quantum connectivity, as opposed to classical connectivity, between nodes. A network of quantum nodes that is linked by classical channels and comprises  $k$  nodes each with  $n$  quantum bits (qubits) has a state space of dimension  $k2^n$ , whereas a fully quantum network has an exponentially larger state space,  $2^{kn}$ . Quantum connectivity also provides a potentially powerful means to overcome size-scaling and error-correlation problems that would limit the size of machines for quantum processing<sup>8</sup>. At any stage in the development of quantum technologies, there will be a largest size attainable for the state space of individual quantum processing units, and it will be possible to surpass this size by linking such units together into a fully quantum network.

A different perspective of a quantum network is to view the nodes as components of a physical system that interact by way of the quantum channels. In this case, the underlying physical processes used for quantum network protocols are adapted to simulate the evolution of quantum many-body systems<sup>9</sup>. For example, atoms that are localized at separate nodes can have effective spin-spin interactions catalysed by

single-photon pulses that travel along the channels between the nodes<sup>10</sup>. This 'quantum wiring' of the network allows a wide range for the effective hamiltonian and for the topology of the resultant 'lattice'. Moreover, from this perspective, the extension of entanglement across quantum networks can be related to the classical problem of percolation<sup>11</sup>.

These exciting opportunities provide the motivation to examine research related to the physical processes for translating the abstract illustration in Fig. 1a into reality. Such considerations are timely because scientific capabilities are now passing the threshold from a learning phase with individual systems and advancing into a domain of rudimentary functionality for quantum nodes connected by quantum channels.

In this review, I convey some basic principles for the physical implementation of quantum networks, with the aim of stimulating the involvement of a larger community in this endeavour, including in systems-level studies. I focus on current efforts to harness optical processes at the level of single photons and atoms for the transportation of quantum states reliably across complex quantum networks.

Two important research areas are strong coupling of single photons and atoms in the setting of cavity quantum electrodynamics (QED) $^{12}$  and quantum information processing with atomic ensembles $^{13}$ , for which crucial elements are long-lived quantum memories provided by the atomic system and efficient, quantum interfaces between light and matter. Many other physical systems are also being investigated and are discussed elsewhere (ref. 2 and websites for the Quantum Computation Roadmap (http://qist.lanl.gov/qcomp_map.shtml), the SCALA Integrated Project (http://www.scala-ip.org/public) and Qubit Applications (http://www.qubitapplications.com)).

# A quantum interface between light and matter

The main scientific challenge in the quest to distribute quantum states across a quantum network is to attain coherent control over the interactions of light and matter at the single-photon level. In contrast to atoms and electrons, which have relatively large long-range interactions for their spin and charge degrees of freedom, individual photons typically have interaction cross-sections that are orders of magnitude too small for non-trivial dynamics when coupled to single degrees of freedom for a material system.

The optical physics community began to address this issue in the 1990s, with the development of theoretical protocols for the coherent transfer of quantum states between atoms and photons in the setting of cavity  $\mathrm{QED}^{6,14,15}$ . Other important advances have been made in the past

decade $^{2,4}$ , including with atomic ensembles $^{13,16}$ . The reversible mapping of quantum states between light and matter provides the basis for quantum-optical interconnects and is a fundamental primitive (building block) for quantum networks. Although the original schemes for such interconnects are sensitive to experimental imperfections, a complete set of theoretical protocols has subsequently been developed for the robust distribution of quantum information over quantum networks, including, importantly, the quantum repeater $^{4,17}$  and scalable quantum networks with atomic ensembles $^{13}$ .

A generic quantum interface between light and matter is depicted in Fig. 1b. This interface is described by the interaction hamiltonian  $H_{\mathrm{int}}(t)$ , where for typical states  $H_{\mathrm{int}}(t)\rangle \approx \hbar \chi (t)$ , with  $\hbar$  being  $h / 2\pi$  (where  $h$  is Planck's constant) and  $\chi (t)$  being the time-dependent coupling strength between the internal material system and the electromagnetic field. Desirable properties for a quantum interface include that  $\chi (t)$  should be 'user controlled' for the clocking of states to and from the

quantum memory (for example, by using an auxiliary laser), that the physical processes used should be robust in the face of imperfections (for example, by using adiabatic transfer) and that mistakes should be efficiently detected and fixed (for example, with quantum error correction). In qualitative terms, the rate  $\kappa$ , which characterizes the bandwidth of the input-output channel, should be large compared with the rate  $\gamma$ , which characterizes parasitic losses, and both of these rates should be small compared with the rate of coherent coupling  $\chi$ .

Examples of physical systems for realizing a quantum interface and distributing coherence and entanglement between nodes are shown in Fig. 1c, d. In the first example (Fig. 1c), single atoms are trapped in optical cavities at nodes A and B, which are linked by an optical fibre. External fields control the transfer of the quantum state  $|\Psi \rangle$  stored in the atom at node A to the atom at node B by way of photons that propagate from node A to node  $\mathrm{B}^{6,18}$ . In the second example (Fig. 1d), a single-photon pulse that is generated at node A is coherently split into two

![](images/38910dc0b55cf5b52cfec55601a7c084565f8b819bff65900742fcb7efd51be7.jpg)  
a

![](images/d87d1ba1f780b0dee869a9d28ebda9c81736fe1c241fa4a094a9e28db7422797.jpg)  
b

![](images/5481651febc6ba36744a25c7184967103a106390dd0e32b749db1d0d7a9e911c.jpg)  
c

![](images/b40cbc89202bfe76f7f6e8905480b1431cd8bc7b1b985f9f344a54a2d0460ffa.jpg)  
d  
Figure 1 | Quantum networks. a, Shown is a notional quantum network composed of quantum nodes for processing and storing quantum states and quantum channels for distributing quantum information. Alternatively, such a network can be viewed as a strongly correlated many-particle system. b, The quantum interface between matter (coloured cube) and light (red curves) is depicted. Coherent interactions in the node are characterized by the rate  $\chi$ ; coupling between the node and photons in the external channel occurs at the rate  $\kappa$ ; and parasitic losses occur at the rate  $\gamma$ . c, Quantum state transfer and entanglement distribution from node A to node B is shown in the setting of cavity quantum electrodynamics (QED) $^6$ . At node A, a pulse of the control field  $\Omega_{\mathrm{A}}^{\mathrm{out}}(t)$  causes the transformation of atomic state  $|\Psi\rangle$  into the state of a  
propagating optical field (that is, into a flying photon). At node B, the pulse  $\Omega_{\mathrm{B}}^{\mathrm{in}}(t)$  is applied to map the state of the flying photon into an atom in the cavity, thereby realizing the transfer of the state  $|\Psi\rangle$  from node A to node B (ref. 18). d, The distribution of entanglement by using ensembles of a large number of atoms is shown<sup>13</sup>. A single-photon pulse at node A is coherently split into two entangled components that propagate to node B and node C and then are coherently mapped by the control fields  $\Omega_{\mathrm{B,C}}^{\mathrm{in}}(t)$  into a state that is entangled between collective excitations in each ensemble at node B and node C. At later times, components of the entangled state can be retrieved from the quantum memories by separate control fields,  $\Omega_{\mathrm{B,C}}^{\mathrm{out}}(t)$  (ref. 19).  $H_{\mathrm{int}}(t)$ , interaction hamiltonian;  $\hbar$ ,  $h/2\pi$  (where  $h$  is Planck's constant).

components and propagates to nodes B and C, where the entangled photon state is coherently mapped into an entangled state between collective excitations at each of the two nodes $^{13,19}$ . Subsequent read-out of entanglement from the memories at node B and/or node C as photon pulses is implemented at the 'push of a button'.

# Cavity QED

At the forefront of efforts to achieve strong, coherent interactions between light and matter has been the study of cavity QED $^{20}$ . In both the optical $^{12,21}$  and the microwave $^{22-25}$  domains, strong coupling of single atoms and photons has been achieved by using electromagnetic resonators of small mode volume (or cavity volume)  $V_{\mathrm{m}}$  with quality factors  $Q \approx 10^{7} - 10^{11}$ . Extensions of cavity QED to other systems $^{26}$  include quantum dots coupled to micropillars and photonic bandgap cavities $^{27}$ , and Cooper pairs interacting with superconducting resonators (that is, circuit QED; see ref. 28 for a review).

# Physical basis of strong coupling

Depicted in Fig. 2a is a single atom that is located in an optical resonator and for which strong coupling to a photon requires that a single intracavity photon creates a 'large' electric field. Stated more quantitatively, if the coupling frequency of one atom to a single mode of an optical resonator is  $g$  (that is,  $2g$  is the one-photon Rabi frequency), then

$$
g = \sqrt {\frac {\left| \boldsymbol {\varepsilon} \cdot \boldsymbol {\mu} _ {0} \right| ^ {2} \omega_ {\mathrm {C}}}{2 \hbar \varepsilon_ {0} V _ {\mathrm {m}}}} \tag {1}
$$

where  $\mu_0$  is the transition dipole moment between the relevant atomic states (with transition frequency  $\omega_{\mathrm{A}}$ ), and  $\omega_{\mathrm{C}} \approx \omega_{\mathrm{A}}$  is the resonant frequency of the cavity field, with polarization vector  $\varepsilon$ . Experiments in cavity QED explore strong coupling with  $g >> (\gamma, \kappa)$ , where  $\gamma$  is the atomic decay rate to modes other than the cavity mode and  $\kappa$  is the decay rate of the cavity mode itself. Expressed in the language of traditional optical physics, the number of photons required to saturate the intracavity atom is  $n_0 \approx \gamma^2 / g^2$ , and the number of atoms required to have an appreciable effect on the intracavity field is  $N_0 \approx \kappa \gamma / g^2$ . Strong coupling in cavity QED moves beyond traditional optical physics, for which  $(n_0, N_0) >> 1$ , to explore a qualitatively new regime with  $(n_0, N_0) << 1$  (ref. 12).

In the past three decades, a variety of approaches have been used to achieve strong coupling in cavity QED $^{12,20-25}$ . In the optical domain, a route to strong coupling is the use of high-finesse optical resonators ( $F \approx 10^{5} - 10^{6}$ ) and atomic transitions with a large  $\mu_0$  (that is, oscillator strengths near unity). Progress along this path is illustrated in Fig. 2c, with research now far into the domain ( $n_0, N_0) << 1$ .

As the cavity volume  $V_{\mathrm{m}}$  is reduced to increase  $g$  (equation (1)), the requirement for atomic localization becomes more stringent. Not surprisingly, efforts to trap and localize atoms in high-finesse optical cavities in a regime of strong coupling have been central to studies of cavity QED in the past decade, and the initial demonstration was in 1999 (ref. 29). Subsequent advances include extending the time for which an atom is trapped to 10 s (refs 30, 31); see ref. 32 for a review. Quantum control over both internal degrees of freedom (that is, the atomic dipole and the cavity field) and external degrees of freedom (that is, atomic motion) has now been achieved for a strongly coupled atom-cavity system<sup>33</sup>. And an exciting prospect is cavity QED with single trapped ions, for which the boundary for strong coupling has been reached<sup>34</sup>.

# Coherence and entanglement in cavity QED

Applying these advances to quantum networks has allowed single photons to be generated 'on demand' (Box 1). Through strong coupling of the cavity field to an atomic transition, an external control field  $\Omega(t)$  transfers one photon into the cavity mode and then to free space by way of the cavity output mirror, leading to a single-photon pulse  $|\phi_1(t)\rangle$  as a collimated beam. The temporal structure (both amplitude and phase) of the resultant 'flying photon'  $|\phi_1(t)\rangle$  can be tailored by way of

![](images/c8272b7f509a50387371a561e81648bf23d4f922ff76c7f1c66fa3372f0bc3ac.jpg)

![](images/8e817c9f75b8645764601c0ba9b2a007f77e1282d5b377d173f0ab5ad92531ee.jpg)

![](images/d2f34a6e2e0c2226c4d75f3880778515877654b534c87b18ece7b2779b882f78.jpg)  
Figure 2 | Elements of cavity QED. a, Shown is a simple schematic of an atom-cavity system depicting the three governing rates  $(g,\kappa ,\gamma)$  in cavity QED, where  $g\approx \chi$  in Fig. 1. Coherent exchange of excitation between the atom and the cavity field proceeds at rate  $g$ , as indicated by the dashed arrow for the atom and the green arrows for the cavity field. b, A photograph of two mirror substrates that form the Fabry-Pérot cavity, which is also shown schematically. The cavity length  $l = 10\mu \mathrm{m}$ , waist  $w_{0} = 12\mu \mathrm{m}$  transverse to the cavity axis, and finesse  $F\approx 5\times 10^{5}$ . The supporting structure allows active servo control of the cavity length to  $\delta l\approx 10^{-14}\mathrm{m}$  (ref. 12). Scale bar,  $3\mathrm{mm}$ . c, The reduction in the critical photon number  $n_0$  over time is shown for a series of experiments in cavity QED that were carried out by the Caltech Quantum Optics Group. These experiments involved either spherical-mirror Fabry-Pérot cavities (circles) or the whispering-gallery modes of monolithic  $\mathrm{SiO}_2$  resonators (squares). The data points shown for 2006 and 2008 are for a microtoroidal  $\mathrm{SiO}_2$  resonator[75,76]; those for 2009 and 2011 (open squares) are projections for this type of resonator[77].

the control field  $\Omega(t)$  (refs 6, 35), with the spatial structure of the wave packet being set by the cavity mode.

Several experiments have confirmed the essential aspects of this process for the deterministic generation of single photons $^{30,34,36}$ . Significantly, in the ideal (adiabatic) limit, the excited state  $|e\rangle$  of the atom is not populated because of the use of a 'dark state' protocol $^{37}$ . By deterministically generating a bit stream of single-photon pulses from single trapped atoms, these experiments are a first step in the development of quantum networks based on flying photons.

Compared with the generation of single photons by a variety of other systems $^{38}$ , one of the distinguishing aspects of the dark-state protocol (Box 1) is that it should be reversible. That is, a photon that is emitted from a system A should be able to be efficiently transferred to another system B by applying the time-reversed (and suitably delayed) field  $\Omega(t)$  to system B (Fig. 1c). Such an advance was made $^{18}$  by implementing the reversible mapping of a coherent optical field to and from internal states of a single trapped caesium atom. Although this experiment was imperfect, it provides the initial verification of the fundamental primitive on which the protocol for the physical implementation of quantum networks in ref. 6 is based (an important theoretical protocol that has been adapted to many theoretical and experimental settings).

# Box 1 Mapping quantum states between atoms and photons

![](images/7360b6fd3baad9742d1bcb00afb3f96bc5466e89c499b953b6df9f6beb245ba0.jpg)  
A  
a

![](images/6d1b926aa42195745b835dba4901c721d3419d180cda7b852accf628843d9047.jpg)

![](images/10198d319c21a3496b6827a1d932ac0161a6cbd2507b2e5caeaa71e5d71d3f2f.jpg)  
b

![](images/01b52b64209f41feb34b91a65bedc15f0a041e705ae72fb816c3d6689337b952.jpg)  
c

Reversible transfer of a state between light and a single trapped atom can be achieved through the mappings  $|b\rangle |1\rangle \rightarrow |a\rangle |0\rangle$  and  $|a\rangle |0\rangle \rightarrow |b\rangle |1\rangle$  for the coherent absorption and emission of single photons (in panel A, a and b of the figure, respectively) $^{18}$ . In this case,  $|a\rangle$  and  $|b\rangle$  represent internal states of the atom with long-lived coherence (for example, atomic hyperfine states in the  $6S_{1/2}$ ,  $F = 3$  and  $F = 4$  manifolds of atomic caesium), and  $|0\rangle$  and  $|1\rangle$  are Fock states of the photons in the intracavity field with  $n = 0$  and  $n = 1$  excitations, respectively. The transition between  $|b\rangle$  and  $|e\rangle$  is strongly coupled to a mode of an optical cavity with interaction energy  $\hbar g$ , where  $g$  (in green) is the coherent coupling rate of the atom and the photon. In this simple setting, the interaction hamiltonian for atom and cavity field has a dark state  $|D\rangle$  (that is, there is no excited state component  $|e\rangle$ ) $^{37}$ , as given by  $|D\rangle = \cos\theta |a\rangle |0\rangle + \sin\theta |b\rangle |1\rangle$ , where

$$
\cos \theta = \left[ 1 + \frac {\Omega^ {2} (t)}{g ^ {2}} \right] ^ {- 1 / 2} \tag {1}
$$

with  $\Omega(t)$  as a classical control field<sup>14</sup>. For  $\Omega(t = 0) = 0$ , then  $|D\rangle = |a\rangle |0\rangle$ . By contrast, for  $\Omega(t \to \infty) >> g$ ,  $|D\rangle \rightarrow |b\rangle |1\rangle$ .

Panel A, a of the figure shows that by adiabatically ramping a control field  $\Omega_1(t) >> g$  from on to off over a time  $\Delta t$  that is slow compared

![](images/7bf158a3362a7ecc78439eb9c33359d6f9cff7406969ddcb75fa75d2b6b442dc.jpg)  
B  
a  
b

![](images/6d263ec075d3f26e1e55a1f398cb0cc21fe2ee76e38a95863374b572c802559e.jpg)  
$\Omega_{1}(t)$

![](images/a46f8ea82dd8462d0d4042ccd8d33ba86b6254eb0063037d3d38f027912962df.jpg)

![](images/5bc21a5bf4418796e99a66e753161c152b61e56580c2206aeff8d85179cbdd91.jpg)

with  $1 / g$ , the atomic state is mapped from  $|b\rangle$  to  $|a\rangle$  with the accompanying coherent absorption of one intracavity photon. Conversely, in panel A, b of the figure, by turning a control field  $\Omega_{2}(t)$  from off to on, the atomic state is mapped from  $|a\rangle$  to  $|b\rangle$  with the transfer of one photon into the cavity mode.

These two processes can be combined to achieve the coherent transfer of the state of a propagating optical field  $\lambda(t) = |\phi_{\mathrm{field}}(t)\rangle$  into and out of a quantum memory formed by the atomic states  $|a\rangle$  and  $|b\rangle$  (ref. 18; figure, panel B). In the ideal case, the mapping is specified by  $|\phi_{\mathrm{field}}(t)\rangle |b\rangle \rightarrow |0\rangle (c_1|a\rangle + c_0|b\rangle)\ldots$  (storage) ...  $|0\rangle (c_1|a\rangle + c_0|b\rangle) \rightarrow |\phi_{\mathrm{field}}(t + \tau)\rangle |b\rangle$ , where the field state is taken to be a coherent superposition of zero  $(c_0)$  and one  $(c_1)$  photon,  $|\phi_{\mathrm{field}}(t)\rangle = E(t)[c_0|0\rangle_{\mathrm{field}} + c_1|1\rangle_{\mathrm{field}}]$ .  $E(t)$  is the envelope of the field external to the cavity, with  $\int |E(t)|^2 dt = 1$ ;  $t + \tau$  is a user-selected time (discussed below). Given timing information for the incoming field  $|\phi_{\mathrm{field}}(t)\rangle$ , the first step in this process (figure, panel B, a) is accomplished by adiabatically ramping the control field  $\Omega_1(t)$  from on to off, as in A, a. After this step, the internal states of the atom provide a long-lived quantum memory (figure, panel B, b). At a user-selected later time  $t + \tau$ , the final step is initiated (figure, panel B, c) by turning  $\Omega_2(t + \tau)$  from off to on (as in A, b), thereby coherently mapping the atomic state  $c_1|a\rangle + c_0|b\rangle$  back to the 'flying' field state  $\beta(t) = |\phi_{\mathrm{field}}(t + \tau)\rangle$ .

The adiabatic transfer of quantum states (as described in Box 1, as well as related possibilities $^{10,35}$ ) relies on strong coupling between an atom and a single polarization of the intracavity field. However, by extending the ideas in Box 1 to the two polarization eigenmodes of the cavity for given transverse and longitudinal mode orders, it is possible to generate entanglement between the internal states of the atom and the polarization state of a coherently generated photon $^{39-41}$ . An initial control field  $\Omega_{1}(t_{1})$  results in entanglement between internal states of the atom  $b$ ,  $|b_{\pm}\rangle$ , and the polarization state of a flying photon  $|\phi_{\mathrm{field}}^{\pm}(t_1)\rangle$  that is coherently generated by the coupled atom-cavity system. Applying a second control field  $\Omega_{2}(t_{2})$  returns the atom to its initial (unentangled) state while generating a second flying photon  $|\xi_{\mathrm{field}}^{\pm}(t_2)\rangle$ , thereby leading to entanglement between the polarizations of the fields,  $\phi_{\mathrm{field}}^{\pm}$  and  $\xi_{\mathrm{field}}^{\pm}$ , emitted at times  $t_1$  and  $t_2$ .

Such a sequence of operations has been applied to single rubidium atoms falling through a high-finesse optical cavity[21]. In this study, entangled photons were generated with a time separation  $\tau = t_2 - t_1$  limited by the atomic transit time. Although the atoms arrived randomly into the cavity mode in this case, the protocol itself is intrinsically deterministic. With trapped atoms, it will be possible to generate entangled states at user selected times  $(t_1, t_2)$  at the 'push of a button.' Moreover, the scheme is inherently reversible, so the entanglement between atom and field can be used to distribute entanglement to a second atom-cavity system in a network.

In a broader context, important advances have been made in the

generation and transfer of quantum states in other physical systems, including quantum dots $^{42}$  and circuits $^{28}$  coupled to cavities.

With the maturation of experimental capabilities in cavity QED that is now evident, many previously developed theoretical protocols will become possible. These include the sequential generation of entangled multiqubit states $^{43}$ , the teleportation of atomic states from one node to another $^{15}$ , photonic quantum computation by way of photon-photon interactions at the nodes $^{35}$  and reversible mapping of quantum states of atomic motion to and from light $^{44}$ . Clearly, new technical capabilities beyond conventional (Fabry-Pérot) cavities will be required to facilitate such scientific investigations; several candidate systems are discussed in Box 2.

# Quantum networks with atomic ensembles

An area of considerable research activity in the quest to distribute coherence and entanglement across quantum networks has been the interaction of light with atomic ensembles that consist of a large collection of identical atoms. For the regime of continuous variables, entanglement has been achieved between two atomic ensembles, each of which consists of  $\sim 10^{12}$  atoms $^{45}$ , and the quantum teleportation of light to matter has been demonstrated by mapping coherent optical states to the collective spin states of an atomic memory $^{46}$ . Further research of the continuous variables regime is reviewed elsewhere $^{47}$ . Here I focus, instead, on the regime of discrete variables, with photons and atomic excitations considered one by one.

# Box 2 | A new paradigm for cavity QED

![](images/3f63950369deb77f3cd3eb9e52646764050d4ede94b8fa511434da72ed3e8048.jpg)

To build large-scale quantum networks $^{4,6}$ , many quantum nodes will need to be interconnected over quantum channels. Because conventional (Fabry-Pérot) configurations are ill suited for this purpose, there have been efforts to develop alternative microcavity systems $^{26}$ , both for single atoms $^{75,76,78}$  and for atom-like systems (such as nitrogen-vacancy centres in diamond $^{79}$ ). A quantitative comparison of candidate systems is provided in ref. 77.

A remarkable resonator for this purpose is the microtoroidal cavity that is formed from fused  $\mathrm{SiO}_2$  (refs 80,81) (shown in the figure). Such a resonator supports a whispering-gallery mode $^{82}$  circulating around the outer circumference of the toroid (shown in cross-section in grey, in panel a of the figure), with an evanescent field external to the resonator. The intensity of the resonator mode is indicated by the coloured contours. Because of the small mode volume  $V_{\mathrm{m}}$  and large quality factor  $Q$ , an atom (blue) interacting with the evanescent field of a whispering-gallery mode can be far into the regime of strong coupling, with projected values for the critical photon  $n_0$  and atom  $N_0$  numbers  $(n_0 \approx 2 \times 10^{-5}$  and  $N_0 \approx 10^{-6})$ $^{77}$  that are significantly greater than current $^{12}$  and projected $^{77}$  values for cavity QED with Fabry-Pérot cavities (Fig. 2c). Pioneering fabrication techniques $^{80,81}$  lend themselves to the integration of many microtoroidal resonators to form optical networks, as illustrated in panel b and c of the figure. Panel b shows a photograph of a silicon chip with a linear array of microtoroidal resonators within an ultrahigh-vacuum apparatus $^{76}$ . The toroids appear as small scattering centres on a silicon chip that runs vertically down the centre of the picture. Black arrows indicate a horizontal  $\mathrm{SiO}_2$  fibre taper for

coupling light to and from one resonator. Scale bar,  $2\mathrm{mm}$ . Panel c is a scanning electron micrograph of an array of microtoroidal resonators (a magnification of the region bounded by the white box in panel b), showing toroids of fused  $\mathrm{SiO}_2$  on silicon supports<sup>80</sup>.

These resonators have the capability for input-output coupling with small parasitic loss $^{81}$  for the configuration shown in panel d (scale bar,  $10~{\mu\mathrm{m}}$ ), which is a micrograph of an individual toroid and fibre taper from panel  $\mathbf{b}^{76}$ .  $Q = 4\times 10^{8}$  has been realized at  $\lambda = 1,550\mathrm{nm}$ , and  $Q\approx 10^{8}$  at  $\lambda = 850\mathrm{nm}$ , with good prospects for improvement to  $Q\approx 10^{10}$  (ref. 77). For these parameters, the efficiency  $\varepsilon$  for coupling quantum fields into and out of the resonator could approach  $\varepsilon \approx 0.99 - 0.999$  while remaining firmly in the regime of strong coupling $^{77}$ . Such high efficiency is crucial for the realization of complex quantum networks, including for distributing and processing quantum information $^{4,6,35}$  and for investigating the association between quantum many-body systems and quantum networks $^{9,11}$ .

The initial step in this quest to realize a quantum network was the demonstration of strong coupling between individual atoms and the field of a microtoroidal resonator<sup>75</sup>. More recently, non-classical fields have been generated from the interaction of single atoms with a microtoroidal resonator by way of a 'photon turnstile', for which a single atom dynamically regulates the transport of photons one by one through the microtoroidal resonator<sup>76</sup> (figure, panel d). Only single photons can be transmitted in the forward direction (from right to left in the figure), with excess photons  $n > 1$  dynamically rerouted to the backward direction.

# Writing and reading collective spin excitations

Research on discrete quantum variables is based on the remarkable theoretical protocol described in ref. 13, in which Luming Duan, Mikhail Lukin, Juan Ignacio Cirac and Peter Zoller presented a realistic scheme for entanglement distribution by way of a quantum-repeater architecture $^{4,17}$ . Fundamental to this protocol, which is known as the DLCZ protocol, is the generation and retrieval of single 'spin' excitations within an ensemble of a large number of atoms $^{48}$  (Box 3). Together with photoelectric detection of field 1, a laser pulse ('write' pulse) creates a single excitation  $|1_{\mathrm{a}}\rangle$  that is stored collectively within the atomic ensemble. At a later time, a second laser pulse ('read' pulse) deterministically converts excitation stored within the atomic memory in the state  $|1_{\mathrm{a}}\rangle$  into a propagating field, denoted field 2.

The basic processes illustrated in Box 3 can be extended to create an entangled pair of ensembles, L and R (ref. 13; Fig. 3a). The entangled state is generated in a probabilistic but heralded $^{49}$  manner from quantum interference in the measurement process. That is, detection of a photon from one atomic ensemble or the other in an indistinguishable

manner results in an entangled state with one collective spin excitation shared coherently between the ensembles. In the ideal case, and to lowest-order probability, a photoelectric detection event at either of the two detectors projects the ensembles into the entangled state  $|\Psi_{\mathrm{L,R}}\rangle = \frac{1}{\sqrt{2}}\langle |0_{\mathrm{a}}\rangle_{\mathrm{L}}|1_{\mathrm{a}}\rangle_{\mathrm{R}} \pm e^{i\eta_{\mathrm{i}}}\lvert 1_{\mathrm{a}}\rangle_{\mathrm{L}}|0_{\mathrm{a}}\rangle_{\mathrm{R}}$ , with the sign (+ or -) set by whether detector 1 or detector 2 records the event. The phase  $\eta_{1}$  is determined by the difference between the phase shifts along the two channels,  $\eta_{1} = \beta_{\mathrm{L}} - \beta_{\mathrm{R}}$  (ref. 49), which must be stable. Any given trial with a 'write' pulse is unlikely to produce a detection event at either detector, and such failed trials require the system to be reinitialized. However, a photoelectric detection event at either detector unambiguously heralds the creation of the entangled state. Limited by the coherence time between the metastable lower atomic states  $|g\rangle_{i}$  and  $|s\rangle_{i}$  for all atoms  $i = 1,2,\dots,N_{\mathrm{a}}$  within the ensemble (ref. 50; Box 3), this entangled state is stored in the quantum memory provided by the ensembles and is available 'on demand' for subsequent tasks, such as entanglement connection[13,51].

Although the above description is for an ideal case and neglects higher-order terms, the DLCZ protocol is designed to be resilient to

# Box 3 Writing and reading single atomic excitations

![](images/af6bf65ab8e6a882c2bb01b6c45dcce2c667078df5b2c53112a8ce74e20271d9.jpg)  
a

![](images/0fb7c4dd5063e2184f923a3a91ddf6c5ef41e53d6e6c41190caafeb39c972b6a.jpg)

![](images/6c5ea8941aa4568efd8443af0d8ca9835c8c7ea38e05b94b2c361f03fe253570.jpg)  
b

![](images/19673f83fa4effdbeba0e910f0400e13aa7a6b8dad5ba8aa5f3197e848bd0153.jpg)  
The DLCZ protocol<sup>13</sup> is based on ensembles of  $N_{\mathrm{a}}$  identical atoms (blue) with a  $\Lambda$ -level configuration, as shown in the figure. The metastable lower states  $|g\rangle$  and  $|s\rangle$  can be, for example, atomic hyperfine states of the electronic ground level to ensure a long lifetime for coherence. All atoms are initially prepared in state  $|g\rangle$  with no excitation (figure, panel a), namely  $|0_{a}\rangle \otimes_{i}^{N_{o}}|g\rangle_{i}$ , and a weak off-resonant 'write' pulse is then sent through the ensemble. This results in a small probability of amplitude  $\sqrt{p}$  that one of the  $N_{\mathrm{a}}$  atoms will be transferred from  $|g\rangle$  to  $|s\rangle$  and will emit a photon into the forward-scattered optical mode

important sources of imperfections, including losses in propagation and detection, and detector dark counts. Indeed, the scheme functions with 'built-in entanglement purification' and enables entanglement to be extended beyond the separation of two ensembles in an efficient and scalable manner. Theoretical extensions of the DLCZ protocol have examined related network architectures for optimizing scalability in view of laboratory capabilities (discussed below).

# Coherence and entanglement with atomic ensembles

The initial, enabling, steps in the implementation of the DLCZ protocol were observations of quantum correlations both for single photon pairs $^{54,55}$  and for a large number of photons  $(10^{3} - 10^{4})$  (ref. 56) generated in the collective emission from atomic ensembles. Single photons were generated by the efficient mapping of stored collective atomic excitation to propagating wave packets for field 2 (refs 57-61; Box 3). Conditional read-out efficiencies of  $50\%$  in free space $^{58}$  and  $84\%$  in a cavity $^{62}$  were realized for state transfer from a single collective 'spin' excitation stored in the atomic ensemble to a single photon for field 2.

With these capabilities for coherent control of collective atomic emission, heralded entanglement between ensembles separated by  $3\mathrm{m}$  was achieved in 2005 (ref. 49). More recent work has led to the inference that the concurrence  $C$  (ref. 63) of entanglement stored between the two ensembles in Fig. 3 is  $C = 0.9 \pm 0.3$  (ref. 50), with the associated density matrix shown in Fig. 3b.

The DLCZ protocol is based on a quantum-repeater architecture involving independent operations on parallel chains of quantum systems<sup>13</sup>, with scalability relying crucially on conditional control of quantum states stored in remote quantum memories<sup>64</sup>. The experiment shown in Fig. 3c took an important step towards this goal by achieving the minimal functionality required for scalable quantum networks<sup>65</sup>.

Apart from the DLCZ protocol, which involves measurement-induced entanglement, it is also possible to achieve deterministic mapping of quantum states of light into and out of atomic ensembles by using electromagnetically induced transparency $^{16,66}$ . Pioneering

( designated field 1) with a frequency and/or polarization distinct from the write field.

For small excitation probability  $p < 1$ , in most cases nothing happens as a result of the writing pulse, so the resultant state  $|\phi_{a,1}\rangle$  for the atomic ensemble and field 1 in the ideal case is given by

$$
\left| \phi_ {a, 1} \right\rangle \left| O _ {a} \right\rangle \left| O _ {1} \right\rangle + e ^ {i \beta} \sqrt {p} \left| I _ {a} \right\rangle \left| I _ {1} \right\rangle + O (p) \tag {1}
$$

where  $|n_1\rangle$  is the state of the forward-propagating field 1 with  $n_1$  photons ( $n_1 = 0$  or 1), the phase  $\beta$  is determined by the propagation phases of the write pulse and field 1, and  $O(p)$  denotes of order  $p$ . The atomic state  $|1_{\mathrm{a}}\rangle$  in equation (1) (above) is a collective (entangled) state with one excitation shared symmetrically between the  $N_{\mathrm{a}}$  atoms (that is, one 'spin flip' from  $|g\rangle$  to  $|s\rangle$ ), where in the ideal case<sup>13</sup>

$$
\left| 1 _ {\mathrm {a}} \right\rangle = \frac {1}{\sqrt {N} _ {\mathrm {a}}} \sum_ {i = 1} ^ {N _ {\mathrm {a}}} | g \rangle_ {i} \dots | s \rangle_ {i} \dots | g \rangle_ {N _ {\mathrm {a}}} \tag {2}
$$

Field 1 is directed to a single-photon detector, where a detection event is recorded with probability  $p$ . Such an event for field 1 heralds that a single excitation (or spin flip from  $|g\rangle$  to  $|s\rangle$ ) has been created and stored in the atomic ensemble in the state  $|1_{\mathrm{a}}\rangle$  with high probability. Higher-order processes with multiple atomic and field 1 excitations are also possible and ideally occur, to lowest order, with probability  $p^2$ .

After a user-defined delay (subject to the finite lifetime of the quantum memory), the collective atomic excitation  $|1_{\mathrm{a}} \rangle$  can be efficiently converted to a propagating beam (designated field 2) by way of a strong 'read' pulse (figure, panel b), where in the ideal case there is a one-to-one transformation of atomic excitation to field excitation,  $|1_{\mathrm{a}} \rangle$  to  $|1_{2} \rangle$ . In the case of resonance with the transition from  $|s \rangle$  to  $|e \rangle$ , the reading process utilizes the phenomenon of electromagnetically induced transparency<sup>16,66</sup>.

work $^{67,68}$  demonstrated the storage and retrieval of classical pulses to and from an atomic ensemble. This work was then extended into the quantum regime of single photons $^{69,70}$ . Entanglement between two ensembles coupled to a cavity mode was achieved by adiabatic transfer of excitation $^{71}$ , thereby providing a means for on-demand entanglement. In addition, the reversible mapping of photonic entanglement into and out of pairs of quantum memories has been achieved $^{19}$  by an electromagnetically-induced-transparency process, which should assist the distribution of entanglement over quantum networks (Fig. 1d).

Contemporary with this work on heralded and deterministic entanglement, a variety of experiments based on entanglement as a postdiction have been carried out[72] (that is, for cases in which a physical state is not available for use in a scalable network but which are nonetheless significant). An important advance in this regard is the use of a pair of ensembles for entanglement generation to achieve a posteriori teleportation of light to an atomic memory[73].

There has also been considerable effort devoted to the detailed characterization of decoherence for stored atomic excitation and entanglement $^{50,65,73}$ . Decoherence of entanglement between distinct atomic ensembles has been observed in the decay of the violation of Bell's inequality $^{65}$  and of the fidelity for teleportation $^{73}$ . By measuring concurrence  $C(t)$ , quantitative characterizations of the relationship between the global evolution of the entangled state and the temporal dynamics of various local correlations were also able to be made $^{50}$ .

# Extending entanglement for quantum networks

The entangled states that have been created so far both in cavity QED and by using the DLCZ protocol are between pairs of systems (known as bipartite entanglement) for which there are definitive procedures for operational verification $^{72}$ . The creation of more-general classes of entangled state shared between more than two nodes would be of great interest. However, as researchers progress towards more-complex quantum networks, the issue of entanglement verification becomes increasingly problematic. At present, the theoretical tools and experimental

![](images/7f246c20fca5ebca0bcd4c98e3910eab09428e3060b9ba0b97c531131906ea9d.jpg)

![](images/be00481f9d707582e0b4e280b913b073ec7e551e49ff533321c7ecb50b85198d.jpg)  
b

![](images/93f99809a37dea866fcd8840dfcb788f8d91212980a1d6a1f820376c8d43b5b7.jpg)  
Figure 3 | Fundamentals of the DLCZ protocol. A realistic scheme for entanglement distribution by way of a quantum-repeater architecture was proposed by Duan, Lukin, Cirac and Zoller and is known as the DLCZ protocol $^{13}$ . a, Measurement-induced entanglement between two atomic ensembles $^{13,49}$ , L and R, is shown. Synchronized laser pulses incident on the ensembles (denoted write beams, blue arrows) generate small amplitudes for optical fields from spontaneous Raman scattering $^{48}$ ; these fields are denoted  $1_{\mathrm{L}}$  and  $1_{\mathrm{R}}$  (red arrows). These fields interfere at a 50/50 beam splitter, with outputs directed to two single-photon detectors. A measurement event at either detector (shown for detector 1) projects the ensembles into the entangled state  $|\Psi_{\mathrm{L,R}}\rangle$  with one quantum of excitation shared remotely between the ensembles. Entanglement is stored in the quantum memory provided by the ensembles and can subsequently be converted to propagating light pulses by a set of 'read' laser pulses (Box 3). b, Experimentally determined components of the density matrix  $\rho_{\mathrm{L,R}}^{\mathrm{exp}}$  for entanglement between two atomic ensembles are shown $^{50}$ , corresponding to concurrence  $C = 0.9 \pm 0.3$ , where  $C = 0$  for an unentangled state. The first number in each ket refers to the excitation number for the ensemble L, and the second is for the ensemble R. For comparison, the density matrix  $\rho_{\mathrm{L,R}}^{\mathrm{iddeal}}$  for the ideal state  $|\Psi_{\mathrm{L,R}}^{\mathrm{u}}\rangle$  is shown, with concurrence  $C = 1$ . c, The laboratory set-up is shown for the entanglement of two pairs of atomic ensembles to generate the functional quantum nodes L and R, which are separated by 3 m (ref. 65). Each of the four elongated ovals shows a cylinder of  $10^{5}$  caesium atoms, which forms an atomic ensemble at each site. Entangled states between the upper u and lower l pairs at the L and R nodes,  $|\Psi_{\mathrm{L,R}}^{\mathrm{u}}\rangle |\Psi_{\mathrm{L,R}}^{\mathrm{l}}\rangle$ , are generated and stored in an asynchronous manner for each pair (u and l) as is the case in panel a. Atomic excitations for the pairs  $\mathbf{L}_{\mathrm{w}}, \mathbf{L}_{\mathrm{i}}$  and  $\mathbf{R}_{\mathrm{w}}, \mathbf{R}_{\mathrm{i}}$  are subsequently converted to flying photons at each node, with a polarization encoding that results in violation of Bell's inequality $^{65}$ . The entire experiment functions under the quantum control of single photon detection events.

![](images/e275500ba2c571f92ee2d07d9f1a244512325677047fb3b57f1a1e2cd406dcfa.jpg)

capabilities for characterizing the general states of quantum networks do not exist.

Perhaps surprisingly, a non-trivial task will be to find out whether a quantum network 'works'. As moderately complex quantum networks are realized in the laboratory, it will become increasingly more difficult to assess the characteristics of a network quantitatively, including whether entanglement extends across the whole network. One strategy, motivated by the underlying physical processes of the network, could be to try to determine the density matrix  $\rho(t)$  for the network. However, this approach would fail because of the exponential growth in  $\rho(t)$  with the size of a network.

An alternative strategy could be based on more functional issues of algorithmic capability. An attempt could be made to implement a quantum algorithm for computation or communication to test whether the purported quantum network has greater capabilities than any classical counterpart. This course is, however, problematic because the advantage of a quantum network might only be realized above some threshold in the size of the network. Furthermore, from an experimental perspective, this strategy does not offer much in the way of diagnostics for 'fixing' the network when it fails.

Another, less obvious, approach might be to adopt more seriously the perspective of a quantum network as a quantum many-body system and to search for more 'physical' characteristics of the network (for example, the scaling behaviour of pair correlation functions and multipartite entanglement). Indeed, an active area of research is the nature of entanglement for systems that undergo quantum phase transitions, and there have been pioneering advances in the study of one-dimensional spin chains $^{74}$ .

# Conclusion

Progress has been made towards the development of quantum networks, but the current state of the art is primitive relative to that required for the robust and scalable implementation of sophisticated network protocols, whether over short or long distances. The realization of quantum memories, local quantum processing, quantum repeaters and error-corrected teleportation are ambitious goals. Nevertheless, there is considerable activity directed towards these goals worldwide.

Here cavity-QED-based networks and networks implemented using the DLCZ protocol were considered separately, but it is clear that quantum networks will evolve as heterogeneous entities. For example, the same protocol that creates the entanglement between the two ensembles shown in Fig. 3a can be used to create an entangled state with one excitation shared between an atom in a cavity and an atomic ensemble. A crucial task will be the development of unambiguous procedures for verifying entanglement, a non-trivial undertaking that has not always been carried out correctly $^{72}$ .

I have used quantum networks as a unifying theme, but the research described here has broader value, including advancing the understanding of quantum dynamical systems and, for the cases considered here, creating new physics from controlled nonlinear interactions of single photons and atoms. These are exciting times in quantum information science as researchers pass from the regime of individual building blocks (for example, a single atom-cavity system) to the realm of complex quantum systems that are assembled block by block from many such units.

1. Nielsen, M. A. & Chuang, I. L. Quantum Computation and Quantum Information (Cambridge Univ. Press, Cambridge, UK, 2000).  
2. Zoller, P. et al. Quantum information processing and communication. Strategic report on current status, visions and goals for research in Europe. Eur. Phys. J. D 36, 203-228 (2005).  
3. Bennett, C. H., Brassard, G. & Ekert, A. K. Quantum cryptography. Sci. Am. 267 (4), 50-57 (1992).  
4. Bouwmeester, D., Ekert, A. & Zeilinger, A. (eds) The Physics of Quantum Information (Springer, Berlin, 2000).  
5. Giovannetti, V., Lloyd, S. & Maccone, L. Quantum-enhanced measurements: beating the standard quantum limit. Science 306, 1330-1336 (2004).  
6. Cirac, J. I., Zoller, P., Kimble, H. J. & Mabuchi, H. Quantum state transfer and entanglement distribution among distant nodes in a quantum network. Phys. Rev. Lett. 78, 3221-3224 (1997).  
7. Preskill, J. P. Plug-in quantum software. Nature 402, 357-358 (1999).  
8. Copsey, D. et al. Toward a scalable, silicon-based quantum computing architecture. IEEE J. Quantum Electron. 9, 1552-1569 (2003).  
9. Illuminati, D. Light does matter. Nature Phys. 2, 803-804 (2006).  
10. Duan, L.-M., Wang, B. & Kimble, H. J. Robust quantum gates on neutral atoms with cavity-assisted photon scattering. Phys. Rev. A 72, 032333 (2005).  
11. Acin, A., Cirac, J.I. & Lewenstein, M., Entanglement percolation in quantum networks. Nature Phys. 3, 256-259 (2007).  
12. Miller, R. et al. Trapped atoms in cavity QED: coupling quantized light and matter. J. Phys. B 38, S551-S565 (2005).  
13. Duan, L.-M., Lukin, M. D., Cirac, J. I. & Zoller, P. Long-distance quantum communication with atomic ensembles and linear optics. Nature 414, 413-418 (2001).  
14. Parkins, A. S., Marte, P., Zoller, P. & Kimble, H. J. Synthesis of arbitrary quantum states via adiabatic transfer of Zeeman coherence. Phys. Rev. Lett. 71, 3095-3098 (1993).

15. van Enk, S. J., Cirac, J. I. & Zoller, P. Photonic channels for quantum communication. Science 279, 205-208 (1998).  
16. Lukin, M. D. Trapping and manipulating photon states in atomic ensembles. Rev. Mod. Phys. 75, 457-472 (2003).  
17. Briegel, H.-J., Dur, W., Cirac, J.I. & Zoller, P. Quantum repeaters: the role of imperfect local operations in quantum communication. Phys. Rev. Lett. 81, 5932-5935 (1998).  
18. Boozer, A. D., Boca, A., Miller, R., Northup, T. E. & Kimble, H. J. Reversible state transfer between light and a single trapped atom. Phys. Rev. Lett. 98, 193601 (2007).  
19. Choi, K. S., Deng, H., Laurat, J. & Kimble, H. J. Mapping photonic entanglement into and out of a quantum memory. Nature 452, 67-71 (2008).  
20. Berman, P. (ed.) Cavity Quantum Electrodynamics (Academic, San Diego, 1994).  
21. Wilk, T., Webster, S. C., Kuhn, A. & Rempe, G. Single-atom single-photon quantum interface. Science 317, 488-490 (2007).  
22. Walther, H. Quantum optics of single atoms. Fortschr. Phys. 52, 1154-1164 (2004).  
23. Meschede, D., Walther, H. & Mueller, G. One-atom maser. Phys. Rev. Lett. 54, 551-554 (1985).  
24. Raimond, J. M. et al. Probing a quantum field in a photon box. J. Phys. B 38, S535-S550 (2005).  
25. Guerlin, C. et al. Progressive field-state collapse and quantum non-demolition photon counting. Nature 448, 889-893 (2007).  
26. Vahala, K.J. Optical microcavities. Nature 424, 839-846 (2004).  
27. Khitrova, G., Gibbs, H. M., Kira, M., Koch, S. W. & Scherer, A. Vacuum Rabi splitting in semiconductors. Nature Phys. 2, 81-90 (2006).  
28. Schoelkopf, R. J. & Girvin, S. M. Wiring up quantum systems. Nature 451, 664-669 (2008).  
29. Ye, J., Vernooy, D. W. & Kimble, H. J. Trapping of single atoms in cavity QED. Phys. Rev. Lett. 83, 4987-4990 (1999).  
30. Hijlkema, M. et al. A single-photon server with just one atom. Nature Phys. 3, 253-255 (2007).  
31. Fortier, K. M., Kim, S. Y., Gibbons, M. J., Ahmadi, P. & Chapman, M. S. Deterministic loading of individual atoms to a high-finesse optical cavity. Phys. Rev. Lett. 98, 233601 (2007).  
32. Ye, J., Kimble, H. J. & Katori, H. Quantum state engineering and precision metrology using state-insensitive light traps. Science (in the press).  
33. Boozer, A. D., Boca, A., Miller, R., Northup, T. E. & Kimble, H. J. Cooling to the ground state of axial motion for one atom strongly coupled to an optical cavity. Phys. Rev. Lett. 97, 083602 (2006).  
34. Keller, M., Lange, B., Hayasaka, K., Lange, W. & Walther, H. Continuous generation of single photons with controlled waveform in an ion-trap cavity system. Nature 431, 1075-1078 (2004).  
35. Duan, L.-M. & Kimble, H. J. Scalable photonic quantum computation through cavity-assisted interactions. Phys. Rev. Lett. 92, 127902 (2004).  
36. McKeever, J. et al. Deterministic generation of single photons from one atom trapped in a cavity, Science 303, 1992-1994 (2004).  
37. Bergmann, K., Theuer, H. & Shore, B. W. Coherent population transfer among quantum states of atoms and molecules. Rev. Mod. Phys. 70, 1003-1025 (1998).  
38. Lounis, B. & Orrit, M. Single-photon sources. Rep. Prog. Phys. 68, 1129-1179 (2005).  
39. Lange, W. & Kimble, H. J. Dynamic generation of maximally entangled photon multiplets by adiabatic passage. Phys. Rev. A 61, 063817 (2000).  
40. Duan, L.-M. & Kimble, H. J. Efficient engineering of multiatom entanglement through single-photon detections. Phys. Rev. Lett. 90, 253601 (2003).  
41. Sun, B., Chapman, M. S. & You, L. Atom-photon entanglement generation and distribution. Phys. Rev. A 69, 042316 (2004).  
42. Englund, D., Faraon, A., Zhang, B., Yamamoto, Y. & Vucovic, J. Generation and transfer of single photons on a photonic crystal chip. Opt. Express 15, 5550-5558 (2007).  
43. Schön, C., Solano, E., Verstraete, F., Cirac, J. I. & Wolf, M. M. Sequential generation of entangled multiqubit states. Phys. Rev. Lett. 95, 110503 (2005).  
44. Parkins, A. S. & Kimble, H. J. Quantum state transfer between motion and light. J. Opt. B 1, 496-504 (1999).  
45. Julsgaard, B., Kozhekin, A. & Polzik, E. S. Experimental long-lived entanglement of two macroscopic objects. Nature 413, 400-403 (2001).  
46. Sherson, J. F. et al. Quantum teleportation between light and matter. Nature 443, 557-560 (2006).  
47. Cerf, N. J., Leuchs, G. & Polzik, E. S. (eds) Quantum Information with Continuous Variables of Atoms and Light (World Scientific, New Jersey, 2007).  
48. Raymer, M. G., Walmsley, I. A., Mostowski, J. & Sobolewka, B. Quantum theory of spatial and temporal coherence properties of stimulated Raman scattering. Phys. Rev. A 32, 332-344 (1985).  
49. Chou, C.-W. et al. Measurement-induced entanglement for excitation stored in remote atomic ensembles. Nature 438, 828-832 (2005).  
50. Laurat, J., Choi, K. S., Deng, H., Chou, C.-W. & Kimble, H. J. Heralded entanglement between atomic ensembles: preparation, decoherence, and scaling. Phys. Rev. Lett. 99, 180504 (2007).

51. Laurat, J. et al. Towards experimental entanglement connection with atomic ensembles in the single excitation regime. New J. Phys. 9, 207-220 (2007).  
52. Jiang, L., Taylor, J. M. & Lukin, M. D. Fast and robust approach to long-distance quantum communication with atomic ensembles. Phys. Rev. A 76, 012301 (2007).  
53. Sanguard, N. et al. Robust and efficient quantum repeaters with atomic ensembles and linear optics. Preprint at http://arxiv.org/abs/0802.1475 (2008).  
54. Kuzmich, A. et al. Generation of nonclassical photon pairs for scalable quantum communication with atomic ensembles. Nature 423, 731-734 (2003).  
55. Balic, V., Braje, D. A., Kolchin, P., Yin, G. Y. & Harris, S. E. Generation of paired photons with controllable waveforms. Phys. Rev. Lett. 94, 183601 (2005).  
56. van der Wal, C. H. et al. Atomic memory for correlated photon states. Science 301, 196-200 (2003).  
57. Chou, C. W., Polyakov, S. V., Kuzmich, A. & Kimble, H. J. Single-photon generation from stored excitation in an atomic ensemble. Phys. Rev. Lett. 92, 213601 (2004).  
58. Laurat, J. et al. Efficient retrieval of a single excitation stored in an atomic ensemble. Opt. Express 14, 6912-6918 (2006).  
59. Thompson, J. K., Simon, J., Loh, H. & Vuletic, V. A high-brightness source of narrowband, identical-photon pairs. Science 313, 74-77 (2006).  
60. Matsukevich, D. N. et al. Deterministic single photons via conditional quantum evolution. Phys. Rev. Lett. 97, 013601 (2006).  
61. Chen, S. et al. Deterministic and storable single-photon source based on a quantum memory. Phys. Rev. Lett. 97, 173004 (2006).  
62. Simon, J., Tanji, H., Thompson, J. K. & Vuletic, V. Interfacing collective atomic excitations and single photons. Phys.Rev.Lett. 98, 183601 (2007).  
63. Wootters, W. K. Entanglement of formation of an arbitrary state of two qubits. Phys. Rev. Lett. 80, 2245-2248 (1998).  
64. Felinto, D. et al. Conditional control of the quantum states of remote atomic memories for quantum networking. Nature Phys. 2, 844-848 (2006).  
65. Chou, C.-W. et al. Functional quantum nodes for entanglement distribution over scalable quantum networks. Science 316, 1316-1320 (2007).  
66. Harris, S. E. Electromagnetically induced transparency. Phys. Today 50, 36-40 (1997).  
67. Liu, C., Dutton, Z., Behroozzi, C. H. & Hau, L. V. Observation of coherent optical information storage in an atomic medium using halted light pulses. Nature 409, 490-493 (2001).  
68. Phillips, D. F., Fleischhauer, A., Mair, A., Walsworth, R. L. & Lukin, M. D. Storage of light in atomic vapor. Phys. Rev. Lett. 86, 783-786 (2001).  
69. Chaneliere, T. et al. Storage and retrieval of single photons transmitted between remote quantum memories. Nature 438, 833-836 (2005).  
70. Eisaman, M. D. et al. Electromagnetically induced transparency with tunable single-photon pulses. Nature 438, 837-841 (2005).  
71. Simon, J., Tanji, H., Ghosh, S. & Vuletic, V. Single-photon bus connecting spin-wave quantum memories. Nature Phys. 3, 765-769 (2007).  
72. van Enk, S. J., Lütkenhaus, N. & Kimble, H. J. Experimental procedures for entanglement verification. Phys. Rev. A 75, 052318 (2007).  
73. Chen, Y.-A. et al. Memory-built-in quantum teleportation with photonic and atomic qubits. Nature Phys. 4, 103-107 (2008).  
74. Vidal, G., Latorre, J.I., Rico, E. & Kitaev, A. Entanglement in quantum critical phenomena. Phys. Rev. Lett. 90, 227902 (2003).  
75. Aoki, T. et al. Observation of strong coupling between one atom and a monolithic microresonator. Nature 443, 671-674 (2006).  
76. Dayan, B. et al. A photon turnstile dynamically regulated by one atom. Science 319, 1062-1065 (2008).  
77. Spillane, S. M. et al. Ultrahigh-Q toroidal microresonators for cavity quantum electrodynamics. Phys. Rev. A 71, 013817 (2005).  
78. Trupke, M. et al. Atom detection and photon production in a scalable, open, optical microcavity. Phys. Rev. Lett. 99, 063601 (2007).  
79. Park, Y.-S., Cook, A. K. & Wang, H. Cavity QED with diamond nanocrystals and silica microspheres. Nano Lett. 6, 2075-2079 (2006).  
80. Armani, D. K., Kippenberg, T. J., Spillane, S. M. & Wahala, K. J. Ultra-high-Q toroid microcavity on a chip. Nature 421, 925-928 (2003).  
81. Spillane, S. M., Koppenberg, T. J., Painter, O. J. & Vahala, K. J. Ideality in a fiber-taper-coupled microresonator system for application to cavity quantum electrodynamics. Phys. Rev. Lett. 91, 043902 (2003).  
82. Braginsky, V. B., Gorodetsky, M. L. & Ilchenko, V. S. Quality-factor and nonlinear properties of optical whispering-gallery modes. Phys. Lett. A 137, 393-397 (1989).

Acknowledgements I am grateful for the contributions of members of the Caltech Quantum Optics Group, especially K. S. Choi, B. Dayan and R. Miller. I am indebted to J. P. Preskill and S. J. van Enk for critical insights. My research is supported by the National Science Foundation, IARPA and Northrop Grumman Space Technology.

Author Information Reprints and permissions information is available at www.nature.com/reprints. The author declares no competing financial interests. Correspondence should be addressed to the author (hjkimble@caltech.edu).