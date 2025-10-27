# Microwave Quantum Illumination

Shabir Barzanjeh, $^{1}$  Saikat Guha, $^{2}$  Christian Weedbrook, $^{3}$  David Vitali, $^{4}$  Jeffrey H. Shapiro, $^{5}$  and Stefano Pirandola $^{6,*}$

$^{1}$ Institute for Quantum Information, RWTH Aachen University, 52056 Aachen, Germany

$^{2}$ Quantum Information Processing Group, Raytheon BBN Technologies, Cambridge, Massachusetts 02138, USA

$^{3}$ QKD Corporation, 60 Saint George Street, Toronto M5S 3G4, Canada

$^{4}$ School of Science and Technology, University of Camerino, Camerino, Macerata 62032, Italy

$^{5}$ Research Laboratory of Electronics, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, USA

$^{6}$ Department of Computer Science and York Centre for Quantum Technologies, University of York, York YO10 5GH, United Kingdom (Received 9 October 2014; revised manuscript received 13 January 2015; published 27 February 2015)

Quantum illumination is a quantum-optical sensing technique in which an entangled source is exploited to improve the detection of a low-reflectivity object that is immersed in a bright thermal background. Here, we describe and analyze a system for applying this technique at microwave frequencies, a more appropriate spectral region for target detection than the optical, due to the naturally occurring bright thermal background in the microwave regime. We use an electro-optomechanical converter to entangle microwave signal and optical idler fields, with the former being sent to probe the target region and the latter being retained at the source. The microwave radiation collected from the target region is then phase conjugated and upconverted into an optical field that is combined with the retained idler in a joint-detection quantum measurement. The error probability of this microwave quantum-illumination system, or quantum radar, is shown to be superior to that of any classical microwave radar of equal transmitted energy.

DOI: 10.1103/PhysRevLett.114.080503

PACS numbers: 03.67.-a, 03.65.Ta, 07.07.Df, 42.50.-p

Introduction. Entanglement is the foundation of many quantum information protocols [1-3], but it is easily destroyed by environmental noise that, in almost all cases, kills any benefit such nonclassical correlations would, otherwise, have provided. Quantum illumination (QI) [4,5], however, is a notable exception: it thrives in environments so noisy that they are entanglement breaking.

The original goal of QI was to detect the presence of a low-reflectivity object, immersed in a bright thermal background, by interrogating the target region with one optical beam while retaining its entangled counterpart for subsequent joint measurement with the light returned from that target region. Although the thermal noise destroys the entanglement, theory showed that the QI system will significantly outperform a classical (coherent-state) system of the same transmitted energy [5-7]. Later, a QI protocol was proposed for secure communication [8] whose experimental realization [9] showed that entanglement's benefit could, indeed, survive an entanglement-breaking channel. Because of this feature, QI is perhaps one of the most surprising protocols for quantum sensing. Together with quantum reading [10-13], it represents a practical example of quantum channel discrimination [3], in which entanglement is beneficial for a technologically driven information task.

So far, QI has only been demonstrated at optical wavelengths [9,14,15], for which naturally occurring background radiation contains far less than one photon per mode on average, even though QI's performance advantage requires the presence of a bright background. The QI communication protocol from [8,9] deals with this problem in a natural way by purposefully injecting amplified

spontaneous emission noise to thwart eavesdropping. By contrast, similar noise injection in QI target-detection experiments has to be considered artificial, because better target-detection performance would be obtained without it. The appropriate wavelengths for QI-enabled target detection, thus, lie in the microwave region, in which almost all radar systems operate and in which there is naturally occurring background radiation containing many photons per mode on average. In general, the development of quantum information techniques for microwave frequencies is quite challenging [16-18].

In this Letter, we introduce a novel QI target-detection system that operates in the microwave regime. Its transmitter uses an electro-optomechanical (EOM) converter [19-23] in which a mechanical resonator entangles signal and idler fields emitted from microwave and optical cavities [19,20]. Its receiver employs another EOM device—operating as a phase-conjugator and a wavelength converter—whose optical output is used in a joint measurement with the retained idler. We show that our system dramatically outperforms a conventional (coherent-state) microwave radar of the same transmitted energy, achieving an orders-of-magnitude lower detection-error probability. Moreover, our system can be realized with state-of-the-art technology, and is suited to such potential applications as standoff sensing of low-reflectivity objects, and environmental scanning of electrical circuits. Thanks to its enhanced sensitivity, our system could also lead to low-flux noninvasive techniques for protein spectroscopy and biomedical imaging.

Electro-optomechanical converter. As depicted in Fig. 1(a), the EOM converter couples a microwave-cavity

![](images/6a4c805d0ae66060f4fbb13a17b9d56837c0a600cb2f0317000cb5ff9f908cce.jpg)  
FIG. 1 (color online). (a) Schematic of the EOM converter in which driven microwave and optical cavities are coupled by a mechanical resonator. (b) Microwave-optical QI using EOM converters. The transmitter's EOM converter entangles microwave and optical fields. The receiver's EOM converter transforms the returning microwave field to the optical domain while performing a phase-conjugate operation.

mode (annihilation operator  $\hat{a}_w$ , frequency  $\omega_w$ , damping rate  $\kappa_w$ ) to an optical-cavity mode (operator  $\hat{a}_o$ , frequency  $\omega_o$ , damping rate  $\kappa_o$ ) through a mechanical resonator (operator  $\hat{b}$ , frequency  $\omega_M$ , damping rate  $\gamma_M$ ) [20-22]. In the frame rotating at the frequencies of the microwave and optical driving fields, the interaction between the cavities' photons and the resonator's phonons is governed by the Hamiltonian [24]

$$
\hat {H} = \hbar \omega_ {M} \hat {b} ^ {\dagger} \hat {b} + \hbar \sum_ {j = w, o} [ \Delta_ {0, j} + g _ {j} (\hat {b} + \hat {b} ^ {\dagger}) ] \hat {a} _ {j} ^ {\dagger} \hat {a} _ {j} + \hat {H} _ {\mathrm {d r i}}.
$$

Here,  $g_{j}$  is the coupling rate between the mechanical resonator and cavity  $j$ , which is driven at frequency  $\omega_{j} - \Delta_{0,j}$  by the coherent-driving Hamiltonian  $\hat{H}_{\mathrm{dri}}$  [24].

The electro-optomechanical coupling rates  $g_{j}$  are typically small, so that we can linearize the Hamiltonian by expanding the cavity modes around their steady-state field amplitudes  $\hat{c}_{j} = \hat{a}_{j} - \sqrt{N_{j}}$ , where the  $N_{j} \gg 1$  are the mean numbers of cavity photons induced by the pumps [19,29]. In the interaction picture with respect to the free Hamiltonian, we may then write [24]

$$
\hat {H} = \hbar G _ {o} \left(\hat {c} _ {o} \hat {b} + \hat {b} ^ {\dagger} \hat {c} _ {o} ^ {\dagger}\right) + \hbar G _ {w} \left(\hat {c} _ {w} \hat {b} ^ {\dagger} + \hat {b} \hat {c} _ {w} ^ {\dagger}\right), \tag {1}
$$

where  $G_{j} = g_{j}\sqrt{N_{j}}$  is the multiphoton coupling rate. This expression assumes that the effective cavity detunings satisfy  $\Delta_w = -\Delta_o = \omega_M$  and that the resonator is in its fast-oscillation regime, so that the red sideband drives the microwave cavity while the blue sideband drives the optical cavity, and we can neglect terms oscillating at  $\pm 2\omega_{M}$ .

Equation (1) shows that the mechanical resonator mediates a delayed interaction between the optical and microwave cavity modes. Its first term is a parametric down-conversion interaction that entangles the mechanical resonator and the optical cavity mode. This entanglement is

transmitted to the propagating optical mode  $\hat{d}_o$ , if the optomechanical rate  $G_o^2 /\kappa_o$  exceeds the decoherence rate of the mechanical resonator  $r = \gamma_{M}\bar{n}_{b}^{T}\approx \gamma_{M}k_{B}T_{\mathrm{EOM}} / \hbar \omega_{M}$ , where  $k_{B}$  is Boltzmann's constant,  $T_{\mathrm{EOM}}$  is the EOM converter's absolute temperature,  $\bar{n}_b^T = [e^{\hbar \omega_M / (k_BT_{\mathrm{EOM}})} - 1]^{-1}$ , and the approximation presumes  $k_{B}T_{\mathrm{EOM}}\gg \hbar \omega_{M}$ , as will be the case for the parameter values assumed later. The second term in Eq. (1) is a beam-splitter interaction between the mechanical resonator and the microwave cavity mode that transfers the entanglement to the propagating microwave field  $\hat{d}_w$ , as long as the microwave-mechanical rate satisfies  $G_w^2 /\kappa_w > r$  [29,30].

Microwave-optical entanglement.-The output propagating modes can be expressed in terms of the intracavity quantum noise operators,  $\hat{c}_{j,\mathrm{in}}$ , and the quantum Brownian noise operator,  $\hat{b}_{\mathrm{int}}$ , via [24]

$$
\hat {d} _ {w} = A _ {w} \hat {c} _ {w, \mathrm {i n}} - B \hat {c} _ {o, \mathrm {i n}} ^ {\dagger} - C _ {w} \hat {b} _ {\mathrm {i n t}}, \tag {2}
$$

$$
\hat {d} _ {o} = B \hat {c} _ {w, \mathrm {i n}} ^ {\dagger} + A _ {o} \hat {c} _ {o, \mathrm {i n}} - C _ {o} \hat {b} _ {\mathrm {i n t}} ^ {\dagger}, \tag {3}
$$

where  $A_{j}$ ,  $B$ , and  $C_{j}$  depend on the cooperativity terms  $\Gamma_{j} = G_{j}^{2} / \kappa_{j}\gamma_{M}$  as given in [24]. The  $\hat{c}_{w,\mathrm{in}},\hat{c}_{o,\mathrm{in}}$  and  $\hat{b}_{\mathrm{int}}$  modes in Eqs. (2) and (3) are in independent thermal states whose average photon numbers,  $\bar{n}_w^T$ $\bar{n}_o^T$  ,and  $\bar{n}_b^T$  ,are given by temperature-TEOM Planck laws at their respective frequencies. It follows that the propagating modes,  $\hat{d}_w$  and  $\hat{d}_o$  , are in a zero-mean, jointly Gaussian state completely characterized by the second moments,

$$
\bar {n} _ {w} \equiv \langle \hat {d} _ {w} ^ {\dagger} \hat {d} _ {w} \rangle = | A _ {w} | ^ {2} \bar {n} _ {w} ^ {T} + | B | ^ {2} (\bar {n} _ {o} ^ {T} + 1) + | C _ {w} | ^ {2} \bar {n} _ {b} ^ {T},
$$

$$
\bar {n} _ {o} \equiv \langle \hat {d} _ {o} ^ {\dagger} \hat {d} _ {o} \rangle = | B | ^ {2} (\bar {n} _ {w} ^ {T} + 1) + | A _ {o} | ^ {2} \bar {n} _ {o} ^ {T} + | C _ {o} | ^ {2} (\bar {n} _ {b} ^ {T} + 1),
$$

$$
\langle \hat {d} _ {w} \hat {d} _ {o} \rangle = A _ {w} B (\bar {n} _ {w} ^ {T} + 1) - B A _ {o} \bar {n} _ {o} ^ {T} + C _ {w} C _ {o} (\bar {n} _ {b} ^ {T} + 1).
$$

The propagating microwave and optical fields will be entangled if and only if the metric  $\mathcal{E} \equiv |\langle \hat{d}_w \hat{d}_o \rangle| / \sqrt{\bar{n}_w \bar{n}_o}$  is greater than one [24]. As we can see from Fig. 2, there is a wide region where  $\mathcal{E} > 1$  in the plane of the cooperativity parameters,  $\Gamma_w$  and  $\Gamma_o$ , varied by varying the microwave and optical powers driving their respective cavities, and assuming experimentally achievable system parameters [29,31]. The threshold condition  $\mathcal{E} = 1$  almost coincides with the boundary between the stable and unstable parameter regions, as given by the Routh-Hurwitz criterion [32].

The quality of our microwave-optical source can also be evaluated using measures of quantum correlations, as is typical in quantum information. Since the QI's advantage is computed at a fixed mean number of microwave photons  $\bar{n}_w$  irradiated through the target, the most powerful quantum resources are expected to be those maximizing their quantum correlations per microwave photon emitted. Following this physical intuition, we analyze our source in terms of the normalized log negativity [34]  $E_N / \bar{n}_w$  and the normalized coherent information [35,36]  $I(o\langle w) / \bar{n}_w$ .

![](images/169237ca5fae34f167eb9113d2ed4b493a0d2bc77b8407c2be082465761584bd.jpg)

![](images/8341cf38c59feb45083dcdce6c567378a22531b77ab063d59c520b6ee562f0a4.jpg)

![](images/dfc0bd635b186b7c256236a70bf200cc86fad3aa737051baf603435285a28600.jpg)  
FIG. 2 (color online). Performance of our microwave-optical source versus the cooperativity parameters  $\Gamma_w$  and  $\Gamma_o$ . We show the behavior of the entanglement metric  $\mathcal{E}$  (abstract units) in panel (a), the normalized logarithmic negativity  $E_N / \bar{n}_w$  (ebits per microwave photon) in panel (b), the normalized coherent information  $I(o\rangle w) / \bar{n}_w$  (qubits per microwave photon) in panel (c), and the normalized quantum discord  $D(w|o) / \bar{n}_w$  (discordant bits per microwave photon) in panel (d). In all panels, we assume experimentally achievable parameters [29,31]: a 10-ng-mass mechanical resonator with  $\omega_M / 2\pi = 10\mathrm{MHz}$  and  $Q = 30\times 10^{3}$ ; a microwave cavity with  $\omega_w / 2\pi = 10\mathrm{GHz}$  and  $\kappa_w = 0.2\omega_M$ ; and a 1-mm-long optical cavity with  $\kappa_o = 0.1\omega_M$  driven by a 1064-nm-wavelength laser. The opto-mechanical and electro-mechanical coupling rates are  $g_0 / 2\pi = 115.512\mathrm{Hz}$  and  $g_w / 2\pi = 0.327\mathrm{Hz}$ , and the entire EOM converter is held at temperature  $T_{\mathrm{EOM}} = 30\mathrm{mK}$ . In each panel, the boundary between stable and unstable operation was obtained from the Routh-Hurwitz criterion [32].

![](images/e8fd5389d9da18a1540513a2a9f0a965fb592d6bec0e9d86de1bdc02cfcc2468.jpg)

Respectively, they represent an upper and a lower bound to the mean number of entanglement bits (ebits) which are distillable for each microwave photon emitted by the source [24]. Furthermore, since our source is in a mixed state (more precisely, a two-mode squeezed thermal state), we also quantify its normalized quantum discord [24,37]  $D(w|o) / \bar{n}_w$ , which captures the quantum correlations carried by each microwave photon. As we can see from Fig. 2, our source has a remarkable performance in producing distillable ebits and discordant bits for each microwave photon emitted.

Microwave quantum illumination. For QI target detection, our signal-idler mode pair analysis must be extended to a continuous-wave EOM converter whose  $W_{m}$ -Hz-bandwidth [38] output fields are used in a  $t_m$ -sec-duration measurement involving  $M = t_{m}W_{m}\gg 1$  independent, identically distributed (iid) mode pairs. The  $M$  signal modes interrogate the target region that is equally likely to contain (hypothesis  $H_{1}$ ) or not contain (hypothesis  $H_0$ ) a low-reflectivity object. Either way, the microwave field that is returned consists of  $M$  iid modes. Using  $\hat{c}_R$  to denote the annihilation operator for the mode returned from transmission of  $\hat{d}_w$ , we have that  $\hat{c}_R = \hat{c}_B$  under hypothesis  $H_0$

and  $\hat{c}_R = \sqrt{\eta}\hat{d}_w + \sqrt{1 - \eta}\hat{c}_B$ , under hypothesis  $H_{1}$ . Here,  $0 < \eta \ll 1$  is the round-trip transmitter-to-target-to-receiver transmissivity (including propagation losses and target reflectivity), and the background-noise mode,  $\hat{c}_B$ , is in a thermal state with temperature- $T_B$  Planck-law average photon number  $\bar{n}_B$  under  $H_0$ , and in a thermal state with  $\bar{n}_B / (1 - \eta) \approx \bar{n}_B$  under  $H_1$  [5]. See Fig. 1(b).

Under  $H_{1}$ , the returned microwave and the retained optical fields are in a zero-mean, jointly Gaussian state with a nonzero phase-sensitive cross correlation  $\langle \hat{c}_R\hat{d}_o\rangle$  that is invariant to the  $\bar{n}_B$  value, while  $\langle \hat{c}_R^\dagger \hat{c}_R\rangle$  increases with increasing  $\bar{n}_B$ . Consequently, the returned and retained radiation under  $H_{1}$  will not be entangled when

$$
\bar {n} _ {B} \geq \bar {n} _ {B} ^ {\mathrm {t h r e s h}} \equiv \eta (| \langle \hat {d} _ {w} \hat {d} _ {o} \rangle | ^ {2} / \bar {n} _ {o} - \bar {n} _ {w}).
$$

Microwave-to-optical phase-conjugate receiver.-The receiver passes the  $M$  return modes into the microwave cavity of another (identical) EOM converter to produce  $M$  iid optical-output modes each given by  $\hat{d}_{\eta ,o} = B\hat{c}_R^\dagger +A_o\hat{c}_{o,\mathrm{in}}^\prime -C_o\hat{b}_{\mathrm{int}}^\dagger$  where  $\{\hat{c}_{w,\mathrm{in}}^{\prime},\hat{c}_{o,\mathrm{in}}^{\prime},\hat{b}_{\mathrm{int}}^{\prime}\}$  have the same states as their counterparts in the transmitter's EOM converter. The receiver's EOM converter, thus, phase conjugates the returned microwave field and upconverts it to an optical field. This output is combined with the retained idler on a 50-50 beam splitter whose outputs are photodetected and their photon counts-over the  $t_m$  -sec-long measurement interval--are subtracted to yield an outcome from which a minimum error-probability decision about object absence or presence will be made [6]. For  $M\gg 1$  , the resulting error probability is [6,24]  $P_{\mathrm{QI}}^{(M)} = \mathrm{erfc}(\sqrt{\mathrm{SNR}_{\mathrm{QI}}^{(M)} / 8}) / 2$  ,with  $\mathrm{SNR}_{\mathrm{QI}}^{(M)}$  being the QI system's signal-to-noise ratio for its  $M$  mode pairs [24] and  $\operatorname {erfc}(\dots)$  being the complementary error function [6].

Comparison with classical microwave transmitters. Suppose that a coherent-state microwave transmitter emitting  $M\bar{n}_w$  photons on average, with  $\bar{n}_w$  equaling the mean number of microwave photons per mode emitted by our source—is used to assess target absence or presence. Homodyne detection of the microwave field returned from the target region followed by minimum error-probability processing of its output results in an error probability [6]  $P_{\mathrm{coh}}^{(M)} = \mathrm{erfc}(\sqrt{\mathrm{SNR}_{\mathrm{coh}}^{(M)}} /8) / 2$  , in terms of this system's signal-to-noise ratio,  $\mathrm{SNR}_{\mathrm{coh}}^{(M)} = 4\eta M\bar{n}_w / (2\bar{n}_B + 1)$  . This performance approximates the error exponent of the quantum Chernoff bound [39-41] computed for  $M\gg 1$  implying that homodyne detection is the asymptotically optimal receiver for target detection when a coherent-state transmitter is employed.

Figure 3 plots  $P_{\mathrm{QI}}^{(M)}$  and  $P_{\mathrm{coh}}^{(M)}$  versus  $\log_{10} M$  for the EOM converter parameters given in Fig. 2 and  $\eta = 0.07$ . It assumes  $\Gamma_w = 5181.95$  and  $\Gamma_o = 668.43$  (implying  $\bar{n}_w = 0.739$  and  $\bar{n}_o = 0.681$ ) and  $T_B = 293 \, \mathrm{K}$  (implying

![](images/314ea5a8eb891cb0352c35a0b5f1ca357424beeedb104f958612c03dfaf82308.jpg)  
FIG. 3 (color online).  $P_{\mathrm{QI}}^{(M)}$  and  $P_{\mathrm{coh}}^{(M)}$  versus the time-bandwidth product,  $M$ , assuming  $\eta = 0.07$ ,  $\Gamma_w = 5181.95$  and  $\Gamma_o = 668.43$  (implying  $\bar{n}_w = 0.739$  and  $\bar{n}_o = 0.681$ ), and room temperature  $T_B = 293 \, \mathrm{K}$  (implying  $\bar{n}_B = 610 \gg \bar{n}_B^{\mathrm{thresh}} = 0.069$ ).

$\bar{n}_B = 610$ . We see that the QI system can have an error probability that is orders of magnitude lower than that of the coherent-state system. Moreover, according to Ref. [5], no other classical-state system with the same energy constraint can have a lower error probability than the coherent-state system.

To further study the performance gain of our microwave QI system over a classical sensor, we evaluate  $\mathcal{F} \equiv \mathrm{SNR}_{\mathrm{QI}}^{(M)} / \mathrm{SNR}_{\mathrm{coh}}^{(M)}$  for large  $M$ . This figure of merit depends on the cooperativity parameters,  $\Gamma_w$  and  $\Gamma_o$ , whose values are typically large  $\Gamma_j \gg 1$  (cf. the values in Fig. 2, which rely on experimentally achievable parameters) and the brightness of the background,  $\bar{n}_B$ . As shown in Fig. 4, QI's superiority prevails in a substantial region of  $\Gamma_w$ ,  $\Gamma_o$  values corresponding to Fig. 2 regions where our source has the best efficiency in producing quantum entanglement and, more generally, quantum correlations, per microwave photon emitted. Such advantage is found as long as the average number of microwave photons is sufficiently low.

![](images/983ab70b25898012a4f050ffdd107806581f8673911dabee3c9e2165f895f8c8.jpg)  
FIG. 4 (color online). QI-adantage figure of merit,  $\mathcal{F}$ , versus  $\Gamma_w$  and  $\Gamma_o$ . For  $\mathcal{F} > 1$ , the QI system has lower error probability than any classical-state system, i.e., classical transmitter (CT), of the same transmitted energy. See Fig. 2 for the other parameter values.

Conclusion and Discussion.-We have shown that quantum illumination can be performed in its more natural setting for target detection, i.e., the microwave regime, by using a pair of electro-optomechanical converters. Thanks to this converter, the target region can be interrogated at a microwave frequency, while the quantum-illumination joint measurement needed for target detection is made at optical frequency, where the high-performance photodetectors needed to obtain QI's performance advantage are available.

An optimized EOM converter is able to generate strong quantum entanglement and quantum correlations between its microwave and optical outputs. These correlations can successfully be exploited for target detection, yielding lower error probability than that of any classical-state microwave system of the same transmitted energy. The QI advantage is especially evident when detecting the faint returns from low-reflectivity objects embedded in the bright thermal noise typical of room-temperature microwave environments.

Note that we assumed unit quantum efficiency for the optical part of our quantum receiver. This is not far from current experimental conditions: photon collection efficiencies from optical cavities can be very high ( $>74\%$  in Ref. [42]), loss at the beam splitter can be extremely low, and photodetection can be extremely efficient at optical wavelengths. Thus, the main source of loss may come from the optical storage of the idler mode, to be preserved during the signal round-trip time. This is not an issue for short-range applications but, for long-range tasks, the idler loss must remain below 3 dB, otherwise, the QI advantage of the phase-conjugating quantum receiver is lost [6]. While using a good quantum memory (e.g., a rare-earth doped crystal [43]) would solve the problem, the practical solution of storing the idler into an optical-fiber delay line would restrict the maximum range of the quantum radar to about  $11.25\mathrm{km}$  in free space (assuming a fiber loss of  $0.2\mathrm{dB / km}$  and fiber propagation speed equal to  $2c / 3$ , where  $c$  is vacuum light speed).

Finally, extending our results to lower frequencies (below 1 GHz), our scheme could potentially be used for noninvasive NMR spectroscopy in structural biology (structure of proteins and nucleic acids) and in medical applications (magnetic resonance imaging). Future implementations of quantum illumination at the microwave regime could also be achieved by using other quantum sources, for instance based on Josephson parametric amplifiers, which are able to generate entangled microwave modes of high quality [44-47]. These amplifiers might become a very good choice once suitable high-performance microwave photodetectors are made available.

S. B. is grateful for support from the Alexander von Humboldt foundation. D. V. is sponsored by the European Commission (ITN-Marie Curie Project "cQOM", Grant No. 290161, and FET-Open Project "iQUOEMS", Grant No. 323924). S. G. was supported by the U.S. Office of Naval Research Contract No. N00014-14-C-0002. J. H. S. appreciates sponsorship by AFOSR and ONR. S.P. has been sponsored by a Leverhulme Trust research fellowship and

EPSRC via "qDATA" (Grant No. EP/L011298/1) and "HIPERCOM" (Grant No. EP/J00796X/1).

*stefano.pirandola@york.ac.uk  
[1] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, England, 2000).  
[2] M. M. Wilde, Quantum Information Theory, (Cambridge University Press, Cambridge, England, 2013).  
[3] C. Weedbrook, S. Pirandola, R. García-Patron, N.J. Cerf, T.C. Ralph, J.H. Shapiro, and S. Lloyd, Rev. Mod. Phys. 84, 621 (2012).  
[4] S. Lloyd, Science 321, 1463 (2008).  
[5] S.-H. Tan, B. I. Erkmen, V. Giovannetti, S. Guha, S. Lloyd, L. Maccone, S. Pirandola, and J. H. Shapiro, Phys. Rev. Lett. 101, 253601 (2008).  
[6] S. Guha and B. I. Erkmen, Phys. Rev. A 80, 052310 (2009).  
[7] C. Weedbrook, S. Pirandola, J. Thompson, V. Vedral, and M. Gu, arXiv:1312.3332.  
[8] J. H. Shapiro, Phys. Rev. A 80, 022320 (2009).  
[9] Z. Zhang, M. Tengner, T. Zhong, F. N. C. Wong, and J. H. Shapiro, Phys. Rev. Lett. 111, 010501 (2013).  
[10] S. Pirandola, Phys. Rev. Lett. 106, 090504 (2011).  
[11] S. Pirandola, C. Lupo, V. Giovannetti, S. Mancini, and S. L. Braunstein, New J. Phys. 13, 113012 (2011).  
[12] G. Spedalieri, C. Lupo, S. Mancini, S. L. Braunstein, and S. Pirandola, Phys. Rev. A 86, 012315 (2012).  
[13] C. Lupo, S. Pirandola, V. Giovannetti, and S. Mancini, Phys. Rev. A 87, 062310 (2013).  
[14] E. D. Lopaeva, I. Ruo Berchera, I. P. Degiovanni, S. Olivares, G. Brida, and M. Genovese, Phys. Rev. Lett. 110, 153603 (2013).  
[15] Z. Zhang, S. Mouradian, F. N. C. Wong, and J. H. Shapiro, arXiv:1411.5969.  
[16] C. Weedbrook, S. Pirandola, S. Lloyd, and T.C. Ralph, Phys. Rev. Lett. 105, 110501 (2010).  
[17] C. Weedbrook, S. Pirandola, and T. C. Ralph, Phys. Rev. A 86, 022318 (2012).  
[18] C. Weedbrook, C. Ottaviani, and S. Pirandola, Phys. Rev. A 89, 012309 (2014).  
[19] Sh. Barzanjeh, D. Vitali, P. Tombesi, and G. J. Milburn, Phys. Rev. A 84, 042342 (2011).  
[20] Sh. Barzanjeh, M. Abdi, G. J. Milburn, P. Tombesi, and D. Vitali, Phys. Rev. Lett. 109, 130503 (2012).  
[21] R. W. Andrews, R. W. Peterson, T. P. Purdy, K. Cicak, R. W. Simmonds, C. A. Regal, and K. W. Lehnert, Nat. Phys. 10, 321 (2014).  
[22] J. Bochmann, A. Vainsencher, D. D. Awschalom, and A. N. Cleland, Nat. Phys. 9, 712 (2013).  
[23] T. Bagci, A. Simonsen, S. Schmid, L. G. Villanueva, E. Zeuthen, J. Appel, J. M. Taylor, A. Sorensen, A. Schliesser, and E. S. Polzik, Nature (London) 507, 81 (2014).  
[24] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.114.080503, which includes Refs. [25-28]. We provide technical details on the following: (i) Hamiltonian of an electro-optomechanical system, (ii) linearization of the Hamiltonian, (iii) derivation of the quantum Langevin equations with internal losses, (iv) study of the microwave-optical entanglement consid

ering the entanglement metric, the logarithmic negativity and the coherent information, (v) general study of the quantum correlations as quantified by quantum discord, and (vi) analysis of the error probability for  $M$  mode pairs.  
[25] I. Devetak and A. Winter, Proc. R. Soc. A 461, 207 (2005).  
[26] R. García-Patrón, S. Pirandola, S. Lloyd, and J. H. Shapiro, Phys. Rev. Lett. 102, 210501 (2009).  
[27] S. Pirandola, R. García-Patrón, S. L. Braunstein, and S. Lloyd, Phys. Rev. Lett. 102, 050503 (2009).  
[28] K. Modi, A. Brodutch, H. Cable, T. Paterek, and V. Vedral, Rev. Mod. Phys. 84, 1655 (2012).  
[29] T. A. Palomaki, J. D. Teufel, R. W. Simmonds, and K. W. Lehnert, Science 342, 710 (2013).  
[30] S.G. Hofer, W. Wieczorek, M. Aspelmeyer, and K. Hammerer, Phys. Rev. A 84, 052327 (2011).  
[31] T. A. Palomaki, J. W. Harlow, J. D. Teufel, R. W. Simmonds, and K. W. Lehnert, Nature (London) 495, 210 (2013).  
[32] The system is stable if the Routh-Hurwitz criterion is satisfied. For  $\Gamma_{i} \gg 0$ , this criterion reduces to the following necessary and sufficient condition [33]:

$$
\kappa_ {w} \Gamma_ {w} - \kappa_ {o} \Gamma_ {o} > \tilde {K} \max \left\{\kappa_ {w} - \kappa_ {o}, \frac {\kappa_ {o} ^ {2} - \kappa_ {w} ^ {2}}{2 \gamma_ {M} + \kappa_ {w} + \kappa_ {o}} \right\},
$$

where  $\tilde{K} = \Gamma_w(1 + \kappa_o / \kappa_w)^{-1} + \Gamma_o(1 + \kappa_w / \kappa_o)^{-1}$  
[33] Y.-D. Wang and A. A. Clerk, Phys. Rev. Lett. 110, 253601 (2013).  
[34] J. Eisert, Ph.D. thesis, University of Potsdam, 2001; G. Vidal and R. F. Werner, Phys. Rev. A 65, 032314 (2002); M. B. Plenio, Phys. Rev. Lett. 95, 090503 (2005).  
[35] B. Schumacher and M. A. Nielsen, Phys. Rev. A 54, 2629 (1996).  
[36] S. Lloyd, Phys. Rev. A 55, 1613 (1997).  
[37] S. Pirandola, G. Spedalieri, S. L. Braunstein, N. J. Cerf, and S. Lloyd, Phys. Rev. Lett. 113, 140405 (2014).  
[38] The common bandwidth of the entangled microwave and optical fields is  $W_{m} = \gamma_{M}(\Gamma_{w} - \Gamma_{o} + 1)$ , in terms of the resonator's damping rate and the cooperativity parameters.  
[39] K. M. R. Audenaert, J. Calsamiglia, R. Muñoz-Tapia, E. Bagan, L. Masanes, A. Acin, and F. Verstraete, Phys. Rev. Lett. 98, 160501 (2007).  
[40] K.M.R. Audenaert, M. Nussbaum, A. Szkola, and F. Verstraete, Commun. Math. Phys. 279, 251 (2008).  
[41] S. Pirandola and S. Lloyd, Phys. Rev. A 78, 012331 (2008).  
[42] A. Reiserer, S. Ritter, and G. Rempe, Science 342, 1349 (2013).  
[43] M. Zhong, M. P. Hedges, R. L. Ahlefeldt, J. G. Bartholomew, S. E. Beavan, S. M. Wittig, J. J. Longdell, and M. J. Sellars, Nature (London) 517, 177 (2015).  
[44] M. A. Castellanos-Beltran and K. W. Lehnert, Appl. Phys. Lett. 91, 083509 (2007).  
[45] N. Bergeal, F. Schackert, M. Metcalfe, R. Vijay, V.E. Manucharyan, L. Frunzio, D.E. Prober, R.J. Schoelkopf, S.M. Girvin, and M.H. Devoret, Nature (London) 465, 64 (2010).  
[46] N. Roch, E. Flurin, F. Nguyen, P. Morfin, P. CampagneIbarcq, M. H. Devoret, and B. Huard, Phys. Rev. Lett. 108, 147701 (2012).  
[47] C. Eichler, Y. Salathe, J. Mlynek, S. Schmidt, and A. Wallraff, Phys. Rev. Lett. 113, 110502 (2014).