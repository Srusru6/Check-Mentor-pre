# REVIEW SUMMARY

# OPTICS

# Dissipative Kerr solitons in optical microresonators

Tobias J. Kippenberg*, Alexander L. Gaeta, Michal Lipson, Michael L. Gorodetsky*

BACKGROUND: Laser frequency combs, which consist of equidistant laser lines, have revolutionized time-keeping, metrology, and spectroscopy. Conventional optical frequency combs based on mode-locked lasers are still mostly confined to scientific laboratories. In recent years, there has been progress in the development of optical frequency combs based on compact, chip-scale microresonators ("microcombs"), with such microcombs operating in the dissipative soliton regime. Dissipative solitons rely on a double balance of nonlinearity and dispersion as well as dissipation and gain and are an example of self-organization in driven dissipative nonlinear systems. Dissipative temporal solitons are providing the long-sought-for re

gime of coherent, broadband microcomb spectra and in addition provide an experimental setting in which to study dissipative soliton physics. Microcombs are now capable of producing coherent, octave-spanning frequency combs, with microwave to terahertz repetition rates, at low pump power, and in chip-scale devices and have been used in a wide variety of applications, owing to bandwidth and coherence provided by the dissipative temporal soliton states.

ADVANCES: Underlying these recent advances has been the observation of temporal dissipative Kerr solitons (DKSs) in microresonators, which represent self-enforcing stationary localized solutions of a damped, driven, and de

![](images/dbf57e60669a3dc3b2bc9488d890923394ec526eb22c28b8e88956b46a88a6fb.jpg)

![](images/17472fa0e2c4f7d5abfe631c21a6c2db0ee7a60cad22bb23729733a1037ecbdc.jpg)

![](images/361c27327b79f8cbe485a85dc1a74c2825736d2d387dbccea60c379832a8ba6a.jpg)

DKSs in optical microresonators. (A) Principle of DKSs, representing a double balance of dispersion and nonlinearity as well as (parametric) gain and cavity loss. (B) Optical field envelope of a single DKS, containing the localized soliton on top of a continuous-wave (CW) background field. (C) Graphic image of dissipative soliton formation in a CW laser-driven photonic chip-based microresonator, generating a continuously circulating DKS, which in frequency space corresponds to a coherent optical frequency comb. The optical frequency comb is shown with two dispersive waves that arise from higher-order dispersion.

tuned nonlinear Schrödinger equation, which was originally used to describe spatial self-organization phenomena. They correspond to solitons (localized patterns) in "open" systems—that is, systems that exhibit dissipation. DKSs, opposite to fiber solitons, therefore rely on a double balance of nonlinearity and dispersion as well as parametric gain and loss and depend on the laser-cavity detuning as a control parameter. Methods have been established that enable the reliable generation of such DKSs in a wide range of microresonator platforms, including platforms based on silicon nitride  $(\mathrm{Si}_3\mathrm{N}_4)$  that

# ON OUR WEBSITE

Read the full article at http://dx.doi.org/10.1126/science.aan8083

are compatible with photonic integration. In addition, a variety of previously unknown and nonanticipated soliton effects have been observed, such as soliton crystallization, Raman

Stokes solitons, and previously unseen soliton breather dynamics. Moreover, dissipative solitons have been shown to be surprisingly robust against imperfections in the resonator mode structure. Dissipative soliton states in microresonators have triggered a large number of applications, including in terabit-coherent optical communications, atomic clocks, ultrafast distance measurements, dual-comb spectroscopy, photonic integrated frequency synthesizers, and the calibration of astrophysical spectrometers for exoplanet searches.

OUTLOOK: The reliable generation of DKSs in microresonators has established a nascent research field at the interface of soliton physics, frequency metrology, and integrated photonics and provided impetus to microcomb sources. Emerging frontiers include using advances in nanofabrication and materials synthesis to realize ultralow-propagation-loss photonic nanostructures with unusual dispersion properties, which could explore dissipative solitons in new and unexplored parameter regimes and allow the synthesis of even broader spectra that in time domain could correspond to single-cycle pulses and whose spectral bandwidth could be extended to the mid-infrared or visible range. Beyond the narrow class of materials used for DKSs so far (Si,  $\mathrm{MgF_2}$ ,  $\mathrm{SiO}_2$ , and  $\mathrm{Si}_3\mathrm{N}_4$ ), many other materials exist with distinct advantages, such as III-V semiconductors, which are already widely used in light-emitting or laser diodes. Beyond existing applications, DKSs could be applied to optical coherence tomography, Raman spectral imaging, chip-scale atomic clocks based on optical transitions, or ultrafast photonic analog-to-digital conversion and have a potential to make frequency metrology and spectroscopy ubiquitous.

This list of author affiliations is available in the full article online.  
*Corresponding author. Email: tobias.kippenberg@epfl.ch (T.J.K); mg@rqc.ru (M.L.G.)

Cite this article as T. J. Kippenberg et al., Science 361, eaan8083 (2018). DOI: 10.1126/science.aan8083

# REVIEW

OPTICS

# Dissipative Kerr solitons in optical microresonators

Tobias J. Kippenberg $^{1*}$ , Alexander L. Gaeta $^{2}$ , Michal Lipson $^{3}$ , Michael L. Gorodetsky $^{4,5*}$

The development of compact, chip-scale optical frequency comb sources (microcombs) based on parametric frequency conversion in microresonators has seen applications in terabit optical coherent communications, atomic clocks, ultrafast distance measurements, dual-comb spectroscopy, and the calibration of astophysical spectrometers and have enabled the creation of photonic-chip integrated frequency synthesizers. Underlying these recent advances has been the observation of temporal dissipative Kerr solitons in microresonators, which represent self-enforcing, stationary, and localized solutions of a damped, driven, and detuned nonlinear Schrödinger equation, which was first introduced to describe spatial self-organization phenomena. The generation of dissipative Kerr solitons provide a mechanism by which coherent optical combs with bandwidth exceeding one octave can be synthesized and have given rise to a host of phenomena, such as the Stokes soliton, soliton crystals, soliton switching, or dispersive waves. Soliton microcombs are compact, are compatible with wafer-scale processing, operate at low power, can operate with gigahertz to terahertz line spacing, and can enable the implementation of frequency combs in remote and mobile environments outside the laboratory environment, on Earth, airborne, or in outer space.

S olitons are robust waveforms that preserve their shape upon propagation in dispersive media and can be found in a variety of nonlinear systems, ranging from hot plasma (1), ferrite films, fiber optics (2), cold atoms (3), hydrodynamics, and biology to cloud and sand dune formation. Although the initial promises of optical solitons for increased bandwidth of telecommunication were not implemented, dissipative solitons circulating in cavities of modelocked lasers (4) are actively used. Similar to the physics of open quantum systems, the "open" soliton systems—dissipative solitons (5)—are highly relevant to actual experimental systems, in which dissipation cannot be neglected. This is in contrast to the mathematical treatment of solitons that have focused on conservative, integrable systems. Dissipative solitons (5) balance loss and gain in an active media, along with the balance of nonlinearity and dispersion (Fig. 1). Although dissipative optical solitons are known to occur in mode-locked lasers (4), dissipative optical solitons can also occur in systems that have parametric gain—gain from four-wave mixing that is the underlying process that enables Kerr frequency comb (6, 7) formation in microresonators.

Such dissipative solitons sustained by parametric gain were first studied in fiber cavities (8). In 2014, it was observed that such dissipative Kerr solitons (DKSs) can spontaneously form in parametrically driven Kerr frequency combs in optical microresonators (9). In these systems, optical sidebands are generated by means of four-wave mixing processes (10, 11) and undergo a self-organization process that leads to the emergence of a soliton pulse train, which can mathematically and rigorously be mapped (12) to the Lugiato-Lefever equation (LLE) (13-15), an equation extensively studied in applied mathematics for decades.

The equation was originally developed to describe spatially localized pattern formation in driven nonlinear systems, in which it can lead to the formation of "dissipative structure." Since their observation in microresonators, such DKSs have been generated in a wide variety of microresonators, ranging from bulk crystalline (9, 16) and silica microdisks (17) to photonic chip-scale devices (17-20), under both continuous-wave (CW) and pulsed excitation (21). In the frequency domain, the pulse train constitutes an optical frequency comb (22-24). Such optical frequency combs, pioneered by using mode-locked lasers based on pulse trains, are key ingredients of optical atomic clocks and have proven invaluable for a wide range of scientific and technological applications [for example, reviewed in (25)]. Although optical comb technology has matured since its first introduction two decades ago based on mode-locked lasers, and is commercially available, such devices are typically not amena

ble to wafer-scale integration and have comparatively narrow line spacing in the hundreds of megahertz range. DKSs in microresonators have provided a route to compact low power in chirp-frequency comb generation. Although Kerr combs have been known for more than one decade (7) [and have been reviewed in (6, 26-28)], the discovery of the DKS regime (9) has unlocked their full potential by providing a route to broadband and fully coherent microresonator-based frequency combs, overcoming earlier challenges of low coherence (29-31). Such soliton-based microcombs in chip-integrated microresonators have achieved low-power, octave-spanning frequency combs in various spectral windows that now encompass the near-infrared (32, 33), telecommunication (34, 35), and mid-infrared spectral window (18, 36), with repetition rates from only a few gigahertz (37) to terahertz. The observation of DKS in microresonators yields a merging of soliton physics and high-precision frequency comb applications, stimulating a renaissance in dissipative soliton research and enabling many technological applications. Soliton microcombs have already been applied successfully to dual-comb spectroscopy in the near-(38-40) and mid-infrared (36), scanning comb spectroscopy (41), as well as the demonstration of a self-referenced comb for the counting of optical frequencies [both with (42) and without external broadening (43)]. Likewise, soliton microcombs have been used in massively parallel communication (44), in pairs at both the transmitter and receiver side, for low-noise microwave generation (45) as well as for chip-scale dual-comb-based light detection and ranging (LIDAR) (46, 47). Moreover, soliton microcombs have been used to realize an all integrated photonics-based chip-frequency synthesizer (48) and been used as a microphotonic astrocomb for exoplanet searches (49, 50). Soliton microcombs exhibit surprisingly rich nonlinear dynamics and have led to the observation of a variety soliton dynamics effects, such as bright soliton formation, dark pulses, flat-topped "platicons" formation (51), soliton Cherenkov radiation (20), Raman self-frequency shift (52-54), Stokes soliton (55), and breather solitons (56-60). Moreover, the inherently multimode nature of microresonators gives rise to new and unanticipated dynamics, such as avoided-crossing-induced dispersive wave formation (61, 62) or soliton-intermode breathing dynamics. Likewise, soliton crystallization (63) and switching (64) have been observed to occur. Today, a growing understanding of the nonlinear dynamics in soliton microcombs has been established, and new dynamics have been observed whose exploration continues to develop.

# Dissipative Kerr solitons

The topic of this Review is a soliton that has long been theoretically discussed (13-15) but only recently experimentally observed: temporal DKSs, in which losses in a passive nonlinear optical cavity are compensated by a parametric interaction via a CW external laser pump in a resonator containing a Kerr nonlinearity (10). Such DKS states, first studied in fiber cavities (8), have

$^{1}$ École Polytechnique Fédérale de Lausanne (EPFL), Institute of Physics, Lausanne, CH-1015, Switzerland.  $^{2}$ Department of Applied Physics and Applied Mathematics, Columbia University, NY 10027, USA.  $^{3}$ Department of Electrical Engineering, Columbia University, NY 10027, USA.  $^{4}$ Faculty of Physics, Lomonosov Moscow State University, Moscow, 119991, Russia.  $^{5}$ Russian Quantum Center, Moscow, 143025, Russia. *Corresponding author. Email: tobias.kippenberg@epfl.ch (T.J.K.); mg@rqc.ru (M.L.G.)

recently been discovered (9) as states in Kerr frequency combs (7). Although DKS formation has similarities to soliton mode-locking in femtosecond lasers, it does not require additional saturable absorbers to stabilize them, and they differ fundamentally because the pump laser frequency is a part of the soliton spectrum. The external coherent pump provides a central control parameter of the soliton and in addition constitutes one of the comb lines—which has no counterpart in conventional mode-locked lasers. Early interest in optical cavities filled with a nonlinear medium and pumped by means of CW source was initially stimulated by optical bistability and its application to optical switching (65), demonstrated by using iterative discrete-time input-output relations (known today as Ikeda map) so that such resonators exhibit multistability. However, it was found afterward (66) that this system can also support very localized optical pulses. If the intensity in the ring resonator changes only slightly per round trip, then the system can be described by a meanfield equation with periodic boundary conditions (67). If the medium has Kerr nonlinearity and quadratic dispersion, the mean field equation has the form of a nonlinear Schrödinger Equation (NLS) (68) with dissipative and driving terms. DKSs were first studied and observed with externally injected pulses (8). Although these experiments conjectured (8) that soliton formation may play a role, only later experiments revealed first evidence of such a regime, in terms of a transition from chaotic to low-phase-noise Kerr comb states (30), as well as evidence of pulse formation (which is consistent with a parameter regime allowing for soliton formation) (69). The first experiments that unambiguously identified DKSs in microresonators found DKS states by recording the transmission during Kerr comb formation. Strikingly, a series of steps on the red-detuned side of the resonance was observed. These steps, as is now well understood, are a sign of soliton formation and correspond to the continued reduction of the number of solitons in the cavity from  $N,N - 1$ , ... Stably accessing soliton states requires overcoming the thermal instabilities associated with the drop in intracavity power and led to the development of a wide range of techniques, so that now stably accessing Kerr soliton states can occur in a wide range of microresonator platforms.

The formation of DKSs in a crystalline microresonator are shown in Fig. 1 (9). A fundamental analytical property of DKSs is that they require a red-detuned pump laser from resonance, as also shown experimentally by using a Pound-Drever-Hall error signal. Although a red-detuned laser excitation in microresonators is conventionally unstable because of the thermal nonlinearity, the presence of a DKS can in turn self-stabilize the system for red detuning. This, however, necessitates overcoming transient thermal effects that are associated with the discrete steps in cavity transmission. Understanding and overcoming the thermal instability in the red-detuned solitonformation regime, as first accomplished with

![](images/54a7359794559fe4e2de45121a8fd53b74cd1296b0c04cc8e53b015c33edf811.jpg)  
A

![](images/e1da5aad3ae68408eb4ac62cbb3d5d11208d8291cc4a937a16e38308f980f9bc.jpg)  
B

![](images/02f12f87c3ccae11b1a40f681f92aa79fd977054d6176b1f886c11ed4ceac2bf.jpg)  
D

![](images/1d87cf202ffac84110467e1fc3ee93d71955476760cc413f305354f4b6f348a2.jpg)  
C

![](images/3a94a2e8a9bbefce1d9c1b31a72ec5ebe667e807e97acd6a8cb36341343c481c.jpg)  
Fig. 1. Soliton microcombs technology. (A) Graphic image of dissipative soliton formation in a CW laser-driven crystalline WGM microresonator, enabling conversion of a CW laser to a train of DKS pulses. (B) Principle of DKSs, representing a double balance of dispersion and nonlinearity as well as (parametric) gain and cavity loss. (C) Field envelope of a temporal soliton. (D) Experimental optical spectrum of a DKS in a crystalline  $\mathrm{MgF}_2$  resonator. (Inset) Detected microwave beatnote of the soliton pulse train. (E) Frequency-resolved optical gating spectrum showing localized optical pulses, separated by the soliton-microcomb line spacing. [Images are adapted from (9)]  
E

optimized frequency tuning schemes (9), has been a pivotal experimental technique to enable stable DKS formation in microresonators. Single DKSs can equally be accessed in fully planar architectures (70), notably in photonic-chip-based silicon nitride  $(\mathrm{Si}_3\mathrm{N}_4)$  resonators (71), despite the fact that this platform has a significantly lower quality  $(Q)$  factor and can exhibit dispersion imperfections and strong thermal effects. Photonic-chip-based microresonators based on  $\mathrm{Si}_3\mathrm{N}_4$  are amenable to wafer-scale manufacturing and integration and, because of their higher nonlinearity (compared with that of crystals or silica), enable broadband DKS (72) with high repetition rates  $(>100\mathrm{GHz})$ . Although tuning into soliton states in integrated  $\mathrm{Si}_3\mathrm{N}_4$  microresonators has also been achieved with a slow laser-tuning method (73), the strong thermal effects have lead to the development of different methods, such as "power kicking" (74), fast tuning by use of heaters (19), and most recently, use of single-sideband modulator schemes (75). Using these techniques, DKSs have been generated in a wide variety of microresonators, ranging from bulk

crystalline (9, 45) and silica microdisks (17) and microspheres (76) to photonic chip-scale devices in Si and  $\mathrm{Si}_3\mathrm{N}_4$  (20, 77) and fiber cavities (21), under both CW and pulsed excitation (21). Moreover, schemes have been devised for soliton feedback stabilization, based on the soliton power (78), or by using the effective laser detuning of the soliton state (79).

# Dissipative soliton regime in Kerr frequency combs

We briefly review the physics of the parametric process in microresonators, discussed in detail in (30, 80). Kerr frequency combs were initially discovered in silica microtoroids, and experiments proved that the parametrically generated (11, 81) sidebands were equidistant to at least one part in  $10^{-17}$  as compared with the optical carrier. In these early experiments, the combs repetition rate was in the terahertz range, and a femtosecond-laser frequency comb was used to bridge and verify the equidistant nature of the teeth spacing. It is today understood that such highly coherent combs only exist in certain regimes.

# Physics of Kerr comb formation

The resonance frequencies of a microresonator can be Taylor-expanded around the pumped mode  $\omega_0$  so that

$$
\omega_ {\mu} = \omega_ {0} + \sum_ {j} D _ {j} \mu^ {j} / j! \tag {1}
$$

where  $D_{1} / 2\pi$  is the mean free spectral range (FSR),  $D_{2}$  is the group velocity dispersion (GVD) (positive for anomalous GVD), and  $j \in Z$ . If the FSR (because of  $D_{2}$  in Eq. 1) increases with frequency, the resonator has anomalous GVD, as required for parametric oscillations and soliton formation. It is often useful to introduce the integrated dispersion, which describes the deviation of a given resonance from an equidistant frequency grid,

$$
D _ {\text {i n t}} (\mu) = \omega_ {\mu} - \left(\omega_ {0} - D _ {1} \mu\right)
$$

For a microresonator with anomalous GVD, the third-order Kerr nonlinearity leads to a nonlinear coupling between different modes. The nonlinear coupling coefficient  $g = \hbar \omega_0^2 cn_2 / n^2 V_0$  is defined as a Kerr frequency shift per photon;  $n$  and  $n_2$  are the refractive and nonlinear optical indices, respectively;  $V_{0}$  is the effective (nonlinear) volume of the pumped mode; and  $c$  is the speed of light.

Parametric oscillation (11, 81)—the emergence of symmetrically spaced signal and idler sidebands around the pump—occurs when the parametric gain exceeds the cavity decay rate. The threshold condition is equivalently understood as a Kerr-induced shift that is comparable with the cavity decay rate and thus the onset of cavity bistability  $(g\cdot \bar{n}_c\sim \kappa /2$  where  $\bar{n}_c$  is the number of photons in the mode). Unlike conventional lasers in which the threshold (11, 81) scales as  $\propto V_0 / Q$  the threshold for parametric oscillation scales with  $\propto V_0 / Q^2$  ,which highlights the dramatic reduction of parametric threshold possible for ultrahigh-  $Q$  microresonators. When scanning the laser into resonance from the blue-detuned side (Fig. 2C), the first pair of sidebands that oscillate are those that are closest to the maximum of the parametric gain curve. The sideband number is approximately

$$
\mu_ {i} \approx \sqrt {\frac {\kappa}{D _ {2}}}
$$

If this distance corresponds to one single FSR, the subsequent cascade leads to fully coherent frequency combs. Such combs are referred to as "natively spaced comb," "Turing rolls," or (coherent) modulation instability (MI) combs.

This coherent operating regime was initially observed in optical silica microtoroids (7). The coherence in these systems is achieved because the comb formation leads to a native comb, whose spacing corresponds to a single FSR. In this scenario, one can create fully coherent and relatively broadband-frequency combs, which has been the case for toroid resonators in the telecommunication band or crystalline resonators in the mid-infrared spectra range (82), and generally integrated resonators with a large FSR (31), which lead to a large accumulated dispersion parameter  $D_{2}$ . Not all platforms, however, yield intrinsically low phase noise. It was observed that the comb formation can give rise to low coherence states—in particular, in integrated platforms based on, for example,  $\mathrm{Si}_3\mathrm{N}_4$ , Hydex glass, Si, AlN, or AlGaAs. Counterintuitively, however, even for ultrahigh-  $\mathbf{Q}$  resonators, such as crystalline resonators or silica disks, low coherence was observed, which is associated with subcomb formation.

# Subcomb formation and chaotic comb states

In the case of resonators that have low  $Q$  (such as  $\mathrm{Si}_3\mathrm{N}_4$  and other integrated resonators) or low dispersion (such as  $\mathrm{MgF}_2$  crystalline resonators

![](images/0e0cca95df63b2159e5fc78414c86d0eb02a793fde8ced12f8a2efa600123094.jpg)

![](images/a18cc034588a47b748e85ca5e15ae672b914ac6efeb6a27e197984479f41e784.jpg)

![](images/7719c0496dd475eb70b4d3eff2d60468170ac9cebbd867c79c0d1ca4e32e74cd.jpg)

![](images/13a25095758148c057b032c629a9f05cd363839b935cd2c38b96aa63b35cb66e.jpg)

Fig. 2. Numerical simulations of DKSs in optical microresonators.  
![](images/79d0e3bb3317537097bff867050af0bab924a4e3b58f20c9a49cac516c71edb8.jpg)  
(A) Temporal and spectral input and output from a CW laser-driven resonator supporting DKS. (B) The mode proliferation in the case of a resonator that exhibits subcomb formation, with eventual transition to DKS. (C) Intracavity field as a function of the laser detuning. Shown are the regions of modulation instability (marked "1"), breather soliton (yellow,

![](images/5d0ae107453525ebcb3382356372ee6638e256bfd758a29ea22e21e3ec8489ae.jpg)

![](images/b0180df1e6fc9a3ef83e938807fc481f377674488e4a0fb60b38688b3d496d64.jpg)  
marked "2") and stable soliton formation (green, marked "3" to "5"). Different trajectories corresponding to multiple simulations are shown in yellow (bold line). The different steps designate transitions between different soliton states. (D) intracavity waveform corresponding to the different chaotic MI, breather solitons, and stable DKS states. [Images are adapted from (9)]

in the telecommunication band), the first pair of sidebands (generated when scanning a pump laser into resonance from the blue-detuned side) are separated by many FSRs, which leads to the formation of subcombs (because  $\mu_{i} = \sqrt{\frac{\kappa}{D_{2}}}\gg 1$ ).

In this process, depicted in Fig. 2, first a primary comb is generated with a line spacing  $\Delta$ . Upon increasing pump power, secondary sidebands around the primary sidebands are generated, leading to the formation of subcombs. The initial subcombs all share the same repetition rate  $\delta$ . Importantly, the primary and secondary spacing do not need to be commensurate. Therefore, once the pumping power is further increased, the subcombs merge and lead to the counterintuitive situation in which more than one single comb tooth can occupy a cavity resonance (30). This scenario leads the comb to exhibit beatnotes that can exhibit multiplets, which for sufficiently strong pump power merge into broad beatnotes. This comb state therefore exhibits low coherence, making it unsuitable for metrology. Although the comb spectral envelope of these combs is recorded with an optical spectrum analyzer to be spectrally smooth, the underlying intracavity waveform in the chaotic MI regime is vastly varying. Many early reported comb spectra (including photonic integrated resonator platforms or crystalline resonators in the telecommunication band) are chaotic in origin and exhibit low coherence. It was first demonstrated in  $\mathrm{Si}_3\mathrm{N}_4$  microresonators (30) that transitions to low noise also exist. Such a transition to low noise state was shortly thereafter also observed in silica resonators (83), and evidence was found that the coherent regime is concomitant with pulse trains (69). These results indicated that the major challenge and roadblock of high noise could be overcome, unlocking the full potential of chip-scale frequency combs. Today, it is understood that these transitions are

likely associated with DKSs (9, 13, 15), which give rise to coherent comb states. Indeed, although the LLE provides an accurate description of soliton states, many phenomena require corrections beyond the established models and are to be explored in Kerr microresonators.

# Transition to the DKS regime

An unusual and unexpected observation was experimentally made in crystalline resonators (9) when analyzing the scan across the cavity resonance during the comb formation process: an unusual set of discrete step-like behavior in the transmitted power occurred, which exhibited a remarkably regular and repeatable step height. Transient measurements of the comb's beatnote in this regime showed low phase noise, indicating a coherent comb-formation regime. This observation confirmed an earlier theoretical prediction (84) that used numerical simulation of the laser-pump scan based on the coupled-mode equations (CMEs) (85). These simulations (9) equally revealed that during the laser scan across the resonance, unexpectedly sharp and discrete step-like transitions to low-noise states appear (Fig. 2). The numerical simulation predicted that the regions with discrete steps are associated with solitons inside the cavity, and the discrete steps in the transmission trace are associated with the annihilation of individual solitons, one by one. The numerical simulation uses the bare cavity detuning as a parameter, which does not correspond to the actual (effective) detuning from the resonance because of the Kerr frequency shift caused by the pump. Actual soliton formation can only occur when the laser transitions to the red-detuned side of the cavity resonance, where the intracavity field is bistable (Fig. 3A). The simulation reveals the primary sidebands, subcomb formation, and chaotic MI, followed by the formation of stable DKS inside the cavity. The

numerical simulation was repeated multiple times, and the yellow curves in Fig. 3A show the evolution of all possible trajectories, whereas blue denotes the numerical simulation of a single laser scan trajectory. Although numerical simulations of dissipative solitons using a mean field model equation (the LLE) have been carried out extensively, simulations of the actual laser scanning process relevant to the microresonator case are a new development and pivotal in the understanding of DKS. The simulations also predicted the existence of a single soliton state with a  $\mathrm{sech}^2$  spectral envelope (Fig. 2D). These predictions are in agreement with experiments. Although MI occurs for the effectively blue-detuned region, the regime of soliton formation occurs in the bistable regime where two solutions exist—where the laser is effectively red-detuned (Fig. 3A). Experimentally, this can be verified by using a Pound-Drever-Hall error signal, which can differentiate between effective red- and blue-detuning (Fig. 3A).

# Stably accessing DKS in the presence of thermal nonlinearity

Accessing the DKS is in practice compounded by thermal effects. A fundamental consequence of the existence of bright solitons is the operation in the bistable regime, which causes the optical pump to be effectively red-detuned from the (Kerr and thermally shifted) cavity resonance. Although blue-detuned excitation is thermally stable—the resonator and laser form an autonomous feedback loop that stabilizes the laser cavity detuning—the opposite is true for a red-detuned operation (required for soliton formation) (86). Moreover, the series of discrete steps in resonator transmission laser scan due to soliton formation compound the stable access of solitons because concomitant with a discrete step is a change in intracavity power and, as a consequence, temperature change. This in turn, via

![](images/d41560ff1f47377cd10b8ec0e781d0a60ffbd4bf60568c10875c87a4507dec2c.jpg)  
Fig. 3. Transition to the dissipative soliton states and soliton crystals. (A) (Top) The cavity bistability in the intra-cavity power due to the Kerr nonlinearity. (Bottom) The integrated dispersion profile  $[D_{\mathrm{int}}(\mu)]$  of a measured progression of resonances exhibiting anomalous dispersion (quadratic variation of the integrated dispersion). (Middle) A series of steps on the red-detuned side of the resonance, indicative

![](images/f6bbabff6cbb677a9a32955a21c74c63f8fc2be4462bb684bdd830d9f1b921ae.jpg)  
of dissipative soliton formation. (B) The evolution of the intracavity power as a function of laser detuning, revealing in particular a series of discrete steps associated with soliton formation. (C) More complex arrangements of a large number of solitons that are ordered in crystals (63, 134) but that contain defects, such as vacancies or defects. [Images are adapted from (9, 63)]

![](images/b3063109680dca5a8f56d5d87f360e9eeae7d27eff3e8bc73bb4cfb7c9bcca6e.jpg)

the thermal effect (temperature-dependent refractive index), changes the relative laser cavity detuning. In early work, this challenge was overcome by using an optimized laser scan (9). Since then, several techniques have been developed, from "power kicking" (74) to very fast laser modulation using single sideband modulators (75), as well as fast thermal on-chip tuning (19) and carrier injection (77). All developed techniques have in common that once the DKS state is reached, the thermal response of the cavity is dominated by the DKS, causing the system to be self-stabilized in the presence of a red-detuned (typically several linewidth) strong pump field. This is due to the fortuitous circumstance that thermal effects make accessing the soliton state more difficult; once the solitons are generated, the thermal nonlinearity induced by the soliton self-stabilizes the laser-cavity detuning, constituting an autonomous feedback loop. Once accessed, DKS in microresonators can be passively stable for hours. Another useful feature of the DKS regime is that if probed with a modulated laser, the soliton state (64) exhibits two resonances: a  $\mathcal{C}$  and  $S$  resonance, which correspond to the modulation response of the cavity and solitonic solution and reveal the effective laser detuning. Experimentally, the detuning of the laser determines the soliton duration, in which detuning further from resonance decreases

the soliton duration, until the point at which the soliton existence range limit is reached (Fig. 2C, green region). In addition to continuous wave pumping schemes, pulsed pumping can be used. Although the generation of the Kerr soliton microcombs can occur at record low power [tens of milliwatts have been reported for octave spanning spectra (48)], the efficiency of the process is low because of the detuned nature of the pump during the DKS formation. Periodic pulsed pumping at a frequency similar to the cavities' inverse round-trip time can enhance this efficiency by approximately the ratio of the round-trip time to the pulse duration. This scheme was recently shown for DKSs in fiber cavities (21), exhibiting a locking behavior to the drive pulse and leading to a substantial increase in the conversion efficiency. This scheme also has been demonstrated for  $\mathrm{Si}_3\mathrm{N}_4$  microresonators for efficient and broadband comb generation (49). Because of the higher efficiency of pulsed pumping, thermal effects are suppressed, making tuning to the DKS state possible by using slow laser scans.

# Theoretical modeling and numerical simulations of DKS in microresonators

Kerr comb formation can, in addition to CMEs described above, also be described by a mean field. The two descriptions are equivalent, but only the latter enables a connection to the soliton

to be established. The internal optical field envelope  $A(\phi, t)$  in a microresonator with a self-focusing Kerr nonlinearity and only second-order GVD may be described with the LLE (12, 13, 16, 72), where  $\phi$  is the angular coordinate in a ring resonator in a frame copropagating the envelope with the group velocity, and  $t$  is the slow time (slower than the round trip)

$$
\frac {\partial A}{\partial t} - i \frac {D _ {2}}{2} \frac {\partial^ {2} A}{\partial \phi^ {2}} - i g | A | ^ {2} A + (\kappa / 2 + i \Delta) A = \sqrt {\eta \kappa s} \tag {2}
$$

Here, the input laser power is given by  $P = \hbar \omega_0 |s|^2$ ,  $\eta = \kappa_{\mathrm{ex}} / \kappa$  is the coupling efficiency determined as a ratio of the output coupling rate  $\kappa_{\mathrm{ex}}$  to the total loss rate  $\kappa$  ( $\eta = 1/2$  corresponds to critical coupling, and  $\eta \approx 1$  corresponds to strong overcoupling),  $h$  is the reduced Planck's constant, and  $\omega_0$  is the pumped optical frequency.  $D_1$  falls out from the equation in transforming to a rotating frame  $\phi = \varphi - D_1 t$ , consideration of terms with  $j > 2$  leads to appearance of higher-order derivatives in Eq. 2, and  $\Delta = \omega_0 - \omega$  is the pump detuning. It is convenient to switch to a dimensionless equation

$$
i \frac {\partial \Psi}{\partial \tau} + \frac {1}{2} \frac {\partial^ {2} \Psi}{\partial \theta^ {2}} + | \Psi | ^ {2} \Psi = \zeta_ {0} \Psi - i \Psi + i f \tag {3}
$$

![](images/2e38bf9db5fa8d46637c601e3084198d6474425af2df0752f67f56584152e028.jpg)

![](images/4a45e14bf44bfb386d956f0d7f0338361ee9871a594c6da427202694fc9b84cb.jpg)

![](images/2acdc8b18608e07ca7ad70bdd8e28dee551b68ce11f76b9ffe0f1bd84a9e3e5e.jpg)  
Wavelength  $\lambda$  
Wavelength  $\lambda$  
E  
Frequency (THz)

![](images/9719a83764dfa999a09c0e1e38838554137ea2c588e1e3ceb785a5de434580f6.jpg)  
Wavelength (nm)

![](images/9f1e945e60b470e4178403ca4eb3870ea9db54a36ddaaf1c27b71090924c8668.jpg)  
Fig. 4. Dispersion engineering in photonic chip-based integrated waveguides and resonators. (A and B) Effective refractive index of a photonic integrated waveguide as a function of wavelength, revealing that tight confinement waveguides give rise to anomalous group velocity dispersion (positive curvature of the effective index curve). By contrast, weak confinement leads to normal GVD. (C) Shown is the measured integrated dispersion

![](images/856b43a2e2947e4ce0360e7e7d7be78bbdb5c6544a0c04e25ad9e80ea5c87f28.jpg)

![](images/6d6d316dc61a4106eecf752e99144c82fbd2fe25f718d329754966609f95ecf5.jpg)  
parameter  $D_{\mathrm{int}}(\mu)$  of a  $\mathrm{Si}_3\mathrm{N}_4$  microresonator by use of frequency comb-assisted spectroscopy, revealing purely anomalous GVD. (D) Engineering of the GVD of a  $\mathrm{Si}_3\mathrm{N}_4$  waveguide cladded with silica, opening an anomalous GVD window in the telecommunication band (98). (E) Integrated microresonator platforms showing Kerr comb formation to date, including diamond, AlGaAs, silica on silicon, and  $\mathrm{Si}_3\mathrm{N}_4$ . DKSs have been generated in silica,  $\mathrm{Si}_3\mathrm{N}_4$ , and Si.

![](images/e2fa2eb02f243e04f174b15415e5835324216be099a62a5a37946117264a22e4.jpg)

![](images/4470c0b1877b0488e2df550acd8a65e6355a1df97dcb388bf9ee54e9919bcd32.jpg)

$(\theta = \phi \sqrt{\frac{\kappa}{2D_2}},f = \sqrt{\frac{8g\eta P_{\mathrm{in}}}{\kappa^2\hbar\omega_0}},\Psi = \sqrt{\frac{2g}{\kappa}} A,\zeta_0 = 2\Delta /\kappa ,$ $\tau = \kappa t / 2)$  .Without the right part, Eq.3-known as the nonlinear Schrodinger (NLS) equation-is integrable with a sech-shaped soliton solution (87). An exact stationary solution of Eq. 3 in the form of solitonic pulses on CW background is also known (14, 88, 89), when only a driving term without losses is considered. Although this solution provides a good approximation in the limit of large detuning  $\zeta_0$  it gives little insight in the understanding of the DKS dynamics without num

erical simulations and asymptotic approximations. The damped driven NLS (Eq. 3) is frequently referred to as the LLE (13), an important equation first introduced to describe two-dimensional spatial transversal solitonic field patterns in nonlinear Fabry-Perot etalons and later reformulated for longitudinal temporal solitons (15). The same longitudinal equation was, however, earlier analyzed in application to plasma physics (90, 91), where solitons on background and existence boundaries were found.

In (85), an alternative approach for Kerr comb simulation was proposed on the basis of discrete analysis of each comb line nonlinearly coupled with all others. The system of equations in this way may consist of hundreds of CMEs with millions of nonlinear terms that nevertheless can be efficiently numerically integrated by using the fast Fourier transform (92). The CME description is equivalent to LLE (11) and may be considered as its discrete Fourier transform. The CME approach is useful to analyze dynamics for each

![](images/20fc1b868c91107ba9141508c445b44b17c23dd25a8d6419add30a46654388d0.jpg)  
A

![](images/b05f962a95b80b567b5c2e6b449ab7e6bf66fe353dc9eb940c221a76bd563716.jpg)

![](images/ffb2130d036fedbe905298ab8e7315106ff8c5dbec1cc20e788765c38dda8bb3.jpg)

![](images/fb93088ebe410ef00d801884a3ff2b9f92d8cd5f6508545bd47216c4e1281d4a.jpg)

![](images/210748eb0aed8fc91b776534bca895f46ec49cc30b07d1ceba1ead631324a6d9.jpg)

![](images/6be290a19eb65027e97fed463817774db0036717d0a38a7be2cd2f3810910670.jpg)

![](images/ae1831802c7643cfd37327efbc6d743d8848195dbdff7dadf64af6c29a2fed5c.jpg)

![](images/c433d1969841e29126532bcffa27d5eda3fa38df93c1452bd73b2dc1b042fde5.jpg)

Fig. 5. The influence of dispersion and Raman effect on DKS.  
![](images/9f49d6761542faff68f691400c198050ce490aba3bd3473405a1a2035d3a7035.jpg)  
(A) A nearly purely quadratic dispersion (anomalous GVD)—dominated DKS generated in a crystalline microresonators. (B) Soliton-induced Cherenkov radiation—a soliton whose spectral envelope encompasses the normal GVD regime. A dispersive wave is emitted where the phase

![](images/bc885fdecab96e2ebd94bc13c8f9f798adaf517829fb4a584308d7a6d714e829.jpg)  
matching condition  $[D_{\mathrm{int}}(\mu) = 0]$  is satisfied. (C) A spectrum with dual dispersive waves, covering a full octave in a  $\mathrm{Si}_3\mathrm{N}_4$  microresonator with terahertz mode spacing. (D) A platicon state (dark pulses) generated in the normal dispersion regime. (E) A Raman soliton, generated from the single soliton state in a silica microdisk.

![](images/1b3293be8e7e59c50073230ed9a0cb5647ab54c080a7666e3dc4fc32b0eb3312.jpg)  
Fig. 6. Applications of soliton microcombs. Applications of areas of microcombs (from top, clockwise): ultrafast dual soliton microcomb distance measurements (LIDAR) (46), chip-scale atomic clocks, photonic Radar (135),  
dual-microcomb spectroscopy (38), optical coherence tomography, low-noise microwave generation (45), integrated optical frequency synthesizer (136), and astrophysical spectrometer calibration for exoplanet detection (49).

comb line and also in cases in which local dispersion for particular lines is perturbed and not easily described by the Taylor series (61).

# Microresonator platforms for soliton formation

Soliton Kerr frequency combs in microresonators were first observed (9) in crystalline  $\mathrm{MgF_2}$  resonators (45, 93) with ultrahigh-  $Q$  factor, leading to a low threshold for nonlinear effects (94). The platforms in which solitons can be generated have been extended significantly and include platforms that are amenable to wafer-scale processing, such as silica microdisk resonators (17) and photonic integrated platforms, notably  $\mathrm{Si}_3\mathrm{N}_4$  (19, 20, 95, 96). Such photonic chip-based resonators based on  $\mathrm{Si}_3\mathrm{N}_4$  enable integration of waveguides and resonators, enable further functionality such as heaters, and are space compatible (70). Moreover, solitons have been generated in Si microresonators in the mid-infrared (77), where two-photon absorption is negligible. A challenge in this case is attaining sufficiently high

$Q$  for efficient nonlinear parametric frequency conversion.

One platform that is particularly well suited is based on  $\mathrm{Si}_3\mathrm{N}_4$  a material that is already a part of the complementary metal-oxide semiconductor (CMOS) process, for the strain engineering of transistors and as a capping layer. Its high refractive index of  $n\approx 2$  enables tight optical confinement waveguides and microring resonators, and the high bandgap  $(\sim 3\mathrm{eV})$  mitigates multiphoton absorption in the telecommunication band. Recent measurements have revealed that  $\mathrm{Si}_3\mathrm{N}_4$  has intrinsic material limited  $Q$  -factors that can exceed  $10^{7}$  (97). Although the  $Q$  -factors attained in  $\mathrm{Si}_3\mathrm{N}_4$  are still substantially below those of crystalline resonators, the significantly tighter optical confinement and higher Kerrnonlinearity have allowed DKS generation. Moreover, DKSs have been observed in fiber Fabry-Perot microcavities (21). Although more platforms exist in which Kerr comb generation has been shown-including, in particular, compound semiconductors such as AlGaAs or AlN

soliton formation has to date not been demonstrated in these materials. Irrespective of the platform or material used, a requirement for soliton formation is attaining anomalous group velocity dispersion. As one approaches the bandgap of the material, the normal GVD will start to dominate. This limitation has been overcome with waveguide geometry-based dispersion engineering (98).

# Dispersion engineering

Optical microresonators exhibit variation of the FSR because of the effect of material and geometric (resonator) dispersion. Material dispersion, commonly expressed via the Sellmeier equations, poses stringent limits on the wavelength range in which anomalous GVD is possible. By contrast, the resonator dispersion can be engineered via the resonator geometry and can be engineered to be anomalous GVD, overcoming the inherent material dispersion (98). For a nanophotonic waveguide, the dependence of the effective refractive index on the wavelengths leads inherently

to normal GVD when the mode is weakly confined and to anomalous GVD for tight confinement. This is illustrated in Fig. 4 and has been applied to achieve Kerr comb generation in  $\mathrm{Si}_3\mathrm{N}_4$  despite the material having normal material dispersion (71). Moreover, coatings can be used to further engineer dispersion properties (99). A limitation arises from the whisperinggallery mode (WGM) potential induced normal GVD for small waveguide radii (99). The comb bandwidth can be significantly extended when making use of higher-order soliton broadening effects. If higher-order dispersion terms are significant, and the comb extends into regions where the dispersion changes sign, the comb bandwidth will be significantly extended. (20, 35, 72, 100-103). Comb lines near zeros in the integrated dispersion profile (Fig. 3A) form dispersive waves coupled to solitons also known as soliton Cherenkov radiation (103-106). An analogous effect may occur because of dispersion perturbation induced by mode coupling (62, 106). Proper design of the resonators (73) also allows for suppressing the nonfundamental modes that, because of mode couplings with multiple avoided mode crossings (61), may prevent generation of solitons. Because of the very short duration of the DKS in microresonators, the LLE needs to be generalized to include higher-order dispersion (72, 105), Raman scattering, and self-steepening terms (107-109) to describe the soliton microcombs.

# Dispersive waves in DKS

For solitons whose spectral bandwidth extends into the normal GVD regime, the LLE has to be extended with higher-order dispersion terms. This gives rise in particular to the effect of soliton-induced Cherenkov radiation, also known as dispersive wave formation. This process was first described for supercontinuum generation in optical fiber (104) and applies also to DKSs in optical microresonators (72). In this case, the soliton develops an oscillatory tail, on the trailing or leading edge of the pulse. The spectral location of this dispersive wave corresponds approximately to the condition where  $D_{\mathrm{int}}(\mu) = 0$ , where the resonator FSR matches that of the dispersionless soliton. Dispersive waves offer the practical advantage that they enable extension of the spectral coverage of the soliton Kerr comb to the normal dispersion regime and increase the power in the spectral ends of the comb. Suitable quartic dispersion enables also the creation of DKSs with two dispersive waves that can cover a full octave (Fig. 5C). The soliton Cherenkov radiation also entails a spectral recoil (105, 110).

# Raman effect in DKS and the Stokes soliton

The Raman effect is particularly relevant in amorphous media such as silica or  $\mathrm{Si}_3\mathrm{N}_4$  but has been observed to be negligible in crystalline material of  $\mathrm{MgF_2}$  because of the narrow Raman gain bandwidth. The Raman effect leads to a Raman self-frequency shift: a soliton that is shifted with respect to the pump [also called frequency-locked Raman soliton (53)]. The Raman

effect can also lead to a new type of soliton, the Stokes soliton, which is a soliton generated by the Raman gain and locked to the pump soliton (Fig. 5E) (55). Recently, it was also shown that DKSs experience a limitation on their temporal duration and bandwidth because of the stimulated Raman scattering (111), once the comb spacing is less than the Raman gain bandwidth. In addition, it was shown that in the presence of a large Raman gain (such as in diamond), comb generation can only occur if the FSR is sufficiently large to suppress Raman lasing.

# Counterpropagating solitons and spatial multiplexing

WGM microresonators support both counterpropagating traveling modes, which allows simultaneous excitation of DKS in both clockwise and counterpropagating directions (112, 113). The two combs, however, have been observed to lock to each other, an effect likely associated with Rayleigh backscattering. Such locking was recently demonstrated and enables the creation of two phase-locked pulse streams of soliton Kerr combs, which can be used for dual-comb distance measurements (47). Such dual-comb soliton pulse streams can also be generated by using spatial multiplexing of solitons—the generation of DKSs in several spatial mode families of one and the same resonator (114).

# Normal dispersion solitonic pulses

The LLE also exhibits solutions for normal GVD, a solution known as dark soliton (short dip in CW background). However, because of periodic boundary conditions, purely dark solitons with opposite sign of phase on both sides are impossible in microresonators, whereas low-contrast gray solitons have a quite narrow, hardly achievable range of existence (115, 116). Nevertheless, mode-locked Kerr frequency combs in the normal dispersion regime were experimentally demonstrated in different materials (117-120). It was revealed by using numerical simulations that these experimental results may be interpreted by use of a type of solitonic pulses called "platicons," flat-topped bright or dark (depending on the duration) pulses that can be softly excited and stably exist in microresonators with normal dispersion in case of bichromatic or amplitude-modulated pump (120) as well as with a local dispersion perturbation (51). In real microresonators, such a perturbation may occur because of the normal mode coupling between different mode families (119, 122). Platicons represent bound states of opposing switching waves (123) that connect upper and lower branches of bistable resonance to satisfy periodic boundary conditions. They may be identified in experiments because of their characteristic optical spectrum with pronounced wings (Fig. 5). In (124), it was demonstrated that the dynamics of platicons in the presence of the third-order dispersion is quite peculiar and drastically different from bright solitons. In (125), a possibility of stable coexistence of dark and bright solitons in case of nonzero third-order dispersion was revealed.

# Applications of DKSs

Accessing DKSs in microresonators has unlocked in a short timeframe several promising applications. The ability of DKSs to generate broadband-coherent combs with gigahertz repetition rates and short pulse streams has a number of applications in which either compactness is required or the high repetition rates are advantageous (Fig. 6).

# Microwave-to-optical link

Soliton Kerr microcombs have enabled the counting of the cycles of light by creating a direct microwave-to-optical link, by using self-referencing assisted with external fiber-based broadening (42, 126) and by directly exploiting the broadband nature of DKS (43).

# Optical frequency synthesizers

DKSs based on a dual-comb approach have been used to create an integrated optical frequency synthesizer that allows synthesizing an optical frequency from a radio-frequency reference (48).

# Massively parallel coherent communications

Kerr combs with hundreds of equally spaced lines can serve as a reference for wavelength division multiplexing in massively parallel coherent telecommunications, with demonstrated data rates exceeding 50 terabits per second, at both the receiver and transmitter ends (44).

# Dual-comb spectroscopy

Two slightly different frequency combs can form on a photodetector a radio-frequency comb (25), with the repetition rate equal to both combs' optical repetition rates difference. DKSs have been used for such dual-comb measurements in both near- and mid-infrared (37-40) and allow even full integration on chip.

# LIDAR

Dual-microcomb may be implemented for ultrafast distance measurements with submicrometer resolution (46), using counterclockwise solitons (47).

# Low-noise microwave generation

Soliton Kerr microcombs can also be used for compact ultrastable microwave generation, especially if augmented with compact atomic cell references (126, 128).

# Astrophysical spectrometer calibration

The large line spacing makes DKSs ideal for calibrating astrophysical spectrometers for exoplanet searches. In contrast to conventional laser frequency combs that require filtering, this is not necessary for DKSs. Recent work demonstrated that DKSs provide calibration sufficient for search of Earth-like planets (49, 50).

Beyond these already demonstrated applications, there is application potential in several domains, in particular for the visible range. Optical coherence tomography, dual-comb coherent anti-Stokes Raman spectroscopy (129), or photonic microwave signal processing (130) are obvious

new directions, but qualitatively and quantitatively new nonlinear physics and devices are expected when advancing the ability to engineer dispersion over broad bandwidth in photonic chips and, when investigated, more complex photonic devices and geometries, such as photonic band-gap waveguides and cavities.

# Further developments and outlook

The fast progress in recent years—in the understanding of soliton formation, the broad range of platforms in which solitons in driven dissipative nonlinear microresonators have been generated, and the rapid rise of applications and proof of concepts—indicate a fruitful playground for future progress. Yet challenges exist, in particular toward making the technology viable: increasing bandwidth of solitons, increasing the efficiency, and increasing the photonic integration. Moreover, despite decades of research, integrated photonic resonators presently still exhibit propagation losses that are more than three orders of magnitude higher than those of standard optical fibers. Overcoming this challenge would allow dramatic improvements in power efficiency and likely requires further research in photonic materials and fabrication processes. Several areas can be identified that may offer advances and new avenues both technological in nature as well as fundamental, such as new and improved materials and new platforms. Although the advances cannot be predicted, several developments can be anticipated.

# Advanced dispersion engineering and new nonlinear materials

The coherent synthesis of an even broader spectrum, possibly corresponding to single-cycle pulses, depends critically on dispersion engineering. Dispersion engineering may open single or even subcycle waveforms inside dielectric resonators, as well as new coupled soliton complexes. Such advanced dispersion engineering is in its infancy at present and could use multilayer coatings, more complex waveguides that use coupled resonators or photonic crystal waveguide geometries, or combinations of existing materials. To date, solitons have been generated in a small class of materials  $\mathrm{(MgF_2}$ $\mathrm{Si}_3\mathrm{N}_4$  Si,and  $\mathrm{SiO}_2)$  ,and evident potential exists when using III-V semiconductors in particular, which offer atomic-scale deposition processes and tailored band gap (131). Likewise, solitons are surprisingly stable attractors-and are robust to dispersion disorder. This could enable machine-learning algorithms to design complex highly multimode systems, whose composite mode coupling induced a broadband desired dispersion landscape that supports solitons. If achieved, it may become possible to engineer arbitrary and much more complex and flat dispersion landscapes that could host multiple a-GVD-hosted soliton complexes.

# Quantum technology

A further area under exploration is the use of parametric interactions, a process that is capable of generating correlated pairs of photons

for the generation of quantum states. One application lies in generating quantum random number generation using optical parametric oscillations (132). Moreover, the parametric fluorescence in Kerr nonlinear microresonators has already been successfully used for correlated photon states and higher-order correlated photon states (133). Beyond technological advances outlined above, there are also fundamental open questions. An emerging question is the behavior of coupled parametric soliton arrays. The behavior of such driven, dissipative, nonlinear systems is an emergent question that is also experimentally accessible and may give rise to unanticipated effects. These possible advances reveal that DKS-based microcombs may offer advances to a wide range of areas, from timekeeping and spectroscopy to sensing and telecommunications, and are emerging as candidate building blocks in tomorrow's photonic technologies.

# REFERENCES AND NOTES

1. N. J. Zabusky, M. D. Kruskal, Interaction of "solitons" in a collisionless plasma and the recurrence of initial states. Phys. Rev. Lett. 15, 240-243 (1965). doi: 10.1103/PhysRevLett.15.240  
2. L. F. Mollenauer, R. H. Stolen, J. P. Gordon, Experimental observation of picosecond pulse narrowing and solitons in optical fibers. Phys. Rev. Lett. 45, 1095-1098 (1980). doi: 10.1103/PhysRevLett.45.1095  
3. K. E. Strecker, G. B. Partridge, A. G. Truscott, R. G. Hulet, Formation and propagation of matter-wave soliton trains. Nature 417, 150-153 (2002). doi: 10.1038/nature747; pmid: 11986621  
4. P. Grelu, N. Akhmediev, Dissipative solitons for mode-locked lasers. Nat. Photonics 6, 84-92 (2012). doi: 10.1038/nphoton.2011.345  
5. N. Akhmediev, A. Ankiewicz, Dissipative Solitons, Lecture Notes in Physics (Springer-Verlag, 2005).  
6. T. J. Kippenberg, R. Holzwarth, S. A. Diddams, Microresonator-based optical frequency combs. Science 332, 555-559 (2011). doi: 10.1126/science.1193968; pmid: 21527707  
7. P. Del'Haye et al., Optical frequency comb generation from a monolithic microresonator. Nature 450, 1214-1217 (2007). doi: 10.1038/nature06401; pmid: 18097405  
8. F. Leo et al., Temporal cavity solitons in one-dimensional Kerr media as bits in an all-optical buffer. Nat. Photonics 4, 471-476 (2010). doi: 10.1038/nphoton.2010.120  
9. T. Herr et al., Temporal solitons in optical microresonators. Nat. Photonics 8, 145-152 (2014). doi: 10.1038/nphoton.2013.343  
10. A. B. Matsko, A. A. Savchenkov, D. Strekalov, V. S. Ilchenko, L. Maleki, Optical hyperparametric oscillations in a whispering-gallery-mode resonator: Threshold and phase diffusion. Phys. Rev. A 71, 033804 (2005). doi: 10.1103/PhysRevA.71.033804  
11. T. J. Kippenberg, S. M. Spillane, K. J. Vahala, Kerr-nonlinearity optical parametric oscillation in an ultrahigh-Q toroid microcavity. Phys. Rev. Lett. 93, 083904 (2004). doi: 10.1103/PhysRevLett.93.083904; pmid: 15447188  
12. Y. K. Chembo, C. R. Menyuk, Spatiotemporal Lugiato-Lefever formalism for Kerr-comb generation in whispering-gallery-mode resonators. Phys. Rev. A 87, 053852 (2013). doi: 10.1103/PhysRevA.87.053852  
13. L. A. Lugiato, R. Lefever, Spatial dissipative structures in passive optical systems. Phys. Rev. Lett. 58, 2209-2211 (1987). doi: 10.1103/PhysRevLett.58.2209; pmid: 10034681  
14. I. V. Barashenkov IV, Y. S. Smirnov, Existence and stability chart for the ac-driven, damped nonlinear Schrodinger solitons. Phys. Rev. E Stat. Phys. Plasmas Fluids Relat. Interdiscip. Topics 54, 5707-5725 (1996). doi: 10.1103/PhysRevE.54.5707; pmid: 9965759  
15. M. Haehterman, S. Trillo, S. Wabnitz, Dissipative modulation instability in a nonlinear dispersive ring cavity. Opt. Commun. 91, 401-407 (1992). doi: 10.1016/0030-4018(92)90367-Z  
16. A. B. Matsko et al., Mode-locked Kerr frequency combs. Opt. Lett. 36, 2845-2847 (2011). doi: 10.1364/OL.36.002845; pmid: 21808332

17. X. Yi, Q.-F. Yang, K. Y. Yang, M.-G. Suh, K. Vahala, Soliton frequency comb at microwave rates in a high-Q silica microresonator. Optica 2, 1078 (2015). doi: 10.1364/OPTICA.2.001078  
18. A. G. Griffith et al., Silicon-chip mid-infrared frequency comb generation. Nat. Commun. 6, 6299 (2015). doi: 10.1038/ncomics7299; pmid: 25708922  
19. C. Joshi et al., Thermally controlled comb generation and soliton modeling in microresonators. Opt. Lett. 41, 2565-2568 (2016). doi: 10.1364/OL.41.002565; pmid: 27244415  
20. V. Brasch et al., Photonic chip-based optical frequency comb using soliton Cherenkov radiation. Science 351, 357-360 (2016). doi: 10.1126/science.aad4811; pmid: 26721682  
21. E. Obrzud, S. Lecomte, T. Herr, Temporal solitons in microresonators driven by optical pulses. Nat. Photonics 11, 600-607 (2017). doi: 10.1038/nphoton.2017.140  
22. T. Udem, R. Holzwarth, T. W. Hansch, Optical frequency metrology. Nature 416, 233-237 (2002). doi: 10.1038/416233a; pmid: 11894107  
23. J. L. Hall, Defining and measuring optical frequencies: The optical clock opportunity—and more (Nobel lecture). Rev. Mod. Phys. 78, 1279-1295 (2006), doi: 10.1103/RevModPhys.78.1279; pmid: 17086589  
24. S. T. Cundiff, J. Ye, Colloquium: Femtosecond optical frequency combs. Rev. Mod. Phys. 75, 325-342 (2003). doi: 10.1103/RevModPhys.75.325  
25. I. Coddington, N. Newbury, W. Swann, Dual-comb spectroscopy. Optica 3, 414 (2016). doi: 10.1364/OPTICA.3.000414  
26. Y. K. Chembo, Kerr optical frequency combs: Theory, applications and perspectives. Nanophotonics 5, 214 (2016). doi: 10.1515/nanoph-2016-0013  
27. A. A. Savchenkov, A. B. Matsko, L. Maleki, On Frequency Combs in Monolithic Resonators. Nanophotonics 5, 363-391 (2016). doi: 10.1515/nanoph-2016-0031  
28. A. Pasquazi et al., Micro-combs: A novel generation of optical sources. Phys. Rep. 729, 1-81 (2018). doi: 10.1016/j.physrep.2017.08.004  
29. P. Del'Haye et al., Octave spanning tunable frequency comb from a microresonator. Phys. Rev. Lett. 107, 063901 (2011). doi: 10.1103/PhysRevLett.107.063901; pmid: 21902324  
30. T. Herr et al., Universal formation dynamics and noise of Kerr-frequency combs in microresonators. Nat. Photonics 6, 480-487 (2012), doi: 10.1038/nphoton.2012.127  
31. F. Ferdous et al., Spectral line-by-line pulse shaping of on-chip microresonator frequency combs. Nat. Photonics 5, 770-776 (2011). doi:10.1038/nphoton.2011.255  
32. S. H. Lee et al., Towards visible soliton microcomb generation. Nat. Commun. 8, 1295 (2017). doi: 10.1038/s41467-017-01473-9; pmid: 29101367  
33. M. Karpov, M. H. Pfeiffer, T. J. Kippenberg, Photonic chip-based soliton frequency combs covering the biological imaging window. arXiv:1706.06445 [physics,optics] (2017).  
34. Q. Li et al., Stably accessing octave-spanning microresonator frequency combs in the soliton regime. Optica 4, 193-203 (2017). doi: 10.1364/OPTICA.4.000193; pmid: 28603754  
35. M. H. P. Pfeiffer et al., Octave-spanning dissipative Kerr soliton frequency combs in Si_3N_4 microresonators. Optica 4, 684 (2017). doi: 10.1364/OPTICA.4.000684  
36. M. Yu et al., Silicon-chip-based mid-infrared dual-comb spectroscopy. arXiv:1610.01121 [physics optics] (2016).  
37. M. G. Suh, K. Vahala, Gigahertz-repetition-rate soliton microcombs. Optica 5, 65-66 (2018). doi: 10.1364/OPTICA.5.000065  
38. M.-G. Suh, Q.-F. Yang, K. Y. Yang, X. Yi, K. J. Vahala, Microresonator soliton dual-comb spectroscopy. Science 354, 600-603 (2016). doi: 10.1126/science.aah6516; pmid: 27738017  
39. N. G. Pavlov et al., Soliton dual frequency combs in crystalline microresonators. Opt. Lett. 42, 514-517 (2017). doi: 10.1364/OL.42.000514; pmid: 28146515  
40. A. Dutt et al., On-chip dual comb source for spectroscopy. arXiv:1611.07673 [physics optics] (2016).  
41. M. Yu, Y. Okawachi, A. G. Griffith, M. Lipson, A. L. Gaeta, Microresonator-based high-resolution gas spectroscopy. Opt. Lett. 42, 4442-4445 (2017). doi: 10.1364/OL.42.004442; pmid: 29088183  
42. J. D. Jost et al., Counting the cycles of light using a self-referenced optical microresonator. Optica 2, 706 (2015). doi: 10.1364/OPTICA.2.000706  
43. V. Brasch, E. Lucas, J. D. Jost, M. Geiselmann, T. J. Kippenberg, Self-referenced photonic chip soliton Kerr

frequency comb. Light Sci. Appl. 6, e16202 (2016). doi: 10.1038/lsa.2016.202  
44. P. Marin-Palomo et al., Microresonator-based solitons for massively parallel coherent optical communications. Nature 546, 274-279 (2017). doi: 10.1038/nature22387; pmid: 28593968  
45. W. Liang et al., High spectral purity Kerr frequency comb radio frequency photonic oscillator. Nat. Commun. 6, 7957 (2015). doi: 10.1038/ncomms8957; pmid: 26260955  
46. P. Trocha et al., Ultrafast optical ranging using microresonator soliton frequency combs. Science 359, 887-891 (2018). doi: 10.1126/science.aao3924; pmid: 29472477  
47. M.-G. Suh, K. Vahala, Soliton microcomb range measurement. arXiv:1705.06697 [physics optics] (2017).  
48. D. T. Spencer et al., An integrated-photonics optical-frequency synthesizer. arXiv:1708.05228 [physics.app-ph] (2017).  
49. E. Obrzud et al., A microphotonic astrocomb. arXiv:1712.09526 [physics optics] (2017).  
50. M.-G. Suh et al., Searching for exoplanets using a microresonator astrocomb. arXiv:1801.05174 [physics,optics] (2018).  
51. V. E. Lobanov, G. Lihachev, T. J. Kippenberg, M. L. Gorodetsky, Frequency combs and platicons in optical microresonators with normal GVD. Opt. Express 23, 7713-7721 (2015). doi: 10.1364/OE.23.007713; pmid: 25837109  
52. M. Karpov et al., Raman self-frequency shift of dissipative Kerr solitons in an optical microresonator. Phys. Rev. Lett. 116, 103902 (2016). doi: 10.1103/PhysRevLett.116.103902; pmid: 27015482  
53. C. Milian, A. V. Gorbach, M. Taki, A. V. Yulin, D. V. Skryabin, Solitons and frequency combs in silica microring resonators: Interplay of the Raman and higher-order dispersion effects. Phys. Rev. A 92, 033851 (2015). doi: 10.1103/PhysRevA.92.033851  
54. X. Yi, Q.-F. Yang, K. Y. Yang, K. Vahala, Theory and measurement of the soliton self-frequency shift and efficiency in optical microcavities. Opt. Lett. 41, 3419-3422 (2016). doi: 10.1364/OL.41.003419; pmid: 27472583  
55. Q. F. Yang, X. Yi, K. Y. Yang, K. Vahala, Stokes solitons in optical microcavities. Nat. Phys. 13, 53-57 (2017). doi: 10.1038/nphys3875  
56. E. Fermi, J. Pasta, S. Ulam, Los Alamos Report LA-1940 (1955); reproduced in A. C. Newell, Nonlinear Wave Motion (AMS, 1974).  
57. A. B. Matsko, A. A. Savchenkov, L. Maleki, On excitation of breather solitons in an optical microresonator. Opt. Lett. 37, 4856-4858 (2012). doi: 10.1364/OL.37.004856; pmid: 23202069  
58. C. Y. Bao et al., Phys. Rev. Lett. 117, 5 (2016).  
59. M. Yu et al., Breather soliton dynamics in microresonators. Nat. Commun. 8, 14569 (2017). doi: 10.1038/ncomms14569; pmid: 28232720  
60. E. Lucas, M. Karpov, H. Guo, M. L. Gorodetsky, T. J. Kippenberg. Breathing dissipative solitons in optical microresonators. Nat. Commun. 8, 736 (2017). doi: 10.1038/s41467-017-00719-w; pmid: 28963496  
61. T. Herr et al., Mode spectrum and temporal soliton formation in optical microresonators. Phys. Rev. Lett. 113, 123901 (2014). doi: 10.1103/PhysRevLett.113.123901; pmid: 25279630  
62. Q.-F. Yang, X. Yi, K. Y. Yang, K. Vahala, Spatial-mode-interaction-induced dispersive waves and their active tuning in microresonators. Optica 3, 1132 (2016). doi: 10.1364/OPTICA.3.001132  
63. D. C. Cole, E. S. Lamb, P. DelHaye, S. A. Diddams, S. B. Papp, Soliton crystals in Kerr resonators. Nat. Photonics 11, 671-676 (2017). doi: 10.1038/s41566-017-0009-z  
64. H. Guo et al., Universal dynamics and deterministic switching of dissipative Kerr solitons in optical microresonators. Nat. Phys. 13, 94-102 (2017). doi: 10.1038/nphys3893  
65. K. Ikeda, H. Daido, O. Akimoto, Optical turbulence: Chaotic behavior of transmitted light from a ring cavity. Phys. Rev. Lett. 45, 709-712 (1980). doi: 10.1103/PhysRevLett.45.709  
66. D. W. M. Laughlin, J. V. Moloney, A. C. Newell, Solitary waves as fixed points of infinite-dimensional maps in an optical bistable ring cavity. Phys. Rev. Lett. 51, 75-78 (1983) PRL. doi: 10.1103/PhysRevLett.51.75  
67. T. Hansson, S. Wabnitz, Dynamics of microresonator frequency comb generation: Models and stability. Nanophotonics 5, 231 (2016). doi: 10.1515/nanoph-2016-0012

68. A. Hasegawa, F. Tappert, Transmission of stationary nonlinear optical pulses in dispersive dielectric fibers. I. Anomalous dispersion. Appl. Phys. Lett. 23, 142-144 (1973). doi: 10.1063/1.1654836  
69. K. Saha et al., Modelocking and femtosecond pulse generation in chip-based frequency combs. Opt. Express 21, 1335-1343 (2013). doi: 10.1364/OE.21.001335; pmid: 23389027  
70. V. Brasch, Q.-F. Chen, S. Schiller, T. J. Kippenberg, Radiation hardness of high-Q silicon nitride microresonators for space compatible integrated optics. Opt. Express 22, 30786-30794 (2014). doi: 10.1364/OE.22.030786; pmid: 25607027  
71. J. S. Levy et al., CMOS-compatible multiple-wavelength oscillator for on-chip optical interconnects. Nat. Photonics 4, 37-40 (2010). doi: 10.1038/nphoton.2009.259  
72. S. Coen, H. G. Randle, T. Sylvestre, M. Erkintalo, Modeling of octave-spanning Kerr frequency combs using a generalized mean-field Lugiato-Lefever model. Opt. Lett. 38, 37-39 (2013). doi: 10.1364/OL.38.000037; pmid: 23282830  
73. A. Kordts, M. H. P. Pfeiffer, H. Guo, V. Brasch, T. J. Kippenberg, Higher order mode suppression in high-Q anomalous dispersion SiN microresonators for temporal dissipative Kerr soliton formation. Opt. Lett. 41, 452-455 (2016). doi: 10.1364/OL.41.000452; pmid: 26907395  
74. V. Brasch, M. Geiselmann, M. H. P. Pfeiffer, T. J. Kippenberg, Bringing short-lived dissipative Kerr soliton states in microresonators into a steady state. Opt. Express 24, 29312-29320 (2016). doi: 10.1364/OE.24.029312; pmid: 27958591  
75. J. Stone et al., Thermal and nonlinear dissipative-soliton dynamics in Kerr microresonator frequency combs. arXiv:1708.08405 [physics,optics] (2017).  
76. K. E. Webb, M. Erkintalo, S. Coen, S. G. Murdoch, Experimental observation of coherent cavity soliton frequency combs in silica microspheres. Opt. Lett. 41, 4613-4616 (2016). doi: 10.1364/OL.41.004613; pmid: 28005849  
77. M. Yu, Y. Okawachi, A. G. Griffith, M. Lipson, A. L. Gaeta, Mode-locked mid-infrared frequency combs in a silicon microresonator. Optica 3, 854 (2016). doi: 10.1364/OPTICA.3.000854  
78. X. Yi, Q.-F. Yang, K. Youl Yang, K. Vahala, Active capture and stabilization of temporal solitons in microresonators. Opt. Lett. 41, 2037-2040 (2016). doi: 10.1364/OL.41.002037; pmid: 27128068  
79. E. Lucas, H. Guo, J. D. Jost, M. Karpov, T. J. Kippenberg, Detuning-dependent properties and dispersion-induced instabilities of temporal dissipative Kerr solitons in optical microresonators. Phys. Rev. A 95, 043822 (2017). doi: 10.1103/PhysRevA.95.043822  
80. T. Herr, M. L. Gorodetsky, T. J. Kippenberg, in Dissipative Kerr Solitons in Optical Microresonators (Wiley, 2015), pp. 129-162.  
81. A. A. Savchenkov et al., Low threshold optical oscillations in a whispering gallery mode  $\mathrm{CaF}_2$  resonator. Phys. Rev. Lett. 93, 243905 (2004). doi: 10.1103/PhysRevLett.93.243905; pmid: 15697815  
82. C. Y. Wang et al., Mid-infrared optical frequency combs at  $2.5\mu \mathrm{m}$  based on crystalline microresonators. Nat. Commun. 4, 1345 (2013). doi: 10.1038/ncomms2335; pmid: 23299895  
83. J. Li, H. Lee, T. Chen, K. J. Yahala, Low-pump-power, low-phase-noise, and microwave to millimeter-wave repetition rate operation in microcombs. Phys. Rev. Lett. 109, 233901 (2012). doi: 10.1103/PhysRevLett.109.233901; pmid: 23368202  
84. M. L. Gorodetsky, WE-Heraeus Seminar on Micro and Macro-cavities in Classical and Non-classical Light (2011); http://goo.gl/tmniGm.  
85. Y. K. Chembo, D. V. Strekalov, N. Yu, Spectrum and dynamics of optical frequency combs generated with monolithic whispering gallery mode resonators. Phys. Rev. Lett. 104, 103902 (2010). doi: 10.1103/PhysRevLett.104.103902; pmid: 20366426  
86. T. Carmon, L. Yang, K. Vahala, Dynamical thermal behavior and thermal self-stability of microcavities. Opt. Express 12, 4742-4750 (2004). doi: 10.1364/OPEX.12.004742; pmid: 19484026  
87. V. E. Zakharov, A. B. Shabat, Exact theory of two-dimensional self-focusing and one-dimensional self-modulation of waves in nonlinear media. Sov. Phys. JETP 34, 62 (1972).  
88. T. S. Raju, C. N. Kumar, P. K. Panigrahi, On exact solitary wave solutions of the nonlinear Schrödinger equation with a

source.J.Phys.Math.Gen.38,L271-L276 2005. doi:10.1088/0305-4470/38/16/L02  
89. W. H. Renninger, P. T. Rakich, Closed-form solutions and scaling laws for Kerr frequency combs. Sci. Rep. 6, 24742 (2016). doi: 10.1038/srep24742; pmid: 27108810  
90. D. J. Kaup, A. C. Newell, Solitons as Particles, Oscillators, and in slowly changing media: A singular perturbation theory. Proc. R. Soc. London Ser. A 361, 413-446 (1978). doi: 10.1098/rspa.1978.0110  
91. K. Nozaki, N. Bekki, Solitons as attractors of a forced dissipative nonlinear Schrödinger equation. Phys. Lett. A 102, 383-386 (1984). doi:10.1016/0375-9601(84)91060-0  
92. T. Hansson, D. Modotto, S. Wabnitz, On the numerical simulation of Kerr frequency combs using coupled mode equations. Opt. Commun. 312, 134-136 (2014). doi: 10.1016/j.optcom.2013.09.017  
93. I. S. Grudinin et al., High-contrast Kerr frequency combs. Optica 4, 434 (2017). doi: 10.1364/OPTICA.4.000434  
94. V. B. Braginsky, M. L. Gorodetsky, V. S. Ilichenko, Quality-factor and nonlinear properties of optical whispering-gallery modes. Phys. Lett. A 137, 393-397 (1989). doi: 10.1016/0375-9601(89)90912-2  
95. P.-H. Wang et al., Intracavity characterization of micro-comb generation in the single-soliton regime. Opt. Express 24, 10890-10897 (2016). doi: 10.1364/OE.24.010890; pmid: 27409909  
96. M. H. P. Pfeiffer et al., Photonic Damascene process for integrated high-Q microresonator based nonlinear photonics. Optica 3, 20 (2016). doi: 10.1364/OPTICA.3.000020  
97. X. Ji et al., Ultra-low-loss on-chip resonators with sub-milliwatt parametric oscillation threshold. Optica 4, 619 (2017). doi: 10.1364/OPTICA.4.000619  
98. M. A. Foster et al., Broad-band optical parametric gain on a silicon photonic chip. Nature 441, 960-963 (2006). doi: 10.1038/nature04932; pmid: 16791190  
99. J. Riemensberger et al., Dispersion engineering of thick high-Q silicon nitride ring-resonators via atomic layer deposition. Opt. Express 20, 27661-27669 (2012). doi: 10.1364/OE.20.027661; pmid: 23262714  
100. L. Zhang et al., Generation of two-cycle pulses and octave-spanning frequency combs in a dispersion-flattened micro-resonator. Opt. Lett. 38, 5122-5125 (2013). doi: 10.1364/OL.38.005122; pmid: 24281525  
101. Y. Okawachi et al., Bandwidth shaping of microresonator-based frequency combs via dispersion engineering. Opt. Lett. 39, 3535-3538 (2014). doi: 10.1364/OL.39.003535; pmid: 24978530  
102. I. S. Grudinin, N. Yu, Dispersion engineering of crystalline resonators via microstructuring. Optica 2, 221 (2015). doi: 10.1364/OPTICA.2.000221  
103. C. Bao et al., High-order dispersion in Kerr comb oscillators. J. Opt. Soc. Am. B 34, 715 (2017). doi: 10.1364/JOSAB.34.000715  
104. N. Akhmediev, M. Karlsson, Cherenkov radiation emitted by solitons in optical fibers. Phys. Rev. A 51, 2602-2607 (1995). doi: 10.1103/PhysRevA.51.2602; pmid: 9911876  
105. A. V. Cherenkov, V. E. Lobanov, M. L. Gorodetsky, Dissipative Kerr solitons and Cherenkov radiation in optical microresonators with third-order dispersion. Phys. Rev. A 95, 033810 (2017). doi: 10.1103/PhysRevA.95.033810  
106. X. Yi et al., Nat. Commun. 8, 9 (2017). doi: 10.1038/s41467-017-00020-w; pmid: 28377584  
107. M. R. E. Lamont, Y. Okawachi, A. L. Gaeta, Route to stabilized ultrabroadband microresonator-based frequency combs. Opt. Lett. 38, 3478-3481 (2013). doi: 10.1364/OL.38.003478; pmid: 24104792  
108. H. Kumar, F. Chand, Dark and bright solitary wave solutions of the higher order nonlinear Schrödinger equation with self-steepening and self-frequency shift effects. J. Nonlinear Opt. Phys. Mater. 22, 135001 (2013). doi: 10.1142/S021886351350001X  
109. C. Bao et al., Nonlinear conversion efficiency in Kerr frequency comb generation. Opt. Lett. 39, 6126-6129 (2014). doi: 10.1364/OL.39.006126; pmid: 25361295  
110. M. Erkintalo, Y. Q. Xu, S. G. Murdoch, J. M. Dudley, G. Genty, Cascaded phase matching and nonlinear symmetry breaking in fiber frequency combs. Phys. Rev. Lett. 109, 223904 (2012). doi: 10.1103/PhysRevLett.109.223904; pmid: 23368122  
111. Y. Wang, M. Anderson, S. Coen, S. G. Murdoch, M. Erkintalo, Stimulated Raman scattering imposes fundamental limits to the duration and bandwidth of temporal cavity solitons. Phys. Rev. Lett. 120, 053902 (2018). doi: 10.1103/PhysRevLett.120.053902; pmid: 29481150

112. Q. F. Yang, X. Yi, K. Y. Yang, K. Vahala, Counter-propagating solitons in microresonators. Nat. Photonics 11, 560-564 (2017). doi: 10.1038/nphoton.2017.117  
113. C. Joshi et al., Counter-rotating cavity solitons in a silicon nitride microresonator. Opt. Lett. 43, 547-550 (2018). doi: 10.1364/OL.43.000547; pmid: 29400837  
114. E. Lucas et al., Spatial multiplexing of soliton microcombs. arXiv:1804.03706v2 [physics,optics] (2018). doi: arxiv.org/abs/1804.03706v2  
115. A. B. Matsko, A. A. Savchenkov, L. Maleki, Normal group-velocity dispersion Kerr frequency comb. Opt. Lett. 37, 43-45 (2012). doi: 10.1364/OL.37.000043; pmid: 22212785  
116. C. Godey, I. V. Balakireva, A. Coillet, Y. K. Chembo, Stability analysis of the spatiotemporal Lugiato-Lefever model for Kerr optical frequency combs in the anomalous and normal dispersion regimes. Phys. Rev. A 89, 063814 (2014). doi: 10.1103/PhysRevA.89.063814  
117. W. Liang et al., Generation of a coherent near-infrared Kerr frequency comb in a monolithic microresonator with normal GVD. Opt. Lett. 39, 2920-2923 (2014). doi: 10.1364/OL.39.002920; pmid: 24978237  
118. S.W. Huang et al., Mode-locked ultrashort pulse generation from on-chip normal dispersion microresonators. Phys. Rev. Lett. 114, 053901 (2015). doi: 10.1103/PhysRevLett.114.053901; pmid: 25699441  
119. X. Xue et al., Mode-locked dark pulse Kerr combs in normal-dispersion microresonators. Nat. Photonics 9, 594-600 (2015). doi: 10.1038/nphoton.2015.137  
120. J. K. Jang et al., Dynamics of mode-coupling-induced microresonator frequency combs in normal dispersion. Opt. Express 24, 28794-28803 (2016). doi: 10.1364/OE.24.028794; pmid: 27958523  
121. V. E. Lobanov, G. Lihachev, M. L. Gorodetsky, Generation of platicons and frequency combs in optical microresonators with normal GVD by modulated pump. Europhys. Lett. 112, 54008 (2015). doi: 10.1209/0295-5075/112/54008

122. X. X. Xue et al., Normal-dispersion microcombs enabled by controllable mode interactions. Laser Photonics Rev. 9, L23-L28 (2015). doi:10.1002/lpor.201500107  
123. P. Parra-Rivas, E. Knobloch, D. Gomila, L. Gelens, Dark solitons in the Lugiato-Lefever equation with normal dispersion. Phys. Rev. A 93, 063839 (2016). doi: 10.1103/PhysRevA.93.063839  
124. V. E. Lobanov, A. V. Cherenkov, A. E. Shitikov, I. A. Bilenko, M. L. Gorodetsky, Dynamics of platicons due to third-order dispersion. Eur. Phys. J. D 71, 185 (2017). doi: 10.1140/epjd/e2017-80148-0  
125. P. Parra-Rivas, D. Gomila, L. Gelens, Coexistence of stable dark- and bright-soliton Kerr combs in normal-dispersion resonators. Phys. Rev. A 95, 053863 (2017). doi: 10.1103/PhysRevA.95.053863  
126. S. B. Papp et al., Microresonator frequency comb optical clock. Optica 1, 10 (2014). doi: 10.1364/OPTICA.1.000010  
127. P. Del'Haye et al., Nat. Photonics 10, 516-520 (2016).  
128. W. Liang et al., IEEE Photonics J. 9, 11 (2017).  
129. T. Ideguchi et al., Coherent Raman spectro-imaging with laser frequency combs. Nature 502, 355-358 (2013). doi: 10.1038/nature12607; pmid: 24132293  
130. V. Ataie, D. Esman, B. P.-P. Kuo, N. Alic, S. Radic, Subnoise detection of a fast random event. Science 350, 1343-1346 (2015). doi: 10.1126/science.aac8446; pmid: 26659052  
131. M. Pu, L. Ottaviano, E. Semenova, K. Yvind, Efficient frequency comb generation in AlGaAs-on-insulator. Optica 3, 823 (2016). doi: 10.1364/OPTICA.3.000823  
132. Y. Okawachi et al., Quantum random number generator using a microresonator-based Kerr oscillator. Opt. Lett. 41, 4194-4197 (2016). doi: 10.1364/OL.41.004194; pmid: 27628355  
133. M. Kues et al., On-chip generation of high-dimensional entangled quantum states and their coherent control.

Nature 546, 622-626 (2017). doi: 10.1038/nature22986; pmid: 28658228  
134. H. Taheri, A. B. Matsko, L. Maleki, Optical lattice trap for Kerr solitons. Eur. Phys. J. D 71, 153 (2017). doi: 10.1140/epjd/e2017-80150-6  
135. P. Ghelfi et al., A fully photonics-based coherent radar system. Nature 507, 341-345 (2014). doi: 10.1038/nature13078; pmid: 24646997  
136. D. T. Spencer et al., An optical-frequency synthesizer using integrated photonics. Nature 557, 81-85 (2018). doi: 10.1038/s41586-018-0065-7; pmid: 29695870

# ACKNOWLEDGMENTS

The authors thank M. Karpov and A. Lukashchuk for assistance in preparing the figures, as well as S. Hohnle from IBM for rendering Fig. 1. Author contributions: This Review was written by T.J.K. and M.L.G. with critical input and support of A.L.G. and M.L. All authors contributed and discussed the content of the Review.

Funding: This material is based on work supported by the Defense Advanced Research Projects Agency (DARPA), Defense Sciences Office (DSO) and (MTO), grants HR0011-15-C-0055 (DODOS), W31P4Q-16-1-0002 (SCOUT), and W31P4Q-14-C-0050 (PULSE); The European Space Technology Centre with ESA (4000116145/16/ NL/MH/GM); the Swiss National Science Foundation via BRIDGE (176563); a Swiss National Science Foundation Grant and Ministry of Education and Science of the Russian Federation (project RFMEFI58516X0005); and the Air Force Office of Scientific Research, Air Force Material Command, USAF under awards FA9550-15-1-0099 and FA9550-15-1-0303. Competing interests: T.J.K. is a cofounder and shareholder of LiGenTec SA, a start-up company offering  $\mathrm{Si}_3\mathrm{N}_4$  photonic integrated circuits as a foundry service. T.J.K., A.L.G., M.L.G., and M.L., are co-inventors of patents in the field of publication. Patents are owned by EPFL, Cornell, and the Max Planck Society.

10.1126/science.aan8083

# Dissipative Kerr solitons in optical microresonators

Tobias J. Kippenberg, Alexander L. Gaeta, Michal Lipson and Michael L. Gorodetsky

Science 361 (6402), eaan8083.

DOI: 10.1126/science.aan8083

ARTICLE TOOLS

http://science.sciencemag.org/content/361/6402/eaan8083

PERMISSIONS

http://www.sciencemag.org/help/reprints-and-permissions

Use of this article is subject to the Terms of Service