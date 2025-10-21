# Taking atom interferometric quantum sensors from the laboratory to real-world applications

Kai Bongs, Michael Holynski, Jamie Vovrosh, Philippe Bouyer, Gabriel Condon, Ernst Rasel, Christian Schubert, Wolfgang P. Schleich and Albert Roura

Abstract | Since the first proof-of-principle experiments over 25 years ago, atom interferometry has matured to a versatile tool that can be used in fundamental research in particle physics, general relativity and cosmology. At the same time, atom interferometers are currently moving out of the laboratory to be used as ultraprecise quantum sensors in metrology, geophysics, space, civil engineering, oil and minerals exploration, and navigation. This Perspective discusses the associated scientific and technological challenges and highlights recent advances.

Wave-particle duality<sup>1</sup> underpins the possibility of matter displaying the same type of interference phenomena as light. Indeed, matter-wave interference has been demonstrated for a variety of systems, including electrons<sup>2,3</sup>, neutrons<sup>4,5</sup>, atoms<sup>6-9</sup> and even biomolecules<sup>10</sup>. However, atoms have become the prime choice for matter-wave interferometry precision measurements thanks to their precise controllability (enabled by their internal structure, whose quantum states can be manipulated with electromagnetic fields) and their lack of electric charge, which ensures little interaction with unwanted environmental influences, such as electric and magnetic fields.

Many atom interferometers conceptually resemble an optical Mach-Zehnder interferometer. In such an interferometer, a light beam is split by a beamsplitter into two beams, which, after a certain distance, are redirected towards each other with mirrors and mixed in another beamsplitter, when they overlap again. This leads to interference visible in the power emerging from the two output ports of the final beamsplitter. Today, most atom interferometers rely on light-pulse atom-optical elements: light takes the role of mirrors and beamsplitters for the matter waves, effectively inverting the roles of light and matter in a traditional, optical interferometer. When laser light

resonant with an atomic transition interacts with an atom, it coherently drives the populations in the ground and excited states in an oscillatory manner, the so-called Rabi oscillations $^{11}$  (FIG. 1a). Starting with the atoms in the ground state and timing the laser pulse to stop after a quarter of an oscillation, that is, after a  $\pi /2$  phase evolution of the Rabi oscillation, will put the atoms into an equal-probability superposition of the ground and excited states. This so-called  $\pi /2$  pulse' acts as a 50:50 beamsplitter. Similarly, a  $\pi$  pulse' is timed to last half an oscillation and inverts the population of the ground and excited states, acting as a mirror.

Taking into account the photon momentum, these laser pulses create a superposition not only of internal but also of momentum states. The excited part of the superposition, which has absorbed the photon and acquired the photon momentum, will move away from the part left in the ground state, allowing the atoms to simultaneously travel along different trajectories. When these paths differ in height, the resulting interference phase will depend on the gravitational potential difference between the trajectories, and the interferometer becomes a very sensitive gravity sensor. The simplest case of an atom-interferometer gravity sensor relies on three light pulses in a  $\pi /2 - \pi -\pi /2$  sequence, which effectively

creates the matter-wave counterpart of a Mach-Zehnder interferometer (FIG. 1b).

Since the first laboratory demonstration of atom interferometers over 25 years ago $^{8,12}$ , many variants have been developed and, nowadays, these devices are used in applications ranging from the foundations of physics $^{13-15}$  to commercial quantum technologies $^{16}$ . This Perspective describes the applications and highlights the challenges in taking atom interferometers from proof-of-principle laboratory-based systems to portable devices used in real-world environments. This journey from the lab to the users is summarized in FIG. 2.

# Precision for fundamental physics

Tests of fundamental physics provide a relatively straightforward first step on the road from laboratory proof-of-principle experiments to applications, as the instrument stays in a well-controlled laboratory environment, is operated by scientists and the main focus is on increasing precision. We review several developments, starting with the use of atom interferometry as a tool to determine fundamental constants.

# Fundamental constants

Atomic masses and fine-structure constant  $\alpha$ . When an atom absorbs a photon, it also absorbs the photon's momentum, resulting in a change of its kinetic energy by an amount equal to the recoil energy. Extending the laser-pulse sequence in an atom interferometer to four  $\pi/2$  pulses creates two closed interferometers (FIG. 3a). The difference between the phase shifts of the two interferometers is proportional to the recoil energy acquired during the beamsplitter  $\pi/2$  pulses.

Combining this interferometer scheme with a precise determination of the wavelength of the light used for the laser pulses allows to obtain a precise value of  $h / m_{X}$ , where  $h$  denotes Planck's constant and  $m_{X}$  is the mass of the atomic species<sup>17</sup>. In the new SI units<sup>18</sup>, where the value of  $h$  is fixed, this approach provides a direct measurement of the inertial mass at microscopic scales. A link to macroscopic scales can then be established through the silicon spheres of the Avogadro Project<sup>19</sup>, whose total number of atoms can be very accurately determined.

![](images/aafadc1adca91eaae8a02ad035163a55692e42969bbd9827acf8c6c2dd3be172.jpg)  
Fig. 1 | Building blocks of an atom interferometer and its use as a gravity sensor. a | The probability of finding a two-level atom in its excited state versus the interaction time, which is the duration of a laser pulse exciting the atom initially in the ground state. If the energy of the laser photon corresponds to the energy difference between the two atomic states, the occupation probabilities (referred to as population) of the states will undergo periodic Rabi oscillations with the Rabi frequency  $\Omega$ . A laser pulse of duration  $\pi/(2\Omega)$  leaves the atoms in a 50:50 superposition of the ground and excited states, whereas one of duration  $\pi/\Omega$  takes the atom from the ground to the excited state with  $100\%$  probability. b | Operation of an atom interferometer as a gravity sensor. In its most basic implementation, a cloud of atoms initially in their ground state is subjected to a time sequence of three laser pulses. The first pulse puts the atoms into a 50:50 superposition of the ground and excited states ( $\pi/2$  pulse). The atoms in the excited state have absorbed a photon and start to move away from those in the ground state due to the transfer of momentum in this process. After a time,  $T$ , another laser pulse is applied with  $100\%$  probability for the ground state to absorb a photon and  $100\%$  probability for the excited state to emit a photon by stimulated emission. Thus, this pulse swaps ground-state and excited-state populations ( $\pi$  pulse). The associated momentum transfers make the atomic trajectories converge, such that they overlap again after time  $T$ . At this point, another  $\pi/2$  pulse mixes the populations in both states, creating interference visible in the populations of the ground and excited states output ports of the interferometer. The interferometer phase, determined by the gravitational acceleration,  $g$ , can be readout by counting the number of atoms in each output port, that is, counting the number of excited-state atoms versus the number of ground-state atoms at the end of the sequence. The sensitivity of the interferometer is proportional to the total spacetime area enclosed by the two trajectories.

![](images/4c6922b3286fff1a34d2c565a2bb50532c91251d1b241c1c40224bcf11c9da02.jpg)

In addition, an accurate quantification of  $h / m_{X}$  also provides an accurate way of determining the fine-structure constant $^{13,17,20}$ ,  $\alpha$ , by linking the two quantities with the Rydberg constant,  $R_{\infty}$ , which can be determined with great accuracy through spectroscopy. In fact, the most accurate results for the fine-structure constant to date, corresponding to  $\alpha = 1/137.035999046(27)$  with a relative uncertainty of  $2 \times 10^{-10}$ , have been obtained based on this approach $^{13}$  and surpass those obtained from the measurement of the anomalous magnetic moment of the electron $^{21}$ . Comparing the two results can be regarded as a high-precision test of quantum electrodynamics $^{13,22}$ .

Newton's gravitational constant,  $G$ . Of all fundamental constants of nature, the gravitational constant  $G$  is by several orders of magnitude[14] the least accurately determined one. By performing a differential measurement with a pair of atom interferometers in a gradiometer configuration (FIG. 3b), the local gravitational field generated by a well-characterized source mass can be precisely determined, and  $G$  accurately inferred[23]. Results

approaching the accuracies of state-of-the-art measurements with macroscopic test masses, mainly torsion-balance experiments $^{24-26}$ , have already been obtained and found  $G = 6.67191(99) \times 10^{-11} \mathrm{~m}^{3} \mathrm{~kg}^{-1} \mathrm{~s}^{-2}$ , with a relative uncertainty of  $150 \mathrm{ppm}^{14}$ . Significant future improvements with an atom interferometer are anticipated $^{27}$ .

# Testing the equivalence principle

The equivalence principle[28,29] states that local physical phenomena in a freely falling frame are equivalent to those in the absence of gravitational fields, provided that tidal effects can be neglected. The differential acceleration between two test masses in free fall, expressing a violation of the universality of free fall (UFF), which is a central aspect of the equivalence principle, is typically quantified by the dimensionless Eötvös parameter. This quantity corresponds to the difference in the ratios of the gravitational and inertial masses of the two objects, divided by their average. Although classical tests have reached uncertainties in the Eötvös ratio below  $10^{-14}$  no deviation from the equivalence principle has been reported so far[30-33].

Atom interferometers34-38 offer a complementary and very clean approach for

probing the equivalence principle, as the test samples are intrinsically isotopically pure and are in a well-specified spin state. This feature can be exploited to search for spin-dependent UFF violations by comparing the results for different spin polarizations. More importantly, atom interferometers provide access to atomic elements, which are technically impractical to use as macroscopic test masses. In this way, it is possible to significantly expand the parameter space, for example, with respect to atomic elements or isotopes with different neutron versus proton numbers[39].

Atom interferometry also opens up new possibilities for testing quantum aspects of the equivalence principle using atoms in superpositions of internal states[40] or with pairs of entangled atoms of different species[41]. A variation using a macroscopically delocalized coherent superposition of atomic clocks[42,43] has also been proposed for tests of the universality of the gravitational redshift.

# Dark-matter and dark-energy searches

Astrophysical and cosmological observations have established[44] that dark energy and dark matter are the dominant contributions to the average energy density of the Universe. Ordinary matter made of standard, model particles makes up only  $5\%$  of its content. However, the precise nature of dark matter and dark energy remains elusive, despite considerable efforts in observational astrophysics and experimental high-energy physics over several decades. Precision measurements based on atom interferometry and atomic clocks can make contributions in the quest to understand the nature of dark matter and dark energy.

A class of theories attempting to explain dark energy, known as chameleon models $^{45}$ , involve a light scalar field that can mediate a long-range interaction and give rise to a 'fifth force'. However, through its interaction with matter, the chameleon field acquires a much larger effective mass in regions where the matter density is not too low. This fact leads to a screening of the interaction, which can, in this way, evade tests of the equivalence principle with macroscopic masses. However, microscopic test masses, such as atoms in a vacuum chamber, should hardly be affected by the screening mechanism, as opposed to the source mass. Hence, atoms could be much more sensitive to forces mediated by chameleon fields $^{45}$ . Atom interferometric measurements have already been able to exclude large regions of the parameter space for such models $^{46,47}$ .

![](images/04a6b8e08fe13ae218d27e8b519a995e2ef1b7c44c14800fbad9aaa2a1a92c4e.jpg)  
Fig. 2 | A roadmap for the development of portable quantum sensors. The road from the first proof-of-principle laboratory demonstration of atom-interferometer gravity sensors to portable consumer devices consists of a sequence of increasingly complex scientific and technological challenges. Each step is independent of the subsequent ones, but benefits from the previous developments. Addressing each challenge opens up new application areas; hence, the emergence of practical measurement systems in this particular sequence is likely. However, many improvements and further refinements in each class of devices will happen in parallel.

Extensive searches $^{48}$  for massive dark-matter candidates known as WIMPs (weakly interacting massive particles) have not yet provided a widely accepted direct observation, spurring a growing experimental interest in exploring a wider range of dark-matter hypotheses. In this respect, the possibility that dark matter could be attributed to coherent oscillations within sub-galactic regions of ultralight scalar or pseudoscalar fields has recently been gaining increasing attention $^{49}$ . These oscillations could lead to small periodic variations in space and time of the parameters of the standard model, which could be detected in highly sensitive gravimetry measurements as a small modulation in the time of the acceleration experienced by freely falling atoms $^{50}$ . They could also produce small oscillations of the transition energies between electronic states that could be identified by comparing different atomic clocks at the same location $^{51}$  or pairs of identical atom interferometers separated by long distances but interrogated by common laser beams $^{50}$ . Experimentally, the search for dark matter and dark energy with atom interferometry is in the early stages and provides a fascinating direction for future development.

# Gravitational-wave detection

Atom interferometry offers a complementary approach[52,53] to the established laser interferometry for the detection of gravitational waves. Two atom interferometers coherently manipulated by the same light field can be interpreted as a differential phase metre tracking the distance traversed by the light field. Based on this principle, space-borne detectors[54,55] have been proposed which target a similar performance as the laser interferometer used in the Laser Interferometer Space Antenna (LISA) project[55,56].

Atom interferometers have been proposed to cover the gap in the frequency band of  $0.1 - 10\mathrm{Hz}$  between LISA and ground-based laser interferometers such as Virgo and the Advanced Laser Interferometer Gravitational Wave Observatory (AdvLIGO)[57]. Concepts for setups on Earth with a vertical[52] or horizontal[57] baseline have been discussed, with developments towards the latter geometry under way in the Matter-wave laser Interferometric Gravitation Antenna (MIGA) consortium[59].

The European Laboratory for Gravitation and Atom-Interferometric Research (ELGAR) facility proposes to design the first long-baseline infrastructure

![](images/5ec6e8d36b522a28bf269da3e7239d98ebe83ddfdc234bfc019db2805c22988a.jpg)  
Fig. 3 | Modified interferometer schemes. Differential measurements between the phase shifts in two simultaneously operated interferometers lead to common-mode suppression of many noise sources, such as vibration and laser noise. a | A four-pulse scheme creates two closed interferometers whose differential phase shift is directly related to the kinetic energy associated with the photon recoil. b | A gravity gradiometer scheme involves two atom interferometers at two different heights within the gravitational potential interrogated by the same laser beam. c | Additional laser pulses (blue arrows) increase the spacetime area of the atom interferometer, thus enhancing the sensitivity. This technique can be applied to single interferometers for inertial sensing and gravimetry and to pairs of interferometers for gradiometry measurements, such as the one shown in panel b.

![](images/70b6d74874511b431795bc37ca3120d7bfd26a108f3e2c89c2e7c7d995a7fc87.jpg)

![](images/ee5ef5724442b77da27baf4e40fec2dc3053ca4d9a346c49a5f8e070a49f6f2b.jpg)

using quantum physics to study spacetime and gravitation. With a correlated array of atom interferometers, it is possible to discriminate between gravitational-wave signals at low frequencies in the range of  $0.1 - 10\mathrm{Hz}$  and Newtonian gravitational noise from the environment[58], which allows a frequency band not covered by other gravitational-wave detectors to be addressed.

In addition to the detection of gravitational waves, this facility is expected to contribute to other studies; for example, to the monitoring of Earth's gravitational field over time and its rotation rate in three dimensions.

Increasing the measurement precision Although atom interferometers are the state of the art in determining the fine-structure constant, many of the other fundamental physics applications still require significant improvements to surpass the sensitivity achieved by other methods. In addition to scaling the sensitivity with longer interferometer times in large, atomic fountains60-64 or in space65,66, there are numerous ideas which allow many orders of magnitude improvement. For example, one approach is to increase the number of laser pulses at each interaction point (FIG. 3c), leading to large-momentum beamsplitters67,68, where a large number,  $N$ , of photon momenta are transferred, leading to an  $N$ -fold increase in sensitivity. Whereas beamsplitters with hundreds of photon recoils have been demonstrated, real sensitivity improvements have only been observed69,70 for photon exchanges of  $N \approx 30$ , because technical challenges (such as wavefront curvature70-74 and nonzero excitation probabilities) still limit the

achievable interferometer contrast. Further advances are promised by atom-number squeezing $^{74}$  and quantum non-demolition measurements $^{75}$ , which increase the signal-to-noise ratio in the interferometer readout.

Research groups worldwide are working on combining the above schemes to achieve up to billion-fold boosts in sensitivity, aiming at UFF tests below the  $10^{-15}$  level, determinations of the gravitational constant at the 1-ppm level[27,76] and gravitational-wave strain sensitivities of  $10^{-21} \mathrm{~Hz}^{-1/2}$ . These experimental efforts are accompanied by developments in the accurate modelling of atom interferometry, allowing the identification of all the relevant noise sources and systematic effects, and the design of suitable mitigation strategies. Detailed studies of the phase-shift contributions in light-pulse atom interferometers already exist, including the effects of accelerations[77], rotations, gravity gradients[78-83] and even branch-dependent forces[81]. Many of these studies take advantage of a useful decomposition of the wave-packet evolution in terms of central trajectories and centred wave packets[78,80,81,84].

A deeper theoretical understanding of atom interferometry, combined with a precise control of the relevant parameters, allows an accurate engineering of the environment[85,86]. This understanding can also be exploited to develop new techniques[87] to circumvent major limitations imposed, for example, by uncertainties in the initial position and velocity of the atomic cloud in the presence of gravity gradients. Indeed, the technique[76,87] for compensating the effects of gravity gradients enables significant breakthroughs in measurements

of the gravitational constant $^{27,76}$ ,  $G$ , and tests of the equivalence principle $^{60}$  with atom interferometry.

Most theoretical approaches to date are non-relativistic, except for phase-shift calculations of freely falling atoms relying on a semi-classical ansatz $^{88-90}$ , but a fully relativistic description of atom interferometry in curved spacetime $^{43}$  has recently been developed. This technique is particularly valuable for investigating interferometry schemes sensitive to relativistic effects.

# Absolute measurements for metrology

The international system of weights and measures as maintained and disseminated by the national metrology institutions aims at defining all SI units in terms of only a few fundamental constants/measurements<sup>91</sup>. The kilogram will no longer be defined by the respective mass prototype at the Bureau International des Poids et Mesures in Paris and its copies at other national metrology organizations but will be realized by a measurement of electromagnetic versus gravitational forces in a so-called Kibble balance<sup>92</sup>, previously referred to as a watt balance. This approach will require a local gravimeter measuring the local gravitational acceleration,  $g$ , thus providing the link between the mass of the test object and the gravitational force. For this application, it is important that the gravimeter provides an absolute measurement of the acceleration, for instance by observing the trajectory of a falling object, and not a relative measurement, such as comparing the gravitational force on a test mass with the force exerted by a spring, which might be affected by mechanical ageing.

Whereas gravity sensors based on atom interferometry are effectively measuring a free-fall trajectory and are, in principle, absolute instruments, there are significant challenges in understanding all the effects that can limit the required level of precision. One example is the crucial role of the wavefront curvature in absolute atom interferometric gravimeters when used as a metrological standard[95]. The expansion of a finite-temperature atom cloud when interrogated by a laser with even only slightly curved wavefronts leads to a shift of the measured phase due to the averaging over the extent of the cloud. Thus, wavefront curvature needs to be delicately controlled[71], and corrections determined by wavefront and temperature measurements applied[71]. Alternatively, or in addition, one can work with ultralow-temperature atomic ensembles, with a negligible expansion and, thus, atoms always exploring the same part of the wavefront, to reach ultimate absolute precision[93-95].

The advantage of atom interferometers over commercial absolute gravimeters based on the observation of the free-fall trajectory of corner cubes with a laser interferometer lies in reduced mechanical wear. This provides the capability to run continuous measurements over long periods of time, as required by metrology service providers.

# Transportability for geophysics

Absolute measurements of gravity are also important for geophysics research, for example in monitoring continental uplift[96,97] or underground water movements[98,99]. In this application, measurements are taken over long periods of time, potentially returning to the same location after some time, and a drift of the measurement instrument could result in false interpretations of the data. In addition, field trials will require transportability with fast setup times at new locations.

These requirements have been met by some of the first commercial atom-interferometer solutions $^{15}$ , which have been tested in continuous operation over one month $^{16}$  and found to have a long-term stability of better than  $10\mathrm{nm s}^{-2}$ , similar to commercial falling corner-cube instruments. An advantage of atom interferometers when compared to their falling corner-cube counterparts is that the ultralight atomic test masses do not cause any noticeable impact when they hit the bottom of the apparatus. This impact requires falling corner-cube instruments to be operated on specially reinforced foundations to achieve full precision, which is not necessary for atom interferometers.

# Autonomous operation for space

Operating atomic sensors in space brings the possibility to reach long interrogation times, large interferometer areas and, ultimately, very high precision $^{100}$ . However, with the cost of increased technical challenges in terms of robustness, size, weight and power (SWAP) and, in particular, the autonomy of operation. SWAP drive the cost of space missions; hence, this application requires detailed system analysis and optimization of the instrument to reduce these factors. In addition, there are very limited options for human interference, requiring autonomous operation with built-in fault diagnostics and recovery routines. Solutions to these problems provide an important step towards practical space-based and ground-based applications.

Preparatory atom-interferometer experiments have been pursued for over 15 years. Atom interferometers operated on parabolic flights have been addressing robustness challenges, pioneering signal recovery by correlation with additional sensors $^{86}$ . They also demonstrated a test of the UFF with a dual-species Rb–K interferometer in flight in both standard gravity and free-fall phases $^{77}$ . The Quantengase Unter Schwerelosingkeit (QUANTUS) collaboration achieved significant steps forward towards autonomous operation and reduced SWAP. It performed drop-tower experiments with Bose–Einstein condensates as ultracold probe samples $^{101,102}$  and realized a Bragg interferometer $^{97}$  with atoms at an effective temperature of  $1\mathrm{nK}$ . The first experiment utilizing Bose–Einstein condensate in space $^{103}$  was performed on board a sounding rocket (FIG. 4a) during  $6\mathrm{min}$  of microgravity $^{104}$ . In microgravity, long interrogation times, large interferometer areas and, ultimately, very high precision could be achievable, but one of the key challenges is reaching ultralow temperatures of the atomic ensemble to overcome the limitations linked to the expansion, such as the gravity gradient coupling across the ensemble.

In 2018, NASA launched an experiment on the International Space Station called the Cold Atom Laboratory (CAL) $^{105}$ , which produced a Bose-Einstein condensate a few months after installation. This provides another example of technology developments towards robustness and SWAP reduction. The challenge to drive SWAP into the realm of small satellite missions has been taken on by the Cold Atom Space Payload (CASPA) collaboration

demonstrator (FIG. 4b). This instrument aims to create  $10^{7}$  laser-cooled atoms in a full payload of 4l and  $4\mathrm{kg}$  weight at  $40\mathrm{W}$  of power consumption, including avionics, and is currently preparing for vibration testing before evaluating long-term autonomous operation and flight preparation[106].

These activities aimed at developing atom interferometers operating in space provide an important test bed for fundamental physics applications, such as testing the UFF to  $10^{-15}$  and beyond[65,66], but also open up new Earth-observation applications through gravity-field monitoring for climate and hydrology[107-110].

# Robustness for civil engineering

The key obstacle in entering the market of geosurveys in civil engineering is ensuring robustness to environmental effects such as ground vibrations and tilt, which can severely limit the speed of surveys<sup>111</sup>. A spring-mass gravimeter takes up to 10 min per measurement point, translating to over a month for a hectare. This is due to the need to align the sensor to better than 1/1,000th of a degree in the direction of gravity and integrate ground vibrations, which are 10-100 times larger than the signals of interest.

Atom interferometers overcome these limitations by operating in gravity gradient mode; that is, interrogating two vertically separated atomic ensembles with the same laser beam (FIG. 3b). This arrangement completely suppresses ground vibrations and reduces the alignment requirements to the degree level[111-114]. A sensor able to measure gravity gradients corresponding to  $1\mathrm{ng}\mathrm{s}^{-1}$  over a 1-m distance, a precision already achieved in the laboratory, promises to reduce measurement times in civil-engineering field surveys by over a factor of 100, creating a commercially attractive option with great economic potential.

Unknown underground conditions present the largest single risk in infrastructure projects and cause significant delays and cost overruns, which, as a study in the Netherlands suggests[114], might reach half a percent of the gross domestic product of the country. Although only excavation can provide full information about the underground, gravity signatures offer information complementary to standard technologies such as ground-penetrating radar, magnetometry, electric resistivity and acoustic measurements[115]. Most importantly, gravity signatures are not shielded by anything and, thus, in principle, have no depth limitation[111], opening up the potential to detect sinkholes,

mineshafts and underground tanks, which pose major challenges to housing, road, rail and development projects on brownfield land.

A gravity gradiometer was designed by the University of Birmingham for civil-engineering applications (FIG. 4c). The device consists of two parts: a control package and a sensor head connected by a cord,

which allows the sensor head to move easily over a survey site[116]. The device has been demonstrated outdoors in temperature conditions ranging from  $0^{\circ}\mathrm{C}$  to  $30^{\circ}\mathrm{C}$ , on road surfaces around construction sites. The aim for this device is to realize a ten-fold reduction in measurement times compared to classical geophysics equipment[117].

![](images/cbf5c915ad43e1024c286489af4ddb9a9c1b2a8b9d3ee2b0e49e7fbead186306.jpg)

![](images/550945a0cc5ab1ddc255dfed06da205279a7a3d4c2353dd5f2e2c95c39996f93.jpg)

![](images/f621a2d92c87d0b9cde52c2ed70a9a9defa714b1b2e2d2c6d592163d048ef065.jpg)

![](images/a60ac704358d6e5f0693038cc9b4f9dde07f50f6d36acdaa50d91cf2d2ee2095.jpg)

![](images/a997cd4a9edcc22e3fb402ac2cca3744c9cf0642d392424e3ad6ebb720e8d5de.jpg)  
Fig. 4 | Examples of portable atom interferometers. a | The MAIUS rocket $^{99}$ , with a payload containing an atom chip on which the first Bose-Einstein condensate was created in space. b | A cold-atom payload $^{103}$  designed to fit onto a cube sat (Cold Atom Space Payload (CASPA) project, Innovate UK 102805). c | A cold-atom gravity gradiometer $^{113}$  developed by the University of Birmingham for civil-engineering applications. d | An airborne matter-wave accelerometer operating on a plane $^{81}$  carrying out parabolic flights with a classical vibration sensor to remove the ambiguity in the phase of the interferometric fringes. e | Cold-atom device for an unmanned aerial vehicle $^{116}$ . f | Cold-atom gravimeter $^{119}$  together with a spring gravimeter installed on a gyrostabilized platform on board the Beautemps-Beaupré ship. MOT, magneto-optical trap. Panel a is reprinted from REF. $^{104}$ , Springer Nature Limited. Panel b CASPA project, Innovate UK 102805, image courtesy of Teledyne e2v. Panel c image courtesy of the Defence Science and Technology Laboratory (DSTL). Panel f is reprinted from REF. $^{122}$ , CC-BY-4.0 https://creativecommons.org/licenses/by/4.0/.

![](images/e91f054988b8dfee7cd0cc3ff203464278f4662a43b5f819df03a6148b3ec47f.jpg)

Gravity measurements are an essential part of oil exploration and often used in conjunction with other magnetic and seismic measurements[118]. Gravity surveys are frequently conducted by aircraft to cover large areas. By combining gravity and magnetic data, it is possible to gain information about the density and the total magnetization of the rock composition. Each measurement provides an independent picture of the subsurface and is responsive to horizontal variations in rock properties. Gravity and magnetic information is best suited for detecting steep discontinuities such as faults.

To be used in oil and mineral exploration, atom-based gravity sensors need to operate reliably on moving platforms, such as drones or planes. In contrast to established methods, atom interferometers promise very low nonlinearity in the relation between readout and acceleration (linear scale factor), even in the presence of large acceleration of the aircraft. However, the interferometer output varies sinusoidally with the acceleration, leading to an ambiguity whenever the acceleration changes during the interferometer sequence, leading to more than one sinusoidal oscillation of the interferometer output. This ambiguity leads to a limited dynamic range of the instrument. One solution is to complement the atom interferometer with a classical accelerometer. This technique was used to measure the acceleration on board an aircraft with a sensitivity of  $2 \times 10^{-4} \mathrm{~ms}^{-2} / \sqrt{\mathrm{Hz}}$ . The resolution of the sensor in FIG. 4d enabled to determine accelerations more than 100 times below the vibration level found on the plane.

Cold-atom devices can provide alternative sensors with vibration suppression, for instance by using gravity-gradiometer schemes. Such methods are already used in oil and minerals prospecting, but atom-interferometer-based technologies are expected to reduce the SWAP and cost of the instruments, and eventually offer the ability to operate under larger accelerations and rotations, allowing faster surveys. The first prototypes $^{119}$  are under development, for example, a system involving the magneto-optical trapping of atoms within a total system payload of  $6.56\mathrm{kg}$  and volume of 131 (FIG. 4e).

# High bandwidth for navigation

Quantum sensors intrinsically provide low bias and high stability, which opens the potential to enable long-term inertial navigation, which is currently not possible

with classical sensors, as these suffer from long-term drift. However, navigation requires acceleration sensors with fast measurement rates of several  $100\mathrm{Hz}$  allowing for operation on highly mobile platforms. This high-bandwidth operation, while maintaining high precision, is a significant challenge for quantum sensors.

Hybrid approaches use a quantum sensor in combination with a conventional one, for instance by providing a correction to the drift of a commercial inertial sensor. Recent developments[120] have shown that hybridization can achieve continuous measurements of acceleration at  $400\mathrm{-Hz}$  bandwidth while showing no visible drift for 11-h periods.

Another approach to increasing bandwidth for navigation is to improve the measurement bandwidth of quantum sensors. Bandwidths in excess of  $100\mathrm{Hz}$  have been demonstrated while realizing sensitivities at the  $\mu \mathrm{g} / \sqrt{\mathrm{Hz}}$  level for acceleration and the  $(\mu \mathrm{rad}s^{-1}) / \sqrt{\mathrm{Hz}}$  level for rotation[12].

In addition to the sensing performance, it is also necessary to address cross-coupling challenges, such as rotation leading to a false accelerometer response. These challenges are associated with the platform dynamics and are highly dependent upon the platform of interest. For example, in marine navigation, sea movement can create a wide range of tilt noise, which can be overcome through the integration of inertial-stabilization platforms and the application of hybrid sensing[121]. Ship-borne measurements at the milligal level have been demonstrated with atom interferometry[122] (FIG. 4f).

# Conclusion

Atom interferometers are a maturing quantum technology that has demonstrated the highest sensitivity in gravity measurements. Instruments designed for tests of fundamental physics provided constraints to extensions of the standard model of particle physics. Portable and robust devices have already achieved unprecedented measurement speed in geophysics research and are on the way to technological applications in other fields.

The portability of atomic sensors imposes SWAP constraints and commercial use also involves cost issues. Strategies to overcome these problems and limitations include 3D printing[123-125] to minimize the use of mechanical mounts, robust and compact laser systems[126-129] to decrease the number of lasers needed in atom interferometers and compact magneto-optical traps[103,117,126-133] operating with just a single input beam

to reduce the space required by optical interfaces. However, a genuine hand-held product will only become available once an integration similar to micromechanical devices is achieved. The feasibility of such an approach has been demonstrated by the chip-scale atomic clock[134,135]. Significant challenges need to be overcome in order to miniaturize atom interferometers in a similar way, but promising initiatives are under way in several laboratories around the world[136-139].

Kai Bongs $^{1*}$ , Michael Holynski $^{1}$ , Jamie Vovrosh $^{1}$ , Philippe Bouyer $^{2}$ , Gabriel Condon $^{3}$ , Ernst Rasel $^{4}$ , Christian Schubert $^{4}$ , Wolfgang P. Schleich $^{5,6}$  and Albert Roura $^{5,7}$

<sup>1</sup>Midlands Ultracold Atom Research Centre (MUARC), University of Birmingham, Birmingham, UK.

$^{2}$ CNRS, Institut d'Optique Graduate School (IOGS), University of Bordeaux, Talence Cedex, France.

3Muquans, Talence Cedex, France.

$^{4}$ Institute of Quantum Optics, Leibniz University Hannover, Hannover, Germany.

$^{5}$ Institute of Quantum Physics and Center for Integrated Quantum Science and Technology (IQST), Ulm University, Ulm, Germany.

$^{6}$ Institute for Quantum Science and Engineering (IQSE), Texas A&M University, College Station, TX, USA.

7German Aerospace Center (DLR), Cologne, Germany.

$^{*}e$  -mail: k.bongs@bham.ac.uk

https://doi.org/10.1038/s42254-019-0117-4

# Published online 28 October 2019

1. De Broglie, L. Recherches sur la theorie des quanta [French]. Thesis, Univ. Paris (1924). English translation: J. W. Haslett. Am. J. Phys. 40, 1315-1320 (1972).  
2. Mollenstedt, G. & Duker, H. Observations and measurements of biprism interference with electron waves. Z. Phys. 145, 377-397 (1956).  
3. Jönsson, C. Electron diffraction at multiple slits. Am. J. Phys. 42, 4-11 (1974).  
4. Rauch, H. & Werner, S. A. in Neutron Interferometry: Lessons in Experimental Quantum Mechanics, Wave-Particle Duality, and Entanglement 2nd edn (Oxford Univ. Press, 2015).  
5. Rauch, H., Treimer, W. & Bonse, U. Test of a single crystal neutron interferometer. Phys. Lett. A 47, 369-371 (1974).  
6. Keith, D. W., Ekstrom, C. R., Turchette, Q. A. & Pritchard, D. E. An interferometer for atoms. Phys. Rev. Lett. 66, 2693-2696 (1991).  
7. Carnal, O. & Mlynek, J. Young's double-slit experiment with atoms: a simple atom interferometer. Phys. Rev. Lett. 66, 2689-2692 (1991).  
8. Kasevich, M. & Chu, S. Atomic interferometry using stimulated Raman transitions. Phys. Rev. Lett. 67, 181-184 (1991).  
9. Riehle, F., Kisters, T., Witte, A., Helmcke, J. & Borde, C. J. Optical Ramsey spectroscopy in a rotating frame: Sagnac effect in a matter-wave interferometer. Phys. Rev. Lett. 67, 177-180 (1991).  
10. Hackermüller, L. et al. Wave nature of biomolecules and fluorfullerenes. Phys. Rev. Lett. 91, 090408 (2003).  
11. Linskens, A. F., Holleman, I., Dam, N. & Reuss, J. Two-photon Rabi oscillations. Phys. Rev. A 54, 4854-4862 (1996).  
12. Kasevich, M. & Chu, S. Measurement of the gravitational acceleration of an atom with a light-pulse atom interferometer. Appl. Phys. B 54, 321-332 (1992).  
13. Richard, H. P., Yu, C., Zhong, W., Estey, B. & Müller, H. Measurement of the fine-structure constant as a test of the standard model. Science 360, 191-195 (2018).  
14. Rosi, G., Sorrentino, F., Cacciapuoti, L., Prevedelli, M. & Tino, G. M. Precision measurement of the Newtonian gravitational constant using cold atoms. Nature 510, 518-521 (2014).

15. Gillot, P., Cheng, B., Imanaliev, A., Merlet, S. & Pereira Dos Santos, F. The LNE-SYRTE cold atom gravimeter. IEEE https://ieeexplore.ieee.org/document/7477832 (2016).  
16. Menoret, V. et al. Gravity measurements below  $10^{-9}$  g with a transportable absolute quantum gravimeter. Sci. Rep. 8, 12300 (2018).  
17. Weiss, D. S., Young, B. C. & Chu, S. Precision measurement of the photon recoil of an atom using atomic interferometry. Phys. Rev. Lett. 70, 2706-2709 (1993).  
18. Bureau International des Poids et Mesures. Resolution 1 of the 26th meeting of the General Conference on Weights and Measures (BIPM, 2018).  
19. Andreas, B. et al. Determination of the Avogadro constant by counting the atoms in a  $^{28}\mathrm{Si}$  crystal. Phys. Rev. Lett. 106, 030801 (2011).  
20. Bouchendira, R., Clade, P., Guellati-Khelila, S., Nez, F. & Biraben, F. New determination of the fine structure constant and test of the quantum electrodynamics. Phys. Rev. Lett. 106, 080801 (2011).  
21. Hanneke, D., Fogwell, S. & Gabrielse, G. New measurement of the electron magnetic moment and the fine structure constant. Phys. Rev. Lett. 100, 120801 (2008).  
22. Bouchendira, R., Clade, P., Guellati-Khelifa, S., Nez, F. & Biraben, F. State of the art in the determination of the fine structure constant: test of quantum electrodynamics and determination of  $h / m_{\mathrm{u}}$ . Ann. Phys. 525, 484-492 (2013).  
23. Fixler, J. B., Foster, G. T., McGuirk, J. M. & Kasevich, M. A. Atom interferometer measurement of the Newtonian constant of gravity. Science 315, 74-77 (2007).  
24. Gundlach, J. H. & Merkowitz, S. M. Measurement of Newton's constant using a torsion balance with angular acceleration feedback. Phys. Rev. Lett. 85, 2869-2872 (2000).  
25. Quinn, T.J., Speake, C.C. & Davis, R.S. Novel torsion balance for the measurement of the Newtonian gravitational constant. Metrologia 34, 245-249 (1997).  
26. Li, Q. et al. Measurements of the gravitational constant using two independent methods. Nature 560, 582-588 (2018).  
27. Rosi, G. A proposed atom interferometry determination of G at  $10^{-5}$  using a cold atomic fountain. Metrologia 55, 50-55 (2017).  
28. Schiff, L. I. On experimental tests of the general theory of relativity. Am. J. Phys. 28, 340-343 (1960).  
29. Will, C. M. The confrontation between general relativity and experiment. Living Rev. Relativ. 17, 4-115 (2014).  
30. Hofmann, F. & Müller, J. Relativistic tests with lunar laser ranging. Class. Quantum Gravity 35, 035015 (2018).  
31. Schlamminger, S., Choi, K. Y., Wagner, T. A., Gundlach, J. H. & Adelberger, E. G. Test of the equivalence principle using a rotating torsion balance. Phys. Rev. Lett. 100, 041101 (2007).  
32. Niebauer, T. M., McHugh, M. P. & Faller, J. E. Galilean test for the fifth force. Phys. Rev. Lett. 59, 609-612 (1987).  
33. Touboul, P. et al. MICROSCOPE mission: first results of a space test of the equivalence principle.Phys.Rev. Lett.119,231101 (2017).  
34. Merlet, S. et al. Comparison between two mobile absolute gravimeters: optical versus atomic interferometers. Metrologica 47, L9-L11 (2010).  
35. Zhou, L. et al. Test of equivalence principle at  $10^{-8}$  level by a dual-species double-diffraction Raman atom interferometer. Phys. Rev. Lett. 115, 013004 (2015).  
36. Fray, S., Diez, C. A., Hansch, T. W. & Weitz, M. Atomic interferometer with amplitude gratings of light and its applications to atom based tests of the equivalence principle. Phys. Rev. Lett. 93, 240404 (2004).  
37. Bonnin, A., Zahzam, N., Bidel, Y. & Bresson, A. Simultaneous dual-species matter-wave accelerometer. Phys. Rev. A 88, 045615 (2013).  
38. Tarallo, M. G. et al. Test of Einstein equivalence principle for O-spin and half-integer-spin atoms: search for spin-gravity coupling effects. Phys. Rev. Lett. 113, 023005 (2014).  
39. Schlippert, D. et al. Quantum test of the universality of free fall. Phys. Rev. Lett. 112, 203002 (2014).  
40. Rosi, G. et al. Quantum test of the equivalence principle for atoms in coherent superposition of internal energy states. Nat. Commun. 8, 15529 (2017).  
41. Geiger, R. & Trupke, M. Proposal for a quantum test of the weak equivalence principle with entangled atomic species. Phys. Rev. Lett. 120, 043602 (2018).

42. Zych, M., Costa, F., Pikovski, I. & Brukner, C. Quantum interferometric visibility as a witness of general relativistic proper time. Nat. Commun. 2, 505 (2011).  
43. Roura, A. Gravitational redshift in quantum-clock interferometry. Preprint at arXiv https://arxiv.org/abs/1810.06744 (2018).  
44. Bertone, G., Hooper, D. & Silk, J. Particle dark matter: evidence, candidates and constraints. Phys. Rep. 405, 279-390 (2005).  
45. Elder, B. et al. Chameleon dark energy and atom interferometry. Phys. Rev. D. 94, 044051 (2016).  
46. Hamilton, P. et al. Atom-interferometry constraints on dark energy. Science 349, 849-851 (2015).  
47. Jaffe, M. et al. Testing sub-gravitational forces on atoms from a miniature in-vacuum source mass. Nat. Phys. 13, 938-942 (2017).  
48. Strigari, L. E. Galactic searches for dark matter. Phys. Rep. 531, 1-88 (2013).  
49. Magana, J. & Matos, T. A brief review of the scalar field dark matter model. J. Phys. Conf. Ser. 378, 012012 (2012).  
50. Arvanitaki, A., Graham, P.W., Hogan, J.M., Rajendran, S. & Tilburg, K.V. Search for light scalar dark matter with atomic gravitational wave detectors. Phys. Rev. D. 97, 075020 (2018).  
51. Hees, A., Guena, J., Abgrall, M., Bize, S. & Wolf, P. Searching for an oscillating massive scalar field as a dark matter candidate using atomic hyperfine frequency comparisons. Phys. Rev. Lett. 117, 061301 (2016).  
52. Dimopoulos, S., Graham, P. W., Hogan, J. M., Kasevich, M. A. & Rajendran, S. Atomic gravitational wave interferometric sensor. Phys. Rev. D 78, 122002 (2008).  
53. Hogan, J. M. & Kasevich, M. A. Atom-interferometric gravitational-wave detection using heterodyne laser links. Phys. Rev. A 94, 033652 (2016).  
54. Hogan, J. M. et al. An atomic gravitational wave interferometric sensor in low earth orbit (AGIS-LEO). Gen. Relativ. Gravit. 43, 1953-2009 (2009).  
55. Amaro-Seane, P. et al. Low-frequency gravitational-wave science with eLISA/NGO. Class. Quantum Gravity 29, 124016 (2012).  
56. Amaro-Seoane, P. et al. The gravitational universe. Preprint at arXiv https://arxiv.org/abs/1305.5720 (2013).  
57. Abbott, B. P. et al. Observation of gravitational waves from a binary black hole merger. Phys. Rev. Lett. 116, 061102 (2016).  
58. Chaibi, W. et al. Low frequency gravitational wave detection with ground-based atom interferometer arrays. Phys. Rev. D, 93, 021101(R) (2016).  
59. Canuel, B. et al. Exploring gravity with the MIGA large scale atom interferometer. Sci. Rep. 8, 14064 (2018).  
60. Overstreet, C. et al. Effective inertial frame in an atom interferometric test of the equivalence principle. Phys. Rev. Lett. 120, 183604 (2018).  
61. Hartwig, J. et al. Testing the universality of free fall with rubidium and ytterbium in a very large baseline atom interferometer. New J. Phys. 17, 035011 (2015).  
62. Dimopoulos, S., Graham, P. W., Hogan, J. M. & Kasevich, M. A. Testing general relativity with atom interferometry. Phys. Rev. Lett. 98, 111102 (2007).  
63. Dickerson, S. M., Hogan, J. M., Sugarbaker, A., Johnson, D. M. S. & Kasevich, M. A. Multiaxis inertial sensing with long-time point source atom interferometry. Phys. Rev. Lett. 111, 083001 (2013).  
64. Zhou, L. et al. Development of an atom gravimeter and status of the 10-meter atom interferometer for precision gravity measurement. Gen. Relativ. Gravit. 43, 1931-1942 (2011).  
65. Aguilera, D. N., et al. STE-QUEST-test of the universality of free fall using cold atom interferometry. Class. Quantum Gravity 11, 115010 (2015).  
66. Williams, J. R., Chiw, S. W., Yu, N. & Müller, H. Quantum test of the equivalence principle and space-time aboard the International Space Station. New J. Phys. 18, 025018 (2016).  
67. Clade, P., Guellati-Khelifa, S., Nez, F. & Biraben, F. Large momentum beam splitter using Bloch oscillations. Phys. Rev. Lett. 102, 240402 (2009).  
68. Muller, H., Chiow, S. W., Long, Q., Herrmann, S. & Chu, S. Atom interferometry with up to 24-photon-momentum-transfer beam splitters. Phys. Rev. Lett. 100, 180405 (2008).  
69. Kovachy, T. et al. Quantum superposition at the half-metre scale. Nature 528, 530 (2015).  
70. Asenbaum, P. et al. Phase shift in an atom interferometer due to spacetime curvature across its wave function. Phys. Rev. Lett. 118, 183602 (2017).

71. Schkolnik, V., Leykauf, B., Hauth, M., Freier, C. & Peters, A. The effect of wavefront aberrations in atom interferometry. Appl. Phys. B 120, 311-316 (2015).  
72. Trimeche, A., Langlois, M., Merlet, S. & Pereira Dos Santos, F. Active control of laser wavefronts in atom interferometers. Phys. Rev. Appl. 7, 034016 (2017).  
73. Langlois M., Trimeche A., Merlet S. & Pereira Dos Santos F. Correction of laser wavefronts in an atom interferometer with a deformable mirror (IEEE, 2017).  
74. Li, W., Tuchman, A. K., Chien, H. C. & Kasevich, M. A. Extended coherence time with atom-number squeezed states. Phys. Rev. Lett. 98, 040402 [2007].  
75. Kuzmich, A., Bigelow, N. P. & Mandel, L. Atomic quantum non-demolition measurements and squeezing. Europhys. Lett. 42, 481-486 (1998)  
76. D'Amico, G. et al. Canceling the gravity gradient phase shift in atom interferometry. Phys. Rev. Lett. 119, 253201 (2017).  
77. Barrett, B. et al. Dual matter-wave inertial sensors in weightlessness. Nat. Commun. 7, 13786 (2016).  
78. Antoine, C. & Borde, C. J. Quantum theory of atomic clocks and gravito-inertial sensors: an update. J. Opt. B Quantum Semiclass. Opt. 5, S199 (2003).  
79. Bongs, K., Launay, R. & Kasevich, M. A. High-order inertial phase shifts for time-domain atom interferometers. Appl. Phys. B 84, 599-602 (2006).  
80. Hogan, J. M., Johnson, D. M. S. & Kasevich, M. A. in Proceedings of the International Summer School of Physics "Enrico Fermi" on Atom Optics and Space Physics (eds Arimondo, E., Ertmer, W., Rasel, E. M. & Schleich, W. P.) (IOS, 2009).  
81. Roura, A., Zeller, W. & Schleich, W. P. Overcoming loss of contrast in atom interferometry due to gravity gradients. New J. Phys. 16, 123012 (2014).  
82. Kleinert, S., Kajari, E., Roura, A. & Schleich, W. P. Representation-free description of light-pulse atom interferometry including non-inertial effects. Phys. Rep. 605, 1-50 (2015).  
83. Audretsch, J. & Marzlin, K. Atom interferometry with arbitrary laser configurations: exact phase shift for potentials including inertia and gravitation. J. Phys. II 4, 2073-2087 (1994).  
84. Borde, C. J. in Les Houches Lectures, Session LIII, 1990: Fundamental Systems in Quantum Optics (eds Dalibard, J. M., Raimond, J. & Zinn-Justin, J.) (Elsevier, 1992).  
85. Chiow, S. W., Williams, J. R., Yu, N. & Muller, H. Gravity-gradient suppression in spaceborne atomic tests of the equivalence principle. Phys. Rev. A 95, 021603(R) (2017).  
86. Geiger, R. et al. Detecting inertial effects with airborne matter-wave interferometry. Nat. Commun. 2, 474 (2011).  
87. Roura, A. Circumventing Heisenberg's uncertainty principle in atom interferometry tests of the equivalence principle. Phys. Rev. Lett. 118, 160401 (2017).  
88. Stodolsky, L. Matter and light wave interferometry in gravitational fields. Gen. Relativ. Gravit. 11, 391-405 (1979).  
89. Dimopoulos, S., Graham, P.W., Hogan, J.M. & Kasevich, M.A. General relativistic effects in atom interferometry. Phys. Rev. D 78, 042003 (2008).  
90. Jaekel, M. T., Lamine, B. & Reynaud, S. Phases and relativity in atomic gravimetry. Gen. Relativ. Gravit. 30, 065006 (2013).  
91. Stock, M. Watt balance experiments for the determination of the Planck constant and the redefinition of the kilogram. Metrologia 50, 3936-3953 (2013).  
92. Geneves, G. et al. The BNM Watt balance project. IEEE Trans. Instrum. Meas. 2, 850-853 (2005).  
93. Karcher, R., Imanaliev, A., Merlet, S. & Pereira Dos Santos, F. Improving the accuracy of atom interferometers with ultracold sources. New J. Phys. 20, 113041 (2018).  
94. Niebauer, T. M., Sasagawa, G. S., Faller, J. E., Hilt, R. & Klopping, F. A new generation of absolute gravimeters. Metrologia 32, 159-180 (1995).  
95. Louchet-Chauvet, A. et al. The influence of transverse motion within an atomic gravimeter. New J. Phys. 13, 065025 (2011).  
96. Djamour, Y. et al. GPS and gravity constraints on continental deformation in the Alborz mountain range, Iran. Geophys. J. Int. 183, 1287-1301 (2010).  
97. Olsson, P., Milne, G., Scherneck, H. & Aggren, J. The relation between gravity rate of change and

vertical displacement in previously glaciated areas. J. Geodynamics 83, 76-84 (2015).  
98. Andersen, O. B. & Hinderer, J. Global inter-annual gravity changes from GRACE: Early results. Geophys. Res. Lett. 32, L01402 (2005).  
99. Jacob, Th. et al. Absolute gravity monitoring of water storage variation in a karst aquifer on the Larzac Plateau (Southern France). J. Hydrol. 359, 105-117 (2008).  
100. Le Coq, Y., Retter, J. A., Richard, S., Aspect, A. & Bouyer, P. Coherent matter wave inertial sensors for precision measurements in space. Appl. Phys. B 84, 627-632 (2006).  
101. van Zoest, T. et al. Bose-Einstein condensation in microgravity. Science 328, 1540-1543 (2010).  
102. Muntinga, H. et al. Interferometry with Bose-Einstein condensates in microgravity. Phys. Rev. Lett. 110, 093602 (2013).  
103. Rudolph, J. et al. A high-flux BEC source for mobile atom interferometers. New J. Phys. 17, 065001 (2015).  
104. Becker, D. et al. Space-borne Bose-Einstein condensation for precision interferometry. Nature 562, 391-395 (2018).  
105. Elliott, E. R., Krutzik, M. C., Williams, J. R., Thompson, R. J. & Aveline, D. C. NASA's Cold Atom Lab (CAL): system development and ground test status. NPJ Microgravity 4, 16 (2018).  
106. Devani, D. et al. Gravity sensing: in-orbit demonstration of a cold atom trap onboard a 6U CubeSat. 4S Symp. (2018).  
107. Tino, G. M. et al. Precision gravity tests with atom interferometry in space. Nucl. Phys. B 234, 243-244 (2013).  
108. Chiow, S., Williams, J. R. & Yu, N. Laser-ranging long-baseline differential atom interferometers for space. Phys. Rev. A 92, 063613 (2015).  
109. Carraz, O., Siemes, C., Massotti, L., Haagmans, R. & Silvestrin, P. A spaceborne gravity gradiometer concept based on cold atom interferometers for measuring Earth's gravity field. Microgravity Sci. Technol. 26, 139-145 (2014).  
110. Douch, K., Wu, H., Schubert, C., Muller, J. & Pereira Dos Santos, F. Simulation-based evaluation of a cold atom interferometry gradiometer concept for gravity field recovery. Adv. Space Res. 61, 1307-1323 (2018).  
111. Boddie, D., Metje, N. & Tuckwell, G. Capability assessment and challenges for quantum technology gravity sensors for near surface terrestrial geophysical surveying. J. Appl. Geophys. 146, 149-159 (2017).  
112. McGuirk, J. M., Foster, G. T., Fixler, J. B., Snadden, M. J. & Kasevich, M. A. Sensitive absolute-gravity gradiometry using atom interferometry. Phys. Rev. A 65, 033608 (2002).  
113. Snadden, M. J., McGuirk, J. M., Bouyer, P., Haritos, K. G. & Kasevich, M. A. Measurement of the Earth's gravity gradient with an atom interferometer-based gravity gradiometer. Phys. Rev. Lett. 81, 971-974 (1998).  
114. van Staveren, M. Risk, Innovation and Change (Legatron Electronic Publishing, 2009).  
115. Metje, N., Chapman, D. N., Rogers, C. D. F. & Bongs, K. Seeing through the ground: the potential of gravity gradient as a complementary technology. Adv. Civ. Eng. 2011, 1-9 (2011).  
116. Lamb, A. Cold Atom Gravity Gradiometer for Field Applications. Thesis, Univ. Birmingham (2019).  
117. Hinton, A. et al. A portable magneto-optical trap with prospects for atom interferometry in civil engineering. Philos. Trans. A Math. Phys. Eng. Sci. 375, 20160238 (2017).  
118. Nettleton, L. L. Gravity and Magnetics in Oil Prospecting (McGraw-Hill, 1976).  
119. Earl, L. Developing Cold Atoms Systems for Novel and Transportable Platforms. Thesis, Univ. Birmingham (2019).  
120. Cheiney, P. et al. Navigation-compatible hybrid quantum accelerometer using a Kalman filter. Phys. Rev. A 10, 034030 (2018).  
121. Rakholia, A. V., McGuinness, H. J. & Biedermann, G. W. Dual-axis high-data-rate atom interferometer via cold ensemble exchange. Phys. Rev. Appl. 2, 054012 (2014).  
122. Bidel, Y. et al. Absolute marine gravimetry with matter-wave interferometry. Nat. Commun. 9, 627 (2018).  
123. Vovrosh, J. et al. Additive manufacturing of magnetic shielding and ultra-high vacuum flange for cold atom sensors. Sci. Rep. 8, 2023 (2018).  
124. Saint, R. et al. 3D-printed components for quantum devices. Sci. Rep. 8, 8368 (2018).

125. Norrgard, E. B. et al. Note: A 3D-printed alkali metal dispenser. Rev. Sci. Instrum. 89, 056101 (2018).  
126. Lévêque, T., Antoni-Micollier, L., Faure, B. & Berthon, J. A laser setup for rubidium cooling dedicated to space applications. Appl. Phys. B 116, 997-1004 (2014).  
127. Theron, F. et al. Narrow linewidth single laser source system for onboard atom interferometry. Appl. Phys. B 118, 1-5 (2015).  
128. Carraz, O. et al. Compact and robust laser system for onboard atom interferometry. Appl. Phys. B 97, 405-411 (2009).  
129. Zhu, L. et al. Application of optical single-sideband laser in Raman atom interferometry. Opt. Express 26, 6542-6553 (2018).  
130. Lee, K. I., Kim, J. A., Noh, H. R. & Jhe, W. Single-beam atom trap in a pyramidal and conical hollow mirror. Opt. Lett. 21, 1177-1179 (1996).  
131. Pollock, S., Cotter, J. P., Laliotis, A. & Hinds, E. A. Integrated magneto-optical traps on a chip using silicon pyramid structures. Opt. Express 17, 14109-14114 (2009).  
132. Abend, S., et al. Atom-chip fountain gravimeter. Phys. Rev. Lett. 117, 203003 (2016).  
133. Bodart, Q. et al. A cold atom pyramidal gravimeter with a single laser beam. Appl. Phys. Lett. 96, 134101 (2010).  
134. Knappe, S. et al. A chip-scale atomic clock based on  $^{87}\mathrm{Rb}$  with improved frequency stability. Opt. Express 13, 1249-1253 (2005).  
135. Knappe, S. et al. Atomic vapor cells for chip-scale atomic clocks with improved long-term frequency stability. Opt. Lett. 30, 2351-2353 (2005).  
136. Rushton, J. A., Aldous, M. & Himsworth, M. D. Contributed review: The feasibility of a fully miniaturized magneto-optical trap for portable

ultracold quantum technology. Rev. Sci. Inst. 85, 121501 (2014).  
137. Kitching, J. Chip-scale atomic devices. Appl. Phys. Rev. 5, 031302 (2018).  
138. Riedl, S., Hoth, G. W., Pelle, B., Kitching, J. & Donley, E. A. Compact atom-interferometer gyroscope based on an expanding ball of atoms. J. Phys. Conf. Ser. 723, 012058 (2016).  
139. Gallacher, K. et al. Integrated DFB lasers on  $\mathrm{Si}_3\mathrm{N}_4$  photonic platform for chip-scale atomic systems. OSA Tech. Digest https://doi.org/10.1364/CLEO_SI.2019.STu4O.7 (2019).

# Acknowledgements

The authors thank our co-workers and collaborators for their long-term efforts and their support. Moreover, we have benefited enormously from many discussions with our colleagues who share our love of this field. K.B., M.H. and J.V. acknowledge funding from the Engineering and Physical Sciences Research Council (EPSRC) through grants EP/M013294 (UK National Quantum Technology Hub for Sensors and Metrology) and EP/R002525/1 (CASA), the Defence Science and Technology Laboratory (DSTL) through contract DSTLX-1000095040 and Innovate UK through the Gravity Pioneer grant 104613. P.B. and G.C. acknowledge funding from Agence Nationale de la Recherche and the Délégation Générale de l'Armement under grant "HYBRIDQUANTA" no. ANR-17-ASTR-0025-01, grant "TAIOL" no. ANR-18-QUAN-00L5-02 and grant "EOSBECMR" no. ANR-18-CE91-0003-01, the European Space Agency, IFRAF (Institut Francilien de Recherche sur les Atomes Froids), the action spécifique GRAM (Gravitation, Relativité, Astronomie et Métrologie) and Conseil Régional de Nouvelle-Aquitaine for the Excellence Chair. Hybrid navigation systems are the result of a joint laboratory between iXBlue and LP2N. E.R. and C.S. acknowledge financial support by the CRC 1227 DQmat, the CRC 1128 geo-O,

the Deutsche Forschungsgemeinschaft under the German Excellence Strategy (EXC-2123-B2), the German Space Agency (DLR) with funds provided by the Federal Ministry for Economic Affairs and Energy (BMWi) due to an enactment of the German Bundestag under grant nos. DLR 50WM1952, 50WP1700, 50WM1431 and "Niedersachsisches Vorab" through "Förderung von Wissenschaft und Technik in Forschung und Lehre" for the initial funding of research in the new DLR-SI Institute, and through the "Quantum and Nanometrology (QUANOMET)" initiative within the project QT3. The work of W.P.S. and A.R. is supported by the DLR with funds provided by the BMWi due to an enactment of the German Bundestag under grant nos. DLR50WM1331-1137, 50WM1556 (QUANTUS IV) and 50WM1641. Moreover, W.P.S. is grateful to Texas A&M University for a Faculty Fellowship at the Hagler Institute for Advanced Study and to Texas A&M AgriLife Research for the support of this work. The research of IQ $^{\text{ST}}$  is financially supported by the Ministry of Science, Research and the Arts of Baden-Württemberg.

# Author contributions

The authors contributed equally to all aspects of the article.

# Competing interests

The authors declare no competing interests.

# Publisher's note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

# Reviewer information

Nature Reviews Physics thanks Guglielmo Tino, Shau-Yu Lan and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

$\odot$  Springer Nature Limited 2019, corrected publication 2021