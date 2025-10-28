# Direct Higgs-top CP-phase measurement with  $t\bar{t}h$  at the 14 TeV LHC and 100 TeV FCC

Dorival Gonçalves, $^{a}$  Jeong Han Kim, $^{b,c,d,1}$  Kyoungchul Kong $^{e}$  and Yongcheng Wu $^{a,1}$

$^{a}$ Department of Physics, Oklahoma State University, Stillwater, OK, 74078, U.S.A.  
$^{b}$ Department of Physics, Chungbuk National University, Cheongju, Chungbuk 28644, South Korea  
$^c$ Center for Theoretical Physics of the Universe, Institute for Basic Science, Daejeon 34126, South Korea  
$^d$  Korea Institute for Advanced Study (KIAS), School of Physics, Seoul 02455, South Korea  
$^{e}$ Department of Physics and Astronomy, University of Kansas, Lawrence, KS 66045, U.S.A.

E-mail: dorival@okstate.edu, jeonghan.kim@cbu.ac.kr, kckong@ku.edu, ywu@okstate.edu

ABSTRACT: The study of the Higgs boson's properties is a cornerstone of the LHC and future collider programs. In this paper, we examine the potential to directly probe the Higgs-top interaction strength and CP-structure in the  $t\bar{t}h$  channel with the Higgs boson decaying to bottom-quark pairs and top-quarks in the di-leptonic mode. We adopt the BDRS algorithm to tag the boosted Higgs and exploit the  $M_2$ -assisted reconstruction to compute observables sensitive to the CP-phase at the  $t\bar{t}$  rest frame, where the new physics sensitivity can be enhanced. Performing a side-band analysis at the LHC to control the continuum  $t\bar{t}b\bar{b}$  background, we find that the Higgs-top strength and CP-phase can be probed up to  $\delta \kappa_t \lesssim 20\%$  and  $|\alpha| \lesssim 36^\circ$  at  $95\%$  CL, respectively. We also derive that a similar analysis at a 100 TeV future collider could further improve the precision to  $\delta \kappa_t \lesssim 1\%$  and  $|\alpha| \lesssim 1.5^\circ$ , where the CP-odd observables play a crucial role, boosting the sensitivity on the CP-phase.

KEYWORDS: Hadron-Hadron Scattering, Higgs Physics

ARXIV EPRINT: 2108.01083

# Contents

1 Introduction 1  
2 Theoretical setup 2  
3 Brief review on the  $M_2$ -assisted reconstruction of top pair 3  
4 Analysis 5

4.1 CP measurement at 14 TeV HL-LHC 6  
4.2 CP measurement at 100 TeV FCC-hh 10

5 Summary 14

# 1 Introduction

The possible existence of new CP-violating interactions can play a significant role in explaining the matter-antimatter asymmetry of the universe [1]. Thus, the search for new sources of CP-violation is a clear target in the quest for new physics. A prominent path in this program is to boost our current understanding of the Higgs boson couplings. Remarkably, from the theoretical viewpoint, there are some couplings more susceptible to display larger new physics effects than others. For instance, the well studied CP-odd Higgs-vector boson interactions can appear only through operators of dimension-6 or higher [2, 3], being naturally suppressed as it can only arise at the loop-level. Nevertheless, the CP-odd Higgsfermion couplings can manifest already at the tree level [4], granting naturally sizable CP violation effects.

Owning to its magnitude, the top quark Yukawa coupling is central to this discussion and could be most sensitive to physics beyond the Standard Model (SM). While it is possible to probe this interaction with loop-induced processes [5-11], the direct measurement via  $pp \rightarrow t\bar{t}h$  production plays a crucial role, disentangling possible new physics contributions [4, 12-26]. Recently ATLAS and CMS collaborations have reported the first experimental CP analyses using the  $t\bar{t}h$  production [27, 28]. These initial studies focus solely on the di-photon final state,  $h \rightarrow \gamma \gamma$ . ATLAS excludes the CP-mixing angle greater than  $43^\circ$  and CMS above  $55^\circ$  at  $95\%$  confidence level (CL).

The high luminosity LHC (HL-LHC) projections, performed by both ATLAS and CMS, indicate that the  $t\bar{t}h$  channel in the di-photon final state will result in dominant sensitivities for new physics searches, with a signal strength limit of  $\delta \mu_{tth}^{\gamma \gamma} \lesssim 5.9\%$  at  $68\%$  CL [29]. Despite the limited signal statistics, the di-photon channel highly benefits from controlled backgrounds through a side-band analysis. At the same time, the dominant Higgs decay to

bottom quarks,  $\mathcal{BR}(h\to b\bar{b})\sim 58\%$ , will only grant sub-leading limits,  $\delta \mu_{tth}^{bb}\lesssim 10.7\%$ , as its search endures a substantial QCD background associated with sizable uncertainties [30, 31].

Focusing on the 100 TeV Future Circular Collider (FCC) and semi-leptonic top pair final states, ref. [32] shows that a combination of side-bands and  $t\bar{t}h / t\bar{t}Z$  ratios can uplift the top-quark Yukawa strength determination with the  $t\bar{t}(h \rightarrow b\bar{b})$  channel. Inspired by this finding, we apply a similar methodology to control the background uncertainties for both the 14 TeV HL-LHC and 100 TeV FCC, deriving the top Yukawa CP-phase sensitivity. Instead of the semi-leptonic top pair final states, we consider the di-leptonic mode. Besides the significant background suppression, this final state benefits from the larger top quark spin analyzing power associated with charged leptons [33], resulting in stronger probes to the CP violation through spin correlations.

This paper is organized as follows. In section 2, we present the theoretical setup and discuss the relevant observables sensitive to the Higgs-top CP-phase. In section 3, we review the adopted reconstruction method for the di-leptonic top pair final state, which is relevant to build up prominent observables sensitive to new physics. We then move on to a detailed analysis in section 4, where we derive the projected sensitivities to the CP-phase from the HL-LHC and FCC, exploring the side-bands and the correlation between the  $t\bar{t}h$  and  $t\bar{t}Z$  uncertainties. Finally, we present a summary in section 5.

# 2 Theoretical setup

We parameterize the Higgs-top interaction as

$$
\mathcal {L} \supset - \frac {m _ {t}}{v} \kappa_ {t} \bar {t} (\cos \alpha + i \gamma_ {5} \sin \alpha) t h, \tag {2.1}
$$

where  $\kappa_{t}$  is a real number that modulates the interaction strength,  $\alpha$  is the CP-phase, and  $v = 246\mathrm{GeV}$  is the SM Higgs vacuum expectation value. The SM hypothesis displays  $\kappa_{t} = 1$  and  $\alpha = 0$ . In contrast, a purely CP-odd particle would have  $\alpha = \pi /2$ .

Among the several probes sensitive to the CP-structure of the Higgs-top interaction in the  $t\bar{t}h$  channel, the observables defined in the  $t\bar{t}$  center-of-mass frame play a special role [21]. First, this reference frame allows the definition of phenomenologically relevant CP-odd observables arising from fully anti-symmetric tensor products. A prominent example of this sort is the tensor product involving the two top quarks and the two final state charged leptons, that carry maximal top spin analyzing power,  $\epsilon_{\mu \nu \rho \sigma}p_t^\mu p_t^\nu p_\ell^{\rho}p_{\ell^-}^{\sigma}$ . This initially complex phenomenological probe can be opportunely simplified in the top pair frame to a simple triple product,  $\vec{p}_t\cdot (\vec{p}_{\ell +}\times \vec{p}_{\ell -})$ , being more suitable for collider studies. In particular, this mathematical property can be used to define the angular correlation between the charged leptons in the  $t\bar{t}$  rest frame [21]

$$
\Delta \phi_ {\ell \ell} ^ {t \bar {t}} = \mathrm {s g n} \left[ \vec {p} _ {t} \cdot (\vec {p} _ {\ell +} \times \vec {p} _ {\ell -}) \right] \arccos \left[ \frac {\vec {p} _ {t} \times \vec {p} _ {\ell +}}{| \vec {p} _ {t} \times \vec {p} _ {\ell +} |} \cdot \frac {\vec {p} _ {t} \times \vec {p} _ {\ell -}}{| \vec {p} _ {t} \times \vec {p} _ {\ell -} |} \right], \tag {2.2}
$$

which is also sensitive to the sign of the CP-phase. Second, there are additional robust observables that also display relevant sensitivity in this frame, such as the Collins-Soper

angle  $\theta^{*}$ . The  $\theta^{*}$  observable is the production angle of the top with respect to the beam axis in the  $t\bar{t}$  center-of-mass frame.

While the definition of several phenomenological probes in the top pair center-of-mass frame is a desirable ingredient to uplift the sensitivity to the CP-phase, the presence of two neutrinos in the di-leptonic  $t\bar{t}h$  channel brings a challenge for the event reconstruction in a hadron collider environment. In the next section, we will describe a mass minimization method to efficiently overcome this obstacle. This approach has been proven robust against parton shower, hadronization, and detector effects [21].

# 3 Brief review on the  $M_2$ -assisted reconstruction of top pair

The event topology considered in this study is depicted in figure 1, where the blue dotted, the green dot-dashed, and the black solid boxes indicate the three subsystems  $(b)$ ,  $(\ell)$ , and  $(b\ell)$ , respectively [34]. The Higgs decays to a pair of bottom quarks and the associated top quarks both decay leptonically. For such events with two missing particles, the on-shell constrained  $M_2$  variable provides a good estimation for the unobserved invisible momenta and thus can be useful to discriminate the combinatorial ambiguities [35-37]. The  $M_2$  [35] is defined as a  $(3 + 1)$ -dimensional version of the transverse mass  $M_{T2}$  [38]:

$$
M _ {2} (\tilde {m}) \equiv \min  _ {\vec {q} _ {1}, \vec {q} _ {2}} \left\{\max  \left[ M _ {P _ {1}} (\vec {q} _ {1}, \tilde {m}), M _ {P _ {2}} (\vec {q} _ {2}, \tilde {m}) \right] \right\}, \tag {3.1}
$$

$$
\vec {P} _ {T} = \vec {q} _ {1 T} + \vec {q} _ {2 T},
$$

where the actual parent masses,  $M_{P_i}$  ( $i = 1, 2$ ), are considered in the minimization instead of their transverse masses, as is done in  $M_{T2}$ . Note that the minimization is performed over the 3-component momentum vectors  $\vec{q}_1$  and  $\vec{q}_2$  of the two missing particles [35] under the missing transverse momentum constraint,  $\vec{P}_T = \vec{q}_{1T} + \vec{q}_{2T}$ . We use the zero test mass ( $\tilde{m} = 0$ ), as two missing particles are neutrinos in our study. At this point  $M_{T2}$  and  $M_2$  are known to be equivalent, in the sense that the resulting two variables lead to the same numerical value,  $M_{T2} = M_2 \leqslant \max(M_{P_1}, M_{P_2})$  [35, 39, 40].

However,  $M_2$  provides more flexibility in incorporating additional kinematic constraints. For example, in the  $tt$ -like production considered in this paper ( $t\bar{t} + X$ , where the transverse momentum of  $X$  is known), we could use the experimentally measured  $W$ -boson mass,  $m_W$ , and introduce the following variable in the ( $b\ell$ ) subsystem:

$$
M _ {2 C W} ^ {(b \ell)} (\tilde {m}) \equiv \min  _ {\vec {q} _ {1}, \vec {q} _ {2}} \left\{\max  \left[ M _ {t _ {1}} \left(\vec {q} _ {1}, \tilde {m}\right), M _ {t _ {2}} \left(\vec {q} _ {2}, \tilde {m}\right) \right] \right\}, \tag {3.2}
$$

$$
\vec {F} _ {T} = \vec {q} _ {1 T} + \vec {q} _ {2 T},
$$

$$
M _ {t _ {1}} = M _ {t _ {2}},
$$

$$
M _ {W _ {1}} = M _ {W _ {2}} = m _ {W}.
$$

Here, the second constraint  $M_{t_1} = M_{t_2}$  requires the equality of two parent mass without use of a specific numerical value, while the true  $W$  mass is used in the third constraint  $M_{W_1} = M_{W_2} = m_W$ . Similarly, taking the top quark mass  $m_t$  in the minimization, we can

![](images/51c32affbbd89d1180aae1925814c88ba7d3523efc20b66445255d072f3edf4f.jpg)  
Figure 1. The event topology considered in this paper. The blue dotted, the green dot-dashed, and the black solid boxes indicate the subsystems  $(b)$ ,  $(\ell)$ , and  $(b\ell)$ , respectively.

define a new variable in the  $(\ell)$  subsystem:

$$
M _ {2 C t} ^ {(\ell)} (\tilde {m}) \equiv \min  _ {\vec {q} _ {1}, \vec {q} _ {2}} \left\{\max  \left[ M _ {W _ {1}} (\vec {q} _ {1}, \tilde {m}), M _ {W _ {2}} (\vec {q} _ {2}, \tilde {m}) \right] \right\}, \tag {3.3}
$$

$$
\vec {P} _ {T} = \vec {q} _ {1 T} + \vec {q} _ {2 T},
$$

$$
M _ {W _ {1}} = M _ {W _ {2}},
$$

$$
M _ {t _ {1}} = M _ {t _ {2}} = m _ {t}.
$$

These distributions exhibit sharper end point structure in their kinematic distribution, due to additional mass information in the minimization, i.e.,  $M_2^{(b\ell)} \leqslant M_{2CW}^{(b\ell)} \leqslant m_t$  and  $M_2^{(\ell)} \leqslant M_{2Ct}^{(\ell)} \leqslant m_W$  [35, 40].

While these mass-constraining variables are proposed for mass measurement originally, one could use them for other purposes, such as measurement of spins and couplings [36, 41]. In our study, we use these variables to fully reconstruct the final state of our interest, with the unknown neutrino momenta obtained via minimization procedure. These momenta may or may not be true momenta of the missing neutrinos, but they provide important non-trivial correlations with other visible particles in the final state, which improves the reconstruction.

Based on ref. [36], we take advantage of the kinematic features of the following 3-dimensional mass space:

$$
\left(m _ {b \ell} ^ {\max } - \max  _ {i} \{m _ {b \ell} ^ {(i)} \}, m _ {t} - M _ {2 C W} ^ {(b \ell)}, m _ {W} - M _ {2 C t} ^ {(\ell)}\right), \tag {3.4}
$$

where  $m_{b\ell}^{(i)}$  is the invariant mass of  $b$  and  $\ell$  in the  $i$ -th side ( $i = 1,2$ ), and  $m_{b\ell}^{\max} = \sqrt{m_t^2 - m_W^2}$  (in the  $m_b \to 0$  limit). Since there are two possible ways of pairing  $b$  and  $\ell$  in the di-lepton channel of the  $t\bar{t}$ -like events, we repeat the same calculation for each partition. The correct combination would respect the anticipated end points of  $m_{b\ell}$ ,  $M_{2CW}^{(b\ell)}$ , and  $M_{2Ct}^{(\ell)}$ , leading to positive values of three components in above 3-dimensional mass space. On the other hand, the wrong pairing could give either sign. By requiring that the partition which gives more "plus" sign as the "correct" one, we can resolve the two-fold

ambiguity. Then, we treat the corresponding momenta of two missing particles, which are obtained via the minimization procedure, as "real" momenta of two missing neutrinos. If both partitions give the same numbers of positive and negative signs, we discard such events, since they are "unresolved cases". We note that we assign the negative sign for a partition, if a viable solution is not found during minimization. This is because the wrong pairing would fail more often than the correct one.

From ref. [36], the efficiency of this method at the parton-level is known to be about  $88\%$ , including unresolved events with a coin flip,  $50\%$  probability of picking the right combination. Since we ignore those events to obtain a high-purity sample, the corresponding efficiency becomes  $83\%$ . In our analysis, we find that the final efficiency is about  $78\%$  including more realistic effects such as parton-shower and hadronization.

We use OPTIMASS [42] for the minimization to obtain momenta of two invisible neutrinos, following the reconstruction method described above. With the obtained neutrino momenta, now we can reconstruct momenta of  $W$ -bosons and top quarks for the measurement of the CP-phase. The fully reconstructed top quark momenta allow the Lorenz-boost transformation from the lab frame to the  $tt$  rest frame, which is crucial for our analysis.

# 4 Analysis

To directly probe the Higgs-top CP-structure, we explore the  $pp \rightarrow t\bar{t}h$  production with the Higgs boson decay to bottom quarks,  $h \rightarrow b\bar{b}$ , associated with di-leptonic top quarks. We derive the new physics sensitivity for both the 14 TeV HL-LHC and 100 TeV FCC [43]. Our signal is characterized by two opposite sign charged leptons,  $\ell = e$  or  $\mu$ , and four  $b$ -tagged jets. The major backgrounds, in order of relevance, are  $t\bar{t}b\bar{b}$  and  $t\bar{t}Z$ . The signal and background event samples are simulated with MadGraph5_aMC@NLO [44]. To include higher order effects, we rescale the  $t\bar{t}h$ ,  $t\bar{t}b\bar{b}$ , and  $t\bar{t}Z$  cross-sections with flat next-to-leading order k-factors derived with MadGraph5_aMC@NLO. The parton shower, hadronization, and underlying event effects are included with Pythia6 [45]. To secure top-quark spin-correlation effects, the top-quark decays are performed with MadSpin [46].

The adopted analysis strategy explores the boosted Higgs regime. Along with the background suppression [47, 48], this kinematic configuration opportunistically enhances the top-quark spin correlation effects [4]. We begin our analysis requiring two isolated and opposite charged leptons with  $p_{T\ell} > 20 \mathrm{GeV}$  and  $|\eta_{\ell}| < 2.5$ . The hadronic part of the event is first reclustered using the Cambridge/Aachen jet algorithm with  $R = 1.2$ , requiring one or more boosted fat-jets with  $p_{TJ} > 200 \mathrm{GeV}$  and  $|\eta_J| < 2.5$ . The jet reclustering is performed with FastJet [49]. We demand one of the fat-jets to be Higgs-tagged via the BDRS algorithm [47], imposing that its two hardest subjets are  $b$ -tagged. Since the complete analysis displays four  $b$ -tags, we take advantage of the improvements reported by ATLAS, associated with the central tracking system for the operation at the HL-LHC, and use a work point with a large  $b$ -tagging efficiency [50]. We assume  $85\%$ $b$ -tagging efficiency associated with  $1\%$  (25%) mistag rate for light-jets ( $c$ -jets), being consistent with the experimental studies from the ATLAS collaboration.

Table 1. Cumulative cut-flow table showing cross-section in fb for  $t\bar{t}h$  signal ( $\kappa_{t} = 1, \alpha = 0$ ) and leading backgrounds  $t\bar{t}\bar{b}\bar{b}$  and  $t\bar{t}Z$  at the 14 TeV LHC. Significances ( $\sigma$ ) are calculated for a luminosity of 3 ab $^{-1}$ . We apply a flat  $b$ -tag rate of  $\epsilon_{b \to b} = 0.85$  and a light-jet ( $c$ -jet) mistag rate of  $\epsilon_{j \to b} = 0.01$  ( $\epsilon_{c \to b} = 0.25$ ) in accordance with the improvements reported by the ATLAS collaboration for the HL-LHC performance [50].  

<table><tr><td>cuts</td><td>t\bar{t}h</td><td>t\bar{t}b\bar{b}</td><td>t\bar{t}Z</td><td>σ</td></tr><tr><td>Nh=1, 4b-tags, pTℓ&gt;20 GeV, |ηℓ|&lt;2.5pTj&gt;30 GeV, |ηj|&lt;2.5, Nj≥2, Nℓ=2</td><td>0.358</td><td>4.08</td><td>0.106</td><td>9.45</td></tr><tr><td>50 GeV &lt; mJ^BDRS &lt; 150 GeV</td><td>0.306</td><td>2.18</td><td>0.0971</td><td>10.9</td></tr><tr><td>Resolving combinatorics</td><td>0.239</td><td>1.47</td><td>0.0796</td><td>10.3</td></tr></table>

Since the signal event does not display another hadronic heavy particle decay, we can safely suppress the underlying event contamination by using a smaller jet size for the rest of the event. Hence, after the Higgs tagging, we remove the fat-jet associated with the Higgs boson and recluster the remaining hadronic activity with the anti- $\mathbf{k}_t$  jet algorithm with  $R = 0.4$ ,  $p_{Tj} > 30 \mathrm{GeV}$ , and  $|\eta_j| < 2.5$ . We demand two extra  $b$ -tagged jets to control possible extra backgrounds. More details on the event selections are described in table 1 and table 2 for the 14 TeV HL-LHC and 100 TeV FCC, respectively.

# 4.1 CP measurement at 14 TeV HL-LHC

We present in figure 2 the invariant mass distribution of the BDRS tagged fat-jet,  $m_J^{\mathrm{BDRS}}$ , for the signal and background samples at the 14 TeV HL-LHC with  $3\mathrm{ab}^{-1}$  of data. Remarkably, the Higgs signal from the  $t\bar{t}h$  sample results in a clear peak structure around the Higgs mass. In particular, this is a result of the BDRS filtering that promotes the invariant mass associated with the fat-jet to a robust observable efficiently controlling the pile-up effects [51].

We show in figure 3 the relevant CP sensitive probes for the  $t\bar{t}h$  samples used in this analysis, namely  $\theta^{*}$  (left),  $\Delta \phi_{\ell \ell}^{\mathrm{lab}}$  (middle), and  $\Delta \phi_{\ell \ell}^{\bar{t}\bar{t}}$  (right). In the bottom of each panel, we show the ratio of non-zero CP phase to the SM prediction ( $\alpha = 0$ ). These distributions are presented after reconstruction of the top quark pair, with the selections outlined in table 1. The  $\Delta \phi_{\ell \ell}^{t\bar{t}}$  distribution exhibits the sensitivity on the sign of the CP-phase, while both  $\theta^{*}$  and  $\Delta \phi_{\ell \ell}^{\mathrm{lab}}$  are CP-even variables. We observe that the  $t\bar{t}$  reconstruction described in section 3 is robust, resulting in observables with strong modulations for distinct top Yukawa CP-phases even at the hadron level.

To enhance the signal sensitivity, we perform a binned log-likelihood analysis exploring the Higgs candidate invariant mass profile, in the signal range  $m_J^{\mathrm{BDRS}} \in [110, 135]$  GeV, together with the CP-sensitive observable  $\theta^{*}$ , defined at the  $t\bar{t}$  center-of-mass frame. Since the considered  $t\bar{t}h$  channel with  $h \to b\bar{b}$  typically confronts a large  $t\bar{t}b\bar{b}$  background, which has a significant uncertainty [30, 31], the final result displays relevant correlation with the considered background uncertainties. To estimate this effect, we derive the new physics sensitivity on the  $(\alpha, \kappa_t)$  plane for two scenarios. In the first case, we assume that, besides

![](images/255d269af50284e909fa2e028335fb13e112695867aeef3058148df2baa5036f.jpg)  
Figure 2. The invariant mass distributions of signal and background for the BDRS tagged fat-jet  $m_J^{\mathrm{BDRS}}$  at the 14 TeV HL-LHC. We show  $t\bar{t}h$  signal (red), the  $t\bar{t}b\bar{b}$  (blue), and  $t\bar{t}Z$  (green) in a nonstacked format. The full stacked result is also presented (black). We assume  $3\mathrm{ab}^{-1}$  of integrated luminosity. For more details on the cut-flow analysis, see table 1.

![](images/42bdc1e0d652b7723d03e94023a64d58c05d2a9a472e2855d2db82410a0ff8ac.jpg)  
Figure 3.  $\theta^{*}$  (left),  $\Delta \phi_{\ell \ell}^{\mathrm{lab}}$  (middle), and  $\Delta \phi_{\ell \ell}^{t\bar{t}}$  (right) distributions for the  $t\bar{t}h$  samples at the 14 TeV LHC, after the basic cuts described in table 1, and resolving the combinatorial problem.

![](images/13c0307c92c1fd774e4061a2c87273983416505e3682909c148a953fc580ff88.jpg)

![](images/1630bc75f3d27061a82c5cb5c7614e66d235473da8245e245f11be9659621286.jpg)

the statistical uncertainties that are modelled using Poisson distribution for each bin of the distribution,  $t\overline{t}b\overline{b}$  background rate has an overall  $20\%$  of systematics, which is included as a nuisance parameter, following a Gaussian distribution centered around the SM value. The magnitude of the considered error is similar to the current experimental analyses [30, 31]. For the second case, we assume an optimistic scenario with  $5\%$  error. The uncertainties on the  $t\bar{t}h$  and  $t\bar{t}Z$  samples are assumed to be  $10\%$  for both scenarios [32]. The result of this analysis is presented in the left panel of figure 4. We obtain that the CP-mixing angle can be constrained to  $|\alpha| \lesssim 32^\circ$  at  $68\%$  CL at the HL-LHC for both scenarios. At the same time, we find that the sensitivity from  $\kappa_t$  to the systematic error is more pronounced. While in the first scenario we can constrain the top Yukawa strength to  $\delta \kappa_t \lesssim 0.3$ , the more optimistic case leads to  $\delta \kappa_t \lesssim 0.15$ .

![](images/6cc1ccbbd5ecd9a52adf256ec8303b37829ea63540ae106a59c796a9fe1f4091.jpg)  
Figure 4. The exclusion at  $68\%$  (red) and  $95\%$  (green) CL in the  $\alpha-\kappa_{t}$  plane at the  $14\mathrm{TeV}$  LHC with  $3\mathrm{ab}^{-1}$  for a narrow (left) and wide (right) mass window.  $20\%$  systematics ( $5\%$ ) for  $t\bar{t}b\bar{b}$  is assumed in solid (dotted) curves, while  $10\%$  systematics is used for both  $t\bar{t}Z$  and  $t\bar{t}h$ .

![](images/610fac1c1058e2264092238c1f89cde029e921e47c3167d4be01fdd24362789a.jpg)

We note that in the absence of the shape information of the  $\theta^{*}$  distribution, there exists a flat direction in the  $(\alpha, \kappa_{t})$  plane, irrespective of the considered uncertainty scenarios, where two red (or green) curves meet tangentially as shown in the left panel of figure 4. In other words, along the flat direction, there is no constraint on the values of  $\kappa_{t}$  and  $\alpha$ . The constraint stems from the shape of  $\theta^{*}$  distribution. Therefore, along that flat direction, the limits on  $(\alpha, \kappa_{t})$  will not change and the considered uncertainties of  $t\bar{t}b\bar{b}$  do not affect the fit. Further, when  $\kappa_{t} \sim 0.4$ , there is no sensitivity on  $\alpha$  for the case with large systematics ( $20\%$  for  $t\bar{t}b\bar{b}$ ). This is because the signal rate is suppressed for  $\kappa_{t}$  around that region, and thus we gain no information from  $\theta^{*}$  distribution, while the large systematics from the  $t\bar{t}b\bar{b}$  can compensate the total event rate. When  $\kappa_{t}$  is even smaller, the signal rate is further suppressed, and the fluctuation from background alone cannot explain the total event rate, excluding the small  $\kappa_{t}$  region.

This observation in the left panel of figure 4 can be more clearly understood by studying the separate exclusions. In figure 5, we show the individual exclusion at  $68\%$  CL from the rate-only measurement (in magenta) and the shape-only measurement (in blue). The exclusion with the rate-only does not have significant sensitivity on  $\alpha$ , since the signal rate remains roughly fixed as the CP angle  $\alpha$  varies. This arises from a combination of two effects that approximately cancel out. While the inclusive  $t\bar{t}h$  production cross-section decreases when scanning  $\alpha$  from 0 to  $\pi/2$  [52, 53], the signal acceptance increases for larger  $\alpha$  due to a sizable difference in kinematics between CP-even ( $\alpha = 0$ ) and CP-odd ( $\alpha = \pi/2$ ) in the boosted regime [21]. The two factors roughly cancel, leading to suppressed differences in event rate for distinct  $\alpha$ . On the other hand, the shape-only exclusion exhibits sensitivity on  $\alpha$ . Hence, one can recover the general profile of the exclusion in figure 4 by combining the four curves in figure 5.

To illustrate how to reduce the systematics for  $t\bar{t} b\bar{b}$  in a realistic measurement, we enlarge the mass range of the Higgs candidate to  $m_J^{\mathrm{BDRS}} \in [50,150]$  GeV. In this way, the events outside the Higgs peak, which mainly come from  $t\bar{t} b\bar{b}$ , can be used together with the shape of  $m_J^{\mathrm{BDRS}}$  distribution of  $t\bar{t} b\bar{b}$  from MC simulation within the binned log-

![](images/86ca044c134b59187d9bb2a7d5036274a227ff73cefcca06e70f10c8aa556c65.jpg)  
Figure 5. The individual exclusion at  $68\%$  CL from the rate-only measurement (magenta) and shape-only measurement (blue) for two different assumptions on the systematic uncertainty for  $t\bar{t} b\bar{b}$ ,  $20\%$  in solid and  $5\%$  in dotted.

likelihood method. By fitting to a broader range of  $m_J^{\mathrm{BDRS}}$ , we have a better control of the uncertainties of  $t\bar{t} b\bar{b}$ . The results are shown in the right panel of figure 4. We find that this analysis depletes the influence of the systematic uncertainties, leading to similar results for the two considered systematic uncertainty scenarios. The obtained limits are  $|\alpha| \lesssim 26^\circ$  ( $36^\circ$ ) and  $\delta \kappa_t \lesssim 0.12$  (0.2) at  $68\%$  ( $95\%$ ) CL. Using the wider mass window, the log-likelihood analysis takes full advantage of the shape information of  $t\bar{t} h$  and  $t\bar{t} b\bar{b}$  events.

It is illuminating to analyze the number of signal and background events in the Higgs peak and side-bands to infer the uncertainty suppression. Around the Higgs peak  $m_J^{\mathrm{BDRS}} \in [110, 135]$  GeV, the number of signal events at the HL-LHC is  $N_{tth} = N_S = N_{\mathrm{total}} - N_{ttbb} \approx 402$ , whereas the number of background events is  $N_B = N_{ttbb} \approx 865$ . For this discussion, given the considered invariant mass window for  $m_J^{\mathrm{BDRS}}$ , the  $ttZ$  background makes a subleading contribution. Assuming  $20\%$  systematics ( $\Delta N_{ttbb} = 0.2 \times N_{ttbb}$ ) for the  $ttbb$  events, one can estimate the uncertainty,  $\Delta N_S$ , for  $N_S$  as follows,

$$
\begin{array}{l} (\Delta N _ {S}) ^ {2} = \left(\sqrt {N _ {\mathrm {t o t a l}}}\right) ^ {2} + (\Delta N _ {t t b b}) ^ {2} \\ = N _ {\text {t o t a l}} + \left(0. 2 \times N _ {t t b b}\right) ^ {2} \\ \approx 3 1, 1 9 6 \\ \approx \left(0. 4 4 \times N _ {S}\right) ^ {2}, \tag {4.1} \\ \end{array}
$$

which is very large due to the background events in the signal region. However, if we use the side-band events to estimate the  $t\bar{t} b\bar{b}$  events within the Higgs peak, we can suppress the uncertainties in the signal region. For  $m_J^{\mathrm{BDRS}} \in [50,110] \oplus [135,150]$  GeV, we have  $N_{\mathrm{sideband}} \approx 3,543$ . Then, the signal  $(t\bar{t} h)$  events can be estimated directly from measurement as  $N_S = N_{\mathrm{total}} - \kappa N_{\mathrm{sideband}}$ , where  $N_{\mathrm{total}} = 1,267$  for  $m_J^{\mathrm{BDRS}} \in [110,135]$  GeV. Here,  $\kappa$  is the ratio of the number of background events in the signal region ( $N_B = 865$ ) to that in the side-band region ( $N_{\mathrm{sideband}} = 3,543$ ), which can be estimated from MC or from the shape of the inferred background distribution using the side-bands. As an illustration, we

![](images/db153501f7751cc7f200e639a26a989a0d91d4f733557d191a6382e03a47e30b.jpg)  
Figure 6. Cross-section for  $pp \to t\bar{t}h$  and  $pp \to t\bar{t}Z$  production at the parton level as a function of the  $pp$  collider energy. We require the Higgs and Z bosons in the boosted regime,  $p_{Th,Z} > 200\mathrm{GeV}$ , and account for their branching ratios to a bottom-quark pair,  $\mathcal{BR}(h,Z \to b\bar{b})$ . Top quarks are set stable.

fix  $\kappa$  as  $\kappa = N_B / N_{\mathrm{sideband}}$ . Then the uncertainties for  $N_S$  is calculated as

$$
\begin{array}{l} \left(\Delta N _ {S}\right) ^ {2} = \left(\sqrt {N _ {\mathrm {t o t a l}}}\right) ^ {2} + \left(\kappa \Delta N _ {\mathrm {s i d e b a n d}}\right) ^ {2} \\ = N _ {\mathrm {t o t a l}} + \left(\kappa \sqrt {N _ {\mathrm {s i d e b a n d}}}\right) ^ {2} \\ = N _ {\mathrm {t o t a l}} + \frac {N _ {B} ^ {2}}{N _ {\mathrm {s i d e b a n d}}} \\ \approx 1, 4 7 8. 2 \\ \approx \left(0. 0 9 6 \times N _ {S}\right) ^ {2}, \tag {4.2} \\ \end{array}
$$

which has significantly lower uncertainties for  $N_{S}$  with the aid of the events from the sidebands [32]. Similar background control regions are actively used in experimental analyses, for example, for the  $h\rightarrow \gamma \gamma$  channel [54], and  $Wh / Zh$  production in the  $h\to b\bar{b}$  decay channel [55].

# 4.2 CP measurement at 100 TeV FCC-hh

The Higgs-top CP-phase measurement would render remarkable gains at a future 100 TeV collider due to the immensely increased statistics. In figure 6, we show the cross-section for  $pp \rightarrow t\bar{t}h$  and  $pp \rightarrow t\bar{t}Z$  production as a function of the collider energy. We require the Higgs and  $Z$  bosons in the boosted regime,  $p_{Th,Z} > 200\mathrm{GeV}$ , and account for their branching ratios to bottom quarks,  $\mathcal{BR}(h,Z \rightarrow b\bar{b})$ . While the  $t\bar{t}(h \rightarrow b\bar{b})$  and  $t\bar{t}(Z \rightarrow b\bar{b})$  processes are phase space suppressed at the 14 TeV LHC, with limited production cross-sections of 0.04 pb and 0.02 pb, the 100 TeV collider would result in one hundred-fold enhancement, with a cross-section of 3.8 pb and 2.1 pb, respectively. Considering the leptonic top pair decay, this corresponds to an uplift in the number of events for the  $t\bar{t}h$  signal from  $5.8 \times 10^{3}$  at the HL-LHC with  $3\mathrm{ab}^{-1}$  to  $5.5 \times 10^{6}$  at 100 TeV with  $30\mathrm{ab}^{-1}$ . This estimate shows

![](images/24a9de371de80dd970179d9c737a27f0ae94f6bd2e75b261c35efbe925f7da4e.jpg)  
Figure 7. The invariant mass distributions of the signal and background for the BDRS tagged fat-jet  $m_J^{\mathrm{BDRS}}$  at the 100 TeV FCC-hh. We show  $t\bar{t} h$  signal (red), the  $t\bar{t}\bar{b}\bar{b}$  (blue), and  $t\bar{t} Z$  (green) in a non-stacked format. The full stacked result is also presented (black). We assume 30 ab $^{-1}$  of the integrated luminosity.

Table 2. Cumulative cut-flow table showing cross-section in fb for  $t\bar{t}h$  signal ( $\kappa_{t} = 1, \alpha = 0$ ) and leading backgrounds  $t\bar{t}b\bar{b}$  and  $t\bar{t}Z$  at a 100 TeV future collider. The signal significances ( $\sigma$ ) are calculated for a luminosity of 30 ab $^{-1}$ .  

<table><tr><td>cuts</td><td>t\bar{t}h</td><td>t\bar{t}b\bar{b}</td><td>t\bar{t}Z</td><td>σ</td></tr><tr><td>Nh=1, 4b-tags, pTl&gt;20 GeV, |ηl&lt;2.5pTj&gt;30 GeV, |ηj&lt;2.5, Nj≥2, Nl=2</td><td>21.5</td><td>351</td><td>6.93</td><td>194.9</td></tr><tr><td>50 GeV &lt; mJ\text{BDRS}&lt; 150 GeV</td><td>17.7</td><td>177</td><td>6.15</td><td>223.0</td></tr><tr><td>Resolving combinatorics</td><td>14.0</td><td>116</td><td>5.11</td><td>216.3</td></tr></table>

that the 100 TeV FCC, with a combination of the increased energy and luminosity, can push further forward precision measurements with the  $t\bar{t}h$  channel. Instead of focusing on the semi-leptonic top pair mode, as in ref. [32], we explore the di-leptonic  $t\bar{t}h$  system. In addition to the extra background suppression, this channel provides a better probe to the top polarization, using the charged leptons. The larger spin analyzing power associated with the charged leptons results in the stronger CP-violation observables, such as  $\Delta \phi_{\ell \ell}^{t\bar{t}}$ , strengthening our CP-sensitivity.

We begin our discussion with the fat-jet invariant mass  $m_J^{\mathrm{BDRS}}$  distribution for the signal and background samples at the 100 TeV FCC-hh with 30 ab $^{-1}$  of data as shown in figure 7 (for the full hadron level analysis). Note the  $\mathcal{O}(10^{3})$  fold enhancement in event rate compared to that in figure 2 for the 14 TeV. The full stacked histogram is presented in black. CP sensitive angular variables are shown in figure 8, where we present distributions of  $\theta^{*}$  (left),  $\Delta \phi_{\ell \ell}^{\mathrm{lab}}$  (middle), and  $\Delta \phi_{\ell \ell}^{tt}$  (right) at both 14 TeV and 100 TeV for comparison. In the laboratory frame,  $\Delta \phi_{\ell \ell}^{\mathrm{lab}}$  distributions look similar, while  $\theta^{*}$  and  $\Delta \phi_{\ell \ell}^{tt}$  tend to be slightly forward or backward in the  $t\bar{t}$  rest frame. However, the ratio of new physics contribution to the SM prediction remains similar, as shown in the bottom of each panel.

![](images/659a764ea1e377a906f00bc3cf2003e3604704f69b971762eb9adf93fa431348.jpg)  
Figure 8. Comparisons between 14 TeV and 100 TeV distributions of  $\theta^{*}$  (left),  $\Delta \phi_{\ell \ell}^{\mathrm{lab}}$  (middle), and  $\Delta \phi_{\ell \ell}^{t\bar{t}}$  (right) after resolving the combinatorial problems described in table 1 and table 2, respectively.

![](images/9e4999ec5b5780489a7202635929bf2eee0d19eea17e99b69563c660cfe569e0.jpg)

![](images/94ab9272e139627b31c0ea99e18e5ed287f4b32a3c1ecf89bb677fbd82c32294.jpg)

![](images/7ef5eb207509e30dacdeb4ca52551c30ad67482c54b3a28222b663541a758822.jpg)  
Figure 9. The precision on  $\kappa_{t}$  assuming  $\alpha = 0$  at  $\sqrt{s} = 14\mathrm{TeV}$  (left) and  $\sqrt{s} = 100\mathrm{TeV}$  (right), using binned log-likelihood method.  $20\%$  systematics for  $t\bar{t}b\bar{b}$  and  $10\%$  systematics for  $t\bar{t}h$  and  $t\bar{t}z$  are assumed. For dashed curves, the uncertainties for  $t\bar{t}h$  and  $t\bar{t}z$  are assumed to be correlated.

![](images/d59c4084dd1eff296e32c06d8cce689799fa63dfad475826dbd3badef8f26229.jpg)

As mentioned previously, one main difference between 14 TeV LHC and 100 TeV FCC is the significant increase in the rate of signal and backgrounds. Especially both  $t\bar{t}h$  and  $t\bar{t}Z$  (i) result in hugely improved statistics, (ii) have similar production mechanisms, and (iii) probe comparable energy scales. Hence, their uncertainties are highly correlated [32]. The theoretical uncertainties in the signal cross-section, that are in the range 7-10% at 100 TeV collider, can be depleted to  $\delta \kappa_t \lesssim 1\%$  in terms of a ratio measurement [32]. This reduction of the uncertainties is also depicted in figure 9 for the 14 TeV LHC (left) and the 100 TeV FCC (right), where we only consider the precision on the  $\kappa_t$  measurement by fixing  $\alpha = 0$ . We considered two different scenarios: (1) binned log-likelihood (red-solid); and (2) binned log-likelihood with  $t\bar{t}h$  and  $t\bar{t}Z$  correlated in uncertainties (red-dashed). At the 14 TeV LHC, whether we consider the correlation between the uncertainties of  $t\bar{t}h$  and  $t\bar{t}Z$  (i.e. we use the same nuisance parameter for the uncertainties of  $t\bar{t}h$  and  $t\bar{t}Z$ ), does not significantly affect the results, as the uncertainties are dominated by the continuum

![](images/4b7454e72eac291b770265d4899975ba41576aef4190ae90ac0992968e35a3f2.jpg)  
Figure 10.  $68\%$  (red) and  $95\%$  (green) CL limits on the  $\alpha -\kappa_{t}$  plane for the 100 TeV FCC with  $30\mathrm{ab}^{-1}$  without (left) and with (right)  $\Delta \phi_{\ell \ell}^{t\bar{t}}$ . For the solid curves,  $10\%$  systematics is used for both  $t\bar{t} h$  and  $t\bar{t} Z$  individually, while for the dashed curves, the uncertainties for  $t\bar{t} h$  and  $t\bar{t} Z$  are assumed to be correlated.  $20\%$  systematics is used for  $t\bar{t} b\bar{b}$  for both scenarios.

![](images/9f832dce2c79b14651debe277700899355cb5ffccfbfa0520f8c950add90dfc1.jpg)

$t\bar{t}b\bar{b}$  background. However, the situation improves dramatically at the 100 TeV FCC. $^{1}$  The scenario (1) is systematically limited around  $\delta \kappa_{t} \lesssim 5\%$  due to the  $10\%$  systematics on the rate of the  $t\bar{t}h$ . When considering the correlation between  $t\bar{t}h$  and  $t\bar{t}Z$  in scenario (2), the  $\kappa_{t}$  measurement improves and can reach sub-percentage precision. Note that our results for  $\kappa_{t}$  at a 100 TeV collider,  $\delta \kappa_{t} \lesssim 0.5 - 0.7\%$ , are consistent with those from ref. [32], that explores the semi-leptonic top pair final state.

In light of the aforementioned improvements on the  $\kappa_{t}$  sensitivity, we perform a similar analysis considering both  $\kappa_{t}$  and  $\alpha$ . With the uplifted cross-section and enlarged luminosity, the 100 TeV FCC can boost the sensitivities on  $(\alpha, \kappa_{t})$ , using the binned log-likelihood method, as summarized in figure 10. We choose a wide mass window,  $m_{\mathrm{BDRS}} \in [50,150]\mathrm{GeV}$  for better control of the continuum  $t\bar{t}b\bar{b}$  background, along with  $\theta^{*}$  in the left panel. In both panels, the solid curves correspond to the case with  $20\%$  systematics for  $t\bar{t}b\bar{b}$  and  $10\%$  systematics for  $t\bar{t}h$  and  $t\bar{t}Z$ , while we assume  $t\bar{t}h$  and  $t\bar{t}Z$  uncertainties are correlated for the dashed curves. It is clear that, at a high luminosity, the solid curves are limited by the systematic uncertainties, similarly to the solid red line scenario in the right panel of figure 9. However, by assuming that the systematics of  $t\bar{t}h$  is correlated with  $t\bar{t}Z$ , the precision can be improved, as shown by the dashed curves, which can achieve  $\delta \kappa_{t} \lesssim 1\%$  and  $|\alpha| \lesssim 3^{\circ}$  at  $95\%$  CL.

Finally, extending the analysis to the  $(m_J^{\mathrm{BDRS}},\theta^*,\Delta \phi_{\ell \ell}^{t\bar{t}})$  plane, we find that the CP-odd observable  $\Delta \phi_{\ell \ell}^{t\bar{t}}$  brings additional improvement on the measurement of  $\alpha$  by a factor of 2,  $|\alpha |\lesssim 1.5^{\circ}$ , as shown in the right panel of figure 10, which highlights the importance of the CP-odd observable in the  $t\bar{t}$  rest frame.

# 5 Summary

The discovery of the Higgs boson at the LHC jump-started a comprehensive program of precision measurements for the Higgs couplings. In this context, the direct measurement of the Higgs-top coupling strength and CP-phase would have a significant impact on our understanding of the Yukawa sector and possible new sources of CP violation. In this paper, we have examined the direct probe of the top quark Yukawa coupling and the Higgs-top CP-structure in the  $t\bar{t}h$  production, with the Higgs boson decaying to a bottom pair and top-quarks in the di-leptonic mode. We have utilized several state-of-the-art strategies to reconstruct the final state with the missing transverse momentum and to control systematic uncertainties. We take advantage of the BDRS algorithm to tag the boosted Higgs, and exploit the  $M_2$ -assisted reconstruction to compute observables sensitive to the CP-phase at the  $t\bar{t}$  rest frame. Our log-likelihood analysis, using the side-band control region, takes full advantage of the shape information of the signal and background. We have shown that the proposed analysis significantly reduces the uncertainty in the CP-phase measurement and the Higgs-top Yukawa coupling. Our results show that the Higgs-top CP-phase  $(\alpha)$  can be probed up to  $|\alpha| \lesssim 36^\circ$  and the top Yukawa  $(\kappa_t)$  up to  $\sim 20\%$  accuracy (95% CL) at the HL-LHC, as shown in figure 4. A similar analysis at a 100 TeV future collider further improves the precision on the coupling modifier and CP-phase to  $\delta \kappa_t \lesssim 1\%$  and  $|\alpha| \lesssim 3^\circ$ , respectively, as shown in figure 10. We find that the CP-odd observable  $\Delta \phi_{\ell \ell}^{t\bar{t}}$  augments the precision by a factor of 2,  $|\alpha| \lesssim 1.5^\circ$ . We note these limits represent only an upper bound, that can be further enhanced via the combination of the other relevant top-quark and Higgs decays from the  $t\bar{t}h$  production.

# Acknowledgments

We thank Joseph Haley, Youngjoon Kwon, and Yue Xu for useful discussion on the control regions. DG and YW thank the U.S. Department of Energy for the financial support, under grant number DE-SC 0016013. KK acknowledges support from the US DOE, Office of Science under contract DE-SC0021447. JK is supported by the National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIT) (No. 2021R1C1C1005076).

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] A.D. Sakharov, Violation of CP Invariance,  $C$  asymmetry, and baryon asymmetry of the universe, Pisma Zh. Eksp. Teor. Fiz. 5 (1967) 32.  
[2] W. Buchmüller and D. Wyler, Effective Lagrangian Analysis of New Interactions and Flavor Conservation, Nucl. Phys. B 268 (1986) 621 [INSPIRE].  
[3] B. Grzadkowski, M. Iskrzynski, M. Misiac and J. Rosiek, Dimension-Six Terms in the Standard Model Lagrangian, JHEP 10 (2010) 085 [arXiv:1008.4884] [INSPIRE].

[4] M.R. Buckley and D. Goncalves, Boosting the Direct CP Measurement of the Higgs-Top Coupling, Phys. Rev. Lett. 116 (2016) 091801 [arXiv:1507.07926] [INSPIRE].  
[5] J. Brod, U. Haisch and J. Zupan, Constraints on CP-violating Higgs couplings to the third generation, JHEP 11 (2013) 180 [arXiv:1310.1385] [INSPIRE].  
[6] M.J. Dolan, P. Harris, M. Jankowiak and M. Spannowsky, Constraining CP-violating Higgs Sectors at the LHC using gluon fusion, Phys. Rev. D 90 (2014) 073008 [arXiv:1406.3322] [INSPIRE].  
[7] C. Englert, D. Goncalves-Netto, K. Mawatari and T. Plehn, Higgs Quantum Numbers in Weak Boson Fusion, JHEP 01 (2013) 148 [arXiv:1212.0843] [INSPIRE].  
[8] F.U. Bernlochner et al., Angles on CP-violation in Higgs boson interactions, Phys. Lett. B 790 (2019) 372 [arXiv:1808.06577] [INSPIRE].  
[9] C. Englert, P. Galler, A. Pilkington and M. Spannowsky, Approaching robust EFT limits for CP-violation in the Higgs sector, Phys. Rev. D 99 (2019) 095007 [arXiv:1901.05982] [INSPIRE].  
[10] A.V. Gritsan, J. Roskes, U. Sarica, M. Schulze, M. Xiao and Y. Zhou, New features in the JHU generator framework: constraining Higgs boson properties from on-shell and off-shell production, Phys. Rev. D 102 (2020) 056022 [arXiv:2002.09888] [INSPIRE].  
[11] H. Bahl et al., Indirect CP probes of the Higgs-top-quark interaction: current LHC constraints and future opportunities, JHEP 11 (2020) 127 [arXiv:2007.08542] [INSPIRE].  
[12] J. Ellis, D.S. Hwang, K. Sakurai and M. Takeuchi, Disentangling Higgs-Top Couplings in Associated Production, JHEP 04 (2014) 004 [arXiv:1312.5736] [INSPIRE].  
[13] F. Boudjema, R.M. Godbole, D. Guadagnoli and K.A. Mohan, Lab-frame observables for probing the top-Higgs interaction, Phys. Rev. D 92 (2015) 015019 [arXiv:1501.03157] [INSPIRE].  
[14] M.R. Buckley and D. Goncalves, Constraining the Strength and CP Structure of Dark Production at the LHC: the Associated Top-Pair Channel, Phys. Rev. D 93 (2016) 034003 [arXiv:1511.06451] [INSPIRE].  
[15] A.V. Gritsan, R. Röntsch, M. Schulze and M. Xiao, Constraining anomalous Higgs boson couplings to the heavy flavor fermions using matrix element techniques, Phys. Rev. D 94 (2016) 055023 [arXiv:1606.03107] [INSPIRE].  
[16] D. Goncalves and D. Lopez-Val, Pseudoscalar searches with dileptonic tops and jet substructure, Phys. Rev. D 94 (2016) 095005 [arXiv:1607.08614] [INSPIRE].  
[17] N. Mileo, K. Kiers, A. Szynkman, D. Crane and E. Gegner, Pseudoscalar top-Higgs coupling: exploration of CP-odd observables to resolve the sign ambiguity, JHEP 07 (2016) 056 [arXiv:1603.03632] [INSPIRE].  
[18] S. Amor Dos Santos et al., Probing the CP nature of the Higgs coupling in tth events at the LHC, Phys. Rev. D 96 (2017) 013004 [arXiv:1704.03565] [INSPIRE].  
[19] D. Azevedo, A. Onofre, F. Filthaut and R. Gonçalo, CP tests of Higgs couplings in tth semileptonic events at the LHC, Phys. Rev. D 98 (2018) 033004 [arXiv:1711.05292] [INSPIRE].  
[20] J. Li, Z.-g. Si, L. Wu and J. Yue, Central-edge asymmetry as a probe of Higgs-top coupling in  $t\overline{th}$  production at the LHC, Phys. Lett. B 779 (2018) 72 [arXiv:1701.00224] [INSPIRE].

[21] D. Gonçalves, K. Kong and J.H. Kim, Probing the top-Higgs Yukawa CP structure in dileptonic  $\bar{t} \bar{h}$  with  $M_2$ -assisted reconstruction, JHEP 06 (2018) 079 [arXiv:1804.05874] [INSPIRE].  
[22] ATLAS collaboration, Observation of Higgs boson production in association with a top quark pair at the LHC with the ATLAS detector, Phys. Lett. B 784 (2018) 173 [arXiv:1806.00425] [INSPIRE].  
[23] CMS collaboration, Observation of ttH production, Phys. Rev. Lett. 120 (2018) 231801 [arXiv:1804.02610] [INSPIRE].  
[24] B. Bortolato, J. F. Kamenik, N. Košnik and A. Smolkovič, Optimized probes of CP-odd effects in the tth process at hadron colliders, Nucl. Phys. B 964 (2021) 115328 [arXiv:2006.13110] [INSPIRE].  
[25] Q.-H. Cao, K.-P. Xie, H. Zhang and R. Zhang, A New Observable for Measuring CP Property of Top-Higgs Interaction, Chin. Phys. C 45 (2021) 023117 [arXiv:2008.13442] [INSPIRE].  
[26] R. Mammen Abraham, D. Gonçalves, T. Han, S.C.I. Leung and H. Qin, Directly probing the Higgs-top coupling at high scales, Phys. Lett. B 825 (2022) 136839 [arXiv:2106.00018] [INSPIRE].  
[27] ATLAS collaboration, CP Properties of Higgs Boson Interactions with Top Quarks in the  $t\bar{t}H$  and  $tH$  Processes Using  $H \rightarrow \gamma \gamma$  with the ATLAS Detector, Phys. Rev. Lett. 125 (2020) 061802 [arXiv:2004.04545] [INSPIRE].  
[28] CMS collaboration, Measurements of ttH Production and the CP Structure of the Yukawa Interaction between the Higgs Boson and Top Quark in the Diphoton Decay Channel, Phys. Rev. Lett. 125 (2020) 061801 [arXiv:2003.10866] [INSPIRE].  
[29] M. Cepeda et al., Report from Working Group 2: Higgs Physics at the HL-LHC and HE-LHC, CERN Yellow Rep. Monogr. 7 (2019) 221 [arXiv:1902.00134] [INSPIRE].  
[30] ATLAS collaboration, Search for the standard model Higgs boson produced in association with top quarks and decaying into a bb pair in pp collisions at  $\sqrt{s} = 13$  TeV with the ATLAS detector, Phys. Rev. D 97 (2018) 072016 [arXiv:1712.08895] [INSPIRE].  
[31] CMS collaboration, Search for ttH production in the H → bb decay channel with leptonic tt decays in proton-proton collisions at  $\sqrt{s} = 13$  TeV, JHEP 03 (2019) 026 [arXiv:1804.03682] [INSPIRE].  
[32] M.L. Mangano, T. Plehn, P. Reimitz, T. Schell and H.-S. Shao, Measuring the Top Yukawa Coupling at 100 TeV, J. Phys. G 43 (2016) 035001 [arXiv:1507.08169] [INSPIRE].  
[33] W. Bernreuther and Z.-G. Si, Distributions and correlations for top quark pair production and decay at the Tevatron and LHC, Nucl. Phys. B 837 (2010) 90 [arXiv:1003.3926] [INSPIRE].  
[34] M. Burns, K. Kong, K.T. Matchev and M. Park, Using Subsystem MT2 for Complete Mass Determinations in Decay Chains with Missing Energy at Hadron Colliders, JHEP 03 (2009) 143 [arXiv:0810.5576] [INSPIRE].  
[35] A.J. Barr et al., Guide to transverse projections and mass-constraining variables, Phys. Rev. D 84 (2011) 095031 [arXiv:1105.2977] [INSPIRE].  
[36] D. Debnath, D. Kim, J.H. Kim, K. Kong and K.T. Matchev, Resolving Combinatorial Ambiguities in Dilepton  $t\bar{t}$  Event Topologies with Constrained  $M_2$  Variables, Phys. Rev. D 96 (2017) 076005 [arXiv:1706.04995] [INSPIRE].  
[37] D. Kim, K.T. Matchev, F. Moortgat and L. Pape, Testing Invisible Momentum Ansatze in Missing Energy Events at the LHC, JHEP 08 (2017) 102 [arXiv:1703.06887] [INSPIRE].

[38] C.G. Lester and D.J. Summers, Measuring masses of semiinvisibly decaying particles pair produced at hadron colliders, Phys. Lett. B 463 (1999) 99 [hep-ph/9906349] [INSPIRE].  
[39] G.G. Ross and M. Serna, Mass determination of new states at hadron colliders, Phys. Lett. B 665 (2008) 212 [arXiv:0712.0943] [INSPIRE].  
[40] W.S. Cho et al., On-shell constrained  $M_2$  variables with applications to mass measurements and topology disambiguation, JHEP 08 (2014) 070 [arXiv:1401.1449] [INSPIRE].  
[41] P. Baringer, K. Kong, M. McCaskey and D. Noonan, Revisiting Combinatorial Ambiguities at Hadron Colliders with  $M_{T2}$ , JHEP 10 (2011) 101 [arXiv:1109.1563] [INSPIRE].  
[42] W.S. Cho et al., OPTIMASS: A Package for the Minimization of Kinematic Mass Functions with Constraints, JHEP 01 (2016) 026 [arXiv:1508.00589] [INSPIRE].  
[43] FCC collaboration, FCC Physics Opportunities: Future Circular Collider Conceptual Design Report Volume 1, Eur. Phys. J. C 79 (2019) 474 [INSPIRE].  
[44] J. Alwall et al., The automated computation of tree-level and next-to-leading order differential cross sections, and their matching to parton shower simulations, JHEP 07 (2014) 079 [arXiv:1405.0301] [INSPIRE].  
[45] T. Sjöstrand, S. Mrenna and P.Z. Skands, PYTHIA 6.4 Physics and Manual, JHEP 05 (2006) 026 [hep-ph/0603175] [INSPIRE].  
[46] P. Artoisenet, R. Frederix, O. Mattelaer and R. Rietkerk, Automatic spin-entangled decays of heavy resonances in Monte Carlo simulations, JHEP 03 (2013) 015 [arXiv:1212.3460] [INSPIRE].  
[47] J.M. Butterworth, A.R. Davison, M. Rubin and G.P. Salam, Jet substructure as a new Higgs search channel at the LHC, Phys. Rev. Lett. 100 (2008) 242001 [arXiv:0802.2470] [INSPIRE].  
[48] T. Plehn, G.P. Salam and M. Spannowsky, Fat Jets for a Light Higgs, Phys. Rev. Lett. 104 (2010) 111801 [arXiv:0910.5472] [INSPIRE].  
[49] M. Cacciari, G.P. Salam and G. Soyez, FastJet User Manual, Eur. Phys. J. C 72 (2012) 1896 [arXiv:1111.6097] [INSPIRE].  
[50] ATLAS collaboration, Technical Design Report for the ATLAS Inner Tracker Pixel Detector, CERN-LHCC-2017-021, ATLAS-TDR-030 (2017).  
[51] ATLAS collaboration, Jet mass and substructure of inclusive jets in  $\sqrt{s} = 7$  TeV pp collisions with the ATLAS experiment, JHEP 05 (2012) 128 [arXiv:1203.4606] [INSPIRE].  
[52] F. Demartin, F. Maltoni, K. Mawatari, B. Page and M. Zaro, Higgs characterisation at NLO in QCD: CP properties of the top-quark Yukawa interaction, Eur. Phys. J. C 74 (2014) 3065 [arXiv:1407.5089] [INSPIRE].  
[53] F. Demartin, F. Maltoni, K. Mawatari and M. Zaro, Higgs production in association with a single top quark at the LHC, Eur. Phys. J. C 75 (2015) 267 [arXiv:1504.00611] [INSPIRE].  
[54] CMS collaboration, Observation of a New Boson at a Mass of 125 GeV with the CMS Experiment at the LHC, Phys. Lett. B 716 (2012) 30 [arXiv:1207.7235] [INSPIRE].  
[55] ATLAS collaboration, *Measurements of WH and ZH production in the H → bb decay channel in pp collisions at 13 TeV with the ATLAS detector*, Eur. Phys. J. C **81** (2021) 178 [arXiv:2007.02873] [INSPIRE].