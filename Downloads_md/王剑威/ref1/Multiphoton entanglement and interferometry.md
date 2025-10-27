# Multiphoton entanglement and interferometry

Jian-Wei Pan, $^{1,*}$  Zeng-Bing Chen, $^{1,†}$  Chao-Yang Lu, $^{1,‡}$  Harald Weinfurter, $^{2,3,§}$

Anton Zeilinger, $^{4,5,}$  and Marek Zukowski $^{6,7,1,}$

<sup>1</sup>Hefei National Laboratory for Physical Sciences at Microscale and Department of Modern Physics, University of Science and Technology of China, Hefei, Anhui 230026, China  
$^{2}$ Fakultät für Physik, Ludwig-Maximilians-Universität, D-80799 München, Germany  
3Max-Planck-Institut für Quantenoptik, D-85748 Garching, Germany  
$^{4}$ Vienna Center of Quantum Science and Technology (VCQ), Faculty of Physics, Universität Wien, Boltzmanngasse 5, A-1090 Wien, Austria  
$^{5}$ Institut für Quantenoptik und Quanteninformation (IQOQI), Österreichische Akademie der Wissenschaften, Boltzmanngasse 3, A-1090 Wien, Austria  
$^{6}$ Instytut Fizyki Teoretycznej i Astrofizyki, Uniwersytet Gdańsk, PL-80-952 Gdańsk, Poland  
<sup>7</sup>Institut für Experimentalphysik, Universität Wien, Boltzmanngasse 5, A-1090 Wien, Austria

(published 11 May 2012)

Multiphoton interference reveals strictly nonclassical phenomena. Its applications range from fundamental tests of quantum mechanics to photonic quantum information processing, where a significant fraction of key experiments achieved so far comes from multiphoton state manipulation. The progress, both theoretical and experimental, of this rapidly advancing research is reviewed. The emphasis is given to the creation of photonic entanglement of various forms, tests of the completeness of quantum mechanics (in particular, violations of local realism), quantum information protocols for quantum communication (e.g., quantum teleportation, entanglement purification, and quantum repeater), and quantum computation with linear optics. The scope of the review is limited to "few-photon" phenomena involving measurements of discrete observables.

DOI: 10.1103/RevModPhys.84.777

PACS numbers: 03.65.Ud, 03.67.-a, 42.50.-p

# CONTENTS

I. Introduction 778

A.Quantum optics 778  
B. The essence of the quantum world: Entanglement 779  
C. Sources of photonic entanglement 779  
D. Applications in quantum information 780  
E. Related reviews 780  
F. Our aims 780

II. Interference and quantum entanglement 780

A.Classical interference 781  
B.Quantum interference 781

1. Single-particle quantum interference 781  
2. Two-particle quantum interference 782

C.Quantum entanglement 782  
D. Interferometry with entangled two-photon and multiphoton states 784

1. EPR interferometry 784  
2. Greenberger Horne Zeilinger interferometry 784

E. Interferometry with multiport beam splitters 785

III. Photonic qubits and linear optics 785

A. Photonic qubits 785  
B. Simple linear-optical elements 786

C. Two-photon interference due to indistinguishability of photons 787  
D.Postselection of entanglement and quantum erasure 789

E. Entangled-state analyzers 789

1.Bell-state analyzer 790  
2. GHZ-state analyzer 790

IV. Experimental realizations of photonic entanglement 791

A. Spontaneous parametric down-conversion 791  
B. Photonic entanglement in higher dimensions 793

1. Entangled quids 793  
2. Hyperentanglement 793

C. Twin-beam multiphoton entanglement 794  
D. Multiphoton entanglement 795

1. Entanglement construction 796  
2.New methods 797  
3. First proposals 798  
4.Experimentalrealizations 798

V.Falsification of a realistic world view 800

A.Bell's inequality 801  
B.GHZ theorem 803

1. Impossibility of deriving realism via perfect quantum correlations and locality 803  
2. GHZ theorem for laboratory measurement 804  
3. Two-observer GHZ-like correlations 805  
4.Hardy'sparadoxes 805

C. Refutation of a class of nonlocal realistic theories 806  
D. Noncontextual hidden-variable theories 807

VI. Quantum communication 808

A.Quantum dense coding 809  
B.Quantum teleportation 809

1. Theory: Qubit teleportation involving an EPR channel and two bit transfer 809  
2.Experimental quantum teleportation 811  
3. Teleportation onto freely flying photons 811  
4. Teleportation of a qubit carried by a photon of the ancillary EPR pair 812  
5. Teleportation with various physical systems 813  
6. More-involved teleportations 813

C. Entanglement swapping 814

1. Theory 814  
2. First experimental demonstration 815  
3. Other experiments on entanglement swapping 815

D. Beating noisy environment 816

1. Entanglement distillation and concentration 817  
2. Entanglement purification 817

E. Long-distance entanglement distribution 819

F.Quantum memory and quantum repeaters 820

1.Quantum repeater protocol 820  
2. Quantum state transfer between matter and photons 822

VII. Photonic quantum computing 823

A. Linear-optical two-qubit logic gates 823  
B. Cluster-state quantum computing 824

1.Constructing photonic cluster states 824

C. Few-photon quantum computing experiments 825  
D. Toward scalable optical quantum computing 826

VIII. Concluding remarks 827

Appendix A: The two-photon states produced by SPDC 828

# I. INTRODUCTION

In his 1704 treatise, Opticks Newton claimed that light is composed of particles, and strongly opposed Huygens wave picture. Later on with Young's double-slit interference experiments, the wave picture seemed to be correct and sufficient. This view was further strengthened by Maxwell's electrodynamics. Yet, 201 years after Newton, during his annus mirabilis Einstein reintroduced lichtquanten (light particles) and in this way explained the photoelectric effect (Einstein, 1905). The ultimate consequences of Einstein's ideas, after fundamental works of Bohr, Heisenberg, and Schroedinger, gave birth to quantum mechanics in 1925. Quantum electrodynamics, the final theory of light, in which photons are elementary excitations of the quantized electromagnetic field interacting with charges, was given by Dirac (1927), and its internal consistency was proved by Dyson, Feynman, Schwinger, and Tonomaga around 20 years later. According to these theories, photons, as all quantum particles, reveal both wavelike and particlelike properties, a phenomenon known as wave-particle duality. The wave nature is revealed by interference, while the particle nature can be recognized in absorption and detection events, or more generally in the statistics of counts. The interference patterns involving single photons or, equally well, the light intensity does not reveal strictly nonclassical phenomena. Some of the most counterintuitive effects begin with two or

more photon interference and in intensity correlation measurements: a plethora of classically impossible phenomena occurs, most of them completely incomprehensible with any classical concepts, neither particle nor wave. As always, in the history of human scientific endeavor, harnessing of new phenomena leads to new applications. The aim of this review is to describe the recent theoretical and experimental advances in multiphoton interference, entanglement, manipulation, and their applications in quantum communication and computation.

# A. Quantum optics

An intensive research of the quantum properties of light started around half a century ago. Its advances allow one to gain a coherent control of quantum optical systems, enabling true quantum engineering. As a result, quantum optical methods made possible to actually perform gedanken experiments concerning the foundations of quantum theory. This control of quantum phenomena further allows one to search for novel information-processing protocols, which now promise new technologies based on quantum information science.

Soon after Einstein's introduction of light quanta, Taylor (1909) tried to find some new effects in a two-slit Young-type experiment using extremely faint light, so faint that on average only one photon at a time was inside the apparatus. No deviation from the classical interference was observed. Now, with a fully developed theory of quantized light, we know that experiments of this type cannot differentiate between the classical explanation (based on the interference of electric field waves) and the quantum explanation (based on the interference of probability amplitudes for photons passing through either of the two slits). The inherently "quantum nature of the electromagnetic field," as we know now, is revealed directly in multiphoton experiments which were not possible earlier.

Still, quantum interference of truly individual photons is certainly a fascinating phenomenon. The first precise experiment aimed at exactly this was performed by Grangier, Roger, and Aspect (1986). They used photon pairs emitted in atomic cascades, one of the photons was used as a trigger, and the other was fed into a Mach-Zehnder interferometer. When detectors are placed in the two arms of the interferometer, besides background noise, no simultaneous detection (i.e., coincidence) in both detectors was observed,[2] i.e., the photon was found only in one of the two arms, a typical particlelike behavior. However, after overlapping the two arms by the output beam splitter of the interferometer the usual (wavelike) interference pattern was observed. Recently, Braig et al. (2003) demonstrated that, when also observing interference depending on the phase difference between both arms, the light from the interferometer output exhibited the characteristic single-photon antibunching.

Modern quantum optics was effectively born in 1956 when Hanbury Brown and Twiss (1956) introduced intensity interferometry. It was the first serious attempt to study the

correlations between intensities recorded at two separated detectors. It motivated more sophisticated photon counting and correlation experiments. The quantum theory of optical coherence of Glauber (1963) gave theoretical clues to search for unambiguously quantum optical phenomena. Carmichael and Walls (1976a, 1976b) predicted photon antibunching in a resonance fluorescence, which was observed experimentally by Kimble, Dagenais, and Mandel (1977). The early experiments used atomic beams as sources. Thus, atomic number (and emission statistics) fluctuations were unavoidable. Later, Diedrich and Walther (1987) realized such experiments using a single trapped ion and observed photon antibunching as well as sub-Poissonian statistics in the system. Squeezed states of light were experimentally generated by using a four-wave mixing in atomic sodium (Slusher et al., 1985) and in optical fibers (Shelby et al., 1986), or by using an optical parametric oscillator (Wu et al., 1986). Interested readers may find excellent reviews in Mandel and Wolf (1995), Scully and Zubairy (1997), Walls and Milburn (1994), and Lounis and Orrit (2005).

The study on photon statistics and photon-counting techniques enables direct examination of some fundamental distinctions between quantum and classical concepts of light. Parallel developments in neutron, atomic, and molecular interferometry, as well as modern methods of cooling and trapping ions, etc., allowed one to probe ever deeper the properties of individual quantum systems and to realize many of the gedanken (thought) experiments testing the foundations quantum physics.

# B. The essence of the quantum world: Entanglement

Entanglement is a property of more than one quantum system such that the state of one system cannot be seen independent of the other's system. It forms the basis for the most remarkable, purely quantum effects and is the main resource for the many applications of quantum information processing. Initially, it was used by Einstein, Podolsky, and Rosen (1935) to show that quantum mechanics is incomplete. The trio, Einstein, Podolsky, and Rosen (EPR), argued that the outcome of a measurement on any physical system is determined prior to and independent of the measurement (realism) and that the outcome cannot depend on any actions in spacelike separated regions (Einstein's locality). This EPR criterion of, what is now called, "local realism" should be fulfilled by every physical description of nature, and, indeed, it looks quite reasonable to us, particularly as all our classical world and experience fully adhere to it. They used the perfect correlations of entangled states (thus often called EPR states) to define "elements of reality," a notion which according to them was missing in quantum theory. Elements of reality are deterministic predictions for a measurement result, which can be established without actually performing the measurement, and without physically disturbing the (sub)system to which they pertain. As elements of reality in the studied case were argued to exist necessarily even for pairs of noncommuting observables, they claimed they are contradicting the Heisenberg uncertainty relation.

The EPR paradox and with it the entanglement of quantum states remained a philosophical issue (Feynman, Leighton, and Sands, 1963), and seemed experimentally untestable for almost 30 years. The breakthrough happened when Bell (1964) derived his remarkable inequalities which revealed that two-particle correlations for the two spin- $\frac{1}{2}$  singlet disagree with any local realistic model. The pioneering "Bell experiment" was done by Freedman and Clauser (1972), followed by the famous ones by Aspect, Grangier, and Roger (1981, 1982) and Aspect, Dalibard, and Roger (1982) and many others. The early experiments used polarization-entangled photon pairs from atomic cascades (Clauser and Shimony, 1978). In late 1980s, parametric down-conversion was discovered as a convenient and robust method to produce entangled photons (see Sec. V).

A quarter of century after Bell's paper, it turned out that the conflict of local realism with quantum mechanics is even more striking for certain three or more particle entangled states. The Greenberger-Horne-Zeilinger (GHZ) theorem (Greenberger, Horne, and Zeilinger, 1989; Greenberger et al., 1990; Mermin, 1990a) showed that the concept of EPR's elements of reality is self-contradictory. That is, there are situations for which local realism and quantum mechanics make completely opposite predictions, even for perfectly correlated results, which were the starting point of the EPR argumentation. The GHZ paper showed that three or more particle interferometry is a rich untested area, full of exciting classically paradoxical phenomena. However, at that time no effective sources of three-photon or four-photon entanglement were present. Thus, a new chapter in experimental multiphoton quantum optics was opened, but had to wait for new ideas and experimental techniques.

# C. Sources of photonic entanglement

The standard source of entangled-photon pairs is nowadays the nonlinear optical process of spontaneous parametric down-conversion (SPDC) ([for a pioneering observation, see Burnham and Weinberg (1970)], the inverse of frequency doubling and up-conversion. In SPDC, photons from a pump laser beam, within a nonlinear crystal, can spontaneously be converted into pairs that are momentum and frequency entangled, and in the so-called type II process can also be polarization entangled (Kwiat et al., 1995). Today, SPDC sources of entangled-photon pairs of high quality and brightness can be routinely realized using various methods.

However, since the GHZ paper, and even more after the birth of quantum information, three or more photon entanglement was in demand. It turned out that using the primary two-photon entanglement, by a procedure which is called entanglement swapping, one can entangle without any direct interaction particles which were independent of each other or, what is more important for us, construct entanglement of higher order (Zukowski, et al., 1993). Since photons basically do not interact with each other, this method is of special importance for schemes aimed at creating multiphoton entanglements. Practical versions of this technique (Rarity, 1995; Zeilinger et al., 1997; Zukowski, Zeilinger,

and Weinfurter, 1995) are thus the basis of all experiments with three or more entangled photons, as well as of many realizations of quantum information protocols, up to measurement-based quantum computation.

# D. Applications in quantum information

Experimental quantum information processing was started right after new experimental techniques allowed one to control individual or compound quantum systems like atoms in traps, pairs of entangled photons, etc., and to observe a new set of classically impossible phenomena. As always, new controllable phenomena lead to new practical applications, especially in information transfer and processing. Quantum information processing harnesses the superposition principle and nonclassical correlations of quantum mechanics and employs them in communication and computation. In quantum cryptography [Bennett and Brassard (1984); Wiesner (1983); Ekert (1991); for a review see Gisin et al. (2002)] complementary measurements on quantum systems are used to establish a secret key shared by two partners, thus enabling for the first time a provably secure communication. Quantum teleportation (Bennett et al., 1993) enables a faithful transfer of an unknown quantum state from one location to another, using entangled states as a quantum channel. Quantum computers promise to greatly increase the efficiency of solving problems such as factoring large integers, database search, and simulation of some quantum phenomena.

Photons are the fastest information carrier, have a very weak coupling to the environment, and are thus best suited for quantum communication tasks. Thanks to this property, quantum key distribution with photons has now went long beyond the first few-meter laboratory demonstrations, to free-space or fiber-based distributions over  $100\mathrm{km}$  [see, e.g., Rosenberg et al. (2007) and Ursin et al. (2007)], and is rapidly commercialized into real life intercity cryptographic networks. To ultimately extend the range of quantum communication to a global scale, a collection of quantum toolkits still has to be developed. A quantum repeater (Briegel et al., 1998) would allow in principle an efficient long-distance high-fidelity transmission of entanglement. Several ingredients of this scheme have been already demonstrated: entanglement swapping (Pan et al., 1998), purification (Pan, Gasparoni, Ursin et al., 2003), quantum memory (Yuan et al., 2008), etc.

Despite the difficulty to "localize" photons, there has been a considerable interest in linear-optical quantum computing. This is motivated by the photon's robustness against decoherence and the relative ease with which it can be manipulated with high precision. Remarkably, by exploiting the nonlinearity induced by measurement, Knill, Laflamme, and Milburn (KLM) showed that scalable quantum computation is in principle possible with linear optics, single-photon sources, and detectors. A new and probably more practical approach is the concept of a "one-way quantum computer" (Raussendorf and Briegel, 2001; see Sec. VII.B.1). In this approach, one starts with the so-called "cluster states" (Briegel and Raussendorf, 2001). The computation algorithm is then performed by applying a sequence of one-qubit measurements. Optical quantum computing proposals (Browne and Rudolph, 2005) based on the one-way model reduce the computational

resource overhead by three orders of magnitudes compared to the KLM scheme. Cluster states up to six entangled photons have been realized (Kiesel, Schmid, Toth, et al., 2005; Walther, Resch, Rudolph et al., 2005; Lu et al., 2007), and applied to demonstrate elementary quantum gates and algorithms (Walther, Resch, Rudolph et al., 2005).

The rapid growth of literature on photonic realizations of quantum information processing still continues. One can expect much more exciting new developments.

# E. Related reviews

The earlier stages of the research of photonic entanglement have been reviewed in Clauser and Shimony (1978) Mandel and Wolf (1995), and Mandel (1999). They contain a collection of descriptions of experiments demonstrating the very nature of quantum mechanics. Because of a limit of space, we shall not discuss these experiments in this review. We start our description more or less at the stage of developments at which these earlier reviews ended. For detailed discussions on quantum entanglement, see Alber et al. (2001) and Horodecki et al. (2008). Reviews on Bell's theorem can be found in Laloë (2001), Werner and Wolf (2001a), and Genovese (2005). For an introduction to quantum information and quantum computation; see Bennett and DiVincenzo (2000), Preskill (1998), Nielsen and Chuang (2000), and Bouwmesster, Ekert, and Zeilinger (2001). Quantum cryptography has been reviewed by Gisin et al. (2002). Linearoptical quantum computing with photonic qubits has been reviewed by Kok et al. (2007), O'Brien (2007), O'Brien, Furasawa, and Vuckovic (2009), and Ralph and Pryde (2010). Weinfurter (2000) and Zeilinger et al. (2005) gave a concise review on experimental progress on photon interference and quantum information applications.

# F. Our aims

In this review, we describe the progress in the last two decades or so, both theoretical and experimental, in multiphoton interferometry, and its applications ranging from fundamental tests of quantum mechanics to photonic quantum information processing. Emphasis will be put on creation and control of photonic entanglement with linear optics and its application in quantum communication and computation. We limit the scope of our review to "few-photon" phenomena involving measurements of discrete observables, thus many fascinating experiments involving continuous variables will be not discussed here.

# II. INTERFERENCE AND QUANTUM ENTANGLEMENT

Classical interference is a macroscopic expression of the quantum one, i.e., the coherent or thermal states of the electromagnetic fields can also be described with Maxwell's laws. The interference phenomena in the quantum realm are richer and more pronounced. We discuss here the basic differences between the classical interference understood as interference of electromagnetic waves in space, and the quantum one which is interference of various operationally indistinguishable processes.

# A. Classical interference

In classical physics interference results from the superposition of waves. It may express itself in the form of intensity variations or intensity correlations.

Consider two quasimonochromatic plane waves linearly polarized in the same direction, described by

$$
E _ {j} (r, t) = E _ {j} e ^ {i \left[ \mathbf {k} _ {j} \cdot \mathbf {r} - \omega t - \phi_ {j} (t) \right]} + c. c. \tag {1}
$$

where  $E_{j}$  is the real amplitude of one of the fields,  $\mathbf{k}_j$  is the wave vector,  $\omega$  is the frequency of both waves,  $j = 1,2$  the index numbering the fields, and finally c.c. denotes the complex conjugate of the previous expression. The intensity of the superposed fields at a certain point in space is given by

$$
I (\mathbf {r}, t) = E _ {1} ^ {2} + E _ {2} ^ {2} + 2 E _ {1} E _ {2} \cos [ \Delta_ {1 2} \mathbf {k} \cdot \mathbf {r} - \Delta_ {1 2} \phi (t) ], \tag {2}
$$

where  $\Delta_{12}$  is the difference of the respective parameters for the two fields, e.g.,  $\Delta_{12}\phi(t) = \phi_1(t) - \phi_2(t)$ . For  $\Delta_{12}\phi(t)$  constant in time, or of values varying much less than  $\pi$ , this formula (after averaging over time) describes a Young-type interference pattern. In the opposite case, of widely fluctuating  $\Delta_{12}\phi(t)$  no interference can be observed because the pattern is washed out. In the case of  $E_1 = E_2$ , one has maximal possible interference. This can be quantified in terms of the interferometric contrast, or visibility,  $V = (I_{\mathrm{max}} - I_{\mathrm{min}}) / (I_{\mathrm{max}} + I_{\mathrm{min}})$ , which in the aforementioned case equals 1.

The Hanbury-Brown and Twiss experiment introduced intensity correlation measurements to optics. Such correlations between two points in space and two moments of time, for two classical fields, are described by an intensity correlation function

$$
G ^ {(2)} \left(\mathbf {r} _ {1}, t _ {1}; \mathbf {r} _ {2}, t _ {2}\right) = \langle I \left(\mathbf {r} _ {1}, t _ {1}\right) I \left(\mathbf {r} _ {2}, t _ {2}\right) \rangle_ {a v}. \tag {3}
$$

The average is taken over an ensemble, and for stationary fields this is equivalent to the temporal average. Even when no intensity variations are observable (i.e., for averaged intensity constant in space), the intensity correlations can reveal interference effects. Assume that the phases of the two fields fluctuate independently of one another. Then for  $t_1 = t_2$ , the  $G^{(2)}$  function still exhibits a spatial modulation or maximal visibility of  $50\%$  as exhibited by

$$
G ^ {(2)} \left(\mathbf {r} _ {1}, t; \mathbf {r} _ {2}, t\right) = \left(I _ {1} + I _ {2}\right) ^ {2} + 2 I _ {1} I _ {2} \cos \left[ \left(\Delta_ {1 2} \mathbf {k}\right) \left(\mathbf {r} _ {1} - \mathbf {r} _ {2}\right) \right], \tag {4}
$$

where  $I_{i} = E_{i}^{2}, i = 1, 2$ . This formula can be easily reached by noting that the temporal average of

$$
\cos [ \alpha + \Delta_ {1 2} \phi (t) ] \cos [ \alpha^ {\prime} + \Delta_ {1 2} \phi (t) ], \tag {5}
$$

where  $\Delta_{12}\phi (t) = \phi_1(t) - \phi_2(t)$  is given by

$$
\begin{array}{l} \cos \alpha \cos \alpha^ {\prime} \langle \cos^ {2} \Delta_ {1 2} \phi (t) \rangle_ {a v} + \sin \alpha \sin \alpha^ {\prime} \langle \sin^ {2} \Delta_ {1 2} \phi (t) \rangle_ {a v} \\ - \frac {1}{2} \sin \left(\alpha + \alpha^ {\prime}\right) \langle \sin 2 \Delta_ {1 2} \phi (t) \rangle_ {a v}, \tag {6} \\ \end{array}
$$

and due to the random nature of  $\Delta_{12}\phi (t)$  only the first two terms survive because both  $\langle \cos^2\Delta_{12}\phi (t)\rangle_{av}$  and  $\langle \sin^2\Delta_{12}\phi (t)\rangle_{av}$  give  $\frac{1}{2}$ , whereas  $\langle \sin 2\Delta_{12}\phi (t)\rangle_{av} = 0$

In addition to the phase fluctuations, one can also take into account amplitude fluctuations. Nevertheless, the basic features of the earlier formula must be retained. Amplitude fluctuations tend to lower the visibility of the intensity correlations patterns even further. Thus, the visibility of intensity correlations for fields with fluctuating phase differences is never full, maximally  $50\%$ . As we shall see, there is no bound on visibility in the quantum case. For a broader treatment of these matters, see Paul (1986) and Belinskii and Klyshko (1993).

# B. Quantum interference

Quantum interference rests on the concept of superposition of probability amplitudes of processes that contribute to the given phenomenon.

# 1. Single-particle quantum interference

Single-particle interference looks almost identical to the classical one. We replace the fields (waves) by amplitudes  $A(\mathbf{x},t)$ , which differ only by the fact that they must be suitably normalized, if one wants to compute the probabilities. Suppose that the (not normalized) amplitude to detect a photon at  $\mathbf{x}$  is given by

$$
A _ {\mathbf {b} _ {1}} (\mathbf {x}, t) = e ^ {i \left[ \mathbf {k} _ {1} \cdot (\mathbf {x} - \mathbf {b} _ {1}) + \Phi_ {\mathbf {x}, \mathbf {b} _ {1}} (t) \right]} \tag {7}
$$

if it originates from point  $\mathbf{b}_1$ , and by

$$
A _ {\mathbf {b} _ {2}} (\mathbf {x}, t) = e ^ {i \left[ \mathbf {k} _ {1} ^ {\prime} \cdot (\mathbf {x} - \mathbf {b} _ {2}) + \Phi_ {\mathbf {x}, \mathbf {b} _ {2}} (t) \right]} \tag {8}
$$

if it originates from  $\mathbf{b}_2$ . The quantum mechanical probability density that a particle is detected at  $\mathbf{x}$  is given by

$$
\begin{array}{l} P (\mathbf {x}, t) \sim | A _ {\mathbf {b} _ {1}} (\mathbf {x}, t) + A _ {\mathbf {b} _ {2}} (\mathbf {x}, t) | ^ {2} \\ \sim 1 + \cos \left[ \Delta \mathbf {k} _ {1} \cdot \mathbf {x} + \Phi_ {0} + \Phi_ {\mathbf {x}, \mathbf {b} _ {1}} (t) - \Phi_ {\mathbf {x}, \mathbf {b} _ {2}} (t) \right], \tag {9} \\ \end{array}
$$

where  $\Delta \mathbf{k}_1 = \mathbf{k}_1 - \mathbf{k}_1'$ , and  $\Phi_0$  is an irrelevant constant phase. Thus if the phase difference  $\Phi_{\mathbf{x},\mathbf{b}_1}(t) - \Phi_{\mathbf{x},\mathbf{b}_2}(t)$  is stable, one can have the Young-type interference patterns of up to  $100\%$  visibility. Such a stable phase difference can be observed with single photons in, e.g., a double-slit experiment. Also, in the case of a classical wave description and classical-like fields the observed intensity is proportional to the probability density  $P(\mathbf{x},t)$ , that is in this respect nothing changes.

Nevertheless, the above description differs drastically from the classical particle picture, in which one would expect that a process originating with state  $A$  and with possible intermediate stages  $B_{1},\ldots B_{N}$ , leading to an event  $C$ , would be described by

$$
P (C | A) = \sum_ {j = 1} ^ {N} P (C | B _ {j}) P (B _ {j} | A). \tag {10}
$$

In the quantum case  $P(C|A) = |\langle C|A\rangle |^2$ , where

$$
\langle C | A \rangle = \sum_ {j = 1} ^ {N} \langle C | B _ {j} \rangle \langle B _ {j} | A \rangle , \tag {11}
$$

this means one sums over amplitudes not probabilities. For a double slit, we have  $N = 2$ , and  $\langle A|B_1\rangle \approx \langle A|B_2\rangle$  give the amplitudes to reach the slits. Finally, one has  $\langle C|B_j\rangle = A_{\mathbf{b}_j}$ . Please note that for classical particles the terms of the summation  $P(C|B_j)$  etc., are real numbers, while in the quantum case the amplitudes  $\langle C|B_j\rangle$  are complex numbers. Thanks to that interference effects can be predicted.

The difference between Eqs. (10) and (11) is in the assumption, inherent in Eq. (10), that the particle had to be in one of the intermediate situations (states)  $B_{i}$ . In the quantum case any attempt to verify by measurement which of the situations actually took place puts one back to the classical formula (10). The formula (11) leads to interference phenomena, and may be thought as a manifestation of a wave nature of quantum particles, whereas, if we make measurements discriminating events  $B_{i}$ , we learn by which way (welcher weg) the particles travel. The "which-way information" is a clear signature of the particle nature.

# 2. Two-particle quantum interference

All this becomes much more puzzling once we consider a two-particle experiment. Already Einstein, Podolsky, and Rosen (1935) pointed out some strange features of such a case. Schrödinger (1935a) noticed that these features are associated with what he called "entangled states," which will be discussed in detail later. Consider now these as superpositions of fully distinguishable products of single-particle states, i.e., that there is a specific pair of local measurements for which the results of the respective measurements on the two subsystems are perfectly correlated (a result of a measurement on one subsystem reveals the unique value of the corresponding observable for the second subsystem).

Consider such a correlation: assume that if particle 1 is at  $b_{1}$ , then particle 2 is also at  $b_{1}$ , and whenever 1 is at  $b_{2}$  then particle 2 is at  $b_{2}$ . Later on the particles are detected at two different points,  $\mathbf{x}_{1}$  and  $\mathbf{x}_{2}$ . Then, according to the rules given above

$$
\begin{array}{l} P (\mathbf {x} _ {1}, \mathbf {x} _ {2}, t) \sim | A _ {b _ {1}} (\mathbf {x} _ {1}, t) A _ {b _ {1}} (\mathbf {x} _ {2}, t) + A _ {b _ {2}} (\mathbf {x} _ {1}, t) A _ {b _ {2}} (\mathbf {x} _ {2}, t) | ^ {2} \\ \sim 1 + \cos \left(\Delta \mathbf {k} _ {1} \cdot \mathbf {x} _ {1} + \Delta \mathbf {k} _ {2} \cdot \mathbf {x} _ {2} + \Delta \Phi_ {b _ {1}, b _ {2}}\right), \tag {12} \\ \end{array}
$$

with

$$
\Delta \Phi_ {b _ {1}, b _ {2}} = \Delta \Phi_ {\mathbf {x} _ {1}, b} (t) + \Delta \Phi_ {\mathbf {x} _ {2}, b} (t) + \Phi_ {o} ^ {\prime}, \tag {13}
$$

where the amplitudes for the second particle are given by formulas (7) and (8), with  $\mathbf{x}_2$  replacing  $\mathbf{x}_1$  and  $\mathbf{k}_2$  replacing  $\mathbf{k}_1$ , and  $\Delta \Phi_{\mathbf{x}_i,b}(t) = \Phi_{\mathbf{x}_i,b_1}(t) - \Phi_{\mathbf{x}_i,b_2}(t)$ , with  $i = 1,2$ . Thus, if the phase relation between the two amplitudes is stable, one can have absolutely noiseless interference with  $100\%$  visibility, while there is no single-particle interference

$$
P \left(\mathbf {x} _ {1}, t\right) = \int d \mathbf {x} _ {2} P \left(\mathbf {x} _ {1}, \mathbf {x} _ {2}, t\right) = \text {c o n s t .} \tag {14}
$$

As we shall see, the unbounded visibility is not the only feature by which two-particle interference differs from the classical one.

# C. Quantum entanglement

Entanglement according to Schrödinger (1935a, 1935b, 1935c, 1935d) contains "the essence of quantum mechanics." Consider a spin-0 particle which decays into two spin-  $1 / 2$  particles (Bohm, 1951). The quantum state is such that along any chosen direction, say the  $z$  axis, the spin of particle 1 when measured can be either up or down, which in turn, by angular momentum conservation, implies that for particle 2 it is, respectively, down or up. The state of the two spins is the rotationally invariant singlet

$$
| \psi \rangle_ {1 2} = \frac {1}{\sqrt {2}} (| \uparrow \rangle_ {1} | \downarrow \rangle_ {2} - | \downarrow \rangle_ {1} | \uparrow \rangle_ {2}), \tag {15}
$$

where  $|\uparrow \rangle_{1}(|\downarrow \rangle_{1})$  describes the state of particle 1 with its spin up (down) along the  $z$  direction. The minus sign is necessary to get the rotational invariance. The state describes a coherent superposition of the two product states: there is no information in the whole Universe on which of the two possibilities will be detected at the measurement stage. None of those two possibilities is the actual case. Actualization can happen only via a measurement. This superposition, like any other, e.g., in the double-slit experiment, survives as long as no measurement actualizing one of those possibilities is performed, and any possible interaction of the particles with an environment does not destroy it. While none of the two possibilities actually can be assigned without measurement, both of them affect the predictions for all measurements. Another property of the state (15) is that it does not make any prediction about the result of spin measurement on only one of the two particles: the result is random. The spin state of one of the particles is described by a reduced density operator, which is a totally random state  $\frac{1}{2} I_k$ , where  $k = 1, 2$  is indexing the subsystems, and  $I_k = |\uparrow \rangle_{kk}\langle \uparrow | + |\downarrow \rangle_{kk}\langle \downarrow |$  is the unit operator for a given subsystem. All information contained in the state in Eq. (15) defines only joint properties (Schrodinger, 1935d). The joint property can be put as follows: the two spins, if measured with respect to the same direction, will be found opposite. As a matter of fact, this

property for any pair of complementary measurement settings fully defines the singlet state.

Imagine that the two particles can be separated far apart, one in Alice's laboratory and the other one in Bob's. As soon as Alice measures the value of a spin projection along some axis, new information is gained, and for her the state of Bob's particle is a well-defined pure one. This is independent of the spatial separation between them. Thus a state like Eq. (15) is a perfect case to study (and to reveal) the EPR paradox.<sup>7</sup> Basically, all earlier studies of entanglement concentrated on entangled states of spins 1/2 or photonic polarizations; for a review, see Clauser and Shimony (1978). Much later, we saw an emergence of research on entanglement of three or more particles, practically together with the advent of quantum information.

Theoretical methods for entanglement analysis: The most important tool for the analysis of pure states of two subsystems is the so-called Schmidt decomposition. For any pure state  $|\Psi \rangle$  of a pair of subsystems, one described by a Hilbert space of dimension  $N$ , the other by a space of dimension  $M$ , say  $N \leq M$ , one can find preferred bases, one for the first system, the other one for the second, such that the state is a sum of bi-orthogonal terms, i.e.,

$$
| \Psi \rangle = \sum_ {i = 1} ^ {N} r _ {i} | a _ {i} \rangle_ {1} | b _ {i} \rangle_ {2} \tag {16}
$$

with  $n\langle x_i|x_j\rangle_n = \delta_{ij}$ , for  $x = a$ ,  $b$  and  $n = 1, 2$ . The coefficients  $r_i$  are real and positive. The appropriate single subsystem bases, here  $|a_i\rangle_1$  and  $|b_j\rangle_2$ , depend upon the state. A proof of the Schmidt decomposition can be found in Peres (2002). A generalization of the Schmidt decomposition to more than two subsystems is not straightforward; see, e.g., Carteret, Higuchi, and Sudbery (2000). It is easy to show that the two reduced density matrices of Eq. (16) are endowed with the same spectrum. This does not hold for three or more particle subsystems.

$^{7}$ Following Bohm (1951), one could apply the EPR reality criterion to the singlet state (15): "If, without in any way disturbing a system, we can predict with certainty (i.e., with probability equal to unity) the value of a physical quantity, then there exists an element of physical reality corresponding to this physical quantity." This would imply that to any possible spin measurement on any one of our particles we can assign such an element of physical reality on the basis of a corresponding measurement on the other particle. Whether or not we can assign an element of reality to a specific spin component of one of the systems must be independent of which measurement we actually perform on the other system and even independent of whether we care to perform any measurement at all on that system. This approach was shown to be leading to a class of theories incompatible with quantum mechanics (Bell, 1964). The concept of elements of reality was shown to be strictly self-contradictory via the GHZ theorem (see further on).

The crux of the proof is that the greatest of the coefficients is given by  $\mathrm{Max}_{|a\rangle_1|b\rangle_2}|\langle\Psi|a\rangle_1|b\rangle_2|$  and after finding it and the states that give the maximization, say  $|a_1\rangle_1$  and  $|b_1\rangle_2$ , one searches for the second greatest coefficient by performing maximization over the linear subspace to which  $|a_1\rangle_1$  and  $|b_1\rangle_2$  do not belong. This is recursively continued to get next coefficients and basis states, till the procedure halts.

Every pure state of two spins  $1/2$  can be put into the following form:

$$
\cos \alpha | \uparrow \rangle_ {1} | \uparrow \rangle_ {2} + \sin \alpha | \downarrow \rangle_ {1} | \downarrow \rangle_ {2},
$$

where the states  $|\uparrow \rangle_{n}$  and  $|\downarrow \rangle_{n}$ ,  $n = 1,2$ , are the eigenstates of the  $\mathbf{z}^{(\mathbf{n})}\cdot \sigma^{(n)}$  operator. The unit vectors  $\mathbf{z}^{(\mathbf{n})}$  are individually defined for each of the observers' particles. They define the basis for the Schmidt decomposition for each of the subsystems.

The theory of entanglement of mixed states is more complicated. A state (pure or mixed) described by a density matrix  $\rho_{AB}$  of a composite quantum system consisting of two subsystems  $A$  and  $B$  is separable if and only if  $\rho_{AB}$  is a convex combination of products density matrices  $\rho_A^\lambda$  and  $\rho_B^\lambda$  of the two subsystems, namely,  $\rho_{AB} = \sum_{\lambda}p_{\lambda}\rho_{A}^{\lambda}\otimes \rho_{B}^{\lambda}$ , where  $p_{\lambda}\geq 0$  and  $\sum_{\lambda}p_{\lambda} = 1$ . Otherwise,  $\rho_{AB}$  is entangled (Werner, 1989). For composite systems of more than two subsystems this definition can be generalized in a straightforward way.

Basic structural criteria, which decide whether a given density operator represents an entangled state, were first given by Peres (1996) and in the full form by Horodecki, Horodecki, and Horodecki (1996). The full set of separable mixed states is a bounded convex set in a multidimensional real space of Hermitian operators. Thus, any entangled state is separated from the set of separable states by a hyperplane. The equation of such a hyperplane is defined by an element of the space, namely, a Hermitian operator  $\hat{W}$ , which is called an "entanglement witness" (Horodecki, Horodecki, and Horodecki, 1996; Lewenstein et al., 2000; Terhal, 2000; Bruß et al., 2002; Bourennane, Eibl, Kurtsiefer, et al., 2004). Since the scalar product in the operator space is given by  $\mathrm{Tr}(\hat{A}^{\dagger}\hat{B})$ , the equation of a hyperplane in the space is given by  $\mathrm{Tr}(\hat{W}\varrho) = \mathrm{const}$ . A Hermitian operator  $\hat{W}$  is an entanglement witness if for all separable states one has  $\mathrm{Tr}(\hat{W}\varrho_{\mathrm{sep}})\geq 0$ , whereas there exists an entangled state for which one has  $\mathrm{Tr}(\hat{W}\varrho_{\mathrm{ent}}) < 0$ . Thus, via measurement of a suitably chosen witness operator, one can detect entanglement.

The original idea of Peres was the observation that positivity of a partial transposition (PPT) of a density matrix (i.e., its transposition for just one subsystem) is a necessary condition for a state to be separable. This was extended by the Horodecki family to a fully general necessary and sufficient condition for separability, which is that a density matrix after any positive transformation (map) on one of the subsystems should remain a density operator. The spin offs of such considerations are measures of entanglement via the negativity of the eigenvalues of a partial transpose of the density matrix, etc. Other methods that give a quantitative measure of the degree of entanglement of bipartite entangled states include the entanglement of formation (Bennett, DiVincenzo, Smolin, and Wootters, 1996; Wootters, 1998a), concurrence (Hill and Wootters, 1997), and tangle (Wootters, 1998b; Coffman, Kundu, and Wootters, 2000). For more

![](images/8a079595ad5ffe68830691431866e81f9e7d3d7312ca9dfff517c75676a58701.jpg)  
FIG. 1. A two-photon interferometer with variable phase shifts  $\phi_{1}$  and  $\phi_{2}$ . Before being combined at the 50:50 beam splitter (BS) and then subject to single-photon detections, the two paths of each photon acquire a relative phase shift. For experimental realization of such a two-photon interferometer, see Fig. 11. Adapted from Horne, Shimony, and Zeilinger, 1989.

details on the entanglement theory, see Alber et al. (2001), Mintert et al. (2005), Gühne and Toth (2009), and Horodecki et al. (2008).

An interesting feature of the theory of entanglement of mixed states is that for two three-dimensional systems, or for more complicated ones, one can find states which are entangled, but from which no maximally entangled state can be distilled $^{10}$  (Horodecki, Horodecki, and Horodecki, 1998). Such states are called bound entangled.

# D. Interferometry with entangled two-photon and multiphoton states

Entanglement can manifest itself in strictly quantum interference phenomena, that is, these phenomena can neither be explained by a classical wave nor by a classical particle picture. To show this, below we present the basics of multi-particle interferometry.

# 1. EPR interferometry

Recall that in a single-particle interferometer, as in Young's double-slit experiment, the interference pattern appears only if the particle's two paths are indistinguishable. However, for interferometers involving two or more particles, dramatically new features arise. Figure 1 is a sketch of the generalization of the concept of a Mach-Zehnder interferometer to two-photon interferometry (Horne and Zeilinger, 1986; Zukowski and Pykacz, 1988; Horne, Shimony, and Zeilinger, 1989; Horne, Shimony, and Zeilinger, 1990; rarity and Tapster, 1990; Greenberger, Horne, and Zeilinger, 1993). We assume that a central source emits two photons in an entangled state

$$
| \psi \rangle_ {1 2} = \frac {1}{\sqrt {2}} (| a \rangle_ {1} | a ^ {\prime} \rangle_ {2} + | b \rangle_ {1} | b ^ {\prime} \rangle_ {2}). \tag {17}
$$

Here  $|a\rangle$  and  $|b\rangle (|a^{\prime}\rangle$  and  $|b^{\prime}\rangle$ ) are two different spatial modes of photon 1 (photon 2). The entanglement of  $|\psi \rangle_{12}$  is actually called momentum entanglement (Horne and Zeilinger, 1986;

Rarity and Tapster, 1990), whose creation will be described in Sec. IV. Before being combined at a 50:50 beam splitter (BS) and then subject to single-photon detections, the two paths of each photon acquire a relative phase shift.

By taking into account the phase shifts  $\phi_{1}$  and  $\phi_{2}$  and the action of the two beam splitters, the probabilities of the coincidence detections of two photons at the detector pairs  $(\mathrm{D}_{1c / d},\mathrm{D}_{2c / d})$  read

$$
\begin{array}{l} p _ {1 c, 2 d} \left(\phi_ {1}, \phi_ {2}\right) = p _ {1 d, 2 c} \left(\phi_ {1}, \phi_ {2}\right) \\ = \frac {1}{4} [ 1 + \cos (\phi_ {1} - \phi_ {2}) ], \\ \end{array}
$$

$$
p _ {1 c, 2 c} \left(\phi_ {1}, \phi_ {2}\right) = p _ {1 d, 2 d} \left(\alpha , \phi_ {2}\right) = \frac {1}{4} \left[ 1 - \cos \left(\phi_ {1} - \phi_ {2}\right) \right]. \tag {18}
$$

Thus, by simultaneously monitoring the detectors on both sides of the interferometer, while varying the phase shifts  $\phi_{1}$  and  $\phi_{2}$ , the interference fringes will be observed as shown by the sinusoidal terms. In contrast, for any single detector the count rate shows no interference at all. For example,  $p_{1c} = p_{1c,2c}(\phi_1,\phi_2) + p_{1c,2d}(\phi_1,\phi_2) = \frac{1}{2}$ , independent of  $\phi_{1}$  and  $\phi_{2}$ .

# 2. Greenberger Horne Zeilinger interferometry

After many years of studying only two-particle entanglements, in 1989 a generalization of the EPR interferometry to three photons was proposed [Greenberger, Horne, and Zeilinger (1989), later refereed to as GHZ]. The most elementary case is shown in Fig. 2. Though such a step from 2 to 3 seems to be small, it nevertheless leads to profound implications, one of which is the GHZ theorem (Greenberger, Horne, and Zeilinger, 1989; Greenberger et al., 1990; Mermin, 1990a).

At the center of the interferometer is a source emitting three photons in a so-called GHZ-entangled state

$$
\left| \mathrm {G H Z} \right\rangle_ {1 2 3} = \frac {1}{\sqrt {2}} \left(\left| a \right\rangle_ {1} \left| a ^ {\prime} \right\rangle_ {2} \left| a ^ {\prime \prime} \right\rangle_ {3} + \left| b \right\rangle_ {1} \left| b ^ {\prime} \right\rangle_ {2} \left| b ^ {\prime \prime} \right\rangle_ {3}\right). \tag {19}
$$

Here each photon has two different spatial modes, which are for photon 1  $|a\rangle$  and  $|b\rangle$ . By taking into account the actions of the relative phase shifts and the 50:50 beam splitters (for their

![](images/9f32e2b4f02a21bfbfaef4e7f11ad0635bf494617e3ac81f4f7b90b914e3af3b.jpg)  
FIG. 2. A three-photon interferometer with variable phase shifts  $\phi_{1}$ ,  $\phi_{2}$ , and  $\phi_{3}$ . Adapted from Greenberger, Horne, and Zeilinger, 1989.

properties see Sec.II.E), one can deduce novel features of three-particle interference (Greenberger et al., 1990). First, the respective threefold coincidence detection probability for the output modes  $[(1c,2c,3c),(1d,2d,3d),$  etc.] reads

$$
\begin{array}{l} p _ {1 c, 2 c, 3 c} \left(\phi_ {1}, \phi_ {2}, \phi_ {3}\right) = \frac {1}{8} \left[ 1 + \sin \left(\phi_ {1} + \phi_ {2} + \phi_ {3}\right) \right], \\ p _ {1 d, 2 c, 3 c} \left(\phi_ {1}, \phi_ {2}, \phi_ {3}\right) = \frac {1}{8} \left[ 1 - \sin \left(\phi_ {1} + \phi_ {2} + \phi_ {3}\right) \right], \text {e t c .} \tag {20} \\ \end{array}
$$

The threefold coincidence rates given in Eq. (20) display sinusoidal oscillations depending on the sum  $\phi_1 + \phi_2 + \phi_3$ . Second, this three-particle interferometer does not exhibit any two-particle fringes. For example, if only two-particle coincidences  $2c - 3c$  are detected, while the modes  $1c$  and  $1d$  are ignored, the observed rate will be constant  $p_{1c,2c,3c}(\phi_1,\phi_2,\phi_3) + p_{1d,2c,3c}(\phi_1,\phi_2,\phi_3) = \frac{1}{4}$ , and completely independent of the phases.[11] Finally, a similar argument shows that, of course, no single-particle fringes can be observed. Actually, an  $n$ -particle interferometer generalized along the above reasoning will only exhibit  $n$ -particle fringes, but no  $(n - 1) - ,(n - 2) - ,\ldots$ , single-particle fringes (Greenberger et al., 1990).

The above two-photon and three-photon interferometry was described using the photon's path degrees of freedom. However, similar interference effects can be observed using any of the photon's degrees of freedom, e.g., polarization. Moreover, the above argument should be understood as a special case of a wider concept indicating that entangled massive particles (e.g., electrons and atoms) could also display multiparticle interference.

# E. Interferometry with multiport beam splitters

Novel interferometric effects can be obtained with  $N$ -port beam splitters, which are devices which split light into more than two output beams [for a general theory of such devices, see Reck et al. (1994)]. Such devices can be utilized in multiparticle interferometry (Zeilinger et al., 1993). With current technology, such experiments are becoming feasible.

# III. PHOTONIC QUBITS AND LINEAR OPTICS

The possibility of performing quantum information-processing tasks with photons is based on the fact that quantum information can be encoded in quantum states of certain degrees of freedom (e.g., polarizations) of individual photons, and that individual photons can be manipulated either by simple optical elements (e.g., wave plates and interferometers) or by letting them interact with matter (trapped ions, atoms, etc.) at an atom-photon interface. Here we show to what extent a photon can carry a qubit, and the simplest elements that are used to manipulate it. To this end, we begin with a formal definition of photons and their quantum states.

The formal theory of quantization of electromagnetic fields was formulated by Dirac (1927). Here we only give its basic mathematical devices for completeness; for detailed treat-

ment, see standard textbooks on quantum optics, e.g., Walls and Milburn (1994), Mandel and Wolf (1995), Scully and Zubairy (1997), and especially Bialynicki-Birula and Bialynicka-Birula (1975).

A single-photon pure state can be characterized by a specific wave packet profile  $g_{\lambda \mathbf{k}}$ , i.e., by the quantum amplitudes for a given momentum  $\mathbf{k}$  and polarization  $\lambda$ . According to the Born rule,  $|g_{\lambda \mathbf{k}}|^2$  gives the probability density of having the single photon with the momentum  $\hbar \mathbf{k}$  and polarization  $\lambda$ . Thus, one has  $\sum_{\lambda = 1,2}\int d\mathbf{k}|g_{\lambda \mathbf{k}}|^2 = 1$ . The wave packet profiles are vectors in a Hilbert space with a scalar product given by

$$
\langle g | h \rangle = \sum_ {\lambda = 1, 2} \int d \mathbf {k} g _ {\lambda \mathbf {k}} ^ {*} h _ {\lambda \mathbf {k}}. \tag {21}
$$

One can introduce an arbitrary orthonormal basis  $g_{\lambda \mathbf{k}}^l$  where  $l$  are natural numbers and  $\langle g^n |g^m\rangle = \delta_{nm}$ . Two different orthonormal bases, to be denoted, respectively, as primed and unprimed, are related by a unitary operation:  $g^{lm} = \sum_{l = 1}^{\infty}U_{ml}g^{l}$ . The complex numbers  $U_{lm}$  satisfy  $\sum_{l = 1}^{\infty}U_{ml}U_{kl}^{*} = \sum_{l = 1}^{\infty}U_{lm}^{*}U_{lk} = \delta_{mk}$ . One can choose a specific basis of the wave packet profiles of the single photon, say  $g^{l}$ , and with each element of such a basis one associates a quantum oscillatorlike construction to introduce number states, namely, the Fock states. One introduces the vacuum state  $|\Omega \rangle \equiv |0,0,0,\ldots \rangle$ , the state with no photons at all for any modes. Next, for a chosen basis one associates a pair of operators satisfying the usual relations for creation and annihilation operators, namely,  $[\hat{a}_l,\hat{a}_l^\dagger ] = 1$  and requires that for all  $l$ $\hat{a}_l|\Omega \rangle = 0$ . Using the standard oscillator algebra, one constructs states like  $(\hat{a}_l^{\dagger n_l} / \sqrt{n_l!})|\Omega \rangle$ , which is a state of the electromagnetic field in which one has  $n_l$  identical photons of the same wave packet profile  $g^{l}$ , and no other photons whatsoever. This is denoted by  $|0,\dots ,0,n_l,0,0,\dots \rangle$ . Finally, one assumes that  $[\hat{a}_n,\hat{a}_m] = 0$  and  $[\hat{a}_n,\hat{a}_m^\dagger ] = \delta_{nm}$ , that is, creation and annihilation operators of photons with orthogonal wave packet profiles always commute. A general (normalized) basis state of the Fock space is therefore of the following form:

$$
\left| n _ {1}, n _ {2}, n _ {3}, \dots \right\rangle = \prod_ {l = 1} ^ {\infty} \frac {\hat {a} _ {l} ^ {\dagger n _ {l}}}{\sqrt {n !}} | \Omega \rangle . \tag {22}
$$

All vectors of the Fock space are linear combinations of the above basis states, which have a finite total number of photons. It is easy to see that if one defines the creation operators with respect to an alternative basis of wave packet profiles (here the primed ones), one has

$$
\hat {a} _ {m} ^ {\prime \dagger} = \sum_ {n = 1} ^ {\infty} U _ {m n} \hat {a} _ {n} ^ {\dagger}. \tag {23}
$$

The vacuum state is invariant with respect to such transformation, i.e., one still has  $\hat{a}_m^\prime |\Omega \rangle = 0$ . For more details, see Bialynicki-Birula and Bialynicka-Birula (1975).

# A. Photonic qubits

A quantum bit, or qubit is the most elementary unit of quantum information. It is a generalization of the classical bit, which has two distinguishable states "0" and "1." Similarly,

we can have a qubit in two distinguishable, i.e., orthogonal states  $|0\rangle$  and  $|1\rangle$ . However, in contradistinction to its classical counterpart, a qubit can be prepared as, or transformed to any superposition of these two states (normalization requires  $\alpha_0^2 + \alpha_1^2 = 1$ )

$$
| \Psi_ {\text {q u b i t}} \rangle = \alpha_ {0} | 0 \rangle + \alpha_ {1} | 1 \rangle . \tag {24}
$$

Any isolated two-level system consisting of a pair of orthogonal quantum states represents a qubit. Photons, massless spin 1 particles, have only two eigenvalues of their spin along the direction of their propagation (wave vector),  $\pm \hbar$ . These two spin values correspond to right-handed and left-handed circular polarization. Thus this property makes the photon an ideal candidate for a qubit. However, there are other degrees of freedom of a photon that can be used to encode qubit information.

Polarization qubits. The most commonly used photonic qubits are realized using polarization. In this case, arbitrary qubit states can be  $\alpha_0|H\rangle +\alpha_1|V\rangle$  , where  $H$  and  $V$  stand for horizontal and vertical polarizations, respectively. The advantage of using polarization qubits stems from the fact that they can easily be created and manipulated with high precision by simple linear-optical elements such as polarizing beam splitters (PBS), polarizers, and wave plates. Photon polarization states and spin states of a spin  $1 / 2$  particle are perfect qubits given by nature, no human invention is required.

Spatial qubits-A single photon can also appear in two different spatial modes or paths  $a$  and  $b$ : the general state reads  $\alpha_0|a\rangle +\alpha_1|b\rangle$ . This may occur if a single photon exits a BS, with two output modes  $a$  and  $b$ . Any state of spatial qubits can be prepared by using suitable phase shifters and BS. A disadvantage of using spatial qubits is that the coherence between  $|a\rangle$  and  $|b\rangle$  is sensitive to the relative phase between the paths  $a$  and  $b$ , and this is difficult to control in long-distance cases.

Time-bin qubits-For a more robust long-distance transmission of quantum information, one may use time-bin qubits. The computational basis $^{12}$  consists of two states which are of the same spectral shape, but time shifted by much more than the coherence time. $^{13}$  Time-bin qubits can be realized by sending a single photon through an unbalanced Mach-Zehnder interferometer. Its wave packet is split by the first BS, with transmission coefficient  $T = |\alpha_0|^2$  and reflection coefficient  $R = |\alpha_{1}|^{2}$  into two coherent parts. The transmitted one propagates along the short arm, and the reflected one along the long arm. If the wave packet extension is shorter than the arm length difference, the output from the ports of the second, 50:50 BS is two wave packets well separated in time. If no photon is registered in, say output port I, in the other output one has a single photon in a coherent superposition of two time-bin states  $\alpha_0|\mathrm{early}\rangle +\alpha_1|\mathrm{late}\rangle$ . The phase relation can be controlled with a phase shifter in one of the

arms of the interferometer. For more details, see Bennett (1992) and Gisin et al. (2002).

While in this review we are mainly concerned with the above three implementations of photonic qubits, one should keep in mind that other implementations are possible. Frequency qubits have first been implemented in quantum cryptography (Sun, Mazurenko, and Fainman, 1995; Mazurenko, Giust, and Goedgebuer, 1997) and also more recently in entangled atom-photon systems (Madsen et al., 2006).

Quantum  $d$ -level (high-dimensional) systems ("audit") can also be realized using, e.g., orbital angular momentum states of photons (Mair et al., 2001), or using simultaneously two or more degrees of freedom listed above. For instance, for the latter case a polarized single photon in a coherent superposition of two spatial modes can be thought of as a quantum system in a four-dimensional Hilbert space (Boschi et al., 1997; Michler, Weinfurter, and Zukowski, 2000; Chen et al., 2003; Kim, 2003).

Two-photon polarization-entangled states-The so-called Bell states14 form a basis in the four-dimensional two-qubit Hilbert space. Bell states of photonic polarization qubits can be, for example,

$$
\left| \psi^ {\pm} \right\rangle_ {1 2} = \frac {1}{\sqrt {2}} \left(\left| H \right\rangle_ {1} \left| V \right\rangle_ {2} \pm \left| V \right\rangle_ {1} \left| H \right\rangle_ {2}\right), \tag {25}
$$

$$
\left| \phi^ {\pm} \right\rangle_ {1 2} = \frac {1}{\sqrt {2}} \left(\left| H \right\rangle_ {1} \left| H \right\rangle_ {2} \pm \left| V \right\rangle_ {1} \left| V \right\rangle_ {2}\right). \tag {26}
$$

As we shall see, such entangled states serve as a central physical resource in various quantum information protocols like quantum cryptography, quantum teleportation, entanglement swapping, and in tests aimed at excluding hidden-variable models of quantum mechanics.

# B. Simple linear-optical elements

In the photonic domain, quantum states of photons can be easily, and with high precision, manipulated by simple passive linear-optical devices. These linear-optical elements include BSs, PBSs, wave plates, and phase shifters. Classically, such devices conserve energy: The total input energy equals the total output energy, and there is no energy transfer between different frequencies. A passive linear-optical device is described by a unitary transformation of annihilation operators for the same frequency

$$
\hat {a} _ {m} ^ {\text {o u t}} = \sum_ {m} U _ {m n} \hat {a} _ {n} ^ {\text {i n}}, \tag {27}
$$

where  $U$  is a unitary matrix, and the indices denote a basis of orthogonal modes.

The BS is one of the most important optical elements. It has two spatial input modes  $a$  and  $b$  and two output modes  $c$  and  $d$  (Fig. 3). The theory of the lossless BS was developed by Zeilinger (1981) and Fearn and Loudon (1987), for

![](images/c65e5be35628baa96a61024437c8a0d637e63cf04596a1ca894ea5bf57a0db81.jpg)  
FIG. 3. The function of a BS. (a) The BS coherently transforms two input spatial modes (a), (b) into two output spatial modes (c), (d). (b) A Mach-Zehnder interferometer consists of two 50-50 BSs, mirrors and phase shift (as a whole it forms a universal tunable beam splitter).

![](images/dcb699d70a50c0ec50e68de8499d2d0d7c504c380b2a419bb0f30b0fe74395f7.jpg)

lossy BS; see Barnett et al. (1998). In a simplified theory of BS, one assumes identical action for every relevant frequency. The most commonly used BS is the symmetric 50:50 BS characterized by the following transformation:

$$
\hat {a} \rightarrow \frac {1}{\sqrt {2}} \hat {c} + \frac {i}{\sqrt {2}} \hat {d}, \quad \hat {b} \rightarrow \frac {i}{\sqrt {2}} \hat {c} + \frac {1}{\sqrt {2}} \hat {d}. \tag {28}
$$

In such a case, an outgoing particle can be found with equal probability  $(50\%)$  in either of the output modes  $c$  and  $d$ , no matter through which single input beam it came. The factor  $i$  in Eq. (28) is a consequence of unitarity. It describes a phase jump upon reflection (Zeilinger, 1981).

Using two 50:50 BS and a phase shifter, one can build a Mach-Zehnder interferometer, which in fact can be used as a universal BS of a variable transmittivity and reflectivity [see Fig. 1(b)]. The phase shifter can be some glass plate, a birefringent optical crystal, or a path-length tuner (e.g., an optical trombone). Together with additional phase shifters in the input and output ports, the Mach-Zehnder interferometer can perform an arbitrary SU(2) unitary transformation on a qubit encoded in the two spatial modes [see, e.g., Englert, Kurtsiefer, and Weinfurter (2001)].

Another important component is the PBS (see Fig. 4). A standard PBS transmits the horizontal and reflects the vertical polarization. The transformations between the incoming modes  $(a$  and  $b)$  and the outgoing modes  $(c$  and  $d)$  are as follows:

$$
\hat {a} _ {H} \rightarrow \hat {c} _ {H} \quad \text {a n d} \quad \hat {a} _ {V} \rightarrow i \hat {d} _ {V}, \tag {29}
$$

$$
\hat {b} _ {H} \rightarrow \hat {d} _ {H} \quad \text {a n d} \quad \hat {b} _ {V} \rightarrow i \hat {c c} _ {V}.
$$

For polarization qubits, any single-qubit operation can be accomplished by using a sequence of suitably oriented quarter-wave and half-wave plates. Simply, a half-wave plate retarding the  $45^{\circ}$  polarization acts on the  $H$  and  $V$  modes exactly as a certain 50:50 BS, etc. Now, the input modes are two orthogonal polarizations, instead of two spatial input modes of a Mach-Zehnder interferometer.

With these simple optical elements, large optical networks can be constructed, mapping an input state onto an output state via a linear transformation determined by the networks' unitary transformation. As a possible generalization of the usual interferometers with two ports, an  $N$ -port interferometer was proposed by Reck et al. (1994), which can realize any  $U(N)$  transformation for  $N$  optical spatial modes by using an arrangement of BS, phase shifters, and mirrors. Weihs et al.

![](images/07efcce7bf6867d71dd6ba394bb99dd73d7cf64b23d81c70094c60e71df4e1a6.jpg)

![](images/4672deab33891569b41c859437f0836faacd79165a6c86889d43ccb539570684.jpg)

![](images/999311f5e2dba8a4f631a9d1ffc14dfadd80a4b2ff03913aadd0c8d20e1cc6b9.jpg)  
FIG. 4. The operation of a polarizing beam splitter (PBS). (a) In the usual configuration, the PBS transmits horizontal, and reflects vertical, polarization. (b) Two photons, each entering via a different input: If the two photons incident onto the PBS have identical polarization, then they will always go out along different directions, so there will be one photon in each of the two output modes. (c) If the two incident photons have opposite polarizations, they will always go out along the same direction, so there will be two photons in one of the two outputs and none in the other. In essence, a PBS can thus be used as a polarization parity checker. From Pan et al., 1998; Pan, Simon, Brukner, and Zeilinger, 2001.

![](images/02f30d3a8973edfcb0be4ec21d8ed54241eb877aea46837ba9b3b67d1e779b7f.jpg)

![](images/0766112f543d78added6c07d9542690ecfb4359c206aa873c3f5fc1686706c59.jpg)

(1996) realized an all-fiber three-path Mach-Zehnder interferometer, which is based on the idea of symmetric unbiased multiport BS (Zeilinger et al., 1993).

# C. Two-photon interference due to indistinguishability of photons

Quantum interference<sup>15</sup> may also occur entirely due to indistinguishability of particles. We describe this phenomenon in the case of photons, i.e., bosons. One can obtain all effects due to indistinguishability by a suitable symmetrization of the amplitudes for elementary processes, for which we do not know which particle ended up in which final state (for bosons amplitudes do not change sign when particles are interchanged). However, it is much more convenient to use the formalism of bosonic creation and annihilation operators, as its algebra directly takes into account the symmetrization. Here we present the most elementary optical effect due to the indistinguishability of photons, the Hong-Ou-Mandel interference (Hong, Ou, and Mandel, 1987) behind a 50:50 BS.

As seen previously, upon reflection off a symmetric 50:50 BS a photon picks a phase shift  $i$ . We denote the input modes as  $a$  and  $b$  and output modes as  $c$  and  $d$ . If we have two spectrally identical photons (of the same polarization) each entering at exactly the same moment an opposite input port of the BS, the initial state  $\hat{a}^{\dagger}\hat{b}^{\dagger}|\Omega\rangle$  is transformed into

$$
\frac {1}{\sqrt {2}} \left(\hat {c} ^ {\dagger} + i \hat {d} ^ {\dagger}\right) \frac {1}{\sqrt {2}} \left(\hat {d} ^ {\dagger} + i \hat {c} ^ {\dagger}\right) | \Omega \rangle = \frac {i}{2} \left(\hat {c} ^ {\dagger 2} + \hat {d} ^ {\dagger 2}\right) | \Omega \rangle . \tag {30}
$$

![](images/12a6914f8cbf917959158b9418108abbfb83236ca56fcc924acee964fff0ea6a.jpg)

![](images/24202a1a65822232f0a7d3e3829e10197bafab6c328d6a46edaaddbd5f2c122d.jpg)  
FIG. 5. (a) Individually incoming photons can be transmitted or reflected. However, since the two photons are identical, we cannot distinguish between the two cases when both are transmitted or both reflected. The BS introduces a phase difference of  $\pi$  between the two amplitudes describing such possibilities. This leads to a destructive interference. Thus, no coincidence detection can be found. (b) Data from Hong, Ou, and Mandel (1987): Pairs of photons impinging on a BS are produced by spontaneous parametric downconversion (see Sec. IV.A) and have the same polarization and frequency distributions. The measured number of coincidence counts as a function of relative path displacement (temporal distinguishability) shows a "Hong-Ou-Mandel" dip, for equal optical paths. From Hong, Ou, and Mandel, 1987.

The two terms, which describe the cases in which each photon exits by a different exit port cancels each other,  $\hat{c}\hat{d} -\hat{d}\hat{c} = 0$ . This cancellation occurs if the two photons are perfectly indistinguishable in terms of all of their other degrees of freedom such as frequency, time, or polarization. The two photons exit the BS paired via only one (random) output port. This is a bunching effect due to the bosonic character of photons. Thus, there are no coincidences between the output ports.[16] Another (and more graphical) way to look at this is shown in Fig. 5(a).

If the photons are at least partially distinguishable (in this case we label the annihilation operators of the photons with different subscripts as  $\hat{a}_1$  and  $\hat{b}_2$ ), the initial state  $\hat{a}_1^\dagger \hat{b}_2^\dagger |\Omega \rangle$  is transformed by a perfect 50:50 BS via the relations in Eq. (28) into

$$
\frac {1}{\sqrt {2}} \left(\hat {c} _ {1} ^ {\dagger} + i \hat {d} _ {1} ^ {\dagger}\right) \frac {1}{\sqrt {2}} \left(\hat {d} _ {2} ^ {\dagger} + i \hat {c} _ {2} ^ {\dagger}\right) | \Omega \rangle . \tag {31}
$$

Since  $\hat{c}_1\neq \hat{c}_2$  and  $\hat{d}_1\neq \hat{d}_2$ , the terms that contribute to the cases in which each photon exits by a different exit port, namely  $\frac{1}{2} (\hat{c}_1^\dagger \hat{d}_2^\dagger -\hat{d}_1^\dagger \hat{c}_2^\dagger)|\Omega \rangle$ , do not cancel with each other.

We use  $\beta$  to denote the degree of distinguishability between photon 1 and 2. The probability of finding a coincidence count at exits  $c$  and  $d$ , which is given by the square of the norm of  $\frac{1}{2} (\hat{c}_1^\dagger \hat{d}_2^\dagger - \hat{d}_1^\dagger \hat{c}_2^\dagger) |\Omega\rangle$ , is  $(1/2) |\beta|^2$ . Thus, if  $|\beta| = 1$  (the photons  $\hat{a}$  and  $\hat{b}$  are fully distinguishable), this probability reads  $1/2$ ; if  $\beta = 0$  (the photons are indistinguishable), it vanishes. Therefore, the Hong-Ou-Mandel effect depends critically on the distinguishability of photons. The distinguishability was tuned in the original experiments with the temporal delay between the two photons [Fig. 5(b)].

The original Hong-Ou-Mandel experiment used the two photons of the same signal-idler pair from parametric downconversion (see Sec. IV.A). Later experiments of this kind evolved into observations of a Hong-Ou-Mandel dip for photons originating from two sources, which were progressively more and more independent of each other. This was motivated by both fundamental issues, such as whether independent photons indeed interfere, and practical ones; interference of photons emerging from different sources must be harnessed if one wants to build complicated schemes realizing quantum protocols, e.g., quantum repeaters (see Sec. VI.F) and distributed quantum computing (see Sec. VII). Rarity, Tapster, and Loudon (1996) observed the interference between independent photons, one of which was a triggered single photon from a down-converted pair, and the other one was in an attenuated beam derived from the pumping laser light. Interference of two triggered single photons created via parametric down-conversion by the same pump pulse passing twice through a nonlinear crystal was achieved in the Innsbruck teleportation experiment (Bouwmeester et al., 1997); for more details see Sec. VI.B. With a similar method of triggering, Keller, Rubin, and Shih (1998) used photons generated by two mutually coherent but time-separated pulses from the same mode-locked laser. Experiments aimed at observing the Hong-Ou-Mandel dip for fully independently emitted photons, like the one of Kaltenbaek et al. (2006), will be described in Sec. VI.C.

The Hong-Ou-Mandel interference provides a powerful tool to estimate the degree of indistinguishability of two separately emitted photons. For instance, two single photons successively emitted from a single quantum dot or a single trapped atom were overlapped on a BS and the Hong-OuMandel effect was observed (Santori et al., 2002; Legero et al., 2004). Other examples include single photons from independent trapped atoms and ions (Beugnon et al., 2006; Maunz et al., 2007), and from remote cold atomic ensembles (Yuan et al., 2007) or independent, tunable quantum dots (Patel et al., 2010). The interference of indistinguishable photons enables a process called entanglement swapping and

teleportation (Zukowski, et al., 1993, see Sec. VI.C), which in turn opens up prospects distributing of entanglement between distant matter qubits such as ions (Moehring et al., 2007) and atomic ensembles (Yuan et al., 2008).

A characteristic feature of the Hong-Ou-Mandel interference is that it is sensitive to path length changes on the order of the coherence length of the photons, while in a Mach-Zehnder interferometer one has subwavelength sensitivity. The photon's coherence length can range from a few hundred micrometers, in pulsed parametric down-conversion, to a few meters for trapped ions. This makes the Hong-Ou-Mandel interferometers very stable.

# D. Postselection of entanglement and quantum erasure

We now discuss other tricks and states obtainable with a single BS on which a pair of photons impinges.

Note first that according to Eq. (30), in a Hong-Ou-Mandel interferometer, the electromagnetic field emerging from the BS associated with the pair of photons is in an entangled state  $[(\hat{c}^{\dagger})^{2} + (\hat{d}^{\dagger})^{2}]|\Omega \rangle = |2_{c}0_{d}\rangle +|0_{c}2_{d}\rangle$ , a so-called  $N00N$  state (see Sec. IV.C), with  $N = 2$ . This state has interesting interferometric properties which will be discussed later.

With the simple device, one can also produce effects characteristic for a maximally entangled polarization state. Ou and Mandel (1988b) and Shih and Alley (1988) were the first to achieve this. In their experiments, the two photons entering the BS, each by a different input port, were indistinguishable in all degrees of freedom, except that they were oppositely polarized [say, one horizontally polarized  $H$  and the other vertically polarized  $V$ , see Fig. 6(a)]. After being superposed on the BS and leaving the two output ports  $c$  and  $d$ , the photons emerged in a polarization-tagged two-photon state

$$
\frac {1}{2} [ \sqrt {2} | \psi^ {-} \rangle_ {c d} + i (| \phi^ {+} \rangle_ {c c} + | \phi^ {+} \rangle_ {d d}) ].
$$

A coincident detection at the two outputs  $c$  and  $d$  can occur only due the entangled  $\left|\psi^{-}\right\rangle_{cd}$  component of the total state. As in the case of the Hong-Ou-Mandel interferometer, the visibility of this polarization interference is reduced once the photons are partially distinguishable. For example, by varying the relative optical paths before the photons reach the BS, the overlap of the photon wave packets behind the beam splitter may be controlled, up to a total distinguishability. The full effect occurs for perfect overlap. This kind of post-selected entanglement was used to violate Bell's inequality,[18] in the experiments of both Ou and Mandel (1988b) and Shih and Alley (1988). The effect was later demonstrated for two indistinguishable photons from quasi-independent sources (Pittman and Franson, 2003; Fattal et al., 2004).

Figure 6(b) shows another setup for generating entanglement, in a similar spirit, however using a PBS [such an effect was used in a proposal for obtaining multiphoton entanglement by Zeilinger et al. (1997); see Sec. IV.D]. As a PBS customarily transmits  $H$  and reflects  $V$  polarization, a

![](images/85d6aaec82f9a8676dd102fb5d6682774c24a02058e61e740705c27b7fa5c276.jpg)  
(a)

![](images/4c5d54951aa1b686f154a1e0e64c400a848993b5dadd45583da823f97d836963.jpg)  
FIG. 6. (a) Shih-Alley type polarization entanglement. One combines two orthogonally polarized photons at a BS and registers the coincidence events behind it. (b) In a similar way, by superposing two  $(H + V)$  polarized photons at a PBS, one can observe an entangled state  $|H\rangle_{c}|H\rangle_{d} + |V\rangle_{c}|V\rangle_{d}$  in the postselected coincidence counts. From Ou and Mandel, 1988b; Shih and Alley, 1988.  
(b)

coincidence detection between the two outputs can originate only if either both photons are transmitted (resulting in a  $|HH\rangle$  case) or both are reflected ( $|VV\rangle$  case). The two cases are quantum mechanically indistinguishable, if the photons are indistinguishable. Thus again, an entangled state  $|\phi^{-}\rangle_{cd}$  can be generated using postselection. As in the case of the Hong-Ou-Mandel interferometer, the entanglement quality is sensitive to optical path length changes of the order of the photons' coherence length. Such interferometers play a crucial role in creation, manipulation, and projection of various multiphoton entangled states.

When analyzing the above experiments, one could be mislead to suppose that the interference arises due to the fact that the wave packets of the two photons overlap at the BS. Indeed the Hong-Ou-Mandel dip is presented as a function of the temporal delay between the two photons, i.e., effectively in terms of the overlap [Fig. 5(b)]. However, it is important to note that essentially the origin of this interference is due to the indistinguishability of two-photon amplitudes describing the various alternatives leading to a coincidence count. To dispel a misconception that the photons must arrive at the BS at the same time for some type of classical local "agreement," Pittman et al. (1996) performed a "postponed compensation" two-photon Shih-Alley type experiment. Interference is observed, even though the photons were arriving at the BS at different times. In the experiment, the optical path of one input light beam was much longer than of the other one with a difference exceeding the photon's coherence length. However, after the interferometer, this delay was compensated (using a polarization-selective unbalanced Mach-Zehnder interferometer) in such a way that the firing times of the two detectors did not provide any information whatsoever concerning which of the two-photon processes led to the coincidence detection. The experimental results confirmed that the quantum interference can indeed be revived. A discussion of related "quantum erasure" experiments can be found in Scully, Englert, and Walther (1991); Kwiat, Steinberg, and Chiao (1992); and Michler et al. (1996).

# E. Entangled-state analyzers

The projection of two photons into a Bell state lies at the heart of many quantum information-processing protocols,

such as quantum dense coding (Bennett and Wiesner, 1992), quantum teleportation (Bennett et al., 1993), and entanglement swapping (Zukowski, et al., 1993). A deterministic controlled-NOT (CNOT) gate would make such a the Bell-state measurement possible. However, CNOT gates are difficult to realize with linear optics and single photons (see Sec. VII). Nevertheless, by exploiting quantum interference effects due to the bosonic nature of photons discussed above, photonic Bell-state and GHZ-state analyzers can be realized in a probabilistic way.

# 1. Bell-state analyzer

A linear-optical Bell-state analyzer was suggested by Weinfurter (1994) and Braunstein and Mann (1995). It is based on the two-photon interference effect at a 50:50 BS and via a coincidence analysis can distinguish two of the four Bell states. As shown in Fig. 7(a), the setup consists of a BS followed by two-channel polarizers in each of its output beams. As the polarization state  $|\psi^{-}\rangle$  is antisymmetric, it results in a coincidence detection at the outputs of the BS (i.e., a coincidence at detectors  $\mathrm{D}_{H1}$  and  $\mathrm{D}_{V2}$  or at  $\mathrm{D}_{H2}$  and  $\mathrm{D}_{V1}$ ). In fact, the state  $|\psi^{-}\rangle$  can be encoded with any degree of freedom [e.g., color encoding, see Moehring et al. (2007)] and can be pinpointed by a two-channel coincidence behind a BS. This property can be easily checked by reversing the action of the Shih-Alley interferometer. The minus sign in  $|\psi^{-}\rangle$  leads to a cancellation of the photon bunching amplitudes, that is to "fermionic-like" behavior. For the remaining three states, both photons exit via the same output port of the BS. The state  $|\psi^{+}\rangle$  can be distinguished from the other two by the fact that the emerging photons have different polarizations.[20] This results in a coincidence counts at detectors  $\mathrm{D}_{H1}$  and  $\mathrm{D}_{V1}$  or at  $\mathrm{D}_{H2}$  and  $\mathrm{D}_{V2}$ . The two states  $|\Phi^{+}\rangle$  and  $|\Phi^{-}\rangle$  both lead to a two-photon event at a single detector, and thus cannot be distinguished.

A modified version of a Bell-state analyzer, which can directly be generalized to the  $N$ -particle case, was introduced by Pan and Zeilinger (1998). Consider the arrangement of Fig. 7(b). Two spectrally identical photons enter the Bell-state analyzer by modes  $a$  and  $b$ . Assume that they arrive at  $\mathrm{PBS}_{ab}$  simultaneously, so that their wave functions overlap behind it. The properties of a PBS depicted in Fig. 4, and a coincidence detection in modes 1 and 2, allow one to distinguish  $|\phi^{+}\rangle_{12}$  and  $|\phi^{-}\rangle_{12}$  polarization Bell states. Specifically, for the incident state  $(1 / \sqrt{2})(|H\rangle_{a}|H\rangle_{b} + |V\rangle_{a}|V\rangle_{b})$  we always observe a coincidence between either detectors  $\mathrm{D}_{H1}$  and  $\mathrm{D}_{H2}$  or  $\mathrm{D}_{V1}$  and  $\mathrm{D}_{V2}$ . On the other hand, if the incident state is

![](images/89b7017a1c1d2f8226646cea0d54e33152a9974fa49a9dc5b8f5996faf416304.jpg)

![](images/6be970abf4b02cae65abbe4059afb34490ff4e64b37a5cef2e64b2784c1c6fb9.jpg)

![](images/1fae407a52cc3ee330afc0197d3dc41255fde3d8d1be198c496c22ac8639e378.jpg)  
FIG. 7. (a) A Bell-state analyzer using a BS. (b) A modified Bell-state analyzer. The angle between the half-wave plate axis and the horizontal direction is  $22.5^{\circ}$ . It corresponds to a  $45^{\circ}$  rotation of the polarization. (c) A GHZ-state analyzer. Adapted from Pan et al., 1998.

$(1 / \sqrt{2})(|H\rangle_{a}|H\rangle_{b} - |V\rangle_{a}|V\rangle_{b})$ , we observe coincidence at detectors  $D_{H1}$  and  $D_{V2}$  or  $D_{V1}$  and  $D_{H2}$ . The other two Bell states would lead to no coincidence at detectors in modes 1 and 2.

Finally, we mention that by taking advantage of the properties of hyperentanglement one can implement a complete Bell-state analysis (Kwiat and Weinfurter, 1998; Walborn, Pádua, and Monken, 2003). Such a scheme was experimentally realized (Schuck et al., 2006) and was used to beat the channel capacity limit for linear photonic superdense coding [Barreiro, Wei, and Kwiat (2008), see Sec. VI.A for more details on dense coding].

# 2. GHZ-state analyzer

Bell-state measurement schemes can be generalized to the  $N$ -particle case. One can construct a GHZ-state analyzer (Pan and Zeilinger, 1998), with which one can identify two out of the  $2^{N}$  maximally entangled GHZ states.

In the case of three spectrally indistinguishable identical photons, eight maximally entangled polarization GHZ states could be given by

$$
\left| \Phi_ {0} ^ {\pm} \right\rangle = \frac {1}{\sqrt {2}} \left(\left| H \right\rangle \left| H \right\rangle \left| H \right\rangle \pm \left| V \right\rangle \left| V \right\rangle \left| V \right\rangle\right), \tag {32}
$$

$$
\left| \Psi_ {1} ^ {\pm} \right\rangle = \frac {1}{\sqrt {2}} \left(\left| V \right\rangle \left| H \right\rangle \left| H \right\rangle \pm \left| H \right\rangle \left| V \right\rangle \left| V \right\rangle\right), \tag {33}
$$

$$
\left| \Psi_ {2} ^ {\pm} \right\rangle = \frac {1}{\sqrt {2}} \left(\left| H \right\rangle \left| V \right\rangle \left| H \right\rangle \pm \left| V \right\rangle \left| H \right\rangle \left| V \right\rangle\right), \tag {34}
$$

$$
\left| \Psi_ {3} ^ {\pm} \right\rangle = \frac {1}{\sqrt {2}} \left(\left| H \right\rangle \left| H \right\rangle \left| V \right\rangle \pm \left| V \right\rangle \left| V \right\rangle \left| H \right\rangle\right). \tag {35}
$$

The notation used is such that the index  $i$  in  $\left|\Psi_i^{\pm}\right\rangle$  designates a GHZ state with the property that the polarization of photon  $i$ , in each of the terms of the superposition, is different from the polarization of the other two. Consider now the setup of Fig. 7 and suppose that three photons enter the GHZ analyzer by modes a, b, and c. The polarization beam splitters transmit  $H$  and reflect  $V$  polarizations, thus a coincidence detection at the three outputs can only originate from the case that either all photons are transmitted (this corresponds to the input state  $|H\rangle |H\rangle |H\rangle$ ) or all reflected  $\langle |V\rangle |V\rangle |V\rangle$ ). The two cases are fully indistinguishable if the photons perfectly overlap spatially and temporally. Thus, two GHZ states, namely  $|\Phi_0^{\pm}\rangle = |H\rangle |H\rangle |H\rangle \pm |V\rangle |V\rangle |V\rangle$ , can be filtered out of the eight. One can further tell apart the states  $|\Phi^{\pm}\rangle$  by placing a polarizer after each PBS, setting it to distinguish the  $+ / -$  polarization basis (by  $+ / -$  here we denote  $\pm 45^{\circ}$  linear polarizations). In such a case, the state  $|\Phi_0^+\rangle$  leads to coincidences  $+ + +$ ,  $+ - -$ ,  $- + -$ , and  $- - +$ , while  $|\Phi_0^-\rangle$  causes totally different events:  $+ + -$ ,  $+ - +$ ,  $- + +$ , and  $- - -$ . The success probability of the GHZ analyzer is thus  $1 / 4$ .

# IV. EXPERIMENTAL REALIZATIONS OF PHOTONIC ENTANGLEMENT

Sources of entangled photons play a central role in the experimental study of foundations of quantum mechanics and are an essential resource in optical quantum information processing. The early Bell-test experiments used entangled photons from atomic cascades; see Clauser and Shimony (1978). Such a source has some drawbacks. The directions of entangled-photon emissions are uncorrelated. This causes very low collection efficiency. Moreover, the entanglement is only perfect for photons that are emitted back to back, a loophole that could allow a local hidden-variable model to explain the experimental data (Santos, 1991). Meanwhile, it was discovered that the process of spontaneous parametric down-conversion allows pairs of entangled photons to be collected in clearly specified directions, with reasonable intensity and with very high purity.

Today, essentially all entangled-photon sources employ the second order optical nonlinearity leading to SPDC or more recently also the third order Kerr nonlinearity in four-wave mixing in optical fibers. Such processes can be realized with an increasing quality and brightness. For instance, Altepeter, Jeffrey, and Kwiat (2005) reported an entangled-photon pair source with an impressive count rate of over  $1 \times 10^{6}$  per second and a fidelity of  $97.7\%$ . In this section, we shall focus on the creation of photonic entanglement of various forms.

# A. Spontaneous parametric down-conversion

If one shines strong laser light on a nonlinear crystal, the pump photons have some probability to split into correlated pairs of lower energy. This is called spontaneous parametric down-conversion. The new photons, customarily called "signal" and "idler," satisfy the following relations: for the wave vectors within the crystal one has  $\mathbf{k}_0 \approx \mathbf{k}_i + \mathbf{k}_s$  where subscripts  $0$ ,  $s$ , and  $i$  denote, respectively, pump, signal, and idler wave vectors, and the respective frequencies satisfy  $\omega_0 \approx \omega_i + \omega_s$ . This is usually called phase matching.

It governs the directional correlations of the emissions. It also implies the emerging photon pairs have entangled frequencies and linear momenta. There are two different types of the process: either signal and idler photons share the same polarization (type I) or they have perpendicular polarizations (type II).

The quantum nature of SPDC was first studied by Klyshko and Zel'dovich (Klyshko, 1967, 1988; Zel'dovich and Klyshko, 1969). With the works of Mollow (1973) and Hong and Mandel (1985) the theory reached its final form (see the Appendix). The predicted strong quantum correlations between the photon pairs created in SPDC were first experimentally observed by Burnham and Weinberg (1970). Quantum interference of (type I) SPDC photons was first used to violate Bell's inequality by Ou and Mandel (1988b) and Shih and Alley (1988). The process was shown to be a ready source of (path) entangled pairs by Horne, Shimony, and Zeilinger (1989). This was demonstrated independently by rarity and Tapster (1990). Polarization entanglement in the type II process was discovered by Kwiat et al. (1995). For a survey of SPDC, see Shih (2003).

We give a brief description of the SPDC process in the Appendix and show below how to create photons entangled in various degrees of freedom.

Polarization entanglement-Currently, the standard method to produce polarization-entangled photons is the noncollinear type II SPDC process (Kwiat et al., 1995). Its principle is described in Fig. 8.

The state emerging through the two beams A and B is a superposition of  $|H\rangle |V\rangle$  and  $|V\rangle |H\rangle$ , namely,

$$
\frac {1}{\sqrt {2}} \left(| H \rangle_ {A} | V \rangle_ {B} + e ^ {i \alpha} | V \rangle_ {A} | H \rangle_ {B}\right), \tag {36}
$$

where the relative phase  $\alpha$  is due to the birefringence. Using an additional birefringent phase shifter (or even slightly rotating the down-conversion crystal itself), the value of  $\alpha$  can be set as desired, e.g., to 0 or  $\pi$ . A net phase shift of  $\pi$  may be obtained by a  $90^{\circ}$  rotation of a quarter-wave plate in one of the paths. A half-wave plate in one path can be used to change horizontal polarization to vertical and vice versa. One can thus produce any of the four Bell states in Eq. (26) (Mattle et al., 1996).

The birefringence of the nonlinear crystal introduces complications. Since the ordinary and extraordinary photons have different velocities and propagate along different directions, the resulting longitudinal and transverse walk-offs between the two terms in the state (36) are maximal for pair creation near the entrance face. This results in a relative time delay  $\delta T = L(1 / u_{o} - 1 / u_{e})$  ( $L$  is the crystal length, and  $u_{o}$  and  $u_{e}$  are the ordinary and extraordinary group velocities, respectively) and a relative lateral displacement  $d = L\tan \rho$  ( $\rho$  is the angle between the ordinary and extraordinary beams inside the crystal). If the coherence time  $\tau_{c}$  of the downconverted light is shorter than  $\delta T$ , the terms in Eq. (36) become, in principle, distinguishable, and no two-photon polarization interference and thus no entanglement is observable. Similarly, if  $d$  is larger than the coherence width, the terms can become partially labeled by their spatial location. Fortunately, because the photons are produced coherently along the entire length of the crystal, one can completely

![](images/e918dd1f7576c0483e26a0e452c277e552de17678a32b076b2153c1e49bdd6a1.jpg)  
FIG. 8 (color). Type II parametric down-conversion. Inside a specially cut (birefringent) nonlinear crystal (e.g., BBO), a pump photon can convert spontaneously into a pair of photons of lower frequencies. The polarization of signals is orthogonal with respect to the one of idlers. One can attempt to pick only photons of frequency which is one-half of the frequency of the pumping field. In such a case, if the crystal is suitably oriented,  $H$  polarized photons are emitted into one cone (in the figure, the lower one), while  $V$  polarized photons are emitted into the other cone, and the two cones intersect. Due to the phase-matching pairs of photons pop up only along an intersection of a plane containing the pump beam with the cones, emissions along the directions at which the two cones intersect have undefined polarizations. However, as one of the photons is from the upper cone and the other one is from the lower one, and due to the indistinguishability of the two processes, we have no way to establish which is which (except from a direct polarization measurement), photons in beams A and B are polarization entangled. This holds under condition that one erases all possible distinguishing features of upper and lower cone photons (which arise because one of them is an ordinary ray and the other one an extraordinary one) which can easily be done via compensation methods described in the text.

compensate for the longitudinal walk-off (Rubin et al., 1994). After the compensation, interference occurs pairwise between processes in which the photon pair is created at distances  $\pm x$  from the middle of the crystal. The ideal compensation is therefore to use two crystals, one in each path, which are identical with the down-conversion crystal, but only half as long. If the polarizations are rotated by  $90^{\circ}$  (e.g., with a half-wave plate), the retardations of the  $o$  and  $e$  components are exchanged and temporal indistinguishability is restored. The method also provides reasonable compensation for the transverse walk-off effect.

An alternative method is using type I SPDC in two orthogonally oriented crystals. Two-photon states of tunable purity and degree of entanglement can be produced (White et al., 1999; Cinelli et al., 2004; Peters et al., 2004). Periodic poling of nonlinear crystals modifies the phase-matching conditions for SPDC and thus allows one to exploit the material's nonlinear properties more efficiently compared to bulk crystals. Kim, Fiorentino, and Wong (2006) proposed and implemented a polarization Sagnac interferometric configuration with bidirectional pumping of a type II phase-matched periodically poled  $\mathrm{KTiOPO_4}$  crystal. A pulsed (Kuzucu and Wong, 2008), and narrow band  $(0.15\mathrm{nm})$  wavelength tunable entangled-photon source based on such a configuration with a spectral brightness up to 273000 pairs  $(\mathrm{sMWnm})^{-1}$  has been reported (Fedrizzi et al., 2007). In a further development, via four-wave mixing in a photonic crystal fiber Fulconis et al. (2007) developed a bright, pulsed source of photon pairs.

![](images/fdb63f60d4c3439ad8888bc192f75d27541044ad618522f7fff0361c85014090.jpg)  
FIG. 9. A Franson-type experiment allowing interference of time-entangled photon pairs (under the condition of a strict coincidence). The main feature of the scheme is a pair of two identical unbalanced Mach-Zehnder interferometers. Adapted from Franson, 1989.

Temporal entanglement-If the crystal is pumped by a continuous wave (CW) laser with a coherence time of  $\Delta L_{c}$ , the time at which pair emission happens is undefined and phase stable within  $\Delta L_{c}$ . Now imagine that each of the photons is sent to a different unbalanced Mach-Zehnder interferometer. We assume that the interferometers have an identical arm-length difference  $\Delta L$  much longer than the coherence length of the photons, but shorter than the coherence length of the pump laser (see Fig. 9). The coincidence count rates at the outputs of both interferometers show a sinusoidal interference pattern, which depends on the sum of the local phase shifts. If the coincidence gate is much shorter than  $\Delta L_{c}$ , only the following coherent processes are selected and contribute to the interference:

$$
\frac {1}{\sqrt {2}} \left(\left| \text {l o n g} \right\rangle_ {1} \left| \text {l o n g} \right\rangle_ {2} + e ^ {i \phi} \left| \text {s h o r t} \right\rangle_ {1} \left| \text {s h o r t} \right\rangle_ {2}\right), \tag {37}
$$

where  $|\mathrm{short}\rangle$  and  $|\mathrm{long}\rangle$  denote the photon in short or long arm of the given local interferometer. This is the principle of Franson-type interferometry (Franson, 1989). The predicted interference phenomena were observed by Brendel, Mohler, and Martienssen (1992) and Kwiat, Steinberg, and Chiao (1993), many other experiments followed.

A pulsed-pump version of Franson interferometry uses so-called time-bin entanglement (Brendel et al., 1999; Gisin et al., 2002; Marcikic et al., 2002) (see Fig. 10). A short, ultraviolet pump pulse is first sent through an unbalanced Mach-Zehnder interferometer (the pump interferometer) creating two mutually coherent pump pulses  $\alpha | \text{short} \rangle_p + \beta | \text{long} \rangle_p$ , and next through a beta barium borate (BBO) crystal. Then, if via SPDC a pump photon is converted into a pair, the latter is in the state

$$
\alpha | \text {s h o r t} \rangle_ {1} | \text {s h o r t} \rangle_ {2} + \beta | \text {l o n g} \rangle_ {1} | \text {l o n g} \rangle_ {2}. \tag {38}
$$

The two entangled photons can be separated and subjected to local measurements in unbalanced interferometers with  $\Delta L$  identical as in the pump interferometer [for more details, see Gisin et al. (2002)]. By varying the parameters of the beam splitters and phases in the pump interferometer, all two-qubit

![](images/e1f71fc3f578c209cb40785d97ac7f2fdec27c80936dd8e879d34a20df698a08.jpg)  
FIG. 10. Schematic of the pulsed time-entangled twin-photon source. The interferometers are represented by curvy lines. This is to stress that practical realizations of this type of interferometers are usually built out of optical fibers and couplers. From Brendel et al., 1999.

entangled time-bin states can be generated. An advantage of the time-bin entanglement is that it is insensitive to polarization fluctuations. Using reference laser pulses to actively lock the phase, it can be robustly distributed over long distances in optical fibers. Note that because the pulses are only separated on the order of a few nanoseconds, and this is much shorter than the time scale of any phase drifts in the fiber, the drifts do not affect the quality of entanglement. An experiment by Marcikic et al. in 2004 demonstrated the distribution of time-bin entanglement over  $50\mathrm{km}$  in optical fibers.

Path entanglement-Entanglement experiments involving path (momentum) entanglement were proposed by Horne and Zeilinger (1986), and their feasible version by Zukowski and Pykacz (1988). Finally, Horne, Shimony, and Zeilinger (1989) proposed that SPDC is an ideal source in case of such experiments. This was realized independently by rarity and Tapster (1990). Because of the phase-matching relation, idler and signal photons of given frequencies are correlated in emission directions. One can use apertures, see Fig. 11, to select only two pairs of spatially conjugate modes (directions). The photon pairs then emerge via the apertures such that they are either in the upper  $a$  mode ( $a1$ ) and lower  $b$  mode ( $b2$ ) or in the lower  $a$  mode ( $a2$ ) and upper  $b$  mode ( $b1$ ). The resulting state is thus

$$
| \Psi \rangle = \frac {1}{\sqrt {2}} \left(e ^ {i \phi_ {b}} | a 1 \rangle | b 2 \rangle + e ^ {i \phi_ {a}} | a 2 \rangle | b 1 \rangle\right). \tag {39}
$$

The  $a$  modes enter a BS via opposite inputs, so do  $b$  modes. Behind the BS upper and lower paths cannot be distinguished, leading to two-photon interference, which depends on the difference of the relative phase shifts in  $a$  and  $b$  modes.

![](images/adcde1f154ac0d548e2482df128a40fcca49929d07a321b3fea01f91acb8bfd5.jpg)  
FIG. 11. The Rarity-Tapster experiment with momentum entanglement from a type I SPDC. Using double apertures A two correlated pairs of modes are selected from the emission spectrum of a type I down-conversion source. On each of the two BS beams of the same wavelength are superimposed. The detectors  $D_{a3}$ ,  $D_{b3}$ ,  $D_{a4}$ , and  $D_{b4}$  register two-photon coincidences between the  $a$  and  $b$  outputs. From Rarity and Tapster, 1990.

# B. Photonic entanglement in higher dimensions

# 1. Entangled qudits

Photonic entanglement in higher dimensions can in principle be generated by SPDC processes in a form of generalization of path or temporal entanglement into more than two conjugate pairs of beams or time bins, respectively (Zeilinger et al., 1993), and analyzed with  $N$ -port beam splitters (Reck et al., 1994). As shown by Zukowski, Zeilinger, and Horne (1997) such configuration can lead to new types of EPR correlations, and can be used for tests of local realism [which are more discriminating than two qubit tests; see Kaszlikowski et al. (2000)].

Another route is to use the photons' orbital angular momentum. Orbital angular momentum eigenstates of photons are states of the electromagnetic field with phase singularities. They can be utilized for observation of higher-dimensional entanglement (Mair et al., 2001; Vaziri, Weihs, and Zeilinger, 2002; Vaziri et al., 2003). This approach has advantages in certain quantum communication protocols (Vaziri, Weihs, and Zeilinger, 2002; Molina-Terriza et al., 2004; Groblacher et al., 2006). High-dimensional entangled qubits have also been created by transverse spatial correlations of two SPDC photons (Neves et al., 2005), or using transverse momentum and position entanglement of photons emitted in SPDC, in a form called pixel entanglement (O'Sullivan-Hale et al., 2005).

# 2. Hyperentanglement

As shown earlier, the SPDC photons are entangled in energy and momentum, and, if suitably selected, can be also entangled in polarization or path. If one selects pairs which are entangled not only in polarization but also in some other degree(s) of freedom, this specific entanglement is called hyperentanglement (Kwiat, 1997). Hyperentanglement may have interesting applications such as Bell-state analysis (Kwiat and Weinfurter, 1998; Walborn, Pádua, and Monken, 2003; Schuck et al., 2006), two-particle GHZ-type tests of local realism (Michler, Weinfurter, and Zukowski, 2000; Chen et al., 2003), implementations of single-photon two-qubit CNOT gate (Fiorentino and Wong, 2004), two-qubit swap gates (Fiorentino, Kim, and Wong, 2005), and quantum cryptography (Chen, Z.-B., et al., 2006).

Polarization-path entanglement-Polarization-path entanglement can be generated by a double pass of a pump laser through a BBO crystal (Chen et al., 2003). The pump passes the crystal and is reflected to pass it again. While the polarization state in each of the two possible emission processes is given by the respective SPDC setting, the path state of the pairs is  $|\psi^{-}(\phi)\rangle_{\mathrm{path}} = (1 / \sqrt{2})(|u\rangle_A|d\rangle_B - e^{i\phi}|d\rangle_A|u\rangle_B)$ , where the two orthonormal kets  $|d\rangle$  and  $|u\rangle$  denote the two path states of photons. By properly adjusting the distance between the mirror and the crystal such that  $\phi = 0$ , one gets

$$
| \Psi \rangle = | \psi^ {-} \rangle_ {\text {p o l}} \otimes | \psi^ {-} (0) \rangle_ {\text {p a t h}}, \tag {40}
$$

which is a two-photon state maximally entangled in both polarization and path. It was independently realized by Barbieri et al. (2005) using type I nonlinear crystals, and by Yang et al. (2005) using a type II nonlinear crystal.

Polarization-time entanglement—A more robust distribution of hyperentanglement is possible with photon pairs which are entangled both in time (i.e., time-bin entanglement) and in polarization (Genovese and Novero, 2002; Chen, Z.-B., et al., 2006; Schuck et al., 2006). To create such a polarization-time entanglement, we similarly combine the creation of polarization entanglement with the method to obtain temporal entanglement. That is, either by using a short, ultraviolet laser pulse sent first through an unbalanced Mach-Zehnder interferometer (the pump interferometer), to have two pulses well separated in time, or by taking advantage of the long coherence time of a CW-pump laser. Using a "time-path transmitter" introduced by Chen, Z.-B., et al. (2006), one can realize a transformation between polarization-path and polarization-time hyperentanglement.

Entanglement in multiple degrees of freedom-In an experiment by Barreiro et al. (2005), besides the entanglement in polarization and in energy, photon pairs from a single nonlinear crystal were also entangled in orbital angular momentum. The experimental setup is shown in Fig. 12. By pumping two BBO crystals with optical axes aligned in perpendicular planes, a two-photon  $(2\otimes 2)\otimes (3\otimes 3)\otimes (2\otimes 2)$  -dimensional hyperentangled state was produced, approximately described by

$$
\underbrace{\left(|HH\rangle + |VV\rangle\right)}_{\text{polarization}}\otimes \underbrace{\left(|1, - 1\rangle_{LG} + \alpha|0,0\rangle_{LG} + | - 1,1\rangle_{LG}\right)}_{\text{spatial}}
$$

$$
\otimes \underbrace {\left(\left| E E \right\rangle + \left| L L \right\rangle\right)} _ {\text {e n e r g y t i m e}}. \tag {41}
$$

Here  $\alpha$  describes the orbital-angular-momentum spatial mode balance, which is due the properties of the source (Torres, Alexandrescu, and Torner, 2003) and the selection via the mode-matching conditions.

# C. Twin-beam multiphoton entanglement

It is also possible to produce entangled states involving large numbers of photons, approaching the macroscopic domain. Such entanglement is related to experiments on twin beams (Smithey et al., 1992) and could be called a twin-beam multiphoton entanglement. It is different from multiphoton entanglement in which each spatially separated

![](images/7a3a260b5e656f0664f1f61d56c00f3227b2e786fc5164ba4ccd3ec932320615.jpg)  
FIG. 12. (a) Experimental setup for the creation and analysis of hyperentangled photons. (b) Spatial filtration (spa): hologram (holo) and single-mode fiber (smf). (c) Energy time transformation (e-t): thick quartz decoherer (dec) and liquid crystal (LC). (d) Polarization filtration (poln): quarter-wave plate (qwp), half-wave plate (hwp), and polarizer (pol). From Barreiro et al., 2005.

photon represents a qubit, and can be individually manipulated and observed.

The twin-beam multiphoton entanglement can be generated via standard SPDC, but with a strong pump pulse. Stimulated SPDC (Lamas-Linares, Howell, and Bouwmeester, 2001; Simon and Bouwmeester, 2003) can be seen as an extension of interferometrically enhanced SPDC (Herzog et al., 1994) and may show an onset of a laserlike emission of entangled photons, i.e., we can have an ("entanglement laser") in the sense that a (spontaneously created) photon pair in two polarization-entangled modes stimulates, inside a nonlinear gain medium, emission of additional pairs.

A simplified Hamiltonian $^{22}$  responsible for generation of polarization-entangled SPDC photons can be given as  $H_0 = i\kappa (a_H^\dagger b_V^\dagger - a_V^\dagger b_H^\dagger) + \mathrm{H.c.}$ . Horizontally ( $H$ ) and vertically ( $V$ ) polarized photons occupy two spatial modes ( $a$  and  $b$ );  $\kappa$  is a coupling constant that depends on the nonlinearity of the crystal and the intensity of the pump pulse. After the interaction time  $t$  the resulting photon state is given by  $|\psi\rangle = e^{-itH_0}|0\rangle$  (Kok and Braunstein, 2000; Lamas-Linares, Howell, and Bouwmeester, 2001; Simon and Bouwmeester, 2003), and in the number state representation reads

$$
| \psi \rangle = \frac {1}{\cosh^ {2} \tau} \sum_ {n = 0} ^ {\infty} \sqrt {n + 1} \tanh  ^ {n} \tau | \psi_ {n} ^ {-} \rangle ,
$$

$$
\left| \psi_ {n} ^ {-} \right\rangle = \sum_ {m = 0} ^ {n} \frac {(- 1) ^ {m}}{\sqrt {n + 1}} | n - m, m; m, n - m \rangle . \tag {42}
$$

The ket  $|n - m, m; m, n - m\rangle$  denotes a number state in the respective modes  $a_H$ ,  $a_V$ ,  $b_H$ , and  $b_V$ , and  $\tau = \kappa t$  is the interaction parameter. To avoid multipair emission events, most SPDC experiments are restricted to  $\tau \ll 0.1$ . By going to higher values, bipartite entangled states constituting of large numbers of photons are generated. The state  $|\psi\rangle$  is a superposition of the states  $|\psi_n^-\rangle$  of  $n$  indistinguishable photon pairs. Each  $|\psi_n^-\rangle$  is an analog of a singlet state of two spin- $n/2$  particles, thus  $|\psi\rangle$  is invariant under joint rotations of the polarization bases of both modes. The polarization of each beam is completely undetermined, but the polarizations

![](images/c5df1d3d5501a23e68e406694bebc7c07788301a6995926ab1f3597a29fd950e.jpg)

![](images/d3701062d970c5c6f8e646ac387d701e4425f77d5b79c83022d73570138c5ea9.jpg)

![](images/8c4b20ff582b341fb2b3e46fb0e1de3b182c13083e31d0f24440a71b39fadabc.jpg)  
FIG. 13 (color online). Super-resolving phase measurement with  $N00N$  states. (a) A schematic of the experimental setup of Nagata et al. (2007): a Mach-Zehnder interferometer consisting of two 50:50 beam splitters. (b) Single-photon count rate in mode  $e$  as a function of phase plate (PP) angle with single-photon input  $|10\rangle_{ab}$ . (c) Two-photon count rate in modes  $e$  and  $f$  for input state  $|11\rangle_{ab}$ . (d) Four-photon count rate of three photons in mode  $e$  and one photon in mode  $f$  for the input state  $|11\rangle_{ab}$ . The visibility of the fringes is 0.91(6), greater than the threshold to beat the standard quantum limit. Adapted from Nagata et al., 2007.

![](images/cdc32000abf6aebbd6d670275243ff46f87295c70783a406b7e6807b237bf109.jpg)

of the two beams are always anticorrelated. The average photon-pair number is  $\langle n\rangle = 2\sinh^2\tau$

Out of such states one can extract, for example, the following two-pair term of Eq. (42):

$$
\left| \psi_ {2} ^ {-} \right\rangle = \frac {1}{\sqrt {3}} \left(| 2, 0; 0, 2 \rangle - | 1, 1, 1, 1 \rangle + | 0, 2; 2, 0 \rangle\right), \tag {43}
$$

which can be treated as a singlet state of two (composite) spin-1 systems [see Howell, Lamas-Linares, and Bouwmeester (2002) for a test of Bell's inequality by entangled states of spin-1-like systems].

The theory of an entanglement laser was developed by Simon and Bouwmeester (2003). The basic principle of a stimulated entanglement creation was first experimentally demonstrated in the few-photon regime (Lamas-Linares, Howell, and Bouwmeester, 2001). Later, twin-beam entanglement of up to 12 photons (Eisenberg et al., 2004) was experimentally observed.

A special twin-beam entanglement is the so-called "high  $N00N$  type (Bouwmeester, 2004) state of two beams (Dowling, 1998; Kok et al., 2001; Kok, Lee, and Dowling, 2002)

$$
| N 0 0 N \rangle = | N, 0; 0, N \rangle = \frac {1}{\sqrt {2}} (| N \rangle_ {a} | 0 \rangle_ {b} + | 0 \rangle_ {a} | N \rangle_ {b}). \tag {44}
$$

It was experimentally realized for  $N = 3$  (Mitchell, Lundeen, and Steinberg, 2004) and  $N = 4$  (Walther et al., 2004) [for  $N = 2$ , see, e.g., Rarity et al. (1990); Edamatsu, Shimizu, and Itoh (2002); and Sun et al. (2006)]. These experiments demonstrated an interesting feature of  $N00N$  states: the effective de Broglie wavelength of the multiphoton state is by  $1/N$  shorter than the wavelength of the single photon (Jacobson et al., 1995). Nagata et al. (2007) not only measured the reduced de Broglie wavelength of four-entangled photons, but also obtained a visibility that exceeds the threshold to beat the standard quantum limit (Fig. 13). See Fig. 13(a) for more details. If we put two

single photons in each input of the Mach-Zehnder interferometer  $(|11\rangle_{ab})$ , the state after the first BS is, due to the Hong-Ou-Mandel effect,  $(|20\rangle_{cd} + |02\rangle_{cd}) / \sqrt{2}$ , which then evolves to  $(|20\rangle + e^{i2\varphi}|02\rangle) / \sqrt{2}$ . After the second BS, the probability of detecting two photons in the output modes  $e$  and  $f$  is  $P = (1 - \cos 2\varphi) / 2$  which shows a phase super resolution [for the experimental data see Fig. 13(c)]. If two photons are fed into in each input of the interferometer  $(|22\rangle_{ab})$ , after the first BS we get  $\sqrt{3 / 8}(|40\rangle_{cd} + |04\rangle_{cd}) + (1 / 2)|22\rangle_{cd}$ : a generalized multiphoton Hong-Ou-Mandel interference phenomenon. After the second BS, the probability of detecting three photons in one output  $e$  and one in  $f$  is  $P = 1 - (3 / 8)\cos 4\varphi$  [see Fig. 13(d) for data]. The high-precision optical phase measurements have many important applications, e.g., overcoming the diffraction limit for classical light (Boto et al., 2000; Kok et al., 2001).

# D. Multiphoton entanglement

The original motivation to observe entanglement of more than two particles, with measurements on the particles performed at spatially separated stations, stems from the observation by GHZ that three-particle entanglement leads to a dramatic conflict between local realism and EPR's ideas with predictions of quantum mechanics (Greenberger, Horne, and Zeilinger, 1989; Greenberger et al., 1990; Mermin, 1990a); see Sec. V.B.1. However, in 1989 no ready sources of three or more particle entanglement were available. Yurke and Stoler (1992a, 1992b) showed that in theory multiparticle entanglement effects should in principle be observable for particles originating from independent sources. A general method for making such an interference observable, and also to swap entanglement, was given by Zukowski, et al. (1993); rarity (1995); Zukowski, Zeilinger, and Weinfurter (1995); and Zeilinger et al. (1997). In the following, we first present the basic methods followed by numerous experiments in which multiphoton entanglement was observed. Once one is able to entangle two photons that never interacted, one can

construct many types of entanglement (Zeilinger et al., 1997), which in turn can be utilized in many ways (Bose, Vedral, and Knight, 1998).

# 1. Entanglement construction

We have at hand only photon sources of two-particle entanglement. We show in detail an operational method to swap entanglement of two pairs of particles (Zukowski, Zeilinger, and Weinfurter, 1995), which has been used in many experiments [the pioneering one was the Innsbruck teleportation (Bouwmeester et al., 1997)]. The technique of essentially erasing which source information can be applied in many other configurations, e.g., in the case of a double pair emission from a single source, etc. It even works for totally independent emissions (provided they are synchronized).

Entangling two independent particles: the principle—Figure 14 shows a configuration for obtaining interference effects for two pairs of particles originating from two independent sources. Assume that the sources of path-entangled states in Fig. 14, A and B, each spontaneously emits a pair of particles in an entangled state (all particles are supposed to be identical) at nearly the same moment of time, and the states of the pairs are  $|\Psi^{A}\rangle = (1 / \sqrt{2})(|a\rangle |d\rangle + |a^{\prime}\rangle |c^{\prime}\rangle)$  for source A and  $|\Psi^{B}\rangle = (1 / \sqrt{2})(|b^{\prime}\rangle |d^{\prime}\rangle + |b\rangle |c\rangle)$  for source B (the letters represent beams taken by the particles in Fig. 14, and  $\langle e|f\rangle = \delta_{ef}$ ). The beams  $x$  and  $x^{\prime}$ , where  $x = a$ ,  $b$ ,  $c$ , or  $d$  are superposed at 50:50 BSs. Behind the BSs, we place detectors in the output ports  $x(\pm)$ . In all unprimed beams, one can introduce a phase shift of  $\phi_{x}$ . The detector stations differ in their role:  $a(\pm)$  and  $b(\pm)$  observe radiation coming from one source only, but this is not so for stations  $d(\pm)$  and  $c(\pm)$ . For instance, if a single particle is detected by  $d(+)$ , its origin may be, under suitable conditions, completely unknown. If it cannot be determined, even in principle, which source produced the particle which activated the detectors, say  $d(+)$  and  $c(+)$ , then four-particle interference effects may occur.

Assume that detectors  $a(+)$  and  $b(+)$  also fired. Simultaneous firings of the four detectors can exhibit interference effects provided the two contributing processes are indistinguishable: detection of the particles from source A in  $d(+)$  and  $a(+)$ , and detection of the particles from B in  $c(+)$  and  $b(+)$ ; detection of the particles from source A in  $c(+)$

![](images/a0eb869fb32bde5bd4446ad378439656a2d65296158fe1c8a79c337efe3179cb.jpg)  
FIG. 14 (color online). Four-particle interference effects for two pairs of particles originating from two independent sources. Adapted from Zukowski et al., 1993.

and  $a(+)$ , and detection of the particles form B in  $d(+)$  and  $b(+)$ . Note that depending on the phase shifts the detection at, e.g.,  $c(+)$  and  $d(+)$ , acts like a Bell-state measurement, projecting the two photons into the state  $(1 / \sqrt{2})(|c^{\prime}\rangle |d^{\prime}\rangle +e^{i(\phi_{c} + \phi_{d})}|c\rangle |d\rangle)$ . The other two photons are, due to this event, in the state  $(1 / \sqrt{2})(|b^{\prime}\rangle |a^{\prime}\rangle +$ $e^{-i(\phi_c + \phi_d)}|b\rangle |a\rangle)$ . This process is called entanglement swapping.

Enforcing source indistinguishability-Imagine now that the sources of entangled states are two crystals pumped by independent, pulsed lasers operating synchronously. Assume that the time separation between two pulses is much larger than all other time scales of the experiment, i.e., we study the radiation generated in each crystal by a single pulse. We omit retardation effects by assuming equal optical paths. We assume that we pick the SPDC radiation with frequencies close to  $\frac{1}{2}\omega_p^o$ , where  $\omega_{p}^{o}$  is the central frequency of the pump pulse. Suppose that the four SPDC photons are detected in almost the same moment of time (up to a few nanosecond window), one in each of the detectors  $a(+)$ ,  $b(+)$ ,  $c(+)$ , and  $d(+)$ . One could determine that the photon detected at  $d(+)$  came from crystal A (B) by noting the near simultaneity of the detection of photon  $d(+)$  and one of the photons at  $a(+)$  or  $b(+)$  [the detection times of a true SPDC pair are extremely tightly correlated, see the Appendix, Eq. (A18) and the discussion after it]. To ensure that the source of photons is unknowable, the (initially spectrally broadband) photons should be detected behind a narrow-band filtering system (to be called later simply a filter) whose inverse of the bandwidth (coherence time) clearly exceeds the pulse duration  $\tau$  (e.g., by an order of magnitude). Then, the temporal separation of true SPDC pairs, all created within  $\tau$ , spreads over times much longer than  $\tau$  and thereby prevents identifying the source of the photon by comparison of the arrival times. Note that filtering is necessary only in modes  $c$  and  $d$ , while no filtering is required in front of the detectors  $a(\pm)$  and  $b(\pm)$ .[23]

One can estimate the maximal visibility expected for the interference process, using the results presented in the Appendix, where the basic properties of the SPDC radiation are derived. The amplitude of the four-photon detections at, say, detectors  $a(+), b(+), c(+)$ , and  $d(+)$  at times  $t_a$ ,  $t_b$ ,  $t_c$ , and  $t_d$ , is proportional to

$$
\begin{array}{l} e ^ {i \left(\phi_ {a} + \phi_ {b} + \phi_ {c} + \phi_ {d}\right)} A _ {a d} \left(t _ {a}, t _ {d}\right) A _ {c b} \left(t _ {c}, t _ {b}\right) \\ + A _ {b ^ {\prime} d ^ {\prime}} \left(t _ {b}, t _ {d}\right) A _ {a ^ {\prime} c ^ {\prime}} \left(t _ {a}, t _ {c}\right), \tag {45} \\ \end{array}
$$

where  $\phi_{i}, i = a, b, c,$  and  $d$ , is the local phase shift in the given beam. The probability amplitude  $A(t, t')$  to detect one photon of a SPDC pair at  $t$  and the other one at  $t'$ , is the one given by Eq. (A20). To get an overall probability of the process, one has to integrate the square of the modulus of the amplitude over the detection times. Since typical time resolution of the detectors is of the order of nanoseconds, which is much longer than the coherence times of typical

filters and the width of femtosecond (fs) pump pulses, the integrations over time can be extended to infinity. The joint probability to have counts in the four detectors behaves as

$$
1 - V _ {(4)} \cos \left(\sum_ {x = a, b, c, d} \phi_ {x}\right)
$$

and the visibility  $V_{(4)}$  is given by

$$
V _ {(4)} = \frac {\int d ^ {4} t \left| A _ {a d} \left(t _ {a} , t _ {d}\right) A _ {b c} \left(t _ {b} , t _ {c}\right) A _ {b ^ {\prime} d ^ {\prime}} \left(t _ {b} , t _ {d}\right) A _ {a ^ {\prime} c ^ {\prime}} \left(t _ {a} , t _ {c}\right) \right|}{\int d ^ {4} t \left| A _ {a d} \left(t _ {a} , t _ {d}\right) A _ {b c} \left(t _ {b} , t _ {c}\right) \right| ^ {2}}, \tag {46}
$$

where  $d^4 t = dt_a dt_b dt_c dt_d$ . Assume that the filter functions in all beams are of identical Gaussian form:  $F_{f}(t) = e^{-\frac{i}{2}\omega_{p}^{o}t}|F_{f}(t)|$ , whereas the pump beam is described by  $G(t) = e^{-i\omega_{p}^{o}t}|G(t)|$ . Here  $\omega_{p}^{o}$  is the central frequency of the pulse, and  $|F|$  and  $|G|$  functions are given by Fourier transforms of  $\exp \left[-\frac{1}{2} (\omega -\Omega)^2 /\sigma^2\right]$ , where  $\Omega = \frac{1}{2}\omega_p^o$  (for  $|F|$ ) or  $\omega_{p}^{o}$  (for  $|G|$ ), and  $\sigma$  is the respective spectral width. One gets

$$
V _ {(4)} = \left[ \frac {\sigma_ {p} ^ {2}}{\sigma_ {p} ^ {2} + \sigma_ {F} ^ {2} \sigma_ {f} ^ {2} / \left(\sigma_ {p} ^ {2} + \sigma_ {F} ^ {2} + \sigma_ {f} ^ {2}\right)} \right] ^ {1 / 2}, \tag {47}
$$

where  $\sigma_{p}$  is the spectral width of the pulse,  $\sigma_{f}$  is the spectral width of the filters in beams  $a$ ,  $a'$ ,  $b$ ,  $b'$ , and the spectral width of the filters in  $c$  and  $d$  is  $\sigma_{F}$ . If one removes the filters in beams  $a$ ,  $a'$ ,  $b$ , and  $b'$ , the formula simplifies to  $V_{(4)} = [\sigma_{p}^{2} / (\sigma_{p}^{2} + \sigma_{F}^{2})]^{1/2}$ ; see Zukowski, Zeilinger, and Weinfurter (1995). Namely, narrow filters in paths  $a$ ,  $a'$  and  $b$ ,  $b'$  are not necessary to obtain high visibility. The other filters, for detectors which observe radiation from both sources, should be always sufficiently narrow.

The influence of photon statistics--The visibility of the four-particle fringes in the setup of Fig. 14 can be impaired by the statistical properties of the emission process. The statistics of a single beam of a down converter is thermal-like. The state of idler-signal pairs emerging via a pair of (perfectly phase matched) pinholes is given by

$$
| \psi \rangle = N ^ {- 1} \sum_ {m = 0} ^ {\infty} z ^ {m} | m, s \rangle | m, i \rangle , \tag {48}
$$

where  $z$  is a number dependent on the strength of the pump,  $|m, s\rangle$  ( $|m, i\rangle$ ) denotes an  $m$ -photon state in the signal (idler) mode, and  $N$  is the normalization constant. It can be shown (Zukowski et al., 1999) that the visibility is reduced below  $50\%$  if  $|z|^2 > (\sqrt{17} - 3)/8 \approx 0.140$ . Thus, to have high visibility the ratio of the probability of each pulse to produce a single down-converted pair to the probability of not producing anything must be less than  $14\%$ . This threshold is at quite high pump powers. Nevertheless, this puts a strong limitation as how many particles can be entangled using such methods. Simply, creation of entanglement for many particles requires more and more initial entangled pairs, thus one pumps stronger. However, a strong pump leads to lower visibility of quantum interference, which may prohibit to observe the correlations due to the desired multiphoton entanglement (Laskowski et al., 2009). Recently, several experiments were performed to identify and quantify the experimental imperfections that contribute error to the produced

multiphoton states [see Barbieri et al. (2009) and Weinhold et al. (2008)].

Note that source indistinguishability in principle can also be achieved with an ultracoincidence technique, which does not require a pulsed pump, but an extremely good detection time resolution  $\Delta T$  much sharper than the coherence time of the filtered SPDC radiation, and rejection of all events at  $c(+)$  and  $d(+)$  which are detected with time difference higher than, say,  $2\Delta T$  [see Zukowski, et al. (1993)]. In such a case, the pumping lasers may be CW ones.[24]

# 2. New methods

The methods described above require a femtosecond pulsed laser pump. Unfortunately, a femtosecond pulse pumped SPDC shows relatively poor quantum interference visibilities (Keller and Rubin, 1997). The following methods are used to increase the quantum interference visibility: (i) a thin nonlinear crystal (Sergienko et al., 1999), (ii) narrowband spectral filters in front of detectors, as shown above (Di Giuseppe et al., 1997; Grice and Walmsley, 1997; Grice et al., 1998), and (iii) an interferometric technique (Branning et al., 1999, 2000) without spectral and amplitude postselection, which is making the spectral wave function of the two photons much more symmetric.[25] The first two methods reduce the intensity of the entangled-photon pairs significantly and cannot achieve perfect overlap of the two-photon amplitudes. For the theoretical and experimental details of the last method, see Kim, Kulik, and Shih (2001).

A method gaining great importance is tuning the properties of the down-conversion source and the pump such that one obtains frequency uncorrelated pairs of photons; see, e.g., Grice, U'Ren, and Walmsley (2001); U'Ren, Banaszek, and Walmsley (2003); Walton et al. (2003, 2004); Torres, Macia, and Torner (2005); Garay-Palmett et al. (2007); Mosley et al. (2008); and Halder et al. (2009) who demonstrated a source of photon pairs based on four-wave mixing in photonic crystal fibers [see also Fulconis et al. (2007)]. Engineering of the phase-matching conditions in the fibers allowed creation of photon pairs at 597 and  $860\mathrm{nm}$  in an intrinsically factorable state of frequencies. Thus there were almost no spectral correlations. The source is narrow band and bright. Two separate sources of such a kind were used to generate a Hong-Ou-Mandel interference. The idlers were used to herald the singles. The observed interference, conditioned on a joint detection event of two idlers, had a raw visibility of  $76.1\%$ . Since narrow-band filtering is unnecessary in case of such

sources, one can achieve a higher collection efficiency than in the case of using passive filtering [see Kim, Kulik, and Shih (2001) and Yao et al. (2012) where the collection efficiency was reported to be about twice as high than in measurements using  $3\mathrm{nm}$  filters].

With mastering these phase-matching tune-up techniques, one can expect that in future they may replace the ones based on passive filtering, as a new method for entanglement swapping and related processes.

# 3. First proposals

In the 1990's, many proposals were made for observations of multiphoton entanglement (Zukowski, et al., 1993; rarity, 1995; Zukowski, Zeilinger, and Weinfurter, 1995; Zeilinger et al., 1997; Pan and Zeilinger, 1998; see also Sec. III.E.2), or involving atoms (Cirac and Zoller, 1994; Haroche, 1995; Sleator and Weinfurter, 1995).

The generic idea of observing photonic GHZ entanglement, later put into practice, was given by Zeilinger et al. (1997); see Fig. 15. Assume that sources A and B simultaneously emit a photon pair each. Pairs in beams  $x$ ,  $y$  (1, 3, and 2, 4) are in identical polarization states  $(1 / \sqrt{2}) \times (|H_x, H_y\rangle + |V_x, V_y\rangle)$ . The state of the four particles, after the passage of 2 and 3 via PBS1, and provided the photons are indistinguishable (which can be secured using the methods as described earlier), reads

$$
\begin{array}{l} \frac {1}{2} \left(\left| H _ {1}, H _ {2}, H _ {3}, H _ {4} \right\rangle + \left| V _ {1}, V _ {2}, V _ {3}, V _ {4} \right\rangle + \left| H _ {1}, H _ {3}, V _ {3}, V _ {4} \right\rangle \right. \\ + \left| V _ {1}, V _ {2}, H _ {2}, H _ {4} \right\rangle). \tag {49} \\ \end{array}
$$

Only the superposition  $|H_1, H_2, H_3, H_4\rangle + |V_1, V_2, V_3, V_4\rangle$ , which is a GHZ state, leads to fourfold coincidence. Therefore, fourfold coincidences can reveal four-particle GHZ correlations.

The scheme in Fig. 15 also allows one to generate unconditional three-particle GHZ states $^{27}$  via a method based on the notion of entangled entanglement (Krenn and Zeilinger, 1996). For example, one could analyze the polarization state of photon 2 by passing it through a PBS selecting  $45^{\circ}$  and  $-45^{\circ}$  polarizations. Then the polarization state of the remaining three photons 1, 3, and 4 will be projected into  $(1/\sqrt{2}) \times (|H_1, H_3, H_4\rangle + |V_1, V_3, V_4\rangle$ , if and only if detector  $\mathrm{D}_{T1}$  detects a single photon. A similar superposition, however with a minus sign, is obtained once detector  $\mathrm{D}_{T2}$  detects a single photon. The detection of photon 2 excludes the last two terms in Eq. (49), and projects the remaining three photons into a spatially separated and freely propagating GHZ state. However, the scheme works only with photon-number discriminating detectors, and if both EPR sources emit only a pair each without double pair (or more) emission events.

![](images/a5515ebb1bb674a88edbefef320e017dc82ed81a071715c1a030e3c7b99185c3.jpg)  
FIG. 15 (color online). A three-photon polarization-entanglement source. The photon sources  $A$  and  $B$  are pumped by short pulses. The PBS1 transmits  $45^{\circ}$  polarization and reflects  $-45^{\circ}$  polarization,  $F$  is a narrow filter, and  $\mathrm{D}_{T1}$  and  $\mathrm{D}_{T2}$  are two single-photon detectors. A single-photon trigger event in one of the detectors signals that coincident detections in channels 1, 2, and 3 would result in GHZ correlations. The setup can also be used for observation of four-photon GHZ interference. From Zeilinger et al., 1997.

Unfortunately, this is not the case in the actual SPDC experiments. Because of the absence of perfect pair sources and perfect single-photon detectors, in the experiments both three-photon and four-photon entanglement (Bouwmeester, et al., 1999; Pan et al., 2001; Eibl et al., 2003; Zhao et al., 2003; see also Sec. IV.D.4) is observed only under the condition that there is one and only one photon in each of the four outputs. As there are other detection events where two photons appear in the same output port, this condition might raise doubts about whether such a source can be used for a valid GHZ test of local realism (Sec. V.B.2). By further developing the ideas of Yurke and Stoler (1992a), Zukowski (2000) showed that the above procedure indeed permits a valid GHZ test.

# 4. Experimental realizations

The first experiment involving techniques of forcing indistinguishability of photons from different parametric downconversion pairs was the teleportation experiment by Bouwmeester et al. (1997). This, however, will be discussed later in the context of quantum communication (Sec.VI). A GHZ-type entanglement among three spatially distributed photons, using the above methods of entanglement construction, was first observed by Bouwmeester et al. (1999). The main idea behind this experiment, as was put forward in Zeilinger et al. (1997), is to transform two pairs of polarization-entangled photons into three entangled photons. The fourth photon served the role of a trigger. Figure 16 illustrates the experimental setup. Two pairs of polarization-entangled photons are generated via a pulsed SPDC. The probability per pulse to create a single pair in the desired modes was on the order of a few  $10^{-4}$  with a correspondingly smaller probability to create four photons and negligible for three pair events. The source was aligned to emit photon pairs in the state  $(1 / \sqrt{2})(|H_a,V_b\rangle -|V_a,H_b\rangle)$ .

![](images/96434fbaac82f1ddf69af6cef2de5df05605ca0b3190d44954e311744d35658d.jpg)  
(a)

![](images/803b8455a4e6634254df06d11b0e868e36566269bad22991e98b4ed89e08f020.jpg)  
FIG. 16 (color online). Entanglement among three single photons. (a). Experimental setup for observing three-photon GHZ entanglement. The UV-pulse incident on the BBO crystal produces four photons, two in each mode. Conditioned on the registration of one photon at the trigger detector T, the three photons registered at D1, D2, and D3 exhibit the desired GHZ correlations. (b). Experimental data. The photon at D1 polarized at  $45^{\circ}$  and the photon at detector D2 polarized at  $-45^{\circ}$ . The two curves show the fourfold coincidences for a polarizer in front of detector D3 oriented at  $-45^{\circ}$  and  $45^{\circ}$ , respectively, as a function of the spatial delay in path a. (c). Experimental data for the case of the polarizer in front of detector D1 set to  $0^{\circ}$ . Adapted from Bouwmeester et al., 1999.

![](images/5c5c5b58a54563fbb4882923300303a6db37231e4ff1d111f7d80150a4d419a1.jpg)

The experimental arrangement was such that the GHZ entanglement could be observed under the condition that both the trigger photon and the three entangled photons are detected. This is usually called a "postselection" (sometimes also called "conditional detection" or "observation in coincidence basis"). We now go into more details on how this works. As initially there were four photons, provided that each of them is detected in a different output, one can infer that the two photons in mode  $a$  were horizontally and vertically polarized. The photon of polarization  $H$  was transmitted through the PBS and detected by the trigger detector  $T$ , and the other one,  $V$  polarized, must have been reflected by the PBS and consequently rotated by the half-wave plate (HWP) into state  $(1 / \sqrt{2})(|H\rangle + |V\rangle)$ . Concerning the two photons in mode  $b$ , they must have been one of polarization  $H$  and the other of  $V$ , in order to match the polarizations in mode  $a$ . After a random distribution by the BS, one photon can be detected by the detector D3 while the other one can be combined on a PBS with the photon from mode  $a$ . Therefore, if each of the three detectors D1, D2, and D3

detects a photon, there are only two possible polarization combinations:  $|H_{1}H_{2}V_{3}\rangle$  and  $|V_{1}V_{2}H_{3}\rangle$ . Bouwmeester et al. adjusted the two path lengths such that the two photons arrived simultaneously at the last PBS. The photons were spectrally filtered, with  $\Delta \lambda = 4.6 \mathrm{~nm}$ , and monitored by single-mode, fiber-coupled single-photon detectors. The filtering process stretched the coherence time so that it was substantially larger than the pump pulse duration ( $\sim 200$  fs). These processes erase the possibility of distinguishing the photons from different pairs by their arrival time or spatial modes (see previous sections). Thus the resulting counts originate from a superposition between  $|H_{1}H_{2}V_{3}\rangle$  and  $|V_{1}V_{2}H_{3}\rangle$ , that is, the three-photon GHZ state

$$
\frac {1}{\sqrt {2}} \left(| H \rangle_ {1} | H \rangle_ {2} | V \rangle_ {3} + | V \rangle_ {1} | V \rangle_ {2} | H \rangle_ {3}\right). \tag {50}
$$

To test whether one indeed dealt with a three-photon GHZ state, Bouwmeester et al. performed a polarization analysis (with polarizing filters in front of each detector, not shown in Fig. 16). They first compared the counts of all eight possible polarization combinations  $HHH,\ldots ,VVV$ . The results showed that the intensity ratio between the desired events  $(HHV$  and  $VVH)$  and the six other undesired ones was about 12:1. The dominance of the two terms is a necessary but not yet sufficient condition for demonstrating a GHZ entanglement, as there could, in principle, be just a statistical mixture of the two states. Next, to test whether the one indeed dealt with a coherent superposition of the two terms, Bouwmeester et al. performed measurements in the "diagonal" basis  $+ / - = H\pm V$ . A result  $^+$  at detector D1 should effectively project the state of the other photons to  $(1 / \sqrt{2})(| + \rangle_{2}| + \rangle_{3} - | - \rangle_{2}| - \rangle_{3})$ . The obtained data are consistent with this prediction, as can be seen from Fig. 16(b). This is so only within a short interval of delay between the photons, while for path length differences larger than the coherence length of the detected photons the coherence between the two GHZ-terms vanishes. Further control experiments were done by setting the polarizer in front of detector D1 at  $0^{\circ}$  such that the GHZ state (50) is projected into a separable state  $|V\rangle_{2}|H\rangle_{3}$ . In this case, the results in Fig. 16(c) show no correlation.

By extending the above technique, GHZ-type entanglement among more particles was observed. A four-photon GHZ state was first observed by Pan et al. (2001) and its genuine entanglement was confirmed by Zhao et al. (2003). Later on, five-photon entanglement was demonstrated by interfering a four-photon GHZ state (Pan et al., 2001) with a source of pseudosingle photons from an attenuated laser light (Zhao et al., 2004). With further improvements in high-power pump source and photon collection efficiency, GHZ entanglement among six photons (Lu et al., 2007) and eight photons (Yao et al., 2012) was also observed. The number of GHZ-like entangled qubits climbed up to ten by entangling both the polarization and momentum degrees of freedom of five photons (Gao, Lu, et al., 2010).

SPDC is quite versatile, as it enables one to observe a number of other, genuinely multipartite entangled states. Emission of two photons into each of two modes gives already a highly entangled state and is significantly different from simply emitting two pairs (Weinfurter and Zukowski,

2001). After beam splitting of these two modes into four modes and again conditioning on detection of one photon in each of the four modes, the observed state can be written as a superposition of a four-photon GHZ state and a product of two EPR pairs. This state, first observed by Eibl et al. (2003), is the extension of the singlet state  $|\Psi^{-}\rangle$  to four photons and is thus invariant under equal unitary transformations in the four output modes. This enables a decoherence-free communication of a qubit encoded in four-photon states (Bourennane, Eibl, Gaertner, et al., 2004). By splitting the two emission modes into three output modes the six-photon singlet was also observed recently by Radmark, Zukowski, and Bourennane (2009), with visibility of the six-photon interference as high as  $85\%$ . The high visibility is possible because the distinctive feature of this scheme is that it does not involve interferometric overlaps; only beam splitting is necessary.

Another important multipartite entangled state, the symmetric Dicke state, can be obtained by using collinear type II SPDC and splitting the four (six) photons into four (six) output modes (Kiesel et al., 2007; Prevedel et al., 2009; Wieczorek, Krischek, Kiesel, Schmid, 2009; Wieczorek et al., 2009). The high symmetry of this state makes it an ideal resource to synthesize a number of different multipartite entangled states by projection as shown above for the GHZ states (Wieczorek, Kiesel, Schmid, Weinfurter, 2009), but also for entanglement enhanced subshot-noise measurements. Finally, all the above states can also be observed by a single, tunable setup. There, a wave plate rotating the polarization in one of the two emission modes of SPDC, followed by a PBS combining these two emission modes, serves to set any superposition between a GHZ state and the product of two entangled pairs [Wieczorek et al. (2008); see also Lanyon and Langford (2009)].

To characterize the created multiphoton entangled states, various methods have been introduced. Quantum state tomography [for an introduction, see James et al. (2001)] uses projective measurements on an ensemble of identically prepared quantum states each probing the state from a different "perspective." It is a tool to fully reconstruct the density matrix of a quantum system.[28] Experimentally, this technique was used for two-photon, three-photon, four-photon polarization states, and also hyperentangled photon pairs (White et al., 1999; Barreiro et al., 2005; Resch et al., 2005; Walther, Resch, Rudolph et al., 2005). A disadvantage of such a method, however, is that the number of measurements grows exponentially with the number of photons, thus the reconstruction of a  $n$ -photon state necessitates  $4^n$ $n$ -fold coincidence measurements which is experimentally demanding.

Entanglement witnesses—The method of entanglement witnesses (Horodecki, Horodecki, and Horodecki, 1996; Lewenstein et al., 2000; Terhal, 2000; Bruß et al., 2002) allows one to detect entanglement via measuring a suitable observable. One speaks of genuine multipartite entanglement (Toth and Gühne, 2005) whenever the state involves quantum

correlations of all subsystems, such that there is no subsystem which is just classically correlated with the other particles. Detection of a genuine multiparticle entanglement with appropriate witnesses usually requires an experimental effort that increases only polynomially with the number of qubits. A toolbox for efficient witness operator construction has been created for some multiparticle states [such as GHZ, cluster, and  $W$  state, see, e.g., Gühne et al. (2007)], and applied in a number of multiphoton experiments [see, e.g., Bourennane, Eibl, Kurtsiefer, et al. (2004); Kiesel, Schmid, Toth, et al. (2005); Lu et al. (2007), and Wieczorek, et al., 2009]. We refer the interested reader to Horodecki et al. (2008) and Gühne and Toth (2009) for more details.

# V. FALSIFICATION OF A REALISTIC WORLD VIEW

With a detailed analysis of the work of EPR and its extension by Bohm (1951), in a trailblazing paper Bell (1964) proved, that despite the hopes of Einstein et al., there is a deep conflict between quantum mechanics and local realistic theories. Not only a conceptual one, which was stressed by EPR is their claims concerning incompleteness of quantum mechanics, but one which straightforwardly leads to drastically different predictions concerning two-particle interference phenomena.

Realism, the cornerstone of classical physics, is a view that for any physical system (also a subsystem of a compound system), one can find a theoretical description (deterministic or probabilistic) which involves all results of all possible experiments that can be performed upon it no matter which experiment actually was performed. Evidently, this directly contradicts the Bohr's complementarity principle. A theory is local if it assumes that information, and influences, cannot travel faster than light. By assuming that local measurement events are determined by other events (i.e., causes) in their backward light cone, the term local realism could be replaced by local causality.

Bell's famous theorem is of profound scientific and philosophical consequences. It also showed that the previously ignored class of entangled states is very important in experimentally distinguishing between the classical and the quantum. We first present the formal aspects of Bell's theorem as well as other forms of "no-go theorems" for hidden-variable theories.[29] Next, we present the most important photonic tests invalidating classes of such theories.

An important line of research was opened with the discovery of the GHZ theorem, which pertains to three or more particle systems, and reveals a contradiction between quantum mechanics and local realistic theories, even for

definite predictions. This result was the initial motivation for experimental efforts to produce entanglement of more than two particles. With the advances in multiphoton entangled-state preparation, discussed in the previous section, a new class of tests of the validity of local realistic theories became possible. Note that, as any classical information processing, or communication, has a local realistic model, the theorems and experiments that reveal phenomena impossible to describe by such formalism clearly indicate existence of a different method of processing and transferring information. That is why quantum information processing is able to perform tasks impossible with the classical methods.

# A. Bell's inequality

Consider pairs of photons simultaneously emitted in opposite directions. They arrive at two very distant measuring devices A and B operated by Alice and Bob, respectively. Their apparatuses have a "knob," which specifies which dichotomic (i.e., two valued, yes no) observable they measure.[30] One can assign to the two possible results (eigen) values  $\pm 1$  (for yes or no).[31] Alice and Bob are at any time free to choose the knob settings (also in a "delayed-choice" mode, after an emission).

Assuming realism allows one to introduce and compare values of results of all possible experiments that can be performed on an individual system, without caring which measurement would be actually done on the system. According to locality, random choices and the consecutive observations made by Alice and Bob, which can be simultaneous in certain reference frames, cannot influence each other, and the choice made on one side cannot influence the results on the other side, and vice versa.

To test local realism Alice chooses randomly, with equal probability, to measure either observable  $\hat{A}_1$  or  $\hat{A}_2$ , and Bob either  $\hat{B}_1$  or  $\hat{B}_2$ . Denote the hypothetical results that they may get for the  $j$ th pair by  $A_1^j$  and  $A_2^j$  for Alice's two possible choices, $^{32}$  and  $B_1^j$  and  $B_2^j$  for Bob's choices. The numerical values of these can be  $\pm 1$ . The assumption of local realism allows one to treat  $A_1^j$  and  $A_2^j$  on equal footing as two numbers, one of them revealed in the experiment, the second one unknown, but still either  $\pm 1$ . Thus, their sum and difference always exist, and are algebraic expressions with two unknowns. For the dichotomic values for all the possible measurement results, one obtains either the combination  $|A_1^j - A_2^j| = 2$  and  $|A_1^j + A_2^j| = 0$ , or  $|A_1^j - A_2^j| = 0$  and  $|A_1^j + A_2^j| = 2$ , and similarly for Bob's values. Thus, the following trivial relation holds:

$$
\sum_ {s _ {1} = \pm 1} \sum_ {s _ {2} = \pm 1} S \left(s _ {1}, s _ {2}\right) \left(A _ {1} ^ {j} + s _ {1} A _ {1} ^ {j}\right) \left(B _ {1} ^ {j} + s _ {2} B _ {2} ^ {j}\right) = \pm 4, \tag {51}
$$

where  $S(s_{1}, s_{2})$  is an arbitrary "sign" function of  $s_{1}$  and  $s_{2}$ , that is, one always has  $|S(s_{1}, s_{2})| = 1$ . Imagine now that  $N$  pairs of photons are emitted, pair by pair, and  $N$  is sufficiently large,  $\sqrt{1 / N} \ll 1$ . The average value of the products of the local values for a joint test (the Bell correlation function), during which, for all photon pairs, only one pair of observables (say,  $\hat{A}_{n}$  and  $\hat{B}_{m}$ ) is chosen, is given by

$$
E \left(A _ {n}, B _ {m}\right) = \frac {1}{N} \sum_ {j = 1} ^ {j = N} A _ {n} ^ {j} B _ {m} ^ {j}, \tag {52}
$$

where  $n = 1, 2$  and  $m = 1, 2$ . Equation (51) after averaging implies, together with Eq. (52), that for the four possible choices the following inequalities<sup>33</sup> must be satisfied for local realistic descriptions [see Weinfurter and Zukowski (2001) and Werner and Wolf (2001b)]:

$$
\begin{array}{l} - 4 \leq \sum_ {s _ {1} = \pm 1, s _ {2} = \pm 1} S (s _ {1}, s _ {2}) [ E (A _ {1}, B _ {1}) + s _ {2} E (A _ {1}, B _ {2}) \\ \left. + s _ {1} E \left(A _ {2}, B _ {1}\right) + s _ {1} s _ {2} E \left(A _ {2}, B _ {2}\right) \right] \leq 4. \tag {53} \\ \end{array}
$$

If one chooses a nonfactorizable function  $S(s_{1}, s_{2})$ , say,  $\frac{1}{2}(1 + s_{1} + s_{2} - s_{1}s_{2})$ , the famous Clauser, Horne, Shimony, and Holt (CHSH) (Clauser, et al., 1969) inequality is recovered<sup>34</sup>

$$
\begin{array}{l} S _ {\text {B e l l}} \equiv | E (A _ {1}, B _ {1}) + E (A _ {1}, B _ {2}) + E (A _ {2}, B _ {1}) - E (A _ {2}, B _ {2}) | \\ \leq 2. \tag {54} \\ \end{array}
$$

We now discuss one more assumption, sometimes provocatively called of free will. For the actual experiment, we assume that choices of actual observables are random and independent from all other processes in the experiment. Note that only in a part of the cases (around  $1/4$ ) the given pair of observables [see Eq. (52)] would be measured. However, as  $N$  is large, the correlation function obtained on a randomly preselected subensemble<sup>35</sup> of pairs, due to the aforementioned randomness and independence, cannot differ too much from the one that would have been obtained for the full ensemble (say, by  $\pm 2/\sqrt{N}$ ), as we deal with two statistically independent processes. Therefore, the results of the

actually chosen measurements, under all the three assumptions, must satisfy a Bell inequality in the form of Eq. (54), up to minor statistical fluctuations of the order of  $1 / \sqrt{N}$ . Note that the Bell-type argument presented above avoids any explicit introduction of hidden variables, other than the hypothetical local realistic values.

Some quantum processes involving entangled states violate the inequality. $^{36}$  For example, the predictions for the spin-  $1 / 2$  singlet give correlations for which  $S_{\mathrm{Bell}}$  can acquire the maximal value  $2\sqrt{2}$  allowed by quantum mechanics, known as the Cirel'son $^{37}$  bound (Cirel'son, 1980; Landau, 1987). In fact, predictions for any pure, nonfactorisable (i.e., not necessarily maximally entangled) two-system state lead to violations (Gisin and Peres, 1992). This is also the case for a wide range of mixed states (Horodecki, Horodecki, and Horodecki, 1995).

Experimental tests of Bell's inequality: The initial experiments using photon pairs produced in an atomic cascade to test Bell's inequalities [Freedman and Clauser (1972); Aspect, Dalibard, and Roger (1982); Aspect, Grangier, and Roger (1982); see also Clauser and Shimony (1978) for more experiments], falsified Bell's inequalities, and thus challenged the local realistic world view. However, this falsification was up to certain loopholes, which are due to experimental imperfections, and still allow one to build local realistic models for the measurement results obtained in the experiments.

The locality loophole is present in experiments which do not have independent, i.e., space-time separated measurement settings, can be guaranteed only with random and fast switching of the local measurement settings. In such a case, one of the assumptions behind Bell's inequalities, full certainty of the independence of Alice's results on Bob's settings, or vice versa, is not enforced. The efficiency loophole emerges due to low collection and detection efficiency of the particles. For an efficiency lower than about  $83\%$ , one can show that one cannot derive a (generalized) CHSH-type inequality that is violated by quantum predictions; see, for example, Garg and Mermin (1987) and Eberhard (1993) managed to lower this threshold to  $67\%$  by effectively, employing, the Clauser and Horne (1974) inequalities, albeit for nonmaximally entangled states only.[38] In the analysis of experiments with efficiency loophole, many authors usually use the so-called fair sampling assumption, which states that one expects that the fact

whether a detector registers a particle or not is statistically independent of all other processes in the experiment.[39] Of course, such an assumption is highly questionable. One can find many ad hoc local realistic models that violate it; see, e.g., Cabello and Santos (1996). For example, for qubits one could assign three possible local outcomes:  $+ / - 1$  and no count, or in the case of polarization experiments, one could expect the response of the detection systems might depend on the photon's polarization, even without turning to hidden-variable approaches. In case of some experiments, especially the early cascade ones, the polarization state of the photons depends on the direction of emission, etc.

The famous Aspect et al. experiments were the pioneering attempt to address the locality loophole. To close the locality loophole, one must freely and rapidly choose the directions of local analyzers and register the particles in such a way that it is impossible for any information about the setting and the detection to travel via any (possibly unknown) causal channel to the other observer before he or she, in turn, chooses the setting and finishes the measurement. Thus, the selection of analyzer directions has to be completely unpredictable, which necessitates a (quantum) physical random number generator. A numerical pseudorandom number generator would not do: its state at any time is predetermined. Furthermore, to achieve a complete independence of both observers, one should avoid any common context, as would be a conventional use of coincidence circuits. Individual events should be registered on both sides completely independently, and compared only long after the measurements are finished. This requires independent and highly accurate time bases on both sides.

Aspect's experiments were the first to use fast but periodic switching of the local polarization analyzers. Although the settings were quickly varying, they were derived from independent function generators with certain correlation times and thus not fully random as it is assumed in the derivation of Bell inequalities. This independent randomness was experimentally realized by Weihs et al. (1998). The observers "Alice" and "Bob" were spatially separated by  $400\mathrm{m}$  across the Innsbruck University science campus. The individual measurements were finished within a time much shorter than  $1.3~\mu \mathrm{s}$ , which is the distance of the two observation stations in light seconds. The actual orientation for local polarization analysis was determined independently by a quantum physical random number generator (Jennewein et al., 2000). The employed generator had a light-emitting diode illuminating a BS whose two outputs were monitored by a pair of photomultipliers. Upon receiving a pulse from one photomultiplier a 0 was produced, whereas the pulse coming from the other one was giving a 1. This results in a set of binary random numbers (Fig. 17). The polarization-entangled photon pairs were distributed to the observers through long optical fibers. A typical observed value of  $S_{\mathrm{Bell}}$ , the right side of inequality (54), was as high as  $2.73\pm$  0.02. In  $10\mathrm{~s~}14700$  coincidence events were collected. This

![](images/ab8d84b2974f0e3c7bfc76d1f4bd36e1557ba1b8ec490a529088892b05bf1850.jpg)  
FIG. 17 (color). One of the two observation stations. A random number generator is driving the electrooptic modulator. Silicon avalanche photodiodes are used as detectors. A "time tag" is stored for each detected photon together with the corresponding random number 0 or 1 and the code for the detector "+" or - corresponding to the two outputs of the polarizer. From Weihs et al., 1998.

corresponds to a violation of the local realistic threshold of 2 by 30 standard deviations. Still the experiment had a detection efficiency well below the required minimum allowing one to avoid the fair sampling assumption.

Meanwhile, there were many ideas to close the detection loophole; see, e.g., Eberhard (1993) and Kwiat et al. (1994). It was first closed in an ion-trap experiment by Rowe et al. (2001) utilizing the nearly perfect detection efficiency of fluorescence detection of single ions. However, as the two entangled ions were separated by approximately  $3\mu \mathrm{m}$ , the locality loophole was left widely open. A recent experiment by Matsukevich et al. (2008) involved two separate ion traps (1 m distance) and an entanglement-swapping procedure involving the photons emitted by the ions. The detection loophole was again perfectly closed. This method gives hope for a future experiment simultaneously closing both loopholes (Simon and Irvine, 2003; Rosenfeld et al., 2009). Violation of Bell's inequality was also demonstrated using Josephson phase qubits with deterministic entangled-state preparation and single-shot readout (Ansmann et al., 2009).

Other aspects of entanglement have been demonstrated distributing entanglement over long distances. For example, over  $10.5\mathrm{km}$  free space in Hefei by Peng et al. (2005), or in an asymmetric arrangement, in the case of which one photon is sent over  $144\mathrm{km}$  between the islands of La Palma and Teneriffe (Ursin et al., 2007). Bell experiments were also performed using fiber-based entangled-photon sources, from which two photons were distributed over a distance of more than  $10\mathrm{km}$  apart; see, e.g., Tittel et al. (1998) and Zbinden et al. (2001). The later experiment and the subsequent ones (Stefanov et al., 2002, 2003) were done with moving reference frames. These Bell tests

in "relativistic configurations" stress the oddness of quantum correlations.[40]

# B. GHZ theorem

# 1. Impossibility of deriving realism via perfect quantum correlations and locality

If there are  $N > 2$  maximally entangled quantum systems (qubits), and if measurements on them are performed in  $N$  mutually spatially separated regions by  $N$  independent observers, the correlations in such an experiment violate bounds imposed by local realism much stronger than in the two-particle case. More remarkably, instead of purely statistical reasoning for deriving Bell's inequality, one can fully follow the spirit of the EPR paper, and first try to define "elements of reality" based on specific perfect correlations of the entangled state. In a further step, one then can show contradicting predictions between local realistic theories and quantum mechanics with precisely those quantum predictions which were used to define the "elements of reality" (Greenberger, Horne, and Zeilinger, 1989).

Take the GHZ experiment, Fig. 2. Assume that a click at the local detector  $D_{x_1}$ , where  $x = d$ ,  $e$ ,  $f$  is described as a result of value  $+1$ , whereas clicks at  $D_{x_2}$  are ascribed  $-1$ . According to the quantum probabilities (20), the average values of the product of local results read

$$
\begin{array}{l} E (\phi_ {a}, \phi_ {b}, \phi_ {c}) = \sum_ {i, j, k = 1, 2} (- 1) ^ {i + j + k + 1} p _ {d _ {i} e _ {j} f _ {k}} (\phi_ {a}, \phi_ {b}, \phi_ {c}) \\ = \sin \left(\phi_ {A} + \phi_ {B} + \phi_ {c}\right). \tag {55} \\ \end{array}
$$

Here  $p_{d_i e_j f_k}(\phi \dots)$  is the probability for a detection of one photon by detectors  $d_i$ ,  $e_j$ , and  $f_k$ , given the phase settings  $\phi_a \dots$ . Therefore, if  $\phi_a + \phi_b + \phi_c = \pi / 2 + k\pi$  (where  $k$  is an integer), one has perfect correlations and perfect predictability of the common measurement result. For instance, for  $\phi_a = \pi / 2$ ,  $\phi_b = 0$ , and  $\phi_c = 0$ , whatever may be the results of local measurements of the observables for, say, the particles belonging to the  $n$ th triple represented by the GHZ quantum state, they have to satisfy

$$
A ^ {n} (\pi / 2) B ^ {n} (0) C ^ {n} (0) = 1, \tag {56}
$$

where  $X^n(\phi)$  ( $X = A, B,$  or  $C$ ) is the value of a local measurement, by Alice, Bob, and Cecil, respectively, that would have been obtained for the  $n$ th particle triple, if the setting of the measuring device is  $\phi$ . Locality assumption forces one to assume that  $X^n(\phi)$  depends solely on the local phase. Equation (56) indicates that we can predict with

certainty the result of measuring the observable pertaining to one of the particles (say,  $C$ ) by choosing to measure suitable observables for the other two. Hence, in a local realistic model the values  $X^n(\phi)$  for the angles specified in the equality are EPR's elements of reality.

Similarly, when measuring different settings, according to Eq. (55), one would obtain

$$
A ^ {n} (0) B ^ {n} (0) C ^ {n} (\pi / 2) = 1, \tag {57}
$$

$$
A ^ {n} (0) B ^ {n} (\pi / 2) C ^ {n} (0) = 1. \tag {58}
$$

Now, in a local realistic model, from these results we can deduce a further correlation by simply multiplying Eqs. (56)-(58). Since  $X^n(0)^2 = +1$ , regardless of whether  $X^n(0) = +1$  or  $-1$ , we obtain

$$
A ^ {n} (\pi / 2) B ^ {n} (\pi / 2) C ^ {n} (\pi / 2) = 1. \tag {59}
$$

This, however, is in a full contradiction with the quantum mechanical prediction obtained from Eq. (55) which reads

$$
A ^ {n} (\pi / 2) B ^ {n} (\pi / 2) C ^ {n} (\pi / 2) = - 1. \tag {60}
$$

Thus, the EPR elements of reality program breaks down, because it leads to a  $1 = -1$  contradiction. Introduction of EPRs elements of reality leads to a prediction concerning one of the perfect correlations, Eq. (59), which is opposite with respect to the quantum prediction. We have a "Bell theorem without inequalities" (Greenberger et al., 1990), which destroys any hopes to derive realism from locality and perfect correlations of the EPR type, as a necessary condition for any reasoning to be logically valid is that it does not lead to a  $1 = -1$  contradiction.

Multiparticle Bell inequalities-In a laboratory one cannot expect perfect correlations, and even if they were possible, any necessarily finite sample would be endowed with a finite, nonzero uncertainty. Thus, any test of local realism based on the GHZ correlations has to resort to some Bell-type inequalities. Series of such inequalities were discovered by Mermin (1990b), Ardehali (1992), and Belinskii and Klyshko (1993). To get the full set of such inequalities, for correlation functions involving the product of the result of all parties, it is enough to generalize Eq. (52) to the situation in question. For example, extending Eq. (51) for three partners one has

$$
\begin{array}{l} \sum_ {s _ {1}, s _ {2}, s _ {3} = \pm 1} S (s _ {1}, s _ {2}, s _ {3}) \left(A _ {1} ^ {n} + s _ {1} A _ {2} ^ {n}\right) \left(B _ {1} ^ {n} + s _ {2} B _ {2} ^ {n}\right) \\ \times \left(C _ {1} ^ {n} + s _ {3} C _ {2} ^ {n}\right) = \pm 8. \tag {61} \\ \end{array}
$$

This leads to the following Bell inequality (Weinfurter and Zukowski, 2001; Werner and Wolf, 2001b):

$$
\sum_ {s _ {1}, s _ {2}, s _ {3} = \pm 1} \left| \sum_ {k, l, m = 1, 2} s _ {1} s _ {2} s _ {3} E \left(A _ {k}, B _ {l}, C _ {m}\right) \right| \leq 8, \tag {62}
$$

which is the necessary and sufficient condition for correlation functions  $E(A_{k},B_{l},C_{m})$  to have a local realistic model [for proofs, see Werner and Wolf (2001b) and Zukowski and Brukner (2002)]. The reasoning is trivially generalizable to

an arbitrary number of parties. $^{41}$  The noise resistance $^{42}$  of violations of such inequalities by  $N$ -qubit GHZ states is growing exponentially with  $N$ . This is an important fact, because usually one expects noise to increase with the number of photons involved in an interferometric experiment (due to the increasing complications and alignment problems). Thus, nonclassicality of the GHZ correlations can be significant even for many particles (Mermin, 1990b; Roy and Singh, 1991; Klyshko, 1993; Zukowski, 1993; Gisin and Bechmann-Pasquinucci, 1998).

# 2. GHZ theorem for laboratory measurement

The first laboratory test of the GHZ-type paradox was done by Pan et al. (2000). The experiment used a three-photon GHZ state

$$
\left| \Delta \right\rangle = \frac {1}{\sqrt {2}} \left(\left| H \right\rangle_ {1} \left| H \right\rangle_ {2} \left| H \right\rangle_ {3} + \left| V \right\rangle_ {1} \left| V \right\rangle_ {2} \left| V \right\rangle_ {3}\right). \tag {63}
$$

The data obtained in the form of the (necessarily imperfect) GHZ correlations were shown to violate local realism.

The GHZ state (63) satisfies the following eigen equations:

$$
\hat {x} _ {1} \hat {y} _ {2} \hat {y} _ {3} | \Delta \rangle = - | \Delta \rangle , \quad \hat {y} _ {1} \hat {x} _ {2} \hat {y} _ {3} | \Delta \rangle = - | \Delta \rangle , \tag {64}
$$

$$
\hat {y} _ {1} \hat {y} _ {2} \hat {x} _ {3} | \Delta \rangle = - | \Delta \rangle , \qquad \hat {x} _ {1} \hat {x} _ {2} \hat {x} _ {3} | \Delta \rangle = | \Delta \rangle ,
$$

where  $\hat{x}$  denotes the observable discriminating between  $|45^{\circ}\rangle$  and  $|135^{\circ}\rangle$  polarizations, whereas  $\hat{y}$  discriminates between left and right circular polarizations. In both cases, the ascribed eigenvalues are 1 and  $-1$ , respectively. With these settings, one can get a GHZ paradox falsifying the elements of reality of the form described in the previous section.

Demonstration of the conflict between local realism and quantum mechanics for GHZ entanglement consists of four experiments. In the experiment by Pan et al. (2000), the measured values for  $\hat{x}_1\hat{y}_2\hat{y}_3$ ,  $\hat{y}_1\hat{x}_2\hat{y}_3$ , and  $\hat{y}_1\hat{y}_2\hat{x}_3$  followed the values predicted by quantum physics in a fraction of  $0.85 \pm 0.04$  of all cases. The fourth experiment, measuring  $\hat{x}_1\hat{x}_2\hat{x}_3$ , was also performed, and yielded results as shown in Fig. 18. The data again agree with quantum mechanics for the same fraction of events. The results are in a clear disagreement with a prediction range that can be made with the data of the three first measurements using a local realistic model.

The experimental results confirmed the quantum predictions, within an experimental uncertainty. The obtained average visibility $^{43}$  of  $(71 \pm 4)\%$  clearly surpasses the threshold of  $50\%$ , necessary for a violation of local realism in three-particle GHZ experiments (Mermin, 1990b; Roy and

![](images/3cc8303783f4ea46556ffbbd1cdc2e9201ef5f34051ef81f8ad9cb72a14d773e.jpg)

![](images/7ee898dcf7581af8f843784bb939a1d842cbc486bfa9369b898438ec59a42bba.jpg)

![](images/5d541c46f9858e7f9d83a2f79ca9a27ae8af6af65cb0e17d2f94303fbb7c4705.jpg)  
FIG. 18. (a) Predictions of quantum mechanics and (b) of local realism, and (c) observed results for the final  $\hat{x}_1\hat{x}_2\hat{x}_3$  measurement in the first GHZ-type experiment.  $H^{\prime}$  and  $V^{\prime}$  denote here diagonal and antidiagonal linear polarizations. From Pan et al., 2000.

Singh, 1991; Ryff, 1997; Zukowski and Kaszlikowski, 1997).

Four-photon entanglement was later demonstrated by Pan et al. (2001) and Eibl et al. (2003), and used for a corresponding multiphoton falsification of local realism [see also Zhao et al. (2003)].

# 3. Two-observer GHZ-like correlations

Interestingly, the GHZ reasoning can be reduced to a two-party (thus two spacelike separated regions) case while its all-versus-nothing feature is still retained. One option is to encode three two-state quantum systems in distinct degrees of freedom of only two photons. Thereby, a GHZ-type argument, now also necessarily involving noncontextuality,[44] can be applied in this two-particle scheme (Zukowski, 1991; Michler, Weinfurter, and Zukowski, 2000). The second option is to find suitable EPR elements of reality in the two-particle case, and to show that they are internally inconsistent. Such an approach has been taken by Bernstein et al. (1993) for a (spinless) two-particle interferometer. Later, after

considerable debate (Cabello, 2001a; Cabello, 2001b; Lvovsky, 2002; Cabello, 2003; Chen et al., 2003; Marinatto, 2003), it was shown that an all-versus-nothing violation of local realism can be shown for two-particle four-dimensional entangled systems. In this new refutation of local realism, one recovers EPR's original situation of two-party perfect correlations, but with much less complexity. This becomes possible with a new approach for defining elements of reality, which nevertheless strictly follows the EPR criteria.

A third protocol of the two-observer GHZ-like theorem uses a two-photon hyperentanglement (Chen et al., 2003). Because of the specific properties of the hyperentanglement, nine variables for each party can be regarded as simultaneous EPR elements of reality. The nine variables can be arranged in three groups of three, and the three variables of each group can be measured by one and the same apparatus. This eliminates the necessity of an argument based on noncontextuality as it is not necessary to assume any of these variables to be independent of local experimental context. Experimental demonstrations of such a protocol were done by Cinelli et al. (2005) and Yang et al. (2005)<sup>45</sup> using a two-photon hyperentangled state in Eq. (40) (for hyperentanglement see Sec. IV.B.2).

# 4. Hardy's paradoxes

Hardy's thought experiment (Hardy, 1993) provides an alternative way to demonstrate a violation of local realism without inequalities for two spin-half particles, or equivalently for polarizations of two photons. A crucial distinguishing feature in Hardy's thought experiment is that the two particles are nonmaximally entangled. In such a case, in the ideal situation, for a specific set of measurements quantum mechanics predicts that approximately  $9\%$  of the pairs of photons must give measurement results in a form of coincidence counts absolutely not allowed by local realism.[46] The original proposal was experimentally demonstrated by Torgerson et al. (1995) and White et al. (1999); as in the GHZ-type experiments, the results of the experiments were fed into specific inequalities, specially derived to take into account experimental imperfections (under the fair sampling assumption, of course). Their violation indicates underlying Hardy's contradiction between local realism and quantum mechanics. Hardy's scheme was later scaled up, so that  $(50 - h)\%$  of photon pairs lead to coincidence events prohibited by local realism (where  $h$  is any small finite number). The effect was demonstrated in an experiment by Boschi et al. (1997).

Another proposal suggested by Hardy (1992) was implemented using a pair of Mach-Zehnder interferometers that couple via the bosonic photon bunching effect at a beam splitter (Irvine et al., 2005). The original idea was based on a double Mach-Zehnder interferometer that involved particles that annihilate each other (say, electron and

positron). The right internal path of the electron interferometer is at some place partially overlapping with the left internal path of the positron interferometer. The individual interferometers are tuned such that if only one of the particles is fed to its interferometer, it would always exit by the left exit port. However, if both electron and positron are simultaneously fed into their interferometers, there is a nonzero probability amplitude of their annihilation. This is related to both particles being in the overlapping arms of the interferometers (within the story, in such a case the annihilation is assumed to happen with probability 1). The two particles act on each other like (two) bombs of the Elitzur and Vaidman (1993) paradox.[47] Thus, if one treats in a realistic way the presence, or the absence, of the particles in the internal paths of the interferometers, they can never be registered both in the right exit ports of their interferometers, because this would mean for each of them that the other particle was traveling via the overlapping arm. That is, both of them were there, thus annihilation must occur. Still, quantum prediction gives a probability of  $1/16$  of both particles emerging via the right exit ports. Of course, all that is a gedanken experiment per se. To formulate a feasible version of it, Irvine et al. resorted to photons, and a pair of Mach-Zehnder interferometers with one of their internal mirrors replaced by a shared 50-50 beam splitter. Instead of annihilation, they relied on the Hong-Ou-Mandel bunching effect: if two indistinguishable photons enter the shared beam splitter, such that each enters by a different input port, they exit randomly via just one port (see Sec. III.C). Thus, if two photons meet (instead of annihilation) one of the interferometers looses the light traveling through it, and no detection is possible in its exit ports. Using a similar realistic reasoning as before, this leads to the conclusion that no joint detection in the right exit ports of the two interferometers is possible. The quantum prediction is different, and the experiment gave results agreeing with it.

# C. Refutation of a class of nonlocal realistic theories

Violation of local realism implies that either locality or realism, or both, cannot provide a foundational basis for quantum theory (provided the freedom assumption of randomness and independence of setting choices holds). In a novel approach, Leggett (2003) discussed a broad class of nonlocal hidden-variable theories, which, based on a very plausible type of realism, provide an explanation for all existing Bell-type experiments. Nevertheless, they are in conflict with quantum predictions as shown theoretically by

Leggett (2003), and experimentally by Gröblacher et al. (2007). Subsequently, a reformulation enabled one to reduce the dependence on auxiliary assumptions as shown independently by Paterek et al. (2007) and by Branciard et al. (2007) [see also Romero et al. (2010)].

We now discuss the description of the polarization of photons within such theories. The following assumptions are made:  $(L_{1})$  realism,  $(L_{2})$  physical states are statistical mixtures of subensembles with definite polarizations, and  $(L_{3})$  local expectation values for polarization measurements taken for each subensemble obey Malus' law.

Importantly, locality is not assumed. Measurement outcomes may depend on whatever the parameters in spacelike separated regions are. It can be shown that such theories can explain some important features of entangled states of two particles: first, by assumption  $(L_{3})$ , they do not allow information to be transmitted faster than at the speed of light; second, they are capable to reproduce perfect anticorrelations, a fundamental feature of the Bell singlet state; and third, they provide a model for all Bell-type experiments in which the CHSH inequality was violated. Nevertheless, theories based on assumptions  $(L_{1}) - (L_{3})$  deliver predictions different from the quantum ones for certain other measurement outcomes.

We now discuss a general mathematical structure of such models. We concentrate on the description of events at Alice's side; events at Bob's side must follow a similar model. Assumption  $(L_{1})$  allows an individual binary measurement outcome  $A$  for any possible polarization measurement along any direction  $\mathbf{a}$  (that is, whether a single photon is transmitted or absorbed by a polarizer set at a specific angle) to be a well-defined function of some set of hidden variables  $\lambda$ , and, by  $(L_{2})$ , of a three-dimensional vector $^{48}$ $\mathbf{u}$ . As locality is not assumed,  $A$  can depend on some set of other possibly non-local parameters  $\eta$  and the remote setting of Bob,  $\mathbf{b}$ . That is, the measurement outcome  $A$  depends on these five variables  $A = A(\lambda, \mathbf{u}, \mathbf{a}, \eta, \mathbf{b})$ , and can take values  $\pm 1$  (two distinct measurement outcomes). According to assumption  $(L_{3})$ , particles with the same  $\mathbf{u}$  but with different  $\lambda$ s and  $\eta$ s build up subensembles of "definite polarizations" described by a probability distribution  $\rho_{\mathbf{u}}(\lambda, \eta)$ , and the local expectation value  $\bar{A}(\mathbf{u})$ , obtained by averaging over  $\lambda$  and  $\eta$ , fulfills Malus' law, that is,  $\bar{A}(\mathbf{u}) = \int d\lambda d\eta \rho_{\mathbf{u}}(\lambda, \eta) A(\lambda, \mathbf{u}, \mathbf{a}, \eta, \mathbf{b}) = \mathbf{u} \cdot \mathbf{a}$ . Finally, with assumption  $(L_{2})$ , the measured expectation value for a general physical state is given by averaging over a distribution  $F(\mathbf{u})$  of the subensembles, that is,  $\langle A\rangle = \int d\mathbf{u} F(\mathbf{u})\bar{A}(\mathbf{u})$ . Of course, one introduces a similar dependence for Bob's measurement outcomes,  $B = B(\lambda, \mathbf{v}, \mathbf{b}, \eta', \mathbf{a})$ , now depending on Bob's vector  $\mathbf{v}$ .

The correlation function of measurement results for a source emitting well-polarized photons is defined as the average of the products of the individual measurement outcomes:

$$
\begin{array}{l} \overline {{A B}} (\mathbf {u}, \mathbf {v}) = \int d \lambda d \eta d \eta^ {\prime} \rho_ {\mathbf {u}, \mathbf {v}} (\lambda , \eta , \eta^ {\prime}) A (\lambda , \mathbf {u}, \mathbf {a}, \eta , \mathbf {b}) \\ \times B (\lambda , \mathbf {v}, \mathbf {b}, \eta^ {\prime}, \mathbf {a}). \tag {65} \\ \end{array}
$$

For a general source producing mixtures of polarized photons, the observable correlations are averaged over a distribution of the polarizations  $F(\mathbf{u},\mathbf{v})$ , and the general correlation function  $E$  is given by

$$
E = \langle A B \rangle = \int d \mathbf {u} d \mathbf {v} F (\mathbf {u}, \mathbf {v}) \overline {{A B}} (\mathbf {u}, \mathbf {v}). \tag {66}
$$

It is an important trait of this model that there exist sub-ensembles of definite polarizations (independent of measurements) and that the predictions for the subensembles agree with Malus' law. It is clear that other classes of nonlocal theories, possibly even fully compliant with all quantum mechanical predictions, might exist that do not have this property when reproducing entangled states. Such theories may, for example, include additional communication or dimensions. A specific case deserving comment is Bohm's theory (Bohm, 1951). There the nonlocal correlations are a consequence of the nonlocal quantum potential, which exerts suitable torque on the particles leading to experimental results compliant with quantum mechanics (Dewdney, Holland, and Kyprianidis, 1987).

Following Leggett (2003) one can use the following identity, which holds for any numbers  $A = \pm 1$  and  $B = \pm 1$ :

$$
- 1 + | A + B | = A B = 1 - | A - B |. \tag {67}
$$

This, plus the above assumptions, implies a Leggett-type inequality [for details of the derivation see Gröblacher et al. (2007)] of the following form:

$$
\begin{array}{l} S _ {\mathrm {N L H V}} \equiv | E _ {1 1} (\varphi) + E _ {2 3} (0) | + | E _ {2 2} (\varphi) + E _ {2 3} (0) | \\ \leq 4 - \frac {4}{\pi} \left| \sin \frac {\varphi}{2} \right|, \tag {68} \\ \end{array}
$$

where  $E_{kl}(\varphi)$  is a uniform average of all correlation functions, defined in the plane of  $\mathbf{a}_k$  and  $\mathbf{b}_l$ , with the same relative angle  $\varphi$ . Inequalities avoiding the averaging were also derived and tested (Branciard et al., 2007; Paterek et al., 2007). For the inequality to be applicable, the vectors  $\mathbf{a}_1$  and  $\mathbf{b}_1$  necessarily have to lie in a plane orthogonal to the one defined by  $\mathbf{a}_2$  and  $\mathbf{b}_2$ . This contrasts with the CHSH inequality. Thus, if, as it is experimentally most easy,  $\vec{a}_1$ ,  $\vec{a}_2$ , and  $\vec{b}_1$  correspond to linear polarizations, then  $\vec{b}_2$  must correspond to an elliptical polarization.

Quantum theory violates inequality (68). Consider quantum predictions for the polarization singlet state,  $|\psi^{-}\rangle_{AB} = (1 / \sqrt{2})[|H\rangle_A|V\rangle_B - |V\rangle_A|H\rangle_B]$ . The quantum correlation function for the local measurements defined by  $\mathbf{a}_k$  and  $\mathbf{b}_l$  depends only on the relative angles between the vectors:  $E_{kl} = -\mathbf{a}_k\cdot \mathbf{b}_l = -\cos \varphi$ . Thus, the left-hand side of inequality (68), for quantum predictions, reads  $|2(\cos \varphi +1)|$ . The maximal violation of inequality (68) is for  $\varphi_{\mathrm{max}} = 18.8^{\circ}$ : the bound given by inequality (68) equals 3.792 whereas the quantum value is 3.893.

The Leggett-type inequality valid for nonlocal realistic theories of the discussed type was experimentally tested by Groblacher et al. (2007). In the experiment a SPDC source of high-fidelity two-photon entangled states was used, with visibilities  $\sim 99.0 \pm 1.2\%$  in the  $H / V$  basis,  $\sim 99.2 \pm 1.6\%$  in the  $\pm 45^{\circ}$  basis, and  $\sim 98.9 \pm 1.7\%$  in the  $R / L$  basis. At that time it was the highest reported visibility for a pulsed

![](images/dd84c142158af60ae251c47f3974116e05133ff5b0d14103999f8af417cd0d36.jpg)  
FIG. 19 (color online). The experimental violation of Leggett-type nonlocal realism in Gröblacher et al. (2007). The dashed line shows the bound of inequality (68) for the particular class of nonlocal realistic theories. The solid line is the quantum prediction reduced to fit the experimentally achieved visibility. The experimental data were taken for various difference angles of local measurement settings (parametrized as on the Poincaré sphere). From Gröblacher et al., 2007.

SPDC entanglement source, and was well beyond the threshold of  $97.4\%$  which is required for testing the Leggett-type inequality. The observed  $S_{\mathrm{NLHV}} = 3.8521 \pm 0.0227$  violates inequality (68) by 3.2 standard deviations (see the data shown in Fig. 19). At the same time, measurements gave  $S_{\mathrm{Bell}} = 2.178 \pm 0.0199$ , which violates the CHSH inequality by  $\sim 9$  standard deviations. This way, the Gröblacher et al. experiment excluded a broad class of nonlocal hidden-variable theories.

# D. Noncontextual hidden-variable theories

Another class of theorems, which show the drastic difference between the classical and the quantum, are the no-go theorems for noncontextual hidden-variable (NCHV) interpretations of quantum mechanics [Specker (1960); Bell (1966); Kochen and Specker (1967); Mermin, N.D. (1990); for a survey, see Mermin (1993)]. Such realistic theories assume that hidden variables fix the values of measurement results of all possible observables for the given system, and that such values are independent of the measurement context. That is, they do not depend on which other observables are measured together with them.[49] It is interesting that already in the lowest dimension of 3 for which a degenerate observable

can exist (only such observables can be measurable in different contexts) noncontextual hidden-variable models of quantum mechanics are impossible (Kochen and Specker, 1967).<sup>50</sup>

Bell's theorem is a case of a no-go theorem for NCHV in which noncontextuality is given "for free" by the locality assumption. As locality forbids the result on Alice's side to depend on the actual observable chosen to be measured by Bob, etc., the required noncontextuality is enforced by the relativistic causality. This is very appealing, because relativity is generally assumed to be a principle setting theory for causal links. Noncontextuality, without the help from relativistic principles, seems to be a much stronger assumption, as it is difficult to argue why nature has to obey it.[51] Nevertheless, both NCHV theories and local realistic ones can be reduced to the assumption of the existence of a joint probability distribution for noncommuting observables. Note that such distributions are impossible in the quantum formalism.

We now present an example of a Kochen-Specker type problem. Recently, Cabello (2009) showed that if nine observables  $A$ ,  $B$ ,  $C$ ,  $a$ ,  $b$ ,  $c$ ,  $\alpha$ ,  $\beta$ , and  $\gamma$  have predefined noncontextual outcomes  $\pm 1$ , they must satisfy the following inequality:

$$
\begin{array}{l} S = \langle A B C \rangle + \langle a b c \rangle + \langle \alpha \beta \gamma \rangle + \langle A a \alpha \rangle \\ + \langle B b \beta \rangle - \langle C c \gamma \rangle \leq 4, \tag {69} \\ \end{array}
$$

where  $\langle ABC\rangle$  denotes the ensemble average of the product of the three outcomes of measuring the mutually compatible observables  $A$ ,  $B$ , and  $C$ . For any four-dimensional quantum system, one can find a set of observables for which the prediction of quantum mechanics is  $S = 6$ , irrespectively of the actual state. This inequality was violated in an experiment by Amselem et al. (2009), where the chosen observables had the form

$$
\begin{array}{l} A = \sigma_ {z} ^ {(1)}, \qquad B = \sigma_ {z} ^ {(2)}, \qquad C = \sigma_ {z} ^ {(1)} \otimes \sigma_ {z} ^ {(2)}, \\ a = \sigma_ {x} ^ {(2)}, \qquad b = \sigma_ {x} ^ {(1)}, \qquad c = \sigma_ {x} ^ {(1)} \otimes \sigma_ {x} ^ {(2)}, \\ \alpha = \sigma_ {z} ^ {(1)} \otimes \sigma_ {x} ^ {(2)}, \quad \beta = \sigma_ {x} ^ {(1)} \otimes \sigma_ {z} ^ {(2)}, \quad \gamma = \sigma_ {y} ^ {(1)} \otimes \sigma_ {y} ^ {(2)}. \tag {70} \\ \end{array}
$$

The above operators  $\sigma_{i}$  ( $i = x, y, z$ ) are the usual Pauli operators, for two subsystems, 1 and 2. This set has the following properties (Peres, 2002): all operators have spectrum  $\pm 1$ , all operators in each row commute, and so do all operators in each column. However, any two operators belonging to different columns and rows do not commute. Thus, each operator belongs to two different contexts explicitly displayed in this array. Furthermore, each operator is the product of the other ones in the column or in the row to which it belongs, with the sole exception that in the case of the last column each operator is also such a product but times  $-1$ . Thus, there is no way that these nine operators behave like real numbers upon multiplication. In other words, if one ascribes to each of the operators whatever realistic values, either  $+1$  or  $-1$ , independent of the row or column, one runs

into a contradiction with quantum formalism. The trick used by Anselem et al. is to treat as subsystem 1 the polarization degree of freedom of a photon, and as subsystem 2 the path degree of freedom, as it was the case in Zukowski (1991), Michler, Weinfurter, and Zukowski (2000), and Simon et al. (2000). This allowed the construction of six elaborate interferometers equivalent to measurements of all the terms in the inequality (69). The observed value of the left-hand side of inequality (69) was for all 20 tested states close to 5.45, with the highest measurement error at 0.0032. After averaging over all states the standard deviation was just 0.0006, thus the violation of the inequality was as high as by 655 standard deviations. The discrepancy between the ideal quantum value 6 was due to imperfections in the complicated interferometers (note that each one had eight exit ports), and the effective observables were slightly deviating from the ideal ones considered in the theoretical reasoning of Cabello. Most recently, a proposal by Klyachko et al. (2008) for a single qutrit contextuality experiment involving only six different measurements was experimentally realized for photons prepared in superposition of three modes (Lapkiewicz et al., 2011).

# VI. QUANTUM COMMUNICATION

Quantum communication ultimately aims at absolute security and faithful transfer of information, classical or quantum. Photons are the fastest information carrier, and due to their very weak coupling to the environment are an obvious choice for quantum communication, especially for long distances. Hence, the ability of manipulating the quantum features (such as coherence and entanglement) of photons is a precious resource.

In this section, we review several breakthroughs in the field of quantum communication<sup>52</sup>: By exploiting entanglement one can efficiently encode classical messages (Bennett and Wiesner, 1992; Sec. VI.A), transfer quantum information to a remote location (Bennett et al., 1993; Sec. VI.B), entangle two remote particles that have no common past (Zukowski, et al., 1993; Sec. VI.C), and purify a large ensemble in a less entangled states into a smaller ensemble with higher entanglement (Bennett et al., 1996; Deutsch et al., 1996; Gisin, 1996; Horodecki, Horodecki, and Horodecki, 1996; Pan, Simon, Brukner, and Zeilinger, 2001; Sec. VI.D).

Needless to say, one of the ultimate dreams is long-distance or even global  $(10^{3} - 10^{4}\mathrm{km})$  quantum communication. As a combination of the ideas of entanglement purification and swapping, the quantum repeater protocol (Briegel et al., 1998, see Sec. VI.F) is an efficient method for beating decoherence and photon losses in attempts to create long-distance high-quality entanglement.

In Sec. VI.E, we discuss steps on the road toward satellite-based quantum communication and its first step, i.e., free-space distribution of entangled-photon pairs over a distance of  $10\mathrm{km}$  achieved in 2005 (Peng et al., 2005; Resch et al., 2005) and, more recently, over  $144\mathrm{km}$  (Ursin et al., 2007; Fedrizzi et al., 2009).

# A. Quantum dense coding

One can encode two bits of classical information with two qubits in such a way that each qubit carries a single bit. To this end, in the case of two qubits represented by polarization states, one could use states  $HH$ ,  $HV$ ,  $VH$ , and  $VV$ . The idea of quantum dense coding introduced by Bennett and Wiesner (1992) is that, by manipulating only one of the two particles in a Bell state, one can also encode two bits of information.

The procedure runs as follows:

Step 1: Sharing maximal entanglement. A maximally entangled qubit pair (say, in the state  $|\psi^{+}\rangle_{AB}$ ) is shared by Alice and Bob. They agree in advance that  $|\psi^{-}\rangle_{AB}, |\phi^{-}\rangle_{AB}, |\phi^{+}\rangle_{AB}$ , and  $|\psi^{+}\rangle_{AB}$  represent the binary numbers 00, 01, 10, and 11, respectively.

Step 2: Coding of the message. According to the value Bob wants to transmit to Alice, he performs one out of four possible unitary transformations (identity operation  $\hat{I}$ ,  $\sigma_x$ ,  $\sigma_y$ , and  $\sigma_z$ ) on his qubit  $B$  alone. The three nonidentity operations transform, in an one-to-one way, the original state  $|\psi^{+}\rangle_{AB}$ , respectively, into  $|\phi^{+}\rangle_{AB}$ ,  $|\phi^{-}\rangle_{AB}$ , and  $|\psi^{-}\rangle_{AB}$ . Once this is done, Bob sends his qubit to Alice. Note that this possibility of transforming any of the four basis states to any other by only manipulating one of the two qubits holds only for the maximally entangled states. For product (and classical) states it is always necessary to have control over both qubits (bits) to encode two bits in four distinguishable states.

Step 3: Decoding of the message. Upon reception, Alice performs a Bell-state measurement, distinguishing between the four code states and thus allowing her to read out both bits of information. The quantum dense coding doubles the information capacity of the transmission channel: what is actually sent is only one qubit. This more efficient way of coding information at first glance seems to be at odds with Holevo (1973), which states that maximally one bit can be encoded on a single qubit. Entanglement, a property of pairs of qubits, allows one to circumvent this theorem and to encode information entirely in the relative properties of the pair, i.e., in their correlations.

The first experimental realization of quantum dense coding was reported by Mattle et al. (1996). The experimental setup is shown in Fig. 20. The preparation of the polarization-entangled photon pairs, the single-qubit operations at Bob's station, and Alice's Bell-state analyzer can all be done with the SPDC and linear-optical techniques presented in the previous sections. In the Innsbruck experiment, each of the two  $|\psi^{\pm}\rangle_{AB}$  states could be distinguished, and they could be distinguished from  $|\phi^{\pm}\rangle_{AB}$ . However, with interferometric Bell-state analysis, there was no possibility to tell which of the states  $\phi^{\pm}$  caused the given detection event. Thus, three different messages could be operationally encoded by manipulating a single qubit only.[53] Thus, an increase of channel capacity to  $\log_23\simeq 1.58$  bits was possible, the highest value achievable using linear optics and classical communications; see Lütkenhaus, Calsamiglia, and Suominen (1999) and Vaidman and Yoran (1999). However, the observed

![](images/c087aa5cf89b5a824952d7478ba62e7ff2c216e2b239a5799b42498871d53e24.jpg)  
FIG. 20. Experimental setup for quantum dense coding. From Mattle et al., 1996.

signal-to-noise ratio reduced the actual channel capacity to on average 1.13 bit for the cases of successful transfers. Nevertheless, the classical and Holevo values of 1 were breached.

Schuck et al. (2006) realized a complete linear-optical Bell-state analyzer which is able to distinguish all four Bell states, provided the initial pair is entangled in two degrees of freedom (hyperentangled), in this case polarization entanglement plus the intrinsic time-energy correlation of SPDC photons (Kwiat and Weinfurter, 1998). With this ability, the dense coding protocol was implemented for all four Bell states in the polarization degree of freedom, achieving an overall channel capacity of 1.18(3) bits per photon. Later developments were using the observation that with hyperentanglement in at least two degrees of freedom four Bell states in one of the degrees of freedom can be distinguished by local measurements (Walborn, Pádua, and Monken, 2003). Barreiro, Wei, and Kwiat (2008) exploited pairs of photons simultaneously entangled in spin and orbital angular momentum and achieved a channel capacity of 1.630(6) bits, finally beating the channel capacity limit of 1.58 bits of the conventional linear-optics implementations.

# B. Quantum teleportation

The fascinating possibility of quantum teleportation was discovered by Bennett et al. (1993). Quantum teleportation is indeed not only a critical ingredient for many more quantum communication protocols and for quantum computation (Gottesman and Chuang, 1999; Knill, Laflamme, and Milburn, 2001), its experimental realization allows new studies of the fundamentals of quantum theory.

# 1. Theory: Qubit teleportation involving an EPR channel and two bit transfer

The idea of quantum teleportation is illustrated in Fig. 21(a). Suppose particle 1 carries a qubit in the state  $|\chi \rangle$  which Alice should teleport to Bob, that is to transfer it to his particle. Consider pure states and we represent our discussion in terms of qubits carried by polarization states of photons. We assume that  $|\chi \rangle_{1} = \alpha |H\rangle_{1} + \beta |V\rangle_{1}$  is the

![](images/de3dfa76219d8514730e7f6cbb5675745a691e233b9f8182f964f9ffa19816a5.jpg)

![](images/edc966f659638d0f90b820fee46597e84a0aea96fcb1a70c400c90495697adb4.jpg)  
FIG. 21 (color). Experimental quantum teleportation. (a) Principle of quantum teleportation. Alice has particle 1, whose qubit state she wants to teleport to Bob. Alice and Bob share an ancillary entangled pair of qubits carried by particles 2 and 3. Alice performs a Bell-state measurement jointly on particles 1 and 2. She sends a two-bit classical information informing Bob about the result of her measurement. Based on this, he performs one of four unitary transformations (U) on his ancillary particle. The transformations are such that particle 3 ends up in the state identical to the original state of particle 1. (b) Setup of the Innsbruck teleportation experiment. A pulse of ultraviolet light passing through a nonlinear crystal creates an ancillary pair of entangled photons 2 and 3 in a polarization state  $|\psi^{-}\rangle_{12}$ . The pulse is reflected, and during its second passage through the crystal another pair of photons can be created. One of them plays the role of particle 1. The other one serves as a trigger indicating that photon 1 is under way. Alice looks for coincidences after the BS at which photons 1 and 2 are superposed. Upon receiving a classical information indicating that Alice obtained a coincidence count in detectors f1 and f2, which implies a collapse into  $|\psi^{-}\rangle_{12}$ , Bob knows that his photon 3 is in the original polarization state of photon 1. He can check whether this is indeed so by a polarization analysis with a PBS and the detectors d1 and d2 behind it. From Bouwmeester et al., 1997.

original polarization state of particle 1. Alice does not know the state of this qubit. Thus, the trivial idea that Alice performs certain measurements on  $|\chi \rangle_{1}$  by which she would obtain all the information necessary for Bob to reconstruct the state is ruled out: an experiment on a qubit can give only one bit of information. This only suffices to determine which state can be ruled out, but is insufficient to reconstruct the actual state. To this end, we need infinitely many measurements on identical copies of the state. The projection postulate makes it impossible to fully determine the state of a single quantum system, or, from another point of view, the no-cloning principle (Wootters and Zurek, 1982) excludes the possibility to create additional high-fidelity replicas of the original state.

Still, according to Bennett et al. there is a way out. Suppose that an ancillary pair of photons 2 and 3 is shared by Alice and Bob, and that it is in the polarization-entangled state  $|\psi^{-}\rangle_{23}$ . The entire system, comprising of the unknown state of particle 1 and the entangled pair, is in a state  $|\chi \rangle_{1}|\psi^{-}\rangle_{23}$ . By expanding the state of particles 1 and 2 (they are in the hand of Alice) in the Bell basis, one gets

$$
\begin{array}{l} \left| \chi \right\rangle_ {1} \left| \psi^ {-} \right\rangle_ {2 3} = \frac {1}{2} [ \left| \psi^ {-} \right\rangle_ {1 2} (- \alpha | H \rangle_ {3} - \beta | V \rangle_ {3}) + \left| \psi^ {+} \right\rangle_ {1 2} \\ \times (- \alpha | H \rangle_ {3} + \beta | V \rangle_ {3}) + | \phi^ {-} \rangle_ {1 2} (\alpha | V \rangle_ {3} \\ + \beta | H \rangle_ {3}) + | \phi^ {+} \rangle_ {1 2} (\alpha | V \rangle_ {3} - \beta | H \rangle_ {3}) ]. \tag {71} \\ \end{array}
$$

Now, if Alice performs a polarization Bell-state measurement on her two particles then the four possible outcomes are equally likely, regardless of the unknown state  $|\chi \rangle_{1}$ . However, once particles 1 and 2 are projected into one of the four entangled states, the polarization state of particle 3 is instantaneously projected into one of the four pure states appearing in Eq. (71). They can be rewritten in the following form:

$$
- | \chi \rangle_ {3}, - \hat {\sigma} _ {z} | \chi \rangle_ {3}, \quad \hat {\sigma} _ {x} | \chi \rangle_ {3}, \quad \hat {\sigma} _ {y} | \chi \rangle_ {3}, \tag {72}
$$

where the hatted symbols represent Pauli operators, which act as unitary transformations. Each of these possible resultant states of Bob's particle 3 is related in a one-to-one way with the original state  $|\chi \rangle_{1}$ , which Alice wanted to teleport. In the case of the first (singlet) outcome, the state of polarization of particle 3 is the same as the initial state of particle 1 (except for an irrelevant phase factor), so Bob does not need to do anything to finish the transfer of the original state of polarization of particle 1. In the other three cases, Bob can apply one of the unitary transformations of Eq. (72) to convert the state of particle 3 into the original one of particle 1. However, all this is possible only if he additionally receives via a classical communication channel a two-bit information on the Bell-state measurement result obtained by Alice.[54] After Bob's unitary operation, the final state of polarization of particle 3 becomes the new carrier of Alice's unknown state,  $|\chi \rangle_{1}$ . The original state of Alice's particle 1 is irrecoverably erased by the Bell-state measurement, as the Bell-state measurement does not reveal any information on the properties of any of the particles prior to the measurement. This is why quantum teleportation circumvents the no-cloning theorem.

The transfer of quantum information from particle 1 to particle 3 can happen over arbitrary distances. It is not necessary for Alice to know where Bob is (although they do need to share some reference frame information in order for the protocol to work). Furthermore, as quantum teleportation is a linear operation applied to  $|\chi \rangle_{1}$ , it works for mixed states, or entangled states, equally well; the initial state  $|\chi \rangle_{1}$  can be completely unknown not only to Alice but to anyone. A fascinating case is that  $|\chi \rangle_{1}$  could even be quantum mechanically completely undefined at the time the Bell-state measurement takes place. This is the case when, as already remarked by Bennett et al. (1993), particle 1 itself is a

member of an entangled pair, ultimately leading to entanglement swapping (Zukowski, et al., 1993; Bose, Vedral, and Knight, 1998). Quantum teleportation does not violate causality: a transfer of two bits of classical information is absolutely necessary to conclude the process.

Generally speaking, the basic criteria to achieve a bona fide qubit[55] teleportation are (1) the experimental scheme without any changes is capable of teleporting any pure or mixed qubit state, this includes the possibility of entanglement swapping; (2) a fidelity better than the classical one of  $2/3$ , see Massar (1995) can be achieved; (3) at least in principle, the scheme should be extendable to long distances; and (4) the state to be teleported should be of external nature, that is, it is carried by a particle which plays no role in the preparation of the quantum part of the teleportation channel (essentially the EPR pair). This in principle allows one to teleport any unknown qubit state delivered by some outside party.

# 2. Experimental quantum teleportation

Figure 21(b) is a schematic of the Innsbruck experimental setup of Bouwmeester et al. (1997). A pulse of ultraviolet laser passing back and forth through a BBO crystal (type II) creates two polarization-entangled EPR pairs. The pair used as the ancillary one, labeled here as photons 2 and 3, is distributed to Alice and Bob. Photon 1 of the other pair passes a polarizer which prepares it in the initial state to be teleported, and photon 4 is a trigger indicating that photon 1 is under way. After photon 1 is given to Alice, she combines it with her photon 2 and performs the Bell-state analysis.

To demonstrate that teleportation is allowed by Nature, it is sufficient to identify one of the four Bell states. Bell-state measurement on photons 1 and 2 is done with the use of a BS. As explained in Sec. III.E.1, if there is a coincidence detection between the two outputs of the beam splitter, then the photons are projected to the antisymmetric state  $|\psi^{-}\rangle_{12}$ . The Bell-state analysis relies on the interference of two independently created photons. Therefore, one has to guarantee that behind the BS the information which photon came from which source is completely erased. This was done using the methods described in Sec. IV.D.1 (Zukowski, Zeilinger, and Weinfurter, 1995). In the experiment, the UV-pump pulse had a duration of 200 fs. By using narrow bandwidth filters  $(\Delta \lambda = 4\mathrm{nm})$  in front of the detectors registering photons 1 and 2, a coherence time of about 500 fs could be obtained, which was sufficiently longer than the pump pulse duration, so that one could not infer anymore during which passage through the crystal which of the two photons was created. This generated high visibility of the multiphoton interference. Furthermore, single-mode fiber couplers acting as spatial filters were used to guarantee good mode overlap of the detected photons.

To experimentally demonstrate that an arbitrary unknown quantum state can be teleported, it is sufficient to show that the scheme works for all mutually orthogonal axes of the

![](images/c7856415bdf8881d07974fd2560ac283d2b5dc7447760ee62ee98b5178987124.jpg)  
FIG. 22. The measured threefold coincidence rates at d2f1f2  $(+45^{\circ})$  and d1f1f2  $(-45^{\circ})$  for two cases of the state to be teleported being polarized under  $+45^{\circ}$  (a) and (b) or  $-45^{\circ}$  (c) and (d), respectively. The coincidence rates are plotted as a function of the delay (in  $\mu \mathrm{m}$ ) between the arrival of photon 1 and 2 at Alice's BS [see Fig. 21(b)]. The threefold coincidence rates are plotted after subtracting the spurious threefold background contribution. The data, together with similar results for other polarizations, constitute a positive result of a test for teleportation of an arbitrary state. From Bouwmeester et al., 1997.

polarization (Poincaré) sphere. The experimental results for teleportation of photon 1 polarized under  $+45^{\circ}$ $(-45^{\circ})$  is shown in the left (right) column of Fig. 22. Bouwmeester et al. demonstrated that quantum teleportation works for orthogonal states  $|H\rangle$  and  $|V\rangle$  as well as for  $|H\rangle + |V\rangle$ ,  $|H\rangle - |V\rangle$ , and  $|H\rangle + i|V\rangle$ . Thus, teleportation was tested for an exhaustive set of mutually unbiased (in other words, fully complementary) bases of polarization (qubit) states. The average fidelities measured for these states were 0.81(1), well above the 2/3 threshold.

# 3. Teleportation onto freely flying photons

Most applications of quantum teleportation include the subsequent manipulation of the teleported photon. Thus, a freely propagating output state, which is teleported with high fidelity, is strongly desired. In the Innsbruck experiment, however, owing to the probabilistic nature of SPDC, there was also the chance to register a pf1f2 coincidence [Fig. 21(b)], seemingly indicating the preparation of a single photon and the identification of a  $|\psi^{-}\rangle_{12}$ , which could occur unfortunately due to an unwanted event of two-pair emission during the second passage of the UV pulse, with no emission in the first passage. In such a case, no photon propagates to Bob. Thus, in the experiment, a successful teleportation act had to be confirmed by a detection event at Bob's side. Because of this fact, Braunstein and Kimble (1998) classified the experiment as involving a "postselection," and implied that the fidelity of the process therefore was not sufficient. Bouwmeester et al. (1998) pointed out that the situation should be interpreted as reducing the

efficiency of teleportation rather than its quality. Possible solutions (Braunstein and Kimble, 1998; Kok and Braunstein, 2000) could include the discrimination of one-photon and two-photon events at detector  $p$  [Fig. 21(b)], a quantum nondemolition measurement of the photon number in mode 3. It should be noted that if one uses a single-photon source or entangled pairs from a single quantum emitter, e.g., from a quantum dot [cf. Akopian et al. (2006) and Stevenson et al. (2006)], one in principle does not need to worry about the double pair emission of SPDC at least up to the antibunching quality of the source. However, due to the lack of appropriate technology, such a scheme has not been thus far realized.

In the experiment of Pan, Gasparoni, Aspelmeyer, et al. (2003) such problems were basically removed. The scheme was such that a coincident registration of photons at the Bell measurement station was heralding that with a high probability one has a propagating photon carrying the teleported state; see Fig. 21(b). Such a process was called "teleportation into freely propagating photons." The basic idea of this experimental method is that the entangled ancillary pair was provided much more frequently than the photon to be teleported [a similar idea was also used in the teleportation experiment using time-bin entanglement carried out by Marcikic et al. (2003)]. Thus, when a qubit which was to be teleported arrived, the teleportation machinery was almost always ready. Technically, the main idea was to reduce the number of unwanted f1-f2 coincidence counts. This was accomplished by attenuating the beam 1 by a factor of  $\gamma$ , while leaving the intensity in modes 2-3 unchanged. With such an arrangement, a threefold coincidence f1-f2- $p$  occurs with probability  $\gamma p^2$  for a successful teleportation ( $p$  is the probability of having a single pair creation during a SPDC process). With a significantly lower probability  $(\gamma p)^2$  one has spurious coincidences without a photon at Bob's side. Thus, for a sufficiently low  $\gamma$  it is not necessary to actually detect photon 3 to be certain that teleportation occurred. Photon 3 gives us a freely propagating beam of teleported qubits.

To demonstrate a nonconditional teleportation, a series of neutral filters were inserted in mode 1, showing that the probability of a successful teleportation conditioned on an f1-f2-  $p$  threefold coincidence increases with decreasing filter transmission  $\gamma$  (e.g., the observed probability of success was  $0.138 \pm 0.002$  for  $\gamma = 0.05$ ). The average fidelity for the unconditional teleportation for three mutually unbiased bases was  $\sim 0.80(2)$ .

# 4. Teleportation of a qubit carried by a photon of the ancillary EPR pair

It is well known that with standard optical devices (passive linear optics plus detectors) one can measure any observable associated with a single photon. Thus, if the photon carries two qubits, any two-qubit measurement can be performed, including a Bell-state measurement, involving states of two different photon "degrees of freedom," e.g., polarization and path. Thus, as teleportation is from an algebraic point of view a three-qubit operation, and as there is no easy solution for a Bell-state measurement for two photons, each carrying a qubit, one can resort to the following. One can have a scheme in which a single photon carries two qubits, the qubit to be

teleported and one of the qubits of the EPR maximally entangled pair. This effectively boils down to an emulation of the third particle (subsystem) in the process [for such an emulation in the case of GHZ correlations see Zukowski (1991) and the experiment Michler, Weinfurter, and Zukowski (2000)]. However, the fact that one of the particles is emulated does not allow one to teleport a qubit state of an independently arriving particle, and it is difficult to imagine an entanglement swapping process which leaves as a result two spatially separated qubits, previously independently emitted, in a maximally entangled state. Thus, the comparative straightforwardness of a Bell-state measurement has a trade off: the process is not fully versatile, and in some respects does not mirror the original idea.

In the protocol with the emulation, the quantum state to be teleported can be prepared by performing a unitary operation on an additional degree of freedom of one of the EPR particles of the quantum channel. A protocol of this kind has been proposed by Popescu (1995) and was experimentally realized by Boschi et al. (1998) with a teleportation fidelity of 0.85(1). As the protocol does not involve interference of photons from two separate emissions, and as only one EPR pair is manipulated, it avoids many difficulties. Just one SPDC source is needed, and it works with just a one pair-emission process.

The main idea (see the experimental setup in Fig. 23) is to use the spatial and polarization degrees of freedom of photons. One emulates the particle which carries the to be teleported qubit with the use of an additional degree of freedom of an EPR particle sent to Alice. The first step is to produce two photons entangled in their directions of propagation (this will serve as the EPR pair), i.e., entangled in momentum, but each with a well-defined polarization. Thus, one starts with

$$
\frac {1}{\sqrt {2}} \left(\left| a _ {1} \right\rangle_ {1} \left| a _ {2} \right\rangle_ {2} + \left| b _ {1} \right\rangle_ {1} \left| b _ {2} \right\rangle_ {2}\right) \left| H \right\rangle_ {1} \left| V \right\rangle_ {2}. \tag {73}
$$

The area indicated as "EPR source" in Fig. 23 shows how this can be achieved.[57] On the way to Alice, photon 1 is intercepted by the preparer  $P$  who changes the polarization from  $H$  to an arbitrary quantum superposition

$$
\left| \chi \right\rangle_ {1} = \alpha \left| H \right\rangle_ {1} + \beta \left| V \right\rangle_ {1}. \tag {74}
$$

This is the quantum state that Alice will transmit to Bob. The preparer transforms the polarization in both paths  $a_1$  and  $b_1$  in the same way. The total state  $|\Phi \rangle$  of the two photons after his or her action is

$$
| \Phi \rangle = \frac {1}{\sqrt {2}} \left(| a _ {1} \rangle_ {1} | a _ {2} \rangle_ {2} + | b _ {1} \rangle_ {1} | b _ {2} \rangle_ {2}\right) | \chi \rangle_ {1} | V \rangle_ {2}, \tag {75}
$$

which is a formal analogue of the initial state in Eq. (71).

Next, Alice performs a Bell-state-like measurement on the two degrees of freedom of her (single) particle. The four "Bell states" are represented by the following correlated polarization-path states of the photon:

![](images/f8ab1ca146608b61c4a0e392539b6814194c0d3c624a1abed11aae3fe2c0d27b.jpg)  
FIG. 23. Experimental setup for the "two qubit at one subsystem scheme" of quantum teleportation. From Boschi et al., 1998.

$$
\left| \bar {\psi} ^ {\pm} \right\rangle_ {1} = \frac {1}{\sqrt {2}} \left(\left| a _ {1} \right\rangle_ {1} | V \rangle_ {1} \pm \left| b _ {1} \right\rangle_ {1} | H \rangle_ {1}\right), \tag {76}
$$

$$
| \bar {\phi} ^ {\pm} \rangle_ {1} = \frac {1}{\sqrt {2}} (| a _ {1} \rangle_ {1} | V \rangle_ {1} \pm | b _ {1} \rangle_ {1} | H \rangle_ {1}).
$$

The measurement of photon 1 with respect to this basis can in principle be achieved with  $100\%$  success rate. (A photon detection by  $D_{1}$ ,  $D_{2}$ ,  $D_{3}$ , or  $D_{4}$  corresponds directly to a projection onto one of the four Bell states; see Fig. 23.)

Since, in terms of the four single-photon Bell states, one has

$$
\begin{array}{l} \left| \Phi \right\rangle = \frac {1}{2} \left[ \left| \bar {\psi} ^ {+} \right\rangle_ {1} \left(\beta \left| a _ {2} \right\rangle_ {2} + \alpha \left| b _ {2} \right\rangle_ {2}\right) \right. \left| H \right\rangle_ {2} + \left| \bar {\psi} ^ {-} \right\rangle_ {1} \left(\alpha \left| a _ {2} \right\rangle_ {2} \right. \\ + \beta \left| b _ {2} \right\rangle_ {2}) \left| H \right\rangle_ {2} + \left| \bar {\phi} ^ {+} \right\rangle_ {1} \left(\alpha \left| a _ {2} \right\rangle_ {2} - \beta \left| b _ {2} \right\rangle_ {2}\right) \left| H \right\rangle_ {2} \\ + | \bar {\phi} ^ {-} \rangle_ {1} (\beta | a _ {2} \rangle_ {2} - \alpha | b _ {2} \rangle_ {2}) | H \rangle_ {2}, \tag {77} \\ \end{array}
$$

the final step of the protocol is that Alice informs Bob which detector clicked. With this information, Bob can reproduce the initial polarization state by transforming the momentum superposition of photon 2 [see Eq. (77)] into a corresponding polarization state, and applying suitable polarization transformations (following the two bit classical information from Alice). They represent the unitary corrections necessary to put his photons into the polarization state that was set by the preparer at the other EPR photon.

# 5. Teleportation with various physical systems

Each teleportation experiment done thus far has advantages and disadvantages [for a comparison between various methods, see Bouwmeester, Pan, Weinfurter, and Zeilinger (2000)]. Quantum teleportation of continuous-variable states (Furusawa et al., 1998; Braunstein and van Loock, 2005) has the advantage that full Bell-state analysis is possible with linear optics (within the experimental bandwidth). Yet, it is hard to extend to a long-distance case. The unavoidable degradation of squeezed-states sets in during longer-distance transfers. This consequently leads to a rapid lowering of the quality of squeezed-state entanglement. Quantum teleportation using nuclear magnetic resonance (Nielsen, Knill, and Laflamme, 1998) or trapped atoms (Barrett et al., 2004; Chiaverini et al., 2004) has an obvious advantage in that the input quantum state can be teleported with an efficiency of  $100\%$ . Yet, it is difficult (if not impossible) to implement it over long distances.

![](images/0dd6891b01bc6afbdf300f842b9c2b0ff4101655759596b920c450814467da94.jpg)  
FIG. 24 (color). The principle of open-destination teleportation. Adapted from Zhao et al., 2004.

The Innsbruck teleportation technique with its later improvements enables one to aim at a long-distance teleportation (Marcikic et al., 2003; Ursin et al., 2004) and toward more complicated schemes (Zhao et al., 2004; Zhang, Q. et al., 2006). There are other interesting developments. Marcikic et al. (2003) realized a teleportation of qubits at telecommunication wavelengths over a fiber length of  $2\mathrm{km}$ . Adopting Boschi et al.'s protocol, Jin et al. (2010) emulated free-space quantum teleportation over  $16\mathrm{km}$ .

# 6. More-involved teleportations

Open-destination quantum teleportation The so-called open-destination teleportation of Karlsson and Bourennane (1998) is a protocol allowing to transfer a state to one of several potential recipients. It can be decided who gets the state even after the initial to be teleported state  $|\chi \rangle$  is wiped out in a Bell-state measurement. Such a teleportation scheme was experimentally demonstrated for  $N = 3$  by Zhao et al. (2004).

Figure 24 shows the basic scheme. One uses a quantum channel in form of a  $N + 1$  qubit GHZ state, say for  $N = 3$  and for polarization qubits:

$$
\left| \Phi \right\rangle_ {2 3 4 5} = \frac {1}{\sqrt {2}} \left(\left| H \right\rangle_ {2} \left| H \right\rangle_ {3} \left| H \right\rangle_ {4} \left| H \right\rangle_ {5} + \left| V \right\rangle_ {2} \left| V \right\rangle_ {3} \left| V \right\rangle_ {4} \left| V \right\rangle_ {5}\right), \tag {78}
$$

and requires, as always, a transfer of two bits of classical information. The polarization state to be teleported  $|\chi \rangle_{1} = \alpha |H\rangle_{1} + \beta |V\rangle_{1}$  is first encoded into an  $N$ -particle coherent superposition of these GHZ particles. By making a Bell-state measurement on, say, photons 1 and 2, one projects the remaining photons into one of four states. For example., whenever the result of the Bell-state measurement is a  $\psi^{+}$ state, one gets

$$
\frac {1}{\sqrt {2}} \left(\beta | H \rangle_ {3} | H \rangle_ {4} | H \rangle_ {5} + \alpha | V \rangle_ {3} | V \rangle_ {4} | V \rangle_ {5}\right). \tag {79}
$$

The state  $|\chi \rangle$  can be read out at any of the three particles, by performing a suitable projection measurement on  $N - 1$  of them, here on 2, and a unitary transformation dependent of the received two bits of data, which is carried out on one of the GHZ particles.[58] Assume that we want to transfer our

state to particle 5. To this end upon the receipt of information concerning the result of the Bell-state measurement (BSM), the partner 5 must perform on his particle a  $\sigma_{x}$  transformation, which interchanges polarizations  $H$  and  $V$ . The partners 3 and 4 make measurements in the  $|\pm \rangle = (|H\rangle \pm |V\rangle) / \sqrt{2}$  basis. The recipient of the state is informed about the measurement results.[59] Once the recipient gets this additional information, only if there was just one result associated with a projection to  $|- \rangle$ , he or she performs the sign flipping  $\sigma_{z}$  transformation. The state is recovered.

In contrast to the original teleportation scheme, after the encoding operation the destination of teleportation is left open until we perform a polarization measurement ("decoding") on two of the remaining three photons. This implies that, even though photons 3, 4, and 5 are far apart, one can still choose which particle should finally carry the teleported state. No prior agreement on the final destination of the teleportation is necessary.

In the Zhao et al. (2004) experiment, the required four-photon GHZ entanglement was generated (conditional upon joint detection) using the techniques of Secs. IV.D.3, and the pseudo-single photon state to be teleported was in the form of polarization of an attenuated laser beam containing on average 0.05 photons per pulse. They detected fivefold coincidence with a rate of 12 per hour and measured fidelities of teleportation from photon 1 to photon 5 and from photon 1 to photon 4. For  $+ / -$  linear and  $R / L$  circular polarization states, these were  $\sim 0.80(4)$ .

Quantum teleportation of composite two-qubit states-Zhang, Q. et al. (2006) demonstrated a teleportation of two-qubit states with a six-photon interferometer. Suppose Alice wants to send an unknown state of a composite system consisting of qubits 1 and 2:

$$
\begin{array}{l} \left| \chi \right\rangle_ {1 2} = \alpha | H \rangle_ {1} | H \rangle_ {2} + \beta | H \rangle_ {1} | V \rangle_ {2} + \gamma | V \rangle_ {1} | H \rangle_ {2} \\ + \delta | V \rangle_ {1} | V \rangle_ {2} \tag {80} \\ \end{array}
$$

to a distant receiver Bob (Fig. 25). Before teleportation, Alice and Bob share two ancillary entangled-photon pairs (photon pairs 3-5 and 4-6), which are both prepared in a Bell state, say,  $|\phi^{+}\rangle = (|HH\rangle + |VV\rangle) / \sqrt{2}$ . Following the standard teleportation protocol, Alice first teleports the state of photon 1 to photon 5 by consuming the entangled pair 3-5. The result of this step is  $|\chi\rangle_{52}$ . Similarly, Alice can also teleport the state of photon 2 to photon 6 by consuming the entangled pair 4-6. After a successful implementation of the two steps, the original two-qubit state  $|\chi\rangle_{12}$  is teleported to qubits 5 and 6 in  $|\chi\rangle_{56}$ .

The teleportation of two-qubit states was realized by teleporting two photonic qubits individually. Thus, neither the two original qubits nor the teleported qubits have to be in the same place. Such a flexibility is desired in distributed quantum information processing such as quantum telecomputation and quantum state sharing. The method can be easily generalized to teleport a state of an  $N$ -qubit composite system.

![](images/558fa9b63ca860376047272b134d515b747af6ba319e65a896c694fc1a22d402.jpg)  
FIG. 25 (color). Two-qubit quantum teleportation. Adapted from Zhang, Q. et al., 2006.

Zhang, et al. (2006) managed to obtain  $10^{5}$  photon pairs per second from each EPR source. As a result, on average 10 six-photon events per minute were registered. The two-qubit teleportation protocol was implemented for three different initial states  $|X\rangle_{A} = |H\rangle_{1}|V\rangle_{2},|X\rangle_{B} = (|H\rangle_{1} + |V\rangle_{1})(|H\rangle_{2}-$ $i|V\rangle_{2}) / 2$  , and  $|X\rangle_C = (|H\rangle_1|V\rangle_2 - |V\rangle_1|H\rangle_2) / \sqrt{2} = |\psi^{-}\rangle .$  The measured fidelity for  $|X\rangle_A$ $|X\rangle_B$  ,and  $|X\rangle_C$  was 0.86(3), 0.75(2), and 0.65(3), respectively. All the measured fidelities were well beyond the state estimation limit of 0.40 for a twoqubit system [for a derivation of the limit see Hayashi, Hashimoto, and Horibe (2005)].

# C. Entanglement swapping

# 1. Theory

Entanglement swapping (Zukowski, et al., 1993) provides a method of entangling two particles that never interacted or even have no common past. It can also be interpreted as teleportation of entanglement, i.e., teleportation of undefined states of a particle entangled with another subsystem (Bennett et al., 1993). We mention that one of the original motivations of entanglement swapping is the so-called "event-ready detection" of the entangled particles, a concept suggested by Bell (Clauser and Shimony, 1978; Bell, 1987). Entanglement swapping, together with entanglement purification, is a key element of the quantum repeater protocol (Briegel et al., 1998; Dür et al., 1999; see also Sec. VI.F) and opens a way to efficiently distribute entanglement for massive particles (Bose, Vedral, and Knight, 1998).

Consider the arrangement of Fig. 26. We have two EPR sources. Assume that each source emits a pair of entangled photons in a state, say,  $|\psi^{-}\rangle$  so that the total state of the four photons is  $|\Psi\rangle_{1234} = |\psi^{-}\rangle_{12}|\psi^{-}\rangle_{34}$ . While pairs 1-2 and 3-4 are entangled, there is no entanglement of any of the photons 1 or 2 with any of the photons 3 or 4.

Next, one performs a Bell-state measurement on photons 2 and 3. According to the expansion

$$
\begin{array}{l} | \Psi \rangle_ {1 2 3 4} = \frac {1}{2} (| \psi^ {+} \rangle_ {1 4} | \psi^ {+} \rangle_ {2 3} - | \psi^ {-} \rangle_ {1 4} | \psi^ {-} \rangle_ {2 3} \\ - \left| \phi^ {+} \right\rangle_ {1 4} \left| \phi^ {+} \right\rangle_ {2 3} + \left| \phi^ {-} \right\rangle_ {1 4} \left| \phi^ {-} \right\rangle_ {2 3}), \tag {81} \\ \end{array}
$$

![](images/020a626d41153ec0bcc3a21c6e1f3f0db3bbef257e15289705c37df65c2e7e11.jpg)  
FIG. 26. Principle of entanglement swapping. From Pan et al., 1998.

this measurement always projects photons 1 and 4 also onto a Bell state. For example, if the result of the Bell-state measurement of photons 2 and 3 is  $|\psi^{-}\rangle$ , then the resulting state for photons 1 and 4 is also  $|\psi^{-}\rangle$ . In all cases, photons 1 and 4 emerge entangled despite the fact that they never interacted in the past. In Fig. 26, entangled particles are indicated by the same degree of darkness of the lines. Note that particles 1 and 4 become entangled after the Bell-state measurement on particles 2 and 3. Without knowing which result of the BSM measurement occurred, however, the state of photons 1 and 4 would remain maximally mixed.

Given an ideal arrangement with sources that emit only a single pair of entangled photons each, the process of entanglement swapping also gives a means to generate event-ready entanglement. Namely, as soon as Alice completes the Bell-state measurement on particles 2 and 3, we know that photons 1 and 4 are on their way, ready for detection in an entangled state. In this way, one has the possibility to perform an event-ready test of Bell's inequality (Bell, 1987; Zukowski, et al., 1993). For a further discussion on event-ready entanglement, see Sec. VII.B.1.

# 2. First experimental demonstration

The above scheme was realized using an SPDC source as shown in Fig. 27, by Pan et al. (1998). As in the Innsbruck teleportation experiment, only the antisymmetric Bell state  $|\psi^{-}\rangle_{23}$  was detectable in this Bell-state measurement. After such a detection event, signaled by a coincidence behind the BS, according to the entanglement-swapping rules, photon 1 and 4 is projected into the same entangled state  $|\psi^{-}\rangle_{14}$ . This entanglement was tested by analyzing the polarization correlations between photons 1 and 4 conditioned on coincidences between the detectors of the Bell-state analyzer. When varying the analysis angle  $\Theta$  for the photons going to detector  $D_4$ , the coincidences with  $D_1^+$  and  $D_1^-$  should follow two complementary sine curves in dependence on  $\Theta$ . The observed sinusoidal behavior (the interference pattern) of the coincidence rates had a visibility of 0.65(2), which clearly surpasses the 0.5 limit for a classical interference for coincidence measurements. A later experiment (Pan et al., 2001) achieved a visibility of  $\sim 0.84$ , which is sufficient for violating a Bell inequality (the threshold is 0.71) for photons 1 and 4. Further advancements were achieved by Jennewein et al. (2001) by implementing a 2-state Bell analyzer. Using a fiber coupler, an ideal spatial mode overlap was obtained. A Bell inequality, for measurements on photons 1 and 4, was violated by the factor of 1.211(45), i.e., by 4.6 standard deviations.

![](images/e994ab3fbcb89b59e28fbe4d83dc174af5f00c65c296691ed4eef5cec30a30b3.jpg)  
FIG. 27. Experimental setup of entanglement swapping. The generation scheme for photon pairs 1-2 and 3-4, and the Bell-state measurement identifying the  $|\psi^{-}\rangle_{23}$  state is identical as in the Innsbruck teleportation experiment. The Bell-state measurement on photons 2 and 3 projects the two remaining photons 1 and 4 onto an entangled state. To analyze their entanglement, one looks at coincidences between detectors  $\mathrm{D1^{+}}$  and D4, and between detectors  $\mathrm{D1^{-}}$  and D4, for different polarization angles  $\Theta$ . Note that, since the detection of coincidences between detectors  $\mathrm{D1^{+}}$  and D4 and  $\mathrm{D1^{-}}$  and D4 are conditioned on the detection of the  $|\psi^{-}\rangle_{23}$  state (which happens whenever one has a coincidence behind the beam splitter), one in fact is looking for fourfold coincidences to signify the event of entanglement swapping. Narrow bandwidth filters (F) are positioned in front of each detector to make photons from different emissions indistinguishable. From Pan et al., 1998.

A test of Bell's inequality involving swapping of entanglement has some appealing features, aside from being an "event-ready" one.[60] In addition, it can be performed in a delayed-choice mode, as suggested by Peres (2000) and realized by Jennewein et al. (2001). In such an experiment, one delays the instant of time at which the Bell-state measurement is performed on photons 2 and 3. Thus, entanglement between photons 1 and 4 in subsembles associated with a specific result for 2 and 3 is revealed, a posteriori, after they have already been measured and may no longer exist. Recently, an experiment with active switching and spacelike separation of the relevant decision was carried out by Ma et al. (2011).

# 3. Other experiments on entanglement swapping

Recently, entanglement-swapping experiments with an increased complexity involving pairs of entangled photons have been demonstrated: multistage entanglement swapping (Goebel et al., 2008) and multiparticle entanglement swapping (Lu, Yang, and Pan, 2009).

If one aims to build a quantum repeater (Briegel et al., 1998, see also Sec. VI.F), one has to achieve entanglement swapping with synchronized entangled-photon sources among all distributed segments. It thus requires stable interference between two independently emitted photons. Kaltenbaek et al. (2006), Yang et al. (2006), and

Kaltenbaek et al. (2009) successfully realized the necessary technique using synchronized fs lasers to solve the above problem. Kaltenbaek et al. (2006)[61] reported an active synchronization method: the two independent fs pulsed lasers pumping the two separate SPDC sources were electronically synchronized to emit pulses at the same time. To enable interference the two photons registered behind the BS cannot be distinguished in any way. To this end, the now standard methods suggested in Zukowski, Zeilinger, and Weinfurter (1995) and discussed in Sec. IV.D were used.

The entangled photons generated via the usual SPDC, as used in the above experiments, have broadband linewidth (usually on the order of several THz) determined by the phase-matching condition. Thus, there the challenge was to achieve sufficiently sharp synchronization of the photons. Halder et al. (2007) took a different approach to achieve entanglement swapping by a precise time measurement. The photon detector used in the experiment was a niobium nitride superconducting single-photon detector with a time resolution of  $74~\mathrm{ps}$ . The photons were filtered using 10 pm-bandwidth filters, which corresponds to a coherence time of  $350~\mathrm{ps}$  well above the temporal resolution of the detectors. Hence, ultracoincidence photon timing could be obtained, and pulsed sources could be replaced by continuous-wave sources, which do not require any synchronization.

The passive filtering used by Halder et al. is, however, extremely inefficient (the  $10\mathrm{pm}$ -filter transmits  $< 1\%$  only of all down-converted photons). Thus, a very bright narrowband entangled-photon source is highly desirable. A recent experiment (Bao et al., 2008) realized such a source with a linewidth of  $9.6\mathrm{MHz}$ . Because of the long coherence time, synchronization for such sources is unnecessary, while coincidence measurements with time resolution of several nanosecond with current commercial single-photon detectors will be sufficient to see interference of photons originating from independent sources.

Entanglement swapping provides a tool to entangle qubits without direct interaction. An interesting application is that we can entangle distant, independent matter qubits through photon-mediated entanglement swapping. Imagine we start with two entangled atom-photon pairs (Blinov et al., 2004; Volz et al., 2006). By implementing a Bell-state measurement of the two photons, we can project the two atomic qubits into an maximally entangled state. Proof-of-principle experiments have been performed by Moehring et al. (2007) who entangled two trapped atomic ions separated  $1\mathrm{m}$  apart using entanglement swapping exploiting interference of photons emitted by the ions, and by Yuan et al. (2008) in atomic

ensembles. These experiments still suffer from low success probability and imperfect state fidelity. For instance, the Moehring et al. (2007) experiment had a success probability of  $3.6 \times 10^{-9}$  and the fidelity of the states of the entangled ions was 0.63(3). The ion-ion entanglement fidelity was improved to be 0.81 in a later experiment by Matsukevich et al. (2008). Together with the high efficiency of the measurement of the quantum state of an ion, this high fidelity allowed one to observe a Bell-inequality violation with an efficiency high enough to close the detection loophole.

# D. Beating noisy environment

So far, significant experimental progress has been achieved in small-scale realizations of quantum information processing. However, interesting challenges arise in bringing quantum information processing to technologically useful scales. This is primarily due to the unavoidable decoherence $^{63}$  caused by a coupling between the quantum system and the environment. In quantum communication, it is the noisy quantum channel that degrades the quality of entanglement between particles the further they propagate. Yet, the implementation of any of the quantum communication schemes (as reviewed above) over large distances requires that two distant parties share entangled pairs with high quality. Similarly, during quantum computation the coherence of a quantum system also decreases exponentially with an increasing operation time, consequently leading to failure in the quantum computation. It is therefore necessary to overcome decoherence in any realistic large-scale realization of quantum information processing.

An important tool to overcome the noise in the quantum communication channel is entanglement distillation, concentration, and purification, proposed by Bennett, Bernstein, Popescu, and Schumacher (1996); Bennett et al. (1996); Bennett, DiVincenzo, Smolin, and Wootters (1996); and Deutsch et al. (1996). A linear-optical implementation of entanglement purification was suggested and experimentally demonstrated by Pan, Simon, Brukner, and Zeilinger (2001) and Pan, Gasparoni, Ursin et al. (2003). Quantum repeater (Briegel et al., 1998; Dür et al., 1999), based on entanglement purification and entanglement swapping, would provide an efficient way to generate highly entangled states between two distant locations. Remarkably, the quantum repeater protocol tolerates general errors on the percent level, which is reachable using entanglement purification based on linear optics (Pan, Simon, Brukner, and Zeilinger, 2001; Pan, Gasparoni, Ursin et al., 2003). It has been shown that, despite of local noise and/or errors on the percent level, the quantum repeater can be used to establish a private and/or secure quantum communication channel (Aschauer and Briegel, 2002). A study (Dür and Briegel, 2003) showed that entanglement purification can also be used to increase, by several orders of magnitude, the quality of logical operations between two qubits. In essence, this implies that the threshold for tolerable errors in quantum computation is within reach using entanglement purification and linear optics.

# 1. Entanglement distillation and concentration

Entanglement concentration aims to obtain with a nonzero probability a higher entanglement from pure states with a lower entanglement. There are two methods to achieve this. The first is the so-called Procrustean method (Bennett, Bernstein, Popescu, and Schumacher, 1996). It requires that the photon pairs are all in a pure nonmaximally entangled state, say,  $|\Psi \rangle_{\mathrm{nonmax}} = \alpha |H\rangle |V\rangle + \beta |V\rangle |H\rangle$ , where  $\alpha$  and  $\beta$  are two known amplitudes. In this case, the scheme only involves local filtering operations (Gisin, 1996; Horodecki, Horodecki, and Horodecki, 1996) on single pairs. Second, the Schmidt decomposition scheme (Bennett, Bernstein, Popescu, and Schumacher, 1996) works for photon pairs that are all in a pure but unknown nonmaximally entangled state  $|\Psi \rangle_{\mathrm{nonmax}}$ . In practice, this scheme is more difficult to implement as it requires simultaneous collective measurements on many photons.

Kwiat et al. (2001) used the Procrustean method to demonstrate experimentally distillation of maximally entangled states from nonmaximally entangled inputs. Using partial polarizers, they performed a filtering process to maximize the entanglement of pure polarization-entangled photon pairs generated by SPDC. The method was also applied to initial states that were partially mixed [see also Wang et al. (2006) for a later experiment]. After filtering, the distilled states show violations of a Bell's inequality, while the initial states do not have this property. For some special two-qubit mixed states, Verstraete, Dehaene, and DeMoor (2001) constructed the optimal local filtering operations for distilling entanglement from the mixed state, with an experimental demonstration done by Wang et al. (2006).

The Schmidt decomposition scheme becomes practically feasible after the proposal of a linear-optical implementation of entanglement concentration (Yamamoto, Koashi, and Imoto, 2001; Zhao, Pan, and Zhan, 2001). Two independent experiments (Yamamoto et al., 2003; Zhao, Yang, Chen, Zhang, Pan, 2003) were reported for linear-optical entanglement concentration.

# 2. Entanglement purification

The underlying idea of entanglement purification is that, by using local operations and classical communication only, to extract from multiple copies of imperfect states (arbitrary mixed states) fewer copies of entangled state asymptotically to near-unity fidelity. Schemes of entanglement purification ware introduced by Bennett, Bernstein, Popescu, and Schumacher (1996) and Bennett, DiVincenzo, Smolin, and Wootters, 1996; Deutsch et al. (1996), as illustrated in Fig. 28(a). However, a drawback of these theoretical schemes is that they require CNOT operations. In the context of long-distance quantum communication, the probability of errors caused by the CNOT operation must be within a few percent, which, unfortunately, is somewhat beyond the current experimental techniques. A more feasible purification scheme was proposed by Pan, Simon, Brukner, and Zeilinger (2001). They showed that purification does not have to entirely rely on CNOT operations. In some cases, a simple linear-optical element, a polarizing beam splitter, suffices [see Fig. 28(b)].

![](images/fea0b346daedd38e28a79f279edf7ca11bd5846505cf44c252d2d9290b2b2a13.jpg)

![](images/d77cdb335e0606df60df92d7811e22f9ce062145600b026d678eba6e0b6023cb.jpg)  
FIG. 28 (color). Scheme of entanglement purification by Bennett, Bernstein, Popescu, and Schumacher (1996); Pan, Simon, Brukner, and Zeilinger (2001). (a). Two poorly entangled (source and target) pairs are initially shared by Alice and Bob. They both perform a (local) CNOT operation on the two particles at their hands, measure the particles belonging to the target pair in the  $0/1$  basis, and compare the measured results via classical communication. If the results are the same, then the remaining pair will have a higher degree of entanglement than the original two pairs. In this case, they keep the source pair. In the case of obtaining opposite results, they discard it. By repeating the same procedure, always starting from the pairs produced in the former purification step, it is possible to distill pairs of arbitrarily high entanglement quality [for more details, see Bennett, Bernstein, Popescu, and Schumacher (1996)]. (b). An alternative and more feasible scheme which does not require a CNOT operation but only polarizing beam splitters. The PBS transmits horizontal  $(|H\rangle)$ , and reflects vertical  $(|V\rangle)$ , polarization. By selecting only those events for which there is one, and only one, photon in each output mode of the PBS, one can project two photons input from different spatial modes into the subspace spanned by  $|H\rangle |H\rangle$  and  $|V\rangle |V\rangle$  (for more details see text). Adapted from Pan, Simon, Brukner, and Zeilinger, 2001.

The linear-optical purification scheme [shown in Fig. 28(b)] will be presented here using a specific example. Our initial state is

$$
\rho_ {a b} = F \left| \phi^ {+} \right\rangle_ {a b} \left\langle \phi^ {+} \right| + (1 - F) \left| \psi^ {-} \right\rangle_ {a b} \left\langle \psi^ {-} \right|, \tag {82}
$$

where  $|\psi^{-}\rangle_{ab}$  is an unwanted admixture. The subscripts  $a$  and  $b$  indicate the particles at Alice's and Bob's locations, respectively.

Alice and Bob share a large number of pairs described by  $\rho_{ab}$ . They start by picking at random two such pairs. Each of them superimposes their photons on a PBS. An essential step in the purification scheme is to select those cases for which there is exactly one photon in each of the four spatial output modes. We shall refer to them as "four-mode cases." This corresponds to a projection onto the subspace in which two photons at the same experimental location (Alice's or Bob's) have equal polarization. This is similar to the bilateral CNOT operation of the original scheme. Note that the polarizations at two different locations do not have to be the same. After performing the purification procedure (selection of four-mode

cases, measurements in modes a4 and b4 in the  $+ / -$  basis, and local operations conditional on the measurement results), Alice and Bob will finally create a new ensemble described by the density operator

$$
\rho_ {a b} ^ {\prime} = F ^ {\prime} \left| \phi^ {+} \right\rangle_ {a b} \left\langle \phi^ {+} \right| + (1 - F ^ {\prime}) \left| \psi^ {-} \right\rangle_ {a b} \left\langle \psi^ {-} \right|, \tag {83}
$$

with a larger fidelity  $F' = F^2 / [F^2 + (1 - F)^2]$  (for  $F > 1/2$ ) of pairs in the desired state than before the purification.

Though it seems that only a rather special example, single bit-flip error, has been considered, the same method actually applies to the arbitrary mixed states  $\rho_{ab}$ , provided that they contain a sufficiently large fraction  $F > 1/2$  of photon pairs in a maximally entangled state. This works as follows: one can first purify away single bit-flip errors; phase errors can then be easily transformed into bit-flip errors by a  $45^{\circ}$  polarization rotation and treated in a subsequent purification step.

An experimental demonstration of the entanglement purification scheme has been reported by Pan, Gasparoni, Ursin et al. (2003). The setup is shown in Fig. 29. For each run two pairs of an initial, mixed state (82) were prepared with SPDC and half-wave plates. Next, the two photons at Alice's (Bob's) side in the mode a1-a2 (b1-b2) were interfered at a PBS. After the four photons' passage through the two PBS, and under the condition that one detects one and only one photon polarized along the  $\pm$  basis in each of the modes a4 and b4, the two photons in the mode a3-b3, according to quantum mechanical calculations, have a higher fidelity to be in the pure entangled state. There is, however, a complication in the actual experiment. Owing to the probabilistic nature of SPDC, with a probability of the same order of magnitude, two photon pairs can be emitted into a one mode pair. Fortunately, as pointed out by Simon and Pan (2002), this does not ruin the purification protocol. Simply, for the higher-order emissions causing a four-mode detection case the photons in a3-b3 are projected, due to interference, to the entangled state. The scheme requires a fine stabilization of the phases between the amplitudes of the four-mode contributions.

In the first purification experiment, a mixed state as in Eq. (82) with fidelity of  $F = 0.75$  was prepared. The preparation was positively tested by measuring fractions both in the  $H / V$  and in the  $+ / -$  bases, as shown in Figs. 30(a) and 30(b), respectively.

The measured results in Figs. 30(c) and 30(d) show a significant improvement of entanglement fidelity to the value of  $F' = 0.92 \pm 0.01$  for the purified subensemble. In a second experiment, entanglement purification was performed for a mixed state with  $F = 0.80$ . After purification, the observed entanglement fidelity for the subensemble in modes a3 and b3 was about  $0.94 \pm 0.01$ . For each initial mixed state the purification scheme worked. The two-photon interference visibility of the original mixed states was  $50\%$  and  $60\%$ , respectively. In a single purification step it was increased to  $84\%$  and  $88\%$ . This is well above the threshold to violate a Bell inequality. In a subsequent development, a Bell experiment with purified states was performed (Walther, Resch, Brukner et al., 2005). The states of initially poorly entangled photons, below thresholds to violate a Bell-CHSH inequality, were prepared by a controllable decoherence. After a

![](images/8e529f177e1a794305c91446d9680e06f346c0879146c333465e587719c100db.jpg)  
FIG. 29. Experimental setup for entanglement purification. UV laser pulses pass through a BBO crystal twice to produce two polarization-entangled photon pairs, i.e., pair 1 in a1-b1 and pair 2 in a2-b2. Four compensators (Comp.) are used to offset the birefringent effect caused by the BBO crystal during parametric down-conversion. The photons in modes b1 and b2 pass through a half-wave plate  $(\lambda /2)$  to simulate a noise that reduces the entanglement quality. Next, the two pairs are sent via local PBSs. This results in entanglement purification. Adjusting the positions of the delay mirrors  $\Delta 1$  and  $\Delta 2$  tunes the optical paths in such a way that the photons at local measurement stations arrive at their PBS simultaneously. Detections of exactly one photon in each of the four outputs (a3, a4, b3, and b4) behind a  $45^{\circ}$  polarizer (Pol.) lead to a successful purification act. From Pan, Gasparoni, Ursin et al., 2003.

purification,  $S_{\mathrm{Bell}} = 2.29 \pm 0.13$  was measured. This violates the inequality by 2.2 standard deviations.

If one estimates the accuracy of local operations at the used PBSs, one obtains theoretical values of fidelity better than  $98\%$  for the process itself, or equivalently an error probability of at most  $2\%$ . Entanglement purification with such a high quality is important not only for quantum communication, but also for quantum computation. With linear optics the accuracy of single-photon operations on polarization and spatial degrees of freedom can be extremely high (a typical accuracy of commercial products is  $\sim 10^{-3}$ ). These facts, together with the experimental realization of high-fidelity teleportation (Pan, Gasparoni, Aspelmeyer, et al., 2003), imply that the threshold of tolerable error rates for quantum repeaters could be achieved.

Although the efficiency of this entanglement purification scheme (Pan, Simon, Brukner, and Zeilinger, 2001) is in theory  $1/4$ , the actual success probability in the experiment (Pan, Gasparoni, Ursin, et al., 2003) was much lower as it relied on the SPDC to probabilistically create two pairs of entangled photons, thus only a small fraction of photons

![](images/6bd91a87eecf7f7a5de799a4188ba4f5c719302f8d9610ffb1c758badd342bfe.jpg)

![](images/5abba63ac5a709bcf0783b24a0a96f443271ad1f5955d2a99bcf3489d5169699.jpg)

![](images/b2574dfde7d813adea43044fff5adf3ab06e5cf0130899c0e39466766e77279e.jpg)  
FIG. 30. Experimental results. (a), (b) Measured fractions, in the  $H / V$  and in the  $+ / -$  bases, for the original mixed state. (c), (d) Measured fractions for the purified state in modes a3 and b3, in the same pair of bases. A comparison of the fractions in (a) and (b), with the results shown in (c) and (d) indicates entanglement purification. From Pan, Gasparoni, Ursin et al., 2003.

![](images/9c4b0883989ef8af30b32a7d9987487f346d118d19368fd6597c05fa6999a9d3.jpg)

actually went through the purification system. In addition to the low efficiency, another weakness of this experiment is that, due to double pairs emission events in SPDC, a phase stabilization was required. This is unfeasible in long-distance quantum communication. Considering possible applications of entanglement purification, these two problems can be solved by using entangled-photon pairs deterministically generated using quantum dots or other emitters.

# E. Long-distance entanglement distribution

The ultimate goal of quantum communication is to work at long distances. A summary of the recent experimental progress is listed in Table I [the distance for the distribution of entanglement in optical fibers was extended from  $50~\mathrm{km}$  (Marcikic et al., 2004) to the order of  $\sim 100\mathrm{km}$  (Honjo et al., 2007; Hübel et al., 2007; Takesue et al., 2007)].

For real life applications of fiber-based quantum communication, one has to face several major limiting factors including photon loss and photon detection noise (mainly dark counts). For quantum key distribution, the rate for dark counts, etc., for a given photon detector is constant, while the key rate decreases with increasing fiber length. Therefore, the signal-to-noise ratio decreases exponentially with the length of the fiber. At a certain fiber length, the signal-to-noise ratio is so low that secure keys cannot be generated. A further extension of the distance over which reliable quantum communication is possible requires detectors of lower noise, fiber links of lower loss, quantum communication systems of faster working rates, etc. In summary, the present-day technology puts a strong limitation on the distance for practical fiber-based

quantum communication. $^{64}$  This underlines the necessity of developing quantum repeaters.

A promising way to realize long-distance quantum communication is to exploit satellite-based free-space distribution of single photons, or entangled-photon pairs (Aspelmeyer, Jennewein, et al., 2003). In the scheme, the photonic quantum states are sent from Earth's surface and reflected from one satellite to another, and finally sent back to the Earth. Since the effective thickness of the atmosphere is on the order of  $5 - 10\mathrm{km}$ , while the outer space photon loss and decoherence is negligible, with the help of satellites one can achieve global free-space quantum communication, provided the quantum states survive the passage through the aerosphere.

Along these lines, an important experimental progress has been made in the free-space transmission of attenuated laser pulses [over  $23.4\mathrm{km}$ , see Kurtsiefer et al. (2002); over  $144\mathrm{km}$ , see Schmitt-Manderbach et al. (2007)], of triggered single photons from entangled-photon pairs [over  $7.8\mathrm{km}$ , see Resch et al. (2005); and over  $144\mathrm{km}$ , see Ursin et al. (2007)], of entangled-photon pairs [over  $144\mathrm{km}$ , see Fedrizzi et al. (2009)], and distribution of entangled-photon pairs to different locations [over  $600\mathrm{m}$ , see Aspelmeyer et al. (2003); over  $13\mathrm{km}$ , see Peng et al. (2005), see Table I for a summary].

More recently, a 144-km free-space link was built between two Canary Islands and used for transmission of one photon of an entangled pair (Ursin et al., 2007), and later, both photons (Fedrizzi et al., 2009). The final photon states were found to preserve excellent, noise-limited fidelity, even though they experienced extreme attenuation due to mainly turbulent atmospheric effects. The total channel loss of  $64\mathrm{dB}$  corresponded to the estimated attenuation regime for a two-photon satellite quantum communication scenario. The entanglement of the received two-photon states was confirmed by violating the CHSH inequality by more than 5 standard deviations. From a fundamental point of view, this means that the photons are subject to virtually no decoherence during their  $0.5\mathrm{ms}$  long flight through air. For those aiming at a world-wide quantum communication this is an encouraging development. The photon-pair flight time of  $\sim 0.5\mathrm{ms}$

TABLE I. Summary of some recent experimental advances on entanglement distribution over long distances. For the details on different settings, see the text.  $S$  refers to the Bell-CHSH parameter.  $V$  refers to the single-photon transmission and visibility of the interference.  

<table><tr><td>Year</td><td>Reference</td><td>Distance Via free-space</td><td>S/Visibility</td><td>Rate (Hz)</td></tr><tr><td>2003</td><td>Aspelmeyer, et al.(2003)</td><td>600 m</td><td>S = 2.41(10)</td><td>&gt;15</td></tr><tr><td>2005</td><td>Resch, et al. (2005)</td><td>7.8 km</td><td>S = 2.27(2)</td><td>84</td></tr><tr><td>2005</td><td>Peng, et al. (2005)</td><td>13 km</td><td>S = 2.45(9)</td><td>150</td></tr><tr><td>2007</td><td>Ursin, et al.(2007)</td><td>144 km</td><td>S = 2.508(37)</td><td>20–40</td></tr><tr><td>2009</td><td>Fedrizzi, et al. (2009)</td><td>144 km</td><td>S = 2.612(114)</td><td>0.071</td></tr><tr><td></td><td></td><td>Via optical fiber</td><td></td><td></td></tr><tr><td>2004</td><td>Marcikic, et al. (2004)</td><td>50 km</td><td>S = 2.185(12)</td><td>5</td></tr><tr><td>2007</td><td>Takesue, et al. (2007)</td><td>60 km</td><td>V = 75.8%</td><td>0.3</td></tr><tr><td>2007</td><td>Honjo, et al. (2007)</td><td>100 km</td><td>V = 81.6%</td><td>1.4</td></tr></table>

represents the longest lifetime of photonic Bell states reported so far.

# F. Quantum memory and quantum repeaters

We have shown that entanglement purification enables one to overcome the degradation of the quality of photon entanglement. Still, a major drawback of schemes for communication between distant nodes is the exponential scaling of the error probability with the length of the connecting channels. The quantum repeater protocol (Briegel et al., 1998; Dur et al., 1999) provides a blueprint of a general framework to remedy this problem by nesting entanglement purification and swapping steps. Once constructed, it would enable one to establish high-quality long-distance entanglement with resources increasing only polynomially with transmission distance.

A quantum memory for single photons, with the ability of interconverting between stationary and flying qubits (see Sec. VI.F.2), is a crucial element in the quantum repeater scheme. There are several candidates for localized qubits. For instance, one may use atomic internal states to store local information. Mapping between the atomic and photonic qubits requires a strong coupling between atoms and photons via high-finesse cavities (Raimond, Brune, and Haroche, 2001; Leibfried et al., 2003; Walther et al., 2006) or initial atom-photon entanglement together with entanglement swapping. Below we focus on the atomic-ensemble based schemes [Duan et al. (2001); Duan, Cirac, and Zoller (2002); Chen et al. (2007); Jiang, Taylor, and Lukin (2007); Zhao et al. (2007); see also Sanguard et al. (2009) for a review].

We emphasize that quantum memories have applications not only in long-distance quantum communication, but they also provide a route to a more efficient multiphoton entanglement (see Sec. IV.D) or linear-optics quantum computing (see Sec. VII). So far, the majority of the reported multiphoton interferometry experiments face the problem of random arrivals of SPDC photon pairs. Thus, scalability of this approach is questionable. Given a quantum repeater, ideally with long storage time, high writing, and retrieval efficiencies,[65] the randomly generated SPDC photon pairs

can be stored and synchronized with the arrival of other photon pairs. This would, for instance, enable efficient generation of multiphoton states in a time which increase only polynomially with number of involved qubits.

# 1. Quantum repeater protocol

In classical communication, the problem of exponential attenuation can be overcome by using repeaters at certain points in the channel. They amplify the signal and restore it to its original shape. In analogy to fault-tolerant quantum computing (Preskill, 1998; Nielsen and Chuang, 2000), the quantum repeater proposal (Briegel et al., 1998; Dur et al., 1999) is a cascaded entanglement purification protocol for communication systems.

The quantum repeater protocol comprises three elements: (i) A method for creation of entanglement between particles at distant nodes, which uses auxiliary particles at intermediate "connection points" and a nested purification protocol. (ii) Entanglement purification, even with imperfect means. (iii) A protocol for which the time needed for entanglement creation scales polynomially, whereas the required material resources per connection point grow only logarithmically with the distance, as show in Fig. 31.

Here we describe a scheme for the physical realizations of a quantum repeater which has been proposed by Duan, Lukin, Cirac, and Zoller (Duan et al., 2001). The ensembles suggested atomic ensembles as local memory qubits. They have a collectively enhanced coupling to light, even without the aid of high-finesse cavities. The scheme incorporates entanglement swapping, built-in entanglement purification, and quantum memory.

Figure 32 is a schematic of a setup for entangling two atomic ensembles (optically thick atomic cells of  $N_{a}$  identical atoms), L and R, which are spatially separated within the channel attenuation length. A pair of metastable lower states  $|g\rangle$  and  $|s\rangle$  can correspond to hyperfine or Zeeman sublevels of electronic ground states of alkali atoms. Long lifetimes for relevant coherences in such systems have been observed

![](images/86a30e20286f9c563a732a4718c2d8dbda161468d5dd2ec1cc9d7920b8df628c.jpg)

![](images/e17ce8f2671a31d9bcbe1b429397366daab26e85ebe9ec0a4efd446e781105fc.jpg)

![](images/7bd570eeeaaff0df5fd67af1d207ca335ec7bd8d5796428504cc7243d609d0f9.jpg)  
FIG. 31 (color online). Quantum repeater scheme. (a) Creation of a sequence of entangled pairs. (b) Nested purification protocol which combines the methods of entanglement swapping and purification, assisted with repeated creation of auxiliary pairs. (c) Purification of entangled pairs stored in distant locations. Adapted from Briegel et al., 1998.

both in a room-temperature dilute atomic gas (Phillips et al., 2001) and in a sample of cold trapped atoms (Liu et al., 2001).

All the atoms are initially prepared in the ground states  $|g\rangle_{i}$ . A sample is illuminated by a short, off-resonant laser pulse that induces Raman transitions into states  $|s\rangle_{i}$ . Particularly important is the forward-scattered Stokes light (the signal mode  $\hat{a}$ ). It is uniquely correlated with the excitation of the symmetric collective atomic mode  $\hat{S} \equiv (1 / \sqrt{N_a})\sum_i|g\rangle_{it}\langle s|$ , where the summation is taken over all the atoms. The light-atom interaction generates, after the interaction time  $t_\Delta$ , a two-mode ( $\hat{a}$  and  $\hat{S}$ ) squeezed state (Braunstein and van Loock, 2005), with the squeezing parameter  $r_c$  proportional to  $t_\Delta$ . If  $t_\Delta$  is very small, the two-mode squeezed state can be written in the perturbative form

$$
| \zeta \rangle = | 0 _ {a} \rangle | 0 _ {p} \rangle + \sqrt {p _ {c}} \hat {S} ^ {\dagger} \hat {a} ^ {\dagger} | 0 _ {a} \rangle | 0 _ {p} \rangle + O \left(p _ {c}\right), \tag {84}
$$

where  $p_c = \tanh^2 r_c \ll 1$  is the small excitation probability and  $O(p_c)$  represents the terms with more excitations, whose probabilities are equal or smaller than  $p_c^2$ . The Hilbert space

![](images/8bbe0b0d59bfb25786ef141c4e7c0f1eca1c6aab366a86daf1a3d6184c54cacd.jpg)  
FIG. 32 (color). Schematic of a setup for generating entanglement between the two atomic ensembles L and R in the DLCZ scheme. The inset shows the relevant level structure of the atoms in the ensemble with the ground state,  $|g\rangle$ , the metastable state for storing a qubit,  $|s\rangle$  and the excited state,  $|e\rangle$ . The transition  $|g\rangle \rightarrow |e\rangle$  is coupled by a classical laser light, with the Rabi frequency  $\Omega$ . The forward-scattered Stokes light comes from the transition  $|e\rangle \rightarrow |s\rangle$ . An off-resonant coupling with a large detuning  $\Delta$  is assumed. Adapted from Duan et al., 2001.

vectors  $|0_{a}\rangle$  and  $|0_{p}\rangle$  are, respectively, the atomic and photonic vacuum states with  $|0_{a}\rangle \equiv \bigotimes_{i}|g\rangle_{i}$ . For a large  $N_{a}$ , the collectively enhanced signal-to-noise ratio may strongly boost the efficiency of the scheme.

This setup enables one to generate entanglement between two distant ensembles, L and R, using the configuration shown in Fig. 32. If two laser pulses excite both ensembles simultaneously, the whole system is described by the state  $|\zeta \rangle_{L} \otimes |\zeta \rangle_{R}$ , where  $|\zeta \rangle_{L}$  and  $|\zeta \rangle_{R}$  are given by Eq. (84). The subscripts L and R denote the respective cells [in Eq. (84) one should add such subscripts to all mathematical objects]. The forward-scattered Stokes signal from both ensembles is combined at the BS and a photodetector click in either D1 or D2 measures the combined radiation from two samples,  $\hat{a}_{+}^{\dagger}\hat{a}_{+}$  or  $\hat{a}_{-}^{\dagger}\hat{a}_{-}$  with  $\hat{a}_{\pm} = (\hat{a}_L \pm e^{i\varphi}\hat{a}_R) / \sqrt{2}$ . The symbol  $\varphi$  denotes an unknown difference of the phase shifts in the two channels. Depending on which detector clicks, one applies  $\hat{a}_{+}$  or  $\hat{a}_{-}$  to the whole state  $|\zeta \rangle_{L} \otimes |\zeta \rangle_{R}$ . The resulting projected state of the ensembles, L and R, is nearly maximally entangled. It reads [we neglect  $O(p_c)$  terms]

$$
\left| \Psi_ {\varphi} \right\rangle_ {L R} ^ {\pm} = \left(\hat {S} _ {L} ^ {\dagger} \pm e ^ {i \varphi} \hat {S} _ {R} ^ {\dagger}\right) / \sqrt {2} \left| 0 _ {a} \right\rangle_ {L} \left| 0 _ {a} \right\rangle_ {R}. \tag {85}
$$

For each round, the probability for getting a click is given by  $p_c$ . Thus, we need to repeat the process about  $1 / p_c$  times to warrant a successful preparation of entanglement. The average preparation time is given by  $T_0 \sim t_{\Delta} / p_c$ .

The entanglement generation (as well as entanglement connection) in the DLCZ scheme is based on single-photon interference at photodetectors,[67] which requires a stable long-distance interferometric stability. The fluctuations of the relative phase  $\varphi$  caused by the environment would wash out the coherence (i.e., entanglement) in Eq. (85). For instance, to maintain path-length phase stability at the level of  $\lambda / 10$  ( $\lambda$  is the wavelength) for single photons, typically of  $\lambda \sim 1\mu \mathrm{m}$ , generated from atomic ensembles (Eisaman et al., 2005) requires a precise control of timing jitter at a subfemtosecond level, which is almost experimentally impossible (Holman et al., 2005). For more detailed analysis on the phase-stability problem of the DLCZ scheme, see Chen et al. (2007).

The phase-stability problem can be overcome by interfering two photons, one coming from each remote ion or atom in a cavity (Bose et al., 1999; Browne, Plenio, and Huelga, 2003; Feng et al., 2003; Simon and Irvine, 2003), which was experimentally implemented by Maunz et al. (2007) and Moehring et al. (2007). A robust implementation of a quantum repeater using atomic ensembles was proposed by Chen et al. (2007); Jiang, Taylor, and Lukin (2007); and Zhao et al. (2007). With the help of two-photon interference it eliminates the stringent requirement of long-distance phase stabilization.

Though the DLCZ scheme does not meet all the criteria for long-distance quantum communication, it provides a promising approach to a fully controllable single-photon source based on atomic ensembles, which seems to be much easier for experimental demonstrations. We now summarize the

basic ideas behind it. The atomic ensemble generates a correlated state in Eq. (84), which is an exact analog of the SPDC radiation. By measuring the forward signal mode with a single-photon detector, under the condition that the detector clicks, the collective atomic mode is projected to a single-excitation state. Such excitations can be stored for a reasonably long time in metastable states (the so-called ground-state manifold) of the atoms. On demand the single-atomic excitation can be transferred to a single photon (still within the storage time) with a method described in the next section. This is with fully controllable properties: the emitted single-photon pulse is directed forward; the emission time is controllable by the repumping time; and the pulse shape is controllable by varying the time dependence of the Rabi frequency of the repumping pulse.

So far, significant advances have been achieved along these lines. For a partial list,[68] we mention the following: controllable generation, storage and retrieval of single photons with tunable frequency, timing and bandwidth (Chou et al., 2004; Eisaman et al., 2004; Chaneliere et al., 2005; and Eisaman et al., 2005), a deterministic single-photon source using measurement-based feedback protocol (Chen, S., et al., 2006; Laurat et al., 2006; Matsukevich et al., 2006b); conditional control of two atomic memories (Felinto et al., 2006), entanglement of two atomic ensembles (Matsukevich et al., 2006a) and its distribution between two quantum nodes located 3 meters apart (Chou et al., 2007), mapping photonic entanglement into and out of an atomic-ensemble-based quantum memory (Choi et al., 2008), optimal control of light pulse storage and retrieval (Novikova et al., 2007), and the Hong-Ou-Mandel interference of photon pairs from two independent ensembles (Chaneliere et al., 2007). A quantum repeater node following the robust protocol (Chen et al., 2007; Zhao et al., 2007) was experimentally demonstrated by Yuan et al. (2008). These experiments are currently limited by the relatively short coherence time ( $\sim 20~\mu \mathrm{s}$ ) of the memory qubits and the low conversion efficiency ( $\sim 15\%$ ) between photonic and atomic states. See Kimble (2008) for a more in-depth review on this topic.

# 2. Quantum state transfer between matter and photons

The technique of quantum state transfer between matter and photons is indispensable for both long-distance quantum communication and large-scale optical quantum computing (see Sec. VII). In such applications, the matter itself should be endowed with a long storage time. This makes atoms strong candidates for localized photonic information carriers. The early proposals (Cirac et al., 1997; van Enk, Cirac, and Zoller, 1997) along these lines use the strong coupling of photons and single atoms in high-finesse cavities.

The basic idea of quantum light memory is in transferring a photonic state to the excitations of atomic internal states. In such a way, it can be stored. After some controllable time, it should be possible to transfer back the excitations to photons restoring the original quantum state. The experimentally challenging technology at the interface of photons and single atoms motivated search for alternative routes to matter-light

![](images/2550f5adf92e84a2b69457f724b8d454ad86e34ed6df0f2fd379cd1a47602a60.jpg)  
FIG. 33 (color). Quantum memory for photonic polarization qubits. Two identical ensembles are identically driven by a classical field, which is equally right-circularly and left-circularly polarized. Classical and quantized light fields are fed into the first  $\mathrm{PBS}_{\mathrm{R} / \mathrm{L}}$  ("rotated" PBS which reflects left-circular photons and transmits right-circular photons) and leave at two different outputs of the second  $\mathrm{PBS}_{\mathrm{R} / \mathrm{L}}$ . Two half-wave plates (HWP), enabling the transformation  $|\mathrm{R}\rangle \leftrightarrow |\mathrm{L}\rangle$ , are placed along the  $|\mathrm{L}\rangle$  output of the first  $\mathrm{PBS}_{\mathrm{R} / \mathrm{L}}$ . As the atomic cell  $r$  (cell  $l$ ) works as a quantum memory for single photons with right-circular (left-circular) polarization, via the adiabatic transfer method, the whole setup is therefore a quantum memory of any single-photon polarization states. The inset shows the relevant level structure of the atoms, with the ground state  $|b\rangle$ , the storage metastable state  $|c\rangle$ , and the excited state  $|e\rangle$ . From Chen et al., 2007.

quantum interfaces. Along this line, theoretical ideas on quantum light memory have been proposed (Fleischhauer and Lukin, 2000; Kozhekin, Mølmer, and Polzik, 2000; Lukin, Yelin, and Fleischhauer, 2000; Duan et al., 2001; Duan, Cirac, and Zoller, 2002; Fleischhauer and Lukin, 2002; Chen et al., 2007) and the relevant experimental advances (Kash et al., 1999; Liu et al., 2001; Schori et al., 2002; Phillips et al., 2001; Bajcsy, Zibrov, and Lukin, 2003; van der Wal et al., 2003; Julsgaard et al., 2004; Matsukevich and Kuzmich, 2004; Hétet et al., 2008) have been reported.[69]

The atomic-ensemble-based quantum memory consists of a coherently driven atomic ensemble ( $N \gg 1$  atoms) of large optical thickness with a level structure shown in the inset of Fig. 33. The  $|c\rangle - |e\rangle$  transition is coherently driven by a classical field of Rabi frequency  $\Omega(t)$ , and the  $|b\rangle - |e\rangle$  transition is coupled to a quantized single-mode (the multimode case is similar) light field (described by an annihilation operator  $\hat{a}$ ). The coupling constant is denoted by  $g$ . Under the two-photon resonance (i.e., the two detunings for the two transitions shown in the inset of Fig. 33 are both equal to  $\Delta$ ), the classical driving field can induce transparency for the quantized light field and a substantial group-velocity reduction, and even the complete stopping of the light [for reviews, see Lukin and Imamoglu (2001), Lukin (2003), and Fleischhauer, Imamoglu, and Marangos (2005)]. The Hamiltonian of the whole system ( $N$  atoms plus the quantized light field), in a frame rotating at the optical frequency,

reads  $H = \hbar \Omega (t)\hat{S}_{ec} + \hbar g\sqrt{N}\hat{a}\hat{S}_{eb} + \mathrm{H.c.}$ , where  $\hat{S}_{ec} = \sum_{i}^{N}|e\rangle_{ii}\langle c|$ ,  $\hat{S}_{eb} = (1 / \sqrt{N})\sum_{i}^{N}|e\rangle_{ii}\langle b|$ , and H.c. denotes a Hermitian conjugate of the previous expression. This Hamiltonian has its zero-energy eigenstates, the so-called "dark states." When the atom number is much larger than the photon number, the dark states represent elementary excitations of bosonic quasiparticles, i.e., the dark-state polaritons. For more details on this concept, see Fleischhauer and Lukin (2000, 2002) and Lukin, Yelin, and Fleischhauer (2000).

By adiabatically changing  $\Omega(t)$  between the two limiting cases  $[\Omega(t) \ll g\sqrt{N}$ , or  $\Omega(t) \gg g\sqrt{N}]$  one can coherently map dark-state polariton states onto either purely atomlike states where the photons are stored or purely photonlike states, which corresponds to the release of the stored photons. In principle, a quantum memory based on the adiabatic transfer method is reversible, preserves a pulse shape of the stored photons (Fleischhauer and Lukin, 2000, 2002), and may have an efficiency very close to unity. As there is no excited atomic state in the dark-state subspace, the storage time can be very long.

The original quantum memory was proposed for storing a coherent superposition of photon-number states. However, two atomic ensembles can be entangled by storage of two entangled light fields (Lukin, Yelin, and Fleischhauer, 2000). Recent experiments achieved single quantum excitation memory times of  $1\mathrm{ms}$  using cold atomic ensembles (Zhao, B. et al., 2009),  $6\mathrm{ms}$  using atomic rubidium confined in a one-dimensional optical lattice (Zhao, R. et al., 2009), and  $0.1\mathrm{s}$  using quantum memory confined in an optical lattice with laser compensation of the lattice light shifts (Radnaev et al., 2010).

# VII. PHOTONIC QUANTUM COMPUTING

As we have seen in the above section, the photon, thanks to its high transmittance through air and glass fibers and its extremely long decoherence time, has arguably been the best candidate for quantum communication. However, things become trickier when we come to the field of quantum computation. The weak interaction between photons, which is of a significant benefit in quantum communication, turns out to be a drawback where nontrivial two-qubit quantum gates are essential. For a long time it seemed obvious that linear-optical two-photon gates can be done only in a nondeterministic fashion and thus quantum computing cannot be scalable. However, in 2001, Knill, Laflamme, and Milburn (2001) proved that scalable optical quantum computing is possible using only single-photon sources, linear-optical elements, and photon-number resolving detectors. The KLM scheme subsequently spurred new experiments demonstrating probabilistic controlled two-photon gates. Despite the efforts of KLM, the resource overhead required for optical quantum computing is daunting. Several improvements of this protocol, particularly those based on cluster states or error encoding, have dramatically reduced this worrying resource overhead, and started to bridge the gap between the theoretical scalability and practical implementations.

We witnessed considerable theoretical and experimental progress in optical quantum computing in these years. This

topic has been reviewed earlier by Kok et al. (2007); O'Brien (2007); O'Brien, Furasawa, and Vuckovic (2009); and Ralph and Pryde (2010). This section serves as a supplement to these previous reviews. Thus, we skip some theoretical details and mainly focus on recent experimental advances.

# A. Linear-optical two-qubit logic gates

Knill, Laflamme, and Milburn (2001) showed that the success rate of the logic gates can be arbitrarily close to 1. To this end, one can use ancilla photons and detectors. A similar conclusion has been independently obtained by Koashi, Yamamoto, and Imoto (2001). Their solution was based on entangled ancilla photons. A novel aspect of this protocol is that, despite the lack of the photon-photon interaction, quantum measurements with photon-number resolving detectors can induce effective nonlinearity sufficient for the realization of two-qubit gates. The original KLM scheme was only very recently implemented in a sophisticated setup up using polarization encoding and Sagnac interferometers for increased stability (Okamoto et al., 2010).

Further improvements reduced the complexity and improved the efficiency of the original scheme by introducing certain assumptions and restrictions, enabling a series of experiments and demonstrations. Hofmann and Takeuchi (2002) and independently Ralph et al. (2001, 2002) proposed quantum gates working under the restriction of what is here called a two-mode or four-mode case. That is, the successful operation of the gate can be verified if the two photons involved are detected in certain outputs (this is also called "detection in coincidence basis" or "conditioned detection"). Essentially a single two-photon interference is enough, together with a state-dependent filtering, to perform probabilistic CNOT operations. The restriction does not allow further operations on the two photons involved and thus limits the depth of calculations, however, the simplicity of the gate makes it a useful and reliable tool if no further joint operations on the two photons are required. The original proposal used dual-rail encoding and was first implemented by O'Brien et al. (2003). With polarization encoding, the CNOT gate and conditional phase shift operations were also demonstrated (Pittman, et al., 2003; Sanaka, et al., 2004). An even simpler setup becomes possible with polarization encoding (Kiesel, Schmid, Weber, et al., 2005; Langford et al., 2005; Okamoto et al., 2005) which in turn could be already applied, e.g., to observe cluster states for one-way quantum computing [see, Kiesel, Schmid, Toth, et al. (2005)]. Exploiting hyperentanglement, Lanyon, et al. (2008) demonstrated a three-qubit Toffoli gate. More recently, Politi et al. (2008) reported high-fidelity silica-on-silicon integrated optical realizations of key quantum photonic circuits. Laing et al. (2010) reported a two-photon quantum interference visibility of  $99.5(4)\%$ , a CNOT gate [the obtained average fidelity of logical basis was  $96.9(2)\%$  ] and a path-entangled two-photon state (with fidelity of  $>92\%$ ). Coffman, Kundu, and Wootters (2010) reported the first probabilistic logic gates on integrated circuits for polarization qubits.

![](images/7d09bbc5fa25da5276bbc33329537fc9b3718f0a742d241d65857b400b2cfd0c.jpg)

![](images/4eda2e4955507b28b51d2fef3506847c6ec1ebb4f28d961645502645e80a8fe1.jpg)  
FIG. 34 (color). A quantum CNOT gate for photonic qubits. (a) A nondestructive CNOT gate constituting of a PBS, half-wave plates (HWP) and using an ancilla entangled photon pair  $|\psi^{-}\rangle_{34}$  (Pittman, Jacobs, and Franson, 2001). (b) Experimental results of two-photon CNOT gate. From Zhao et al., 2005.

![](images/4ddff762016532d29745b887b34f88d85e26cdf015fe99a2905a2c0b045ce804.jpg)

In a separate development, Koashi, Yamamoto, and Imoto (2001) and Pittman, Jacobs, and Franson (2001) showed that by using entangled pairs of photons as ancilla, the success of the gate operation can be inferred by the detection of photons in ancilla outputs. This enables one to perform the gate operation in a nondestructive manner. Such gates, assisted by entangled or unentangled photon pairs, were reported using four or five photons; see Gasparoni et al. (2004); Zhao et al. (2005); Bao et al. (2007); Tokunaga et al. (2008); and Gao, Yao, et al. (2010).

In this section, we present, for pedagogical purposes, the working principle and a proof-of-principle demonstration (Zhao et al., 2005) of a nondestructive CNOT gate for two independent photons. Pittman, Jacobs, and Franson (2001) suggested that a successful operation of the gate can be indicated by detection acts of measured ancilla photons. Such information is feed forwardable. This is an important feature for both the circuit model and the one-way model of scalable optical quantum computing.

Suppose that one aims to perform a CNOT gate on an arbitrary two-qubit state  $|\chi \rangle_{25}$  [Eq. (80)] using an ancilla entangled-photon pair in the Bell state  $|\psi^{-}\rangle_{34}$ . Note that PBS2 in Fig. 34(a) transmits  $|H + V\rangle$  while it reflects  $|H - V\rangle$  polarization. The output state of the whole apparatus is (Pittman, Jacobs, and Franson, 2001)

$$
\begin{array}{l} | \chi \rangle_ {2 5} | \psi^ {-} \rangle_ {3 4} \rightarrow \frac {1}{4} [ | V ^ {\prime} \rangle_ {3 ^ {\prime}} | V \rangle_ {4 ^ {\prime}} (\mathrm {C N O T} _ {2 ^ {\prime} 5 ^ {\prime}} | \chi \rangle_ {2 ^ {\prime} 5 ^ {\prime}}) \\ + \left| H ^ {\prime} \right\rangle_ {3 ^ {\prime}} / V \rangle_ {4 ^ {\prime}} \left(\hat {z} _ {5 ^ {\prime}} \mathrm {C N O T} _ {2 ^ {\prime} 5 ^ {\prime}} | \chi \rangle_ {2 ^ {\prime} 5 ^ {\prime}}\right) \\ + \left| H ^ {\prime} \right\rangle_ {3 ^ {\prime}} \left| H \right\rangle_ {4 ^ {\prime}} \left(\hat {x} _ {5 ^ {\prime}} \hat {z} _ {5 ^ {\prime}} / \mathrm {C N O T} _ {2 ^ {\prime} 5 ^ {\prime}} \mid \chi \right\rangle_ {2 ^ {\prime} 5 ^ {\prime}}) \\ + \left| V ^ {\prime} \right\rangle_ {3 ^ {\prime}} \left| H \right\rangle_ {4 ^ {\prime}} \left(\hat {x} _ {5 ^ {\prime}} \mathrm {C N O T} _ {2 ^ {\prime} 5 ^ {\prime}} \mid \chi_ {2 ^ {\prime} 5 ^ {\prime}}\right) ] \\ + \frac {\sqrt {3}}{2} | \dots \rangle_ {\text {n o t f o u r - m o d e c a s e s}}. \tag {86} \\ \end{array}
$$

Consider a detection of a pair of photons at the output modes  $3^{\prime}$  and  $4^{\prime}$ , only one photon at each output (the four-mode

case). Depending on the registered polarizations, up to a specific unitary transformation, a nondestructive CNOT gate operation is then performed on  $|\chi \rangle_{2^{\prime}5^{\prime}}$ .

# B. Cluster-state quantum computing

Another significant step is the discovery of "cluster-state quantum computing" (Raussendorf and Briegel, 2001; Raussendorf, Browne, and Briegel, 2003; Briegel et al., 2009), which is based on the preparation of highly entangled multiqubit states, the so-called "cluster states" (Briegel and Raussendorf, 2001) and adaptive one-qubit measurements. Besides its thought-provoking theoretical structure, this model also brings a number of practical advantages for physical realization of quantum computation. In scenarios in which quantum gates can be performed directly in, at best, a nondeterministic fashion, the one-way model is particularly useful. Linear-optical cluster-state quantum computation is the most prominent example. For existing, short surveys of the topic, see O'Brien (2007) and Briegel et al. (2009).

Cluster states can be created by a controllable Ising-type interaction (Briegel and Raussendorf, 2001; Raussendorf and Briegel, 2001; Raussendorf, Browne, and Briegel, 2003). It was recently shown that an efficient preparation of cluster states is possible with probabilistic two-qubit controlled phase flip gates (Duan and Raussendorf, 2005; Chen, Q., et al., 2006). Few-photon cluster states were created in several recent experiments (Kiesel, Schmid, Toth, et al., 2005; Walther, Resch, Rudolph et al., 2005; Zhang, A.-N. et al., 2006; Lu et al., 2007; Tokunaga et al., 2008).

# 1. Constructing photonic cluster states

By combing the one-way model with linear-optical quantum computing, recent theoretical proposals require much less resources and effectively replace the original KLM scheme [see Nielsen (2004); Browne and Rudolph (2005); Bodiya and Duan (2006); Chen, Zhao, and Pan (2008); and an efficient parity-encoded optical quantum computing model by Gilchrist, Hayes, and Ralph (2007)]. Nielsen showed that efficiency can be greatly enhanced by building photonic cluster states using easy nondeterministic gates. The resource overhead (Bell states, operations, etc.) for a reliable entangling gate in Nielsen's scheme is  $\sim 10^3$ , and thus about 2 orders of magnitude less than the original KLM protocol. Furthermore, by introducing two linear-optical fusion operations, Browne and Rudolph (2005) achieved a greater degree of efficiency ( $\sim 10^2$ ) and in a simpler scheme than the previous proposals. Matter qubits can also be constructed into cluster states using linear optics and photon interference, as proposed by Barrett and Kok (2005). Here we focus on a linear-optical architecture for one-way quantum computing.

# a. Linear-optical architecture

The Browne-Rudolph scheme has an important practical advantage. It requires stable interferometry over only the coherence length of the photons, i.e., the interferometer path lengths differences only need to be kept constant to within tens of microns, not fractions of a wavelength. Its two basic operations are the type I and type II "two-qubit

![](images/7928d74dfb1e345ba2cd8593c95e3545227fead437765b9c2b582f985fdf5b51.jpg)  
Type-I fusion

![](images/5af96df950efb14f9d767a0e36ed42b61d5778eb8fc862829d4e93944e8ec4c6.jpg)  
FIG. 35 (color online). Nondeterministic photonic qubit fusion gates. The type I fusion gate combines two input single photons on a PBS and one of the outputs is measured in the  $H \pm V$  basis. The type II fusion gate combines two photons on a  $45^{\circ}$  rotated PBS (that is, both inputs and outputs are rotated using a HWP), and both outputs are detected. Adapted from Browne and Rudolph, 2005.  
Type-II fusion

fusion" operations (Fig. 35). The physical mechanism of type I fusion is again two-photon interference at the PBS, which is used as a parity check (Cerf, Adami, and Kwiat, 1998; Pan et al., 1998; Pan, Simon, Brukner, and Zeilinger, 2001; Pittman, Jacobs, and Franson, 2001). As displayed in Fig. 36, starting from a supply of two qubit polarization cluster states  $\frac{1}{2}(|HH\rangle + |VH\rangle + |HV\rangle - |VV\rangle)$  (which are equivalent to a Bell state and can be created via the methods described in Sec. VII.B.1), the type I fusion operation allows one to efficiently generate arbitrarily long linear cluster states. If the type I fusion is applied to the end qubits of linear (i.e., one-dimensional) clusters of lengths  $n$  and  $m$ , successful outcomes (with a probability of  $50\%$ ) generate a linear cluster of length  $n + m - 1$ . The type I fusion

![](images/ea786a71b24d099533bb6edafd2fab1c3f0a3e7e0838f7a9375cdd803d8c5d4a.jpg)

![](images/2cdea677fd1bcbbfd8d4ad8aef0031161d8afb5eae6b5463059befe078d961e8.jpg)

![](images/a254ecd1a6b607c5c2607f7759cdc4667ead229ce671f5e4bdf43238820b9930.jpg)

![](images/7956dd22de891d9b6e77174a97cbacb4311245bad43a58d8e651c8265f7615f3.jpg)  
redundant encoding

![](images/0c85fcaeea2928649ddecf4c1b914856ed8f70ef14403f5451a6dc0af44b91a4.jpg)

![](images/239af35c2c492c505f68a79586d963a5665a48e3d817f7ae2110ee2cf90a8f4e.jpg)  
FIG. 36 (color online). Construction of two-dimensional cluster states using photon fusion (Browne and Rudolph, 2005; Duan and Raussendorf, 2005). (a) Certain measurements on a cluster qubit will leave the remaining qubits in a new cluster state with a different layout. (b) The effect of type I and type II fusion operations on successful connection of two linear cluster states. (c) One method of efficient construction of two-dimensional cluster states [see also Duan and Raussendorf (2005)].

operation fails (also with a probability of  $50\%$ ) when zero or two photons of either polarization are detected. The failure outcomes have the effect of measuring both input qubits in the  $\sigma_z$  eigenbasis, which leaves the remaining qubits in a cluster state of the same layout as before the measurement, but now with all the bonds broken to the measured qubit. Browne and Rudolph (2005) also showed that one can finally prepare a square-lattice cluster of  $N$  qubits with a temporal overhead scaling logarithmically with  $N$ , and with an operational overhead (i.e., number of fusion operations) scaling as  $\sim N \ln N$  (Chen, Zhao, and Pan, 2008). The described protocol is a linear-optical realization of the Duan and Raussendorf (2005) proposal, and combines the advantages of the Browne-Rudolph scheme, whose overall efficiency is thereby demonstrated. A crucial element for a realistic realization is quantum memory for polarization qubits, which was discussed in Sec. VI.F.2.

# b. Event-ready entangler

In the above linear-optical architecture, two-photon entangled pairs are the basic resources. In the case of SPDC, one usually does not know when a pair is emitted. Only a firing of photon detectors informs one that a spontaneous emission act happened. However, most schemes of optical quantum computation, including the nondestructive CNOT gates, scalable fusion of cluster states, require that the photon pairs should be created in an "event-ready" (or heralded) way.

Zhang et al. (2008) proposed a way to generate one pair of event-ready entangled photons from four single photons, with a method that requires only linear optics and photon-number-discriminating detectors and performed an experimental simulation using four photons from SPDC. Another scheme of generating triggered photon pairs, which does not need true single-photon sources but totally rests upon SPDC, was proposed by Sliwa and Banaszek (2003). Following this proposal, in two experiments, Barz et al. (2010) and Wagenknecht et al. (2010), have demonstrated heralded generation of photon states that are maximally entangled in polarization.

Probably a more promising realization of a triggered entangled-photon source will come from the biexciton (two electron-hole pairs) radiative decay in a self-assembled quantum dot. This was demonstrated by Stevenson et al. (2006). A quantum dot can emit a single pair of entangled photons on demand, with a probability close to 1. However, it has a very low extraction efficiency. Recently, Dousse et al. (2010) used a carefully fabricated cavity to increase the collection efficiency, and created a source of polarization-entangled photon pairs with a state fidelity of 0.67 and a rate of 0.12 per an excitation pulse.

# C. Few-photon quantum computing experiments

In recent years, we also witnessed a number of proof-of-principle demonstrations of quantum computing involving several photons and linear optics (experimental realizations of photonic CNOT gates are been discussed in Sec. VII.A). For example, Mohseni et al. (2003) and Tame et al. (2007) demonstrated the two-qubit Deutsch-Josza algorithm in a

![](images/f5a18dc4965bd660a34e03dba45384d909c767124ab881ed5a414c3ca51bd2e5.jpg)  
FIG. 37 (color online). Few-qubit cluster states and the quantum circuits they implement. For each three-qubit and four-qubit cluster, its quantum state  $(|\Phi_{\mathrm{lin}3}\rangle ,|\Phi_{\mathrm{lin}4}\rangle ,|\Phi_{\square 4}\rangle ,|\Phi_{\square 4}\rangle)$  or  $|\Phi_{\square 4}\rangle$  ) and the computation carried out in the one-way quantum computer model is shown. Adapted from Walther, Resch, Rudolph et al., 2005.

circuit and a one-way model. The Grover's search algorithm (Grover, 1997) has been realized by Kwiat et al. (2000) by designing an optical circuit, and later by Walther, Resch, Rudolph et al. (2005); Chen, K. et al. (2007); Prevedel, Walther et al. (2007); and Vallone, Pomerico, and Martini (2008), who used four-qubit cluster states.

In the experiment of Walther, Resch, Rudolph et al. (2005) via a SPDC a four-photon polarization-entangled cluster state was created (with a fidelity of  $F = 0.63 \pm 0.02$ ):

$$
\begin{array}{l} \left| \Phi_ {\mathrm {c}} \right\rangle = \frac {1}{2} \left(| H \rangle_ {1} | H \rangle_ {2} | H \rangle_ {3} | H \rangle_ {4} + | H \rangle_ {1} | H \rangle_ {2} | V \rangle_ {3} | V \rangle_ {4} \right. \\ + | V \rangle_ {1} | V \rangle_ {2} | H \rangle_ {3} | H \rangle_ {4} - | V \rangle_ {1} | V \rangle_ {2} | V \rangle_ {3} | V \rangle_ {4}). \tag {87} \\ \end{array}
$$

With local unitary operations  $|\Phi_{\mathrm{c}} \rangle$  can be arranged to various cluster shapes  $|\Phi_{\mathrm{lin4}} \rangle$ ,  $|\Phi_{\square 4} \rangle$ ,  $|\Phi_{\square 4} \rangle$ , and  $|\Phi_{\square 4} \rangle$  (see Fig. 37). Using the cluster state  $|\Phi_{\mathrm{c}} \rangle$ , a universal set of quantum logic operations, single-qubit rotations, and nontrivial two-qubit gates were demonstrated. In addition, Walther et al. also implemented a two-qubit Grover's quantum search algorithm using the box cluster  $|\Phi_{\square 4} \rangle$ . The measured probability of the quantum computer to determine the correct outcome was about  $90\%$ . A drawback of the experiment is that no feed forward was used. This reduced the success rate of the computation by a factor of 2 for every measurement. An improved experiment by Prevedel, Walther et al. (2007) incorporated active fast feed forward, so that the earlier measurement outcomes could change the setting of a future measurement in real time. Particularly, the computational step (i.e., the individual feed-forward cycle) could be operated in less than 150 ns using electrooptical modulators.

Shor's quantum algorithm provides a way of factoring large integers in polynomial time, a task for which no efficient classical method is known. Recently, a compiled version of Shor's algorithm has been demonstrated using

four photonic qubits by Lanyon et al. (2007) and Lu, Browne, Yang, and Pan (2007). Aiming to solve the easiest case of Shor's algorithm  $(15 = 3\times 5)$ , these two experiments designed a simplified linear-optical network to implement the quantum circuits of the modular exponential execution. The results yielded a high success probability  $(\sim 0.99)$  of factoring. It is notable that in these optical experiments during the computation genuine multiparticle entanglement and multipath interference were observed, which did not appear in the previous implementations using nuclear magnetic resonance (Vandersypen et al., 2001). Optical implementations of Shor's algorithm later moved into an integrated photonic chip devices (Politi, Matthews, and O'Brien, 2009).

Another interesting avenue of the ongoing multiphoton experiments is to exploit the preliminary photonic quantum computers for simulation of many-body physics, a powerful application of quantum computers proposed in the early 1980s. Following proposals by Han, Raussendorf, and Duan (2007) and Pachos (2007), four-qubit and six-qubit graph states were created to mimic the ground state of the Kitaev spin-lattice model (Kitaev, 2003). Using the photonic graph states to simulate the creation and braiding of the anyons in the Kitaev model, a phase shift of  $\pi$  related to the anyon braiding was observed, confirming the predictions for the fractional statistics of Abelian  $1/2$  anyons (Lu et al., 2009; Pachos et al., 2009). Recently, Lanyon et al. (2010) employed a photonic quantum computer to solve a quantum chemistry problem: calculation of the energies of the hydrogen molecule. In their experiment, the iterative phase estimation quantum algorithm was performed in full. With the assistance of a classical computer, it was possible to calculate the complete energy spectrum, up to 20 bits of precision. Ma et al. (2011) used polarization states of four photons to simulate a frustrated Heisenberg spin system: a spin-1/2 tetramer.

# D. Toward scalable optical quantum computing

While in small-scale tests of optical quantum computing, we have witnessed a progress, serious problems exist in scaling up this technique. Here, we briefly discuss the key challenges and the ongoing efforts in designing fault-tolerant architectures, fighting against experimental noise, and improving single-photon sources and detectors.

Quantum computers will be very susceptible to noise, which rapidly destroys the fragile quantum information. Much effort has been devoted to the understanding of the scalability under realistic noise models. The threshold theorem has established that if the noise is below some value, an arbitrarily long quantum computation can be realized. Several fault-tolerant architectures for optical quantum computing have been proposed. Nielsen and Dawson (2005) showed that the thresholds are respectively  $< 3 \times 10^{-3}$  and  $< 10^{-4}$  for photon loss and depolarizing noise [see also Dawson, Haselgrove, and Nielsen (2006)]. In addition, there are proposals of one-way quantum computing in decoherence-free subspaces (Tame, Paternostro, and Kim, 2007; Jiang et al., 2009) and topological cluster-state quantum computing (Raussendorf, Harrington, and Goya, 2006; Rausendorf, Harrington, and Goya, 2007). The latter proposal achieved

a high error threshold of  $0.75 \times 10^{-3}$ , the highest known for a local architecture. For photon loss alone, Ralph, Hayes, and Gilchrist (2005), Varnava, Browne, and Rudolph (2006), and Varnava, Browne, and Rudolph (2008) have designed loss-tolerant quantum computer schemes within the circuit model and one-way model; the latter scheme can tolerate an overall optical loss, including source inefficiency and collection loss, up to an impressive  $33\%$ . Gong et al. (2010) proposed a new scheme where the efficiency threshold for loss tolerance requires the product of source and detector efficiencies to be  $>50\%$ . Despite the progress, one should note that when the losses are high, the resource requirements become impractically high. Moreover, unfortunately, these loss-tolerant codes tend to amplify the depolarizing errors (e.g., bit flips and phase flips); the trade off has been discussed and new schemes have been designed which tolerate both errors in Rohde, Ralph, and Munro (2007).

Some basic quantum error correction codes have been tested in optical experiments. O'Brien et al. (2005) demonstrated a two-qubit code for correction of a  $Z$ -measurement error. With a continuous-variable encoding, Aoki et al. (2009) realized a nine-qubit Shor's code, which is able to correct an arbitrary single-qubit error. Decoherence-free subspaces, a type of passive error-preventing codes, have been experimentally realized using two photons by Kwiat et al. (2000) and four photons by Bourennane, Eibl, Gaertner, et al. (2004). Furthermore, the decoherence-free subspace approach was applied in an optical demonstration of the Deutsch-Jozsa algorithm (Mohseni et al., 2003), and for reliable measurement-based one-way information transfer (Prevedel, Tame et al., 2007). To fight against the qubit-loss error, an especially serious problem for photonic qubits, Lu et al. (2008) demonstrated a four-qubit Grassl erasure correction code [for the theoretical proposals see Grassl, Beth, and Pellizzari (1997) and Ralph, Hayes, and Gilchrist (2005)], and a tree-shaped graph state (Varnava, Browne, and Rudolph, 2006). The tested method is applicable both in the quantum circuit model and in the one-way model.

Despite the progress, the fault-tolerant thresholds are still well beyond what is achievable with today's technology. Optical quantum computing makes critical use of sources of on-demand single photons which are indistinguishable and can be collected efficiently. The majority of experimental demonstrations so far have relied on the SPDC photons, which suffers from undesired higher-order photon emissions [Weinhold et al. (2008), this has been considered as the major source of error for most experiments reviewed here, see Sec. IV.D.1], large bandwidth, and the probabilistic manner of photon pair emission. New generations of single-photon sources have been developed: they are based on solid-state devices, atoms, molecules, ions, etc. [see Lounis and Orrit (2005) for a recent review]. These new single-photon emitters include single quantum dots (Michler et al., 2000; Pelton et al., 2002; Santori et al., 2002; Bennett et al., 2005; Englund et al., 2007; Shields, 2007; Strauf et al., 2007), nitrogen-vacancy color centers (Brouri et al., 2000; Kurtsiefer et al., 2000), neutral atoms (Kuhn, Hennrich, and Rempe, 2002; McKeever et al., 2004; Darquie, M. J. et al., 2005), ions (Keller et al., 2004), and molecules (Brunel et al., 1999; Lounis and Moerner, 2000). Solid-state sources of single photons hold

the promise of a ready integration, and much experimental effort has recently been devoted to improving the single-photon quality, collection efficiency, and interference of photons from remote independent quantum dots. Other controllable single-photon sources can be devised using trapped single atoms in high-finesse optical cavities, which are spectrally narrow and have a well-defined spatial mode. However, there are problems associated with low out-coupling efficiency. Single photons emitted by atomic ensembles, as we discussed in Sec. VI.F, are another promising source. This type of single-photon sources naturally enjoys a very narrow ( $\sim \mathrm{MHz}$ ) line width and good indistinguishability. However, in addition to the low photon extraction efficiency, much work needs to be done to improve the retrieval efficiency (converting atomic collective excitations into photons) up to unity.

To meet the stringent demands of scalable optical quantum computing, one faces yet another challenge: new single-photon detectors that have near-unity efficiencies, high repetition rates, low dark count rates, and the ability to resolve the photon number. Currently, mostly used room-temperature silicon single-photon detectors can be operated at  $10\mathrm{MHz}$  with a peak efficiency of  $65\%$ , a dark count rate of about  $100\mathrm{Hz}$ , and a timing jitter of typically 500 ps; work is in progress to improve these parameters [see, e.g., Kardynal, Yuan, and Shields (2008)]. Significant progress (Rosenberg et al., 2005; Divochiy et al., 2008; Lita, Miller, and Nam, 2008) has been made on superconducting detectors capable of resolving photon number, with an ultralow dark count rate  $(0.15\mathrm{Hz}$  at the wavelength of  $1.3\mu \mathrm{m})$  and high efficiency up to  $95\%$ . See Hadfield (2009) for more details.

Finally, it is worth mentioning that chip-scale waveguide quantum circuits have been created recently, and used to demonstrate high-visibility Hong-Ou-Mandel interference, CNOT gates, a realization of an elementary Shor's algorithm (Politi et al., 2008; Politi, Matthews, and O'Brien, 2009), and quantum walk (Peruzzo, 2010). Current silica waveguide circuits have dimensions of about  $1\mathrm{cm}$  per logic gate. This is a step toward integrated optics architecture for improved performance, miniaturization, and scalability. An open challenge is to integrate such devices with single-photon sources and detectors.

# VIII. CONCLUDING REMARKS

We reviewed the principles and experimental techniques for manipulation of multiphoton entangled states, which have enabled a series of pioneering experiments in the field of quantum information. A number of important applications have been highlighted: Laboratory tests demonstrating the contradiction between quantum mechanics and local realism performed with entangled photons, that is, the Bell and Greenberger-Horne-Zeilinger experiments (Weihs et al., 1998; Pan, Simon, Brukner, and Zeilinger, 2001). Quantum teleportation, the transfer and reconstruction of quantum states over arbitrary distances, which became an experimental reality with four-photon interferometry (Bouwmeester et al., 1997; Marcikic et al., 2003). A variation of teleportation, entanglement swapping (Pan et al., 1998), which together with entanglement purification (Pan, Gasparoni, Ursin et al., 2003) and quantum memory [see, e.g., Yuan et al. (2008)] are

the essential components of quantum repeaters necessary for quantum networking and long-distance quantum communication. Proof-of-principle demonstrations of linear-optics quantum computing [see, e.g., O'Brien et al. (2003); Walther, Resch, Rudolph et al., (2005); Lu et al. (2008); and Lanyon et al. (2010)] and super-resolving phase measurements [see, e.g., Nagata et al. (2007)] with multiphoton devices.

The ultimate goals are long-distance quantum communication and scalable optical quantum computing. However, many technological challenges remain. Parametric downconversion (Kwiat et al., 1995; White et al., 1999) has been serving as the main workhorse for the multiphoton experiments reviewed here; up to eight entangled photons have been observed (Yao et al., 2012). However, due to its intrinsic limitations, there is a bottleneck with regard to the attainable brightness and fidelity of multiphoton states based on it. This calls for the development of a next generation of more reliable and scalable single-photon sources (Lounis and Orrit, 2005). Other challenges include efficient coupling and detection of single photons and quantum memories for photons with long storage times and a high retrieval efficiency, etc. Continuing effort is devoted in this direction and encouraging results have been obtained. For instance, single photons and entangled photons have been generated from self-assembled quantum dots embedded in a microcavity, with extraction efficiency up to  $80\%$  (Dousse et al., 2010). In the case of a long-lived quantum memory based on atomic ensembles, storage times were reported to reach up to  $8\mathrm{ms}$  (Zhao, R. et al., 2009). Employment of cavities in this case may lead to additional potential improvements. Armed with these new techniques, the control of multiphoton states will reach a higher level. In any event, we expect that the techniques reviewed in this article will be in the forthcoming future in the mainstream of further progress of experimental multi-photon interferometry.

# ACKNOWLEDGMENTS

We would like to thank Y.-J. Wei, Z.-S. Yuan, B. Zhao, X.-H. Bao, M. Zhang, and N.-L. Liu for valuable comments and helps. This work was supported by the National Natural Science Foundation of China, the National Fundamental Research Program (under Grant No. 2011CB921300) and the Chinese Academy of Sciences. M. Z. was supported by Professorial Subsidy of FNP and the MNiI Grant No 1 P03B 04927, MNiSW Grant No. N202 208538, and EU programs QAP and Q-ESSENCE. He acknowledges Austrian-Polish and German-Polish exchange programmes, and finally CAS visiting professorship. H. W. acknowledges the support from DFG (MAP) and BMBF (QPENS and QuORep) and the EU programs QAP and Q-ESSENCE. A.Z. acknowledges the supports from EPSRC, QIPIRC, FWF, and EC under the Integrated Project Qubit Applications.

# APPENDIX A: THE TWO-PHOTON STATES PRODUCED BY SPDC

Crystal-field interaction-In the interaction Hamiltonian of the electromagnetic field with an atom or a molecule, the

dominating part is  $\hat{H}_{a - f}\sim \hat{\pmb{\mu}}_e\cdot \pmb {E}(\pmb {x},t)$  , i.e., scalar product of the dipole moment  $\pmb{\mu}$  of the atoms or molecules with the local electric field. Since the electric polarization  $\pmb {p}(\pmb {x},t)$  of a medium is given by the mean dipole moment of the atoms or molecules per unit volume, the principal term of the fieldcrystal interaction Hamiltonian  $H_{\mathrm{int}}$  is proportional to  $\int_V\pmb {p}(\pmb {x},t)\cdot \pmb {E}(\pmb {x},t)d^3 x$  where  $V$  is the volume of the crystal. One can assume that  $\pmb {E}(\pmb {x},t)$  interacts with  $\pmb {p}(\pmb {x},t)$  only in the point  $\pmb{x}$  , thus the ith component of polarization is in the most general case given by

$$
\begin{array}{l} p _ {i} (\boldsymbol {x}, t) = \sum_ {j = 1} ^ {3} \chi_ {i j} ^ {(1)} (\boldsymbol {x}) E _ {j} (\boldsymbol {x}, t) \\ + \sum_ {j, k = 1} ^ {3} \chi_ {i j k} ^ {(2)} (\boldsymbol {x}) E _ {j} (\boldsymbol {x}, t) E _ {k} (\boldsymbol {x}, t) + \dots , \tag {A1} \\ \end{array}
$$

where  $\chi_{ij}^{(1)}$  and  $\chi_{ijk}^{(2)}$  are the (macroscopic) polarizability tensors. For any crystal with centrosymmetric structure the quadratic term of the polarizability vanishes. Thus, as we shall see, the SPDC effect exists only for birefringent media having a nonzero value of  $\chi^{(2)}$ . If one assumes that  $\chi_{ijk}^{(2)}(\pmb{x})$  has the same value for all points within the crystal, one gets

$$
\begin{array}{l} H _ {\text {i n t}} \sim \int_ {V} \boldsymbol {p} (\boldsymbol {x}, t) \cdot \boldsymbol {E} (\boldsymbol {x}, t) d ^ {3} x \\ = \int_ {V} \boldsymbol {p} ^ {\text {l i n}} (\boldsymbol {x}, t) \cdot \boldsymbol {E} (\boldsymbol {x}, t) d ^ {3} x + \int_ {V} \boldsymbol {p} ^ {\text {n l}} (\boldsymbol {x}, t) \cdot \boldsymbol {E} (\boldsymbol {x}, t) d ^ {3} x, \\ \end{array}
$$

where  $p^{\mathrm{lin}}(p^{\mathrm{nl}})$  is the linear (nonlinear) term of polarization. The nonlinear (NL) part of the Hamiltonian is

$$
H ^ {\mathrm {N L}} \sim \int_ {V} \sum_ {i j k} \chi_ {i j k} ^ {(2)} E _ {i} (\boldsymbol {x}, t) E _ {j} (\boldsymbol {x}, t) E _ {k} (\boldsymbol {x}, t) d ^ {3} x. \tag {A2}
$$

The quantized electric field can be expressed (in the interaction picture) as

$$
\begin{array}{l} \boldsymbol {E} (\boldsymbol {x}, t) = \sum_ {\lambda = 1} ^ {2} \int d ^ {3} k \frac {i}{\sqrt {2 \omega (2 \pi) ^ {3}}} \hat {\epsilon} (\boldsymbol {k}, \lambda) a (\boldsymbol {k}, \lambda) e ^ {i (\boldsymbol {k} \cdot \boldsymbol {x} - \omega t)} + \mathrm {H . c .} \\ = \boldsymbol {E} ^ {(+)} (\boldsymbol {x}, t) + \boldsymbol {E} ^ {(-)} (\boldsymbol {x}, t), \tag {A3} \\ \end{array}
$$

where  $E^{(-)}(\pmb {x},t) = [E^{(+)}(\pmb {x},t)]^{\dagger}$ , and the summation is over two orthogonal linear polarizations, H.c. denotes the Hermitian conjugate of the previous term, and  $\hat{\epsilon} (\pmb {k},\lambda)$  is a unit vector defining the linear polarization. The symbol  $a(k,\lambda)$  denotes the annihilation operator of a monochromatic photon with wave vector  $\pmb{k}$  and polarization  $\hat{\epsilon} (\pmb {k},\lambda)$ . The principal commutation rules for such creation and annihilation operators are given by[70]  $[a(\pmb {k},\lambda),a^{\dagger}(\pmb{k}^{\prime},\lambda^{\prime})] =$ $\delta_{\lambda ,\lambda '}\delta^{(3)}(\pmb {k} - \pmb{k}'),\qquad [a^\dagger (\pmb {k},\lambda),a^\dagger (\pmb {k}',\lambda ')] = 0,\qquad \mathrm{and}\qquad [a(\pmb {k},\lambda),a(\pmb {k}',\lambda ')] = 0.$

The relevant terms in the Hamiltonian-One can neglect the depletion of the laser field and assume that the total field is  $E^{\mathrm{Laser}}(\pmb{x},t) + \pmb{E}(\pmb{x},t)$ , where  $E^{\mathrm{Laser}}$  is a classical field. The quantum field  $\pmb{E}$  describes the emitted photons. The downconversion takes place, thanks to only the terms in Eq. (A2) of the form

$$
\int_ {V} \sum_ {i j k} \chi_ {i j k} ^ {(2)} E _ {i} ^ {\text {L a s e r}} E _ {j} ^ {(-)} E _ {k} ^ {(-)} d ^ {3} x. \tag {A4}
$$

Simply, only  $E^{(-)}$  contains the creation operators, and thus acting on the vacuum state  $|\Omega\rangle$  can give rise to a two-photon state. Thus, we forget about all other terms and analyze only  $H^{\mathrm{NL}}$  in the form of Eq. (A4) plus its Hermitian conjugate.

We now describe the laser field as a monochromatic plane wave  $\hat{z} E_0(e^{i(k_0\cdot x - \omega_0t - \phi)} + \mathrm{c.c.})$ , where  $E_0$  is the field amplitude. Then, from Eq. (A4), one gets for  $H^{\mathrm{NL}}$

$$
\begin{array}{l} \sim \int_ {V} d ^ {3} x \sum_ {j k} \left\{\chi_ {3 j k} ^ {(2)} E _ {0} \left[ e ^ {i \left(\boldsymbol {k} _ {0} \cdot \boldsymbol {x} - \omega_ {0} t - \phi\right)} + c. c. \right] \right. \\ \times \sum_ {\lambda} \int d ^ {3} k f (\omega) \hat {\epsilon} _ {j} (\boldsymbol {k}, \lambda) a ^ {\dagger} (\boldsymbol {k}, \lambda) e ^ {- i (\boldsymbol {k} \cdot \boldsymbol {x} - \omega t)} \\ \times \sum_ {\lambda^ {\prime}} \int d ^ {3} k ^ {\prime} f \left(\omega^ {\prime}\right) \hat {\epsilon} _ {k} \left(k ^ {\prime}, \lambda\right) a ^ {\dagger} \left(k ^ {\prime}, \lambda\right) e ^ {- i \left(\boldsymbol {k} \cdot \boldsymbol {x} - \omega^ {\prime} t\right) t} + \text {H . c .}, \tag {A5} \\ \end{array}
$$

with  $f(\omega)$  a factor dependent on  $\omega$ . Its specific structure is irrelevant here. Extracting only those elements of the above expressions which contain  $x$  and  $t$ , one sees that their overall contribution to  $H^{\mathrm{NL}}$  is given by  $\Delta (\pm k_0 - k - k') e^{-i(\pm \omega_o - \omega - \omega')t}$ , where  $\Delta_{\pm}(..) = \int_V d^3 x e^{i(\pm k_0 - k - k') \cdot x}$ . The terms with the time-dependent factors  $e^{i(\omega_o + \omega + \omega')t}$  average out in any time integration (see below), and thus we can drop them. If we assume that our crystal is a cube  $L \times L \times L$ , then for  $L \to \infty$ ,  $\Delta_{\pm}$  approaches  $\delta (\pm k_0 - k - k')$ . Thus, emission of the photon pairs is possible only for the directions for which the condition  $k_0 \approx k + k'$  is met. Finally, one has

$$
\begin{array}{l} H ^ {\mathrm {N L}} \sim \sum_ {\lambda , \lambda^ {\prime}} \int d ^ {3} k \int d ^ {3} k ^ {\prime} \Delta \left(\boldsymbol {k} _ {0} - \boldsymbol {k} - \boldsymbol {k} ^ {\prime}\right) A _ {\lambda , \lambda^ {\prime}} ^ {\mathrm {e f f}} e ^ {- i (\omega_ {0} - \omega - \omega^ {\prime}) t} \\ \times a ^ {\dagger} (\boldsymbol {k}, \lambda) a ^ {\dagger} \left(\boldsymbol {k} ^ {\prime}, \lambda^ {\prime}\right) + \mathrm {H . c .}, \tag {A6} \\ \end{array}
$$

where  $A_{\lambda ,\lambda^{\prime}}^{\mathrm{eff}} = \sum_{j,k}E_{0}\chi_{3jk}^{(2)}\hat{\epsilon}_{j}(\pmb {k},\lambda)\hat{\epsilon}_{k}(\pmb{k}^{\prime},\lambda^{\prime})$  is the effective strength of the laser-crystal coupling. Henceforth, we shall replace the symbol  $A_{\lambda ,\lambda^{\prime}}^{\mathrm{eff}}$  by  $F_{o}(\pmb{k}_{0})$

The state of photons emitted in the SPDC process-The pump-crystal coupling is weak. The evolution of the state  $|\Psi_D(t)\rangle$  (in the interaction picture) is given by  $i\hbar (d / dt)|\Psi_D(t)\rangle = H^{\mathrm{NL}}(t)|\Psi_D(t)\rangle$  . In the first order in the perturbation expansion

$$
\left| \Psi_ {D} (t) \right\rangle \simeq \left| \Psi_ {D} \left(t _ {0}\right) \right\rangle + \frac {1}{i \hbar} \int_ {t _ {0}} ^ {t} H ^ {\mathrm {N L}} \left(t ^ {\prime}\right) \left| \Psi_ {D} \left(t _ {0}\right) \right\rangle d t ^ {\prime}. \tag {A7}
$$

Put  $t_0 = -\infty$  and take the vacuum state (no photons)  $|\Omega \rangle$  as the initial state  $|\Psi (0)\rangle$ . Only in the term with the integral can one find creation of pairs of photons. For  $t\to \infty$  it contains an integral of the following form:  $\int_{-\infty}^{+\infty}dt^{\prime}e^{it^{\prime}(\omega +\omega^{\prime} - \omega_{0})}$ , which is  $2\pi \delta (\omega +\omega^{\prime} - \omega_{0})$ . Thus, the two-photon component of the state, at  $t = \infty$ , is effectively given by

$$
\begin{array}{l} \sum_ {\lambda , \lambda^ {\prime}} \int d ^ {3} k \int d ^ {3} k ^ {\prime} F _ {o} (\boldsymbol {k} _ {0}) \Delta (\boldsymbol {k} _ {0} - \boldsymbol {k} - \boldsymbol {k} ^ {\prime}) \delta (\omega + \omega^ {\prime} \\ - \omega_ {0}) a ^ {\dagger} (\boldsymbol {k}, \lambda) a ^ {\dagger} \left(\boldsymbol {k} ^ {\prime}, \lambda^ {\prime}\right) | \Omega \rangle , \tag {A8} \\ \end{array}
$$

and the frequencies of the emissions satisfy the relation $^{72}$ $\omega_0 = \omega + \omega'$ .

Directions of emissions-Since  $\omega = |k|c / n(\omega ,\lambda)$  , where  $c / n(\omega ,\lambda) = c(\omega ,\lambda)$  is the speed of light in the given medium, which depends on frequency and polarization, the condition for frequencies becomes  $|\pmb {k}_0|c(\omega_0)\simeq |\pmb {k}|c(\omega ,\lambda) +$ $|\pmb{k}^{\prime}|c(\omega^{\prime},\lambda^{\prime})$  . This together with  $\pmb {k}_0\simeq \pmb {k}_s + \pmb {k}_i$  fixes the possible emission directions, frequencies, and polarizations.73

Time correlations- The probability of a detection of a photon, of, e.g., the horizontal polarization  $H$ , at a detector situated at point  $\mathbf{x}$  and at time  $t$ , is proportional to  $\eta \mathrm{Tr}[\varrho (t)E_H^{(-)}(\pmb {x},t)E_H^{(+)}(\pmb {x},t)]$ , where  $\eta$  is the coefficient which characterizes the quantum efficiency of the detection process,  $\varrho$  is the density operator, and  $E_{H}$  is the horizontal component of the field in the detector. For the above relation to be true, we also assume that only photons of a specified direction of the wave vector enter via the aperture of the detector. For a pure state, this reduces to  $p(x,t,H)\simeq \langle \psi |E_H^{(-)}E_H^{(+)}|\psi \rangle$ . The probability of a joint detection of two photons, of polarization  $H$ , at the locations  $x_{1}$  and  $x_{2}$ , and at the moments of time  $t$  and  $t^{\prime}$ , is proportional to

$$
\begin{array}{l} p \left(\boldsymbol {x} _ {1}, t; \boldsymbol {x} _ {2}, t ^ {\prime}\right) \\ \sim \langle \psi | E _ {H} ^ {(-)} (\boldsymbol {x} _ {1}, t) E _ {H} ^ {(-)} (\boldsymbol {x} _ {2}, t ^ {\prime}) E _ {H} ^ {(+)} (\boldsymbol {x} _ {2}, t ^ {\prime}) E _ {H} ^ {(+)} (\boldsymbol {x} _ {1}, t) | \psi \rangle . \tag {A9} \\ \end{array}
$$

If the detectors are very far away from each other, and from the crystal, then the photon field reaching them can be treated as free evolving. We put into Eq. (A9) the photon state Eq. (A8). Let  $t = t_1$  and  $t' = t_2$ , and  $|\psi\rangle = |\psi(t = \infty)\rangle$ , then Eq. (A9) can be written down as

$$
\begin{array}{l} p \left(\boldsymbol {x} _ {1}, t \mid \boldsymbol {x} _ {2}, t ^ {\prime}\right) \simeq \langle \psi | E _ {H} ^ {(-)} \left(\boldsymbol {x} _ {1}, t\right) E _ {H} ^ {(-)} \left(\boldsymbol {x} _ {2}, t ^ {\prime}\right) \\ \times E _ {H} ^ {(+)} \left(\boldsymbol {x} _ {1}, t\right) E _ {H} ^ {(+)} \left(\boldsymbol {x} _ {2}, t ^ {\prime}\right) | \psi \rangle . \tag {A10} \\ \end{array}
$$

To simplify the description, we replace the annihilation and creation operators, which were used above, with new operators  $a_{i}(\omega)$  and their conjugates, which describe "unidirectional" excitations of the photon field [i.e., we assume that the detectors see only the photons of a specified direction of propagation, a good assumption if the detectors are far from the crystal, and the apertures are narrow, see Fearn and Loudon (1987)]. The index  $i$  defines the direction (fixed) of the wave vector. The new operators satisfy commutation relations, which are a modification of those given above to the current specific case  $[a_{i}(\omega), a_{j}^{\dagger}(\omega')] = \delta_{ij} \delta(\omega - \omega'), [a_{i}(\omega), a_{j}(\omega')] = 0$ . If we choose just two propagation

directions that fulfill the phase-matching conditions, then effectively one can put

$$
E _ {H} ^ {(+)} \left(\boldsymbol {x} _ {i}, t\right) = \int d \omega e ^ {- i \omega t} f _ {i} (\omega) a _ {i} (\omega) \tag {A11}
$$

with  $i = 1,2$ , and where  $f_{1}$  and  $f_{2}$  are the frequency response functions of the filter-detector system.

We assume that the maxima of the functions agree with the frequencies given by the phase-matching conditions. Introducing a unit operator  $\hat{I} = \sum_{i=0}^{\infty} |b_i\rangle \langle b_i|$ , where  $|b_i\rangle$  is a basis states, into Eq. (A10), we obtain

$$
\begin{array}{l} p \left(\boldsymbol {x} _ {1}, t \mid \boldsymbol {x} _ {2}, t ^ {\prime}\right) \simeq \langle \psi \mid E _ {H} ^ {(-)} \left(\boldsymbol {x} _ {1}, t\right) E _ {H} ^ {(-)} \left(\boldsymbol {x} _ {2}, t ^ {\prime}\right) \hat {I} E _ {H} ^ {(+)} \left(\boldsymbol {x} _ {1}, t\right) \\ \times E _ {H} ^ {(+)} \left(\boldsymbol {x} _ {2}, t ^ {\prime}\right) | \psi \rangle . \tag {A12} \\ \end{array}
$$

Since  $E_H^{(+)}$  contains only the annihilation operators, they transform the two-photon state  $|\Psi \rangle$  into the vacuum state. Thus, Eq. (A12) can be put as (Mollow, 1973)

$$
p \left(\boldsymbol {x} _ {1}, t \mid \boldsymbol {x} _ {2}, t ^ {\prime}\right) \simeq \langle \psi | E _ {H} ^ {(-)} E _ {H} ^ {t (-)} | \Omega \rangle \langle \Omega | E _ {H} ^ {(+)} E _ {H} ^ {t (+)} | \psi \rangle , \tag {A13}
$$

where the primed expressions pertain to the moment of time  $t^\prime$  and the position  $\pmb{x}_2$ . Thus, we have  $p(\pmb {x}_1,t|\pmb {x}_2,t^{\prime})\simeq |A_{12}(t,t^{\prime})|^{2}$ , where  $A_{12}(t,t^{\prime}) = \langle \Omega |E_H^{(+)}(\pmb {x}_1,t)E_H^{\prime (+)}(\pmb {x}_2,t^{\prime})|\psi \rangle$ . With the use of the new creation operators, the state  $|\Psi \rangle$  can be approximated by

$$
\left| \Omega \right\rangle + \int d \omega_ {1} \int d \omega_ {2} F _ {o} \delta \left(\omega - \omega_ {1} - \omega_ {2}\right) a _ {1} ^ {\dagger} \left(\omega_ {1}\right) a _ {2} ^ {\dagger} \left(\omega_ {2}\right) \left| \Omega \right\rangle . \tag {A14}
$$

Therefore, one gets the following formula for the detection amplitude:

$$
\begin{array}{l} A _ {1 2} (t, t ^ {\prime}) \\ = \langle \Omega | \int d \omega^ {\prime} e ^ {- i \omega^ {\prime} t ^ {\prime}} f _ {2} (\omega^ {\prime}) a _ {2} (\omega^ {\prime}) \int d \omega e ^ {- i \omega t} f _ {1} (\omega) a _ {1} (\omega) \\ \times \int d \omega_ {1} \int d \omega_ {2} F _ {o} \delta \left(\omega_ {0} - \omega_ {1} - \omega_ {2}\right) a _ {2} ^ {\dagger} \left(\omega_ {2}\right) a _ {1} ^ {\dagger} \left(\omega_ {1}\right) | \Omega \rangle . \tag {A15} \\ \end{array}
$$

Since the creation and annihilation operators for different modes commute, and since one can use  $\langle \Omega |a_i(\omega ')a_j^\dagger (\omega)|\Omega \rangle = \delta_{ij}\delta (\omega ' - \omega)$ , we get

$$
A _ {1 2} (t, t ^ {\prime}) = F _ {o} e ^ {- i \omega_ {0} t ^ {\prime}} \int d \omega e ^ {- i \omega (t - t ^ {\prime})} f _ {2} (\omega_ {0} - \omega) f _ {1} (\omega), \tag {A16}
$$

and we have

$$
\begin{array}{l} p (\boldsymbol {x} _ {1}, t | \boldsymbol {x} _ {2}, t ^ {\prime}) \sim | A _ {1 2} (t, t ^ {\prime}) | ^ {2} \\ \simeq \left| \int d \omega e ^ {- i \omega (t - t ^ {\prime})} f _ {2} \left(\omega_ {0} - \omega\right) f _ {1} (\omega) \right| ^ {2}, \tag {A17} \\ \end{array}
$$

i.e., the probability depends on the difference of the detection times.

For instance, assume that  $f_{1} = f_{2} = f$ , and that they are Gaussian,  $f(\omega) = Ce^{-(\omega_c - \omega)^2 / \sigma^2}$ , with the central frequency  $\omega_c = \omega_0 / 2$ . Then we have  $f_{1}(\omega) = f_{2}(\omega_{0} - \omega) = f(\omega)$ .

The probability of detection of two photons at the moments  $t$  and  $t'$  reads

$$
\begin{array}{l} p (\boldsymbol {x} _ {1}, t | \boldsymbol {x} _ {2}, t ^ {\prime}) \\ \sim \left| \int d \omega e ^ {- i \omega (t - t ^ {\prime})} C ^ {2} e ^ {- 2 \left[ \left(\omega_ {c} - \omega\right) ^ {2} / \sigma^ {2} \right]} \right| ^ {2} \sim e ^ {- (\sigma^ {2} / 2) (t - t ^ {\prime}) ^ {2}}. \tag {A18} \\ \end{array}
$$

As  $\sigma \to \infty$ , Eq. (A18) approaches  $\delta(t - t')$ . We have a perfect time correlation. For a realistic case of final bandwidths, the degree of time correlation of the detection of the SPDC photons depends entirely on the frequency response of the detectors (plus interference filters, if any, in front of them).

The output state of pulsed pumped SPDC-Since the pump pulse is a superposition of monochromatic waves, the output state for this case is an integral of the monochromatic case over the momentum profile of the pulse:  $|\psi_{\mathrm{pulse}}\rangle = \int d^3 k_0|\psi (F_o(k_0))\rangle$  , where  $|\psi (F_o(k_0))\rangle$  is the state for the monochromatic case with wave vector  $\pmb{k}_0$  and field amplitude  $F_{o}(k_{0})$  . Since the frequency of the pulse and the wave vector are not strictly defined, if the pulse is too short the SPDC photons are less tightly correlated directionally.

The two-photon state produced by a SPDC process is given by (in the unidirectional approximation)

$$
\begin{array}{l} | \Psi \rangle = \int d \omega_ {0} F _ {o} (\omega_ {0}) \int d \omega_ {1} \int d \omega_ {2} \delta (\omega_ {0} - \omega_ {1} - \omega_ {2}) \\ \times a _ {1} ^ {\dagger} \left(\omega_ {1}\right) a _ {2} ^ {\dagger} \left(\omega_ {2}\right) | \Omega \rangle , \tag {A19} \\ \end{array}
$$

where we have replaced the effective pump amplitude by the spectral decomposition of the laser pulse  $F_{o}(\omega_{0})$

Two-photon detection amplitude: the pulsed-pump case-If we have a pulsed pump, we have to integrate the amplitude (A16) over the frequency content of the pump [just like it is in the case of the state (A19)]:

$$
\begin{array}{l} A (t, t ^ {\prime}) = \int d \omega_ {o} F _ {o} (\omega_ {o}) e ^ {- \omega_ {o} t ^ {\prime}} \\ \times \int d \omega e ^ {- i \omega (t - t ^ {\prime})} f _ {2} (\omega_ {o} - \omega) f _ {1} (\omega) \\ = \int d t _ {p} F _ {o} \left(t _ {p}\right) f _ {1} \left(t - t _ {p}\right) f _ {2} \left(t ^ {\prime} - t _ {p}\right), \tag {A20} \\ \end{array}
$$

where  $F_{o}(t)$  is the Fourier transformation (time profile) of  $F_{o}(\omega)$ . Namely, the time correlation of the detections is defined by the resolution of the respective filters, while the events happen at times dictated by the pulse. This is clearly visible in the case of no filters and broad band radiation. The (unphysical) limiting case is reached by replacing  $f_{s}$  by  $\delta(t - t_{p})$  and  $\delta(t' - t_{p})$ . This gives  $F(t)\delta(t' - t)$ .

# REFERENCES

Aerts, S., P. Kwiat, J.-A. Larsson, and M. Zukowski, 1999, Phys. Rev. Lett. 83, 2872.  
Akopian, N., N. Lindner, E. Poem, Y. Berlatzky, J. Avron, D. Gershoni, B. Gerardot, and P. Petroff, 2006, Phys. Rev. Lett. 96, 130501.  
Alber, G., T. Beth, M. Horodecki, P. Horodecki, R. Horodecki, M. Rotteler, H. Weinfurter, R. Werner, and A. Zeilinger, 2001,

Quantum Information: An Introduction to Basic Theoretical Concepts and Experiments (Springer-Verlag, Berlin).  
Altepeter, J., E. Jeffrey, and P. Kwiat, 2005, Opt. Express 13, 8951.  
Amselem, E., M. Radmark, M. Bourennane, and A. Cabello, 2009, Phys. Rev. Lett. 103, 160405.  
Ansmann, M., H. Wang, Radoslaw, C. Bialczak, M. Hofheinz, E. Lucero, M. Neeley, A.D. O'Connell, D. Sank, M. Weides, J. Wenner, A.N. Cleland, and J.M. Martinis, 2009, Nature (London) 461, 504.  
Aoki, T., G. Takahashi, T. Kajiya, J. Yoshikawa, S.L. Braunstein, P. van Loock, and A. Furusawa, 2009, Nature Phys. 5, 541.  
Ardehali, M., 1992, Phys. Rev. A 46, 5375.  
Aschauer, H., and H. Briegel, 2002, Phys. Rev. Lett. 88, 047902.  
Aspect, A., 1999, Nature (London) 398, 189.  
Aspect, A., J. Dalibard, and G. Roger, 1982, Phys. Rev. Lett. 49, 1804.  
Aspect, A., P. Grangier, and G. Roger, 1981, Phys. Rev. Lett. 47, 460.  
Aspect, A., P. Grangier, and G. Roger, 1982, Phys. Rev. Lett. 49, 91.  
Aspelmeyer, M., H.R. Böhm, T. Gyatso, T. Jennewein, R. Kaltenbaek, M. Lindenthal, G. Molina-Terriza, A. Poppe, K. Resch, M. Taraba, R. Ursin, P. Walther, and A. Zeilinger, 2003, Science 301, 621.  
Aspelmeyer, M., H.R. Bohm, T. Gyatso, T. Jennewein, R. Kaltenbaek, M. Lindenthal, G. Molina-Terriza, A. Poppe, K. Resch, M. Taraba, R. Ursin, P. Walther, and A. Zeilinger, 2003, Science 301, 621.  
Aspelmeyer, M., T. Jennewein, M. Pfenningbauer, W. Leeb, and A. Zeilinger, 2003, IEEE J. Sel. Top. Quantum Electron. 9, 1541.  
Bajcsy, M., A. Zibrov, and M. Lukin, 2003, Nature (London) 426, 638.  
Bao, X.-H., T.-Y. Chen, Q. Zhang, J. Yang, H. Zhang, T. Yang, and J.-W. Pan, 2007, Phys. Rev. Lett. 98, 170502.  
Bao, X.-H., Y. Qian, J. Yang, H. Zhang, Z.-B. Chen, T. Yang, and J.-W. Pan, 2008, Phys. Rev. Lett. 101, 190501.  
Barbieri, M., C. Cinelli, P. Mataloni, and F. D. Martini, 2005, Phys. Rev. A 72, 052110.  
Barbieri, M., T. J. Weinhold, B. Lanyon, A. Gilchrist, K. Resch, M. Almeida, and A. White, 2009, J. Mod. Opt. 56, 209.  
Barnett, S., J. Jeffers, A. Gatti, and R. Loudon, 1998, Phys. Rev. A 57, 2134.  
Barreiro, J., N. Langford, N. Peters, and P. Kwiat, 2005, Phys. Rev. Lett. 95, 260501.  
Barreiro, J., T.-C. Wei, and P. Kwiat, 2008, Nature Phys. 4, 282.  
Barrett, M., J. Chiaverini, T. Schaetz, J. Britton, W.M. Itano, J.D. Jost, E. Knill, C. Langer, D. Leibfried, R. Ozeri, and D.J. Wineland, 2004, Nature (London) 429, 737.  
Barrett, S., and P. Kok, 2005, Phys. Rev. A 71, 060310(R).  
Barz, S., G. Cronenberg, A. Zeilinger, and P. Walther, 2010, Nature Photon. 4, 553.  
Belinskii, A., and D. Klyshko, 1993, Phys. Usp. 36, 653.  
Bell, J., 1964, Physics 1, 195, http://www.drchinese.com/David/Bell_Compact.pdf.  
Bell, J., 1987, Speakable and Unspeakable in Quantum Mechanics (Cambridge University Press, Cambridge).  
Bell, J. S., 1966, Rev. Mod. Phys. 38, 447.  
Bennett, A., D. Unitt, P. Atkinson, D. Ritchie, and A. Shields, 2005, Opt. Express 13, 50.  
Bennett, C., H. Bernstein, S. Popescu, and B. Schumacher, 1996, Phys. Rev. A 53, 2046.  
Bennett, C., and G. Brassard, 1984, Proceedings of the IEEE International Conference on Computers and Systems and Singal Proceeding and Bangalore and India (IEEE and New York), 175.  
Bennett, C., G. Brassard, C. Crepeau, R. Jozsa, A. Peres, and W. Wootters, 1993, Phys. Rev. Lett. 70, 1895.

Bennett, C., G. Brassard, S. Popescu, B. Schumacher, J. Smolin, and W. Wootters, 1996, Phys. Rev. Lett. 76, 722.  
Bennett, C., and D. DiVincenzo, 2000, Nature (London) 404, 247.  
Bennett, C., D. DiVincenzo, J. Smolin, and W. Wootters, 1996, Phys. Rev. A 54, 3824.  
Bennett, C., and S. Wiesner, 1992, Phys. Rev. Lett. 69, 2881.  
Bennett, C.H., 1992, Phys. Rev. Lett., 68, 3121.  
Bernstein, H., D.M. Greenberger, M.A. Horne, and A. Zeilinger, 1993, Phys. Rev. A 47, 78.  
Beugnon, J., M. P. A. Jones, J. Dingjan, B. Darquie, G. Messin, A. Browaecs, and P. Grangier, 2006, Nature (London) 440, 779.  
Bialynicki-Birula, I., and Z. Bialynicka-Birula, 1975, Quantum Electrodynamics (Pergamon, New York).  
Blinov, B., D. Moehring, L.-M. Duan, and C. Monroe, 2004, Nature (London) 428, 153.  
Bodiya, T., and L.-M. Duan, 2006, Phys. Rev. Lett. 97, 143601.  
Bohm, D., 1951, Quantum Theory (Prentice-Hall, Englewood Cliffs, NJ).  
Boschi, D., S. Branca, F. D. Martini, and L. Hardy, 1997, Phys. Rev. Lett. 79, 2755.  
Boschi, D., S. Branca, F.D. Martini, L. Hardy, and S. Popescu, 1998, Phys. Rev. Lett. 80, 1121.  
Bose, S., P. Knight, M. Plenio, and V. Vedral, 1999, Phys. Rev. Lett. 83, 5158.  
Bose, S., V. Vedral, and P. Knight, 1998, Phys. Rev. A 57, 822.  
Boto, A., P. Kok, D. Abrams, S. Braunstein, C. Williams, and J. Dowling, 2000, Phys. Rev. Lett. 85, 2733.  
Boureennane, M., M. Eibl, S. Gaertner, C. Kurtsiefer, A. Cabello, and H. Weinfurter, 2004, Phys. Rev. Lett. 92, 107901.  
Bourennane, M., M. Eibl, C. Kurtsiefer, S. Gaertner, H. Weinfurter, O. Guhne, P. Hyllus, D. Bru, M. Lewenstein, and A. Sanpera, 2004, Phys. Rev. Lett. 92, 087902.  
Bouwmeester, D., A. Ekert, and A. Zeilinger, 2001, Eds., The Physics of Quantum Information, (Springer-Verlag, Berlin).  
Bouwmeester, D., 2004, Nature (London) 429, 139.  
Bouwmeester, D., J.-W. Pan, M. Daniell, H. Weinfurter, and A. Zeilinger, 1999, Phys. Rev. Lett. 82, 1345.  
Bouwmeester, D., J.-W. Pan, M. Daniell, H. Weinfurter, M. Zukowski, and A. Zeilinger, 1998, Nature (London) 394, 841.  
Bouwmeester, D., J.-W. Pan, K. Mattle, M. Eibl, H. Weinfurter, and A. Zeilinger, 1997, Nature (London) 390, 575.  
Bouwmeester, D., J.-W. Pan, H. Weinfurter, and A. Zeilinger, 2000, J. Mod. Opt. 47, 279.  
Braig, C., P. Zarda, C. Kurtsiefer, and H. Weinfurter, 2003, Appl. Phys. B 76, 113.  
Branciard, C., A. Ling, N. Gisin, C. Kurtsiefer, A. Lamas-Linares, and V. Scarani, 2007, Phys. Rev. Lett. 99, 210407.  
Branning, D., W. Grice, R. Erdmann, and I. Walmsley, 1999, Phys. Rev. Lett. 83, 955.  
Branning, D., W. Grice, R. Erdmann, and I. Walmsley, 2000, Phys. Rev. A 62, 013814.  
Braunstein, S., and H. Kimble, 1998, Nature (London) 394, 840.  
Braunstein, S., and A. Mann, 1995, Phys. Rev. A 51, R1727.  
Braunstein, S., and P. van Loock, 2005, Rev. Mod. Phys. 77, 513.  
Brendel, J., N. Gisin, W. Tittel, and H. Zbinden, 1999, Phys. Rev. Lett. 82, 2594.  
Brendel, J., E. Mohler, and W. Martienssen, 1992, Europhys. Lett. 20, 575.  
Briegel, H., and R. Raussendorf, 2001, Phys. Rev. Lett. 86, 910.  
Briegel, H.-J., D. E. Browne, W. Dur, R. Raussendorf, and M. V. den Nest, 2009, Nature Phys. 5, 19.  
Briegel, H.-J., W. Dür, J. Cirac, and P. Zoller, 1998, Phys. Rev. Lett. 81, 5932.

Brouri, R., A. Beveratos, J.-P. Poizat, and P. Grangier, 2000, Opt. Lett. 25, 1294.  
Browne, D., M. Plenio, and S. Huelga, 2003, Phys. Rev. Lett. 91, 067901.  
Browne, D., and T. Rudolph, 2005, Phys. Rev. Lett. 95, 010501.  
Brunel, C., B. Lounis, P. Tamarat, and M. Orrit, 1999, Phys. Rev. Lett. 83, 2722.  
Bruß, D., J. Cirac, P. Horodecki, F. Hulpke, B. Kraus, M. Lewenstein, and A. Sanpera, 2002, J. Mod. Opt. 49, 1399.  
Burnham, D., and D. Weinberg, 1970, Phys. Rev. Lett. 25, 84.  
Cabello, A., 2001a, Phys. Rev. Lett. 86, 1911.  
Cabello, A., 2001b, Phys. Rev. Lett. 87, 010403.  
Cabello, A., 2003, Phys. Rev. Lett. 90, 258902.  
Cabello, A., 2009, Phys. Rev. Lett. 102, 040401.  
Cabello, A., and E. Santos, 1996, Phys. Lett. A 214, 316.  
Cabrillo, C., J. Cirac, P. Garca-Fernandez, and P. Zoller, 1999, Phys. Rev. A 59, 1025.  
Carmichael, H., and D. Walls, 1976a, J. Phys. B 9, L43.  
Carmichael, H., and D. Walls, 1976b, J. Phys. B 9, 1199.  
Carteret, H., A. Higuchi, and A. Sudbery, 2000, J. Math. Phys. (N.Y.) 41, 7932.  
Cerf, N., C. Adami, and P. Kwiat, 1998, Phys. Rev. A 57, R1477.  
Chaneliere, T., D. Matsukevich, S. Jenkins, S.-Y. Lan, T. Kennedy, and A. Kuzmich, 2005, Nature (London) 438, 833.  
Chaneliere, T., D.N. Matsukevich, S.D. Jenkins, S.-Y. Lan, R. Zhao, T.A.B. Kennedy, and A. Kuzmich, 2007, Phys. Rev. Lett. 98, 113602.  
Chen, K., C.-M. Li, Q. Zhang, Y.-A. Chen, A. Goebel, S. Chen, A. Mair, and J.-W. Pan, 2007, Phys. Rev. Lett. 99, 120503.  
Chen, Q., J. Cheng, K.-L. Wang, and J. Du, 2006, Phys. Rev. A 73, 012303.  
Chen, S., Y.-A. Chen, T. Strassel, Z.-S. Yuan, B. Zhao, J. Schmiedmayer, and J.-W. Pan, 2006, Phys. Rev. Lett. 97, 173004.  
Chen, Z.-B., J.-W. Pan, Y.-D. Zhang, C. Brukner, and A. Zeilinger, 2003, Phys. Rev. Lett. 90, 160408.  
Chen, Z.-B., Q. Zhang, X.-H. Bao, J. Schmiedmayer, and J.-W. Pan, 2006, Phys. Rev. A 73, 050302.  
Chen, Z.-B., B. Zhao, Y.-A. Chen, J. Schmiedmayer, and J.-W. Pan, 2007, Phys. Rev. A 76, 022329.  
Chen, Z.-B., B. Zhao, and J.-W. Pan, 2008 (unpublished).  
Chiaverini, J., et al., 2004, Nature (London) 432, 602.  
Childress, L., J. Taylor, A. Srensen, and M. Lukin, 2005, Phys. Rev. A 72, 052330.  
Childress, L., J. Taylor, A. Srensen, and M. Lukin, 2006, Phys. Rev. Lett. 96, 070504.  
Choi, K., H. Deng, J. Laurat, and H. Kimble, 2008, Nature (London) 452, 67.  
Chou, C., J. Laurat, H. Deng, K. Choi, H. de Riedmatten, D. Felinto, and H. Kimble, 2007, Science 316, 1316.  
Chou, C., S. Polyakov, A. Kuzmich, and H. Kimble, 2004, Phys. Rev. Lett. 92, 213601.  
Cinelli, C., M. Barbieri, R. Perris, P. Mataloni, and F. D. Martini, 2005, Phys. Rev. Lett. 95, 240405.  
Cinelli, C., G. D. Nepi, F. D. Martini, M. Barbieri, and P. Mataloni, 2004, Phys. Rev. A 70, 022321.  
Cirac, J., and P. Zoller, 1994, Phys. Rev. A 50, R2799.  
Cirac, J., P. Zoller, H. Kimble, and H. Mabuchi, 1997, Phys. Rev. Lett. 78, 3221.  
Cirel'son,B.,1980,Lett.Math.Phys.4,93.  
Clauser, J., and M. Horne, 1974, Phys. Rev. D 10, 526.  
Clauser, J., and A. Shimony, 1978, Rep. Prog. Phys. 41, 1881.  
Clauser, J.F., M. A. Horne, A. Shimony, and R. A. Holt, 1969, Phys. Rev. Lett. 23, 880.

Coffman, V., J. Kundu, and W. K. Wootters, 2000, Phys. Rev. A 61, 052306.  
B. Darquie, M.J., J. Dingjan, J. Beugnon, S. Bergamini, Y. Sortais, G. Messin, A. Browaeys, and P. Grangier, 2005, Science 309, 454.  
Dawson, C., H. Haselgrove, and M. Nielsen, 2006, Phys. Rev. A 73, 052306.  
Deutsch, D., A. Ekert, R. Jozsa, C. Macchiavello, S. Popescu, and A. Sanpera, 1996, Phys. Rev. Lett. 77, 2818.  
Dewdney, C., P. Holland, and A. Kyprianidis, 1987, J. Phys. A 20, 4717.  
Diedrich, F., and H. Walther, 1987, Phys. Rev. Lett. 58, 203.  
Di Giuseppe, G., L. Haiberger, F. De Martini, and A. V. Sergienko, 1997, Phys. Rev. A 56, R21.  
Dirac, P., 1927, Proc. R. Soc. A 114, 243.  
Divochiy, A., F. Marsili, D. Bitauld, A. Gaggero, R. Leoni, F. Mattioli, A. Korneev, V. Seleznev, N. Kaurova, O. Minaeva, G. Gol'stman, K.G. Lagoudakis, M. Benkhaoul, F. Lévy, and A. Fiore, 2008, Nature Photon. 2, 302.  
Dousse, A., J. Suffczynski, A. Beveratos, O. Krebs, A. Lematre, I. Sagnes, J. Bloch, P. Voisin, and P. Senellart, 2010, Nature (London) 466, 217.  
Dowling, J., 1998, Phys. Rev. A 57, 4736.  
Duan, L.-M., J. Cirac, and P. Zoller, 2002, Phys. Rev. A 66, 023818.  
Duan, L.-M., M. Lukin, J. Cirac, and P. Zoller, 2001, Nature (London) 414, 413.  
Duan, L.-M., and R. Raussendorf, 2005, Phys. Rev. Lett. 95, 080503.  
Dür, W., and H.-J. Briegel, 2003, Phys. Rev. Lett. 90, 067901.  
Dür, W., H.-J. Briegel, J. Cirac, and P. Zoller, 1999, Phys. Rev. A 59, 169.  
Eberhard, P., 1993, Phys. Rev. A 47, R747.  
Edamatsu, K., R. Shimizu, and T. Itoh, 2002, Phys. Rev. Lett. 89, 213601.  
Eibl, M., S. Gaertner, M. Bourennane, C. Kurtsiefer, M. Zukowski, and H. Weinfurter, 2003, Phys. Rev. Lett. 90, 200403.  
Einstein, A., 1905, Ann. Phys. (Leipzig) 322, 132.  
Einstein, A., B. Podolsky, and N. Rosen, 1935, Phys. Rev. 47, 777.  
Eisaman, M., F.M. A. Andre, M. Fleischhauer, A. Zibrov, and M. Lukin, 2005, Nature (London) 438, 837.  
Eisaman, M., L. Childress, F.M. A. Andre, A. Zibrov, and M. Lukin, 2004, Phys. Rev. Lett. 93, 233602.  
Eisenberg, H., G. Khoury, G. Durkin, C. Simon, and D. Bouwmeester, 2004, Phys. Rev. Lett. 93, 193901.  
Ekert, A., 1991, Phys. Rev. Lett. 67, 661.  
Elitzur, A., and L. Vaidman, 1993, Found. Phys. 23, 987.  
Englert, B.-G., C. Kurtsiefer, and H. Weinfurter, 2001, Phys. Rev. A 63, 032303.  
Englund, D., A. Faraon, B. Zhang, Y. Yamamoto, and J. Vucković, 2007, Opt. Express 15, 5550.  
Fattal, D., K. Inoue, J. Vuckovic, C. Santori, G. S. Solomon, and Y. Yamamoto, 2004, Phys. Rev. Lett. 92, 037903.  
Fearn,H.,and R.Loudon,1987,Opt.Commun.64,485.  
Fedrizzi, A., T. Herbst, A. Poppe, T. Jennewein, and A. Zeilinger, 2007, Opt. Express 15, 15377.  
Fedrizzi, A., R. Ursin, T. Herbst, M. Nespoli, R. Prevedel, T. Scheidl, F. Tiefenbacher, T. Jennewein, and A. Zeilinger, 2009, Nature Phys. 5, 389.  
Felinto, D., C. Chou, J. Laurat, E. Schomburg, H. de Riedmatten, and H. Kimble, 2006, Nature Phys. 2, 844.  
Feng, X.-L., Z.-M. Zhang, X.-D. Li, S.-Q. Gong, and Z.-Z. Xu, 2003, Phys. Rev. Lett. 90, 217902.  
Feynman, R., R. Leighton, and M. Sands, 1963, The Feynman Lectures on Physics III (Addison-Wesley, Reading, MA).

Fiorentino, M., T. Kim, and F. Wong, 2005, Phys. Rev. A 72, 012318.  
Fiorentino, M., and F.N.C. Wong, 2004, Phys. Rev. Lett. 93, 070502.  
Fleischhauer, M., A. Imamoglu, and J. Marangos, 2005, Rev. Mod. Phys. 77, 633.  
Fleischhauer, M., and M. Lukin, 2000, Phys. Rev. Lett. 84, 5094.  
Fleischhauer, M., and M. Lukin, 2002, Phys. Rev. A 65, 022314.  
Franson, J., 1989, Phys. Rev. Lett. 62, 2205.  
Freedman, S., and J. Clauser, 1972, Phys. Rev. Lett. 28, 938.  
Fulconis, J., O. Alibart, J.L. O'Brien, W.J. Wadsworth, and J.G. Rarity, 2007, Phys. Rev. Lett. 99, 120501.  
Furusawa, A., J. Srensen, S. Braunstein, C. Fuchs, H. Kimble, and E. Polzik, 1998, Science 282, 706.  
Gao, W.-B., C.-Y. Lu, X.-C. Yao, P. Xu, O. Guhne, Y.-A. Chen, C.-Z. Peng, Z.-B. Chen, and J.-W. Pan, 2010, Nature Phys. 6, 331.  
Gao, W.-B., X.-C. Yao, P. Xu, O. Guhne, C.-Y. Lu, C.-Z. Peng, Z.-B. Chen, and J.-W. Pan, 2010, Phys. Rev. Lett. 104, 020501.  
Garay-Palmett, K., H.J. McGuinness, O. Cohen, J.S. Lundeen, R. Rangel-Rojo, A.B. U'ren, M.G. Raymer, C.J. McKinstrie, S. Radic, and I.A. Walmsley, 2007, Opt. Express 15, 14870.  
Garg,A.,and N.Mermin,1987,Phys.Rev.D35,3831.  
Gasparoni, S., J.-W. Pan, P. Walther, T. Rudolph, and A. Zeilinger, 2004, Phys. Rev. Lett. 93, 020504.  
Genovese,M.,2005,Phys.Rep.413,319  
Genovese, M., and C. Novero, 2002, Eur. Phys. J. D 21, 109.  
Gilchrist, A., A. Hayes, and T. Ralph, 2007, Phys. Rev. A 75, 052328.  
Gill, R., G. Weihs, A. Zeilinger, and M. Zukowski, 2002, Proc. Natl. Acad. Sci. U.S.A. 99, 14632.  
Gisin,N.,1996,Phys.Lett.A210,151.  
Gisin, N., and H. Bechmann-Pasquinucci, 1998, Phys. Lett. A 246, 1.  
Gisin, N., and A. Peres, 1992, Phys. Lett. A 162, 15.  
Gisin, N., G. Ribordy, W. Tittel, and H. Zbinden, 2002, Rev. Mod. Phys. 74, 145.  
Glauber, R., 1963, Phys. Rev. 130, 2529.  
Goebel, A., C. Wagenknecht, Q. Zhang, Y.-A. Chen, K. Chen, J. Schmiedmayer, and J.-W. Pan, 2008, Phys. Rev. Lett. 101, 080403.  
Gong, Y.-X., X.-B. Zou, T.C. Ralph, S.-N. Zhu, and G.-C. Guo, 2010, Phys. Rev. A 81, 052303.  
Gottesman, D., and I. Chuang, 1999, Nature (London) 402, 390.  
Grangier, P., G. Roger, and A. Aspect, 1986, Europhys. Lett. 1, 173.  
Grassl, M., Beth, Th., and Pellizzari, T., 1997, Phys. Rev. A 56, 33.  
Greenberger, D., M. Horne, A. Shimony, and A. Zeilinger, 1990, Am. J. Phys. 58, 1131.  
Greenberger, D., M. Horne, and A. Zeilinger, 1989, Bell's Theorem and Quantum Theory and Conceptions of the Universe (Kluwer Academic, Dordrecht).  
Greenberger, D., M. Horne, and A. Zeilinger, 1993, Phys. Today 46 (8), 22.  
Grice, W., R. Erdmann, I. Walmsley, and D. Branning, 1998, Phys. Rev. A 57, R2289.  
Grice, W., A. U'Ren, and I. Walmsley, 2001, Phys. Rev. A 64, 063815.  
Grice, W., and I. Walmsley, 1997, Phys. Rev. A 56, 1627.  
Groblacher, S., T. Jennewein, A. Vaziri, G. Weihs, and A. Zeilinger, 2006, New J. Phys. 8, 75.  
Groblacher, S., T. Paterek, R. Kaltenbaek, C. Brukner, M. Zukowski, M. Aspelmeyer, and A. Zeilinger, 2007, Nature (London) 446, 871.  
Grover, L., 1997, Phys. Rev. Lett. 79, 325.

Gühne, O., C. Lu, W. Gao, and J. Pan, 2007, Phys. Rev. A 76, 030305.  
Guhne, O., and G. Toth, 2009, Phys. Rep. 474, 1.  
Hadfield, R. H., 2009, Nature Photon. 3, 696.  
Halder, M., A. Beveratos, N. Gisin, V. Scarani, C. Simon, and H. Zbinden, 2007, Nature Phys. 3, 692.  
Halder, M., J. Fulconis, B. Cemlyn, A. Clark, C. Xiong, W.J. Wadsworth, and J.G. rarity, 2009, Opt. Express 17, 4670.  
Hammerer, K., A. Sorensen, and E. Polzik, 2010, Rev. Mod. Phys. 82, 1041.  
Han, Y.-J., R. Raussendorf, and L.-M. Duan, 2007, Phys. Rev. Lett. 98, 150404.  
Hanbury Brown, R. and R.Q. Twiss, 1956, Nature (London) 177, 27.  
Hardy, L., 1992, Phys. Rev. Lett. 68, 2981.  
Hardy, L., 1993, Phys. Rev. Lett. 71, 1665.  
Haroche,S.,1995,Ann.N.Y.Acad.Sci.755,73.  
Hayashi, A., T. Hashimoto, and M. Horibe, 2005, Phys. Rev. A 72, 032325.  
Herzog, T.J., J.G. Rarity, H. Weinfurter, and A. Zeilinger, 1994, Phys. Rev. Lett. 72, 629.  
Hétet, G., B. Buchler, O. Göckl, M. Hsu, A. Akulshin, H.-A. Bachor, and P. Lam, 2008, Opt. Express 16, 7369.  
Hill, S. and W.K. Wootters, 1997, Phys. Rev. Lett. 78, 5022.  
Hofmann, H., and S. Takeuchi, 2002, Phys. Rev. A 66, 024308.  
Holevo, A., 1973, Probl. Inf. Transm. 9, 177, http://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid:=ppi&paperid:=903&option-lang=eng.  
Holman, K., D. D. Hudson, J. Ye, and D. Jones, 2005, Opt. Lett. 30, 1225.  
Hong, C., and L. Mandel, 1985, Phys. Rev. A 31, 2409.  
Hong, C., Z. Ou, and L. Mandel, 1987, Phys. Rev. Lett. 59, 2044.  
Honjo, T., H. Takesue, H. Kamada, Y. Nishida, O. Tadanaga, M. Asobe, and K. Inoue, 2007, Opt. Express 15, 13957.  
Horne, M., A. Shimony, and A. Zeilinger, 1989, Phys. Rev. Lett. 62, 2209.  
Horne, M., A. Shimony, and A. Zeilinger, 1990, Nature (London) 347, 429.  
Horne, M., and A. Zeilinger, 1986, Ann. N.Y. Acad. Sci. 480, 469.  
Horne, M.A., and A. Zeilinger, 1985, Symposium on the Foundations of Modern Physics and Joensuu and P. Lahti and P. Mittelstaedt (World Scientific, Singapore).  
Horodecki, R., P. Horodecki, and M. Horodecki, 1995, Phys. Lett. A 200, 340.  
Horodecki, R., P. Horodecki, and M. Horodecki, 1996, Phys. Lett. A 223, 1.  
Horodecki, R., P. Horodecki, and M. Horodecki, 1998, Phys. Rev. Lett. 80, 5239.  
Horodecki, R., P. Horodecki, M. Horodecki, and K. Horodecki, 2009, Rev. Mod. Phys. 81, 865.  
Howell, J., A. Lamas-Linares, and D. Bouwmeester, 2002, Phys. Rev. Lett. 88, 030401.  
Hübel, H., M. Vanner, T. Lederer, B. Blauensteiner, T. Lorunser, A. Poppe, and A. Zeilinger, 2007, Opt. Express 15, 7853.  
Hwang, W., 2003, Phys. Rev. Lett. 91, 057901.  
Irvine, M.W.T., J.F. Hodelin, C. Simon, and D. Bouwmeester, 2005, Phys. Rev. Lett. 95, 030401.  
Jacobson, J., G. Björk, I. Chuang, and Y. Yamamoto, 1995, Phys. Rev. Lett. 74, 4835.  
James, D.F.V., P.G. Kwiat, W.J. Munro, and A.G. White, 2001, Phys. Rev. A 64, 052312.  
Jennewein, T., U. Achleitner, C. Simon, G. Weihs, H. Weinfurter, and A. Zeilinger, 2000, Rev. Sci. Instrum. 71, 1675.

Jennewein, T., G. Weihs, J.-W. Pan, and A. Zeilinger, 2001, Phys. Rev. Lett. 88, 017903.  
Jiang, L., A. Rey, O. Romero-Isart, J. García-Ripoll, A. Sanpera, and M. Lukin, 2009, Phys. Rev. A 79, 022309.  
Jiang, L., J. Taylor, and M. Lukin, 2007, Phys. Rev. A 76, 012301.  
Jin, X.-M., J.-G. Ren, B. Yang, Z.-H. Yi, F. Zhou, X.-F. Xu, S.-K. Wang, D. Yang, Y.-F. Hu, S. Jiang, T. Yang, H. Yin, K. Chen, C.-Z. Peng, and J.-W. Pan, 2010, Nature Photon. 4, 376.  
Julsgaard, B., J. Sherson, J. Cirac, J. Fiurasek, and E. Polzik, 2004, Nature (London) 432, 482.  
Kaltenbaek, R., B. Blauensteiner, M. Zukowski, M. Aspelmeyer, and A. Zeilinger, 2006, Phys. Rev. Lett. 96, 240502.  
Kaltenbaek, R., R. Prevedel, M. Aspelmeyer, and A. Zeilinger, 2009, Phys. Rev. A 79, 040302(R).  
Kardynal, B. E., Z. L. Yuan, and A. J. Shields, 2008, Nature Photon. 2, 425.  
Karlsson, A., and M. Bourennane, 1998, Phys. Rev. A 58, 4394.  
Kash, M., V. Sautenkov, A. Zibrov, L. Hollberg, G. Welch, M. Lukin, Y. Rostovtsev, E. Fry, and M. Scully, 1999, Phys. Rev. Lett. 82, 5229.  
Kaszlikowski, D., P. Gnaciński, M. Zukowski, W. Miklaszewski, and A. Zeilinger, 2000, Phys. Rev. Lett. 85, 4418.  
Keller, M., B. Lange, K. Hayasaka, W. Lange, and H. Walther, 2004, Nature (London) 431, 1075.  
Keller, T., and M. Rubin, 1997, Phys. Rev. A 56, 1534.  
Keller, T., M. Rubin, and Y. Shih, 1998, Phys. Lett. A 244, 507.  
Kiesel, N., C. Schmid, G. Toth, E. Solano, and H. Weinfurter, 2007, Phys. Rev. Lett. 98, 063604.  
Kiesel, N., C. Schmid, U. Weber, G. Toth, O. Gühne, R. Ursin, and H. Weinfurter, 2005, Phys. Rev. Lett. 95, 210502.  
Kiesel, N., C. Schmid, U. Weber, R. Ursin, and H. Weinfurter, 2005, Phys. Rev. Lett. 95, 210505.  
Kim, T., M. Fiorentino, and F.N.C. Wong, 2006, Phys. Rev. A 73, 012316.  
Kim, Y.-H., 2003, Phys. Rev. A 67, 040301(R).  
Kim, Y.-H., S. Kulik, and Y. Shih, 2001, Phys. Rev. Lett. 86, 1370.  
Kimble, H., 2008, Nature (London) 453, 1023.  
Kimble, H., M. Dagenais, and L. Mandel, 1977, Phys. Rev. Lett. 39, 691.  
Kimble, H., M. Dagenais, and L. Mandel, 1978, Phys. Rev. A 18, 201.  
Kitaev, A., 2003, Ann. Phys. (N.Y.) 303, 2.  
Klyachko, A.A., M.A. Can, S. Binicioglu, and A.S. Shumovsky, 2008, Phys. Rev. Lett. 101, 20403.  
Klyshko, D., 1967, JETP Lett. 6, 23.  
Klyshko, D., 1988, *Photons and Nonlinear Optics* (Gordon and Breach, New York).  
Klyshko, D., 1993, Phys. Lett. A 172, 399.  
Knill, E., R. Laflamme, and G. Milburn, 2001, Nature (London) 409, 46.  
Koashi, M., T. Yamamoto, and N. Imoto, 2001, Phys. Rev. A 63, 030301.  
Kochen, S., and E. Specker, 1967, J. Math. Mech. 17, 59.  
Kok, P., A. Boto, D. Abrams, C. Williams, S. L. Braunstein, and J. Dowling, 2001, Phys. Rev. A 63, 063407.  
Kok, P., and S. Braunstein, 2000, Phys. Rev. A 61, 042304.  
Kok, P., H. Lee, and J. Dowling, 2002, Phys. Rev. A 65, 052104.  
Kok, P., W. Munro, K. Nemoto, T. Ralph, J. Dowling, and G. Milburn, 2007, Rev. Mod. Phys. 79, 135.  
Korneev, A., Y. Vachtomin, O. Minaeva, A. Divochiy, K. Smirnov, O. Okunev, G. Gol'stman, C. Zinoni, N. Chauvin, L. Balet, F. Marsili, D. Bitauld, B. Alloing, L. Lianhe, A. Fiore, L. Lunghi, A. Gerardino, M. Halder, C. Jorel, C., and H. Zbinden, 2007, IEEE J. Quantum Electron. 13, 944.

Kozhekin, A., K. Mølmer, and E. Polzik, 2000, Phys. Rev. A 62, 033809.  
Krenn, G., and A. Zeilinger, 1996, Phys. Rev. A 54, 1793.  
Kuhn, A., M. Hennrich, and G. Rempe, 2002, Phys. Rev. Lett. 89, 067901.  
Kurtsiefer, C., S. Mayer, P. Zarda, and H. Weinfurter, 2000, Phys. Rev. Lett. 85, 290.  
Kurtsiefer, C., P. Zarda, M. Halder, H. Weinfurter, P. Gorman, P. Tapster, and J. Rarity, 2002, Nature (London) 419, 450.  
Kuzucu, O., and F. N. C. Wong, 2008, Phys. Rev. A 77, 032314.  
Kwiat, P., 1997, J. Mod. Opt. 44, 2173.  
Kwiat, P., S. Barraza-Lopez, A. Stefanov, and N. Gisin, 2001, Nature (London) 409, 1014.  
Kwiat, P., A. Berglund, J. Altepeter, and A. White, 2000, Science 290, 498.  
Kwiat, P., P. Eberhard, A. Steinberg, and R. Chiao, 1994, Phys. Rev. A 49, 3209.  
Kwiat, P., K. Mattle, H. Weinfurter, A. Zeilinger, A. Sergienko, and Y. Shih, 1995, Phys. Rev. Lett. 75, 4337.  
Kwiat, P., A. Steinberg, and R. Chiao, 1993, Phys. Rev. A 47, R2472.  
Kwiat, P., and H. Weinfurter, 1998, Phys. Rev. A 58, R2623.  
Kwiat, P.G., A.M. Steinberg, and R.Y. Chiao, 1992, Phys. Rev. A 45, 7729.  
Laing, A., A. Peruzzo, A. Politi, M. Verde, M. Halder, T. Ralph, M. Thompson, and J. O'Brien, 2010, Appl. Phys. Lett. 97, 211109.  
Laloe, F., 2001, Am. J. Phys. 69, 655.  
Lamas-Linares, A., J. Howell, and D. Bouwmeester, 2001, Nature (London) 412, 887.  
Landau, L., 1987, Phys. Lett. A 120, 54.  
Langford, N., T. Weinhold, R. Prevedel, K. Resch, A. Gilchrist, J. O'Brien, G. Pryde, and A. White, 2005, Phys. Rev. Lett. 95, 210504.  
Lanyon, B.P., M. Barbieri, M.P. Almeida, T. Jennewein, T.C. Ralph, K.J. Resch, G.J. Pryde, J.L. O'Brien, A. Gilchrist, and A.G. White, 2009 Nature Phys. 5, 134.  
Lanyon, B.P., and N.K. Langford, 2009, New J. Phys. 11, 013008.  
Lanyon, B. P., T. J. Weinhold, N. K. Langford, M. Barbieri, D. F. V. James, A. Gilchrist, and A. G. White, 2007, Phys. Rev. Lett. 99, 250505.  
Lanyon, B.P., J.D. Whitfield, G.G. Gillett, M.E. Goggin, M.P. Almeida, I. Kassal, J.D. Biamonte, M. Mohseni, B.J. Powell, M. Barbieri, A. Aspuru-Guzik, and A.G. White, 2010, Nature Chem. 2, 106.  
Lapkiewicz, R., L. Peizhe, S. Christoph, N. Langford, S. Ramelow, M. Wiesniak, and A. Zeilinger, 2011, Nature (London) 474, 490.  
Laskowski, W., M. Wiesniak, M. Zukowski, M. Bourennane, and H. Weinfurter, 2009, J. Phys. B 42, 114004.  
Laurat, J., H. de Riedmatten, D. Felinto, C.-W. Chou, E. Schomburg, and H. Kimble, 2006, Opt. Express 14, 6912.  
Legero, T., T. Wilk, M. Hennrich, G. Rempe, and A. Kuhn, 2004, Phys. Rev. Lett. 93, 070503.  
Leggett, A., 2003, Found. Phys. 33, 1469.  
Leibfried, D., R. Blatt, C. Monroe, and D. Wineland, 2003, Rev. Mod. Phys. 75, 281.  
Lewenstein, M., B. Kraus, J. Cirac, and P. Horodecki, 2000, Phys. Rev. A 62, 052310.  
Lewis, G., 1926, Nature (London) 118, 874.  
Lita, A., A. Miller, and S. Nam, 2008, Opt. Express 16, 3032.  
Liu, C., Z. Dutton, C. Behroozzi, and L. Hau, 2001, Nature (London) 409, 490.  
Lo, H.-K., 2004, Proceedings of IEEE ISIT (IEEE, New York), p. 137.

Lo, H.-K., X. Ma, and K. Chen, 2005, Phys. Rev. Lett. 94, 230504.  
Lounis, B., and W. Moerner, 2000, Nature (London) 407, 491.  
Lounis, B., and M. Orrit, 2005, Rep. Prog. Phys. 68, 1129.  
Lu, C.-Y., D.E. Browne, T. Yang, and J.-W. Pan, 2007, Phys. Rev. Lett. 99, 250504.  
Lu, C.-Y., W.-B. Gao, O. Gühne, X.-Q. Zhou, Z.-B. Chen, and J.-W. Pan, 2009, Phys. Rev. Lett. 102, 030502.  
Lu, C.-Y., W.-B. Gao, J. Zhang, X.-Q. Zhou, T. Yang, and J.-W. Pan, 2008, Proc. Natl. Acad. Sci. U.S.A. 105, 11050.  
Lu, C.-Y., T. Yang, and J.-W. Pan, 2009, Phys. Rev. Lett. 103, 020501.  
Lu, C.-Y., X.-Q. Zhou, O. Gühne, W.-B. Gao, J. Zhang, Z.-S. Yuan, A. Goebel, T. Yang, and J.-W. Pan, 2007, Nature Phys. 3, 91.  
Lukin, M., 2003, Rev. Mod. Phys. 75, 457.  
Lukin, M., and A. Imamoglu, 2001, Nature (London) 413, 273.  
Lukin, M., S. Yelin, and M. Fleischhauer, 2000, Phys. Rev. Lett. 84, 4232.  
Lütkenhaus, N., J. Calsamiglia, and K.-A. Suominen, 1999, Phys. Rev. A 59, 3295.  
Lvovsky, A., 2002, Phys. Rev. Lett. 88, 098901.  
Ma, X.-S., B. Dakic, W. Naylor, A. Zeilinger, and P. Walther, 2011, Nature Phys. 7, 399.  
Madsen, M., D. Moehring, P. Maunz, R. Kohn, Jr., L.-M. Duan, and C. Monroe, 2006, Phys. Rev. Lett. 97, 040505.  
Mair, A., A. Vaziri, G. Weihs, and A. Zeilinger, 2001, Nature (London) 412, 313.  
Mandel, L., 1999, Rev. Mod. Phys. 71, S274.  
Mandel, L., and E. Wolf, 1995, Optical Coherence and Quantum Optics (Cambridge University Press, Cambridge).  
Mann, A., M. Revzen, and W. Schleich, 1992, Phys. Rev. A 46, 5363.  
Marcikic, I., H. de Riedmatten, W. Tittel, V. Scarani, H. Zbinden, and N. Gisin, 2002, Phys. Rev. A 66, 062308.  
Marcikic, I., H. de Riedmatten, W. Tittel, H. Zbinden, and M. Legre, and N. Gisin, 2004, Phys. Rev. Lett. 93, 180502.  
Marcikic, I., H. de Riedmatten, W. Tittel, H. Zbinden, and N. Gisin, 2003, Nature (London) 421, 509.  
Marinatto, L., 2003, Phys. Rev. Lett. 90, 258901.  
Marsili, F., D. Bitauld, A. Fiore, A. Gaggero, F. Mattioli, R. Leoni, M. Benkahoul, and F. Lévy, 2008, Opt. Express 16, 3191.  
Massar, S., and S. Popescu, 1995, Phys. Rev. Lett. 74, 1259.  
Matsukevich, D., T. Chaneliere, S.D. Jenkins, S.-Y. Lan, T. Kennedy, and A. Kuzmich, 2006a, Phys. Rev. Lett. 96, 030405.  
Matsukevich, D., T. Chaneliere, S.D. Jenkins, S.Y. Lan, T. Kennedy, and A. Kuzmich, 2006b, Phys. Rev. Lett. 97, 013601.  
Matsukevich, D., and A. Kuzmich, 2004, Science 306, 663.  
Matsukevich, D., P. Maunz, D. Moehring, S. Olmschenk, and C. Monroe, 2008, Phys. Rev. Lett. 100, 150404.  
Mattle, K., H. Weinfurter, P. Kwiat, and A. Zeilinger, 1996, Phys. Rev. Lett. 76, 4656.  
Maunz, P., D. Moehring, S. Olmschenk, K. Younge, D.N. Matsukevich, and C. Monroe, 2007, Nature Phys. 3, 538.  
Mazurenko, Y., R. Giust, and J. Goedgebuer, 1997, Opt. Commun. 133, 87.  
McKeever, J., A. Boca, A. Boozer, R. Miller, J. Buck, A. Kuzmich, and H. Kimble, 2004, Science 303, 1992.  
Mermin, N., 1990a, Phys. Today 43(6), 9.  
Mermin, N., 1990b, Phys. Rev. Lett. 65, 1838.  
Mermin,N.,1993,Rev.Mod.Phys.65,803  
Mermin, N.D., 1990, Phys. Rev. Lett. 65, 3373.  
Michler, M., K. Mattle, H. Weinfurter, and A. Zeilinger, 1996, Phys. Rev. A 53, R1209.

Michler, M., H. Weinfurter, and M. Zukowski, 2000, Phys. Rev. Lett. 84, 5457.  
Michler, P., A. Kiraz, C. Becher, W. Schoenfeld, P.M. Petroff, L. Zhang, E. Hu, and A. Imamoglu, 2000, Science 290, 2282.  
Mintert, F., A. Carvalho, M. Kus, and A. Buchleitner, 2005, Phys. Rep. 415, 207.  
Mitchell, M., J. Lundeen, and A. Steinberg, 2004, Nature (London) 429, 161.  
Moehring, D., P. Maunz, S. Olmschenk, K. Younge, D.N. Matsukevich, L.-M. Duan, and C. Monroe, 2007, Nature (London) 449, 68.  
Mohseni, M., J. Lundeen, K. Resch, and A. Steinberg, 2003, Phys. Rev. Lett. 91, 187903.  
Molina-Terriza, G., A. Vaziri, J. Rehacek, Z. Hradil, and A. Zeilinger, 2004, Phys. Rev. Lett. 92, 167903.  
Mollow, B., 1973, Phys. Rev. A 8, 2684.  
Mosley, P., J. Lundeen, B. Smith, P. Wasylczyk, A.B. U'Ren, C. Silberhorn, and I. Walmsley, 2008, Phys. Rev. Lett. 100, 133601.  
Nagata, T., R. Okamoto, J. O'Brien, K. Sasaki, and S. Takeuchi, 2007, Science 316, 726.  
Neves, L., G. Lima, J.G.A. Gomez, C.H. Monken, C. Saavedra, and S. Pádua, 2005, Phys. Rev. Lett. 94, 100501.  
Nielsen, M., 2004, Phys. Rev. Lett. 93, 040503.  
Nielsen, M., and I. Chuang, 2000, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, England).  
Nielsen, M., and C. Dawson, 2005, Phys. Rev. A 71, 042323.  
Nielsen, M., E. Knill, and R. Laflamme, 1998, Nature (London) 396, 52.  
Novikova, I., A. Gorshkov, D. Phillips, A. S. rensen, M. Lukin, and R. Walsworth, 2007, Phys. Rev. Lett. 98, 243602.  
O'Brien, J., 2007, Science 318, 1567.  
O'Brien, J., G. Pryde, A. White, T. Ralph, and D. Branning, 2003, Nature (London) 426, 264.  
O'Brien, J. L., A. Furasawa, and J. Vuckovic, 2009, Nature Photon. 3, 687.  
O'Brien, J.L., G.J. Pryde, A. Gilchrist, D.F.V. James, N.K. Langford, T.C. Ralph, and A.G. White, 2004, Phys. Rev. Lett. 93, 080502.  
O'Brien, J. L., G. J. Pryde, A. G. White, and T. C. Ralph, 2005, Phys. Rev. A 71, 060303.  
Okamoto, R., H. Hofmann, S. Takeuchi, and K. Sasaki, 2005, Phys. Rev. Lett. 95, 210506.  
Okamoto, R., J. O'Brien, H. Hofmann, and S. Takeuchi, 2010, arXiv:1006.4743.  
O'Sullivan-Hale, M., I. Khan, R. Boyd, and J. Howell, 2005, Phys. Rev. Lett. 94, 220501.  
Ou, Z., and L. Mandel, 1988a, Phys. Rev. Lett. 61, 54.  
Ou, Z., and L. Mandel, 1988b, Phys. Rev. Lett. 61, 50.  
Pachos, J., 2007, Ann. Phys. (N.Y.) 322, 1254.  
Pachos, J., W. Wieczorek, C. Schmid, N. Kiesel, R. Pohlner, and H. Weinfurter, 2009, New J. Phys. 11, 083010.  
Pan, J.-W., D. Bouwmeester, M. Daniell, H. Weinfurter, and A. Zeilinger, 2000, Nature (London) 403, 515.  
Pan, J.-W., D. Bouwmeester, H. Weinfurter, and A. Zeilinger, 1998, Phys. Rev. Lett. 80, 3891.  
Pan, J.-W., M. Daniell, S. Gasparoni, G. Weihs, and A. Zeilinger, 2001, Phys. Rev. Lett. 86, 4435.  
Pan, J.-W., S. Gasparoni, M. Aspelmeyer, T. Jennewein, and A. Zeilinger, 2003, Nature (London) 421, 721.  
Pan, J.-W., S. Gasparoni, R. Ursin, G. Weihs, and A. Zeilinger, 2003, Nature (London) 423, 417.

Pan, J.-W., C. Simon, C. Brukner, and A. Zeilinger, 2001, Nature (London) 410, 1067.  
Pan, J.-W., and A. Zeilinger, 1998, Phys. Rev. A 57, 2208.  
Patel, R., A. Bennett, I. Farrer, C. Nicoll, D. Ritchie, and A. Shields, 2010, Nature Photon. 4, 632.  
Paterek, T., A. Fedrizzi, S. Gröblacher, T. Jennewein, M. Zukowski, M. Aspelmeyer, and A. Zeilinger, 2007, Phys. Rev. Lett. 99, 210406.  
Paul,H.,1986,Rev.Mod.Phys.58,209.  
Pelton, M., C. Santori, B. Z. J. Vuckovic, G. Solomon, J. Plant, and Y. Yamamoto, 2002, Phys. Rev. Lett. 89, 233602.  
Peng, C.-Z., T. Yang, X.-H. Bao, J. Zhang, X.-M. Jin, F.-Y. Feng, B. Yang, J. Yang, J. Yin, Q. Zhang, N. Li, B.-L. Tian, and J.-W. Pan, 2005, Phys. Rev. Lett. 94, 150501.  
Peng, C.-Z., J. Zhang, D. Yang, W.-B. Gao, H.-X. Ma, H. Yin, H.-P. Zeng, T. Yang, X.-B. Wang, and J.-W. Pan, 2007, Phys. Rev. Lett. 98, 010505.  
Peres,A.,1996,Phys.Rev.Lett.77,1413.  
Peres,A.,2000,J.Mod.Opt.47,531.  
Peres, A., 2002, Quantum Theory: Concepts and Methods (Kluwer Academic Publishers, New York).  
Peruzzo, A., 2010, Science 329, 1500.  
Peters, N., J. Altepeter, D. Branning, E.J., and T.C. Wei, and P. Kwiat, 2004, Phys. Rev. Lett. 92, 133601.  
Phillips, D., A. Fleischhauer, A. Mair, R. Walsworth, and M. Lukin, 2001, Phys. Rev. Lett. 86, 783.  
Pittman, T., and J. Franson, 2003, Phys. Rev. Lett. 90, 240401.  
Pittman, T., B. Jacobs, and J. Franson, 2001, Phys. Rev. A 64, 062311.  
Pittman, T. B., M. J. Fitch, B. C. Jacobs, and J. D. Franson, 2003, Phys. Rev. A 68, 032316.  
Pittman, T.B., D.V. Strekalov, A. Migdall, M.H. Rubin, A.V. Sergienko, and Y.H. Shih, 1996, Phys. Rev. Lett. 77, 1917.  
Politi, A., M. Cryan, J. Rarity, S. Yu, and J. O'Brien, 2008, Science 320, 646.  
Politi, A., J.C.F. Matthews, and J.L. O'Brien, 2009, Science 325, 1221.  
Popescu, S., 1995, arXiv:quant-ph/9501020.  
Popescu, S., L. Hardy, and M. Zukowski, 1997, Phys. Rev. A 56, R4353.  
Preskill, J., 1998, http://www.theory.caltech.edu/people/preskill/ph229/.  
Prevedel, R., G. Cronenberg, M. Tame, M. Paternostro, P. Walther, M. Kim, and A. Zeilinger, 2009, Phys. Rev. Lett. 103, 020503.  
Prevedel, R., M. Tame, A. Stefanov, M. Paternostro, M. Kim, and A. Zeilinger, 2007, Phys. Rev. Lett. 99, 250503.  
Prevedel, R., P. Walther, F. Tiefenbacher, P. Böhi, R. Kaltenbaek, T. Jennewein, and A. Zeilinger, 2007, Nature (London) 445, 65.  
Radmark, M., M. Zukowski, and M. Bourennane, 2009, Phys. Rev. Lett. 103, 150501.  
Radnaev, A., Y.O. Dudin, R. Zhao, H.H. Jen, S.D. Jenkins, A. Kuzmich, and T.A.B. Kennedy, 2010, Nature Phys. 6, 894.  
Raimond, J., M. Brune, and S. Haroche, 2001, Rev. Mod. Phys. 73, 565.  
Ralph, T., A. Hayes, and A. Gilchrist, 2005, Phys. Rev. Lett. 95, 100501.  
Ralph, T., N. Langford, T. Bell, and A. White, 2002, Phys. Rev. A 65, 062324.  
Ralph, T., and G.J. Pryde, 2010, Prog. Opt. 54, 209.  
Ralph, T., A. White, W. Munro, and G. Milburn, 2001, Phys. Rev. A 65, 012314.  
Rarity, J., 1995, Ann. N.Y. Acad. Sci. 755, 624.  
Rarity, J., and P. Tapster, 1990, Phys. Rev. Lett. 64, 2495.

Rarity, J., P. Tapster, E. Jakeman, T. Larchuk, R. A. Campos, M. Teich, and B. Saleh, 1990, Phys. Rev. Lett. 65, 1348.  
Rarity, J., P. Tapster, and R. Loudon, 1996, Quantum Interferometry, edited by F. De Martini, G. Denardo, and Y. Shih (VCH, Weinheim, Germany).  
Raussendorf, R., and H. Briegel, 2001, Phys. Rev. Lett. 86, 5188.  
Raussendorf, R., D. Browne, and H. Briegel, 2003, Phys. Rev. A 68, 022312.  
Raussendorf, R., J. Harrington, and K. Goya, 2006, Ann. Phys. (N.Y.) 321, 2242.  
Raussendorf, R., J. Harrington, and K. Goya, 2007, New J. Phys. 9, 199.  
Reck, M., A. Zeilinger, H.J. Bernstein, and P. Bertani, 1994, Phys. Rev. Lett. 73, 58.  
Resch, K., M. Lindenthal, B. Blauensteiner, H. Böhm, A. Fedrizzi, C. Kurtsiefer, A. Poppe, T. Schmitt-Manderbach, M. Taraba, R. Ursin, P. Walther, H. Weier, H. Weinfurter, and A. Zeilinger, 2005, Opt. Express 13, 202.  
Rohde, P., T. Ralph, and W. Munro, 2007, Phys. Rev. A 75, 010302 (R).  
Romero, J., J. Leach, B. Jack, S. Barnett, M. Padgett, and S. Franke-Arnold, 2010, New J. Phys. 12, 123007.  
Rosenberg, D., J. Harrington, P. Rice, P. Hiskett, C. Peterson, R. Hughes, A. Lita, S. Nam, and J. Nordholt, 2007, Phys. Rev. Lett. 98, 010503.  
Rosenberg, D., A. Lita, A. Miller, and S. Nam, 2005, Phys. Rev. A 71, 061803.  
Rosenfeld, W., M. Weber, J. Volz, F. Henkel, M. Krug, A. Cabello, M. Zukowski, and H. Weinfurter, 2009, Adv. Sci. Lett. 2, 469.  
Rowe, M., D. Kielpinski, V. Meyer, C. Sackett, W.M. Itano, C. Monroe, and D.J. Wineland, 2001, Nature (London) 409, 791.  
Roy, S., and V. Singh, 1991, Phys. Rev. Lett. 67, 2761.  
Rubin, M., D. Klyshko, Y. Shih, and A. Sergienko, 1994, Phys. Rev. A 50, 5122.  
Ryff, L., 1997, Am. J. Phys. 65, 1197.  
Sanaka, K., T. Jennewein, J.-W. Pan, K. Resch, and A. Zeilinger, 2004, Phys. Rev. Lett. 92, 017902.  
Sangouard, N., C. Simon, H. de Riedmatten, and N. Gisin, 2009, arXiv:0906.2699.  
Sansoni, L., F. Sciarrino, G. Vallone, P. Mataloni, A. Crespi, R. Ramponi, and R. Osellame, 2010, Phys. Rev. Lett. 105, 200503.  
Santori, C., D. Fattal, G. S. J. Vuckovic, and Y. Yamamoto, 2002, Nature (London) 419, 594.  
Santos, E., 1991, Phys. Rev. Lett. 66, 1388.  
Santos, E., 1992, Phys. Rev. Lett. 68, 2702.  
Schmitt-Manderbach, T., H. Weier, M. Fürst, R. Ursin, F. Tiefenbacher, T. Scheidl, J. Perdigues, Z. Sodnik, C. Kurtsiefer, J.G. rarity, A. Zeilinger, and H. Weinfurter, 2007, Phys. Rev. Lett. 98, 010504.  
Schori, C., B. Julsgaard, J. S. rensen, and E. Polzik, 2002, Phys. Rev. Lett. 89, 057903.  
Schrödinger, E., 1935a, Naturwissenschaften 23, 807.  
Schrödinger, E., 1935b, Naturwissenschaften 23, 823.  
Schrödinger, E., 1935c, Naturwissenschaften 23, 844.  
Schrödinger, E., 1935d, Math. Proc. Cambridge Philos. Soc. 31, 555.  
Schuck, C., G. Huber, C. Kurtsiefer, and H. Weinfurter, 2006, Phys. Rev. Lett. 96, 190501.  
Scully, M., and M. Zubairy, 1997, Quantum Optics (Cambridge University Press, Cambridge, England).  
Scully, M. O., B.-G. Englert, and H. Walther, 1991, Nature (London) 351, 111.

Selleri, F., and A. Zeilinger, 1988, Found. Phys. 18, 1141.  
Sergienko, A., M. Atature, Z. Walton, G. Jaeger, B. Saleh, and M. Teich, 1999, Phys. Rev. A 60, R2622.  
Shelby, R., M. Levenson, S. Perlmutter, R. DeVoe, and D. Walls, 1986, Phys. Rev. Lett. 57, 691.  
Shields, A., 2007, Nature Photon. 1, 215.  
Shih,Y.,2003,Rep.Prog.Phys.66,1009.  
Shih, Y., and C. Alley, 1988, Phys. Rev. Lett. 61, 2921.  
Simon, C., and D. Bouwmeester, 2003, Phys. Rev. Lett. 91, 053601.  
Simon, C., and W. Irvine, 2003, Phys. Rev. Lett. 91, 110405.  
Simon, C., and J.-W. Pan, 2002, Phys. Rev. Lett. 89, 257901.  
Simon, C., M. Žukowski, H. Weinfurter, and A. Zeilinger, 2000, Phys. Rev. Lett. 85, 1783.  
Sleator, T., and H. Weinfurter, 1995, Phys. Rev. Lett. 74, 4087.  
Sliwa, C., and K. Banaszek, 2003, Phys. Rev. A 67, 030101.  
Slusher, R., L. Hollberg, B. Yurke, J. Mertz, and J. F. Valley, 1985, Phys. Rev. Lett. 55, 2409.  
Smithey, D., M. Beck, M. Belsley, and M. Raymer, 1992, Phys. Rev. Lett. 69, 2650.  
Specker, E. P., 1960, Dialectica 14, 239.  
Stefanov, A., H. Zbinden, N. Gisin, and A. Suarez, 2002, Phys. Rev. Lett. 88, 120404.  
Stefanov, A., H. Zbinden, N. Gisin, and A. Suarez, 2003, Phys. Rev. A 67, 042115.  
Stevenson, R., R. Young, P. Atkinson, K. Cooper, D. Ritchie, and A. Shields, 2006, Nature (London) 439, 179.  
Strauf, S., N. Stoltz, M. Rakher, L. Coldren, P.M. Petroff, and D. Bouwmeester, 2007, Nature Photon. 1, 704.  
Sun, F. W., B. H. Liu, Y. F. Huang, Z. Y. Ou, and G. C. Guo, 2006, Phys. Rev. A 74, 033812.  
Sun, P., Y. Mazurenko, and Y. Fainman, 1995, Opt. Lett. 20, 1062.  
Takesue, H., S. Nam, Q. Zhang, R. Hadfield, T. Honjo, K. Tamaki, and Y. Yamamoto, 2007, Nature Photon. 1, 343.  
Tame, M. S., M. Paternostro, and M. S. Kim, 2007, New J. Phys. 9, 201.  
Tame, M., R. Prevedel, M. Paternostro, P.Bohi, M. Kim, and A. Zeilinger, 2007, Phys. Rev. Lett. 98, 140501.  
Taylor, G., 1909, Proc. Camb. Phil. Soc. Math. Phys. Sci. 15, 114.  
Terhal,B.,2000,Phys.Lett.A271,319.  
Tittel, W., J. Brendel, H. Zbinden, and N. Gisin, 1998, Phys. Rev. Lett. 81, 3563.  
Tittel, W., and G. Weihs, 2001, Quantum Inf. Comput. 1, 3.  
Tokunaga, Y., S. Kuwashiro, T. Yamamoto, M. Koashi, and N. Imoto, 2008, Phys. Rev. Lett. 100, 210501.  
Torgerson, J., D. Branning, C. Monken, and L. Mandel, 1995, Phys. Lett. A 204, 323.  
Torres, J., A. Alexandrescu, and L. Torner, 2003, Phys. Rev. A 68, 050301.  
Torres, J., S. C. F. Macia, and L. Torner, 2005, Opt. Lett. 30, 314.  
Toth, G., and O. Gühne, 2005, Phys. Rev. Lett. 94, 060501.  
U'Ren, A., K. Banaszek, and I. Walmsley, 2003, Quantum Inf. Comput. 3, 480.  
Ursin, R., T. Jennewein, M. Aspelmeyer, R. Kaltenbaek, M. Lindenthal, P. Walther, and A. Zeilinger, 2004, Nature (London) 430, 849.  
Ursin, R., F. Tiefenbacher, T. Schmitt-Manderbach, H. Weier, T. Scheidl, M. Lindenthal, B. Blauensteiner, T. Jennewein, J. Perdigues, P. Trojek, B. Omer, M. Fürst, M. Meyenburg, J. rarity, Z. Sodnik, C. Barbieri, H. Weinfurter, and A. Zeilinger, 2007, Nature Phys. 3, 481.  
Vaidman, L., and N. Yoran, 1999, Phys. Rev. A 59, 116.  
Vallone, G., E. Pomarico, and F. D. Martini, 2008, Phys. Rev. A 78, 042335.

Vandersypen, L., M. Steffen, G. Breyta, C. Yannoni, M. Sherwood, and I. Chuang, 2001, Nature (London) 414, 883.  
van der Wal, C., M. Eisaman, A. Andre, R. Walsworth, D. Phillips, A. Zibrov, and M. Lukin, 2003, Science 301, 196.  
van Enk, S., J. Cirac, and P. Zoller, 1997, Phys. Rev. Lett. 78, 4293.  
van Loock, P., T. Ladd, K. Sanaka, F. Yamaguchi, K. Nemoto, W. Munro, and Y. Yamamoto, 2006, Phys. Rev. Lett. 96, 240501.  
Varnava, M., D. Browne, and T. Rudolph, 2006, Phys. Rev. Lett. 97, 120501.  
Varnava, M., D. Browne, and T. Rudolph, 2008, Phys. Rev. Lett. 100, 060502.  
Vaziri, A., J.-W. Pan, T. Jennewein, G. Weihs, and A. Zeilinger, 2003, Phys. Rev. Lett. 91, 227902.  
Vaziri, A., G. Weihs, and A. Zeilinger, 2002, Phys. Rev. Lett. 89, 240401.  
Verstraete, F., J. Dehaene, and B. DeMoor, 2001, Phys. Rev. A 64, 010101(R).  
Vertesi, T., S. Pironio, and N. Brunner, 2010, Phys. Rev. Lett. 104, 060401.  
Volz, J., M. Weber, D. Schlenk, W. Rosenfeld, J. Vrana, K. Saucke, C. Kurtsiefer, and H. Weinfurter, 2006, Phys. Rev. Lett. 96, 030404.  
Wagenknecht, C., C.-M. Li, A. Reingruber, X.-H. Bao, A. Goebel, Y.-A. Chen, Q. Zhang, K. Chen, and J.-W. Pan, 2010, Nature Photon. 4, 549.  
Waks, E., A. Zeevi, and Y. Yamamoto, 2002, Phys. Rev. A 65, 052310.  
Walborn, S., S. Pádua, and C. Monken, 2003, Phys. Rev. A 68, 042313.  
Walls, D., and G. Milburn, 1994, Quantum Optics (Springer-Verlag, Berlin).  
Walther, H., B. Varcoe, B.-G. Englert, and T. Becker, 2006, Rep. Prog. Phys. 69, 1325.  
Walther, P., J.-W. Pan, M. Aspelmeyer, R. Ursin, S. Gasparoni, and A. Zeilinger, 2004, Nature (London) 429, 158.  
Walther, P., K. Resch, C. Brukner, A. Steinberg, J.-W. Pan, and A. Zeilinger, 2005, Phys. Rev. Lett. 94, 040504.  
Walther, P., K. Resch, T. Rudolph, E. Schenck, H. Weinfurter, V. Vedral, M. Aspelmeyer, and A. Zeilinger, 2005, Nature (London) 434, 169.  
Walton, Z., M. Booth, A. Sergienko, B. Saleh, and M. Teich, 2003, Phys. Rev. A 67, 053810.  
Walton, Z., A. Sergienko, B. Saleh, and M. Teich, 2004, Phys. Rev. A 70, 052317.  
Wang, X.-B., 2005, Phys. Rev. Lett. 94, 230503.  
Wang, Z.-W., X.-F. Zhou, Y.-F. Huang, Y.-S. Zhang, X.-F. Ren, and G.-C. Guo, 2006, Phys. Rev. Lett. 96, 220505.  
Weihs, G., T. Jennewein, C. Simon, H. Weinfurter, and A. Zeilinger, 1998, Phys. Rev. Lett. 81, 5039.  
Weihs, G., M. Reck, H. Weinfurter, and A. Zeilinger, 1996, Opt. Lett. 21, 302.  
Weinfurter, H., 1994, Europhys. Lett. 25, 559.  
Weinfurter, H., 2000, Adv. At. Mol. Opt. Phys. 42, 489.  
Weinfurter, H., and M. Zukowski, 2001, Phys. Rev. A 64, 010102.  
Weinhold, T., A. Gilchrist, K. Resch, A. Doherty, J. O'Brien, G. Pryde, and A. White, 2008, arXiv:0808.0794.  
Werner, R., 1989, Phys. Rev. A 40, 4277.  
Werner, R., and M. M. Wolf, 2001a, Quantum Inf. Comput. 1(3), 1.  
Werner, R., and M. M. Wolf, 2001b, Phys. Rev. A 64, 032112.  
White, A., D. James, P. Eberhard, and P. Kwiat, 1999, Phys. Rev. Lett. 83, 3103.

White, A.G., D. James, W.J. Munro, and P.G. Kwiat, 2001, Phys. Rev. A 65, 012301.  
Wieczorek, W., N. Kiesel, C. Schmid, and H. Weinfurter, 2009, Phys. Rev. A 79, 022311.  
Wieczorek, W., R. Krischek, N. Kiesel, P. Michelberger, G. Tóth, and H. Weinfurter, 2009, Phys. Rev. Lett. 103, 020504.  
Wieczorek, W., C. Schmid, N. Kiesel, R. Pohlner, O. Guhne, and H. Weinfurter, 2008, Phys. Rev. Lett. 101, 010503.  
Wiesner, S., 1983, SIGACT News 15, 78.  
Wootters,W.K.,1998a,Phys.Rev.Lett.80,2245.  
Wootters, W.K., 1998b, Phil. Trans. R. Soc. A 356, 1717.  
Wootters, W., and W. Zurek, 1982, Nature (London) 299, 802.  
Wu, L.-A., H. Kimble, J. Hall, and H. Wu, 1986, Phys. Rev. Lett. 57, 2520.  
Yamamoto, T., M. Koashi, and N. Imoto, 2001, Phys. Rev. A 64, 012304.  
Yamamoto, T., M. Koashi, S.K. Ozdemir, and N. Imoto, 2003, Nature (London) 421, 343.  
Yang, T., Q. Zhang, T.-Y. Chen, S. Lu, J. Yin, J.-W. Pan, Z.-Y. Wei, J.-R. Tian, and J. Zhang, 2006, Phys. Rev. Lett. 96, 110501.  
Yang, T., Q. Zhang, J. Zhang, J. Yin, Z. Zhao, M. Zukowski, Z.-B. Chen, and J.-W. Pan, 2005, Phys. Rev. Lett. 95, 240406.  
Yao, X.-C., T.-X. Wang, P. Xu, H. Lu, G.-S. Pan, X.-H. Bao, C.-Z. Peng, C.-Y. Lu, Y.-A. Chen, and J.-W. Pan, 2012, Nature Photon. 6, 225.  
Yuan, Z.-S., Y.-A. Chen, S. Chen, B. Zhao, M. Koch, T. Strassel, Y. Zhao, G.-J. Zhu, J. Schmiedmayer, and J.-W. Pan, 2007, Phys. Rev. Lett. 98, 180503.  
Yuan, Z.-S., Y.-A. Chen, B. Zhao, S. Chen, J. Schmiedmayer, and J.-W. Pan, 2008, Nature (London) 454, 1098.  
Yurke, B., and D. Stoler, 1992a, Phys. Rev. Lett. 68, 1251.  
Yurke, B., and D. Stoler, 1992b, Phys. Rev. A 46, 2229.  
Zbinden, H., J. Brendel, N. Gisin, and W. Tittel, 2001, Phys. Rev. A 63, 022111.  
Zeilinger, A., 1981, Am. J. Phys. 49, 882.  
Zeilinger, A., H.J. Bernstein, D.M. Greenberger, M.A. Horne, and M. Zukowski, 1993, Quantum Control and Measurement, edited by H. Ezawa and Y. Murayama (North Holland, Amsterdam) p. 9.  
Zeilinger, A., M. Horne, H. Weinfurter, and M. Zukowski, 1997, Phys. Rev. Lett. 78, 3031.  
Zeilinger, A., G. Weihs, T. Jennewein, and M. Aspelmeyer, 2005, Nature (London) 433, 230.

Zel'dovich, Y., and D. Klyshko, 1969, JETP Lett. 9, 40.  
Zhang, A.-N., C.-Y. Lu, X.-Q. Zhou, Y.-A. Chen, Z.Z., and T. Yang, and J.-W. Pan, 2006, Phys. Rev. A 73, 022330.  
Zhang, Q., X.-H. Bao, C.-Y. Lu, X.-Q. Zhou, T. Yang, T. Rudolph, and J.-W. Pan, 2008, Phys. Rev. A 77, 062316.  
Zhang, Q., A. Goebel, C. Wagenknecht, Y.-A. Chen, B. Zhao, T. Yang, A. Mair, J. Schmiedmayer, and J.-W. Pan, 2006, Nature Phys. 2, 678.  
Zhao, B., Y.-A. Chen, X.-H. Bao, T. Strassel, C.-S. Chuu, X.-M. Jin, J. Schmiedmayer, Z.-S. Yuan, S. Chen, and J.-W. Pan, 2009, Nature Phys. 5, 95.  
Zhao, B., Z.-B. Chen, Y.-A. Chen, J. Schmiedmayer, and J.-W. Pan, 2007, Phys. Rev. Lett. 98, 240502.  
Zhao, R., Y. Dudin, S. Jenkins, C. Campbell, D. Matsukevich, T. Kennedy, and A. Kuzmich, 2009, Nature Phys. 5, 100.  
Zhao, Z., Y.-A. Chen, A.-N. Zhang, T. Yang, H. Briegel, and J.-W. Pan, 2004, Nature (London) 430, 54.  
Zhao, Z., J.-W. Pan, and M. Zhan, 2001, Phys. Rev. A 64, 014301.  
Zhao, Z., T. Yang, Y.-A. Chen, A.-N. Zhang, M.Zukowski, and J.-W. Pan, 2003, Phys. Rev. Lett. 91, 180401.  
Zhao, Z., T. Yang, Y.-A. Chen, A.-N. Zhang, and J.-W. Pan, 2003, Phys. Rev. Lett. 90, 207901.  
Zhao, Z., A.-N. Zhang, Y.-A. Chen, H.Z.J.-F. Du, T. Yang, and J.-W. Pan, 2005, Phys. Rev. Lett. 94, 030501.  
Zukowski,M.,1991,Phys.Lett.A 157,198.  
Zukowski, M., 1993, Phys. Lett. A 177, 290.  
Zukowski, M., 2000, Phys. Rev. A 61, 022109.  
Zukowski, M., and C. Brukner, 2002, Phys. Rev. Lett. 88, 210401.  
Zukowski, M., and D. Kaszlikowski, 1997, Phys. Rev. A 56, R1682.  
Zukowski, M., and J. Pykacz, 1988, Phys. Lett. A 127, 1.  
Zukowski, M., A. Zeilinger, and M.A. Horne, 1997, Phys. Rev. A 55, 2564.  
Zukowski, M., A. Zeilinger, M.A. Horne, and A.K. Ekert, 1993, Phys. Rev. Lett. 71, 4287.  
Zukowski, M., A. Zeilinger, M. Horne, and H. Weinfurter, 1999, Int. J. Theor. Phys. 38, 501.  
Zukowski, M., A. Zeilinger, and H. Weinfurter, 1995, Ann. N.Y. Acad. Sci. 755, 91.  
Zurek,W.,2003,Rev.Mod.Phys.75,715.