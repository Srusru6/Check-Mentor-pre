RECEIVED: February 14, 2018

REVISED: June 18, 2018

ACCEPTED: June 27, 2018

PUBLISHED: July 9, 2018

# Signals of the electroweak phase transition at colliders and gravitational wave observatories

Mikael Chala, $^{a}$  Claudius Krause $^{b,c}$  and Germano Nardini $^{d,e}$

$^{a}$ Institute of Particle Physics Phenomenology, Physics Department, Durham University, South Road, Durham, DH1 3LE, U.K.  
bIFIC, Universitat de Valencia-CSIC, Apt. Correus 22085, E-46071 Valencia, Spain  
$^{c}$ Theoretical Physics Department, Fermi National Accelerator Laboratory, P.O. Box 500, Batavia, IL 60510, U.S.A.  
d Albert Einstein Center, Institute for Theoretical Physics, University of Bern, Sidlerstrasse 5, CH-3012 Bern, Switzerland  
$^{e}$  Faculty of Science and Technology, University of Stavanger, N-4036 Stavanger, Norway

E-mail: mikael.chala@durham.ac.uk, ckrause@fnal.gov, nardini@itp.unibe.ch

ABSTRACT: If the electroweak phase transition (EWPT) is of strongly first order due to higher dimensional operators, the scale of new physics generating them is at the TeV scale or below. In this case the effective-field theory (EFT) neglecting operators of dimension higher than six may overlook terms that are relevant for the EWPT analysis. In this article we study the EWPT in the EFT to dimension eight. We estimate the reach of the future gravitational wave observatory LISA for probing the region in which the EWPT is strongly first order and compare it with the capabilities of the Higgs measurements via double-Higgs production at current and future colliders. We also match different UV models to the previously mentioned dimension-eight EFT and demonstrate that, from the top-down point of view, the double-Higgs production is not the best signal to explore these scenarios.

KEYWORDS: Beyond Standard Model, Higgs Physics

ARXIV EPRINT: 1802.02168

# Contents

1 Introduction 1  
2 The electroweak phase transition in the EFT to dimension eight 2

2.1 Finite temperature potential 3  
2.2 Mean-field estimates 4  
2.3 Numerical procedure 6  
2.4 Interplay between gravitational wave signatures and Higgs-self coupling measurements 9

3 Matching of concrete models 10

3.1 New scalars with weak isospin  $I\leq 1$  12  
3.2 New scalars with weak isospin  $I > 1$  13

3.2.1 A custodial quadruplet setup 14  
3.3 Strongly-coupled models 17  
4 Conclusions 21

# 1 Introduction

We accurately measured the Higgs mass and its couplings to the heavy SM fermions and gauge bosons [1], but the ElecroWeak (EW) sector remains very uncertain. Within the current constraints, there is still room for a vast variety of phenomena that exhibit intriguing signatures. One of them is the possibility that the Higgs field produces gravitational waves when it acquires a Vacuum Expectation Value (VEV) [2-4]. For this to happen, the EW Symmetry Breaking (EWSB) must proceed via a Strong First Order EW Phase Transition (SFOEWPT). This is only possible if physics beyond the Standard Model (SM) exists, as such a transition requires the finite-temperature Higgs potential to behave radically differently from the one of the SM [5-8].<sup>1</sup>

Numerous extensions of the SM exhibiting a SFOEWPT have been considered in the literature. In most of the cases, the main ingredient to depart from the SM finite-temperature Higgs potential is to invoke new light particles in the thermal plasma coupled to the Higgs [21, 22]. In general, making these new light fields naturally compatible with the present LHC constraints requires to rely on either extra symmetries or particular parameter regions. The strategies to test these scenarios are therefore very model dependent. However, new light particles are not a necessary ingredient to achieve a SFOEWPT.

Higher-dimensional operators, obtained by integrating out heavy fields, can also provide large non-SM contributions to the Higgs potential. In this case, the lack of observation of additional particles would not be ascribed to circumstantial conditions, but simply to a considerable gap between the EW scale and the new physics scale,  $f$ .

At the EW scale, the theory with  $\mathcal{O}(f)$ -mass fields can be described by an effective Lagrangian containing the SM interactions as well as a tower of effective operators suppressed by powers of  $1/f$ . Among these operators, the interactions  $\mathcal{O}_n = (\phi^\dagger \phi)^{\frac{n}{2}}$  have a radical impact on the Higgs potential (here  $\phi$  is the Higgs EW doublet and  $n$  an even integer larger than four). Refs. [23-29] studied in detail the dynamics of the EWPT in the presence of only  $\mathcal{O}_6$ . They showed that, in order for the EWSB to proceed via a SFOEWPT, the new physics scale must be  $f \lesssim 600\mathrm{GeV}$  if its couplings are of order one. The small gap between the EW scale  $v \sim 246\mathrm{GeV}$  and the required  $f$  carries two major implications. (i) It points out that the EFT to dimension six is inaccurate. Any observable related to the EWPT receives corrections of order  $\sim v^2 / f^2 \gtrsim 20\%$ . The next tower of effective interactions, namely  $\mathcal{O}_8$ , must be included. (ii) It triggers the question of which new physics, at a scale of few hundreds GeV can produce such large modifications of the Higgs potential without being constrained by other Higgs measurements or direct LHC searches. We address these two points in this paper.

Thus, in section 2, we present the analysis of the EWPT in this extended EFT. We investigate the validity of the mean-field approximation. Moreover, we accurately determine the regions of the parameter space leading to the SFOEWPT, and characterize the consequent gravitational wave spectrum. We also identify the precise values of the coefficients of  $\mathcal{O}_6$  and  $\mathcal{O}_8$  that the future gravitational wave observatory LISA can test. Finally, we compare this region with the one that can be tested at colliders, sensitive to  $\mathcal{O}_6$  and  $\mathcal{O}_8$  via the Higgs self coupling measurements.

Next, in section 3, we discuss those models that can be matched to the EFT above without conflicting with current data. Among the most natural candidates, we single out a weakly-coupled custodial quadruplet extension. We study its phenomenology and find that at the LHC the most promising search for such an extension is to look for multi-lepton signals. Section 4 is devoted to our conclusions.

# 2 The electroweak phase transition in the EFT to dimension eight

Let us consider the SM extended with the effective operators  $\mathcal{O}_6$  and  $\mathcal{O}_8$ , the relevant Lagrangian being

$$
L = L _ {\mathrm {S M}} + \frac {c _ {6}}{f ^ {2}} (\phi^ {\dagger} \phi) ^ {3} + \frac {c _ {8}}{f ^ {4}} (\phi^ {\dagger} \phi) ^ {4}, \tag {2.1}
$$

where  $L_{\mathrm{SM}}$  is the SM Lagrangian,  $\phi$  is the Higgs doublet and  $f$  stands for the scale of new physics. In this section we determine the VEV of the Higgs at the critical and nucleation temperatures,  $v_{T_c}$  and  $v_{T_n}$ , the latent heat of the phase transition,  $\alpha$ , and the inverse duration time of the phase transition,  $\beta / H$ , in this non-minimal EFT. The results we obtain extend those previously obtained in the literature (see e.g. refs. [24, 26]), where only  $\mathcal{O}_6$  has been considered (despite the low cutoff and the consequent potential breaking of the EFT approach).

# 2.1 Finite temperature potential

The first ingredient we need is the Coleman-Weinberg effective potential at finite temperature; see ref. [21] for a review. In the Landau gauge and in the  $\overline{MS}$  renormalization scheme, the one-loop effective potential  $V_{1\ell}$  of our EFT scenario can be expressed as

$$
V _ {1 \ell} = V _ {\text {t r e e}} + \Delta V _ {1 \ell}, \tag {2.2}
$$

with

$$
V _ {\text {t r e e}} = - \frac {\mu^ {2}}{2} h _ {c} ^ {2} + \frac {\lambda}{4} h _ {c} ^ {4} + \frac {c _ {6}}{8 f ^ {2}} h _ {c} ^ {6} + \frac {c _ {8}}{1 6 f ^ {4}} h _ {c} ^ {8}, \tag {2.3}
$$

$$
\Delta V _ {1 \ell} = \Delta V _ {1 \ell , T = 0} + V _ {1 \ell , T \neq 0}, \tag {2.4}
$$

$$
\Delta V _ {1 \ell , T = 0} = \sum_ {i = h, \chi , W, Z, t} \frac {n _ {i} m _ {i} ^ {2} \left(h _ {c}\right)}{6 4 \pi^ {2}} \left(\log \frac {m _ {i} ^ {4} \left(h _ {c}\right)}{v ^ {2}} - C _ {i}\right), \tag {2.5}
$$

$$
V _ {1 \ell , T \neq 0} = \frac {n _ {t} T ^ {4}}{2 \pi^ {2}} J _ {f} \left(m _ {t} ^ {2} \left(h _ {c}\right) / T ^ {2}\right) + \sum_ {i = h, \chi , W, Z} \frac {n _ {i} T ^ {4}}{2 \pi^ {2}} J _ {b} \left(m _ {i} ^ {2} \left(h _ {c}\right) / T ^ {2}\right), \tag {2.6}
$$

where  $\Delta V_{1\ell, T=0}$  is the temperature-independent one-loop contribution and  $V_{1\ell, T \neq 0}$  is the (one-loop) remaining part. The variable  $h_c$  is a constant background field of the Higgs. In eq. (2.5),  $n_i$  are the degrees of freedom  $n_W = 2n_Z = 2n_\chi = 6n_h = -n_t / 2 = 6$ , while  $C_i$  is equal to  $5/6$  for gauge bosons and  $3/2$  for scalars and fermions. The  $h_c$ -dependent squared masses  $m_i^2$  are

$$
m _ {h} ^ {2} \left(h _ {c}\right) = - \mu^ {2} + 3 \lambda h _ {c} ^ {2} + \frac {1 5 c _ {6}}{4 f ^ {2}} h _ {c} ^ {4} + \frac {7 c _ {8}}{2 f ^ {4}} h _ {c} ^ {6}, \tag {2.7}
$$

$$
m _ {\chi} ^ {2} \left(h _ {c}\right) = - \mu^ {2} + \lambda h _ {c} ^ {2} + \frac {3 c _ {6}}{4 f ^ {2}} h _ {c} ^ {4} + \frac {c _ {8}}{2 f ^ {4}} h _ {c} ^ {6}, \tag {2.8}
$$

$$
m _ {t} ^ {2} (h _ {c}) = \frac {y _ {t} ^ {2}}{2} h _ {c} ^ {2}, \quad m _ {W} ^ {2} (h _ {c}) = \frac {g ^ {2}}{4} h _ {c} ^ {2}, \quad m _ {Z} ^ {2} (h _ {c}) = \frac {g ^ {2} + g ^ {\prime 2}}{4} h _ {c} ^ {2}. \tag {2.9}
$$

The explicit expression of the functions  $J_{b}$  and  $J_{f}$ , with or without the hard thermal loop resummation, can be found e.g. in refs. [21, 30].

Since our main results turn out to be quite insensitive to details, we can set the Yukawa,  $\mathrm{SU}(2)_L$  and  $\mathrm{U}(1)_Y$  gauge couplings at tree level by fixing  $m_t(v)$ ,  $m_W(v)$  and  $m_Z(v)$  in eq. (2.9) at 172, 80 and  $91\mathrm{GeV}$ , respectively. For the mean-field estimates, in which zero-temperature one-loop corrections are neglected, we moreover constrain  $\mu^2$  at tree level by requiring  $V_{\mathrm{tree}}$  to have a minimum at  $h_c = v$ :

$$
\mu^ {2} = \lambda v ^ {2} + \frac {3 c _ {6}}{4 f ^ {2}} v ^ {4} + \frac {c _ {8}}{2 f ^ {4}} v ^ {6}. \tag {2.10}
$$

Similarly, to set  $\lambda$ , we require  $\partial^2 V(\phi_c) / \partial h_c^2|_{h_c = v} = (125\mathrm{GeV})^2$ , which implies

$$
\lambda = - \frac {3 c _ {6}}{2 f ^ {2}} v ^ {2} - \frac {3 c _ {8}}{2 f ^ {4}} v ^ {4} + \frac {m _ {h} ^ {2}}{2 v ^ {2}}. \tag {2.11}
$$

The remaining free parameters in  $V_{1\ell}$  are therefore  $c_6 / f^2$  and  $c_8 / f^4$ .

![](images/e87695fb5ac2ce4b92f02084b5d9e8e4b1321c403a4d24524a18850feffaaa23.jpg)  
Figure 1. The potentials  $V_{\mathrm{tree}}$  (black solid curve),  $V_{1\ell}$  at  $T = 0$  (orange dashed curve) and  $V_{1\ell}$  at  $T = T_x$  (green dashed curve) for the choices of  $c_6 / f^2$  and  $c_8 / f^4$  indicated in each panel. In the left panel, there exist two vacua already at zero temperature ( $\mu^2 \simeq -3100GeV^2$ ,  $\lambda \simeq -0.23$ ,  $T_x = T_c = 35GeV$ ). In the central panel, the existence of two vacua arises only at finite temperature ( $\mu^2 = 1900GeV^2$ ,  $\lambda = -0.06$ ,  $T_x = T_c = 82GeV$ ). In the right panel, the potential is unbounded from below, but the instability scale is above the cutoff  $f = 1$  TeV ( $\mu^2 = 3000GeV^2$ ,  $\lambda = -0.03$ ,  $T_x = T_n = 99GeV$ ).  $T_c$  is the critical temperature obtained in the mean-field approximation.

![](images/b0b0df19f08c6901513431bb97e0dda67fcedf8b48e360f80f5ef00469a72936.jpg)

![](images/19fcb493117ae46ea3ec3088770bd307bb4b2baa7a24116a20ebd7f9f67f0cf0.jpg)

Notice that the EFT is a valid description of the theory only at energy scales much below  $f$ , therefore we do not address questions of the stability of the potential. Thus, we do not exclude a priori all values of  $c_{8}$  and  $c_{6}$  leading to  $V_{1\ell}$  unbounded from below; we only require

$$
V _ {\text {t r e e}} (v) <   V _ {\text {t r e e}} \left(h _ {c}\right) \quad \text {f o r a n y} h _ {c} \in ] v, f ]. \tag {2.12}
$$

This in practice corresponds to imposing a lower bound on  $c_8$  that varies with  $f$ . Such constraint is  $c_8 \gtrsim -9$  for  $f = 1 \mathrm{TeV}$  and  $c_8 \gtrsim -2$  for  $f = 2 \mathrm{TeV}$ . For concreteness, we limit the plots hereafter to the first bound.

Figure 1 shows the typical classes of potentials that we consider: cases where the potential has a tree level barrier between the minima (left panel), cases where such a barrier is only due to a finite temperature (one-loop) effect (central panel), and cases where the potential is unbounded from below but the instability arises at a scale larger than  $f$  (right panel). See ref. [31] for phenomenological discussions of new physics models in each class.

# 2.2 Mean-field estimates

From  $V_{1\ell}$  it is straightforward to determine some quantities that roughly characterise the EWPT, namely  $T_{c}$  and  $v_{T_c} / T_c$ . The critical temperature,  $T_{c}$ , is the temperature at which the minima of the broken and unbroken phases are degenerate. It provides the upper bound on the temperature at which the EWPT really starts,  $T_{n}$ . The quantity  $v_{T_c} / T_c$ , with  $v_{T_c}$  being the VEV of the Higgs in the EW broken phase at  $T = T_{c}$ , is linked to the strength of the EWPT. Indeed, due to the fact that  $v_{T} / T$  typically decreases with increasing  $T$ ,  $v_{T_c} / T_c$  can be used as a lower bound on the actual value of  $v_{T} / T$  during the EWPT (if the transition ever happens; see below).

The potential  $V_{1\ell}$  is easy to treat numerically, but for analytic insights on  $T_{c}$  and  $v_{T_c} / T_c$ , the mean-field approximation may be helpful. We then begin neglecting  $\Delta_{1\ell ,T = 0}V(h_c)$ . In  $\Delta_{1\ell ,T\neq 0}V(h_c)$ , we consider the high-temperature expansion of  $J_{b}$  and  $J_{f}$  and retain their

![](images/9232ba56c40cc20d3c1872ad8efa0463fa37d65731f206229f3d95670607e568.jpg)  
Figure 2.  $c_6 / f^2 - c_8 / f^4$  of parameter space for a SFOEWPT in the mean-field approximation. Left) The filled region shows the allowed values for  $c_6$  and  $c_8$  such that at  $T = 0$  the deepest minimum is at  $v$ . In the darker areas there is a second minimum above the one at  $v$ . For negative  $c_8$ , we cut off the potential at  $1\mathrm{TeV}$  and demand that  $V(1\mathrm{TeV}) > V(v)$  to ensure that the global minimum is at  $v$ . Superimposed are shades of yellow to green to show the strength of the phase transition,  $v_{T_c} / T_c$ , based on the critical temperature. Right) Zoomed version on the black rectangle of the left panel (note the different axis ranges). Lines of constant  $T_c$  are depicted.

![](images/3103ffce95c60380be6f7efc86ce79a44722d4eb3f8179fdc5f1b7f97f89c046.jpg)

leading terms, i.e.  $J_{b}(x) \to \pi^{2}x / 12$  and  $J_{f}(x) \to -\pi^{2}x / 24$  in eq. (2.6). The potential  $V_{1\ell}$  now reduces to the form

$$
V _ {\mathrm {m e a n}} (\phi , T) = \frac {- \mu^ {2} + a _ {T} T ^ {2}}{2} h _ {c} ^ {2} + \frac {\lambda}{4} h _ {c} ^ {4} + \frac {c _ {6}}{8 f ^ {2}} h _ {c} ^ {6} + \frac {c _ {8}}{1 6 f ^ {4}} h _ {c} ^ {8}, \tag {2.13}
$$

with  $a_{T} = \frac{1}{16}\left(4\frac{m_{h}^{2}}{v^{2}} + 3g^{2} + g^{\prime 2} + 4y_{t}^{2} - 12c_{6}\frac{v^{2}}{f^{2}} - 12c_{8}\frac{v^{4}}{f^{4}}\right)$ .

In eq. (2.13) the thermal contribution can only raise the potential at  $h_c \neq 0$ . No transition from the symmetric to the broken phase is conceivable if at zero temperature the EW breaking minimum is above the symmetric one. Hence, the condition  $V_{\mathrm{mean}}(v,T = 0) < V_{\mathrm{mean}}(0,T = 0)$  has to be satisfied, which is equivalent to

$$
\frac {c _ {6}}{f ^ {2}} <   \frac {m _ {h} ^ {2}}{v ^ {4}} - \frac {3 v ^ {2}}{2} \frac {c _ {8}}{f ^ {4}}. \tag {2.14}
$$

Saturating the inequality is not feasible. As previously mentioned, there must be a gap between  $T_{c}$  and  $T_{n}$ , and the stronger the phase transition is the larger is the gap. For this reason, values of  $c_{6} / f^{2}$  close to the upper bound in eq. (2.14) are not acceptable since they lead to  $T_{c} \to 0$  and  $v_{T_c} / T_c \to \infty$ . In this limit the EWPT would never happen within the lifetime of the Universe. Such values of  $c_{6} / f^{2}$  are thus expected to be ruled out by more sophisticated estimates; see section 2.3. For the same reason, it is at large  $c_{6} / f^{2}$  that, whenever the EWPT can really start, the parameter scenarios with the strongest EWPTs arise. To appreciate the relevance of this effect, let us first evaluate the EWPT disregarding the issue.

We fix the values of  $\mu$  and  $\lambda$  as in eqs. (2.10) and (2.11), and we require  $c_{6}$  and  $c_{8}$  to fulfil eq. (2.12). Moreover, by definition, at  $T = T_{c}$  the EWSB minimum is degenerate

with the symmetric one. These properties lead to the following relations for  $v_{T_c}$  and  $T_c$ :

$$
v _ {T _ {c}} ^ {2} = \left[ - \frac {2 c _ {6}}{3 c _ {8}} \pm 2 \sqrt {\frac {c _ {6} ^ {2}}{9 c _ {8} ^ {2}} - \frac {\lambda}{3 c _ {8}}} \right] f ^ {2}, \tag {2.15}
$$

$$
T _ {c} ^ {2} = \frac {\mu^ {2}}{a _ {0}} - \left[ \frac {2 c _ {6} ^ {3}}{2 7 c _ {8} ^ {2}} - \frac {c _ {6} \lambda}{3 c _ {8}} \mp 2 \sqrt {\left(\frac {c _ {6} ^ {2}}{9 c _ {8}} - \frac {\lambda}{3}\right) ^ {3} \frac {1}{c _ {8}}} \right] \frac {f ^ {2}}{a _ {0}},
$$

The left panel of figure 2 summarises our mean-field-approximation results in the plane  $c_{6} / f^{2} - c_{8} / f^{4}$ . To the right of the whole shaded area, eq. (2.14) is violated. Therefore, along the right border,  $T_{c} = 0$  and  $v_{T_c} / T_c = \infty$ . On the left of it, the above conditions for a first order EWPT are not satisfied. Below it, instead, eq. (2.12) is not satisfied for  $f = 1\mathrm{TeV}$ . (As previously explained, this border would move up or down by assuming different values of  $f$ .) The yellow and green regions mark the values of  $c_{6} / f^{2}$  and  $c_{8} / f^{2}$  leading to  $0.7 < v_{T_c} / T_c < 1.3$  and  $v_{T_c} / T_c > 1.3$ , respectively. These regions are split into a darker and a lighter areas. For  $c_{8} / f^{2} < 0$  the former shows where  $V_{\mathrm{tree}}$  is unbounded from below but the instability is above the cutoff (cf. right panel in figure 1); in the latter,  $V_{\mathrm{tree}}$  does not provide any sign of instability below the cutoff (cf. left and central panels in figure 1). The same split is applied to the grey region where the EWPT is not strong. In the dark grey area with  $c_{8} / f^{2} > 0$ , besides the global minimum at  $h_c = v$ ,  $V_{\mathrm{tree}}$  presents a further minimum at  $h_c \in ]v, f[$ . (For phenomenological implications of the latter see e.g. ref. [32].) We do not further discuss this peculiar configuration since it does not appear in the region with a SFOEWT. The right panel of figure 2 shows a zoom of the rectangle in the plot in the left panel. It also reports some contour curves for  $T_{c}$ .

# 2.3 Numerical procedure

The quantity  $v_{T_c} / T_c$  is a good estimate of the strength of the EWPT only when the gap between  $T_{c}$  and  $T_{n}$  is small. Quantitatively,  $T_{n}$  is defined as the temperature at which the probability for the nucleation of one single bubble (containing the broken phase) in a horizon volume is approximately  $\sim 1$ . For our scenario, the nucleation temperature can be considered in practice as the temperature  $T_{n}$  such that  $S_{3}[V_{1\ell}(h_{c},T_{n})]\simeq 140T_{n}$ , with  $S_{3}$  the action of the thermal decay from the false to the true vacuum of  $V_{1\ell}$  [21, 30].<sup>2</sup> Analytically,  $S_{3}$  can be calculated in the limit of thin or thick wall bubbles [21], but in general we do not expect our bubble profiles to precisely fulfil any of these two limits. We thus determine  $S_{3}$  numerically. For this scope, we use the code CosmoTransition [33] in which, to be more accurate, we do not implement the potential in the mean-field approximation but as in eq. (2.2) with the hard-thermal loop resummations in  $J_{b}$  and  $J_{f}$  included.<sup>3</sup> For this second and more precise study of the EWPT, for each value of  $c_6 / f^2$  and  $c_8 / f^4$  we determine numerically the values of  $\mu$  and  $\lambda$  for which  $h_c = v$  and  $m_h\sim 125\mathrm{GeV}$ .

The findings for  $T_{n}$  and  $v_{T_n} / T_n$  are respectively displayed in the top left and top right panels of figure 3 (dotted lines). As expected, for values of  $c_{6} / f^{2}$  nearby its upper limit (right border of the gray area; cf. eq. (2.14)),  $S_{3}[V_{1\ell}(h_{c},T)] / T$  is larger than 140 for any  $T$ ,

![](images/02a814b9e63114e3f4833d2d3f5b614cf1f1d1bd64c23347bf87cdcfe48f4b97.jpg)

![](images/cff5f8efb7592f3b29ec14313bedfd8cb3f58022eee226efadf5bcfe147d5318.jpg)

![](images/46c91cf9cc89107c0e0b1574ddeada8f99ead0408d63d935610cf448e07f31f7.jpg)  
Figure 3. Values of  $T_{n}$  (top left),  $v_{T_n} / T_n$  (top right),  $\alpha$  (bottom left) and  $\beta / H$  (bottom right) characterising the SFOEWPT in the plane  $c_6 / f^2 - c_8 / f^4$ . The labels of  $T_{n}$  and  $T_{c}$  are in GeV units. On the right of the grey area the condition in eq. (2.14) is violated. In the gray area to the right of the dashed line, the lifetime of the EW symmetric vacuum is longer that the age of the Universe, whereas on the left the transition results too weak for our purposes, i.e.  $v_{T_n} / T_n < 0.7$ . Below the grey area, the EW vacuum at zero temperature is not the global minimum at scales below the cutoff  $f = 1$  TeV. In orange the parameter region LISA is sensitive to.

![](images/fc9fa248ac3377588e9799172b08e991652cf5e50043b38aae0cd501b1d2dc0e.jpg)

meaning that the EWPT never starts. This problem is avoided when  $2c_{6} / f^{2} + 3v^{2}c_{8} / f^{4}$  goes below the threshold of about 3.5 (black, thick dashed line). Conceptually, at the threshold one obtains  $T_{n} = 0$  and  $v_{T_n} / T_n = \infty$ . The strongest EWPTs and largest supercoolings (namely, the gaps between  $T_{n}$  and  $T_{c}$ ) are thus achieved just below this threshold. By departing from it (i.e. by reducing  $c_{6} / f^{2}$  at fixed  $c_{8} / f^{4}$ ), the supercooling is reduced and, in turn,  $v_{T_n} / T_n$  drops down. At some point, at about  $c_{6} / f^{2} + 3v^{2}c_{8} / (2f^{4}) \approx 1.5$ , the parameter  $v_{T_n} / T_n$  reaches 0.7, below which we do not draw any result. (We also omit the findings in the region where the EW vacuum instability is below the cutoff; see section 2.2.) The values of  $c_{6} / f^{2}$  and  $c_{8} / f^{4}$  relevant for the present paper are therefore those within the gray and yellow regions on the left of the dashed thick line.

![](images/dde57832fff28dbcd9e8973b3cab4ee67ed9895c017d3e4f11e56f1f2007eb54.jpg)  
Figure 4. Left panel) The values of  $(T_{c} - T_{n}) / T_{c}$  in the plane  $c_{6} / f^{2} - c_{8} / f^{4}$  (dotted lines). The rest stands as in figure 3. Right panel) The values of  $\beta /H$  and  $10^{6}\times \alpha$  as a function of  $c_{6} / f^{2}$  for  $c_{8} / f^{4} = 5\mathrm{TeV}^{-4}$  (dotted curves),  $c_{8} / f^{4} = 2\mathrm{TeV}^{-4}$  (dashed curves) and  $c_{8} / f^{4} = 0$  (solid curves).

![](images/962f6acdfd4daf1e3ffdea65cc626ef2f02747644973a0c6fa706bf23b13f6a4.jpg)

The behaviour of  $T_{n}$  and  $T_{c}$  just described is also visible in the left panel of figure 4. As the figure highlights, for  $v_{T_n} / T_n \gtrsim 4$  the discrepancy between  $T_{n}$  (evaluated with the full potential  $V_{1\ell}$  and hard-thermal loop resummation) and  $T_{c}$  (evaluated in the mean-field approximation) is about  $20\%$ , whereas negligible for  $v_{T_n} / T_n \lesssim 1$ . From this point of view, what prevents the use of  $v_{T_c} / T_c \gtrsim 1$  in the mean-field approximation as a bound for EW baryogenesis (instead of  $v_{T_n} / T_n \gtrsim 1$ ) is not the accuracy of the result but the presence of a sizeable region where the nucleation never occurs.

Within the allowed  $c_{6} / f^{2} - c_{8} / f^{4}$  parameter region, we also calculate the inverse duration time of the phase transition and the normalised latent heat. In our case we can approximate them, respectively, by  $\beta / H = T_{n} \frac{d}{dT} \left( \frac{S_{3}}{T} \right)$  and  $\alpha = \epsilon (T_{n}) / (35T_{n}^{4})$ , where  $\epsilon (T_{n})$  is the latent heat at the temperature  $T_{n}$ . We determine them by means of CosmoTransition. Their dependencies on  $c_{6} / f^{2}$  and  $c_{8} / f^{4}$  are presented in the bottom panels of figure 3. The correlation between  $T_{n}$ ,  $v_{T_{n}} / T_{n}$ ,  $\alpha$  and  $\beta / H$  is evident. It is clear that all these quantities practically do not depend on  $c_{6} / f^{2}$  and  $c_{8} / f^{4}$  separately but only on  $2c_{6} / f^{2} + 3v^{2}c_{8} / f^{4}$ . As expected, nearby the thick dashed line, where  $T_{n}$  is small and  $v_{T_{n}} / T_{n}$  is large, the EWPT exhibits small  $\beta / H$  and large  $\alpha$ , typical of large supercoolings. The values of  $\alpha$  and  $\beta / H$  that we obtain are more readable in figure 4 (right panel) where their values are expressed as a function of  $c_{6} / f^{2}$  for  $c_{8} / f^{4} = 5\mathrm{TeV}^{-4}$  (dotted curves),  $c_{8} / f^{4} = 2\mathrm{TeV}^{-4}$  (dashed curves) and  $c_{8} / f^{4} = 0$  (solid curves). In general, for  $c_{8} = 0$ , our results are in very good agreement with those of refs. [24, 26].

A further quantity useful to characterise the EWPT is  $v_{w}$ , the velocity at which the bubbles containing the broken phase expand into the EW symmetric phase. This speed

Table 1. Comparison between tree (denoted by the superscript “(0)”) and loop level values of  $\lambda_{3}$  and  $\lambda_{4}$  with respect to their SM, tree-level values.  

<table><tr><td>c6f2[TeV-2]</td><td>c8f4[TeV-4]</td><td>λ3(0)/λ3,SM</td><td>λ4(0)/λ4,SM</td><td>λ3/λ3,SM</td><td>λ4/λ4,SM</td></tr><tr><td>0</td><td>0</td><td>1</td><td>1</td><td>0.91</td><td>0.56</td></tr><tr><td>2</td><td>-2</td><td>1.82</td><td>5.72</td><td>1.68</td><td>5.02</td></tr><tr><td>2</td><td>0</td><td>1.94</td><td>6.63</td><td>1.77</td><td>5.81</td></tr><tr><td>2</td><td>5</td><td>2.22</td><td>8.89</td><td>2.01</td><td>7.79</td></tr><tr><td>4</td><td>-2</td><td>2.76</td><td>11.34</td><td>2.53</td><td>10.48</td></tr><tr><td>4</td><td>0</td><td>2.88</td><td>12.25</td><td>2.63</td><td>11.32</td></tr><tr><td>4</td><td>5</td><td>3.16</td><td>14.52</td><td>2.87</td><td>13.44</td></tr></table>

results from the balance between the pressure difference between the two phases and the friction of the plasma on the bubbles. In general, the determination of  $v_{w}$  is subtle [25, 35-37]. Fortunately, for our aim, it is relevant to know  $v_{w}$  only when  $v_{T_n} / T_n \gtrsim 4$ ; see below. In such a regime, on one side one expects  $v \gtrsim 0.9$  [35], on the other side  $v_{w}$  cannot reach the speed of light, even asymptotically [38, 39]. Due to this tiny window, it seems acceptable to take  $v_{w} = 0.95$ , for which we can straightforwardly adopt some results of the gravitational wave literature.

A SFOEWPT sources a gravitational wave stochastic background. Its power spectrum depends on  $v_{w}$ ,  $T_{n}$ ,  $\beta / H$  and  $\alpha$  [40]. If the amplitude of the signal is strong enough, the LISA experiment will be able to detect it towards the end of the LHC [41]. Figure 4 in ref. [40] shows the values of  $\beta / H$  and  $\alpha$  that LISA can probe when  $v_{w} \simeq 0.95$ . We use this figure to forecast the capabilities of LISA for constraining the EFT we are working with. The region that can be tested is marked in yellow in figures 3 and 4.

# 2.4 Interplay between gravitational wave signatures and Higgs-self coupling measurements

From the bottom-up perspective we have adopted so far, the only collider implications of the operators  $\mathcal{O}_6$  and  $\mathcal{O}_8$  are changes in the rates of double- and triple-Higgs production. These are related to the modified Higgs couplings. Neglecting radiative corrections, the latter are given by

$$
\frac {\lambda_ {3}}{\lambda_ {3 , \mathrm {S M}}} = 1 + \frac {v ^ {2}}{m _ {h} ^ {2}} \left(2 c _ {6} \frac {v ^ {2}}{f ^ {2}} + 4 c _ {8} \frac {v ^ {4}}{f ^ {4}}\right), \quad \frac {\lambda_ {4}}{\lambda_ {4 , \mathrm {S M}}} = 1 + 4 \frac {v ^ {2}}{m _ {h} ^ {2}} \left(3 c _ {6} \frac {v ^ {2}}{f ^ {2}} + 8 c _ {8} \frac {v ^ {4}}{f ^ {4}}\right), \qquad (2. 1 6)
$$

The corresponding numbers at one loop, obtained numerically for several values of  $c_6 / f^2$  and  $c_8 / f^8$  are also shown in table 1.

These couplings have not been experimentally constrained yet. However, departures on the Higgs trilinear coupling beyond the range  $[-0.7, 7.1]$  will be accessible at the  $95\%$

![](images/60d6e468b95d5fb1f9a8c9bec53f8a638e7886d0fbd1d0d15e543cd086619388.jpg)  
Figure 5. Left panel) Region of figure 2 where the SFOEWPT is achieved accordingly to the criterion  $v_{T_n} \gtrsim T_n$  instead of  $v_{T_c} \gtrsim T_c$ . The reaches of FCC-ee [43] and LISA [40] are also displayed. Right panel) Allowed region from the left panel translated to the  $\lambda_3 / \lambda_{3,\mathrm{SM}} - \lambda_4 / \lambda_{4,\mathrm{SM}}$  plane together with the future experimental sensitivities [46].

![](images/98ca4a0fe21034f3b5a6ecf2843b74cd76bc6af51676baf14096c45614806f83.jpg)

C.L. in the HL-LHC run [42-44]. Moreover, values outside the interval [0.1, 1.9] [43] can be probed in a future FCC-ee facility [45]. Likewise, searches for double-Higgs and triple-Higgs production at future hadron colliders might also constrain  $\lambda_4$  [46]. The reach of the different facilities is shown in the left panel of figure 5 as a function of  $c_{6} / f^{2}, c_{8} / f^{4}$ . In the right panel, this information is depicted in the plane  $\lambda_3 / \lambda_{3,\mathrm{SM}} - \lambda_4 / \lambda_{4,\mathrm{SM}}$ . The grey area in the latter shows the non-accessible region of a  $100\mathrm{TeV~pp}$  collider, taken from ref. [46] (the reference cuts at  $\lambda_4 / \lambda_{4,\mathrm{SM}} = 11$ , and so do we). As we already mentioned, the region of the SFOEWPT identified by the nucleation temperature is a subset of the region found by the mean-field approximation. The region of parameter space that LISA is sensitive to is a subset of the former.

With LISA starting to take data in the early 2030's, a sensible part of the parameter space where the SFOEWPT takes place would be first probed by LISA. Almost the complete parameter space would be tested at a future FCC-ee. A future hadron collider with  $30\mathrm{ab}^{-1}$  [46] could be fully conclusive.

# 3 Matching of concrete models

The operators  $\mathcal{O}_6$  and  $\mathcal{O}_8$  are most commonly induced by new heavy scalars. These fields, however, generate normally other operators already at dimension six. Our aim here is to single out the properties of those UV completions that generate only  $\mathcal{O}_6$  and  $\mathcal{O}_8$  and are allowed by current data. Let us parameterize the effective Lagrangian after integrating out the new degrees of freedom as

$$
L = L _ {\mathrm {S M}} + \sum_ {i} \frac {c _ {i}}{f ^ {4 - d _ {i}}} \mathcal {O} _ {i}, \tag {3.1}
$$

where  $L_{\mathrm{SM}}$  stands for the SM Lagrangian,  $c_{i} / f^{4 - d_{i}}$  represents the coefficient of the corresponding operator  $\mathcal{O}_i$  and  $f$  is the typical new-physics scale. The couplings are all expected to scale as  $c_{i}\sim \tilde{g}^{2}\times \tilde{g}^{2n} / (4\pi)^{2n}$ , with  $\tilde{g}$  some weak coupling,  $n$  the perturbative order at which  $\mathcal{O}_i$  is generated, and  $d_{i}$  the canonical dimension of  $\mathcal{O}_i$ . This means that  $c_{6}$  can be  $\mathcal{O}(1)\mathrm{TeV}^{-2}$  as required by the SFOEWPT only if the operator  $\mathcal{O}_6$  is induced at tree level. Additionally, other operators with couplings of similar size will be generated. Among these, we have, in a Warsaw-like basis [47], the following ones [48]:

$$
\mathcal {O} _ {6} = (\phi^ {\dagger} \phi) ^ {3}, \quad \mathcal {O} _ {d 6} = \frac {1}{2} \partial_ {\mu} (\phi^ {\dagger} \phi) \partial^ {\mu} (\phi^ {\dagger} \phi), \quad \mathcal {O} _ {\phi D} = (\phi^ {\dagger} D _ {\mu} \phi) ((D ^ {\mu} \phi) ^ {\dagger} \phi). \tag {3.2}
$$

These typically appear together with further effective interactions. The same scalars generating  $\mathcal{O}_6, \mathcal{O}_{d6}$  and  $\mathcal{O}_{\phi D}$  also induce, at the same order, the operators

$$
\mathcal {O} _ {\psi \phi} = y _ {\psi} \left(\phi^ {\dagger} \phi\right) \left(\bar {\psi} _ {L} \phi \psi_ {R}\right), \tag {3.3}
$$

with  $y_{\psi}$  the Yukawa coupling of the SM fermions, here generically indicated as  $\psi_L$  and  $\psi_R$ . These operators modify the Higgs-fermion interactions.

$\mathcal{O}_{d6}$  provides a contribution to the Higgs kinetic term. As a consequence, the Higgs couplings to fermions and gauge bosons are modified with respect to those of the SM by the factors<sup>7</sup>

$$
\frac {g _ {h f f}}{g _ {h f f} ^ {\mathrm {S M}}} = c, \quad \frac {g _ {h V V}}{g _ {h V V} ^ {\mathrm {S M}}} = a, \quad \frac {g _ {h g g}}{g _ {h g g} ^ {\mathrm {S M}}} = c, \quad \frac {g _ {h \gamma \gamma}}{g _ {h \gamma \gamma} ^ {\mathrm {S M}}} = \frac {a I _ {\gamma} + c J _ {\gamma}}{I _ {\gamma} + J _ {\gamma}}, \tag {3.4}
$$

with

$$
a = 1 - c _ {d 6} \frac {v ^ {2}}{2 f ^ {2}}, \quad c = 1 - c _ {d 6} \frac {v ^ {2}}{2 f ^ {2}} + \mathcal {O} \left(c _ {\psi \phi}, c _ {\phi D}\right) \frac {v ^ {2}}{f ^ {2}}, \tag {3.5}
$$

and  $I_{\gamma} \simeq -1.84$ ,  $J_{\gamma} \simeq 8.32$ . We can obtain robust constraints on  $c_{d6}$  from the present LHC measurements by marginalising the Run-2 constraints on  $a$  over all possible values of  $c$ . One obtains [51]

$$
c _ {d 6} \frac {v ^ {2}}{2 f ^ {2}} = - 0.01 \pm 0.06 \quad \text {at} 68 \% \mathrm {C}. \tag{3.6}
$$

A further improvement to  $\pm 0.03$  is expected at the end of the HL run if no new physics is found [51]. We also note that neglecting  $\mathcal{O}_{\phi D}$  can be justified at the matching scale, since  $c_{\phi D}(f)\approx 0$  can be naturally explained by means of UV symmetries. However, due to  $\mathcal{O}_{d6}$ ,  $c_{\phi D}$  runs between the renormalization scales  $f$  and  $v$  [52]:

$$
c _ {\phi D} (v) \simeq c _ {\phi D} (f) + \frac {5}{2 4 \pi^ {2}} g ^ {\prime 2} c _ {d 6} (f) \log \frac {f}{v}. \tag {3.7}
$$

The present constraint on the coupling of  $\mathcal{O}_{\phi D}$ , namely [53]

$$
- 0. 0 2 3 <   c _ {\phi D} / f ^ {2} \mathrm {T e V} ^ {2} <   0. 0 0 6, \tag {3.8}
$$

provides an (indirect) bound on  $c_{d6}$ .

Clearly, in view of the these bounds on  $c_{d6}$  and  $c_{\phi D}$ , there will be little room for these couplings to be of the size of  $c_6$ , as suggested by power counting estimates in weakly-coupled scenarios. It is therefore crucial to understand whether there exist concrete UV scenarios that, at low energy, naturally generate a large hierarchy between  $c_6$  and the other  $c_i$  coefficients. A hierarchy between different operator coefficients can also be generated (rather model-independently) with strongly-coupled UV-completions. We discuss the resulting picture in section 3.3.

# 3.1 New scalars with weak isospin  $I \leq 1$

In light of the above discussion, it is worth considering scenarios in which operators other than  $\mathcal{O}_6$  are negligible. To this aim, let us first assume that the SM Higgs sector is extended only with new heavy scalars with isospin  $I \leqslant 1$ ; see ref. [49] for a related discussion. Concrete realisations and their signals at lepton colliders have been also discussed in ref. [54]. In the simplest case in which there is only one new field,  $\varphi$ ,  $\mathcal{O}_6$  is the only operator generated at tree level if and only if  $\varphi$  is a colourless  $\mathrm{SU}(2)_L$  doublet with vanishing couplings to the fermions [48, 55]. This scenario is then poorly motivated, because there is no symmetry that can remove only the doublet couplings to fermionic currents, since a  $\mathbb{Z}_2$  parity under which they are the only odd fields would make  $c_6$  also vanish. Moreover, the new doublets appearing in the most common UV setups do not exhibit this property.

On the other hand, one might argue that many motivated extensions of the SM Higgs sector involve several new fields. This is for instance the case of non-minimal composite Higgs models. $^{8}$  One particularly interesting example is the coset  $\mathrm{SU}(5) / \mathrm{SO}(5)$  [57], which admits a four-dimensional UV completion [58]. The scalar sector consists of a hyperchargeless triplet,  $\Xi_0$ , a triplet with hypercharge  $1$ ,  $\Xi_{1}$ , and a neutral singlet  $\mathcal{S}$  on top of the Higgs doublet. The effective operators we are interested in receive multiple contributions, namely

$$
\frac {c _ {d 6}}{f ^ {2}} = \frac {1}{M ^ {4}} \left(\kappa_ {\mathcal {S}} ^ {2} - \kappa_ {\Xi_ {0}} ^ {2} - 4 | \kappa_ {\Xi_ {1}} | ^ {2}\right), \quad \frac {c _ {\phi D}}{f ^ {2}} = - \frac {2}{M ^ {4}} \left(\kappa_ {\Xi_ {0}} ^ {2} - 2 | \kappa_ {\Xi_ {1}} | ^ {2}\right), \tag {3.9}
$$

$$
\frac {c _ {\psi \phi}}{f ^ {2}} = \frac {1}{M ^ {4}} \left(\kappa_ {\Xi_ {0}} ^ {2} + 2 | \kappa_ {\Xi_ {1}} | ^ {2}\right), \tag {3.10}
$$

and

$$
\begin{array}{l} \frac {c _ {6}}{f ^ {2}} = \frac {\kappa_ {\mathcal {S}}}{M ^ {4}} \left(- \lambda_ {\mathcal {S}} \kappa_ {\mathcal {S}} + \frac {\kappa_ {\mathcal {S} ^ {3}} \kappa_ {\mathcal {S}} ^ {2}}{M ^ {2}} - \lambda_ {\mathcal {S} \Xi_ {0}} \kappa_ {\Xi_ {0}} - 4 \operatorname {R e} \left[ \lambda_ {\mathcal {S} \Xi_ {1}} (\kappa_ {\Xi_ {1}}) ^ {*} \right] + \frac {\kappa_ {\mathcal {S} \Xi_ {0}} \kappa_ {\Xi_ {0}} ^ {2}}{M ^ {2}} + \frac {2 \kappa_ {\mathcal {S} \Xi_ {1}} | \kappa_ {\Xi_ {1}} | ^ {2}}{M ^ {2}}\right) \\ - \frac {\kappa_ {\Xi_ {0}} ^ {2}}{M ^ {4}} (\lambda_ {\Xi_ {0}} - 2 \lambda) - \frac {| \kappa_ {\Xi_ {1}} | ^ {2}}{M ^ {4}} (2 \lambda_ {\Xi_ {1}} - \sqrt {2} \tilde {\lambda} _ {\Xi_ {1}} - 4 \lambda) - \frac {2 \sqrt {2}}{M ^ {4}} \mathrm {R e} [ \lambda_ {\Xi_ {1} \Xi_ {0}} (\kappa_ {\Xi_ {1}}) ^ {*} \kappa_ {\Xi_ {0}} ] \\ - \frac {\sqrt {2}}{M ^ {6}} \kappa_ {\Xi_ {0} \Xi_ {1}} \kappa_ {\Xi_ {0}} \left| \kappa_ {\Xi_ {1}} \right| ^ {2}, \tag {3.11} \\ \end{array}
$$

where  $M$  is the (assumed common) mass term of all new scalars, and the other couplings just parameterise the renormalizable interactions among themselves and the SM particles [48].

It is interesting to show that not even in this case, which contains several scalars and many different couplings, can  $\mathcal{O}_6$  be the only non-vanishing operator. Indeed,  $c_{\phi D}$  only vanishes for  $\kappa_{\Xi_0} = \sqrt{2} |\kappa_{\Xi_1}|$ . This choice can in fact be enforced by an  $\mathrm{SU}(2)_L\times \mathrm{SU}(2)_R$  symmetry, as in the Georgi-Machacek model [59]. It would yield

$$
\frac {c _ {d 6}}{f ^ {2}} = \frac {1}{M ^ {4}} \left(\kappa_ {\mathcal {S}} ^ {2} - 6 | \kappa_ {\Xi_ {1}} | ^ {2}\right), \tag {3.12}
$$

which could then be removed by enforcing  $\kappa_{\mathcal{S}} = \sqrt{6} |\kappa_{\Xi_1}|$ . As a result, it would turn out that  $c_{\psi \phi} / f^2 = 4|\kappa_{\Xi_1}|^2 /M^4$ , which vanishes if and only if  $\kappa_{\Xi_1} = 0$ . In such a case, however,  $c_{6}$  is vanishing too.

Actually, we can go further and show that there is no weakly-coupled renormalizable extension of the Higgs sector containing singlets or triplets — with non-vanishing couplings to the SM—in which the effective operators produced after integrating out all new scalars at tree level modify only the scalar potential.

In order to prove this statement, let us work in the Warsaw basis and use the results of ref. [48]. Let us also assume first that the extended Higgs sector contains (at least) one neutral singlet. This field generates a positive  $c_{d6}$  that can be only cancelled by the contribution of a colourless triplet scalar. Indeed, any combination of colourless-triplet scalars, independently of the number of fields and their quantum numbers, gives a negative contribution to  $c_{d6}$ . This contribution is in fact the sum of all independent contributions [48].

Colourless triplet scalars, on their side, also produce the operator  $\mathcal{O}_{\psi \phi}$  with coefficient  $c_{\psi \phi} \propto c_{d6}$ . Therefore, it cannot be neglected if the triplet has to cancel the singlet contribution to  $\mathcal{O}_{d6}$ . The operator  $\mathcal{O}_{\psi \phi}$ , in turn, cannot be cancelled by the singlet, which does not produce it at all at tree level. For this matter, at least one extra doublet is to be present, too. However, doublets produce also four-fermion operators like  $\mathcal{O}_{le} = (\overline{l_L}\gamma_\mu l_L)(\overline{e_R}\gamma^\mu e_R)$ . This is actually generated only by doublets, with negative sign for  $l_L$  and  $e_R$  of the same flavour. So, it cannot be removed at all by including other scalar fields. Instead, its coefficient must be explicitly forced to vanish. In such a case, however, the coupling  $c_{\psi \phi}$  induced by the triplets would be strictly vanishing, and so all the linear interactions between the new physics and the SM, in contradiction with our hypothesis. Had we started considering the presence of at least one triplet, instead of one singlet, we would have arrived to exactly the same conclusion.

# 3.2 New scalars with weak isospin  $I > 1$

Let us now consider the case  $I > 1$ . The only scalars that can couple in a renormalizable way to the SM sector are quadruplets with hypercharges  $Y = 1/2, 3/2$ . Interestingly, they contribute only to  $\mathcal{O}_6$  when integrated out. These quadruplets can appear, for example, in Grand Unified Theories (GUT).

In GUT models, the SM fermions as well as the Higgs doublet are embedded in multiplets of a simple gauge group containing the SM  $\mathrm{SU}(3)_c\times \mathrm{SU}(2)_L\times \mathrm{U}(1)_Y$ . Two main GUT

gauge groups have been typically considered in the literature, namely  $\mathrm{SU}(5)$  and  $\mathrm{SO}(10)$  (and at a lesser extent,  $E_6\supset \mathrm{SO}(10)\supset \mathrm{SU}(5)$ ). The minimal irreducible representations of the scalar fields that can lead to SM gauge uncoloured quadruplets are the 35 and the 70 in  $\mathrm{SU}(5)$  [60, 61]. Obviously, such large-dimensional representations do not decompose only into quadruplets, but into many other states. An example is

$$
\mathbf {3 5} = (\mathbf {1}, \mathbf {4}) _ {3 / 2} + (\overline {{\mathbf {3}}}, \mathbf {3}) _ {2 / 3} + (\overline {{\mathbf {6}}}, \mathbf {2}) _ {1 / 6} + (\overline {{\mathbf {1 0}}}, \mathbf {1}) _ {1}, \tag {3.13}
$$

where the two numbers in parenthesis and the sub-index denote the dimension of the irreducible representation of  $\mathrm{SU}(3)_c$  and  $\mathrm{SU}(2)_L$  under which the corresponding field transforms and its hypercharge, respectively. Clearly, larger representations reduce to a larger number of exotic fields. Despite being unlikely, it is still possible that the effective operators generated by the coloured scalars are sub-leading with respect to the  $\mathcal{O}_6$  induced by the quadruplet. This can happen if two cases:  $i)$  If the coloured scalars are much heavier (which can be justified if a specific mechanism, similar to those advocated to solve the doublet-triplet splitting problem in SUSY GUT models [62-67], is enforced);  $ii)$  if all nonquadruplet fields have vanishing linear couplings to the SM at the renormalizable level. Surprisingly, this is the case for all extra fields in eq. (3.13) (although in principle they could couple, e.g., to dangerous flavour-violating currents via effective interactions).

Although the representation 35 does not include the Higgs boson, nor is required to break SU(5) down to the SM gauge group (unlike e.g. the 24), the aforementioned observations motivate further studies of a Higgs sector extended with quadruplets. $^9$  There is a caveat, though. Despite being suppressed by higher powers of  $1 / M^2$ , with  $M$  the mass of these fields, dimension-eight operators can be also in conflict with current data. For example, for a quadruplet with  $Y = 3 / 2$ , the operator  $(\phi^\dagger \phi)\mathcal{O}_{\phi D}$ , which violates custodial symmetry at dimension eight, carries a coefficient of order  $\sim c_6 / M^4$ . The rather low upper bound on  $M \lesssim$  few hundred GeVs implied by the SFOEWPT is therefore in tension with the very well measured value of the  $\rho$  parameter [68, 69]. Indeed, the experimental bound  $\rho_{exp} = (1.00037 \pm 0.00023)$  [70] imposes  $M \gg 1$  TeV. A way out to this problem is considering a custodialy symmetric quadruplet setup. We devote next section to this topic.

# 3.2.1 A custodial quadruplet setup

We start from the custodialy symmetric Lagrangian of the SU(2)-quadruplet that was discussed in ref. [71]. The potential is<sup>10</sup>

$$
\begin{array}{l} \mathcal {L} = \frac {1}{2} \langle (D _ {\mu} \Theta) ^ {\dagger} D ^ {\mu} \Theta \rangle + \frac {1}{2} \langle (D _ {\mu} \Phi) ^ {\dagger} D ^ {\mu} \Phi \rangle - \frac {\mu^ {2}}{2} \langle \Phi^ {\dagger} \Phi \rangle - \frac {\lambda}{4} \langle \Phi^ {\dagger} \Phi \rangle^ {2} \\ - \frac {\mu_ {\Theta} ^ {2}}{2} \langle \Theta^ {\dagger} \Theta \rangle - \frac {\lambda^ {\prime}}{4} \langle \Phi^ {\dagger} \Phi \rangle \langle \Theta^ {\dagger} \Theta \rangle - \widetilde {\lambda} \langle \Phi^ {\dagger} T _ {1 / 2} ^ {a} \Phi T _ {1 / 2} ^ {b} \rangle \langle \Theta^ {\dagger} T _ {3 / 2} ^ {a} \Theta T _ {3 / 2} ^ {b} \rangle \tag {3.14} \\ \end{array}
$$

$$
\begin{array}{l} - \frac {2 \sqrt {2}}{3} \lambda_ {\Theta} \langle \Phi^ {\dagger} \hat {T} _ {1 / 2} ^ {1, a} \Phi (\hat {T} _ {1 / 2} ^ {1, b}) ^ {\dagger} \rangle \langle \Phi^ {\dagger} (\hat {T} _ {3 / 2 1 / 2} ^ {1, a}) ^ {\dagger} \Theta \hat {T} _ {3 / 2 1 / 2} ^ {1, b} \rangle \\ {- \frac {2 \sqrt {2}}{3} \lambda_ {\Theta} \langle \Phi \hat {T} _ {1 / 2} ^ {1, a} \Phi^ {\dagger} (\hat {T} _ {1 / 2} ^ {1, b}) ^ {\dagger} \rangle \langle \Phi (\hat {T} _ {3 / 2 1 / 2} ^ {1, a}) ^ {\dagger} \Theta^ {\dagger} \hat {T} _ {3 / 2 1 / 2} ^ {1, b} \rangle} {+ \mathcal {O} (\Theta^ {3}, \Theta^ {4}),} \\ \end{array}
$$

where  $\langle A\rangle$  is the trace of the matrix  $A$ , and

$$
\Theta = \left( \begin{array}{c c c c} \Theta_ {3} ^ {*} & - \Theta_ {1} ^ {- *} & \Theta_ {1} ^ {+ +} & \Theta_ {3} ^ {+ + +} \\ - \Theta_ {3} ^ {+ *} & \Theta_ {1} ^ {*} & \Theta_ {1} ^ {+} & \Theta_ {3} ^ {+ +} \\ \Theta_ {3} ^ {+ + *} & - \Theta_ {1} ^ {+ *} & \Theta_ {1} & \Theta_ {3} ^ {+} \\ - \Theta_ {3} ^ {+ + + *} & \Theta_ {1} ^ {+ + *} & \Theta_ {1} ^ {-} & \Theta_ {3} \end{array} \right) \equiv \left(\widetilde {\Theta} _ {3} \widetilde {\Theta} _ {1} \Theta_ {1} \Theta_ {3}\right) \quad \text {a n d} \quad \Phi = \left( \begin{array}{c c} h _ {0} ^ {*} & h ^ {+} \\ - h ^ {-} & h _ {0} \end{array} \right) \equiv \left(\widetilde {\phi} \phi\right). \tag {3.15}
$$

In this notation,  $\Theta_3$  has hypercharge  $3/2$ ,  $\Theta_1$  has hypercharge  $1/2$ , and  $\phi$  is the SM-Higgs doublet. The covariant derivative is defined as

$$
D _ {\mu} \Theta = \partial_ {\mu} \Theta + i g W _ {\mu} \Theta - i g ^ {\prime} B _ {\mu} \Theta T _ {3 / 2} ^ {3}. \tag {3.16}
$$

From eq. (3.14) we can derive the equations of motion for  $\Theta$  and integrate it out at tree level. We find

$$
\Delta \mathcal {L} _ {6} = \frac {\lambda_ {\Theta} ^ {2}}{\mu_ {\Theta} ^ {2}} \left(\phi^ {\dagger} \phi\right) ^ {3}, \tag {3.17}
$$

$$
\Delta \mathcal {L} _ {8} = \frac {\lambda_ {\Theta} ^ {2}}{2 \mu_ {\Theta} ^ {4}} \left(5 (\phi^ {\dagger} \phi) ^ {2} (D _ {\mu} \phi) ^ {\dagger} (D ^ {\mu} \phi) + (\phi^ {\dagger} \phi) D _ {\mu} (\phi^ {\dagger} \phi) D ^ {\mu} (\phi^ {\dagger} \phi)\right) - \frac {\lambda_ {\Theta} ^ {2}}{\mu_ {\Theta} ^ {4}} \left(\lambda^ {\prime} + \frac {1 5}{4} \widetilde {\lambda}\right) (\phi^ {\dagger} \phi) ^ {4}.
$$

The contribution to  $\Delta \mathcal{L}_6$  is consistent with [48]. There, the contribution of  $\Theta_3$  is  $3\lambda_{\Theta}^{2} / (2\mu_{\Theta}^{2})$  and the one of  $\Theta_{1}$  (with the relation  $\lambda_{\Theta_1} = -\sqrt{3}\lambda_{\Theta_3}$  coming from eq. (3.14)) is also  $3\lambda_{\Theta}^{2} / (2\mu_{\Theta}^{2})$ . The resulting factor of 3 is absorbed in the different definition of  $\mathcal{O}_6$  compared to ours. We see that at dimension eight the model induces the desired contribution to the Higgs potential, as well as two more contributions with two derivatives. All of them conserve custodial symmetry.

We have also checked, using SARAH [72], that loop corrections to the  $\rho$  and  $S$  parameters are well within the experimental bound. The collider phenomenology of the custodial quadruplet can be understood in terms of the unbroken  $\mathrm{SU}(2)_V$ . The Higgs bi-doublet decomposes as  $(2,2) = 1 + 3$ , while the custodial bi-quadruplet decomposes as  $(4,4) = 1 + 3 + 5 + 7$ . The latter singlet and triplet contain only electrically neutral and singly-charged scalars, which are difficult to produce and detect at colliders. Note that they only couple to the SM fermions via the mixing with the Higgs singlet and triplet. Moreover, this mixing is very small: after all,  $\mathcal{O}_6$  is the only operator generated at tree level, which does not modify the Higgs couplings at low energy. This also suggests that measuring the Higgs couplings is not the most promising strategy to test this setup.

Moreover, the septuplet contains large electric charges. However, these cannot directly decay into pairs of SM particles.[11] They decay only via the emission of (soft) gauge bosons

![](images/8a8a7c234111966302a2d18d1fe2f174afbcb4d1b2d1ab01fa899eab15d803f8.jpg)

![](images/7c982e325d517b7aab80bfa29c5b7d4c068577cb14dfe5c3d431c3029fb034ee.jpg)

![](images/abb9efa10b98b15892ba80a9ee423eefcc13bcd767023f99b075e6109ff60bac.jpg)  
Figure 6. Upper left) Neutral current cross sections for pair-production of scalars in the custodial quadruplet model. Upper right) Same as before but for the charged current. Bottom left) Integrated luminosity required to exclude the custodial quadruplet at the  $95\%$  C.L. for different masses using two different analyses; see text for details. Two representative values of the collected luminosity,  $\mathcal{L} = 300\mathrm{fb^{-1}}$  and  $\mathcal{L} = 3\mathrm{ab^{-1}}$  are also shown with dashed lines. Bottom right) Parameter space region where the FOEWPT takes place for  $\lambda^{\prime} = \tilde{\lambda} = 1$  and the reach of different searches. The yellow region shows the HL-LHC reach taken from the bottom-left panel.

![](images/cf1c7d58afac26d576c4fbcffc06cd2fa57377d7fff6a2aad2c158ae5d35ae36.jpg)

into lower-charged states in the custodial quadruplet, which are also difficult to test at colliders. The quintuplet, instead, can be both efficiently produced (in pairs via EW interactions) and decays mostly into pairs of gauge bosons (indeed  $\mathbf{3} \times \mathbf{3} = 1 + \mathbf{3} + \mathbf{5}$ ). Decays into pairs of Higgs bosons are not allowed, because this is a complete singlet of  $\mathrm{SU}(2)_V$ . In particular, the doubly-charged, singly-charged and neutral components of the quintuplet decay with branching ratios

$$
\operatorname {B r} \left(\Theta^ {\pm \pm} \rightarrow W ^ {\pm} W ^ {\pm}\right) = 1, \quad \operatorname {B r} \left(\Theta^ {\pm} \rightarrow W ^ {\pm} Z\right) = 1, \quad \operatorname {B r} \left(\Theta^ {0} \rightarrow W ^ {+} W ^ {-} + Z Z\right) = 1. \tag {3.18}
$$

We implement this model in MadGraph v5 [73] by means of Feynrules v2 [74]. We subsequently compute the pair-production cross sections mediated by neutral and charged currents for masses in between 300 and  $1000\mathrm{GeV}$ . The results are shown in the upper left and upper right panels of figure 6, respectively.

We have also estimated the current and the future LHC reach for this scenario. To this aim, we have generated Monte Carlo events, including radiation, fragmentation and hadronization effects with Pythia v6 [75], and analysed them using CheckMate v2 [76].

The latter implements several multi-lepton SUSY searches. Among them, the search that turns out to be the most sensitive to our scenario, is the "SR3 $\ell$  -  $H$  " signal region of ref. [77], which looks for three leptons, no  $b$ -jets and large missing energy. This analysis considers  $13\mathrm{fb}^{-1}$  of LHC data at  $\sqrt{s} = 13$  TeV. The integrated luminosity needed to exclude a particular value of the quadruplet mass at the  $95\%$  C.L. can then be estimated as

$$
\mathcal {L} = 1 3 \mathrm {f b} ^ {- 1} \times \frac {1}{\left(s / s _ {\mathrm {e x c l}}\right) ^ {2}}, \tag {3.19}
$$

where  $s / s_{\mathrm{excl}}$  is the number of expected signal events over the number of excluded signal events as reported by CheckMate. The corresponding result is represented by the thick solid line in the left bottom panel of figure 6. The thin solid line represents the luminosity required to test the different masses using the improved multi-lepton search described in ref. [78]. As things stand, masses as large as  $M \sim 600 \mathrm{GeV}$  can be tested in multi-lepton final states at the LHC. Getting ahead of the results discussed, we also show the reach of LHC Higgs-self couplings measurements as well as that of the gravitational wave observatory LISA; see right bottom panel in figure 6. Interestingly, the former cannot even test the parameter space region where the FOEWPT takes place. (As a matter of fact, in the present scenario the LHC Higgs-self couplings measurements are sensitive only to the region where the theory does not achieve EWSB.). These results suggest that most weakly-coupled models (those containing  $\mathrm{SU}(2)_L$  charged states), even if tuned to avoid large corrections to operators other than  $\mathcal{O}_6$ , can be better tested at gravitational wave observatories or in direct LHC searches.[12]

# 3.3 Strongly-coupled models

So far, we discussed the dynamics of the electroweak phase transition in presence of effective modifications of the scalar potential only, as well as potential UV-completions that lead to this particular pattern of low-energy effects. Working in a generic bottom-up EFT, we would in principle have many more effective operators, with coefficients of similar size to the coefficients that modify the potential. To overcome the strong experimental constraints on these operators, we require a hierarchy between the large effects in the scalar sector and the more constrained effects in the gauge-fermion sector. This can be achieved with a strongly-coupled UV-completion. While the complete description of such a UV-completion requires lattice simulations (and is therefore more model-dependent), we can describe the low-energy effects by assuming a mass gap between the (pseudo-) Nambu-Goldstone bosons and the higher resonances of the theory. The EW chiral Lagrangian  $(ew\chi L)$  [79-91] is the most general EFT that describes such low-energy effects of strongly-coupled new physics. Historically, it emerged from the Higgs-less chiral Lagrangian [92-95], which was then supplemented with a generic scalar singlet  $h$ . Since this does not assume any IR-doublet structure for the Higgs, it describes a very wide class of new-physics models that induce

large deviations in the Higgs sector from the SM. The leading-order  $ew\chi L$  is

$$
\begin{array}{l} L _ {\mathrm {L O}} ^ {e w \chi} = - \frac {1}{2} \langle G _ {\mu \nu} G ^ {\mu \nu} \rangle - \frac {1}{2} \langle W _ {\mu \nu} W ^ {\mu \nu} \rangle - \frac {1}{4} B _ {\mu \nu} B ^ {\mu \nu} \\ + i \bar {q} _ {L} \not D q _ {L} + i \bar {\ell} _ {L} \not D \ell_ {L} + i \bar {u} _ {R} \not D u _ {R} + i \bar {d} _ {R} \not D d _ {R} + i \bar {e} _ {R} \not D e _ {R} \\ + \frac {v ^ {2}}{4} \operatorname {T r} \left(D _ {\mu} U ^ {\dagger} D ^ {\mu} U\right) (1 + F (h)) + \frac {1}{2} \partial_ {\mu} h \partial^ {\mu} h - V (h) \\ - \frac {v}{\sqrt {2}} \left[ \bar {q} _ {L} \left(Y _ {u} + \sum_ {n = 1} ^ {\infty} Y _ {u} ^ {(n)} \left(\frac {h}{v}\right) ^ {n}\right) U P _ {+} q _ {R} + \bar {q} _ {L} \left(Y _ {d} + \sum_ {n = 1} ^ {\infty} Y _ {d} ^ {(n)} \left(\frac {h}{v}\right) ^ {n}\right) U P _ {-} q _ {R} \right. \\ \left. + \bar {\ell} _ {L} \left(Y _ {e} + \sum_ {n = 1} ^ {\infty} Y _ {e} ^ {(n)} \left(\frac {h}{v}\right) ^ {n}\right) U P _ {-} \ell_ {R} + \text {h . c .} \right], \tag {3.20} \\ \end{array}
$$

where  $U$  stands for the exponential of the Goldstone matrix,  $G, W$  and  $B$  are the SM gauge fields,  $u_{R}, d_{R}, e_{R}, q_{L}$  and  $\ell_{L}$  are the fermions of the SM, and  $Y$  are generalised Yukawa couplings. The scalar  $h$  couples through general polynomials to the other fields, which reflects its strongly-coupled origin.

These polynomials  $(V(h), F(h)$ , and  $Y_{i}(h) = Y_{i} + \sum_{n=1}^{\infty} Y_{i}^{(n)} (h / v)^{n}$  are not truncated at canonical dimension four, but go to arbitrary order. (An additional operator of the structure  $(\partial_{\mu} h)(\partial^{\mu}) f(h)$  is also allowed by symmetry, but can be removed via field redefinitions, without loss of generality [90].) The coefficients of these polynomials depend on  $v / f$ .

As the Lagrangian in eq. (3.20) contains terms with arbitrarily high canonical dimension, the EFT can clearly not be organized in terms of canonical dimensions. Instead, it is organised by a generalisation of the momentum expansion of chiral perturbation theory [96], the chiral dimensions [90, 91]. They reflect an expansion in terms of loops, which guarantees the renormalizability of the EFT at a fixed order in the expansion. The cutoff of the EFT is at  $\Lambda = 4\pi f$ , yielding the expansion parameter  $f^2 /\Lambda^2 = 1 / 16\pi^2$ . For  $v < f$ , the parameter  $\xi = v^{2} / f^{2}$  is smaller than the unity and eq. (3.20) can be further expanded in  $\xi$ . In this scenario, a double expansion in  $\xi$  and  $1 / 16\pi^2$  organises the EFT [97], in the spirit of the strongly-interacting light Higgs Lagrangian [98].

In this double expansion, we still see some of the decoupling effects, but also a pattern of Wilson coefficients that is coming from the strong sector. Depending on the structure of the operators, they will be suppressed by ratios of scales ( $\xi$ , based on their canonical dimension) and loop factors  $(1/16\pi^2$ , based on their chiral dimension). This creates an additional hierarchy among the operators of a given canonical dimension, compared to the weakly-coupled case of section 3. Some of the dimension six operators, corresponding to  $L_{\mathrm{LO}}^{ew\chi}$ , will only be suppressed by  $\xi$ , while other operators, corresponding to  $L_{\mathrm{NLO}}^{ew\chi}$ , will be suppressed by an additional loop factor, resulting in  $\xi/16\pi^2$ . The former affects the Higgs sector with deviations of  $\mathcal{O}(10\%)$ , dominating over effects in the gauge-fermion sector of the latter group, with deviations of  $\mathcal{O}(1\%)$  or below. This hierarchy also reflects the current experimental constraints: the gauge-fermion sector is rather strongly constrained, while large effects in the Higgs couplings are still possible. The  $ew\chi L$  of eq. (3.20) is now expanded in both chiral and canonical dimensions.

Since  $\xi = \mathcal{O}(0.1 - 0.2)$  [1, 51, 99, 100], effects of  $\mathcal{O}(\xi^2)$  could in principle be larger than the  $\mathcal{O}(1 / 16\pi^2)$  effects. The leading effects in the double expansion are then given by expanding  $L_{\mathrm{LO}}$  up to  $\mathcal{O}(\xi^2)$ . A priori, the Higgs potential, which at this order contains both  $\mathcal{O}_6$  and  $\mathcal{O}_8$ , is of chiral dimension 0 and the dominating effect. However, the Higgs mass is then expected to be of order  $\mathcal{O}(\Lambda)$ , which would break the EFT approach. In order for this to make sense, the Higgs mass must be parametrically suppressed to appear at chiral dimension of 2. $^{13}$  An additional fine tuning of  $\mathcal{O}(\xi)$  is needed for  $m_h \sim v$ . This, however, might only affect the mass term of the potential and the Higgs self-couplings could have large deviations from the SM, induced by  $c_6$  and  $c_8$ .

We can understand the enhancement on the operators in the potential by just dimensional analysis if we assume that the strongly-coupled theory is described by only one relevant coupling  $g_*$ . To this aim, we need to abandon the convention  $\hbar = c = 1$  recovering the physical dimensions of these two constants. It turns out that the coefficient of any operator involving  $r$  Higgs insertions and  $q$  derivatives scales as  $g_*^2 f^4 [h / f]^r [\partial /(g_*f)]^q$ , up to  $\mathcal{O}(1)$  coefficients [56, 98, 101, 102]. Hence, scalar operators not carrying derivatives are enhanced with respect to the derivative ones by several powers of  $g_*$  ( $\gg 1$  in a strongly couple theory); e.g.  $c_{6} \sim g_{*}^{2}$  versus  $c_{d6} \sim 1$ . We refer to ref. [103] for a discussion on which scenarios show this enhancement while still having  $m_h \sim v$ . This justifies why we studied the effects of  $\mathcal{O}_6$  and  $\mathcal{O}_8$ , neglecting other effects, as first approximation.

To account for all leading effects consistently, we have to consider the full set of dimension-six and dimension-eight operators that contribute at chiral dimension 2 for the expansion in  $\xi$ . The operators are

$$
\left(\phi^ {\dagger} \phi\right) ^ {3}, \qquad \partial_ {\mu} \left(\phi^ {\dagger} \phi\right) \partial^ {\mu} \left(\phi^ {\dagger} \phi\right), \qquad \bar {\Psi} Y \phi \Psi \left(\phi^ {\dagger} \phi\right),
$$

$$
\left(\phi^ {\dagger} \phi\right) ^ {4}, \quad \partial_ {\mu} \left(\phi^ {\dagger} \phi\right) \partial^ {\mu} \left(\phi^ {\dagger} \phi\right) \left(\phi^ {\dagger} \phi\right), \quad \bar {\Psi} Y \phi \Psi \left(\phi^ {\dagger} \phi\right) ^ {2}. \tag {3.21}
$$

With the identification  $\phi = \frac{(v + h)}{\sqrt{2}} U\binom{0}{1}$ , we find at the different orders of  $\xi$ :

$$
\begin{array}{l} L _ {\xi^ {0}} = \frac {1}{2} \partial_ {\mu} h \partial^ {\mu} h + \frac {\mu^ {2}}{2} (v + h) ^ {2} - \frac {\lambda}{4} (v + h) ^ {4} - \frac {1}{\sqrt {2}} \bar {\Psi} \hat {Y} _ {\Psi} U P _ {\pm} \Psi (v + h) \\ + \frac {v ^ {2}}{4} \operatorname {T r} \left(D _ {\mu} U ^ {\dagger} D ^ {\mu} U\right) \left(1 + \frac {h}{v}\right) ^ {2}, \\ \end{array}
$$

$$
L _ {\xi^ {1}} = \frac {c _ {d 6}}{2 f ^ {2}} \partial_ {\mu} h \partial^ {\mu} h (v + h) ^ {2} - \frac {c _ {6}}{8 f ^ {2}} (v + h) ^ {6} - \frac {1}{\sqrt {2} f ^ {2}} \bar {\Psi} \hat {Y} _ {\Psi} ^ {(6)} U P _ {\pm} \Psi (v + h) ^ {3},
$$

$$
L _ {\xi^ {2}} = \frac {c _ {d 8}}{2 f ^ {4}} \partial_ {\mu} h \partial^ {\mu} h (v + h) ^ {4} - \frac {c _ {8}}{1 6 f ^ {4}} (v + h) ^ {8} - \frac {1}{\sqrt {2} f ^ {4}} \bar {\Psi} \hat {Y} _ {\Psi} ^ {(8)} U P _ {\pm} \Psi (v + h) ^ {5}. \tag {3.22}
$$

To bring the Lagrangian to the form of  $L_{\mathrm{LO}}^{ew\chi}$  in eq. (3.20), we have to canonically normalise the field  $h$  using the field redefinition discussed in ref. [90]. We find [104]

$$
\begin{array}{l} h \rightarrow h \left\{1 - \frac {\xi}{2} c _ {d 6} \left(1 + \frac {h}{v} + \frac {h ^ {2}}{3 v ^ {2}}\right) + \xi^ {2} c _ {d 6} ^ {2} \left(\frac {3}{8} + \frac {h}{v} + \frac {1 3}{1 2} \left(\frac {h}{v}\right) ^ {2} + \frac {1 3}{2 4} \left(\frac {h}{v}\right) ^ {3} + \frac {1 3}{1 2 0} \left(\frac {h}{v}\right) ^ {4}\right)\right. \\ \left. - \xi^ {2} c _ {d 8} \left(\frac {1}{2} + \frac {h}{v} + \left(\frac {h}{v}\right) ^ {2} + \frac {1}{2} \left(\frac {h}{v}\right) ^ {3} + \frac {1}{1 0} \left(\frac {h}{v}\right) ^ {4}\right) \right\}. \tag {3.23} \\ \end{array}
$$

To obtain the right Higgs VEV and mass, the parameters  $\mu^2$  and  $\lambda$  have to fulfil

$$
\mu^ {2} = \frac {m _ {h} ^ {2}}{2} + \frac {v ^ {2}}{f ^ {2}} \left(\frac {1}{2} c _ {d 6} m _ {h} ^ {2} - \frac {3}{4} c _ {6} v ^ {2}\right) + \frac {v ^ {4}}{f ^ {4}} \left(\frac {1}{2} c _ {d 8} m _ {h} ^ {2} - c _ {8} v ^ {2}\right), \tag {3.24}
$$

$$
\lambda = \frac {m _ {h} ^ {2}}{2 v ^ {2}} + \frac {v ^ {2}}{f ^ {2}} \left(\frac {c _ {d 6}}{2} \frac {m _ {h} ^ {2}}{v ^ {2}} - \frac {3 c _ {6}}{2}\right) + \frac {v ^ {4}}{f ^ {4}} \left(\frac {c _ {d 8}}{2} \frac {m _ {h} ^ {2}}{v ^ {2}} - \frac {3 c _ {8}}{2}\right).
$$

Applying eq. (3.23) everywhere in eq. (3.22), we find the expansion of  $V(h), F(h)$ , and  $Y(h)$  in  $\xi$ . Writing

$$
V (h) = \frac {1}{2} m _ {h} ^ {2} v ^ {2} \left[ \frac {h ^ {2}}{v ^ {2}} + \sum_ {i = 3} ^ {8} \lambda_ {i} \left(\frac {h}{v}\right) ^ {i} \right], \tag {3.25}
$$

$$
F (h) = \sum_ {i = 1} ^ {6} f _ {i} \left(\frac {h}{v}\right) ^ {i},
$$

we finally have

$$
\lambda_ {3} = 1 + \frac {v ^ {2}}{f ^ {2}} \left(2 c _ {6} \frac {v ^ {2}}{m _ {h} ^ {2}} - \frac {3}{2} c _ {d 6}\right) + \frac {v ^ {4}}{f ^ {4}} \left(\frac {1 5}{8} c _ {d 6} ^ {2} - 3 \frac {v ^ {2}}{m _ {h} ^ {2}} c _ {6} c _ {d 6} - \frac {5}{2} c _ {d 8} + 4 \frac {v ^ {2}}{m _ {h} ^ {2}} c _ {8}\right), \tag {3.26}
$$

$$
\lambda_ {4} = \frac {1}{4} + \frac {v ^ {2}}{f ^ {2}} \left(3 c _ {6} \frac {v ^ {2}}{m _ {h} ^ {2}} - \frac {2 5}{1 2} c _ {d 6}\right) + \frac {v ^ {4}}{f ^ {4}} \left(\frac {1 1}{2} c _ {d 6} ^ {2} - 9 \frac {v ^ {2}}{m _ {h} ^ {2}} c _ {6} c _ {d 6} - \frac {2 1}{4} c _ {d 8} + 8 \frac {v ^ {2}}{m _ {h} ^ {2}} c _ {8}\right),
$$

$$
f _ {1} = 2 - \frac {v ^ {2}}{f ^ {2}} c _ {d 6} + \frac {v ^ {4}}{f ^ {4}} \left(\frac {3}{4} c _ {d 6} ^ {2} - c _ {d 8}\right), \tag {3.27}
$$

$$
f _ {2} = 1 - 2 \frac {v ^ {2}}{f ^ {2}} c _ {d 6} + \frac {v ^ {4}}{f ^ {4}} \left(3 c _ {d 6} ^ {2} - 3 c _ {d 8}\right)
$$

and

$$
Y _ {\Psi} ^ {(1)} = Y _ {\Psi} + \frac {v ^ {2}}{f ^ {2}} \left(2 \hat {Y} _ {\Psi} ^ {(6)} - \frac {c _ {d 6}}{2} Y _ {\Psi}\right) + \frac {v ^ {4}}{f ^ {4}} \left(4 \hat {Y} _ {\Psi} ^ {(8)} - \frac {c _ {d 8}}{2} Y _ {\Psi} - c _ {d 6} \hat {Y} _ {\Psi} ^ {(6)} + \frac {3}{8} c _ {d 6} ^ {2} Y _ {\Psi}\right), \tag {3.28}
$$

$$
Y _ {\Psi} ^ {(2)} = \frac {v ^ {2}}{f ^ {2}} \left(3 \hat {Y} _ {\Psi} ^ {(6)} - \frac {c _ {d 6}}{2} Y _ {\Psi}\right) + \frac {v ^ {4}}{f ^ {4}} \left(1 0 \hat {Y} _ {\Psi} ^ {(8)} - c _ {d 8} Y _ {\Psi} - 4 c _ {d 6} \hat {Y} _ {\Psi} ^ {(6)} + c _ {d 6} ^ {2} Y _ {\Psi}\right),
$$

where we only list the couplings relevant for the subsequent discussion. The matrices  $Y_{\Psi}$  and  $Y_{\Psi}^{(n)}$  are the fermion mass and Yukawa matrices defined in eq. (3.20). Note that the functional dependence of eqs. (3.26) and (3.28) on  $c_{i}$  differ from the result of refs. [97, 104], as we do not include explicit factors of  $\lambda$  in the definition of the Wilson coefficients. Already now we see two of the implications of adding these effective operators. The triple

and quartic-Higgs couplings are further modified with respect to the SM. Moreover, new vertices, such as  $\bar{\Psi}\Psi hh$ , also relevant for the study of double-Higgs production, arise.

Additionally, for current Higgs observables, also the local  $G Gh$  and  $\gamma \gamma h$  operators are important, even though they are formally of next-to-leading order. This is because these amplitudes arise at the one-loop level of the leading-order Lagrangian; see ref. [105]. Such a Lagrangian is

$$
L _ {G G h} = L _ {k i n} + G _ {\mu \nu} G ^ {\mu \nu} \left[ \frac {c _ {g 6}}{1 6 \pi^ {2} f ^ {2}} \phi^ {\dagger} \phi + \frac {c _ {g 8}}{1 6 \pi^ {2} f ^ {4}} (\phi^ {\dagger} \phi) ^ {2} \right]. \tag {3.29}
$$

After symmetry breaking and the field redefinition of eq. (3.23), this creates a contribution that renormalizes the gluon kinetic term and therefore  $G_{\mu \nu}$ . After this renormalization, we find

$$
L _ {G G h} = G _ {\mu \nu} G ^ {\mu \nu} \left[ 1 + f _ {G 1} \frac {h}{v} + f _ {G 2} \frac {h ^ {2}}{v ^ {2}} + \mathcal {O} \left(h ^ {3}\right) \right], \tag {3.30}
$$

with

$$
1 6 \pi^ {2} f _ {G 1} = \xi c _ {g 6} + \xi^ {2} \left(c _ {g 8} - \frac {1}{2} c _ {d 6} c _ {g 6} - \frac {c _ {g 6} ^ {2}}{3 2 \pi^ {2}}\right), \tag {3.31}
$$

$$
3 2 \pi^ {2} f _ {G 2} = \xi c _ {g 6} + \xi^ {2} \left(3 c _ {g 8} - \frac {1}{2} c _ {d 6} c _ {g 6} - \frac {c _ {g 6} ^ {2}}{3 2 \pi^ {2}}\right).
$$

The last term in each of the  $f_{Gi}$  comes from the renormalization and is sub-leading. Finally, it is also worth noting that all these operators would contribute to the EWPT, as they alter the  $h_c$ -dependent squared masses  $m_i^2$  in eqs. (2.7)-(2.9). In addition, the derivative operator  $\mathcal{O}_{d6}$  requires a reevaluation of the Coleman-Weinberg effective potential at finite temperature, as the field redefinition of eq. (3.23) cannot be done in the unbroken phase [106, 107]. All these effects would be suppressed by  $v^2 / f^2$  in  $a_0$ , but would nevertheless have an impact on the computation of the quantities of the EWPT.

Current experimental results only constrain effective couplings with a single Higgs field [51, 99], namely  $Y_{t,b,\tau}^{(1)}, f_1$ , and  $f_{G1}$  from the list above. From these,  $f_1$  is the most constrained, but still allows for deviations of  $\mathcal{O}(5\%)$ . The others are not constrained beyond  $\mathcal{O}(10\%)$ . While from a bottom-up point of view a deviation in one of these couplings might hint to a deviation in  $\lambda_3$  of comparable size, such conclusions are strongly model dependent.

Double Higgs production, which would shed light on the  $\lambda_{3}$  coupling of the Higgs potential in the SM, depends on five of the effective parameters from above [44, 108] if we restrict ourselves to the top loops only. These are  $Y_{t}^{(1)}, Y_{t}^{(2)}, f_{G1}, f_{G2}$ , and  $\lambda_{3}$ . A large deviation in  $\lambda_{3}$  from its SM value could then be not seen in the experiment because of the interplay with the otherwise unconstrained other parameters.

# 4 Conclusions

It is well known that the presence of higher-dimensional operators in the Standard Model Higgs potential can drastically influence the dynamics of the ElectroWeak (EW) symmetry breaking. Among the possible operators, the interactions  $\mathcal{O}_n = (\phi^\dagger \phi)^{\frac{n}{2}}$ , with  $\phi$  being the Higgs doublet, have attracted a lot of attention to make the EW Phase Transition (EWPT)

strongly first order while evading any scheduled LHC search. Achieving a strongly first order EWPT requires  $c_6 / f^2 \gtrsim 1 \, \mathrm{TeV}^{-2}$ , with  $f$  the cutoff of the theory and  $c_6$  the coefficient of  $\mathcal{O}_6$ . This implies that  $f$  is likely too close to the EW scale for the dimension-six EFT to be accurate, at least in weakly-coupled theories. Dimension-eight operators have then to be considered as well, which is also the case when strongly-coupled sectors are present. Such sectors can also lead to naturally large corrections to the Higgs potential (in comparison with other operators). In view of this possibility, we have also examined the EFT where (only) both  $\mathcal{O}_6$  and  $\mathcal{O}_8$  are unsuppressed.

In the aforementioned dimension-eight setup, we have computed the parameters relevant for the EWPT, including the critical and nucleation temperatures and the VEVs of the Higgs at these temperatures. We have also estimated the latent heat and the inverse duration time of the phase transition, characterising the gravitational waves produced in the collisions of nucleated bubbles. Regarding the coefficients of  $\mathcal{O}_6$  and  $\mathcal{O}_8$ ,  $c_6$  and  $c_8$  respectively, we have obtained that the parameter region  $3 \lesssim c_6 / f^2 + 3v^2 c_8 / (2f^4) \lesssim 3.5$  is in the reach of the future LISA experiment. Remarkably, due to the low LHC sensitivity to  $\mathcal{O}_6$  and  $\mathcal{O}_8$ , LISA will be the first experiment able to significantly constrain these operators. Concerning the reach of future colliders, we have shown that almost all values of interest will be probed by a future FCC-ee in double-Higgs production, while the whole parameter space will be testable combining double- and triple-Higgs production in hadronic colliders.

Given that the new physics matching the previous EFT must be quite low, we have also explored the possibility of producing the supposedly heavy new fields at the LHC. Among the ultraviolet completions exhibiting only the operators  $\mathcal{O}_n$ , we have proven that in weakly-coupled setups consisting of new scalar singlets or triplets, the presence at low energies of other effective operators already quite constrained by LHC and EW precision data is unavoidable. (Of course, in scenarios with several scalars, a tuning in the fundamental parameters can still yield to an EFT where the coefficients  $c_6$  and  $c_8$  are substantially larger than those of the other effective operators.) On the contrary, in models involving only doublets or quadruplets (higher representations do only lead to  $\mathcal{O}_6$  at the loop level, being  $c_6$  therefore very small to modify the EWPT), new symmetries can make all operators other than those modifying the scalar potential vanish. Such models still contain charged particles that can be produced in pairs via Drell-Yan and then decay into longitudinal polarizations of the gauge bosons. We have shown that even in the particular case of a custodial quadruplet, the LHC reach is far smaller than that of LISA.

# Acknowledgments

We are grateful to Florian Staub for useful support on SARAH. MC acknowledges AEC for hospitality during the first state of this project. CK thanks Andrew J. Long for discussions about the effective potential, and the Enrico Fermi Institute at the University of Chicago and Fermi National Laboratory for hospitality, where parts of this research was carried out. CK acknowledges also fruitful discussions at the LHCPHENO 2017 workshop at IFIC Valencia. MC is supported by the Royal Society under the Newton International Fellowships programme. The work of CK is supported in part by the Spanish Government and ERDF funds from the EU Commission [Grants No. FPA2014-53631-C2-1-P and SEV-2014-0398],

by the Alexander von Humboldt-Foundation, and by the Fermi Research Alliance, LLC under Contract No. DE-AC02-07CH11359 with the U.S. Department of Energy, Office of Science, Office of High Energy Physics. GN is financed by the Swiss National Science Foundation (SNF) under grant 200020-168988.

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] ATLAS and CMS collaborations, *Measurements of the Higgs boson production and decay rates and constraints on its couplings* from a combined ATLAS and CMS analysis of the LHC pp collision data at  $\sqrt{s} = 7$  and 8 TeV, JHEP **08** (2016) 045 [arXiv:1606.02266] [INSPIRE].  
[2] E. Witten, *Cosmic separation of phases*, Phys. Rev. D **30** (1984) 272 [INSPIRE].  
[3] C.J. Hogan, Gravitational radiation from cosmological phase transitions, Mon. Not. Roy. Astron. Soc. 218 (1986) 629 [INSPIRE].  
[4] M. Kamionkowski, A. Kosowsky and M.S. Turner, Gravitational radiation from first order phase transitions, Phys. Rev. D 49 (1994) 2837 [astro-ph/9310044] [INSPIRE].  
[5] K. Kajantie, M. Laine, K. Rummukainen and M.E. Shaposhnikov, Is there a hot electroweak phase transition at  $m_H$  larger or equal to  $m_W$ ?, Phys. Rev. Lett. 77 (1996) 2887 [hep-ph/9605288] [INSPIRE].  
[6] K. Rummukainen, M. Tsypin, K. Kajantie, M. Laine and M.E. Shaposhnikov, The universality class of the electroweak theory, Nucl. Phys. B 532 (1998) 283 [hep-lat/9805013] [INSPIRE].  
[7] M. Laine and K. Rummukainen, What's new with the electroweak phase transition?, Nucl. Phys. Proc. Suppl. 73 (1999) 180 [hep-lat/9809045] [INSPIRE].  
[8] F. Csikor, Z. Fodor and J. Heitger, Endpoint of the hot electroweak phase transition, Phys. Rev. Lett. 82 (1999) 21 [hep-ph/9809291] [INSPIRE].  
[9] P. Creminelli, A. Nicolis and R. Rattazzi, Holography and the electroweak phase transition, JHEP 03 (2002) 051 [hep-th/0107141] [INSPIRE].  
[10] L. Randall and G. Servant, Gravitational waves from warped spacetime, JHEP 05 (2007) 054 [hep-ph/0607158] [INSPIRE].  
[11] G. Nardini, M. Quiros and A. Wulzer, A confining strong first-order electroweak phase transition, JHEP 09 (2007) 077 [arXiv:0706.3388] [INSPIRE].  
[12] T. Konstandin, G. Nardini and M. Quiros, Gravitational backreaction effects on the holographic phase transition, Phys. Rev. D 82 (2010) 083513 [arXiv:1007.1468] [INSPIRE].  
[13] E. Megías, G. Nardini and M. Quiós, Cosmological phase transitions in warped space: gravitational waves and collider signatures, arXiv:1806.04877 [INSPIRE].  
[14] J. García-Bellido, D. Yu. Grigoriev, A. Kusenko and M.E. Shaposhnikov, Nonequilibrium electroweak baryogenesis from preheating after inflation, Phys. Rev. D 60 (1999) 123504 [hep-ph/9902449] [INSPIRE].

[15] L.M. Krauss and M. Trodden, Baryogenesis below the electroweak scale, Phys. Rev. Lett. 83 (1999) 1502 [hep-ph/9902420] [INSPIRE].  
[16] J. García-Bellido, M. Garcia Perez and A. Gonzalez-Arroyo, Symmetry breaking and false vacuum decay after hybrid inflation, Phys. Rev. D 67 (2003) 103501 [hep-ph/0208228] [INSPIRE].  
[17] J. Smit and A. Tranberg, Chern-Simons number asymmetry from CP-violation at electroweak tachyonic preheating, JHEP 12 (2002) 020 [hep-ph/0211243] [INSPIRE].  
[18] T. Konstandin and G. Servant, Natural cold baryogenesis from strongly interacting electroweak symmetry breaking, JCAP 07 (2011) 024 [arXiv:1104.4793] [INSPIRE].  
[19] S. ArunaSalam, A. Kobakhidze, C. Lagger, S. Liang and A. Zhou, Low temperature electroweak phase transition in the Standard Model with hidden scale invariance, Phys. Lett. B 776 (2018) 48 [arXiv:1709.10322] [INSPIRE].  
[20] B. von Harling and G. Servant, QCD-induced electroweak phase transition, JHEP 01 (2018) 159 [arXiv:1711.11554] [INSPIRE].  
[21] M. Quiros, Finite temperature field theory and phase transitions, in Proceedings, Summer School in high-energy physics and cosmology, Trieste, Italy, 29 June-17 July 1998, pg. 187 [hep-ph/9901312] [INSPIRE].  
[22] D.E. Morrissey and M.J. Ramsey-Musolf, Electroweak baryogenesis, New J. Phys. 14 (2012) 125003 [arXiv:1206.2942] [INSPIRE].  
[23] X.-M. Zhang, Operators analysis for Higgs potential and cosmological bound on Higgs mass, Phys. Rev. D 47 (1993) 3065 [hep-ph/9301277] [INSPIRE].  
[24] C. Grojean, G. Servant and J.D. Wells, First-order electroweak phase transition in the Standard Model with a low cutoff, Phys. Rev. D 71 (2005) 036001 [hep-ph/0407019] [INSPIRE].  
[25] D. Bödeker, L. Fromme, S.J. Huber and M. Seniuch, The baryon asymmetry in the Standard Model with a low cut-off, JHEP 02 (2005) 026 [hep-ph/0412366] [INSPIRE].  
[26] C. Delaunay, C. Grojean and J.D. Wells, Dynamics of non-renormalizable electroweak symmetry breaking, JHEP 04 (2008) 029 [arXiv:0711.2511] [INSPIRE].  
[27] B. Grinstein and M. Trott, Electroweak baryogenesis with a pseudo-Goldstone Higgs, Phys. Rev. D 78 (2008) 075022 [arXiv:0806.1971] [INSPIRE].  
[28] P.H. Damgaard, A. Haarr, D. O'Connell and A. Tranberg, Effective field theory and electroweak baryogenesis in the singlet-extended Standard Model, JHEP 02 (2016) 107 [arXiv:1512.01963] [INSPIRE].  
[29] J. de Vries, M. Postma, J. van de Vis and G. White, Electroweak baryogenesis and the Standard Model effective field theory, JHEP 01 (2018) 089 [arXiv:1710.04061] [INSPIRE].  
[30] M. Laine and A. Vuorinen, Basics of thermal field theory, Lect. Notes Phys. 925 (2016) 1 [arXiv:1701.01554] [INSPIRE].  
[31] D.J.H. Chung, A.J. Long and L.-T. Wang, 125 GeV Higgs boson and electroweak phase transition model classes, Phys. Rev. D 87 (2013) 023509 [arXiv:1209.1819] [INSPIRE].  
[32] E. Greenwood, E. Halstead, R. Poltis and D. Stojkovic, Dark energy, the electroweak vacua and collider phenomenology, Phys. Rev. D 79 (2009) 103003 [arXiv:0810.5343] [INSPIRE].

[33] C.L. Wainwright, CosmoTransitions: computing cosmological phase transition temperatures and bubble profiles with multiple fields, Comput. Phys. Commun. 183 (2012) 2006 [arXiv:1109.4189] [INSPIRE].  
[34] M. Chala, G. Nardini and I. Sobolev, Unified explanation for dark matter and electroweak baryogenesis with direct detection and gravitational wave signatures, Phys. Rev. D 94 (2016) 055006 [arXiv:1605.08663] [INSPIRE].  
[35] S.J. Huber and M. Sopena, An efficient approach to electroweak bubble velocities, arXiv:1302.1044 [INSPIRE].  
[36] T. Konstandin, G. Nardini and I. Rues, From Boltzmann equations to steady wall velocities, JCAP 09 (2014) 028 [arXiv:1407.3132] [INSPIRE].  
[37] L. Leitao and A. Megevand, Hydrodynamics of phase transition fronts and the speed of sound in the plasma, Nucl. Phys. B 891 (2015) 159 [arXiv:1410.3875] [INSPIRE].  
[38] D. Bödeker and G.D. Moore, Can electroweak bubble walls run away?, JCAP 05 (2009) 009 [arXiv:0903.4099] [INSPIRE].  
[39] D. Bödeker and G.D. Moore, Electroweak bubble wall speed limit, JCAP 05 (2017) 025 [arXiv:1703.08215] [INSPIRE].  
[40] C. Caprini et al., Science with the space-based interferometer eLISA. II: gravitational waves from cosmological phase transitions, JCAP 04 (2016) 001 [arXiv:1512.06239] [INSPIRE].  
[41] LISA collaboration, H. Audley et al., Laser Interferometer Space Antenna, arXiv:1702.00786 [INSPIRE].  
[42] S. Di Vita, C. Grojean, G. Panico, M. Riembau and T. Vantalon, A global view on the Higgs self-coupling, JHEP 09 (2017) 069 [arXiv:1704.01953] [INSPIRE].  
[43] S. Di Vita et al., A global view on the Higgs self-coupling at lepton colliders, JHEP 02 (2018) 178 [arXiv:1711.03978] [INSPIRE].  
[44] J.H. Kim, Y. Sakaki and M. Son, Combined analysis of double Higgs production via gluon fusion at the HL-LHC in the effective field theory approach, arXiv:1801.06093 [INSPIRE].  
[45] TLEP DESIGN STUDY WORKING GROUP collaboration, M. Bicer et al., First look at the physics case of TLEP, JHEP 01 (2014) 164 [arXiv:1308.6176] [INSPIRE].  
[46] A. Papaefstathiou and K. Sakurai, *Triple Higgs boson production at a 100 TeV proton-proton collider*, JHEP **02** (2016) 006 [arXiv:1508.06524] [INSPIRE].  
[47] B. Grzadkowski, M. Iskrzynski, M. Misiak and J. Rosiek, Dimension-six terms in the Standard Model Lagrangian, JHEP 10 (2010) 085 [arXiv:1008.4884] [INSPIRE].  
[48] J. de Blas, M. Chala, M. Pérez-Victoria and J. Santiago, Observable effects of general new scalar particles, JHEP 04 (2015) 078 [arXiv:1412.8480] [INSPIRE].  
[49] Y. Jiang and M. Trot, On the non-minimal character of the SMEFT, Phys. Lett. B 770 (2017) 108 [arXiv:1612.02040] [INSPIRE].  
[50] J. de Blas, J.C. Criado, M. Pérez-Victoria and J. Santiago, Effective description of general extensions of the Standard Model: the complete tree-level dictionary, JHEP 03 (2018) 109 [arXiv:1711.10391] [INSPIRE].  
[51] J. de Blas, O. Eberhardt and C. Krause, Current and future constraints on Higgs couplings in the nonlinear effective theory, arXiv:1803.00939 [INSPIRE].

[52] R. Alonso, E.E. Jenkins, A.V. Manohar and M. Trott, Renormalization group evolution of the Standard Model dimension six operators III: gauge coupling dependence and phenomenology, JHEP 04 (2014) 159 [arXiv:1312.2014] [INSPIRE].  
[53] J. de Blas, Electroweak limits on physics beyond the Standard Model, EPJ Web Conf. 60 (2013) 19008 [arXiv:1307.6173] [INSPIRE].  
[54] Q.-H. Cao, F.P. Huang, K.-P. Xie and X. Zhang, Testing the electroweak phase transition in scalar extension models at lepton colliders, Chin. Phys. C 42 (2018) 023103 [arXiv:1708.04737] [INSPIRE].  
[55] L. Di Luzio, R. Gröber and M. Spannowsky, Maxi-sizing the trilinear Higgs self-coupling: how large could it be?, Eur. Phys. J. C 77 (2017) 788 [arXiv:1704.02311] [INSPIRE].  
[56] M. Chala, G. Durieux, C. Grojean, L. de Lima and O. Matsedonskyi, Minimally extended SILH, JHEP 06 (2017) 088 [arXiv:1703.10624] [INSPIRE].  
[57] L. Vecchi, A dangerous irrelevant UV-completion of the composite Higgs, JHEP 02 (2017) 094 [arXiv:1506.00623] [INSPIRE].  
[58] G. Ferretti and D. Karateev, Fermionic UV completions of composite Higgs models, JHEP 03 (2014) 077 [arXiv:1312.5330] [INSPIRE].  
[59] H. Georgi and M. Machacek, Doubly charged Higgs bosons, Nucl. Phys. B 262 (1985) 463 [INSPIRE].  
[60] R. Slansky, Group theory for unified model building, Phys. Rept. 79 (1981) 1 [INSPIRE].  
[61] R. Feger and T.W. Kephart, LieART — a Mathematica application for Lie algebras and representation theory, Comput. Phys. Commun. 192 (2015) 166 [arXiv:1206.6379] [INSPIRE].  
[62] E. Witten, Mass hierarchies in supersymmetric theories, Phys. Lett. B 105 (1981) 267 [INSPIRE].  
[63] G.R. Dvali, Why is the Higgs doublet light?, Phys. Lett. B 324 (1994) 59 [INSPIRE].  
[64] H. Georgi, An almost realistic gauge hierarchy, Phys. Lett. B 108 (1982) 283 [INSPIRE].  
[65] A. Masiero, D.V. Nanopoulos, K. Tamvakis and T. Yanagida, Naturally massless Higgs doublets in supersymmetric SU(5), Phys. Lett. B 115 (1982) 380 [INSPIRE].  
[66] K.S. Babu, I. Gogoladze and Z. Tavartkiladze, Missing partner mechanism in SO(10) grand unification, Phys. Lett. B 650 (2007) 49 [hep-ph/0612315] [INSPIRE].  
[67] K.S. Babu and S.M. Barr, Natural suppression of Higgsino mediated proton decay in supersymmetric SO(10), Phys. Rev. D 48 (1993) 5354 [hep-ph/9306242] [INSPIRE].  
[68] K.S. Babu, S. Nandi and Z. Tavartkiladze, New mechanism for neutrino mass generation and triply charged Higgs bosons at the LHC, Phys. Rev. D 80 (2009) 071702 [arXiv:0905.2710] [INSPIRE].  
[69] K. Ghosh, S. Jana and S. Nandi, Neutrino mass generation and 750 GeV diphoton excess via photon-photon fusion at the Large Hadron Collider, arXiv:1607.01910 [INSPIRE].  
[70] PARTICLE DATA GROUP collaboration, C. Patrignani et al., Review of particle physics, Chin. Phys. C 40 (2016) 100001 [INSPIRE].  
[71] H.E. Logan and V. Rental, All the generalized Georgi-Machacek models, Phys. Rev. D 92 (2015) 075011 [arXiv:1502.01275] [INSPIRE].

[72] F. Staub, SARAH 4: a tool for (not only SUSY) model builders, Comput. Phys. Commun. 185 (2014) 1773 [arXiv:1309.7223] [INSPIRE].  
[73] J. Alwall et al., The automated computation of tree-level and next-to-leading order differential cross sections and their matching to parton shower simulations, JHEP 07 (2014) 079 [arXiv:1405.0301] [INSPIRE].  
[74] A. Alloul, N.D. Christensen, C. Degrande, C. Duhr and B. Fuks, *FeynRules* 2.0 — a complete toolbox for tree-level phenomenology, *Comput. Phys. Commun.* **185** (2014) 2250 [arXiv:1310.1921] [INSPIRE].  
[75] T. Sjöstrand, S. Mrenna and P.Z. Skands, PYTHIA 6.4 physics and manual, JHEP 05 (2006) 026 [hep-ph/0603175] [INSPIRE].  
[76] D. Dercks, N. Desai, J.S. Kim, K. Rolbiecki, J. Tattersall and T. Weber, CheckMATE 2: from the model to the limit, Comput. Phys. Commun. 221 (2017) 383 [arXiv:1611.09856] [INSPIRE].  
[77] ATLAS collaboration, Search for supersymmetry with two and three leptons and missing transverse momentum in the final state at  $\sqrt{s} = 13$  TeV with the ATLAS detector, ATLAS-CONF-2016-096, CERN, Geneva, Switzerland, (2016).  
[78] J. Alcaide, M. Chala and A. Santamaria, LHC signals of radiatively-induced neutrino masses and implications for the Zee-Babu model, Phys. Lett. B 779 (2018) 107 [arXiv:1710.05885] [INSPIRE].  
[79] F. Feruglio, The chiral approach to the electroweak interactions, Int. J. Mod. Phys. A 8 (1993) 4937 [hep-ph/9301281] [INSPIRE].  
[80] J. Bagger et al., The strongly interacting WW system: gold plated modes, Phys. Rev. D 49 (1994) 1246 [hep-ph/9306256] [INSPIRE].  
[81] V. Koulovassilopoulos and R.S. Chivukula, The phenomenology of a nonstandard Higgs boson in  $W_{L}W_{L}$  scattering, Phys. Rev. D 50 (1994) 3218 [hep-ph/9312317] [INSPIRE].  
[82] C.P. Burgess, J. Matias and M. Pospelov, A Higgs or not a Higgs? What to do if you discover a new scalar particle, Int. J. Mod. Phys. A 17 (2002) 1841 [hep-ph/9912459] [INSPIRE].  
[83] L.-M. Wang and Q. Wang, Electroweak chiral Lagrangian for neutral Higgs boson, Chin. Phys. Lett. 25 (2008) 1984 [hep-ph/0605104] [INSPIRE].  
[84] B. Grinstein and M. Trott, A Higgs-Higgs bound state due to new physics at a TeV, Phys. Rev. D 76 (2007) 073002 [arXiv:0704.1505] [INSPIRE].  
[85] R. Contino, C. Grojean, M. Moretti, F. Piccinini and R. Rattazzi, *Strong double Higgs production at the LHC*, JHEP **05** (2010) 089 [arXiv:1002.1011] [INSPIRE].  
[86] R. Contino, The Higgs as a composite Nambu-Goldstone boson, in Physics of the large and the small, TASI 09, proceedings of the Theoretical Advanced Study Institute in Elementary Particle Physics, Boulder, CO, U.S.A., 1-26 June 2009, World Scientific, Singapore, (2011), pg. 235 [arXiv:1005.4269] [INSPIRE].  
[87] A. Azatov, R. Contino and J. Galloway, Model-independent bounds on a light Higgs, JHEP 04 (2012) 127 [Erratum ibid. 04 (2013) 140] [arXiv:1202.3415] [INSPIRE].  
[88] R. Alonso, M.B. Gavela, L. Merlo, S. Rigolin and J. Yepes, The effective chiral Lagrangian for a light dynamical "Higgs particle", Phys. Lett. B 722 (2013) 330 [Erratum ibid. B 726 (2013) 926] [arXiv:1212.3305] [INSPIRE].

[89] G. Buchalla and O. Catà, Effective theory of a dynamically broken electroweak Standard Model at NLO, JHEP 07 (2012) 101 [arXiv:1203.6510] [INSPIRE].  
[90] G. Buchalla, O. Catà and C. Krause, Complete electroweak chiral Lagrangian with a light Higgs at NLO, Nucl. Phys. B 880 (2014) 552 [Erratum ibid. B 913 (2016) 475] [arXiv:1307.5017] [INSPIRE].  
[91] G. Buchalla, O. Càà and C. Krause, On the power counting in effective field theories, Phys. Lett. B 731 (2014) 80 [arXiv:1312.5624] [INSPIRE].  
[92] T. Appelquist and C.W. Bernard, Strongly interacting Higgs bosons, Phys. Rev. D 22 (1980) 200 [INSPIRE].  
[93] A.C. Longhitano, Low-energy impact of a heavy Higgs boson sector, Nucl. Phys. B 188 (1981) 118 [INSPIRE].  
[94] A. Dobado, D. Espriu and M.J. Herrero, Chiral Lagrangians as a tool to probe the symmetry breaking sector of the SM at LEP, Phys. Lett. B 255 (1991) 405 [INSPIRE].  
[95] M.J. Herrero and E. Ruiz Morales, The electroweak chiral Lagrangian for the Standard Model with a heavy Higgs, Nucl. Phys. B 418 (1994) 431 [hep-ph/9308276] [INSPIRE].  
[96] S. Weinberg, Phenomenological Lagrangians, Physica A 96 (1979) 327 [INSPIRE].  
[97] G. Buchalla, O. Catà and C. Krause, A systematic approach to the SILH Lagrangian, Nucl. Phys. B 894 (2015) 602 [arXiv:1412.6356] [INSPIRE].  
[98] G.F. Giudice, C. Grojean, A. Pomarol and R. Rattazzi, The strongly-interacting light Higgs, JHEP 06 (2007) 045 [hep-ph/0703164] [INSPIRE].  
[99] G. Buchalla, O. Cata, A. Celis and C. Krause, Fitting Higgs data with nonlinear effective theory, Eur. Phys. J. C 76 (2016) 233 [arXiv:1511.00988] [INSPIRE].  
[100] V. Sanz and J. Setford, Composite Higgs models after run 2, Adv. High Energy Phys. 2018 (2018) 7168480 [arXiv:1703.10190] [INSPIRE].  
[101] G. Panico and A. Wulzer, The composite Nambu-Goldstone Higgs, Lect. Notes Phys. 913 (2016) 1 [arXiv:1506.01961] [INSPIRE].  
[102] G. Buchalla, O. Catà, A. Celis and C. Krause, Comment on “analysis of general power counting rules in effective field theory”, arXiv:1603.03062 [INSPIRE].  
[103] A. Azatov, R. Contino, G. Panico and M. Son, Effective field theory analysis of double Higgs boson production via gluon fusion, Phys. Rev. D 92 (2015) 035001 [arXiv:1502.00539] [INSPIRE].  
[104] G. Buchalla, O. Cata, A. Celis and C. Krause, Standard Model extended by a heavy singlet: linear vs. nonlinear EFT, Nucl. Phys. B 917 (2017) 209 [arXiv:1608.03564] [INSPIRE].  
[105] G. Buchalla, O. Catà, A. Celis and C. Krause, Note on anomalous Higgs-boson couplings in effective field theory, Phys. Lett. B 750 (2015) 298 [arXiv:1504.01707] [INSPIRE].  
[106] C.P. Burgess, H.M. Lee and M. Trot, Comment on Higgs inflation and naturalness, JHEP 07 (2010) 007 [arXiv:1002.2730] [INSPIRE].  
[107] G. Passarino and M. Trott, The Standard Model effective field theory and next to leading order, arXiv:1610.08356 [INSPIRE].  
[108] R. Grober, M. Muhlleitner, M. Spira and J. Streicher, NLO QCD corrections to Higgs pair production including dimension-6 operators, JHEP 09 (2015) 092 [arXiv:1504.06577] [INSPIRE].