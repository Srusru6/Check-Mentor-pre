# Prospects of detecting cosmic ray up-scattered dark matter with DUNE

Richard Diurba  $^{\text{品}}$  and Helena Kolešová  $^{\text{品}}$

<sup>a</sup> Albert Einstein Center, Laboratory for High Energy Physics, University of Bern, Sidlerstrasse 5, CH-3012 Bern, Switzerland  
$^{b}$ Department of Mathematics and Physics, University of Stavanger, 4036 Stavanger, Norway

E-mail: richard.diurba@unibe.ch, helena.kolesova@uis.no

ABSTRACT: Detection of sub-GeV dark matter (DM) particles in direct detection experiments is inherently difficult, as their low kinetic energies in the galactic halo are insufficient to produce observable recoils of the heavy nuclei in the detectors. On the other hand, whenever DM particles interact with nucleons, they can be accelerated by scattering with galactic cosmic rays. These cosmic-ray-boosted DM particles can then interact not only through coherent elastic scattering with nuclei, but also through scattering with individual nucleons in the detectors and produce outgoing particles at MeV to GeV kinetic energies. The resulting signal spectrum overlaps with the detection capabilities of modern neutrino experiments. One future experiment is the Deep Underground Neutrino Experiment (DUNE) at the Sanford Underground Research Facility. Our study shows that DUNE has a unique ability to search for cosmic-ray boosted DM with sensitivity comparable to dedicated direct detection experiments in the case of spin-independent interactions. Importantly, DUNE's sensitivity reaches similar values of DM-nucleon cross sections also in the case of spin-dependent interactions, offering a key advantage over traditional direct detection experiments.

KEYWORDS: Particle Nature of Dark Matter, Cosmic Rays

ARXIV EPRINT: 2504.16996

# Contents

# 1 Introduction 1

# 2 Cosmic-ray up-scattered dark matter 3

2.1 Cosmic-ray up-scattering 3  
2.2 Detection methodology 5

# 3 Dark matter interactions 5

3.1 Model for dark matter-quark interaction 5  
3.2 Scattering with nucleons 6  
3.3 Scattering with nuclei 9

# 4 Results 11

4.1 CRDM flux 12  
4.2 Expected number of events in DUNE 12  
4.3Constraints on dark matter parameter space 14  
4.4 Discussion on other datasets 16

# 5 Conclusions and outlook 19

# A Kinematics of dark matter scattering with nucleons and nuclei 20

# B Attenuation of the CRDM flux 21

# C Atmospheric neutrino background 22

# D Generating samples of boosted dark matter interactions in GENIE 23

# 1 Introduction

The nature of dark matter (DM) in our Universe remains one of the most profound mysteries in modern physics. New particles beyond the Standard Model (SM) are often proposed to explain the existence of DM, and various strategies have been developed to probe their nature [1]. In this work, we focus on the so-called direct detection of dark matter, with rare interactions between DM particles and atomic nuclei in terrestrial detectors observed as the Earth moves through the DM halo surrounding our galaxy [2]. Most attention in direct detection experiments goes towards the example of spin-independent (SI) interactions with nuclei, which occurs, e.g., through DM coupling to SM quarks via a scalar or vector mediator. The SI interactions of DM with nucleons within a nucleus are coherently summed, hence, the DM-nucleus cross section scales with the square of the atomic number  $A^2$ . Consequently, experiments utilizing large-  $A$  xenon nuclei, such as LZ [3] or XENONnT [4], have achieved remarkable sensitivity to DM-nucleon cross sections as low as  $\sigma_p^{\mathrm{SI}} \sim 10^{-47} \mathrm{cm}^2$  for DM masses around 30 GeV. However, kinematic constraints limit the sensitivity of these experiments to

low-mass DM, as particles from the galactic halo have velocities constrained by the galactic escape velocity of  $\sim 540\mathrm{km / s}$  and lack the kinetic energy needed to produce a detectable recoil on a heavy nucleus. As a result, extensive efforts are underway to enhance experimental sensitivity to hadrophylic halo dark matter in the sub-GeV mass range. New detection strategies with lower detection threshold are being developed [5], or alternative processes related to DM-nucleus scattering with more favorable kinematics are being considered, such as the production of Migdal electrons [6-8] or bremsstrahlung photons [9].

Another strategy is to explore scenarios where DM is accelerated by specific mechanisms, allowing sub-GeV DM to acquire enough kinetic energy to produce a detectable nuclear recoil in existing direct detection experiments or to produce signatures in neutrino experiments. A flux of accelerated DM coming to Earth may arise, for example, when a heavier dark sector component annihilates or decays into a lighter one [10–12], when DM undergoes scattering with particles in the Sun [13–15], or with energetic galactic cosmic-ray (CR) nuclei [16–18]. In this work, we concentrate on the last option of cosmic-ray up-scattered dark matter (CRDM). Although acceleration by CR electrons and subsequent detection via interaction with electrons in different detectors was considered in some studies [19–27], we focus on the case of hadrophylic DM studied in the context of CRDM by refs. [28–53]. While CRDM constraints from direct detection experiments are based on the coherent elastic scattering of DM with nuclei, it was shown in [34, 35, 40, 41] that neutrino experiments may detect the scattering of DM with individual nucleons, referred to as quasi-elastic (QE) scattering in this text. Furthermore, scattering with individual partons, so-called deep inelastic scattering (DIS), was shown to be crucial for possible CRDM detection in IceCube [32, 54, 55].<sup>1</sup>

From the experiments considered in refs. [32, 35, 41, 55], the Deep Underground Neutrino Experiment (DUNE) has the highest sensitivity to DM with mass in the MeV-GeV range that is most interesting for us, as lower DM masses are typically strongly constrained by the Big Bang Nucleosynthesis (BBN) [57]. With four planned modules with 17.5 kilotons of liquid argon [58], DUNE can provide the exposure and detector capabilities to search for DM boosted by different mechanisms [59–62], including CRDM. This work focuses on this experiment and improves upon existing works in several aspects. First, we employ more precise modeling of the interactions relevant for DM detection. In particular, ref. [35] modeled the QE process as scattering off free nucleons and neglected the DIS contribution when determining the sensitivity region of the DUNE detector. Our work employs the boosted dark matter module [63] of the GENIE interaction event generator [64–66] to properly model the complicated nuclear effects that influence the QE scattering and add DIS. Second, this paper studies the effect of the atmospheric neutrino background on the DUNE sensitivity, which was neglected in [35]. Finally, the inelastic scattering is newly considered for the DM up-scattering by CR. The effect of DIS in CR-DM scattering was discussed in [32]; however, they focused on the secondary photons produced in such a process. The enhancement of DM up-scattering due to inelastic scattering was discussed in [49, 52] focusing on the implications for direct detection experiments, where the bounds are not enormously extended since these experiments predominantly detect DM with lower kinetic energies. However, the sensitivity

of neutrino experiments can be significantly enhanced by inclusion of the inelastic CR-DM scattering, as we show in the present work.

The original work [17] attempted to present the CRDM constraints in a model independent way, assuming the simplified "constant" cross section for DM scattering with nucleons, thereby, neglecting the dependence on the transferred momentum  $Q^2$ . On the other hand, follow-up works like [28-31, 35, 41, 42, 47-50, 52] showed that the  $Q^2$  dependence might alter the CRDM constraints for different DM scenarios. Moreover, in order to describe the DIS process, a specific model for DM-quark interactions must be chosen. This work is based on DM-quark interactions mediated by a new massive gauge boson  $Z'$  as implemented in the GENIE event generator [63]. We consider the vector couplings that lead to SI scattering with nuclei mentioned above and axial-vector couplings that lead to spin-dependent (SD) interactions. For SD scattering, the interactions with DM are stronger for nuclei with convenient spin structures, like the fluorine isotope  $^{19}\mathrm{F}$ , and there is no  $A^2$  enhancement for nuclei with large atomic numbers. Therefore, the direct detection bounds on the DM-nucleon cross section based on halo dark matter are relatively weaker for SD scattering than for SI scattering, at only  $\sigma_p^{\mathrm{SD}} \sim 10^{-41}\mathrm{cm}^2$  for  $\mathcal{O}(10\mathrm{GeV})$  DM masses [67]. In contrast, we show that the CRDM constraints for SI and SD cases remain relatively similar. In fact, CRDM constraints are expected to exist for any model where DM couples to nucleons since both the boosting and detection mechanisms rely solely on the DM-nucleon interaction.

This work will first introduce the mechanism of DM up-scattering by interactions with CR (section 2.1) and discuss the detection of CRDM particles (section 2.2). Example DM scenarios are described in section 3, where the resulting interactions with nucleons and nuclei are also discussed. The corresponding sensitivities for DUNE are then presented and compared with complementary constraints in section 4. We conclude in section 5 and discuss several technical aspects in the appendices.

# 2 Cosmic-ray up-scattered dark matter

In this section, we will explain the mechanism of DM acceleration by galactic CR and the calculation of the possible event rate in the DUNE experiment. The description of the attenuation of the CRDM flux is postponed to appendix B.

# 2.1 Cosmic-ray up-scattering

Let us consider galactic CR nuclei  $A$  with kinetic energies  $T_{A}$  and differential fluxes  $d\Phi_A / dT_A(x)$  that vary by position. These energetic particles may scatter with halo DM with density  $\rho_{\chi}(x)$ , giving rise to a flux of up-scattered DM particles with kinetic energies of  $T_{\chi}$  [17]:<sup>2</sup>

$$
\begin{array}{l} \frac {d \Phi_ {\chi}}{d T _ {\chi}} = \int \frac {d \Omega}{4 \pi} \int_ {\mathrm {l . o . s .}} d \ell \frac {\rho_ {\chi}}{m _ {\chi}} \sum_ {A} \int_ {T _ {A} ^ {\mathrm {m i n}}} ^ {\infty} d T _ {A} \frac {d \sigma_ {\chi A}}{d T _ {\chi}} \frac {d \Phi_ {A}}{d T _ {A}} (2.1) \\ \equiv D _ {\mathrm {e f f}} \frac {\rho_ {\chi} ^ {\mathrm {l o c a l}}}{m _ {\chi}} \sum_ {A} \int_ {T _ {A} ^ {\mathrm {m i n}}} ^ {\infty} d T _ {A} \frac {d \sigma_ {\chi A}}{d T _ {\chi}} \frac {d \Phi_ {A} ^ {\mathrm {L I S}}}{d T _ {A}}. (2.2) \\ \end{array}
$$

On the second line, the dependencies of the DM density and CR flux on position are captured by the effective distance  $D_{\mathrm{eff}}$ . Therefore, only the local interstellar CR flux,  $d\Phi_A^{\mathrm{LIS}} / dT_A$  [69, 70] and the local DM density,  $\rho_{\chi}^{\mathrm{local}} = 0.3\mathrm{GeV} / \mathrm{cm}^3$ , appear in the final formula. We assume  $D_{\mathrm{eff}} = 10\mathrm{kpc}$  in this work, as motivated by the detailed analysis presented in ref. [68].

Furthermore,  $d\sigma_{\chi A} / dT_{\chi}$  in eq. (2.1) is the differential cross section for the scattering of CR nuclei with DM at rest where  $T_{\chi}$  is the kinetic energy of the recoiled DM particle. We improve existing results by adding the effect of inelastic CR-DM scattering that may play an important role in scenarios where elastic scattering is suppressed. As mentioned above, we extract the cross sections for inelastic DM-nucleus scattering from the numerical code GENIE [63], and these are calculated in the nucleus rest frame. Conveniently, the Lorentz-invariant momentum transfer  $Q^2$  is related to  $T_{\chi}$  by

$$
Q ^ {2} = 2 m _ {\chi} T _ {\chi}, \tag {2.3}
$$

leading to  $d\sigma_{\chi A} / dT_{\chi} = 2m_{\chi}d\sigma_{\chi A} / dQ^{2}$ . The latter cross section is invariant under the boost between the DM and nucleus rest frames, allowing the GENIE results to be directly used. Let us note that two kinematic variables are needed to describe inelastic scattering, hence,  $d\sigma_{\chi A} / dQ^{2}$  in fact refers to an integral, such as:

$$
\frac {d \sigma_ {\chi A}}{d Q ^ {2}} \equiv \int_ {X} \frac {d ^ {2} \sigma_ {\chi A}}{d Q ^ {2} d X} d X \tag {2.4}
$$

where  $X$  refers to some other kinematic variable (see examples in appendix A). When inferring  $d\sigma_{\chi A} / dQ^2$  from GENIE, the DM kinetic energy in the nucleus rest frame  $\tilde{T}_{\chi,\mathrm{in}}$  is needed. The following relation between  $\tilde{T}_{\chi,\mathrm{in}}$  and the kinetic energy of the CR nucleus  $T_A$  in the DM rest frame is then used:

$$
\tilde {T} _ {\chi , \text {i n}} = \frac {m _ {\chi}}{m _ {A}} T _ {A}. \tag {2.5}
$$

Finally, the lower bound for the integration over the CR kinetic energies in eq. (2.1),  $T_{A}^{\mathrm{min}}$ , arises because a given final DM kinetic energy  $T_{\chi}$  can be obtained only for sufficiently large initial CR kinetic energy. Different processes considered for CR-DM scattering involve different kinematics (see appendix A). However, it turns out that  $T_{A}^{\mathrm{min}}$  attains the smallest value for the case of coherent DM-nucleus scattering, where

$$
T _ {A} ^ {\mathrm {m i n}} = \frac {T _ {\chi}}{2} - m _ {A} + \sqrt {\left(\frac {T _ {\chi}}{2} - m _ {A}\right) ^ {2} + \frac {(m _ {\chi} + m _ {A}) ^ {2} T _ {\chi}}{2 m _ {\chi}}}. (2. 6)
$$

In practice, we evaluate the CRDM flux using the 6.4 version of the DarkSUSY code [71-73]. We benefit from the fact that user modification can be easily implemented and we complement the public version of DarkSUSY by including inelastic CR-DM scattering. $^{3}$

The CRDM flux (2.2) is expected to reach the top of the Earth's atmosphere. Still, DM with relatively strong interactions may have part of the flux reduced by interactions with the Earth's atmosphere or crust. To model such flux attenuation in a fully reliable way, dedicated Monte Carlo simulations are needed [76] and performing these is beyond the scope of this work. We, therefore, restrict our signal region to DM particles that come "from above", more precisely, from zenith angles  $\theta_z$  satisfying  $\cos \theta_z \geq 0.1$ . We checked that when this cut is applied, the number of events in DUNE should not be affected by the CRDM flux attenuation for the smallest cross sections that DUNE is capable to probe. Consequently, the main results of our paper are unaffected by the stopping of CRDM particles. We still studied this effect in a simplified way to obtain a rough estimate of the upper bound of the DUNE sensitivity region, as described in appendix B.

# 2.2 Detection methodology

The CRDM flux coming to the Earth's atmosphere (2.2) is assumed to be roughly isotropic in this work. The attenuation of this flux depends on the thickness of the soil that must be penetrated to reach the detector, that is, on the direction of the incoming DM particle. The CRDM flux at the DUNE location  $\Phi_{\mathrm{DUNE}}$  is, therefore, anisotropic and when calculating the possible DM event rate in DUNE, integration over the zenith angle is performed:

$$
R _ {\chi} = N _ {\mathrm {A r}} \int_ {T _ {\chi}} d T _ {\chi} \sigma_ {\chi \mathrm {A r}} ^ {\mathrm {e f f}} (T _ {\chi}) \int_ {0. 1} ^ {1} d \cos \theta_ {z} \frac {d \Phi_ {\mathrm {D U N E}}}{d T _ {\chi} d \cos \theta_ {z}}. \tag {2.7}
$$

Here  $N_{\mathrm{Ar}} = 40$  kiloton/mAr is the number of argon nuclei in the DUNE detector, with  $m_{\mathrm{Ar}} = 39.95 \times \mathrm{AMU}$  (atomic mass unit). Further,  $\sigma_{\mathrm{Ar}\chi}^{\mathrm{eff}}$  is the effective total cross section for scattering of a DM particle with kinetic energy  $T_{\chi}$  off an argon nucleus, taking into account the DUNE detection thresholds from [77] (see appendix D for details regarding the detection thresholds).

The most important background relevant to the scattering of energetic DM particles in DUNE is from neutral-current interactions of atmospheric neutrinos. We estimate the number of background atmospheric neutrino events in appendix C. We arrive at a threshold number of DM events at  $N_{\chi}^{\mathrm{thr}} = 196.7$ , needed to observe DM at the  $2\sigma$  level. Only statistical errors are considered for the number of background neutrino events that enter into our estimate of  $N_{\chi}^{\mathrm{thr}}$ .

# 3 Dark matter interactions

# 3.1 Model for dark matter-quark interaction

A specific model has to be chosen already at the quark level to describe energetic DM interactions. Utilizing the GENIE module for boosted DM [63], we present an example scenario with a massive  $\mathrm{U}(1)_D$  gauge boson  $Z^{\prime}$  assumed. It couples to a DM fermion  $\chi$  via

$$
\mathcal {L} _ {\chi , \text {i n t}} = g _ {Z ^ {\prime}} Z _ {\mu} ^ {\prime} \bar {\chi} \gamma^ {\mu} \left(Q _ {\chi} ^ {L} P _ {L} + Q _ {\chi} ^ {R} P _ {R}\right) \chi . \tag {3.1}
$$

The new mediator also interacts with SM fermions as:

$$
\mathcal {L} _ {f, \text {i n t}} = g _ {Z ^ {\prime}} Z _ {\mu} ^ {\prime} \bar {\psi} _ {f} \gamma^ {\mu} \left(Q _ {f} ^ {L} P _ {L} + Q _ {f} ^ {R} P _ {R}\right) \psi_ {f} \tag {3.2}
$$

where, in practice, only the four lightest quarks  $f = u, d, s, c$  contribute in our analysis. In the above expressions,  $P_L$  and  $P_R$  are projectors on the left- and right-handed components of a fermion, respectively:  $P_{L / R} = (1\mp \gamma^5) / 2$ , and  $g_{Z'}$  is the gauge coupling.

For the simplest case of the vector mediator, we choose that

$$
Q _ {\chi} ^ {L} = Q _ {\chi} ^ {R} \equiv Q _ {\chi} ^ {V}, \quad Q _ {q} ^ {L} = Q _ {q} ^ {R} \equiv Q _ {q} ^ {V} \quad (\text {v e c t o r c o u p l i n g s}). \tag {3.3}
$$

If the  $Q_{q}^{V}$  charges are equal to the electric charges, this case can be mapped onto the standard "dark photon" scenario. The U(1) gauge boson that couples to SM fields via kinetic mixing with the SM photon in this scenario is relatively tightly constrained (see ref. [78] for a review). Additionally, the charge assignment (3.3) also corresponds to the case where the SM baryon number symmetry  $\mathrm{U}(1)_B$  is gauged, which is much less constrained (depending on the branching fraction to visible and dark sectors, as shown through phenomenological studies in refs. [79-82]). In our numerical results, we choose all the charges  $Q_{q}^{V}$  to be equal, corresponding rather to the gauged  $\mathrm{U}(1)_B$ ; however, our results are independent of the  $Z'$  couplings to  $b$  and  $t$  quarks and also the impact of the coupling to  $c$  is small since it contributes to DIS process only.

The second scenario under consideration is described as

$$
- Q _ {\chi} ^ {L} = Q _ {\chi} ^ {R} \equiv Q _ {\chi} ^ {A}, \quad - Q _ {q} ^ {L} = Q _ {q} ^ {R} \equiv Q _ {q} ^ {A} \quad (\text {a x i a l - v e c t o r c o u p l i n g s}). \tag {3.4}
$$

Also in the axial-vector case, we assume the magnitude of the axial-vector charges to be equal for all relevant quarks.

For a fully consistent model, conditions on anomaly cancellation should be satisfied, the mechanism of  $Z'$  mass generation should be specified, or the issue of the Higgs charge assignment should be addressed in the axial-vector case. In this work, we choose the above models mostly for illustration. We do not elaborate further on the above-mentioned issues, we refer to [82-94] for more details on  $Z'$  phenomenology.

# 3.2 Scattering with nucleons

In this section, we present formulas for the elastic DM-nucleon cross sections that are used directly in our work to describe DM scattering with CR protons and also serve as the basis for describing QE scattering of DM with nuclei.

Nucleon matrix elements for the two relevant quark operators can be parametrized by a set of form factors in the following way [95]:

$$
\langle N (p ^ {\prime}) | \bar {q} \gamma^ {\mu} q | N (p) \rangle = \overline {{u}} (p ^ {\prime}) \left(F _ {1} ^ {q | N} (Q ^ {2}) \gamma^ {\mu} + F _ {2} ^ {q | N} (Q ^ {2}) \frac {i q _ {\nu} \sigma^ {\mu \nu}}{2 m _ {N}}\right) u (p), \qquad (3. 5)
$$

$$
\langle N (p ^ {\prime}) | \bar {q} \gamma^ {\mu} \gamma^ {5} q | N (p) \rangle = \bar {u} (p ^ {\prime}) \left(F _ {A} ^ {q | N} (Q ^ {2}) \gamma^ {\mu} \gamma^ {5} + F _ {P} ^ {q | N} (Q ^ {2}) \frac {q ^ {\mu}}{2 m _ {N}} \gamma^ {5}\right) u (p). \tag {3.6}
$$

Here  $\sigma^{\mu \nu} = i / 2[\gamma^{\mu},\gamma^{\nu}]$ ,  $p$ , and  $p'$  are the initial and final 4-momenta of the nucleon  $N$  ( $N = n,p$ ), respectively, and  $m_N$  is the nucleon mass. The term  $q = p' - p$  is the 4-momentum exchanged in the collision and we denote  $Q^2 \equiv -q^2$ .

With the charge assignments from eqs. (3.3) and (3.4) considered in this work, the formula for the DM-nucleon cross section presented in [63] simplifies to:

$$
\frac {d \sigma_ {\chi N}}{d Q ^ {2}} = \frac {g _ {Z ^ {\prime}} ^ {4} Q _ {\chi} ^ {2} m _ {N} ^ {4}}{\pi s Q _ {\mathrm {m a x}} ^ {2}} \frac {1}{(Q ^ {2} + m _ {Z ^ {\prime}} ^ {2}) ^ {2}} \left[ A + C \frac {(s - u) ^ {2}}{1 6 m _ {N} ^ {4}} \right], \tag {3.7}
$$

where  $s$  and  $u$  are the usual Mandelstam variables. In the reference frame where the nucleon is initially at rest,  $s$  is given by:

$$
s = (m _ {N} + m _ {\chi}) ^ {2} + 2 m _ {N} T _ {\chi} \tag {3.8}
$$

with  $T_{\chi}$  being the initial DM kinetic energy and

$$
s - u = 4 m _ {N} \left(m _ {\chi} + T _ {\chi}\right) - Q ^ {2}. \tag {3.9}
$$

The maximum transferred 4-momentum is given by

$$
Q _ {\max } ^ {2} = \frac {4 m _ {N} ^ {2}}{s} \left(T _ {\chi} ^ {2} + 2 m _ {\chi} T _ {\chi}\right). \tag {3.10}
$$

The other coefficients in eq. (3.7) differ for the vector and axial-vector cases.

Vector couplings. For the charge assignment from eq. (3.3),  $Q_{\chi} \equiv Q_{\chi}^{V}$  in eq. (3.7) and

$$
A = A _ {1 1} \left(F _ {1} ^ {N}\right) ^ {2} + A _ {1 2} F _ {1} ^ {N} F _ {2} ^ {N} + A _ {2 2} \left(F _ {2} ^ {N}\right) ^ {2}, \tag {3.11}
$$

$$
A _ {1 1} = \tau (\tau - \delta - 1), \tag {3.12}
$$

$$
A _ {1 2} = 2 \tau (2 \tau - \delta), \tag {3.13}
$$

$$
A _ {2 2} = \tau [ \tau (1 - \tau) - \delta ], \tag {3.14}
$$

$$
C = \left(F _ {1} ^ {N}\right) ^ {2} + \tau \left(F _ {2} ^ {N}\right) ^ {2}, \tag {3.15}
$$

with  $\tau \equiv Q^2 /(4m_N^2)$  and  $\delta \equiv m_{\chi}^{2} / m_{N}^{2}$ . The form factors are related to quark vector charges in the following way:

$$
F _ {i} ^ {N} = \sum_ {q = u, d, s} Q _ {q} ^ {V} F _ {i} ^ {q | N}, \tag {3.16}
$$

$i = 1,2$ . Aligned with definitions in ref. [63], this work employs the isospin limit ( $F_{i}^{u|p} = F_{i}^{d|n}$ ,  $F_{i}^{d|p} = F_{i}^{u|n}$ ) and uses the following values at zero momentum transfer  $Q^2 = 0$ :

$$
F _ {1} ^ {u | p} (0) = 2, \quad F _ {1} ^ {d | p} (0) = 1, \quad F _ {1} ^ {s | p} (0) = F _ {1} ^ {s | n} (0) = 0, \tag {3.17}
$$

$$
F _ {2} ^ {u | p} (0) = 2 \mu_ {p} + \mu_ {n} - 1, \qquad F _ {2} ^ {d | p} (0) = 2 \mu_ {n} + \mu_ {p} - 1, \qquad F _ {2} ^ {s | p} (0) = F _ {2} ^ {s | n} (0) = 0. \qquad (3. 1 8)
$$

Here  $\mu_p = 2.7930$  and  $\mu_n = -1.913042$  represent the proton and neutron anomalous magnetic moments, respectively. The dependence of the form factors on  $Q^2$  is given by:

$$
F _ {1} ^ {N} \left(Q ^ {2}\right) = \frac {F _ {1} ^ {N} (0) + \tau \left[ F _ {1} ^ {N} (0) + F _ {2} ^ {N} (0) \right]}{(1 + \tau) \left(1 + Q ^ {2} / M _ {V} ^ {2}\right) ^ {2}}, \quad F _ {2} ^ {N} \left(Q ^ {2}\right) = \frac {F _ {2} ^ {N} (0)}{(1 + \tau) \left(1 + Q ^ {2} / M _ {V} ^ {2}\right) ^ {2}} \tag {3.19}
$$

where  $M_V = 0.84 \, \mathrm{GeV}$ . The values of  $M_V$ ,  $\mu_p$  and  $\mu_n$  correspond to the default values used in the GENIE module [63].

At low energies, the vector couplings lead to the SI scattering of DM with nuclei. To compare our results with the existing direct detection limits on SI interactions of halo DM, we calculate the quantity  $(d\sigma_{\chi p} / dQ^2)Q_{\mathrm{max}}^2$  in the highly non-relativistic limit,  $Q^2\rightarrow 0$ ,  $s\rightarrow (m_{\chi} + m_p)^2$ , that, in this limit, corresponds to the total DM-proton cross section:

$$
\sigma_ {p} ^ {\mathrm {S I}} = \frac {g _ {Z ^ {\prime}} ^ {4} (3 Q _ {q} ^ {V}) ^ {2} (Q _ {\chi} ^ {V}) ^ {2} \mu_ {\chi p} ^ {2}}{\pi m _ {Z ^ {\prime}} ^ {4}}. \tag {3.20}
$$

Here  $\mu_{\chi p}$  represents the reduced mass of the DM-proton system.

Axial-vector couplings. For the charge assignment (3.4),  $Q_{\chi} \equiv Q_{\chi}^{A}$  in eq. (3.7) and

$$
A = \left(F _ {A} ^ {N} - \tau F _ {P} ^ {N}\right) ^ {2} \delta \left(1 + \frac {Q ^ {2}}{m _ {Z ^ {\prime}} ^ {2}}\right) ^ {2} + \left(F _ {A} ^ {N}\right) ^ {2} (1 + \tau) (\delta + \tau), \tag {3.21}
$$

$$
C = \left(F _ {A} ^ {N}\right) ^ {2}. \tag {3.22}
$$

The form factors are now related to quark axial charges:

$$
F _ {i} ^ {N} = \sum_ {q = u, d, s} Q _ {q} ^ {A} F _ {i} ^ {q | N}, \tag {3.23}
$$

$i = A, P$ . The axial form factors are related in isospin limit as  $F_{A}^{u|p} = F_{A}^{d|n}$ ,  $F_{A}^{d|p} = F_{A}^{u|n}$  and  $F_{A}^{s|p} = F_{A}^{s|n}$  and their  $Q^2 = 0$  values are denoted by

$$
F _ {A} ^ {q | p} (0) = \Delta q, \tag {3.24}
$$

where  $\Delta u = 0.827$ ,  $\Delta d = -0.38$  and  $\Delta s = -0.0427$ . The dipole form is assumed also for the axial form factor:

$$
F _ {A} \left(Q ^ {2}\right) = \frac {F _ {A} (0)}{\left(1 + Q ^ {2} / M _ {A} ^ {2}\right) ^ {2}} \tag {3.25}
$$

with  $M_A = 0.99$  GeV. For the pseudoscalar form factors, ref. [63] assumes  $F_P^{s|p} = F_P^{s|n} = 0$  and

$$
F _ {P} ^ {u / d | p} = \frac {2 m _ {p} ^ {2}}{(1 + Q ^ {2} / M _ {A} ^ {2}) ^ {2}} \left(\pm \frac {\Delta u - \Delta d}{m _ {\pi} ^ {2} + Q ^ {2}} + \frac {\Delta u + \Delta d - 2 \Delta s}{m _ {\eta} ^ {2} + Q ^ {2}}\right) \tag {3.26}
$$

with  $m_{\pi} = 0.1349766 \mathrm{GeV}$  and  $m_{\eta} = 0.547862 \mathrm{GeV}$  representing the pion and  $\eta$  masses, respectively. The neutron form factors can be again obtained using the isospin relations  $F_{P}^{u|p} = F_{P}^{d|n}$ ,  $F_{P}^{d|p} = F_{P}^{u|n}$ . Notably, the shapes of the form factors and values of the constants above again correspond to the defaults in the current version of the GENIE code that may differ slightly from other works, such as from ref. [95].

The axial couplings lead to SD coupling of DM with nuclei at low energies<sup>7</sup> and the formula for the total cross section in the highly non-relativistic limit now reads

$$
\sigma_ {p} ^ {\mathrm {S D}} = \frac {3 g _ {Z ^ {\prime}} ^ {4} (Q _ {\chi} ^ {A}) ^ {2} \mu_ {p \chi} ^ {2} F _ {A} ^ {p} (0) ^ {2}}{\pi m _ {Z ^ {\prime}} ^ {4}}, \tag {3.27}
$$

where  $F_A^p(0)$  is the  $Q^2 = 0$  value of the axial form factor, see eqs. (3.23) and (3.24).

Finally, DIS of DM with nucleons becomes relevant at higher energies and this contribution is calculated numerically using the GENIE code [63]. In figure 1, the differential cross section  $d\sigma_{\chi p} / dQ^2$  is shown, including both elastic scattering and DIS for the case of vector and axial-vector couplings. For the kinetic energies of the incoming DM particles at  $T_{\chi} = 1$  GeV and with the proton initially at rest, the DIS contribution is already significant at larger momentum transfers and is similar in size for vector and axial-vector couplings. The  $Q^2 \rightarrow 0$  value of the elastic contribution to the differential cross section is, however, suppressed for the axial-vector couplings by the factor

$$
\left. \frac {\frac {d \sigma_ {x p} ^ {A}}{d Q ^ {2}}}{\frac {d \sigma_ {x p} ^ {V}}{d Q ^ {2}}} \right| _ {Q ^ {2} = 0} = \frac {\left[ F _ {A} ^ {p} (0) \right] ^ {2}}{\left(3 Q _ {q} ^ {V}\right) ^ {2}} \left[ 1 + \frac {2 m _ {\chi} ^ {2}}{\left(m _ {\chi} + T _ {\chi}\right) ^ {2}} \right] \xrightarrow {T _ {\chi} \rightarrow 0} \frac {\sigma_ {p} ^ {\mathrm {S D}}}{\sigma_ {p} ^ {\mathrm {S I}}} \simeq 0. 0 5, \tag {3.28}
$$

where the last equality holds for the specific charges we use for our numerical results:  $Q_{\chi}^{V} = Q_{\chi}^{A} = Q_{q}^{V} = Q_{q}^{A} = 1$  for all quarks  $q$ .

# 3.3 Scattering with nuclei

Coherent DM-nucleus scattering is the dominant process at lower energies. For the vector couplings, the relevant cross section was calculated in [42]. Under the assumption that the DM-nucleon cross sections in the non-relativistic limit are equal,  $\sigma_{n}^{\mathrm{SI}} = \sigma_{p}^{\mathrm{SI}}$ , following expression is obtained

$$
\begin{array}{l} \frac {d \sigma_ {\chi A}}{d Q ^ {2}} = \frac {A ^ {2} \sigma_ {p} ^ {\mathrm {S I}}}{\mu_ {\chi p} ^ {2} Q _ {\max } ^ {2}} \frac {m _ {Z ^ {\prime}} ^ {4}}{\left(Q ^ {2} + m _ {Z ^ {\prime}} ^ {2}\right) ^ {2}} \times G _ {A} ^ {2} \left(Q ^ {2}\right) \tag {3.29} \\ \times \frac {1}{4 s} \left\{ \begin{array}{l l} m _ {\chi} ^ {2} Q ^ {2} - Q ^ {2} s + (s - m _ {A} ^ {2} - m _ {\chi} ^ {2}) ^ {2} & \mathrm {f o r s c a l a r n u c l e i ,} \\ \frac {1}{2} Q ^ {4} - Q ^ {2} s + (s - m _ {A} ^ {2} - m _ {\chi} ^ {2}) ^ {2} & \mathrm {f o r f e r m i o n i c n u c l e i ,} \end{array} \right. \\ \end{array}
$$

for a nucleus with atomic number  $A$  and mass  $m_A$ . Here  $G_A(Q^2)$  is the nuclear form factor capturing the loss of coherence at large momentum transfers. As in [42], we employ the model-independent form factors [98] based on elastic electron scattering data. The Fourier-Bessel expansion approach is used, with parameters taken from ref. [99]. We use

![](images/8db552ddcd1075ca236b1c639f258fc8f799895cfc331093a4c39a81b7f068e9.jpg)  
Figure 1. Differential cross sections for the scattering of DM with kinetic energy  $T_{\chi} = 1$  GeV with a proton initially at rest for the cases of vector and axial-vector couplings. The mediator and DM masses are set to  $m_{Z^{\prime}} = 1$  GeV and  $m_{\chi} = 1$  GeV, respectively, further, the values  $Q_{\chi}^{V} = Q_{\chi}^{A} = Q_{q}^{V} = Q_{q}^{A} = 1$  for all quarks  $q$  and  $g_{Z^{\prime}} = 0.1$  are assumed. The dashed lines correspond to the elastic scattering given by formula (3.7), the dotted lines correspond to the DIS contribution obtained from the GENIE module [63], and the solid lines correspond to the sum of these two contributions.

model-independent Sum of Gaussian form factors for nuclei where these parameters are not available. Furthermore,  $\sigma_p^{\mathrm{SI}}$  was defined in eq. (3.20). For the scattering of DM with kinetic energy  $T_{\chi}$  with a nucleus at rest, the kinematic variables are given by:

$$
Q _ {\mathrm {m a x}} ^ {2} = \frac {4 m _ {A} ^ {2}}{s} \left(T _ {\chi} ^ {2} + 2 m _ {\chi} T _ {\chi}\right), \tag {3.30}
$$

and

$$
s = \left(m _ {A} + m _ {\chi}\right) ^ {2} + 2 m _ {A} T _ {\chi}. \tag {3.31}
$$

For the axial couplings, the cross section for coherent elastic scattering vanishes for nuclei with zero spin. Consequently, this process will not be included in this work since the dominant isotopes of larger CR nuclei in our analysis (He, C, O) have zero spin. Additionally, the analysis neglects the nuclei with non-zero spin in our estimate of the attenuation effect, as further described in appendix B.

DM may scatter with individual nucleons within a nucleus through QE scattering at higher energies. The full description of this process requires, apart from the knowledge of the DM-nucleon cross section (3.7), also modeling of the initial momenta of the nucleons and the nuclear potential that affects the final state of the nucleus after the collision. For this reason, the GENIE module [63], specifically the GDM18_00a_00_000 tune from GENIE v3_04_00, is used for calculating the cross sections that are employed for the treatment of DM up-scattering by CR, attenuation, and also DM detection in DUNE, see appendix D for

![](images/88cc56643bfef61a1330a57728056145104ca26145f2cbccc52b9a5f3e82fc8f.jpg)  
Figure 2. Differential cross sections for the scattering of DM with kinetic energy  $T_{\chi} = 1$  GeV with an argon nucleus initially at rest for the cases of vector and axial-vector couplings, obtained from the GENIE module [63]. The values of the couplings and DM and mediator masses are the same as in figure 1. The dashed and dotted lines correspond to QE scattering and DIS, respectively. The solid lines correspond to the sum of these two contributions. The dot-dashed line depicts the simple estimate of the QE cross section from the sum of elastic cross sections for nucleons initially at rest. The grid lines depict the maximum kinematically allowed momentum transfer  $Q_{\mathrm{max}}^2$  for the elastic scattering of DM with a nucleon at rest ( $\sim 2$  GeV $^2$ ) and with an argon nucleus at rest ( $\sim 10$  GeV $^2$ ), see appendix A for details.

details. Let us note that in this way, we improve the analysis of ref. [35] that considered the scattering off free nucleons in the DUNE detector, which corresponds to the approximation  $\sigma_{\chi A} \sim A \times \sigma_{\chi N}$ . We show in figure 2 that this simplified formula (depicted by a dot-dashed line) overestimates the cross section for QE scattering of DM off argon nuclei (dashed line).

Finally, DM particles can probe individual partons in the nuclei at the highest energies, corresponding to the DIS process. Figure 2 shows the relevant DIS cross section as the dotted lines. The DIS cross sections are again comparable for the vector and axial-vector case. In contrast, the QE cross section is suppressed roughly by the factor (3.28) in the axial case in comparison to the vector case, i.e., we observe roughly the same relative suppression as for the DM-nucleon cross sections depicted in figure 1.

# 4 Results

This section presents the DUNE sensitivities for the two example DM scenarios described above. In the numerical analysis, we choose  $Q_{\chi}^{A} = Q_{\chi}^{V} = Q_{q}^{A} = Q_{q}^{V} = 1 \forall q$ , with  $m_{Z'}$  fixed at  $1\mathrm{GeV}$ . Note that with this charge assignment, the DM coupling to protons and neutrons is equal. Our study explores the sensitivity as a function of the DM mass and the coupling constant  $(g_{Z'})$  or equivalently the non-relativistic cross sections  $(\sigma_p^{\mathrm{SI}} = \sigma_n^{\mathrm{SI}}$ ,  $\sigma_p^{\mathrm{SD}} = \sigma_n^{\mathrm{SD}})$ .

# 4.1 CRDM flux

Using the DarkSUSY program [71-73] where the formulas from section 2.1 are implemented, the CRDM fluxes are produced in figure 3. For the vector couplings (top panel), the solid lines depict the full flux due to the scattering of DM with CR protons and He, C, and O nuclei, including both elastic scattering (coherent elastic scattering in case of larger nuclei) and inelastic scattering (DIS for all elements and QE for larger nuclei). The dashed lines then show the case with elastic CR-DM scattering only, whereas the dotted lines correspond to the case where only the scattering with CR protons is included.

For low DM kinetic energies, the scattering with larger nuclei is important. However, it can be checked that it is mainly the coherent elastic scattering that accounts for the difference between the solid and dotted curves at low energies. For larger  $T_{\chi}$ , the contribution of the larger nuclei is negligible due to nuclear form factors that suppress the coherent elastic scattering. By comparison of the solid, dashed, and dotted lines, the contribution of DIS of DM with CR protons significantly increases the flux at large  $T_{\chi}$ . The tiny difference between the dashed and solid lines around the peak of the CRDM flux is mainly due to QE scattering of DM with CR helium.

Based on the results for vector couplings, only scattering with CR protons is considered for the axial-vector case, where elastic coherent scattering with He, C and O nuclei is absent due to the zero spin of these nuclei. Solid lines in the bottom panel of figure 3 depict the fluxes where both elastic scattering and DIS with CR protons are included, whereas the dashed lines include the elastic scattering only. The DIS contribution is even more important for the flux at high  $T_{\chi}$  than for the vector couplings. The higher contribution of DIS at high  $T_{\chi}$  comes from the relative suppression of elastic scattering for the axial-coupling case compared to the vector couplings, as seen in figure 1.

# 4.2 Expected number of events in DUNE

After obtaining the CRDM flux, the next step calculates the number of events that the DUNE experiment should expect for a given DM model given 400 kiloton\*years of data-taking, the baseline exposure for DUNE [58]. The counting considers a selection cut  $\cos \theta_z \geq 0.1$ , which corresponds to DM coming from above. Dark matter from below becomes attenuated as it travels through the earth, weakening the signal strength compared to the atmospheric neutrino background. For that reason, the selection cut is used to optimize the signal-to-background ratio. In figure 4, solid lines depict the expected total number of events related to DM particles from the signal region  $\cos \theta_z \geq 0.1$  for two particular parameter choices. We choose to fix  $g_{Z'}$  since then the number of events varies only mildly for smaller DM masses. Grid lines depict the corresponding non-relativistic cross sections. The number of events drops rapidly for  $m_{\chi} \gtrsim 1\mathrm{GeV}$ , which is related to the fact that the CRDM flux decreases and contains DM with too small kinetic energies. The dashed lines in figure 4 show the calculated number of DM events when the inelastic interactions are neglected in the CR-DM scattering. As expected based on the observation of the CRDM fluxes, the inclusion of the inelastic CR-DM scattering considerably increases the number of events in the case of axial-vector couplings, especially for larger DM masses. The dotted lines in figure 4, in turn, depict the number of events due to full CRDM flux, but when DIS is neglected in the scattering of DM

![](images/07d39e9335d37f7f2fd91155a4354925e17e22efab3fa160314ab118654c1d6a.jpg)

![](images/a0c23b0433528bd37e3d299f0b61826aa905fd44381bc259f4e5c8c853006574.jpg)  
Figure 3. CRDM flux coming to the Earth's atmosphere. For the vector couplings (top), the solid lines correspond to the flux of the DM particles accelerated by the elastic and inelastic DM scattering with CR protons and He, C, and O nuclei. In contrast, the dotted lines correspond to scattering with protons only. On the other hand, only elastic scattering with the four most abundant CR nuclei is considered for the dashed lines. For the axial-vector couplings (bottom), the solid lines depict scattering with only CR protons (the contribution of the heavier spin-0 nuclei is subdominant in this case). The dashed lines again correspond to the flux from elastic scattering only.

![](images/70373a65f49548526f18b109db09f357f0fc985db6e36f230f9be9a1bbbf30fc.jpg)  
Figure 4. Number of events given 400 kiloton\*years of data-taking in the signal region  $\cos \theta_z \geq 0.1$  possibly seen in DUNE for a fixed value of  $g_{Z'}$  and vector (left) or axial-vector (right) couplings. The solid lines correspond to the full CRDM flux induced by both elastic and inelastic scattering with CR and both QE scattering and DIS of DM with argon nuclei in the detector. The dashed lines correspond to elastic-only contribution to the CR-DM scattering, whereas the dotted lines correspond to QE-only scattering with argon. Finally, the dashed gray line corresponds to the detection threshold derived in appendix C.

![](images/c33ae01a3276c511c0a5b5793b84a87b16f5b13496b2bf53c9caf8dbbf14201d.jpg)

with argon nuclei in the DUNE detector. The DIS contribution is crucial for detecting DM with axial-vector couplings and at lower DM masses. We confirm the findings of [100] showing that DIS becomes less important for DM detection in DUNE-like detectors for DM masses  $\gtrsim 1$  GeV. Finally, the gray dashed line shows for comparison the threshold number of DM events  $N_{\chi}^{\mathrm{thr}} = 196.7$  that can be distinguished from the atmospheric neutrino background. For the chosen  $g_{Z'}$  couplings in figure 4, the CRDM particles in the signal region  $\cos \theta_z \geq 0.1$  are not considerably slowed down by the Earth's crust or atmosphere. Hence, the number of DM events is calculated directly based on the CRDM fluxes depicted in figure 3.

# 4.3 Constraints on dark matter parameter space

We will now present the sensitivity regions for DUNE given 400 kiloton\*years of data-taking. These regions correspond to the parameter space of the different DM scenarios where the predicted number of events is larger than  $N_{\chi}^{\mathrm{thr}}$ . In figure 5, we show the sensitivity regions in the  $m_{\chi} - \sigma_{p}$  plane to allow comparisons to other existing constraints. $^9$

For the vector couplings (top panel of figure 5), corresponding to SI scattering with nuclei, the results are compared with the bounds on CRDM [42, 52] obtained by reinterpretation of Xenon1T data [101].<sup>10</sup> Notably, the CRDM constraints based on LZ results [53] are

stronger than those based on the Xenon1T experiment; however, the results of [53] assume the simplified constant (i.e.,  $Q^2$ -independent) cross section and need to be recast for the case of vector mediators to make comparisons possible. Ref. [48] suggests that a limit by LZ is expected to be about a factor of two stronger than the one by Xenon1T, but detailed analysis of the LZ bound is left for future work. Further, we include in figure 5 the bounds on nuclear recoils produced by halo DM by the CRESST program (their surface run [102] and the underground CRESST-III run [103]) and the rocket-based XQC experiment [104, 105]. The DarkSide-50 results [106] place stronger constraints than CRESST-III on DM with masses larger than  $1.8\mathrm{GeV}$ , however, this would not appear in the cross-section range depicted in our figure 5. Further, strong bounds on SI scattering of light DM have been obtained based on the searches for Migdal electrons produced in nuclear recoils [7, 8]. We depict the DarkSide-50 Migdal constraints [8] by a dashed line in our comparison plot due to uncertainties in the modeling of the Migdal effect [107]. Let us note that similarly as CRDM, also the halo DM can be stopped by Earth's crust or atmosphere before reaching the detectors, consequently, the direct detection limits do not reach arbitrarily high cross sections. For the CRESST surface run, the corresponding maximal cross section is depicted by a dotted green line obtained from [108]. For other direct detection experiments, similar analysis of the maximal probed cross section is not present in the existing literature to the best of our knowledge. For the experiments located in the Gran Sasso laboratory (CRESST-III and DarkSide), value of about  $10^{-30}\mathrm{cm}^2$  for  $m_{\chi}\sim 1\mathrm{GeV}$  might be expected based on the results of [108] for CRESST-II.

Finally, we present the limits coming from structure formation, in particular, from the Lyman-  $\alpha$  forest [109], and the Milky Way satellite population [110], and also the bounds related to the BBN [57]. The latter bound is related to the fact that for large DM-nucleon cross sections, DM particles would be in thermal equilibrium with SM plasma in the early Universe and if  $m_{\chi} \lesssim 10 \mathrm{MeV}$ , they would contribute to the effective number of relativistic degrees of freedom, which would alter the BBN predictions. Let us, however, note that this bound might be slightly loosened depending on the couplings to other SM fermions [35, 111, 112], for this reason, we depict the BBN bound by a dashed line.

In the case of SD scattering (bottom panel of figure 5), refs. [17, 28] report constraints on CRDM by the neutrino experiment Borexino [113, 114]. While ref. [17] does not consider the  $Q^2$ -dependence of the cross section, ref. [28] introduces a mediator with axial-vector couplings similar to this work. Hence, we display only the latter results in figure 5. $^{11}$  Further complementary limits come from direct detection experiments like CDMS [115], PICO-60  $[116]^{12}$  or PICASSO [117], and from delayed-coincidence searches in near-surface detectors [118]. Also for these experiments, DM can be stopped by the Earth's atmosphere or

the attenuation of the CRDM flux in the Earth's crust is treated in a simplified manner as found in ref. [42]. The full analysis of the attenuation, including the GENIE data on the cross sections of DM with nucleons in the soil, roughly confirms the approximate method [52].  
<sup>11</sup>Ref. [28] introduces axial-vector couplings of the mediator directly to nucleons (not quarks). The contribution of the pseudo-scalar form factor to the DM-nucleon scattering is neglected. Further, when presenting their results on the excluded values of  $\sigma_p^{\mathrm{SD}}$ , they fix the gauge coupling and vary the mediator mass, whereas we fix  $m_{Z'}$  and vary  $g_{Z'}$ . On the other hand, it can be checked that also ref. [28] constraints  $\mathcal{O}(\mathrm{GeV})$  mediator masses, so the results should be comparable.  
$^{12}$ PICO-60 update from 2019 [67] refers to DM cross sections smaller than  $\sim 10^{-36} \, \mathrm{cm}^2$ , so it would not bring further excluded parameter space in our comparison plot.

crust before reaching the detectors, so the corresponding bounds do not extend to arbitrarily large cross sections. Reach to larger cross sections is expected for the case of [118] based on near-surface detectors than for the underground experiments CDMS, PICO and PICASSO, dedicated analysis would be needed for further details.

In figure 6, we compare the DUNE sensitivity region in the  $m_{\chi} - g_{Z'}$  plane obtained for vector and axial-vector couplings. Using the same type of lines as in figure 4, we also show how the sensitivity region shrinks when only elastic scattering of DM with CR is included (dashed lines) and when only QE scattering of DM with argon nuclei in the DUNE detector is considered. The suppression of the DM-nucleon cross section for the axial-vector couplings compared to the vector ones (see figure 1) leads to weaker limits on  $g_{Z'}$  in the axial-vector case. It also makes the contribution from DIS stronger in the axial-vector case. The inelastic scattering of DM with CR is important for the largest DM masses, without this contribution, DUNE would not be able to probe DM masses of  $m_{\chi} = 5 \mathrm{GeV}$  neither in the vector nor axial-vector case.[13]

# 4.4 Discussion on other datasets

Comparison to previous works that presented CRDM constraints by neutrino experiments [35, 41] is not provided directly in figure 5 since these results used different models, namely, scalar or pseudoscalar mediators. For the pseudoscalar mediator case, it is impossible to compare to our results for DUNE since the corresponding interaction of DM with quarks does not lead to SD scattering with nuclei at low energies, as in the case of axial-vector couplings. On the other hand, based on the results of [42], we expect that the sensitivity regions in terms of the non-relativistic cross sections should not differ considerably for the case of vector and scalar mediators, and our work indeed obtained DUNE sensitivities for similar  $\sigma_p^{\mathrm{SI}}$ , as in [35].

Ref. [35] further reports on the DUNE sensitivity region in terms of the product of the scalar mediator coupling to quarks and to DM  $g_{\phi \chi}g_{\phi q}$  that is analogous to the quantity  $g_{Z^{\prime}}^{2}Q_{\chi}^{V}Q_{q}^{V}$  in our work. One can see in [35] that considerably smaller values of  $g_{\phi \chi}g_{\phi q}$  can be probed by DUNE compared to the values of  $g_{Z^{\prime}}^{2}$ , that can be inferred from figure 6. This difference occurs because the coupling of a scalar mediator to nucleons is strongly enhanced compared to its coupling to quarks:  $g_{\phi N}\sim \sqrt{300} g_{\phi q}$ , while in the case of vector mediator, the coupling of  $Z^{\prime}$  to nucleons is of the same order as the coupling to quarks at  $g_{Z^{\prime}N} = 3Q_q^V g_{Z^{\prime}}$ .

Moreover, ref. [35] derives bounds based on KamLAND [119] and SuperK [120] data and predicts sensitivities of future detectors JUNO [121] and HyperK [122]. The results of [35] for both the scalar and pseudoscalar mediator show that these experiments do not probe as small DM couplings as DUNE. We expect that also in the case of vector and axial-vector couplings discussed in our work, the DUNE experiment will be most sensitive, consequently, we do not consider other experiments in detail. Despite its large volume, Hyper-K is expected to be less sensitive to CRDM due to larger threshold for proton detection (ref. [35] assumed the detection threshold of  $485\mathrm{MeV}$  for Hyper-K while for DUNE the kinetic energy necessary for detection is  $40\mathrm{MeV}$ ). Further, the sensitivity of the liquid scintillator detector JUNO

![](images/2ea8fe1048f69b7eb7f87d7afee5ad922b679a178e60569544a237aa725f4846.jpg)

![](images/5cb4e94267d5a960aaf13a17c3d89f7b8b2ff03291925c075417623fefcf69c9.jpg)  
Figure 5. Sensitivity of the DUNE detector assuming 400 kiloton\*years of data taking and considering only statistical errors on the number of background neutrino events (red region). Other colored regions correspond to complementary constraints. In particular, the brown regions depict the CRDM bounds by Xenon1T [52] and Borexino [28] for similar mediator scenarios as considered in our work. Further, different shades of green depict bounds on halo DM by direct detection experiments while shades of blue are used for cosmological constraints, see the main text for details. The gray region corresponds to parameter space where our DM scenarios would become non-perturbative.

![](images/caddfc085ab986810ea661f368d6d8f683d1bb94f0d5097eb49ed2c01ce2a8c1.jpg)  
Figure 6. Comparison of the values of  $g_{Z'}$  that DUNE will be sensitive to for the vector and axial-vector couplings. As in figure 4, dashed lines show how the boundary of the sensitivity region is changed if only elastic scattering of DM with CR is included in the analysis. The dotted lines, in turn, correspond to the case of QE-only detection in DUNE.

(similarly to the existing limits by KamLAND) was derived in [34, 35, 40] by considering the signal from elastic scattering with hydrogen, the signal from elastic scattering with carbon nuclei is expected to be strongly quenched [34, 40, 123]. Consequently, only part of the detector mass was assumed to form targets for DM detection and, therefore, weaker bounds were obtained. Using scattering with hydrogen only, we expect the JUNO sensitivity region to be smaller than for DUNE also in our case. $^{14}$  On the other hand, all the planned large underground neutrino experiments have the potential to probe the unexplored DM parameter space [35] and in the presence of a DM signal, combining the data from all these experiments located in different parts of the world could provide further insights.

Finally, let us note that we compared the CRDM constraints mainly to standard direct detection experiments that depend on the non-relativistic DM-nucleon interactions only. Refs. [48, 125] suggest that the scenarios with sub-GeV mediators might be strongly constrained by other complementary probes like meson decays, however, these probes are model-dependent, in particular, depend on the  $Z^{\prime}$  coupling to heavier quarks that are not important for our study. Consequently, a discussion of further theoretical and experimental constraints on the  $Z^{\prime}$  scenarios is beyond the scope of this work. An analogous study is performed in [35] for the case of scalar and pseudoscalar mediators and the results suggest that when CRDM is taken into account, DUNE might be sensitive to DM parameter space not yet constrained by any other experiment.

# 5 Conclusions and outlook

This work presents the sensitivity of the planned DUNE experiment to sub-GeV DM particles accelerated by scattering with galactic CR. The DM interactions occur with ordinary matter via a new gauge boson  $Z'$  that couples to SM quarks and DM either through vector or axial-vector interactions. The latter scenario is much more weakly constrained by standard direct detection experiments, as it corresponds to SD scattering with nuclei. However, we demonstrated that the CRDM constraints are comparable in both cases. This result points to an essential feature of the CRDM constraints, namely, that their presence is inevitable for any model where DM couples to nucleons since both the acceleration and detection mechanisms rely on this coupling. The results encourage further study of the CRDM constraints for other scenarios that might be less constrained by standard direct detection experiments, such as those where the low-energy interactions of DM with nucleons are velocity-suppressed.

Our work improved the previous studies by more realistic modeling of the QE scattering of DM with nuclei thanks to the GENIE module [63] and also by the inclusion of DIS process both for the DM up-scattering and detection. We observe that the DIS process is vital for the axial-vector couplings where the elastic scattering is relatively suppressed compared to the vector case (see figure 1). More detailed comparisons of the two panels in figure 5 reveal that the bounds on the DM-nucleon non-relativistic cross section are by about a factor of two stronger in the axial-vector case than for the vector couplings, mainly due to the DIS contributions.

We also improved on previous works by considering the atmospheric neutrino background relevant for the possible DM detection in DUNE. Let us note that a more efficient background subtraction would be possible if the directionality of the signal is taken into account, in particular, the CRDM flux is expected to arrive predominantly from the direction of the galactic center where the most significant DM density is expected [36, 41, 45, 46]. Study of the resulting anisotropy of the CRDM flux requires careful modeling of both the DM and CR distributions, and we believe this is another interesting avenue for future work.

On the topic of modeling particle scattering, another future path would be comparing the different outgoing particles from DM and neutral current neutrino interactions. Backgrounds can be rejected by selecting interactions based on the number and energies of outgoing particles predicted for DM interactions. These backgrounds also have neutrino scattering modeling uncertainties that impact the systematic uncertainties for this CRDM search, which are outside the scope of this work. We are excited at the prospect of existing and future neutrino cross sections from the Short Baseline Neutrino (SBN) program [126]. Investigating data from the SBN program allows the community to build thorough models with constrained uncertainties for this neutral current background, allowing us to include informed modeling uncertainties in future sensitivity studies.

# Acknowledgments

We thank Torsten Bringmann for useful discussions, coding tips and comments on the manuscript. We further thank Josh Berger and Martin Hoferichter for helpful discussions, and to James Alvey, Gonzalo Herrera, and Gailyn Monroe for useful input in the initial stages

of this project. Finally, we thank to AEC, University of Bern for providing an environment that allowed for starting this collaboration between the two authors. H.K. is supported by the Research Council of Norway under the FRIPRO Young Research Talent grant no. 335388.

# A Kinematics of dark matter scattering with nucleons and nuclei

When calculating the CRDM flux (2.1), integration bounds for the CR kinetic energy must be determined. It is, therefore, necessary to study the ranges that different kinematic variables can attain for different scattering processes.

Let us first consider the scattering of a DM particle with a nucleon, the initial 4-momenta of these particles being  $k = (E_{\chi}, \vec{k})$  and  $p$ , respectively. The (square of the) invariant mass of this system is then defined as  $s = (k + p)^2$ . Let us further denote the final DM 4-momentum by  $k' = (E_{\chi}', \vec{k}')$  and the 4-momentum of the final hadronic system by  $W$ , where  $m_N^2 \leq W^2 \leq \sqrt{s} - m_{\chi}$ , with the lower and upper bounds for  $W^2$  corresponding to the elastic collision and the perfectly inelastic collision, respectively. The 4-momentum exchange  $Q^2 \equiv -q^2 \equiv -(k - k')^2$  can be then written as

$$
Q ^ {2} = 2 \left(E _ {\chi} E _ {\chi} ^ {\prime} - m _ {\chi} ^ {2} - \sqrt {E _ {\chi} ^ {2} - m _ {\chi} ^ {2}} \sqrt {E _ {\chi} ^ {\prime 2} - m _ {\chi} ^ {2}} \cos \theta\right) \tag {A.1}
$$

where  $\theta$  is the angle between the vectors  $\vec{k}$  and  $\vec{k'}$  and this relation holds in any reference frame. In order to find the possible range of  $Q^2$ , it is convenient to use the center-of-mass frame where

$$
E _ {\chi} ^ {\mathrm {c . m .}} = \frac {s + m _ {\chi} ^ {2} - m _ {N} ^ {2}}{2 \sqrt {s}} \qquad E _ {\chi} ^ {\prime \mathrm {c . m .}} = \frac {s + m _ {\chi} ^ {2} - W ^ {2}}{2 \sqrt {s}}. \tag {A.2}
$$

The maximum value of  $Q^2$  is then obtained for  $\cos \theta_{\mathrm{c.m.}} = -1$  and for the minimum value of  $W^2$ :  $W_{\min}^2 = m_N^2$ . Consequently, maximum  $Q^2$  is achieved in an elastic collision where eq. (A.1) can be simplified and

$$
Q _ {\mathrm {m a x}} ^ {2} = \frac {\left(s + m _ {\chi} ^ {2} - m _ {N} ^ {2}\right) ^ {2}}{s} - 4 m _ {\chi} ^ {2}. \tag {A.3}
$$

For the case of DM with kinetic energy  $T_{\chi}$  scattering with nucleons initially at rest, Mandelstam  $s$  and  $Q_{\mathrm{max}}^2$  are given by formulas (3.8) and (3.10), respectively.

For scattering with nuclei initially at rest, we need to distinguish between different possible processes. At low energies, coherent scattering with the whole nucleus is dominant, and the maximum  $Q^2$  for this process is given by eq. (3.30). At higher energies, scattering with individual nucleons becomes relevant, formula (A.3) then applies, but  $Q_{\mathrm{max}}^2$  might be larger than in formula (3.10) since the nucleons are not initially at rest, they are moving within the nucleus, the typical momenta being  $\mathcal{O}(10) - \mathcal{O}(100)$  MeV, depending on the size of the nucleus. The numerical output from the GENIE code, however, suggests that  $Q^2$  in the inelastic scattering of DM with nuclei is smaller than  $Q_{\mathrm{max}}^2$  for the coherent elastic scattering, see figure 2 for the example of DM-Ar scattering. In this figure, the grid line at  $Q^2 \sim 2$  GeV² depicts the value of  $Q_{\mathrm{max}}^2$  for the elastic scattering of DM with kinetic energy  $T_{\chi} = 1$  GeV with a nucleon at rest and we see that the cross section indeed quickly drops for larger  $Q^2$ .

In particular, non-negligible values of the cross section do not reach the second grid line at  $Q^2 \sim 10\mathrm{GeV}^2$  that corresponds to  $Q_{\mathrm{max}}^2$  for the coherent elastic DM-Ar scattering.

In summary, for DM with fixed kinetic energy scattering off a nucleus initially at rest, the largest  $Q^2$  is obtained for coherent elastic scattering. Using this information, the value of  $T_A^{\mathrm{min}}$  entering eq. (2.1) can be found in the following way. First, note that for a given nucleus  $A$ , the DM kinetic energy in the nucleus rest frame (2.5) is fixed by  $T_A$ . Consequently, for fixed  $T_A$ , the largest  $Q^2$  is again obtained for coherent elastic scattering. For this process, the kinematic variables can then be evaluated in the DM rest frame that is more suitable for the study of the CR-DM scattering. The Mandelstam  $s$  for the case of a CR nucleus  $A$  scattering with DM particles at rest is analogous to eq. (3.31), however, with the role of  $A$  and  $\chi$  exchanged:

$$
s = \left(m _ {A} + m _ {\chi}\right) ^ {2} + 2 m _ {\chi} T _ {A}. \tag {A.4}
$$

Using  $Q_{\mathrm{max}}^2 = 2m_\chi T_\chi^{\mathrm{max}}$ , we obtain the maximum kinetic energy of the up-scattered DM particle

$$
T _ {\chi} ^ {\max } = \frac {2 m _ {\chi} ^ {2}}{s} \left(T _ {A} ^ {2} + 2 m _ {A} T _ {A}\right). \tag {A.5}
$$

From this relation, eq. (2.6) is obtained.

Finally, as mentioned above eq. (2.4), two kinematic variables are needed to describe the inelastic scattering of DM with nuclei or nucleons. The 4-momentum transfer  $Q^2$ , the angle between incoming and outgoing DM particles  $\theta$  and the hadronic invariant mass  $W$  were already mentioned above. Let us add for completeness that other kinematic variables might be used, such as the Lorenz invariant Bjorken  $x$ , or inelasticity  $y$ .

# B Attenuation of the CRDM flux

As explained in section 2.1, part of the CRDM particles can be stopped by the Earth's atmosphere or crust. For the simplified modeling of this effect, an energy-loss equation for the DM kinetic energy at a depth  $z$  is used:

$$
\frac {d T _ {\chi} ^ {z}}{d z} = - \sum_ {A} n _ {A} \int_ {0} ^ {\omega_ {\chi} ^ {\mathrm {m a x}}} d \omega_ {\chi} \frac {d \sigma_ {\chi A}}{d \omega_ {\chi}} \omega_ {\chi}. \tag {B.1}
$$

It was shown in [108] that this approach typically overestimates the attenuation effect compared to the Monte-Carlo techniques. Hence, our evaluations should be conservative in this sense. In eq. (B.1),  $\omega_{\chi} \equiv T_{\chi} - T_{\chi}'$  is the energy loss of the DM particle in a single collision with a nucleus  $A$  initially at rest. Let us note that for elastic scattering,  $\omega_{\chi} = Q^2 / (2m_A) = T_A$  where  $T_A$  is the kinetic energy of the recoiled nucleus. Importantly, for large  $Q^2$ , the cross section of the coherent elastic scattering is suppressed by nuclear form factors. Consequently, without the inclusion of inelastic scattering, the attenuation effect is substantially underestimated [42, 127]. In this work, the inelastic scattering of DM with nuclei and the relevant contribution to  $d\sigma_{\chi A} / d\omega_{\chi}$  comes from the GENIE code [63]. In principle, all the DM kinetic energy can be lost in the collisions from inelastic processes, hence,  $\omega_{\chi}^{\mathrm{max}} = T_{\chi}$  in formula (B.1).

In the case of underground detectors like DUNE, the attenuation is dominated by the contribution of the Earth's crust. Consequently, the sum in eq. (B.1) runs over the nuclei in

the Homestake rock, with  $n_A$  being the corresponding number densities. These are calculated from the soil density (assumed to be equal to  $2.7\mathrm{g/cm^3}$  that was used in [35] and that lies in the density range reported in [128]) and the mass fractions of different elements. Inspired by Homestake geology [129], this work assumes  $52.7\%$  of oxygen,  $31.5\%$  of silicon,  $6.2\%$  of aluminum,  $3.9\%$  of magnesium,  $3.8\%$  of calcium and  $1.9\%$  of potassium. These fractions correspond roughly to the average among the different rock formations; however, the final results are not sensitive to their variation. Among these nuclei, only potassium and aluminum have dominant isotopes with non-zero spin, and could then, in principle, contribute to the coherent elastic scattering in the case of axial couplings that lead to the SD scattering with nuclei. On the other hand, the coherent elastic scattering is not enhanced by the factor of  $A^2$  in the SD case and, in general, this process predominantly influences DM with lower energies that may not pass the detection threshold in DUNE. Consequently, we neglect the coherent elastic scattering in the case of axial couplings.

As mentioned in the main text, the signal region is restricted to the zenith angles with  $\cos \theta_z \geq 0.1$ , and the number of events in the DUNE detector is then not affected by the attenuation effect for DM with masses  $\lesssim 1\mathrm{GeV}$  and the cross sections at the lower boundary of the DUNE sensitivity region. However, the CRDM flux becomes attenuated for larger cross sections and masses, and this is taken into account when calculating the event rate (2.7). In practice, the flux (2.2) is split into 20 parts related to different length intervals of 0.1 in  $\cos \theta_z$ . Only nine of these parts then contribute, given the cut of  $\cos \theta_z \geq 0.1$ . For each part, the analysis evaluates the attenuation by the soil layer with the largest thickness within the given interval of  $\cos \theta_z$ , assuming Earth to be approximately spherical. For example, for the DM particles coming from the directions with  $0.1 \leq \cos \theta_z \leq 0.2$ , the soil layer is quantified to be  $14.8\mathrm{km}$ . Consequently, integration over  $\cos \theta_z$  in eq. (2.7) is performed as a sum over the nine bins in  $\cos \theta_z$  mentioned above. Let us note that the differential equation (B.1) is solved using the DarkSUSY code [71-73], again supplemented by the inelastic DM-nucleus cross sections obtained from GENIE [63].

# C Atmospheric neutrino background

The signatures of the boosted DM in DUNE might be very similar to the ones of neutral-current interactions of atmospheric neutrinos. To estimate the related background, we consider the atmospheric neutrino flux presented in the works by Honda et al. [130-132]. The corresponding data are available at the web page [133], in particular, we use the tables for averaged fluxes  $d\overline{\Phi}_{\nu}^{j} / (dE_{\nu}d\Omega)$  in the units of  $(\mathrm{m}^2\mathrm{s}\mathrm{sr}\mathrm{GeV})^{-1}$  describing the neutrinos arriving to the Homestake location from the zenith angles  $0.1j\leq \cos \theta_{z}\leq 0.1(j + 1)$ $j\in (-10,9)$ . Using the fluxes for  $\nu_{e},\bar{\nu}_{e},\nu_{\mu}$ , and  $\bar{\nu}_{\mu}$  and taking into account that our signal region corresponds to  $\cos \theta_z\geq 0.1$ , the number of the background events can be obtained in analogy with formula (2.7):

$$
\begin{array}{l} R _ {\nu} = N _ {\mathrm {A r}} \sum_ {\nu = \nu_ {e}, \bar {\nu} _ {e}, \nu_ {\mu}, \bar {\nu} _ {\mu}} \int_ {E _ {\nu}} d E _ {\nu} \sigma_ {\nu \mathrm {A r}} ^ {\mathrm {e f f}} (E _ {\nu}) \int_ {0. 1} ^ {1} d \cos \theta_ {z} \frac {d \Phi_ {\nu}}{d E _ {\nu} d \cos \theta_ {z}} (C.1) \\ = N _ {\mathrm {A r}} \sum_ {\nu = \nu_ {e}, \bar {\nu} _ {e}, \nu_ {\mu}, \bar {\nu} _ {\mu}} \int_ {E _ {\nu}} d E _ {\nu} \sigma_ {\nu \mathrm {A r}} ^ {\mathrm {e f f}} (E _ {\nu}) \sum_ {j = 1} ^ {9} 2 \pi \frac {d \bar {\Phi} _ {\nu} ^ {j}}{d E _ {\nu} d \Omega} \times 0. 1 (C.2) \\ \end{array}
$$

Again, the effective total neutrino-argon cross section  $\sigma_{\nu \mathrm{Ar}}^{\mathrm{eff}}$  takes into account the detection thresholds, see appendix D. The analysis predicts 990.4 and 930.2 background neutrino events per year at solar minimum and maximum, respectively.

Ref. [60] also considers the background due to  $\nu_{\tau}$  charged-current interactions (since the  $\tau$  lepton may not be reconstructed if it decays). However, the  $\nu_{\tau}$  background only constitutes  $2.8\%$  of atmospheric neutrinos [60], making it negligible for our studies. Therefore, this work omits it from consideration as it requires complicated simulations of atmospheric neutrino oscillations for the background calculations. The CRDM signal at DUNE represents excess interactions above the neutral current atmospheric neutrino background. Using the same statistical method as in [60], the significance of the discovery of a certain signal process in a counting experiment is calculated from ref. [134]:

$$
Z = \sqrt {2 \left[ (N _ {s} + N _ {b}) \log \left(1 + \frac {N _ {s}}{N _ {b}}\right) - N _ {s} \right]}. \tag {C.3}
$$

Here  $N_{s}$  and  $N_{b}$  are the numbers of signal and background events, respectively. This formula assumes large statistics (so that the Poisson distribution can be approximated by the Gaussian one), and it also accounts only for the statistical errors for the number of background events  $N_{b}$ . As in [60], the DUNE sensitivity region after 400 kiloton\*years of data is taken at the  $2\sigma$  level. After averaging the solar maximum and minimum results, the number of background events is  $N_{b} = 10(990.4 + 930.2) / 2 = 9603$ . The value  $Z = 2$  then requires the number of signal events at  $N_{s} = 196.7 \equiv N_{\chi}^{\mathrm{thr}}$ .

# D Generating samples of boosted dark matter interactions in GENIE

GENIE is a modular neutrino interaction simulation software intended for neutrino cross section measurements at the GeV-scale [60, 63-65]. In addition to neutrino interaction simulations, GENIE includes beyond standard model physics, such as boosted DM [63]. We use the Berger formulation in GENIE to model fermionic DM interactions, specifically the GDM18_00a_00_000 tune with GENIE v3_04_00. The standard model configuration sets the sign of all left-handed and right-handed parameters to positive. For the spin-dependent analysis, the left-handed parameters are reversed.

The model simulates both QE scattering and DIS, the latter being a catch-all term that may include interactions not typically called deep inelastic scatters. The flux of boosted DM depends on the differential DM-nucleus cross sections with respect to the energy transfer of the DM component  $(\omega_{\chi})$  and momentum transfer  $(\mathrm{Q}^2)$ . These differential cross sections are calculated for various kinetic energies of DM and targets.

To compute differential cross sections, samples with high statistics of interactions must be generated with GENIE, and the differential cross section measured from these samples. The measurement of the differential cross section per bin equates to the number of events in a bin multiplied by the total cross section divided by the number of events and bin size. It is not possible to calculate both differential cross sections of  $\omega$  and  $Q^2$  analytically within GENIE for the two relevant channels. Therefore, the generation of cross section distributions is computationally expensive, requiring each type of interaction, each kinetic energy of the incident DM particle, and each target to have individualized interaction samples.

However, it also provides flexibility for future studies as information on the final state particles, hadronization, and intranuclear interactions are also saved when generating these events.

The sample generation happens for ten targets, each a relevant material in the Earth's crust or a dominant CR element. Targets include hydrogen, helium, carbon, oxygen, magnesium, aluminum-27, silicon, argon-40, potassium-39, and calcium (see appendix B and section 2.1). Interactions are simulated to calculate the cross sections for DM masses from  $50\mathrm{MeV}$  to  $10\mathrm{GeV}$ , with cross sections for lower masses scaled based on results for  $50\mathrm{MeV}$ . The kinetic energy of the incident DM on the target is set at discrete points and sampled using a logarithmic scale starting at  $0.1\mathrm{GeV}$  and ending at  $100\mathrm{GeV}$  with 40 intermediate steps. Each kinetic energy step for each target and DM mass for each interaction type contains one hundred thousand events. The resulting  $\omega$  and  $Q^2$  from all events in a sample are binned into a differential histogram and saved using ROOT [135, 136]. An interpolating spline is then drawn over each histogram for ease of interpretation.

The rate of DM events in DUNE (2.7) is then estimated from the detector capabilities of DUNE. The DUNE liquid argon detectors are designed for detecting MeV-scale particles produced from neutrino interactions. An event is detected if a pion, proton, or kaon is produced above the kinetic energy threshold for DUNE. The kinetic energy threshold for charged pions is  $20\mathrm{MeV}$ , and the kinetic energy threshold for protons and kaons is  $40\mathrm{MeV}$ . There is no threshold for neutral pions. The thresholds used are from the most recent DUNE results from their ProtoDUNE Single-Phase detector [77]. The cross section is then re-calculated by multiplying the total boosted DM cross section by the fraction of detectable interactions given those thresholds. The same process is repeated to calculate the atmospheric neutrino background from neutral current interactions (C.1).

Data Availability Statement. This article has no associated data or the data will not be deposited.

Code Availability Statement. This article has no associated code or the code will not be deposited.

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] G. Bertone, D. Hooper and J. Silk, Particle dark matter: evidence, candidates and constraints, Phys. Rept. 405 (2005) 279 [hep-ph/0404175] [INSPIRE].  
[2] M.W. Goodman and E. Witten, Detectability of certain dark matter candidates, Phys. Rev. D 31 (1985) 3059 [INSPIRE].  
[3] LZ collaboration, First dark matter search results from the LUX-ZEPLIN (LZ) experiment, Phys. Rev. Lett. 131 (2023) 041002 [arXiv:2207.03764] [INSPIRE].  
[4] XENON collaboration, First dark matter search with nuclear recoils from the XENONnT experiment, Phys. Rev. Lett. 131 (2023) 041003 [arXiv:2303.14729] [INSPIRE].

[5] R. Essig et al., Snowmass2021 cosmic frontier: the landscape of low-threshold dark matter direct detection in the next decade, in the proceedings of the Snowmass 2021, (2022) [arXiv:2203.08297] [INSPIRE].  
[6] M. Ibe, W. Nakano, Y. Shoji and K. Suzuki, Migdal effect in dark matter direct detection experiments, JHEP 03 (2018) 194 [arXiv:1707.07258] [INSPIRE].  
[7] XENON collaboration, Search for light dark matter interactions enhanced by the Migdal effect or Bremsstrahlung in XENON1T, Phys. Rev. Lett. 123 (2019) 241803 [arXiv:1907.12771] [INSPIRE].  
[8] DARKSIDE collaboration, Search for dark-matter-nucleon interactions via Migdal effect with DarkSide-50, Phys. Rev. Lett. 130 (2023) 101001 [arXiv:2207.11967] [INSPIRE].  
[9] C. Kouvaris and J. Pradler, Probing sub-GeV dark matter with conventional detectors, Phys. Rev. Lett. 118 (2017) 031803 [arXiv:1607.01789] [INSPIRE].  
[10] K. Agashe, Y. Cui, L. Necib and J. Thaler, (In)direct detection of boosted dark matter, JCAP 10 (2014) 062 [arXiv:1405.7370] [INSPIRE].  
[11] J. Berger, Y. Cui and Y. Zhao, Detecting boosted dark matter from the Sun with large volume neutrino detectors, JCAP 02 (2015) 005 [arXiv:1410.2246] [INSPIRE].  
[12] J. Kopp, J. Liu and X.-P. Wang, Boosted dark matter in IceCube and at the galactic center, JHEP 04 (2015) 105 [arXiv:1503.02669] [INSPIRE].  
[13] C. Kouvaris, Probing light dark matter via evaporation from the Sun, Phys. Rev. D 92 (2015) 075001 [arXiv:1506.04316] [INSPIRE].  
[14] H. An, M. Pospelov, J. Pradler and A. Ritz, Directly detecting MeV-scale dark matter via solar reflection, Phys. Rev. Lett. 120 (2018) 141801 [Erratum ibid. 121 (2018) 259903] [arXiv:1708.03642] [INSPIRE].  
[15] T. Emken, C. Kouvaris and N.G. Nielsen, The Sun as a sub-GeV dark matter accelerator, Phys. Rev. D 97 (2018) 063007 [arXiv:1709.06573] [INSPIRE].  
[16] W. Yin, Highly-boosted dark matter and cutoff for cosmic-ray neutrinos through neutrino portal, EPJ Web Conf. 208 (2019) 04003 [arXiv:1809.08610] [INSPIRE].  
[17] T. Bringmann and M. Pospelov, Novel direct detection constraints on light dark matter, Phys. Rev. Lett. 122 (2019) 171801 [arXiv:1810.10543] [INSPIRE].  
[18] C.V. Cappiello, K.C.Y. Ng and J.F. Beacom, Reverse direct detection: cosmic ray scattering with light dark matter, Phys. Rev. D 99 (2019) 063004 [arXiv:1810.07705] [INSPIRE].  
[19] Y. Ema, F. Sala and R. Sato, Light dark matter at neutrino experiments, Phys. Rev. Lett. 122 (2019) 181802 [arXiv:1811.00520] [INSPIRE].  
[20] J.B. Dent et al., Present and future status of light dark matter models from cosmic-ray electron upscattering, Phys. Rev. D 103 (2021) 095015 [arXiv:2010.09749] [INSPIRE].  
[21] J.B. Dent et al., Gamma ray signals from cosmic ray scattering on axionlike particles, Phys. Rev. D 104 (2021) 055044 [arXiv:2012.07930] [INSPIRE].  
[22] D. Bardhan et al., Bounds on boosted dark matter from direct detection: the role of energy-dependent cross sections, Phys. Rev. D 107 (2023) 015010 [arXiv:2208.09405] [INSPIRE].  
[23] Q.-H. Cao, R. Ding and Q.-F. Xiang, Searching for sub-MeV boosted dark matter from xenon electron direct detection, Chin. Phys. C 45 (2021) 045002 [arXiv:2006.12767] [INSPIRE].

[24] Y. Jho, J.-C. Park, S.C. Park and P.-Y. Tseng, Leptonic new force and cosmic-ray boosted dark matter for the XENON1T excess, Phys. Lett. B 811 (2020) 135863 [arXiv:2006.13910] [INSPIRE].  
[25] PANDAX collaboration, Search for cosmic-ray boosted sub-MeV dark-matter-electron scattering in PandaX-4T, Phys. Rev. Lett. 133 (2024) 101805 [arXiv:2403.08361] [INSPIRE].  
[26] T. Herbermann, M. Lindner and M. Sen, Attenuation of cosmic ray electron boosted dark matter, Phys. Rev. D 110 (2024) 123023 [arXiv:2408.02721] [INSPIRE].  
[27] A. Guha and J.-C. Park, Constraints on cosmic-ray boosted dark matter with realistic cross section, JCAP 07 (2024) 074 [arXiv:2401.07750] [INSPIRE].  
[28] J.B. Dent, B. Dutta, J.L. Newstead and I.M. Shoemaker, Bounds on cosmic ray-boosted dark matter in simplified models and its corresponding neutrino-floor, Phys. Rev. D 101 (2020) 116007 [arXiv:1907.03782] [INSPIRE].  
[29] W. Wang et al., Cosmic ray boosted sub-GeV gravitationally interacting dark matter in direct detection, JHEP 12 (2020) 072 [Erratum ibid. 02 (2021) 052] [arXiv:1912.09904] [INSPIRE].  
[30] K. Bondarenko et al., Direct detection and complementary constraints for sub-GeV dark matter, JHEP 03 (2020) 118 [arXiv:1909.08632] [INSPIRE].  
[31] W. Cho, K.-Y. Choi and S.M. Yoo, Searching for boosted dark matter mediated by a new gauge boson, Phys. Rev. D 102 (2020) 095010 [arXiv:2007.04555] [INSPIRE].  
[32] G. Guo, Y.-L.S. Tsai, M.-R. Wu and Q. Yuan, Elastic and inelastic scattering of cosmic-rays on sub-GeV dark matter, Phys. Rev. D 102 (2020) 103004 [arXiv:2008.12137] [INSPIRE].  
[33] C. Xia, Y.-H. Xu and Y.-F. Zhou, Azimuthal asymmetry in cosmic-ray boosted dark matter flux, Phys. Rev. D 107 (2023) 055012 [arXiv:2206.11454] [INSPIRE].  
[34] C.V. Cappiello and J.F. Beacom, *Strong new limits on light dark matter from neutrino experiments*, Phys. Rev. D 100 (2019) 103011 [Erratum ibid. 104 (2021) 069901] [arXiv:1906.11283] [INSPIRE].  
[35] Y. Ema, F. Sala and R. Sato, Neutrino experiments probe hadrophilic light dark matter, SciPost Phys. 10 (2021) 072 [arXiv:2011.01939] [INSPIRE].  
[36] S.-F. Ge, J. Liu, Q. Yuan and N. Zhou, Diurnal effect of sub-GeV dark matter boosted by cosmic rays, Phys. Rev. Lett. 126 (2021) 091804 [arXiv:2005.09480] [INSPIRE].  
[37] R. Harnik, R. Plestid, M. Pospelov and H. Ramani, Millicharged cosmic rays and low recoil detectors, Phys. Rev. D 103 (2021) 075029 [arXiv:2010.11190] [INSPIRE].  
[38] J. Bramante, B.J. Kavanagh and N. Raj, Scattering searches for dark matter in subhalos: neutron stars, cosmic rays, and old rocks, Phys. Rev. Lett. 128 (2022) 231801 [arXiv:2109.04582] [INSPIRE].  
[39] PANDAX-II collaboration, Search for cosmic-ray boosted sub-GeV dark matter at the PandaX-II experiment, Phys. Rev. Lett. 128 (2022) 171801 [arXiv:2112.08957] [INSPIRE].  
[40] B. Chauhan, B. Dasgupta and A. Dighe, Large-energy single hits at JUNO from atmospheric neutrinos and dark matter, Phys. Rev. D 105 (2022) 095035 [arXiv:2111.14586] [INSPIRE].  
[41] SUPER-KAMIOKANDE collaboration, Search for cosmic-ray boosted sub-GeV dark matter using recoil protons at Super-Kamiokande, Phys. Rev. Lett. 130 (2023) 031802 [Erratum ibid. 131 (2023) 159903] [arXiv:2209.14968] [INSPIRE].  
[42] J. Alvey, T. Bringmann and H. Kolesova, No room to hide: implications of cosmic-ray upscattering for GeV-scale dark matter, JHEP 01 (2023) 123 [arXiv:2209.03360] [INSPIRE].

[43] H. Kolesova, Attenuation of cosmic-ray up-scattered dark matter, SciPost Phys. Proc. 12 (2023) 055 [arXiv:2209.14600] [INSPIRE].  
[44] T.N. Maity and R. Laha, *Cosmic-ray boosted dark matter in Xe-based direct detection experiments*, Eur. Phys. J. C **84** (2024) 117 [arXiv:2210.01815] [INSPIRE].  
[45] K.I. Nagao, S. Higashino, T. Naka and K. Miuchi, Directional direct detection of light dark matter up-scattered by cosmic rays from direction of the galactic center, JCAP 07 (2023) 061 [arXiv:2211.13399] [INSPIRE].  
[46] NEWSDM collaboration, Directional sensitivity of the NEWSdm experiment to cosmic ray boosted dark matter, JCAP 07 (2023) 067 [arXiv:2305.00112] [INSPIRE].  
[47] W. Wang, W.-L. Xu, J.M. Yang and R. Zhu, Direct detection of cosmic ray-boosted puffy dark matter, Nucl. Phys. B 995 (2023) 116348 [arXiv:2305.12668] [INSPIRE].  
[48] N.F. Bell, J.L. Newstead and I. Shaukat-Ali, *Cosmic-ray boosted dark matter confronted by constraints on new light mediators*, Phys. Rev. D 109 (2024) 063034 [arXiv:2309.11003] [INSPIRE].  
[49] L. Su, L. Wu and B. Zhu, An improved bound on accelerated light dark matter, Sci. China Phys. Mech. Astron. 67 (2024) 221012 [arXiv:2308.02204] [INSPIRE].  
[50] B. Dutta et al., Prospects for light dark matter searches at large-volume neutrino detectors, Phys. Rev. Lett. 133 (2024) 161801 [arXiv:2402.04184] [INSPIRE].  
[51] I. Reis, E. Moulin, A. Viana and V.P. Goncalves, Sensitivity to sub-GeV dark matter from cosmic-ray scattering with very-high-energy gamma-ray observatories, JCAP 07 (2024) 012 [arXiv:2403.09343] [INSPIRE].  
[52] R. Diurba, H. Kolešová and G. Monroe, Effect of inelastic scattering on cosmic-ray-boosted dark matter, PoS ICHEP2024 (2025) 774 [arXiv:2409.05932] [INSPIRE].  
[53] LZ collaboration, New constraints on cosmic ray-boosted dark matter from the LUX-ZEPLIN experiment, Phys. Rev. Lett. 134 (2025) 241801 [arXiv:2503.18158] [INSPIRE].  
[54] G. Guo, Y.-L.S. Tsai and M.-R. Wu, Probing cosmic-ray accelerated light dark matter with IceCube, JCAP 10 (2020) 049 [arXiv:2004.03161] [INSPIRE].  
[55] C.V. Cappiello, Q. Liu, G. Mohlabeng and A.C. Vincent, *Cosmic ray-boosted dark matter at IceCube*, Phys. Rev. D 110 (2024) 095031 [arXiv:2405.00086] [INSPIRE].  
[56] F. Lin, N. Liu, L. Su and L. Wu, Detecting light dark matter with prompt-delayed events in neutrino experiments, arXiv:2504.13007 [INSPIRE].  
[57] G. Krnjaic and S.D. McDermott, Implications of BBN bounds for cosmic ray upscattered dark matter, Phys. Rev. D 101 (2020) 123022 [arXiv:1908.00007] [INSPIRE].  
[58] DUNE collaboration, Deep Underground Neutrino Experiment (DUNE), far detector technical design report. Volume I: introduction to DUNE, 2020 JINST 15 T08008 [arXiv:2002.02967] [INSPIRE].  
[59] D. Kim, J.-C. Park and S. Shin, Dark matter "collider" from inelastic boosted dark matter, Phys. Rev. Lett. 119 (2017) 161801 [arXiv:1612.06867] [INSPIRE].  
[60] J. Berger et al., Prospects for detecting boosted dark matter in DUNE through hadronic interactions, Phys. Rev. D 103 (2021) 095012 [arXiv:1912.05558] [INSPIRE].  
[61] A. De Roeck et al., Probing energetic light dark matter with multi-particle tracks signatures at DUNE, JHEP 11 (2020) 043 [arXiv:2005.08979] [INSPIRE].

[62] J.F. Acevedo, J. Berger and P.B. Denton, Dark matter raining on DUNE and other large volume detectors, JHEP 11 (2024) 011 [arXiv:2407.01670] [INSPIRE].  
[63] J. Berger, A module for boosted dark matter event generation in GENIE, arXiv:1812.05616 [INSPIRE].  
[64] C. Andreopoulos et al., The GENIE neutrino Monte Carlo generator, Nucl. Instrum. Meth. A 614 (2010) 87 [arXiv:0905.2517] [INSPIRE].  
[65] C. Andreopoulos et al., The GENIE neutrino Monte Carlo generator: physics and user manual, arXiv:1510.05494 [INSPIRE].  
[66] GENIE collaboration, Hadronization model tuning in GENIE v3, Phys. Rev. D 105 (2022) 012009 [arXiv:2106.05884] [INSPIRE].  
[67] PICO collaboration, Dark matter search results from the complete exposure of the PICO-60  $C_3F_8$  bubble chamber, Phys. Rev. D 100 (2019) 022001 [arXiv:1902.04031] [INSPIRE].  
[68] C. Xia, Y.-H. Xu and Y.-F. Zhou, Production and attenuation of cosmic-ray boosted dark matter, JCAP 02 (2022) 028 [arXiv:2111.05559] [INSPIRE].  
[69] M.J. Boschini et al., Deciphering the local interstellar spectra of primary cosmic ray species with HelMod, Astrophys. J. 858 (2018) 61 [arXiv:1804.06956] [INSPIRE].  
[70] M.J. Boschini et al., Inference of the local interstellar spectra of cosmic-ray nuclei  $Z \leq 28$  with the GalProp-HelMod framework, Astrophys. J. Suppl. 250 (2020) 27 [arXiv:2006.01337] [INSPIRE].  
[71] P. Gondolo et al., DarkSUSY: computing supersymmetric dark matter properties numerically, JCAP 07 (2004) 008 [astro-ph/0406204] [INSPIRE].  
[72] T. Bringmann et al., DarkSUSY 6: an advanced tool to compute dark matter properties numerically, JCAP 07 (2018) 033 [arXiv:1802.03399] [INSPIRE].  
[73] T. Bringmann and J. Edsjö, DarkSUSY 6.3 — freeze-in, out-of-equilibrium freeze-out, cosmic-ray upscattering and further new features, PoS CompTools2021 (2022) 038 [arXiv:2203.07439] [INSPIRE].  
[74] O. Buss et al., Transport-theoretical description of nuclear reactions, Phys. Rept. 512 (2012) 1 [arXiv:1106.1344] [INSPIRE].  
[75] GiBUU project webpage, https://gibuu.hepforge.org/trac/wiki.  
[76] T. Emken and C. Kouvaris, DaMaSCUS: the impact of underground scatterings on direct detection of light dark matter, JCAP 10 (2017) 031 [arXiv:1706.02249] [INSPIRE].  
[77] DUNE collaboration, First measurement of the total inelastic cross section of positively charged kaons on argon at energies between 5.0 and 7.5 GeV, Phys. Rev. D 110 (2024) 092011 [arXiv:2408.00582] [INSPIRE].  
[78] M. Fabbrichesi, E. Gabrielli and G. Lanfranchi, The dark photon, Springer International Publishing (2021) [DOI:10.1007/978-3-030-62519-1] [arXiv:2005.01515] [INSPIRE].  
[79] P. Ilten, Y. Soreq, M. Williams and W. Xue, Serendipity in dark photon searches, JHEP 06 (2018) 004 [arXiv:1801.04847] [INSPIRE].  
[80] P. Fileviez Perez, E. Golias, C. Murgui and A.D. Plascencia, The Higgs and leptophobic force at the LHC, JHEP 07 (2020) 087 [arXiv:2003.09426] [INSPIRE].  
[81] B. Batell et al., Hadrophilic dark sectors at the forward physics facility, Phys. Rev. D 105 (2022) 075001 [arXiv:2111.10343] [INSPIRE].

[82] C. Blanco, M. Escudero, D. Hooper and S.J. Witte, Z' mediated WIMPs: dead, dying, or soon to be detected?, JCAP 11 (2019) 024 [arXiv:1907.05893] [INSPIRE].  
[83] C.D. Carone and H. Murayama, Possible light  $U(1)$  gauge boson coupled to baryon number, Phys. Rev. Lett. 74 (1995) 3122 [hep-ph/9411256] [INSPIRE].  
[84] C.D. Carone and H. Murayama, Realistic models with a light  $U(1)$  gauge boson coupled to baryon number, Phys. Rev. D 52 (1995) 484 [hep-ph/9501220] [INSPIRE].  
[85] A. Aranda and C.D. Carone, Limits on a light leptophobic gauge boson, Phys. Lett. B 443 (1998) 352 [hep-ph/9809522] [INSPIRE].  
[86] A. Alves, S. Profumo and F.S. Queiroz, The dark Z' portal: direct, indirect and collider searches, JHEP 04 (2014) 063 [arXiv:1312.5281] [INSPIRE].  
[87] S. Tulin, New weakly-coupled forces hidden in low-energy QCD, Phys. Rev. D 89 (2014) 114008 [arXiv:1404.4370] [INSPIRE].  
[88] O. Lebedev and Y. Mambrini, Axial dark matter: the case for an invisible  $Z'$ , Phys. Lett. B 734 (2014) 350 [arXiv:1403.4837] [INSPIRE].  
[89] Y. Kahn, G. Krnjaic, S. Mishra-Sharma and T.M.P. Tait, Light weakly coupled axial forces: models, constraints, and projections, JHEP 05 (2017) 002 [arXiv:1609.09072] [INSPIRE].  
[90] J.A. Dror, R. Lasenby and M. Pospelov, New constraints on light vectors coupled to anomalous currents, Phys. Rev. Lett. 119 (2017) 141803 [arXiv:1705.06726] [INSPIRE].  
[91] M. Frank, Evading  $Z'$  boson mass limits in  $U(1)'$  supersymmetric models, Eur. Phys. J. ST 229 (2020) 3205 [INSPIRE].  
[92] A. Greljo, P. Stangl, A.E. Thomsen and J. Zupan, On  $(g - 2)_{\mu}$  from gauged  $U(1)_X$ , JHEP 07 (2022) 098 [arXiv:2203.13731] [INSPIRE].  
[93] T. Alanne et al., Z'-mediated Majorana dark matter: suppressed direct-detection rate and complementarity of LHC searches, JHEP 08 (2022) 093 [arXiv:2202.02292] [INSPIRE].  
[94] S. Balan et al., Resonant or asymmetric: the status of sub-GeV dark matter, JCAP 01 (2025) 053 [arXiv:2405.17548] [INSPIRE].  
[95] F. Bishara, J. Brod, B. Grinstein and J. Zupan, From quarks to nucleons in dark matter direct detection, JHEP 11 (2017) 059 [arXiv:1707.06998] [INSPIRE].  
[96] N. Anand, A.L. Fitzpatrick and W.C. Haxton, Weakly interacting massive particle-nucleus elastic scattering response, Phys. Rev. C 89 (2014) 065501 [arXiv:1308.6288] [INSPIRE].  
[97] A. Bodek and U.K. Yang, Higher twist,  $\xi_{\omega}$  scaling, and effective LO PDFs for lepton scattering in the few GeV region, J. Phys. G 29 (2003) 1899 [hep-ex/0210024] [INSPIRE].  
[98] G. Duda, A. Kemper and P. Gondolo, Model independent form factors for spin independent neutralino-nucleon scattering from elastic electron scattering data, JCAP 04 (2007) 012 [hep-ph/0608035] [INSPIRE].  
[99] H. De Vries, C.W. De Jager and C. De Vries, Nuclear charge and magnetization density distribution parameters from elastic electron scattering, Atom. Data Nucl. Data Tabl. 36 (1987) 495 [INSPIRE].  
[100] D. Kim, P.A.N. Machado, J.-C. Park and S. Shin, Optimizing energetic light dark matter searches in dark matter and neutrino experiments, JHEP 07 (2020) 057 [arXiv:2003.07369] [INSPIRE].

[101] XENON collaboration, Dark matter search results from a one ton-year exposure of XENON1T, Phys. Rev. Lett. 121 (2018) 111302 [arXiv:1805.12562] [INSPIRE].  
[102] CRESST collaboration, Results on MeV-scale dark matter from a gram-scale cryogenic calorimeter operated above ground, Eur. Phys. J. C 77 (2017) 637 [arXiv:1707.06749] [INSPIRE].  
[103] CRESST collaboration, First results from the CRESST-III low-mass dark matter program, Phys. Rev. D 100 (2019) 102002 [arXiv:1904.00498] [INSPIRE].  
[104] D. McCammon et al., A high spectral resolution observation of the soft X-ray diffuse background with thermal detectors, Astrophys. J. 576 (2002) 188 [astro-ph/0205012] [INSPIRE].  
[105] M.S. Mahdawi and G.R. Farrar, Constraints on dark matter with a moderately large and velocity-dependent DM-nucleon cross-section, JCAP 10 (2018) 007 [arXiv:1804.03073] [INSPIRE].  
[106] DARKSIDE collaboration, Low-mass dark matter search with the DarkSide-50 experiment, Phys. Rev. Lett. 121 (2018) 081307 [arXiv:1802.06994] [INSPIRE].  
[107] J. Xu et al., Search for the Migdal effect in liquid xenon with keV-level nuclear recoils, Phys. Rev. D 109 (2024) L051101 [arXiv:2307.12952] [INSPIRE].  
[108] T. Emken and C. Kouvaris, How blind are underground and surface detectors to strongly interacting dark matter?, Phys. Rev. D 97 (2018) 115047 [arXiv:1802.04764] [INSPIRE].  
[109] K.K. Rogers, C. Dvorkin and H.V. Peiris, Limits on the light dark matter-proton cross section from cosmic large-scale structure, Phys. Rev. Lett. 128 (2022) 171301 [arXiv:2111.10386] [INSPIRE].  
[110] K. Maamari et al., Bounds on velocity-dependent dark matter-proton scattering from Milky Way satellite abundance, Astrophys. J. Lett. 907 (2021) L46 [arXiv:2010.02936] [INSPIRE].  
[111] M. Escudero, Neutrino decoupling beyond the Standard Model: CMB constraints on the dark matter mass with a fast and precise  $N_{\mathrm{eff}}$  evaluation, JCAP 02 (2019) 007 [arXiv:1812.05605] [INSPIRE].  
[112] N. Sabti et al., Refined bounds on MeV-scale thermal dark sectors from BBN and the CMB, JCAP 01 (2020) 004 [arXiv:1910.01649] [INSPIRE].  
[113] BOREXINO collaboration, New experimental limits on the Pauli forbidden transitions in  $^{12}C$  nuclei obtained with 485 days Borexino data, Phys. Rev. C 81 (2010) 034317 [arXiv:0911.0548] [INSPIRE].  
[114] BOREXINO collaboration, New limits on heavy sterile neutrino mixing in  $^8 B$  decay obtained with the Borexino detector, Phys. Rev. D 88 (2013) 072010 [arXiv:1311.5347] [INSPIRE].  
[115] SUPERCDMS collaboration, Low-mass dark matter search with CDMSLite, Phys. Rev. D 97 (2018) 022002 [arXiv:1707.01632] [INSPIRE].  
[116] PICO collaboration, Dark matter search results from the PICO-60  $C_3F_8$  bubble chamber, Phys. Rev. Lett. 118 (2017) 251301 [arXiv:1702.07666] [INSPIRE].  
[117] E. Behnke et al., Final results of the PICASSO dark matter search experiment, Astropart. Phys. 90 (2017) 85 [arXiv:1611.01499] [INSPIRE].  
[118] J.I. Collar, Search for a nonrelativistic component in the spectrum of cosmic rays at earth, Phys. Rev. D 98 (2018) 023005 [arXiv:1805.02646] [INSPIRE].  
[119] KAMLAND collaboration, Measurement of the  $^8 B$  solar neutrino flux with the KamLAND liquid scintillator detector, Phys. Rev. C 84 (2011) 035804 [arXiv:1106.0861] [INSPIRE].

[120] SUPER-KAMIOKANDE collaboration, Kinematic reconstruction of atmospheric neutrino events in a large water Cherenkov detector with proton identification, Phys. Rev. D 79 (2009) 112010 [arXiv:0901.1645] [INSPIRE].  
[121] JUNO collaboration, JUNO physics and detector, Prog. Part. Nucl. Phys. 123 (2022) 103927 [arXiv:2104.02565] [INSPIRE].  
[122] HYPER-KAMIOKANDE collaboration, Hyper-Kamiokande design report, arXiv:1805.04163 [INSPIRE].  
[123] B. Dasgupta and J.F. Beacom, Reconstruction of supernova  $\nu_{\mu}$ ,  $\nu_{\tau}$ , anti- $\nu_{\mu}$ , and anti- $\nu_{\tau}$  neutrino spectra at scintillator detectors, Phys. Rev. D 83 (2011) 113006 [arXiv:1103.2768] [INSPIRE].  
[124] JUNO collaboration, Atmospheric neutrino spectrum reconstruction with JUNO, PoS EPS-HEP2019 (2020) 041 [arXiv:1910.11172] [INSPIRE].  
[125] G. Elor, R. McGehee and A. Pierce, Maximizing direct detection with highly interactive particle relic dark matter, Phys. Rev. Lett. 130 (2023) 031803 [arXiv:2112.03920] [INSPIRE].  
[126] MICROBOONE et al. collaborations, A proposal for a three detector short-baseline neutrino oscillation program in the Fermilab booster neutrino beam, arXiv:1503.01520 [INSPIRE].  
[127] L. Su, L. Wu, N. Zhou and B. Zhu, Accelerated-light-dark-matter-earth inelastic scattering in direct detection, Phys. Rev. D 108 (2023) 035004 [arXiv:2212.02286] [INSPIRE].  
[128] Minefill services, Technical report and updated mineral resource estimate for the Homestake ridge gold project, https://www.dollyvardensilver.com/wp-content/uploads/2022/03/20220120-Homestake-Ridge-Technical-Report-Apex-Geosciences.pdf.  
[129] C. Dey et al., The Homestake gold mine, an early proterozoic iron-formation-hosted gold deposit, Lawrence County, South Dakota, https://pubs.usgs.gov/bul/1857j/report.pdf.  
[130] M. Honda et al., Calculation of atmospheric neutrino flux using the interaction model calibrated with atmospheric muon data, Phys. Rev. D 75 (2007) 043006 [astro-ph/0611418] [INSPIRE].  
[131] M. Honda, T. Kajita, K. Kasahara and S. Midorikawa, Improvement of low energy atmospheric neutrino flux calculation using the JAM nuclear interaction model, Phys. Rev. D 83 (2011) 123001 [arXiv:1102.2688] [INSPIRE].  
[132] M. Honda et al., Atmospheric neutrino flux calculation using the NRLMSISE-00 atmospheric model, Phys. Rev. D 92 (2015) 023004 [arXiv:1502.03916] [INSPIRE].  
[133] M. Honda et al., Atmospheric neutrino flux tables, http://www-rccn.icrr.u-tokyo.ac.jp/mhonda/public/nfIx2014/index.html.  
[134] G. Cowan, K. Cranmer, E. Gross and O. Vitells, Asymptotic formulae for likelihood-based tests of new physics, Eur. Phys. J. C 71 (2011) 1554 [Erratum ibid. 73 (2013) 2501] [arXiv:1007.1727] [INSPIRE].  
[135] R. Brun and F. Rademakers, *ROOT: an object oriented data analysis framework*, Nucl. Instrum. Meth. A 389 (1997) 81 [INSPIRE].  
[136] ROOT webpage, https://github.com/root-project/root/tree/v6-12-06.