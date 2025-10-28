# Strong first-order phase transitions in the NMSSM — a comprehensive survey

Peter Athron, $^{a}$  Csaba Balazs, $^{a}$  Andrew Fowlie, $^{a,b}$  Giancarlo Pozzo, $^{a}$  Graham White $^{c}$  and Yang Zhang $^{a}$

$^{a}$ ARC Centre of Excellence for Particle Physics at the Terascale, School of Physics and Astronomy, Monash University, Victoria 3800, Australia  
$^{b}$ Department of Physics and Institute of Theoretical Physics, Nanjing Normal University, Nanjing, 210023, China  
cTRIUMF, 4004 Westbrook Mall, Vancouver, British Columbia V6T 2A3, Canada

E-mail: peter.athron@coepp.org.au, csaba.balazs@monash.edu, andrew.j.fowlie@qq.com, biancarlo.pozzo@monash.edu, gwhite@triumf.ca, yang.zhang@monash.edu

ABSTRACT: Motivated by the fact that the Next-to-Minimal Supersymmetric Standard Model is one of the most plausible models that can accommodate electroweak baryogenesis, we analyze its phase structure by tracing the temperature dependence of the minima of the effective potential. Our results reveal rich patterns of phase structure that end in the observed electroweak symmetry breaking vacuum. We classify these patterns according to the first transition in their history and show the strong first-order phase transitions that may be possible in each type of pattern. These could allow for the generation of the matter-antimatter asymmetry or potentially observable gravitational waves. For a selection of benchmark points, we checked that the phase transitions completed and calculated the nucleation temperatures. We furthermore present samples that feature strong first-order phase transitions from an extensive scan of the whole parameter space. We highlight common features of our samples, including the fact that the Standard Model like Higgs is often not the lightest Higgs in the model.

KEYWORDS: Supersymmetry Phenomenology

ARXIV EPRINT: 1908.11847

# Contents

1 Introduction 1  
2 NMSSM 3

2.1 Matching to the THDMS 4

3 Effective potential 5

3.1 Effective potential at zero temperature 5  
3.2 Effective potential at finite temperature 7

4 First-order phase transitions 8  
5 Results 10

5.1 Parameter space, constraints and sampling strategy 10  
5.2 Classification of phase transitions 12  
5.3 Benchmark points 13  
5.4 Reaching the observed SM vacuum 16

5.4.1 The strongest FOPT ends in the SM vacuum 16  
5.4.2 The strongest FOPT does not end in the SM vacuum 21

5.5 Properties of the Higgs bosons 27

6 Conclusions 28

A Field dependent masses 30  
B Numerical methods for FOPTs 32

# 1 Introduction

One of the enduring problems in modern physics is the origin of the baryon asymmetry of the Universe (BAU) [1-3]. This asymmetry cannot be an initial condition in any cosmology that includes inflation, as that would wash out any initial asymmetry. Therefore baryon asymmetry must be produced; however, as yet there is no experimental confirmation of any production mechanism. Any mechanism that produces the BAU must satisfy three criteria [5]:

1. charge (C) and charge-parity (CP) violation,  
2. baryon number (B) violation, and  
3. departure from equilibrium.

The Standard Model (SM) has the ingredients to satisfy all three criteria: there is a CP violating phase in the CKM matrix, B is violated through sphalerons which are unsuppressed at high temperature and there could be departures from equilibrium following two phase transitions (PTs) that occur in the SM vacuum as it cools — the electroweak (EW) and the QCD transition. Quantitatively, however, the CP violating phase in the CKM matrix is far too feeble to produce enough baryon asymmetry. Furthermore the two transitions that occur in the SM at high temperature are both crossover transitions rather than first-order phase transitions (FOPTs) and therefore do not provide a large enough departure from equilibrium (see e.g., ref. [6]). As such one has to look beyond the SM for explanations.

While the origin of the baryon asymmetry is a mystery, its measurement is on a firm foundation. During big bang nucleosynthesis, the baryon asymmetry is an input to the set of Boltzmann equations that govern the production of primordial light elements. Since we can measure some of these primordial abundances (deuterium in particular) with high accuracy, this constrains the baryon asymmetry $^2$  to be [7]

$$
Y _ {B} \equiv \frac {n _ {B}}{s} = 8.2 - 9.4 \times 10 ^ {- 11} (95 \% \mathrm {CL}). \tag{1.1}
$$

Furthermore the baryon asymmetry produces acoustic oscillations in the power spectrum of the cosmic microwave background (CMB) [8]. Observing these oscillations gives an even tighter bound on the BAU,

$$
Y _ {B} = 8. 6 5 \pm 0. 0 9 \times 1 0 ^ {- 1 1}. \tag {1.2}
$$

The fact that there is a concordance between these two unrelated measurement approaches is a triumph of cosmology. Along with dark matter and inflation, the origin of the BAU is a powerful cosmological argument for physics beyond the SM.

Electroweak baryogenesis is a minimal and natural explanation for the origin of the baryon asymmetry in the Universe [3, 9-44]. It utilizes the electroweak phase transition (EWPT) which is known to have occurred in our cosmic history providing the reheating temperature was not unnaturally small. Although this transition is a crossover in the SM, its character may be modified by the introduction of new weak scale bosons such that the transition becomes a strongly FOPT (SFOPT) and proceeds by bubble nucleation. Such a phenomenon is all the more interesting because it might directly be probed by future gravitational wave detectors [45-50].

This mechanism can be in principle realized within supersymmetry. In the Minimal Supersymmetric Standard Model (MSSM) a barrier between the EW symmetric and broken vacuums arises from thermal corrections from stops; however, one requires light stops to catalyze the PT such that it is sufficiently strongly first order [51, 52]. This is all but ruled out by LHC constraints on stop masses [53]. Much more attractive is the possibility of the Next-to-Minimal Supersymmetric Standard Model (NMSSM) [54, 55] where a light singlet scalar can catalyze a strongly first order EWPT [16, 25, 56]. Unlike the stop which catalyzes the PT through thermal effects, the singlet can change the potential such that there is a barrier even at zero temperature.

Electroweak baryogenesis was recently considered within the NMSSM [15, 57-61] and it was found that the baryon asymmetry can vary by an order of magnitude depending on whether the singlet acquires a vacuum expectation value (VEV) before or during the EWPT (with a simultaneous transition providing more efficient baryon production) [59]. Furthermore the baryon yield is proportional to the maximal variation of the ratio of the two Higgs VEVs,  $\Delta \beta$ , and it was shown in refs. [15, 30, 62-65] that  $\Delta \beta$  can be an order of magnitude larger in the NMSSM compared to the MSSM.

In this work we explore the plausibility of EW baryogenesis within the NMSSM, focusing on the PT and leaving CP violation to future work (see [57, 66-78] for various approaches to generating CP violation). We consider the case where the superpartners are all heavy enough to have their thermal contributions Boltzmann suppressed during the transition. Thus we can match our model to a two Higgs doublet model plus a singlet (THDMS). We sample the parameter space to find points with an EW SFOPT. For such points, we investigate the phase structure, that is the evolution of the minima of the effective potential as the Universe cools. This investigation includes determining whether the singlet acquires a VEV during or before the EWPT and it also involves calculating the strength of the PT.

As we focus on the third Sakharov condition (a departure from thermal equilibrium), we do not consider explicit or spontaneous CP violation in the Higgs sector. We instead assume that CP violation enters the Higgs sector radiatively, though remain agnostic about the exact source of CP violation and do not examine constraints on complex phases (such as electric dipole moments). This simplification allows us to focus only on PTs between the ground states of CP-even fields, easing the numerical problem of finding vacua of a multifield scalar potential.

The structure of this paper is as follows. In section 2 we introduce the NMSSM and the THDMS, fixing the notation we will use in the paper. Following this, in section 3 we describe the radiative and finite temperature corrections that we include in our analysis. Then in section 4 we outline the procedure we use to determine if a point in the parameter space has a FOPT or not, and if so calculate the critical temperature and transition strength. The results of our scan are presented in section 5 and finally our conclusions are given in section 6.

# 2 NMSSM

The NMSSM extends the MSSM particle content by adding one singlet superfield,  $\hat{S}$ . Here we work in the  $\mathbb{Z}_3$  symmetric NMSSM where the  $\mu$ -term of the MSSM is forbidden and instead an effective  $\mu$ -term,  $\mu_{\mathrm{eff}} = \lambda \langle S \rangle$ , is generated when the singlet develops a VEV, thus solving the  $\mu$ -problem of the MSSM. The superpotential is given by

$$
\mathcal {W} _ {\mathrm {N M S S M}} = (Y _ {u}) _ {i j} \hat {Q} _ {i} \cdot \hat {H} _ {u} \hat {u} _ {j} ^ {c} + (Y _ {d}) _ {i j} \hat {Q} _ {i} \cdot \hat {H} _ {d} \hat {d} _ {j} ^ {c} + (Y _ {e}) _ {i j} \hat {L} _ {i} \cdot \hat {H} _ {d} \hat {e} _ {j} ^ {c}, + \lambda \hat {S} \hat {H} _ {u} \cdot \hat {H} _ {d} + \frac {1}{3} \kappa \hat {S} ^ {3}, (2. 1)
$$

where a hat is used for superfields,  $i,j\in \{1,2,3\}$  are family indices, and we have introduced the  $\mathrm{SU}(2)_L$  dot product,  $A\cdot B = A^{1}B^{2} - A^{2}B^{1}$ . The discrete  $\mathbb{Z}_3$  symmetry is spontaneously

broken when the Higgs fields or singlet obtain a VEV. We assume that following the strategies of refs. [79-81] domain wall problems can in principle be avoided without impacting any phenomenology.

Under the SM gauge group  $G_{\mathrm{SM}} = \mathrm{SU}(3)_C \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$  the superfields transform as

$$
\hat {Q}: (\mathbf {3}, \mathbf {2}, \frac {1}{6}), \quad \hat {u} ^ {c}: (\bar {\mathbf {3}}, \mathbf {1}, - \frac {2}{3}), \quad \hat {d} ^ {c}: (\bar {\mathbf {3}}, \mathbf {1}, \frac {1}{3}), \quad \hat {L}: (\mathbf {1}, \mathbf {2}, - \frac {1}{2}), \quad \hat {e} ^ {c}: (\mathbf {1}, \mathbf {1}, 1), \tag {2.2}
$$

$$
\hat {H} _ {d}: (\mathbf {1}, \mathbf {2}, - \frac {1}{2}), \quad \hat {H} _ {u}: (\mathbf {1}, \mathbf {2}, \frac {1}{2}), \quad \hat {S}: (\mathbf {1}, \mathbf {1}, 0)
$$

where the first two entries inside the parentheses give the representation under  $\mathrm{SU}(3)_C$  and  $\mathrm{SU}(2)_L$ , respectively, while the third entry gives the  $\mathrm{U}(1)_Y$  hypercharges without GUT normalization.

There are three contributions to the tree-level Higgs potential of the NMSSM:

$$
V _ {\mathrm {N M S S M}} = V _ {F} + V _ {D} + V _ {\text {s o f t}}. \tag {2.3}
$$

Here the  $F$ - and  $D$ -term contributions are

$$
V _ {F} = \left| \lambda S \right| ^ {2} \left(\left| H _ {u} \right| ^ {2} + \left| H _ {d} \right| ^ {2}\right) + \left| \lambda H _ {u} \cdot H _ {d} + \kappa S ^ {2} \right| ^ {2}, \tag {2.4}
$$

$$
V _ {D} = \frac {1}{8} \left(g ^ {2} + g ^ {\prime 2}\right) \left(\left| H _ {u} \right| ^ {2} - \left| H _ {d} \right| ^ {2}\right) ^ {2} + \frac {1}{2} g ^ {2} \left| H _ {u} ^ {\dagger} H _ {d} \right| ^ {2}, \tag {2.5}
$$

where  $g$  and  $g'$  are respectively the  $\mathrm{SU}(2)_L$  and  $\mathrm{U}(1)_Y$  gauge couplings without GUT normalization. Finally, the soft-breaking terms are

$$
V _ {\mathrm {s o f t}} = m _ {H _ {u}} ^ {2} | H _ {u} | ^ {2} + m _ {H _ {d}} ^ {2} | H _ {d} | ^ {2} + m _ {S} ^ {2} | S | ^ {2} + \left[ \lambda A _ {\lambda} S H _ {u} \cdot H _ {d} + \frac {1}{3} \kappa A _ {\kappa} S ^ {3} + \mathrm {h . c .} \right]. (2. 6)
$$

The couplings  $\lambda$  and  $\kappa$  and the corresponding trilinears,  $A_{\lambda}$  and  $A_{\kappa}$ , are in general complex. Three of the four phases, however, may be removed through field redefinitions of  $H_{u}$ ,  $H_{d}$  and  $S$ . Since current LHC limits and the 125 GeV Higgs mass measurements require squarks and gluinos to be TeV-scale, the mass spectrum of the NMSSM must contain a large hierarchy between the SM particles and colored sparticles. Furthermore the states with the largest couplings include both heavy sparticles and light SM particles, i.e., stops and the top quark. Therefore higher-order corrections will always include large logarithms since one cannot choose the renormalization scale  $Q$  to simultaneously minimize  $\ln m_t / Q$  and  $\ln M_{\mathrm{SUSY}} / Q$ . This makes it challenging to perform precise calculations when working in the full theory. To improve the precision of our calculations we will integrate out the heavy superpartners and use an effective field theory (EFT) which contains only the light states. This makes it possible run to  $Q = m_t$  and perform calculations in the EFT which are free from large logarithms.

# 2.1 Matching to the THDMS

Since we want to consider scenarios in which all superpartners are too heavy to impact the PT, we match the NMSSM to a two Higgs doublet model plus a singlet (THDMS), which in this context is an effective field theory of the full NMSSM theory valid below  $M_{\mathrm{SUSY}}$ .<sup>3</sup>

The tree-level potential of a  $\mathbb{Z}_3$  symmetric THDMS model is

$$
\begin{array}{l} V _ {\mathrm {T H D M S}} ^ {\mathrm {t r e e}} = \frac {1}{2} \lambda_ {1} | H _ {d} | ^ {4} + \frac {1}{2} \lambda_ {2} | H _ {u} | ^ {4} + (\lambda_ {3} + \lambda_ {4}) | H _ {u} | ^ {2} | H _ {d} | ^ {2} - \lambda_ {4} | H _ {u} ^ {\dagger} H _ {d} | ^ {2} \\ + \lambda_ {5} | S | ^ {2} | H _ {d} | ^ {2} + \lambda_ {6} | S | ^ {2} | H _ {u} | ^ {2} + \left(\lambda_ {7} S ^ {* 2} H _ {d} \cdot H _ {u} + \text {h . c .}\right) + \lambda_ {8} | S | ^ {4} \tag {2.7} \\ + m _ {1} ^ {2} | H _ {d} | ^ {2} + m _ {2} ^ {2} | H _ {u} | ^ {2} + m _ {3} ^ {2} | S | ^ {2} - (m _ {4} S H _ {d} \cdot H _ {u} + \mathrm {h . c .}) - \frac {1}{3} (m _ {5} S ^ {3} + \mathrm {h . c .}), \\ \end{array}
$$

where the couplings  $\lambda_7$ ,  $m_4$  and  $m_5$  may be complex. Two of the three phases, however, may be removed by redefinitions of  $H_{u}$ ,  $H_{d}$  and  $S$ , leaving a single complex phase, as in the NMSSM. In (2.7) we follow the conventions in refs. [15, 82-84]; in particular the  $|H_u|^2 |H_d|^2$  coefficient is  $\lambda_3 + \lambda_4$ . We match the NMSSM to the THDMS at the scale  $M_{\mathrm{USY}}$  by identifying the tree-level conditions

$$
\lambda_ {1} = \frac {1}{4} \left(g ^ {\prime 2} + g ^ {2}\right), \quad \lambda_ {2} = \frac {1}{4} \left(g ^ {\prime 2} + g ^ {2}\right) + \Delta \lambda_ {2}, \quad \lambda_ {3} = \frac {1}{4} \left(g ^ {2} - g ^ {\prime 2}\right),
$$

$$
\lambda_ {4} = \frac {1}{2} (2 | \lambda | ^ {2} - g ^ {2}), \quad \lambda_ {5} = \lambda_ {6} = | \lambda | ^ {2}, \quad \lambda_ {7} = - \lambda \kappa^ {*}, \quad \lambda_ {8} = | \kappa | ^ {2}, \tag {2.8}
$$

$$
m _ {1} ^ {2} = m _ {H _ {d}} ^ {2}, \quad m _ {2} ^ {2} = m _ {H _ {u}} ^ {2}, \quad m _ {3} ^ {2} = m _ {S} ^ {2}, \quad m _ {4} = A _ {\lambda} \lambda , \quad m _ {5} = - A _ {\kappa} \kappa .
$$

We furthermore included a dominant one-loop threshold correction to the matching for  $\lambda_{2}$

$$
\Delta \lambda_ {2} = \frac {3 y _ {t} ^ {4} A _ {t} ^ {2}}{8 \pi^ {2} M _ {\mathrm {S U S Y}} ^ {2}} \left(1 - \frac {A _ {t} ^ {2}}{1 2 M _ {\mathrm {S U S Y}} ^ {2}}\right). \tag {2.9}
$$

Although we stated the potential and matching conditions for  $\lambda_7$ ,  $m_4$  and  $m_5$  without loss of generality, we later consider only real, CP conserving parameters. As discussed in section 1 we assume that the CP violation demanded by Sakharov's first condition originates in a different sector of the NMSSM, e.g., the squark sector. Although CP violation must enter the Higgs sector through loops, since we only consider the dominant one-loop corrections in the matching, CP violating phases that may appear outside of the Higgs sector do not enter our calculation. At higher orders, however, we would be forced to consider complex parameters and consequently (as later discussed) PTs involving CP-odd fields. An examination of the potential impact this could have is left for future study. Since we match the NMSSM to a THDMS, our results are also applicable to a subspace of the THDMS, which is well-motivated even in the absence of supersymmetry.

# 3 Effective potential

# 3.1 Effective potential at zero temperature

In the  $R_{\xi}$  gauge the one-loop corrections to the potential,  $\Delta V$  , are given by [85]

$$
\begin{array}{l} \Delta V = \frac {1}{6 4 \pi^ {2}} \left(\sum_ {h} n _ {h} m _ {h} ^ {4} (\xi) \left[ \ln \left(\frac {m _ {h} ^ {2} (\xi)}{Q ^ {2}}\right) - 3 / 2 \right] + \sum_ {V} n _ {V} m _ {V} ^ {4} \left[ \ln \left(\frac {m _ {V} ^ {2}}{Q ^ {2}}\right) - 5 / 6 \right]\right) \\ \left. - \sum_ {V} \frac {1}{3} n _ {V} \left(\xi m _ {V} ^ {2}\right) ^ {2} \left[ \ln \left(\frac {\xi m _ {V} ^ {2}}{Q ^ {2}}\right) - 3 / 2 \right] - \sum_ {f} n _ {f} m _ {f} ^ {4} \left[ \ln \left(\frac {m _ {f} ^ {2}}{Q ^ {2}}\right) - 3 / 2 \right]\right). \tag {3.1} \\ \end{array}
$$

where  $Q$  is the renormalization scale,  $m_{i}$  are field dependent  $\overline{\mathrm{MS}}$  masses and the  $n_i$  are the numbers of degrees of freedom for field  $i$ . The first term sums fluctuations of scalar fields, which at the EW breaking minimum can be separated into physical Higgs bosons and Goldstone bosons, the second term sums transverse and longitudinal massive gauge bosons, the third one scalar gauge boson fluctuations, and the final one fermions.

We neglect contributions to the vacuum energy. The numbers of degree of freedom for the particles that we include are

$$
n _ {h _ {i} ^ {0}} = n _ {A _ {i} ^ {0}} = n _ {H _ {i} ^ {+}} = n _ {H _ {i} ^ {-}} = 1, \tag {3.2}
$$

$$
n _ {W ^ {+}} = n _ {W ^ {-}} = n _ {Z} = 3, \tag {3.3}
$$

$$
n _ {t} = n _ {b} = 1 2, n _ {\tau} = 4 \tag {3.4}
$$

for the real scalar, vector and Dirac fermion fields in our model, where  $A_{i}^{0}, H_{i}^{+}$  and  $H_{i}^{-}$  include the physical Higgs states and the Goldstone bosons.

At zero temperature, the minimum of the one-loop potential lies at non-zero values for the Higgs fields, which we refer to as VEVs, and assume may always be written as

$$
\langle H _ {u} \rangle = \frac {1}{\sqrt {2}} \left( \begin{array}{c} 0 \\ v _ {u} \end{array} \right), \quad \langle H _ {d} \rangle = \frac {1}{\sqrt {2}} \left( \begin{array}{c} v _ {d} \\ 0 \end{array} \right), \quad \langle S \rangle = \frac {1}{\sqrt {2}} v _ {S}, \tag {3.5}
$$

where  $v_{u}, v_{d}$  and  $v_{S}$  are real, i.e., we do not consider charge or CP breaking VEVs. As we assume that the VEVs are CP conserving, a tadpole condition forces CP violating phases in the potential to vanish.

To construct the field dependent masses appearing in (3.1), we consider the potential as a function of the fields corresponding to the VEVs, i.e., we consider the  $h_u$ ,  $h_d$  and  $s$  components of the fields,

$$
H _ {u} = \left( \begin{array}{c} H _ {u} ^ {+} \\ \frac {1}{\sqrt {2}} (h _ {u} + i a _ {u}) \end{array} \right), \qquad H _ {d} = \left( \begin{array}{c} \frac {1}{\sqrt {2}} (h _ {d} + i a _ {d}) \\ H _ {d} ^ {-} \end{array} \right), \qquad S = \frac {1}{\sqrt {2}} (s + i \sigma), \qquad (3. 6)
$$

where  $h_u, h_d$  and  $s$  are real. The field dependent masses are functions of  $h_u, h_d$  and  $s$ . In principle, we could consider variation of the charged and CP-odd fields which cannot all be eliminated by gauge fixing. However, because we consider PTs only between charge and CP conserving vacua, we set charged and CP-odd Higgs fields to zero in the field dependent masses. The expressions for the field dependent masses are given in appendix A.

The effective potential also contains explicit dependence on the gauge parameter  $\xi$ . The physical, gauge-independent content of the effective potential may be found through Nielsen identities [88], which express the fact that at extrema,  $\mathfrak{h}$ , the gauge dependence of the effective potential vanishes, since

$$
\frac {\partial V _ {\text {e f f}} (h , \xi)}{\partial \xi} \propto \frac {\partial V _ {\text {e f f}} (h , \xi)}{\partial h}, \tag {3.7}
$$

and thus

$$
\frac {\mathrm {d} V _ {\text {e f f}} (\mathfrak {h} , \xi)}{\mathrm {d} \xi} = \frac {\partial V _ {\text {e f f}} (\mathfrak {h} , \xi)}{\partial \xi} + \frac {\partial \mathfrak {h}}{\partial \xi} \frac {\partial V _ {\text {e f f}} (\mathfrak {h} , \xi)}{\partial h} = 0. \tag {3.8}
$$

The location of the extrema, however, are gauge dependent, i.e.,  $\partial \mathfrak{h} / \partial \xi \neq 0$ . See e.g., refs. [85, 89] for further discussion of this issue. We work in the  $\xi = 1$  (Feynman) gauge. The effective potential furthermore depends on a choice of renormalization scale, which could in fact have greater impact than gauge ambiguities [90].

# 3.2 Effective potential at finite temperature

To describe the conditions of the early Universe we need to take into account temperature corrections. We calculate one-loop finite temperature corrections including daisy terms using the Arnold-Espinosa method [91] in the  $\xi = 1$  (Feynman) gauge. The effective potential can be written as a sum of zero temperature and finite temperature pieces

$$
V _ {\mathrm {e f f}} = V _ {\mathrm {T H D M S}} ^ {\mathrm {t r e e}} + \Delta V _ {\mathrm {T H D M S}} + \Delta V _ {T} + V _ {\mathrm {d a i s y}}. \tag {3.9}
$$

The one-loop thermal corrections in the  $R_{\xi}$  gauge are [85]

$$
\begin{array}{l} \Delta V _ {T} = \frac {T ^ {4}}{2 \pi^ {2}} \left[ \sum_ {h} n _ {h} J _ {\mathrm {B}} \left(\frac {m _ {h} ^ {2} (\xi)}{T ^ {2}}\right) + \sum_ {V} n _ {V} J _ {\mathrm {B}} \left(\frac {m _ {V} ^ {2}}{T ^ {2}}\right) \right. \tag {3.10} \\ \left. - \sum_ {V} \frac {1}{3} n _ {V} J _ {\mathrm {B}} \left(\frac {\xi m _ {V} ^ {2}}{T ^ {2}}\right) + \sum_ {f} n _ {f} J _ {\mathrm {F}} \left(\frac {m _ {f} ^ {2}}{T ^ {2}}\right) \right], \\ \end{array}
$$

where the field dependent masses are the same as those appearing in (3.1) in the previous section, and the expressions for them are given in appendix A. The degrees of freedom,  $n$ , are as in (3.2); we again neglect contributions to the vacuum energy and the thermal functions are

$$
J _ {\mathrm {B} / \mathrm {F}} \left(y ^ {2}\right) = \pm \operatorname {R e} \int_ {0} ^ {\infty} x ^ {2} \ln \left(1 \mp e ^ {- \sqrt {x ^ {2} + y ^ {2}}}\right) \mathrm {d} x. \tag {3.11}
$$

Here the upper/ lower signs are for bosons/fermions. For  $m^2\gg T^2$  the thermal functions are exponentially suppressed by a Boltzmann factor. This ensures that the massive supersymmetric particles that we integrated out do not impact the finite temperature corrections.

The daisy terms are

$$
V _ {\text {d a i s y}} = - \frac {T}{1 2 \pi} \left(\sum_ {h} n _ {h} \left[ \left(\bar {m} _ {h} ^ {2}\right) ^ {\frac {3}{2}} - \left(m _ {h} ^ {2}\right) ^ {\frac {3}{2}} \right] + \sum_ {V} \frac {1}{3} n _ {V} \left[ \left(\bar {m} _ {V} ^ {2}\right) ^ {\frac {3}{2}} - \left(m _ {V} ^ {2}\right) ^ {\frac {3}{2}} \right]\right), \tag {3.12}
$$

where we sum over the Higgs fields (including Goldstone bosons) and massive gauge bosons, and  $\bar{m}^2$  are field dependent mass eigenvalues that include Debye corrections to the tree-level masses in the mass matrices. The Debye corrections add additional  $T$  dependent terms of the form  $c_{\Phi}T^{2}|\Phi |^{2}$  for all complex scalar gauge eigenstates and  $c_{A}T^{2}A_{\mu}A^{\mu}$  for all gauge bosons associated with the original gauge symmetries before EWSB. For the

THDMS we find,

$$
c _ {H _ {u}} = \frac {1}{4 8} \left(3 g ^ {\prime 2} + 9 g ^ {2} + 1 2 y _ {t} ^ {2} + 1 2 \lambda_ {2} + 8 \lambda_ {3} + 4 \lambda_ {4} + 4 \lambda_ {6}\right), \tag {3.13}
$$

$$
c _ {H _ {d}} = \frac {1}{4 8} \left(3 g ^ {\prime 2} + 9 g ^ {2} + 1 2 y _ {b} ^ {2} + 4 y _ {\tau} ^ {2} + 1 2 \lambda_ {1} + 8 \lambda_ {3} + 4 \lambda_ {4} + 4 \lambda_ {5}\right), \tag {3.14}
$$

$$
c _ {S} = \frac {1}{4 8} \left(8 \lambda_ {5} + 8 \lambda_ {6} + 1 6 \lambda_ {8}\right), \tag {3.15}
$$

$$
c _ {W _ {1, 2, 3}} = 2 g ^ {2}, \tag {3.16}
$$

$$
c _ {B} = 2 g ^ {\prime 2}, \tag {3.17}
$$

where the couplings  $g^{\prime}, g, y_{t}, y_{b}$  and  $y_{\tau}$  are as in (A.1). The corrections for the gauge bosons are in the gauge basis before symmetry breaking and every component of a gauge representation receives the same Debye correction. The scalar coefficients are gauge independent, as they originate from a high-temperature expansion of (3.10), in which the dependence on  $\xi$  cancels,

$$
c _ {i j} = \frac {1}{T ^ {2}} \left. \frac {\partial^ {2} \Delta V _ {T}}{\partial \phi_ {i} \partial \phi_ {j}} \right| _ {T ^ {2} \gg m ^ {2}}. \tag {3.18}
$$

The coefficients for the gauge bosons are the same as those of the two-Higgs doublet model, which can be found in the literature [92]. We cross-checked our results in (3.13) - (3.17) against general expressions in ref. [93]. Thus we have described the full finite temperature potential, which is a function of the fields  $h_u$ ,  $h_d$  and  $s$  and the temperature,  $T$ .

# 4 First-order phase transitions

Having constructed the finite temperature effective potential, we investigated whether there was a FOPT in which the vacuum of the potential changed abruptly as the Universe cooled. For such a transition to occur, the potential must exhibit two minima separated by a barrier. The temperature at which the two minima are exactly degenerate is known as the critical temperature. That is, at the critical temperature,  $T_{C}$ , there are minima such that

$$
V _ {\text {e f f}} \left(\mathfrak {h} _ {u}, \mathfrak {h} _ {d}, \mathfrak {s}, T _ {C}\right) = V _ {\text {e f f}} \left(\mathfrak {h} _ {u} ^ {\prime}, \mathfrak {h} _ {d} ^ {\prime}, \mathfrak {s} ^ {\prime}, T _ {C}\right) \tag {4.1}
$$

where caligraphic fonts,  $\mathfrak{h}_u$  etc, indicate a minimum of the scalar potential, i.e.,

$$
\partial_ {h _ {u}} V _ {\text {e f f}} \left(\mathfrak {h} _ {u}, \mathfrak {h} _ {d}, \mathfrak {s}\right) = \partial_ {h _ {d}} V _ {\text {e f f}} \left(\mathfrak {h} _ {u}, \mathfrak {h} _ {d}, \mathfrak {s}\right) = \partial_ {s} V _ {\text {e f f}} \left(\mathfrak {h} _ {u}, \mathfrak {h} _ {d}, \mathfrak {s}\right) = 0. \tag {4.2}
$$

Below the critical temperature, the potential develops a minimum that is deeper than the other minima. The system may tunnel through the barrier to the new vacuum state with the lower minimum [94-96]. As discussed below, however, the transition might not complete.

We developed a  $\mathrm{C}++$  program, PhaseTracer, to map the temperature dependence of the minima of the effective potential and to find potential PTs between them. It enhances the algorithm that was developed in CosmoTransitions [97] to map out the phase structure, and to find out possible PTs between every phase. The numerical method coded in PhaseTracer is briefly described in appendix B. This method is different from the one applied in the code BSMPT [93] and previous works on SFOPTs in the NMSSM [61], which

may only find a single PT between the EW symmetric vacuum and the observed EWSB vacuum. Our method is able to map out a more complicated phase structure and find multiple PTs in it. Of equal importance, by analyzing the phase structure obtained by PhaseTracer, we confirmed that not all potential tunnelings actually take place in the early Universe. This may happen because the tunneling rate is too slow or because the PT is located on a branch of the phase structure that the system never utilizes because it evolved in a different direction.

To exhibit spontaneous EWSB as the Universe cooled, the vacuum of the finite temperature effective potential (3.9) should respect EW symmetry at high temperature, which is 1 TeV in this work, and should violate it at zero temperature. Thus at high temperature the global minimum should lie at the origin,  $h_u = 0$  and  $h_d = 0$ , and at zero temperature the deepest minimum should lie at the observed EWSB VEV. We can use this information to fix the boundaries of the phase structure by finding all minima of the potential at  $T = 0$  and  $T = 1$  TeV and checking that spontaneous symmetry breaking occurs. Starting from  $T = 0$  then we can use PhaseTracer to find all possible PTs.

The strength of such a transition is described by an order parameter. For baryogenesis, we consider the order parameter

$$
\gamma_ {\mathrm {E W}} \equiv \frac {\sqrt {\left(\mathfrak {h} _ {u} - \mathfrak {h} _ {u} ^ {\prime}\right) ^ {2} + \left(\mathfrak {h} _ {d} - \mathfrak {h} _ {d} ^ {\prime}\right) ^ {2}}}{T _ {C}}. \tag {4.3}
$$

The singlet VEV is not included here because it does not affect EW sphalerons. Order parameters of about  $\gamma_{\mathrm{EW}} \gtrsim 1$  are considered strong and could catalyze baryogenesis.

The Nielsen identities in (3.8) imply that the critical temperature is gauge independent, since the effective potential is gauge independent at extrema. Our one-loop truncation of the effective potential, however, means that it is gauge independent only at the tree-level extrema. Thus the critical temperature, which we find from the effective potential at the one-loop minima, is gauge dependent. See ref. [85] for further discussion and a procedure that may enforce gauge independence. The location of the minima, furthermore, and thus the order parameter, always depend on the gauge parameter  $\xi$ .

A first order transition occurs through bubble nucleation and there is a finite probability per unit time and volume for tunneling to a new phase. The new phase dominates once the following condition is satisfied [98, 99],

$$
\frac {S _ {E} \left(T _ {N}\right)}{T _ {N}} \simeq 1 4 0, \tag {4.4}
$$

where  $S_{E}$  stands for the Euclidean bubble action, and  $T_{N}$  is the so-called nucleation temperature. If there is no solution, we conclude that the transition cannot complete. During the scan, we identify all possible PTs without checking whether they successfully nucleate. After classifying phase structures, we check nucleation temperatures for a subset of our samples using CosmoTransitions [97].

# 5 Results

# 5.1 Parameter space, constraints and sampling strategy

To explore all possible PTs in the NMSSM, including strong EWPTs, we sampled the parameter space of the model within the ranges shown in table 1. The first four parameters,  $\lambda$ ,  $\kappa$ ,  $A_{\lambda}$  and  $A_{\kappa}$  are from the tree-level NMSSM potential and enter the matching conditions at tree-level (2.8), while the fifth parameter, the stop trilinear  $A_{t}$  enters at the one-loop level (2.9). These parameters are all defined at the matching scale  $m_{\mathrm{SUSY}}$  which we also take as an input and represents the geometric mean of the left and right soft SUSY breaking masses of the stops, which have been integrated out, i.e.

$$
m _ {\mathrm {S U S Y}} = \sqrt {m _ {\tilde {t} _ {L}} m _ {\tilde {t} _ {R}}}. \tag {5.1}
$$

The final two parameters are the ratio of the Higgs VEVs  $\tan \beta \equiv v_u / v_d$  and the singlet VEV,  $v_{S}$ , which are defined at the top quark mass,  $m_t = 173.1\mathrm{GeV}$ . Therefore our model has eight free parameters.

From these inputs the parameters of the THDMS at  $m_t$  are obtained using FlexibleSUSY-2.1.0 [100, 101], coupled with SARAH-4.12.3 [104-107], which implements the matching and running procedure described in section 2.1, with (2.8) specified as a boundary condition in the FlexibleSUSY model file. Since all running and effective potential calculations are performed in the THDMS it is not necessary to specify any further soft-breaking masses in the NMSSM. Because the quartic coupling  $\lambda$  can always be made positive through field redefinitions, we do not consider negative values for it, but we do consider both negative and positive values for the soft trilinears,  $\kappa$  and  $v_S$ . Lastly, as discussed earlier, for self-consistency we only consider real parameters.

The field dependent masses which enter the one-loop corrections to potential are calculated with FlexibleSUSY, and the thermal functions are evaluated using the implementation described in ref. [108]. We use PhaseTracer to find the phases and critical temperatures by exploring the finite temperature potential between  $T = 0$  and  $T = 1 \mathrm{TeV}$ , as described in section 4. Since this involves varying the field values that enter the field-dependent masses, in principle it is possible that this could re-introduce large logarithms and lead to perturbativity problems, therefore we do not consider VEVs greater than  $1.6 \mathrm{TeV}$ . In practice in all our results the VEVs are significantly smaller than this, and are less than  $300 \mathrm{GeV}$  in all but one very special category of points, therefore this restriction does not have an impact on our results.<sup>7</sup>

The main experimental constraints on the parameter region of interest come from LEP chargino searches and the observed Higgs properties. The Higgs sector of our model must be compatible with observations of an SM-like Higgs boson with a mass close to  $125\mathrm{GeV}$ . The observed Higgs, however, could correspond to any one of the three neutral Higgs bosons in our model. We calculated tree-level reduced couplings between the neutral

Table 1. Ranges and metric of parameters that we scanned in the NMSSM at the SUSY scale. We considered positive and negative  $\kappa$ ,  $v_{S}$  and trilinear couplings. The "hybrid" metric is flat below  $10\mathrm{GeV}$ , and logarithmic elsewhere. The top mass was fixed to its measured value  $173.1\mathrm{GeV}$  [7].  

<table><tr><td>Parameter</td><td>Range</td><td>Metric</td></tr><tr><td>λ</td><td>0, π/2</td><td>flat</td></tr><tr><td>|κ|</td><td>0, π/2</td><td>flat</td></tr><tr><td>|Aλ|</td><td>0, 10 TeV</td><td>hybrid</td></tr><tr><td>|Aκ|</td><td>0, 10 TeV</td><td>hybrid</td></tr><tr><td>|At|</td><td>0, 10 TeV</td><td>hybrid</td></tr><tr><td>mSUSY</td><td>1, 10 TeV</td><td>log</td></tr><tr><td>|vS|</td><td>0, 10 TeV</td><td>hybrid</td></tr><tr><td>tan β</td><td>1, 60</td><td>log</td></tr></table>

Higgs bosons and SM fermions by taking into account mixing between the neutral Higgs bosons. We furthermore calculated one-loop reduced couplings between the Higgs bosons and photons and gluons using FlexibleSUSY routines developed in ref. [109]. By passing this information and the Higgs masses to Lilith-1.1.4_DB-17.05 [110], we find a chisquared,  $\chi_{\mathrm{Higgs}}^2$ , for our Higgs sector from Run I and II measurements of the Higgs boson at the LHC.

We penalized points in tension with LEP bounds on charginos [7] by introducing a chi-squared for the effective  $\mu$ -parameter

$$
\chi_ {\mathrm {L E P}} ^ {2} \equiv \left\{ \begin{array}{l l} 0 & \mu_ {\text {e f f}} \geq 1 0 0 \mathrm {G e V}, \\ \left(\frac {\mu_ {\text {e f f}} - 1 0 0 \mathrm {G e V}}{5 \mathrm {G e V}}\right) ^ {2} & \mu_ {\text {e f f}} <   1 0 0 \mathrm {G e V}. \end{array} \right. \tag {5.2}
$$

We constructed this function to guide our sampling algorithm towards acceptable solutions with  $m_{\tilde{\chi}_1^{\pm}} \gtrsim 100 \mathrm{GeV}$ , rather than precisely reflect experimental constraints from LEP. We furthermore penalized points without an SFOPT by the chi-squared

$$
\chi_ {\mathrm {S F O P T}} ^ {2} \equiv \left(\frac {\log_ {1 0} \gamma_ {\mathrm {E W}}}{0 . 2}\right) ^ {2}. \tag {5.3}
$$

The role of this term is to focus our sampling algorithm on SFOPT with  $\gamma_{\mathrm{EW}} \simeq 1$ ; it is in fact equivalent to a Gaussian penalty  $\log_{10} \gamma_{\mathrm{EW}} = 0 \pm 0.2$ .

Since the parameter space shown in table 1 is eight-dimensional we sampled points from our model using MultiNest-3.10 [111-113] with a chi-squared

$$
\chi^ {2} = \chi_ {\text {H i g g s}} ^ {2} + \chi_ {\text {S F O P T}} ^ {2} + \chi_ {\text {L E P}} ^ {2}. \tag {5.4}
$$

We saved and considered all points evaluated by MultiNest, i.e., we disabled the cuts ordinarily placed on saved points by the MultiNest algorithm. To be consistent with the LHC Higgs measurements and LEP bounds on charginos [7], and to satisfy our SFOPT requirement, we select points with

$$
\chi_ {\mathrm {H i g g s}} ^ {2} - \min  \chi_ {\mathrm {H i g g s}} ^ {2} \leq 6. 1 8, \mu_ {\text {e f f}} \geq 1 0 0 \mathrm {G e V} \text {a n d} \gamma_ {\mathrm {E W}} \geq 1, \tag {5.5}
$$

where  $\min \chi_{\mathrm{Higgs}}^2 = 22.3$  was the minimum  $\chi_{\mathrm{Higgs}}^2$  found in our scan. After that, we further required that remaining points satisfied LHC and LEP bounds on BSM Higgs bosons using HiggsBounds-5.3.2beta [114-118], which we interfaced via NMSSMCALC [119].

# 5.2 Classification of phase transitions

After collecting more than three million valid points, we found that the possible phase structures in the NMSSM harbored rich and novel phenomenology. To reflect this phenomenology, we classify these points into three categories that differ by the nature of the first possible PT in the cosmological history:

1. Type-H-and-S: EW symmetry is spontaneously broken such that at least one Higgs field and the singlet field obtain non-vanishing VEVs simultaneously.  
2. Type-Only-H: EW symmetry is spontaneously broken by one or both Higgs fields obtaining VEVs, but the singlet VEV remains zero.  
3. Type-Only-S: EW symmetry remains unbroken, but the singlet field obtains a VEV. The Higgs obtain non-vanishing VEVs in a SFOPT afterwards, during which the sign of singlet VEV may be maintained or flipped. Thus we further classify this type into two subcategories:

- Type-Only-S(maintain): the strongest PT maintains the sign of singlet VEV.  
- Type-Only-S(flip): the strongest PT flips the sign of singlet VEV.

It is important to understand that at this stage we do not have the means to ensure that a PT is definitely part of the cosmological history. More precisely, for such an extensive sample of parameter points, we are not in the position to calculate nucleation temperatures, actions, decay rates, etc. for each potential transition in the phase structure. For this reason, unless specified otherwise when we say 'PT' we typically mean 'possible PT'.

To simplify our discussion of this non-trivial structure, we introduce the following shorthand notation:

- We denote the minimum value of the potential in a given direction with a calligraphic font. For example,  $\mathfrak{s}$  is a value of singlet field  $s$  at a minimum of the scalar potential.  
- By the triplet of values e.g., (100, 200, 300), we mean  $\mathfrak{h}_u = 100\mathrm{GeV}$ ,  $\mathfrak{h}_d = 200\mathrm{GeV}$ , and  $\mathfrak{s} = 300\mathrm{GeV}$ .  
- At a critical temperature, two vacua are degenerate. However, we always define the true vacuum to be the deepest of these vacua just below the critical temperature, and the other one is the false vacuum in our notation.  
- In case of multiple SFOPTs we refer to the SFOPT with the greatest  $\gamma_{\mathrm{EW}}$  as the strongest one.  
We define

$$
\mathfrak {h} \equiv \operatorname {s i g n} \left(\mathfrak {h} _ {u} \mathfrak {h} _ {d}\right) \sqrt {\mathfrak {h} _ {u} ^ {2} + \mathfrak {h} _ {d} ^ {2}}, \tag {5.6}
$$

as the signed geometric mean of the Higgs fields.

# 5.3 Benchmark points

In figure 1, we present a phase history for a typical point in each category. For these benchmark points, we checked our results with CosmoTransitions and calculated the nucleation temperature for every possible FOPT. The corresponding input parameters, Higgs properties and transition information are shown in table 2. On each panel, the lines show the signed geometric mean of the Higgs fields (left) or the singlet field (right) at a minimum of the potential as a function of temperature. $^{8}$  Two phases linked by an arrow at a given temperature are degenerate and thus a FOPT could occur in the direction indicated by the arrow (i.e., below the critical temperature, the phase at the end of the arrow contains a deeper minimum). When there is more than one possible sequence of FOPTs that leads from the origin at  $T = 1$  TeV to the observed vacuum at  $T = 0$ , we show the FOPTs that belong to the sequence that includes the strongest FOPT by black arrows, and PTs that are not part of that history by gray arrows. Note though that other possible FOPTs between phases that are never degenerate are not marked. For example, in the upper left panel, the minima in phase 2, which appears at about  $T = 88$  GeV, always lies shallower than that in phase 3. A FOPT between them is possible, although there is no critical temperature.

From figure 1 we can see that in all categories at high temperature,  $T > 400 \mathrm{GeV}$ , the true vacuum is always at the origin (as described in section 4 this is a requirement in our scan). In the upper left panel, the first (and only) PT occurs at  $T \lesssim 145 \mathrm{GeV}$  between  $(0,0,0)$  and  $(106,117,276)$  with  $\gamma_{\mathrm{EW}} = 1.09$  and nucleation temperature  $T_N = 116 \mathrm{GeV}$ . Thus it is classified as Type-H-and-S.

In the upper right panel, only one of the Higgs fields,  $h_u$ , develops a VEV during the first crossover transition at  $T = 155\mathrm{GeV}$ . The first transition in the cosmological history was never first order in our Type-0only-H samples. As the Universe cools, however, a deeper minimum exists between  $T = 151\mathrm{GeV}$  and  $T = 124\mathrm{GeV}$  at about (0,0,450), which belongs to phase 2. The FOPT to this deeper minimum would (temporarily) restore EW symmetry; however, we find that it cannot complete as (4.4) cannot be satisfied. If it completed, EW symmetry would subsequently be permanently broken by another SFOPT at  $T \lesssim 123.6\mathrm{GeV}$  which would complete, from (0,0,463) to (91,162,274) with  $\gamma_{\mathrm{EW}} = 1.5$  and  $T_N = 119\mathrm{GeV}$ . Indeed, in all the Type-0only-H samples that we found, EW symmetry was broken, possibly restored and finally broken again, and the final FOPT would be the strongest, just as in this example. However, these sequences of transitions are impossible, as the actions for the transitions that restore EW symmetry are always so large that bubbles cannot nucleate properly. Thus although there appear to be SFOPTs with  $\gamma_{\mathrm{EW}} > 1$  and nucleation temperatures in the Type-0only-H samples, they cannot explain the observed baryon asymmetry of the Universe, as a previous transition in the cosmological history would not complete.

For the Type-Only-S(maintain) point (lower left panel) in the first transition at  $T = 233 \, \mathrm{GeV}$  only the singlet obtains a positive VEV; EW symmetry is broken with the

Table 2. Benchmark points for our four scenarios. All dimensionful quantities are in GeV. The abbreviation vac. is for vacuum and nuc. is for nucleation. The +ve in Type-Only-H means that the field value of vacuum during the 2nd order phase transition is shifted to positive direction.  

<table><tr><td></td><td>Type-H-and-S</td><td>Type-Only-H</td><td>Type-Only-S (maintain)</td><td>Type-Only-S (flip)</td></tr><tr><td>λ</td><td>0.618</td><td>0.607</td><td>0.601</td><td>0.935</td></tr><tr><td>κ</td><td>0.229</td><td>0.191</td><td>0.175</td><td>1.137</td></tr><tr><td>Aλ</td><td>160.1</td><td>160.5</td><td>170.0</td><td>147.4</td></tr><tr><td>Aκ</td><td>-93.7</td><td>-117.5</td><td>-25.2</td><td>61.4</td></tr><tr><td>At</td><td>-21.4</td><td>38.3</td><td>-24.6</td><td>-478.6</td></tr><tr><td>mSUSY</td><td>6374.7</td><td>3463.1</td><td>5857.5</td><td>4164.3</td></tr><tr><td>vS</td><td>307.9</td><td>247.5</td><td>245.7</td><td>183.1</td></tr><tr><td>tanβ</td><td>1.2</td><td>2.0</td><td>2.6</td><td>3.2</td></tr><tr><td>mH1</td><td>91.7</td><td>47.9</td><td>45.6</td><td>126.2</td></tr><tr><td>mH2</td><td>127.4</td><td>124.6</td><td>125.1</td><td>184.4</td></tr><tr><td>mH3</td><td>237.6</td><td>226.6</td><td>252.7</td><td>366.5</td></tr><tr><td>mA1</td><td>167.3</td><td>145.9</td><td>103.8</td><td>145.4</td></tr><tr><td>mA2</td><td>229.7</td><td>225.9</td><td>248.2</td><td>325.8</td></tr><tr><td>mH±</td><td>214.2</td><td>206.7</td><td>233.1</td><td>294.3</td></tr><tr><td>χ2Higgs</td><td>27.0</td><td>25.6</td><td>26.2</td><td>26.4</td></tr><tr><td colspan="5">First PT</td></tr><tr><td>Order</td><td>1st</td><td>2nd at T=155</td><td>1st</td><td>1st</td></tr><tr><td>False vac.</td><td>(0,0,0)</td><td>(0,0,0)</td><td>(0,0,0)</td><td>(0,0,0)</td></tr><tr><td>True vac.</td><td>(106,117,276)</td><td>(0,+ve,0)</td><td>(0,0,182)</td><td>(0,0,-12)</td></tr><tr><td>TC</td><td>145</td><td>N/A</td><td>233</td><td>368</td></tr><tr><td>TN</td><td>116</td><td>N/A</td><td>230</td><td>367</td></tr><tr><td colspan="5">Strongest FOPT</td></tr><tr><td>False vac.</td><td></td><td>(0,0,463)</td><td>(0,0,400)</td><td>(0,0,-188)</td></tr><tr><td>True vac.</td><td>Same as above</td><td>(91,162,274)</td><td>(59,114,349)</td><td>(66,209,179)</td></tr><tr><td>TC</td><td></td><td>124</td><td>121</td><td>104</td></tr><tr><td>TN</td><td></td><td>119</td><td>119</td><td>N/A; no nuc.</td></tr><tr><td>γEW</td><td>1.1</td><td>1.5</td><td>1.1</td><td>2.1</td></tr><tr><td>Ends at SM vac.</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Possible</td><td>Yes</td><td>No; prior PT fails</td><td>Yes</td><td>No; no nuc.</td></tr></table>

![](images/e464321b9a21e625a1164a40722d1e40cb241a26991a0a7d3d43fa988ad0791d.jpg)

![](images/7461281b22889138c2b092e46ff23f6df19da0424593eccf87774f77da3a3c07.jpg)

![](images/d0ccc86c87a3dab4e86e0b68ef31bcd065ae9f62193a8c5e61bffe57e5d636bd.jpg)  
Figure 1. Phase structures for typical points in the categories Type-H-and-S (upper left), Type-Only-H (upper right), Type-Only-S(maintain) (lower left) and Type-Only-S(flip) (lower right). The lines show the field values at a particular minimum as a function of temperature. The arrows indicate that at that temperature the two phases linked by the arrows are degenerate and thus that a FOPT could occur in the direction of the arrow. The dots in the lower panels represent transitions that do not change the corresponding field values. The black arrows and dots show a path that includes the strongest EW FOPT, while the gray ones are not in that path.

![](images/47839928ec0a9889fdc0629a5fe0895a25986a3adbd0257804d190963f4a8dc6.jpg)

sign of singlet VEV maintained in the second (and final) PT at  $T = 121 \, \mathrm{GeV}$ . Both of the transitions are strongly first order and complete. Although transitions in which only the singlet obtains a VEV cannot precipitate baryogenesis, they might nevertheless result in interesting gravitational wave signatures.

Finally, we consider a Type-Only-S(flip) point (lower right panel). The singlet field develops a negative value during the first transition at  $T = 368\mathrm{GeV}$ , which is first-order and completes at  $T_{N} = 367\mathrm{GeV}$ . At  $T \lesssim 368\mathrm{GeV}$ , just below the critical temperature of the first transition, a phase with positive  $\mathfrak{s}$  develops, which is approximately symmetric

with respect to the phase with negative  $\mathfrak{s}$ . Eventually, a second first-order transition at  $T = 104\mathrm{GeV}$  breaks EW symmetry and flips the sign of the singlet by transitioning to this approximately symmetric phase. Although this is the strongest PT, it cannot complete, as the barrier between the phases means that the tunneling action is too large for (4.4) to be satisfied. This phenomenon appears in a large fraction of our Type-0only-S(flip) samples.

Phase histories of types Type-H-and-S and Type-Only-S(maintain) were previously investigated in refs. [15, 59-61]; however, the richer phase histories in Type-Only-H and Type-Only-S(flip) have not been discussed in the literature as far as we are aware. Note that the barrier between the minima in the Type-Only-H and Type-Only-S(flip) are usually so high that the tunneling may not happen. This shows the importance of studying phase structure as well as calculating the transition strength.

We also checked the robustness of our results against the change of the renormalization scale. For the Type-H-and-S benchmark point in table 2, we found a mild  $(1\% - 2\%)$  variation of the critical temperature and the transition strength as the renormalization scale changes in the  $(m_t / 2, 2m_t)$  range. We furthermore checked gauge dependence by repeating our calculations for our benchmark points in the  $\xi = 0$  (Landau) gauge. We found, as anticipated, that gauge dependence was present but typically mild, especially for the critical temperatures. The gauge dependence could, nevertheless, motivate the application of gauge independent techniques in future works.

# 5.4 Reaching the observed SM vacuum

During the scan we required that the deepest minimum at zero temperature agreed with the observed VEV,  $\mathfrak{h} = 246\mathrm{GeV}$ . We call the phase associated with the observed VEV the SM vacuum. We split our samples by two ways of reaching the SM vacuum. First, in section 5.4.1 we consider samples for which the strongest SFOPT ends in the SM vacuum, which changes smoothly to  $\mathfrak{h} = 246\mathrm{GeV}$  at  $T = 0$ . Second, in section 5.4.2 we consider samples for which the strongest FOPT does not end in the SM vacuum. As we discuss, such samples must feature at least one further FOPT that ultimately ends in the observed vacuum at  $T = 0$ . In both cases, the Type-Only-H scenario was by far the rarest, with noticeably few samples shown in the following scatter plots.

# 5.4.1 The strongest FOPT ends in the SM vacuum

We selected samples in which the strongest FOPT ended in the SM vacuum. For our samples, it was sufficient to check that  $\mathfrak{h}_u > 0$  GeV and  $\mathfrak{h}_d > 0$  GeV for the true vacuum of strongest FOPT. All of our benchmark points in table 2 are in this category. In figure 2, we present the true and false minima of the strongest FOPT at the critical temperature. It demonstrates some features of each of the types of point that we described above. For Type-H-and-S, the first transition, in which the Higgs and singlet fields acquire VEVs, is usually also the strongest FOPT. There are however three exceptional points where the singlet field values at the false minimum are non-zero. They have similar phase structures to the upper right panel of figure 1 except that the minima of phase 1 is always deeper than the minima of phase 2 in all three cases. Thus there is no critical temperature between these phases, and so the strongest FOPT for these three points is not in the cosmological history.

![](images/9cbad7a9233332e1895d943ae955abdaed645bfb05cac16d7081d70a9e70d379.jpg)

![](images/6911fbb012679c8d89a210b67a365900dded006887b67e13ebf4796c90f09e8a.jpg)

![](images/eb8c410b98c909f998a9dc3de882bda82628ddc3ae6fb77cc93bffe81bca0a76.jpg)  
Figure 2. The Higgs and singlet field values at the true and false minima at the critical temperature of the strongest FOPT for samples for which the strongest FOPT ends in the SM vacuum.

![](images/0f5172402582c00cb73242ef5c003722db9cad872b61b122c101240e891d14d3.jpg)

According to the definition of Type-Only-H, only the Higgs fields obtain VEVs in the first transition in the history, while the upper right panel of figure 2 shows that the false vacuums of strongest FOPT have zero Higgs VEVs,  $\mathfrak{h}_u = \mathfrak{h}_d = 0$ , but a non-vanishing singlet VEV,  $\mathfrak{s} \neq 0$ . This means that there must be an intermediate transition that restores EW symmetry and generates a singlet VEV. Since the number of Type-Only-H scenarios that we found are quite small, we checked each one in detail. We found that this intermediate transition exists for all Type-Only-H samples, but the corresponding tunneling probabilities are too small. Nonetheless it is possible that there exist scenarios of this type where the transition does complete.

The lower panels of figure 2 display samples of Type-0only-S where the strongest FOPT maintains (left) or flips (right) the sign of the singlet VEV. We see that the singlet VEV can evolve to up to  $1.6\mathrm{TeV}$  after the first transition, and then shifts to about  $150\mathrm{GeV}$  to  $650\mathrm{GeV}$  during the strongest FOPT. The singlet VEV  $\mathfrak{s}$  of the true vacuum can be both

![](images/395aa852419ee973eee6b25129b05081da1ca54bb063bc7bd518f2f4015467b5.jpg)

![](images/aef1acd91030825ef897a3f6615017ae41ad0999dbaff5f36983d5074b8d36e4.jpg)

![](images/58d6bff9f3560a3a0d2d4a740727aa3f0b439e74f80ee606ee17f323eef0ef1e.jpg)  
$T_{C}$  of the strongest FOPT (GeV)

![](images/0518ba04ec6d427069f4717494a8173c14b93bfaac9e12e3c13bd222c35e58d0.jpg)  
Figure 3. The critical temperature and order parameter for the strongest PTs for samples for which the strongest FOPT ends in the SM vacuum. The points are colored by the effective  $\mu$ -parameter.  
$T_{C}$  of the strongest FOPT (GeV)

positive or negative, because the input  $v_{S}$  includes both signs. We have checked that the singlet VEV at the true vacuum has the same sign as the input  $v_{S}$ .

In all scenarios, the spread in the possible true vacuum for the Higgs fields at the critical temperature is small, and typically it matches and rarely exceeds the input EWSB vacuum, i.e.,  $\mathfrak{h} \lesssim 246\mathrm{GeV}$ . This can be further seen in figure 3, which shows the FOPT strength against the critical temperature. The strength lies close to what it would be if  $\mathfrak{h} = 246\mathrm{GeV}$  (dashed gray line). For higher critical temperatures, however, deviations from the gray line are visible, as the thermal loop-corrections are relevant. The thermal loop-corrections tend to make the potential more convex, thus decreasing  $\mathfrak{h}$  at the critical temperature and the strength of the PT.

We now delineate the regions of the NMSSM parameter space in which our four scenarios occur. We checked that in all scenarios the stops were truly decoupled by checking stop mixing,  $X_{t} = A_{t} - \mu_{\mathrm{eff}}\cot \beta$ , which could potentially split the stop mass eigenvalues making one of them light. We found that most samples were actually concentrated within

![](images/8cd4c78629eef7e5fa3819ae902aa9c3022a6c597e86628650a7cd2d6bfe5f6f.jpg)

![](images/e72396baab4378539289263c39d21a551c4755db3b37967217060238a2420cdf.jpg)

![](images/f12a5e9c0a60eb269748bc268238b6ef8838d4e99cf90f06753bc1d03cb21bb9.jpg)  
$\mu$  (GeV)  
Figure 4. The parameters  $(\mu_{\mathrm{eff}}, \tan \beta)$  for samples for which the strongest FOPT ends in the SM vacuum. The points are colored by the  $\gamma_{\mathrm{EW}}$  of the strongest FOPT.

![](images/a5d4ce1dd948c7d48f26602026209cbaed81566f66367ac06c502cf2ece7ae22.jpg)  
$\mu$  (GeV)

the range  $-m_{\mathrm{SUSY}} \leq X_t \leq m_{\mathrm{SUSY}}$  and no particular value of  $m_{\mathrm{SUSY}}$  was preferred by our samples.

In figure 4 we show that the Higgs sector parameters ( $\mu_{\mathrm{eff}}$ ,  $\tan \beta$ ) are severely constrained. Indeed, the Type-H-and-S and Type-Only-H scenarios require  $\tan \beta \lesssim 3$ , whereas the Type-Only-S(maintain) and Type-Only-S(flip) scenarios permit  $\tan \beta \lesssim 7$  and  $\tan \beta \lesssim 17$ , respectively. For all types, the upper limit of  $\tan \beta$  decreases with  $\mu_{\mathrm{eff}}$  increasing. The effective  $\mu$ -parameter, and thus the higgsinos, are always light,  $|\mu_{\mathrm{eff}}| \lesssim 300\mathrm{GeV}$ . Thus we find further motivation for scenarios with small  $\mu_{\mathrm{eff}} \lesssim 1\mathrm{TeV}$ , which are also motivated by naturalness, and we anticipate that the searches for higgsinos at the LHC could be sensitive to our models. Samples with  $\mu_{\mathrm{eff}} < 0$  were extremely rare in the Type-H-and-S and Type-Only-S(maintain) scenarios, and not present in the Type-Only-H samples.

We see, furthermore, in figure 5, that quartic couplings of around  $\lambda \approx 0.6$  and  $\kappa \approx 0.2$  could result in an SFOPT in all our scenarios, though a broad range of couplings result in SFOPTs in Type-0only-S(flip) scenario, including couplings with values far above the

![](images/5de4b1be0eef7a930e04bb6e080474b329aea252eb38280064816ee1e5be8458.jpg)

![](images/05d77545b0982e57351b5b10cc6c78f606a43e85e06f27a3d07de2f99ab66595.jpg)

![](images/9d6e605a6286b9a672d3aa617347a41dae43846be2c5e53a164e23de68e95cc0.jpg)  
Figure 5. The quartics  $(\lambda, \kappa)$  for samples for which the strongest FOPT ends in the SM vacuum. The points are colored by the  $\gamma_{\mathrm{EW}}$  of the strongest FOPT.

![](images/4cf812bf72a3c62b51c83f854f5677cdeaf3396a92b1d25d46f12f62a8add7b4.jpg)

limits that would be set if we required perturbativity up to the GUT scale. The constraints strongly prefer that  $\lambda \kappa > 0$ , a combination that is invariant under the field redefinition  $S \rightarrow -S$ . Since we worked in a  $\lambda > 0$  convention, the inequality  $\lambda \kappa > 0$  is equivalent to  $\kappa > 0$ . In the Type-Only-S (maintain) scenarios, however, we find a few solutions for which  $\kappa < 0$ .

Figure 6 shows the trilinear couplings  $(A_{\lambda}, A_{\kappa})$  with the quartic coupling  $\kappa$  shown by the color bar. The trilinears play an important role. As different types of sample require different sign of singlet VEV at low temperatures, the parameter space of each type shows distinguishable tendency. The samples in Type-H-and-S, Type-Only-H and Type-Only-S(maintain) scenarios are concentrated at negative  $A_{\kappa}$  with positive  $\kappa$  or positive  $A_{\kappa}$  with negative  $\kappa$ , as well as a horizontal slice of points at  $A_{\kappa} \approx 10\mathrm{GeV}$  for Type-H-and-S and Type-Only-S(maintain). On the other hand,  $A_{\lambda}$  is typically positive but  $\lesssim 500\mathrm{GeV}$ . The one point with negative  $A_{\lambda}$  in Type-H-and-S and the two points with negative  $A_{\lambda}$  in Type-Only-S(maintain) correspond the point of negative  $\mu_{\mathrm{eff}}$  in

![](images/e3a52366eb815791bafa4317cc03ec56fd824dab3093a794eb3f139d2876ad3c.jpg)

![](images/54812e9c570ab08f3158ab2d982d11597a674f211bfdfc31de8cb52f703e0e2c.jpg)

![](images/ce7e2b475698c5c771db1f3e476a01726c3cefb4c575bf0855fdb140d39898fc.jpg)  
Figure 6. The trilinears  $(A_{\lambda}, A_{\kappa})$  for samples for which the strongest FOPT ends in the SM vacuum. The points are colored by the parameter  $\kappa$ .

![](images/990735127ffd535bd51f32c508af0c49dbeb9f71d574342116c04a6ada65305c.jpg)

figure 4. The distinction between Type-H-and-S and Type-Only-S(maintain) is that Type-Only-S(maintain) favors smaller  $A_{\kappa}$  and  $A_{\lambda}$ . Finally, Type-Only-S(flip) shows two approximately symmetric regions that were previously identified in figure 4 by the sign of  $\mu_{\mathrm{eff}}$ . The region of positive (negative)  $A_{\lambda}$  and  $A_{\kappa}$  corresponds to positive (negative)  $\mu_{\mathrm{eff}}$ .

We emphasize again that the parameter spaces shown in figure 4, figure 5 and figure 6 can only ensure the existence of a SFOPT with  $\gamma_{\mathrm{EW}} \gtrsim 1$ . Establishing whether this SFOPT is definitely part of the cosmological history requires further investigation, which we only present for our benchmark points.

# 5.4.2 The strongest FOPT does not end in the SM vacuum

Other than the scenario discussed above, we have plenty of samples in which the strongest FOPT does not end in the SM vacuum, as shown in figure 7. In these samples, in the true vacuum for the strongest FOPT,  $\mathfrak{h}$  is always negative and  $\mathfrak{s}$  is either zero or has a different sign to  $\mu_{\mathrm{eff}}$ , so this almost certainly does not belong to the SM vacuum in which  $\mathfrak{h} = 246\mathrm{GeV}$ . The spread in the possible true vacuum for the Higgs fields at the critical

![](images/e9a0593e6184ffb87c54e944bd23b45ad1461c4b56f3824e2764ce967641f42d.jpg)

![](images/09077a0fad772db491ecbc6c3985101090ce54d95e9aafb6f3c470a1da2a5177.jpg)

![](images/da30682f131bbe66ceab43dafe236f4c1fa2ca1d2e81ad15bcfb7086c4728262.jpg)  
Figure 7. The Higgs and singlet fields at the critical temperature of the strongest FOPT for samples for which the strongest FOPT does not end in the SM vacuum.

![](images/834fffaf40908612734ba91dd7f1a479642811660e51d0ed7a8bcf938f497ec5.jpg)

temperature is substantial, and could differ considerably from the observed EW vacuum. Because of this, we no longer find that  $\mathfrak{h} \approx 246\mathrm{GeV}$ , allowing enhancement or suppression of the strength of the PT in figure 8, which differs markedly from figure 3. Indeed, in the Type-Only-S(maintain) scenario, SFOPTs are possible for substantial critical temperatures of up to  $T_{C} \lesssim 500\mathrm{GeV}$ .

At first glance, these points might seem uninteresting, as they do not end in the correct zero-temperature vacuum. They may be especially interesting, however, as this means that in order for such samples to achieve the correct zero-temperature vacuum, there must be another EW FOPT transition or sequence of transitions that complete and end in the correct vacuum. Thus in figure 9 we histogram the number of possible FOPTs with  $\gamma_{\mathrm{EW}} \gtrsim 1$  for each sample. Let us stress that strictly speaking, we count the number of temperatures at which two vacua are degenerate. This differs from the number of FOPTs that can take place in one cosmological history, since only particular routes through the

![](images/c067d5024b52adf681f0b3539f3460df2fe7531ef029a11a9f9d660dd03000d7.jpg)

![](images/d0734b88e90e7ae2dc0d0e4ba2ed307ebd702977440dffba639c7983b95895c5.jpg)

![](images/69daa2e0d36b27730427ef2324fd540c4e572aa6a8efa8652a32eed059f54254.jpg)  
$T_{C}$  of the strongest FOPT (GeV)

![](images/3cb35ce68d7501cc811325a2508f6cae83b8d7fcfbf27058546268f0e4f80bcc.jpg)  
Figure 8. The critical temperature and order parameter for the strongest PTs for samples for which the strongest FOPT does not end in the SM vacuum. The points are colored by the effective  $\mu$ -parameter.  
$T_{C}$  of the strongest FOPT (GeV)

phases are possible. For example the upper right panel of figure 1 exhibits one or two FOPTs from phase 1 to phase 3, but we would count this though as three. Furthermore FOPTs may also occur between phases that were never degenerate, but such possibilities are not included in our count.

For the samples that end in the SM vacuum (left panel), there is usually a single FOPT with  $\gamma_{\mathrm{EW}} > 1$ , except in the Type-Only-H scenario, in which there are often two FOPTs with  $\gamma_{\mathrm{EW}} > 1$ . For the samples that do not end in the SM vacuum (right panel), almost all of Type-Only-H and Type-Only-S (maintain) samples and about half the Type-H-and-S samples have more than one EW SFOPTs. We also checked that for most of them the second strongest FOPT does end in the SM vacuum.

Thus, without further calculations, the samples for which the strongest FOPT does not end in the SM vacuum could still potentially explain the observed baryon asymmetry. We display the parameter spaces in figure 10, figure 11 and figure 12. Compared to the

![](images/a3746f1d3a2e03b106586d29d34bfe7e7d31777706ca05671b4c9a8ede605219.jpg)  
The strongest FOPT ends in the SM vacuum

![](images/e56ffcf53e8ae4d6ce4c168139e2c238a0f1ef1dcb08eceb6bac30b4e4336f2d.jpg)  
Figure 9. Number of FOPTs with  $\gamma_{\mathrm{EW}} \gtrsim 1$  per point, for points for which the strongest FOPT ends in the SM vacuum (left panel) and does not end in the SM vacuum (right panel).  
The strongest FOPT does not end in the SM vacuum

![](images/97c647f66f55505a49921ba77c2debc9378579bf0ae96870bfcc3461a52fd4a4.jpg)

![](images/a565c96bdca82e047a589c04cbb6af425b209b343829ff2a9b6ce89197591266.jpg)

![](images/a304d9a7056011610c195bdd43d4f9690728646de02fa88054b3c226f8a3de64.jpg)  
$\mu$  (GeV)  
Figure 10.  $(\mu_{\mathrm{eff}}, \tan \beta)$  for samples for which the strongest FOPT does not end in the SM vacuum. The points are colored by the  $\gamma_{\mathrm{EW}}$  of the strongest FOPT.

![](images/ecf9dda327fd1ae5ed9bc0deb6cf6c04cf87abecb0e085900945da7f2a7f0e37.jpg)  
$\mu$  (GeV)

![](images/86c30accc44325f170318ac914e11846a1d7cb06a90e1c0d50b3c3e220f6c7bb.jpg)

![](images/0c341d17f637e9aa1b48602c0851830ad80eced8185ff5b265cc32353afc5ea7.jpg)

![](images/9a58664ba2783593e7602522a2f254f8dcd4d84632af8058a6435680df1177b3.jpg)  
Figure 11.  $(\lambda, \kappa)$  for samples for which the strongest FOPT does not end in the SM vacuum. The points are colored by the  $\gamma_{\mathrm{EW}}$  of the strongest FOPT.

![](images/35320aa9aef16f885ed6d2be6000d22e951c69a34234d96ec803d69ec85c0c4d.jpg)

scenario in which the strongest FOPT ends in the SM vacuum, the parameter spaces of Type-H-and-S and Type-Only-H are roughly unchanged, while Type-Only-S(maintain) and Type-Only-S(flip) exchange parameter spaces with each other. This is because here the Type-Only-S(maintain) (Type-Only-S(flip)) requires a minimum on the singlet axis with  $\mathfrak{s} < 0$  ( $\mathfrak{s} > 0$ ), opposite to the Type-Only-S(maintain) (Type-Only-S(flip)) scenarios in which the strongest FOPT ends in the SM vacuum.

From figure 10 we see that the constraints on the effective  $\mu$ -parameter are stricter than they are in the scenario in which the strongest FOPT ends in the SM vacuum, especially for small  $\tan \beta$ . The Type-H-and-S, Type-Only-H and Type-Only-S(flip) scenarios require an effective  $\mu$ -parameter smaller than about  $200\mathrm{GeV}$ , whereas the Type-Only-S (maintain) permits  $\mu_{\mathrm{eff}} \lesssim 400\mathrm{GeV}$ . The slender bar in the Type-Only-S(maintain) scenario at  $\tan \beta \simeq 1$  and  $\mu_{\mathrm{eff}} \in [200,400]\mathrm{GeV}$  corresponds to samples with  $T_{C} \gtrsim 200\mathrm{GeV}$  for the strongest FOPT, displayed in the lower left panel of figure 8.

In figure 11, a visible difference appears in Type-Only-S(maintain) compared to figure 5. The parameter space of  $\lambda$  and  $\kappa$  splits into two separate regions, and relatively

![](images/179a1e021e8fb916a05ec770f157a1a574db107af6446140dfcf5d38675d38e8.jpg)

![](images/a8bd1c3c591a54cc9ef9ab65d819d99437aaa73f4edaa260017cf3c17041f529.jpg)

![](images/5485839464d9058ed09f4f151384031099a908e4eb2dc05fafa24c87872642d3.jpg)  
Figure 12.  $(A_{\lambda}, A_{\kappa})$  for samples for which the strongest FOPT does not end in the SM vacuum. The points are colored by the  $\kappa$ -parameter.

![](images/2729549aacbb33b248cd86106d49775525a64fe387539edc1ea472e80d40407e.jpg)

large  $\lambda \gtrsim 0.5$  is favored. For instance, when  $\kappa \simeq 1.4$ , here  $\lambda$  is always larger than 1, whereas in lower left panel of figure 5  $\lambda$  can be as low as 0.5.

On the trilinear couplings  $(A_{\lambda}, A_{\kappa})$  plane, there are two additional regions in the Type-Only-S(maintain) scenario (lower left, figure 12) compared to the Type-Only-S(flip) samples for which the strongest FOPT end in the SM vacuum (lower right, figure 6). First, there is an additional region at  $A_{\lambda} \simeq 0\mathrm{GeV}$ . This region corresponds to the previously mentioned region at  $\tan \beta \simeq 1$  and  $\mu_{\mathrm{eff}} \in [200,400]\mathrm{GeV}$ , with  $T_{C} \gtrsim 200\mathrm{GeV}$  for the strongest FOPT. Second, there is an additional region at  $A_{\kappa} \simeq -50\mathrm{GeV}$  and  $A_{\lambda} > 0$ . This region is similar to one in the Type-Only-S(flip) scenario (lower right, figure 12). Indeed, for this region, as well as the strongest FOPT that maintains the sign of singlet, there is another weaker FOPT that flips the sign of singlet.

In summary, the scenario in which the strongest FOPT does not end in the SM vacuum introduces new interesting regions of parameter space that were not covered by the scenarios in which the strongest FOPT ends in the SM vacuum. These scenarios may be especially interesting because they could be followed by additional FOPTs. However, at the same

time there is an additional requirement to ensure that the subsequent transitions actually lead to the EW breaking phase we observe today, which we have not checked.

# 5.5 Properties of the Higgs bosons

As shown by our benchmark points, although our points pass experimental constraints from LEP and the LHC, our scenarios are not in a decoupling regime in which Higgses other than the  $125\mathrm{GeV}$  one are heavy. This is not surprising since it is well known that in the NMSSM a light singlet Higgs state plays an important role in generating a FOPT that breaks EW symmetry [16, 25, 56], without the need for light stops which are heavily constrained by LHC searches [120, 121]. In fact, in all our benchmarks, all Higgs bosons are lighter than about  $400\mathrm{GeV}$ , while there are always at least two CP even Higgs states with masses below  $600\mathrm{GeV}$  in the samples from our scan, with the SM-like Higgs being either  $h_1$  or  $h_2$ .

In figure 13 we show the masses of the non-SM-like CP even neutral Higgs bosons in our four scenarios by plotting the mass of  $h_3$ , which is never SM-like, against the mass of the Higgs (either  $h_1$  or  $h_2$ ) that did not play the role of the SM-like Higgs. Samples that are allowed by experimental constraints are shown by green points. We also show excluded samples to aid explanations (gray and blue points).

For the samples where the strongest FOPT ends in the SM vacuum we see that the SM-like Higgs is actually the next to lightest CP even Higgs for almost all allowed samples (green points) in Type-H-and-S, Type-Only-H and Type-Only-S(maintain), with just three exceptions that all appear in the Type-H-and-S samples. In contrast, in the Type-Only-S(flip) scenarios, the SM-like Higgs can be either the lightest Higgs or the next to lightest Higgs. The samples where the strongest FOPT does not end in the SM vacuum show very similar results, but as usual the patterns of the Type-Only-S(maintain) and Type-Only-S(flip) scenarios are exchanged.

The reason we see so few samples where the SM-like Higgs is the lightest state for the categories mentioned above seems to be the constraints on the observed Higgs. We note that, although it is not clear in the plot, for these types of scenarios there are already a significantly larger number of gray points where the SM-like Higgs is the second lightest CP even Higgs boson than there are for the case where it is the lightest. Applying the constraints on the SM-like Higgs from Lilith-1.1.4_DB-17.05 then reduces the number of samples where it is the lightest to almost zero. The samples excluded by HiggsBounds-5.3.2beta in Type-Only-S(flip) scenario for which the strongest FOPT ends in the SM vacuum and Type-Only-S(maintain) scenario for which the strongest FOPT does not end in the SM vacuum (shown by blue points) are mainly excluded by an LHC search for a scalar resonance decaying to a pair of  $Z$  bosons [122]. It is also worth noting that even without the requirement of an SFOPT, similar observations have been made in the NMSSM previously. A preference for the SM-like Higgs being the next to lightest one was also found in a global analysis of the NMSSM [123] that did not consider PTs.

Lastly, we note that many of the panels in figure 13 appear to indicate an upper bound on the mass of the heaviest Higgs,  $m_{h_3}$ , in each scenario. For example, for the Type-H-and-S scenario in which the strongest FOPT ends in the SM vacuum, the samples allowed

![](images/ad1e1b93c8f29767fd9b2185ff70866018a8bcd4e64a6e123513e5b213ce0d5c.jpg)  
Figure 13. Masses of the non-SM-like Higgs bosons in our four scenarios, for points for which the strongest FOPT ends in the SM vacuum (left block of four plots) and does not end in the SM vacuum (right block of four plots). We show points satisfying  $\mu > 100\mathrm{GeV}$  and  $\gamma_{\mathrm{EW}} > 1$  (gray), further allowed by Lilith-1.1.4_DB-17.05 [110] constraints on the SM-like Higgs (blue), and by HiggsBounds-5.3.2beta [114-118] constraints on non-SM-like Higgses (green). The vertical red line indicates  $m_h = 125\mathrm{GeV}$  in each panel.

![](images/b68fab7fc789949a0fb1b97ca0d1550a54e6f6891863e837a70e64e5850a2255.jpg)

by collider constraints on Higgs bosons (green points) stop at about  $m_{h_3} \lesssim 500\mathrm{GeV}$ . However, despite collecting more than three million samples, we judged our coverage at the largest Higgs masses to be inadequate to reliably address the question of whether upper bounds on the Higgs masses exist, as large masses may just be rare with our sampling strategy. We checked, however, that experimental constraints on the Higgs sector appear to be (at most) weakly sensitive to  $m_{h_3}$ . We thus anticipate that there is in fact no upper bound on the mass of the heaviest Higgs, as we suspect that it can be arbitrarily heavy without impacting the phase structure or Higgs observables.

# 6 Conclusions

Motivated by EW baryogenesis and gravitational wave experiments, in this article we investigated the properties of PTs in the NMSSM. We employed an effective field theory approach to calculate the finite temperature effective potential by matching the NMSSM to the THDMS. By tracing the change in the minima of the effective potential with temperature, we mapped out the phase structure and computed the strengths of any EWPTs,  $\gamma_{\mathrm{EW}}$ . By scanning the parameter space of the NMSSM, we obtained millions of samples that featured an SFOPT with  $\gamma_{\mathrm{EW}} > 1$  and satisfied the constraints from LHC Higgs measurements and LEP bounds on charginos.

We classified them into three categories, Type-H-and-S, Type-Only-H and Type-Only-S, based on the nature of the first PT in their cosmological histories. The Type-

Only-S samples were further divided into Type-Only-S(maintain) and Type-Only-S (flip) according to whether the singlet VEV changed sign during the strongest EWPT. In the Type-H-and-S samples, the first PT in the cosmological history breaks EW symmetry and gives the singlet a VEV at the same time. This transition is usually the strongest one.

The Type-Only-H samples, on the other hand, go through a series of PTs that break, restore and break again EW symmetry. The first one is a crossover transition during which only the  $h_d$  field obtains a non-vanishing VEV, and the last one is the strongest EW FOPT. This scenario was by far the rarest in our scan. For the Type-Only-S(maintain) samples, during the first transition EW symmetry remains unbroken, but the singlet field obtains a non-vanishing VEV. Then EW symmetry breaks through a subsequent FOPT. Both of the transitions can be SFOPTs, which could give interesting gravitational wave signatures [124] as well as triggering an EW baryogenesis mechanism. The first PT of the Type-Only-S(flip) samples is usually a FOPT with very small  $\gamma$ , and the following strongest FOPT flips the sign of the singlet VEV. We found, however, that the tunneling rates in Type-Only-H and Type-Only-S(flip) scenarios could be problematic. For our benchmarks, the SFOPT in the Type-Only-H scenario did not complete, and in the Type-Only-S(flip) scenario, a preceding PT required to reach the SFOPT did not complete. Thus, unfortunately, these scenarios might not help EW baryogenesis.

The regions of NMSSM parameter space in which the four scenarios occur show different features. In the samples for which the strongest FOPT ends in the observed zero temperature phase:

- The observed 125 GeV Higgs is often the second lightest Higgs in the model, not the lightest one.  
- All of the input parameters are severely constrained, except the SUSY scale  $m_{\mathrm{SUSY}}$  and stop trilinear  $A_t$ .  
- Quartic couplings of around  $\lambda \simeq 0.6$  and  $\kappa \simeq 0.2$  could result in an SFOPT in all our scenarios, though a broad range of couplings result in SFOPTs in the Type-0n1y-S (flip) scenario, including couplings far away from limits on perturbativity.  
- The scenarios predict different trilinear couplings, i.e., they are distinguishable on the  $(A_{\lambda}, A_{\kappa})$  plane. The  $A_{\lambda}$  and  $A_{\kappa}$  of the Type-Only-S(flip) samples always have the same sign, while in the other scenarios the samples are concentrated in the quadrant of negative  $A_{\kappa}$  and positive  $A_{\lambda}$ . Compared to the Type-H-and-S scenario, the Type-Only-S(maintain) scenario favors smaller  $|A_{\kappa}|$  and  $A_{\lambda}$ .

In addition we found substantial samples for which the strongest FOPT does not end in the SM vacuum. The regions of parameter space are similar to the samples for which the strongest FOPT ends in the SM vacuum, except that Type-Only-S(maintain) and Type-Only-S(flip) exchange parameter spaces with each other. There are, furthermore, two additional regions that appear in the Type-Only-S(maintain) scenario, and one of them results in critical temperatures higher than 200 GeV.

In summary, we mapped out and classified intricate patterns of symmetry breaking that are possible in the NMSSM, and checked which scenarios could in principle help provide a viable theory of EW baryogenesis or potentially lead to a gravitational wave signal. We found viable scenarios in which the Higgs fields and singlet or only singlet first acquired VEVs. We checked that the sequences of required PTs actually nucleated, contained a SFOPT, and that the model satisfied constraints from LEP and the LHC. The combination of constraints lead to the predictions that  $\lambda \simeq 0.6$ ,  $\kappa \simeq 0.2$  and that the observed  $125\mathrm{GeV}$  Higgs tends to be the second lightest Higgs in the model.

# Acknowledgments

We thank Sujeet Akula for early collaboration on the paper. We are grateful for Margarete Mühleitner and Jonathan Kozaczuk for responding to queries regarding previous work and Junjie Cao for helpful remarks. TRIUMF receives federal funding via a contribution agreement with the National Research Council of Canada and the Natural Science and Engineering Research Council of Canada. The work of P.A. is supported by the Australian Research Council Future Fellowship grant FT160100274. The work of C.B. was supported by the Australian Research Council through the ARC Centre of Excellence for Particle Physics at the Terascale (grant CE110001104). The work of P.A. and C.B. are also supported with the Australian Research Council Discovery Project grant DP180102209.

# A Field dependent masses

When exploring the potential away from minima we need to account for the Higgs field dependence of the  $\overline{\mathrm{MS}}$  mass eigenstates in (3.1). Therefore here we present the so-called field dependent masses of the THDMS.

The field dependent masses of the gauge bosons and top, bottom and tau fermions are given by the simple tree-level expressions

$$
M _ {W} ^ {2} = \frac {1}{4} g ^ {2} \left(h _ {u} ^ {2} + h _ {d} ^ {2}\right), \quad M _ {Z} ^ {2} = \frac {1}{4} \left(g ^ {\prime 2} + g ^ {2}\right) \left(h _ {u} ^ {2} + h _ {d} ^ {2}\right), \tag {A.1}
$$

$$
m _ {t} = \frac {1}{\sqrt {2}} y _ {t} h _ {u}, \quad m _ {b} = \frac {1}{\sqrt {2}} y _ {b} h _ {d}, \quad m _ {\tau} = \frac {1}{\sqrt {2}} y _ {\tau} h _ {d},
$$

where the gauge couplings are without GUT normalization, and the  $y_{t}$ ,  $y_{b}$  and  $y_{\tau}$  are the (3,3) elements of the corresponding Yukawa matrices.

Since the Higgs states mix, the CP even, CP odd and charged  $\overline{\mathrm{MS}}$  Higgs masses are the eigenvalues of the corresponding CP even, CP odd and charged mass matrices. The mass matrix for the CP even neutral Higgs bosons, in the basis  $\{H_d,H_u,S\}$ , is

$$
\left(M _ {H ^ {0}} ^ {2}\right) _ {1 1} = \overline {{m}} _ {1} ^ {2} + \frac {3}{2} \lambda_ {1} h _ {d} ^ {2} + \frac {1}{2} \lambda_ {5} s ^ {2} + \frac {1}{2} (\lambda_ {3} + \lambda_ {4}) h _ {u} ^ {2},
$$

$$
\left(M _ {H ^ {0}} ^ {2}\right) _ {2 2} = \overline {{m}} _ {2} ^ {2} + \frac {3}{2} \lambda_ {2} h _ {u} ^ {2} + \frac {1}{2} \lambda_ {6} s ^ {2} + \frac {1}{2} (\lambda_ {3} + \lambda_ {4}) h _ {d} ^ {2},
$$

$$
\left(M _ {H ^ {0}} ^ {2}\right) _ {3 3} = \overline {{m}} _ {S} ^ {2} - \sqrt {2} \mathrm {R e} (m _ {5}) s + \frac {1}{2} \lambda_ {5} h _ {d} ^ {2} + \mathrm {R e} (\lambda_ {7}) h _ {u} h _ {d} + \frac {1}{2} \lambda_ {6} h _ {u} ^ {2} + 3 \lambda_ {8} s ^ {2},
$$

$$
\left(M _ {H ^ {0}} ^ {2}\right) _ {1 2} = \left(M _ {H ^ {0}} ^ {2}\right) _ {2 1} = - \frac {1}{\sqrt {2}} \mathrm {R e} (m _ {4}) s + \frac {1}{2} \mathrm {R e} (\lambda_ {7}) s ^ {2} + (\lambda_ {3} + \lambda_ {4}) h _ {u} h _ {d},
$$

$$
\left(M _ {H ^ {0}} ^ {2}\right) _ {1 3} = \left(M _ {H ^ {0}} ^ {2}\right) _ {3 1} = - \frac {1}{\sqrt {2}} \operatorname {R e} (m _ {4}) h _ {u} + \lambda_ {5} h _ {d} s + \operatorname {R e} (\lambda_ {7}) h _ {u} s,
$$

$$
\left(M _ {H ^ {0}} ^ {2}\right) _ {2 3} = \left(M _ {H ^ {0}} ^ {2}\right) _ {3 2} = - \frac {1}{\sqrt {2}} \operatorname {R e} \left(m _ {4}\right) h _ {d} + \operatorname {R e} \left(\lambda_ {7}\right) h _ {d} s + \lambda_ {6} h _ {u} s. \tag {A.2}
$$

where we have written  $\overline{m}_1^2$ ,  $\overline{m}_2^2$  and  $\overline{m}_S^2$  with a bar to denote the fact that in this context these are fixed to fulfill the following tree-level EW symmetry breaking (EWSB) conditions

$$
\overline {{m _ {1} ^ {2}}} = - \frac {1}{2} (\lambda_ {3} + \lambda_ {4}) v _ {u} ^ {2} - \frac {1}{2} \lambda_ {1} v _ {d} ^ {2} - \frac {1}{2} \lambda_ {5} v _ {S} ^ {2} - \frac {1}{2} \operatorname {R e} (\lambda_ {7}) \frac {v _ {u} v _ {S} ^ {2}}{v _ {d}} + \frac {1}{\sqrt {2}} \operatorname {R e} (m _ {4}) \frac {v _ {u} v _ {S}}{v _ {d}},
$$

$$
\overline {{m _ {2} ^ {2}}} = - \frac {1}{2} \lambda_ {2} v _ {u} ^ {2} - \frac {1}{2} (\lambda_ {3} + \lambda_ {4}) v _ {d} ^ {2} - \frac {1}{2} \lambda_ {6} v _ {S} ^ {2} - \frac {1}{2} \operatorname {R e} (\lambda_ {7}) \frac {v _ {d} v _ {S} ^ {2}}{v _ {u}} + \frac {1}{\sqrt {2}} \operatorname {R e} (m _ {4}) \frac {v _ {d} v _ {S}}{v _ {u}}, \tag {A.3}
$$

$$
\overline {{m}} _ {S} ^ {2} = - \frac {1}{2} \lambda_ {6} v _ {u} ^ {2} - \frac {1}{2} \lambda_ {5} v _ {d} ^ {2} - \lambda_ {8} v _ {S} ^ {2} - \mathrm {R e} (\lambda_ {7}) v _ {d} v _ {u} + \frac {1}{\sqrt {2}} \mathrm {R e} (m _ {4}) \frac {v _ {u} v _ {d}}{v _ {S}} + \frac {1}{\sqrt {2}} \mathrm {R e} (m _ {5}) v _ {S}.
$$

Note that the VEVs appearing on the right hand side are the zero temperature VEVs, so  $\overline{m}_1^2$ ,  $\overline{m}_2^2$  and  $\overline{m}_S^2$  do not vary with either temperature or with the fields. If we permit a complex phase in the THDMS parameters, there is in fact an additional tadpole equation relating it to complex phases in the VEVs. As we assume real, CP conserving VEVs, however, this extra tadpole simply forces the complex phase in the THDMS parameters to vanish. The three CP even mass eigenstates,  $h_1$ ,  $h_2$  and  $h_3$ , are then found by diagonalizing  $M_{H^0}^2$ .

Similarly, the CP odd mass matrix is

$$
\left(M _ {A} ^ {2}\right) _ {1 1} = \overline {{m}} _ {1} ^ {2} + \frac {1}{2} \lambda_ {1} h _ {d} ^ {2} + \frac {1}{2} \lambda_ {5} s ^ {2} + \frac {1}{2} (\lambda_ {3} + \lambda_ {4}) h _ {u} ^ {2},
$$

$$
\left(M _ {A} ^ {2}\right) _ {2 2} = \overline {{m}} _ {2} ^ {2} + \frac {1}{2} \lambda_ {2} h _ {u} ^ {2} + \frac {1}{2} \lambda_ {6} s ^ {2} + \frac {1}{2} (\lambda_ {3} + \lambda_ {4}) h _ {d} ^ {2},
$$

$$
\left(M _ {A} ^ {2}\right) _ {3 3} = \overline {{m}} _ {S} ^ {2} + \sqrt {2} \mathrm {R e} (m _ {5}) s + \frac {1}{2} \lambda_ {5} h _ {d} ^ {2} - \mathrm {R e} (\lambda_ {7}) h _ {u} h _ {d} + \frac {1}{2} \lambda_ {6} h _ {u} ^ {2} + \lambda_ {8} s ^ {2},
$$

$$
\left(M _ {A} ^ {2}\right) _ {1 2} = \left(M _ {A} ^ {2}\right) _ {2 1} = \frac {1}{\sqrt {2}} \operatorname {R e} (m _ {4}) s - \frac {1}{2} \operatorname {R e} (\lambda_ {7}) s ^ {2}, \tag {A.4}
$$

$$
\left(M _ {A} ^ {2}\right) _ {1 3} = \left(M _ {A} ^ {2}\right) _ {3 1} = \frac {1}{\sqrt {2}} \mathrm {R e} (m _ {4}) h _ {u} + \mathrm {R e} (\lambda_ {7}) h _ {u} s,
$$

$$
\left(M _ {A} ^ {2}\right) _ {2 3} = \left(M _ {A} ^ {2}\right) _ {3 2} = \frac {1}{\sqrt {2}} \operatorname {R e} (m _ {4}) h _ {d} + \operatorname {R e} (\lambda_ {7}) h _ {d} s.
$$

Diagonalizing it results in a neutral Goldstone boson  $G^0$  and the two physical CP odd Higgs bosons,  $A_1$  and  $A_2$ . The field dependent Goldstone masses are only zero at extrema of the tree-level potential. Thus, away from extrema, we cannot easily distinguish Goldstone bosons from physical Higgs bosons. In the  $\xi = 1$  gauge, however, they are treated on an equal footing and we do not need to identify Goldstones.

Finally, the charged Higgs mass matrix is

$$
\left(M _ {H ^ {\pm}} ^ {2}\right) _ {1 1} = \overline {{m}} _ {1} ^ {2} + \frac {1}{2} \lambda_ {5} s ^ {2} + \frac {1}{2} \lambda_ {1} h _ {d} ^ {2} + \frac {1}{2} \lambda_ {3} h _ {u} ^ {2},
$$

$$
\left(M _ {H ^ {\pm}} ^ {2}\right) _ {2 2} = \bar {m} _ {2} ^ {2} + \frac {1}{2} \lambda_ {6} s ^ {2} + \frac {1}{2} \lambda_ {3} h _ {d} ^ {2} + \frac {1}{2} \lambda_ {2} h _ {u} ^ {2}, \tag {A.5}
$$

$$
\left(M _ {H ^ {\pm}} ^ {2}\right) _ {2 1} = \left(M _ {H ^ {\pm}} ^ {2}\right) _ {1 2} ^ {*} = \frac {1}{\sqrt {2}} m _ {4} s - \frac {1}{2} \lambda_ {7} s ^ {2} - \frac {1}{2} \lambda_ {4} h _ {d} h _ {u}.
$$

Diagonalizing it results in the charged Higgs boson,  $H^{\pm}$  and the charged Goldstone boson  $G^{\pm}$ .

Gauge-fixing, however, alters the tree-level mass matrices, such that the field dependent scalar masses are gauge dependent. The CP even mass matrix receives no gauge-fixing contribution but the CP odd and charged mass matrices receive additional contributions in the  $R_{\xi}$  gauge,

$$
\left(M _ {A} ^ {2}\right) _ {1 1} \rightarrow \left(M _ {A} ^ {2}\right) _ {1 1} + \frac {1}{4} \xi (g ^ {2} + g ^ {\prime 2}) h _ {a} ^ {2},
$$

$$
\left(M _ {A} ^ {2}\right) _ {1 2} \rightarrow \left(M _ {A} ^ {2}\right) _ {1 2} - \frac {1}{4} \xi (g ^ {2} + g ^ {\prime 2}) h _ {d} h _ {u},
$$

$$
\left(M _ {A} ^ {2}\right) _ {2 2} \rightarrow \left(M _ {A} ^ {2}\right) _ {2 2} + \frac {1}{4} \xi \left(g ^ {2} + g ^ {\prime 2}\right) h _ {u} ^ {2}, \tag {A.6}
$$

$$
\left(M _ {H ^ {\pm}} ^ {2}\right) _ {1 1} \rightarrow \left(M _ {H ^ {\pm}} ^ {2}\right) _ {1 1} + \frac {1}{4} \xi g ^ {2} h _ {d} ^ {2},
$$

$$
\left(M _ {H ^ {\pm}} ^ {2}\right) _ {1 2} \rightarrow \left(M _ {H ^ {\pm}} ^ {2}\right) _ {1 2} - \frac {1}{4} \xi g ^ {2} h _ {d} h _ {u},
$$

$$
\left(M _ {H ^ {\pm}} ^ {2}\right) _ {2 2} \rightarrow \left(M _ {H ^ {\pm}} ^ {2}\right) _ {2 2} + \frac {1}{4} \xi g ^ {2} h _ {u} ^ {2}.
$$

The elements involving the singlet are unaffected. At the tree-level minimum, in which the Goldstone bosons are otherwise massless, the gauge-fixing contributions do not affect the masses of the physical Higgs bosons but result in Goldstone masses

$$
M _ {G ^ {0}} ^ {2} = \xi M _ {Z} ^ {2},
$$

$$
M _ {G ^ {\pm}} ^ {2} = \xi M _ {W} ^ {2}, \tag {A.7}
$$

where  $M_W$  and  $M_Z$  are the masses of the  $W$  and  $Z$  bosons.

# B Numerical methods for FOPTs

We first find all minima of the potential at  $T = 0$  and  $T = 1$  TeV to check that spontaneous symmetry breaking occurs, where in particular we reject points where the deepest  $T = 0$  minima is not the observed SM vacuum. If it occurs, we trace the trajectory with temperature of every  $T = 0$  and  $T = 1$  TeV minima. We call the trajectory of a particular minima a phase (note though this definition cannot distinguish phases linked by second-order or crossover transitions). A phase ends at the temperature at which the minima disappears. If two phases coexist at the same temperature, there may exist a critical temperature at which they are degenerate.

We apply an algorithm developed in CosmoTransitions [97] to trace phases in steps no greater than  $\Delta T$ :

0. We select a minima  $\mathfrak{m} \equiv (\mathfrak{h}_u, \mathfrak{h}_d, \mathfrak{s})$  at temperature  $T$  to trace.  
1. We use a local minimum finding algorithm, such as Nelder-Mead [125], to find the minimum  $\mathfrak{m}'$  at  $T' = T + \Delta T$ .  
2. We check that the new minimum  $\mathfrak{m}'$  lies close to that expected from a shift caused by thermal corrections.

We calculate the difference

$$
R = \max  \left( \right.\left\| \right. \mathfrak {m} + \frac {\partial \mathfrak {m}}{\partial T} \left. \right| _ {\mathfrak {m}} \Delta T - \mathfrak {m} ^ {\prime} \left. \right\|, \left\| \right. \mathfrak {m} ^ {\prime} - \frac {\partial \mathfrak {m}}{\partial T} \left. \right| _ {\mathfrak {m} ^ {\prime}} \Delta T - \mathfrak {m} \left\| \right.\left. \right)\left. \right). \tag {B.1}
$$

3. If  $R \leq \max R$ , where  $\max R$  governs the maximum acceptable changes in the field, we accept that the minima  $\mathfrak{m}'$  at temperature  $T'$  belongs to the same phase as the minima  $\mathfrak{m}$  at temperature  $T$ . We continue to trace the phase by returning to step 1 with  $\mathfrak{m} \to \mathfrak{m}'$  and  $T \to T'$ , and we reset any changes to  $\Delta T$ .

If  $R > \max R$ , we assume that the change in temperature dramatically changed the potential. We reduce the change in temperature by a factor of two,  $\Delta T \rightarrow \Delta T / 2$  and return to 1.

If, however,  $R > \max R$  and  $|\Delta T| < \min \Delta T$ , where  $\min \Delta T$  governs the smallest permissible step in temperature, we conclude that the phase must have ended, as the minima appears to change abruptly with a small change in temperature.

We save the sequence of minima and temperature found through this process — this is a phase. We find all the phases by tracing all  $T = 0$  minima up to at most  $1\mathrm{TeV}$  (the phase may end earlier) and all  $T = 1\mathrm{TeV}$  minima down to  $T = 0$  (in which case  $\Delta T < 0$ ). After removing degenerate phases, we denote the  $i$ -th phase by  $\mathfrak{m}_i(T)$ .

If any two of the phases, e.g., the  $i$ -th and  $j$ -th phase, coexist between temperatures  $T_{1}$  and  $T_{2}$ , and if

$$
V _ {\text {e f f}} \left(\mathfrak {m} _ {i} \left(T _ {1}\right), T _ {1}\right) > V _ {\text {e f f}} \left(\mathfrak {m} _ {j} \left(T _ {1}\right), T _ {1}\right) \tag {B.2}
$$

$$
V _ {\text {e f f}} \left(\mathfrak {m} _ {i} \left(T _ {2}\right), T _ {2}\right) <   V _ {\text {e f f}} \left(\mathfrak {m} _ {j} \left(T _ {2}\right), T _ {2}\right) \tag {B.3}
$$

there must exit a critical temperature,  $T_{C}$ , between temperatures  $T_{1}$  and  $T_{2}$  at which they are degenerate,

$$
V _ {\text {e f f}} \left(\mathfrak {m} _ {i} \left(T _ {C}\right), T _ {C}\right) = V _ {\text {e f f}} \left(\mathfrak {m} _ {j} \left(T _ {C}\right), T _ {C}\right). \tag {B.4}
$$

We calculate the critical temperature using bisection, and find properties of the transition, e.g., the strength of transition from (4.3).

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] D.E. Morrissey and M.J. Ramsey-Musolf, Electroweak baryogenesis, New J. Phys. 14 (2012) 125003 [arXiv:1206.2942] [INSPIRE].  
[2] J.M. Cline, Baryogenesis, in Les Houches Summer School — Session 86: Particle Physics and Cosmology: The Fabric of Spacetime Les Houches, France, July 31 – August 25, 2006, 2006, hep-ph/0609145 [INSPIRE].  
[3] G.A. White, A Pedagogical Introduction to Electroweak Baryogenesis, Morgan & Claypool Publishers, (2016), pp. 2053-2571, [https://doi.org/10.1088/978-1-6817-4457-5].

[4] G. Krnjaic, Can the Baryon Asymmetry Arise From Initial Conditions?, Phys. Rev. D 96 (2017) 035041 [arXiv:1606.05344] [INSPIRE].  
[5] A.D. Sakharov, Violation of  $CP$  invariance,  $C$  asymmetry, and baryon asymmetry of the universe, *Pis'ma Zh. Eksp. Teor. Fiz.* 5 (1967) 32.  
[6] M. D'Onofrio and K. Rummukainen, Standard model cross-over on the lattice, Phys. Rev. D 93 (2016) 025003 [arXiv:1508.07161] [INSPIRE].  
[7] PARTICLE DATA GROUP collaboration, Review of Particle Physics, Chin. Phys. C 40 (2016) 100001 [INSPIRE].  
[8] PLANCK collaboration, Planck 2015 results. XIII. Cosmological parameters, Astron. Astrophys. 594 (2016) A13 [arXiv:1502.01589] [INSPIRE].  
[9] M. Trodden, Electroweak baryogenesis, Rev. Mod. Phys. 71 (1999) 1463 [hep-ph/9803479] [INSPIRE].  
[10] J.M. Cline, M. Jarvinen and F. Sannino, The Electroweak Phase Transition in Nearly Conformal Technicolor, Phys. Rev. D 78 (2008) 075027 [arXiv:0808.1512] [INSPIRE].  
[11] J.M. Cline, G. Laporte, H. Yamashita and S. Kraml, Electroweak Phase Transition and LHC Signatures in the Singlet Majoron Model, JHEP 07 (2009) 040 [arXiv:0905.2559] [INSPIRE].  
[12] D. Borah and J.M. Cline, Inert Doublet Dark Matter with Strong Electroweak Phase Transition, Phys. Rev. D 86 (2012) 055001 [arXiv:1204.4722] [INSPIRE].  
[13] J.M. Cline and K. Kainulainen, Improved Electroweak Phase Transition with Subdominant Inert Doublet Dark Matter, Phys. Rev. D 87 (2013) 071701 [arXiv:1302.2614] [INSPIRE].  
[14] T. Konstandin, Quantum Transport and Electroweak Baryogenesis, Phys. Usp. 56 (2013) 747 [arXiv:1302.6713] [INSPIRE].  
[15] J. Kozaczuk, S. Profumo, L.S. Haskins and C.L. Wainwright, Cosmological Phase Transitions and their Properties in the NMSSM, JHEP 01 (2015) 144 [arXiv:1407.4134] [INSPIRE].  
[16] S. Profumo, M.J. Ramsey-Musolf, C.L. Wainwright and P. Winslow, Singlet-catalyzed electroweak phase transitions and precision Higgs boson studies, Phys. Rev. D 91 (2015) 035018 [arXiv:1407.5342] [INSPIRE].  
[17] D. Curtin, P. Meade and C.-T. Yu, Testing Electroweak Baryogenesis with Future Colliders, JHEP 11 (2014) 127 [arXiv:1409.0005] [INSPIRE].  
[18] F.P. Huang and C.S. Li, Electroweak baryogenesis in the framework of the effective field theory, Phys. Rev. D 92 (2015) 075014 [arXiv:1507.08168] [INSPIRE].  
[19] S. Inoue, G. Ovanesyan and M.J. Ramsey-Musolf, Two-Step Electroweak Baryogenesis, Phys. Rev. D 93 (2016) 015013 [arXiv:1508.05404] [INSPIRE].  
[20] A. Katz, M. Perelstein, M.J. Ramsey-Musolf and P. Winslow, Stop-Catalyzed Baryogenesis Beyond the MSSM, Phys. Rev. D 92 (2015) 095019 [arXiv:1509.02934] [INSPIRE].  
[21] K. Fuyuto, J. Hisano and E. Senaha, Toward verification of electroweak baryogenesis by electric dipole moments, Phys. Lett. B 755 (2016) 491 [arXiv:1510.04485] [INSPIRE].  
[22] F.P. Huang, P.-H. Gu, P.-F. Yin, Z.-H. Yu and X. Zhang, Testing the electroweak phase transition and electroweak baryogenesis at the LHC and a circular electron-positron collider, Phys. Rev. D 93 (2016) 103515 [arXiv:1511.03969] [INSPIRE].

[23] A. Kobakhidze, L. Wu and J. Yue, Electroweak Baryogenesis with Anomalous Higgs Couplings, JHEP 04 (2016) 011 [arXiv:1512.08922] [INSPIRE].  
[24] F.P. Huang, Y. Wan, D.-G. Wang, Y.-F. Cai and X. Zhang, Hearing the echoes of electroweak baryogenesis with gravitational wave detectors, Phys. Rev. D 94 (2016) 041702 [arXiv:1601.01640] [INSPIRE].  
[25] A.V. Kotwal, M.J. Ramsey-Musolf, J.M. No and P. Winslow, Singlet-catalyzed electroweak phase transitions in the 100 TeV frontier, Phys. Rev. D 94 (2016) 035022 [arXiv:1605.06123] [INSPIRE].  
[26] V. Vaskonen, Electroweak baryogenesis and gravitational waves from a real scalar singlet, Phys. Rev. D 95 (2017) 123515 [arXiv:1611.02073] [INSPIRE].  
[27] C. Balázs, G. White and J. Yue, *Effective field theory, electric dipole moments and electroweak baryogenesis*, JHEP 03 (2017) 030 [arXiv:1612.01270] [INSPIRE].  
[28] A. Beniwal, M. Lewicki, J.D. Wells, M. White and A.G. Williams, Gravitational wave, collider and dark matter signals from a scalar singlet electroweak baryogenesis, JHEP 08 (2017) 108 [arXiv:1702.06124] [INSPIRE].  
[29] G. Kurup and M. Perelstein, Dynamics of Electroweak Phase Transition In Singlet-Scalar Extension of the Standard Model, Phys. Rev. D 96 (2017) 015036 [arXiv:1704.03381] [INSPIRE].  
[30] S. Akula, C. Balázs, L. Dunn and G. White, Electroweak baryogenesis in the  $\mathbb{Z}_3$ -invariant NMSSM, JHEP 11 (2017) 051 [arXiv:1706.09898] [INSPIRE].  
[31] C.-W. Chiang, M.J. Ramsey-Musolf and E. Senaha, Standard Model with a Complex Scalar Singlet: Cosmological Implications and Theoretical Considerations, Phys. Rev. D 97 (2018) 015005 [arXiv:1707.09960] [INSPIRE].  
[32] Q.-H. Cao, F.P. Huang, K.-P. Xie and X. Zhang, Testing the electroweak phase transition in scalar extension models at lepton colliders, Chin. Phys. C 42 (2018) 023103 [arXiv:1708.04737] [INSPIRE].  
[33] M.J. Ramsey-Musolf, P. Winslow and G. White, Color Breaking Baryogenesis, Phys. Rev. D 97 (2018) 123509 [arXiv:1708.07511] [INSPIRE].  
[34] F.P. Huang and C.S. Li, Probing the baryogenesis and dark matter relaxed in phase transition by gravitational waves and colliders, Phys. Rev. D 96 (2017) 095028 [arXiv:1709.09691] [INSPIRE].  
[35] J. de Vries, M. Postma, J. van de Vis and G. White, Electroweak Baryogenesis and the Standard Model Effective Field Theory, JHEP 01 (2018) 089 [arXiv:1710.04061] [INSPIRE].  
[36] L. Niemi, H.H. Patel, M.J. Ramsey-Musolf, T.V.I. Tenkanen and D.J. Weir, Electroweak phase transition in the real triplet extension of the SM: Dimensional reduction, Phys. Rev. D 100 (2019) 035002 [arXiv:1802.10500] [INSPIRE].  
[37] T. Modak and E. Senaha, Electroweak baryogenesis via bottom transport, Phys. Rev. D 99 (2019) 115022 [arXiv:1811.08088] [INSPIRE].  
[38] M. Carena, M. Quiros and Y. Zhang, Electroweak Baryogenesis from Dark-Sector CP-violation, Phys. Rev. Lett. 122 (2019) 201802 [arXiv:1811.09719] [INSPIRE].  
[39] M. Chala, M. Ramos and M. Spannowsky, Gravitational wave and collider probes of a triplet Higgs sector with a low cutoff, Eur. Phys. J. C 79 (2019) 156 [arXiv:1812.01901] [INSPIRE].

[40] R. Zhou, W. Cheng, X. Deng, L. Bian and Y. Wu, Electroweak phase transition and Higgs phenomenology in the Georgi-Machacek model, JHEP 01 (2019) 216 [arXiv:1812.06217] [INSPIRE].  
[41] A. Alves, T. Ghosh, H.-K. Guo, K. Sinha and D. Vagie, *Collision and Gravitational Wave Complementarity in Exploring the Singlet Extension of the Standard Model*, JHEP 04 (2019) 052 [arXiv:1812.09333] [INSPIRE].  
[42] S. Yaser Ayazi and A. Mohamadnejad, Conformal vector dark matter and strongly first-order electroweak phase transition, JHEP 03 (2019) 181 [arXiv:1901.04168] [INSPIRE].  
[43] A. Mohamadnejad, Gravitational waves from scale-invariant vector dark matter model: Probing below the neutrino-floor, arXiv:1907.08899 [INSPIRE].  
[44] A. Mazumdar and G. White, Review of cosmic phase transitions: their significance and experimental signatures, Rept. Prog. Phys. 82 (2019) 076901 [arXiv:1811.01948] [INSPIRE].  
[45] E. Witten, *Cosmic Separation of Phases*, Phys. Rev. D 30 (1984) 272 [INSPIRE].  
[46] C.J. Hogan, Gravitational radiation from cosmological phase transitions, Mon. Not. Roy. Astron. Soc. 218 (1986) 629 [INSPIRE].  
[47] L.M. Krauss, Gravitational waves from global phase transitions, Phys. Lett. B 284 (1992) 229 [INSPIRE].  
[48] A. Kosowsky, M.S. Turner and R. Watkins, Gravitational radiation from colliding vacuum bubbles, Phys. Rev. D 45 (1992) 4514 [INSPIRE].  
[49] A. Kosowsky, M.S. Turner and R. Watkins, Gravitational waves from first order cosmological phase transitions, Phys. Rev. Lett. 69 (1992) 2026 [INSPIRE].  
[50] M. Kamionkowski, A. Kosowsky and M.S. Turner, Gravitational radiation from first order phase transitions, Phys. Rev. D 49 (1994) 2837 [astro-ph/9310044] [INSPIRE].  
[51] C. Lee, V. Cirigliano and M.J. Ramsey-Musolf, Resonant relaxation in electroweak baryogenesis, Phys. Rev. D 71 (2005) 075010 [hep-ph/0412354] [INSPIRE].  
[52] C. Balázs, M. Carena, A. Menon, D.E. Morrissey and C.E.M. Wagner, The supersymmetric origin of matter, Phys. Rev. D 71 (2005) 075002 [hep-ph/0412264] [INSPIRE].  
[53] S. Liebler, S. Profumo and T. Stefaniak, Light Stop Mass Limits from Higgs Rate Measurements in the MSSM: Is MSSM Electroweak Baryogenesis Still Alive After All?, JHEP 04 (2016) 143 [arXiv:1512.09172] [INSPIRE].  
[54] M. Maniatis, The Next-to-Minimal Supersymmetric extension of the Standard Model reviewed, Int. J. Mod. Phys. A 25 (2010) 3505 [arXiv:0906.0777] [INSPIRE].  
[55] U. Ellwanger, C. Hugonie and A.M. Teixeira, The Next-to-Minimal Supersymmetric Standard Model, Phys. Rept. 496 (2010) 1 [arXiv:0910.1785] [INSPIRE].  
[56] H.-L. Li, M. Ramsey-Musolf and S. Willocq, Probing a scalar singlet-catalyzed electroweak phase transition with resonant di-Higgs boson production in the 4b channel, Phys. Rev. D 100 (2019) 075035 [arXiv:1906.05289] [INSPIRE].  
[57] L. Bian, H.-K. Guo and J. Shu, Gravitational Waves, baryon asymmetry of the universe and electric dipole moment in the CP-violating NMSSM, Chin. Phys. C 42 (2018) 093106 [arXiv:1704.02488] [INSPIRE].

[58] S.J. Huber, T. Konstandin, T. Prokopec and M.G. Schmidt, Electroweak Phase Transition and Baryogenesis in the NMSSM, Nucl. Phys. B 757 (2006) 172 [hep-ph/0606298] [INSPIRE].  
[59] C. Balázs, A. Mazumdar, E. Pukartas and G. White, Baryogenesis, dark matter and inflation in the Next-to-Minimal Supersymmetric Standard Model, JHEP 01 (2014) 073 [arXiv:1309.5091] [INSPIRE].  
[60] K. Cheung, T.-J. Hou, J.S. Lee and E. Senaha, Singlino-driven Electroweak Baryogenesis in the Next-to-MSSM, Phys. Lett. B 710 (2012) 188 [arXiv:1201.3781] [INSPIRE].  
[61] W. Huang, Z. Kang, J. Shu, P. Wu and J.M. Yang, New insights in the electroweak phase transition in the NMSSM, Phys. Rev. D 91 (2015) 025006 [arXiv:1405.1152] [INSPIRE].  
[62] S.V. Demidov, D.S. Gorbunov and D.V. Kirpichnikov, *Split NMSSM with electroweak baryogenesis*, JHEP **11** (2016) 148 [Erratum ibid. **08** (2017) 080] [arXiv:1608.01985] [INSPIRE].  
[63] X.-J. Bi, L. Bian, W. Huang, J. Shu and P.-F. Yin, Interpretation of the Galactic Center excess and electroweak phase transition in the NMSSM, Phys. Rev. D 92 (2015) 023507 [arXiv:1503.03749] [INSPIRE].  
[64] M. Carena, N.R. Shah and C.E.M. Wagner, Light Dark Matter and the Electroweak Phase Transition in the NMSSM, Phys. Rev. D 85 (2012) 036003 [arXiv:1110.4378] [INSPIRE].  
[65] A. Menon, D.E. Morrissey and C.E.M. Wagner, Electroweak baryogenesis and dark matter in the NMSSM, Phys. Rev. D 70 (2004) 035005 [hep-ph/0404184] [INSPIRE].  
[66] N.F. Bell, M.J. Dolan, L.S. Friedrich, M.J. Ramsey-Musolf and R.R. Volkas, Electroweak Baryogenesis with Vector-like Leptons and Scalar Singlets, JHEP 09 (2019) 012 [arXiv:1903.11255] [INSPIRE].  
[67] J. De Vries, M. Postma and J. van de Vis, The role of leptons in electroweak baryogenesis, JHEP 04 (2019) 024 [arXiv:1811.11104] [INSPIRE].  
[68] C.-Y. Chen, H.-L. Li and M. Ramsey-Musolf, CP-Violation in the Two Higgs Doublet Model: from the LHC to EDMs, Phys. Rev. D 97 (2018) 015020 [arXiv:1708.00435] [INSPIRE].  
[69] H.-K. Guo, Y.-Y. Li, T. Liu, M. Ramsey-Musolf and J. Shu, Lepton-Flavored Electroweak Baryogenesis, Phys. Rev. D 96 (2017) 115034 [arXiv:1609.09849] [INSPIRE].  
[70] W. Chao and M.J. Ramsey-Musolf, Catalysis of Electroweak Baryogenesis via Fermionic Higgs Portal Dark Matter, arXiv:1503.00028 [INSPIRE].  
[71] J.M. Cline, K. Kainulainen and D. Tucker-Smith, Electroweak baryogenesis from a dark sector, Phys. Rev. D 95 (2017) 115006 [arXiv:1702.08909] [INSPIRE].  
[72] J.M. Cline and K. Kainulainen, Electroweak baryogenesis and dark matter from a singlet Higgs, JCAP 01 (2013) 012 [arXiv:1210.4196] [INSPIRE].  
[73] J.M. Cline, K. Kainulainen and M. Trot, Electroweak Baryogenesis in Two Higgs Doublet Models and B meson anomalies, JHEP 11 (2011) 089 [arXiv:1107.3559] [INSPIRE].  
[74] M. Carena, Z. Liu and M. Riembau, Probing the electroweak phase transition via enhanced di-Higgs boson production, Phys. Rev. D 97 (2018) 095032 [arXiv:1801.00794] [INSPIRE].  
[75] J.M. Cline, M. Joyce and K. Kainulainen, Supersymmetric electroweak baryogenesis in the WKB approximation, Phys. Lett. B 417 (1998) 79 [Erratum ibid. B 448 (1999) 321] [hep-ph/9708393] [INSPIRE].

[76] B. Grzadkowski and D. Huang, Spontaneous CP-Violating Electroweak Baryogenesis and Dark Matter from a Complex Singlet Scalar, JHEP 08 (2018) 135 [arXiv:1807.06987] [INSPIRE].  
[77] S.A.R. Ellis, S. Ipek and G. White, Electroweak Baryogenesis from Temperature-Varying Couplings, JHEP 08 (2019) 002 [arXiv:1905.11994] [INSPIRE].  
[78] F.P. Huang, Z. Qian and M. Zhang, Exploring dynamical CP-violation induced baryogenesis by gravitational waves and colliders, Phys. Rev. D 98 (2018) 015014 [arXiv:1804.06813] [INSPIRE].  
[79] S.A. Abel, Destabilizing divergences in the NMSSM, Nucl. Phys. B 480 (1996) 55 [hep-ph/9609323] [INSPIRE].  
[80] C. Panagiotakopoulos and K. Tamvakis, Stabilized NMSSM without domain walls, Phys. Lett. B 446 (1999) 224 [hep-ph/9809475] [INSPIRE].  
[81] C. Panagiotakopoulos and K. Tamvakis, New minimal extension of MSSM, Phys. Lett. B 469 (1999) 145 [hep-ph/9908351] [INSPIRE].  
[82] T. Elliott, S.F. King and P.L. White, Supersymmetric Higgs bosons at the limit, Phys. Lett. B 305 (1993) 71 [hep-ph/9302202] [INSPIRE].  
[83] T. Elliott, S.F. King and P.L. White, Squark contributions to Higgs boson masses in the next-to-minimal supersymmetric standard model, Phys. Lett. B 314 (1993) 56 [hep-ph/9305282] [INSPIRE].  
[84] T. Elliott, S.F. King and P.L. White, Radiative corrections to Higgs boson masses in the next-to-minimal supersymmetric Standard Model, Phys. Rev. D 49 (1994) 2435 [hep-ph/9308309] [INSPIRE].  
[85] H.H. Patel and M.J. Ramsey-Musolf, Baryon Washout, Electroweak Phase Transition and Perturbation Theory, JHEP 07 (2011) 029 [arXiv:1101.4665] [INSPIRE].  
[86] J.C. Romao, Spontaneous CP Violation in SUSY Models: A No Go Theorem, Phys. Lett. B 173 (1986) 309 [INSPIRE].  
[87] P.M. Ferreira, M. Mühlleitner, R. Santos, G. Weiglein and J. Wittbrodt, Vacuum Instabilities in the N2HDM, JHEP 09 (2019) 006 [arXiv:1905.10234] [INSPIRE].  
[88] N.K. Nielsen, On the Gauge Dependence of Spontaneous Symmetry Breaking in Gauge Theories, Nucl. Phys. B 101 (1975) 173 [INSPIRE].  
[89] L. Di Luzio and L. Mihaila, On the gauge dependence of the Standard Model vacuum instability scale, JHEP 06 (2014) 079 [arXiv:1404.7450] [INSPIRE].  
[90] M. Laine, M. Meyer and G. Nardini, Thermal phase transition with full 2-loop effective potential, Nucl. Phys. B 920 (2017) 565 [arXiv:1702.07479] [INSPIRE].  
[91] P.B. Arnold and O. Espinosa, The effective potential and first order phase transitions: Beyond leading-order, Phys. Rev. D 47 (1993) 3546 [Erratum ibid. D 50 (1994) 6662] [hep-ph/9212235] [INSPIRE].  
[92] P. Basler, M. Krause, M. Muhlleitner, J. Wittbrodt and A. Wlotzka, *Strong First Order Electroweak Phase Transition in the CP-Conserving 2HDM Revisited*, JHEP **02** (2017) 121 [arXiv:1612.04086] [INSPIRE].  
[93] P. Basler and M. Mühlleitner, BSMPT (Beyond the Standard Model Phase Transitions): A tool for the electroweak phase transition in extended Higgs sectors, Comput. Phys. Commun. 237 (2019) 62 [arXiv:1803.02846] [INSPIRE].

[94] S.R. Coleman, The Fate of the False Vacuum. 1. Semiclassical Theory, Phys. Rev. D 15 (1977) 2929 [Erratum ibid. D 16 (1977) 1248] [INSPIRE].  
[95] C.G. Callan Jr. and S.R. Coleman, The Fate of the False Vacuum. 2. First Quantum Corrections, Phys. Rev. D 16 (1977) 1762 [INSPIRE].  
[96] A.D. Linde, Fate of the False Vacuum at Finite Temperature: Theory and Applications, Phys. Lett. 100B (1981) 37 [INSPIRE].  
[97] C.L. Wainwright, Cosmo Transitions: Computing Cosmological Phase Transition Temperatures and Bubble Profiles with Multiple Fields, Comput. Phys. Commun. 183 (2012) 2006 [arXiv:1109.4189] [INSPIRE].  
[98] L.D. McLerran, M.E. Shaposhnikov, N. Turok and M.B. Voloshin, Why the baryon asymmetry of the universe is approximately  $10^{**}-10$ , Phys. Lett. B 256 (1991) 451 [INSPIRE].  
[99] M. Dine, P. Huet and R.L. Singleton Jr., Baryogenesis at the electroweak scale, Nucl. Phys. B 375 (1992) 625 [INSPIRE].  
[100] P. Athron, J.-h. Park, D. Stöckinger and A. Voigt, Flexible SUSY—A spectrum generator generator for supersymmetric models, Comput. Phys. Commun. 190 (2015) 139 [arXiv:1406.2319] [INSPIRE].  
[101] P. Athron et al., FlexibleSUSY 2.0: Extensions to investigate the phenomenology of SUSY and non-SUSY models, Comput. Phys. Commun. 230 (2018) 145 [arXiv:1710.03760] [INSPIRE].  
[102] B.C. Allanach, SOFTSUSY: a program for calculating supersymmetric spectra, Comput. Phys. Commun. 143 (2002) 305 [hep-ph/0104145] [INSPIRE].  
[103] B.C. Allanach, P. Athron, L.C. Tunstall, A. Voigt and A.G. Williams, Next-to-Minimal SOFTSUSY, Comput. Phys. Commun. 185 (2014) 2322 [arXiv:1311.7659] [INSPIRE].  
[104] F. Staub, From Superpotential to Model Files for FeynArts and CalcHep/CompHEP, Comput. Phys. Commun. 181 (2010) 1077 [arXiv:0909.2863] [INSPIRE].  
[105] F. Staub, Automatic Calculation of supersymmetric Renormalization Group Equations and Self Energies, Comput. Phys. Commun. 182 (2011) 808 [arXiv:1002.0840] [INSPIRE].  
[106] F. Staub, SARAH 3.2: Dirac Gauginos, UFO output and more, Comput. Phys. Commun. 184 (2013) 1792 [arXiv:1207.0906] [INSPIRE].  
[107] F. Staub, SARAH 4: A tool for (not only SUSY) model builders, Comput. Phys. Commun. 185 (2014) 1773 [arXiv:1309.7223] [INSPIRE].  
[108] A. Fowlie, A fast  $C++$  implementation of thermal functions, Comput. Phys. Commun. 228 (2018) 264 [arXiv:1802.02720] [INSPIRE].  
[109] F. Staub et al., Precision tools and models to narrow in on the 750 GeV diphoton resonance, Eur. Phys. J. C **76** (2016) 516 [arXiv:1602.05581] [INSPIRE].  
[110] J. Bernon and B. Dumont, *Lilith: a tool for constraining new physics from Higgs measurements*, Eur. Phys. J. C **75** (2015) 440 [arXiv:1502.04138] [INSPIRE].  
[111] F. Feroz and M.P. Hobson, Multimodal nested sampling: an efficient and robust alternative to MCMC methods for astronomical data analysis, Mon. Not. Roy. Astron. Soc. 384 (2008) 449 [arXiv:0704.3704] [INSPIRE].

[112] F. Feroz, M.P. Hobson and M. Bridges, MultiNest: an efficient and robust Bayesian inference tool for cosmology and particle physics, Mon. Not. Roy. Astron. Soc. 398 (2009) 1601 [arXiv:0809.3437] [INSPIRE].  
[113] F. Feroz, M.P. Hobson, E. Cameron and A.N. Pettitt, Importance Nested Sampling and the MultiNest Algorithm, arXiv:1306.2144 [INSPIRE].  
[114] P. Bechtle, O. Brein, S. Heinemeyer, G. Weiglein and K.E. Williams, Higgs Bounds: Confronting Arbitrary Higgs Sectors with Exclusion Bounds from LEP and the Tevatron, Comput. Phys. Commun. 181 (2010) 138 [arXiv:0811.4169] [INSPIRE].  
[115] P. Bechtle, O. Brein, S. Heinemeyer, G. Weiglein and K.E. Williams, HiggsBounds 2.0.0: Confronting Neutral and Charged Higgs Sector Predictions with Exclusion Bounds from LEP and the Tevatron, Comput. Phys. Commun. 182 (2011) 2605 [arXiv:1102.1898] [INSPIRE].  
[116] P. Bechtle et al., *Recent Developments in HiggsBounds and a Preview of HiggsSignals*, PoS(CHARGED 2012)024 [arXiv:1301.2345] [INSPIRE].  
[117] P. Bechtle et al., HiggsBounds - 4: Improved Tests of Extended Higgs Sectors against Exclusion Bounds from LEP, the Tevatron and the LHC, Eur. Phys. J. C 74 (2014) 2693 [arXiv:1311.0055] [INSPIRE].  
[118] P. Bechtle, S. Heinemeyer, O. Stal, T. Stefaniak and G. Weiglein, Applying Exclusion Likelihoods from LHC Searches to Extended Higgs Sectors, Eur. Phys. J. C 75 (2015) 421 [arXiv:1507.06706] [INSPIRE].  
[119] J. Baglio et al., NMSSMCALC: A Program Package for the Calculation of Loop-Corrected Higgs Boson Masses and Decay Widths in the (Complex) NMSSM, Comput. Phys. Commun. 185 (2014) 3372 [arXiv:1312.4788] [INSPIRE].  
[120] ATLAS collaboration, Search for a scalar partner of the top quark in the jets plus missing transverse momentum final state at  $\sqrt{s} = 13$  TeV with the ATLAS detector, JHEP 12 (2017) 085 [arXiv:1709.04183] [INSPIRE].  
[121] CMS collaboration, Search for direct top squark pair production in events with one lepton, jets and missing transverse energy at 13 TeV, CMS-PAS-SUS-19-009 (2019).  
[122] CMS collaboration, Search for a new scalar resonance decaying to a pair of  $Z$  bosons in proton-proton collisions at  $\sqrt{s} = 13$  TeV, JHEP 06 (2018) 127 [Erratum ibid. 03 (2019) 128] [arXiv:1804.01939] [INSPIRE].  
[123] S. AbdusSalam, Testing Higgs boson scenarios in the phenomenological NMSSM, Eur. Phys. J. C 79 (2019) 442 [arXiv:1710.10785] [INSPIRE].  
[124] A.P. Morais, R. Pasechnik and T. Vieu, Multi-peaked signatures of primordial gravitational waves from multi-step electroweak phase transition, arXiv:1802.10109 [INSPIRE].  
[125] J. Nelder and R. Mead, A Simplex Method for Function Minimization, Comput. J. 7 (1965) 308.