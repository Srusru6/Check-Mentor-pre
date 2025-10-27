# Investigating the collinear splitting effects of boosted dark matter at neutrino detectors

Jinmian Li, $^{a}$  Junle Pei $^{b,c}$  and Cong Zhang $^{a}$

$^{a}$ College of Physics, Sichuan University, Chengdu 610065, China  
$^{b}$ Institute of High Energy Physics, Chinese Academy of Sciences, Beijing 100049, China  
c Spallation Neutron Source Science Center, Dongguan 523803, China

E-mail: jmli@scu.edu.cn, peijunle@ihep.ac.cn, zhangcong.phy@gmail.com

ABSTRACT: We study the probing prospects of cosmic ray boosted dark matter (DM) in the framework of simplified electron-philic dark photon model. Focusing on the dark matter and dark photon masses around keV  $\sim$  MeV scale, we consider the bounds obtained from the XENON1T and Super-K experiments. The electron bound state effects are treated carefully in calculating the XENON1T constraint. As for the detection at neutrino detector where the energy threshold is relatively higher, the large logarithmic effects induced by the scale hierarchy between the masses and momentum transfer are considered by introducing the DM parton distribution function (PDF). The logarithmic effects will reduce the electron recoil rate for DM scattering in neutrino detectors. Moreover, we find the DUNE and JUNO experiments provide high sensitivities for probing the dark photon component in the DM PDF through the dark Compton process. We also check the Bullet Cluster constraint on the DM self-scattering cross section.

KEYWORDS: Particle Nature of Dark Matter, Specific BSM Phenomenology, New Light Particles

ARXIV EPRINT: 2209.10816

# Contents

1 Introduction 1  
2 The dark matter parton distribution function 3  
3 Boosted dark matter from cosmic ray acceleration 5  
4 Boosted dark matter scattering with electron 6

4.1 Dark matter direct detection experiments 6  
4.2 Neutrino detector — higher threshold 7

5 Results 9

5.1 Bounds from XENON1T and SuperK 9  
5.2 The photon signal at neutrino detectors 12  
5.3Constraints on DM self-scattering cross section 15

6 Conclusion 16

A Dark matter scattering off bounded electron 17  
B Dark matter scattering off free electron 19

# 1 Introduction

Dark Matter (DM) is one of the most evident new physics beyond the Standard Model (SM). The potential DM signals have been searched in various forms in terms of DM direct detection, indirect detection and collider searches. However, so far these observations which concern the particle properties of DM remain null about the sign of DM. The DM direct detection experiments utilizing the signal of recoiled nucleon or electron from the DM scattering aim to search for the DM in the Galactic halo with characteristic velocities of  $v_{\chi} \sim 10^{-3}c$ . Due to the smallness of the kinetic energy of halo DM, those analyses are most sensitive when the DM mass is comparable to the target mass. They will lose the sensitivities rapidly for DM mass below GeV scale [1].

Recently, it has been pointed out in literature that the halo DM can be boosted in several ways in astrophysics, such as primordial black holes evaporation [2], two-component DM annihilation [3], DM semi-annihilation [4] and so on [5, 6]. This sub-dominant and (near-)relativistic component of DM can produce a detectable signal at direct detection experiment even for DM masses well below  $1\mathrm{GeV}$ . It could be a smoking gun for the DM discovery. In particular, in DM models with freezeout mechanism, the interactions between the DM and the SM particles induce the scattering between the DM and high energy cosmic

ray (CR) particles. The up-scattering of DM particles by CR will inevitably give rise to a non-negligible flux of boosted DM in detect detection experiment [7-20]. Even very light DM particles can deposit large energy at the target detector in this case [21-25]. It has been studied that electronic recoil data at XENON1T detector [26, 27] can be sensitive to the DM with mass around MeV scale [28-33].

Moreover, large-volume neutrino experiments installed deep underground such as Super-K [34], DUNE [35] and JUNO [36] have been considered to probe the boosted DM flux as well. Compared with the DM direct detection, the energy threshold for the signal electron is much higher in those neutrino detectors, which will reject a large amount of DM scattering events. On the other hand, the statistic at neutrino detectors can be regained via the considerably larger size (typically with several kilotons of materials). As a result, the sensitivities of the neutrino detector to the DM models can be complementary to those of the DM direct detections [37-47]. In such scenarios, the energy scale of the DM-SM particle scattering is usually much higher than the mass scale of the DM sector. As has been well known in the SM, the hierarchy between two scales in a process will lead to large logarithms [48-51]. Those large logarithms will give significant contributions to the differential cross section of DM scattering. They need to be resumed using the Dokshitzer-Gribov-Lipatov-Altarelli-Parisi (DGLAP) equations [52-55]. The corresponding scattering cross section can be calculated following the factorization theorem [51].

In this work, based on a simplified version of electron-philic dark photon model with fermionic DM and focusing on the CR up-scattering DM acceleration mechanism, we consider the boosted DM — bounded electron scattering process at the XENON1T detector as well as several neutrino detectors, including Super-K, DUNE and JUNO. In particular, in calculating the electron recoil rate at the XENON1T, we carefully treat the bound state effects of the initial electron. As for the signals at neutrino detectors, we first calculate the DM parton distribution function (PDF) by using the DGLAP equations, and consider the scattering rate between all components in the DM PDF and the electron. The high energy electron recoil signals can be induced by DM, anti-DM and dark photon components, which are stringently constrained by the Super-K data (161.9 kiloton-years exposure) [56]. Furthermore, we find the dark photon component in the DM PDF can induce the dark Compton scattering [57], giving the mono-energetic photon in the final states. Although the Super-K detector which is water Cherenkov based is not able to probe such a monochromatic photon discriminately from electron, future neutrino detectors such as DUNE and JUNO can probe such photons efficiently, as have been studied in ref. [58]. We explicitly calculate the rate for photon signal at those two detectors, and find that this signal provides better sensitivity than the electron recoil signal in the region with relatively light DM and heavy dark photon. The corresponding bounds on DM self-scattering cross section from Bullet Cluster [59–61] are investigated over the parameter regions of interest.

This paper is organized as follows. In section 2, we calculate the DM PDF by solving the DGLAP equations in the simplified dark photon model. In section 3, we estimate the flux of boosted DM that is induced by the cosmic ray up-scattering. The differential recoil rates for DM direct detection experiments and neutrino detectors are calculated in section 4. The corresponding results are shown and discussed in section 5. We conclude our study in

section 6. Moreover, the paper is supplemented with appendices A and B, to provide technical details in calculating the recoil rates for both DM direct detections and neutrino detectors.

# 2 The dark matter parton distribution function

Considering a spacelike branching process  $A \to B + C$ , the four-momentum of particles is chosen as

$$
P _ {A} = \left(E _ {A}, 0, 0, E _ {A} - \frac {m _ {A} ^ {2}}{2 E _ {A}}\right), \tag {2.1}
$$

$$
P _ {B} = \left(z E _ {A}, k _ {T}, 0, z E _ {A} + \frac {k _ {T} ^ {2} - \bar {z} m _ {A} ^ {2} + m _ {C} ^ {2}}{2 \bar {z} E _ {A}}\right), \tag {2.2}
$$

$$
P _ {C} = \left(\bar {z} E _ {A}, - k _ {T}, 0, \bar {z} E _ {A} - \frac {k _ {T} ^ {2} + m _ {C} ^ {2}}{2 \bar {z} E _ {A}}\right), \tag {2.3}
$$

where  $z$  ranges in  $(0, 1)$ ,  $\bar{z} = 1 - z$ , and  $E_A^2 \gg k_T^2$ ,  $m_i^2$  ( $i = A, B, C$ ). By ignoring the terms proportional to  $\frac{k_T^2 \text{ or } m_i^2}{E_A^2}$  ( $i = A, B, C$ ), we can obtain

$$
P _ {A} ^ {2} = m _ {A} ^ {2}, \tag {2.4}
$$

$$
P _ {B} ^ {2} = - \frac {k _ {T} ^ {2} + z m _ {C} ^ {2} - z \bar {z} m _ {A} ^ {2}}{\bar {z}}, \tag {2.5}
$$

$$
P _ {C} ^ {2} = m _ {C} ^ {2}, \tag {2.6}
$$

which means A and C particles are on-shell but B particle is off-shell under the limit of  $E_A^2 \gg k_T^2, m_i^2$  ( $i = A, B, C$ ). The corresponding splitting function can be expressed as

$$
\frac {d \mathcal {P} _ {A \rightarrow B + C}}{d z d k _ {T} ^ {2}} \simeq \frac {1}{N} \frac {1}{1 6 \pi^ {2}} \frac {z \bar {z} | M _ {\mathrm {s p l i t}} | ^ {2}}{\left(k _ {T} ^ {2} + \bar {z} m _ {B} ^ {2} + z m _ {C} ^ {2} - z \bar {z} m _ {A} ^ {2}\right) ^ {2}}, \tag {2.7}
$$

where the matrix-element square  $|M_{\mathrm{split}}|^2$  is computed from the amputated  $A \to B + C$  Feynman diagram with on-shell polarization vectors.  $N = 2$  (1) is taken when  $B$  and  $C$  are identical (non-identical) particles.

In our simplified model with the interaction of

$$
\mathcal {L} \supset g ^ {\prime} A _ {\mu} ^ {\prime} \bar {\chi} \gamma^ {\mu} \chi \tag {2.8}
$$

between Dirac fermion DM  $\chi (\bar{\chi})$  and dark photon  $A^\prime$ , the splitting functions of different spacelike branching processes are summarized in table 1, where  $m_{\chi /A^{\prime}}$  is the mass of  $\chi (A^{\prime})$  particle,  $\alpha^{\prime} = \frac{g^{\prime 2}}{4\pi}$ , and  $A_{T / L}^{\prime}$  denotes the dark photon mode of transverse/longitudinal polarization. All the splitting functions in table 1 have been averaged (summed) over polarizations of the corresponding initial (final) particles. The splitting function of  $\chi /\bar{\chi}\rightarrow$ $\chi /\bar{\chi} +A_{T / L}^{\prime}$  can be obtained by using the relation

$$
P _ {A \rightarrow B + C} (z) = P _ {A \rightarrow C + B} (\bar {z}). \tag {2.9}
$$

Table 1. Splitting functions involving  $\chi ,\bar{\chi }$  ,and  ${A}^{\prime }$  .  

<table><tr><td>A→B+C</td><td>dP_A→B+C/dzdkT2=PA→B+C(z)</td></tr><tr><td>x/χ→AT′+x/χ</td><td>α′/2πkT2z-ξ/2mχ2z2+mχ2A′(1+z2)/kT2+mχ2z2+mχ2A′z</td></tr><tr><td>x/χ→AL′+x/χ</td><td>α′/πkT2mχ2A′z2/z(kT2+mχ2z2+mχ2A′z)2</td></tr><tr><td>A′T→x/χ+χ/χ</td><td>α′/2πkT2z2+z2+ξz(2mχ2+mχ′2(z2+z2))/kT2+mχ−mχ2A′z</td></tr><tr><td>AL′→x/χ+χ/χ</td><td>2α′/πkT2mχ2z2z2/(kT2+mχ−mχ2A′z)2</td></tr></table>

It is noted that terms proportional to  $(k_T^2 +\bar{z} m_B^2 +zm_C^2 -z\bar{z} m_A^2)$  in  $M_{\mathrm{split}}$  that used to calculate the splitting functions of processes involving the longitudinal mode of dark photon have to be eliminated according to the Reference [62].

We use  $f_{i}(k_{T},x)$  to denote the PDF of the particle  $i$  ( $i = \chi, \bar{\chi}, A_{T}^{\prime}, A_{L}^{\prime}$ ) with an energy fraction  $x$  at a factorization scale  $k_{T}$ .  $f_{i}(k_{T},x)$  evolves according to the DGLAP equations<sup>1</sup>

$$
\frac {d f _ {i} \left(k _ {T} , x\right)}{d \ln k _ {T} ^ {2}} = \sum_ {m, n} N \int_ {x} ^ {1} \frac {d z}{z} P _ {m \rightarrow i + n} (z) f _ {m} \left(k _ {T}, \frac {x}{z}\right) - \sum_ {j, k} \int_ {0} ^ {1} d z P _ {i \rightarrow j + k} (z) f _ {i} \left(k _ {T}, x\right), \tag {2.10}
$$

where  $N = 2$  (1) is taken when  $n = i$  ( $n \neq i$ ). The initial conditions of the PDFs are

$$
f _ {i} \left(Q _ {0}, x\right) = \left\{ \begin{array}{l l} \delta (1 - x), & i = \chi \\ 0, & i \neq \chi \end{array} , \quad Q _ {0} = \max  \left(m _ {A ^ {\prime}}, m _ {\chi}\right). \right. \tag {2.11}
$$

In figure 1, we plot the PDFs for  $\chi$ ,  $\bar{\chi}$  and  $A'$  with parameter choices that are most relevant to this work as will be discussed later. Given the DGLAP evolution equation, at a scale  $Q \gg m_{\chi, A'}$ , there are large fractions of energy carried by  $\bar{\chi}$  and  $A'$  in the DM PDF. However, we note that, as the PDFs evolve with  $\ln k_T^2$ , varying the scale within one order of magnitude will not lead to dramatic difference in the PDFs. For  $g' = 1$ , the dark photon fraction  $f_{A'}$  can exceed the DM fraction  $f_{\chi}$  when  $x \lesssim 0.5$ . The anti-DM fraction  $f_{\bar{\chi}}$  becomes comparable to  $f_{\chi}$  for  $x \lesssim 10^{-2}$ . Moreover, lighter  $A'$  not only leads to higher fractions for  $\bar{\chi}$  and  $A'$ , but also gives higher  $f_{\chi}$  in the low  $x$  region. As the coupling approaching the perturbative limit  $g' = 3$ ,  $f_{\chi}$  no longer has the peak around  $x \sim 1$ , due to the intensive splittings. And the dark photon fraction even becomes more important than the DM fraction for  $m_{A'} \lesssim 1$  MeV. It is also interesting to observe that in the region  $x \gtrsim 0.4$ , the dark photon fraction decreases for decreasing  $m_{A'}$ , as opposed to the low  $x$  region.

![](images/b8e90bbdf1b009d0fba545b6376a3bf27bf953fd34ae4a5b42ac86b2f5808319.jpg)  
Figure 1. The PDFs of  $\chi$  (solid line),  $\bar{\chi}$  (dashed line) and  $A^\prime$  (dotted line) at factorization scale of  $100\mathrm{MeV}$ . Different colors indicate the dark photon mass as shown in the legend. The coupling  $g^{\prime} = 1$  in left panel and  $g^{\prime} = 3$  in right panel. The dark matter mass is taken to be  $0.01\mathrm{MeV}$ .

![](images/b7fa0bb69a9f46705179926c37c9fab859e9bafde4eeb93d009110cc08f625bd.jpg)

# 3 Boosted dark matter from cosmic ray acceleration

There are large amounts of energetic cosmic ray (CR) particles in Milk Way halo. DM can be accelerated by its interactions with those particles, obtaining velocity much larger than the escape velocity. We will focus on the DM-electron interaction in this work, i.e., assuming the dark photon interaction is electron-philic

$$
\mathcal {L} \supset \epsilon \times g _ {\mathrm {e m}} A _ {\mu} ^ {\prime} \bar {e} \gamma^ {\mu} e. \tag {3.1}
$$

During the cosmic ray upscattering, the typical momentum transfer is much larger than the momentum of halo DM. So, we assume the halo DM to be at rest.

To give an upscattered DM with kinetic energy  $T_{\chi}$ , the minimal incoming kinetic energy of cosmic electron is [29]

$$
T _ {\mathrm {C R}} ^ {\mathrm {m i n}} = \left(\frac {T _ {\chi}}{2} - m _ {e}\right) \left[ 1 \pm \sqrt {1 + \frac {2 T _ {\chi}}{m _ {\chi}} \frac {(m _ {e} + m _ {\chi}) ^ {2}}{(2 m _ {e} - T _ {\chi}) ^ {2}}} \right], \tag {3.2}
$$

where the  $+$  (-) sign is for  $T_{\chi} > 2m_e$  ( $T_{\chi} < 2m_e$ ).

The recoil flux of CR-induced DM (CRDM) is obtained by convoluting the flux of cosmic electrons  $d\Phi_{e} / dT_{\mathrm{CR}}$  with the DM spectrum  $d\sigma_{\chi e} / dT_{\chi}$  of fixed incident electron energy [64]

$$
\frac {d \Phi_ {\chi}}{d T _ {\chi}} = D _ {\text {e f f}} \frac {\rho_ {\chi} ^ {\text {l o c a l}}}{m _ {\chi}} \int_ {T _ {\mathrm {C R}} ^ {\min }} ^ {\infty} d T _ {\mathrm {C R}} \frac {d \Phi_ {e}}{d T _ {\mathrm {C R}}} \frac {d \sigma_ {\chi e}}{d T _ {\chi}}. \tag {3.3}
$$

In eq. (3.3), the effective distance  $D_{\mathrm{eff}} = 8.02$  kpc is obtained by integrating along the line-of-sight to  $10$  kpc, assuming homogeneous CR distribution and NFW DM halo profile with  $\rho_{\chi}^{\mathrm{local}} = 0.4$  GeV cm $^{-3}$ . The differential flux of cosmic electrons  $d\Phi_e / dT_{\mathrm{CR}} = 4\pi dI / dT_{\mathrm{CR}}$  where the differential intensity of local electrons  $dI / dT_{\mathrm{CR}}$  is simulated by HelMod-4 [65].

![](images/514fa306a1d30fbf724a17466f5c9dd14a1a02004f78e62d60ae24d80a9ac368.jpg)  
Figure 2. Differential CRDM flux for different DM and dark photon masses. The masses are indicated by colors and line types as explained in the legends. In the right panel,  $m_{A'} = 1$  MeV is chosen. For both panels, we have chosen  $g' = 1$  and  $\epsilon = 1$ .

![](images/014ed9115382236767400f599714df0f0fb151694d81ed9de39b35fd1c8c0ecd.jpg)

Finally, the differential cross section for fixed CR kinetic energy  $T_{\mathrm{CR}}$  is [29]

$$
\frac {d \sigma_ {\chi e}}{d T _ {\chi}} = g ^ {\prime 2} (\epsilon g _ {\mathrm {e m}}) ^ {2} \frac {2 m _ {\chi} (m _ {e} + T _ {\mathrm {C R}}) ^ {2} - T _ {\chi} ((m _ {e} + m _ {\chi}) ^ {2} + 2 m _ {\chi} T _ {\mathrm {C R}}) + m _ {\chi} T _ {\chi} ^ {2}}{4 \pi (2 m _ {e} T _ {\mathrm {C R}} + T _ {\mathrm {C R}} ^ {2}) (2 m _ {\chi} T _ {\chi} + m _ {A} ^ {2}) ^ {2}}. \tag {3.4}
$$

In figure 2, we show the differential CRDM fluxes for several different choices of  $m_{\chi}$  and  $m_{A'}$ . In the left panel, for  $m_{\chi} = 10^{-3.5} \mathrm{MeV}$ , the flux is proportional to  $m_{A'}^{-4}$  (for  $m_{A'} \gtrsim 10^{-3} \mathrm{MeV}$ ) in the low  $T_{\chi}$  region and is independent from  $m_{A'}$  in the high  $T_{\chi}$  region. As can be observed in eq. (3.4), this is because the denominator (from the dark photon propagator in the matrix element) is approximate to  $m_{A'}^4$  for small  $T_{\chi}$  and  $(2m_{\chi}T_{\chi})^2$  for large  $T_{\chi}$ , respectively. Similarly, the flux becomes independent of  $m_{A'}$  for  $m_{A'} \lesssim 10^{-4} \mathrm{MeV}$ . For heavier DM case, the flux becomes independent of  $m_{A'}$  at smaller  $m_{A'}$  values, as shown by the dashed curves. Note the dashed green line, dashed red line and dashed blue line are overlapping with each other. In the right panel, we fix  $m_{A'} = 1 \mathrm{MeV}$  and decrease  $m_{\chi}$  from 1 MeV to  $10^{-5} \mathrm{MeV}$ . The sizes of fluxes are similar for all  $m_{\chi}$  when  $T_{\chi} \lesssim 10^{-1} \mathrm{MeV}$ , because the dependence of the differential crossing section on  $m_{\chi}$  is cancelled by the factor of  $1 / m_{\chi}$  in eq. (3.3). For larger  $T_{\chi} \gtrsim 10^2 \mathrm{MeV}$ , the flux firstly increases with decreasing  $m_{\chi}$  and then decreases for  $m_{\chi} \lesssim 10^{-4} \mathrm{MeV}$ . Overall, we can find that the differential flux is more flat for lighter DM and heavier dark photon, i.e., higher fraction of high energy DM. We will focus on this region in current work. Moreover, it should be noted that the flux is proportional to  $\epsilon^2$ . Although we have only shown the case for  $\epsilon = 1$ , fluxes for different  $\epsilon$  can be simply obtained by overall rescaling.

# 4 Boosted dark matter scattering with electron

# 4.1 Dark matter direct detection experiments

The traditional DM direct detections aim to search for non-relativistic halo DM. Those experiments lose the sensitivity for sub-GeV DM due to the small recoil energy. As has been

discussed above, the CR-boosted DM can have sizable rate in some parameter space. It has been studied in many literatures that the electronic recoil data at XENON1T detector is sensitive to the MeV scale CRDM. The scattering between the CRDM and the electrons in xenon atom is described as follows.

A boosted CRDM scattering off an electron in target atom  $(A)$  is described by the ionization process  $\chi + A \rightarrow \chi + A^{+} + e^{-}$ . One can ignore the target atom and consider the initial electron as bound state within the potential of target atom. And the final state electron can be treated as a free particle. So, the process is simplified to  $\chi(p_{1}) + e^{-}(p_{2}) \rightarrow \chi(k_{1}) + e^{-}(k_{2})$ . Those  $p_{1,2}$  and  $k_{1,2}$  in the brackets indicate the four-momentum of particles.

The initial bounded electrons are in energy eigenstates, with binding energy  $E_B^{nl}$  for  $(n,l)$  electron shell of xenon atom. And their three-momentum distributions are given by momentum-space atomic wave function  $\psi_{nlm}(\mathbf{p})$ , which can be obtained by solving Schrodinger equation with given potentials. So, the masses of the bounded electrons can be effectively written as [66]

$$
m _ {\mathrm {e f f}} ^ {2} = \left(m _ {e} - E _ {B} ^ {n l}\right) ^ {2} - \mathbf {p} ^ {2}. \tag {4.1}
$$

The differential cross section with respect to the electron recoil kinetic energy  $T_{R}$  can be expressed by

$$
\begin{array}{l} \frac {d \sigma_ {n l}}{d \ln T _ {R}} = \frac {2 l + 1}{1 6 \cdot (2 \pi) ^ {5}} \frac {T _ {R} | {\bf p _ {2}} |}{E _ {\chi} (m _ {e} - E _ {B} ^ {n l}) | {\bf p _ {1}} |} \left| i M (p _ {1}, p _ {2}, k _ {1}, k _ {2}) \right| ^ {2} \\ \times \left| \chi_ {n l} \left(\left| \mathbf {p} _ {\mathbf {2}} \right|\right) \right| ^ {2} d \phi_ {p _ {2}} d \left| \mathbf {p} _ {\mathbf {2}} \right| d q, \tag {4.2} \\ \end{array}
$$

where  $E_{\chi}(|\mathbf{p_1}|)$  is incident CRDM energy (momentum size),  $\phi_{p_2}(|\mathbf{p_2}|)$  is the initial electron azimuthal angle (momentum size), and  $q$  is the size of momentum transfer in the scattering. The  $\chi_{nl}(|\mathbf{p_2}|)$  is the corresponding radial wave function in momentum space for electron in  $(n,l)$  shell of xenon atom, whose information is available in the reference [67]. The scattering amplitude  $M(p_1,p_2,k_1,k_2)$  describes the underlying new physics. Note that in literature such as reference [29], assuming initial electron to satisfy  $p_2^2 = m_e^2$ , only two parameters  $T_{\chi}$  and  $q$  need to be integrated. While in our case, we consider the initial electron to have effective mass different from  $m_e$ , so there are two additional free parameters to integrate. We take those free parameters to be  $\phi_{p_2}$  and  $|\mathbf{p_2}|$ . More details about the calculation of the amplitude and integration ranges can be found in the appendix A

Finally, the ionization rate [64] can be obtained by convoluting the CRDM flux with the differential cross section

$$
\frac {d R _ {\text {i o n}}}{d \ln T _ {R}} = \sum_ {n l} N _ {T} \int d T _ {\chi} \frac {d \sigma_ {n l}}{d \ln T _ {R}} \frac {d \phi_ {\chi}}{d T _ {\chi}}, \tag {4.3}
$$

where the  $N_{T}$  corresponds to the total number of target atoms in the detector.

# 4.2 Neutrino detector — higher threshold

Comparing to the DM direct detection experiments, the neutrino detectors probe the recoiled electron with much higher kinetic energy threshold, typically larger than  $\mathcal{O}(10)\mathrm{MeV}$ . We will consider the probing prospects of Super-K, DUNE and JUNO experiments to the CRDM in the dark photon model of eq. (2.8) and eq. (3.1).

We will mainly focus on the parameter region, where the masses of the DM and dark photon are much smaller than the typical energy scale of the DM-electron scattering in neutrino detectors. So, the consideration of the DM PDFs becomes necessary. Due to the interaction in eq. (2.8), a boosted DM can induce dark photon and anti-DM densities as well. The parton density for each dark sector species can be obtained by solving the DGLAP equation. All of the components will contribute to the DM-electron scattering. Following the factorization theorem, the differential cross section can be written as

$$
\frac {d \sigma}{d \ln T _ {R}} = \sum_ {i} \int_ {0} ^ {x _ {\operatorname* {m a x}}} d x \frac {d \sigma^ {i}}{d \ln T _ {R}} f _ {i} (Q, x) \Theta \left(x E _ {\chi} ^ {0} - E _ {i} ^ {\min}\right). \tag {4.4}
$$

The index  $i$  runs over DM  $(\chi)$ , anti-DM  $(\bar{\chi})$  and dark photon  $(A')$ , which correspond to the  $\chi + e^{-} \rightarrow \chi + e^{-}$ ,  $\bar{\chi} + e^{-} \rightarrow \bar{\chi} + e^{-}$  and  $A' + e^{-} \rightarrow \gamma + e^{-}$  scattering processes, respectively.  $E_{i}^{\mathrm{min}}$  is the minimal energy of the component  $i$  in incoming DM for producing an electron with recoil kinetic energy  $T_{R}$ . Parton density  $f_{i}(Q, x)$  is obtained by solving DGLAP equations as discussed in the section 2 and the evolution scale  $Q$  is defined as the sum of momentum sizes of final states, e.g., for  $\chi(p_{1}) + e^{-}(p_{2}) \rightarrow \chi(k_{1}) + e^{-}(k_{2})$ ,  $Q = |\vec{k}_{1}| + |\vec{k}_{2}|$ . The lower limit of energy fraction  $x$  is determined by  $xE_{\chi}^{0} - E_{i}^{\mathrm{min}} > 0$ . The upper limit of  $x(x_{\mathrm{max}})$  is related to the  $E_{\chi}^{0}$  and masses. In the limit of  $E_{\chi}^{0} \gg m_{\chi, A'}$ , it can reach  $x_{\mathrm{max}} = 1$ .

The ionization rate of eq. (4.3) can be generalized as

$$
\begin{array}{l} \frac {d R _ {\mathrm {i o n}}}{d \ln T _ {R}} = N _ {T} ^ {S K} \sum_ {i} \int d T _ {\chi} ^ {0} \int_ {0} ^ {x _ {\mathrm {m a x}}} d x \frac {d \sigma^ {i}}{d \ln T _ {R}} f _ {i} (Q, x) \frac {d \phi_ {\chi}}{d T _ {\chi} ^ {0}} \Theta (x E _ {\chi} ^ {0} - E _ {i} ^ {\mathrm {m i n}}) \\ = N _ {T} ^ {S K} \sum_ {i} \int d T _ {i} \int_ {0} ^ {x _ {\max }} d x \frac {1}{x} \frac {d \sigma^ {i}}{d \ln T _ {R}} f _ {i} (Q, x) \frac {d \phi_ {\chi}}{d T _ {\chi} ^ {0}} \Theta \left(T _ {i} + m _ {i} - E _ {i} ^ {\min }\right), \tag {4.5} \\ \end{array}
$$

where a new variable  $T_{i} = xE_{\chi}^{0} - m_{i}$  which is the kinetic energy of component  $i$  in incoming DM has been introduced in the second line. Moreover, the upper limit of the energy fraction  $x$  for  $\chi$ ,  $\bar{\chi}$  and  $A'$  can be calculated by

$$
\frac {T _ {\chi} + m _ {\chi}}{x} (1 - x) > m _ {A ^ {\prime}},
$$

$$
\frac {T _ {\bar {\chi}} + m _ {\chi}}{x} (1 - x) > 2 m _ {\chi}, \tag {4.6}
$$

$$
\frac {T _ {A ^ {\prime}} + m _ {A ^ {\prime}}}{x} (1 - x) > m _ {\chi},
$$

respectively. Those conditions correspond to the minimal requirements for considering mass effects.

We need to emphasize that the mass effects are ignored in the integration bounds of the DGLAP equations, in contrast to the calculation of ionization rate above. Since we focus on the case where the recoil energy is much larger than particle masses, such treatment is still acceptable except for the DM-electron scattering. Applying the first condition of eq. (4.6) clearly removes the phase space in which the DM carries all of the initial energy, i.e.,  $x_{\chi} = 1$ . To include this contribution consistently in our calculation, the integrated

parton density  $\int_{x_{\mathrm{max}}}^{1}f_{\chi}(Q,x)dx$  is taken as the probability of DM with  $x = 1$ . As a result, the ionization rate receives an extra contribution

$$
N _ {T} ^ {S K} \int d T _ {\chi} \frac {d \sigma_ {\chi}}{d \ln T _ {R}} \frac {d \phi_ {\chi}}{d T _ {\chi}} \Theta (T _ {\chi} - T _ {\chi} ^ {\mathrm {m i n}}) \int_ {x _ {\mathrm {m a x}}} ^ {1} f _ {\chi} (Q, x). \tag {4.7}
$$

Considering the DM PDFs, it will be most interesting to observe the scattering between the dark photon and the electron, i.e.  $A' + e^- \rightarrow \gamma + e^-$ . This process is also dubbed as dark Compton scattering [57], in which one can observe the photon in the final states besides the recoiled electron. The corresponding recoil rate is given by

$$
\begin{array}{l} \frac {d R}{d \ln E _ {\gamma}} = N _ {T} ^ {S K} \int d T _ {\chi} ^ {0} \int_ {0} ^ {x _ {\mathrm {m a x}}} d x \frac {d \sigma^ {A ^ {\prime}}}{d \ln E _ {\gamma}} f _ {A ^ {\prime}} (Q, x) \frac {d \phi_ {\chi}}{d T _ {\chi} ^ {0}} \Theta (x E _ {\chi} ^ {0} - E _ {A ^ {\prime} \gamma} ^ {\mathrm {m i n}}) \Theta (E _ {A ^ {\prime} \gamma} ^ {\mathrm {m a x}} - x E _ {\chi} ^ {0}) \\ = N _ {T} ^ {S K} \int d T _ {A ^ {\prime}} \int_ {0} ^ {x _ {\mathrm {m a x}}} d x \frac {1}{x} \frac {d \sigma^ {A ^ {\prime}}}{d \ln E _ {\gamma}} f _ {A ^ {\prime}} (Q, x) \frac {d \phi_ {\chi}}{d T _ {\chi} ^ {0}} \\ \times \Theta \left(T _ {A ^ {\prime}} + m _ {A ^ {\prime}} - E _ {A ^ {\prime} \gamma} ^ {\min }\right) \cdot \Theta \left(E _ {A ^ {\prime} \gamma} ^ {\max } - T _ {A ^ {\prime}} - m _ {A ^ {\prime}}\right), \tag {4.8} \\ \end{array}
$$

where  $E_{A'\gamma}^{\min}$  and  $E_{A'\gamma}^{\max}$  are given in eq. (B.11), and  $x_{\mathrm{max}}$  is constrained by the third equation in eqs. (4.6). More details of the calculation are provided in the appendix B.

# 5 Results

# 5.1 Bounds from XENON1T and SuperK

We have calculated the recoil rate of DM-electron scattering at both DM direct detection experiments and neutrino detectors, in terms of parameters  $m_{\chi}$ ,  $m_{A'}$ ,  $g'$  and  $\epsilon$ . In this section, considering the measurements of electronic recoil data at the XENON1T detector and the Super-Kamiokande as examples, we calculate the corresponding bounds for our simplified model.

For XENON1T experiment, the consistency between the theory and experiment is tested by the  $\chi^2$  [68], which is defined as

$$
\chi^ {2} = \sum_ {i} \frac {\left[ \left(\frac {d R _ {\chi + B _ {0}}}{d T _ {R}}\right) _ {i} - \left(\frac {d R _ {o b s}}{d T _ {R}}\right) _ {i} \right] ^ {2}}{\sigma_ {i} ^ {2}}, \tag {5.1}
$$

where  $\frac{dR_{\chi}}{dT_R}$ ,  $\frac{dR_{B_0}}{dT_R}$  and  $\frac{dR_{obs}}{dT_R}$  are the recoil rates in the  $i$ th bin from theoretical prediction, estimated background and the observation, respectively. The  $\sigma_i$  in the denominator corresponds to the uncertainty in the  $i$ th bin. The event numbers of background and observation in each bin can be found in reference [27]. The  $\chi^2$  value for background only is 46.4. Assuming the test statistic follows a  $\chi^2$  distribution with two degrees of freedom, the  $2\sigma$  bound corresponds to  $\Delta \chi^2 = \chi^2 - \chi_{B_0}^2 = 6.18$ .

For Super-K experiment, an analysis for boosted DM search with electron recoil kinetic energy  $T_{e} > 100\mathrm{MeV}$  has been performed on the data corresponding to 161.9 kiloton-year exposure [56]. The total measured number of events  $N_{\mathrm{sk}}$  is 4042 in the bin

![](images/3c702c23145feb2e552edbd9864eea2f2da027ad6b88abdc7e2038c6883ae5e3.jpg)  
Figure 3. Left panel: exclusion limits of XENON1T (dashed lines) and Super-K (solid lines) in the  $m_{A'} - \epsilon$  plane. The values of  $m_{\chi}$  are indicated by the line colors. Right panel: exclusion limits of XENON1T (dashed lines) and Super-K (solid lines) in the  $m_{\chi} - \epsilon$  plane. The values of  $m_{A'}$  are indicated by the line colors. In both cases, the DM coupling  $g' = 1$ .

![](images/3c730b3c7078d0089b92c85725dcc4dd8352df4c711a8020fe75cf9bee49326b.jpg)

$0.1 < T_{e} / \mathrm{GeV} < 1.33$ . Following the analysis proposed in reference [37], a conservative upper limit on DM signal can be obtained by requiring

$$
\xi \times N _ {\mathrm {D M}} <   N _ {\mathrm {s k}}, \tag {5.2}
$$

where the signal efficiency  $\xi = 0.93$ . The number of DM scattering events  $N_{\mathrm{DM}}$  is calculated by integrating  $\frac{dR_{\mathrm{ion}}}{dT_R}$  over the region  $T_R > 100\mathrm{MeV}$ , with total number of electrons inside the Super-K detector  $N_e = 7.5\times 10^{33}$  and data-taking period of 2628.1 days.

In figure 3, we plot the exclusion limits for XENON1T and Super-K in the  $m_{A'} - \epsilon$  plane and  $m_{\chi} - \epsilon$  plane. In the left panel, it can be observed that the sensitivities of both experiments degrade with increasing dark photon mass, and the degradation of XENON1T sensitivity is severer. This feature can be attributed to the dark photon propagators for both CR-DM scattering and DM-electron scattering. The dark photon propagator contains terms of  $m_{A'}^2$ ,  $2m_{\chi}T_{\chi}$  and  $2m_{e}T_{R}$ . For the recoil rate, each of the two propagators will be suppressed by  $1 / m_{A'}^2$  when  $m_{A'}$  dominates over other terms. The typical energy scale of DM-electron scattering at Super-K experiment is much larger than that at XENON1T experiment. So, the  $m_{A'}$  suppression for Super-K occurs at larger  $m_{A'}$ . In the right panel, given the dark photon mass, both experiments are most sensitive to a certain  $m_{\chi}$  (the specific value depends on  $m_{A'}$ ), while the sensitivities degrade for  $m_{\chi}$  deviating from this value. This feature is mainly attributed to the flux of CRDM, as we have been discussed for the right panel of figure 2, i.e., for a fixed  $m_{A'}$ , in the kinematic region  $T_{\chi} \gtrsim \mathcal{O}(1)\mathrm{MeV}$ , the CRDM flux is highest for a certain value of  $m_{\chi}$ .

Moreover, in the figure 3, we can find that the Super-K experiment is complementary to the XENON1T experiment in exploring the full parameter space. And the Super-K experiment exhibits a stronger bound than the XENON1T experiment in the large  $m_{A'}$  and light  $m_{\chi}$  region. From the left panel, the intersection points (between the solid and dashed lines with the same color) show positive correlation between  $m_{\chi}$  and  $m_{A'}$ . As has been discussed before, for the CRDM flux, the fraction of energetic DM is higher for

![](images/a4c0e31f38e516e5965df59072a8b80b26b12eb9b6dc48ced31e780cc542959a.jpg)  
Figure 4. The ratio between the exclusion limits of Super-K with (denoted by  $\epsilon$ ) and without (denoted by  $\epsilon_0$ ) considering the PDF effects. The ratios for different dark photon masses are indicated by the line colors. The dark matter coupling  $g' = 1$ .

heavier dark photon. Thus, in the heavy dark photon region, the signal rate at Super-K detector is less suppressed by the  $m_{A'}$  than that at XENON1T. Nevertheless, the situation becomes opposite in the light dark photon region, where most CRDM have very small energy, rendering better sensitivity of XENON1T detector.

To emphasize the importance of the DM PDF effects for DM detection at neutrino detector, we plot the ratio between the exclusion limits of Super-K with (denoted by  $\epsilon$ ) and without (denoted by  $\epsilon_0$ ) considering the PDF effects in figure 4. The ratio is shown by  $(\epsilon_0 / \epsilon)^4$  since the recoil rate  $\frac{dR_{\mathrm{ion}}}{d\ln T_R} \propto \epsilon^4$ . The recoil rate without DM PDF effects is calculated from eq. (4.5), by taking into account only the DM component and setting parton density  $f_{\chi} = \delta(1 - x)$  and  $f_{A'} = f_{\bar{\chi}} = 0$ . In the full parameter space, the DM PDF effects always reduce the experimental sensitivity, i.e., the allowed value of  $\epsilon$  is always larger than that of  $\epsilon_0$  for given DM and dark photon masses. The reason is twofold. Firstly, for the DM-electron scattering, the recoil rate is higher for larger incident DM energy. To demonstrate this point, in the left panel of figure 5, we plot the differential recoil rate for several different incident DM kinetic energies, with fixed  $m_{\chi}$ ,  $m_{A'}$ ,  $g'$  and  $\epsilon$ . The features are kept the same for other parameter choices. Including the PDF effects will soften the  $\chi$  spectrum, thus leading to the reduced recoil rate. Secondly, due to the relatively soft CRDM flux and high threshold of Super-K ( $T_R > 100\mathrm{MeV}$ ), the dark photon and anti-DM components can only provide sub-dominant contributions to the electron recoil. As has been discussed above, the CRDM flux deceases quickly for  $T_{\chi} \gtrsim 100\mathrm{MeV}$  in the parameter space of interest and the dark photon/anti-DM density is sizable only in the small  $x$  region.

The feature of ratios in figure 4 can be understood better in terms of two mass limits. The marked region 1 and region 2 in the figure correspond to heavy DM region and light

![](images/821f578c7e1e9ff92246d415d6b6b54c1514bf57871704e56eacf79fd6450283.jpg)  
Figure 5. Left panel: the differential recoil rate with fixed incident DM kinetic energy as indicated in the legend, where we have chosen  $m_{\chi} = 0.32 \mathrm{MeV}$ ,  $m_{A'} = 10 \mathrm{MeV}$ ,  $g' = 1$  and  $\epsilon = 1$ . Right panel: the differential recoil rate for three different values of  $m_{A'}$ , where we have taken incident DM kinetic energy  $T_{\chi} = 1255 \mathrm{MeV}$ ,  $m_{\chi} = 0.32 \mathrm{MeV}$ ,  $g' = 1$  and  $\epsilon = 1$ .

![](images/a50ff467e410c073d3247710cc6ec5dd4cf06cb11f15f4fb53784a75323d94e2.jpg)

DM region, respectively. In the region 1, the CRDM flux (in the high  $T_{\chi}$  region) is almost the same for different  $m_{A'}$ , as shown by dashed lines in the left panel of figure 2. On the contrary, as shown in the right panel of figure 5, the fraction of events with  $T_{R} > 100 \mathrm{MeV}$  is higher for heavier dark photon, especially when  $m_{A'} \gtrsim 1 \mathrm{MeV}$ . This means that the typical energy scale of DM-electron scattering for heavier dark photon case is higher, leading to more significant PDF effects. As the dark photon/anti-DM contributions are subdominant and the energy spectrum of DM component is softened by the PDF effects, the recoil rate is strongly suppressed when the dark photon is heavy. In the region 2, the ratio of recoil rates is most close to 1 when  $m_{A'} \sim 1 \mathrm{MeV}$  and decreases as the  $m_{A'}$  deviates from  $1 \mathrm{MeV}$ . For dark photon mass heavier than  $1 \mathrm{MeV}$ , the ratio decreases with increasing  $m_{A'}$ , due to the similar reason as discussed for region 1. As for dark photon mass below  $1 \mathrm{MeV}$ , the feature is mainly determined by the flux of CRDM. The CRDM flux is more flat for heavier  $m_{A'}$  as shown in the left panel of figure 2, i.e., higher fraction of energetic DM. The distribution of recoil energy has strong dependence on the DM kinetic energy in the region  $T_{\chi} \lesssim 10^{3} \mathrm{MeV}$ , as shown in the left panel of figure 5. So, the PDF effects are most significant when the signal DM flux is dominated by the DM with  $T_{\chi} \sim \mathcal{O}(100) \mathrm{MeV}$  (this is the case for lighter dark photon). Furthermore, the flux also becomes more flat when  $m_{\chi}$  decreases, so the ratio increases as decreasing  $m_{\chi}$ .

# 5.2 The photon signal at neutrino detectors

Besides the recoiled electron signal, the dark photon component can induce mono-energetic photon final state through the dark Compton scattering  $A^{\prime}e \rightarrow \gamma e$ . It has been found that the dark Compton scattering has a substantial impact on the reach and discovery potential of direct detection experiments for bosonic DM [57].

In figure 6, we show the differential recoil rate for the outgoing photon induced by the dark photon component in the DM PDF at the Super-K detector, where we also plot the corresponding differential recoil rate for the recoiled electron for comparison. The parameter

![](images/8324c5c2ff9fd0e1d1d7c8191d8367ca8132222e1664d737e55454217d3f74ea.jpg)  
Figure 6. The differential recoil rate (at Super-K with data taking of 2628.1 days) for recoiled electron without DM PDF effects (solid line), with DM PDF effects (dashed line) and for the outgoing photon (dotted line), where we have taken fixed dark photon mass as indicated in the legend, DM mass  $m_{\chi} = 0.01 \mathrm{MeV}$ , signal efficiency  $\xi = 0.93$  and the  $\epsilon$  is chosen as the maximal value that satisfies the XENON1T and Super-K bounds. Left panel: DM coupling  $g' = 1$ ; Right panel: DM coupling  $g' = 3$ .

![](images/c238ab2a5559d78ec98fbfbe98069407db7be218f0cd405e560de0ce12560cb2.jpg)

choices are explained in the caption, in particular the  $\epsilon$  values are chosen as the maximal values that satisfy the XENON1T and Super-K bounds, which are  $1.92 \times 10^{-4}$ ,  $1.59 \times 10^{-5}$  and  $1.56 \times 10^{-6}$  for  $m_{A'} = 1\mathrm{MeV}$ ,  $m_{A'} = 0.1\mathrm{MeV}$  and  $m_{A'} = 0.01\mathrm{MeV}$ , respectively. In the left panel, the DM coupling is chosen as  $g' = 1$  such that the DM PDF effects are mild. For the  $m_{A'} = 1\mathrm{MeV}$  case (blue lines), the Super-K poses a stronger bound than the XENON1T due to the electron recoil. At the Super-K, it can produce 4042 recoiled electrons with  $T_R > 100\mathrm{MeV}$  and 40519.8 outgoing photons with  $T_R > 1\mathrm{MeV}$ . For the  $m_{A'} = 0.1\mathrm{MeV}$  case (red lines), the XENON1T poses a stronger bound instead. At the Super-K, such parameter choice can lead to 0.30 recoiled electrons with  $T_R > 100\mathrm{MeV}$  and 119.56 outgoing photons with  $T_R > 1\mathrm{MeV}$ . As for the third case  $m_{A'} = 0.01\mathrm{MeV}$ , XENON1T constraint is much stronger than the Super-K constraint. The numbers of both recoiled electrons and outgoing photons are small at Super-K detector, i.e.,  $2.56 \times 10^{-5}$  and 0.022 for electrons with  $T_R > 100\mathrm{MeV}$  and photons with  $T_R > 1\mathrm{MeV}$ . The rate of mono-energetic photon can be further enhanced for larger DM coupling  $g'$  as shown in the right panel of figure 6. $^2$  Firstly, the flux of CRDM is proportional to  $g'^2$ . The rates of both the signal electron and photon are enhanced, leading to a stronger limit on  $\epsilon$ . Secondly, although the ratio  $(\epsilon_0 / \epsilon)^4$  (as shown in figure 4) is always greater than  $\mathcal{O}(0.1)$  for  $g' = 1$ , it can be reduced to  $\lesssim \mathcal{O}(10^{-2})$  for  $g' = 3$ . It means that the calculated exclusion limits without considering the DM PDFs are considerably over-estimated. Thirdly, the ratio between the numbers of signal photons and signal electrons can be significantly enhanced by the large  $g'$ . As a result, the mono-energetic photon signal may provide a much better experimental sensitivity than the recoiled electron when  $g'$  is large.

However, the Super-K is water-based Cherenkov detectors, where the Cherenkov rings induced by photons and electrons are similar. It is not possible to identify the mono-energetic

![](images/0c9bfb69dac9801c7283822ed146299dfd8cde7c3f05b26a268deaa1ff7e4560.jpg)

![](images/d92fe00cc2e8bd074cd724a35ef1220b80d19c8ea0a9e2b331133de185c68209.jpg)

![](images/3e06b012ed63a2d028e2db8ccc715d6e9d447b8400e414255f13905a1170510d.jpg)  
Figure 7. The orange shaded regions and cyan shaded regions correspond to the Super-K and XENON1T bounds. The DM self-interaction constraints are shown by hatched vertical lines, and regions on the left-hand side are excluded. The blue lines and red lines correspond to the contours of three signal photon events in each year at DUNE and JUNO, respectively. The threshold of the photon detection is indicated by the line types as explained in the legend. We choose four different DM masses for demonstration, the values of which are given in the titles of plots.

![](images/eb6b3c13ff7f7f8cf55a4cb881ca3238084a93f686016dc728727375cecee881.jpg)

photon with threshold  $\mathcal{O}(1) \sim \mathcal{O}(10)$  MeV. On the other hand, as discussed in reference [58], DUNE and JUNO detectors have the capacity of high efficiency photon identification, which enable us to identify the mono-energetic photon with a much lower threshold. Moreover, such an energetic single photon signal at DUNE and JUNO can be treated as background free, which means an event rate of a few can lead to the exclusion/discovery.

In figure 7, we plot the contours of three signal photon events per year at DUNE and JUNO experiments in the  $m_{A'} - \epsilon$  plane, assuming two different photon energy thresholds for each experiment. For DUNE detector, considering the single phase LArTPC module, we calculate the sensitivity reach with active LAr of 40 kilotons, which corresponds to  $1.085 \times 10^{34}$  electrons inside the detector. The JUNO experiment will be equipped with liquid scintillator (2,5-diphenyloxazole) detector with fiducial mass of 20 kilotons, so that the total number of electrons inside the detector is  $6.314 \times 10^{33}$ . For simplicity, we assume the detection efficiencies of energetic photon of both detectors to be unity. From figure 7,

we can find that the features of DUNE and JUNO sensitivities are similar, and the DUNE provides slightly better sensitivity than the JUNO due to a larger number of electrons in the detector. Figure 7 also shows that the photon component in DM PDFs provides an efficient and complementary way to discover the DM sector, especially in the parameter space with relatively heavy dark photon and light DM. It should be noted that although we have shown the exclusion curves of DUNE and JUNO with dark photon mass up to  $100\mathrm{MeV}$ , the limits in the region  $m_{A'} \gtrsim \mathcal{O}(10)$  MeV may suffer from large uncertainty. Because the condition of  $E_{\chi} \gg m_{A'}$  in PDF calculation (see discussions in section 2) may not be fully satisfied.

# 5.3 Constraints on DM self-scattering cross section

The light mediator as well as sizeable coupling lead to remarkable DM self-scattering, the cross-section of which could be constrained by Bullet Cluster [59-61] and other cosmological simulations with self-interacting DM on the scales of galaxies and galaxy clusters [69, 70].<sup>3</sup> The general bound is  $\sigma_{\mathrm{self}} / m_{\chi} < 1 \, \mathrm{cm}^2/\mathrm{g}$ . In our case, the DM self-interaction is mediated by the dark photon. The cross section of the scattering between  $\chi$  and  $\bar{\chi}$  in the non-relativistic limit is determined by the attractive Yukawa potential

$$
V (r) = - \alpha^ {\prime} \frac {e ^ {- m _ {A ^ {\prime}} r}}{r}, \tag {5.3}
$$

where  $\alpha' = g'^2 / (4\pi)$ . With  $\delta_l$  being the phase shift for a partial wave  $l$ , the scattering amplitude can be expressed as

$$
f (\theta) = \frac {2}{m _ {\chi} v} \sum_ {l = 0} ^ {\infty} (2 l + 1) e ^ {i \delta_ {l}} P _ {l} (\cos \theta) \sin \delta_ {l}, \tag {5.4}
$$

where  $v$  ( $v \ll 1$ ) is the relative velocity between  $\chi$  and  $\bar{\chi}$  in the scattering. We use the transfer cross section  $\sigma_{\mathrm{T}}$  to describe this scattering [75], which is defined as

$$
\begin{array}{l} \sigma_ {\mathrm {T}} = \int d \Omega (1 - \cos \theta) | f (\theta) | ^ {2} (5.5) \\ = \frac {1 6 \pi}{m _ {\chi} ^ {2} v ^ {2}} \sum_ {\ell = 0} ^ {\infty} (\ell + 1) \sin^ {2} \left(\delta_ {\ell + 1} - \delta_ {\ell}\right). (5.6) \\ \end{array}
$$

The characteristic velocity on cluster scales is around  $1000\mathrm{km / s}$ . Instead of numerically solving the Schrödinger equation with the potential  $V(r)$  to obtain  $\delta_{l}$  and then  $\sigma_{\mathrm{T}}$  with too much time cost, the improved analytical expression for the DM self-interacting cross section which takes into account the Born level effects proposed in [76, 77] can be used to estimate  $\sigma_{\mathrm{T}}$  quickly.

In figure 7, the lower limits on the dark photon mass from DM self-scattering constraints are indicated by the hatched vertical lines. Although we have calculated the bounds with the full analytical expression, the parameter regions around the hatched lines are in the

Born regime since  $\alpha^{\prime}m_{\chi} / m_{A^{\prime}}\lesssim 1$ . In the Born regime the analytical expression for  $\sigma_{\mathrm{T}}$  can be simplified to

$$
\sigma_ {\mathrm {T}} ^ {\mathrm {B o r n}} = \frac {8 \pi \alpha^ {\prime 2}}{m _ {\chi} ^ {2} v ^ {4}} \left(\ln \left(1 + 4 t ^ {2}\right) - \frac {4 t ^ {2}}{1 + 4 t ^ {2}}\right) \tag {5.7}
$$

$$
\stackrel {t \leqslant 1} {=} \frac {g ^ {\prime 4}}{4 \pi} \frac {m _ {\chi} ^ {2}}{m _ {A ^ {\prime}} ^ {4}}, \tag {5.8}
$$

where  $t = m_{\chi}v / (2m_{A'})$ . Given the dark matter coupling  $g' = 1$ , the lower bounds on the dark photon mass vary as  $(m_{\chi})^{1/4}$ , which are 8.582 MeV, 3.619 MeV, 1.526 MeV and 0.644 MeV for  $m_{\chi} = 10^{-0.5}$  MeV, 10 $^{-2}$  MeV, 10 $^{-3.5}$  MeV and 10 $^{-5}$  MeV, respectively.

# 6 Conclusion

In this work, we study the constraints and detection prospects of the boosted DM at DM direct detection experiments and neutrino detectors. A simplified electron-philic dark photon model with fermionic DM is considered. In the model, the DM can be accelerated through its scattering with high energy CR particles. We find that the spectrum of CRDM flux is more flat in the region with relatively heavy dark photon and light DM, such that the DM with energy well above the detector threshold could still provide non-negligible contribution to the DM-electron scattering. Since the energy threshold of neutrino detectors is around  $\mathcal{O}(10 - 100)\mathrm{MeV}$ , the parameter space with  $m_{A^{\prime}}$ ,  $m_{\chi} \in [1\mathrm{keV}, 1\mathrm{MeV}]$  is investigated in detail.

In calculating the electron recoil rate at the XENON1T, we consider carefully the bound state effects of the initial electron by introducing the effective mass and atomic wave function. Due to the low energy threshold of the detector, it is most sensitive to the parameter space with light  $m_{A'}$  where the coupling  $\epsilon$  as small as  $10^{-7}$  is excluded.

The calculation at neutrino detector is more complicated, due to the hierarchy between the mass of DM and the energy scale of the DM-electron scattering. It will lead to large logarithms which significantly affect the differential cross section of the DM scattering. The DGLAP equation is adopted for resummation of those large logarithms, producing the DM PDFs. The high energy electron recoil signals can be induced by all of the DM, anti-DM and dark photon components in the DM PDFs, which are found to be stringently constrained by the Super-K data. Especially in the region with relative light DM and heavy dark photon, the Super-K constraint is much stronger than the XENON1T constraint. Moreover, we find the PDF effects would reduce the electron recoil rate at the neutrino detectors, thus relaxing the corresponding bounds. The reduction on the rate is  $\sim \mathcal{O}(0.1)$  for DM coupling  $g^{\prime} = 1$  and can reach as small as  $10^{-2}$  for DM coupling  $g^{\prime} = 3$ .

We also point out for the first time that the dark photon component in the DM PDFs can induce the dark Compton scattering. It can produce a mono-energetic photon in the final states, which can be probed efficiently in future neutrino detectors such as DUNE and JUNO. In terms of coupling  $\epsilon$ , the constraints obtained from the mono-energetic photon at the DUNE and JUNO detectors are around one order of magnitude stronger than those obtained from the electron recoil signal at the Super-K.

The parameter regions of interest are stringently constrained by simulations of the Bullet Cluster and other galaxy clusters due to strong DM self-interaction. Adopting the improved analytical expression for the DM self-scattering cross section, and applying the bound of  $\sigma_{\mathrm{self}} / m_{\chi} < 1\mathrm{cm}^2 /\mathrm{g}$ , we find the neutrino detectors can have better sensitivities in the region with relatively heavier dark photon, e.g.  $m_{A'}\gtrsim 1$  MeV for  $m_{\chi}\lesssim 10^{-4}$  MeV.

Finally, we note that the simplified electron-philic dark photon model adopted in the current work is by no means complete. In particular, the DM is overabundant in most regions of interest where the DM is lighter than the dark photon. In this case, the annihilation channel  $\chi \chi \rightarrow A' A'$  is kinematically forbidden, and the dark matter dominantly annihilates through the process  $\chi \chi \rightarrow A' \rightarrow e^{+} e^{-}$  in the early universe. Given the  $m_{A'} > m_{\chi} \sim \mathcal{O}(1)$  MeV,  $g' \sim 1$  and  $\epsilon \sim 10^{-4}$ , the DM relic density can be as high as  $10^{4}$ . However, this problem can be easily solved by either introducing new couplings of  $A'$  to light SM particles such as neutrinos or introducing new mediator particles such as dark Higgs boson.

# Acknowledgments

This work was supported by the National Natural Science Foundation of China under grant No. 11905149.

# A Dark matter scattering off bounded electron

For a relativistic CRDM scattering off an electron with effective mass  $m_{\mathrm{eff}}$ ,  $\chi(p_1) + e^- (p_2) \rightarrow \chi(k_1) + e^- (k_2)$ , the differential cross section can be expressed as

$$
\begin{array}{l} d \sigma = \sum_ {n l m s} \frac {1}{2 E _ {\chi} 2 \left(m _ {e} - E _ {B} ^ {n l}\right)} \frac {d ^ {3} k _ {2}}{(2 \pi) ^ {3} 2 E _ {k _ {2}}} \frac {d ^ {3} k _ {1}}{(2 \pi) ^ {3} 2 E _ {k _ {1}}} \frac {d ^ {3} p _ {2}}{(2 \pi) ^ {3}} (2 \pi) ^ {4} \delta^ {4} \left(p _ {1} + p _ {2} - k _ {1} - k _ {2}\right) \tag {A.1} \\ \times \left| i M \left(\mathbf {p _ {1}}, \mathbf {p _ {2}}, \mathbf {k _ {1}}, \mathbf {k _ {2}}\right) \right| ^ {2} \left| \psi_ {n l m} \left(\mathbf {p _ {2}}\right) \right| ^ {2}, \\ \end{array}
$$

where the wave function of initial bounded electron in momentum space  $\psi_{nlm}(\mathbf{p_2}) = \chi_{nl}(|\mathbf{p_2}|)Y_{lm}(\hat{\mathbf{p}}_2)$  with the normalization  $\int d^3 p_2|\psi_{nlm}(\mathbf{p_2})|^2 = (2\pi)^3$ .  $\chi_{nl}(|\mathbf{p_2}|)$  is radial wave function in momentum space and  $Y_{lm}(\hat{\mathbf{p}}_2)$  is the spherical harmonic function.

The radial wave function in coordinate space can be obtained by the RHF method. Here, we adopt the expressions provided in reference [29]. Summing over the magnetic quantum number  $m$  and the spin  $s$  for each  $(n,l)$ , and using the property of harmonics function  $\sum_{m=-l}^{+l}|Y_{lm}(\hat{\mathbf{p}}_2)|^2 = \frac{2l + 1}{4\pi}$ , we get

$$
\begin{array}{l} d \sigma = \sum_ {n l} \frac {1}{2 E _ {\chi} 2 \left(m _ {e} - E _ {B} ^ {n l}\right)} \frac {d ^ {3} k _ {2}}{(2 \pi) ^ {3} 2 E _ {k _ {2}}} \frac {d ^ {3} k _ {1}}{(2 \pi) ^ {3} 2 E _ {k _ {1}}} \frac {d ^ {3} p _ {2}}{(2 \pi) ^ {3}} (2 \pi) ^ {4} \delta^ {4} \left(p _ {1} + p _ {2} - k _ {1} - k _ {2}\right) \tag {A.2} \\ \times \left| i M \left(\mathbf {p _ {1}}, \mathbf {p _ {2}}, \mathbf {k _ {1}}, \mathbf {k _ {2}}\right) \right| ^ {2} \left| \chi_ {n l} (p _ {2}) \right| ^ {2} \frac {2 l + 1}{2 \pi}. \\ \end{array}
$$

In order to simplify the integration, we apply the variable substitutions as follows

$$
\begin{array}{l} \mathrm {p h a s e s p a c e} = d ^ {3} p _ {2} d ^ {3} k _ {1} d ^ {3} k _ {2} \delta^ {4} (p _ {1} + p _ {2} - k _ {1} - k _ {2}) \\ = \frac {1}{4 \pi} d \Omega_ {p _ {1}} d ^ {3} p _ {2} d ^ {3} k _ {1} d ^ {3} k _ {2} d ^ {3} q \delta (p _ {1} ^ {0} + p _ {2} ^ {0} - k _ {1} ^ {0} - k _ {2} ^ {0}) \delta^ {3} (\vec {p _ {1}} - \vec {k _ {1}} - \vec {q}) \delta^ {3} (\vec {k _ {2}} - \vec {p _ {2}} - \vec {q}) \\ = \frac {1}{4 \pi} d \Omega_ {p _ {1}} d ^ {3} p _ {2} d ^ {3} k _ {2} d ^ {3} q \delta^ {3} (\vec {k} _ {2} - \vec {p} _ {2} - \vec {q}) \delta \left(p _ {1} ^ {0} + p _ {2} ^ {0} - k _ {1} ^ {0} - k _ {2} ^ {0}\right), \tag {A.3} \\ \end{array}
$$

where we have introduced an extra integration over solid angle  $\Omega_{p_1}$  divided by  $4\pi$ . This corresponds to the global rotation of the reference frame, which does not change the result.

Then, the four-momentum of the DM and the electron can be parameterized by  $(p_i$  and  $k_{i}$  denote  $|\mathbf{p_i}|$  and  $(|{\bf k_i}|)$  respectively in the following discussion)

$$
p _ {1} ^ {\mu} = \left(E _ {\chi}, p _ {1} \sin \theta_ {p _ {1}}, 0, p _ {1} \cos \theta_ {p _ {1}}\right),
$$

$$
p _ {2} ^ {\mu} = \left(m _ {e} - E _ {B} ^ {n l}, p _ {2} \sin \theta_ {p _ {2}} \cos \phi_ {p _ {2}}, p _ {2} \sin \theta_ {p _ {2}} \sin \phi_ {p _ {2}}, p _ {2} \cos \theta_ {p _ {2}}\right), \tag {A.4}
$$

$$
k _ {1} ^ {\mu} = \left(E _ {\chi} ^ {\prime}, p _ {1} \sin \theta_ {p _ {1}}, 0, p _ {1} \cos \theta_ {p _ {1}} - q\right),
$$

$$
k _ {2} ^ {\mu} = \left(m _ {e} + T _ {R}, k _ {2} \sin \theta_ {k _ {2}} \cos \phi_ {k _ {2}}, k _ {2} \sin \theta_ {k _ {2}} \sin \phi_ {k _ {2}}, k _ {2} \cos \theta_ {k _ {2}}\right).
$$

We have chosen the  $\vec{q}$  along the  $z$ -axes and  $\vec{p_1}$  in the  $x - z$  plane by gauge fixing constraints  $\delta (\phi_q - 0)$ ,  $\delta (\theta_q - 0)$  and  $\delta (\phi_{p_1} - 0)$ . In this parameterization, the conversation laws  $\delta^3 (\vec{k}_2 - \vec{p}_2 - \vec{q})$  and  $\delta (p_1^0 +p_2^0 -k_1^0 -k_2^0)$ , as well as the on-shell constraints have not been imposed. However, the conservation law  $\delta^3 (\vec{p_1} -\vec{k_1} -\vec{q})$  can be satisfied automatically.

To proceed with the integration, those delta functions are transformed as

$$
\begin{array}{l} \delta^ {3} \left(\vec {k} _ {2} - \vec {p} _ {2} - \vec {q}\right) = \frac {1}{k _ {2} ^ {2}} \delta \left(k _ {2} - \sqrt {p _ {2} ^ {2} + q ^ {2} + 2 p _ {2} q \cos \theta_ {p _ {2}}}\right) \delta \left(\cos \theta_ {k _ {2}} - \frac {k _ {2} ^ {2} + q ^ {2} - p _ {2} ^ {2}}{2 k _ {2} q}\right) \delta \left(\phi_ {k _ {2}} - \phi_ {p _ {2}}\right) \\ = \frac {1}{k _ {2} p _ {2} q} \delta \left(\cos \theta_ {p _ {2}} - \frac {k _ {2} ^ {2} - p _ {2} ^ {2} - q ^ {2}}{2 p _ {2} q}\right) \delta \left(\cos \theta_ {k _ {2}} - \frac {k _ {2} ^ {2} + q ^ {2} - p _ {2} ^ {2}}{2 k _ {2} q}\right) \delta \left(\phi_ {k _ {2}} - \phi_ {p _ {2}}\right), \tag {A.5} \\ \end{array}
$$

$$
\begin{array}{l} \delta (p _ {1} ^ {0} + p _ {2} ^ {0} - k _ {1} ^ {0} - k _ {2} ^ {0}) = \delta \left(\sqrt {p _ {1} ^ {2} + m _ {\chi} ^ {2}} - \sqrt {m _ {\chi} ^ {2} + p _ {1} ^ {2} + q ^ {2} - 2 p _ {1} q \cos \theta_ {p _ {1}}} - \Delta E _ {e}\right) \\ = \frac {E _ {k _ {1}}}{p _ {1} q} \delta \left(\cos \theta_ {p _ {1}} - \frac {q ^ {2} - \Delta E _ {e} \left(\Delta E _ {e} - 2 E _ {\chi}\right)}{2 q \sqrt {E _ {\chi} ^ {2} - m _ {\chi} ^ {2}}}\right), \tag {A.6} \\ \end{array}
$$

where  $\Delta E_{e} = T_{R} + E_{B}^{nl}$  and  $E_{k_1}\equiv k_1^0\equiv E_\chi '$ . Using eq. (A.5) and eq. (A.6), the differential phase space element in eq. (A.3) becomes

$$
\begin{array}{l} \mathrm {p h a s e s p a c e} = \frac {1}{4 \pi} p _ {2} ^ {2} k _ {2} ^ {2} q ^ {2} \frac {1}{k _ {2} p _ {2} q} \frac {E _ {k _ {1}}}{p _ {1} q} d \phi_ {p _ {1}} d \phi_ {p _ {2}} d \Omega_ {q} d p _ {2} d k _ {2} d q \\ = 2 \pi \frac {E _ {k _ {1}} k _ {2} p _ {2}}{p _ {1}} d \phi_ {p _ {2}} d p _ {2} d k _ {2} d q \\ = 2 \pi \frac {\left(T _ {R} + m _ {e}\right) T _ {R} E _ {k _ {1}} p _ {2}}{p _ {1}} d \phi_ {p _ {2}} d p _ {2} d q d \ln T _ {R}, \tag {A.7} \\ \end{array}
$$

where the integration variables  $\phi_{p_1}$  and  $\Omega_q$  correspond to the global rotation of interaction plane around the  $z$ -axis and the global rotation of the  $\vec{q}$ , respectively. After considering all

momentum conservation constraints and on-shell conditions, only  $\phi_{p_2}, p_2, q, T_R$  and  $T_{\chi}(p_1)$  are left as free parameters.

The integration bounds for those parameters are determined by the conditions  $-1 \leq \cos \theta_{p_2}$ ,  $\cos \theta_{k_2}$ ,  $\cos \theta_{p_1} \leq 1$  and  $\phi_{p_2} \in (0, 2\pi)$ . The conditions  $-1 \leq \cos \theta_{p_2}$ ,  $\cos \theta_{k_2} \leq 1$  require  $q \in (|k_2 - p_2|, |k_2 + p_2|)$ , and the  $-1 \leq \cos \theta_{p_1} \leq 1$  gives

$$
p _ {1} > p _ {1} ^ {\mathrm {m i n}} = \frac {q}{2} + \frac {\Delta E _ {e}}{2 (q ^ {2} - \Delta E _ {e} ^ {2})} \sqrt {(q ^ {2} - \Delta E _ {e} ^ {2}) (q ^ {2} - \Delta E _ {e} ^ {2} + 4 m _ {\chi} ^ {2})}, q > \Delta E _ {e}. \quad \mathrm {(A . 8)}
$$

As a result, for given  $\ln T_R$ , the integration bounds are

$$
p _ {2} \in (0, m _ {e} - E _ {n l} ^ {B}),
$$

$$
q \in \left(\Delta E _ {e}, + \infty\right) \cap \left(| k _ {2} - p _ {2} |, | k _ {2} + p _ {2} |\right), \tag {A.9}
$$

$$
T _ {\chi} \in \left(T _ {\chi} ^ {\min } (q), \infty\right),
$$

where  $T_{\chi}^{\mathrm{min}}(q)$  is calculated by eq. (A.8) using on-shell condition. Note that for the  $p_2$  bound, we also require the electron effective mass to be a real number.

Furthermore, using the four-momentum parameterizations in eq. (A.4), eq. (A.5) and eq. (A.6), the matrix element square can be calculated as

$$
\left| i M \right| ^ {2} = 2 g ^ {\prime 2} \left(\epsilon g _ {\mathrm {e m}}\right) ^ {2} \times \frac {A}{\left(t - m _ {A} ^ {2}\right) ^ {2}}, \tag {A.10}
$$

where

$$
\begin{array}{l} A = t \left(m _ {e} ^ {2} + 2 m _ {e} m _ {\mathrm {e f f}} - m _ {\mathrm {e f f}} ^ {2} + 2 m _ {\chi} ^ {2} - 4 p _ {1} ^ {\mu} k _ {2, \mu}\right) - 2 m _ {\chi} ^ {2} \left(m _ {e} - m _ {\mathrm {e f f}}\right) ^ {2} \\ - 4 p _ {1} ^ {\mu} k _ {2, \mu} \left(m _ {e} ^ {2} - m _ {\text {e f f}} ^ {2}\right) + 8 \left(p _ {1} ^ {\mu} k _ {2, \mu}\right) ^ {2} + t ^ {2}, \tag {A.11} \\ \end{array}
$$

with  $t = \Delta E_e^2 - q^2$  is the four-momentum transfer. Finally, we obtain the differential cross section in eq. (A.2) and eq. (4.3) as

$$
d \sigma = \frac {2 l + 1}{1 6 (2 \pi) ^ {5}} \frac {T _ {R} p _ {2}}{E _ {\chi} (m _ {e} - E _ {B} ^ {n l}) p _ {1}} | i M (\mathbf {p _ {1}}, \mathbf {p _ {2}}, \mathbf {k _ {1}}, \mathbf {k _ {2}}) | ^ {2} | \chi_ {n l} (p _ {2}) | ^ {2} d \phi_ {p _ {2}} d p _ {2} d q d \ln T _ {R}. \quad \mathrm {(A . 1 2)}
$$

# B Dark matter scattering off free electron

In neutrino detectors, the momentum transfer of signal process is much larger than the typical momentum of the initial electron in the atom. So, the initial electron can be approximated to be rest.

The cross section for a boosted DM/dark photon scattering off a free electron  $(\chi /A^{\prime}(p_1) + e^{-}(p_2)\to \chi /\gamma (k_1) + e^{-}(k_2))$  is given by

$$
d \sigma = \frac {1}{2 E _ {\text {i n}} 2 m _ {e}} \frac {d ^ {3} k _ {2}}{(2 \pi) ^ {3} 2 E _ {k _ {2}}} \frac {d ^ {3} k _ {1}}{(2 \pi) ^ {3} 2 E _ {k _ {1}}} (2 \pi) ^ {4} \delta^ {4} \left(p _ {1} + p _ {2} - k _ {1} - k _ {2}\right)\left| i M \left(p _ {1}, p _ {2} \rightarrow k _ {1}, k _ {2}\right)\right| ^ {2}, \tag {B.1}
$$

where  $E_{\mathrm{in}} = E_{\chi}$  and  $E_{A'}$  for initial DM and dark photon, respectively.

For the DM-electron scattering, we choose the momentum transfer  $\vec{q} = \vec{k}_2 = \vec{p}_1 - \vec{k}_1$  alone the  $z$ -axes and  $\vec{p}_1$  in  $x-z$  plane. Considering the three momentum conservation  $\vec{p}_1 + \vec{p}_2 - \vec{k}_1 - \vec{k}_2 = 0$ , the four-momentum of initial and final state particles can be parameterized as

$$
p _ {1} ^ {\mu} = \left(E _ {\chi}, p _ {1} \sin \theta_ {p _ {1}}, 0, p _ {1} \cos \theta_ {p _ {1}}\right)
$$

$$
p _ {2} ^ {\mu} = \left(m _ {e}, 0, 0, 0\right) \tag {B.2}
$$

$$
k _ {1} ^ {\mu} = \left(E _ {\chi} - T _ {R}, p _ {1} \sin \theta_ {p _ {1}}, 0, p _ {1} \cos \theta_ {p _ {1}} - k _ {2}\right)
$$

$$
k _ {2} ^ {\mu} = (m _ {e} + T _ {R}, 0, 0, k _ {2})
$$

Then the differential phase space element in eq. (B.1) can be simplified to

$$
\begin{array}{l} d ^ {3} k _ {1} d ^ {3} k _ {2} \delta^ {4} (p _ {1} + p _ {2} - k _ {1} - k _ {2}) = \frac {1}{4 \pi} d \Omega_ {p _ {1}} d ^ {3} k _ {2} \delta (p _ {1} ^ {0} + p _ {2} ^ {0} - k _ {1} ^ {0} - k _ {2} ^ {0}) \\ = \frac {1}{4 \pi} d \Omega_ {p _ {1}} d ^ {3} k _ {2} \delta \left(E _ {\chi} - T _ {R} - \sqrt {p _ {1} ^ {2} + k _ {2} ^ {2} - 2 p _ {1} k _ {2} \cos \theta_ {p _ {1}} + m _ {\chi} ^ {2}}\right) \\ = \frac {1}{4 \pi} d \Omega_ {p _ {1}} d ^ {3} k _ {2} \frac {E _ {\chi} - T _ {R}}{p _ {1} k _ {2}} \delta \left(\cos \theta_ {p _ {1}} - \frac {k _ {2} ^ {2} - T _ {R} \left(T _ {R} - 2 E _ {\chi}\right)}{2 k _ {2} \sqrt {E _ {\chi} ^ {2} - m _ {\chi} ^ {2}}}\right) \\ = \frac {1}{4 \pi} d \Omega_ {p _ {1}} d \Omega_ {k _ {2}} k _ {2} ^ {2} d k _ {2} \frac {E _ {\chi} - T _ {R}}{p _ {1} k _ {2}} \delta \left(\cos \theta_ {p _ {1}} - \frac {k _ {2} ^ {2} - T _ {R} (T _ {R} - 2 E _ {\chi})}{2 k _ {2} \sqrt {E _ {\chi} ^ {2} - m _ {\chi} ^ {2}}}\right) \\ = 2 \pi \frac {\left(E _ {\chi} - T _ {R}\right) \left(T _ {R} + m _ {e}\right) T _ {R}}{p _ {1}} d \ln T _ {R}. \tag {B.3} \\ \end{array}
$$

In the last line, the solid angles  $\Omega_{p_1}$  and  $\Omega_{k_2}$  which correspond to the global rotation of the reference frame have been integrated out.

The lower bound of the incident DM kinetic energy for producing a given  $T_{R}$  can be obtained from the condition  $-1\leq \cos \theta_{p_1} = \frac{k_2^2 - T_R(T_R - 2E_\chi)}{2k_2\sqrt{E_\chi^2 - m_\chi^2}}\leq 1$  as shown in the third line of eq. (B.3), which is

$$
T _ {\chi} > T _ {\chi} ^ {\mathrm {m i n}} = \left(\frac {T _ {R}}{2} - m _ {\chi}\right) \left[ 1 \pm \sqrt {1 + \frac {2 T _ {R}}{m _ {e}} \frac {(m _ {e} + m _ {\chi}) ^ {2}}{(2 m _ {\chi} - T _ {R}) ^ {2}}} \right], \qquad \mathrm {(B . 4)}
$$

where the  $+(-)$  sign is used for  $T_{R} > 2m_{\chi}$  ( $T_{R} < 2m_{\chi}$ ).

For dark photon scattering off electron  $A'(p_1) + e^- (p_2) \to \gamma (k_1) + e^- (k_2)$ , concerning the electron recoil energy, we choose  $\vec{q} = \vec{k}_2 = \vec{p}_1 - \vec{k}_1$  alone  $z$ -axes, and  $\vec{p}_1$  in  $x-z$  plane as the same with the DM scattering. As a result, the parameterizations of the four-momentum of initial and final state particles are similar as those shown in eq. (B.2), with the subscript

$\chi$  replaced by  $A^{\prime}$ . And the differential phase space element is given by

$$
\begin{array}{l} d ^ {3} k _ {1} d ^ {3} k _ {2} \delta^ {4} (p _ {1} + p _ {2} - k _ {1} - k _ {2}) = \frac {1}{4 \pi} d \Omega_ {p _ {1}} d ^ {3} k _ {2} \delta (p _ {1} ^ {0} + p _ {2} ^ {0} - k _ {1} ^ {0} - k _ {2} ^ {0}) \\ = \frac {1}{4 \pi} d \Omega_ {p _ {1}} d ^ {3} k _ {2} \delta \left(E _ {A ^ {\prime}} - T _ {R} - \sqrt {p _ {1} ^ {2} + k _ {2} ^ {2} - 2 p _ {1} k _ {2} \cos \theta_ {p _ {1}}}\right) \\ = \frac {1}{4 \pi} d \Omega_ {p _ {1}} d ^ {3} k _ {2} \frac {E _ {A ^ {\prime}} - T _ {R}}{p _ {1} k _ {2}} \delta \left(\cos \theta_ {p _ {1}} - \frac {- m _ {A ^ {\prime}} ^ {2} + k _ {2} ^ {2} - T _ {R} \left(T _ {R} - 2 E _ {A ^ {\prime}}\right)}{2 k _ {2} \sqrt {E _ {A ^ {\prime}} ^ {2} - m _ {A ^ {\prime}} ^ {2}}}\right) \\ = \frac {1}{4 \pi} d \Omega_ {p _ {1}} d \Omega_ {k _ {2}} k _ {2} ^ {2} d k _ {2} \frac {E _ {A ^ {\prime}} - T _ {R}}{p _ {1} k _ {2}} \delta \left(\cos \theta_ {p _ {1}} - \frac {- m _ {A ^ {\prime}} ^ {2} + k _ {2} ^ {2} - T _ {R} \left(T _ {R} - 2 E _ {A ^ {\prime}}\right)}{2 k _ {2} \sqrt {E _ {A ^ {\prime}} ^ {2} - m _ {A ^ {\prime}} ^ {2}}}\right) \\ = 2 \pi \frac {\left(E _ {\chi} - T _ {R}\right) \left(T _ {R} + m _ {e}\right) T _ {R}}{p _ {1}} d \ln T _ {R}. \tag {B.5} \\ \end{array}
$$

Similarly, the lower bound of the incident dark photon kinetic energy for producing a given  $T_{R}$  can be obtained from the condition  $-1 \leq \cos \theta_{p_1} = \frac{-m_{A'}^2 + k_2^2 - T_R(T_R - 2E_{A'})}{2k_2\sqrt{E_{A'}^2 - m_{A'}^2}} \leq 1$  as shown in the fourth line of eq. (B.5):

$$
\begin{array}{l} T _ {A ^ {\prime}} > T _ {A ^ {\prime}} ^ {\mathrm {m i n}} = \frac {- m _ {A ^ {\prime}} ^ {2} - 4 m _ {A ^ {\prime}} m _ {e} + 2 m _ {e} T _ {R}}{4 m _ {e}} \\ + \frac {1}{4} \sqrt {\frac {2 m _ {A ^ {\prime}} ^ {4} m _ {e} + m _ {A ^ {\prime}} ^ {4} T _ {R} + 8 m _ {A ^ {\prime}} ^ {2} m _ {e} ^ {2} T _ {R} + 4 m _ {A ^ {\prime}} ^ {2} m _ {e} T _ {R} ^ {2} + 8 m _ {e} ^ {3} T _ {R} ^ {2} + 4 m _ {e} ^ {2} T _ {R} ^ {3}}{m _ {e} ^ {2} T _ {R}}}. \tag {B.6} \\ \end{array}
$$

Finally, for dark photon scattering off electron  $A'(p_1) + e^- (p_2) \to \gamma (k_1) + e^- (k_2)$  while concerning the outgoing photon energy, the same reference frame is chosen, i.e.,  $\vec{q}$  along  $z$ -axes and  $\vec{p}_1$  in  $x-z$  plane. Considering the three-momentum conservation  $\vec{q} - \vec{k}_2 = 0$ , the four-momentum of initial and final state particles can be parameterized as

$$
p _ {1} = \left(E _ {A ^ {\prime}}, p _ {1} \sin \theta_ {p _ {1}}, 0, p _ {1} \cos \theta_ {p _ {1}}\right)
$$

$$
p _ {2} = \left(m _ {e}, 0, 0, 0\right) \tag {B.7}
$$

$$
k _ {1} = \left(E _ {\gamma}, E _ {\gamma} \sin \theta_ {k _ {1}} \cos \phi_ {k _ {1}}, E _ {\gamma} \sin \theta_ {k _ {1}} \sin \phi_ {k _ {1}}, E _ {\gamma} \cos \theta_ {k _ {1}}\right)
$$

$$
k _ {2} = \left(E _ {A ^ {\prime}} + m _ {e} - E _ {\gamma}, 0, 0, q\right)
$$

where  $p_1 = \sqrt{E_{A'} - m_{A'}^2}$ . And the differential phase space element is expressed by

$$
\begin{array}{l} d ^ {3} k _ {1} d ^ {3} k _ {2} \delta \left(p _ {1} ^ {0} + p _ {2} ^ {0} - k _ {1} ^ {0} - k _ {2} ^ {0}\right) \delta^ {3} \left(\vec {p} _ {1} + \vec {p} _ {2} - \vec {k} _ {1} - \vec {k} _ {2}\right) \\ = \frac {d \Omega_ {p _ {1}}}{4 \pi} d ^ {3} k _ {1} d ^ {3} k _ {2} d ^ {3} q \delta \left(p _ {1} ^ {0} + p _ {2} ^ {0} - k _ {1} ^ {0} - k _ {2} ^ {0}\right) \delta^ {3} (\vec {p} _ {1} - \vec {k} _ {1} - \vec {q}) \delta^ {3} (\vec {k} _ {2} - \vec {q}) \tag {B.8} \\ = \frac {d \Omega_ {p _ {1}}}{4 \pi} d ^ {3} k _ {1} d ^ {3} q \delta \left(p _ {1} ^ {0} + p _ {2} ^ {0} - k _ {1} ^ {0} - k _ {2} ^ {0}\right) \delta^ {3} \left(\vec {p _ {1}} - \vec {k _ {1}} - \vec {q}\right), \\ \end{array}
$$

where the delta functions can be transformed as

$$
\begin{array}{l} \delta^ {3} \left(\vec {p} _ {1} - \vec {k} _ {1} - \vec {q}\right) \\ = \frac {1}{p _ {1} ^ {2}} \delta \left(p _ {1} - \sqrt {E _ {\gamma} ^ {2} + q ^ {2} + 2 q E _ {\gamma} \cos \theta_ {k _ {1}}}\right) \delta \left(\cos \theta_ {p _ {1}} - \frac {p _ {1} ^ {2} + q ^ {2} - E _ {\gamma} ^ {2}}{2 p _ {1} q}\right) \delta \left(0 - \phi_ {k _ {1}}\right) \\ = \frac {1}{p _ {1} q E _ {\gamma}} \delta \left(\cos \theta_ {k _ {1}} - \frac {p _ {1} ^ {2} - E _ {\gamma} ^ {2} - q ^ {2}}{2 q E _ {\gamma}}\right) \delta \left(\cos \theta_ {p _ {1}} - \frac {p _ {1} ^ {2} + q ^ {2} - E _ {\gamma} ^ {2}}{2 p _ {1} q}\right) \delta \left(0 - \phi_ {k _ {1}}\right), \\ \end{array}
$$

$$
\begin{array}{l} \delta (p _ {1} ^ {0} + p _ {2} ^ {0} - k _ {1} ^ {0} - k _ {2} ^ {0}) = \delta \left((E _ {A ^ {\prime}} + m _ {e} - E _ {\gamma}) - \sqrt {q ^ {2} + m _ {e} ^ {2}}\right) \\ = \frac {E _ {A ^ {\prime}} + m _ {e} - E _ {\gamma}}{q} \delta \left(q - \sqrt {\left(E _ {A ^ {\prime}} + m _ {e} - E _ {\gamma}\right) ^ {2} - m _ {e} ^ {2}}\right) \tag {B.9} \\ \end{array}
$$

So, the eq. (B.8) can be further simplified to

$$
\begin{array}{l} \text {p h a s e} = \frac {E _ {\gamma} ^ {2} \left(E _ {A ^ {\prime}} + m _ {e} - E _ {\gamma}\right)}{4 \pi p _ {1}} d \Omega_ {q} d \phi_ {p _ {1}} d \ln E _ {\gamma} \tag {B.10} \\ = 2 \pi \frac {E _ {\gamma} ^ {2} \left(E _ {A ^ {\prime}} + m _ {e} - E _ {\gamma}\right)}{p _ {1}} d \ln E _ {\gamma} \\ \end{array}
$$

The lower and upper bounds of the incident dark photon energy for producing a given photon energy  $E_{\gamma}$  can be obtained from the condition  $-1 \leq \cos \theta_{k_1}, \cos \theta_{p_1} \leq 1$  and  $q \in \mathcal{R}$  as shown in the delta functions of eq. (B.9), which are

$$
E _ {A ^ {\prime}} \in \left\{ \begin{array}{l l} \left(E _ {A ^ {\prime}} ^ {-}, E _ {A ^ {\prime}} ^ {+}\right) & m _ {A ^ {\prime}} <   m _ {e} \text {a n d} \frac {- m _ {A ^ {\prime}} ^ {2} + 2 m _ {A ^ {\prime}} m _ {e}}{2 m _ {e}} <   E _ {\gamma} <   \frac {m _ {e}}{2} \\ \left(E _ {A ^ {\prime}} ^ {+}, \infty\right) & E _ {\gamma} > \frac {m _ {e}}{2} \end{array} , \right. \tag {B.11}
$$

where  $E_{A'}^-$  and  $E_{A'}^+$  are defined as the following

$$
\begin{array}{l} E _ {A ^ {\prime}} ^ {\pm} = \frac {(E _ {\gamma} - m _ {e}) (- m _ {A ^ {\prime}} ^ {2} + 2 E _ {\gamma} m _ {e})}{(2 E _ {\gamma} - m _ {e}) 2 m _ {e}} \\ \pm \frac {E _ {\gamma}}{2 m _ {e}} \sqrt {\frac {\left(m _ {A ^ {\prime}} ^ {2} + 2 E _ {\gamma} m _ {e} - 2 m _ {A ^ {\prime}} m _ {e}\right) \left(m _ {A ^ {\prime}} ^ {2} + 2 \left(E _ {\gamma} + m _ {A ^ {\prime}}\right) m _ {e}\right)}{\left(- 2 E _ {\gamma} + m _ {e}\right) ^ {2}}}. \tag {B.12} \\ \end{array}
$$

Note that in our case, we only focus on the branch with  $E_{\gamma} > \frac{m_e}{2}$ .

The only unknown ingredient of the cross section in eq. (B.1) is the matrix element square. The matrix element squares for the DM-electron scattering with respect to the recoiled electron kinetic energy  $|iM_{\chi e}^{e}|^{2}$ , the dark photon-electron scattering with respect to the recoiled electron kinetic energy  $|iM_{A^{\prime}e}^{e}|^{2}$  as well as the dark photon-electron scattering with respect to the outgoing photon energy  $|iM_{A^{\prime}e}^{\gamma}|^{2}$  can be calculated as

$$
| i M _ {\chi e} ^ {e} | ^ {2} = 2 g ^ {\prime 2} (\epsilon g _ {\mathrm {e m}}) ^ {2} \frac {2 (s (t - 2 m _ {e} ^ {2} - 2 m _ {\chi} ^ {2}) + (m _ {e} ^ {2} + m _ {\chi} ^ {2}) ^ {2} + s ^ {2}) + t ^ {2}}{(t - m _ {A ^ {\prime}} ^ {2}) ^ {2}}, \tag {B.13}
$$

$$
\begin{array}{l} | i M _ {A ^ {\prime} e} ^ {e} | ^ {2} = \frac {4}{3} (\epsilon g _ {\mathrm {e m}}) ^ {2} g _ {\mathrm {e m}} ^ {2} \frac {1}{(m _ {e} ^ {2} - s) ^ {2} (m _ {e} ^ {2} - u) ^ {2}} \times \{- 2 m _ {A ^ {\prime}} ^ {4} (m _ {e} ^ {2} - s) (m _ {e} ^ {2} - u) \\ + 2 m _ {A ^ {\prime}} ^ {2} (m _ {e} ^ {4} (s + u) - 4 m _ {e} ^ {2} s u + s u (s + u)) + 6 m _ {e} ^ {8} - m _ {e} ^ {4} (3 s ^ {2} + 1 4 s u + 3 u ^ {2}) \\ + m _ {e} ^ {2} (s + u) \left(s ^ {2} + 6 s u + u ^ {2}\right) - s u \left(s ^ {2} + u ^ {2}\right) \}, \tag {B.14} \\ \end{array}
$$

$$
\left| i M _ {A ^ {\prime} e} ^ {\gamma} \right| ^ {2} = \left| i M _ {A ^ {\prime} e} ^ {e} \right| ^ {2}, \tag {B.15}
$$

where the Mandelstam variables  $s, t, u$  for each process are defined as

$$
\begin{array}{r l} {i M _ {\chi e} ^ {e}:} & {\left\{ \begin{array}{l l} s = (m _ {\chi} + m _ {e}) ^ {2} + 2 m _ {e} T _ {\chi} \\ t = - 2 m _ {e} T _ {R} \end{array} \right.,} \end{array}
$$

$$
i M _ {A ^ {\prime} e} ^ {e}: \left\{ \begin{array}{l} s = \left(m _ {A ^ {\prime}} + m _ {e}\right) ^ {2} + 2 m _ {e} T _ {A ^ {\prime}} \\ u = m _ {e} ^ {2} - 2 m _ {e} \left(m _ {A ^ {\prime}} + T _ {A ^ {\prime}} - T _ {R}\right), \end{array} \right. \tag {B.16}
$$

$$
\begin{array}{l l} i M _ {A ^ {\prime} e} ^ {\gamma}: & \left\{ \begin{array}{l} s = (m _ {A ^ {\prime}} + m _ {e}) ^ {2} + 2 m _ {e} T _ {A ^ {\prime}} \\ u = m _ {e} ^ {2} - 2 m _ {e} E _ {\gamma} \end{array} \right.. \end{array}
$$

Combining the matrix elements with the phase space elements, we obtain the differential cross sections for all of the processes

$$
\frac {d \sigma_ {\chi e} ^ {e}}{d \ln T _ {R}} = \frac {1}{3 2 \pi} \frac {T _ {R}}{p _ {1} E _ {\chi} m _ {e}} | i M _ {\chi e} ^ {e} | ^ {2},
$$

$$
\frac {d \sigma_ {A ^ {\prime} e} ^ {e}}{d \ln E _ {\gamma}} = \frac {1}{3 2 \pi} \frac {T _ {R}}{p _ {1} E _ {A ^ {\prime}} m _ {e}} | i M _ {A ^ {\prime} e} ^ {e} | ^ {2}, \tag {B.17}
$$

$$
\frac {d \sigma_ {A ^ {\prime} e} ^ {\gamma}}{d \ln E _ {\gamma}} = \frac {1}{3 2 \pi} \frac {E _ {\gamma}}{p _ {1} E _ {A ^ {\prime}} m _ {e}} | i M _ {A ^ {\prime} e} ^ {\gamma} | ^ {2}.
$$

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.  $\mathrm{SCOAP}^3$  supports the goals of the International Year of Basic Sciences for Sustainable Development.

# References

[1] T. Marrodán Undagoitia and L. Rauch, Dark matter direct-detection experiments, J. Phys. G 43 (2016) 013001 [arXiv:1509.08767] [INSPIRE].  
[2] B. Carr, K. Kohri, Y. Sendouda and J. Yokoyama, Constraints on primordial black holes, Rept. Prog. Phys. 84 (2021) 116902 [arXiv:2002.12778] [INSPIRE].  
[3] K. Agashe, Y. Cui, L. Necib and J. Thaler, (In)direct Detection of Boosted Dark Matter, JCAP 10 (2014) 062 [arXiv:1405.7370] [INSPIRE].  
[4] F. D'Eramo and J. Thaler, Semi-annihilation of Dark Matter, JHEP 06 (2010) 109 [arXiv:1003.5912] [INSPIRE].  
[5] J. Jaeckel and W. Yin, Boosted Neutrinos and Relativistic Dark Particles as Messengers from Reheating, JCAP 02 (2021) 044 [arXiv:2007.15006] [INSPIRE].  
[6] G. Herrera and A. Ibarra, Direct detection of non-galactic light dark matter, Phys. Lett. B 820 (2021) 136551 [arXiv:2104.04445] [INSPIRE].  
[7] T. Bringmann and M. Pospelov, Novel direct detection constraints on light dark matter, Phys. Rev. Lett. 122 (2019) 171801 [arXiv:1810.10543] [INSPIRE].  
[8] C.V. Cappiello, K.C.Y. Ng and J.F. Beacom, Reverse Direct Detection: Cosmic Ray Scattering With Light Dark Matter, Phys. Rev. D 99 (2019) 063004 [arXiv:1810.07705] [INSPIRE].  
[9] W. Yin, Highly-boosted dark matter and cutoff for cosmic-ray neutrinos through neutrino portal, EPJ Web Conf. 208 (2019) 04003 [arXiv:1809.08610] [INSPIRE].

[10] V.V. Flambaum, L. Su, L. Wu and B. Zhu, Constraining sub-GeV dark matter from Migdal and Boosted effects, arXiv:2012.09751 [INSPIRE].  
[11] PANDAX-II collaboration, Search for Cosmic-Ray Boosted Sub-GeV Dark Matter at the PandaX-II Experiment, Phys. Rev. Lett. 128 (2022) 171801 [arXiv:2112.08957] [INSPIRE].  
[12] C. Xia, Y.-H. Xu and Y.-F. Zhou, Production and attenuation of cosmic-ray boosted dark matter, JCAP 02 (2022) 028 [arXiv:2111.05559] [INSPIRE].  
[13] J. Bramante, B.J. Kavanagh and N. Raj, Scattering Searches for Dark Matter in Subhalos: Neutron Stars, Cosmic Rays, and Old Rocks, Phys. Rev. Lett. 128 (2022) 231801 [arXiv:2109.04582] [INSPIRE].  
[14] Y. Jho, J.-C. Park, S.C. Park and P.-Y. Tseng, *Cosmic-Neutrino-Boosted Dark Matter (νBDM)*, arXiv:2101.11262 [INSPIRE].  
[15] J.-C. Feng, X.-W. Kang, C.-T. Lu, Y.-L.S. Tsai and F.-S. Zhang, Revising inelastic dark matter direct detection by including the cosmic ray acceleration, JHEP 04 (2022) 080 [arXiv:2110.08863] [INSPIRE].  
[16] Y. Chen et al., Earth Shielding and Daily Modulation from Electrophilic Boosted Dark Particles, arXiv:2110.09685 [INSPIRE].  
[17] G. Elor, R. McGehee and A. Pierce, Maximizing Direct Detection with Highly Interactive Particle Relic Dark Matter, Phys. Rev. Lett. 130 (2023) 031803 [arXiv:2112.03920] [INSPIRE].  
[18] C. Xia, Y.-H. Xu and Y.-F. Zhou, Azimuthal asymmetry in cosmic-ray boosted dark matter flux, arXiv:2206.11454 [INSPIRE].  
[19] D. Bardhan, S. Bhowmick, D. Ghosh, A. Guha and D. Sachdeva, Bounds on boosted dark matter from direct detection: The role of energy-dependent cross sections, Phys. Rev. D 107 (2023) 015010 [arXiv:2208.09405] [INSPIRE].  
[20] J. Alvey, T. Bringmann and H. Kolesova, No room to hide: implications of cosmic-ray upscattering for GeV-scale dark matter, JHEP 01 (2023) 123 [arXiv:2209.03360] [INSPIRE].  
[21] S.-F. Ge, J. Liu, Q. Yuan and N. Zhou, Diurnal Effect of Sub-GeV Dark Matter Boosted by Cosmic Rays, Phys. Rev. Lett. 126 (2021) 091804 [arXiv:2005.09480] [INSPIRE].  
[22] Z.-H. Lei, J. Tang and B.-L. Zhang, Constraints on cosmic-ray boosted dark matter in CDEX-10, Chin. Phys. C 46 (2022) 085103 [arXiv:2008.07116] [INSPIRE].  
[23] J.B. Dent, B. Dutta, J.L. Newstead and I.M. Shoemaker, Bounds on Cosmic Ray-Boosted Dark Matter in Simplified Models and its Corresponding Neutrino-Floor, Phys. Rev. D 101 (2020) 116007 [arXiv:1907.03782] [INSPIRE].  
[24] W. Cho, K.-Y. Choi and S.M. Yoo, Searching for boosted dark matter mediated by a new gauge boson, Phys. Rev. D 102 (2020) 095010 [arXiv:2007.04555] [INSPIRE].  
[25] W. Wang, L. Wu, W.-N. Yang and B. Zhu, The Spin-dependent Scattering of Boosted Dark Matter, arXiv:2111.04000 [INSPIRE].  
[26] XENON collaboration, Light Dark Matter Search with Ionization Signals in XENON1T, Phys. Rev. Lett. 123 (2019) 251801 [arXiv:1907.11485] [INSPIRE].  
[27] XENON collaboration, Excess electronic recoil events in XENON1T, Phys. Rev. D 102 (2020) 072004 [arXiv:2006.09721] [INSPIRE].

[28] W. Wang, L. Wu, J.M. Yang, H. Zhou and B. Zhu, Cosmic ray boosted sub-GeV gravitationally interacting dark matter in direct detection, JHEP 12 (2020) 072 [Erratum ibid. 02 (2021) 052] [arXiv:1912.09904] [INSPIRE].  
[29] Q.-H. Cao, R. Ding and Q.-F. Xiang, Searching for sub-MeV boosted dark matter from xenon electron direct detection, Chin. Phys. C 45 (2021) 045002 [arXiv:2006.12767] [INSPIRE].  
[30] Y. Jho, J.-C. Park, S.C. Park and P.-Y. Tseng, Leptonic New Force and Cosmic-ray Boosted Dark Matter for the XENON1T Excess, Phys. Lett. B 811 (2020) 135863 [arXiv:2006.13910] [INSPIRE].  
[31] T. Emken, J. Frerick, S. Heeba and F. Kahlhoefer, *Electron recoils from terrestrial upscattering of inelastic dark matter*, Phys. Rev. D 105 (2022) 055023 [arXiv:2112.06930] [INSPIRE].  
[32] A. Das and M. Sen, Boosted dark matter from diffuse supernova neutrinos, Phys. Rev. D 104 (2021) 075029 [arXiv:2104.00027] [INSPIRE].  
[33] C. Xia, Y.-H. Xu and Y.-F. Zhou, Constraining light dark matter upscattered by ultrahigh-energy cosmic rays, Nucl. Phys. B 969 (2021) 115470 [arXiv:2009.00353] [INSPIRE].  
[34] SUPER-KAMIOKANDE collaboration, The Super-Kamiokande detector, Nucl. Instrum. Meth. A 501 (2003) 418 [INSPIRE].  
[35] DUNE collaboration, Deep Underground Neutrino Experiment (DUNE), Far Detector Technical Design Report, Volume II: DUNE Physics, Tech. Rep. FERMILAB-PUB-20-025-ND (2020) [arXiv:2002.03005] [INSPIRE].  
[36] JUNO collaboration, JUNO physics and detector, Prog. Part. Nucl. Phys. 123 (2022) 103927 [arXiv:2104.02565] [INSPIRE].  
[37] Y. Ema, F. Sala and R. Sato, Light Dark Matter at Neutrino Experiments, Phys. Rev. Lett. 122 (2019) 181802 [arXiv:1811.00520] [INSPIRE].  
[38] C.V. Cappiello and J.F. Beacom, *Strong New Limits on Light Dark Matter from Neutrino Experiments*, Phys. Rev. D 100 (2019) 103011 [Erratum ibid. **104** (2021) 069901] [arXiv:1906.11283] [INSPIRE].  
[39] J. Berger et al., Prospects for detecting boosted dark matter in DUNE through hadronic interactions, Phys. Rev. D 103 (2021) 095012 [arXiv:1912.05558] [INSPIRE].  
[40] D. Kim, P.A.N. Machado, J.-C. Park and S. Shin, Optimizing Energetic Light Dark Matter Searches in Dark Matter and Neutrino Experiments, JHEP 07 (2020) 057 [arXiv:2003.07369] [INSPIRE].  
[41] G. Guo, Y.-L.S. Tsai and M.-R. Wu, Probing cosmic-ray accelerated light dark matter with IceCube, JCAP 10 (2020) 049 [arXiv:2004.03161] [INSPIRE].  
[42] A. De Roeck, D. Kim, Z.G. Moghaddam, J.-C. Park, S. Shin and L.H. Whitehead, Probing Energetic Light Dark Matter with Multi-Particle Tracks Signatures at DUNE, JHEP 11 (2020) 043 [arXiv:2005.08979] [INSPIRE].  
[43] R. Harnik, R. Plestid, M. Pospelov and H. Ramani, Millicharged cosmic rays and low recoil detectors, Phys. Rev. D 103 (2021) 075029 [arXiv:2010.11190] [INSPIRE].  
[44] Y. Ema, F. Sala and R. Sato, Neutrino experiments probe hadrophilic light dark matter, SciPost Phys. 10 (2021) 072 [arXiv:2011.01939] [INSPIRE].  
[45] J.B. Dent, B. Dutta, J.L. Newstead, I.M. Shoemaker and N.T. Arellano, Present and future status of light dark matter models from cosmic-ray electron upscattering, Phys. Rev. D 103 (2021) 095015 [arXiv:2010.09749] [INSPIRE].

[46] A. Granelli, P. Ullio and J.-W. Wang, *Blazar-boosted dark matter at Super-Kamiokande*, JCAP 07 (2022) 013 [arXiv:2202.07598] [INSPIRE].  
[47] J. Berger et al., Snowmass 2021 White Paper: Cosmogenic Dark Matter and Exotic Particle Searches in Neutrino Experiments, in 2022 Snowmass Summer Study, (2022) [arXiv:2207.02882] [INSPIRE].  
[48] M. Ciafaloni, P. Ciafaloni and D. Comelli, Bloch-Nordsieck violating electroweak corrections to inclusive TeV scale hard processes, Phys. Rev. Lett. 84 (2000) 4810 [hep-ph/0001142] [INSPIRE].  
[49] P. Ciafaloni, D. Comelli and A. Vergine, Sudakov electroweak effects in transversely polarized beams, JHEP 07 (2004) 039 [hep-ph/0311260] [INSPIRE].  
[50] P. Ciafaloni and D. Comelli, Electroweak evolution equations, JHEP 11 (2005) 022 [hep-ph/0505047] [INSPIRE].  
[51] T. Han, Y. Ma and K. Xie, High energy leptonic collisions and electroweak parton distribution functions, Phys. Rev. D 103 (2021) L031301 [arXiv:2007.14300] [INSPIRE].  
[52] V.N. Gribov and L.N. Lipatov, Deep inelastic e p scattering in perturbation theory, Sov. J. Nucl. Phys. 15 (1972) 438 [INSPIRE].  
[53] L.N. Lipatov, The parton model and perturbation theory, Yad. Fiz. 20 (1974) 181 [INSPIRE].  
[54] G. Altarelli and G. Parisi, Asymptotic Freedom in Parton Language, Nucl. Phys. B 126 (1977) 298 [INSPIRE].  
[55] Y.L. Dokshitzer, Calculation of the Structure Functions for Deep Inelastic Scattering and  $e^{+}e^{-}$  Annihilation by Perturbation Theory in Quantum Chromodynamics, Sov. Phys. JETP 46 (1977) 641 [INSPIRE].  
[56] SUPER-KAMIOKANDE collaboration, Search for Boosted Dark Matter Interacting With Electrons in Super-Kamiokande, Phys. Rev. Lett. 120 (2018) 221301 [arXiv:1711.05278] [INSPIRE].  
[57] Y. Hochberg, B. von Krosigk, E. Kuflik and T.C. Yu, Impact of Dark Compton Scattering on Direct Dark Matter Absorption Searches, Phys. Rev. Lett. 128 (2022) 191801 [arXiv:2109.08168] [INSPIRE].  
[58] Y. Cui, J.-L. Kuo, J. Pradler and Y.-D. Tsai, Shining light on cosmogenic axions with neutrino experiments, Phys. Rev. D 106 (2022) 115024 [arXiv:2207.13107] [INSPIRE].  
[59] M. Markevitch et al., Direct constraints on the dark matter self-interaction cross-section from the merging galaxy cluster 1E0657-56, Astrophys. J. 606 (2004) 819 [astro-ph/0309303] [INSPIRE].  
[60] D. Clowe, A. Gonzalez and M. Markevitch, Weak lensing mass reconstruction of the interacting cluster 1E0657-558: Direct evidence for the existence of dark matter, Astrophys. J. 604 (2004) 596 [astro-ph/0312273] [INSPIRE].  
[61] S.W. Randall, M. Markevitch, D. Clowe, A.H. Gonzalez and M. Bradac, Constraints on the Self-Interaction Cross-Section of Dark Matter from Numerical Simulations of the Merging Galaxy Cluster 1E 0657-56, Astrophys. J. 679 (2008) 1173 [arXiv:0704.0261] [INSPIRE].  
[62] J. Chen, T. Han and B. Tweedie, Electroweak Splitting Functions and High Energy Showering, JHEP 11 (2017) 093 [arXiv:1611.00788] [INSPIRE].  
[63] M. Botje, QCDNUM: Fast QCD Evolution and Convolution, Comput. Phys. Commun. 182 (2011) 490 [arXiv:1005.1481] [INSPIRE].

[64] K. Bondarenko, A. Boyarsky, T. Bringmann, M. Hufnagel, K. Schmidt-Hoberg and A. Sokolenko, Direct detection and complementary constraints for sub-GeV dark matter, JHEP 03 (2020) 118 [arXiv:1909.08632] [INSPIRE].  
[65] M.J. Boschini et al., HelMod in the works: from direct observations to the local interstellar spectrum of cosmic-ray electrons, Astrophys. J. 854 (2018) 94 [arXiv:1801.04059] [INSPIRE].  
[66] I.B. Whittingham, Scattering of low energy neutrinos and antineutrinos by atomic electrons, Phys. Rev. D 105 (2022) 013008 [arXiv:2109.13454] [INSPIRE].  
[67] C.F. Bunge, J.A. Barrientos and A.V. Bunge, Roothaan-Hartree-Fock Ground-State Atomic Wave Functions: Slater-Type Orbital Expansions and Expectation Values for  $Z = 2 - 54$ , Atom. Data Nucl. Data Tabl. 53 (1993) 113 [INSPIRE].  
[68] T. Li and J. Liao, *Electron-target experiment constraints on light dark matter produced in primordial black hole evaporation*, Phys. Rev. D 106 (2022) 055043 [arXiv:2203.14443] [INSPIRE].  
[69] M. Rocha et al., Cosmological Simulations with Self-Interacting Dark Matter I: Constant Density Cores and Substructure, Mon. Not. Roy. Astron. Soc. 430 (2013) 81 [arXiv:1208.3025] [INSPIRE].  
[70] A.H.G. Peter, M. Rocha, J.S. Bullock and M. Kaplinghat, Cosmological Simulations with Self-Interacting Dark Matter II: Halo Shapes vs. Observations, Mon. Not. Roy. Astron. Soc. 430 (2013) 105 [arXiv:1208.3026] [INSPIRE].  
[71] A.R. Duffy, J. Schaye, S.T. Kay, C. Dalla Vecchia, R.A. Batty and C.M. Booth, Impact of baryon physics on dark matter structures: a detailed simulation study of halo density profiles, Mon. Not. Roy. Astron. Soc. 405 (2010) 2161 [arXiv:1001.3447] [INSPIRE].  
[72] A. Pontzen and F. Governato, How supernova feedback turns dark matter cusps into cores, Mon. Not. Roy. Astron. Soc. 421 (2012) 3464 [arXiv:1106.0499] [INSPIRE].  
[73] S.Y. Kim, A.H.G. Peter and J.R. Hargis, Missing Satellites Problem: Completeness Corrections to the Number of Satellite Galaxies in the Milky Way are Consistent with Cold Dark Matter Predictions, Phys. Rev. Lett. 121 (2018) 211302 [arXiv:1711.06267] [INSPIRE].  
[74] S. Tulin and H.-B. Yu, Dark Matter Self-interactions and Small Scale Structure, Phys. Rept. 730 (2018) 1 [arXiv:1705.02358] [INSPIRE].  
[75] P.S. Krstić and D.R. Schultz, Consistent definitions for, and relationships among, cross sections for elastic scattering of hydrogen ions, atoms, and molecules, Phys. Rev. A 60 (1999) 2118.  
[76] B. Colquhoun, S. Heeba, F. Kahlhoefer, L. Sagunski and S. Tulin, *Semiclassical regime for dark matter self-interactions*, Phys. Rev. D 103 (2021) 035006 [arXiv:2011.04679] [INSPIRE].  
[77] J. Li, J. Pei and C. Zhang, Multi-scalar signature of self-interacting dark matter in the NMSSM and beyond, JHEP 09 (2021) 151 [arXiv:2104.10449] [INSPIRE].