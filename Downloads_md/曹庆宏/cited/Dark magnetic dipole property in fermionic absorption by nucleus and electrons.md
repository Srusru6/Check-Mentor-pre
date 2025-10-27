# Dark magnetic dipole property in fermionic absorption by nucleus and electrons

Tong Li, $^{a}$  Jiajun Liao $^{b}$  and Rui-Jia Zhang $^{a}$

$^{a}$  School of Physics, Nankai University, 94 Weijin Road, Tianjin 300071, China  
$^{b}$ School of Physics, Sun Yat-Sen University, 135 Xingang Xi Road, Guangzhou 510275, China

E-mail: litong@nankai.edu.cn, liaojiajun@mail.sysu.edu.cn, zhangruijia@mail.nankai.edu.cn

ABSTRACT: The fermionic dark matter (DM) absorption by nucleus or electron targets provides a distinctive signal to search for sub-GeV DM. We consider a Dirac fermion DM charged under a dark gauge group and with the dark magnetic dipole operator. The DM field mixes with right-handed neutrino and interacts with the ordinary electromagnetic charge current via the kinetic mixing term of gauge fields. As a result, the incoming DM is absorbed and converted into neutrino in final state through the dipole-charge interaction. For the DM absorption by nucleus, the recoil energy spectrum exhibit a peak at  $m_{\chi}^{2} / 2m_{N}$  for each isotope in the target. XENON1T can probe the DM mass above  $27\mathrm{MeV}$  and the projected constraint on the inelastic DM-nucleon cross section becomes  $10^{-49}\mathrm{cm}^2$ . CRESSTIII with lower energy threshold would be sensitive to the DM mass above  $2\mathrm{MeV}$ . We also check that the contribution from the nuclear magnetic dipole is negligible for  $^{131}\mathrm{Xe}$  target. The absorption of DM by bound electron target induces ionization signal and is sensitive to sub-MeV DM mass. The involvement of the ionization form factor spreads out the localized recoil energy. We show the future prospect for the constraint on the magnetic dipole coupling from the electron ionization of  $^{131}\mathrm{Xe}$ .

KEYWORDS: Particle Nature of Dark Matter, Models for Dark Matter

ARXIV EPRINT: 2201.11905

# Contents

1 Introduction 1  
2 The dark photon model with magnetic dipole moment 2  
3 Dark matter absorption by nuclear targets 4  
4 Dark matter absorption by electron targets 8  
5 Conclusions 12

A Nuclear magnetic dipole form factor  $F_{D}(q)$  13  
B The calculation of the radial wave-functions in the electron ionization form factor  $|f_{\mathrm{ion}}^{nl}(k',q)|^2$  15

B.1 The radial wave-function  $R_{k^{\prime}l^{\prime}}(r)$  15  
B.2 The radial wave-function  $R_{nl}(r)$  16

# 1 Introduction

The existence of dark matter (DM) has been supported by a number of observation evidences in astronomy. However, the DM particle has not been observed in the terrestrial facilities and its microscopic nature is still unknown. The null evidence of the ordinary DM-nucleus elastic scattering in direct detection experiments encourages us to pay attention to other theoretical hypotheses and search methods. The inelastic DM is of particular interest among the alternative strategies [1]. The idea was originally introduced to reconcile the tension between the DAMA annual modulation signature [2, 3] and null result from other direct detection experiments. The mass difference  $\delta \sim 100\mathrm{keV}$  between the incoming DM and the final state changes the kinematics and thus plays as an important unknown parameter to explain the DAMA signal spectrum. It was pointed out that the inelastic DM transition can be dynamically induced by a dark magnetic dipole under the idea that the DM particle could have an off-diagonal magnetic dipole [4-7]. Moreover, the sizable magnetic dipole of iodine in DAMA's NaI target should be taken into account to accommodate the positive DAMA signal through the dipole-dipole inelastic scattering [8, 9].

Apparently, a particular case of inelastic DM is the transition from DM to nearly massless neutrino in which the mass difference is not an additional free parameter any more. Refs. [10-12] recently proposed the idea of fermionic DM absorption by nucleus or electron targets which eventually emit a neutrino in final states, that is

$$
\chi + N (e) \rightarrow \nu + N (e), \tag {1.1}
$$

where  $\chi$  denotes the DM particle. In particular, the energy conservation of the initial and final states in this process induces a localized recoil energy of nucleus or electron

$$
E _ {R} = m _ {\chi} ^ {2} / 2 m _ {N, e}. \tag {1.2}
$$

This kinematics exhibits a distinct peak-like signature in the scattering rate [10, 11], rather than the smooth distribution in ordinary elastic scattering. The possible peak-like energy deposit would enable us to search for the relevant interaction between DM and neutrino in this way. In fact, the inverse process, i.e., the conversion from neutrino to an exotic fermion [13-17], has been utilized to explain the recent XENON1T excess [18]. It turns out that the neutrino magnetic dipole portal can account for the excess of keV electron recoil events because the induced scattering rate is inversely proportional to the recoil energy [14, 19-22]. It is thus natural to consider the above fermionic DM absorption through the transition from dark magnetic dipole and the dynamical conversion to neutrino. Naively speaking, according to the recoil energy formula in eq. (1.2), the absorption by the nucleus and electron targets in direct detection experiments is sensitive to sub-GeV or sub-MeV DM, respectively.

In this work we consider a Dirac fermion DM  $\chi$  charged under a dark gauge group  $U(1)'$  and the dark magnetic dipole operator. The dark gauge field  $A'$  interacts with the Standard Model (SM) electromagnetic field through a kinetic mixing term. The DM field mixes with right-handed neutrino and the DM- $\nu$  tensor current interacts with the ordinary electromagnetic charge current via the kinetic mixing term of gauge fields. As a result, the incoming DM is absorbed and converted into neutrino in final states intermediated by dark photon through the dipole-charge interaction. We also estimate the contribution from the nuclear magnetic dipole by evaluating the nuclear magnetic dipole form factor for inelastic DM-nucleus scattering. The inelastic scattering off electron target will also be studied by calculating the ionization form factor of the bound electrons. We aim to obtain the prospective sensitivity of direct detection experiments to the dark magnetic dipole moment, the kinetic mixing of gauge fields as well as the DM- $\nu$  coupling.

This paper is organized as follows. In section 2 we describe the dark photon model with DM magnetic dipole moment. In section 3 we study the DM absorption by nuclear targets, and display the projected constraint on the total cross section as well as the couplings. The ionization signal in the DM absorption by electron target will be discussed in section 4. Our main conclusions are summarized in section 5. We show how we calculate the nuclear magnetic dipole form factor and the ionization form factor in appendices.

# 2 The dark photon model with magnetic dipole moment

We consider a Dirac fermion  $\chi$  charged under a dark gauge group  $\mathrm{U}(1)'$ . The magnetic dipole operator of  $\chi$  and the gauge Lagrangian of the dark gauge field  $A_{\mu}^{\prime}$  are given by

$$
\mathcal {L} \supset \frac {\mu_ {\chi}}{2} \bar {\chi} \sigma^ {\mu \nu} \chi F _ {\mu \nu} ^ {\prime} + \frac {1}{4} F ^ {\prime \mu \nu} F _ {\mu \nu} ^ {\prime} + \frac {\epsilon}{2} F ^ {\mu \nu} F _ {\mu \nu} ^ {\prime} + \frac {1}{2} m _ {A ^ {\prime}} ^ {2} A ^ {\prime \mu} A _ {\mu} ^ {\prime}, \tag {2.1}
$$

where  $\mu_{\chi}$  is the dipole strength,  $F_{\mu \nu} = \partial_{\mu}A_{\nu} - \partial_{\nu}A_{\mu}$  is the SM electromagnetic field tensor and  $F_{\mu \nu}^{\prime} = \partial_{\mu}A_{\nu}^{\prime} - \partial_{\nu}A_{\mu}^{\prime}$  is the field strength tensor of  $\mathrm{U}(1)^{\prime}$ . For dark photon, see ref. [23]

![](images/b626c07f83ebfa99d5cd4f14964b2a8f823dff16a5af66ba25bcb5575e732248.jpg)  
Figure 1. Diagrams for DM absorption from dipole-charge (left) or dipole-dipole (right) interaction in our model. The black dot denotes the magnetic dipole operator.

![](images/0dfa7d5b70e2950b45a3ac57ba9f46ff12aa16bad071f2add275d481cc23b51a.jpg)

for a recent review and references therein. A scalar field  $\phi$  charged under  $\mathrm{U}(1)'$  is then introduced and the relevant Lagrangian is

$$
\mathcal {L} \supset m _ {\chi} \bar {\chi} \chi + y \phi \bar {\chi} P _ {R} \nu + \text {h . c .}. \tag {2.2}
$$

The right-handed fields  $\chi_R$  and  $\nu_{R}$  are then mixed and shifted in terms of a mixing angle  $\theta_{R} = y\langle \phi \rangle /m_{\chi}$  [10-12]. Thus, the  $\chi_R$  eigenstate has an additional component  $-\theta_{R}\nu_{R}$ . Suppose the SM fermions are not charged under  $\mathrm{U}(1)^{\prime}$ , the diagonalization of the kinetic mixing term in eq. (2.1) gives the coupling of dark photon  $A^{\prime}$  to the ordinary electromagnetic current  $-e\epsilon A_{\mu}^{\prime}J_{em}^{\mu}$ . Then we have the following effective interaction as shown in the left panel of figure 1

$$
\mathcal {L} _ {\text {e f f}} \supset \frac {\epsilon e Q _ {f} \mu_ {\chi} \theta_ {R}}{q ^ {2} - m _ {A ^ {\prime}} ^ {2}} q ^ {\mu} \bar {\chi L} \sigma_ {\mu \nu} \nu_ {R} \bar {f} \gamma^ {\nu} f + \text {h . c .}, \tag {2.3}
$$

where  $q$  is the momentum transfer carried by the dark photon,  $f$  denotes the SM quark or electron and  $Q_{f}$  is the electromagnetic charge of fermion  $f$ . One can see that the DM only scatters off proton or electron but not neutron as the electromagnetic charge of neutron is zero.

On the other hand, some nuclei targets have sizable magnetic dipoles such as cesium (Cs), iodine (I) or a couple of xenon's isotopes. Thus, besides the above dipole-charge (DC) interaction, there could be dipole-dipole (DD) contribution in the scattering on a nucleus when the dark photon interacts with the nuclear magnetic dipole as shown in the right panel of figure 1. The scattering induced by the dipole-dipole interaction may dominate over the dipole-charge scattering and accounts for the DAMA annual modulation signature [8, 9]. The dipole-dipole interaction at the nuclear level in our model is given by

$$
\frac {\epsilon \mu_ {\chi} \mu_ {N} \theta_ {R}}{q ^ {2} - m _ {A ^ {\prime}} ^ {2}} q ^ {\mu} q ^ {\alpha} g ^ {\nu \beta} \bar {\chi L} \sigma_ {\mu \nu} \nu_ {R} \bar {N} \sigma_ {\alpha \beta} N + \text {h . c .}, \tag {2.4}
$$

where  $\mu_N$  denotes the nuclear magnetic moment.

To guarantee that the fermion  $\chi$  serves as a stable DM particle, the lifetime of  $\chi$  should be longer than the age of the Universe, i.e.  $t_{\mathrm{Universe}} = 4.4\times 10^{17}$  sec [24]. Requiring the DM being stable at the Universe time scale would set a stringent bound on the coupling

and the mass of DM particle. For the above model mediated by dark photon, the leading decay channel would be  $\chi \rightarrow \nu \gamma \gamma \gamma$  for light DM [12]. The two-body decay  $\chi \rightarrow \nu A^{\prime}$  can be forbidden by requiring  $m_{\chi} < m_{A^{\prime}}$ . We define  $U = \mu_{\chi}\epsilon \theta_{R}$  and recall the decay rate in refs. [10-12] as

$$
\Gamma (\chi \rightarrow \nu \gamma \gamma \gamma) \simeq 1 0 ^ {- 3 2} \mathrm {s} ^ {- 1} \left(\frac {m _ {\chi}}{1 0 0 \mathrm {k e V}}\right) ^ {1 5} \left(\mathrm {T e V} \cdot e U\right) ^ {2} \left(\frac {\mathrm {G e V}}{m _ {A ^ {\prime}}}\right) ^ {4}. (2. 5)
$$

Note that this result assumes that the dark photon mass is larger than the momentum transfer.

# 3 Dark matter absorption by nuclear targets

For DM absorption by nuclear targets, i.e.,  $\chi + N \rightarrow \nu + N$ , the differential scattering cross section induced by neutral current (NC) is given by

$$
\begin{array}{l} \frac {d \sigma_ {N C}}{d E _ {R}} = \frac {d \sigma_ {D C}}{d E _ {R}} + \frac {d \sigma_ {D D}}{d E _ {R}} \tag {3.1} \\ = \frac {\alpha \mu_ {\chi} ^ {2} \theta_ {R} ^ {2} \epsilon^ {2} m _ {\chi}}{v m _ {N} (m _ {A ^ {\prime}} ^ {2} + 2 m _ {N} E _ {R}) ^ {2}} Z ^ {2} F _ {Z} ^ {2} (E _ {R}) \delta (E _ {R} - E _ {R} ^ {0}) \\ \left(6 m _ {N} ^ {2} m _ {\chi} E _ {R} - 8 m _ {N} ^ {2} E _ {R} ^ {2} - m _ {N} m _ {\chi} ^ {3} + 4 m _ {N} m _ {\chi} ^ {2} E _ {R} - 2 m _ {N} m _ {\chi} E _ {R} ^ {2} + m _ {\chi} ^ {3} E _ {R}\right) \\ + \frac {\mu_ {\chi} ^ {2} \mu_ {N} ^ {2} \theta_ {R} ^ {2} \epsilon^ {2} m _ {\chi} E _ {R}}{2 \pi v (m _ {A ^ {\prime}} ^ {2} + 2 m _ {N} E _ {R}) ^ {2}} \frac {I + 1}{3 I} F _ {D} ^ {2} (E _ {R}) \delta (E _ {R} - E _ {R} ^ {0}) \\ \Big (- 4 m _ {N} ^ {2} E _ {R} ^ {2} + 8 m _ {N} m _ {\chi} ^ {2} E _ {R} - 8 m _ {N} m _ {\chi} E _ {R} ^ {2} + 2 m _ {N} E _ {R} ^ {3} + m _ {\chi} ^ {4} + 4 m _ {\chi} ^ {3} E _ {R} - 3 m _ {\chi} ^ {2} E _ {R} ^ {2} \Big), \\ \end{array}
$$

where  $E_R^0 = m_\chi^2 / 2m_N$ ,  $v$  is the DM velocity,  $Z$  is the atomic number,  $I$  is the nuclear spin,  $F_Z(E_R)$  is the ordinary nuclear form factor and  $F_D(E_R)$  is the nuclear magnetic dipole form factor. The two terms in the above differential cross section correspond to the dipole-charge (DC) interaction and the dipole-dipole (DD) interaction, respectively. The kinematics in this inelastic scattering with nearly massless neutrino in final states simplifies the energy conservation and leads to the delta functions in eq. (3.1) by only keeping the  $\mathcal{O}(v^0)$  terms. As a result, the fermion DM absorption recoil is peaked at  $m_\chi^2 / 2m_N$ . This is the key difference between the DM absorption and the usual elastic scattering.

Given the delta function in eq. (3.1), the DM-nucleus scattering rate from the dipole-charge interaction can be easily obtained as [11]

$$
R = \frac {\rho_ {\chi}}{m _ {\chi}} \sigma_ {N C} Z ^ {2} \sum_ {j} N _ {T, j} F _ {j} (q) ^ {2} \Theta \left(E _ {R, j} ^ {0} - E _ {t h}\right), \tag {3.2}
$$

where  $\rho_{\chi}$  is the local DM density,  $\sigma_{NC}$  is the total cross section of inelastic DM-nucleon scattering,  $N_{T}$  and  $F(q)$  correspond to the target number per detector mass and nuclear form factor, respectively, and  $\Theta$  is a step function enforcing the minimal recoil energy to be the energy threshold  $E_{th}$  of the detector. All isotope targets in the experiments should be summed over the index  $j$ . Note that we replace the atom mass number  $A$  in the eq. (3.8) of ref. [11] by the atomic number  $Z$  here for our model and extract it out of eq. (3.1).

![](images/12189f555d2eda736f46cd0fdb4065e20d0a85d6de101f62834a97f72280194f.jpg)  
Figure 2. Projected constraints on the DM-nucleon cross section  $\sigma_{NC}$  in our model as a function of  $m_{\chi}$ . The constraints are given for different experiments: LUX (pink) [25], PandaX-II (blue) [26], XENON1T (purple) [27], CRESSTII (red) [28], CRESSTIII (orange) [29] and DarkSide-50 (green) [30, 31]. The target isotopes include  $^{131}\mathrm{Xe}$  for LUX, PandaX-II, and XENON1T,  $^{186}\mathrm{W},^{40}\mathrm{Ca},^{16}\mathrm{O}$  for CRESSTII and CRESSTIII, and  $^{40}\mathrm{Ar}$  for DarkSide-50.

Moreover, as we drop the high order terms of DM velocity  $O(v)$ , the integration over DM velocity distribution  $f(v)$  should be normalized, i.e.,  $\int d^3vf(v) = 1$ . When only considering the dipole-charge contribution in the first term of eq. (3.1), one can project a bound on  $\sigma_{NC}$  by requiring a certain number of absorption events in any given experiment (here for simplicity  $< 10$  events with the exposures and  $E_{th}$  values in table 3 of ref. [11]). In figure 2 we show the projected constraints on the DM-nucleon cross section  $\sigma_{NC}$  in our model as a function of  $m_{\chi}$ . The lower limit of DM mass is determined by the recoil energy threshold in each experiment. For instance, XENON1T can probe the DM mass above  $27\mathrm{MeV}$  and is sensitive to  $\sigma_{NC} \gtrsim 10^{-49}\mathrm{cm}^2$ . The kinks occur for different DM masses due to the atomic numbers of different target isotopes and the step function in eq. (3.2) determines the abscissa of kink according to  $m_{\chi} = \sqrt{2m_{N}E_{th}}$ . In addition, we consider the DM mass less than  $150\mathrm{MeV}$  because the nuclear recoil energy threshold is normally smaller than  $100\mathrm{keV}$ . In this range, the influence caused by nuclear form factor can be neglected.

Note that the above constraint on  $\sigma_{NC}$  given by eq. (3.2) is independent of the DM absorption models. Next we wonder the specific constraint on the effective interaction in eq. (2.3) and take into account higher order expansion of DM velocity. After integrating eq. (3.2) over the DM velocity distribution  $f(v)$ , the differential scattering rate per nuclear recoil energy for the dipole-charge interaction is given by

$$
\begin{array}{l} \frac {d R _ {D C}}{d E _ {R}} = N _ {T} \frac {\rho_ {\chi}}{m _ {\chi}} \sqrt {\frac {E _ {R}}{2 m _ {N}}} \frac {e ^ {2} U ^ {2} m _ {N}}{4 \pi m _ {\chi} p _ {\nu} (m _ {A ^ {\prime}} ^ {2} + 2 m _ {N} E _ {R}) ^ {2}} Z ^ {2} F _ {Z} ^ {2} (E _ {R}) \int d ^ {3} \pmb {v} \frac {f (\pmb {v})}{v} \Theta (v - v _ {\mathrm {m i n}}) \\ \times \left[ 6 m _ {N} ^ {2} m _ {\chi} E _ {R} - 8 m _ {N} ^ {2} E _ {R} ^ {2} - m _ {N} m _ {\chi} ^ {3} + 4 m _ {N} m _ {\chi} ^ {2} E _ {R} - 2 m _ {N} m _ {\chi} E _ {R} ^ {2} + m _ {\chi} ^ {3} E _ {R} \right], \tag {3.3} \\ \end{array}
$$

![](images/6b9a540593ce6aa318981db20e4faa0d6a1dd35c89e0728fd0383cd5a8789f43.jpg)  
(a)  $m_{\chi} = 10 \mathrm{MeV}$

![](images/91da10e302b7bf0657cf863cf00a6c41db66c03f56594fea6c3e74f6bfdbd437.jpg)  
Figure 3. Differential scattering rates of target  $^{131}\mathrm{Xe}$  for some masses of DM and dark photon. The coupling  $e^2 U^2$  in eq. (3.3) is fixed to be  $10^{-50}\mathrm{cm}^2$ . The differential rates of the scalar and vector interactions with  $1 / \Lambda^2 = 10^{-50}\mathrm{cm}^2$  in ref. [10] are also shown for reference.  
(b)  $m_{\chi} = 100 \mathrm{MeV}$

where  $p_{\nu}$  is neutrino momentum and  $U$  is defined as  $U = \mu_{\chi}\theta_{R}\epsilon$ . Since the velocity distribution is non-trivial in this case, we use the truncated Maxwell distribution  $f(v)$  [32, 33]. The  $f(v)$  is truncated at  $\Theta (v_{\mathrm{esc}} - |\vec{v} +\vec{v}_e(t)|)$ , according to the DM standard halo model where  $\vec{v}$  is the speed of DM,  $v_{\mathrm{esc}}\sim 550~\mathrm{km / s}$  is the galactic escape velocity, and  $\vec{v}_{e}(t)$  is the speed of earth which can be decomposed into the Sun's motion in the Galaxy and the Earth's motion in solar system orbit  $(\vec{v}_{\odot}(t) + \vec{v}_{\oplus}(t))$ . In figure 3 we show the differential scattering rate of target  $^{131}\mathrm{Xe}$  for some masses of DM and dark photon. One can see that the distributions indeed peak around  $m_{\chi}^{2} / 2m_{N}$ . Although lighter DM produces more events, the recoil energy of these nuclear scatterings is less than  $1\mathrm{keV}$  when  $m_{\chi} < 10\mathrm{MeV}$  which is too small to be detected by current detectors. For the majority of DM detection experiments, the recoil energy thresholds are generally greater than  $1\mathrm{keV}$ . Furthermore, the widths of the spectra in figure 3 are also very small. Different target isotopes result in a tiny distinction for the spectra. For example, in CRESSTII the target  $\mathrm{CaWO_4}$  contains four isotopes of tungsten:  $^{182}\mathrm{W}$ ,  $^{183}\mathrm{W}$ ,  $^{184}\mathrm{W}$  and  $^{186}\mathrm{W}$  [28] which are only distinguishable when the energy resolution is less than  $50\mathrm{eV}$ . For comparison, by taking XENON1T experiment for illustration, the resolution of the reconstructed energy yields  $5\%$  (1.4%) for energy deposit 41.5 (609) keV as shown in ref. [34]. Thus, the typical energy resolution there is about  $2\mathrm{keV}$  for  $40\mathrm{keV}$  recoil energy.

To constrain the coupling  $e^2 U^2$ , after integrating over the recoil energy, we have the total scattering rate due to the dipole-charge interaction

$$
R _ {D C} = N _ {T} \left(\frac {\rho_ {\chi}}{m _ {\chi}}\right) \frac {e ^ {2} U ^ {2}}{4 \pi \left(m _ {A ^ {\prime}} ^ {2} + m _ {\chi} ^ {2}\right) ^ {2}} \left(2 m _ {\chi} ^ {4}\right) Z ^ {2} F _ {Z} ^ {2} (q) \Theta \left(E _ {R} ^ {0} - E _ {t h}\right), \tag {3.4}
$$

where  $q = |\mathbf{q}| = \sqrt{2m_{N}E_{R}}\sim m_{\chi}$ . The only unknown parameter is the dark photon mass  $m_{A^{\prime}}$ . In figure 4 we show the projected constraint on  $e^2 U^2$  for both liquid (left) and crystal (right) targets, assuming different dark photon masses. Lower  $e^2 U^2$  can be constrained for decreasing  $m_{A^{\prime}}$ , for instance  $e^2 U^2\simeq 10^{-47}\mathrm{cm}^2$  or  $10^{-45}\mathrm{cm}^2$  for  $m_{A^{\prime}} = 100\mathrm{keV}$ . The target isotope of DarkSide-50 is  $^{40}\mathrm{Ar}$  which is lighter than  $^{131}\mathrm{Xe}$  and its recoil energy threshold is

![](images/da48d54c75a81c606c484dcfd22255eee5dabfaf11b9f9af6bfd53569fbe5059.jpg)  
Figure 4. The projected constraint on  $e^2 U^2$  from dipole-charge contribution for both liquid (left) and crystal (right) targets, assuming different dark photon masses.

![](images/29546c6d5ba740904b82d563474b5d4f9ca12bef5122c7c7da2102164d9202b1.jpg)

50 times lower than those of XENON1T and PandaX-II. Thus, as shown in the left panel, the DarkSide-50 bounds can reach a lower DM mass limit. The target isotope of CRESSTII and CRESSTIII is  $\mathrm{CaWO_4}$  [28, 29]. As seen from the right panel, due to the threshold  $\Theta (E_R^0 -E_{th})$ , there appear three kinks corresponding to oxygen  $(^{16}\mathrm{O})$ , calcium  $(^{40}\mathrm{Ca})$  and tungsten  $(^{186}\mathrm{W})$  from left to right. For large DM mass, there is an apparent increasing behavior due to the strong suppression of Helm form factor  $F_{Z}(q)$  with high momentum transfer.

For the nuclei targets discussed above, there is a lower limit of  $m_{\chi} \sim \mathrm{MeV}$  for the searching capability due to the detector energy threshold at keV level and the nuclear masses. There exist proposals of future experiments with light nuclei (such as Hydrogen or Lithium [35, 36]) or semiconductor/superconductor (see ref. [37] for a recent review) and low-threshold at the level of 1 eV or even less. As a result, the detectable DM mass can reach as low as  $\mathcal{O}(0.01)$  MeV [11]. To explore sub-MeV DM mass region, we also consider new scattering strategy which will be discussed in next section.

Moreover, it turns out that the DM lifetime constraint becomes quite severe for the sensitive region of the above DM-nucleus scattering. For the DM mass range of  $m_{\chi} \gtrsim 1 \mathrm{MeV} \gtrsim 2m_e$ , the dominant decay channel would be  $\chi \rightarrow \nu e e$  at tree-level. The decay width becomes  $\Gamma (\chi \rightarrow \nu e e) \simeq 10^{-8} \mathrm{s}^{-1} \left( \frac{m_{\chi}}{1 \mathrm{MeV}} \right)^{7} \left( \mathrm{TeV} \cdot eU \right)^{2} \left( \frac{\mathrm{GeV}}{m_{A'}} \right)^{4}$ . For lower DM masses the dominant decay is  $\chi \rightarrow \nu \gamma \gamma \gamma$  given in eq. (2.5). These constraints rule out the sensitive region of DM-nucleus scattering in figure 4 for those nuclei targets. To avoid such constraints, in theoretical aspect, one needs advanced model building and induce necessary fine-tuning in the UV completion. In an alternative model, we can consider SM fermions charged under the new  $\mathrm{U}(1)'$  and the charge current is  $J_{\mu}' = Q_f' g' \bar{f} \gamma_\mu f$  but with non-universal charges  $Q_f'$ . Thus, the diagrams in above decay processes are induced by  $A'$  propagator without additional kinetic mixing. We further assume leptophobic  $A'$  to forbid  $\chi \rightarrow \nu e e$  decay. Moreover, the charges of SM quarks are fine-tuned in the loop of  $\chi \rightarrow \nu \gamma \gamma \gamma$  process. As a result, the decay widths are highly suppressed. Nevertheless, the UV completion would be quite dedicated to avoid the lifetime constraint. In the

aspect of experiment, as mentioned above, future low-threshold detectors would have energy threshold at eV level or even less and be sensitive to much lower DM masses [11]. In addition, other detection strategies such as cosmic-ray boosted DM [38] or Midgal effect [39] would also lower the detectable DM mass range. These improvements can also help to evade the lifetime constraint. We leave the relevant studies to a future work. This also motivates us to explore lighter DM through the scattering of DM and bound electrons.

In addition, we can also take into account the dipole-dipole contribution in eq. (3.1) and obtain the relevant scattering rate as follows

$$
R _ {D D} = N _ {T} \left(\frac {\rho_ {\chi}}{m _ {\chi}}\right) \frac {\mu_ {N} ^ {2} U ^ {2}}{2 \pi \left(m _ {A ^ {\prime}} ^ {2} + m _ {\chi} ^ {2}\right) ^ {2}} \frac {I + 1}{3 I} \left(\frac {m _ {\chi} ^ {3}}{2 m _ {N}}\right) F _ {D} ^ {2} (q) \frac {m _ {\chi} ^ {4}}{2 m _ {N} ^ {2}} \left(8 m _ {N} ^ {2} - m _ {\chi} ^ {2}\right) \Theta \left(E _ {R} ^ {0} - E _ {t h}\right), \tag {3.5}
$$

where the nuclear magnetic dipole form factor  $F_{D}$  includes the contributions from both angular momentum and nuclear spin. Recall that in DAMA experiment (target NaI) iodine has large nuclear magnetic moment and large mass, thus it is necessary to consider the dipole-dipole contribution. Although the magnetic dipole moment of xenon is not as large as iodine, we wonder here whether the dipole-dipole contribution from xenon target can induce sizable constraint for the given scattering process in eq. (3.1). According to appendix A, the form factor  $F_{D}$  for  $^{131}\mathrm{Xe}$  can be written as

$$
F _ {D} ^ {2} (q) = \left(0. 4 \frac {L (q)}{L (0)} + 0. 6 \sqrt {\frac {S (q)}{S (0)}}\right) ^ {2}, \tag {3.6}
$$

where  $L(q)$  (the spin-independent Helm form factor) and  $S(q)$  are the angular momentum and nuclear spin contributions to the magnetic dipole moment, respectively. The detailed expression of  $S(q)$  is given by polynomial fitting and the fitted coefficient can be found in ref. [40]. For  $^{131}\mathrm{Xe}$  one has  $I = 3/2$  and  $\mu_N = 0.692e/2m_p$  [9]. We then display the bound on  $e^2U^2$  from eq. (3.5) for  $^{131}\mathrm{Xe}$  in the left panel of figure 5. It shows that there is no significant contribution from dipole-dipole interaction for the inelastic DM absorption. Note that, since the  $O(v)$  terms are neglected, we here make an approximation of the momentum transfer that is  $q = \sqrt{E_R^2 + 2m_nE_R} \approx m_\chi$  with  $E_R \approx m_\chi^2 / 2m_N$ . Thus, the form factors  $F_D(q)$  and  $F_Z(q)$  are more precise for low DM masses  $m_\chi \ll 1\mathrm{GeV}$  as shown in the right panel of figure 5.

# 4 Dark matter absorption by electron targets

As seen from the above section, the DM absorption by nuclear targets leads to distinctive peak-like scattering signal. However, due to the limited energy resolution, it is very likely to suffer from the difficulties of identifying the energy deposition and distinguishing the target isotopes. The fermionic DM can also be absorbed by bound electron targets, which induces ionization signal. Such signal would be sensitive to lower DM mass and the electron binding energies from both inner and outer atomic shells make the localized recoil energy  $E_{R} = m_{\chi}^{2} / 2m_{e}$  spread out.

![](images/b98ce4a8496eec800c1e5f1394faa0fe3125fcea514ac81e9e04e0f3b1ee969f.jpg)  
Figure 5. Left: the projected constraint on  $e^2 U^2$  from dipole-dipole contribution for  $^{131}\mathrm{Xe}$  target. The assumed dark photon masses are the same as those in figure 4. Right: the comparison of form factors  $F_Z^2(q)$  and  $F_D^2(q)$ .

![](images/6cb41565d979ca237d50b04e24e9c77c62ac6a3ba312975a26040f92f367bc5e.jpg)

According to the effective Lagrangian in eq. (2.3), induced by the dipole-charge interaction, we have the differential scattering cross section of DM absorption by electron

$$
\begin{array}{l} \frac {d \langle \sigma_ {\mathrm {i o n}} ^ {n l} v \rangle_ {D C}}{d E _ {R}} = \frac {| \mathcal {M} | ^ {2}}{6 4 \pi m _ {\chi} m _ {e} ^ {2}} \frac {q}{E _ {R}} | f _ {\mathrm {i o n}} ^ {n l} (k ^ {\prime}, q) | ^ {2} \Theta (q) \\ = \frac {e ^ {2} U ^ {2}}{1 6 \pi (m _ {A ^ {\prime}} ^ {2} - m _ {\chi} (m _ {\chi} - 2 q)) ^ {2}} \frac {q}{E _ {R}} \frac {m _ {\chi} ^ {2}}{m _ {e} ^ {2}} | f _ {\mathrm {i o n}} ^ {n l} (k ^ {\prime}, q) | ^ {2} \Theta (q) \\ \times \left[ - 4 m _ {e} m _ {\chi} \left(m _ {e} + m _ {\chi}\right) - m _ {\chi} ^ {3} + 3 \left(m _ {\chi} ^ {2} + 2 m _ {e} ^ {2} + 4 m _ {e} m _ {\chi}\right) q - 2 \left(m _ {\chi} + 4 m _ {e}\right) q ^ {2} \right], \tag {4.1} \\ \end{array}
$$

where the bracket  $\langle \dots \rangle$  denotes the integral of the Maxwell-Boltzmann DM velocity distribution  $f(v)$  as mentioned in section 3, and  $k^{\prime} = \sqrt{2m_{e}E_{R}}$  is the momentum of the electron in the shell  $(n,l)$ . For the electron scattering, we should sum over all possible shells together and the differential scattering rate is

$$
\frac {d R _ {\text {i o n}}}{d E _ {R}} = N _ {T} \frac {\rho_ {\chi}}{m _ {\chi}} \sum_ {n l} \frac {d \left\langle \sigma_ {\text {i o n}} ^ {n l} v \right\rangle_ {D C}}{d E _ {R}}. \tag {4.2}
$$

To evaluate the integral of the scattering cross section, one should specify the electron ionization form factor  $|f_{\mathrm{ion}}^{nl}(k',q)|$  which becomes an important part in the calculation of the fermionic DM absorption by electron target.

The general form of the ionization form factor  $|f_{\mathrm{ion}}^{nl}(k',q)|$  can be given in terms of Wigner 3-  $j$  symbol, spherical Bessel functions  $j_{L}$  and radial wave-functions [41, 42]

$$
\left| f _ {\text {i o n}} ^ {n l} \left(k ^ {\prime}, q\right) \right| ^ {2} = \frac {4 k ^ {\prime 3}}{(2 \pi) ^ {3}} \sum_ {l ^ {\prime} L} (2 l + 1) (2 l ^ {\prime} + 1) (2 L + 1) \times \left[ \begin{array}{c c c} l & l ^ {\prime} & L \\ 0 & 0 & 0 \end{array} \right] ^ {2} \left| \int r ^ {2} d r R _ {k ^ {\prime} l ^ {\prime}} (r) R _ {n l} (r) j _ {L} (q r) \right| ^ {2}, \tag {4.3}
$$

where the sum  $\sum_{l' L}$  denotes  $\sum_{l'=0}^{\infty} \sum_{L=|l-l'|}^{l+l'}$  (excluding  $L = 0$ ). Here we have used the following fact that the angular integral of the product of three spherical harmonics can be

given by [43]

$$
\begin{array}{l} \int d \Omega Y _ {l _ {1}} ^ {m _ {1}} (\theta , \phi) Y _ {l _ {2}} ^ {m _ {2}} (\theta , \phi) Y _ {l _ {3}} ^ {m _ {3}} (\theta , \phi) \\ = \sqrt {\frac {(2 l _ {1} + 1) (2 l _ {2} + 1) (2 l _ {3} + 1)}{4 \pi}} \times \left[ \begin{array}{l l l} l _ {1} & l _ {2} & l _ {3} \\ 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{l l l} l _ {1} & l _ {2} & l _ {3} \\ m _ {1} & m _ {2} & m _ {3} \end{array} \right]. \tag {4.4} \\ \end{array}
$$

The angular quantum numbers  $l, l'$  and  $L$  rely on specific shells, and the spherical Bessel functions  $j_{L}(qr)$  are also known.  $R_{nl}(r)$  denotes the bound electron radial wave-function and  $R_{k'l'}(r)$  is the radial wave-function of the outgoing unbound electrons. The detailed calculation of the radial wave-functions  $R_{k'l'}(r)$  and  $R_{nl}(r)$  is given in appendix B.

Now we can numerically determine the value of ionization form factor. In the fermionic DM absorption by electron target, i.e.,  $\chi + e \rightarrow \nu + e$ , the momentum transfer is approximately equal to  $q = m_{\chi} + E_B^{nl} - E_R$  with negative binding energy  $E_B^{nl} < 0$ . We should note that the radial integral in eq. (4.3) is complicated in general and the convergence speed depends on different orbitals. It means that we should determine the iteration number of every orbital. In fact, for inner shells 1s, 2s, 2p, ..., 4s, the electron energies on these orbitals are lower than those of 4p, 4d, 5s and 5p shells. Thus, their radial wave-functions decrease faster (see figure 9 in appendix B), and the convergence of numerical calculation acts quickly. To efficiently evaluate the integral for the outer shells, we replace eq. (4.3) by the following form [44, 45]

$$
\left| f _ {\text {i o n}} ^ {n l} \left(k ^ {\prime}, q\right) \right| ^ {2} = \frac {(2 l + 1) k ^ {\prime 2}}{4 \pi^ {3} q} \int_ {\left| k ^ {\prime} - q \right|} ^ {\left| k ^ {\prime} + q \right|} k d k \left| \chi_ {n l} (k) \right| ^ {2}, \tag {4.5}
$$

where  $\chi_{nl}(k)$  is an analytical function in momentum space [46, 47]

$$
\begin{array}{l} \chi_ {n l} (k) = 4 \pi i ^ {l} \int d r r ^ {2} R _ {n l} (r) j _ {L} (k r) \\ = \sum_ {j} C _ {n l j} 2 ^ {n _ {l j} - l} \left(\frac {2 \pi a _ {0}}{Z _ {l j}}\right) ^ {3 / 2} \left(\frac {i k a _ {0}}{Z _ {l j}}\right) ^ {l} \times \frac {\Gamma (n _ {l j} + l + 2)}{\Gamma (l + 3 / 2) \sqrt {(2 n _ {l j}) !}} \tag {4.6} \\ \times_ {2} F _ {1} \left[ \frac {1}{2} (n _ {l j} + l + 2), \frac {1}{2} (n _ {l j} + l + 3), l + \frac {3}{2}, - \left(\frac {a _ {0} k}{Z _ {l j}}\right) ^ {2} \right]. \\ \end{array}
$$

In this way we can easily obtain the ionization form factor for different recoil energies. However, it does not work well for the case of light DM ( $\lesssim 50\mathrm{keV}$ ) scattering. In our content, as the DM initial momentum is negligible and we assume  $E_{R} - E_{B}^{nl}\ll m_{\chi}$ , one has  $q = m_{\chi} + E_B^{nl} - E_R\sim m_\chi \gg 0$ . Thus, for larger DM mass and lower recoil energy, the calculation based on the above formula is more precise.

Thus, to ensure both efficiency and precision, we compute the ionization form factor for different DM masses in different ways. When  $m_{\chi} < 50 \mathrm{keV}$ , we numerically evaluate eq. (4.3) by modifying the public code DarkARC from ref. [48]. For  $m_{\chi} > 50 \mathrm{keV}$ , we use eq. (4.5) to analytically calculate the form factor. We display the obtained ionization form factor of different orbitals in figure 6. One can see that the outer orbital shells dominate

![](images/1d0bbe759598561a5fdc50f91419be6d20ca745f1320ffc80f357f9a0537cc24.jpg)  
Figure 6. The ionization form factors of some electron orbitals with  $m_{\chi} = 20 \mathrm{keV}$  and  $200 \mathrm{keV}$ .

at  $m_{\chi} = 200 \mathrm{keV}$ , while the contributions from shells 1s and 2p are negligible compared to the outer ones. For the case of  $m_{\chi} = 20 \mathrm{keV}$ , although the outmost electron does not dominate anymore, there is still a distinct difference between the form factors of the inner and outer orbitals.

In fact, there is also an enhancement due to the attractive potential around the nucleus which results in a larger phase space. This effect is attributed to the difference between the exact and the free (under the plane wave approximation) wave-functions. We compensate it by an extra factor of  $E_{R}$  and  $Z_{\mathrm{eff}}$ , usually called Fermi factor  $F(E_{R},Z_{\mathrm{eff}}) = |\Psi_{\mathrm{exact}}(0) / \Psi_{\mathrm{free}}(0)|^2$  [44]. It can be given by the following form in non-relativistic limit

$$
F (E _ {R}, Z _ {\mathrm {e f f}}) = \frac {2 \pi \xi}{1 - e ^ {- 2 \pi \xi}}, \quad \xi = \alpha Z _ {\mathrm {e f f}} \sqrt {\frac {m _ {e}}{2 E _ {R}}}, \tag {4.7}
$$

which tends to unity for large recoil energy. Actually, this contribution to the ionization form factor is negligible for inner shells.

We show the ionization rate of fermionic DM absorption by electron targets in  $^{131}\mathrm{Xe}$  in the left panel of figure 7. The coupling  $e^2 U^2$  is fixed to be  $10^{-45}\mathrm{cm}^2$  and we take different masses of DM and dark photon for illustration. It turns out that lighter DM favors softer spectrum and lighter dark photon enhances the ionization rate. Note that the step function  $\Theta (q)$  in eq. (4.1) forces the recoil energy range to be  $q = m_{\chi} + E_B^{nl} - E_R > 0$  with  $E_B^{nl}$  being the binding energy. Thus, the differential scattering rate is truncated at high recoil energies and the cutoff depends on both the DM mass and the binding energy of electron. On the other hand, the profile of ionization rate is determined by the ionization form factor  $|f_{\mathrm{ion}}^{nl}(k',q)|^2$ . We find that each ionization rate with  $m_{\chi} > 50\mathrm{keV}$  has a peak of the maximal rate for  $E_R > 1\mathrm{keV}$ . Given the ionization form factor, we find that the ionization rate has a broader distribution with respect to the recoil energy than that in DM-nucleon scattering. This signal can thus be searched for through the photoelectron signature in the detector.

![](images/6e280eb4a138042d8536c5ff65bebed415bbef158023c04ed2fa8de9ea83b753.jpg)  
Figure 7. Left: ionization rate with different masses of DM and dark photon  $m_{A'}$ . The coupling  $e^2 U^2$  is fixed at  $10^{-45} \, \mathrm{cm}^2$ . The curve corresponding to  $m_{\chi} = 20 \, \mathrm{keV}$  and  $m_{A'} = 1 \, \mathrm{MeV}$  has been multiplied by a factor of  $10^3$ . Right: the projected constraint on  $e^2 U^2$  from the electron ionization of  $^{131}\mathrm{Xe}$  with an exposure of one tonne·year. The shaded region has been ruled out by DM lifetime.

![](images/0978f8bd3c4409c8e477432b5324b6e18c33bec9e2cc7e726c9dd7ff5df03701.jpg)

The right panel of figure 7 shows the projected constraint on  $e^2 U^2$  from the electron ionization of  $^{131}\mathrm{Xe}$  with an exposure of one tonne-year. We again assume at least 10 events to be observed. The recoil energy has been integrated over from  $1\mathrm{keV}$  to the cutoff. The shaded region has been ruled out by DM lifetime. One can see that, for extremely small dark photon mass, the limit of the coupling  $e^2 U^2$  can be pushed down to  $10^{-49}\mathrm{cm}^2$ . Note that the 2-body decay  $\chi \rightarrow \nu A'$  is allowed if  $m_{A'} < m_{\chi}$ . However, this decay has no dependence on the kinetic mixing  $\epsilon$  and is parametrically different from the scattering cross section in eq. (4.1). Despite of this, the inclusion of this additional channel for DM decay would make the constraint more severe for the region of  $m_{A'} < m_{\chi}$ . In the right panel of figure 7 we use gray color lines to emphasize that the DM mass region of  $m_{\chi} > m_{A'}$  gets more constrained.

# 5 Conclusions

The fermionic DM absorption by nucleus or electron targets provides a distinctive signal to search for sub-GeV DM. We consider a Dirac fermion DM charged under a dark gauge group  $\mathrm{U}(1)^\prime$  and the magnetic dipole operator. The DM field mixes with right-handed neutrino and interacts with the ordinary electromagnetic current via the kinetic mixing term of gauge fields. As a result, the incoming DM is absorbed and converted into neutrino in final state through the dipole-charge interaction.

For the DM absorption by nucleus, the recoil energy spectrum exhibit a peak at  $m_{\chi}^{2} / 2m_{N}$  for each target isotope. XENON1T can probe the DM mass above  $27\mathrm{MeV}$  and the projected constraint on the inelastic DM-nucleon cross section becomes  $10^{-49}\mathrm{cm}^2$ . CRESSTIII with lower energy threshold would be sensitive to the DM mass around  $2\mathrm{MeV}$ . We also check that the contribution from the nuclear magnetic dipole is negligible for  $^{131}\mathrm{Xe}$  target.

However, the peak-like signature would be difficult to be detected due to the limited energy resolution of detectors. Moreover, the DM lifetime constraint becomes quite severe for the sensitive region of the inelastic DM-nucleus scattering. These issues motivate us to explore lighter DM through the scattering between DM and bound electrons.

The absorption of DM by bound electron target induces ionization signal and is sensitive to sub-MeV DM mass below  $100\mathrm{keV}$ . The involvement of the ionization form factor spreads out the localized recoil energy. Lighter DM favors softer spectrum and lighter dark photon enhances the ionization rate. For extremely small dark photon mass, the limit of coupling  $e^2 U^2$  can reach as small as  $10^{-49}\mathrm{cm}^2$ .

Note added. During the completion of this work, a study [49] appeared and investigated the fermionic absorption by electron in the framework of effective field theories.

# Acknowledgments

TL would like to thank Wei Chao for useful discussion. TL is supported by the National Natural Science Foundation of China (Grant No. 11975129, 12035008) and “the Fundamental Research Funds for the Central Universities”, Nankai University (Grant No. 63196013). JL is supported by the National Natural Science Foundation of China (Grant No. 11905299), Guangdong Basic and Applied Basic Research Foundation (Grant No. 2020A1515011479), the Fundamental Research Funds for the Central Universities, and the Sun Yat-Sen University Science Foundation.

# A Nuclear magnetic dipole form factor  $F_{D}(q)$

The nuclear magnetic dipole form factor arises from the following matrix element which includes the spin-dependent interactions for  $\chi - N$  scattering [40]

$$
\mathcal {M} = C \langle N | a _ {p} \boldsymbol {S} _ {p} + a _ {n} \boldsymbol {S} _ {n} | N \rangle \cdot \boldsymbol {s} _ {\chi}, \tag {A.1}
$$

where  $C$  is the normalization constant,  $\pmb{S}_{n,p}$  are the total nuclear spin operators for neutron  $n$  and proton  $p$ ,  $\pmb{s}_{\chi}$  is the spin operator for DM, and  $a_{n,p}$  are the coupling constants for the interactions between DM and nucleon. In general, the nuclear magnetic moment can be written as [50]

$$
\mu_ {N} = \left\langle N \mid g _ {n} ^ {s} \boldsymbol {S} _ {n} + g _ {n} ^ {l} \boldsymbol {L} _ {n} + g _ {p} ^ {s} \boldsymbol {S} _ {p} + g _ {p} ^ {l} \boldsymbol {L} _ {p} \mid N \right\rangle , \tag {A.2}
$$

where  $L_{n,p}$  are the orbital angular momentum operators,  $g_{n,p}^{l,s}$  are the factors weighting the contributions from different angular momentum operators. For the standard free particles, the  $g$  factors are  $g_{n}^{s} = -3.826$ ,  $g_{n}^{l} = 0$ ,  $g_{p}^{s} = 5.586$ ,  $g_{p}^{l} = 1$  (in unit of nuclear magneton  $\mu_N$ ) [51]. Here we use the effective  $g$  factors from the linear least-squares (LLS) fit, i.e.,  $g_{n}^{s} = -3.370$ ,  $g_{p}^{s} = 3.189$ ,  $g_{n}^{l} = 0.01903$ ,  $g_{p}^{l} = 1.119$ . For  ${}^{131}\mathrm{Xe}$ , after taking the spin and orbital angular momentum matrix elements of proton and neutron from ref. [51] and plugging them into eq. (A.2), one can obtain that the ratio of the contributions from

orbital and spin angular moments is approximately  $0.4:0.6$  (normalized to 1). According to ref. [8], the nuclear magnetic dipole moment form factor is

$$
F _ {D} ^ {2} (q) = \left(0. 4 \frac {L (q)}{L (0)} + 0. 6 \sqrt {\frac {S (q)}{S (0)}}\right) ^ {2}, \tag {A.3}
$$

where the structure function  $L(q)$  and  $S(q)$  can be obtained in terms of the spin-independent form factor  $F_{\mathrm{mass}}(q) = L(q) / L(0)$  and the spin-dependent form factor  $F_{\mathrm{spin}}(q)^2 = S(q) / S(0)$ .

To get a complete analytical form of  $F_{D}(q)$ , we need to determine the form factors  $F_{\mathrm{mass}}(q)$  and  $F_{\mathrm{spin}}(q)$ . Generally speaking, they are the encapsulation of the matrix element of the nucleon level operators between the nuclear states  $|N\rangle$ . The form factor  $F_{\mathrm{mass}}(q)$  is defined as

$$
F _ {\mathrm {m a s s}} (q) \equiv \int d ^ {3} \pmb {x} e ^ {- i \pmb {q} \cdot \pmb {x}} \frac {\rho_ {n} (\pmb {x})}{m _ {n}}, \tag {A.4}
$$

where  $\rho_{n}(\pmb{x})$  is the mass density of nucleons in nucleus. There are numerous proposed mass density distributions. A commonly used one is proposed by Helm [52]

$$
\rho_ {n} (r) = \rho_ {0} \left[ 1 + \exp \left(\frac {r - c}{a}\right) \right] ^ {- 1}, \tag {A.5}
$$

where  $a$  and  $c$  are the parameters obtained by using two-parameters least-squares fit. This distribution has the advantage of yielding an analytical form, that is the so-called Helm form factor

$$
F _ {\mathrm {m a s s}} (q) \rightarrow \frac {3 j _ {1} (q r _ {n})}{q r _ {n}} e ^ {- (q s) ^ {2} / 2}, \tag {A.6}
$$

where  $r_n$  has a good fit related to the atom mass number  $A$ :  $r_n \approx 1.14A^{1/3}$ , and  $s \approx 0.9$  fm. For the spin-dependent form factor, the spin structure function  $S(q)$  is the following linear superposition which includes pure isoscalar  $S_{00}$ , isovector  $S_{11}$  and interference term  $S_{01}$

$$
S (q) = a _ {0} ^ {2} S _ {0 0} (q) + a _ {1} ^ {2} S _ {1 1} (q) + a _ {0} a _ {1} S _ {0 1} (q), \tag {A.7}
$$

where  $a_0$  ( $a_1$ ) is the isoscalar (isovector) projection of  $a_n$  and  $a_p$ , and they have a fixed ratio by using EMC (European Muon Collaboration) values for proton:  $a_0 / a_1 = 0.297$  [53]. We normalize it by requiring  $S(0) = 1$ , and then one has  $a_0 = 2.775$  and  $a_1 = 9.341$ , or equivalently,  $a_p = 6.058$ ,  $a_n = -3.283$  ( $a_0 = a_p + a_n$ ,  $a_1 = a_p - a_n$ ). The components  $S_{ij}(q)$  of  $^{131}\mathrm{Xe}$  can be found in ref. [40]. Note that the atomic number of xenon ( $Z = 54$ ) is between those of cesium ( $Z = 55$ ) and iodine ( $Z = 53$ ) which are both proton-odd. For neutron-odd isotope  $^{131}\mathrm{Xe}$ , according to the suggested values in ref. [40], it follows that  $|\langle S_p\rangle| \ll |\langle S_n\rangle|$ . Thus, the dipole moment in xenon is dominated by neutron spin  $S_n$  unlike the cesium and iodine whose dipole moments are dominated by  $S_p$ .

Table 1. Binding energy and effective charge of each shell in Xenon.  

<table><tr><td>orbital</td><td>1s</td><td>2s</td><td>2p</td><td>3s</td><td>3p</td><td>3d</td><td>4s</td><td>4p</td><td>4d</td><td>5s</td><td>5p</td></tr><tr><td>|EnB| (keV)</td><td>33.3174</td><td>5.1522</td><td>4.8377</td><td>1.0932</td><td>0.9584</td><td>0.7107</td><td>0.2138</td><td>0.1635</td><td>0.0756</td><td>0.0257</td><td>0.0124</td></tr><tr><td>Zeff</td><td>49.5</td><td>38.93</td><td>37.72</td><td>26.90</td><td>25.18</td><td>21.69</td><td>15.86</td><td>13.87</td><td>9.43</td><td>6.87</td><td>4.77</td></tr></table>

# B The calculation of the radial wave-functions in the electron ionization form factor  $|f_{\mathrm{ion}}^{nl}(k', q)|^2$

Here we give a general method to numerically determine the ionization form factor for different shells and DM masses. According to the general form of eq. (4.3), we have known that  $l, l'$  and  $L$  are the angular quantum numbers relying on specific shells, and  $j_{L}(qr)$  is also a known spherical Bessel function. Thus, only the radial wave-functions  $R_{k'l'}(r)$  and  $R_{nl}(r)$  are unknown. In this section, we mainly discuss how to calculate these two functions.

# B.1 The radial wave-function  $R_{k^{\prime}l^{\prime}}(r)$

To obtain the radial wave-function  $R_{k^{\prime}l^{\prime}}(r)$  of outgoing unbound electrons, one needs to solve the radial Schrödinger equation with a central potential  $Z_{\mathrm{eff}}(r) / r$ . In order to get  $Z_{\mathrm{eff}}(r) / r$ , we take the assumption that it can be approximated as the central potential corresponding to the bound state of hydrogen-like atom. Thus, the function  $Z_{\mathrm{eff}}$  becomes a radial independent factor whose values are determined by the following table 1 from ref. [54].

$Z_{\mathrm{eff}}$ , the effective charge felt by the scattered electron, is then determined by the binding energy of different orbitals  $Z_{\mathrm{eff}}^{nl} = \sqrt{|E_B^{nl}| / 13.6\mathrm{eV}}\times n$  with  $E_B^{nl}$  being the binding energy. The general solution with positive energy continuum for radial Schödinger equation of hydrogen-like atom is given by [55, 56]

$$
\begin{array}{l} R _ {k ^ {\prime} l ^ {\prime}} (r) = \frac {(2 \pi) ^ {3 / 2}}{\sqrt {V}} (2 k ^ {\prime} r) ^ {l ^ {\prime}} \frac {\sqrt {\frac {2}{\pi}} \left| \Gamma \left(l ^ {\prime} + 1 - \frac {i Z _ {\mathrm {e f f}}}{k ^ {\prime} a _ {0}}\right) \right| e ^ {\frac {\pi Z _ {\mathrm {e f f}}}{2 k ^ {\prime} a _ {0}}}}{(2 l ^ {\prime} + 1) !} \\ \times e ^ {- i k ^ {\prime} r} _ {1} F _ {1} \left(l ^ {\prime} + 1 + \frac {i Z _ {\mathrm {e f f}}}{k ^ {\prime} a _ {0}}, 2 l ^ {\prime} + 2, 2 i k ^ {\prime} r\right), \tag {B.1} \\ \end{array}
$$

where  ${}_{1}F_{1}(a,b,z)$  is the first kind confluent hypergeometric function, and  $a_0$  denotes the Bohr radius. It should be noticed that the extra volume factor  $1 / \sqrt{V}$  can be eventually cancelled by the integral of space. It means that once the momentum of the outgoing electron  $k'$  and the orbital quantum number  $l'$  are determined, we can evaluate the wavefunction  $R_{k'l'}$  at any radii. At the same time, due to the asymptotic approximation, the wave-function value is more accurate at large radii. In figure 8 we show the numerical results of radial wave-function  $R_{k'l'}(r)$  corresponding to 1s, 2p, 3d, 4p shells, respectively.

![](images/e45ffd22996042754a3f60a1fc3cce361a3858dc1554c54672d454d495aaad43.jpg)  
(a) Orbital 1s

![](images/34cf10655e34c2d746cfc263a52f3476cc835977efcf2e675e11c80dfa26935a.jpg)  
(b) Orbital 2p

![](images/318ea7f7f960ac0cabf1fa57cb5443e10c0d93e6834ad7fc78ad9c66fa159bf8.jpg)  
(c) Orbital 3d

![](images/1ed8b0e299a93d2aa70b77356e1e323363bb23201ed0c1ca7a0228a4bb6353ba.jpg)  
Figure 8. The radial wave-function  $R_{k^{\prime}l^{\prime}}(r)$  of the outgoing electron with recoil energy  $E_{R} = 50\mathrm{keV}$  for illustration.  
(d) Orbital 4p

# B.2 The radial wave-function  $R_{nl}(r)$

The orbital wave-function  $R_{nl}$  on the  $(n,l)$  shell can be given as a linear combination of the Slater-type orbitals via the Roothaan-Hartree-Fock (RHF) approximation [54]. In the RHF method, the atomic orbitals of xenon can be obtained as a finite superposition of analytical radial function

$$
R _ {n l} (r) = a _ {0} ^ {- 3 / 2} \sum_ {j} C _ {j l n} \frac {\left(2 Z _ {j l}\right) ^ {n _ {j l} ^ {\prime} + 1 / 2}}{\sqrt {\left(2 n _ {j l} ^ {\prime}\right) !}} \times \left(\frac {r}{a _ {0}}\right) ^ {n _ {j l} ^ {\prime} - 1} \exp \left(- Z _ {j l} \frac {r}{a _ {0}}\right), \tag {B.2}
$$

where the coefficients  $C_{jln}$ ,  $Z_{jl}$  and  $n_{jl}'$  are all obtained from ref. [54]. Similarly, in figure 9, we show the results of radial wave-function  $R_{nl}(r)$  for 1s, 2p, 3d, 4p shells, respectively.

![](images/8649d94ed31b3379e2946042118fae3eb373f1cc54089955997d54d05684c989.jpg)  
(a) Orbital 1s

![](images/78c1dc105b08493e622c24e38b58f33f978cda05ab78ad7d7333fc31d72f5bbe.jpg)  
(b) Orbital 2p

![](images/13ad1f37ac6faa90e5670fef53ae5bee238ea33db08ec051a4e715374f3a0067.jpg)  
(c) Orbital 3d

![](images/97744934a62186e620b49a90b38173bbcc42ec14c9dc595b76a3295bc4d00e59.jpg)  
Figure 9. The radial wave-function  $R_{nl}(r)$  of the bound electron outside the xenon nucleus.  
(d) Orbital 4p

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] D. Tucker-Smith and N. Weiner, Inelastic dark matter, Phys. Rev. D 64 (2001) 043502 [hep-ph/0101138] [INSPIRE].  
[2] DAMA collaboration, Search for WIMP annual modulation signature: Results from DAMA/NaI-3 and DAMA/NaI-4 and the global combined analysis, Phys. Lett. B 480 (2000) 23 [INSPIRE].  
[3] DAMA and LIBRA collaborations, New results from DAMA/LIBRA, Eur. Phys. J. C 67 (2010) 39 [arXiv:1002.1028] [INSPIRE].  
[4] M. Pospelov and T. ter Veldhuis, Direct and indirect limits on the electromagnetic form-factors of WIMPs, Phys. Lett. B 480 (2000) 181 [hep-ph/0003010] [INSPIRE].  
[5] K. Sigurdson, M. Doran, A. Kurylov, R.R. Caldwell and M. Kamionkowski, Dark-matter electric and magnetic dipole moments, Phys. Rev. D 70 (2004) 083501 [Erratum ibid. 73 (2006) 089903] [astro-ph/0406355] [INSPIRE].  
[6] S. Gardner, Shedding Light on Dark Matter: A Faraday Rotation Experiment to Limit a Dark Magnetic Moment, Phys. Rev. D 79 (2009) 055007 [arXiv:0811.0967] [INSPIRE].

[7] E. Masso, S. Mohanty and S. Rao, *Dipolar Dark Matter*, Phys. Rev. D **80** (2009) 036009 [arXiv:0906.1979] [INSPIRE].  
[8] S. Chang, N. Weiner and I. Yavin, Magnetic Inelastic Dark Matter, Phys. Rev. D 82 (2010) 125011 [arXiv:1007.4200] [INSPIRE].  
[9] V. Barger, W.-Y. Keung and D. Marfatia, Electromagnetic properties of dark matter: Dipole moments and charge form factor, Phys. Lett. B 696 (2011) 74 [arXiv:1007.4345] [INSPIRE].  
[10] J.A. Dror, G. Elor and R. McGehee, Directly Detecting Signals from Absorption of Fermionic Dark Matter, Phys. Rev. Lett. 124 (2020) 18 [arXiv:1905.12635] [INSPIRE].  
[11] J.A. Dror, G. Elor and R. Mcgehee, Absorption of Fermionic Dark Matter by Nuclear Targets, JHEP 02 (2020) 134 [arXiv:1908.10861] [INSPIRE].  
[12] J.A. Dror, G. Elor, R. McGehee and T.-T. Yu, Absorption of sub-MeV fermionic dark matter by electron targets, Phys. Rev. D 103 (2021) 035001 [arXiv:2011.01940] [INSPIRE].  
[13] S.-F. Ge, P. Pasquini and J. Sheng, Solar neutrino scattering with electron into massive sterile neutrino, Phys. Lett. B 810 (2020) 135787 [arXiv:2006.16069] [INSPIRE].  
[14] I.M. Shoemaker, Y.-D. Tsai and J. Wyenberg, Active-to-sterile neutrino dipole portal and the XENON1T excess, Phys. Rev. D 104 (2021) 115026 [arXiv:2007.05513] [INSPIRE].  
[15] S. Shakeri, F. Hajkarim and S.-S. Xue, Shedding New Light on Sterile Neutrinos from XENON1T Experiment, JHEP 12 (2020) 194 [arXiv:2008.05029] [INSPIRE].  
[16] N. Hurtado, H. Mir, I.M. Shoemaker, E. Welch and J. Wyenberg, Dark Matter-Neutrino Interconversion at COHERENT, Direct Detection, and the Early Universe, Phys. Rev. D 102 (2020) 015006 [arXiv:2005.13384] [INSPIRE].  
[17] Z. Chen, T. Li and J. Liao, Constraints on general neutrino interactions with exotic fermion from neutrino-electron scattering experiments, JHEP 05 (2021) 131 [arXiv:2102.09784] [INSPIRE].  
[18] XENON collaboration, Excess electronic recoil events in XENON1T, Phys. Rev. D 102 (2020) 072004 [arXiv:2006.09721] [INSPIRE].  
[19] O.G. Miranda, D.K. Papoulias, M. Tórtola and J.W.F. Valle, XENON1T signal from transition neutrino magnetic moments, Phys. Lett. B 808 (2020) 135685 [arXiv:2007.01765] [INSPIRE].  
[20] K.S. Babu, S. Jana and M. Lindner, Large Neutrino Magnetic Moments in the Light of Recent Experiments, JHEP 10 (2020) 040 [arXiv:2007.04291] [INSPIRE].  
[21] V. Brdar, A. Greljo, J. Kopp and T. Opferkuch, The Neutrino Magnetic Moment Portal: Cosmology, Astrophysics, and Direct Detection, JCAP 01 (2021) 039 [arXiv:2007.15563] [INSPIRE].  
[22] D. Aristizabal Sierra, R. Branada, O.G. Miranda and G. Sanchez Garcia, Sensitivity of direct detection experiments to neutrino magnetic dipole moments, JHEP 12 (2020) 178 [arXiv:2008.05080] [INSPIRE].  
[23] M. Fabbrichesi, E. Gabrielli and G. Lanfranchi, The Dark Photon, arXiv:2005.01515 [INSPIRE].  
[24] PLANCK collaboration, Planck 2015 results. XIII. Cosmological parameters, Astron. Astrophys. 594 (2016) A13 [arXiv:1502.01589] [INSPIRE].

[25] LUX collaboration, Results from a search for dark matter in the complete LUX exposure, Phys. Rev. Lett. 118 (2017) 021303 [arXiv:1608.07648] [INSPIRE].  
[26] PANDAX-II collaboration, Dark Matter Results From 54-Ton-Day Exposure of PandaX-II Experiment, Phys. Rev. Lett. 119 (2017) 181302 [arXiv:1708.06917] [INSPIRE].  
[27] XENON collaboration, Dark Matter Search Results from a One Ton-Year Exposure of XENON1T, Phys. Rev. Lett. 121 (2018) 111302 [arXiv:1805.12562] [INSPIRE].  
[28] CRESST collaboration, Results on light dark matter particles with a low-threshold CRESST-II detector, Eur. Phys. J. C 76 (2016) 25 [arXiv:1509.01515] [INSPIRE].  
[29] CRESST collaboration, First results on low-mass dark matter from the CRESST-III experiment, J. Phys. Conf. Ser. 1342 (2020) 012076 [arXiv:1711.07692] [INSPIRE].  
[30] DARKSIDE collaboration, First Results from the DarkSide-50 Dark Matter Experiment at Laboratori Nazionali del Gran Sasso, Phys. Lett. B 743 (2015) 456 [arXiv:1410.0653] [INSPIRE].  
[31] DARKSIDE collaboration, Low-Mass Dark Matter Search with the DarkSide-50 Experiment, Phys. Rev. Lett. 121 (2018) 081307 [arXiv:1802.06994] [INSPIRE].  
[32] G. Jungman, M. Kamionkowski and K. Griest, Supersymmetric dark matter, Phys. Rept. 267 (1996) 195 [hep-ph/9506380] [INSPIRE].  
[33] G. Bélanger, F. Boudjema, A. Pukhov and A. Semenov, Dark matter direct detection rate in a generic model with MicrOMEGAs 2.2, Comput. Phys. Commun. 180 (2009) 747 [arXiv:0803.2360] [INSPIRE].  
[34] XENON collaboration, Energy resolution and linearity of XENON1T in the MeV energy range, Eur. Phys. J. C 80 (2020) 785 [arXiv:2003.03825] [INSPIRE].  
[35] R. Budnik, O. Chesnovsky, O. Slone and T. Volansky, Direct Detection of Light Dark Matter and Solar Neutrinos via Color Center Production in Crystals, Phys. Lett. B 782 (2018) 242 [arXiv:1705.03016] [INSPIRE].  
[36] M. Szydagis et al., Demonstration of neutron radiation-induced nucleation of supercooled water, arXiv:1807.09253 [INSPIRE].  
[37] R. Essig et al., Snowmass2021 Cosmic Frontier: The landscape of low-threshold dark matter direct detection in the next decade, in 2022 Snowmass Summer Study, Seattle, U.S.A. (2022) [arXiv:2203.08297] [INSPIRE].  
[38] T. Bringmann and M. Pospelov, Novel direct detection constraints on light dark matter, Phys. Rev. Lett. 122 (2019) 171801 [arXiv:1810.10543] [INSPIRE].  
[39] M. Ibe, W. Nakano, Y. Shoji and K. Suzuki, Migdal Effect in Dark Matter Direct Detection Experiments, JHEP 03 (2018) 194 [arXiv:1707.07258] [INSPIRE].  
[40] M.T. Ressell and D.J. Dean, Spin dependent neutralino-nucleus scattering for  $A$  approximately 127 nuclei, Phys. Rev. C 56 (1997) 535 [hep-ph/9702290] [INSPIRE].  
[41] R. Essig, A. Manalaysay, J. Mardon, P. Sorensen and T. Volansky, First Direct Detection Limits on sub-GeV Dark Matter from XENON10, Phys. Rev. Lett. 109 (2012) 021301 [arXiv:1206.2644] [INSPIRE].  
[42] R. Essig, T. Volansky and T.-T. Yu, New Constraints and Prospects for sub-GeV Dark Matter Scattering off Electrons in Xenon, Phys. Rev. D 96 (2017) 043017 [arXiv:1703.00910] [INSPIRE].

[43] G.B. Arfken, H.J. Weber and F.E. Harris, Chapter 16 — angular momentum, in Mathematical Methods for Physicists, seventh edition, G.B. Arfken, H.J. Weber and F.E. Harris eds., Academic Press, Boston, U.S.A. (2013), pg. 773.  
[44] R. Essig, J. Mardon and T. Volansky, Direct Detection of Sub-GeV Dark Matter, Phys. Rev. D 85 (2012) 076007 [arXiv:1108.5383] [INSPIRE].  
[45] S.K. Lee, M. Lisanti, S. Mishra-Sharma and B.R. Safdi, Modulation Effects in Dark Matter-Electron Scattering Experiments, Phys. Rev. D 92 (2015) 083517 [arXiv:1508.07361] [INSPIRE].  
[46] J. Kopp, V. Niro, T. Schwetz and J. Zupan, DAMA/LIBRA and leptonically interacting Dark Matter, Phys. Rev. D 80 (2009) 083502 [arXiv:0907.3159] [INSPIRE].  
[47] Q.-H. Cao, R. Ding and Q.-F. Xiang, Searching for sub-MeV boosted dark matter from xenon electron direct detection, Chin. Phys. C 45 (2021) 045002 [arXiv:2006.12767] [INSPIRE].  
[48] R. Catena, T. Emken, N.A. Spaldin and W. Tarantino, Atomic responses to general dark matter-electron interactions, Phys. Rev. Res. 2 (2020) 033195 [arXiv:1912.08204] [INSPIRE].  
[49] S.-F. Ge, X.-G. He, X.-D. Ma and J. Sheng, Revisiting the Fermionic Dark Matter Absorption on Electron Target, arXiv:2201.11497 [INSPIRE].  
[50] W.Y.P. Hwang, 2008 International Symposium on cosmology and particle astrophysics, Int. J. Mod. Phys. Conf. Ser. 01 (2011) 1 [INSPIRE].  
[51] P. Toivanen, M. Kortelainen, J. Suhonen and J. Toivanen, Large-scale shell-model calculations of elastic and inelastic scattering rates of lightest supersymmetric particles (LSP) on  $^{127}\mathrm{I}$ ,  $^{129}\mathrm{Xe}$ ,  $^{131}\mathrm{Xe}$ , and  $^{133}\mathrm{Cs}$  nuclei, Phys. Rev. C 79 (2009) 044302 [INSPIRE].  
[52] R.H. Helm, Inelastic and Elastic Scattering of 187-Mev Electrons from Selected Even-Even Nuclei, Phys. Rev. 104 (1956) 1466 [INSPIRE].  
[53] M.T. Ressell, M.B. Aufderheide, S.D. Bloom, K. Griest, G.J. Mathews and D.A. Resler, Nuclear shell model calculations of neutralino-nucleus cross-sections for  $^{29}\mathrm{Si}$  and  $^{73}\mathrm{Ge}$ , Phys. Rev. D 48 (1993) 5519 [hep-ph/9307228] [INSPIRE].  
[54] C. Bunge, J. Barrientos and A. Bunge, Roothaan-hartree-fock ground-state atomic wave functions: Slater-type orbital expansions and expectation values for  $z = 2 - 54$ , At. Data Nucl. Data Tables 53 (1993) 113.  
[55] DARKSIDE collaboration, Constraints on Sub-GeV Dark-Matter-Electron Scattering from the DarkSide-50 Experiment, Phys. Rev. Lett. 121 (2018) 111303 [arXiv:1802.06998] [INSPIRE].  
[56] H.A. Bethe and E.E. Salpeter, Quantum Mechanics of One- and Two-Electron Atoms (1957), Springer, Berlin, Germany (1957) [INSPIRE].  
[57] PARTICLE DATA GROUP collaboration, Review of Particle Physics, PTEP 2020 (2020) 083C01 [INSPIRE].