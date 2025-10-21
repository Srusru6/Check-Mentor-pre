# Beyond Spectral Homodyne Detection: Complete Quantum Measurement of Spectral Modes of Light

F. A. S. Barbosa, $^{1}$  A. S. Coelho, $^{1}$  K. N. Cassemiro, $^{2}$  P. Nussenzweig, $^{1}$  C. Fabre, $^{3}$  M. Martinelli, $^{1}$  and A. S. Villar $^{2,*}$ \
 $^{1}$ Instituto de Física, Universidade de São Paulo, P.O. Box 66318, 05315-970 São Paulo, São Paulo, Brazil\
 $^{2}$ Departamento de Física, Universidade Federal de Pernambuco, 50670-901 Recife, Pernambuco, Brazil\
 $^{3}$ Laboratoire Kastler Brossel, Case 74, Université Pierre et Marie Curie, 4 Place Jussieu, 75252 Paris Cedex 05, France\
(Received 26 August 2013; published 14 November 2013)

Spectral homodyne detection, a widely used technique for measuring quantum properties of light beams, cannot retrieve all the information needed to reconstruct the quantum state of spectral field modes. We show that full quantum state reconstruction can be achieved with the alternative measurement technique of resonator detection. We experimentally demonstrate this difference by engineering a quantum state with features that go undetected by homodyne detection but are clearly revealed by resonator detection.

DOI: 10.1103/PhysRevLett.111.200402

PACS numbers: 03.65.Wj, 03.65.Ta, 42.50.Ar, 42.50.Lc

Quantum states of light offer novel capabilities for information exchange and processing that are actively investigated. These range from increased security to quantum data compression and quantum teleportation. In order to fully harness such capabilities, it is necessary to coherently exploit the larger configuration space of multimode fields [1-7]. Quantum states can then be entangled over many modes and present useful multimode quantum correlations. Spectral modes, with well-defined frequencies, are particularly interesting in this respect as they can be easily separated by spectral filtering.

To determine the spectral content of quantum states of light, homodyne techniques stand as the most important class of quantum measurements available in the continuous variable regime [8-12]. By interfering the field of interest with a suitable classical field, the local oscillator (LO), they provide direct access to the phase space distribution of field quadratures.

The detection of spectral modes is usually performed with spectral homodyne detection. In this case, a spectrally narrow laser field constitutes the LO, and the detected photocurrent undergoes Fourier analysis, its power spectrum providing all the accessible information about the quantum state. The technique has been employed in observations of quantum noise squeezing, phase space reconstruction of a squeezed quantum state, and EPR-type entanglement in spectral modes [13-16]. More recently, it has allowed the teleportation of quantum correlations as well as partial realization of other quantum information protocols [17-19]. It has been noted, however, that homodyne detection does not yield a complete measurement of the quantum state of light spanning over the two sideband modes which contribute to quantum noise [20-22].

An alternative measurement technique, here called "resonator detection," consists of a "self-homodyne" technique which employs an optical resonator to manipulate the spectral modes prior to intensity measurement. This technique allows the measurement of quantum noise

in experimental situations in which an external LO is not readily available [23,24]. That feature is thought to be the only advantage of resonator detection, which is usually considered to be equivalent to the spectral homodyne technique as a quantum measurement [25-28].

In this Letter, we show that resonator detection indeed provides a complete joint measurement of the two-sideband mode quadrature quantum fluctuations and correlations, allowing us to completely reconstruct the two-mode quantum state. It is therefore more powerful as a quantum measurement than the spectral homodyne detection. We provide an experimental illustration of this property by exhibiting two Gaussian quantum states which are perfectly distinguishable with resonator detection, whereas they appear indistinguishable with homodyne detection.

Photodetection by light absorption is described by the measurement operator  $\hat{I}(t) = \hat{E}^{-}(t)\hat{E}^{+}(t)$ , where the positive and negative frequency parts of the electric field operator form a mode continuum [29]:

$$
\hat {E} ^ {+} (t) = \int d \omega e ^ {- i \omega t} \hat {a} _ {\omega}, \quad \hat {E} ^ {-} (t) = [ \hat {E} ^ {+} (t) ] ^ {\dagger}. \tag {1}
$$

Field amplitude  $\hat{p}_{\omega}$  and phase  $\hat{q}_{\omega}$  quadrature observables, fulfilling the canonical commutation relation  $[\hat{p}_{\omega},\hat{q}_{\omega^{\prime}}] = 2i\delta (\omega -\omega^{\prime})$  , satisfy  $\hat{a}_{\omega} = (\hat{p}_{\omega} + i\hat{q}_{\omega}) / 2.$

Homodyne detection employs as the input field a LO mode, i.e., a coherent state  $|\alpha \rangle_{\omega_0}$  (at frequency  $\omega_0$ ), to amplify the quantum noise stemming from modes in its frequency vicinity and possessing the quantum state of interest,  $\hat{\rho}$ . In the balanced detection configuration, the associated quantum measurement is represented by the operator

$$
\delta \hat {I} (t) = \alpha^ {*} \hat {a} (t) + \alpha \hat {a} ^ {\dagger} (t), \tag {2}
$$

where  $\hat{a}(t) = \int d\omega e^{-i(\omega - \omega_0)t} \hat{a}_\omega$  and the frequency integral is limited around  $\omega_0$  by detection bandwidth. Perfect spatial overlap between LO and quantum modes is assumed.

Spectral resolution of field modes is achieved by Fourier analysis of  $\delta \hat{I}(t)$ . Experimentally, it is performed by mixing the photocurrent with a sinusoidal electronic reference at frequency  $\Omega$  and integrating the result for a time compatible with the desired spectral resolution. The following operator condenses the ideal quantum measurement (unit efficiency) of the spectral photocurrent fluctuations:

$$
\delta \hat {I} _ {\Omega} = \alpha^ {*} \hat {a} _ {\omega_ {0} + \Omega} + \alpha \hat {a} _ {\omega_ {0} - \Omega} ^ {\dagger} = \frac {| \alpha |}{\sqrt {2}} (\hat {I} _ {\cos} + i \hat {I} _ {\sin}), \tag {3}
$$

$\hat{I}_{\mathrm{cos}}$  and  $\hat{I}_{\mathrm{sin}}$  being the two Hermitian operators associated with the cosine and sine photocurrent observables, respectively [8,20]. They are given by

$$
\begin{array}{l} \hat {I} _ {\cos} (\varphi) = \cos \varphi \hat {p} _ {+} + \sin \varphi \hat {q} _ {+} \equiv \hat {X} _ {+} (\varphi), \\ \hat {I} _ {\sin} (\varphi) = - \sin \varphi \hat {p} _ {-} + \cos \varphi \hat {q} _ {-} \equiv \hat {X} _ {-} (\varphi + \pi / 2), \tag {4} \\ \end{array}
$$

where the LO phase  $\varphi$  (in  $\alpha = |\alpha|e^{i\varphi}$ ) determines the direction of quadrature observation in phase space. Modes labeled by subscripts  $+$  and  $-$  are the symmetric and antisymmetric coherent combinations, respectively, of spectral sideband modes  $\omega_0 \pm \Omega$ , in the form

$$
\hat {p} _ {\pm} = \frac {1}{\sqrt {2}} \left(\hat {p} _ {\omega_ {0} + \Omega} \pm \hat {p} _ {\omega_ {0} - \Omega}\right), \tag {5}
$$

$$
\hat {q} _ {\pm} = \frac {1}{\sqrt {2}} (\hat {q} _ {\omega_ {0} + \Omega} \pm \hat {q} _ {\omega_ {0} - \Omega}).
$$

They represent the quadrature operators of modes naturally associated with spectral homodyne detection.

The measurement operators of Eq. (4) are each single-mode quadrature observables [30]. The cosine photocurrent component refers to the symmetric mode and the sine component to the antisymmetric mode. The LO phase controls the direction of observation in phase space for both individual modes, which are thus connected to one another: It is not possible to rotate phase spaces independently. Hence only two-mode correlations of the type  $\langle \hat{X}_{+}(\varphi)\hat{X}_{-}(\varphi +\pi /2)\rangle$  can be accessed, while moments of the form  $\langle \hat{X}_{+}(\varphi)\hat{X}_{-}(\varphi)\rangle$  are missing.

Consider  $\mathcal{E}_{\omega_0\pm \Omega} = \frac{1}{2} (\Delta^2\hat{p}_{\omega_0\pm \Omega} + \Delta^2\hat{q}_{\omega_0\pm \Omega}) - 1$  as the energy present in the quantum noise of each spectral mode above zero point fluctuation. The missing two-mode moment then reads as  $\mathcal{E}_{\omega_0 + \Omega} - \mathcal{E}_{\omega_0 - \Omega}$ . In the spectral modal basis, it has a clear meaning: energy imbalance. With only one controllable parameter, homodyne detection is blind to two-mode energy asymmetry, since it treats spectral modes in a perfectly indistinguishable manner according to Eq. (4). Although some classes of the quantum states commonly produced in laboratories, such as in spontaneous parametric down-conversion, should present sideband modes with no energy imbalance, we must point out that many other quantum states, such as those relying on resonant phenomena (e.g., atomic emission), should possess imbalanced fluctuations in sideband modes.

In most experiments, the phases of the optical field and the electronic oscillator are not locked to each other. Thus, only the photocurrent spectral noise power  $S_{\mathrm{HD}} = (\Delta^{2}\hat{I}_{\mathrm{cos}} + \Delta^{2}\hat{I}_{\mathrm{sin}}) / 2$  carries quantum state information [31]. Its expression in terms of symmetric and antisymmetric modes reads as

$$
\begin{array}{l} S _ {\mathrm {H D}} (\varphi) = \frac {1}{2} \cos^ {2} \varphi \left(\Delta^ {2} \hat {p} _ {+} + \Delta^ {2} \hat {q} _ {-}\right) + \frac {1}{2} \sin^ {2} \varphi \left(\Delta^ {2} \hat {p} _ {-} + \Delta^ {2} \hat {q} _ {+}\right) \\ + \frac {1}{2} \sin 2 \varphi \left(C _ {\hat {p} _ {+} \hat {q} _ {+}} - C _ {\hat {p} _ {-} \hat {q} _ {-}}\right), \tag {6} \\ \end{array}
$$

where  $C_{\hat{\sigma}\hat{\sigma}^{\prime}}$  denotes the symmetrized correlation function of quadratures  $\hat{o}$  and  $\hat{o}^\prime$ . By scanning the LO phase  $\varphi$ , one can therefore measure only the three noise-dependent coefficients figuring in Eq. (6).

Let us now turn to resonator detection. Equation (3) describes the quantum observables associated with the spectral analysis of intensity measurement, where  $\alpha$  is the mean field impinging on the photodetector. Reflection off an optical resonator placed just prior to intensity detection changes modal annihilation operators according to [28]

$$
\hat {a} _ {\omega} \rightarrow r (\Delta_ {\omega}) \hat {a} _ {\omega} + t (\Delta_ {\omega}) \hat {b} _ {\omega}, \tag {7}
$$

where the resonator reflection  $r(\Delta_{\omega})$  and transmission  $t(\Delta_{\omega}) = \sqrt{1 - r^{2}(\Delta_{\omega})}$  coefficients, which combine the input quantum field of interest  $\hat{a}_{\omega}$  with a field mode  $\hat{b}_{\omega}$  in a vacuum state, are functions of cavity detuning  $\Delta_{\omega} = (\omega - \omega_c) / \gamma$  relative to the cavity bandwidth  $\gamma$ . In addition, the resonator performs the transformation  $\alpha \rightarrow \alpha_r = r(\Delta)\alpha$  on the mean value of the input field of frequency  $\omega_0$ . The detuning  $\Delta = (\omega_0 - \omega_c) / \gamma$  is a parameter which is experimentally controllable by scanning the cavity length. The intensity of the reflected field is then measured and Fourier analyzed, yielding  $\Delta$ -dependent photocurrent spectral components  $\hat{J}_{\mathrm{cos}}$  and  $\hat{J}_{\mathrm{sin}}$  given, respectively, by

$$
\hat {J} _ {\cos} = x _ {\Omega} \hat {p} _ {\Omega} + y _ {\Omega} \hat {q} _ {\Omega} + x _ {- \Omega} \hat {p} _ {- \Omega} + y _ {- \Omega} \hat {q} _ {- \Omega} + \hat {J} _ {u}, \tag {8}
$$

$$
\hat {J} _ {\sin} = - y _ {\Omega} \hat {p} _ {\Omega} + x _ {\Omega} \hat {q} _ {\Omega} + y _ {- \Omega} \hat {p} _ {- \Omega} - x _ {- \Omega} \hat {q} _ {- \Omega} + \hat {J} _ {v},
$$

where mode notation has been compacted,  $\omega_0\pm \Omega \to \pm \Omega$  and coefficients  $x_{\pm \Omega}$  and  $y_{\pm \Omega}$  are real functions of  $\Delta$ :

$$
x _ {\pm \Omega} + i y _ {\pm \Omega} = R _ {\pm \Omega} = \frac {1}{\sqrt {2}} \frac {r (\Delta)}{| r (\Delta) |} r ^ {*} (\Delta \pm \Omega / \gamma). \tag {9}
$$

Operators  $\hat{J}_u$  and  $\hat{J}_{\nu}$  stand for vacuum contributions related to cavity losses. We see in expression (8) that, unlike homodyne detection, the resonator technique inherently gives more information about the two spectral modes, from which it is possible to derive the whole two-mode covariance matrix [31,32] and, therefore, perform the reconstruction of any two-mode Gaussian state.

The corresponding spectral noise power is

$$
\begin{array}{l} S _ {\mathrm {R D}} (\Delta) = g _ {+} (\Delta) (\mathcal {E} _ {\Omega} + \mathcal {E} _ {- \Omega} + 2) + g _ {-} (\Delta) (\mathcal {E} _ {\Omega} - \mathcal {E} _ {- \Omega}) \\ + g _ {r} (\Delta) \left(\Delta^ {2} \hat {p} _ {+} + \Delta^ {2} \hat {q} _ {-} - \Delta^ {2} \hat {p} _ {-} - \Delta^ {2} \hat {q} _ {+}\right) \\ + g _ {i} (\Delta) \left(C _ {\hat {p} _ {+} \hat {q} _ {+}} - C _ {\hat {p} _ {-} \hat {q} _ {-}}\right) + \Delta^ {2} \hat {J} _ {u} + \Delta^ {2} \hat {J} _ {v}, \tag {10} \\ \end{array}
$$

where  $g_{\pm} = (|R_{\Omega}|^{2}\pm |R_{-\Omega}|^{2}) / 2$  stands for the sum or subtraction of resonator response and  $g_{r}$  and  $g_{i}$  are real functions of  $\Delta$  defined by  $g_{r} + ig_{i} = R_{\Omega}R_{-\Omega} / 2$ . Vacuum noise contributions are  $\Delta^2\hat{J}_u + \Delta^2\hat{J}_v = 1 - |R_\Omega|^2 -|R_{-\Omega}|^2$

The different  $g$  being known functions of  $\Delta$ , it is possible to retrieve their four coefficients from a least-squares fit to the experimental data. Resonator detection offers in particular the ability to pinpoint quantum states showing strong energy imbalance between spectral sideband modes. The reason for that is the introduction not only of dispersion by the optical resonator, but also of frequency-dependent modal attenuation. Apart from photodetector efficiency, modal coupling with the resonator is the only factor to limit the quantum efficiency of measurement, just in the same way that the overlap with the LO mode limits the efficiency of homodyne detection.

In our experiment, we generate a quantum state possessing an energy imbalance that is likely to benchmark the differences between homodyne and resonator detection. It is produced in two steps, as depicted in Fig. 1. First, two spectral modes are displaced with the aid of an electro-optic modulator (EOM) to produce coherent states with complex

![](images/f4e5d1a69a228f5c243b5869d2b9da40d180f863f2f6f21716a321007f0af72c.jpg)  
FIG. 1 (color online). Experimental setup. State preparation (solid green beam): An EOM displaces spectral modes, and an asymmetry resonator attenuates one of them. State detection: Either homodyne (dotted blue beam) or resonator detection (dashed red beam) is employed. A flip mirror and blocking of LO are used to choose between the two types of quantum measurement.

conjugate amplitudes,  $|\psi_{1}\rangle = \hat{D}_{\omega_{0} - \Omega}(\beta^{*})\hat{D}_{\omega_{0} + \Omega}(\beta)|0\rangle = |\beta^{*}\rangle_{\omega_{0} - \Omega}|\beta \rangle_{\omega_{0} + \Omega}$ , where  $\beta = |\beta |e^{i\theta}$ . This state vector shows balanced spectral energy distribution. Second, an auxiliary optical resonator, called the asymmetry resonator, produces an energy imbalance between spectral modes by attenuating one of them in reflection. In our case, the asymmetry resonator is locked to resonance with mode  $\omega_{0} - \Omega$ , and the quantum state becomes  $|\psi_{2}\rangle = |\beta^{\prime *} \rangle_{\omega_{0} - \Omega}|\beta \rangle_{\omega_{0} + \Omega}$ , where  $\beta^{\prime} = \sqrt{R_0^{\prime}}\beta$ .

The quantum state preparation and measurement are illustrated in Fig. 1. The input laser beam at  $532~\mathrm{nm}$  is mode cleaned by a filter cavity. The same signal used for EOM modulation is employed as an electronic reference in the measurement of quantum noise, with frequency  $\Omega = 17\mathrm{MHz}$  [16,33]. Spectral analysis of the photocurrent is performed with  $600\mathrm{kHz}$  bandwidth. Photodetector efficiency is  $95\%$ . Each intermediate step  $|\psi_1\rangle$  and  $|\psi_2\rangle$  for the quantum state preparation of  $\hat{\rho}$  is experimentally verified. Although we employ resonator detection at this stage, homodyne detection would find the same measurement results, since only first-order moments appear and all second-order moments are either shot noise or null.

Data are presented in Fig. 2. In the first step, quadrature state averages on  $|\psi_1\rangle$  relative to the standard quantum level are shown in Fig. 2(a) as functions of  $\theta$ . Quadrature mean values are obtained by theoretical fits of quantum state averages of Eq. (8) to the data. Amplitude and phase quadratures alternate with  $\theta$  in pairs as projections of  $\beta = \langle \hat{p}_{\omega_0 + \Omega}\rangle_1 + i\langle \hat{q}_{\omega_0 + \Omega}\rangle_1$  and  $\beta^{*} = \langle \hat{p}_{\omega_{0} - \Omega}\rangle_{1} - i\langle \hat{q}_{\omega_{0} - \Omega}\rangle_{1}$ . Complex conjugate displacements are attested to by the data. In the second step, the asymmetry resonator produces state  $|\psi_2\rangle$  with an energy imbalance. Reflection at resonance is  $R_0^{\prime} = 0.12(2)$ , and bandwidth is 4.1 (2) MHz. Displacement amplitudes for both spectral modes can be observed in Fig. 2. While one spectral mode

![](images/79f26874456f1753c4f2d626664d8f1d206a623ed42182a29fe47f87749259e6.jpg)

![](images/81145635a22c95a2709dd6b3fa38ffa34cde939a650a2739a932519dc709168b.jpg)  
FIG. 2 (color online). Measured expectation values of spectral quadrature observables as functions of displacement angle  $\theta$ . Left: Quantum state  $|\psi_{1}\rangle$  with a balanced energy distribution. Right: Quantum state  $|\psi_{2}\rangle$  with a spectral energy imbalance.

![](images/80cc42b135054c645cd40c475a93c9b1e3e9390b67f9cd2fb92aed353bcabf1c.jpg)

![](images/8c2933527ba812f25cc81f41dc50232b59ba3f4329bfa2dbffe0daad5aec7193.jpg)

presents  $\langle \hat{p}_{\omega_0 + \Omega}\rangle_2\approx 19$  at maximum, the other shows  $\langle \hat{p}_{\omega_0 - \Omega}\rangle_2\approx 10$  , attesting to an energy imbalance ratio of  $\mathcal{E}_{\omega_0 - \Omega} / \mathcal{E}_{\omega_0 + \Omega}\approx 0.28.$

We seek to create a state with an imbalance in the second-order moments. This is achieved by randomizing the amplitudes and phases of the displacements, by driving the EOM with Gaussian noise as the input. This procedure scrambles the displacement mean values and produces field fluctuations with the desired properties. The desired benchmark quantum state  $\hat{\rho} = \int d^{2}\beta e^{-(|\beta|^{2}/|\beta_{0}|^{2})}|\psi_{2}\rangle\langle\psi_{2}|$  bearing a modal energy imbalance, where  $|\beta_{0}|$  is the typical modulation energy, is thus generated. For each single mode,  $\hat{\rho}$  is a thermal state. We then measure the benchmark quantum state  $\hat{\rho}$  with homodyne and resonator detection schemes (Fig. 1). For comparison purposes, we also prepare a reference thermal state  $\hat{\rho}_{r}$  showing a balanced energy distribution, by amplitude randomization of  $|\psi_{1}\rangle$  in the form  $\hat{\rho}_{r} = \int d^{2}\beta e^{-(|\beta|^{2}/|\beta_{0}|^{2})}|\psi_{1}\rangle\langle\psi_{1}|$ .

Experimental results for the symmetric state  $\hat{\rho}_r$  using both techniques are presented in Fig. 3. Data with homodyne detection appear at the top right. Fringe contrast exceeds  $91\%$ . The solid line (labeled HD) depicts the theoretical fit of Eq. (6) to the data. The insets depict the Wigner functions of individual spectral modes associated with measured operator moments, yielding a visual representation of the measured single-mode covariance matrices.

![](images/3c71d4988053cf102c28845680ee6a3970169aad967ba8aace7690564f9cab34.jpg)

![](images/ede284ef107a48eacf1643caadc0b41b433e6a9004e3b398357021407c45fef1.jpg)  
FIG. 3 (color online). Measurements of spectral quantum noise produced by the balanced quantum state  $\hat{\rho}_r$ . Top: Homodyne detection, as a function of  $\varphi$ . Bottom: Resonator detection, as a function of  $\Delta$ . Solid lines ('HD' on top and 'RD' on bottom) are theoretical fits to the data. Dashed line on the bottom ('HD-like') represents the theoretical noise curve of Eq. (10) as it would appear in resonator detection using only moments obtainable with homodyne detection.

At the bottom left, we observe resonator detection data obtained from a symmetric quantum state produced in a similar manner. The only difference is the increase in mean energy to facilitate the comparison between techniques in our particular implementation. Resonator bandwidth is  $\gamma = 6.0(3)\mathrm{MHz}$ , mode coupling efficiency is  $93.5(1.0)\%$ , and  $R_0 = 0.04(2)$ . The solid line (labeled RD) represents a theoretical fit of Eq. (10) to the data (taking into account that mode coupling efficiency slightly modifies the equation). The dashed line (HD) represents noise as it would be observed with resonator detection in case only moments available to homodyne detection had been retrieved. Both curves provide equally good fits.

We see in this first series of measurements that both techniques are able to recover correctly the quantum state prepared, as established by the Wigner functions in the insets. Resonator and homodyne detection find compatible results for  $\hat{\rho}_r$ , meaning that no spectral energy imbalance is necessary to describe the quantum state.

Next, measurements of the benchmark quantum state  $\hat{\rho}$  are shown in Fig. 4 for both techniques. Homodyne detection (top right) retrieves the same qualitative shape of quantum noise as in Fig. 3, as emphasized by theoretical curve fittings of Eq. (6) to the data. Essentially, single-mode subspaces of  $\hat{\rho}$  appear to homodyne detection as balanced attenuated versions of  $\hat{\rho}_r$ . The insets at the top left show that two different thermal states are mistakenly identified as carrying the same mean energy, an assumption tacitly made whenever quantum noise is observed with spectral homodyne detection. The technique is insensitive to an energy imbalance between spectral modes.

![](images/4a03a4aed926372b5259b44c5e1df7cc11958361afa8c40f2e98cda535467b37.jpg)

![](images/feff642a17de1e53b823a303d55949cc0e5811b980b88ecb36485804db93e1c5.jpg)  
FIG. 4 (color online). Measurements of spectral quantum noise produced by the imbalanced quantum state  $\hat{\rho}$ . Curves and labels follow Fig. 3.

Data acquired with resonator detection appear at the bottom left. The solid line represents a theoretical fitting of Eq. (10) to the data. The dashed line shows quantum noise as it would appear if only the moments measured with homodyne detection were available, for comparison. Equivalently, this also shows how a quantum state showing a balanced modal energy would produce a symmetric noise curve around resonance. The solid and dashed curves show a strong disagreement, establishing the need to invoke a strong modal energy imbalance to explain the data on  $\hat{\rho}$ . The experimental signature is clear at  $\Delta \approx \pm 2.6$ , when the optical resonator replaces one of the spectral modes of interest by vacuum. At  $\Delta \approx -2.6$ , the resonator reflects the populated spectral mode and transmits the attenuated mode, causing no perceptible change to the quantum noise. The situation is reversed, however, at  $\Delta \approx 2.6$ , and a large dip can be seen in the quantum noise. The Wigner functions show that both  $\hat{\rho}_r$  and  $\hat{\rho}$  are correctly identified with resonator detection.

In conclusion, we have shown that resonator detection allows one to collect more information about the two-mode spectral quantum state than homodyne detection. In particular, resonator detection is able to detect energy imbalances between sideband modes' fluctuations. Any quantum state spanning over the two-sideband modes can be exactly reconstructed. As a complete measurement technique, it also allows an experimental determination of state purity, in contrast to the intrinsically imperfect spectral homodyne detection. In order to efficiently implement quantum information protocols with the continuous variables of multimode spectral fields, one needs to use superior measurement techniques, such as resonator detection.

We thank Y. Golubev and T. Golubeva for stimulating discussions in the initial stage of this research. This work was supported by Grants No. 2010/52282-1, No. 2010/08448-2, and No. 2009/52157-5, São Paulo Research Foundation (FAPESP), CNPq, CAPES (through program PROCAD), and CNRS. This research was performed within the framework of the Brazilian National Institute for Science and Technology in Quantum Information (INCT-IQ).

* villar@df.ufpe.br

[1] S. Spälter, N. Korolkova, F. König, A. Sizmann, and G. Leuchs, Phys. Rev. Lett. 81, 786 (1998).  
[2] N.C. Menicucci, S.T. Flammia, and O. Pfister, Phys. Rev. Lett. 101, 130501 (2008).  
[3] V. Boyer, A.M. Marino, R.C. Pooser, and P.D. Lett, Science 321, 544 (2008).  
[4] J. Janousek, K. Wagner, J-F. Morizur, N. Treps, P. K. Lam, C.C. Harb, and H-A. Bacher, Nat. Photonics 3, 399 (2009).

[5] O. Pinel, P. Jian, R. Medeiros de Araujo, J. Feng, B. Chalopin, C. Fabre, and N. Treps, Phys. Rev. Lett. 108, 083601 (2012).  
[6] N. V. Corzo, A. M. Marino, K. M. Jones, and P. D. Lett, Phys. Rev. Lett. 109, 043602 (2012).  
[7] C. Polycarpou, K.N. Cassemiro, G. Venturi, A. Zavatta, and M. Bellini, Phys. Rev. Lett. 109, 053602 (2012).  
[8] H. P. Yuen and J. H. Shapiro, IEEE Trans. Inf. Theory 26, 78 (1980).  
[9] H.P. Yuen and V.W.S. Chan, Opt. Lett. 8, 177 (1983).  
[10] J.H. Shapiro, IEEE J. Quantum Electron. 21, 237 (1985).  
[11] B. Yurke, Phys. Rev. A 32, 300 (1985); 32, 311 (1985).  
[12] A. I. Lvovsky and M. G. Raymer, Rev. Mod. Phys. 81, 299 (2009).  
[13] R.E. Slusher, L.W. Hollberg, B. Yurke, J.C. Mertz, and J.F. Valley, Phys. Rev. Lett. 55, 2409 (1985).  
[14] Z. Y. Ou, S. F. Pereira, H. J. Kimble, and K. C. Peng, Phys. Rev. Lett. 68, 3663 (1992).  
[15] D. T. Smithey, M. Beck, M. G. Raymer, and A. Faridani, Phys. Rev. Lett. 70, 1244 (1993).  
[16] G. Breitenbach, S. Schiller, and J. Mlynek, Nature (London) 387, 471 (1997).  
[17] H. Yonezawa, T. Aoki, and A. Furusawa, Nature (London) 431, 430 (2004).  
[18] X. Jia, X. Su, Q. Pan, J. Gao, C. Xie, and K. Peng, Phys. Rev. Lett. 93, 250503 (2004).  
[19] R. Ukai, N. Iwata, Y. Shimokawa, S.C. Armstrong, A. Politi, J.-i. Yoshikawa, Peter van Loock, and A. Furusawa, Phys. Rev. Lett. 106, 240504 (2011).  
[20] C.M. Caves, Phys. Rev. D 26, 1817 (1982).  
[21] B.L. Schumaker, S.H. Perlmutter, R.M. Shelby, and M.D. Levenson, Phys. Rev. Lett. 58, 357 (1987).  
[22] T. C. Ralph, E. H. Huntington, and T. Symul, Phys. Rev. A 77, 063817 (2008).  
[23] A. S. Villar, L. S. Cruz, K. N. Cassemiro, M. Martinelli, and P. Nussenzveig, Phys. Rev. Lett. 95, 243603 (2005).  
[24] A. S. Coelho, F. A. S. Barbosa, K. N. Cassemiro, A. S. Villar, M. Martinelli, and P. Nussenzveig, Science 326, 823 (2009).  
[25] G. C. Bjorklund, M. D. Levenson, W. Lenth, and C. Ortiz, Appl. Phys. B 32, 145 (1983).  
[26] M. D. Levenson, R. M. Shelby, and S. H. Perlmutter, Opt. Lett. 10, 514 (1985).  
[27] P. Galatola, L. A. Lugiato, M. G. Porreca, P. Tombesi, and G. Leuchs, Opt. Commun. 85, 95 (1991).  
[28] A.S. Villar, Am. J. Phys. 76, 922 (2008).  
[29] L. Mandel and E. Wolf, Optical Coherence and Quantum Optics (Cambridge University Press, Cambridge, England, 1995).  
[30] M. J. Collett, R. Loudon, and C. W. Gardiner, J. Mod. Opt. 34, 881 (1987).  
[31] F. A. S. Barbosa, A. S. Coelho, K. N. Cassemiro, P. Nussenzveig, C. Fabre, A. S. Villar, and M. Martinelli, Phys. Rev. A 88, 052113 (2013).  
[32] E.H. Huntington and T.C. Ralph, J. Opt. B 4, 123 (2002).  
[33] M. Vasilyev, S.K. Choi, P. Kumar, and G.M. D'Ariano, Opt. Lett. 23, 1393 (1998).