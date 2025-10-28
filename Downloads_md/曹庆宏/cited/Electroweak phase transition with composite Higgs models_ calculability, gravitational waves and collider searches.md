# Electroweak phase transition with composite Higgs models: calculability, gravitational waves and collider searches

Ligong Bian, $^{a}$  Yongcheng Wu $^{b}$  and Ke-Pan Xie $^{c}$

$^a$ Department of Physics, Chongqing University, Chongqing 401331, China  
b Ottawa-Carleton Institute for Physics, Carleton University, 1125 Colonel By Drive, Ottawa, Ontario K1S 5B6, Canada  
$^{c}$ Center for Theoretical Physics, Department of Physics and Astronomy, Seoul National University, Seoul 08826, Korea

E-mail: lgbycl@cqu.edu.cn, ycwu@physics.carleton.ca, kpxie@snu.ac.kr

ABSTRACT: We study the strong first order electroweak phase transition (SFOEWPT) with the SO(6)/SO(5) composite Higgs model, whose scalar sector contains one Higgs doublet and one real singlet. Six benchmark models are built with fermion embeddings in 1, 6, and 15 of SO(6). We show that SFOEWPT cannot be triggered under the minimal Higgs potential hypothesis, which assumes the scalar potential is dominated by the form factors from the lightest composite resonances. To get a SFOEWPT, the contributions from local operators induced by physics above the cutoff scale are needed. We take the  $\mathbf{6} + \mathbf{6}$  model as an example to investigate the gravitational waves prediction and the related collider phenomenology.

KEYWORDS: Beyond Standard Model, Technicolor and Composite Models, Thermal Field Theory

ARXIV EPRINT: 1909.02014

# Contents

# 1 Introduction 1

# 2 NMCHM and the SFOEWPT condition 3

2.1 A brief introduction to NMCHM 3  
2.2 The scalar potential and the condition of SFOEWPT 7

# 3 Deriving the scalar potential of NMCHM 10

3.1 The sources of the scalar potential 10  
3.2 Contribution from vector bosons 12  
3.3 Contribution from fermions: the  $\mathbf{6} + \mathbf{6}$  model 13  
3.4 Contribution from fermions: the 15 + 6 model 16  
3.5 Contribution from fermions: the 15 + 15 model 17

# 4 Realizing SFOEWPT in the 6 + 6 NMCHM 18

4.1 Calculating the IR contributions with Weinberg sum rules 18  
4.2 SFOEWPT and gravitational waves 21  
4.3 Collider phenomenology 23

# 5 Conclusion 26

# A The CCWZ formulae for NMCHM 27

# B  $Zb_{L}\bar{b}_{L}$  coupling in the  $q_{L}^{15}$  embedding 30

# C The validity of polynomial approximation 30

# 1 Introduction

The composite Higgs models (CHMs) were originally proposed to solve the Standard Model (SM) hierarchy problem. In CHMs, the Higgs boson is a composite object emerged as a pseudo-Nambu-Goldstone boson (pNGB) from the global symmetry breaking  $\mathcal{G} / \mathcal{H}$  of a new strongly interacting sector. The interactions between the elementary (SM) sector and the composite (strong) sector break  $\mathcal{G}$  explicitly and generate the Higgs potential at loop levels [1-3], triggering the electroweak symmetry breaking (EWSB). The Higgs boson is then naturally light. In addition, the linear mixing between the elementary quarks and the strong fermionic operator (the so-called partial compositeness mechanism) provides an explanation for the quark mass hierarchy [3]. Depends on different choices of  $\mathcal{G} / \mathcal{H}$  and various embeddings of the SM fermions, one can have different kinds of CHMs. For example, the minimal CHM (MCHM) is based on  $\mathrm{SO}(5) / \mathrm{SO}(4)$  [3, 4], which gives exactly one Higgs

doublet; while the next-to-minimal CHM (NMCHM) is based on  $\mathrm{SO}(6) / \mathrm{SO}(5)$  [5], whose scalar sector contains one Higgs doublet and one real singlet.

During the last decade, people were aware that CHMs can also account for the astrophysics phenomena beyond the scope of SM. For example, refs. [10-14] consider the extra pNGBs in the non-minimal CHMs as dark matter candidates, while refs. [15-19] use CHMs to explain the baryon asymmetry of the universe. In the latter case, the extra scalars, either from the dilaton of the conformal invariance breaking [15, 16] or from the pNGBs of the  $\mathcal{G} / \mathcal{H}$  global symmetry breaking [17-19] of the strong sector, assist the Higgs field to trigger a strong first order electroweak phase transition (SFOEWPT), creating the departure from thermal equilibrium in the early universe; while the Yukawa interactions in the quark sector provide necessary CP violating phase to realize the EW baryogenesis mechanism [15-19].

In this article, we focus on the SFOEWPT scenario of NMCHM. SFOEWPT is not only a necessary ingredient of the EW baryogenesis mechanism but also testable via gravitational waves signals at the future detectors such as LISA [20], Tianqin [21], Taiji [22], BBO [23] or DECIGO (Ultimate DECIGO) [24, 25]. The scalar sector of NMCHM is similar to the real singlet extensions of SM (with a  $\mathbb{Z}_2$  symmetry in the scalar potential), which are motivated by EW baryogenesis and dark matter [27-37]. However, NMCHM differs from those models in several important aspects. First, due to the pNGB nature, the interactions between the singlet and the Higgs boson include derivative vertexes. Second, the scalar potential is not added by hand but generated by the SO(6)-breaking terms. Third, as a strongly interacting theory, NMCHM contains additional vector and fermion resonances, whose masses are expected to be  $\mathcal{O}(\mathrm{TeV})$ . Compare to previous studies about the SFOEWPT in non-minimal CHMs [17, 18], the novelty of our work is that we consider various fermion embeddings, perform the concrete calculation of the form factor contributions to the scalar potential and point out that they are not sufficient for a SFOEWPT (see below).

This paper is organized as follows. In section 2, we briefly introduce the NMCHM, list the form of its scalar potential at both zero and finite temperature, and give the conditions for SFOEWPT. A complete analysis of the scalar potential is given in section 3, where we specify two sources of the scalar potential: the IR contributions, which are from the one-loop form factors of the lightest composite resonances and calculable; the UV contributions, which are from local higher dimensional operators and incalculable. In

<sup>1</sup>In the concept of global symmetry breaking pattern, NMCHM is the minimal extension of MCHM. However, concerning about the underlying theory of the strong sector, NMCHM is the minimal model with a fundamental UV description from the bound states of new fermions. This is because  $\mathrm{SO}(6) / \mathrm{SO}(5) \cong \mathrm{SU}(4) / \mathrm{Sp}(4)$ , a coset that can be realized by a QCD-like theory with four-flavor Weyl fermions [6-9].  
2For a recent review of the cosmic phase transition and gravitational waves, see ref. [26].  
In principle, the scalar potential of a composite Higgs model with UV completion can be evaluated via lattice calculation. However, due to the complexity of the calculation, only very few lattice results are available for specific UV models. While no dedicated lattice calculations for the scalar potential have been done for the models mentioned in our paper, we therefore use the bottom-up approach and the form factor integrals to derive the scalar potential. This is inspired by the successful experiences in QCD (such as the calculation of the pion mass difference [38-41]).

many previous studies, the authors assume the UV contributions are negligible due to some unknown mechanisms of the underlying theory [11, 42-45]. This is known as the minimal Higgs potential hypothesis (MHP), first clearly proposed in ref. [42]. However, in this study we will show that MHP is not sufficient for the SFOEWPT in NMCHM, at least for various fermion embeddings from 1 up to 15 representations of SO(6). To trigger a SFOEWPT, we have to add the UV contributions, whose sizes are estimated by the naive dimensional analysis (NDA) [46]. Section 4 demonstrates that when combining the IR and UV contributions, SFOEWPT in the  $\mathbf{6} + \mathbf{6}$  NMCHM can be triggered and experimentally tested by the gravitational waves. A brief discussion about the collider phenomenology of the model is also provided. Finally, we summarize and conclude in section 5.

# 2 NMCHM and the SFOEWPT condition

# 2.1 A brief introduction to NMCHM

Since we are interested in the physics at  $\mathcal{O}(\mathrm{TeV})$ , which is well below the confinement scale of the strong sector, the relevant physical degrees of freedom are the pNGBs, the vector and fermion resonances. In this case, the Coleman-Callan-Wess-Zumino (CCWZ) formalism [47, 48] can be used to describe the effective Lagrangian of NMCHM. The full expressions and formulae are put in appendix A, while here we only quote the main results.

Denote the 15 generators of SO(6) as  $T^{A} = \{T^{\bar{A}},\hat{T}_{2}^{r}\}$ , where  $T^{\bar{A}} = \{T_L^a,T_R^a,\hat{T}_1^i\}$  are the 10 generators of the unbroken SO(5) [in which  $\{T_L^a,T_R^a\}$  belong to the subgroup  $\mathrm{SO}(4)\cong \mathrm{SU}(2)_L\times \mathrm{SU}(2)_R$  while  $\hat{T}_1^i$  belong to the coset  $\mathrm{SO}(5) / \mathrm{SO}(4)]$ , and  $\hat{T}_2^r$  are the 5 broken generators of SO(6)/SO(5). The ranges of the subscripts are  $(a = 1,2,3)$ ,  $(i = 1,\dots ,4)$  and  $(r = 1,\ldots ,5)$ . The Goldstone matrix is defined as

$$
U (\vec {\pi}) = e ^ {i \frac {\sqrt {2}}{f} \pi_ {r} \hat {T} _ {2} ^ {r}}, \tag {2.1}
$$

where  $f$  is the decay constant, and  $\vec{\pi} = (\pi_1,\dots ,\pi_5)^T$  are the 5 pNGBs, which transform as the 5 representation of the unbroken SO(5). Under the group decomposition of  $\mathrm{SO}(5)\to \mathrm{SO}(4)\cong \mathrm{SU}(2)_L\times \mathrm{SU}(2)_R$ $\mathbf{5}\rightarrow \mathbf{4}\oplus \mathbf{1}\cong (\mathbf{2},\mathbf{2})\oplus (\mathbf{1},\mathbf{1})$ , where

$$
H = \frac {1}{\sqrt {2}} \left( \begin{array}{c} \pi_ {2} + i \pi_ {1} \\ \pi_ {4} - i \pi_ {3} \end{array} \right), \tag {2.2}
$$

is the Higgs doublet  $(\mathbf{2},\mathbf{2})$  and  $\pi_5$  is the real singlet  $(\mathbf{1},\mathbf{1})$ . Choosing the SO(5)-preserved vacuum state vector as  $\Sigma_0 = (0,0,0,0,0,1)^T$ , we define the Goldstone vector as  $\Sigma (\vec{\pi}) = U(\vec{\pi})\Sigma_0$ . The  $d$  and  $e$  symbols are given by the Maurer-Cartan form

$$
U ^ {\dagger} i D _ {\mu} U = d _ {\mu} ^ {r} \hat {T} _ {2} ^ {r} + e _ {\mu} ^ {\bar {A}} T ^ {\bar {A}} \equiv d _ {\mu} + e _ {\mu}, \tag {2.3}
$$

where

$$
D _ {\mu} = \partial_ {\mu} - i g _ {0} A _ {\mu} = \partial_ {\mu} - i g _ {0} W _ {\mu} ^ {a} T _ {L} ^ {a} - i g _ {0} ^ {\prime} B _ {\mu} T _ {R} ^ {3}, \tag {2.4}
$$

is the gauge covariant derivative. We only gauge a subgroup  $\mathrm{SU}(2)_L\times \mathrm{U}(1)_Y\subset \mathrm{SO}(6)$  with  $Y = T_R^3$

It is convenient to work under the unitary gauge, where  $\pi_{1,2,3} = 0$  and  $\pi_{4,5}$  are redefined as [5]

$$
\frac {h}{f} = \frac {\pi_ {4}}{\sqrt {\pi_ {4} ^ {2} + \pi_ {5} ^ {2}}} \sin \frac {\sqrt {\pi_ {4} ^ {2} + \pi_ {5} ^ {2}}}{f}, \quad \frac {\eta}{f} = \frac {\pi_ {5}}{\sqrt {\pi_ {4} ^ {2} + \pi_ {5} ^ {2}}} \sin \frac {\sqrt {\pi_ {4} ^ {2} + \pi_ {5} ^ {2}}}{f}. (2. 5)
$$

Under the unitary gauge, the kinetic term of the Goldstone fields is

$$
\begin{array}{l} \mathcal {L} _ {\mathrm {k i n}} = \frac {f ^ {2}}{4} \mathrm {t r} [ d _ {\mu} d ^ {\mu} ] = \frac {1}{2} \partial_ {\mu} h \partial^ {\mu} h + \frac {1}{2} \partial_ {\mu} \eta \partial^ {\mu} \eta \\ + \frac {1}{2} \frac {\left(h \partial_ {\mu} h + \eta \partial_ {\mu} \eta\right) ^ {2}}{f ^ {2} - h ^ {2} - \eta^ {2}} + \frac {g _ {0} ^ {2}}{8} h ^ {2} \left[ \left(W _ {\mu} ^ {1}\right) ^ {2} + \left(W _ {\mu} ^ {2}\right) ^ {2} + \left(W _ {\mu} ^ {3} - \frac {g _ {0} ^ {\prime}}{g _ {0}} B _ {\mu}\right) ^ {2} \right], \tag {2.6} \\ \end{array}
$$

in which we can read the  $W$  and  $Z$  mass terms after EWSB, i.e.  $\langle h\rangle = v$ . Higher order operators can also be constructed using the  $d$  and  $e$  symbols.

There are two kinds of composite resonances in the NMCHM. One is spin-1, similar to the  $\rho$ -mesons in the QCD; the other is spin-1/2, also known as the top partner. The composite objects transform in the representations of the unbroken SO(5). For the vector resonances, we consider the 10 and 5 representations, and denote them as  $\rho_{\mu} = \rho_{\mu}^{\bar{A}}T^{\bar{A}}$  and  $a_{\mu} = a_{\mu}^{r}\hat{T}_{2}^{r}$ . Under the decomposition  $\mathrm{SO}(5)\to \mathrm{SU}(2)_L\times \mathrm{U}(1)_Y$ , the  $\rho_{\mu}$  decomposes to 1 triplet, 3 singlet and 1 complex doublet; while the  $a_{\mu}$  decomposes to 1 complex doublet and 1 singlet, i.e.

$$
\left[\begin{array}{c}\mathbf {1 0} \rightarrow \mathbf {3} _ {0} \oplus \mathbf {1} _ {1} \oplus \mathbf {1} _ {0} \oplus \mathbf {1} _ {- 1} \oplus \mathbf {2} _ {1 / 2} \oplus \mathbf {2} _ {- 1 / 2}\\\rho^ {\bar {A}} \rightarrow \rho_ {L} \oplus \rho_ {R} ^ {+} \oplus \rho_ {R} ^ {0} \oplus \rho_ {R} ^ {- 1} \oplus \rho_ {D} \oplus \tilde {\rho} _ {D}\end{array}\right]; \quad \left[\begin{array}{c}\mathbf {5} \rightarrow \mathbf {2} _ {1 / 2} \oplus \mathbf {2} _ {- 1 / 2} \oplus \mathbf {1} _ {0}\\a ^ {r} \rightarrow a _ {D} \oplus \tilde {a} _ {D} \oplus a _ {S}\end{array}\right], \tag {2.7}
$$

where  $\tilde{\rho}_D = i\sigma^2\rho_D^*$  and  $\tilde{a}_D = i\sigma^2 a_D^*$ . The full expressions of the resonances can be found in appendix A. The Lagrangian of vector resonances reads<sup>5</sup>

$$
\mathcal {L} _ {\rho} = - \frac {1}{4} \operatorname {t r} \left[ \rho_ {\mu \nu} \rho^ {\mu \nu} \right] + \frac {M _ {\rho} ^ {2}}{2 g _ {\rho} ^ {2}} \operatorname {t r} \left[ \left(g _ {\rho} \rho_ {\mu} - e _ {\mu}\right) ^ {2} \right] - \frac {1}{4} \operatorname {t r} \left[ a _ {\mu \nu} a ^ {\mu \nu} \right] + \frac {M _ {a} ^ {2}}{2} \operatorname {t r} \left[ a _ {\mu} a ^ {\mu} \right], \tag {2.8}
$$

where  $g_{\rho} \gg g_{0}$ ,  $g_{0}'$  is the coupling constant of the strong sector. The field strengths are

$$
\rho_ {\mu \nu} = \partial_ {\mu} \rho_ {\nu} - \partial_ {\nu} \rho_ {\mu} - i g _ {\rho} [ \rho_ {\mu}, \rho_ {\nu} ], \quad a _ {\mu \nu} = \nabla_ {\mu} a _ {\nu} - \nabla_ {\nu} a _ {\mu}, \tag {2.9}
$$

where the  $\mathrm{SO}(6) / \mathrm{SO}(5)$  covariant derivative is  $\nabla_{\mu} = \partial_{\mu} - ie_{\mu}$ .

For the fermion resonances, we consider the 1, 5 and 10 representations of SO(5). To give the correct hypercharge, an extra  $\mathrm{U}(1)_X$  is introduced, and the gauging of hypercharge

is extended to  $Y = T_R^3 + X$ . As we will see, for the fermion resonances relevant to the top-quark interactions,  $X = 2/3$ . Under the decomposition  $\mathrm{SO}(5) \times \mathrm{U}(1)_X \to \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ , we get

$$
\left[\begin{array}{c}\mathbf {5} _ {2 / 3} \rightarrow \mathbf {2} _ {7 / 6} \oplus \mathbf {2} _ {1 / 6} \oplus \mathbf {1} _ {2 / 3}\\\Psi_ {\mathbf {5}} \rightarrow Q _ {X} \oplus Q \oplus \widetilde {T}\end{array}\right]; \quad \left[\begin{array}{c}\mathbf {1 0} _ {2 / 3} \rightarrow \mathbf {3} _ {2 / 3} \oplus \mathbf {1} _ {5 / 3} \oplus \mathbf {1} _ {2 / 3} \oplus \mathbf {1} _ {- 1 / 3} \oplus \mathbf {2} _ {7 / 6} \oplus \mathbf {2} _ {1 / 6}\\\Psi_ {\mathbf {1 0}} \rightarrow Y \oplus K _ {5 / 3} \oplus K _ {2 / 3} \oplus K _ {- 1 / 3} \oplus J _ {X} \oplus J _ {Q}\end{array}\right], \tag {2.10}
$$

where the full expressions of the above fields are given in appendix A. The Lagrangian of top partners reads

$$
\begin{array}{l} \mathcal {L} _ {\Psi} = \mathrm {t r} \left[ \bar {\Psi} _ {\bf 1 0} \left(i \vec {\nabla} + g _ {0} ^ {\prime} \frac {2}{3} \not B - M _ {\bf 1 0}\right) \Psi_ {\bf 1 0} \right] \\ + \bar {\Psi} _ {5} \left(i \dot {\nabla} + g _ {0} ^ {\prime} \frac {2}{3} \not B - M _ {5}\right) \Psi_ {5} + \bar {\Psi} _ {1} \left(i \not \partial / + g _ {0} ^ {\prime} \frac {2}{3} \not B - M _ {1}\right) \Psi_ {1}, \tag {2.11} \\ \end{array}
$$

where the  $\mathrm{SO}(6) / \mathrm{SO}(5)$  covariant derivatives

$$
\nabla_ {\mu} \Psi_ {5} = \left(\partial_ {\mu} - i e _ {\mu} ^ {\bar {A}} t ^ {\bar {A}}\right) \Psi_ {5}, \quad \nabla_ {\mu} \Psi_ {1 0} = \partial_ {\mu} \Psi_ {1 0} - i e _ {\mu} ^ {\bar {A}} t ^ {\bar {A}} \Psi_ {1 0} + i \Psi_ {1 0} e _ {\mu} ^ {\bar {A}} t ^ {\bar {A}}, \tag {2.12}
$$

and the matrices  $[t_{L,R}^a ]_{rs}\equiv [T_{L,R}^a ]_{rs},[\hat{t}_1^i ]_{rs}\equiv [\hat{T}_1^i ]_{rs}$  with  $(r,s = 1,\ldots ,5)$ .

The SM fermions gain their masses through EWSB and the mixing with the strong sector, i.e. the partial compositeness interactions. The heavier a fermion is, the more strongly it couples to the top partners. Therefore, only the interactions with top quark are sizable due to the large top mass, and hereafter we only consider  $q_{L} = (t_{L},b_{L})^{T}$  and  $t_R$ . In CCWZ, the elementary fermions are embedded into the incomplete representation of SO(6), and one has the degree of freedom to choose various embeddings when building the model. For  $q_{L}$ , we consider the 6 and 15 representations; while for  $t_R$ , we consider the 1, 6 and 15 representations. The explicit expressions of the embeddings are as follows. First,  $t_R$  can be the  $\mathbf{1}_{2/3}$  of SO(6) × U(1)_X:  $t_R^{\mathbf{1}} \equiv t_R$ . Second, under group decomposition SO(6) × U(1)_X → SU(2)_L × U(1)_Y we get

$$
\mathbf {6} _ {2 / 3} \rightarrow \mathbf {2} _ {7 / 6} \oplus \mathbf {2} _ {1 / 6} \oplus \mathbf {1} _ {2 / 3} \oplus \mathbf {1} _ {2 / 3}, \tag {2.13}
$$

thus the embedding of  $q_{L}$  is unique while of  $t_{R}$  can be the superposition of the two  $\mathbf{1}_{2/3}$ :

$$
q _ {L} ^ {\mathbf {6}} = \frac {1}{\sqrt {2}} \left(i b _ {L} b _ {L} i t _ {L} - t _ {L} 0 0\right) ^ {T}, \quad t _ {R} ^ {\mathbf {6}} = \left(0 0 0 0 t _ {R} e ^ {i \phi} c _ {\theta} t _ {R} s _ {\theta}\right) ^ {T}, \tag {2.14}
$$

where  $c_{\theta}$  and  $s_{\theta}$  stand respectively for  $\cos \theta$  and  $\sin \theta$ , with  $\theta$  and  $\phi$  being the mixing angles [44]. The phase  $\phi$  is unphysical [44, 50].

Finally, we consider the 15 representation. Under the decomposition chain  $\mathrm{SO}(6) \times \mathrm{U}(1)_X \to \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$  we have

$$
\mathbf {1 5} _ {2 / 3} \rightarrow \mathbf {3} _ {2 / 3} \oplus \mathbf {1} _ {5 / 3} \oplus \mathbf {1} _ {2 / 3} \oplus \mathbf {1} _ {- 1 / 3} \oplus \mathbf {2} _ {7 / 6} \oplus \mathbf {2} _ {1 / 6} \oplus \mathbf {2} _ {7 / 6} \oplus \mathbf {2} _ {1 / 6} \oplus \mathbf {1} _ {2 / 3}. \tag {2.15}
$$

Since two  $\mathbf{2}_{1/6}$  are obtained, we have two different ways to embed  $q_L$  in to 15, namely

$$
q _ {L} ^ {\mathbf {1 5} _ {A}} = \left(q _ {L} ^ {\mathbf {6}}\right) _ {j} \hat {T} _ {1} ^ {j}, \quad q _ {L} ^ {\mathbf {1 5} _ {B}} = i \left(q _ {L} ^ {\mathbf {6}}\right) _ {j} \hat {T} _ {2} ^ {j}, \tag {2.16}
$$

where  $(j = 1,\ldots ,4)$ . The  $\mathbf{15}_B$  embedding has been considered in ref. [51], while the  $\mathbf{15}_A$  is first proposed here. Phenomenologically, the model with  $\mathbf{15}_B$  embedding is stringently constrained by the  $Zb_{L}\bar{b}_{L}$  coupling measurement, see appendix B for the details. Hereafter we only consider  $q_{L}^{15_{A}}$  and denote it as  $q_{L}^{15}$ . On the other hand, the right-handed top can be embedded into the superposition of the two  $\mathbf{1}_{2 / 3}$  in eq. (2.15), i.e.

$$
t _ {R} ^ {\mathbf {1 5}} = T _ {R} ^ {3} t _ {R} c _ {\theta} + \hat {T} _ {2} ^ {5} t _ {R} e ^ {i \phi} s _ {\theta}. \tag {2.17}
$$

The special case  $\theta = 0$  is considered in ref. [51] for a collider phenomenology study.

Having the SM embeddings in hand, we are able to write down the partial compositeness interactions. Since  $q_{L}$  has two different embeddings while  $t_{R}$  has three, the combinations yield six different models, which can be labeled by (left-handed embedding) + (right-handed embedding). For example, the  $15 + 6$  NMCHM means the benchmark model with  $q_{L}$  embedded in 15 while  $t_{R}$  embedded in 6. We will discuss those models one by one.

The  $6 + 1$  model.

$$
\mathcal {L} _ {\mathbf {6} + \mathbf {1}} \supset y _ {L} ^ {\mathbf {5}} f \left(\bar {q} _ {L} ^ {\mathbf {6}}\right) _ {I} U _ {I r} \Psi_ {\mathbf {5}} ^ {r} + y _ {L} ^ {\mathbf {1}} f \left(\bar {q} _ {L} ^ {\mathbf {6}}\right) _ {I} U _ {I 6} \Psi_ {\mathbf {1}} + y _ {R} ^ {\mathbf {1}} f \bar {t} _ {R} ^ {\mathbf {1}} \Psi_ {\mathbf {1}} + \text {h . c .}, \tag {2.18}
$$

where  $(I = 1,\ldots ,6)$ . After EWSB, the Yukawa interactions give mass to the top quark.

The  $6 + 6$  model.

$$
\mathcal {L} _ {\mathbf {6} + \mathbf {6}} \supset y _ {L} ^ {\mathbf {5}} f (\bar {q} _ {L} ^ {\mathbf {6}}) _ {I} U _ {I r} \Psi_ {\mathbf {5}} ^ {r} + y _ {L} ^ {\mathbf {1}} f (\bar {q} _ {L} ^ {\mathbf {6}}) _ {I} U _ {I 6} \Psi_ {\mathbf {1}} + y _ {R} ^ {\mathbf {5}} f (\bar {t} _ {R} ^ {\mathbf {6}}) _ {I} U _ {I r} \Psi_ {\mathbf {5}} ^ {r} + y _ {R} ^ {\mathbf {1}} f (\bar {t} _ {R} ^ {\mathbf {6}}) _ {I} U _ {I 6} \Psi_ {\mathbf {1}} + \text {h . c .}. \tag {2.19}
$$

The  $6 + 15$  model.

$$
\begin{array}{l} \mathcal {L} _ {\mathbf {6} + \mathbf {1 5}} \supset y _ {L} ^ {\mathbf {5}} f (\bar {q} _ {L} ^ {\mathbf {6}}) _ {I} U _ {I r} \Psi_ {\mathbf {5}} ^ {r} + y _ {L} ^ {\mathbf {1}} f (\bar {q} _ {L} ^ {\mathbf {6}}) _ {I} U _ {I 6} \Psi_ {\mathbf {1}} \\ + y _ {R} ^ {\mathbf {1 0}} f \left(\bar {t} _ {R} ^ {\mathbf {1 5}}\right) _ {I J} U _ {J r} \Psi_ {\mathbf {1 0}} ^ {r s} \left[ U ^ {\dagger} \right] _ {s I} + y _ {R} ^ {\mathbf {5}} f \Sigma_ {I} ^ {\dagger} \left(\bar {t} _ {R} ^ {\mathbf {1 5}}\right) _ {I J} U _ {J r} \Psi_ {\mathbf {5}} ^ {r} + \mathrm {h . c .}. \tag {2.20} \\ \end{array}
$$

The  $15 + 1$  model.

$$
\mathcal {L} _ {\mathbf {1 5} + \mathbf {1}} \supset y _ {L} ^ {\mathbf {1 0}} f (\bar {q} _ {L} ^ {\mathbf {1 5}}) _ {I J} U _ {J r} \Psi_ {\mathbf {1 0}} ^ {r s} [ U ^ {\dagger} ] _ {s I} + y _ {L} ^ {\mathbf {5}} f \Sigma_ {I} ^ {\dagger} (\bar {q} _ {L} ^ {\mathbf {1 5}}) _ {I J} U _ {J r} \Psi_ {\mathbf {5}} ^ {r} + y _ {R} ^ {\mathbf {1}} f \bar {t} _ {R} ^ {\mathbf {1}} \Psi_ {\mathbf {1}} + \text {h . c .}, \tag {2.21}
$$

where  $(I,J = 1,\ldots ,6)$ . Note that the Yukawa interactions in above equation cannot give a mass to the top quark, because  $q_{L}$  mixes with  $\Psi_{\mathbf{10}}$  and  $\Psi_{\mathbf{5}}$ , while  $t_R$  mixes with  $\Psi_{\mathbf{1}}$ . Therefore, this model is not supported by reality.

The  $15 + 6$  model.

$$
\begin{array}{l} \mathcal {L} _ {\mathbf {1 5} + \mathbf {6}} \supset y _ {L} ^ {\mathbf {1 0}} f (\bar {q} _ {L} ^ {\mathbf {1 5}}) _ {I J} U _ {J r} \Psi_ {\mathbf {1 0}} ^ {r s} [ U ^ {\dagger} ] _ {s I} + y _ {L} ^ {\mathbf {5}} f \Sigma_ {I} ^ {\dagger} (\bar {q} _ {L} ^ {\mathbf {1 5}}) _ {I J} U _ {J r} \Psi_ {\mathbf {5}} ^ {r} \\ + y _ {R} ^ {\mathbf {5}} f \left(\bar {t} _ {R} ^ {\mathbf {6}}\right) _ {I} U _ {I r} \Psi_ {\mathbf {5}} ^ {r} + y _ {R} ^ {\mathbf {1}} f \left(\bar {t} _ {R} ^ {\mathbf {6}}\right) _ {I} U _ {I 6} \Psi_ {\mathbf {1}} + \text {h . c .}. \tag {2.22} \\ \end{array}
$$

The  $15 + 15$  model.

$$
\begin{array}{l} \mathcal {L} _ {\mathbf {1 5} + \mathbf {1 5}} \supset y _ {L} ^ {\mathbf {1 0}} f (\bar {q} _ {L} ^ {\mathbf {1 5}}) _ {I J} U _ {J r} \Psi_ {\mathbf {1 0}} ^ {r s} [ U ^ {\dagger} ] _ {s I} + y _ {L} ^ {\mathbf {5}} f \Sigma_ {I} ^ {\dagger} (\bar {q} _ {L} ^ {\mathbf {1 5}}) _ {I J} U _ {J r} \Psi_ {\mathbf {5}} ^ {r} \\ + y _ {R} ^ {\mathbf {1 0}} f \left(\bar {t} _ {R} ^ {\mathbf {1 5}}\right) _ {I J} U _ {J r} \Psi_ {\mathbf {1 0}} ^ {r s} \left[ U ^ {\dagger} \right] _ {s I} + y _ {R} ^ {\mathbf {5}} f \Sigma_ {I} ^ {\dagger} \left(\bar {t} _ {R} ^ {\mathbf {1 5}}\right) _ {I J} U _ {J r} \Psi_ {\mathbf {5}} ^ {r} + \text {h . c .}. \tag {2.23} \\ \end{array}
$$

In summary, we get five different NMCHMs to study (the  $15 + 1$  model is dropped because of the issue of massless top quark).

# 2.2 The scalar potential and the condition of SFOEWPT

In the strong sector,  $h$  and  $\eta$  are protected by the Goldstone theorem and strictly massless. It is the SO(6)-breaking interactions between the elementary sector and the strong sector that generate the effective potential  $V(h,\eta)$ . As we will see in section 3, the potential can be written in a very good approximation as

$$
V (h, \eta) = \frac {\mu_ {h} ^ {2}}{2} h ^ {2} + \frac {\lambda_ {h}}{4} h ^ {4} + \frac {\mu_ {\eta} ^ {2}}{2} \eta^ {2} + \frac {\lambda_ {\eta}}{4} \eta^ {4} + \frac {\lambda_ {h \eta}}{2} h ^ {2} \eta^ {2}. \tag {2.24}
$$

Above potential implies a  $\mathbb{Z}_2$  symmetry  $\eta \rightarrow -\eta$ , which might be broken either spontaneously by the global vacuum expectation value (VEV) of  $\eta$  or explicitly by the Yukawa interactions such as  $t\bar{t}\eta$  (depends on the choice of  $\theta$  in the  $t_R$  embedding). A physically acceptable potential  $V(h,\eta)$  should have a VEV  $\langle h\rangle = v$  at zero temperature and give correct masses to the observed particles such as the Higgs boson, the  $W^{\pm}$  and  $Z$  bosons, the top quark, etc.

At finite temperature,  $V(h,\eta)$  receives the thermal corrections and the vacuum structure changes. For the tree-level driven first-order EWPT, the high-temperature expansion approximation of the finite temperature potential could be adopted to characterize the dynamics of the phase transition [52]. Keeping only the leading  $T^2$  terms, the finite temperature potential is then written as:

$$
V _ {T} (h, \eta) = \frac {\mu_ {h} ^ {2} + c _ {h} T ^ {2}}{2} h ^ {2} + \frac {\lambda_ {h}}{4} h ^ {4} + \frac {\mu_ {\eta} ^ {2} + c _ {\eta} T ^ {2}}{2} \eta^ {2} + \frac {\lambda_ {\eta}}{4} \eta^ {4} + \frac {\lambda_ {h \eta}}{2} h ^ {2} \eta^ {2}, \tag {2.25}
$$

where

$$
c _ {h} = \frac {3 g ^ {2} + g ^ {\prime 2}}{1 6} + \frac {y _ {t} ^ {2}}{4} + \frac {\lambda_ {h}}{2} + \frac {\lambda_ {h \eta}}{1 2}, \quad c _ {\eta} = \frac {\lambda_ {\eta}}{4} + \frac {\lambda_ {h \eta}}{3}, \tag {2.26}
$$

with  $g^{(t)}$  and  $y_{t}$  being the physical EW couplings and top Yukawa, respectively. The necessary condition for SFOEWPT is the existence of two degenerate vacuums at some critical temperature  $T_{c}$ . In the thermal potential  $V_{T}(h,\eta)$ , the proper way to realize that is the so-called "two-step" phase transition, in which the VEV  $(\langle h\rangle ,\langle \eta \rangle)$  changed as  $(0,0)\to (0,w)\to (v,0)$  when the universe cooled down from the temperature  $T\gg M_h$  to  $T = 0$ . This also tells us the  $\mathbb{Z}_2$  symmetry of  $\eta$  is preserved by the scalar potential at zero temperature (but it might be broken by the Yukawa interactions, see the discussions in section 3).

Now we address the conditions for the two-step phase transition. The method used here is similar to those in refs. [34, 35]. At zero temperature there should be a EW breaking

local minimum  $(v,0)$  along the  $h$  direction, which requires

$$
\mu_ {h} ^ {2} <   0, \quad \lambda_ {h} > 0, \quad \lambda_ {h} \mu_ {\eta} ^ {2} > \lambda_ {h \eta} \mu_ {h} ^ {2}, \quad \Rightarrow v = \sqrt {- \mu_ {h} ^ {2} / \lambda_ {h}}; \qquad (2. 2 7)
$$

and another local minimum  $(0, w)$  along the  $\eta$  direction, which needs

$$
\mu_ {\eta} ^ {2} <   0, \quad \lambda_ {\eta} > 0, \quad \lambda_ {\eta} \mu_ {h} ^ {2} > \lambda_ {h \eta} \mu_ {\eta} ^ {2}, \quad \Rightarrow w = \sqrt {- \mu_ {\eta} ^ {2} / \lambda_ {\eta}}. \tag {2.28}
$$

Note the third inequalities in eqs. (2.27) and (2.28) come from the Hessian matrix and ensure  $(v,0)$ ,  $(0,w)$  to be local minima but not saddle points. One can infer  $\lambda_{h\eta} > 0$  and  $\lambda_{h\eta}^2 > \lambda_h \lambda_\eta$  from those inequalities too. In addition, the EWSB minimum should be the true vacuum, i.e.

$$
V (v, 0) = - \frac {\mu_ {h} ^ {4}}{4 \lambda_ {h}} <   V (0, w) = - \frac {\mu_ {\eta} ^ {4}}{4 \lambda_ {\eta}}, \tag {2.29}
$$

thus  $\mu_{\eta}^{2}\sqrt{\lambda_{h}} >\mu_{h}^{2}\sqrt{\lambda_{\eta}}.$

At the critical temperature  $T_{c}$ , there should exist two degenerate vacuums  $(v_{c},0)$  and  $(0,w_{c})$  satisfying

$$
\mu_ {h} ^ {2} + c _ {h} T _ {c} ^ {2} <   0, \quad \lambda_ {h} \left(\mu_ {\eta} ^ {2} + c _ {\eta} T _ {c} ^ {2}\right) > \lambda_ {h \eta} \left(\mu_ {h} ^ {2} + c _ {h} T _ {c} ^ {2}\right), \quad v _ {c} = \sqrt {- \left(\mu_ {h} ^ {2} + c _ {h} T _ {c} ^ {2}\right) / \lambda_ {h}}; \tag {2.30}
$$

$$
\mu_ {\eta} ^ {2} + c _ {\eta} T _ {c} ^ {2} <   0, \lambda_ {\eta} (\mu_ {h} ^ {2} + c _ {h} T _ {c} ^ {2}) > \lambda_ {h \eta} (\mu_ {\eta} ^ {2} + c _ {\eta} T _ {c} ^ {2}), w _ {c} = \sqrt {- (\mu_ {\eta} ^ {2} + c _ {\eta} T _ {c} ^ {2}) / \lambda_ {\eta}},
$$

and

$$
V (v _ {c}, 0) = - \frac {(\mu_ {h} ^ {2} + c _ {h} T _ {c} ^ {2}) ^ {2}}{4 \lambda_ {h}} = V (0, w _ {c}) = - \frac {(\mu_ {\eta} ^ {2} + c _ {\eta} T _ {c} ^ {2}) ^ {2}}{4 \lambda_ {\eta}}. \tag {2.31}
$$

Solving the above equation yields

$$
T _ {c} ^ {2} = \frac {\mu_ {h} ^ {2} \sqrt {\lambda_ {\eta}} - \mu_ {\eta} ^ {2} \sqrt {\lambda_ {h}}}{c _ {\eta} \sqrt {\lambda_ {h}} - c _ {h} \sqrt {\lambda_ {\eta}}}. (2. 3 2)
$$

Requiring  $T_{c} \in \mathbb{R}$  yields  $c_{h}\sqrt{\lambda_{\eta}} > c_{\eta}\sqrt{\lambda_{h}}$ . Substituting the expression of  $T_{c}$  into eq. (2.30), one obtain  $c_{\eta}\mu_h^2 > c_h\mu_\eta^2$ . Combining all the inequalities we get, the condition of two degenerate vacuums for  $V_{T}(h,\eta)$  is

$$
\frac {c _ {\eta}}{c _ {h}} <   \frac {\mu_ {\eta} ^ {2}}{\mu_ {h} ^ {2}} <   \frac {\sqrt {\lambda_ {\eta}}}{\sqrt {\lambda_ {h}}} <   \frac {\lambda_ {h \eta}}{\lambda_ {h}}. \tag {2.33}
$$

Note that eq. (2.33) is necessary but not sufficient for a first order EWPT. To really achieve a first order EWPT, one should calculate the bubble nucleation rate per volume in the early universe

$$
\Gamma / V \approx T ^ {4} \left(\frac {S _ {3}}{2 \pi T}\right) ^ {3 / 2} e ^ {- S _ {3} (T) / T}, \tag {2.34}
$$

and confirm that the critical condition

$$
\frac {S _ {3} \left(T _ {n}\right)}{T _ {n}} \sim 4 \ln \frac {\xi M _ {\mathrm {P l}}}{T _ {n}} \sim 1 4 0, \tag {2.35}
$$

is satisfied at some nucleation temperature  $T_{n}$ . Here  $S_{3}$  is the classical action of the  $O(3)$  symmetric bounce solution [62],  $\xi \approx 0.03$  and  $M_{\mathrm{Pl}} = 1.22 \times 10^{19} \mathrm{GeV}$ . Normally  $T_{n}$  is slightly lower than  $T_{c}$ . Only when eq. (2.35) is satisfied can the bubbles percolate in an expanding universe and phase transition successfully complete. In addition, to avoid the generated baryon asymmetry being washed out, the EW sphaleron process should be suppressed. That means the phase transition should be sufficiently strong [63-65], satisfying

$$
v _ {n} / T _ {n} \gtrsim 1, \tag {2.36}
$$

where  $v_{n}$  is the Higgs VEV at  $T_{n}$ . We will deal with eqs. (2.35) and (2.36) numerically in section 4.

In the end of this subsection, we discuss the allowed parameter space under eq. (2.33). At zero temperature, due to the derivative interactions in the kinetic term, the field shift that canonicalizes the Higgs kinetic term should be

$$
h \rightarrow v + \sqrt {1 - \frac {v ^ {2}}{f ^ {2}}} h, \tag {2.37}
$$

which changes the zero temperature potential eq. (2.24) to

$$
\begin{array}{l} V (h, \eta) \rightarrow - \mu_ {h} ^ {2} \left(1 - \frac {v ^ {2}}{f ^ {2}}\right) h ^ {2} + \lambda_ {h} v \left(1 - \frac {v ^ {2}}{f ^ {2}}\right) ^ {3 / 2} h ^ {3} + \frac {\lambda_ {h}}{4} \left(1 - \frac {v ^ {2}}{f ^ {2}}\right) ^ {2} h ^ {4} \tag {2.38} \\ + \frac {1}{2} \left(\mu_ {\eta} ^ {2} + \lambda_ {h \eta} v ^ {2}\right) \eta^ {2} + \frac {\lambda_ {\eta}}{4} \eta^ {4} + \lambda_ {h \eta} v \sqrt {1 - \frac {v ^ {2}}{f ^ {2}}} h \eta^ {2} + \frac {\lambda_ {h \eta}}{2} \left(1 - \frac {v ^ {2}}{f ^ {2}}\right) h ^ {2} \eta^ {2}, \\ \end{array}
$$

and the physical masses can be easily read as

$$
M _ {h} ^ {2} = - 2 \mu_ {h} ^ {2} \left(1 - \frac {v ^ {2}}{f ^ {2}}\right), \quad M _ {\eta} ^ {2} = \mu_ {\eta} ^ {2} + \lambda_ {h \eta} v ^ {2}. \tag {2.39}
$$

Since  $v^2 \ll f^2$  is expected,  $\mu_h^2$  is almost fixed by the observed  $M_h = 125.09\mathrm{GeV}$ . And  $\lambda_h$  is also fixed by  $-\mu_h^2 /v^2$ . The mass and the Higgs coupling of the EW bosons are respectively

$$
M _ {W} ^ {2} = \frac {g ^ {2} v ^ {2}}{4}, \quad g _ {h W W} = \frac {g ^ {2} v}{2} \sqrt {1 - \frac {v ^ {2}}{f ^ {2}}} = g _ {h W W} ^ {\mathrm {S M}} \sqrt {1 - \frac {v ^ {2}}{f ^ {2}}}, \tag {2.40}
$$

see the Goldstone kinetic term in eq. (2.6). Current EW and Higgs measurements have constrained  $f \gtrsim 1$  TeV.

When  $M_{\eta} < M_h / 2$ , the decay channel  $h \to \eta \eta$  opens and the partial width is [10]

$$
\Gamma (h \rightarrow \eta \eta) = \frac {v ^ {2}}{3 2 \pi M _ {h}} \left(\frac {M _ {h} ^ {2}}{f \sqrt {f ^ {2} - v ^ {2}}} - 2 \lambda_ {h \eta} \sqrt {1 - \frac {v ^ {2}}{f ^ {2}}}\right) ^ {2} \sqrt {1 - \frac {4 M _ {\eta} ^ {2}}{M _ {h} ^ {2}}}. \tag {2.41}
$$

Depending on the various  $\eta$  decay channels,  $h\rightarrow \eta \eta$  can lead to invisible decay (for the dark matter scenario), multi-boson final state (if  $\eta$  decays to a pair of EW bosons via WZW anomaly) or multi-jet final state (if  $\eta$  decays to  $jj$  or  $gg$  via fermion loops), etc. On the

![](images/4d30c589323000601b94af73f6384e11132af8d187c002ba68678c2deabc34df.jpg)  
Figure 1. The parameter space giving degenerate vacuums.

other hand, the Higgs total width in SM is extremely small that  $\Gamma_h = 4.07\mathrm{MeV}$  [66], thus even a small  $h\eta \eta$  vertex can change the Higgs branching ratios a lot. As SFOEWPT needs a sizable  $\lambda_{h\eta}$  (see eq. (2.33) for details), were  $h\rightarrow \eta \eta$  allowed it would dominate the Higgs decay. This would be ruled out by the existing experimental measurements [67, 68], which show compatible branching ratios with the SM prediction. To avoid this conflict, we will consider only the  $M_{\eta} > M_{h} / 2$  region, and  $h\to \eta \eta$  is then forbidden by phase space.

Given eq. (2.39), the coefficients in  $V(h, \eta)$  can be expressed in terms of  $f$ ,  $M_{\eta}$ ,  $\lambda_{\eta}$  and  $\lambda_{h\eta}$ , because  $M_h$  and  $v$  are fixed by experiments. As long as  $f \gg v$ , the dependence of  $f$  is mild and the degrees of freedom reduce to three. In figure 1 we plot the parameter regions allowed by eq. (2.33) for different  $M_{\eta}$  values. One can see that  $\lambda_{h\eta}$  has a positive correlation with  $M_{\eta}$ , as expected.

# 3 Deriving the scalar potential of NMCHM

In this section, we first classify the sources of the potential and then investigate them one by one. Especially, we will demonstrate that the IR contributions can't trigger SFOEWPT alone.

# 3.1 The sources of the scalar potential

The coefficients  $\mu_{h,\eta}^{2}$  and  $\lambda_{h,\eta,h\eta}$  in  $V(h,\eta)$  are generated by two kinds of SO(6)-breaking interactions. The first type is gauge interaction, see eq. (2.4). This breaks  $\mathrm{SO}(6) \times \mathrm{U}(1)_X$  into its largest subgroup containing the SM gauge group as an ideal, i.e.  $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y \times \mathrm{U}(1)_\eta$  [5], where  $\mathrm{U}(1)_\eta$  is the subgroup generated by  $\hat{T}_2^5$ . As a result, the gauge interactions contribute to the potential for  $h$  (i.e.  $\mu_h^2$  and  $\lambda_h$ ) but not  $\eta$  (i.e.  $\mu_\eta^2$  and  $\lambda_{\eta,h\eta}$ ).

The second source of the potential comes from the partial compositeness terms, i.e. eqs. (2.18) to (2.23). In general, they break  $\mathrm{SO}(6)\times \mathrm{U}(1)_X$  into  $\mathrm{SU}(2)_L\times \mathrm{U}(1)_Y$  and

Table 1. The sources of the scalar potential in the NMCHM.  

<table><tr><td></td><td>Gauge-induced</td><td>Fermion-induced</td></tr><tr><td>IR contributions (calculable)</td><td>Form factors from eq. (2.8), in terms of g(t), gρ and Mρ,a</td><td>Form factors from eqs. (2.11) and (2.18)~(2.23), in terms of M1,5,10 and yL,R1,5,10</td></tr><tr><td>UV contributions (estimated by NDA)</td><td>Local operators involved g(t)</td><td>Local operators involved yL,R1,5,10</td></tr></table>

contribute to all coefficients in  $V(h,\eta)$ . However, in some embeddings, accidentally the elementary fermion multiplet has a definite  $\mathrm{U}(1)_\eta$  quantum number and then its contribution to the  $\eta$  potential vanishes. For the embeddings considered in this paper, under the action of  $e^{i\alpha^5\hat{T}_2^5}$ ,

$$
\delta q _ {L} ^ {\mathbf {6}} = 0, \quad \delta t _ {R} ^ {\mathbf {1}} = 0, \quad \delta t _ {R} ^ {\mathbf {1 5}} = 0. \tag {3.1}
$$

Thus they have  $\mathrm{U}(1)_{\eta}$  quantum number zero. $^8$  As a result we expect  $\mu_{\eta}^{2}$  and  $\lambda_{\eta}$  receive no contributions from the  $q_{L}^{6}$ ,  $t_{R}^{1}$  and  $t_{R}^{15}$  embeddings ( $\lambda_{h\eta}$  may receive contributions from the combination of one of these embeddings and another  $\mathrm{U}(1)_{\eta}$ -breaking embedding). Hence in the  $\mathbf{6} + \mathbf{1}$  and  $\mathbf{6} + \mathbf{15}$  NMCHMs,  $\mathrm{U}(1)_{\eta}$  is only spontaneously broken by the strong dynamics and  $\eta$  remains as an exactly massless NGB. These two models are not only unable to trigger SFOEWPT but also ruled out by the experimental searches for axion [5, 69], thus they will not be studied in the rest of this paper. In summary, only the  $\mathbf{6} + \mathbf{6}$ ,  $\mathbf{15} + \mathbf{6}$  and  $\mathbf{15} + \mathbf{15}$  NMCHMs are considered for the SFOEWPT in the following text.

According to the calculability, the sources of the scalar potential are also classified into two types. The first type is the IR contributions, which come from the leading operators in Lagrangians eq. (2.8), eq. (2.11) and eqs. (2.18) to (2.23). When integrating out the heavy resonances and require suitable Weinberg sum rules, the IR contributions are calculable and expressed in terms of the resonances masses and couplings. The second type, denoted as the UV contributions, are from the local higher dimensional operators which depend on the interactions above the cutoff scale and their interplay with the SO(6)-breaking interactions. This type of contributions is incalculable but only estimated by NDA [46]. Unfortunately, NDA shows the UV contributions  $\gtrsim$  IR contributions [42], thus strictly speaking the scalar potential  $V(h,\eta)$  is not calculable in CHMs. To ensure the calculability, and partially inspired by the pion mass mechanism in QCD, ref. [42] proposes the MHP hypothesis, which assumes the UV contributions are negligible due to some unknown mechanism of the underlying theory. MHP has been generally adopted in the studies of CHMs [11, 42-45]. However, as we will demonstrate, under MHP all three NMCHMs we consider fail to trigger SFOEWPT. To realize a SFOEWPT, the UV contributions must be included. A summary of the sources of the scalar potential is given in table 1.

In the following subsections we will derive the scalar potential for the three benchmark NMCHMs: the  $6 + 6$ ,  $15 + 6$  and  $15 + 15$  models. For the IR contributions, we express the potential coefficients in terms of the form factor integrals; while for the UV contributions, we list the relevant local operators. For the Higgs field  $h$ , according to the sources of the

SO(6)-breaking interactions we can separate the coefficients into

$$
\mu_ {h} ^ {2} = \mu_ {g} ^ {2} + \mu_ {f} ^ {2}, \quad \lambda_ {h} = \lambda_ {g} + \lambda_ {f}, \tag {3.2}
$$

where “ $g$ ” and “ $f$ ” denote the gauge and partial compositeness (fermion) contributions, respectively. The  $\mu_{\eta}^{2}$  and  $\lambda_{\eta,h\eta}$  receive fermion contributions only. We will first discuss the gauge contributions and then the fermion contributions for various embeddings.

# 3.2 Contribution from vector bosons

The gauge contributions are universal for all benchmark NMCHMs. Generally, the gauge-induced potential can be written in a polynomial form

$$
V _ {g} (h) = \frac {\mu_ {g} ^ {2}}{2} h ^ {2} + \frac {\lambda_ {g}}{4} h ^ {4}, \tag {3.3}
$$

where the coefficients receive contributions from both IR and UV sources.

The IR contributions. Integrating out the  $\rho$  and  $a$  resonances in eq. (2.8) we get the Lagrangian involving vector bosons up to quadratic terms in the momentum space

$$
\mathcal {L} _ {\rho} \rightarrow \frac {1}{2} P _ {T} ^ {\mu \nu} \left(- p ^ {2} B _ {\mu} B _ {\nu} - p ^ {2} \operatorname {t r} \left[ W _ {\mu} W _ {\nu} \right] + \Pi_ {0} (p ^ {2}) \operatorname {t r} \left[ A _ {\mu} A _ {\nu} \right] + \Pi_ {1} (p ^ {2}) \Sigma^ {\dagger} A _ {\mu} A _ {\nu} \Sigma\right), \tag {3.4}
$$

where  $\Pi_{0,1}(p^2)$  are form factors, and  $A_{\mu}$  is defined eq. (2.4). The transverse and longitudinal projection operators are defined as

$$
P _ {T} ^ {\mu \nu} = g ^ {\mu \nu} - \frac {p ^ {\mu} p ^ {\nu}}{p ^ {2}}, \quad P _ {L} ^ {\mu \nu} = \frac {p ^ {\mu} p ^ {\nu}}{p ^ {2}}, \tag {3.5}
$$

respectively. Under the unitary gauge, eq. (3.4) becomes

$$
\begin{array}{l} \mathcal {L} _ {\rho} \rightarrow \frac {1}{2} P _ {T} ^ {\mu \nu} \left\{\left(- p ^ {2} + \frac {g _ {0} ^ {r 2}}{g _ {0} ^ {2}} \Pi_ {0} (p ^ {2})\right) B _ {\mu} B _ {\nu} + \left(- p ^ {2} + \Pi_ {0} (p ^ {2})\right) W _ {\mu} ^ {a} W _ {\nu} ^ {a} \right. \\ \left. + \frac {\Pi_ {1} \left(p ^ {2}\right)}{4} \frac {h ^ {2}}{f ^ {2}} \left[ W _ {\mu} ^ {1} W _ {\nu} ^ {1} + W _ {\mu} ^ {2} W _ {\nu} ^ {2} + \left(W _ {\mu} ^ {3} - \frac {g _ {0} ^ {\prime}}{g _ {0}} B _ {\mu}\right) \left(W _ {\nu} ^ {3} - \frac {g _ {0} ^ {\prime}}{g _ {0}} B _ {\nu}\right) \right] \right\}, \tag {3.6} \\ \end{array}
$$

and it contributes to the Higgs potential as [3]

$$
V _ {g} ^ {\mathrm {I R}} (h) \approx \frac {6}{2} \int \frac {d ^ {4} Q}{(2 \pi) ^ {4}} \ln \left(1 + \frac {\Pi_ {1}}{4 \Pi_ {W}} \frac {h ^ {2}}{f ^ {2}}\right) + \frac {3}{2} \int \frac {d ^ {4} Q}{(2 \pi) ^ {4}} \ln \left[ 1 + \left(\frac {g _ {0} ^ {\prime 2}}{g _ {0} ^ {2}} \frac {\Pi_ {1}}{4 \Pi_ {B}} + \frac {\Pi_ {1}}{4 \Pi_ {W}}\right) \frac {h ^ {2}}{f ^ {2}} \right], \tag {3.7}
$$

where  $Q^2 \equiv -p^2$ ,  $\Pi_W = Q^2 + \Pi_0$  and  $\Pi_B = Q^2 + (g_0'^2 / g_0^2)\Pi_0$ . Above result is derived under the assumption of Landau gauge  $\xi = 0$ . Only in this gauge can we omit the contributions from the ghost fields [70]. An expansion of eq. (3.7) up to  $h^4$  can give a very good approximation, because higher order terms are suppressed by  $g_0^2 v^2 / f^2$ . Matching the polynomial potential to eq. (3.3), we get

$$
\begin{array}{l} \left(\mu_ {g} ^ {2}\right) ^ {\mathrm {I R}} = \frac {3}{4 f ^ {2}} \int \frac {d ^ {4} Q}{(2 \pi) ^ {4}} \left(\frac {g _ {0} ^ {\prime 2}}{g _ {0} ^ {2}} \frac {\Pi_ {1}}{\Pi_ {B}} + 3 \frac {\Pi_ {1}}{\Pi_ {W}}\right), \\ \left(\lambda_ {g}\right) ^ {\mathrm {I R}} = - \frac {3}{1 6 f ^ {4}} \int \frac {d ^ {4} Q}{(2 \pi) ^ {4}} \left[ 2 \left(\frac {\Pi_ {1}}{\Pi_ {W} ^ {2}}\right) ^ {2} + \left(\frac {g _ {0} ^ {\prime 2}}{g _ {0} ^ {2}} \frac {\Pi_ {1}}{\Pi_ {B}} + \frac {\Pi_ {1}}{\Pi_ {W}}\right) ^ {2} \right]. \tag {3.8} \\ \end{array}
$$

Since  $\Pi_{B,W} \sim Q^2$  at large momentum, the coefficients are quadratic divergent. To get a convergent  $V_g$ , the  $\Pi_1$  form factor should at least have a scaling  $Q^{-4}$ . This can be realized via suitable Weinberg sum rules, as we will see in section 4.

The UV contributions. This part of contributions comes from the higher order operators, which can be written down using the spurion trick [46]. We rewrite the gauge field as

$$
g A _ {\mu} = g T _ {L} ^ {a} W _ {\mu} ^ {a} + g ^ {\prime} T _ {R} ^ {3} B _ {\mu} \equiv \mathcal {G} _ {\bar {A} a} T ^ {\bar {A}} W _ {\mu} ^ {a} + \mathcal {G} _ {\bar {A}} ^ {\prime} T ^ {\bar {A}} B _ {\mu}. \tag {3.9}
$$

The symmetry of the theory is formally extended to  $\mathrm{SO}(6)\times \mathrm{SU}(2)_0\times \mathrm{U}(1)_0$ , in which the spurions have quantum number

$$
\mathcal {G} _ {\bar {A} a}: (\mathbf {6}, \mathbf {3} _ {0}), \quad \mathcal {G} _ {\bar {A}} ^ {\prime}: (\mathbf {6}, \mathbf {1} _ {0}). \tag {3.10}
$$

The VEVs of the spurions

$$
\left\langle \mathcal {G} _ {\bar {A} a} \right\rangle = g \delta_ {\bar {A} a _ {L}}, \quad \left\langle \mathcal {G} _ {\bar {A}} ^ {\prime} \right\rangle = g ^ {\prime} \delta_ {\bar {A} 3 _ {R}}, \tag {3.11}
$$

break the  $\mathrm{SO}(6)\times \mathrm{SU}(2)_0\times \mathrm{U}(1)_0$  back to  $\mathrm{SU}(2)_L\times \mathrm{U}(1)_Y\times \mathrm{U}(1)_\eta$ . The spurions can be used to count the number of gauge insertions when generating a specific operator. Denoting  $\mathcal{G}_a = \mathcal{G}_{\bar{A} a}T^{\bar{A}}$  and  $\mathcal{G}' = \mathcal{G}_{\bar{A}}'T^{\bar{A}}$ , the relevant operators for  $h$  potential are

$$
c _ {g} f ^ {4} \Sigma^ {\dagger} \mathcal {G} _ {a} \mathcal {G} _ {a} \Sigma , \quad c _ {g ^ {\prime}} f ^ {4} \Sigma^ {\dagger} \mathcal {G} ^ {\prime} \mathcal {G} ^ {\prime} \Sigma , \quad \frac {d _ {g}}{1 6 \pi^ {2}} f ^ {4} \left(\Sigma^ {\dagger} \mathcal {G} _ {a} \mathcal {G} _ {a} \Sigma\right) ^ {2}, \quad \frac {d _ {g ^ {\prime}}}{1 6 \pi^ {2}} f ^ {4} \left(\Sigma^ {\dagger} \mathcal {G} ^ {\prime} \mathcal {G} ^ {\prime} \Sigma\right) ^ {2}, \tag {3.12}
$$

where the coefficients  $c_{g,g'}$  and  $d_{g,g'}$  are all  $\mathcal{O}(1)$  according to NDA. Matching above operators to eq. (3.3) yields

$$
(\mu_ {g} ^ {2}) ^ {\mathrm {U V}} = c _ {g} \frac {3 g ^ {2}}{2} f ^ {2} + c _ {g ^ {\prime}} \frac {g ^ {\prime 2}}{2} f ^ {2}, (\lambda_ {g}) ^ {\mathrm {U V}} = d _ {g} \frac {9 g ^ {4}}{6 4 \pi^ {2}} + d _ {g ^ {\prime}} \frac {g ^ {\prime 4}}{6 4 \pi^ {2}}. (3. 1 3)
$$

# 3.3 Contribution from fermions: the  $6 + 6$  model

The fermion-induced potential of all kinds of embeddings can be generally written in

$$
V _ {f} (h, \eta) = \frac {\mu_ {f} ^ {2}}{2} h ^ {2} + \frac {\lambda_ {f}}{4} h ^ {4} + \frac {\mu_ {\eta} ^ {2}}{2} \eta^ {2} + \frac {\lambda_ {\eta}}{4} \eta^ {4} + \frac {\lambda_ {h \eta}}{2} h ^ {2} \eta^ {2}, \tag {3.14}
$$

and the contributions to the coefficients can be classified into IR and UV ones.

The IR contributions. Integrating out the top partners in eq. (2.19), the general fermion Lagrangian up to quadratic term is

$$
\begin{array}{l} \mathcal {L} _ {\mathbf {6} + \mathbf {6}} \rightarrow \bar {q} _ {L} ^ {\mathbf {6}} \not p \left(\Pi_ {0} ^ {q} (p ^ {2}) + \Pi_ {1} ^ {q} (p ^ {2}) \Sigma \Sigma^ {\dagger}\right) q _ {L} ^ {\mathbf {6}} + \bar {t} _ {R} ^ {\mathbf {6}} \not p \left(\Pi_ {0} ^ {t} (p ^ {2}) + \Pi_ {1} ^ {t} (p ^ {2}) \Sigma \Sigma^ {\dagger}\right) t _ {R} ^ {\mathbf {6}} \\ + \bar {q} _ {L} ^ {\mathbf {6}} \left(M _ {0} ^ {t} \left(p ^ {2}\right) + M _ {1} ^ {t} \left(p ^ {2}\right) \Sigma \Sigma^ {\dagger}\right) t _ {R} ^ {\mathbf {6}} + \text {h . c .}, \tag {3.15} \\ \end{array}
$$

where  $\Pi_{q,t}^{0,1}(p^2)$  and  $M_{0,1}^{t}(p^{2})$  are form factors. Above Lagrangian is greatly simplified under the unitary gauge

$$
\begin{array}{l} \mathcal {L} _ {\mathbf {6 + 6}} \rightarrow \bar {t} _ {L} \rlap / p \left(\Pi_ {0} ^ {q} + \frac {\Pi_ {1} ^ {q}}{2} \frac {h ^ {2}}{f ^ {2}}\right) t _ {L} + \bar {t} _ {R} \rlap / p \left[ \Pi_ {0} ^ {t} + \Pi_ {1} ^ {t} \left(c _ {\theta} ^ {2} \frac {\eta^ {2}}{f ^ {2}} + s _ {\theta} ^ {2} \left(1 - \frac {h ^ {2} + \eta^ {2}}{f ^ {2}}\right)\right)\right] t _ {R} \\ - \frac {M _ {1} ^ {t}}{\sqrt {2}} \frac {h}{f} \left(s _ {\theta} \sqrt {1 - \frac {h ^ {2} + \eta^ {2}}{f ^ {2}} + i c _ {\theta} \frac {\eta}{f}}\right) \bar {t} _ {L} t _ {R} + \text {h . c .}, \tag {3.16} \\ \end{array}
$$

where we have chosen the unphysical phase  $\phi = \pi /2$  in  $t_R^6$ . The  $\bar{b}_L b_L$  form factor is accidentally zero because of the  $q_{L}^{6}$  embedding. Note that  $(h^{2} + \eta^{2}) / f^{2} < 1$  by definition (see eq. (2.5) for details), thus the square root in eq. (3.16) is always well-defined. In the studies involving dark matter,  $\theta = \pi /2$  (for which the  $t\bar{t}\eta$  vertex is absent) is chosen to ensure the  $\eta \rightarrow -\eta$  symmetry and get a stable dark matter candidate [10, 11]. Here we focus on SFOEWPT where the stability of  $\eta$  is unimportant, thus allow  $\theta$  to be any real number.

The effective potential caused by eq. (3.16) is

$$
\begin{array}{l} V _ {f} ^ {\mathrm {I R}} (h, \eta) \approx - 2 N _ {c} \int \frac {d ^ {4} Q}{(2 \pi) ^ {4}} \left\{\ln \left(1 + \frac {\Pi_ {1} ^ {q}}{2 \Pi_ {0} ^ {q}} \frac {h ^ {2}}{f ^ {2}}\right) + \ln \left[ 1 + \frac {\Pi_ {1} ^ {t}}{\Pi_ {0} ^ {t}} \left(s _ {\theta} ^ {2} \left(1 - \frac {h ^ {2}}{f ^ {2}}\right) + c _ {2 \theta} \frac {\eta^ {2}}{f ^ {2}}\right) \right] \right. \\ \left. + \ln \left[ 1 + \frac {1}{Q ^ {2}} \frac {\left| M _ {1} ^ {t} \right| ^ {2}}{2 \Pi_ {0} ^ {q} \Pi_ {0} ^ {t}} \frac {h ^ {2}}{f ^ {2}} \left(s _ {\theta} ^ {2} \left(1 - \frac {h ^ {2}}{f ^ {2}}\right) + c _ {2 \theta} \frac {\eta^ {2}}{f ^ {2}}\right) \right] \right\}, \tag {3.17} \\ \end{array}
$$

with  $N_{c} = 3$  being the QCD color number of the SM quarks. A good approximation can be obtained by truncating the Taylor expansion up to the quartic term of  $h$  and  $\eta$ , as shown in eq. (3.14). The coefficients can be expressed in terms of five basic integrals [45],

$$
\alpha_ {q, t} = \frac {N _ {c}}{f ^ {2}} \int \frac {d ^ {4} Q}{(2 \pi) ^ {4}} \frac {\Pi_ {1} ^ {q , t}}{\Pi_ {0} ^ {q , t}}, \quad \beta_ {q, t} = \frac {N _ {c}}{f ^ {4}} \int \frac {d ^ {4} Q}{(2 \pi) ^ {4}} \left(\frac {\Pi_ {1} ^ {q , t}}{\Pi_ {0} ^ {q , t}}\right) ^ {2}, \quad \epsilon = \frac {N _ {c}}{f ^ {4}} \int \frac {d ^ {4} Q}{(2 \pi) ^ {4}} \frac {| M _ {1} ^ {t} | ^ {2}}{Q ^ {2} \Pi_ {0} ^ {q} \Pi_ {0} ^ {t}}, \tag {3.18}
$$

giving

$$
(\mu_ {f} ^ {2}) ^ {\mathrm {I R}} = - 2 \alpha_ {q} + 4 s _ {\theta} ^ {2} \alpha_ {t} - 4 s _ {\theta} ^ {4} f ^ {2} \beta_ {t} - 2 s _ {\theta} ^ {2} f ^ {2} \epsilon , (\mu_ {\eta} ^ {2}) ^ {\mathrm {I R}} = - 4 c _ {2 \theta} \alpha_ {t} + 4 c _ {2 \theta} s _ {\theta} ^ {2} f ^ {2} \beta_ {t},
$$

$$
\left(\lambda_ {f}\right) ^ {\mathrm {I R}} = \beta_ {q} + 4 s _ {\theta} ^ {4} \beta_ {t} + 4 s _ {\theta} ^ {2} \epsilon , \quad \left(\lambda_ {\eta}\right) ^ {\mathrm {I R}} = 4 c _ {2 \theta} ^ {2} \beta_ {t}, \tag {3.19}
$$

$$
(\lambda_ {h \eta}) ^ {\mathrm {I R}} = - 4 c _ {2 \theta} s _ {\theta} ^ {2} \beta_ {t} - 2 c _ {2 \theta} \epsilon .
$$

Note that  $(\mu_{\eta}^{2})^{\mathrm{IR}}$  and  $(\lambda_{\eta})^{\mathrm{IR}}$  are irrelevant to  $\alpha_{q}$  and  $\beta_{q}$  due to the  $\mathrm{U}(1)_{\eta}$  symmetry of  $q_{L}^{6}$ . In addition, provided  $\theta = \pi /4$ ,  $\eta$  would decouple from the effective potential. This is because in this limit even  $t_R^6$  has a definite  $\mathrm{U}(1)_{\eta}$  quantum number:  $-1 / \sqrt{2}$ , and then  $\eta$  is a true NGB that free of potential [5]. The form factors in the basic integrals of eq. (3.18) can be derived for the QCD-like underlying theory in terms of the masses of top partners and mixing couplings. Although they are generally divergent, by imposing suitable Weinberg sum rules we can make them converge and get the finite results of eq. (3.19). This will be done in section 4.

Before turning to the UV contributions, we demonstrate that SFOEWPT cannot be triggered by the IR contributions alone. The issue is from  $(\mu_{\eta}^{2})^{\mathrm{IR}}$  and  $(\lambda_{\eta})^{\mathrm{IR}}$ . SFOEWPT

needs a local minimum along the  $\eta$  direction, which is

$$
w = \sqrt {- \frac {\mu_ {\eta} ^ {2}}{\lambda_ {\eta}}} \xrightarrow {\mathrm {I R o n l y}} \sqrt {\frac {\alpha_ {t} - s _ {\theta} ^ {2} f ^ {2} \beta_ {t}}{c _ {2 \theta} \beta_ {t}}}. (3. 2 0)
$$

However, as  $\alpha_{t}$  and  $\beta_{t}$  come from the expansion of the same logarithm,  $|\alpha_t| \gg \beta_t f^2$  is expected, thus  $w^{2}|_{\mathrm{IR}} \gg f^{2}$ . This inequality can never be achieved because  $\eta < f$  is given by its definition, see eq. (2.5). Therefore, the IR contributions fail to trigger SFOEWPT.

The UV contributions. A spurion approach is used to rewrite

$$
q _ {L} ^ {\mathbf {6}} = \mathcal {Q} ^ {\mathbf {6}} q _ {L}, \quad t _ {R} ^ {\mathbf {6}} = \mathcal {T} ^ {\mathbf {6}} t _ {R}, \tag {3.21}
$$

where the spurions have quantum numbers

$$
\mathcal {Q} ^ {\mathbf {6}}: \left(\mathbf {6} _ {2 / 3}, \mathbf {2} _ {- 1 / 6}\right), \quad \mathcal {T} ^ {\mathbf {6}}: \left(\mathbf {6} _ {2 / 3}, \mathbf {1} _ {- 2 / 3}\right), \tag {3.22}
$$

under the extended  $\mathrm{SO}(6)\times \mathrm{U}(1)_X\times \mathrm{SU}(2)_0\times \mathrm{U}(1)_0$  group. Their VEVs,

$$
\left\langle \mathcal {Q} ^ {6} \right\rangle = \frac {1}{\sqrt {2}} \left( \begin{array}{c c c c c} 0 & 0 & i & - 1 & 0 & 0 \\ i & 1 & 0 & 0 & 0 & 0 \end{array} \right) ^ {T}, \quad \left\langle \mathcal {T} ^ {6} \right\rangle = \left( \begin{array}{c c c c c} 0 & 0 & 0 & 0 & e ^ {i \phi} c _ {\theta} s _ {\theta} \end{array} \right) ^ {T}, \tag {3.23}
$$

break the symmetry down to  $\mathrm{SU}(2)_L\times \mathrm{U}(1)_Y$ . The operators relevant for scalar potential are

$$
c _ {f} ^ {L} \left| y _ {L} \right| ^ {2} f ^ {4} \Sigma^ {\dagger} \mathcal {Q} ^ {6} \mathcal {Q} ^ {6 \dagger} \Sigma , \quad c _ {f} ^ {R} \left| y _ {R} \right| ^ {2} f ^ {4} \Sigma^ {\dagger} \mathcal {T} ^ {6} \mathcal {T} ^ {6 \dagger} \Sigma ,
$$

$$
\frac {d _ {f} ^ {L}}{1 6 \pi^ {2}} \left| y _ {L} \right| ^ {4} f ^ {4} \left(\Sigma^ {\dagger} \mathcal {Q} ^ {\mathbf {6}} \mathcal {Q} ^ {\mathbf {6} \dagger} \Sigma\right) ^ {2}, \quad \frac {d _ {f} ^ {R}}{1 6 \pi^ {2}} \left| y _ {R} \right| ^ {4} f ^ {4} \left(\Sigma^ {\dagger} \mathcal {T} ^ {\mathbf {6}} \mathcal {T} ^ {\mathbf {6} \dagger} \Sigma\right) ^ {2}, \tag {3.24}
$$

where the coefficients  $c_{f}^{L,R}$  and  $d_{f}^{L,R}$  are the  $\mathcal{O}(1)$  Wilson coefficients according to NDA. The contributions to the scalar potential eq. (3.14) are then

$$
(\mu_ {f} ^ {2}) ^ {\mathrm {U V}} = c _ {f} ^ {L} | y _ {L} | ^ {2} f ^ {2} - 2 c _ {f} ^ {R} | y _ {R} | ^ {2} f ^ {2} s _ {\theta} ^ {2} - \frac {d _ {f} ^ {R}}{4 \pi^ {2}} | y _ {R} | ^ {4} f ^ {2} s _ {\theta} ^ {4},
$$

$$
\left(\mu_ {\eta} ^ {2}\right) ^ {\mathrm {U V}} = 2 c _ {f} ^ {R} \left| y _ {R} \right| ^ {2} f ^ {2} c _ {2 \theta} + \frac {d _ {f} ^ {R}}{4 \pi^ {2}} \left| y _ {R} \right| ^ {4} f ^ {2} s _ {\theta} ^ {2} c _ {2 \theta}, \tag {3.25}
$$

$$
(\lambda_ {f}) ^ {\mathrm {U V}} = \frac {d _ {f} ^ {L}}{1 6 \pi^ {2}} | y _ {L} | ^ {4} + \frac {d _ {f} ^ {R}}{4 \pi^ {2}} | y _ {R} | ^ {4} s _ {\theta} ^ {4},
$$

$$
\left(\lambda_ {\eta}\right) ^ {\mathrm {U V}} = \frac {d _ {f} ^ {R}}{4 \pi^ {2}} \left| y _ {R} \right| ^ {4} c _ {2 \theta} ^ {2}, \quad \left(\lambda_ {h \eta}\right) ^ {\mathrm {U V}} = - \frac {d _ {f} ^ {R}}{4 \pi^ {2}} \left| y _ {R} \right| ^ {4} s _ {\theta} ^ {2} c _ {2 \theta}.
$$

The  $c_{f}^{L}$  and  $d_{f}^{L}$  don't contribute to  $(\mu_{\eta}^{2})^{\mathrm{UV}}$  and  $(\lambda_{\eta})^{\mathrm{UV}}$  because of the  $\mathrm{U}(1)_\eta$  symmetry. Again,  $\eta$  decouples if  $\theta = \pi /4$

The combination of IR and UV contributions gives the complete fermion-induced potential for the  $6 + 6$  NMCHM. If  $d_f^R$  is large enough, then  $\lambda_{\eta}$  receives an enhancement and  $w^{2} \ll f^{2}$  may be satisfied. In section 4 we will show numerically this is indeed the case, i.e. SFOEWPT can be triggered in the  $6 + 6$  NMCHM when both IR and UV contributions are taken into account.

# 3.4 Contribution from fermions: the  $15 + 6$  model

In this subsection, we match the IR and UV contributions of the  $15 + 6$  model into the general potential in eq. (3.14).

The IR contributions. Integrating out the top partners from eq. (2.22) gives

$$
\begin{array}{l} \mathcal {L} _ {\mathbf {1 5} + \mathbf {6}} \rightarrow \left(\Pi_ {0} ^ {q} (p ^ {2}) \mathrm {t r} \left[ \bar {q} _ {L} ^ {\mathbf {1 5}} p q _ {L} ^ {\mathbf {1 5}} \right] + \Pi_ {1} ^ {q} (p ^ {2}) \Sigma^ {\dagger} \bar {q} _ {L} ^ {\mathbf {1 5}} p q _ {L} ^ {\mathbf {1 5}} \Sigma\right) \\ + \left(\Pi_ {0} ^ {t} (p ^ {2}) \bar {t} _ {R} ^ {\mathbf {6}} \not p t _ {R} ^ {\mathbf {6}} + \Pi_ {1} ^ {t} (p ^ {2}) \bar {t} _ {R} ^ {\mathbf {6}} \not p \Sigma \Sigma^ {\dagger} t _ {R} ^ {\mathbf {6}}\right) + M _ {1} ^ {t} (p ^ {2}) \Sigma^ {\dagger} \bar {q} _ {L} ^ {\mathbf {1 5}} t _ {R} ^ {\mathbf {6}} + \text {h . c .}, \tag {3.26} \\ \end{array}
$$

which is simplified in the unitary gauge as

$$
\begin{array}{l} \mathcal {L} _ {\mathbf {1 5 + 6}} \rightarrow \bar {b} _ {L} \rlap / p \left(\Pi_ {0} ^ {q} + \frac {\Pi_ {1} ^ {q}}{2} \frac {\eta^ {2}}{f ^ {2}}\right) b _ {L} + \bar {t} _ {L} \rlap / p \left[ \Pi_ {0} ^ {q} + \frac {\Pi_ {1} ^ {q}}{2} \left(\frac {h ^ {2}}{2 f ^ {2}} + \frac {\eta^ {2}}{f ^ {2}}\right)\right] t _ {L} \\ + \bar {t} _ {R} \not \psi \left[ \Pi_ {0} ^ {t} + \Pi_ {1} ^ {t} \left(c _ {\theta} ^ {2} \frac {\eta^ {2}}{f ^ {2}} + s _ {\theta} ^ {2} \left(1 - \frac {h ^ {2} + \eta^ {2}}{f ^ {2}}\right)\right) \right] t _ {R} - \frac {M _ {1} ^ {t}}{2} \frac {h}{f} c _ {\theta} \bar {t} _ {L} t _ {R} + \text {h . c .}, \tag {3.27} \\ \end{array}
$$

where the unphysical phase  $\phi$  in  $t_R^6$  is set to  $\pi /2$ . The corresponding potential can be derived, expanded up to quartic level and matched to the polynomial potential,

$$
\left(\mu_ {f} ^ {2}\right) ^ {\mathrm {I R}} = - \alpha_ {q} + 4 \alpha_ {t} s _ {\theta} ^ {2} - 4 s _ {\theta} ^ {4} f ^ {2} \beta_ {t} - c _ {\theta} ^ {2} f ^ {2} \epsilon , \quad \left(\mu_ {\eta} ^ {2}\right) ^ {\mathrm {I R}} = - 4 \alpha_ {q} - 4 \alpha_ {t} c _ {2 \theta} + 4 c _ {2 \theta} s _ {\theta} ^ {2} \beta_ {t} f ^ {2},
$$

$$
\left(\lambda_ {f}\right) ^ {\mathrm {I R}} = \frac {\beta_ {q}}{4} + 4 s _ {\theta} ^ {4} \beta_ {t}, \quad \left(\lambda_ {\eta}\right) ^ {\mathrm {I R}} = 2 \beta_ {q} + 4 c _ {2 \theta} ^ {2} \beta_ {t}, \tag {3.28}
$$

$$
(\lambda_ {h \eta}) ^ {\mathrm {I R}} = \frac {\beta_ {q}}{2} - 4 c _ {2 \theta} s _ {\theta} ^ {2} \beta_ {t}.
$$

And the five basic integrals are the same as eq. (3.18).

The  $15 + 6$  model should be the most hopeful one to realize SFOEWPT using only the IR contributions, because both the embeddings  $q_{L}^{15}$  and  $t_R^6$  break  $\mathrm{U}(1)_\eta$  and then contribute to  $\mu_{\eta}^{2}$ . Therefore, a cancelation may exist in eq. (3.28) and reduce  $(\mu_{\eta}^{2})^{\mathrm{IR}}$  to an acceptable value that gives  $w^{2}\ll f^{2}$ . However, the quartic coefficients suffer from another problem. The condition eq. (2.33) requires  $\lambda_{h\eta}^{2} > \lambda_{h}\lambda_{\eta}$ . Since  $\lambda_f\gg \lambda_g$  [42], we expect

$$
\begin{array}{l} (\lambda_ {h \eta} ^ {2}) ^ {\mathrm {I R}} - (\lambda_ {h}) ^ {\mathrm {I R}} (\lambda_ {\eta}) ^ {\mathrm {I R}} \approx (\lambda_ {h \eta} ^ {2}) ^ {\mathrm {I R}} - (\lambda_ {f}) ^ {\mathrm {I R}} (\lambda_ {\eta}) ^ {\mathrm {I R}} \\ = - \frac {1}{4} \beta_ {q} \left[ \beta_ {q} + 8 \left(1 - c _ {2 \theta}\right) \beta_ {t} + 2 \left(1 + c _ {4 \theta}\right) \beta_ {t} \right] <   0, \tag {3.29} \\ \end{array}
$$

where the last inequality holds because  $\beta_{q,t} > 0$  by definition. Therefore, the necessary condition for SFOEWPT is broken and then IR contributions from the  $15 + 6$  cannot realize SFOEWPT.

The UV contributions. For  $q_{L}^{15}$ , we introduce spurion as

$$
\left(q _ {L} ^ {\mathbf {1 5}}\right) _ {I J} = \left(\mathcal {Q} ^ {\mathbf {1 5}}\right) _ {I J \alpha} (q _ {L}) _ {\alpha}, \quad \mathcal {Q} ^ {\mathbf {1 5}}: (\mathbf {1 5} _ {2 / 3}, \mathbf {2} _ {- 1 / 6}), \tag {3.30}
$$

under the extended  $\mathrm{SO}(6)\times \mathrm{U}(1)_X\times \mathrm{SU}(2)_0\times \mathrm{U}(1)_0$  group (here  $\alpha = 1,2$  is the subscript of  $\mathrm{SU}(2)_0$  elementary representation). The VEV of  $\mathcal{Q}^{15}$  can be inferred from eq. (2.16) thus not shown here. The relevant operators for the scalar potential are

For the fermion contributions, we have

$$
c _ {f} ^ {L} \left| y _ {L} \right| ^ {2} f ^ {4} \Sigma^ {\dagger} \mathcal {Q} _ {\alpha} ^ {\mathbf {1 5}} \mathcal {Q} _ {\alpha} ^ {\mathbf {1 5} \dagger} \Sigma , \quad \frac {d _ {f} ^ {L}}{1 6 \pi^ {2}} \left| y _ {L} \right| ^ {4} f ^ {4} \left(\Sigma^ {\dagger} \mathcal {Q} _ {\alpha} ^ {\mathbf {1 5}} \mathcal {Q} _ {\alpha} ^ {\mathbf {1 5} \dagger} \Sigma\right) ^ {2}, \qquad (3. 3 1)
$$

where the coefficients  $c_{f}^{L}$  and  $d_{f}^{L}$  are  $\mathcal{O}(1)$  numbers. The spurion relevant to  $t_R^6$  and the corresponding operators have been introduced in last subsection. Combining them together we get the UV contributions to the scalar potential

$$
(\mu_ {f} ^ {2}) ^ {\mathrm {U V}} = \frac {c _ {f} ^ {L}}{2} | y _ {L} | ^ {2} f ^ {2} - 2 c _ {f} ^ {R} | y _ {R} | ^ {2} f ^ {2} s _ {\theta} ^ {2} - \frac {d _ {f} ^ {R}}{4 \pi^ {2}} | y _ {R} | ^ {4} f ^ {2} s _ {\theta} ^ {4},
$$

$$
\left(\mu_ {\eta} ^ {2}\right) ^ {\mathrm {U V}} = 2 c _ {f} ^ {L} \left| y _ {L} \right| ^ {2} f ^ {2} + 2 c _ {f} ^ {R} \left| y _ {R} \right| ^ {2} f ^ {2} c _ {2 \theta} + \frac {d _ {f} ^ {R}}{4 \pi^ {2}} \left| y _ {R} \right| ^ {4} f ^ {2} s _ {\theta} ^ {2} c _ {2 \theta}, \tag {3.32}
$$

$$
(\lambda_ {f}) ^ {\mathrm {U V}} = \frac {d _ {f} ^ {L}}{6 4 \pi^ {2}} | y _ {L} | ^ {4} + \frac {d _ {f} ^ {R}}{4 \pi^ {2}} | y _ {R} | ^ {4} s _ {\theta} ^ {4},
$$

$$
(\lambda_ {\eta}) ^ {\mathrm {U V}} = \frac {d _ {f} ^ {L}}{4 \pi^ {2}} | y _ {L} | ^ {4} + \frac {d _ {f} ^ {R}}{4 \pi^ {2}} | y _ {R} | ^ {4} c _ {2 \theta} ^ {2}, (\lambda_ {h \eta}) ^ {\mathrm {U V}} = \frac {d _ {f} ^ {L}}{1 6 \pi^ {2}} | y _ {L} | ^ {4} - \frac {d _ {f} ^ {R}}{4 \pi^ {2}} | y _ {R} | ^ {4} s _ {\theta} ^ {2} c _ {2 \theta}.
$$

With the assistance of the UV contributions,  $\lambda_{h\eta}$  may be enhanced to be larger than  $\sqrt{\lambda_h\lambda_\eta}$  and the necessary conditions of SFOEWPT are achieved.

# 3.5 Contribution from fermions: the  $15 + 15$  model

The IR contribution. Integrating out the top partners in eq. (2.23), the Lagrangian up to quadratic term is

$$
\begin{array}{l} \mathcal {L} _ {\mathbf {1 5} + \mathbf {1 5}} \rightarrow \left(\Pi_ {0} ^ {q} (p ^ {2}) \mathrm {t r} [ \bar {q} _ {L} ^ {\mathbf {1 5}} \not p q _ {L} ^ {\mathbf {1 5}} ] + \Pi_ {1} ^ {q} (p ^ {2}) \Sigma^ {\dagger} \bar {q} _ {L} ^ {\mathbf {1 5}} \not p q _ {L} ^ {\mathbf {1 5}} \Sigma\right) \\ + \left(\Pi_ {0} ^ {t} (p ^ {2}) \operatorname {t r} [ \bar {t} _ {R} ^ {\mathbf {1 5}} p t _ {R} ^ {\mathbf {1 5}} ] + \Pi_ {1} ^ {t} (p ^ {2}) \Sigma^ {\dagger} \bar {t} _ {R} ^ {\mathbf {1 5}} p t _ {R} ^ {\mathbf {1 5}} \Sigma\right) + M _ {1} ^ {t} (p ^ {2}) \Sigma^ {\dagger} \bar {q} _ {L} ^ {\mathbf {1 5}} t _ {R} ^ {\mathbf {1 5}} \Sigma + \text {h . c .}, \tag {3.33} \\ \end{array}
$$

Using unitary gauge and choosing the phase  $\phi = 0$  in  $t_R^{15}$ , we can simplify the expression as

$$
\begin{array}{l} \mathcal {L} _ {\mathbf {1 5} + \mathbf {1 5}} \rightarrow \bar {b} _ {L} \not p \left(\Pi_ {0} ^ {q} + \frac {\Pi_ {1} ^ {q}}{2} \frac {\eta^ {2}}{f ^ {2}}\right) b _ {L} \\ + \bar {t} _ {L} \rlap / p \left[ \Pi_ {0} ^ {q} + \frac {\Pi_ {1} ^ {q}}{2} \left(\frac {h ^ {2}}{2 f ^ {2}} + \frac {\eta^ {2}}{f ^ {2}}\right) \right] t _ {L} + \bar {t} _ {R} \rlap / p \left[ \Pi_ {0} ^ {t} + \frac {\Pi_ {1} ^ {t}}{4} \left(2 s _ {\theta} ^ {2} + (1 - 3 s _ {\theta} ^ {2}) \frac {h ^ {2}}{f ^ {2}}\right) \right] t _ {R} \\ + \frac {M _ {1} ^ {t}}{4} \frac {h}{f} \left(\sqrt {2} s _ {\theta} \sqrt {1 - \frac {h ^ {2} + \eta^ {2}}{f ^ {2}}} + i \frac {\eta}{f} c _ {\theta}\right) \bar {t} _ {L} t _ {R} + \text {h . c .}. \tag {3.34} \\ \end{array}
$$

Matching the corresponding potential to the polynomial form eq. (3.14) gives the coefficients

$$
(\mu_ {f} ^ {2}) ^ {\mathrm {I R}} = - \alpha_ {q} - \alpha_ {t} (1 - 3 s _ {\theta} ^ {2}) + \frac {\beta_ {t} f ^ {2}}{2} (1 - 3 s _ {\theta} ^ {2}) s _ {\theta} ^ {2} - \frac {\epsilon f ^ {2}}{2} s _ {\theta} ^ {2}, (\mu_ {\eta} ^ {2}) ^ {\mathrm {I R}} = - 4 \alpha_ {q},
$$

$$
\left(\lambda_ {f}\right) ^ {\mathrm {I R}} = \frac {\beta_ {q}}{4} + \frac {\beta_ {t}}{4} \left(1 - 3 s _ {\theta} ^ {2}\right) ^ {2} + \epsilon s _ {\theta} ^ {2}, \quad \left(\lambda_ {\eta}\right) ^ {\mathrm {I R}} = 2 \beta_ {q}, \tag {3.35}
$$

$$
\left(\lambda_ {h \eta}\right) ^ {\mathrm {I R}} = \frac {\beta_ {q}}{2} - \frac {1 - 3 s _ {\theta} ^ {2}}{4} \epsilon .
$$

The five basic integrals the same as eq. (3.18). The  $(\mu_{\eta}^{2})^{\mathrm{IR}}$  and  $(\lambda_{\eta})^{\mathrm{IR}}$  are independent of  $\alpha_{t}$  and  $\beta_{t}$  because the embedding  $t_R^{15}$  conserves  $\mathrm{U}(1)_\eta$ . It is apparent that eq. (3.35) cannot trigger SFOEWPT, because it gives a  $\eta$ -direction local minimum  $w^{2}|_{\mathrm{IR}} = 2\alpha_{q} / \beta_{q} \gg f^{2}$ .

The UV contributions. The spurions for  $\mathcal{T}^{15}$  is

$$
\left(t _ {R} ^ {\mathbf {1 5}}\right) _ {I J} = \left(\mathcal {T} ^ {\mathbf {1 5}}\right) _ {I J} t _ {R}, \quad \mathcal {T} ^ {\mathbf {1 5}}: \left(\mathbf {1 5} _ {2 / 3}, \mathbf {1} _ {- 2 / 3}\right), \tag {3.36}
$$

under the extended  $\mathrm{SO}(6)\times \mathrm{U}(1)_X\times \mathrm{SU}(2)_0\times \mathrm{U}(1)_0$  group.  $\langle \mathcal{T}^{15}\rangle$  can be inferred from eq. (2.17) thus not shown here. The relevant operators are

$$
c _ {f} ^ {R} \left| y _ {R} \right| ^ {2} f ^ {4} \Sigma^ {\dagger} \mathcal {T} ^ {\mathbf {1 5}} \mathcal {T} ^ {\mathbf {1 5} \dagger} \Sigma , \quad \frac {d _ {f} ^ {R}}{1 6 \pi^ {2}} \left| y _ {R} \right| ^ {2} f ^ {4} \left(\Sigma^ {\dagger} \mathcal {T} ^ {\mathbf {1 5}} \mathcal {T} ^ {\mathbf {1 5} \dagger} \Sigma\right) ^ {2}, \tag {3.37}
$$

with  $c_f^R$  and  $d_f^R$  being  $\mathcal{O}(1)$  parameters. The UV contribution to the scalar potential is

$$
(\mu_ {f} ^ {2}) ^ {\mathrm {U V}} = \frac {c _ {f} ^ {L}}{2} | y _ {L} | ^ {2} f ^ {2} + \frac {c _ {f} ^ {R}}{2} | y _ {R} | ^ {2} f ^ {2} (1 - 3 s _ {\theta} ^ {2}) + \frac {d _ {f} ^ {R}}{3 2 \pi^ {2}} | y _ {R} | ^ {4} f ^ {2} s _ {\theta} ^ {2} (1 - 3 s _ {\theta} ^ {2}),
$$

$$
\left(\mu_ {\eta} ^ {2}\right) ^ {\mathrm {U V}} = 2 c _ {f} ^ {L} \left| y _ {L} \right| ^ {2} f ^ {2},
$$

$$
\left(\lambda_ {f}\right) ^ {\mathrm {U V}} = \frac {d _ {f} ^ {L}}{6 4 \pi^ {2}} \left| y _ {L} \right| ^ {4} + \frac {d _ {f} ^ {R}}{6 4 \pi^ {2}} \left| y _ {R} \right| ^ {4} \left(1 - 3 s _ {\theta} ^ {2}\right) ^ {2}, \tag {3.38}
$$

$$
(\lambda_ {\eta}) ^ {\mathrm {U V}} = \frac {d _ {f} ^ {L}}{4 \pi^ {2}} | y _ {L} | ^ {4}, (\lambda_ {h \eta}) ^ {\mathrm {U V}} = \frac {d _ {f} ^ {L}}{1 6 \pi^ {2}} | y _ {L} | ^ {4}.
$$

They can help to reduce  $w^2$  and match the requirement of SFOEWPT.

# 4 Realizing SFOEWPT in the  $6 + 6$  NMCHM

In last section, we have seen the necessary conditions of SFOEWPT are not satisfied by the IR contributions alone, for all benchmark models we considered. However, we also showed that with the help of the UV contributions, SFOEWPT may exist in the  $6 + 6$ ,  $15 + 6$  and  $15 + 15$  models. In this section, we take the  $6 + 6$  NMCHM as an example to investigate the SFOEWPT under the combination of the IR and UV contributions.

# 4.1 Calculating the IR contributions with Weinberg sum rules

The UV contributions to  $V(h,\eta)$  of the  $6 + 6$  model have been given in eqs. (3.13) and (3.25), while the IR contributions are expressed as the integrals of the form factors in eqs. (3.8) and (3.19). For a QCD-like strong dynamics, the form factors can be written explicitly and the integrals can be evaluated with the help of suitable sum rules.

Gauge contributions. The  $\Pi_{0,1}(p^2)$  are expressed by the strong couplings and vector resonances masses [38]

$$
\Pi_ {0} (p ^ {2}) = g _ {0} ^ {2} p ^ {2} \sum_ {n = 1} ^ {N _ {\rho}} \frac {f _ {\rho (n)} ^ {2}}{p ^ {2} - M _ {\rho (n)} ^ {2}},
$$

$$
\Pi_ {1} \left(p ^ {2}\right) = g _ {0} ^ {2} f ^ {2} + 2 g _ {0} ^ {2} p ^ {2} \left(\sum_ {n = 1} ^ {N _ {a}} \frac {f _ {a (n)} ^ {2}}{p ^ {2} - M _ {a (n)} ^ {2}} - \sum_ {n = 1} ^ {N _ {\rho}} \frac {f _ {\rho (n)} ^ {2}}{p ^ {2} - M _ {\rho (n)} ^ {2}}\right), \tag {4.1}
$$

where  $f_{\rho(n)} \equiv M_{\rho(n)} / g_{\rho(n)}$ . Then in eq. (3.6), the kinetic terms of  $B$  and  $W$  fields are modified into

$$
- \frac {p ^ {2}}{2} P _ {T} ^ {\mu \nu} \left(1 + \sum_ {n = 1} ^ {N _ {\rho}} \frac {g _ {0} ^ {\prime 2}}{g _ {\rho (n)} ^ {2}}\right) B _ {\mu} B _ {\nu}, - \frac {p ^ {2}}{2} P _ {T} ^ {\mu \nu} \left(1 + \sum_ {n = 1} ^ {N _ {\rho}} \frac {g _ {0} ^ {2}}{g _ {\rho (n)} ^ {2}}\right) W _ {\mu} ^ {a} W _ {\nu} ^ {a}. \tag {4.2}
$$

A field redefinition is needed to get the canonical kinetic terms, i.e.  $W_{\mu}^{a}\rightarrow (g / g_{0})W_{\mu}^{a}$  and  $B_{\mu}\to (g^{\prime} / g_{0}^{\prime})B_{\mu}$ , where

$$
g ^ {2} = g _ {0} ^ {2} \left(1 + \sum_ {n = 1} ^ {N _ {\rho}} \frac {g _ {0} ^ {2}}{g _ {\rho (n)} ^ {2}}\right) ^ {- 1}, \quad g ^ {2} = g _ {0} ^ {\prime 2} \left(1 + \sum_ {n = 1} ^ {N _ {\rho}} \frac {g _ {0} ^ {\prime 2}}{g _ {\rho (n)} ^ {2}}\right) ^ {- 1}, \tag {4.3}
$$

are the physical gauge couplings. After this redefinition, the  $g_0^{(t)}$  in  $\Pi_{0,1}$  can be replaced by  $g^{(t)}$ .

As mentioned in previous section, the convergent IR contributions require a scaling  $\Pi_1\sim Q^{-4}$ . By expanding the second line in eq. (4.1), we find that means the following two equations,

$$
\sum_ {n = 1} ^ {N _ {\rho}} f _ {\rho (n)} ^ {2} = \frac {f ^ {2}}{2} + \sum_ {n = 1} ^ {N _ {a}} f _ {a (n)} ^ {2}; \quad \sum_ {n = 1} ^ {N _ {\rho}} f _ {\rho (n)} ^ {2} M _ {\rho (n)} ^ {2} = \sum_ {n = 1} ^ {N _ {a}} f _ {a (n)} ^ {2} M _ {a (n)} ^ {2}, \tag {4.4}
$$

known as the Weinberg first and second sum rules, which are first proposed in the study of QCD  $\rho$ -mesons [71]. If we further assume the lightest resonances dominate, i.e.  $N_{\rho} = N_{a} = 1$ , then the sum rules become

$$
f _ {\rho} ^ {2} = \frac {f ^ {2}}{2} + f _ {a} ^ {2}, \quad f _ {\rho} ^ {2} M _ {\rho} ^ {2} = f _ {a} ^ {2} M _ {a} ^ {2}. \tag {4.5}
$$

Note that above equation implies  $M_{a} > M_{\rho}$ . In such a case, the form factors become

$$
\Pi_ {0} (Q ^ {2}) = g ^ {2} Q ^ {2} \frac {f _ {\rho} ^ {2}}{Q ^ {2} + M _ {\rho} ^ {2}}, \quad \Pi_ {1} (Q ^ {2}) = \frac {g ^ {2} f ^ {2} M _ {\rho} ^ {2} M _ {a} ^ {2}}{(Q ^ {2} + M _ {\rho} ^ {2}) (Q ^ {2} + M _ {a} ^ {2})}, \tag {4.6}
$$

and eq. (3.8) can be calculated analytically. If we impose  $\Pi_{B,W} \approx Q^2$  (the error of this approximation is  $\mathcal{O}(g^2 / g_\rho^2)$ , small enough to neglect), the results are quite simple

$$
(\mu_ {g} ^ {2}) ^ {\mathrm {I R}} = \frac {3 (3 g ^ {2} + {g ^ {\prime}} ^ {2})}{6 4 \pi^ {2}} \frac {M _ {\rho} ^ {2} M _ {a} ^ {2}}{M _ {a} ^ {2} - M _ {\rho} ^ {2}} \ln \frac {M _ {a} ^ {2}}{M _ {\rho} ^ {2}},
$$

$$
\left(\lambda_ {g}\right) ^ {\mathrm {I R}} = \frac {3 \left[ 2 g ^ {4} + \left(g ^ {2} + g ^ {\prime 2}\right) ^ {2} \right]}{2 5 6 \pi^ {2} \left(M _ {a} ^ {2} - M _ {\rho} ^ {2}\right) ^ {2}} \left[ M _ {a} ^ {4} + \frac {M _ {\rho} ^ {4} \left(M _ {\rho} ^ {2} - 3 M _ {a} ^ {2}\right)}{M _ {a} ^ {2} - M _ {\rho} ^ {2}} \ln \frac {M _ {a} ^ {2}}{M _ {W} ^ {2}} + (a \leftrightarrow \rho) \right]. \tag {4.7}
$$

We have used a cutoff  $Q^2 = M_W^2$  to regularize the IR divergence of  $(\lambda_g)^{\mathrm{IR}}$ . Note that  $(\mu_g^2)^{\mathrm{IR}}$  is positive definite. Comparing eqs. (4.7) and (3.13), one can see  $(\mu_g^2)^{\mathrm{UV}} \gtrsim (\mu_g^2)^{\mathrm{IR}}$  because  $g_{\rho} \lesssim 4\pi$ ; while  $(\lambda_g)^{\mathrm{UV}} \sim (\lambda_g)^{\mathrm{IR}}$ . Thus in general the UV contribution is not negligible.

Fermion contributions. The fermion form factors  $\Pi_{0,1}^{q,t}(p^2)$  and  $M_{0,1}^{t}(p^{2})$  are expressed in terms of the resonances masses and coupling constants,

$$
\Pi_ {0} ^ {q, t} (p ^ {2}) = 1 - \sum_ {n = 1} ^ {N _ {\mathbf {5}}} \frac {| y _ {L , R} ^ {\mathbf {5} (n)} | ^ {2} f ^ {2}}{p ^ {2} - M _ {\mathbf {5} (n)} ^ {2}}, \quad \Pi_ {1} ^ {q, t} (p ^ {2}) = \sum_ {n = 1} ^ {N _ {\mathbf {5}}} \frac {| y _ {L , R} ^ {\mathbf {5} (n)} | ^ {2} f ^ {2}}{p ^ {2} - M _ {\mathbf {5} (n)} ^ {2}} - \sum_ {n = 1} ^ {N _ {\mathbf {1}}} \frac {| y _ {L , R} ^ {\mathbf {1} (n)} | ^ {2} f ^ {2}}{p ^ {2} - M _ {\mathbf {1} (n)} ^ {2}}, \tag {4.8}
$$

and

$$
M _ {0} ^ {t} \left(p ^ {2}\right) = - \sum_ {n = 1} ^ {N _ {5}} \frac {y _ {L} ^ {\mathbf {5} (n)} \left(y _ {R} ^ {\mathbf {5} (n)}\right) ^ {*} f ^ {2} M _ {\mathbf {5} (n)}}{p ^ {2} - M _ {\mathbf {5} (n)} ^ {2}}, \tag {4.9}
$$

$$
M _ {1} ^ {t} (p ^ {2}) = \sum_ {n = 1} ^ {N _ {\mathbf {5}}} \frac {y _ {L} ^ {\mathbf {5} (n)} (y _ {R} ^ {\mathbf {5} (n)}) ^ {*} f ^ {2} M _ {\mathbf {5} (n)}}{p ^ {2} - M _ {\mathbf {5} (n)} ^ {2}} - \sum_ {n = 1} ^ {N _ {\mathbf {1}}} \frac {y _ {L} ^ {\mathbf {1} (n)} (y _ {R} ^ {\mathbf {1} (n)}) ^ {*} f ^ {2} M _ {\mathbf {1} (n)}}{p ^ {2} - M _ {\mathbf {1} (n)} ^ {2}}.
$$

Defining  $Q^2 = -p^2$ , now the IR-driven coefficients eq. (3.19) can be evaluated. To converge the integrals, the following scaling is needed,

$$
\Pi_ {1} ^ {q, t} \sim \frac {1}{Q ^ {6}}, \quad M _ {1} ^ {t} \sim \frac {1}{Q ^ {2}}. \tag {4.10}
$$

While the second scaling is already satisfied, the first one requires two sets of sum rules

$$
\sum_ {n = 1} ^ {N _ {\mathbf {5}}} \left| y _ {L, R} ^ {\mathbf {5} (n)} \right| ^ {2} = \sum_ {n = 1} ^ {N _ {\mathbf {1}}} \left| y _ {L, R} ^ {\mathbf {1} (n)} \right| ^ {2}, \quad \sum_ {n = 1} ^ {N _ {\mathbf {5}}} \left| y _ {L, R} ^ {\mathbf {5} (n)} \right| ^ {2} M _ {\mathbf {5} (n)} ^ {2} = \sum_ {n = 1} ^ {N _ {\mathbf {1}}} \left| y _ {L, R} ^ {\mathbf {1} (n)} \right| ^ {2} M _ {\mathbf {1} (n)} ^ {2}. \tag {4.11}
$$

Assuming the lightest resonances dominate, we consider the particle spectrum  $N_{5} = 1$  and  $N_{1} = 2$ . In this case eq. (4.11) reduces to

$$
\left| y _ {L, R} ^ {\mathbf {5}} \right| ^ {2} = \left| y _ {L, R} ^ {\mathbf {1}} \right| ^ {2} + \left| y _ {L, R} ^ {\mathbf {1} ^ {\prime}} \right| ^ {2}, \quad \left| y _ {L, R} ^ {\mathbf {5}} \right| ^ {2} M _ {\mathbf {5}} ^ {2} = \left| y _ {L, R} ^ {\mathbf {1}} \right| ^ {2} M _ {\mathbf {1}} ^ {2} + \left| y _ {L, R} ^ {\mathbf {1} ^ {\prime}} \right| ^ {2} M _ {\mathbf {1} ^ {\prime}} ^ {2}, \tag {4.12}
$$

where the heavier singlet top partner is denoted as  $\Psi_{\mathbf{1}'}$ . The form factors are then

$$
\Pi_ {0} ^ {q, t} (Q ^ {2}) = 1 + \frac {\left| y _ {L , R} ^ {\bar {5}} \right| ^ {2} f ^ {2}}{Q ^ {2} + M _ {\mathbf {5}} ^ {2}}, \quad \Pi_ {1} ^ {q, t} (Q ^ {2}) = \frac {\left| y _ {L , R} ^ {1 ^ {\prime}} \right| ^ {2} f ^ {2} \left(M _ {\mathbf {1} ^ {\prime}} ^ {2} - M _ {\mathbf {5}} ^ {2}\right) \left(M _ {\mathbf {1} ^ {\prime}} ^ {2} - M _ {\mathbf {1}} ^ {2}\right)}{\left(Q ^ {2} + M _ {\mathbf {5}} ^ {2}\right) \left(Q ^ {2} + M _ {\mathbf {1}} ^ {2}\right) \left(Q ^ {2} + M _ {\mathbf {1} ^ {\prime}} ^ {2}\right)}, \tag {4.13}
$$

and

$$
M _ {1} ^ {t} \left(Q ^ {2}\right) = \frac {y _ {L} ^ {1} \left(y _ {R} ^ {1}\right) ^ {*} f ^ {2} M _ {\mathbf {1}}}{Q ^ {2} + M _ {\mathbf {1}} ^ {2}} + \frac {y _ {L} ^ {1 ^ {\prime}} \left(y _ {R} ^ {1 ^ {\prime}}\right) ^ {*} f ^ {2} M _ {\mathbf {1} ^ {\prime}}}{Q ^ {2} + M _ {\mathbf {1} ^ {\prime}} ^ {2}} - \frac {y _ {L} ^ {\mathbf {5}} \left(y _ {R} ^ {\mathbf {5}}\right) ^ {*} f ^ {2} M _ {\mathbf {5}}}{Q ^ {2} + M _ {\mathbf {5}} ^ {2}}. \tag {4.14}
$$

Table 2. The contributions to the scalar potential in the  $6 + 6$  NMCHM. Note that this table is a realization of table 1.  

<table><tr><td>6 + 6</td><td>Gauge-induced</td><td>Fermion-induced</td></tr><tr><td>IR</td><td>Π0(Q2) = g2Q2fρ2/Q2+ Mρ2, Π1(Q2) = g2f2Mρ2Ma2/(Q2+ Mρ2)(Q2+ Ma2)</td><td>Π0q,t(Q2) = 1 + |yL,R|2f2/Q2+ M2,Π1q,t(Q2) = |yL,R&#x27;|2f2(M12&#x27;-M2)(M12&#x27;-M2),M1t(Q2) = yL1(yR)*f2M1/Q2+ M12&#x27; + yL1&#x27;(yR)&#x27;f2M1&#x27; / Q2+ M12&#x27; - yL5(yR)*f2M5/Q2+ M5</td></tr><tr><td>UV</td><td>cg4Σ†GgAσ, dg/16π2f4(Σ†GgAσ)2, cg&#x27;4Σ†G&#x27;G&#x27;σ, dg&#x27;/16π2f4(Σ†G&#x27;G&#x27;σ)2</td><td>cf|yL|2f4Σ†Q6Q6†Σ, df/16π2|yL|4f4(Σ†Q6Q6†Σ)2,cf|RyR|2f4Σ†T6T6†Σ, df/16π2|yR|4f4(Σ†T6T6†Σ)2</td></tr></table>

The mass of top quark can be read as

$$
M _ {t} = \frac {v \left| s _ {\theta} \right|}{\sqrt {2}} \frac {M _ {\mathbf {5}}}{\sqrt {M _ {\mathbf {5}} ^ {2} + \left| y _ {L} ^ {\mathbf {5}} \right| ^ {2} f ^ {2}}} \frac {M _ {\mathbf {5}}}{\sqrt {M _ {\mathbf {5}} ^ {2} + \left| y _ {R} ^ {\mathbf {5}} \right| ^ {2} f ^ {2}}} \left| \frac {y _ {L} ^ {\mathbf {1}} y _ {R} ^ {\mathbf {1} *} f}{M _ {\mathbf {1}}} + \frac {y _ {L} ^ {\mathbf {1} ^ {\prime}} y _ {R} ^ {\mathbf {1} ^ {\prime} *} f}{M _ {\mathbf {1} ^ {\prime}}} - \frac {y _ {L} ^ {\mathbf {5}} y _ {R} ^ {\mathbf {5} *} f}{M _ {\mathbf {5}}} \right| \sqrt {1 - \frac {v ^ {2}}{f ^ {2}}}, \tag {4.15}
$$

while the bottom quark remains massless. A mass hierarchy  $M_{\mathbf{1}'} > M_{\mathbf{5}} > M_{\mathbf{1}}$  can be derived from eq. (4.12).

Given eq. (4.7), eqs. (4.13) and (4.14), the quantitative connection between the IR contributions and resonances masses and couplings are known and the numerical study is in order.[11]

# 4.2 SFOEWPT and gravitational waves

The sources of  $V(h,\eta)$  are summarized in table 2. Combining the IR and UV parts of  $\mu_{h,\eta}^2$  and  $\lambda_{h,\eta,h\eta}$ , we use the MultiNest package [72] to find the allowed parameter space by the SM mass spectrum and the conditions for SFOEWPT. For the IR parts, the variables we use in scan are

$$
\left\{M _ {\rho}, M _ {a}, f, M _ {1}, M _ {5}, M _ {1 ^ {\prime}}, y _ {L} ^ {5}, y _ {R} ^ {5}, \theta \right\}, \tag {4.16}
$$

while  $g_{\rho, a}$  and  $y_{L,R}^{1,1'}$  are derived via the sum rules. The mass ranges are  $2 \sim 7 \mathrm{TeV}$  for the vector resonances and  $1 \sim 6 \mathrm{TeV}$  for the fermion resonances, while  $f > 0.5 \mathrm{TeV}$ . For the fermion interactions, all the mixing couplings  $\left|y_{L,R}^{5,1,1'}\right|$  are constrained within 5. For the UV parts, we consider only the fermion-induced operators  $c_f^{L,R}$  and  $d_f^{L,R}$ , requiring the absolute values of the Wilson coefficients to be smaller than 5. The range of mixing angle in embedding  $t_R^6$  is  $|\theta| \in [0, \pi/2]$ , where the upper limit is due to the fact that  $\theta$  exist only as  $s_\theta^2$  thus  $(\pi - \theta)$  is equivalent to  $\theta$ . To satisfy the EW and Higgs measurements, we require the derived  $M_h = 125.09 \mathrm{GeV}$  [67],  $M_Z = 91.1876 \mathrm{GeV}$  [73], and the top mass  $M_t = 172.9 \pm 0.4 \mathrm{GeV}$  [74]. To really achieve a SFOEWPT, the bubble nucleation condition eq. (2.35) should be satisfied, i.e. there should exist a nucleation temperature  $T_n$  giving

![](images/9bb120a72853bd52597972dc904eb5f8ec5fc0c4eb33b48f25750ed6d7f1c4e5.jpg)  
Figure 2. Left: the projections for the parameter points on the  $M_{\eta} - f$  plane. All the points can reproduce SM mass spectrum and give degenerate vacuums at critical temperature  $T_{c}$ , while only the red points give SFOEWPT. Right: the  $T_{n} - T_{c}$  values for the points with successful SFOEWPT.

![](images/93a3cc26f1aa62886dbd522cf3095b30a08b3cb9bddf0e8952ffa7f6ab3b0dd2.jpg)

$S_{3}(T_{n}) / T_{n} \sim 140$ . Numerically, we use the CosmoTransitions [75] package to derive the  $O(3)$ -symmetric classical bounce solution for  $V_{T}(h,\eta)$  and get  $S_{3}(T)$ , and then solve  $T_{n}$ . The allowed parameter points distribute almost uniformly in the  $M_{\rho,a}$  and  $M_{5,1,1^{\prime}}$  regions we set. We also verify that the for  $\mu_{h,\eta}^{2}$  and  $\lambda_{h,h\eta}$ , the IR and UV contributions are comparable; while for  $\lambda_{\eta}$  the UV contributions dominate. The allowed  $|\theta|$  lies in  $1.0 \lesssim |\theta| \lesssim \pi/2$ , thus a dark matter scenario for  $\eta$  (corresponding to  $\theta = \pi/2$ ) is still possible. However, as pointed out in ref. [28], under the requirement of SFOEWPT, such a singlet can only contribute a subdominant component after taking into account the direct search bounds.

In figure 2, we project the surviving parameter points into the  $f - M_{\eta}$  and  $T_{n} - T_{c}$  planes. In the left panel, all points in the figure reproduce the SM particle spectrum and give degenerate vacuums, while only the red points can trigger SFOEWPT. The mass of  $\eta$  is around  $100\mathrm{GeV}$  and the decay constant  $f \gtrsim 1\mathrm{TeV}$ . The right panel of figure 2 shows the critical temperatures  $T_{c}$  and the nucleation temperatures  $T_{n}$  for the parameter points with successful nucleation. One can find  $T_{n} \sim 120\mathrm{GeV}$  and  $T_{n} \lesssim T_{c}$  as expected.

SFOEWPT can produce gravitational waves (GWs) in the early universe. After the cosmological redshift, the peak of GW frequencies are typically mille-Hz [76], in the sensitive region of a broad class of GW detectors, such as LISA [20], Tianqin [21], Taiji [22], BBO [23] or DECIGO (Ultimate DECIGO) [24, 25]. As is pointed out in ref. [76], the GWs from SFOEWPT can be reduced into a two-parameter problem. The first crucial parameter is  $\alpha$ , defined by the ratio of the phase transition latent heat to the radiative energy density of the universe in the SFOEWPT period,

$$
\alpha = \frac {\epsilon}{\rho_ {\mathrm {r a d}}}, \quad \epsilon = - \Delta V _ {T} + T _ {n} \Delta \frac {\partial V _ {T}}{\partial T} \bigg | _ {T _ {n}}, \quad \rho_ {\mathrm {r a d}} = \frac {\pi^ {2}}{3 0} g _ {*} T _ {n} ^ {4}, \qquad (4. 1 7)
$$

where  $v_{n}$  and  $g_{*}$  are respectively the Higgs VEV and the relativistic degrees of freedom at  $T_{n}$ , and “ $\Delta$ ” denotes the difference between the EW broken and symmetric phases. The

second key parameter is  $\beta / H_{n}$ , with  $\beta^{-1}$  being the time duration of SFOEWPT, and  $H_{n}$  the Hubble constant when SFOEWPT completed,

$$
\beta = \frac {d}{d t} \left(\frac {S _ {3}}{T}\right) \Big | _ {t = t _ {n}}, \quad \frac {\beta}{H _ {n}} = T _ {n} \frac {d}{d T} \left(\frac {S _ {3}}{T}\right) \Big | _ {T = T _ {n}}, \tag {4.18}
$$

where  $t_n$  is the cosmic time at  $T_n$ . The smaller  $\beta / H_n$  is, the stronger the phase transition is. The signal strength of GWs is described by

$$
\Omega_ {\mathrm {G W}} (f) = \frac {1}{\rho_ {c}} \frac {d \rho_ {\mathrm {G W}}}{d \ln f}, \tag {4.19}
$$

where  $\rho_{c}$  stands for the critical energy density of the universe today. There are three sources of the phase transition GWs: bubble collision, sound waves in the fluid, and the turbulence in plasma. They are all expressed as numerical formulae in terms of  $\alpha$  and  $\beta / H_{n}$  in ref. [77]. In our scenario, the velocity of the expanding bubble wall is given by the detonation wave formula [78]

$$
v _ {\mathrm {w}} = \frac {1}{1 + \alpha} \left(\frac {1}{\sqrt {3}} + \sqrt {\alpha^ {2} + \frac {2}{3} \alpha}\right), \tag {4.20}
$$

and the dominant source of GWs comes from sound waves, while the turbulence is subdominant and the bubble collision contribution is negligible [77].<sup>12</sup>

For our study, the relativistic degrees of freedom during SFOEWPT is  $g_{*} = 106.75 + 1$ , i.e the number of SM plus one real singlet. For the data points with successful nucleation in  $\mathbf{6} + \mathbf{6}$  NMCHM, we calculate  $\alpha$  and  $\beta / H_{n}$  with CosmoTransitions and a homemade codes plugin. The obtained values of  $\alpha$  and  $\beta / H_{n}$  are projected in the left panel of figure 3. Using the formulae in [77] we are able to calculate the GW signal strengths. The results are presented in the right panel of figure 3, where some typical signal curves are plotted in thin black lines while the envelope of all allowed data points are plotted in a thick black line. One can clearly see that GW signals are testable for most future detectors.

# 4.3 Collider phenomenology

The NMCHM is rather predictive and they have very rich phenomenology at the LHC. On one hand, the deviations of the Higgs couplings or oblique parameters can be probed in the EW and Higgs precision measurements [51, 80, 81]; on the other hand, the composite resonances can be directly discovered [80, 81]. While no excess is obtained, the experiments have been putting stronger and stronger constrains on the model.

The discovery of composite resonances would be the smoking gun of the CHMs. In NMCHM, the vector mass terms in eq. (2.8) induce EFT operators

$$
\mathcal {L} _ {\rho} \supset \frac {M _ {\rho} ^ {2}}{2 g _ {\rho} ^ {2}} \left[ \left(g _ {\rho} \rho_ {L \mu} ^ {a} - g _ {0} W _ {\mu} ^ {a} + \frac {i}{2 f ^ {2}} H ^ {\dagger} \sigma^ {a} \stackrelleftrightarrow {\leftrightarrow} D _ {\mu} H\right) ^ {2} + \left(g _ {\rho} \rho_ {R \mu} ^ {3} - g _ {0} ^ {\prime} B _ {\mu} + \frac {i}{2 f ^ {2}} H ^ {\dagger} \stackrelleftrightarrow {\leftrightarrow} D _ {\mu} H\right) ^ {2} \right], (4. 2 1)
$$

![](images/3c3e90be227e6ff7e8f478f78d89222cddf9c919b97f1f05a89aa90c6a88f923.jpg)  
Figure 3. Left: the  $\alpha$  and  $\beta / H_{n}$  distribution for the parameter points with SFOEWPT. Right: the GW signals, where the thin black lines are typical GW curves from the data points of the left panel, while the thick black line represents the envelope of all data points.

![](images/e551743b6c8fdf1b6e119d892a07c2777a0d2a66886f7b422fbb8ffd6410b8ae.jpg)

implying the mixings  $\rho_L^a - W^a$  and  $\rho_R^3 - B$  before EWSB, and the mixing angles are  $\approx g / g_{\rho}$  and  $g' / g_{\rho}$  respectively. As a result, the  $\rho_L^{\pm,0}$  and  $\rho_R^3 (= \rho_R^0)$  interact with light quarks with couplings  $\approx g^2 / g_{\rho}$  and  $g'^2 / g_{\rho}$  respectively and can be produced via Drell-Yan process at the LHC and then decay to the SM di-boson channels ( $W^{\pm}Z / W^{\pm}h$  and  $W^{+}W^{-} / Zh$ ). Other vector resonances such as  $\rho_R^{\pm}$ ,  $\rho_D^{\pm,0,0*}$ ,  $a_D^{\pm,0,0*}$  and  $a_S^0$  interact with quark partons only after EWSB thus the couplings are suppressed by  $v^2 / f^2$ . Therefore, it is hard to probe them via the quark-antiquark fusion at the LHC. The  $\rho_R^{\pm}$  may be produced via vector boson fusion as well, however the cross section is tiny due to the phase space suppression. In summary, the most hopeful channel to probe the vector resonances of NMCHM is the Drell-Yan produced  $\rho_L^{\pm,0}$  and  $\rho_R^0$ . The dominant decay channels of  $\rho_L^{\pm,0}$  and  $\rho_R^0$  depend on the relation between the masses of vector and fermion resonances [82].<sup>13</sup> In the region  $M_{\rho} < M_{5}$ , the SM di-boson channels dominate. While if  $M_5 < M_{\rho} < 2M_5$ , the "heavy-light" decay modes with  $t / b$  plus a top partner (such as  $t\bar{\Psi}_{5}$ ) kinematically open and acquire considerable branching ratios. Although di-boson channels are sub-leading here, they play an important role in phenomenology because of the accurate measurement at the LHC, see below. Finally, if  $M_{\rho} > 2M_{5}$ , the decay modes  $\rho_L^{\pm,0}$ ,  $\rho_R^0 \to \Psi_5\bar{\Psi}_5$  (so-called "heavy-heavy" channels) induced by the interactions in the strong sector

$$
\mathcal {L} _ {\rho \Psi} = c _ {\rho} \bar {\Psi} _ {\mathfrak {5}} \gamma^ {\mu} t ^ {\bar {A}} \Psi_ {\mathfrak {5}} \left(g _ {\rho} \rho_ {\mu} ^ {\bar {A}} - e _ {\mu} ^ {\bar {A}}\right), \quad c _ {\rho} \sim \mathcal {O} (1), \tag {4.22}
$$

contribute almost  $100\%$  branching ratio because of the large  $g_{\rho}$ .

For the  $6 + 6$  NMCHM, we found that almost all parameter points yielding SFOEWPT lie in the mass region  $M_{\rho} > M_{5}$ , as shown in figure 4. By recasting ref. [83] we find most

![](images/ee56b5e4cd3a0594af4325a5ea36751b225c9d0e070ebc4a703fe5aefa403c3d.jpg)  
Figure 4. The collider phenomenology of the parameter points with SFOEWPT. The SM di-boson bound comes from ref. [83], while the  $X_{5/3}\bar{X}_{5/3}$  bound is taken from ref. [84].

points in region  $M_{\mathbf{1}} < M_{\rho} < 2M_{\mathbf{5}}$  have been excluded by the SM di-boson searches of ATLAS at  $139\mathrm{fb^{-1}}$ , see the red points in figure 4. For the region  $M_{\rho} > 2M_{\mathbf{5}}$ , the bound is weak that a  $\rho$ -resonances of  $\sim 3\mathrm{TeV}$  is still allowed. That is because a dedicated search for the heavy-heavy channels is still lacking (see ref. [85] for a summary of the performed searches after LHC Run II). As in this region the  $\rho$ -resonances are typically rather broad that  $\Gamma_{\rho} / M_{\rho}$  can reach  $\sim 50\%$ , the search is more challenging. In this case, the same-sign lepton final state which doesn't require the reconstruction of a resonant peak may be useful to hunt the signal. The studies in refs. [82, 86, 87] show that for

$$
p p \rightarrow \rho_ {L} ^ {\pm} \rightarrow X _ {5 / 3} \bar {X} _ {2 / 3} + \text {c . c .} \rightarrow \ell^ {\pm} \ell^ {\pm} + \text {j e t s}, \tag {4.23}
$$

the HL-LHC can reach a region of  $M_{\rho} \gtrsim 4.5 \mathrm{TeV}$  for a  $g_{\rho} \sim 2$ , 3.

At the LHC, the top partners can be either pair produced via QCD or singly produced via EW interactions. The QCD production is model-independent but suffers from the double-suppression in phase space; while the EW production can probe higher mass scale but depends on the details of the fermion embedding. For the  $6 + 6$  NMCHM, matching eq. (2.19) to SM EFT yields

$$
\mathcal {L} _ {\mathbf {6} + \mathbf {6}} \supset - s _ {\theta} y _ {R} ^ {\mathbf {5}} \left[ \bar {t} _ {R} \left(H ^ {\dagger} Q _ {X} - \widetilde {H} ^ {\dagger} Q\right) + \bar {t} _ {R} \widetilde {T} \pi_ {5} \right] - y _ {L} ^ {\mathbf {1}} \bar {q} _ {L} \widetilde {H} T _ {S} - i c _ {\theta} y _ {R} ^ {\mathbf {1}} \bar {t} _ {R} T _ {S} \pi_ {5}. \tag {4.24}
$$

According to the Goldstone equivalence theorem, the decay channels of the top partners are

$$
X _ {5 / 3} \rightarrow t W ^ {+}, \quad X _ {2 / 3}, T \rightarrow t Z, t h, \quad B \rightarrow t W ^ {-}, \quad \tilde {T}, T _ {S} \rightarrow b W ^ {+}, t Z, t h, t \eta . \tag {4.25}
$$

The EW fusion production mechanism can also be read, e.g.  $tW \rightarrow X_{5/3}$ . Except for the  $T, T_S \rightarrow t\eta$  channel, the phenomenology of top partners in the  $6 + 6$  NMCHM is quite similar to the case of the  $5 + 5$  MCHM and we refer the readers to the relevant study in [82] and

the references therein. A search based on the CMS  $35.9\mathrm{fb}^{-1}$  data in the  $X_{5/3}\bar{X}_{5/3}$  channel sets a bound  $M_5 \geqslant 1.32\mathrm{TeV}$ , assuming  $\mathrm{Br}(X_{5/3} \rightarrow tW^{+}) = 100\%$  [84]. We plot this bound into figure 4 as the blue shadow region. Note that for a NMCHM based on the bottom-up model building of a specific underlying theory, there may exist extra scalars which are not described in our top-down CCWZ approach. For instance, the NMCHM based on coset  $\mathrm{SU}(4)/\mathrm{Sp}(4)$  and gauge group  $\mathrm{Sp}(2N_{\mathrm{HC}})$  (where  $N_{\mathrm{HC}}$  is the number of the "hyper-color" in the strong sector) contains a real color octet  $\pi_8$ , a complex color sextet  $\pi_6$ , and two real gauge singlets  $\sigma$  and  $\sigma_c$  [88, 89]. Some of those extra particles are expected to be light and may be decayed from the top partners [90, 91], which would even make the bounds weaker because there are no specific searches for those channels yet. A recent study shows that in the same-sign lepton channel, the results from the search for pair-produced  $X_{5/3} \rightarrow tW^{+}$  are robust as well for many other exotic decays such as  $X_{5/3} \rightarrow \bar{b}\pi_6$ , and the HL-LHC can reach a mass of  $M_5 \sim 1.6\mathrm{TeV}$  [92]. Another fresh paper [93] gives the result for the decay  $T \rightarrow t\sigma$ . For other non-standard decay channels, more detailed studies are still needed.

In short, we've found a lot of parameter points with SFOEWPT in the range  $M_{\rho,a} \in [2,7]$  TeV and  $M_{5,1,1'} \in [1,6]$  TeV, and a considerable fraction of them lie in  $M_{\rho} > 2M_{5}$ , a region that has been constrained very weakly so far. In this case, current bounds for the vector and fermion resonances are  $\sim 3$  TeV and  $\sim 1.3$  TeV respectively. Therefore, there is plenty of rooms for future LHC experiments to explore this scenario. The excess at the collider can be a good crosscheck of the signals from the GW detectors.

# 5 Conclusion

In this article, we study the SFOEWPT scenario in the NMCHM. Within the framework of gauge-invariant thermal corrections to the scalar potential, the SFOEWPT is realized via a two-step phase transition. We have considered various fermion embeddings: for the left-handed doublet  $q_{L} = (t_{L},b_{L})^{T}$ , we consider 6 or 15; while for the right-handed  $t_{R}$ , we consider 1, 6 and 15. Among the six different combinations, the  $15 + 1$  model fails to give a massive top quark, while the  $6 + 1$  and  $6 + 15$  models are unable to generate a potential for the singlet  $\eta$  thus cannot trigger a two-step phase transition. We then investigate the remained three models  $6 + 6$ ,  $15 + 6$  and  $15 + 15$  in detail.

We show that if only the IR contributions to the scalar potential are considered, all those three models cannot trigger SFOEWPT. For the  $6 + 6$  and  $15 + 15$  models, the problem is  $\langle \eta \rangle \gg f$ , which breaks the perturbativity of the theory; while for the  $15 + 6$  model, the issue is  $\lambda_{h\eta}^2 > \lambda_h \lambda_\eta$  cannot be satisfied. That means the generally-adopted assumption called minimal Higgs potential hypothesis (MHP), which assumes the IR contributions dominate the UV ones, is incompatible with the SFOEWPT in NMCHM for fermion embeddings up to 15. We also demonstrate that the SFOEWPT is hopeful to happen when the UV contributions are added. Taking the  $6 + 6$  model a concrete example, we combine the IR and UV contributions and numerically derive its allowed parameter space for SFOEWPT. The GWs from the phase transition are within the sensitive region of the future GW detectors. In addition, the model can be explored at the LHC via the searches for the composite resonances.

At last, we note the conundrum on the wall velocity for EW baryogenesis (EWB) and the GW: a significant GW signal prediction from the EWPT requires supersonic bubble wall expansion velocities  $v_{\mathrm{w}}$ , but the EWB prefers subsonic wall velocities for the effective diffusion. At present, this conundrum is still an open problem. refs. [94-96] suggest that the relevant velocity for baryogenesis is actually not  $v_{\mathrm{w}}$  but  $v_{+}$ , i.e. the relative velocity between the expanding bubble wall and the plasma just in front of it. Hydrodynamics analysis of the plasma shows that it is possible to have supersonic  $v_{\mathrm{w}}$  but sufficiently low  $v_{+}$  [94-96] and hence the EWB still works. We leave the detailed study on this issue for the future work.

# Acknowledgments

We are grateful to Lian-Tao Wang for the useful discussions about the UV contributions and EW sphaleron. We thank Avik Banerjee, Giacomo Cacciapaglia, Fa Peng Huang, Andrew Long, Michele Redi, Jing Shu and Yang Zhang for the discussions about phase transition and/or composite Higgs model. We are grateful to Guy D. Moore and Michael J. Ramsey-Musolf for discussions on baryon number preservation criterion and phase transition strength. LGB is supported by the National Natural Science Foundation of China under grant No. 11605016 and No. 11647307. YCW is supported by the Natural Sciences and Engineering Research Council of Canada (NSERC). KPX is supported by Grant Korea NRF 2015R1A4A1042542 and NRF 2017R1D1A1B03030820. KPX would like to express a special thanks to the Mainz Institute for Theoretical Physics (MITP) of the DFG Cluster of Excellence PRISMA $^{+}$  (Project ID 39083149) for its hospitality, because appendix C of this paper is a consequence of the discussions at MITP.

# A The CCWZ formulae for NMCHM

The generators of SO(6) group. They can be written as [81]:

$$
[ T _ {L} ^ {a} ] _ {I J} = - \frac {i}{2} \left[ \frac {1}{2} \epsilon^ {a b c} (\delta_ {b I} \delta_ {c J} - \delta_ {b J} \delta_ {c I}) + (\delta_ {a I} \delta_ {4 J} - \delta_ {a J} \delta_ {4 I}) \right],
$$

$$
\left[ T _ {R} ^ {a} \right] _ {I J} = - \frac {i}{2} \left[ \frac {1}{2} \epsilon^ {a b c} \left(\delta_ {b I} \delta_ {c J} - \delta_ {b J} \delta_ {c I}\right) - \left(\delta_ {a I} \delta_ {4 J} - \delta_ {a J} \delta_ {4 I}\right) \right], \tag {A.1}
$$

$$
[ \hat {T} _ {1} ^ {i} ] _ {I J} = - \frac {i}{\sqrt {2}} (\delta_ {i I} \delta_ {5 J} - \delta_ {i J} \delta_ {5 I}),
$$

$$
[ \hat {T} _ {2} ^ {r} ] _ {I J} = - \frac {i}{\sqrt {2}} (\delta_ {r I} \delta_ {6 J} - \delta_ {r J} \delta_ {6 I}),
$$

where  $(a = 1,2,3)$ ,  $(i = 1,\dots ,4)$ ,  $(r = 1,\dots ,5)$  and  $(I,J = 1,\dots ,6)$ . The normalization is  $\mathrm{tr}[T^A T^B] = \delta^{AB}$ . We denote the 10 unbroken generators of SO(5) as  $T^{\bar{A}} = \{T_L^a,T_R^a,\hat{T}_1^i\}$ , in which the  $\{T_L^a,T_R^a\}$  belong to the SO(4)  $\cong$  SU(2)  $L\times$  SU(2)  $R$  subgroup.

The  $d$  and  $e$  symbols in unitary gauge. The  $d$  symbol is

$$
d _ {\mu} ^ {1} = \frac {g _ {0} W _ {\mu} ^ {1}}{\sqrt {2}} \frac {h}{f}, d _ {\mu} ^ {2} = \frac {g _ {0} W _ {\mu} ^ {2}}{\sqrt {2}} \frac {h}{f}, d _ {\mu} ^ {3} = \frac {g _ {0} W _ {\mu} ^ {3} - g _ {0} ^ {\prime} B _ {\mu}}{\sqrt {2}} \frac {h}{f},
$$

$$
d _ {\mu} ^ {4} = \frac {\sqrt {2}}{f} \frac {1}{h ^ {2} + \eta^ {2}} \left[ \eta (h \partial_ {\mu} \eta - \eta \partial_ {\mu} h) - \frac {h (h \partial_ {\mu} h + \eta \partial_ {\mu} \eta)}{\sqrt {1 - (h ^ {2} + \eta^ {2}) / f ^ {2}}} \right], \tag {A.2}
$$

$$
d _ {\mu} ^ {5} = \frac {\sqrt {2}}{f} \frac {1}{h ^ {2} + \eta^ {2}} \left[ h (\eta \partial_ {\mu} h - h \partial_ {\mu} \eta) - \frac {\eta (h \partial_ {\mu} h + \eta \partial_ {\mu} \eta)}{\sqrt {1 - (h ^ {2} + \eta^ {2}) / f ^ {2}}} \right].
$$

The Goldstone kinetic term is given in eq. (2.6).

The  $e$  symbol has 10 components:  $e_{\mu}^{\bar{A}} = \{e_{L\mu}^{a}, e_{R\mu}^{a}, e_{1\mu}^{i}\}$ , corresponding to the SO(5)  $\rightarrow$  SO(4) decomposition  $\mathbf{10} \rightarrow (\mathbf{3}, \mathbf{1}) \oplus (\mathbf{1}, \mathbf{3}) \oplus (\mathbf{2}, \mathbf{2})$ . For the  $(\mathbf{3}, \mathbf{1})$  subset, we get

$$
e _ {L \mu} ^ {1} = g _ {0} W _ {\mu} ^ {1} - \frac {1}{2} g _ {0} W _ {\mu} ^ {1} \frac {h ^ {2}}{f ^ {2}} \left(\frac {1}{1 + \sqrt {1 - (h ^ {2} + \eta^ {2}) / f ^ {2}}}\right),
$$

$$
e _ {L \mu} ^ {2} = g _ {0} W _ {\mu} ^ {2} - \frac {1}{2} g _ {0} W _ {\mu} ^ {2} \frac {h ^ {2}}{f ^ {2}} \left(\frac {1}{1 + \sqrt {1 - \left(h ^ {2} + \eta^ {2}\right) / f ^ {2}}}\right), \tag {A.3}
$$

$$
e _ {L \mu} ^ {3} = g _ {0} W _ {\mu} ^ {3} - \frac {1}{2} \left(g _ {0} W _ {\mu} ^ {3} - g _ {0} ^ {\prime} B _ {\mu}\right) \frac {h ^ {2}}{f ^ {2}} \left(\frac {1}{1 + \sqrt {1 - (h ^ {2} + \eta^ {2}) / f ^ {2}}}\right);
$$

while for the  $(\mathbf{1},\mathbf{3})$  subset we get

$$
e _ {R \mu} ^ {1} = \frac {1}{2} g _ {0} W _ {\mu} ^ {1} \frac {h ^ {2}}{f ^ {2}} \left(\frac {1}{1 + \sqrt {1 - (h ^ {2} + \eta^ {2}) / f ^ {2}}}\right),
$$

$$
e _ {R \mu} ^ {2} = \frac {1}{2} g _ {0} W _ {\mu} ^ {2} \frac {h ^ {2}}{f ^ {2}} \left(\frac {1}{1 + \sqrt {1 - (h ^ {2} + \eta^ {2}) / f ^ {2}}}\right), \tag {A.4}
$$

$$
e _ {R \mu} ^ {3} = g _ {0} ^ {\prime} B _ {\mu} + \frac {1}{2} \left(g _ {0} W _ {\mu} ^ {3} - g _ {0} ^ {\prime} B _ {\mu}\right) \frac {h ^ {2}}{f ^ {2}} \left(\frac {1}{1 + \sqrt {1 - (h ^ {2} + \eta^ {2}) / f ^ {2}}}\right);
$$

finally the  $(\mathbf{2},\mathbf{2})$  gives

$$
e _ {1 \mu} ^ {1} = - \frac {1}{\sqrt {2}} g _ {0} W _ {\mu} ^ {1} \frac {h \eta}{f ^ {2}} \left(\frac {1}{1 + \sqrt {1 - (h ^ {2} + \eta^ {2}) / f ^ {2}}}\right),
$$

$$
e _ {1 \mu} ^ {2} = - \frac {1}{\sqrt {2}} g _ {0} W _ {\mu} ^ {2} \frac {h \eta}{f ^ {2}} \left(\frac {1}{1 + \sqrt {1 - \left(h ^ {2} + \eta^ {2}\right) / f ^ {2}}}\right), \tag {A.5}
$$

$$
e _ {1 \mu} ^ {3} = - \frac {1}{\sqrt {2}} \left(g _ {0} W _ {\mu} ^ {3} - g _ {0} ^ {\prime} B _ {\mu}\right) \frac {h \eta}{f ^ {2}} \left(\frac {1}{1 + \sqrt {1 - (h ^ {2} + \eta^ {2}) / f ^ {2}}}\right),
$$

$$
e _ {1 \mu} ^ {4} = \sqrt {2} \frac {\eta \partial_ {\mu} h - h \partial_ {\mu} \eta}{f ^ {2}} \left(\frac {1}{1 + \sqrt {1 - (h ^ {2} + \eta^ {2}) / f ^ {2}}}\right).
$$

The composite resonances. For the vector resonances, the full expressions of the decompositions in eq. (2.7) are

$$
\rho_ {L \mu} ^ {\pm} = \frac {\rho_ {L \mu} ^ {1} \mp i \rho_ {L \mu} ^ {2}}{\sqrt {2}}, \quad \rho_ {L \mu} ^ {0} = \rho_ {L \mu} ^ {3}; \quad \rho_ {R \mu} ^ {\pm} = \frac {\rho_ {R \mu} ^ {1} \mp i \rho_ {R \mu} ^ {2}}{\sqrt {2}}, \quad \rho_ {R \mu} ^ {0} = \rho_ {R \mu} ^ {3};
$$

$$
\rho_ {D \mu} = \left( \begin{array}{c} \rho_ {D \mu} ^ {+} \\ \rho_ {D \mu} ^ {0} \end{array} \right) = \frac {1}{\sqrt {2}} \left( \begin{array}{c} \rho_ {1 \mu} ^ {2} + i \rho_ {1 \mu} ^ {1} \\ \rho_ {1 \mu} ^ {4} - i \rho_ {1 \mu} ^ {3} \end{array} \right),
$$

for the  $\rho$ -resonances, and

$$
a _ {D \mu} = \left( \begin{array}{c} a _ {D \mu} ^ {+} \\ a _ {D \mu} ^ {0} \end{array} \right) = \frac {1}{\sqrt {2}} \left( \begin{array}{c} a _ {\mu} ^ {2} + i a _ {\mu} ^ {1} \\ a _ {\mu} ^ {4} - i a _ {\mu} ^ {3} \end{array} \right), \quad a _ {S \mu} = a _ {\mu} ^ {5}, \tag {A.7}
$$

for the  $a$ -resonances. In total, we have 4 singly charged and 7 real neutral vector resonances, in total 15 degrees of freedom.

The decomposition of the top partners are listed in eq. (2.10). For  $\Psi_{5}$ , the result is

$$
\Psi_ {5} = \frac {1}{\sqrt {2}} \left(i B - i X _ {5 / 3} B + X _ {5 / 3} i T + i X _ {2 / 3} - T + X _ {2 / 3} \widetilde {T}\right) ^ {T}, \tag {A.8}
$$

in which we can form two  $\mathrm{SU}(2)_L\times \mathrm{U}(1)_Y$  doublets

$$
Q _ {X} = \binom {X _ {5 / 3}} {X _ {2 / 3}} _ {7 / 6}, \quad Q = \binom {T} {B} _ {1 / 6}, \tag {A.9}
$$

and one singlet  $\widetilde{T}:\mathbf{1}_{2 / 3}$ . The decomposition of  $\Psi_{\mathbf{10}}$  is a little bit complicated,

$$
\Psi_ {\mathbf {1 0}} = t _ {L} ^ {a} Y ^ {a} + t _ {R} ^ {a} K ^ {a} + \hat {t} _ {1} ^ {i} J ^ {i}, \tag {A.10}
$$

where  $[t_{L,R}^a ]_{rs}\equiv [T_{L,R}^a ]_{rs},[\hat{t}_1^i ]_{rs}\equiv [\hat{T}_1^i ]_{rs}$  with  $(r,s = 1,\ldots ,5)$ , and  $Y^{a}$ ,  $K^{a}$  and  $J^{i}$  are respectively  $(\mathbf{3},\mathbf{1})_{2 / 3}$ ,  $(\mathbf{1},\mathbf{3})_{2 / 3}$  and  $(\mathbf{2},\mathbf{2})_{2 / 3}$  in  $\mathrm{SO}(4)\times \mathrm{U}(1)_X$ . Their explicit expressions are

$$
Y ^ {a} = \frac {1}{\sqrt {2}} \left( \begin{array}{c} Y _ {5 / 3} + Y _ {- 1 / 3} \\ i Y _ {5 / 3} - i Y _ {- 1 / 3} \\ \sqrt {2} Y _ {2 / 3} \end{array} \right), \quad K ^ {a} = \frac {1}{\sqrt {2}} \left( \begin{array}{c} K _ {5 / 3} + K _ {- 1 / 3} \\ i K _ {5 / 3} - i K _ {- 1 / 3} \\ \sqrt {2} K _ {2 / 3} \end{array} \right), \quad J ^ {i} = \frac {1}{\sqrt {2}} \left( \begin{array}{c} i J _ {- 1 / 3} - i J _ {5 / 3} \\ J _ {- 1 / 3} + J _ {5 / 3} \\ i J _ {2 / 3 A} + i J _ {2 / 3 B} \\ - J _ {2 / 3 A} + J _ {2 / 3 B} \end{array} \right), \tag {A.11}
$$

where the subscripts denote the electric charges. The  $J$  can be further organized into two  $\mathrm{SU}(2)_L\times \mathrm{U}(1)_Y$  doublets

$$
J _ {X} = \binom {J _ {5 / 3}} {J _ {2 / 3 B}} _ {7 / 6}, \quad J _ {Q} = \binom {J _ {2 / 3 A}} {J _ {- 1 / 3}} _ {1 / 6}. \tag {A.12}
$$

# B  $Zb_{L}\bar{b}_{L}$  coupling in the  $q_{L}^{15}$  embedding

The Lagrangian of top partner eq. (2.11) can be matched to the SM EFT form, yielding

$$
\mathcal {L} _ {\Psi} \supset \operatorname {t r} \left[ \bar {\Psi} _ {\mathbf {1 0}} \left(i \nabla + g _ {0} ^ {\prime} \frac {2}{3} \not B\right) \Psi_ {\mathbf {1 0}} \right] \supset \bar {Y} i D / Y + \bar {K} _ {- 1 / 3} i D / K _ {- 1 / 3} + \bar {J} _ {Q} i D / J _ {Q}, \tag {B.1}
$$

where  $D_{\mu}$  denotes the SM gauge covariant derivative. For a fermion with  $\mathrm{SU}(2)_L$  quantum number  $T_L^3$  and electric charge  $Q$ , the tree level coupling to  $Z$  boson is

$$
\frac {g}{c _ {W}} \left(T _ {L} ^ {3} - s _ {W} ^ {2} Q\right). \tag {B.2}
$$

For the charge  $-1 / 3$  particles we get

$$
T _ {L} ^ {3} (b _ {L}) = T _ {L} ^ {3} (B) = T _ {L} ^ {3} (J _ {- 1 / 3}) = - \frac {1}{2}, \quad T _ {L} ^ {3} (Y _ {- 1 / 3}) = - 1, \quad T _ {L} ^ {3} (K _ {- 1 / 3}) = 0. \qquad (\mathrm {B . 3})
$$

Thus the mixing between  $b_{L}$  and  $Y$ ,  $K$  will change the  $Zb_{L}\bar{b}_{L}$  coupling.14 While for the partial compositeness interactions,

$$
(\bar {q} _ {L} ^ {\mathbf {1 5} _ {A}}) _ {I J} U _ {J r} \Psi_ {\mathbf {1 0}} ^ {r s} [ U ^ {\dagger} ] _ {s I} \supset i \frac {1}{2 \sqrt {2} f ^ {2}} \bar {q} _ {L} \sigma^ {a} \widetilde {H} Y ^ {a} \pi^ {5} - i \frac {1}{2 f ^ {2}} \bar {q} _ {L} H K _ {- 1 / 3} \pi^ {5}, \qquad \mathrm {(B . 4)}
$$

and

$$
\begin{array}{l} \left(\bar {q} _ {L} ^ {\mathbf {1 5} _ {B}}\right) _ {I J} U _ {J r} \Psi_ {\mathbf {1 0}} ^ {r s} \left[ U ^ {\dagger} \right] _ {s I} \supset \\ \frac {1}{\sqrt {2} f} \bar {q} _ {L} \sigma^ {a} \widetilde {H} Y ^ {a} \left(1 - \frac {2 | H | ^ {2} + \pi_ {5} ^ {2}}{6 f ^ {2}}\right) - \frac {1}{f} \bar {q} _ {L} H K _ {- 1 / 3} \left(1 - \frac {2 | H | ^ {2} + \pi_ {5} ^ {2}}{6 f ^ {2}}\right). \quad (\mathrm {B . 5}) \\ \end{array}
$$

There is no  $b_{L} - Y$  or  $b_{L} - K$  mixing for the  $\mathbf{15}_A$  embedding, as long as  $\langle \pi_5 \rangle = \langle \eta \rangle = 0$  at zero temperature. In contrast, those mixings are present in  $\mathbf{15}_B$ . Since the  $Zb_{L}\bar{b}_{L}$  couplings are stringently constrained by LEP [73, 98],  $\mathbf{15}_B$  is strongly disfavored by the experiment and we will not use it to build the NMCHM in this paper.

# C The validity of polynomial approximation

Let's take the  $6 + 6$  model as an example. For the IR-driven potential, we expand the logarithms up to quartic level to get a polynomial, see eq. (3.7) for the gauge part and eq. (3.17) for the fermion part, respectively. For the gauge part, the polynomial approximation is valid even for  $h \sim f$ , because the expansion is suppressed by an additional factor of  $g^2 / g_\rho^2 \ll 1$ . However, for the fermion-induced potential, the corresponding factor is  $|y_{L,R}^{5,1,1'}|^2 f^2 / M_{5,1,1'}^2$ , which can be  $\mathcal{O}(1)$ . Therefore, one may concern about the validity of the polynomial approximation when  $\eta \sim f$ .

First we give a quantitative illustration about the difference between the two approaches (full calculation or polynomial expansion) using the SFOEWPT parameter points derived in section 4. The IR-driven potentials from those parameter points give  $|\eta| \gg f$ ,

![](images/f6c45594bb52b94eed0c5c03273d44a73816af376a05e3d20e94e3e6c5339a03.jpg)  
Figure 5. Left: the relative difference between potentials calculated by the complete Coleman-Weinberg integral and the polynomial expansion. Right: the relative difference of  $F_{1}$  and  $F_{2}$ .

![](images/360c0e2effacd7d85791617b3efd83d3edbbf795772dcdb23921ac6057f655e2.jpg)

thus we need the UV contributions to enhance  $\lambda_{f}$  to match the condition of SFOEWPT. Denoting the IR fully-calculated and polynomial potentials respectively as  $V_{\mathrm{full}}^{\mathrm{IR}}$  and  $V_{\mathrm{poly}}^{\mathrm{IR}}$ , the relative difference of the full calculation and the polynomial expansion along the  $\eta$  direction is defined as

$$
\delta V _ {\eta} = \left| \frac {V _ {\text {f u l l}} ^ {\mathrm {I R}} (0 , \eta) - V _ {\text {p o l y}} ^ {\mathrm {I R}} (0 , \eta)}{V _ {\text {f u l l}} ^ {\mathrm {I R}} (0 , \eta)} \right|, \tag {C.1}
$$

which is a function of  $\eta / f$ . In left panel of figure 5 we show the envelope of  $\delta V_{\eta}$  for all chosen parameter points. It can be read that the relative error of the polynomial approximation is within  $0.4\%$ , even for  $\eta / f \to 1$ . Thus the polynomial form of the potential is trustable. This is because of another additional factor in the logarithm expansion:  $\Pi_1^t / \Pi_0^t$  (see eq. (3.17) for the details). Since  $\Pi_1^t$  scales as  $Q^{-6}$ ,  $\Pi_1^t / \Pi_0^t$  is extremely small and the polynomial expansion works.

There is a semiquantitative way to understand the behavior of  $V_{\mathrm{full}}^{\mathrm{IR}}(0,\eta)$ . Eq. (3.17) is an integral of type

$$
V _ {\text {f u l l}} ^ {\mathrm {I R}} (0, \eta) \sim F _ {1} (\xi_ {f}) = - 2 N _ {c} \int \frac {Q ^ {2} d Q ^ {2}}{1 6 \pi^ {2}} \ln \left[ 1 + \frac {\xi_ {f} M ^ {6}}{\left(M ^ {2} + Q ^ {2}\right) ^ {3}} \right], \tag {C.2}
$$

where  $M\sim M_{5,1,1^{\prime}}$  and

$$
\xi_ {f} \sim \frac {\left| y _ {L , R} ^ {\mathbf {5} , \mathbf {1} , \mathbf {1} ^ {\prime}} \right| ^ {2} f ^ {2}}{M _ {\mathbf {5}, \mathbf {1} , \mathbf {1} ^ {\prime}} ^ {2}} \frac {\eta^ {2}}{f ^ {2}}. \tag {C.3}
$$

The polynomial expansion of  $V_{f}$ , on the other hand, is like

$$
V _ {\mathrm {p o l y}} ^ {\mathrm {I R}} (0, \eta) \sim F _ {2} (\xi_ {f}) = - 2 N _ {c} \int \frac {Q ^ {2} d Q ^ {2}}{1 6 \pi^ {2}} \left[ \frac {\xi_ {f} M ^ {6}}{(M ^ {2} + Q ^ {2}) ^ {3}} - \frac {1}{2} \left(\frac {\xi_ {f} M ^ {6}}{(M ^ {2} + Q ^ {2}) ^ {3}}\right) ^ {2} \right]. \tag {C.4}
$$

The integrals in eqs. (C.2) and (C.4) can be analytically evaluated, and the relative difference  $\left| \left( F_{1} - F_{2} \right) / F_{1} \right|$  depends only on  $\xi_{f}$ . The right panel of figure 5 shows this difference. One can see that even for  $\xi_{f} = 4$ , the relative error is smaller than  $9.5\%$ . Normally  $\xi_{f}$  is at most  $\mathcal{O}(1)$ , because we expect  $|y_{L,R}^{5,1,1'}| f \lesssim M_{5,1,1'}$ . For example, in the  $6 + 6$  model  $\xi_{f} < 0.6$  for all points with SFOEWPT. Therefore, the relative difference of full expression and polynomial approximation is usually within  $1\%$ .

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] D.B. Kaplan, Flavor at SSC energies: A New mechanism for dynamically generated fermion masses, Nucl. Phys. B 365 (1991) 259 [INSPIRE].  
[2] R. Contino, Y. Nomura and A. Pomarol, Higgs as a holographic pseudoGoldstone boson, Nucl. Phys. B 671 (2003) 148 [hep-ph/0306259] [INSPIRE].  
[3] K. Agashe, R. Contino and A. Pomarol, The Minimal composite Higgs model, Nucl. Phys. B 719 (2005) 165 [hep-ph/0412089] [INSPIRE].  
[4] R. Contino, L. Da Rold and A. Pomarol, Light custodians in natural composite Higgs models, Phys. Rev. D 75 (2007) 055014 [hep-ph/0612048] [INSPIRE].  
[5] B. Gripaios, A. Pomarol, F. Riva and J. Serra, Beyond the Minimal Composite Higgs Model, JHEP 04 (2009) 070 [arXiv:0902.1483] [INSPIRE].  
[6] G. Cacciapaglia and F. Sannino, Fundamental Composite (Goldstone) Higgs Dynamics, JHEP 04 (2014) 111 [arXiv:1402.0233] [INSPIRE].  
[7] J. Barnard, T. Gherghetta and T.S. Ray, UV descriptions of composite Higgs models without elementary scalars, JHEP 02 (2014) 002 [arXiv:1311.6562] [INSPIRE].  
[8] G. Ferretti and D. Karateev, Fermionic UV completions of Composite Higgs models, JHEP 03 (2014) 077 [arXiv:1312.5330] [INSPIRE].  
[9] A. Hietanen, R. Lewis, C. Pica and F. Sannino, Fundamental Composite Higgs Dynamics on the Lattice: SU(2) with Two Flavors, JHEP 07 (2014) 116 [arXiv:1404.2794] [INSPIRE].  
[10] M. Frigerio, A. Pomarol, F. Riva and A. Urbano, Composite Scalar Dark Matter, JHEP 07 (2012) 015 [arXiv:1204.2808] [INSPIRE].  
[11] D. Marzocca and A. Urbano, Composite Dark Matter and LHC Interplay, JHEP 07 (2014) 107 [arXiv:1404.7419] [INSPIRE].  
[12] Y. Wu, T. Ma, B. Zhang and G. Cacciapaglia, *Composite Dark Matter and Higgs*, JHEP **11** (2017) 058 [arXiv:1703.06903] [INSPIRE].  
[13] G. Cacciapaglia, S. Vatani, T. Ma and Y. Wu, Towards a fundamental safe theory of composite Higgs and Dark Matter, arXiv:1812.04005 [INSPIRE].  
[14] C. Cai, G. Cacciapaglia and H.-H. Zhang, Vacuum alignment in a composite 2HDM, JHEP 01 (2019) 130 [arXiv:1805.07619] [INSPIRE].

[15] S. Bruggisser, B. Von Harling, O. Matsedonskyi and G. Servant, Baryon Asymmetry from a Composite Higgs Boson, Phys. Rev. Lett. 121 (2018) 131801 [arXiv:1803.08546] [INSPIRE].  
[16] S. Bruggisser, B. Von Harling, O. Matsedonskyi and G. Servant, Electroweak Phase Transition and Baryogenesis in Composite Higgs Models, JHEP 12 (2018) 099 [arXiv:1804.07314] [INSPIRE].  
[17] J.R. Espinosa, B. Gripaios, T. Konstandin and F. Riva, Electroweak Baryogenesis in Non-minimal Composite Higgs Models, JCAP 01 (2012) 012 [arXiv:1110.2876] [INSPIRE].  
[18] M. Chala, G. Nardini and I. Sobolev, Unified explanation for dark matter and electroweak baryogenesis with direct detection and gravitational wave signatures, Phys. Rev. D 94 (2016) 055006 [arXiv:1605.08663] [INSPIRE].  
[19] M. Chala, M. Ramos and M. Spannowsky, Gravitational wave and collider probes of a triplet Higgs sector with a low cutoff, Eur. Phys. J. C 79 (2019) 156 [arXiv:1812.01901] [INSPIRE].  
[20] LISA collaboration, Laser Interferometer Space Antenna, arXiv:1702.00786 [INSPIRE].  
[21] TIANQIN collaboration, TianQin: a space-borne gravitational wave detector, Class. Quant. Grav. 33 (2016) 035010 [arXiv:1512.02076] [INSPIRE].  
[22] W.-R. Hu and Y.-L. Wu, The Taiji Program in Space for gravitational wave physics and the nature of gravity, Natl. Sci. Rev. 4 (2017) 685 [INSPIRE].  
[23] J. Crowder and N.J. Cornish, Beyond LISA: Exploring future gravitational wave missions, Phys. Rev. D 72 (2005) 083005 [gr-qc/0506015] [INSPIRE].  
[24] S. Kawamura et al., The Japanese space gravitational wave antenna: DECIGO, Class. Quant. Grav. 28 (2011) 094011 [INSPIRE].  
[25] S. Kawamura et al., The Japanese space gravitational wave antenna DECIGO, Class. Quant. Grav. 23 (2006) S125 [INSPIRE].  
[26] A. Mazumdar and G. White, Review of cosmic phase transitions: their significance and experimental signatures, Rept. Prog. Phys. 82 (2019) 076901 [arXiv:1811.01948] [INSPIRE].  
[27] J.M. Cline and K. Kainulainen, Electroweak baryogenesis and dark matter from a singlet Higgs, JCAP 01 (2013) 012 [arXiv:1210.4196] [INSPIRE].  
[28] T. Alanne, K. Tuominen and V. Vaskonen, *Strong phase transition, dark matter and vacuum stability from simple hidden sectors*, Nucl. Phys. B 889 (2014) 692 [arXiv:1407.0688] [INSPIRE].  
[29] F.P. Huang and C.S. Li, Electroweak baryogenesis in the framework of the effective field theory, Phys. Rev. D 92 (2015) 075014 [arXiv:1507.08168] [INSPIRE].  
[30] V. Vaskonen, Electroweak baryogenesis and gravitational waves from a real scalar singlet, Phys. Rev. D 95 (2017) 123515 [arXiv:1611.02073] [INSPIRE].  
[31] F.P. Huang and C.S. Li, Probing the baryogenesis and dark matter relaxed in phase transition by gravitational waves and colliders, Phys. Rev. D 96 (2017) 095028 [arXiv:1709.09691] [INSPIRE].  
[32] F.P. Huang, Z. Qian and M. Zhang, Exploring dynamical CP-violation induced baryogenesis by gravitational waves and colliders, Phys. Rev. D 98 (2018) 015014 [arXiv:1804.06813] [INSPIRE].

[33] C.-W. Chiang, Y.-T. Li and E. Senaha, Revisiting electroweak phase transition in the standard model with a real singlet scalar, Phys. Lett. B 789 (2019) 154 [arXiv:1808.01098] [INSPIRE].  
[34] L. Bian and X. Liu, Two-step strongly first-order electroweak phase transition modified FIMP dark matter, gravitational wave signals and the neutrino mass, Phys. Rev. D 99 (2019) 055003 [arXiv:1811.03279] [INSPIRE].  
[35] L. Bian and Y.-L. Tang, Thermally modified sterile neutrino portal dark matter and gravitational waves from phase transition: The Freeze-in case, JHEP 12 (2018) 006 [arXiv:1810.03172] [INSPIRE].  
[36] W. Cheng and L. Bian, Higgs inflation and cosmological electroweak phase transition with  $N$  scalars in the post-Higgs era, Phys. Rev. D 99 (2019) 035038 [arXiv:1805.00199] [INSPIRE].  
[37] G. Kurup and M. Perelstein, Dynamics of Electroweak Phase Transition In Singlet-Scalar Extension of the Standard Model, Phys. Rev. D 96 (2017) 015036 [arXiv:1704.03381] [INSPIRE].  
[38] R. Contino, The Higgs as a Composite Nambu-Goldstone Boson, in Physics of the large and the small, TASI 09, proceedings of the Theoretical Advanced Study Institute in Elementary Particle Physics, Boulder, Colorado, U.S.A., 1-26 June 2009, pp. 235-306 (2011) [DOI:10.1142/9789814327183_0005] [arXiv:1005.4269] [INSPIRE].  
[39] M.A. Shifman, A.I. Vainshtein and V.I. Zakharov, QCD and Resonance Physics. Theoretical Foundations, Nucl. Phys. B 147 (1979) 385 [INSPIRE].  
[40] M.A. Shifman, A.I. Vainshtein and V.I. Zakharov, QCD and Resonance Physics: Applications, Nucl. Phys. B 147 (1979) 448 [INSPIRE].  
[41] M. Knecht and E. de Rafael, Patterns of spontaneous chiral symmetry breaking in the large  $N_{c}$  limit of QCD-like theories, Phys. Lett. B 424 (1998) 335 [hep-ph/9712457] [INSPIRE].  
[42] D. Marzocca, M. Serone and J. Shu, General Composite Higgs Models, JHEP 08 (2012) 013 [arXiv:1205.0770] [INSPIRE].  
[43] A. Pomarol and F. Riva, The Composite Higgs and Light Resonance Connection, JHEP 08 (2012) 135 [arXiv:1205.6434] [INSPIRE].  
[44] M. Redi and A. Tesi, Implications of a Light Higgs in Composite Models, JHEP 10 (2012) 166 [arXiv:1205.0232] [INSPIRE].  
[45] A. Banerjee, G. Bhattacharyya and T.S. Ray, Improving Fine-tuning in Composite Higgs Models, Phys. Rev. D 96 (2017) 035040 [arXiv:1703.08011] [INSPIRE].  
[46] G. Panico and A. Wulzer, The Discrete Composite Higgs Model, JHEP 09 (2011) 135 [arXiv:1106.2719] [INSPIRE].  
[47] S.R. Coleman, J. Wess and B. Zumino, Structure of phenomenological Lagrangians. 1., Phys. Rev. 177 (1969) 2239 [INSPIRE].  
[48] C.G. Callan Jr., S.R. Coleman, J. Wess and B. Zumino, Structure of phenomenological Lagrangians. 2., Phys. Rev. 177 (1969) 2247 [INSPIRE].  
[49] G. Panico and A. Wulzer, The Composite Nambu-Goldstone Higgs, Lect. Notes Phys. 913 (2016) 1 [arXiv:1506.01961] [INSPIRE].  
[50] J. Mrazek, A. Pomarol, R. Rattazzi, M. Redi, J. Serra and A. Wulzer, The Other Natural Two Higgs Doublet Model, Nucl. Phys. B 853 (2011) 1 [arXiv:1105.5403] [INSPIRE].

[51] A. Banerjee, G. Bhattacharyya, N. Kumar and T.S. Ray, Constraining Composite Higgs Models using LHC data, JHEP 03 (2018) 062 [arXiv:1712.07494] [INSPIRE].  
[52] J.R. Espinosa, T. Konstandin and F. Riva, *Strong Electroweak Phase Transitions in the Standard Model with a Singlet*, Nucl. Phys. B 854 (2012) 592 [arXiv:1107.5441] [INSPIRE].  
[53] L. Dolan and R. Jackiw, Symmetry Behavior at Finite Temperature, Phys. Rev. D 9 (1974) 3320 [INSPIRE].  
[54] E. Braaten and R.D. Pisarski, Resummation and Gauge Invariance of the Gluon Damping Rate in Hot QCD, Phys. Rev. Lett. 64 (1990) 1338 [INSPIRE].  
[55] H.H. Patel and M.J. Ramsey-Musolf, Baryon Washout, Electroweak Phase Transition and Perturbation Theory, JHEP 07 (2011) 029 [arXiv:1101.4665] [INSPIRE].  
[56] X.-m. Zhang, Operators analysis for Higgs potential and cosmological bound on Higgs mass, Phys. Rev. D 47 (1993) 3065 [hep-ph/9301277] [INSPIRE].  
[57] C. Grojean, G. Servant and J.D. Wells, First-order electroweak phase transition in the standard model with a low cutoff, Phys. Rev. D 71 (2005) 036001 [hep-ph/0407019] [INSPIRE].  
[58] X. Gan, A.J. Long and L.-T. Wang, Electroweak sphaleron with dimension-six operators, Phys. Rev. D 96 (2017) 115018 [arXiv:1708.03061] [INSPIRE].  
[59] F.P. Huang, P.-H. Gu, P.-F. Yin, Z.-H. Yu and X. Zhang, Testing the electroweak phase transition and electroweak baryogenesis at the LHC and a circular electron-positron collider, Phys. Rev. D 93 (2016) 103515 [arXiv:1511.03969] [INSPIRE].  
[60] F.P. Huang, Y. Wan, D.-G. Wang, Y.-F. Cai and X. Zhang, Hearing the echoes of electroweak baryogenesis with gravitational wave detectors, Phys. Rev. D 94 (2016) 041702 [arXiv:1601.01640] [INSPIRE].  
[61] Q.-H. Cao, F.P. Huang, K.-P. Xie and X. Zhang, Testing the electroweak phase transition in scalar extension models at lepton colliders, Chin. Phys. C 42 (2018) 023103 [arXiv:1708.04737] [INSPIRE].  
[62] A.D. Linde, Decay of the False Vacuum at Finite Temperature, Nucl. Phys. B 216 (1983) 421 [Erratum ibid. B 223 (1983) 544] [INSPIRE].  
[63] G.D. Moore, Measuring the broken phase sphaleron rate nonperturbatively, Phys. Rev. D 59 (1999) 014503 [hep-ph/9805264] [INSPIRE].  
[64] M. Quiros, Finite temperature field theory and phase transitions, in Proceedings, Summer School in High-energy physics and cosmology, Trieste, Italy, 29 June-17 July 1998, pp. 187-259 (1999) [hep-ph/9901312] [INSPIRE].  
[65] R. Zhou, L. Bian and H.-K. Guo, Probing the Electroweak Sphaleron with Gravitational Waves, arXiv:1910.00234 [INSPIRE].  
[66] A. Denner, S. Heinemeyer, I. Puljak, D. Rebuzzi and M. Spira, Standard Model Higgs-Boson Branching Ratios with Uncertainties, Eur. Phys. J. C 71 (2011) 1753 [arXiv:1107.5909] [INSPIRE].  
[67] ATLAS collaboration, Combined measurements of Higgs boson production and decay using up to  $80fb^{-1}$  of proton-proton collision data at  $\sqrt{s} = 13$  TeV collected with the ATLAS experiment, ATLAS-CONF-2018-031 (2018).

[68] CMS collaboration, Combined measurements of Higgs boson couplings in proton-proton collisions at  $\sqrt{s} = 13$  TeV, Eur. Phys. J. C 79 (2019) 421 [arXiv:1809.10733] [INSPIRE].  
[69] H. Georgi, D.B. Kaplan and L. Randall, *Manifesting the Invisible Axion at Low-energies*, Phys. Lett. **169B** (1986) 73 [INSPIRE].  
[70] R. Jackiw, Functional evaluation of the effective potential, Phys. Rev. D 9 (1974) 1686 [INSPIRE].  
[71] S. Weinberg, Precise relations between the spectra of vector and axial vector mesons, Phys. Rev. Lett. 18 (1967) 507 [INSPIRE].  
[72] F. Feroz, M.P. Hobson and M. Bridges, MultiNest: an efficient and robust Bayesian inference tool for cosmology and particle physics, Mon. Not. Roy. Astron. Soc. 398 (2009) 1601 [arXiv:0809.3437] [INSPIRE].  
[73] ALEPH, DELPHI, L3, OPAL and SLD collaborations, LEP Electroweak Working Group, SLD Electroweak Group and SLD Heavy Flavour Group, Precision electroweak measurements on the Z resonance, Phys. Rept. 427 (2006) 257 [hep-ex/0509008] [INSPIRE].  
[74] PARTICLE DATA GROUP collaboration, Review of Particle Physics, Phys. Rev. D 98 (2018) 030001 [INSPIRE].  
[75] C.L. Wainwright, Cosmo Transitions: Computing Cosmological Phase Transition Temperatures and Bubble Profiles with Multiple Fields, Comput. Phys. Commun. 183 (2012) 2006 [arXiv:1109.4189] [INSPIRE].  
[76] C. Grojean and G. Servant, Gravitational Waves from Phase Transitions at the Electroweak Scale and Beyond, Phys. Rev. D 75 (2007) 043507 [hep-ph/0607107] [INSPIRE].  
[77] C. Caprini et al., Science with the space-based interferometer eLISA. II: Gravitational waves from cosmological phase transitions, JCAP 04 (2016) 001 [arXiv:1512.06239] [INSPIRE].  
[78] P.J. Steinhardt, Relativistic Detonation Waves and Bubble Growth in False Vacuum Decay, Phys. Rev. D 25 (1982) 2074 [INSPIRE].  
[79] J. Ellis, M. Lewicki and J.M. No, On the Maximal Strength of a First-Order Electroweak Phase Transition and its Gravitational Wave Signal, arXiv:1809.08242 [INSPIRE].  
[80] D. Buarque Franzosi, G. Cacciapaglia, H. Cai, A. Deandrea and M. Frandsen, Vector and Axial-vector resonances in composite models of the Higgs boson, JHEP 11 (2016) 076 [arXiv:1605.01363] [INSPIRE].  
[81] C. Niehoff, P. Stangl and D.M. Straub, Electroweak symmetry breaking and collider signatures in the next-to-minimal composite Higgs model, JHEP 04 (2017) 117 [arXiv:1611.09356] [INSPIRE].  
[82] D. Liu, L.-T. Wang and K.-P. Xie, Prospects of searching for composite resonances at the LHC and beyond, JHEP 01 (2019) 157 [arXiv:1810.08954] [INSPIRE].  
[83] ATLAS collaboration, Search for diboson resonances in hadronic final states in  $139fb^{-1}$  of pp collisions at  $\sqrt{s} = 13$  TeV with the ATLAS detector, JHEP 09 (2019) 091 [arXiv:1906.08589] [INSPIRE].  
[84] CMS collaboration, Search for top quark partners with charge 5/3 in the same-sign dilepton and single-lepton final states in proton-proton collisions at  $\sqrt{s} = 13$  TeV, JHEP 03 (2019) 082 [arXiv:1810.03188] [INSPIRE].

[85] J.H. Kim, K. Kong, B. Nachman and D. Whiteson, The motivation and status of two-body resonance decays after the LHC Run 2 and beyond, arXiv:1907.06659 [INSPIRE].  
[86] D. Barducci and C. Delaunay, Bounding wide composite vector resonances at the LHC, JHEP 02 (2016) 055 [arXiv:1511.01101] [INSPIRE].  
[87] N. Vignaroli, New  $W'$  signals at the LHC, Phys. Rev. D 89 (2014) 095027 [arXiv:1404.5558] [INSPIRE].  
[88] G. Cacciapaglia, H. Cai, A. Deandrea, T. Flacke, S.J. Lee and A. Parolini, Composite scalars at the LHC: the Higgs, the Sextet and the Octet, JHEP 11 (2015) 201 [arXiv:1507.02283] [INSPIRE].  
[89] A. Belyaev et al., Di-boson signatures as Standard Candles for Partial Compositeness, JHEP 01 (2017) 094 [Erratum ibid. 12 (2017) 088] [arXiv:1610.06591] [INSPIRE].  
[90] J. Serra, Beyond the Minimal Top Partner Decay, JHEP 09 (2015) 176 [arXiv:1506.05110] [INSPIRE].  
[91] N. Bizot, G. Cacciapaglia and T. Flacke, Common exotic decays of top partners, JHEP 06 (2018) 065 [arXiv:1803.00021] [INSPIRE].  
[92] K.-P. Xie, G. Cacciapaglia and T. Flacke, *Exotic decays of top partners with charge 5/3: bounds and opportunities*, JHEP **10** (2019) 134 [arXiv:1907.05894] [INSPIRE].  
[93] G. Cacciapaglia, T. Flacke, M. Park and M. Zhang, *Exotic decays of top partners: mind the search gap*, Phys. Lett. B **798** (2019) 135015 [arXiv:1908.07524] [INSPIRE].  
[94] J.M. No, Large Gravitational Wave Background Signals in Electroweak Baryogenesis Scenarios, Phys. Rev. D 84 (2011) 124025 [arXiv:1103.2159] [INSPIRE].  
[95] A. Alves, T. Ghosh, H.-K. Guo and K. Sinha, Resonant Di-Higgs Production at Gravitational Wave Benchmarks: A Collider Study using Machine Learning, JHEP 12 (2018) 070 [arXiv:1808.08974] [INSPIRE].  
[96] A. Alves, T. Ghosh, H.-K. Guo, K. Sinha and D. Vagie, *Collision and Gravitational Wave Complementarity in Exploring the Singlet Extension of the Standard Model*, JHEP 04 (2019) 052 [arXiv:1812.09333] [INSPIRE].  
[97] K. Agashe, R. Contino, L. Da Rold and A. Pomarol, A Custodial symmetry for  $Zb\bar{b}$ , Phys. Lett. B 641 (2006) 62 [hep-ph/0605341] [INSPIRE].  
[98] S. Gori, J. Gu and L.-T. Wang, The Zbbar couplings at future  $e^+ e^-$  colliders, JHEP 04 (2016) 062 [arXiv:1508.07010] [INSPIRE].