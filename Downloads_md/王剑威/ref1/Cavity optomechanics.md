# Cavity optomechanics

Markus Aspelmeyer*

Vienna Center for Quantum Science and Technology (VCQ), Faculty of Physics, University of Vienna, 1090 Vienna, Austria

Tobias J. Kippenberg†

Ecole Polytechnique Fédérale de Lausanne (EPFL), Institute of Condensed Matter Physics CH-1015 Lausanne, Switzerland

Florian Marquardt‡

University of Erlangen-Nürnberg, Institute for Theoretical Physics, Staudtstrasse 7, 91058 Erlangen, Germany, and Max Planck Institute for the Science of Light, 91058 Erlangen, Germany

(published 30 December 2014)

The field of cavity optomechanics is reviewed. This field explores the interaction between electromagnetic radiation and nanomechanical or micromechanical motion. This review covers the basics of optical cavities and mechanical resonators, their mutual optomechanical interaction mediated by the radiation-pressure force, the large variety of experimental systems which exhibit this interaction, optical measurements of mechanical motion, dynamical backaction amplification and cooling, nonlinear dynamics, multimode optomechanics, and proposals for future cavity-quantum-optomechanics experiments. In addition, the perspectives for fundamental quantum physics and for possible applications of optomechanical devices are described.

DOI: 10.1103/RevModPhys.86.1391

PACS numbers: 42.50.-p

# CONTENTS

I. Introduction 1392

II. Optical Cavities and Mechanical Resonators 1394

A. Optical resonators 1395

1. Basic properties 1395  
2. Input-output formalism for an optical cavity 1395

B.Mechanical resonators 1397

1.Mechanical normal modes 1397  
2.Mechanical dissipation 1398  
3. Susceptibility, noise spectra, and fluctuation-dissipation theorem 1398

III. Principles of Optomechanical Coupling 1399

A. The radiation-pressure force and optomechanical coupling 1399  
B. Hamiltonian formulation 1400  
C. Optomechanical equations of motion 1402

IV. Experimental Realizations and Optomechanical Parameters 1404

A. Optomechanical parameters 1405  
B. Suspended mirrors 1405  
C. Optical microresonators 1406  
D.Waveguides and photonic crystal cavities 1407  
E. Suspended and levitated nano-objects 1408  
F. Microwave resonators 1408  
G. Ultracold atoms 1409

V. Basic Consequences of the Optomechanical Interaction 1409

A. Static phenomena: Optical potential and bistability 1409  
B. Dynamical backaction 1410

1. Optical spring effect 1411  
2. Optomechanical damping rate 1411

a.Mechanical picture 1411  
b. Scattering picture 1412  
c. Feedback picture 1413  
d. Resolved-sideband regime 1413  
e. Doppler regime 1413

VI. Quantum Optical Measurements of Mechanical Motion 1413

A. Parametric displacement sensing and the standard quantum limit 1414  
1. Introduction and qualitative discussion 1414  
2. The standard quantum limit 1414

B. Optical QND measurements 1417  
1. Single-quadrature measurements 1417

2.Mechanical Fock-state detection 1418  
3. Optical feedback cooling (cold damping) 1419

VII. Optomechanical Cooling 1419

A. Quantum theory of radiation-pressure cooling 1420  
1. Finite thermal cavity occupancy 1421  
2. Equations-of-motion approach 1421  
3. Optical output spectrum 1422

B. Experiments and practical limitations 1423

1. Experimental developments 1423  
2. Laser phase noise 1424  
3. Cavity frequency noise 1424

C. Strong-coupling regime 1424

1. Optomechanical normal-mode splitting 1424  
2. Optomechanically induced transparency 1426

3. Optomechanically induced amplification and electromagnetically induced absorption

VIII. Classical Nonlinear Dynamics 1428

A. Parametric instability and attractor diagram 1429  
B. Chaotic dynamics 1431

IX. Multimode Optomechanics 1431

X.Quantum Optomechanics 1433

A.Light-assisted coherent manipulation of mechanics 1433  
B. Mechanics-assisted readout and manipulation of light 1433  
C.Optomechanical entanglement 1434  
D.Quantum hybrid systems 1436  
E.Quantum protocols 1437  
F.Nonlinear quantum optomechanics 1439

XI. Future Perspectives 1442

A. Foundational aspects 1442  
B. Applications 1443

Acknowledgments 1444

Appendix: Experimental Challenges 1444

1. Influence of classical excess laser phase noise on laser cooling 1444  
2. Influence of cavity frequency noise on laser cooling 1444  
a. Finite thermal cavity occupancy 1445  
3. Influence of classical excess laser noise on sideband thermometry 1445

References 1445

# I. INTRODUCTION

Light carries momentum which gives rise to radiation-pressure forces. These forces were already postulated in the 17th century by Kepler, who noted that the dust tails of comets point away from the Sun during a comet transit (Kepler, 1619). The first unambiguous experimental demonstrations of the radiation-pressure force predicted by Maxwell were performed using a light mill configuration (Lebedew, 1901; Nichols and Hull, 1901). A careful analysis of these experiments was required to distinguish the phenomenon from thermal effects that had dominated earlier observations. As early as 1909, Einstein derived the statistics of the radiation-pressure force fluctuations acting on a movable mirror (Einstein, 1909), including the frictional effects of the radiation force, and this analysis allowed him to reveal the dual wave-particle nature of blackbody radiation. In pioneering experiments, both the linear and angular momentum transfers of photons to atoms and macroscopic objects were demonstrated by Frisch (1933) and Beth (1936), respectively.

In the 1970s Ashkin demonstrated the fact that focused laser beams can be used to trap and control dielectric particles, which also included feedback cooling (Ashkin, 1978, 2006). The nonconservative nature of the radiation-pressure force and the resulting possibility to use it for cooling atomic motion were first pointed out by Hansch and Schawlow (1975) and Wineland and Dehmelt (1975). Laser cooling was subsequently realized experimentally in the 1980s and has since become an extraordinarily important technique (Stenholm, 1986). It has, for example, allowed cooling of ions to their motional ground state and it is the underlying resource for ultracold atom experiments. Many applications have been enabled by laser cooling (Metcalf and van der Straten, 1999), including optical atomic clocks, precision measurements of

the gravitational field, and systematic studies of quantum many-body physics in trapped clouds of atoms (Bloch and Zwerger, 2008).

The role of radiation pressure and its ability to provide cooling for larger objects were already investigated earlier by Braginsky in the context of interferometers. Braginsky considered the dynamical influence of radiation pressure on a harmonically suspended end mirror of a cavity (see Fig. 1). His analysis revealed that the retarded nature of the force, due to the finite cavity lifetime, provides either damping or antidamping of mechanical motion, two effects that he was able to demonstrate in pioneering experiments using a microwave cavity (Braginsky and Manukin, 1967; Braginsky, Manukin, and Tikhonov, 1970). In later experiments, these phenomena were also observed in microwave-coupled kg-scale mechanical resonators (Cuthbertson et al., 1996). Independently, similar physics was explored theoretically for solid-state vibrations (Dykman, 1978). In the optical domain, the first cavity-optomechanical experiment (Dorsel et al., 1983) demonstrated bistability of the radiation-pressure force acting on a macroscopic end mirror.

Braginsky also addressed the fundamental consequences of the quantum fluctuations of radiation pressure and demonstrated that they impose a limit on how accurately the position of a free test mass (e.g., a mirror) can be measured (Braginsky and Manukin, 1977; Braginsky and Khalili, 1995). Detailed analyses by Caves (1980), Jaekel and Renaud (1991), and Pace, Collett, and Walls (1993) clarified the role of this ponderomotive quantum noise in interferometers. These works established the standard quantum limit for continuous

![](images/fc1273e80e98784445fd38e8f974a05ccfb1fd04a8d9b848417389a14d81300a.jpg)

![](images/7e352cefe6b4d4d85440a6b9a45c378dde9cbbc5dafd94129ed0c0e2c2b15fb3.jpg)  
FIG. 1 (color online). Schematic of a generic optomechanical system, both in the optical domain (top), with a laser-driven optical cavity and a vibrating end mirror, and in the microwave domain (bottom), with a vibrating capacitor. Here we depicted a microwave drive entering along a transmission line that is inductively coupled to the  $LC$  circuit representing the microwave resonator.

position detection, which is essential for gravitational wave detectors such as LIGO or VIRGO.

During the 1990s, several aspects of quantum cavity-optomechanical systems started to be explored theoretically. These include squeezing of light (Fabre et al., 1994; Mancini and Tombesi, 1994) and quantum nondemolition (QND) detection of the light intensity (Jacobs et al., 1994; Pinard, Fabre, and Heidmann, 1995), which exploit the effective Kerr nonlinearity generated by the optomechanical interaction. It was also pointed out that for extremely strong optomechanical coupling the resulting quantum nonlinearities could give rise to nonclassical and entangled states of the light field and the mechanics (Bose, Jacobs, and Knight, 1997; Mancini, Man'ko, and Tombesi, 1997). Furthermore, feedback cooling by radiation pressure was suggested (Mancini, Vitali, and Tombesi, 1998). Around the same time, in a parallel development, cavity-assisted laser cooling was proposed as a method to cool the motion of atoms and molecules that lack closed internal transitions (Hechenblaikner et al., 1998; Vuletic and Chu, 2000).

On the experimental side, optical feedback cooling based on the radiation-pressure force was first demonstrated by Cohadon, Heidmann, and Pinard (1999) for the vibrational modes of a macroscopic end mirror. This approach was later taken to much lower temperatures (Kleckner and Bouwmeester, 2006; Poggio et al., 2007). At the same time, there was a trend to miniaturize the mechanical element. For example, the thermal motion of a mm-scale mirror was monitored in a cryogenic optical cavity (Tittonen et al., 1999). Producing high-quality optical Fabry-Pérot cavities below that scale, however, turned out to be very challenging. In spite of this, it was still possible to observe optomechanical effects of retarded radiation forces in microscale setups where the forces were of photothermal origin, effectively replacing the cavity lifetime with a thermal time constant. Examples include demonstration of the optical spring effect (Vogel et al., 2003), feedback damping (Mertz, Marti, and Mlynek, 1993), self-induced oscillations (Zalalutdinov et al., 2001; Hohberger and Karrai, 2004), and cavity cooling due to the dynamical backaction of retarded photothermal light forces (Hohberger-Metzger and Karrai, 2004).

Yet for future applications in quantum coherent optomechanics it is highly desirable to be able to exploit the nondissipative radiation-pressure force. The advent of both optical microcavities and advanced nanofabrication techniques eventually allowed this regime to be entered. In 2005 it was discovered that optical microtoroid resonators with their high optical finesse at the same time contain mechanical modes and thus are able to display optomechanical effects, in particular, radiation-pressure-induced selfoscillations (Carmon et al., 2005; Kippenberg et al., 2005; Rokhsari et al., 2005) (i.e., the effect Braginsky termed "parametric instability"). In 2006 three different teams

demonstrated radiation-pressure cavity cooling, for suspended micromirrors (Arcizet et al., 2006a; Gigan et al., 2006) and for microtoroids (Schliesser et al., 2006). Since then, cavity optomechanics has advanced rapidly and optomechanical coupling has been reported in numerous novel systems. These include membranes (Thompson et al., 2008) and nanorods (Favero et al., 2009) inside Fabry-Pérot resonators, whispering gallery microdisks (Jiang et al., 2009; Wiederhecker et al., 2009) and microspheres (Ma et al., 2007; Park and Wang, 2009; Tomes and Carmon, 2009), photonic crystals (Eichenfield, Camacho et al., 2009; Eichenfield, Chan, Camacho et al., 2009), and evanescently coupled nanobeams (Anetsberger et al., 2009). In addition, cavity optomechanics has been demonstrated for the mechanical excitations of cold atom clouds (Brennecke et al., 2008; Murch et al., 2008). Optomechanical interactions are also present in optical waveguides, as first studied and observed in the context of squeezing, where the confined mechanical modes of fibers lead to guided acoustic-wave scattering (Shelby, Levenson, and Bayer, 1985). Nowadays there are a number of systems where such optomechanical interactions are explored in the absence of a cavity, such as waveguides in photonic circuits or photonic crystal fibers; see, e.g., Li et al. (2008) and Kang et al. (2009). These setups lie somewhat outside the scope of the concepts presented in this review, but we emphasize that they are very promising for applications due to their large bandwidth.

Optomechanical coupling has also been realized using microfabricated superconducting resonators, by embedding a nanomechanical beam inside a superconducting transmission line microwave cavity (Regal, Teufel, and Lehnert, 2008) or by incorporating a flexible aluminum membrane into a lumped element superconducting resonator (Teufel, Li et al., 2011). In these systems the mechanical motion capacitively couples to the microwave cavity. This approach ties cavity optomechanics to an independent development that has been garnering momentum since the late 1990s, which is concerned with measuring and controlling the motion of nanomechanical and micromechanical oscillators using electrical and other nonoptical coupling techniques. Examples include coupling of mechanical oscillators to single-electron transistors (Cleland et al., 2002; LaHaye et al., 2004; Naik et al., 2006) or a quantum point contact (Cleland et al., 2002; Flowers-Jacobs, Schmidt, and Lehnert, 2007). Besides a wealth of possible applications for such devices in sensitive detection (Cleland and Roukes, 1998; LaHaye et al., 2004; Rugar et al., 2004), these methods provide the possibility of realizing mechanical quantum devices (Blencowe, 2005; Ekinci and Roukes, 2005; Schwab and Roukes, 2005) by direct interaction with two-level quantum systems (Cleland and Geller, 2004; Rugar et al., 2004; Wilson-Rae, Zoller, and Imamoglu, 2004; LaHaye et al., 2009; O'Connell et al., 2010; Arcizet et al., 2011; Kolkowitz et al., 2012). For recent comprehensive general reviews of nanomechanical systems (in particular, electromechanical devices), we refer the interested reader to Blencowe (2005), Greenberg, Pashkin, and Ilichev (2012), and Poot and van der Zant (2012).

It should be noted that in atomic systems quantum coherent control of mechanical motion is state of the art since early pioneering experiments with trapped ions [for reviews, see Leibfried et al. (2003), Blatt and Wineland (2008), and Wineland (2013)]. In fact, quantum information processing

TABLE I. The most important symbols and some formulas used in this review.  

<table><tr><td>Symbol</td><td>Meaning</td></tr><tr><td>Ωm</td><td>Mechanical frequency</td></tr><tr><td>Γm</td><td>Mechanical damping rate</td></tr><tr><td>Qm</td><td>Mechanical quality factor Qm = Ωm/Γm</td></tr><tr><td>ωcav</td><td>Cavity resonance frequency</td></tr><tr><td>ωL</td><td>Laser frequency</td></tr><tr><td>Δ</td><td>Laser detuning from the cavity resonance Δ = ωL - ωcav</td></tr><tr><td>κ = κex + κ0</td><td>Overall cavity intensity decay rate, from input (κex) coupling and intrinsic (κ0) losses</td></tr><tr><td>g0</td><td>Optomechanical single-photon coupling strength, inˆint = -hgoa†hat(ˆb + b†)</td></tr><tr><td>g</td><td>Light-enhanced optomechanical coupling for the linearized regime g = g0√n_cav</td></tr><tr><td>G</td><td>Optical frequency shift per displacement G = ∂ω_cav/∂x</td></tr><tr><td>C0</td><td>C0 = 4g02/Γmκ single-photon cooperativity</td></tr><tr><td>C</td><td>C = 4g2/Γmκ = C0n_cav (multiphoton) cooperativity</td></tr><tr><td>Cqu</td><td>Cqu = C/ˆn_th quantum cooperativity</td></tr><tr><td>xZPF</td><td>Mechanical zero-point fluctuation amplitude xZPF = √h/2m_effΩm</td></tr><tr><td>ˆa</td><td>Photon annihilation operator, withˆa†ˆa the circulating photon number</td></tr><tr><td>ˆb</td><td>Phonon annihilation operator, withˆb†ˆb the phonon number</td></tr><tr><td>ˆn</td><td>Average number of phonons stored in the mechanical resonator n = ⟨ˆb†ˆb⟩</td></tr><tr><td>ˆn_th</td><td>Average phonon number in thermal equilibrium n_th = (e^hΩ_m/k_B T - 1)^{-1}</td></tr><tr><td>ˆn_cav</td><td>Photon number circulating inside the cavity n_cav = ⟨ˆa†ˆa⟩</td></tr><tr><td>P</td><td>Incoming laser power</td></tr><tr><td>χopt(ω)</td><td>Optical susceptibility of the cavity χopt(ω) = [κ/2 - i(ω + Δ)]^-1</td></tr><tr><td>χm(ω)</td><td>Mechanical susceptibility χm(ω) = [meff(Ω_m^2 - ω^2) - imeff Γm ω]^-1</td></tr><tr><td>Sxx(ω)</td><td>Quantum noise spectrum Sxx(ω) ≈ ∫-∞+∞ dteiωt{⟨ˆx(t)ˆx(0)⟩ (Sec. II.B.3)}</td></tr><tr><td>Sxx(ω)</td><td>Symmetrized spectral density Sxx(ω) ≈ (Sxx(ω) + Sxx(-ω))/2</td></tr><tr><td>SxxZPF(ω)</td><td>(Symmetrized) mechanical zero-point fluctuations SxxZPF(ω) = h|Imχm(ω)|</td></tr><tr><td>Sadd(xx)(ω) ≥ SZPF(xx)(ω)</td><td>Standard quantum limit result for added noise in displacement measurement (Sec. VI.A)</td></tr><tr><td>Γopt</td><td>Optomechanical damping rate (Sec. V.B.2): max. 4ˆn_cav g02/κ for κ &lt;&lt; Ωm</td></tr><tr><td>δΩm</td><td>Optical spring (mechanical frequency shift, Sec. V.B.1): 2ˆn_cav g02/Δ for κ &lt;&lt; Ωm, |Δ|</td></tr><tr><td>ˆn_min</td><td>Minimum reachable phonon number in laser cooling n_min = (κ/4Ωm)2 for κ &lt;&lt; Ωm</td></tr><tr><td>γ</td><td>Thermal decoherence rate γ ≈ Γmˆn_th</td></tr></table>

in these systems relies on using the quantum states of motion to mediate interactions between distant atomic spins (Cirac and Zoller, 1995). In contrast, the fabricated nanomechanical and micromechanical structures that form the subject of this review extend this level of control to a different realm, one of objects with large masses and devices with a great flexibility in design and the possibility to integrate them in on-chip architectures.

There are several different motivations that drive the rapidly growing interest into cavity optomechanics. On the one hand, there is the highly sensitive optical detection of small forces, displacements, masses, and accelerations. On the other hand, cavity quantum optomechanics promises to manipulate and detect mechanical motion in the quantum regime using light, creating nonclassical states of light and mechanical motion. These tools form the basis for applications in quantum information processing, where optomechanical devices could serve as coherent light-matter interfaces, for example, to interconvert information stored in solid-state qubits into flying photonic qubits. Another example is the ability to build hybrid quantum devices that combine otherwise incompatible degrees of freedoms of different physical systems. At the same time, it offers a route toward fundamental tests of quantum mechanics in a hitherto unaccessible parameter regime of size and mass.

A number of reviews (Kippenberg and Vahala, 2007, 2008; Favero and Karrai, 2009; Genes et al., 2009; Marquardt and Girvin, 2009; Aspelmeyer et al., 2010; Schliesser and Kippenberg, 2010; Aspelmeyer, Meystre, and Schwab,

2012; Cole and Aspelmeyer, 2012; Meystre, 2013) and brief commentary papers (Karrai, 2006; Cleland, 2009; Cole and Aspelmeyer, 2011; Marquardt, 2011) on cavity optomechanics have been published during the past few years, and the topic has also been discussed as part of larger reviews on nanomechanical systems (Greenberg, Pashkin, and Ilichev, 2012; Poot and van der Zant, 2012). Here we aim for a comprehensive treatment that incorporates the most recent advances and points the way toward future challenges.

This review is organized follows: We first discuss optical cavities, mechanical resonators, the basic optomechanical interaction between them, and the large range of experimental setups and parameters that are now available. We then go on to derive the basic consequences of the interaction (such as optomechanical damping and the optical spring effect), describe various measurement schemes, and present the quantum theory of optomechanical cooling. After studying nonlinear effects in the classical regime, we address multimode setups and the wide field of proposed applications in the quantum domain, before concluding with an outlook. A list of symbols and abbreviations is given in Table I.

# II. OPTICAL CAVITIES AND MECHANICAL RESONATORS

In this section we recall the basic aspects of optical cavities and mechanical resonators as needed to describe cavity-optomechanical systems. Much more about these topics can

be found in standard textbooks: for quantum optics, see, e.g., Walls and Milburn (1994), and for nanomechanical systems, see, e.g., Cleland (2003).

# A. Optical resonators

Optical resonators can be realized experimentally in a multitude of forms of which several types will be discussed later in this review. Here we give a unifying description of the optical properties and provide the mathematical description of a cavity that is pumped with a single monochromatic laser source.

# 1. Basic properties

We first consider the classical response of a simple Fabry-Pérot resonator, which will allow one to introduce the relevant parameters to characterize an optical cavity. A Fabry-Pérot resonator or etalon consisting of two highly reflective mirrors, separated by a distance  $L$ , contains a series of resonances which are given by the angular frequency  $\omega_{\mathrm{cav},m} \approx m \cdot \pi (c / L)$ . Here  $m$  is the integer mode number. The separation of two longitudinal resonances is denoted as the free spectral range (FSR) of the cavity:

$$
\Delta \omega_ {\mathrm {F S R}} = \pi \frac {c}{L}. \tag {1}
$$

In the following, we almost always focus on a single optical mode, whose frequency we denote  $\omega_{\mathrm{cav}}$ .

Both the finite mirror transparencies and the internal absorption or scattering out of the cavity lead to a finite photon (intensity) cavity decay rate $^2$ $\kappa$ .

A further useful quantity is the optical finesse  $\mathcal{F}$ , which gives the average number of round-trips before a photon leaves the cavity:

$$
\mathcal {F} \equiv \frac {\Delta \omega_ {\mathrm {F S R}}}{\kappa}. \tag {2}
$$

The optical finesse is a useful parameter as it gives the enhancement of the circulating power over the power that is coupled into the resonator. Alternatively, we can introduce the quality factor of the optical resonator,

$$
Q _ {\text {o p t}} = \omega_ {\text {c a v}} \tau , \tag {3}
$$

where  $\tau = \kappa^{-1}$  is the photon lifetime. Note that the quality factor is also used to characterize the damping rate of mechanical resonators (see Sec. II.B.1). Generally speaking, the cavity decay rate  $\kappa$  can have two contributions, one from losses that are associated with the (useful) input (and output) coupling and a second contribution from the internal losses. It is useful to differentiate these two contributions. For the case of a high- $Q$  cavity, the total cavity loss rate can be written as the sum of the individual contributions:

$$
\kappa = \kappa_ {\mathrm {e x}} + \kappa_ {0}.
$$

Here  $\kappa_{\mathrm{ex}}$  refers to the loss rate associated with the input coupling, and  $\kappa_0$  refers to the remaining loss rate. For example, in the case of a waveguide coupled to a microtoroidal or microsphere resonator,  $\kappa_{\mathrm{ex}}$  is the loss rate associated with the waveguide-resonator interface and  $\kappa_0$  describes the light absorption inside the resonator. For the case of a Fabry-Pérot cavity,  $\kappa_{\mathrm{ex}}$  is the loss rate at the input cavity mirror and  $\kappa_0$  summarizes the loss rate inside the cavity, including transmission losses at the second cavity mirror as well as all scattering and absorption losses behind the first mirror. Note that by splitting the total decay rate into these two contributions, we are assuming that the photons going into the  $\kappa_0$  decay channel will not be recorded. More generally, one could distinguish between more decay channels (e.g., input mirror, output mirror, absorption).

# 2. Input-output formalism for an optical cavity

A quantum mechanical description of a cavity that is coupled to the outside electromagnetic environment can be given via either master equations (if only the internal dynamics is of interest) or a framework known as input-output theory, if one also wants to access the light field being emitted by (or reflected from) the cavity. Input-output theory allows us to directly model the quantum fluctuations injected from any coupling port (such as the input mirror) into the cavity. In addition, it takes into account any coherent laser drive that may be present. For more details beyond the brief discussion provided here, see, e.g., Gardiner and Zoller (2004) and Clerk et al. (2010).

Input-output theory is formulated on the level of Heisenberg equations of motion, describing the time evolution of the field amplitude  $\hat{a}$  inside the cavity. One finds that the amplitude  $\hat{a}$  experiences decay at a rate  $\kappa /2$ . At the same time, its fluctuations are constantly replenished via the quantum noise entering through the various ports of the cavity. In the present case, we distinguish between the channels associated with the input coupling (decay rate  $\kappa_{\mathrm{ex}}$ ) and the other loss processes (overall decay rate  $\kappa_0$ , including loss through the second mirror). The equation of motion reads

$$
\dot {\hat {a}} = - \frac {\kappa}{2} \hat {a} + i \Delta \hat {a} + \sqrt {\kappa_ {\mathrm {e x}}} \hat {a} _ {\mathrm {i n}} + \sqrt {\kappa_ {0}} \hat {f} _ {\mathrm {i n}}. \tag {4}
$$

In the classical case,  $\hat{a}$  would be replaced by a properly normalized complex amplitude of the electric field of the cavity mode under consideration. Indeed, the classical version of this equation (and the following ones) can be obtained by simply taking the average, such that  $\hat{a} \mapsto \langle \hat{a} \rangle$ . We have chosen a frame rotating with the laser frequency  $\omega_{L}$ , i.e.,  $\hat{a}^{\mathrm{orig}} = e^{-i\omega_{L}t}\hat{a}^{\mathrm{here}}$ , and have introduced the laser detuning  $\Delta = \omega_{L} - \omega_{\mathrm{cav}}$  with respect to the cavity mode (see also Sec. III.B). Note that a similar equation can also be given for the mechanical oscillator in order to describe its dissipation and the associated noise force, comprising quantum and thermal contributions (see Sec. II.C).

The input field  $\hat{a}_{\mathrm{in}}(t)$  should be thought of as a stochastic quantum field. In the simplest case, it represents the fluctuating vacuum electric field coupling to the cavity at time  $t$ , plus a coherent laser drive. However, the same formalism can also be used to describe squeezed states or any other more complex field state. The field is normalized in such a way that

$$
P = \hbar \omega_ {L} \langle \hat {a} _ {\mathrm {i n}} ^ {\dagger} \hat {a} _ {\mathrm {i n}} \rangle
$$

is the input power launched into the cavity, i.e.,  $\langle \hat{a}_{\mathrm{in}}^{\dagger}\hat{a}_{\mathrm{in}}\rangle$  is the rate of photons arriving at the cavity (and  $\omega_{\mathrm{cav}}\approx \omega_L$ ). The same kind of description holds for the "unwanted" channel associated with  $\hat{f}_{\mathrm{in}}$ .

According to the input-output theory of open quantum systems, the field that is reflected from the Fabry-Pérot resonator (or coupled back into the coupling waveguide) is given by

$$
\hat {a} _ {\text {o u t}} = \hat {a} _ {\text {i n}} - \sqrt {\kappa_ {\mathrm {e x}}} \hat {a}. \tag {5}
$$

Note that this input-output relation correctly describes the field reflected from the input mirror of a Fabry-Pérot resonator. Equation (5) also describes the transmitted pump field of an evanescently coupled unidirectional waveguide-resonator system, such as a whispering-gallery-mode resonator coupled to a waveguide (Cai, Painter, and Vahala, 2000). In this case the above expression yields the transmitted pump field.

We still have to consider the case of a two-sided cavity, e.g., a two-sided Fabry-Pérot cavity. Other examples in this review include a waveguide coupled to superconducting stripline cavities or fiber-taper coupled photonic crystal defect cavities. In these cases there are both transmitted and reflected fields. In all of these cases there are two options for the description. If the field transmitted through the second mirror is not of interest to the analysis, one may lump the effects of that mirror into the decay rate  $\kappa_0$ , which now represents both internal losses and output coupling through the second mirror. If, however, the field is important, it should be represented by an additional term of the type  $\sqrt{\kappa_{\mathrm{ex}}^{(2)}}\hat{a}_{\mathrm{in}}^{(2)}$  in Eq. (4). Then an equation analogous to Eq. (5) will hold for the output field  $\hat{a}_{\mathrm{out}}^{(2)}$  at that second mirror.

In the following, we are not concerned with noise properties, but focus instead on classical average quantities (for a single-sided cavity), taking the average of Eqs. (4) and (5). We can solve Eq. (4) first for the steady-state amplitude in the presence of a monochromatic laser drive whose amplitude is given by  $\langle \hat{a}_{\mathrm{in}}\rangle$ . Noting that  $\langle \hat{f}_{\mathrm{in}}\rangle = 0$ , we obtain

$$
\langle \hat {a} \rangle = \frac {\sqrt {\kappa_ {\mathrm {e x}}} \left\langle \hat {a} _ {\mathrm {i n}} \right\rangle}{\kappa / 2 - i \Delta}. \tag {6}
$$

The expression linking the input field to the intracavity field<sup>3</sup> is referred to as the optical susceptibility,

$$
\chi_ {\mathrm {o p t}} (\omega) \equiv \frac {1}{- i (\omega + \Delta) + \kappa / 2}.
$$

Here  $\omega$  denotes the Fourier frequency of the fluctuations of the input field around its laser frequency  $\omega_{L}$ . We note that having such a simple Lorentzian response is, of course, an approximation, as it neglects all other cavity resonances. This is adequate as long as the decay rate  $\kappa$  is much smaller than the frequency distance between resonances (free spectral range), which, in particular, means we are dealing with a cavity of high optical  $Q$ . The steady-state cavity population

![](images/2204007b74b6cad1060d4649ba18d4b571e0a612784384f02f64ee7148001f27.jpg)

![](images/efbb6fba9eebcb069ef5063fb0912ae612012de0d97455f27b6b88729a1767af.jpg)

![](images/709aca816971786f0f56790e9736d471ba4e768dba17d071bcb0506f881fdb7b.jpg)

![](images/ddf59e0ab7adfaa17ab4206d68f64a945b36419d455509d2a2233643a2fd1e51.jpg)  
FIG. 2 (color online). Comparison of unidirectionally and bidirectionally coupled cavities and the notion of reflected and transmitted field amplitude. (a) A waveguide-coupled unidirectional resonator [e.g., whispering gallery mode (WGM) cavity coupled to waveguide]. (b) A single-sided cavity coupled in reflection (or a double-sided cavity where the transmission signal is disregarded). (c) A waveguide-coupled bidirectional cavity, which can decay in both forward and backward propagating waveguide modes (i.e., a tapered fiber coupled photonic crystal mode, or a waveguide-coupled quarter-wave stripline resonator). (d) The coupling to a double-sided Fabry-Pérot resonator, in which both transmitted and reflected fields are measured.

$\bar{n}_{\mathrm{cav}} = \langle \hat{a}^{\dagger}\hat{a}\rangle$  , i.e., the average number of photons circulating inside the cavity, is given by

$$
\bar {n} _ {\mathrm {c a v}} = | \langle \hat {a} \rangle | ^ {2} = \frac {\kappa_ {\mathrm {e x}}}{\Delta^ {2} + (\kappa / 2) ^ {2}} \frac {P}{\hbar \omega_ {L}}, \tag {7}
$$

where  $P$  is the input power launched into the cavity, with  $P = \hbar \omega_{L}|\langle \hat{a}_{\mathrm{in}}\rangle |^{2}$ . The reflection or transmission amplitude (for the case of a Fabry-Pérot cavity or a waveguide-coupled resonator, respectively) can be calculated by inserting Eq. (6) into Eq. (5). Using the symbol  $\mathcal{R}$  for the reflection amplitude in the sense of Fig. 2(b), we obtain

$$
\mathcal {R} = \frac {\left\langle \hat {a} _ {\text {o u t}} \right\rangle}{\left\langle \hat {a} _ {\text {i n}} \right\rangle} = \frac {\left(\kappa_ {0} - \kappa_ {\mathrm {e x}}\right) / 2 - i \Delta}{\left(\kappa_ {0} + \kappa_ {\mathrm {e x}}\right) / 2 - i \Delta}. \tag {8}
$$

The square  $|\mathcal{R}|^2$  of this amplitude gives the probability of reflection from the cavity (for Fabry-Pérot) or transmission in the case of a unidirectional waveguide-resonator system. From this expression, several regimes can be differentiated. If the external coupling  $\kappa_{\mathrm{ex}}$  dominates the cavity losses ( $\kappa_{\mathrm{ex}} \approx \kappa \gg \kappa_0$ ), the cavity is called "overcoupled." In that case  $|\mathcal{R}|^2 \approx 1$  and the pump photons emerge from the cavity without having been absorbed or lost via the second mirror (a property that is important as discussed below in the context of quantum limited detection). The case where  $\kappa_0 = \kappa_{\mathrm{ex}}$  refers to the situation of "critical coupling." In this case,

$\mathcal{R}(\Delta = 0) = 0$  on resonance. This implies that the input power is either fully dissipated within the resonator or fully transmitted through the second mirror (in the case of a Fabry-Pérot cavity with  $\kappa_0$  denoting the decay through the second mirror). The situation  $\kappa_{\mathrm{ex}} \ll \kappa_0$  is referred to as "undercoupling" and is associated with cavity losses dominated by intrinsic losses. For many experiments this coupling condition is not advantageous as it leads to an effective loss of information.

The physical meaning of reflection (or transmission) depends sensitively on the experimental realization under consideration. One can distinguish four scenarios, which are outlined in Fig. 2.

# B. Mechanical resonators

# 1. Mechanical normal modes

The vibrational modes of any object can be calculated by solving the equations of the linear theory of elasticity under the appropriate boundary conditions that are determined by the geometry $^{4}$  (Cleland, 2003). This eigenvalue problem yields a set of normal modes and corresponding eigenfrequencies  $\Omega_{(n)}$ . The mechanical displacement patterns associated with mechanical motion are given by the displacement field  $\vec{u}_n(\vec{r})$ , where  $n$  designates the normal mode.

For the purposes of this review, we mostly focus on a single normal mode of vibration of frequency  $\Omega_{m}$  (where  $m$  stands for "mechanical"), assuming that the mode spectrum is sufficiently sparse such that there is no spectral overlap with other mechanical modes. The loss of mechanical energy is described by the (energy) damping rate  $\Gamma_{m}$ , which is related to the mechanical quality factor by  $Q_{m} = \Omega_{m} / \Gamma_{m}$ . If one is interested in the equation of motion for the global amplitude  $x(t)$  of the motion, one can utilize a suitably normalized (see the discussion of the effective mass, below) dimensionless mode function  $\vec{u} (\vec{r},t)$ , such that the displacement field would be  $\vec{u} (\vec{r},t) = x(t)\cdot \vec{u} (\vec{r})$ . Then the temporal evolution of  $x(t)$  can be described by the canonical simple equation of motion of a harmonic oscillator of effective mass  $m_{\mathrm{eff}}$ :

$$
m _ {\text {e f f}} \frac {d x ^ {2} (t)}{d t ^ {2}} + m _ {\text {e f f}} \Gamma_ {m} \frac {d x (t)}{d t} + m _ {\text {e f f}} \Omega_ {m} ^ {2} x (t) = F _ {\text {e x}} (t). \tag {9}
$$

Here  $F_{\mathrm{ex}}(t)$  denotes the sum of all forces that are acting on the mechanical oscillator. In the absence of any external forces, it is given by the thermal Langevin force (see Sec. II.B.3). In Eq. (9) the (energy) damping rate  $\Gamma_{m}$  has been assumed to be frequency independent. Deviations from this model are treated, for example, by Saulson (1990).

A brief remark about the effective mass  $m_{\mathrm{eff}}$  is necessary at this point (Pinard, Hadjar, and Heidmann, 1999; Cleland, 2003). The normalization that has been chosen for the mode function  $\vec{u}(\vec{r})$  affects the normalization of  $x(t)$ . However, it will always be true that the potential energy is given by

$m_{\mathrm{eff}}\Omega_m^2\langle x^2 (t)\rangle /2$  . This value can then be compared to the expression for the potential energy that arises from a calculation according to the theory of elasticity. Demanding them to be equal yields the correct value for the effective mass  $m_{\mathrm{eff}}$  (which therefore is seen to depend on the normalization that was chosen for the mode function). Of course, for the simple case of a center-of-mass oscillation of a solid object, a natural definition of  $x(t)$  is the center-of-mass displacement in which case the effective mass will be the total mass of the object. A treatment of effective mass in optomechanical experiments is given by Pinard, Hadjar, and Heidmann (1999).

Equation (9) can be solved easily, which is best done in frequency space. We introduce the Fourier transform via  $x(\omega) = \int_{-\infty}^{+\infty} dte^{i\omega t} x(t)$ . Then  $x(\omega) = \chi_m(\omega) F_{\mathrm{ex}}(\omega)$  defines the susceptibility  $\chi_m$ , connecting the external force to the response of the coordinate:

$$
\chi_ {m} (\omega) = \left[ m _ {\text {e f f}} \left(\Omega_ {m} ^ {2} - \omega^ {2}\right) - i m _ {\text {e f f}} \Gamma_ {m} \omega \right] ^ {- 1}. \tag {10}
$$

The low-frequency response is given by  $\chi_{m}(0) = (m_{\mathrm{eff}}\Omega_{m}^{2})^{-1} = 1 / k$  where  $k$  is the spring constant.

The quantum mechanical treatment of the mechanical harmonic oscillator leads to the Hamiltonian

$$
\hat {H} = \hbar \Omega_ {m} \hat {b} ^ {\dagger} \hat {b} + \frac {1}{2} \hbar \Omega_ {m}.
$$

Here the phonon creation  $(\hat{b}^{\dagger})$  and annihilation  $(\hat{b})$  operators have been introduced, with

$$
\hat {x} = x _ {\mathrm {Z P F}} (\hat {b} + \hat {b} ^ {\dagger}), \qquad \hat {p} = - i m _ {\mathrm {e f f}} \Omega_ {m} x _ {\mathrm {Z P F}} (\hat {b} - \hat {b} ^ {\dagger}),
$$

where

$$
x _ {\mathrm {Z P F}} = \sqrt {\frac {\hbar}{2 m _ {\mathrm {e f f}} \Omega_ {m}}}
$$

is the zero-point fluctuation amplitude of the mechanical oscillator, i.e., the spread of the coordinate in the ground state  $\langle 0|\hat{x}^2 |0\rangle = x_{\mathrm{ZPF}}^2$ , and where  $|0\rangle$  denotes the mechanical vacuum state. The position and momentum satisfy the commutator relation  $[\hat{x},\hat{p}] = i\hbar$ . The quantity  $\hat{b}^\dagger \hat{b}$  is the phonon number operator, whose average is denoted by  $\bar{n} = \langle \hat{b}^\dagger \hat{b}\rangle$ . In the following, we will typically not explicitly display the contribution  $(1 / 2)\hbar \Omega_m$  of the zero-point energy to the energy of the oscillator.

We briefly discuss the effect of dissipation. If the mechanical oscillator is coupled to a high-temperature bath, the average phonon number will evolve according to

$$
\frac {d}{d t} \bar {n} = - \Gamma_ {m} (\bar {n} - \bar {n} _ {\mathrm {t h}}).
$$

For an oscillator that is initially in the ground state,  $\bar{n} (t = 0) = 0$  , this implies a simple time dependence of the

occupation according to  $\bar{n} (t) = \bar{n}_{\mathrm{th}}(1 - e^{-\Gamma_m t})$  , where  $\bar{n}_{\mathrm{th}}$  is the average phonon number of the environment. Consequently, the rate at which the mechanical oscillator heats out of the ground state is given by

$$
\frac {d}{d t} \bar {n} (t = 0) = \bar {n} _ {\mathrm {t h}} \Gamma_ {m} \approx \frac {k _ {B} T _ {\mathrm {b a t h}}}{\hbar Q _ {m}}.
$$

The latter is often referred to as the thermal decoherence rate and given by the inverse time it takes for one quantum to enter from the environment. In the above expression the high-temperature limit has been taken, i.e.,  $\bar{n}_{\mathrm{th}}\approx k_{B}T_{\mathrm{bath}} / \hbar \Omega_{m}$ . This expression shows that to attain low decoherence a high mechanical  $Q$  factor and a low-temperature bath are important. The change of population of a certain Fock state can be described within the framework of the master equation approach. This approach allows one to calculate the decoherence rate of other quantum states such as a Fock state  $|n\rangle$ . The latter is given by (Gardiner and Zoller, 2004)

$$
(n + 1) \bar {n} _ {\mathrm {t h}} \Gamma_ {m} + n (\bar {n} _ {\mathrm {t h}} + 1) \Gamma_ {m},
$$

revealing that higher Fock states exhibit a progressively higher rate of decoherence.

# 2. Mechanical dissipation

The loss of mechanical excitations, i.e., phonons, is quantified by the energy dissipation rate  $\Gamma_{m} = \Omega_{m} / Q_{m}$ . The origins of mechanical dissipation have been intensively studied over the last decades and comprehensive reviews are given, for example, by Cleland (2003) and Ekinci and Roukes (2005). The most relevant loss mechanisms include the following:

- viscous damping, which is caused by interactions with the surrounding gas atoms or by compression of thin fluidic layers (Vignola et al., 2006; Karabacak, Yakhot, and Ekinci, 2007; Verbridge, Craighead, and Parpia, 2008);  
- clamping losses, which are due to the radiation of elastic waves into the substrate through the supports of the oscillator (Wang, Wong, and Nguyen, 2000; Cross and Lifshitz, 2001; Mattila, 2002; Park and Park, 2004; Photiadis and Judge, 2004; Bindel and Govindjee, 2005; Clark et al., 2005; Judge et al., 2007; Anetsberger et al., 2008; Wilson-Rae, 2008; Eichenfield, Chan, Camacho et al., 2009; Cole et al., 2011; Jockel et al., 2011);  
- fundamental anharmonic effects such as thermoelastic damping and phonon-phonon interactions (Zener, 1938; Lifshitz and Roukes, 2000; Duwel et al., 2006; Kiselev and Iafrate, 2008);  
- materials-induced losses, which are caused by the relaxation of intrinsic or extrinsic defect states in the bulk or surface of the resonator (Yasumura et al., 2000; Mohanty et al., 2002; Southworth et al., 2009; Unterreithmeier, Faust, and Kotthaus, 2010; Venkatesan et al., 2010). Such losses have been successfully described by a phenomenological model involving two-level defect states, which are coupled to the strain via the deformation potential (Anderson, Halperin, and Varma, 1972;

Hunklinger, Arnold, and Stein, 1973; Phillips, 1987; Tielbürger et al., 1992; Seoánez, Guinea, and Castro Neto, 2008; Remus, Blencowe, and Tanaka, 2009). In the context of nanomechanical and micromechanical oscillators the two-level fluctuator damping has been revisited (Seoánez, Guinea, and Castro Neto, 2008; Remus, Blencowe, and Tanaka, 2009).

The various dissipation processes contribute independently to the overall mechanical losses and hence add up incoherently. The resulting mechanical quality factor  $Q_{\mathrm{total}}$  is given by

$$
\frac {1}{Q _ {\text {t o t a l}}} = \sum \frac {1}{Q _ {i}},
$$

where  $i$  labels the different loss mechanisms.

Another helpful quantity is the so-called  $Qf$  product, which plays an important role in the phase noise performance of oscillators. In the context of optomechanics, it quantifies the decoupling of the mechanical resonator from a thermal environment. Specifically,

$$
\frac {\Omega_ {m}}{\bar {n} _ {\mathrm {t h}} \Gamma_ {m}} = Q _ {m} f _ {m} \times \left(\frac {h}{k _ {B} T}\right)
$$

denotes the number of coherent oscillations in the presence of thermal decoherence and evidently scales with  $Qf$ .

# 3. Susceptibility, noise spectra, and fluctuation-dissipation theorem

If one measures the motion of a single harmonic oscillator in thermal equilibrium, one will observe a trajectory  $x(t)$  oscillating at the eigenfrequency  $\Omega_{m}$ . However, due to the influence of both mechanical damping and the fluctuating thermal Langevin force, these oscillations will have a randomly time-varying amplitude and phase [see Fig. 3; see also Giovannetti and Vitali (2001) for a treatment of the quantum regime]. Both amplitude and phase change on the time scale given by the damping time  $\Gamma_{m}^{-1}$ . Such real-time measurements have been performed in optomechanical systems (Hadjar et al., 1999) (see Fig. 4).

In experiments, the mechanical motion is often not analyzed in real time but instead as a noise spectrum in frequency space. This allows one to easily separate the contributions from different normal modes. We briefly recapitulate the relevant concepts. Given one particular realization of the trajectory  $x(t)$  obtained during a measurement time  $\tau$ , we define the gated Fourier transform over a finite time interval  $\tau$ :

![](images/6f388a40ef733a16bf56a943f7403139a6dca327aed7048561b9a90de1ec1aaf.jpg)  
FIG. 3 (color online). Brownian motion (thermal fluctuations) of a nanomechanical resonator in the time domain (schematic), with amplitude and phase fluctuating on a time scale set by the damping time  $\Gamma_{m}^{-1}$ .

![](images/477cda7f846db2cd6750901b149019ace20b43dddaa9e089e6f33de9d7c7af8d.jpg)

![](images/2cf09a9500ff3128e81f975b5c1dcef07127b49c2a2bb6b777470e79599cd7c9.jpg)  
FIG. 4. Brownian motion of a mechanical resonator obtained in an optomechanical setup. The two "quadratures"  $x(t) = X_{1}(t)\cos (\Omega_{m}t) + X_{2}(t)\sin (\Omega_{m}t)$  are displayed in a frame rotating at the angular mechanical resonance frequency  $\Omega_{m}$ , such that the unperturbed undamped motion would correspond to a stationary single point existing somewhere in phase space. The fluctuations are a consequence of the thermal Brownian motion [figure courtesy of A. Heidmann; see also (Hadjar et al. (1999)].

$$
\tilde {x} (\omega) = \frac {1}{\sqrt {\tau}} \int_ {0} ^ {\tau} x (t) e ^ {i \omega t} d t. \tag {11}
$$

Averaging over independent experimental runs, we obtain the spectral density  $\langle |\tilde{x} (\omega)|^2\rangle$ . The definition adopted in Eq. (11), with the prefactor  $1 / \sqrt{\tau}$ , ensures that the spectral density has a well-defined limiting value for  $\tau \rightarrow \infty$ , where the Wiener-Khinchin theorem connects this to the Fourier transform  $S_{xx}(\omega)$  of the autocorrelation function, also called the noise power spectral density. The latter is defined as

$$
S _ {x x} (\omega) \equiv \int_ {- \infty} ^ {+ \infty} \langle x (t) x (0) \rangle e ^ {i \omega t} d t, \tag {12}
$$

and the theorem states

$$
\lim  _ {\tau \rightarrow \infty} \langle | \tilde {x} (\omega) | ^ {2} \rangle = S _ {x x} (\omega). \tag {13}
$$

The important assumptions made here are that the process is stationary and is of finite intensity (Gillespie, 1996). From Eqs. (12) and (13), we immediately obtain the important result that the area under the experimentally measured mechanical noise spectrum yields the variance of the mechanical displacement  $\langle x^2\rangle$ :

![](images/c48df443510564506b0e63feb20eb6e4dddf7cb55c854c3828f4febed0833a54.jpg)  
FIG. 5 (color online). Noise spectrum of a damped harmonic oscillator in thermal equilibrium (symmetric for  $\omega \mapsto -\omega$  in the classical limit  $k_{B}T \gg \hbar \omega$ ).

$$
\int_ {- \infty} ^ {+ \infty} S _ {x x} (\omega) \frac {d \omega}{2 \pi} = \langle x ^ {2} \rangle . \tag {14}
$$

Furthermore, in thermal equilibrium, the fluctuation-dissipation theorem (FDT) relates the noise to the dissipative part of the linear response,

$$
S _ {x x} (\omega) = 2 \frac {k _ {B} T}{\omega} \operatorname {I m} \chi_ {m} (\omega), \tag {15}
$$

where  $\chi_{m}(\omega)$  denotes the mechanical susceptibility introduced above and we have treated the high-temperature (classical) case. For weak damping  $(\Gamma_{m}\ll \Omega_{m})$  , this gives rise to Lorentzian peaks of width  $\Gamma_{m}$  in the noise spectrum, located at  $\omega = \pm \Omega_{m}$  see Fig.5). Integration of  $S_{xx}(\omega)$  according to Eq. (14) yields the variance, which for weak damping is set by the equipartition theorem  $\langle x^2\rangle = k_BT / m_{\mathrm{eff}}\Omega_m^2$

In the quantum regime, the natural generalization of Eq. (12) contains the product of Heisenberg time-evolved operators  $\langle \hat{x}(t)\hat{x}(0)\rangle$ , which do not commute. As a consequence, the spectrum  $S_{xx}(\omega)$  is asymmetric in frequency. The quantum FDT

$$
S _ {x x} (\omega) = \frac {2 \hbar}{1 - e ^ {- \hbar \omega / k _ {B} T}} \operatorname {I m} \chi_ {x x} (\omega) \tag {16}
$$

implies that  $S_{xx}(\omega) = 0$  for  $\omega < 0$  at  $T = 0$ . Our discussion of dynamical backaction cooling (Sec. VII.A) mentions that this means the  $T = 0$  bath is not able to supply energy, as there are no thermal excitations. In this review we also consider the symmetrized noise spectrum  $\bar{S}_{xx}(\omega) = \{S_{xx}(\omega) + S_{xx}(-\omega)\} /2$ . For more on noise spectra, see Clerk et al. (2010).

# III. PRINCIPLES OF OPTOMECHANICAL COUPLING

# A. The radiation-pressure force and optomechanical coupling

In our discussion the fundamental mechanism that couples the properties of the cavity radiation field to the mechanical motion is the momentum transfer of photons, i.e., radiation pressure. The simplest form of radiation-pressure coupling is the momentum transfer due to reflection that occurs in a Fabry-Pérot cavity. A single photon transfers the momentum  $|\Delta p| = 2h / \lambda$  ( $\lambda$  is the photon wavelength). As a consequence the radiation-pressure force is given by

$$
\langle \hat {F} \rangle = 2 \hbar k \frac {\langle \hat {a} ^ {\dagger} \hat {a} \rangle}{\tau_ {c}} = \hbar \frac {\omega_ {\mathrm {c a v}}}{L} \langle \hat {a} ^ {\dagger} \hat {a} \rangle . \tag {17}
$$

Here  $\tau_{c} = 2L / c$  denotes the cavity round-trip time. Therefore,  $\hbar \omega_{\mathrm{cav}} / L$  describes the radiation-pressure force caused by one intracavity photon. The parameter  $G = \omega_{\mathrm{cav}} / L$  which appears in this expression also describes the change of cavity resonance frequency with position, i.e., the frequency pull parameter. In Sec. III.B, which introduces a Hamiltonian description of the interaction between a movable mirror and optical cavity, this relation will be derived in its full generality.

More generally, the optomechanical coupling can arise, for example, by direct momentum transfer via reflection (Fabry-Pérot-type cavities with a movable end mirror, microtoroids), by coupling via a dispersive shift of the cavity frequency (membrane in the middle, levitated nano-objects trapped inside the cavity) or by optical near-field effects (e.g., nanoobjects in the evanescent field of a resonator or a waveguide just above a substrate).

Various radiation-pressure forces have been investigated in the pioneering work of Ashkin (2006), who first demonstrated that small dielectric particles can be trapped in laser light. The relevant forces are generally referred to as gradient (or dipole) forces, as the force arises from the gradient of the laser field intensity. The particle is attracted to the center of the Gaussian trapping laser beam. If  $\vec{E} (\vec{r})$  denotes the laser electric field distribution, the time-averaged dielectric energy of the particle in the field is given by

$$
U = - \frac {1}{2} \vec {p} \cdot \vec {E} = - \frac {1}{2} \alpha | \vec {E} (\vec {r}) | ^ {2}
$$

(with  $\alpha$  the polarizability), which correspondingly yields a force  $\vec{F} = -\vec{\nabla} U$ . In addition to the gradient force, scattering forces occur for a traveling wave. These forces scale with  $|\vec{k}|$ , i.e., the wave number of the electromagnetic radiation, in contrast to the gradient forces. In addition there is also a contribution from the strain-optical effect, i.e., the strain-dependent polarizability. The strain-optical coupling is the dominant coupling mechanism in guided acoustic-wave scattering (Shelby, Levenson, and Bayer, 1985; Locke et al., 1998). Independent of the physical interpretation of the force, however, the optomechanical interaction in an optomechanical system can always be derived by considering the cavity resonance frequency shift as a function of displacement (i.e., the "dispersive" shift). This is the basis for our Hamiltonian description adopted in Sec. III.B.

Micromechanical systems are also subject to radiation forces based on thermal effects. Absorption of light can heat a structure and deform it, which corresponds to the action of a force (e.g., in an asymmetric, bimorph structure, including materials of different thermal expansion). These photothermal forces can in many ways lead to effects similar to retarded radiation-pressure forces, with the thermal relaxation time of the structure replacing the cavity photon lifetime. However, since such forces are based on absorption of light, they cannot form the basis for future fully coherent quantum optomechanical setups, since at least the coherence of the light field is thereby irretrievably lost.

# B. Hamiltonian formulation

The starting point of all our subsequent discussions is the Hamiltonian describing the coupled system of a radiation mode interacting with a vibrational mode (Fig. 1). For brevity we refer to the radiation field as "optical," even though the important case of microwave setups is included here as well.

We focus on the simplest possible model system in cavity optomechanics, which has been used to successfully describe most of the experiments to date. In this model, we restrict our attention to one of the many optical modes, i.e., the one closest to resonance with the driving laser. Moreover, we also describe only one of the many mechanical normal modes. This is mostly arbitrary, as the displacement frequency spectrum will show peaks at any of the mechanical resonances. Still, as long as the dynamics is linear with independently evolving normal modes, the model will provide a valid approximation. In some cases, such as sideband-resolved cooling, it may be possible to experimentally select a particular mechanical mode by adjusting the laser detuning, whereas in other cases, such as nonlinear dynamics, an extended description involving several mechanical modes may become crucial.

The uncoupled optical  $(\omega_{\mathrm{cav}})$  and mechanical  $(\Omega_m)$  modes are represented by two harmonic oscillators, which is typically an excellent approximation at the displacements generated in the experiments:

$$
\hat {H} _ {0} = \hbar \omega_ {\mathrm {c a v}} \hat {a} ^ {\dagger} \hat {a} + \hbar \Omega_ {m} \hat {b} ^ {\dagger} \hat {b}. \tag {18}
$$

In the case of a cavity with a movable end mirror the coupling of optical and mechanical modes is parametric, i.e., the cavity resonance frequency is modulated by the mechanical amplitude<sup>7</sup>:

$$
\omega_ {\mathrm {c a v}} (x) \approx \omega_ {\mathrm {c a v}} + x \partial \omega_ {\mathrm {c a v}} / \partial x + \dots .
$$

For most experimental realizations discussed in this review, it suffices to keep the linear term, where we define the optical frequency shift per displacement as  $G = -\partial \omega_{\mathrm{cav}} / \partial x$  (but see Sec. VI.B.2 for a different example). A more detailed derivation of the optomechanical Hamiltonian can be found in an early paper (Law, 1995).

We mention that other coupling mechanisms have been discussed. For example, the transparency of a moving Bragg mirror, and hence  $\kappa$ , can depend on its velocity (Karrai, Favero, and Metzger, 2008). More generally, the displacement may couple to the external cavity decay rate, yielding  $\kappa_{\mathrm{ex}} = \kappa_{\mathrm{ex}}(x)$ . This case (sometimes termed "dissipative coupling," although it refers to the external coupling channel), which is of practical relevance in some setups (Li, Pernice, and Tang, 2009c), can lead to novel physical effects, e.g., in cooling (Elste, Girvin, and Clerk, 2009).

For a simple cavity of length  $L$ , we have  $G = \omega_{\mathrm{cav}} / L$ . The sign reflects the fact that we take  $x > 0$  to indicate an

increase in cavity length, leading to a decrease in  $\omega_{\mathrm{cav}}(x)$  if  $G > 0$ . In general, expanding to leading order in the displacement, we have

$$
\hbar \omega_ {\mathrm {c a v}} (x) \hat {a} ^ {\dagger} \hat {a} \approx \hbar (\omega_ {\mathrm {c a v}} - G \hat {x}) \hat {a} ^ {\dagger} \hat {a}. \tag {19}
$$

Here  $\hat{x} = x_{\mathrm{ZPF}}(\hat{b} + \hat{b}^{\dagger})$  as defined before. Thus, the interaction part of the Hamiltonian can be written

$$
\hat {H} _ {\text {i n t}} = - \hbar g _ {0} \hat {a} ^ {\dagger} \hat {a} (\hat {b} + \hat {b} ^ {\dagger}), \tag {20}
$$

where

$$
g _ {0} = G x _ {\mathrm {Z P F}} \tag {21}
$$

is the vacuum optomechanical coupling strength, expressed as a frequency. It quantifies the interaction between a single phonon and a single photon. We stress that, generally speaking,  $g_{0}$  is more fundamental than  $G$ , since  $G$  is affected by the definition of the displacement that is to some extent arbitrary for more complicated mechanical normal modes (see the discussion in Sec. II.B.1). Therefore, in the following we almost always refer to  $g_{0}$ . Later, we also mention  $g$ , which is an often-used measure for the effective optomechanical coupling in the linearized regime. It is enhanced compared to  $g_{0}$  by the amplitude of the photon field. The Hamiltonian reveals that the interaction of a movable mirror with the radiation field is fundamentally a nonlinear process, involving three operators (three-wave mixing).

The radiation-pressure force is simply the derivative of  $\hat{H}_{\mathrm{int}}$  with respect to displacement:

$$
\hat {F} = - \frac {d \hat {H} _ {\mathrm {i n t}}}{d \hat {x}} = \hbar G \hat {a} ^ {\dagger} \hat {a} = \hbar \frac {g _ {0}}{x _ {\mathrm {Z P F}}} \hat {a} ^ {\dagger} \hat {a}. \tag {22}
$$

The full Hamiltonian  $\hat{H}$  also includes terms that describe dissipation (photon decay and mechanical friction), fluctuations (influx of thermal phonons), and driving by an external laser. These effects are formulated most efficiently using the equations of motion and the input-output formalism (see Sec. II.A.2, and also Sec. III.C). Here we remark that it is convenient to change the description of the optical mode by switching to a frame rotating at the laser frequency  $\omega_{L}$ . Applying the unitary transformation  $\hat{U} = \exp (i\omega_{L}\hat{a}^{\dagger}\hat{a} t)$  makes the driving terms time independent, $^{8}$  and generates a new Hamiltonian  $\hat{H} = \hat{U}\hat{H}_{\mathrm{old}}\hat{U}^{\dagger} - i\hbar \hat{U}\partial \hat{U}^{\dagger} / \partial t$  of the form

$$
\hat {H} = - \hbar \Delta \hat {a} ^ {\dagger} \hat {a} + \hbar \Omega_ {m} \hat {b} ^ {\dagger} \hat {b} - \hbar g _ {0} \hat {a} ^ {\dagger} \hat {a} (\hat {b} + \hat {b} ^ {\dagger}) + \dots , \tag {23}
$$

where

$$
\Delta = \omega_ {L} - \omega_ {\mathrm {c a v}} \tag {24}
$$

is the laser detuning introduced already in Sec. II.A.2, and where we omitted (the ellipsis) driving, decay, and fluctuation terms, which are discussed below employing input-output theory (Sec. III.C). In particular, the driving term

reads  $\hat{H}_{\mathrm{drive}} = i\hbar \sqrt{\kappa_{\mathrm{ex}}}\hat{a}^{\dagger}\alpha_{\mathrm{in}} + \mathrm{H.c.}$ , for a laser of amplitude  $\alpha_{\mathrm{in}}$ . Equation (23) is the frequently used starting point in cavity optomechanics.

We now introduce the so-called "linearized" approximate description of cavity optomechanics. To this end, we split the cavity field into an average coherent amplitude  $\langle \hat{a}\rangle = \bar{\alpha}$  and a fluctuating term

$$
\hat {a} = \bar {\alpha} + \delta \hat {a}. \tag {25}
$$

Then the interaction part of the Hamiltonian

$$
\hat {H} _ {\text {i n t}} = - \hbar g _ {0} (\bar {\alpha} + \delta \hat {a}) ^ {\dagger} (\bar {\alpha} + \delta \hat {a}) (\hat {b} + \hat {b} ^ {\dagger}) \tag {26}
$$

may be expanded in powers of  $\bar{\alpha}$ . The first term  $-\hbar g_0|\bar{\alpha}|^2 (\hat{b} + \hat{b}^\dagger)$  indicates the presence of an average radiation-pressure force  $\bar{F} = \hbar G|\bar{\alpha}|^2$ . It may be omitted after implementing an appropriate shift of the displacement's origin by  $\delta \bar{x} = \bar{F} / m_{\mathrm{eff}}\Omega_m^2$  and afterward always using a modified detuning  $\Delta_{\mathrm{new}} \equiv \Delta_{\mathrm{old}} + G\delta \bar{x}$ . The second term, of order  $|\bar{\alpha}|^1$ , is the one we keep:

$$
- \hbar g _ {0} \left(\bar {\alpha} ^ {*} \delta \hat {a} + \bar {\alpha} \delta \hat {a} ^ {\dagger}\right) (\hat {b} + \hat {b} ^ {\dagger}). \tag {27}
$$

The third term  $-\hbar g_0\delta \hat{a}^\dagger \delta \hat{a}$  is omitted as being smaller by a factor  $|\bar{\alpha}|$ . Without loss of generality, we now assume  $\bar{\alpha} = \sqrt{\bar{n}_{\mathrm{cav}}}$  as real valued. Thus, the Hamiltonian in the rotating frame reads

$$
\hat {H} \approx - \hbar \Delta \delta \hat {a} ^ {\dagger} \delta \hat {a} + \hbar \Omega_ {m} \hat {b} ^ {\dagger} \hat {b} + \hat {H} _ {\text {i n t}} ^ {(\mathrm {l i n})} + \dots , \tag {28}
$$

where the quadratic interaction part

$$
\hat {H} _ {\text {i n t}} ^ {(\mathrm {l i n})} = - \hbar g _ {0} \sqrt {\bar {n} _ {\mathrm {c a v}}} (\delta \hat {a} ^ {\dagger} + \delta \hat {a}) (\hat {b} + \hat {b} ^ {\dagger}) \tag {29}
$$

is referred to as linearized, since the resulting coupled equations of motion are linear in this approximation. Note that the remaining terms in Eq. (28) no longer contain the laser driving, as that has already been taken care of by the shift implemented in Eq. (25). In the literature up to now, the combination

$$
g = g _ {0} \sqrt {\bar {n} _ {\mathrm {c a v}}} \tag {30}
$$

is often referred to as "the optomechanical coupling strength." Obviously, it depends on the laser intensity and is thus less fundamental than the single-photon coupling  $g_{0}$  (obtained for  $\bar{n}_{\mathrm{cav}} = 1$ ).

The linearized description can be good even if the average photon number circulating inside the cavity is not large. This is because the mechanical system may not be able to resolve the individual photons if the decay rate  $\kappa$  is sufficiently large. The detailed conditions for the linearized approximation to be valid may depend on the questions that are asked. We return to this question in Sec. X.F.

We briefly note that  $g > \kappa$  is one necessary condition for the so-called "strong-coupling" regime of cavity optomechanics, where the mechanical oscillator and the driven optical mode hybridize (Sec. VII.C). A much more challenging condition is to have  $g_0 > \kappa$ , i.e., the single-photon optomechanical coupling rate exceeding the cavity decay rate. In the latter regime, nonlinear quantum effects become observable (see Sec. X.F).

Depending on the detuning, three different regimes can be distinguished with respect to the interaction (29), especially in the sideband-resolved regime ( $\kappa \ll \Omega_{m}$ , which we assume in the remainder of this section). For  $\Delta \approx -\Omega_{m}$  (red-detuned regime), we have two harmonic oscillators of (nearly) equal frequency that can interchange quanta: the mechanical oscillator and the driven cavity mode. The terms in the interaction Hamiltonian describing this process are the following:

$$
- \hbar g \left(\delta \hat {a} ^ {\dagger} \hat {b} + \delta \hat {a} \hat {b} ^ {\dagger}\right). \tag {31}
$$

In contrast, we may omit those terms that create or destroy two quanta at the same time ( $\delta \hat{a}^{\dagger}\hat{b}^{\dagger}$  and  $\delta \hat{a}\hat{b}$ ), because they are strongly "nonresonant," i.e., applying those terms to a state changes the total energy by an amount much larger than the coupling. Keeping only the resonant terms of Eq. (31) is known as the rotating-wave approximation (RWA). The case  $\Delta \approx -\Omega_{m}$  is the one relevant for cooling (transferring all thermal phonons into the cold photon mode, Sec. VII.A) and for quantum state transfer between light and mechanics (Sec. X). In the quantum optical domain, Eq. (31) is referred to as a "beam-splitter" interaction.

For  $\Delta \approx +\Omega_{m}$  (blue-detuned regime), the dominant terms in the RWA

$$
- \hbar g \left(\delta \hat {a} ^ {\dagger} \hat {b} ^ {\dagger} + \delta \hat {a} \hat {b}\right) \tag {32}
$$

represent a "two-mode squeezing" interaction that lies at the heart of parametric amplification (Clerk et al., 2010). In the absence of dissipation, this leads to an exponential growth of the energies stored in both the vibrational mode and the driven optical mode, with strong quantum correlations between the two. Thus, it may be used for efficiently entangling both modes (Sec. X). Focusing on the mechanical mode alone, the growth of energy can be interpreted as "antidamping" or amplification (Sec. V.B.2). If the intrinsic dissipation is low enough, this behavior may trigger a dynamical instability that leads to self-induced mechanical oscillations. The resulting features are discussed in Sec. VIII.

Finally, when  $\Delta = 0$ , the interaction

$$
- \hbar g \left(\delta \hat {a} ^ {\dagger} + \delta \hat {a}\right) \left(\hat {b} + \hat {b} ^ {\dagger}\right) \tag {33}
$$

means that the mechanical position  $\hat{x} \propto \hat{b} + \hat{b}^{\dagger}$  leads to a phase shift of the light field, which is the situation encountered in optomechanical displacement detection (Sec. VI). In addition, this interaction Hamiltonian can be viewed as implementing QND detection of the optical amplitude quadrature  $\delta \hat{a} + \delta \hat{a}^{\dagger}$ , since that operator commutes with the full Hamiltonian in this case.

# C. Optomechanical equations of motion

The mechanical motion induces a shift of the optical resonance frequency, which in turn results in a change of circulating light intensity and, therefore, of the radiation-pressure force acting on the motion. This kind of feedback loop is known as optomechanical "backaction" (see Fig. 15). The finite cavity decay rate  $\kappa$  introduces some retardation

![](images/464c60c712861a73fcf4a3632d38cb65064415f5e771be609c685d2e640841cf.jpg)  
FIG. 6 (color online). Optomechanical (linearized) interaction between a driven optical mode and a mechanical resonator.

between the motion and the resulting changes of the force, hence the term "dynamical" backaction.

A convenient starting point for the analytical treatment of the radiation-pressure dynamical backaction phenomena (Secs. V.B and VII) is the input-output formalism. This formalism (briefly introduced in Sec. II.A.2) provides us with equations of motion for the cavity field amplitude  $\hat{a}$  and, analogously, for the mechanical amplitude  $\hat{b}$ . These equations have the form of quantum Langevin equations, since both the light amplitude and the mechanical motion are driven by noise terms that comprise the vacuum noise and any thermal noise entering the system:

$$
\dot {\hat {a}} = - \frac {\kappa}{2} \hat {a} + i (\Delta + G \hat {x}) \hat {a} + \sqrt {\kappa_ {\mathrm {e x}}} \hat {a} _ {\mathrm {i n}} + \sqrt {\kappa_ {0}} \hat {f} _ {\mathrm {i n}}, \tag {34}
$$

$$
\dot {\hat {b}} = \left(- i \Omega_ {m} - \frac {\Gamma_ {m}}{2}\right) \hat {b} + i g _ {0} \hat {a} ^ {\dagger} \hat {a} + \sqrt {\Gamma_ {m}} \hat {b} _ {\text {i n}}. \tag {35}
$$

See Sec. II.A.2 for remarks on the input-output treatment and the optical decay rates  $\kappa, \kappa_{\mathrm{ex}}, \kappa_0$ . With regard to the damping term  $-\Gamma_m / 2$  for the mechanical dissipation, we note that this treatment is correct as long as  $\Omega_m \gg \Gamma_m$ . Otherwise the equations would have to be formulated on the level of the displacement  $\hat{x}$ , with a damping force  $-m_{\mathrm{eff}} \Gamma_m \dot{\hat{x}}$ .

The noise correlators associated with the input fluctuations are given by

$$
\langle \hat {a} _ {\mathrm {i n}} (t) \hat {a} _ {\mathrm {i n}} ^ {\dagger} \left(t ^ {\prime}\right) \rangle = \delta \left(t - t ^ {\prime}\right), \tag {36}
$$

$$
\left\langle \hat {a} _ {\mathrm {i n}} ^ {\dagger} (t) \hat {a} _ {\mathrm {i n}} \left(t ^ {\prime}\right) \right\rangle = 0, \tag {37}
$$

$$
\left\langle \hat {b} _ {\mathrm {i n}} (t) \hat {b} _ {\mathrm {i n}} ^ {\dagger} \left(t ^ {\prime}\right) \right\rangle = \left(\bar {n} _ {\mathrm {t h}} + 1\right) \delta \left(t - t ^ {\prime}\right), \tag {38}
$$

$$
\left\langle \hat {b} _ {\mathrm {i n}} ^ {\dagger} (t) \hat {b} _ {\mathrm {i n}} \left(t ^ {\prime}\right) \right\rangle = \bar {n} _ {\mathrm {t h}} \delta \left(t - t ^ {\prime}\right). \tag {39}
$$

The correlators for  $\hat{f}_{\mathrm{in}}$  look like those for  $\hat{a}_{\mathrm{in}}$  listed above. Here we assumed that the optical field has zero thermal occupation ( $k_{B}T / \hbar \omega_{\mathrm{cav}} \approx 0$ ), which is an approximation that is valid for optical fields at room temperature, although it may fail for the case of microwave fields, unless the setup is cooled to sufficiently low temperatures. In contrast, the mechanical degree of freedom is typically coupled to a hot environment, with an average number of quanta given by  $\bar{n}_{\mathrm{th}} \approx k_{B}T / \hbar \Omega_{m} \gg 1$ . Together with these correlators, the quantum Langevin equations describe the evolution of the

![](images/553ed4f74330864f429e91332bd1de1532c8b196e9e35437946514d1818e5fa7.jpg)  
FIG. 7 (color online). A gallery illustrating the variety of optomechanical devices, arranged according to mass. Pictures courtesy (from top left, down): N. Mavalvala, A. Heidmann, M. Aspelmeyer, D. Bouwmeester, J. Harris, P. Treutlein, T. J. Kippenberg, I. Favero, M. Lipson, T. J. Kippenberg/E. Weig/J. Kotthaus, H. Tang, K. Vahala/T. Carmon, J. Teufel/K. Lehnert, I. Robert, O. Painter, O. Painter, I. Favero/E. Weig/K. Karrai, and D. Stamper-Kurn.

optical cavity field and the mechanical oscillator, including all fluctuation effects.

It is equally useful to give the classical, averaged version of these equations that will be valid for sufficiently large photon and phonon numbers, in the semiclassical limit. Then we can write down the equations for the complex light amplitude  $\alpha(t) = \langle \hat{a}(t) \rangle$  and the oscillator position  $x(t) = \langle \hat{x}(t) \rangle$ :

$$
\dot {\alpha} = - \frac {\kappa}{2} \alpha + i (\Delta + G x) \alpha + \sqrt {\kappa_ {\mathrm {e x}}} \alpha_ {\mathrm {i n}}, \tag {40}
$$

$$
m _ {\text {e f f}} \ddot {x} = - m _ {\text {e f f}} \Omega_ {m} ^ {2} x - m _ {\text {e f f}} \Gamma_ {m} \dot {x} + \hbar G | \alpha | ^ {2}. \tag {41}
$$

Here we neglected all fluctuations, although these could be added to describe thermal and even, in a semiclassical approximation, quantum noise forces. The term  $\alpha_{\mathrm{in}}$  represents the laser drive. Note that we also chose to write the mechanical equation of motion in terms of the displacement, where  $x = 2x_{\mathrm{ZPF}}\mathrm{Re}(\langle \hat{b}\rangle)$ . This becomes equivalent to the equation given above only for weak damping  $\Gamma_m \ll \Omega_m$ . These fully nonlinear coupled differential equations are the basis for our discussion of nonlinear phenomena, in particular, the optomechanical parametric instability (also called "self-induced oscillations" or "mechanical lasing," see Sec. VIII).

The equations of motion (34) and (35) (and likewise their classical versions) are inherently nonlinear as they contain the product of the mechanical oscillator amplitude and the cavity field [Eq. (34)] or the radiation-pressure force  $\propto \hat{a}^{\dagger}\hat{a}$  that is quadratic in photon operators [Eq. (35)]. While they can still be solved numerically in the classical case, for the quantum regime they are of purely formal use and in practice cannot be solved exactly, either analytically or numerically. However, in many situations that we encounter it is permissible to linearize this set of equations around some steady-state solution, setting  $\hat{a} = \bar{\alpha} +\delta \hat{a}$ . Using  $\bar{\alpha} = \sqrt{\bar{n}_{\mathrm{cav}}}$  and keeping only the linear terms, we find the following set of coupled linear equations of motion:

$$
\begin{array}{l} \delta \dot {\hat {a}} = \left(i \Delta - \frac {\kappa}{2}\right) \delta \hat {a} + i g (\hat {b} + \hat {b} ^ {\dagger}) + \sqrt {\kappa_ {\mathrm {e x}}} \delta \hat {a} _ {\mathrm {i n}} (t) + \sqrt {\kappa_ {0}} \hat {f} _ {\mathrm {i n}} (t), (42) \\ \dot {\hat {b}} = \left(- i \Omega_ {m} - \frac {\Gamma_ {m}}{2}\right) \hat {b} + i g \left(\delta \hat {a} + \delta \hat {a} ^ {\dagger}\right) + \sqrt {\Gamma_ {m}} \hat {b} _ {\mathrm {i n}} (t). (43) \\ \end{array}
$$

These correspond to what one would have obtained alternatively by employing the "linearized" coupling Hamiltonian of Eq. (29) and then applying input-output theory. Here we have (as is common practice) redefined the origin of the mechanical oscillations to take into account the constant displacement  $\hbar G|\alpha|^2 /m_{\mathrm{eff}}\Omega_m^2$  that is induced by the average radiation-pressure force. It is evident that now the mutual coupling terms between the optical and mechanical degrees of freedom are linear in the field operators, and that the strength is set by the field-enhanced coupling rate  $g = g_0\sqrt{\bar{n}_{\mathrm{cav}}}$ .

As shown in later sections, these linearized equations are able to fully describe several phenomena, including optomechanical cooling, amplification, and parametric normal-mode splitting (i.e., strong, coherent coupling). They can be solved analytically, which is best performed in the frequency domain (see Sec. V.B).

For completeness, we display the linearized quantum equations in frequency space:

$$
\begin{array}{l} - i \omega \delta \hat {a} [ \omega ] = \left(i \Delta - \frac {\kappa}{2}\right) \delta \hat {a} [ \omega ] + i g [ \hat {b} [ \omega ] + (\hat {b} ^ {\dagger}) [ \omega ] ] \\ + \sqrt {\kappa_ {\mathrm {e x}}} \delta \hat {a} _ {\mathrm {i n}} [ \omega ] + \sqrt {\kappa_ {0}} \hat {f} _ {\mathrm {i n}} [ \omega ], \tag {44} \\ \end{array}
$$

$$
\begin{array}{l} - i \omega \hat {b} [ \omega ] = \left(- i \Omega_ {m} - \frac {\Gamma_ {m}}{2}\right) \hat {b} [ \omega ] + i g [ \delta \hat {a} [ \omega ] + (\delta \hat {a} ^ {\dagger}) [ \omega ] ] \\ + \sqrt {\Gamma_ {m}} \hat {b} _ {\mathrm {i n}} [ \omega ]. \tag {45} \\ \end{array}
$$

![](images/5e8e24753ff5584c4e1b4a76502230bf00caa79d5e5ea3303461a85980522874.jpg)  
FIG. 8 (color online). Schematic representation of the radiation modes (mode shape indicated) and vibrational degrees of freedom (vibrations indicated by gray lines) involved in several of the most common types of setups (from left to right, and top to bottom): a suspended mirror, a microtoroid, a nano-object (or a membrane) inside an optical cavity, localized modes in a photonic crystal nanobeam, a trapped and vibrating cold atom cloud (or other levitated object) inside a cavity, and a vibrating drum capacitor coupled to a microwave field.

Here  $\hat{b}[\omega] = \int_{-\infty}^{+\infty} dt e^{i\omega t} \hat{b}(t)$  is the Fourier transform of  $\hat{b}$ . Note the important relation  $(\hat{b}^{\dagger})[\omega] = (\hat{b}[-\omega])^{\dagger}$ , which has to be taken care of while solving the equations.

It is equally useful to consider the linearized version of the classical equations of motion for the light amplitude  $[\alpha(t) = \bar{\alpha} + \delta \alpha]$  and the displacement, Eqs. (40) and (41):

$$
\delta \dot {\alpha} = \left(i \Delta - \frac {\kappa}{2}\right) \delta \alpha + i G \bar {\alpha} x, \tag {46}
$$

$$
m _ {\text {e f f}} \ddot {x} = - m _ {\text {e f f}} \Omega_ {m} ^ {2} x - m _ {\text {e f f}} \Gamma_ {m} \dot {x} + \hbar G (\bar {\alpha} ^ {*} \delta \alpha + \bar {\alpha} \delta \alpha^ {*}). \tag {47}
$$

Finally, we display them in frequency space, in the form that we employ in Sec. V.B:

$$
- i \omega \delta \alpha [ \omega ] = \left(i \Delta - \frac {\kappa}{2}\right) \delta \alpha [ \omega ] + i G \bar {\alpha} x [ \omega ], \tag {48}
$$

$$
\begin{array}{l} - m _ {\mathrm {e f f}} \omega^ {2} x [ \omega ] = - m _ {\mathrm {e f f}} \Omega_ {m} ^ {2} x [ \omega ] + i \omega m _ {\mathrm {e f f}} \Gamma_ {m} x [ \omega ] \\ + \hbar G \{\bar {\alpha} ^ {*} \delta \alpha [ \omega ] + \bar {\alpha} (\delta \alpha^ {*}) [ \omega ] \}. \tag {49} \\ \end{array}
$$

Again, note that  $(\delta \alpha^{*})[\omega] = \delta \alpha[-\omega]^{*}$ .

# IV. EXPERIMENTAL REALIZATIONS AND OPTOMECHANICAL PARAMETERS

The increasing availability of high-quality optomechanical devices, i.e., high- $Q$  mechanical resonators that are efficiently

TABLE II. Experimental parameters for a representative sampling of published cavity-optomechanics experiments.  

<table><tr><td>Reference</td><td>Ωm/2π (Hz)</td><td>m (kg)</td><td>Γm/2π (Hz)</td><td>Qf (Hz)</td><td>κ/2π (Hz)</td><td>κ/Ωm</td><td>g0/2π (Hz)</td></tr><tr><td>Murch et al. (2008)</td><td>4.2 × 104</td><td>1 × 10-22</td><td>1 × 103</td><td>1.7 × 106</td><td>6.6 × 105</td><td>15.7</td><td>6 × 105</td></tr><tr><td>Chan et al. (2011)</td><td>3.9 × 109</td><td>3.1 × 10-16</td><td>3.9 × 104</td><td>3.9 × 1014</td><td>5 × 108</td><td>0.13</td><td>9 × 105</td></tr><tr><td>Teufel, Donner et al. (2011)</td><td>1.1 × 107</td><td>4.8 × 10-14</td><td>32</td><td>3.5 × 1012</td><td>2 × 105</td><td>0.02</td><td>2 × 102</td></tr><tr><td>Verhagen et al. (2012)</td><td>7.8 × 107</td><td>1.9 × 10-12</td><td>3.4 × 103</td><td>1.8 × 1012</td><td>7.1 × 106</td><td>0.09</td><td>3.4 × 103</td></tr><tr><td>Thompson et al. (2008)</td><td>1.3 × 105</td><td>4 × 10-11</td><td>0.12</td><td>1.5 × 1011</td><td>5 × 105</td><td>3.7</td><td>5 × 101</td></tr><tr><td>Kleckner et al. (2011)</td><td>9.7 × 103</td><td>1.1 × 10-10</td><td>1.3 × 10-2</td><td>9 × 109</td><td>4.7 × 105</td><td>55</td><td>2.2 × 101</td></tr><tr><td>Gröblacher, Hammerer et al. (2009)</td><td>9.5 × 105</td><td>1.4 × 10-10</td><td>1.4 × 102</td><td>6.3 × 109</td><td>2 × 105</td><td>0.22</td><td>3.9</td></tr><tr><td>Arcizet et al. (2006a)</td><td>8.14 × 105</td><td>1.9 × 10-7</td><td>81</td><td>8.1 × 109</td><td>1 × 106</td><td>1.3</td><td>1.2</td></tr><tr><td>Cuthbertson et al. (1996)</td><td>103</td><td>1.85</td><td>2.5 × 10-6</td><td>4.1 × 1010</td><td>275</td><td>0.9</td><td>1.2 × 10-3</td></tr></table>

coupled to high- $Q$  optical cavities, has been driving a plethora of experiments during recent years that are successfully demonstrating the working principles of cavity optomechanics (see Figs. 7 and 8). We now discuss some of the most frequently used architectures.

# A. Optomechanical parameters

Table I summarizes the relevant optomechanical parameters for some typical current experimental implementations. These are as follows: the mechanical resonator frequency  $\Omega_{m}$  and mass  $m$ ; the fundamental mechanical (phonon) and optical (photon) dissipation rates  $\Gamma_{m} = \Omega_{m} / Q_{m}$  and  $\kappa$ , respectively; the  $Qf$  product, which is a direct measure for the degree of decoupling from the thermal environment (specifically,  $Q_{m}f_{m} = Q_{m}\Omega_{m} / 2\pi > k_{B}T / \hbar$  is the condition for neglecting thermal decoherence over one mechanical period); the sideband suppression factor  $\kappa / \Omega_{m}$  that determines the ability to realize ground-state cooling (see Sec. VII); and finally the bare optomechanical coupling rate  $g_{0}$ , which corresponds to the cavity frequency shift induced by a mechanical zero-point displacement.

Some parameter combinations are of particular relevance for optomechanical tasks. Figures 9-12 provide an overview of the state of the art in current experiments. The data are compiled from published experiments. They are numbered as follows:

1 (Cuthbertson et al., 1996), 2 (Massel et al., 2011), 3 (Regal, Teufel, and Lehnert, 2008), 4 (Rocheleau et al., 2010), 5 (Teufel, Donner et al., 2011), 6 (Chan et al., 2011), 7 (Gavartin et al., 2011), 8 (Thompson et al., 2008), 9 (Wilson et al., 2009), 10 (Jiang et al., 2009), 11 (Lin et al., 2009), 12 (Wiederhecker et al., 2009), 13 (Eichenfield, Camacho et al., 2009), 14 (Ding et al., 2011), 15 (Park and Wang, 2009), 16 (Schliesser et al., 2008), 17 (Verhagen et al., 2012), 18 (Schliesser et al., 2009), 19 (Arcizet et al., 2006b), 20 (Favero et al., 2007), 21 (Gigan et al., 2006), 22 (Groblacher, Hertzberg et al., 2009), 23 (Kleckner et al., 2006), 24 (Mow-Lowry et al., 2008),

![](images/85c7a5498e203b0e7d79c340cb3a94193c47b758709a73bc6e12add0b5b6f495.jpg)  
FIG. 9 (color online). The single-photon optomechanical coupling strength  $g_{0}$ , vs cavity decay rate  $\kappa$ , for published experiments (see main text for references). A high value of  $g_{0} / \kappa$  is favorable for nonlinear quantum-optomechanical experiments, working with single photons and phonons (Sec. X.F).

![](images/11912b8d2604a4f210c287eb988bce88d83881889e4192ffc8218ab4c45ba572.jpg)  
FIG. 10 (color online). Mechanical quality factor  $Q_{m} = \Omega_{m} / \Gamma_{m}$  vs mechanical frequency  $\Omega_{m} = 2\pi f_{m}$  for published experiments (see main text for references). The dashed lines represent constant  $Q_{m}f_{m}$  values. Note that full coherence over one mechanical period  $1 / f_{m}$  is obtained for  $Q_{m}f_{m} = k_{B}T / \hbar$ . For example,  $Q_{m}f_{m}\gg 6\times 10^{12}$  is a minimum requirement for room-temperature quantum optomechanics. Note that data point 30 involves capacitive readout but is not a microwave cavity setup.

25 (Kleckner et al., 2011), 26 (Gröblacher, Hammerer et al., 2009), 27 (Schleier-Smith et al., 2011), 28 (Murch et al., 2008), 29 (Brennecke et al., 2008), 30 (Goryachev et al., 2012), 31 (Verlot et al., 2009), 32 (Gieseler et al., 2012). Different symbols indicate the different optomechanical implementations: suspended mirrors  $(\triangleleft)$ , optical microresonators  $(\spadesuit)$ , photonic crystal cavities  $(\triangle)$ , suspended nano-objects  $(\triangledown)$ , microwave resonators  $(\bullet)$ , and cold atoms  $(\triangleright)$ .

# B. Suspended mirrors

An obvious way to realize optomechanical interactions in a cavity is to suspend one of the cavity's mirrors. The mechanical motion directly changes the cavity length and hence the frequency response of such a "rubber cavity."10

The first experimental implementations of this type were a Fabry-Pérot cavity with moving mirrors, and they date back to the early attempts of laser interferometric detection of gravitational waves (Abramovici et al., 1992). While there the purpose of suspending the macroscopic cavity mirrors is to achieve acoustic isolation, optomechanical effects, in particular, quantum mechanical radiation-pressure fluctuations, eventually pose the fundamental limit for its interferometric sensitivity (Caves, 1980; Unruh, 1983) (see Sec. VI.A for a detailed discussion). At the same time this configuration allows one to exploit cavity optomechanics for the center-of-mass motion of truly macroscopic test masses. Experiments of that type have to date resulted in the demonstration of the optical bistability (Dorsel et al., 1983) (Sec. V.A), the optical spring effect (Sheard et al., 2004; Corbitt, Chen et al., 2007) (Sec. V.B.1), and optical cooling (Corbitt, Wipf et al., 2007;

![](images/e84405082fd0522ea7b915079ad759eff973421cdc9d9f22ad56e8b723b7ea45.jpg)  
FIG. 11 (color online). Single-photon blockade parameter  $D = g_0^2 / (\Omega_m \kappa)$  vs sideband resolution  $\Omega_m / \kappa$ , for published experiments (see main text for references). A single photon induces a cavity frequency shift  $\Delta \omega_c = D \cdot \kappa$ , which results in a blockade effect for a subsequent photon for  $D > 1$ , as discussed in Sec. X.F. The maximum two-photon suppression scales with  $(\kappa / \Omega_m)^2$  and therefore sideband resolution (shaded area) is an additional requirement for successful single-photon blockade.

Mow-Lowry et al., 2008) (Secs. V.B and VII) with suspended mirrors on the gram scale and even of feedback cooling of suspended mirrors on the kilogram scale at the LIGO facility (Abbott et al., 2009). A practical challenge of these experiments is their operation at very low mechanical frequencies  $(\Omega_{m} / 2\pi < 1\mathrm{kHz})$  , which requires sophisticated isolation against acoustic noise. For such experiments this is achieved by suspending the macroscopic mirrors over several stages. To minimize mechanical losses it was recently suggested to levitate the macroscopic mirror in an optical trap (Singh et al., 2010). Finally, this kind of setup also allows one to monitor and optomechanically control internal mechanical modes of macroscopic mirrors (Cohadon, Heidmann, and Pinard, 1999; Hadjar et al., 1999), which are a dominant source for unwanted cavity phase noise, e.g., in gravitational wave detectors (Harry et al., 2002; Harry, Bodiya, and DeSalvo, 2011), cavity QED (Buck, 2003), or frequency stabilization of atomic optical clocks (Numata, Kemery, and Camp, 2004).

Another possibility is to use highly reflecting micromechanical devices such as a Fabry-Pérot end mirror. These systems include coated cantilevers (Tittonen et al., 1999; Hohberger-Metzger and Karrai, 2004; Arcizet et al., 2006a, 2008) and micropillars (Verlot et al., 2011), micrometer-sized mirror pads on top of beams and cantilevers (Kleckner et al., 2006, 2011; Favero et al., 2007; Groblacher, Hertzberg et al., 2009; Serra et al., 2012), or micromechanically suspended optical coatings (Böhm et al., 2006; Cole et al., 2008, 2010) and photonic crystal slabs (Antoni et al., 2011; Kemiktarak et al., 2012). Efficient optomechanical coupling in this configuration requires the size of the mechanical structure to be much larger than the wavelength of the light: typical cavity lengths range from  $10^{-5}$  to  $10^{-2}\mathrm{m}$ , with an optical finesse up to  $10^{5}$ , which is generally limited by losses due to the finite cavity mirror sizes. It was pointed out that additional

![](images/b8b9fbbfd62005cb8f6f4cb392a10ac7cee6d0a9a14662d40b7c8fcf1109d6d5.jpg)  
FIG. 12 (color online). The single-photon cooperativity  $C_0 = 4g_0^2 / \kappa \Gamma_m$  vs mechanical frequency. This quantity is important for aspects such as the strength of optomechanically induced transparency (Sec. VII.C.2). Moreover, if the "quantum cooperativity"  $C_{\mathrm{qu}} \equiv C_0 \bar{n}_{\mathrm{cav}} / \bar{n}_{\mathrm{th}}$  is larger than unity, the state transfer between light and mechanics is faster than the mechanical decoherence rate. Contour lines indicate at which temperatures this would be true even for single photons ( $\bar{n}_{\mathrm{cav}} = 1$ ).

interference effects may be able to overcome this limit significantly (Kleckner et al., 2010). Compared to the macroscopic mirrors already discussed, these micromechanical devices allow access to higher mechanical frequencies (up to some tens of MHz) and, in principle, to higher mechanical quality factors. In particular, the possibility of exact geometric control via microfabrication techniques allows one to minimize mechanical losses due to clamping (Anetsberger et al., 2008; Wilson-Rae, 2008; Cole et al., 2011; Serra et al., 2012).

The accessible mass and frequency ranges in combination with the restrictions on cavity length  $(L > \lambda)$  and achievable cavity finesse set some practical limitations for this geometry. In particular, sideband resolution (small  $\kappa$ ) and large optomechanical coupling  $g_{0}$  (small  $L$ , leading to a large  $\kappa$ ), impose conflicting conditions and need to be traded against each other. On the other hand, along with the macroscopic microwave transducers (see Sec. IV.F), this realization provides optomechanical control over by far the largest range of mass and frequency.

# C. Optical microresonators

A situation similar to the Fabry-Pérot case occurs in optical microresonators, where light is guided in whispering-gallery modes along the rim of a circular resonator (Vahala, 2003). There is a large number of different mechanical normal modes of vibration of these structures. The resulting distortions of the structure directly modify the optical path length of the resonator, shifting its optical resonance frequency and hence generating optomechanical coupling. The small size of microresonators allows one to achieve large coupling rates  $g_{0}$  (Ding et al., 2011; Verhagen et al., 2012) and to access mechanical frequencies from several megahertz up to some gigahertz. In

essence, three different architectures can be distinguished: (i) Microdisk resonators, which are the standard resonator structure in planar photonic circuits and can be fabricated with high precision. Recent experiments have demonstrated large optomechanical coupling rates up to  $g_{0} \approx 2\pi \times 8 \times 10^{5}\mathrm{Hz}$  (Ding et al., 2011). A fundamental limit in their performance is given by radiation losses at the sidewalls. Another limitation is due to internal materials losses, which could be improved by using single-crystalline materials. The first demonstration in this direction, specifically optomechanical coupling to internal modes of a single-crystalline  $\mathrm{CaF}_2$  resonator, has been reported (Hofer, Schliesser, and Kippenberg, 2010). In another development, the coupling of whispering-gallery modes to surface acoustic waves in a crystalline resonator was studied by Matsko et al. (2009) and Savchenko et al. (2011). (ii) Microsphere resonators, which allow a larger optical quality (Ma et al., 2007; Park and Wang, 2009; Tomes and Carmon, 2009); there, the mechanical quality is mainly limited by internal materials losses, in particular, for the often-used silica microspheres. (iii) Microtoroidal resonators, which are obtained from microdisk resonators by a thermal reflow process that melts the sidewalls into a toroidal topology. The generated smooth surface together with the microfabrication control provides a combination of high optical (Armani et al., 2003) and high mechanical quality (Anetsberger et al., 2008). This resulted in the first demonstration of radiation-pressuredriven optomechanical parametric amplification (Carmon et al., 2005; Kippenberg et al., 2005; Rokhsari et al., 2005) as well as sideband-resolved operation (Schliesser et al., 2008). Recently, hybrid toroid devices were developed that combine optomechanical and electromechanical actuation (Lee et al., 2010), or optomechanical and magnetostrictive actuation (Forstner et al., 2012).

The practical benefits of these geometries are the availability of large optical qualities in combination with the resolved-sideband regime  $\kappa < \Omega_{m}$ , essentially owed to the fact that the mechanical frequencies range from  $10\mathrm{MHz}$  to several GHz. Possible limitations arise from the necessity to propagate light inside a solid-state medium, which increases the sensitivity to optical absorption and thermorefractive cavity noise.

# D. Waveguides and photonic crystal cavities

On-chip waveguides and photonic crystal cavities offer a different implementation architecture. Photonic crystals are formed by a periodic modulation of the index of refraction of some material (typically silicon), which leads to the formation of optical bands, in analogy with the electronic bands for electron waves propagating in a crystal lattice. Light cannot propagate in the band gaps. Thus, when artificial defects are introduced into the periodic pattern, localized electromagnetic field modes (Vahala, 2004) can form that do not decay into the continuum inside the structure. These structures are called photonic crystal cavities. To obtain an optomechanical device, in-plane photonic crystal cavities are underetched to form nanomechanical beams. The mechanical motion results in modulations of the cavity boundaries and stresses in the material, both of which contribute to the optomechanical coupling between the cavity photons and the mechanical

modes of the structure. The simultaneous presence of both localized optical and vibrational defect modes in a photonic crystal was predicted theoretically by Maldova and Thomas (2006). The optomechanical coupling in photonic crystals was demonstrated experimentally for both 1D (Eichenfield, Camacho et al., 2009; Eichenfield, Chan, Camacho et al., 2009) and 2D (Safavi-Naeini et al., 2010; Gavartin et al., 2011) photonic crystal cavities. The small cavity dimensions in combination with the small mass of the localized mechanical mode result in an optomechanical coupling strength that is much larger than in regular Fabry-Pérot approaches, with current experiments achieving  $g_{0} / 2\pi \approx \mathrm{MHz}$ . The available mechanical frequencies can range from several tens of megahertz up to several gigahertz, which significantly reduces the environmental thermal occupation  $\bar{n}_{\mathrm{th}} \approx k_{B}T / \hbar \Omega_{m}$ . The idea of creating band gaps by inducing periodic boundary conditions can be extended to the modes of the mechanical beam. Introducing a surrounding periodic structure matched to the phonon wavelength ("phonon shield") results in a 1D photonic crystal cavity with co-localized photonic and phononic modes with a significantly increased mechanical quality  $Q_{m}$  (Chan et al., 2011); see Eichenfield, Chan, Safavi-Naeini et al. (2009) and Safavi-Naeini and Painter (2010) for more on the design of 1D and 2D optomechanical crystals. It is also possible to integrate two-level quantum systems inside the photonic crystal nanobeam by fabricating photonic crystal cavity nanobeams out of diamond (Riedrich-Möller et al., 2012) or GaAs (Rundquist and Majumdar, 2011), which can include artificial qubits formed by, for example, nitrogen vacancy centers or quantum dots, respectively. Another possibility is to have hybrid devices with both optical and electrical actuation (Winger et al., 2011).

Currently, because of the large available coupling rates  $g_0 / \kappa$ , this approach may allow one to enter the regime of nonlinear photon-phonon interactions (see Sec. X.F). Moreover, the large mechanical frequencies in the gigahertz range could allow for low-temperature operation in a regime where the average phonon number drops below 1 even without additional laser cooling. This would be highly beneficial for quantum applications. Finally, the in-plane architecture is immediately compatible with the architectures of integrated (silicon) photonics and provides a direct route to larger-scale optomechanical arrays, which is interesting in the context of classical and quantum information processing, and for the study of collective dynamics (Sec. IX).

It should be noted that optomechanical forces can become strong even in the absence of a cavity for structures with waveguides running close to a substrate or close to each other. This approach (while somewhat outside the domain of the concepts covered in the present review) could be very fruitful for applications, since it does away with the bandwidth restrictions generated by a cavity (Li et al., 2008; Pernice, Li, and Tang, 2008, 2009; Li, Pernice, and Tang, 2009a, 2009b; Bagheri et al., 2011). In another equally promising development, the gigahertz acoustic vibrations of photonic crystal fibers are being excited and controlled via optomechanical interactions (Dainese et al., 2006; Kang et al., 2008, 2009; Wiederhecker et al., 2008; Kang, Brennan, and Russell, 2010; Kang, Butsch, and Russell, 2011; Butsch, Conti et al., 2012; Butsch, Kang et al., 2012).

# E. Suspended and levitated nano-objects

This class of cavity-optomechanics implementations uses a rigid optical cavity that contains a mechanical element either inside the cavity or in the near field of the cavity. It allows, in particular, the efficient optomechanical coupling to subwavelength-size mechanical objects, which has been demonstrated for systems such as high-quality mechanical membranes made of high-stress SiN (Thompson et al., 2008; Sankey et al., 2010), stochiometric SiN (Wilson et al., 2009), or AlGaAs (Liu et al., 2011), and for carbon nanowires (Favero et al., 2009), which have been suspended inside state-of-the-art Fabry-Pérot cavities. The embedded nano-objects modify the cavity field via either dispersion (Thompson et al., 2008) or dissipation, as suggested by Xuereb, Schnabel, and Hammerer (2011).

An alternative approach to Fabry-Pérot resonators is to exploit near-field effects close to the surface of optical microresonators, where the evanescent optical field allows dispersive coupling to other structures. In essence, the mechanical motion modulates the distance  $d$  between the interfaces. Because of the near-field character the optomechanical coupling strength scales exponentially with  $d$  and hence allows one to generate large values for  $g_{0}$ . This has been used to demonstrate optomechanical coupling between a toroidal microcavity and a nearby SiN nanomechanical resonator (Anetsberger et al., 2009). Another related possibility is to couple two mechanically vibrating microdisk resonators (Jiang et al., 2009; Lin et al., 2009; Wiederhecker et al., 2009) or two photonic crystal cavities (Eichenfield, Camacho et al., 2009; Roh et al., 2010) via their optical near field.

In order to further suppress mechanical clamping losses, it was suggested that the mechanical objects should be levitated either by an additional optical dipole trap or in the standing-wave trap formed by the cavity field (Barker and Shneider, 2010; Chang et al., 2010; Romero-Isart et al., 2010). This implementation allows a direct extension to matter-wave interferometry (Romero-Isart et al., 2011a) and may enable fundamental tests of quantum theory in a new macroscopic parameter regime (see also Sec. X.D). The necessary parameter regime for such tests is experimentally challenging (Romero-Isart, 2011) and may even require a space environment (Kaltenbaek et al., 2012). Levitation of micrometer-size (Ashkin and Dziedzic, 1977; Li, Kheifets, and Raizen, 2011) and sub-micrometer-size (Gieseler et al., 2012) silica spheres has already been demonstrated in optical dipole traps in high vacuum. An alternative approach could be to combine optical trapping with a low-frequency mechanical suspension (Corbitt, Wipf et al., 2007; Ni et al., 2012), which it was suggested could lead to thermal decoupling of similar quality as purely optical trapping  $(Qf\approx 10^{18})$  (Chang et al., 2012).

A prominent feature of such setups, with a nano-object inside the standing light wave of a cavity mode, is quadratic coupling to position. The optical frequency shift may no longer be linear but rather quadratic in the mechanical displacement, if the object is placed at a node or antinode. This could lead to interesting applications, such as QND detection of single phonons, as explained in Sec. VI.B.2. These setups have also been suggested to strongly couple two

nano-objects, for example, a mechanical membrane to a single atom (Hammerer, Wallquist et al., 2009; Wallquist et al., 2010) (see Sec. X.D).

# F. Microwave resonators

Analogous to optical cavities,  $LC$  circuits form a resonator for electromagnetic radiation in the microwave regime, i.e.,  $\omega_c / 2\pi \sim \mathrm{GHz}$ , or even for radio frequencies. The motion of a mechanical element capacitively coupled to this microwave cavity results in a shift of capacitance, and thereby of the  $LC$  resonance frequency  $(\partial C / \partial x \propto \partial \omega_c / \partial x)$ . Thus, one obtains the standard cavity-optomechanical radiation-pressure interaction. The first experiments along this line were performed by Braginsky and Manukin (1967, 1977) and Braginsky, Manukin, and Tikhonov (1970), and later in the context of resonant bar gravitational wave detection (Blair et al., 1995; Cuthbertson et al., 1996). Already back then these works demonstrated both cold damping and optomechanical backaction effects such as cooling and parametric amplification. Later, in the context of ion-trap physics, cooling of a micromechanical resonator via an  $LC$  circuit was shown (Brown et al., 2007). With the advent of microfabricated superconducting circuits it is possible to enter the size and frequency regime of nanomechanical devices coupled to microwave cavities (Regal, Teufel, and Lehnert, 2008). Typical available mechanical frequencies range from some MHz to some tens of MHz. In order to resemble a low-entropy reservoir of the radiation field, which is of particular importance for quantum optomechanics (see Sec. X), the microwave photons need to be kept at cryogenic temperatures. For GHz photons, environment temperatures in the mK regime are sufficient, which necessitates operation inside a dilution refrigerator. Although the momentum transfer of microwave photons is several orders of magnitude smaller compared to photons at optical frequencies, the bare optomechanical coupling rates  $g_0$  can be made comparable to (or larger than) implementations in the optical domain (Rocheleau et al., 2010; Teufel, Donner et al., 2011; Pirkkalainen et al., 2013). The essential idea is to have a very small coupling gap and to optimize the fraction of the total capacitance that responds to the mechanical motion (see also Fig. 9).

A current practical challenge for the microwave schemes is the sparse availability of quantum optics techniques such as the preparation and detection of Fock states or of squeezed states of the radiation field. However, several recent proof-of-concept experiments have demonstrated their availability in principle (Hofheinz et al., 2009; Eichler et al., 2011; Mallet et al., 2011).

As a side note, capacitive coupling has also been used to couple nanomechanical objects directly to two-level quantum systems, e.g., to a superconducting Cooper-pair box (LaHaye et al., 2009) or to a superconducting phase qubit (O'Connell et al., 2010). Note finally that the coupling need not be capacitive. Recently, it was shown that a microwave resonator can also be coupled via dielectric gradient forces to the vibrations of a nanobeam (Faust et al., 2012). This makes available a larger range of materials, which could be beneficial for applications.

# G. Ultracold atoms

The ideas of cavity optomechanics have also been implemented by using clouds of up to  $10^{6}$  atoms. Their collective motional dynamics can resemble a single mechanical mode that, for the case of ultracold atoms, is already precooled to its quantum ground state of motion. In one case, the collective motion of a cloud of ultracold Rb atoms inside a Fabry-Pérot cavity was used to observe signatures of shot-noise radiation-pressure fluctuations (Murch et al., 2008). The dispersive coupling of the collective motion of the cloud to an optical cavity field results in a position-dependent frequency shift and therefore to quantum optomechanical interactions.

Suppose the single-photon dispersive energy shift of a single atom sitting at an antinode of the standing light wave pattern is  $\delta E = -\hbar (g_0^{\mathrm{at}})^2 /\Delta_{\mathrm{at}}$  with  $g_0^{\mathrm{at}}$  the atom-cavity vacuum Rabi frequency, and  $\Delta_{\mathrm{at}}$  the detuning between atom and cavity resonance. Then the coupling Hamiltonian between the cavity mode and an atom cloud of  $N$  atoms trapped near position  $\bar{x}$  is  $N\delta E\hat{a}^{\dagger}\hat{a}\sin^{2}[k(\bar{x} +\hat{x})]$ . Expanding to lowest order in  $\hat{x}$ , this yields a bare optomechanical coupling rate (Stamper-Kurn, 2014)

$$
g _ {0} = \frac {\left(g _ {0} ^ {\mathrm {a t}}\right) ^ {2}}{\Delta_ {\mathrm {a t}}} \left(k x _ {\mathrm {Z P F}} ^ {\mathrm {a t o m}}\right) \sin (2 k \bar {x}) \sqrt {N},
$$

where  $x_{\mathrm{ZPF}}^{\mathrm{atom}} = \sqrt{\hbar / 2m_{\mathrm{atom}}\Omega_m}$  denotes the zero-point fluctuations of a single atom in the trapping potential. We note that  $x_{\mathrm{ZPF}}^{\mathrm{atom}}$  is  $\sqrt{N}$  times larger than  $x_{\mathrm{ZPF}}^{\mathrm{c.m.}}$  of the center-of-mass motion of the cloud. Here we assumed that the extent of the cloud is small with respect to the wavelength. Sometimes the cloud is actually distributed over several lattice sites. Note that the trapping potential could be provided by another optical lattice or magnetically. Incidentally, we note that the same kind of derivation applies for trapped dielectric particles (Sec. IV.E). We also mention that if the atoms are trapped right at a node or antinode, the leading optomechanical coupling is to  $\hat{x}^2$  instead of  $\hat{x}$ , which leads to different physics (e.g., as in Sec. VI.B.2).

In another experiment, cavity optomechanics was used to cool the motion of a thermal cloud of Cs atoms trapped inside an optical cavity (Schleier-Smith et al., 2011). Finally, density fluctuations in a Bose-Einstein condensate of  $10^{6}$  atoms have been used as the mechanical mode inside a Fabry-Pérot cavity (Brennecke et al., 2008). In both ultracold cases, due to the strong dispersive atomic coupling and the small mass (leading to a large zero-point motional amplitude), operation was close to the single-photon strong-coupling regime  $g_{0} / \kappa \sim 1$ .

More recently, a setup was demonstrated that couples the motion of a vibrating mirror to the motion of atoms trapped in a standing light wave being reflected from that mirror (Camerer et al., 2011), without an optical cavity.

# V. BASIC CONSEQUENCES OF THE OPTOMECHANICAL INTERACTION

# A. Static phenomena: Optical potential and bistability

We first deal with the simplest case, when the light force reacts instantaneously to the mechanical motion. This is

![](images/a20511e2e8bf7f80dd3a63fdbb3ae2b871e4f9607953c4a01ddebc3b5b7dc2e8.jpg)  
FIG. 13 (color online). Optomechanical static bistability occurs when the laser intensity is sufficiently high to generate two stable local minima in the effective mechanical potential (top). This results in bistable behavior and hysteresis when recording the circulating photon number  $\bar{n}_{\mathrm{cav}}$  or the transmission as a function of laser detuning (bottom).

relevant for  $\kappa \gg \Omega_{m}$ . Then the radiation-pressure force  $F(x) = \hbar G\bar{n}_{\mathrm{cav}}(x)$  depends on the displacement  $x$  via  $\bar{n}_{\mathrm{cav}}(x)$ , the photon number circulating inside the optical mode. Such a 1D conservative force can be derived from a potential (Fig. 13):

$$
F (x) = - \frac {\partial V _ {\mathrm {r a d}} (x)}{\partial x}. \tag {50}
$$

For the case of a single, high-finesse optical resonance we have  $\bar{n}_{\mathrm{cav}}(x) = \bar{n}_{\mathrm{cav}}^{\max} / \{1 + [2(Gx + \Delta) / \kappa ]^{2}\}$ , where  $\bar{n}_{\mathrm{cav}}^{\mathrm{max}}$  is the maximum number of circulating photons obtained at resonance (proportional to the incoming laser intensity). As a result,

$$
V _ {\text {r a d}} (x) = - \frac {1}{2} \hbar \kappa \bar {n} _ {\text {c a v}} ^ {\max } \arctan [ 2 (G x + \Delta) / \kappa ]. \tag {51}
$$

Note that for the case of photothermal forces, the discussion still applies, only with a different prefactor in  $F(x) \propto \bar{n}_{\mathrm{cav}}(x)$ . The overall potential for the mechanical motion also includes the intrinsic harmonic restoring potential:

$$
V (x) = \frac {m _ {\text {e f f}} \Omega_ {m} ^ {2}}{2} x ^ {2} + V _ {\text {r a d}} (x). \tag {52}
$$

The first effect of the radiation force is to shift the equilibrium position to  $x_0 \neq 0$ , with  $V'(x_0) = 0$ . In addition, the effective spring constant is changed to its new value

$$
k _ {\text {e f f}} = V ^ {\prime \prime} \left(x _ {0}\right) = m _ {\text {e f f}} \Omega_ {m} ^ {2} + V _ {\text {r a d}} ^ {\prime \prime} \left(x _ {0}\right), \tag {53}
$$

where the second contribution is called "optical spring." In particular, for low-frequency mechanical modes, this term can be orders of magnitude larger than the intrinsic mechanical spring (Corbitt, Chen et al., 2007). Such an approach essentially amounts to a variant of optical trapping and can be exploited to diminish the unwanted mechanical dissipation and heating connected with the intrinsic mechanical spring being

![](images/bafa6099e941520b10e0f2eb9b27c8ad5a5551a5314437e18634b5d694f34123.jpg)  
FIG. 14 (color online). "Thermodynamic" style schematic diagram depicting the work done by the radiation force during one cycle of oscillation. The work is given by the finite area swept in the force-displacement diagram, which is due to the retardation of the force (finite cavity decay rate). The work is negative or positive, depending on whether one is on the red-detuned or blue-detuned side of the resonance. This then gives rise to damping or amplification, respectively.

attached to a substrate. In the limit of low light intensity, the resulting correction for the mechanical frequency [obtained from  $V_{\mathrm{rad}}^{\prime \prime}(0) = m_{\mathrm{eff}}\delta (\Omega_m^2)$ ] is

$$
\delta \Omega_ {m} = 8 \Delta \left(\frac {g _ {0}}{\kappa}\right) ^ {2} \frac {\bar {n} _ {\mathrm {c a v}} ^ {\max }}{\left[ 1 + (2 \Delta / \kappa) ^ {2} \right] ^ {2}}. \tag {54}
$$

This corresponds to the limit  $\kappa \gg \Omega_{m}$  of the dynamical case discussed below (note the relation between  $\bar{n}_{\mathrm{cav}}$  and  $\bar{n}_{\mathrm{cav}}^{\mathrm{max}}$ ).

At larger light intensities  $V(x)$  may develop into a double-well potential, with two local minima, leading to what we term static bistability. Both of these minima correspond to stable equilibrium positions, determined by the nonlinear equation  $F(x_{1/2}) = m_{\mathrm{eff}} \Omega_m^2 x_{1/2}$ , which equates the radiation-pressure force to the restoring force. Physically, they represent situations with low or high light intensity and low or high restoring force, respectively. The bistable behavior will occur at negative detunings  $\Delta < 0$ , roughly when  $\delta \Omega_m \sim -\Omega_m$ , such that the original equilibrium position becomes unstable. As negative detunings are necessary for cooling, the bistability limits the achievable cooling laser intensities for the case  $\kappa > \Omega_m$ .

More quantitatively, analysis of the equation  $F(x) = m_{\mathrm{eff}} \Omega_m^2 x$  shows that bistability sets in first, at a single value of  $\Delta$ , when the maximum (in magnitude) correction to the spring constant  $-\partial F(x) / \partial x$  obtained at  $Gx + \Delta = -\kappa / (2\sqrt{3})$  equals the intrinsic spring constant  $m_{\mathrm{eff}} \Omega_m^2$  (Meystre et al., 1985). This happens at a critical detuning of  $\Delta = -\sqrt{3} \kappa / 2$  and at a critical laser power determined by

$$
6 \sqrt {3} \frac {g _ {0} ^ {2}}{\Omega_ {m} \kappa} \bar {n} _ {\text {c a v}} ^ {\max } = 1, \tag {55}
$$

where we employed the relations  $G = g_{0} / x_{\mathrm{ZPF}}$  and  $x_{\mathrm{ZPF}}^{2} = \hbar /(2m_{\mathrm{eff}}\Omega_{m})$ . At higher light intensities, the range of detunings for which bistability is observed widens. In experiments, bistability is revealed in hysteresis, e.g., when recording the transmission or phase shift while sweeping the detuning up and down. The first experiments on optomechanical bistability, with a macroscopic mirror, were reported and analyzed already in the 1980s, in both the optical (Dorsel et al., 1983; Meystre et al., 1985) and microwave domains (Gozzini et al., 1985).

![](images/15eb16f485bc1127ad75a68da3c04b64bf4be8da21cf857b5224aa46d876bffb.jpg)  
FIG. 15 (color online). Schematic optomechanical feedback loop.

For low-finesse systems, nearby optical resonances may also become relevant for the mechanical motion, leading to a more complicated effective potential, possibly with several local minima (Fig. 13).

# B. Dynamical backaction

We now turn to dynamical effects, due to the retarded nature of the radiation-pressure force. To derive the dynamics arising from the optomechanical coupling, one can solve the linearized coupled equations of motion for the light and the mechanics, as presented in Sec. III.C. This is best done in frequency space. We employ the classical linearized equations (48) and (49) as the basis for our following analysis. This is possible since we are interested only in the linear response to an external mechanical force, and the averaged linearized quantum equations are identical to their classical version (and do not contain the noise sources anymore).

In the linearized regime described here, the optomechanical system can be viewed in analogy to a linear amplifier (Botter et al., 2012) that receives optical and mechanical input fields (see Fig. 15).

In the absence of optomechanical coupling, the mechanical oscillator has the susceptibility  $\chi_{m}^{-1}(\omega) = m_{\mathrm{eff}}[(\Omega_{m}^{2} - \omega^{2}) - i\Gamma_{m}\omega ]$  (see Sec. II.B.3). We now assume that a weak test force  $F$  acts on the mechanical oscillator in the presence of the optomechanical interaction. Solving the coupled set of equations, we find the mechanical response to that force. This defines the modified mechanical susceptibility, which can be expressed in terms of the original susceptibility plus some modification<sup>11</sup>:

$$
\chi_ {m, \text {e f f}} ^ {- 1} (\omega) = \chi_ {m} ^ {- 1} (\omega) + \Sigma (\omega). \tag {56}
$$

The coupled equations (48) and (49) are solved by expressing  $\delta \alpha[\omega]$  in terms of  $x[\omega]$  and inserting the result into the equation for  $x[\omega]$ . This yields the modification of the linear response to an external force:

$$
\Sigma (\omega) = 2 m _ {\text {e f f}} \Omega_ {m} g ^ {2} \left\{\frac {1}{(\Delta + \omega) + i \kappa / 2} + \frac {1}{(\Delta - \omega) - i \kappa / 2} \right\}, \tag {57}
$$

where we employed the relation  $G = g_{0} / x_{\mathrm{ZPF}}$  and we obtain  $\hbar G^{2}|\bar{\alpha}|^{2} = 2m_{\mathrm{eff}}\Omega_{m}g^{2}$ . For now, we just define

$$
\Sigma (\omega) \equiv m _ {\mathrm {e f f}} \omega [ 2 \delta \Omega_ {m} (\omega) - i \Gamma_ {\mathrm {o p t}} (\omega) ],
$$

such that the new terms have the structure that is suggested by the form of the original susceptibility, leading to:

$$
\chi_ {m, \text {e f f}} ^ {- 1} (\omega) = m _ {\text {e f f}} \left\{\Omega_ {m} ^ {2} + 2 \omega \delta \Omega_ {m} (\omega) - \omega^ {2} - i \omega \left[ \Gamma_ {m} + \Gamma_ {\text {o p t}} (\omega) \right] \right\}. \tag {58}
$$

The real and imaginary parts then yield the frequency-dependent mechanical frequency shift  $\delta \Omega_{m}(\omega)$  and optomechanical damping rate  $\Gamma_{\mathrm{opt}}(\omega)$ , whose meaning will be discussed further in the next sections (Secs. V.B.1 and V.B.2). The explicit expressions are [by taking real and imaginary parts  $\delta \Omega_{m}(\omega) = \mathrm{Re}\Sigma (\omega) / 2\omega m_{\mathrm{eff}}$  and  $\Gamma_{\mathrm{opt}}(\omega) = -\mathrm{Im}\Sigma (\omega) / m_{\mathrm{eff}}\omega ]$ :

$$
\begin{array}{l} \delta \Omega_ {m} (\omega) = g ^ {2} \frac {\Omega_ {m}}{\omega} \left[ \frac {\Delta + \omega}{(\Delta + \omega) ^ {2} + \kappa^ {2} / 4} + \frac {\Delta - \omega}{(\Delta - \omega) ^ {2} + \kappa^ {2} / 4} \right], \\ \Gamma_ {\mathrm {o p t}} (\omega) = g ^ {2} \frac {\Omega_ {m}}{\omega} \left[ \frac {\kappa}{(\Delta + \omega) ^ {2} + \kappa^ {2} / 4} - \frac {\kappa}{(\Delta - \omega) ^ {2} + \kappa^ {2} / 4} \right]. \\ \end{array}
$$

These expressions provide an exact solution of the linearized problem that is also valid in the regime of strong coupling, where  $g > \kappa / 2$  (Sec. VII.C). Also note that the effect is linear in the laser drive power, i.e., in the circulating photon number:  $g^2 = g_0^2 \bar{n}_{\mathrm{cav}}$ . In Secs. V.B.1 and V.B.2 we discuss the resulting physical phenomena, i.e., optical spring effect and amplification and cooling.

The frequency dependence of  $\Sigma (\omega)$  will in general yield a non-Lorentzian line shape for the susceptibility that will even turn into a double-peak structure at strong coupling (Sec. VII.C.1). However, for sufficiently weak laser drive  $(g\ll \kappa)$ , it is permissible to evaluate  $\delta \Omega_{m}(\omega)$  and  $\Gamma_{\mathrm{opt}}(\omega)$  at the original, unperturbed oscillation frequency  $\omega = \Omega_{m}$ . Then we just have a shifted and broadened mechanical resonance. This picture also explains why we need the assumption  $\kappa \gg \Gamma_{\mathrm{eff}}$  for this approach to hold, where  $\Gamma_{\mathrm{eff}} = \Gamma_m + \Gamma_{\mathrm{opt}}(\Omega)$  is the full linewidth (see below). A high- $Q$  mechanical oscillator samples the optical density of states at  $\omega = \pm \Omega_{m}$ , with a small frequency linewidth  $\Gamma_{\mathrm{eff}}$  that can be neglected as long as  $\Gamma_{\mathrm{eff}}\ll \kappa$ . We now discuss both quantities, the frequency shift and the damping rate, under this assumption.

# 1. Optical spring effect

We find, with  $\omega = \Omega_{m}$ , for the frequency shift of the oscillator induced by the light field:

$$
\delta \Omega_ {m} = g ^ {2} \bigg (\frac {\Delta - \Omega_ {m}}{\kappa^ {2} / 4 + (\Delta - \Omega_ {m}) ^ {2}} + \frac {\Delta + \Omega_ {m}}{\kappa^ {2} / 4 + (\Delta + \Omega_ {m}) ^ {2}} \bigg).
$$

In the limit of a large cavity decay rate (i.e., the Doppler regime  $\kappa \gg \Omega_{m}$ ), this formula yields

$$
\left. \delta \Omega_ {m} (\Delta) \right| _ {\kappa \gg \Omega_ {m}} = g ^ {2} \frac {2 \Delta}{\kappa^ {2} / 4 + \Delta^ {2}}.
$$

This implies that the mechanical oscillator will be spring softened for a red-detuned laser beam  $(\Delta < 0)$ , and spring hardened for a blue-detuned laser  $(\Delta > 0)$ .

Note that the frequency shift takes a markedly different form when we enter the resolved-sideband regime. Here the optical spring effect vanishes at certain detunings, where the radiation pressure contributes only to cooling or amplification.

# 2. Optomechanical damping rate

Using the same approximation as for the optical spring effect, the optomechanical damping rate is given by

$$
\Gamma_ {\text {o p t}} = \bar {n} _ {\text {c a v}} g _ {0} ^ {2} \left(\frac {\kappa}{\kappa^ {2} / 4 + \left(\Delta + \Omega_ {m}\right) ^ {2}} - \frac {\kappa}{\kappa^ {2} / 4 + \left(\Delta - \Omega_ {m}\right) ^ {2}}\right). \tag {59}
$$

This yields the full effective mechanical damping rate

$$
\Gamma_ {\text {e f f}} = \Gamma_ {m} + \Gamma_ {\text {o p t}}.
$$

Since  $\Gamma_{\mathrm{opt}}$  can be both positive and negative, it can either increase or decrease the mechanical damping rate, i.e., cause extra damping or antidamping. Extra damping leads to cooling (Sec. III), while antidamping can lead to amplification of thermal fluctuations, and finally to an instability if the full damping rate becomes negative  $\Gamma_{\mathrm{eff}} < 0$  (see Sec. VIII).

This behavior can also be observed experimentally: Figs. 16 and 17 show the damping rate and optically induced frequency shift for different ratios of  $\Omega_{m} / \kappa$ .

The physical origin of the optomechanical damping rate can be described in several ways.

# a. Mechanical picture

Cooling and heating can be understood by the following mechanical consideration. As the mechanical oscillator is performing its harmonic motion, it traces a trajectory in the diagram of radiation-pressure force versus displacement as

![](images/44e61f10ca45b080d2f14d5fc12d33679fede4de3560aa2a8a8d18ba984c9d95.jpg)

![](images/614c0e3ce79876dd72fbbe7833ebecfd31008a6c385934371cbd3df4bc1d734e.jpg)

![](images/85fe3de30755c278965d5db91518e9d8afa186aaba705405f18028b6c5535d9c.jpg)  
Relative detuning

![](images/bcab54bf6179f66242cd009db050e06647cebc8f5931c412c4bd0c2835094a2f.jpg)

![](images/c82f2573fb4029398027a9ba9c3ed42955ccb36ff45c594eff791b4de10f13b1.jpg)

![](images/ebb5ca7124a85c9766f0972bd73925841210d58979cf616d59263903c28917bd.jpg)

![](images/487271c3367c07a41309e5f3d872142d274ab5057edb279c156e853d48850d0e.jpg)  
Relative detuning

FIG. 16 (color online). Optomechanical damping rate and optical spring effect vs detuning and different sideband parameters, with theory (black lines) and experimental data (dots). (a)-(d) Full mechanical damping rate  $\Gamma_{\mathrm{eff}} / 2\pi$  vs detuning  $\Delta /\kappa$  with decreasing values of  $\kappa /\Omega_{m}$  from top to bottom  $(\kappa /\Omega_{m} = 3.7,2.2,1.4,0.7)$ . The regime where  $\Gamma_{\mathrm{eff}}$  touches zero is the regime of dynamical instability (mechanical lasing). (e)-(h) Optical spring effect, i.e., light-induced mechanical frequency shift  $\delta \Omega_{m} / 2\pi$ . Adapted from Schliesser and Kippenberg, 2010.

![](images/7044de03ee53c08a6dedfd757ffc41fee7229666c84f0d2e53efb39710699fa4.jpg)  
FIG. 17 (color online). Optomechanical cooling rate and frequency shift in the resolved-sideband regime, shown here for  $\kappa / \Omega_{m} \ll 1$ . Adapted from Teufel et al., 2008.

shown in Fig. 14. In the limit where  $\kappa \gg \Omega_{m}$ , the intracavity field (and the associated radiation-pressure force) respond instantaneously to the oscillator motion. If, however, we still take into account the remaining cavity retardation, this leads to the radiation-pressure force getting out of phase with the mechanical motion. We then can split the force as  $F(t) = \bar{F} +\delta F_I(t) + \delta F_Q(t)$  into a component  $\delta F_I(t)$  in phase with the motion  $x(t)$  (responsible for the optical spring effect) and an out-of-phase quadrature term  $\delta F_Q(t)$  (responsible for cooling or heating). In the diagram this implies that the oscillator motion no longer traces out a line but an area. The sense in which this area is encompassed gives the direction of energy flow, i.e., cooling or amplification.

# b. Scattering picture

Writing the optomechanical dynamical backaction in the above fashion allows one to gain physical insight into the origin of cooling and amplification. The expression consists of two terms which are essentially the cavity buildup factor  $\kappa / (\Delta^2 + \kappa^2 / 4)$  evaluated at the frequencies  $\Delta = \omega + \Omega_m$  and  $\Delta = \omega - \Omega_m$ . These terms describe the strength of the motional sidebands of the intracavity field, generated due to the cavity frequency oscillating because of the motion  $x(t) = x_0 \cdot \sin(\Omega_m t)$  of the mechanical oscillator. To see this, we calculate the behavior of the intracavity field amplitude in the presence of this finite-amplitude mechanical oscillation. Perturbation theory analysis of the classical coupled mode equations reveals that the intracavity field exhibits sidebands (Kippenberg and Vahala, 2007):

$$
a (t) \approx a _ {0} (t) + a _ {1} (t), \tag {60}
$$

where  $a_0(t) = \alpha_{\mathrm{in}}\cdot e^{-i\omega_Lt}\sqrt{\kappa_{\mathrm{ex}}} /(-i\Delta +\kappa /2)$  is the unperturbed field and  $a_1(t)$  contains the anti-Stokes  $a_{as}(t)$  and Stokes  $a_{s}(t)$  sidebands:

$$
a _ {1} (t) = \frac {g _ {0} x _ {0}}{2 x _ {\mathrm {Z P F}}} a _ {0} (t) \left(\frac {e ^ {- i \Omega_ {m} t}}{- i (\Delta + \Omega_ {m}) + \kappa / 2} - \frac {e ^ {i \Omega_ {m} t}}{- i (\Delta - \Omega_ {m}) + \kappa / 2}\right). \tag {61}
$$

![](images/f87c205a07c84e8d292c0e9e0d75a9588468acfb7b59c1c17c336e8ad44599c9.jpg)

![](images/947edf0e3176853649ae776c0a6d764a5dafe003ad4ae8cc11ec3817d010b4b9.jpg)  
FIG. 18 (color online). Scattering picture of cooling and amplification. (a) Amplification and heating proceeds by suppressing anti-Stokes scattering and enhancing Stokes scattering, via the cavity density of states. (b) Cooling proceeds vice versa, by suppressing the Stokes process and enhancing anti-Stokes scattering.

These two sidebands become asymmetric for nonzero laser detuning due to the cavity density of states. Applying energy conservation arguments implies that the mode-density-induced sideband asymmetry must either extract from or add power to the mechanical oscillator. The total power deposited into the mechanical motion is obtained by the difference of the optical powers emitted from the Stokes and anti-Stokes sidebands, $^{12}$  i.e.,

$$
\Delta P = P _ {s} - P _ {a s} = \left(\hbar \Omega_ {m} \kappa\right) \left(| a _ {s} | ^ {2} - | a _ {a s} | ^ {2}\right).
$$

Writing this mechanical power in terms of an effective damping rate, i.e.,  $\Delta P = -\Gamma_{\mathrm{opt}} \cdot m_{\mathrm{eff}} \Omega_m^2 x_0^2 / 2$ , we recover a cooling rate identical to the expression derived above. Consequently, cooling and amplification can be viewed as originating from the imbalance of Stokes and anti-Stokes scattering (see Fig. 18).

For the case of resolved sidebands  $(\Omega_{m}\gg \kappa)$  the cavity absorption spectrum  $1 - |\mathcal{R}(\Delta)|^2$  develops a series of sidebands due to the mechanical oscillator's motion, similar to the absorption spectrum of an oscillating ion (Stenholm, 1986) (Fig. 19):

$$
\left| \mathcal {R} (\Delta) \right| ^ {2} \approx 1 - \eta (1 - \eta) \kappa^ {2} \sum_ {n} \frac {J _ {n} (\beta) ^ {2}}{(\Delta + n \Omega_ {m}) ^ {2} + \kappa^ {2} / 4}, \tag {62}
$$

where  $\eta = \kappa_{\mathrm{ex}} / \kappa$  and  $\beta = (G / \Omega_m)x_0$  denotes the modulation index. For the simple case of a weak coherent oscillation (with amplitude  $x_0$ ) one obtains to lowest order two sidebands only, i.e.,  $J_{\pm 1}(\beta)^2 = \beta^2$ . The lower and upper motional sidebands that appear in the spectrum are, in analogy to trapped-ion physics, related to motionally increasing

![](images/43345e62e68b3ae1d38e0233fea4c88dfd6a7823f9f4de4f1167b61c78891e0a.jpg)  
FIG. 19 (color online). Transmission spectrum of an oscillating cavity in the resolved-sideband regime, as measured by Schliesser et al. (2008). The mechanical motion leads to the appearance of a series of sidebands spaced by multiples of the mechanical frequency  $n\Omega_{m}$ , where  $n = 0, \pm 1, \pm 2, \ldots$ . In most optomechanical experiments only the first pair of sidebands is relevant. Optomechanical cooling proceeds by pumping the lower sideband (as indicated by the arrow labeled  $\omega_{L}$ ), which leads to cooling of the mechanical oscillator.

and motionally decreasing scattering processes (Wineland and Itano, 1979).<sup>13</sup>

# c. Feedback picture

Finally, one can also understand the cooling by considering a feedback picture. In this picture the mechanical oscillator motion modulates the cavity field, and the latter gives rise to a radiation-pressure force, which in turn acts back onto the mechanical oscillator. Cooling arises again from the phase relationship (retardation) between the mechanical motion and the radiation-pressure force. Note that the feedback is not entirely noiseless: Quantum noise adds to the intracavity radiation-pressure force, giving rise to the quantum limit of cooling treated in Sec. VII.A.

It is instructive to consider several limiting cases of the cooling rate expression.

# d. Resolved-sideband regime

First, in the limit where the mechanical frequency is much larger than the cavity decay rate  $(\Omega_{m} \gg \kappa)$ , the cooling rate exhibits pronounced maxima and minima near the lower and upper sidebands  $(\Delta = \pm \Omega_{m})$ . The maximum cooling rate is attained on the lower sideband  $(\Delta = -\Omega_{m})$ :

$$
\left. \Gamma_ {\text {o p t}} \right| _ {\kappa \ll \Omega_ {m}} = 4 \bar {n} _ {\text {c a v}} \frac {g _ {0} ^ {2}}{\kappa} = \frac {4 g ^ {2}}{\kappa}. \tag {63}
$$

$$
\frac {d E}{d t} = - \frac {\eta P}{\hbar \omega_ {L}} \beta^ {2} \hbar \Omega_ {m} = - \Gamma_ {\mathrm {o p t}} E,
$$

yielding again

$$
\Gamma_ {\text {o p t}} = \left(g _ {0} ^ {2} / \Omega_ {m} ^ {2}\right) \frac {\eta P}{\hbar \omega} = 4 \bar {n} _ {\text {c a v}} g _ {0} ^ {2} / \kappa
$$

where  $\eta = \kappa_{\mathrm{ex}} / \kappa$  in agreement with the classical calculation.

Note that the cooling rate in the resolved-sideband regime can also be expressed via the so-called cooperativity  $\mathcal{C} = \mathcal{C}_0\bar{n}_{\mathrm{cav}}$  where  $\mathcal{C}_0 = 4g_0^2 /\kappa \Gamma_m$  is the single-photon cooperativity. We have  $\Gamma_{\mathrm{opt}} = \Gamma_m\mathcal{C}$  in this regime.

The cooling rate in the resolved-sideband regime can also be expressed in a different way, as detailed by Schliesser et al. (2008). In the resolved-sideband regime (considering an overcoupled single-sided cavity for simplicity), the relation between the intracavity photon number and input power is given by  $\bar{n}_{\mathrm{cav}} = (\eta P / \hbar \omega_L)\cdot \kappa /\Omega_m^2$  , where  $\eta = \kappa_{\mathrm{ex}} / \kappa$  . Thus

$$
\left. \Gamma_ {\text {o p t}} \right| _ {\kappa \ll \Omega_ {m}} = \frac {4 \eta P}{\hbar \omega_ {L}} \frac {g _ {0} ^ {2}}{\Omega_ {m} ^ {2}}, \tag {64}
$$

Evidently, the cooling rate in the resolved-sideband limit does not depend on the cavity linewidth.

# e. Doppler regime

In the unresolved-sideband regime (Doppler case, i.e.,  $\kappa \gg \Omega_{m}$ ), the rate is given by the following expression, and we show later that the lowest possible effective temperature is reached for a detuning equal to  $\Delta = -\kappa /2$  [which does not correspond to the maximum cooling rate, which is achieved at  $\Delta = -\kappa /(2\sqrt{3})$  for fixed  $g$ ], provided we keep the intracavity photon number (and therefore  $g$ ) fixed:

$$
\Gamma_ {\text {o p t}} (\Delta) = g ^ {2} \Omega_ {m} \frac {- 4 \Delta \kappa}{\left(\kappa^ {2} / 4 + \Delta^ {2}\right) ^ {2}}, \tag {65}
$$

$$
\Gamma_ {\text {o p t}} \left(\Delta = - \frac {\kappa}{2}\right) = 8 \left(\frac {g}{\kappa}\right) ^ {2} \Omega_ {m}. \tag {66}
$$

In this case the mechanical cooling and amplification rates exhibit a strong dependence on the inverse (cubic) cavity decay rate. This shows that the cooling rate strongly diminishes in the Doppler regime. Note that sub-Doppler cooling in the unresolved-sideband regime can still be achieved by using pulsed optical pumping schemes (Vanner et al., 2011, 2012; Wang et al., 2011; Machnes et al., 2012).

# VI. QUANTUM OPTICAL MEASUREMENTS OF MECHANICAL MOTION

One of the principal advantages of cavity-optomechanical systems is the built-in readout of mechanical motion via the light field transmitted through (or reflected from) the cavity. In the following, we discuss several variants of optical measurement schemes. We first address the measurement of position, where we find that quantum mechanics places fundamental restrictions on the overall precision in the regime typically employed in experiments (i.e., weak measurements). Then we discuss alternative schemes, where there are no such limitations. Some supply a measurement of a selected quadrature of mechanical motion, i.e., the amplitude of the  $\cos (\Omega_m t)$  or  $\sin (\Omega_m t)$  contribution to  $x(t)$ . Other schemes measure the discrete phonon number. Both approaches are examples of so-called quantum nondemolition (QND) measurements. We close the section by pointing out some experimental issues in phase measurements and discussing feedback cooling based on the possibility of precise readout.

# A. Parametric displacement sensing and the standard quantum limit

Measuring the displacement of a mechanical resonator via the transmission or reflection phase shift typically involves integrating the data over a long time in order to suppress the noise. It is therefore an example of a weak, continuous measurement. It turns out that such a measurement applied to the coordinate of a harmonic oscillator cannot be more precise than what is known as the "standard quantum limit" (SQL). In the following we give a brief qualitative and quantitative discussion. More about this topic can be found in Caves (1980, 1981, 1982), Braginsky, Mitrofanov, and Panov (1985), Braginsky and Khalili (1995), and Clerk et al. (2010).

# 1. Introduction and qualitative discussion

The optical cavity represents an interferometer and thus allows a direct measurement of the mechanical position via the phase shift of transmitted or reflected light. In practice this requires either a homodyne or a heterodyne detector, in which the signal is brought into interference with a local oscillator that serves as a phase reference. The optomechanical-cavity frequency pull  $Gx$  is converted into a phase shift  $\theta \propto Gx / \kappa$  imparted on the photons during their lifetime  $1 / \kappa$  inside the cavity (assuming slow motion  $\Omega_{m} \ll \kappa$ ). If one tries to measure this phase shift using  $N$  photons passing through the cavity (and interfering with a reference beam to read out the phase later), then the fundamental uncertainty relation between the number and the phase yields a shot-noise-limited imprecision of  $\delta \theta = 1 / (2\sqrt{N})$  (see Fig. 20). It seems that this would allow for an arbitrarily precise readout, provided one uses a sufficiently large number of photons. Indeed, this would be true for an instantaneous readout with a very intense flash of light.

However, in many experiments one rather performs a weak measurement: The noisy signal  $x(t)$  determined from the phase

![](images/98e24738279ab7171cdfd53f53fe5bb96c42f96716464743904bbd6cba519340.jpg)  
FIG. 20 (color online). Optomechanical systems transduce displacements into changes of the optically transmitted (or reflected) phase. Upper panel: amplitude response. Lower panel: phase response. The inset in the lower panel shows the mechanical phase space spanned by the position  $(x$  axis) and momentum  $(y$  axis) quadratures.

measurement is effectively integrated over many oscillation periods to average away the noise and get a sufficient signal-to-noise ratio. The fact that this will pose a problem can be seen from the general quantum mechanical uncertainty principle which states that it is impossible to follow the trajectory  $x(t)$  of a particle with arbitrary precision (or to know both position and momentum at the same time). It is instructive to see qualitatively how that limitation is enforced in our case. The fluctuating radiation-pressure force (again, due to the photon shot noise) imprints an unavoidable jitter on the mechanical motion. Each of the photons imparts a random kick, and their overall effect on the momentum and position will grow like  $\sqrt{N}$ , as in a random walk. That effect is called backaction noise and counteracts the increase of phase readout precision at large  $N$ . Thus, there is an optimum at intermediate photon numbers, where the sum of the two effects is minimal.

The quantitative analysis outlined below will be phrased in terms of noise spectra, describing the imprecision and back-action noise contributions to the overall measurement error. In that context, the appropriate question to ask is how large the error is given a certain measurement time (which sets the bandwidth over which the spectra are to be integrated). In thermal equilibrium, the mechanical oscillator's phase and amplitude will fluctuate on the scale of the damping time  $1 / \Gamma_{m}$ . Thus, this is the longest reasonable measurement time at our disposal. The outcome of the analysis will be that one can determine the trajectory (or rather its two quadratures) up to a precision given by the oscillator's zero-point fluctuations  $x_{\mathrm{ZPF}} = (\hbar /2m_{\mathrm{eff}}\Omega_m)^{-1 / 2}$  during a time  $1 / \Gamma_{m}$ . This statement [see Eq. (73)] is known as the standard quantum limit of displacement detection in a weak measurement. It is independent of whether the oscillator is in its ground state or at high temperatures.

# 2. The standard quantum limit

We first state more formally why there must be a standard quantum limit. The oscillator's trajectory can be decomposed into quadratures:

$$
\hat {x} (t) = \hat {X} \cos \left(\Omega_ {m} t\right) + \hat {Y} \sin \left(\Omega_ {m} t\right), \tag {67}
$$

where  $\hat{X}$  and  $\hat{Y}$  remain constant during intervals smaller than the damping time. Since  $\hat{X} = \hat{x}(0)$  and  $\hat{Y} = \hat{p}(0) / m_{\mathrm{eff}}\Omega_m$ , the commutator  $[\hat{x},\hat{p}] = i\hbar$  carries over to  $\hat{X}$  and  $\hat{Y}$ , yielding  $[\hat{X},\hat{Y}] = i\hbar /m_{\mathrm{eff}}\Omega_m$ . Heisenberg's uncertainty relation thus reads

$$
\Delta X \cdot \Delta Y \geq \frac {\hbar}{2 m _ {\mathrm {e f f}} \Omega_ {m}} = x _ {\mathrm {Z P F}} ^ {2}, \tag {68}
$$

and any simultaneous measurement that tries to measure both quadratures with equal precision is limited to  $\Delta X = \Delta Y = x_{\mathrm{ZPF}}$ .<sup>14</sup>

Here we discuss only the most important results. For a more extended recent discussion of the quantum limits to weak measurements see Clerk et al. (2010). We consider a single-sided optical cavity (overcoupled,  $\kappa_{\mathrm{ex}}\approx \kappa$ ) driven at laser

detuning  $\Delta = 0$  (the optimal case), where the number of photons circulating inside the cavity is  $\bar{n}_{\mathrm{cav}} = 4P / \kappa \hbar \omega_{\mathrm{cav}}$ . All noise spectral densities are symmetrized (see Sec. II.B.3) in frequency (indicated by  $\bar{S}$ ).

The noise in the optical phase readout  $\delta \theta \sim 1 / \sqrt{N}$  induces an imprecision in the  $x$  measurement, where  $\delta x^{\mathrm{imp}}\sim \kappa \delta \theta /G = \kappa /G\sqrt{N}$ , as discussed previously. Inserting the photon number  $N = t\dot{N}\sim t\kappa \bar{n}_{\mathrm{cav}}$ , we find  $(\delta x^{\mathrm{imp}})^2\sim (\kappa /\bar{n}_{\mathrm{cav}}G^2)t^{-1}$ . This can be understood as the integral of a flat noise spectral density  $\bar{S}_{xx}^{\mathrm{imp}}\sim \kappa /\bar{n}_{\mathrm{cav}}G^2$  over the bandwidth  $t^{-1}$  set by the measurement time  $t$ . The complete expression (Schliesser et al., 2009) for the quantum-noise-limited imprecision noise spectral density reads

$$
\bar {S} _ {x x} ^ {\mathrm {i m p}} (\omega) = \frac {\kappa}{1 6 \bar {n} _ {\mathrm {c a v}} G ^ {2}} \left(1 + 4 \frac {\omega^ {2}}{\kappa^ {2}}\right), \tag {69}
$$

where we also kept the growth of the noise at higher values of  $\omega / \kappa$ . This is due to the fact that the cavity is a low-pass filter, suppressing the contribution of motional frequencies  $\omega > \kappa$  to the phase output. On the other hand, the phase noise itself is independent of  $\omega$ , so referring it back to the input leads to larger imprecision at higher  $\omega$ .

At the same time, the backaction noise force has the following spectral density (cf. Sec. VII.A):

$$
\bar {S} _ {F F} (\omega) = \bar {n} _ {\mathrm {c a v}} \frac {4 \hbar^ {2} G ^ {2}}{\kappa} \left(1 + 4 \frac {\omega^ {2}}{\kappa^ {2}}\right) ^ {- 1}. \tag {70}
$$

The product of imprecision noise and backaction force noise densities fulfills a fundamental inequality, a variant of the Heisenberg uncertainty relation [see Braginsky and Khalili (1995) for the derivation of the general version<sup>15</sup>; some further discussion can be found in recent reviews such as Clerk et al. (2010)].

$$
\bar {S} _ {x x} ^ {\mathrm {i m p}} (\omega) \bar {S} _ {F F} (\omega) \geq \frac {\hbar^ {2}}{4}. \tag {71}
$$

In our particular case, we see that the equality is realized, i.e., the cavity displacement detector is as good as allowed by quantum mechanics.

The total noise registered at the detector, expressed in terms of  $x$  ("referred back to the input"), reads

$$
\bar {S} _ {x x} ^ {\text {t o t a l}} (\omega) = \bar {S} _ {x x} ^ {\text {t h}} (\omega) + \bar {S} _ {x x} ^ {\text {i m p}} (\omega) + \bar {S} _ {F F} (\omega) | \chi_ {m} (\omega) | ^ {2}. \tag {72}
$$

Here we added the intrinsic thermal fluctuation spectrum (including the vacuum fluctuations), the imprecision noise, and the effect of the backaction noise force on the displacement, calculated via the mechanical susceptibility  $\chi_{m}$  (see Sec. II.B.3). In doing so we assumed a situation where there are no cross correlations between the force noise and the imprecision noise. See Clerk et al. (2010) for a more complete discussion including the general case and Fig. 21 for a typical measurement of the total noise power. In the following, we denote the sum of the imprecision and backaction noises as the total added noise  $\bar{S}_{xx}^{\mathrm{add}}$ . Inserting the relation (71), and treating

![](images/d17f7c1a8536411fc09953c38ad9df868423d3857b8411a8c4242bfefceff8d1.jpg)  
FIG. 21 (color online). Mechanical frequency spectrum for an example of an optomechanical system. The actual imprecision noise floor (dark data points at bottom) is indicated along with the full noise at the standard quantum limit. Similar data demonstrating imprecision below that at the SQL exists for nanomechanical oscillators using a microwave-cavity interferometer (Teufel et al., 2009) or nanomechanical oscillators coupled to the near field of an optical microresonator. Adapted from Schliesser and Kippenberg, 2010.

$\bar{S}_{FF}$  as variable (e.g., by tuning  $\bar{n}_{\mathrm{cav}}$ ), we can minimize  $\bar{S}_{xx}^{\mathrm{add}}$ . The minimum (at any given, fixed frequency) is reached at  $\bar{S}_{FF} = \hbar /(2|\chi_m|)$ , and this yields  $\bar{S}_{xx}^{\mathrm{add}}(\omega)\geq \hbar |\chi_m(\omega)|\geq \hbar |\mathrm{Im}\chi_m(\omega)|$ . By using the quantum FDT at  $T = 0$  [see Eq. (16)], we can introduce the spectral density of mechanical zero-point fluctuations  $\bar{S}_{xx}^{\mathrm{ZPF}}(\omega) = \hbar |\mathrm{Im}\chi_m(\omega)|$ . We arrive at the fundamental inequality

$$
\tilde {S} _ {x x} ^ {\mathrm {a d d}} (\omega) \geq \tilde {S} _ {x x} ^ {\mathrm {Z P F}} (\omega). \tag {73}
$$

This is the standard quantum limit (SQL) of weak displacement detection. The measurement adds at least the zero-point noise, on top of the intrinsic fluctuations. Backaction and imprecision noise both contribute equally to the added noise at the SQL. The combined effect on the noise looks as if the oscillator's energy were increased by  $\hbar \Omega_{m} / 2$ , i.e., one-half a phonon. However, only the backaction contribution really corresponds to a physical increase of the oscillator's effective temperature by  $\hbar \Omega_{m} / 4$ .

If we measure at the mechanical resonance  $\omega = \Omega_{m}$ , then the added noise of the cavity displacement detector is  $\bar{S}_{xx}^{\mathrm{add}}(\Omega_m) = \bar{S}_{xx}^{\mathrm{ZPF}}(\Omega_m) = \hbar / m_{\mathrm{eff}} \Omega_m \Gamma_m$ . This corresponds to resolving the zero-point fluctuations in a measurement time  $t \sim \Gamma_m^{-1}$ , just as stated in the introduction of this section. Obviously, if one is limited by laser power, it is better to have a high-quality oscillator (small  $\Gamma_m$ ), which boosts  $\bar{S}_{xx}^{\mathrm{ZPF}}(\Omega_m)$  and makes it easier to reach that imprecision level. The power to reach the standard quantum limit therefore is a natural expression to characterize a transducer. For an overcoupled cavity ( $\kappa \gg \kappa_{\mathrm{ex}}$ ), it is given by

$$
P _ {\mathrm {S L}} = \Gamma_ {m} \hbar \omega_ {L} \frac {\kappa^ {2}}{6 4 g _ {0} ^ {2}} \left(1 + 4 \frac {\omega^ {2}}{\kappa^ {2}}\right). \tag {74}
$$

![](images/4e7de28b3f662e75b7f7913039d6639102cdc7658cfc6d2ca2784d01765f2f8a.jpg)

![](images/a318f6ad8589acc3e127d236cbd23670be0a7d0ddda10379bca40b852cf69f6b.jpg)  
FIG. 22 (color online). The full measured noise spectrum contains contributions from the intrinsic fluctuations of the mechanical oscillator, but also extra noise due to imprecision in the measurement (typically flat in frequency) and noise due to the backaction heating of the oscillator. Bottom: The added noise evaluated at the mechanical resonance, plotted as a function of the power of the measurement beam. At lower powers, imprecision noise dominates (a small number of photons yields bad phase resolution), while at higher powers the backaction noise represents the most important contribution. The standard quantum limit minimal noise is reached at intermediate powers.

Both the imprecision noise and the backaction noise are shown as functions of laser power (or optomechanical coupling) in Fig. 22. When referring to "precision beyond that at the standard quantum limit" in this context, one wants to emphasize that one can make the imprecision noise alone lower than the SQL (which implies that the backaction noise is already appreciable). This situation has been achieved in optomechanical systems for mechanical oscillators of nanoscale (Anetsberger et al., 2009; Teufel et al., 2009) and microscale dimensions (Schliesser et al., 2008; Westphal et al., 2012). Using phase-squeezed input states of light a reduction of the imprecision noise has been demonstrated in microcavities (Hoff et al., 2013) and gravitational wave detectors (Aasi et al., 2013).

The observed thermal noise at any large temperature can also be used to obtain the value of the standard quantum limit via

$$
\bar {S} _ {x x} ^ {\mathrm {t h}} (\omega) / \bar {S} _ {x x} ^ {\mathrm {Z P F}} (\omega) = 2 \bar {n} _ {\mathrm {t h}} (\omega) \approx 2 k _ {B} T / \hbar \omega .
$$

This is a useful expression, since it is independent of the calibration of the  $x$  measurement.

In the context of measurements at the SQL, an important step for optomechanical experiments is to observe the effects of radiation-pressure shot noise on the mechanical oscillator. This has been achieved already in cold atom setups (Murch et al., 2008; Brooks et al., 2012), which are conducted

![](images/ec53090400e773a82891fe3b3a4c012a57032b7a354235ba0d7e9e28d7ad80c0.jpg)  
FIG. 23 (color online). Observation of quantum radiation-pressure force fluctuations through the energy transferred to a near-ground-state mechanical oscillator. Experiments were performed with an ultracold atomic gas serving as the mechanical element within a Fabry-Pérot optical cavity. (a) The energy transferred to the gas was quantified via the rate at which atoms were ejected from a finite-depth optical trap. The force-fluctuation spectral density at the mechanical oscillation frequency  $S_{FF}(\Omega_m)$  is thereby obtained at different detunings  $\Delta$  between the cavity probe and resonance frequencies. From Murch et al., 2008. (b) From the power difference between the red and blue motional sidebands observed in the emission of a resonantly driven optical cavity, one obtains the heat flux into the mechanical system via the cavity probe. The observed heating, given in units of mechanical energy quanta per second, matches well to that predicted for intracavity shot noise from a coherent optical field (gray line). From Brahms et al., 2012. Courtesy of D. Stamper-Kurn.

![](images/4ef89c582ca30e7256c6506bb1ebd0312950b14895cdc8f0da0bac0f2c342904.jpg)

routinely at low temperatures, and where the particularly low effective mass of the atomic cloud leads to a very strong single-photon coupling rate  $g_{0}$ . This is an advantage, since the ratio of quantum backaction to thermal force noise (at  $\Delta = 0$ ) is given by (assuming  $\kappa \gg \kappa_{\mathrm{ex}}$ )

$$
\frac {S _ {F F} \left(\Omega_ {m}\right)}{S _ {F F} ^ {\mathrm {t h}} \left(\Omega_ {m}\right)} = \mathcal {C} _ {0} \frac {\bar {n} _ {\mathrm {c a v}}}{\bar {n}} = \frac {1 6 \eta P g _ {0} ^ {2} \Omega_ {m}}{\kappa^ {2} \Gamma_ {m} \omega_ {\mathrm {c a v}} k _ {B} T} \frac {1}{1 + 4 \Omega_ {m} ^ {2} / \kappa^ {2}}, \tag {75}
$$

where  $\mathcal{C}_0 = 4g_0^2 /\kappa \Gamma_m$  is the single-photon optomechanical cooperativity. These atomic cloud experiments have allowed access to the radiation-pressure shot-noise spectrum, e.g., via tracking the heating of the cloud (see Fig. 23) and subsequently demonstrated the ability to detect forces at the standard quantum limit (Schreppler et al., 2014).

Current solid-state-based devices still exhibit both significantly smaller ratios  $g_0 / \kappa$  and deleterious effects of thermal noise, which make the observation of radiation-pressure shot-noise effects a challenging task. One possible strategy is to measure the cross correlations between a strong beam exerting radiation-pressure force fluctuations and another beam measuring the resulting displacement fluctuations [Heidmann, Hadjar, and Pinard (1997); see also Borkje et al. (2010) for a more recent analysis]. This idea was demonstrated for a model situation with deliberately introduced classical noise instead of the quantum shot noise of a laser beam (Verlot et al., 2009). In another experiment, it was demonstrated how the radiation-pressure backaction can be employed for amplifying an interferometric signal, which can lead to a sensitivity lower than the SQL (Verlot et al., 2010). Recently, a direct observation of radiation-pressure shot noise was reported (Purdy, Peterson, and Regal, 2013), where an increasingly strong measurement led to the expected increasing backaction force that was

comparable in magnitude to the thermal forces in the system. Moreover, in this experiment, the cross correlations between the fluctuations in the radiation-pressure force and the position of the mechanical resonator could be demonstrated.

# B. Optical QND measurements

The weak-displacement measurements discussed in Sec. VI.A effectively try to measure noncommuting observables simultaneously, namely, the two quadrature components of motion. They are therefore limited fundamentally by the Heisenberg uncertainty principle. However, it is also possible to perform measurements of a single observable. This observable can be measured with arbitrary precision, thereby approaching an idealized projection measurement. Repeating the measurement before the state has a chance to decay reproduces the same outcome. This is because the system's Hamiltonian commutes with the observable (neglecting decay). Therefore such measurements are said to be quantum nondemolition (Braginsky, Vorontsov, and Thorne, 1980; Braginsky and Khalili, 1995, 1996). These were successfully realized in the quantum optical domain (Leibfried et al., 1996; Haroche and Raimond, 2006; Lvovsky and Raymer, 2009).

# 1. Single-quadrature measurements

It is possible to optically measure only one quadrature component of the mechanical motion to arbitrary precision. The idea of such backaction-evading measurements of a single quadrature was proposed and analyzed in detail by Caves et al. (1980) [see also Braginsky and Khalili (1995)]. Pioneering proof-of-principle experiments in the classical limit were performed by Bocko and Johnson (1984)) and later applied to realize classical thermal squeezing (Rugar and Grütter, 1991).

The application of this technique to quantum optomechanics was worked out by Clerk, Marquardt, and Jacobs (2008), and first experiments have now been performed in this direction. An ideally noise-free measurement of a single quadrature is important, since it can be used for a full reconstruction of the mechanical quantum state, extracting its Wigner density using quantum-state tomography (see Fig. 24). In addition, it can serve to measure the correlation of mechanical quadratures with either the light field quadratures or those of another mechanical object. The resulting correlators can then be used to test for entanglement. The fundamentally limited precision of a standard displacement measurement would not be sufficient for such tests.

One way of achieving this makes use of a simple property of harmonic motion: Any force applied at time  $t$  does not affect the position until a full period later, at  $t + 2\pi /\Omega_{m}$ . Thus, the unavoidable perturbation of the momentum connected with a position measurement does not destroy the precision of "stroboscopic" periodic observations at times  $t + n2\pi /\Omega_{m}$ . An equivalent but more practical approach is to do a displacement measurement with a laser beam (at detuning  $\Delta = 0$ ) whose intensity is modulated at frequency  $\Omega_{m}$  (see Fig. 24). This reads out only one quadrature (say,  $\hat{X}_{\varphi}$ ) in the decomposition

$$
\hat {x} (t) = \hat {X} _ {\varphi} \cos \left(\Omega_ {m} t + \varphi\right) + \hat {Y} _ {\varphi} \sin \left(\Omega_ {m} t + \varphi\right), \tag {76}
$$

![](images/79cfee3da728c498b6855963393e288aab28c067f1e7a41d61df8c6ed4c22886.jpg)

![](images/8b25693597438693089e805577dd325b45921382938229eb24079803f570ad64.jpg)  
FIG. 24 (color online). (a) Schematic setup for an optomechanical single-quadrature measurement, with a laser-beam amplitude modulated at the mechanical frequency. (b) In optical frequency space, the beam carries two sidebands, which are then modulated by the motion (vertical arrows indicate injected laser beams; scattering into sidebands is indicated as well). (c) Tomographical reconstruction of the full mechanical Wigner phase-space density is possible based on measurements of the quadratures at different phases  $\varphi$ .

![](images/ed525abcc1921e5b63b50d2faa96511d2b1a1866952478b343db49c94f3ef2bd.jpg)

whose phase  $\varphi$  is determined by the phase of the laser amplitude modulation. The backaction noise exclusively affects the other quadrature (Clerk, Marquardt, and Jacobs, 2008). All this can be derived in the Hamiltonian formulation (Sec. III.B). Suppose the modulated drive yields an intracavity amplitude  $\alpha = 2\alpha_0\cos (\Omega_m t + \varphi)$  in a frame rotating at the cavity resonance. Then the standard linearization gives

$$
\begin{array}{l} H _ {\text {i n t}} = - 2 \hbar G \alpha_ {0} \cos \left(\Omega_ {m} t + \varphi\right) \left(\delta \hat {a} + \delta \hat {a} ^ {\dagger}\right) \hat {x} \\ \approx - \hbar G \alpha_ {0} (\delta \hat {a} + \delta \hat {a} ^ {\dagger}) \hat {X} _ {\varphi}, \tag {77} \\ \end{array}
$$

where we omitted rapidly oscillating terms and adopted the rotating frame for the mechanical resonator in the second step. This is a QND Hamiltonian for measuring  $\hat{X}_{\varphi}$ . Deviations from this idealized picture are small in the resolved-sideband limit, i.e., for  $\kappa / \Omega_{m} \ll 1$ . As a side effect, the state conditioned on the measurement result becomes squeezed, since the variance of  $\hat{X}_{\varphi}$  after the measurement approaches zero. The first experimental steps along these lines were taken by Hertzberg et al. (2009) and Suh et al. (2014).

There is an alternative approach for QND detection of single quadratures: measuring much faster than the oscillation period of the mechanical resonator. Such an approach requires very short, intense laser pulses that essentially implement an instantaneous projection measurement of displacement. Picking another quadrature to measure then simply involves performing the measurement at another time, when the phase of the harmonic oscillations has advanced. This approach was proposed and analyzed by Braginsky, Vorontsov, and Khalili (1978), Braginsky and Khalili (1995), and Vanner et al. (2011). Because of the short pulses, this scheme operates in the nonresolved-sideband regime  $\kappa \gg \Omega_{m}$ . First experiments in this direction were recently reported by Vanner et al. (2012). It was also pointed out that properly controlled pulse sequences can alter the effective optomechanical interaction, enabling, for example, sub-Doppler cooling rates in the

nonresolved-sideband regime (Wang et al., 2011; Machnes et al., 2012).

In both of these approaches, quantum-state tomography (Lvovsky and Raymer, 2009) then works by repeatedly preparing the same mechanical state, measuring the probability densities of the quadratures at a large number of phases  $\varphi$ , and applying the inverse radon transform to obtain the Wigner density. Reconstruction of the Wigner density of quantum states of vibrational motion has, for example, successfully been achieved for ions (Leibfried et al., 1996).

# 2. Mechanical Fock-state detection

Another crucial observable in the mechanical oscillator is the phonon number  $\hat{n} = \hat{b}^{\dagger}\hat{b}$ . It is especially important, since measuring the discrete Fock states  $n = 0,1,2,\ldots$  is a direct proof of the quantum nature of an oscillator. We note that the first measurements of the phonon number in a fabricated, mesoscopic mechanical oscillator were recently performed in a nanoelectromechanical system, exploiting the strong interaction between a piezomechanical vibration and a superconducting qubit (O'Connell et al., 2010). Here we discuss a potential route toward observing quantum jumps between mechanical Fock states in an optomechanical system (Jayich et al., 2008; Thompson et al., 2008).

The idea is that any measurement of  $\hat{x}^2$  instead of  $\hat{x}$  will be closely connected to the oscillator's energy, and thus the phonon number. This then permits QND detection of the phonon number in a mechanical resonator [for an early detailed analysis of this concept in an anharmonic two-mode nanomechanical system, see Santamore, Doherty, and Cross (2004)]. In practice, for an optomechanical system this requires changing the standard setup to another variant where the light field couples to the square of the displacement. That can be achieved, for example, by placing a thin membrane (or any other dielectric object) inside an optical cavity and positioning it near a node (or antinode) of the standing light wave that forms one optical mode (see Fig. 25). In that case, the light intensity at the object's position, and thereby the object's effect on the optical resonance frequency, depends quadratically on the displacement  $\hat{x}$ . The optomechanical coupling then reads

$$
\hat {H} _ {\text {i n t}} = \hbar g _ {0} ^ {(2)} (\hat {b} + \hat {b} ^ {\dagger}) ^ {2} \hat {a} ^ {\dagger} \hat {a}, \tag {78}
$$

where

$$
g _ {0} ^ {(2)} = 1 / 2 \frac {\partial^ {2} \omega_ {\mathrm {c a v}}}{\partial x ^ {2}} x _ {\mathrm {Z P F}} ^ {2}.
$$

If the membrane is highly reflecting, an alternative way of deriving Eq. (78) is to focus on two optical modes (to the left and right of the membrane). Their coupling, provided by photon tunneling through the membrane, then leads to an avoided level crossing in the optical spectrum as a function of  $x$ . At the degeneracy point, both the upper and lower optical branch frequencies are extremal (Thompson et al., 2008; Sankey et al., 2010), leading to Eq. (78) for each of them. Quadratic couplings have recently also been observed in a cold atom setup (Purdy et al., 2010).

The phase shift observed in reflection from the cavity measures  $(\hat{b} +\hat{b}^{\dagger})^{2}\propto \hat{x}^{2}$ , but averaged over the photon

![](images/c11cd2d2c7778c43c156816a886b0755edd4f3900c97c23de62216a4de6c2315.jpg)

![](images/931c6330e4a365e2e1ecac5af3e2b5d3001640c3b6cbfa15fefb19df26277a91.jpg)  
FIG. 25 (color online). (a) The "membrane-in-the-middle" setup used to generate an optomechanical coupling to  $\hat{x}^2$ . It can be viewed as two optical modes, one to the left and one to the right of the membrane, with photon transmission through the membrane coupling those modes. (b) Resulting optical spectrum, with an avoided crossing between the left and right optical modes as a function of displacement  $x$ . Coupling to  $\hat{x}^2$  is obtained at the degeneracy point. (c) Future dispersive setups along these lines (with greatly improved parameters) may enable detection of quantum jumps between mechanical Fock states in the phase shift of light reflected from the cavity. An idealized quantum jump trajectory (without measurement noise) is depicted here, starting from the mechanical ground state (0 phonons).

![](images/c2cfc58bf938ef12540cce7bd1cbc32b32c272c0fb3bdb7d3452002b0594b858.jpg)

lifetime  $1 / \kappa$ . If  $\kappa \ll \Omega_{m}$ , the time average of this term reduces to  $2\hat{b}^{\dagger}\hat{b} + 1$ . One may arrive at the same result by keeping only this contribution in Eq. (78), invoking the rotating-wave approximation. Thus, this setup in principle allows a QND measurement of the phonon number. Cooling the oscillator to near its ground state and then measuring the phase shift versus time, one should be able to observe quantum jumps between mechanical Fock states, similar to the jumps that have been observed between Fock states of an electron cyclotron oscillator (Peil and Gabrielse, 1999) or between photon number states (Guerlin et al., 2007). To this end, the phase shift  $\sim g_0^{(2)} / \kappa$  induced by a single phonon must be resolved during the lifetime  $(\Gamma_m\bar{n}_{\mathrm{th}})^{-1}$  of the ground state, by reflecting a sufficient number of photons from the cavity. More precisely, the measurement time and the photon lifetime must be much shorter than the Fock-state lifetime (Jayich et al., 2008; Gangat, Stace, and Milburn, 2011). Note that one must suppress any deviations from the ideal case, such as imperfect placement away from the degeneracy point (Jayich et al., 2008; Thompson et al., 2008) or deviations from a perfectly one-sided cavity. Such deviations lead to extra noise acting on the membrane that hampers the phonon QND measurement. A careful analysis (Miao et al., 2009) showed that this requires  $g_0 \gg \kappa_0$ , where  $\kappa_0$  includes any absorption in the membrane or cavity, but not the "good" decay channel through the entrance mirror. Here we assumed for simplicity the commonly chosen condition of critical coupling  $\kappa_{\mathrm{ex}} = \kappa_0$ , where this is identical to the challenging single-photon strong-coupling regime, to be discussed further in Sec. X.F.

Detailed quantum jump trajectory simulations of the phonon detection process were first presented by Gangat, Stace, and Milburn (2011) for the idealized case of a single optical mode. More recently, studies of the complete two-mode setup (Ludwig et al., 2012) were able to confirm the physics discussed above (Miao et al., 2009).

The detection of quantum jumps between mechanical Fock states is obviously extremely challenging. However, one might detect quantum signatures of the mechanical oscillator in another way: When driving it strongly into a coherent mechanical state of mean phonon number  $\bar{n}$ , there will be Poissonian phonon shot noise of size  $\sqrt{\bar{n}}$ . A setup like the one described above may then detect this noise, which reveals the granularity of mechanical quanta (Clerk, Marquardt, and Harris, 2010), much in the same way that measurements of electrical current noise can reveal the charge of the charge carriers (Blanter and Böttiker, 2000). Furthermore, higher moments of the phonon shot noise may be observed in this way as well. These display distinctly nonclassical features; for an in-depth analysis see Clerk (2011).

# 3. Optical feedback cooling (cold damping)

The high sensitivity provided by the cavity readout of mechanical motion can also be used for directly cooling the mechanical motion via active feedback. The main idea is to obtain the oscillator position by a phase-sensitive detection of the cavity output and to use it to generate a negative feedback on the oscillator, i.e., a force  $F = -m_{\mathrm{eff}} \delta \Gamma \dot{x}$  proportional to the time derivative of the output signal. This increases the damping rate of the system by  $\delta \Gamma$  without increasing the thermal noise (cold damping). The scheme was suggested by Mancini, Vitali, and Tombesi (1998) and was experimentally realized in several optomechanical devices (Cohadon, Heidmann, and Pinard, 1999; Arcizet et al., 2006b; Kleckner and Bouwmeester, 2006; Poggio et al., 2007) with radiation pressure as the feedback force. Because the scheme relies on the precise readout of the instantaneous oscillator position, the ideal configuration comprises both weak coupling and a fast cavity decay, i.e.,  $\kappa \gg \Omega_m \gg g$  (adiabatic

![](images/1d22f590777a97272f36e6b95209038a5fdee6325f94c63f0949f4c24cdb2f96.jpg)  
FIG. 26 (color online). Optomechanical feedback cooling of a cantilever. Note the "noise squashing" at strong feedback (reduction of the spectrum below the noise floor due to interference between the classical noise in the readout and the signal caused by the mechanical motion). From Poggio et al., 2007.

regime). The quantum limits of this cooling method were discussed by Courty, Heidmann, and Pinard (2001), Vitali et al. (2002), and Genes et al. (2008) and it has been shown that ground-state cooling by cold damping is possible. A detailed discussion has been given by Genes et al. (2008). The maximum amount of cooling is limited by the imprecision of the readout. An important aspect here is the phenomenon of "noise squashing," where the noise on the detector and the noise-driven motion of the mechanical oscillator become correlated (see Fig. 26).

In the context of cold atoms, feedback cooling of a single neutral atom was implemented in a cavity QED setup (Koch et al., 2010).

# VII. OPTOMECHANICAL COOLING

Optomechanical quantum control requires the mechanical oscillator to be in or near its quantum ground state. Unless the mechanical frequency  $\Omega_{m}$  is in the GHz range [which is true only for some recent nanomechanical setups (Eichenfield, Chan, Camacho et al., 2009; Chan et al., 2011)], even dilution refrigerator temperatures of  $20\mathrm{mK}$  are not sufficient to ensure  $k_{B}T \ll \hbar \Omega_{m}$ . Thus, additional cooling of the selected mechanical mode is needed.

In Sec. V.B, we discussed dynamical backaction effects and the resulting optomechanical damping rate. It is obvious that this can be used for cooling the mechanical motion. The purpose of this section is to develop the quantum theory of cooling, which, in particular, describes the limits for cooling that cannot be obtained from a discussion of the damping rate alone. We focus in this section on intrinsic cavity cooling. For a comparison of this approach to feedback cooling (discussed previously), see Genes et al. (2008).

A simple classical theory of an oscillator at initial temperature  $T_{\mathrm{init}}$  subject to extra damping  $\Gamma_{\mathrm{opt}}$  (proportional to the laser power) predicts that its temperature is reduced down to

$$
T _ {\text {f i n a l}} = T _ {\text {i n i t}} \frac {\Gamma_ {m}}{\Gamma_ {m} + \Gamma_ {\text {o p t}}}. \tag {79}
$$

However, this classical expression ceases to be valid at sufficiently low  $T_{\mathrm{final}}$ , when the fluctuations of the radiation-pressure force due to photon shot noise set a lower bound to the achievable temperature. In the following, we discuss the full quantum theory that permits one to calculate the quantum limits to cooling and predicts that, in many cases, ground-state cooling is possible only in the resolved-side-band regime  $\kappa \ll \Omega_m$ .

Note that the absence of sideband resolution does not intrinsically prohibit optomechanical ground-state cooling. For example, the displacement may not couple only to the cavity frequency  $\omega_{\mathrm{cav}} = \omega_{\mathrm{cav}}(x)$ , but also to the decay rate, yielding  $\kappa = \kappa (x)$ . This mechanism is quite plausible both for nano-objects that scatter light out of the cavity (depending on where they are in the standing light wave pattern) and for vibrating objects that are evanescently coupled to some tapered fiber, as well as for other geometries. This kind of behavior was observed experimentally (Li, Pernice, and Tang, 2009c). The consequences depend sensitively on whether it is

the coupling to the drive channel (input mirror) that is modulated or just the internal absorption and scattering. It was predicted (Elste, Girvin, and Clerk, 2009) that this dissipative optomechanical coupling mechanism can yield novel behavior for cooling, with the possibility of reaching the quantum ground state even when  $\kappa >\Omega_{m}$ ; see also Weiss, Bruder, and Nunnenkamp (2013). Similar results hold for pulsed cooling schemes (Vanner et al., 2011; Wang et al., 2011; Machnes et al., 2012) and photothermal cooling (Restrepo et al., 2011).

Another interesting option is to consider a nonlinear medium inside a cavity, which may enhance the efficiency of cooling (Huang and Agarwal, 2009a), or to improve the cooling efficiency by modulating the cavity dissipation in time (Liu et al., 2013).

Finally, one could do away with the cavity by exploiting other sharp changes of radiation forces as a function of wavelength. This was proposed, e.g., for a Bragg mirror (Karrai, Favero, and Metzger, 2008) or for microspheres with their narrow internal whispering-gallery resonances (Barker, 2010).

We focus on radiation-pressure cooling in cavity setups, which is conceptually the simplest case. Recently it was argued that photothermal forces, which were exploited for optomechanical cooling early on (Höhberger-Metzger and Karrai, 2004; Metzger et al., 2008a), could in principle also lead to the quantum ground state (Pinard and Dantan, 2008; Restrepo et al., 2011).

# A. Quantum theory of radiation-pressure cooling

In the following, we work in the weak-coupling regime  $g \ll \kappa$ , where a perturbative picture applies. The quantum theory of optomechanical cooling (Marquardt et al., 2007; Wilson-Rae et al., 2007; Genes et al., 2008) is related to earlier approaches for trapped ions (Neuhauser et al., 1978; Itano et al., 1992) and for cavity-assisted laser cooling of atomic and molecular motion (Hechenblaikner et al., 1998; Vuletic and Chu, 2000). The idea is best explained in a Raman-scattering picture (see Fig. 27). Photons impinging at a

![](images/3098a605699738a5c747b723d36f66cf794e75db6d399b7f00a99923847fed48.jpg)  
FIG. 27 (color online). Principle of cavity-optomechanical cooling and corresponding transition diagram. Three processes can be distinguished. First, a photon can be absorbed by the cavity leaving the motional states unchanged (carrier transitions). Second, the photon can create a phonon (corresponding to absorption on the upper motional sideband). Third, the photon leads to the annihilation of a phonon (corresponding to a photon being absorbed by the lower motional sideband). Appropriate red detuning of the laser can lead to effective suppression of the first two processes and efficient cooling. Adapted from Schliesser et al., 2008.

frequency red detuned from the cavity resonance will, via the optomechanical interaction, preferentially scatter upward in energy in order to enter the cavity resonance, absorbing a phonon from the oscillator in the process. As a consequence, they will be reflected blueshifted by  $\Omega_{m}$ , carrying away a quantum of mechanical energy. These "anti-Stokes" processes happen at a rate  $A^{-}$  (to be calculated later). More precisely, the transition rate from phonon state  $n$  to  $n - 1$  includes a bosonic factor  $n$ ,

$$
\Gamma_ {n \rightarrow n - 1} = n A ^ {-}. \tag {80}
$$

The "Stokes" process, where photons are return redshifted and leave behind an extra phonon, happens at a smaller rate  $A^{+}$  [with  $\Gamma_{n\rightarrow n + 1} = (n + 1)A^{+}$ ] due to the suppression in the final density of available photon states (Clerk et al., 2010), if the laser is red detuned. Note that we choose to follow the notation  $A^{\pm}$  for these rates, as is used in the context of atomic laser cooling.

Given these rates ( $A^{+}$  for upward transitions in the mechanical oscillator,  $A^{-}$  for downward transitions), the full optomechanical damping rate is the net downward rate,

$$
\Gamma_ {\text {o p t}} = A ^ {-} - A ^ {+}. \tag {81}
$$

The average phonon number  $\bar{n} = \sum_{n=0}^{\infty} nP_n$  (with the Fock-state populations  $P_n$ ) changes according to the rates  $\Gamma_{n\to n\pm 1}$ , leading to

$$
\dot {\bar {n}} = (\bar {n} + 1) \left(A ^ {+} + A _ {\mathrm {t h}} ^ {+}\right) - \bar {n} \left(A ^ {-} + A _ {\mathrm {t h}} ^ {-}\right). \tag {82}
$$

Here we introduced the extra transition rates due to the oscillator's thermal environment, which has a mean phonon number  $\bar{n}_{\mathrm{th}}$ :  $A_{\mathrm{th}}^{+} = \bar{n}_{\mathrm{th}}\Gamma_{m}$  and  $A_{\mathrm{th}}^{-} = (\bar{n}_{\mathrm{th}} + 1)\Gamma_{m}$ . In the absence of optomechanical effects, these establish equilibrium at  $\bar{n} = \bar{n}_{\mathrm{th}}$ . Now, however, the steady-state final phonon number [requiring  $\dot{\bar{n}} = 0$  in Eq. (82)] is

$$
\bar {n} _ {f} = \frac {A ^ {+} + \bar {n} _ {\mathrm {t h}} \Gamma_ {m}}{\Gamma_ {\mathrm {o p t}} + \Gamma_ {m}}. \tag {83}
$$

Even in the optimal case, i.e., in the absence of any coupling to a mechanical thermal environment  $(\Gamma_{m} = 0)$ , this leads to a minimal phonon number of

$$
\bar {n} _ {\min } = \frac {A ^ {+}}{\Gamma_ {\text {o p t}}} = \frac {A ^ {+}}{A ^ {-} - A ^ {+}}. \tag {84}
$$

The rates  $A^{\pm}$  can be calculated using Fermi's golden rule, applied to the interaction of the oscillator with the fluctuating radiation-pressure force  $\hat{H}_{\mathrm{int}} = -\hat{x}\hat{F}$ , where  $\hat{F} = \hbar G\hat{a}^{\dagger}\hat{a}$  according to Eq. (20) (see also Fig. 28). In the weak-coupling limit, all the transition rates can be calculated once the quantum noise spectrum  $S_{FF}(\omega) = \int_{-\infty}^{+\infty}dt e^{i\omega t}\langle \hat{F} (t)\hat{F} (0)\rangle$  of the force is known [see, e.g., Clerk et al. (2010) for more on quantum noise spectra]. Reexpressing the result in terms of noise spectra yields

![](images/78bda76b79fc61fd2841475635149319fe75f629b33784c22eafedff6eee5bf0.jpg)  
FIG. 28 (color online). Quantum noise spectrum  $S_{FF}(\omega)$  for the radiation-pressure force fluctuations acting on the end mirror of a laser-driven optical cavity. The spectrum is asymmetric in frequency, due to the quantum nature of the fluctuations. For red detuning, the bulk of the spectrum is at positive frequencies. This implies (see text) that the fluctuations induce more downward (cooling) transitions than upward transitions.

$$
A ^ {\pm} = \frac {x _ {\mathrm {Z P F}} ^ {2}}{\hbar^ {2}} S _ {F F} (\omega = \mp \Omega_ {m}) = g _ {0} ^ {2} S _ {N N} (\omega = \mp \Omega_ {m}), \tag {85}
$$

where we introduced the photon number noise spectrum

$$
S _ {N N} (\omega) = \int_ {- \infty} ^ {+ \infty} d t e ^ {i \omega t} \langle (\hat {a} ^ {\dagger} \hat {a}) (t) (\hat {a} ^ {\dagger} \hat {a}) (0) \rangle .
$$

By exploiting shifted photon operators, one can show (Marquardt et al., 2007) that the photon number spectrum of a laser-driven cavity is

$$
S _ {N N} (\omega) = \bar {n} _ {\mathrm {c a v}} \frac {\kappa}{\kappa^ {2} / 4 + (\Delta + \omega) ^ {2}}. \tag {86}
$$

Inserting this into Eq. (85), one obtains  $A^{\pm}$  and from there the optomechanical damping rate  $\Gamma_{\mathrm{opt}} = A^{-} - A^{+}$ , which coincides with the expression obtained using the linearized equations of motion [Sec. V.B.2, Eq. (59)]. We obtain the final minimum phonon number (84) as

$$
\bar {n} _ {\min } = \left(\frac {A ^ {-}}{A ^ {+}} - 1\right) ^ {- 1} = \left(\frac {(\kappa / 2) ^ {2} + (\Delta - \Omega_ {m}) ^ {2}}{(\kappa / 2) ^ {2} + (\Delta + \Omega_ {m}) ^ {2}} - 1\right) ^ {- 1}. \tag {87}
$$

Experimentally, one can still vary the laser detuning  $\Delta$  to minimize this expression. In the resolved-sideband regime  $\kappa \ll \Omega_{m}$ , this leads to

$$
\bar {n} _ {\min } = \left(\frac {\kappa}{4 \Omega_ {m}}\right) ^ {2} <   1, \tag {88}
$$

which permits ground-state cooling, while in the opposite limit  $(\kappa \gg \Omega_{m})$  we find

$$
\bar {n} _ {\min } = \frac {\kappa}{4 \Omega_ {m}} \gg 1. \tag {89}
$$

These two results are almost identical to the case of atomic laser cooling (in the atomic laser cooling expressions, the scalar prefactor is different due to the directional dependence of the spontaneous emission).<sup>16</sup>

In the presence of a thermal environment, the final phonon number (83) can be written as the result of coupling to two baths at average occupations  $\bar{n}_{\mathrm{min}}$  and  $\bar{n}_{\mathrm{th}}$  with coupling rates  $\Gamma_{\mathrm{opt}}$  and  $\Gamma_{m}$ , respectively,

$$
\bar {n} _ {f} = \frac {\Gamma_ {\mathrm {o p t}} \bar {n} _ {\min } + \Gamma_ {m} \bar {n} _ {\mathrm {t h}}}{\Gamma_ {\mathrm {o p t}} + \Gamma_ {m}}. \tag {90}
$$

This result of the quantum theory of optomechanical back-action cooling was derived by Marquardt et al. (2007) and Wilson-Rae et al. (2007). Note that in the resolved-sideband regime, for the limit  $\Gamma_{\mathrm{opt}} \gg \Gamma_m$ , the suppression of the thermal occupation can be expressed via the so-called quantum cooperativity  $\mathcal{C}_{\mathrm{qu}} = \mathcal{C} / \bar{n}_{\mathrm{th}}$ . We have  $\Gamma_m \bar{n}_{\mathrm{th}} / \Gamma_{\mathrm{opt}} = 1 / \mathcal{C}_{\mathrm{qu}}$ .

# 1. Finite thermal cavity occupancy

Equation (90) is modified when the cooling field has thermal occupation. This is, in particular, the case for microwave fields due to their low frequency. If the cavity occupation is given by  $\bar{n}_{\mathrm{cav}}^{\mathrm{th}}$ , then the final occupation is modified to (in the resolved-sideband limit)

$$
\bar {n} _ {f} = \bar {n} _ {\mathrm {t h}} \frac {\Gamma_ {m}}{\Gamma_ {\mathrm {e f f}}} + \bar {n} _ {\mathrm {c a v}} ^ {\mathrm {t h}} + \frac {\kappa^ {2}}{1 6 \Omega_ {m} ^ {2}}, \tag {91}
$$

where  $\Gamma_{\mathrm{eff}} = \Gamma_{\mathrm{opt}} + \Gamma_m$ . This implies that the final phonon number can never be below the effective thermal occupation of the drive field (Dobrindt, Wilson-Rae, and Kippenberg, 2008). It should be noted that when the radiation field and the mechanical oscillator initially have the same bath temperature (as is the case in equilibrium, without extra absorption), the equilibration of these two oscillators of frequency  $\omega_{\mathrm{cav}}$  and  $\Omega_m$  will lead to an effective cooling of the lower-frequency mechanical oscillator, as

$$
\bar {n} _ {\mathrm {t h}} \approx \frac {k _ {B} T _ {\mathrm {b a t h}}}{\hbar \Omega_ {m}} \gg \bar {n} _ {\mathrm {c a v}} \approx \frac {k _ {B} T _ {\mathrm {b a t h}}}{\hbar \omega_ {\mathrm {c a v}}}.
$$

# 2. Equations-of-motion approach

An alternative way to calculate the final phonon number is to write down the linearized equations of motion for the oscillator and light field, eliminate the light field dynamics, and exploit the known spectra of the quantum Langevin forces

driving both the mechanics and the cavity (see Sec. III.C).<sup>17</sup> We do this by considering the influence of the quantum backaction force noise driving the mechanical oscillator. Adopting the classical equations of motion for the mechanical oscillator (but keeping the quantum part of the symmetrized noise spectrum), we find an average energy of

$$
\langle E _ {m} \rangle = \int_ {- \infty} ^ {+ \infty} d \omega | \chi_ {m, \mathrm {e f f}} (\omega) | ^ {2} \bar {S} _ {F F} (\omega) m _ {\mathrm {e f f}} \omega^ {2},
$$

where  $\bar{S}_{FF}$  is the symmetrized version of the spectrum introduced above and we assumed the laser to be dominant,  $\Gamma_{\mathrm{eff}}\gg \Gamma_m$  , and also  $\Omega_{m}\gg \Gamma_{\mathrm{eff}}$  . This leads to the correct quantum result (Stenholm, 1986):

$$
\langle E _ {m} \rangle = \frac {\hbar \Omega_ {m}}{2} \left(1 + \frac {A ^ {+}}{A ^ {-} - A ^ {+}}\right).
$$

This expression reveals that the energy, consisting of the zero-point motion and an additional residual term, is caused by the quantum fluctuations of the laser field. The fact that the quantum fluctuations of the laser field also give rise to the zero-point energy can be understood by noting that the dominant bath that the mechanical oscillator is coupled to is the laser field itself when  $\Gamma_{\mathrm{eff}} \gg \Gamma_m$ . In this sense then, the correct quantum limit for cooling can be formulated on a semiclassical basis, where it is sufficient to consider only the quantum fluctuations of the drive field.

# 3. Optical output spectrum

The output spectrum of the light that emerges from the optomechanical cavity can be calculated using the input-output formalism (Sec. III.C). In close analogy with the fluorescence spectrum of a laser-cooled trapped ion, the spectrum is given by

$$
\begin{array}{l} S (\omega) \approx I _ {0} \delta (\omega - \omega_ {L}) + A ^ {-} \bar {n} _ {f} I _ {\text {s i d e}} (\omega - \Omega_ {m}) \\ + A ^ {+} \left(\bar {n} _ {f} + 1\right) I _ {\text {s i d e}} \left(\omega + \Omega_ {m}\right). \tag {92} \\ \end{array}
$$

This spectrum refers to the frequency-resolved photon flux. Here

$$
I _ {\mathrm {s i d e}} (\omega) = \frac {1}{2 \pi} \frac {\Gamma_ {\mathrm {e f f}}}{\left(\omega - \omega_ {L}\right) ^ {2} + \Gamma_ {\mathrm {e f f}} ^ {2} / 4}
$$

$$
\bar {n} _ {f} = \frac {\Gamma_ {\mathrm {o p t}} \bar {n} _ {\mathrm {m i n}} + \Gamma_ {m} \bar {n} _ {\mathrm {t h}}}{\Gamma_ {\mathrm {o p t}} + \Gamma_ {m}} + \frac {\gamma_ {\mathrm {s c a t}}}{\kappa}.
$$

The analytical form of the scattering rate depends on the geometry of the mechanical oscillator under consideration. For the case of a small sphere, trapped within a Fabry-Pérot cavity, an analytic solution of  $\gamma_{\mathrm{scat}}$  can be derived (Chang et al., 2010; Romero-Isart et al., 2010).

![](images/b47596136e7f25bcc0f8ff752adbcf0e39ac1ab5d3baba57e926901db806d6c8.jpg)

![](images/6b1171a06cddffd0f957a6b5a773c8a072903b4c0dab91c9a8ebc7b8966adcd4.jpg)  
FIG. 29 (color online). (a) Sideband thermometry revealing the growing asymmetry between photons scattered into the cavity resonance when increasing the cooling laser power. Courtesy of O. Painter. From Safavi-Naeini, 2012. (b) Schematics of the readout scheme. Left: A readout laser  $(\omega_{L})$  that is red detuned by the mechanical frequency  $\Omega_{m}$  primarily scatters photons into the Stokes motional sideband. Right: Blue detuning of the readout laser by  $\Omega_{m}$  primarily generates photons at the anti-Stokes motional sideband.

![](images/8ca982b94a26f377b65fc76dfef7d6eca67285495698787eab6ea23f454ab442.jpg)

is the Lorentzian shape of the sidebands, where the width of the sidebands is given by the overall effective mechanical damping rate  $\Gamma_{\mathrm{eff}}$ . The weight of the main peak<sup>18</sup> at the laser frequency is (for a single-sided Fabry-Pérot resonator)

$$
I _ {0} = \frac {\kappa_ {\mathrm {e x}}}{\kappa} \frac {P}{\hbar \omega_ {L}} \left[ \frac {\kappa}{\kappa_ {\mathrm {e x}}} - \frac {\kappa^ {2} - \kappa_ {\mathrm {e x}} \kappa}{\Delta^ {2} + \frac {1}{4} \kappa^ {2}} \right].
$$

As expected, the spectrum consists (in addition to the carrier) of blueshifted (anti-Stokes) photons at  $\omega = \omega_{L} + \Omega_{m}$  [last term in Eq. (92)] and redshifted (Stokes) photons at  $\omega = \omega_{L} - \Omega_{m}$  (second-to-last term). The sideband asymmetry changes as a function of the cooling laser power. Detailed balance causes the initially asymmetric sidebands (as  $A^{-} \gg A^{+}$ ) to become progressively more symmetric, with  $A^{+}(\bar{n}_{f} + 1) = A^{-}\bar{n}_{f}$  in the limit where  $\bar{n}_{f}$  is entirely determined by the cooling process  $(\Gamma_{\mathrm{opt}}\bar{n}_{\mathrm{min}} \gg \Gamma_{m}\bar{n}_{\mathrm{th}})$ . This provides a means to determine the temperature of the mechanical oscillator via the spectral weight of the two sidebands, a technique that has been widely used in the trapped-ion community and is termed sideband thermometry (Diedrich et al., 1989). There the spectral weight can be directly measured via optical shelving (Leibfried et al., 2003). A variant of this method was recently demonstrated in an optomechanical cooling experiment (Safavi-Naeini, Chan et al., 2013; Weinstein et al., 2014) (see Fig. 29). In this method the excitation laser is placed on the upper  $(\Delta = +\Omega_{m})$  and subsequently on the lower  $(\Delta = -\Omega_{m})$  sideband and the rate of scattering into the cavity  $\dot{N}^{\mathrm{cav}}$  is measured. This yields

$$
\dot {N} ^ {\mathrm {c a v}} (\Delta = \Omega_ {m}) = \frac {\kappa_ {\mathrm {e x}}}{\kappa} A ^ {+} (\bar {n} _ {f} + 1)
$$

![](images/fd8a6a145ca28012ba3a91022a6652d3de9808eb002a9614952246e3d5ef761d.jpg)  
FIG. 30 (color online). Experimental results for optomechanical laser cooling. We display the initial and final phonon numbers (logarithmic scale) vs the sideband-resolution parameter  $\Omega_{m} / \kappa$ . The quantum limit for the minimum achievable phonon number is plotted as well. MIT: (Corbitt, Chen et al., 2007); LKB: (Arcizet et al., 2006a); Yale: (Thompson et al., 2008); Vienna: (Groblacher, Hertzberg et al., 2009); MPQ: (Schliesser et al., 2009); JILA: (Teufel et al., 2008); Cornell 2010: (Rocheleau et al., 2010); Caltech 2011: (Chan et al., 2011); EPFL 2011: (Riviere et al., 2011); Boulder 2011: (Teufel, Donner et al., 2011); MIT 2011: (Schleier-Smith et al., 2011).

and

$$
\dot {N} ^ {\text {c a v}} (\Delta = - \Omega_ {m}) = \frac {\kappa_ {\text {e x}}}{\kappa} A ^ {-} (\bar {n} _ {f}).
$$

# B. Experiments and practical limitations

# 1. Experimental developments

The first experimental attempts to damp the motion of a mechanical oscillator with radiation-pressure dynamical back-action were carried out by Braginsky, Manukin, and Tikhonov (1970). In these experiments a microwave cavity was employed, and a modification of the damping rate of the end-mirror pendulum could be observed. Microwave cooling deeply in the resolved-sideband regime was moreover implemented in the field of gravitational wave detectors, in the form of a high- $Q$  cryogenic sapphire transducer, where it served the role of reducing the effective noise temperature (Cuthbertson et al., 1996).

Optical feedback cooling of a micromechanical mirror using the radiation-pressure force was demonstrated by Cohadon, Heidmann, and Pinard (1999). Dynamical back-action cooling in the optical domain was achieved using photothermal forces by Höhberger-Metzger and Karrai (2004), and radiation-pressure forces by Arcizet et al. (2006a), Gigan et al. (2006), and Schliesser et al. (2006).

These early experiments operated in the Doppler regime  $(\kappa >\Omega_{m})$  .As outlined in Sec. VII.A, an important requirement for many applications is the resolved-sideband regime. This was demonstrated in the microwave regime for the first time (Cuthbertson et al., 1996) and later in the optical domain (Schliesser et al., 2008). Since then, a plethora of novel systems [see, e.g., (Thompson et al. (2008), Teufel et al. (2008), and Lin et al. (2009) and many more] have been realized in the

resolved-sideband regime (see Fig. 30). All these experiments were, however, essentially room-temperature experiments.

To initialize a mechanical oscillator in the ground state at thermal equilibrium, the condition  $k_{B}T / \hbar \Omega_{m}\ll 1$  has to be realized. In general, the probability of finding the system in the ground state is related to the average occupation number  $\bar{n}$  by  $P_0 = 1 / (1 + \bar{n})$ . Note that in the field of trapped-ion experiments, the motional ground state can nowadays routinely be prepared with more than  $97\%$  probability (Diedrich et al., 1989; Leibfried et al., 2003). Reaching the ground state (often referred to as  $\bar{n} < 1$ ) is challenging for low-frequency oscillators, as the thermal freezeout for a  $1\mathrm{MHz}$  oscillator equates to  $50~\mu \mathrm{K}$ . These temperatures are far below those attained with a dilution refrigerator. Ground-state cooling with conventional cryogenics can therefore be reached only for  $\mathrm{GHz}$  oscillators. Indeed, the first demonstration of quantum control at the single-phonon level was demonstrated with a  $6\mathrm{GHz}$  piezoelectric mechanical oscillator cooled to below  $50~\mathrm{mK}$  (O'Connell et al., 2010).

It is challenging to reach the quantum ground state of micromechanical oscillators at lower frequencies. A widely pursued strategy has been to combine cryogenic precooling with dynamical backaction laser cooling. The precooling thereby allows one to reduce the starting mode temperature. This technique has over the past years allowed a substantial reduction of the phonon occupancy.

While initial cryogenic experiments demonstrated cooling to a level of a few dozen quanta in the optical domain (Groblacher, Hertzberg et al., 2009; Park and Wang, 2009; Schliesser et al., 2009), further experimental progress allowed the reduction of the motional energy to a level close to the zero-point motion in several experiments in both the microwave domain (Rocheleau et al., 2010; Teufel, Donner et al., 2011) and the optical domain (Chan et al., 2011; Riviere et al., 2011), with ground-state probabilities ranging from 0.2 to 0.7.

Specifically, in the microwave domain, increasing the coupling strength by improved cavity designs resulted in cooling to around 4 quanta (Rocheleau et al., 2010)  $(P_0 = 0.2)$  and to  $\bar{n}_f = 0.38$ $(P_0 = 0.72)$  using a superconducting resonator coupled to a micromechanical drum mode (Teufel, Donner et al., 2011). In both experiments the limitation for the occupancy was set by the fact that the cavity had a low, yet finite, residual thermal occupation. This also led to the observation of squashing in the mechanical noise spectrum data of this experiment for some drive powers. All these experiments have been performed in dilution refrigerators with base temperatures as low as about  $25\mathrm{mK}$ .

Also in the optical domain, new geometries allowed one to improve the cooling performance to  $\bar{n}_f = 1.7$  quanta  $(P_0 = 0.37)$  for improved microtoroidal resonators (Verhagen et al., 2012) and to 0.8 quanta  $(P_0 = 0.54)$  for a nanomechanical mode of a photonic crystal beam (Chan et al., 2011). In the experiments using spoke-supported microtoroids (Verhagen et al., 2012), the occupancy was limited by the cavity decay rate  $\kappa$  due to the onset of strong coupling (see Sec. VII.C.1), and by reheating of the sample due to the laser (Riviere et al., 2011). The experiment by Chan et al. (2011) involved a  $3.67\mathrm{GHz}$  mechanical mode and an external-cavity diode laser drive. The cooling was limited by reheating of the sample to its initial temperature of ca.  $20\mathrm{K}$  inside a  $\mathrm{He}^4$  flowthrough cryostat and

the fact that the mechanical  $Q$  factor exhibited a strong temperature dependence, as well as unwanted effects at higher drive powers. In all cases, higher-fidelity ground-state preparation (as achieved in ion trapping) will require further reduction of the effects of laser heating of the sample, further increases of the mechanical quality factor, or higher optomechanical coupling rates.

A selection of cooling experiments is displayed in Fig. 30. There we plot the initial and final phonon numbers versus the sideband-resolution parameter  $\Omega_{m} / \kappa$  that determines the minimum achievable phonon number.

The technique of radiation-pressure dynamical backaction cooling has many similarities to atomic laser cooling (Diedrich et al., 1989; Leibfried et al., 2003). Nevertheless there are substantial differences. For instance, optomechanical cooling does not proceed by the use of a two-level system, but by a cavity that is excited with a coherent laser field. From an experimental point of view, optomechanical cooling of a mechanical oscillator to the ground state is impeded by several challenges. First, in contrast to atomic laser cooling where the atoms are well isolated, mechanical systems are usually coupled to a high-temperature bath with correspondingly large motional heating rates. In addition, optomechanical laser cooling is extraordinarily sensitive to laser phase (i.e., frequency) noise. In the following discussion, we review the fundamental limits of cooling due to both laser phase noise and thermorefractive cavity noise.

# 2. Laser phase noise

In Sec. VII.A, the laser input noises were considered to be essentially quantum noises, i.e., the laser beam is considered a perfect coherent state. However, real laser systems exhibit excess noise, e.g., due to relaxation oscillations that can be derived from the dynamical equations of laser theory. In these cases, the laser frequency noise cannot simply be inferred by the laser linewidth, and simplified models fail to provide an accurate description of the laser's phase and amplitude noise. Lasers exhibit generally significant excess noise for frequencies below the relaxation oscillation frequency, which can differ strongly, from the kHz-MHz range in Nd:YAG or fiber lasers to several GHz in the case of diode lasers (Vahala, Harder, and Yariv, 1983; Wieman and Hollberg, 1991; Jayich et al., 2012; Kippenberg, Schliesser, and Gorodetksy, 2013; Safavi-Naeini, Groblacher et al., 2013). This noise will lead to radiation-pressure fluctuations that heat the mechanical oscillator and impact optomechanical experiments, as discussed by Diosi (2008), Schliesser et al. (2008), Rabl et al. (2009), Jayich et al. (2012), and Safavi-Naeini, Chan et al. (2013). For ground-state cooling, laser phase noise at  $\Omega_{m}$  needs to be below (Rabl et al., 2009) (see the Appendix for more details)

$$
\bar {S} _ {\omega \omega} \left(\Omega_ {m}\right) <   \frac {g _ {0} ^ {2}}{k _ {B} T / \hbar Q _ {m}}. \tag {93}
$$

Moreover, phase noise impacts state transfer and entanglement generation (Abdi et al., 2011; Ghobadi, Bahrampour, and Simon, 2011) and can impact sideband asymmetry measurements, as discussed by Jayich et al. (2012), Safavi-Naeini, Chan et al. (2013), and Harlow (2013). For a more detailed discussion see Appendix A.3.

# 3. Cavity frequency noise

In addition to laser phase noise, which in principle can be mitigated by properly filtered laser systems, a more fundamental limit to dynamical backaction laser cooling arises from the fact that at finite temperature the cavity frequency exhibits thermodynamical fluctuations (Gorodetsky and Grudinin, 2004). These are due to local temperature fluctuations that affect the dielectric properties of the cavity itself (for microtoroids, microspheres, or photonic crystals) or of the mirror. For more details, see Appendix A.2.

# C. Strong-coupling regime

We now discuss what happens when the laser power  $P$  is increased further. At first, this will just improve cooling, since  $\Gamma_{\mathrm{opt}} \propto P$ . However, as we see in the Sec. VII.C.1, qualitatively new features start to appear when  $\Gamma_{\mathrm{opt}} \sim \kappa$ , or equivalently when  $g \sim \kappa$ . This regime is referred to as the strong-coupling regime, where the driven optical mode and the mechanical mode hybridize to form two new modes, with a splitting set by  $2g$ . Furthermore, even for lower laser drive powers interesting features in the transmission spectrum of the cavity appear if it is probed weakly in the presence of a strong drive. This is the phenomenon of optomechanically induced transparency, discussed in Sec. VII.C.2.

# 1. Optomechanical normal-mode splitting

The strong-coupling regime is discussed most easily if we assume the nondissipative part of the Hamiltonian to dominate all decay channels, i.e.,  $g \gg \kappa$ ,  $\Gamma_{m}$ . In that case, we can just consider the following part of the linearized Hamiltonian:

$$
\hat {H} = - \hbar \Delta \delta \hat {a} ^ {\dagger} \delta \hat {a} + \hbar \Omega_ {m} \hat {b} ^ {\dagger} \hat {b} - \hbar g (\delta \hat {a} ^ {\dagger} + \delta \hat {a}) (\hat {b} + \hat {b} ^ {\dagger}). \tag {94}
$$

In the most interesting red-detuned regime, where  $\Delta \approx -\Omega_{m}$ , we can even start our discussion by employing the rotating-wave approximation for the coupling  $-\hbar g(\delta \hat{a}^{\dagger}\hat{b} +\delta \hat{a}\hat{b}^{\dagger})$  which is the beam-splitter Hamiltonian of Eq. (31). The Hamiltonian of these two coupled oscillators is then easily diagonalized by going over to the two eigenmodes. These modes now represent excitations that are hybrids between the mechanical oscillations  $(\hat{b})$  and the fluctuations of the driven cavity mode  $(\delta \hat{a})$  around the strong coherent amplitude. Their eigenfrequencies are

$$
\omega_ {\pm} = \frac {\Omega_ {m} - \Delta}{2} \pm \sqrt {g ^ {2} + \left(\frac {\Omega_ {m} + \Delta}{2}\right) ^ {2}}. \tag {95}
$$

In particular, right at resonance  $\Delta = -\Omega_{m}$ , one observes an avoided crossing, with a splitting of  $\omega_{+} - \omega_{-} = 2g$  between the two excitation branches. At this point, the eigenmodes are symmetric and antisymmetric superpositions of light and mechanics, with new annihilation operators  $(\delta \hat{a} \pm \hat{b}) / \sqrt{2}$ . Far from resonance, one recovers the two bare frequencies  $-\Delta$  and  $\Omega_{m}$ , and the excitations become again of purely optical and mechanical nature, respectively.

This is the picture appropriate for  $g \gg \kappa$ , where we assume that  $\kappa \gg \Gamma_{m}$  is the dominant decay channel. In the opposite

case  $g \ll \kappa$  (assumed in Secs. VII.A and VII.B), the two peaks at  $\omega_{\pm}$  merge and the avoided crossing cannot be observed.

In principle, the complete scenario, including the decay channels and the transition into the strong-coupling regime, is described fully by the solution of the linearized equations of motion (42) and (43). As discussed in Sec. V.B, one can solve these coupled equations analytically. In this way, for example, one arrives at an exact expression for the mechanical susceptibility, Eq. (56). When plotting this versus frequency for increasing values of  $g$ , one observes peaks at  $\omega_{\pm}$  that can be clearly resolved for  $g \gg \kappa$ . The evolution of the mechanical spectrum in the strong-coupling regime  $g > \kappa / 4$  as a function of laser detuning  $\Delta$  is displayed in Fig. 31. The same kind of analysis also applies to the transmission spectrum of the cavity which can be expressed via the same solution.

However, instead of referring to these rather lengthy exact expressions, we simplify things by considering the regime  $\Delta \approx -\Omega_{m}$ , which allows us to perform the rotating-wave approximation already employed above. We then write the following linearized equations of motion for the mean values:

$$
\binom {\langle \dot {\delta} \hat {a} \rangle} {\dot {\hat {b}}} = - i \left( \begin{array}{c c} - \Delta - i \frac {\kappa}{2} & - g \\ - g & \Omega_ {m} - i \frac {\Gamma_ {m}}{2} \end{array} \right) \binom {\langle \delta \hat {a} \rangle} {\langle \hat {b} \rangle}. \tag {96}
$$

Solving for the complex eigenvalues of this non-Hermitian matrix, we recover the expression for the two branches  $\omega_{\pm}$  given in Eq. (95), except with the replacements  $\Delta \mapsto \Delta + i\kappa / 2$  and  $\Omega_m \mapsto \Omega_m - i\Gamma_m / 2$ . With  $\delta \equiv -\Delta - \Omega_m$ , we have

$$
\omega_ {\pm} = \Omega_ {m} + \frac {\delta}{2} - i \frac {\kappa + \Gamma_ {m}}{4} \pm \sqrt {g ^ {2} + \left(\frac {\delta + i (\Gamma_ {m} - \kappa) / 2}{2}\right) ^ {2}}.
$$

![](images/8893aa1a8ca8b11a9fd9ed5c75a52332fee391df0c76efa8da618e73c4cf878f.jpg)  
FIG. 31 (color online). Mechanical frequency spectrum (frequency on vertical axis) as a function of laser detuning, for a strongly coupled optomechanical system. An avoided crossing, with a splitting of size  $2g$ , appears when the negative detuning equals the mechanical resonance frequency. This is due to the hybridization of the mechanical mode (frequency  $\Omega_{m}$ ) and the driven cavity mode (effective frequency  $-\Delta$ ).

In particular, at resonance  $\Delta = -\Omega_{m}$ $(\delta = 0)$  we find

$$
\omega_ {\pm} = \Omega_ {m} - i \frac {\kappa}{4} \pm \sqrt {g ^ {2} - \left(\frac {\kappa}{4}\right) ^ {2}},
$$

where we assumed  $\kappa \gg \Gamma_{m}$  to slightly simplify this formula. Thus, the eigenfrequencies change character at the threshold  $g = \kappa /4$ , where the root changes from purely imaginary  $(g < \kappa /4)$  to real valued  $(g > \kappa /4)$ . This corresponds to the transition into the strong-coupling regime, with two well-resolved peaks. Each of those peaks is of width [full width at half maximum (FWHM)]  $\kappa /2$ . This is because both of these excitations are half optical, and so each of them shares one-half of the optical decay rate. Away from the degeneracy point  $\Delta = -\Omega_{m}$ , the relative contributions of the two decay channels  $\Gamma_{m}$  and  $\kappa$  get reweighted according to the unequal distribution of optical and mechanical excitation in the two branches.

It turns out that cooling becomes less efficient when one approaches the strong-coupling regime. In fact, the exact solution of the linearized equations of motion can be employed to derive the appropriate modification to the formulas for the final occupancy in the case of strong optomechanical coupling (Marquardt et al. (2007)):

$$
\bar {n} _ {f} = \bar {n} _ {f} ^ {(0)} + \bar {n} _ {\text {t h}} \frac {\Gamma_ {m}}{\kappa} + 2 \bar {n} _ {\min } \frac {\Gamma_ {\text {o p t}}}{\kappa}. \tag {97}
$$

Here  $\bar{n}_f^{(0)}$  is the standard result from Eq. (90) derived above for the weak-coupling regime  $g\ll \kappa$ , and to simplify the expression we assumed the resolved-sideband regime  $\kappa \ll \Omega_{m}$ , where  $\bar{n}_{\mathrm{min}} = (\kappa /4\Omega_m)^2$  and  $\Gamma_{\mathrm{opt}} = 4g^2 /\kappa$ , as well as strong cooling  $\Gamma_{\mathrm{opt}}\gg \Gamma_{m}$ , neglecting terms of still higher orders in  $\kappa /\Omega_{m}$ .

The peak splitting in the strong-coupling regime  $(g\gg \kappa ,\Gamma_{m})$  and the resulting modification to cooling (notably the limitation arising from the finite cavity decay rate) was predicted by Marquardt et al. (2007). It was analyzed extensively by Dobrindt, Wilson-Rae, and Kippenberg (2008) and Wilson-Rae et al. (2008); see also Marquardt, Clerk, and Girvin (2008) and Groblacher, Hammerer et al. (2009). More generally, the full expression (Dobrindt, WilsonRae, and Kippenberg, 2008; Wilson-Rae et al., 2008) for  $\bar{n}_f$  can be given, including any possible thermal occupation of the cavity field (which has been observed in microwave setups):

$$
\begin{array}{l} \bar {n} _ {f} = \bar {n} _ {\mathrm {t h}} \frac {\Gamma_ {m}}{\kappa} \frac {4 g ^ {2} + \kappa^ {2}}{4 g ^ {2} + \Gamma_ {m} \kappa} + \frac {4 g ^ {2}}{4 g ^ {2} + \Gamma_ {m} \kappa} \bar {n} _ {\mathrm {c a v}} ^ {\mathrm {t h}} \\ + \bar {n} _ {\mathrm {t h}} \frac {\Gamma_ {m}}{\kappa} \frac {g ^ {2}}{\Omega_ {m} ^ {2}} + \left(\bar {n} _ {\mathrm {c a v}} ^ {\mathrm {t h}} + \frac {1}{2}\right) \frac {\kappa^ {2} + 8 g ^ {2}}{8 \Omega_ {m} ^ {2}}. \tag {98} \\ \end{array}
$$

The first experimental observation of strong optomechanical coupling  $(g > \kappa, \Gamma_{m})$  was reported by Gröblacher, Hammerer et al. (2009) (see Fig. 32). Subsequently, experiments on other setups have been able to achieve significantly larger ratios  $g / \kappa$ ; see Teufel, Li et al. (2011). In addition, the regime of  $g > \kappa, \Gamma_{m}\bar{n}_{\mathrm{th}}$  (see below) was reached as well (Teufel, Donner et al., 2011; Teufel, Li et al., 2011; Verhagen et al., 2012), where coherent quantum-state transfer between light and mechanics could take place (see Sec. X.E).

![](images/fd100d3251168386101be6ffff9b7400a483e5b0018a38fff16c4cff0dc2882f.jpg)  
FIG. 32 (color online). Experimental observation of strong coupling of a mechanical oscillator to a light field ("parametric normal-mode splitting"). From top to bottom: the light intensity and thereby  $g = g_0 \sqrt{\bar{n}_{\mathrm{cav}}}$  is increased. From Gröblacher, Hammerer et al., 2009.

The photon statistics of an optomechanical system in the strong-coupling regime have been found to display interesting antibunching behavior and photon correlations (Huang and Agarwal, 2010), and the same analysis discussed four-wave mixing in a setup driven by a strong pump field and another (Stokes) field. One can also consider having a nonlinear medium inside the optical cavity. Huang and Agarwal (2009c) studied the effects of an optical parametric amplifier cavity on the phenomenon of optomechanical normal-mode splitting.

The spectroscopic signatures of strong coupling indicate whether the coupling exceeds the cavity decay rate. If the coupling rate also exceeds the thermal decoherence rate  $(\gamma = \Gamma_{m}\bar{n}_{\mathrm{th}})$ , the interaction between the mechanical oscillator and the light field becomes quantum coherent, i.e., the time scale of the mutual coupling is faster than the time scale for one quantum of noise to enter from the environment:

$$
g > \left\{\Gamma_ {m} \bar {n} _ {\text {t h}}, \kappa \right\}.
$$

This parameter regime of coherent coupling is a precondition for many quantum protocols such as quantum-state transfer between the cavity field and a mechanical mode (see Sec. X.E). Experimentally, this regime has been reached using a superconducting membrane coupled to an  $LC$  circuit (Teufel, Donner et al., 2011), and in the optical domain using a toroidal spoke-supported microresonator (Verhagen et al., 2012) (see Fig. 33).

# 2. Optomechanically induced transparency

Electromagnetically induced transparency (Fleischhauer, Imamoglu, and Marangos, 2005) is a phenomenon which occurs in multilevel atoms and manifests itself as a cancellation of absorption in the presence of an auxiliary laser field. It arises from electronic interference or, in an equivalent

![](images/bcc881ae4f44c5342e0b90aaf93a871dba827c3828e03935f151b801ee3a85c1.jpg)  
FIG. 33 (color online). Experimental observation of the coherent coupling regime, i.e.,  $g > \{\kappa, \bar{n}_m\Gamma_m\}$ , between a mechanical oscillator and a microwave cavity mode as well as an optical cavity mode. The data show the splitting in the mechanical displacement spectrum as a function of increasing drive power [left panel, for the case of a superconducting drum resonator (Teufel, Li et al., 2011), courtesy of J. Teufel] and as a function of the laser detuning around the lower sideband [right panel, for the case of a spoke-supported microtoroid resonator (Verhagen et al., 2012), courtesy of T. J. Kippenberg].

![](images/2df931564daf4581651e6a3d26a01102e28f89194229833c0d944fb003292284.jpg)

![](images/125527e6b4d3eefd29b5e05f87fdfaaa8b58bb056ebe9db80bc4cd395db37ac2.jpg)  
FIG. 34 (color online). (a) Level scheme for optomechanically induced transparency. A strong control laser on the red sideband drives the optomechanical system, while a weak probe laser scans across the cavity resonance and takes the (b) spectrum of the driven system, which displays a sharp transparency feature (for a side-coupled toroid setup). The linewidth of that feature is given by the mechanical linewidth (at weak driving), much narrower than the cavity linewidth. Adapted from Schliesser, 2009, and Schliesser and Kippenberg, 2010.

![](images/2138db61cbb5336dde4d194c7a31452fbcc161ca7e7ec9d7be8f3647811268ea.jpg)

picture, is due to a dark-state resonance of the excited state (see Fig. 34). This phenomenon has been demonstrated for cold atomic ensembles, giving rise to a host of phenomena, ranging from optical pulse storage to slowing or advancing of light pulses. An analogous phenomenon also occurs in optomechanical systems, as predicted theoretically by Schliesser (2009) and Agarwal and Huang (2010) and analyzed further for optical pulse storage (Chang et al., 2011). Optomechanically induced transparency has been observed in experiments (Weis et al., 2010; Safavi-Naeini et al., 2011) (see Fig. 35). On injecting a strong control laser beam into the lower (red-detuned) sideband of an optomechanical system, the optomechanical interaction causes the cavity resonance, as seen by a second, weak probe laser field, to be rendered transparent. The simultaneous presence of a strong control laser  $(\bar{s} e^{-i\omega_{c}t})$  and a weak probe laser  $(\delta s e^{-i\omega_{p}t})$  leads to a transmission  $|\mathcal{R}_p|^2$  of the weak probe laser given by

![](images/bc478a53c990f3d66851c947e56078cef91c2c89022d4a13c7ef132920272436.jpg)  
FIG. 35 (color online). Optomechanically induced transparency observed in the experiment. Data from a photonic crystal setup (Safavi-Naeini et al., 2011) (left panel) and for a microtoroid setup (Weis et al., 2010) (right panel). Note that in the case of a photonic crystal the OMIT signature is visible in both the reflected and the transmitted signals.

$$
\left| \mathcal {R} _ {p} \right| ^ {2} = \left| 1 - \eta \kappa \frac {\chi_ {\mathrm {o p t}} (\Omega)}{1 + g _ {0} ^ {2} \bar {a} ^ {2} \chi_ {\mathrm {m e c h}} (\Omega) \chi_ {\mathrm {o p t}} (\Omega)} \right| ^ {2}. \tag {99}
$$

Here  $\Delta = \omega_{c} - \omega_{\mathrm{cav}}$  denotes the detuning of the strong control field from the cavity resonance  $\omega_{\mathrm{cav}}$ , and  $\Omega$  denotes the detuning between the control laser and probe laser, i.e.,  $\Omega = \omega_{p} - \omega_{c}$ . Moreover, the coupling efficiency  $\eta = \kappa_{\mathrm{ex}} / \kappa$  has been introduced, and the mechanical susceptibility<sup>19</sup>  $\chi_{\mathrm{mech}}^{-1}(\Omega) = -i(\Omega - \Omega_m) + \Gamma_m / 2$  as well as the optical susceptibility  $\chi_{\mathrm{opt}}^{-1}(\Omega) = -i(\Omega + \bar{\Delta}) + \kappa / 2$ . Note that, with regard to the transmission, we used the terminology appropriate for a waveguide-coupled unidirectional cavity (e.g., whispering-gallery-mode resonator), and we followed the discussion of Weis et al. (2010). Plotting the expression  $|\mathcal{R}_p|^2$  reveals that when the resonance condition  $\Omega \approx \Omega_m$  is met, a transparency window arises. When the coupling laser is placed on the lower sideband ( $\Delta = -\Omega_m$ ), the expression for the transmission of the probe in the vicinity of  $\Omega = \Omega_m$  (which corresponds to  $\omega_p \approx \omega_{\mathrm{cav}}$ ) reduces to

$$
| \mathcal {R} _ {p} | ^ {2} = \left| \frac {4 \bar {n} _ {\mathrm {c a v}} g _ {0} ^ {2}}{4 \bar {n} _ {\mathrm {c a v}} g _ {0} ^ {2} + \Gamma_ {m} \kappa - 2 i (\Omega - \Omega_ {m}) \kappa} \right| ^ {2},
$$

where for simplicity we assumed critical coupling, i.e.,  $\eta = 1 / 2$ . Evaluating the above expression for  $\Omega = \Omega_{m}$  yields

$$
\left| \mathcal {R} _ {p} \right| ^ {2} = \left(\frac {\mathcal {C}}{\mathcal {C} + 1}\right) ^ {2}.
$$

Here  $\mathcal{C}$  is the optomechanical cooperativity  $\mathcal{C} = 4g_0^2\bar{n}_{\mathrm{cav}} / \kappa \Gamma_m$ . Thus a cooperativity of unity is required to change the transmission to  $50\%$ . Note that the assumption underlying these theoretical considerations, of two coherent drive fields, requires from an experimental point of view two laser fields that are coherent for times longer than the effective mechanical damping time.

The physical origin of the transparency window can be understood by realizing that the beat of the probe field and the coupling laser induces a time-varying radiation-pressure force. If the beat frequency matches the mechanical oscillation frequency, then the mechanical oscillator is driven resonantly. The driven oscillator in turn creates sidebands on the intracavity field. Considering the strong-coupling laser only, in the resolved-sideband limit, the lower motional sideband is far off cavity resonance and can be neglected. In contrast, the upper sideband of the coupling laser, created by the mechanical motion, has precisely the same frequency as the probe field and is moreover phase coherent with the probe field. This leads to an interference that yields a cancellation of the intracavity field on resonance, giving rise to the transparency window. The phenomenon thereby results from the destructive interference between reflection amplitudes for photons scattered from the coupling laser and photons of the probe field. The effect of higher-order sidebands was discussed by Xiong et al. (2012).

The width of the (Lorentzian) transparency feature in the weak-coupling regime (where  $\Gamma_{\mathrm{eff}} \ll \kappa$ ) is given by the total effective mechanical damping rate:

$$
\Gamma_ {\mathrm {O M I T}} = \Gamma_ {m} + 4 g _ {0} ^ {2} \bar {n} _ {\mathrm {c a v}} / \kappa = \Gamma_ {\mathrm {e f f}}.
$$

We note that at stronger drive this feature smoothly evolves into the normal-mode splitting discussed above (Sec. VII.C.1). The narrow transparency window is concomitant with a rapid variation of the transmission phase of the probe beam. This implies that a pulse with a bandwidth smaller than  $\Gamma_{\mathrm{OMIT}}$  will experience a group delay (without distortion of the pulse). The change of the phase of the transmitted light is given by (for  $\Delta = -\Omega_m$ )

$$
\phi = \arctan \left(\frac {2 (\Omega - \Omega_ {m}) \kappa}{4 \bar {n} _ {\mathrm {c a v}} g _ {0} ^ {2} + \Gamma_ {m} \kappa}\right).
$$

Evaluating this expression for zero detuning  $(\Omega = \Omega_{m})$  leads to a group delay of

$$
\tau_ {g} = \frac {d \phi}{d \Omega} = \frac {1}{\Gamma_ {m}} \frac {2}{C + 1} = \frac {2}{\Gamma_ {\mathrm {O M I T}}}.
$$

However, the bandwidth of the pulse needs to be smaller than the transparency window for undistorted pulse propagation, which limits the delay-bandwidth product to  $\tau_{g}\Gamma_{\mathrm{OMIT}}\approx 2$  Using an array of optomechanical systems, the delay-bandwidth product can be increased and may therefore serve as a way to store an optical wave form in long-lived phonons. Such cascaded optomechanical systems can be realized using, e.g., photonic crystals (Chang et al., 2011).

# 3. Optomechanically induced amplification and electromagnetically induced absorption

If instead we consider the control laser being injected on the upper sideband  $(\Delta = \Omega_{m})$ , an additional optical signal in the probe beam is amplified (Massel et al., 2011; Safavi-Naeini et al., 2011; Hocke et al., 2012). The analogous effect in atomic physics is referred to as electromagnetically induced absorption (EIA) (Lezama, Barreiro, and Akulshin, 1999). The amplification process can parametrically amplify a small signal (provided the resonance condition is met), by virtue of the constructive interference of the light scattered from the pump (control) to the signal (probe) frequency, in direct

![](images/66edd83c00b23f7a0feba52b33e64d4c332ce10c90d9f02e2cf9d3e6a191aa45.jpg)  
FIG. 36 (color online). Transmission of the probe beam in the presence of a strong control field on the lower sideband (left panel, optomechanically induced transparency, OMIT) and on the upper sideband (right panel, electromagnetically induced absorption, EIA).

![](images/f5351537a588f9c39b3bf110e3210480fd0961cbfc1ae7d7c8ba19f96397053d.jpg)

analogy to the above phenomenon of optomechanically induced transparency (see Fig. 36). Theoretically the phenomenon can be described by the same equations as the effect of transparency, except for the fact that now the mechanical damping is reduced with increasing power on the upper sideband. The maximum gain is set by the maximum power which can be injected onto the upper sideband  $(\Delta = +\Omega_{m})$  which is limited by the onset of the parametric oscillatory instability, in which the coherent amplification of mechanical motion from the noise occurs. The maximum average gain in this case is given by  $G_{\mathrm{av}}(\Delta = \Omega_m)\approx 4(4\Omega_m / \kappa)^2$  (Massel et al., 2011). As for any nondegenerate parametric amplifier, the amplification process has to add one-half a quantum of noise for fundamental reasons (Clerk et al., 2010), and the total added noise is given by  $\bar{n}_{\mathrm{add}} = \bar{n}_m + 1 / 2\approx k_BT / \hbar \Omega_m$  in the presence of thermal fluctuations. In the ideal case the relative phase between pump and signal is not important for the EIA process. However, any relative phase fluctuations between pump and signal need to take place on a time scale long compared to the inverse effective mechanical damping rate.

However, this optical amplification process does not lead to a stimulated optical amplification process, as in the case of optical Brillouin scattering. The reason is that unlike in the optical Brillouin scattering case, the optical dissipation is larger than the mechanical dissipation ( $\kappa \gg \Gamma_{m}$ ). This implies that the mechanical mode can experience exponential buildup, while in a Brillouin laser the opposite is the case.[20]

# VIII. CLASSICAL NONLINEAR DYNAMICS

Up to now we mostly discussed effects that can be fully understood within the linearized equations of motion, i.e., within the quadratic approximation (29) to the optomechanical Hamiltonian. However, the approximation itself can be used to predict its breakdown: In the blue-detuned regime  $(\Delta > 0)$ ,  $\Gamma_{\mathrm{opt}}$  becomes negative, decreasing the overall damping rate. At first, this leads to heating (instead of cooling), enhancing the oscillator's effective temperature. Once the overall damping rate  $\Gamma_m + \Gamma_{\mathrm{opt}}$  becomes negative, an instability ensues. In that case, any small initial (e.g., thermal) fluctuation will at first grow exponentially in time. Later, nonlinear effects will saturate the growth of the mechanical oscillation amplitude (Fig. 37). A steady-state regime is reached, with oscillations proceeding at a fixed amplitude  $A$ . These are called self-induced (backaction-induced) optomechanical oscillations. In fact, they are analogous to the lasing action, but now in a mechanical system and with the incoming laser radiation providing the pump. Therefore, this optomechanical effect can also be understood as one variant of "mechanical lasing" or "phonon lasing." Just as for lasers or

![](images/4a8c986d6d4ac9397ac5d6605cd60058e7693bc90eafb183207d52cc3b12d907.jpg)  
FIG. 37 (color online). Optomechanical parametric instability toward "self-induced oscillations" (mechanical lasing): displacement  $x$  vs time  $t$ . In a system with a sufficiently strong blue-detuned laser drive, the mechanical oscillations can display antidamping  $(\Gamma_{\mathrm{eff}} < 0)$ . This leads first to exponential growth of any initial fluctuations, which then finally saturates due to nonlinear effects, resulting in self-sustained mechanical oscillations at a stable amplitude  $A$ .

masers, the optomechanical system displays a threshold and linewidth narrowing above the threshold, described by a Schawlow-Townes-type limit.

# A. Parametric instability and attractor diagram

In this section, we present the classical theory of the optomechanical instability produced by radiation-pressure backaction, following Marquardt, Harris, and Girvin (2006) and Ludwig, Kubala, and Marquardt (2008). Our main goal is to discuss the amplitude  $A$  of the steady-state mechanical oscillations, as a function of system parameters such as laser power, detuning, and mechanical damping rate. We find that for a fixed set of parameters,  $A$  can in general take on multiple stable values, corresponding to several stable attractors of this dynamical system. This effect is known as dynamical multistability, and in experiments it may lead to hysteretic behavior. Our discussion is directly applicable for the radiation-pressure-induced parametric instability. However, note that very similar physics and analogous formulas apply for the case when this instability is induced by photothermal forces. In fact, if the thermal decay time  $\tau_{\mathrm{th}}$  is long  $(\tau_{\mathrm{th}}^{-1} \ll \Omega_m)$ , one can reuse most parts of the discussion below, effectively replacing only  $\kappa$  by  $\tau_{\mathrm{th}}^{-1}$  [see Marquardt, Harris, and Girvin (2006) for a discussion of the differences].

The threshold of the instability can be obtained in a linear analysis by demanding that

$$
\Gamma_ {m} + \Gamma_ {\text {o p t}} = 0. \tag {100}
$$

This defines the limits of an interval where  $\Gamma_{m} + \Gamma_{\mathrm{opt}} < 0$ , i.e., where the system is unstable. This interval widens as the laser power is increased.

A simple argument can now be used to obtain the amplitude  $A$ . We start from the ansatz

$$
x (t) = \bar {x} + A \cos \left(\Omega_ {m} t\right) \tag {101}
$$

for the self-induced oscillations. This is good for typical experimental parameters, where  $\Gamma_{m},\Gamma_{\mathrm{opt}}\ll \Omega_{m}$ , such that both damping and optomechanical effects show up only after many oscillation periods. We discuss the breakdown of this ansatz in Sec. VIII.B on chaotic dynamics.

From Eq. (101), one can obtain the time dependence of the radiation-pressure force  $F(t)$  (which will depend on  $A$  and  $\bar{x}$ ). In steady state, the time-averaged power input due to this

force,  $\langle F\dot{x}\rangle$ , must equal the power lost due to friction,  $m_{\mathrm{eff}}\Gamma_m\langle \dot{x}^2\rangle$ . This can be recast into a condition resembling Eq. (100), by defining an amplitude-dependent effective optomechanical damping rate:

$$
\Gamma_ {\text {o p t}} (A) \equiv \frac {- \langle F \dot {x} \rangle}{m _ {\text {e f f}} \left\langle \dot {x} ^ {2} \right\rangle}. \tag {102}
$$

In the low-amplitude limit  $A \to 0$ , this reduces to the standard definition of  $\Gamma_{\mathrm{opt}}$  used up to now. Then the power balance condition is simply

$$
\Gamma_ {m} + \Gamma_ {\text {o p t}} (A) = 0, \tag {103}
$$

which is an implicit equation for  $A$ . This strategy can be used for arbitrary optomechanical systems also containing more optical modes or other types of radiation forces.

We need yet another condition to fix the oscillation offset  $\bar{x}$ , which is not identical with the unperturbed oscillator equilibrium position. The time-averaged radiation-pressure force deflects the harmonic oscillator:

$$
\langle F \rangle = m _ {\text {e f f}} \Omega_ {m} ^ {2} \bar {x}. \tag {104}
$$

In general, Eqs. (103) and (104) need to be solved simultaneously for the unknowns  $A$  and  $\bar{x}$ . However, if  $\Gamma_{m} \ll \Omega_{m}$ , one can already see the instability in a regime where the shift  $\bar{x}$  is small and can be neglected, such that only Eq. (103) is relevant.

We still have to obtain  $F(t)$ . This can be deduced by solving the classical equation for the light field amplitude (Sec. III.C),

$$
\dot {\alpha} = - \frac {\kappa}{2} \left(\alpha - \alpha_ {\max }\right) + i [ \Delta + G x (t) ] \alpha , \tag {105}
$$

where we defined  $\alpha_{\mathrm{max}}$  to be the amplitude reached inside the cavity right at resonance (in terms of Sec. III.C, we have  $\alpha_{\mathrm{max}} = 2\alpha_{\mathrm{in}}\sqrt{\kappa_{\mathrm{ex}}} /\kappa$ ). After inserting the ansatz (101), the solution (Marquardt, Harris, and Girvin, 2006) can be written in a Fourier series  $\alpha (t) = e^{i\varphi (t)}\sum_{n}\alpha_{n}e^{\mathrm{i}\Omega_{m}t}$ , with coefficients

$$
\alpha_ {n} = \frac {\alpha_ {\max}}{2} \frac {J _ {n} (- G A / \Omega_ {m})}{i n \Omega_ {m} / \kappa + 1 / 2 - i (G \bar {x} + \Delta) / \kappa}, \tag {106}
$$

where  $J_{n}$  is the Bessel function of the first kind and the global phase  $\varphi(t) = (GA / \Omega_m) \sin(\Omega_m t)$ . Now the force  $F(t) = \hbar G |\alpha(t)|^2$  and the time averages  $\langle F \dot{x} \rangle$  and  $\langle F \rangle$  can be calculated. One has  $\langle |\alpha(t)|^2 \rangle = \sum_n |\alpha_n|^2$  and  $\langle |\alpha(t)|^2 \dot{x} \rangle = A \Omega_m \mathrm{Im} \sum_n \alpha_n^* \alpha_{n+1}$ . This series can be efficiently summed numerically to obtain the explicit dependence of Eqs. (103) and (104) on  $A, \bar{x}$ , and the system parameters.

The result is best discussed graphically. In Fig. 38 we show the attractor diagram, i.e., the possible amplitudes  $A$  as a function of any system parameter (in this case, the detuning  $\Delta$ ). This diagram can be generated by plotting the value of  $\Gamma_{\mathrm{opt}}(A,\Delta)$  and then showing the contour lines  $\Gamma_{\mathrm{opt}} = -\Gamma_m$  that indicate possible attractors. Note that stable attractors are only those where  $|\Gamma_{\mathrm{opt}}|$  grows with  $A$  (the upper half of each line). In the case shown here  $(\kappa /\Omega_{m} = 0.2)$ , the structure of sidebands at  $\Delta = n\Omega_{m}$ , for both red and blue detunings shows clearly. Remarkably, one can have stable self-induced oscillations even on the red-detuned side  $(\Delta < 0)$ , but only for

![](images/6d66ed5e5994e6a08b0a23456ffff492e91b3bb1533865cffc7894182d553899.jpg)  
FIG. 38 (color online). Attractor diagram for mechanical lasing in an optomechanical system. The damping rate  $\Gamma_{\mathrm{opt}}$  as a function of both mechanical oscillation amplitude  $A$  and laser detuning  $\Delta$ , for a system in the resolved-sideband regime ( $\kappa/\Omega_m = 0.2$ ). Contour lines of  $\Gamma_{\mathrm{opt}}$  correspond to possible attractors. For each line, only the upper part is stable, i.e., those points on the curve where  $\Gamma_{\mathrm{opt}}$  increases when going toward higher amplitudes. The offset  $\bar{x}$  has been assumed to be negligible. (The plot shows  $\Gamma_{\mathrm{opt}}m_{\mathrm{eff}}\Omega_m^2/(2\hbar G^2\alpha_{\mathrm{max}}^2)$  vs  $GA/\Omega_m$  and  $\Delta/\Omega_m$ ; the contours are shown at levels  $-10^{-2}$ ,  $-10^{-3}$ , and  $-10^{-4}$ .)

finite amplitude  $A > 0$ . This is consistent with the fact that the linearized theory there predicts cooling at  $A \to 0$ .

Mathematically, the onset of small-amplitude oscillations, starting from  $A = 0$ , is an example of a Hopf bifurcation. In this regime,  $A \propto \sqrt{I - I_{\mathrm{th}}}$ , where  $I$  is any system parameter (such as the detuning or the laser power), and  $I_{\mathrm{th}}$  is its threshold value.

An important feature is the dynamical multistability, i.e., the existence of several stable solutions for a fixed set of external parameters. This is observed for sufficiently good mechanical quality factors, when higher-amplitude attractors become stable. It leads to hysteresis in experiments, and might also be used for high-sensitivity "latching" measurements. For more on this and the effects of noise and slow dynamics of the amplitude, see Marquardt, Harris, and Girvin (2006).

In experiments, an optomechanical instability due to retarded light forces was first studied in a low-finesse setup with photothermal forces (Höhberger and Karrai, 2004), where the retardation is due to finite thermal conductivity and the theory described here applies with appropriate modifications; see Marquardt, Harris, and Girvin (2006) and Metzger, Ludwig et al. (2008). Subsequent studies of the photothermal setup observed parts of the attractor diagram, confirmed dynamical bistability, and uncovered a new regime where more than one mechanical mode gets involved in the nonlinear dynamics (Metzger et al., 2008b) (see Fig. 39).

The parametric instability driven by radiation-pressure backaction, as discussed here, was first demonstrated in a microtoroid setup (Carmon et al., 2005; Kippenberg et al.,

![](images/f0134831484820e898a5cf78a41632378f881ac77c535219683ba0763757f38c.jpg)  
FIG. 39 (color online). (a) Experimental observation of dynamical multistability for optomechanical oscillations. The mechanical oscillation amplitude vs static displacement (or, equivalently, detuning) displays hysteresis upon sweeping in different directions.  $\lambda$  is the optical wavelength for this setup. From Metzger, Ludwig et al., 2008, where the radiation force was of photothermal origin. (b) Experimental results for the linewidth narrowing above the threshold, as a function of the oscillation amplitude, obtained for a microtoroidal setup by Rokhsari et al. (2006).

![](images/b5af392b87d6dadf33e2b868b9599dddcadd3dae9950bf90110c3c67da197501.jpg)

2005; Rokhsari et al., 2005). The full attractor diagram still has to be observed in an experiment.

A recent experiment demonstrated mechanical lasing (i.e., coherent oscillations) in a setup where two optical modes are involved and photon transitions between those modes provide the power to feed the mechanical oscillations (Grudinin et al., 2010). The attractor diagram for the parametric instability in systems involving more than one optical mode (including a "membrane in the middle") displays qualitatively new features due to the effects of optical Landau-Zener dynamics (Wu, Heinrich, and Marquardt, 2013).

Just as in a laser, the phase of the self-induced oscillations is arbitrary. Thus, external noise, including thermal Langevin forces acting on the mechanical oscillator and radiation-pressure shot noise, imparts a slow phase diffusion. The effect of a force  $\delta F$  on the phase scales inversely with the amplitude,  $\delta \varphi \propto \delta F / A$ , as seen in a phase-space diagram. Thus, the diffusion constant for the phase scales with  $1 / A^2$ , diverging just above threshold (Vahala, 2008). This is the optomechanical analog of the Schawlow-Townes result for the linewidth of a laser (Schawlow and Townes, 1958). More precisely, the scenario is closer to the case of a maser, since the thermal noise is not negligible in the mechanical oscillator:

$$
\Gamma_ {m} ^ {\mathrm {o s c}} = \frac {\Gamma_ {m}}{\bar {n}} (2 \bar {n} _ {\mathrm {t h}} + 1). \tag {107}
$$

A full discussion of the linewidth narrowing and phase diffusion in optomechanical oscillations can be found in Rodriguez and Armour (2010), where the effects of photon shot noise are taken into account as well.

Up to now, we discussed exclusively the classical dynamics. In the quantum regime (Ludwig, Kubala, and Marquardt, 2008), the parametric instability threshold is broadened due to quantum fluctuations, with strong amplification of fluctuations below threshold. The existence of attractors with finite amplitude shows up, e.g., in phase-space plots of the Wigner density, and it changes the phonon (as well as photon) statistics (Qian et al., 2012).

Interesting new collective physics results if many such optomechanical oscillators are coupled together. In particular,

![](images/d2ca17c76b8cc3e4eee48711fc64de230ea928d10e9c20789813aca611e53a31.jpg)  
FIG. 40 (color online). The transition toward chaotic motion in an optomechanical system has been observed by Carmon, Cross, and Vahala (2007) (courtesy of Tal Carmon).

this can lead to synchronization, which we discuss in more detail in Sec. IX on multimode optomechanics.

# B. Chaotic dynamics

If the laser input power is increased sufficiently, the coupled motion of the light field and the mechanical oscillator becomes chaotic. In that regime, amplitude and phase fluctuate in a seemingly random fashion that depends sensitively on initial conditions, even in the absence of noise sources. Technically, the ansatz (101) of sinusoidal oscillations breaks down, and the full dissipative driven dynamics of 4 degrees of freedom  $(x,p$ , and the complex light amplitude  $\alpha$  has to be taken into account. The chaotic regime is characterized by positive Lyapunov exponents, where any small deviation from the initial trajectory grows exponentially with time.

Chaotic motion in optomechanical systems has been explored relatively little so far, although it had been observed early on (Carmon et al., 2005) and has been studied more systematically in a subsequent experiment (Carmon, Cross, and Vahala, 2007) (see Fig. 40).

# IX. MULTIMODE OPTOMECHANICS

Up to now we almost exclusively considered one optical mode coupled to one mechanical mode. This is the "minimal model" of cavity optomechanics, captured by the Hamiltonian (23). Of course, it is clear in principle that every mechanical resonator has a multitude of normal modes, and every optical resonator likewise has many different modes as well. It is relatively straightforward to write down the appropriate extension of Eq. (23) to the more general case:

$$
\begin{array}{l} \hat {H} = \sum_ {k} \hbar \omega_ {\mathrm {c a v}, k} \hat {a} _ {k} ^ {\dagger} \hat {a} _ {k} + \sum_ {j} \hbar \Omega_ {j} \hat {b} _ {j} ^ {\dagger} \hat {b} _ {j} \\ - \hbar \sum_ {j, k, l} [ g _ {0} ] _ {k l} ^ {j} \hat {a} _ {k} ^ {\dagger} \hat {a} _ {l} (\hat {b} _ {j} + \hat {b} _ {j} ^ {\dagger}) + \dots . \tag {108} \\ \end{array}
$$

Here the various optical  $(\hat{a}_k)$  and mechanical  $(\hat{b}_j)$  modes interact according to the optomechanical coupling constant tensor  $[g_0]_{kl}^j = [g_0]_{lk}^{j*}$ , whose entries depend on the details of the optical and vibrational modes and their mutual interactions. We left out the laser drive and the coupling to the radiation and mechanical environments.

Before discussing the general case, note that restricting one's attention to the minimal model is often justified for many purposes. The incoming monochromatic laser drive will select one optical resonance. With regard to the mechanical motion, all mechanical resonances will show up in the rf

![](images/83052edc26fc1f1e6535005c2f31a367ea5cc354ec979a373921ea584cf3cd3b.jpg)

![](images/4c1aca9f22dccad9483794b7b90aa8ed2cadf58480c79e6612938e24b1837824.jpg)

![](images/89fd65e65e29b0171141e6f094ef44220e928d482aa9bd6f95bdc65c476b7a19.jpg)

![](images/f4e9a9ad59a8f061666f755bcd40769118e4836d02f0fcd38e379ad21e272f4b.jpg)

![](images/4154d90a268c73f983b31d2777a87b788b338fd1fb8995dcea21152928c55f5b.jpg)  
FIG. 41 (color online). The possible variety of multimode structures for optomechanical circuits. (a) Two mechanical modes coupled to a common optical mode (for entanglement, etc.). (b) Two optical modes coupled to a mechanical mode (QND phonon detection, etc.). (c) 1D array, with mechanical couplings between the cells. (d) 2D array, with coupling via common optical modes. (e) Optical and acoustic waveguides feeding into localized optical and mechanical modes (e.g., photon-phonon translator).

spectrum obtained from a displacement measurement, but we may choose to focus on one of those resonances, as long as they are well separated. Likewise, cooling or heating in the resolved-sideband regime singles out a particular mechanical mode via the choice of laser detuning. In the bad cavity limit, multiple modes can be cooled (or amplified) simultaneously (Metzger, Ludwig et al., 2008; Bagheri et al., 2011).

In the following, we discuss some scenarios and features where it becomes crucial to go beyond the minimal model. It is clear that going to structures with two or more mechanical or optical modes leads to a wealth of different possible schemes (Fig. 41), only a few of which have been explored so far. Further examples can be found in Sec. X on quantum optomechanics.

Braginsky pointed out that scattering of photons between two optical modes can lead to a parametric instability (Braginsky, Strigin, and Vyatchanin, 2001). This analysis was intended primarily for interferometric gravitational wave observatories, where the free spectral range may match relevant mechanical frequencies.

We already mentioned a setup with a membrane in the middle of a cavity (Sec. VI.B.2), in the context of QND phonon detection (Jayich et al., 2008; Thompson et al., 2008; Miao et al., 2009). This setup can be viewed as consisting of two optical modes, where photons can tunnel between those modes via transmission through the membrane. Having two optical modes is essential for the quadratic dependence of optical frequency on displacement that arises from the avoided crossing in the optical mode spectrum.

Besides the QND scheme, setups with two relevant optical modes can be realized in a large variety of implementations and have many additional interesting features. Mechanical oscillations can take the system through the avoided crossing, potentially resulting in Landau-Zener-Stueckelberg physics and optical Rabi oscillations for the optical two-state system, coherently shuffling photons between the two branches

(Heinrich, Harris, and Marquardt, 2010). Cooling and squeezing in the presence of quadratic optomechanical coupling has been analyzed (Nunnenkamp et al., 2010). Moreover, displacement sensing in a two-mode setup can be much more efficient than the standard scheme (Dobrindt and Kippenberg, 2010). The optomechanical system of two coupled optical modes can also be viewed as a photonic version of the Josephson effect and its classical dynamics can give rise to chaos (Larson and Horsdal, 2011).

If the mechanical resonance frequency matches the transition between the optical branches, one can implement a version of optomechanical phonon lasing (Grudinin et al., 2010) that is directly based on a population inversion between the two optical levels, just like in a real laser. The Landau-Zener physics mentioned above will significantly modify the dynamics of these self-oscillations for large amplitudes (Wu, Heinrich, and Marquardt, 2013). An interesting variant of this situation can be implemented for whispering-gallery optical and acoustical modes in toroids or spheres in a stimulated Brillouin scattering scheme (Tomes and Carmon, 2009; Bahl et al., 2011). In the same kind of Brillouin setup, the reverse process has been demonstrated as well, i.e., cooling via a photon transition between the lower and upper optical modes (Tomes et al., 2011; Bahl et al., 2012). Similar physics has been demonstrated for whispering-gallery optical modes coupling to surface acoustic waves (Matsko et al., 2009; Savchenko et al., 2011).

Recently it was pointed out theoretically that schemes with two optical modes can be exploited to enhance the quantum nonlinearities in optomechanical systems (Ludwig et al., 2012; Stannigel et al., 2012); see Sec. X.F. The photonphonon translator discussed in Sec. X.E is another example of a possible device that employs two optical modes.

Likewise, there are many schemes where more than only a single mechanical mode is relevant. These could be the various normal modes of a given mechanical structure, or several vibrating objects placed inside a cavity or coupling to one optical mode (see Sec. X.F). We mention only a few illustrative examples. An array of multiple membranes inside a cavity was studied theoretically by Bhattacharya and Meystre (2008), Hartmann and Plenio (2008), and Xuereb, Genes, and Dantan (2012) with regard to mechanical normal modes, entanglement, and collective interactions. A recent experiment demonstrated tripartite optomechanical mixing between one microwave mode and two mechanical modes (Massel et al., 2012). Effects of multiple mechanical modes can also be studied for levitated setups. It was proposed that an array of levitated dumbbell-shaped dielectric objects can undergo an ordering transition.

The nonlinear dynamics of the self-oscillations (mechanical lasing, Sec. VIII) become particularly interesting when more mechanical modes are involved. It was shown experimentally (Metzger et al., 2008b) that collective self-oscillations may arise when several mechanical modes are excited simultaneously, using a strong blue-detuned drive for a "bad cavity" whose linewidth encompasses several mechanical normal modes of the structure (a cantilever in that case). More recently, it was pointed out that optomechanical systems are very promising for observing synchronization phenomena

(Heinrich et al., 2011). Assume an array of optomechanical oscillators, each of which consists of a mechanical mode coupled to an optical mode that is driven by a blue-detuned laser beam such as to go into the mechanical lasing regime (Sec. VIII). If these "clocks" are coupled mechanically or optically, their mechanical frequencies can lock to each other, even if they have been distinct initially. Under appropriate conditions, a variant of the Kuramoto model can be derived for optomechanical systems (Heinrich et al., 2011), which is a paradigmatic model of synchronization physics. For two mechanically coupled cells, the equation turns out to be of the form

$$
\delta \dot {\varphi} = \delta \Omega - K \sin (2 \delta \varphi),
$$

where  $\delta \Omega$  is the intrinsic frequency difference,  $\delta \varphi$  is the difference of mechanical oscillation phases, and  $K$  is an effective coupling constant that can be related to microscopic parameters. If  $K$  is large enough, synchronization ensues  $(\delta \dot{\varphi} = 0)$ . If, on the other hand, several oscillators couple to the same optical mode, the behavior can become of a form that is not described by any Kuramoto-type model. This was analyzed recently in detail (Holmes, Meaney, and Milburn, 2012).

Synchronization may be important for metrological applications, where several synchronized optomechanical clocks of this type are expected to be more stable against noise (Tallur et al., 2010). Experimentally, some signs of synchronization in an optomechanical device have been observed recently (Zhang et al., 2012) for two optically coupled optomechanical oscillators, each of them implemented as a double-disk SiN structure. Mechanical spectra showed the onset first of self-oscillations and then of synchronization as a function of laser detuning.

Two coupled mechanical modes of widely different damping rates can give rise to Fano line shapes in their excitation spectrum when they hybridize. This was demonstrated in an optomechanical system (Lin et al., 2010) and suggested for information storage and retrieval in long-lived mechanical "dark" states.

Optomechanical photonic crystal structures present an opportunity to design more complex optomechanical circuits. These might be 1D or 2D array structures, where many optical and mechanical modes are arranged in a periodic layout and coupled to each other. Alternatively, one can think of more intricate circuits, more similar to computer chips, where different elements fulfill various functionalities (sensing, amplification, general signal processing).

Optomechanical arrays of this type have been studied theoretically in only a few works so far, with respect to their collective classical nonlinear dynamics (Heinrich et al., 2011), their quantum many-body dynamics (Ludwig and Marquardt, 2013), and for engineering quantum dissipation (Tomadin et al., 2012), as well as with respect to quantum applications: A suitably engineered array of optical and mechanical modes coupled to a waveguide can slow down and store light (Chang et al., 2011). Photon-phonon entanglement in an optomechanical array of three cells was studied by Akram and Milburn (2012). Many nanomechanical modes in an array geometry can be entangled via the light field, using a suitable

parametric drive to select mode pairs (Schmidt, Ludwig, and Marquardt, 2012). These studies pave the way toward future architectures for (continuous-variable) quantum information processing with optomechanical circuits.

# X. QUANTUM OPTOMECHANICS

Quantum mechanics has already figured in several places in our discussion so far, notably in setting the limits for displacement sensing or cooling. We now turn to discussing potential future optomechanical experiments where quantum behavior takes center stage. We discuss ways to create interesting quantum states in both the optical and mechanical systems, and to create entanglement between the various subsystems. We then turn to nonlinear quantum effects whose understanding requires us to go beyond the linearized optomechanical interaction, i.e., beyond the quadratic Hamiltonian of Eq. (29). Finally, we see how it is envisaged that these effects form the ingredients of future optomechanically aided protocols for quantum information processing.

# A. Light-assisted coherent manipulation of mechanics

The light field can be employed in principle to generate arbitrary quantum states of the mechanical oscillator. In this section, we restrict ourselves to the action of the linearized interaction Hamiltonian of Eq. (29),

$$
\hat {H} _ {\text {i n t}} ^ {(\mathrm {l i n})} = - \hbar g _ {0} \sqrt {\bar {n} _ {\mathrm {c a v}}} (\delta \hat {a} ^ {\dagger} + \delta \hat {a}) (\hat {b} + \hat {b} ^ {\dagger}). \tag {109}
$$

When injecting Gaussian optical states, as is the case for the usual laser drive, this can produce arbitrary mechanical Gaussian states, i.e., coherent and squeezed states out of the ground state (which has to be reached first, via either optomechanical or bulk cooling techniques). As long as the linearized Hamiltonian is valid, non-Gaussian mechanical states can be produced only from non-Gaussian optical states. The parameters that can be varied easily are the laser detuning  $\Delta$  and the laser input power. Any pulse of light will generate a radiation-pressure force pulse that shifts the oscillator's wave function and thereby permits one to create a coherent state.

It is only slightly more difficult to create a squeezed state. As seen in Sec. V.B.1, a far-detuned light beam creates an optical spring effect, i.e., a change in the mechanical frequency by  $\delta \Omega_{m} = 2\bar{n}_{\mathrm{cav}}g_{0}^{2} / \Delta$ . As is well known, a time-dependent modulation of  $\Omega_{m}$ , i.e., a parametric driving of the mechanical oscillator creates a squeezed state; see Mari and Eisert (2009) and Liao and Law (2011) for an analysis in the case of optomechanical systems, where one can employ a modulation of the laser power, and Farace and Giovannetti (2012) for a generalization of the scheme. For  $\delta \Omega_{m}(t) = \delta \Omega \cos(2\Omega_{m}t)$ , the resulting effective mechanical Hamiltonian turns out to be (in a frame rotating at  $\Omega_{m}$ , and in rotating-wave approximation) the standard squeezing Hamiltonian

$$
\hat {H} _ {\text {m e c h}} = \frac {\hbar \delta \Omega}{2} [ \hat {b} ^ {2} + (\hat {b} ^ {\dagger}) ^ {2} ], \tag {110}
$$

such that  $\hat{b}(t) = \cosh(\delta \Omega t) \hat{b}(0) - i \sinh(\delta \Omega t) \hat{b}^\dagger(0)$  in the absence of dissipation. Thus, in this time-dependent scheme,

squeezing grows exponentially with time. However, a realistic analysis needs to take into account the initial thermal population, as well as dissipation and decoherence, and distinguish between the steady-state situation and the transient case. Adding feedback to the parametric driving scheme has been shown to relax the requirements to achieve squeezing (Szorkovszky et al., 2011). When several mechanical modes are coupled to the same optical mode, a modulated laser drive will generate two-mode squeezing or beam-splitter interactions between pairs of modes that are selected according to their frequency. This can form the basis for continuous-variable quantum state processing in optomechanical arrays (Schmidt, Ludwig, and Marquardt, 2012).

Measurements can also be used to generate interesting mechanical states in a probabilistic manner, i.e., conditioned on the measurement result. This includes squeezed states via single quadrature detection (Sec. VI.B.1) or mechanical Fock states via phonon number readout (Sec. VI.B.2). Further, we comment on other ways to generate more nonclassical states (including non-Gaussian states), by nonlinear effects (Sec. X.F) or various state transfer protocols (Sec. X.E).

# B. Mechanics-assisted readout and manipulation of light

The optomechanical interaction can be exploited to detect and manipulate the quantum state of the light field. An example that was suggested early on is the possibility of a QND detection (Braginsky, Vorontsov, and Thorne, 1980) for the light intensity circulating inside the cavity (Braginsky, Vorontsov, and Khalili, 1977; Jacobs et al., 1994; Pinard, Fabre, and Heidmann, 1995). The displacement of the end mirror, induced by the radiation-pressure force, can serve as a noiseless meter for the light intensity. In addition, as the radiation-pressure force is proportional to the photon number, it increases in discrete steps. If the photons are sufficiently long lived and the interaction strong enough, this may even enable QND photon detection, by registering the resulting mechanical displacement. In practice, however, that regime is extremely challenging to reach, as it requires  $g_0^2 / \kappa \Omega_m \gg 1$  (see Sec. X.F).

Regarding the manipulation of the light's quantum state, one of the most straightforward applications of optomechanics consists in squeezing the noise of the light beam (Vyatchanin and Matsko, 1993; Fabre et al., 1994; Mancini and Tombesi, 1994). In this context, the change of the cavity length due to the intensity-dependent radiation force can be compared to the effect of a Kerr medium inside a rigid cavity. The resulting physical picture depends sensitively on the detuning and the frequency at which the noise of the light beam is analyzed. In the simplest case, one can imagine that a temporary fluctuation in the incoming intensity of the light beam induces a change in the cavity length via the radiation-pressure force. This, in turn, shifts the optical resonance and thereby affects the circulating and outgoing intensities, potentially suppressing the noise. Note that for a single-sided optical cavity (without internal losses) there can be no change of the amplitude noise at zero frequency, since the incoming and outgoing intensities have to be equal. However, there can be amplitude squeezing at finite frequencies (and phase squeezing down to zero frequency). The squeezing effect diminishes

toward frequencies above the mechanical resonance. Finite temperatures degrade squeezing, as the thermal motion of the mirror imprints extra noise on the light beam. At low frequencies, and for detunings on the order of  $\kappa$ , the light beam's noise is increased (Fabre et al., 1994) by a factor of  $\bar{n}_{\mathrm{th}} / Q_m$ , where  $\bar{n}_{\mathrm{th}}$  is the equilibrium phonon number.

A recent review of the current efforts toward demonstrating radiation-pressure shot-noise effects and squeezing in optomechanical experiments can be found in Verlot et al. (2011). First experiments in this direction have simulated the quantum fluctuations by classical intensity noise (Marino et al., 2010). More recently, the very strong coupling and low temperatures attainable in realizations of cavity optomechanics with both atomic clouds and photonic crystal cavities have allowed the first signatures of genuine optical squeezing (Brooks et al., 2012; Safavi-Naeini, Groblacher et al., 2013) at the quantum level to be obtained.

# C. Optomechanical entanglement

The optomechanical interaction can be used to engineer entanglement between the light beam and the mechanical motion, or between several light beams or several mechanical modes. However, a prerequisite for all of these approaches is to cool the mechanical oscillator to near its ground state and to achieve sufficiently strong coupling. Entanglement between motional states of trapped and laser-cooled ions has been demonstrated by Jost et al. (2009).

In the following, we first describe entanglement in the single-photon strong-coupling regime (for more on this regime, see Sec. X.F) and then turn to continuous-variable entanglement. A particularly simple physical picture applies in an idealized situation where we imagine starting with a superposition of photon states inside the cavity. Then, the radiation-pressure force assumes different, discrete values for each photon number, displacing the mechanical harmonic oscillator potential by  $2x_{\mathrm{ZPF}}g_0 / \Omega_m$  per photon. If initially the mechanics was in its ground state, it will evolve into a coherent state  $|\alpha_{n}(t)\rangle_{\mathrm{vib}}$  oscillating around the new, displaced origin that depends on the photon number. Thus, we immediately arrive at a nonfactorizable, i.e., entangled, state of the form:

$$
| \Psi (t) \rangle = \sum_ {n = 0} ^ {\infty} c _ {n} e ^ {i \varphi_ {n} (t)} | n \rangle_ {\text {c a v}} \otimes | \alpha_ {n} (t) \rangle_ {\text {v i b}}. \tag {111}
$$

Here  $n$  is the photon number,  $c_{n}$  are the arbitrary initial amplitudes for the photon field (e.g., corresponding to a coherent state), and  $\varphi_{n}(t)$  is a phase shift that can be obtained by solving the time-dependent Schrödinger equation for this problem. The state (111) can be interpreted as a "Schrödinger cat"-type state, where a "microscopic" degree of freedom (the optical cavity mode) is entangled with a "macroscopic" (or mesoscopic) degree of freedom, the vibrating mirror. This picture was first analyzed by Bose, Jacobs, and Knight (1997) and Mancini, Man'ko, and Tombesi (1997).

Several signatures of entanglement exist. In this example, where the overall state is pure, we can simply trace out the mechanical vibrations, arriving at the reduced density matrix of the optical field, which is found in a mixed state whenever

![](images/a1971a414839b4f4da4f9ca00f948819047f6cbb5a4367ee3b9cade27095cb61.jpg)  
FIG. 42 (color online). An optomechanical which-path experiment can be employed to test for the decoherence of mechanical superposition states. A photon would leave behind a vibration in the mirror of an optomechanical cavity, which destroys the photon's coherence with the other path. However, if the photon exits after a full mirror oscillation period, it will be fully coherent again, unless mechanical decoherence has occurred in the meantime. From Marshall et al., 2003.

there is entanglement. However, at multiples of the mechanical period, light and mechanics completely disentangle, since the coherent state  $\left|\alpha_{n}(t)\right\rangle_{\mathrm{vib}}$  will have returned back to the origin, independent of photon number. At these times, the photon state becomes pure again, even independent of the mirror's effective temperature. The optical field's coherence thus demonstrates decay and revivals. This can in principle be tested in an interferometric optomechanical "which-way" experiment, where a photon can take either of two paths, one of which contains an optomechanical cavity (see Fig. 42). The revivals can be observed in the interference visibility, as a function of the time the photon has spent inside the cavity. However, any mechanical decoherence occurring in the meantime will spoil these perfect revivals of the photon field's coherence. This can in principle be employed for highly sensitive optical tests of sources of mechanical dissipation and decoherence and fundamental quantum physics in general (Bouwmeester et al., 1998; Bose, Jacobs, and Knight, 1999; Folman et al., 2001; Marshall et al., 2003). Experiments of this kind could quantify the decoherence of superpositions of heavy objects (i.e., the mirror), and thus potentially shed new light on the quantum-to-classical transition (see Sec. XI.A). In particular, models of gravitationally induced decoherence might be tested (Bose, Jacobs, and Knight, 1999; Marshall et al., 2003), where the (admittedly small) hypothetical extra decoherence rate becomes potentially observable only for relatively massive objects. Such experiments require the challenging regime of  $g_{0} / \Omega_{m} > 1$  (when the displacement induced by a single photon may be on the order of the mechanical zero-point motion). It was recently suggested that nested interferometry allows one to significantly reduce this requirement (Pepper, Ghobadi et al., 2012).

On the other hand, entanglement can also exist on the level of continuous variables (Braunstein and van Loock, 2005), of the type first proposed in the famous Einstein, Podolsky, and Rosen (1935) (EPR) article. The analysis of entanglement in

this context has to be performed by taking into account the dissipative nature of the systems involved and typically relies on solving the linearized quantum equations of motion (including, if needed, input-output theory for treating the reflected or transmitted light beam). In the regime where linearized equations of motion are valid, Gaussian states of the mechanics and the light field will be produced, and their entanglement (of the continuous-variable type) can be characterized completely once the correlations between the various mechanical and optical quadratures are known. A typical measure of entanglement that is commonly applied here is the logarithmic negativity, which can be calculated easily for Gaussian states (Vidal and Werner, 2002), both pure and mixed.

The entanglement between mechanical vibrations and the optical cavity field (already described in a picture appropriate for strong coupling) has been analyzed in more detail for the continuous-variable case by Paternostro et al. (2007) and Vitali et al. (2007). It was pointed out that a suitable time-dependent modulation of the drive can improve the efficiency of photon-phonon entanglement (Mari and Eisert, 2012).

Recently, optomechanical entanglement between mechanical motion and the microwave radiation field was demonstrated experimentally (Palomaki, Teufel et al., 2013), implementing a pulsed scheme (Hofer et al., 2011) (see also Sec. X.E).

It is also possible to create entanglement of two spatially separate mirrors. When a strong pump beam runs through a nonlinear optical  $\chi^{(2)}$  medium acting as a nondegenerate optical parametric amplifier, two-mode squeezing produces entanglement between the quadratures of pairs of emanating light beams. This entanglement could then be transferred via the radiation-pressure force onto two spatially separated mirrors that are part of optomechanical cavities on which these light beams impinge (Zhang, Peng, and Braunstein, 2003). In this way, optomechanics would help to create mechanical EPR-type entanglement at a distance. The verification of EPR entanglement between macroscopic test masses by sensitive measurements has been studied in more detail for the context of gravitational wave interferometer setups (Müller-Ebhardt et al., 2009; Miao et al., 2010). In the context of optomechanics, we usually consider the system to be driven by a coherent laser beam. However, it is natural to ask whether special opportunities arise when the light that is injected displays quantum features. For example, the injection of squeezed light can be beneficial for entangling nanomechanical resonators via the optomechanical interaction (Huang and Agarwal, 2009b).

In another approach, one can achieve the same goal without the optical entanglement created by a nonlinear medium, and instead perform an optical measurement after the interaction has taken place, in an entanglement swapping scheme. If two independent light beams interact with separate optomechanical cavities, then the beams can afterward be brought to interfere at a beam splitter, and a suitable Bell-state measurement can then be used to generate entanglement between the distant mechanical resonators (Pirandola et al., 2006) [see Borkje, Nunnenkamp, and Girvin (2011) for a similar proposal].

Alternatively, the driven optical field inside the cavity automatically induces an effective interaction between several mechanical modes, thus providing yet another way to generate mechanical entanglement, without the need for any optical nonlinearities or entanglement swapping schemes. In the case of two mechanical resonators (or two normal modes of one resonator) coupling to the same driven cavity mode, this can be understood as a consequence of the optical spring effect (Sec. V.B.1). For the case of a single mechanical mode  $\hat{b}$ , eliminating the driven cavity mode by second-order perturbation theory creates an effective interaction term  $\hbar (g_0^2\bar{n}_{\mathrm{cav}} / \Delta)(\hat{b} +\hat{b}^\dagger)^2$ . Proceeding through the same argument for the case of two mechanical modes gives rise to an effective mechanical interaction. It is of the form

$$
\hat {H} _ {\text {e f f}} ^ {\text {i n t}} = \hbar \frac {g _ {0} ^ {2} \bar {n} _ {\text {c a v}}}{\Delta} \left[ \left(\hat {b} _ {1} + \hat {b} _ {1} ^ {\dagger}\right) + \left(\hat {b} _ {2} + \hat {b} _ {2} ^ {\dagger}\right) \right] ^ {2}, \tag {112}
$$

if we assume for simplicity that both mechanical oscillators couple equally strongly to the optical mode.

In order to successfully entangle different mechanical modes, one has to laser cool those modes, since the mechanical vibrations are far from their ground state for typical bulk temperatures. The optically induced steady-state entanglement between two movable mirrors under simultaneous laser cooling was carefully studied by Pinard et al. (2005), and later for somewhat different setups by Hartmann and Plenio (2008) and Müller-Ebhardt et al. (2008). There is an interesting caveat for such studies: It is insufficient to apply the Markov approximation to describe the dissipative dynamics of the mechanical vibrations in this context, even though for many other purposes in optomechanics that is a very reliable approach. In fact, it can be shown that in a proper treatment (Ludwig, Hammerer, and Marquardt, 2010) there is an optimum intermediate laser cooling strength for which entanglement is maximized (an effect entirely missed by the common Markovian treatments).

The light-induced interaction given in Eq. (112) can form the basis of a general scheme for quantum-state processing with many nanomechanical modes. In order to selectively address pairs of such modes for entanglement and state transfer, one simply has to modulate the coupling strength (i.e., the laser intensity) at sum and difference frequencies of those modes. Such a parametric scheme requires only one appropriately modulated laser input to address whole arrays of modes, if the proper layout is chosen (Schmidt, Ludwig, and Marquardt, 2012). If the individual nanomechanical resonators are very nonlinear (i.e., with nonlinearities important on the single-phonon level), they can be viewed as qubits, and a common optical mode can then be used to perform operations on them (Rips and Hartmann, 2013).

Another possibility consists of exploiting optomechanics to entangle two light beams. In these cases, the optomechanical interaction essentially serves the purpose of a  $\chi^{(2)}$  nonlinear medium. This was proposed, e.g., for an optomechanical setup where two degenerate, orthogonally polarized cavity modes are driven strongly and their interaction with the movable mirror creates EPR correlations (Giovannetti, Mancini, and Tombesi, 2001) between the quadrature variables of the beams emanating from these modes. Another option is to entangle

the two sidebands reflected from a vibrating mirror, which works even in the absence of a cavity, for a strong short incoming laser pulse (Pirandola et al., 2003). For this situation, a more detailed analysis of the entanglement between mirror vibrations and the full light field (infinitely many degrees of freedom) was performed by Miao, Danilishin, and Chen (2010). Optically trapped mirrors in a cavity-optomechanics setup can also be exploited to entangle light beams (Wipf et al., 2008).

# D. Quantum hybrid systems

Optomechanical systems already represent a quantum hybrid system, i.e., a coupling between two quantum systems of a different physical nature: light and mechanical vibrations. In general, hybrid approaches may be useful for purposes such as quantum information processing, in order to combine the advantages of different physical systems in one architecture. Some systems may be strongly interacting (good for computation), some are very coherent (good for long-term storage), and yet others are easily transported over long distances (good for communication).

In principle, other components may be easily added to optomechanical setups. This is because both the light field and the mechanical vibrations are quite versatile in coupling to a variety of systems, such as cold atoms, spins, superconducting and other electronic qubits, etc. Consequently, there are already several proposals along these lines.

In a cloud of atoms, the total spin can sometimes be treated as a harmonic oscillator, identifying its small fluctuations around a preferred direction as position and momentum quadratures. This picture is useful when discussing experiments where the state of the light field is transferred to the atomic spin state and back again (Hammerer, Sorensen, and Polzik, 2010). More recently, it was suggested that light might also be used to couple the collective spin of an atom cloud to a nanomechanical oscillator (Hammerer, Aspelmeyer et al., 2009). In such a setup, a light beam passing first through an optomechanical cavity and then through an atom cloud carries information in its quadratures about the sum and the difference of position and momentum variables of the mechanics and the spin state. A subsequent QND measurement then is able to prepare the two systems in an EPR state, conditioned on the measurement result. As another example, coupling to the internal transitions of atoms can enhance cooling (Genes, Ritsch, and Vitali, 2009). One can also consider more involved internal level schemes for the atoms. For example, a vibrating mirror could be strongly coupled to the collective spin of a cloud of three-level atoms displaying electromagnetically induced transparency phenomena (Genes et al., 2011). In addition, it was suggested that coupling the collective spin of an atom cloud parametrically to a resonator can lead to the phenomena known from optomechanics (Brahms and Stamper-Kurn, 2010) (amplification and cooling of the spin, frequency shifts, and squeezing of light), with the collective spin replacing the mirror motion.

After the pioneering experiments on optomechanics using cold atoms (Sec. IV.G), a number of different possibilities have been explored theoretically to couple the motion of atoms to other systems. For example, the light field inside the

cavity may be used to couple the motion of a single atom to the vibrations of an end mirror or a membrane (Hammerer, Wallquist et al., 2009; Wallquist et al., 2010), where the strong-coupling regime seems to be within reach. This could be the basis for exploiting all the well-known tools for manipulating and reading out the motion of a single trapped atom to gain access to the membrane motion. It would also be an interesting system to observe the entanglement between a microscopic and a macroscopic degree of freedom. Another model system that has been studied (Hammerer et al., 2010) and is now being implemented (Camerer et al., 2011) is a cloud of atoms in a standing light wave reflected from a vibrating mirror (without a cavity). This could allow long-distance coupling between atoms and mechanical objects spaced apart by macroscopic distances.

A variety of other ideas exist for merging cold atom systems with optomechanics [see the review by Hunger et al. (2011)]. For example, the magnetic moments of atoms in a Bose-Einstein condensate might couple to a cantilever carrying a nanomagnet (Treutlein et al., 2007). In addition, the optomechanics of both Bose-Einstein condensates (Chen et al., 2010; Jing et al., 2011; Steinke et al., 2011) and degenerate cold atom Fermi gases (Kanamoto and Meystre, 2010) have been explored theoretically in some depth. Even the Mott insulator to superfluid transition of atoms in an optical lattice coupled to a vibrating mirror has been analyzed, as an example of a strongly interacting quantum system subject to the optomechanical interaction (Larson et al., 2008; Chen et al., 2009).

The idea of doing optomechanics on trapped atoms found an interesting counterpart in proposals for doing optomechanics on levitated dielectric objects (Sec. IV.E). The promise of this approach lies in a greatly enhanced mechanical quality factor. Some proposals considered trapping and cooling a mirror (Bhattacharya and Meystre, 2007a, 2007b; Bhattacharya, Uys, and Meystre, 2008; Singh et al., 2010), which has the advantage (over other objects) that scattering of the light into unwanted directions is greatly reduced. Alternatively, one can have dielectric spheres or other particles trapped in an optical lattice or by other means (Barker, 2010; Barker and Shneider, 2010; Chang et al., 2010; Romero-Isart et al., 2010). A more detailed analysis of fundamental applications and protocols can be found in Romero-Isart (2011), Romero-Isart et al. (2011b, 2011c), and Pender et al. (2012). If the promise of very long mechanical coherence times is fulfilled, then these platforms could offer the best means to test novel decoherence mechanisms (see Sec. X.C). Some early experiments and studies on cavity optomechanics with subwavelength nano-objects (Favero and Karrai, 2008; Favero et al., 2009) (Sec. IV.E) have already explored the optical coupling and some of the scattering mechanisms that may become relevant in this domain, even though they did not yet benefit from a suppression of mechanical dissipation.

Connecting the world of superconducting or other solid-state qubits to optomechanical systems represents an intriguing possibility in the context of quantum information processing. This has become particularly relevant since the pioneering experiment at the University of California at Santa Barbara (O'Connell et al., 2010) that demonstrated strong coupling between a superconducting phase qubit and the

GHz oscillations of a piezoelectric nanoresonator, swapping a single excitation from the qubit into the resonator. The first experiments demonstrated how to manipulate a mechanical nanoresonator via both the optomechanical interaction and electrically (Lee et al., 2010; Winger et al., 2011), which is an important ingredient for a future hybrid platform of solid-state qubits with electrical interactions coupled to mechanical nanoresonators coupled to the light field. Theoretical proposals already pointed out how to use systems of this type to map solid-state quantum information into photons and back again (Stannigel et al., 2010, 2011; Regal and Lehnert, 2011; Safavi-Naeini and Painter, 2011; Tian, 2012; Wang and Clerk, 2012). More elementarily, the nanomechanical structure can serve as an intermediary to generate entanglement between microwave and optical fields (Barzanjeh et al., 2011). The presence of qubits also readily allows the creation of nonclassical states, e.g., in microwave cavities coupled to mechanical systems (Gangat, McCulloch, and Milburn, 2012).

An equally promising avenue is to merge the fields of solid-state quantum optics and cavity optomechanics. The first experiments deliberately introducing semiconductor materials in cavity-optomechanical setups now exist. These include  $2\text{-}\mu \mathrm{m}$ -diameter GaAs vibrating disk structures with very high optomechanical coupling strength (Ding et al., 2010, 2011) and coupling of the light field to a semiconductor nanomembrane (Usami et al., 2012). The excitonic transitions of quantum dots embedded in such materials could couple to the mechanical vibrations either directly via deformation potentials or indirectly via the light field (Rundquist and Majumdar, 2011).

# E. Quantum protocols

The previous sections introduced some basic quantum physical features in optomechanical systems, such as producing and reading out nonclassical states of light and mechanics. As soon as this can be achieved reliably, one may envisage building a toolbox for quantum manipulation in these systems and exploit it for purposes of quantum communication and quantum information processing. This would follow the pioneering ideas and efforts in the ion-trap community, where it was suggested early on that one can exploit the motional degrees of freedom to facilitate quantum gates between the internal states of ions (Cirac and Zoller, 1995; Leibfried et al., 2003). Micromechanics and nanomechanics offer the added value that they can be functionalized and hence couple to many different physical degrees of freedom. Optomechanical devices therefore offer a fruitful addition to the vast array of physical systems that are being explored for quantum information processing (Zoller et al., 2005).

One of the most prominent protocols is quantum-state transfer. In the context of optomechanics, this allows one to reliably convert an optical pulse into a mechanical excitation (and vice versa). In principle, this is straightforward, since the linearized optomechanical interaction describes a coupling between two oscillators (mechanical and driven cavity mode), which can be tuned via the laser intensity (see Sec. III.B and Fig. 43 for a summary). For the red-detuned case  $\Delta = -\Omega_{m}$  in the resolved-sideband limit, we found a beam-splitter type of interaction:

![](images/852c64f8b7b59d7ec4072b23926c966ee5e84f2cb166df89c9e7009c926de159.jpg)

![](images/3c93f4d7bb187c3da7f0c5478c2751bff94f28be24f3db3e42219cd3ff781895.jpg)

![](images/db6805422b2c92affce0160ecee0fe7defa9bfbe8d8e3133345d6ef21cc525c6.jpg)

![](images/4e162e8276cb51cd5e13334f2afead618da9509c291dee16c3ec6318fbb349e5.jpg)  
FIG. 43 (color online). The linearized Hamiltonian of cavity quantum optomechanics describes three different kinds of interaction between the mechanical resonator and the driven cavity mode, depending on which laser detuning is chosen. This is the basis for elementary quantum protocols, such as storing optical information into the mechanical degree of freedom.

![](images/1a17f39ef7e1a25fb5ec4c17d8d464ddbf9dac513c68921c78dc399c851fabfc.jpg)

![](images/9ec9a1fb4fe3188a5ffe50313be79270681f3cdb7e03bcaa3959c4679c96ea7e.jpg)

$$
\hat {H} = - \hbar \Delta \delta \hat {a} ^ {\dagger} \delta \hat {a} + \hbar \Omega_ {m} \hat {b} ^ {\dagger} \hat {b} - \hbar g (\delta \hat {a} ^ {\dagger} \hat {b} + \delta \hat {a} \hat {b} ^ {\dagger}) + \dots . \tag {113}
$$

Thus, the excitations  $\delta \hat{a}$  on top of the strong coherent laser drive can be swapped onto the mechanical resonator. Such an operation would be performed in a pulsed scheme. The coupling  $g(t)$  becomes time dependent via the laser intensity, and it would be switched on for just the right amount of time to perform a complete state swap between the two oscillators ( $\delta \hat{a}$  and  $\hat{b}$ ). Two laser pulses are needed for this scheme. A redetuned control pulse at  $\omega_{L}^{\mathrm{control}} = \omega_{\mathrm{cav}} - \Omega_{m}$  determines the time-dependent coupling  $g(t)$ . A second, "signal" pulse serves to excite the  $\delta \hat{a}$  oscillator into some target state that then will be written onto the mechanics. Since  $\delta \hat{a}$  oscillates at the frequency  $-\Delta = \Omega_{m}$  in the frame rotating at  $\omega_{L}^{\mathrm{control}}$ , the signal pulse has to be injected at a frequency  $\omega_{L}^{\mathrm{signal}} = \omega_{L}^{\mathrm{control}} + \Omega_{m} = \omega_{\mathrm{cav}}$  i.e., right at the cavity resonance. Ideally, the whole swapping pulse sequence is shorter than the cavity decay time, which however requires a two-mode setup with different decay rates for the modes (since the control pulse cannot be shorter than  $1 / \kappa$  for a single mode). A detailed analysis of swapping protocols has been given by Wang and Clerk (2012).

There is also a simple classical picture for what happens during such a pulse sequence: The superposition of signal and control beam leads to a beat note in the intensity at  $\Omega_{m}$ . This translates into a radiation-pressure force that resonantly excites the mechanical oscillator.

The optomechanical interaction can also be exploited for conversion between different optical wavelengths. That

![](images/ea5f86ab8d17f12d698f48b21d7b61147d21fdb5d0aaa50246954f556a6a46cd.jpg)  
FIG. 44 (color online). Optical wavelength conversion in an optomechanical setup: Two modes at different frequencies are illuminated by strongly red-detuned control beams. When a signal is injected at the resonance of mode 1, it is converted into a signal emanating from mode 2.

scheme is illustrated schematically in Fig. 44. It involves two optical resonances, each of which is driven by a strong control beam, red detuned by  $\Omega_{m}$ . When an input signal (e.g., a pulse) is injected at the resonance of mode 1, it will be converted to an output signal emanating from the resonance of mode 2. This was demonstrated recently by Dong et al. (2012) and Hill et al. (2012).

First experimental proof-of-principle demonstrations have shown these concepts in the classical regime (Fiore et al., 2011; Verhagen et al., 2012). In this context it was pointed out (Romero-Isart et al., 2011c; Verhagen et al., 2012) that the requirement for coherent state transfer of this type is  $g > \kappa, \Gamma_{m}\bar{n}_{\mathrm{th}}$ . The next challenge will be to drastically improve the fidelity and demonstrate true quantum-state transfer (Parkins and Kimble, 1999; Ritter et al., 2012), e.g., by reconstructing the mechanical quantum state (Sec. VI.B.1).

Recently, state transfer between a mechanical mode and an itinerant microwave coherent state was reported (Palomaki, Harlow et al., 2013). In this experiment, a suitably shaped microwave pulse was written onto the motional state of a micromechanical membrane and later retrieved via quickly switched control beams, hence realizing a coherent mechanical memory for microwave pulses in the weak-coupling regime. Another protocol that does not require the strong-coupling regime is based on quantum-state teleportation (Hofer et al., 2011; Romero-Isart et al., 2011c).

If a single photon is sent into the setup and transferred to the mechanical resonator, this will prepare the resonator in a Fock state or some nonclassical state in general (Akram et al., 2010; Kahili et al., 2010). That may be the most efficient route toward generating nonclassical mechanical states in optomechanical systems as long as the single-photon strong-coupling regime (Sec. X.F) has not been reached. Alternatively, single-photon detection and postselection can be used to prepare non-Gaussian states even if the single-photon optomechanical coupling is not very strong, as shown by Vanner, Aspelmeyer, and Kim (2013).

Up to now, we described only how single localized phonons (stored inside the mechanical resonator) can be converted to photons and back again. An equally interesting, or perhaps even more useful, scheme takes traveling phonons and converts them to photons. Such a device was proposed recently and was termed an optomechanical "traveling wave phonon-photon translator" (Safavi-Naeini and Painter, 2011). Although the frequency is shifted by many orders of magnitude, the wave function of the outgoing single photon is designed to be a faithful replica of the incoming phonon's wave function.

The basic idea is the following: Phonons are traveling down a phononic waveguide and enter a localized phononic mode, where they experience the usual optomechanical interaction. Frequency up-conversion is achieved by having a high-intensity stream of incoming photons. In a Raman-type scattering process, the phonon combines with one of those photons to form a single photon at a slightly different frequency, so energy conservation is obeyed. The strong pump beam and the weak stream of outgoing converted photons can be efficiently separated by being coupled to two different optical modes. Indeed, a suitably engineered optomechanical structure (Safavi-Naeini and Painter, 2011)

has two optical modes coupling to the phonon displacement field in the following way (which is conceptually identical to the membrane-in-the-middle setup discussed in Sec. VI.B.2):

$$
\hat {H} = - \hbar g _ {0} (\hat {b} + \hat {b} ^ {\dagger}) (\hat {a} _ {1} ^ {\dagger} \hat {a} _ {2} + \hat {a} _ {2} ^ {\dagger} \hat {a} _ {1}) + \dots . \tag {114}
$$

If mode  $\hat{a}_1$  is pumped strongly, we can replace the field operator by the classical amplitude  $\hat{a}_1(t) \mapsto \bar{\alpha} e^{-i\omega_L t}$  (assume  $\bar{\alpha}$  is real valued). If  $\omega_2 \approx \omega_1 + \Omega_m$ , then the resonant terms to be retained are

$$
\hat {H} = - \hbar g _ {0} \bar {\alpha} \left(\hat {b} \hat {a} _ {2} ^ {\dagger} e ^ {- i \omega_ {L} t} + \hat {b} ^ {\dagger} \hat {a} _ {2} e ^ {+ i \omega_ {L} t}\right) + \dots . \tag {115}
$$

This displays the elementary process of converting a single phonon to a single photon (and back). It also shows that the conversion rate can be tuned via the pump strength  $\bar{a}$ . The remaining challenge lies in ensuring that  $100\%$  of the phonons arriving at the device are indeed converted into photons. This is essentially an impedance-matching problem, since the coupling of the phonon mode to the phonon waveguide (ideally set by  $\Gamma_{m}$  if other losses can be neglected) is usually much weaker than the coupling of the optical mode to the photon waveguide (set by  $\kappa_{2}$ ). Without extra fine-tuning, most of the phonons would be reflected. This can be overcome by a judicious choice of the coupling. Indeed, from the point of view of the phonon mode, the coupling (115) to the lifetime-broadened photon mode  $\hat{a}_{2}$  gives rise to a Fermi golden rule transition rate  $4g_0^2\bar{\alpha}^2 /\kappa_2$ . This is the rate at which a given localized phonon would be converted and decay into the photonic waveguide, and it is identical to the optomechanical cooling rate in the sideband-resolved regime. By matching this to the coupling to the phononic waveguide, i.e., demanding  $4g_0^2\bar{\alpha}^2 /\kappa_2 = \Gamma_m$ , one creates a situation that is equivalent to a two-sided cavity with equal mirrors, where  $100\%$  transmission can be achieved on resonance. Consequently, in the present setup ideally  $100\%$  of the phonons can be converted if  $2g_{0}\bar{\alpha} = \sqrt{\kappa_{2}\Gamma_{m}}$ . A detailed analysis (Safavi-Naeini and Painter, 2011) considered the full scattering matrix that describes scattering of incoming phonons into the photon waveguide (or reflection back into the phonon waveguide), and it includes the unwanted effects of extra intrinsic losses and noise.[21]

On a classical level, the device described takes the slow amplitude and phase modulations of the phonon field, i.e., of a sound wave traveling down the waveguide, and transposes them into the optical domain by shifting the carrier frequency from mechanical frequencies (e.g., GHz) up to optical frequencies. The fact that the bandwidth is set by the smallest damping rate in the problem, which is  $\Gamma_{m}$ , can be an advantage if one uses the device as a narrow-bandwidth frequency filter. For example, two photon-phonon translators in series (the first one operated in reverse, i.e., going from photons to phonons) implement a potentially very narrow filter in the optical domain.

Phonon-photon conversion has been analyzed for transferring solid-state quantum information to the optical domain (Stannigel et al., 2010, 2011; Wang and Clerk, 2012) and for transferring optical pulses between different wavelengths and pulse shaping (Tian and Wang, 2010; Safavi-Naeini and Painter, 2011; Tian, 2012).

Microwave-to-optical conversion was demonstrated recently in two experiments: One of them employed a piezoelectric AlN photonic crystal nanobeam (Bochmann et al., 2013), and the other used a partially metallized SiN membrane (Andrews et al., 2014) coupled to both a microwave circuit and an optical cavity. One example for the more advanced possibilities of optomechanical quantum protocols is to perform continuous-variable quantum teleportation. Besides employing this for generating entanglement between distant mechanical oscillators (as mentioned), one may also teleport an arbitrary input state of the light field onto the mechanics. The generic idea is to start with the entanglement between the mechanical motion and a light beam, and then to let the beam interfere at a beam splitter with another light beam, carrying an arbitrary input state. A subsequent measurement in both output ports of the beam splitter (Bell measurement) then yields a classical measurement result on the basis of which one manipulates the mechanical state, leaving it in a final quantum state that equals the arbitrary input state. Such a scheme was analyzed for a strong short laser pulse impinging on a vibrating mirror in a free-beam setup (without a cavity) (Mancini, Vitali, and Tombesi, 2003; Pirandola et al., 2003), where the reflected optical Stokes and anti-Stokes modes at  $\omega_{L} \pm \Omega_{m}$  get entangled with the vibrations, and for a time-dependent drive of an optomechanical cavity (Hofer et al., 2011; Romero-Isart et al., 2011c).

# F. Nonlinear quantum optomechanics

In this section, we describe what happens when the nonlinearity of the optomechanical interaction plays a role on the quantum level. Other approaches to introduce quantum nonlinearity into optomechanical systems involve having a nonlinear optical medium or a nonlinear mechanical oscillator, as mentioned previously.

The optomechanical interaction  $-\hbar g_0\hat{a}^\dagger \hat{a} (\hat{b} +\hat{b}^\dagger)$  is cubic in field operators, i.e., the corresponding Heisenberg equations of motion are nonlinear. However, in experiments this nonlinearity so far has played a role only in the classical regime of large-amplitude oscillations (both mechanical and with regard to the light field); see Sec. VIII.A. In the quantum regime, we have thus far resorted to the linearized description, with a quadratic interaction Hamiltonian of the type  $-\hbar g_0\sqrt{\bar{n}_{\mathrm{cav}}}\left(\delta \hat{a}^\dagger +\delta \hat{a}\right)\left(\hat{b} +\hat{b}^\dagger\right)$ ; see Eq. (29). This linearized approach is sufficient to understand many facets of cavity optomechanics: displacement detection down to the SQL (Sec. VI.A), the theory of optomechanical ground-state cooling (Sec. VII.A), light or mechanics hybridization in the strong-coupling regime  $g_0\sqrt{\bar{n}_{\mathrm{cav}}} >\kappa$  (Sec. VII.C.1), optomechanically induced transparency (Sec. VII.C.2), optomechanical squeezing of light (Sec. X.B), and almost all of the various entanglement and state transfer schemes presented. The experimental advantage of the linearized interaction is that its strength  $g = g_{0}\sqrt{\bar{n}_{\mathrm{cav}}}$  can be tuned at will by the incoming photon energy.

laser power. In this way, a small value of  $g_{0}$  (fixed by the setup) may be compensated for by a stronger laser drive, until technical constraints become important.

The disadvantage of relying on the linearized interaction is that, by itself, it will always turn Gaussian states (of the light field and the mechanics) into Gaussian states. These may be squeezed or entangled, but they will never have a negative Wigner density, which may be required for certain quantum applications. Note that there are some ways around this restriction, by introducing a nonlinearity at some other stage of the experiment: For example, one may send in single-photon pulses and then transfer these Fock states onto the mechanics using the linearized interaction. Another, sometimes equivalent, option is to perform single-photon detection at the end, thereby creating nonclassical states via a postselection of events. These strategies are therefore related to the general schemes that have been exploited already for linear optics quantum computation by adding single-photon sources and photodetectors (Knill, Laflamme, and Milburn, 2001).

Thus far, we encountered only two ideas on true nonlinear quantum optomechanics: The optical QND detection of the phonon number (Sec. VI.B.2) is such an example, and it indeed would prepare (probabilistically) Fock states of the mechanical oscillator. Another example, discussed early in the literature, is the optomechanical Schrödinger cat type of entanglement, where a single photon should ideally be able to displace the mechanical oscillator by about a mechanical zero-point width (Sec. X.C).

These examples require a large value of  $g_0$ , which is a challenge. We remind the reader that in a typical (Fabry-Pérot-type) setup the value of  $g_0$  can be estimated as

$$
g _ {0} = \omega_ {\mathrm {c a v}} \frac {x _ {\mathrm {Z P F}}}{L} = \omega_ {\mathrm {c a v}} \frac {1}{L} \sqrt {\frac {\hbar}{2 m _ {\mathrm {e f f}} \Omega_ {\mathrm {m}}}}. \tag {116}
$$

Here  $L$  is the effective size of the cavity, and  $m_{\mathrm{eff}}$  is the effective mass. Both can be made small by miniaturizing the setup, and consequently record values of  $g_{0}$  are achieved in micrometer-sized devices, such as photonic crystal nanobeams or very small disks and toroids. This is even in spite of the fact that miniaturization also drives up the mechanical frequency  $\Omega_{m}$ . In such setups,  $g_{0}$  currently takes values on the order of up to some MHz (see Sec. IV.A).

Next we discuss in which sense  $g_0$  can be "large." The steady-state displacement produced by a single photon on average ( $\bar{n}_{\mathrm{cav}} = 1$ ) is

$$
\frac {\delta x}{x _ {\mathrm {Z P F}}} = 2 \frac {g _ {0}}{\Omega_ {m}}. \tag {117}
$$

Thus, to displace by more than the zero-point width (mechanical ground-state width), one needs  $g_0 > \Omega_m$ . However, if the photon decay rate  $\kappa$  is large, then one can see only the average displacement produced by the photon number fluctuating around  $\bar{n}_{\mathrm{cav}} = 1$ , and one would not resolve the granularity of the photon stream. Such a situation should still be well described within the linearized approximation. To obtain truly nonlinear effects, one would want to make sure the following picture applies. Take any single photon entering the cavity. If its lifetime is large enough  $(\Omega_m \gg \kappa$ , the resolved-sideband

regime), it will displace the oscillator by the amount given in Eq. (117). This then implies  $g_0 \gg \kappa$  as a necessary (but not sufficient) condition.

These considerations directly lead us to consider the ratio

$$
\frac {g _ {0}}{\kappa}. \tag {118}
$$

If that ratio is larger than 1, then the presence of a single phonon will shift the optical frequency by more than a cavity linewidth. More precisely, the mechanical displacement produced by a superposition of 0 and 1 phonons will be measured so efficiently that the passage of a single photon through the cavity already destroys the superposition. We can also look at the light field's backaction: In the bad cavity limit ( $\kappa \gg \Omega_{m}$ ), a single passing photon with a lifetime  $\kappa^{-1}$  gives an average momentum kick  $\delta p = 2p_{\mathrm{ZPF}}g_0 / \kappa$  to the mechanical oscillator, which is larger than its zero-point momentum uncertainty  $p_{\mathrm{ZPF}} = m_{\mathrm{eff}}\Omega_mx_{\mathrm{ZPF}}$  if  $g_0 > \kappa$ . One can make a connection to the Lamb-Dicke parameter used in ion-trap physics, by defining the ratio of momentum kick to momentum zero-point fluctuations:  $\eta_{\mathrm{Lamb - Dicke}}\equiv \delta px_{\mathrm{ZPF}} / \hbar = \delta p / (2p_{\mathrm{ZPF}}) = g_0 / \kappa$ .

The ratio  $g_0 / \kappa$  has been called the "granularity parameter" (Murch et al., 2008), as  $g_0 / \kappa > 1$  allows one to reveal the granularity of the photon stream (the discreteness of individual photons). It has reached values on the order of and larger than 1 in experiments with clouds of ultracold atoms (see Sec. IV.G).

There are other ways of interpreting  $g_0 / \kappa > 1$  as well: The (sideband-resolved) cooling rate  $g_0^2 \bar{n}_{\mathrm{cav}} / \kappa$  will be so large that one enters the strong-coupling regime (Sec. VII.C) already for  $\bar{n}_{\mathrm{cav}} = 1$ . Alternatively,  $g_0 / \kappa$  can be written as the ratio between the mechanical zero-point fluctuations and the width of the optical cavity resonance, expressed in terms of a displacement (where the optomechanical coupling enters):

$$
\frac {g _ {0}}{\kappa} = \frac {x _ {\mathrm {Z P F}}}{\delta x _ {\mathrm {c a v}}},
$$

where  $\delta x_{\mathrm{cav}} = \kappa / G = \kappa x_{\mathrm{ZPF}} / g_0$

There is an additional interesting aspect about  $g_0 / \kappa$ . It can serve as a "quantumness" parameter (Ludwig, Kubala, and Marquardt, 2008), with larger values denoting a gradual classical-to-quantum crossover. All the parameters of any given standard optomechanical setup can be boiled down to the following five dimensionless combinations:

$$
\frac {\kappa}{\Omega_ {m}}, \quad Q _ {m} = \frac {\Omega_ {m}}{\Gamma_ {m}}, \quad \frac {\Delta}{\Omega_ {m}}, \quad \frac {g}{\kappa}, \quad \frac {g _ {0}}{\kappa}. \tag {119}
$$

Here the first four do not depend on the value of Planck's constant. This is obvious for the first three (the sideband-resolution ratio, the mechanical quality factor, and the laser detuning in units of mechanical frequency). It is less obvious for  $g / \kappa$ . However, this can be written as

$$
\frac {g}{\kappa} = \frac {g _ {0}}{\kappa} \sqrt {\bar {n} _ {\mathrm {c a v}}} = \sqrt {\frac {E _ {\mathrm {c a v}}}{2 m _ {\mathrm {e f f}} L ^ {2}} \frac {\omega_ {\mathrm {c a v}}}{\Omega_ {m}}}. \tag {120}
$$

Here  $E_{\mathrm{cav}} = \hbar \omega_{\mathrm{cav}} \bar{n}_{\mathrm{cav}}$  is the light energy stored inside the cavity, which is connected to the laser driving power. In this

sense,  $g / \kappa$  serves as a dimensionless classical measure of laser power. Only the ratio  $g_0 / \kappa$  depends on  $\hbar$ , as can be seen from Eq. (116):  $g_0 \propto \sqrt{\hbar}$ .

Thus, one can imagine keeping all four classical ratios fixed and increasing only  $g_0 / \kappa$  by changing parameters in the setup. This is then completely equivalent to increasing Planck's constant, allowing one to resolve more and more quantum features as  $g_0 / \kappa$  grows. It should be noted that of course even for  $g_0 / \kappa \ll 1$  one can observe quantum effects, but only in the linearized regime. Proving the quantumness of these effects produced by linearized interactions usually requires a quantitative comparison (e.g., with the light field's or the oscillator's zero-point fluctuations). In contrast, some features observed for larger values of  $g_0 / \kappa$  may even be qualitatively distinct from classical predictions. An example noted earlier is the quantum jumps of phonon number that could be observed for  $g_0 > \kappa_0$  (Sec. VI.B.2).

The third important ratio involving the coupling is

$$
\frac {g _ {0} ^ {2}}{\Omega_ {m} \kappa}.
$$

This is the ratio between the strength  $g_0^2 / \Omega_m$  of the effective photon-photon interaction induced by the mechanics and the optical linewidth. When this starts to be larger than 1 (and  $\kappa \ll \Omega_m$ ), then the presence of one photon shifts the resonance sufficiently that a second photon cannot enter the cavity. That leads to the photon-blockade phenomenon (see later).

Ludwig, Kubala, and Marquardt (2008) considered the regime of  $g_0 \sim \kappa \sim \Omega_m$  using both full numerical master equation simulations and a quantum Langevin approach. They found that for increasing values of  $g_0 / \kappa$  quantum fluctuations start to have a pronounced effect on the mechanical lasing instability that is observed at blue-detuned laser driving. The strongly enhanced susceptibility of the system just below the threshold amplifies the effects of these fluctuations, and the threshold is smeared and shifted. In this quantum regime, the coexistence of several attractors (known from the classical case, see Sec. VIII.A) results in non-Gaussian mechanical Wigner densities and mechanical states with non-Poissonian phonon distributions and large Fano factors (Ludwig, Kubala, and Marquardt, 2008). It was found that in this regime for appropriate parameters one can even generate true nonclassical mechanical states, with partially negative Wigner densities (Qian et al., 2012). These states are present in the steady state (under constant drive), so the Wigner densities could then be readout according to the schemes presented in Sec. VI. Another possibility for generating nonclassical states would be to design nanomechanical resonators that have very strong anharmonicities even at the single-phonon level (Rips et al., 2012).

Nunnenkamp, Borkje, and Girvin (2011) further extended master equation simulations to discuss the full range of detunings and the excitation spectrum of the cavity. Multiple optical sidebands are found, and the mechanical state of the oscillator is seen to develop non-Gaussian states particularly at detunings which drive multiphoton transitions.

The nonlinear quantum optomechanical regime leads to interesting photon correlations (see Fig. 45). In particular,

![](images/f6ff789af42bc3ea54964b8ecf15eb59cc9a354bcb355ec4c9a9133b942faa65.jpg)  
FIG. 45 (color online). Single-photon strong-coupling regime. (a) Displacement depending on photon number (leading to Franck-Condon physics). (b) Transmission sidebands. (c) Photon-photon correlator as a function of detuning (for weak drive). [(a), (b) Courtesy of A. Nunnenkamp, (c) courtesy of P. Rabl;  $g$  in this figure refers to our  $g_0$ ].

![](images/cd260a5f66415c1262af673cb4eb1be10544354f951a07ce1f17895b7ff5b07e.jpg)

![](images/3fcc5615380a6c7e3afdd18677c33f475a4cdf474d869cd3d9025dcb0dc80a37.jpg)

under appropriate conditions one may observe optomechanically induced photon blockade (Rabl, 2011). This shows up in the photon-photon correlations as strong antibunching  $g^{(2)}(t = 0) < 1$ , which has been calculated and discussed by Rabl (2011) for the case of weak laser driving. The regime of an optomechanical photon blockade requires sideband resolution ( $\kappa < \Omega_{m}$ ) as well as strong single-photon coupling with  $g_{0} > \kappa$  and  $g_{0}^{2} > \Omega_{m}\kappa$ . In more recent work, the analysis of photon correlations in this regime was extended to cover the full temporal evolution of  $g^{(2)}(t)$  and the Fano factor, as well as higher moments of the photon counting statistics (Kronwald, Ludwig, and Marquardt, 2013). Moreover, it was pointed out that first signatures of nonlinear quantum effects may be detected even for smaller values of  $g_{0} / \kappa$  by detailed investigation of certain OMIT features that would be absent if the Hamiltonian were correctly described by its linearized version (Borkje et al., 2013; Kronwald and Marquardt, 2013; Lemonde, Didier, and Clerk, 2013).

Liao, Cheung, and Law (2012) and Hong et al. (2013) presented exact solutions for the regime where only a single photon is transmitted through such a strongly coupled optomechanical setup, which is important for the generation of entanglement (Sec. X.C).

The understanding of the strongly nonlinear quantum regime is aided by the following picture, already partially discussed in Sec. X.C, and first employed by Bose, Jacobs, and Knight (1997) and Mancini, Man'ko, and Tombesi (1997): For any given photon number  $\bar{n}_{\mathrm{cav}}$ , the mechanical equilibrium position is shifted by an amount  $2x_{\mathrm{ZPF}}\bar{n}_{\mathrm{cav}}g_0 / \Omega_m$ . One should thus consider the mechanical Fock states in this new displaced parabolic potential.

If an additional photon enters the cavity, the potential suddenly shifts, but the mechanical wave function at first remains the same. Thus, the overlaps of the given initial wave function and the displaced new Fock states will determine the strength of possible transitions. These overlap integrals are known as Franck-Condon factors from the theory of molecules, where vibrations may be excited during electronic transitions.

We conclude by briefly describing the formal treatment via the well-known polaron transformation, as applied to an optomechanical system (Mancini, Man'ko, and Tombesi,

![](images/c1831b92af947191ceca10b22ba826935401225d13b176c6b2a46a90dd4e1fee.jpg)  
FIG. 46 (color online). The energy level spectrum of an optomechanical system at zero detuning  $\Delta = 0$ :  $E(n_{\mathrm{phonon}},n_{\mathrm{cav}}) / \hbar = -(g_0^2 /\Omega_m)n_{\mathrm{cav}}^2 +\Omega_m n_{\mathrm{phonon}}$ . Some possible processes are indicated: Blue-detuned laser drive at the first sideband ( $\Delta \approx +\Omega_{m}$ ) leading to the creation of a phonon and subsequent escape of the photon out of the cavity, a similar cycle at red-detuned drive ( $\Delta \approx -\Omega_{m}$ ) leading to cooling by annihilation of a phonon, photon-blockade-prohibiting transitions  $0\rightarrow 1\rightarrow 2$  toward two photons, and a resonant two-photon transition  $0\rightarrow 2$  via a virtual intermediate state (dashed). Note that the last two, nonlinear, effects require  $\Omega_{m}, g_{0}^{2} / \Omega_{m} > \kappa$ .

1997; Gröblacher, Hammerer et al., 2009; Nunnenkamp, Borkje, and Girvin, 2011; Rabl, 2011). We consider the standard optomechanical Hamiltonian (in the frame rotating with the laser frequency)

$$
\begin{array}{l} \hat {H} = - \hbar \Delta \hat {a} ^ {\dagger} \hat {a} + \hbar \Omega_ {m} \hat {b} ^ {\dagger} \hat {b} - \hbar g _ {0} \hat {a} ^ {\dagger} \hat {a} (\hat {b} + \hat {b} ^ {\dagger}) + \hbar \alpha_ {L} (\hat {a} + \hat {a} ^ {\dagger}) \\ + \hat {H} _ {\mathrm {b a t h}}, \\ \end{array}
$$

where  $\alpha_{L}$  is proportional to the laser amplitude. We complete the square to obtain

$$
\hbar \Omega_ {m} \left(\hat {b} - \frac {g _ {0}}{\Omega_ {m}} \hat {a} ^ {\dagger} \hat {a}\right) ^ {\dagger} \left(\hat {b} - \frac {g _ {0}}{\Omega_ {m}} \hat {a} ^ {\dagger} \hat {a}\right) - \hbar \left(g _ {0} ^ {2} / \Omega_ {m}\right) \left(\hat {a} ^ {\dagger} \hat {a}\right) ^ {2} \tag {121}
$$

for the second and third terms in  $\hat{H}$ . This shows two things: First, an effective photon-photon interaction is generated, viz., the  $(\hat{a}^{\dagger}\hat{a})^{2}$  term, which is crucial for nonlinear effects and quantum gates. Second,  $n$  photons shift  $\hat{b}$  by  $(g_0 / \Omega_m)n$ , i.e., they shift the equilibrium oscillator position by  $2x_{\mathrm{ZPF}}(g_0 / \Omega)n$  to the right. This can be accomplished by a unitary  $\hat{U} = \exp[(\hat{b}^{\dagger} - \hat{b})(g_0 / \Omega)\hat{a}^{\dagger}\hat{a}]$  acting on the wave functions. After applying that transformation to the Hamiltonian, via  $\hat{H}^{\mathrm{new}} = \hat{U}^{\dagger}\hat{H}\hat{U}$ , we obtain a Hamiltonian that is diagonal in the absence of driving and decay:

$$
\begin{array}{l} \hat {H} = - \hbar \left(\Delta + \frac {g _ {0} ^ {2}}{\Omega} \hat {a} ^ {\dagger} \hat {a}\right) \hat {a} ^ {\dagger} \hat {a} + \hbar \Omega \hat {b} ^ {\dagger} \hat {b} \\ + \alpha_ {L} \left(\hat {a} ^ {\dagger} e ^ {(\hat {b} - \hat {b} ^ {\dagger}) (g _ {0} / \Omega)} + \mathrm {H . c .}\right) + \hat {U} ^ {\dagger} \hat {H} _ {\text {b a t h}} \hat {U}. \tag {122} \\ \end{array}
$$

Note that in these new coordinates the addition of one photon shifts the wave function to the left, whereas the center of the mechanical oscillator potential is now forced to remain fixed (in contrast to the actual physical situation, where the potential shifts and the wave function is fixed). The exponential (polaron operator) in the laser driving term generates the Franck-Condon overlap factors.

The energy level scheme for the nonlinear quantum optomechanical regime (Fig. 46) displays equally spaced phonon ladders whose offset shifts depending on the photon number  $E(n_{\mathrm{phonon}}, n_{\mathrm{cav}}) / \hbar = -(\Delta + g_0^2 / \Omega_m n_{\mathrm{cav}}) n_{\mathrm{cav}} + \Omega_m n_{\mathrm{phonon}}$ . In this scheme, the driving laser induces only energy-conserving transitions, horizontal in the diagram. Different transitions are activated upon changing the detuning. Multiphoton transitions become possible via virtual nonresonant intermediate states (e.g., adding two photons at once).

# XI. FUTURE PERSPECTIVES

The fast experimental and theoretical advances in cavity optomechanics during recent years are constantly opening up new avenues with respect to applications and tests on the foundations of physics. Here we remark briefly on the broader outlook.

# A. Foundational aspects

The ability to achieve coherent quantum control over the center-of-mass motion of massive mechanical objects provides a fresh approach to fundamental tests of quantum theory in a hitherto unachieved parameter regime. Specifically, quantum optomechanics offers a universal scheme for experiments in the quantum regime of massive mechanical objects from clouds of  $10^{5}$  atoms or nanometer-sized solid-state devices of  $10^{7}$  atoms and a mass of  $10^{-20}$  kg, to micromechanical structures of  $10^{14}$  atoms and  $10^{-11}$  kg, to macroscopic centimeter-sized objects for gravitational wave detectors comprising more than  $10^{20}$  atoms and weighing up to several kg. In principle, this offers a range of almost 20 orders of magnitude in mass and 6 orders of magnitude in size for macroscopic quantum experiments.

A specific example where quantum optomechanics provides a new direction for future experiments is the quantum measurement problem, which addresses the question of why quantum superpositions do not seem to occur at the level of macroscopic objects (Leggett, 2002). Various new theories and phenomena beyond quantum theory have been suggested in order to achieve an irreversible decay of superposition states, i.e., decoherence, into well-defined classical states (Karolyhazy, 1966; Diosi, 1984; Penrose, 1996; Bassi and Ghirardi, 2003; Adler and Bassi, 2009). Each of these approaches predicts a particular scaling of the decoherence rates with particle number or mass, and with the actual distinctness of the states involved in the superposition. For sufficiently macroscopic systems and sufficiently distinct superposition states, these predictions deviate significantly from the decoherence rates expected from standard quantum theory (Zurek, 1991, 2003; Schlosshauer, 2008). Current matter-wave experiments with molecules may soon start to enter such a regime (Gerlich et al., 2011; Nimmrichter et al.,

2011). Systematic tests of the validity of quantum theory necessarily also involve tests of such scaling laws and the large mass range offered by quantum optomechanical systems provides a unique opportunity. One way of producing quantum states involving superpositions of mechanical states is via optomechanical entanglement (see Sec. X.C). Probing the decoherence of such optomechanical superposition states, for example, via the interference visibility in a single-photon interferometer (Bouwmeester et al., 1998; Bose, Jacobs, and Knight, 1999; Marshall et al., 2003; Pepper, Ghobadi et al., 2012; Pepper, Jeffrey et al., 2012), may allow decisive tests of specific "collapse" models (Bassi, Ippoliti, and Adler, 2005; Kleckner et al., 2008). A particularly exciting perspective is to extend these experiments to the large masses that are available in gravitational wave interferometers [see Chen (2013) for a recent review] and that were recently cooled to 200 thermal quanta above the quantum ground state (Abbott et al., 2009). Another route that has been suggested is to analyze the contrast of matter-wave interference of levitated nano-objects, where superpositions of macroscopically distinct position states are generated via optomechanics (Romero-Isart et al., 2011a). It was shown that such experiments would in principle allow one to enter a regime in which all nonstandard decoherence theories can be systematically tested (Romero-Isart, 2011). The demanding experimental boundary conditions with respect to temperature and background pressure (to minimize the effects of standard decoherence) might require the added benefit of a space environment. First studies along this line are currently being performed (Kaltenbaek et al., 2012).

The generation of macroscopic superposition states also allows for more general tests of quantum theory. One example is the validity of the assumption of macrealism by probing Leggett-Garg inequalities (Leggett and Garg, 1985). Proposals were recently put forward to realize this using optomechanical (Lambert, Johansson, and Nori, 2011) or electromechanical (Asadian, Brukner, and Rabl, 2013) devices.

Another fascinating long-term perspective is the possibility to make use of the accessible large masses in quantum optomechanics experiments to explore the scarcely studied interface between quantum physics and gravity. Some of its aspects are already covered by the decoherence tests discussed, as the models of Karolyhazy (1966), Diósi (1984, 2007), and Penrose (1996, 2000) identify gravity as the dominant player of their state-vector collapse. A completely different approach was taken by a recent proposal (Pikovski et al., 2012) that suggests that quantum optomechanics experiments could directly test predictions from quantum gravity, using pulsed quantum optomechanics (Vanner et al., 2011). Specifically, the availability of large masses in combination with quantum optical state preparation and readout is shown to be sensitive to possible deviations from the quantum commutation relation even at the Planck scale. This opens the route to table-top quantum optics tests of quantum gravity predictions.

The possibility of interconnecting optomechanical devices in large-scale arrays was already discussed in the context of investigating synchronization effects (Heinrich et al., 2011). The dynamics in such arrays may also enable the study of many-body quantum effects, which could complement the

current efforts in quantum simulations, yet in a solid-state architecture (Tomadin et al., 2012; Ludwig and Marquardt, 2013). Another scarcely explored direction is to exploit the role of nonlinear mechanical responses. For example, the double-well potential of bistable mechanical resonators (Bagheri et al., 2011) could be the starting point for macroscopic tunneling experiments.

Finally, it is interesting to note that in a broader context also, the topic of controlled photon-phonon interaction is receiving increasing attention. For example, a recent experiment demonstrated quantum entanglement between optical phonon modes of two separate macroscopic solids, specifically of millimeter-scale bulk diamond at room temperature (Lee et al., 2011), which was generated from photon-phonon entanglement. Besides providing an interesting alternative to obtaining quantum effects involving macroscopic objects this is also of direct relevance for applications, such as solid-state quantum memories. Other examples include new schemes to achieve coherent conversion of bosonic modes, and even suggestions to exploit the measurement of optomechanical recoil energies for mesoscopic mass standards (Lan et al., 2013).

# B. Applications

Although the field of cavity optomechanics is only in its infancy, several domains of applications have already become obvious. In laser sciences, these include tunable optical filters, based on the fact that optomechanical coupling can lead to extreme tuning of the mechanical frequency up to several octaves, as well as optomechanical implementations of laser stabilization (Alegre, Perahia, and Painter, 2010). In addition, the compatibility of some optomechanical devices with silicon photonics (see Sec. IV) enables on-chip optical architectures with added versatility. For example, exploiting strong optical nonlinearities provided by optomechanical cavities (see Sec. V) adds an important and long-sought feature to optical information processing. Along the same lines, embedded optomechanical cavities have been shown to serve as an all-optical memory element (Bagheri et al., 2011; Cole and Aspelmeyer, 2011), or have been proposed as a new technology for single-photon detection (Ludwig et al., 2012). In the first case, the binary states of a bistable nanomechanical resonator are controlled and monitored by an optomechanical cavity; in the latter case, a single photon induces a measureable frequency shift to an optomechanical cavity, thereby resulting in a detection that is in principle destruction-free and photon number resolving. In the long run, these features may provide a new momentum to all-optical information processing (Caulfield and Dolev, 2010).

For sensing applications, cavity optomechanics provides several new aspects: for example, while damping of mechanical motion has been used to increase the bandwidth of scanning microscopes for decades (Bruland et al., 1996; Garbini et al., 1996), cavity-optomechanical devices allow both readout and damping of much higher mechanical frequencies, hence providing faster sampling and scanning rates. At the same time, the high sensitivity of the optical readout allows new integrated optomechanical platforms for

acceleration sensing. A recent demonstration using optomechanical crystals achieved an on-chip acceleration resolution of  $10~\mu \mathrm{g} / \sqrt{\mathrm{Hz}}$  with a test mass of only a few ng (Krause et al., 2012). Cavity-optomechanics-based magnetometry may offer sensitivities as low as  $\mathrm{fT} / \sqrt{\mathrm{Hz}}$  at a large dynamic range (Forstner et al., 2012). Optomechanical cooling in combination with on-chip mechanical sensors has recently also been suggested to provide a reduction in thermal noise for the optical readout (Winger et al., 2011). In turn, the ability to coherently amplify mechanical motion provides a route to radiation-pressure-driven coherent oscillators with compact form factor and low power consumption. Finally, the combination with optomechanical preparation of squeezed mechanical states (see Sec. X.A) could lead to a new mechanical sensing technology with unprecedented levels of sensitivity due to the reduced position variance of the readout device. Suitable optomechanical setups may also lead to optical detection of small rf signals in an  $LC$  circuit (Taylor et al., 2011). This scheme was implemented experimentally recently (Bagci et al., 2014), using a high-quality room-temperature nanomembrane.

From a quantum information processing perspective cavity optomechanics offers a new architecture for coherent light-matter interfaces in a solid-state implementation. Mechanical motion can serve as a universal transducer to mediate long-range interactions between stationary quantum systems (see Sec. X.E). The specific trait of optomechanical systems is the interconversion between stationary qubits and flying (photonic) qubits, which constitutes one of the main elements of long-distance quantum communication and a future quantum internet (Kimble, 2008). At the same time, strong optomechanical coupling in the single-photon regime opens up the field of non-Gaussian quantum optomechanics with a wealth of quantum operations and protocols (see Sec. X.F). The phenomenon of optomechanically induced transparency enables slowing of light pulses or even their storage, hence providing an interesting solid-state implementation of a quantum memory (see Sec. VII.C.2).

Eventually, combining cavity optomechanics with other transduction mechanisms will allow one to exploit the full functionality of micromechanical and nanomechanical devices. Such quantum hybrid systems utilize the mechanical motion to achieve coupling between otherwise incompatible or uncoupled quantum systems (see Sec. X.D). A particularly exciting perspective of optoelectromechanical hybrid devices is their ability for coherent conversion between optical and microwave frequencies. First steps in this direction have been taken recently in two experiments (Bochmann et al., 2013; Andrews et al., 2014). Cavity cooling in these hybrid structures could also be applied to certain modes of a heat bath in integrated electronic circuits, for example, to suppress unwanted thermalization effects in spintronic devices (Usami et al., 2012). Another interesting direction is to couple individual qubits, for example, single atoms or single spins, to optomechanical devices. In combination with large mechanical frequencies such structures could allow mechanically mediated qubit interactions without additional laser cooling of the mechanical modes, thereby significantly relaxing the experimental requirements for information processing in qubit registers.

# ACKNOWLEDGMENTS

We thank our many colleagues and co-workers in the field, from whom we have learned a lot about this subject in numerous discussions. We are grateful to Anton Zeilinger for enabling a stay at the "Internationale Akademie Traunkirchen" in the summer of 2010, during which this review was started. Among the many helpful remarks we received from colleagues, we thank, in particular, Sebastian Hofer, Max Ludwig, Oskar Painter, Albert Schliesser, Ewold Verhagen, Dalziel Wilson, and Dan Stamper-Kurn for their critical reading of the manuscript and valuable feedback, and Uros Delic, David Grass, and Nikolai Kiesel for their assistance with figures and references. Each of us acknowledges support from a Starting Grant of the European Research Council (ERC StG). In addition, we acknowledge the following funding sources: the DFG with the Emmy-Noether Program (F.M.), the DARPA ORCHID Program (F.M. and T.J.K.), the European Commission FP7 STREP Project MINOS (M.A. and T.J.K.), and the Marie-Curie ITN cQOM (M.A., T.J.K., and F.M.). T.J.K. acknowledges funding from the Swiss National Science Foundation (SNF) and the NCCR of Quantum Engineering. M.A. acknowledges support from the Austrian Science Fund FWF (Projects FOQUS and START), from the European Commission (Q-Essence), and from the European Space Agency ESA.

# APPENDIX: EXPERIMENTAL CHALLENGES

# 1. Influence of classical excess laser phase noise on laser cooling

We briefly consider the role of laser noise in optomechanical cooling. Of particular interest is phase noise, described by the phase noise spectral density  $\bar{S}_{\phi \phi}(\Omega)$  [or alternatively described by its equivalent frequency noise  $\bar{S}_{\omega \omega}(\Omega) = \bar{S}_{\phi \phi}(\Omega)\Omega^2$ ]. Excess phase (and amplitude) noise can be found in many laser systems due to relaxation oscillations, which can even in the case of diode lasers extend well into the GHz regime (Wieman and Hollberg, 1991; Safavi-Naeini, Chan et al., 2013; Kippenberg, Schliesser, and Gorodetksy, 2013). Such excess phase noise was experimentally observed to heat the mechanical oscillator (Schliesser et al., 2008) and was analyzed theoretically (Diosi, 2008; Schliesser et al., 2008; Rabl et al., 2009; Jayich et al., 2012; Safavi-Naeini, Chan et al., 2013; Kippenberg, Schliesser, and Gorodetksy, 2013). The spectral density of force fluctuations caused by this noise when pumping on the lower sideband in the resolved sideband regime is given by (Schliesser et al., 2008) (with  $\eta = \kappa_{\mathrm{ex}} / \kappa$ )

$$
\bar {S} _ {F F} ^ {\mathrm {f n}} \left(\Omega_ {m}\right) \approx \frac {4 \eta^ {2} G ^ {2} P ^ {2}}{\omega_ {L} ^ {2} \Omega_ {m} ^ {4}} \bar {S} _ {\omega \omega} \left(\Omega_ {m}\right). \tag {A1}
$$

By comparing this force noise to an effective thermal Langevin force of the laser  $[\bar{S}_{FF}^{\mathrm{fn}}(\Omega_m) = 2m_{\mathrm{eff}}\Gamma_m\bar{n}_L\hbar \Omega_m]$  near the mechanical resonance an equivalent laser noise occupation  $\bar{n}_L$  can be derived. The final occupancy of the mechanical oscillator in the presence of optomechanical sideband cooling is subsequently

$$
\bar {n} _ {f} = \frac {\Gamma_ {m}}{\Gamma_ {m} + \Gamma_ {\mathrm {o p t}}} (\bar {n} _ {\mathrm {t h}} + \bar {n} _ {L}),
$$

where  $\bar{n}_{\mathrm{th}}$  denotes the average occupancy of the thermal bath. The excess contribution of the frequency noise is therefore

$$
\bar {n} _ {\min } ^ {\text {e x c e s s}} = \frac {\bar {n} _ {\text {c a v}}}{\kappa} S _ {\omega \omega} \left(\Omega_ {m}\right). \tag {A2}
$$

The lowest occupancy that can be attained in the presence of excess phase noise is given by (Rabl et al., 2009)

$$
\bar {n} _ {\min } = \sqrt {\frac {\bar {n} _ {\mathrm {t h}} \Gamma_ {m}}{g _ {0} ^ {2}} \bar {S} _ {\omega \omega} \left(\Omega_ {m}\right)}. \tag {A3}
$$

Equation (A3) can also be recast into a condition for the amount of phase noise that would lead to unit occupancy, i.e.,  $P_{0} = 0.5$ . Given the cavity photon number required to cool near to the ground state ( $\bar{n}_{f} = 1$ ), we find that  $n_{\mathrm{min}}^{\mathrm{excess}} > 1$  if the frequency noise exceeds the level (Rabl et al., 2009)

$$
\bar {S} _ {\omega \omega} (\Omega_ {m}) > \frac {g _ {0} ^ {2}}{k _ {B} T / \hbar Q _ {m}}. \tag {A4}
$$

If this level of noise is present, phase noise will preclude ground-state cooling. Equation (A4) also reveals that to mitigate the effect of phase noise it is generally desirable to have a large vacuum optomechanical coupling rate and a low mechanical damping rate, to increase the level of tolerable phase noise.

# 2. Influence of cavity frequency noise on laser cooling

The cavity frequency fluctuations are driven by thermodynamical temperature fluctuations. Considering the situation where light propagates inside a dielectric cavity (microtoroid, microspheres, photonic crystals) or penetrates a mirror surface, the temperature fluctuations of the sampled volume  $\mathcal{V}$  are determined by both the absolute temperature and the heat capacity of that volume:

$$
\left\langle \delta T ^ {2} \right\rangle = \frac {k _ {B} T ^ {2}}{\rho C \mathcal {V}}.
$$

Here  $C$  is the specific heat capacity (per mass). In general, these temperature fluctuations exhibit a spectral density that depends on the resonator geometry and boundary conditions for the thermal transport. For some cases, such as silica microspheres, the spectral densities  $S_{TT}[\omega]$  are known analytically (Gorodetsky and Grudinin, 2004) and the corresponding frequency noise  $S_{\omega \omega}[\omega] = K_{\mathrm{th}}^2 S_{TT}[\omega]$  can be evaluated [where  $K_{\mathrm{th}} = (dn / dT)\omega_0$  in the case of thermorefractive noise and  $K_{\mathrm{th}} = (d\alpha /dT)\omega_0$  in the case of thermoelastic noise]. While it has been noted that one can in principle compensate also thermorefractive noise (Kimble, Lev, and Ye, 2008), the noise is of particular relevance to optomechanical cooling as it provides a limit to the minimal occupancy. This can be understood with the model referred to in Appendix A.1, i.e., the fact that cavity frequency noise will translate into

radiation-pressure force fluctuations in the presence of a strong cooling laser.

# a. Finite thermal cavity occupancy

A further source of cavity noise can arise from the fact that the cooling field has thermal occupation. This is, in particular, the case for microwave fields due to their low frequency. If the cavity occupation is given by  $\bar{n}_{\mathrm{cav}}^{\mathrm{th}}$ , then the final occupation is modified to (in the resolved-sideband limit)

$$
\bar {n} _ {f} = \bar {n} _ {\mathrm {t h}} \frac {\Gamma_ {m}}{\Gamma_ {\mathrm {e f f}}} + \bar {n} _ {\mathrm {c a v}} ^ {\mathrm {t h}} + \frac {\kappa^ {2}}{1 6 \Omega_ {m} ^ {2}}. \tag {A5}
$$

This implies that the final phonon number can never be below the effective thermal occupation of the drive field (Dobrindt, Wilson-Rae, and Kippenberg, 2008). Note that when the radiation field and the mechanical oscillator initially have the same bath temperature (as is the case in equilibrium, without extra absorption), the equilibration of these two oscillators of frequency  $\omega_{\mathrm{cav}}$  and  $\Omega_{m}$  will lead to an effective cooling of the lower-frequency mechanical oscillator, as

$$
\bar {n} _ {\mathrm {t h}} \approx \frac {k _ {B} T _ {\mathrm {b a t h}}}{\hbar \Omega_ {m}} \gg \bar {n} _ {\mathrm {c a v}} \approx \frac {k _ {B} T _ {\mathrm {b a t h}}}{\hbar \omega_ {\mathrm {c a v}}}.
$$

# 3. Influence of classical excess laser noise on sideband thermometry

Excess noise of the readout laser (characterized by an occupancy  $\bar{n}_L$ ) compromises the self-calibration of the sideband thermometry method (Sec. VII.A), as it can lead equally to an asymmetry, since in the presence of laser noise

$$
\dot {N} ^ {\mathrm {c a v}} (\Delta = \Omega_ {m}) = \frac {\kappa_ {\mathrm {e x}}}{\kappa} A ^ {+} (\bar {n} _ {f} + 1 + \bar {n} _ {L})
$$

and

$$
\dot {N} ^ {\mathrm {c a v}} (\Delta = - \Omega_ {m}) ^ {\mathrm {l o w e r}} = \frac {\kappa_ {\mathrm {e x}}}{\kappa} A ^ {-} (\bar {n} _ {f} - \bar {n} _ {L}).
$$

This asymmetry can in this case be understood as arising from noise squashing and antisquashing of the classical and quantum noises alike. This noise-induced asymmetry on the upper and lower sidebands can also be viewed as originating from the effects of OMIT and EIA.

# REFERENCES

Aasi, J., et al., 2013, Nat. Photonics 7, 613.  
Abbott, B., et al., 2009, New J. Phys. 11, 073032.  
Abdi, M., S. Barzanjeh, P. Tombesi, and D. Vitali, 2011, Phys. Rev. A 84, 032325.  
Abramovici, A., et al., 1992, Science 256, 325.  
Adler, S. L., and A. Bassi, 2009, Science 325, 275.  
Agarwal, G. S., and S. Huang, 2010, Phys. Rev. A 81, 041803.  
Akram, U., N. Kiesel, M. Aspelmeyer, and G. J. Milburn, 2010, New J. Phys. 12, 083030.  
Akram, U., and G. J. Milburn, 2012, Phys. Rev. A 86, 042306.

Alegre, T. P. M., R. Perahia, and O. Painter, 2010, Opt. Express 18, 7872.  
Anderson, P. W., B. I. Halperin, and C. M. Varma, 1972, Philos. Mag. 25, 1.  
Andrews, R. W., R. W. Peterson, T. P. Purdy, K. Cicak, R. W. Simmonds, C. A. Regal, and K. W. Lehnert, 2014, Nat. Phys. 10, 321.  
Anetsberger, G., O. Arcizet, Q.P. Unterreithmeier, R. Rivière, A. Schliesser, E.M. Weig, J.P. Kotthaus, and T.J. Kippenberg, 2009, Nat. Phys. 5, 909.  
Anetsberger, G., R. Rivière, A. Schliesser, O. Arcizet, and T. J. Kippenberg, 2008, Nat. Photonics 2, 627.  
Antoni, T., et al., 2011, Opt. Lett. 36, 3434.  
Arcizet, O., P.-F. Cohadon, T. Briant, M. Pinard, and A. Heidmann, 2006a, Nature (London) 444, 71.  
Arcizet, O., P.-F. Cohadon, T. Briant, M. Pinard, A. Heidmann, J.-M. Mackowski, C. Michel, L. Pinard, O. François, and L. Rousseau, 2006b, Phys. Rev. Lett. 97, 133601.  
Arcizet, O., V. Jacques, A. Siria, P. Poncharal, P. Vincent, and S. Seidelin, 2011, Nat. Phys. 7, 879.  
Arcizet, O., C. Molinelli, T. Briant, P.-F. Cohadon, A. Heidmann, J.-M. Mackowksi, C. Michel, L. Pinard, O. Francais, and L. Rousseau, 2008, New J. Phys. 10, 125021.  
Armani, D.K., T.J. Kippenberg, S.M. Spillane, and K.J. Vahala, 2003, Nature (London) 421, 925.  
Asadian, A., C. Brukner, and P. Rabl, 2013, arXiv:1309.2229v1.  
Ashkin,A.,1978,Phys.Rev.Lett.40,729.  
Ashkin, A., 2006, Optical trapping and manipulation of neutral particles using lasers (World Scientific, Singapore).  
Ashkin, A., and J. M. Dziedzic, 1977, Appl. Phys. Lett. 30, 202.  
Aspelmeyer, M., S. Groblacher, K. Hammerer, and N. Kiesel, 2010, J. Opt. Soc. Am. B 27, A189.  
Aspelmeyer, M., P. Meystre, and K. C. Schwab, 2012, Phys. Today 65, No. 7, 29.  
Bagci, T., et al., 2014, Nature (London) 507, 81.  
Bagheri, M., M. Poot, M. Li, W. P. H. Pernice, and H. X. Tang, 2011, Nat. Nanotechnol. 6, 726.  
Bahl, G., M. Tomes, F. Marquardt, and T. Carmon, 2012, Nat. Phys. 8, 203.  
Bahl, G., J. Zehnpfennig, M. Tomes, and T. Carmon, 2011, Nat. Commun. 2, 403.  
Barker, P. F., 2010, Phys. Rev. Lett. 105, 073002.  
Barker, P. F., and M. N. Shneider, 2010, Phys. Rev. A 81, 023826.  
Barzanjeh, S., D. Vitali, P. Tombesi, and G. J. Milburn, 2011, Phys. Rev. A 84, 042342.  
Bassi, A., and G. Ghirardi, 2003, Phys. Rep. 379, 257.  
Bassi, A., E. Ippoliti, and S. Adler, 2005, Phys. Rev. Lett. 94, 030401.  
Beth,R.,1936,Phys.Rev.50,115.  
Bhattacharya, M., and P. Meystre, 2007a, Phys. Rev. Lett. 99, 073601.  
Bhattacharya, M., and P. Meystre, 2007b, Phys. Rev. Lett. 99, 153603.  
Bhattacharya, M., and P. Meystre, 2008, Phys. Rev. A 78, 041801.  
Bhattacharya, M., H. Uys, and P. Meystre, 2008, Phys. Rev. A 77, 033819.  
Bindel, D. S., and S. Govindjee, 2005, Int. J. Numer. Methods Eng. 64, 789.  
Blair, D. G., E. N. Ivanov, M. E. Tobar, P. J. Turner, F. van Kann, and I. S. Heng, 1995, Phys. Rev. Lett. 74, 1908.  
Blanter, Y. M., and M. Buttiker, 2000, Phys. Rep. 336, 1.  
Blatt, R., and D. Wineland, 2008, Nature (London) 453, 1008.  
Blencowe, M. P., 2005, Contemp. Phys. 46, 249.

Bloch,I.,andW.Zwerger,2008,Rev.Mod.Phys.80,885.  
Bochmann, J., A. Vainsencher, D. D. Awschalom, and A. N. Cleland, 2013, Nat. Phys. 9, 712.  
Bocko, Mark F., and Warren W. Johnson, 1984, Phys. Rev. A 30, 2135(R).  
Bohm, H. R., S. Gigan, G. Langer, J. B. Hertzberg, F. Blaser, D. Bauerle, K. C. Schwab, A. Zeilinger, and M. Aspelmeyer, 2006, Appl. Phys. Lett. 89, 223101.  
Borkje, K., A. Nunnenkamp, and S. M. Girvin, 2011, Phys. Rev. Lett. 107, 123601.  
Borkje, K., A. Nunnenkamp, J. D. Teufel, and S. M. Girvin, 2013, Phys. Rev. Lett. 111, 053603.  
Borkje, K., A. Nunnenkamp, B. M. Zwickl, C. Yang, J. G. E. Harris, and S. M. Girvin, 2010, Phys. Rev. A 82, 013818.  
Bose, S., K. Jacobs, and P. L. Knight, 1997, Phys. Rev. A 56, 4175.  
Bose, S., K. Jacobs, and P. L. Knight, 1999, Phys. Rev. A 59, 3204.  
Botter, T., D. W. C. Brooks, N. Brahms, S. Schreppler, and D. M. Stamper-Kurn, 2012, Phys. Rev. A 85, 013812.  
Bouwmeester, D., et al., 1998, Gravitation and Relativity at the turn of the Millennium (IUCAA Press, India).  
Braginsky, V., S. Strigin, and S. P. Vyatchanin, 2001, Phys. Lett. A 287, 331.  
Braginsky, V., Y. I. Vorontsov, and F. Y. Khalili, 1977, Sov. Phys. JETP 46, 705 [http://www.jetp.ac.ru/cgi-bin/e/index/e/46/4/p705?a=list].  
Braginsky, V. B., and F. Y. Khalili, 1996, Rev. Mod. Phys. 68, 1.  
Braginsky, V. B., and F. Y. A. Khalili, 1995, Quantum Measurements (Cambridge University Press, Cambridge, England).  
Braginsky, V. B., and A. B. Manukin, 1967, Sov. Phys. JETP 25, 653 [http://www.jetp.ac.ru/cgi-bin/e/index/e/25/4/p653?a=list].  
Braginsky, V. B., and A. B. Manukin, 1977, Measurement of weak forces in Physics experiments (University of Chicago Press, Chicago).  
Braginsky, V. B., A. B. Manukin, and M. Y. Tikhonov, 1970, Sov. Phys. JETP 31, 829 [http://www.jetp.ac.ru/cgi-bin/e/index/e/31/5/p829?a=list].  
Braginsky, V.B., V.P. Mitrofanov, and V.I. Panov, 1985, Systems with small dissipation (University of Chicago Press, Chicago).  
Braginsky, V. B., Y. I. Vorontsov, and F. Y. Khalili, 1978, JETP Lett. 27, 276 [http://www.jetpleletters.ac.ru/ps/1548/article_23699.shtml].  
Braginsky, V. B., Y. I. Vorontsov, and K. Thorne, 1980, Science 209, 547.  
Brahms, N., T. Botter, S. Schreppler, D. W. C. Brooks, and D. M. Stamper-Kurn, 2012, Phys. Rev. Lett. 108, 133601.  
Brahms, N., and D.M. Stamper-Kurn, 2010, Phys. Rev. A 82, 041804.  
Braunstein, S. L., and P. van Loock, 2005, Rev. Mod. Phys. 77, 513.  
Brennecke, F., S. Ritter, T. Donner, and T. Esslinger, 2008, Science 322, 235.  
Brooks, D. W. C., T. Botter, S. Schreppler, T. P. Purdy, N. Brahms, and D. M. Stamper-Kurn, 2012, Nature (London) 488, 476.  
Brown, K. R., J. Britton, R. J. Epstein, J. Chiaverini, D. Leibfried, and D. J. Wineland, 2007, Phys. Rev. Lett. 99, 137205.  
Bruland, K. J., J. L. Garbini, W. M. Dougherty, and J. A. Sidles, 1996, J. Appl. Phys. 80, 1959.  
Buck, Jr., J. R., 2003, Cavity QED in Microspere and Fabry-Perot Cavities, Ph.D. thesis (California Institute of Technology).  
Butsch, A., C. Conti, F. Biancalana, and P.S.J. Russell, 2012, Phys. Rev. Lett. 108, 093903.  
Butsch, A., M. S. Kang, T. G. Euser, J. R. Koehler, S. Rammler, R. Keding, and P. S. Russell, 2012, Phys. Rev. Lett. 109, 183904.  
Cai, M., O. Painter, and K. J. Vahala, 2000, Phys. Rev. Lett. 85, 74.

Camerer, S., M. Korppi, A. Jöckel, D. Hunger, T. W. Hänsch, and P. Treutlein, 2011, Phys. Rev. Lett. 107, 223001.  
Carmon, T., M. C. Cross, and K. J. Vahala, 2007, Phys. Rev. Lett. 98, 167203.  
Carmon, T., H. Rokhsari, L. Yang, T. J. Kippenberg, and K. J. Vahala, 2005, Phys. Rev. Lett. 94, 223902.  
Caulfield, H. J. and S. Dolev, 2010, Nat. Photonics 4, 261.  
Caves, C. M., 1980, Phys. Rev. Lett. 45, 75.  
Caves, C. M., 1981, Phys. Rev. D 23, 1693.  
Caves, C. M., 1982, Phys. Rev. D 26, 1817.  
Caves, C. M., K. S. Thorne, R. W. Drever, V. D. Sandberg, and M. Zimmermann, 1980, Rev. Mod. Phys. 52, 341.  
Chan, J., T. P. M. Alegre, A. H. Safavi-Naeini, J. T. Hill, A. Krause, S. Groblacher, M. Aspelmeyer, and O. Painter, 2011, Nature (London) 478, 89.  
Chang, D. E., K. K. Ni, O. Painter, and H. J. Kimble, 2012, New J. Phys. 14, 045002.  
Chang, D. E., C. A. Regal, S. B. Papp, D. J. Wilson, J. Ye, O. Painter, H. J. Kimble, and P. Zoller, 2010, Proc. Natl. Acad. Sci. U.S.A. 107, 1005.  
Chang, D. E., A. H. Safavi-Naeini, M. Hafezi, and O. Painter, 2011, New J. Phys. 13, 023003.  
Chen, W., D. S. Goldbaum, M. Bhattacharya, and P. Meystre, 2010, Phys. Rev. A 81, 053833.  
Chen, W., K. Zhang, D. S. Goldbaum, M. Bhattacharya, and P. Meystre, 2009, Phys. Rev. A 80, 011801.  
Chen, Y., 2013, J. Phys. B 46, 104001.  
Cirac, J., and P. Zoller, 1995, Phys. Rev. Lett. 74, 4091.  
Clark, J. R., W. T. Hsu, M. A. Abdelmoneum, and C. T.-C. Nguyen, 2005, J. Microelectromech. Syst. 14, 1298.  
Cleland,A.,2009,Nat.Phys.5,458.  
Cleland, A. N., J. S. Aldridge, D. C. Driscoll, and A. C. Gossard, 2002, Appl. Phys. Lett. 81, 1699.  
Cleland, A. N., and M. R. Geller, 2004, Phys. Rev. Lett. 93, 070501.  
Cleland, A. N., and M. L. Roukes, 1998, Nature (London) 392, 160.  
Cleland, A. N. N., 2003, Foundations of Nanomechanics (Springer, Berlin).  
Clerk, A. A., 2011, Phys. Rev. A 84, 043824.  
Clerk, A. A., M. H. Devoret, S. M. Girvin, F. Marquardt, and R. J. Schoelkopf, 2010, Rev. Mod. Phys. 82, 1155.  
Clerk, A. A., F. Marquardt, and J. G. E. Harris, 2010, Phys. Rev. Lett. 104, 213603.  
Clerk, A. A., F. Marquardt, and K. Jacobs, 2008, New J. Phys. 10, 095010.  
Cohadon, P.-F., A. Heidmann, and M. Pinard, 1999, Phys. Rev. Lett. 83, 3174.  
Cole, G., and M. Aspelmeyer, 2011, Nat. Nanotechnol. 6, 690.  
Cole, G. D., and M. Aspelmeyer, 2012, Quantum Optomechanics (Cambridge University Press, Cambridge, England), pp. 259-279.  
Cole, G. D., S. Gröblacher, S. Gugler, K. Gigan, and M. Aspelmeyer, 2008, Appl. Phys. Lett. 92, 261108.  
Cole, G. D., I. Wilson-Rae, M. R. Vanner, S. Groblacher, J. Pohl, M. Zorn, M. Weyers, A. Peters, and M. Aspelmeyer, 2010, in 2010 IEEE 23rd International Conference on Micro Electro Mechanical Systems (MEMS) (IEEE, New York), pp. 847-850.  
Cole, G.D., I. Wilson-Rae, K. Werbach, M.R. Vanner, and M. Aspelmeyer, 2011, Nat. Commun. 2, 231.  
Corbitt, T., Y. Chen, E. Innerhofer, H. Müller-Ebhardt, D. Ottaway, H. Rehbein, D. Sigg, S. Whitcomb, C. Wipf, and N. Mavalvala, 2007, Phys. Rev. Lett. 98, 150802.  
Corbitt, T., C. Wipf, T. Bodiya, D. Ottaway, D. Sigg, N. Smith, S. Whitcomb, and N. Mavalvala, 2007, Phys. Rev. Lett. 99, 160801.

Courty, J. M., A. Heidmann, and M. Pinard, 2001, Eur. Phys. J. D 17, 399.  
Cross, M., and R. Lifshitz, 2001, Phys. Rev. B 64, 085324.  
Cuthbertson, B. D., M. E. Tobar, E. N. Ivanov, and D. G. Blair, 1996, Rev. Sci. Instrum. 67, 2435.  
Dainese, P., P. S. Russell, N. Joly, J. C. Knight, G. S. Wiederhecker, H. L. Fragnito, V. Laude, and A. Khelif, 2006, Nat. Phys. 2, 388.  
Diedrich, F., J. C. Bergquist, W. M. Itano, and D. J. Wineland, 1989, Phys. Rev. Lett. 62, 403.  
Ding, L., C. Baker, P. Senellart, A. Lemaitre, S. Ducci, G. Leo, and I. Favero, 2011, Appl. Phys. Lett. 98, 113108.  
Ding, L., C. Baker, P. Senellart, A. Lemaitre, S. Ducci, G. Leo, and I. Favero, 2010, Phys. Rev. Lett. 105, 263903.  
Diosi, L., 1984, Phys. Lett. 105A, 199.  
Diosi, L., 2007, J. Phys. A 40, 2989.  
Diosi, L., 2008, Phys. Rev. A 78, 021801(R).  
Dobrindt, J. M., and T. J. Kippenberg, 2010, Phys. Rev. Lett. 104, 033901.  
Dobrindt, J. M., I. Wilson-Rae, and T. J. Kippenberg, 2008, Phys. Rev. Lett. 101, 263602.  
Dong, C., V. Fiore, M. C. Kuzyk, and H. Wang, 2012, Science 338, 1609.  
Dorsel, A., J. D. McCullen, P. Meystre, E. Vignes, and H. Walther, 1983, Phys. Rev. Lett. 51, 1550.  
Duwel, A., R.N. Candler, T.W. Kenny, and M. Varghese, 2006, J. Microelectromech. Syst. 15, 1437.  
Dykman, M. I., 1978, Sov. Phys. Solid State 20, 1306.  
Eichenfield, M., R. Camacho, J. Chan, K. J. Vahala, and O. Painter, 2009, Nature (London) 459, 550.  
Eichenfield, M., J. Chan, R.M. Camacho, K.J. Vahala, and O. Painter, 2009, Nature (London) 462, 78.  
Eichenfield, M., J. Chan, A. H. Safavi-Naeini, K. J. Vahala, and O. Painter, 2009, Opt. Express 17, 20078.  
Eichler, C., D. Bozyigit, C. Lang, M. Baur, L. Steffen, J. Fink, S. Filipp, and A. Wallraff, 2011, Phys. Rev. Lett. 107, 113601.  
Einstein, A., 1909, Z. Phys. 10, 817; English version of this paper is reprinted in the book http://www.pupress.princeton.edu/titles/4453.htm.  
Einstein, A., B. Podolsky, and N. Rosen, 1935, Phys. Rev. 47, 777.  
Ekinci, K. L., and M. L. Roukes, 2005, Rev. Sci. Instrum. 76, 061101.  
Elste, F., S. M. Girvin, and A. A. Clerk, 2009, Phys. Rev. Lett. 102, 207209.  
Fabre, C., M. Pinard, S. Bourzeix, A. Heidmann, E. Giacobino, and S. Reynaud, 1994, Phys. Rev. A 49, 1337.  
Farace, A., and V. Giovannetti, 2012, Phys. Rev. A 86, 013820.  
Faust, T., P. Krenn, S. Manus, J. P. Kotthaus, and E. M. Weig, 2012, Nat. Commun. 3, 728.  
Favero, I., and K. Karrai, 2008, New J. Phys. 10, 095006.  
Favero, I., and K. Karrai, 2009, Nat. Photonics 3, 201.  
Favero, I., C. Metzger, S. Camerer, D. König, H. Lorenz, J.P. Kotthaus, and K. Karrai, 2007, Appl. Phys. Lett. **90**, 104101.  
Favero, I., S. Stapfner, D. Hunger, P. Paulitschke, J. Reichel, H. Lorenz, E. M. Weig, and K. Karrai, 2009, Opt. Express 17, 12813.  
Fiore, V., Y. Yang, M. C. Kuzyk, R. Barbour, L. Tian, and H. Wang, 2011, Phys. Rev. Lett. 107, 133601.  
Fleischhauer, M., A. Imamoglu, and J. P. Marangos, 2005, Rev. Mod. Phys. 77, 633.  
Flowers-Jacobs, N. E., D. R. Schmidt, and K. W. Lehnert, 2007, Phys. Rev. Lett. 98, 096804.  
Folman, R., J. Schmiedmayer, H. Ritsch, and D. Vitali, 2001, Eur. Phys. J. D 13, 93.

Forstner, S., S. Prams, J. Knittel, E. D. van Ooijen, J. D. Swaim, G. I. Harris, A. Szarkovszky, W. P. Bowen, and H. Rubinsztein-Dunlop, 2012, Phys. Rev. Lett. 108, 120801.  
Frisch,O.,1933,Z.Phys.B86,42.  
Gangat, A. A., I. P. McCulloch, and G. J. Milburn, 2012, arXiv: 1211.4302.  
Gangat, A. A., T. M. Stace, and G. J. Milburn, 2011, New J. Phys. 13, 043024.  
Garbini, J. L., K. J. Bruland, W. M. Dougherty, and J. A. Sidles, 1996, J. Appl. Phys. 80, 1951.  
Gardiner, C. W., and P. Zoller, 2004, Quantum Noise, Springer Series in Synergetics (Springer, Berlin/Heidelberg).  
Gavartin, E., R. Braive, I. Sagnes, O. Arcizet, A. Beveratos, T. Kippenberg, and I. Robert-Philip, 2011, Phys. Rev. Lett. 106, 203902.  
Genes, C., A. Mari, D. Vitali, and P. Tombesi, 2009, Adv. At. Mol. Phys. 57, 33 [http://www.sciencedirect.com/science/article/pii/S1049250X09570024].  
Genes, C., H. Ritsch, M. Drewsen, and A. Dantan, 2011, Phys. Rev. A 84, 051801.  
Genes, C., H. Ritsch, and D. Vitali, 2009, Phys. Rev. A 80, 061803.  
Genes, C., D. Vitali, P. Tombesi, S. Gigan, and M. Aspelmeyer, 2008, Phys. Rev. A 77, 033804.  
Gerlich, S., S. Eibenberger, M. Tomandl, S. Nimmrichter, K. Hornberger, P.J. Fagan, J. Tuxen, M. Mayor, and M. Arndt, 2011, Nat. Commun. 2, 263.  
Ghobadi, R., A. R. Bahrampour, and C. Simon, 2011, Phys. Rev. A 84, 063827.  
Gieseler, J., B. Deutsch, R. Quidant, and L. Novotny, 2012, Phys. Rev. Lett. 109, 103603.  
Gigan, S., H. R. Böhm, M. Paternostro, F. Blaser, G. Langer, J. B. Hertzberg, K. C. Schwab, D. Bäuerle, M. Aspelmeyer, and A. Zeilinger, 2006, Nature (London) 444, 67.  
Giovannetti, V., S. Mancini, and P. Tombesi, 2001, Europhys. Lett. 54, 559.  
Gillespie, D. T., 1996, Am. J. Phys. 64, 225.  
Giovannetti, V., and D. Vitali, 2001, Phys. Rev. A 63, 023812.  
Gorodetsky, M. L., and I. S. Grudinin, 2004, J. Opt. Soc. Am. B 21, 697.  
Goryachev, M., D. L. Creedon, E. N. Ivanov, S. Galliou, R. Bourquin, and M. E. Tobar, 2012, Appl. Phys. Lett. **100**, 243504.  
Gozzini, A., F. Maccarrone, F. Mango, I. Longo, and S. Barbarino, 1985, J. Opt. Soc. Am. B 2, 1841.  
Greenberg, Y. S., Y. A. Pashkin, and E. Ilichev, 2012, Phys. Usp. 55, 382.  
Groblacher, S., K. Hammerer, M. R. Vanner, and M. Aspelmeyer, 2009, Nature (London) 460, 724.  
Groblacher, S., J. B. Hertzberg, M. R. Vanner, G. D. Cole, S. Gigan, K. C. Schwab, and M. Aspelmeyer, 2009, Nat. Phys. 5, 485.  
Grudinin, I. S., H. Lee, O. Painter, and K. J. Vahala, 2010, Phys. Rev. Lett. 104, 083901.  
Guerlin, C., J. Bernu, S. Deleglise, C. Sayrin, S. Gleyzes, S. Kuhr, M. Brune, J.-M. Raimond, and S. Haroche, 2007, Nature (London) 448, 889.  
Hadjar, Y., P.F. Cohadon, C.G. Aminoff, M. Pinard, and A. Heidmann, 1999, Europhys. Lett. 47, 545.  
Hammerer, K., M. Aspelmeyer, E. Polzik, and P. Zoller, 2009, Phys. Rev. Lett. 102, 020501.  
Hammerer, K., A. S. Sørensen, and E. S. Polzik, 2010, Rev. Mod. Phys. 82, 1041.  
Hammerer, K., K. Stannigel, C. Genes, P. Zoller, P. Treutlein, S. Camerer, D. Hunger, and T. Hänsch, 2010, Phys. Rev. A 82, 021803(R).

Hammerer, K., M. Wallquist, C. Genes, M. Ludwig, F. Marquardt, P. Treutlein, P. Zoller, J. Ye, and H. J. Kimble, 2009, Phys. Rev. Lett. 103, 063005.  
Hänsch, T. W., and A. L. Schawlow, 1975, Opt. Commun. 13, 68.  
Harlow, J. W., 2013, Microwave Electromechanics: Measuring and Manipulating the Quantum State of a Macroscopic Mechanical Oscillator, Ph.D. thesis (University of Colorado, Boulder, CO).  
Haroche, S., and J.-M. Raimond, 2006, Exploring the Quantum: Atoms, Cavities, and Photons (Oxford University Press, New York).  
Harry, G., T.P. Bodiya, and R. DeSalvo, 2011, Eds., Optical Coatings and Thermal Noise in Precision Measurement (Cambridge University Press, Cambridge, England).  
Harry, G. M., et al., 2002, Classical Quantum Gravity 19, 897.  
Hartmann, M. J., and M. B. Plenio, 2008, Phys. Rev. Lett. 101, 200503.  
Hechenblaikner, G., M. Gangl, P. Horak, and H. Ritsch, 1998, Phys. Rev. A 58, 3030.  
Heidmann, A., Y. Hadjar, and M. Pinard, 1997, Appl. Phys. B 64, 173.  
Heinrich, G., J. G. E. Harris, and F. Marquardt, 2010, Phys. Rev. A 81, 011801(R).  
Heinrich, G., M. Ludwig, J. Qian, B. Kubala, and F. Marquardt, 2011, Phys. Rev. Lett. 107, 043603.  
Hertzberg, J. B., T. Rocheleau, T. Ndukum, M. Savva, A. A. Clerk, and K. C. Schwab, 2010, Nat. Phys. 6, 213.  
Hill, J.T., A.H. Safavi-Naeini, J. Chan, and O. Painter, 2012, Nat. Commun. 3, 1196.  
Hocke, F., X. Zhou, A. Schliesser, T. J. Kippenberg, H. Huebl, and R. Gross, 2012, New J. Phys. 14, 123037.  
Hofer, J., A. Schliesser, and T. J. Kippenberg, 2010, Phys. Rev. A 82, 031804(R).  
Hofer, S.G., W. Wieczorek, M. Aspelmeyer, and K. Hammerer, 2011, Phys. Rev. A 84, 052327.  
Hoff, U. B., G. I. Harris, L. S. Madsen, H. Kerdoncuff, M. Lassen, B. M. Nielsen, W. P. Bowen, and U. L. Andersen, 2013, Opt. Lett. 38, 1413.  
Hofheinz, M., et al., 2009, Nature (London) 459, 546.  
Höhberger, C., and K. Karrai, 2004, in Proceedings of the 4th IEEE Conference on Nanotechnology (IEEE, New York).  
Höhberger-Metzger, C., and K. Karrai, 2004, Nature (London) 432, 1002.  
Holmes, C. A., C. P. Meaney, and G. J. Milburn, 2012, Phys. Rev. E 85, 066203.  
Hong, T., H. Yang, H. Miao, and Y. Chen, 2013, Phys. Rev. A 88, 023812.  
Huang, S., and G. S. Agarwal, 2009a, Phys. Rev. A 79, 013821.  
Huang, S., and G. S. Agarwal, 2009b, New J. Phys. 11, 103044.  
Huang, S., and G. S. Agarwal, 2009c, Phys. Rev. A 80, 033807.  
Huang, S., and G. S. Agarwal, 2010, Phys. Rev. A 81, 033830.  
Hunger, D., S. Camerer, M. Korppi, A. Jöckel, T. Hänsch, and P. Treutlein, 2011, C.R. Phys. 12, 871.  
Hunklinger, S., W. Arnold, and S. Stein, 1973, Phys. Lett. 45A, 311.  
Itano, W.M., J.C. Bergquist, J.J. Bollinger, and D.J. Wineland, 1992, Laser cooling of trapped ions (North-Holland, Amsterdam), pp. 519-537S.  
Jacobs, K., P. Tombesi, M. Collett, and D. Walls, 1994, Phys. Rev. A 49, 1961.  
Jaekel, M., and S. Renaud, 1991, J. Phys. I (France) 1, 1395.  
Jayich, A. M., J. C. Sankey, B. M. Zwickl, C. Yang, J. D. Thompson, S. M. Girvin, A. A. Clerk, F. Marquardt, and J. G. E. Harris, 2008, New J. Phys. 10, 095008.

Jayich, A.M., J.C. Sankey, K. Børkje, D. Lee, C. Yang, M. Underwood, L. Childress, A. Petrenko, S.M. Girvin, and J.G.E. Harris, 2012, New J. Phys. 14, 115018.  
Jiang, X., Q. Lin, J. Rosenberg, K. Vahala, and O. Painter, 2009, Opt. Express 17, 20911.  
Jing, H., D. S. Goldbaum, L. Buchmann, and P. Meystre, 2011, Phys. Rev. Lett. 106, 223601.  
Jöckel, A., M. T. Rakher, M. Korppi, S. Camerer, D. Hunger, M. Mader, and P. Treutlein, 2011, Appl. Phys. Lett. 99, 143109.  
Jost, J. D., J. P. Home, J. M. Amini, D. Hanneke, R. Ozeri, C. Langer, J. J. Bollinger, D. Leibfried, and D. J. Wineland, 2009, Nature (London) 459, 683.  
Judge, J. A., D. M. Photiadis, J. F. Vignola, B. H. Houston, and J. Jarzynski, 2007, J. Appl. Phys. 101, 013521.  
Kahili, F., S. Danilishin, H. Miao, H. Müller-Ebhardt, H. Yang, and Y. Chen, 2010, Phys. Rev. Lett. 105, 070403.  
Kaltenbaek, R., G. Hechenblaikner, N. Kiesel, O. Romero-Isart, K. C. Schwab, U. Johann, and M. Aspelmeyer, 2012, Exp. Astron. 34, 123.  
Kanamoto, R., and P. Meystre, 2010, Phys. Rev. Lett. 104, 063601.  
Kang, M. S., A. Brenn, and P. S. Russell, 2010, Phys. Rev. Lett. 105, 153901.  
Kang, M. S., A. Brenn, G. S. Wiederhecker, and P. S. Russell, 2008, Appl. Phys. Lett. 93, 131110.  
Kang, M. S., A. Butsch, and P. S. Russell, 2011, Nat. Photonics 5, 549.  
Kang, M.S., A. Nazarkin, A. Brenn, and P.S. Russell, 2009, Nat. Phys. 5, 276.  
Karabacak, D. M., V. Yakhot, and K. L. Ekinci, 2007, Phys. Rev. Lett. 98, 254505.  
Karolyhazy, F., 1966, Il Nuovo Cimento A 42, 390.  
Karrai, K., 2006, Nature (London) 444, 41.  
Karrai, K., I. Favero, and C. Metzger, 2008, Phys. Rev. Lett. 100, 240801.  
Kemiktarak, U., M. Metcalfe, M. Durand, and J. Lawall, 2012, Appl. Phys. Lett. 100, 061124.  
Kepler, J., 1619, De cometis libelli tres (Typis Andreae Apergiri).  
Kimble, H. J., 2008, Nature (London) 453, 1023.  
Kimble, H. J., B. L. Lev, and J. Ye, 2008, Phys. Rev. Lett. 101, 260602.  
Kippenberg, T., A. Schliesser, and M. Gorodetsky, 2013, New J. Phys. 15, 015019.  
Kippenberg, T. J., H. Rokhsari, T. Carmon, A. Scherer, and K. J. Vahala, 2005, Phys. Rev. Lett. 95, 033901.  
Kippenberg, T.J., and K.J. Vahala, 2007, Opt. Express 15, 17 172.  
Kippenberg, T. J., and K. J. Vahala, 2008, Science 321, 1172.  
Kiselev, A., and G. Iafrate, 2008, Phys. Rev. B 77, 205436.  
Kleckner, D., and D. Bouwmeester, 2006, Nature (London) 444, 75.  
Kleckner, D., W. T. M. Irvine, S. S. R. Oemrawsingh, and D. Bouwmeester, 2010, Phys. Rev. A 81, 043814.  
Kleckner, D., W. Marshall, J. M. A. De Dood, N. D. Khodadad, B.-J. Pors, W. T. M. Irvine, and D. Bouwmeester, 2006, Phys. Rev. Lett. 96, 173901.  
Kleckner, D., B. Pepper, E. Jeffrey, P. Sonin, S. M. Thon, and D. Bouwmeester, 2011, Opt. Express 19, 19708.  
Kleckner, D., I. Pikovski, E. Jeffrey, L. Ament, E. Eliel, J. van den Brink, and D. Bouwmeester, 2008, New J. Phys. 10, 095020.  
Knill, E., R. Laflamme, and G.J. Milburn, 2001, Nature (London) 409, 46.  
Koch, M., C. Sames, A. Kubanek, M. Apel, M. Balbach, A. Ourjountsev, P. W. H. Pinkse, and G. Rempe, 2010, Phys. Rev. Lett. 105, 173003.

Kolkowitz, S., A.C. Bleszynski Jayich, Q. Unterreithmeier, S.D. Bennett, P. Rabl, J.G.E. Harris, and M.D. Lukin, 2012, Science 335, 1603.  
Krause, A. G., M. Winger, T. D. Blasius, Q. Li, and O. Painter, 2012, Nat. Photonics 6, 768.  
Kronwald, A., M. Ludwig, and F. Marquardt, 2013, Phys. Rev. A 87, 013847.  
Kronwald, A., and F. Marquardt, 2013, Phys. Rev. Lett. 111, 133601.  
LaHaye, M.D., O. Buu, B. Camarota, and K.C. Schwab, 2004, Science 304, 74.  
LaHaye, M. D., J. Suh, P. M. Echternach, K. C. Schwab, and M. L. Roukes, 2009, Nature (London) 459, 960.  
Lambert, N., R. Johansson, and F. Nori, 2011, Phys. Rev. B 84, 245421.  
Lan, S.-Y., P.-C. Kuan, B. Estey, D. English, J. M. Brown, M. A. Hohensee, and Müller, H., 2013, Science 339, 554.  
Larson, J., B. Damski, G. Morigi, and M. Lewenstein, 2008, Phys. Rev. Lett. 100, 050401.  
Larson, J., and M. Horsdal, 2011, Phys. Rev. A 84, 021804.  
Law, C. K., 1995, Phys. Rev. A 51, 2537.  
Lebedew, P., 1901, Ann. Phys. (Berlin) 311, 433.  
Lee, K.C., et al., 2011, Science 334, 1253.  
Lee, K. H., T. G. McRae, G. I. Harris, J. Knittel, and W. P. Bowen, 2010, Phys. Rev. Lett. 104, 123604.  
Leggett, A., and A. Garg, 1985, Phys. Rev. Lett. 54, 857.  
Leggett, A.J., 2002, J. Phys. Condens. Matter 14, R415.  
Leibfried, D., R. Blatt, C. Monroe, and D. Wineland, 2003, Rev. Mod. Phys. 75, 281.  
Leibfried, D., D. Meekhof, B. King, C. Monroe, W. Itano, and D. Wineland, 1996, Phys. Rev. Lett. 77, 4281.  
Lemonde, M. A., N. Didier, and A. A. Clerk, 2013, Phys. Rev. Lett. 111, 053602.  
Lezama, A., S. Barreiro, and A. Akulshin, 1999, Phys. Rev. A 59, 4732.  
Li, M., W. Pernice, and H. Tang, 2009a, Nat. Photonics 3, 464.  
Li, M., W. H. P. Pernice, and H. X. Tang, 2009b, Nat. Nanotechnol. 4, 377.  
Li, M., W. H. P. Pernice, and H. X. Tang, 2009c, Phys. Rev. Lett. 103, 223901.  
Li, M., W. H. P. Pernice, C. Xiong, T. Baehr-Jones, M. Hochberg, and H. X. Tang, 2008, Nature (London) 456, 480.  
Li, T., S. Kheifets, and M. G. Raizen, 2011, Nat. Phys. 7, 527.  
Liao, J.-Q., H. K. Cheung, and C. K. Law, 2012, Phys. Rev. A 85, 025803.  
Liao, J. Q., and C. K. Law, 2011, Phys. Rev. A 83, 033820.  
Lifshitz, R., and M. L. Roukes, 2000, Phys. Rev. B 61, 5600.  
Lin, Q., J. Rosenberg, X. Jiang, K. Vahala, and O. Painter, 2009, Phys. Rev. Lett. 103, 103601.  
Lin, Q., J. Rosenberg, D. Chang, R. Camacho, M. Eichenfield, K. J. Vahala, and O. Painter, 2010, Nat. Photonics 4, 236.  
Liu, J., K. Usami, A. Naesby, T. Bagci, E. S. Polzik, P. Lodahl, and S. Stobbe, 2011, Appl. Phys. Lett. 99, 243102.  
Liu, Y.C., Y.F. Xiao, X. Luan, and W.C. Wong, 2013, Phys. Rev. Lett. 110, 153606.  
Locke, C.R., M.E. Tobar, E.N. Ivanov, and D.G. Blair, 1998, J. Appl. Phys. 84, 6523.  
Ludwig, M., K. Hammerer, and F. Marquardt, 2010, Phys. Rev. A 82, 012333.  
Ludwig, M., B. Kubala, and F. Marquardt, 2008, New J. Phys. 10, 095013.  
Ludwig, M., and F. Marquardt, 2013, Phys. Rev. Lett. 111, 073603.

Ludwig, M., A. Safavi-Naeini, O. Painter, and F. Marquardt, 2012, Phys. Rev. Lett. 109, 063601.  
Lvovsky, A. I., and M. G. Raymer, 2009, Rev. Mod. Phys. 81, 299.  
Ma, R., A. Schliesser, P. Del'Haye, A. Dabirian, G. Anetsberger, and T. Kippenberg, 2007, Opt. Lett. 32, 2200.  
Machnes, S., J. Cerrillo, M. Aspelmeyer, W. Wieczorek, M. B. Plenio, and A. Retzker, 2012, Phys. Rev. Lett. 108, 153601.  
Maldova, M., and E. L. Thomas, 2006, Appl. Phys. Lett. 88, 251907.  
Mallet, F., M. Castellanos-Beltran, H. Ku, S. Glancy, E. Knill, K. Irwin, G. Hilton, L. Vale, and K. Lehnert, 2011, Phys. Rev. Lett. 106, 220502.  
Mancini, S., V. I. Man'ko, and P. Tombesi, 1997, Phys. Rev. A 55, 3042.  
Mancini, S., and P. Tombesi, 1994, Phys. Rev. A 49, 4055.  
Mancini, S., D. Vitali, and P. Tombesi, 1998, Phys. Rev. Lett. 80, 688.  
Mancini, S., D. Vitali, and P. Tombesi, 2003, Phys. Rev. Lett. 90, 137901.  
Mari, A., and J. Eisert, 2009, Phys. Rev. Lett. 103, 213603.  
Mari, A., and J. Eisert, 2012, New J. Phys. 14, 075014.  
Marino, F., F. S. Cataliotti, A. Farsi, M. S. de Cumis, and F. Marin, 2010, Phys. Rev. Lett. 104, 073601.  
Marquardt, F., 2011, Nature (London) 478, 47.  
Marquardt, F., J.P. Chen, A.A. Clerk, and S.M. Girvin, 2007, Phys. Rev. Lett. 99, 093902.  
Marquardt, F., A. A. Clerk, and S. M. Girvin, 2008, J. Mod. Opt. 55, 3329.  
Marquardt, F., and S. M. Girvin, 2009, Physics 2, 40.  
Marquardt, F., J. G. E. Harris, and S. M. Girvin, 2006, Phys. Rev. Lett. 96, 103901.  
Marshall, W., C. Simon, R. Penrose, and D. Bouwmeester, 2003, Phys. Rev. Lett. 91, 130401.  
Massel, F., S. U. Cho, J.-M. Pirkkalainen, P.J. Hakonen, T.T. Heikkila, and M.A. Sillanpää, 2012, Nat. Commun. 3, 987.  
Massel, F., T. T. Heikkila, J.M. Pirkkalainen, S.U. Cho, H. Saloniemi, P. Hakonen, and M.A. Sillanpää, 2011, Nature (London) 480, 351.  
Matsko, A. B., A. A. Savchenko, V. S. Ilchenko, D. Seidel, and L. Maleki, 2009, Phys. Rev. Lett. 103, 257403.  
Mattila, T., 2002, Sens. Actuators, A 101, 1.  
Mertz, J., O. Marti, and J. Mlynek, 1993, Appl. Phys. Lett. 62, 2344.  
Metcalf, H.J., and P. van der Straten, 1999, *Laser Cooling and Trapping* (Springer, New York).  
Metzger, C., I. Favero, A. Ortlieb, and K. Karrai, 2008a, Phys. Rev. B 78, 035309.  
Metzger, C., I. Favero, A. Ortlieb, and K. Karrai, 2008b, Phys. Rev. B 78, 035309.  
Metzger, C., M. Ludwig, C. Neuenhahn, A. Ortlieb, I. Favero, K. Karrai, and F. Marquardt, 2008, Phys. Rev. Lett. 101, 133903.  
Meystre, P., 2013, Ann. Phys. (Berlin) 525, 215.  
Meystre, P., E. M. Wright, J. D. McCullen, and E. Vignes, 1985, J. Opt. Soc. Am. B 2, 1830.  
Miao, H., S. Danilishin, and Y. Chen, 2010, Phys. Rev. A 81, 052307.  
Miao, H., S. Danilishin, T. Corbitt, and Y. Chen, 2009, Phys. Rev. Lett. 103, 100402.  
Miao, H., S. Danilishin, H. Müller-Ebhardt, H. Rehbein, K. Somiya, and Y. Chen, 2010, Phys. Rev. A 81, 012114.  
Mohanty, P., D. A. Harrington, K. L. Ekinci, Y. T. Yang, M. J. Murphy, and M. L. Roukes, 2002, Phys. Rev. B 66, 085416.  
Mow-Lowry, C. M., A. J. Mullavey, S. Goßler, M. B. Gray, and D. E. McClelland, 2008, Phys. Rev. Lett. 100, 010801.  
Müller-Ebhardt, H., H. Rehbein, R. Schnabel, K. Danzmann, and Y. Chen, 2008, Phys. Rev. Lett. 100, 013601.

Müller-Ebhardt, H., H. Rehbein, C. Li, Y. Mino, K. Somiya, R. Schnabel, K. Danzmann, and Y. Chen, 2009, Phys. Rev. A 80, 043802.  
Murch, K.W., K.L. Moore, S. Gupta, and D.M. Stamper-Kurn, 2008, Nat. Phys. 4, 561.  
Naik, A., O. Buu, M. D. LaHaye, A. D. Armour, A. A. Clerk, M. P. Blencowe, and K. C. Schwab, 2006, Nature (London) 443, 193.  
Neuhauser, W., M. Hohenstatt, P. Toschek, and H. Dehmelt, 1978, Phys. Rev. Lett. 41, 233.  
Ni, K. K., R. Norte, D. J. Wilson, J. D. Hood, D. E. Chang, O. Painter, and H. J. Kimble, 2012, Phys. Rev. Lett. 108, 214302.  
Nichols, E. F., and G. F. Hull, 1901, Phys. Rev. 13, 307 [http://dx.doi.org/10.1103/PhysRevSeriesI.13.307].  
Nimmrichter, S., K. Hornberger, P. Haslinger, and M. Arndt, 2011, Phys. Rev. A 83, 043621.  
Numata, K., A. Kemery, and J. Camp, 2004, Phys. Rev. Lett. 93, 250602.  
Nunnenkamp, A., K. Borkje, and S. M. Girvin, 2011, Phys. Rev. Lett. 107, 063602.  
Nunnenkamp, A., K. Borkje, J. G. E. Harris, and S. M. Girvin, 2010, Phys. Rev. A 82, 021806.  
O'Connell, A. D., et al., 2010, Nature (London) 464, 697.  
Pace, A., M. Collett, and D. Walls, 1993, Phys. Rev. A 47, 3173.  
Palomaki, T., J. Harlow, J. Teufel, R. Simmonds, and K. Lehnert, 2013, Nature (London) 495, 210.  
Palomaki, T. A., J. D. Teufel, R. W. Simmonds, and K. W. Lehnert, 2013, Science 342, 710.  
Park, Y.-H., and K. Park, 2004, J. Microelectromech. Syst. 13, 238.  
Park, Y.-S., and H. Wang, 2009, Nat. Phys. 5, 489.  
Parkins, A. S., and H. J. Kimble, 1999, J. Opt. B 1, 496.  
Paternostro, M., D. Vitali, S. Gigan, M. S. Kim, C. Brukner, J. Eisert, and M. Aspelmeyer, 2007, Phys. Rev. Lett. 99, 250401.  
Peil, S., and G. Gabrielse, 1999, Phys. Rev. Lett. 83, 1287.  
Pender, G. A. T., P. F. Barker, F. Marquardt, T. S. Monteiro, and J. Millen, 2012, Phys. Rev. A 85, 021802.  
Penrose, R., 1996, Gen. Relativ. Gravit. 28, 581.  
Penrose, R., 2000, Quantum [un]speakables: from Bell to quantum information (Springer, New York), pp. 319-330.  
Pepper, B., R. Ghobadi, E. Jeffrey, C. Simon, and D. Bouwmeester, 2012, Phys. Rev. Lett. 109, 023601.  
Pepper, B., E. Jeffrey, R. Ghobadi, C. Simon, and D. Bouwmeester, 2012, New J. Phys. 14, 115025.  
Pernice, W., M. Li, and H. Tang, 2008, Appl. Phys. Lett. 93, 213106.  
Pernice, W., M. Li, and H. Tang, 2009, Opt. Express 17, 1806.  
Phillips, W., 1987, Rep. Prog. Phys. 50, 1657.  
Photiadis, D. M., and J. A. Judge, 2004, Appl. Phys. Lett. 85, 482.  
Pikovski, I., M. R. Vanner, M. Aspelmeyer, M. S. Kim, and C. Brukner, 2012, Nat. Phys. 8, 393.  
Pinard, M., and A. Dantan, 2008, New J. Phys. 10, 095012.  
Pinard, M., A. Dantan, D. Vitali, O. Arcizet, T. Briant, and A. Heidmann, 2005, Europhys. Lett. 72, 747.  
Pinard, M., C. Fabre, and A. Heidmann, 1995, Phys. Rev. A 51, 2443.  
Pinard, M., Y. Hadjar, and A. Heidmann, 1999, Eur. Phys. J. D 7, 107 [http://link.springer.com/article/10.1007/s100530050354].  
Pirandola, S., S. Mancini, D. Vitali, and P. Tombesi, 2003, Phys. Rev. A 68, 062317.  
Pirandola, S., D. Vitali, P. Tombesi, and S. Lloyd, 2006, Phys. Rev. Lett. 97, 150403.  
Pirkkalainen, J. M., S. U. Cho, J. Li, G. S. Paraoanu, P. S. Hakonen, and M. A. Sillanpää, 2013, Nature (London) 494, 211.  
Poggio, M., C. L. Degen, H. J. Mamin, and D. Rugar, 2007, Phys. Rev. Lett. 99, 017201.

Poot, M., and H. S. J. van der Zant, 2012, Phys. Rep. 511, 273.  
Purdy, T. P., D. W. C. Brooks, T. Botter, N. Brahms, Z.-Y. Ma, and D. M. Stamper-Kurn, 2010, Phys. Rev. Lett. 105, 133602.  
Purdy, T. P., R. W. Peterson, and C. A. Regal, 2013, Science 339, 801.  
Qian, J., A. A. Clerk, K. Hammerer, and F. Marquardt, 2012, Phys. Rev. Lett. 109, 253601.  
Rabl, P., 2011, Phys. Rev. Lett. 107, 063601.  
Rabl, P., C. Genes, K. Hammerer, and M. Aspelmeyer, 2009, Phys. Rev. A 80, 063819.  
Regal, C. A., and K. W. Lehnert, 2011, J. Phys. Conf. Ser. 264, 012025.  
Regal, C. A., J. D. Teufel, and K. W. Lehnert, 2008, Nat. Phys. 4, 555.  
Remus, L., M. Blencowe, and Y. Tanaka, 2009, Phys. Rev. B 80, 174103.  
Restrepo, J., J. Gabelli, C. Ciuti, and I. Favero, 2011, Comptes Rendues Physique 12, 860 [http://www.sciencedirect.com/science/article/pii/S1631070511000570].  
Riedrich-Moller, J., et al., 2012, Nat. Nanotechnol. 7, 69.  
Rips, S., and M. J. Hartmann, 2013, Phys. Rev. Lett. 110, 120503.  
Rips, S., M. Kiffner, I. Wilson-Rae, and M. J. Hartmann, 2012, New J. Phys. 14, 023042.  
Ritter, S., C. Nolleke, C. Hahn, A. Reiserer, A. Neuzner, M. Uphoff, M. Mucke, E. Figueroa, J. Bochmann, and G. Rempe, 2012, Nature (London) 484, 195.  
Riviere, R., S. Deleglise, S. Weis, E. Gavartin, O. Arcizet, A. Schliesser, and T. Kippenberg, 2011, Phys. Rev. A 83, 063835.  
Rocheleau, T., T. Ndukum, C. Macklin, J. B. Hertzberg, A. A. Clerk, and K. C. Schwab, 2010, Nature (London) 463, 72.  
Rodriguez, D. A., and A. D. Armour, 2010, Phys. Rev. Lett. 104, 053601.  
Roh, Y.-G., T. Tanabe, A. Shinya, H. Taniyama, E. Kuramochi, S. Matsuo, T. Sato, and M. Notomi, 2010, Phys. Rev. B 81, 121101(R).  
Rokhsari, H., M. Hossein-Zadeh, A. Hajimiri, and K. Vahala, 2006, Appl. Phys. Lett. 89, 261109.  
Rokhsari, H., T. J. Kippenberg, T. Carmon, and K. J. Vahala, 2005, Opt. Express 13, 5293.  
Romero-Isart, O., 2011, Phys. Rev. A 84, 052121.  
Romero-Isart, O., M.L. Juan, R. Quidant, and J.I. Cirac, 2010, New J. Phys. 12, 033015.  
Romero-Isart, O., A. Pflanzer, F. Blaser, R. Kaltenbaek, N. Kiesel, M. Aspelmeyer, and J. Cirac, 2011a, Phys. Rev. Lett. 107, 020405.  
Romero-Isart, O., A. C. Pflanzer, F. Blaser, R. Kaltenbaek, N. Kiesel, M. Aspelmeyer, and J. I. Cirac, 2011b, Phys. Rev. Lett. 107, 020405.  
Romero-Isart, O., A. C. Pflanzer, M. L. Juan, R. Quidant, N. Kiesel, M. Aspelmeyer, and J. I. Cirac, 2011c, Phys. Rev. A 83, 013803.  
Rugar, D., R. Budakian, H. J. Mamin, and B. W. Chui, 2004, Nature (London) 430, 329.  
Rugar, D., and P. Grütter, 1991, Phys. Rev. Lett. 67, 699.  
Rundquist, A., and A. Majumdar, 2011, Appl. Phys. Lett. 99, 251907.  
Safavi-Naeini, A., J. Chan, J. T. Hill, S. Groeblacher, H. Miao, Y. Chen, M. Aspelmeyer, and O. Painter, 2013, New J. Phys. 15, 035007.  
Safavi-Naeini, A.H., J. Chan, J.T. Hill, T.P. Mayer Alegre, A. Krause, and O. Painter, 2012, Phys. Rev. Lett. 108, 033602.  
Safavi-Naeini, A. H., T. P. M. Alegre, M. Winger, and O. Painter, 2010, Appl. Phys. Lett. 97, 181106.  
Safavi-Naeini, A.H., S. Gröblacher, J.T. Hill, J. Chan, M. Aspelmeyer, and O. Painter, 2013, Nature (London) 500, 185.

Safavi-Naeini, A.H., T.P. Mayer Alegre, J. Chan, M. Eichenfield, M. Winger, Q. Lin, J.T. Hill, D.E. Chang, and O. Painter, 2011, Nature (London) 472, 69.  
Safavi-Naeini, A. H., and O. Painter, 2010, Opt. Express 18, 14926.  
Safavi-Naeini, A. H., and O. Painter, 2011, New J. Phys. 13, 013017.  
Sankey, J.C., C. Yang, B.M. Zwickl, A.M. Jayich, and J.G.E. Harris, 2010, Nat. Phys. 6, 707.  
Santamore, D. H., A. C. Doherty, and M. C. Cross, 2004, Phys. Rev. B 70, 144301.  
Saulson, P. R., 1990, Phys. Rev. D 42, 2437.  
Savchenko, A. A., A. B. Matsko, V. S. Ilchenko, D. Seidel, and L. Maleki, 2011, Opt. Lett. 36, 3338.  
Schawlow, A., and C. Townes, 1958, Phys. Rev. 112, 1940.  
Schleier-Smith, M. H., I. D. Leroux, H. Zhang, M. A. V. Camp, and V. Vuleti, 2011, Phys. Rev. Lett. 107, 143005.  
Schliesser, A., 2009, "Cavity optomechanics and optical frequency comb generation with silica whispering-gallery-mode resonators," Ph.D. thesis (Ludwig-Maximilians-Universität München).  
Schliesser, A., G. Anetsberger, R. Rivière, O. Arcizet, and T.J. Kippenberg, 2008, New J. Phys. 10, 095015.  
Schliesser, A., O. Arcizet, R. Riviere, G. Anetsberger, and T.J. Kippenberg, 2009, Nat. Phys. 5, 509.  
Schliesser, A., P. Del'Haye, N. Nooshi, K.J. Vahala, and T.J. Kippenberg, 2006, Phys. Rev. Lett. 97, 243905.  
Schliesser, A., and T.J. Kippenberg, 2010, Advances in atomic, molecular and optical physics (Elsevier Academic Press, New York).  
Schliesser, A., R. Rivière, G. Anetsberger, O. Arcizet, and T. Kippenberg, 2008, Nat. Phys. 4, 415.  
Schlosshauer, M., 2008, Decoherence and the Quantum-to-Classical Transition (Springer, New York).  
Schmidt, M., M. Ludwig, and F. Marquardt, 2012, New J. Phys. 14, 125005.  
Schreppler, S., N. Spethmann, N. Brahms, T. Botter, M. Barrios, and D. M. Stamper-Kurn, 2014, Science 344, 1486.  
Schwab, K. C., and M. L. Roukes, 2005, Phys. Today 58, No. 7, 36.  
Seoáñez, C., F. Guinea, and A. Castro Neto, 2008, Phys. Rev. B 77, 125107.  
Serra, E., A. Borrielli, F. S. Cataliotti, F. Marin, F. Marino, A. Pontin, G. A. Prodi, and M. Bonaldi, 2012, Phys. Rev. A 86, 051801(R).  
Sheard, B., M. Gray, C. Mow-Lowry, and D. McClelland, 2004, Phys. Rev. A 69, 051801.  
Shelby, R. M., M. D. Levenson, and P. W. Bayer, 1985, Phys. Rev. B 31, 5244.  
Singh, S., G. A. Phelps, D. S. Goldbaum, E. M. Wright, and P. Meystre, 2010, Phys. Rev. Lett. 105, 213602.  
Southworth, D., R. Barton, S. Verbridge, B. Ilic, A. Fefferman, H. Craighead, and J. Parpia, 2009, Phys. Rev. Lett. 102, 225503.  
Stamper-Kurn, D.M., 2014, "Cavity optomechanics with cold atoms," Cavity Optomechanics (Springer, New York) [http://link.springer.com/book/10.1007%2F978-3-642-55312-7].  
Stannigel, K., P. Komar, S. J. M. Habraken, S. D. Bennett, M. D. Lukin, P. Zoller, and P. Rabl, 2012, Phys. Rev. Lett. 109, 013603.  
Stannigel, K., P. Rabl, A. S. Sorensen, M. D. Lukin, and P. Zoller, 2011, Phys. Rev. A 84, 042341.  
Stannigel, K., P. Rabl, A. S. Sorensen, P. Zoller, and M. D. Lukin, 2010, Phys. Rev. Lett. 105, 220501.  
Steinke, S. K., S. Singh, M. E. Tasgin, P. Meystre, K. C. Schwab, and M. Vengalattore, 2011, Phys. Rev. A 84, 023841.  
Stenholm, S., 1986, Rev. Mod. Phys. 58, 699.  
Suh, J., A. J. Weinstein, C. U. Lei, E. E. Wollman, S. K. Steinke, P. Meystre, A. A. Clerk, K. C. Schwab, 2014, Science 344, 1262.

Szarkovszky, A., A. C. Doherty, G. I. Harris, and W. P. Bowen, 2011, Phys. Rev. Lett. **107**, 213603.  
Tallur, S., S. Sridaran, S. Bhave, and T. Carmon, 2010, in Frequency Control Symposium (FCS) (IEEE International, New York).  
Taylor, J. M., A. S. Sørensen, C. M. Marcus, and E. S. Polzik, 2011, Phys. Rev. Lett. 107, 273601.  
Teufel, J. D., R. Donner, M. A. Castellanos-Beltran, J. W. Harlow, and K. W. Lehnert, 2009, Nat. Nanotechnol. 4, 820.  
Teufel, J. D., T. Donner, D. Li, J. W. Harlow, M. S. Allman, K. Cicak, A. J. Sirois, J. D. Whittaker, K. W. Lehnert, and R. W. Simmonds, 2011, Nature (London) 475, 359.  
Teufel, J. D., J. W. Harlow, C. A. Regal, and K. W. Lehnert, 2008, Phys. Rev. Lett. 101, 197203.  
Teufel, J.D., D. Li, M.S. Allman, K. Cicak, A.J. Sirois, J.D. Whittaker, and R.W. Simmonds, 2011, Nature (London) 471, 204.  
Thompson, J. D., B. M. Zwickl, A. M. Jayich, F. Marquardt, S. M. Girvin, and J. G. E. Harris, 2008, Nature (London) 452, 72.  
Tian, L., 2012, Phys. Rev. Lett. 108, 153604.  
Tian, L., and H. Wang, 2010, Phys. Rev. A 82, 053806.  
Tielbürger, D., R. Merz, R. Ehrenfels, and S. Hunklinger, 1992, Phys. Rev. B 45, 2750.  
Tittonen, I., G. Breitenbach, T. Kalkbrenner, T. Müller, R. Conradt, S. Schiller, E. Steinsland, N. Blanc, and N.F. de Rooij, 1999, Phys. Rev. A 59, 1038.  
Tomadin, A., S. Diehl, M. D. Lukin, P. Rabl, and P. Zoller, 2012, Phys. Rev. A 86, 033821.  
Tomes, M., and T. Carmon, 2009, Phys. Rev. Lett. 102, 113601.  
Tomes, M., F. Marquardt, G. Bahl, and T. Carmon, 2011, Phys. Rev. A 84, 063806.  
Treutlein, P., D. Hunger, S. Camerer, T. Hänsch, and J. Reichel, 2007, Phys. Rev. Lett. 99, 140403.  
Unruh, W. G., 1983, Quantum Optics, Experimental Gravitation and Measurement Theory (Plenum Press, New York).  
Unterreithmeier, Q., T. Faust, and J. Kotthaus, 2010, Phys. Rev. Lett. 105, 027205.  
Usami, K., A. Naesby, T. Bagci, B. M. Nielsen, J. Liu, S. Stobbe, P. Lodahl, and E. S. Polzik, 2012, Nat. Phys. 8, 168.  
Vahala, K., 2004, Optical microcavities, Advanced series in applied physics (World Scientific, Singapore).  
Vahala, K., 2008, Phys. Rev. A 78, 023832.  
Vahala, K., C. Harder, and A. Yariv, 1983, Appl. Phys. Lett. 42, 211.  
Vahala, K. J., 2003, Nature (London) 424, 839.  
Vanner, M. R., M. Aspelmeyer, and M. S. Kim, 2013, Phys. Rev. Lett. 110, 010504.  
Vanner, M. R., J. Hofer, G. D. Cole, and M. Aspelmeyer, 2012, Nat. Commun. 4, 2295 [http://www.nature.com/ncomms/2013/130815/ncomms3295/full/ncomms3295.html].  
Vanner, M. R., I. Pikovski, G. D. Cole, M. S. Kim, C. Brukner, K. Hammerer, G. J. Milburn, and M. Aspelmeyer, 2011, Proc. Natl. Acad. Sci. U.S.A. 108, 16 182.  
Venkatesan, A., K. J. Lulla, M. J. Patton, A. D. Armour, C. J. Mellor, and J. R. Owers-Bradley, 2010, Phys. Rev. B 81, 073410.  
Verbridge, S. S., H. G. Craighead, and J. M. Parpia, 2008, Appl. Phys. Lett. **92**, 013112.  
Verhagen, E., S. Deleglise, S. Weis, A. Schliesser, and T.J. Kippenberg, 2012, Nature (London) 482, 63.  
Verlot, P., A. Tavernarakis, T. Briant, P.-F. Cohadon, and A. Heidmann, 2009, Phys. Rev. Lett. 102, 103601.  
Verlot, P., A. Tavernarakis, T. Briant, P.-F. Cohadon, and A. Heidmann, 2010, Phys. Rev. Lett. 104, 133602.  
Verlot, P., et al., 2011, C.R. Phys. 12, 826.  
Vidal, G., and R. F. Werner, 2002, Phys. Rev. A 65, 032314.

Vignola, J. F., J. A. Judge, J. Jarzynski, M. Zalalutdinov, B. H. Houston, and J. W. Baldwin, 2006, Appl. Phys. Lett. 88, 041921.  
Vitali, D., S. Gigan, A. Ferreira, H.R. Böhm, P. Tombesi, A. Guerreiro, V. Vedral, A. Zeilinger, and M. Aspelmeyer, 2007, Phys. Rev. Lett. 98, 030405.  
Vitali, D., S. Mancini, L. Ribichini, and P. Tombesi, 2002, Phys. Rev. A 65, 063803.  
Vogel, M., C. Mooser, K. Karrai, and R. J. Warburton, 2003, Appl. Phys. Lett. 83, 1337.  
Vuletic, V., and S. Chu, 2000, Phys. Rev. Lett. 84, 3787.  
Vyatchanin, S. P., and A. B. Matsko, 1993, Sov. Phys. JETP 77, 218 [http://www.jetp.ac.ru/cgi-bin/e/index/e/77/2/p218?a=list].  
Wallquist, M., K. Hammerer, P. Zoller, C. Genes, M. Ludwig, F. Marquardt, P. Treutlein, J. Ye, and H. J. Kimble, 2010, Phys. Rev. A 81, 023816.  
Walls, D. F., and G. J. Milburn, 1994, Quantum Optics (Springer, New York).  
Wang, K., A.-C. Wong, and C.T.-C. Nguyen, 2000, J. Microelectromech. Syst. 9, 347.  
Wang, X., S. Vinjanampathy, F.W. Strauch, and K. Jacobs, 2011, Phys. Rev. Lett. 107, 177204.  
Wang, Y.-D., and A. A. Clerk, 2012, Phys. Rev. Lett. 108, 153603.  
Weinstein, A. J., C. U. Lei, E. E. Wollman, J. Suh, A. Metelmann, A. A. Clerk, and K. C. Schwab, 2014, Phys. Rev. X 4, 041003.  
Weis, S., R. Riviere, S. Deleglise, E. Gavartin, O. Arcizet, A. Schliesser, and T. J. Kippenberg, 2010, Science 330, 1520.  
Weiss, T., C. Bruder, and A. Nunnenkamp, 2013, New J. Phys. 15, 045017.  
Westphal, T., D. Friedrich, H. Kaufer, K. Yamamoto, S. Goßler, H. Müller-Ebhardt, S. L. Danilishin, F. Y. Khalili, K. Danzmann, and R. Schnabel, 2012, Phys. Rev. A 85, 063806.  
Wiederhecker, G. S., A. Brenn, H. L. Fragnito, and P. S. Russell, 2008, Phys. Rev. Lett. 100, 203903.  
Wiederhecker, G. S., L. Chen, A. Gondarenko, and M. Lipson, 2009, Nature (London) 462, 633.  
Wieman, C. E., and L. Hollberg, 1991, Rev. Sci. Instrum. 62, 1.  
Wilson, D., C. Regal, S. Papp, and H. Kimble, 2009, Phys. Rev. Lett. 103, 207204.

Wilson-Rae,I.,2008,Phys.Rev.B77,245418.  
Wilson-Rae, I., N. Nooshi, J. Dobrindt, T.J. Kippenberg, and W. Zwerger, 2008, New J. Phys. 10, 095007.  
Wilson-Rae, I., N. Nooshi, W. Zwerger, and T. J. Kippenberg, 2007, Phys. Rev. Lett. 99, 093901.  
Wilson-Rae, I., P. Zoller, and A. Imamoglu, 2004, Phys. Rev. Lett. 92, 075507.  
Wineland, D. J., 2013, Rev. Mod. Phys. 85, 1103.  
Wineland, D. J., and H. Dehmelt, 1975, Bull. Am. Phys. Soc. 20, 637.  
Wineland, D. J., and W. M. Itano, 1979, Phys. Rev. A 20, 1521.  
Winger, M., T. D. Blasius, T. P. M. Alegre, A. H. Safavi-Naeini, S. Meenehan, J. Cohen, S. Stobbe, and O. Painter, 2011, Opt. Express 19, 24 905.  
Wipf, C., T. Corbitt, Y. Chen, and N. Mavalvala, 2008, New J. Phys. 10, 095017.  
Wu, H., G. Heinrich, and F. Marquardt, 2013, New J. Phys. 15, 123022.  
Xiong, H., L.-G. Si, A.-S. Zheng, X. Yang, and Y. Wu, 2012, Phys. Rev. A 86, 013815.  
Xuereb, A., C. Genes, and A. Dantan, 2012, Phys. Rev. Lett. 109, 223601.  
Xuereb, A., R. Schnabel, and K. Hammerer, 2011, Phys. Rev. Lett. 107, 213604.  
Yasumura, K., T. Stowe, E. Chow, T. Pfafman, T. Kenny, B. Stipe, and D. Rugar, 2000, J. Microelectromech. Syst. 9, 117.  
Zalalutdinov, M., A. Zehnder, A. Olkhovets, S. Turner, L. Sekaric, B. Ilic, D. Czaplewski, J. M. Parpia, and H. G. Craighead, 2001, Appl. Phys. Lett. 79, 695.  
Zener, C., 1938, Phys. Rev. 53, 90.  
Zhang, J., K. Peng, and S. L. Braunstein, 2003, Phys. Rev. A 68, 013808.  
Zhang, M., G. Wiederhecker, S. Manipatruni, A. Barnard, P.L. McEuen, and M. Lipson, 2012, Phys. Rev. Lett. 109, 233906.  
Zoller, P., et al., 2005, Eur. Phys. J. D 36, 203.  
Zurek,W.H.,2003,Rev.Mod.Phys.75,715.  
Zurek, W. H., 1991, Phys. Today 44, No. 10, 36.