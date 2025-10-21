# Wave-Packet and Coherent Control Dynamics

Kenji Ohmori

Institute for Molecular Science, National Institutes of Natural Sciences; The Graduate University for Advanced Studies (SOKENDAI); and CREST, Japan Science and Technology Agency, Myodaiji, Okazaki 444-8585, Japan; email: ohmori@ims.ac.jp

Annu. Rev. Phys. Chem. 2009. 60:487-511

First published online as a Review in Advance on December 9, 2008

The Annual Review of Physical Chemistry is online at physchem.annualreviews.org

This article's doi: 10.1146/annurev.physchem.59.032607.093818

Copyright © 2009 by Annual Reviews. All rights reserved

0066-426X/09/0505-0487$20.00

# Key Words

wave-packet interferometry, quantum ripple, quantum carpet, information processing with molecular eigenstates, decoherence

# Abstract

This review summarizes progress in coherent control as well as relevant recent achievements, highlighting, among several different schemes of coherent control, wave-packet interferometry (WPI). WPI is a fundamental and versatile scenario used to control a variety of quantum systems with a sequence of short laser pulses whose relative phase is finely adjusted to control the interference of electronic or nuclear wave packets (WPs). It is also useful in retrieving quantum information such as the amplitudes and phases of eigenfunctions superposed to generate a WP. Experimental and theoretical efforts to retrieve both the amplitude and phase information are recounted. This review also discusses information processing based on the eigenfunctions of atoms and molecules as one of the modern and future applications of coherent control. The ultrafast coherent control of ultracold atoms and molecules and the coherent control of complex systems are briefly discussed as future perspectives.

# 1. INTRODUCTION

Coherent control is a technique that manipulates the interference of wave functions by adjusting their amplitudes and phases. It is a basic way of controlling a variety of quantum systems, ranging from isolated atoms to bulk solids, and it may help us better understand the wave nature of matter and develop new quantum technologies, such as bond-selective chemistry and novel information processing. One promising approach to realizing coherent control is the use of coherent light to modulate the amplitudes and phases of wave functions. For example, Figure 1 shows schematically a diatomic molecule irradiated with an ultrashort optical pulse to be electronically excited. If the duration of the pulse is shorter than the classical vibrational period of the molecule (which is typically on the order of picoseconds to femtoseconds), the bandwidth of the pulse is then broad enough to cover multiple vibrational eigenstates. Those eigenstates are thus coherently superposed

![](images/8852b236ae6c8c54d90ea1625eca5552e6050fb7993ef0b02efe45b40ae38624.jpg)  
Figure 1

Schematic representation of the generation of a vibrational wave packet (WP) with an ultrashort laser pulse. If the pulse duration is shorter than the classical vibrational period of the molecule, its bandwidth is broad enough to superpose multiple vibrational eigenstates. The superposed eigenstates interfere with each other to create a spatially localized wave function referred to as a WP.

to give constructive or destructive interferences as functions of time and space to create a spatially localized wave function:

$$
| \Psi (r, t) \rangle = \sum_ {n} c _ {n} | \psi_ {n} (r) \rangle \exp \left[ - i \left(\omega_ {n} t - \phi_ {n}\right) \right], \tag {1}
$$

where  $\psi_{n}(r)$  and  $\omega_{n}$  are the eigenfunction and transition frequency of the  $n$ -th vibrational level, respectively;  $c_{n}$  and  $\phi_{n}$  represent its amplitude and phase; and  $r$  is an internuclear distance. This superposition of the eigenstates is called a wave packet (WP). Because the periods  $2\pi /\omega_{n}$  of the temporal oscillation of the eigenstate depend on  $n$ , the interference at a particular  $r$  becomes alternately constructive and destructive. This alternation makes the WP move back and forth along the internuclear axis with a period of the classical vibrational motion of the molecule. In the generation of this WP, the amplitude and phase of each frequency component within the bandwidth of the optical pulse are imprinted on  $c_{n}$  and  $\phi_{n}$  of the vibrational eigenstate excited by that frequency component. Manipulating the optical amplitudes and phases, therefore, allows the manipulation of the quantum amplitudes and phases of a WP. Importantly, this strategy basically is applicable not only to the vibrational eigenstates of a diatomic molecule, but also to any type of eigenstate of a variety of quantum systems.

The concept of coherent control was first proposed in the 1980s by renowned theoreticians in the field of physical chemistry. Brumer, Shapiro, and colleagues (1, 2) published a series of seminal papers in which they proposed a scenario to control branching ratios in molecular photodissociation. In their approach, a molecule is irradiated simultaneously with two continuous-wave laser beams with different wavelengths to be excited to continuum vibronic states whose temporal oscillations are synchronized with those of the two laser fields. Their theoretical simulations have shown that constructive and destructive interferences can be induced selectively in desired and undesired reaction pathways, respectively, by adjusting the relative phase between those two laser fields. This scenario with a phase-related pair of two-color laser beams is called the Brumer-Shapiro scheme. Tannor, Kosloff, and Rice published a series of seminal theoretical papers that described another scenario to control molecular photodissociation (3, 4). They proposed the use of a sequence of femtosecond laser pulses, one of which illuminates a molecule to create a WP on the excited potential surface, and the WP then travels on that surface to reach a particular point to be further excited to another potential surface or de-excited to the ground surface by the other pulse to promote the desired reaction pathway. This type of scenario, in which the timing of two femtosecond laser pulses is optimized, is called the Tannor-Kosloff-Rice scheme. Both the Brumer-Shapiro and Tannor-Kosloff-Rice schemes were not implemented in the laboratory until the 1990s when laser technology was developing rapidly. The Brumer-Shapiro scheme has been implemented in the ionization of the mercury atom by Elliot and coworkers (5) and in the photoionization and photodissociation of the HI molecule by Gordon and coworkers (6, 7). The Tannor-Kosloff-Rice scheme, conversely, has been implemented in the photoionization and photodissociation of the  $\mathrm{Na}_2$  molecule by Gerber and coworkers (8) and in  $\mathrm{Xe} + \mathrm{I}_2$  reactions by Zewail and coworkers (9). In the early 1990s, Fleming and coworkers (10, 11) demonstrated another important scheme by employing a sequence of phase-related femtosecond laser pulses to induce selectively the constructive or destructive interference of two vibrational WPs in the iodine molecule. This type of scenario is called wave-packet interferometry (WPI). WPI can be regarded as a fruitful combination of the Brumer-Shapiro and Tannor-Kosloff-Rice schemes, and the phase-locked double-pulse approach offers a basic and versatile strategy to control a variety of quantum systems even in the liquid and solid state (12–18). WPI is a main topic of this review, and is described in detail in Section 2. Another approach has developed rapidly based on the amplitude and phase shaping of ultrashort laser pulses. The simplest cases have been exemplified so that the temporal evolutions of vibrational

WP: wave packet

WPI: wave-packet interferometry

WPs in diatomic molecules are modified by changing the chirp rates of femtosecond laser pulses (19, 20). Moreover, a successful combination of the pulse-shaping device and the closed-loop control based on a genetic algorithm has been effective in controlling the dynamics of more complex systems such as molecules in the liquid phase and large polyatomic molecules (21-29). The target of coherent control is cross-disciplinary now, and the range of its applications includes a variety of research fields, such as solid-state physics and information processing with quantum states of matter, which is another main issue discussed in this review. The reader is referred to other excellent reviews and books for a more general overview of the history of coherent control (30-38).

# 2. WAVE-PACKET INTEREROMETRY

# 2.1. Theoretical Background

A pair of electronic or vibrational WPs can be created in a single atom or molecule with a train of two femtosecond laser pulses with their optical amplitudes and phases imprinted on the quantum amplitudes and phases of the WPs. By controlling the relative phase of the femtosecond pulses, therefore, one can induce selectively the constructive or destructive interference of those two WPs. This is a schematic concept of WPI. For example, the diatomic molecule schematically shown in Figure 1 is irradiated by a sequence of pump and control pulses with their interpulse delay  $\tau_{\mathrm{control}}$ :

$$
E _ {\mathrm {p c}} (t, \tau_ {\text {c o n t r o l}}) = E _ {0} (t) \cos (\omega_ {0} t) + \alpha E _ {0} (t - \tau_ {\text {c o n t r o l}}) \cos [ \omega_ {0} (t - \tau_ {\text {c o n t r o l}}) ], \tag {2}
$$

where  $E_0(t)$  and  $\omega_0$  denote a pulse envelope and a carrier angular frequency, respectively, and  $\alpha$  is the amplitude ratio of the control pulse to the pump pulse. According to Equation 1, the wave function created in the excited state by this laser field is described in the perturbative regime as

$$
| \Psi (r, t) \rangle = \sum_ {n} c _ {n} | \psi_ {n} (r) \rangle \exp \left[ - i \left(\omega_ {n} t - \phi_ {n}\right) \right] + \alpha \sum_ {n} c _ {n} | \psi_ {n} (r) \rangle \exp \left\{- i \left[ \omega_ {n} \left(t - \tau_ {\text {c o n t r o l}}\right) - \phi_ {n} \right] \right\}. \tag {3}
$$

The population  $\rho_{n}$  of a particular vibrational level  $v = n$  is given by

$$
\begin{array}{l} \rho_ {n} = | \langle v = n | \Psi (r, t) \rangle | ^ {2} = c _ {n} ^ {2} | \exp (- i \omega_ {n} t) + \alpha \exp [ - i \omega_ {n} (t - \tau_ {\text {c o n t r o l}}) ] | ^ {2} \\ = c _ {n} ^ {2} \left| 1 + \alpha \exp \left(i \omega_ {n} \tau_ {\text {c o n t r o l}}\right) \right| ^ {2} = c _ {n} ^ {2} \left[ 1 + \alpha^ {2} + 2 \alpha \cos \left(\omega_ {n} \tau_ {\text {c o n t r o l}}\right) \right], \tag {4} \\ \end{array}
$$

where  $\omega_{n}$  is the transition frequency of the level  $v = n$  from the initial vibronic level, and accordingly  $\omega_{n} \sim \omega_{0}$ . The population  $\rho_{n}$  thus oscillates with a period of  $2\pi /\omega_{n}$  as a function of  $\tau_{\mathrm{control}}$  scanned with a resolution better than the optical cycle of the laser fields, alternately giving constructive and destructive interferences. By locking  $\tau_{\mathrm{control}}$ , conversely, with a stability better than the optical cycle, one can induce selectively the constructive or destructive interference.

# 2.2. History of the Development of Wave-Packet Interferometry

Fleming and coworkers (10, 11) first demonstrated the use of WPI in the early 1990s. They employed a sequence of identical femtosecond laser pulses whose relative phase was locked to create a pair of phase-locked vibrational WPs in the iodine molecule  $(\mathrm{I}_2)$  on the  $B$ -state potential curve. They measured the intensity of the total fluorescence from the  $B$  state as a function of the delay between those two femtosecond pulses, actively locking their relative phase to be either constructive or destructive selectively. Hence they selectively induced either the constructive or destructive interference of the two WPs generated with those phase-locked pulses. Since this seminal work, WPI has been developed with electronic (e.g., Rydberg, spin-orbit) WPs in atoms

and molecules (39-63) and vibrational and rotational WPs in molecules (64-75) based on the measurement of the population of the bound excited state sensitive to the relative phase of the twin optical pulses.

Following the Fleming group's success, similar double-pulse approaches have been applied mostly to electronic WPs in alkali atoms (39-43, 45-57, 61-63). Some of these studies (45, 47, 52, 55-57, 61) scanned the pump-control delay with a temporal resolution better than the optical cycle of the pulses, instead of actively locking their relative phase, as was done by Fleming group, to observe directly the so-called Ramsey fringe, which is a temporal interferogram of the two electronic WPs. Similar fringe-resolved interferograms were observed also for vibrational WPs in diatomic molecules (64, 65, 68, 70). From Equations 3 and 4, one can clearly see that the oscillations in such interferograms directly correspond to the temporal oscillations of the eigenfunctions superposed in the WPs, so they are reasonably expected to give detailed information on the quantum states of WPs.

These WPI experiments have been carried out with an ensemble of many atoms or molecules instead of a single atom or molecule. This experimental condition leads to an essential physical difference between atomic and molecular WPI. Molecules have more degrees of freedom, such as vibration and rotation, than atoms, and rotation especially plays a critical role in vibrational WPI in molecular systems. The thermal distribution of the rotational states in a molecular ensemble is known to be a major source of decoherence, called rotational dephasing, that can wipe out the interference structure much more quickly than in atomic systems. More than  $\sim 50\%$  of the fringe contrast could be lost within a single molecular vibration (10, 11, 64-67) in molecular WPI. In atomic WPI, conversely, coherence can last for more than several tens of picoseconds (45, 55, 57). Such quick decoherence in molecular systems could seriously distort the correlation between the relative phase of the double pulse and that of the WPs and degrade controllability. A new approach suppresses such rotational dephasing through the combination of two experimental techniques (68-70): (a) highly state-selective interrogation of the state populations by laser-induced fluorescence (LIF) and (b) a low-temperature and dilute ensemble prepared by molecular jet expansion. Whereas preceding molecular WPI studies had measured the total population of WPs, the LIF technique uses another narrow-band nanosecond probe pulse to interrogate the state population of the subensemble within a narrow band of rotational states of a particular vibrational level within a WP. The low rotational temperature gives the initial population concentrated into low rotational levels, and the dilute ensemble eliminates decoherence caused by molecular collisions.

The state-selective interrogation above has allowed also for the measurement of an interferogram of each individual vibrational eigenstate within a WP, referred to as an eigenstate interferogram (68, 70). In this measurement, the wavelength of the nanosecond probe pulse is tuned to a particular vibrational band of the LIF transition, and the pump-control delay  $\tau_{\mathrm{control}}$  in Equation 4 was scanned with a temporal resolution better than the optical cycle of the laser pulses. By switching the nanosecond probe wavelength from one vibrational band to another with  $\tau_{\mathrm{control}}$  scanned continuously, one can obtain the relative phase between those two different eigenstate interferograms (68, 70). This is referred to as a phase-jump measurement. Figure 2 shows an example of a set of phase-jump measurements with one reference eigenstate switched to different eigenstates that are combined to retrieve the relative phases among all the principal eigenstates within a WP (68, 70). From Figure 2 one can see that the population ratio of the eigenstates within a WP can be manipulated by tuning  $\tau_{\mathrm{control}}$  (68-70). The relative phases of the eigenstates can also be manipulated by tuning  $\tau_{\mathrm{control}}$  (discussed in Section 3) (69, 70).

Recently a new stage of WPI has been reached that is characterized by the first demonstration of the real-time observation of WP interference. Pump-control and probe (three-pulse) experiments,

LIF: laser-induced fluorescence

APM: attosecond phase modulator

![](images/f78d3789fe409c5655d1c6730dcaa41c3abe98c360c80690a0c246890320dcca.jpg)

![](images/6df114a3e8d94d175ca61f08372f1a72c8afeb6dbd8cd732b1f606f3fe19261d.jpg)  
Figure 2

Phase-jump measurements of the eigenstate interferograms of the  $\mathrm{I}_2$  molecule. An interferogram of each vibrational eigenstate within a vibrational wave packet in the  $B$  state was measured with the pump-control delay  $\tau_{\mathrm{control}}$  tuned around  $(1 + 3 / 4)T_{\mathrm{vib}}$ , where  $T_{\mathrm{vib}}$  is a classical vibrational period of the molecule. In the upper three panels  $(a - c)$ , the probe wavelength was switched from one vibrational band to another at  $\tau_{\mathrm{control}} - \tau_0 \cong 0$  with  $\tau_{\mathrm{control}}$  scanned continuously toward a negative direction. The abscissas of panels  $a - c$  were calibrated by the periods of the interferograms calculated from the relevant spectroscopic constants. Black dots represent measured data, and the blue and red curves are the sine functions least-squares-fitted to the regions on the right and left sides of the switching point,  $\tau_{\mathrm{control}} - \tau_0 \cong 0$ , respectively. In the lowest panel  $(d)$ , the four different eigenstate interferograms are plotted together with their relative phases determined in the upper three panels. Figure reprinted from Reference 70.

in which the femtosecond pump and control pulses (typically  $\sim 100 - 200$ -fs pulse widths) are phase locked and another femtosecond probe pulse is unlocked to the pump pulse, have been used to observe the interference of two vibrational WPs produced by the pump and control pulses on the  $B$ -state potential curve of the iodine molecule (69, 70). Figure 3a illustrates this pump-control-probe scheme. The real-time evolution of the WP interference has been measured clearly by scanning the femtosecond probe pulse delay  $\tau_{\mathrm{probe}}$  with the pump-control phase stably locked with a highly stable interferometer [attosecond phase modulator (APM)] (68-70) (Figure 3b). Only with these real-time measurements one can observe a whole dynamical sequence of the WP interference, in which the first WP is created in the molecule, moves back and forth for a certain period, and then interacts with the second WP to trigger a complicated temporal evolution sensitive to the

a  
Figure 3  
![](images/c52497eed5d4488c85d6ac316b71651c7f1b3643444a55af012a35c93efd08dc.jpg)  
(a) Pump-control-probe scheme for the real-time or state-resolved measurement of wave-packet (WP) interference with a femtosecond or nanosecond probe pulse. The potentials are only schematic. (b) Real-time evolution of the interference of two phase-locked vibrational WPs on the  $B$ -state potential of the  $\mathrm{I}_2$  molecule. The pump and control delay  $\tau_{\mathrm{control}}$ ’s are tuned to  $\sim 1$ $T_{\mathrm{vib}}$  ( $\sim 305$  fs), where  $T_{\mathrm{vib}}$  is a classical vibrational period of  $\mathrm{I}_2$ . The relative phase  $\theta_{\mathrm{p-c}}$  of the pump and control pulses is different by  $\sim \pi$  between panels  $i$  and  $ii$ . The gray trace is the evolution measured without a control pulse and is displayed for reference. The cross-correlation of the pump and probe pulses was not taken, and the origin of the probe delay ( $\tau_{\mathrm{probe}} = 0$ ) denotes a position of the top of the first undulation in each measured trace. The vertical scaling of each trace is arbitrary and is normalized by the height of its first undulation. Figure reprinted from Reference 69.

![](images/881b95c6ec63a2f6d6f7400e111cd9bed1c90d9aefe0de33c0881e89fdfb36ec.jpg)

![](images/72597106277d9bd540ce4c409c1763a64709eb9c346fe621bc0b5f6ca6bf6a0d.jpg)  
b

relative phase of the two WPs. The ordinary frequency-domain interpretation (68), based on the spectral interference of the pump and control pulses, is no longer suitable for the present real-time observation. Moreover, the real-time observation has demonstrated experimentally that we can precisely control not only populations (68), but also the dynamics of WPs (69, 70). The APM is indispensable to the demonstration of these real-time observations of WP interferences. The APM consists of a Michelson interferometer whose optical paths are highly stabilized by the assembly of all optical components in a vacuum chamber to reduce the influence of air-flow disturbance and temperature drift. The delay  $\tau_{\mathrm{control}}$  is coarsely tuned with a mechanical translation stage inserted into one arm of the APM, whereas it is fine-tuned by changing the gas pressure within a stainless cell in the other arm of the APM. Figure 4 shows an optical interferogram of the temporally superposed pump and control pulses tuned to  $\sim 537~\mathrm{nm}$  measured by scanning the gas-cell pressure and plotted against  $\tau_{\mathrm{control}}$  calibrated by an optical cycle of the present carrier wavelength,  $\sim 537~\mathrm{nm}$ . The origin  $\tau_{\mathrm{control}} = 0$  is arbitrary. One standard deviation of the sine curve least-squares-fitted to the measured optical interferogram is only 700 zeptoseconds. During the measurement of the real-time evolution of the WP interference as a function of the probe delay  $\tau_{\mathrm{probe}}$ , the control delay  $\tau_{\mathrm{control}}$  was actively stabilized on the attosecond scale with periodical compensations of the drift of a spectral interferogram of the pump and control pulses monitored with a linear detector attached to a spectrometer. Aside from such bound-state interferometry, WP interference has also been observed for the free states located above the dissociation limits of the relevant potential curves (76-79).

![](images/c4fa2a9f7ceafc6e1eb1d6c3c750768a3e0d1c732d75e4977c32cf12966cc4d5.jpg)  
Figure 4

Example of an optical interferogram of two femtosecond laser pulses measured around  $\tau_{\mathrm{control}} \sim 0$  fs. The abscissa was calibrated by an optical cycle 1.79 fs of the present carrier wavelength,  $537~\mathrm{nm}$ . The solid curve represents a sine curve least-squares-fitted to the measured interferogram. One standard deviation of the oscillation period is 700 zephyseconds. Figure reprinted from Reference 70.

# 3. RETRIEVAL OF FULL QUANTUM INFORMATION STORED IN WAVE PACKETS

Two kinds of information are stored in a WP (Equation 1). One is a set of the amplitudes  $c_{n}$ 's of the eigenstates, and the other is a set of their phases  $\phi_{n}$ 's. The quantum state of a WP is fully characterized by these two sets of parameters. Several experimental and theoretical efforts have been made to retrieve both the amplitude and phase information. One approach is based on WPI and is called quantum-state holography (49-51, 80-82). In this approach, a target WP,

$$
\left| \Psi_ {\text {t a r g e t}} (r, t) \right\rangle = \sum_ {n} c _ {n} \left| \psi_ {n} (r) \right\rangle \exp \left[ - i \left(\omega_ {n} t - \phi_ {n}\right) \right], \tag {5}
$$

is created at  $t = 0$  with a shaped femtosecond laser pulse (pump pulse), and the second WP,

$$
\left| \Psi_ {\text {r e f}} (r, t) \right\rangle = \sum_ {n} d _ {n} \left| \psi_ {n} (r) \right\rangle \exp \left[ - i \omega_ {n} \left(t - \tau_ {\text {c o n t r o l}}\right) \right], \tag {6}
$$

created by another Fourier transform (FT)-limited laser pulse (control pulse) at  $t = \tau_{\mathrm{control}}$  is superposed on the target WP to give the resulting total WP:

$$
\left| \Psi_ {\text {t o t a l}} (r, t) \right\rangle = \sum_ {n} c _ {n} \left| \psi_ {n} (r) \right\rangle \exp \left[ - i \left(\omega_ {n} t - \phi_ {n}\right) \right] + \sum_ {n} d _ {n} \left| \psi_ {n} (r) \right\rangle \exp \left[ - i \omega_ {n} \left(t - \tau_ {\text {c o n t r o l}}\right) \right]. \tag {7}
$$

The population  $\rho_{n}$  of a particular level  $n$  is given by

$$
\begin{array}{l} \rho_ {n} = | \langle n | \Psi_ {\text {t o t a l}} (r, t) \rangle | ^ {2} = | c _ {n} \exp [ - i (\omega_ {n} t - \phi_ {n}) ] + d _ {n} \exp [ - i \omega_ {n} (t - \tau_ {\text {c o n t r o l}}) ] | ^ {2} \\ = \left| c _ {n} \exp \left(i \phi_ {n}\right) + d _ {n} \exp \left(i \omega_ {n} \tau_ {\text {c o n t r o l}}\right) \right| ^ {2} = c _ {n} ^ {2} + d _ {n} ^ {2} + 2 c _ {n} d _ {n} \cos \left(\omega_ {n} \tau_ {\text {c o n t r o l}} - \phi_ {n}\right). \tag {8} \\ \end{array}
$$

From Equation 8, one can see that the phase information  $\phi_{n}$  of each eigenstate of the target WP is now converted to its population  $\rho_{n}$  of the total WP, and the population should be measured easily with a conventional spectroscopic technique. The population  $\rho_{n}$ , however, oscillates with its own frequency  $\omega_{n} / 2\pi$ , which is close to the optical frequency of the laser pulse, so the stability of the delay  $\tau_{\mathrm{control}}$  needs to be much better than the optical cycle of the laser pulse to retrieve  $\phi_{n}$  directly from  $\rho_{n}$ . Bucksbaum and coworkers (49-51) pioneered the experimental implementation of quantum-state holography. They prepared a Rydberg WP in the Cs atom with a femtosecond laser pulse shaped with an acousto-optic modulator and superposed a reference WP prepared with a near FT-limited pulse on that shaped WP. The populations of the Rydberg eigenstates involved in those WPs were measured by the state-selective field ionization method. In their experiments,

FT: Fourier transform

the stability of the delay  $\tau_{\mathrm{control}}$  was not better than the optical cycle,  $\sim 2$  fs, of the laser pulses used, so the cosine term in Equation 8 is averaged to zero over several laser pulses, and the measured populations averaged over several laser pulses  $\langle \rho_n\rangle$  lose any information on  $\phi_{n}$ . This problem was later solved using the APM, as mentioned above (68-70). Instead of stabilizing the delay  $\tau_{\mathrm{control}}$ , Bucksbaum and coworkers employed a covariance technique to calculate the correlation function,

$$
r _ {n m} = \frac {\left\langle \rho_ {n} \rho_ {m} \right\rangle - \left\langle \rho_ {n} \right\rangle \left\langle \rho_ {m} \right\rangle}{(\Delta \rho_ {n}) (\Delta \rho_ {m})} = \cos [ (\omega_ {n} - \omega_ {m}) \tau - \phi_ {n m} ], \tag {9}
$$

with measured populations  $\rho_{n}$  and  $\rho_{m}$  and the standard deviations  $\Delta \rho_{n}$  and  $\Delta \rho_{m}$  to retrieve information on the relative phase  $\phi_{nm}$  of the different states  $n$  and  $m$ . They combined this holography with the feedback loop to actively manipulate the phases and amplitudes of the electronic eigenstates within a Rydberg WP in the Cs atom (Figure 5) (50).

Another new approach retrieves both the amplitude and phase information stored in a WP. As explained in Section 2, phase-jump measurements (Figure 2) have shown that the population ratio of the eigenstates within a WP can be manipulated by WPI with pump and control pulses, whose relative phase is tuned on the attosecond timescale. The population ratio thus manipulated can be retrieved as the LIF excitation spectrum measured by scanning the wavelength of the

![](images/bbbc087c01ed7fdf40a146ab639762698db2c9a68ab8c1ff06847a82c743c722.jpg)  
Figure 5

Rydberg wave packets (WPs) of the Cs atom. The vertical axis denotes the amplitude, and the color denotes the phase. The axis to the right is the  $z$  axis, and the other is the  $x$  axis, with the excitation laser polarized along the  $x$  axis. The range of the  $x$  and  $z$  axes is 1800 a.u., and the vertical axis range is  $1.5 \times 10^{-3}$  a.u. The phase ranges from  $-180$  degrees to 180 degrees in the color bar shown at the bottom of the figure. The top row shows the target WP, which is the only WP that was not measured. All the other rows show the WPs reconstructed from the amplitudes and phases of the eigenstates measured using quantum holography. Each row corresponds to a different control delay  $\tau_{\mathrm{control}}$ , and each new column shows the next iteration in the feedback loop. Figure reprinted from Reference 50.

![](images/65dae0e0daa1e60125f0d5e1e74eabdb8ff83c6b64d0a6af15f20732de7d10a3.jpg)  
Figure 6

Population and phase codes written in the vibrational wave packets (WPs) of the iodine molecule with a pair of femtosecond laser pulses (pump and control pulses) produced by an attosecond phase modulator. The relative phase of the pump and control pulses is increased in steps of  $\sim \pi /2$  from code A to code D. (a) The population distribution of the vibrational eigenstates within the WPs was measured by scanning the wavelength of the nanosecond probe pulse. (b) Real-time evolutions of the WP interference measured with almost the same pump-control phases as for population codes A-D. Figure reprinted from Reference 69.

nanosecond narrow-band probe pulse (Figure 6a). This spectrum is referred to as a population code. Figure 6b shows the real-time evolutions of WPs generated with almost the same pump-control phases with those of the population codes A-D. This temporal evolution is referred to as a phase code. Population codes A and C are barely distinguishable from each other, whereas phase codes A and C are in antiphase and are clearly distinguishable from each other. This  $\pi$  phase shift between phase codes A and C arises from the  $\pi$  shift in the relative phase between the even and odd vibrational eigenstates (69, 70). Therefore, a combination of the population and phase codes

Figure 7  
![](images/b2f03d5dffb18a7f34cb08d49e1bcc3981370cd3edfc5d099300e3c9ce445bf4.jpg)  
Coherent transients in the Rb atom. (a) The temporal evolutions of the population of the  $5\mathrm{p}^2\mathrm{P}_{1/2}$  state resulting from a sequence of FT-limited and chirped pulses. The relative phase of the pulses is  $\theta_0 \cong -0.7$  rad for the lower panel and  $\theta_0 + \pi/2$  for the upper panel. Gray and black traces denote theory and experiment, respectively. (b) The probability amplitude reconstructed from the coherent transients shown in panel  $a$ . Figure reprinted from Reference 62.

![](images/3ee80811d292afff08caa5f64c2a32ecb9e52d5335aab91b92b3d6039b6d6f7f.jpg)

can be regarded as another straightforward and robust approach to providing the full quantum information of a WP (69, 70).

Girard and coworkers (62, 63) have demonstrated another holographic approach to measuring the temporal evolutions of the phase and amplitude of the electronic eigenstate of an atom during its interaction with a chirped ultrashort laser pulse. In their experiments, the  $5\mathrm{s}^2\mathrm{S}_{1/2} - 5\mathrm{p}^2\mathrm{P}_{1/2}$  transition of the Rb atom at  $795~\mathrm{nm}$  was induced with a sequence of the FT-limited and chirped pulses generated with a programmable pulse-shaping device. The temporal evolution of the  $5\mathrm{p}^2\mathrm{P}_{1/2}$  state population was measured with another ultrashort probe pulse by the LIF technique with the (8s, 6d) state being the fluorescent state, as shown in Figure 7a with two different relative phases of the FT-limited and chirped pulses. The first FT-limited pulse creates the population of the  $5\mathrm{p}^2\mathrm{P}_{1/2}$  state to induce an oscillating atomic dipole, and this oscillating dipole interferes with the second chirped laser field to give strong oscillations with a steep rise at approximately 6-7 ps when the laser frequency crosses the resonance. These oscillations are called coherent transients. The analysis of these coherent transients yields the temporal evolutions of the amplitude and phase of the  $5\mathrm{p}^2\mathrm{P}_{1/2}$  state during the interaction with the chirped pulse (Figure 7b).

Bucksbaum and coworkers (83, 84) have demonstrated a completely different approach to retrieving the phase information of a Rydberg WP in the Cs atom by using a terahertz half-cycle pulse. They irradiated a GaAs wafer with an ultrashort optical pulse to produce a half-cycle pulse, which was focused on the Cs atomic beam with an off-axis parabolic mirror. The Rydberg WP was prepared in the Cs atom with an acousto-optic modulator so that one of its constituent Rydberg eigenstates was phase-flipped by  $\pi$  from the others. With an optimized timing and peak field of the half-cycle pulse, the populations were redistributed among those eigenstates so that the phase-flipped state was predominantly amplified, and those redistributed populations were measured with the state-selective field ionization method.

![](images/62c59062e561ef0f2dc1644aff02c461d63d685b02c876669ba978e426223dfa.jpg)  
a

![](images/1b87c0c646299e57065f62cd68a31a08bfdff76e3a8f3a6d595063b9d41ea35d.jpg)  
b

# Figure 8

Schematic of two-color nonlinear wave-packet interferometry. (a) A sequence of the four laser pulses induces couplings among the three electronic states shown in panel  $b$ . The relative phases of the first pair (1 and 2) and the second pair (3 and 4) are locked. Pulses 1 and 2 have a common carrier wavelength, as do pulses 3 and 4. Figure reprinted from Reference 72.

Cina and coworkers (38, 71, 72) recently published important theoretical papers in which they proposed an approach called two-color nonlinear WPI, which uses a sequence of four ultrashort laser pulses (Figure 8a). These four pulses induce couplings among three electronic states  $(g, e, \text{and } f)$  (Figure 8b). The relative phases of the first pair (pulses 1 and 2) and the second pair (pulses 3 and 4) are locked. Pulses 1 and 2 have a common carrier wavelength resonant with the  $e - g$  transition, and pulses 3 and 4 have another common carrier wavelength resonant with the  $f - g$  transition. The initial state is a  $g$ -state vibrational eigenstate, and the final state in the  $f$  state, created after pulse 4, is a superposition of four WPs. They are  $|\mathrm{tar}3\rangle$  and  $|\mathrm{tar}4\rangle$  created with the first-order interactions with pulses 3 and 4, respectively, and  $|\mathrm{ref}321\rangle$  and  $|\mathrm{ref}421\rangle$  created with the third-order interactions with a sequence of pulses 1-2-3 and 1-2-4, respectively. Among those four, the full quantum states of the target WPs  $|\mathrm{tar}3\rangle$  and  $|\mathrm{tar}4\rangle$  are retrieved from their overlaps with the reference WPs  $|\mathrm{ref}421\rangle$  and  $|\mathrm{ref}321\rangle$ , respectively, measured in the two-dimensional interferograms as functions of the interpulse delays  $t_{21}$  and  $t_{32}$ . This nonlinear WPI has an advantage over linear WPI from the viewpoint of quantum-state reconstruction in that it does not require detailed knowledge of the potential curve of the final state.

Aside from the above efforts to retrieve both the amplitude and phase information, the full quantum information of a WP can also be reconstructed from its spatiotemporal evolution. Walmsley and coworkers (85-87) have demonstrated an approach they call emission tomography. They prepared a vibrational WP in the  $A^{1}\Sigma_{\mathrm{u}}^{+}$  state of the  $\mathrm{Na}_{2}$  molecule and measured time- and frequency-resolved spontaneous emission from the WP with the upconversion technique, in which they employed a 60-fs gate pulse mixed with spontaneous emission in a BBO crystal to generate ultraviolet sum-frequency radiation to be monitored by a photomultiplier through a double-prism monochromator. The temporal evolution of the emission spectrum is reconstructed from several scans of the gate pulse delay with different wavelength settings of the monochromator. The emission wavelengths are then converted to internuclear distances with the known molecular potentials.

A similar reconstruction of the spatiotemporal evolution of WP interference has been demonstrated recently. Figure 9a schematically shows WP interference in the  $B$  state of the  $\mathrm{I}_2$  molecule around the half-revival period, in which a single WP initially prepared is bifurcated to two counterpropagating sub-WPs because of the potential anharmonicity. Picometric ripples appear only when the two WPs cross each other. The lifetime of each ripple is no more than  $\sim 100$  fs. These

a  
Figure 9  
![](images/79c9bd6ab7b8690cc3a2dd827e3aa4193de88318ff131dae96915d59063db045.jpg)  
The spatiotemporal evolution of wave-packet (WP) interference. (a) Schematic representation of the interferences of two vibrational WPs in the  $\mathrm{I}_2$  molecule around the half-revival period. Picometric quantum ripples appear and disappear synchronously with the periodic crossing of two counterpropagating WPs.  $T_{\mathrm{cl}}$  is a classical vibrational period of the molecule and is approximately 0.3 ps. (b) Quantum ripples in the  $\mathrm{I}_2$  molecule visualized experimentally (left column) and the theoretical simulation of the experimental signal (middle column) and the WP (right column).  $\lambda_{\mathrm{pr}}$  and  $r$  denote the wavelength of the probe pulse and the internuclear distance, respectively. Figure reprinted from Reference 88.

![](images/cdcbeb5df939d84774b415ad8bbaf47f8a4970eec2e2efc709faed578b029573.jpg)  
b

quantum ripples have been recently visualized (Figure 9b) (88). This visualization employed a pump-probe scheme (Figure 10) in which a probe pulse was used to excite the quantum ripple generated on the  $B$ -state potential curve to the upper  $E$ -state one. The fluorescence intensity from this  $E$ -state was measured as a function of the timing  $\tau_{\mathrm{probe}}$  and the wavelength  $\lambda_{\mathrm{pr}}$  of the probe pulse. Based on the classical Franck-Condon principle, it is reasonable to consider that the  $E-B$  excitation occurs around a particular internuclear distance at which the energy of the probe pulse is equal to the difference of the potential energies of the  $E$  and  $B$  states, which is a function of the internuclear distance  $r$ . The wavelength  $\lambda_{\mathrm{pr}}$ , therefore, is successfully converted to the internuclear distance  $r$ . Thus the space-time image shown in Figure 9b was obtained by measuring eight quantum beats by scanning  $\tau_{\mathrm{probe}}$  with eight different  $\lambda_{\mathrm{pr}}$ ’s and interpolating them along the  $\lambda_{\mathrm{pr}}$  axis. The geometric space-time image of quantum interference thus visualized is called a quantum carpet (89). Quantum carpets are wonderful manifestations of and compelling evidence for the wave nature of matter. The classical analog is the well-known Talbot effect, which was first discovered approximately 170 years ago by Henry Talbot for the white light diffracted by a grating (89). The Talbot carpet is woven on a spatial plane instead of the space-time plane for the quantum carpet and has recently been observed also for atomic beams (90-92). Both the quantum and Talbot carpets originate from interferences among different eigenwaves superposed coherently. The quantum carpet has been studied theoretically in various quantum systems, such as the

Figure 10  
![](images/d00a678cfe480fda381b3b09429bf9d2dd90ce85ca4506e458770ba7d8fdbe5a.jpg)  
Pump-probe scheme visualizing the quantum ripples shown in Figure 9. The intensity of the fluorescence from the  $E$  state was measured as a function of the probe delay  $\tau_{\mathrm{probe}}$  and the probe wavelength  $\lambda_{\mathrm{pr}}$ , which is converted to the internuclear distance  $r$  according to the classical Franck-Condon principle. Figure reprinted from Reference 88.

particle-in-a-box model and other model potentials (93-95), Bose-Einstein condensates (96, 97), the Fermions-in-a-box potential (98), and one-dimensional lattice (99). Deng et al. (100) observed the quantum carpet in Bose-Einstein condensates experimentally in 1999.

Theory predicts that the quantum carpet shown in Figure 9b can be actively designed if we can precisely tune the relative phase of the two counterpropagating WPs schematically shown in Figure 9a. Such an actively designed quantum carpet in the  $\mathrm{I}_2$  molecule has been demonstrated recently by using the APM (101).

# 4. INFORMATION PROCESSING WITH MOLECULAR EIGENSTATES

The high-speed information processing in our modern societies is based on a highly integrated circuit, and its further integration is still in progress. It is generally predicted, however, that the downsizing of the present Si-based electronic circuit will reach its fundamental limit in a couple of decades (102, 103) because current leakage is unavoidable with insulators thinned to atomic levels and will also cause heat and error. These fundamental problems exist even with sophisticated molecular electronics (104), as long as a real charge is used as a carrier of information. Instead of a real charge, however, one can use wave functions of neutral systems as information carriers, making them a promising candidate for a new strategy that could possibly avoid leakage problems. Furthermore, as described above, an ultrashort laser pulse can access many eigenstates simultaneously in an atom or molecule. The amplitudes and phases of those eigenstates can be manipulated individually with a pulse shaper. It is not unrealistic that 10 vibrational eigenstates in a diatomic molecule are coherently superposed to generate a WP. As mentioned in

Figure 11  
![](images/cc8202dda8ce3c60a02ccddc3a63932a7b5c474af0d90ccab50626a33ab5f77a.jpg)  
Schematic of the experimental setup for the implementation of discrete Fourier transform based on the temporal evolution of a vibrational wave packet in the  $\mathrm{I}_2$  molecule. Figure reprinted from Reference 123.

Section 3, each eigenstate has its own amplitude and phase information, which could be binarized as  $[0,1]$  and  $[0,\pi]$ , respectively, to give four possible binary codes:  $(00)$ ,  $(0\pi)$ ,  $(10)$ , and  $(1\pi)$ ; each vibrational eigenstate serves as two bits in this case. Accordingly,  $4^{10} = 1,048,576$  different kinds of information can be encoded to the WP in a simple diatomic molecule on the angstrom scale. This inherent property as a high-density memory makes it meaningful to investigate information processing with eigenstates of atoms and molecules. Molecules are especially now expected to be a promising medium for large-scale quantum computing (105-109); the dipole-dipole interaction of molecules is expected to serve as a useful resource for two-qubit operation based on quantum correlation. Hence it is promising to study information processing with molecular eigenstates, which we refer to as molecular eigenstate-based information processing (MEIP) hereafter, for both high-density classical information processing and quantum information processing.

Read and write operations are the most fundamental operations in any type of information processing. For MEIP, the read procedure is the retrieval of amplitude and phase information stored in a WP, and the write procedure is the creation of arbitrarily shaped WPs with shaped ultrashort laser pulses. As described above, the development of these most fundamental operations is almost finished.

The next step should be the development of logic gates. A number of theoretical papers on logic gates for MEIP have proposed their implementation in the vibrational, rovibrational, and vibronic manifolds of diatomic and polyatomic molecules (110-131). De Vivie-Riedle and coworkers (110-115) have proposed the use of shaped strong femtosecond laser pulses to carry out basic quantum gates such as phase shift, Hadamard transform, and CNOT, employing vibrational eigenstates of different vibrational modes of a polyatomic molecule. Leone and coworkers (116, 117) have experimentally demonstrated a classical multiple-input AND gate and the Deutch-Jozsa algorithm with a superposition of rovibrational eigenstates in the  $E$  state of the  $\mathrm{Li}_2$  molecule, using a shaped femtosecond laser pulse. A recent theoretical simulation demonstrated that discrete Fourier transform (DFT) can be executed in the temporal evolution of a vibrational WP created with a shaped laser pulse in the  $B$  state of the  $\mathrm{I}_2$  molecule (123). The proposed experimental system is shown schematically in Figure 11. As for the four-element DFT, for example, an input  $\mathbf{L}$  such as (1,1,1,1) is base-transformed to the coefficient vector  $\mathbf{k} = (a_v,a_{v + 2},a_{v + 3},a_{v + 4})$  of a set of vibrational eigenstates  $v,v + 2,v + 3$ , and  $v + 4$  in the  $B$  state of the  $\mathrm{I}_2$  molecule:

$$
\mathbf {k} = \mathbf {w} ^ {- 1} \mathbf {L}, \tag {10}
$$

MEIP: molecular eigenstate-based information processing

where the  $4 \times 4$  DFT matrix  $\mathbf{G}$  is diagonalized as

$$
\mathbf {G} = \mathbf {w} \mathbf {D} \mathbf {w} ^ {- 1}. \tag {11}
$$

DFT: discrete Fourier transform

Therefore, the DFT of the input  $\mathbf{L}$  is

$$
\mathbf {G L} = \mathbf {w D k}, \tag {12}
$$

where the diagonal matrix  $\mathbf{D}$  represents the temporal evolution of  $\mathbf{k}$  for one-fourth the classical vibrational period  $T_{\mathrm{vib}}$ . In the actual experiment, therefore,  $\mathbf{k}$  is input to the vibrational WP with a shaped laser pulse produced by the pulse shaper placed in one arm of the interferometer shown in Figure 11. The amplitudes and phases of that target WP after its temporal evolution for  $1 / 4T_{\mathrm{vib}}$  are measured holographically, with the reference WP generated with the unshaped pulse coming from the other arm of the interferometer, scanning the relative phase of the shaped and unshaped pulses. The  $\mathbf{Dk}$  thus experimentally obtained is finally transformed by  $\mathbf{w}$  to give the final result GL. The transform matrix  $\mathbf{w}$  is common to any arbitrary input  $\mathbf{L}$ . This DFT has been implemented experimentally quite recently (132).

Scaling is a key issue in MEIP for both classical and quantum processes. Palao & Kosloff (119) carried out numerical simulations to propose one possible approach that uses a shaped intense laser pulse to induce intrapulse high-order stimulated Raman transitions between two multivibrational-level systems in the electronically excited and ground states. In this scheme, the number of transition pathways  $O(M^{I / 2\pi})$  scales exponentially with intensity  $(I)$ , where  $M$  is the number of vibrational levels involved in the Raman transitions, to show what they refer to as moderate scaling. Another approach addresses each single molecule instead of processing an ensemble average of many molecules. This approach needs a molecule trapped in space. To realize such a trapped molecule, several innovative efforts are being made to generate a cold diatomic molecule from laser-cooled alkaline atoms by using photoassociation (133-171) and/or a Feshbach resonance between the free and weakly bound states of the ground electronic states, which are Zeeman-shifted by external magnetic fields (149, 151, 170-177). Ye, Jin, and their coworkers have recently combined a Feshbach resonance and stimulated Raman transitions to successfully produce the KRb molecule in the low vibrational states of the  $a^3\Sigma^+$  and  $X^1\Sigma^+$  states (170, 171). Moreover, this experiment has been performed with heteronuclear molecules, whose dipole-dipole interaction is expected to serve as a useful resource for two-qubit operation as mentioned above (105-109). Aside from these approaches based on the photoassociation of laser-cooled atoms, direct cooling of the ground-state molecules such as CaH, CaF, PbO, OH, NH, CO, ND₃, OH, and H₂CO is in progress, too (178-191).

# 5. FUTURE PERSPECTIVES

Ultrafast coherent control and ultracold physics have developed independently. With the recent extensive efforts on cold molecules mentioned above, however, these two research fields are rapidly merging. Once stable cold molecules are prepared, they could be controlled coherently with broadband ultrashort laser pulses to realize highly selective reaction control. The various resources developed in the field of coherent control may be powerful tools even for the creation of a cold molecule itself (139, 146, 147, 150-162, 164-169). The ultrafast coherent control of ultracold atoms and molecules will be a fascinating new target.

Testing coherence and its control has been done not only in isolated atoms and simple molecules, but also in a complex many-bodied system such as molecules in the liquid phase and large polyatomic molecules (22-29, 192-194), impurity molecules in the rare-gas matrices and ice (18, 195-198), nanostructures (12, 16, 199), surfaces (200-202), and bulk solids (13-15,

203-207). Recent examples include Fleming and coworkers' (194) use of the two-color photon echo technique to investigate the role of electronic coherence in a bacterial reaction center and Miller and coworkers' (29) application of a genetic algorithm and feedback approach to the shaped pulse control of the all-trans to 13-cis photoisomerization of the retinal molecule in bacteriorhodopsin. These biological systems may be the future target of coherent control (208). The coherent control of these complex systems needs to be accompanied by the management of decoherence.

Testing and managing decoherence are other key issues to pursue (209-211). Decoherence should be tested and understood from the viewpoint of the boundary between the quantum and classical worlds. It is not clear how the microscopic coherent world is smoothly connected to the macroscopic classical world. As long as coherent control is based on the wave nature of matter, pursuing coherent control in a variety of complexities should provide an opportunity to test the quantum worldview. We may find a clue to help us better understand the mystery.

# DISCLOSURE STATEMENT

The author is not aware of any biases that might be perceived as affecting the objectivity of this review.

# ACKNOWLEDGMENTS

The author acknowledges all the collaborators who have coauthored the papers introduced in this review. H. Katsuki and H. Chiba (Institute for Molecular Science) especially have played indispensable roles in initiating and developing this challenging and difficult research. This work was partly supported by a Grant in Aid from MEXT of Japan.

# LITERATURE CITED

1. Shapiro M, Brumer P. 1986. Laser control of product quantum state populations in unimolecular reactions. J. Chem. Phys. 84:4103-4  
2. Shapiro M, Hepburn JW, Brumer P. 1988. Simplified laser control of unimolecular reactions: simultaneous  $(\omega_{1},\omega_{3})$  excitation. Chem. Phys. Lett. 149:451-54  
3. Tannor DJ, Rice SA. 1985. Control selectivity of chemical reaction via control of wave packet evolution. J. Chem. Phys. 83:5013-18  
4. Tannor DJ, Kosloff R, Rice SA. 1986. Coherent pulse sequence induced control of selectivity of reactions: exact quantum mechanical calculations. J. Chem. Phys. 85:5805-20  
5. Chen C, Yin YY, Elliot DS. 1990. Interference between optical transitions. Phys. Rev. Lett. 64:507-10  
6. Zhu L, Kleiman V, Li X, Lu SP, Trentelman K, Gordon RJ. 1995. Coherent laser control of the product distribution obtained in the photoexcitation of HI. Science 270:77-80  
7. Zhu L, Suto K, Fiss JA, Wada R, Seideman T, Gordon RJ. 1997. Effect of resonances on the coherent control of the photoionization and photodissociation of HI and DI. Phys. Rev. Lett. 79:4108-11  
8. Baumert T, Grosser M, Thalweiser R, Gerber G. 1991. Femtosecond time-resolved molecular multiphoton ionization: the  $\mathrm{Na}_2$  system. Phys. Rev. Lett. 67:3753-56  
9. Potter ED, Herek JL, Pedersen S, Liu Q, Zewail AH. 1992. Femtosecond laser control of a chemical reaction. Nature 355:66-68  
10. Scherer NF, Carlson RJ, Matro A, Du M, Ruggiero AJ, et al. 1991. Fluorescence-detected wave packet interferometry: time resolved molecular spectroscopy with sequences of femtosecond phase-locked pulses. J. Chem. Phys. 95:1487-511  
11. Scherer NF, Matro A, Ziegler LD, Du M, Carlson RJ, et al. 1992. Fluorescence-detected wave packet interferometry. II. Role of rotations and determination of the susceptibility. J. Chem. Phys. 96:4180-94

12. Heberle AP, Baumberg JJ, Kohler K. 1995. Ultrafast coherent control and destruction of excitons in quantum wells. Phys. Rev. Lett. 75:2598-601  
13. Wehner MU, Ulm MH, Chemla DS, Wegener M. 1998. Coherent control of electron-LO-phonon scattering in bulk GaAs. Phys. Rev. Lett. 80:1992-95  
14. Ogawa S, Nagano H, Petek H, Heberle AP. 1997. Optical dephasing in Cu (111) measured by interferometric two-photon time-resolved photoemission. Phys. Rev. Lett. 78:1339-42  
15. Ogawa S, Nagano H, Petek H. 1999. Phase and energy relaxation in an antibonding surface state: Cs/Cu(111). Phys. Rev. Lett. 82:1931-34  
16. Kamada H, Gotoh H, Temmyo J, Takagahara T, Ando H. 2001. Exciton Rabi oscillation in a single quantum dot. Phys. Rev. Lett. 87:246401  
17. Mihailovic D, Dvorskev D, Kabanov VV, Demsr J, Forro L, Berger H. 2002. Femtosecond data storage, processing, and search using collective excitations of a macroscopic quantum state. Appl. Phys. Lett. 80:871-73  
18. Fushitani M, Bargheer M, Gehr M, Schwentner N. 2005. Pump-probe spectroscopy with phase-locked pulses in the condensed phase: decoherence and control of vibrational wavepackets. Phys. Chem. Chem. Phys. 7:3143-49  
19. Kohler B, Yakovlev VV, Che J, Krause JL, Messina M, et al. 1995. Quantum control of wave packet evolution with tailored femtosecond pulses. Phys. Rev. Lett. 74:3360-63  
20. Bardeen CJ, Che J, Wilson KR, Yakovlev VV, Apkarian VA, et al. 1997. Quantum control of  $\mathrm{I}_2$  in the gas phase and in condensed phase solid Kr matrix. J. Chem. Phys. 106:8486-503  
21. Judson RS, Rabitz H. 1992. Teaching lasers to control molecules. Phys. Rev. Lett. 68:1500-3  
22. Bardeen CJ, Yakovlev VV, Wilson KR, Carpenter SD, Weber PM, Warren WS. 1997. Feedback quantum control of molecular electronic population transfer. Chem. Phys. Lett. 280:151-58  
23. Assion A, Baumert T, Bergt M, Brixner T, Kiefer B, et al. 1998. Control of chemical reactions by feedback-optimized phase-shaped femtosecond laser pulses. Science 282:919-22  
24. Levis RJ, Menkir GM, Rabitz H. 2001. Selective bond dissociation and rearrangement with optimally tailored, strong-field laser pulses. Science 292:709-13  
25. Herek JL, Wohlleben W, Cogdell RJ, Zeidler D, Motzkus M. 2002. Quantum control of energy flow in light harvesting. Nature 417:533-35  
26. Daniel C, Full J, González L, Lupulescu C, Manz J, et al. 2003. Deciphering the reaction dynamics underlying optimal control laser fields. Science 299:536-39  
27. Pearson BJ, Buckbaum PH. 2004. Control of Raman lasing in the nonimpulsive regime. Phys. Rev. Lett. 92:243003; Erratum. 94:209901  
28. Vogt G, Krampert G, Niklaus P, Nuernberger P, Gerber G. 2005. Optimal control of photoisomerization. Phys. Rev. Lett. 94:068305  
29. Prokhorenko VI, Nagy AM, Waschuk SA, Brown LS, Birge RR, Miller RJD. 2006. Coherent control of retinal isomerization in bacteriorhodopsin. Science 313:1257-61  
30. Gordon RJ, Rice SA. 1997. Active control of the dynamics of atoms and molecules. Annu. Rev. Phys. Chem. 48:601-41  
31. Rice SA, Zhao M. 2000. Optical Control of Molecular Dynamics. New York: Wiley & Sons  
32. Rabitz H, de Vivie-Riedle R, Motzkus M, Kompa K. 2000. Whither the future of controlling quantum phenomena. Science 288:824-28  
33. Rice SA. 2001. Interfering for the good of a chemical reaction. Nature 409:422-26  
34. Shapiro M, Brumer P. 2003. Coherent control of molecular dynamics. Rep. Prog. Phys. 66:859-942  
35. Shapiro M, Brumer P. 2003. Principles of the Quantum Control of Molecular Processes. New York: Wiley & Sons  
36. Dantus M, Lozovoy VV. 2004. Experimental coherent laser control of physicochemical processes. *Chem. Rev.* 104:1813-60  
37. Fielding HH. 2005. Rydberg wavepackets in molecules: from observation to control. Annu. Rev. Phys. Chem. 56:91-117  
38. Cina JA. 2008. Wave-packet interferometry and molecular state reconstruction: spectroscopic adventures on the left-hand side of the Schrödinger equation. Annu. Rev. Phys. Chem. 59:319-42

39. Noordam LD, Duncan DI, Gallagher TF. 1992. Ramsey fringes in atomic Rydberg wave packets. Phys. Rev. A 45:4734-37  
40. Christian JF, Broers B, Hoogenraad JH, van der Zande WJ, Noordam LD. 1993. Rubidium electronic wavepackets probed by a phase-sensitive pump-probe technique. Opt. Commun. 103:79-84  
41. Broers B, Christian JF, Hoogenraad JH, van der Zande WJ, van Linden van den Heuvel HB, Noordam LD. 1993. Time-resolved dynamics of electronic wave packets above the classical field-ionization threshold. Phys. Rev. Lett. 71:344-47  
42. Marmet L, Held H, Raithel G, Yeazell JA, Walther H. 1994. Observation of quasi-Landau wave packets. Phys. Rev. Lett. 72:3779-82  
43. Wals J, Fielding HH, Christian JF, Snoek LC, van der Zande WJ, van Linden van den Heuvelt HB. 1994. Observation of Rydberg wave packet dynamics in a Coulombic and magnetic field. Phys. Rev. Lett. 72:3783-86  
44. Christian JF, Broers B. 1995. Cross correlations in Ramsey pump-probe interferometry. Phys. Rev. A 52:3655-60  
45. Jones RR, Raman CS, Schumacher DW, Bucksbaum PH. 1993. Ramsey interference in strongly driven Rydberg systems. Phys. Rev. Lett. 71:2575-78  
46. Jones RR, Schumacher DW, Gallagher TF, Bucksbaum PH. 1995. Bound-state interferometry using incoherent light. J. Phys. B 28:L405-11  
47. Jones RR. 1995. Multiphoton ionization enhancement using two phase-coherent laser pulses. Phys. Rev. Lett. 75:1491-94  
48. Schumacher DW, Hoogenraad JH, Pinkos D, Bucksbaum PH. 1995. Programmable cesium Rydberg wave packets. Phys. Rev. A 52:4719-26  
49. Weinacht TC, Ahn J, Bucksbaum PH. 1998. Measurement of the amplitude and phase of a sculpted Rydberg wave packet. Phys. Rev. Lett. 80:5508-11  
50. Weinacht TC, Ahn J, Bucksbaum PH. 1999. Controlling the shape of a quantum wavefunction. Nature 397:233-35  
51. Ahn J, Weinacht TC, Bucksbaum PH. 2000. Information storage and retrieval through quantum phase. Science 287:463-65  
52. Noel MW, Stroud CR Jr. 1995. Young's double-slit interferometry within an atom. Phys. Rev. Lett. 75:1252-55  
53. Noel MW, Stroud CR Jr. 1996. Excitation of an atomic electron to a coherent superposition of macroscopically distinct states. Phys. Rev. Lett. 77:1913-16  
54. Noel MW, Stroud CR Jr. 1997. Shaping an atomic electron wave packet. Opt. Express 1:176-85  
55. Blanchet V, Nicole C, Bouchene MA, Girard B. 1997. Temporal coherent control in two-photon transitions: from optical interferences to quantum interferences. Phys. Rev. Lett. 78:2716-19  
56. Bouchene MA, Blanchet V, Nicole C, Melikechi N, Girard B, et al. 1998. Temporal coherent control induced by wave packet interferences in one and two photon atomic transitions. Eur. Phys. J. D 2:131-41  
57. Bellini M, Bartoli A, Hänsch TW. 1997. Two-photon Fourier spectroscopy with femtosecond light pulses. Opt. Lett. 22:540-42  
58. VerletJRR, Stavros VG, Minns RS, Fielding HH. 2002. Controlling the angular momentum composition of a Rydberg electron wave packet. Phys. Rev. Lett. 89:263004  
59. Verlet JRR, Stavros VG, Minns RS, Fielding HH. 2003. Controlling the radial dynamics of Rydberg wavepackets in Xe using phase-locked optical pulse sequences. J. Phys. B 36:3683-96  
60. Minns RS, Patel R, Verlet JRR, Fielding HH. 2003. Optical control of the rotational angular momentum of a molecular Rydberg wave packet. Phys. Rev. Lett. 91:243601  
61. Carley RE, Boléat ED, Minns RS, Petel R, Fielding HH. 2005. Interfering Rydberg wave packets in Na. J. Phys. B 38:1907-22  
62. Monmayrant A, Chatel B, Girard B. 2006. Quantum state measurement using coherent transients. Phys. Rev. Lett. 96:103002  
63. Monmayrant A, Chatel B, Girard B. 2006. Real time quantum state holography using coherent transients. Opt. Commun. 264:256-63  
64. Blanchet V, Bouchene MA, Cabrol O, Girard B. 1995. One-color coherent control in  $\mathrm{Cs_2}$ : observation of 2.7 fs beats in the ionization signal. Chem. Phys. Lett. 233:491-99

65. Blanchet V, Bouchene MA, Girard B. 1998. Temporal coherent control in the photoionization of  $\mathrm{Cs}_2$ : theory and experiment. J. Chem. Phys. 108:4862-76  
66. Warmuth CH, Tortschanoff A, Milota F, Shapiro M, Prior Y, et al. 2000. Studying vibrational wavepacket dynamics by measuring fluorescence interference fluctuations. J. Chem. Phys. 112:5060-69  
67. Warmuth CH, Tortschanoff A, Milota F, Leibscher M, Shapiro M, et al. 2001. Molecular quantum dynamics in a thermal system: fractional wave packet revivals probed by random-phase fluorescence interferometry. J. Chem. Phys. 114:9901-10  
68. Ohmori K, Sato Y, Nikitin EE, Rice SA. 2003. High-precision molecular wave-packet interferometry with HgAr dimers. Phys. Rev. Lett. 91:243003  
69. Ohmori K, Katsuki H, Chiba H, Honda M, Hagihara Y, et al. 2006. Real-time observation of phase-controlled molecular wave-packet interference. Phys. Rev. Lett. 96:093002  
70. Katsuki H, Hosaka K, Chiba H, Ohmori K. 2007. Read and write amplitude and phase information by using high-precision molecular wave-packet interferometry. Phys. Rev. A 76:013403  
71. Humble TS, Cina JA. 2004. Molecular state reconstruction by nonlinear wave packet interferometry. Phys. Rev. Lett. 93:060402  
72. Humble TS, Cina JA. 2006. Nonlinear wave-packet interferometry and molecular state reconstruction in a vibrating and rotating diatomic molecule. J. Phys. Chem. B 110:18879-92  
73. Boléat ED, Fielding HH. 2005. Optical control of the quantum-state distribution of vibrational wave packets using trains of phase-locked pulses. Mol. Phys. 103:491-99  
74. Ballard JB, Stauffer HU, Mirowski E, Leone SR. 2002. Simultaneous control of time-dependent population transfer dynamics and wave-packet quantum interferences in  $\mathrm{Li}_2$  by shaped ultrafast pulses. Phys Rev. A 66:043402  
75. Lerch EBW, Dai X, Gilb S, Torres EA, Leone SR. 2006. Control of  $\mathrm{Li}_2$  wave packet dynamics by modification of the quantum mechanical amplitude of a single state. J. Chem. Phys. 124:044306  
76. Skovsen E, Machholm M, Ejdrup T, Thogersen J, Stapelfeldt H. 2002. Imaging and control of interfering wave packets in a dissociating molecule. Phys. Rev. Lett. 89:133004  
77. Petersen C, Peronne E, Thogersen J, Stapelfeldt H, Machholm M. 2004. Control and imaging of interfering wave packets in dissociating  $\mathrm{I}_2$  molecules. Phys. Rev. A 70:033404  
78. Wollenhaupt M, Assion A, Liese D, Sarpe-Tudoran Ch, Baumert T. 2002. Interferences of ultrashort free electron wave packets. Phys. Rev. Lett. 89:173001  
79. Degert J, Meier C, Chatel B, Girard B. 2003. Coherent control of matter-wave interference in molecular predissociation. Phys. Rev. A 67:041402  
80. Chen X, Yeazell JA. 1997. Reconstruction of engineered atomic wave functions via phase-dependent population measurements. Phys. Rev. A 56:2316-20  
81. Leichtle C, Schleich WP, Averbukh ISh, Shapiro M. 1998. Quantum state holography. Phys. Rev. Lett. 80:1418-21  
82. Averbukh ISh, Shapiro M, Leichtle C, Schleich WP. 1999. Reconstructing wave packets by quantum-state holography. Phys. Rev. A 59:2163-73  
83. Ahn J, Hutchinson DN, Rangan C, Bucksbaum PH. 2001. Quantum phase retrieval of a Rydberg wave packet using a half-cycle pulse. Phys. Rev. Lett. 86:1179-82  
84. Ahn J, Rangan C, Hutchinson DN, Bucksbaum PH. 2002. Quantum-state information retrieval in a Rydberg-atom data register. Phys. Rev. A 66:022312  
85. Dunn TJ, Sweetser JN, Walmsley IA, Radzewicz C. 1993. Experimental determination of the dynamics of a molecular nuclear wave packet via the spectra of spontaneous emission. Phys. Rev. Lett. 70:3388-91  
86. Dunn TJ, Walmsley IA, Mukamel S. 1995. Experimental determination of the quantum-mechanical state of a molecular vibrational mode using fluorescence tomography. Phys. Rev. Lett. 74:884-87  
87. Walmsley IA, Raymer MG. 1995. Detecting quantum superpositions of classically distinguishable states of a molecule. Phys. Rev. A 52:681-85  
88. Katsuki H, Chiba H, Girard B, Meier C, Ohmori K. 2006. Visualizing picometric quantum ripples of ultrafast wave-packet interference. Science 311:1589-92  
89. Berry M, Marzoli I, Schleich WP. 2001. Quantum carpets, carpets of light. Phys. World 14:39-44  
90. Clauser JF, Li S. 1994. Talbot-vonLau atom interferometry with cold slow potassium. Phys. Rev. A 49:R2213-16

91. Chapman MS, Ekstrom CR, Hammond TD, Schmiedmayer J, Tannian BE, et al. 1995. Near-field imaging of atom diffraction gratings: the atomic Talbot effect. Phys. Rev. A 51:R14-17  
92. Nowak S, Kurtsiefer Ch, Pfau T, David C. 1997. High-order Talbot fringes for atomic matter waves. Opt. Lett. 22:1430-32  
93. Kaplan AE, Stifter P, van Leeuwen KAH, Lamb WE Jr, Schleich WP. 1998. Intermode traces: fundamental interference phenomenon in quantum and wave physics. Phys. Scr. T76:93-97  
94. Friesch OM, Marzoli I, Schleich WP. 2000. Quantum carpets woven by Wigner functions. New J. Phys. 2:4  
95. Kaplan AE, Marzoli I, Lamb WE Jr, Schleich WP. 2000. Multimode interference: highly regular pattern formation in quantum wave-packet evolution. Phys. Rev. A 61:032101  
96. Ruostekoski J, Kneer B, Schleich WP, Rempe G. 2001. Interference of a Bose-Einstein condensate in a hard-wall trap: from the nonlinear Talbot effect to the formation of vorticity. Phys. Rev. A 63:043613  
97. Gammal A, Kamchatnov AM. 2004. Temporal Talbot effect in interference of matter waves from arrays of Bose-Einstein condensates and transition to Fraunhofer diffraction. Phys. Lett. A 324:227-34  
98. Nest M. 2006. Quantum carpets and correlated dynamics of several fermions. Phys. Rev. A 73:023613  
99. Mulken O, Blumen A. 2005. Spacetime structures of continuous-time quantum walks. Phys. Rev. E 71:036128  
100. Deng L, Hagley EW, Denschlag J, Simsarian JE, Edwards M, et al. 1999. Temporal, matter-wave-dispersion Talbot effect. Phys. Rev. Lett. 83:5407-11  
101. Katsuki H, Chiba H, Meier C, Girard B, Ohmori K. 2009. Actively tailored spatiotemporal images of quantum interference on the picometer and femtosecond scales. Phys. Rev. Lett. In press  
102. Normile D. 2001. The end: not here yet, but coming soon. Science 293:787  
103. Lundstrom M. 2003. Moore's law forever? Science 299:210-11  
104. Green JE, ChoiJW, Boukai A, Bunimovich Y, Johnston-Halperin E, et al. 2007. A 160-kilobit molecular electronic memory patterned at  $10^{11}$  bits per square centimeter. Nature 445:414-17  
105. DeMille D. 2002. Quantum computation with trapped polar molecules. Phys. Rev. Lett. 88:067901  
106. Micheli A, Brennen GK, Zoller P. 2006. A toolbox for lattice-spin models with polar molecules. Nat. Phys. 2:341-47  
107. Andre A, DeMille D, Doyle JM, Lukin MD, Maxwell SE, et al. 2006. A coherent all-electrical interface between polar molecules and mesoscopic superconducting resonators. Nat. Phys. 2:636-42  
108. Rabl P, DeMille D, Doyle JM, Lukin MD, Schoelkopf RJ, Zoller P. 2006. Hybrid quantum processors: molecular ensembles as quantum memory for solid state circuits. Phys. Rev. Lett. 97:033003  
109. Rabl P, Zoller P. 2007. Molecular dipolar crystals as high-fidelity quantum memory for hybrid quantum computing. Phys. Rev. A 76:042308  
110. Tesch CM, Kurtz L, de Vivie-Riedle R. 2001. Applying optimal control theory for elements of quantum computation in molecular systems. Chem. Phys. Lett. 343:633-41  
111. Tesch CM, de Vivie-Riedle R. 2002. Quantum computation with vibrationally excited molecules. Phys. Rev. Lett. 89:157901  
112. Korff BMR, Troppmann U, Kompa KL, de Vivie-Riedle R. 2005. Manganese pentacarbonyl bromide as candidate for a molecular qubit system operated in the infrared regime. J. Chem. Phys. 123:244509  
113. Troppmann U, de Vivie-Riedle R. 2005. Mechanisms of local and global molecular quantum gates and their implementation prospects. J. Chem. Phys. 122:154105  
114. Gollub C, Troppmann U, de Vivie-Riedle R. 2006. The role of anharmonicity and coupling in quantum computing based on vibrational qubits. New J. Phys. 8:48  
115. de Vivie-Riedle R, Troppmann U. 2007. Femtosecond lasers for quantum information technology. *Chem. Rev.* 107:5082-100  
116. Amitay Z, Kosloff R, Leone SR. 2002. Experimental coherent computation of a multiple-input AND gate using pure molecular superpositions. Chem. Phys. Lett. 359:8-14; Erratum. 361:530  
117. Vala J, Amitay Z, Zhang B, Leone SR, Kosloff R. 2002. Experimental implementation of the Deutsch-Jozsa algorithm for three-qubit functions using pure coherent molecular superpositions. Phys. Rev. A 66:062316  
118. Palao JP, Kosloff R. 2002. Quantum computing by an optimal control algorithm for unitary transformations. Phys. Rev. Lett. 89:188301

119. Palao JP, Kosloff R. 2003. Optimal control theory for unitary transformations. Phys. Rev. A 68:062308; Erratum. 69:059901  
120. Bihary Z, Glenn DR, Lidar DA, Apkarian VA. 2002. An implementation of the Deutsch-Jozsa algorithm on molecular vibronic coherences through four-wave mixing: a theoretical study. *Chem. Phys. Lett.* 360:459-65  
121. Shapiro EA, Khavkine I, Spanner M, Ivanov MY. 2003. Strong-field molecular alignment for quantum logic and quantum control. Phys. Rev. A 67:013406  
122. Ohtsuki Y. 2005. Simulating the Deutsch-Jozsa algorithm using vibration states of  $\mathrm{I}_2$  excited by optimally designed gate pulses. Chem. Phys. Lett. 404:126-31  
123. Teranishi Y, Ohtsuki Y, Hosaka K, Chiba H, Katsuki H, Ohmori K. 2006. Implementation of quantum gate operations in molecules with weak laser fields. J. Chem. Phys. 124:114110  
124. Sola IR, Malinovsky VS, Santamaría J. 2004. Implementing quantum gates on oriented optical isomers. *J. Chem. Phys.* 120:10955-60  
125. Suzuki S, Mishima K, Yamashita K. 2005. Ab initio study of optimal control of ammonia molecular vibrational wavepackets: towards molecular quantum computing. *Chem. Phys. Lett.* 410:358-64  
126. Shioya K, Mishima K, Yamashita K. 2007. Quantum computing using molecular vibrational and rotational modes. Mol. Phys. 105:1283-95  
127. Zhao M, Babikov D. 2006. Phase control in the vibrational qubit. J. Chem. Phys. 125:024105  
128. Cheng T, Brown A. 2006. Quantum computing based on vibrational eigenstates: pulse area theorem analysis. J. Chem. Phys. 124:034111  
129. Menzel-Jones C, Shapiro M. 2007. Robust operation of a universal set of logic gates for quantum computation using adiabatic population transfer between molecular levels. Phys. Rev. A 75:052308  
130. Weidinger D, Gruebele M. 2007. Quantum computation with vibrationally excited polyatomic molecules: effects of rotation, level structure, and field gradients. Mol. Phys. 105:1999-2008  
131. Bomble L, Lauvergnat D, Remacle F, Desouter-Lecomte M. 2008. Vibrational computing: simulation of a full adder by optimal control. J. Chem. Phys. 128:064110  
132. Hosaka K, Chiba H, Katsuki H, Shimada H, Ohmori K. 2008. Manuscript in preparation  
133. Thorsheim HR, Weiner J, Julienne PS. 1987. Laser-induced photoassociation of ultracold sodium atoms. Phys. Rev. Lett. 58:2420-23  
134. Band YB, Julienne PS. 1995. Ultracold-molecule production by laser-cooled atom photoassociation. Phys. Rev. A 51:R4317-20  
135. Jones KM, Tiesinga E, Lett PD, Julienne PS. 2006. Ultracold photoassociation spectroscopy: long-range molecules and atomic scattering. Rev. Mod. Phys. 78:483-535  
136. Cline RA, Miller JD, Heinzen DJ. 1994. Study of  $\mathrm{Rb_2}$  long-range states by high-resolution photoassociation spectroscopy. Phys. Rev. Lett. 73:632-35; Errata. 73:2636  
137. Fioretti A, Comparat D, Crubellier A, Dulieu O, Masnou-Seeuws F, Pillet P. 1998. Formation of cold  $\mathrm{Cs}_2$  molecules through photoassociation. Phys. Rev. Lett. 80:4402-5  
138. Vanhaecke N, Comparat D, Crubellier A, Pillet P. 2004. Photoassociation spectroscopy of ultra-cold long-range molecules. C. R. Phys. 5:161-69  
139. Viteau M, Chotia A, Allegrini M, Bouloufa N, Dulieu O, et al. 2008. Optical pumping and vibrational cooling of molecules. Science 321:232-34  
140. Wang H, Gould PL, Stwalley WC. 1996. Photoassociative spectroscopy of ultracold  $^{39}\mathrm{K}$  atoms in a high-density vapor-cell magneto-optical trap. Phys. Rev. A 53:R1216-19  
141. Wang H, Gould PL, Stwalley WC. 1997. Long-range interaction of  $^{39}\mathrm{K}(4\mathrm{s}) + {}^{39}\mathrm{K}(4\mathrm{p})$  asymptote by photoassociative spectroscopy. I. The  $0_{\mathrm{g}}^{-}$ pure long-range state and the long-range potential constants. J. Chem. Phys. 106:7899-912  
142. Nikolov AN, Eyler EE, Wang XT, Li J, Wang H, et al. 1999. Observation of ultracold ground-state potassium molecules. Phys. Rev. Lett. 82:703-6  
143. Farooqi SM, Tong D, Krishnan S, Stanojevic J, Zhang YP, et al. 2003. Long-range molecular resonances in a cold Rydberg gas. Phys. Rev. Lett. 91:183002  
144. Wang D, Qi J, Stone MF, Nikolayeva O, Wang H, et al. 2004. Photoassociative production and trapping of ultracold KRb molecules. Phys. Rev. Lett. 93:243005

145. Nagel SB, Mickelson PG, Saenz AD, Martinez YN, Chen YC, et al. 2005. Photoassociative spectroscopy at long range in ultracold strontium. Phys. Rev. Lett. 94:083004  
146. Wright MJ, Gensemer SD, Vala J, Kosloff R, Gould PL. 2005. Control of ultracold collisions with frequency-chirped light. Phys. Rev. Lett. 95:063001  
147. Wright MJ, Pechkis JA, Carini JL, Kallush S, Kosloff R, Gould PL. 2007. Coherent control of ultracold collisions with chirped light: direction matters. Phys. Rev. A 75:051401  
148. McKenzie C, Hecker Denschlag J, Haffner H, Browaeys A, de Araujo LEE, et al. 2002. Photoassociation of sodium in a Bose-Einstein condensate. Phys. Rev. Lett. 88:120403  
149. Lang F, Winkler K, Strauss C, Grimm R, Hecker Denschlag J. 2008. Ultracold triplet molecules in the rovibrational ground state. Phys. Rev. Lett. 101:133005  
150. Vala J, Dulieu O, Masnou-Seeuws F, Pillet P, Kosloff R. 2000. Coherent control of cold-molecule formation through photoassociation using a chirped-pulsed-laser field. Phys. Rev. A 63:013412  
151. Koch CP, Palao JP, Kosloff R, Masnou-Seeuws F. 2004. Stabilization of ultracold molecules using optimal control theory. Phys. Rev. A 70:013402  
152. Luc-Koenig E, Kosloff R, Masnou-Seeuws F, Vatasescu M. 2004. Photoassociation of cold atoms with chirped laser pulses: time-dependent calculations and analysis of the adiabatic transfer within a two-state model. Phys. Rev. A 70:033414  
153. Koch CP, Masnou-Seeuws F, Kosloff R. 2005. Creating ground state molecules with optical Feshbach resonances in tight traps. Phys. Rev. Lett. 94:193001  
154. Koch CP, Kosloff R, Luc-Koenig E, Masnou-Seeuws F, Crubellier A. 2006. Photoassociation with chirped laser pulses: calculation of the absolute number of molecules per pulse. J. Phys. B 39:S1017-41  
155. Koch CP, Luc-Koenig E, Masnou-Seeuws F. 2006. Making ultracold molecules in a two-color pump-dump photoassociation scheme using chirped pulses. Phys. Rev. A 73:033408  
156. Koch CP, Kosloff R, Masnou-Seeuws F. 2006. Short-pulse photoassociation in rubidium below the  $\mathrm{D}_1$  line. Phys. Rev. A 73:043409  
157. Poschinger U, Salzmann W, Wester R, Weidemüller M, Koch CP, Kosloff R. 2006. Theoretical model for ultracold molecule formation via adaptive feedback control. J. Phys. B 39:S1001-15  
158. Kallush S, Kosloff R. 2008. Unitary photoassociation: one-step production of ground-state bound molecules. Phys. Rev. A 77:023421  
159. Fatemi F, Jones KM, Wang H, Walmsley I, Lett PD. 2001. Dynamics of photoinduced collisions of cold atoms probed with picosecond laser pulses. Phys. Rev. A 64:033421  
160. Brown BL, Dicks AJ, Walmsley IA. 2006. Coherent control of ultracold molecule dynamics in a magnetooptical trap by use of chirped femtosecond laser pulses. Phys. Rev. Lett. 96:173002  
161. Salzmann W, Poschinger U, Wester R, Weidemüller M, Merli A, et al. 2006. Coherent control with shaped femtosecond laser pulses applied to ultracold molecules. Phys. Rev. A 73:023414  
162. Salzmann W, Mullins T, Eng J, Albert M, Wester R, et al. 2008. Coherent transients in the femtosecond photoassociation of ultracold molecules. Phys. Rev. Lett. 100:233003  
163. Deiglmayr J, Grochola A, Repp M, Mörtlbauer K, Glick C, et al. 2008. Formation of ultracold polar molecules in the rovibrational ground state. Phys. Rev. Lett. 101:133004  
164. Schafer-Bung B, Mitric R, Bonacic-Koutecky V. 2006. Photostabilization of the ultracold  $\mathrm{Rb}_2$  molecule by optimal control. J. Phys. B 39:S1043-53  
165. Trachy ML, Veshapidze G, Shah MH, Jang HU, DePaola BD. 2007. Photoassociation in cold atoms via ladder excitation. Phys. Rev. Lett. 99:043003  
166. Veshapidze G, Trachy ML, Jang HU, Fehrenbach CW, DePaola BD. 2007. Pathway for two-color photoassociative ionization with ultrafast optical pulses in a Rb magneto-optical trap. Phys. Rev. A. 76:051401  
167. Pe'er A, Shapiro EA, Stowe MC, Shapiro M, Ye J. 2007. Precise control of molecular dynamics with a femtosecond frequency comb. Phys. Rev. Lett. 98:113004  
168. Shapiro EA, Shapiro M, Pe'er A, Ye J. 2007. Photoassociation adiabatic passage of ultracold Rb atoms to form ultracold  $\mathrm{Rb}_2$  molecules. Phys. Rev. A 75:013405; Erratum. 78:029903  
169. Shapiro EA, Pe'er A, Ye J, Shapiro M. 2008. Piecewise adiabatic population transfer in a molecule via a wave packet. Phys. Rev. Lett. 101:023601

170. Ospelkaus S, Pe'er A, Ni K-K, Zirbel JJ, Neyenhuis B, et al. 2008. Efficient state transfer in an ultracold dense gas of heteronuclear molecules. Nat. Phys. 4:622-26  
171. Ni K-K, Ospelkaus S, de Miranda MHG, Pe'er A, Neyenhuis B, et al. 2008. A high phase-space-density gas of polar molecules. Science 322:231-35  
172. Xu K, Mukaiyama T, Abo-Shaer JR, Chin JJK, Miller DE, Ketterle W. 2003. Formation of quantum-degenerate sodium molecules. Phys. Rev. Lett. 91:210402  
173. Zwierlein MW, Stan CA, Schunck CH, Raupach SMF, Gupta S, et al. 2003. Observation of Bose-Einstein condensation of molecules. Phys. Rev. Lett. 91:250401  
174. Jochim S, Bartenstein M, Altmeyer A, Hendl G, Riedl S, et al. 2003. Bose-Einstein condensation of molecules. Science 302:2101-3  
175. Greiner M, Regal CA, Jin DS. 2003. Emergence of a molecular Bose-Einstein condensate from a Fermi gas. Nature 426:537-40  
176. O'Hara KM, Hemmer SL, Gehm ME, Granade SR, Thomas JE. 2002. Observation of a strongly interacting degenerate Fermi gas of atoms. Science 298:2179-82  
177. Kinect J, Turlapov A, Thomas JE, Chen Q, Stajic J, Levin K. 2005. Heat capacity of a strongly interacting Fermi gas. Science 307:1296-99  
178. Weinstein JD, deCarvalho R, Guillet T, Friedrich B, Doyle JM. 1998. Magnetic trapping of calcium monohydride molecules at millikelvin temperatures. Nature 395:148-50  
179. Maussang K, Egorov D, Helton JS, Nguyen SV, Doyle JM. 2005. Zeeman relaxation of CaF in low-temperature collisions with helium. Phys. Rev. Lett. 94:123002  
180. Maxwell SE, Brahms N, deCarvalho R, Glenn DR, Helton JS, et al. 2005. High-flux beam source for cold, slow atoms or molecules. Phys. Rev. Lett. 95:173201  
181. Campbell WC, Tsikata E, Lu H-I, van Buuren LD, Doyle JM. 2007. Magnetic trapping and Zeeman relaxation of NH  $(X^{3}\Sigma^{-})$ . Phys. Rev. Lett. 98:213001  
182. Campbell WC, Groenenboom GC, Lu H-I, Tsikata E, Doyle JM. 2008. Time-domain measurement of spontaneous vibrational decay of magnetically trapped NH. Phys. Rev. Lett. 100:083003  
183. Bethlem HL, Berden G, Meijer G. 1999. Decelerating neutral dipolar molecules. Phys. Rev. Lett. 83:1558-61  
184. Bethlem HL, Berden G, Crompvoets FMH, Jongma RT, van Roij AJA, Meijer G. 2000. Electrostatic trapping of ammonia molecules. Nature 406:491-94  
185. Bochinski JR, Hudson ER, Lewandowski HJ, Meijer G, Ye J. 2003. Phase space manipulation of cold free radical OH molecules. Phys. Rev. Lett. 91:243001  
186. van de Meerakker SYT, Smeets PHM, Vanhaecke N, Jongma RT, Meijer G. 2005. Deceleration and electrostatic trapping of OH radicals. Phys. Rev. Lett. 94:023004  
187. Hudson ER, Bochinski JR, Lewandowski HJ, Sawyer BC, Ye J. 2004. Efficient Stark deceleration of cold polar molecules. Eur. Phys. f. D 31:351-58  
188. Sawyer BC, Lev BL, Hudson ER, Stuhl BK, Lara M, et al. 2007. Magnetoelectrostatic trapping of ground state OH molecules. Phys. Rev. Lett. 98:253002  
189. Rangwala SA, Junglen T, Rieger T, Pinkse PWH, Rempe G. 2003. Continuous source of translationally cold dipolar molecules. Phys. Rev. A 67:043406  
190. Junglen T, Rieger T, Rangwala SA, Pinkse PWH, Rempe G. 2004. Slow ammonia molecules in an electrostatic quadrupole guide. Eur. Phys. J. D 31:365-73  
191. Rieger T, Junglen T, Rangwala SA, Pinkse PWH, Rempe G. 2005. Continuous loading of an electrostatic trap for polar molecules. Phys. Rev. Lett. 95:173002  
192. Gershgoren E, Bartels RA, Fourkas JT, Tobey R, Murnane MM, Kapteyn HC. 2003. Simplified setup for high-resolution spectroscopy that uses ultrashort pulses. Opt. Lett. 28:361-63  
193. Hoki K, Brumer P. 2005. Mechanisms in adaptive feedback control: photoisomerization in a liquid. Phys. Rev. Lett. 95:168305  
194. Lee H, Cheng Y-C, Fleming GR. 2007. Coherence dynamics in photosynthesis: protein protection of excitonic coherence. Science 316:1462-65  
195. Gehr M, Schwentner N. 2005. Effective chromophore potential, dissipative trajectories, and vibrational energy relaxation: Br $_2$  in Ar matrix. J. Chem. Phys. 123:244506

196. Bihary Z, Karavitis M, Apkarian VA. 2004. Onset of decoherence: six-wave mixing measurements of vibrational decoherence on the excited electronic state of  $\mathrm{I}_2$  in solid argon. J. Chem. Phys. 120:8144-56  
197. Kiviniemi T, Aumanen J, Myllyperkiö P, Apkarian VA, Pettersson M. 2005. Time-resolved coherent anti-Stokes Raman-scattering measurements of  $\mathrm{I}_2$  in solid Kr: vibrational dephasing on the ground electronic state at 2.6–32 K. J. Chem. Phys. 123:064509  
198. Senekerimyan V, Goldschleger I, Apkarian VA. 2007. Vibronic dynamics of  $\mathrm{I}_2$  trapped in amorphous ice: coherent following of cage relaxation. J. Chem. Phys. 127:214511  
199. Franco I, Shapiro M, Brumer P. 2007. Robust ultrafast currents in molecular wires through Stark shifts. Phys. Rev. Lett. 99:126802  
200. Watanabe K, Takagi N, Matsumoto Y. 2004. Direct time-domain observation of ultrafast dephasing in absorbate-substrate vibration under the influence of a hot electron bath: Cs adatoms on Pt(111). Phys. Rev. Lett. 92:057401  
201. Watanabe K, Takagi N, Matsumoto Y. 2005. Mode-selective excitation of coherent surface phonons on alkali-covered metal surfaces. Phys. Chem. Chem. Phys. 7:2697-700  
202. Fuyuki M, Watantabe K, Matsumoto Y. 2006. Coherent surface phonon dynamics at K-covered Pt(111) surfaces investigated by time-resolved second harmonic generation. Phys. Rev. B 74:195412  
203. Hase M, Itano T, Mizoguchi K, Nakashima S. 1998. Selective enhancement of coherent optical phonons using Thz-rate pulse train. Jpn. J. Appl. Phys. 37:L281-83  
204. Hase M, Kitajima M, Constantinescu AM, Petek H. 2003. The birth of a quasiparticle in silicon observed in time-frequency space. Nature 426:51-54  
205. Ishioka K, Hase M, Kitajima M, Petek H. 2006. Coherent optical phonons in diamond. Appl. Phys. Lett. 89:231916; Erratum. 92:019903  
206. Ishioka K, Hase M, Kitajima M, Wirtz L, Rubio A, Petek H. 2008. Ultrafast electron-phonon decoupling in graphite. Phys. Rev. B 77:121402  
207. Lee KG, Kim DS, Yee KJ, Lee HS. 2006. Control of coherent optical phonon excitations in GaN using femtosecond pulse shaping. Phys. Rev. B 74:113201  
208. Mitric R, Bonacic-Koutecky V. 2007. Optimal control of mode-selective femtochemistry in multidimensional systems. Phys. Rev. A 76:031405  
209. Meekhof DM, Monroe C, King BE, Itano WM, Wineland DJ. 1996. Generation of nonclassical motional states of a trapped atom. Phys. Rev. Lett. 76:1796-99; Erratum. 77:2346  
210. Myatt CJ, King BE, Turchette QA, Sackett CA, Kielpinski D, et al. 2000. Decoherence of quantum superpositions through coupling to engineered reservoirs. Nature 403:269-73  
211. Turchette QA, Myatt CJ, King BE, Sackett CA, Kielpinski D, et al. 2000. Decoherence and decay of motional quantum states of a trapped atom coupled to engineered reservoirs. Phys. Rev. A 62:053807

![](images/4239014c3a46fddc6776798aebdb43d74b83ba0458ea3bafa7521378a81c8818.jpg)

Annual Review of

Physical Chemistry

Volume 60, 2009

# Contents

Frontispiece xiv

Sixty Years of Nuclear Moments John S. Waugh 1

Dynamics of Liquids, Molecules, and Proteins Measured with Ultrafast 2D IR Vibrational Echo Chemical Exchange Spectroscopy M.D. Fayer 21

Photofragment Spectroscopy and Predissociation Dynamics of Weakly Bound Molecules  
Hanna Reisler 39

Second Harmonic Generation, Sum Frequency Generation, and  $\chi^{(3)}$ : Dissecting Environmental Interfaces with a Nonlinear Optical Swiss Army Knife Franz M. Geiger 61

Dewetting and Hydrophobic Interaction in Physical and Biological Systems Bruce J. Berne, John D. Weeks, and Rubong Zhou 85

Photoelectron Spectroscopy of Multiply Charged Anions Xue-Bin Wang and Lai-Sheng Wang 105

Intrinsic Particle Properties from Vibrational Spectra of Aerosols  
Ómar F. Sigurbjörnsson, George Firanescu, and Ruth Signorell 127

Nanofabrication of Plasmonic Structures
Joel Henzie, Feungboon Lee, Min Hyung Lee, Warefta Hasan, and Teri W. Odom ..... 147

Chemical Synthesis of Novel Plasmonic Nanoparticles  
Xianmao Lu, Matthew Rycenga, Sara E. Skrabalak, Benjamin Wiley, and Younan Xia 167

Atomic-Scale Templates Patterned by Ultrahigh Vacuum Scanning Tunneling Microscopy on Silicon Michael A. Walsh and Mark C. Hersam 193

DNA Excited-State Dynamics: From Single Bases to the Double Helix  
Chris T. Middleton, Kimberly de La Harpe, Charlene Su, Yu Kay Law, Carlos E. Crespo-Hernández, and Bern Kohler 217

Dynamics of Light Harvesting in Photosynthesis  
Yuan-Chung Cheng and Graham R. Fleming 241  
High-Resolution Infrared Spectroscopy of the Formic Acid Dimer Ozgur Birer and Martina Havenith 263  
Quantum Coherent Control for Nonlinear Spectroscopy and Microscopy Yaron Silberberg 277  
Coherent Control of Quantum Dynamics with Sequences of Unitary Phase-Kick Pulses Luis G.C. Rego, Lea F. Santos, and Victor S. Batista 293  
Equation-Free Multiscale Computation: Algorithms and Applications
Ioannis G. Kevrekidis and Giovanni Samaey 321  
Chirality in Nonlinear Optics
Levi M. Haupert and Garth f. Simpson 345  
Physical Chemistry of DNA Viruses Charles M. Knobler and William M. Gelbart 367  
Ultrafast Dynamics in Reverse Micelles Nancy E. Levinger and Laura A. Swafford 385  
Light Switching of Molecules on Surfaces
Wesley R. Browne and Ben L. Feringa 407  
Principles and Progress in Ultrafast Multidimensional Nuclear Magnetic Resonance Mor Mishkovsky and Lucio Frydman 429  
Controlling Chemistry by Geometry in Nanoscale Systems L. Lizana, Z. Konkoli, B. Bauer, A. Fesorka, and O. Orwar 449  
Active Biological Materials Daniel A. Fletcher and Phillip L. Geissler 469  
Wave-Packet and Coherent Control Dynamics Kenji Ohmori 487

# Indexes

Cumulative Index of Contributing Authors, Volumes 56-60 513  
Cumulative Index of Chapter Titles, Volumes 56-60 516

# Errata

An online log of corrections to Annual Review of Physical Chemistry articles may be found at http://physchem.annualreviews.org/errata.shtml