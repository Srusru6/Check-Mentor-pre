# Probing new physics scales from Higgs and electroweak observables at  $e^{+}e^{-}$  Higgs factory

Shao-Feng Ge, $^{a}$  Hong-Jian He $^{b,c}$  and Rui-Qing Xiao $^{b,d}$

Max-Planck-Institut für Kernphysik, Heidelberg 69117, Germany  
$^{b}$ Institute of Modern Physics and Center for High Energy Physics, Tsinghua University, Beijing 100084, China  
$^c$ Center for High Energy Physics, Peking University, Beijing 100871, China  
$^{d}$ Lawrence Berkeley National Laboratory, Berkeley, California 94720, U.S.A.

E-mail: gesf02@gmail.com, hjhe@tsinghua.edu.cn, ruiqingxiao@lbl.gov

ABSTRACT: New physics beyond the standard model (SM) can be model-independently formulated via dimension-6 effective operators, whose coefficients (cutoffs) characterize the scales of new physics. We study the probe of new physics scales from the electroweak precision observables (EWPO) and the Higgs observables (HO) at the future  $e^{+}e^{-}$  Higgs factory (such as CEPC). To optimize constraints of new physics from all available observables, we establish a scheme-independent approach. With this formulation, we treat the SM electroweak parameters and the coefficients of dimension-6 operators on equal footing, which can be fitted simultaneously by the same  $\chi^2$  function. As deviations from the SM are generally small, we can expand the new physics parameters up to linear order and perform an analytical  $\chi^2$  fit to derive the potential reach of the new physics scales. We find that the HO from both Higgs production and decay rates can probe the new physics scales up to 10 TeV (and to 44 TeV for the case of gluon-involved operator  $\mathcal{O}_g$ ), and the new physics scales of Yukawa-type operators can be probed by the precision Higgs coupling measurements up to (13 - 25) TeV. Further including the EWPO can push the limit up to 35 TeV. From this prospect, we demonstrate that the EWPO measured in the early phase of a Higgs factory can be as important as the Higgs observables. These indirect probes of new physics scales at the Higgs factory can mainly cover the energy range to be directly explored by the next generation hadron colliders of  $pp(50 - 100\mathrm{TeV})$ , such as the SPPC and FCC-hh.

KEYWORDS: Beyond Standard Model, Higgs Physics

ARXIV EPRINT: 1603.03385

# Contents

1 Introduction 1  
2 Scheme-independent approach for precision observables 3

3 New physics from dimension-6 effective operators 5

3.1 Effective Lagrangian with dimension-6 operators 6  
3.2 New physics via kinetic terms and mass terms 7

3.2.1 Higgs field  $h$  8  
3.2.2 Charged gauge boson 8  
3.2.3 Neutral gauge bosons 8  
3.2.4 Gluons 9

3.3 New physics via interaction vertices 9

3.3.1 Gauge boson coupling with fermions 9  
3.3.2 Gauge boson couplings with Higgs 10  
3.3.3 Hybrid couplings between bosons and fermions 12

4 Probing new physics scales of dimension-6 operators 12

4.1 New physics contributions to precision observables 13

4.1.1 Fine-structure constant 13  
4.1.2 Fermi constant 13  
4.1.3 Weak gauge boson masses  $M_W$  and  $M_Z$  13

4.2 New physics contributions to Higgs observables at  $e^{+}e^{-}$  colliders 15

4.2.1 Higgsstrahlung:  $e^{+}e^{-}\to Zh$  15  
4.2.2 WW fusion:  $e^{+}e^{-}\rightarrow \nu \bar{\nu} h$  at 250 GeV and 350 GeV 17  
4.2.3 Higgs decay into  $Z$  boson pair 18  
4.2.4 Higgs decay into  $W$  boson pair 19  
4.2.5 Other decay channels 19

4.3 Probing new physics scales at Higgs factory 20  
4.4 Combining with electroweak precision observables 24  
4.5 Enhanced sensitivity from CEPC measurements of  $W / Z$  masses 25  
4.6 Enhancement from  $Z$  -pole observables at CEPC 27

5 Higgs coupling precision tests at CEPC and probing dimension-6 Yukawa-type operators 29

5.1 Higgs coupling precision tests at CEPC 29  
5.2 Probing dimension-6 Yukawa-type operators at CEPC 33

6 Conclusions 35

A Kinetic mixing of gauge bosons 36

A.1Charged gauge bosons 36  
A.2 Neutral gauge bosons 37

B Analytic linear  $\chi^2$  fit 39

# 1 Introduction

The LHC discovery [1, 2] of a light Higgs boson  $h(125\mathrm{GeV})$  [3-7] has completed the particle spectrum of the standard model (SM) of particle physics. This culminates in the success of searches that lasted for decades [8]. Although the new physics has not yet been established so far, there are already strong motivations for going beyond the SM, including the observed neutrino oscillations and cosmic baryon asymmetry, as well as evidences for the dark matter and inflation. Since 2012, the particle physics has come to a turning point at which the precision Higgs measurements have become an important task for seeking clues to the new physics discovery [9].

We should stress that the SM is not merely a collection of various observed particles (fermions and bosons). The completion of the SM particle spectrum does not mean the completion of the SM itself until all SM interaction forces could be firmly measured. In fact, the SM consists of three fundamental gauge forces as its key ingredients, the electromagnetic force, the weak force, and the strong force, which are mediated by spin-1 gauge bosons, the photon  $(A_{\mu})$ , the weak bosons  $(W_{\mu}^{\pm}, Z_{\mu}^{0})$ , and the gluons  $(G_{\mu}^{a})$ , respectively. Furthermore, the spin-0 Higgs boson  $h(125\mathrm{GeV})$  is not merely another particle in the SM, because it joins three types of fundamental forces: (i) the gauge forces mediated by the spin-1 weak gauge bosons  $(W,Z)$ ; (ii) the Yukawa forces with fermions mediated by the spin-0 Higgs boson  $h$ ; (iii) and the cubic and quartic Higgs self-interactions<sup>1</sup>  $h^3$  and  $h^4$ . Among these, the type-(ii) and type-(iii) are new forces solely mediated by the Higgs boson itself.<sup>2</sup> They are largely untested so far, and provide the most likely places to encode new physics beyond the SM. Even for the type-(i) force, the LHC Run-2 could only measure the  $hWW$  and  $hZZ$  couplings down to  $(10 - 20)\%$  at  $2\sigma$  level [11]. It should be stressed that the discovery of the SM is not complete until all three types of Higgs-involved forces are fully tested by direct measurements.

The existence of such a spin-0 Higgs boson  $h(125\mathrm{GeV})$  is truly profound. This is because  $h$  is responsible for mass-generations for all SM particles, the spin-1 weak gauge

bosons and the spin- $\frac{1}{2}$  quarks and leptons, $^3$  via the above type-(i) and type-(ii) forces. Note that the observed unnaturally large hierarchies among the quark and lepton masses correspond to the same hierarchies among the Higgs Yukawa couplings. These Yukawa couplings range from the top quark Yukawa coupling  $y_{t} \simeq 1$  down to a tiny electron Yukawa coupling  $y_{e} = \mathcal{O}(10^{-6})$ , and have a rather irregular pattern, which are all unexplained within the SM. Hence, the Yuwaka sector apparently calls for new physics. The upper bounds on the new physics scales associated with all SM fermion mass-generations vary within the range of  $3.5 - 107\mathrm{TeV}$ , from the top quark to the electron [12, 13]. This range of scales are mainly beyond the reach of the LHC, but are within the (in)direct reaches of the next generation of high energy circular colliders [10, 12, 13]. The Higgs boson  $h$  also generates a physical mass  $M_{h}$  for itself via its type-(iii) self-interaction force after spontaneous symmetry breaking, but this mass is not protected against radiative corrections, causing the naturalness problem [14, 15]. Furthermore, this Higgs boson could serve as the inflaton to drive the required exponential expansion of the early universe [16, 17], and may also be connected to dark matter [18-21]. But, the SM Higgs potential suffers instability at scales well below the Planck mass [22-34] and calls for new physics at or beyond the TeV scale [35-40].

The above physics considerations strongly motivate the next generation high energy colliders beyond the LHC. Because of the profound implications of the newly discovered light Higgs boson  $h(125\mathrm{GeV})$ , it is natural to first precisely measure its properties at an  $e^{+}e^{-}$  Higgs factory and find compelling clues to the new physics. There are three major proposals on the market, the Circular Electron Positron Collider (CEPC) [41-43], the Future Circular Collider (FCC-ee) [44-46], and the International Linear Collider (ILC) [47-49]. All three proposed colliders can run at  $\sqrt{s} = 250\mathrm{GeV}$  by producing Higgs boson via Higgsstrahlung  $(e^{+}e^{-}\rightarrow Zh)$  and  $WW$  fusion  $(e^{+}e^{-}\rightarrow \nu \bar{\nu} h)$ . By measuring decay products of the final state  $Z$  boson in the Higgsstrahlung process, the Higgs signal can be extracted with the aid of recoil mass reconstruction technique [50]. This allows model-independent measurement of Higgs decay branching fractions down to percentage level. The CEPC runs at the collision energy of  $250\mathrm{GeV}$  with  $5\mathrm{ab}^{-1}$  integrated luminosity can produce about 1 million Higgs bosons. With these, most Higgs decay channels can be precisely measured with sizable events. Hence, such a Higgs factory will be an ideal place to probe the new physics deviations via Higgs production and decays, as well as other precision measurements.

In this work, we will study the probe of new physics scales at the  $e^{+}e^{-}$  Higgs factory, with CEPC as a concrete example. For such a Higgs factory, all the new physics effects associated with the light Higgs boson  $h(125\mathrm{GeV})$  can be parametrized by model-independent dimension-6 effective operators, which involve the SM Higgs doublet  $H$ . We will establish a scheme-independent approach to optimize the constraints of new physics from all available observables, including both the electroweak precision observables (EWPO) and the Higgs

observables (HO). With this formulation, we treat the SM electroweak parameters and the coefficients of dimension-6 operators on equal footing for a combined analysis, which can be fitted simultaneously by the same  $\chi^2$  function. Since deviations from the SM are generally small, we can expand the new physics parameters up to linear order and perform an analytical  $\chi^2$  fit to derive the potential reach of the new physics scales. We will demonstrate that the  $Z$ -pole measurements in the early phase of a Higgs factory can be as important as the Higgs observables. Some aspects of the effects of these operators on Higgsstrahlung production were studied before for  $e^{+}e^{-}$  colliders at various energies and with different focuses [67-77], which usually did not cover a complete list of these operators, and also did not consider the interplay with precision observables. A recent paper [78] studied the probe of these operators at a Higgs factory in the  $Z$ -scheme by taking the three most precisely measured electroweak observables (the fine structure constant  $\alpha$ , the Fermi constant  $G_{F}$ , and the  $Z$  boson mass  $M_Z$ ) as fixed inputs. The extended studies considered the existing electroweak precision observables at LEP [80], and the measurements at a future Higgs factory [81]. But a comprehensive investigation to combine the constraints of all HO and EWPO would be highly beneficial.

This paper is organized as follows. In section 2, we first establish a scheme-independent approach with linear expansion, which puts both dimension-6 operators and electroweak parameters on equal footing for fitting the data. In section 3, we analyze the CP-conserving dimension-6 effective operators that involve the SM Higgs doublet  $H$ , and summarize their effects on the field redefinition, particle masses, and interaction vertices, along with appendix A on kinetic mixing of gauge bosons. With these, in section 4, we study the Higgs and precision observables to deduce the reach of new physics scales that can be probed at the  $e^{+}e^{-}$  Higgs factory. Then, in section 5, we present the reach of precision measurement of the SM Higgs couplings at the CEPC, and apply this to study the probe of new physics scales associated with the dimension-6 Yukawa-type operators. Finally, we conclude in section 6. We also present our method of the analytic linear  $\chi^2$  fit in appendix B, which is used for the current analyses in section 4 and section 5.

# 2 Scheme-independent approach for precision observables

The electroweak sector of SM contains three basic parameters, the  $SU(2)_L$  gauge coupling  $g$ , the  $\mathrm{U}(1)_Y$  gauge coupling  $g'$ , and the Higgs vacuum expectation value (VEV)  $v$ . They can be determined by the existing precision tests, especially the four most precisely measured observables: the  $Z$  boson mass  $M_Z$ , the  $W$  boson mass  $M_W$ , the Fermi constant  $G_F$ , and the fine structure constant  $\alpha$ . Fixing the electroweak (EW) parameters  $(g,g',v)$  needs only three observables as inputs. In common practice, one usually adopts either  $Z$ -scheme  $(M_Z,G_F,\alpha)$  or  $W$ -scheme  $(M_Z,M_W,\alpha)$  to fix the values of  $(g,g',v)$ . Picking up which scheme is thus a matter of choice. In addition, the numerical analysis with this approach could only implement the central values of these electroweak observables without including

the associated uncertainties. This means, some information from experimental measurements is discarded and the outcome turns out to be scheme-dependent. In the present study, we try to incorporate all precision observables, so we can realize more sensitive probe of the new physics scales of the dimension-6 operators by using all the information available from experiments. The improvement of this new method is minor for the current precision data, but will become significant for analyzing the future precision measurements at the Higgs factory.

Our new strategy is to employ all the precision observables, including both their central values and uncertainties. The values of  $(g,g^{\prime},v)$  are determined by fitting the data altogether with effective operator coefficients [cf. (3.1)], rather than being expressed as functions of central values of 3 input parameters chosen for the  $Z$ -scheme or  $W$ -scheme. In this way, we can utilize all the most precisely measured precision EW observables  $(M_Z,M_W,G_F,\alpha)$  altogether with any other relevant observables in our  $\chi^2$  fit. We no longer need to invoke the concept of scheme or input parameters. Our analysis only involves model (fitting) parameters and experimental data. The basic EW parameters and the coupling coefficients can be treated equally as the fitting parameters. This will just add three more fitting parameters, but all precision observables can be equally used to constrain the dimension-6 operators.

An observable contains the SM contribution, expressed in terms of the EW parameters, plus the corrections from new physics. When fitting experimental measurements, the SM contribution and new physics contribution vary simultaneously. So long as the precision measurements are included, the EW parameters are constrained with small uncertainties. On the other hand, the new physics contribution is expected to be small. Thus, it is well justified that both the EW parameters and the effective operator coefficients have only small shifts from their reference values. We can expand observables as linear combinations of the shifts. In consequence, we can perform analytic  $\chi^2$  fit as elaborated in B.

To implement the two features above, we treat all model-parameters (EW parameter and effective operator coefficients) on equal footing and make analytic  $\chi^2$  fit for small variations. We lay out the procedure as follows. First, we split each EW parameter  $f$  as a sum of the reference value (acting as starting point for the  $\chi^2$  fit) and the shift from it,

$$
f ^ {(\mathrm {s m})} \equiv f ^ {(r)} + \delta f \simeq f ^ {(r)} \left(1 + \frac {\delta f}{f}\right), \tag {2.1}
$$

where  $f^{(\mathrm{sm})}$  is the SM prediction,  $f^{(r)}$  the reference value, and  $\delta f$  the shift between them. Note that before fitting the data each of these quantities exists only symbolically and should be treated as a variable without specific value. Then, any observable  $X$  can be expanded in a similar way,

$$
X \equiv X [   [ f ^ {(\mathrm {s m})} ]   ] + \overline {{\delta X}} = X [   [ f ^ {(r)} ]   ] + X ^ {\prime} [   [ f ]   ] \delta f + \overline {{\delta X}} \equiv X ^ {(r)} + \widetilde {\delta X}, \tag {2.2}
$$

where  $X[[f]]$  is a functional form of the observable in terms of the EW parameters, while the new physics contribution (which can arise from the relevant dimension-6 operators [83-88] for instance, cf. eq. (3.1) and table 1) and the SM loop corrections are included in  $\overline{\delta X}$ . Corresponding to the reference value  $f^{(r)}$  of the EW parameters, the observable also has a

reference value  $X^{(r)}\equiv X[[f^{(r)}]]$  . Its shift from reference value is then combined into

$$
\widetilde {\delta X} \equiv X ^ {\prime} [   [ f ]   ] \delta f + \overline {{\delta X}} , \tag {2.3}
$$

where  $X'[[f]]$  is a functional derivative with respect to  $f$ .

For the present study, we use  $f = (M_Z, G_F, \alpha)$  as EW fitting parameters which are equivalent to using  $(g, g', v)$ , but have the benefit of being direct physical observables. Each of them contains a shift from its reference value,

$$
M _ {Z} ^ {(\mathrm {s m})} = M _ {Z} ^ {(r)} \left(1 + \frac {\delta M _ {Z}}{M _ {Z}}\right), \quad G _ {F} ^ {(\mathrm {s m})} = G _ {F} ^ {(r)} \left(1 + \frac {\delta G _ {F}}{G _ {F}}\right), \quad \alpha^ {(\mathrm {s m})} = \alpha^ {(r)} \left(1 + \frac {\delta \alpha}{\alpha}\right). \tag {2.4}
$$

The quantities  $(\delta M_Z, \delta G_F, \delta \alpha)$  are the differences between the SM prediction and reference value. Note that the SM prediction can be at either tree-level or loop-level, depending on whether the loop-level correction needs to be taken into consideration. In either case, the dependence on the electroweak parameter shifts remains the same, since the SM loop-contribution is already at the linear order and hence can be treated as a constant term in our linear  $\chi^2$  fit,  $\delta X_{1 - \mathrm{loop}}[[f]] \simeq \delta X_{1 - \mathrm{loop}}[[f^{(r)}]]$ , as long as the reference values are close to the experimental central values so that the effect of the shift  $\delta f$  belongs to higher orders and is negligible at the linear-order perturbation. We will give an explicit example for the case of  $W$  boson mass in section 4.1, which justifies that eq. (2.4) applies to either tree-level or loop-level analysis. $^6$

In principle, the reference point  $f^{(f)}$  can take any value. This arbitrariness is then compensated by the corresponding shift parameter  $\delta f$ . Nevertheless, for our linear expansion and thus the analytic  $\chi^2$  fit to work, the reference point should be close to the best-fit value which is around the experimental central value. When the reference value is fixed to the experimental central value and if no parameter is allowed to be freely adjusted, the shift quantity  $\widetilde{\delta X}$  would vanish. For our choice of  $(M_Z, G_F, \alpha)$  as fitting parameter, the assumption of vanishing  $(\widetilde{\delta M_Z}, \widetilde{\delta G_F}, \widetilde{\delta\alpha})$  will reduce our scheme-independent approach to the commonly used  $Z$ -scheme. For the practical analysis here, we will assign the reference values of  $(M_Z, G_F, \alpha)$  to be their current experimental central values for convenience and allow their shifts  $(\delta M_Z, \delta G_F, \delta \alpha)$  to vary for scheme-independent fit (when needed).

# 3 New physics from dimension-6 effective operators

In this section, we first present the effective Lagrangian with relevant dimension-6 operators for the current precision Higgs study (section 3.1). Then, we systematically derive their effects via kinetic terms and mass terms (section 3.2), and via interaction vertices (section 3.3).

Table 1. List of dimension-6 effective operators for the present study.  

<table><tr><td>Higgs</td><td>EW Gauge Bosons</td><td>Fermions</td></tr><tr><td>O_H=1/2(∂μ|H|^2)^2</td><td>O_WW=g^2|H|^2W^a_{μν}W^{aμν}</td><td>O_L^{(3)}=(iH^†σ^a\stackrel{\leftrightarrow}{D}_μH)(\overline{\Psi}_L\gamma^μσ^a\Psi_L)</td></tr><tr><td>O_T=1/2(H^†D^aμH)^2</td><td>O_BB=g^2|H|^2B^a_{μν}B^bμν</td><td>O_{LL}^{(3)}=(\overline{\Psi}_L\gamma^a\sigma^a\Psi_L)(\overline{\Psi}_L\gamma^μ\sigma^a\Psi_L)</td></tr><tr><td></td><td>O_WB=gg&#x27;H^†σ^aHW^a_{μν}B^bμν</td><td>O_L=(iH^†\stackrel{\leftrightarrow}{D}_μH)(\overline{\Psi}_L\gamma^μ\Psi_L)</td></tr><tr><td>Gluon</td><td>O_HW=G(d^μH)†σ^a(D^νH)W^a_{μν}</td><td>O_R=(iH^†\stackrel{\leftrightarrow}{D}_μH)(\overline{\psi}_Rγ^μψ_R)</td></tr><tr><td>O_g=g_s^2|H|^2G^a_{μν}G^{aμν}</td><td>O_HB=ig&#x27;(D^μH)†(D^νH)B^a_{μν}</td><td>O_y^u=|H|^2\overline{\Psi}_L^q\tilde{H}u_R</td></tr><tr><td></td><td>O_W=\frac{ig}{2}(H^†σ^a\stackrel{\leftrightarrow}{D}_μH)D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^{aμν}</td><td>O_y^d=|H|^2\overline{\Psi}_L^qHd_R</td></tr><tr><td></td><td>O_B=\frac{ig&#x27;}{2}(H^†\stackrel{\leftrightarrow}{D}_μH)D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{μν}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^ a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}D^a_{φ}</td><td></td></tr></table>

# 3.1 Effective Lagrangian with dimension-6 operators

The new physics effects beyond the SM can be generally parametrized by the dimension-6 effective operators in a model-independent way [83-88],

$$
\mathcal {L} = \mathcal {L} _ {\mathrm {S M}} + \sum_ {j} \frac {c _ {j}}{\Lambda^ {2}} \mathcal {O} _ {j}. \tag {3.1}
$$

If these new physics effects are associated with Higgs boson, we expect a set of gauge-invariant and CP-conserving dimension-6 operators will appear in the low energy effective theory, as summarized in table 1. We expect the associated cutoff scale  $\Lambda / |c_{j}|^{\frac{1}{2}}$  to be around TeV scale or not far above it. Since the physical processes at an  $e^{+}e^{-}$ Higgs factory with  $\sqrt{s} = 240 - 250\mathrm{GeV}$  have energy scales well below the TeV scale, we see that the effective Lagrangian (3.1) provides a perfectly valid low energy formulation of the new physics effects.

This effective Lagrangian contains ten bosonic and seven fermionic dimension-6 operators, where each operator is associated with its own coefficient  $c_{j} / \Lambda^{2}$ . We note that integration by part gives the identities [89],

$$
\mathcal {O} _ {B} = \mathcal {O} _ {H B} + \frac {1}{4} \left(\mathcal {O} _ {B B} + \mathcal {O} _ {W B}\right), \tag {3.2a}
$$

$$
\mathcal {O} _ {W} = \mathcal {O} _ {H W} + \frac {1}{4} \left(\mathcal {O} _ {W W} + \mathcal {O} _ {W B}\right). \tag {3.2b}
$$

It means that among the seven operators  $(\mathcal{O}_B, \mathcal{O}_W, \mathcal{O}_{BB}, \mathcal{O}_{WB}, \mathcal{O}_{WW}, \mathcal{O}_{HB}, \mathcal{O}_{HW})$ , two of them are redundant. We could use these to eliminate  $(\mathcal{O}_B, \mathcal{O}_W)$ , which is called the HISZ basis in the literature [90]. We further note that the operators  $(\mathcal{O}_B, \mathcal{O}_W)$  can be replaced by the equation of motion (EOM) [89],

$$
\mathcal {O} _ {B} = g ^ {\prime 2} \left[ - \frac {1}{2} \mathcal {O} _ {T} + \frac {1}{2} \left(Y _ {L} \mathcal {O} _ {L} + Y _ {R} \mathcal {O} _ {R}\right) \right], \tag {3.3a}
$$

$$
\mathcal {O} _ {W} = g ^ {2} \biggl [ - \frac {3}{2} \mathcal {O} _ {H} + 2 \mathcal {O} _ {6} + \frac {1}{2} \left(\mathcal {O} _ {y} ^ {u} + \mathcal {O} _ {u} ^ {d} + \mathcal {O} _ {y} ^ {\ell} + \mathrm {h . c .}\right) + \frac {1}{4} \mathcal {O} _ {L} ^ {(3)} \biggr ], (3. 3 \mathrm {b})
$$

where  $Y_{L}$  and  $Y_{R}$  stand for the hypercharges of fermion fields  $\Psi_{L}$  and  $\Psi_{R}$ , respectively. Eqs. (3.3a)-(3.3b) also make  $(\mathcal{O}_B, \mathcal{O}_W)$  redundant. Thus, one may use the identities (3.2a)-(3.2b) to eliminate the two other operators  $(\mathcal{O}_{WW}, \mathcal{O}_{WB})$  instead. This means that the four operators  $(\mathcal{O}_B, \mathcal{O}_W)$  and  $(\mathcal{O}_{WW}, \mathcal{O}_{WB})$  are redundant, and can be eliminated in principle. For the current first-step study, with the limited experimental observables and a large number of dimension-6 effective operators, we will not carry out a global  $\chi^2$  fit of all operators together. Instead, we perform the  $\chi^2$  fit by including only one operator at each time, which is common in the literature. So we need not to exclude the redundant operators. In this way, we can first examine how each operator contributes and how it can be constrained, for completeness. Nevertheless, in the current study, we will always impose the basic identities (3.2a)-(3.2b) to eliminate  $(\mathcal{O}_B, \mathcal{O}_W)$ , as is the commonly used HISZ basis [90]. [But we stress that when considering a future global  $\chi^2$  fit including many operators simultaneously, it is necessary to remove all the redundant operators by using both the identities (3.2) and the EOM (3.3).]

Note that in table 1,  $\mathcal{O}_{LL}^{(3)}$  does not involve the SM Higgs doublet, but we take it into account since it affects the Fermi constant (which is the coefficient of dimension-6 fourfermion operator itself), and consequently the other observables through parameter shift. Since each of the Yukawa-type effective operators  $(\mathcal{O}_y^u,\mathcal{O}_y^d,\mathcal{O}_y^\ell)$  modifies the SM Yuakawa coupling only by a rescaling factor, we study their tests separately in section 5.

If the underlying UV theory for these effective operators is known, their coefficients could be expressed in terms of the model-parameters in principle. For the present study, we follow the model-independent effective theory formulation, where the coefficients of dimension-6 operators are independent of each other. We will use experimental measurements to estimate the potential reach of indirectly probing the effective new physics scale  $\Lambda_{j}\equiv \Lambda /|c_{j}|^{\frac{1}{2}}$  associated with each operator at the Higgs factory (cf. section 4).<sup>7</sup> We will keep in mind that the coefficient  $c_{j}$  of each effective operator  $\mathcal{O}_j$  usually depends on powers of the couplings from the underlying UV theory, which could be larger or smaller than  $\mathcal{O}(1)$ . The coefficient  $c_{j}$  could also depend on loop-factors when  $\mathcal{O}_j$  is induced from loop-level contributions (such as the case of  $\mathcal{O}_g$ ). Hence, it is a model-dependent issue to further convert our general bound on  $\Lambda_{j}$  to the corresponding bound on  $\Lambda$ . In the rest of this section, we first analyze the contributions of these dimension-6 operators to the relevant Feynman vertices and physical observables.

# 3.2 New physics via kinetic terms and mass terms

Before drawing Feynman diagrams and computing the relevant Higgs production cross sections and decay width, it is necessary to check whether all the involved propagators take their canonical form. If not, we need to make proper field redefinitions as summarized in appendix A. Such redefinitions will modify the relevant mass terms and interaction vertices. With the dimension-6 operators in table 1, the kinetic terms of fermions remain the same, while those of bosonic fields, the Higgs field  $h$  and the gauge bosons  $(W^{\pm}, Z^{0}, A^{0})$ , are affected.

# 3.2.1 Higgs field  $h$

The operator  $\mathcal{O}_H$  in table 1 could contribute a nonzero correction to the kinetic term of the Higgs field. Redefining the Higgs field,

$$
h \rightarrow \left(1 - \frac {1}{2} \frac {v ^ {2}}{\Lambda^ {2}} c _ {H}\right) h \equiv Z _ {h} h, \tag {3.4}
$$

will absorb the deviation from the canonical form. It applies to every  $h$  that appears in the Lagrangian and leads to a rescaling factor for any interaction vertex involving Higgs field(s). Each Higgs field  $h$  receives a rescaling factor  $Z_{h}$ , and Higgs mass term receives a rescaling factor  $Z_{h}^{2}$ .

# 3.2.2 Charged gauge boson

The  $W^{\pm}$  gauge bosons receive a correction to its kinetic term from the operator  $\mathcal{O}_{WW}$  in table 1. This leads to the field redefinition of the  $W^{\pm}$  bosons,

$$
W ^ {\pm} \rightarrow \left(1 + \frac {v ^ {2}}{\Lambda^ {2}} g ^ {2} c _ {W W}\right) W ^ {\pm} \equiv Z _ {W} W ^ {\pm}. \tag {3.5}
$$

Although the  $W$  mass receives no direct correction, the field redefinition and parameter shift can contribute indirectly,

$$
\widetilde {\frac {\delta M _ {W}}{M _ {W}}} = \frac {1}{c _ {w} ^ {2} - s _ {w} ^ {2}} \left[ c _ {w} ^ {2} \frac {\delta M _ {Z}}{M _ {Z}} + \frac {1}{2} s _ {w} ^ {2} \left(\frac {\delta G _ {F}}{G _ {F}} - \frac {\delta \alpha}{\alpha}\right) \right] + \frac {v ^ {2}}{\Lambda^ {2}} g ^ {2} c _ {W W}, (3. 6)
$$

according to (A.3). The weak mixing angle is denoted as  $(c_w, s_w) \equiv (\cos \theta_w, \sin \theta_w)$  evaluated at the reference point. Note that the correction from field redefinition to the mass term has the same sign as in (3.5).

# 3.2.3 Neutral gauge bosons

The case of neutral gauge bosons is a little bit more complicated since both kinetic term and mass term are  $2 \times 2$  matrices. From the dimension-6 operators  $(\mathcal{O}_{WW}, \mathcal{O}_{BB}, \mathcal{O}_{WB})$  in table 1, we derive corrections to the kinetic term,  $\mathbb{I}\partial^2 \to \mathbb{K}\partial^2 \equiv (\mathbb{I} + \delta K)$ , with the explicit form of  $\delta K$  given in (A.13). The neutral  $Z$  and  $A$  gauge bosons need to be not only redefined but also diagonalized as we elaborate in appendix A.2,

$$
Z ^ {\mu} \rightarrow \left[ 1 + \frac {v ^ {2}}{\Lambda^ {2}} \left(c _ {w} ^ {2} g ^ {2} c _ {W W} + c _ {w} s _ {w} g g ^ {\prime} c _ {W B} + s _ {w} ^ {2} g ^ {\prime 2} c _ {B B}\right)\right] Z ^ {\mu}, \tag {3.7a}
$$

$$
\begin{array}{l} A ^ {\mu} \rightarrow \left[ 1 + \frac {v ^ {2}}{\Lambda^ {2}} \left(s _ {w} ^ {2} g ^ {2} c _ {W W} - c _ {w} s _ {w} g g ^ {\prime} c _ {W B} + c _ {w} ^ {2} g ^ {\prime 2} c _ {B B}\right)\right] A ^ {\mu} \\ + 2 \frac {v ^ {2}}{\Lambda^ {2}} \left[ c _ {w} s _ {w} g ^ {2} c _ {W W} - \frac {1}{2} (c _ {w} ^ {2} - s _ {w} ^ {2}) g g ^ {\prime} c _ {W B} - c _ {w} s _ {w} g ^ {\prime 2} c _ {B B} \right] Z ^ {\mu}. \qquad (3. 7 \mathrm {b}) \\ \end{array}
$$

For convenience, we denote the field redefinition of  $A$  and  $Z$  as  $A \to Z_A A + \delta Z_X Z \equiv (1 + \delta Z_A) A + \delta Z_X Z$  and  $Z \to Z_Z Z \equiv (1 + \delta Z_Z) Z$ , respectively, where the explicit form of  $(\delta Z_A, \delta Z_Z, \delta Z_X)$  can be read off from (3.7). Note that kinetic mixing can introduce not

only field redefinition  $(\delta Z_A, \delta Z_Z)$  to both  $A$  and  $Z$ , but also equal correction  $\delta Z_X$  to the left- and right-handed currents of the  $Z$  boson from the electromagnetic current as shown in the last line.

Any vertex involving  $n$  fields of  $Z$  should be divided by a factor of  $Z_Z^n$  due to this field redefinition. The mass term can be treated as a vertex with two gauge fields. Hence, it is rescaled by  $Z_Z^2$ . The mass of the neutral gauge boson  $Z$  is also affected by  $\mathcal{O}_T$  in table 1,

$$
\frac {\widetilde {\delta M _ {Z}}}{M _ {Z}} = \frac {\delta M _ {Z}}{M _ {Z}} - \frac {1}{2} \frac {v ^ {2}}{\Lambda^ {2}} c _ {T} + \delta Z _ {Z}. (3. 8)
$$

where the extra contribution comes from the field redefinition (3.7a) of the  $Z$  gauge boson as indicated by the general analysis in appendix A.2.

# 3.2.4 Gluons

Once the Higgs field  $H$  develops nonzero VEV, the operator  $\mathcal{O}_g$  in table 1 can induce a correction to the kinetic term of gluons. The effect is a field redefinition,

$$
G _ {\mu} ^ {a} \rightarrow \left(1 + \frac {v ^ {2}}{\Lambda^ {2}} g _ {s} ^ {2} c _ {g}\right) G _ {\mu} ^ {a} \equiv Z _ {G} G _ {\mu} ^ {a}, \tag {3.9}
$$

which only affect the relevant interaction vertices.

# 3.3 New physics via interaction vertices

The new physics parameters of the dimension-6 operators can affect the interaction vertices in three ways. First, they can give direct contributions to the existing vertex, sometimes with a different tensor structure such as the case of  $ZZh$  coupling. Second, the field redefinition can introduce an overall rescaling factor of the relevant vertex that contains the corresponding field. Finally, the shifts of electroweak parameters from their reference values can affect the existing vertex through zeroth order correlations. In addition, the dimension-6 operators may introduce some new vertices, such as the trilinear vertex  $AZh$ , and other quartic interactions  $Zh\psi \bar{\psi}$  and  $Wh\ell\nu$ .

# 3.3.1 Gauge boson coupling with fermions

The coupling between the charged gauge boson  $W^{\pm}$  and leptons can be modified by the operator  $\mathcal{O}_L^{(3)}$  in table 1 and the  $W$  field redefinition (3.5),

$$
\frac {g}{\sqrt {2}} \left(\frac {v ^ {2}}{\Lambda^ {2}} c _ {L} ^ {(3)} + \frac {v ^ {2}}{\Lambda^ {2}} g ^ {2} c _ {W W}\right) \left(W _ {\mu} ^ {+} \bar {\nu} _ {L} \gamma^ {\mu} \ell_ {L} + W _ {\mu} ^ {-} \bar {\ell} _ {L} \gamma^ {\mu} \nu_ {L}\right). \tag {3.10}
$$

Note that the direct correction to this vertex has the same form as the SM counterpart. Hence, its contribution can be combined into the overall coupling constant. In addition,  $g_{W\ell \nu}$  can split into the reference value plus parameter shift in  $g$ ,

$$
\widetilde {\frac {\delta g _ {W \ell \nu}}{g _ {W \ell \nu}}} = \frac {1}{\cos 2 \theta_ {w}} \left(c _ {w} ^ {2} \frac {\delta M _ {Z}}{M _ {Z}} + \frac {1}{2} c _ {w} ^ {2} \frac {\delta G _ {F}}{G _ {F}} - \frac {1}{2} s _ {w} ^ {2} \frac {\delta \alpha}{\alpha}\right) + \frac {v ^ {2}}{\Lambda^ {2}} c _ {L} ^ {(3)} + \frac {v ^ {2}}{\Lambda^ {2}} g ^ {2} c _ {W W}. (3. 1 1)
$$

For the  $Z\bar{\ell}\ell$  vertex, new physics contributions arise from both direct correction and kinetic mixing. The first part comes from operators  $(\mathcal{O}_L^{(3)},\mathcal{O}_L,\mathcal{O}_R)$  in table 1,

$$
\frac {g}{2 c _ {w}} \frac {v ^ {2}}{\Lambda^ {2}} \left[ \left(c _ {L} ^ {(3)} - c _ {L}\right) \bar {\nu} _ {L} \gamma^ {\mu} \nu_ {L} - \left(c _ {L} ^ {(3)} + c _ {L}\right) \bar {\ell} _ {L} \gamma^ {\mu} \ell_ {L} - c _ {R} ^ {\nu} \bar {\nu} _ {R} \gamma^ {\mu} \nu_ {R} - c _ {R} ^ {\ell} \bar {\ell} _ {R} \gamma^ {\mu} \ell_ {R} \right] Z _ {\mu}. \quad (3. 1 2)
$$

We can see that the four terms are independent of each other with four different dimension-6 operator coefficients. In addition, the redefinitions (3.7) of  $(Z,A)$  introduce extra corrections to the left- and right-handed currents,

$$
\delta g _ {L} ^ {*} = Q g _ {z} c _ {w} s _ {w} \delta Z _ {X} + g _ {z} \left(T _ {3} - s _ {w} ^ {2} Q\right) \delta Z _ {Z}, \tag {3.13a}
$$

$$
\delta g _ {R} ^ {*} = Q g _ {z} c _ {w} s _ {w} \delta Z _ {X} - g _ {z} s _ {w} ^ {2} Q \delta Z _ {Z}. (3. 1 3 \mathrm {b})
$$

The first term is universal for left- and right-handed couplings, since it comes from the  $Z$ - $A$  mixing and most importantly is proportional to the electromagnetic current. On the other hand, the second term comes from the field redefinition of the  $Z$  gauge boson, rendering it proportional to the SM prediction of  $g_{L}$  and  $g_{R}$ , respectively. Finally, from the zeroth-order coupling, extra correction can appear through parameter shift. Here we show the correction to the coupling with charged leptons,

$$
\widetilde {\delta g _ {L}} \equiv - \left[ \frac {1}{2 \cos 2 \theta_ {w}} \left(\frac {\delta M _ {Z}}{M _ {Z}} + \frac {1}{2} \frac {\delta G _ {F}}{G _ {F}}\right) - \frac {c _ {w} ^ {2} s _ {w} ^ {2}}{\cos 2 \theta_ {w}} \frac {\delta \alpha}{\alpha} \right] g _ {z} - \frac {g _ {z} v ^ {2}}{2 \Lambda^ {2}} \left(c _ {L} ^ {(3)} + c _ {L}\right) + \delta g _ {L} ^ {*}, (3. 1 4 a)
$$

$$
\widetilde {\delta g _ {R}} \equiv - \left[ \frac {s _ {w} ^ {2}}{\cos 2 \theta_ {w}} \left(\frac {\delta M _ {Z}}{M _ {Z}} + \frac {1}{2} \frac {\delta G _ {F}}{G _ {F}}\right) - \frac {c _ {w} ^ {2} s _ {w} ^ {2}}{\cos 2 \theta_ {w}} \frac {\delta \alpha}{\alpha} \right] g _ {z} - \frac {g _ {z} v ^ {2}}{2 \Lambda^ {2}} c _ {R} + \delta g _ {R} ^ {*}, \tag {3.14b}
$$

where the second term accounts for the direct contribution summarized in (3.12). For convenience, we use  $g_{z} \equiv g / \cos \theta_{w}$  to denote the weak gauge coupling associated with  $Z$  boson.

# 3.3.2 Gauge boson couplings with Higgs

Corrections to the  $ZZh$  vertex arise from  $(\mathcal{O}_T,\mathcal{O}_{WW},\mathcal{O}_{BB},\mathcal{O}_{WB},\mathcal{O}_{HW},\mathcal{O}_{HB})$  in table 1,

$$
- \frac {g ^ {2} v}{2 c _ {w} ^ {2}} \frac {v ^ {2}}{\Lambda^ {2}} c _ {T} h Z _ {\mu} Z ^ {\mu} + \delta Z _ {Z} h \mathcal {Z} _ {\mu \nu} \mathcal {Z} ^ {\mu \nu} + \frac {g}{2} \frac {v \partial_ {\mu} h}{\Lambda^ {2}} \left[ g c _ {H W} + \frac {s _ {w}}{c _ {w}} g ^ {\prime} c _ {H B} \right] Z _ {\nu} \mathcal {Z} ^ {\mu \nu}, (3. 1 5)
$$

where  $\mathcal{Z}_{\mu \nu} \equiv \partial_{\mu}Z_{\nu} - \partial_{\nu}Z_{\mu}$ . Note that the Higgs field redefinition (3.4) also contributes an overall term,  $-\delta Z_{h}g_{z}M_{Z}\frac{1}{2} hZ_{\mu}Z^{\mu}$ , which should be combined with the first term that has the same tensor structure as the SM contribution. To keep the expression neat, let us define  $f^{\mu \nu}[[p,q]] \equiv p^{\nu}q^{\mu} - (p\cdot q)g^{\mu \nu}$ . Then, the Feynman rule reads,

$$
i g _ {Z Z h} \left\{\left(1 + c _ {0} ^ {Z}\right) g ^ {\mu \nu} + c _ {1} ^ {Z} f ^ {\mu \nu} [ [ k _ {1}, k _ {2} ] ] + c _ {2} ^ {Z} f ^ {\mu \nu} [ [ k _ {1}, k _ {1} ] ] + c _ {3} ^ {Z} f ^ {\mu \nu} [ [ k _ {2}, k _ {2} ] ] \right\}, \tag {3.16}
$$

with  $g_{ZZh} \equiv gM_Z / c_w$ . The decomposition (3.16) is useful when discussing Higgs decay and will be applied to the  $W^{+}W^{-}h$  and  $AZh$  vertices discussed later in this section. The coefficients  $c_i^Z$  are defined as

$$
c _ {1} ^ {Z} = \frac {2}{\Lambda^ {2}} \left[ 4 \left(s _ {w} ^ {4} c _ {B B} + c _ {w} ^ {2} s _ {w} ^ {2} c _ {W B} + c _ {w} ^ {4} c _ {W W}\right) - \left(s _ {w} ^ {2} c _ {H B} + c _ {H W} ^ {2}\right) \right], \tag {3.17a}
$$

$$
c _ {2} ^ {Z} = c _ {3} ^ {Z} = - \frac {1}{\Lambda^ {2}} \left(s _ {w} ^ {2} c _ {H B} + c _ {w} ^ {2} c _ {H W}\right). \tag {3.17b}
$$

Note that the overall rescaling factor of the SM contribution has been combined with the  $Z$  boson field redefinition (3.7a) and the parameter shift,

$$
c _ {0} ^ {Z} = \widetilde {\frac {\delta g _ {Z Z h}}{g _ {Z Z h}}} = \frac {1}{2} \frac {\delta G _ {F}}{G _ {F}} + 2 \frac {\delta M _ {Z}}{M _ {Z}} - 2 \frac {v ^ {2}}{\Lambda^ {2}} \left(c _ {T} + \frac {1}{4} c _ {H}\right) + 2 \delta Z _ {Z}. (3. 1 8)
$$

The  $W^{+}W^{-}h$  vertex is much simpler without complication from kinetic mixing. It receives corrections from  $(\mathcal{O}_{WW},\mathcal{O}_{HW})$  in table 1,

$$
2 g ^ {2} \frac {v h}{\Lambda^ {2}} c _ {W W} \mathcal {W} _ {\mu \nu} ^ {+} \mathcal {W} ^ {- \mu \nu} - \frac {g ^ {2}}{2} \frac {v \partial_ {\mu} h}{\Lambda^ {2}} c _ {H W} \left(W _ {\nu} ^ {+} \mathcal {W} ^ {- \mu \nu} + W _ {\nu} ^ {-} \mathcal {W} ^ {+ \mu \nu}\right), \tag {3.19}
$$

where  $\mathcal{W}^{\pm \mu \nu}\equiv \partial^{\mu}W^{\pm \nu} - \partial^{\nu}W^{\pm \mu}$ . It can be grouped into the same form as (3.16), with  $p_{\pm}$  denoting the momenta of  $W_{\pm}$ ,

$$
i g M _ {W} \left\{\left(1 + c _ {0} ^ {W}\right) g ^ {\mu \nu} + c _ {1} ^ {W} f ^ {\mu \nu} [   [ p _ {+}, p _ {-} ]   ] + c _ {2} ^ {W} f ^ {\mu \nu} [   [ p _ {+}, p _ {+} ]   ] + c _ {3} ^ {W} f ^ {\mu \nu} [   [ p _ {-}, p _ {-} ]   ] \right\}, \tag {3.20}
$$

where the coefficients  $c_{i}^{W}$  are defined as

$$
c _ {1} ^ {W} = \frac {2}{\Lambda^ {2}} \left(4 c _ {W W} + c _ {H W}\right), \quad c _ {2} ^ {W} = c _ {3} ^ {W} = \frac {1}{\Lambda^ {2}} c _ {H W}. \tag {3.21}
$$

The field redefinitions of  $W$  and Higgs field redefinitions, (3.5) and (3.4), contribute as an overall rescaling and hence can be combined with the parameter shift,

$$
c _ {0} ^ {W} = \widetilde {\frac {\delta g _ {W W h}}{g _ {W W h}}} = \frac {1}{2} \left(2 c _ {w} ^ {2} \frac {\delta M _ {Z}}{M _ {Z}} + \frac {1}{2} \frac {\delta G _ {F}}{G _ {F}} - s _ {w} ^ {2} \frac {\delta \alpha}{\alpha}\right) - \frac {1}{2} \frac {v ^ {2}}{\Lambda^ {2}} c _ {H} + 2 \frac {v ^ {2}}{\Lambda^ {2}} g ^ {2} c _ {W W}. (3. 2 2)
$$

In the SM, the photon  $A_{\mu}$  only couples to a pair of charged particle and its anti-particle. This is violated by effective operators  $(\mathcal{O}_{WW},\mathcal{O}_{BB},\mathcal{O}_{WB},\mathcal{O}_{HW},\mathcal{O}_{HB})$  in table 1,

$$
2 \frac {\delta Z _ {X}}{v} h \mathcal {Z} _ {\mu \nu} F ^ {\mu \nu} + \frac {s _ {w} g ^ {2} v}{2 c _ {w} \Lambda^ {2}} \left(c _ {H W} - c _ {H B}\right) \partial_ {\mu} h Z _ {\nu} F ^ {\mu \nu}, \tag {3.23}
$$

where  $F^{\mu \nu} = \partial^{\mu}A^{\nu} - \partial^{\nu}A^{\mu}$  is the field strength of photon. We can see that the first term actually comes from kinetic mixing which is proportional to  $\delta Z_{X}$  and arises from the second line of (3.7b). With everything combined, the Feynman rule of this vertex  $A^{\mu}Z^{\nu}h$  can be grouped into,

$$
i g _ {Z Z h} \left(c _ {1} ^ {A} f ^ {\mu \nu} [ [ k _ {A}, k _ {Z} ] ] + c _ {3} ^ {A} f ^ {\mu \nu} [ [ k _ {A}, k _ {A} ] ]\right), \tag {3.24a}
$$

where

$$
c _ {1} ^ {A} + c _ {3} ^ {A} = 2 \frac {\delta Z _ {X}}{g _ {Z Z h} v}, \qquad c _ {3} ^ {A} = - \frac {v}{\Lambda^ {2}} c _ {w} s _ {w} (c _ {H W} - c _ {H B}). \qquad \qquad (3. 2 4 \mathrm {b})
$$

In SM, the Higgs boson couples with a pair photons/gluons through triangle loops. The  $hAA$  and  $hgg$  vertices can also be induced from high-energy theory, and can be contributed by the effective dimension-6 operators. From the operators  $\mathcal{O}_{WW}$ ,  $\mathcal{O}_{BB}$ , and  $\mathcal{O}_{WB}$  in table 1, the Higgs field  $h$  can directly couple with a pair of photons with the effective coupling,

$$
V _ {h A A} = \frac {4}{v} \delta Z _ {A} f ^ {\mu \nu} [ [ p _ {1}, p _ {2} ], \tag {3.25}
$$

where the momenta are assigned as  $A^{\mu}(p_1)A^{\nu}(p_2)h$ . The operator  $\mathcal{O}_g$  induces the effective coupling,

$$
V _ {h g g} = \frac {4 v}{\Lambda^ {2}} g _ {s} ^ {2} c _ {g} \delta_ {a b} f ^ {\mu \nu} [   [ p _ {1}, p _ {2} ]   ], \tag {3.26}
$$

for the vertex  $g^{\mu}(p_1)g^{\nu}(p_2)h$ . Note that the above tree-level corrections by the dimension-6 operators should be of the same order as the one-loop contributions in the SM.

# 3.3.3 Hybrid couplings between bosons and fermions

The first vertex  $Zh\bar{f} f$  arises from  $(\mathcal{O}_L^{(3)},\mathcal{O}_L,\mathcal{O}_R)$  in table 1,

$$
\frac {g _ {z} v}{\Lambda^ {2}} \left[ \left(c _ {L} ^ {(3)} - c _ {L}\right) Z _ {\mu} \bar {u} _ {L} \gamma^ {\mu} u _ {L} - \left(c _ {L} ^ {(3)} + c _ {L}\right) Z _ {\mu} \bar {d} _ {L} \gamma^ {\mu} d _ {L} - c _ {R} ^ {\psi} \bar {\psi} _ {R} \gamma^ {\mu} \psi_ {R} \right] h. \tag {3.27}
$$

The corresponding Feynman rules are

$$
\bar {u} u Z h: i \frac {g _ {z} v}{\Lambda^ {2}} \gamma^ {\mu} \left[ + \left(c _ {L} ^ {(3)} - c _ {L}\right) P _ {L} - c _ {R} ^ {u} P _ {R} \right], \tag {3.28a}
$$

$$
\bar {d} d Z h: i \frac {g _ {z} v}{\Lambda^ {2}} \gamma^ {\mu} \left[ - \left(c _ {L} ^ {(3)} + c _ {L}\right) P _ {L} - c _ {R} ^ {d} P _ {R} \right]. \tag {3.28b}
$$

Similarly, the vertex  $W^{+}h\bar{f} f^{\prime}$  can arise from  $\mathcal{O}_L^{(3)}$ ,

$$
\frac {\sqrt {2} g v c _ {L} ^ {(3)}}{\Lambda^ {2}} \left(W _ {\mu} ^ {+} \bar {u} _ {L} \gamma^ {\mu} d _ {L} + W _ {\mu} ^ {-} \bar {d} _ {L} \gamma^ {\mu} u _ {L}\right) h. \tag {3.29}
$$

# 4 Probing new physics scales of dimension-6 operators

The dimension-6 operators in table 1 can contribute to a wide range of physical observables, including the electroweak precision observables (EWPO) and the Higgs observables (HO) at a Higgs factory. Using the scheme-independent approach, we can utilize all of them to constrain the dimension-6 operators. Both the EWPO and HO could sensitively probe the new physics at high energy [79-81, 98]. For instance, ref. [79] studied the LHC Run-1 constraints on some dimension-6 operators via measurements of triple gauge couplings, while ref. [80] studied the LEP-I and LEP-II limits on the coefficients of dimension-6 operators. These can probe the new physics scales of dimension-6 operators from roughly a TeV up to about 10 TeV.

In section 4.1 and section 4.2, we first derive the contributions of dimension-6 operators to precision observables  $(\alpha, G_F, M_Z, M_W)$  and Higgs observables (among which two production cross sections  $\sigma(Zh)$  and  $\sigma(h\nu \bar{\nu})$  together with all decay branching fractions can be measured). Then, we use these results, supplemented by the existing precision measurements, to estimate the new physics scales that can be probed at the CEPC in section 4.3. We show the CEPC probe of these new physics scales can reach up to  $10\mathrm{TeV}$ . We continue to elaborate the role of precision observables in section 4.4, and demonstrate that the much more precisely measured  $(\alpha, G_F, M_Z)$  effectively fix the three EW parameters  $(g, g', v)$ , while the less precisely known  $M_W$  helps to enhance the new physics scale limit. The situation changes if  $M_W$  can achieve comparable precision with  $M_Z$  at Higgs factory as demonstrated in section 4.5. We include more precision observables at  $Z$ -pole running of the  $e^+ e^-$  Higgs factory in section 4.6, and demonstrate that the limit on the new physics scale can be further pushed up to around  $30\mathrm{TeV}$ .

# 4.1 New physics contributions to precision observables

The existing best electroweak measurements include the weak gauge boson masses  $(M_W, M_Z)$ , the fine-structure constant  $\alpha$ , and the Fermi constant  $G_F$ . Since they have already been measured experimentally, it is necessary to consider both their central values and uncertainties. To achieve this, we will include the SM loop corrections (which are of the same order as the dimension-6 operators) altogether. In this subsection, we first show how the four precision observables  $(\alpha, G_F, M_Z, M_W)$  are affected by dimension-6 operators via their linear combination and by the SM one-loop corrections via a constant term. Since we have four observables versus three electroweak parameters, only one observable  $(M_W)$  will receive explicit SM loop correction if the other three  $(\alpha, G_F, M_Z)$  are used to fix the renormalization conditions.

# 4.1.1 Fine-structure constant

The fine-structure constant rescales by the photon field redefinition (3.7b),  $\overline{\delta\alpha} / \alpha = 2\delta Z_A$ . In addition, the parameter shift can also induce a correction. Altogether we have,

$$
\frac {\widetilde {\delta \alpha}}{\alpha} \simeq \frac {\delta \alpha}{\alpha} + 0. 0 1 1 1 \left(\frac {c _ {W W}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - \frac {c _ {W B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + \frac {c _ {B B}}{\Lambda_ {\mathrm {T e V}} ^ {2}}\right), \tag {4.1}
$$

where  $\Lambda_{\mathrm{TeV}} \equiv \Lambda / \mathrm{TeV}$  is the cutoff scale in unit of TeV. Since the measurement of the fine-structure constant  $\alpha$  is much more precise than any other observables, fitting data effectively gives  $\widetilde{\delta \alpha} \simeq 0$ . In this sense, the parameter shift  $\delta \alpha$  is always connected to the dimension-6 operator coefficients. Nevertheless, we keep it free at the moment, to give a general expression.

# 4.1.2 Fermi constant

The Fermi constant is modified by the operators  $\mathcal{O}_L^{(3)}$  and  $\mathcal{O}_{LL}^{(3)}$  in table 1, where the latter contributes a contact four-fermion vertex. Thus, we have  $\overline{\delta G_F} /G_F = 2(v^2 /\Lambda^2)(c_{LL}^{(3)} - c_L^{(3)})$ . On the other hand, the effect of the  $W$  field redefinition (3.5) is cancelled by the correction (3.6) to its mass. Including the parameter shift, we deduce the total effect,

$$
\frac {\widetilde {\delta G _ {F}}}{G _ {F}} \simeq \frac {\delta G _ {F}}{G _ {F}} + 0. 1 2 1 \left(\frac {c _ {L L} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - \frac {c _ {L} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}}\right). \tag {4.2}
$$

# 4.1.3 Weak gauge boson masses  $M_W$  and  $M_Z$

The contributions of dimension-6 operators to the  $(W,Z)$  masses have been summarized in eqs. (3.6) and (3.8). Including the parameter shifts, we derive the total contributions,

$$
\frac {\widetilde {\delta M _ {W}}}{M _ {W}} \simeq 0. 1 8 4 \frac {\delta G _ {F}}{G _ {F}} + 1. 3 7 \frac {\delta M _ {Z}}{M _ {Z}} - 0. 1 8 4 \frac {\delta \alpha}{\alpha} + 0. 0 2 6 2 \frac {c _ {W W}}{\Lambda_ {\mathrm {T e V}} ^ {2}}, \tag {4.3a}
$$

$$
\frac {\widetilde {\delta M _ {Z}}}{M _ {Z}} \simeq \frac {\delta M _ {Z}}{M _ {Z}} - 0. 0 3 0 3 \frac {c _ {T}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 2 0 6 \frac {c _ {W W}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 0 1 4 9 \frac {c _ {B B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 0 5 5 5 \frac {c _ {W B}}{\Lambda_ {\mathrm {T e V}} ^ {2}}, \qquad (4. 3 \mathrm {b})
$$

for  $W$  and  $Z$  boson masses, respectively.

To make a consistent fit with the existing data, it is necessary to include the SM radiative corrections. The coefficients of dimension-6 operators belong to the next-to-leading (NLO) order. Up to the linear order of these NLO coefficients, their contributions are independent of the SM loop corrections. Hence, the radiative correction can be computed fully within the SM without involving new ultraviolet divergence. Among the four observables  $(\alpha, G_{F}, M_{Z}, M_{W})$ , three of them can be used to fix the renormalization conditions, while the remaining one receives a constant correction term. For convenience, we follow the convention in [99] by imposing renormalization conditions on the SM predictions of  $(\alpha, G_{F}, M_{Z})$ . Then, up to two-loop level, the  $W$  mass becomes [99],

$$
M _ {W} ^ {2} = M _ {Z} ^ {2} \left\{\frac {1}{2} + \sqrt {\frac {1}{4} - \frac {\pi \alpha}{\sqrt {2} G _ {F} M _ {Z} ^ {2}} [ 1 + \Delta r ]} \right\}. (4. 4)
$$

The contribution of radiative corrections is included in  $\Delta r$ , which is a function of electroweak parameters,  $(\alpha, G_F, M_Z)$ , as well as Higgs mass  $M_h$  and the top quark mass  $M_t$ . Since  $\Delta r$  is already suppressed by loop factors, the effect of varying its arguments is fairly small and negligible up to the linear order. So  $\Delta r$  can be treated as a constant. For convenience, we define,  $\Delta r \equiv \Delta r_1 + \Delta r_2$ , with  $\Delta r_1$  ( $\Delta r_2$ ) denoting one-loop (two-loop) contributions. For  $M_h = 125\mathrm{GeV}$ , the values of  $\Delta r_1$  and  $\Delta r_2$  can be inferred from the table 1 of [99],  $\Delta r_1 = 290.24 \times 10^{-4}$  and  $\Delta r_2 = 72.99 \times 10^{-4}$ . The parameters  $(\alpha, G_F, M_Z)$  have been precisely measured, with precision much better than  $10^{-4}$ , while the radiative corrections  $\Delta r_1 \simeq 4\Delta r_2 = O(10^{-2})$ . So it is a reasonable approximation to expand the corrected  $W$  boson mass (4.4) up to the linear order of  $\delta \alpha$ ,  $\delta G_F$ ,  $\delta M_Z$ ,  $\Delta r_2$ , and the second order of  $\Delta r_1$ ,

$$
M _ {W} = M _ {W} ^ {(r)} \left\{1 + \frac {1}{\cos 2 \theta_ {w}} \left[ c _ {w} ^ {2} \frac {\delta M _ {Z}}{M _ {Z}} + \frac {s _ {w} ^ {2}}{2} \left(\frac {\delta G _ {F}}{G _ {F}} - \frac {\delta \alpha}{\alpha}\right) - \frac {s _ {w} ^ {2}}{2} \Delta r - \frac {s _ {w} ^ {4} (5 c _ {w} ^ {2} - s _ {w} ^ {2})}{8 (c _ {w} ^ {2} - s _ {w} ^ {2}) ^ {2}} \Delta r _ {1} ^ {2} \right] \right\}. (4. 5)
$$

The dependence on the shifts of electroweak parameters remains the same as in eq. (3.6). This is a general feature for any observables. Loop corrections do not change the dependence on the shifts of electroweak parameters up to the linear order, and only contribute as a constant term to the observables. By setting the reference values be the experimental central values [105],  $\alpha^{(r)} = 7.2973525698 \times 10^{-3}$ ,  $G_F^{(r)} = 1.1663787 \times 10^{-5} \mathrm{GeV}^{-2}$ , and  $M_Z^{(r)} = 91.1876 \mathrm{GeV}$ , the  $W$  boson mass is predicted as  $M_W = 80.385 \mathrm{GeV}$ , which equals the current experimental central value [105].

Two remarks are in order. First, in the above discussion we have imposed the renormalization conditions on  $(\alpha, G_F, M_Z)$ . But one is free to choose any other renormalization conditions. The difference caused by using different sets of renormalization conditions only appears at higher order and thus can be ignored at the linear order analysis. Second, since the dependence on parameter shifts  $(\delta \alpha, \delta G_F, \delta M_Z)$  remains the same as going from tree-level to one-loop level and the loop corrections only contribute a constant term, all the expansions derived earlier will continue to hold.

![](images/00fe4661cd7831affd63ba1885351f80332f0c883fb6eef1b22f27f794745b66.jpg)  
(a)

![](images/95e1ec7eb482777076a64e117ab128df6046fe6b5b4cd6ca9c7c8db49d38517d.jpg)  
Figure 1. Feynman diagrams for the Higgsstrahlung process  $e^{+}e^{-}\rightarrow Zh$ , which include contributions of the relevant dimension-6 operators in table 1.  
(b)

# 4.2 New physics contributions to Higgs observables at  $e^{+}e^{-}$  colliders

At future  $e^{+}e^{-}$  colliders (such as the CEPC [41-43], FCC-ee [44-46], and ILC [47-49]), both productions and decays of the Higgs boson can be systematically studied. The Higgs boson with mass  $M_{h} = 125\mathrm{GeV}$  is an ideal case for precision measurement of Higgs decay. If  $M_{h}$  would be either lighter or heavier than  $125\mathrm{GeV}$ , the branching fractions would decrease very fast for some decay channels ( $h \to WW,ZZ$  when  $h$  is too light, or  $h \to \gamma \gamma,gg,ff$  when  $h$  is too heavy). With  $10^{6}$  Higgs bosons to be collected at the CEPC, the Higgs decay into all gauge bosons and fermions ( $b,c,\tau ,\mu$ ) can be measured. Both production and decay rates can help to measure the Higgs coupling with other SM particles. The projected precision of measuring the SM Higgs couplings can be extracted as we will elaborate in appendix 5. In this subsection, we derive the corrections to these processes from new physics as parametrized by the dimension-6 operators in table 1.

# 4.2.1 Higgsstrahlung:  $e^{+}e^{-}\rightarrow Zh$

The Higgsstrahlung process  $e^{+}e^{-}\rightarrow Zh$  is the major production mode of the Higgs boson  $h$  (125GeV) at the Higgs factory with center-of-mass energy  $\sqrt{s} = 240 - 250\mathrm{GeV}$ . Its key advantage is using the recoil mass distribution to make inclusive measurements, regardless of what final-states the Higgs boson decays into. The Higgs event rate can reach about  $10^{6}$  at CEPC (250 GeV) with an integrated luminosity of  $5\mathrm{ab}^{-1}$  [104]. From naive expectation, this cross section could be measured to a precision level about  $\delta N / N\approx 1 / \sqrt{N} = 0.1\%$ . The recent CEPC detector simulations [41-43] give the estimated sensitivity,  $\delta \sigma /\sigma \simeq 0.51\%$ , at  $68\%$  C.L.

In figure 1, we summarize the relevant Feynman diagrams for  $e^{+}e^{-}\rightarrow Zh$  production, which include possible contributions of the dimension-6 operators in table 1. Note that only the first diagram (a) has visible contributions, while other diagrams are negligible due to the tiny Higgs-electron Yukawa coupling. This means that the Higgsstrahlung is mainly mediated by  $s$ -channel gauge boson  $Z_{\mu}$  or  $A_{\mu}$ . The new physics contributions come from corrections to vertices  $Z\psi \bar{\psi}$  (cf. section 3.3.1),  $ZZh$  and  $AZh$  (cf. section 3.3.2), as well as  $Zh\psi \bar{\psi}$  (cf. section 3.3.3). Among these, the first does not introduce new topology since it contributes an overall factor  $\delta(g_L^2 + g_R^2)$  to the SM cross section. This kind of contribution, including field redefinitions which can contribute to the exiting vertices  $Z\psi \bar{\psi}$  and  $ZZh$ , can

be treated as a simple rescaling. The others will either modify the tensor structure of the existing vertex or introduce new vertex. We have systematically derived these contributions for the present study. Since the final state consists of only the on-shell particles  $Zh$ , we can present the results in analytical form. We express the total cross section as a linear combination of the SM contribution and the corrections of dimension-6 operators,

$$
\sigma (Z h) = \left(1 + 2 c _ {0} ^ {Z}\right) \sigma_ {\mathrm {s m}} + \sum_ {j, V} c _ {j} ^ {V} \sigma_ {j} ^ {V}, \tag {4.6a}
$$

where  $c_0^Z$  is defined in eq. (3.18), and  $c_j^V = c_j^Z, c_j^A$  are given by eqs. (3.17) and (3.24). For eq. (4.6a), we derive  $\sigma_{\mathrm{sm}}$  and  $\sigma_j^V$  as follows,

$$
\sigma_ {\mathrm {s m}} = \frac {\left(g _ {R} ^ {2} + g _ {L} ^ {2}\right) g _ {h Z Z} ^ {2}}{4 8 \pi M _ {Z} ^ {2} \sqrt {s}} \frac {P _ {Z} \left(P _ {Z} ^ {2} + 3 M _ {Z} ^ {2}\right)}{\left(s - M _ {Z} ^ {2}\right) ^ {2}}, \tag {4.6b}
$$

$$
\sigma_ {1} ^ {Z} = \frac {\left(g _ {R} ^ {2} + g _ {L} ^ {2}\right) g _ {h Z Z} ^ {2} P _ {Z} E _ {Z}}{8 \pi \left(s - M _ {Z} ^ {2}\right) \left(s - M _ {V} ^ {2}\right)}, \quad \sigma_ {1} ^ {A} = - \frac {g _ {Z Z h} ^ {2} \left(g _ {R} + g _ {L}\right) e}{8 \pi \left(s - M _ {Z} ^ {2}\right) s} E _ {Z} P _ {Z}, \tag {4.6c}
$$

$$
\sigma_ {2} ^ {Z} = - 2 M _ {Z} ^ {2} \sigma_ {\mathrm {s m}}, \tag {4.6d}
$$

$$
\sigma_ {3} ^ {Z} = - 2 s \sigma_ {\mathrm {s m}}, \quad \sigma_ {3} ^ {A} = \frac {2 (g _ {L} + g _ {R}) e}{g _ {L} ^ {2} + g _ {R} ^ {2}} (s - M _ {Z} ^ {2}) \sigma_ {\mathrm {s m}}, \tag {4.6e}
$$

$$
\sigma_ {Z} ^ {\prime} = 2 \frac {g _ {L} \delta f _ {L} + g _ {R} \delta f _ {R}}{\left(g _ {L} ^ {2} + g _ {R} ^ {2}\right) g _ {Z Z h}} (s - M _ {Z} ^ {2}) \sigma_ {\mathrm {s m}}, \tag {4.6f}
$$

where  $(E_Z, P_Z)$  denote (energy,  $|\mathrm{momentum}|$ ) of the final-state  $Z$  boson, and the coefficients  $(c_j^Z, c_j^A)$  are defined in (3.17)-(3.18) as well as (3.24). The corrections to fermionic coupling appear in  $\delta g_L$  and  $\delta g_R$ , as summarized in section 3.3.1. In the last equation (4.6f), the corrections  $\delta f_L = g_z v(c_L^{(3)} + c_L) / \Lambda^2$  and  $\delta f_R = g_z vc_R / \Lambda^2$  are coupling constants of the effective  $\bar{e} e Z h$  vertex discussed in (3.28). Combining everything, we derive the relative corrections to the cross section  $\sigma(Zh)$ ,

$$
\begin{array}{l} \frac {\widetilde {\delta \sigma}}{\sigma} \simeq 2. 3 4 \frac {\delta G _ {F}}{G _ {F}} + 5. 5 1 \frac {\delta M _ {Z}}{M _ {Z}} - 0. 3 4 4 \frac {\delta \alpha}{\alpha} - 0. 0 6 0 5 \frac {c _ {H}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 2 0 6 \frac {c _ {T}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ + 0. 3 3 8 \frac {c _ {W W}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 1 2 2 \frac {c _ {B B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 6 8 2 \frac {c _ {W B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 4 2 9 \frac {c _ {H W}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 0 3 1 5 \frac {c _ {H B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ + 1. 0 2 \frac {c _ {L} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 1. 0 2 \frac {c _ {L}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 7 5 5 \frac {c _ {R}}{\Lambda_ {\mathrm {T e V}} ^ {2}}. \tag {4.7} \\ \end{array}
$$

Comparing the above with the eq. (3.10) of ref. [78], we can see that our coefficient  $c_{T}$  is much larger, due to the fact that we use scheme-independent approach instead of the  $Z$ -scheme. The essential difference between these two approaches is due to the fact that in the  $Z$ -scheme,  $(\alpha, G_{F}, M_{Z})$  are fixed to the measured values. To reproduce the  $Z$ -scheme result from our scheme-independent approach, we can simply set  $\widetilde{\delta\alpha}$  in (4.1),  $\widetilde{\delta G_{F}}$  in (4.2), and  $\widetilde{\delta M_{Z}}$  in (4.3b) to be zero. In this way, the parameter shifts  $(\delta\alpha, \delta G_{F}, \delta M_{Z})$  can be expressed in terms of dimension-6 operator coefficients. Then, implement these

![](images/b205a3d56ee6118019e7be8e1aa8227eda7ff4c4e20a93f123907ba6cf02c343.jpg)  
(a)

![](images/fc987994dbc7ca5e23973515a9a9327783fb975b84c6c5d0c982cada1e73da79.jpg)  
Figure 2. Feynman diagrams for  $WW$  fusion process  $e^{+}e^{-}\rightarrow h\nu \bar{\nu}$ , including contributions of the relevant dimension-6 operators in table 1.  
(b)

![](images/01b75943bd6920b480f323aa8601d8fc3cf93dabca2be8098736f4cea1ce8b16.jpg)  
(c)

![](images/f8fb14b23ac5ded5d993f42e190f2a626ac5af2df7becf94a7094a8f9aa55eaf.jpg)  
(d)

expressions of the parameter shifts into (4.7). After these operations, the coefficient of  $c_{T}$  becomes -0.0397, and agrees well with the value -0.04 in ref. [78].<sup>8</sup>

# 4.2.2 WW fusion:  $e^{+}e^{-}\rightarrow \nu \bar{\nu} h$  at 250 GeV and 350 GeV

The next production mode at the Higgs factory is the  $WW$  fusion process as depicted in figure 2. Since the cross section  $\sigma(\nu \bar{\nu} h)$  at  $\sqrt{s} = 250\mathrm{GeV}$  is about  $1/30$  of  $\sigma(Zh)$  [104], the  $\sigma(\nu \bar{\nu} h)$  can be measured to a precision of  $2.8\%$  at the CEPC [41-43]. Although not as precise as the cross section  $\sigma(Zh)$  of the Higgsstrahlung process, it can provide complementary constraint on the Higgs coupling with  $W$  gauge bosons.

The new physics contributions can be classified into two categories. The first kind is the contribution to the vertex  $WWh$  with fusion topology, as studied in section 3.3.2, which shares the same Feynman diagram figure 2(a) as the SM contribution. Corresponding to the coefficients  $(c_0^W, c_1^W, c_2^W, c_3^W)$  defined in (3.21) and (3.22), we derive the squared  $S$ -matrix elements,

$$
\overline {{| \mathcal {M} | _ {0} ^ {2}}} = \frac {4 g _ {W f f} ^ {4} g ^ {2} M _ {W} ^ {2}}{\left(M _ {W} ^ {2} + 2 p _ {1} \cdot p _ {+}\right) ^ {2} \left(M _ {W} ^ {2} + 2 p _ {2} \cdot p _ {-}\right) ^ {2}} \left(p _ {1} \cdot p _ {-}\right) \left(p _ {2} \cdot p _ {+}\right), \tag {4.8a}
$$

$$
\overline {{| \mathcal {M} | _ {1} ^ {2}}} = \frac {- 2 g _ {V f f} ^ {4} g ^ {2} M _ {W} ^ {2} (p _ {1} \cdot p _ {-} + p _ {2} \cdot p _ {+})}{(M _ {W} ^ {2} + 2 p _ {1} \cdot p _ {+}) ^ {2} (M _ {W} ^ {2} + 2 p _ {2} \cdot p _ {-}) ^ {2}} (2 p _ {1} \cdot p _ {-} p _ {2} \cdot p _ {+} + 2 p _ {1} \cdot p _ {+} p _ {2} \cdot p _ {-} - s p _ {+} \cdot p _ {-}), (4. 8 \mathrm {b})
$$

$$
\overline {{| \mathcal {M} | _ {2} ^ {2}}} = - 2 k _ {+} ^ {2} \overline {{| \mathcal {M} | ^ {2}}} _ {0} = 4 (p _ {2} \cdot p _ {-}) \overline {{| \mathcal {M} | _ {0} ^ {2}}}, \tag {4.8c}
$$

$$
\overline {{| \mathcal {M} | _ {3} ^ {2}}} = - 2 k _ {-} ^ {2} \overline {{| \mathcal {M} | _ {0} ^ {2}}} = 4 (p _ {1} \cdot p _ {+}) \overline {{| \mathcal {M} | _ {0} ^ {2}}}, \tag {4.8d}
$$

where  $p_1$  and  $p_2$  denote the momenta of  $e^+$  and  $e^-$ , while  $p_+$  and  $p_-$  are the momenta of  $\nu$  and  $\bar{\nu}$ , respectively. The zeroth-order term  $|\mathcal{M}|_0^2$  gives the SM contribution. Only  $|\overline{\mathcal{M}}|_1^2$  needs to be evaluated independently, the rest are proportional to the zeroth-order result. For the first diagram, its total effect is  $(1 + 2c_0^W)\sigma_{\mathrm{sm}} + \sum_j c_j\sigma_j$ , with coefficients defined in eqs. (3.21) and (3.22). The second contribution comes from the new vertices in section 3.3.3. Their contribution to the WW fusion is represented by the three new

diagrams figure 2(b)-(d),

$$
\delta | \mathcal {M} _ {W h \ell \bar {\nu}} | ^ {2} = 2 | \mathcal {M} _ {0} | ^ {2} \frac {g _ {W h \ell \bar {\nu}}}{g _ {W e \nu} g _ {h W W}} \left[ (k _ {+} ^ {2} - M _ {W} ^ {2}) + (k _ {-} ^ {2} - M _ {W} ^ {2}) \right], \tag {4.9a}
$$

$$
\delta | \mathcal {M} _ {Z h \nu \bar {\nu}} | ^ {2} = 2 | \mathcal {M} _ {0} | ^ {2} \frac {(k _ {+} ^ {2} - M _ {W} ^ {2}) (k _ {-} ^ {2} - M _ {W} ^ {2})}{s - M _ {z} ^ {2}} \left(- \frac {g _ {Z e e L} g _ {Z h \nu \bar {\nu}}}{g _ {W e \nu} ^ {2} g _ {h W W}}\right), \tag {4.9b}
$$

where  $k_{\pm}$  denotes the momenta of  $W^{\pm}$ . Both contributions come from the interference with the SM contribution  $\mathcal{M}_0$ . For convenience we have denoted the couplings as  $g_{Wh\ell \bar{\nu}} \equiv \sqrt{2} gvc_L^{(3)} / \Lambda^2$ ,  $g_{Zh\nu \bar{\nu}} \equiv g_zv(c_L^{(3)} - c_L) / \Lambda^2$ ,  $g_{ZeeL} \equiv g_z(\frac{1}{2} - s_w^2)$ ,  $g_{We\nu} \equiv g / \sqrt{2}$ , and  $g_{hWW} \equiv g^2 v / 2$ , where  $g_z \equiv g / \cos \theta_w$ . Note that only the left-handed part of the neutral current  $g_{Zee,L}Z_\mu \bar{e}_L\gamma^\mu e_L$  in figure 2(d) can interfere with the SM contribution  $\mathcal{M}_0$ . After combining the two contributions, we derive

$$
\begin{array}{l} 2 5 0 \mathrm {G e V} \colon \frac {\widetilde {\delta \sigma}}{\sigma} \simeq 3. 4 4 \frac {\delta G _ {F}}{G _ {F}} + 3. 2 8 \frac {\delta M _ {Z}}{M _ {Z}} - 0. 4 4 2 \frac {\delta \alpha}{\alpha} - 0. 0 6 0 5 \frac {c _ {H}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ + 0. 0 5 1 5 \frac {c _ {W W}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 1 2 6 \frac {c _ {H W}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 1 5 9 \frac {c _ {L} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 1 3 6 \frac {c _ {L}}{\Lambda_ {\mathrm {T e V}} ^ {2}}, \tag {4.10a} \\ \end{array}
$$

$$
\begin{array}{l} 3 5 0 \mathrm {G e V} \colon \frac {\widetilde {\delta \sigma}}{\sigma} \simeq 3. 5 2 \frac {\delta G _ {F}}{G _ {F}} + 3. 8 9 \frac {\delta M _ {Z}}{M _ {Z}} - 0. 5 2 3 \frac {\delta \alpha}{\alpha} - 0. 0 6 0 5 \frac {c _ {H}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ + 0. 0 5 7 5 \frac {c _ {W W}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 1 8 8 \frac {c _ {H W}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 2 2 6 \frac {c _ {L} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 0 9 1 8 \frac {c _ {L}}{\Lambda_ {\mathrm {T e V}} ^ {2}}, \quad (4. 1 0 \mathrm {b}) \\ \end{array}
$$

for  $\sqrt{s} = 250\mathrm{GeV}$  and  $350\mathrm{GeV}$ , respectively. At  $\sqrt{s} = 350\mathrm{GeV}$ , we see that the Higgs production cross section through  $WW$  fusion has sizable increase, leading to a better measurement of  $\sigma (\nu \bar{\nu} h)$ .

# 4.2.3 Higgs decay into  $Z$  boson pair

For Higgs decay into the  $Z$  boson pair, at least one of them must be off-shell. The decay width can be computed via the corresponding three-body decay process,  $h \rightarrow ZZ^{*} \rightarrow Zf\bar{f}$ . In addition, the double off-shell process  $h \rightarrow Z^{*}Z^{*}$  still contributes  $25\%$  of the partial width and thus should be included via the four-body decay process,  $h \rightarrow Z^{*}Z^{*} \rightarrow f_{1}\bar{f}_{1}f_{2}\bar{f}_{2}$ . We compute the new physics contributions to the Higgs partial width by using FeynRules [100] and MadGraph5 [101]. With these, we derive the following expression,

$$
\begin{array}{l} \frac {\widetilde {\delta \Gamma}}{\Gamma} \simeq 3. 4 2 \frac {\delta G _ {F}}{G _ {F}} - 5. 4 4 \frac {\delta M _ {Z}}{M _ {Z}} - 0. 4 2 0 \frac {\delta \alpha}{\alpha} - 0. 0 6 0 5 \frac {c _ {H}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 1 9 0 \frac {c _ {T}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ - 0. 0 9 6 8 \frac {c _ {W W}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 0 2 5 5 \frac {c _ {B B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 0 5 7 9 \frac {c _ {W B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 1 3 1 \frac {c _ {H W}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 1 4 4 \frac {c _ {H B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ + 0. 0 4 1 0 \frac {c _ {L} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 0 1 1 2 \frac {c _ {L}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 0 0 9 5 7 \frac {c _ {R}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ + 0. 1 0 1 \frac {c _ {L , q} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 2 6 9 \frac {c _ {L , q}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 1 2 8 \frac {c _ {R , u}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 0 0 9 5 7 \frac {c _ {R , d}}{\Lambda_ {\mathrm {T e V}} ^ {2}}. \tag {4.11} \\ \end{array}
$$

The CEPC detector simulations [41-43] show that this decay branching fraction can be measured to the precision of  $4.3\%$ .

# 4.2.4 Higgs decay into  $W$  boson pair

The analysis of this process is similar to that of  $h \to ZZ$ . We use FeynRules [100] and MadGraph5 [101] to numerically compute the new physics contributions to  $h \to WW^*, W^*W^*$  with 3-body and 4-body final states. Altogether, we derive the contributions of the relevant dimension-6 operators to the following,

$$
\begin{array}{l} \frac {\widetilde {\delta \Gamma}}{\Gamma} \simeq 1. 6 4 \frac {\delta G _ {F}}{G _ {F}} - 1 0. 1 \frac {\delta M _ {Z}}{M _ {Z}} + 1. 3 6 \frac {\delta \alpha}{\alpha} - 0. 0 6 0 5 \frac {c _ {H}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ - 0. 2 3 3 \frac {c _ {W W}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 2 2 5 \frac {c _ {H W}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 4 7 9 \frac {c _ {L} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 9 6 8 \frac {c _ {L , q} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}}. \tag {4.12} \\ \end{array}
$$

The branching fraction of  $h \to WW$  can be measured with to  $1.5\%$  accuracy at the CEPC [41-43]. Note that this channel is measured with better precision than  $h \to ZZ$ . This is because  $W$  is lighter than  $Z$ , and hence the  $WW$  channel has much larger branching fraction than the  $ZZ$  channel. This difference in decay rates leads to different precisions which are mainly dominated by statistical fluctuations.

# 4.2.5 Other decay channels

The remaining Higgs decay channels can be divided into two major classes: one with fermionic decay products and the other with massless gauge bosons (photons or gluons). The first class occurs at tree-level, while the second class arises from one-loop level. Both receive contributions from the Higgs field redefinition (3.4),

$$
\frac {\delta \Gamma}{\Gamma} = - 0. 0 6 0 5 \frac {c _ {H}}{\Lambda_ {\mathrm {T e V}} ^ {2}}, \tag {4.13}
$$

which is the only contribution to fermionic decays. The vertex  $f\bar{f}h$  comes from Yukawa interaction which flips chirality and is not affected by either the dimension-6 operators in table 1 or the EW parameters mentioned earlier. On the other hand, the decay into photons has extra contributions. For fermion loop, it is affected by the photon field redefinition (3.7b) only. For bosonic  $W$ -loop, the new physics effects come from  $W$ -mass correction (3.6) and the photon field redefinition (3.7b). Note that the corrections of  $W$ -field redefinition to the vertex and mass should cancel with each other. Since the EW parameters are involved in bosonic decay, their shifts  $(\delta \alpha, \delta G_F, \delta M_Z)$  should also appear. Note that  $h \rightarrow gg$  only has fermionic contributions.

Furthermore, dimension-6 operators induce direct coupling of the Higgs field  $h$  with photons or gluons, as shown in eqs. (3.25) and (3.26), respectively. Thus, we derive the following  $hAA$  and  $hgg$  couplings,

$$
\mathcal {M} _ {h A A} = \frac {4}{v} \delta Z _ {A} f ^ {\mu \nu} [ [ p _ {1}, p _ {2} ] ] \epsilon_ {1 \mu} \epsilon_ {2 \nu}, \tag {4.14a}
$$

$$
\mathcal {M} _ {h g g} = \frac {4 v}{\Lambda^ {2}} g _ {s} ^ {2} c _ {g} f ^ {\mu \nu} [   [ p _ {1}, p _ {2} ]   ] \delta_ {a b} \epsilon_ {1 \mu} \epsilon_ {2 \nu}. \tag {4.14b}
$$

We may compare them with the corresponding SM-loop results,

$$
\mathcal {M} _ {h A A} ^ {\mathrm {s m}} = \frac {e ^ {2}}{8 \pi^ {2} v} \left(F _ {W} + \sum N _ {c} Q _ {f} ^ {2} F _ {f}\right) f ^ {\mu \nu} [ [ p _ {1}, p _ {2} ] ] \epsilon_ {1 \mu} \epsilon_ {2 \nu}, \qquad (4. 1 5 \mathrm {a})
$$

$$
\mathcal {M} _ {h g g} ^ {\mathrm {s m}} = \frac {\alpha_ {s}}{4 \pi v} F _ {f} f ^ {\mu \nu} [ [ p _ {1}, p _ {2} ] ] \delta_ {a b} \epsilon_ {1 \mu} \epsilon_ {2 \nu}, (4. 1 5 \mathrm {b})
$$

$$
F _ {W} \equiv 2 + 3 \tau_ {W} ^ {- 1} [ 1 + (2 - \tau_ {W} ^ {- 1}) f (\tau_ {W}) ], \tag {4.15c}
$$

$$
F _ {f} \equiv - 2 \tau_ {f} ^ {- 1} \left[ 1 + \left(1 - \tau_ {f} ^ {- 1}\right) f (\tau_ {f}) \right], \tag {4.15d}
$$

where  $\tau_{j}\equiv M_{h}^{2} / (4M_{j}^{2})$  and  $f(\tau_j)\equiv (\arcsin \sqrt{\tau_j})^2$ , with  $j = W,t$ . Combining everything together, we derive the total corrections,

$$
\frac {\delta \Gamma_ {A A}}{\Gamma_ {A A}} = 0. 9 9 7 \frac {\delta G _ {F}}{G _ {F}} + 2 \frac {\delta \alpha}{\alpha} - 0. 0 2 1 8 \frac {\delta M _ {Z}}{M _ {Z}} - 0. 0 6 0 5 \frac {c _ {H}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 5. 9 1 \frac {c _ {W W} - c _ {W B} + c _ {B B}}{\Lambda_ {\mathrm {T e V}} ^ {2}}, \tag {4.16a}
$$

$$
\frac {\delta \Gamma_ {g g}}{\Gamma_ {g g}} = \frac {\delta G _ {F}}{G _ {F}} - 0. 0 6 0 5 \frac {c _ {H}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 5 5. 2 \frac {c _ {g}}{\Lambda_ {\mathrm {T e V}} ^ {2}}, \tag {4.16b}
$$

for  $\Gamma_{AA}$  and  $\Gamma_{gg}$ , respectively. We note that the coefficients of the last terms in both (4.16a) and (4.16b) come from the interference between the SM prediction (4.15) and the contribution (4.14) by dimension-6 operators. Although the SM predictions of  $h\rightarrow gg$  and  $h\rightarrow \gamma \gamma$  arise from loop-level and are expected to be of the same order as that of dimension-6 operators, it is well justified to make expansion up to the linear terms of  $c_{g}$  and  $(c_{WW},c_{WB},c_{BB})$ . This is because the current LHC data constrain the deviations from the SM predictions within about  $20\%$  at  $2\sigma$  level [102, 103], and the future Higgs factory sensitivities to such deviations are even much smaller (table 2 in section 4.3 and figure 5 in appendix 5). Hence, the dimension-6 contributions can be well treated as small perturbations up to the linear order.

# 4.3 Probing new physics scales at Higgs factory

As discussed in section 4.1 and section 4.2, the dimension-6 effective operators can modify both EW precision observables (EWPO) and Higgs observables (HO). The EWPO have been precisely measured at the LEP and Tevatron with high precision, while the HO can be measured at the future Higgs factory under planning. Currently, there are three major candidates of Higgs factory, CEPC [41-43], FCC-ee [44-46], and ILC [47-49], which can run at the collision energies around  $240 - 250\mathrm{GeV}$ . They can measure the Higgs production cross sections and decay branching fractions with precisions at percentage level. This provides important means to indirectly probe the scales of new physics. In the following, we study how the EWPO and HO can probe the new physics scales via effective dimension-6 operators and the interplay with each other.

For convenience, we first summarize the inputs for our analysis in table 2. Since the EWPO have already been measured, we list both their central values and relative errors. These four observables are the most precisely measured ones. Especially, the fine-structure constant  $\alpha$  is measured with unprecedented precision of  $\delta \alpha / \alpha = 3.29 \times 10^{-10}$ ,

Table 2. Inputs used to constrain the new physics scales of dimension-6 operators. The electroweak precision observables in the first four rows are taken from PDG [105], and the estimated precisions of Higgs measurements (68% C.L.) are given by the CEPC detector simulations [41-43]. For the WW fusion cross section  $\sigma[\nu \bar{\nu} h]_{350\mathrm{GeV}}$  at  $\sqrt{s} = 350\mathrm{GeV}$ , we adopt the FCC-ee (TLEP) estimation [44-46] for illustration. For the "Measurements" entry, the number inside the parentheses stands for experimental uncertainty.  

<table><tr><td>Observables</td><td>Measurements</td><td>Relative Error</td><td>SM Prediction</td></tr><tr><td>MZ</td><td>91.1876(21) GeV</td><td>2.3 × 10-5</td><td>—</td></tr><tr><td>MW</td><td>80.385(15) GeV</td><td>1.87 × 10-4</td><td>—</td></tr><tr><td>GF</td><td>1.1663787(6) × 10-5GeV-2</td><td>5.14 × 10-7</td><td>—</td></tr><tr><td>α</td><td>7.2973525698(24) × 10-3</td><td>3.29 × 10-10</td><td>—</td></tr><tr><td>σ[Zh]</td><td>—</td><td>0.50%</td><td>—</td></tr><tr><td>σ[ννh]</td><td>—</td><td>2.86%</td><td>—</td></tr><tr><td>σ[ννh]350GeV</td><td>—</td><td>0.75%</td><td>—</td></tr><tr><td>Br[WW]</td><td>—</td><td>1.2%</td><td>22.5%</td></tr><tr><td>Br[ZZ]</td><td>—</td><td>4.3%</td><td>2.77%</td></tr><tr><td>Br[bb]</td><td>—</td><td>0.54%</td><td>58.1%</td></tr><tr><td>Br[cc]</td><td>—</td><td>2.5%</td><td>2.10%</td></tr><tr><td>Br[gg]</td><td>—</td><td>1.4%</td><td>7.40%</td></tr><tr><td>Br[ττ]</td><td>—</td><td>1.1%</td><td>6.64%</td></tr><tr><td>Br[γγ]</td><td>—</td><td>9.0%</td><td>0.243%</td></tr><tr><td>Br[μμ]</td><td>—</td><td>17%</td><td>0.023%</td></tr></table>

much better than all the others. According to its expression (4.1), one degrees of freedom can be effectively eliminated. This is also true for the Fermi constant  $G_{F}$ , whose precision  $\delta G_{F} / G_{F} = 5.14 \times 10^{-7}$  is just next to that of  $\alpha$ .

For the Higgs observables, table 2 summarizes the estimated precisions at the CEPC [41-43]. The production cross sections and branching fractions are independent of each other. Nevertheless, the decay widths (4.11)-(4.12) for Higgs decays into  $ZZ$  and  $WW$  bosons cannot be directly used to compare with the branching fraction precisions in table 2. The decay width for a specific channel competes with all other channels, so its corresponding branching fraction is given by  $\mathrm{Br}_j\equiv \Gamma_j / \Gamma$ , where  $\Gamma \equiv \sum_{k}\Gamma_{k}$  is the total decay width. Each partial width can be expressed as  $\Gamma_j\equiv \Gamma_j^{(r)}(1 + \delta \Gamma_j / \Gamma_j)$  with  $\delta \Gamma_{j}$  denoting the deviation from the reference point. When expanded to linear order, the decay branching fraction becomes,

$$
\mathrm {B r} _ {j} \simeq \mathrm {B r} _ {j} ^ {(r)} \left[ 1 + \left(1 - \mathrm {B r} _ {j} ^ {(r)}\right) \frac {\delta \Gamma_ {j}}{\Gamma_ {j}} - \sum_ {k \neq j} \mathrm {B r} _ {k} ^ {(r)} \frac {\delta \Gamma_ {k}}{\Gamma_ {k}} \right]. \tag {4.17}
$$

The corrections to Higgs partial width affect not only its own branching fraction, but also

all the others. Eq. (4.17) shows that for the branching fraction  $\mathrm{Br}_j$ , the contribution due to its own channel is modulated by  $1 - \mathrm{Br}_j^{(r)}$ , while other channels by the corresponding  $\mathrm{Br}_k^{(r)}$ . Since the reference value is around the SM prediction,  $\mathrm{Br}_j^{(r)} \approx \mathrm{Br}_j^{\mathrm{sm}}$ , the modulation is essentially controlled by the SM predictions. In this way, the precision measurements of branching fractions at CEPC will constrain the new physics scales via  $\delta \Gamma_j$  term and  $\delta \Gamma_k$  term.

The observables in table 2 can be used to constrain the electroweak parameters ( $\delta \alpha$ ,  $\delta G_{F}$ ,  $\delta M_{Z}$ ) and the coefficients of dimension-6 operators simultaneously. This can be achieved by the so-called  $\chi^2$  fit technique. As described in appendix B, the  $\chi^2$  function sums over all experimental observables  $\mathcal{O}_j$ ,

$$
\chi^ {2} \left(\delta \alpha , \delta G _ {F}, \delta M _ {Z}, \frac {c _ {i}}{\Lambda^ {2}}\right) = \sum_ {j} \left[ \frac {\mathcal {O} _ {j} ^ {\mathrm {t h}} \left(\delta \alpha , \delta G _ {F} , \delta M _ {Z} , \frac {c _ {i}}{\Lambda^ {2}}\right) - \mathcal {O} _ {j} ^ {\mathrm {e x p}}}{\Delta \mathcal {O} _ {j}} \right] ^ {2}, \tag {4.18}
$$

where the theoretical predictions are functions of the fitting parameters. The  $\chi^2$  function reaches its minimal value at the best fit values of  $(\delta \alpha, \delta G_F, \delta M_Z)$  and  $c_i / \Lambda^2$ . Using the linear  $\chi^2$  fitting method shown in appendix B, we can perform this fit analytically with the package BSMfitter [106]. As usual, for simplicity, we will consider only one dimension-6 effective operator to be nonzero during each fit, and turn off the others. Thus, each fit will deal with only four fitting parameters,  $(\delta \alpha, \delta G_F, \delta M_Z)$  and one dimension-6 coefficient  $c_i / \Lambda^2$ .

In figure 3, we present the lower limit on the new physics scale of each dimension-6 operator by combining the existing electroweak precision measurements and future Higgs measurements at the CEPC with  $\sqrt{s} = 250\mathrm{GeV}$ . We see that it can probe the new physics scales up to about  $12\mathrm{TeV}$  for  $\mathcal{O}_L^{(3)}$  at  $95\%$  C.L.

For the operators listed in table 1,  $(\mathcal{O}_T,\mathcal{O}_{LL}^{(3)},\mathcal{O}_L^{(3)},\mathcal{O}_{L,R},\mathcal{O}_g)$  are among the first group to be sensitively probed. Roughly speaking, they can be probed up to the new physics scales (8 - 10) TeV. The second group consists  $(\mathcal{O}_H,\mathcal{O}_{WW},\mathcal{O}_{BB},\mathcal{O}_{WB},\mathcal{O}_{HW},\mathcal{O}_{Lq}^{(3)})$ , which can be probed up to the scales (2 - 5) TeV. The others operators,  $(\mathcal{O}_{HB},\mathcal{O}_{Lq},\mathcal{O}_{Ru},\mathcal{O}_{Rd})$  cannot be probed above the 1 TeV scale. We note that the strong constraint on  $\mathcal{O}_T$  mainly comes from the  $W$  boson mass  $M_W$ . Including electroweak precision observables can significantly improve the probe of new physics scales, as we will fully elaborate in following section 4.4 and section 4.5. The remaining constraints come from measuring the Higgs production and decay rates, most of which is provided by the Higgsstrahlung process. For the gluonic operator  $\mathcal{O}_g$ , its constraint is mainly given by the branching fraction of  $h\rightarrow gg$  which is the only relevant channel here. Although this is not the major Higgs decay channel, with the SM prediction  $\mathrm{Br}[gg] = 7.4\%$ , it can put severe constraint on the scale of  $\mathcal{O}_g$ , as high as about 43.8 TeV (cf. figure 3). Since in the SM the Higgs coupling with gluons arises at one-loop level and the dimension-6 operator  $\mathcal{O}_g$  contributes to this coupling at tree-level, so the scale of  $\mathcal{O}_g$  has to be high enough to suppress the deviation from the SM loop prediction. This is expected since the operator  $\mathcal{O}_g$  may well be induced from loop-level in a given underlying theory and thus its coefficient  $c_{g}$  will be suppressed by the corresponding loop-factor.

![](images/a52898aa853d692d5e2bb2a4bad7ce8edef875585ad9275bf413865e0adcd568.jpg)  
Figure 3. The  $95\%$  exclusion limits (blue) and  $5\sigma$  discovery sensitivities (red) to the new physics scales  $\Lambda/\sqrt{|c_j|}$  by combining the current electroweak precision observables ( $\alpha$ ,  $G_F$ ,  $M_Z$ ,  $M_W$ ) [105] and the future Higgs observables (table 2) at the Higgs factory CEPC (250 GeV) [41-43] with a projected luminosity of  $5\mathrm{ab}^{-1}$ . In the last column for  $\mathcal{O}_g$ , we have rescaled its height by a factor  $1/4$  to fit the plot, so its actual reach is  $\Lambda/\sqrt{|c_g|} = 43.8\mathrm{TeV}$ .

Note that figure 3 contains more fermionic operators than listed in table 1 since quark and lepton can provide different contributions. For a specific operator, we assume the same operator coefficient for the three generations of fermions. Consequently, each of the operators involving left-handed fermions,  $(\mathcal{O}_{LL}^{(3)},\mathcal{O}_L^{(3)},\mathcal{O}_L)$ , has two copies, one for leptons and the other for quarks (with extra subscript " $q$ "). On the other hand, the operator  $\mathcal{O}_R$  that contains the right-handed fermions has three copies, one for charged leptons and the other two for quarks (with subscripts " $u$ ” for up- and " $d$ ” for down-type quarks). We can see that leptonic operators are generally better constrained than those of quarks, since the former can enter the most precisely measured Higgsstrahlung process, and the latter can only be constrained by Higgs decays into  $WW$  and  $ZZ$  with limited branching fractions and statistics. Although the Higgs decay mode  $h\rightarrow b\bar{b}$  has the largest branching fraction, it is not connected to the fermionic operators shown in table 1.

For clarity, in table 3, we further present the numerical limits of figure 3 at both  $95\%$  and  $5\sigma$  confidence levels. The  $95\%$  limit corresponds to the exclusion reach, while  $5\sigma$  limits gives the discovery reach. Since the results are obtained after reducing to one-dimensional Gaussian distribution by marginalization (see appendix B for detail), the value of the  $5\sigma$  reach on the new physics scale equals  $39\%$  of the corresponding  $95\%$  confidence limit.

Note that these results are obtained with all Higgs observables to be measured at  $\sqrt{s} = 250\mathrm{GeV}$ . If the collision energy is upgraded to  $350\mathrm{GeV}$ , the cross section of the WW

Table 3. New physics scales  $\Lambda/\sqrt{|c_j|}$  (in TeV) which can be probed by combining the current electroweak precision tests on  $(\alpha, G_F, M_Z, M_W)$  [105] and the future Higgs measurements on  $(\sigma(Zh), \sigma(\nu \bar{\nu} h)$ , and branching fractions) at the Higgs factory CEPC (250 GeV) [41-43] with a projected luminosity of  $5\mathrm{ab}^{-1}$ . The sensitivities are presented as the  $95\%$  exclusions (first row) and the  $5\sigma$  discoveries (second row), respectively.  

<table><tr><td>O_H</td><td>O_T</td><td>O_WW</td><td>O_BB</td><td>O_WB</td><td>O_HW</td><td>O_HB</td><td>O_(3)LL</td><td>O_(3)L</td><td>O_L</td><td>O_R</td><td>O_(3)L,q</td><td>O_L,q</td><td>O_R,u</td><td>O_R,d</td><td>O_g</td></tr><tr><td>2.5</td><td>10.6</td><td>6.38</td><td>5.78</td><td>6.53</td><td>2.12</td><td>0.604</td><td>8.23</td><td>12.1</td><td>10.2</td><td>8.78</td><td>2.06</td><td>0.568</td><td>0.393</td><td>0.339</td><td>43.8</td></tr><tr><td>1.57</td><td>6.65</td><td>4.00</td><td>3.62</td><td>4.09</td><td>1.33</td><td>0.378</td><td>5.15</td><td>7.57</td><td>6.39</td><td>5.49</td><td>1.29</td><td>0.356</td><td>0.246</td><td>0.212</td><td>27.4</td></tr></table>

fusion process for Higgs production will increase significantly. This can help to enhance the sensitivity to the scale of  $\mathcal{O}_H$  by about  $10\%$ , as will be shown in the first column of table 6, while the others remain the same.

# 4.4 Combining with electroweak precision observables

For comparison, we note that the  $Z$ -scheme is adopted in the recent studies [78] and [81], where the latter also invokes the  $W$  mass measurement at a Higgs factory. In this scheme, not all the electroweak parameters, especially the most precisely measured ones  $(\alpha, G_{F}, M_{Z})$ , were included in their analysis. After incorporating the electroweak precision measurements, including also  $M_{W}$ , the reach of new physics scales [81] becomes higher than the one with the  $\sigma(Zh)$  constraints alone [78]. Although the  $M_{W}$  measurement is also used in [81], its interplay with  $M_{Z}$  could not be studied within the  $Z$ -scheme. In this subsection, we first study the role of electroweak precision observables (EWPO) with the current data [105]. We will further analyze the interplay of including a significantly improved  $M_{W}$  measurement in section 4.5.

Among the existing EWPO, the most precisely measured observables are  $\alpha$ ,  $G_{F}$ , and  $M_Z$ , in the order of their relative uncertainties, as shown in table 2. Even the least precise one,  $M_Z$ , is much better measured than the other mass  $M_W$  by about one order of magnitude. This hierarchical structure in the relative uncertainties makes it appropriate to treat  $(\alpha, G_F, M_Z)$  as inputs to fix the electroweak parameters  $(g, g', v)$ , and implement the  $M_W$  measurement into the fit. As we discussed in section 4.2.1, this is equivalent to setting  $(\widetilde{\delta\alpha}, \widetilde{\delta G_F}, \widetilde{\delta M_Z}) = 0$ , from which  $(\delta\alpha, \delta G_F, \delta M_Z)$  can be solved in terms of dimension-6 operator contributions. With these extra constraints (which is exactly the definition of  $Z$ -scheme) implemented into (4.3a), we derive the  $W$  mass correction as

$$
\widetilde {\frac {\delta M _ {W}}{M _ {W}}} = 0. 0 4 1 4 \frac {c _ {T}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 0 0 9 6 4 \frac {c _ {W B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 0 2 2 3 \frac {c _ {L L} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 2 2 3 \frac {c _ {L} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}}, \tag {4.19}
$$

which is a function of the coefficients of dimension-6 operators alone. In eq. (4.19), even though the coefficients of the  $c_{T}$  and  $c_{L}$  terms are not sizable, after imposing the experimental data  $M_W = 80.385 \times (1 \pm 1.87 \times 10^{-4}) \mathrm{GeV}$  (which is much more precise than the Higgs observables to be measured at the future Higgs factory), we can estimate the limit on the new physics scale to be  $\Lambda / \sqrt{|c_T|} > 14.9$  (7.59) TeV at  $1\sigma$  (95% C.L.). This demonstrates significant improvement of the new physics reach from the precision measurements of the

Table 4. Impacts of adding the current electroweak precision observables  $(\alpha, G_F, M_Z, M_W)$  [105] on probing the new physics scales  $\Lambda / \sqrt{|c_j|}$  (in TeV) at  $95\%$  C.L. The limits in the first row are obtained from  $\sigma(Zh)$  to be measured at the CEPC [41-43] only. The limits in the second row are given by combining with the current  $M_W$  measurement plus  $\sigma(Zh)$ . Finally, the third row presents the limits by including the current measurements of  $(\alpha, G_F, M_Z)$  altogether. In the first two rows,  $(\alpha, G_F, M_Z)$  are fixed to their experimental central values as in the  $Z$ -scheme, while the third row adopts the scheme-independent approach by allowing all electroweak parameters to freely vary in each fit. We label the entries of most significant improvements in red color with an underscore.  

<table><tr><td>O_H</td><td>O_T</td><td>O_WW</td><td>O_BB</td><td>O_WB</td><td>O_HW</td><td>O_HB</td><td>O_(3)LL</td><td>O_(3)L</td><td>O_L</td><td>O_R</td></tr><tr><td>2.48</td><td>2.01</td><td>4.83</td><td>0.89</td><td>1.86</td><td>2.09</td><td>0.567</td><td>5.38</td><td>11.6</td><td>10.2</td><td>8.78</td></tr><tr><td>2.48</td><td>10.6</td><td>4.83</td><td>0.89</td><td>5.16</td><td>2.09</td><td>0.567</td><td>8.22</td><td>12.1</td><td>10.2</td><td>8.78</td></tr><tr><td>2.48</td><td>10.6</td><td>4.83</td><td>0.875</td><td>5.12</td><td>2.09</td><td>0.567</td><td>8.15</td><td>12.1</td><td>10.2</td><td>8.78</td></tr></table>

Table 5. Projected precisions (68% C.L.) of  $Z$  and  $W$  mass measurements to be achieved at the CEPC [41-43, 107].  

<table><tr><td>Observables</td><td>Relative Error</td><td>Absolute Error</td></tr><tr><td>MZ</td><td>(0.55 – 1.1) × 10-5</td><td>(0.5 – 1) MeV</td></tr><tr><td>MW</td><td>(3.7 – 6.2) × 10-5</td><td>(3 – 5) MeV</td></tr></table>

EWPO. After further including the CEPC measurement of  $\sigma(Zh)$ , we find the improved limit,  $\Lambda / \sqrt{|c_T|} > 10.6 \mathrm{TeV}$  at  $95\%$  C.L., as shown in table 4.

In table 4, the first two rows are essentially  $Z$ -scheme approach with  $(\alpha, G_F, M_Z)$  fixed. Here we see whether including the current  $M_W$  measurement or not leads to significant difference. The change appears in the probed new physics scales of the four operators  $\mathcal{O}_T$ ,  $\mathcal{O}_{WB}$ ,  $\mathcal{O}_{LL}^{(3)}$ , and  $\mathcal{O}_L^{(3)}$ , which are involved in the  $Z$ -scheme correction (4.19). For them, the most significant changes come from  $\mathcal{O}_T$  and  $\mathcal{O}_{WB}$ , since the reaches of the corresponding new physics scales are enhanced by about a factor of 5 and 3, respectively. It shows that for  $\mathcal{O}_T$ , the probe of its new physics scale is enhanced from 2.01 TeV to 10.6 TeV once  $M_W$  measurement is included. Setting the most precisely measured observables  $(\alpha, G_F, M_Z)$  be their experimental central values is equivalent to fixing the electroweak observables. This justifies the  $Z$ -scheme approach when the precisions of  $(\alpha, G_F, M_Z)$  are much higher than the others. In section 4.5, we will further analyze how the situation changes when the precisions of  $M_Z$  and  $M_W$  measurements become comparable with each other.

# 4.5 Enhanced sensitivity from CEPC measurements of  $W / Z$  masses

Lepton colliders such as the CEPC, FCC-ee and ILC can also make  $Z$ -pole measurements, which are necessary for calibrations at the initial stage of running the machine. To make full use of the  $Z$ -pole running, we can utilize the  $Z$ -pole data to further enhance the indirect probe of new physics scales. The most significant improvements include the weak boson masses  $M_Z$  and  $M_W$ , as shown in table 5 for the CEPC.

Table 6. Impacts of the projected  $M_Z$  and  $M_W$  measurements at CEPC [41-43, 107] on the reach of new physics scale  $\Lambda / \sqrt{|c_j|}$  (in TeV) at 95% C.L. The Higgs observables (including  $\sigma(\nu \bar{\nu} h)$  at 350 GeV) and the existing electroweak precision observables (table 2) are always included in each row. The differences among the four rows arise from whether taking into account the measurements of  $M_Z$  and  $M_W$  (table 5) or not. The second (third) row contains the measurement of  $M_Z(M_W)$  alone, while the first (last) row contains none (both) of them. We mark the entries of the most significant improvements from  $M_Z$  and/or  $M_W$  measurements in red color with an underscore.  

<table><tr><td>O_H</td><td>O_T</td><td>O_WW</td><td>O_BB</td><td>O_WB</td><td>O_HW</td><td>O_HB</td><td>O_(3)L</td><td>O_(3)L</td><td>O_L</td><td>O_R</td><td>O_(3)L,q</td><td>O_L,q</td><td>O_R,u</td><td>O_R,d</td><td>O_g</td></tr><tr><td>2.74</td><td>10.6</td><td>6.38</td><td>5.78</td><td>6.53</td><td>2.16</td><td>0.604</td><td>8.58</td><td>12.1</td><td>10.2</td><td>8.78</td><td>2.06</td><td>0.568</td><td>0.393</td><td>0.339</td><td>43.8</td></tr><tr><td>2.74</td><td>10.7</td><td>6.38</td><td>5.78</td><td>6.54</td><td>2.16</td><td>0.604</td><td>8.62</td><td>12.1</td><td>10.2</td><td>8.78</td><td>2.06</td><td>0.568</td><td>0.393</td><td>0.339</td><td>43.8</td></tr><tr><td>2.74</td><td>21.0</td><td>6.38</td><td>5.78</td><td>10.4</td><td>2.16</td><td>0.604</td><td>15.5</td><td>16.4</td><td>10.2</td><td>8.78</td><td>2.06</td><td>0.568</td><td>0.393</td><td>0.339</td><td>43.8</td></tr><tr><td>2.74</td><td>23.7</td><td>6.38</td><td>5.78</td><td>11.6</td><td>2.16</td><td>0.604</td><td>17.4</td><td>18.1</td><td>10.2</td><td>8.78</td><td>2.06</td><td>0.568</td><td>0.393</td><td>0.339</td><td>43.8</td></tr></table>

In comparison with the existing precision data shown in the first block of table 2, we see that the uncertainties of  $M_Z$  and  $M_W$  can be further improved by a factor of  $2 - 4$  and  $3 - 5$ , respectively. Since the constraints from current precision measurements are already rather sensitive, we can expect more significant enhancements by imposing the CEPC measurements. A rough estimate leads us to expect that the sensitivity to new physics scales could be doubled for operators  $\mathcal{O}_T$  and  $\mathcal{O}_L$ , reaching about  $20\mathrm{TeV}$ .

In table 6, we quantitatively analyze the impacts of imposing the  $Z$ -pole measurements of  $M_Z$  and  $M_W$  at the CEPC. In the following analysis, we implement the relative errors  $8.25 \times 10^{-6}$  for  $M_Z$  and  $3.7 \times 10^{-5}$  for  $M_W$  as an illustration. Here, we see that the relative errors of  $M_Z$  and  $M_W$  become comparable with each other. Including  $M_Z$  alone makes no significant improvement. As we demonstrated in table 4 and the related discussions, the effect of inputting the precision data  $M_Z$  is to fix one of the three electroweak parameters. Adding a better measurement of  $M_Z$  would not change this picture, except to further enhance it. On the other hand, imposing the CEPC measurement of  $M_W$  alone can significantly improve the reach of new physics scales. This increases the sensitivities to the scales of  $\mathcal{O}_T$ ,  $\mathcal{O}_{WB}$ ,  $\mathcal{O}_L$ , and  $\mathcal{O}_{LL}^{(3)}$  by about a factor of two, as shown in the third row of table 6. This result is consistent with what we have observed in table 4. A new point is that further imposing the CEPC measurement of  $M_Z$ , after imposing  $M_W$ , can introduce extra improvement, although adding the CEPC measurement of  $M_Z$  alone cannot. It demonstrates the fact that when the precisions of  $M_Z$  and  $M_W$  are comparable with each other, it is no longer appropriate to just pick up the three observables to fix the three electroweak variables. In other words,  $Z$ -scheme is a good approximation when the relative errors of  $(\alpha, G_F, M_Z)$  are all much smaller than the others. This appears no longer the case at future lepton colliders. Here, we use the projected CEPC sensitivities to  $M_Z$  and  $M_W$  [41-43, 107] as an illustration, and we have demonstrated that the present scheme-independent approach is a more general-purpose method. In the conventional  $Z$ -scheme,  $M_Z$  is commonly fixed to the experimental central value, so that the above improvement is impossible.

Table 7. Projected precisions (68% C.L.) of  $Z$  -pole measurements at the CEPC [41-43, 107].  

<table><tr><td>Observables</td><td>Relative Error</td></tr><tr><td>Nν</td><td>1.8 × 10-3</td></tr><tr><td>AFB(b)</td><td>1.5 × 10-3</td></tr><tr><td>Rb</td><td>8 × 10-4</td></tr><tr><td>Rμ</td><td>5 × 10-4</td></tr><tr><td>Rτ</td><td>5 × 10-4</td></tr><tr><td>sin2θW</td><td>1 × 10-4</td></tr></table>

# 4.6 Enhancement from  $Z$ -pole observables at CEPC

In addition to the mass measurements of  $W$  and  $Z$ , CEPC can also measure the  $Z$  boson lineshape at the  $Z$ -pole,  $\sqrt{s} = M_Z$ . Currently, there are six observables that have been simulated at CEPC [41-43, 107]. For convenience, we summarize them in table 7, in the order of their relative precisions.

In comparison with the existing measurements of LEP [105], CEPC can improve the accuracy by at least one order of magnitude. The relative errors of the projected CEPC measurements range from  $1.8 \times 10^{-3}$  to  $10^{-4}$  as shown in table 7. Although these relative errors appear larger than those of the mass measurements for  $Z$  and  $W$  bosons, they are still much smaller than the Higgs observables listed in table 2. The most sensitive Higgs observable at the CEPC is the production cross section  $\sigma(Zh)$ , which can be measured to the precision of  $0.51\%$ . We can expect a much more improved constraint on the new physics scales by using the  $Z$ -pole observables.

For this analysis, we derive the linearly expanded expressions for the new physics contributions to the observables shown in table 7. We use the analytical formulae of these observables given in [108]. The new physics enters these observables through the parameter shifts of the involved vertices between the  $Z$  boson and fermions. Since the deviations from the SM predictions should be reasonably small, we can expand the parameter shifts up to the linear order. For convenience, we present the expanded expressions as follows,

$$
\begin{array}{l} \frac {\delta \widetilde {N _ {\nu}}}{N _ {\nu}} = 2 \frac {\delta G _ {F}}{G _ {F}} + 5 \frac {\delta M _ {Z}}{M _ {Z}} - 0. 0 9 0 8 \frac {c _ {T}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ + 0. 1 0 3 \frac {c _ {W W}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 0 7 4 7 \frac {c _ {B B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 2 7 7 \frac {c _ {W B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 1 2 1 \frac {c _ {L L} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 1 2 1 \frac {c _ {L}}{\Lambda_ {\mathrm {T e V}} ^ {2}}, (4. 2 0 \mathrm {a}) \\ \end{array}
$$

$$
\begin{array}{l} \frac {\delta \widetilde {A _ {F B} (b)}}{A _ {F B} (b)} = 7. 5 \frac {\delta G _ {F}}{G _ {F}} + 1 5 \frac {\delta M _ {Z}}{M _ {Z}} - 7. 5 \frac {\delta \alpha}{\alpha} + 0. 3 9 1 \frac {c _ {W W}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 0 4 8 8 \frac {c _ {B B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 0 3 8 \frac {c _ {W B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ + 0. 3 2 4 \frac {c _ {L} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 3 2 4 \frac {c _ {L}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 4 4 \frac {c _ {R}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ - 0. 0 0 7 6 6 \frac {c _ {L , q} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 0 7 6 6 \frac {c _ {L , q}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 4 6 5 \frac {c _ {R , d}}{\Lambda_ {\mathrm {T e V}} ^ {2}}, \tag {4.20b} \\ \end{array}
$$

$$
\begin{array}{l} \frac {\delta \widetilde {R _ {b}}}{R _ {b}} = - 0. 0 6 5 8 \frac {\delta G _ {F}}{G _ {F}} - 0. 1 1 7 \frac {\delta M _ {Z}}{M _ {Z}} + 0. 0 6 5 8 \frac {\delta \alpha}{\alpha} - 0. 0 0 0 4 5 1 \frac {c _ {T}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ + 0. 0 0 2 6 8 \frac {c _ {W W}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 0 0 8 7 2 \frac {c _ {B B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 0 1 9 8 \frac {c _ {W B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ - 0. 0 9 7 6 \frac {c _ {L , q} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 9 7 6 \frac {c _ {L , q}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 0 1 9 8 \frac {c _ {R , u}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 0 0 7 0 3 \frac {c _ {R , d}}{\Lambda_ {\mathrm {T e V}} ^ {2}}, \tag {4.20c} \\ \end{array}
$$

$$
\begin{array}{l} \frac {\delta \widetilde {R _ {\mu}}}{R _ {\mu}} = 0. 0 9 2 3 \frac {\delta G _ {F}}{G _ {F}} + 0. 1 8 9 \frac {\delta M _ {Z}}{M _ {Z}} - 0. 0 9 2 3 \frac {\delta \alpha}{\alpha} - 0. 0 0 0 1 3 8 \frac {c _ {T}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ + 0. 0 2 5 3 \frac {c _ {W W}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 0 0 8 8 7 \frac {c _ {B B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 0 5 0 6 \frac {c _ {W B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ - 0. 1 3 6 \frac {c _ {L} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 1 3 6 \frac {c _ {L}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 1 \frac {c _ {R}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ - 0. 0 3 9 8 \frac {c _ {L , q} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 3 9 8 \frac {c _ {L , q}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 1 9 8 \frac {c _ {R , u}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 0 1 4 6 \frac {c _ {R , d}}{\Lambda_ {\mathrm {T e V}} ^ {2}}, \tag {4.20d} \\ \end{array}
$$

$$
\begin{array}{l} \frac {\delta \widetilde {R _ {\tau}}}{R _ {\tau}} = 0. 0 9 1 5 \frac {\delta G _ {F}}{G _ {F}} + 0. 1 8 3 \frac {\delta M _ {Z}}{M _ {Z}} - 0. 0 9 1 5 \frac {\delta \alpha}{\alpha} + 0. 0 2 5 2 \frac {c _ {W W}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ + 0. 0 0 0 8 8 6 \frac {c _ {B B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 0 5 0 4 \frac {c _ {W B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 1 3 6 \frac {c _ {L} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 1 3 6 \frac {c _ {L}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 1 \frac {c _ {R}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ - 0. 0 3 9 8 \frac {c _ {L , q} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 3 9 8 \frac {c _ {L , q}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 1 9 8 \frac {c _ {R , u}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 0 1 4 6 \frac {c _ {R , d}}{\Lambda_ {\mathrm {T e V}} ^ {2}}, \tag {4.20e} \\ \end{array}
$$

$$
\begin{array}{l} \overbrace {\frac {\delta \sin^ {2} \theta_ {W}}{\sin^ {2} \theta_ {W}}} ^ {\widetilde {\delta \sin^ {2} \theta_ {W}}} = - 1. 3 7 \frac {\delta G _ {F}}{G _ {F}} - 2. 7 4 \frac {\delta M _ {Z}}{M _ {Z}} + 1. 3 7 \frac {\delta \alpha}{\alpha} - 0. 0 6 9 2 \frac {c _ {W W}}{\Lambda_ {\mathrm {T e V}} ^ {2}} + 0. 0 0 9 0 7 \frac {c _ {B B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} \\ + 0. 0 0 7 5 3 \frac {c _ {W B}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 0 6 0 5 \frac {c _ {L} ^ {(3)}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 0 6 0 5 \frac {c _ {L}}{\Lambda_ {\mathrm {T e V}} ^ {2}} - 0. 0 8 2 1 \frac {c _ {R}}{\Lambda_ {\mathrm {T e V}} ^ {2}}. \tag {4.20f} \\ \end{array}
$$

We see that these observables involve almost all dimension-6 operators in table 1, except the pure-Higgs operator  $\mathcal{O}_H$  and the gluon operator  $\mathcal{O}_g$ . The bosonic operators  $\mathcal{O}_T$ ,  $\mathcal{O}_{WW}$ ,  $\mathcal{O}_{BB}$ , and  $\mathcal{O}_{WB}$  can enter through the field redefinitions and mass shifts. Only the operators  $\mathcal{O}_{HB}$  and  $\mathcal{O}_{HW}$  are not involved.

In table 8, we present the sensitivity reaches by including the  $Z$ -pole observables summarized in table 7. The  $n$ -th row corresponds to the constraint from the  $(Z,W)$  mass measurements, the Higgs observables, and the existing EWPO, plus the first  $n$  observables in table 7. The difference between the  $(n)$ -th and  $(n+1)$ -th rows represents the effect of the  $n$ -th  $Z$ -pole observable in table 7. It is striking to see that including the CEPC  $Z$ -pole measurements can further probe the new physics scale up to  $35\mathrm{TeV}$  for  $\mathcal{O}_L^{(3)}$ . This is another factor-2 enhancement over that of only including  $(Z,W)$  mass measurements in table 6. The relative enhancements to the scales of  $\mathcal{O}_{WW}$ ,  $\mathcal{O}_R$ ,  $\mathcal{O}_{L,q}^{(3)}$ ,  $\mathcal{O}_{L,q}$ ,  $\mathcal{O}_{R,u}$ , and  $\mathcal{O}_{R,d}$  are even larger, while operators  $\mathcal{O}_{WB}$ ,  $\mathcal{O}_{LL}^{(3)}$ , and  $\mathcal{O}_L$  also receive significantly enhanced constraints. In contrast, the operator  $\mathcal{O}_{BB}$  is not significantly improved since its contribution to  $Z$ -pole observables is highly suppressed. We present the final results in figure 4.

Table 8. Impacts of the projected  $Z$ -pole measurements at the CEPC [41-43, 107] on the reach of new physics scale  $\Lambda / \sqrt{|c_j|}$  (in TeV) at 95% C.L. For comparison, the first row of this table repeats the last row of table 6, as our starting point of this table. For the  $(n + 1)$ -th row, the first  $n$  observables in table 7 are taken into account. In addition, the estimated  $M_Z$  and  $M_W$  measurements at the CEPC in table 5, the Higgs observables (HO), and the existing electroweak precision observables (EWPO) in table 2 are always included for each row. The entries with major enhancements of the new physics scale limit are marked in red color with an underscore.  

<table><tr><td>O_H</td><td>O_T</td><td>O_WW</td><td>O_BB</td><td>O_WB</td><td>O_HW</td><td>O_HB</td><td>O_(3)LL</td><td>O_(3)L</td><td>O_L</td><td>O_R</td><td>O_(3)L,q</td><td>O_L,q</td><td>O_R,u</td><td>O_R,d</td><td>O_g</td></tr><tr><td>2.74</td><td>23.7</td><td>6.38</td><td>5.78</td><td>11.6</td><td>2.16</td><td>0.604</td><td>17.4</td><td>18.1</td><td>10.2</td><td>8.78</td><td>2.06</td><td>0.568</td><td>0.393</td><td>0.339</td><td>43.8</td></tr><tr><td>2.74</td><td>23.7</td><td>6.38</td><td>5.78</td><td>11.6</td><td>2.16</td><td>0.604</td><td>17.5</td><td>18.3</td><td>10.5</td><td>8.78</td><td>2.06</td><td>0.568</td><td>0.393</td><td>0.339</td><td>43.8</td></tr><tr><td>2.74</td><td>24.0</td><td>8.32</td><td>5.80</td><td>12.2</td><td>2.16</td><td>0.604</td><td>20.7</td><td>23.0</td><td>12.5</td><td>13.0</td><td>2.23</td><td>1.62</td><td>0.393</td><td>3.97</td><td>43.8</td></tr><tr><td>2.74</td><td>24.0</td><td>8.33</td><td>5.80</td><td>12.2</td><td>2.16</td><td>0.604</td><td>20.7</td><td>23.0</td><td>12.5</td><td>13.0</td><td>7.90</td><td>7.89</td><td>3.55</td><td>4.05</td><td>43.8</td></tr><tr><td>2.74</td><td>24.0</td><td>8.54</td><td>5.80</td><td>12.2</td><td>2.16</td><td>0.604</td><td>20.7</td><td>23.4</td><td>14.4</td><td>14.0</td><td>8.63</td><td>8.62</td><td>4.88</td><td>4.71</td><td>43.8</td></tr><tr><td>2.74</td><td>24.0</td><td>8.75</td><td>5.81</td><td>12.3</td><td>2.16</td><td>0.604</td><td>20.7</td><td>23.7</td><td>15.8</td><td>14.9</td><td>9.21</td><td>9.21</td><td>5.59</td><td>5.17</td><td>43.8</td></tr><tr><td>2.74</td><td>26.3</td><td>12.6</td><td>5.93</td><td>15.3</td><td>2.16</td><td>0.604</td><td>30.2</td><td>35.2</td><td>19.8</td><td>21.6</td><td>9.21</td><td>9.21</td><td>5.59</td><td>5.17</td><td>43.8</td></tr></table>

Figure 4 demonstrates that the  $Z$ -pole measurements are even more sensitive than the Higgs observables for indirectly constraining the new physics scales of effective dimension-6 operators. This is mainly because of the huge event number that can be produced at the  $Z$ -pole resonance. We see that running the future  $e^{+}e^{-}$  collider at  $Z$ -pole is beyond the technical purpose of the machine calibration. Our study shows that it is worth of running the collider at  $Z$ -pole for a longer time. Or, after running the Higgs factory at Higgsstrahlung energy  $(240 - 250\mathrm{GeV})$ , it is invaluable to return to the  $Z$ -pole running for a period and thus ensure the no-lose probe of new physics.

# 5 Higgs coupling precision tests at CEPC and probing dimension-6 Yukawa-type operators

In this section, we study the CEPC sensitivities to the SM-type Higgs couplings, and then apply these limits to study the probe of Yukawa-type dimension-6 operators (cf. table 1). In section 5.1, we first apply our analytical linear  $\chi^2$  fitting method in appendix B to study the sensitivity probe of the SM-type Higgs couplings at the CEPC. Then, based upon these, we will analyze the CEPC reach of new physics scales associated with the Yukawa-type dimension-6 operators in section 5.2.

# 5.1 Higgs coupling precision tests at CEPC

For an illustration, we apply the analytical linear  $\chi^2$  fitting method described in appendix B to extract the projected precisions of the CEPC Higgs measurements for probing the SM-type Higgs couplings. The Higgs couplings to other SM particles may be defined relative to their SM values by rescaling,  $g_{hii} / g_{hii}^{\mathrm{sm}}\equiv \kappa_i$ , where the possible deviation  $\kappa_{i} - 1$  denotes the anomalous Higgs couplings. Such deviations  $\kappa_{i} - 1$  can arise from the dimension-6

![](images/d5e85d16c7e60ff1f3957f4b8764c53a83b3b896903c173118ca79f1cf0f32e2.jpg)  
Figure 4. The  $95\%$  exclusion (blue) and  $5\sigma$  discovery (red) sensitivities to the new physics scales  $\Lambda / \sqrt{|c_j|}$  by combining the current electroweak precision measurements  $(\alpha, G_F, M_Z, M_W)$  [105] with the future Higgs observables at the Higgs factory CEPC (table 2) and  $Z$ -pole measurements (table 5) under a projected luminosity of  $5\mathrm{ab}^{-1}$  [41-43].

operators shown in table 1. The anomalous Higgs couplings  $\kappa_{i} \neq 1$  will modify the Higgs observables in table 2 and thus receive constraints by the CEPC measurements.

The cross sections of Higgsstrahlung and  $WW$  fusion processes are scaled by the Higgs couplings with  $Z$  and  $W$  gauge bosons as  $\delta \sigma (Zh) / \sigma (Zh)\simeq 2\delta \kappa_{Z}$  and  $\delta \sigma (\nu \nu h) / \sigma (\nu \nu h)\simeq$ $2\delta \kappa_{W}$ . On the other hand, each partial decay width of  $h\rightarrow ii$  scales as,  $\Gamma_{hii} / \Gamma_{hii}^{\mathrm{sm}} =$ $\kappa_i^2$ . For the exotic decay channels which are not present in the SM, such as the invisible decays, we can parametrize its contribution as a fraction of the total SM Higgs decay width,  $\Gamma_{\mathrm{inv}} / \Gamma_{\mathrm{tot}}^{\mathrm{sm}} = \mathrm{Br}(\mathrm{inv})\equiv \delta \kappa_{\mathrm{inv}}$ , which is relatively small deviation in principle. Each branching fraction  $\mathrm{Br}_i$  is a ratio between the individual decay width and total width, and is thus a function of all scaling factors  $\{\kappa_i\}$ . Since so far the SM fits LHC data quite well and the CEPC measurements can be rather precise, we expect that the relative deviations from the SM are significantly below one,  $|\kappa_i - 1|\ll 1$ . We thus define,  $\kappa_{i}\equiv 1 + \delta \kappa_{i}$ , with  $|\delta \kappa_{i}|\ll 1$ . Thus, we may expand the branching fractions up to the linear order of  $\delta \kappa_{i}$ ,

$$
\mathrm {B r} _ {i} ^ {\mathrm {t h}} \simeq \mathrm {B r} _ {i} ^ {\mathrm {t h}, 0} \left(1 + \sum_ {j} A _ {i j} \delta \kappa_ {j}\right), \quad \mathrm {B r} _ {\text {i n v}} ^ {\mathrm {t h}} \simeq \delta \kappa_ {\text {i n v}}, \tag {5.1}
$$

where  $\mathrm{Br}_i^{\mathrm{th},0} = \mathrm{Br}_i^{\mathrm{sm}}$  is the SM prediction, and the coefficient matrix  $A$  is,

$$
A _ {i j} = 2 \left(\delta_ {i j} - \mathrm {B r} _ {j} ^ {\mathrm {s m}}\right), \quad A _ {i, \text {i n v}} = - 1, \quad A _ {\text {i n v}, i} = 0, \quad A _ {\text {i n v}, \text {i n v}} = 1. \tag {5.2}
$$

Table 9. Projected precisions of measuring Higgs couplings (68% C.L.) at the CEPC (250GeV,  $5\mathrm{ab}^{-1}$ ) from our fit, in comparison with the LHC (14TeV,  $300\mathrm{fb}^{-1}$ ), HL-LHC (14TeV,  $3\mathrm{ab}^{-1}$ ) and ILC (250GeV,  $250\mathrm{fb}^{-1}$ )+(500GeV,  $500\mathrm{fb}^{-1}$ ) [11].  

<table><tr><td rowspan="2">Precision (%)</td><td colspan="2">CEPC</td><td rowspan="2">LHC</td><td rowspan="2">HL-LHC</td><td rowspan="2">ILC-250</td><td rowspan="2">ILC-500</td></tr><tr><td>9+1 fit</td><td>8+1 fit</td></tr><tr><td>κZ</td><td>0.249</td><td>0.249</td><td>8.5</td><td>6.3</td><td>0.78</td><td>0.50</td></tr><tr><td>κW</td><td>1.20</td><td>1.20</td><td>5.4</td><td>3.3</td><td>4.6</td><td>0.46</td></tr><tr><td>κγ</td><td>4.67</td><td>4.67</td><td>9.0</td><td>6.5</td><td>18.8</td><td>8.6</td></tr><tr><td>κg</td><td>1.42</td><td>1.42</td><td>6.9</td><td>4.8</td><td>6.1</td><td>2.0</td></tr><tr><td>κb</td><td>1.27</td><td>1.27</td><td>14.9</td><td>8.5</td><td>4.7</td><td>0.97</td></tr><tr><td>κc</td><td>1.75</td><td>1.75</td><td>—</td><td>—</td><td>6.4</td><td>2.6</td></tr><tr><td>κτ</td><td>1.33</td><td>1.33</td><td>9.5</td><td>6.5</td><td>5.2</td><td>2.0</td></tr><tr><td>κμ</td><td>8.59</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Brinv)</td><td>0.134</td><td>0.134</td><td>8.0</td><td>4.0</td><td>0.54</td><td>0.52</td></tr><tr><td>Γh</td><td>2.6</td><td>2.6</td><td>—</td><td>—</td><td>—</td><td>—</td></tr></table>

Note that different branching fractions are correlated with coefficient proportional to the corresponding SM values, as shown in (4.17). For the branching fraction  $\mathrm{Br}_i$ , the contribution due to its own channel is modulated by  $1 - \mathrm{Br}_i^{\mathrm{sm}}$ , while the effect from other channels by the corresponding  $\mathrm{Br}_i^{\mathrm{sm}}$ . Larger branching fraction means the channel has smaller effect on its own, but larger on the others.

Applying our analytical  $\chi^2$  fitting method (appendix B) together with the relative uncertainties of Higgs production cross sections and branching fractions from table 2, we extract the sensitivities of CEPC measurements to the SM Higgs couplings as shown in table 9 with two different fits in the second and third columns. The first is a  $9 + 1$  parameter fit, including 9 parameters for decay branching fractions and 1 for total decay width. All the anomalous Higgs couplings have precisions at  $1\%$  level, except that  $\kappa_{\gamma}$  and  $\kappa_{\mu}$  have larger uncertainties. This is because the branching fractions,  $\mathrm{Br}(\gamma \gamma)$  and  $\mathrm{Br}(\mu \bar{\mu})$ , are too small according to the SM predictions [114]. As shown in table 2, their values are well below  $1\%$ . Since roughly 1 million Higgs particles can be produced at CEPC [41-43], the decay into photon or muon can collect less than  $10^{4}$  events. The statistical fluctuation is thus larger than  $1\%$ . A realistic estimate gives  $9\%$  and  $17\%$ , respectively, including both statistical and systematic uncertainties. On the contrary, the  $ZZh$  Higgs coupling  $\kappa_Z$  has a precision much better than  $1\%$ , due to the direct measurement of the Higgsstrahlung production cross section  $\sigma(Zh)$ . This inclusive production rate has larger event rate than any individual decay channel. Without  $\sigma(Zh)$ , the precision on  $\kappa_Z$  is also at percentage level. The same thing applies to  $\kappa_W$ , which can be constrained by the  $WW$  fusion production rate  $\sigma(\nu \nu h)$ , leading to roughly a factor of  $\sqrt{2}$  improvement.

![](images/96cc3f64bfa505935ad551f13af8b6e74aad414350ae21ae99caffe9f46a2cd6.jpg)  
Figure 5. Precisions (68% C.L.) of the CEPC (250 GeV) for measuring the Higgs gauge couplings and Yukawa couplings from our  $9+1$  parameter fit, with an integrated luminosity of  $(1,3,5)\mathrm{ab}^{-1}$ , respectively. These are compared to the precisions of the LHC ( $14\mathrm{TeV}$ ,  $300\mathrm{fb}^{-1}$ ) and HL-LHC ( $14\mathrm{TeV}$ ,  $3\mathrm{ab}^{-1}$ ) [11].

For comparison, we further present an  $8 + 1$  parameter fit with  $\mathrm{Br}(\mu \bar{\mu})$  and  $\kappa_{\mu}$  removed in the third column of table 9. We note that the precision of measuring other anomalous couplings are not affected at all. This is because the branching fraction of this channel is very small in the first place. As explained below eq. (5.2), the correlation is proportional to the corresponding SM prediction  $\mathrm{Br}_j^{\mathrm{sm}}$ . Hence, it is rather weakly correlated with other channels. We present the result of these two fits in figure 5.

Besides the precision limits on Higgs couplings at the CEPC (250 GeV, 5ab $^{-1}$ ), we also show the bounds on Higgs couplings from the LHC (14 TeV, 300fb $^{-1}$ ) and the HLHLC (14 TeV, 3ab $^{-1}$ ) [11], in table 9, for comparison. It is clear that the CEPC (250 GeV, 5ab $^{-1}$ ) can significantly improve the precision of Higgs coupling measurements. In addition, many decay channels cannot be probed at the LHC. For instance, the LHC has no sensitivity to the  $hcc$  coupling [11], as well as  $h\mu \bar{\mu}$  coupling. But, they can be measured at the CEPC instead. The total decay width of the SM Higgs with 125 GeV mass is about 4 MeV, which is far below the LHC sensitivity. It is hard to make a direct measurement at the LHC without model assumptions. In table 9, we also show the projected limits of the ILC (250 GeV, 250fb $^{-1}$ ) and ILC (500 GeV, 500fb $^{-1}$ ) for comparison [11]. It shows that CEPC (250GeV, 5ab $^{-1}$ ) can have better sensitivities than the ILC (500GeV, 500fb $^{-1}$ ), except for the  $hWW$  and  $hb\bar{b}$  couplings.

# 5.2 Probing dimension-6 Yukawa-type operators at CEPC

The last column of table 1 also presents three Yukawa-type dimension-6 operators  $\mathcal{O}_y^f = (\mathcal{O}_y^u,\mathcal{O}_y^d,\mathcal{O}_y^\ell)$ . These operators will modify the SM Yukawa coupling by a rescaling factor,

$$
y _ {f} ^ {\mathrm {s m}} \longrightarrow y _ {f} = y _ {f} ^ {\mathrm {s m}} + \frac {3 c _ {f} v ^ {2}}{2 \Lambda^ {2}}, (5. 3)
$$

and correct the SM fermion mass,

$$
m _ {f} ^ {\mathrm {s m}} = \frac {y _ {f} ^ {\mathrm {s m}} v}{\sqrt {2}} \longrightarrow m _ {f} = \frac {v}{\sqrt {2}} \left(y _ {f} ^ {\mathrm {s m}} + \frac {c _ {f} v ^ {2}}{2 \Lambda^ {2}}\right), \tag {5.4}
$$

where  $m_f$  is the full fermion mass including contributions of dimension-6 operators. Thus, using (5.4), we can reexpress  $y_f^{\mathrm{sm}}$  as

$$
y _ {f} ^ {\mathrm {s m}} = \frac {\sqrt {2} m _ {f}}{v} - \frac {c _ {f} v ^ {2}}{2 \Lambda^ {2}} = y _ {f} ^ {\mathrm {s m , 0}} - \frac {c _ {f} v ^ {2}}{2 \Lambda^ {2}}, (5. 5)
$$

where  $y_{f}^{\mathrm{sm},0}\equiv \sqrt{2} m_{f} / v$ . From eqs. (5.3) and (5.5), we compute the coupling ratios up to  $\mathcal{O}(\Lambda^{-2})$

$$
\kappa_ {f} = \frac {y _ {f}}{y _ {f} ^ {\mathrm {s m}}} \simeq 1 + \frac {3 c _ {f} v ^ {3}}{2 \sqrt {2} m _ {f} \Lambda^ {2}}, \tag {5.6a}
$$

$$
y _ {f} = y _ {f} ^ {\mathrm {s m}, 0} \left(y _ {f} / y _ {f} ^ {\mathrm {s m}, 0}\right) = y _ {f} ^ {\mathrm {s m}, 0} \tilde {\kappa} _ {f}, \tag {5.6b}
$$

$$
\tilde {\kappa} _ {f} \equiv \frac {y _ {f}}{y _ {f} ^ {\mathrm {s m} , 0}} = \frac {y _ {f} ^ {\mathrm {s m}}}{y _ {f} ^ {\mathrm {s m} , 0}} \kappa_ {f} \simeq 1 + \frac {c _ {f} v ^ {3}}{\sqrt {2} m _ {f} \Lambda^ {2}}. \tag {5.6c}
$$

We note that it is the effective coupling  $y_{f}$  that actually enters the physical observables, and the  $\chi^2$  fit we made in section 5.1 (table 9) is just a fit of the sensitivity reach on the coupling ratio  $\tilde{\kappa}_{f}\equiv y_{f} / y_{f}^{\mathrm{sm},0}\equiv 1 + \Delta \tilde{\kappa}_{f}$ , for the case of Higgs Yukawa couplings, where  $\Delta \tilde{\kappa} = \tilde{\kappa}_f - 1$  is given by eq. (5.6c) for the contribution of dimension-6 operator  $\mathcal{O}_y^f$ . This means that each  $\kappa_{f}$  in table 9 should be replaced by the current notation  $\tilde{\kappa}_{f}$  as we exactly defined in eq. (5.6c). Thus, for each given fitted experimental sensitivity  $\Delta \tilde{\kappa}_{f}$  (table 9) and using eq. (5.6c), we can derive the following lower bound on the Yukawa-type new physics scale,

$$
\frac {\Lambda}{\sqrt {| c _ {f} |}} \geqslant \sqrt {\frac {v ^ {3}}{\sqrt {2} m _ {f} \Delta \tilde {\kappa} _ {f}}}. \tag {5.7}
$$

In eq. (5.7), the Yukawa coupling precision  $\Delta \tilde{\kappa}_f$  will be measured at the CEPC with a typical renormalization scale  $\mu = M_h$ . So we will input the fermion mass  $m_f$  as the running mass defined at  $\mu = M_h$ . With these, we present the CEPC potential reaches (95% C.L.) in figure 6 and table 10, and compare them with the corresponding limits estimated for the LHC (14TeV, 300fb $^{-1}$ ), HL-LHC (14TeV, 3ab $^{-1}$ ), and ILC (250GeV, 250fb $^{-1}$ )+(500GeV, 500fb $^{-1}$ ) [11]. We see that depending on the experimental precision and the involved fermion mass, the CEPC probe of the Yukawa-type new

![](images/c46cffc1d04fe22704dff989c5c184dc4cab565342076613eda7e50f8953af7e.jpg)  
Figure 6. Sensitivity reaches (95% C.L.) of the new physics scales  $\Lambda / \sqrt{|c_j|}$  of Yukawatype dimension-6 operators by the precision Higgs coupling measurements at the Higgs factory CEPC (250GeV), in comparison with LHC (14TeV,  $300\mathrm{fb}^{-1}$ ) and the HL-LHC (14TeV,  $3\mathrm{ab}^{-1}$ ).

Table 10. Sensitivity reaches (95% C.L.) of the new physics scales of Yukawa-type dimension-6 operators at the CEPC (250GeV,  $5\mathrm{ab}^{-1}$ ), in comparison with the LHC (14TeV,  $300\mathrm{fb}^{-1}$ ), HLHC (14TeV,  $3\mathrm{ab}^{-1}$ ), and ILC (250GeV,  $250\mathrm{fb}^{-1}$ )+(500GeV,  $500\mathrm{fb}^{-1}$ ).  

<table><tr><td rowspan="2">\( \Lambda/\sqrt{|c_j|}(\mathrm{TeV}) \)</td><td colspan="2">CEPC</td><td rowspan="2">LHC</td><td rowspan="2">HL-LHC</td><td rowspan="2">ILC-250</td><td rowspan="2">ILC-500</td></tr><tr><td>9+1 fit</td><td>8+1 fit</td></tr><tr><td>b quark</td><td>13.2</td><td>13.2</td><td>3.87</td><td>5.12</td><td>6.89</td><td>15.2</td></tr><tr><td>c quark</td><td>24.4</td><td>24.4</td><td>—</td><td>—</td><td>12.8</td><td>20.0</td></tr><tr><td>τ lepton</td><td>15.4</td><td>15.4</td><td>5.74</td><td>6.95</td><td>7.76</td><td>12.5</td></tr><tr><td>μ lepton</td><td>25.1</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr></table>

physics scales can reach  $13 - 25\mathrm{TeV}$  range with a  $5\mathrm{ab}^{-1}$  integrated luminosity. These sensitivities are much higher than that of the LHC Run-2 and the HL-LHC.

From figure 6 and table 10, it is interesting to see that the probe of the new physics scales with operators  $\mathcal{O}_y^\mu$  and  $\mathcal{O}_y^c$  are significantly better than other Yukawatype operators such as  $(\mathcal{O}_y^b,\mathcal{O}_y^\tau)$ . This is because the lower bound (5.7) is proportional to  $(m_f\Delta \tilde{\kappa}_f)^{-1 / 2}$ , which depends on both the coupling precision  $\Delta \tilde{\kappa}_f$  and the fermion mass  $m_{f}$ . Here we have used the running masses [110-112],  $(m_b,m_c,m_\tau ,m_\mu)\simeq$  (2.41, 0.515, 1.713, 0.0996)GeV, at the scale  $\mu = M_h$ . As shown in table 9 and figure 5, among the sensitivities to  $(\tilde{\kappa}_b,\tilde{\kappa}_c,\tilde{\kappa}_\tau ,\tilde{\kappa}_\mu)$ , CEPC can measure  $\tilde{\kappa}_b$  most precisely (down to

a relative precision  $\Delta \tilde{\kappa}_b = 1.27\%$  ), and probe  $\tilde{\kappa}_{\mu}$  least precisely (down to  $\Delta \tilde{\kappa}_{\mu} = 8.59\%$  ), which differ by a factor 6.76. But, their running masses differ by a much larger ratio  $m_b / m_\mu \simeq 24.2$ . This means that the fermion mass ratio has a larger effect than the ratio of their coupling sensitivities. Hence, we find that the reach of new physics scale with  $\mathcal{O}_y^\mu$  is higher than that with  $\mathcal{O}_y^b$  by a factor of  $\sqrt{24.2 / 6.76} \simeq 1.9$ . This explains our findings shown in table 10 and figure 6. Similarly, for the other two operators  $(\mathcal{O}_y^c, \mathcal{O}_y^\tau)$  with fermions  $(c, \tau)$ , we can deduce that the corresponding reaches of new physics scales are enhanced relative to that of  $\mathcal{O}_y^b$  by a factor about (1.8, 1.2).

# 6 Conclusions

The LHC Higgs discovery in 2012 has led particle physics to a turning point at which the precision Higgs measurements have become an important task for seeking clues to the new physics discovery. A future Higgs factory (like the proposed  $e^{+}e^{-}$  colliders CEPC, FCC-ee, and ILC) can provide such precision Higgs measurements.

In this work, we studied the new physics scales that a future Higgs factory can probe via general dimension-6 operators involving the observed Higgs boson (table 1). Our analysis utilizes the existing electroweak precision observables (EWPO), as well as the Higgs observables and precision measurements at the future  $e^{+}e^{-}$  Higgs factory (taking the CEPC as an illustration). The conventional scheme-dependent analysis usually fixes the three electroweak parameters  $(g,g^{\prime},v)$  with three high precision electroweak observables  $(\alpha ,G_{F},M_{Z})$  in the  $Z$ -scheme or  $(\alpha ,M_W,M_Z)$  in the  $W$ -scheme, while ignoring their experimental uncertainties. In contrast, we developed a scheme-independent approach to incorporate full experimental information (including both central values and uncertainties) of the EWPO in section 2. With this approach, the electroweak parameters and the new physics scales of dimension-6 operators can be fitted simultaneously by the same  $\chi^2$  function.

The advantage of our scheme-independent approach is made clear when the precisions of  $Z$  and  $W$  mass measurements become comparable at the Higgs factory (cf. table 6). Since new physics deviations from the SM are fairly small, as already constrained by the LHC data, the analytical expansion up to their linear order holds well (section 3). Accordingly, we performed the analytic linear  $\chi^2$  fit in appendix B, which is physically intuitive, numerically fast, and can be straightforwardly generalized to include any number of observables and fitting parameters under consideration. In section 4, we demonstrated that including the existing EWPO together with future Higgs measurements can probe the new physics scales up to 10 TeV (and to 40 TeV for the gluon-involved operator  $\mathcal{O}_g$ ) at 95% C.L., as shown in figure 3 and table 3. We found that including the CEPC precision measurements can further lift the reach up to 35 TeV (figure 4 and table 8). In addition, the CEPC precision tests of Higgs couplings can probe the new physics scales with Yukawatype operators up to (13-25) TeV, (figure 6 and table 10). We note that these indirect new physics reaches do cover the energy range to be probed by the future hadron colliders of  $pp(50 - 100)$  TeV [41-46] running in the same circular tunnel. Hence, the precision probe at the Higgs factory can provide an important guideline for the future new physics discoveries

at the SPPC or FCC-hh. Our study demonstrates that the Higgs factory can probe the new physics of the Higgs sector much more sensitively than what the LHC would achieve [109].

The  $Z$ -pole running of the  $e^{+}e^{-}$  collider is required by the machine calibration at its initial stage. In section 4.6, we further demonstrated that during the CEPC early phase, the  $Z$ -pole measurements can provide even stronger indirect probe of the new physics scales than the Higgs observables alone as measured at the Higgs factory (250GeV). This motivates a longer  $Z$ -pole running to ensure the no-lose probe of new physics deviations from the SM, complementary to the Higgs factory via the  $Zh$  production.

# Acknowledgments

We thank Matthew McCullough, Manqi Ruan, and Tevong You for many valuable discussions. We are grateful to Michael Peskin for discussing the  $\chi^2$  analysis of ref. [11]. We also thank Timothy Barklow, Tao Han, Zhijun Liang, Matthew Strassler, Liantao Wang, Xinchou Lou and Yifang Wang for discussions. SFG thanks Matthew McCullough for kind invitation and hospitality during his visit at CERN Theory Division. This work is supported in part by National NSF of China (under grants 11275101 and 11135003) and by Tsinghua University (under grant 20141081211).

# A Kinetic mixing of gauge bosons

The dimension-6 operators can make nontrivial corrections to both the mass matrices and the kinetic terms of gauge bosons. The situation is much simpler for charged weak bosons  $W^{\pm}$  which have only one mass eigenstate and thus no extra mixing in the effective theory of the SM with dimension-6 operators. On the other hand, the situation for neutral gauge bosons are more involved since mixing between the photon  $A$  and the  $Z$  boson can arise from either loop corrections or new physics beyond the SM. Both kinetic mixing and mass diagonalization may appear. It is necessary to first transform their kinetic terms into the canonical forms and mass matrix into the diagonal form before deriving Feynman rules and computing physical processes. Here, we provide a general formalism within this effective theory and describe how to deal with the corrections from dimension-6 operators up to the linear order.

# A.1 Charged gauge bosons

For charged gauge boson, there is no mixing in either kinetic or mass term,

$$
\mathbf {D} (q ^ {2}) = \frac {1}{q ^ {2} K - \left[ (M _ {W} ^ {(0)}) ^ {2} - \delta M _ {W} ^ {2} \right]}, \tag {A.1}
$$

where  $K \equiv 1 + \delta K = Z_W^{-2}$  with  $Z_W$  given by eq. (3.5). Thus, we have

$$
\delta K \simeq - 2 \delta Z _ {W} = - \frac {2 v ^ {2}}{\Lambda^ {2}} g ^ {2} c _ {W W}. \tag {A.2}
$$

The propagator (A.1) reduces to its canonical form,  $\mathbf{D}(q^2) = \frac{1}{q^2 - M_W^2}$ , when the  $W$  boson field and its mass are renormalized as

$$
W \rightarrow \frac {W}{\sqrt {K}}, \quad M _ {W} ^ {2} = \left(M _ {W} ^ {(0)}\right) ^ {2} \left(1 + \frac {\delta M _ {W} ^ {2}}{M _ {W} ^ {2}} - \delta K\right). \tag {A.3}
$$

Here we have omitted the small difference between  $M_W$  and  $M_W^{(0)}$  in the denominator of the second term, which is of the higher order.

# A.2 Neutral gauge bosons

For neutral gauge bosons, both  $A$  and  $Z$  are involved. The kinetic mixing and mass terms are hence  $2 \times 2$  matrices. Nontrivial mixing effects can appear in both parts. We first generally parametrize the correlated propagator as,

$$
\mathbf {D} (q ^ {2}) = \frac {1}{q ^ {2} \mathbb {K} - \mathbb {M} ^ {2}}, \tag {A.4}
$$

where both kinetic coefficient matrix  $\mathbb{K}$  and the mass matrix  $\mathbb{M}$  need to be diagonalized,  $S\mathbb{K}S^{-1}\equiv \mathbb{T}$  and  $R\mathbb{M}^2 R^{-1}\equiv \mathbb{D}^2$ , with  $\mathbb{T}$  and  $\mathbb{D}$  denoting the diagonal kinetic matrix and diagonal mass matrix, respectively. Then, we can first diagonalize the kinetic term as

$$
\mathbf {D} (q ^ {2}) = \frac {1}{q ^ {2} S ^ {- 1} \mathbb {T} S - \mathbb {M} ^ {2}} = S ^ {- 1} \mathbb {T} ^ {- \frac {1}{2}} \frac {1}{q ^ {2} \mathbb {I} - \mathbb {T} ^ {- \frac {1}{2}} S \mathbb {M} ^ {2} S ^ {- 1} \mathbb {T} ^ {- \frac {1}{2}}} \mathbb {T} ^ {- \frac {1}{2}} S, \tag {A.5}
$$

by folding kinetic mixing to the mass matrix,  $\widetilde{\mathbb{M}}^2\equiv \mathbb{T}^{-\frac{1}{2}}S\mathbb{M}^2 S^{-1}\mathbb{T}^{-\frac{1}{2}}$ . The modified mass matrix can be diagonalized by  $\widetilde{\mathbb{M}}^2 = \widetilde{R}^{-1}\widetilde{\mathbb{D}}^2\widetilde{R}$ . Then, the propagator can be reduced to the fully diagonalized form,

$$
\mathbf {D} (q ^ {2}) = S ^ {- 1} \mathbb {T} ^ {- \frac {1}{2}} \widetilde {R} ^ {- 1} \frac {1}{q ^ {2} \mathbb {I} - \widetilde {\mathbb {D}} ^ {2}} \widetilde {R} \mathbb {T} ^ {- \frac {1}{2}} S \equiv \widetilde {S} ^ {T} \frac {1}{q ^ {2} \mathbb {I} - \widetilde {\mathbb {D}} ^ {2}} \widetilde {S}. \tag {A.6}
$$

For the current effective theory, the original mass matrix  $\mathbb{M}^2 = \mathrm{diag}\{0,M_Z^2\}$  of neutral gauge bosons is diagonalized in the  $A - Z$  space. It should be noted that  $M_Z^2\equiv (M_Z^{(0)})^2 +\delta M_Z^2$  is already the value after including the dimension-6 operator contributions. It remains diagonalized because of the unbroken  $\mathrm{U}(1)_{\mathrm{em}}$  gauge symmetry requires,  $\Pi_{AA}(0) = \Pi_{AZ}(0) = 0$ , when writing down the effective operators. On the other hand, for generality, kinetic mixing can be parametrized as,  $\mathbb{K}\equiv \mathbb{I} + \delta K$ , where  $\delta K$  is a  $2\times 2$  symmetric matrix whose explicit form will be given at the end of this section. A general feature is that its matrix elements ( $\delta K_{11},\delta K_{12},\delta K_{22}$ ) belong to the linear order in terms of dimension-6 operator coefficients. This leads to a sizable mixing of order  $\mathcal{O}(1)$ ,

$$
S \equiv \left( \begin{array}{c c} \cos \theta & \sin \theta \\ - \sin \theta & \cos \theta \end{array} \right), \qquad \tan 2 \theta = \frac {2 \delta K _ {1 2}}{\delta K _ {1 1} - \delta K _ {2 2}}, \qquad \qquad (A. 7)
$$

under which the kinetic term becomes diagonal. But, the deviations from canonical form are still of the linear order,  $\mathbb{T} \equiv \mathrm{diag}\{1 + \delta K_1, 1 + \delta K_2\}$ , which is a diagonal matrix. Then,

the modified mass matrix  $\tilde{\mathbb{M}}^2$  of neutral gauge bosons becomes,

$$
\widetilde {\mathbb {M}} ^ {2} \equiv \mathbb {T} ^ {- \frac {1}{2}} S \mathbb {M} ^ {2} S ^ {- 1} \mathbb {T} ^ {- \frac {1}{2}} = M _ {Z} ^ {2} \left( \begin{array}{c c} \frac {\sin^ {2} \theta}{1 + \delta K _ {1}} & \frac {\cos \theta \sin \theta}{\sqrt {1 + \delta K _ {1}} \sqrt {1 + \delta K _ {2}}} \\ \frac {\cos \theta \sin \theta}{\sqrt {1 + \delta K _ {1}} \sqrt {1 + \delta K _ {2}}} & \frac {\cos^ {2} \theta}{1 + \delta K _ {2}} \end{array} \right). \tag {A.8}
$$

Since the rank of  $\widetilde{\mathbb{M}}^2$  equals 1, it contains a massless eigenstate as the photon. This property is a consequence of the unbroken  $\mathrm{U}(1)_{\mathrm{em}}$  gauge symmetry. In addition, the  $Z$  boson mass is modified as

$$
\widetilde {M} _ {Z} ^ {2} \simeq M _ {Z} ^ {2} \left(1 - \sin^ {2} \theta \delta K _ {1} - \cos^ {2} \theta \delta K _ {2}\right) = \left[ M _ {Z} ^ {(0)} \right] ^ {2} \Big (1 + \frac {\delta M _ {Z} ^ {2}}{M _ {Z} ^ {2}} - \delta K _ {2 2} \Big). \qquad (\mathrm {A . 9})
$$

For convenience, we have denoted the zeroth-order of  $Z$  boson mass as  $M_Z^{(0)}$  and the correction as  $\delta M_Z^2$  which is independent of the correction from kinetic mixing. The modified mixing matrix  $\widetilde{R}$  is

$$
\widetilde {R} = \left( \begin{array}{l l} \cot \theta \sqrt {\frac {1 + \delta K _ {1}}{1 + \delta K _ {2} + \cot^ {2} \theta (1 + \delta K _ {1})}} & - \sqrt {\frac {1 + \delta K _ {2}}{1 + \delta K _ {2} + \cot^ {2} \theta (1 + \delta K _ {1})}} \\ \tan \theta \sqrt {\frac {1 + \delta K _ {2}}{1 + \delta K _ {1} + \tan^ {2} \theta (1 + \delta K _ {2})}} & \sqrt {\frac {1 + \delta K _ {1}}{1 + \delta K _ {1} + \tan^ {2} \theta (1 + \delta K _ {2})}} \end{array} \right). \tag {A.10}
$$

Altogether, we can derive the full current rotation  $\widetilde{S}$ ,

$$
\widetilde {S} \equiv \widetilde {R} \mathbb {T} ^ {- \frac {1}{2}} S = \mathbb {I} - \frac {1}{2} \left( \begin{array}{c c} \delta K _ {1 1} & 0 \\ 2 \delta K _ {1 2} & \delta K _ {2 2} \end{array} \right). \tag {A.11}
$$

The mixing matrix  $\widetilde{S}$  rotates  $A$  and  $Z$  as well as their corresponding currents,

$$
\widetilde {J} \equiv \widetilde {S} J = \left( \begin{array}{c c} \left(1 - \frac {1}{2} \delta K _ {1 1}\right) J _ {A} & \\ & - \delta K _ {1 2} J _ {A} + \left(1 - \frac {1}{2} \delta K _ {2 2}\right) J _ {Z} \end{array} \right). \tag {A.12}
$$

Note that this result still has linear dependence on the dimension-6 operator coefficients. The corrections to the kinetic term can lead to not only the field redefinitions of  $A$  and  $Z$ , but also the mixing between them.

For the effective operators under consideration, the  $\delta K$  matrix elements are

$$
\delta K _ {1 1} = \frac {- 2 v ^ {2}}{\Lambda^ {2}} \left[ s _ {w} ^ {2} g ^ {2} c _ {W W} - c _ {w} s _ {w} g g ^ {\prime} c _ {W B} + c _ {w} ^ {2} g ^ {\prime 2} c _ {B B} \right], \tag {A.13a}
$$

$$
\delta K _ {1 2} = \frac {- 2 v ^ {2}}{\Lambda^ {2}} \left[ c _ {w} s _ {w} g ^ {2} c _ {W W} - \frac {1}{2} (c _ {w} ^ {2} - s _ {w} ^ {2}) g g ^ {\prime} c _ {W B} - c _ {w} s _ {w} g ^ {\prime 2} c _ {B B} \right], \tag {A.13b}
$$

$$
\delta K _ {2 2} = \frac {- 2 v ^ {2}}{\Lambda^ {2}} \left[ c _ {w} ^ {2} g ^ {2} c _ {W W} + c _ {w} s _ {w} g g ^ {\prime} c _ {W B} + s _ {w} ^ {2} g ^ {\prime 2} c _ {B B} \right], \tag {A.13c}
$$

which involve only three operators,  $\mathcal{O}_{WW}$ ,  $\mathcal{O}_{BB}$ , and  $\mathcal{O}_{WB}$ .

# B Analytic linear  $\chi^2$  fit

To make our analysis fully transparent, in this appendix we present the  $\chi^2$  fitting method used for the current study. With a set of observables  $\mathcal{O}_j$  to constrain model parameters, we need to minimize the  $\chi^2$  function,

$$
\chi^ {2} = \sum_ {j} \left(\frac {\mathcal {O} _ {j} ^ {\mathrm {t h}} - \mathcal {O} _ {j} ^ {\mathrm {e x p}}}{\Delta \mathcal {O} _ {j}}\right) ^ {2}, \tag {B.1}
$$

which is a summation of individual constraints. In the above, we use  $\mathcal{O}_j^{\mathrm{th}}$  to denote the theoretical prediction,  $\mathcal{O}_j^{\mathrm{exp}}$  the experimental measurement, and  $\Delta \mathcal{O}_j$  the associated uncertainty. The theoretical prediction is a function of model parameters. Here, we will just use the  $\kappa_{j}$  rescaling of the Higgs coupling with the SM particles to fit experimental data (as to be elaborated in appendix 5), for an illustration. The deviation from the SM is then parametrized as  $\delta \kappa_{j} \equiv \kappa_{j} - 1$ , which are small numbers. When expanded to the linear term of  $\delta \kappa_{j}$ , the  $\chi^{2}$  function can be expressed as a quadratic function with matrix manipulations,

$$
\chi^ {2} = \left(\mathcal {O} ^ {\mathrm {t h}, 0} + A \delta \kappa - \mathcal {O} ^ {\mathrm {e x p}}\right) ^ {T} \overline {{\Sigma}} ^ {- 1} \left(\mathcal {O} ^ {\mathrm {t h}, 0} + A \delta \kappa - \mathcal {O} ^ {\mathrm {e x p}}\right). \tag {B.2}
$$

Note that, in matrix notations, the observable  $\mathcal{O}$  has dimension  $m\times 1$ , the deviation  $\delta \kappa$  has dimension  $n\times 1$ , coefficient matrix  $A$  has dimension  $m\times n$ , and error matrix  $\overline{\Sigma}$  dimension  $m\times m$ , where  $m$  and  $n$  are the number of observables and model/fitting parameters, respectively. The error matrix  $\overline{\Sigma}^{-1}$  of independent measurements is diagonal,

$$
\bar {\Sigma} ^ {- 1} = \operatorname {d i a g} \left\{\frac {1}{(\Delta \mathcal {O} _ {1}) ^ {2}}, \frac {1}{(\Delta \mathcal {O} _ {2}) ^ {2}}, \dots , \frac {1}{(\Delta \mathcal {O} _ {n}) ^ {2}} \right\}, \tag {B.3}
$$

according to the definition in (B.1). This corresponds to uncorrelated/independent measurements. Nevertheless, this assumption is not necessary. For correlated/dependent measurements, the error matrix  $\overline{\Sigma}^{-1}$  in the observable basis is in general a symmetric matrix,  $\overline{\Sigma}_{ij} \equiv \sigma_i \rho_{ij} \sigma_j$ , where  $\rho$  is the so-called correlation matrix.

The  $\chi^2$  function reaches its minimum under the condition,  $\partial \chi^2 /\partial \delta \kappa_j = 0$ . From this, we can solve the best fit values of  $\delta \kappa$ ,

$$
\delta \kappa_ {\text {b e s t}} = \left(A ^ {T} \bar {\Sigma} ^ {- 1} A\right) ^ {- 1} A ^ {T} \bar {\Sigma} ^ {- 1} \left(\mathcal {O} ^ {\exp} - \mathcal {O} ^ {\text {t h}, 0}\right). \tag {B.4}
$$

For convenience, let us rewrite the  $\chi^2$  function in the fitting parameter basis,

$$
\chi^ {2} = \chi_ {\min } ^ {2} + \left(\delta \kappa - \delta \kappa_ {\text {b e s t}}\right) ^ {T} \Sigma^ {- 1} \left(\delta \kappa - \delta \kappa_ {\text {b e s t}}\right), \tag {B.5}
$$

where the error matrix  $\Sigma \equiv A^T\overline{\Sigma}^{-1}A$  can be obtained from  $\overline{\Sigma}$  through matrix manipulation, and has dimension  $n\times n$ . Note that the error matrix  $\Sigma^{-1}$  is also symmetric. The  $\chi_{\mathrm{min}}^{2}$  can also be expressed analytically,  $\chi_{\mathrm{min}}^{2} = (\mathcal{O}^{\mathrm{exp}} - \mathcal{O}^{\mathrm{th},0})^{T}B^{T}\overline{\Sigma}^{-1}B(\mathcal{O}^{\mathrm{exp}} - \mathcal{O}^{\mathrm{th},0})$ , where  $B\equiv \mathbb{I} - A(A^{T}\overline{\Sigma}^{-1}A)^{-1}A^{T}\overline{\Sigma}^{-1}$ . If the theoretical prediction is consistent with experimental measurement,  $\mathcal{O}_j^{\mathrm{th},0} = \mathcal{O}_j^{\mathrm{exp}}$ , the  $\chi^2$  function reaches the minimum at the SM

values,  $\delta \kappa_{j} = 0$ , which is the best value. This formalism of analytic  $\chi^2$  function can even be used to estimate the statistical fluctuation in  $\chi_{\mathrm{min}}^2$  [113].

In general, different fitting parameters are correlated with each other through the coefficient matrix  $A$  and hence can affect each other. To obtain the precision of a specific fitting parameter, we need to marginalize over the others. This can be done as a series of iterative reductions from higher-dimensional  $\chi^2$  function to lower one, each time reducing the number of fitting parameters by 1. During this process, the  $\chi^2$  function can still be expressed with the quadratic form (B.5) in the fitting parameter basis while the n-dimensional error matrix  $\Sigma$  can be reduced to  $(n - 1)$ -dimensional  $\widetilde{\Sigma}$  by integrating out one degree of freedom, say the  $k$ -th branching fraction,

$$
\widetilde {\Sigma} _ {i j} ^ {- 1} = \Sigma_ {i j} ^ {- 1} - \frac {\Sigma_ {i k} ^ {- 1} \Sigma_ {j k} ^ {- 1}}{\Sigma_ {k k} ^ {- 1}}. \tag {B.6}
$$

Note that there is no summation over  $k$ . This reduction formula is just a reflection of integrating out the  $k$ -th degree of freedom from the probability distribution  $\mathbb{P}(\delta \kappa_j) \equiv \exp(-\chi^2 / 2)$ ,

$$
\mathbb {P} \left(\delta \kappa_ {1} \dots \delta \hat {\kappa} _ {k} \dots \delta \kappa_ {n}\right) = \int_ {- \infty} ^ {+ \infty} \mathbb {P} \left(\delta \kappa_ {1} \dots \delta \kappa_ {k} \dots \delta \kappa_ {n}\right) d \delta \kappa_ {k}. \tag {B.7}
$$

The hat means that the corresponding variable has been integrated out. With quadratic  $\chi^2$ , this is an integration of Gaussian distribution that can be done analytically to produce (B.6). The same procedure should be carried out until there is only one degree of freedom left, say, the  $\ell$ -th anomalous coupling. The only element of the 1-dimensional error matrix is then its uncertainty,  $\Delta (\delta \kappa_{\ell}) \equiv \sqrt{\widetilde{\Sigma}_{\ell\ell}}$ . To deduce the precision of all fitting parameters, we need to run over all possible values of  $\ell$  and make the reduction for each case. This analytic  $\chi^2$  fitting technique, along with other extensions, will be delivered in a general purpose package BSMfitter [106].

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] ATLAS collaboration, Observation of a new particle in the search for the Standard Model Higgs boson with the ATLAS detector at the LHC, Phys. Lett. B 716 (2012) 1 [arXiv:1207.7214] [INSPIRE].  
[2] CMS collaboration, Observation of a new boson at a mass of 125 GeV with the CMS experiment at the LHC, Phys. Lett. B 716 (2012) 30 [arXiv:1207.7235] [INSPIRE].  
[3] F. Englert and R. Brout, Broken symmetry and the mass of gauge vector mesons, Phys. Rev. Lett. 13 (1964) 321 [INSPIRE].  
[4] P.W. Higgs, Broken symmetries, massless particles and gauge fields, Phys. Lett. 12 (1964) 132 [INSPIRE].

[5] P.W. Higgs, Broken symmetries and the masses of gauge bosons, Phys. Rev. Lett. 13 (1964) 508 [INSPIRE].  
[6] G.S. Guralnik, C.R. Hagen and T.W.B. Kibble, Global conservation laws and massless particles, Phys. Rev. Lett. 13 (1964) 585 [INSPIRE].  
[7] T.W.B. Kibble, Symmetry breaking in non-Abelian gauge theories, Phys. Rev. 155 (1967) 1554 [INSPIRE].  
[8] J. Ellis, M.K. Gaillard and D.V. Nanopoulos, An updated historical profile of the Higgs boson, arXiv:1504.07217 [INSPIRE].  
[9] J. Ellis, Summary and outlook: 2015 lepton-photon symposium, in the proceedings of International Symposium on Lepton Photon Interactions at High Energies, Ljubljana Slovenia August 17-22 2015 [arXiv:1509.07336] [INSPIRE].  
[10] N. Arkani-Hamed, Vision for the future, presented at the Workshop on Physics at the CEPC, http://indico.ihep.ac.cn/event/4937, IHEP, Beijing China August 10-12 2015.  
[11] M.E. Peskin, Estimation of LHC and ILC capabilities for precision Higgs boson coupling measurements, in the proceedings of Snowmass, U.S.A. (2013) [arXiv:1312.4974] [INSPIRE].  
[12] D.A. Dicus and H.-J. He, Scales of mass generation for quarks, leptons and Majorana neutrinos, Phys. Rev. Lett. 94 (2005) 221802 [hep-ph/0502178] [INSPIRE].  
[13] D.A. Dicus and H.-J. He, Scales of fermion mass generation and electroweak symmetry breaking, Phys. Rev. D 71 (2005) 093009 [hep-ph/0409131] [INSPIRE].  
[14] K.G. Wilson, The renormalization group and strong interactions, Phys. Rev. D 3 (1971) 1818 [INSPIRE].  
[15] L. Susskind, Dynamics of spontaneous symmetry breaking in the Weinberg-Salam theory, Phys. Rev. D 20 (1979) 2619 [INSPIRE].  
[16] F.L. Bezrukov and M. Shaposhnikov, The Standard Model Higgs boson as the inflaton, Phys. Lett. B 659 (2008) 703 [arXiv:0710.3755] [INSPIRE].  
[17] F. Bezrukov, The Higgs field as an inflaton, Class. Quant. Grav. 30 (2013) 214001 [arXiv:1307.0708] [INSPIRE].  
[18] SNOWMASS 2013 COSMIC FRONTIER WORKING GROUPS 1-4 collaboration, D. Bauer et al., Dark matter in the coming decade: complementary paths to discovery and beyond, Phys. Dark Univ. 7-8 (2015) 16 [arXiv:1305.1605] [INSPIRE].  
[19] S. Arrenberg et al., Working group report: dark matter complementarity, arXiv:1310.8621 [INSPIRE].  
[20] J. Ren and H.-J. He, Probing gravitational dark matter, JCAP 03 (2015) 052 [arXiv:1410.6436] [INSPIRE].  
[21] Y. Bai, V. Barger, L.L. Everett and G. Shaughnessy, Two-Higgs-doublet-portal dark-matter model: LHC data and Fermi-LAT 135 GeV line, Phys. Rev. D 88 (2013) 015008 [arXiv:1212.5604] [INSPIRE].  
[22] J.R. Espinosa, G.F. Giudice and A. Riotto, Cosmological implications of the Higgs mass measurement, JCAP 05 (2008) 002 [arXiv:0710.2484] [INSPIRE].  
[23] J. Ellis, J.R. Espinosa, G.F. Giudice, A. Hoecker and A. Riotto, The probable fate of the Standard Model, Phys. Lett. B 679 (2009) 369 [arXiv:0906.0954] [INSPIRE].

[24] A. Kobakhidze and A. Spencer-Smith, Electroweak vacuum (in)stability in an inflationary universe, Phys. Lett. B 722 (2013) 130 [arXiv:1301.2846] [INSPIRE].  
[25] K. Enqvist, T. Meriniemi and S. Nurmi, Generation of the Higgs condensate and its decay after inflation, JCAP 10 (2013) 057 [arXiv:1306.4511] [INSPIRE].  
[26] M. Fairbairn and R. Hogan, Electroweak vacuum stability in light of BICEP2, Phys. Rev. Lett. 112 (2014) 201801 [arXiv:1403.6786] [INSPIRE].  
[27] K. Enqvist, T. Meriniemi and S. Nurmi, Higgs dynamics during inflation, JCAP 07 (2014) 025 [arXiv:1404.3699] [INSPIRE].  
[28] M. Herranen, T. Markkanen, S. Nurmi and A. Rajantie, Spacetime curvature and the Higgs stability during inflation, Phys. Rev. Lett. 113 (2014) 211102 [arXiv:1407.3141] [INSPIRE].  
[29] K. Kamada, Inflationary cosmology and the Standard Model Higgs with a small Hubble induced mass, Phys. Lett. B 742 (2015) 126 [arXiv:1409.5078] [INSPIRE].  
[30] A. Spencer-Smith, Higgs vacuum stability in a mass-dependent renormalisation scheme, arXiv:1405.1975 [INSPIRE].  
[31] A. Shkerin and S. Sibiryakov, On stability of electroweak vacuum during inflation, Phys. Lett. B 746 (2015) 257 [arXiv:1503.02586] [INSPIRE].  
[32] A. Hook, J. Kearney, B. Shakya and K.M. Zurek, Probable or improbable universe? Correlating electroweak vacuum instability with the scale of inflation, JHEP 01 (2015) 061 [arXiv:1404.5953] [INSPIRE].  
[33] J. Kearney, H. Yoo and K.M. Zurek, Is a Higgs vacuum instability fatal for high-scale inflation?, Phys. Rev. D 91 (2015) 123537 [arXiv:1503.05193] [INSPIRE].  
[34] J.R. Espinosa et al., The cosmological Higgs story of the vacuum instability, JHEP 09 (2015) 174 [arXiv:1505.04825] [INSPIRE].  
[35] J.R. Ellis and D. Ross, A light Higgs boson would invite supersymmetry, Phys. Lett. B 506 (2001) 331 [hep-ph/0012067] [INSPIRE].  
[36] H.-J. He and Z.-Z. Xianyu, Extending Higgs inflation with TeV scale new physics, JCAP 10 (2014) 019 [arXiv:1405.7331] [INSPIRE].  
[37] Z.-Z. Xianyu and H.-J. He, Asymptotically safe Higgs inflation, JCAP 10 (2014) 083 [arXiv:1407.6993] [INSPIRE].  
[38] J. Ellis, H.-J. He and Z.-Z. Xianyu, New Higgs inflation in a no-scale supersymmetric SU(5) GUT, Phys. Rev. D 91 (2015) 021302 [arXiv:1411.5537] [INSPIRE].  
[39] J. Ellis, H.-J. He and Z.-Z. Xianyu, Higgs inflation, reheating and gravitino production in no-scale supersymmetric GUTs, JCAP 08 (2016) 068 [arXiv:1606.02202] [INSPIRE].  
[40] S.-F. Ge, H.-J. He, J. Ren and Z.-Z. Xianyu, Realizing dark matter and Higgs inflation in light of LHC diphoton excess, Phys. Lett. B 757 (2016) 480 [arXiv:1602.01801] [INSPIRE].  
[41] CEPC collaboration, CEPC-SPPC preliminary conceptual design report, http://cepc.ihep.ac.cn.  
[42] M. Ruan, Higgs measurement at  $e^+e^-$  circular colliders, presentation at  $37^{th}$  International Conference on High Energy Physics (ICHEP-2014), Valencia Spain July 2–9 2014 [Nucl. Part. Phys. Proc. 273-275 (2016) 857] [arXiv:1411.5606] [INSPIRE].  
[43] M. Ruan, Higgs physics at CEPC, talk at KITPC, Beijing China July 28 2016.

[44] FCC collaboration webpage, http://cern.ch/FCC-ee.  
[45] TLEP DESIGN STUDY WORKING GROUP collaboration, M. Bicer et al., First look at the physics case of TLEP, JHEP 01 (2014) 164 [arXiv:1308.6176] [INSPIRE].  
[46] D. d'Enterria, Physics at the FCC-ee, arXiv:1602.05043 [INSPIRE].  
[47] H. Baer et al., The International Linear Collider technical design report — volume 2: physics, arXiv:1306.6352 [INSPIRE].  
[48] A. Arbey et al., Physics at the  $e^+ e^-$  linear collider, Eur. Phys. J. C 75 (2015) 371 [arXiv:1504.01726] [INSPIRE].  
[49] K. Fujii et al., Physics case for the International Linear Collider, arXiv:1506.05992 [INSPIRE].  
[50] ILD DESIGN STUDY GROUP collaboration, H. Li et al.,  $HZ$  recoil mass and cross section analysis in ILD, arXiv:1202.1439 [INSPIRE].  
[51] M. McCullough, An indirect model-dependent probe of the Higgs self-coupling, Phys. Rev. D 90 (2014) 015001 [arXiv:1312.3322] [INSPIRE].  
[52] W. Yao, Studies of measuring Higgs self-coupling with  $HH \rightarrow b\bar{b}\gamma \gamma$  at the future hadron colliders, in the Proceedings of Snowmass Community Summer Study (CSS 2013), Minneapolis U.S.A. July 29 - August 6 2013 [arXiv:1308.6302] [INSPIRE].  
[53] H.-J. He, J. Ren and W. Yao, Probing new physics of cubic Higgs boson interaction via Higgs pair production at hadron colliders, Phys. Rev. D 93 (2016) 015003 [arXiv:1506.03302] [INSPIRE].  
[54] A.J. Barr, M.J. Dolan, C. Englert, D.E. Ferreira de Lima and M. Spannowsky, Higgs self-coupling measurements at a 100 TeV hadron collider, JHEP 02 (2015) 016 [arXiv:1412.7154] [INSPIRE].  
[55] C.-R. Chen and I. Low, Double take on new physics in double Higgs boson production, Phys. Rev. D 90 (2014) 013018 [arXiv:1405.7040] [INSPIRE].  
[56] D. Curtin, P. Meade and C.-T. Yu, Testing electroweak baryogenesis with future colliders, JHEP 11 (2014) 127 [arXiv:1409.0005] [INSPIRE].  
[57] A. Azatov, R. Contino, G. Panico and M. Son, Effective field theory analysis of double Higgs boson production via gluon fusion, Phys. Rev. D 92 (2015) 035001 [arXiv:1502.00539] [INSPIRE].  
[58] Q. Li, Z. Li, Q.-S. Yan and X. Zhao, Probe Higgs boson pair production via the  $3\ell 2j + \mathcal{E}$  mode, Phys. Rev. D 92 (2015) 014015 [arXiv:1503.07611] [INSPIRE].  
[59] A.V. Kotwal, S. Chekanov and M. Low, Double Higgs boson production in the  $4\tau$  channel from resonances in longitudinal vector boson scattering at a 100 TeV collider, Phys. Rev. D 91 (2015) 114018 [arXiv:1504.08042] [INSPIRE].  
[60] A. Carvalho, M. Dall'Osso, T. Dorigo, F. Goertz, C.A. Gottardo and M. Tosi, Higgs pair production: choosing benchmarks with cluster analysis, JHEP 04 (2016) 126 [arXiv:1507.02245] [INSPIRE].  
[61] B. Batell, M. McCullough, D. Stolarski and C.B. Verhaaren, Putting a stop to di-Higgs modifications, JHEP 09 (2015) 216 [arXiv:1508.01208] [INSPIRE].  
[62] A. Papaefstathiou and K. Sakurai, *Triple Higgs boson production at a 100 TeV proton-proton collider*, JHEP **02** (2016) 006 [arXiv:1508.06524] [INSPIRE].

[63] D. Curtin and P. Saraswat, Towards a no-lose theorem for naturalness, Phys. Rev. D 93 (2016) 055044 [arXiv:1509.04284] [INSPIRE].  
[64] C.-Y. Chen, Q.-S. Yan, X. Zhao, Y.-M. Zhong and Z. Zhao, Probing triple-Higgs productions via  $4b2\gamma$  decay channel at a 100 TeV hadron collider, Phys. Rev. D 93 (2016) 013007 [arXiv:1510.04013] [INSPIRE].  
[65] Q.-H. Cao, Y. Liu and B. Yan, Measuring trilinear Higgs coupling in WHH and ZHH productions at the HL-LHC, arXiv:1511.03311 [INSPIRE].  
[66] R. Grober, M. Muhlleitner and M. Spira, Signs of composite Higgs pair production at next-to-leading order, JHEP 06 (2016) 080 [arXiv:1602.05851] [INSPIRE].  
[67] K. Hagiwara and M.L. Stong, Probing the scalar sector in  $e^{+}e^{-} \to f\bar{f}H$ , Z. Phys. C 62 (1994) 99 [hep-ph/9309248] [INSPIRE].  
[68] G.J. Gounaris, F.M. Renard and N.D. Vlachos, Tests of anomalous Higgs boson couplings through  $e^{-}e^{+} \to HZ$  and  $H\gamma$ , Nucl. Phys. B 459 (1996) 51 [hep-ph/9509316] [INSPIRE].  
[69] W. Kilian, M. Kramer and P.M. Zerwas, Anomalous couplings in the Higgsstrahlung process, Phys. Lett. B 381 (1996) 243 [hep-ph/9603409] [INSPIRE].  
[70] M.C. Gonzalez-Garcia, Anomalous Higgs couplings, Int. J. Mod. Phys. A 14 (1999) 3121 [hep-ph/9902321] [INSPIRE].  
[71] K. Hagiwara, S. Ishihara, J. Kamoshita and B.A. Kniehl, Prospects of measuring general Higgs couplings at  $e^{+}e^{-}$  linear colliders, Eur. Phys. J. C 14 (2000) 457 [hep-ph/0002043] [INSPIRE].  
[72] V. Barger, T. Han, P. Langacker, B. McElrath and P. Zerwas, Effects of genuine dimension-six Higgs operators, Phys. Rev. D 67 (2003) 115001 [hep-ph/0301097] [INSPIRE].  
[73] S.S. Biswal, R.M. Godbole, R.K. Singh and D. Choudhury, *Signatures of anomalous VVH interactions at a linear collider*, Phys. Rev. D 73 (2006) 035001 [Erratum ibid. D 74 (2006) 039904] [hep-ph/0509070] [INSPIRE].  
[74] J. Kile and M.J. Ramsey-Musolf, *Fermionic effective operators and Higgs production at a linear collider*, Phys. Rev. D **76** (2007) 054009 [arXiv:0705.0554] [INSPIRE].  
[75] S. Dutta, K. Hagiwara and Y. Matsumoto, Measuring the Higgs-vector boson couplings at linear  $e^{+}e^{-}$  collider, Phys. Rev. D 78 (2008) 115016 [arXiv:0808.0477] [INSPIRE].  
[76] R. Contino, C. Grojean, D. Pappadopulo, R. Rattazzi and A. Thamm, *Strong Higgs interactions at a linear collider*, JHEP 02 (2014) 006 [arXiv:1309.7038] [INSPIRE].  
[77] G. Amar et al., Exploration of the tensor structure of the Higgs boson coupling to weak bosons in  $e^+ e^-$  collisions, JHEP 02 (2015) 128 [arXiv:1405.3957] [INSPIRE].  
[78] N. Craig, M. Farina, M. McCullough and M. Perelstein, Precision Higgsstrahlung as a probe of new physics, JHEP 03 (2015) 146 [arXiv:1411.0676] [INSPIRE].  
[79] J. Ellis, V. Sanz and T. You, The effective Standard Model after LHC Run I, JHEP 03 (2015) 157 [arXiv:1410.7703] [INSPIRE].  
[80] A. Falkowski and F. Riva, Model-independent precision constraints on dimension-6 operators, JHEP 02 (2015) 039 [arXiv:1411.0669] [INSPIRE].  
[81] J. Ellis and T. You, *Sensitivities of prospective future e+e- colliders to decoupled new physics*, JHEP **03** (2016) 089 [arXiv:1510.04561] [INSPIRE].

[82] W. Hollik and H.J. Timme, Renormalization scheme dependence of electroweak radiative corrections, Z. Phys. C 33 (1986) 125 [INSPIRE].  
[83] S. Weinberg, *Effective gauge theories*, Phys. Lett. B 91 (1980) 51 [INSPIRE].  
[84] S.R. Coleman, J. Wess and B. Zumino, Structure of phenomenological Lagrangians. 1, Phys. Rev. 177 (1969) 2239 [INSPIRE].  
[85] C.G. Callan Jr., S.R. Coleman, J. Wess and B. Zumino, Structure of phenomenological Lagrangians. 2, Phys. Rev. 177 (1969) 2247 [INSPIRE].  
[86] C.J.C. Burges and H.J. Schnitzer, Virtual effects of excited quarks as probes of a possible new hadronic mass scale, Nucl. Phys. B 228 (1983) 464 [INSPIRE].  
[87] C.N. Leung, S.T. Love and S. Rao, Low-energy manifestations of a new interaction scale: operator analysis, Z. Phys. C 31 (1986) 433 [INSPIRE].  
[88] W. Buchmüller and D. Wyler, Effective Lagrangian analysis of new interactions and flavor conservation, Nucl. Phys. B 268 (1986) 621 [INSPIRE].  
[89] J. Elias-Miro, J.R. Espinosa, E. Masso and A. Pomarol, Higgs windows to new physics through  $D = 6$  operators: constraints and one-loop anomalous dimensions, JHEP 11 (2013) 066 [arXiv:1308.1879] [INSPIRE].  
[90] B. Henning, X. Lu and H. Murayama, How to use the Standard Model effective field theory, JHEP 01 (2016) 023 [arXiv:1412.1837] [INSPIRE].  
[91] S. Antusch, E. Cazzato and O. Fischer, Higgs production from sterile neutrinos at future lepton colliders, JHEP 04 (2016) 189 [arXiv:1512.06035] [INSPIRE].  
[92] S. Antusch and O. Fischer, Testing sterile neutrino extensions of the Standard Model at future lepton colliders, JHEP 05 (2015) 053 [arXiv:1502.05915] [INSPIRE].  
[93] S. Antusch and O. Fischer, Non-unitarity of the leptonic mixing matrix: present bounds and future sensitivities, JHEP 10 (2014) 094 [arXiv:1407.6607] [INSPIRE].  
[94] S. Antusch and O. Fischer, Testing sterile neutrino extensions of the Standard Model at the circular electron positron collider, Int. J. Mod. Phys. A 30 (2015) 1544004 [INSPIRE].  
[95] Q.-H. Cao, H.-R. Wang and Y. Zhang, Probing  $HZ\gamma$  and  $H\gamma\gamma$  anomalous couplings in the process  $e^{+}e^{-}\rightarrow H\gamma$ , Chin. Phys. C 39 (2015) 113102 [arXiv:1505.00654] [INSPIRE].  
[96] J. Cao, C. Han, J. Ren, L. Wu, J.M. Yang and Y. Zhang, SUSY effects in Higgs productions at high energy  $e^+ e^-$  colliders, arXiv:1410.1018 [INSPIRE].  
[97] S.B. Giddings, T. Liu, I. Low and E. Mintun, Unraveling the physics behind modified Higgs couplings: LHC versus a Higgs factory, Phys. Rev. D 88 (2013) 095003 [arXiv:1301.2324] [INSPIRE].  
[98] B. Henning, X. Lu and H. Murayama, What do precision Higgs measurements buy us?, arXiv:1404.1058 [INSPIRE].  
[99] M. Awramik, M. Czakon, A. Freitas and G. Weiglein, Precise prediction for the  $W$  boson mass in the Standard Model, Phys. Rev. D 69 (2004) 053006 [hep-ph/0311148] [INSPIRE].  
[100] A. Alloul, N.D. Christensen, C. Degrande, C. Duhr and B. Fuks, FeynRules 2.0 — a complete toolbox for tree-level phenomenology, Comput. Phys. Commun. 185 (2014) 2250 [arXiv:1310.1921] [INSPIRE].

[101] J. Alwall et al., The automated computation of tree-level and next-to-leading order differential cross sections and their matching to parton shower simulations, JHEP 07 (2014) 079 [arXiv:1405.0301] [INSPIRE].  
[102] J. Ellis and T. You, Updated global analysis of Higgs couplings, JHEP 06 (2013) 103 [arXiv:1303.3879] [INSPIRE].  
[103] C. Englert, R. Kogler, H. Schulz and M. Spannowsky, *Higgs coupling measurements at the LHC*, Eur. Phys. J. C **76** (2016) 393 [arXiv:1511.05170] [INSPIRE].  
[104] X. Mo, G. Li, M.-Q. Ruan and X.-C. Lou, Physics cross sections and event generation of  $e^{+}e^{-}$  annihilations at the CEPC, Chin. Phys. C 40 (2016) 033001 [arXiv:1505.01008] [INSPIRE].  
[105] PARTICLE DATA GROUP collaboration, K.A. Olive et al., Review of particle physics, Chin. Phys. C 38 (2014) 090001 [INSPIRE].  
[106] S.F. Ge, BSMfitter — beyond Standard Model fitter, http://bsmfitter.hepforge.org.  
[107] CEPC DETECTOR WORKING GROUP collaboration, H. Yang et al., Z and W physics at CEPC, presentation at the Fourth International Workshop on Future High Energy Circular Colliders, http://indico.ihep.ac.cn/event/4338/session/2/material/slides/1?contribId=32, Shanghai China September 12-13 2014.  
[108] W. Hollik and G. Duckeck, Electroweak precision tests at LEP, Springer Tracts Mod. Phys. 162 (2000) 1 [INSPIRE].  
[109] J. Ellis, V. Sanz and T. You, The effective Standard Model after LHC Run I, JHEP 03 (2015) 157 [arXiv:1410.7703] [INSPIRE].  
[110] A. Djouadi, J. Kalinowski and M. Spira, HDECAY: a program for Higgs boson decays in the Standard Model and its supersymmetric extension, Comput. Phys. Commun. 108 (1998) 56 [hep-ph/9704448] [INSPIRE].  
[111] Z.-Z. Xing, H. Zhang and S. Zhou, Updated values of running quark and lepton masses, Phys. Rev. D 77 (2008) 113016 [arXiv:0712.1419] [INSPIRE].  
[112] PARTICLE DATA GROUP collaboration, K.A. Olive et al., Review of particle physics, Chin. Phys. C 38 (2014) 090001 [INSPIRE].  
[113] S.-F. Ge, K. Hagiwara, N. Okamura and Y. Takaesu, Determination of mass hierarchy with medium baseline reactor neutrino experiments, JHEP 05 (2013) 131 [arXiv:1210.8141] [INSPIRE].  
[114] A. Djouadi, J. Kalinowski and M. Spira, HDECAY: a program for Higgs boson decays in the Standard Model and its supersymmetric extension, Comput. Phys. Commun. 108 (1998) 56 [hep-ph/9704448] [INSPIRE].