PAPER

# XQC and CSR constraints on strongly interacting dark matter with spin and velocity dependent cross sections

To cite this article: Yonglin Li et al JCAP05(2023)060

View the article online for updates and enhancements.

# You may also like

- Measuring the Density Fields around Bright Quasars at z 6 with XQR-30 Spectra  
Huanqing Chen, Anna-Christina Eilers, Sarah E. I. Bosman et al.  
- An improved Q-learning algorithm (XQL) for mobile robot path planning in unknown environments  
Yadong Chen, Hongyu Xu, Yunjie Zhang et al.  
- No Redshift Evolution in the Fe ii/Mg ii Flux Ratios of Quasars across Cosmic Time Danyang Jiang, Masafusa Onoue, Linhua Jiang et al.

# XQC and CSR constraints on strongly interacting dark matter with spin and velocity dependent cross sections

Yonglin Li, $^{a}$  Zuowei Liu $^{a,b}$  and Yilun Xue $^{a}$

$^{a}$ Department of Physics, Nanjing University, Nanjing 210093, China  
$^{b}$ CAS Center for Excellence in Particle Physics, Beijing 100049, China

E-mail: DZ20220015@smail.nju.edu.cn, zuoweliu@nju.edu.cn, mg1722018@smail.nju.edu.cn

Received November 10, 2022

Revised March 6, 2023

Accepted April 28, 2023

Published May 31, 2023

Abstract. Dark matter that interacts strongly with baryons can avoid the stringent dark matter direct detection constraints, because, like baryons, they are likely to be absorbed when traversing the rocks, leading to a suppressed flux in deep underground labs. Such strongly interacting dark matter, however, can be probed by dark matter experiments or other experiments operated on the ground level or in the atmosphere. In this paper we carry out systematic analysis of two of these experiments, XQC and CSR, to compute the experimental constraints on the strongly interacting dark matter in the following three scenarios: (1) spin-independent and spin-dependent interactions; (2) different velocity dependent cross sections; (3) different dark matter mass fractions. Some of the scenarios are first analyzed in the literature. We find that the XQC exclusion region has some non-trivial dependencies on the various parameters and the limits in the spin-dependent case is quite different from the spin-independent case. A peculiar region in the parameter space, where the XQC constraint disappears, is also found in our Monte Carlo simulations. This occurs in the case where the interaction cross section is proportional to the square of the velocity. We further compare our XQC and CSR limits to other experimental constraints, and find that a large parameter space is allowed by various experiments if the dark matter mass fraction is sufficiently small,  $f_{\chi} \lesssim 10^{-4}$ .

Keywords: dark matter simulations, dark matter theory

ArXiv ePrint: 2209.04387

# Contents

1 Introduction 1  
2 DM models 2

2.1 DM-nuclear interaction 2  
2.2 Velocity-dependent cross section 3  
2.3 Mass fraction 3

3XQC constraints on DM 3

3.1 MC simulation on XQC 4  
3.2 XQC data and  $\chi^2$  analysis 6

4 XQC constraints on velocity-dependent cross section 6

4.1 The  $n = 2$  case 7  
4.2 The lower boundary in the  $n = -4$  case 7  
4.3 The upper boundary in the  $n = -4$  case 8

5XQC constraints on SI cross sections 9  
6 XQC constraints on SD cross sections 10  
7 Constraints from CSR experiment 11

7.1 The lower boundary of the CSR exclusion region 12  
7.2 The upper boundary of the CSR exclusion region 12

8 Comparison of XQC and CSR limits to other experimental limits 12  
9 Summary 15

A Nucleus with spin 16  
B DM velocity after scattering 16  
C XQC data 17  
D The number of DM particles inside the FoV of XQC 17

E DM energy loss through an overburden 17

E.1 The upper boundary of the XQC exclusion region 18  
E.2 The allowed band in the  $n = 2$  case 18

F Atmosphere model 20  
G Thermalization efficiency 20

# 1 Introduction

Although the experimental evidence of dark matter (DM) is overwhelming, the property of DM still remains unknown. Particle DM is perhaps the most elegant way to address the various experimental observations on DM. Currently, there are several ways to decoding the nature of the particle DM: DM direct detection, DM indirect detection, and collider searches. In past decades, underground DM direct detection experiments have made great progress, for example, the Xenon-target DM direct detection experiments have probed the spin-independent (SI) DM-proton cross section down to  $10^{-46}\mathrm{cm}^2$  [1, 2]. However, the interaction cross section constrained by such underground experiments have a "ceiling", above which DM particles are shielded by the rocks on top of the underground labs, or even the atmosphere, so that they are not constrained by DM underground experiments. Such DM is often referred to as "strongly interacting dark matter" (SIDM). Although SIDM cannot be constrained by underground DM direct detection experiments, there are ground based DM experiments and experiments operated in the atmosphere that can probe SIDM: the XQC rocket experiment [3], the CRESST surface run [4], the EDELWEISS-Surf run [5], the RRS balloon experiment [6], and satellite experiments [7].

Although the XQC experiment was designed for X-ray spectroscopy, it can provide stringent constraints to SIDM [7-14]. The XQC exclusion contours have been computed for the spin-independent DM-nucleus cross section via Monte Carlo (MC) methods in ref. [10]; several rather sizeable mass fractions ( $f_{\chi} > 0.1$ ) have been considered in ref. [10]. The MC simulations can take into account multiple scatterings and thus can provide reliable constraints that cannot be easily derived via (semi-)analytic methods [10]. Recently the lower boundary of the XQC exclusion region has been re-analyzed by taking into account the DM particles that penetrate the aluminum body of the XQC rocket [11], leading to a slightly stronger limit in the mass range of [0.3, 100] GeV than in ref. [10], where DM are assumed to be completely shielded by the rocket body. The lower boundary of the XQC exclusion region for different velocity-dependent cross sections are computed in ref. [13]. Recently, the lower boundary of the XQC exclusion region has been re-scaled to estimate the constraints on different DM models: ref. [12] re-scaled the SI limits in ref. [11] to obtain the limits on spin-dependent (SD) cross sections; ref. [14] re-scaled the constrains in the mass range of [0.1, 100] GeV in ref. [13] to obtain the limits for different DM mass fractions; ref. [15] re-scaled the results in refs. [11, 13] to obtain constraints on Yukawa interactions.

We note that the recent XQC limits obtained via analytic methods in ref. [11] were only for a rather narrow mass range of  $[0.3, 100]\mathrm{GeV}$ . This is because analytic methods are based on the single scattering assumption between DM and the detector, which dominates in the mass range of  $[0.3, 100]\mathrm{GeV}$ . Outside this mass range, as multiple scatterings become important, analytic methods are no longer reliable. To extend the analysis in ref. [11] to DM mass of  $\sim 0.01\mathrm{GeV}$ , ref. [13] have used the MC methods, which can properly take into account multiple scatterings. Besides the DM mass  $\lesssim 0.3\mathrm{GeV}$ , we further find that the analytical method is not a good approximation for DM mass  $\gtrsim 10^{4}\mathrm{GeV}$  or for mass fraction  $\lesssim 10^{-3}$ . Because the analytic method used in refs. [11, 13] (as well as the re-scaling method used in refs. [12, 14, 15]) cannot be used in the entire XQC exclusion region, we use MC method in our analysis.

In this paper, we carry out detailed XQC MC simulations for different DM scenarios: (1) both SI and SD DM-nucleus cross sections; (2) different velocity-dependent DM-nucleus cross sections,  $\sigma \propto v^n$ ; (3) different DM mass fractions. Many XQC MC simulations in this paper

have not been analyzed previously, such as the upper boundary of the XQC exclusion region for the SD and velocity-dependent cross sections. We provide the first XQC simulations for the SD cross sections, which have been recently estimated by rescaling the previous limits in ref. [12]; our results for DM with  $100\%$  mass fraction are in good agreement with ref. [12]. We also provide XQC simulations for very small DM fractions, down to  $f_{\chi} = 10^{-5}$ . Our XQC MC simulations show that the upper boundary of the XQC exclusion region depends non-trivially on the mass fraction and on the velocity-dependence. We also find that for the velocity-dependent cross section with  $n = 2$ , there exists a large portion of parameter space allowed by the XQC data, which cannot be found by rescaling previous results.

The CSR upper bound on the DM-nucleon cross section in the mass range of [0.1, 10] GeV in the SI case is given in ref. [4]. The CSR exclusion region (including both the upper and lower boundaries) for DM mass less the  $1\mathrm{GeV}$  in the SI case is analyzed in ref. [16]. The upper boundary of the CSR exclusion region in the SI case is extended up to DM mass of  $10^{8}\mathrm{GeV}$  in ref. [17]. The CSR exclusion regions for both SI and SD cases are computed in ref. [12]. Recently, MC simulations have been used to more accurately determine the CSR exclusion regions [13, 18]. It is found that the upper boundary of CSR exclusion region for DM mass less than  $100\mathrm{GeV}$  in the SI case obtained in MC simulations in ref. [18] is in good agreement with refs. [16, 17], but is significantly higher than that in ref. [12]. The upper boundary of the CSR exclusion region for different velocity dependencies and mass fractions for DM mass less than  $100\mathrm{GeV}$  in the SI case are analyzed with MC simulations in ref. [13]. In our analysis, we compute the CSR exclusion region in both the SI and the SD cases for different mass fractions. In our analysis, we adopt methods that can yield consistent results to ref. [18], and thus provide more reliable CSR limits for both the SI and the SD cases than ref. [12].

The rest of the paper is organized as follows. In section 2 we introduce the three different DM scenarios considered in our analysis. In section 3 we introduce the Monte Carlo method to compute the XQC constraints. We then compute the XQC exclusion regions for DM with different velocity-dependent cross sections in section 4, for SI and SD DM with different mass fractions in section 5 and in section 6 respectively. In section 7 we introduce our method to compute the constraints on DM from the CSR experiment. In section 8 we compare the XQC and CSR limits in our analysis with various different experimental constraints. We summarize our findings in section 9. We further provide some detailed calculations in the appendix.

# 2 DM models

In this analysis we consider the following three DM scenarios:

- spin dependence: DM interacts with nucleus either via the spin-independent cross section or via the spin-dependent cross section.  
- mass fraction: the DM component of interest is only a sub-component of the whole DM in the universe.  
- velocity dependence: the DM-nucleus interaction cross section depends strongly on the relative velocity.

# 2.1 DM-nuclear interaction

The interaction between DM and nucleus is usually classified into two different types: spin-independent (SI) and spin-dependent (SD) interactions. For these two interactions, the

DM-nucleus cross section is related to the DM-proton cross section via [12]

$$
\sigma_ {\chi N} = \sigma_ {\chi p} \left(\frac {\mu_ {\chi N}}{\mu_ {\chi p}}\right) ^ {2} \times \left\{ \begin{array}{c c} {\left[ Z + \frac {f _ {n}}{f _ {p}} (A - Z) \right] ^ {2}} & (\mathrm {S I}), \\ {\left[ \langle S _ {p} \rangle + \frac {f _ {n}}{f _ {p}} \langle S _ {n} \rangle \right] ^ {2} \frac {4}{3} \frac {J _ {A} + 1}{J _ {A}}} & (\mathrm {S D}), \end{array} \right. \tag {2.1}
$$

where  $\sigma_{\chi N}(\sigma_{\chi p})$  is the DM-nucleus (DM-proton) cross section,  $\mu_{\chi N}(\mu_{\chi p})$  is the reduced mass of the DM-nucleus (DM-proton) system,  $f_{p}(f_{n})$  is the DM-proton (DM-neutron) coupling,  $Z(A)$  is the proton (atomic) number of the nucleus  $N$ ,  $J_{A}$  is the spin of the nucleus  $N$ , and  $\langle S_p\rangle$  and  $\langle S_n\rangle$  are the average spin of proton and neutron respectively in  $N$ . For the SD interaction, only the nucleus with  $\mathrm{spin}^1$  can participate in the scattering with DM. See appendix A for the list of the nuclei with spin considered in this analysis. We note that the scaling relations given in eq. (2.1) may fail for very large DM-nucleus interaction cross sections [15, 20]. For the sake of comparison with different detector targets, we use the scaling relations in eq. (2.1) throughout our analysis. However, one should interpret the very large cross section region in a model-dependent manner to ensure the validity of the Born approximation which is needed to derive the scaling relation [15, 20].

# 2.2 Velocity-dependent cross section

We consider DM models in which the DM-proton cross section can be parameterized as

$$
\sigma_ {\chi p} = \sigma_ {\chi p} ^ {0} v ^ {n}, \tag {2.2}
$$

where  $\sigma_{\chi p}^{0}$  is velocity-independent. In our analysis, we work with phenomenological models and consider the  $n = \{0,2, - 2, - 4\}$  cases. There are some well-motivated realizations of the various velocity dependencies. For example, millicharged DM scatters with the nucleus via a t-channel photon, which results in an interaction cross section proportional to  $v^{-4}$ ; for recent studies on millicharged DM, see e.g., refs. [21-40]. The  $n = \pm 2$  case can arise in dipole DM models [9]. For a variety of velocity-dependent cross sections in the non-relativistic limit, see e.g., ref. [41].

# 2.3 Mass fraction

We consider DM models in which SIDM is only a sub-component DM. Typically, the direct detection limits is inversely proportional to the DM mass fraction  $f_{\chi}$ , since the direct detection signal is linearly dependent on the number of DM particles. However, the upper boundary of the direct detection exclusion region has non-trivial dependence on the mass fraction.

# 3 XQC constraints on DM

XQC (the X-ray Quantum Calorimetry experiment), the rocket experiment originally designed to detect the diffuse X-ray in the range of  $60 - 1000\mathrm{eV}$  [3], can also place leading constraints to strongly interacting DM [10, 13]. XQC was launched in 1999 and collected data at  $165 - 225\mathrm{km}$  above Earth's surface for 100.7s [3, 10].

The detector of the XQC experiment consists of 36 quantum calorimeters with 34 active during the data-taking. Each calorimeter consists of a  $0.5\mathrm{mm} \times 2\mathrm{mm} \times 0.96\mu \mathrm{m}$  HgTe

deposited on a  $0.5\mathrm{mm} \times 2\mathrm{mm} \times 14\mu \mathrm{m}$  silicon substrate. In our Monte Carlo analysis we neglect the effects of HgTe and only consider the effects of silicon in the detector. The FoV of the XQC experiment is 1 sr which is centered at  $(\ell, b) = (90^{\circ}, 60^{\circ})$  in the galactic coordinate system [10]. There are five filters, located at  $2\mathrm{mm}$ ,  $6\mathrm{mm}$ ,  $9\mathrm{mm}$ ,  $11\mathrm{mm}$  and  $28\mathrm{mm}$  above the detectors, which are intended to block the long wavelength radiation for its designed experimental goal [3]. Each filter consists of a  $150\AA$  aluminum supported on a  $1380\AA$  parylene substrate.

# 3.1 MC simulation on XQC

To compute the XQC constraints on DM, we carry out MC simulations in the following three steps.

- Step 1. We first select DM particles with velocity in the FoV of XQC, which is 1 sr centered at  $(\ell, b) = (90^{\circ}, 60^{\circ})$ , where  $\ell$  ( $b$ ) is the longitude (latitude) in the galactic coordinate system. We use a truncated Boltzmann distribution [42, 43] for DM in the halo frame

$$
f (v) = \frac {1}{N} e ^ {- v ^ {2} / v _ {0} ^ {2}} \theta \left(v _ {\mathrm {e s c}} - v\right), \tag {3.1}
$$

where  $v$  is the DM velocity in the halo frame,  $v_{0}$  is the average velocity of DM,  $v_{\mathrm{esc}}$  is the escape velocity,  $\theta (v)$  is the Heaviside function, and  $N = \pi v_0^3 [\sqrt{\pi}\mathrm{Erf}(a) - 2ae^{-a^2}]$  is the normalization factor with  $a = v_{\mathrm{esc}} / v_0$ . We take  $v_{0} = 220\mathrm{km / s}$  and  $v_{\mathrm{esc}} = 587\mathrm{km / s}$  [10]. The total number of DM particles that are inside the FoV on the surface of the top filter during the XQC data-taking is given by

$$
N _ {\chi} \simeq 7. 3 2 \times 1 0 ^ {8} f _ {\chi} \frac {\mathrm {G e V}}{m _ {\chi}}, \tag {3.2}
$$

where we have used  $S \simeq 7.1\mathrm{cm}^2$  for the area of the filter. See appendix D for the derivation of eq. (3.2).

- Step 2. We then let DM with the correct velocity traverse the five filters and the detector. Each filter consists of a  $15\mathrm{nm}$  Al layer with mass density  $\rho_{\mathrm{Al}} \simeq 2.7\mathrm{g/cm^3}$  and a  $138\mathrm{nm}$  parylene layer with mass density  $\rho_{\mathrm{CH}} \simeq 1.1\mathrm{g/cm^3}$ . We assume equal composition of  $C$  and  $H$  in the parylene layer. The detector is made of Si with mass density  $\rho_{\mathrm{Si}} \simeq 2.33\mathrm{g/cm^3}$ . The mean free path  $\lambda$  of DM in the filter/detector is determined by

$$
\lambda = \left(\sum_ {A} n _ {A} \sigma_ {\chi A}\right) ^ {- 1}, \tag {3.3}
$$

where  $n_A$  is the number density of the nucleus  $A$ , and  $\sigma_{\chi A}$  is the DM-A cross section. The summation is computed on all nuclei in the filter/detector. The distance traveled in each step is given by  $-\ln (1 - R)\lambda$ , where  $R$  is a random number between 0 and 1. The direction of the motion is given by the DM velocity. When there are multiple nuclei to interact with, the probability of DM scattering with nucleus A (in each step) is given by

$$
P (A) = \frac {n _ {A} \sigma_ {\chi A}}{\sum_ {B} n _ {B} \sigma_ {\chi B}}. \tag {3.4}
$$

- Step 3. For each given nucleus we compute the DM velocity with two random numbers for the polar angle and azimuthal angle in the CM frame. See appendix B for details. In our simulations, for simplicity, we assume that DM-nucleus cross sections are isotropic in the CM frame. Interaction cross sections with non-trivial angular distributions are beyond the scope of this analysis.

We repeat the simulation steps (1-3) as described above until one of the following conditions is satisfied: (1) The kinetic energy of DM falls below  $1\mathrm{eV}$ , or below  $29\mathrm{eV}$  (the lowest energy of XQC data bins) before reaching the detector; (2) the energy deposited in the detector exceeds  $4000\mathrm{eV}$  (the last XQC data bin has energy  $\geq 4000\mathrm{eV}$ ); (3) DM does not hit the detector/filter when reaching the detector/filter.

To facilitate the simulation, we use a  $8.5\mathrm{mm} \times 4\mathrm{mm} \times 14\mu \mathrm{m}$  cuboid to model the detector. The radius of the filters is taken to be  $1.5\mathrm{cm}$ , as inferred from the figure 1 of ref. [3]. For simulations near the lower boundary of the exclusion region, we do not consider the effects of the filters, because the probability of interacting with filters is small for these regions.

Recently, the lower boundary of the XQC exclusion region has been reanalyzed in the mass region of [0.3, 100] GeV by ref. [11] to take into account the probability of DM penetrating the aluminum shield (with a thickness of  $3.7\mathrm{cm}$ ) of the rocket, and in the mass region of [0.01, 100] GeV by ref. [13] to include the thermalization effects of the silicon detector. Because the thickness of the aluminum shield is smaller than the DM mean free path on the lower boundary of the XQC exclusion region in the mass range of  $\sim$  [0.3, 100] GeV, inclusion of DM penetrating the aluminum shield leads to a factor of few improvement on the XQC limits in that mass range [11, 13]. However, as one moves outside of the above mass range, the thickness of the aluminum shield quickly exceeds the DM mean free path so that DM can no longer penetrate the shield easily. Thus, we have neglected this effect in our MC simulations for the entire parameter space. As pointed out by ref. [13], the actual measured energy in the XQC silicon detector could be much smaller than the DM nuclear recoil energy. However, to our knowledge, the thermalization efficiency for silicon in the energy range of interest has not been measured. Thus, in the current analysis, we have not considered the effects due to the thermalization efficiency for most figures. To illustrate the effects of the thermalization efficiency, we have computed the XQC exclusion region adopting the three values of the thermalization efficiency in ref. [13], which are shown in figure 7. See appendix G for the detailed analysis.

We next discuss the effects due to DM particles that are captured by the Earth. As recently pointed out in ref. [44], the non-equilibrium component of DM captured by the Earth can be significantly larger than the equilibrium component near the surface of the Earth. We note that both the equilibrium and the non-equilibrium components are captured and thermalized, with the latter possessing a non-zero diffusion velocity. Because the velocity of the equilibrium component is less than the escape velocity of the Earth,  $v_{\mathrm{esc}}^E \simeq 11.2\mathrm{km / s}$  (near the surface), to produce a recoil energy above  $29\mathrm{eV}$  (the energy threshold of XQC), the DM mass has to be at least  $\sim 40\mathrm{GeV}$ . At such large DM mass, the density of the equilibrium component near the Earth surface is much smaller than the local DM density [44]. To estimate the effects of the non-equilibrium component of DM on our XQC analysis, we use eq. (E.5) to calculate the DM velocity at the XQC detector. Following ref. [44], we consider the atmosphere up to  $180\mathrm{km}$ . To simplify the calculation, we assume that the atmosphere is only composed of oxygen, and has a temperature of  $T = 700\mathrm{K}$  and a density of  $\rho = 9.75\times 10^{-10}\mathrm{kg / m^3}$  [45], at the altitude of  $165 - 180\mathrm{km}$ . The condition that DM is captured and thermalized by the

Earth is  $v_{\chi}^{f} \leq v_{\mathrm{esc}}^{E} = 11.2 \, \mathrm{km/s}$  and  $v_{\chi}^{f} \leq v_{\mathrm{th}} = \sqrt{8T/\pi m_{\chi}}$  where  $v_{\mathrm{th}}$  is the thermal velocity. We find that at the altitude of  $165 \, \mathrm{km}$ , the cross section needed to capture and thermalize DM are much larger than the upper boundary of XQC exclusion region. For example, the minimal cross sections to capture DM and to thermalize DM for a  $40 \, \mathrm{GeV}$  DM, are found to be  $\sigma_{\chi p} \sim 7.5 \times 10^{-21} \, \mathrm{cm}^2$  and  $\sigma_{\chi p} \sim 1.5 \times 10^{-20} \, \mathrm{cm}^2$  respectively. Thus, inside the XQC exclusion region, DM is not able to be captured and thermalized at the upper atmosphere due to its low density.

# 3.2 XQC data and  $\chi^2$  analysis

We use the XQC data from table 1 of ref. [10]. Following ref. [10] we carry out the following  $\chi^2$  analysis to compute the XQC exclusion region

$$
\chi^ {2} = \sum_ {i} \left\{\frac {\left(E _ {i} - U _ {i}\right) ^ {2}}{E _ {i}} \text {w i t h} U _ {i} <   E _ {i} \right\}, \tag {3.5}
$$

where  $i$  denotes the  $i$ -th data bin,  $E_{i}$  is the number of simulated events and  $U_{i}$  is the number of events in the XQC data. To compute  $E_{i}$  we also take into account the XQC detection efficiency: The detection efficiency of XQC is  $f = 0.3815$  (0.5083) for the first (second) energy bin, and  $f = 1$  for the other eleven high energy bins [10]. Here we use the one-side  $\chi^2$  because the background of the XQC experiment is unknown; thus we only consider the cases where the events that DM generate exceed the XQC data. The 90% CL exclusion region is then obtained by requiring  $\chi^2 = 2.71$ .

# 4 XQC constraints on velocity-dependent cross section

We compute XQC constraints on DM models in which the DM-proton cross section are velocity-dependent and can be parameterized as in eq. (2.2). Figure 1 shows the XQC constraints on DM models with  $n = \{0,2, - 2, - 4\}$  both for SI interaction and for SD interaction. To compare XQC constraints for different  $n$  values, we computed the excluded DM-proton cross section at  $v = 10^{-3}c$ . Figure 1 shows that most of the exclusion regions for the four different velocity dependencies overlap with each other. However, there are some noticeable differences among them: (i) the upper boundary of the exclusion region for heavy DM mass increases with  $n$ , with the  $n = 2$  case significantly higher than other cases; (ii) there exists a band-shape parameter space allowed by XQC in the  $n = 2$  case that is inside the XQC region, which can be parameterized as

$$
\log_ {1 0} \left[ \frac {\sigma_ {\chi p} (v = 1 0 ^ {- 3})}{\mathrm {c m} ^ {2}} \right] = k \log_ {1 0} \left[ \frac {m _ {\chi}}{\mathrm {G e V}} \right] - b, \tag {4.1}
$$

where  $k \simeq 2$  and  $b \simeq -26(-22.6)$  for the SI (SD) case. (iii) in the  $n = -4$  case, the lower boundary of the exclusion region is lower than other cases, and the upper boundary for low mass is higher than other cases.

We note that on the lower boundary of the XQC exclusion region, the scattering probability of DM with the detector is typically very small so that DM can only scatter with the detector once, and the scattering between DM and the 5 filters can be ignored (except for the very small mass region). However, on the upper boundary of the XQC exclusion region, the interaction cross section is so large that the scattering between DM and the 5 filters becomes very important.

![](images/587a56435c2bf4aa905ef85ece335e5713293772638cee66b2e57201b9fed3b5.jpg)  
Figure 1. The XQC exclusion region at the  $90\%$  CL in the parameter space spanned by the DM-proton cross section  $\sigma_{\chi p}$  evaluated at  $v = 10^{-3}$  and the DM mass  $m_{\chi}$ , both in the SI case (left) and in the SD case (right). Different velocity-dependent DM-p cross sections in the form of  $\sigma_{\chi p} = \sigma_{\chi p}^{0}v^{n}$ , where  $n = \{0,2, - 2, - 4\}$ , are indicated by different color-shaded regions.

![](images/625e3707733af19a647883f712382b5a1129bcf5deb51b40a44dae1f897d5c0e.jpg)

We note that, for the  $f_{\chi} = 1$  case, the upper boundary and a significant portion of the XQC exclusion region have been ruled out by the CMB and Lyman-  $\alpha$  constraints; see figure 4 for the comparison. Nonetheless, it is of importance to study the XQC constraints on various velocity-dependent cross sections, because CMB and Lyman-  $\alpha$  constraints are derived based on physics processes in the early universe, but XQC constraints are obtained in the current time. The underlying assumption of the comparisons between different experimental limits in figure 4 is that the particle identity and the mass fraction of DM do not change from the CMB epoch to the current time, which may not be true in a real cosmology model.

# 4.1 The  $n = 2$  case

For the  $n = 2$  case, there exists certain parameter space in which the kinetic energy of the DM particle after traversing the five filters is localized in a narrow energy range; see appendix E for more detailed discussions on the final kinetic energy distribution of DM. If the narrow energy range of the DM final kinetic energy falls inside [2505, 4000] eV, the disregarded XQC energy range, then there is no XQC constraints, which results in the band-shape parameter space in the  $n = 2$  case. If the narrow energy range of the final kinetic energy falls inside any other data bin, it can result in a much larger  $\chi^2$  than the case where the events are more evenly distributed among many data bins. This then gives rise to stronger constraints near the upper boundary of the XQC exclusion region in the  $n = 2$  case. We note that the two features of the XQC exclusion region in the  $n = 2$  case should also appear in  $n > 2$  cases.

# 4.2 The lower boundary in the  $n = -4$  case

We next discuss the lower boundary in the  $n = -4$  case. Because the DM-p cross section has a significant dependence on the velocity such that the cross section increases significantly when the velocity decreases. On the lower boundary of the exclusion region, the scattering probability of DM with the XQC detector is small so that DM particles with low velocity have more contributions to the interactions between DM and the detector. When evaluating the cross section at relatively large velocity, such as  $v = 10^{-3}$  as done in figure 1, one should

obtain a smaller cross section than the low velocity. This explains why the lower boundary of the XQC exclusion region in the  $n = -4$  case is lower than other cases.

# 4.3 The upper boundary in the  $n = -4$  case

We next discuss the upper boundary in the  $n = -4$  case. On the upper boundary of the XQC exclusion region, the interactions between DM and the 5 filters play a dominant role in determining the constraints. In our analysis, we assume an isotropic scattering cross section in the CM frame. For light DM  $(m_{\chi} \ll m_N)$ , because the lab frame is nearly the same as the CM frame, the scattering cross section between DM and the filters in the lab frame is also isotropic. Thus, large-angle scatterings can occur quite often and light DM are easily scattered outside of the XQC FoV during interactions with the filters. On the contrary, for heavy DM  $(m_{\chi} \gg m_N)$ , the lab frame is no longer the CM frame, and the scattering cross section is mostly forward in the lab frame. Thus, heavy DM particles mainly lose their kinetic energies via interactions with the filters, but keep the direction of motion nearly fixed.

We next compare the XQC upper boundary for the  $n = 0$  and  $n = -4$  cases. As shown in both panel figures in figure 1, for DM mass below (above)  $\sim 10^{3} \mathrm{GeV}$ , the upper boundary in the  $n = -4$  case is higher (lower) than the  $n = 0$  case. Below we discuss two benchmark DM masses: 1 GeV and  $10^{5} \mathrm{GeV}$ , to provide some qualitative understandings of this phenomenon. We first note that the number of DM particles of 1 GeV is  $10^{5}$  times larger than DM of  $10^{5} \mathrm{GeV}$ , since  $n \propto m_{\chi}^{-1}$ . For DM of 1 GeV, most DM particles are scattered outside of the XQC FoV via large-angle scatterings in the lab frame. On the contrary, for DM of  $10^{5} \mathrm{GeV}$ , most DM particles penetrate the filters to reach the detector (if they initially aim right at the detector). The upper boundary of the heavy DM is determined by the filters such that the DM kinetic energy after multiple scatterings with the filters is below the XQC threshold. Due to the different interactions between the filters and the DM, the mean free path of DM of 1 GeV is many times larger than DM of  $10^{5} \mathrm{GeV}$ .

We discuss the upper boundary for the low DM mass. In the  $n = 0$  case, the stopping effects are more or less the same for all DM velocity, since the interaction cross section is velocity independent. However, for the  $n = -4$  case, the stopping effects are significantly weakened for the high energy DM particles so that DM particles with high velocity has a higher probability to penetrate the 5 filters than those with low velocity. Thus, for the exclusion cross section (evaluated at  $v = 10^{-3}$ ) at the upper boundary of the  $n = 0$  case, DM particles of high velocity are absorbed by the filters in the  $n = 0$  case, but these DM particles in the  $n = -4$  case can penetrate the filters. Thus, one needs a larger cross section to stop these DM particles of high velocity in the  $n = -4$  case. Note DM particles that penetrate the filters on the upper boundary are likely to be absorbed by the detector, since the detector is about 100 times thicker than the 5 filters.

The situation for the heavy DM is a little complicated. Most DM particles penetrate the filters with reduced velocities; for the  $n = -4$  case, the DM of high velocity receives a relatively smaller reduction on the velocity than the  $n = 0$  case. Because the DM mass is very large, the kinetic energies of most DM particles are large such that they would result in events in the last XQC data bin,  $E > 4000\mathrm{eV}$ , since most of the kinetic energy is absorbed by the detector. For the  $n = -4$  case, because the interaction cross section at low DM velocity is much larger, the number of DM particles with low velocity are more easily to lose energy leading to more (less) events below (above) the XQC threshold. Therefore, with the same cross section, there are more events in the last XQC data bin in the  $n = 0$  case than the

$n = -4$  case, for DM of  $10^{5}\mathrm{GeV}$ . One then needs a larger cross section to reduce the velocity of the DM in the  $n = 0$  case in the heavy DM region.

# 5 XQC constraints on SI cross sections

We further compute the XQC exclusion region on the DM-proton cross section with different mass fractions. Figure 2 shows the XQC exclusion regions for the following mass fractions:  $f_{\chi} = \{1, 10^{-1}, 10^{-2}, 10^{-3}, 10^{-4}, 10^{-5}\}$ . The XQC exclusion region shrinks as the mass fraction decreases. The lower boundary and the right boundary of the XQC exclusion region have a strong dependence on the mass fraction  $f_{\chi}$ , whereas the upper boundary and the left boundary have a weak dependence on the mass fraction  $f_{\chi}$ .

As shown in figure 2, in the case where  $f_{\chi} = 10^{-5}$ , all the XQC exclusion regions become very small, which are expected to disappear if the mass fraction goes below  $f\simeq 10^{-6}$ . This is due to the fact that the number of DM particles inside the FoV is significantly small for such a small mass fraction so that there are not enough signal events to be excluded by XQC even if all DM particles are absorbed by the detector. The expected number of the DM particles that are inside the FoV of the XQC detector is (see appendix D for details)

$$
N _ {\chi} \simeq 3. 5 \times 1 0 ^ {7} f _ {\chi} \frac {\mathrm {G e V}}{m _ {\chi}}, \tag {5.1}
$$

where we have used the area of  $0.34\mathrm{cm}^2$  for the XQC detector. Thus if  $f_{\chi}\lesssim 10^{-6}$ $N_{\chi}\lesssim$  35  $(\mathrm{GeV} / m_{\chi})$  ; since the total number of events in the XQC data is  $\mathcal{O}(500)$  , there is no constraint when  $f_{\chi}\lesssim 10^{-6}$

For the lower boundary of the XQC exclusion region, the DM-p cross section  $\sigma_{\chi p}^{0}$  on the lower boundary is inversely proportional to the mass fraction  $f_{\chi}$ . This is because on the lower boundary, for a significant mass fraction such that the expected DM events  $N_{\chi}$  is much larger than  $\mathcal{O}(500)$ , the interaction probability between DM and the detector is very small, and it is a good approximation to assume that DM only interacts with the detector once when traversing the detector. Under the single-scattering assumption, the event rate on the lower boundary is thus proportional to the product of the interaction cross section and the mass fraction,  $R \propto \sigma_{\chi p} f_{\chi}$ . Thus the lower boundary of the XQC exclusion region is inversely proportional to the mass fraction  $f_{\chi}$ .

The right boundary of the XQC exclusion region is nearly vertical (namely independent of the cross section) for many cases, as shown in figure 2. This truncation arises because on the right-hand side of the vertical boundary, the number of DM particles that enter the XQC detector becomes less than the number of events observed in the last bin of the XQC data. The location of the right boundary, namely the DM mass, moves with the mass fraction such that the ratio  $f_{\chi} / m_{\chi}$  stays unchanged. This is due to the fact that the number of DM particles in the halo is inversely proportional to the DM mass. Thus the total number of DM particles remains constant on the right boundary if  $f_{\chi} / m_{\chi}$  is fixed. In the  $f_{\chi} = 1$  case, the DM mass is in the range of  $10^{5 - 6} \mathrm{GeV}$  on the right boundary. For such a large DM mass, the energy deposited by DM particles in the detector is typically in the last bin of the XQC data, namely the total deposit energy  $E_{R} \geq 4 \mathrm{keV}$ . Thus the right boundary of the XQC exclusion region is primarily determined by the number of events in the last bin of the XQC data, which is  $N = 60$ ; this is valid for  $f_{\chi} \gtrsim 10^{-3}$ , when  $m_{\chi} \gtrsim 100 \mathrm{GeV}$ .

In the literature it is often assumed that the upper and/or the left boundary of the XQC exclusion region do not change when the mass fraction decreases. However, as shown in

![](images/08d91ccfcdfeff52a27911aa26a423a8276629190e368c72d4010278d7e6ee6f.jpg)

![](images/725d808ac1271c3a8588450eb309c9b9c5ff9d62459fcedd940e9f84f17f05d0.jpg)

![](images/fb0a5e043d2037801a9c6084f7918b31b1efac14426a071c1fa048be93dcb185.jpg)  
Figure 2. The XQC exclusion region at the  $90\%$  CL in the SI case for different velocity-dependent DM-p cross sections in the form of  $\sigma_{\chi p} = \sigma_{\chi p}^{0}v^{n}$ :  $n = 0$  (upper-left),  $n = 2$  (upper-right),  $n = -2$  (lower-left),  $n = -4$  (lower-right). In each figure, different mass fractions are considered:  $f_{\chi} = 1$  (gray),  $f_{\chi} = 10^{-1}$  (steel-blue),  $f_{\chi} = 10^{-2}$  (blue),  $f_{\chi} = 10^{-3}$  (purple),  $f_{\chi} = 10^{-4}$  (brown),  $f_{\chi} = 10^{-5}$  (red).

![](images/8de383a155d8bf6128d7d5f1260f16f1964d84637b7e403b4b846c978c1c9bc3.jpg)

figure 2, the upper boundary and the left boundary do change as the mass fraction decreases. We note that the changes on the upper boundary and on the left boundary are less significant than the lower/right boundary. This is because on the left boundary the limit is set by requiring the kinetic energy of each DM particle to be below the XQC threshold,  $29\mathrm{eV}$ ; on the upper boundary the limit is set by requiring each DM particle to be absorbed by the filters.

# 6 XQC constraints on SD cross sections

In this section, we calculate the XQC exclusion region in the SD case. In the XQC filters, the nuclei with spin include  $^{27}\mathrm{Al}$ ,  $^{13}\mathrm{C}$ , and  $^{1}\mathrm{H}$ ; in the detector, the nucleus with spin is  $^{29}\mathrm{Si}$ . The natural abundance of  $^{27}\mathrm{Al}$  and  $^{1}\mathrm{H}$  are about  $100\%$ , and the natural abundance of  $^{13}\mathrm{C}$  and  $^{29}\mathrm{Si}$  are  $1.1\%$  and  $4.7\%$  respectively [46].

Figure 3 shows the XQC exclusion regions in the SD case with different mass fractions and different velocity-dependent cross sections. The lower boundary of the SD case is about  $10^{5}$  times larger than the SI case, as shown in figure 2; the shape of the lower boundary in the SD case is similar to the SI case. This is because on the lower boundary the probability of DM scattering with the detector is small and the probability of DM scattering with the filters is negligible. This rescaling of the limits are then deduced by the ratio between the SI

![](images/1dee955e7b4d381cfb5e73b86492aec84c8fb61ac6791ffcaf7dcca1beacb88a.jpg)

![](images/d2acf66253a3b2d1fcdc5b7faed1240a5a30dfacd2ed01b15810c535c2410d6f.jpg)

![](images/5a57109de5f72f7e8b3ed8474ae6017b775ad41828389c79bf6cc37a459c5d40.jpg)  
Figure 3. The XQC exclusion region at the  $90\%$  CL in the SD case for different velocity-dependent DM-p cross sections in the form of  $\sigma_{\chi p} = \sigma_{\chi p}^{0}v^{n}$ :  $n = 0$  (upper-left),  $n = 2$  (upper-right),  $n = -2$  (lower-left),  $n = -4$  (lower-right). In each figure, different mass fractions are considered:  $f_{\chi} = 1$  (gray),  $f_{\chi} = 10^{-1}$  (steel-blue),  $f_{\chi} = 10^{-2}$  (blue),  $f_{\chi} = 10^{-3}$  (purple),  $f_{\chi} = 10^{-4}$  (brown).

![](images/66524ae47267683bb5db1be37f3bbb81bf259d59c2bf7776c161d5dec316cffb.jpg)

and SD cross sections given in eq. (2.1) and the natural abundance of  $^{29}\mathrm{Si}$ , which together give rise to a factor of  $\sim 10^5$ . We note that the shape of the XQC exclusion region on the upper boundary in the SD case is also quite different from the SI case: for example in the  $n = 0$  case, the upper boundary at small DM mass is much smaller than heavy DM mass in the SD case, whereas in the SI case, they are comparable. We also note that the XQC exclusion region disappears when  $f_{\chi} \lesssim 10^{-5}$ .

# 7 Constraints from CSR experiment

CSR (CRESST surface run) is a ground-based experiment which used the cryogenic detector to detect the DM signal [4]. The CSR detector is made of  $\mathrm{Al_2O_3}$ , which has a size of  $5\times 5\times 5\mathrm{mm}^3$  and a mass of  $0.49\mathrm{g}$ . The CSR data consists of 511 events in a net live-time of  $2.27\mathrm{h}$  which corresponds to a net exposure of  $0.046\mathrm{g}$ -day. We compute the CSR exclusion region on DM models with different mass fractions for both SI and SD interactions [4]. Below we describe our calculation on the upper boundary and the lower boundary of the CSR exclusion region.

# 7.1 The lower boundary of the CSR exclusion region

For the lower boundary we first calculate the event rate via

$$
\frac {d R}{d E _ {R}} = \frac {\rho_ {\chi}}{m _ {\chi}} \sum_ {A} N _ {A} \int d ^ {3} v v f (v) \frac {d \sigma_ {\chi A}}{d E _ {R}}, \tag {7.1}
$$

where  $R$  is the event rate,  $E_R$  is the recoil energy,  $\rho_{\chi}$  is the local DM mass density,  $A$  denotes different nuclei in the detector (different isotopes of Al and O in the CSR detector [4]),  $N_A$  is the number of nucleus  $A$  per unit mass,  $\sigma_{\chi A}$  is interaction cross section between DM and nucleus  $A$ , as given in eq. (2.1), and  $f(v)$  is the DM velocity distribution, as given in eq. (3.1). For the SI case, we do not need to distinguish different isotopes. For the SD case, we only need to consider the isotopes with non-zero spin:  $^{17}\mathrm{O}$  and  $^{27}\mathrm{Al}$ . Since the natural abundance of  $^{17}\mathrm{O}$  is  $0.04\%$  [46], the dominant contribution to SD scatterings comes from  $^{27}\mathrm{Al}$ , whose natural abundance is  $100\%$ . The number of the isotope are obtained by multiplying the number of the element with the natural abundance.

We obtain the CSR experimental data from the data file provided at the website [47]. We bin the data in the energy range of  $[19.7,600]\mathrm{eV}$  with a bin width of  $5\mathrm{eV}$ , following ref. [4]. We further carry out a  $\chi^2$  analysis to calculate the lower boundary of the CSR exclusion region, where  $\chi^2$  is obtained via the same method as in the XQC case, namely computed via eq. (3.5) with the quantities substituted with the CSR predictions and data such that  $U_{i}$  is the number of events in the CSR data [4]. We exclude the data bins with null results in the total  $\chi^2$  analysis; we find that such a method leads to consistent results with ref. [4]. The  $90\%$  CL constraints on the lower boundary of the exclusion region are then obtained by requiring a total  $\chi^2 = 2.71$ .

# 7.2 The upper boundary of the CSR exclusion region

We adopt "method-a" in ref. [18] to compute the upper boundary of the CSR exclusion region. This method demands that all DM lose energy in the atmosphere so that after traversing the atmosphere, the maximum recoil energy of DM is below the CSR detection threshold  $(E_R^{\mathrm{min}} = 19.7\mathrm{eV})$ . This method leads to a satisfactory limit as compared with the MC method as shown in figure 5 of ref. [18].

In our analysis, we consider the DM particle with the largest possible initial velocity before entering the atmosphere,  $v_{\chi}^{i} = v_{\mathrm{esc}} + v_{\odot} \simeq 800 \mathrm{~km/s}$ , where  $v_{\odot} \simeq 220 \mathrm{~km/s}$  is the velocity of the sun. We then obtain the final kinetic energy  $E_{\chi}^{f}$  of DM by computing the total energy loss as the DM particle traverses the atmosphere via the differential equation given in eq. (E.1). In our analysis, we adopt the same atmosphere model as in ref. [13]; a brief description of the atmosphere model is given in appendix F. We obtain the upper limit by demanding the maximum recoil energy of DM,  $E_{R}^{\max} = 4E_{\chi}^{f}m_{\chi}m_{N} / (m_{\chi} + m_{N})^{2}$ , to be below the CSR detection threshold,  $E_{R}^{\min} = 19.7 \mathrm{eV}$ .

# 8 Comparison of XQC and CSR limits to other experimental limits

We compare the XQC and CSR limits computed in our analysis with other experimental constraints, for DM models with different DM mass fractions and for both the SI and SD cases. These include: (1) the balloon experiment: RRS [6]; (2) experiments at the surface of the Earth: EDELWEISS [5]; (3) underground experiments near the surface of the Earth: CDMS

![](images/818c70334e72026b14553be050e6660ad775d5f2e3e9e22937a2520aac3ed702.jpg)

![](images/244a09d70a562d09af0fb763e12d97723912e974624edad7219205cca0aa5755.jpg)

![](images/a20712b4638eb02fa00ec84dba2af744691bd6282571b0a56c6b22a4e7bb497d.jpg)

![](images/05dddeb9626925ef2a1ac126b64a127357bba4bc5dd242adf2858278b6f23041.jpg)

![](images/40a46b9bba2255fd3808cbefc74d166a2189c3995d1b1f9e54d4a8a51c6cb092.jpg)  
Figure 4. Experimental exclusion regions for velocity-independent DM-proton cross sections, both in the SI case (left) and in the SD (right) cases, with different mass fractions:  $f_{\chi} = 1$  (top),  $f_{\chi} = 10^{-2}$  (middle), and  $f_{\chi} = 10^{-4}$  (bottom). The exclusion region of XQC (our results) and CSR (our results) are shown as the red and orange regions respectively. Other exclusion regions include RRS (cyan), CDMS (gray), DAMIC (brown) and deep-underground experiments (black) [12], EDELWEISS (green) [5], and CR-boosted DM (purple) [61, 64, 73, 76, 79, 80]. The CMB and Lyman- $\alpha$  limits are adopted from Lyman- $\alpha$  (top) [58], and from CMB (middle) [59].

![](images/b82ef28dc27eaee8eb9ff20a986fe1fd1da2ab172d075699986633e486aeba2c.jpg)

surface [48] and DAMIC shallow site run [49]; (4) deep underground experiments considered in ref. [12]; (5) CMB and Lyman-  $\alpha$  constraints [50-60]; (6) boosted DM constraints [61-82].

Figure 4 shows the various experimental constraints on velocity-independent DM-proton cross sections, for both SI and SD interactions, and for three different mass fractions:  $f_{\chi} = 1$ ,  $f_{\chi} = 10^{-2}$ , and  $f_{\chi} = 10^{-4}$ . In the  $f_{\chi} = 1$  case, we adopt the EDELWEISS exclusion region from ref. [5], the boosted DM constraints from refs. [61, 64, 73, 76, 79, 80], and constraints of other experiments from ref. [12]. For the boosted DM constraints in the SI case, we consider limits from KamLAND [64], PROSPECT [73], PANDAX-II [79], CDEX [80], XENON1T and MiniBooNE [61]; For the boosted DM constraints in the SD case, we consider limits from Borexino [61] and XENON1T [76].<sup>3</sup> We rescale the above limits given in the  $f_{\chi} = 1$  case to the  $f_{\chi} = 10^{-2}$  and  $f_{\chi} = 10^{-4}$  cases in figure 4.<sup>4</sup> For mass fractions less than  $f_{\chi} = 1$  we use the following approximation to compute the exclusion regions: The upper boundary of the exclusion region is assumed to be the same as the  $f_{\chi} = 1$  case; the lower boundary of the exclusion region is computed by rescaling the lower boundary in the  $f_{\chi} = 1$  case by the mass fraction such that

$$
\sigma_ {l} \left(f _ {\chi}\right) = \frac {\sigma_ {l} \left(f _ {\chi} = 1\right)}{f _ {\chi} ^ {k}}, \tag {8.1}
$$

where  $\sigma_{l}(f_{\chi} = 1)$  is the lower boundary on the cross section in the  $f_{\chi} = 1$  case, and  $k = 1(1 / 2)$  for DM with expected velocity in the DM halo (for the boosted DM). The rescaling for the halo DM for most cases has been confirmed to be a fairly reasonable approximation in our XQC simulations; the rescaling for the boosted DM is due to the fact that the event rate of the boosted DM is proportional to  $\rho_{\chi}\sigma_{\chi p}^{2}$  [78].

For CMB and Lyman- $\alpha$  constraints shown in figure 4, we adopt the Lyman- $\alpha$  constraints from ref. [58] and the CMB limits from ref. [59] and with further rescalings. In the  $f_{\chi} = 1$  case, because the Lyman- $\alpha$  limits are stronger than the CMB limits, we only show the Lyman- $\alpha$  constraints from ref. [58] for both SI and SD cases.

In the  $f_{\chi} = 0.01$  case, the CMB limits become stronger than the Lyman-  $\alpha$  constraints, since the Lyman-  $\alpha$  constraints are expected to decrease with the DM mass fraction much faster than the CMB limits. Thus we obtain the CMB constraints in the  $f_{\chi} = 0.01$  case by inverse-linearly rescaling the limits analyzed in the  $f_{\chi} = 1$  case from ref. [59] for both SI and SD cases. We note that recently refs. [58, 60] have combined the CMB constraints with the baryon acoustic oscillations (BAO) limits, leading to a better upper bound on the cross section than the CMB only, by a factor of  $\lesssim 2.5$  ( $\sim 1.5$ ) for light (heavy) DM mass.

Although we do not show the CMB constraints for even smaller DM mass fractions, we note that the stringent CMB constraints on DM of the  $n = -4$  case (e.g., millicharged DM) disappear if the DM mass fraction is less than  $0.2\%$ , since such a small DM component is distinguishable from baryons [56]. Thus we expect the CMB and Lyman-  $\alpha$  constraints to be further weakened as the DM mass fraction decreases to even smaller values, or even to disappear.

In the SI case with  $f_{\chi} = 1$ , DM with cross section shown in figure 4 and with mass in the range of  $[10,10^{5}]$  GeV are ruled out by combining all experimental constraints. However, in the SD case with  $f_{\chi} = 1$ , there are two parameter regions as shown in figure 4 are still allowed. The allowed parameter space increases significantly as the mass fraction  $f_{\chi}$  is changed from unity to  $10^{-2}$  and further to  $10^{-4}$ . In the SD case with  $f_{\chi} = 10^{-4}$ , almost the entire parameter space with  $m_{\chi} \gtrsim 10$  GeV and  $\sigma_{\chi p} \gtrsim 10^{-27}$  cm $^2$  seems to be allowed.

# 9 Summary

In this paper, we use MC simulations to calculate the XQC exclusion regions on SIDM with different mass fractions, with different velocity-dependent cross sections, and with both SI and SD interactions. It is found that, to a good approximation, there is a (inverse) linear relation between the lower/right boundary of the XQC exclusion region and the mass fraction. For the upper/left boundary of the XQC exclusion region, the MC simulations reveal some non-trivial dependence on the mass fraction. We note that our results agree with previous analyses that used MC simulations to compute the XQC limits, such as refs. [10, 11, 13], when the same assumptions on the DM models and on the response of the XQC detector are made. The primary goal of our analysis is to study the entire XQC excluded parameter space for different types of DM interaction cross sections and for different DM mass fractions, which have not been fully explored in previous studies. To facilitate the intensive MC simulations in modeling the interactions of DM with the XQC detector for the full parameter space, we have neglected the fact that the aluminum shield can be somewhat transparent in a small portion of the parameter space at low DM mass, and the thermalization efficiency of the silicon detector, which, however, has not been experimentally measured yet.

For the velocity-dependent cross sections, we consider four different cases:  $n = \{0, 2, -2, -4\}$  in the form of  $\sigma_{\chi p} = \sigma_{\chi p}^{0}v^{n}$ . We find that most of the exclusion regions for different  $n$ 's overlap with each other. However, there are also some differences among them: For the  $n = -4$  case, the lower boundary of the XQC exclusion region is a little lower than other cases; for the  $n = 2$  case, the upper boundary for heavy mass is much higher than other cases. Also, for the  $n = 2$  case, there exists a large portion of parameter space deep inside the XQC exclusion region that is unconstrained by XQC; this is due to the unused energy range in the XQC data and the "focusing" effects of the filters on the DM velocity so that the DM velocity is localized in a narrow range.

We compare the XQC exclusion regions in the SI and the SD cases and find that the XQC exclusion regions in the SD case are quite different from the SI case. Although the lower boundary of the XQC exclusion region in the SD case is similar to the SI case in the shape, it is larger by a factor of  $10^{5}$ . For the upper boundary, the XQC exclusion region in the SD case is very different from the SI case and there is no simple re-scaling relation between them. We also find that the XQC exclusion regions disappear if the mass fraction is significantly small,  $f_{\chi} \lesssim 10^{-5}(10^{-4})$  for the SI (SD) case.

We also analyze the CSR constraints for different DM mass fractions both for the SI and for the SD cases. We further compare the XQC and CSR limits computed in our analysis, with various other experimental constraints. We find that the allowed parameter space increases when the mass fraction decreases; for a sufficiently small mass fraction, such as  $f \lesssim 10^{-4}$ , a very large portion of parameter space is allowed.

# Acknowledgments

The work was supported in part by the National Natural Science Foundation of China under Grant Nos. 12275128, 11775109, and 12147103, and by the Fundamental Research Funds for the Central Universities.

# A Nucleus with spin

Only nuclei with spin participate in the SD interactions. Table 1 shows the nuclei with spin that are used in our analysis.

Table 1. Nuclei that are considered in the SD calculations in the analysis. The natural abundance of the nuclei is obtained in ref. [46], and the spin information  $(J_{A},\langle \mathbf{S}_{p}\rangle ,\langle \mathbf{S}_{n}\rangle)$  is obtained from refs. [12, 84]. We have neglected  $^{15}\mathrm{N}$ , since its contribution is too small compared with  $^{14}\mathrm{N}$ .  

<table><tr><td>Element</td><td>Abundance</td><td>JA</td><td>⟨Sp⟩</td><td>⟨Sn⟩</td></tr><tr><td>27Al</td><td>100%</td><td>5/2</td><td>0.343</td><td>0.0296</td></tr><tr><td>13C</td><td>1.1%</td><td>1/2</td><td>0</td><td>-0.167</td></tr><tr><td>29Si</td><td>4.7%</td><td>1/2</td><td>-0.002</td><td>0.13</td></tr><tr><td>17O</td><td>0.04%</td><td>5/2</td><td>0</td><td>0.5</td></tr><tr><td>14N</td><td>99.6%</td><td>1</td><td>0.5</td><td>0.5</td></tr></table>

# B DM velocity after scattering

The final velocity  $\pmb{v}_f$  of the DM particle in the lab frame after a single scattering with the target nucleus  $N$  is given by

$$
\boldsymbol {v} _ {f} = \boldsymbol {v} _ {f} ^ {*} + \boldsymbol {u}, \tag {B.1}
$$

where  $\pmb{v}_f^*$  is the DM final velocity in the CM frame, and  $\pmb{u}$  is the velocity of the CM frame in the lab frame, which is given by

$$
\boldsymbol {u} = \frac {m _ {\chi} v}{m _ {\chi} + m _ {N}} \left( \begin{array}{c} \sin \theta \cos \phi \\ \sin \theta \sin \phi \\ \cos \theta \end{array} \right), \tag {B.2}
$$

where  $m_{\chi}$  is the DM mass,  $m_N$  is the target nuclear mass, and  $v$ ,  $\theta$  and  $\phi$  are the magnitude, polar angle and azimuthal angle of the DM initial velocity in the lab frame respectively. Setting the  $z$  axis of the CM frame along the initial velocity of the DM particle, one has

$$
\boldsymbol {v} _ {f} ^ {*} = \frac {m _ {N} v}{m _ {\chi} + m _ {N}} \left( \begin{array}{c} \cos \phi (\sin \alpha \cos \beta \cos \theta + \sin \theta \cos \alpha) - \sin \phi \sin \alpha \sin \beta \\ \sin \phi (\sin \alpha \cos \beta \cos \theta + \sin \theta \cos \alpha) + \cos \phi \sin \alpha \sin \beta \\ \cos \theta \cos \alpha - \sin \theta \sin \alpha \cos \beta \end{array} \right),
$$

where  $\alpha$  and  $\beta$  are the polar angle and the azimuthal angle of the final DM velocity in the CM frame respectively. The percentage energy loss of the DM particle during the scattering process is then given by

$$
\frac {\Delta E}{E _ {\chi} ^ {i}} \equiv \frac {E _ {\chi} ^ {i} - E _ {\chi} ^ {f}}{E _ {\chi} ^ {i}} = \frac {2 m _ {\chi} m _ {N}}{(m _ {\chi} + m _ {N}) ^ {2}} (1 - \cos \alpha), \tag {B.4}
$$

where  $E_{\chi}^{i}\left(E_{\chi}^{f}\right)$  the initial (final) kinetic energy of the DM particle in the lab frame.

# C XQC data

The XQC data are binned into thirteen different energy bins in ref. [10]; see table 1 of ref. [10] for the energy ranges and the number of counts for each bin. The detection efficiency is small for the low energy measurements. Following ref. [10], we use efficiency  $f = 0.3815$  (0.5083) for the first (second) energy bin, and  $f = 1$  for the eleven high energy bins.

# D The number of DM particles inside the FoV of XQC

The total number of DM particles (incident on the surface area of the detector or of the filter) in the XQC FoV during the data-takings is given by

$$
N _ {\chi} = f _ {\chi} \frac {\rho_ {\chi}}{m _ {\chi}} S t \int f _ {B} \left(\left| \boldsymbol {v} ^ {\prime} + \boldsymbol {v} _ {\mathrm {d e t}} \right|\right) v ^ {\prime} \cos \theta v ^ {\prime 2} d v ^ {\prime} d \Omega , \tag {D.1}
$$

where  $\rho_{\chi} = 0.3\mathrm{GeV / cm}^3$  is the local DM mass density,  $m_{\chi}$  is the DM mass,  $f_{\chi}$  is the mass fraction,  $S$  is the surface area of the detector or the filter,  $t = 100.7$  sec is the detection time,  $\pmb{v}^{\prime}$  is the DM velocity in the lab frame,  $\pmb{v}_{\mathrm{det}} = (39.14,230.5,3.573)\mathrm{km / s}$  [10] is the velocity of the detector in the halo frame in the galactic coordinate system, and  $f_{B}$  is the truncated Boltzmann distribution of the DM velocity in the halo frame as given in eq. (3.1). In our analysis, we take  $S = 0.34~\mathrm{cm}^2$  ( $S = 7.1~\mathrm{cm}^2$ ) for the detector (filter) area [3]. In the coordinate system where the z-axis points to the opposite direction of the center of the FoV, the integral is performed in the range of  $0 < \theta < \cos^{-1}(1 - (2\pi)^{-1})$  and  $0 < \varphi < 2\pi$ . Thus, we have

$$
N _ {\chi} = 3. 5 2 \times 1 0 ^ {7} f _ {\chi} \frac {\mathrm {G e V}}{m _ {\chi}} \frac {S}{0 . 3 4 \mathrm {c m} ^ {2}}. \tag {D.2}
$$

# E DM energy loss through an overburden

In this section, we analyze the energy loss of the DM when traversing an overburden. See also refs. [13, 18] for similar analysis. The energy loss of DM, when passing through an overburden, can be computed via

$$
\frac {d E _ {\chi}}{d x} = - \sum_ {N} n _ {N} \int_ {0} ^ {E _ {R} ^ {\mathrm {m a x}}} d E _ {R} E _ {R} \frac {d \sigma_ {\chi N}}{d E _ {R}}, \tag {E.1}
$$

where  $E_{\chi}$  is the DM kinetic energy,  $x$  is the distance traveled by DM,  $n_N$  is the number density of nucleus  $N$ ,  $E_R$  is the nuclear recoil energy,  $d\sigma_{\chi N} / dE_R$  is the differential cross section, and  $E_R^{\mathrm{max}} = 2\mu_{\chi N}^2 v_\chi^2 /m_N$  is the maximum recoil energy where  $v_{\chi}$  is the DM velocity,  $m_N$  is the nucleus mass, and  $\mu_{\chi N} = m_{\chi}m_{N} / (m_{\chi} + m_{N})$  is the reduced mass with  $m_{\chi}$  being the DM mass. Here the summation runs over different nuclei in the overburden. For a velocity-dependent cross section that is proportional to  $v^n$ , one has

$$
\frac {d \sigma_ {\chi N}}{d E _ {R}} = \frac {\sigma_ {\chi N} ^ {\mathrm {t o t}}}{E _ {R} ^ {\mathrm {m a x}}} = \frac {\sigma_ {\chi N} ^ {0} v _ {\chi} ^ {n}}{E _ {R} ^ {\mathrm {m a x}}}, \tag {E.2}
$$

where  $\sigma_{\chi N}^{\mathrm{tot}}$  is the total DM-nucleus cross section, and we have assumed that the scattering cross section is isotropic in the CM frame. Substituting eq. (E.2) into eq. (E.1) and performing the integral on  $E_R$ , one has

$$
\frac {d E _ {\chi}}{d x} = - E _ {T} ^ {2} \left(\frac {2 E _ {\chi}}{m _ {\chi}}\right) ^ {\frac {n}{2} + 1}, \tag {E.3}
$$

![](images/2ce873fc27bf9e05f8ec863d5f1a05a384fcd26d225f8268ee4fb3693dc6e107.jpg)  
Figure 5. Comparison of different methods of computing the upper boundary of the XQC exclusion region in the SI and  $n = 0$  case: our MC simulation (red), the analytical "method-a" adopted from ref. [18] (blue), and the  $90\%$  CL exclusion region given by ref. [10] (black).

where we have used  $E_{\chi} = m_{\chi}v_{\chi}^{2} / 2$  and defined the following quantity

$$
E _ {T} ^ {2} \equiv \sum_ {N} \frac {n _ {N} \mu_ {\chi N} ^ {2} \sigma_ {\chi N} ^ {0}}{m _ {N}}. \tag {E.4}
$$

The final energy of DM after passing through an overburden can then be obtained by solving eq. (E.3)

$$
E _ {\chi} ^ {f} = E _ {\chi} ^ {i} \left\{ \begin{array}{l l} \left[ (v _ {\chi} ^ {i}) ^ {n} \frac {n d E _ {T} ^ {2}}{m _ {\chi}} + 1 \right] ^ {- \frac {2}{n}}, & n \neq 0, \\ \exp \left[ - 2 d E _ {T} ^ {2} / m _ {\chi} \right], & n = 0 \end{array} \right. \tag {E.5}
$$

where  $d$  is the distance traveled by DM in the overburden,  $v_{\chi}^{i}$  is the initial DM velocity, and  $E_{\chi}^{i}(E_{\chi}^{f})$  is the initial (final) kinetic energy of DM.

# E.1 The upper boundary of the XQC exclusion region

We can use "method-a" in ref. [18] to estimate the upper boundary of the XQC exclusion region: We demand that DM particles with the largest possible velocity,  $v_{\chi}^{i} = v_{\mathrm{esc}} + v_{\odot} \simeq 800 \mathrm{~km/s}$ , lose energy through the 5 filters such that the final energy after those filters are below the energy threshold of the XQC experiment, which is  $29 \mathrm{eV}$ . We compare such an estimate with our MC simulations in figure 5. We find that the estimated method is consistent with our MC simulations for DM masses larger than  $\sim 1000 \mathrm{GeV}$ . For small DM masses, however, the estimates are a little larger than results in our MC simulations.

# E.2 The allowed band in the  $n = 2$  case

As shown in figure 2 and figure 3, for the  $n = 2$  case, there exist parameter space, as described by eq. (4.1), where the XQC constraints are "mysteriously" gone. This can be explained by the energy loss calculations presented here and the XQC data bins. In the  $n = 2$  case, eq. (E.5) becomes

$$
\frac {1}{E _ {\chi} ^ {f}} = \frac {1}{E _ {c}} + \frac {1}{E _ {\chi} ^ {i}}, \tag {E.6}
$$

![](images/7ec82be815b8b2dae8704a83da8e16f9c027c3fec677cebd68bf6ef9bef80a34.jpg)  
Figure 6. Left panel: The DM velocity distributions in the lab frame for DM before penetrating the XQC filters (black) and for two DM model points after penetrating the XQC filters: model  $A$  (blue) and model  $B$  (red). The vertical gray bands indicate the velocity range where the kinetic energy of the DM is in the range of [2505, 4000] eV. Right panel: The XQC exclusion region in the SI case (red boundary) in the parameter space spanned by  $\sigma_{\chi p}^{0}$  and the DM mass in the  $n = 2$  case. The two blue lines are obtained by equating  $E_{c}$  in eq. (E.7) to  $2505\mathrm{eV}$  and  $4000\mathrm{eV}$  respectively. The benchmark model point  $A$  with  $(m_{\chi},\sigma_{\chi p}^{0}) = (10^{3}\mathrm{GeV},10^{-14}\mathrm{cm}^{2})$  and the model point  $B$  with  $(m_{\chi},\sigma_{\chi p}^{0}) = (10^{5}\mathrm{GeV},10^{-10}\mathrm{cm}^{2})$  are shown as stars.

![](images/bb3ee59d16c4793765f8d67c57ff47bb47e1e80cb09bcad50b1ab17e6b900038.jpg)

where  $E_{c} = m_{\chi}^{2} / (4dE_{T}^{2})$ . Thus, for XQC, one has (for  $m_{\chi}\gg m_N$ )

$$
E _ {c} \simeq 3. 6 7 \times 1 0 ^ {3} (1. 1 7 \times 1 0 ^ {7}) \mathrm {e V} \left[ \frac {m _ {\chi}}{1 0 ^ {4} \mathrm {G e V}} \right] ^ {2} \frac {1 0 ^ {- 1 2} \mathrm {c m} ^ {2}}{\sigma_ {\chi p} ^ {0}}, \tag {E.7}
$$

for the SI (SD) case. For  $E_{\chi}^{i} \gg E_{c}$ , the DM final energy becomes localized in the vicinity of  $E_{c}$ , namely  $E_{\chi}^{f} \approx E_{c}$ , which is independent of the DM initial energy  $E_{\chi}^{i}$ . Under such circumstances, if  $E_{c}$  (obtained by summing the 5 filters) falls inside [2505, 4000] eV (the energy range discarded by XQC [10]), these DM particles do not give rise to detectable events in XQC. Thus, by equating  $E_{c}$  in eq. (E.7) to 2505 eV and 4000 eV, we obtain two curves in the parameter space spanned by  $m_{\chi}$  and  $\sigma_{\chi p}^{0}$ , which are shown in the right panel of figure 6 for the SI case; the two lines obtained via eq. (E.7) accurately describe the MC results in the mass range of  $10^{4} - 3 \times 10^{5} \mathrm{GeV}$ .

To understand why the analytical results via eq. (E.7) fail below  $\sim 10^{4}\mathrm{GeV}$ , we select two benchmark model points on the right panel figure of figure 6: model point  $A$  with  $(m_{\chi},\sigma_{\chi p}^{0}) = (10^{3}\mathrm{GeV},10^{-14}\mathrm{cm}^{2})$  and model point  $B$  with  $(m_{\chi},\sigma_{\chi p}^{0}) = (10^{5}\mathrm{GeV},10^{-10}\mathrm{cm}^{2})$ , and compare their velocity distributions after passing the five XQC filters on the left panel figure of figure 6. The kinetic energy of DM particles in the model point  $B$  has a very narrow distribution so that almost all the DM particles are inside the energy range of [2505, 4000] eV: 252 DM particles inside the [2505, 4000] eV range with less than 1 event outside during the XQC data-taking. However, the kinetic energy in the model point  $A$  has a rather extended distribution so that a significant fraction of DM particles are outside the energy range of [2505, 4000] eV: 14553 and 8807 events are inside and outside the [2505, 4000] eV range during the XQC data-taking respectively. Thus the DM particles in the model point  $A$  are no longer all inside the XQC discarded data bin of [2505, 4000] eV, which results in the failure of the simple analytic method.

Table 2. The atmosphere model adopted from ref. [13]. Here  $z$  is the altitude,  ${z}_{\min }\left( {z}_{\max }\right)$  is the minimum (maximum) altitude of each layer,and  ${\rho }_{\text{atm }}\left( {z = 0}\right)  = {1.225} \times  {10}^{-3}\mathrm{\;g}/{\mathrm{{cm}}}^{3}$  is the atmosphere density at the sea level. The atmosphere density is taken to be zero above  ${84.8}\mathrm{\;{km}}$  .  

<table><tr><td>layer</td><td>zmin(km)</td><td>zmax(km)</td><td>ρatm(z)/ρatm(z=0)</td></tr><tr><td>1</td><td>0</td><td>11</td><td>(1-z/44.31)4.256</td></tr><tr><td>2</td><td>11</td><td>20</td><td>0.297 exp((11-z)/6.34)</td></tr><tr><td>3</td><td>20</td><td>32</td><td>(0.978+z/201.02)-35.16</td></tr><tr><td>4</td><td>32</td><td>47</td><td>(0.857+z/57.94)-13.2</td></tr><tr><td>5</td><td>47</td><td>51</td><td>1.165 × 10-3exp((47-z)/7.92)</td></tr><tr><td>6</td><td>51</td><td>71</td><td>(0.8-z/184.8)11.2</td></tr><tr><td>7</td><td>71</td><td>84.8</td><td>(0.9-z/198.1)16.08</td></tr></table>

# F Atmosphere model

We use the same atmosphere model as in ref. [13]. For completeness, we provide a brief description of the atmosphere model in this appendix. The atmosphere from the Earth surface to the altitude of  $z = 84.8\mathrm{km}$  is divided into 7 layers [13], as shown in table 2.

For the SI case, we consider both N and O elements in the atmosphere that scatter with DM. The mass fractions of N (O) in the atmosphere is  $78.08\%$ $(20.94\%)$ . For the SD case, we only consider N in the atmosphere that can scatter with DM through SD interaction. We neglect the contribution of O for the CSR upper boundary in the SD case, because the natural abundance of  $^{17}\mathrm{O}$  (the O isotope that has spin) is  $0.04\%$  [46].

# G Thermalization efficiency

The effects of the thermalization efficiency, the ratio between the measured energy in XQC and the DM nuclear recoil energy, have been recently investigated in ref. [13], for the parameter space of  $m_{\chi} \in [0.01, 100]$  GeV and  $\sigma_{\chi p} \in [10^{-31}, 10^{-21}]$  cm $^2$ . In this section, we study the effects of the thermalization efficiency on the XQC contour in the entire parameter space spanned by the DM-proton cross-section and the DM mass.

Figure 7 shows the XQC exclusion region in the SI case where  $n = 0$  and  $f_{\chi} = 1$ , for three different thermalization efficiencies:  $\epsilon = 1$ ,  $\epsilon = 0.1$ , and  $\epsilon = 0.02$ . These three thermalization efficiencies have been recently suggested by ref. [13], since the experimentally measured value is not available in the energy range of interest for the XQC detector. As shown in figure 7, as  $\epsilon$  decreases, the left boundary of XQC exclusion reigon shifts to the right, and the right boundary shifts to the left. The effects of the thermalization efficiency are less significant on the upper and lower boundaries of the XQC exclusion contours. We note that the difference at the lower boundary in the mass range of  $\sim (1 - 100)$  GeV between our calculation and ref. [13] is due to the effects of DM penetrating the aluminum body of the rocket considered in ref. [13].

![](images/c3e7aa8a2cd7c5d0c299e01cc03b4146cfd5654eab19d1b49fe34aa58249d0c6.jpg)  
Figure 7. XQC exclusion region in the SI case where  $n = 0$  and  $f_{\chi} = 1$ , for different thermalization efficiencies:  $\epsilon = 1$  (black-solid),  $\epsilon = 0.1$  (blue-solid), and  $\epsilon = 0.02$  (red-solid). Results from ref. [13] (Mahdawi et al.) are shown in dashed lines:  $\epsilon = 1$  (black-dashed),  $\epsilon = 0.1$  (blue-dashed), and  $\epsilon = 0.02$  (red-dashed).

# References

[1] XENON collaboration, Dark Matter Search Results from a One Ton-Year Exposure of XENON1T, Phys. Rev. Lett. 121 (2018) 111302 [arXiv:1805.12562] [INSPIRE].  
[2] PANDAX-II collaboration, Results of dark matter search using the full PandaX-II exposure, Chin. Phys. C 44 (2020) 125001 [arXiv:2007.15469] [INSPIRE].  
[3] D. McCammon et al., A high spectral resolution observation of the soft  $x$ -ray diffuse background with thermal detectors, Astrophys. J. 576 (2002) 188 [astro-ph/0205012] [INSPIRE].  
[4] CRESST collaboration, Results on MeV-scale dark matter from a gram-scale cryogenic calorimeter operated above ground, Eur. Phys. J. C 77 (2017) 637 [arXiv:1707.06749] [INSPIRE].  
[5] EDELWEISS collaboration, Searching for low-mass dark matter particles with a massive Ge bolometer operated above-ground, Phys. Rev. D 99 (2019) 082003 [arXiv:1901.03588] [INSPIRE].  
[6] J. Rich, R. Rocchia and M. Spiro, A Search for Strongly Interacting Dark Matter, Phys. Lett. B 194 (1987) 173 [INSPIRE].  
[7] B.D. Wandelt et al., Selfinteracting dark matter, in the proceedings of the 4th International Symposium on Sources and Detection of Dark Matter in the Universe (DM 2000), Marina del Rey, U.S.A., February 23–25, 2000, [astro-ph/0006344] [INSPIRE].  
[8] G. Zaharijas and G.R. Farrar, A window in the dark matter exclusion limits, Phys. Rev. D 72 (2005) 083502 [astro-ph/0406531] [INSPIRE].  
[9] K. Sigurdson et al., Dark-matter electric and magnetic dipole moments, Phys. Rev. D 70 (2004) 083501 [Erratum ibid. 73 (2006) 089903] [astro-ph/0406355] [INSPIRE].  
[10] A.L. Erickcek, P.J. Steinhardt, D. McCammon and P.C. McGuire, Constraints on the Interactions between Dark Matter and Baryons from the X-ray Quantum Calorimetry Experiment, Phys. Rev. D 76 (2007) 042007 [arXiv:0704.0794] [INSPIRE].  
[11] M.S. Mahdawi and G.R. Farrar, Closing the window on  $\sim$ GeV Dark Matter with moderate ( $\sim$ $\mu b$ ) interaction with nucleons, JCAP 12 (2017) 004 [arXiv:1709.00430] [INSPIRE].  
[12] D. Hooper and S.D. McDermott, Robust Constraints and Novel Gamma-Ray Signatures of Dark Matter That Interacts Strongly With Nucleons, Phys. Rev. D 97 (2018) 115006 [arXiv:1802.03025] [INSPIRE].

[13] M.S. Mahdawi and G.R. Farrar, Constraints on Dark Matter with a moderately large and velocity-dependent DM-nucleon cross-section, JCAP 10 (2018) 007 [arXiv:1804.03073] [INSPIRE].  
[14] D. McKeen et al., Accelerating Earth-bound dark matter, Phys. Rev. D 106 (2022) 035011 [arXiv:2202.08840] [INSPIRE].  
[15] X. Xu and G.R. Farrar, Resonant Scattering between Dark Matter and Baryons: Revised Direct Detection and CMB Limits, arXiv:2101.00142 [INSPIRE].  
[16] J.H. Davis, Probing Sub-GeV Mass Strongly Interacting Dark Matter with a Low-Threshold Surface Experiment, Phys. Rev. Lett. 119 (2017) 211302 [arXiv:1708.01484] [INSPIRE].  
[17] B.J. Kavanagh, Earth scattering of superheavy dark matter: Updated constraints from detectors old and new, Phys. Rev. D 97 (2018) 123013 [arXiv:1712.04901] [INSPIRE].  
[18] T. Emken and C. Kouvaris, How blind are underground and surface detectors to strongly interacting Dark Matter?, Phys. Rev. D 97 (2018) 115047 [arXiv:1802.04764] [INSPIRE].  
[19] J.M. Blatt and V.F. Weisskopf, Theoretical nuclear physics, Courier Corporation (1991).  
[20] M.C. Digman et al., Not as big as a barn: Upper bounds on dark matter-nucleus cross sections, Phys. Rev. D 100 (2019) 063013 [Erratum ibid. 106 (2022) 089902] [arXiv:1907.10618] [INSPIRE].  
[21] S. Davidson, S. Hannestad and G. Raffelt, Updated bounds on millicharged particles, JHEP 05 (2000) 003 [hep-ph/0001179] [INSPIRE].  
[22] S.L. Dubovsky, D.S. Gorbunov and G.I. Rubtsov, Narrowing the window for millicharged particles by CMB anisotropy, JETP Lett. 79 (2004) 1 [hep-ph/0311189] [INSPIRE].  
[23] K. Cheung and T.-C. Yuan, Hidden fermion as milli-charged dark matter in Stueckelberg Z-prime model, JHEP 03 (2007) 120 [hep-ph/0701107] [INSPIRE].  
[24] D. Feldman, Z. Liu and P. Nath, The Stueckelberg Z-prime Extension with Kinetic Mixing and Milli-Charged Dark Matter From the Hidden Sector, Phys. Rev. D 75 (2007) 115001 [hep-ph/0702123] [INSPIRE].  
[25] D. Feldman, Z. Liu and P. Nath, The Stueckelberg extension and milli weak and milli charged dark matter, AIP Conf. Proc. 939 (2007) 50 [arXiv:0705.2924] [INSPIRE].  
[26] S.D. McDermott, H.-B. Yu and K.M. Zurek, Turning off the Lights: How Dark is Dark Matter?, Phys. Rev. D 83 (2011) 063509 [arXiv:1011.2907] [INSPIRE].  
[27] J.M. Cline, Z. Liu and W. Xue, Millicharged Atomic Dark Matter, Phys. Rev. D 85 (2012) 101302 [arXiv:1201.4858] [INSPIRE].  
[28] A.D. Dolgov, S.L. Dubovsky, G.I. Rubtsov and I.I. Tkachev, Constraints on millicharged particles from Planck data, Phys. Rev. D 88 (2013) 117701 [arXiv:1310.2376] [INSPIRE].  
[29] H. Vogel and J. Redondo, Dark Radiation constraints on minicharged particles in models with a hidden photon, JCAP 02 (2014) 029 [arXiv:1311.2600] [INSPIRE].  
[30] A. Kamada, K. Kohri, T. Takahashi and N. Yoshida, Effects of electrically charged dark matter on cosmic microwave background anisotropies, Phys. Rev. D 95 (2017) 023502 [arXiv:1604.07926] [INSPIRE].  
[31] J.B. Muñoz and A. Loeb, A small amount of mini-charged dark matter could cool the baryons in the early Universe, Nature 557 (2018) 684 [arXiv:1802.10094] [INSPIRE].  
[32] A. Berlin, D. Hooper, G. Krynjaic and S.D. McDermott, Severely Constraining Dark Matter Interpretations of the 21-cm Anomaly, Phys. Rev. Lett. 121 (2018) 011102 [arXiv:1803.02804] [INSPIRE].  
[33] E.D. Kovetz et al., Tighter limits on dark matter explanations of the anomalous EDGES 21 cm signal, Phys. Rev. D 98 (2018) 103529 [arXiv:1807.11482] [INSPIRE].

[34] Z. Liu and Y. Zhang, Probing millicharge at BESIII via monophoton searches, Phys. Rev. D 99 (2019) 015004 [arXiv:1808.00983] [INSPIRE].  
[35] J. Liang, Z. Liu, Y. Ma and Y. Zhang, Millicharged particles at electron colliders, Phys. Rev. D 102 (2020) 015002 [arXiv:1909.06847] [INSPIRE].  
[36] ARGONEUT collaboration, Improved Limits on Millicharged Particles Using the ArgoNeuT Experiment at Fermilab, Phys. Rev. Lett. 124 (2020) 131801 [arXiv:1911.07996] [INSPIRE].  
[37] R. Plestid et al., New Constraints on Millicharged Particles from Cosmic-ray Production, Phys. Rev. D 102 (2020) 115032 [arXiv:2002.11732] [INSPIRE].  
[38] A. Ball et al., Search for millicharged particles in proton-proton collisions at  $\sqrt{s} = 13$  TeV, Phys. Rev. D 102 (2020) 032002 [arXiv:2005.06518] [INSPIRE].  
[39] G. Marocco and S. Sarkar, Blast from the past: Constraints on the dark sector from the BEBC WA66 beam dump experiment, SciPost Phys. 10 (2021) 043 [arXiv:2011.08153] [INSPIRE].  
[40] Q. Li and Z. Liu, Two-component millicharged dark matter and the EDGES 21 cm signal, Chin. Phys. C 46 (2022) 045102 [arXiv:2110.14996] [INSPIRE].  
[41] J.J. Fan, M. Reece and L.-T. Wang, Non-relativistic effective theory of dark matter direct detection, JCAP 11 (2010) 042 [arXiv:1008.1591] [INSPIRE].  
[42] J.D. Lewin and P.F. Smith, Review of mathematics, numerical factors, and corrections for dark matter experiments based on elastic nuclear recoil, Astrophys. 6 (1996) 87 [INSPIRE].  
[43] R. Essig et al., Direct Detection of sub-GeV Dark Matter with Semiconductor Targets, JHEP 05 (2016) 046 [arXiv:1509.01598] [INSPIRE].  
[44] R.K. Leane and J. Smirnov, *Floating Dark Matter in Celestial Bodies*, arXiv:2209.09834 [INSPIRE].  
[45] A.M. Dziewonski and D.L. Anderson, Preliminary reference earth model, Phys. Earth Planet. Interiors 25 (1981) 297 [INSPIRE].  
[46] K. Lodders et al., The planetary scientist's companion, Oxford University Press on Demand (1998).  
[47] https://arxiv.org/src/1707.06749v4/anc/additional_material.txt.  
[48] CDMS collaboration, Exclusion limits on the WIMP nucleon cross-section from the cryogenic dark matter search, Phys. Rev. Lett. 84 (2000) 5699 [astro-ph/0002471] [INSPIRE].  
[49] DAMIC collaboration, Search for low-mass WIMPs in a 0.6 kg day exposure of the DAMIC experiment at SNOLAB, Phys. Rev. D 94 (2016) 082006 [arXiv:1607.07410] [INSPIRE].  
[50] C. Boehm, A. Riazuelo, S.H. Hansen and R. Schaeffer, Interacting dark matter disguised as warm dark matter, Phys. Rev. D 66 (2002) 083505 [astro-ph/0112522] [INSPIRE].  
[51] R.H. Cyburt, B.D. Fields, V. Pavlidou and B.D. Wandelt, Constraining strong baryon dark matter interactions with primordial nucleosynthesis and cosmic rays, Phys. Rev. D 65 (2002) 123503 [astro-ph/0203240] [INSPIRE].  
[52] X.-L. Chen, S. Hannestad and R.J. Scherrer, *Cosmic microwave background and large scale structure limits on the interaction between dark matter and baryons*, Phys. Rev. D 65 (2002) 123515 [astro-ph/0202496] [INSPIRE].  
[53] C. Boehm and R. Schaeffer, Constraints on dark matter interactions from structure formation: Damping lengths, *Astron. Astrophys.* 438 (2005) 419 [astro-ph/0410591] [INSPIRE].  
[54] C. Dvorkin, K. Blum and M. Kamionkowski, Constraining Dark Matter-Baryon Scattering with Linear Cosmology, Phys. Rev. D 89 (2014) 023519 [arXiv:1311.2937] [INSPIRE].  
[55] V. Gluscevic and K.K. Boddy, Constraints on Scattering of keV-TeV Dark Matter with Protons in the Early Universe, Phys. Rev. Lett. 121 (2018) 081301 [arXiv:1712.07133] [INSPIRE].

[56] K.K. Boddy et al., Critical assessment of CMB limits on dark matter-baryon scattering: New treatment of the relative bulk velocity, Phys. Rev. D 98 (2018) 123506 [arXiv:1808.00001] [INSPIRE].  
[57] W.L. Xu, C. Dvorkin and A. Chael, Probing sub-GeV Dark Matter-Baryon Scattering with Cosmological Observables, Phys. Rev. D 97 (2018) 103530 [arXiv:1802.06788] [INSPIRE].  
[58] M.A. Buen-Abad, R. Essig, D. McKeen and Y.-M. Zhong, Cosmological constraints on dark matter interactions with ordinary matter, Phys. Rept. 961 (2022) 1 [arXiv:2107.12377] [INSPIRE].  
[59] K.K. Boddy, G. Krnjaic and S. Moltner, Investigation of CMB constraints for dark matter-helium scattering, Phys. Rev. D 106 (2022) 043510 [arXiv:2204.04225] [INSPIRE].  
[60] D.C. Hooper et al., One likelihood to bind them all: Lyman-  $\alpha$  constraints on non-standard dark matter, JCAP 10 (2022) 032 [arXiv:2206.08188] [INSPIRE].  
[61] T. Bringmann and M. Pospelov, Novel direct detection constraints on light dark matter, Phys. Rev. Lett. 122 (2019) 171801 [arXiv:1810.10543] [INSPIRE].  
[62] C.V. Cappiello, K.C.Y. Ng and J.F. Beacom, Reverse Direct Detection: Cosmic Ray Scattering With Light Dark Matter, Phys. Rev. D 99 (2019) 063004 [arXiv:1810.07705] [INSPIRE].  
[63] D. Kim, J.-C. Park and S. Shin, Searching for boosted dark matter via dark-photon bremsstrahlung, Phys. Rev. D 100 (2019) 035033 [arXiv:1903.05087] [INSPIRE].  
[64] C.V. Cappiello and J.F. Beacom, *Strong New Limits on Light Dark Matter from Neutrino Experiments*, Phys. Rev. D 100 (2019) 103011 [Erratum ibid. 104 (2021) 069901] [arXiv:1906.11283] [INSPIRE].  
[65] J.B. Dent, B. Dutta, J.L. Newstead and I.M. Shoemaker, Bounds on Cosmic Ray-Boosted Dark Matter in Simplified Models and its Corresponding Neutrino-Floor, Phys. Rev. D 101 (2020) 116007 [arXiv:1907.03782] [INSPIRE].  
[66] G. Krnjaic and S.D. McDermott, Implications of BBN Bounds for Cosmic Ray Upscattered Dark Matter, Phys. Rev. D 101 (2020) 123022 [arXiv:1908.00007] [INSPIRE].  
[67] W. Wang et al., Cosmic ray boosted sub-GeV gravitationally interacting dark matter in direct detection, JHEP 12 (2020) 072 [Erratum ibid. 02 (2021) 052] [arXiv:1912.09904] [INSPIRE].  
[68] G. Guo, Y.-L.S. Tsai and M.-R. Wu, Probing cosmic-ray accelerated light dark matter with IceCube, JCAP 10 (2020) 049 [arXiv:2004.03161] [INSPIRE].  
[69] S.-F. Ge, J. Liu, Q. Yuan and N. Zhou, Diurnal Effect of Sub-GeV Dark Matter Boosted by Cosmic Rays, Phys. Rev. Lett. 126 (2021) 091804 [arXiv:2005.09480] [INSPIRE].  
[70] Q.-H. Cao, R. Ding and Q.-F. Xiang, Searching for sub-MeV boosted dark matter from xenon electron direct detection, Chin. Phys. C 45 (2021) 045002 [arXiv:2006.12767] [INSPIRE].  
[71] C. Xia, Y.-H. Xu and Y.-F. Zhou, Constraining light dark matter upscattered by ultrahigh-energy cosmic rays, Nucl. Phys. B 969 (2021) 115470 [arXiv:2009.00353] [INSPIRE].  
[72] V.V. Flambaum, L. Su, L. Wu and B. Zhu, New Strong Bounds on sub-GeV Dark Matter from Boosted and Migdal Effects, arXiv:2012.09751 [INSPIRE].  
[73] PROSPECT and PROSPECT collaborations, Limits on sub-GeV dark matter from the PROSPECT reactor antineutrino experiment, Phys. Rev. D 104 (2021) 012009 [arXiv:2104.11219] [INSPIRE].  
[74] N.F. Bell et al., Cosmic-ray upscattered inelastic dark matter, Phys. Rev. D 104 (2021) 076020 [arXiv:2108.00583] [INSPIRE].  
[75] J.-C. Feng et al., Revising inelastic dark matter direct detection by including the cosmic ray acceleration, JHEP 04 (2022) 080 [arXiv:2110.08863] [INSPIRE].

[76] W. Wang, L. Wu, W.-N. Yang and B. Zhu, Spin-dependent scattering of boosted dark matter, Phys. Rev. D 107 (2023) 073002 [arXiv:2111.04000] [INSPIRE].  
[77] C. Xia, Y.-H. Xu and Y.-F. Zhou, Production and attenuation of cosmic-ray boosted dark matter, JCAP 02 (2022) 028 [arXiv:2111.05559] [INSPIRE].  
[78] J.-W. Wang, A. Granelli and P. Ullio, Direct Detection Constraints on Blazar-Boosted Dark Matter, Phys. Rev. Lett. 128 (2022) 221104 [arXiv:2111.13644] [INSPIRE].  
[79] PANDAX-II collaboration, Search for Cosmic-Ray Boosted Sub-GeV Dark Matter at the PandaX-II Experiment, Phys. Rev. Lett. 128 (2022) 171801 [arXiv:2112.08957] [INSPIRE].  
[80] CDEX collaboration, Constraints on sub-GeV dark matter boosted by cosmic rays from the CDEX-10 experiment at the China Jinping Underground Laboratory, Phys. Rev. D 106 (2022) 052008 [arXiv:2201.01704] [INSPIRE].  
[81] A. Granelli, P. Ullio and J.-W. Wang, *Blazar-boosted dark matter at Super-Kamiokande*, JCAP 07 (2022) 013 [arXiv:2202.07598] [INSPIRE].  
[82] C. Xia, Y.-H. Xu and Y.-F. Zhou, Azimuthal asymmetry in cosmic-ray boosted dark matter flux, Phys. Rev. D 107 (2023) 055012 [arXiv:2206.11454] [INSPIRE].  
[83] G. Elor, R. McGehee and A. Pierce, Maximizing Direct Detection with Highly Interactive Particle Relic Dark Matter, Phys. Rev. Lett. 130 (2023) 031803 [arXiv:2112.03920] [INSPIRE].  
[84] V.A. Bednyakov and F. Simkovic, Nuclear spin structure in dark matter search: The zero momentum transfer limit, Phys. Part. Nucl. 36 (2005) 131 [hep-ph/0406218] [INSPIRE].