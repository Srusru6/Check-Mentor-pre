# Cosmological phase transitions: is effective field theory just a toy?

Marieke Postma<sup>a</sup> and Graham White<sup>b</sup>

a Nikhef,

Science Park 105,1098 XG Amsterdam, The Netherlands

b Kavli IPMU (WPI), UTIAS, The University of Tokyo,

Kashiwa, Chiba 277-8583, Japan

E-mail: mpostma@nikhef.nl, graham.white@ipmu.jp

ABSTRACT: To obtain a first order phase transition requires large new physics corrections to the Standard Model (SM) Higgs potential. This implies that the scale of new physics is relatively low, raising the question whether an effective field theory (EFT) description can be used to analyse the phase transition in a (nearly) model-independent way. We show analytically and numerically that first order phase transitions in perturbative extensions of the SM cannot be described by the SM-EFT. The exception are Higgs-singlet extension with tree-level matching; but even in this case the SM-EFT can only capture part of the full parameter space, and if truncated at dim-6 operators, the description is at most qualitative. We also comment on the applicability of EFT techniques to dark sector phase transitions.

KEYWORDS: Beyond Standard Model, Effective Field Theories, Higgs Physics

ARXIV EPRINT: 2012.03953

# Contents

# 1 Introduction 1

# 2 SMEFT and first order phase transitions 3

2.1 The Higgs potential in SMEFT 4  
2.2 First order phase transition 5  
2.3 Temperature corrections 5  
2.4 Validity of the SMEFT 7  
2.5 Dark phase transition 8

# 3 Matching the SMEFT to UV theories 9

3.1 Tree-level matching 9  
3.2 Loop-level matching 10

# 4 Phase transitions in UV theories and in SMEFT 11

4.1 Loop level matching: scalar extensions 11  
4.1.1 Dark sector 12  
4.2 Tree level matching: two Higgs doublet models 12  
4.3 Tree level matching: Higgs-singlet models 13

4.3.1 Numerical results 14  
4.3.2 Dark sector 17

4.4 Multifield UV theories 18

# 5 Conclusion 18

# A Numerical scan 19

A.1 Higgs-singlet model 19  
A.2 EFT 21  
A.3 Parameter values 21

# 1 Introduction

Determining the nature of the electroweak phase transition would be a major scientific achievement. The Standard Model (SM) predicts a crossover, but the transition may be different in extensions of the SM provided the new physics is important at the electroweak scale. Such new physics can be searched for at the LHC and, with more precision, in next generation colliders [1-5]. Especially interesting is the possibility of a strongly first-order electroweak phase transition (SFO-EWPT). The ensuing bubble dynamics could provide suitable conditions for producing the observed asymmetry between baryons and anti-baryons [6-9] (see [10, 11] for a review), and moreover can produce a potentially

observable stochastic background of gravitational waves in the frequency range that LISA will be sensitive to [12].

The above considerations have motivated the construction of many SM extensions with a SFO-EWPT. It would be advantageous if these could be studied in a single framework, allowing for a (nearly) model-independent assessment of key aspects, such as the strength of the phase transition and the phenomenological implications. The Standard Model effective field theory (SMEFT) [13, 14] may provide such an approach. The idea is that the new physics degrees of freedom are heavy and can be integrated out; their effects on the low-energy SM degrees of freedom are then parameterized by a tower of higher dimensional operators. If there is a sufficient separation of scales between the light and heavy fields, then the higher the mass dimension of the operator the more suppressed the impact on low energy observables, and consequently the EFT can be truncated at a given dimension depending on the desired precision. The EFT approach to the electroweak phase transition has been explored in multiple studies [15-23].

Lattice calculations show that in the standard model, a SFO-EWPT is only achieved for a Higgs mass  $m_{h0} \lesssim 65$  GeV [24-28] well below the measured value  $m_{h0} \cong 125.1$  GeV [29]. To obtain a strong phase transition therefore requires a large modification of the SM Higgs potential, by order one effects, which can only be achieved with new degrees of freedom that are sufficiently light. A first order phase transition requires a barrier (at finite temperature) between the false vacuum at the origin and the electroweak vacuum at non-zero Higgs field values. As was noted in [19], in the SMEFT, the local maximum follows from balancing the quadratic and (negative) quartic terms in the potential, whereas the minimum at finite vacuum expectation value (vev) is obtained balancing the quartic term with the higher dimensional operators. This implies that there is no separation of scales, and one generically expects the EFT approach to break down — this was indeed observed in the specific set-up of [19], where it was found that the effect of dimension 8 operators could be as large as the dimension 6 operators. ref. [30] did a numerical analysis comparing the Higgs-singlet model with the SMEFT approximation, and also found the EFT does not provide a good description.

In this work we perform a systematic study of the validity of the SMEFT description to capture perturbative UV models with a strongly first-order electroweak phase transition. In matching the UV theory to SMEFT, the Wilson coefficients of the non-renormalizable operators can be generated at tree and/or loop level. We find:

- In set-ups with only loop level matching, the SMEFT expansion breaks down, and the EFT cannot be truncated at operators of a given mass dimension.  
- In set-ups with tree level matching, the SMEFT expansion also breaks down, with the possible exception of Higgs-singlet extensions.  
- In Higgs-singlet extension with tree level matching, i.e. without a  $Z_{2}$  symmetry, the SMEFT description is (marginally) valid only in part of the parameter space for a SFO-EWPT. For accurate results dimension 8 operators need to be included, even though the impact of dimension 10 and higher order operators may be small.

As the SMEFT can only be used for a single SM extension, and with limited success, we advise against using the SMEFT as it mostly does not reliably correspond to a UV complete model. There are many papers studying the electroweak phase transition and the implications for baryogenesis and gravitational wave production using SMEFT with dimension 6 operators [15, 17-22, 31, 32], partially because it is very tractable. Our results imply that for most of the interesting parameter space no UV completion exists, and for those points that can be mapped to a Higgs-singlet model, only qualitative results can be obtained.

Finally we note that the EFT language is also used to describe strongly first order phase transitions (SFO-PTs) in a hidden sector, to determine the produced background of gravitational waves [33-35]. As the dark sector is relatively unconstrained, e.g. the mass of the dark Higgs and its couplings to dark fermions and gauge bosons are unknown, it is not surprising that the separation of scales required for the validity of the EFT expansion can be achieved. Nonetheless, we can also formulate conditions on the validity (and usefulness) of the EFT framework for dark sector SFO-PTs.

The structure of this paper is as follows. In section 2 we introduce the Standard Model effective field theory and we discuss the requirements for a first order phase transition, the thermal corrections to the Lagrangian in the early universe, the validity of the SMEFT expansion, and the generalization to dark sectors. In section 3 we review the matching results at tree and loop level. We focus on SM extensions with additional scalars (or gauge bosons), as these can facilitate a first order phase transition. We then discuss the implications for the EWPT and the validity of the SMEFT expansion in section 4. As the singlet-Higgs extension is the most interesting in this context, we provide numerical results for this set-up as well. Details on the numerical implementation can be found in appendix A. We end this section with some comments on dark sector phase transitions. Our results are summarized in section 5.

# 2 SMEFT and first order phase transitions

The SM effective field theory (SMEFT) rests on the assumption that the new particles in extensions of the SM have a mass larger than the electroweak scale, i.e. the scale of the SM states. The effective theory at the electroweak scale is then the SM augmented with a series of gauge invariant higher dimensional operators constructed out of the SM fields, to incorporate the effects of integrating out the heavy physics:

$$
\mathcal {L} _ {\mathrm {S M E F T}} = \mathcal {L} _ {\mathrm {S M}} + \sum_ {i} \frac {1}{M ^ {d _ {i} - 4}} c _ {i} \mathcal {O} _ {i}, \quad \mathcal {L} _ {\mathrm {S M}} = | D _ {\mu} H | ^ {2} - (\mu^ {2} | H | ^ {2} + \lambda | H | ^ {4}) + \dots \tag {2.1}
$$

Here  $M$  is the mass scale of the heavy particles,  $c_{i}$  the Wilson coefficients and  $d_{i}$  the mass dimension of the operator  $\mathcal{O}_i$ . For the electroweak phase transition we are interested in corrections to the kinetic term and potential for the SM Higgs doublet  $H$ , and we only consider operators  $\mathcal{O}_i = \mathcal{O}_i(H)$ .

In this section we discuss the Higgs potential in SMEFT with only dimension 6 operators included, and identify the conditions for a strongly first order electroweak phase transition and the validity of the EFT expansion.

# 2.1 The Higgs potential in SMEFT

The operators in the SMEFT that are at most dimension 6 and relevant for Higgs dynamics are (listed in the Warsaw basis [36])

$$
\begin{array}{l} \mathcal {L} _ {\mathrm {S M E F T}} ^ {(6)} = c _ {\mathrm {H \square}} | H | ^ {2} \square | H | ^ {2} + c _ {H D} | H D _ {\mu} H | ^ {2} + c _ {H} | H | ^ {6} + \mathcal {O} (M ^ {- 4}) \\ = c _ {\text {k i n}} \bar {h} ^ {2} \left(\partial \bar {h}\right) ^ {2} + \frac {1}{8} c _ {H} \bar {h} ^ {6} \tag {2.2} \\ \end{array}
$$

with the last expression written in unitary gauge  $\sqrt{2} H^{\top} = (0\bar{h})$ , and  $c_{\mathrm{kin}} = \frac{1}{4} c_{HD} - c_{\mathrm{H}\square}$ . We can define the approximate canonical field  $h = \bar{h} +\frac{1}{3} c_{\mathrm{kin}}\bar{h}^{3} + \mathcal{O}(c_{\mathrm{kin}}^{2}\bar{h}^{5})$ , solve for  $\bar{h} (h)$  and write the Higgs Lagrangian as

$$
\mathcal {L} _ {\mathrm {S M E F T}} ^ {(6)} \simeq \frac {1}{2} (\partial h) ^ {2} - \left(\frac {1}{2} a _ {2} h ^ {2} + \frac {1}{4} a _ {4} h ^ {4} + \frac {1}{6} a _ {6} h ^ {6}\right), \tag {2.3}
$$

with

$$
a _ {2} = \mu^ {2}, \quad a _ {4} = \lambda - \frac {4}{3} c _ {\mathrm {k i n}} \mu^ {2}, \quad a _ {6} = - \frac {3}{4} c _ {H} - 2 c _ {\mathrm {k i n}} \lambda . \tag {2.4}
$$

The parameters  $a_2, a_4$  are fixed by the measured Higgs vev  $v = 246\mathrm{GeV}$  and Higgs mass  $m_{h0} = 125\mathrm{GeV}$  via

$$
\partial_ {h} V | _ {h = v} = 0, \quad \partial_ {h} ^ {2} V | _ {h = v} = m _ {h 0} ^ {2}. \tag {2.5}
$$

Rewriting the tree-level potential in terms of these physical quantities gives

$$
V = - \frac {1}{4} \left(m _ {h 0} ^ {2} - 2 a _ {6} v ^ {4}\right) h ^ {2} + \frac {1}{4} \left(\frac {m _ {h 0} ^ {2}}{2 v ^ {2}} - 2 a _ {6} v ^ {2}\right) h ^ {4} + \frac {1}{6} a _ {6} h ^ {6}. \tag {2.6}
$$

The full potential governing the phase transition includes the one-loop Coleman-Weinberg (CW) contribution [37] and the thermal corrections of the SM particles  $V_{\mathrm{eff}} = V + V_{\mathrm{CW}} + V_T$ . The off-shell effective action is gauge dependent [38, 39], but at one loop order the gauge dependence is cancelled when rewritten in terms of the canonical Higgs field [40-42]; another prescription to deal with the gauge dependence can be found in [39]. The CW potential introduces a scale dependence; if the theoretical uncertainty this causes becomes large [23], higher order loop contributions should be included. That being said, we choose to work in the on shell renormalization scheme [17, 43] with counter terms chosen such that  $\partial_h V_{\mathrm{CW}}|_{h = v} = \partial_h^2 V_{\mathrm{CW}}|_{h = v} = 0$  at the  $Z$ -pole scale. This results in the property that the higgs vev and mass are set by the parameters of the tree-level potential, which is very convenient for numerical scans. In this prescription, the one-loop Coleman-Weinberg potential is given by

$$
V _ {\mathrm {C W}} = \sum_ {i} \frac {n _ {i}}{(8 \pi) ^ {2}} \left[ m _ {i} ^ {4} \left(\ln \left(\frac {m _ {i} ^ {2}}{m _ {0 i} ^ {2}}\right) - \frac {3}{2}\right) + 2 m _ {i} ^ {2} m _ {0 i} ^ {2} \right], \tag {2.7}
$$

with  $m_{i}$  the field-dependent mass,  $m_{0i}$  the vacuum mass at  $h = v$ , and  $n_i = \{1,3,3,6, - 12\}$  the degrees of freedom (d.o.f). of the Higgs, goldstones,  $Z$ ,  $W$  and top quark respectively, which give the dominant contributions. The thermal potential is

$$
V _ {T} = \sum_ {i = \text {b o s o n s}} n _ {i} T ^ {4} J _ {B} \left(\frac {m _ {h} ^ {2}}{T ^ {2}}\right) + \sum_ {j = \text {f e r m i o n s}} n _ {j} T ^ {4} J _ {F} \left(\frac {m _ {h} ^ {2}}{T ^ {2}}\right) \tag {2.8}
$$

with  $n_i, n_j$  the bosonic and fermion degrees of freedom, and the explicit thermal functions  $J_{B / F}$  given in eq. (A.2). For the bosonic and longitudinal gauge d.o.f. we include the infrared contribution from daisy diagrams [44, 45]. To leading order in the high-temperature expansion, giving  $V_{\mathrm{eff}}$  up to  $\mathcal{O}(T^0)$  corrections, this is equivalent to replacing  $m_i^2 \to m_i^2 + \Pi_i$  with  $\Pi_i$  thermal self energies [46]. More details can be found in appendix A. We expect that our main (qualitative) results on the validity of the EFT description for a SFO-EWPT will not depend on the details of how renormalization and thermal resummations are implemented.

# 2.2 First order phase transition

For  $a_6 \gtrsim m_{h0}^2 / (2v^4)$  the quadratic and quartic terms in the zero temperature potential eq. (2.6) change sign, and the potential has a minimum at the origin and a minimum at finite field value with a barrier in between. The barrier cannot be too large, otherwise the Higgs field will be stuck in the false vacuum until after big bang nuclear synthesis; in fact, for  $a_6 \gtrsim 3m_{h0}^2 / (4v^4)$  the minimum at the origin is the true minimum.

A strong first order electroweak phase transition can happen if the potential parameters are close to the critical point of the sign flip

$$
a _ {6} \sim \frac {m _ {h 0} ^ {2}}{2 v ^ {4}} \approx (6 8 5 \mathrm {G e V}) ^ {- 2}, \tag {2.9}
$$

such that with quantum and temperature effects included there is a barrier at electroweak scale temperatures. For small  $a_6 \ll m_{h0}^2 / v^4$  the potential is far from the critical point, and order one loop CW and/or thermal corrections are needed to get a barrier, which would make the theory non-perturbative. Note that we also can write eq. (2.9) as

$$
- a _ {4} \sim a _ {6} v ^ {2} \sim \frac {m _ {h 0} ^ {2}}{2 v ^ {2}} \approx 0. 1 2. \tag {2.10}
$$

In the EW minimum (at zero temperature) the dimension 4 and dimension 6 terms of the potential are balanced. The right-most numerical expression is valid for the measured SM quantities.

# 2.3 Temperature corrections

The thermal corrections to the potential are given in eq. (2.8) and we will briefly show that the effect of the dimension six operator on the thermal corrections to the potential is small. Consider a SM extension with a heavy scalar field  $\Phi$  with mass  $m_{\Phi}^{2} \gg T^{2}$ . Its thermal corrections are Boltzmann suppressed  $V_{T}^{(\Phi)} \propto \mathrm{e}^{-m_{\Phi} / T}$ , see eq. (A.2). The heavy degree of freedom decouples and can be integrated out. In SMEFT the dimension 6 (and higher) operators correct the Higgs mass. As the thermal correction depends on the masses, there is thus still an effect. However, this correction is power law suppressed — it does not have the Boltzmann suppression factor, and it corresponds to a two-loop effect in the UV theory. In a perturbative theory and in the decoupling limit, it is small.

To be explicit, the Higgs loop gives a contribution to the thermal potential  $V_T^{(h)} \propto T^4 J_B\left(\frac{m_h^2}{T^2}\right) \sim m_h^2 T^2 + m_h^3 T + \mathcal{O}\left(\frac{m_h^4}{T^4}\right)$ . The Higgs mass in the EFT is

$$
m _ {h} ^ {2} = a _ {2} + 3 a _ {4} h ^ {2} + 5 a _ {6} h ^ {4} = - \frac {1}{2} m _ {h 0} ^ {2} + a _ {6} v ^ {4} + \frac {3}{2} \left(\frac {m _ {h 0} ^ {2}}{v ^ {2}} - 4 a _ {6} v ^ {2}\right) h ^ {2} + 5 a _ {6} h ^ {4} \tag {2.11}
$$

For  $a_6 \sim m_{h0}^2 / (4v^4)$  the dimension 6 operator can give an order one correction to  $h^2$ -term, and consequently to the Higgs contribution to the thermal mass and cubic term in the effective potential. Nonetheless, this will only have a small impact on the total thermal corrections, which are dominated by the loops of the gauge bosons and top quark, as the couplings are much larger than the Higgs self coupling  $g^2, g'^2, y_t^2 \gg m_h^2 / (2v^2)$ . In the SMEFT, the thermal corrections to the potential are thus to a good approximation the same as in the SM.

The SM does not have a strongly first order electroweak phase transition. Let us ignore the dimension six term for the moment and see how this comes about [47]. Including thermal corrections, the potential in the high temperature limit is of the form

$$
V _ {\mathrm {S M}} = \frac {1}{2} a _ {2} (T) h ^ {2} - \frac {1}{2 \sqrt {2}} E T h ^ {3} + \frac {1}{4} a _ {4} h ^ {4}, \tag {2.12}
$$

with  $a_2(T)$  the quadratic term including thermal corrections, and  $E$  the coefficient of the cubic thermal corrections of the bosonic fields. At the critical temperature,  $T_{c}$ , when the potential has two degenerate minima at field values  $h = 0$  and  $h = v_{c}$  (determined by the conditions  $V|_{h=0} = V|_{h=v_{c}}$  and  $\partial_{h}V|_{h=v_{c}} = 0$ ), one finds

$$
R _ {c} \equiv \frac {v _ {c}}{T _ {c}} = \frac {E}{\sqrt {2} a _ {4}} = \frac {\sqrt {2} v ^ {2} E}{m _ {h 0} ^ {2}}. (2. 1 3)
$$

The physical quantity of interest is the strength of the phase transition at the nucleation temperature  $R_{N} \sim v_{N} / T_{N}$ , rather than the critical temperature. A strong first order electroweak phase transition requires  $R_{N}$  larger than unity. Typically  $R_{c} \sim R_{N}$  and working with the expression for  $R_{c}$  allows us to make useful analytical estimates. In our numerical analysis and figures we will always plot  $R_{N}$ . As was recently pointed out in [49], for accurate parameter scans of the parameters space for a SFO-EWPT it is important to work with  $R_{N}$  as otherwise the results can be markedly different. A strong first order transition is not realized in the SM, as the value of  $E$  is too small. Adding the dimension 6 term will predominantly affect the denominator in eq. (2.13). We can get an estimate of the strength of the phase transition in SMEFT by using equation eq. (2.6) to modify the quartic coefficient  $a_{4}$  in the denominator

$$
R _ {c} \approx \frac {E}{\sqrt {2} \left(m _ {h 0} ^ {2} / (2 v ^ {2}) - 2 a _ {6} v ^ {2}\right)}. \tag {2.14}
$$

It is clear that it is now possible to tune the denominator small to get  $R_{c} > 1$  if we take  $a_{6}$  close to the critical value in (2.9). This is basically the derivation of the arguments in the previous subsection.

![](images/ba4ef88792c2b0f67703d24d50287361cecc0743e14c6a197563f16cea09b4f4.jpg)

![](images/58016465a6b5f4d4989de38de071b9c46f02ef1a4c66cafe6e9500270e635204.jpg)  
Figure 1. The strength of the first order phase transition  $R_{N} = \frac{v_{N}}{T_{N}}$  as function of  $\Lambda$  and  $c_{8}$  in SMEFT (left plot) and for a dark Higgs mass of  $m_{h_D} = 80 \, \text{GeV}$  and all other parameters as in the SM (right plot). The red line corresponds to the SMEFT truncated at dimension 6, which is a good approximation only when the dimension 8 operator is negligible. In the white region there is no cosmological first order phase transition to the electroweak vacuum.

![](images/00a21f7fee738ce7273f452aa7dea2b103d8be5589ecb633b54c982f952fd5c8.jpg)

![](images/f95a6324285bbe310bac466d5b61e0837c085234d0ee7eb891cf82180cbd91d8.jpg)

# 2.4 Validity of the SMEFT

The first demand on the validity of the EFT is that the dimension 6 corrections to the kinetic terms are small

$$
2 c _ {\text {k i n}} v ^ {2} <   \frac {1}{2} \tag {2.15}
$$

This assures the dimension eight and higher order derivative operators have a subdominant effect. This condition was already used in defining the canonical field to arrive at eq. (2.3).

We further demand that the higher order corrections to the potential are small as well, starting with the dimension 8 term. We parameterize the potential including dimension 8 terms as

$$
V = \frac {1}{2} a _ {2} h ^ {2} + \frac {1}{4} a _ {4} h ^ {4} + \frac {1}{6} a _ {6} h ^ {6} + \frac {1}{8} a _ {8} h ^ {8} = \frac {1}{2} a _ {2} h ^ {2} + \frac {1}{4} a _ {4} h ^ {4} + \frac {1}{6} \frac {h ^ {6}}{\Lambda^ {2}} + \frac {c _ {8}}{8} \frac {h ^ {8}}{\Lambda^ {4}} \tag {2.16}
$$

with the cutoff scale  $\Lambda^2 = a_6^{-1}$  and  $c_{8} = a_{8} / a_{6}^{2}$ . In the EW vacuum the dimension 4 and dimension 6 operators are balanced eq. (2.10); requiring the dimension 8 contribution to be small thus leads to the condition

$$
\frac {\left| a _ {8} \right| v ^ {2}}{a _ {6}} = \frac {c _ {8} v ^ {2}}{\Lambda^ {2}} <   \frac {1}{2} \tag {2.17}
$$

The conditions eqs. (2.15) and (2.17) assure that the separation of scales between the light and heavy degrees of freedom required for the EFT expansion in operators of increasing mass dimensions converges. Depending on the accuracy aimed for, the EFT can then be truncated at a given mass dimension. To get accurate results for the parameters

of the phase transition, e.g. the nucleation temperature and the strength of the phase transition  $R_{N} = \frac{v_{N}}{T_{N}}$ , in SMEFT at dimension 6 operators is only possible if the ratio in eq. (2.17) is sufficiently small. In the left plot of figure 1 we show the numerical results for  $R_{N}$  as a function of the cutoff scale  $\Lambda$  and coefficient of the dimension 8 operator  $c_{8}$ . All parameter scans are done with the CosmoTransitions package [50]; details on our implementation can be found in appendix A. Numerically calculating the tunneling solution at nucleation temperature is challenging, especially in regions of parameter space where a first order phase transition is only just possible. In the raw data there are many spurious numerical data points. In our figures we have smoothed the results a bit to focus on the content important for the EFT analysis. It should be kept in mind, though, that especially the boundary regions are fuzzy.

Turning on the dimension 8 operator and changing  $c_{8}$  from zero to order one values generically gives a change in  $R_{N}$  of  $10\%$  or larger. From this we conclude that a quantitative description of the phase transition — with parameters determined within  $10\%$  accuracy — requires

$$
\left| c _ {8} \right| \lesssim 1 \tag {2.18}
$$

which is a stronger condition than convergence of the EFT eq. (2.17). Although this conditions seem independent of the scale separation in eq. (2.17), this is not the case, as will become clear as we discuss dark sector phase transitions in the next subsection. We further note that eqs. (2.15) and (2.17) assures the EFT validity in the electroweak vacuum, which not necessary implies the same during the phase transition (although it gives a good indication). Condition eq. (2.18), on the other hand, derives directly from the phase transition dynamics.

# 2.5 Dark phase transition

Let us also discuss the validity of an EFT description for a strongly first order phase transition (SFO-PT) in a dark sector with a potential  $V(|H_D|^2)$  for the dark Higgs field  $H_{D}$  that mimics that of the SM. The important difference is that the dark Higgs mass and vev, as well as the thermal corrections (in particular the size of the cubic term  $E$ ) are now all free parameters not fixed by experiment. We will assume that the dimension 6 terms are essential for obtaining a strong first order phase transition, and that in its absence  $R_N < 1$ ; otherwise the EFT description can always be made to work by taking the cutoff scale arbitrarily large. This leads to the condition

$$
\frac {m _ {h _ {D} 0} ^ {2}}{v _ {D} ^ {2}} \gtrsim \sqrt {2} E \sim 0. 0 3 n _ {g} g ^ {2} \tag {2.19}
$$

if the dark Higgs couples to  $n_g$  thermal bosonic degrees of freedom with coupling  $g$ .

The requirement on the parameter space for a SFO-PT can be read off again from the expression for  $R_{c}$  in eq. (2.14). As we have seen, in the SM the measured Higgs mass is far off the critical value, and the correction of the dimension 6 term to the potential needs to be order one. In the dark sector the ratio  $m_{h_D0}^2 /(2v_D^2)$  can be small and much closer to the critical value, allowing the dimension 6 term to only give a small (but essential) correction. This allows for a larger cutoff scale and a thus a better convergence of the EFT expansion.

This is confirmed by our numerical results. The right plot in figure 1 shows  $R_N$  as a function of the cutoff  $\Lambda$  and dimension 8 coefficient  $c_8$  for a dark Higgs mass of  $m_{h_D0} = 80\mathrm{GeV}$ ; the dark Higgs vev and thermal spectrum are chosen as in the SM. We indeed see that for a smaller ratio  $m_{h_D0}^2 /(2v_D^2)$  than in the SM, the cutoff scale of the dimension 6 operator is much larger in the parameter space for a SFO-PT. As a consequence of the much larger separation of scales, the dependence on  $c_8$  is less as well.

# 3 Matching the SMEFT to UV theories

We consider the SM augmented with heavy degrees of freedom. If the heavy fields are flavor diagonal, the low energy EFT can be matched to the UV theory using the covariant derivative expansion method of [51-54] (for a SMEFT review, see [14]). For flavor off-diagonal new physics the more general SMEFT structure of [55-58] can be used, which also includes the effects of mixed diagrams with both heavy and light fields in the loop.

We focus on the simplest possibility of adding a single (multiplet) field to the SM, and use the covariant derivative expansion method. We will briefly comment on more complicated set-ups with multiple heavy fields in section 4.4. To match the UV theory onto SMEFT, the effective action is calculated and expanded in powers of the mass parameter of the heavy field. We will discuss tree level and loop level matching in turn.

# 3.1 Tree-level matching

The SMEFT higher dimensional operators can be generated by tree level diagrams if the heavy field  $\Phi$  has a non-zero vacuum expectation value (vev). This limits the possibilities to (effective) scalar fields. Furthermore, the model space is severely limited by electroweak precision constraints. Specifically, if we add new scalar degrees of freedom with non-zero vev  $v_{i}$  to the SM, the  $\rho$ -parameter becomes

$$
\rho = \frac {\sum_ {i} (4 I _ {i} (I _ {i} + 1) - Y _ {i} ^ {2}) v _ {i} ^ {2}}{\sum_ {i} Y _ {i} ^ {2} v _ {i} ^ {2}}, \tag {3.1}
$$

with  $I_{i}, Y_{i}$  the isospin and hypercharge of the additional multiplets. For singlets with  $I = Y = 0$  or additional doublets with  $I = 1/2, Y = 1$  the  $\rho$ -parameter is the same as in the SM  $\rho = \rho_{\mathrm{SM}}$ . For all other multiplets  $X$  the precise measurement of  $\rho - \rho_{\mathrm{SM}} = 0.0038 \pm 0.00020$  [59] severely limits the size of the vev  $v_{X}^{2}/v^{2} \lesssim 10^{-2}$ . This implies that the mass of this multiplet has to be in the  $10\mathrm{TeV}$  range or higher, and the set-up is not interesting for the EWPT. This leaves Higgs-singlet extensions and two Higgs doublet models as the interesting cases for tree level matching, which we will discuss in detail in the next section. Here we briefly recap the generic tree-level matching results.

Write the UV Lagrangian for the heavy complex scalar (multiplet)  $\Phi$  in the form

$$
\mathcal {L} _ {\mathrm {U V}} = \left(\Phi^ {\dagger} B + \mathrm {h . c .}\right) + \Phi^ {\dagger} (- D ^ {2} - M ^ {2} - U) \Phi + \mathcal {O} \left(\Phi^ {3}\right), \tag {3.2}
$$

with  $M$  the field-independent mass of the heavy field, and  $B(H),\mathrm{U}(H)$  parameterizing the coupling to the Higgs field. Since we are only interested in the Higgs dynamics we can replace covariant derivatives with partial derivatives  $D^{2} = \partial^{2}$ . For a real scalar field we

can substitute  $\Phi = \Phi^{\dagger} \rightarrow \phi / \sqrt{2}$ . The scalar vev will be non-zero for  $B \neq 0$ , and we can integrate it out using its equation of motion:

$$
(P ^ {2} - M ^ {2} - U) \Phi = - B + \mathcal {O} (\Phi^ {2}) \tag {3.3}
$$

with  $P^2 = -\partial^2$ . To leading approximation (for small couplings of the  $\mathcal{O}(\Phi^3)$  terms) the solution is

$$
\Phi_ {c} = - \frac {1}{P ^ {2} - M ^ {2} - U} B. \tag {3.4}
$$

We can improve this perturbatively by replacing  $B \to B + \mathcal{O}(\Phi_c^2)$ , where the higher order terms are evaluated at the 0th order solution  $\Phi_c$ . Plugging back in the action gives

$$
\begin{array}{l} \mathcal {L} _ {\mathrm {t r e e - l e v e l}} = - B ^ {\dagger} \frac {1}{P ^ {2} - M ^ {2} - U} B + \mathcal {O} (\Phi_ {c} ^ {3}) \\ = \frac {1}{M ^ {2}} B ^ {\dagger} B + \frac {1}{M ^ {4}} B ^ {\dagger} (P ^ {2} - U) B + \frac {1}{M ^ {6}} B ^ {\dagger} (P ^ {2} - U) ^ {2} B + \mathcal {O} (M ^ {- 8}) + \mathcal {O} \left(\Phi_ {c} ^ {3}\right), \tag {3.5} \\ \end{array}
$$

where we expanded in large  $M^2$  and demand that EFT expansion is valid (cf. eqs. (2.15) and (2.17))

$$
\frac {P ^ {2} - U}{M ^ {2}} \ll 1, \quad \frac {| B | ^ {2}}{M ^ {2}} \ll v ^ {2}. \tag {3.6}
$$

# 3.2 Loop-level matching

In addition to the tree level matching there will also be loop level matching contributions to the SMEFT operators. Focus on a scalar extension again with the UV Lagrangian given in eq. (3.2). For theories with  $B = 0$  there are only loop-level matching contributions. Vanishing of  $B$  may be enforced by symmetries, for example, in Higgs-singlet extensions the linear  $B$ -term can be forbidden by a  $Z_{2}$  symmetry under which the singlet transforms as  $\Phi \rightarrow -\Phi$ .

Calculating the one-loop corrections to the effective action and expanding in powers of  $M^2$ , the results can be matched to the SMEFT Lagrangian [54]. The logarithmically divergent  $M^4$  and  $M^2$ ,  $M^0$ -terms contribute to the cosmological constant, and the  $\mu$ -term and Higgs self-coupling respectively. The quadratic and quartic counterterms in the SMEFT are fixed by our on-shell renormalization condition. Let's then focus on the finite dimension 6 and dimension 8 operators

$$
(4 \pi) ^ {2} c _ {i} ^ {- 1} \mathcal {L} _ {\text {l o o p}} = \operatorname {t r} \left[ \frac {1}{M ^ {2}} \left(- \frac {1}{6} U ^ {3} + \frac {1}{1 2} (\partial_ {\mu} U) ^ {2}\right) + \frac {1}{M ^ {4}} \left(\frac {1}{2 4} U ^ {4} - \frac {1}{1 2} \mathrm {U} (\partial_ {\mu} U) ^ {2} + \frac {1}{1 2 0} (\partial^ {2} U) ^ {2}\right) \right] \tag {3.7}
$$

with  $c_{i} = 1 / 2(1)$  for a real (complex) scalar. The trace over the gauge indices depends on the representation of the heavy d.o.f. The results eq. (3.7) can also be applied to UV theories with a heavy fermion or gauge field, with  $c_{i}$  and  $U$  taken as in [54]. For fermions the loop contributions have a minus sign, and are of no help for obtaining a SFO-PT. If the Higgs field is charged under a gauge symmetry that is broken at a large scale, there can be a  $g^{2}h^{2}B^{2}$ -interaction term in the Lagrangian, with  $B$  the heavy gauge field,

and the loop matching results will qualitatively be similar to the scalar field case with a  $\kappa h^2 |\Phi |^2$ -interaction [54].

The result eq. (3.7) is valid if both the EFT expansion in powers of  $M^{-2}$  and the perturbative loop expansion holds, which gives respectively

$$
\frac {U}{M ^ {2}} \ll 1, \quad \& \quad \frac {c _ {i} \kappa^ {2}}{(4 \pi) ^ {2}} \ll 1. \tag {3.8}
$$

# 4 Phase transitions in UV theories and in SMEFT

In this section we analyse the parameter space for a strongly first order electroweak phase transitions in specific UV theories, and compare that with the results obtained using the EFT description. We focus on the most interesting cases of singlet extensions of the SM, both with tree-level and only loop level matching, and two Higgs doublet models. We will also discuss how results can be adapted to dark phase transitions.

# 4.1 Loop level matching: scalar extensions

Consider a  $Z_{2}$ -symmetric scalar extension of the SM, with no linear interaction in eq. (3.2) and  $B = 0$ . The SMEFT operators then only arise from the loop diagrams as in eq. (3.7). For a singlet field the interaction term is

$$
U = \frac {1}{2} \kappa h ^ {2} \tag {4.1}
$$

expressed in unitary gauge  $|H|^2 = h^2 / 2$ . For scalar multiplets there will be gauge generators as well and the dimension 6 operator in eq. (3.7) may be enhanced by trace factors. However, generically the dimension 8 and higher terms will then be likewise enhanced, and the perturbativity constraint is stronger for larger  $c_i$  — we thus do not expect that the multiplet structure will significantly improve the EFT validity eq. (3.8) and for simplicity we work with eq. (4.1) above.

We can then read off the explicit Wilson coefficients by comparing the general expression in eq. (3.7) with eq. (2.2)

$$
c _ {H} = - \frac {c _ {i}}{6 M ^ {2} \left(4 \pi^ {2}\right)} \kappa^ {3}, \quad c _ {\text {k i n}} = \frac {c _ {i}}{1 2 M ^ {2} (4 \pi) ^ {2}} \kappa^ {2} \quad \Rightarrow \quad a _ {6} = \frac {c _ {i}}{M ^ {2} (4 \pi) ^ {2}} \left(\frac {1}{8} \kappa^ {3} + \frac {1}{6} \kappa^ {2} \lambda\right). \tag {4.2}
$$

The requirement that  $c_{\mathrm{kin}}$  gives a small correction to the kinetic term eq. (2.15) is satisfied automatically for a perturbatively small coupling  $\kappa$ . For the singlet to have an impact on the phase transition dynamics, and thus for the dimension 6 term in the SMEFT approximation to be sufficiently large, requires relatively large couplings  $\kappa_i \gtrsim 1$ . As a first approximation we can then neglect  $c_{\mathrm{kin}}$  and thus the  $(\partial U)$  derivative terms in eq. (3.7).

A strong first order electroweak phase transition requires balancing the dimension 4 and dimension 6 terms eq. (2.10). Neglecting the derivative terms this gives

$$
\frac {1}{4} \frac {c _ {i} \kappa^ {2}}{(4 \pi) ^ {2}} \frac {U}{M ^ {2}} \sim \frac {m _ {h 0} ^ {2}}{v ^ {2}} \approx 0. 1 2. \tag {4.3}
$$

This cannot be satisfied without either violating the EFT expansion or the loop expansion eq. (3.8). We thus conclude that the SMEFT framework with only loop-suppressed higher order operators cannot be used for SFO-EWPTs.

# 4.1.1 Dark sector

Turning our attention to dark sectors, we recall that for a dark Higgs potential  $V(|H_{D}|^{2})$  with  $H_{D}$  the dark sector Higgs field, a strong first order phase transition is possible if

$$
\frac {m _ {h _ {D} 0} ^ {2}}{v _ {D} ^ {2}} \sim \frac {1}{2} \frac {c _ {i} \kappa^ {2}}{(4 \pi) ^ {2}} \frac {U}{M ^ {2}} = \frac {\kappa}{4} \frac {c _ {i} \kappa^ {2}}{(4 \pi) ^ {2}} \frac {v _ {D} ^ {2}}{M ^ {2}} \ll 1 \tag {4.4}
$$

which can be satisfied for sufficiently small dark Higgs mass. Note, however, that the  $(m_{h_D0}^2 /v_D^2)$ -ratio can also not be too small if the dimension 6 term is to be essential for the SFO-PT, see eq. (2.19), which limits the applicability of the EFT framework for loop-level matching.

# 4.2 Tree level matching: two Higgs doublet models

In two Higgs doublet models (2HDMs) both Higgs fields can obtain a vev. If there is a separation of scales between the Standard Model-like Higgs and the heavy Higgs, this allows for an EFT description with tree level matching. The most general effective potential in the 2HDM is given by [60-62]

$$
\begin{array}{l} V _ {H} = m _ {1 1} ^ {2} \Phi_ {1} ^ {\dagger} \Phi_ {1} + m _ {2 2} ^ {2} \Phi_ {2} ^ {\dagger} \Phi_ {2} - (m _ {1 2} ^ {2} \Phi_ {1} ^ {\dagger} \Phi_ {2} + \mathrm {h . c .}) \\ + \frac {1}{2} \lambda_ {1} \left(\Phi_ {1} ^ {\dagger} \Phi_ {1}\right) ^ {2} + \frac {1}{2} \lambda_ {2} \left(\Phi_ {2} ^ {\dagger} \Phi_ {2}\right) ^ {2} + \lambda_ {3} \left(\Phi_ {1} ^ {\dagger} \Phi_ {1}\right) \left(\Phi_ {2} ^ {\dagger} \Phi_ {2}\right) + \lambda_ {4} \left(\Phi_ {1} ^ {\dagger} \Phi_ {2}\right) \left(\Phi_ {2} ^ {\dagger} \Phi_ {1}\right) \\ + \left[ \frac {1}{2} \lambda_ {5} \left(\Phi_ {1} ^ {\dagger} \Phi_ {2}\right) ^ {2} + \lambda_ {6} \left(\Phi_ {1} ^ {\dagger} \Phi_ {1}\right) \left(\Phi_ {1} ^ {\dagger} \Phi_ {2}\right) + \lambda_ {7} \left(\Phi_ {2} ^ {\dagger} \Phi_ {2}\right) \left(\Phi_ {1} ^ {\dagger} \Phi_ {2}\right) + h. c. \right] \tag {4.5} \\ \end{array}
$$

We identify  $\Phi_1 = H$  with the Standard Model-like Higgs and  $\Phi_2 = \Phi$  with the heavy degree of freedom. Then

$$
B = A _ {2} H + A _ {0} H \left(H ^ {\dagger} H\right), \quad U = \lambda_ {3} H ^ {\dagger} H + \lambda_ {4} H H ^ {\dagger}, \tag {4.6}
$$

with  $A_2 = -m_{12}^2$ ,  $A_0 = -\lambda_6$  (the subscript on  $A$  denotes the mass dimension of the coupling), and  $M^2 = m_{22}^2$ .

The leading corrections to the kinetic terms are

$$
\mathcal {L} _ {M} \supset - \frac {1}{M ^ {4}} \left[ A _ {2} H ^ {\dagger} + A _ {0} \left(H ^ {\dagger} H\right) H ^ {\dagger} \right] \square \left[ A _ {2} H + A _ {0} H \left(H ^ {\dagger} H\right) \right], \tag {4.7}
$$

which are perturbatively small eq. (2.15) for

$$
\frac {\left| B \right| ^ {2}}{M ^ {4}} \ll v ^ {2} \Rightarrow \frac {\left| A _ {2} \right|}{M ^ {4}} \ll 1 \& \frac {\left| A _ {0} \right| ^ {2} v ^ {4}}{M ^ {4}} \ll 1. \tag {4.8}
$$

The  $\square$ -corrections above are subdominant for  $\lambda_{3,4} > \lambda$ , which follows from using the Higgs equations of motion  $\square h = -\partial_h V_{\mathrm{SM}} + \mathcal{O}(M^{-2})$ . This is indeed the limit of interest for

a SFO-EWPT, which requires a strong coupling between the Higgs and the heavy field. Ignoring then the dimension 6 derivative operators the effective potential is

$$
V _ {\mathrm {E F T}} = \frac {h ^ {6}}{8 M ^ {2}} \left(- | A _ {0} | ^ {2} + \frac {2 \kappa \mathrm {R e} (A _ {0} A _ {2})}{M ^ {2}} - \frac {\kappa^ {2} | A _ {2} | ^ {2}}{M ^ {4}}\right), \tag {4.9}
$$

with  $\kappa = \lambda_3 + \lambda_4$ . The dimension 6 term is negative, which does not work for obtaining a SFO-EWPT in SMEFT at this mass dimension. An electroweak minimum separated by a barrier from the minimum at the origin can only be obtained balancing the dimension 6 with positive dimension 8 terms. This clearly violates the EFT expansion, and we conclude that the SMEFT framework fails to describe SFO-EWPT in two Higgs doublet models.

# 4.3 Tree level matching: Higgs-singlet models

Consider the SM coupled to a real singlet field  $s$  with Lagrangian

$$
\mathcal {L} \supset | D H | ^ {2} + \frac {1}{2} (\partial s) ^ {2} - \left(\mu_ {0} ^ {2} | H | ^ {2} + \frac {1}{2} M ^ {2} s ^ {2} + \lambda_ {0} | H | ^ {4} + \frac {\lambda_ {s}}{4} s ^ {4} + \frac {\kappa}{2} | H | ^ {2} s ^ {2} - A _ {1} | H | ^ {2} s + \frac {g _ {s} A _ {1}}{3} s ^ {3}\right). \tag {4.10}
$$

Setting  $A_{1}$  to zero, the Lagrangian has a discrete  $Z_{2}$ -symmetry. The tree level matching contributions are thus proportional to  $A_{1}$ . Specifically, we identify (cf. eq. (3.2))

$$
U = \kappa | H | ^ {2} = \frac {1}{2} \kappa h ^ {2}, \quad B = \sqrt {2} A _ {1} | H | ^ {2} = \frac {1}{\sqrt {2}} A _ {1} h ^ {2} \tag {4.11}
$$

The leading SMEFT Lagrangian operators are<sup>3</sup>

$$
\mathcal {L} _ {\mathrm {E F T}} \supset - \frac {\left| A _ {1} \right| ^ {2}}{8 M ^ {4}} h ^ {2} \square h ^ {2} - \frac {\kappa \left| A _ {1} \right| ^ {2}}{1 6 M ^ {4}} h ^ {6} + \frac {\left| A _ {1} \right| ^ {2} \kappa^ {2}}{3 2 M ^ {6}} h ^ {8} + \dots \tag {4.12}
$$

The dimension 6  $\square$ -operator that corrects the Higgs kinetic term is small enough for the EFT expansion to be valid eq. (3.6), and singlet loop diagrams constructed with the  $A_{1}$ -coupling are perturbative, for respectively

$$
\frac {\left| A _ {1} \right| ^ {2} v ^ {2}}{4 M ^ {4}} \ll 1 \quad \& \quad \frac {\left| A _ {1} \right| ^ {2}}{M ^ {2}} \ll (4 \pi) ^ {2} \tag {4.13}
$$

which are both not very strong constraints.

The matching is performed at the heavy scale  $M$ . We will neglect the running of the parameters between this scale and the  $Z$ -scale relevant for the electroweak phase transition, as the separation is not large and we expect this effect to be small. Using  $-h^2 \Box h^2 = 4h^2 (\partial h)^2$  we read off  $c_{\mathrm{kin}} = |A_1|^2 / (2M^4)$  and  $c_H = -\kappa |A_1|^2 / (2M^4)$ . Comparing with

eq. (2.4) this gives a SMEFT effective potential  $V = \sum_{n} \frac{1}{2n} a_{2n} h^{2n}$  for the canonically normalized Higgs field, with

$$
a _ {2} = \mu^ {2}, \quad a _ {4} = \lambda - \frac {2}{3} \frac {\left| A _ {1} \right| ^ {2} \mu^ {2}}{M ^ {4}}, \quad a _ {6} = \frac {3}{8} \frac {\left| A _ {1} \right| ^ {2}}{M ^ {4}} \left(\kappa - \frac {8}{3} \lambda\right), \quad a _ {8} = - \frac {\left| A _ {1} \right| ^ {2} \kappa^ {2}}{4 M ^ {6}} + \mathcal {O} \left(\lambda , \frac {\mu^ {2}}{M ^ {2}}\right). \tag {4.14}
$$

For simplicity, in this procedure we have neglected the dimension 8 derivative operators, and the corrections to  $a_8$  from rewriting the potential in terms of the canonical field. In the parameter space of interest the potential corrections dominate over the derivative corrections, and this is a good approximation. The parameters  $(\mu, \lambda)$  are fixed by the on shell renormalization conditions discussed below eq. (2.6). In addition to these tree level matching results there will also be the subdominant loop level corrections, as discussed in section 4.1. We will neglect them in our discussion below, as they will not change our qualitative results; but for a precise quantitative discussion they should be included as well.

A strong first order phase transition can arise if eq. (2.9) is satisfied, which gives

$$
0. 1 2 \simeq \frac {m _ {h 0} ^ {2}}{2 v ^ {2}} \sim a _ {6} v ^ {2} = \frac {3}{8} \frac {\kappa | A _ {1} | ^ {2} v ^ {2}}{M ^ {4}} \ll \frac {3}{4} \frac {| A _ {1} | ^ {2}}{M ^ {2}}, \tag {4.15}
$$

where in the last step we used  $U \ll M^2$ , see eq. (3.6), to assure the convergence of the EFT expansion. We used here that  $\lambda \ll \kappa$  in the parameter space of interest, which is the statement that the dimension 6□-corrections are subdominant. The above condition can be marginally satisfied and SMEFT may adequately describe the SFO-EWPT for  $|A_1|^2 \sim M^2$  (satisfying eq. (4.13)) and for  $U / M^2 \gtrsim 0.1$  not too small (and thus for large  $\kappa$ ). The cutoff scale of the dimension 6 operator and the coefficient of the dimension 8 operator, both defined in eq. (2.16) are

$$
\Lambda^ {2} = \frac {8}{3} \frac {M ^ {4}}{\kappa | A _ {1} | ^ {2}}, \quad c _ {8} = - \frac {1 6}{9} \frac {M ^ {2}}{| A _ {1} | ^ {2}}. \tag {4.16}
$$

Since  $c_8 = \mathcal{O}(1)$  for  $|A_1|^2 \sim M^2$ , for an accurate description of the phase transition the dimension 8 terms should be included, as follows from eq. (2.10).

Finally, we note that there is a phenomenological constraint on the vev of the scalar field denoted by  $s_0$ . Defining the mixing angle via  $h_1 = h\cos \theta +s\sin \theta$  with  $h_1$  the lightest, mostly-Higgs mass eigenstate, gives (the full expression for  $y$  is given in eq. (A.6))

$$
\tan \theta = \frac {y}{1 + \sqrt {1 + y ^ {2}}}, \qquad y = \frac {2 v (A _ {1} - \kappa s _ {0})}{M ^ {2}} + \mathcal {O} (M ^ {- 4}). \tag {4.17}
$$

For singlet masses  $m_{s} \gtrsim 600\mathrm{GeV}$  the experimental bound was derived in ref. [3] to be  $\cos \theta \gtrsim 0.97(0.91)$  at  $2\sigma (3\sigma)$ .

# 4.3.1 Numerical results

As our analytic results are order-of-magnitude estimates only, and because we find that SMEFT might provide a good description of the phase transition in part of parameter space of singlet-extensions, we also performed numerical scans. The details on the implementation can be found in appendix A.

![](images/6e90410c77cc7109257d2c5672f5b6c2c99e54108d3dfb5a781705853bca5447.jpg)

![](images/b6277d9b4f3f9d0453f8263110146f2b161cb9f73e8db33bf227a30dec22e403.jpg)  
(a) Strength of the first order phase transition  $R_N$  as function of the singlet vev  $s_0$  and mass  $m_s$  in the Higgs-singlet model with  $\kappa = 4$  (left plot) and  $\kappa = 2$  (right plot). The gray arched area in top right corner is excluded by the  $2\sigma$  constraint on the mixing parameter; the  $3\sigma$  constraint does not affect parameter space. The white hole that appears in the top-right figure around  $m_s \sim 1$  TeV,  $s_0 \sim 40$  GeV is most likely a numerical artifact.

![](images/881ddaabd9454b3eb8326ee2cc7291534b5e4f642575a6cf36003e18dea4a9c3.jpg)

![](images/37cde9d7930db6594adc388627198e49b34dcdfa5a91c7a9b2e760f8f35f7e6b.jpg)

![](images/8196eed031653b32eaad1c703f50a6abfae2196ed31e8699d52822b0add3256c.jpg)

![](images/d86cf2cb2db43e3704e6255af26f89958d84303aa76f1af05b0bf1949d6eb39c.jpg)  
(b) Strength of the first order phase transition  $R_N$  as function of the EFT parameters  $\Lambda$  and mass  $c_8$ . The red lines for constant  $R_N$  in the singlet model are mapped to the corresponding SMEFT parameters for  $\kappa = 4$  (left plot) and  $\kappa = 2$  (right plot).

![](images/a9f00439bc5e6fb26cdfa98ecf837773712acf71702bb8ce6c49c54184c85964.jpg)

![](images/be769108aa6f09f6946ed1c1beb488192a099d86cdcba9908356c35d02c937d1.jpg)  
Figure 2. Parameter space for a SFO-EWPT in the singlet extension of the standard model (top row) and SMEFT (bottom row). The solid (dashed) red lines correspond to  $R_{N} = \frac{v_{N}}{T_{N}} = 1$  (1.4) in the singlet model; the magenta lines show the same mapping of the equi- $R_{N}$  but without the inclusion of the box-operators in the EFT, i.e., for  $c_{\mathrm{kin}} = 0$ . Further, the solid (dashed) green lines correspond to  $a_{8}v^{2} / a_{6} = 0.5$  (0.3) and theq solid (dashed) black lines to  $\Lambda = 600$  (800) GeV in SMEFT. These lines are mapped between Higgs-singlet model and SMEFT parameters and shown in both plots for  $\kappa = 4$  (right side) and  $\kappa = 2$  left side; in both cases  $(g_{s},\lambda_{s}) = (0,1)$ .

![](images/c3e1bbfa1246b48f996edd9f0a2248bdaa2c48bdd4498d84a01f4b4e57a1b069.jpg)  
Figure 3.  $(R_N)_{\mathrm{EFT}}$  on the x-axis vs.  $(R_N)_{\mathrm{UV}}$  on the y-axis for points from the singlet scan with  $\kappa = 4$  in figure 2; in the left plot we included all points with  $c_8v^2 /\Lambda^2 < 0.5$ , and in the right plot all points with  $c_8v^2 /\Lambda^2 < 0.3$ . The red line corresponds to  $(R_N)_{\mathrm{EFT}} = (R_N)_{\mathrm{UV}}$ . The blue, orange, green points correspond to SMEFT with only dimension 6 operators, SMEFT with dimension 6 and dimension 8 operators, and SMEFT with dimension 6 & 8 and dimension 6 derivative corrections.

![](images/7c272ae7c5bdf3ad69d53d2affa58465160cb6b3e7a5186a66a8586f83c6b03c.jpg)

Figure 2 shows the parameter space for a SFO-EWPT in the Higgs-Singlet model (top row) and in SMEFT (bottom row) for  $\kappa = 4$  (left plots) and  $\kappa = 2$  (right plots). The color coding gives the strength of the phase transition  $R_{N} = v_{N} / T_{N}$  as a function of scalar vev  $s_0$  and mass  $m_s$  for the UV theory, and as a function of cutoff scale  $\Lambda$  and strength of dimension 8 operator  $c_8$  in SMEFT. In the white area there is no first order phase transition. Comparing the top plots we see that for smaller Higgs-singlet coupling  $\kappa$  a SFO-EWPT requires a larger singlet vev. The  $3\sigma$  bound on the mixing angle in eq. (4.17) does not constrain the parameter space, but the stronger  $2\sigma$  bound — indicated by the hatched region in the plots — already cuts almost all parameter space with  $\kappa = 2$  for a strong phase transition with  $R_N > 1$ . In all of parameter space we find  $|A_1| / M \sim 1$  and the constraints eq. (4.13) are satisfied.

We have mapped the parameters of the UV theory to those in SMEFT and vice versa,  $(m_s, s_0) \leftrightarrow (\Lambda, c_8)$ , using eqs. (4.14) and (2.16). For example, the solid (dashed) green line corresponds to  $c_8 v^2 / \Lambda^2 = 0.5$  (0.3) in SMEFT, below which the EFT expansion (almost) does not converge in the electroweak vacuum eq. (2.17) and higher order operators are important for a consistent description. The top plots show the green lines mapped to the parameters of the Higgs-singlet model. Further, the red solid (dashed) lines correspond  $R_N = 1$  ( $R_N = 1.4$ ) in the UV model, and the black solid (dashed) lines to the SMEFT cutoff values of 600 (800)GeV. We have included the dimension 6 derivative operator proportional to  $c_{\mathrm{kin}}$  in the mapping; the magenta lines show the mapping of the equi- $R_N$  for  $c_{\mathrm{kin}} = 0$ . The difference between the red and magenta lines in the bottom plots is only appreciable in the region below the green lines where the EFT description fails. This a posteriori justifies setting  $c_{\mathrm{kin}} = 0$  in our analytical analysis when focusing on the parameter space of interest.

There are two important lessons to draw from the plots. First, the perturbative UV theory covers only part of parameter space for a SFO-EWPT in SMEFT, in particular the points with  $c_{8} \ll 1$  have no valid counterpart in the UV theory. Conversely, part of

the parameter space for a SFO-EWPT in the UV theory maps to a weak first order phase transition in SMEFT with  $R_{N} < 1$ . Second, truncating SMEFT at dimension 6, i.e. with  $c_{8} = 0$ , does not accurately reproduce the UV results, such as the strength of the first order phase transition in the SMEFT.

This last point can be better appreciated looking at figure 3, which shows the strength of the phase transition in SMEFT  $(R_{N})_{\mathrm{EFT}}$  vs. that in  $(R_{N})_{\mathrm{UV}}$  in the Higgs-singlet model for the points taken from the  $\kappa = 4$  scan in figure 2. In the left plot we have included all points with  $c_{8}v^{2}/\Lambda^{2} < 0.5$  for which the EFT expansion marginally converges. For perfect agreement between SMEFT and the UV theory all points should lie on the red line in the figure corresponding to  $(R_{N})_{\mathrm{EFT}} = (R_{N})_{\mathrm{UV}}$ . What we see instead is that the blue points for SMEFT with dimension 6 operators reproduce  $R_{N}$ -values significantly below that in the full theory. Including dimension 8 operators (orange points), and dimension 8 and dimension 6 derivative operators (green points) improves the matching somewhat. In the right plot we have only included the points  $c_{8}v^{2}/\Lambda^{2} < 0.3$  which have a much better EFT expansion. We see that SMEFT at dimension 6 is still a poor approximation, but the dimension 8 SMEFT gives a much better agreement. As the effect of dimension 10 operators is small for these points, we expect that the main error here comes from neglecting loop level matching effects and dimension 8 derivative operators.

We end this subsection by noting that our results partially agree with ref. [30], who also compared the predictions of the Higgs-singlet model and SMEFT truncated at dimension 6. They find that SMEFT can only give qualitative results for a SFO-EWPT, and only in an extremely limited region of parameter space; our results indicate a large overlap region, and also for smaller mixing angles. There are some differences in how we implemented our numerical analysis. First, we did not include thermal corrections from diagrams with a singlet loop, as for the large masses involved, these loops are Boltzmann suppressed. Second, we only considered a non-perturbative Higgs-singlet coupling  $\kappa < (4\pi)$ , which translates in an upper bound on the singlet mass for the parameter space of a SFO-EWPT. Third, we also included the effect of dimension 8 operators. And fourth, and this may be the main cause of the difference, they restrict all parameters with mass dimension to be smaller than  $M$ . However, in most of the SFO-EWPT parameter space for which the EFT-expansion is (marginally) valid — the region above the green lines in the plots of figure 2 — the ratio  $A^2 / M^2$  is slightly larger than one for (but comfortably smaller than the bounds eq. (4.13) we use).

# 4.3.2 Dark sector

For a dark sector Higgs-singlet type set-up the ratio of Higgs mass to Higgs vev can be smaller  $m_{h_D0}^2 / v_D^2 \ll 1$ , although for too small values eq. (2.19) the Higgs potential by itself, without the singlet, can already give a SFO-PT. The requirement for a valid EFT then becomes

$$
\frac {m _ {h _ {D} 0} ^ {2}}{2 v _ {D} ^ {2}} \sim \frac {3}{8} \frac {\kappa | A _ {1} | ^ {2} v _ {D} ^ {2}}{M ^ {4}} \ll \frac {3}{4} \frac {| A _ {1} | ^ {2}}{M ^ {2}} \tag {4.18}
$$

which allows for a larger separation of scales, that is for smaller values of  $v_{D}^{2} / M^{2}$  than in the SM, provided  $|A_1|^2 /M^2\ll 1$  is smaller as well. As discussed in section 2.5 the larger

the separation of scales the smaller the sensitivity to  $c_{8}$ . However, this is counterbalanced by the increased value of  $c_{8} \propto M^{2} / |A_{1}|^{2}$  (see eq. (4.16)) in this limit. We thus expect that dimension 8 operators will also be important for a dark sector EFT description of dark Higgs-singlet models.

# 4.4 Multifield UV theories

To end this section, we comment on extending the SM with multiple fields. Adding multiple singlets, one can always redefine the fields such that only one singlet direction obtains a vev. The tree-level matching results will then be the same as in the set-up with a single singlet discussed above. A UV theory with both singlets and extra Higgs doublets allows to tune parameters in the EFT theory, and maybe reduce the Wilson coefficient of the dimension 8 operator(s). Even if possible, this is in such a limited part of parameter space that it seems more useful to study the UV model itself than embark on an EFT analysis.

Loop contributions may be enhanced by large-  $N$  effects, with  $N$  the number of heavy fields, the most interesting case if the dimension 6 operators are enhanced the most (or the perturbativity constraint weakened). This is not the case in for example  $O(N)$ -scalar extensions with couplings  $\kappa |H|^2\sum_i s_i^2$ ; then all one-loop contributions simply pick up a factor  $N$  but no further hierarchy between dimension 6 and higher is obtained. It may be that in generic large  $N$  models, with all possible  $s_i - s_j$ -couplings allowed, the wanted enhancement of the dimension 6 operator is possible.

# 5 Conclusion

The nature of the electroweak phase transition is a key question that will be probed by next generation colliders and gravitational wave detectors. It is very attractive then to have a model-independent way of interpreting new results. UV theories that give rise to a strongly first order electroweak phase transition require new degrees of freedom that are relatively light, to obtain the necessary large corrections to the SM Higgs potential. As we have shown in this paper, the lack of a clear separation of scales invalidates the SMEFT description for these set-ups. Unfortunately, updating our knowledge of the electroweak phase diagram thus requires a separate detailed (numerical) study of each (class of) SM extension.

An exception to this are Higgs-singlet models, for which the SMEFT approach can be used to some extent. However, given that SMEFT can only cover part of the interesting parameter space for a first order phase transition, and that accurate agreement with the UV theory is only obtained if dimension 8 operators are included as well, the usefulness of this limited applicability of SMEFT is unclear. As these models have non-zero Higgs mixing angle, they will be further probed by colliders.

Finally, non-renormalizable dark sectors provide a computationally convenient framework to study gravitational wave production from a strongly first order phase transition. We have derived conditions for when the EFT approach is valid. The applicability to the study of gravitational waves is left for future work.

# Acknowledgments

MP thanks J. van de Vis for useful discussions. This work was supported by World Premier International Research Center Initiative (WPI), MEXT, Japan, and by the Netherlands Organization for Scientific Research (NWO).

# A Numerical scan

In this appendix we detail the input — the effective potential and parameter values — for our numerical calculation. To define the effective potential we follow [17, 43]. The numerical scans of the phase transition are done with the CosmoTransitions package [50].

# A.1 Higgs-singlet model

The one-loop effective potential at finite temperature is  $V_{\mathrm{eff}} = V_{\mathrm{tree}} + V_{\mathrm{CW}} + V_T$  with

$$
V _ {\mathrm {t r e e}} = \mu_ {0} ^ {2} | H | ^ {2} + \frac {1}{2} M ^ {2} s ^ {2} + \lambda_ {0} | H | ^ {4} + \frac {1}{4} \lambda_ {s} s ^ {4} + \frac {1}{2} \kappa | H | ^ {2} s ^ {2} - A _ {1} | H | ^ {2} s + \frac {1}{3} g _ {s} A _ {1} s ^ {3},
$$

$$
V _ {\mathrm {C W}} = \sum_ {i} \frac {n _ {i}}{(8 \pi) ^ {2}} \left[ m _ {i} ^ {4} \left(\ln \left(\frac {| m _ {i} ^ {2} |}{m _ {0 i} ^ {2}}\right) - \frac {3}{2}\right) + 2 m _ {i} ^ {2} m _ {0 i} ^ {2} \right],
$$

$$
V _ {T} = \sum_ {i = \operatorname {s c a l a r}, A ^ {\parallel}} n _ {i} T ^ {4} J _ {B} \left(\frac {m _ {T i} ^ {2}}{T ^ {2}}\right) + \sum_ {i = A ^ {\perp}} n _ {i} T ^ {4} J _ {B} \left(\frac {m _ {i} ^ {2}}{T ^ {2}}\right) + \sum_ {i = \text {f e r m i o n s}} n _ {j} T ^ {4} J _ {F} \left(\frac {m _ {i} ^ {2}}{T ^ {2}}\right). \tag {A.1}
$$

The thermal functions are given by [63]

$$
J _ {B / F} \left(y ^ {2}\right) = \frac {1}{2 \pi^ {2}} \int_ {0} ^ {\infty} \mathrm {d} x x ^ {2} \ln \left(1 - s \mathrm {e} ^ {- \sqrt {x ^ {2} + y ^ {2}}}\right) = - s \times \left\{ \begin{array}{l l} \left(\frac {y}{2 \pi}\right) ^ {3 / 2} \mathrm {e} ^ {- y}, & y \gg 1 \\ \frac {c _ {0} \pi^ {2}}{9 0} - \frac {c _ {2} y ^ {2}}{2 4} + \frac {c _ {3} y ^ {3}}{1 2 \pi} + \mathcal {O} \left(y ^ {4}\right), & y \ll 1 \end{array} \right. \tag {A.2}
$$

with for bosons  $\{s, c_0, c_2, c_3\} = \{1, 1, 1, 1\}$  and for fermions  $\{s, c_0, c_2, c_3\} = \{-1, 7/8, 1/2, 0\}$ .

We work in an on-shell renormalization scheme such that  $\partial_i V_{\mathrm{CW}}| = \partial_i\partial_j V_{\mathrm{CW}}|_{(v,s_0)} = 0$  with  $i = h, s$  — vanishes in the EW vacuum  $(h, s) = (v, s_0)$ . The  $n_i = \{1, 1, 3, 3, 6, -12\}$  gives the degrees of freedom for the Higgs, singlet, goldstones,  $Z$ ,  $W$  and top respectively, which together give the dominant one loop contributions. We take the absolute values of  $|m_i^2|$  in the log, to assure a real CW potential for negative masses (the Higgs/goldstone masses become negative for small Higgs field values); as argued in [17] the imaginary part of the CW potential is cancelled by an imaginary contribution from the thermal potential, assuring the full potential is real. The zero temperature masses entering  $V_{\mathrm{CW}}$  are

$$
m _ {W} ^ {2} = \frac {1}{4} g _ {2} ^ {2} h ^ {2}, \quad m _ {Z} ^ {2} = \frac {1}{4} \left(g _ {1} ^ {2} + g _ {2} ^ {2}\right) h ^ {2}, \quad m _ {t} = \frac {1}{2} y _ {t} ^ {2} h ^ {2}, \quad m _ {\chi} ^ {2} = \mu_ {0} ^ {2} + \lambda_ {0} h ^ {2} + \frac {1}{2} \kappa s ^ {2} - A _ {1} s + \epsilon_ {\chi}. \tag {A.3}
$$

We included  $\epsilon_{\chi} \ll 1$  to keep the log-term well defined in the electroweak vacuum for the Goldstone bosons (as then  $m_{0\chi}^2 = \epsilon_{\chi} \neq 0$ ). The Higgs and singlet mass eigenstates are

obtained by diagonalizing the mass matrix  $V_{ij}$

$$
m _ {h, s} ^ {2} = \frac {1}{2} \left(V _ {h h} + V _ {s s} \pm \sqrt {V _ {h h} ^ {2} - 2 V _ {h h} V _ {s s} + V _ {s s} ^ {2} + 4 V _ {h s} ^ {2}}\right), \tag {A.4}
$$

where we take the Higgs field to be the lightest mass eigenstate, ycorresponding to the minus sign solution above. The notation is that  $m_{i}^{2}$  are the higgs field dependent masses, and  $m_{0i}^{2} = m_{i}^{2}|_{(v,s_{0})}$  the masses in the EW vacuum. Explicitly

$$
V _ {h h} = - A _ {1} s + \frac {1}{2} \kappa s ^ {2} + 3 \lambda_ {0} h ^ {2} + \mu_ {0} ^ {2}, \quad V _ {s s} = \frac {1}{2} h ^ {2} \kappa + 3 \lambda_ {s} s ^ {2} + \mu_ {s} ^ {2} + 2 A _ {1} g _ {s} s, \quad V _ {h s} = h (\kappa s - A _ {1}) \tag {A.5}
$$

The mass eigenstates are  $h_1 = h\cos \theta +s\sin \theta$  and  $h_2 = -h\sin \theta +s\cos \theta$  with mixing angle

$$
\tan \theta = \frac {y}{1 + \sqrt {1 + y ^ {2}}},
$$

$$
y = \frac {2 V _ {h s}}{V _ {h h} - V _ {s s}} = \frac {2 h (\kappa s - A _ {1})}{- A _ {1} s + \frac {1}{2} \kappa s ^ {2} + 3 \lambda_ {0} h ^ {2} \mu_ {0} ^ {2} - \frac {1}{2} h ^ {2} \kappa - 3 \lambda_ {s} s ^ {2} - \mu_ {s} ^ {2} - 2 A _ {1} g _ {s} s} \tag {A.6}
$$

Since  $|\cos \theta| > 1 / \sqrt{2}$  the  $h_1$  mass eigenstate, with mass  $m_h$ , is the state with the largest  $h$ -component [64].

To include leading order infra red thermal corrections from the daisy diagrams we use the thermal masses  $m_{iT}^2$  (the leading term in the high-  $T$  expansion) in  $V_T$  for the scalars and longitudinal gauge bosons. At linear order in the high-  $T$  expansion this gives the same potential as adding the daisy diagrams separately [46]. As the singlet is heavy, its thermal loop contribution is Boltzmann suppressed and we leave it out from the thermal self-energies. For the transverse gauge d.o.f. and the fermions we can use the zero temperature mass, as these field do not generate daisy corrections.

The thermal self-energies for the scalars are then

$$
\Pi_ {h} = \Pi_ {\chi} = T ^ {2} \left(\frac {g _ {1} ^ {2}}{1 6} + \frac {3 g _ {2} ^ {2}}{1 6} + \frac {y _ {t} ^ {2}}{4} + \frac {\lambda_ {0}}{4}\right), \quad \Pi_ {s} = 0. \tag {A.7}
$$

Note that the singlet is heavy and does not contribute to the strong coupling of long wavelength modes, hence its thermal mass is set to zero. Then  $m_{T\chi}^2 = m_\chi^2 + \Pi_\chi$  and  $m_{Ti}^2$  for the singlet/higgs are the eigenvalues of  $V_{ab} + \mathrm{Diag}(\Pi_h, \Pi_s)$ . For the longitudinal gauge bosons

$$
m _ {T W _ {L}} ^ {2} = g _ {2} ^ {2} \left(\frac {1}{4} h ^ {2} + \frac {1 1}{6} T ^ {2}\right), \quad m _ {T Z _ {L}, \gamma_ {L}} ^ {2} = \text {e i g e n v a l u e s o f} \binom {g _ {2} ^ {2} \left(\frac {1}{4} h ^ {2} + \frac {1 1}{6} T ^ {2}\right)} {- \frac {g _ {1} g _ {2}}{4} h ^ {2}} \begin{array}{c} - \frac {g _ {1} g _ {2}}{4} h ^ {2} \\ g _ {1} ^ {2} \left(\frac {1}{4} h ^ {2} + \frac {1 1}{6} T ^ {2}\right) \end{array} \tag {A.8}
$$

where we also include the non-zero thermal photon mass.

We can exchange the parameters  $(\lambda_0, A_1, \mu_0^2, M^2)$  for the physical vacuum vevs and masses  $(v, s_0, m_{0h}^2, m_{0s}^2)$  using  $\partial_s V = \partial_h V|_{(v, s_0)} = 0$  and eq. (A.4). The explicit expressions are cumbersome, but straightforward to implement.

# A.2 EFT

The SMEFT potential is given in eq. (2.16). The parameters  $a_2, a_4$  are fixed by the vacuum conditions  $V_h|_v = 0$  and  $V_{hh}|_v = m_{0h}^2$  which gives

$$
a _ {2} = - \frac {1}{2} m _ {0 h} ^ {2} + \frac {v ^ {4}}{\Lambda^ {2}} + \frac {2 c _ {8} v ^ {6}}{\Lambda^ {4}}, \quad a _ {4} v ^ {2} = \frac {1}{2} m _ {0 h} ^ {2} - \frac {2 v ^ {4}}{\Lambda^ {2}} - \frac {3 c _ {8} v ^ {6}}{\Lambda^ {4}}. \tag {A.9}
$$

The Higgs and Goldstone masses are

$$
m _ {h} ^ {2} = a _ {2} + 3 a _ {4} h ^ {2} + \frac {5 h ^ {4}}{\Lambda^ {2}} + \frac {7 c _ {8} h ^ {6}}{\Lambda^ {4}}, \quad m _ {\chi} ^ {2} = a _ {2} + a _ {4} h ^ {2} + \frac {h ^ {4}}{\Lambda^ {2}} + \frac {c _ {8} h ^ {6}}{\Lambda^ {4}}. \tag {A.10}
$$

We include the corrections from the EFT operators to the Higgs/Goldstone self-energies which become

$$
\Pi_ {h / \chi} = T ^ {2} \left(\frac {g _ {1} ^ {2}}{1 6} + \frac {3 g _ {2} ^ {2}}{1 6} + \frac {y _ {t} ^ {2}}{4} + \frac {1}{2 4} \left(1 5 0 \frac {c 8 h ^ {4}}{\Lambda^ {4}} + 7 2 \frac {c 6 h ^ {2}}{\Lambda^ {2}} + 1 2 a _ {4}\right)\right). \tag {A.11}
$$

All other SM masses and thermal corrections are the same as in the singlet model (if we identify  $a_2 = \mu_0^2$ ,  $a_4 = \lambda_0$ ).

# A.3 Parameter values

$$
g _ {1} = 0. 3 7 7, \quad g _ {2} = 0. 6 5 3, \quad y _ {t} = 1, \quad v = 1 2 6 \mathrm {G e V}, \quad m _ {h} ^ {2} = 1 2 5. 7 \mathrm {G e V}. \tag {A.12}
$$

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] M.J. Ramsey-Musolf, The electroweak phase transition: a collider target, JHEP 09 (2020) 179 [arXiv:1912.07189] [INSPIRE].  
[2] A.V. Kotwal, M.J. Ramsey-Musolf, J.M. No and P. Winslow, Singlet-catalyzed electroweak phase transitions in the 100 TeV frontier, Phys. Rev. D 94 (2016) 035022 [arXiv:1605.06123] [INSPIRE].  
[3] T. Huang, J.M. No, L. Pernié, M. Ramsey-Musolf, A. Safonov, M. Spannowsky et al., Resonant di-Higgs boson production in the bbWW channel: Probing the electroweak phase transition at the LHC, Phys. Rev. D 96 (2017) 035007 [arXiv:1701.04442] [INSPIRE].  
[4] M. Benedikt, M. Capeans Garrido, F. Cerutti, B. Goddard, J. Gutleber, J.M. Jimenez et al., Future Circular Collider — European Strategy Update Documents, Tech. Rep. CERN-ACC-2019-0005, CERN, Geneva (2019).  
[5] A. Papaefstathiou and G. White, The Electro-Weak Phase Transition at Colliders: Confronting Theoretical Uncertainties and Complementary Channels, arXiv:2010.00597 [INSPIRE].  
[6] V.A. Kuzmin, V.A. Rubakov and M.E. Shaposhnikov, On the Anomalous Electroweak Baryon Number Nonconservation in the Early Universe, Phys. Lett. B 155 (1985) 36 [INSPIRE].

[7] M.E. Shaposhnikov, Possible Appearance of the Baryon Asymmetry of the Universe in an Electroweak Theory, JETP Lett. 44 (1986) 465 [INSPIRE].  
[8] M.E. Shaposhnikov, Baryon Asymmetry of the Universe in Standard Electroweak Theory, Nucl. Phys. B 287 (1987) 757 [INSPIRE].  
[9] A.G. Cohen, D.B. Kaplan and A.E. Nelson, Progress in electroweak baryogenesis, Ann. Rev. Nucl. Part. Sci. 43 (1993) 27 [hep-ph/9302210] [INSPIRE].  
[10] D.E. Morrissey and M.J. Ramsey-Musolf, Electroweak baryogenesis, New J. Phys. 14 (2012) 125003 [arXiv:1206.2942] [INSPIRE].  
[11] G.A. White, A Pedagogical Introduction to Electroweak Baryogenesis, IOP Publishing (2016), [DOI].  
[12] C. Caprini et al., Detecting gravitational waves from cosmological phase transitions with LISA: an update, JCAP 03 (2020) 024 [arXiv:1910.13125] [INSPIRE].  
[13] E.E. Jenkins, A.V. Manohar and M. Trott, Renormalization Group Evolution of the Standard Model Dimension Six Operators I: Formalism and lambda Dependence, JHEP 10 (2013) 087 [arXiv:1308.2627] [INSPIRE].  
[14] I. Brivio and M. Trot, The Standard Model as an Effective Field Theory, Phys. Rept. 793 (2019) 1 [arXiv:1706.08945] [INSPIRE].  
[15] C. Grojean, G. Servant and J.D. Wells, First-order electroweak phase transition in the standard model with a low cutoff, Phys. Rev. D 71 (2005) 036001 [hep-ph/0407019] [INSPIRE].  
[16] D. Bödeker, L. Fromme, S.J. Huber and M. Seniuch, The Baryon asymmetry in the standard model with a low cut-off, JHEP 02 (2005) 026 [hep-ph/0412366] [INSPIRE].  
[17] C. Delaunay, C. Grojean and J.D. Wells, Dynamics of Non-renormalizable Electroweak Symmetry Breaking, JHEP 04 (2008) 029 [arXiv:0711.2511] [INSPIRE].  
[18] C. Balázs, G. White and J. Yue, Effective field theory, electric dipole moments and electroweak baryogenesis, JHEP 03 (2017) 030 [arXiv:1612.01270] [INSPIRE].  
[19] J. de Vries, M. Postma, J. van de Vis and G. White, Electroweak Baryogenesis and the Standard Model Effective Field Theory, JHEP 01 (2018) 089 [arXiv:1710.04061] [INSPIRE].  
[20] J. De Vries, M. Postma and J. van de Vis, The role of leptons in electroweak baryogenesis, JHEP 04 (2019) 024 [arXiv:1811.11104] [INSPIRE].  
[21] M. Chala, C. Krause and G. Nardini, Signals of the electroweak phase transition at colliders and gravitational wave observatories, JHEP 07 (2018) 062 [arXiv:1802.02168] [INSPIRE].  
[22] S.A.R. Ellis, S. Ipek and G. White, Electroweak Baryogenesis from Temperature-Varying Couplings, JHEP 08 (2019) 002 [arXiv:1905.11994] [INSPIRE].  
[23] D. Croon, O. Gould, P. Schicho, T.V.I. Tenkanen and G. White, Theoretical uncertainties for cosmological first-order phase transitions, arXiv:2009.10080 [INSPIRE].  
[24] K. Kajantie, M. Laine, K. Rummukainen and M.E. Shaposhnikov, The Electroweak phase transition: A Nonperturbative analysis, Nucl. Phys. B 466 (1996) 189 [hep-lat/9510020] [INSPIRE].  
[25] K. Kajantie, M. Laine, K. Rummukainen and M.E. Shaposhnikov, Is there a hot electroweak phase transition at  $m(H)$  larger or equal to  $m(W)$ ?, Phys. Rev. Lett. 77 (1996) 2887 [hep-ph/9605288] [INSPIRE].

[26] K. Kajantie, M. Laine, K. Rummukainen and M.E. Shaposhnikov, A Nonperturbative analysis of the finite  $T$  phase transition in  $\mathrm{SU}(2) \times \mathrm{U}(1)$  electroweak theory, Nucl. Phys. B 493 (1997) 413 [hep-1at/9612006] [INSPIRE].  
[27] F. Csikor, Z. Fodor and J. Heitger, Endpoint of the hot electroweak phase transition, Phys. Rev. Lett. 82 (1999) 21 [hep-ph/9809291] [INSPIRE].  
[28] M. D'Onofrio and K. Rummukainen, Standard model cross-over on the lattice, Phys. Rev. D 93 (2016) 025003 [arXiv:1508.07161] [INSPIRE].  
[29] PARTICLE DATA GROUP collaboration, Review of Particle Physics, Phys. Rev. D 98 (2018) 030001 [INSPIRE].  
[30] P.H. Damgaard, A. Haarr, D. O'Connell and A. Tranberg, Effective Field Theory and Electroweak Baryogenesis in the Singlet-Extended Standard Model, JHEP 02 (2016) 107 [arXiv:1512.01963] [INSPIRE].  
[31] Q.-H. Cao, F.P. Huang, K.-P. Xie and X. Zhang, Testing the electroweak phase transition in scalar extension models at lepton colliders, Chin. Phys. C 42 (2018) 023103 [arXiv:1708.04737] [INSPIRE].  
[32] V.Q. Phong, P.H. Khiem, N.P.D. Loc and H.N. Long, Sphaleron in the first-order electroweak phase transition with the dimension-six Higgs field operator, Phys. Rev. D 101 (2020) 116010 [arXiv:2003.09625] [INSPIRE].  
[33] I. Baldes, Gravitational waves from the asymmetric-dark-matter generating phase transition, JCAP 05 (2017) 028 [arXiv:1702.02117] [INSPIRE].  
[34] D. Croon, V. Sanz and G. White, Model Discrimination in Gravitational Wave spectra from Dark Phase Transitions, JHEP 08 (2018) 203 [arXiv:1806.02332] [INSPIRE].  
[35] D. Croon, A. Kusenko, A. Mazumdar and G. White, Solitosynthesis and Gravitational Waves, Phys. Rev. D 101 (2020) 085010 [arXiv:1910.09562] [INSPIRE].  
[36] B. Grzadkowski, M. Iskrzynski, M. Misiak and J. Rosiek, Dimension-Six Terms in the Standard Model Lagrangian, JHEP 10 (2010) 085 [arXiv:1008.4884] [INSPIRE].  
[37] S.R. Coleman and E.J. Weinberg, Radiative Corrections as the Origin of Spontaneous Symmetry Breaking, Phys. Rev. D 7 (1973) 1888 [INSPIRE].  
[38] R. Jackiw, Functional evaluation of the effective potential, Phys. Rev. D 9 (1974) 1686 [INSPIRE].  
[39] H.H. Patel and M.J. Ramsey-Musolf, Baryon Washout, Electroweak Phase Transition, and Perturbation Theory, JHEP 07 (2011) 029 [arXiv:1101.4665] [INSPIRE].  
[40] J.M. Frere and P. Nicoletopoulos, Gauge Invariant Content of the Effective Potential, Phys. Rev. D 11 (1975) 2332 [INSPIRE].  
[41] M. Sher, The Renormalization Group and Inflationary Potentials, Phys. Lett. B 135 (1984) 52 [INSPIRE].  
[42] J.R. Espinosa, G.F. Giudice, E. Morgante, A. Riotto, L. Senatore, A. Strumia et al., The cosmological Higgs story of the vacuum instability, JHEP 09 (2015) 174 [arXiv:1505.04825] [INSPIRE].  
[43] D. Curtin, P. Meade and C.-T. Yu, Testing Electroweak Baryogenesis with Future Colliders, JHEP 11 (2014) 127 [arXiv:1409.0005] [INSPIRE].

[44] L. Dolan and R. Jackiw, Symmetry Behavior at Finite Temperature, Phys. Rev. D 9 (1974) 3320 [INSPIRE].  
[45] M.E. Carrington, The Effective potential at finite temperature in the Standard Model, Phys. Rev. D 45 (1992) 2933 [INSPIRE].  
[46] P.B. Arnold and O. Espinosa, The Effective potential and first order phase transitions: Beyond leading-order, Phys. Rev. D 47 (1993) 3546 [Erratum ibid. 50 (1994) 6662] [hep-ph/9212235] [INSPIRE].  
[47] J.M. Cline, Baryogenesis, in Les Houches Summer School - Session 86: Particle Physics and Cosmology: The Fabric of Spacetime, (2006) [hep-ph/0609145] [INSPIRE].  
[48] A.D. Linde, Decay of the False Vacuum at Finite Temperature, Nucl. Phys. B 216 (1983) 421 [Erratum ibid. 223 (1983) 544] [INSPIRE].  
[49] S. Baum, M. Carena, N.R. Shah, C.E.M. Wagner and Y. Wang, *Nucleation is More than Critical - A Case Study of the Electroweak Phase Transition in the NMSSM*, arXiv:2009.10743 [INSPIRE].  
[50] C.L. Wainwright, Cosmo Transitions: Computing Cosmological Phase Transition Temperatures and Bubble Profiles with Multiple Fields, Comput. Phys. Commun. 183 (2012) 2006 [arXiv:1109.4189] [INSPIRE].  
[51] M.K. Gaillard, The Effective One Loop Lagrangian With Derivative Couplings, Nucl. Phys. B 268 (1986) 669 [INSPIRE].  
[52] O. Cheyette, Effective Action for the Standard Model With Large Higgs Mass, Nucl. Phys. B 297 (1988) 183 [INSPIRE].  
[53] F. del Aguila, Z. Kunszt and J. Santiago, One-loop effective lagrangians after matching, Eur. Phys. J. C 76 (2016) 244 [arXiv:1602.00126] [INSPIRE].  
[54] B. Henning, X. Lu and H. Murayama, How to use the Standard Model effective field theory, JHEP 01 (2016) 023 [arXiv:1412.1837] [INSPIRE].  
[55] A. Drozd, J. Ellis, J. Quevillon and T. You, The Universal One-Loop Effective Action, JHEP 03 (2016) 180 [arXiv:1512.03003] [INSPIRE].  
[56] B. Henning, X. Lu and H. Murayama, One-loop Matching and Running with Covariant Derivative Expansion, JHEP 01 (2018) 123 [arXiv:1604.01019] [INSPIRE].  
[57] S.A.R. Ellis, J. Quevillon, T. You and Z. Zhang, Extending the Universal One-Loop Effective Action: Heavy-Light Coefficients, JHEP 08 (2017) 054 [arXiv:1706.07765] [INSPIRE].  
[58] J. Fuentes-Martin, J. Portoles and P. Ruiz-Femenia, Integrating out heavy particles with functional methods: a simplified framework, JHEP 09 (2016) 156 [arXiv:1607.02142] [INSPIRE].  
[59] P.D. Group, P.A. Zyla, R.M. Barnett, J. Beringer, O. Dahl. D.A. Dwyer et al., Review of Particle Physics, PTEP 2020 (2020) 8 [https://academic.oup.com/ptep/article-pdf/2020/8/083C01/33653179/ptaa104.pdf].  
[60] T.D. Lee, A Theory of Spontaneous  $T$  Violation, Phys. Rev. D 8 (1973) 1226 [INSPIRE].  
[61] J.F. Gunion, H.E. Haber, G.L. Kane and S. Dawson, The Higgs Hunter's Guide, Perseus (2000).

[62] G.C. Branco, P.M. Ferreira, L. Lavoura, M.N. Rebelo, M. Sher and J.P. Silva, Theory and phenomenology of two-Higgs-doublet models, Phys. Rept. 516 (2012) 1 [arXiv:1106.0034] [INSPIRE].  
[63] M. Laine and A. Vuorinen, *Basics of Thermal Field Theory* **925** Springer (2016), [DOI] [arXiv:1701.01554] [INSPIRE].  
[64] S. Profumo, M.J. Ramsey-Musolf and G. Shaughnessy, Singlet Higgs phenomenology and the electroweak phase transition, JHEP 08 (2007) 010 [arXiv:0705.2425] [INSPIRE].