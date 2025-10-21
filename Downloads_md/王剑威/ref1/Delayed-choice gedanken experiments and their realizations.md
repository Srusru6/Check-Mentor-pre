# Delayed-choice gedanken experiments and their realizations

Xiao-song Ma*

Institute for Quantum Optics and Quantum Information (IQOJI), Austrian Academy of Sciences, Boltzmanngasse 3, 1090 Vienna, Austria, Department of Electrical Engineering, Yale University, 15 Prospect Street, New Haven, Connecticut 06520, USA, and National Laboratory of Solid State Microstructures, School of Physics, Collaborative Innovation Center of Advanced Microstructures, Nanjing University, Nanjing 210093, China

Johannes Kofler†

Max Planck Institute of Quantum Optics (MPQ), Hans-Kopfermann-Straße 1, 85748 Garching, Germany

Anton Zeilinger

Vienna Center of Quantum Science and Technology (VCQ), University of Vienna, Boltzmanngasse 5, 1090 Vienna, Austria and Institute for Quantum Optics and Quantum Information (IQOQI), Austrian Academy of Sciences, Boltzmanngasse 3, 1090 Vienna, Austria

(published 3 March 2016)

The wave-particle duality dates back to Einstein's explanation of the photoelectric effect through quanta of light and de Broglie's hypothesis of matter waves. Quantum mechanics uses an abstract description for the behavior of physical systems such as photons, electrons, or atoms. Whether quantum predictions for single systems in an interferometric experiment allow an intuitive understanding in terms of the particle or wave picture depends on the specific configuration which is being used. In principle, this leaves open the possibility that quantum systems always behave either definitely as a particle or definitely as a wave in every experimental run by a priori adapting to the specific experimental situation. This is precisely what is tried to be excluded by delayed-choice experiments, in which the observer chooses to reveal the particle or wave character of a quantum system—or even a continuous transformation between the two—at a late stage of the experiment. The history of delayed-choice gedanken experiments, which can be traced back to the early days of quantum mechanics, is reviewed. Their experimental realizations, in particular, Wheeler's delayed choice in interferometric setups as well as delayed-choice quantum erasure and entanglement swapping are discussed. The latter is particularly interesting, because it elevates the wave-particle duality of a single quantum system to an entanglement-separability duality of multiple systems.

# CONTENTS

I. Introduction 2

II. Delayed-choice Gedanken Experiments 3

A. Heisenberg's microscope 3  
B.von Weizsacker,Einstein,and Hermann 4  
C.Bohr's account 4  
D. Wheeler's delayed-choice wave-particle duality gedanken experiment 5  
E. Delayed-choice quantum erasure 6  
F. Delayed-choice entanglement swapping 8  
G.Quantum delayed choice 9

III. Realizations of Delayed-choice Wave-particle Duality Experiments 10

A. First realizations of Wheeler's delayed-choice experiment 10

B. Wheeler's delayed-choice experiment with single particles: Photons and atoms 12  
C. Wheeler's delayed-choice experiment with single photons and spacelike separation 13

IV. Realizations of Delayed-choice Quantum-eraser Experiments 14

A. Photonic quantum erasure 14  
B. Matter-wave quantum erasure 15  
C.Quantum erasure with delayed choice 16  
D. Quantum erasure with active and causally disconnected choice 17  
E.Quantum delayed choice 18  
F. Delayed-choice quantum random walk 20

V. Realizations of Delayed-choice Entanglement-swapping Experiments 20

A. Delayed entanglement swapping 20  
B. Delayed-choice entanglement swapping 21

VI. Conclusion and Outlook 22  
Acknowledgments 23  
References 23

# I. INTRODUCTION

In the 17th century, two different theories of light were developed. While Huygens explained optical phenomena by a theory of waves, Newton put forward a corpuscular description where light consists of a stream of fast particles. At first, the large authority of Newton led to the general acceptance of the corpuscular theory. However, at the beginning of the 19th century, Young demonstrated the wave character of light, in particular, by showing interference fringes in the shadow of a "slip of card, about one-thirtieth of an inch in breadth," formed by the "portions of light passing on each side" (Young, 1804). Many other subsequent experiments further established the wave nature of light, in particular, the discovery of electromagnetic waves with light being a special case.

The picture changed again in 1905, when Einstein explained the photoelectric effect with his hypothesis that light consists of "energy quanta which move without splitting and can only be absorbed or produced as a whole" (Einstein, 1905). These massless corpuscles of light, called photons, carry a specific amount of energy  $E = h\nu$  with  $h$  being Planck's constant and  $\nu$  the light's frequency. In 1909, Taylor performed a low-intensity Young-type experiment, measuring the shadow of a needle with an exposure time of the photographic plate of 3 months (Taylor, 1909). Despite the feeble light with on average less than one photon at a time, the interference pattern was observed.

In 1924, de Broglie postulated that also all massive particles behave as waves (de Broglie, 1924). The wavelength associated with a particle with momentum  $p$  is given by  $\lambda = h / p$ . This wave-particle duality was confirmed experimentally through diffraction of an electron beam at a nickel crystal (Davisson and Germer, 1927) and through diffraction of helium atoms at a crystal face of lithium fluoride (Estermann and Stern, 1930). In 1961, the first nonphotonic double-slit-type experiment was performed using electrons (Joensson, 1961). A good decade later, neutron interference (Rauch, Treimer, and Bonse, 1974) allowed one to measure the quantum-mechanical phase shift caused by the Earth's gravitational field (Colella, Overhauser, and Werner, 1975). In modern interferometric experiments, the wave nature of molecules of approximately 7000 atomic mass units and 1 pm de Broglie wavelength has been demonstrated (Gerlich et al., 2011).

In the language of quantum mechanics, the wave-particle duality is reflected by the superposition principle, i.e., the fact that individual systems are described by quantum states, which can be superpositions of different states with complex amplitudes. In a Young-type double-slit experiment, every quantum system is at one point in time in an equal-weight superposition of being at the left and the right slit. When detectors are placed directly at the slits, the system is found only at one of the slits, reflecting its particle character. At which slit an individual system is found is completely random. If, however, detectors are not placed at the slits but at a larger distance, the superposition state will evolve into a state which gives rise to an interference pattern, reflecting the wave character of the system. This pattern cannot emerge when the state at the slit would have been a mere classical mixture of systems being at the left or the right slit.

![](images/2399340ff017f0b1c6af3a79f399f1420d6e34be82d7d53e7b1a8ba4a79bfd74.jpg)  
FIG. 1. Schematic of a Mach-Zehnder interferometer. A quantum system enters from the left via a semitransparent beam splitter. When detectors are placed in the paths  $a$  and  $b$  inside the interferometer, the system is found in one and only one of the arms with probability  $1/2$  each. This reflects the picture that it traveled one of the two paths as a particle. If, however, detectors are not placed inside the interferometer but at the exit ports  $a'$  and  $b'$  after the second beam splitter, the probability of detection depends on the phase  $\varphi$ . This reflects the view that the system traveled both paths  $a$  and  $b$  as a wave, leading to constructive and destructive interference.

To make things more precise, we consider a situation almost equivalent to the double-slit experiment, namely, quantum systems, e.g., photons, electrons, or neutrons, which enter a Mach-Zehnder interferometer (MZI) (Zehnder, 1891; Mach, 1892) via a semitransparent mirror (beam splitter). We denote the transmitted and reflected arm by  $b$  and  $a$ , respectively (Fig. 1). Let there be a phase shift  $\varphi$  in the reflected arm  $a$ , additionally to a  $\pi/2$  shift due to the reflection. Then the quantum state of the system is a superposition of the two path states with in general complex amplitudes:

$$
| \psi \rangle = \frac {1}{\sqrt {2}} (| b \rangle + i e ^ {i \varphi} | a \rangle). \tag {1}
$$

Whenever one decides to measure through which path the system is traveling by putting detectors into the arms  $a$  and  $b$ , one will find it in one and only one arm, in agreement with its particle character. Until the measurement the system is considered to be in a superposition of both paths. The state  $|\psi\rangle$  determines only the probabilities for the respective outcomes  $a$  and  $b$ . They are given by the squared modulus of the amplitudes and are thus  $p_a = p_b = 1/2$ . If, however, the two paths are recombined on a second beam splitter with outgoing paths  $a'$  and  $b'$ , the quantum state will (up to a global phase) be transformed into

$$
\left| \psi^ {\prime} \right\rangle = \cos \frac {\varphi}{2} \left| a ^ {\prime} \right\rangle - \sin \frac {\varphi}{2} \left| b ^ {\prime} \right\rangle . \tag {2}
$$

This state gives rise to detection probabilities  $p_{a'} = \cos^2\varphi / 2$  and  $p_{b'} = \sin^2\varphi / 2$ . The  $\varphi$ -dependent interference fringes indicate that the system traveled through the interferometer through both arms, reflecting its wave character. Particle and wave behavior are complimentary (Bohr, 1928) in the sense that they can be revealed only in different experimental contexts and not simultaneously (see Sec. II.C).

When two physical systems 1 and 2 interact with each other, they will in general end up in an entangled state, i.e., a (nonseparable) superposition of joint states. An example would be two particles, each of them in a separate interferometer:

$$
\left| \Psi \right\rangle_ {1 2} = \cos \alpha \left| a \right\rangle_ {1} \left| \bar {a} \right\rangle_ {2} + \sin \alpha e ^ {i \varphi} \left| b \right\rangle_ {1} \left| \bar {b} \right\rangle_ {2}. \tag {3}
$$

Here with probability  $\cos^2\alpha$  the first system is in path  $a$  in interferometer 1, and the second system is in path  $\bar{a}$  of interferometer 2. With probability  $\sin^2\alpha$  they are in paths  $b$  and  $\bar{b}$ , respectively. Again, the superposition states  $a\bar{a}$  and  $b\bar{b}$  are distinctly different in character from classical mixtures  $a\bar{a}$  or  $b\bar{b}$ . Entanglement can be studied for multipartite systems, arbitrary high-dimensional state spaces, and for mixed states (Horodecki et al., 2009; Pan et al., 2012). Entanglement also plays a crucial role in Bell tests of local realism (Bell, 1964; Brunner et al., 2014) and it is an essential resource for modern quantum information applications (Nielsen and Chuang, 2000; Horodecki et al., 2009).

Because of the many counterintuitive features of quantum mechanics, a still heavily debated question is which meaning the quantum state has, in particular, whether it is a real physical property or whether it is only a mathematical tool for predicting measurement results. Delayed-choice experiments have particularly highlighted certain peculiarities and non-classical features. In interferometric delayed-choice experiments, the choice whether to observe the particle or wave character of a quantum system can be delayed with respect to the system entering the interferometer. Moreover, it is possible to observe a continuous transformation between these two extreme cases. This rules out the naive classical interpretation that every quantum system behaves either definitely as a particle or definitely as a wave by adapting a priori to the specific experimental situation. Using multipartite states, one can decide a posteriori whether two systems were entangled or separable, showing that, just as "particle" and "wave," also "entanglement" and "separability" are not realistic physical properties carried by the systems.

This review is structured as follows: In Sec. II, we discuss the history of delayed-choice gedanken experiments, regarding both single (wave-particle duality) and multipartite (entanglement) scenarios such as delayed-choice quantum erasure and entanglement swapping. In Secs. III, IV, and V we review their experimental realizations. Section VI contains conclusions and an outlook. Some fractions of this review are based on Ma (2010).

# II. DELAYED-CHOICE GEDANKEN EXPERIMENTS

# A. Heisenberg's microscope

The history of delayed-choice gedanken experiments can be traced back to 1927, when Heisenberg put forward a rudimentary and semiclassical version of the uncertainty relation (Heisenberg, 1927). He visualized a microscope which is used to determine the position of an electron. Because of the Abbe limit the accuracy  $\epsilon_{x}$  of the position measurement is essentially given by the wavelength  $\lambda$  of the light used, and since the resolution gets better with shorter wavelengths, one also often talks about the "gamma ray microscope." Considering the microscope's opening angle  $\varepsilon$  (see Fig. 2), the laws of optics yield the approximate relation  $\epsilon_{x} \sim \lambda / \sin \varepsilon$  for the accuracy. For a position measurement, at least one photon needs to (Compton) scatter from the electron and reach the observer through the microscope. The momentum transfer depends on

![](images/32590a5fdc2745ff50863a5183bd1a5c7de78e046d114c7cbbe21ce849c89c1d.jpg)  
FIG. 2. Heisenberg's microscope drawing from the notes of his 1929 lectures, printed in 1930. A photon with energy  $h\nu$  is scattered at an electron (represented by a dot) and reaches the observer via a microscope with opening angle  $\varepsilon$ . The product of uncertainty of the position measurement and the momentum disturbance is of the order of Planck's constant  $h$ . From Heisenberg, 1991.

the angle of the outgoing photon, which is uncertain within  $\varepsilon$ . The uncertainty of the momentum transfer in  $x$  direction is thus  $\eta_{p} = \sin \varepsilon h / \lambda$  and implies the same uncertainty of the electron momentum. The product of position accuracy and momentum disturbance reads

$$
\epsilon_ {x} \eta_ {p} \sim h. \tag {4}
$$

For Heisenberg, this mathematical relation was a "direct illustrative explanation" (Heisenberg, 1927) of the quantum-mechanical commutation relation  $[\hat{x},\hat{p}_x] = i\hbar$  for the position and momentum operator. He noted (Heisenberg, 1991) (translated from German)

that every experiment, which for instance allows a measurement of the position, necessarily disturbs the knowledge of the velocity to a certain degree.

In the subsequent years, Heisenberg's uncertainty principle was derived accurately within the formalism of quantum mechanics (Kennard, 1927; Weyl, 1928; Robertson, 1929; Schrödinger, 1930). However, the resulting famous inequality

$$
\Delta x \Delta p \geq \hbar / 2 \tag {5}
$$

acquired a different meaning, as it did not involve the notion of disturbance any longer:  $\Delta x$  and  $\Delta p$  are the standard deviations of position and momentum for an ensemble of identically prepared quantum systems. These quantities can be inferred by measuring either the position or the momentum of every system. No sequential or joint measurements are made. Every quantum state predicts intrinsic uncertainties, which

cannot be overcome, that is, which necessarily fulfill Heisenberg's uncertainty relation (5). Experimental observations of ensembles of identically prepared systems confirm these predictions.

More recently, Heisenberg's original derivation in the sense of an error-disturbance relation was revisited in fully quantum-mechanical terms (Ozawa, 2004; Branciard, 2013; Busch, Lahti, and Werner, 2013). In particular, it is now known that Heisenberg's uncertainty appears in three manifestations, namely, (i) for the widths of the position and momentum distributions in any quantum state, (ii) for the inaccuracies of any unsharp joint measurement of both quantities, and (iii) for the inaccuracy of a measurement of one of the quantities and the resulting disturbance in the distribution of the other one (Busch, Heinonen, and Lahti, 2007). Note that these manifestations are in close connection to wave-particle duality and complementarity, as they provide partial information about complementary observables.

# B. von Weizsäcker, Einstein, and Hermann

In 1931, von Weizsäcker gave a detailed account of Heisenberg's thought experiment (von Weizsäcker, 1931). He remarked that one can place the observer not in the image plane, as originally intended, but in the focal plane of the microscope. This constitutes a measurement not of the electron's position but of its momentum. A small but conceptually very important step was made by Einstein (for a similar type of experiment) and Hermann (for the Heisenberg microscope), who made explicit the possibility to delay the choice of measurement after the relevant physical interaction had already taken place (Einstein, 1931; Hermann, 1935). This paved the path for the paradigm of delayed-choice experiments. In an article on the interpretation of quantum mechanics, von Weizsäcker wrote (von Weizsäcker, 1941) (translated from German, italics in the original):

It is not at all the act of physical interaction between object and measuring device that defines which quantity is determined and which remains undetermined, but the act of noticing. If, for example, we observe an electron with initially known momentum by means of a single photon, then we are in principle able, after the photon has traversed the lens, therefore certainly not interacting with the electron any more, to decide, whether we move a photographic plate into the focal plane or the image plane of the lens and thus determine the momentum of the electron after the observation or its position. For here the physical "disturbance" of the photon determines the description of the state of the electron, which is related to it not any more physically but only via the connection of the state probabilities given in the wave function, the physical influence is apparently merely important as technical auxiliary means of the intellectual act of constituting a well-defined observation context.

# C. Bohr's account

We briefly review Bohr's viewpoint on complementarity, measurement, and temporal order in quantum experiments. Already in 1928, Bohr said about the requirement of using both a corpuscular and a wave description for electrons that "we are not dealing with contradictory but complementary pictures of the phenomena" (Bohr, 1928). In his "Discussion with Einstein on epistemological problems in atom physics" (Bohr, 1949) he wrote

Consequently, evidence obtained under different experimental conditions cannot be comprehended within a single picture, but must be regarded as complementary in the sense that only the totality of phenomena exhausts the possible information about the objects.

In other words, "in quantum theory the information provided by different experimental procedures that in principle cannot, because of the physical character of the needed apparatus, be performed simultaneously, cannot be represented by any mathematically allowed quantum state of the system being examined. The elements of information obtainable from incompatible measurements are said to be complementary" (Stapp, 2009).

The term "phenomenon" is defined by Bohr as follows (Bohr, 1949):

As a more appropriate way of expression I advocated the application of the word phenomenon exclusively to refer to the observations obtained under specified circumstances, including an account of the whole experimental arrangement.

Miller and Wheeler (1983) vividly illustrated the concept of "elementary quantum phenomenon" in a cartoon shown in Fig. 3. The sharp tail and head of a dragon correspond to Bohr's "specified circumstances" (the experimental preparation and arrangement) and the result of the observation (the outcome of the experiment), respectively. The body of the dragon, between its head and tail, is unknown and smoky:

![](images/058fad50447062b075aa556e36449e698009619a1487169bd121844ae1aa2142.jpg)  
FIG. 3. The quantum "phenomenon" can be viewed as a "great smoky dragon." From Miller and Wheeler, 1983.

"But about what the dragon does or looks like in between we have no right to speak, either in this or any delayed-choice experiment. We get a counter reading but we neither know nor have the right to say how it came. The elementary quantum phenomenon is the strangest thing in this strange world."

Already in his response to the Einstein-Podolsky-Rosen (EPR) argument (Einstein, Podolsky, and Rosen, 1935), Bohr stresses the experimenter's "freedom of handling the measuring instruments" (Bohr, 1935). Later, he wrote (Bohr, 1949)

It may also be added that it obviously can make no difference as regards observable effects obtainable by a definite experimental arrangement, whether our plans for constructing or handling the instruments are fixed beforehand or whether we prefer to postpone the completion of our planning until a later moment when the particle is already on its way from one instrument to another. In the quantum-mechanical description our freedom of constructing or handling the experimental arrangement finds its proper expression in the possibility of choosing the classically defined parameters entering in any proper application of the formalism.

Therefore, in the language of Heisenberg, von Weizsacker, and Bohr—the main proponents of the Copenhagen interpretation of quantum mechanics—the observer is free to choose at any point in time, even after physical interactions have been completed, the further classical conditions of the experiment. This decision, e.g., the positioning of the detector in the focal or image plane in the Heisenberg microscope experiment, defines which particular of the complementary observables is determined.

# D. Wheeler's delayed-choice wave-particle duality gedanken experiment

The paradigm of delayed-choice experiments was revived by Wheeler (1978) and a series of works between 1979 and 1981 which were merged in Wheeler (1984). To highlight the inherently nonclassical principle behind wave-particle complementarity, he proposed a scheme shown at the top in Fig. 4, where one has a Mach-Zehnder interferometer and a single-photon wave packet as input. After the first half-silvered mirror (beam splitter) on the left, there are two possible paths, indicated by  $2a$  and  $2b$ . Depending on the choice made by the observer, different properties of the photon can be demonstrated. If the observer chooses to reveal the particle nature, he should not insert the second half-silvered mirror  $\left(\frac{1}{2} S\right)$ , as shown at the bottom left in Fig. 4. With perfect mirrors ( $A$  and  $B$ ) and  $100\%$  detection efficiency, both detectors will fire with equal probabilities but only one will fire for every individual photon and that event will be completely random. As Wheeler pointed out, "[...] one counter goes off, or the other. Thus the photon has traveled only one route" (Wheeler, 1984).

On the other hand, if the observer chooses to demonstrate the photon's wave nature, he inserts the beam splitter  $\frac{1}{2} S$  as shown on the bottom right in Fig. 4. For identical beam splitters and zero path difference (or an integer multiple of the

![](images/0e428a56a530de64a34c4ac829f7e241fa5006bd7abb9ab066ade1ffa538fa4e.jpg)

![](images/6e79bf0384f821048e052e87ecb08dcf144fbb3c9cb5b8cf9b35155fea18106b.jpg)  
FIG. 4. Wheeler's delayed-choice gedanken experiment with a single-photon wave packet in a Mach-Zehnder interferometer. Top: The second half-silvered mirror  $(\frac{1}{2} S)$  of the interferometer can be inserted or removed at will. Bottom left: When  $\frac{1}{2} S$  is removed, the detectors allow one to determine through which path the photon propagated. Which detector fires for an individual photon is absolutely random. Bottom right: When  $\frac{1}{2} S$  is inserted, detection probabilities of the two detectors depend on the length difference between the two arms. From Wheeler, 1984.

![](images/d586b7f9217afe51999e174220097255baa4e99c00e8ba735e1e1fbd8e08159d.jpg)

photon wavelength), only the detector on the bottom right will fire. As Wheeler pointed out: “This is evidence of interference [...] evidence that each arriving light quantum has arrived by both routes” (Wheeler, 1984).

One might argue that whether the single-photon wave packet traveled both routes or one route depends on whether the second half-silvered mirror is inserted or not. In order to rule out naive interpretations of that kind, Wheeler proposed a "delayed-choice" version of this experiment, where the choice of which property will be observed is made after the photon has passed the first beam splitter. In Wheeler's words: "In this sense, we have a strange inversion of the normal order of time. We, now, by moving the mirror in or out have an unavoidable effect on what we have a right to say about the already past history of that photon." And: "Thus one decides whether the photon 'shall have come by one route or by both routes' after it has already done its travel" (Wheeler, 1984). Very much along the line of the reasoning of Bohr, one can talk only about a property of the quantum system, for example, wave or particle, after the quantum phenomenon has come to a conclusion. In the situation just discussed, this is only the case after the photon has completely finished its travel and has been registered.

Illustrated in Fig. 5, Wheeler proposed a most dramatic "delayed-choice gedanken experiment at the cosmological scale" (Wheeler, 1984). He explained it as follows:

We get up in the morning and spend the day in meditation whether to observe by "which route" or to observe interference between "both routes." When night comes and the telescope is at last usable we leave the half-silvered mirror out or put it in, according to our choice. The monochromatizing filter placed over the telescope makes the counting rate low. We may have to wait an hour for the first photon. When it triggers a counter, we

![](images/0960e914630b522b375df4f3c05e65002e9ceea40d9523076c6a24d9861188a1.jpg)  
FIG. 5. Delayed-choice gedanken experiment at the cosmological scale. Left: Because of the gravitational lens action of galaxy  $G - 1$ , light generated from a quasar  $(Q)$  has two possible paths to reach the receptor. This mimics the setup in Fig. 4. Center: The receptor setup. Filters are used to increase the coherence length of the light, thus allowing one to perform the interference experiment. A fiber optics delay loop adjusts the phase of the interferometer. Right: The choice to not insert (top) or insert (bottom) the half-silvered mirror at the final stage of the experiment allows one to either measure which particular route the light traveled or what the relative phase of the two routes was when it traveled both of them. Given the distance between the quasar and the receptor (billions of light years), the choice can be made long after the light's entry into the interferometer, an extreme example of the delayed-choice gedanken experiment. From Wheeler, 1984.

discover "by which route" it came with one arrangement; or by the other, what the relative phase is of the waves associated with the passage of the photon from source to receptor "by both routes"—perhaps 50 000 light years apart as they pass the lensing galaxy  $G-1$ . But the photon has already passed that galaxy billions of years before we made our decision. This is the sense in which, in a loose way of speaking, we decide what the photon "shall have done" after it has "already" done it. In actuality it is wrong to talk of the "route" of the photon. For a proper way of speaking we recall once more that it makes no sense to talk of the phenomenon until it has been brought to a close by an irreversible act of amplification: "No elementary phenomenon is a phenomenon until it is a registered (observed) phenomenon."

Given the distance between the quasar and the receptor (billions of light years), the choice is made by the experimenter long after the photon's entry into the cosmic interferometer (i.e., emission by the quasar). The speed of light of intergalactic space is not exactly the vacuum speed of light. Therefore, whether the experimenter's choice is in the timelike future of the emission event or spacelike separated therefrom depends on the size of the interferometer and the amount of time between the choice event and the photon arrival at the

second beam splitter. Depending on the specific parameters, Wheeler's delayed choice can thus be thought of being in the timelike future of, or spacelike separated from, the photon emission.

While Wheeler did not specifically discuss the latter case, it is particularly appealing because it rules out any causal influence from the emission to the choice which might instruct the photon to behave as a particle or as a wave. Note that this resembles the freedom-of-choice loophole (Bell, 2004; Scheidl et al., 2010; Gallicchio, Friedman, and Kaiser, 2014) discussed in the context of Bell tests for the falsification of hidden-variable theories using entangled states of at least two systems. The question in Wheeler's gedanken experiment is about if and when a single quantum system decides to behave as a particle or as a wave. Spacelike separation excludes unknown communication from this decision to the choice of the experimenter.

Although Wheeler suggested employing (thermal) light from a quasar, it is conceptually important to use true single photons rather than thermal light. This is because the indivisible particle nature of single photons guarantees that the two detectors will never click at the same time. Otherwise, one could explain the results by what is often called a semiclassical theory of light, where light propagates as a classical wave and is quantized only at the detection itself (Paul, 1982).

Therefore, important requirements for an ideal delayed-choice wave-particle duality experiment are (1) a free or random choice of measurement with spacelike separation between the choice and the entry of the quantum system into the interferometer, and (2) using single-particle quantum states.

# E. Delayed-choice quantum erasure

Scully and collaborators proposed the so-called quantum eraser (Scully and Druhl, 1982; Scully, Englert, and Walther, 1991), in which an entangled atom-photon system was studied. They considered the scattering of light from two atoms located at sites 1 and 2 and analyzed three different cases (Fig. 6):

(A) A resonant light pulse  $l_{1}$  impinges on two two-level atoms [Fig. 6(A)] located at sites 1 and 2. One of the two atoms is excited to level  $a$  and emits a photon labeled  $\gamma$ , bringing it back to state  $b$ . As it is impossible to know which atom emits  $\gamma$ , because both atoms are finally in the state  $b$ , one obtains interference of these photons at the detector. This is an analog of Young's double-slit experiment.  
(B) In the case of three atomic levels [Fig. 6(B)], the resonant light  $l_{1}$  excites the atoms from the ground state  $c$  to the excited state  $a$ . The atom in state  $a$  can then emit a photon  $\gamma$  and end up in state  $b$ . The other atom remains in level  $c$ . This distinguishability of the atoms' internal states provides which-path information of the photon and no interference can be observed.  
(C) An additional light pulse  $l_{2}$  takes the atom from level  $b$  to  $b^{\prime}$  [Fig. 6(C)]. Then a photon labeled  $\phi$  is

![](images/beb20e2617e188c60e92d63bf6feaf55cd4be0690b45e8b7c173218538c10d8d.jpg)  
FIG. 6. The delayed-choice quantum eraser following Scully and Druhl (1982). (A) Two two-level atoms are initially in the state  $b$ . The incident pulse  $l_{1}$  excites one of the two atoms to state  $a$  from where it decays to state  $b$ , emitting a photon labeled  $\gamma$ . Because the final states of both atoms are identical, one can observe interference of the photons at the detector  $D$ . (B) Two atoms are initially in the ground state  $c$  and one of them is excited by the pulse  $l_{1}$  to state  $a$  from where it decays to state  $b$ . Since the final states of both atoms are different, one cannot observe interference of the photons. (C) A fourth level is added. A pulse  $l_{2}$  excites the atom from state  $b$  to  $b'$ . The atom in  $b'$  emits a photon labeled  $\phi$  and ends up in state  $c$ . If one can detect  $\phi$  in a way that the which-path information is erased, interference can be recovered for photon  $\gamma$ . From Aharonov and Zubairy, 2005.

![](images/8f865942cf15fd31f182be366f05b919bd0abb43588334b01676b16afc7ebab3.jpg)

![](images/197211d176425e854e035e73f50f87dc526ddc80a4d6af039eaa78d8575f967d.jpg)

emitted and the atom ends up in level  $c$ . Now the final state of both atoms is  $c$ , and thus the atoms' internal states cannot provide any which-path information. If one can detect photon  $\phi$  in a way that its spatial origin (thus which-path information of  $\gamma$ ) is erased, interference is recovered. Note that in this case there are two photons: One is  $\gamma$  for interference, and the other one is  $\phi$ , acting as a which-path information carrier. (This resembles closely von Weizsäcker's account of Heisenberg's microscope.)

Scully and Druhl designed a device based on an electro-optical shutter, a photon detector, and two elliptical cavities to implement the above described experimental configuration (C) in a delayed-choice arrangement (Fig. 7). There one can choose to reveal or erase the which-path information after the photon  $\gamma$  has been generated.

In another proposal (Scully, Englert, and Walther, 1991), the interfering system is an atomic beam propagating through two cavities coherently. The atomic state is the quantum superposition  $(|e\rangle_1 + |e\rangle_2) / \sqrt{2}$ , where  $|e\rangle_{i}$  denotes the excited state of the atom passing through cavity  $i = 1, 2$  (see Fig. 8). The excited atom can decay to its ground state  $|g\rangle_{i}$  and emit a photon in state  $|\gamma \rangle_{i}$ . In conjunction with the perfectly reflective shutters, the two cavities, separated by a photon detector wall, are used to trap the photon. Conditional on the emission of one photon  $\gamma$  from the atom in one of the cavities, the state of atom  $(a)$  and photon  $(p)$  becomes

$$
\left| \right. \Phi \left. \right\rangle_ {a p} = \frac {1}{\sqrt {2}} \left( \right.\left| \right. g \left. \right\rangle_ {1} \mid \gamma \left. \right\rangle_ {1} + \left| \right. g \left. \right\rangle_ {2} \mid \gamma \left. \right\rangle_ {2}). \tag {6}
$$

If shutter 1 is open and shutter 2 is closed, detection of a photon (in cavity 1) reveals the atom's position in cavity 1, and vice versa if shutter 2 is open while 1 is closed. Repeating experiments with these two configurations (i.e., only one shutter open) will not lead to an interference

pattern of the atom detections [dashed curve in Fig. 8(a)]. The same pattern will emerge when both shutters remain closed at all times. The lack of interference in both cases is because the which-path information is still present in the Universe, independent of whether an observer takes note of it or not. Ignoring the photon state, which carries which-path information about the atom, leads to a mixed state of the atom from  $(|g\rangle_{1}\langle g| + |g\rangle_{2}\langle g|)/2$  which cannot show an interference pattern.

![](images/e4e69b7c529ba54646c47b76232d08f73366c35dd0cfe77e3132d156a99a2d92.jpg)  
FIG. 7. Proposed delayed-choice quantum-eraser setup. Laser pulses  $l_{1}$  and  $l_{2}$  are incident on atoms at sites 1 and 2. A scattered photon,  $\gamma_{1}$  or  $\gamma_{2}$ , is generated by  $a \rightarrow b$  atomic transition. The atom's decay from  $b' \rightarrow c$  produces a photon  $\phi$ . This corresponds to the situation depicted in Fig. 6(C). In order to operate this experiment in a delayed-choice mode, two elliptical cavities and an electro-optical shutter are employed. The cavities reflect  $\phi$  onto a common detector. The electro-optical shutter transmits  $\phi$  only when the switch is open. By opening or closing the shutter, one can either erase the information which atom (1 or 2) emitted the photon or not. This determines whether one can observe the wave or particle nature of  $\gamma$ . The choice can be delayed with respect to the generation of  $\gamma$ . From Scully and Druhl, 1982.

![](images/e9cf30f8600151d13a969c1b96b982b8517dd2cf08db1ebcd597c18a3cbb7994.jpg)  
FIG. 8. Proposed quantum-eraser setup. A detector wall, separating two cavities for microwave photons, is sandwiched by two electro-optic shutters. (a) By always opening only one of the shutters, the photon detections reveal the cavity where the photon was emitted and, thus, which-path information for the atoms. Consequently, no interference pattern emerges. When opening both shutters the photon detections will erase which-path information of the atoms and interference shows up. (b) Both shutters are open. It is assumed that the detector wall can be excited only by the symmetric photon state  $|+ \rangle_{12}$ . Hence, if a photon is being emitted in one of the cavities but not detected, it was in the antisymmetric state  $|- \rangle_{12}$ . The detections of the symmetric and antisymmetric photon state give rise to oppositely modulated interference fringes of the atoms (solid and dashed curves), respectively. From Scully, Englert, and Walther, 1991.

However, Eq. (6) can also be written as

$$
\left| \Phi \right\rangle_ {a p} = \frac {1}{2} \left(\left| g \right\rangle_ {1} + \left| g \right\rangle_ {2}\right) | + \rangle_ {1 2} + \frac {1}{2} \left(\left| g \right\rangle_ {1} - \left| g \right\rangle_ {2}\right) | - \rangle_ {1 2}, \tag {7}
$$

with the symmetric and antisymmetric photon states  $| + \rangle_{12} = (|\gamma \rangle_1 + |\gamma \rangle_2) / \sqrt{2}$  and  $| - \rangle_{12} = (|\gamma \rangle_1 - |\gamma \rangle_2) / \sqrt{2}$ . If one opens both shutters and detects the symmetric photon state  $| + \rangle_{12}$ , one cannot in principle distinguish which cavity the atom propagated through as its state is the coherent superposition  $(|g\rangle_1 + |g\rangle_2) / \sqrt{2}$ . Detection of the photon in the state  $| + \rangle_{12}$  has erased the which-path information of the atom. Therefore, interference in the atom detections shows up again [solid curves in Figs. 8(a) and 8(b)]. If one detects the antisymmetric photon state  $| - \rangle_{12}$ , the atomic state becomes a superposition with a different relative phase between the two paths  $(|g\rangle_1 - |g\rangle_2) / \sqrt{2}$ , leading to a shift of the interference pattern [dashed curve in Fig. 8(b)]. Scully, Englert, and Walther (1991) assumed that the detector has perfect detection efficiency but cannot be excited by the antisymmetric photon state, which is why the shifted interference pattern emerges in the case of both shutters being open and no eraser photon being detected. The detector wall used here is sufficiently thin such that it cannot distinguish which side the photon has impinged on and hence is able to collapse the photons' superposition states into the symmetric or antisymmetric state. It is important to note that the interference patterns of the atoms can be seen only in coincidence with the corresponding photon projections into the symmetric or antisymmetric states.

This gedanken experiment triggered a controversial discussion on whether complementarity is more fundamental than the uncertainty principle (Storey et al., 1994, 1995; Englert, Scully, and Walther, 1995). Wiseman and colleagues reconciled divergent opinions and recognized the novelty of the quantum-eraser concept (Wiseman and Harrison, 1995; Wiseman et al., 1997). Experimental demonstrations of quantum erasure for atomic systems were realized by Eichmann et al. (1993) and Durr, Nonn, and Rempe (1998) and are reviewed in Sec. IV.B.

A delayed-choice configuration can be arranged in this experiment: one can choose to reveal or erase the which-path information of the atoms (by not opening or opening both shutters) after the atom finishes the propagation through the two cavities.

A detailed analysis of the fundamental aspects of single-particle interference experiments facing decoherence was reported by Scully, Englert, and Schwinger (1989). They considered the quantum (system-apparatus) correlations which are at the root of decoherence rather than the recoil or collision. This topic is further discussed in Secs. III and IV.

# F. Delayed-choice entanglement swapping

When two systems are in an entangled quantum state, the correlations of the joint system are well defined but not the properties of the individual systems (Einstein, Podolsky, and Rosen, 1935; Schrödinger, 1935). Peres (2000) raised the question of whether it is possible to produce entanglement between two systems even after they have been registered by detectors. Remarkably, quantum mechanics allows this via entanglement swapping (Zukowski et al., 1993). We note that Cohen (1999) had previously analyzed a similar situation in the context of counterfactual entanglement generation in separable states.

In a photonic implementation of entanglement swapping, two pairs of polarization-entangled photons, 1 and 2, and 3 and 4, are produced from two different EPR sources (Fig. 9). The initial four-photon entangled state is of the form

$$
\left| \Psi \right\rangle_ {1 2 3 4} = \left| \Psi^ {-} \right\rangle_ {1 2} \left| \Psi^ {-} \right\rangle_ {3 4}, \tag {8}
$$

where  $|\Psi^{-}\rangle_{ij} = (|H\rangle_i|V\rangle_j - |V\rangle_i|H\rangle_j) / \sqrt{2}$  are the entangled antisymmetric Bell (singlet) states of photons  $i$  and  $j$ .  $H$  and  $V$  denote horizontal and vertical polarization, respectively. While photon 1 is sent to Alice and photon 4 is sent to Bob, photons 2 and 3 propagate to Victor.

Alice and Bob perform polarization measurements on photons 1 and 4, choosing freely between the three mutually unbiased bases (Wootters and Fields, 1989)  $|H\rangle / |V\rangle$ ,  $|R\rangle / |L\rangle$ , and  $|+ \rangle / |- \rangle$ , with  $|R\rangle = (|H\rangle + i|V\rangle) / \sqrt{2}$ ,  $|L\rangle = (|H\rangle - i|V\rangle) / \sqrt{2}$ , and  $|\pm \rangle = (|H\rangle \pm |V\rangle) / \sqrt{2}$ . If Victor chooses to measure his two photons 2 and 3 separately in the  $H / V$  basis, i.e., in the basis of separable (product) states  $|H\rangle_2|H\rangle_3$ ,  $|H\rangle_2|V\rangle_3$ ,  $|V\rangle_2|H\rangle_3$ , and  $|V\rangle_2|V\rangle_3$ , then the answer of the experiment is one of the four random results. Upon Victor's measurement, photons 1 and 4 will also remain separable and be projected into the corresponding product state  $|V\rangle_1|V\rangle_4$ ,  $|V\rangle_1|H\rangle_4$ ,  $|H\rangle_1|V\rangle_4$ ,

![](images/8ad1edab108c82f39ffaa966dd6ca8a828ddf72d33465b6876665270a29cfddb.jpg)  
FIG. 9. The concept of delayed-choice entanglement swapping. Two entangled pairs of photons 1 and 2, and 3 and 4 are produced in the joint state  $|\Psi^{-}\rangle_{12}|\Psi^{-}\rangle_{34}$  from the EPR sources I and II, respectively. Alice and Bob perform polarization measurements on photons 1 and 4 in any of the three mutually unbiased bases and record the outcomes. Victor has the freedom of performing either an entangled- or a separable-state measurement on photons 2 and 3. If Victor decides to perform a separable-state measurement in the four-dimensional two-particle basis  $\{|H\rangle_2|H\rangle_3, |H\rangle_2|V\rangle_3, |V\rangle_2|H\rangle_3, |V\rangle_2|V\rangle_3\}$ , then the outcome is random and one of these four product states. Photons 1 and 4 are projected into the corresponding product state and remain separable. On the other hand, if Victor chooses to perform an entangled-state measurement on photons 2 and 3 in the Bell-state basis  $\{|\Psi^{+}\rangle_{23}, |\Psi^{-}\rangle_{23}, |\Phi^{+}\rangle_{23}, |\Phi^{-}\rangle_{23}\}$ , then the random result is one of the four Bell states. Consequently, photons 1 and 4 are also projected into the corresponding Bell state. Therefore, entanglement is swapped from pairs 1 and 2, and 3 and 4 to pairs 2 and 3, and 1 and 4. Adapted from Ma et al., 2012.

or  $|H\rangle_1|H\rangle_4$ , respectively. Alice's and Bob's polarization measurements are thus correlated only in the  $|H\rangle / |V\rangle$  basis.

However, Eq. (8) can also be written in the basis of Bell states of photons 2 and 3:

$$
\begin{array}{l} \left| \Psi \right\rangle_ {1 2 3 4} = \frac {1}{2} \left(\left| \Psi^ {+} \right\rangle_ {1 4} \left| \Psi^ {+} \right\rangle_ {2 3} - \left| \Psi^ {-} \right\rangle_ {1 4} \left| \Psi^ {-} \right\rangle_ {2 3} \right. \\ - \left| \Phi^ {+} \right\rangle_ {1 4} \left| \Phi^ {+} \right\rangle_ {2 3} - \left| \Phi^ {-} \right\rangle_ {1 4} \left| \Phi^ {-} \right\rangle_ {2 3}, \tag {9} \\ \end{array}
$$

with the entangled symmetric Bell (triplet) states  $|\Psi^{+}\rangle_{ij} = (|H\rangle_i|V\rangle_j + |V\rangle_i|H\rangle_j / \sqrt{2}$ , and  $|\Phi^{\pm}\rangle_{ij} = (|H\rangle_i|H\rangle_j\pm |V\rangle_i|V\rangle_j / \sqrt{2}$ . When Victor decides to perform a Bell-state measurement (BSM), i.e., when he measures in the basis of entangled states  $|\Psi^{+}\rangle_{23}$ ,  $|\Psi^{-}\rangle_{23}$ ,  $|\Phi^{+}\rangle_{23}$ , and  $|\Phi^{-}\rangle_{23}$ , then the answer of the experiment is one of the four random results. Alice's and Bob's photons are then projected into the

corresponding entangled state  $|\Psi^{+}\rangle_{14}$ ,  $|\Psi^{-}\rangle_{14}$ ,  $|\Phi^{+}\rangle_{14}$ , or  $|\Phi^{-}\rangle_{14}$ , respectively. Alice's and Bob's polarization measurements are thus correlated in all possible bases. This implies that Victor can establish entanglement between photons 1 and 4, although they have never interacted nor share any common past. After entanglement swapping, pairs 1 and 2, and 3 and 4 are no longer entangled, obeying the monogamy of entanglement (Coffman, Kundu, and Wootters, 2000).

Peres suggested an addition to the entanglement-swapping protocol, thereby combining it with Wheeler's delayed-choice paradigm. He proposed that the correlations of photons 1 and 4 can be defined even after they have been detected via a later projection of photons 2 and 3 into an entangled state. According to Victor's choice and his results, Alice and Bob can sort their already recorded data into subsets and can verify that each subset behaves as if it consisted of either entangled or separable pairs of distant photons, which have neither communicated nor interacted in the past. Such an experiment leads to the seemingly paradoxical situation, that "entanglement is produced a posteriori, after the entangled particles have been measured and may even no longer exist" (Peres, 2000).

Since the property whether the quantum state of photons 1 and 4 is separable or entangled can be freely decided by Victor's choice of applying a separable-state or Bell-state measurement on photons 2 and 3 after photons 1 and 4 have already been measured, the delayed-choice wave-particle duality of a single particle is brought to an entanglement-separability duality of two particles.

# G. Quantum delayed choice

Wheeler's delayed-choice experiment [Fig. 10(a)] of a photon in an interferometer with phase  $\varphi$  can be translated into the language of quantum circuits (Nielsen and Chuang, 2000), where Hadamard gates represent the beam splitters and an ancilla is used in a quantum random number generator (QRNG) for making the choice [Fig. 10(b)]. A quantum version of this experiment was suggested (Ioniciou and Terno, 2011), where the ancilla can coherently control the second beam splitter of the interferometer [Fig. 10(c)]. Bias can be achieved by more general ancilla states  $\cos \alpha |0\rangle +\sin \alpha |1\rangle$  with amplitudes depending on a parameter  $\alpha$  [Fig. 10(d)]. By this, the second beam splitter can be in a superposition of being present and absent. Following the language of Wheeler, the photon must consequently be in a superposition of particle and wave at the same time. Moreover, one can arbitrarily choose the temporal order of the measurements. In particular, if one measures the ancilla after the photon, the latter can be described as having behaved as a particle or as a wave after it has already been detected. From the experimental point of view, it is advantageous that no fast switching of any devices is required.

With an appropriate alignment of the interferometer, before the detectors in Fig. 2(d) the state of the photon and the ancilla reads

$$
| \Psi \rangle = \cos \alpha | \text {p a r t i c l e} \rangle | 0 \rangle + \sin \alpha | \text {w a v e} \rangle | 1 \rangle , \tag {10}
$$

with the photon states

![](images/29f55e944ea681edf9a6ead1d61f1187aef85ebd028e8a14fc8824d857604687.jpg)  
(a)

![](images/6e39ecadb5f30624d35df32f080980c02bcd44da901bfc069a26360639951d02.jpg)  
(b)

![](images/769cc5e311af8aad2424ebe738895ea6a2bd3f341a1c680decac61b648229ba4.jpg)  
(c)  
FIG. 10. (a) The "classical" delayed-choice experiment: The second beam splitter  $\mathrm{BS}_2$  is inserted or not after the photon has already entered the interferometer. (b) An equivalent quantum network: An ancilla (lower input) acts as a quantum random number generator (QRNG). Its initial state  $|0\rangle$  is transformed by a Hadamard gate  $H$  into  $(|0\rangle + |1\rangle) / \sqrt{2}$ . A measurement in the computational  $|0\rangle / |1\rangle$  basis gives a random outcome, which determines whether or not the second Hadamard gate is applied with the system qubit (equivalent to  $\mathrm{BS}_2$ ). (c) Delayed choice with a quantum beam splitter: The second beam splitter  $\mathrm{BS}_2$  (represented by a controlled Hadamard gate) is coherently controlled by the state of the ancilla qubit. It is now in the superposition of present and absent. (d) The QRNG can be biased by preparing the ancilla in the state  $\cos \alpha |0\rangle + \sin \alpha |1\rangle$ . From Ionicioiu and Terno, 2011.

![](images/e2625dc02c6d344220c14a617adabb4d1105cdae4b43fabab34b6746eb13b8d5.jpg)  
(d)

$$
| \text {p a r t i c l e} \rangle = \frac {1}{\sqrt {2}} (| 0 \rangle + e ^ {i \varphi} | 1 \rangle), \tag {11}
$$

$$
\left| \text {w a v e} \right\rangle = e ^ {i \varphi / 2} \left(\cos \frac {\varphi}{2} | 0 \rangle + i \sin \frac {\varphi}{2} | 1 \rangle\right). \tag {12}
$$

The overlap between the latter states is  $\langle \mathrm{particle}|\mathrm{wave}\rangle = 2^{-1 / 2}\cos \varphi$ . As  $\varphi$  varies, the probability to find the photon in state 0 is  $I_{p}(\varphi) = 1 / 2$  (visibility  $V = 0$ ) for the particle state and  $I_{w}(\varphi) = \cos^{2}(\varphi /2)$  (visibility  $V = 1$ ) for the wave state. Equation (10) is a quantitative expression of complementarity, and the question whether a system behaves as a wave can now be seen in the language of mutually unbiased bases. If the photon data are analyzed in the respective subenssembles of the ancilla outcomes, they show either perfect particlelike (ancilla in  $|0\rangle$ , photon visibility  $V = 0$ ) or wavelike behavior (ancilla in  $|1\rangle$ , photon visibility  $V = 1$ ).

For an equal-weight superposition  $(\alpha = \pi /4)$ , analyzing only the photon data itself as a function of  $\varphi$  leads to an interference pattern with a reduced visibility of  $V = 1 / 2$ . Changing  $\alpha$  from 0 (photon in state  $|\mathrm{particle}\rangle$ ) to  $\pi /2(|\mathrm{wave}\rangle)$  allows one to continuously morph into particle and wave properties. Ignoring the ancilla outcome, the detector for the photon state 0 fires with probability  $I_{p}(\varphi)\cos^{2}\alpha + I_{w}(\varphi)\sin^{2}\alpha$ , i.e.,

$$
\frac {1}{2} \cos^ {2} \alpha + \cos^ {2} \frac {\varphi}{2} \sin^ {2} \alpha , \tag {13}
$$

corresponding to a visibility  $V = \sin^2\alpha$

A hidden-variable based analysis of quantum delayed-choice experiments needs to describe the entire (entangled)

system of photon and ancilla. It was argued that quantum delayed-choice experiments without spacelike separation between system photon and ancilla are equivalent to classical delayed-choice experiments with spacelike separation (Céleri et al., 2014). The continuous morphing behavior predicted by quantum mechanics in quantum delayed-choice experiments cannot be described by hidden-variable theories for the system photon and the ancilla, which obey objectivity (particle and wave are intrinsic attributes of the system photon during its lifetime), determinism (the hidden variables determine the individual outcomes), and independence (the hidden variables do not depend on the experimental setting, i.e., the choice of  $\alpha$ ) (Ioniciou et al., 2014). Moreover, these three assumptions are indeed incompatible with any theory, not only quantum mechanics (Ioniciou, Mann, and Terno, 2015).

# III. REALIZATIONS OF DELAYED-CHOICE WAVE-PARTICLE DUALITY EXPERIMENTS

# A. First realizations of Wheeler's delayed-choice experiment

Inspired by Wheeler's gedanken experiment, there have been several concrete experimental proposals and analyses for different physical systems, including neutron interferometers (Greenberger et al., 1983; Miller, 1983; Miller and Wheeler, 1983) and photon interferometers (Alley et al., 1983; Mittelstaedt, 1986). Pioneering endeavors in realizing these experiments have been reported by Alley, Jakubowicz, and Wickes (1986), Schleich and Walther (1986), and Hellmuth et al. (1987).

Hellmuth and collaborators performed delayed-choice experiments with a low-intensity MZI in the spatial domain as well as time-resolved atomic fluorescence in the time domain (Hellmuth et al., 1987). The layout of the delayed-choice experiment in the spatial domain is shown in Fig. 11. An attenuated picosecond laser (on average less than 0.2 photon per pulse) was used as the light source for the MZI. Two  $5\mathrm{m}$  (20 ns) glass fibers were used to delay the input photon. The transit time of the photon through the whole interferometer was about 24 ns. The combination of a Pockels cell (PC) and a polarizer (POL) was placed in the upper arm of the MZI as a shutter.

![](images/0a3751989d8323c8532060fd3b8be3970120d801932648c6ad6ccbb60ab785ab.jpg)  
FIG. 11. Setup of the delayed-choice experiment. The combination of a Pockels cell (PC) and a polarizer (POL) in the upper arm of the interferometer was used as a shutter. From Hellmuth et al., 1987.

When a half-wave voltage was applied on the Pockels cell, it rotated the polarization of the photons propagating through it, such that they were reflected out of the interferometer. In this case the shutter was closed and interference vanished as the upper path of the interferometer was interrupted and only photons from the lower arm could reach the photomultipliers (PM 1 and PM 2). This provided which-path information, as the photon arrived at beam splitter 2 because it could only have come via the other open path. On the other hand, if the shutter was open upon the photon's arrival, one could observe the interference pattern, because then no information was present about the path the photon took.

The temporal structure in the "delayed-choice mode" of this experiment was as follows. The input photon met beam splitter 1 first, where its amplitude was split between two paths through the interferometer. It then was kept in a fiber, one in each path, for  $20~\mathrm{ns}$ . During the photon propagation in the fiber, the shutter opened after  $4\mathrm{ns}$  PC rise time. Then the photon exited from the fibers and met the opened shutter and beam splitter 2 sequentially. Therefore, in this case, opening of the shutter was delayed until after the input photon met beam splitter 1 and was well inside of the interferometer. With this experimental arrangement, the photon's entry into the MZI was clearly located in the past light cone of opening the shutter.

In the "normal mode," opening the shutter was prior to the input photon meeting beam splitter 1. The authors alternated the experimental arrangement from the normal mode (opening the shutter before the photon reaches beam splitter 1) to the delayed-choice mode (opening the shutter after the photon reaches beam splitter 1) for each successive light pulse, while they kept all the other experimental configurations the same, in particular, the phase of the MZI. The photon counts detected by PM 1 as a function of the phase variation are presented in Fig. 12. The results measured by PM 2 showed complementary behavior, i.e., the pattern was shifted by a phase  $\pi$  with respect to the one recorded by PM 1.

This experiment was one of the pioneering realizations of Wheeler's gedanken experiment, although no true single photons were used and no real active choices were implemented. The switch-on time of the Pockels cell was delayed, but eventually it was turned on such that always the light's wave character was tested.

Alley and co-workers put forward a concrete scheme for realizing Wheeler's gedanken experiment with a delayed and

![](images/2e2eac79046eaa0056bbb1a6a3c7cd204423e8331a2ec3d31140377e9751c092.jpg)  
FIG. 12. Experimental results of the delayed-choice experiment. Interference patterns for normal mode (dots) and delayed-choice mode (crosses) measured by PM 1 are similar and consistent with quantum-mechanical predictions. From Hellmuth et al., 1987.

random choice for the configuration (open or closed) of a MZI (Alley et al., 1983). Three years later, they reported a successful experimental demonstration (Alley, Jakubowicz, and Wickes, 1986). The full details of this work are described by Jakubowicz (1984). The experiment was conceptually similar to that by Hellmuth et al. (1987) with some important differences. It was realized with a  $4 \times 0.3 \mathrm{~m}^2$  free-space interferometer, where delayed random choices were implemented. An additional photomultiplier was used to detect the photons which were reflected out of the interferometer by the combination of the Pockels cell and the polarizer. The random choice was made at a photocathode which had a  $50\%$  probability of producing a photoelectron upon the strike of a laser pulse. This photoelectron was then amplified and used to switch the electro-optical modulator (EOMs) in the MZI. Detailed information of the random-choice generation is shown in Fig. 13.

Five experimental runs with different space-time configurations were implemented. The equivalent one-space-dimensional space-time diagram is shown in Fig. 14. In runs  $R$ ,  $T$ , and  $U$  the choice events were not only 3.5 ns delayed with respect to the entry of the photons into the MZI in the laboratory reference frame (event  $E$ , the origin point in Fig. 13) but also spacelike separated from  $E$ . In run  $Y$ , the choices were also spacelike separated from  $E$  but took place 5 ns earlier. In run  $W$ , the choices were in the timelike past of  $E$ . About 90% interference visibility was obtained when the wave property of the input photons was measured, and no observable interference was obtained when the particle property was measured. The authors concluded the following: "The predictions of quantum mechanics are confirmed even with the choice of the final configuration being made randomly during the course of the 'elementary quantum phenomenon'" (Alley, Jakubowicz, and Wickes, 1986).

![](images/42489b29f3c4e75bbe1b481bc72762b6451c01e23e91b5895a6c846dd28a781a.jpg)  
FIG. 13. Schematic diagram of the device generating the random choices proposed by Alley et al. (1983) and used by Alley, Jakubowicz, and Wickes (1986). A weak light pulse emitted from a light emitting diode has a pulse duration of 0.67 ns. The detection event of this light pulse makes the random choice which determines the setting of the Pockels cell. To realize that, a photocathode with  $50\%$  probability of producing a photoelectron within 1 ns is amplified by a fast amplifier within 2 ns. This electric pulse then triggers the avalanche transistor chain switch and hence the Pockels cell. The time of the choice can be tuned with respect to the photon's entry into the MZI. From Alley et al., 1983, and Alley, Jakubowicz, and Wickes, 1986.

![](images/c20e46aba85489f8ed6bc53ccdd400fe76c4f3e193c0474ba0a774f22cb46c00.jpg)  
FIG. 14. Space-time diagram. It shows the locations of the random-choice events for different runs with respect to the photons meeting the beam splitter and hence entering into the MZI in the laboratory reference frame. In runs  $R, T, U$ , and  $Y$ , the choice events were spacelike separated from the photon's entry into the interferometer (origin of the diagram). From Alley, Jakubowicz, and Wickes, 1986.

# B. Wheeler's delayed-choice experiment with single particles: Photons and atoms

To meet the requirement of using a single-particle quantum state, Baldzuhn, Mohler, and Martienssen (1989) used heralded single photons generated from spontaneous parametric downconversion (SPDC) (Friberg, Hong, and Mandel, 1985) to perform a delayed-choice wave-particle experiment. The layout of the setup is shown in Fig. 15. The detection of one (trigger) photon was used to trigger a Pockels cell  $(P)$  in a Sagnac interferometer (Sagnac, 1913) through which the other (signal) photon propagated.

In the clockwise path, the signal photon first passed the Pockels cell  $P$  and then the reference point  $I$ . In the anticlockwise path, however, the situation is reverse. (a) If the Pockels cell was off during the photon's propagation through the whole interferometer, the polarization of the signal photon was not rotated and remained the same for both the clockwise and the anticlockwise path. (b) Similarly, if the Pockels cell was continuously on, the polarization was rotated in both paths. In both cases (a) and (b) the final polarization state was the same for both paths, leading to interference. If, however, the Pockels cell was switched on at the time when the signal photon arrives at the reference point  $I$  and was kept on until after the photon met the beam splitter again, no interference was observed. This is because the polarization of the clockwise path remained unchanged, while

![](images/88f111f519889f40bd87741c7be8ab96cb2398dec44ed827c30df7dc4775ca26.jpg)  
FIG. 15. Setup of the delayed-choice experiment reported by Baldzuhn, Mohler, and Martienssen (1989). Photon pairs were produced by parametric downconversion in the  $\mathrm{LiIO}_3$  crystal. Detection of the (trigger) photon 1 in  $D1$  heralded (signal) photon 2 propagating through fiber  $F$  to a Sagnac interferometer. The detection at  $D1$  triggered a Pockels cell  $P$  in the interferometer through which the signal photons propagated in a clockwise or anticlockwise path before reaching detector  $D2$ . The signal photons showed wave behavior, if the Pockels cell was continuously left on or off. Particle behavior was revealed if the Pockels cell was switched on at the moment when the signal photons reached the reference point  $I$  in the interferometer. From Baldzuhn, Mohler, and Martienssen, 1989.

the polarization of the counterclockwise path was rotated. The polarization degree of freedom introduced a distinguishability between the two paths and hence destroyed the possibility of interference.

The experimental results are presented in Fig. 16. If the Pockels cell was continuously on or off, one observed an interference pattern [Fig. 16(a)]. This corresponds to the photon's wavelike behavior. On the other hand, if the Pockels cell was switched on at the time when the photon passed the reference point  $I$ , no interference pattern was observed [Fig. 16(b)]. This corresponds to the particlelike behavior of the photon.

The delayed-choice aspect of this experiment was realized by delaying the signal photon by an optical fiber [labeled  $F$  in Fig. 15] and varying the time of the application of the voltage on the Pockels cell via electronic delays. This allowed one to switch the Pockels cell at the time when the photon was

![](images/c8118ebab2676c165663367bccf965dc646f17bb6e70c25617849079e65a14f9.jpg)  
FIG. 16. Experimental results of the delayed-choice experiment by Baldzuhn, Mohler, and Martienssen (1989). (a) If the Pockels cell was continuously on or off, an interference pattern was observed. (b) If the Pockels cell was switched on when the signal photon reached the reference point  $I$ , indicated in Fig. 15, no interference showed up. From Baldzuhn, Mohler, and Martienssen, 1989.

![](images/d1b00cf625dabbc1ca84450847b7cdc314fccb92d0ce9726f2d2815d9dde9f32.jpg)

at the reference point, i.e., already within the interferometer. Spacelike separation between the choice of the performed measurement and the entering of the photon into the interferometer was not implemented in this experiment.

Recently a realization of Wheelers delayed-choice gedanken experiment with single atoms was reported (Manning et al., 2015). The physical beam splitters and mirrors were replaced with optical Bragg pulses. The choice of either applying the last beam splitting pulse or not was controlled by an external quantum random number generator. This choice event occurred after the entry of the atoms into the interferometer.

# C. Wheeler's delayed-choice experiment with single photons and spacelike separation

Two important requirements of an ideal realization of delayed-choice wave-particle duality gedanken experiment—namely, use of single-particle quantum states as well as spacelike separation between the choice of the measurement and the entry of the particle into the interferometer—have been fulfilled simultaneously by Jacques et al. (2007, 2008). Nitrogen-vacancy (NV) color centers in diamonds were employed as single-photon sources (Kurtsiefer et al., 2000). As shown in Fig. 17(a), a 48-m-long polarization interferometer and a fast EOM controlled by a QRNG were used to fulfill relativistic spacelike separation. The random numbers were generated from the amplified shot noise of a white light beam.

The space-time diagram of this experiment is illustrated in Fig. 17(b). The sequence for the measurement applied to the nth photon constituted three steps. First, the choice was made by the QRNG, creating a binary random number, which determined the interferometer configuration. This choice happened simultaneously with the trigger pulse of the nth photon's emission. Second, the random number [bit values 1, 0, and 1 for photons  $n - 1$ ,  $n$ , and  $n + 1$  in Fig. 17(b)] drove the EOM voltage to  $V = 0$  (bit value 0) or  $V = V_{\pi}$  (bit value 1) within rise time 40 ns, which determined the state of the second beam splitter  $(\mathrm{BS}_{\mathrm{output}})$ . Finally, the photon was recorded by detectors  $D1$  or  $D2$ , after its time of flight  $\tau_{\mathrm{interf}}$  in the interferometer. The shaded center zone in Fig. 17(b) represents the future light cone of the choice. The event "entry of photon into the interferometer" was spacelike separated from the respective choice. If the EOM was on with voltage  $V = V_{\pi}$ , one erased the polarization distinguishability of the two paths and thus observed an interference pattern when tuning the phase of the interferometer by tilting  $\mathrm{BS}_{\mathrm{input}}$  [Fig. 17(c)]. If, however, the EOM was switched off, due to the polarization distinguishability of the two paths, no interference showed up [Fig. 17(d)].

Furthermore, Jacques and co-workers varied the driving voltages applied to the EOM and thus realized a fast switchable beam splitter with an adjustable reflection coefficient  $R$  (Jacques et al., 2008). The QRNG switched this beam splitter on and off randomly. Each randomly set value of  $R$  allowed them to obtain partial interference with visibility  $V$  and partial which-path information. The which-path information was parametrized by the distinguishability  $D$ . They confirmed

![](images/129fd76d55ecf5b387ba56f60d2699a3574bec1a6526f70c91edf87803743bf1.jpg)

![](images/89283a0c4b8b0e1f118277500f284e6327b83a0b4d0118b36f9ea22f5ca54073.jpg)

![](images/91f00981b5f58e40ac9e52b17b82125d9f70d677d556ebbd34b19587522f1b17.jpg)  
FIG. 17. The delayed-choice experiment realized by Jacques et al. (2007). (a) Layout of the setup. Single photons were generated by NV color centers in diamond. A 48-m-long polarization interferometer and a fast EOM, controlled by a QRNG, were used to fulfill the relativistic spacelike separation condition. (b) The space-time diagram. The choice whether to open or close the interferometer was spacelike separated from the entry of the photon into the interferometer. (c) If the EOM was on, the polarization distinguishability of the two paths was erased and thus an interference pattern emerged. (d) If, however, the EOM was switched off, no interference showed up due to the polarization distinguishability of the two paths. From Jacques et al., 2007.

![](images/8ae240bacdfe5031fff4974c47133ec6ba4935ad43127628d131044810e9c45a.jpg)

that  $V$  and  $D$  fulfilled the complementary relation (Wootters and Zurek, 1979; Greenberger and Yasin, 1988; Jaeger, Shimony, and Vaidman, 1995; Englert, 1996)

$$
V ^ {2} + D ^ {2} \leq 1, \tag {14}
$$

where equality holds for pure states (see Fig. 18). The visibility is defined as  $V = (p_{\mathrm{max}} - p_{\mathrm{min}}) / (p_{\mathrm{max}} + p_{\mathrm{min}})$ , with  $p_{\mathrm{max}}$  and  $p_{\mathrm{min}}$  the maximal and minimal probabilities for recording a photon in a chosen detector when scanning through the phase of the interferometer. The distinguishability (or which-path information) is defined as  $D = D_1 + D_2$  with  $D_i = |p(i,1) - p(i,2)|$  and  $p(i,j)$  the probability that the photon traveled path  $i = 1, 2$  and is recorded by detector  $j = 1, 2$ . The quantity  $D_1$  is measured by blocking path 2, and vice versa.

![](images/3b888188a371df247588a0d7a84e108a88551158b55806027cd3edd9be172189.jpg)

![](images/86fe686f6c33546314afade610293bd629fb2488f2c0b98147a3151d6eb502a3.jpg)  
FIG. 18. Experimental visibility ( $V^2$ , starting at 0) and distinguishability ( $D^2$ , starting at 1) results from Jacques et al. (2008). (a)  $V^2$  and  $D^2$  as functions of the EOM voltage (corresponding to the reflectivity of the second beam splitter). Solid lines are the theoretical expectations. (b)  $V^2 + D^2$  as a function of the EOM voltage, in agreement with Eq. (14). From Jacques et al., 2008.

# IV. REALIZATIONS OF DELAYED-CHOICE QUANTUM-ERASER EXPERIMENTS

Delayed-choice experiments with two particles offer more possibilities than those with single particles. Especially in the experiments performed with entangled particles in the context of quantum erasure, the choice of measurement setting for one particle can be made even after the other particle has been registered. This has been shown in delayed-choice quantum eraser experiments, where the which-path information of one particle was erased by a later suitable measurement on the other particle. This allowed to a posteriori decide a single-particle characteristic, namely, whether the already measured photon behaved as a wave or as a particle. We will discuss the experimental realizations along this line in the following sections.

# A. Photonic quantum erasure

Energy-time (Friberg, Hong, and Mandel, 1985; Joobeur, Saleh, and Teich, 1994), momentum (Rarity and Tapster, 1990), and polarization (Shih and Alley, 1988; Kwait et al., 1995) entanglement of photon pairs generated from SPDC have been widely used in experiments realizing photonic quantum erasure. Herzog et al. (1995) used photon pairs generated from type-I SPDC and demonstrated the quantum eraser concept via various experiments. Polarization as well as time delay was used as quantum markers, and wave plates as well as narrow-bandwidth interference filters were used as quantum erasers. They harnessed the momentum entanglement and polarization correlation between photon pairs and performed remote measurements on one photon either revealing or erasing which-path information of the other one.

An arrangement consisting of a double slit and two entangled particles allows a combination of the gedanken experiments of Heisenberg's microscope and the quantum eraser. Dopfer and collaborators employed photon pairs generated from type-I SPDC (Dopfer, 1998; Zeilinger, 1999; Zeilinger et al., 2005). Because of the phase matching condition, photons 1 and 2 were entangled in their linear momentum states. Figure 19(a) shows one of their experimental configurations. Photon 2 passed a double slit and a lens and was measured by a static detector  $D2$  in the focal plane. Photon 1 was sent through another lens with focal length  $f$  and was measured by detector  $D1$ , which was mounted on translation stages capable of moving along both axes  $x$  and  $z$ . This allowed an implementation of the idea of von Weizsacker switching from the focal plane to the image plane.

![](images/c55f9c92998d2adbbce752592c573131a465d3c9c03707af79243b6f321606e2.jpg)

![](images/4e6fc7a7f26ca2cd127872b8bfa5bbf8ba008ee0f48ded41cc5e276098ff9ca0.jpg)

![](images/ae3c26cfd4680f9381276d3293603fe68822c43c471a8df890f0d7ebfa9e9a7d.jpg)  
FIG. 19. (a) Experimental scheme of the experiment, using a momentum entangled state of two photons. See text for details. (b) A high-visibility interference pattern in the conditional photon counts was obtained when  $D1$  was positioned in the focal plane of the lens, thus erasing all path information. (c) The profile of the double slit was resolved when  $D1$  was positioned in the image plane of the lens, revealing path information and therefore no interference pattern arose. From Dopfer, 1998.

If  $D1$  was placed in the focal plane of the lens (i.e., at distance  $f$  from the lens), one measured photon 1's momentum state and hence lost the information about its position. Because of the momentum entanglement, the measurement of photon 1's momentum state projected the state of photon 2 into a momentum eigenstate which could not reveal any position information. One therefore had no information whatsoever about which slit photon 2 went through. When both photons were detected, neither photon 1 nor photon 2 revealed any path information. Therefore, when coincidence counts between  $D1$  and  $D2$  were measured as a function of  $D1$ 's position along the  $x$  axis, an interference pattern showed up with a visibility as high as  $97.22\%$  [Fig. 19(b)].

On the other hand, when  $D1$  was placed in the image plane (i.e., distance  $2f$  from the lens), the detection events of photon 1 revealed the path photon 2 took through the double slit. In Fig. 19(c), two prominent peaks indicate the profile of the double-slit assembly with no interference pattern.

In the experiment of Walborn et al. (2002), one photon of a polarization-entangled pair impinged on a special double-slit device, where two quarter-wave plates, oriented such that their fast axes are orthogonal, were placed in front of each slit to serve as which-path markers. The quarter-wave plates rotated the polarization states of the photons passing through them and hence the subsequent slits. This rotation introduced a distinguishability of the two possible paths and thus destroyed the interference pattern. To recover interference, polarization entanglement was used and the polarization of the other entangled photon was measured in a proper basis. This experiment was also performed under delayed erasure conditions, in which the interfering photon is detected before its entangled twin. The experimental data were in agreement with the predictions of quantum mechanics.

# B. Matter-wave quantum erasure

Light scattered from laser-cooled atoms provides information on the localization of atoms and can be used to realize quantum-eraser experiments, if the atomic separation is large enough and the wavelength of the scattered light short enough to allow in principle identification of the atom's position by imaging conditions. Eichmann et al. (1993) performed an experiment with light scattered from two ions. By employing the polarization of the scattered light, they realized the previously mentioned cases (A) and (B) in Sec. II.E and observed polarization-detection dependent interference patterns.

Durr, Nonn, and Rempe (1998) carried out an atomic interferometric experiment showing that the disturbance of path detection on an atom's momentum is too small to destroy the interference pattern. The principle of this experiment is shown in Fig. 20(a). By using a standing-wave grating formed by off-resonant laser light, the collimated atomic beam  $A$  was split into two beams: beam  $B$  was reflected and beam  $C$  was transmitted. After free propagation for a time duration of  $t_{\mathrm{sep}}$ , they were separated by a lateral distance  $d$ . The beams  $B$  and  $C$  were then split again by a second standing light wave grating. In the far field, complementary spatial interference patterns were observed in two regions. Experimentally, the phase of the atomic interferometer was varied by setting

![](images/6ad07257e3428f2aa6d0eec27eefcc23b688014327cb54ef3b421ee564999fa2.jpg)

![](images/88fa04cc730a31a5cc49ab0afd86b402eef8e40eebcfab9652dad333d46a4a76.jpg)  
FIG. 20. Quantum-eraser experiment from Durr, Nonn, and Rempe (1998)) based on an atomic interferometer. (a) The atomic beam  $A$  was split into two beams: beam  $B$  was reflected by the first Bragg grating formed by a standing wave, and beam  $C$  was transmitted. The atomic beams freely propagated for a time duration of  $t_{\mathrm{sep}}$  and acquired a lateral separation  $d$ . The beams  $B$  and  $C$  were then split again by a second standing light wave grating. In the far field, complementary spatial interference patterns were observed in two regions. These interference patterns were due to superpositions of beams  $D$  and  $E$  ( $F$  and  $G$ ). (b), (c) The spatial fringe patterns in the far field of the interferometer for  $t_{\mathrm{sep}} = 105 \mu \mathrm{s}$  with  $d = 1.3 \mu \mathrm{m}$  and  $t_{\mathrm{sep}} = 255 \mu \mathrm{s}$  with  $d = 3.1 \mu \mathrm{m}$ , respectively. The left and right complementary interference patterns were, respectively, generated by the atomic beams  $D$  and  $E$ , and  $F$  and  $G$  [shown in (a)]. The dashed lines indicate the sum of the intensities of two interference patterns obtained with a relative phase shift of  $\pi$ . (d) The simplified scheme of the internal atomic states, which were addressed using microwave (mw) radiation and light. (e) The principle of correlating the path the atoms took with their internal electronic states. The standing-wave grating produced a relative  $\pi$  phase shift of state  $|2\rangle$  relative to  $|3\rangle$  conditional on its path. A Ramsey interferometer employed two microwave  $\pi / 2$  pulses and converted different relative phases into different final internal states  $|2\rangle$  and  $|3\rangle$ , respectively. (f) When the which-path information was stored in the internal atomic state, the interference patterns vanished. From Durr, Nonn, and Rempe, 1998.

![](images/482bc790f8f41162239ce06359fb6ef906e81c90e4ba5d96e63e76ac1427ed96.jpg)

![](images/3b697c0710f0fa31f683731fe9c374c42352c889ae88c7211b55c1aad7860f6e.jpg)

![](images/23a4c6ef42df0ce56f7f78d0a061f8cacfe7d3870cf59c8ef248c01c3419c60f.jpg)

![](images/62d32d406a984927d30e68f7b0712eda3e6bb541f7b11e4e3604a8972c8e5b69.jpg)

different separation durations  $t_{\mathrm{sep}}$  between the first and the second standing-wave gratings. Interference patterns with visibilities of  $(75 \pm 1)\%$  and  $(44 \pm 1)\%$  for  $t_{\mathrm{sep}} = 105$  and  $255~\mu \mathrm{s}$ , shown in Figs. 20(b) and 20(c), have been observed which were in good agreement with the theoretical expectations.

The internal electronic states  $|2\rangle$  and  $|3\rangle$  were used as a which-path detector for the paths  $B$  and  $C$  [Fig. 20(d)]. These two states were addressed and manipulated with microwave pulses. Figure 20(e) shows how the atomic internal electronic

states were employed in controlling the paths the atoms took. They converted the input state  $|2\rangle$  to a superposition state  $|2\rangle + |3\rangle$  by a  $\pi/2$  microwave pulse with frequency  $\omega_{\mathrm{mw}} = \omega_3 - \omega_2$ , where  $\omega_2$  and  $\omega_3$  are the frequencies of states  $|2\rangle$  and  $|3\rangle$ . (We omit the normalization to be consistent with the original notation.) Then a standing-wave grating was formed by a laser with frequency  $\omega_{\mathrm{light}}$ , which was tuned to be halfway between the  $|2\rangle \rightarrow |e\rangle$  and  $|3\rangle \rightarrow |e\rangle$  transitions to the excited state  $|e\rangle$ , i.e.,  $\omega_{\mathrm{light}} = \omega_e - (\omega_3 - \omega_2) / 2$ . Because of these detunings an internal-state dependent phase shift was implemented. In the reflected arm  $(B)$ , the light grating induced a  $\pi$  phase shift on state  $|2\rangle$  with respect to  $|3\rangle$  resulting in state  $|3\rangle - |2\rangle$ . In the transmitted arm  $(C)$ , no phase shift was induced and hence the state remained  $|3\rangle + |2\rangle$ . A subsequent  $\pi/2$  microwave pulse converted the superposition states in the reflected and transmitted arm to  $|2\rangle$  and  $|3\rangle$ , respectively. Therefore, the atom path in the interferometer was correlated with its internal electronic states. Consequently, no interference patterns did arise, as shown in Fig. 20(f).

In this experiment, the disturbance of the path, which was induced by using microwave pulses, was 4 orders of magnitude smaller than the fringe period and hence was not able to explain the disappearance of the interference patterns. Instead, "the mere fact that which-path information is stored in the detector and could be read out already destroys the interference pattern" (Durr, Nonn, and Rempe, 1998).

Recently, an experimental realization of quantum erasure in a mesoscopic electronic device was reported by Weisz et al. (2014). Interacting electrons have been used to extract which-path information and a smooth variation of the degree of quantum erasure was demonstrated.

We also remark here that neutral kaon systems have been theoretically suggested to be suitable for a demonstration of quantum erasure as shown in Bramon, Garbarino, and Hiesmayr (2004). There, strangeness oscillations would represent the interference pattern linked to wavelike behavior.

# C. Quantum erasure with delayed choice

Kim et al. (2000) used pairs of entangled photons to mimic the entangled atom-photon system proposed by Scully, Englert, and Walther (1991). The layout of the experimental setup is shown in Fig. 21(a). Photon pairs were generated noncollinearly from either region  $A$  or region  $B$  of a  $\beta$ -barium borate (BBO) crystal via type-I SPDC. From each pair, photon 1, simulating the atom, propagated to the right and was focused by a lens. It was then detected by  $D_0$ , which was mounted on a step motor capable of changing the lateral position  $x_0$ .

Photon 2, propagating to the left, passed through one or two of the three beam splitters. If the pair was generated in region  $A$ , photon 2 would follow path  $a$  and meet beam splitter BSA, where it had a  $50\%$  chance of being reflected or transmitted. If the pair was generated in region  $B$ , photon 2 would propagate path  $b$  and meet beam splitter BSB, again with a  $50\%$  chance of being reflected or transmitted.

In the case that photon 2 was transmitted at BSA or BSB, it would be detected by detector  $D_{3}$  or  $D_{4}$ , respectively. The detection of  $D_{3}$  or  $D_{4}$  provided which-path information (path  $a$  or path  $b$ ) for photon 2, thus also providing the which-path information for photon 1 due to the linear momentum

![](images/c7a6a4869d91db5265578adbfb08466b8767591c16f9146378ac940e3106b7e2.jpg)  
(a)  
(c)

![](images/7803961ef37a8be88549502f7bc42fd9aa6b52289454da5a72716a63e23cd2a3.jpg)  
(b)

![](images/45b77c18b5fc6a75fb1d9b191f48e643e8ec291e373c11d0547101bf728aaf7e.jpg)  
FIG. 21. Delayed-choice quantum-eraser experiment realized by Kim et al. (2000). (a) Experimental scheme. Pairs of entangled photons were emitted from either region  $A$  or region  $B$  of a BBO crystal via spontaneous parametric downconversion. These two emission processes were coherent. Detections at  $D_{3}$  or  $D_{4}$  provided which-path information and detections at  $D_{1}$  or  $D_{2}$  erased it. (b) Coincidence counts between  $D_{0}$  and  $D_{3}$  as a function of the lateral position  $x_{0}$  of  $D_{0}$ . Absence of interference was demonstrated. (c) Coincidence counts between  $D_{0}$  and  $D_{1}$  as well as between  $D_{0}$  and  $D_{2}$  are plotted as a function of  $x_{0}$ . Interference fringes were obtained. See text for details. From Kim et al., 2000.

entanglement of the photon pair. Therefore, there was no interference, as verified by the results shown in Fig. 21(b).

On the other hand, given a reflection at BSA or BSB, photon 2 continued its path to meet another 50:50 beam splitter BS and was then detected by either  $D_{1}$  or  $D_{2}$ . The detection by  $D_{1}$  or  $D_{2}$  erased the which-path information carried by photon 2 and therefore an interference pattern showed up for photon 1 [Fig. 21(c)]. This confirmed the theoretical prediction.

The "choice" of observing interference or not was made randomly by photon 2 by being either reflected or transmitted at BSA or BSB. In the actual experiment, the photons traveled almost collinearly, but the distance from the BBO to BSA and BSB was about  $2.3\mathrm{m}$  (7.7 ns) longer than the distance from the BBO to  $D_0$ . Thus, after  $D_0$  was triggered by photon 1, photon 2 was still on its way to BSA or BSB, i.e., the which-path or the both-path choice was "delayed" compared to the detection of photon 1.

As an extension, a delayed-choice quantum-eraser experiment based on a two-photon imaging scheme using entangled photon pairs (signal and idler photons) was reported by Scarcelli, Zhou, and Shih (2007). The complete which-path information of the signal photon was transferred to the distant idler photon through a "ghost" image. By setting different sizes of the apertures, they could either obtain or erase which-path information. In the case of which-path information erasure, interference with a visibility of about  $95\%$  was obtained. When not erasing which-path information, no interference was observed.

# D. Quantum erasure with active and causally disconnected choice

Quantum erasure with an active and causally disconnected choice was experimentally demonstrated by Ma et al. (2013). To this end, the erasure event of which-path information had to be spacelike separated from the passage of the interfering system through the interferometer as well as its detection event. Based on the special theory of relativity, the event of quantum erasure was therefore causally disconnected from all relevant interference events.

The concept of the experiment is illustrated in Fig. 22(a). Hybrid entangled photon pairs (Ma et al., 2009) were produced, with entanglement between path  $a$  or  $b$  of one

![](images/1f3204629551ef2ae552fe9e494376941ccf1c180aa584f0e9eb7e7335c30434.jpg)  
(a)

![](images/0deadfd0c4c3f491e51e8d8afe1f0c534d7eb554b756f6bc67f9bd1b932e79ff.jpg)  
(b)

![](images/b34a0dfc6fd097013be1990c6012951ff9ac85eb9cfadbb4c7a12ca7fc41bca6.jpg)  
(c)  
FIG. 22. Quantum erasure with causally disconnected choice. (a) Principle: The source  $S$  emitted path-polarization-entangled photon pairs. The system photons propagated through an interferometer (right side), and the environment photons were subject to polarization measurements (left). (b) Scheme of the Vienna experiment: In Lab 1, the polarization-entangled state generated via type-II spontaneous parametric downconversion was converted into a hybrid entangled state with a polarizing beam splitter (PBS1) and two fiber polarization controllers (FPC). In Lab 2, the polarization projection setup of the environment photon consisted of an electro-optical modulator (EOM) and another polarizing beam splitter (PBS2). In Lab 3, the choice was made with a quantum random number generator (QRNG) (Jennewein et al., 2000). (c) Space-time diagram. The choice-related events  $\mathbf{C}_e$  and the polarization projection of the environment photon  $\mathbf{P}_e$  were spacelike separated from all events of the interferometric measurement of the system photon  $\mathbf{I}_s$ . Additionally, the events  $\mathbf{C}_e$  were also spacelike separated from the emission of the entangled photon pair from the source  $\mathbf{E}_{se}$ . The shaded areas are the past and the future light cones of events  $\mathbf{I}_s$ . This ensured that Einstein locality was fulfilled. From Ma et al., 2013.

photon (the system photon  $s$ ) in an interferometer, and the polarization  $H$  or  $V$  of the other photon (the environment photon  $e$ ):

$$
\left| \Psi \right\rangle_ {s e} = \frac {1}{\sqrt {2}} \left(\left| a \right\rangle_ {s} \left| H \right\rangle_ {e} + \left| b \right\rangle_ {s} \left| V \right\rangle_ {e}\right). \tag {15}
$$

Analogous to the original proposal of the quantum eraser, the environment photon's polarization carried which-path information of the system photon due to the entanglement between the two photons. Depending on which polarization basis the environment photon was measured in, one was able to either acquire which-path information of the system photon and observe no interference or erase which-path information and observe interference. In the latter case, it depended on the specific outcome of the environment photon which one out of two different interference patterns the system photon was showing.

The quantum-eraser concept under Einstein locality was tested on two different length scales. In the first experiment performed in Vienna in 2007, the environment photon was sent away from the system photon via a 55-m-long optical fiber [Figs. 22(b) and 22(c)]. In the second experiment performed on the Canary Islands in 2008, the photons were separated by  $144\mathrm{km}$  via a free-space link. See the caption of Fig. 22 for details on the first experiment and its space-time diagram.

In order to quantitatively demonstrate quantum erasure under Einstein locality, they employed a bipartite complementarity inequality of Eq. (14) (Wootters and Zurek, 1979; Greenberger and Yasin, 1988; Jaeger, Shimony, and Vaidman, 1995; Englert, 1996), in which  $D$  and  $V$  stand for conditional which-path information (distinguishability) and interference visibilities, respectively. It is an extension of the single-particle complementarity inequality [experimentally verified by Jacques et al. (2008) and discussed in Sec. III.C]. Under Einstein locality,  $D$  and  $V$  were measured in sequential experimental runs as a function of the applied voltage of the EOM, which changed the polarization projection basis of the environment photon. Hence, a continuous transition between measurements of particle nature and wave nature was acquired. The results are shown in Fig. 23.

Note that similar setups were proposed by Grangier (1986), Ballentine (1998), and Kwiat and Englert (2004). Another successful experiment along this line was reported by Kaiser et al. (2012). Kaiser and collaborators used polarization-entangled photon pairs at the telecom wavelength. Every "test" photon was sent into an interferometer (with phase  $\theta \equiv \varphi$ ), while the corresponding "corroborative" photon was subject to a polarization measurement. While no active random choices were implemented in their experiment, the detection events of the corroborative and test photon were spacelike separated (Fig. 24).

The interferometer employed a polarization-dependent beam splitter (PDBS) with bulk optics which was able to reflect horizontally polarized test photons with close to  $100\%$  probability and reflect or transmit vertically polarized photons with  $50\%$  or  $50\%$  probability. Then polarizing beam splitters oriented at  $45^{\circ}$  to the  $H / V$  basis erased all polarization information that potentially existed at the PDBS output.

![](images/cda76c3f363701cc35a940d18f8138970488a4d380521dc05f3727cc59039514.jpg)  
FIG. 23. Experimental test of the complementarity inequality under Einstein locality, manifested by a trade-off of the which-path information parameter  $D$  and the interference visibility  $V$ . The dotted line is the ideal curve from the saturation of the complementary inequality. The solid line  $V = 0.95[1 - (D / 0.97)^{2}]^{1/2}$  is the estimation from experimental imperfections. From Ma et al., 2013.

The corroborative photon passed an EOM which rotated its polarization state by an angle  $\alpha$  before it was measured. The total quantum state of the test  $(t)$  and corroborative photon  $(c)$  was

$$
\begin{array}{l} | \Psi \rangle_ {t c} = \frac {1}{\sqrt {2}} \left[ (\cos \alpha | \text {p a r t i c l e} \rangle_ {t} - \sin \alpha | \text {w a v e} \rangle_ {t}) | H \rangle_ {c} \right. \\ + \left(\cos \alpha | \text {w a v e} \rangle_ {t} + \sin \alpha | \text {p a r t i c l e} \rangle_ {t}\right) | V \rangle_ {c} ]. \tag {16} \\ \end{array}
$$

Here  $|\mathrm{particle}\rangle$  and  $|\mathrm{wave}\rangle$  are defined similar to Eqs. (11) and (12). This allowed for a continuous transition between wave and particle properties, verifying the predicted intensity

![](images/0f3ad922da4bc09f7df5d4407b4953e342ad9224357a93c43dd3f8a38c947db6.jpg)  
FIG. 24. Space-time diagram of the experiment reported by Kaiser et al. (2012). The detections of the corroborative photon and the test photon were spacelike separated. From Kaiser et al., 2012.

![](images/c5ed972f4982b0bd2e6a379958bbb559985eabdf8bdf3f66d6ccee4e47dec09b.jpg)  
FIG. 25. Experimental results reported by Kaiser et al. (2012). When the corroborative photon was found to be horizontally polarized, the test photons produced an intensity pattern following Eq. (13), with  $\theta \equiv \varphi$ . The same pattern emerged when the corroborative photon was measured in the  $|+\rangle / |-\rangle$  basis, verifying the entanglement. From Kaiser et al., 2012.

pattern of Eq. (13). The experimental results are shown in Fig. 25.

# E. Quantum delayed choice

Quantum delayed choice shares a few features with quantum erasure. An experiment following the proposal described in Sec. II.G was realized using single photons in an interferometer (Tang et al., 2012). This was achieved by taking the polarization state of the photon itself as the ancilla. Only the horizontally polarized photons  $|H\rangle$  passed through a second beam splitter, while for vertical polarization  $|V\rangle$  the interferometer was open. Similar to Eq. (10), with initial polarization state  $\sin \alpha |V\rangle +\cos \alpha |H\rangle$  the total one-photon state was transformed into

$$
| \psi \rangle = \sin \alpha | \text {p a r t i c l e} \rangle | V \rangle + \cos \alpha | \text {w a v e} \rangle | H \rangle , \tag {17}
$$

where  $|\mathrm{particle}\rangle = (|0\rangle +e^{i\varphi}|1\rangle) / \sqrt{2}$  and  $|\mathrm{wave}\rangle = e^{i\varphi /2}(\cos \varphi /2|0\rangle -i\sin \varphi /2|1\rangle)$ , similar to Eqs. (11) and (12), and  $|0\rangle$  and  $|1\rangle$  are the path states in the interferometer. [Note the different conventions for the ancilla bias parameter  $\alpha$  in states (10) and (17).]

The experimental setup is shown and explained in Fig. 26. If the final path measurement was not sensitive to the polarization (i.e., no polarizer at the end), the detection results were described by a mixed state (density matrix) of the form

$$
\sin^ {2} \alpha | \text {p a r t i c l e} \rangle \langle \text {p a r t i c l e} | + \cos^ {2} \alpha | \text {w a v e} \rangle \langle \text {w a v e} |. \tag {18}
$$

This corresponded to ignoring the ancilla outcome in Sec. II.G and led to a visibility pattern of the form  $\cos^2\alpha$ . If, however, the photon was postselected in the polarization state  $(|H\rangle + |V\rangle) / \sqrt{2}$  (i.e., polarizer at  $45^\circ$ ), its path state was left in the "wave-particle superposition"

$$
\sin \alpha | \text {p a r t i c l e} \rangle + \cos \alpha | \text {w a v e} \rangle . \tag {19}
$$

The experimental results for these two states were very different. Figure 27 shows the visibility as a function of  $\alpha$  for state (18) with solid circles and for state (19) with

![](images/232928898c2491f0e150c3ece92cdfab794b15f00b6cf4df02fc26e17e1ac480.jpg)  
FIG. 26. Experimental quantum delayed choice with single photons. Single photons entered the interferometer at beam displacer BD1 which split the light into horizontal and vertical polarization. The phase  $\varphi$  was scanned by the quartz plates before BD1. The "second beam splitter" in the closed (open) interferometer was provided by the combination of BD3, BD4, and halfwave plates HwP2 (HwP1). For HwP2 in the wave layer, the optical-axis direction  $\theta$  was set to  $22.5^{\circ}$  and interference appears (closed interferometer). For HwP1 in the particle layer  $\theta$  was set to  $0^{\circ}$  (open interferometer), showing the particle properties. Depending on the polarization (parameter  $\alpha$ ), BD2 controlled whether the photons passed through the particle or wave layer. The two layers were combined by BD5. A  $45^{\circ}$  polarizer could be inserted to postselect on the polarization state  $(|H\rangle + |V\rangle) / \sqrt{2}$ . Finally, two detectors counted the photons in paths 0 and 1. From Tang et al., 2012.

diamonds. The solid circle curve follows the expected form  $\cos^2\alpha$ , as only the wave part in Eq. (18) leads to fringes. The diamond curve is more complicated and reflects the fact that there was also quantum interference between the wave and particle properties.

Also a two-photon experiment was performed by Peruzzo et al. (2012) realizing the proposal of Ioniciou and Terno (2011). The setup, which used an integrated photonic device, is explained in Fig. 28.

The measured intensity at detector  $D^{\prime}$  was in excellent agreement with the theoretical prediction given by Eq. (13), as shown in Fig. 29. Since the ancilla photon was finally measured in its computational basis, the system photon

![](images/3f16811d72fe4226cf7fc307ab0fb2fbfc350c297530cdd913467f427214cedd.jpg)  
FIG. 27. Visibility as a function of  $\alpha$  for the mixed state (18) (solid circles) and for the superposition state (19) (diamonds). The solid circle curve has the form  $\cos^2\alpha$ , while the diamond one also reflects interference between wave and particle properties. The larger symbols are experimental data, while the smaller symbols are theoretical simulation results. From Tang et al., 2012.

![](images/3326aefba8a5535246cbc8a9ba298d9ad49c14d647b83801c6e7ca3252b5d914.jpg)  
FIG. 28. Two-photon experimental quantum delayed-choice experiment. Nonentangled photon pairs were injected into an integrated photonic device. The system photon ( $s$ , black optical path) passed a Hadamard gate ( $H$ ) and a phase shifter  $\varphi$ . The "second beam splitter" was a controlled Hadamard gate ( $CH$ ), implemented with additional Mach-Zehnder interferometers. The ancilla photon ( $a$ , top optical path) passed a phase shifter  $\alpha$ , allowing a superposition of present and absent beam splitter for the system photon. For the Bell test, single qubit rotations ( $U_{\mathrm{Alice}}$  and  $U_{\mathrm{Bob}}$ ) were performed before the photon detectors. Directional couplers are abbreviated by "dc" and resistive heaters are shown by rectangles. From Peruzzo et al., 2012.

data could be explained by a classical model in which the ancilla photon was prepared in a mixture of the form  $\cos^2\alpha |0\rangle \langle 0| + \sin^2\alpha |1\rangle \langle 1|$ . The particular state in every run would be known to the system photons beforehand, deciding whether their particle or wave behavior is measured.

To ensure that the choice cannot have been a classical variable known in advance, the entanglement of state (10) needed to be shown. This was done using unitary transformations at the final stage of the setup (Fig. 28) and performing a test of the Clauser-Horne-Shimony-Holt (Clauser et al., 1969) inequality. Maximal entanglement of the state (10) is reached for  $\alpha = \pi /4$  (ancilla initially in equal-weight superposition) and  $\varphi = \pi /2$  (for which  $\langle \mathrm{particle}| \mathrm{wave} \rangle = 0$ ). For this parameter choice, a Bell value of  $S = 2.45 \pm 0.03$  was reported, a significant violation of the local realistic bound 2 (Peruzzo et al., 2012). However, it was correctly acknowledged that the claim to have ruled out a classical description of the wave-particle duality without further assumptions would require a loophole-free Bell test, which has been demonstrated recently by three groups (Giustina et al., 2015; Hensen et al., 2015; Shalm et al., 2015).

![](images/0e8b809e5a1a197981e512648c74ab5e58304286f103b6492d5b2c0db41b1505.jpg)  
FIG. 29. Continuous transition between wave and particle behavior. The experimental data are shown by white dots and were fitted (colored surface) based on Eq. (13). From Peruzzo et al., 2012.

Two other successful realizations of the quantum delayed-choice scenario were achieved in nuclear magnetic resonance (NMR) experiments with  $^{13}\mathrm{CHCl}_3$  molecules. Roy, Shukla, and Mahesh (2012) encoded the system qubits (i.e., path in the interferometer) in the hydrogen nuclear spins, while the ancilla qubits (control of the interferometer) were encoded in carbon nuclear spins. According to Auccaise et al. (2012) it was exactly the opposite. Both experiments showed excellent agreement with the quantum predictions.

# F. Delayed-choice quantum random walk

An experimental realization of a delayed-choice two-dimensional (2D) quantum walk was reported by Jeong et al. (2013). There, the standard single-photon interferometer was replaced by a 2D quantum walk lattice, which was mapped to a temporal grid for the arrival times of a single photon by using polarization optical elements and fibers. In a quantum walk, a coin and a shift operator are applied repeatedly. The experimental scheme is shown in Fig. 30.

The essence of the experiment is similar to the quantum eraser concept. The way in which a photon interfered in the 2D quantum walk circuitry depended on its polarization, which was determined by the (delayed) polarization measurement of its distant twin. This was the first experiment

![](images/4705017c68d7fa1a143f6bae652ed88bdd1d00d1c1e14fc6a085d15db2446e04.jpg)  
FIG. 30. Experimental scheme of the delayed-choice quantum walk reported by Jeong et al. (2013). Entangled photon pairs were generated in a periodically poled  $\mathrm{KTiOPO_4}$  (PPKTP) crystal. One photon of every pair delayed in a  $340\mathrm{m}$  optical fiber and then sent to Alice, who was able to perform polarization measurements in any basis. This constituted a delayed-choice projection of the initial coin (polarization) state of the other photon, which was already sent to Bob without any fiber delay. In an optical loop, Bob's photons performed a 2D ( $x$  and  $y$  steps) quantum walk in the time domain. Before each step operation is taken, the coin operation ("Coin 1" and "Coin 2" are Hadamard gates) was applied. In order to map the 2D quantum walk lattice uniquely onto the photon arrival times, the lengths of the optical fibers ( $L1-L4$ ) were chosen appropriately. From Jeong et al., 2013.

realizing a 2D quantum walk with a single-photon source and in a delayed-choice fashion. Additionally, they also showed the first experimental simulation of a Grover walk, a model that can be used to implement the Grover quantum search algorithm (Grover, 1997). The similarities between the theoretical and experimental probability distributions in the Grover walk were above 0.95.

# V. REALIZATIONS OF DELAYED-CHOICE ENTANGLEMENT-SWAPPING EXPERIMENTS

Entanglement swapping (Zukowski et al., 1993) is a generalization of quantum teleportation (Bennett et al., 1993) and can teleport entangled states. It is of crucial importance in quantum information processing because it is one of the basic building blocks of quantum repeaters (Briegel et al., 1998; Duan et al., 2001), third-man quantum cryptography (Chen et al., 2005), and other protocols. On the other hand, entanglement swapping also allows experiments on the foundations of quantum physics, including loophole-free Bell tests (Simon and Irvine, 2003) and other fundamental tests of quantum mechanics (Greenberger, Horne, and Zeilinger, 2008; Greenberger, Horne, Zeilinger, and Zukowski, 2008). The entanglement-swapping protocol itself has been experimentally demonstrated with various physical systems (Pan et al., 1998; Barrett et al., 2004; Riebe et al., 2004; Halder et al., 2007; Matsukevich et al., 2008; Yuan et al., 2008; Kaltenbaek et al., 2009).

In light of finding which kind of physical interactions and processes are needed for the production of quantum entanglement, Peres (2000) put forward the radical idea of delayed-choice entanglement swapping. Realizations of this proposal are discussed in the following.

# A. Delayed entanglement swapping

Jennewein et al. (2001) performed a delayed entanglement-swapping experiment. For the conceptual setup, see Fig. 9. Detection of photons 2 and 3 by Victor was delayed by two  $10\mathrm{m}$  (about  $50~\mathrm{ns}$ ) optical fiber delays after the outputs of the Bell-state analyzer. Alice's and Bob's detectors were located next to each other. The traveling time of photons 1 and 4 from the source to these detectors was about  $20~\mathrm{ns}$ . Victor was separated from Alice and Bob by about  $2.5\mathrm{m}$ , corresponding to a luminal traveling time of approximately  $8\mathrm{ns}$  between them. Therefore, Victor's measurements were in the timelike future of Alice's and Bob's measurements. The observed fidelity of the measured state  $\rho_{14}$  of photons 1 and 4 with the ideal singlet state, defined as  ${}_{14}\langle\Psi^{-}|\rho_{14}|\Psi^{-}\rangle_{14}$ , was around 0.84, both above the classical limit of  $2/3$  and the limit of approximately 0.78 necessary to violate Bell's inequality, as shown in Fig. 31. This was the first attempt of the realization of delayed-choice entanglement swapping, although a switchable Bell-state analyzer has not been implemented.

We note that Sciarrino et al. (2002) performed a successful experiment on delayed entanglement swapping with two singlet entangled states comprised of the vacuum and the one-photon states. This allowed one to use a pair of entangled photons rather than four photons. The obtained correlation visibility was  $(91\pm 2)\%$

![](images/30292ec6598eeb53d2619100c7cd5cc25194a59f43f4547542665519e6711ee1.jpg)  
FIG. 31. Experimental results of delayed entanglement swapping. Data points show the entanglement fidelity obtained through correlation measurements between photons 1 and 4. Data shown with white open squares (a black filled circle) was obtained when Victor's Bell-state measurement was spacelike separated from (in the timelike future of) Alice's and Bob's measurements. The angles  $\phi_0 / \phi_3$  are the setting of the polarization analyzer for photons  $1/4$  (Fig. 9), which were aligned to be equal. The minimum fidelity is above the limit achievable with classical swapping protocols as well as above the limit necessary for violating a Bell inequality with the swapped entangled state. From Jennewein et al., 2001.

![](images/f5544042ae89ad13cfc633f6d9c9ca76301800271c5d2c3d19b6b152a076af34.jpg)  
FIG. 32. Experimental setup of delayed-choice entanglement swapping. Two polarization-entangled photon pairs (photons 1 and 2, and photons 3 and 4) were generated from BBO crystals. Alice and Bob measured the polarization of photons 1 and 4 in whatever basis they chose. Photons 2 and 3 were each delayed with  $104\mathrm{m}$  fiber and then overlapped on the tunable bipartite state analyzer (BiSA) (top block). The BiSA performed either a Bell-state measurement (BSM) or a separable-state measurement (SSM), depending on the outcome of a QRNG. An active phase stabilization system was employed in order to compensate the phase noise in the tunable BiSA. From Ma et al., 2012.

# B. Delayed-choice entanglement swapping

A refined and conclusive realization of Peres' gedanken experiment was reported (Ma et al., 2012). The layout of this experiment is illustrated in Fig. 32. The essential point was the implementation of bipartite state projections based on the random and delayed choice. The choice was to either perform a BSM or a separable-state measurement (SSM) on photons 2 and 3. In order to realize this, a bipartite state analyzer (BiSA) with two-photon interference on a high-speed tunable beam splitter combined with photon detections was used.

The initial four-photon entangled state was of the form (8). Alice and Bob measured the polarization of photons 1 and 4 without any delay. Photons 2 and 3 were sent through  $104\mathrm{m}$  single-mode fibers, corresponding to a delay time of  $520~\mathrm{ns}$ . Victor actively chose and implemented the measurements on photons 2 and 3 (either BSM or SSM) by using a high-speed tunable BiSA. A QRNG was used to make the random choice. Both the choice and the measurement of photons 2 and 3 were in the timelike future of the registration of photons 1 and 4. This projected the state of the two already registered photons, 1 and 4, onto either an entangled or a separable state.

The diagram of the temporal order of the relevant events is shown in Fig. 33. For each successful run (a fourfold coincidence count), both Victor's measurement event and his choice were in the timelike future of Alice's and Bob's measurements.

![](images/2f4bfcf342c3740c1ecd07faa403adc3458ec92ae133290b693a91233fe3725c.jpg)  
FIG. 33. Time diagram of the delayed-choice entanglement-swapping experiment. Two entangled photon pairs (1 and 2, and 3 and 4) were generated by EPR sources I and II (events  $\mathbf{G}_{\mathrm{I}}$  and  $\mathbf{G}_{\mathrm{II}}$ ) at 0 ns. Alice and Bob measured the polarization of photons 1 and 4 at 35 ns (events  $\mathbf{M}_{\mathrm{A}}$  and  $\mathbf{M}_{\mathrm{B}}$ ). Photons 2 and 3 were delayed and sent to Victor who chose (event  $\mathbf{C}_{\mathrm{V}}$ ) to perform a Bell-state measurement (BSM) or a separable-state measurement (SSM) (event  $\mathbf{M}_{\mathrm{V}}$ ). Victor's choice and measurement were made after Alice's and Bob's polarization measurements. From Ma et al., 2012.

![](images/032542f30bcd4070f486a01f516393958bf2cf1ef7b39900e2b80c36fa66caab.jpg)  
FIG. 34. Correlation functions from the experiment of Ma et al. (2012). (a) Victor subjected photons 2 and 3 to a Bell-state measurement and observed the result  $|\Phi^{-}\rangle_{23}$ . Alice's and Bob's photons 1 and 4 were projected into the corresponding entangled state  $|\Phi_{14}^{-}\rangle$ , showing correlations in all three mutually unbiased bases  $|H\rangle / |V\rangle$ ,  $|R\rangle / |L\rangle$ , and  $|+\rangle / |-\rangle$ . Entanglement between photons 1 and 4 is witnessed by the absolute sum of the correlation values exceeding 1. (b) When Victor performed a separable-state measurement in the  $|H\rangle / |V\rangle$  basis, photons 1 and 4 also ended up in the corresponding separable state and hence showed correlations only in that basis but not the other two. From Ma et al. (2012).

![](images/0ec295d3ae507b8593afe24f800f1914957320f088a06e598fc6e62b20804885.jpg)

In that experiment, the existence of entanglement was verified by measuring the state fidelities and the expectation values of entanglement witness operators (Guhne and Toth, 2009). It was found that whether photons 1 and 4 were entangled or separable depended only on the type of the measurements Victor implemented, not on the temporal order (Fig. 34).

# VI. CONCLUSION AND OUTLOOK

Delayed-choice gedanken experiments and their realizations play an important role in the foundations of quantum physics, because they serve as striking illustrations of the counterintuitive and inherently nonclassical features of quantum mechanics. A summary of the photonic delayed-choice experiments discussed in this review is presented in Table I.

Wheeler's delayed-choice experiments challenge a realistic explanation of the wave-particle duality. In such an

explanation every photon is assumed to behave either definitely as a wave (traveling both paths in an interferometer) or definitely as a particle (traveling only one of the paths), by adapting a priori on the experimental situation. Especially when the choice of whether or not to insert the second beam splitter into an interferometer is made spacelike separated from the photon's entry into the interferometer, this picture becomes untenable.

In delayed-choice experiments with two entangled quantum systems such as the delayed-choice quantum eraser, one can choose that one system exhibits wave or particle behavior by choosing different measurements for the other one. These choices and measurements can be made even after the former system has already been detected.

In delayed-choice entanglement-swapping experiments, one can demonstrate that whether two quantum systems are entangled or separable can be decided even after they have been measured. This generalizes the wave-particle duality for single systems to an entanglement-separability duality for two (and more) systems.

It is a general feature of delayed-choice experiments that quantum effects can mimic an influence of future actions on past events. However, there never emerges any paradox if the quantum state is viewed only as a "catalog of our knowledge" (Schrodinger, 1935) without any underlying hidden-variable description. Then the state is a probability list for all possible measurement outcomes and not a real physical object. The relative temporal order of measurement events is not relevant, and no physical interactions or signals, let alone into the past, are necessary to explain the experimental results. To interpret quantum experiments, any attempt in explaining what happens in an individual observation of one system has to include the whole experimental configuration and also the complete quantum state, potentially describing joint properties with other systems. According to Bohr and Wheeler, no elementary phenomenon is a phenomenon until it is a registered phenomenon (Bohr, 1949; Wheeler, 1984). In light of quantum erasure and entanglement swapping, one might like to even

TABLE I. A summary of delayed-choice experiments realized with photons.  $C, I,$  and  $M$  stand for the space-time relations between events  $C$  (choice),  $I$  (entry into the interferometer), and  $M$  (measurement of the photon). Note that in the experiments involving more than one photon,  $M$  stands for the measurement of ancillary photon(s). Other abbreviations: sep. stands for spacelike separated, after and before stand for timelike after and timelike before, ext. and int. stand for external and internal, QRNG stands for quantum random number generator, and BS stands for beam splitter. For example, the entry "before" in the  $C$  and  $I$  column means that  $C$  happens timelike before  $I$ .  

<table><tr><td>Experiment (Reference)</td><td>Number of photons</td><td>Nature of the choice</td><td>C and I</td><td>M and I</td></tr><tr><td>Alley et al. (1983)</td><td>1</td><td>Ext. choice, photon detection</td><td>Sep.</td><td>After</td></tr><tr><td>Hellmuth et al. (1987)</td><td>1</td><td>Fixed setting</td><td>Before</td><td>After</td></tr><tr><td>Baldzuhn, Mohler, and Martienssen (1989)</td><td>1</td><td>Fixed setting</td><td>Before</td><td>After</td></tr><tr><td>Jacques et al. (2007, 2008)</td><td>2</td><td>Ext. choice, shot noise</td><td>Sep.</td><td>After</td></tr><tr><td>Dopfer (1998)</td><td>2</td><td>Fixed setting</td><td>Before</td><td>After</td></tr><tr><td>Walborn et al. (2002)</td><td>2</td><td>Fixed setting</td><td>Before</td><td>After</td></tr><tr><td>Kim et al. (2000)</td><td>2</td><td>Int. choice, 50/50 BS</td><td>After</td><td>After</td></tr><tr><td>Ma et al. (2013)</td><td>2</td><td>Ext. choice, QRNG with 50/50 BS</td><td>Sep. &amp; after</td><td>Sep. &amp; after</td></tr><tr><td>Tang et al. (2012)</td><td>1</td><td>Quantum delayed choice, fixed setting</td><td>Before</td><td>After</td></tr><tr><td>Kaiser et al. (2012)</td><td>2</td><td>Quantum delayed choice, fixed setting</td><td>Before</td><td>Sep.</td></tr><tr><td>Peruzzo et al. (2012)</td><td>2</td><td>Quantum delayed choice, fixed setting</td><td>Before</td><td>After</td></tr><tr><td>Jeong et al. (2013)</td><td>1</td><td>Fixed setting</td><td>Before</td><td>After</td></tr><tr><td>Jennewein et al. (2001)</td><td>4</td><td>Fixed setting</td><td>Before</td><td>After</td></tr><tr><td>Sciarrino et al. (2002)</td><td>2</td><td>Fixed setting</td><td>Before</td><td>...</td></tr><tr><td>Ma et al. (2012)</td><td>4</td><td>Ext. choice, QRNG with 50/50 BS</td><td>After</td><td>After</td></tr></table>

say that some registered phenomena do not have a meaning unless they are put in relationship with other registered phenomena (Ma et al., 2012).

Delayed-choice gedanken experiments and their realizations have played important roles in the development of quantum physics. The applicability of the delayed-choice paradigm for practical quantum information processing is yet to be explored. For example, Lee et al. (2014) introduced and experimentally demonstrated a delayed-choice decoherence suppression protocol. In their experiment, the decision to suppress decoherence on an entangled two-qubit state is delayed until after the decoherence and even after the detection of the qubit. This result suggests a new way to tackle Markovian decoherence in a delayed-choice way, which could be useful for practical entanglement distribution over a dissipative channel.

The concept of delayed-choice entanglement swapping is of importance for the security of quantum communication schemes such as third-man quantum cryptography (Chen et al., 2005) and could also be employed in probabilistic instantaneous quantum computing. In the latter case, quantum state teleportation and entanglement swapping imply a computational speed-up in time over classical procedures (Jennewein, 2002; Brukner et al., 2003). This can be realized by sending one photon of a Bell state into the input of a quantum computer and performing a quantum computation with it. Since this photon is a part of a Bell state, its individual property is not well defined. Therefore, the output of the quantum computation will also not be defined. However, as soon as the required input is known, it can be teleported onto the state of the photon which had been fed into the quantum computer. If the BSM results in one specific Bell state which requires no corrective unitary transformation, then immediately the output of the quantum computer will be projected into the correct result. By this means the computation is performed quasi-instantaneously. Note that this instantaneous quantum computation is intrinsically probabilistic because the BSM results in all four Bell states with equal probability of  $1/4$ .

Finally, we observe that the development of quantum mechanics has been accompanied initially by a series of ingenious gedanken experiments, which have—with the advance of technology—found more and more realizations over time. This again has opened up avenues for new experiments and even applications. Likewise, while the history of the delayed-choice paradigm dates back to the early days of quantum mechanics, only in the past decades have many remarkable experiments demonstrated its counterintuitive aspects in different scenarios and with different physical systems. It can be expected that delayed-choice gedanken experiments will continue to lead to novel foundational tests as well as further practical implementations.

# ACKNOWLEDGMENTS

We thank Guido Bacciagaluppi, Daniel Greenberger, Radu Ioniciou, Thomas Jennewein, Florian Kaiser, Marlan Scully, Sébastien Tanzilli, Daniel R. Terno, and Marek Zukowski for helpful comments and remarks. X. S. M. is supported by a Marie Curie International Outgoing Fellowship within the 7th

European Community Framework Programme and Youth Qianren Program. A.Z. acknowledges support by the Austrian Science Fund through the Project SFB 40 and by the European Commission.

# REFERENCES

Aharonov, Y., and M. S. Zubairy, 2005, Science 307, 875.  
Alley, C. O., O. Jakubowicz, C. A. Steggerda, and W. C. Wickes, 1983, in International Symposium on Foundations of Quantum Mechanics in the Light of New Technology (Physical Society of Japan, Tokyo).  
Alley, C. O., O. Jakubowicz, and W. C. Wickes, 1986, in 2nd International Symposium on Foundations of Quantum Mechanics in the Light of New Technology (Physical Society of Japan, Tokyo).  
Auccaise, R., R. M. Serra, J. G. Filgueiras, R. S. Sarthour, I. S. Oliveira, and L. C. Celeri, 2012, Phys. Rev. A 85, 032121.  
Baldzuhn, J., E. Mohler, and W. Martienssen, 1989, Z. Phys. B 77, 347.  
Ballentine, L.E., 1998, Quantum Mechanics: A Modern Development (World Scientific Publishing Company, Singapore).  
Barrett, M. D., et al., 2004, Nature (London) 429, 737.  
Bell, J. S., 1964, Physics (N.Y.) 1, 195.  
Bell, J. S., 2004, Speakable and Unspeakable in Quantum Mechanics (Cambridge University Press, Cambridge, UK), pp. 243-244, revised edition.  
Bennett, C. H., G. Brassard, C. Crépeau, R. Jozsa, A. Peres, and W. K. Wootters, 1993, Phys. Rev. Lett. 70, 1895.  
Bohr, N., 1928, Nature (London) 121, 580.  
Bohr, N., 1935, Phys. Rev. 48, 696.  
Bohr, N., 1949, in Albert Einstein: Philosopher-Scientist, edited by P. A. Schlipp, The Library of Living Philosophers (MJF Books, New York).  
Bramon, A., G. Garbarino, and B.C. Hiesmayr, 2004, Phys. Rev. Lett. 92, 020405.  
Branciard, C., 2013, Proc. Natl. Acad. Sci. U.S.A. 110, 6742.  
Briegel, H.-J., W. Dür, J. I. Cirac, and P. Zoller, 1998, Phys. Rev. Lett. 81, 5932.  
Brukner, C., J.-W. Pan, C. Simon, G. Weihs, and A. Zeilinger, 2003, Phys. Rev. A 67, 034304.  
Brunner, N., D. Cavalcanti, S. Pironio, V. Scarani, and S. Wehner, 2014, Rev. Mod. Phys. 86, 419.  
Busch, P., T. Heinonen, and P. Lahti, 2007, Phys. Rep. 452, 155.  
Busch, P., P. Lahti, and R. F. Werner, 2013, Phys. Rev. Lett. 111, 160405.  
Céleri, L. C., R. M. Gomes, R. Ioniciou, T. Jennewein, R. B. Mann, and D. R. Terno, 2014, Found. Phys. 44, 576.  
Chen, Y.-A., A.-N. Zhang, Z. Zhao, X.-Q. Zhou, C.-Y. Lu, C.-Z. Peng, T. Yang, and J.-W. Pan, 2005, Phys. Rev. Lett. 95, 200502.  
Clauser, J. F., M. A. Horne, A. Shimony, and R. A. Holt, 1969, Phys. Rev. Lett. 23, 880.  
Coffman, V., J. Kundu, and W. K. Wootters, 2000, Phys. Rev. A 61, 052306.  
Cohen,O.,1999,Phys.Rev.A60,80.  
Colella, R., A. W. Overhauser, and S. A. Werner, 1975, Phys. Rev. Lett. 34, 1472.  
Davisson, C., and L. H. Germer, 1927, Phys. Rev. 30, 705.  
de Broglie, L., 1924, Recherches sur la théorie des quanta, Ph.D. thesis, Migration—université en cours d'affection, Paris.  
Dopfer, B., 1998, Zwei Experimente zur Interferenz von Zwei-Photonen Zuständen. Ein Heisenbergmikroskop und Pendellösung, Ph.D. thesis (University of Innsbruck).

Duan, L. M., M. D. Lukin, J. I. Cirac, and P. Zoller, 2001, Nature (London) 414, 413.  
Durr, S., T. Nonn, and G. Rempe, 1998, Nature (London) 395, 33.  
Eichmann, U., J. C. Bergquist, J. J. Bollinger, J. M. Gilligan, W. M. Itano, D. J. Wineland, and M. G. Raizen, 1993, Phys. Rev. Lett. **70**, 2359.  
Einstein,A.,1905,Ann.Phys.(Berlin)322,23.  
Einstein,A.,1931,Angew.Chem.45,718.  
Einstein, A., B. Podolsky, and N. Rosen, 1935, Phys. Rev. 47, 777.  
Englert, B.-G., 1996, Phys. Rev. Lett. 77, 2154.  
Englert, B.-G., M. O. Scully, and H. Walther, 1995, Nature (London) 375, 367.  
Estermann, I., and O. Stern, 1930, Z. Phys. 61, 95.  
Friberg, S., C. K. Hong, and L. Mandel, 1985, Phys. Rev. Lett. 54, 2011.  
Gallicchio, J., A. S. Friedman, and D. I. Kaiser, 2014, Phys. Rev. Lett. 112, 110405.  
Gerlich, S., S. Eibenberger, M. Tomandl, S. Nimmrichter, K. Hornberger, P.J. Fagan, J. Tuexen, M. Mayor, and M. Arndt, 2011, Nat. Commun. 2, 263.  
Giustina, M., et al., 2015, Phys. Rev. Lett. 115, 250401.  
Grangier, P., 1986, Experimental study of non-classical properties of light; single-photon interferences, Ph.D. thesis (Institut d'Optique et Université Paris).  
Greenberger, D. M., M. Horne, and A. Zeilinger, 2008, Phys. Rev. A 78, 022110.  
Greenberger, D. M., M. Horne, A. Zeilinger, and M. Zukowski, 2008, Phys. Rev. A 78, 022111.  
Greenberger, D. M., M. A. Horne, C. G. Shull, and A. Zeilinger, 1983, in International Symposium on Foundations of Quantum Mechanics in the Light of New Technology (Physical Society of Japan, Tokyo).  
Greenberger, D. M., and A. Yasin, 1988, Phys. Lett. A 128, 391.  
Grover, L. K., 1997, Phys. Rev. Lett. 79, 325.  
Gühne, O., and G. Toth, 2009, Phys. Rep. 474, 1.  
Halder, M., A. Beveratos, N. Gisin, V. Scarani, C. Simon, and H. Zbinden, 2007, Nat. Phys. 3, 692.  
Heisenberg, W., 1927, Z. Phys. 43, 172.  
Heisenberg, W., 1991, Physikalische Prinzipien der Quantentheorie (B.I.-Wissenschaftsverlag, Mannheim/Wien/Zürich).  
Hellmuth, T., H. Walther, A. Zajonc, and W. Schleich, 1987, Phys. Rev. A 35, 2532.  
Hensen,B.,et al.,2015,Nature(London)526,682.  
Hermann, G., 1935, Naturwissenschaften 23, 718.  
Herzog, T. J., P. G. Kwiat, H. Weinfurter, and A. Zeilinger, 1995, Phys. Rev. Lett. 75, 3034.  
Horodecki, R., P. Horodecki, M. Horodecki, and K. Horodecki, 2009, Rev. Mod. Phys. 81, 865.  
Ionicioui, R., T. Jennewein, R. B. Mann, and D. R. Terno, 2014, Nat. Commun. 5, 3997.  
Ionicioui, R., R.B. Mann, and D.R. Terno, 2015, Phys. Rev. Lett. 114, 060405.  
Ionicioiu, R., and D. R. Terno, 2011, Phys. Rev. Lett. 107, 230406.  
Jacques, V., E. Wu, F. Grosshans, F. Treussart, P. Grangier, A. Aspect, and J.-F. Roch, 2007, Science 315, 966.  
Jacques, V., E. Wu, F. Grosshans, F. Treussart, P. Grangier, A. Aspect, and J.-F. Roch, 2008, Phys. Rev. Lett. 100, 220402.  
Jaeger, G., A. Shimony, and L. Vaidman, 1995, Phys. Rev. A 51, 54.  
Jakubowicz, O.G., 1984, A delayed random choice quantum mechanics experiment using light quanta., Ph.D. thesis (Maryland University, College Park).

Jennewein, T., 2002, Quantum Communication and Teleportation Experiments using Entangled Photon Pairs, Ph.D. thesis (University of Vienna).  
Jennewein, T., U. Achleitner, G. Weihs, H. Weinfurter, and A. Zeilinger, 2000, Rev. Sci. Instrum. 71, 1675.  
Jennewein, T., G. Weihs, J.-W. Pan, and A. Zeilinger, 2001, Phys. Rev. Lett. 88,017903.  
Jeong, Y.C., C.D. Franco, and H.T. Lim, and M.S. Kim, and Y.H. Kim, 2013, Nat. Commun. 4, 2471.  
Joensson, C., 1961, Z. Phys. 161, 454.  
Joobeur, A., B. E. A. Saleh, and M. C. Teich, 1994, Phys. Rev. A 50, 3349.  
Kaiser, F., T. Coudreau, P. Milman, D. B. Ostrowsky, and S. Tanzilli, 2012, Science 338, 637.  
Kaltenbaek, R., R. Prevedel, M. Aspelmeyer, and A. Zeilinger, 2009, Phys. Rev. A 79, 040302.  
Kennard,E.H.,1927,Z.Phys.44,326.  
Kim, Y.-H., R. Yu, S. P. Kulik, Y. Shih, and M. O. Scully, 2000, Phys. Rev. Lett. 84, 1.  
Kurtsiefer, C., S. Mayer, P. Zarda, and H. Weinfurter, 2000, Phys. Rev. Lett. 85, 290.  
Kwait, P. G., K. Mattle, H. Weinfurter, A. Zeilinger, A. V. Sergienko, and Y. Shih, 1995, Phys. Rev. Lett. 75, 4337.  
Kwiat, P.G., and B.-G. Englert, 2004, in Science and Ultimate Reality: Quantum Theory, Cosmology and Complexity, edited by J. D. Barrow, P. C. W. Davies, and S. C. L. Harper, Jr. (Cambridge University Press, Cambridge, England).  
Lee, L. C., H. T. Lim, K. H. Hong, Y. C. Jeong, M. S. Kim, and Y. H. Kim, 2014, Nat. Commun. 5, 4522.  
Ma, X.-S., 2010, Nonlocal delayed-choice experiments with entangled photons, Ph.D. thesis (University of Vienna).  
Ma, X.-S., A. Qarry, J. Kofler, T. Jennewein, and A. Zeilinger, 2009, Phys. Rev. A 79, 042101.  
Ma, X.-S., S. Zotter, J. Kofler, R. Ursin, T. Jennewein, C. Brukner, and A. Zeilinger, 2012, Nat. Phys. 8, 479.  
Ma, X.-S., et al., 2013, Proc. Natl. Acad. Sci. U.S.A. 110, 1221.  
Mach, L., 1892, Z. Instrumentenkd. 12, 89.  
Manning, A.G., R.I. Khakimov, R.G. Dall, and A.G. Truscott, 2015, Nat. Phys. 11, 539.  
Matsukevich, D. N., P. Maunz, D. L. Moehring, S. Olmschenk, and C. Monroe, 2008, Phys. Rev. Lett. 100, 150404.  
Miller, W. A., 1983, in International Symposium on Foundations of Quantum Mechanics in the Light of New Technology (Physical Society of Japan, Tokyo).  
Miller, W. A., and J. A. Wheeler, 1983, in International Symposium on Foundations of Quantum Mechanics in the Light of New Technology (Physical Society of Japan, Tokyo).  
Mittelstaedt, P., 1986, in 2nd International Symposium on Foundations of Quantum Mechanics in the Light of New Technology (Physical Society of Japan, Tokyo).  
Nielsen, M. A., and I. L. Chuang, 2000, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, England).  
Ozawa,M.,2004,Phys.Lett.A320,367.  
Pan, J.-W., D. Bouwmeester, H. Weinfurter, and A. Zeilinger, 1998, Phys. Rev. Lett. 80, 3891.  
Pan, J.-W., Z.-B. Chen, C.-Y. Lu, H. Weinfurter, A. Zeilinger, and M. Zukowski, 2012, Rev. Mod. Phys. 84, 777.  
Paul,H.,1982,Rev.Mod.Phys.54,1061.  
Peres,A.,2000,J.Mod.Opt.47,139  
Peruzzo, A., P. Shadbolt, N. Brunner, S. Popescu, and J. L. OBrien, 2012, Science 338, 634.  
Rarity, J. G., and P. R. Tapster, 1990, Phys. Rev. Lett. 64, 2495.

Rauch, H., W. Treimer, and U. Bonse, 1974, Phys. Lett. A 47, 369.  
Riebe, M., et al., 2004, Nature (London) 429, 734.  
Robertson,H.P.,1929,Phys.Rev.34,163  
Roy, S. S., A. Shukla, and T. S. Mahesh, 2012, Phys. Rev. A 85, 022109.  
Sagnac, G., 1913, C.R. Phys. 157, 708.  
Scarcelli, G., Y. Zhou, and Y. Shih, 2007, Eur. Phys. J. D 44, 167.  
Scheidl, T., et al., 2010, Proc. Natl. Acad. Sci. U.S.A. 107, 19708.  
Schleich, W., and H. Walther, 1986, in 2nd International Symposium on Foundations of Quantum Mechanics in the Light of New Technology (Physical Society of Japan, Tokyo).  
Schrödinger, E., 1930, Physikalisch-mathematische Klasse 14, 296.  
Schrödinger, E., 1935, Naturwissenschaften 23, 844.  
Sciarrino, F., E. Lombardi, G. Milani, and F. De Martini, 2002, Phys. Rev. A 66, 024309.  
Scully, M. O., and K. Druhl, 1982, Phys. Rev. A 25, 2208.  
Scully, M. O., B.-G. Englert, and J. Schwinger, 1989, Phys. Rev. A 40, 1775.  
Scully, M. O., B.-G. Englert, and H. Walther, 1991, Nature (London) 351, 111.  
Shalm, L. K., et al., 2015, Phys. Rev. Lett. 115, 250402.  
Shih, Y. H., and C. O. Alley, 1988, Phys. Rev. Lett. 61, 2921.  
Simon, C., and W. T. M. Irvine, 2003, Phys. Rev. Lett. 91, 110405.  
Stapp, H., 2009, in Compendium of Quantum Physics, edited by D. Greenberger, K. Hentschel, and F. Weinert (Springer, New York).  
Storey, P., S. Tan, M. Collett, and D. Walls, 1994, Nature (London) 367, 626.  
Storey, P., S. Tan, M. Collett, and D. Walls, 1995, Nature (London) 375, 368.  
Tang, J.-S., Y.-L. Li, X.-Y. Xu, G.-Y. Xiang, C.-F. Li, and G.-C. Guo, 2012, Nat. Photonics 6, 600.

Taylor, G. I., 1909, Proc. Cambridge Philos. Soc. 15, 114.  
von Weizsacker, C. F., 1941, Z. Phys. 118, 489.  
von Weizsacker, K.F., 1931, Z. Phys. 70, 114.  
Walborn, S. P., M. O. Terra Cunha, S. Pádua, and C. H. Monken, 2002, Phys. Rev. A 65, 033818.  
Weisz, E., H. K. Choi, I. Sivan, M. Heiblum, Y. Gefen, D. Mahalu, and V. Umansky, 2014, Science 344, 1363.  
Weyl, H., 1928, Gruppentheorie und Quantenmechanik (Leipzig, Hirzel).  
Wheeler, J. A., 1978, in Mathematical Foundations of Quantum Theory, edited by R. Marlow (Academic Press, New York).  
Wheeler, J. A., 1984, in Quantum Theory and Measurement, edited by J. A. Wheeler and W. H. Zurek (Princeton University Press, Princeton, NJ).  
Wiseman, H. M., and F. E. Harrison, 1995, Nature (London) 377, 584.  
Wiseman, H. M., F. E. Harrison, M. J. Collett, S. M. Tan, D. F. Walls, and R. B. Killip, 1997, Phys. Rev. A 56, 55.  
Wootters, W.K., and B.D. Fields, 1989, Ann. Phys. (N.Y.) 191, 363.  
Wootters, W.K., and W.H. Zurek, 1979, Phys. Rev. D 19, 473.  
Young, T., 1804, Philos. Trans. R. Soc. London 94, 1.  
Yuan, Z.-S., Y.-A. Chen, B. Zhao, S. Chen, J. Schmiedmayer, and J.-W. Pan, 2008, Nature (London) 454, 1098.  
Zehnder, L., 1891, Z. Instrumentenkd. 11, 275.  
Zeilinger, A., 1999, Rev. Mod. Phys. 71, S288.  
Zeilinger, A., G. Weihs, T. Jennewein, and M. Aspelmeyer, 2005, Nature (London) 433, 230.  
Zukowski, M., A. Zeilinger, M. A. Horne, and A. K. Ekert, 1993, Phys. Rev. Lett. 71, 4287.