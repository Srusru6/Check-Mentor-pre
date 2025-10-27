# Revisiting the fermionic dark matter absorption on electron target

Shao-Feng Ge, $^{a,b}$  Xiao-Gang He, $^{a,b,c}$  Xiao-Dong Ma $^{a,b}$  and Jie Sheng $^{a,b}$

$^{a}$  Tsung-Dao Lee Institute (TDLI) & School of Physics and Astronomy (SPA), Shanghai Jiao Tong University (SJTU), Shanghai 200240, China  
<sup>b</sup>Key Laboratory for Particle Astrophysics and Cosmology (MOE) & Shanghai Key Laboratory for Particle Physics and Cosmology, Shanghai Jiao Tong University, Shanghai 200240, China  
$^{c}$ Department of Physics, National Taiwan University, Taipei 10617, Taiwan

E-mail: gesf@sjtu.edu.cn, hexg@phys.ntu.edu.tw, maxid@sjtu.edu.cn, shengjie04@sjtu.edu.cn

ABSTRACT: We perform a systematic study of the fermionic DM absorption interactions on electron target in the context of effective field theory. The fermionic DM absorption is not just sensitive to sub-MeV DM with efficient energy release, but also gives a unique signature with clear peak in the electron recoil spectrum whose shape is largely determined by the atomic effects. Fitting with the Xenon1T and PandaX-II data prefers DM mass at  $m_{\chi} = 59 \mathrm{keV}$  and  $105 \mathrm{keV}$ , respectively, while the cut-off scale is probed up to around 1 TeV. The DM overproduction in the early Universe, the invisible decay effect on the cosmological evolution, and the visible decay signal collected by the astrophysical X(gamma)-ray observations (Insight-HXMT, NuSTAR, HEAO-1, and INTEGRAL) are thoroughly explored to constrain the DM absorption interactions. With stringent bounds on the tensor and pseudo-scalar operators, the other fermionic DM operators are of particular interest at tonne-scale direct detection experiments such as PandaX-4T, XENONnT, and LZ.

KEYWORDS: Particle Nature of Dark Matter, Models for Dark Matter

ARXIV EPRINT: 2201.11497

# Contents

# 1 Introduction 1

# 2 Sub-MeV fermionic absorption DM on electron target 3

2.1 Fermionic DM absorption on electron and atomic effects 4  
2.2 Confronting the Xenon1T and PandaX-II data 7

# 3 The DM overproduction in the early universe 8

3.1 Boltzmann equation and its solution 8  
3.2 Consistency check of the simplified Boltzmann equation 11  
3.3Constraints from DM overproduction 13

# 4 DM decay 15

4.1 The scalar and pseudo-scalar operators  $\mathcal{O}_{e\nu \chi}^{S(P)}$  15  
4.2 The vector operator  $\mathcal{O}_{e\nu \chi}^{V}$  17  
4.3 The axial-vector operator  $\mathcal{O}_{e\nu \chi}^{A}$  18  
4.4 The tensor operator  $\mathcal{O}_{e\nu \chi}^{T}$  19

# 5 The cosmological and astrophysical constraints on DM decays 20

5.1 The cosmological evolution constraints on the DM invisible decay  $\chi \rightarrow 3\nu$  20  
5.2 The astrophysical X-ray and gamma ray constraints on the visible decays  $\chi \rightarrow \nu +\gamma (\mathrm{s})$  20

5.2.1 X-ray and gamma ray fluxes from the visible decays 20  
5.2.2 Constraints from astrophysical X-ray and gamma ray data in the keV-MeV range 22

# 6 Conclusions 26

# A Analytic  $\chi^2$  fit with collective marginalization 26

# 1 Introduction

The nature of dark matter (DM) remains a mysterious puzzle in our understanding of the Universe [1, 2]. The possible particle nature of DM is a well-motivated scenario to be probed by the direct detection experiments [3, 4] and indirect observations [5, 6]. The stability of DM particle is usually realized by some discrete symmetry such as  $\mathbb{Z}_2$  [7-9]. A direct consequence is that in direct detection, the scattering process has a DM particle in the initial state and another DM particle in the final one. The energy deposit comes from the DM kinetic energy. With typical experimental threshold at  $\mathcal{O}(1)\mathrm{keV}$ , direct

detection experiments are only sensitive to the DM mass above GeV. In the  $\mathrm{GeV} \sim \mathrm{TeV}$  mass range, the null result from the direct detection experiments has put very strong limit on the DM interaction strength with the Standard Model (SM) particles [10, 11]. In contrast, the cross section of sub-GeV light DM scattering with SM particles is much less stringently constrained and can still be large [3, 4]. More attention has been turned to light DM alternatives with sub-GeV mass [12] or even lighter ones such as the sterile neutrino DM [13-16].

However, one difficulty for the light DM detection is its small recoil energy. For a typical DM scattering with nuclei target, the recoil energy  $T_{r} = 4m_{\chi}m_{A}T_{\chi} / (m_{\chi} + m_{A})^{2}$  is proportionally scaled from the DM kinetic energy  $T_{\chi}$ . The most efficient energy transfer happens when the DM mass  $m_{\chi}$  is roughly the size of the atomic mass  $m_{A}$  of the nuclei target,  $T_{r} \approx T_{\chi}$ . With light DM,  $m_{\chi} \ll m_{A}$ , the recoil energy  $T_{r} \approx 4m_{\chi}T_{\chi} / m_{A}$  decreases with not just the DM mass  $m_{\chi}$  but also its kinetic energy  $T_{\chi}$ . More importantly, the DM kinetic energy is also proportional to its mass,  $T_{\chi} \approx \frac{1}{2} m_{\chi}v_{\chi}^{2}$ , while the distribution of its velocity  $v_{\chi}$  is fixed by the galaxy gravitational potential [17]. Altogether, the nuclear recoil from the light DM scattering scales with  $m_{\chi}^{2}$ . This explains why the direction detection sensitivity deteriorates quickly in the sub-GeV range. It is desirable to find possible ways to overcome this difficulty.

There are several ways of improving the detection of light DM. For nuclear recoil, the detection threshold can be lowered by using Germanium point-contact detector [18], bolometer [19, 20], nuclear bremsstrahlung [21, 22], and Migdal effect [22-33]. Or one may replace the nuclear recoil by electron recoil. Then, the elastic recoil energy is  $T_{r} = 4m_{\chi}m_{e}T_{\chi} / (m_{\chi} + m_{e})^{2}$  which removes the suppression factor  $m_{\chi} / m_{A}$ . In addition to using the conventional detector for measuring the electron recoils, various new technology has been developed. From the condensed matter side, the typically small energy gap is of great advantage to build a low threshold detector such as using superheated liquid [34], superconduction [35], Fermi degenerate materials [36], super-fluid [37, 38], scintillation [39], magnetic molecular [40], Dirac material [41], diamond crystal [42], nanowire [43], nanotube [44, 45], magnon [46, 47], graphene [48, 49], and plasmon [50]. In particular, a semiconductor detector such as skipper CCD is very sensitive to single electron events [51-53]. The biological DNA also provides an interesting possibility [54].

On the other hand, DM particles upscattered to higher energy can also overcome the detection threshold. Several possibilities have been discussed in the literature. The nonrelativistic DM particles can be boosted by the cosmic rays to gain sufficient energy [55-70]. This cosmic ray boosted DM (CRDM) scenario can happen as long as DM interacts with SM particles which is exactly the foundation of DM direct detection. Actual experimental search with real DM direct detection data has been carried out by PandaX-II [71] and CDEX [72], in addition to those constraints from neutrino experiments [57, 73-77] and indirect constraints [55, 78]. The CRDM may also be produced by astrophysical neutrinos [79-85] and blazar [86]. If the DM particle is light enough, it is also possible for them to be produced by the cosmic ray interactions with the atmosphere [87-89]. Another place to boost light DM is the Sun [90-95]. With multiple components, the boosted light DM can also happen inside the dark sector [96-100].

Another possibility is the fermionic DM absorption. The upscattered DM scenarios mentioned in the above paragraph can probe light DM, but the dependence on the DM mass may not be significant. This is because smaller mass usually means smaller effect on the kinematics, especially if DM particles are highly boosted. In order for DM detection to be sensitive to the light DM mass, the mass term should dominate the relevant kinematics. Namely, non-relativistic DM may have some advantage in this regard. If a non-relativistic DM releases all its mass into energy, its mass is the dominant factor and the detection threshold can also be overcome with efficient amplification by the speed of light,  $E = mc^2$ . This is exactly the idea of DM absorption for bosonic [101-110] and fermionic [111-113] DM. In this work, we take the effective field theory approach to systematically investigate the fermionic DM absorption on electron target and obtain model-independent constraints from the DM overproduction, the cosmological evolution, and the astrophysical X(gamma)-ray by using new observational results.

This paper is organized as follows. In section 2, we introduce the motivation for the sub-MeV fermionic absorption DM and enumerate all the possible effective absorption operators. In section 2.1 we discuss the signal in direct detection experiment. Then we evaluate the constraints from the DM overproduction in the early Universe in section 3 as well as the cosmological evolution constraint on the invisible decay  $\chi \rightarrow 3\nu$  and astrophysical constraints with X(gamma)-rays on the visible decay modes  $\chi \rightarrow \nu +\gamma (s)$  in section 5. More details about the calculation of DM decay is provided in section 4. Our main results are summarized in section 6. On the technical side, we provide simplified algorithms for a general-purpose analytic  $\chi^2$  fit with collective marginalization in appendix A.

# 2 Sub-MeV fermionic absorption DM on electron target

As pointed out above, the light DM has intrinsic difficulty in the direct detection experiments due to energy threshold. One possible way of overcoming this comes from the fermionic DM absorption,  $\chi e\rightarrow \nu e$ , where the DM particle  $\chi$  scatters into a massless SM neutrino  $\nu$ . Placing neutrino in the final state not only conserves charge but also is the most economical choice to maximize the energy release. Then the DM mass  $m_{\chi}$  is wholly converted to the electron recoil and neutrino energies. The fermionic DM absorption on a nuclear target is also possible [111, 112] but requires heavier DM above MeV mass to overcome the detection threshold. In our current paper, we focus on the electron target that is optimal for sub-MeV DM [113].

For a free electron target at rest, the electron recoil energy is  $T_{r} \approx m_{\chi}^{2} / 2m_{e}$  [113], which is a good approximation for  $m_{\chi} \ll m_{e}$ . A keV scale DM can already produce large enough electron recoil energy to overcome the detection threshold that is typically 1 keV for the electron signal [114, 116]. Although larger electron recoil energy  $T_{r}$  is better for direct detection threshold, the DM mass is not larger the better. For  $m_{\chi} = 1 \mathrm{MeV}$ , the electron recoil approaches 1 MeV which may saturate the detector capability. So we focus on the sub-MeV DM mass range with  $1 \mathrm{keV} \lesssim m_{\chi} \lesssim 1 \mathrm{MeV}$  across this paper.

To make a systematic study of the fermionic DM absorption, we take the effective field theory (EFT) approach for a model independent analysis. As argued at the beginning

of this section, the relevant degrees of freedom are the light SM particles, electron and neutrino, augmented with an additional DM particle. Usually, the SM gauge symmetries  $\mathrm{U}(1)_Y\times \mathrm{SU}(2)_L\times \mathrm{SU}(3)_c$  is kept intact for an EFT approach. Nevertheless, the DM direct detection happens at low energy where the electroweak part is broken. Only the electromagnetic  $\mathrm{U}(1)_{\mathrm{em}}$  is a good symmetry to guide the construction of EFT operators as far as gauge symmetry of the theory is concerned. The strong interaction  $\mathrm{SU}(3)_c$  is of no relevance since no color degrees of freedom are involved.

For the fermionic DM absorption on the electron target, the leading local interactions are dimension-six operators involving a dark matter particle  $\chi$ , an active SM neutrino  $\nu$  and an electron current,

$$
\mathcal {O} _ {e \nu \chi} ^ {S} \equiv (\bar {e} e) (\bar {\nu} _ {L} \chi_ {R}), \tag {2.1a}
$$

$$
\mathcal {O} _ {e \nu \chi} ^ {P} \equiv (\bar {e} i \gamma_ {5} e) (\bar {\nu} _ {L} \chi_ {R}), \tag {2.1b}
$$

$$
\mathcal {O} _ {e \nu \chi} ^ {V} \equiv (\bar {e} \gamma_ {\mu} e) (\bar {\nu} _ {L} \gamma^ {\mu} \chi_ {L}), \tag {2.1c}
$$

$$
\mathcal {O} _ {e \nu \chi} ^ {A} \equiv (\bar {e} \gamma_ {\mu} \gamma_ {5} e) (\bar {\nu} _ {L} \gamma^ {\mu} \chi_ {L}), \tag {2.1d}
$$

$$
\mathcal {O} _ {e \nu \chi} ^ {T} \equiv (\bar {e} \sigma_ {\mu \nu} e) (\bar {\nu} _ {L} \sigma^ {\mu \nu} \chi_ {R}), \tag {2.1e}
$$

and their Hermitian conjugates. For completeness, we have considered all the five independent Lorentz structures for the electron bilinear (scalar [S], pseudo-scalar [P], vector [V], axial-vector [A] and tensor [T]). The neutrino field is taken to be the SM left-handed component  $\nu_{L}$  and the DM  $\chi$  is assumed to be a Dirac particle for convenience. Any other types of operators can be converted to those in eq. (2.1) by Dirac gamma matrix identities and Fierz transformations [117-119]. For instance, the operator  $(\bar{e}\sigma_{\mu \nu}\gamma_5e)(\bar{\nu}_L\sigma^{\mu \nu}\chi_R)$  is equivalent to  $\mathcal{O}_{e\nu \chi}^{T}$  by the identities  $\sigma^{\mu \nu}\gamma^{5} = \frac{i}{2}\epsilon^{\mu \nu \rho \sigma}\sigma_{\rho \sigma}$  and  $\gamma_5P_R = P_R$  with  $P_R$  being the right-handed projection operator.

Each operator carries a Wilson coefficient  $C_i$ . Since the operators are already dimension 6,  $C_i \equiv 1 / \Lambda^2$  carry two units of inverse mass dimension,  $[\mathrm{mass}]^{-2}$ . Given new physics scenario, a heavy mediator can be integrated away to match the effective interaction. Equivalently, the effective scale  $\Lambda$  can be identified with the heavy mediator mass up to some dimensionless coupling constants. Although there is no fundamental principle to forbid the above operators to simultaneously appear, we consider them separately in the following discussions.

# 2.1 Fermionic DM absorption on electron and atomic effects

The local DM distribution around the Sun is roughly known from the hydrodynamic simulation of our Milky Way galaxy [17]. With the local DM energy density,  $\rho_{\chi} \approx 0.4 \mathrm{GeV/cm}^3$ , its number density  $n_{\chi} = \rho_{\chi}/m_{\chi}$  is inversely proportional to mass  $m_{\chi}$ . In addition, the DM velocity distribution is determined by the gravitational potential of the galaxy matter and dark matter. Around the Sun, the DM velocity follows the Maxwell-Boltzmann distribution and peaks around typically  $v_{\chi} \sim (200 \sim 300) \mathrm{km/s}$ . In other words, the DM in our solar system is non-relativistic with only  $\mathcal{O}(10^{-3})$  of the speed of light. Since the absorption process releases the whole DM mass as the energy of final-state particles, its kinetic energy  $T_{\chi} \approx \frac{1}{2} m_{\chi} v_{\chi}^{2}$  is negligibly small,  $T_{\chi}/m_{\chi} \sim \mathcal{O}(10^{-6})$ .

To better understand the impact of atomic effects, we compare the DM-electron scattering without and with the nuclei Coulomb potential. We first take the initial electron as free particle at rest and estimate the scattering cross section  $\sigma_{\chi e}$ ,

$$
\sigma_ {\chi e} ^ {S} v _ {\chi} \approx \frac {1}{\Lambda^ {4}} \frac {m _ {\chi} ^ {2} (2 m _ {e} + m _ {\chi}) ^ {4}}{6 4 \pi (m _ {e} + m _ {\chi}) ^ {4}}, \tag {2.2a}
$$

$$
\sigma_ {\chi e} ^ {P} v _ {\chi} \approx \frac {1}{\Lambda^ {4}} \frac {m _ {\chi} ^ {4} (2 m _ {e} + m _ {\chi}) ^ {2}}{6 4 \pi (m _ {e} + m _ {\chi}) ^ {4}}, \tag {2.2b}
$$

$$
\sigma_ {\chi e} ^ {V} v _ {\chi} \approx \frac {1}{\Lambda^ {4}} \frac {m _ {\chi} ^ {2} (2 m _ {e} + m _ {\chi}) ^ {2} (2 m _ {e} ^ {2} + 4 m _ {e} m _ {\chi} + 3 m _ {\chi} ^ {2})}{3 2 \pi (m _ {e} + m _ {\chi}) ^ {4}}, \tag {2.2c}
$$

$$
\sigma_ {\chi e} ^ {A} v _ {\chi} \approx \frac {1}{\Lambda^ {4}} \frac {m _ {\chi} ^ {2} (2 m _ {e} + m _ {\chi}) ^ {2} (6 m _ {e} ^ {2} + 8 m _ {e} m _ {\chi} + 3 m _ {\chi} ^ {2})}{3 2 \pi (m _ {e} + m _ {\chi}) ^ {4}}, \tag {2.2d}
$$

$$
\sigma_ {\chi e} ^ {T} v _ {\chi} \approx \frac {1}{\Lambda^ {4}} \frac {m _ {\chi} ^ {2} (2 m _ {e} + m _ {\chi}) ^ {2} (6 m _ {e} ^ {2} + 1 0 m _ {e} m _ {\chi} + 5 m _ {\chi} ^ {2})}{8 \pi (m _ {e} + m _ {\chi}) ^ {4}}. \tag {2.2e}
$$

Those terms suppressed by the DM velocity  $v_{\chi}$  have been neglected for clarity. Nevertheless, the DM velocity does not disappear completely since the quantity that enters the DM event rate is  $\sigma_{\chi e}v_{\chi}$  as a whole. In the limit of tiny DM mass,  $m_{\chi}\ll m_{e}$ , all cross sections except for the pseudo-scalar case reduce to a universal quantity,  $m_{\chi}^{2} / 4\pi \Lambda^{4}$  [113], up to numerical factors.

In reality, the initial and final electrons are subject to the Coulomb potential produced by the central nuclei and other surrounding electrons. The initial electron inside the atom is not at rest and its kinetic energy is of the same size as the binding energy. And for typical electron recoil energy of  $\mathcal{O}(\mathrm{keV})$  in the final state, the atomic binding effect could be large enough to affect the direct detection event rate. We follow the general formalism developed with second quantization for both the initial bound and final ionized electron states [120]. The differential cross section is then a convolution of the particle scattering amplitude  $|\mathcal{M}|^2$  and the atomic  $K$ -factor  $K_{nl}(T_r,|\mathbf{q}|)$ ,

$$
\frac {d \sigma_ {\chi e}}{d T _ {r}} v _ {\chi} = \frac {1}{T _ {r}} \sum_ {n, l} (4 l + 2) \int \frac {d ^ {3} \mathbf {q}}{(2 \pi) ^ {3} 2 E _ {\nu}} \frac {1}{8 m _ {e} ^ {2} E _ {\chi}} | \mathcal {M} | ^ {2} (\mathbf {q}) K _ {n l} (T _ {r}, | \mathbf {q} |) (2 \pi) \delta_ {E}. \tag {2.3}
$$

The summation over the principle quantum number  $n$  and the angular momentum  $l$  is a product of the electron number  $(2l + 1)$  of the state  $|nl\rangle$  and the spin degrees of freedom 2.

The remaining  $\delta_{E}$  function comes from energy conservation. For non-relativistic DM, its kinetic energy can be omitted in comparison with the energy release from the DM absorption process,

$$
\delta_ {E} \equiv \delta \left(m _ {\chi} - | \mathbf {q} | - \Delta E _ {n l}\right). \tag {2.4}
$$

With vanishing mass, the neutrino energy  $E_{\nu} = |\mathbf{q}|$  is the same as its momentum and equivalently the size of momentum transfer  $|\mathbf{q}|$ . On the electron side, the energy gain,  $\Delta E_{nl} \equiv T_r - E_{nl}$ , is the difference between the ionized electron energy  $T_r$  and the negative initial binding energy  $E_{nl}$  for the state  $|nl\rangle$ . It is then desirable to first integrate  $|\mathbf{q}|$  away from the phase space element  $d^3\mathbf{q} = |\mathbf{q}|^2 d|\mathbf{q}|d\Omega_q$ . For the scattering with a bound electron,

$\left|\mathbf{q}\right|$  and  $T_{r}$  are usually independent variables due to the unknown initial electron momentum inside an atom. However, the energy conservation eq. (2.4) establishes a correlation,  $\left|\mathbf{q}\right| = m_{\chi} - \Delta E_{nl}$ .

On the other hand, the solid angle integration  $d\Omega_q \equiv d\cos \theta_q d\phi_q$  contains the information of momentum transfer direction. However, neither the  $K$ -factor  $K_{nl}(T_r, |\mathbf{q}|)$  [120] nor the scattering matrix element  $|\mathcal{M}(\mathbf{q})|^2$  has dependence on the angular coordinates of  $\mathbf{q}$ . For the latter, the angular independence happens due to the fact that the DM velocity is negligible in the absorption process. Without a preference, the direction of  $\mathbf{q}$  is not important either. The solid angle integration then simply gives an overall factor of  $4\pi$ . Consequently, eq. (2.3) becomes,

$$
\frac {d \left\langle \sigma_ {\chi e} v _ {\chi} \right\rangle}{d T _ {r}} = \sum_ {n l} (4 l + 2) \frac {1}{T _ {r}} \frac {m _ {\chi} - \Delta E _ {n l}}{1 6 \pi m _ {e} ^ {2} m _ {\chi}} | \mathcal {M} | ^ {2} (\mathbf {q}) K _ {n l} \left(T _ {r}, | \mathbf {q} |\right), \tag {2.5}
$$

where we have implemented the facts that  $E_{\nu} = |\mathbf{q}|$  and  $|\mathbf{q}| = m_{\chi} - \Delta E_{nl}$ . Since the left-hand sides of eq. (2.3) and eq. (2.5) are independent of the DM velocity,  $\sigma_{\chi e}v_{\chi}$  is essentially  $\langle \sigma_{\chi e}v_{\chi}\rangle$ . Although there are five operators in eq. (2.1), the scattering matrix element  $|\mathcal{M}|^2$  has only two different forms,

$$
\left| \mathcal {M} ^ {(S, V, A, T)} \right| ^ {2} = (4, 4, 1 2, 4 8) \times \frac {1}{\Lambda^ {4}} m _ {\chi} m _ {e} ^ {2} \left(m _ {\chi} - \Delta E _ {n l}\right), \quad \left| \mathcal {M} ^ {P} \right| ^ {2} = \frac {1}{\Lambda^ {4}} m _ {\chi} \left(m _ {\chi} - \Delta E _ {n l}\right) ^ {3}. \tag {2.6}
$$

Note that the scalar (S), vector (V), axial-vector (A), and tensor (T) operators all have the same structure while the pseudo-scalar (P) case is different as its matrix element intrinsically has a momentum transfer dependence as elaborated in [120].

The left panel of figure 1 shows the typical differential and total cross sections for  $m_{\chi} = (59,105) \mathrm{keV}$ . Since the scalar, vector, axial-vector, and tensor interactions share the same matrix element structure and consequently the same differential spectrum, only vector (blue) and pseudo-scalar (green) curves are shown. For comparison, the electron recoil energy from the DM absorption on a free electron at rest takes a fixed value (gray),  $T_{r} = m_{\chi}^{2} / 2(m_{e} + m_{\chi})$  which is derived without approximation. Although the spectrum widens due to atomic effect, the peak is still at exactly the same location as the free case. For  $m_{\chi} = (59,105) \mathrm{keV}$ , the peak position is  $T_{r} = (3.05,8.95) \mathrm{keV}$ , respectively. We have adjusted the  $y$ -axis scales for the vector (left blue) and pseudo-scalar (right green) cases to make the  $m_{\chi} = 105 \mathrm{keV}$  peaks with roughly the same height. Since the matrix element  $|\mathcal{M}|^2$  has  $m_{\chi} - \Delta E_{nl}$  dependence for the vector operator and  $(m_{\chi} - \Delta E_{nl})^3$  for the pseudo-scalar one, the  $m_{\chi} = 59 \mathrm{keV}$  peak heights scale accordingly. With major contribution coming from the outer shell electrons, the binding energy  $E_{b} = (0.16,0.012) \mathrm{keV}$  for  $(4p,5p)$  shells can be negligibly small [121]. Then the peak height scales with  $m_{\chi} - T_{r}$  and  $(m_{\chi} - T_{r})^3$ , respectively. For the vector (pseudo-scalar) case, the peak height reduces by a factor of 0.58 (0.20). This explains why the pseudo-scalar peak is only around  $1/3$  of the vector counterpart for  $m_{\chi} = 59 \mathrm{keV}$ . The  $T_{r}$  dependence arises from the  $K$ -factor and energy gain  $\Delta E_{nl} = T_{r} - E_{nl}$ . Although the  $m_{\chi} - T_{r}$  dependence is quite different, the spectrum shape has only slight difference among operators. This is because the two cases shown in the left panel of figure 1 has  $m_{\chi} \gg T_{r}$ . Consequently, the electron recoil energy

![](images/f975be44478c0a1a78ac3dbaf455d6f452cd2c8d21b745d9beda7594c3d1fab5.jpg)  
Figure 1. (Left) The atomic effects of Xe on the electron recoil spectrum with two typical DM masses  $m_{\chi} = 59 \mathrm{keV}$  (dot-dashed) and  $105 \mathrm{keV}$  (solid) for vector (blue) and pseudo-scalar (green) operators. Since the pseudo-scalar cross section is sensitive to the DM mass, the left axis adopts a scale of  $\mathcal{O}(1000)$  in blue for the vector case while the right one of  $\mathcal{O}(10)$  in green for the pseudo-scalar one. (Right) The atomic effects on the thermally averaged total cross section with velocity weight  $\langle \sigma_{\chi e} v_{\chi} \rangle$  for vector (blue) and pseudo-scalar (green) cases. Comparison has been made between the scattering cross section with a bound (thick) and free (thin) electron while the bound/free ratios are shown in red color according to the right axis scale.

![](images/6c5a7f795a1a97889880fc40061594f4c155accf9db518ba57a6f2632fc2ab58.jpg)

$T_{r}$  spectrum shows exactly the shape of the  $K$ -factor which is operator-independent. Once enough events are detected, the shape of the  $K$ -factor can be reconstructed from the  $T_{r}$  spectrum.

The right panel of figure 1 shows the total cross section  $\langle \sigma v_{\chi} \rangle$  as a function of the DM mass. With larger  $m_{\chi}$ , the cross section also becomes larger. For light DM,  $m_{\chi} \ll m_e$ , eq. (2.2) indicates that  $\sigma_{\chi e}^{P} v_{\chi}$  for pseudo-scalar type scales as  $m_{\chi}^{4}$  while the others as  $m_{\chi}^{2}$ . The curves for free electron scattering are fully consistent with the expected scaling behavior. Including the atomic effects reduces the total cross section due to binding energy of the initial electron. For inner shells, such as  $E_b = (4.53, 0.95)$  keV for  $(2p, 3p)$  electrons [121], the binding energy can be as large as the recoil energy  $T_r$  to significantly reduce the event rate. The red lines show the ratio between the total cross sections with bound and free electrons. A reduction of  $0.5 \sim 0.7$  can happen. With smaller  $m_{\chi}$ , the energy release is also smaller and consequently harder to overcome the atomic bound energy which leads to a larger suppression in the total cross section.

# 2.2 Confronting the Xenon1T and PandaX-II data

In 2020, both Xenon1T and PandaX-II collaborations published their electron recoil spectrum [114, 122]. An excess around  $(2\sim 3)\mathrm{keV}$  appears in the Xenon1T data with significance reaching  $3\sigma$ . This could be explained by the  $\beta$  decays of tritium at  $3.2\sigma$  with a concentration in xenon of  $(6.2\pm 2.0)\times 10^{-25}\mathrm{mol / mol}$ , but "such a trace amount can neither be confirmed nor excluded" [114]. The PandaX-II data is consistent with the Xenon1T excess within  $1\sigma$  [122]. Since a sub-MeV fermionic DM absorption also leaves a sharp peak at low recoil energy as shown in figure 1, confronting the Xenon1T and PandaX-II data can also provide a meaningful constraint on the preferred parameter space.

The event rate of DM direct detection,

$$
\frac {d N}{d T _ {r}} = N _ {T} \frac {\rho_ {\chi}}{m _ {\chi}} t \times \epsilon (T _ {r}) \frac {d \langle \sigma_ {\chi e} v _ {\chi} \rangle}{d T _ {r}}, \tag {2.7}
$$

scales with the number of Xenon atoms  $N_{T}$ , DM local number density  $\rho_{\chi} / m_{\chi}$ , and run time  $t$ . The Xenon1T analysis uses 0.65 tonne-years of data and PandaX-II has 100 tonne-days. In addition, the detection efficiencies  $\epsilon (T_r)$  are basically constant above  $(3\sim 4)$  keV and decrease to 0 below there [114, 115].

We adopt the analytical  $\chi^2$  analysis [123, 124], whose advanced version is summarized in appendix A, to estimate the sensitivity. In addition to the fermionic DM absorption signal, background estimations are taken from the experimental papers [114]. The results are shown in figure 2 for the fit with Xenon1T (left panel) and PandaX-II (right panel) data. Since the different DM absorption operators share roughly the same spectrum shape, one representative vector case can already show the features clearly. For Xenon1T, the best fit is at  $m_{\chi} = 59\mathrm{keV}$  and  $\Lambda = 0.979\mathrm{TeV}$ , being consistent with [113]. The inset plot shows the signal and background curves with the best-fit values. The fermionic DM absorption signal with peak at  $T_r = 3.1\mathrm{keV}$  can fit the Xenon1T excess very nicely. Comparing with the background-only fit, the  $\chi_{\mathrm{min}}^2$  decreases from 46.3 to 32.2. The decreasing edge for  $m_{\chi} \rightarrow 20\mathrm{keV}$  is due to two major reasons: 1) the cross section decreases with  $m_{\chi}^2$  in this region and 2) the efficiency further suppresses its event rate to make it less sensitive. Both needs compensation of a larger coupling strength, or equivalently a lower cut-off scale  $\Lambda$ . On the other side, the rising edge for  $m_{\chi} \rightarrow 150\mathrm{keV}$  at Xenon1T is due to the abnormally lower data point around  $(17 \sim 18)\mathrm{keV}$  where the recoil spectrum peaks. For PandaX-II data [122], the best fit is at  $m_{\chi} = 105\mathrm{keV}$  corresponding to the small excess at  $T_r = (8 \sim 9)\mathrm{keV}$ . Since the peak is not that significant, the  $\chi_{\mathrm{min}}^2$  decreases by only less than 3 from 31.0 of the background-only fit to 28.3. Different from the Xenon1T data, the  $T_r = (17 \sim 19)\mathrm{keV}$  data points are higher than the expected background instead which leads to a flat tail for  $m_{\chi} \rightarrow 150\mathrm{keV}$ .

# 3 The DM overproduction in the early universe

A light DM is typically produced non-thermally. This is because the thermal freeze-out gives a relic density  $\rho_{\chi} \propto m_{\chi}^{2} / \langle \sigma v \rangle$  as ratio between the DM mass and the thermally averaged cross section [125]. To obtain the correct relic density, the interaction strength between DM and SM particles should scale linearly with its mass. Consequently, a light DM typically has a very small coupling with SM particles. Then it is difficult for the light DM to reach thermal equilibrium with the environmental plasma before the thermal freeze-out [126]. Instead, their production is usually realized by the so-called freeze-in mechanism [127-131]. No matter how the DM relic density is generated, it cannot exceed the observed value,  $\Omega_{\mathrm{dm}} h^2 \approx 0.12$  [132].

# 3.1 Boltzmann equation and its solution

For the fermionic DM absorption on electron target, the DM is intrinsically connected to electrons and positrons as demonstrated by the operators in eq. (2.1). The light DM can be

![](images/564dca1e6547630349041d21fd14da20ace50034cf1234ea2ce5cdc7a39f25b2.jpg)  
Figure 2. The best fits (red star) and sensitivity contours of fermionic DM absorption at Xenon1T (Left) and PandaX-II (Right). Deeper color corresponds to smaller  $\Delta \chi^2$  and the white region has been excluded with  $\Delta \chi^2 > 49$ . For illustration, only the vector case is shown with best fit values  $m_{\chi} = 59\mathrm{keV}$  and  $\Lambda = 0.979\mathrm{TeV}$  at Xenon1T while  $m_{\chi} = 105\mathrm{keV}$  and  $\Lambda = 1.003\mathrm{TeV}$  at PandaX-II. The red dashed contour shows the  $95\%$  C.L. for comparison with other plots. In addition to data points (black), the inset plots demonstrate the background (red dashed) and total (blue solid) event rates with the corresponding best-fit values.

![](images/8033c015625be62972dde2c41952aa377cadecae06fa8a650e63452b26bc17a1.jpg)

produced by the pair annihilation process  $e^{+}e^{-}\rightarrow \chi \nu$ . The Boltzmann equation governing the evolution of DM number density  $n_{\chi}$  is,

$$
\begin{array}{l} \frac {d n _ {\chi}}{d t} + 3 H n _ {\chi} = \int d \Pi_ {\chi} d \Pi_ {\nu} d \Pi_ {e ^ {-}} d \Pi_ {e ^ {+}} (2 \pi) ^ {4} \delta^ {(4)} (p _ {e ^ {+}} + p _ {e ^ {-}} - p _ {\chi} - p _ {\nu}) \\ \times \left[ | \mathcal {M} | _ {e ^ {+} e ^ {-} \rightarrow \nu \chi} ^ {2} f _ {e ^ {+}} f _ {e ^ {-}} (1 - f _ {\nu}) (1 - f _ {\chi}) - | \mathcal {M} | _ {\nu \chi \rightarrow e ^ {+} e ^ {-}} ^ {2} f _ {\nu} f _ {\chi} (1 - f _ {e ^ {+}}) (1 - f _ {e ^ {-}}) \right], \tag {3.1} \\ \end{array}
$$

where  $H$  is the Hubble parameter. For particle  $i$ ,  $f_{i}$  is its phase space distribution function and  $d\Pi_{i} \equiv d^{3}p_{i}/2E_{i}(2\pi)^{3}$  is the phase space integration element.

With the freeze-in mechanism, the DM density increases from 0. During the production process, the phase space distribution of DM is much less than that of the electrons and positrons,  $f_{\chi} \ll f_{e^{+}}, f_{e^{-}}$ . As we will discuss in section 3.2, the second term of eq. (3.1) can be omitted [131] and the Boltzmann equation then reduces to,

$$
\frac {d n _ {\chi}}{d t} + 3 H n _ {\chi} = \left\langle v _ {\mathrm {M} \emptyset \mathrm {l}} \sigma_ {e ^ {+} e ^ {-}} \right\rangle n _ {e ^ {+}} ^ {\mathrm {e q}} n _ {e ^ {-}} ^ {\mathrm {e q}}, \tag {3.2}
$$

where  $v_{\mathrm{M}\varnothing \mathrm{l}}$  is the Møller velocity of incoming electron/positron pair [133] and  $n_{e^{\pm}}^{\mathrm{eq}}$  are their number density at thermal equilibrium. We will come back to provide a detailed justification of this simplification later.

To solve the Boltzmann equation, we introduce the DM yield  $Y \equiv n_{\chi} / s(T)$  as the ratio of DM number density  $n_{\chi}$  over the entropy density  $s(T)$  as a function of temperature  $T$ . At the epoch of DM production, the universe is dominated by radiation. Both the Hubble parameter  $H$  and entropy density  $s(T)$  can evolve with temperature,

$$
H = 1. 6 6 \sqrt {g _ {*}} \frac {T ^ {2}}{M _ {\mathrm {P}}}, \quad s (T) = g _ {* s} \frac {2 \pi^ {2}}{4 5} T ^ {3}, \tag {3.3}
$$

where  $M_P = 1.22 \times 10^{19} \, \mathrm{GeV}$  is the Planck mass. The relativistic degrees of freedom  $g_* = g_*(T)$  and  $g_{*s} = g_{*s}(T)$  associated with the energy and entropy densities, respectively, are taken from [134] while more detailed discussions can be found in [135, 136]. Although the DM yield keeps increasing, the effective degrees of freedom are mainly contributed by the SM particles. Then in terms of yield  $Y$ , the Boltzmann equation in eq. (3.2) becomes,

$$
\frac {d Y}{d T} = - \frac {4 5 M _ {\mathrm {P}}}{2 \pi^ {2} (1 . 6 6 \sqrt {g _ {*}}) \tilde {g} _ {* s} T ^ {6}} \left\langle v _ {\mathrm {M o l}} \sigma_ {e ^ {+} e ^ {-}} \right\rangle n _ {e ^ {+}} ^ {\mathrm {e q}} n _ {e ^ {-}} ^ {\mathrm {e q}}, \quad \text {w i t h} \quad \tilde {g} _ {* s} \equiv g _ {* s} \left(1 + \frac {T}{3 g _ {* s}} \frac {d g _ {* s}}{d T}\right) ^ {- 1}. \tag {3.4}
$$

The minus sign in  $dY / dT$  arises because the temperature decreases with time but the DM yield  $Y$  increases.

The DM generation through the electron and positron annihilation  $e^{+}e^{-}\rightarrow \chi \nu$  is assumed to happen when the temperature decreases to around twice the electron mass,  $T\sim 2m_e$  [137]. Below this temperature,  $T\lesssim 2m_{e}$ , the Fermi-Dirac distribution of electron (positron) can be approximated by the Maxwell-Boltzmann distribution  $f_{e^{\pm}}^{\mathrm{eq}}\approx e^{-E / T}$ . For quantitative illustration, the typical electron (positron) energy is  $E_{e} = 2.27\mathrm{MeV}$  at  $T = 1\mathrm{MeV}$  to  $E_{e} = 1.01\mathrm{MeV}$  at  $T = 0.4\mathrm{MeV}$ . Correspondingly, the Maxwell-Boltzmann distribution gives  $e^{-E / T} = 0.104$  at  $T = 1\mathrm{MeV}$  and 0.080 at  $T = 0.4\mathrm{MeV}$ , which are very close to the Fermi-Dirac values 0.094 and 0.074, respectively. This further simplifies the thermally averaged cross section  $\langle v_{\mathrm{Mol}}\sigma_{e^{+}e^{-}}\rangle$  [133],

$$
\langle v _ {\mathrm {M o l}} \sigma_ {e ^ {+} e ^ {-}} \rangle n _ {e ^ {+}} ^ {\mathrm {e q}} n _ {e ^ {-}} ^ {\mathrm {e q}} = \frac {T}{8 \pi^ {4}} \int_ {4 m _ {e} ^ {2}} ^ {\infty} d s (s - 4 m _ {e} ^ {2}) \sqrt {s} K _ {1} \left(\frac {\sqrt {s}}{T}\right) \sigma_ {e ^ {+} e ^ {-}} (s), \tag {3.5}
$$

where  $K_{1}$  is the first modified Bessel function of second kind and  $s \equiv (p_{e^{-}} + p_{e^{+}})^{2}$  is the electron positron invariant mass squared.

The solution of the Boltzmann equation in eq. (3.4) can be obtained by integrating the temperature  $T$  from neutrino decoupling  $T_{\mathrm{max}} = 1 \mathrm{MeV}$ ,

$$
Y (T) = \frac {4 5 M _ {\mathrm {P}}}{1 6 \pi^ {6}} \int_ {T} ^ {T _ {\max }} \frac {d \widetilde {T}}{(1 . 6 6 \sqrt {g _ {*}}) \widetilde {g} _ {* s} \widetilde {T} ^ {5}} \int_ {4 m _ {e} ^ {2}} ^ {\infty} d s (s - 4 m _ {e} ^ {2}) \sqrt {s} K _ {1} \left(\frac {\sqrt {s}}{\widetilde {T}}\right) \sigma_ {e ^ {-} e ^ {+}} (s). \tag {3.6}
$$

For the DM absorption operators in eq. (2.1), the  $e^{-}e^{+}\rightarrow \nu \chi$  cross section is a function of the invariant mass  $s$ ,

$$
\sigma_ {e ^ {+} e ^ {-}} ^ {S} = \frac {1}{\Lambda^ {4}} \frac {\sqrt {s - 4 m _ {e} ^ {2}} (s - m _ {\chi} ^ {2}) ^ {2}}{3 2 \pi s \sqrt {s}}, \tag {3.7a}
$$

$$
\sigma_ {e ^ {+} e ^ {-}} ^ {P} = \frac {1}{\Lambda^ {4}} \frac {\left(s - m _ {\chi} ^ {2}\right) ^ {2}}{3 2 \pi \sqrt {s} \sqrt {s - 4 m _ {e} ^ {2}}}, \tag {3.7b}
$$

$$
\sigma_ {e ^ {+} e ^ {-}} ^ {V} = \frac {1}{\Lambda^ {4}} \frac {(s + 2 m _ {e} ^ {2}) (2 s + m _ {\chi} ^ {2}) (s - m _ {\chi} ^ {2}) ^ {2}}{4 8 \pi s ^ {2} \sqrt {s} \sqrt {s - 4 m _ {e} ^ {2}}}, \tag {3.7c}
$$

$$
\sigma_ {e ^ {+} e ^ {-}} ^ {A} = \frac {1}{\Lambda^ {4}} \frac {[ 2 s (s - 4 m _ {e} ^ {2}) + m _ {\chi} ^ {2} (s + 2 m _ {e} ^ {2}) ] (s - m _ {\chi} ^ {2}) ^ {2}}{4 8 \pi s ^ {2} \sqrt {s} \sqrt {s - 4 m _ {e} ^ {2}}}, \qquad (3. 7 \mathrm {d})
$$

$$
\sigma_ {e ^ {+} e ^ {-}} ^ {T} = \frac {1}{\Lambda^ {4}} \frac {(s + 2 m _ {e} ^ {2}) (s + 2 m _ {\chi} ^ {2}) (s - m _ {\chi} ^ {2}) ^ {2}}{1 2 \pi s ^ {2} \sqrt {s} \sqrt {s - 4 m _ {e} ^ {2}}}. \qquad (3. 7 \mathrm {e})
$$

![](images/b6b58d4b64d478626ff40538b34ac6650142a7db06dacc177f51ce2aeac83b23.jpg)  
Figure 3. The evolution of the DM yield  $Y(T)$  as function of temperature  $T$  for the DM absorption operators with the best-fit values  $m_{\chi} = 59(105)\mathrm{keV}$  and  $\Lambda = 0.979(1.003)\mathrm{TeV}$  of the Xenon1T (PandaX-II) data as shown in thin (thick) lines. The different fermionic DM absorption operators are shown with different line types and colors: scalar (S: green solid), pseudo-scalar (P: red dotted), vector (V: blue dashed), axial vector (A: purple dash-dotted), and tensor (T: cyan long dashed). Note that the colored light-face (bold-face) number is the rescaled DM yield today,  $10^{6}Y_{0}$ , for the corresponding operator with the best-fit values of the Xenon1T (PandaX-II) data.

Figure 3 shows the evolution of the DM yield  $Y(T)$  as a function of temperature  $T$ . For illustration, we adopt the best-fit values of DM mass  $m_{\chi} = 59$  (105) keV and the scale  $\Lambda = 0.979$  (1.003) TeV of the Xenon1T (PandaX-II) data as shown in thin (thick) lines. For all the five DM absorption operators, the DM yield converges when the Universe cools down to  $T \sim 0.4$  MeV. In the light DM limit,  $m_{\chi} \ll m_e \lesssim \sqrt{s}$ , the cross sections in eq. (3.7) have quite simple scaling behaviors,  $\sigma_{e^+ e^-}^{S,P,V,A,T} \approx \left( \frac{1}{8}, \frac{1}{8}, \frac{1}{6}, \frac{1}{6}, \frac{1}{3} \right) \times s / 4\pi \Lambda^4$ . There is no big difference among scalar and pseudo-scalar operators or among the vector and axial-vector ones as correctly reflected in figure 3. With larger cross section, the DM yield converges to a larger value. Between the scalar/pseudo-scalar group and the vector/axial-vector group, the converging values of the DM yield roughly differ by a factor of  $3/4$  which is consistent with the relative size among the cross sections,  $\sigma_{e^+ e^-}^{S,P} / \sigma_{e^+ e^-}^{V,A} \approx 3/4$ . The small deviation comes from the finite size of the DM mass  $m_{\chi} = 59$  (105) keV that is used in figure 3. The DM yield scales linearly with the  $e^+ e^- \rightarrow \chi \nu$  cross section. We can also check that between the vector/axial-vector group and the tensor operator, the factor of 2 difference is also consistent with both sides.

# 3.2 Consistency check of the simplified Boltzmann equation

Before proceeding to constrain the coupling strength of the DM absorption operators, we need to first justify the omission of the second term in eq. (3.1) for consistency check. The

freeze-in production of DM spans from neutrino decoupling ( $T \sim 1\mathrm{MeV}$ ) to the end of  $e^{+}e^{-}$ annihilation ( $T \sim 0.1\mathrm{MeV}$ ) [137]. During this period of time, electrons and positrons are still in equilibrium with the thermal bath and therefore follow the Fermi-Dirac distribution,  $f_{e^{\pm}} \equiv 1 / (e^{E_e \pm / T} + 1)$ . The most likely value of the electron/positron energy maximizes the energy distribution  $\sqrt{E_e^2 - m_e^2} E_ef_e^{\mathrm{eq}}$ . For example, the peak energy is  $E_{e} = 2.27\mathrm{MeV}$  at  $T = 1\mathrm{MeV}$  and  $E_{e} = 1.01\mathrm{MeV}$  at  $T = 0.4\mathrm{MeV}$ . Correspondingly, the phase space distribution function is roughly  $f_{e}^{\mathrm{eq}} \sim 0.094$  (0.074) at  $T = 1\mathrm{MeV}$  (0.4 MeV). Therefore, we can approximate  $(1 - f_{e^{\pm}}) \approx 1$  in the second term of eq. (3.1).

The cosmological evolution of DM density is related to the observed number density  $n_{\chi}^{0} = \rho_{\chi} / m_{\chi}$  today. Especially, the maximal value of  $n_{\chi}$  at the end of freeze-in process is  $n_{\chi}^{0} / a^{3}$  neglecting the possible DM decay. At temperature  $T = 0.4 \mathrm{MeV}$ , the scale factor  $a \equiv 1 / (1 + z)$  or equivalently the redshift is  $z \approx 1 / a \approx 1.6 \times 10^{9}$  [1]. The upper limit is reached when the freeze-in process contributes the full DM density. Since the DM is not in thermal equilibrium, one can only use the typical energy  $\overline{E}_{\chi}$  to estimate the size of the phase space distribution function,

$$
n _ {\chi} = \int \frac {d ^ {3} p}{(2 \pi) ^ {3}} f _ {\chi} \approx \frac {1}{2 \pi^ {2}} f _ {\chi} (\overline {{E}} _ {\chi}) \overline {{E}} _ {\chi} ^ {3} \lesssim \frac {n _ {\chi} ^ {0}}{a ^ {3}} \approx \frac {\rho_ {\chi} ^ {0}}{m _ {\chi}} z ^ {3} \approx 4 \times 1 0 ^ {- 5} \mathrm {M e V} ^ {3} \frac {\mathrm {k e V}}{m _ {\chi}}. (3. 8)
$$

The typical DM energy can be determined using the energy conservation condition  $E_{\chi} + E_{\nu} = E_{e^{+}} + E_{e^{-}}$  with the typical electron and positron energies  $E_{e^{\pm}}$ . In a head-on collision and  $E_{e^{+}} = E_{e^{-}}$ , the neutrino energy  $E_{\nu} = \sqrt{E_{\chi}^{2} - m_{\chi}^{2}}$  is directly related to the DM momentum and the DM energy is solved to be  $E_{\chi} = [m_{\chi}^{2} + (E_{e^{-}} + E_{e^{+}})^{2}] / [2(E_{e^{-}} + E_{e^{+}})]$ . For a sub-MeV DM with  $m_{\chi} \ll E_{e^{\pm}}$ , the DM energy has a lower limit,  $E_{\chi} \gtrsim (E_{e^{-}} + E_{e^{+}}) / 2$  which is approximately 1 MeV at  $T \approx 0.4 \mathrm{MeV}$ . The typical DM phase space factor is then bounded from above,

$$
f _ {\chi} \lesssim 4 \times 1 0 ^ {- 5} \mathrm {M e V} ^ {3} \frac {\mathrm {k e V}}{m _ {\chi}} \frac {2 \pi^ {2}}{\overline {{E}} _ {\chi} ^ {3}} \approx 8 \times 1 0 ^ {- 4} \frac {\mathrm {k e V}}{m _ {\chi}}, \tag {3.9}
$$

which is truly small comparing with the electron counterpart,  $f_{e} \sim 0.1$ .

For the neutrino phase space distribution  $f_{\nu}$ , there are two components. One is the standard cosmic neutrino background that follows the Fermi-Dirac distribution  $f_{\nu}^{\mathrm{eq}} \equiv 1 / (e^{E_{\nu} / T} + 1)$ . The other one is from the associated production together with the DM,  $e^{+}e^{-}\rightarrow \chi \nu$ , and shares a similar number density as that of the DM,  $n_{\nu}^{\prime} = n_{\chi}$ . Similar to the estimation of the DM phase space in eq. (3.8), this neutrino phase space component  $f_{\nu}^{\prime}$  satisfies a similar relation,  $n_{\nu}^{\prime} \approx f_{\nu}^{\prime}(\bar{E}_{\nu})\bar{E}_{\nu}^{3} / (2\pi^{2}) \lesssim 4\times 10^{-5}\mathrm{MeV}^{3}(\mathrm{keV} / m_{\chi})$ . The neutrino energy is  $\bar{E}_{\nu} = [(E_{e^{-}} + E_{e^{+}})^{2} - m_{\chi}^{2}] / [2(E_{e^{-}} + E_{e^{+}})]$ . For the sub-MeV DM with  $1\mathrm{keV}\lesssim m_{\chi}\lesssim 1\mathrm{MeV}$  and the fact that  $(E_{e^{-}} + E_{e^{+}}) / 2\gtrsim 1\mathrm{MeV}$  for  $T\gtrsim 0.4\mathrm{MeV}$ , we obtain  $\bar{E}_{\nu}\gtrsim \frac{3}{4}\mathrm{MeV}$ . Thus,  $f_{\nu}^{\prime}$  has an upper bound,  $f_{\nu}^{\prime}\lesssim 2\times 10^{-3}(\mathrm{keV} / m_{\chi})$ , which means it is much smaller than 1 for our interested range of  $m_{\chi}$ . So we can approximate  $f_{\nu}\approx f_{\nu}^{\mathrm{eq}}$ . Based on a similar analysis as for  $f_{e}^{\mathrm{eq}}$  by requiring that  $E_{\nu}^{2}f_{\nu}^{\mathrm{eq}}$  takes its maximal value, one can obtain the typical neutrino energy  $E_{\nu} = 2.22(0.89)\mathrm{MeV}$  at  $T = 1(0.4)\mathrm{MeV}$ . This further leads to a typical phase space distribution  $f_{\nu}^{\mathrm{eq}}\approx 0.1$ . With massless neutrino, this

estimation is independent of  $T$  since its phase space distribution function only depends on the ratio  $E_{\nu} / T$ . Therefore, we also approximate  $1 - f_{\nu} \approx 1$  to a very good accuracy.

Putting things  $(f_{e^{\pm}}, f_{\chi},$  and  $f_{\nu})$  together, we can justify the simplification of omitting the second term in eq. (3.1). At the converging point  $(T \approx 0.4\mathrm{MeV})$  of DM yield, the phase space factor ratio

$$
\frac {f _ {e ^ {+}} f _ {e ^ {-}}}{f _ {\nu} \bar {f} _ {\chi}} \gtrsim 6 1 \frac {m _ {\chi}}{\mathrm {k e V}} \gg 1, \tag {3.10}
$$

for the sub-MeV DM  $1\mathrm{keV}\lesssim m_{\chi}\lesssim 1\mathrm{MeV}$  clearly indicates that the first term of eq. (3.1) dominates over the second one [131].

# 3.3 Constraints from DM overproduction

To estimate the DM yield today  $Y_{0}$ , we assume there is no other mechanisms to produce/deplete DM after its production after the converging point  $T_{\mathrm{min}}$ . Then  $Y_{0} = Y(T_{\mathrm{min}})$  with time-independence since both the DM number density  $n_{\chi}$  and the entropy density  $s$  scale as  $1 / a^{3}$ . The DM relic density is estimated as,

$$
\Omega_ {\chi} h ^ {2} = \frac {2 m _ {\chi} Y _ {0} s _ {0} h ^ {2}}{\rho_ {c}}, \tag {3.11}
$$

where  $s_0 = 2970\mathrm{cm}^{-3}$  is the present entropy density and  $\rho_c = 1.054\times 10^{-5}h^2\mathrm{GeVcm}^{-3}$  the critical density. The Hubble constant  $h = 0.67$  is in unit of  $100\mathrm{km~s^{-1}Mpc^{-1}}$ . Since both DM and its anti-particle can be produced, there is a factor of 2 in the above estimation. Requiring the DM relic density to be less than the measured value,  $\Omega_{\chi}h^{2}\lesssim 0.12$ , sets a lower bound on the new physics scale  $\Lambda$  of the DM absorption operators in eq. (2.1). In other words, the DM relic density cannot be overproduced.

Figure 4 shows the constraints on the direct detection cross section  $\sigma_{\chi e}v_{\chi}$ . The excluded parameter space by the DM overproduction is shown as filled region with dashed boundary. These DM overproduction bounds are quite stringent in the low mass region, especially for the pseudo-scalar case. This is because for  $m_{\chi} \ll 2m_e$ , the cross-section scales as  $\sigma_{e^{-}e^{+}} \propto 1 / \Lambda^{4}$  and becomes independent of the DM mass according to eq. (3.7). Consequently, the DM yield  $Y$  estimated by eq. (3.6) is not sensitive to  $m_{\chi}$  and the DM relic density scales as  $\Omega_{\chi}h^{2} \propto m_{\chi} / \Lambda^{4}$ . However, the direct detection cross section in eq. (2.2) scales as power of the DM mass,  $\sigma_{\chi e}^{P}v_{\chi} \propto m_{\chi}^{4} / \Lambda^{4} \propto m_{\chi}^{3}\Omega_{\chi}$  for the pseudo-scalar case and  $\sigma_{\chi e}^{V,S,A,T}v_{\chi} \propto m_{\chi}^{2} / \Lambda^{4} \propto m_{\chi}\Omega_{\chi}$  for the others. This explains why the pseudo-scalar bound decreases faster with  $m_{\chi}$ . For the scalar, (axial-)vector, and tensor cases, they have a similar sensitivity around  $10^{-50}\mathrm{cm}^2$  to  $10^{-47}\mathrm{cm}^2$  for the DM mass from  $1\mathrm{keV}$  to  $1\mathrm{MeV}$ .

Using the more exactly calculated cross section  $\sigma_{\chi e}v_{\chi}$  as summarized in eq. (2.2), instead of the approximation  $m_{\chi}^{2} / 4\pi \Lambda^{4}$  in the  $m_{\chi}\ll m_e$  limit, for the vertical axis has some advantage. As explained below eq. (3.7), the  $e^{+}e^{-}\rightarrow \chi \nu$  cross section almost degenerates between scalar  $(\sigma_{e^{+}e^{-}}^{S})$  and pseudo-scalar  $(\sigma_{e^{+}e^{-}}^{P})$  operators. So one may expect their overproduction limits not to differ much and hard to distinguish in figure 4 if the universal  $m_{\chi}^{2} / 4\pi \Lambda^{4}$  is adopted. In contrast, the direct detection cross sections  $\sigma_{\chi e}^{S}v_{\chi}$  and  $\sigma_{\chi e}^{P}v_{\chi}$  have quite different scaling behaviors as discussed around eq. (2.2). So we can still see the clear

![](images/5df676d3d126deaa3080c832e6a4e2c13011261d95ace7d0a66234c38bff25be.jpg)  
Figure 4. The  $95\%$  C.L. constraints on the fermionic absorption operators from the DM overproduction (filled regions with dashed boundary), the cosmological evolution history (filled regions for invisible decay  $\chi \rightarrow 3\nu$  with dot-dashed boundary), as well as the astrophysical X(gamma)-ray data (filled regions for visible decays  $\chi \rightarrow \nu \gamma(s)$ ). The exclusion regions are filled with colors for scalar (S: green), pseduo-scalar (P: red), vector (V: blue), axial-vector (A: magenta), and tensor (T: cyan) operators, respectively. Note that the exclusion region for the tensor operator from astrophysical X(gamma)-ray constraint (T:  $\chi \rightarrow \nu \gamma$ ) uses dotted boundary to indicate that this constraint is subject to uncertainty in the regularization scheme. For comparison, the best-fit points (star) and  $95\%$  C.L. contours (contour) for the Xenon1T (light green) and PandaX-II (yellow) are also shown with the vector-type operator as an example.

difference between the scalar and pseudo-scalar cases in figure 4. In addition,  $\sigma_{\chi e}v_{\chi}$  also has the advantage of being able to reflect the realistic direct detection signal strength.

For comparison, the best-fit points (star) for Xenon1T (light green) and PandaX-II (yellow) are also shown. The best-fit values are taken from figure 2 for the vector case. We can see that for both data sets, the best-fit points are already at the boundary of the DM overproduction constraints. Also shown are the  $95\%$  C.L. allowed regions for the Xenon1T (light green contour) and PandaX-II (yellow contour) data. Consistent with the  $95\%$  C.L. contours in figure 2, the  $95\%$  C.L. allowed parameter space here is divided into 2 (3) regions for the Xenon1T (PandaX-II) data. The regions extend significantly down to a few keV of the DM mass  $m_{\chi}$ . More discussions about the cosmological constraints from the expansion history of the Universe and the astrophysical ones from various X(gamma)-ray observations will be discussed later in section 5.1 and section 5.2, respectively.

# 4 DM decay

One important feature of the DM absorption process is that only one DM particle can appear in the process as demonstrated by the general fermionic DM absorption operators in eq. (2.1). A natural consequence is that DM is unstable and can decay into light SM particles unless forbidden by kinematics. Since the DM particle is neutral, electron and positron should appear as a pair if such decay topology is possible. For  $\chi \rightarrow e^{+}e^{-} + \dots$  to happen, the DM mass has to be larger than twice of the electron mass,  $m_{\chi} > 2m_{e}$ , which is already outside the mass range considered in the current paper. The only possible decay products are the neutrinos and photons.

With the DM particle being a fermion, the final state has to contain an odd number of neutrinos, including the visible decay modes ( $\chi \rightarrow \nu + \gamma$ ,  $\chi \rightarrow \nu + \gamma \gamma$ , and  $\chi \rightarrow \nu + \gamma \gamma \gamma$ ) as well as the invisible mode  $\chi \rightarrow 3\nu$ . All these can happen only at loop level since the absorption operators in eq. (2.1) contains two electron fields. The leading 1-loop Feynman diagrams are listed in figure 5. For the visible decay modes, only electromagnetic interaction of the SM is needed in addition to the absorption operator. In contrast, the invisible decay mode  $\chi \rightarrow 3\nu$  requires the SM weak interactions with  $W / Z$  mediator.

To have a better understanding of the connection between operators and decay processes, table 1 summarizes the leading decay channels for each operator highlighted with a checkmark  $(\checkmark)$ . The cross  $(\times)$  indicates the decay channel that cannot be generated at 1-loop level. Although some can appear at two-loop level, they are hugely suppressed by loop factor, the weak scale, and/or phase space. For the  $\chi \rightarrow \nu \gamma \gamma \gamma$  and  $\chi \rightarrow 3\nu$  channels from the tensor operator, the  $\times!$  symbol is used to indicate that such processes can be generated at 1-loop order but heavily suppressed. In the following subsections we detail our calculation for each operator. The calculated decay width and spectrum are further used in section 5 to derive the cosmological and astrophysical constraints.

# 4.1 The scalar and pseudo-scalar operators  $\mathcal{O}_{e\nu \chi}^{S(P)}$

For the operators  $\mathcal{O}_{e\nu \chi}^{S,P}$  with an electron scalar or pseudo-scalar current, the dominant decay mode is  $\chi \rightarrow \nu +\gamma \gamma$ . As shown in figure 5(b), this process is generated through electron loop with two photons attached to the electron loop. The amplitudes from loop calculation are free from the UV divergence. Consequently, the decay widths can be calculated exactly,

$$
\Gamma_ {\chi \rightarrow \nu \gamma \gamma} ^ {S} = \frac {1}{\Lambda^ {4}} \frac {\alpha^ {2}}{2 0 4 8 \pi^ {5} m _ {e} ^ {2} m _ {\chi} ^ {3}} \int_ {0} ^ {m _ {\chi} ^ {2}} d s _ {1 2} s _ {1 2} ^ {2} (m _ {\chi} ^ {2} - s _ {1 2}) ^ {2} | F _ {S} (\eta) | ^ {2}, \tag {4.1a}
$$

$$
\Gamma_ {\chi \rightarrow \nu \gamma \gamma} ^ {P} = \frac {1}{\Lambda^ {4}} \frac {\alpha^ {2}}{2 0 4 8 \pi^ {5} m _ {e} ^ {2} m _ {\chi} ^ {3}} \int_ {0} ^ {m _ {\chi} ^ {2}} d s _ {1 2} s _ {1 2} ^ {2} (m _ {\chi} ^ {2} - s _ {1 2}) ^ {2} | F _ {P} (\eta) | ^ {2}, \qquad (4. 1 \mathrm {b})
$$

where  $\alpha \equiv e^4 / 4\pi$  is the electromagnetic fine structure constant. The integration variable  $s_{12}$  is the squared invariant mass of the two final-state photons, staring from 0 to the maximal value  $m_{\chi}^{2}$ . The loop functions  $F_{S,P}(\eta)$  with  $\eta \equiv s_{12} / m_e^2$  are,

$$
F _ {S} (\eta) \equiv \frac {4}{\eta} - \frac {\eta - 4}{\eta^ {2}} \ln^ {2} \frac {\sqrt {\eta - 4} - \sqrt {\eta}}{\sqrt {\eta - 4} + \sqrt {\eta}}, \tag {4.2a}
$$

$$
F _ {P} (\eta) \equiv - \frac {1}{\eta} \ln^ {2} \frac {\sqrt {\eta - 4} - \sqrt {\eta}}{\sqrt {\eta - 4} + \sqrt {\eta}}. \tag {4.2b}
$$

![](images/38a5836eba709886be18e06ce28417acac013dfa418e3a63355dce3b09d2cf65.jpg)  
(a)

![](images/aa241920aa566a301669f9f48cd984904b6a801f4e27f1a51c8a1d3782931a88.jpg)  
Figure 5. The representative Feynman diagrams contributing to the DM visible decays  $\chi \rightarrow \nu +\gamma (\mathrm{s})$  as well as the invisible decay  $\chi \rightarrow 3\nu$ . The blue vertex is the DM absorption operator while the others are SM interactions.  
(b)

![](images/d94211a51e8c34f97e91d0f53692e149e6dd6f6582e90e2f69f48e0f638dc50b.jpg)  
(c)

![](images/8f569c5f3a5d9631322f3f0c96f8597b5a6273511091f3340294bc283de267e3.jpg)  
(d)

![](images/c508670a180dd0e126206a1e525632d13e70e1b7213488b4a8a9b8dcc2387d58.jpg)  
(e)

Table 1. Contributions of the Fermionic DM absorption operators to the visible  $(\chi \rightarrow \nu \gamma (s))$  and invisible  $(\chi \rightarrow 3\nu)$  decay channels. The one allowed at one-loop level is shown with a checkmark  $(\checkmark)$  or a cross  $(\times)$  if otherwise. For those that allowed at one-loop level but highly suppressed, an exclaimed cross  $(\times !)$  is used.  

<table><tr><td>Operator\Process</td><td>\( \chi \rightarrow \nu \gamma \)</td><td>\( \chi \rightarrow \nu \gamma \gamma \)</td><td>\( \chi \rightarrow \nu \gamma \gamma \gamma \)</td><td>\( \chi \rightarrow 3\nu \)</td></tr><tr><td>S: \( \mathcal{O}_{e\nu \chi}^{S} \)</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>P: \( \mathcal{O}_{e\nu \chi}^{P} \)</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>V: \( \mathcal{O}_{e\nu \chi}^{V} \)</td><td>×</td><td>×</td><td>✓</td><td>✓</td></tr><tr><td>A: \( \mathcal{O}_{e\nu \chi}^{A} \)</td><td>×</td><td>✓</td><td>×</td><td>✓</td></tr><tr><td>T: \( \mathcal{O}_{e\nu \chi}^{T} \)</td><td>✓</td><td>×</td><td>×!</td><td>×!</td></tr></table>

In the limit of  $m_{\chi} \ll 2m_e$  and consequently  $s_{12} \ll m_e^2$ , the loop functions reduce to  $F_S(\eta) \approx 2/3$  and  $F_P(\eta) \approx 1$ . Then the decay widths above can be approximated as,

$$
\Gamma_ {\chi \rightarrow \nu \gamma \gamma} ^ {S} \approx 9. 4 \times 1 0 ^ {- 2 0} \sec^ {- 1} \left(\frac {m _ {\chi}}{2 0 0 \mathrm {k e V}}\right) ^ {7} \left(\frac {\mathrm {T e V}}{\Lambda}\right) ^ {4}, \tag {4.3a}
$$

$$
\Gamma_ {\chi \rightarrow \nu \gamma \gamma} ^ {P} \approx 2. 1 \times 1 0 ^ {- 1 9} \sec^ {- 1} \left(\frac {m _ {\chi}}{2 0 0 \mathrm {k e V}}\right) ^ {7} \left(\frac {\mathrm {T e V}}{\Lambda}\right) ^ {4}. \tag {4.3b}
$$

For the 2-body mode  $\chi \rightarrow \nu \gamma$  in figure 5(a) and the 4-body one  $\chi \rightarrow \nu \gamma \gamma \gamma$  in figure 5(c), the electron loop contribution vanishes due to the QED (quantum electrodynamics) charge conjugation symmetry. This is because the involved electron currents  $\bar{e} e$  and  $\bar{e}\gamma_{5}e$  have an even parity under charge conjugation transformation while the photon field is odd. With an odd number of photons, the one-loop diagram is odd and should vanish. Nonvanishing contribution can only be generated at the 2-loop level involving both QED and weak interactions. However, such a contribution is severely suppressed by the loop factor and weak scale such as  $m_e^2 / m_W^2$ . Therefore, we can neglect the single- and triple-photon contributions.

The 3-body invisible decay  $\chi \rightarrow 3\nu$  in the last two diagrams of figure 5 is also vanishing. The connection between the  $\chi \nu$  fermion lines at the top and the other two neutrinos is established through the  $\mathcal{O}_{e\nu \chi}^{S}$  and  $\mathcal{O}_{e\nu \chi}^{P}$  operators. Correspondingly, the effective current for the other two neutrinos after loop integration should also be of the same scalar feature as the  $\bar{e} e$  and  $\bar{e}\gamma_{5}e$  counterpart in the operator. Since the SM neutrinos are effectively

massless and purely left-handed, the only possibility is  $\partial_{\mu}(\bar{\nu}_{L}\gamma^{\mu}\nu_{L})$  with Lorentz indices fully contracted. Then, the equation of motion for a massless neutrino renders  $\partial_{\mu}\gamma^{\mu}\nu_{L}$  to vanish. Although constructing a Majorana mass term with only left-handed neutrinos is possible, lepton number is not violated in weak interactions and hence cannot appear without involving other new physics.

# 4.2 The vector operator  $\mathcal{O}_{e\nu \chi}^{V}$

For the vector operator, the 2-body  $\chi \rightarrow \nu \gamma$  and 3-body  $\chi \rightarrow \nu \gamma \gamma$  channels cannot arise at 1-loop level. The vanishing of  $\chi \rightarrow \nu \gamma$  is due to the gauge symmetry. As mentioned in the previous paragraph, the electron current  $\bar{e}\gamma_{\mu}e$  in the vector operator  $\mathcal{O}_{e\nu \chi}^{V}$  contributes to the loop mediator and needs to be integrated away with a remaining photon field as external state. This feature is generally parametrized as the matrix element  $\langle \gamma (q,\epsilon)|\bar{e}\gamma_{\mu}e|0\rangle$ . In the presence of an external photon, the matrix element is a linear function of its polarization vector  $\epsilon_{\mu}^{*}$ . Another quantity that can provide a Lorentz index is the momentum transfer  $q_{\mu}$ . The full matrix element also contains a piece  $\bar{u}_{\nu}\gamma^{\mu}P_{L}u_{\chi}$  from the neutrino side,

$$
\mathcal {M} \equiv \left[ A (q ^ {2}) q _ {\mu} \epsilon^ {*} \cdot q + B (q ^ {2}) \epsilon_ {\mu} ^ {*} \right] (\bar {u} _ {\nu} \gamma^ {\mu} P _ {L} u _ {\chi}) \equiv \epsilon_ {\mu} ^ {*} \mathcal {M} ^ {\mu}. \tag {4.4}
$$

The coefficients  $A(q^2)$  and  $B(q^2)$  correlate with each other by the QED Ward identity:  $q_{\mu}\mathcal{M}^{\mu} = 0$  from replacing the photon polarization vector  $\epsilon_{\mu}^{*}$  with its four-momentum  $q_{\mu}$ . Namely,

$$
\left[ A (q ^ {2}) q ^ {2} + B (q ^ {2}) \right] q _ {\mu} \left(\bar {u} _ {\nu} \gamma^ {\mu} P _ {L} u _ {\chi}\right) = 0. \tag {4.5}
$$

Since  $q^{\mu} \equiv p_{\chi}^{\mu} - p_{\nu}^{\mu}$ , the second term  $q_{\mu}(\bar{u}_{\nu}\gamma^{\mu}P_{L}u_{\chi}) = \bar{u}_{\nu}(\psi_{\chi} - \psi_{\nu})P_{L}u_{\chi} = m_{\chi}\bar{\nu}_{\nu}P_{R}u_{\chi} \neq 0$  is nonzero. Then the only solution is  $B(q^{2}) = -A(q^{2})q^{2}$  and the effective current,

$$
\langle \gamma (q, \epsilon) | \bar {e} \gamma_ {\mu} e | 0 \rangle = A (q ^ {2}) \left(q ^ {2} \epsilon_ {\mu} ^ {*} - q _ {\mu} \epsilon^ {*} \cdot q\right), \tag {4.6}
$$

vanishes due to the photon on-shell ( $q^2 = 0$ ) and transverse ( $\epsilon^{*} \cdot q = 0$ ) conditions. For the 2-photon decay  $\chi \rightarrow \nu \gamma \gamma$ , the loop part again contains 3 currents and hence vanishes due to the QED charge conjugation symmetry.

The dominant visible decay channel is the 4-body process  $\chi \rightarrow \nu \gamma \gamma \gamma$  whose matrix element can be generally parametrized as,

$$
\mathcal {M} _ {\nu \gamma \gamma \gamma} = - \frac {e ^ {3}}{1 6 \pi^ {2} \Lambda^ {2}} \left(\bar {u} _ {\nu} \gamma_ {\mu} P _ {L} u _ {\chi}\right) \epsilon_ {1 \alpha} ^ {*} \epsilon_ {2 \beta} ^ {*} \epsilon_ {3 \rho} ^ {*} \Pi^ {\mu \alpha \beta \rho}, \tag {4.7}
$$

where  $\epsilon_{i}^{*}$  is the polarization vector of the  $i$ -th final-state photon. The tensor  $\Pi^{\mu \alpha \beta \rho}$  is the reduced matrix element from the electron loop in figure 5(c). Correspondingly, the spin averaged squared matrix amplitude becomes,

$$
\overline {{| \mathcal {M} _ {\chi \rightarrow \nu \gamma \gamma \gamma} | ^ {2}}} = \frac {1 6 \alpha^ {3}}{\pi \Lambda^ {4}} \left\{- \frac {1}{4} \operatorname {T r} \left[ \not p _ {\nu} \gamma_ {\mu} \not p _ {\chi} \gamma_ {\nu} \right]\left(\frac {1}{8} \Pi^ {\mu \alpha \beta \rho}\right)\left(\frac {1}{8} \Pi_ {\alpha \beta \rho} ^ {\nu}\right)\right\}. \tag {4.8}
$$

The reduced matrix element  $\Pi^{\mu \alpha \beta \rho}$  is evaluated first analytically by Package-X [138] and then numerically by COLLIER [139]. The decay width is an integral over the 4-body phase space  $d\Phi_4$

$$
\Gamma_ {\chi \rightarrow \nu \gamma \gamma \gamma} ^ {V} = \frac {1}{3 !} \frac {1}{2 m _ {\chi}} \int d \Phi_ {4} \overline {{| \mathcal {M} _ {\chi \rightarrow \nu \gamma \gamma \gamma} | ^ {2}}}, \tag {4.9}
$$

with the factor  $1/3!$  to avoid phase space overcounting for the 3 identical photons. In the limit of  $m_{\chi} \ll 2m_e$ , the decay width also has a simple scaling behavior,

$$
\Gamma_ {\chi \rightarrow \nu \gamma \gamma \gamma} ^ {V} \approx 2. 6 \times 1 0 ^ {- 2 9} \sec^ {- 1} \left(\frac {m _ {\chi}}{2 0 0 \mathrm {k e V}}\right) ^ {1 3} \left(\frac {\mathrm {T e V}}{\Lambda}\right) ^ {4}. \tag {4.10}
$$

For the DM invisible decay  $\chi \rightarrow 3\nu$ , the loop diagrams (d) and (e) in figure 5 suffer from a UV divergence. To make a reasonable estimation, we use the dimensional regularization (DR) to tackle this issue. For the  $W$ -loop contribution, the amplitude in the unitary gauge is

$$
\mathcal {M} _ {\chi \rightarrow 3 \nu} ^ {W} = - \frac {\bar {u} _ {\nu} \gamma^ {\mu} P _ {L} u _ {\chi}}{\Lambda^ {2}} \frac {3 g _ {2} ^ {2}}{6 4 \pi^ {2}} \left[ 1 + \frac {m _ {e} ^ {2}}{m _ {W} ^ {2}} \left(\frac {1}{\epsilon} + \frac {1 1}{6} + \ln \frac {\Lambda^ {2}}{m _ {W} ^ {2}}\right) + \dots \right] [ \bar {u} _ {\nu_ {e}} (p _ {1}) \gamma_ {\mu} P _ {L} v _ {\nu_ {e}} (p _ {2}) ], \tag {4.11}
$$

where  $g_{2}$  is the weak coupling constant while  $\mu$  the dimensional regularization scale. The terms in the bracket is from the  $W$ -loop for generating the electron neutrino pair, and  $\cdots$  stand for terms suppressed by higher powers of  $q^{2} / m_{W}^{2}$ . Dropping the divergent piece  $1 / \epsilon$  altogether with the terms proportional to  $q^{2} / m_{W}^{2}$ , the finite amplitude used in our estimation is,

$$
\mathcal {M} _ {\chi \rightarrow 3 \nu} ^ {W} \approx - \frac {1}{\Lambda^ {2}} \frac {3 g _ {2} ^ {2}}{6 4 \pi^ {2}} \left(\bar {u} _ {\nu} \gamma^ {\mu} P _ {L} u _ {\chi}\right)\left[ \bar {u} _ {\nu_ {e}} \left(p _ {1}\right) \gamma_ {\mu} P _ {L} v _ {\nu_ {e}} \left(p _ {2}\right)\right]. \tag {4.12}
$$

The amplitude and decay width depend on the neutrino flavor that appears in the DM absorption operator. For  $(\bar{\nu}_e\gamma^\mu \chi_L)$ , there are two diagrams by exchanging the two electron neutrinos but only a single one for  $(\bar{\nu}_{\mu ,\tau}\gamma^{\mu}\chi_{L})$ . Considering this difference, the decay width for muon/tau flavor is,

$$
\Gamma_ {\chi \rightarrow 3 \nu} ^ {V} \approx \frac {m _ {\chi} ^ {5}}{1 5 3 6 \pi^ {3}} \left(\frac {3 g _ {2} ^ {2}}{6 4 \pi^ {2}}\right) ^ {2} \frac {1}{\Lambda^ {4}} \approx 3. 6 6 \times 1 0 ^ {- 1 7} \sec^ {- 1} \left(\frac {m _ {\chi}}{2 0 0 \mathrm {k e V}}\right) ^ {5} \left(\frac {\mathrm {T e V}}{\Lambda}\right) ^ {4}, \tag {4.13}
$$

and for the electron neutrino in  $\mathcal{O}_{e\nu \chi}^{V}$ , there is an additional enhancement factor 2. Note that the  $Z$  boson mediated diagram of figure 5(e) is always suppressed by  $1 / m_Z^2$  and hence can be neglected.

# 4.3 The axial-vector operator  $\mathcal{O}_{e\nu \chi}^{A}$

The dominant decay modes for the axial-vector operator  $\mathcal{O}_{e\nu \chi}^{A}$  are the 3-body decay  $\chi \rightarrow \nu \gamma \gamma$  and  $\chi \rightarrow 3\nu$ . This is because the 2-body mode  $\chi \rightarrow \nu \gamma$  and the 4-body one  $\chi \rightarrow \nu \gamma \gamma \gamma$  with an odd number of photons in the final state are forbidden by the QED charge conjugation symmetry.

First, the 3-body process  $\chi \rightarrow \nu \gamma \gamma$  is generated through the similar electron loop as the scalar and pseudo-scalar cases. The exact decay width is,

$$
\Gamma_ {\chi \rightarrow \nu \gamma \gamma} ^ {A} = \frac {1}{\Lambda^ {4}} \frac {\alpha^ {2}}{5 1 2 \pi^ {5} m _ {e} ^ {4} m _ {\chi}} \int_ {0} ^ {m _ {\chi} ^ {2}} d s _ {1 2} s _ {1 2} ^ {2} (m _ {\chi} ^ {2} - s _ {1 2}) ^ {2} | F _ {A} (\eta) | ^ {2}, \tag {4.14}
$$

where  $s_{12}$  is again the squared invariant mass of the two final-state photons and  $\eta \equiv s_{12} / m_e^2$ . The new loop function  $F_{A}(\eta)$ ,

$$
F _ {A} (\eta) \equiv - \frac {1}{\eta} - \frac {1}{\eta^ {2}} \ln^ {2} \frac {\sqrt {\eta - 4} - \sqrt {\eta}}{\sqrt {\eta - 4} + \sqrt {\eta}}, \tag {4.15}
$$

reduces to  $F_{A}(\eta) \approx 1 / 12$  in the limit of  $m_{\chi} \ll 2m_{e}$ . Accordingly, the decay width scales as

$$
\Gamma_ {\chi \rightarrow \nu \gamma \gamma} ^ {A} \approx 9 \times 1 0 ^ {- 2 2} \sec^ {- 1} \left(\frac {m _ {\chi}}{2 0 0 \mathrm {k e V}}\right) ^ {9} \left(\frac {\mathrm {T e V}}{\Lambda}\right) ^ {4}, \tag {4.16}
$$

for tiny DM mass. Note that the dependence on  $m_{\chi}$  is higher by 2 powers than that of the scalar and pseudo-scalar cases in eq. (4.3).

Second, the invisible decay  $\chi \rightarrow 3\nu$  shares the similar features as that of the vector case including the divergence. We use the same procedure to keep only the leading nondivergent term,

$$
\Gamma_ {\chi \rightarrow 3 \nu} ^ {A} \approx \frac {m _ {\chi} ^ {5}}{1 5 3 6 \pi^ {3}} \left(\frac {3 g _ {2} ^ {2}}{6 4 \pi^ {2}}\right) ^ {2} \frac {1}{\Lambda^ {4}} \approx 3. 6 6 \times 1 0 ^ {- 1 7} \sec^ {- 1} \left(\frac {m _ {\chi}}{2 0 0 \mathrm {k e V}}\right) ^ {5} \left(\frac {\mathrm {T e V}}{\Lambda}\right) ^ {4}. (4. 1 7)
$$

for the  $\mathcal{O}_{e\nu \chi}^{A}$  operator with a muon/tau neutrino. There is also an additional factor 2 for the electron neutrino case.

# 4.4 The tensor operator  $\mathcal{O}_{e\nu \chi}^{T}$

The dominant decay mode for the tensor operator is the 2-body decay  $\chi \rightarrow \nu \gamma$  in figure 5(a). However, it suffers from a UV divergence,

$$
\mathcal {M} _ {\chi \rightarrow \nu \gamma} = \frac {1}{\Lambda^ {2}} (\bar {u} _ {\nu} \sigma^ {\mu \nu} P _ {R} u _ {\chi}) \left[ - i \frac {e m _ {e} q _ {\mu} \epsilon_ {\nu} ^ {*}}{2 \pi^ {2}} \left(\frac {1}{\epsilon} + \ln \frac {\Lambda^ {2}}{m _ {e} ^ {2}}\right)\right], \qquad (4. 1 8)
$$

and needs to be regularized by the DR scheme. The vectors  $q_{\mu}$  and  $\epsilon_{\nu}^{*}$  are the outgoing photon momentum and polarization vector, respectively. After dropping the divergent factor  $1 / \epsilon$ , the decay width from the finite part becomes

$$
\Gamma_ {\chi \rightarrow \nu \gamma} ^ {T} = \frac {\alpha m _ {e} ^ {2} m _ {\chi} ^ {3}}{1 6 \pi^ {4} \Lambda^ {4}} \ln^ {2} \frac {\Lambda^ {2}}{m _ {e} ^ {2}} \approx 1. 5 \times 1 0 ^ {- 8} \sec^ {- 1} \left(\frac {m _ {\chi}}{2 0 0 \mathrm {k e V}}\right) ^ {3} \left(\frac {\mathrm {T e V}}{\Lambda}\right) ^ {4} \frac {\ln^ {2} (\Lambda^ {2} / m _ {e} ^ {2})}{1 0 0 0}, (4. 1 9)
$$

where the cut-off scale  $\Lambda$  enters through the log term. Since the logarithm is not sensitive to the change of  $\Lambda$ , we approximate it by a typical value  $\ln^2 (\Lambda^2 /m_e^2)\sim \mathcal{O}(10^3)$ . Comparing eq. (4.19) with eq. (4.3), eq. (4.10) and eq. (4.16), we see that the  $\chi \rightarrow \nu \gamma$  decay width for  $\mathcal{O}_{e\nu \chi}^{T}$  is much larger than the dominant visible decay width for all other operators. This implies that a much stronger constraint will be put on the tensor operator. Again, the 3-body channel  $\chi \rightarrow \nu \gamma \gamma$  vanishes due to the QED charge conjugation symmetry. In addition, the 4-body decay  $\chi \rightarrow \nu \gamma \gamma \gamma$  is suppressed by additional couplings as well as phase space factor.

For the invisible decay  $\chi \rightarrow 3\nu$ , as dictated by Lorentz invariance and the left-handedness of SM neutrinos, the electron tensor structure  $(\bar{e}\sigma^{\mu \nu}e)$  induces an effective operator  $(m_e / m_W^2)\partial^\mu (\bar{\nu}_L\gamma^\nu \nu_L)$  after loop integration. The electron mass  $m_{e}$  comes from the chirality flip introduced by the tensor operator. With the mass dimensions of  $m_{e}$  and  $\partial^{\mu}$  compensated by  $1 / m_W^2$ , this contribution is severely suppressed by a factor  $m_e^2 /m_W^2\sim 10^{-11}$  than  $\chi \rightarrow \nu \gamma$  and can be safely neglected.

# 5 The cosmological and astrophysical constraints on DM decays

As elaborated above, the DM absorption operators contain only one DM field. There is no intrinsic mechanism to forbid DM from decaying. This can provide some visible effect on the cosmological evolution history and the astrophysical observations via X-ray and gamma ray. This section evaluates first the constraints from cosmology in section 5.1 and astrophysical observations in section 5.2.

# 5.1 The cosmological evolution constraints on the DM invisible decay  $\chi \rightarrow 3\nu$

As illustrated in section 4, both the vector and axial-vector operators can have invisible decay  $\chi \rightarrow 3\nu$ . More importantly, the invisible decay mode dominates over the visible ones by at least 4 orders of magnitude. This can be seen by comparing eq. (4.10) with eq. (4.13), and eq. (4.16) with eq. (4.17). If a significant amount of the DM decays invisibly to inject its energy into relativistic degrees of freedom, the expansion history of the Universe can receive sizable modifications. Previous studies have already put quite strong constraints on the decaying DM scenario [140-143]. The currently most stringent constraint is  $\Gamma_{\mathrm{inv}}^{-1} < 468$  Gyr [144].

The constraints on  $\sigma_{\chi e}^{V,A}v_{\chi}$  are shown as dot-dashed lines in figure 4. The blue one is for the vector case while the magenta one for the axial-vector one. In the mass range  $40\mathrm{keV}\lesssim \mathrm{m}_{\chi}\lesssim 500\mathrm{keV}$ , the constraints from  $\chi \rightarrow 3\nu$  for the vector case is stronger than the DM overproduction and gamma-ray constraints. Together with the approximation  $\sigma_{\chi e}v_{\chi}\approx m_{\chi}^{2} / 4\pi \Lambda^{4}$ , the scaling behaviors  $\Gamma_{3\nu}^{V,A}\propto m_{\chi}^{5} / \Lambda^{4}$  in eq. (4.13) and eq. (4.17) renders the constraint to scale as  $\propto 1 / m_{\chi}^{3}$ . This estimation is consistent with the resulting curves shown in figure 4. For other operators, the  $\chi \rightarrow 3\nu$  channel is much smaller.

# 5.2 The astrophysical X-ray and gamma ray constraints on the visible decays  $\chi \rightarrow \nu +\gamma (\mathrm{s})$

Although the visible decays are typically much smaller than the invisible one as explored in section 4, it is much easier to observe photon than neutrino. This is especially true in the low energy range for sub-MeV DM. With DM distributing everywhere in the Universe and being especially concentrated in our Milky Way galaxy, the observation of diffuse X-ray and gamma ray can put stringent constraints on the decay width and therefore the cut-off scale  $\Lambda$ . We first describe how the DM visible decays contribute to the X(gamma)-ray observations in section 5.2.1 and then compare with the astrophysics observation data sets in section 5.2.2.

# 5.2.1 X-ray and gamma ray fluxes from the visible decays

Both galactic and extra-galactic sources of DM visible decay  $\chi \rightarrow \nu \gamma (s)$  can contribute to the X(gamma)-ray observations around our Earth. Typically the extra-galactic contributions are much smaller than the galactic counterpart. But for those diffuse cosmic fluxes, the major contribution comes from extra-galactic sources. So we will discuss both contributions below.

For DM decay, the galactic contribution is proportional to its local density  $\rho_{\chi} / m_{\chi}$  and the decay spectrum  $d\Gamma_{\chi} / dE_{\gamma}$  calculated in the rest frame of DM. So the differential photon flux per unit energy per solid angle is,

$$
\frac {d ^ {2} \Phi_ {\gamma}}{d E _ {\gamma} d \Omega} = \frac {1}{4 \pi} \frac {d \Gamma_ {\chi}}{d E _ {\gamma}} \int_ {\mathrm {l . o . s .}} ^ {s _ {\max }} \frac {\rho_ {\chi} (r)}{m _ {\chi}} d s, \tag {5.1}
$$

where  $d\Gamma_{\chi} / dE_{\gamma}$  is the corresponding differential decay width. The integration over the line of sight (l.o.s.) takes all the contribution along a specific direction. Note that the DM density  $\rho_{\chi}(r)$  is a direct function of the distance  $r$  from the galactic center. We adopt the NFW profile,  $\rho(r) = \rho_0 / [(r / r_s)(1 + r / r_s)^2]$  [145, 146], where  $r_s = 17\mathrm{kpc}$  [147] and  $\rho_0 = 0.43\mathrm{GeV/cm^3}$  to give the local DM density  $\rho_{\chi} \approx 0.4\mathrm{GeV/cm^3}$ . The distance  $r(s)$  is a function of the l.o.s. distance  $s$  in the galactic coordinate,

$$
r (s) = \sqrt {r _ {\odot} ^ {2} + s ^ {2} - 2 r _ {\odot} s \cos \psi}. \tag {5.2}
$$

In addition,  $r_{\odot} = 8.3\mathrm{kpc}$  is the distance of Earth to the galactic center and  $\cos \psi \equiv \cos b\cos l$ . The integration range for the l.o.s. distance  $s$  is from 0 to a maximal value determined by the virial radius  $r_{\mathrm{vir}} = 300\mathrm{kpc}$  of the DM halo [9],

$$
s _ {\max } = r _ {\odot} \cos \psi + \sqrt {r _ {\mathrm {v i r}} ^ {2} - r _ {\odot} ^ {2} \sin^ {2} \psi}. \tag {5.3}
$$

The extra-galactic contribution comes from the smooth DM distribution in the whole universe. Its contribution is isotropic and integrated over a large range of the redshift [148],

$$
\frac {d ^ {2} \Phi_ {r} ^ {\mathrm {E G}}}{d E _ {\gamma} d \Omega} = \frac {\Omega_ {\mathrm {D M}} \rho_ {c}}{4 \pi m _ {\chi} H _ {0} \sqrt {\Omega_ {m}}} \int_ {0} ^ {\infty} \frac {d \Gamma_ {\chi}}{d E _ {\gamma} (z)} \frac {d z}{\sqrt {\kappa + (1 + z) ^ {3}}}. \tag {5.4}
$$

The Hubble constant  $H_0 = 67.4\mathrm{km~sec}^{-1}\mathrm{Mpc}^{-1}$  and the cosmological critical density  $\rho_{c} = 5.8\times 10^{-6}\mathrm{GeVcm}^{-3}$  are present values. Of the total matter fraction  $\Omega_{m} = 0.315$ , DM takes the largest share  $\Omega_{\mathrm{DM}} = 0.265$ . In addition, the dark energy (DE) also has a large effect on the cosmological evolution, especially in the late stage. We use  $\kappa \equiv \Omega_{\Lambda} / \Omega_{m} = 2.17$  to parametrize the contribution of DE. The decay width and spectrum calculated in section 4 cannot be used directly. Due to cosmological redshift, the photon energy  $E_{\gamma}(z) = (1 + z)E_{\gamma}$  emitted at redshift  $z$  is  $1 + z$  times of the apparent  $E_{\gamma}$ .

The total photon flux  $d^{2}\Phi_{r} / dE_{\gamma}d\Omega$  due to DM decay is then a sum of the above two components. For a telescope with effective area  $A_{\mathrm{eff}}$  and field of view (FOV)  $\Delta \Omega$  as well as exposure time  $T_{\mathrm{obs}}$ , the predicted photon event rate in energy bin  $[E_i^{-},E_i^{+}]$  is

$$
N _ {i} ^ {\mathrm {t h}} \equiv A _ {\mathrm {e f f}} T _ {\mathrm {o b s}} \int_ {E _ {i} ^ {-}} ^ {E _ {i} ^ {+}} d E _ {\gamma} \int_ {\Delta \Omega} d \Omega \frac {d ^ {2} \Phi_ {\gamma}}{d E _ {\gamma} d \Omega}. \tag {5.5}
$$

Below we use real data to constrain the DM decay width and subsequently the DM coupling strength.

![](images/2b032c5964990fc8b812f04a294fa0c1b2236cf0d62e2e09a5e75a8b11075441.jpg)  
Figure 6. The observed X(gamma)-ray fluxes by Insight-HXMT/CXB (blue) [149], NuSTAR/CMB (red) [150], NuSTAR/M31 (cyan) [151], HEOA-1 (green) [152], INTEGRAL (magenta, yellow, and black) [153, 154]. The three INTEGRAL data sets are released in 2008 (magenta) [153] and 2011 (yellow for 11C and black for 11R) [154] for different observational sky regions as described in the main text.

# 5.2.2 Constraints from astrophysical X-ray and gamma ray data in the keV-MeV range

As argued at the beginning of section 2, we are interested in the DM mass range between keV and MeV. The relevant observations in our analysis include Insight-HXMT [149], NuSTAR [150, 151], HEAO-1 [152], and INTEGRAL [153, 154]. Figure 6 summarizes the observed X(gamma)-ray data. Most data sets are used to constrain the fermionic DM absorption operators for the first time with the only exception of HEAO-1 and INTEGRAL/08 [148]. The constraints on the DM decay width  $\Gamma_{\chi}$  are shown in figure 7 while the constraints on the interaction strength in terms of the direct detection cross section  $\sigma_{\chi e}v_{\chi}$  have already been included in figure 4 altogether.

To constrain the DM decay width  $\Gamma_{\chi}$ , we require the predicted photon events in each energy bin does not exceed the experimental counts at  $95\%$  C.L. In a single energy bin  $[E_i^{-}, E_i^{+}]$ , the constraint is obtained with

$$
N _ {i} ^ {\mathrm {t h}} \leq N _ {i} ^ {\mathrm {o b s}} \equiv A _ {\mathrm {e f f}} T _ {\mathrm {o b s}} \Delta \Omega \left(\frac {d ^ {2} \Phi_ {\gamma}}{d E _ {\gamma} d \Omega}\right) _ {\exp @ 95 \%} ^ {i} \Delta E _ {i}. \tag{5.6}
$$

In principle, one may directly compare the predicted flux  $d^2\Phi_r / dE_\gamma d\Omega$  with the data in

![](images/2de426de876e825e2d5216a0ed596a7b7c44e6d8acaf140f17e7ceeedfbcfd95.jpg)  
Figure 7. The astrophysical X-ray and gamma-ray constraints on the visible decay width of  $\chi \rightarrow \nu +\gamma (s)$  as a function of the DM mass  $m_{\chi}$ . For illustration, the vector operator with continuum spectrum from  $\chi \rightarrow \nu \gamma \gamma \gamma$  and the tensor one with discrete  $\delta$ -function from  $\chi \rightarrow \nu \gamma$  are shown in the left and right panels, respectively.

![](images/c153c9c48a81d10f90dcec1c28e74983ae46792c08ad44242971bdf5557ad22c.jpg)

figure 6 without converting to event number in each bin. Nevertheless, the spectrum of the two-body channel  $\chi \rightarrow \nu \gamma$  for the tensor operator  $\mathcal{O}_{e\nu \chi}^{T}$  is a  $\delta$  function which is difficult to directly compare with figure 6. With multiple data points, we can obtain a corresponding limit for the decay width  $\Gamma_{\chi}^{i}$  from the  $i$ -th energy bin, and we take the strongest bound among all bins as the final limit for the corresponding mass point.

Some data releases, especially Insight-HXMT [149] and NuSTAR/M31 [151], even provide background models in addition to data points. This opens the possibility to use  $\chi^2$  fit to obtain enhanced sensitivity than simply comparing with the central value plus the  $95\%$  C.L. uncertainty for individual bins. Putting things together, the corresponding  $\chi^2$  function for fitting the Insight-HXMT or NuSTAR/M31 data is,

$$
\chi^ {2} (x _ {i}, \Lambda) \equiv \sum_ {i} \left[ \frac {\Lambda_ {\mathrm {T e V}} ^ {- 4} N _ {i} ^ {\mathrm {D M}} (\Lambda = 1 \mathrm {T e V}) + \sum_ {a} c _ {a} N _ {i} ^ {a} - N _ {i} ^ {\mathrm {e x p}}}{\delta N _ {i}} \right] ^ {2}, \tag {5.7}
$$

where  $\Lambda_{\mathrm{TeV}} \equiv \Lambda / \mathrm{TeV}$ . The observation data provides the central values  $N_i^{\mathrm{exp}}$  and the corresponding uncertainty  $\delta N_i$  for the  $i$ -th bin. Each observation can have multiple backgrounds  $N_i^a$  with  $a$  denoting its type and  $c_a$  the corresponding normalization factor. The  $\chi^2$  fit with data takes  $c_a$  as fitting parameters while the one for the DM contribution is the cut-off scale  $\Lambda_{\mathrm{TeV}}$  in unit of  $\mathrm{TeV}$ . More details of the analytic  $\chi^2$  fit can be found in appendix A.

Below is a detailed description of each data set and their constraints on the DM decay width and coupling strength.

- Insight-HXMT/CXB: we use the  $(1\sim 12)$  keV cosmic X-ray background (CXB) data observed by the Low Energy X-ray Telescope on Insight-HXMT (Hard X-ray Modulation Telescope) [149]. The observation points to the sky in the direction  $(l,b) = (219.3^{\circ}, -50.0^{\circ})$  with a small FOV  $(1.6^{\circ}\times 6^{\circ})$ . The relevant effective detector area is taken from figure 1 on the HXMT website [155]. For comparison, the

background model for CXB is taken from the yellow line of figure 11 therein. With both data points and background model provided, we use analytic  $\chi^2$  fit to obtain constraint. The result is shown in figure 7 with blue color. In the  $\mathcal{O}(1)\mathrm{keV}$  range, Insight-HXMT/CXB gives a strong constraint.

- NuSTAR/CXB: figure 10 of [150] gives the average CXB spectrum within the  $(3\sim 20)\mathrm{keV}$  energy range. This spectrum is obtained by stacking the focal plane module (FPM) A and B (FPMA and FPMB) observations with all six data sets (COSMOS EP1,2,3, EGS, ECDFS, UDS).  
- NuSTAR/M31: in addition to the diffuse CXB, galaxy observation can also provide a strong constraint due to the concentrated DM density profile. A typical case is the NuSTAR observation of M31. We use the  $(5\sim 100)$  keV data in figure 2 of [151] from the observation ID 50026002003. The NuSTAR instrumental and solar contributions, the 0-bounce CXB component, and the 2-bounce component from the diffuse M31 emission are taken into consideration as backgrounds. Here the 0-bounce photons refer to the unfocused X-rays while the 2-bounce photons are those reflected twice in the telescope. The background models are taken from the fit curves in figure 2 of [151]. Each component has its own normalization factor as fitting parameter. Since the 2-bounce CXB component is very small, we neglect it in our  $\chi^2$  fit to avoid numerical instability.

For the DM decay photons, the 0-bounce and 2-bounce DM decay photons have different effective areas. To properly take the 2-bounce contribution into account, we use the enhancement factor defined in [151],

$$
\xi \left(E _ {\gamma}\right) \equiv 1 + \frac {A _ {2 \mathrm {b}} \left(E _ {\gamma}\right) \Delta \Omega_ {2 \mathrm {b}} \mathcal {J} _ {2 \mathrm {b}}}{A _ {0 \mathrm {b}} \Delta \Omega_ {0 \mathrm {b}} \mathcal {J} _ {0 \mathrm {b}}}. \tag {5.8}
$$

Then the predicted DM decay photon events in each energy bin can be written as,

$$
N _ {i} ^ {\mathrm {D M}} \equiv A _ {0 \mathrm {b}} T _ {\mathrm {o b s}} \Delta \Omega_ {0 \mathrm {b}} \frac {\mathcal {I} _ {0 \mathrm {b}}}{4 \pi m _ {\chi}} \int d E _ {\gamma} \xi \left(E _ {\gamma}\right) \frac {d \Gamma_ {\gamma}}{d E _ {\gamma}}, \tag {5.9}
$$

where the observational effective area for the 0-bounce photons is  $A_{0b} = 11.85$  (11.80) cm $^2$ , the exposure time is  $T_{\mathrm{obs}} = 82.4$  (82.2) ks and the FOV  $\Delta \Omega_{0b} = 4.45$  (4.55) deg $^2$  for the FPMA (FPMB) observation, respectively. The DM decay factor  $\mathcal{I}_{0\mathrm{b}} = 6.72$  (7.13) GeV cm $^{-3}$  kpc sr $^{-1}$  for FPMA (FPMB) includes both the Milky Way and M31 contributions. One can neglect the extragalactic contribution which is much smaller.

- HEOA-1: the HEAO-1 extragalactic diffuse X-ray data in figure 2 of [152] corresponds to the sky region  $l \in (58^{\circ}, 106^{\circ}) \cup (238^{\circ}, 289^{\circ}), |b| \in (20^{\circ}, 90^{\circ})$ . Following [148], we only use the  $(3 \sim 50)$  keV data set observed by the A2 High-Energy Detector (HED).  
- INTEGRAL: we use both the galactic center gamma-ray spectrum  $(|b| < 15^{\circ}$  and  $|l| < 30^{\circ})$  as well as the galactic ridge emission spectrum from the SPI measurements on board INTEGRAL. 1) There are two data sets for the galactic center gamma-ray spectrum with photon energy  $(20\sim 2000)\mathrm{keV}$ . One is from figure 9 of [153]

released in 2008 and shown as INTEGRAL/08 (magenta) in figure 6 while the other comes from figure 6 of [154] released in 2011 and shown as INTEGRAL/11C (yellow). 2) For the galactic ridge emission spectrum, figure 4 of [154] gives the diffuse emission as a function of galactic longitude with the latitude being integrated over and figure 5 therein gives the one with the longitude being integrated over. The INTEGRAL measurements from this analysis are divided into five energy bins with divisions at  $E = (27,49,100,200,600,1800) \mathrm{keV}$ , respectively. We select those bins that give the strongest limit and show their corresponding fluxes in figure 6 as INTEGRAL/11R (black).

Figure 7 compiles all the astrophysical X-ray and gamma-ray constraints on the DM visible decay. While the photon energy is typically smaller than half of the DM mass,  $E_{\gamma} < m_{\chi} / 2$ , the energy range (1 ~ 3000) keV in figure 6 covers the DM mass window (2 ~ 1000) keV in figure 7. Although there are three different decay channels,  $\chi \rightarrow (\nu \gamma, \nu \gamma \gamma, \nu \gamma \gamma \gamma)$ , the last two share similar features of continuum spectrum while the first has a discrete  $\delta$  function. For illustration purpose, we only show the vector and tensor cases in the left and right panels of figure 7, respectively. Due to this difference, the curves for the vector case are quite smooth while the tensor ones have many breaks and spikes. In addition, the tensor case typically has much clearer boundaries such as the NuSTAR/M31 curve. The results for  $\chi \rightarrow \nu \gamma \gamma$  are quite similar to those of  $\chi \rightarrow \nu \gamma \gamma \gamma$ .

It is interesting to observe that, although the NuSTAR/M31 flux in figure 6 is not as small as other observations, its constraint on the DM visible decay width is not bad and even better than some others such as INTEGRAL. This is because the INTEGRAL constraints come from comparing the theoretical prediction with all observed event counts plus errors at  $95\%$  C.L. while the NuSTAR/M31 constraint is from a more realistic  $\chi^2$  fit. If possible,  $\chi^2$  fit is more desirable although doing this for all astrophysical data is beyond the scope of the current paper.

Another important feature is that, the constraining power can go beyond the  $E_{\gamma} < m_{\chi} / 2$  correspondence. Taking the Insight-HXMT curve for demonstration, the adopted spectrum spans the energy range (1~12) keV while the constrained mass range can extend up to  $\mathcal{O}(100)\mathrm{keV}$ . This is because the extragalactic contributions from the vast Universe receive redshift to different extent. Although the emitted photon spectrum is fixed by the DM mass  $m_{\chi}$  and the decay vertex, the observed photon energy could be much lower. A heavier  $m_{\chi}$  above the energy window can also receive constraint from low energy X-ray observation.

The constraints in terms of the direct detection cross section  $\sigma_{\chi e}v_{\chi}$  have already been shown in figure 4 for comparison. Comparing with the overproduction constraints, the decay constraints are typically more stringent for heavier DM for both the invisible and visible channels. This is because the decay width typically grows with the DM mass. The constraint for the tensor operator is particularly strong since it comes from the single photon channel  $\chi \rightarrow \nu \gamma$  with much larger phase space. The next highly constrained operator is the pseudo-scalar type. Neither the freeze-in production nor decay process of the pseudoscalar operator is suppressed. So the constraints on its cut-off scale should be roughly the same as others. However, the direct detection cross section is highly suppressed for the

pseudo-scalar case. Both pseudo-scalar and tensor operators are difficult to be directly probed. The constraints on the other operators are not that severe. Of them, the vector case is of particular interest for tonne-scale direct detection experiments (such as PandaX-4T [156, 157], XENONnT [158], and LZ [159, 160]) which will soon be able to probe small DM mass  $m_{\chi}$  of  $\mathcal{O}(10 \sim 100) \mathrm{keV}$  that has not been excluded by cosmological or astrophysical constraints.

# 6 Conclusions

We systematically investigated the effective operators for fermionic DM absorption on electron targets that allow a unique probe of sub-MeV DM. Using the effective fermionic absorption operators, we found that the electron recoil spectrum in direct detection has roughly the same shape that is mainly determined by the atomic  $K$ -factor for different operators. This allows a model-independent, or at least operator-independent, measurement to some extent. If the fermionic DM absorption is confirmed, the shape of the  $K$ -factor can even be reconstructed from the electron recoil spectrum. The only complication is that the pseudo-scalar case has quite different signal size. The comparison with the Xenon1T and PandaX-II electron recoil spectrum prefers a vector-type DM absorption with  $m_{\chi} = 59$  keV and  $105$  keV respectively. With the corresponding best-fit value  $\Lambda \approx 1$  TeV, the Xenon1T and PandaX-II can probe the new physics cut-off scale up to TeV scale. We also systematically update the overproduction, cosmological, and astrophysical constraints. Especially, the X(gamma)-ray constraints from the Insight-HXMT, NuSTAR, and INTEGRAL 2011 data sets are newly used to constrain the sub-MeV fermionic absorption DM. Even though the tensor and pseudo-scalar operators are strongly constrained, the fermionic DM absorption with other operator types is still testable at tonne-scale experiments.

# Acknowledgments

The authors would like to thank Roman Krivonos, Lei Lei, Jin-Yuan Liao, Jiang-Lai Liu, Dan Zhang, and Shuang-Nan Zhang for useful discussions. The authors thank Kenny C.Y. Ng for providing us the NuSTAR/M31 data, the  $\mathcal{I}$  factor and the enhancement factor of the 2 bounce FOV in their paper [151]. The authors also thank Jeff A. Dror for double-checking the results in [113]. This work is supported in part by the Double First Class start-up fund (WF220442604), the Shanghai Pujiang Program (20PJ1407800), National Natural Science Foundation of China (Nos. 12090064, 11975149, 11735010), Chinese Academy of Sciences Center for Excellence in Particle Physics (CCEPP), and Key Laboratory for Particle Physics, Astrophysics and Cosmology, Ministry of Education, and Shanghai Key Laboratory for Particle Physics and Cosmology (Grant No. 15DZ2272100). XGH was also supported in part by the MOST (Grant No. MOST 109-2112-M-002-017-MY3).

# A Analytic  $\chi^2$  fit with collective marginalization

The fitting with experimental data points in this paper is achieved with analytical  $\chi^2$  fit [123, 124]. With Gaussian distribution, the  $\chi^2$  minimization is equivalent to matrix

manipulation. Most importantly, the marginalization for a single parameter can also be done as matrix element manipulation to reduce a  $\chi^2$  function with  $n$  parameters to the one with  $n - 1$  parameters. This single-parameter marginalization needs to be done recursively in order to marginalize over multiple parameters. Here we provide a more elegant formalism to marginalize over multiple parameters collectively.

Given a set of observables  $\mathcal{O}_j$ , the  $\chi^2$  function can be generally parametrized as,

$$
\chi^ {2} = \sum_ {j} \left(\frac {\mathcal {O} _ {j} ^ {\mathrm {t h}} - \mathcal {O} _ {j} ^ {\exp}}{\Delta \mathcal {O} _ {j}}\right) ^ {2}, \tag {A.1}
$$

where  $\mathcal{O}_j^{\mathrm{th}}$  and  $\mathcal{O}_j^{\mathrm{exp}}$  are the theoretical prediction and experimental observation for the  $j$ -th bin, respectively. A Gaussian  $\chi^2$  function is equivalent to linear dependence of  $\mathcal{O}_j^{\mathrm{th}}$  on the model parameters  $x_i$ ,  $(i = 1,2,\ldots,n)$  as  $\mathcal{O}_j^{\mathrm{th}} \approx \mathcal{O}_j^{\mathrm{th},0} + \sum_i A_{ji} x_i$ . In matrix form, the  $\chi^2$  function can be written as

$$
\chi^ {2} \left(x _ {i}\right) = \left(\mathcal {O} ^ {\mathrm {t h}, 0} + A x - \mathcal {O} ^ {\exp}\right) ^ {\mathrm {T}} \overline {{\Sigma}} ^ {- 1} \left(\mathcal {O} ^ {\mathrm {t h}, 0} + A x - \mathcal {O} ^ {\exp}\right), \quad \overline {{\Sigma}} ^ {- 1} \equiv \operatorname {d i a g} \left(\Delta \mathcal {O} _ {j} ^ {- 2}\right). \tag {A.2}
$$

For  $m$  observables and  $n$  fitting parameters,  $A$  is a  $m \times n$  constant coefficient matrix and  $x \equiv (x_{1},\dots ,x_{n})^{T}$  is a  $n \times 1$  column vector. Then  $A$  converts the  $n \times 1$  parameter vector  $x$  to a  $m \times 1$  observable vector  $Ax$  that can match with  $\mathcal{O}^{\mathrm{th},0}$  and  $\mathcal{O}^{\mathrm{exp}}$ . Finally, the  $m \times m$  error matrix  $\overline{\Sigma}^{-1}$  in the observable space contracts with two observable vectors, one column and one row vectors, to produce a scalar  $\chi^2$  function. By definition, error matrix is symmetric.

The  $\chi^2$  minimization condition  $\partial \chi^2 / \partial x_i \equiv 0$  gives a unique solution for the best-fit value of the fitting parameters,

$$
x _ {\text {b e s t}} \equiv \left(A ^ {T} \bar {\Sigma} ^ {- 1} A\right) ^ {- 1} A ^ {T} \bar {\Sigma} ^ {- 1} \left(\mathcal {O} ^ {\text {t h}, 0} - \mathcal {O} ^ {\text {e x p}}\right). \tag {A.3}
$$

With larger deviation between the experimentally observed  $\mathcal{O}^{\mathrm{exp}}$  and the zeroth-order prediction  $\mathcal{O}^{\mathrm{th},0}$ , the fitting parameter should also deviate more from the one used to predict  $\mathcal{O}^{\mathrm{th},0}$ . Correspondingly, the  $\chi^2$  function splits into two parts

$$
\chi^ {2} (x _ {i}) = \chi_ {\mathrm {m i n}} ^ {2} + (x - x _ {\mathrm {b e s t}}) ^ {T} \Sigma^ {- 1} (x - x _ {\mathrm {b e s t}}), \tag {A.4}
$$

Now  $\chi^2$  becomes a function of fitting parameters  $x_{i}$ , instead of observables, with the corresponding  $n\times n$  error matrix  $\Sigma^{-1}\equiv A^{T}\overline{\Sigma}^{-1}A$  in the parameter space. The first term of eq. (A.4) is the minimum value of the  $\chi^2$ ,

$$
\chi_ {\min } ^ {2} \equiv (\mathcal {O} ^ {\mathrm {t h}, 0} - \mathcal {O} ^ {\exp}) ^ {T} B ^ {\mathrm {T}} \bar {\Sigma} ^ {- 1} B (\mathcal {O} ^ {\mathrm {t h}, 0} - \mathcal {O} ^ {\exp}) ^ {T}, B \equiv \mathbb {I} - A (A ^ {T} \bar {\Sigma} ^ {- 1} A) ^ {- 1} A ^ {T} \bar {\Sigma} ^ {- 1}, \tag {A.5}
$$

while the second is actually  $\delta \chi^2 (x_i)$  as deviation from  $\chi_{\mathrm{min}}^2$

With multiple fitting parameters in eq. (A.4), it is difficult to see the probability distribution of any specific one. It is desirable to obtain the  $\chi^2$  of a single parameter by marginalizing over the others. This can be achieved by integrating out the unnecessary ones from the distribution function  $\mathbb{P}(x_1, \dots, x_n)$ . Taking one-parameter reduction for illustration,

$$
\mathbb {P} \left(x _ {1}, \dots , \hat {x} _ {k}, \dots , x _ {n}\right) = \int \mathbb {P} \left(x _ {1}, \dots , x _ {n}\right) d x _ {k}, \tag {A.6}
$$

where the  $k$ -th element is marginalized. For a Gaussian distribution, this is equivalent to matrix element manipulation of the error matrix  $\Sigma^{-1}$  in the parameter space,

$$
\widetilde {\Sigma} _ {i j} ^ {- 1} = \Sigma_ {i j} ^ {- 1} - \frac {\Sigma_ {i k} ^ {- 1} \Sigma_ {j k} ^ {- 1}}{\Sigma_ {k k} ^ {- 1}}. \tag {A.7}
$$

While  $\Sigma^{-1}$  being a  $n\times n$  matrix,  $\widetilde{\Sigma}^{-1}$  is  $(n - 1)\times (n - 1)$  after marginalizing one single parameter  $x_{k}$ . Keeping doing this repeatedly, one can finally arrive at a  $\chi^2$  function with only one parameter.

Nevertheless, this procedure is a little bit troublesome with  $n - 1$  repetition when  $n$  becomes large. Below we provide a more convenient algorithm of collective marginalization which can reduce a  $n$ -parameter  $\chi^2$  function directly to a single-parameter one without repetition. Suppose one needs to marginalize over  $k$  parameters out of the original  $n$  ones. Instead of using a single  $n \times 1$  vector  $x$ , the fitting parameters can be separated into one  $(n - k) \times 1$  vector  $X$  that shall remain and one  $k \times 1$  vector  $Y$  that needs to be marginalized away. Correspondingly, the experimental observables are predicted as

$$
\mathcal {O} ^ {\text {t h}, 0} + A _ {X} X + A _ {Y} Y, \tag {A.8}
$$

instead of the original  $\mathcal{O}^{\mathrm{th},0} + Ax$ . The  $\chi^2$  function eq. (A.2) then becomes

$$
\chi^ {2} (X, Y) = \left(\mathcal {O} ^ {\text {t h}, 0} + A _ {X} X + A _ {Y} Y - \mathcal {O} ^ {\exp}\right) ^ {T} \bar {\Sigma} ^ {- 1} \left(\mathcal {O} ^ {\text {t h}, 0} + A _ {X} X + A _ {Y} Y - \mathcal {O} ^ {\exp}\right). \tag {A.9}
$$

For convenience, one may define  $\delta \mathcal{O}_X\equiv \mathcal{O}^{\mathrm{th},0} + A_XX - \mathcal{O}^{\mathrm{exp}}$  and the  $\chi^2 (X,Y)$  function becomes,

$$
\chi^ {2} (X, Y) = Y ^ {T} \Sigma_ {Y} ^ {- 1} Y + 2 Y ^ {T} A _ {Y} ^ {T} \bar {\Sigma} ^ {- 1} \delta \mathcal {O} _ {X} + \delta \mathcal {O} _ {X} ^ {T} \bar {\Sigma} ^ {- 1} \delta \mathcal {O} _ {X}, \tag {A.10}
$$

with  $\Sigma_Y^{-1} \equiv A_Y^T \overline{\Sigma}^{-1} A_Y$ . Only the first two terms are relevant in the Gaussian integration of the marginalization of  $Y$ ,

$$
\mathbb {P} (X) = \int \mathbb {P} (X, Y) d Y = N \int e ^ {- \frac {1}{2} \chi^ {2} (X, Y)} d Y, \tag {A.11}
$$

with a normalization factor  $N$  that would not affect the probability distribution. The result would be more transparent by reforming eq. (A.10) as,

$$
\begin{array}{l} \chi^ {2} (X, Y) = \left(Y + \Sigma_ {Y} A _ {Y} ^ {T} \bar {\Sigma} ^ {- 1} \delta \mathcal {O} _ {X}\right) ^ {T} \Sigma_ {Y} ^ {- 1} \left(Y + \Sigma_ {Y} A _ {Y} ^ {T} \bar {\Sigma} ^ {- 1} \delta \mathcal {O} _ {X}\right) \\ + \delta \mathcal {O} _ {X} ^ {T} \left[ \bar {\Sigma} ^ {- 1} - \bar {\Sigma} ^ {- 1} A _ {Y} \Sigma_ {Y} A _ {Y} ^ {T} \bar {\Sigma} ^ {- 1} \right] \delta \mathcal {O} _ {X}. \tag {A.12} \\ \end{array}
$$

The first line is a Gaussian form of  $Y$  while the second line is independent of  $Y$ . Then the Gaussian integration eq. (A.11) gives,

$$
\mathbb {P} (X) \propto \exp \left[ - \frac {1}{2} \left(\mathcal {O} ^ {\text {t h}, 0} + A _ {X} X - \mathcal {O} ^ {\text {e x p}}\right) ^ {T} \overline {{\Sigma}} _ {X} ^ {- 1} \left(\mathcal {O} ^ {\text {t h}, 0} + A _ {X} X - \mathcal {O} ^ {\text {e x p}}\right) \right], \tag {A.13}
$$

up to a normalization factor. Since a Gaussian probability distribution is defined as  $\mathbb{P}(X) \propto e^{-\chi^2(X)/2}$ , one can read off the reduced  $\chi^2(X)$  directly from the above equation. The reduced experimental error matrix,

$$
\bar {\Sigma} _ {X} ^ {- 1} \equiv \bar {\Sigma} ^ {- 1} - \bar {\Sigma} ^ {- 1} A _ {Y} \Sigma_ {Y} A _ {Y} ^ {T} \bar {\Sigma} ^ {- 1}, \tag {A.14}
$$

with only parameters  $X$  replaces the original  $\overline{\Sigma}^{-1}$ . It is interesting to observe that the reduced  $\chi^2(X)$  in eq. (A.13) resembles the original form eq. (A.2). The effect of  $Y$  parameters is wholly encoded in  $\overline{\Sigma}_X^{-1}$ . It not only affects the  $X$  error matrix,  $\Sigma_X^{-1} \equiv A_X^T \overline{\Sigma}_X^{-1} A_X$ , but also its best-fit values. The marginalization down to a single parameter corresponds to  $k = n - 1$ .

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] B.-L. Young, A survey of dark matter and related topics in cosmology, Front. Phys. (Beijing) 12 (2017) 121201 [Erratum ibid. 12 (2017) 121202] [INSPIRE].  
[2] A. Arbey and F. Mahmoudi, Dark matter and the early Universe: a review, Prog. Part. Nucl. Phys. 119 (2021) 103865 [arXiv:2104.11488] [INSPIRE].  
[3] J. Liu, X. Chen and X. Ji, Current status of direct dark matter detection experiments, Nature Phys. 13 (2017) 212 [arXiv:1709.00688] [INSPIRE].  
[4] J. Billard et al., Direct Detection of Dark Matter — APPEC Committee Report, arXiv:2104.07634 [INSPIRE].  
[5] R.K. Leane, Indirect Detection of Dark Matter in the Galaxy, arXiv:2006.00513 [INSPIRE].  
[6] T.R. Slatyer, Les Houches Lectures on Indirect Detection of Dark Matter, in proceedings of the Les Houches Summer School on Dark Matter, Les Houches, France, 26 July–20 August 2021, arXiv:2109.02696 [INSPIRE].  
[7] A. Albert et al., Towards the next generation of simplified Dark Matter models, Phys. Dark Univ. 16 (2017) 49 [arXiv:1607.06680] [INSPIRE].  
[8] K. Arun, S.B. Gudennavar and C. Sivaram, Dark matter, dark energy, and alternate models: A review, Adv. Space Res. 60 (2017) 166 [arXiv:1704.06155] [INSPIRE].  
[9] T. Lin, Dark matter models and direct detection, PoS 333 (2019) 009 [arXiv:1904.07915] [INSPIRE].  
[10] L. Roszkowski, E.M. Sessolo and S. Trojanowski, WIMP dark matter candidates and searches — current status and future prospects, Rept. Prog. Phys. 81 (2018) 066201 [arXiv:1707.06277] [INSPIRE].  
[11] S. Bottaro et al., Closing the window on WIMP Dark Matter, Eur. Phys. J. C 82 (2022) 31 [arXiv:2107.09688] [INSPIRE].  
[12] J.H. Davis, The Past and Future of Light Dark Matter Direct Detection, Int. J. Mod. Phys. A 30 (2015) 1530038 [arXiv:1506.03924] [INSPIRE].  
[13] M. Drewes et al., A White Paper on keV Sterile Neutrino Dark Matter, JCAP 01 (2017) 025 [arXiv:1602.04816] [INSPIRE].  
[14] K.N. Abazajian, Sterile neutrinos in cosmology, Phys. Rept. 711-712 (2017) 1 [arXiv:1705.01837] [INSPIRE].  
[15] A. Boyarsky, M. Drewes, T. Lasserre, S. Mertens and O. Ruchayskiy, Sterile neutrino Dark Matter, Prog. Part. Nucl. Phys. 104 (2019) 1 [arXiv:1807.07938] [INSPIRE].

[16] J. Kopp, Sterile neutrinos as dark matter candidates, in Les Houches summer school on Dark Matter. 2021-07: Dark Matter, SciPost Phys. Lect. Notes 36 (2022) 1 [arXiv:2109.00767] [INSPIRE].  
[17] N. Bozorgnia et al., Simulated Milky Way analogues: implications for dark matter direct searches, JCAP 05 (2016) 024 [arXiv:1601.04707] [INSPIRE].  
[18] J.I. Collar, A.R.L. Kavner and C.M. Lewis, Germanium response to sub-keV nuclear recoils: a multipronged experimental characterization, Phys. Rev. D 103 (2021) 122003 [arXiv:2102.10089] [INSPIRE].  
[19] S. Pirro and P. Mauskopf, Advances in Bolometer Technology for Fundamental Physics, Ann. Rev. Nucl. Part. Sci. 67 (2017) 161 [INSPIRE].  
[20] CRESST collaboration, First results from the CRESST-III low-mass dark matter program, Phys. Rev. D 100 (2019) 102002 [arXiv:1904.00498] [INSPIRE].  
[21] C. Kouvaris and J. Pradler, Probing sub-GeV Dark Matter with conventional detectors, Phys. Rev. Lett. 118 (2017) 031803 [arXiv:1607.01789] [INSPIRE].  
[22] G. Grilli di Cortona, A. Messina and S. Piacentini, Migdal effect and photon Bremsstrahlung: improving the sensitivity to light dark matter of liquid argon experiments, JHEP 11 (2020) 034 [arXiv:2006.02453] [INSPIRE].  
[23] M. Ibe, W. Nakano, Y. Shoji and K. Suzuki, Migdal Effect in Dark Matter Direct Detection Experiments, JHEP 03 (2018) 194 [arXiv:1707.07258] [INSPIRE].  
[24] D. Baxter, Y. Kahn and G. Krunjaic, *Electron Ionization via Dark Matter-Electron Scattering and the Migdal Effect*, Phys. Rev. D 101 (2020) 076014 [arXiv:1908.00012] [INSPIRE].  
[25] R. Essig, J. Pradler, M. Sholapurkar and T.-T. Yu, Relation between the Migdal Effect and Dark Matter-Electron Scattering in Isolated Atoms and Semiconductors, Phys. Rev. Lett. 124 (2020) 021801 [arXiv:1908.10881] [INSPIRE].  
[26] U.K. Dey, T.N. Maity and T.S. Ray, Prospects of Migdal Effect in the Explanation of XENON1T Electron recoil Excess, Phys. Lett. B 811 (2020) 135900 [arXiv:2006.12529] [INSPIRE].  
[27] C.P. Liu, C.-P. Wu, H.-C. Chi and J.-W. Chen, Model-independent determination of the Migdal effect via photoabsorption, Phys. Rev. D 102 (2020) 121303 [arXiv:2007.10965] [INSPIRE].  
[28] K.D. Nakamura, K. Miuchi, S. Kazama, Y. Shoji, M. Ibe and W. Nakano, Detection capability of the Migdal effect for argon and xenon nuclei with position-sensitive gaseous detectors, Prog. Theor. Exp. Phys. 2021 (2021) 013C01 [arXiv:2009.05939] [INSPIRE].  
[29] S. Knapen, J. Kozaczuk and T. Lin, Migdal Effect in Semiconductors, Phys. Rev. Lett. 127 (2021) 081805 [arXiv:2011.09496] [INSPIRE].  
[30] V.V. Flambaum, L. Su, L. Wu and B. Zhu, Constraining sub-GeV dark matter from Migdal and Boosted effects, arXiv:2012.09751 [INSPIRE].  
[31] N.F. Bell, J.B. Dent, B. Dutta, S. Ghosh, J. Kumar and J.L. Newstead, Low-mass inelastic dark matter direct detection via the Migdal effect, Phys. Rev. D 104 (2021) 076013 [arXiv:2103.05890] [INSPIRE].  
[32] J.F. Acevedo, J. Bramante and A. Goodman, Accelerating composite dark matter discovery with nuclear recoils and the Migdal effect, Phys. Rev. D 105 (2022) 023012 [arXiv:2108.10889] [INSPIRE].

[33] W. Wang, K.-Y. Wu, L. Wu and B. Zhu, Direct Detection of Spin-Dependent Sub-GeV Dark Matter via Migdal Effect, arXiv:2112.06492 [INSPIRE].  
[34] V. Zacek, Search for dark matter with moderately superheated liquids, Nuovo Cim. A 107 (1994) 291 [INSPIRE].  
[35] Y. Hochberg, Y. Zhao and K.M. Zurek, Superconducting Detectors for Superlight Dark Matter, Phys. Rev. Lett. 116 (2016) 011301 [arXiv:1504.07237] [INSPIRE].  
[36] Y. Hochberg, M. Pyle, Y. Zhao and K.M. Zurek, Detecting Superlight Dark Matter with Fermi-Degenerate Materials, JHEP 08 (2016) 057 [arXiv:1512.04533] [INSPIRE].  
[37] K. Schutz and K.M. Zurek, Detectability of Light Dark Matter with Superfluid Helium, Phys. Rev. Lett. 117 (2016) 121302 [arXiv:1604.08206] [INSPIRE].  
[38] S. Knapen, T. Lin and K.M. Zurek, Light Dark Matter in Superfluid Helium: Detection with Multi-excitation Production, Phys. Rev. D 95 (2017) 056019 [arXiv:1611.06228] [INSPIRE].  
[39] S. Derenzo, R. Essig, A. Massari, A. Soto and T.-T. Yu, Direct Detection of sub-GeV Dark Matter with Scintillating Targets, Phys. Rev. D 96 (2017) 016026 [arXiv:1607.01009] [INSPIRE].  
[40] P.C. Bunting, G. Gratta, T. Melia and S. Rajendran, Magnetic Bubble Chambers and Sub-GeV Dark Matter Direct Detection, Phys. Rev. D 95 (2017) 095001 [arXiv:1701.06566] [INSPIRE].  
[41] Y. Hochberg et al., Detection of sub-MeV Dark Matter with Three-Dimensional Dirac Materials, Phys. Rev. D 97 (2018) 015004 [arXiv:1708.08929] [INSPIRE].  
[42] N.A. Kurinsky, T.C. Yu, Y. Hochberg and B. Cabrera, *Diamond Detectors for Direct Detection of Sub-GeV Dark Matter*, Phys. Rev. D 99 (2019) 123005 [arXiv:1901.07569] [INSPIRE].  
[43] Y. Hochberg, I. Charaev, S.-W. Nam, V. Verma, M. Colangelo and K.K. Berggren, Detecting Sub-GeV Dark Matter with Superconducting Nanowires, Phys. Rev. Lett. 123 (2019) 151802 [arXiv:1903.05101] [INSPIRE].  
[44] G. Cavoto, E.N.M. Cirillo, F. Cocina, J. Ferretti and A.D. Polosa, WIMP detection and slow ion dynamics in carbon nanotube arrays, Eur. Phys. J. C 76 (2016) 349 [arXiv:1602.03216] [INSPIRE].  
[45] G. Cavoto, F. Luchetta and A.D. Polosa, Sub-GeV Dark Matter Detection with Electron Recoils in Carbon Nanotubes, Phys. Lett. B 776 (2018) 338 [arXiv:1706.02487] [INSPIRE].  
[46] T. Trickle, Z. Zhang and K.M. Zurek, Detecting Light Dark Matter with Magnons, Phys. Rev. Lett. 124 (2020) 201801 [arXiv:1905.13744] [INSPIRE].  
[47] S. Chigusa, T. Moroi and K. Nakayama, Detecting light boson dark matter through conversion into a magnon, Phys. Rev. D 101 (2020) 096013 [arXiv:2001.10666] [INSPIRE].  
[48] S.-Y. Wang, Graphene-based detectors for directional dark matter detection, Eur. Phys. J. C 79 (2019) 561 [arXiv:1509.08801] [INSPIRE].  
[49] D. Kim, J.-C. Park, K.C. Fong and G.-H. Lee, Detecting keV-Range Super-Light Dark Matter Using Graphene Josephson Junction, arXiv:2002.07821 [INSPIRE].  
[50] N. Kurinsky, D. Baxter, Y. Kahn and G. Krunjaic, Dark matter interpretation of excesses in multiple direct detection experiments, Phys. Rev. D 102 (2020) 015017 [arXiv:2002.06937] [INSPIRE].

[51] R. Essig, M. Fernandez-Serra, J. Mardon, A. Soto, T. Volansky and T.-T. Yu, Direct Detection of sub-GeV Dark Matter with Semiconductor Targets, JHEP 05 (2016) 046 [arXiv:1509.01598] [INSPIRE].  
[52] E. Andersson, A. Bökmark, R. Catena, T. Emken, H.K. Moberg and E. Åstrand, Projected sensitivity to sub-GeV dark matter of next-generation semiconductor detectors, JCAP 05 (2020) 036 [arXiv:2001.08910] [INSPIRE].  
[53] P. Du, D. Egana-Ugrinovic, R. Essig and M. Sholapurkar, Sources of Low-Energy Events in Low-Threshold Dark-Matter and Neutrino Detectors, Phys. Rev. X 12 (2022) 011009 [arXiv:2011.13939] [INSPIRE].  
[54] C.A.J. O'Hare et al., Particle detection and tracking with DNA, Eur. Phys. J. C 82 (2022) 306 [arXiv:2105.11949] [INSPIRE].  
[55] C.V. Cappiello, K.C.Y. Ng and J.F. Beacom, Reverse Direct Detection: Cosmic Ray Scattering With Light Dark Matter, Phys. Rev. D 99 (2019) 063004 [arXiv:1810.07705] [INSPIRE].  
[56] T. Bringmann and M. Pospelov, Novel direct detection constraints on light dark matter, Phys. Rev. Lett. 122 (2019) 171801 [arXiv:1810.10543] [INSPIRE].  
[57] Y. Ema, F. Sala and R. Sato, Light Dark Matter at Neutrino Experiments, Phys. Rev. Lett. 122 (2019) 181802 [arXiv:1811.00520] [INSPIRE].  
[58] J.B. Dent, B. Dutta, J.L. Newstead and I.M. Shoemaker, Bounds on Cosmic Ray-Boosted Dark Matter in Simplified Models and its Corresponding Neutrino-Floor, Phys. Rev. D 101 (2020) 116007 [arXiv:1907.03782] [INSPIRE].  
[59] W. Wang, L. Wu, J.M. Yang, H. Zhou and B. Zhu, *Cosmic ray boosted sub-GeV gravitationally interacting dark matter in direct detection*, JHEP **12** (2020) 072 [Erratum JHEP **02** (2021) 052] [arXiv:1912.09904] [INSPIRE].  
[60] S.-F. Ge, J. Liu, Q. Yuan and N. Zhou, Diurnal Effect of Sub-GeV Dark Matter Boosted by Cosmic Rays, Phys. Rev. Lett. 126 (2021) 091804 [arXiv:2005.09480] [INSPIRE].  
[61] Q.-H. Cao, R. Ding and Q.-F. Xiang, Searching for sub-MeV boosted dark matter from xenon electron direct detection, Chin. Phys. C 45 (2021) 045002 [arXiv:2006.12767] [INSPIRE].  
[62] W. Cho, K.-Y. Choi and S.M. Yoo, Searching for boosted dark matter mediated by a new gauge boson, Phys. Rev. D 102 (2020) 095010 [arXiv:2007.04555] [INSPIRE].  
[63] Z.-H. Lei, J. Tang and B.-L. Zhang, Constraints on cosmic-ray boosted DM in CDEX-10, arXiv:2008.07116 [INSPIRE].  
[64] C. Xia, Y.-H. Xu and Y.-F. Zhou, Constraining light dark matter upscattered by ultrahigh-energy cosmic rays, Nucl. Phys. B 969 (2021) 115470 [arXiv:2009.00353] [INSPIRE].  
[65] J.B. Dent, B. Dutta, J.L. Newstead, I.M. Shoemaker and N.T. Arellano, Present and future status of light dark matter models from cosmic-ray electron upscattering, Phys. Rev. D 103 (2021) 095015 [arXiv:2010.09749] [INSPIRE].  
[66] N.F. Bell et al., Cosmic-ray upscattered inelastic dark matter, Phys. Rev. D 104 (2021) 076020 [arXiv:2108.00583] [INSPIRE].  
[67] J.-C. Feng, X.-W. Kang, C.-T. Lu, Y.-L.S. Tsai and F.-S. Zhang, Revising inelastic dark matter direct detection by including the cosmic ray acceleration, JHEP 04 (2022) 080 [arXiv:2110.08863] [INSPIRE].

[68] Y. Chen et al., Earth Shielding and Daily Modulation from Electrophilic Boosted Dark Matter, arXiv:2110.09685 [INSPIRE].  
[69] W. Wang, W.N. Yang and B. Zhu, The Spin-dependent Scattering of Boosted Dark Matter, arXiv:2111.04000.  
[70] C. Xia, Y.-H. Xu and Y.-F. Zhou, Production and attenuation of cosmic-ray boosted dark matter, JCAP 02 (2022) 028 [arXiv:2111.05559] [INSPIRE].  
[71] PANDAX-II collaboration, Search for Cosmic-Ray Boosted Sub-GeV Dark Matter at the PandaX-II Experiment, Phys. Rev. Lett. 128 (2022) 171801 [arXiv:2112.08957] [INSPIRE].  
[72] CDEX collaboration, Constraints on sub-GeV Dark Matter Boosted by Cosmic Rays from CDEX-10 Experiment at the China Jinping Underground Laboratory, arXiv:2201.01704 [INSPIRE].  
[73] C.V. Cappiello and J.F. Beacom, *Strong New Limits on Light Dark Matter from Neutrino Experiments*, Phys. Rev. D **100** (2019) 103011 [Erratum ibid. **104** (2021) 069901] [arXiv:1906.11283] [INSPIRE].  
[74] G. Guo, Y.-L.S. Tsai and M.-R. Wu, Probing cosmic-ray accelerated light dark matter with IceCube, JCAP 10 (2020) 049 [arXiv:2004.03161] [INSPIRE].  
[75] Y. Ema, F. Sala and R. Sato, Neutrino experiments probe hadrophilic light dark matter, SciPost Phys. 10 (2021) 072 [arXiv:2011.01939] [INSPIRE].  
[76] PROSPECT collaboration, Limits on sub-GeV dark matter from the PROSPECT reactor antineutrino experiment, Phys. Rev. D 104 (2021) 012009 [arXiv:2104.11219] [INSPIRE].  
[77] B. Chauhan, B. Dasgupta and A. Dighe, Large Energy Singles at JUNO from Atmospheric Neutrinos and Dark Matter, arXiv:2111.14586 [INSPIRE].  
[78] G. Guo, Y.-L.S. Tsai, M.-R. Wu and Q. Yuan, Elastic and Inelastic Scattering of Cosmic-Rays on Sub-GeV Dark Matter, Phys. Rev. D 102 (2020) 103004 [arXiv:2008.12137] [INSPIRE].  
[79] W. Yin, Highly-boosted dark matter and cutoff for cosmic-ray neutrinos through neutrino portal, EPJ Web Conf. 208 (2019) 04003 [arXiv:1809.08610] [INSPIRE].  
[80] S. Pandey, S. Karmakar and S. Rakshit, Interactions of astrophysical neutrinos with dark matter: a model building perspective, JHEP 01 (2019) 095 [Erratum JHEP 11 (2021) 215] [arXiv:1810.04203] [INSPIRE].  
[81] Y. Zhang, Speeding up dark matter with solar neutrinos, Prog. Theor. Exp. Phys. 2022 (2022) 013B05 [arXiv:2001.00948] [INSPIRE].  
[82] Y. Jho, J.-C. Park, S.C. Park and P.-Y. Tseng, *Cosmic-Neutrino-Boosted Dark Matter (νBDM)*, arXiv:2101.11262 [INSPIRE].  
[83] A. Das and M. Sen, Boosted dark matter from diffuse supernova neutrinos, Phys. Rev. D 104 (2021) 075029 [arXiv:2104.00027] [INSPIRE].  
[84] W. Chao, T. Li and J. Liao, Connecting Primordial Black Hole to boosted sub-GeV Dark Matter through neutrino, arXiv:2108.05608 [INSPIRE].  
[85] D. Ghosh, A. Guha and D. Sachdeva, *Exclusion limits on Dark Matter-Neutrino Scattering Cross-section*, arXiv:2110.00025 [INSPIRE].  
[86] J.-W. Wang, A. Granelli and P. Ullio, Direct Detection Constraints on Blazar-Boosted Dark Matter, arXiv:2111.13644 [INSPIRE].

[87] J. Alvey, M. Campos, M. Fairbairn and T. You, Detecting Light Dark Matter via Inelastic Cosmic Ray Collisions, Phys. Rev. Lett. 123 (2019) 261802 [arXiv:1905.05776] [INSPIRE].  
[88] R. Plestid, V. Takhistov, Y.-D. Tsai, T. Bringmann, A. Kusenko and M. Pospelov, New Constraints on Millicharged Particles from Cosmic-ray Production, Phys. Rev. D 102 (2020) 115032 [arXiv:2002.11732] [INSPIRE].  
[89] M. Kachelriess and J. Tjemsland, Meson production in air showers and the search for light exotic particles, Astrophys. 132 (2021) 102622 [arXiv:2104.06811] [INSPIRE].  
[90] C. Kouvaris, Probing Light Dark Matter via Evaporation from the Sun, Phys. Rev. D 92 (2015) 075001 [arXiv:1506.04316] [INSPIRE].  
[91] H. An, M. Pospelov, J. Pradler and A. Ritz, Directly Detecting MeV-scale Dark Matter via Solar Reflection, Phys. Rev. Lett. 120 (2018) 141801 [Erratum ibid. 121 (2018) 259903] [arXiv:1708.03642] [INSPIRE].  
[92] T. Emken, C. Kouvaris and N.G. Nielsen, The Sun as a sub-GeV Dark Matter Accelerator, Phys. Rev. D 97 (2018) 063007 [arXiv:1709.06573] [INSPIRE].  
[93] Y. Chen, M.-Y. Cui, J. Shu, X. Xue, G.-W. Yuan and Q. Yuan, Sun heated MeV-scale dark matter and the XENON1T electron recoil excess, JHEP 04 (2021) 282 [arXiv:2006.12447] [INSPIRE].  
[94] T. Emken, Solar reflection of light dark matter with heavy mediators, Phys. Rev. D 105 (2022) 063020 [arXiv:2102.12483] [INSPIRE].  
[95] H. An, H. Nie, M. Pospelov, J. Pradler and A. Ritz, Solar reflection of dark matter, Phys. Rev. D 104 (2021) 103026 [arXiv:2108.10332] [INSPIRE].  
[96] K. Agashe, Y. Cui, L. Necib and J. Thaler, (In)direct Detection of Boosted Dark Matter, JCAP 10 (2014) 062 [arXiv:1405.7370] [INSPIRE].  
[97] J. Berger, Y. Cui and Y. Zhao, Detecting Boosted Dark Matter from the Sun with Large Volume Neutrino Detectors, JCAP 02 (2015) 005 [arXiv:1410.2246] [INSPIRE].  
[98] J.F. Cherry, M.T. Frandsen and I.M. Shoemaker, Direct Detection Phenomenology in Models Where the Products of Dark Matter Annihilation Interact with Nuclei, Phys. Rev. Lett. 114 (2015) 231303 [arXiv:1501.03166] [INSPIRE].  
[99] X. Chen and L. Yang, Search for boosted dark matter with high-Z material in underground experiments, arXiv:2002.04995 [INSPIRE].  
[100] B. Fornal, P. Sandick, J. Shu, M. Su and Y. Zhao, Boosted Dark Matter Interpretation of the XENON1T Excess, Phys. Rev. Lett. 125 (2020) 161804 [arXiv:2006.11264] [INSPIRE].  
[101] M. Pospelov, A. Ritz and M.B. Voloshin, Bosonic super-WIMPs as keV-scale dark matter, Phys. Rev. D 78 (2008) 115012 [arXiv:0807.3279] [INSPIRE].  
[102] H. An, M. Pospelov, J. Pradler and A. Ritz, Direct Detection Constraints on Dark Photon Dark Matter, Phys. Lett. B 747 (2015) 331 [arXiv:1412.8378] [INSPIRE].  
[103] Y. Hochberg, T. Lin and K.M. Zurek, Detecting Ultralight Bosonic Dark Matter via Absorption in Superconductors, Phys. Rev. D 94 (2016) 015019 [arXiv:1604.06800] [INSPIRE].  
[104] Y. Hochberg, T. Lin and K.M. Zurek, Absorption of light dark matter in semiconductors, Phys. Rev. D 95 (2017) 023013 [arXiv:1608.01994] [INSPIRE].  
[105] I.M. Bloch, R. Essig, K. Tobioka, T. Volansky and T.-T. Yu, Searching for Dark Absorption with Direct Detection Experiments, JHEP 06 (2017) 087 [arXiv:1608.02123] [INSPIRE].

[106] D. Green and S. Rajendran, The Cosmology of Sub-MeV Dark Matter, JHEP 10 (2017) 013 [arXiv:1701.08750] [INSPIRE].  
[107] A. Arvanitaki, S. Dimopoulos and K. Van Tilburg, Resonant absorption of bosonic dark matter in molecules, Phys. Rev. X 8 (2018) 041001 [arXiv:1709.05354] [INSPIRE].  
[108] B. von Krosigk et al., Effect on dark matter exclusion limits from new silicon photoelectric absorption measurements, Phys. Rev. D 104 (2021) 063002 [arXiv:2010.15874] [INSPIRE].  
[109] A. Mitridate, T. Trickle, Z. Zhang and K.M. Zurek, Dark matter absorption via electronic excitations, JHEP 09 (2021) 123 [arXiv:2106.12586] [INSPIRE].  
[110] Y. Hochberg, B. von Krosigk, E. Kuflik and T.C. Yu, Impact of Dark Compton Scattering on Direct Dark Matter Absorption Searches, Phys. Rev. Lett. 128 (2022) 191801 [arXiv:2109.08168] [INSPIRE].  
[111] J.A. Dror, G. Elor and R. Mcgehee, Directly Detecting Signals from Absorption of Fermionic Dark Matter, Phys. Rev. Lett. 124 (2020) 18 [arXiv:1905.12635] [INSPIRE].  
[112] J.A. Dror, G. Elor and R. Mcgehee, Absorption of Fermionic Dark Matter by Nuclear Targets, JHEP 02 (2020) 134 [arXiv:1908.10861] [INSPIRE].  
[113] J.A. Dror, G. Elor, R. McGehee and T.-T. Yu, Absorption of sub-MeV fermionic dark matter by electron targets, Phys. Rev. D 103 (2021) 035001 [arXiv:2011.01940] [INSPIRE].  
[114] XENON collaboration, Excess electronic recoil events in XENON1T, Phys. Rev. D 102 (2020) 072004 [arXiv:2006.09721] [INSPIRE].  
[115] PANDAX-II collaboration, Dark Matter Results from First 98.7 Days of Data from the PandaX-II Experiment, Phys. Rev. Lett. 117 (2016) 121303 [arXiv:1607.07400] [INSPIRE].  
[116] PANDAX-II collaboration, Search for Light Dark Matter-Electron Scatterings in the PandaX-II Experiment, Phys. Rev. Lett. 126 (2021) 211803 [arXiv:2101.07479] [INSPIRE].  
[117] J.F. Nieves and P.B. Pal, Generalized Fierz identities, Am. J. Phys. 72 (2004) 1100 [hep-ph/0306087] [INSPIRE].  
[118] C.C. Nishi, Simple derivation of general Fierz-like identities, Am. J. Phys. 73 (2005) 1160 [hep-ph/0412245] [INSPIRE].  
[119] Y. Liao and J.-Y. Liu, Generalized Fierz Identities and Applications to Spin-3/2 Particles, Eur. Phys. J. Plus 127 (2012) 121 [arXiv:1206.5141] [INSPIRE].  
[120] S.-F. Ge, P. Pasquini and J. Sheng, Solar active-sterile neutrino conversion with atomic effects at dark matter direct detection experiments, JHEP 05 (2022) 088 [arXiv:2112.05560] [INSPIRE].  
[121] R. Catena, T. Emken, N.A. Spaldin and W. Tarantino, Atomic responses to general dark matter-electron interactions, Phys. Rev. Res. 2 (2020) 033195 [arXiv:1912.08204] [INSPIRE].  
[122] PANDAX-II collaboration, A Search for Solar Axions and Anomalous Neutrino Magnetic Moment with the Complete PandaX-II Data, Chin. Phys. Lett. 38 (2021) 011301 [Erratum ibid. 38 (2021) 109902] [arXiv:2008.06485] [INSPIRE].  
[123] S.-F. Ge, K. Hagiwara, N. Okamura and Y. Takaesu, Determination of mass hierarchy with medium baseline reactor neutrino experiments, JHEP 05 (2013) 131 [arXiv:1210.8141] [INSPIRE].  
[124] S.-F. Ge, H.-J. He and R.-Q. Xiao, Probing new physics scales from Higgs and electroweak observables at  $e^{+}$ $e^{-}$  Higgs factory, JHEP 10 (2016) 007 [arXiv:1603.03385] [INSPIRE].

[125] E.W. Kolb and M.S. Turner, The Early Universe, in Frontiers of Physics 69, CRC Press, Boca Raton, FL, U.S.A. (1990) [INSPIRE].  
[126] N. Bernal, M. Heikinheimo, T. Tenkanen, K. Tuominen and V. Vaskonen, The Dawn of FIMP Dark Matter: A Review of Models and Constraints, Int. J. Mod. Phys. A 32 (2017) 1730023 [arXiv:1706.07442] [INSPIRE].  
[127] T. Asaka, K. Ishiwata and T. Moroi, Right-handed sneutrino as cold dark matter, Phys. Rev. D 73 (2006) 051301 [hep-ph/0512118] [INSPIRE].  
[128] S. Gopalakrishna, A. de Gouvêa and W. Porod, Right-handed sneutrinos as nonthermal dark matter, JCAP 05 (2006) 005 [hep-ph/0602027] [INSPIRE].  
[129] T. Asaka, K. Ishiwata and T. Moroi, Right-handed sneutrino as cold dark matter of the universe, Phys. Rev. D 75 (2007) 065001 [hep-ph/0612211] [INSPIRE].  
[130] V. Page, Non-thermal right-handed sneutrino dark matter and the  $\Omega_{\mathrm{DM}} / \Omega_b$  problem, JHEP 04 (2007) 021 [hep-ph/0701266] [INSPIRE].  
[131] L.J. Hall, K. Jedamzik, J. March-Russell and S.M. West, Freeze-In Production of FIMP Dark Matter, JHEP 03 (2010) 080 [arXiv:0911.1120] [INSPIRE].  
[132] PLANCK collaboration, Planck 2018 results. Part VI. Cosmological parameters, Astron. Astrophys. 641 (2020) A6 [Erratum ibid. 652 (2021) C4] [arXiv:1807.06209] [INSPIRE].  
[133] P. Gondolo and G. Gelmini, *Cosmic abundances of stable particles: Improved analysis*, Nucl. Phys. B **360** (1991) 145 [INSPIRE].  
[134] L. Husdal, On Effective Degrees of Freedom in the Early Universe, Galaxies 4 (2016) 78 [arXiv:1609.04979] [INSPIRE].  
[135] K. Saikawa and S. Shirai, Primordial gravitational waves, precisely: The role of thermodynamics in the Standard Model, JCAP 05 (2018) 035 [arXiv:1803.01038] [INSPIRE].  
[136] K. Saikawa and S. Shirai, Precise WIMP Dark Matter Abundance and Standard Model Thermodynamics, JCAP 08 (2020) 011 [arXiv:2005.03544] [INSPIRE].  
[137] B.V. Lehmann and S. Profumo, Cosmology and prospects for sub-MeV dark matter in electron recoil experiments, Phys. Rev. D 102 (2020) 023038 [arXiv:2002.07809] [INSPIRE].  
[138] H.H. Patel, Package-X: A Mathematica package for the analytic calculation of one-loop integrals, Comput. Phys. Commun. 197 (2015) 276 [arXiv:1503.01469] [INSPIRE].  
[139] A. Denner, S. Dittmaier and L. Hofer, Collier: a Fortran-based Complex One-Loop Library in Extended Regularizations, Comput. Phys. Commun. 212 (2017) 220 [arXiv:1604.06792] [INSPIRE].  
[140] Y. Gong and X. Chen, Cosmological Constraints on Invisible Decay of Dark Matter, Phys. Rev. D 77 (2008) 103511 [arXiv:0802.2296] [INSPIRE].  
[141] S. De Lope Amigo, W.M.-Y. Cheung, Z. Huang and S.-P. Ng, Cosmological Constraints on Decaying Dark Matter, JCAP 06 (2009) 005 [arXiv:0812.4016] [INSPIRE].  
[142] B. Audren, J. Lesgourgues, G. Mangano, P.D. Serpico and T. Tram, *Strongest model-independent bound on the lifetime of Dark Matter*, JCAP **12** (2014) 028 [arXiv:1407.2418] [INSPIRE].  
[143] V. Poulin, P.D. Serpico and J. Lesgourgues, A fresh look at linear cosmological constraints on a decaying dark matter component, JCAP 08 (2016) 036 [arXiv:1606.02073] [INSPIRE].

[144] G.F. Abellán, R. Murgia and V. Poulin, Linear cosmological constraints on two-body decaying dark matter scenarios and the  $S_{8}$  tension, Phys. Rev. D 104 (2021) 123533 [arXiv:2102.12498] [INSPIRE].  
[145] J.F. Navarro, C.S. Frenk and S.D.M. White, The Structure of cold dark matter halos, Astrophys. J. 462 (1996) 563 [astro-ph/9508025] [INSPIRE].  
[146] J.F. Navarro, C.S. Frenk and S.D.M. White, A Universal density profile from hierarchical clustering, Astrophys. J. 490 (1997) 493 [astro-ph/9611107] [INSPIRE].  
[147] R. Laha, J.B. Muñoz and T.R. Slatyer, INTEGRAL constraints on primordial black holes and particle dark matter, Phys. Rev. D 101 (2020) 123514 [arXiv:2004.00627] [INSPIRE].  
[148] R. Essig, E. Kuflik, S.D. McDermott, T. Volansky and K.M. Zurek, Constraining Light Dark Matter with Diffuse X-Ray and Gamma-Ray Observations, JHEP 11 (2013) 193 [arXiv:1309.4091] [INSPIRE].  
[149] J.-Y. Liao et al., Background model for the Low-Energy Telescope of Insight-HXMT, J. High Energy Astrophys. 27 (2020) 24 [arXiv:2004.01432] [INSPIRE].  
[150] R. Krivonos et al., NuSTAR measurement of the cosmic X-ray background in the 3-20 keV energy band, Mon. Not. Roy. Astron. Soc. 502 (2021) 3966 [arXiv:2011.11469] [INSPIRE].  
[151] K.C.Y. Ng et al., New Constraints on Sterile Neutrino Dark Matter from NuSTAR M31 Observations, Phys. Rev. D 99 (2019) 083005 [arXiv:1901.01262] [INSPIRE].  
[152] D.E. Gruber, J.L. Matteson, L.E. Peterson and G.V. Jung, The spectrum of diffuse cosmic hard X-rays measured with HEAO-1, Astrophys. J. 520 (1999) 124 [astro-ph/9903492] [INSPIRE].  
[153] L. Bouchet et al., INTEGRAL SPI All-Sky View in Soft Gamma Rays: Study of Point Source and Galactic Diffuse Emissions, Astrophys. J. 679 (2008) 1315 [arXiv:0801.2086] [INSPIRE].  
[154] L. Bouchet, A.W. Strong, T.A. Porter, I.V. Moskalenko, E. Jourdain and J.-P. Roques, Diffuse emission measurement with INTEGRAL/SPI as indirect probe of cosmic-ray electrons and positrons, Astrophys. J. 739 (2011) 29 [arXiv:1107.0200] [INSPIRE].  
[155] The Hard X-ray Modulation Telescope (Insight-HXMT) website, (2022) http://hxfmten.ihep.ac.cn/mission.jhtml.  
[156] PANDAX collaboration, Dark matter direct search sensitivity of the PandaX-4T experiment, Sci. China Phys. Mech. Astron. 62 (2019) 31011 [arXiv:1806.02229] [INSPIRE].  
[157] PANDAX-4T collaboration, Dark Matter Search Results from the PandaX-4T Commissioning Run, Phys. Rev. Lett. 127 (2021) 261802 [arXiv:2107.13438] [INSPIRE].  
[158] XENON collaboration, Projected WIMP sensitivity of the XENONnT dark matter experiment, JCAP 11 (2020) 031 [arXiv:2007.08796] [INSPIRE].  
[159] LZ collaboration, LUX-ZEPLIN (LZ) Conceptual Design Report, arXiv:1509.02910 [INSPIRE].  
[160] B.J. Mount et al., LUX-ZEPLIN (LZ) Technical Design Report, arXiv:1703.09144 [INSPIRE].