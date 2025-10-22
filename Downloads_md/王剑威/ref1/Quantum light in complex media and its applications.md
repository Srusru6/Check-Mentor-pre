# Quantum light in complex media and its applications

Ohad Lib and Yaron Bromberg

Photons are often referred to as flying quantum bits, a phrase that emphasizes both their quantum character and their ability to carry quantum information between two distant points. To what extent this holds for complex disordered media, such as the turbulent atmosphere or multimode optical fibres, is an active avenue of research. Over the past few decades physicists have discovered fascinating transport properties of classical light in complex media and developed incredibly powerful tools for controlling it. Recently, these findings have been extended to the quantum realm, demonstrating that quantum properties of light can also be controlled while traversing a complex scattering medium. In this Perspective we highlight some of the main developments in this endeavour, as well as their relevance to applications in quantum key distribution, quantum authentication and Boson sampling.

scattering of particles and waves sets fundamental limits on the transport of energy and information in inhomogeneous media. It deflects their propagation direction and completely randomizes it after multiple scattering events. In classical physics, multiple scattering of particles such as electrons in metals causes a diffusive spread in the sample. When quantum mechanics kicks in, a variety of coherent effects coined mesoscopic phenomena dramatically change the particle's transport properties. Shortly after the discovery of mesoscopic phenomena for electrons, it was realized that classical theory predicts very similar effects for light, as these are essentially wave phenomena<sup>1</sup>. Indeed, over the past few decades researchers have discovered a plethora of optical mesoscopic phenomena that govern the transport of light in complex media, and developed strikingly powerful tools to control it (see the Review by Cao, Mosk and Rotter in this issue<sup>2</sup>). However, despite the field of mesoscopic optics being inspired by the quantum transport theory for electrons, until recently it hardly dealt with quantum effects related to scattering of photons.

Photons are seemingly particles of light, but they scatter very differently from balls in a pinball machine. When a single photon scatters, its various trajectories in the medium interfere. The spatial distribution of the photon therefore exhibits a speckle pattern, which is identical to the speckle pattern observed for a classical wave at the same optical mode. However, when two or more photons scatter, peculiar two-photon interference effects can emerge (Box 1). If the photons occupy quantum states such as Fock, squeezed or entangled states, two-photon interference can induce correlations that cannot be explained by the classical theory of light. We call such states quantum light, in contrast to classical light that relates, for example, to coherent and thermal states, which yield correlations that can be described by classical physics.

An immediate question is then: what can we learn about scattering of quantum light from nearly 40 years of research on mesoscopic phenomena with classical light? And can we adopt the powerful tools developed to control transport of classical light to deliver quantum light through disordered media? Answering such questions will bring us one step closer to understanding fundamental quantum limits on the transport of light. This has become a timely issue, given the recent rapid advances in utilizing quantum light in real-life scenarios. On the flip side, it is important to ask how we can benefit from recent breakthroughs in quantum information processing with photons to advance our understanding of classical

light transport. Can quantum light improve the sensitivity of measuring features of complex media? Are there new applications in quantum technologies that can benefit from scattering in complex media? Although research on some of these questions is still at its infancy, remarkable developments are constantly being reported. In this Perspective we highlight some of the main findings in this discipline, and point to what we believe are promising future directions.

# Quantum light in scattering media

An outstanding challenge in studying quantum light in scattering media is to identify to what extent its non-classical features survive multiple scattering. As scattering in the optical domain is mostly elastic and does not induce decoherence, it can be modelled by local unitary transformations. In essence, the quantum properties of light are conserved under local unitary transformations, independently of their complexity. In practice, however, absorption, finite collection efficiencies or scattering by a dynamic medium can all result in a non-unitary evolution that smears non-classical features.

Consider for example scattering of amplitude-squeezed light—states with sub-shot-noise fluctuations in the number of photons they carry. When only part of the scattered light is collected, sub-shot-noise statistics are smeared by excess noise due to vacuum fluctuations entering from unused channels, and due to classical fluctuations in the sample's scattering matrix. It is generally difficult to distinguish between fluctuations inherent to the quantum state of the light and excess classical fluctuations, as they are non-separable[6,7]. Early experiments therefore focused on the easier task of measuring the shot noise of coherent light that undergoes multiple scattering, as the statistics of coherent states is immune to finite collection efficiencies[8]. Later, carefully designed experiments were able to show that sub-shot-noise statistics of amplitude-squeezed light survives multiple scattering in strongly scattering samples, even after disorder averaging. Remarkably, when more than  $25\%$  of the scattered light was collected and detected, it became possible to measure intensity fluctuations that are  $0.5\mathrm{dB}$  lower than the shot-noise limit, in either reflection or transmission geometries[9,10] (Fig. 1a).

Identifying the signatures of entanglement between photons in scattering media is another ongoing challenge for researchers in the field. Because entanglement is immune to local unitary transformations, it is preserved—even in the multiple scattering regime—as long as all scattered photons can be collected. But when the quantum state evolution is not unitary, incident entangled states evolve

# Box 1 | Single counts, coincidence counts and two-photon interference

Quantum features of light cannot be probed by simply counting the average number of photons that arrive at the detector. Imagine, for example, that we inject a single photon into an input port of a symmetric beam splitter (left). As the photon cannot split, it will reach either one of the output detectors with a probability of 0.5. If we repeat this experiment multiple times, we will find that the detection rate at each detector  $R$ , the single-counts rate, is half the rate of the incoming flux. This is also what we would have expected from classical theory of light, as the single-counts rate, or equivalently the mean photon number  $\langle \hat{n} \rangle$ , is proportional to the optical intensity.

To experimentally show that at each instance of time exactly one photon entered the beam splitter, higher-order moments of the photon-number distribution typically need to be measured. As most single-photon detectors cannot resolve the number of photons that instantaneously illuminate them, such higher-order moments are often measured in a Hanbury Brown-Twiss configuration $^{83}$ , by registering the rate of events in which both detectors detect a photon simultaneously, known as the coincidence rate. As the coincidence rate  $C_{12}$  between detectors 1 and 2 is proportional to the two-photon correlation  $\langle \hat{n}_1\hat{n}_2\rangle$ , for perfect single-photon sources the coincidence rate is zero.

Surprisingly, when two indistinguishable photons enter the beam splitter, one from each port, the coincidence rate also vanishes (middle). The reason is that out of the four paths that the photons can take, there are two indistinguishable paths that lead to a coincidence event (depicted in the dashed box): both photons can be either transmitted or reflected by the beam splitter. When it is impossible to identify which path the photons took, interference of the two paths is observed (two-photon interference). For a symmetric lossless beam splitter, the paths interfere destructively and the photons never arrive at the two detectors simultaneously, as first discovered by Hong, Ou and Mandel (HOM)[84]. By

introducing a delay between the photons, the paths become distinguishable and coincidence events are observed.

Remarkably, two-photon interference can occur even if the photons themselves are distinguishable. For example, the photons entering the beam splitter can have orthogonal polarizations and still exhibit the HOM effect if they are in a polarization entangled state; that is, a superposition of a state describing a horizontally polarized photon entering port a and a vertically polarized photon entering port  $a^{\prime}$ , and a state describing a vertically polarized photon entering port a and a horizontally polarized photon entering port  $a^{\prime}$ . For such inputs it is not known which port each photon entered, and it is therefore impossible to distinguish between the possibility that both photons were reflected or transmitted by the beam splitter, so the two paths interfere. Interestingly, the nature of the interference is determined by the symmetry of the entangled state. An antisymmetric (singlet) state yields a constructive interference, meaning that the two photons will always exit the beam splitter at opposite ports, hence mimicking fermion-like behaviour.

HOM interference is a cornerstone of quantum optics: it reflects the subtle interplay between the wave and particle natures of light, it is a powerful way to measure indistinguishability of photons and it is a key ingredient in generating non-classical states of light. A major body of research on quantum light in complex media is focused on investigating the HOM effect, and more broadly two-photon interference, in complex media. Photons can couple to the sample through many different channels and follow complex scattering trajectories in it, captured by the scattering matrix of the sample  $S_{\mathrm{ba}}$  (right). The coincidence rate and higher-order correlations between photons arriving at detectors b and  $\mathbf{b}^{\prime}$ , which are determined by the scattering matrix, are measured and analysed to probe and control the quantum state of the photons.

![](images/aeba26b706712c8aea3c37d51edb6d64a94f3c44289beea8711a251bb51c44f1.jpg)

to mixed states and entanglement may be lost $^{11,12}$ . If the non-unitary evolution stems from loss, post selection can be used to recover a pure state, and entanglement can be probed. In particular, spatially resolved coincidence detection can be used to measure the two-photon probability amplitude of spatially entangled photons, even if just a small fraction of the photons is detected.

A prominent example is the scattering of photons in an Einstein-Podolsky-Rosen (EPR) maximally entangled state—pairs of photons that are perfectly correlated in the spatial domain and at the same time perfectly anti-correlated in the angular domain. Although the spatial distribution of scattered EPR photons is flat and does not reveal spatial information, the coincidence map

exhibits a speckle pattern called two-photon speckle[13,14] (Fig. 1b). Similar to the HOM effect, nulls of the two-photon speckle indicate that photons never arrive at the two detectors simultaneously, even though each detector constantly detects photons. In fact, the simultaneous observation of a high-contrast two-photon speckle and a low-contrast single-photon distribution is a signature that the incident photons were in a high-dimensional entangled state. The dimension of the EPR state, quantified by its Schmidt number  $K$ , can be probed by the statistics of the two-photon speckle. For high-dimensional states ( $K \gg 1$ ), the two-photon speckle follows Rayleigh statistics with an exponential probability distribution—exactly like the intensity in classical speckle patterns[13,15]. This is a

![](images/f8d815483a2e0f2ea50da15aed0c607f6cec721a7bd17fb73e2a0a2f164fcf5b.jpg)  
a

![](images/2995aca4843b938eeb5ace1abf2deb2f11b50b0dd9e89aea130face3c7671784.jpg)

![](images/e5c865c609ad2ea0884e7b3367f853ef6b61228cf369f1fef3d37e4a96562f47.jpg)

![](images/9a3c912598bc8234f23a16d3e03b32eca3a37a9afe9743fc1b603a55826cf994.jpg)  
b

![](images/d743da3da156e2ee8903cc42f290706c16a7a29902d8e1162b026e25b8251895.jpg)  
Single count rate (MHz)

![](images/02d5c40e798fd2b79d8695f50ed8356a3eeb8462f7d83513a4e0d8e98951bf5f.jpg)  
(1)

![](images/cf49e472fbca136fb8c57c3b6bad36871724897286c60776c003bac14afddbd7.jpg)  
$C_{12} / \langle C_{12}\rangle$

![](images/24f8935f56b553734a1f2a5e1627614e3d60396d6dd412397ccffee91d025ab5.jpg)  
c  
Homogeneous lattices  
Two-photon quantum walk

![](images/9d56ec509bd6d71616568f961bb3e9cadd784178f86e4303d125beb3a4730721.jpg)  
Disordered lattices

![](images/2c1d8d5fa65b7eb7111f9900e24ec7a89b3dbbe0972a89baf899319db9cd2ab2.jpg)  
Bosons

![](images/df07232f89a1eb1c65d918d1949e1b343392a7911a1b0e4d1c73aa95ea8d3f8b.jpg)

![](images/6cd3bcd92ecfc773b29df647044ce458c8ccdddb0cbe45ef15708d5e1c2cf08c.jpg)  
Fermions  
b

![](images/663979417d4dc033a7c60ba38733d846e93f56b196686bd2a57402dd93db97f6.jpg)  
$b$

![](images/4104b503b4e86b7b69db2e44e8eb0a8e1ecba89b0492772f208877388a00f862.jpg)  
Fig. 1 | Quantum light in disordered samples. a, Squeezed light, generated by interfering light from an optical parametric generator with a local oscillator, is scattered by a strongly scattering sample S. The single-count pattern (bottom left) exhibits a seemingly noisy speckle pattern. Nevertheless, when the relative phase  $\phi$  between the local oscillator and the optical parametric generator is set to generate amplitude-squeezed light, fluctuations in the total number of collected photons are lower than the shot-noise limit (bottom right, grey data points). BS: beam splitter, FM: folding mirror, PPKTP: periodically poled potassium titanyl phosphate nonlinear crystal, SA spectrum analyzer. b, Top left, spatially entangled photons in an EPR state are scattered by a scattering sample S and detected in the far-field. While the pattern of the single counts (top right) is homogeneous and does not exhibit interference effects, the coincidence map  $C_{12}$  (bottom left) exhibits two-photon speckles with statistics described by an exponential probability distribution function  $P_2$  (bottom right). Dotted and dashed lines mark the predicted distributions in linear and logarithmic scales. c, Quantum walks in homogeneous and disordered lattices: photons in a lattice of coupled waveguides $^{23}$ , or a mesh of integrated couplers $^{24}$ , coherently hop between sites. In homogeneous lattices (left column), the single-photon distribution is characterized by two lobes that spread ballistically in the lattice (top left). When two photons walk in the lattice, they bunch to the same lobe, as manifested by the diagonal peak in the coincidence map measured at the output of the lattice (middle left) $^{23}$ . Fermions, mimicked by an antisymmetric spatial amplitude, exhibit peaks along the anti-diagonal, which corresponds to antibunching (bottom left) $^{24}$ . In disordered lattices (right column), the photons experience transverse Anderson localization $^{25}$ . For an EPR input, a localized coincidence map is observed while the single-count distribution is wide (middle right) $^{27}$ . Fermionic-like antibunching can still be observed right before the onset of localization (bottom right) $^{26}$ . The mean photon number distribution is plotted to the right of each coincidence map, each coincidence map is normalized to its maximum. Figure adapted with permission from: a, ref. $^{9}$ , APS; b, top right and bottom left: ref. $^{14}$ , APS; bottom right: ref. $^{15}$ , APS; c, top row: ref. $^{25}$ , APS; middle left: ref. $^{23}$ , AAAS; bottom left: ref. $^{24}$  Springer Nature Limited; middle right: ref. $^{27}$ , APS; bottom right: ref. $^{26}$ , APS.

![](images/a8625e7c95a515c0d968263988f089232ec71b3dcec0342a1efa87958c3e80b8.jpg)

unique feature of high-dimensional entanglement, as for classical light and for separable states  $(K = 1)$ , the coincidence counts exhibit super-Rayleigh statistics with long-tailed probability distributions.

When the photons scatter in a dynamic medium, most of the features of two-photon speckle are smeared. The photons are found in a mixed state and post selection becomes impossible, unless the detection bandwidth is wider than the bandwidth of the medium's fluctuations. Nevertheless, the disorder-averaged

coincidence map can still exhibit pronounced coherent phenomena. For example, in transmission geometry it exhibits a peak, or dip, depending on the bosonic or fermionic symmetry of the incident two-photon state<sup>16</sup>. Interestingly, in a backscattering geometry, the disorder-averaged coincidence map exhibits a coherent backscattering peak, which is more robust and carries more information on the transport mean-free path of the scattering sample than its classical counterpart<sup>17</sup>. To further advance our understanding of quantum

light transport in a scattering medium, it is essential to investigate other mesoscopic effects of quantum light that survive disorder averaging, such as universal conductance fluctuations and universal optimal transmission.

# Quantum walks in disordered lattices

The propagation of light in scattering media can be conveniently studied using lattices of coupled waveguides. Such lattices allow precise control over the disorder strength, the system dimension and the number of modes involved, and have proved useful for observing mesoscopic phenomena of classical light such as transverse Anderson localization<sup>18</sup>. It is therefore extremely interesting to analyse the physics of quantum light in such lattices, because they highlight genuine quantum phenomena and suggest applications that could then be enhanced when implemented in complex multiply scattering media.

The dynamics of photons in waveguide lattices is often modelled by a quantum walk process. In quantum walks, the walkers—in this case photons—randomly choose which path to follow as they hop between lattice sites, but maintain coherence over all the paths taken[19]. Interestingly, the coherent propagation results in striking features even in the absence of disorder; that is, in lattices of identical waveguides at equal spacing. A single photon in an ordered lattice exhibits a fast ballistic spread in a pattern characterized by two strong lobes, which can be linked to potential speed-ups in quantum computation[20]. Single-photon dynamics can be observed using classical laser light[21,22], whereas experiments with pairs of photons reveal quantum features that cannot be mimicked by classical light. Specifically, two-photon interference yields a generalized HOM effect that determines whether the photons can occupy the same lobe or not (Fig. 1c). When correlated photons are injected into the lattice, bunching is observed and the photons are found in the same lobe, manifested by vanishing anti-diagonal lobes in the two-photon coincidence map[23]. When the photons are injected into the lattice in an antisymmetric entangled state that mimics fermions, they anti-bunch and arrive at opposite sides of the lattice[24].

Adding disorder to the lattice dramatically affects the two-photon quantum walk $^{25}$ . Static disorder halts the spread of a single walker in the lattice via transverse Anderson localization $^{18}$ . As a consequence, the two-photon coincidence map also exhibits localized correlations, with features that are imprinted by the two-photon input state. For example, antisymmetric fermionic-like inputs are slightly less localized than symmetric bosonic inputs $^{24}$  and exhibit a checkered correlation map that persists after disorder averaging $^{25,26}$ . When the input two-photon state is extended over multiple lattice sites in an EPR state, the single-photon distribution is extended but the two-photon correlation remains localized $^{27}$ . Interestingly, the crossover between ballistic propagation and localization can be studied at short propagation distances, revealing that the localization of one photon increases the probability that its twin photon will also localize $^{25,26}$ .

Quantum walks in waveguide lattices provide an exciting test-bed for experimental studies of the interplay between disorder and the quantum nature of light, as they allow precise tuning of the lattice parameters, together with high coupling and collection efficiencies. However, experiments thus far have mostly been restricted to one-dimensional geometries, limiting opportunities to study phenomena that are absent in one-dimensional waveguide lattices such as coherent backscattering, universal conductance fluctuations and universal optimal transmission. Recent developments in two-photon quantum walks in two-dimensional lattices may open new opportunities to study the effect of disorder in higher dimensions[28]. Nonetheless, complex media such as paint layers or multimode fibres are very promising optical platforms for observing these effects owing to their complex three-dimensional geometries

and the very large number of modes and degrees of freedom (polarization, space and time) they couple.

# Shaping quantum light in complex media

The ability to not only observe, but also to control, scattering of light in complex media has led to a plethora of opportunities for studying, utilizing and compensating scattering of classical light (see Reviews by Cao, Mosk and Rotter $^{2}$  and Bertolotti and Katz $^{29}$ ). It is therefore appealing to extend wavefront shaping to the quantum domain. In particular, a pioneering motivation for the use of shaping in this context is to turn complex media into reconfigurable optical platforms for quantum light, in the spirit of what is done with quantum walks in photonic lattices $^{30}$  but on a much larger complexity scale $^{31-34}$ . Quantum wavefront shaping is, however, a challenging task, because the inherently weak signals associated with quantum light prevent direct evaluation of the desired wavefront by means of optimization or transmission matrix measurements.

The first attempts to overcome this challenge exploited the correspondence between scattering of a single photon and scattering of classical laser light sharing the same wavelength, polarization and spatial mode. By co-aligning an auxiliary classical laser with the same properties as the single photons, one can apply wavefront-shaping techniques to the classical laser light and then apply the same wavefront correction to the single photons (Fig. 2a). This approach was used to compensate scattering of single photons by white paint[31,32] and in a few-mode fibre[35]. Good spatial overlap was ensured by passing both the single photons and the classical laser through the same single-mode fibre before they entered the medium. The same approach was later extended to control two-photon interference in scattering media[33] and multimode fibres (Fig. 2b)[34]. By coupling two photons to single-mode fibres and independently shaping their wavefronts, programmable two-photon quantum interference and focusing was achieved by either relying on the optimization of the classical laser[33] or the full characterization of the two-photon transmission matrix by classical light[34] (Fig. 2b).

Passing the photons through single-mode fibres before they are shaped and scattered is ideal for matching the spatial profiles of the classical laser and the quantum light. However, this leads to a non-unitary projection of each photon onto a single spatial mode, destroying any spatial entanglement between them—unless methods with tailored encoding schemes in other degrees of freedom are used[36]. This limitation was lifted in ref.[37], where scattering of photons in an EPR state was compensated by taking advantage of the optical memory effect, which predicts correlations between speckle patterns observed by two different illumination angles (see box 1 in ref.[29]). Compensating scattering of a classical laser beam that was co-aligned with the central propagation angle of the EPR state also compensated scattering of all the pairs within the angular bandwidth of the memory effect.

Although using a co-aligned laser beam to undo scattering of EPR states solves the problem of relying on the weak flux of quantum light for the optimization process, real-time wavefront shaping still remains a challenge. This is because the strong classical laser that shares the properties of the quantum signal cannot be filtered out, so that the optimization process and the transmission of the quantum signals cannot be done simultaneously. One solution to this problem is to use a classical laser with a wavelength similar, yet not identical, to that of the quantum light as a beacon for optimization. Using this approach, adaptive optics was employed to compensate for scattering of single photons induced by atmospheric turbulence[38-40]. An alternative solution for real-time shaping of EPR states is pump shaping[41], where, rather than directly manipulating the quantum light, shaping is applied to the wavefront of the classical pump beam that generates the entangled photons via spontaneous parametric down conversion (SPDC) (Fig. 2c). In addition, instead of adding an auxiliary laser source, the intensity of

![](images/d6ee7f08c82ffeff6f3c97103e2935f034df319fbd200d7a617f14ec48dcd670.jpg)  
a

![](images/2756aa9f09fbabe98343cc8303ba5d91c1d24ef162330dc93e7dc46ab327e906.jpg)  
c

![](images/d629193b1bae77dd7719ec4bb5647637f98aeacb37ca077eb3c2d6a45e2fe469.jpg)  
b  
d

![](images/c4da765178fa0b8ecfcfba6c5c3cd90fe1f7266aa27c0f0ec3f14f9921abc377.jpg)

![](images/54072bbfb98c5a13c2641f30ce04087b87da514aa2a1a080da9f1ad1c1c7193d.jpg)  
Fig. 2 | Quantum wavefront shaping. a, Focusing of heralded single photons through a complex medium can be achieved by tailoring their wavefront using a spatial light modulator (SLM). The required phase mask for focusing is found by first passing a bright classical laser through the same polarization maintaining single-mode fibre (PMSMF) as the heralded single photon and then searching for the phase mask that will focus the laser light by measuring the transmission matrix of the sample or using an adaptive optimization algorithm<sup>31,32</sup>. Top panel, a typical set-up. Bottom, the single-photon detection rate before (red curve) and after (green curve) optimization<sup>32</sup>. SPDC, spontaneous parametric down conversion; BPF, bandpass filter; PBS, polarization beam splitter; NA, numerical aperture. b, Top panel, two-photon interference in scattering media is controlled, according to a previous classical measurement with a bright source, by shaping the wavefront of two indistinguishable photons entering the medium<sup>34</sup>. Bottom panel, two-photon interference contrast as a function of a delay  $\delta$  introduced between the photons. c, Scattering of spatially entangled photons is compensated using pump shaping. Despite their different wavelengths, the classical pump beam (top left inset) and the entangled photons (top middle inset) exhibit similar speckle patterns. The classical optimization of the pump beam simultaneously compensates for the scattering of the entangled photons, without shaping them directly (top right inset)<sup>41</sup>. L1-L5: lenses. d, The  $d^2$ -dimensional transmission matrix of a complex medium (T) can be mapped onto a single maximally entangled state of dimension  $d$  (bottom left), instead of probing the medium with  $d$  separate classical probe states (top left). Spatial entanglement between pairs of photons can be restored after a complex medium by applying the inverse operation on the photon that did not enter it<sup>43</sup>. Right panels depict T represented in the pixel basis  $|m\rangle$ , before (top) and after (bottom) the inverse operation. Figure adapted with permission from: a, ref.<sup>32</sup>, The Optical Society; b, ref.<sup>34</sup> under a Creative Commons license CC BY-NC 4.0; c, ref.<sup>41</sup> under a Creative Commons license CC BY-NC 4.0; d, ref.<sup>43</sup>, Springer Nature Limited.

the scattered pump beam is used as feedback to optimize the quantum correlations.

Although pump shaping is attractive for real-time shaping of entangled photons, it relies on the fact that both photons are sent through the scattering medium, which is often not the case. In many applications, such as quantum key distribution (QKD), one-sided channels are typically used, where only one photon from an entangled pair is transmitted through the scattering medium (for example, a turbulent atmosphere[42]). In ref.[43], only one photon from a pair of high-dimensional entangled photons was sent through a one-sided channel consisting of a multimode fibre. Interestingly, six-dimensional entanglement between the photons was certified after the multimode fibre by 'scrambling' the photon that was not sent through it, rather than by 'unscrambling' the photon that did. Finding the phase pattern needed to scramble the photon requires

the transmission matrix of the multimode fibre to be measured. Unlike transmission matrix measurements using classical light, which are performed by sending a set of orthogonal probe states through the medium (see the Review by Bertolotti and Katz[29]), with maximally entangled states, it is enough to measure the final two-photon amplitude of a single input state (Fig. 2d). This is an outstanding example of the Choi-Jamiolkowski isomorphism, which maps maximally entangled states to channels, thus providing full information on the channel by performing quantum state tomography, and vice versa[42,44].

# Scattering in quantum applications

The transition of photonic quantum technologies from small-scale laboratory demonstrations to real-world implementations often involves unavoidable scattering and mixing. In applications such

![](images/69dfbd53604a64c892616a36e3acc8bdf893790013187272d84f260f66f84785.jpg)  
a

![](images/5a9b196015709f06da581281479d1b287171f32ac0d1ed28c56906b5c42b16ac.jpg)  
b

![](images/dff14f66a68e05b0032375245e44ab86327e34394df0fefdc8c3e8862b47d109.jpg)  
c

![](images/62cde1c87dab7dbda7f67d7c52dc861258ae0a910a087bff291885f43c74e4df.jpg)  
Fig. 3 | Applications with quantum light in complex media. a, Quantum adaptive optics using a deformable mirror (DM), fast steering mirror (FSM), and a beacon laser (BL) improved the collection efficiency of single photons passing a total of  $19.2\mathrm{km}$  through turbulent atmosphere between Alice and Bob to Charlie's measurement station in a demonstration of measurement-device-independent QKD in free space40. SNSPD, superconducting nanowire single-photon detector; F(P)BS, fibre (polarization) beam splitter; DWDM, dense wavelength division multiplexing. b, Quantum secure authentication using a physically unclonable key based on a complex scattering sample. A spatial light modulator (SLM1) shapes a few-photon wavefront to create a random challenge. SLM2 is set so that a focused spot (left inset) is obtained for the true key. If a wrong key is inserted, a random speckle pattern will be detected (right inset) and the authentication will fail52. c, Top, boson sampling achieves a quantum computational advantage by passing (for example) single photons or squeezed light through a multiport interferometer with a random transmission matrix57. Bottom, the distribution of the output amplitude (left) and phase (right) at each port approaches that of a scattering medium for large interferometers58. Figure adapted with permission from: a, ref.40, APS; b, ref.52, The Optical Society; c(bottom), ref.58, AAAS. Panel c (top) reproduced with permission from ref.57 under a Creative Commons license CC BY 4.0.

![](images/6bedf3a279a1bbc5a60c5414168b8c40d6873d65f8d65814321191d1bddb32ef.jpg)

as quantum communication, scattering deteriorates the performance of the system, and ways to mitigate it are constantly being explored (Fig. 3a) $^{45,46}$ . Specifically in free-space QKD, single photons are sent through a turbulent atmospheric link that may scramble the encoded information and reduce collection efficiencies $^{45,46}$ . High-dimensional spatial encoding of quantum information, which is useful for enhancing the capacity of a quantum link, is especially sensitive to scattering and aberrations. Scattering of orbital-angular-momentum modes has therefore been extensively studied over the past few years, setting limits on the capacity of free-space QKD using orbital-angular-momentum modes $^{47-51}$ . When the mode structure is not resilient enough, adaptive optics offers a way to mitigate the detrimental effect of atmospheric turbulence. In two recent demonstrations, optimization based on a beacon laser was employed in a high-dimensional  $300\mathrm{m}$  link $^{39}$ , and in a  $19.2\mathrm{km}$  QKD link based on a single spatial mode, indicating up to  $12\mathrm{dB}$  improvements in link efficiency (Fig. 3a) $^{40}$ .

Scattering of quantum light is not necessarily a nuisance. For example, as the complexity of large scattering samples is nearly impossible to reproduce, they are excellent candidates for authentication applications, where quantum security is ensured when the number of photons per detected mode is less than one (Fig. 3b) $^{52}$ . Similarly, the complex propagation of single photons or weak coherent pulses through multimode fibres, together with wavefront

shaping, offer new possibilities for high-dimensional quantum key establishment[53]. In addition, mode mixing in multimode fibres provides access to the large Hilbert space spanned by the fibre's modes, making quantum wavefront shaping in multimode fibres an intriguing platform to realize programmable quantum networks[54,55].

Another interesting application that can benefit from mixing a massively large number of spatial modes is Boson sampling, where quantum advantage can be demonstrated by measuring the output distribution of photons passing through random unitary interferometers, sampled according to the Haar measure (Fig. 3c) $^{56-58}$ . A route for simplifying the implementation of such large multiport interferometers using scattering media was recently proposed $^{59}$ , offering exciting new possibilities for applications of quantum light in disordered samples.

# Future directions, challenges and outlook

Over the past two decades significant progress has been made in studying, overcoming and utilizing scattering of quantum light in complex media. Nevertheless, some fundamental questions and phenomena, as well as important applications, remain largely unexplored. For example, a timely challenge in our fundamental understanding of high-dimensional entanglement is to develop efficient and robust methods to certify and quantify entanglement in high dimensions $^{60}$ . As entanglement certification typically requires

projection of the quantum state onto a set of mutually unbiased bases—whereas scattering of spatially entangled photons can be considered as projection onto random bases—it is appealing to study whether scattering of entangled photons exhibits features that cannot be reproduced by separable states and can therefore be utilized to certify entanglement. Although experiments relating (for example) the visibility of a two-photon speckle pattern<sup>15</sup> or the width of a disorder-averaged two-photon Hanbury Brown-Twiss peak<sup>61</sup> with spatial entanglement have been performed, a clear, assumption-free criterion for entanglement has yet to be formulated.

Another current challenge is to design experiments that can probe the rich spatiotemporal dynamics of quantum light in complex media. Most experiments have so far focused on spatial correlations and assumed that the photons occupy a single temporal mode, but theory predicts intriguing temporal dynamics of time-frequency entangled photons[62,63]. The two-photon interference is expected to depend on the interplay between the time the photons spend in the sample (Thouless time) and the two timescales that characterize time-frequency entangled photons, namely the coherence time of the two-photon state and the typical time difference between the photons. Scattering can therefore encode temporal information on the quantum state of the photons, potentially with the help of spatiotemporal wavefront shaping tools[64-66], which can then be probed by temporally resolved coincidence measurements.

In terms of applications, rapid developments in imaging with classical light in complex medium (see the Review by Bertolotti and Katz $^{29}$ ), along with constant advancements in the means to generate and control quantum light, call for the exploration of quantum imaging in complex media $^{67}$ . Quantum imaging offers several appealing features, such as super-resolution imaging $^{68}$ , enhanced resilience to noise $^{69,70}$  and new imaging configurations $^{71}$ . We anticipate that by combining knowledge from classical and quantum wavefront shaping with quantum imaging, scattering of entangled photons can be overcome and allow quantum imaging inside and through scattering samples $^{72}$  and living tissue $^{73,74}$ . In this respect, it is essential to extend the set of quantum light sources that are currently used to illuminate the samples, and consider quantum emitters that are embedded within the sample $^{68,75,76}$ .

Finally, the need to control and detect photons spread over a large number of spatial modes is common for almost all applications and experiments presented in this Perspective. We thus believe that developing better methods to shape single and entangled photons is crucial to further advance the field. For example, a higher degree of control can be obtained by shaping the photons in more than a single plane, using multi-plane light converters[77-79]. Besides shaping, the number of detected modes of scattered photons can be boosted, for example by using electron multiplying charge coupled devices (EMCCDs) instead of scanning detectors[80,81], and ultimately by utilizing the rapidly developing technology of single-photon avalanche diode arrays[82]. We expect that these new technologies and methods will open up new opportunities for research and applications of scattering of quantum light.

Received: 4 February 2022; Accepted: 27 June 2022

Published online: 8 September 2022

# References

1. Akkermans, E. & Montambaux, G. Mesoscopic Physics of Electrons and Photons (Cambridge Univ. Press, 2007).  
2. Cao, H., Mosk, A. & Rotter, S. Shaping the propagation of light in complex media. Nat. Phys. https://doi.org/10.1038/s41567-022-01677-x (2022).  
3. Gerry, C., Knight, P. & Knight, P. L. Introductory Quantum Optics (Cambridge Univ. Press, 2005).  
4. Patra, M. & Beenakker, C. W. J. Propagation of squeezed radiation through amplifying or absorbing random media. Phys. Rev. A 61, 063805 (2000).

5. Starshynov, I., Bertolotti, J. & Anders, J. Quantum correlation of light scattered by disordered media. Opt. Express 24, 4662-4671 (2016).  
6. Lodahl, P., Mosk, A. & Lagendijk, A. Spatial quantum correlations in multiple scattered light. Phys. Rev. Lett. 95, 173901 (2005).  
7. Skipetrov, S. E. Quantum theory of dynamic multiple light scattering in fluctuating disordered media. Phys. Rev. A 75, (2007).  
8. Lodahl, P. & Lagendijk, A. Transport of quantum noise through random media. Phys. Rev. Lett. 94, 153905 (2005).  
9. Smolka, S., Huck, A., Andersen, U. L., Lagendijk, A. & Lodahl, P. Observation of spatial quantum correlations induced by multiple scattering of nonclassical light. Phys. Rev. Lett. 102, 193901 (2009).  
10. Smolka, S., Ott, J. R., Huck, A., Andersen, U. L. & Lodahl, P. Continuous-wave spatial quantum correlations of light induced by multiple scattering. Phys. Rev. A 86, 033814 (2012).  
11. Aiello, A. & Woerdman, J. P. Intrinsic entanglement degradation by multimode detection. Phys. Rev. A 70, 023808 (2004).  
12. Candé, M., Goetschy, A. & Skipetrov, S. E. Transmission of quantum entanglement through a random medium. *Europhys. Lett.* 107, 54004 (2014).  
13. Beenakker, C. W. J., Venderbos, J. W. F. & van Exter, M. P. Two-photon speckle as a probe of multi-dimensional entanglement. Phys. Rev. Lett. 102, 193601 (2009).  
14. Peeters, W. H., Moerman, J. J. D. & van Exter, M. P. Observation of two-photon speckle patterns. Phys. Rev. Lett. 104, 173601 (2010).  
15. Pires, H. D. L., Woudenberg, J. & Van Exter, M. Statistical properties of two-photon speckles. Phys. Rev. A 85, 033807 (2012).  
16. Van Exter, M., Woudenberg, J., Pires, H. D. L. & Peeters, W. Bosonic, fermionic, and anyonic symmetry in two-photon random scattering. Phys. Rev. A 85, 033823 (2012).  
17. Safadi, M. et al. Coherent backscattering of entangled photon pairs. Preprint at https://arxiv.org/abs/2203.09650 (2022).  
18. Segev, M., Silberberg, Y. & Christodoulides, D. N. Anderson localization of light. Nat. Photon. 7, 197-204 (2013).  
19. Aharonov, Y., Davidovich, L. & Zagury, N. Quantum random walks. Phys. Rev. A 48, 1687-1690 (1993).  
20. Childs, A. M. Universal computation by quantum walk. Phys. Rev. Lett. 102, 180501 (2009).  
21. Perets, H. B. et al. Realization of quantum walks with negligible decoherence in waveguide lattices. Phys. Rev. Lett. 100, 170506 (2008).  
22. Schreiber, A. et al. A 2D quantum walk simulation of two-particle dynamics. Science 336, 55-58 (2012).  
23. Peruzzo, A. et al. Quantum walks of correlated photons. Science 329, 1500-1503 (2010).  
24. Crespi, A. et al. Anderson localization of entangled photons in an integrated quantum walk. Nat. Photon. 7, 322-328 (2013).  
25. Lahini, Y., Bromberg, Y., Christodoulides, D. N. & Silberberg, Y. Quantum correlations in two-particle Anderson localization. Phys. Rev. Lett. 105, 163905 (2010).  
26. Gilead, Y., Verbin, M. & Silberberg, Y. Ensemble-averaged quantum correlations between path-entangled photons undergoing Anderson localization. Phys. Rev. Lett. 115, 133602 (2015).  
27. Di Giuseppe, G. et al. Einstein-Podolsky-Rosen spatial entanglement in ordered and Anderson photonic lattices. Phys. Rev. Lett. 110, 150503 (2013).  
28. Jiao, Z.-Q. et al. Two-dimensional quantum walks of correlated photons. Optica 8, 1129-1135 (2021).  
29. Bertolotti, J. & Katz, O. Imaging in complex media. Nat. Phys. https://doi.org/10.1038/s41567-022-01723-8 (2022).  
30. Carolan, J. et al. Universal linear optics. Science 349, 711-716 (2015).  
31. Huisman, T. J., Huisman, S. R., Mosk, A. P. & Pinkse, P. W. Controlling single-photon Fock-state propagation through opaque scattering media. Appl. Phys. B 116, 603-607 (2014).  
32. Defienne, H. et al. Nonclassical light manipulation in a multiple-scattering medium. Opt. Lett. 39, 6090-6093 (2014).  
33. Wolterink, T. A. et al. Programmable two-photon quantum interference in  $10^{3}$  channels in opaque scattering media. Phys. Rev. A 93, 053817 (2016).  
34. Defienne, H., Barbieri, M., Walmsley, I. A., Smith, B. J. & Gigan, S. Two-photon quantum walk in a multimode fiber. Sci. Adv. 2, e1501054 (2016).  
35. Carpenter, J. et al. Mode multiplexed single-photon and classical channels in a few-mode fiber. Opt. Express 21, 28794-28800 (2013).  
36. Liu, J. et al. Multidimensional entanglement transport through single-mode fiber. Sci. Adv. 6, eaay0837 (2020).  
37. Defienne, H., Reichert, M. & Fleischer, J. W. Adaptive quantum optics with spatially entangled photon pairs. Phys. Rev. Lett. 121, 233601 (2018).  
38. Liu, C. et al. Single-end adaptive optics compensation for emulated turbulence in a bi-directional 10-mbit/s per channel free-space quantum communication link using orbital-angular-momentum encoding. Research 2019, 8326701 (2019).

39. Zhao, J. et al. Performance of real-time adaptive optics compensation in a turbulent channel with high-dimensional spatial-mode encoding. Opt. Express 28, 15376-15391 (2020).  
40. Cao, Y. et al. Long-distance free-space measurement-device-independent quantum key distribution. Phys. Rev. Lett. 125, 260503 (2020).  
41. Lib, O., Hasson, G. & Bromberg, Y. Real-time shaping of entangled photons by classical control and feedback. Sci. Adv. 6, eabb6298 (2020).  
42. Ndagano, B. et al. Characterizing quantum channels with non-separable states of classical light. Nat. Phys. 13, 397-402 (2017).  
43. Valencia, N. H., Goel, S., McCutcheon, W., Defienne, H. & Malik, M. Unscrambling entanglement through a complex medium. Nat. Phys. 16, 1112-1116 (2020).  
44. Konrad, T. et al. Evolution equation for quantum entanglement. Nat. Phys. 4, 99-102 (2008).  
45. Liao, S.-K. et al. Satellite-to-ground quantum key distribution. Nature 549, 43-47 (2017).  
46. Bedington, R., Arrazola, J. M. & Ling, A. Progress in satellite quantum key distribution. npj Quantum Inf. 3, 30 (2017).  
47. Paterson, C. Atmospheric turbulence and orbital angular momentum of single photons for optical communication. Phys. Rev. Lett. 94, 153901 (2005).  
48. Hamadou Ibrahim, A., Roux, F. S., McLaren, M., Konrad, T. & Forbes, A. Orbital-angular-momentum entanglement in turbulence. Phys. Rev. A 88, 012312 (2013).  
49. Malik, M. et al. Influence of atmospheric turbulence on optical communications using orbital angular momentum for encoding. Opt. Express 20, 13195-13200 (2012).  
50. Goyal, S. K., Roux, F. S., Konrad, T. & Forbes, A. et al. The effect of turbulence on entanglement-based free-space quantum key distribution with photonic orbital angular momentum. J. Opt. 18, 064002 (2016).  
51. Sit, A. et al. High-dimensional intricacy quantum cryptography with structured photons. Optica 4, 1006-1010 (2017).  
52. Goorden, S. A., Horstmann, M., Mosk, A. P., Skorić, B. & Pinkse, P. W. H. Quantum-secure authentication of a physical unclonable key. Optica 1, 421-424 (2014).  
53. Amitonova, L. V. et al. Quantum key establishment via a multimode fiber. Opt. Express 28, 5965-5981 (2020).  
54. Leedrumrongwatthanakun, S. et al. Programmable linear quantum networks with a multimode fibre. Nat. Photon. 14, 139-142 (2020).  
55. Goel, S. et al. Inverse-design of high-dimensional quantum optical circuits in a complex medium. Preprint at https://arxiv.org/abs/2204.00578 (2022).  
56. Aaronson, S. & Arkhipov, A. The computational complexity of linear optics. In Proc. Forty-Third Annual ACM Symposium on Theory of Computing 333-342 (Association for Computing Machinery, 2011).  
57. Brod, D. J. et al. Photonic implementation of boson sampling: a review. Adv. Photon. 1, 034001 (2019).  
58. Zhong, H.-S. et al. Quantum computational advantage using photons. Science 370, 1460-1463 (2020).  
59. van der Meer, R., Huber, S., Pinkse, P., García-Patron, R. & Renema, J. Boson sampling in low-depth optical systems. Preprint at https://arxiv.org/abs/2110.05099 (2021).  
60. Friis, N., Vitagliano, G., Malik, M. & Huber, M. Entanglement certification from theory to experiment. Nat. Rev. Phys. 1, 72-87 (2019).  
61. Lib, O. & Bromberg, Y. Thermal biphotons. *APL Photon.* 7, 031301 (2022).  
62. Cherroret, N. & Buchleitner, A. Entanglement and thouless times from coincidence measurements across disordered media. Phys. Rev. A 83, 033827 (2011).  
63. Candé, M. & Skipetrov, S. E. Quantum versus classical effects in two-photon speckle patterns. Phys. Rev. A 87, 013846 (2013).  
64. Pe'Er, A., Dayan, B., Friesem, A. A. & Silberberg, Y. Temporal shaping of entangled photons. Phys. Rev. Lett. 94, 073601 (2005).  
65. Aulbach, J., Gjonaj, B., Johnson, P. M., Mosk, A. P. & Lagendijk, A. Control of light transmission through opaque scattering media in space and time. Phys. Rev. Lett. 106, 103901 (2011).  
66. Mounaix, M. et al. Spatiotemporal coherent control of light through a multiple scattering medium with the multispectral transmission matrix. Phys. Rev. Lett. 116, 253901 (2016).  
67. Gigan, S. et al. Roadmap on wavefront shaping and deep imaging in complex media. J. Phys Photonics https://iopscience.iop.org/article/10.1088/2515-7647/ac76f9/meta (2022).

68. Tenne, R. et al. Super-resolution enhancement by quantum image scanning microscopy. Nat. Photon. 13, 116-122 (2019).  
69. Brida, G., Genovese, M. & Berchera, I. R. Experimental realization of sub-shot-noise quantum imaging. Nat. Photon. 4, 227-230 (2010).  
70. Defienne, H., Reichert, M., Fleischer, J. W. & Faccio, D. Quantum image distillation. Sci. Adv. 5, eaax0307 (2019).  
71. Lemos, G. B. et al. Quantum imaging with undetected photons. Nature 512, 409-412 (2014).  
72. Defienne, H., Ndagano, B., Lyons, A. & Faccio, D. Polarization entanglement-enabled quantum holography. Nat. Phys. 17, 591-597 (2021).  
73. Shi, L., Galvez, E. J. & Alfano, R. R. Photon entanglement through brain tissue. Sci. Rep. 6, 1-6 (2016).  
74. Lum, D. J. et al. Witnessing the survival of time-energy entanglement through biological tissue and scattering media. Biomed. Opt. Express 12, 3658-3670 (2021).  
75. Sapienza, L. et al. Cavity quantum electrodynamics with Anderson-localized modes. Science 327, 1352-1355 (2010).  
76. Kim, D. & Englund, D. R. Quantum reference beacon-guided superresolution optical focusing in complex media. Science 363, 528-531 (2019).  
77. Brandt, F., Hiekkamäki, M., Bouchard, F., Huber, M. & Fickler, R. High-dimensional quantum gates using full-field spatial modes of photons. Optica 7, 98-107 (2020).  
78. Hiekkamäki, M. & Fickler, R. High-dimensional two-photon interference effects in spatial modes. Phys. Rev. Lett. 126, 123601 (2021).  
79. Lib, O., Sulimany, K. & Bromberg, Y. Reconfigurable synthesizer for quantum information processing of high-dimensional entangled photons. Preprint at https://arxiv.org/abs/2108.02258 (2021).  
80. Defienne, H., Reichert, M. & Fleischer, J. W. General model of photon-pair detection with an image sensor. Phys. Rev. Lett. 120, 203604 (2018).  
81. Gnatiessoro, S., Mosset, A., Lantz, E. & Devaux, F. Imaging spatial quantum correlations through a thin scattering medium. OSA Contin. 2, 3393-3403 (2019).  
82. Madonini, F., Severini, F., Zappa, F. & Villa, F. Single photon avalanche diode arrays for quantum imaging and microscopy. Adv. Quantum Technol. 4, 2100005 (2021).  
83. Brown, R. & Twiss, R. Q. Correlation between photons in two coherent beams of light. Nature 177, 27-29 (1956).  
84. Hong, C. K., Ou, Z. Y. & Mandel, L. Measurement of subpicosecond time intervals between two photons by interference. Phys. Rev. Lett. 59, 2044-2046 (1987).

# Acknowledgements

We sincerely thank Shlomi Kotler for invaluable assistance in preparing this Perspective. Funding was provided by the Zuckerman STEM Leadership Program, the ISF-NRF Singapore Joint Research Program (grant no. 3538/20), and the Israel Science Foundation (grant no. 2497/21).

# Competing interests

The authors declare no competing interests.

# Additional information

Correspondence should be addressed to Yaron Bromberg.

Peer review information Nature Physics thanks Hugo Defienne and Andrew Forbes for their contribution to the peer review of this work.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Springer Nature or its licensor holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

$\odot$  Springer Nature Limited 2022, corrected publication 2023