PAPER

# Distinct photon-ALP propagation modes

To cite this article: Qing-Hong Cao et al JCAP01(2025)099

View the article online for updates and enhancements.

# You may also like

- Production of the axion-like particles on electron-nucleus and ultraperipheral heavy ion collisions  
C P Oliveira, D Hadjimichef and M V T Machado  
- Constraints on axion-like particles with different magnetic field models from the PKS 2155-304 energy spectrum  
Jia Bu and Ya-Ping Li  
- Physics Beyond the Standard Model with Future X-Ray Observatories: Projected Constraints on Very-light Axion-like Particles with Athena and AXIS  
Julia Sisk-Reynes, Christopher S. Reynolds, Michael L. Parker et al.

# Distinct photon-ALP propagation modes

Qing-Hong Cao  $^{a,b}$  Zuowei Liu  $^{c}$  and Jun-Chen Wang  $^{a}$

$^{a}$ School of Physics, Peking University, Beijing 100871, China  
$^{b}$ Center for High Energy Physics, Peking University, Beijing 100871, China  
$^{c}$ Department of Physics, Nanjing University, Nanjing 210093, China

E-mail: qinghongcao@pku.edu.cn, zuoweliu@nju.edu.cn, junchenwang@stu.pku.edu.cn

ABSTRACT: Measurement of cosmic photons may reveal their propagation in the interstellar environment, thereby offering a promising way to probe axions and axion-like particles (ALPs). Numerical methods are usually used to compute the propagation of the photon-ALP beam due to the complexity of both the interstellar magnetic field and the evolution equation. However, under certain conditions, the evolution equation can be greatly simplified so that the photon-ALP propagation can be analytically solved. By using analytic methods, we find two distinct photon-ALP propagation modes, determined by the relative magnitude of the photon-ALP mixing term in comparison to the photon attenuation term. In one mode, the intensity of photons decreases with the increasing distance; in the other mode, it also exhibits oscillatory behavior. To distinguish the two propagation modes, we compute the observable quantities such as the photon survival probability and the degree of polarization. We also determine through analytic methods the conditions under which maximum polarization can be observed and the corresponding upper bound of the survival probability.

KEYWORDS: axions, ultra high energy cosmic rays

ARXIV EPRINT: 2307.15602

# Contents

1 Introduction 1  
2 Propagation equation 2  
3 Two different propagation modes 4

3.1 The  $D > 0$  propagation mode 5  
3.2 The  $D <   0$  propagation mode 6

4 Propagation modes for high-energy photons with  $\omega \geq 100$  GeV

4.1 Photons from M31 7  
4.2 The  $D > 0$  case 9  
4.3 The  $D <   0$  case 11

5 Propagation modes for photons with energy  $\omega = 10^{-3} - 10^{2}$  GeV 13  
6 Conclusions 15

A Comparison between analytic and numerical calculations 16

A.1 MW galaxy 16  
A.2 Galaxy clusters 17

# 1 Introduction

The existence of axions and axion-like particles (ALPs) is a topic of great interest in modern particle physics [1-3]. The QCD axion was initially proposed as a natural solution to the strong CP problem [4, 5]. Recently, the study of ALPs has gained widespread attention due to the much wider range of mass and coupling parameters than the QCD axion [6]. ALPs arise naturally in a plethora of extensions of the standard model, including supersymmetric models [7, 8] and superstring theories [9-11].

The presence of ALPs can significantly alter photon propagation in the universe, leading to distinct photon-ALP oscillation signatures [12, 13]. Because of the complex astrophysical environment through which photon-ALP beams propagate, most recent studies used numerical simulations to analyze their propagation properties; see e.g., [14-21]. Nevertheless, there are also a number of analytical studies on the photon-ALP propagation, see e.g., [13, 22-30]. Although numerical simulations lead to more accurate results than analytical calculations, some physical phenomena that can be discerned in analytical calculations are often obscure in numerical simulations. In this paper we use analytic methods to study the propagation of the photon-ALP beams. We find that under certain conditions the evolution equation of the photon-ALP beam can be significantly simplified so that analytic methods can be used. Our analytic methods reveal two distinct photon propagation modes, determined by the relative magnitude of the photon-ALP mixing term in comparison to the photon

attenuation term. More precisely, the two propagation modes are determined by the sign of the quantity  $D$  given in eq. (3.2): in the  $D > 0$  case, photons exhibit clear oscillations during the propagation; conversely, in the  $D < 0$  case, the oscillations are absent. We investigate the astrophysical conditions that lead to the emergence of these two propagation modes, and further study the implications for relevant physical observables such as the photon survival probability and degree of polarization. We study the distinguishing features of the two propagation modes in detail, which can be used to discriminate between the two modes, as well as against the standard model background.

The rest of paper is organized as follows. In section 2, we introduce the ALPs and the propagation equation governing the photon-ALP system. In section 3, we introduce the two distinct photon propagation modes that are characterized by the sign of a quantity  $D$ . We compute the density matrix via analytic methods and further discuss the effects of ALPs on the density matrix. In sections 4 and 5, we discuss the physical observables such as the photon survival probability and the photon degree of polarization in the two propagation modes: We focus on photons with energies above  $100\mathrm{GeV}$  in section 4, and photons with energies in the range of  $10^{-3} - 10^{2}\mathrm{GeV}$  in section 5. In section 6, we summarize our findings. In the appendix, we compare our analytic method in which a uniform magnetic field is assumed, with numerical calculations in which magnetic field models that aim to describe the astrophysical conditions are used.

# 2 Propagation equation

Consider the following effective interaction Lagrangian between the axion-like particle (ALP)  $a$  and the photon

$$
\mathcal {L} _ {\mathrm {i n t}} = - \frac {1}{4} g _ {a \gamma} F ^ {\mu \nu} \tilde {F} _ {\mu \nu} a = g _ {a \gamma} \mathbf {E} \cdot \mathbf {B} a, (2. 1)
$$

where  $F^{\mu \nu}$  is the electromagnetic stress tensor and  $\tilde{F}_{\mu \nu}$  is the dual,  $\mathbf{E}$  and  $\mathbf{B}$  are the electric and magnetic fields, respectively, and  $g_{a\gamma}$  is the coupling constant.

The propagation of the photon-ALP beam along the  $z$ -direction with energy  $\omega$  can be described by a three-component vector  $\psi = (A_x, A_y, a)^T$ , where  $A_x$  and  $A_y$  are the electromagnetic potentials linearly polarized along the  $x$  and  $y$  axes, respectively. Without loss of generality, we consider the case where the external magnetic field is along the  $y$  direction and the equation that governs the propagation of  $\psi$  is given by [13, 31, 32],

$$
\left(i \frac {d}{d z} + \omega + \mathcal {M}\right) \psi = 0, \tag {2.2}
$$

where  $\mathcal{M}$  is given by

$$
\mathcal {M} = \left( \begin{array}{c c c} \Delta_ {x} & 0 & 0 \\ 0 & \Delta_ {y} & \Delta_ {a \gamma} \\ 0 & \Delta_ {a \gamma} & \Delta_ {a a} \end{array} \right) + \frac {1}{2} \left( \begin{array}{c c c} i \Gamma & 0 & 0 \\ 0 & i \Gamma & 0 \\ 0 & 0 & 0 \end{array} \right). \tag {2.3}
$$

Here,  $\Delta_x$  and  $\Delta_y$  describe the medium effects,  $\Gamma$  is the absorption rate accounting for the attenuation of photons,  $\Delta_{a\gamma} = g_{a\gamma}B / 2$  is the photon-ALP mixing term with  $B = |\pmb {B}|$ , and

$\Delta_{aa} = -m_a^2 /(2\omega)$  with  $m_{a}$  being the ALP mass. The absorption rate  $\Gamma$  is mainly caused by the reaction  $\gamma \gamma \rightarrow e^{+}e^{-}$  between the propagating photons and ambient photons, such as cosmic microwave background, extragalactic background light, and so on [33, 34]. As shown in the black line of figure 1,  $\Gamma$  becomes significant as energy  $\omega \gtrsim 10^{5}\mathrm{GeV}$ .

The medium effects are given by

$$
\Delta_ {x, y} = N \Delta_ {\mathrm {Q E D}} + \Delta_ {\mathrm {p l}} + \Delta_ {\mathrm {d i s}}, \tag {2.4}
$$

where  $N = 2$  (7/2) for  $\Delta_x$  ( $\Delta_y$ ),  $\Delta_{\mathrm{QED}}$  represents the QED birefringence,  $\Delta_{\mathrm{pl}}$  represents the plasma effect, and  $\Delta_{\mathrm{dis}}$  accounts for dispersion effects from photon-photon scattering on environmental radiation field [17, 18]. The plasma effect  $\Delta_{\mathrm{pl}}$  is given by

$$
\Delta_ {\mathrm {p l}} = - \frac {\omega_ {\mathrm {p l}} ^ {2}}{2 \omega} = - \frac {e ^ {2} n _ {e}}{2 m _ {e} \omega}, (2. 5)
$$

where  $\omega_{\mathrm{pl}}$  is the plasma frequency,  $e$  is the QED coupling, and  $m_e$  and  $n_e$  is the mass and number density of the electron, respectively. For the case of  $\omega \lesssim 10^5$  GeV, the QED birefringence and dispersion effects can be obtained from the Euler-Heisenberg Lagrangian [35-39]

$$
\Delta_ {\mathrm {Q E D}} = \frac {\alpha \omega}{4 5 \pi} \left(\frac {B e}{m _ {e} ^ {2}}\right) ^ {2}, (2. 6)
$$

$$
\Delta_ {\mathrm {d i s}} = \frac {4 4 \alpha^ {2} \rho_ {\mathrm {R F}} \omega}{1 3 5 m _ {e} ^ {4}}, \tag {2.7}
$$

where  $\alpha$  is the fine structure constant, and  $\rho_{\mathrm{RF}}$  is the ambient photon energy density. For the high energy cosmic gamma-ray with  $\omega \gtrsim \omega_2 = 10^5\mathrm{GeV}$ , Euler-Heisenberg approximation breaks down, and one can use the scaling function  $g_{2}(\omega /\omega_{2})$  to take into account the gamma-gamma scattering due to background photon [40]. Thus, at photon energy  $\omega \gtrsim \omega_{2} = 10^{5}\mathrm{GeV}$ , the quantities  $\Delta_{\mathrm{QED}}$  and  $\Delta_{\mathrm{dis}}$  are both modified to  $\Delta_{\mathrm{QED(dis)}}g_2(\omega /\omega_2)$ , as follows [40]:

$$
g _ {2} (u) = \frac {1 5}{\pi^ {4}} \int_ {0} ^ {\infty} d x \frac {x ^ {3}}{e ^ {x} - 1} g _ {1} \left(u x \frac {3 0 \zeta (3)}{\pi^ {4}}\right),
$$

$$
g _ {1} (u) = \frac {3}{8} \int_ {- 1} ^ {+ 1} d \mu (1 - \mu) ^ {2} g _ {0} \left(u \frac {1 - \mu}{2}\right), \tag {2.8}
$$

$$
g _ {0} (u) = \frac {4 5}{4 4} \int_ {1} ^ {\infty} d u ^ {\prime} \frac {f (u ^ {\prime})}{u ^ {\prime 2} - u ^ {2}},
$$

$$
f (u) = \frac {4 u (u + 1) - 2}{u ^ {3}} \ln \left(\sqrt {u} + \sqrt {u - 1}\right) - \frac {2 (u + 1) \sqrt {u - 1}}{u ^ {5 / 2}}.
$$

Note that eq. (2.2) is similar to the Schrödinger equation if the coordinate  $z$  is replaced by the time  $t$  and  $(\omega + \mathcal{M})$  is replaced by  $-\mathcal{H}$ , where  $\mathcal{H}$  denotes the Hamiltonian. Thus, analogous to solving the Schrödinger equation, one can also construct the transition matrix  $U(z) = e^{i\mathcal{M}z}$  for the photon-ALP propagation. For a more general case, one can define the density matrix  $\rho \equiv \psi \psi^{\dagger}$ , which satisfies an equation similar to the Von Neumann equation,

$$
i \frac {d}{d z} \rho = \rho \mathcal {M} ^ {\dagger} - \mathcal {M} \rho . \tag {2.9}
$$

The solution can then be obtained via  $\rho (z) = U(z)\rho_0U(z)^\dagger$ , where  $\rho_0$  is the initial condition. In our analysis, we assume an unpolarized photon beam such that  $\rho_0 = \mathrm{diag}(1 / 2,1 / 2,0)$ . The upper-left  $2\times 2$  submatrix of  $\rho$ , denoted as  $\rho_{\gamma}$ , can be parameterized as [41]

$$
\rho_ {\gamma} = \left( \begin{array}{c c} \rho_ {x} & \rho_ {x y} \\ \rho_ {x y} ^ {*} & \rho_ {y} \end{array} \right) = \frac {1}{2} \left( \begin{array}{c c} I + Q & U - i V \\ U + i V & I - Q \end{array} \right), \tag {2.10}
$$

where  $I$ ,  $Q$ ,  $U$ , and  $V$  are the Stokes parameters. The photon degree of polarization  $\Pi_L$  is then given by [42]

$$
\Pi_ {L} = \frac {\sqrt {Q ^ {2} + U ^ {2}}}{I}. \tag {2.11}
$$

The photon survival probability after propagation is given by [31]

$$
P _ {\gamma \rightarrow \gamma} = \rho_ {x} + \rho_ {y} = I. \tag {2.12}
$$

# 3 Two different propagation modes

Although recent studies focused on numerical methods to solve the photon-ALP propagation, due to the complex medium effects and the magnetic fields in the astrophysical environments, there are instances where analytic calculations are good approximations to the photon propagation. In this section we first identify the conditions in which analytic methods to the photon propagation can be used. We then discuss two different propagation modes that are found in our analysis.

We will use the high-energy photons as the example in this section, though analytic methods can also be used for low-energy photons. We first consider the very high energy photons with  $\omega > 10^{5}\mathrm{GeV}$ . At such high energy, the matrix  $\mathcal{M}$  can be greatly simplified, because the various  $\Delta$  terms can be neglected except the new physics term  $\Delta_{a\gamma}$  and the absorption term  $\Gamma$ , as shown in figure 1, where  $g_{a\gamma} = 3\times 10^{-12}\mathrm{GeV}^{-1}$  and  $B = 5.5\mu \mathrm{G}$  are assumed. Thus we have

$$
\mathcal {M} \simeq \frac {1}{2} \left( \begin{array}{c c c} i \Gamma & 0 & 0 \\ 0 & i \Gamma & g _ {a \gamma} B \\ 0 & g _ {a \gamma} B & 0 \end{array} \right). \tag {3.1}
$$

We further assume that the variation of external magnetic field is relatively small so that it can be approximated by a uniform magnetic field. In this case, one can then analytically solve the propagation. We note that the analytical solution can facilitate the calculations and can reveal some physics pictures of the problem that are difficult to be seen in the numerical calculations.

We then find that in the analytic solutions for the simplified  $\mathcal{M}$ , there exist two different propagation modes of photons, characterized by the sign of  $D$ , which is defined as

$$
D \equiv g _ {a \gamma} ^ {2} B ^ {2} - \frac {\Gamma^ {2}}{4}. \tag {3.2}
$$

We discuss these two propagation modes:  $D > 0$  and  $D < 0$  below.

![](images/ed456ca5f5a76987e1deca3504f95ada788bffa863a200d1e4860cf92b662e2a.jpg)  
Figure 1. Matrix elements of  $\mathcal{M}$  as a function of the photon energy  $\omega$ . Here we take  $g_{a\gamma} = 3 \times 10^{-12} \mathrm{GeV}^{-1}$ ,  $B = 5.5 \mu \mathrm{G}$ ,  $m_a = 1 \times 10^{-18} \mathrm{GeV}$ ,  $n_e = 0.1 \mathrm{~cm}^{-3}$  accounting for the electron number density in the Andromeda galaxy (M31) [43-45] and  $\rho_{\mathrm{RF}} = 2.01 \times 10^{-51} \mathrm{GeV}^4$  accounting for the energy density of CMB [40]. We use eq. (2.6) and eq. (2.7) to compute  $\Delta_{\mathrm{QED}}$  and  $\Delta_{\mathrm{dis}}$ ; for  $\omega > 10^{5} \mathrm{GeV}$ , we further multiply a factor of  $g_2(\omega / \omega_2)$  where  $\omega_2 = 10^5 \mathrm{GeV}$  given in ref. [40]. The  $\Gamma$  curve is adopted from ref. [34].

# 3.1 The  $D > 0$  propagation mode

We first discuss the  $D > 0$  case. To solve the propagation analytically, we first compute the transition matrix  $U(z) = e^{i\mathcal{M}z}$ , where  $\mathcal{M}$  is given by eq. (3.1). Thus, for the  $D > 0$  case, we have

$$
U _ {D > 0} (z) = \frac {e ^ {- \frac {\Gamma}{4} z}}{\cos \varphi} \left( \begin{array}{c c c} e ^ {- \frac {\Gamma}{4} z} \cos \varphi & 0 & 0 \\ 0 & \cos \left(\varphi + \frac {\Delta}{2} z\right) & i \sin \frac {\Delta}{2} z \\ 0 & i \sin \frac {\Delta}{2} z & \cos \left(\varphi - \frac {\Delta}{2} z\right) \end{array} \right), \tag {3.3}
$$

where we have defined  $\Delta = \sqrt{D}$  and  $\varphi = \arctan (\Gamma /(2\Delta))$ . We then compute  $\rho (z)$  at distance  $z$  from the source via  $\rho (z) = U(z)\rho_0U(z)^\dagger$ , where  $\rho_0 = \mathrm{diag}(1 / 2,1 / 2,0)$  is initial condition for an unpolarized photon beam at the source. The matrix elements of  $\rho_{\gamma}(z)$  in this case are given by

$$
\rho_ {x} (z) = \frac {1}{2} e ^ {- \Gamma z}, \tag {3.4}
$$

$$
\rho_ {y} (z) = \frac {1}{2} \frac {e ^ {- \frac {\Gamma}{2} z}}{\cos^ {2} \varphi} \cos^ {2} \left(\varphi + \frac {\Delta}{2} z\right), \tag {3.5}
$$

$$
\rho_ {x y} (z) = 0. \tag {3.6}
$$

Here  $\rho_{x}(z)$  and  $\rho_{y}(z)$  describe the intensities of photons polarized along  $x$  and  $y$  directions, respectively. Because the off-diagonal element  $\rho_{xy}(z)$  vanishes in this case, the photon degree of polarization  $\Pi_L$  becomes

$$
\Pi_ {L} = \frac {\left| \rho_ {x} - \rho_ {y} \right|}{\rho_ {x} + \rho_ {y}}. \tag {3.7}
$$

We note that the intensities of photons with polarization along the  $x$  and  $y$  directions exhibit different dependencies on the propagation distance  $z$ . We discuss the distinct behaviors below.

First, the intensity of photons polarized along the  $y$  direction depends both on the attenuation term  $\Gamma$  and on the ALP-interaction term  $\Delta_{a\gamma}$  (through  $\Delta$  and  $\varphi$ ), but the intensity along the  $x$  direction depends on  $\Gamma$  only. This discrepancy arises from the fact that the external magnetic field is taken to be along the  $y$  direction so that photons polarized along the  $x$  direction are not directly affected by the ALP.

Second, the intensity of photons polarized along the  $x$  direction decreases exponentially as the distance  $z$  increases, with a decay length of  $L_{d} = \Gamma^{-1}$ , as shown in eq. (3.4). On the other hand, the intensity for photons polarized along the  $y$  direction appears to exhibit a longer decay length of  $L_{d} = (\Gamma /2)^{-1}$  (twice of that along the  $x$  direction), based solely on the argument of the exponential function in eq. (3.5). This change on the decay length is due to the fact that photons polarized along the  $y$  direction can convert into ALPs that do not experience the photon attenuation effects  $\Gamma$ . We emphasize that the actual decay length for photons polarized along the  $y$  direction will deviate somewhat from the value of  $L_{d} = (\Gamma /2)^{-1}$  due to the additional  $z$ -dependence in eq. (3.5). Specifically, taking the limit  $g_{a\gamma}\rightarrow 0$  in eq. (3.5) introduces an additional exponential factor  $e^{-(\Gamma /2)z}$ , which must be taken into account. $^{1}$

Third, the intensity of photons polarized along the  $y$  direction, while propagating, exhibits an oscillatory behavior. We define the oscillation length, denoted by  $L_{o}$ , as the period of the absolute value of the cosine function in eq. (3.5). The oscillation length is given by

$$
L _ {o} = \frac {2 \pi}{\Delta} = \frac {2 \pi}{\sqrt {g _ {a \gamma} ^ {2} B ^ {2} - \left(\frac {\Gamma}{2}\right) ^ {2}}}. \tag {3.8}
$$

Thus, the increase in the difference between  $g_{a\gamma}B$  and  $\Gamma$  leads to an increase in the oscillation length. We note that the oscillation is attenuated by the exponential factor  $e^{-(\Gamma /2)z}$ .

# 3.2 The  $D < 0$  propagation mode

We next discuss the  $D < 0$  case. For the case of  $D < 0$ , the transition matrix  $U(z)$  can be written as

$$
U _ {D <   0} (z) = \frac {e ^ {- \frac {\Gamma}{4} z}}{\cos 2 \alpha} \left( \begin{array}{c c c} e ^ {- \frac {\Gamma}{4} z} \cos 2 \alpha & 0 & 0 \\ 0 & e ^ {- \frac {\Delta}{2} z} \cos^ {2} \alpha - e ^ {\frac {\Delta}{2} z} \sin^ {2} \alpha & i \left(e ^ {\frac {\Delta}{2} z} - e ^ {- \frac {\Delta}{2} z}\right) \sin \alpha \cos \alpha \\ 0 & i \left(e ^ {\frac {\Delta}{2} z} - e ^ {- \frac {\Delta}{2} z}\right) \sin \alpha \cos \alpha & e ^ {\frac {\Delta}{2} z} \cos^ {2} \alpha - e ^ {- \frac {\Delta}{2} z} \sin^ {2} \alpha \end{array} \right), \tag {3.9}
$$

where  $\Delta = \sqrt{-D}$  and  $\alpha = \arcsin \sqrt{\Gamma / 2 - \Delta} /\sqrt{\Gamma}$ .<sup>2</sup>

For an unpolarized photon beam at the source, the diagonal matrix elements of  $\rho_{\gamma}(z)$  are given by

$$
\rho_ {x} (z) = \frac {1}{2} e ^ {- \Gamma z}, \tag {3.10}
$$

$$
\rho_ {y} (z) = \frac {1}{2} \frac {e ^ {- \frac {\Gamma}{2} z}}{\cos^ {2} (2 \alpha)} e ^ {- \Delta z} \left| \cos^ {2} \alpha - e ^ {\Delta z} \sin^ {2} \alpha \right| ^ {2}, \tag {3.11}
$$

$$
\rho_ {x y} (z) = 0. \tag {3.12}
$$

We note that both  $\rho_{x}(z)$  and  $\rho_{xy}(z)$  are the same as in the  $D > 0$  case. Similarly to the  $D > 0$  case, the vanishing off-diagonal element  $\rho_{xy}(z)$  leads to a simplified expression of the photon as given in eq. (3.7). We next discuss the distinct dependencies on the propagation distance  $z$  of the intensities of photons with polarization along the  $x$  and  $y$  directions, and also make comparison to the  $D > 0$  case.

First, photons polarized along the  $x$  direction only undergo attenuation characterized by the photon attenuation coefficient  $\Gamma$ , whereas photons polarized along the  $y$  direction are influenced both by  $\Gamma$  and by the mixing term with the ALP. This is similar to the  $D > 0$  case.

Second, the ALP-photon mixing term weakens the photon attenuation. This can be seen from the argument of the exponential function in eq. (3.11), which hints a decay length of  $L_{d} = (\Gamma /2 + \Delta)^{-1}$  for  $y$ -polarized photons. The decay length of  $x$ -polarized photons is  $L_{d} = \Gamma^{-1}$ . Since  $\Delta < \Gamma /2$ , photons polarized along the  $y$ -direction has a larger decay length than photons polarized along the  $x$ -direction. The reason behind this is the same as the  $D > 0$  case: when propagating,  $y$ -polarized photons can convert into ALPs which are unaffected by photons attenuation effects.

Third, in contrast to the  $D > 0$  scenario, where photons polarized in the  $y$  direction exhibit oscillations, photons in the  $D < 0$  scenario do not exhibit any oscillatory behavior.

# 4 Propagation modes for high-energy photons with  $\omega \geq 100$  GeV

In this section we discuss the propagation modes for photons with energy  $\omega \geq 100\mathrm{GeV}$ . In the Milky Way (MW) and many other spiral galaxies including the Andromeda galaxy (M31), the strength of the magnetic field is of  $O(1)$ $\mu \mathrm{G}$  [46-48]. Taking  $B = 1$ $\mu \mathrm{G}$  and  $g_{a\gamma} = 3\times 10^{-12}\mathrm{GeV}^{-1}$ , we find that  $Bg_{a\gamma}\simeq 0.01\mathrm{kpc}^{-1}$ ; equating  $Bg_{a\gamma}$  with  $\Gamma /2$  leads to the photon energy at  $\sim 250\mathrm{TeV}$ . Thus, in this case, the photon propagation mode is the  $D < 0$  mode for  $\omega \gtrsim 250\mathrm{TeV}$ , and the  $D > 0$  mode for  $\omega \lesssim 250\mathrm{TeV}$ . For active galactic nuclei, galaxy clusters, and intergalactic space, the typical magnetic field strengths are  $O(1 - 10^{5})$ $\mu \mathrm{G}$  [49, 50],  $O(1 - 10)$ $\mu \mathrm{G}$  [51], and  $O(10^{-7} - 1)$  nG [52, 53], respectively. Because the magnetic field in active galactic nuclei and galaxy clusters can be much larger than that in spiral galaxies, one can have the  $D > 0$  mode for photons with energy  $\omega \geq 100\mathrm{GeV}$ . On the other hand, the magnetic field in intergalactic space is much smaller than that in the MW galaxy, leading to the  $D < 0$  mode for photons with energy  $\omega \geq 100\mathrm{GeV}$ . We note that our general discussions here are not applicable in extreme environments where the magnitude of the magnetic field and/or electron number density is significantly large such that the terms  $\Delta_{\mathrm{QED}}$  and/or  $\Delta_{\mathrm{pl}}$  in the  $\mathcal{M}$  matrix can become substantial.

# 4.1 Photons from M31

To be concrete, in this section we focus on photons originating from the M31 galaxy and propagating to Earth. In this case, the photon-ALP propagation consists of three components:

Table 1. The regular component of the magnetic field in the M31 disk, adopted from ref. [48]. Here  $r$  is the radial coordinate and  $B$  is the magnetic field.  

<table><tr><td>r (kpc)</td><td>6-8</td><td>8-10</td><td>10-12</td><td>12-14</td></tr><tr><td>B (μG)</td><td>4.9</td><td>5.2</td><td>4.9</td><td>4.6</td></tr></table>

propagation in the M31 galaxy, propagation in the Milky Way (MW) galaxy, and propagation through the intergalactic space between the two galaxies. Note that since the inclination of the M31 galaxy is  $77.5^{\circ}$ ,[6] and the M31 disk is about 1 kpc thick [54, 55], photons propagating in the M31 disk with distance of  $\sim 5$  kpc can point to Earth. Also note that because the M31 galaxy is located at RA 00h 42m 44.3s, Dec  $41^{\circ} 16'$  9", photons originating from it have a rather small propagation distance in the MW disk. Moreover, the out-of-disk component of the magnetic field in the MW galaxy is very small [46]. Thus, in our analysis we only consider photon-ALP propagation in the M31 galaxy and in the intergalactic space, but neglect the propagation in the MW galaxy.

Although the M31 galaxy is the nearest major galaxy to the MW galaxy, its high inclination angle presents some challenges for observing its structure [56-58]. The M31 galaxy comprises several major components, including a disk and a bulge. For the bulge radius, various measurements and analyses have produced a wide range of values, ranging from  $0.1\mathrm{kpc}$  to  $10\mathrm{kpc}$  [59]. Accounting for the uncertainties, we model the M31 galaxy with a spherical bulge with radius  $r < 6\mathrm{kpc}$  and a disk with radius  $6 < r < 20\mathrm{kpc}$  [60]. We further note that the current understanding of the magnetic field in the M31 galaxy remains limited [43, 61]. Thus, for the bulge, we adopt a magnetic field of  $6\mu \mathrm{G}$  [58, 62], and assume that the direction of the magnetic field is azimuthal, analogous to the MW bulge [46]. For the M31 disk, we only consider the regular component of the magnetic field, and adopt the model in ref. [48], which is given in table 1. We neglect the turbulent field of the M31 galaxy, since its coherence length is usually much smaller than the  $\gamma \leftrightarrow a$  oscillation length [18].

The magnitude of the intergalactic magnetic field has been found to be in the range of  $3 \times 10^{-7} \mathrm{nG} \lesssim \mathrm{B} \lesssim 1.7 \mathrm{nG}$  [52, 53]. Note that the intergalactic magnetic field is believed to be domain-like with a domain length of  $\mathcal{O}(1)$  Mpc: within one domain, the magnetic field is constant [63, 64]. Since the M31 galaxy is  $\sim 765$  kpc away from us, in our analysis we assume the intergalactic space between the M31 and MW galaxies to be within one domain of the intergalactic magnetic field. We thus take a constant magnetic field of  $B = 1 \mathrm{nG}$  for the intergalactic magnetic field between the M31 and MW galaxies.

To illustrate the two different propagation modes ( $D > 0$  and  $D < 0$ ), we consider the ALP model where  $m_{a} = 10^{-18}\mathrm{GeV}^{7}$  and  $g_{a\gamma} = 3\times 10^{-12}\mathrm{GeV}^{-1}$ , and monochromatic photons originating from the M31 galaxy with energy of  $5\times 10^{2}\mathrm{GeV}$  and  $5\times 10^{5}\mathrm{GeV}$ :

- For the  $5 \times 10^{2}$  GeV case, we consider photons originating from the center of the M31 galaxy and propagating to Earth such that the propagation distances in the M31 galaxy

are  $6\mathrm{kpc}$  in the bulge and  $5\mathrm{kpc}$  in the disk. Note that for the  $\omega = 5\times 10^{2}\mathrm{GeV}$  case, the attenuation term is  $\Gamma \sim 10^{-4}\mathrm{kpc}^{-1}$ , and the photon-ALP mixing term in the intergalactic space is  $g_{a\gamma}B\sim 10^{-4}\mathrm{kpc}^{-1}$ , where we have used  $B = 1$  nG. In the contrast, the photon-ALP mixing term in the M31 galaxy is  $g_{a\gamma}B\sim 10^{-1}\mathrm{kpc}^{-1}$ , where we have used  $B = 6\mu \mathrm{G}$ . Thus, in this case we neglect the propagation in the intergalactic space and only consider the propagation in the M31 galaxy. Note that the propagation in the M31 galaxy is the  $D > 0$  mode, since  $g_{a\gamma}B > \Gamma /2$  in this case.

- For the  $5 \times 10^{5}$  GeV case, we consider photons originating from the edge of the M31 galaxy so that the propagation within the M31 galaxy can be neglected. We thus only need to consider the propagation in the intergalactic space. Note that the attenuation effect for the  $\omega = 5 \times 10^{5}$  GeV case in the intergalactic space is significant:  $\Gamma \sim 10^{-2} \mathrm{kpc}^{-1}$ , which exceeds the photon-ALP term,  $g_{a\gamma}B \sim 10^{-4} \mathrm{kpc}^{-1}$ , in the intergalactic space. Therefore, the photon propagation in this case corresponds to the  $D < 0$  mode.

# 4.2 The  $D > 0$  case

We first discuss the physics in the  $D > 0$  case, including the photon degree of polarization and the photon survival probability.

# 4.2.1 Photon degree of polarization

For the  $D > 0$  mode, we first compute the photon degree of polarization  $\Pi_L$ , which is given by eq. (3.7), in the absence of the off-diagonal elements of the  $\rho_{\gamma}$  matrix. Due to the interaction with the ALP, photons observed at Earth can be fully polarized, i.e.,  $\Pi_L = 1$ , in spite of the unpolarized initial condition at the source position. This is a remarkable signature for ALP detection. Thus, it is of great interest to determine under what conditions photons observed can be fully polarized. The nearly fully-polarized  $\Pi_L \sim 1$  can be achieved in two cases: (1)  $\rho_x \gg \rho_y$ , and (2)  $\rho_x \ll \rho_y$ .

- The  $\rho_{x} \gg \rho_{y}$  case: Since  $\rho_{x}(z) > 0$ , the full-polarization case  $\Pi_{L} = 1$  can be achieved if  $\rho_{y}(z) = 0$ ; by using the analytic expression of  $\rho_{y}(z)$  given in eq. (3.5), we obtain the  $z$  values for  $\Pi_{L} = 1$ :

$$
z _ {n} = \frac {2}{\Delta} \left[ \frac {n - 1}{2} \pi + \arctan \left(\frac {2 \Delta}{\Gamma}\right) \right], \tag {4.1}
$$

where  $n$  is a positive odd integer. Thus, the full-polarization  $\Pi_L = 1$  phenomena are evenly distributed in space, and the distance between adjacent  $\Pi_L$  points is  $2\pi /\Delta$ . Because  $\rho_{x}(z) > 0$  decreases with  $z$ , the detection should be performed with the smallest distance  $z_{1}$  in eq. (4.1), if possible. Note that  $z_{1} = 2\arctan (2\Delta /\Gamma) / \Delta$  can be significantly small if  $g_{a\gamma}B$  is sufficiently large.

- The  $\rho_{x} \ll \rho_{y}$  case: Because the  $y$ -polarized photons have a longer decay length than the  $x$ -polarized photons, eventually  $\rho_{x}$  can become much smaller than  $\rho_{y}$ , leading to a relatively large polarization,  $\Pi_{L} \simeq 1$ . By using the analytic expressions given in eq. (3.4) and eq. (3.5), we obtain the maximum values of  $\Pi_{L}$  in the  $\rho_{x} \ll \rho_{y}$  case

$$
\Pi_ {L} ^ {n} = \tanh  \left(\frac {\Gamma}{4} z _ {n}\right), \text {w i t h} z _ {n} = \frac {\pi n}{\Delta}, \tag {4.2}
$$

![](images/f7ea475d48b639537bee24cef5b2c28769a6bece93858bea7e9cac9b7b732142.jpg)  
Figure 2. The photon polarization degree  $\Pi_L$  (left) and the photon survival probability  $P_{\gamma \rightarrow \gamma}$  (right) as a function of the propagation distance  $z$  in the M31 galaxy (red-dotted), in the  $D > 0$  case. Here we consider photons originating from the central region of the M31 galaxy such that the photon propagation distances are  $6\mathrm{kpc}$  in the bulge and  $5\mathrm{kpc}$  in the disk of the M31 galaxy, respectively. Here, we use  $g_{a\gamma} = 3\times 10^{-12}\mathrm{GeV}^{-1}$  and  $\omega = 500\mathrm{GeV}$ . Also shown are the calculations of  $\Pi_L$  and  $P_{\gamma \rightarrow \gamma}$  using a uniform magnetic field  $B = 5.5\mu \mathrm{G}$  (blue-solid).

![](images/d81e10ef2949dc7829e8e972b5309c510f70ddeed5f16564f21b54e0080c0b92.jpg)

where  $n$  is a positive even integer. We further extrapolate the maximum value of  $\Pi_L$  on  $z_n$ , as given in eq. (4.2), to all  $z$  values,

$$
\Pi_ {L} = \tanh  \left(\frac {\Gamma}{4} z\right), \tag {4.3}
$$

which can be interpreted as the theoretical upper bound of  $\Pi_L$ . It is interesting to note that eq. (4.3) is independent of the external magnetic field.

The left-panel figure of figure 2 shows the photon polarization degree  $\Pi_L$  as a function of the propagation distance  $z$ , for the case where  $m_a = 10^{-18}\mathrm{GeV}$ ,  $g_{a\gamma} = 3\times 10^{-12}\mathrm{GeV}^{-1}$  and  $\omega = 500\mathrm{GeV}$ . Note that  $\Pi_L$  at different  $z$  values can be interpreted as the observed polarization for photons with shorter propagation distances in the M31 galaxy. In figure 2, we analyze photon propagation using two different treatments on the magnetic fields: (1) the magnetic model of the M31 galaxy as described in section 4.1, and (2) a constant magnetic field of  $B = 5.5~\mu \mathrm{G}$ , which is the average M31 magnetic field. We find that the approximation of using a constant magnetic field of  $B = 5.5~\mu \mathrm{G}$  closely matches the actual magnetic model of the M31 galaxy. Thus, computing photon propagation using the analytical formulas in section 3 with a constant magnetic field is a valid approximation for the analysis.

In figure 2, the maximal photon degree of polarization should first occur in the  $\rho_{x} \gg \rho_{y}$  case. According to eq. (4.1),  $z_{1} \simeq 61.7\mathrm{kpc}$  for  $n = 1$ , and the distance between adjacent peaks in the  $\rho_{x} \gg \rho_{y}$  case is  $2\pi/\Delta \simeq 123.4\mathrm{kpc}$ . We observe that  $z_{1}$  and  $2\pi/\Delta$  are not visible in the left-panel figure of figure 2, because both the propagation distance  $z \sim 10\mathrm{kpc}$  and the ALP coupling term  $g_{a\gamma}B \sim 10^{-1}\mathrm{kpc}^{-1}$  are relatively small. To observe polarization peaks, the condition  $g_{a\gamma}Bz \gtrsim \mathcal{O}(10)$  must be met. Therefore, with ALP parameters  $g_{a\gamma} = 3 \times 10^{-12}\mathrm{GeV}^{-1}$  and  $m_{a} = 10^{-18}\mathrm{GeV}$ , the polarization peaks are unobservable for photons originating from M31.

![](images/b90b0dbd3f16e292d8f1e5d6fc261b958508feb12592af2f6c6e1cdfc2704e97.jpg)  
Figure 3. Same as figure 2 except  $g_{a\gamma} = 4 \times 10^{-11} \, \mathrm{GeV}^{-1}$ .

![](images/a32c4f77aa296228b6c7c293ded49b592daa6bf1ad00fa2dc2268a69484939fb.jpg)

To illustrate the underlying physics, we increase the ALP-photon coupling to  $g_{a\gamma} = 4 \times 10^{-11} \mathrm{GeV}^{-1}$  in the left-panel figure of figure 3. The first polarization peak appears at  $z = 4.63$  kpc, corresponding to  $z_{1}$  in eq. (4.1). Additionally, there also exists a small polarization peak at  $z = 9.26$  kpc, corresponding to  $z_{2}$  in eq. (4.2). While the coupling constant  $g_{a\gamma} = 4 \times 10^{-11} \mathrm{GeV}^{-1}$  exceeds current experimental limits, it allows the polarization peaks to become clearly visible. Alternatively, the desired polarization peaks could also become observable with smaller, experimentally allowed ALP couplings if the magnetic field is significantly large with a substantial coherence length. For example, in environments such as galaxy clusters where  $g_{a\gamma}Bz \sim \mathcal{O}(100)$ , the required conditions may arise. If such systems are identified in future observations, the same physics demonstrated in figure 3 could be realized using parameters consistent with current experimental constraints.

# 4.2.2 Photon survival probability

The right-panel figure of figure 2 shows the photon survival probability  $P_{\gamma \rightarrow \gamma}$  as a function of the propagation distance  $z$ , for the same parameters as the left-panel figure of figure 2. Again, the oscillatory behavior in the photon survival probability due to the presence of the ALP is difficult to detect in figure 2. To illustrate the oscillatory behavior, we increase the ALP-photon coupling to  $g_{a\gamma} = 4 \times 10^{-11} \mathrm{GeV}^{-1}$  in the right-panel figure of figure 3, where the photon survival probability reaches its minimum value at  $z \simeq 4.63 \mathrm{kpc}$ . Note that the photon survival probability  $P_{\gamma \rightarrow \gamma}$  is bounded from above by  $P_{\gamma \rightarrow \gamma} < (e^{-\Gamma z} + e^{-\Gamma z / 2} / \cos \phi) / 2$ , which is larger than the case without ALP,  $P_{\gamma \rightarrow \gamma} = e^{-\Gamma z}$ . Thus, the presence of ALP makes distant galaxies brighter, resulting in a better detection probability.

# 4.3 The  $D < 0$  case

We next discuss the physics in the  $D < 0$  case. The left panel figure of figure 4 shows the degree of polarization  $\Pi_L$ , for the  $\omega = 5 \times 10^5$  GeV case, as a function of the propagation distance  $z$ , where a constant intergalactic magnetic field  $B = 1 \mathrm{nG}$ ,  $g_{a\gamma} = 3 \times 10^{-12} \mathrm{GeV}^{-1}$ , and  $\Gamma = 0.057 \mathrm{kpc}^{-1}$  are used. Similarly to the  $D > 0$  propagation mode, the nearly fully-polarized  $\Pi_L \sim 1$  in the  $D < 0$  propagation mode can be also achieved in two cases: (1)  $\rho_x \gg \rho_y$ , (2)  $\rho_x \ll \rho_y$ .

![](images/85064f04edb6399e3d95fe5cf85015e50087e33f79587c84eeca3294f68408d7.jpg)  
Figure 4. The photon polarization degree  $\Pi_L$  (left) and the photon survival probability  $P_{\gamma \rightarrow \gamma}$  (right) as a function of the photon propagating distance  $z$ , in the  $D < 0$  case. A constant external magnetic  $B = 1$  nG, the coupling constant  $g_{a\gamma} = 3\times 10^{-12}\mathrm{GeV}^{-1}$ , and the energy  $\omega = 5\times 10^{5}\mathrm{GeV}$  are used.

![](images/60ca22c16bcbdf92aac1ec3c429207980265056e14bcee7c4f080710eccaf006.jpg)

We first discuss the  $\rho_{x} \gg \rho_{y}$  case. In this case, the full-polarization cases  $\Pi_{L} = 1$  occurs when  $\rho_{y}(z) = 0$ , since  $\rho_{x}(z) > 0$ . Unlike the infinite  $z$  values for  $\rho_{y}(z) = 0$  in the  $D > 0$  case, there is only a single point for  $\rho_{y}(z) = 0$  in the  $D < 0$  case. By using the analytic expression of  $\rho_{y}(z)$  in eq. (3.11), we obtain the single  $z$  value for  $\rho_{y}(z) = 0$  as

$$
z _ {0} = \frac {1}{\Delta} \ln \frac {\Gamma + 2 \Delta}{\Gamma - 2 \Delta} = \frac {2}{\sqrt {\left(\frac {\Gamma}{2}\right) ^ {2} - g _ {a \gamma} ^ {2} B ^ {2}}} \ln \frac {\frac {\Gamma}{2} + \sqrt {\left(\frac {\Gamma}{2}\right) ^ {2} - g _ {a \gamma} ^ {2} B ^ {2}}}{g _ {a \gamma} B}. \tag {4.4}
$$

In figure 4, one has that  $z_0 \simeq 612 \mathrm{kpc}$ , which is the first point where the full-polarization cases  $\Pi_L$  reaches one.

We next discuss the  $\rho_{x} \ll \rho_{y}$  case. Because the  $y$ -polarized photons have a longer decay length than the  $x$ -polarized photons, eventually  $\rho_{x}$  can become much smaller than  $\rho_{y}$ , leading to a nearly full-polarization,  $\Pi_{L} \simeq 1$ . This occurs at a relatively large  $z$  value. Note that  $\rho_{y}$  has a local maximal point at  $z = 2z_{0}$ . Thus, we take the  $z \gtrsim 2z_{0}$  as the region for the nearly full-polarization,  $\Pi_{L} \simeq 1$ .

The right panel figure of figure 4 shows the photon survival probability  $P_{\gamma \rightarrow \gamma}$ , in the  $D < 0$  case. Unlike the  $D > 0$  case, here  $P_{\gamma \rightarrow \gamma}$  does not oscillate with the propagation distance  $z$ . Nevertheless, the presence of ALPs can still facilitate the detection of remote photons more effectively than in the absence of ALPs.

We next investigate the optimal conditions for observing polarization signals in the  $D < 0$  propagation mode. In order to observe a distinct polarization signature with a strong signal strength, two conditions must be met. Firstly, the degree of polarization should be close to one, namely  $\Pi_L\approx 1$ . This condition can be achieved either at  $z\simeq z_0$  or at  $z\geq 2z_{0}$ . Secondly, the total intensity of photons should be significant, which implies a significant photon survival probability  $P_{\gamma \rightarrow \gamma} = \rho_x + \rho_y$ . Since  $\rho_{x}(z)$  decreases with increasing  $z$ , observation at  $z = z_{0}$  should be perused as the first option.

We next study the  $z \geq z_0$  region. In this region, while the intensity  $\rho_x(z)$  continues to decrease with increasing  $z$ , the intensity  $\rho_y(z)$  starts to grow from zero at  $z = z_0$  to its local

![](images/c49601879f6883e065be07ca775d1746c35c0568ebef8ef160ed6dd6c7a96711.jpg)

![](images/e7028c67f9b25b2d5927d4117e66b76c020ad35319be8535e07e55fe98d77137.jpg)

![](images/1a5a72122b186384ec6d8650aba41887d003c6ab9b82524277650834da79e58e.jpg)  
Figure 5. The photon survival probability  $P_{\gamma \rightarrow \gamma}$  (upper) and the photon degree of polarization  $\Pi_L$  (lower) as a function of the photon energy. Blue lines are results adopted from figure 11 of ref. [18], where photons originate from clusters at redshift  $z = 0.03$  (left column) and at redshift  $z = 0.4$  (right column). The red lines indicate  $P_{\gamma \rightarrow \gamma} = 1.8\%$ .

![](images/eeefe095451b50bfb14948bf6496c96dd16a6dc43617f047fea2248bdca8868e.jpg)

maximum point at  $z = 2z_{0}$ , and then decreases with increasing  $z$ . Therefore, the maximum value of the photon survival probability in the  $z \geq z_{0}$  region should occur in the interval of  $z_{0} \leq z \leq 2z_{0}$ ; within this interval, the maximum value of  $\rho_{x}$  is  $e^{-\Gamma z_{0}} / 2$  at  $z = z_{0}$ , which is the same as the maximum value of  $\rho_{y}$  at  $z = 2z_{0}$ . The theoretical upper bound on the photon survival probability can be obtained by simply summing these two maximum values, leading to  $P_{\gamma \rightarrow \gamma} < e^{-\Gamma z_{0}}$ . We next study the possible maximum value of the above upper bound. By using eq. (4.4), we have  $\Gamma z_{0} = 2x\ln[(x + 1) / (x - 1)]$ , where  $x \equiv \Gamma / (2\Delta) \geq 1$ . When  $x \to \infty$ , the quantity  $\Gamma z_{0}$  reaches its minimum value, which is 4. This can be achieved by setting  $\Delta = 0$ , which arises if  $\Gamma / 2 = g_{a\gamma}B$ . This then leads to a maximum value for the upper bound on the photon survival probability  $P_{\gamma \rightarrow \gamma} < e^{-4} \simeq 1.8\%$ .

Therefore, for  $D < 0$  propagation mode, the observations on the degree of polarization  $\Pi_L$  should be first conducted at the distance of  $z \simeq z_0$  and  $z \simeq 2z_0$ . The theoretical upper bound on the photon survival probability in the  $z \geq z_0$  region is  $\simeq 1.8\%$ . However, we note that in figure 4, the photon survival probability  $P_{\gamma \rightarrow \gamma} \simeq 10^{-15}$  for  $z \geq z_0$ ; thus, it is difficult to observe a significant polarization signal in this case.

In figure 5, we further compare the theoretical upper bound on the photon survival probability in the  $z \geq z_0$  region, which is  $P_{\gamma \rightarrow \gamma} < 1.8\%$ , to the actual calculations given in ref. [18], for photons produced in galaxy clusters and propagating to Earth, where different medium effects and varying magnetic fields are taken into consideration. We find that in the energy range where the photon polarization  $\Pi_L \approx 1$ , which is  $\omega \gtrsim 2 \times 10^4 \mathrm{GeV}$  ( $\omega \gtrsim 10^3 \mathrm{GeV}$ ) on the left (right) panel figure of figure 5, the photon survival probability is indeed below  $1.8\%$ .

# 5 Propagation modes for photons with energy  $\omega = 10^{-3} - 10^{2}$  GeV

In this section, we discuss the propagation modes for photons with energy  $\omega = 10^{-3} - 10^{2}\mathrm{GeV}$ . In this energy range, as compared to the ALP-photon mixing term, the quantity  $\Gamma$  can also

be considered negligible, in addition to the  $\Delta_x$  and  $\Delta_y$  terms, which are considered to be negligible in section 3. Thus our analytical analysis carried out in section 3 is still valid and can be further simplified by taking the  $\Gamma \rightarrow 0$  limit. In section 3 we have neglected the ALP mass term. In this section we also study the effects of the ALP mass term.

We first discuss the case where the ALP mass term is neglected. In this case, we take the  $\Gamma \rightarrow 0$  limit in eqs. (3.4) and (3.5), which lead to

$$
\rho_ {x} (z) = \frac {1}{2}, \tag {5.1}
$$

$$
\rho_ {y} (z) = \frac {1}{2} \cos^ {2} \left(\frac {g _ {a \gamma} B z}{2}\right). \tag {5.2}
$$

Thus, both  $\rho_{x}(z)$  and  $\rho_{y}(z)$  are independent on energy, which also result in energy-independence of the photon survival probability  $P_{\gamma \rightarrow \gamma}$  and the photon degree of polarization  $\Pi_L$ .

We next discuss the case where the ALP mass term is important. We consider the case where  $m_{a} = 10^{-18}$  GeV. In this case, we have  $\rho_{x}(z) = 1 / 2$ . The analytical form of  $\rho_{y}(z)$  can be obtained by replacing  $\Gamma$  in eq. (3.5) with  $2i\Delta_{aa} = -im_a^2 /\omega$ . Thus, we have

$$
\rho_ {y} (z) = \frac {1}{2} \left| \cos \left(\frac {\Delta}{2} z\right) + i \frac {\Delta_ {a a}}{\Delta} \sin \left(\frac {\Delta}{2} z\right) \right| ^ {2}, \tag {5.3}
$$

where  $\Delta = \sqrt{g_{a\gamma}^2B^2 + m_a^4 / (4\omega^2)}$ . We further compute the photon survival probability  $P_{\gamma \rightarrow \gamma}$  and the polarization degree  $\Pi_L$  by  $P_{\gamma \rightarrow \gamma} = 1 / 2 + \rho_y$  and

$$
\Pi_ {L} = \frac {1 - 2 \rho_ {y}}{1 + 2 \rho_ {y}} = (P _ {\gamma \rightarrow \gamma}) ^ {- 1} - 1. \tag {5.4}
$$

Thus, the polarization degree is solely determined by the photon survival probability  $P_{\gamma \rightarrow \gamma}$ . We note that the relationship between the polarization degree of photons and their survival probability has been discussed in refs. [18, 19, 32, 65, 66]. However, these references focused on the connection between the survival probability and the initial polarization degree. In contrast, eq. (5.4) addresses the relationship between the survival probability and the polarization degree at the time of observation.

Figure 6 shows the relation between the photon survival probability  $P_{\gamma \rightarrow \gamma}$  and the photon energy  $\omega$ . Interestingly, we find that there exist two energy regions where the photon survival probability  $P_{\gamma \rightarrow \gamma}$  is (nearly) independent of the photon energy: (1)  $\omega \lesssim 1\mathrm{GeV}$ , (2)  $\omega \gtrsim 10\mathrm{GeV}$ . This can be understood as follows. If the photon energy  $\omega$  is high such that the term  $\Delta_{aa} = -m_a^2 /(2\omega)$  can be neglected, this is just the case where the ALP mass can be neglected. Thus one should have energy-independent  $\rho_{x}$  and  $\rho_{y}$ , as given in eqs. (5.1) and (5.2), resulting in energy-independence in  $P_{\gamma \rightarrow \gamma}$  for  $\omega \gtrsim 10\mathrm{GeV}$  in figure 6. If the photon energy is low such that  $\Delta_{aa} / \Delta \to 1$ , we have  $\rho_{y}\to 1 / 2$ . This then leads to  $P_{\gamma \rightarrow \gamma}\approx 1$  for  $\omega \lesssim 1\mathrm{GeV}$  in figure 6.

The measurement of photon polarization degree can be carried out in the energy range of  $10^{-3} - 10^{1}$  GeV through advanced gamma-ray detectors, such as COSI [67], e-ASTROGAM [68, 69], and AMEGO [70], in the upcoming future. We note that the polarization degree,  $\Pi_L$ , can be indirectly determined using the relation  $\Pi_L = (1 / P_{\gamma \rightarrow \gamma} - 1)$ . Additionally, due to

![](images/1c5c98a70c46c068ebc45366ac0e2156b6f9e2209e7c86566fa1e0e653ef83de.jpg)  
Figure 6. Photon survival probability as a function of the energy. Here we take the magnetic field as  $B = 5 \mu \mathrm{G}$ , the coupling constant as  $g_{a\gamma} = 3 \times 10^{-12} \mathrm{GeV}^{-1}$ , the propagation distance as  $z = 1$  Mpc, and the ALP mass as  $m_{a} = 10^{-18}$  GeV.

the photon-ALP interaction, the photon energy spectrum can exhibit a distinct oscillatory pattern sandwiched between two almost energy-independent regions, as illustrated in figure 6, which may serve as a novel signature for the ALP detection.

# 6 Conclusions

In this paper we have identified two distinct photon propagation modes in the presence of ALPs. We classify the two different modes by the sign of  $D = (g_{a\gamma}B)^2 - \Gamma^2 / 4$ . For the  $D > 0$  propagation mode, the intensity of photon oscillates as propagating, producing multiple peaks along its propagation path. For the  $D < 0$  case, on the contrary, the intensity of photon does not exhibit any oscillatory behavior.

We use analytic methods to study the two photon propagation modes, because they are not readily discernible in numerical simulations, which have been extensively used in the literature to model the photon-ALP propagation. In our analytic methods, we assume a uniform magnetic field and negligible medium effects so that the propagation equation of the photon-ALP system can be solved in a simple analytic form.

We investigate photon propagation in two energy regions where our analytic methods are appropriate: (1) photon with energy  $\omega > 100\mathrm{GeV}$ ; (2) photon in the energy range of  $10^{-3} - 10^{2}\mathrm{GeV}$ . We identify the two photon propagation modes by comparing the magnetic field and the photon attenuation rate  $\Gamma$  in different astrophysical environments. For the two propagation modes, We compute the photon survival probability  $P_{\gamma \rightarrow \gamma}$  and the degree of photon polarization  $\Pi_L$ .

In the  $D > 0$  propagation mode, the fully-polarization can occur either in the  $\rho_{x} \ll \rho_{y}$  case or in the  $\rho_{y} \ll \rho_{x}$  case. Because of the oscillatory behavior in the intensity, the fully-polarization exhibits as various peaks in the propagation distance. In the  $D < 0$  propagation mode, there is no oscillation in the photon intensity. The detection condition that yields optimal results should include both a nearly full-polarization signal and a considerable photon survival probability. The distances at which this condition is met in the  $D < 0$  case are

Table 2. The regular component of the magnetic field model in the MW disk [46]. The disk is partitioned into 7 regions with 8 boundaries that are given by  $r_i = r_{xi} \exp(\phi \tan(90^\circ - \beta))$ , where  $\beta = 11.5^\circ$ ; the  $i$ -th region is bounded by the two curves  $r_{i-1}$  and  $r_i$ . The coordinates  $(r, \phi)$  are defined such that the Galactic center is  $(0,0)$  and the Sun is  $(-8.5 \, \mathrm{kpc}, 0)$ . The direction of the regular component is  $\hat{b} = \sin(\beta) \hat{r} + \cos(\beta) \hat{\phi}$ ; the magnitude of the regular component in the  $i$ -th region is given by  $B = b_i r_0 / r$  where  $r_0 = 5 \, \mathrm{kpc}$ .  

<table><tr><td>i</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>rxi(kpc)</td><td>5.1</td><td>6.3</td><td>7.1</td><td>8.3</td><td>9.8</td><td>11.4</td><td>12.7</td><td>15.5</td></tr><tr><td>bi(μG)</td><td></td><td>0.1</td><td>3.0</td><td>-0.9</td><td>-0.8</td><td>-2.0</td><td>-4.2</td><td>0</td></tr></table>

$z \simeq z_0$  and  $z \simeq 2z_0$ , where  $z_0$  is defined in eq. (4.4). We further find an upper bound on the photon survival probability,  $\simeq 1.8\%$ , for the full-polarization region,  $\Pi_L \approx 1$ .

In the energy interval of  $10^{-3} < \omega < 10^{2}\mathrm{GeV}$ , both medium and attenuation effects can become small compared to the ALP-photon mixing term, leading to even simpler analytic results. In this energy range, the propagation mode is predominately the  $D > 0$  mode in most of the parameter space of interest. We further find some distinguishing signatures associated with the ALP mass  $m_{a}$ : If  $m_{a} \simeq 0$ , both  $P_{\gamma \rightarrow \gamma}$  and  $\Pi_L$  are energy-independent; If  $m_{a}$  cannot be neglected, there exist two energy-independent regions separated by an oscillating pattern in the energy spectrum of  $P_{\gamma \rightarrow \gamma}$  and  $\Pi_L$ , which may serve as a novel signature to detect ALPs in the future experiments.

# Acknowledgments

The work is supported in part by the National Natural Science Foundation of China under Grant Nos. 11675002, 11725520, 12147103, 12235001, and 12275128. ZL thank Yonglin Li and Zi-Wei Tang for discussions.

# A Comparison between analytic and numerical calculations

In this section we compare analytic calculations based on a uniform magnetic field assumption, with the numerical calculations using a more realistic consideration of the magnetic field, both in the MW galaxy and in galaxy clusters.

# A.1 MW galaxy

We first discuss the photon propagation in the MW galaxy. We adopt the MW magnetic field model given in refs. [46, 47], in which the magnetic field consists of two components: the regular component and the random component. Following ref. [17], we neglect the random fields in our analysis. For completeness, we present the regular component of the MW magnetic field from refs. [46, 47] in table 2.

We consider a source in the direction of  $(\ell, b) = (180^{\circ}, 0^{\circ})$  (the opposite direction of GC) and with a distance of  $4\mathrm{kpc}$  from Earth. In our analytic calculation we use  $B_0 = 0.98\mu \mathrm{G}$ , which is the average value of the magnitude of the magnetic field along the propagation path. Figure 7 shows the polarization degree and survival probability, computed both in the analytic calculations and in the numerical calculations where the medium effects

![](images/110dd6fd5aec8a258b3dd8b825a0e26485f4fb5b9008857cd46698326531ea17.jpg)  
Figure 7. The polarization degree (left) and survival probability (right) as a function of the photon energy in the MW galaxy. The blue lines are obtained in analytic calculations where the medium effects are neglected and the magnetic field  $B_{0} = 0.98 \mu \mathrm{G}$  is used. The red lines are obtained in numerical calculations where the medium effects  $(\Delta_{x}$  and  $\Delta_{y}$ ) and the MW magnetic field model are used (see main text).

![](images/72599e11b27ea3c26f3d21d972f3e2bad47d144fe40ae4219196e94f80596d1e.jpg)

and the MW magnetic field model are used. The agreements between the analytic and numerical calculations indicate that the analytic calculation with a uniform magnetic field is a good approximation.

# A.2 Galaxy clusters

We next discuss galaxy clusters. To model the complex magnetic field in galaxy clusters, we use the parametrization given in refs. [18, 71]

$$
B _ {\mathrm {c l u}} (z) = B _ {\mathrm {c l u} 0} \left(1 + \frac {z ^ {2}}{r _ {\mathrm {c o r e}} ^ {2}}\right) ^ {- \frac {3}{2} \eta \beta}. \tag {A.1}
$$

For galaxy clusters, we adopt the following parameters:  $B_{\mathrm{clus0}} = 15 \mu \mathrm{G}$ ,  $r_{\mathrm{core}} = 100 \mathrm{kpc}$ ,  $\beta = 2/3$ , and  $\eta = 0.75$  [18]. Following ref. [71], we assume that the direction of the magnetic field is random; hence, we simulate the magnetic field direction by using Monte Carlo method with a step of  $1 \mathrm{kpc}$  along the propagation path. Figure 8 shows the simulated magnetic fields in the  $x-$  (left) and  $y-$  (right) directions in the galaxy cluster as a function of propagation distance  $z$ .

We obtain the mean value of the magnetic field in the galaxy cluster by taking the average of the magnetic field along the propagation path. In our simulation, we obtain  $B_{0} = 0.19 \mu \mathrm{G}$ , which is the average of the magnetic field from  $z = 0$  to  $z = 500 \mathrm{kpc}$ . Figure 9 shows the polarization degree and survival probability, computed both in the analytic calculations and in the numerical calculations where the medium effects are considered and the magnetic field model given in eq. (A.1) is used. We note that although the analytic calculation deviates from the numerical calculation, it describes the behavior qualitatively and provides valuable insights for ALP effects.

![](images/45d7708868b609629bd2999629ad528f269c5d2b19b5a838ee7b9a6422eca03a.jpg)  
Figure 8. Simulated magnetic fields in the  $x$ - (left) and  $y$ - (right) directions in the galaxy cluster as a function of propagation distance  $z$ .

![](images/c0d825f9861d05d91008fa1518ac178272f0be66fb1e8fb4c72434c7b07abc8b.jpg)

![](images/689065cd4c6967e7cba6508a8f2d62d708e60ce58372c18f36397a457f87ec86.jpg)  
Figure 9. The polarization degree (left) and survival probability (right) as a function of the photon energy in the a galaxy cluster. The blue lines are obtained in analytic calculations where the medium effects are neglected and a uniform magnetic field of  $B_{0} = 0.19 \mu \mathrm{G}$  is used. The red lines are obtained in numerical calculations where the medium effects are considered and the magnetic fields shown in figure 8 are used.

![](images/df8d9e61c4ccfe363088cc2fe5a4721aae927ccc7a238051ff5d978764b09ae6.jpg)

# References

[1] A. Ringwald, Exploring the Role of Axions and Other WISPs in the Dark Universe, Phys. Dark Univ. 1 (2012) 116 [arXiv:1210.5081] [INSPIRE].  
[2] I.G. Irastorza and J. Redondo, New experimental approaches in the search for axion-like particles, Prog. Part. Nucl. Phys. 102 (2018) 89 [arXiv:1801.08127] [INSPIRE].  
[3] C.B. Adams et al., Axion Dark Matter, in the proceedings of the Snowmass 2021, Seattle, U.S.A., July 17–26 (2022) [arXiv:2203.14923] [INSPIRE].  
[4] R.D. Peceei and H.R. Quinn, CP Conservation in the Presence of Instantons, Phys. Rev. Lett. 38 (1977) 1440 [INSPIRE].  
[5] F. Wilczek, Problem of Strong  $P$  and  $T$  Invariance in the Presence of Instantons, Phys. Rev. Lett. 40 (1978) 279 [INSPIRE].  
[6] J. Jaeckel and A. Ringwald, The Low-Energy Frontier of Particle Physics, Ann. Rev. Nucl. Part. Sci. 60 (2010) 405 [arXiv:1002.0329] [INSPIRE].

[7] S. Chang, S. Tazawa and M. Yamaguchi, Axion model in extra dimensions with TeV scale gravity, Phys. Rev. D 61 (2000) 084005 [hep-ph/9908515] [INSPIRE].  
[8] N. Turok, Almost Goldstone bosons from extra dimensional gauge theories, Phys. Rev. Lett. 76 (1996) 1015 [hep-ph/9511238] [INSPIRE].  
[9] P. Svrcek and E. Witten, *Axions In String Theory*, JHEP **06** (2006) 051 [hep-th/0605206] [INSPIRE].  
[10] A. Ringwald, From Axions to Other WISPs, in the proceedings of the 4th Patras Workshop on Axions, WIMPs and WISPs, Hamburg, Germany, June 18-21 (2008) [DOI:10.3204/DESY-PROC-2008-02/ringwald_andreas] [arXiv:0810.3106] [INSPIRE].  
[11] A. Arvanitaki et al., String Axiverse, Phys. Rev. D 81 (2010) 123530 [arXiv:0905.4720] [INSPIRE].  
[12] L. Maiani, R. Petronzio and E. Zavattini, Effects of Nearly Massless, Spin Zero Particles on Light Propagation in a Magnetic Field, Phys. Lett. B 175 (1986) 359 [INSPIRE].  
[13] G. Raffelt and L. Stodolsky, Mixing of the Photon with Low Mass Particles, Phys. Rev. D 37 (1988) 1237 [INSPIRE].  
[14] H.-J. Li et al., Limits on axion-like particles from Mrk 421 with 4.5-year period observations by ARGO-YBJ and Fermi-LAT, Phys. Rev. D 103 (2021) 083003 [arXiv:2008.09464] [INSPIRE].  
[15] D. Horns, L. Maccione, A. Mirizzi and M. Roncadelli, Probing axion-like particles with the ultraviolet photon polarization from active galactic nuclei in radio galaxies, Phys. Rev. D 85 (2012) 085021 [arXiv:1203.2184] [INSPIRE].  
[16] R. Gill and J.S. Heyl, Constraining the photon-axion coupling constant with magnetic white dwarfs, Phys. Rev. D 84 (2011) 085001 [arXiv:1105.2083] [INSPIRE].  
[17] X.-J. Bi et al., Axion and dark photon limits from Crab Nebula high energy gamma-rays, Phys. Rev. D 103 (2021) 043018 [arXiv:2002.01796] [INSPIRE].  
[18] G. Galanti, Photon-ALP oscillations inducing modifications to photon polarization, Phys. Rev. D 107 (2023) 043006 [arXiv:2202.11675] [INSPIRE].  
[19] G. Galanti, M. Roncadelli, F. Tavecchio and E. Costa, ALP induced polarization effects on photons from galaxy clusters, Phys. Rev. D 107 (2023) 103007 [arXiv:2202.12286] [INSPIRE].  
[20] Z.-Q. Xia et al., Searching for the possible signal of the photon-axionlike particle oscillation in the combined GeV and TeV spectra of supernova remnants, Phys. Rev. D 100 (2019) 123004 [arXiv:1911.08096] [INSPIRE].  
[21] Y.-F. Liang et al., Constraints on axion-like particle properties with TeV gamma-ray observations of Galactic sources, JCAP 06 (2019) 042 [arXiv:1804.07186] [INSPIRE].  
[22] Y. Grossman, S. Roy and J. Zupan, Effects of initial axion production and photon axion oscillation on type Ia supernova dimming, Phys. Lett. B 543 (2002) 23 [hep-ph/0204216] [INSPIRE].  
[23] C. Csaki, N. Kaloper, M. Peloso and J. Terning, Super GZK photons from photon axion mixing, JCAP 05 (2003) 005 [hep-ph/0302030] [INSPIRE].  
[24] D. Lai and J. Heyl, Probing Axions with Radiation from Magnetic Stars, Phys. Rev. D 74 (2006) 123003 [astro-ph/0609775] [INSPIRE].  
[25] A. De Angelis, M. Roncadelli and O. Mansutti, Evidence for a new light spin-zero boson from cosmological gamma-ray propagation?, Phys. Rev. D 76 (2007) 121301 [arXiv:0707.4312] [INSPIRE].

[26] N. Agarwal, P. Jain, D.W. McKay and J.P. Ralston, *Signatures of Pseudoscalar Photon Mixing in CMB Radiation*, Phys. Rev. D **78** (2008) 085028 [arXiv:0807.4587] [INSPIRE].  
[27] A.K. Ganguly, P. Jain and S. Mandal, Photon and axion oscillation in a magnetized medium: A general treatment, Phys. Rev. D 79 (2009) 115014 [arXiv:0810.4380] [INSPIRE].  
[28] A. Mirizzi and D. Montanino, Stochastic conversions of TeV photons into axion-like particles in extragalactic magnetic fields, JCAP 12 (2009) 004 [arXiv:0911.0015] [INSPIRE].  
[29] C. Wang and D. Lai, Axion-photon Propagation in Magnetized Universe, JCAP 06 (2016) 006 [arXiv:1511.03380] [INSPIRE].  
[30] A. Kartavtsev, G. Raffelt and H. Vogel, Extragalactic photon-ALP conversion at CTA energies, JCAP 01 (2017) 024 [arXiv:1611.04526] [INSPIRE].  
[31] A. De Angelis, G. Galanti and M. Roncadelli, Relevance of axion-like particles for very-high-energy astrophysics, Phys. Rev. D 84 (2011) 105030 [Erratum ibid. 87 (2013) 109903] [arXiv:1106.1132] [INSPIRE].  
[32] G. Galanti and M. Roncadelli, Axion-like Particles Implications for High-Energy Astrophysics, Universe 8 (2022) 253 [arXiv:2205.00940] [INSPIRE].  
[33] S. Vernetto and P. Lipari, Absorption of very high energy gamma rays in the Milky Way, Phys. Rev. D 94 (2016) 063009 [arXiv:1608.01587] [INSPIRE].  
[34] P. Lipari and S. Vernetto, Diffuse Galactic gamma ray flux at very high energy, Phys. Rev. D 98 (2018) 043003 [arXiv:1804.10116] [INSPIRE].  
[35] W. Dittrich and H. Gies, Probing the quantum vacuum. Perturbative effective action approach in quantum electrodynamics and its application, Springer Berlin, Heidelberg (2000) [DOI:10.1007/3-540-45585-X] [INSPIRE].  
[36] J.I. Latorre, P. Pascual and R. Tarrach, Speed of light in nontrivial vacua, Nucl. Phys. B 437 (1995) 60 [hep-th/9408016] [INSPIRE].  
[37] M.V. Cougo-Pinto, C. Farina, F.C. Santos and A. Tort, The speed of light in confined QED vacuum: Faster or slower than  $c$ ?, Phys. Lett. B 446 (1999) 170 [INSPIRE].  
[38] R. Tarrach, Thermal Effects on the Speed of Light, Phys. Lett. B 133 (1983) 259 [INSPIRE].  
[39] S.L. Adler, Photon splitting and photon dispersion in a strong magnetic field, Annals Phys. 67 (1971) 599 [INSPIRE].  
[40] A. Dobrynina, A. Kartavtsev and G. Raffelt, Photon-photon dispersion of TeV gamma rays and its role for photon-ALP conversion, Phys. Rev. D 91 (2015) 083003 [Erratum ibid. 95 (2017) 109905] [arXiv:1412.4777] [INSPIRE].  
[41] A. Kosowsky, Introduction to microwave background polarization, New Astron. Rev. 43 (1999) 157 [astro-ph/9904102] [INSPIRE].  
[42] G.B. Rybicki and A.P. Lightman, Radiative Processes in Astrophysics, Wiley (1979).  
[43] A. McDaniel, T. Jeltema and S. Profumo, Exploring a cosmic-ray origin of the multiwavelength emission in M31, Phys. Rev. D 100 (2019) 023014 [arXiv:1903.06833] [INSPIRE].  
[44] D. Caprioli, Understanding hadronic gamma-ray emission from supernova remnants, JCAP 05 (2011) 026 [arXiv:1103.2624] [INSPIRE].  
[45] D. Caprioli, E. Amato and P. Blasi, The contribution of supernova remnants to the galactic cosmic ray spectrum, Astrophys. 33 (2010) 160 [arXiv:0912.2964] [INSPIRE].

[46] R. Jansson and G.R. Farrar, A New Model of the Galactic Magnetic Field, Astrophys. J. 757 (2012) 14 [arXiv:1204.3662] [INSPIRE].  
[47] R. Jansson and G.R. Farrar, The Galactic Magnetic Field, Astrophys. J. Lett. 761 (2012) L11 [arXiv:1210.7820] [INSPIRE].  
[48] A. Fletcher, E.M. Berkhuijsen, R. Beck and A. Shukurov, The magnetic field of M 31 from multi-wavelength radio polarization observations, *Astron. Astrophys.* **414** (2004) 53 [astro-ph/0310258] [INSPIRE].  
[49] R.E. Pudritz, M.J. Hardcastle and D.C. Gabuzda, Magnetic Fields in Astrophysical Jets: From Launch to Termination, Space Sci. Rev. 169 (2012) 27 [arXiv:1205.2073] [INSPIRE].  
[50] F. Tavecchio et al., TeV BL Lac objects at the dawn of the Fermi era, Mon. Not. Roy. Astron. Soc. 401 (2010) 1570 [arXiv:0909.0651] [INSPIRE].  
[51] F. Govoni and L. Feretti, Magnetic field in clusters of galaxies, Int. J. Mod. Phys. D 13 (2004) 1549 [astro-ph/0410182] [INSPIRE].  
[52] A. Neronov and I. Vovk, Evidence for strong extragalactic magnetic fields from Fermi observations of TeV blazars, Science 328 (2010) 73 [arXiv:1006.3504] [INSPIRE].  
[53] M.S. Pshirkov, P.G. Tinyakov and F.R. Urban, New limits on extragalactic magnetic fields from rotation measures, Phys. Rev. Lett. 116 (2016) 191302 [arXiv:1504.06546] [INSPIRE].  
[54] J. Ma, Q.-H. Peng and Q.-S. Gu, The Thickness of M31, Astrophys. J. Lett. 490 (1997) L51.  
[55] T. Hu, Z. Shao, M. Wang and Q. Peng, Disk thickness and spiral arm structure of M31, New Astron. 23 (2013) 49.  
[56] H. Arp, Spiral structure in m31, Astrophys. J. 139 (1964) 1045.  
[57] A. Ferguson et al., Evidence for stellar substructure in the halo and outer disk of M31, Astron. J. 124 (2002) 1452 [astro-ph/0205530] [INSPIRE].  
[58] R. Beck and R. Wielebinski, Magnetic Fields in the Milky Way and in Galaxies, Springer (2013) [DOI:10.1007/978-94-007-5612-0_13] [arXiv:1302.5663] [INSPIRE].  
[59] D. Leahy, T. Craiciu and J. Postma, The Complex Structure of the Bulge of M31, Astrophys. J. Suppl. 265 (2023) 6 [arXiv:2211.16311] [DOI:10.3847/1538-4365/acae90].  
[60] F. Hammer et al., A 2-3 billion year old major merger paradigm for the andromeda galaxy and its outskirts, Mon. Not. Roy. Astron. Soc. 475 (2018) 2754 [arXiv:1801.04279].  
[61] R. Gießübel and R. Beck, The magnetic field structure of the central region in M 31, Astron. Astrophys. 571 (2014) A61 [arXiv:1408.4582].  
[62] R. Beck, *Cosmic Magnetic Fields: Observations and Prospects*, AIP Conf. Proc. **1381** (2011) 117 [arXiv:1104.3749] [INSPIRE].  
[63] P.P. Kronberg, Extragalactic magnetic fields, Rept. Prog. Phys. 57 (1994) 325 [INSPIRE].  
[64] D. Grasso and H.R. Rubinstein, Magnetic fields in the early universe, Phys. Rept. 348 (2001) 163 [astro-ph/0009061] [INSPIRE].  
[65] G. Galanti, M. Roncadelli and F. Tavecchio, ALP-induced polarization effects on photons from blazars, Phys. Rev. D 108 (2023) 083017 [arXiv:2301.08204] [INSPIRE].  
[66] G. Galanti, Photon-ALP interaction as a measure of initial photon polarization, Phys. Rev. D 105 (2022) 083022 [arXiv:2202.10315] [INSPIRE].

[67] C.-Y. Yang et al., The polarimetric performance of the Compton spectrometer and imager (COSI), in the proceedings of the Space Telescopes and Instrumentation 2018: Ultraviolet to Gamma Ray, (2018) [DOI:10.1117/12.2312556].  
[68] K. Kawata et al., Energy determination of gamma-ray induced air showers observed by an extensive air shower array, Exper. Astron. 44 (2017) 1 [INSPIRE].  
[69] E-ASTROGAM collaboration, The e-ASTROGAM gamma-ray space observatory for the multimeter messenger astronomy of the 2030s, Proc. SPIE Int. Soc. Opt. Eng. 10699 (2018) 106992J [arXiv:1805.06435] [INSPIRE].  
[70] AMEGO TEAM collaboration, AMEGO: Exploring the Extreme Multimessenger Universe, Proc. SPIE Int. Soc. Opt. Eng. 11444 (2020) 1144431 [arXiv:2101.03105] [INSPIRE].  
[71] A. Bonafede et al., The Coma cluster magnetic field from Faraday rotation measures, Astron. Astrophys. 513 (2010) A30 [arXiv:1002.0594] [INSPIRE].