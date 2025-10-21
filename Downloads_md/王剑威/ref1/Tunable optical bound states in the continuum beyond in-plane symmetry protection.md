# Tunable optical bound states in the continuum beyond in-plane symmetry protection

Liangfu Ni, Zhixin Wang, Chao Peng,\* and Zhengbin Li  
State Key Laboratory of Advanced Optical Communication Systems & Networks, Department of Electronics, Peking University, Beijing 100871, China

(Received 7 August 2016; revised manuscript received 12 December 2016; published 30 December 2016)

The formation of tunable bound states in the continuum (BICs) within photonic crystal (PC) slabs has been investigated by using a semianalytical coupled-wave theory framework. An analytic expression of the radiative wave has been derived in order to depict the condition of BICs. As a result, in addition to well-known symmetry-protected BICs, a novel type of vertical-cancellation BIC can be realized through continuously varying a given parameter to eliminate radiative waves at the boundaries. We investigated one-dimensional and two-dimensional (2D) periodic structures, and found that such tunable BICs can occur for a wide range of wave vectors by the selection of appropriate slab thicknesses. For a 2D PC slab, a ring of high- $Q$  modes is predicted and confirmed by numerical simulation.

DOI: 10.1103/PhysRevB.94.245148

# I. INTRODUCTION

Bound states in the continuum (BICs) have attracted much attention since they were first proposed by von Neumann and Wigner [1]. Researchers have expended significant effort to construct BICs by artificially designing quantum potentials; however, owing to the difficulties in manipulating atoms, they cannot be readily realized [2,3]. Alternatively, photonic systems have come to be promising candidates to demonstrate such physical phenomena, according to the analogy between quantum mechanics and electrodynamics [4-9]. In particular, there is great interest in using photonic crystal (PC) slabs [10], the band structures of which are analogous to electronic band structures, to realize BICs [6,8,11-13]. Recently, BICs within PC slabs have been experimentally observed [11,13].

The occurrence of BICs was first interpreted as the interference of resonances in different channels [2]. It is a very general effect in wave physics [14-20]. In PC slabs, the Bloch waves the optical fields of which are well confined within the slab are recognized as "closed channels," whereas the leaky radiative waves are referred to as "open channels" because they transport energy away from the slab. The photonic system thus becomes non-Hermitian. When the radiation is completely canceled by the destructive interference of resonances, anomalously narrow resonances, namely, BICs, occur in the continuum.

It is well known that symmetries play an important role in achieving BICs [11-13,21]. When the structure of the PC slab and the electromagnetic fields possess mirror symmetries, complete destructive interference results in a symmetry-protected BIC at the  $\Gamma$  point. Experimental observations of BICs of this type have been reported [11]. Another type of BIC was observed in PC slabs at some seemingly unremarkable wave vectors without symmetry protection [12,22]. This was attributed to the weighted destructive interference in the vicinity of accidental symmetry of certain off- $\Gamma$  wave vectors [23], and was investigated from the perspective of conserved topological charges [13,24,25]. In this case, symmetries constrain the topological charges as well as their generation, evolution, and annihilation.

Friedrich and Wintgen's early results on the quantum system indicated that, if we have the freedom of varying the separation of two noninterfering resonances as a function of a continuous parameter, the leaky radiative wave can be eliminated for a given parameter value, and thus one of the interfering resonances becomes a BIC state [2,3]. During this process, it is noteworthy that the symmetries are beneficial but not necessary. It has been demonstrated that the occurrence of BICs can be continuously tuned by varying the refractive index of the upper/lower cladding [23]. Owing to their topological nature, this type of BIC robustly appears somewhere in the parameter space. We notice that the occurrence of BICs is actually quite a general and stable phenomenon within PC slabs. Although the primary focus in our previous works was on TM-like modes, BICs can also be found on TE-like bands [13] when the leaky radiative wave is canceled out by continuously varying structural parameters.

In recent years, we developed a coupled-wave theory (CWT) framework to realize accurate and efficient analysis of the detailed wave interaction within the PC slab [26-28]. The framework is capable of analyzing finite [29] or infinite PC slabs with different crystalline geometries and arbitrary tilted sidewalls [27] on both TE- and TM-like modes [30-33]. The CWT depicts the analogous physics of BICs within the photonic system in great detail, as did Friedrich's theory for the quantum system. As a result, CWT provides a comprehensive tool to investigate BICs within a PC slab.

In this paper, we extend the CWT formulation by inducing the  $E_{z}$  component, in order to model the potential TE-TM coupling effect within the TE-like mode. Further, we investigate the cancellation of radiative waves according to vertical geometries, and a closed-form expression is derived. Compared with the topological perspective [13], such an expression provides an explicit and localized indicator to study the conditions of eliminating radiative waves, i.e., realizing BICs, or more specifically, achieving zero amplitude of the radiative waves on the boundaries between the PC slab and upper/lower claddings. The CWT indicates that BICs can be achieved not only in the TM-like mode [23] but also in the TE-like mode, by continuously varying the slab thickness regardless of conventional in-plane symmetry protection. A ring of off-  $\Gamma$  high- $Q$  states has been demonstrated within a

![](images/43ae5d902483b52719c8284510ae65025d9afb191d4de1e89a70e90b00fa6855.jpg)

![](images/2e38e42c0aecd1e0e3caebb10bd363fc36f1a9d9f69a00e82cb4f65b42d2efbf.jpg)

![](images/55dd8f6970c89f1ab5ddb2c9820a77d673487e0e64e2b28b82b6fa950c11639a.jpg)  
FIG. 1. Schematic illustration of a 1D diffraction grating and a 2D PC slab and their band structures. They are both symmetric along the  $z$  axis, normally immersed in air or a certain type of liquid. (a) The 1D diffraction grating consists of dielectric bars that extend infinitely along the  $y$  axis, and are distributed periodically along the  $x$  axis. The filling factor is defined as  $1 - w / a$ . (b) The 2D PC slab is a dielectric slab with circular air holes distributed periodically in a square lattice. The air holes have vertical sidewalls, and the filling factor is defined as  $\pi r^2 / a^2$ , where  $r$  is the radius of the air holes.

![](images/183633f7d0a5fc9cccedca0a9dc11f219e19191eca136b071a2e1cd242d58566.jpg)

two-dimensional (2D) PC slab of a proper thickness, which may be promising to generate tailored beams for PC laser applications [34,35].

The remainder of this paper is organized as follows. In Sec. II, we derive the CWT formulation with the  $E_z$  component. In Sec. III, we present the analytic expression of the radiative wave and discuss the condition to form BICs in a one-dimensional (1D) PC structure, i.e., a diffraction grating. In Sec. IV, we discuss tunable BICs within a 2D PC slab. In Sec. V, we conclude with our findings.

# II. THEORY AND FORMULATION

A PC slab is a dielectric slab with periodic permittivity. For simplicity, we still assume the structure possesses infinite periodicity, and the vertical direction is defined as normal to the slab plane.

A typical 1D diffraction grating and 2D PC slab are shown in Fig. 1. The structural parameters are listed in Table I. Here, the refractive index contrast between the dielectric slab and the cladding is assumed as "low-contrast," and thus the perturbation assumption is valid. For the case of

TABLE I. Structural parameters.  

<table><tr><td>Name</td><td>εa(SiO2)</td><td>εb(Si3N4)</td><td>Filling factor</td></tr><tr><td>1D diffraction grating</td><td>2.1141</td><td>4.0800</td><td>0.1781</td></tr><tr><td>2D PC slab</td><td>2.1141</td><td>4.0800</td><td>0.1781</td></tr></table>

"high-contrast," in which the stronger confinement of optical fields within the slab significantly increases the coupling strength, certain iteration techniques are required to obtain self-consistent results [28,32].

For the TE-like modes we are focusing on, the electric field is given as  $(E_x,E_y,E_z)$ . The  $E_{z}$  component was formerly neglected because of the transverse nature of the TE mode. However, since  $E_{z} = 0$  is rigorously true only at the center cross section when the structure has vertical mirror symmetry, the existence of the  $E_{z}$  component in TE-like mode may cause some potential coupling between TE- and TM-like modes. This is because they share the same radiative wave polarization [23,30]. Hence,  $E_{z}$  is included in the formulation to improve accuracy.

For an infinite  $xy$  plane, the  $E$  field with a Bloch wave vector of  $\beta = (\Delta_x\mathbf{e}_x + \Delta_y\mathbf{e}_y)\beta_0$  is formed as  $E_{i}(\mathbf{r}) = \sum E_{i,mn}(z)e^{-im_{x}\beta_{0}x - in_{x}\beta_{0}y}$ , where  $i$  refers to  $x$ ,  $y$ , or  $z$  and  $m_{x} = m + \Delta_{x}$ ,  $n_{y} = n + \Delta_{y}$ . Meanwhile, within the PC slab  $(|z| < h / 2)$ , permittivity can be expanded as  $\varepsilon (\mathbf{r}) = \sum \varepsilon_{mn}e^{-im\beta_0x - in\beta_0y}$ . In this paper, we elaborate on the major difference incurred by the introduction of  $E_z$  into the formulation. For detailed derivations please refer to our previous works [26,30]. Therefore, the CWT equations become

$$
\begin{array}{l} \left(\frac {d ^ {2}}{d z ^ {2}} + \varepsilon_ {0} k ^ {2} - n _ {y} ^ {2} \beta_ {0} ^ {2}\right) E _ {x, m n} + m _ {x} n _ {y} \beta_ {0} ^ {2} E _ {y, m n} + i m _ {x} \beta_ {0} \frac {d}{d z} E _ {z, m n} \\ = - k ^ {2} \sum_ {m ^ {\prime} \neq m, n ^ {\prime} \neq n} \varepsilon_ {\substack {m - m ^ {\prime} \\ n - n ^ {\prime}}} E _ {x, m ^ {\prime} n ^ {\prime}}, \tag{1} \\ \end{array}
$$

$$
\begin{array}{l} \left(\frac {d ^ {2}}{d z ^ {2}} + \varepsilon_ {0} k ^ {2} - m _ {x} ^ {2} \beta_ {0} ^ {2}\right) E _ {y, m n} + m _ {x} n _ {y} \beta_ {0} ^ {2} E _ {x, m n} + i n _ {y} \beta_ {0} \frac {d}{d z} E _ {z, m n} \\ = - k ^ {2} \sum_ {m ^ {\prime} \neq m, n ^ {\prime} \neq n} \varepsilon_ {\substack {m - m ^ {\prime} \\ n - n ^ {\prime}}} E _ {y, m ^ {\prime} n ^ {\prime}}, \tag{2} \\ \end{array}
$$

$$
\begin{array}{l} \left[ \varepsilon_ {0} k ^ {2} - \left(m _ {x} ^ {2} + n _ {y} ^ {2}\right) \beta_ {0} ^ {2} \right] E _ {z, m n} + i \beta_ {0} \frac {d}{d z} \left(m _ {x} E _ {x, m n} + n _ {y} E _ {y, m n}\right) \\ = - k ^ {2} \sum_ {m ^ {\prime} \neq m, n ^ {\prime} \neq n} \varepsilon_ {\substack {m - m ^ {\prime} \\ n - n ^ {\prime}}} E _ {z, m ^ {\prime} n ^ {\prime}}. \tag{3} \\ \end{array}
$$

For  $m_x^2 +n_y^2 >0$  , rotate the coordinate system:

$$
\binom {E _ {x ^ {\prime}, m n}} {E _ {y ^ {\prime}, m n}} = \binom {\cos \theta} {- \sin \theta} \binom {E _ {x, m n}} {E _ {y, m n}} \tag {4}
$$

where  $\cos \theta = m_x / \sqrt{m_x^2 + n_y^2}$ ,  $\sin \theta = n_y / \sqrt{m_x^2 + n_y^2}$ . For  $m_x^2 + n_y^2 = 0$ , Eq. (4) still holds as long as we let  $\theta = 0$ . Thus, Eqs. (1) and (2) are rearranged as

$$
\begin{array}{l} \left(\frac {d ^ {2}}{d z ^ {2}} + \varepsilon_ {0} k ^ {2}\right) E _ {x ^ {\prime}, m n} + i \beta_ {0} \sqrt {m _ {x} ^ {2} + n _ {y} ^ {2}} \frac {d}{d z} E _ {z, m n} \\ = - k ^ {2} \sum_ {m ^ {\prime} \neq m, n ^ {\prime} \neq n} \varepsilon_ {\substack {m - m ^ {\prime} \\ n - n ^ {\prime}}} E _ {x ^ {\prime}, m ^ {\prime} n ^ {\prime}}, \tag{5} \\ \end{array}
$$

$$
\begin{array}{l} \left[ \frac {d ^ {2}}{d z ^ {2}} + \varepsilon_ {0} k ^ {2} - \left(m _ {x} ^ {2} + n _ {y} ^ {2}\right) \beta_ {0} ^ {2} \right] E _ {y ^ {\prime}, m n} \\ = - k ^ {2} \sum_ {m ^ {\prime} \neq m, n ^ {\prime} \neq n} \varepsilon_ {\substack {m - m ^ {\prime} \\ n - n ^ {\prime}}} E _ {y ^ {\prime}, m ^ {\prime} n ^ {\prime}}. \tag{6} \\ \end{array}
$$

Further, let the right-hand side of Eq. (3) be zero and denote  $\Delta = \sqrt{\Delta_x^2 + \Delta_y^2}$ . Following Eqs. (5), (6), and (3), the zeroth-order radiative waves (denoted as  $E_{i,0}$ ) have the following form:

$$
\begin{array}{l} \left(\frac {d ^ {2}}{d z ^ {2}} + \varepsilon_ {0} k ^ {2}\right) E _ {x ^ {\prime}, 0} + i \Delta \beta_ {0} \frac {d}{d z} E _ {z, 0} \\ = - k ^ {2} \sum_ {m ^ {\prime} \neq 0, n ^ {\prime} \neq 0} \varepsilon_ {\substack {m - m ^ {\prime} \\ n - n ^ {\prime}}} E _ {x ^ {\prime}, m ^ {\prime} n ^ {\prime}}, \tag{7} \\ \end{array}
$$

$$
\begin{array}{l} \left(\frac {d ^ {2}}{d z ^ {2}} + \varepsilon_ {0} k ^ {2} - \Delta^ {2} \beta_ {0} ^ {2}\right) E _ {y ^ {\prime}, 0} \\ = - k ^ {2} \sum_ {m ^ {\prime} \neq 0, n ^ {\prime} \neq 0} \varepsilon_ {\substack {m - m ^ {\prime} \\ n - n ^ {\prime}}} E _ {y ^ {\prime}, m ^ {\prime} n ^ {\prime}}, \tag{8} \\ \end{array}
$$

$$
\left(\varepsilon_ {0} k ^ {2} - \Delta^ {2} \beta_ {0} ^ {2}\right) E _ {z, 0} + i \Delta \beta_ {0} \frac {d}{d z} E _ {x ^ {\prime}, 0} = 0. \tag {9}
$$

By eliminating  $E_{z,0}$  from Eqs. (7) and (9), we obtain

$$
\begin{array}{l} \left(\frac {d ^ {2}}{d z ^ {2}} + \varepsilon_ {0} k ^ {2} - \Delta^ {2} \beta_ {0} ^ {2}\right) E _ {x ^ {\prime}, 0} = \frac {i \Delta \beta_ {0} E _ {z , 0}}{\varepsilon_ {0}} \frac {d \varepsilon_ {0}}{d z} \\ - k ^ {2} \left(1 - \frac {\Delta^ {2} \beta_ {0} ^ {2}}{\varepsilon_ {0} k ^ {2}}\right) \sum_ {m ^ {\prime}, n ^ {\prime} \neq m, n} \varepsilon_ {\substack {m - m ^ {\prime} \\ n - n ^ {\prime}}} E _ {x ^ {\prime}, m ^ {\prime} n ^ {\prime}}. \tag{10} \\ \end{array}
$$

The  $E_z$  terms have been taken into account in the above equations. Otherwise, the operator on the left-hand side of Eq. (10) would be dominated by  $(d^2 / dz^2 + \varepsilon_0 k^2)$  instead of  $(d^2 / dz^2 + \varepsilon_0 k^2 - \Delta^2 \beta_0^2)$ , indicating that the radiative wave is propagating along the  $z$  direction regardless of the in-plane wave vector  $\Delta$ , which is obviously counterintuitive in physics.

Eliminating the energy leakage requires zero amplitude of the radiative wave at the PC slab's boundaries, that is,  $E_{x',y',0}(z)|_{z = \pm h / 2} = 0$ . The first term on the right-hand side of Eq. (10) concerns the derivative of the permittivity  $d\varepsilon_0 / dz$ , which is always zero within the PC slab because we assume the air holes have vertical sidewalls. Only at the boundaries between the PC slab and the upper/lower claddings,  $d\varepsilon_0 / dz$  is nonzero owing to the discontinuous permittivity. However, for the nonradiation case,  $E_{x',0}$  and  $E_{z,0}$ , which represent the transversal and nontransversal parts of the radiative wave, simultaneously approach zero. This result may be confirmed by the finite-difference time-domain (FDTD) simulation [36]. Therefore, the influence of the first term on the right-hand side of Eq. (10) is quite limited and can be neglected as an approximation.

In Eqs. (8) and (10), denoting  $\hat{G} = (d^2 / dz^2 + \varepsilon_0 k^2 - \Delta^2 \beta_0^2)^{-1}$ , the radiative wave can be written as

$$
\begin{array}{l} E_{i^{\prime},0} = -k^{2}\hat{G}\sum_{\substack{m^{\prime}\neq 0,n^{\prime}\neq 0}}\varepsilon_{\substack{-m^{\prime}\\ -n^{\prime}}}E_{i^{\prime},m^{\prime}n^{\prime}} \\ = - k ^ {2} \hat {G} f _ {i ^ {\prime}} (z) \tag {11} \\ \end{array}
$$

where  $i = x, y$ . Notice that  $\varepsilon_{mn}(z)$  is nonzero only within the PC slab, and so are  $f_{x'}(z)$  and  $f_{y'}(z)$ , and hence the radiative wave, though it spans the  $z$  axis, can only be excited within the PC slab. Using Eq. (11), the BIC condition is equivalent to  $\hat{G} f_{x'}(z)|_{z = \pm h / 2} = 0$  and  $\hat{G} f_{y'}(z)|_{z = \pm h / 2} = 0$ .

For a 1D periodic structure, we can obtain similar CWT equations in comparison with the 2D case:

$$
\begin{array}{l} \left[ \frac {d ^ {2}}{d z ^ {2}} + \varepsilon_ {0} k ^ {2} - m _ {x} ^ {2} \beta_ {0} ^ {2} \right] E _ {m} (z) = - k ^ {2} \sum_ {m ^ {\prime} \neq m} \varepsilon_ {m - m ^ {\prime}} E _ {m ^ {\prime}} (z), (12) \\ E _ {0} (z) = - k ^ {2} \hat {G} \sum_ {m ^ {\prime} \neq 0} \varepsilon_ {- m ^ {\prime}} E _ {m ^ {\prime}} (z) = - k ^ {2} \hat {G} f (z). (13) \\ \end{array}
$$

Notice that  $E_{x} \equiv 0$  and  $E_{z} \equiv 0$  for the TE modes in the 1D diffraction grating, and  $E_{m}$  represents the electric field of the  $m$ th-order Bloch wave polarized in the  $y$  direction. To calculate the radiative waves at the boundaries, a proper Green's function with boundary reflection taken into account is required (see Appendix A for details).

As a perturbation method, we choose a set of Bloch waves  $V$  as the basis to depict the wave interaction within the PC slab, which we denote as "basic waves." For the second-order  $\Gamma$  point, the basic waves are given by  $m^2 + n^2 = 1$ . Namely, they are  $[1,0],[-1,0],[0,1],[0,-1]$ -order waves for a 2D PC slab, and  $\pm 1$ -order waves for a 1D diffraction grating. After solving the zeroth-order and high-order waves, the coupling strengths between the basic waves follow the coupling matrix  $\mathbf{C}$  [26], as

$$
k \mathbf {V} = \mathbf {C V} \tag {14}
$$

where  $\mathbf{V} = (R_x, S_x, R_y, S_y)^T$  for a 2D PC slab and  $\mathbf{V} = (R, S)^T$  for a 1D diffraction grating. The complex frequencies  $\omega$  can be obtained from the eigenvalues by solving Eq. (14) as  $\omega = ck$ , and the  $Q$  factors can be calculated as  $\mathrm{Re}(\omega) / 2\mathrm{Im}(\omega)$  accordingly.

# III. CLOSED-FORM RADIATIVE WAVE AND CONDITION OF BICS

# A. Radiative waves and vertical profiles

We start with 1D periodic structure to investigate the tunability of BICs. For such a structure, there exist two band-edge modes, which we refer to as modes A and B as shown in Fig. 1, in the order of increasing frequency. Moreover, the phase-matching condition can be fulfilled at any order of waveguide mode (TE $_0$ , TE $_1$ , ..., and TM $_0$ , TM $_1$ ) on any order of  $\Gamma$  point ( $\beta = n\beta_0$ ). In this paper, we focus on the second-order  $\Gamma$  point and TE-like modes. Typically, mode A is recognized as antisymmetric with respect to the  $x$  direction, and thus the destructive interference makes mode A become a symmetry-protected BIC at the  $\Gamma$  point. Conventionally, mode B is a symmetric and low- $Q$  mode.

For  $\mathrm{TE}_0^A$ ,  $\mathrm{TE}_1^A$ ,  $\mathrm{TE}_2^A$ , i.e., mode A under phase matching with  $\mathrm{TE}_{0\sim 2}$  waveguide modes, their frequencies as functions of varying slab thickness  $h$  are calculated with both CWT and FDTD by assuming off- $\Gamma$  deviation  $\Delta = 0.04$ , as shown in Fig. 2. The mode frequencies and  $Q$  factors obtained from CWT and FDTD agree well with each other. It is well known that symmetry ensures the  $Q$  factor at the  $\Gamma$  point to be infinity [11-13,21,37,38]. However, for a certain off- $\Gamma$  wave vector  $(\Delta = 0.04)$  that does not fulfill the symmetry-protection condition, the  $Q$  factors also quasiperiodically approach infinity for a varying slab thickness, as shown in Fig. 2(b). This indicates that there might be some BIC states occurring at off- $\Gamma$

![](images/09398e23801770a205ed498ea2f18d085421607b5c02f2b8d9b5d12c715d2e5c.jpg)

![](images/41bed825b03384846a4a77ee6fda7dbcb366acc1cbd3948b77ec88ad699ed887.jpg)

![](images/3965a3b4832c9c51b8c709f791bec61239f006d477ced19dd390aadca6c2bb6d.jpg)  
FIG. 2. (a) Mode frequency and (b)  $Q$  factor versus varying slab thickness, for mode  $\mathrm{TE}_{0\sim 2}^{A}$  in 1D diffraction grating structure at off-  $\Gamma$  deviation  $\Delta = 0.04$ , calculated by CWT (solid lines) and FDTD (circles). (c) Vertical profiles of Bloch wave  $m = \pm 1$  and radiative waves  $(m = 0)$  for mode  $\mathrm{TE}_0^A$  at the first slab thickness, where the  $Q$  factor approaches infinity [red box in (b)], with  $h = 1.1696$  given by CWT and  $h = 1.1564$  given by FDTD. Vertical profiles are normalized to slab thickness  $h$ .

points, and the underlying physics is beyond conventional in-plane symmetry protection.

We also calculate the vertical profiles of the electric field for the mode  $\mathrm{TE}_0^A$ , at the slab thickness for which the first BIC occurs, as illustrated in Fig. 2(c). It is noticed that the amplitude of the radiative wave approaches zero at the boundaries, resulting in no energy leakage out of the slab and forming a BIC state at the off- $\Gamma$  point.

# B. Analytic conditions of BICs

Tunable BICs can be realized by continuously scanning various parameters, including slab thickness, filling factor, dielectric constants, lattice geometry, among others, as long as the boundary condition  $E_0(z)|_{z = \pm h / 2} = 0$  is satisfied. For

simplicity, we focus on slab thickness  $(h)$  as a parameter to fulfill the BIC condition. Equation (13) shows that  $E_0$  is excited by other Bloch waves, that is,  $E_0(z) = -k^2\hat{G}f(z)$ . We rewrite the source function  $f(z)$  as

$$
f (z) = \sum_ {m ^ {\prime} \neq 0} \varepsilon_ {- m ^ {\prime}} E _ {m ^ {\prime}} (z). \tag {15}
$$

As Eq. (15) shows,  $f(z)$  is a linear combination of the vertical profiles of all Bloch waves except for the zeroth order.  $f(z)$  physically represents the source that excites the zeroth-order Bloch wave. For simplicity, we assume in this paper that the zeroth-order wave is the only radiative wave, namely, the only "open channel." Thus the BIC condition is equivalent to  $E_0(z)|_{z = \pm h / 2} = 0$ , or  $\hat{G} f(z)|_{z = \pm h / 2}$ .

A conventional symmetry-protected BIC requires  $f(z) \equiv 0$  and  $E_0(z) \equiv 0$ . For instance, the BIC occurs at the  $\Gamma$  point when  $\varepsilon$  is symmetric and  $E$  is antisymmetric along the  $x$  axis, and the radiative wave is canceled out due to such inplane symmetry. For a 2D PC slab, BICs occurring at off-  $\Gamma$  points have been reported [12], in which the radiative wave cancellation may be achieved by certain accidental symmetries [23].

However, the in-plane symmetry of the electromagnetic field is not necessary for  $\hat{G} f(z)|_{z = \pm h / 2} = 0$ . We denote the vertical-cancellation BIC condition as  $\hat{G} f(z)|_{z = \pm h / 2} = 0$ . Such a condition can still be realized when in-plane symmetry of the electromagnetic field is absent. For a certain in-plane propagation constant  $\Delta$ , it can be satisfied by varying  $h$ . Taking the Green's function presented in Appendix A, a more specific form of  $\hat{G} f(z)|_{z = h / 2}$  can be written as (for the  $z = -h / 2$  boundary, the condition is the same since the geometry possesses vertical symmetry)

$$
\begin{array}{l} \hat {G} f (z) | _ {z = h / 2} = \frac {i t e ^ {- i \beta_ {r} h}}{2 \beta_ {r} \left(1 - r ^ {2} e ^ {- 2 i \beta_ {r} h}\right)} \int_ {- h / 2} ^ {h / 2} \left[ e ^ {i \beta_ {r} (h / 2 + z)} \right. \\ \left. + r e ^ {- i \beta_ {r} (h / 2 + z)} \right] f (z) d z \tag {16} \\ \end{array}
$$

where  $r$  and  $t$  represent the reflection and transmission coefficient at the boundary, respectively, and  $\beta_r$  is the vertical wave vector of the radiative wave within the PC slab. From Eq. (16), we define  $I_0$  as

$$
I _ {0} = \int_ {- h / 2} ^ {h / 2} e ^ {i \beta_ {r} z} f (z) d z. \tag {17}
$$

As shown in Appendix B,  $I_0$  can be chosen as real, and  $I_0 = 0$  is equivalent to  $\hat{G} f(z)|_{z=h/2} = 0$ . For a system without symmetry protection,  $I_0$  can be regarded as an indicator for vertical-cancellation BICs. For a 1D diffraction grating, the  $I_0$  of mode  $\mathrm{TE}_0^A$  obtained by varying  $h$  at the off-  $\Gamma$  deviation  $\Delta = 0.04$  is presented in Fig. 3(a).  $I_0$  crosses zero periodically, which leads to  $E_0|_{z=\pm h/2} = 0$ , and forms of BIC.

The physical interpretation for  $I_0$  is the coherent superposition of the zeroth-order Bloch wave excited by other Bloch waves at the PC boundary.  $I_0 = 0$  means that the waves interfere destructively, and do not permit radiative energy. The phenomenon of  $I_0 = 0$  is different from symmetry-protected BICs, because it does not require the in-plane wave vector to be zero, which guarantees  $\varepsilon_{-m}E_m = \varepsilon_mE_{-m}$  for any  $m$ th-order Bloch wave.

![](images/6c3e2dbaa3157497ceea4b8f84e5312fb07152959289bd407105ee3722d31f7f.jpg)

![](images/86bd8ae894c6991e14a4d5a6d3aa14f96854c3a9994303d28197ae3c573042d6.jpg)  
FIG. 3. (a)  $Q$  factor,  $|E_0|_{z=h/2}|^2$ , and  $I_0$  vs slab thickness  $h$  for mode  $\mathrm{TE}_0^A$  in a 1D diffraction grating at the off-  $\Gamma$  deviation  $\Delta = 0.04$ .  $E_0|_{z=h/2}$  is the electric field of the zeroth-order radiative wave at the PC slab upper boundary.  $I_0$  is calculated analytically by using Eq. (17) and numerically by the FDTD simulation, while  $I_0^g$  is obtained using Eq. (19). The vertical dashed lines indicate BICs. (b) The required slab thickness to achieve BICs at given wave vectors in a 1D diffraction grating, for modes  $\mathrm{TE}_0^A$  and  $\mathrm{TE}_0^B$ . The first, second, and third zero points on the radiative waves  $(|E_0|_{z=h/2}|^2)$  are presented.

It is noteworthy that the phenomenon of  $I_0 = 0$  is also different from the Fabry-Perot (FP) effect, which is caused by the interference of multiple light reflections on two reflecting surfaces. The phenomenon of  $I_0 = 0$  is actually due to the interference of radiative waves excited by multiple transverse Bloch waves. Unlike the FP effect, the free spectral range of which is exactly periodic, the periodicity of  $I_0 = 0$  with slab thickness is not exactly the same. Moreover, there is no

constraint of the reflection coefficient to achieve  $I_0 = 0$ , which can be sufficiently low whereas the BIC still survives.

For a better understanding of  $I_0$  varying with  $h$ , we adopt some approximations to further simplify the expression. Within the PC slab, energy is dominated by basic waves. In the case of a 1D diffraction grating, they occupy  $99.98\%$  of the whole energy. The contribution of high-order waves can be neglected, owing to their trivial amplitudes, and basic waves are assumed to share an identical profile  $\Theta_0$  to that of the guide mode. Therefore,  $f(z)$  can be simplified as  $(\varepsilon_{-1}A_{1} + \varepsilon_{1}A_{-1})\Theta_{0,\mathrm{PC}}(z)$ , where  $A_{m}$  represents the amplitude of the  $m$ th-order wave,  $m \in \{1, -1\}$ , and  $I_0$  is obtained as

$$
I _ {0} \approx \left(\varepsilon_ {1} A _ {- 1} + \varepsilon_ {- 1} A _ {1}\right) I _ {0} ^ {g} \tag {18}
$$

where  $I_0^g$  is

$$
I _ {0} ^ {g} = \int_ {- h / 2} ^ {h / 2} e ^ {i \beta_ {r} z} \Theta_ {0, \mathrm {P C}} (z) d z. \tag {19}
$$

The guide-mode profile  $\Theta_0$  is sinusoidal within the PC slab, and decays exponentially in the cladding. Within the PC slab,  $\Theta_0$  can be either  $\cos (\beta z)$  or  $\sin (\beta z)$ , corresponding to even or odd modes, respectively, where  $\beta$  is the propagation constant of the guide mode along the  $z$  axis. Therefore, taking  $\Theta_0 = \cos (\beta z)$  and  $\Theta_0 = i\sin (\beta z)$  into Eq. (19),  $I_0^g$  is rewritten as a closed-form expression:

$$
I _ {0} ^ {g} = \frac {h \sqrt {\kappa^ {2} \cos^ {2} u + \sin^ {2} u}}{u \left(\kappa^ {2} - 1\right)} \sin \left(\kappa u - \arctan \frac {\tan u}{\kappa}\right), \tag {20}
$$

$$
I _ {0} ^ {g} = \frac {h \sqrt {\kappa^ {2} \cos^ {2} u + \sin^ {2} u}}{u \left(\kappa^ {2} - 1\right)} \cos \left(\kappa u + \arctan \frac {\cot u}{\kappa}\right) \tag {21}
$$

where  $\kappa = \beta_r / \beta$  and  $u = \beta h / 2$ .

Using  $\beta_r = [\varepsilon_0k^2 -\Delta^2\beta_0^2 ]^{1 / 2}$  (Appendix A) and  $\beta = (\varepsilon_0k^2 -\beta_0^2)^{1 / 2}$  (Appendix C), we have  $\kappa u = \beta_rh / 2 = [u^2 +$ $(1 - \Delta^{2})\beta_{0}^{2}h^{2} / 4]^{1 / 2}$ . As discussed in Appendix C,  $u$  increases monotonically with  $h$ , and as a result,  $\kappa u$  increases monotonically with  $h$ . Moreover, the value of  $[\arctan (\tan u / \kappa)]$  and  $[\arctan (\cot u / \kappa)]$  is between zero and  $\pi /2$ . Therefore, with increasing  $h$ , the phase in sin or cos goes all the way up to infinity, indicating that there are infinite strict zero points for  $I_0^g$  in both equations.

$I_0^g$  provides a simple and analytic form of  $I_0$  based on the assumption that basic waves are dominant. As shown in Fig. 3(a),  $I_0^g$  and  $I_0$  agree well with each other, which confirms the accuracy of  $I_0^g$  under moderate perturbation.

# C. Results and discussion

A comparison between the CWT and FDTD results clearly validates the physics and theory mentioned above. Taking the mode  $\mathrm{TE}_0^A$  of a 1D periodic structure as an example, the  $Q$  factor, electric field on the boundary  $|E_0|_{z=h/2}|^2$ , and  $I_0$  under varying slab thickness  $h$  are illustrated in Fig. 3(a). Apparently, the  $Q$  factor quasiperiodically becomes infinitely high, although the period is not absolutely constant.  $E_0$  varies consistently with the  $Q$  factor, sharing the same zero points with respect to slab thickness. When the  $Q$  factor approaches infinity or  $|E_0|^2$  reaches zero,  $I_0$  equals zero as well. Therefore, the derived analytic expression for  $I_0$  is an effective indicator

to depict the physical nature of BICs, and  $I_0 = 0$  can be used as a criterion for the appearance of vertical-cancellation BICs.

Furthermore, the slab thickness  $h$  that supports BICs under a varying  $k_{x}$  is illustrated in Fig. 3(b), representing modes of  $\mathrm{TE}_0^A$  and  $\mathrm{TE}_0^B$ , respectively. This result is obtained by both CWT and FDTD, confirming the high reliability of our CWT calculation. It is noteworthy that, although the mode  $\mathrm{TE}_0^B$  is conventionally a low-  $Q$  mode at the  $\Gamma$  point owing to its in-plane symmetry, it can become a BIC at a proper slab thickness that fulfills the vertical-cancellation BIC condition.

The calculation of  $I_0^g$  above has assumed that  $f(z) \approx (\varepsilon_{-1}A_1 + \varepsilon_1A_{-1})\Theta_{0,\mathrm{PC}}(z)$ , where  $\Theta_0 = \cos \beta z$  or  $\Theta_0 = i\sin \beta z$ . In fact, perturbations from high-order waves may affect  $I_0$ , especially for high-contrast structures. However, as discussed in Appendix B,  $I_0$  can be chosen as real, and  $I_0 = 0$  is equivalent to  $E_0|_{z = \pm h / 2} = 0$  as long as the structure is symmetric along the  $z$  axis. As an approximation of  $I_0$ ,  $I_0^g$ , depicted in Fig. 3(a), retains high accuracy by assuming basic waves are dominant. It is noteworthy that the energy concentration ratios of the basic waves to the whole mode energy are 0.9998 and 0.9929 for a 1D diffraction grating and a 2D PC slab, respectively, which strongly supports the basis of the CWT analysis, that the dominance of basic waves is valid.

# IV. TUNABLE BICS WITHIN A TWO-DIMENSIONAL PHOTONIC CRYSTAL SLAB

BICs within a 2D PC slab are more sophisticated because they require destructive interference in two polarized directions. As discussed above, the symmetry-protected and vertical-cancellation conditions can suppress radiative waves independently and simultaneously. For a 2D PC slab, the vertical-cancellation BIC condition can be mathematically described as  $\hat{G} f_{x'}(z)|_{z=h/2} = 0$  and  $\hat{G} f_{y'}(z)|_{z=h/2} = 0$ . Neglecting high-order waves, we have

$$
f _ {x ^ {\prime}} (z) \approx \sum_ {m, n} \varepsilon_ {- n} A _ {x ^ {\prime}, m n} \Theta_ {0, m n} (z), \tag {22}
$$

$$
f _ {y ^ {\prime}} (z) \approx \sum_ {m, n} \varepsilon_ {- m} A _ {y ^ {\prime}, m n} \Theta_ {0, m n} (z) \tag {23}
$$

where  $(m,n)\in \{(1,0),(0,1),(-1,0),(0, - 1)\}$ $\Theta_{0,mn}$  are the vertical profiles of the four basic waves, and  $A_{x^{\prime},mn}$  and  $A_{y^{\prime},mn}$  are the projections of the amplitudes of basic waves onto the  $x^{\prime}$  and  $y^\prime$  axes, respectively.

$\Theta_{0,mn}$  of four individual basic waves are usually different at an arbitrary wave vector in reciprocal-lattice space. As a result,  $\hat{G} f_{x'}(z)|_{z = h / 2} = 0$  and  $\hat{G} f_{y'}(z)|_{z = h / 2} = 0$  cannot hold simultaneously in general, since  $f_{x'}(z)$  and  $f_{y'}(z)$  are different depending on the wave vector. That is, one continuously varying parameter (slab thickness  $h$ ) can only support the vertical-cancellation condition in one direction. To form BICs in a 2D PC slab, either of the symmetry-protected and vertical-cancellation conditions can be individually fulfilled in either of two orthogonal directions.

A symmetry analysis is presented in Fig. 4, in which the eigenvectors of mode A, B, C, and D, at three wave vectors (at  $\Gamma$ , on  $\Gamma - X$ , and on  $\Gamma - M$ ) are illustrated. Since in-plane geometric symmetries are assumed, we have  $\varepsilon_{0,\pm 1} = \varepsilon_{\pm 1,0}$

![](images/7b70d19a82a0d622d6da7b121a8381e5f72aeac96f439c9cccf550b89873b547.jpg)  
FIG. 4. Symmetry analysis for modes in a 2D PC slab. Three  $k$  points (at  $\Gamma$ , on  $\Gamma - X$ , and on  $\Gamma - M$ ) are each presented for modes A, B, C, and D. The blue arrows indicate the wave vectors of the basic waves, while the arrows normal to them indicate their amplitude. The coupling coefficients from the basic waves to the radiative wave are identical, owing to the geometric symmetry. Therefore, the vector sum of the magnitude arrows determines the amplitude of the radiative wave. The dashed box indicates conventional symmetry-protected BICs at the  $\Gamma$  point, whereas the others are tunable BICs based on both symmetry protection and vertical cancellation.

and the overall radiative wave can be represented by the vector sum of  $\mathbf{A}_{mn}\Theta_{0,mn}(z)$ , where  $\mathbf{A}_{mn} = A_{x'}\mathbf{e}_{x'} + A_{y'}\mathbf{e}_{y'}$ . The dashed box shows the conventional symmetry-protected BICs at the  $\Gamma$  point, in which the radiative waves in both the  $x,y$  directions are eliminated owing to symmetry. In addition, the other cases show that the radiative waves can be canceled out due to symmetry protection in one direction and vertical cancellation in the other direction. For wave vectors on  $\Gamma - X$  and  $\Gamma - M$  in the reciprocal-lattice space, the in-plane symmetry ensures that the basic waves have identical vertical profiles as well as amplitudes with respect to the symmetric axis. Taking mode A on the  $\Gamma - X$  direction, for example (in Fig. 4), the in-plane symmetry leads to  $E_{x,0} = 0$  and leaves  $E_{y,0} = -k^2\hat{G}f_y$ . According to the discussion above, we can find a proper slab thickness  $h$  to fulfill the vertical-cancellation condition, and hence,  $-k^2\hat{G}f_y|_{z = \pm h / 2} = 0$ . As a result, the radiative wave was completely eliminated to form a BIC state. A similar principle can be applied to both the  $\Gamma - X$  and  $\Gamma - M$  directions and mode  $A \sim D$ . Interestingly, the conventional low- $Q$  modes, C and D, can also become BICs under the vertical-cancellation condition.

The  $Q$  factor, electric field on the boundary  $|E_s|^2$ ,  $|E_p|^2$ , and  $I_0$  under varying slab thickness  $h$  are illustrated in Fig. 5 for the  $\mathrm{TE}_0^A$  mode of a 2D PC slab at  $k_x = 0.20, k_y = 0.00$  on the  $\Gamma - X$  direction,  $k_x = 0.20, k_y = 0.20$  on  $\Gamma - M$ , and arbitrary direction  $k_x = 0.20, k_y = 0.10$ , with respect to two polarizations, as shown in Fig. 1. Apparently, for a wave vector

![](images/7023f105426ba14dfb9109aaf0a6eceb6623a39b21436762ed6a77d9a781e785.jpg)  
FIG. 5.  $Q$  factor, electric field  $(|E_s|_{z = h / 2}|^2$  and  $|E_p|_{z = h / 2}|^2)$ , and  $I_0$  versus slab thickness  $h$ , for mode  $\mathrm{TE}_0^A$  within a 2D PC slab, at reciprocal-lattice vector  $k_x,k_y = (0.20,0.00),(0.20,0.20),(0.20,0.10)$ , calculated by CWT (solid lines) and FDTD (circles).  $E_{s}|_{z = h / 2}$  and  $E_{p}|_{z = h / 2}$  are the radiative waves with  $s$  and  $p$  polarizations at the PC slab upper boundary, where directions  $s$  and  $p$  are defined in Fig. 1.  $I_{0i'} = \int_{-h / 2}^{h / 2}e^{i\beta_r z}f_{i'}(z)dz$ , where  $i'$  represents  $x'$  or  $y'$ . The vertical dashed lines indicate BICs.

![](images/d22f5639d29b55aacd91f21cf1a6225adc79010a92a2c5ceb4d37a0af4cc45a1.jpg)

![](images/89f8b15a218802f46f9f99a3b1f055ba6665e4ceb8fc7c687ccf967118773520.jpg)

along  $\Gamma - X$  and  $\Gamma - M$ , the radiative wave in one direction is always zero (red line) due to the in-plane symmetry, whereas the radiative wave in the orthogonal direction periodically reaches zero with respect to the varying slab thickness (blue line). According to the analysis above, along the  $\Gamma - X$  and  $\Gamma - M$  directions, BICs can be rigorously constructed.

As mentioned above, the vertical-cancellation condition  $\hat{G} f_{x'}(z)|_{z=h/2}=0$  and  $\hat{G} f_{y'}(z)|_{z=h/2}=0$  cannot hold simultaneously, since one continuously varying parameter (slab thickness  $h$ ) cannot support the vertical-cancellation condition in both directions. Therefore, BICs cannot be rigorously achieved for an arbitrary in-plane wave vector without symmetry protection. However, notice that the basic waves occupy more than  $99\%$  of the whole energy in a 2D PC slab, and  $\Theta_{0,mn}$  of the four basic waves are only slightly different. As a result,  $f_{x'}(z)$  and  $f_{y'}(z)$  are almost degenerate and the zero points of  $I_{0,x'}$  and  $I_{0,y'}$  are quite close.

As the results of  $k_{x} = 0.20, k_{y} = 0.10$  in Fig. 5 show, the red and blue lines of  $|E_0|_{z=h/2}|^2$  and  $I_0$  vary accordingly with respect to the slab thickness, because the  $k_{x} = 0.20, k_{y} = 0.10$  direction is beyond symmetry protection. However, the vertical cancellation in two orthogonal directions occurs at nearly degenerate zero points, indicating that a high- $Q$  mode (although not a rigorous BIC) can be realized.

We calculate the  $Q$  factors of  $\mathrm{TE}_0^A$  for the wave vector  $k_{x}, k_{y} \in [\pi / a, -\pi / a]$ , with slab thickness  $h = 1.50a$  by both FDTD and CWT, as shown in Fig. 6. Here,  $Q_p$  and  $Q_s$  are defined as the  $Q$  factors corresponding to the electric components  $E_p$  and  $E_s$ , as illustrated in Fig. 1. Owing to

the quasidegeneracy of the zero points of  $I_{0,x'}$  and  $I_{0,y'}$ , a ring of high- $Q$  modes appears in the reciprocal-lattice space, which may be promising for photonic crystal surface emitting lasers to generate tailored vector beams [21,35]. The shape of this ring is almost the same as the interception of the plane  $\omega = \omega_0$  with the 2D band structure  $\omega(k_x, k_y)$ ; therefore, the modes lying on the ring have close frequencies. This  $\omega_0$  makes the basic

![](images/172bd92c09e3d19864de2d14a921b93c853ca1645b542541f26f9aa455b61ec4.jpg)  
FIG. 6.  $Q$  factor distribution in reciprocal-lattice space for mode  $\mathrm{TE}_0^A$  within a 2D PC slab of slab thickness  $h = 1.50$ .  $Q$  is the overall  $Q$  factor whereas  $Q_{s}$  and  $Q_{p}$  are calculated according to the radiative waves  $E_{s}$  or  $E_{p}$ , respectively, where  $s$  and  $p$  are defined in Fig. 1. A ring of high-  $Q$  modes is predicted and confirmed by FDTD, among which rigorous BICs marked by small circles lie on high-symmetric directions.

wave profile  $\Theta_{0,mn}(z)$  close to identical, and hence benefits the degeneracy of  $f_{x'}(z)$  and  $f_{y'}(z)$  to form a ring of high- $Q$  modes. The ring will expand or shrink according to different slab thickness. Strictly speaking, at the  $\Gamma$  point as well as along the  $\Gamma-X$  and  $\Gamma-M$  directions, BICs can be rigorously constructed.

It is noteworthy that the occurrence of BICs has also been explained by topological singularities in far-field polarization [13]. At the singularities where there is no way to assign a far-field polarization that is consistent with the neighboring wave vector, the radiative wave achieves zero amplitude, which is the same principle as our CWT derivation. The topological perspective provides an overall picture to identify whether the BICs exist in a given set of structural parameters, by numerically calculating the radiative wave within the 2D Brillouin zone. Actually, one can perform a similar calculation more efficiently by using the analytic expression of the radiative wave given by the CWT. The indicator  $I_0$  derived in this paper is more like a "localized" indicator at a given  $k$  point, to find out how much divergence there is from the BIC condition in a set of parameters (filling factor, slab thickness, etc.), without scanning the whole Brillouin zone. We believe this feature is promising for finding BICs in the system over a wide range of parameters.

# V. CONCLUSION

In this paper, we presented an investigation of the formation of BICs within PC slabs, based on a semianalytical CWT framework for TE-like modes in both a 1D diffraction grating and 2D PC slab. We first improved the CWT model by taking  $E_{z}$  into account, and then derived an analytic expression to depict the condition of BICs, i.e., the amplitude of the radiative wave being zero at the upper and lower PC boundaries.

According to the analytic expression of radiation, there are two different ways to realize BICs. One is by utilizing in-plane symmetry to completely cancel out the radiative wave within the whole space, which is well known as symmetry-protected BICs. The other way is by continuously varying a given parameter (for instance, slab thickness) to eliminate the radiative wave at boundaries, which we refer to as vertical-cancellation BICs.

For 1D diffraction gratings, a criterion to indicate vertical-cancellation  $I_0$  has been proposed. We proved that  $I_0$  can be chosen as real, and has infinite zero points to support BICs. Such a condition does not require the electromagnetic field to possess any in-plane symmetries. As a result, by continuously varying structural parameters, either conventional in-plane antisymmetric modes or symmetric modes can become BICs at either the  $\Gamma$  point or an off-  $\Gamma$  wave vector. The structural parameter could be the slab thickness, filling factor, or dielectric constant.

The formation of BICs becomes more sophisticated for a 2D PC slab because it requires the radiative waves to be eliminated in two polarized directions. We found that either of the symmetry-protected and vertical-cancellation conditions can be individually fulfilled in either of two orthogonal directions. Along some directions in reciprocal-lattice space ( $\Gamma$  point,  $\Gamma - X$  direction, and  $\Gamma - M$  direction), symmetry protection cancels out the radiative wave in one polarization, and vertical

cancellation eliminates the other polarization via a varying slab thickness. As a result, along these directions, BICs can be rigorously constructed. For an arbitrary wave vector, one varying parameter, such as the slab thickness, usually cannot support vertical cancellation in two directions when symmetry protection is absent. However, owing to the quasidegenerate nature of the zero points of  $I_{0x'}$  and  $I_{0y'}$ , a ring of high- $Q$  modes can still be found in reciprocal-lattice space for a proper slab thickness.

The analytic expression of the radiative wave presents an effective interpretation of the formation of tunable BICs. It indicates that photonic BIC states are actually quite general phenomena within a PC slab, which can occur for both TE-like and TM-like modes at a wide range of reciprocal lattice vectors, by continuously varying structural parameters. Tunable BICs provide a novel way of trapping light and can be essentially important.

# ACKNOWLEDGMENTS

This paper was supported by the National Natural Science Foundation of China under Grants No. 61320106001, No. 61307089, and No. 61575002 and the State Key Laboratory of Advanced Optical Communication Systems and Networks, China.

# APPENDIX A: THE GREEN'S FUNCTION

In this paper, we only derive the solution of a three-layered structure. For a multilayered structure, the Green's function can be derived similarly but in a matrix form, as elaborated in our previous work [27].

We assume the source is located at the origin, and  $z_{1}$  and  $z_{2}$  are the coordinates of the boundaries,  $z_{1} \leqslant 0$  and  $z_{2} \geqslant 0$ . The Green's function satisfies

$$
\left[ \frac {\partial^ {2}}{\partial z ^ {2}} + \beta_ {z} ^ {2} (z) \right] G (z) = \delta (z) \tag {A1}
$$

where  $\beta_{z}(z) = [\varepsilon_{0}(z)k^{2} - m_{x}^{2}\beta_{0}^{2}]^{1 / 2}$ . Particularly, the vertical wave vector of the zeroth-order Bloch wave inside the PC slab has the form  $\beta_{r} = [\varepsilon_{0}k^{2} - \Delta^{2}\beta_{0}^{2}]^{1 / 2}$ .

If  $\beta_{z} = \beta_{z}(z)|_{\mathrm{PC}}$ , and  $r_1$  and  $r_2$  are the reflection coefficients of the boundaries, the Green's function can be expressed as

$$
G _ {+} (z) = A _ {2} e ^ {- i \beta_ {z} z} + B _ {2} e ^ {i \beta_ {z} z} = A _ {2} e ^ {- i \beta_ {z} z} + r _ {2} A _ {2} e ^ {- 2 i \beta_ {z} h _ {2}} e ^ {i \beta_ {z} z}, \tag {A2}
$$

$$
G _ {-} (z) = A _ {1} e ^ {i \beta_ {z} z} + B _ {1} e ^ {- i \beta_ {z} z} = A _ {1} e ^ {i \beta_ {z} z} + r _ {1} A _ {1} e ^ {- 2 i \beta_ {z} h _ {1}} e ^ {- i \beta_ {z} z} \tag {A3}
$$

where  $G_{-}$  and  $G_{+}$  refer to the Green's function for  $z \in [z_1,0]$  and  $z \in [0,z_2]$ , respectively, and  $h_1 = -z_1$ ,  $h_2 = z_2$ . According to the boundary conditions  $G_{+}(0) = G_{-}(0)$  and  $G_{+}'(0) - G_{-}'(0) = 1$ , we obtain

$$
A _ {1} = \frac {i}{2 \beta_ {z}} \frac {1 + r _ {2} e ^ {- 2 i \beta_ {z} h _ {2}}}{1 - r _ {1} r _ {2} e ^ {- 2 i \beta_ {z} h}}, \tag {A4}
$$

$$
A _ {2} = \frac {i}{2 \beta_ {z}} \frac {1 + r _ {1} e ^ {- 2 i \beta_ {z} h _ {1}}}{1 - r _ {1} r _ {2} e ^ {- 2 i \beta_ {z} h}} \tag {A5}
$$

where  $h = z_2 - z_1$ . Moreover, the amplitudes for the Green's function outside the PC slab,  $C_1$  and  $C_2$ , have the following expressions:

$$
C _ {1} = t _ {1} A _ {1} e ^ {- i \beta_ {z} h _ {1}}, \tag {A6}
$$

$$
C _ {2} = t _ {2} A _ {2} e ^ {- i \beta_ {z} h _ {2}} \tag {A7}
$$

where  $t_1 = 1 + r_1$  and  $t_2 = 1 + r_2$ .

When applied to a more general situation in which the source is located at an arbitrary point  $z'$ , the Green's function can be obtained by making the substitution  $z \to z - z'$ ,  $h_1 = z' - z_1$ ,  $h_2 = z_2 - z'$ ,  $h = z_2 - z_1$  in Eqs. (A2)-(A7).

# APPENDIX B: DISCUSSION OF  $I_0$

We first present the proof that  $I_0 = 0$  is equivalent to  $\hat{G} f(z)|_{z=h/2} = 0$ . Since the geometry of the PC structure is symmetric along the vertical direction,  $f(z)$  is either even symmetric or odd symmetric in the  $z$  direction. If  $f(z)$  is an even function, then

$$
I _ {0} = \int_ {- h / 2} ^ {h / 2} e ^ {i \beta_ {r} z} f (z) = \int_ {- h / 2} ^ {h / 2} \cos (\beta_ {r} z) f (z). \tag {B1}
$$

The first and second terms of the integral in Eq. (16) can be obtained:

$$
I _ {1} = e ^ {i \beta_ {r} h / 2} \int_ {- h / 2} ^ {h / 2} e ^ {i \beta_ {r} z} f (z) = e ^ {i \beta_ {r} h / 2} I _ {0}, \tag {B2}
$$

$$
\begin{array}{l} I _ {2} = r e ^ {- i \beta_ {r} h / 2} \int_ {- h / 2} ^ {h / 2} e ^ {- i \beta_ {r} z} f (z) d z \\ = \int_ {- h / 2} ^ {h / 2} \cos \left(\beta_ {r} z\right) f (z) = r e ^ {- i \beta_ {r} h / 2} I _ {0}. \tag {B3} \\ \end{array}
$$

Similarly, if  $f(z)$  is an odd function, then

$$
I _ {0} = \int_ {- h / 2} ^ {h / 2} e ^ {i \beta_ {r} z} f (z) = i \int_ {- h / 2} ^ {h / 2} \sin (\beta_ {r} z) f (z). \tag {B4}
$$

Moreover, the first and second terms of the integral in Eq. (16) can be calculated in a similar manner. As a result, Eq. (16) is rearranged as follows:

$$
\hat {G} f (z) | _ {z = h / 2} = \frac {i t}{2 \beta_ {r} \left(e ^ {i \beta_ {r} h / 2} \mp r e ^ {- i \beta_ {r} h / 2}\right)} I _ {0} \tag {B5}
$$

where  $\mp$  represents the even or odd symmetric  $f(z)$ , respectively. Equation (B5) indicates that  $\hat{G} f(z)|_{z=h/2}$  is proportional to  $I_0$ . We can conclude that  $I_0 = 0$  is equivalent to  $\hat{G} f(z)|_{z=h/2} = 0$  if the structure is symmetric along the  $z$  axis.

Subsequently, we prove that  $I_0$  can be chosen as a real function. Owing to the arbitrary selection of the initial phase in the eigenproblem of the electromagnetic field,  $f(z)$  can be multiplied by an arbitrary phase factor and still satisfy the coupled equation, i.e.,  $f(z) = e^{i\theta}f_{0}(z)$ , and hence,  $I_0 = e^{i\theta}\int_{-h / 2}^{h / 2}e^{i\beta z}f_0(z)dz$ . Consequently, it can be concluded that  $I_0$  can always be a real function by the adjustment of the initial phase  $\theta$ .

More specifically, considering  $f(z) = u(z) + iv(z)$ , for an even symmetric  $f(z)$ , we obtain

$$
I _ {0} = \int_ {- h / 2} ^ {h / 2} \cos \left(\beta_ {r} z\right) u (z) d z + i \int_ {- h / 2} ^ {h / 2} \cos \left(\beta_ {r} z\right) v (z) d z. \tag {B6}
$$

The initial phase should be chosen as

$$
\int_ {- h / 2} ^ {h / 2} \cos (\beta_ {r} z) v (z) d z = 0 \quad \text {a n d} \quad \int_ {0} ^ {h / 2} u (z) d z > 0.
$$

For an odd symmetric  $f(z)$ , a similar formulation can be derived.

# APPENDIX C: THE GUIDED MODE

The calculation of the guided mode profile is quite similar to solving the wave function of an electron in a finite potential well. The average permittivity is  $\varepsilon_0$  within the PC slab  $[-h/2, h/2]$ , and  $\varepsilon_1$  for the outside region. Since the structure is mirror symmetric with respect to the  $z$  axis, the guided mode profile  $\Theta_0(z)$  is either even or odd. For instance, the even mode follows the equations at  $z \geqslant 0$ $[\Theta_0(z) = \Theta_0(-z)$  for  $z < 0]$ :

$$
\left[ \frac {\partial^ {2}}{\partial z ^ {2}} + \left(\varepsilon_ {0} k ^ {2} - \beta_ {0} ^ {2}\right) \right] \Theta_ {0} = 0, \quad 0 \leqslant z <   h / 2, \tag {C1}
$$

$$
\left[ \frac {\partial^ {2}}{\partial z ^ {2}} + \left(\varepsilon_ {1} k ^ {2} - \beta_ {0} ^ {2}\right) \right] \Theta_ {0} = 0, \quad z \geqslant h / 2. \tag {C2}
$$

We denote  $\beta_0 = (\varepsilon_0k^2 -\beta_0^2)^{1 / 2}$  and  $\gamma = (\beta_0^2 -\varepsilon_1k^2)^{1 / 2}$ , both of which are real and positive. We have  $\Theta_0 = \cos \beta z(0\leqslant z\leqslant h / 2)$  and  $Ce^{-\gamma z}(z > h / 2)$ . Owing to the continuity of  $\Theta_0(z)$  and  $\Theta_0'(z)$  at the boundary  $z = h / 2$ , we obtain

$$
\cos \beta h / 2 = C e ^ {- \gamma h / 2}, \tag {C3}
$$

$$
\beta \sin \beta h / 2 = \gamma C e ^ {- \gamma z}, \tag {C4}
$$

then

$$
\beta \tan \beta \frac {h}{2} = \gamma . \tag {C5}
$$

Denoting  $u = \beta h / 2$  and  $v = \gamma h / 2$ , Eq. (C5) is rewritten as

$$
u \tan u = v. \tag {C6}
$$

![](images/a793b42d5140af594a8657f2c73f90fa380138a779176f9b7049119913a16796.jpg)  
FIG. 7.  $uv$  curves to solve  $\beta$ , with the average permittivity within the PC slab  $\varepsilon_0 = 3.7299$ , the permittivity outside the PC slab  $\varepsilon_1 = 2.1141$ , and the PC slab thickness  $h = 1.1$ .

From the expression of  $\beta$  and  $\gamma, u$  and  $v$  also follow

$$
\frac {u ^ {2}}{U ^ {2}} + \frac {v ^ {2}}{V ^ {2}} = 1 \tag {C7}
$$

where  $U = [(\varepsilon_0 - \varepsilon_1) / \varepsilon_1]^{1 / 2}\beta_0h / 2$  and  $V = [(\varepsilon_0 - \varepsilon_1) / \varepsilon_0]^{1 / 2}$ $\beta_0h / 2$ , respectively.

The odd mode can be solved similarly, by assuming  $\Theta_0(z) = \sin \beta z$  within the PC slab, and Eq. (C6) becomes

$$
u \cot u = - v. \tag {C8}
$$

Equations (C7) and (C6) and Eqs. (C7) and (C8) give the solutions for even and odd modes, respectively. For example, if  $\varepsilon_0 = 3.7299$ ,  $\varepsilon_1 = 2.1141$ , and  $h = 1.1$ , the  $uv$  curves are shown in Fig. 7. For a given  $u$ , we have  $\beta = 2u / h$ .

Note that  $u$  and  $v$  are both positive, and each of the intersections of the black ellipse and the colored lines (red or blue) in the first quadrant gives one solution of  $\beta$ . As shown in Fig. 7, as  $h$  increases,  $U$  and  $V$  increase correspondingly, which leads to a series of intersections and solutions. These solutions are labeled  $\mathrm{TE}_0$ ,  $\mathrm{TE}_1$ ,  $\mathrm{TE}_2$ , etc. For a given solution, for example,  $\mathrm{TE}_0$ ,  $u$  increases monotonically with  $h$ , as shown in Fig. 7.

[1] J. von Neumann and E. Wigner, Phys. Z. 30, 465 (1929).  
[2] H. Friedrich and D. Wintgen, Phys. Rev. A 32, 3231 (1985).  
[3] H. Friedrich and D. Wintgen, Phys. Rev. A 31, 3964 (1985).  
[4] D. C. Marinica, A. G. Borisov, and S. V. Shabanov, Phys. Rev. Lett. 100, 183902 (2008).  
[5] E. N. Bulgakov and A. F. Sadreev, Phys. Rev. B 78, 075105 (2008).  
[6] Y. Plotnik, O. Peleg, F. Dreisow, M. Heinrich, S. Nolte, A. Szameit, and M. Segev, Phys. Rev. Lett. 107, 183901 (2011).  
[7] M. I. Molina, A. E. Miroshnichenko, and Y. S. Kivshar, Phys. Rev. Lett. 108, 070401 (2012).  
[8] C. W. Hsu, B. Zhen, S.-L. Chua, S. G. Johnson, J. D. Joannopoulos, and M. Soljacic, Light Sci. Appl. 2, e84 (2013).  
[9] E. N. Bulgakov and A. F. Sadreev, Phys. Rev. A 90, 053801 (2014).  
[10] J. D. Joannopoulos, S. G. Johnson, J. N. Winn, and R. D. Meade, Photonic Crystals: Molding the Flow of Light (Princeton University Press, Princeton, NJ, 2011).  
[11] J. Lee, B. Zhen, S.-L. Chua, W. Qiu, J. D. Joannopoulos, M. Soljacic, and O. Shapira, Phys. Rev. Lett. 109, 067401 (2012).  
[12] C. W. Hsu, B. Zhen, J. Lee, S.-L. Chua, S. G. Johnson, J. D. Joannopoulos, and M. Soljačić, Nature (London) 499, 188 (2013).  
[13] B. Zhen, C. W. Hsu, L. Lu, A. D. Stone, and M. Soljačić, Phys. Rev. Lett. 113, 257401 (2014).  
[14] F. H. Stillinger and D. R. Herrick, Phys. Rev. A 11, 446 (1975).  
[15] E. Bulgakov and A. Sadreev, Phys. Rev. B 83, 235321 (2011).  
[16] A. Albo, D. Fekete, and G. Bahir, Phys. Rev. B 85, 115307 (2012).  
[17] J. M. Zhang, D. Braak, and M. Kollar, Phys. Rev. Lett. 109, 116405 (2012).  
[18] S. Longhi and G. Della Valle, Sci. Rep. 3, 2219 (2013).  
[19] R. Porter and D. V. Evans, Wave Motion 43, 29 (2005).  
[20] C. M. Linton and P. McIver, Wave Motion 45, 16 (2007).  
[21] C. W. Hsu, B. Zhen, A. D. Stone, J. D. Joannopoulos, and M. Soljacic, Nat. Rev. Mater. 1, 16048 (2016).

[22] J. W. Yoon, S. H. Song, and R. Magnusson, Sci. Rep. 5, 18301 (2015).  
[23] Y. Yang, C. Peng, Y. Liang, Z. Li, and S. Noda, Phys. Rev. Lett. 113, 037401 (2014).  
[24] L. Lu, J. D. Joannopoulos, and M. Soljačić, Nat. Photonics 8, 821 (2014).  
[25] L. Lu, J. D. Joannopoulos, and M. Soljacic, Nat. Phys. 12, 626 (2016).  
[26] Y. Liang, C. Peng, K. Sakai, S. Iwahashi, and S. Noda, Phys. Rev. B 84, 195119 (2011).  
[27] C. Peng, Y. Liang, K. Sakai, S. Iwahashi, and S. Noda, Opt. Express 19, 24672 (2011).  
[28] Z. Wang, H. Zhang, L. Ni, W. Hu, and C. Peng, IEEE J. Quantum Electron. 52, 1 (2016).  
[29] Y. Liang, C. Peng, K. Sakai, S. Iwahashi, and S. Noda, Opt. Express 20, 15945 (2012).  
[30] C. Peng, Y. Liang, K. Sakai, S. Iwahashi, and S. Noda, Phys. Rev. B 86, 035108 (2012).  
[31] Y. Liang, C. Peng, K. Ishizaki, S. Iwahashi, K. Sakai, Y. Tanaka, K. Kitamura, and S. Noda, Opt. Express 21, 565 (2013).  
[32] Y. Yang, C. Peng, and Z. Li, Opt. Express 21, 20588 (2013).  
[33] Y. Yang, C. Peng, Y. Liang, Z. Li, and S. Noda, Opt. Lett. 39, 4498 (2014).  
[34] K. Kitamura, K. Sakai, N. Takayama, M. Nishimoto, and S. Noda, Opt. Lett. 37, 2421 (2012).  
[35] K. Hirose, Y. Liang, Y. Kurosaka, A. Watanabe, T. Sugiyama, and S. Noda, Nat. Photonics 8, 406 (2014).  
[36] A. F. Oskooi, D. Roundy, M. Ibanescu, P. Bermel, J. D. Joannopoulos, and S. G. Johnson, Comput. Phys. Commun. 181, 687 (2010).  
[37] W. Streifer, D. Scifres, and R. Burnham, IEEE J. Quantum Electron. 12, 422 (1976).  
[38] R. Kazarinov and C. Henry, IEEE J. Quantum Electron. 21, 144 (1985).