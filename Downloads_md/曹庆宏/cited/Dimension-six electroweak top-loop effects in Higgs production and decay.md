# Dimension-six electroweak top-loop effects in Higgs production and decay

# Eleni Vryonidou<sup>a</sup> and Cen Zhang<sup>b</sup>

${}^{a}$  CERN,Theoretical Physics Department,

Geneva 23 CH-1211, Switzerland

$^b$ Institute of High Energy Physics and School of Physical Sciences,

University of Chinese Academy of Sciences,

P.O. Box 918-4, Beijing, P.R. China

E-mail: eleni.vryonidou@cern.ch, cenzhang@ihep.ac.cn

ABSTRACT: We study the next-to-leading order electroweak corrections to Higgs processes from dimension-six top-quark operators in the Standard Model Effective Field Theory approach. We consider the major production channels, including  $WH$ ,  $ZH$ , and VBF production at the LHC, and  $ZH$ , VBF production at future lepton colliders, as well as the major decay channels including  $H \rightarrow \gamma \gamma, \gamma Z, Wl\nu, Zll, b\bar{b}, \mu \mu, \tau \tau$ . The results show that within the current constraints, top-quark operators can shift the signal strength of the loop-induced processes, i.e.  $H \rightarrow \gamma \gamma, \gamma Z$ , by factors of  $\sim \mathcal{O}(1) - \mathcal{O}(10)$ , and that of the tree-level processes, i.e. all remaining production and decay channels, by  $\sim 5 - 10\%$  at the LHC, and up to  $\sim 15\%$  at future lepton colliders. This implies that essentially all Higgs channels have started to become sensitive to top-quark couplings, and in particular, Higgs observables at high luminosity LHC as well as future lepton colliders, even below the  $t\bar{t}$  threshold, will improve our knowledge of top-quark couplings. We derive the sensitivities of Higgs measurements to top-quark operators at the high luminosity LHC, using projections for both inclusive and differential measurements. We conclude that treating the dimension-six top-quark sector and the Higgs/electroweak sector separately may not continue to be a good strategy. A global analysis combining Higgs and top-quark measurements is desirable, and our calculation and implementation provide an automatic and realistic simulation tool for this purpose.

KEYWORDS: Heavy Quark Physics, Higgs Physics, Effective Field Theories, Beyond Standard Model

ARXIV EPRINT: 1804.09766

# Contents

1 Introduction 1  
2 Operators 5

3 Calculation and renormalisation 6

3.1 Dim-6 renormalisation 8  
3.2 SM renormalisation 9  
3.3 Counter terms 11

4 Numerical results 12  
5 Physics implications 16

5.1 Impact on Higgs measurements at the LHC 16  
5.2 Impact on Higgs measurements at the future lepton colliders 17  
5.3 Potential at high luminosity LHC 19  
5.4 Improvements with differential distributions 24  
5.5 Loop/tree discrimination 28

6 Conclusion 30  
A More numerical results 31

# 1 Introduction

Deviations in the top-quark and Higgs couplings are often studied within the Standard Model Effective Field Theory (SMEFT) approach [1-3]. Even though the SMEFT is a global approach where different measurements are supposed to be combined and studied together, in practice, several main sectors are often considered separately. Dimension-six (dim-6) operators in the top-quark sector are analysed with top measurements [4-15], while those in the Higgs sector are analysed with Higgs and triple gauge-boson coupling (TGC) measurements [16-23], the rationale behind being that the interplay between the two sectors is negligible with the accuracy of the current measurements.

This assumption may not continue to be true as the LHC experiments improve on higher integrated luminosities and higher energies. Once the precision reaches the point where loop corrections become relevant, the top- and the Higgs-sectors should not be viewed separately. In particular, top-quark operators could play a role in Higgs measurements through electroweak (EW) top and bottom loops and have non-trivial impacts. The goal of this paper is to answer the following two questions: 1) will this happen at the LHC,

![](images/ae257d025730dd8dfa2c8e33dab9e52eb843a9275d07651ed0c6a6869d31e6c2.jpg)  
WH,ZH

![](images/128b317c9f9b19c301265897d84276a1c85615ee61ada07832ee88e87cad5e93.jpg)  
VBF

![](images/2e06525faa18215f3620cba408aa1954cc07f2ed15ffbb78c8b8dd995500e32d.jpg)  
H>μμ,τT

![](images/b40cbd7f91d967665ede14b0ce6e46a73fa77daca96bda1006c4fe672c20a661.jpg)  
W,Z masses, oblique paretmers

![](images/09c690c3fd1ded130736f4789f2fcecc1c80f5a7004c9f16e3206b86aea8f536.jpg)  
H→γγ,γZ

![](images/3892892bb83fcbac83c8244b4c3e28df1cfe925f84d80ce6d8a646a8edc8d623.jpg)  
$\mathrm{H}\rightarrow \mathrm{ZII},\mathrm{WIV}$

![](images/4296142b5a980c7126a4293ffe86dabd96395aec114c912315614ccd9fe92997.jpg)  
$\mathrm{H}\rightarrow \mathrm{bb}$

![](images/67831dcfbf082effb7ee64a25ec2a6643219653215653bfeda8d3448f692f93c.jpg)  
$\mu$  decay

![](images/4ff3d11d70a4f36c48f061abcc08fdba8074bce1effc0cee4754f87f5c200ccf.jpg)

![](images/3b1bcb8fae0ab8ad223289ad65dd0ccdcb19cd9ffdabb9b433bab41f14b9396d.jpg)

![](images/3de4fa7623a3bdfa8999968f44b2bdf0789ef2226a649a00e697b1d564776a03.jpg)

![](images/9a9ef5964b7ce8c017203458613b635095d229cc8b9f062df3a7b8d30026ff1f.jpg)  
Figure 1. Electroweak contributions from two-fermion top-quark operators to the production and decay of the Higgs boson, the oblique parameters, and the SM input parameters which we will take as  $M_W$ ,  $M_Z$  and  $G_F$  (from muon decay). Here blue fermion lines represent light fermions, and red fermion lines represent the top quark. Large grey blobs denote collectively the SM contributions and dim-6 EW corrections from top-quark loops, as illustrated below the processes. Dark small blobs represent the dim-6 operator insertions. Diagrams that can be obtained by crossing legs or reversing fermion flows are not shown.

and/or future lepton colliders? and 2) can Higgs measurements help to constrain top-quark couplings?

To answer these two questions, in this work we compute the EW loop-induced contributions from dim-6 top-quark two-fermion operators in the following main Higgs production and decay processes:

production at LHC: VBF, WH, ZH

production at lepton collider:  $ZH$ , VBF

decay:  $H\to \gamma \gamma$ $\gamma Z$ $Wl\nu$ $Zll$ $b\bar{b}$ $\mu^{+}\mu^{-}$ $\tau^{+}\tau^{-}$

All relevant contributions are shown in figure 1.

Loop corrections in the SMEFT with dim-6 operators have been studied in the literature. The loop contributions in  $gg \to H$  and  $H \to gg$  have been presented in [24, 25]. Top loop induced  $gg \to ZH$ ,  $gg \to HH$  and  $gg \to Hj$  have also been considered in [26-28]. Some of the decay processes, including  $H \to WW^*$ ,  $ZZ^*$ ,  $\gamma \gamma$  and  $Z\gamma$ , have been studied in

refs. [29-32]. All other results in this work, in particular the next-to-leading order (NLO) EW corrections for the production channels, are new and are relevant for future Higgs and top studies at the LHC. Note that loop corrections to  $H \rightarrow b\bar{b}$  and  $\tau^{+}\tau^{-}$  from fourfermion operators have been computed in [33], while the NLO QCD corrections to  $WH$ ,  $ZH$ , VBF and  $t\bar{t}H$  production processes are also known [28, 34, 35], but they are not relevant for the purpose of this work. We do not consider  $t\bar{t}H$  production because its leading contribution comes from the tree level top Yukawa operator. Our approach is based on the MadGraph5_aMC@NLO (MG5_aMC) framework [36]. It is part of the ongoing efforts of automating NLO EFT simulations for colliders [26, 28, 35, 37-41], and is a first step towards including NLO EW corrections.

Formally, the top loop contributions in Higgs measurements are part of the NLO EW corrections to the dim-6 operators. One might think that the effects must be small relative to the tree level contributions from other EW and Higgs operators. However, they could be important because the top quark operators enter for the first time at the one-loop level, and in this sense these are leading order (LO) contributions. Therefore it is important to know their sizes. An interesting and similar example in the Higgs sector is that one can set bounds on the Higgs self coupling  $\lambda_{3}$ , by using the  $\lambda_{3}$ -dependent EW corrections, which enter the single Higgs boson cross section starting at the one-loop level [42-46]. The problem we consider in this work is in analogy. The one-loop contribution of some top operator,  $O_{t}$ , relative to the tree level ones from another, say, Higgs operator  $O_{H}$ , are proportional to the ratio of their coefficients, i.e.  $\mathcal{O}(\alpha_{EW}C_t / C_H)$  instead of just  $\mathcal{O}(\alpha_{EW})$ . Given that the current constraints on the Higgs operators are in general much stronger than those on the top operators, it is likely that the  $C_t / C_H$  factor enhances the top-loop induced contributions, so that they are of more physical relevance. This is one of the reasons why we would like to focus on the top-quark operators at one loop instead of the regular NLO EW corrections to Higgs and EW operators, as the latter are naively of order  $\mathcal{O}(\alpha_{EW})$ , and therefore less important. Another reason is that there are processes that are loop-induced in the SM, such as  $gg \rightarrow H$  and  $H \rightarrow \gamma \gamma$ , and for them the top-loop induced dim-6 contributions are not small.

The above arguments also apply to other non-top operators, which could enter Higgs processes at one-loop. While their effects could be potentially interesting, in this work we are mostly interested in top and Higgs physics, and so we start with the interplay of these two classes of operators. This is a first step justified by the fact that the top quark has the strongest coupling to Higgs. If non-top operators contribute to Higgs processes at one loop, it is more likely that these effects are better constrained by processes without a Higgs, to such a level that their loop contributions are not important in Higgs measurements. This is not the case for top-quark operators due to the large Yukawa coupling of the top quark.

The collider sensitivity to the loop contributions from effective operators may depend on our assumptions. Let us briefly comment on this. Once including one-loop top operator contributions, the cross section (or decay width) of the Higgs boson takes the following form:

$$
\sigma = C _ {H} \left(\mu_ {E F T}\right) \sigma_ {\text {t r e e}} + C _ {t} \frac {\alpha_ {E W}}{\pi} \left(\log \frac {Q ^ {2}}{\mu_ {E F T} ^ {2}} \sigma_ {\log} + \sigma_ {\text {f i n}}\right) \tag {1.1}
$$

where  $C_H(\mu_{EFT})$  is the coefficient of some Higgs operator,  $O_H$ , that enters the process at

the tree level and  $\mu_{EFT}$  is the scale at which it is defined.  $C_t$  is the coefficient of some top-quark operator  $O_t$  which mixes into  $O_H$ .  $Q^2$  is the energy of the process. A measurement of  $\sigma$  will give us information about a linear combination of  $C_H$  and  $C_t$ . Even though one cannot immediately infer the constraint on  $C_t$ , this piece of information itself is already useful, as it can be combined with other measurements, and eventually the degeneracy will be lifted. It is however important to have all measured quantities in such a fit expressed in terms of operator coefficients defined at a common scale  $\mu_{EFT}$ , as one can clearly see from eq. (1.1), the linear combination of  $C_H$  and  $C_t$  depends on the scale  $\mu_{EFT}$ .

In this work, as a first step, we will focus on studying the collider sensitivity to the loop effects. We do not perform any global fit, and we will ignore the  $C_H$  coefficient, except for two Higgs operators which we will use as examples to demonstrate that distinguishing between tree-level and loop-level contributions is in principle possible only by using Higgs data. The consequence of neglecting  $C_H$  is that the experimental sensitivity on  $C_t$  depends on the scale  $\mu_{EFT}$  at which  $C_H$  is set to 0. We consider two options:

- Take  $\mu_{EFT} = \Lambda$ . The underlying assumption is that new physics effects at high scale are mainly captured by top-quark operators. The large scale  $\mu_{EFT}$  in this case can be considered as a proxy of renormalisation group (RG) running and mixing effects to the scale of measurement. The contributions from  $C_t$  will be relatively large due to the logarithmic terms, leading to relatively tighter limits. This however does not mean that the finite terms are not important, see for example discussions in [28, 29, 40]. The disadvantage of this approach is that resulting limits rely on strong assumptions, and in particular it is difficult to combine these limits with other analyses, as the assumptions at scale  $\Lambda$  can be different.  
- Take  $\mu_{EFT}^2 = Q^2$ , where  $Q$  is the scale of the measurement. This is a bottom-up point of view, where the coefficient  $C_H$  is assumed to have already evolved down to scale  $Q^2$  to absorb the  $\sigma_{\log}$  contributions. The resulting sensitivity will become weaker, but it is a fair estimate of the expected sensitivity in a global analysis. As we will discuss later, this is because the finite terms are crucial for discriminating the top-loop induced effects from the tree-level contributions of other Higgs operators, which cannot be avoided in a real bottom-up global SMEFT fit.

In this work we will present results for both options. For the first we will take  $\mu_{EFT} = \Lambda = 1\mathrm{TeV}$  and for the second  $\mu_{EFT} = m_H = 125\mathrm{GeV}$ . Besides, we will also show that, even with Higgs operators included, by combining observables at different energies or using differential measurements, it is possible to lift the degeneracy between top and Higgs operators. This is because the finite term  $\sigma_{\mathrm{fin}} / \sigma_{\mathrm{tree}}$  is process dependent, unlike the logarithmic term  $\sigma_{\log} / \sigma_{\mathrm{tree}}$ .

While we are mostly interested in LHC physics, for completeness we will also discuss the same effects at possible future lepton colliders. An  $e^{+}e^{-}$  collider is an ideal machine for determining possible deviations in the Higgs sector. Several proposals of such Higgs factories have been made, including the Circular Electron Positron Collider (CEPC) in China [47], the Future Circular Collider with  $e^{+}e^{-}$  (FCC-ee) at CERN [48], and the In

ternational Linear Collider (ILC) in Japan [49]. The Compact Linear Collider (CLIC) at CERN [50] could also run at higher center-of-mass energies. The precision on Higgs signal strengths at these machines could reach  $\mathcal{O}(1\%) - \mathcal{O}(0.1\%)$  level, and therefore one has to carefully investigate possible loop contributions from deviations in the top-quark sector. We will show that our results imply that future lepton colliders will be sensitive to top-quark couplings even below the  $t\bar{t}$  threshold.

This paper is organised as follows. In section 2 we discuss the relevant effective operators in this study. In section 3 we briefly outline our calculation strategy, implementation and validation, and in particular discuss the renormalisation scheme. We present our major numerical results in section 4. Section 5 is devoted to a discussion of the physics implications of our results, including impacts at the LHC, at future lepton colliders, the potential sensitivities at high-luminosity LHC, possible improvements by using differential distributions, and the possibilities to discriminate between tree-level and loop-level operator contributions. In section 6 we conclude.

# 2 Operators

We consider the effective Lagrangian at dim-6

$$
\mathcal {L} _ {E F T} = \mathcal {L} _ {S M} + \sum_ {i} \frac {C _ {i}}{\Lambda^ {2}} O _ {i} + \dots \tag {2.1}
$$

where we consider CP-even operators only. Two classes of operators are relevant in this work. The first is the set of two-fermion top-quark operators that could enter Higgs measurements via loop effects, including [51]

$$
O _ {t \varphi} = \bar {Q} t \tilde {\varphi} (\varphi^ {\dagger} \varphi) + h. c., \qquad \qquad O _ {\varphi Q} ^ {(1)} = (\varphi^ {\dagger} \overleftarrow {i D} _ {\mu} \varphi) (\bar {Q} \gamma^ {\mu} Q),
$$

$$
O _ {\varphi Q} ^ {(3)} = (\varphi^ {\dagger} \stackrel {\leftrightarrow} {i D} _ {\mu} ^ {I} \varphi) (\bar {Q} \gamma^ {\mu} \tau^ {I} Q), \qquad \qquad O _ {\varphi t} = (\varphi^ {\dagger} \stackrel {\leftrightarrow} {i D} _ {\mu} \varphi) (\bar {t} \gamma^ {\mu} t),
$$

$$
O _ {\varphi t b} = (\tilde {\varphi} ^ {\dagger} i D _ {\mu} \varphi) (\bar {t} \gamma^ {\mu} b) + h. c., \qquad O _ {t W} = (\bar {Q} \sigma^ {\mu \nu} \tau^ {I} t) \tilde {\varphi} W _ {\mu \nu} ^ {I} + h. c.,
$$

$$
O _ {t B} = \left(\bar {Q} \sigma^ {\mu \nu} t\right) \tilde {\varphi} B _ {\mu \nu} + h. c., \tag {2.2}
$$

and we define

$$
O _ {\varphi Q} ^ {(+)} \equiv \frac {1}{2} \left(O _ {\varphi Q} ^ {(1)} + O _ {\varphi Q} ^ {(3)}\right) \quad O _ {\varphi Q} ^ {(-)} \equiv \frac {1}{2} \left(O _ {\varphi Q} ^ {(1)} - O _ {\varphi Q} ^ {(3)}\right), \tag {2.3}
$$

so that the operators  $O_{\varphi Q}^{(+)}$  and  $O_{\varphi Q}^{(-)}$  modify the Zbb and Ztt couplings respectively. The coefficient of  $O_{\varphi Q}^{(+)}$  is constrained by the LEP experiment [52], but we include it for a complete study of the loop-induced sensitivity. Four-fermion operators could have similar loop-effects in Higgs measurements, but we will leave them for future study. The chromodipole operator,

$$
O _ {t G} = \left(\bar {Q} \sigma^ {\mu \nu} T ^ {A} t\right) \tilde {\varphi} G _ {\mu \nu} ^ {A} \tag {2.4}
$$

enters  $ggH$  at one loop. Since its contribution has been studied up to two loops [25], we will not include it in this study. When presenting the physics impact in section 5, the  $ggH$  loop will be included as it is the dominant production channel, but we will only consider the contribution from  $O_{t\varphi}$ , which is a simple rescaling factor.

The above operators are the main objects of this study. To correctly take into account their impact on Higgs measurements, RG running and mixing effects [53-55] need to be considered. We thus introduce the second set of operators that enter the same processes at the tree level and will provide the corresponding counter terms:

$$
\begin{array}{l} O _ {\varphi W B} = \varphi^ {\dagger} \tau^ {I} \varphi W _ {\mu \nu} ^ {I} B ^ {\mu \nu}, O _ {\varphi W} = \varphi^ {\dagger} \varphi W _ {\mu \nu} ^ {I} W ^ {I \mu \nu}, \\ O _ {\varphi B} = \varphi^ {\dagger} \varphi B _ {\mu \nu} B ^ {\mu \nu}, \\ O _ {\varphi D} = \left(\varphi^ {\dagger} D ^ {\mu} \varphi\right) ^ {*} \left(\varphi^ {\dagger} D _ {\mu} \varphi\right), \\ O _ {B} = i D ^ {\mu} \varphi^ {\dagger} D ^ {\nu} \varphi B _ {\mu \nu}, \\ O _ {\mu \varphi} = (\varphi^ {\dagger} \varphi) \bar {l} _ {2} e _ {2} \varphi , \quad O _ {\tau \varphi} = (\varphi^ {\dagger} \varphi) \bar {l} _ {3} e _ {3} \varphi , \tag {2.5} \\ \end{array}
$$

where the subscripts 2,3 for the lepton doublet  $l$  and singlet  $e$  are flavour indices. The above operators are sufficient to provide all mixing counter terms needed in this study to guarantee physically meaningful results at the loop level. Note that in the Warsaw basis [51], top quark operators could mix into light-fermion operators, in particular the ones that involve EW gauge bosons. This is slightly inconvenient for a study of the loop-induced Higgs couplings, as some of the counter terms manifest as light-fermion interactions. Fortunately, these effects turn out to be universal, in the sense that they can be captured by dim-6 operators which involve SM bosons only, up to suitable field redefinitions [56]. For this reason, instead of introducing these light-fermion operators in our basis, we follow [57] and include  $O_W$  and  $O_B$  with a slightly different convention. This means we replace the following two combinations of Warsaw basis operators

$$
O _ {\varphi q} ^ {(3)} + O _ {\varphi l} ^ {(3)}, \tag {2.6}
$$

$$
\frac {1}{6} O _ {\varphi q} ^ {(1)} - \frac {1}{2} O _ {\varphi l} ^ {(1)} + \frac {2}{3} O _ {\varphi u} - \frac {1}{3} O _ {\varphi d} - O _ {\varphi e}, \tag {2.7}
$$

by  $O_W$  and  $O_B$ , using the equations of motion. The counter terms provided by them are equivalent, but the physical interpretation is more clear. Note that these two operators project out the flat directions in the precision EW tests [58, 59], and so in this basis it is clear that the precision constraints only apply to two operators, i.e.  $O_{\varphi W B}$  and  $O_{\varphi D}$ , which is convenient for our analysis. Note also that in this basis the mixing pattern of the EW operators becomes different than in the Warsaw basis.

Throughout the paper we will refer to the first class (eq. (2.2)) as top operators, and the second (eq. (2.5)) as Higgs operators.

# 3 Calculation and renormalisation

In this section we briefly describe our calculation for the EW corrections in Higgs processes and precision EW observables from top-quark operators. All relevant Feynman diagrams are shown in figure 1.

At dim-6 at one loop, of all the operators we study, the  $gg \to H$  production and  $H \to gg$  decay channels receive a contribution only from  $O_{t\varphi}$ , which is easy to include with a rescaling factor. All other processes, except for  $H \to bb$ , share the same kinds of contributions from top-loop operators, shown as the large grey circles in figure 1. Thus a very efficient way to obtain results is to implement all these contributions in MG5_aMC [36], with the help of FeynRules [60], and use the reweighting functionality [61] in MG5_aMC to compute the dim-6 loop contributions. The reweighting is particularly simple in this case because there are no real corrections. For the loop computation, we work in the Feynman gauge. Gauge fixing is done following [62], in a way similar to the SM, that cancels the Goldstone-gauge boson mixing and leads to SM-like propagators. In addition we need to provide the corresponding electroweak UV and R2 counter terms. The R2 counter terms need to be provided only for the  $HH$ ,  $VV$  two-point functions and  $HVV$  three-point functions. These are computed by using FeynArts [63] interfaced with FeynCalc [64, 65]. For terms involving  $\gamma^5$  we follow the scheme of [66-68], and have checked that our results for the SM pieces agree with ref. [69]. The UV counter terms come from the renormalisation of the theory, which we will describe in the following subsections. In particular, the UV counter terms needed for our purpose are  $HH$ ,  $VV$ ,  $HVV$ ,  $ffV$ , and  $ffH$ .

Finally,  $h \to bb$  has a unique contribution from  $W - t$  loops, not shared with other channels. We compute it by using FeynArts and FormCalc [70]. The renormalisation is similar to the other channels. For the contribution from the  $O_{\varphi tb}$ , our result for the finite part agrees with that of ref. [9]. We have also repeated our calculation in the  $R_{\xi}$  gauge, and checked that the results are  $\xi$  independent.

The Yukawa operators,  $O_{t\varphi}$ ,  $O_{b\varphi}$ ,  $O_{\mu \varphi}$  and  $O_{\tau \varphi}$  can change the quark and lepton masses already at the tree level. In the on-shell mass scheme these effects should be canceled by redefining the SM Yukawa terms, which is equivalent to making the following replacement:

$$
\varphi^ {\dagger} \varphi \rightarrow \varphi^ {\dagger} \varphi - \frac {v ^ {2}}{2} \tag {3.1}
$$

in their definitions, where  $v$  is the Higgs vev, i.e. they only represent deviations from the SM Yukawa terms. In our calculation we will use the definition after this replacement, and do not consider the dim-6 shift to fermion masses.

Throughout the calculation, we assume that the CKM matrix is identity. We are interested in the main decay channels of the Higgs boson, where quark flavor changing effect does not play a role. Moreover, in top-quark loops, any flavor changing effects are suppressed by two powers of the off-diagonal component of the CKM matrix. For these reasons we believe that an identity CKM matrix is a good approximation for our purpose.

We have validated our implementation by computing the  $H \to 4l$  and  $H \to 2l2\nu$  decay processes and comparing with FormCalc. The implementation provides a simulation tool for all processes shown in figure 1, allowing us to generate events associated with weights corresponding to dim-6 top-loop contributions, apart from  $H \to b\bar{b}$ . Both total rates as well as differential distributions can be efficiently obtained from the weighted events. Note that this implementation can also be used to compute other non-Higgs processes involving

dim-6 top loops, such as  $Z$ -pole processes as well as Drell-Yan at the LHC, provided that no additional counter terms are needed.

# 3.1 Dim-6 renormalisation

The dim-6 operator coefficients can be renormalised using the  $\overline{MS}$  scheme

$$
C _ {i} \Rightarrow Z _ {i j} C _ {j} = C _ {i} + \delta Z _ {i j} C _ {j}, \tag {3.2}
$$

$$
\delta Z _ {i j} = \frac {\alpha}{2 \pi} \Delta \left(\mu_ {E F T}\right) \frac {1}{\epsilon} \gamma_ {i j} \tag {3.3}
$$

with  $\delta Z_{ij}$  the anomalous dimension matrix, which has been obtained in refs. [53-55] in the Warsaw basis. Under our operator basis, the relevant terms in matrix  $\gamma_{ij}$  are:

<table><tr><td></td><td>Oj = Oφt</td><td>O(+)φQ</td><td>O(-)φQ</td><td>Oφtb</td><td>OtW</td><td>OtB</td><td>Otφ</td></tr><tr><td>Oi = OφWB</td><td>1/3sWcW</td><td>1/3sWcW</td><td>-1/6sWcW</td><td>0</td><td>-5yt/2ecW</td><td>-3yt/2esW</td><td>0</td></tr><tr><td>OφD</td><td>-6yt2/e2</td><td>3yt2-b2/e2</td><td>3yt2-b2/e2</td><td>-6yt2b/e2</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Oφ□</td><td>-3yt2/e2</td><td>-3yt2+6yt2/2e2</td><td>6yt2+3yt2/2e2</td><td>3yt2b/e2</td><td>0</td><td>0</td><td>0</td></tr><tr><td>OφW</td><td>0</td><td>1/4s2W</td><td>-1/4s2W</td><td>0</td><td>3yt/2esW</td><td>0</td><td>0</td></tr><tr><td>OφB</td><td>1/3c2W</td><td>1/12c2W</td><td>1/12c2W</td><td>0</td><td>0</td><td>5yt/2ecW</td><td>0</td></tr><tr><td>OW</td><td>0</td><td>1/esW</td><td>-1/esW</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>OB</td><td>4/3ecW</td><td>1/3ecW</td><td>1/3ecW</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="2">Obφ</td><td rowspan="2">0</td><td>-yt/b/2cW</td><td rowspan="2">yb-4λ+3yt2+7yt2/4e2</td><td>3yt/4s2W</td><td rowspan="2">ytby/2esW</td><td rowspan="2">0</td><td rowspan="2">3ytby/4e2</td></tr><tr><td>+yt8λ-3yt2-5yt2/4e2</td><td>-yt2λ+yt2-6yt2/2e2</td></tr><tr><td>Oμφ</td><td>0</td><td>-3ytμ(yt2+yb2)/2e2</td><td>3ytμ(yt2+yb2)/2e2</td><td>3ytbybμ/e2</td><td>0</td><td>0</td><td>3ytbyμ/2e2</td></tr><tr><td>Oτφ</td><td>0</td><td>-3yt(τy2+yb2)/2e2</td><td>3yt(τy2+yb2)/2e2</td><td>3ytbybτ/e2</td><td>0</td><td>0</td><td>3ytbyτ/2e2</td></tr></table>

with

$$
\Delta (x) \equiv \Gamma (1 + \epsilon) \left(\frac {4 \pi \mu^ {2}}{x ^ {2}}\right) ^ {\epsilon}, \tag {3.4}
$$

and the operator coefficients are defined at the scale  $\mu_{EFT}$ . Here the Yukawa couplings are defined by  $y_{t,b} \equiv \sqrt{2} m_{t,b} / v$ .

In this work, we slightly modify the  $\overline{MS}$  scheme, by introducing the oblique parameters  $S$  and  $T$  as renormalisation conditions. This is done by modifying eq. (3.3):

$$
\delta Z _ {i j} = \frac {\alpha}{2 \pi} \Delta \left(\mu_ {E F T}\right) \left(\frac {1}{\epsilon} + \Delta_ {i j}\right) \gamma_ {i j} \tag {3.5}
$$

for  $O_{i} = O_{\varphi WB}, O_{\varphi D}$ , and fixing  $\Delta_{ij}$  by requiring that the dim-6 contribution to  $S$  and  $T$  up to one loop is exactly the measured value. This can be done because we are using a basis which, apart from the top-quark operators that are not relevant in precision EW

tests, includes only oblique operators. Therefore  $S$  and  $T$  can be defined as the outcome of a global fit for the EW sector, under the oblique assumption, as described in [52]. At the tree level, they correspond exactly to the coefficients of  $O_{\varphi WB}$  and  $O_{\varphi D}$ .

The main reason for doing this, is that we are interested in the top-quark loop effects in the directions that do not lead to severe inconsistency with precision EW observables. This implies that  $C_{\varphi WB}$  and  $C_{\varphi D}$  should always take the values that minimise the inconsistency between top-loop effects and precision EW measurements. A complete global fit for the EW sector is required to fully address this problem [14], but in this work we take a simplified approach. We assume BSM effects are dominated by operators in eqs. (2.2)-(2.5), i.e. they are oblique, and so the oblique parameters summarise the main constraints from precision EW observables. The  $S$  and  $T$  parameters can be used to fix the values of  $C_{\varphi WB}$  and  $C_{\varphi D}$ , by simply setting  $S = T = 0$ . This approach implicitly assumes that gauge boson self-energy corrections from top-quark loops are approximately linear functions of  $q^2$ , which is not strictly true, but is enough for a sensitivity study.

In the  $\overline{MS}$  scheme,  $S = T = 0$  does not imply that we can simply drop  $C_{\varphi WB}(\mu_{EFT})$  and  $C_{\varphi D}(\mu_{EFT})$  in our analysis. Instead, due to the top-quark operators contributing to  $S$  and  $T$  at the loop level, this approximation implies that we need to set the coefficients of  $C_{\varphi WB}(\mu_{EFT})$  and  $C_{\varphi D}(\mu_{EFT})$  to values that exactly cancel the contributions from top-quark operators at one loop. These coefficients will then give other contributions in other Higgs processes. A more convenient way to take these additional contributions into account, is simply to use  $S$  and  $T$  as renormalisation conditions, so that the renormalised values for  $C_{\varphi WB}$  and  $C_{\varphi D}$  correspond to the physical values of  $S$  and  $T$ , and so with our approximation they can be excluded from the analysis. The physical results are always independent of renormalisation scheme at the order of this calculation. The numerical results of  $S$  and  $T$  parameters in terms of top operator coefficients are given in section 4.

# 3.2 SM renormalisation

The SM parameters are renormalised in the on-shell scheme, following [71]. In particular, the following parameters are split into renormalised quantities and renormalisation constants:

$$
e _ {0} = (1 + \delta Z _ {e}) e, \tag {3.6}
$$

$$
M _ {W, 0} ^ {2} = M _ {W} ^ {2} + \delta M _ {W} ^ {2} \tag {3.7}
$$

$$
M _ {Z, 0} ^ {2} = M _ {Z} ^ {2} + \delta M _ {Z} ^ {2} \tag {3.8}
$$

$$
M _ {H, 0} ^ {2} = M _ {H} ^ {2} + \delta M _ {H} ^ {2}. \tag {3.9}
$$

Wave function renormalisation is defined as follows:

$$
W _ {0} ^ {\pm} = \left(1 + \frac {1}{2} \delta Z _ {W}\right) W ^ {\pm} \tag {3.10}
$$

$$
Z _ {0} = \left(1 + \frac {1}{2} \delta Z _ {Z Z}\right) Z + \frac {1}{2} \delta Z _ {Z A} A \tag {3.11}
$$

$$
A _ {0} = \frac {1}{2} \delta Z _ {A Z} Z + \left(1 + \frac {1}{2} \delta Z _ {A A}\right) A \tag {3.12}
$$

$$
H _ {0} = \left(1 + \frac {1}{2} \delta Z _ {H}\right) H. \tag {3.13}
$$

The renormalisation of the tadpole does not show up in any counter term relevant in this calculation, so we do not consider it here.

To determine the dim-6 contributions in the renormalisation constants, we compute the two-point functions of the gauge bosons and the Higgs boson, from the top-quark operators. They can be written as

$$
\begin{array}{l} \bar {\Sigma} _ {V V} ^ {(6)} (q ^ {2}) = \Sigma_ {V V} ^ {(6)} (q ^ {2}) + \Sigma_ {V V} ^ {C T} (q ^ {2}) \\ = \sum_ {i} C _ {i} \Sigma_ {V V} ^ {i, l o o p} \left(q ^ {2}\right) + \sum_ {i, j} \delta Z _ {j i} C _ {i} \Sigma_ {V V} ^ {j, t r e e} \left(q ^ {2}\right) \tag {3.14} \\ \end{array}
$$

where in the last line, index  $i$  runs over all top-quark operators, and  $j$  runs over all Higgs operators that are needed to provide counter terms.  $\Sigma_{VV}^{i / j,\text{loop}/\text{tree}}(q^2)$  are the corresponding operator contributions to the  $VV$  transverse two-point function. The Higgs-boson self energy  $\bar{\Sigma}_{HH}$  is defined similarly. The dim-6 contributions in the renormalisation constants (denoted by the superscript (6)) are determined by these two-point functions, namely

$$
\delta M _ {W} ^ {2 (6)} = \Re \bar {\Sigma} _ {W W} ^ {(6)} (M _ {W} ^ {2}), \qquad \delta M _ {Z} ^ {2 (6)} = \Re \bar {\Sigma} _ {Z Z} ^ {(6)} (M _ {Z} ^ {2}),
$$

$$
\delta M _ {H} ^ {2 (6)} = \Re \bar {\Sigma} _ {H H} ^ {(6)} (M _ {H} ^ {2}), \qquad \qquad \qquad \delta Z _ {W} ^ {(6)} = - \Re \left. \frac {\partial \bar {\Sigma} _ {W W} ^ {(6)} (k ^ {2})}{\partial k ^ {2}} \right| _ {k ^ {2} = M _ {W} ^ {2}},
$$

$$
\delta Z _ {Z Z} ^ {(6)} = - \Re \left. \frac {\partial \bar {\Sigma} _ {Z Z} ^ {(6)} \left(k ^ {2}\right)}{\partial k ^ {2}} \right| _ {k ^ {2} = M _ {Z} ^ {2}}, \quad \delta Z _ {A A} ^ {(6)} = - \left. \frac {\partial \bar {\Sigma} _ {A A} ^ {(6)} \left(k ^ {2}\right)}{\partial k ^ {2}} \right| _ {k ^ {2} = 0}, \tag {3.15}
$$

$$
\delta Z _ {A Z} ^ {(6)} = - 2 \Re \frac {\bar {\Sigma} _ {A Z} ^ {(6)} (M _ {Z} ^ {2})}{M _ {Z} ^ {2}}, \quad \delta Z _ {Z A} ^ {(6)} = 2 \frac {\bar {\Sigma} _ {A Z} ^ {(6)} (0)}{M _ {Z} ^ {2}},
$$

$$
\delta Z _ {H} ^ {(6)} = - \Re \left. \frac {\partial \bar {\Sigma} _ {H H} ^ {(6)} (k ^ {2})}{\partial k ^ {2}} \right| _ {k ^ {2} = M _ {H} ^ {2}}, \qquad \delta Z _ {e} ^ {(6)} = \frac {1}{2} \left. \frac {\partial \bar {\Sigma} _ {A A} ^ {(6)} (k ^ {2})}{\partial k ^ {2}} \right| _ {k ^ {2} = 0} - \frac {s _ {W}}{c _ {W}} \frac {\bar {\Sigma} _ {A Z} ^ {(6)} (0)}{M _ {Z} ^ {2}}.
$$

In particular, the renormalized  $Z$  and  $A$  two-point functions become diagonal if the external lines are on their mass shell. The last equation defines the electric charge at zero momentum transfer. For the operators we have included, there are no large logarithmic terms arising from the  $b$ -quark mass, and so there is no need to define the running electric charge to resum the logs, as we only need the dim-6 EW contributions from the top loop. Note that the explicit expressions for  $\Sigma_{VV}^{(6)}(q^2)$  have been given in ref. [14], with an overall minus sign due to different conventions. In  $H \rightarrow b\bar{b}$ , the  $b$ -quark mass is renormalized in a similar way. The expressions for renormalisation constants can be found in ref. [71], and therefore we do not repeat them here.

The above renormalisation constants would be sufficient to determine all the relevant counter terms, if we used  $\alpha$ ,  $M_Z$  and  $M_W$  as the input parameters. Conventionally, EW corrections are often computed with  $\alpha$ ,  $M_Z$  and  $G_F$  as input parameters. In our case,

however, it is more convenient to use  $M_W$ ,  $M_Z$  and  $G_F$  instead. This is because  $M_W$  enters the final state phase space, and we do not want its mass to depend on the dim-6 coefficients, because it would be particularly inconvenient for using the reweighting technique. To switch to the  $M_W$ ,  $M_Z$  and  $G_F$  scheme, we use

$$
M _ {W} ^ {2} \left(1 - \frac {M _ {W} ^ {2}}{M _ {Z} ^ {2}}\right) = \frac {\pi \alpha}{\sqrt {2} G _ {F}} (1 + \Delta r), \tag {3.16}
$$

where the  $\Delta r$  contribution from the top-quark operators is

$$
\Delta_ {r} ^ {(6)} = \left. \frac {\partial \bar {\Sigma} _ {A A} ^ {(6)} \left(k ^ {2}\right)}{\partial k ^ {2}} \right| _ {k ^ {2} = 0} - \frac {c _ {W} ^ {2}}{s _ {W} ^ {2}} \left(\frac {\bar {\Sigma} _ {Z Z} ^ {(6)} \left(M _ {Z} ^ {2}\right)}{M _ {Z} ^ {2}} - \frac {\bar {\Sigma} _ {W W} ^ {(6)} \left(M _ {W} ^ {2}\right)}{M _ {W} ^ {2}}\right) + \frac {\bar {\Sigma} _ {W W} ^ {(6)} (0) - \bar {\Sigma} _ {W W} ^ {(6)} \left(M _ {W} ^ {2}\right)}{M _ {W} ^ {2}}. \tag {3.17}
$$

One can simply define

$$
\bar {\alpha} = \alpha (1 + \Delta r) \tag {3.18}
$$

so that the tree level relation between  $M_W$ ,  $M_Z$ ,  $G_F$ , and  $\alpha$  holds. To switch to the new scheme, one just needs to modify the renormalisation constant for  $\alpha$ :

$$
\delta \bar {\alpha} ^ {(6)} = \delta \alpha^ {(6)} + (\alpha - \bar {\alpha}) _ {d i m - 6}. \tag {3.19}
$$

# 3.3 Counter terms

The counter term Feynman rules are determined by the renormalisation constants and the RG mixing matrix. For example, consider the  $HZZ$  vertex, whose tree level Feynman rule is

$$
\Gamma_ {H Z Z} ^ {\mu \nu} = i \frac {e M _ {W}}{s _ {W} c _ {W} ^ {2}} g ^ {\mu \nu} + \sum_ {i} C _ {i} \Gamma_ {H Z Z, i} ^ {\mu \nu}, \tag {3.20}
$$

where the subscript  $i$  covers all Higgs operators that have a contribution, including  $O_{\varphi WB}$ ,  $O_{\varphi W}$ ,  $O_{\varphi B}$ ,  $O_{\varphi D}$ ,  $O_W$ , and  $O_B$ . The corresponding dim-6 counter term has two parts. The first is the dim-6 contribution in the SM renormalisation, given by

$$
i \frac {e M _ {W}}{s _ {W} c _ {W} ^ {2}} g ^ {\mu \nu} \left[ \delta Z _ {e} ^ {(6)} + \frac {\delta M _ {W} ^ {2 (6)}}{2 M _ {W} ^ {2}} - \frac {\delta s _ {W} ^ {(6)}}{s _ {W}} - \frac {2 \delta c _ {W} ^ {(6)}}{c _ {W}} + \delta Z _ {Z Z} ^ {(6)} + \frac {1}{2} \delta Z _ {H} ^ {(6)} \right] \tag {3.21}
$$

where

$$
\delta c _ {W} = \frac {c _ {W}}{2} \left(\frac {\delta M _ {W} ^ {2}}{M _ {W} ^ {2}} - \frac {\delta M _ {Z} ^ {2}}{M _ {Z} ^ {2}}\right) \tag {3.22}
$$

$$
\delta s _ {W} = - \frac {c _ {W}}{s _ {W}} \delta c _ {W} \tag {3.23}
$$

while the second is from the RG mixing between dim-6 coefficients, given by

$$
\sum_ {i, j} C _ {j} \delta Z _ {i j} \Gamma_ {H Z Z, i} ^ {\mu \nu} \tag {3.24}
$$

where  $i$  runs over the Higgs operators and  $j$  runs over the top-quark operators.

# 4 Numerical results

We are now ready to present the numerical results of our computation. We use the following input parameters:

$$
M _ {Z} = 9 1. 1 8 7 6 \mathrm {G e V}, \quad M _ {W} = 8 0. 3 8 5 \mathrm {G e V}, \tag {4.1}
$$

$$
G _ {F} = 1. 1 6 6 3 8 \times 1 0 ^ {- 5} \mathrm {G e V} ^ {- 2}, \quad M _ {H} = 1 2 5 \mathrm {G e V}, \tag {4.2}
$$

$$
M _ {t} = 1 7 2. 5 \mathrm {G e V}, \quad M _ {b} = 4. 7 \mathrm {G e V}. \tag {4.3}
$$

As we have explained in the introduction, all channels are computed for two cases:  $\mu_{EFT} = M_H = 125\mathrm{GeV}$  and  $\mu_{EFT} = \Lambda = 1000\mathrm{GeV}$ . Results will be displayed as ratios w.r.t. to LO SM predictions:

$$
\mu_ {i} \equiv \frac {\sigma_ {i}}{\sigma^ {\mathrm {S M}}} \text {o r} \frac {\Gamma_ {i}}{\Gamma^ {\mathrm {S M}}} \equiv 1 + \sum_ {j} C _ {j} \left(\frac {1 \mathrm {T e V} ^ {2}}{\Lambda^ {2}}\right) \mu_ {i j} \tag {4.4}
$$

where  $i$  denotes channel,  $j$  runs over all contributing operators.  $\mu_{ij}$  is the relative deviation in channel  $i$  from operator  $j$  if  $C_j / \Lambda^2 = 1 / \mathrm{TeV}^2$ .  $\mu_{ij}$  for all decay processes are given in percentage, in table 1, and for all production processes at the LHC at 13 TeV and future lepton colliders are given in tables 2-5. For lepton colliders we consider 250 and 350 GeV centre-of-mass energies, to cover possible scenarios at CEPC, FCC-ee, and ILC, which are planned to collect data at both  $240\sim 250\mathrm{GeV}$  and 350 GeV [72-75]. We present results for two beam polarisation configurations  $P(e^{+},e^{-}) = (\pm 30\%,\mp 80\%)$ . In the 350 GeV case, we only consider the  $O_{t\varphi}$  contributions, as the sensitivity to other operators is unlikely to compete with the direct production modes [76, 77]. In all processes we set the renormalisation and factorisation scale to  $M_H$ . For  $VH$  production no cuts are applied, whilst for VBF we apply the following jet cuts at the LHC:

$$
p _ {T} ^ {j} > 2 0 \mathrm {G e V}, | y _ {j} | <   5, | y _ {j 1} - y _ {j 2} | > 3, M _ {j j} > 1 3 0 \mathrm {G e V}. \tag {4.5}
$$

No cuts are applied for the lepton collider results. In both cases the Higgs and vector bosons are not decayed. We note here that for  $ZH$  production at the LHC we consider only the  $q\bar{q}$  contribution. The impact of top operators on the gluon fusion contribution,  $gg \rightarrow ZH$  have already been considered in [26, 27].

Note that these results are computed with our modified  $\overline{MS}$  scheme. For completeness, in appendix A we also present results computed with the standard  $\overline{MS}$  scheme.

From tables 1-5 we see that loop-induced decay channels  $H \rightarrow \gamma \gamma$  and  $H \rightarrow Z\gamma$  can show large deviations from the SM. For all other processes, the relative deviation caused by a top operator with  $C_j / \Lambda^2 = 1 / \mathrm{TeV}^2$  is around the percent level. One also observes that  $\mu_{EFT} = 1000\mathrm{GeV}$  results are in general larger than the  $\mu_{EFT} = 125\mathrm{GeV}$  ones, due to the logarithmic terms, but  $\mu_{EFT} = 125\mathrm{GeV}$  deviations are not negligible at all. There are also entries where the  $\mu_{EFT} = 125\mathrm{GeV}$  result is larger.

Another observation is that these results depend on the scheme of input parameters used in the calculation. For example, if we used the  $\alpha$ ,  $M_Z$  and  $G_F$  scheme, the operator  $O_{tB}$  would give a contribution to  $H \to Wl\nu$  and  $pp \to HW$ , because its contribution to

Table 1. Percentage deviation  ${\mu }_{ij}$  for decay channel  $i$  and operator  $j$  .  

<table><tr><td>channel</td><td>μEFT [GeV]</td><td>Oφt</td><td>O(+)φQ</td><td>O(-)φQ</td><td>Oφtb</td><td>OtW</td><td>OtB</td><td>Otφ</td></tr><tr><td>H → bb</td><td>125</td><td>-0.15</td><td>-0.06</td><td>0.24</td><td>-1.13</td><td>-0.28</td><td>0</td><td>-0.18</td></tr><tr><td>H → bb</td><td>1000</td><td>0.79</td><td>0.54</td><td>-1.25</td><td>-8.16</td><td>0.34</td><td>0</td><td>0.29</td></tr><tr><td>H → μμ,ττ</td><td>125</td><td>-0.15</td><td>0.001</td><td>0.15</td><td>0</td><td>0</td><td>0</td><td>-0.27</td></tr><tr><td>H → μμ,ττ</td><td>1000</td><td>0.79</td><td>0.002</td><td>-0.79</td><td>0</td><td>0</td><td>0</td><td>0.68</td></tr><tr><td>H → γγ</td><td>125</td><td>-3.37</td><td>5.86</td><td>2.64</td><td>0</td><td>-56.4</td><td>-117.9</td><td>3.45</td></tr><tr><td>H → γγ</td><td>1000</td><td>6.95</td><td>16.2</td><td>-2.52</td><td>0</td><td>14.0</td><td>101.3</td><td>3.45</td></tr><tr><td>H → Zγ</td><td>125</td><td>0.51</td><td>2.20</td><td>2.74</td><td>0</td><td>-39.5</td><td>14.0</td><td>0.72</td></tr><tr><td>H → Zγ</td><td>1000</td><td>4.35</td><td>6.04</td><td>0.83</td><td>0</td><td>33.9</td><td>-51.6</td><td>0.72</td></tr><tr><td>H → Zll</td><td>125</td><td>-0.54</td><td>-0.10</td><td>0.56</td><td>-0.00</td><td>0.19</td><td>-0.06</td><td>0.08</td></tr><tr><td>H → Zll</td><td>1000</td><td>0.33</td><td>0.74</td><td>-1.25</td><td>-0.06</td><td>0.05</td><td>0.33</td><td>0.08</td></tr><tr><td>H → Wlν</td><td>125</td><td>-0.15</td><td>-0.24</td><td>0.38</td><td>0.00</td><td>-0.13</td><td>0</td><td>-0.03</td></tr><tr><td>H → Wlν</td><td>1000</td><td>0.79</td><td>0.63</td><td>-1.42</td><td>-0.05</td><td>0.33</td><td>0</td><td>-0.03</td></tr></table>

Table 2. Percentage deviation  ${\mu }_{ij}$  for production channel  $i$  and operator  $j$  at LHC  ${13}\mathrm{{TeV}}$  .  

<table><tr><td>channel</td><td>μEFT [GeV]</td><td>Oφt</td><td>O(+)φQ</td><td>O(-)φQ</td><td>Oφtb</td><td>OtW</td><td>OtB</td><td>Otφ</td></tr><tr><td>pp → ZH</td><td>125</td><td>-0.30</td><td>0.21</td><td>0.21</td><td>-0.00</td><td>1.00</td><td>-0.06</td><td>-0.02</td></tr><tr><td>pp → ZH</td><td>1000</td><td>0.57</td><td>0.11</td><td>-0.66</td><td>-0.06</td><td>-2.75</td><td>-0.44</td><td>-0.02</td></tr><tr><td>pp → WH</td><td>125</td><td>-0.15</td><td>-0.04</td><td>0.19</td><td>0.00</td><td>0.43</td><td>0</td><td>-0.21</td></tr><tr><td>pp → WH</td><td>1000</td><td>0.79</td><td>-0.27</td><td>-0.52</td><td>-0.05</td><td>-4.08</td><td>0</td><td>-0.21</td></tr><tr><td>pp → Hjj</td><td>125</td><td>-0.26</td><td>-0.24</td><td>0.51</td><td>0.01</td><td>0.05</td><td>-0.00</td><td>0.03</td></tr><tr><td>pp → Hjj</td><td>1000</td><td>0.68</td><td>0.94</td><td>-1.61</td><td>-0.04</td><td>0.28</td><td>-0.00</td><td>0.03</td></tr></table>

Table 3. Percentage deviation  ${\mu }_{ij}$  for production channel  $i$  and operator  $j$  for  ${250}\mathrm{{GeV}}$  and  $P\left( {{e}^{ + },{e}^{ - }}\right)  = \left( {{30}\% , - {80}\% }\right)$  .  

<table><tr><td>channel</td><td>μEFT [GeV]</td><td>Oφt</td><td>O(+)φQ</td><td>O(-)φQ</td><td>Oφtb</td><td>OtW</td><td>OtB</td><td>Otφ</td></tr><tr><td>e+e-→ ZH</td><td>125</td><td>-0.40</td><td>-0.21</td><td>0.22</td><td>-0.00</td><td>1.82</td><td>-0.25</td><td>0.01</td></tr><tr><td>e+e-→ ZH</td><td>1000</td><td>0.78</td><td>-0.10</td><td>-0.71</td><td>-0.05</td><td>-2.71</td><td>0.62</td><td>0.01</td></tr><tr><td>e+e-→ Hνν</td><td>125</td><td>-0.15</td><td>-0.26</td><td>0.41</td><td>0.01</td><td>-0.08</td><td>0</td><td>-0.01</td></tr><tr><td>e+e-→ Hνν</td><td>1000</td><td>0.79</td><td>0.76</td><td>-1.55</td><td>-0.04</td><td>0.13</td><td>0</td><td>-0.01</td></tr><tr><td>e+e-→ He+e-</td><td>125</td><td>-0.51</td><td>-0.27</td><td>0.56</td><td>0.00</td><td>0.72</td><td>0.79</td><td>0.08</td></tr><tr><td>e+e-→ He+e-</td><td>1000</td><td>0.28</td><td>0.76</td><td>-1.50</td><td>-0.05</td><td>0.77</td><td>-0.71</td><td>0.08</td></tr></table>

Table 4. Percentage deviation  $\mu_{ij}$  for production channel  $i$  and operator  $j$  for 250 GeV and  $P(e^{+},e^{-}) = (-30\%,80\%)$ .  

<table><tr><td>channel</td><td>μEFT [GeV]</td><td>Oφt</td><td>O(+)φQ</td><td>O(-)φQ</td><td>Oφtb</td><td>OtW</td><td>OtB</td><td>Otφ</td></tr><tr><td>e+e-→ZH</td><td>125</td><td>-0.44</td><td>0.36</td><td>0.55</td><td>-0.01</td><td>-0.62</td><td>0.17</td><td>0.06</td></tr><tr><td>e+e-→ZH</td><td>1000</td><td>0.00</td><td>1.14</td><td>-1.42</td><td>-0.06</td><td>-1.35</td><td>-2.35</td><td>0.06</td></tr><tr><td>e+e-→Hνν</td><td>125</td><td>-0.15</td><td>-0.26</td><td>0.41</td><td>0.01</td><td>-0.01</td><td>0</td><td>-0.01</td></tr><tr><td>e+e-→Hνν</td><td>1000</td><td>0.79</td><td>0.76</td><td>-1.55</td><td>-0.04</td><td>0.01</td><td>0</td><td>-0.01</td></tr><tr><td>e+e-→He+e-</td><td>125</td><td>-0.62</td><td>0.14</td><td>0.66</td><td>-0.01</td><td>0.32</td><td>1.40</td><td>0.05</td></tr><tr><td>e+e-→He+e-</td><td>1000</td><td>0.30</td><td>0.95</td><td>-1.08</td><td>-0.06</td><td>-0.60</td><td>-0.85</td><td>0.05</td></tr></table>

Table 5. Percentage deviation  ${\mu }_{ij}$  for production channel  $i$  and operator  ${O}_{t\varphi }$  for  ${350}\mathrm{{GeV}}$  and  $P\left( {{e}^{ + },{e}^{ - }}\right)  = \left( {\pm {30}\% , \mp  {80}\% }\right)$  . The results are identical at any  ${\mu }_{\text{EFT }}$  .  

<table><tr><td>channel Otφ</td><td>P(30%, -80%)</td><td>P(-30%, 80%)</td></tr><tr><td>e+e- → ZH</td><td>-0.15</td><td>0.01</td></tr><tr><td>e+e- → Hνν</td><td>-0.01</td><td>-0.01</td></tr><tr><td>e+e- → He+e-</td><td>0.10</td><td>0.08</td></tr></table>

the  $ZZ$  two-point function could affect the  $Z$  mass, which in turn enters  $g_{w}$  and  $M_W$ . But these contributions vanish if we use the  $M_W$ ,  $M_Z$  and  $G_{F}$  input scheme, because the renormalisation condition for  $G_{F}$  will fix the renormalisation constant of  $g_{w}$  so that it only depends on the  $WW$  two-point function, to which  $O_{tB}$  does not contribute. The same applies to  $O_{\varphi t}$ , i.e.  $O_{\varphi t}$  gives no contribution in  $H \to Wl\nu$  and  $pp \to HW$  if the standard  $\overline{MS}$  scheme is used. However it does give a contribution to the  $T$  parameter, and because we use  $T$  as one of the renormalisation conditions to fix  $C_{\varphi D}$ , a non-zero contribution arises due to  $O_{\varphi D}$  modifying the Higgs wave-function. In general, most results we have obtained so far will depend on the input scheme used in the calculation. This is also why we want to include constraints from precision EW tests, so that the relation between  $\alpha$ ,  $M_W$ ,  $M_Z$  and  $G_{F}$  is not significantly modified. In table 6 we present results for  $S$ ,  $T$  and  $U$  in the original  $\overline{MS}$  scheme. They are parameterised by

$$
S \equiv \sum_ {j} C _ {j} \left(\frac {1 \mathrm {T e V} ^ {2}}{\Lambda^ {2}}\right) S _ {j}, \tag {4.6}
$$

and similarly for  $T$ ,  $U$ . Note that  $U$  is finite and is scheme independent [15].

The precision EW tests contain more information than  $S$ ,  $T$  and  $U$ . This information is lost in the STU formalism simply because the two-point functions of gauge bosons are approximated as linear functions of the momentum squared. A complete analysis for precision EW data without using these oblique parameters can be performed to obtain better constraints, see ref. [14] for more details. Since a global fit is not the goal of this study, in this paper we will only use the oblique parameters to simplify the analysis of the precision EW part, but one should keep in mind that in principle more information can be obtained.

Table 6. Deviation in  $S$ ,  $T$  and  $U$  parameters due to top operators.  

<table><tr><td></td><td>μEFT [GeV]</td><td>Oφt</td><td>O(+)φQ</td><td>O(-)φQ</td><td>Oφtb</td><td>OtW</td><td>OtB</td><td>Otφ</td></tr><tr><td>S</td><td>125</td><td>-0.017</td><td>0.029</td><td>0.013</td><td>0</td><td>0.084</td><td>0.095</td><td>0</td></tr><tr><td>S</td><td>1000</td><td>0.035</td><td>0.081</td><td>-0.013</td><td>0</td><td>-0.504</td><td>-0.565</td><td>0</td></tr><tr><td>T</td><td>125</td><td>-0.186</td><td>0.022</td><td>0.165</td><td>0.003</td><td>0</td><td>0</td><td>0</td></tr><tr><td>T</td><td>1000</td><td>1.016</td><td>-0.579</td><td>-0.436</td><td>0.036</td><td>0</td><td>0</td><td>0</td></tr><tr><td>U</td><td>125</td><td>0.010</td><td>-0.048</td><td>-0.016</td><td>0.001</td><td>0.090</td><td>0</td><td>0</td></tr><tr><td>U</td><td>1000</td><td>0.010</td><td>-0.048</td><td>-0.016</td><td>0.001</td><td>0.090</td><td>0</td><td>0</td></tr></table>

We briefly demonstrate that physical results are scheme-independent. Consider  $H \to \gamma \gamma$  with  $\mu_{EFT} = 125\mathrm{GeV}$  as an example. Taking the standard  $\overline{MS}$  results in table 14 in appendix A, we have the following dim-6 contributions to the width:

$$
\Gamma_ {\gamma \gamma} ^ {(6)} = \Gamma_ {\gamma \gamma} ^ {\mathrm {S M}} \left(1 + 2 5. 7 4 C _ {\varphi W B} - 0. 7 3 3 C _ {t W} - 1. 3 6 7 C _ {t B} + 0. 0 3 4 5 C _ {t \varphi}\right) \tag {4.7}
$$

where we have used that  $O_{\varphi W B}$  gives the following  $H \to \gamma \gamma$  amplitude:

$$
4 \frac {C _ {\varphi W B} s _ {W} c _ {W}}{\Lambda^ {2}} \left(\frac {M _ {H} ^ {2}}{2} \epsilon_ {1} \cdot \epsilon_ {2} - (p _ {1} \cdot \epsilon_ {2}) (p _ {2} \cdot \epsilon_ {1})\right). \tag {4.8}
$$

Following table 6, the  $S$  parameter is given by

$$
S = - 1 2. 9 C _ {\varphi W B} - 0. 0 1 7 C _ {\varphi t} + 0. 0 2 9 C _ {\varphi Q} ^ {(+)} + 0. 0 1 3 C _ {\varphi Q} ^ {(-)} + 0. 0 8 4 C _ {t W} + 0. 0 9 5 C _ {t B} \tag {4.9}
$$

where the coefficient of  $C_{\varphi W B}$  is given by

$$
\alpha_ {E W} S = \frac {C _ {\varphi W B} 4 v ^ {2} s _ {W} c _ {W}}{\Lambda^ {2}}. \tag {4.10}
$$

Combining eqs. (4.7) and (4.9) and eliminating  $C_{\varphi WB}$ , we find the expression of  $\Gamma_{\gamma \gamma}^{(6)}$  for a fixed  $S$  parameter, which agrees with results in table 1. One can easily check the same relation holds for  $\mu_{EFT} = 1000 \mathrm{GeV}$  and for  $H \rightarrow \gamma Z$ .

Finally, we note here that our results in tables 1-6 provide the  $\mathcal{O}(1 / \Lambda^2)$  deviation from the SM predictions from the top operators. Our computational setup allows us to also obtain the  $\mathcal{O}(1 / \Lambda^4)$  contribution coming from squaring the 1-loop contributions. As an example in table 7 we show the percentage deviation from the SM induced at  $\mathcal{O}(1 / \Lambda^4)$  by the top operators for  $C_i = 1$  and  $\Lambda = 1\mathrm{TeV}$  for  $ZH$  production at the LHC. We find that these high-order contributions are suppressed by about two orders of magnitude compared to the  $\mathcal{O}(1 / \Lambda^2)$  contributions in table 2. Given the current limits on the operator coefficients, we can safely ignore these contributions. A similar behaviour is expected also for the other processes studied in this work, except for loop-induced processes in the SM, i.e.  $gg\rightarrow H$ ,  $H\rightarrow \gamma \gamma ,\gamma Z,gg$ . For these processes, the SM contributions are suppressed, so dim-6 squared terms can be potentially important. Their quadratic dependence on the operator coefficients will be kept in section 5.1 and 5.2, where we only use current limits to constrain top-quark operators.

Table 7. Percentage deviation at  $\mathcal{O}\left( {1/{\Lambda }^{4}}\right)$  for  ${ZH}$  production at LHC 13 TeV.  

<table><tr><td>channel</td><td>μEFT [GeV]</td><td>Oφt</td><td>O(+)φQ</td><td>O(-)φQ</td><td>Oφtb</td><td>OtW</td><td>OtB</td><td>Otφ</td></tr><tr><td>pp → ZH</td><td>125</td><td>0.0014</td><td>0.0078</td><td>0.0041</td><td>4.0 × 10-8</td><td>0.0085</td><td>0.0012</td><td>3.7 × 10-5</td></tr><tr><td>pp → ZH</td><td>1000</td><td>0.0022</td><td>0.0062</td><td>0.0047</td><td>7.5 × 10-6</td><td>0.037</td><td>0.0054</td><td>3.7 × 10-5</td></tr></table>

Table 8. Individual limits on operator coefficients, from the Top Fitter Collaboration [5], right-handed charged currents (RHCC) (tree-level only) [9], and  $t\bar{t}H$  cross section [28].  $\Lambda = 1$  TeV is assumed.  

<table><tr><td>Operator</td><td>Top Fitter</td><td>RHCC</td><td>σtbarH [28]</td></tr><tr><td>Cφtb</td><td></td><td>[-5.28,5.28]</td><td></td></tr><tr><td>C(3)φQ</td><td>[-2.59,1.50]</td><td></td><td></td></tr><tr><td>C(1)φQ</td><td>[-3.10,3.10]</td><td></td><td></td></tr><tr><td>Cφt</td><td>[-9.78,8.18]</td><td></td><td></td></tr><tr><td>CtW</td><td>[-2.49,2.49]</td><td></td><td></td></tr><tr><td>CtB</td><td>[-7.09,4.68]</td><td></td><td></td></tr><tr><td>Ctφ</td><td></td><td></td><td>[-6.5,1.3]</td></tr></table>

# 5 Physics implications

In this section we discuss the impact of our numerical results.

# 5.1 Impact on Higgs measurements at the LHC

The first consequence of these loop contributions in Higgs measurements is that they can shift the measured signal strengths at the LHC. The current constraints on top-quark operator coefficients are not very stringent compared to Higgs operator constraints, and so within the allowed range, the loop-induced contributions could potentially affect the signal strengths of all Higgs channels. Without knowing exactly the coefficients of top-quark operators, these contributions can only be dealt with as theoretical uncertainties, and should be considered in all Higgs measurements that are analysed using a SMEFT approach. These theoretical uncertainties cannot be avoided in a bottom-up view of the SMEFT, as in general there is no strong motivation to overlook a certain type of operators [78], in particular at the energy scale of the measurements, where the RG effects will take place and mix different types of operators.

To estimate the size of possible contributions from top operators, we consider the current constraints on top-quark operator coefficients from direct measurements. These constraints originate from processes where these operators enter already at the tree level. First, the TopFitter collaboration performed a global fit (excluding  $O_{\varphi tb}$ ) at LO using both Tevatron and LHC data for top production and decay [5]. Individual limits are given for each operator, by setting other operator coefficients to zero. In addition, the  $O_{\varphi tb}$  operator gives rise to right handed  $Wtb$  coupling, which is constrained at tree-level by single top and

Table 9. Possible deviations in signal strengths, due to top-quark operators, in major Higgs production and decay channels at the LHC. The top-quark operator coefficients are allowed to vary within the current constraints, described in table 8.  

<table><tr><td></td><td>γγ</td><td>γZ</td><td>bb</td><td>WW*</td><td>ZZ*</td><td>ττ</td><td>μμ</td></tr><tr><td>gg</td><td>(-100%,1980%)</td><td>(-88%,200%)</td><td>(-40%,48%)</td><td>(-40%,47%)</td><td>(-40%,46%)</td><td>(-40%,48%)</td><td>(-40%,48%)</td></tr><tr><td>VBF</td><td>(-100%,1880%)</td><td>(-88%,170%)</td><td>(-6.1%,5.3%)</td><td>(-6.8%,6.7%)</td><td>(-8.8%,9.2%)</td><td>(-6.2%,5.9%)</td><td>(-6.2%,5.9%)</td></tr><tr><td>WH</td><td>(-100%,1880%)</td><td>(-88%,170%)</td><td>(-5.5%,4.2%)</td><td>(-6.1%,5.6%)</td><td>(-7.8%,7.9%)</td><td>(-5.8%,5.1%)</td><td>(-5.8%,5.1%)</td></tr><tr><td>ZH</td><td>(-100%,1880%)</td><td>(-87%,170%)</td><td>(-6.5%,5.9%)</td><td>(-7.1%,7.1%)</td><td>(-9.4%,9.9%)</td><td>(-6.8%,6.7%)</td><td>(-6.8%,6.7%)</td></tr></table>

top decay measurements, and indirectly at loop-level by  $B$  meson decay and  $h \rightarrow b\bar{b}$  [9]. Here we only use the direct limits. For the Yukawa operator  $\mathcal{O}_{t\varphi}$ , we follow the approach in ref. [28], and update the analysis with the recent 13 TeV measurements in refs. [79-82]. Again, we do not use the loop-induced  $gg \rightarrow H$  process. In table 8 we list these constraints.

Using all the individual direct constraints and neglecting correlations, we can approximately identify the allowed region in the 7-dimensional parameter space at  $95\%$  CL, by reconstructing a  $\chi^2$ . We shift all the intervals so that they are centred at zero. Within the range allowed by the constraints, using the results presented in table 1 and table 2, we find the maximum and minimum percentage deviations in signal strengths in all Higgs channels, taking  $\mu_{EFT} = 125\mathrm{GeV}$ , i.e. the scale of the measurements. These deviations are given in table 9. For example, the interval shown in the 4th row and 3rd column means that in  $pp\rightarrow ZH$ ,  $H\rightarrow bb$ , the signal strength can be shifted by  $-7\%$  to  $+6\%$  by top-quark operators within the current constraints.

We see that for the loop-induced processes, i.e. those in the first row and the first two columns, the deviations are large. This simply demonstrates that for operators like  $O_{tB}$ , loop-induced constraints are much stronger than the tree-level ones. For example, the  $gg \rightarrow H \rightarrow \gamma \gamma$  signal strength can deviate by a factor of  $\sim 20$  and this is mainly driven by  $|C_{tB}| \approx 6$ . It implies that this channel is sensitive to  $C_{tB}$  and can be used to place much stronger bounds compared with the current ones. The same applies to other loop-induced channels.

For the remaining tree-level Higgs channels, the impact of top-operators through loops is in general weaker, but remains around  $5 \sim 10\%$ , and is not negligible even for the current precision. Although theory uncertainties of this size may not significantly change the result of a Higgs coupling analysis, they will become relevant from now on, and eventually, at the high luminosity scenario, become an important component of theory uncertainties in a bottom-up global SMEFT analysis.

This also implies that once the precision of Higgs measurements goes beyond  $\sim 10\%$ , we can even hope to use Higgs measurements to place useful constraints on top-quark operators. In section 5.3 we discuss this possibility by estimating the sensitivity in the high luminosity scenario of LHC.

# 5.2 Impact on Higgs measurements at the future lepton colliders

As we have mentioned in the introduction, at lepton colliders, the estimated precision of Higgs signal strength measurements could reach  $\mathcal{O}(1\%) - \mathcal{O}(0.1\%)$  level. For the Higgs

Table 10. Possible deviations in signal strengths (in percent) caused by top-quark operators, in Higgs production (WWF for WW fusion and ZZF for ZZ fusion) and decay channels, at an  $e^{+}e^{-}$  collider at 250 GeV centre-of-mass energy. All top-quark operator coefficients are allowed to vary within the current constraints, described in table 8.  

<table><tr><td></td><td>γγ</td><td>γZ</td><td>bb</td><td>WW*</td><td>ZZ*</td><td>ττ</td><td>μμ</td></tr><tr><td>ZH(+30%,-80%)</td><td>(-100%,1900%)</td><td>(-87%,160%)</td><td>(-7.5%,7.5%)</td><td>(-8.3%,8.6%)</td><td>(-11%,11%)</td><td>(-8%,8.3%)</td><td>(-8%,8.3%)</td></tr><tr><td>ZH(-30%,+80%)</td><td>(-100%,1870%)</td><td>(-88%,180%)</td><td>(-7.6%,7.1%)</td><td>(-8.1%,7.9%)</td><td>(-10%,11%)</td><td>(-7.6%,7.3%)</td><td>(-7.6%,7.3%)</td></tr><tr><td>WWF(+30%,-80%)</td><td>(-100%,1880%)</td><td>(-88%,170%)</td><td>(-5.7%,4.7%)</td><td>(-6.5%,6.2%)</td><td>(-8.1%,8.3%)</td><td>(-5.9%,5.3%)</td><td>(-5.9%,5.3%)</td></tr><tr><td>WWF(-30%,+80%)</td><td>(-100%,1880%)</td><td>(-88%,170%)</td><td>(-5.7%,4.7%)</td><td>(-6.5%,6.2%)</td><td>(-8.1%,8.3%)</td><td>(-5.9%,5.3%)</td><td>(-5.9%,5.3%)</td></tr><tr><td>ZZF(+30%,-80%)</td><td>(-100%,1790%)</td><td>(-88%,180%)</td><td>(-11%,8.6%)</td><td>(-11%,9.6%)</td><td>(-13%,12%)</td><td>(-11%,9%)</td><td>(-11%,9%)</td></tr><tr><td>ZZF(-30%,+80%)</td><td>(-100%,1730%)</td><td>(-88%,180%)</td><td>(-14%,11%)</td><td>(-14%,12%)</td><td>(-15%,15%)</td><td>(-14%,11%)</td><td>(-14%,11%)</td></tr></table>

Table 11. Possible deviations in signal strengths (in percent) caused by top-quark operators, in Higgs production (WWF for  $WW$  fusion and ZZF for  $ZZ$  fusion) and decay channels, at an  $e^{+}e^{-}$  collider at  $250\mathrm{GeV}$  centre-of-mass energy. Only the coefficient of  $O_{t\varphi}$  is allowed to vary within the current constraints, described in table 8.  

<table><tr><td></td><td>γγ</td><td>γZ</td><td>bb</td><td>WW*</td><td>ZZ*</td><td>ττ</td><td>μμ</td></tr><tr><td>ZH(+30%, -80%)</td><td>(-17%, 19%)</td><td>(-7.3%, 7%)</td><td>(-4%, 3.3%)</td><td>(-4.5%, 4%)</td><td>(-4.9%, 4.4%)</td><td>(-3.6%, 3%)</td><td>(-3.6%, 3%)</td></tr><tr><td>ZH(-30%, +80%)</td><td>(-17%, 19%)</td><td>(-7.5%, 7.2%)</td><td>(-4.1%, 3.5%)</td><td>(-4.7%, 4.2%)</td><td>(-5.1%, 4.6%)</td><td>(-3.8%, 3.2%)</td><td>(-3.8%, 3.2%)</td></tr><tr><td>WWF(+30%, -80%)</td><td>(-17%, 18%)</td><td>(-7.2%, 7%)</td><td>(-3.9%, 3.3%)</td><td>(-4.4%, 3.9%)</td><td>(-4.9%, 4.3%)</td><td>(-3.5%, 2.9%)</td><td>(-3.5%, 2.9%)</td></tr><tr><td>WWF(-30%, +80%)</td><td>(-17%, 18%)</td><td>(-7.2%, 7%)</td><td>(-3.9%, 3.3%)</td><td>(-4.4%, 3.9%)</td><td>(-4.9%, 4.3%)</td><td>(-3.5%, 2.9%)</td><td>(-3.5%, 2.9%)</td></tr><tr><td>ZZF(+30%, -80%)</td><td>(-17%, 19%)</td><td>(-7.6%, 7.3%)</td><td>(-4.2%, 3.6%)</td><td>(-4.8%, 4.3%)</td><td>(-5.2%, 4.7%)</td><td>(-3.9%, 3.3%)</td><td>(-3.9%, 3.3%)</td></tr><tr><td>ZZF(-30%, +80%)</td><td>(-17%, 19%)</td><td>(-7.5%, 7.2%)</td><td>(-4.1%, 3.5%)</td><td>(-4.7%, 4.2%)</td><td>(-5.1%, 4.6%)</td><td>(-3.8%, 3.2%)</td><td>(-3.8%, 3.2%)</td></tr></table>

measurements to make sense at this accuracy level, one has to check carefully the top-loop induced contributions. If the machine is planned to run at  $350\mathrm{GeV}$ , it is likely that the top-quark operator coefficients will be determined directly through  $t\bar{t}$  production, except for the  $O_{t\varphi}$ . However, for the CEPC case a  $350\mathrm{GeV}$  run has not been officially planned, and therefore an interesting question is by how much the top-quark operators could change the Higgs cross sections below the  $t\bar{t}$  threshold through loops, given the current constraints. In fact, in table 3 we see that a top operator with a coefficient of order  $1/\mathrm{TeV}^2$  could already have visible effects.

In tables 10, 11 and 12 we present the possible deviations at lepton colliders, in a way similar to table 9 for the LHC. We consider two scenarios: 1)  $250\mathrm{GeV}$  run only, and we allow all top operators to vary within the current constraints. These results are given in table 10. 2) runs above  $t\bar{t}$  threshold are planned, which will fix all operator coefficients by direct production, except for  $C_{t\varphi}$ , and so only  $C_{t\varphi}$  is allowed to vary. Corresponding results are shown in tables 11 and 12, for 250 and  $350\mathrm{GeV}$  runs respectively. All these deviations are obtained with numerical results presented in table 3. For each process, two polarisations for  $(e^{+},e^{-})$  are considered.

In the first scenario, apart from the large deviations in the loop-induced decay  $\gamma \gamma$  and  $\gamma Z$ , a  $5 - 15\%$  level deviations are common in all channels. These results suggest that the current sensitivities to top-quark couplings can be already improved by up to an order of magnitude even with an  $e^{+}e^{-}$  collider below the  $t\bar{t}$  threshold. In the second

Table 12. Possible deviations in signal strengths (in percent) caused by top-quark operators, in Higgs production (WWF for WW fusion and ZZF for ZZ fusion) and decay channels, at an  $e^{+}e^{-}$  collider at 350 GeV centre-of-mass energy. Only the coefficient of  $O_{t\varphi}$  is allowed to vary within the current constraints, described in table 8.  

<table><tr><td></td><td>γγ</td><td>γZ</td><td>bb</td><td>WW*</td><td>ZZ*</td><td>ττ</td><td>μμ</td></tr><tr><td>ZH(+30%, -80%)</td><td>(-17%, 18%)</td><td>(-6.7%, 6.4%)</td><td>(-3.4%, 2.7%)</td><td>(-3.9%, 3.3%)</td><td>(-4.4%, 3.8%)</td><td>(-3%, 2.4%)</td><td>(-3%, 2.4%)</td></tr><tr><td>ZH(-30%, +80%)</td><td>(-17%, 19%)</td><td>(-7.3%, 7.1%)</td><td>(-4%, 3.4%)</td><td>(-4.5%, 4%)</td><td>(-5%, 4.4%)</td><td>(-3.6%, 3%)</td><td>(-3.6%, 3%)</td></tr><tr><td>WWF(+30%, -80%)</td><td>(-17%, 18%)</td><td>(-7.3%, 7%)</td><td>(-3.9%, 3.3%)</td><td>(-4.5%, 3.9%)</td><td>(-4.9%, 4.4%)</td><td>(-3.6%, 2.9%)</td><td>(-3.6%, 2.9%)</td></tr><tr><td>WWF(-30%, +80%)</td><td>(-17%, 18%)</td><td>(-7.3%, 7%)</td><td>(-3.9%, 3.3%)</td><td>(-4.5%, 3.9%)</td><td>(-4.9%, 4.4%)</td><td>(-3.6%, 2.9%)</td><td>(-3.6%, 2.9%)</td></tr><tr><td>ZZF(+30%, -80%)</td><td>(-17%, 19%)</td><td>(-7.7%, 7.4%)</td><td>(-4.3%, 3.7%)</td><td>(-4.9%, 4.3%)</td><td>(-5.3%, 4.8%)</td><td>(-4%, 3.4%)</td><td>(-4%, 3.4%)</td></tr><tr><td>ZZF(-30%, +80%)</td><td>(-17%, 19%)</td><td>(-7.6%, 7.4%)</td><td>(-4.3%, 3.7%)</td><td>(-4.8%, 4.3%)</td><td>(-5.2%, 4.7%)</td><td>(-3.9%, 3.3%)</td><td>(-3.9%, 3.3%)</td></tr></table>

scenario, deviations are smaller at  $\sim 5\%$ , but are sufficient to further pin down the top Yukawa coupling. More reliable estimates of the potential constraints that can be placed on top-quark couplings would require a global analysis including both the Higgs and the top operators, which we will leave for future studies.

# 5.3 Potential at high luminosity LHC

Given that the precision of Higgs measurements will be largely improved at the high luminosity LHC (HL-LHC), the potential  $\sim 5 - 10\%$  deviations in Higgs measurements can be used to place constraints on the top-quark operator coefficients. This does not mean that we will have 7 more free parameters to fit in the Higgs sector, because the top operators are also constrained by direct top-quark measurements. However, it is likely that one has to combine the two sectors to obtain the correct exclusion limits on both top and Higgs operators. To see if this is the case, in this section we will estimate the sensitivity of dim-6 top-loop effects at the HL-LHC at  $3000\mathrm{fb}^{-1}$ .

To this end, we perform a  $\chi^2$  analysis including all top operators but fixing all the Higgs operator coefficients to zero, at  $\mu_{EFT} = M_H = 125\mathrm{GeV}$  and at  $\mu_{EFT} = \Lambda = 1000\mathrm{GeV}$ . As discussed in the introduction, the first scale choice gives an estimate of sensitivity from a bottom-up point of view, while the second is from a top-down point view taking into account RG running and mixing effects. In the  $\chi^2$  analysis we assume the measured values will be exactly the same as the SM predictions. For the projection of future signal strength measurements, we follow ref. [83], where in table 3 the statistical and systematic errors for  $gg\rightarrow H$ , VBF,  $WH$  and  $ZH$  production, with  $ZZ^{*}$ ,  $\gamma \gamma$ ,  $WW^{*}$ ,  $\tau \tau$ ,  $\mu \mu$  decay channels are all documented. We take one half of the theory errors, to account for possible theory improvements in the future, and we have checked that in any case the resulting sensitivities are affected by theory errors only at the percent level. QCD corrections are potentially important, but they are likely to cancel in the signal strengths, when taking ratios w.r.t. SM cross sections, so we will not consider them. For the  $H\to bb$  channel we use ref. [84], where we have assumed that two-lepton and one-lepton channels correspond exactly to  $ZH$  and  $WH$  production. Finally we consider the  $Z\gamma$  signal strength taken from [85], assuming that the production channel is dominated by  $gg\to H$ .

Table 13. Sensitivity of Higgs measurements at HL-LHC to top-quark operators, compared with current constraints. Here sensitivity is defined as one half of the size of interval of coefficient  $C_i$  at 95% CL, assuming  $\Lambda = 1$  TeV, and all other operators coefficients are set to zero.  

<table><tr><td>Operator</td><td>Cφt</td><td>C(+)φQ</td><td>C(-)φQ</td><td>Cφtb</td><td>CtW</td><td>CtB</td><td>Ctφ</td></tr><tr><td>μEFT=125 GeV</td><td>2.5</td><td>1.3</td><td>3.2</td><td>9.3</td><td>0.2</td><td>0.07</td><td>0.9</td></tr><tr><td>μEFT=1000 GeV</td><td>1.3</td><td>0.5</td><td>4.3</td><td>1.3</td><td>0.6</td><td>0.08</td><td>0.9</td></tr><tr><td>Current</td><td>9.0</td><td>5.1</td><td>5.1</td><td>5.3</td><td>2.5</td><td>5.9</td><td>3.9</td></tr></table>

Top-operator contributions to signal strengths can be easily computed using results presented in tables 1 and 2. We assume that the percentage deviations do not change much from  $13\mathrm{TeV}$  to  $14\mathrm{TeV}$ . The modifications to the Higgs total width are taken into account. A specific  $X$ -like production channel may contain components from all five major production mechanisms, including ggF, VBF, WH, ZH and ttH. Numerical results for VBF, WH, ZH are presented in table 2, while for the other two channels we only need to take into account the leading effect from the top Yukawa operator  $O_{t\varphi}$ , which rescales the total cross section.

As we have mentioned in section 3.1, the consistency of precision EW observables is important for the results to be scheme independent. As explained in section 3, to simplify the analysis we assume that the  $S$  and  $T$  parameters are measured accurately and set them to zero. Thanks to our renormalisation scheme, this approximation simply means that we can exclude the operators  $O_{\varphi WB}$  and  $O_{\varphi D}$  from the analysis. We however take into account the  $U$  parameter which is scheme-independent up to dim-6. The current bound is  $\pm 0.1$ , taken from the PDG [52].

A total  $\chi^2$  is constructed by using Higgs data plus the  $U$  parameter. We truncate the  $\chi^2$  at the quadratic order in  $C$ , the Wilson coefficients. The one-sigma interval for any single parameter is given by  $\Delta \chi^2 = 1$ . The individual sensitivities on operator coefficients are given in table 13, where we compare the results of the two scenarios  $\mu_{EFT} = M_H = 125\mathrm{GeV}$ , and  $\mu_{EFT} = \Lambda = 1000\mathrm{GeV}$ , and the current constraints. Here, "sensitivity" is defined as one half of the size of interval of coefficient  $C_i$  at  $95\%$  CL, assuming  $\Lambda = 1\mathrm{TeV}$  and all other operators vanish. We can see that sensitivities on the first four coefficients are comparable with the current direct measurements. The last three coefficients are even more tightly constrained. This is mainly because they enter  $gg\rightarrow H$ ,  $H\rightarrow \gamma \gamma$  and/or  $H\rightarrow Z\gamma$ , where the relative deviations at dim-6 are large due to the loop suppression of the SM. From table 13 we can already conclude that Higgs measurements will provide useful information on top-quark operators.

The individual sensitivities do not fully reflect the constraining power of the combined analysis. To better study the structure of the  $\chi^2$ , we present the limits on each eigenstate

of the quadratic terms of  $\chi^2$ . This is done by writing

$$
\chi^ {2} = C M C ^ {T} \tag {5.1}
$$

where

$$
C = \left(C _ {\varphi t} C _ {\varphi Q} ^ {(+)} C _ {\varphi Q} ^ {(-)} C _ {\varphi t b} C _ {t W} C _ {t B} C _ {t \varphi}\right). \tag {5.2}
$$

By diagonalizing the matrix  $M \to M^D$ :

$$
\chi^ {2} = C U ^ {T} M ^ {D} U C ^ {T} \tag {5.3}
$$

we find seven linear combinations of operator coefficients, given by  $UCT$ , which are statistically independent. Then for the  $i$ th linear combination, the  $\chi^2$  is given by  $M_{ii}^{D}(UC^{T})_{i}^{2}$ , so the one-sigma limit on the  $i$ th combination will be  $M_{ii}^{D - \frac{1}{2}}$ . For  $\mu_{EFT} = 125\mathrm{GeV}$ , we find

$$
\begin{array}{l} \left( \begin{array}{c c c c c c c} - 0. 0 2 5 & 0. 0 4 5 & 0. 0 1 9 & 0. 0 0 5 & - 0. 4 3 & - 0. 9 & - 0. 0 4 1 \\ 0. 0 2 2 & - 0. 0 7 6 & - 0. 0 5 8 & - 0. 0 4 9 & 0. 4 2 & - 0. 2 5 & 0. 8 7 \\ 0. 0 0 1 2 & 0. 1 8 & 0. 0 6 8 & - 0. 0 3 3 & - 0. 7 7 & 0. 3 5 & 0. 4 9 \\ 0. 2 6 & - 0. 9 1 & - 0. 2 6 & 0. 0 0 9 9 & - 0. 2 1 & 0. 0 4 & 0. 0 0 9 9 \\ 0. 4 2 & 0. 2 7 & - 0. 5 4 & - 0. 6 8 & - 0. 0 0 2 & - 0. 0 0 9 5 & - 0. 0 6 4 \\ - 0. 4 8 & - 0. 2 6 & 0. 4 1 & - 0. 7 3 & - 0. 0 0 3 9 & 0. 0 0 7 6 & - 0. 0 2 1 \\ 0. 7 2 & - 0. 0 0 0 7 7 & 0. 6 8 & - 0. 0 9 5 & 0. 0 4 7 & - 0. 0 2 8 & - 0. 0 0 9 2 \end{array} \right) \\ \times \frac {1 \mathrm {T e V} ^ {2}}{\Lambda^ {2}} \left( \begin{array}{l} C _ {\varphi t} \\ C _ {\varphi Q} ^ {(+)} \\ C _ {\varphi Q} ^ {(-)} \\ C _ {\varphi t b} \\ C _ {t W} \\ C _ {t B} \\ C _ {t \varphi} \end{array} \right) = \pm \left( \begin{array}{l} 0. 0 3 2 6 \\ 0. 5 4 8 \\ 0. 6 3 7 \\ 2. 6 2 \\ 7. 3 1 \\ 1 9. 8 \\ 7 9. 6 \end{array} \right) \tag {5.4} \\ \end{array}
$$

We can see that all seven linear combinations can be constrained. Even though the last one may be too weak to give meaningful constraints, we will show that it can be significantly improved once differential distributions are taken into account. The first five numbers are all quite constraining.

To see where exactly these constraints come from, for each of the eigenstates given above, we compute the contribution from each measurement to the eigenvalue of  $\chi^2$ . Since the sensitivities given in eq. (5.4) are the inverse square root of these eigenvalues, the fraction for each measurement in the eigenvalue reflects the relative importance of that measurement in the direction that corresponds to the eigenvectors. To have a physical intuition about what is happening, below we give the most important operators in each of the seven eigenstates, and the measurements that contribute the largest fractions to the

corresponding  $\chi^2$ :

<table><tr><td>Eigenstates</td><td>Coefficients</td><td>Channels</td></tr><tr><td>1st</td><td>CtB(81%)</td><td>gg → H → γγ (84%)</td></tr><tr><td>2nd</td><td>Ctφ(75%), CtW(18%)</td><td>gg → H → ZZ*, γZ, μμ, WW* (77%)</td></tr><tr><td>3rd</td><td>CtW(59%), Ctφ(24%)</td><td>gg → H → γZ (42%), U (25%)</td></tr><tr><td>4th</td><td>C(+)φQ(82%)</td><td>U (68%), gg → H → γZ (28%)</td></tr><tr><td>5th</td><td>Cφtb(46%), C(-)φQ(29%)</td><td>VBF → ττ, ZZ*, γγ (64%), WH → ZZ*, γγ (16%)</td></tr><tr><td>6th</td><td>Cφtb(53%), Cφt(23%), C(-)φQ(17%)</td><td>ZH, WH → bb (59%) gg → H → μμ (17%)</td></tr><tr><td>7th</td><td>Cφt(52%), C(-)φQ(47%)</td><td>ggF, VBF → WW*(49%) WH, ZH → γγ (18%)</td></tr></table>

We can see, for example, the most constrained eigenvector, i.e. the 1st one, is mainly due to  $H \rightarrow \gamma \gamma$ . From eq. (5.4) we see that it places a constraint mainly on  $C_{tB}$ . This is due to its relatively large contributions to  $H \rightarrow \gamma \gamma$ . Similarly, the second one comes mostly from  $gg \rightarrow H$ . The constraint is mostly on  $C_{t\varphi}$  as it enters the  $ggH$  loop. The third and the fourth are two combinations of  $U$  parameter and  $gg \rightarrow H \rightarrow \gamma Z$ , and from the sensitivities we know that in the latter it is the  $H \rightarrow \gamma Z$  that leads to the bounds, on three most relevant operators. Until this point, the most useful information comes from processes that are loop-induced in the SM, from which tighter constraints are expected. The last three eigenvalues are dominated by corrections to tree-level processes in the SM, and mainly constrain the first four operators that give rise to vector-like  $ttV$  and  $tbW$  couplings. They rely mostly on the  $VH$  and VBF production channels and  $ZZ^{*}$ ,  $WW^{*}$  and  $b\bar{b}$  decay channels. This information is also given in figure 2 left, where the heights of the bars are the constraints of each eigenstate (in terms of  $\Lambda / \sqrt{C}$ ), and different colours indicate relative contributions of different measurements to this constraint, taking into account all decay channels and the  $U$  parameter measurement. For each decay channel all production modes are included. Similarly, the relative contributions from all production channels (with all decay modes grouped together) and the  $U$  parameter is given in figure 2 right.

Following the same procedure for  $\mu_{EFT} = 1000\mathrm{GeV}$ , we find the following eigenstates:

$$
\left( \begin{array}{c c c c c c c} - 0. 0 6 1 & - 0. 1 5 & 0. 0 1 6 & - 0. 0 4 5 & - 0. 1 3 & - 0. 9 8 & 0. 0 5 5 \\ - 0. 0 3 6 & - 0. 0 6 4 & 0. 0 1 3 & - 0. 4 & - 0. 3 8 & 0. 1 3 & 0. 8 2 \\ 0. 1 3 & 0. 0 0 5 4 & - 0. 0 1 8 & - 0. 1 7 & 0. 9 & - 0. 0 9 9 & 0. 3 6 \\ 0. 1 1 & 0. 4 6 & - 0. 0 9 1 & 0. 7 7 & - 0. 0 4 8 & - 0. 0 8 7 & 0. 4 \\ - 0. 0 1 9 & - 0. 8 4 & - 0. 3 1 & 0. 4 1 & 0. 0 3 5 & 0. 1 1 & 0. 1 4 \\ 0. 6 1 & 0. 1 2 & - 0. 7 3 & - 0. 2 1 & - 0. 1 1 & - 0. 0 5 1 & - 0. 0 9 7 \\ 0. 7 7 & - 0. 2 & 0. 6 & 0. 0 7 2 & - 0. 0 8 3 & 0. 0 0 1 2 & 0. 0 0 4 \end{array} \right)
$$

![](images/a62e115505514d65279044671b738daaf5d091b8e980e9ef6756d3881f829590.jpg)  
Figure 2. Sensitivities for each eigenstate, and the relative contributions from each channel for  $\mu_{EFT} = 125\mathrm{GeV}$ .

![](images/4f28f643ef53b32c47d57812893aee96e857dd457766e37d29ab6575f1514175.jpg)

![](images/13f9d986fbc0fd414e1c30ac789f4015ecb5bcc33f1037a6d4a555a55eead42a.jpg)  
Figure 3. Sensitivities for each eigenstates, and the relative contributions from each channel for  $\mu_{EFT} = 1000\mathrm{GeV}$ .

![](images/7000c5e0b94ee275de259da36873a779597924c8bb8076c940f84930d3aff6d1.jpg)

$$
\times \frac {1 \mathrm {T e V} ^ {2}}{\Lambda^ {2}} \left( \begin{array}{l} C _ {\varphi t} \\ C _ {\varphi Q} ^ {(+)} \\ C _ {\varphi Q} ^ {(-)} \\ C _ {\varphi t b} \\ C _ {t W} \\ C _ {t B} \\ C _ {t \varphi} \end{array} \right) = \pm \left( \begin{array}{l} 0. 0 4 1 \\ 0. 4 8 7 \\ 0. 6 3 8 \\ 1. 4 5 \\ 1. 5 5 \\ 5. 8 4 \\ 1 2. 7 \end{array} \right) \tag {5.5}
$$

The sensitivities are in general better due to the log enhanced terms. The most important channels for each eigenstate are slightly different. We show the channel decomposition in figure 3.

![](images/ef65c8c4cc304500e7c2e2945d078a778ddd9ced918ac0f697136ad58e640e86.jpg)

![](images/efabfdc5f55f4c21c204c40282e6eec32a76216a23586d1cf062bd65be0c5d26.jpg)

![](images/94b4c6084d3c09978ef869bd1e30fb2c241655beca8169855ca104ea043ea0f6.jpg)  
Figure 4. Sensitivity of the Higgs transverse momentum distribution (top) and  $ZH$  invariant mass distribution (bottom) in  $ZH$  production for the different operators at  $\mu_{EFT} = 1000\mathrm{GeV}$  (left) and  $\mu_{EFT} = 125\mathrm{GeV}$  (right).

![](images/333036a28764c32cfe0c8bb0956dbc32fed4772bf95ffc06d76bac48a3b7e7f0.jpg)

# 5.4 Improvements with differential distributions

Higher dimensional operators typically lead to different differential distributions than the SM, due to different Lorentz structures and sometimes an  $E^2 / \Lambda^2$  enhancement. This is expected also at the loop order, and therefore to fully exploit this behaviour, we study differential observables for the Higgs production processes, which can be easily simulated thanks to our implementation. Again, we show results both for  $\mu_{EFT} = \Lambda = 1 \mathrm{TeV}$  and for  $\mu_{EFT} = M_H = 125 \mathrm{GeV}$ .

As a representative sample of distributions, we show the transverse momentum of the Higgs and invariant mass distribution of the  $ZH$  system in  $ZH$  in figure 4, whilst the corresponding distributions for  $WH$  are shown in figure 5. For VBF we show the Higgs and hardest jet transverse momentum distributions in figure 6. The vertical axes are the bin-by-bin relative deviation w.r.t. the LO SM prediction, i.e. following the definition in eq. (4.4).

We find that in most cases, the impact of the operators increases in the tails giving larger deviations from the SM prediction than those obtained at the inclusive level. By comparing the two  $\mu_{EFT}$  scales we find significant differences related to the impact of the logarithmic terms, which are present in the predictions for  $\mu_{EFT} = 1000\mathrm{GeV}$  but absent at  $\mu_{EFT} = 125$ . In most cases the finite contributions which are the only ones present at  $\mu_{EFT} = 125$  are far from negligible. For  $VH$  production we find that the two observables we consider, i.e.  $p_T(H)$  and  $m(VH)$  show similar sensitivities at  $m(VH) \sim 2p_T(H)$ . Similarly

![](images/f07ea940d2084f1c1eb98f31bcc14ed06125638277d21a56bde096c961d57b17.jpg)

![](images/3ec06f3779096e3b682137647406d5e370f73d30fcda5129e75e6c8b28097656.jpg)

![](images/ff8ad341101182a383754dca3afec761a522ad4d950d218ac623ffd7b232df61.jpg)  
Figure 5. Sensitivity of the Higgs transverse momentum distribution (top) and  $WH$  invariant mass distribution (bottom) in  $WH$  production for the different operators at  $\mu_{EFT} = 1000\mathrm{GeV}$  (left) and  $\mu_{EFT} = 125\mathrm{GeV}$  (right).

![](images/5b81362ab5bc8cb5b3f5b856acb31a00ab514fcbdc45191ce78b02cd0ea1f4e9.jpg)

in VBF, the two  $p_T$  distributions show comparable effects but typically smaller than what is seen in  $VH$  production. An interesting observation is that  $O_{\varphi t}$  gives rise to a constant deviation in the  $WH$  production channel. As we have explained in section 4, this is due to the renormalisation scheme we are using, and the contribution enters only through Higgs wave-function renormalisation, so no different kinematics can be generated.

Given that the top-quark operators give rise to harder  $p_T(H)$  distributions, we could use the differential information to improve the sensitivity at the HL-LHC. To estimate the potential of differential measurements at HL-LHC, again we follow the approach in ref. [83], and assume that the number of events in the  $j$ th bin of an  $X$ -like measurement, from production channel  $i$  and decay channel  $f$ , is given by

$$
N _ {X \text {- l i k e}, i, f, j} ^ {S M} = r _ {j} ^ {X} N _ {X \text {- l i k e}, i, f} ^ {S M} \tag {5.6}
$$

where  $r_j^X$  is the ratio of the cross section of the  $j$ th bin with the total cross section for process  $i$ . For each production-like mode we use  $r_j^X$  only for the dominant production process and decay. The same assumption is made for the background. Theoretical errors are taken to be the same as the inclusive ones. Systematic errors are also scaled using  $r_j^X$ . Unlike ref. [83], we consider the differential distributions in all three channels:  $WH$ ,  $ZH$  and VBF, and use different binning. The  $r_j^X$  values as well as the deviations in the signal

![](images/8ed517cb4ac2bce50e24fcac11246373385b4f29a45ce3bf76e8b17617b51fbe.jpg)

![](images/490034310b40ed50868b63fddc38d4b96a51afd45cbcb91f35f212fdfa9a2e0f.jpg)

![](images/e7541cfbf52132b4f3b3e8cc915bc78a8493d699ca389d5f1d31da38ed9b67d7.jpg)  
Figure 6. Sensitivity of the Higgs (top) and hardest jet (bottom) transverse momentum distribution in VBF Higgs production for the different operators at  $\mu_{EFT} = 1000\mathrm{GeV}$  (left) and  $\mu_{EFT} = 125\mathrm{GeV}$  (right).

![](images/c9b083b1fff66a6bddacaad1fc4034d8ad7e4b9837aafc23e2f0434120c11859.jpg)

strength, i.e.  $\mu_{ij}$  in each  $p_T(H)$  bin, for all three production channels, are given in tables 16 and 17 in appendix A.

The resulting individual sensitivities are not significantly different than the inclusive analysis, as they are dominated by the loop-induced processes, such as  $gg \rightarrow H$ ,  $H \rightarrow \gamma \gamma$ ,  $\gamma Z$  where no distributions can be used. However, by looking into the eigenvalues of the  $\chi^2$  we find improvements in particular in the last three eigenvalues, which are mainly driven by the top-loop corrections to SM tree-level processes. For  $\mu_{EFT} = 125\mathrm{GeV}$  we have

$$
\left( \begin{array}{c c c c c c c} - 0. 0 2 5 & 0. 0 4 5 & 0. 0 1 9 & 0. 0 0 5 & - 0. 4 3 & - 0. 9 & - 0. 0 4 1 \\ 0. 0 2 4 & - 0. 0 7 3 & - 0. 0 5 8 & - 0. 0 5 1 & 0. 4 & - 0. 2 4 & 0. 8 8 \\ 0. 0 0 0 7 6 & 0. 1 9 & 0. 0 6 9 & - 0. 0 3 3 & - 0. 7 8 & 0. 3 6 & 0. 4 7 \\ - 0. 2 6 & 0. 9 1 & 0. 2 4 & - 0. 0 0 8 2 & 0. 2 1 & - 0. 0 4 3 & - 0. 0 0 9 7 \\ 0. 3 9 & 0. 2 8 & - 0. 6 4 & - 0. 6 & - 0. 0 0 6 7 & - 0. 0 0 7 6 & - 0. 0 6 4 \\ 0. 1 3 & 0. 2 & - 0. 5 7 & 0. 7 8 & - 0. 0 1 6 & 0. 0 0 5 1 & 0. 0 3 \\ 0. 8 7 & 0. 1 2 & 0. 4 4 & 0. 1 5 & 0. 0 4 5 & - 0. 0 3 & - 0. 0 0 4 3 \end{array} \right) \times \frac {1 \mathrm {T e V} ^ {2}}{\Lambda^ {2}} \left( \begin{array}{c} C _ {\varphi t} \\ C _ {\varphi Q} ^ {(+)} \\ C _ {\varphi Q} ^ {(-)} \\ C _ {\varphi t b} \\ C _ {t W} \\ C _ {t B} \\ C _ {t \varphi} \end{array} \right)
$$

$$
= \pm \left( \begin{array}{l} 0. 0 3 2 5 \\ 0. 5 4 3 \\ 0. 6 3 \\ 2. 5 3 \\ 6. 0 3 \\ 1 4. 8 \\ 3 2. 1 \end{array} \right), \text {c o m p a r e d w i t h} \left( \begin{array}{l} 0. 0 3 2 6 \\ 0. 5 4 8 \\ 0. 6 3 7 \\ 2. 6 2 \\ 7. 3 1 \\ 1 9. 8 \\ 7 9. 6 \end{array} \right) \text {f r o m i n c l u s i v e m e a s u r e m e n t s .} \tag {5.7}
$$

The improvement on the last eigenstate is about a factor of 2.5. On average, the Global Determinant Parameter (GDP) [86] of this fit is improved by a factor of 0.81 compared to the inclusive results, which is not huge, but it is very important that the weaker constraints receive larger improvements, which means that directions that were almost flat are now lifted. For  $\mu_{EFT} = 1$  TeV we find:

$$
\begin{array}{l} \left( \begin{array}{c c c c c c c} - 0. 0 6 1 & - 0. 1 5 & 0. 0 1 6 & - 0. 0 4 6 & - 0. 1 3 & - 0. 9 8 & 0. 0 5 4 \\ - 0. 0 3 4 & - 0. 0 6 5 & 0. 0 2 2 & - 0. 4 2 & - 0. 3 5 & 0. 1 2 & 0. 8 3 \\ 0. 1 3 & - 0. 0 0 4 2 & - 0. 0 1 6 & - 0. 1 7 & 0. 9 2 & - 0. 1 & 0. 3 2 \\ - 0. 1 2 & - 0. 2 4 & 0. 2 & - 0. 8 3 & 0. 0 3 & 0. 0 5 8 & - 0. 4 5 \\ - 0. 0 4 2 & - 0. 9 3 & - 0. 2 8 & 0. 2 & 0. 0 3 7 & 0. 1 3 & 0. 0 3 2 \\ 0. 5 2 & 0. 1 4 & - 0. 7 9 & - 0. 2 5 & - 0. 0 9 9 & - 0. 0 4 9 & - 0. 1 1 \\ 0. 8 3 & - 0. 1 8 & 0. 5 1 & 0. 0 5 6 & - 0. 0 9 6 & - 0. 0 0 5 6 & - 0. 0 0 4 2 \end{array} \right) \times \frac {1 \mathrm {T e V} ^ {2}}{\Lambda^ {2}} \left( \begin{array}{c} C _ {\varphi t} \\ C _ {\varphi Q} ^ {(+)} \\ C _ {\varphi Q} ^ {(-)} \\ C _ {\varphi t b} \\ C _ {t W} \\ C _ {t B} \\ C _ {t \varphi} \end{array} \right) \\ = \pm \left( \begin{array}{l} 0. 0 4 0 9 \\ 0. 4 7 9 \\ 0. 6 2 9 \\ 1. 3 \\ 1. 5 \\ 5. 4 4 \\ 1 0. 8 \end{array} \right), \text {c o m p a r e d w i t h} \left( \begin{array}{l} 0. 0 4 1 \\ 0. 4 8 7 \\ 0. 6 3 8 \\ 1. 4 5 \\ 1. 5 5 \\ 5. 8 4 \\ 1 2. 7 \end{array} \right) \text {f r o m i n c l u s i v e m e a s u r e m e n t s .} \tag {5.8} \\ \end{array}
$$

Improvements are smaller than the  $\mu_{EFT} = 125\mathrm{GeV}$  case.

In summary, after taking into account differential distributions, the one-sigma constraints on the seven linear combinations of top operator coefficients span the range from  $\mathcal{O}(10^{-2})\mathrm{TeV}^{-2}$  to  $\mathcal{O}(10)\mathrm{TeV}^{-2}$ . This reflects the HL-LHC potential on probing top-quark operators through EW loops. We summarise the individual and marginalised sensitivities in figure 7. They are not stronger than the current ones from direct top-quark measurements, but are definitely competitive. This means that in the near future the loop-induced effects cannot be neglected, and the only way to correctly take them into account is to perform global SMEFT fits by combining both the top-quark and the Higgs-boson sectors.

Figure 7. Individual and marginalised sensitivities (i.e. one-half of  $95\%$  CL interval) at HL-LHC through top loops, including differential measurements, compared with current individual limits.  $\mu_{EFT}$  is set at either  $M_H = 125\mathrm{GeV}$  or  $\Lambda = 1\mathrm{TeV}$ .  
![](images/14c435dbfbed702ee081dddbbe8dc04dbd274b0f7446865f510ca4bde0415c5b.jpg)  
Current individual  
Loop-induced individual  $\mu_{\mathrm{EFT}} = \mathbf{M}_{\mathrm{H}}$  
Loop-induced individual  $\mu_{\mathrm{EFT}} = \Lambda$  
Loop-induced marginalized  $\mu_{\mathrm{EFT}} = \mathrm{M_H}$  
Loop-induced marginalized  $\mu_{\mathrm{EFT}} = \Lambda$

# 5.5 Loop/tree discrimination

Until now we have focused on the sensitivities of the top operators, and have not considered the effects of Higgs operators at the tree level. In a real fit, one has to consider these contributions, and include sufficient observables so that no blind directions remain. In the following we briefly argue that, in principle, we can discriminate the tree-level contribution from Higgs operators and loop-level contribution from top operators, by only using Higgs measurements. This possibility relies on the finite non-logarithmic terms,  $\sigma_{\mathrm{fin}}$ , in eq. (1.1). The reason is that the logarithmic terms are completely captured by RG effects, and are thus process- and observable-independent. If one considers only these effects, the discrimination between top/Higgs operators would be impossible no matter how many observables are included.

As an example, consider the top-quark operator  $C_{tB}$  which mixes into  $C_{\varphi B}$  and  $C_{\varphi WB}$ . The latter mixing does not exist in our scheme as we renormalise it to a physical quantity. Consider the measurements  $H \rightarrow \gamma \gamma, \gamma Z, WW^{*}, ZZ^{*}$  and  $ZH / WH$  production. Another operator that enters these observables is  $O_{\varphi W}$ . Assuming all these processes are measured with  $10\%$  precision, we can construct a  $\chi^2$  and marginalise over the  $O_{\varphi W}$  operator. Taking  $\mu_{EFT} = 125 \mathrm{GeV}$ , after diagonalisation we find

$$
C _ {\varphi B} + 0. 0 2 1 C _ {t B} = \pm 0. 0 0 2 2 (\Lambda / 1 \mathrm {T e V}) ^ {2}, \tag {5.9}
$$

$$
C _ {t B} - 0. 0 2 1 C _ {\varphi B} = \pm 6. 7 (\Lambda / 1 \mathrm {T e V}) ^ {2}, \tag {5.10}
$$

so both directions are constrained and no blind direction is left.

On the other hand, if one takes  $\mu_{EFT} = 1$  TeV but only includes the logarithmic terms, the situation will be different. In this case we find

$$
C _ {\varphi B} - 0. 0 4 6 C _ {t B} = \pm 0. 0 0 2 2 (\Lambda / 1 \mathrm {T e V}) ^ {2}, \tag {5.11}
$$

$$
C _ {t B} + 0. 0 4 6 C _ {\varphi B} = \pm \infty (\Lambda / 1 \mathrm {T e V}) ^ {2}, \tag {5.12}
$$

![](images/c92d430682b6566f701794e7b455bbf0c348b5fade53fdf84fe7330992a542cd.jpg)  
Figure 8. Constraining both  $C_{tB}$  (top operator, loop level) and  $C_{\varphi B}$  (Higgs operator, tree level) by combining  $H \rightarrow ZZ^{*}$  and  $ZH$  production, assuming  $1\%$  precision on both.  $\mu_{EFT} = 125\mathrm{GeV}$ .  $\Lambda = 1\mathrm{TeV}$ .

so one combination is unconstrained. This demonstrates that the finite contributions in the SMEFT loop corrections are important, not only because their sizes can be large, but more importantly, because they allow us to discriminate the pure loop-induced effects from the tree-level contributions of other operators, into which they could mix, by combining various measurements, preferably at different energies, to eliminate possible unconstrained directions in a global fit. This is why we believe a study taking  $\mu_{EFT} = M_H = 125\mathrm{GeV}$  is a more reasonable estimate of sensitivities that can be achieved in a bottom-up global fit, where the discriminating power between loop- and tree-level effects is crucial for setting bounds on top operators. In figure 8 we illustrate that the  $H\rightarrow ZZ^{*}$  and  $ZH$  production are complementary in the  $C_{\varphi B} - C_{tB}$  plane.

Instead of combining several inclusive measurements, one could also use the differential information in one measurement. The differential distributions of the logarithmic terms can not be distinguished from the tree level ones, but they differ from the ones of the finite terms. In figure 9 we compare the normalised distributions (over the SM) from finite and log terms for the operators which show the most promising energy dependence in  $VH$  production. These plots demonstrate that indeed the kinematic behaviour of the finite and logarithmic terms can be very different, and so the kinematic distributions will serve as discriminating observables in a global fit, lifting the degeneracy between loop and tree-level contributions.

![](images/6b833a3b9cc24dbc05043c1555d62ccd88e600442302aea37adec391c3ec4954.jpg)  
Figure 9. Comparison of logarithmic and finite terms in the Higgs transverse momentum distribution in  $ZH$  and  $WH$  production for the different operators. The lower panels show the ratio of the finite over the logarithmic terms.

![](images/ceda27d0ff9970850ff4e291d6eaafb8fd13675c3f601c9eb3ab6b1c99748b45.jpg)

# 6 Conclusion

We have computed the NLO EW corrections to Higgs production and decay processes from dim-6 top-quark operators in the SMEFT framework. We have studied the major production channels including VBF,  $WH$  and  $ZH$  at the LHC,  $ZH$  and VBF at  $e^{+}e^{-}$  colliders, and the major decay channels including  $H\rightarrow \gamma \gamma ,\gamma Z,Zll,Wl\nu ,bb,\mu \mu ,\tau \tau$ . These results are part of the ongoing efforts of automating SMEFT simulations for colliders at NLO, and is a first step towards including EW corrections.

These results allow us to study whether the Higgs measurements at the LHC and future colliders are sensitive to possible deviations in the top-quark sector. We find that, within the current direct constraints on the top-quark sector, the top-quark operators can shift the signal strength of the loop-induced Higgs processes, i.e.  $gg \rightarrow H$  and  $H \rightarrow \gamma \gamma$ ,  $\gamma Z$  by factors  $\sim \mathcal{O}(1) - \mathcal{O}(10)$ , and that of the tree-level processes, i.e. all remaining production and decay channels, by  $\sim 5 - 10\%$  through loop corrections at the LHC and up to  $15\%$  at future lepton colliders. This implies that with the current precision we can already learn about top-quark couplings by using EW loops in Higgs measurements, while in the future, at the high-luminosity scenario, all Higgs measurements can be sensitive to top-quark couplings. It also implies that at an  $e^{+}e^{-}$  collider, even measurements below the  $t\bar{t}$  threshold can be sensitive to deviations in top-quark couplings. As a result, in a global fit for Higgs couplings based on the SMEFT approach, theoretical uncertainties due to unknown top-quark operators are not negligible and should be taken into account.

These results also allow us to quantitatively derive the experimental sensitivities to top-quark operators at the HL-LHC, by only using the Higgs observables. Using projected in-

clusive measurements, we are able to constrain all directions in the 7-dimensional parameter space spanned by all seven operator coefficients. We have also studied the change of differential distributions from top-quark operators, and have found that the signal/background ratio is enhanced at the tail of the distributions. By considering the  $p_T(H)$  distributions in VBF,  $WH$  and  $ZH$  production processes, we have significantly improved the sensitivities on the most weakly constrained eigenvectors. The resulting one-sigma range on the seven eigenvectors of Wilson coefficients span the range from  $\mathcal{O}(10^{-2})\mathrm{TeV}^{-2}$  to  $\mathcal{O}(10)\mathrm{TeV}^{-2}$ .

Finally, we have briefly discussed possible ways to discriminate the loop-level top-quark operator contributions from the tree-level Higgs operator contributions, which is necessary in a global fit. We have demonstrated that this can be done by combining several observables or looking into the differential distributions, and that the crucial information is supplied by the finite (i.e. non-logarithmic) terms in the full NLO EW corrections. Therefore, even though they cannot be obtained using the RG matrix, it is very important to compute these finite terms for an actual SMEFT fit.

In conclusion, as the experimental precision on Higgs measurements continues to improve, the NLO EW corrections from dim-6 top-quark operators via top-loop effects have started to become relevant. For this reason, treating the dim-6 top-quark sector and the Higgs/EW sector separately may not continue to be a good strategy. A global SMEFT analysis taking into account both sectors by combining Higgs and top-quark measurements is desirable. Our calculation is a first step towards this direction, and our implementation in the MG5_aMC framework provides an automatic and realistic simulation tool for this purpose.

# Acknowledgments

We thank F. Maltoni and X. Zhao for useful discussions and comments on the manuscript, and O. Mattelaer for technical assistance with the reweighting module in MG5_aMC. CZ thanks M. Trotter for a discussion about the renormalisation scheme. CZ is supported by IHEP under Contract No. Y7515540U1. EV is supported by a Marie Skłodowska-Curie Individual Fellowship of the European Commission's Horizon 2020 Programme under contract number 704187 HEFTinLOOPS.

# A More numerical results

In tables 14 and 15 we present results similar to tables 1 and 2 but with the standard  $MS$  scheme. In tables 16 and 17 we show the  $r_j^X$  values for the distributions we consider in section 5.4, as well as the deviations in the signal strength, i.e.  $\mu_{ij}$  in each  $p_T(H)$  bin, for all three production channels.

Table 14. Percentage deviation  ${\mu }_{ij}$  for decay channel  $i$  and operator  $j$  ,in the  $\overline{MS}$  scheme.  

<table><tr><td>channel</td><td>μEFT [GeV]</td><td>Oφt</td><td>O(+)φQ</td><td>O(-)φQ</td><td>Oφtb</td><td>OtW</td><td>OtB</td><td>Otφ</td></tr><tr><td>H → bb</td><td>125</td><td>0</td><td>-0.07</td><td>0.11</td><td>-1.13</td><td>-0.28</td><td>0</td><td>-0.18</td></tr><tr><td>H → bb</td><td>1000</td><td>0</td><td>-0.99</td><td>-0.91</td><td>-8.18</td><td>0.34</td><td>0</td><td>0.29</td></tr><tr><td>H → ll</td><td>125</td><td>0</td><td>-0.02</td><td>0.02</td><td>-0.00</td><td>0</td><td>0</td><td>-0.27</td></tr><tr><td>H → ll</td><td>1000</td><td>0</td><td>0.45</td><td>-0.45</td><td>-0.03</td><td>0</td><td>0</td><td>0.68</td></tr><tr><td>H → γγ</td><td>125</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-73.3</td><td>-136.8</td><td>3.45</td></tr><tr><td>H → γγ</td><td>1000</td><td>0</td><td>0</td><td>0</td><td>0</td><td>114.6</td><td>214.0</td><td>3.45</td></tr><tr><td>H → Zγ</td><td>125</td><td>1.77</td><td>0.03</td><td>1.77</td><td>0</td><td>-45.8</td><td>6.97</td><td>0.72</td></tr><tr><td>H → Zγ</td><td>1000</td><td>1.77</td><td>0.03</td><td>1.77</td><td>0</td><td>71.3</td><td>-9.69</td><td>0.72</td></tr><tr><td>H → Zll</td><td>125</td><td>-0.65</td><td>-0.07</td><td>0.65</td><td>-0.00</td><td>0.22</td><td>-0.02</td><td>0.08</td></tr><tr><td>H → Zll</td><td>1000</td><td>0.88</td><td>0.47</td><td>-1.49</td><td>-0.04</td><td>-0.16</td><td>0.11</td><td>0.08</td></tr><tr><td>H → Wlν</td><td>125</td><td>0</td><td>-0.25</td><td>0.25</td><td>0.00</td><td>-0.13</td><td>0</td><td>-0.03</td></tr><tr><td>H → Wlν</td><td>1000</td><td>0</td><td>1.08</td><td>-1.08</td><td>-0.08</td><td>0.33</td><td>0</td><td>-0.03</td></tr></table>

Table 15. Percentage deviation  $\mu_{ij}$  for production channel  $i$  and operator  $j$ , in the  $\overline{MS}$  scheme.  

<table><tr><td>channel</td><td>μEFT [GeV]</td><td>Oφt</td><td>O(+)φQ</td><td>O(-)φQ</td><td>Oφtb</td><td>OtW</td><td>OtB</td><td>Otφ</td></tr><tr><td>pp → ZH</td><td>125</td><td>-0.44</td><td>0.16</td><td>0.33</td><td>0.00</td><td>0.80</td><td>-0.29</td><td>-0.02</td></tr><tr><td>pp → ZH</td><td>1000</td><td>1.45</td><td>-0.64</td><td>-1.05</td><td>-0.02</td><td>-1.53</td><td>0.93</td><td>-0.02</td></tr><tr><td>pp → WH</td><td>125</td><td>0</td><td>-0.06</td><td>0.06</td><td>-0.00</td><td>0.43</td><td>0</td><td>-0.21</td></tr><tr><td>pp → WH</td><td>1000</td><td>0</td><td>0.18</td><td>-0.18</td><td>-0.08</td><td>-4.09</td><td>0</td><td>-0.21</td></tr><tr><td>pp → Hjj</td><td>125</td><td>-0.21</td><td>-0.25</td><td>0.46</td><td>0.01</td><td>0.04</td><td>-0.02</td><td>0.03</td></tr><tr><td>pp → Hjj</td><td>1000</td><td>0.36</td><td>1.10</td><td>-1.48</td><td>-0.06</td><td>0.36</td><td>0.09</td><td>0.03</td></tr></table>

Table 16.  $r$  values and percentage deviations  ${\mu }_{ij}$  for VBF,  ${WH}$  and  ${ZH}$  production in 11 bins of the  ${p}_{T}\left( H\right)$  distribution at  ${\mu }_{EFT} = {125}\mathrm{{GeV}}$  .  

<table><tr><td>Bin [GeV]</td><td>Channel</td><td>r value</td><td>\(O_{\varphi t}\)</td><td>\(O_{\varphi Q}^{(+)}\)</td><td>\(O_{\varphi Q}^{(-)}\)</td><td>\(O_{\varphi tb}\)</td><td>\(O_{tW}\)</td><td>\(O_{tB}\)</td><td>\(O_{t\varphi}\)</td></tr><tr><td rowspan="3">0-50</td><td>VBF</td><td>0.22</td><td>-0.24</td><td>-0.22</td><td>0.47</td><td>0.01</td><td>-0.19</td><td>-0.03</td><td>0.02</td></tr><tr><td>WH</td><td>0.35</td><td>-0.15</td><td>-0.16</td><td>0.31</td><td>0.00</td><td>0.69</td><td>0.00</td><td>-0.25</td></tr><tr><td>ZH</td><td>0.34</td><td>-0.42</td><td>-0.01</td><td>0.35</td><td>0.00</td><td>0.98</td><td>-0.10</td><td>0.02</td></tr><tr><td rowspan="3">50-100</td><td>VBF</td><td>0.37</td><td>-0.25</td><td>-0.22</td><td>0.47</td><td>0.01</td><td>-0.04</td><td>0.00</td><td>0.02</td></tr><tr><td>WH</td><td>0.38</td><td>-0.15</td><td>-0.18</td><td>0.32</td><td>0.00</td><td>0.47</td><td>0.00</td><td>-0.24</td></tr><tr><td>ZH</td><td>0.38</td><td>-0.35</td><td>0.05</td><td>0.30</td><td>0.00</td><td>1.00</td><td>-0.08</td><td>0.00</td></tr><tr><td rowspan="3">100-150</td><td>VBF</td><td>0.23</td><td>-0.27</td><td>-0.22</td><td>0.50</td><td>0.01</td><td>0.09</td><td>0.01</td><td>0.03</td></tr><tr><td>WH</td><td>0.16</td><td>-0.15</td><td>-0.14</td><td>0.29</td><td>0.00</td><td>0.11</td><td>0.00</td><td>-0.19</td></tr><tr><td>ZH</td><td>0.17</td><td>-0.13</td><td>0.20</td><td>0.25</td><td>0.00</td><td>0.99</td><td>0.01</td><td>-0.07</td></tr><tr><td rowspan="3">150-200</td><td>VBF</td><td>0.1</td><td>-0.29</td><td>-0.24</td><td>0.55</td><td>0.01</td><td>0.26</td><td>0.00</td><td>0.04</td></tr><tr><td>WH</td><td>0.062</td><td>-0.15</td><td>0.04</td><td>0.10</td><td>0.01</td><td>-0.10</td><td>0.00</td><td>-0.13</td></tr><tr><td>ZH</td><td>0.066</td><td>0.00</td><td>0.50</td><td>0.09</td><td>0.00</td><td>0.85</td><td>0.06</td><td>-0.13</td></tr><tr><td rowspan="3">200-250</td><td>VBF</td><td>0.043</td><td>-0.32</td><td>-0.27</td><td>0.63</td><td>0.01</td><td>0.46</td><td>0.00</td><td>0.06</td></tr><tr><td>WH</td><td>0.026</td><td>-0.15</td><td>0.42</td><td>-0.27</td><td>0.01</td><td>-0.12</td><td>0.00</td><td>-0.07</td></tr><tr><td>ZH</td><td>0.027</td><td>-0.07</td><td>0.97</td><td>-0.19</td><td>0.00</td><td>0.93</td><td>0.00</td><td>-0.11</td></tr><tr><td rowspan="3">250-300</td><td>VBF</td><td>0.018</td><td>-0.33</td><td>-0.36</td><td>0.73</td><td>0.01</td><td>0.73</td><td>-0.01</td><td>0.07</td></tr><tr><td>WH</td><td>0.012</td><td>-0.15</td><td>1.10</td><td>-0.91</td><td>0.02</td><td>0.02</td><td>0.00</td><td>-0.01</td></tr><tr><td>ZH</td><td>0.012</td><td>-0.18</td><td>1.60</td><td>-0.63</td><td>0.00</td><td>1.10</td><td>-0.10</td><td>-0.07</td></tr><tr><td rowspan="3">300-350</td><td>VBF</td><td>0.0087</td><td>-0.37</td><td>-0.50</td><td>0.93</td><td>0.01</td><td>0.85</td><td>-0.02</td><td>0.10</td></tr><tr><td>WH</td><td>0.0063</td><td>-0.15</td><td>1.90</td><td>-1.70</td><td>0.03</td><td>0.22</td><td>0.00</td><td>0.05</td></tr><tr><td>ZH</td><td>0.0056</td><td>-0.26</td><td>2.50</td><td>-1.30</td><td>0.00</td><td>1.30</td><td>-0.19</td><td>-0.01</td></tr><tr><td rowspan="3">350-400</td><td>VBF</td><td>0.0038</td><td>-0.42</td><td>-0.66</td><td>1.20</td><td>0.02</td><td>1.00</td><td>-0.04</td><td>0.12</td></tr><tr><td>WH</td><td>0.0034</td><td>-0.15</td><td>3.10</td><td>-2.90</td><td>0.03</td><td>0.49</td><td>0.00</td><td>0.11</td></tr><tr><td>ZH</td><td>0.0033</td><td>-0.31</td><td>4.00</td><td>-2.50</td><td>0.00</td><td>1.70</td><td>-0.35</td><td>0.06</td></tr><tr><td rowspan="3">400-450</td><td>VBF</td><td>0.002</td><td>-0.41</td><td>-0.96</td><td>1.40</td><td>0.02</td><td>1.80</td><td>-0.04</td><td>0.13</td></tr><tr><td>WH</td><td>0.002</td><td>-0.15</td><td>4.60</td><td>-4.40</td><td>0.04</td><td>0.70</td><td>0.00</td><td>0.15</td></tr><tr><td>ZH</td><td>0.0017</td><td>-0.31</td><td>5.10</td><td>-3.40</td><td>0.00</td><td>1.70</td><td>-0.40</td><td>0.10</td></tr><tr><td rowspan="3">450-500</td><td>VBF</td><td>0.00098</td><td>-0.48</td><td>-1.20</td><td>1.70</td><td>0.02</td><td>1.90</td><td>-0.06</td><td>0.16</td></tr><tr><td>WH</td><td>0.0014</td><td>-0.15</td><td>6.20</td><td>-6.00</td><td>0.04</td><td>1.00</td><td>0.00</td><td>0.20</td></tr><tr><td>ZH</td><td>0.0011</td><td>-0.24</td><td>6.50</td><td>-4.50</td><td>0.00</td><td>1.80</td><td>-0.45</td><td>0.15</td></tr><tr><td rowspan="3">500+</td><td>VBF</td><td>0.0014</td><td>-0.58</td><td>-2.50</td><td>3.00</td><td>0.03</td><td>3.00</td><td>-0.10</td><td>0.21</td></tr><tr><td>WH</td><td>0.0024</td><td>-0.15</td><td>14.00</td><td>-14.00</td><td>0.05</td><td>1.90</td><td>0.00</td><td>0.32</td></tr><tr><td>ZH</td><td>0.0021</td><td>0.35</td><td>15.00</td><td>-12.00</td><td>0.00</td><td>2.40</td><td>-0.71</td><td>0.29</td></tr></table>

Table 17.  $r$  values and percentage deviations  ${\mu }_{ij}$  for VBF,  ${WH}$  and  ${ZH}$  production in 11 bins of the  ${p}_{T}\left( H\right)$  distribution at  ${\mu }_{EFT} = 1\mathrm{{TeV}}$  .  

<table><tr><td>Bin [GeV]</td><td>Channel</td><td>r value</td><td>\(O_{\varphi t}\)</td><td>\(O_{\varphi Q}^{(+)}\)</td><td>\(O_{\varphi Q}^{(-)}\)</td><td>\(O_{\varphi tb}\)</td><td>\(O_{tW}\)</td><td>\(O_{tB}\)</td><td>\(O_{t\varphi}\)</td></tr><tr><td rowspan="3">0-50</td><td>VBF</td><td>0.22</td><td>0.70</td><td>0.82</td><td>-1.50</td><td>-0.05</td><td>0.60</td><td>0.00</td><td>0.02</td></tr><tr><td>WH</td><td>0.35</td><td>0.79</td><td>0.13</td><td>-0.93</td><td>-0.05</td><td>-3.40</td><td>0.00</td><td>-0.25</td></tr><tr><td>ZH</td><td>0.34</td><td>0.50</td><td>0.37</td><td>-0.98</td><td>-0.05</td><td>-2.30</td><td>-0.45</td><td>0.02</td></tr><tr><td rowspan="3">50-100</td><td>VBF</td><td>0.37</td><td>0.69</td><td>0.85</td><td>-1.50</td><td>-0.05</td><td>0.37</td><td>-0.01</td><td>0.02</td></tr><tr><td>WH</td><td>0.38</td><td>0.79</td><td>-0.10</td><td>-0.69</td><td>-0.05</td><td>-4.00</td><td>0.00</td><td>-0.24</td></tr><tr><td>ZH</td><td>0.38</td><td>0.56</td><td>0.23</td><td>-0.84</td><td>-0.05</td><td>-2.70</td><td>-0.45</td><td>0.00</td></tr><tr><td rowspan="3">100-150</td><td>VBF</td><td>0.23</td><td>0.67</td><td>0.95</td><td>-1.60</td><td>-0.04</td><td>0.20</td><td>0.00</td><td>0.03</td></tr><tr><td>WH</td><td>0.16</td><td>0.79</td><td>-0.55</td><td>-0.24</td><td>-0.05</td><td>-4.90</td><td>0.00</td><td>-0.19</td></tr><tr><td>ZH</td><td>0.17</td><td>0.73</td><td>-0.05</td><td>-0.48</td><td>-0.05</td><td>-3.20</td><td>-0.38</td><td>-0.07</td></tr><tr><td rowspan="3">150-200</td><td>VBF</td><td>0.1</td><td>0.65</td><td>1.10</td><td>-1.70</td><td>-0.04</td><td>0.00</td><td>0.01</td><td>0.04</td></tr><tr><td>WH</td><td>0.062</td><td>0.79</td><td>-1.10</td><td>0.30</td><td>-0.04</td><td>-5.40</td><td>0.00</td><td>-0.13</td></tr><tr><td>ZH</td><td>0.066</td><td>0.79</td><td>-0.43</td><td>0.01</td><td>-0.05</td><td>-3.70</td><td>-0.35</td><td>-0.13</td></tr><tr><td rowspan="3">200-250</td><td>VBF</td><td>0.043</td><td>0.64</td><td>1.30</td><td>-1.90</td><td>-0.04</td><td>-0.20</td><td>0.00</td><td>0.06</td></tr><tr><td>WH</td><td>0.026</td><td>0.79</td><td>-1.70</td><td>0.88</td><td>-0.04</td><td>-5.50</td><td>0.00</td><td>-0.07</td></tr><tr><td>ZH</td><td>0.027</td><td>0.61</td><td>-0.86</td><td>0.58</td><td>-0.05</td><td>-3.80</td><td>-0.42</td><td>-0.11</td></tr><tr><td rowspan="3">250-300</td><td>VBF</td><td>0.018</td><td>0.63</td><td>1.50</td><td>-2.00</td><td>-0.04</td><td>-0.47</td><td>0.00</td><td>0.07</td></tr><tr><td>WH</td><td>0.012</td><td>0.79</td><td>-2.30</td><td>1.50</td><td>-0.03</td><td>-5.50</td><td>0.00</td><td>-0.01</td></tr><tr><td>ZH</td><td>0.012</td><td>0.37</td><td>-1.30</td><td>1.20</td><td>-0.05</td><td>-3.80</td><td>-0.52</td><td>-0.07</td></tr><tr><td rowspan="3">300-350</td><td>VBF</td><td>0.0087</td><td>0.61</td><td>1.80</td><td>-2.20</td><td>-0.04</td><td>-0.43</td><td>-0.02</td><td>0.10</td></tr><tr><td>WH</td><td>0.0063</td><td>0.79</td><td>-2.80</td><td>2.10</td><td>-0.03</td><td>-5.30</td><td>0.00</td><td>0.05</td></tr><tr><td>ZH</td><td>0.0056</td><td>0.13</td><td>-1.70</td><td>1.80</td><td>-0.05</td><td>-3.60</td><td>-0.62</td><td>-0.01</td></tr><tr><td rowspan="3">350-400</td><td>VBF</td><td>0.0038</td><td>0.58</td><td>2.00</td><td>-2.50</td><td>-0.04</td><td>-0.32</td><td>-0.04</td><td>0.12</td></tr><tr><td>WH</td><td>0.0034</td><td>0.79</td><td>-3.40</td><td>2.60</td><td>-0.02</td><td>-5.10</td><td>0.00</td><td>0.11</td></tr><tr><td>ZH</td><td>0.0033</td><td>-0.14</td><td>-2.20</td><td>2.50</td><td>-0.05</td><td>-3.60</td><td>-0.80</td><td>0.06</td></tr><tr><td rowspan="3">400-450</td><td>VBF</td><td>0.002</td><td>0.60</td><td>2.30</td><td>-2.70</td><td>-0.03</td><td>-1.20</td><td>-0.04</td><td>0.13</td></tr><tr><td>WH</td><td>0.002</td><td>0.79</td><td>-3.90</td><td>3.10</td><td>-0.02</td><td>-5.00</td><td>0.00</td><td>0.15</td></tr><tr><td>ZH</td><td>0.0017</td><td>-0.32</td><td>-2.50</td><td>2.90</td><td>-0.05</td><td>-3.30</td><td>-0.82</td><td>0.10</td></tr><tr><td rowspan="3">450-500</td><td>VBF</td><td>0.00098</td><td>0.58</td><td>2.60</td><td>-2.90</td><td>-0.03</td><td>-0.96</td><td>-0.07</td><td>0.16</td></tr><tr><td>WH</td><td>0.0014</td><td>0.79</td><td>-4.20</td><td>3.40</td><td>-0.01</td><td>-4.60</td><td>0.00</td><td>0.20</td></tr><tr><td>ZH</td><td>0.0011</td><td>-0.55</td><td>-2.80</td><td>3.30</td><td>-0.05</td><td>-3.10</td><td>-0.89</td><td>0.15</td></tr><tr><td rowspan="3">500+</td><td>VBF</td><td>0.0014</td><td>0.55</td><td>3.20</td><td>-3.50</td><td>-0.03</td><td>-1.30</td><td>-0.08</td><td>0.21</td></tr><tr><td>WH</td><td>0.0024</td><td>0.79</td><td>-4.80</td><td>4.00</td><td>0.00</td><td>-3.70</td><td>0.00</td><td>0.32</td></tr><tr><td>ZH</td><td>0.0021</td><td>-0.96</td><td>-3.10</td><td>4.00</td><td>-0.05</td><td>-2.80</td><td>-1.20</td><td>0.29</td></tr></table>

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] S. Weinberg, Phenomenological Lagrangians, Physica A 96 (1979) 327 [INSPIRE].  
[2] W. Buchmüller and D. Wyler, *Effective Lagrangian analysis of new interactions and flavor conservation*, Nucl. Phys. B **268** (1986) 621 [INSPIRE].  
[3] C.N. Leung, S.T. Love and S. Rao, Low-energy manifestations of a new interaction scale: operator analysis, Z. Phys. C 31 (1986) 433 [INSPIRE].  
[4] A. Buckley et al., Global fit of top quark effective theory to data, Phys. Rev. D 92 (2015) 091501 [arXiv:1506.08845] [INSPIRE].  
[5] A. Buckley et al., Constraining top quark effective theory in the LHC run II era, JHEP 04 (2016) 015 [arXiv:1512.03360] [INSPIRE].  
[6] V. Cirigliano, W. Dekens, J. de Vries and E. Mereghetti, Constraining the top-Higgs sector of the Standard Model effective field theory, Phys. Rev. D 94 (2016) 034031 [arXiv:1605.04311] [INSPIRE].  
[7] M.P. Rosello and M. Vos, Constraints on four-fermion interactions from the  $\bar{t} \bar{t}$  charge asymmetry at hadron colliders, Eur. Phys. J. C 76 (2016) 200 [arXiv:1512.07542] [INSPIRE].  
[8] J. de Blas, M. Chala and J. Santiago, Renormalization group constraints on new top interactions from electroweak precision data, JHEP 09 (2015) 189 [arXiv:1507.00757] [INSPIRE].  
[9] S. Alioli, V. Cirigliano, W. Dekens, J. de Vries and E. Mereghetti, Right-handed charged currents in the era of the Large Hadron Collider, JHEP 05 (2017) 086 [arXiv:1703.04751] [INSPIRE].  
[10] C. Bernardo et al., Studying the Wtb vertex structure using recent LHC results, Phys. Rev. D 90 (2014) 113007 [arXiv:1408.7063] [INSPIRE].  
[11] A. Tonero and R. Rosenfeld, Dipole-induced anomalous top quark couplings at the LHC, Phys. Rev. D 90 (2014) 017701 [arXiv:1404.2581] [INSPIRE].  
[12] Q.-H. Cao, B. Yan, J.-H. Yu and C. Zhang, A general analysis of Wtb anomalous couplings, Chin. Phys. C 41 (2017) 063101 [arXiv:1504.03785] [INSPIRE].  
[13] S. Jung, P. Ko, Y.W. Yoon and C. Yu, Renormalization group-induced phenomena of top pairs from four-quark effective operators, JHEP 08 (2014) 120 [arXiv:1406.4570] [INSPIRE].  
[14] C. Zhang, N. Greiner and S. Willenbrock, Constraints on non-standard top quark couplings, Phys. Rev. D 86 (2012) 014024 [arXiv:1201.6670] [INSPIRE].  
[15] N. Greiner, S. Willenbrock and C. Zhang, Effective field theory for nonstandard top quark couplings, Phys. Lett. B 704 (2011) 218 [arXiv:1104.3122] [INSPIRE].  
[16] T. Corbett, O.J.P. Eboli, J. Gonzalez-Fraile and M.C. Gonzalez-Garcia, Robust determination of the Higgs couplings: power to the data, Phys. Rev. D 87 (2013) 015022 [arXiv:1211.4580] [INSPIRE].

[17] A. Butter, O.J.P. Éboli, J. Gonzalez-Fraile, M.C. Gonzalez-Garcia, T. Plehn and M. Rauch, The gauge-Higgs legacy of the LHC run I, JHEP 07 (2016) 152 [arXiv:1604.03105] [INSPIRE].  
[18] C. Englert, R. Kogler, H. Schulz and M. Spannowsky, *Higgs coupling measurements at the LHC*, Eur. Phys. J. C **76** (2016) 393 [arXiv:1511.05170] [INSPIRE].  
[19] A. Falkowski, M. Gonzalez-Alonso, A. Greljo and D. Marzocca, Global constraints on anomalous triple gauge couplings in effective field theory approach, Phys. Rev. Lett. 116 (2016) 011801 [arXiv:1508.00581] [INSPIRE].  
[20] A. Falkowski and F. Riva, Model-independent precision constraints on dimension-6 operators, JHEP 02 (2015) 039 [arXiv:1411.0669] [INSPIRE].  
[21] J. Ellis, V. Sanz and T. You, Complete Higgs sector constraints on dimension-6 operators, JHEP 07 (2014) 036 [arXiv:1404.3667] [INSPIRE].  
[22] J. Ellis, V. Sanz and T. You, The effective Standard Model after LHC run I, JHEP 03 (2015) 157 [arXiv:1410.7703] [INSPIRE].  
[23] J. Ellis, C.W. Murphy, V. Sanz and T. You, Updated global SMEFT fit to Higgs, diboson and electroweak data, JHEP 06 (2018) 146 [arXiv:1803.03252] [INSPIRE].  
[24] C. Degrande, J.M. Gerard, C. Grojean, F. Maltoni and G. Servant, Probing top-Higgs non-standard interactions at the LHC, JHEP 07 (2012) 036 [Erratum ibid. 03 (2013) 032] [arXiv:1205.1065] [INSPIRE].  
[25] N. Deutschmann, C. Duhr, F. Maltoni and E. Vryonidou, Gluon-fusion Higgs production in the Standard Model effective field theory, JHEP 12 (2017) 063 [Erratum ibid. 02 (2018) 159] [arXiv:1708.00460] [INSPIRE].  
[26] O. Bessidskaia Bylund, F. Maltoni, I. Tsinikos, E. Vryonidou and C. Zhang, Probing top quark neutral couplings in the Standard Model effective field theory at NLO in QCD, JHEP 05 (2016) 052 [arXiv:1601.08193] [INSPIRE].  
[27] C. Englert, R. Rosenfeld, M. Spannowsky and A. Tonero, New physics and signal-background interference in associated pp  $\rightarrow$  HZ production, EPL 114 (2016) 31001 [arXiv:1603.05304] [INSPIRE].  
[28] F. Maltoni, E. Vryonidou and C. Zhang, Higgs production in association with a top-antitop pair in the Standard Model effective field theory at NLO in QCD, JHEP 10 (2016) 123 [arXiv:1607.05330] [INSPIRE].  
[29] C. Hartmann and M. Trot, On one-loop corrections in the Standard Model effective field theory; the  $\Gamma(h \to \gamma \gamma)$  case, JHEP 07 (2015) 151 [arXiv:1505.02646] [INSPIRE].  
[30] C. Hartmann and M. Trott, Higgs decay to two photons at one loop in the Standard Model effective field theory, Phys. Rev. Lett. 115 (2015) 191801 [arXiv:1507.03568] [INSPIRE].  
[31] M. Ghezzi, R. Gomez-Ambrosio, G. Passarino and S. Uccirati, NLO Higgs effective field theory and  $\kappa$ -framework, JHEP 07 (2015) 175 [arXiv:1505.03706] [INSPIRE].  
[32] S. Dawson and P.P. Giardino, Higgs decays to ZZ and  $Z\gamma$  in the Standard Model effective field theory: an NLO analysis, Phys. Rev. D 97 (2018) 093003 [arXiv:1801.01136] [INSPIRE].  
[33] R. Gauld, B.D. Pecjak and D.J. Scott, One-loop corrections to  $h \to b\bar{b}$  and  $h \to \tau \bar{\tau}$  decays in the Standard Model dimension-6 EFT: four-fermion operators and the large- $m_t$  limit, JHEP 05 (2016) 080 [arXiv:1512.02508] [INSPIRE].

[34] K. Mimasu, V. Sanz and C. Williams, Higher order QCD predictions for associated Higgs production with anomalous couplings to gauge bosons, JHEP 08 (2016) 039 [arXiv:1512.02572] [INSPIRE].  
[35] C. Degrande, B. Fuks, K. Mawatari, K. Mimasu and V. Sanz, Electroweak Higgs boson production in the Standard Model effective field theory beyond leading order in QCD, Eur. Phys. J. C 77 (2017) 262 [arXiv:1609.04833] [INSPIRE].  
[36] J. Alwall et al., The automated computation of tree-level and next-to-leading order differential cross sections and their matching to parton shower simulations, JHEP 07 (2014) 079 [arXiv:1405.0301] [INSPIRE].  
[37] C. Zhang, Automating predictions for Standard Model effective field theory in MadGraph5 aMC@NLO, PoS(RADCOR2015)101 [arXiv:1601.03994] [INSPIRE].  
[38] C. Degrande, F. Maltoni, J. Wang and C. Zhang, Automatic computations at next-to-leading order in QCD for top-quark flavor-changing neutral processes, Phys. Rev. D 91 (2015) 034024 [arXiv:1412.5594] [INSPIRE].  
[39] D. Buarque Franzosi and C. Zhang, Probing the top-quark chromomagnetic dipole moment at next-to-leading order in QCD, Phys. Rev. D 91 (2015) 114010 [arXiv:1503.08841] [INSPIRE].  
[40] C. Zhang, Single top production at next-to-leading order in the Standard Model effective field theory, Phys. Rev. Lett. 116 (2016) 162002 [arXiv:1601.06163] [INSPIRE].  
[41] C. Degrande, F. Maltoni, K. Mimasu, E. Vryonidou and C. Zhang, Single-top associated production with a  $Z$  or  $H$  boson at the LHC: the SMEFT interpretation, submitted to JHEP (2018) [arXiv:1804.07773] [INSPIRE].  
[42] M. McCullough, An indirect model-dependent probe of the Higgs self-coupling, Phys. Rev. D 90 (2014) 015001 [Erratum ibid. D 92 (2015) 039903] [arXiv:1312.3322] [INSPIRE].  
[43] M. Gorbahn and U. Haisch, Indirect probes of the trilinear Higgs coupling:  $gg \to h$  and  $h \to \gamma \gamma$ , JHEP 10 (2016) 094 [arXiv:1607.03773] [INSPIRE].  
[44] G. Degrassi, P.P. Giardino, F. Maltoni and D. Pagani, Probing the Higgs self coupling via single Higgs production at the LHC, JHEP 12 (2016) 080 [arXiv:1607.04251] [INSPIRE].  
[45] W. Bizon, M. Gorbahn, U. Haisch and G. Zanderighi, Constraints on the trilinear Higgs coupling from vector boson fusion and associated Higgs production at the LHC, JHEP 07 (2017) 083 [arXiv:1610.05771] [INSPIRE].  
[46] S. Di Vita, C. Grojean, G. Panico, M. Riembau and T. Vantalon, A global view on the Higgs self-coupling, JHEP 09 (2017) 069 [arXiv:1704.01953] [INSPIRE].  
[47] CEPC-SPPC STUDY GROUP collaboration, CEPC-SPPC preliminary conceptual design report. 1. Physics and detector, tech. rep. IHEP-CEPC-DR-2015-01, (2015) [IHEP-TH-2015-01] [IHEP-EP-2015-01] [INSPIRE].  
[48] TLEP DESIGN STUDY WORKING GROUP collaboration, M. Bicer et al., First look at the physics case of TLEP, JHEP 01 (2014) 164 [arXiv:1308.6176] [INSPIRE].  
[49] H. Baer et al., The International Linear Collider technical design report — volume 2: physics, arXiv:1306.6352 [INSPIRE].  
[50] CLICDP and CLIC collaborations, M.J. Boland et al., Updated baseline for a staged Compact Linear Collider, arXiv:1608.07537 [INSPIRE].  
[51] B. Grzadkowski, M. Iskrzynski, M. Misiak and J. Rosiek, Dimension-six terms in the Standard Model Lagrangian, JHEP 10 (2010) 085 [arXiv:1008.4884] [INSPIRE].

[52] PARTICLE DATA GROUP collaboration, C. Patrignani et al., Review of particle physics, Chin. Phys. C 40 (2016) 100001 [INSPIRE].  
[53] E.E. Jenkins, A.V. Manohar and M. Trot, Renormalization group evolution of the Standard Model dimension six operators I: formalism and  $\lambda$  dependence, JHEP 10 (2013) 087 [arXiv:1308.2627] [INSPIRE].  
[54] E.E. Jenkins, A.V. Manohar and M. Trot, *Renormalization group evolution of the Standard Model dimension six operators II: Yukawa dependence*, JHEP 01 (2014) 035 [arXiv:1310.4838] [INSPIRE].  
[55] R. Alonso, E.E. Jenkins, A.V. Manohar and M. Trott, Renormalization group evolution of the Standard Model dimension six operators III: gauge coupling dependence and phenomenology, JHEP 04 (2014) 159 [arXiv:1312.2014] [INSPIRE].  
[56] J.D. Wells and Z. Zhang, Effective theories of universal theories, JHEP 01 (2016) 123 [arXiv:1510.08462] [INSPIRE].  
[57] K. Hagiwara, S. Ishihara, R. Szalapski and D. Zeppenfeld, Low-energy effects of new interactions in the electroweak boson sector, Phys. Rev. D 48 (1993) 2182 [INSPIRE].  
[58] C. Grojean, W. Skiba and J. Terning, Disguising the oblique parameters, Phys. Rev. D 73 (2006) 075008 [hep-ph/0602154] [INSPIRE].  
[59] I. Brivio and M. Trot, Scheming in the SMEFT... And a reparameterization invariance!, JHEP 07 (2017) 148 [arXiv:1701.06424] [INSPIRE].  
[60] A. Alloul, N.D. Christensen, C. Degrande, C. Duhr and B. Fuks, *FeynRules* 2.0 — a complete toolbox for tree-level phenomenology, *Comput. Phys. Commun.* **185** (2014) 2250 [arXiv:1310.1921] [INSPIRE].  
[61] O. Mattelaer, On the maximal use of Monte Carlo samples: re-weighting events at NLO accuracy, Eur. Phys. J. C 76 (2016) 674 [arXiv:1607.00763] [INSPIRE].  
[62] A. Dedes, W. Materkowska, M. Paraskevas, J. Rosiek and K. Suxho, Feynman rules for the Standard Model effective field theory in  $R_{\xi}$ -gauges, JHEP 06 (2017) 143 [arXiv:1704.03888] [INSPIRE].  
[63] T. Hahn, Generating Feynman diagrams and amplitudes with FeynArts 3, Comput. Phys. Commun. 140 (2001) 418 [hep-ph/0012260] [INSPIRE].  
[64] R. Mertig, M. Böhm and A. Denner, FEYN CALC: computer algebraic calculation of Feynman amplitudes, Comput. Phys. Commun. 64 (1991) 345 [INSPIRE].  
[65] V. Shtabovenko, R. Mertig and F. Orellana, New developments in FeynCalc 9.0, Comput. Phys. Commun. 207 (2016) 432 [arXiv:1601.01167] [INSPIRE].  
[66] D. Kreimer, The  $\gamma_{5}$  problem and anomalies: a Clifford algebra approach, Phys. Lett. B 237 (1990) 59 [INSPIRE].  
[67] J.G. Korner, D. Kreimer and K. Schilcher, A practicable  $\gamma_5$  scheme in dimensional regularization, Z. Phys. C 54 (1992) 503 [INSPIRE].  
[68] D. Kreimer, The role of  $\gamma_{5}$  in dimensional regularization, hep-ph/9401354 [INSPIRE].  
[69] H.-S. Shao, Y.-J. Zhang and K.-T. Chao, Feynman rules for the rational part of the Standard Model one-loop amplitudes in the 't Hooft-Veltman  $\gamma_{5}$  scheme, JHEP 09 (2011) 048 [arXiv:1106.5030] [INSPIRE].  
[70] T. Hahn and M. Pérez-Victoria, Automatized one loop calculations in four-dimensions and  $D$ -dimensions, Comput. Phys. Commun. 118 (1999) 153 [hep-ph/9807565] [INSPIRE].

[71] A. Denner, Techniques for calculation of electroweak radiative corrections at the one loop level and results for  $W$  physics at LEP-200, Fortsch. Phys. 41 (1993) 307 [arXiv:0709.1075] [INSPIRE].  
[72] M. Ruan, Status & updates from CEPC simulation — detector optimization, in Presentation at the High Energy Physics Conference, http://ias.ust.hk/program/shared_doc/2017/201701hep/HEP_20170124_Manqi_Ruan.pdf, IAS HKUST, Hong Kong, 24 January 2017.  
[73] A. Blondel, Summary FCC-ee experiments, in Presentation at the FCC week, https://indico.cern.ch/event/556692/contributions/2487579/attachments/1469993/2274251/99-Blondel-FCC-ee-summary-Berlin.pdf, Berlin, Germany, 2 June 2017.  
[74] K. Fujii et al., Physics case for the International Linear Collider, arXiv:1506.05992 [INSPIRE].  
[75] T. Barklow et al., ILC operating scenarios, arXiv:1506.07830 [INSPIRE].  
[76] G. Durieux, Precision constraints on the top-quark effective field theory at future lepton colliders, PoS(DIS2017)088 [arXiv:1708.09849] [INSPIRE].  
[77] G. Durieux, M. Perelló, M. Vos and C. Zhang, Global and optimal probes for the top-quark effective field theory at future lepton colliders, arXiv:1807.02121 [INSPIRE].  
[78] Y. Jiang and M. Trott, On the non-minimal character of the SMEFT, Phys. Lett. B 770 (2017) 108 [arXiv:1612.02040] [INSPIRE].  
[79] CMS collaboration, Search for the associated production of a Higgs boson with a top quark pair in final states with a  $\tau$  lepton at  $\sqrt{s} = 13$  TeV, CMS-PAS-HIG-17-003, CERN, Geneva, Switzerland, (2017).  
[80] CMS collaboration, Search for Higgs boson production in association with top quarks in multilepton final states at  $\sqrt{s} = 13$  TeV, CMS-PAS-HIG-17-004, CERN, Geneva, Switzerland, (2017).  
[81] ATLAS collaboration, Evidence for the associated production of the Higgs boson and a top quark pair with the ATLAS detector, Phys. Rev. D 97 (2018) 072003 [arXiv:1712.08891] [INSPIRE].  
[82] ATLAS collaboration, Search for the Standard Model Higgs boson produced in association with top quarks and decaying into a bb pair in pp collisions at  $\sqrt{s} = 13$  TeV with the ATLAS detector, Phys. Rev. D 97 (2018) 072016 [arXiv:1712.08895] [INSPIRE].  
[83] F. Maltoni, D. Pagani, A. Shivaji and X. Zhao, Trilinear Higgs coupling determination via single-Higgs differential measurements at the LHC, Eur. Phys. J. C 77 (2017) 887 [arXiv:1709.08649] [INSPIRE].  
[84] ATLAS collaboration, Prospects for the study of the Higgs boson in the  $VH(bb)$  channel at HL-LHC, ATL-PHYS-PUB-2014-011, CERN, Geneva, Switzerland, (2014).  
[85] ATLAS collaboration, Update of the prospects for the  $H \to Z\gamma$  search at the High-Luminosity LHC, ATL-PHYS-PUB-2014-006, CERN, Geneva, Switzerland, (2014).  
[86] G. Durieux, C. Grojean, J. Gu and K. Wang, The leptonic future of the Higgs, JHEP 09 (2017) 014 [arXiv:1704.02333] [INSPIRE].