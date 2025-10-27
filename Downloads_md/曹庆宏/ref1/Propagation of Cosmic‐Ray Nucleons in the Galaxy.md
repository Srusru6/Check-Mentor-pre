# PROPAGATION OF COSMIC-RAY NUCLEONS IN THE GALAXY

ANDREW W. STRONG<sup>1</sup> AND IGOR V. MOSKALENKO<sup>1,2</sup>

Received 1998 February 17; accepted 1998 July 13

# ABSTRACT

We describe a method for the numerical computation of the propagation of primary and secondary nucleons, primary electrons, and secondary positrons and electrons. Fragmentation and energy losses are computed using realistic distributions for the interstellar gas and radiation fields, and diffusive reacceleration is also incorporated. The models are adjusted to agree with the observed cosmic-ray B/C and  $^{10}\mathrm{Be} / ^{9}\mathrm{Be}$  ratios. Models with diffusion and convection do not account well for the observed energy dependence of B/C, while models with reacceleration reproduce this easily. The height of the halo propagation region is determined using recent  $^{10}\mathrm{Be} / ^{9}\mathrm{Be}$  measurements as  $>4$  kpc for diffusion/convection models and 4-12 kpc for reacceleration models. For convection models, we set an upper limit on the velocity gradient of  $dV/dz < 7$  km s $^{-1}$  kpc $^{-1}$ . The radial distribution of cosmic-ray sources required is broader than current estimates of the supernova remnant (SNR) distribution for all halo sizes. Full details of the numerical method used to solve the cosmic-ray propagation equation are given.

Subject headings: acceleration of particles — cosmic rays — diffusion — Galaxy: general — ISM: abundances — ISM: general

# 1. INTRODUCTION

A numerical method and corresponding computer code for the calculation of Galactic cosmic-ray propagation has been developed, building on the approach described by Strong & Youssefi (1995) and Strong (1996). Primary and secondary nucleons, primary and secondary electrons, and secondary positrons are included. The basic spatial propagation mechanisms are (momentum-dependent) diffusion and convection, while energy loss and diffusive reacceleration are treated in momentum space. Fragmentation and energy losses are computed using realistic distributions for the interstellar gas and radiation fields. Preliminary results were presented in Strong & Moskalenko (1997; hereafter Paper I), and full results for protons, helium, positrons, and electrons were presented in Moskalenko & Strong (1998a; hereafter Paper II). In Paper II, we referred the description of the numerical method to the present paper (Paper III), and full details are now given. Results for gamma rays and synchrotron radiation will be given in Moskalenko & Strong (1998b; hereafter Paper IV).

We note that our positron predictions from Paper II have been compared with more recent absolute measurements in Barwick et al. (1998), with good agreement; for the positrons, this new comparison has the advantage of being independent of the electron spectrum, unlike the positron/ electron ratio that was the main focus of Paper II. The ultimate goal is to combine all constraints, including gamma-ray and synchrotron spectra; this will be pursued in Paper IV.

The rationale for our approach has been given previously (Paper I, Paper II). Briefly, the idea is to develop a model that simultaneously reproduces observational data of many kinds related to cosmic-ray origin and propagation: directly via measurements of nuclei, electrons, and positrons; indirectly via gamma rays and synchrotron radi-

ation. These data provide many independent constraints on any model, and our approach is able to take advantage of this, since it must be consistent with all types of observation. We also emphasize the use of realistic astrophysical inputs (e.g., for the gas distribution) as well as theoretical developments (e.g., reacceleration). The code is sufficiently general that new physical effects can be introduced as required. We aim to generate a standard model that can be improved with new astrophysical inputs and additional observational constraints. For interested users, our model is available on our web site.<sup>3</sup>

It was pointed out many years ago (see Ginzburg, Khazan, & Ptuskin 1980; Berezinskii et al. 1990) that the interpretation of radioactive cosmic-ray nuclei is model dependent, and in particular that halo models lead to a physical picture that is quite different from that of homogeneous models. The latter simply show a rather lower average matter density than the local Galactic hydrogen (e.g., Simpson & Garcia-Munoz 1988; Lukasiak et al. 1994a), but do not lead to a meaningful estimate of the size of the confinement region, and the corresponding cosmic-ray lifetime is model dependent. In such treatments, the lifetime is combined with the grammage to yield an average density. For example, Lukasiak et al. (1994a) find an average density of  $0.28~\mathrm{cm}^{-3}$ , compared to the local interstellar value of about  $1~\mathrm{cm}^{-3}$ , indicating a  $z$ -extent of less than  $1\mathrm{kpc}$ , compared to the several kpc found in diffusive halo models. In the present work, we use a model that includes spatial dimensions as a basic element, and so these issues are automatically addressed.

The possible role of convection was demonstrated by Jokipii (1976), and Jones (1979) pointed out its effect on the energy dependence of the secondary/primary ratio. Recent papers give estimates for the halo size and limits on convection based on existing calculations (e.g., Webber, Lee, & Gupta 1992); in the present work, we attempt to improve on these models with a more detailed treatment.

Previous approaches to the spatial nucleon propagation problem have been mainly analytical: Jones (1979), Freedman et al. (1980), Berezinskii et al. (1990), Webber et al. (1992), and Bloemen et al. (1993) treated diffusion/ convection models in this way. One problem here is that energy losses are difficult to treat, and in fact were apparently not included in any of the above analyses except Webber et al. (1992)—although even there not explicitly. Bloemen et al. (1993) used the “grammage” formulation rather than the explicit isotope ratios, and their propagation equation implicitly assumes identical distributions of primary and secondary source functions. These papers did not attempt to fit the low-energy  $(< 1\mathrm{GeV}$  nucleon $^{-1}$ ) B/C data (which we will show leads to problems), and also did not consider reacceleration. It is clear that an analytical treatment quickly becomes limited as soon as more realistic models are desired; this is the main justification for the numerical approach presented in this paper. The case of electrons and positrons is even more intractable analytically, although fairly general cases have been treated (Lerche & Schlickeiser 1982). Owens & Jokipii (1977a, 1977b) adopted an alternative approach with Monte Carlo simulations for both nucleons and electrons. Recently, Porter & Protheroe (1997) made use of this method for electrons. Both of these applications are for one-dimensional propagation in the  $z$ -direction only. This method allows realistic models to be computed, but would be very time-consuming for two- or three-dimensional cases. Our method, using a numerical solution of the propagation equation, is a practical alternative. Since most of these studies were done, the data on both stable and radioactive nuclei has improved considerably, and thus a reevaluation is warranted.

Reacceleration has previously been handled using leaky-box calculations (Letaw, Silberberg, & Tsao 1993; Seo & Ptuskin 1994; Heinbach & Simon 1995); this has the advantage of allowing a full reaction network to be used (far beyond what is possible in the present approach), but suffers from the usual limitations of leaky-box models, especially concerning radioactive nuclei, which were not included in these treatments. Our simplified reaction network is necessary because of the added spatial dimensions, but we believe it is fully sufficient for our purpose, since we are not attempting to derive a comprehensive isotopic composition. A similar approach was followed by Webber et al. (1992). A more complex reaction scheme would not in any way change our conclusions.

We model convection in a simple way, taking a linear increase of velocity with  $z$ . Detailed self-consistent models of cosmic ray-driven magnetohydrodynamic (MHD) winds (Zirakashvili et al. 1996; Ptuskin et al. 1997) provide explicit predictions for the convective transport of cosmic rays, and our approach could be used in future to evaluate the observational consequences of such models.

In this paper we concentrate on the evaluation of the B/C and  $^{10}\mathrm{Be} / ^{9}\mathrm{Be}$  ratios, evaluation of diffusion/convection and reacceleration models, and on setting limits to the halo size. The B/C data is used because it is the most accurately measured ratio covering a wide energy range and having well-established cross sections. The  $^{10}\mathrm{Be} / ^{9}\mathrm{Be}$  ratio is used rather than  $^{10}\mathrm{Be} / (^{7}\mathrm{Be} + ^{9}\mathrm{Be})$  because it is less sensitive to solar modulation and to rigidity effects in the propagation. A reevaluation of the halo size is desirable, since new  $^{10}\mathrm{Be} / ^{9}\mathrm{Be}$  data are now available from Ulysses (Connell 1998), with

better statistics than previously. It is not the purpose of this approach to perform detailed source abundance calculations with a large network of reactions, which is still best done with the path-length distribution approach (DuVernois, Simpson, & Thayer 1996 and references therein). Instead, we use only the principal progenitors and weighted cross sections based on the observed cosmic-ray abundances (see Webber et al. 1992). Other key cosmic-ray ratios, such as  $^{26}\mathrm{Al} / ^{27}\mathrm{Al}$  and sub-Fe/Fe, are beyond the scope of this paper, but will be addressed in future work.

Also important are cosmic-ray gradients derived from gamma rays; this provides a consistency check on the distribution of cosmic-ray sources, and we address this here.

# 2.DESCRIPTION OF THE MODELS

The models are three-dimensional, with cylindrical symmetry in the Galaxy; the basic coordinates are  $(R,z,p)$ , where  $R$  is Galactocentric radius,  $z$  is the distance from the Galactic plane, and  $p$  is the total particle momentum. The distance from the Sun to the Galactic center is taken as 8.5 kpc. The propagation region in the models is bounded by  $R = R_{h}$  and  $z = z_{h}$ , beyond which free escape is assumed. We take  $R_{h} = 30\mathrm{kpc}$ . The range  $z_{h} = 1 - 20\mathrm{kpc}$  is considered, since this is suggested by previous studies of radioactive nuclei (e.g., Lukasiak et al. 1994a) and the distribution of synchrotron radiation (Phillips et al. 1981). For a given  $z_{h}$ , the diffusion coefficient as a function of momentum is determined by B/C for the case of no reacceleration; if reacceleration is assumed, then the reacceleration strength (related to the Alfven speed) is constrained by the energy dependence of B/C. The spatial diffusion coefficient for the case of no reacceleration is taken as  $D_{xx} = \beta D_0(\rho /\rho_0)^{\delta_1}$  below rigidity  $\rho_0$  and  $\beta D_0(\rho /\rho_0)^{\delta_2}$  above rigidity  $\rho_0$ , where the factor  $\beta (= v / c)$  is a natural consequence of a random-walk process. Since the introduction of a sharp break in  $D_{xx}$  is an extremely contrived procedure that is adopted simply to fit B/C at all energies, we also consider the case of  $\delta_1 = \delta_2$ , i.e., with no break, in order to investigate the possibility of reproducing the data in a physically simpler way. The convection velocity (in the  $z$ -direction only),  $V(z)$ , is assumed to increase linearly with distance from the plane ( $V > 0$  for  $z > 0$ ,  $V < 0$  for  $z < 0$ , and  $dV / dz > 0$  for all  $z$ ). This implies a constant adiabatic energy loss; the possibility of adiabatic energy gain ( $dV / dz < 0$ ) is not considered. The linear form for  $V(z)$  is consistent with cosmic ray-driven MHD wind models (e.g., Zirakashvili et al. 1996). The velocity at  $z = 0$  is a model parameter, but here we consider only  $V(0) = 0$ .

Some stochastic reacceleration is inevitable, and it provides a natural mechanism for reproducing the energy dependence of the B/C ratio without an ad hoc form for the diffusion coefficient (Letaw et al. 1993; Seo & Ptuskin 1994; Heinbach & Simon 1995; Simon & Heinbach 1996). The spatial diffusion coefficient for the case of reacceleration assumes a Kolmogorov spectrum of weak MHD turbulence, so  $D_{xx} = \beta D_0(\rho /\rho_0)^{\delta}$  with  $\delta = \frac{1}{3}$  for all rigidities. Simon & Heinbach (1996) showed that the Kolmogorov form best reproduces the observed B/C variation with energy. For the case of reacceleration, the momentum-space diffusion coefficient  $D_{pp}$  is related to the spatial coefficient

using the formula given by Seo & Ptuskin (1994; their eq. [9]) and Berezinskii et al. (1990):

$$
D _ {p p} D _ {x x} = \frac {4 p ^ {2} v _ {\mathrm {A}} ^ {2}}{3 \delta (4 - \delta^ {2}) (4 - \delta) w}, \tag {1}
$$

where  $w$  characterizes the level of turbulence and is equal to the ratio of MHD wave energy density to magnetic field energy density. The main free parameter in this relation is the Alfven speed,  $v_{\mathrm{A}}$ ; we take  $w = 1$  (Seo & Ptuskin 1994), but clearly only the quantity  $v_{\mathrm{A}}^2 / w$  is relevant.

The atomic hydrogen distribution is represented by the formula

$$
n _ {\mathrm {H I}} (R, z) = n _ {\mathrm {H I}} (R) e ^ {- (\ln 2) \left(z / z _ {0}\right) ^ {2}}, \tag {2}
$$

where  $n_{\mathrm{HI}}(R)$  is taken from Gordon & Burton (1976) and  $z_0$  from Cox, Krugel, & Mezger (1986), giving an exponential increase in the width of the H I layer outside the solar circle:

$$
z _ {0} (R) = \left\{ \begin{array}{l l} 0. 2 5 \mathrm {k p c}, & R \leq 1 0 \mathrm {k p c} \\ 0. 0 8 3 e ^ {0. 1 1 R} \mathrm {k p c}, & R > 1 0 \mathrm {k p c}. \end{array} \right. \tag {3}
$$

The distribution of molecular hydrogen is taken from Bronfman et al. (1988) using CO surveys:

$$
n _ {\mathrm {H} _ {2}} (R, z) = n _ {\mathrm {H} _ {2}} (R) e ^ {- (\ln 2) (z / 7 0 \mathrm {p c}) ^ {2}}. \tag {4}
$$

The adopted radial distribution of  $\mathbf{H}^{\mathrm{I}}$  and  $\mathbf{H}_2$  is shown in Figure 1.

For the ionized gas, we use the two-component model of Cordes et al. (1991):

$$
\begin{array}{l} n _ {\mathrm {H I I}} = 0. 0 2 5 \exp \left[ - \frac {| z |}{1 \mathrm {k p c}} - \left(\frac {R}{2 0 \mathrm {k p c}}\right) ^ {2} \right] \\ + 0. 2 \exp \left[ - \frac {| z |}{0 . 1 5 \mathrm {k p c}} - \left(\frac {R}{2 \mathrm {k p c}} - 2\right) ^ {2} \right] \mathrm {c m} ^ {- 3}. \tag {5} \\ \end{array}
$$

The first term represents the extensive warm ionized gas and is similar to the distribution given by Reynolds (1989); the second term represents H II regions and is concentrated around  $R = 4$  kpc. A temperature of  $10^{4}$  K is assumed in order to compute Coulomb energy losses in ionized gas.

The He/H ratio of the interstellar gas is taken to be 0.11 by number; there is some uncertainty in this quantity, but our value is consistent with recent photospheric determini

![](images/ae2c39c26b0ed9067ad2e8f77907b2901fdc205825e433f64b678f670f7d117b.jpg)  
FIG. 1. Adopted radial distribution of atomic, molecular, and ionized hydrogen at  $z = 0$ .

nations  $(0.10 \pm 0.008$ ; see Grevesse, Noels, & Savuval 1996). Helioseismological methods (Hernandez & Christensen-Dalsgaard 1994) give a helium abundance by mass of 0.242, corresponding to  $\mathrm{He} / \mathrm{H} = 0.08$ , but still with possible uncertainties due to the details of the models. Although the latter is perhaps the most accurate local determination, the uncertainty in extending the photospheric value to the interstellar medium over the whole Galaxy is large. Other uncertainties dominate the secondary production; for example, the density of neutral and molecular hydrogen. In any case, even if  $\mathrm{He} / \mathrm{H} = 0.08$ , the influence of the uncertainty of  $\mathrm{He} / \mathrm{H}$  on the secondary production does not exceed  $10\%$ .

The distribution of cosmic-ray sources is chosen to reproduce (after propagation) the cosmic-ray distribution determined by analysis of EGRET gamma-ray data (Strong & Mattox 1996). The form used is

$$
q (R, z) = q _ {0} \left(\frac {R}{R _ {\odot}}\right) ^ {\eta} \exp \left(- \xi \frac {R - R _ {\odot}}{R _ {\odot}} - \frac {| z |}{0 . 2 k p c}\right), \tag {6}
$$

where  $q_0$  is a normalization constant and  $\eta$  and  $\xi$  are parameters; the  $R$ -dependence has the same parameterization as that used for supernovae remnants (SNRs) by Case & Bhattacharya (1996), but we adopt different parameters in order to fit the gamma-ray gradient. We also compute models with the SNR distribution, in order to investigate the possibility of fitting the gradient in this case. We apply a cutoff in the source distribution at  $R = 20$  kpc, since it is unlikely that significant sources are present at such large radii. The  $z$ -dependence of  $q$  is nominal and simply reflects the assumed confinement of sources to the disk.

We assume that the source distribution of all cosmic-ray primaries is the same. Meyer, Drury, & Ellison (1997) suggest that part of the C and O originates in acceleration of C- and O-enriched pre-SN Wolf-Rayet wind material by supernovae, but the source distribution in this case would still follow that of SNRs.

First, the primary propagation is computed giving the primary distribution as a function of  $(R, z, p)$ ; then the secondary source function is obtained from the gas density and cross sections, and finally the secondary propagation is computed. Tertiary reactions such as  $^{11}\mathbf{B} \rightarrow {}^{10}\mathbf{B}$  are treated as described in Appendix A. The entire calculation is performed with momentum as the kinematic variable, since this greatly facilitates the inclusion of reacceleration.

Full details of the propagation equation and numerical method used are given in Appendices A and B. The method encompasses nucleons, electrons, and positrons. Energy losses for nucleons by ionization and Coulomb interactions are included, following Mannheim & Schlickeiser (1994) (see Appendix C.1). Details of the positron source function, magnetic field, and interstellar radiation field models were given in Paper II, and the energy loss formulae for electrons are given in Appendix C.2.

As an illustration of the calculations performed by the code, Figure 2 shows the  $(R,z)$  distribution of primary  $^{12}\mathrm{C}$  and secondary  $^{10,11}\mathrm{B}$  at  $515\mathrm{MeV}$  nucleon $^{-1}$  for a reacceleration model with  $z_{h} = 10$  kpc. In practice, we are only interested in the isotope ratios at the solar position, but it is worth noting the variations over the Galaxy, which are attributable to the effect of the inhomogeneous distribution of sources and gas on the secondary production, fragmenta

![](images/f00181bacf108d873f09dc94b884c1e0648d27a8037415e47ed99145db5d4b9e.jpg)

![](images/74796df70cd979dc751322274e270b1170fb75e72df3c829d3b9275ccf21328a.jpg)  
FIG. 2. Three-dimensional distribution of  $^{12}\mathrm{C}$  and  $^{10,11}\mathrm{B}$  at 515 MeV nucleon  $^{-1}$  for reacceleration model with  $z_{h} = 10$  kpc, for  $v_{\mathrm{A}} = 20$  km s  $^{-1}$ . For parameters, see model 10500 in Table 2.

tion, and energy losses. For comparison with gamma-ray data, the full three-dimensional distribution is of course important and will be addressed in Paper IV, but here only the radial cosmic-ray gradient from gamma rays is considered.

# 3. EVALUATION OF MODELS

We consider the cases of diffusion + convection and diffusion + reacceleration, since these are the minimum combinations that can reproduce the key observations. In

principle, all three processes could be significant, and such a general model could be considered if independent astrophysical information or models, for example for a Galactic wind (e.g., Zirakashvili et al. 1996; Ptuskin et al. 1997), were to be used. Anticipating the results, it can be noted at the outset that the reacceleration models are more satisfactory in meeting the constraints provided by the data, reproducing the B/C energy dependence without ad hoc variations in the diffusion coefficient; furthermore, it is not possible to find any simple version of the diffusion/

TABLE 1 PARAMETERS OF DIFFUSION/CONVECTION MODELS  

<table><tr><td>Model</td><td>zh(kpc)</td><td>D0cm2s-1)</td><td>ρ0(GV)</td><td>δ1</td><td>δ2</td><td>dV/dz(km s-1kpc-1)</td></tr><tr><td>01000</td><td>1</td><td>0.7</td><td>3</td><td>0.60</td><td>0.60</td><td>0</td></tr><tr><td>01010</td><td>1</td><td>0.7</td><td>3</td><td>0.60</td><td>0.60</td><td>10</td></tr><tr><td>01020</td><td>1</td><td>0.7</td><td>3</td><td>0.60</td><td>0.60</td><td>20</td></tr><tr><td>03000</td><td>3</td><td>2.0</td><td>3</td><td>0.60</td><td>0.60</td><td>0</td></tr><tr><td>03010</td><td>3</td><td>1.4</td><td>3</td><td>0.65</td><td>0.65</td><td>10</td></tr><tr><td>03020</td><td>3</td><td>1.1</td><td>3</td><td>0.70</td><td>0.70</td><td>20</td></tr><tr><td>10000</td><td>10</td><td>5.0</td><td>3</td><td>0.60</td><td>0.60</td><td>0</td></tr><tr><td>10010</td><td>10</td><td>2.5</td><td>3</td><td>0.70</td><td>0.70</td><td>10</td></tr><tr><td>10020</td><td>10</td><td>1.1</td><td>3</td><td>0.90</td><td>0.90</td><td>20</td></tr><tr><td>01100</td><td>1</td><td>0.9</td><td>5</td><td>-0.60</td><td>0.60</td><td>0</td></tr><tr><td>01105</td><td>1</td><td>0.8</td><td>5</td><td>-0.60</td><td>0.60</td><td>5</td></tr><tr><td>01110</td><td>1</td><td>0.8</td><td>5</td><td>-0.60</td><td>0.60</td><td>10</td></tr><tr><td>03100</td><td>3</td><td>2.5</td><td>5</td><td>-0.60</td><td>0.60</td><td>0</td></tr><tr><td>03105</td><td>3</td><td>2.2</td><td>5</td><td>-0.60</td><td>0.60</td><td>5</td></tr><tr><td>03110</td><td>3</td><td>2.0</td><td>5</td><td>-0.60</td><td>0.60</td><td>10</td></tr><tr><td>04100</td><td>4</td><td>3.5</td><td>5</td><td>-0.60</td><td>0.60</td><td>0</td></tr><tr><td>04105</td><td>4</td><td>2.7</td><td>5</td><td>-0.60</td><td>0.70</td><td>5</td></tr><tr><td>04110</td><td>4</td><td>2.5</td><td>5</td><td>-0.60</td><td>0.70</td><td>10</td></tr><tr><td>05100</td><td>5</td><td>4.5</td><td>5</td><td>-0.60</td><td>0.60</td><td>0</td></tr><tr><td>05105</td><td>5</td><td>3.2</td><td>5</td><td>-0.60</td><td>0.70</td><td>5</td></tr><tr><td>05110</td><td>5</td><td>2.5</td><td>5</td><td>-0.60</td><td>0.70</td><td>10</td></tr><tr><td>10100</td><td>10</td><td>7.0</td><td>5</td><td>-0.60</td><td>0.60</td><td>0</td></tr><tr><td>10105</td><td>10</td><td>3.8</td><td>5</td><td>-0.60</td><td>0.80</td><td>5</td></tr><tr><td>10110</td><td>10</td><td>3.0</td><td>5</td><td>-0.60</td><td>0.80</td><td>10</td></tr><tr><td>15100</td><td>15</td><td>9.0</td><td>5</td><td>-0.60</td><td>0.60</td><td>0</td></tr><tr><td>15105</td><td>15</td><td>3.8</td><td>5</td><td>-0.60</td><td>0.80</td><td>5</td></tr><tr><td>15110</td><td>15</td><td>3.0</td><td>5</td><td>-0.60</td><td>0.80</td><td>10</td></tr><tr><td>20100</td><td>20</td><td>9.0</td><td>5</td><td>-0.60</td><td>0.60</td><td>0</td></tr><tr><td>20105</td><td>20</td><td>3.8</td><td>5</td><td>-0.60</td><td>0.80</td><td>5</td></tr><tr><td>20110</td><td>20</td><td>3.0</td><td>5</td><td>-0.60</td><td>0.80</td><td>10</td></tr></table>

convection model that reproduces B/C satisfactorily without additional special assumptions.

In our calculations we use the B/C data summarized by Webber et al. (1996) from HEAO 3 and Voyager 1 and 2. The spectra were modulated to  $500\mathrm{MV}$ , appropriate to this data, using the force-field approximation (Gleeson & Axford 1968). We also show B/C values from Ulysses (DuVernois et al. 1996) for comparison, but since this has large modulation  $(600 - 1080\mathrm{MV})$ , we do not base conclusions on these values. We use the measured  ${}^{10}\mathrm{Be}/{}^{9}\mathrm{Be}$  ratio from Ulysses (Connell 1998) and from Voyager 1 and 2, Interplanetary Monitoring Platform (IMP) 7/8, and ISEE 3, as summarized by Lukasiak et al. (1994a).

The source distribution adopted has  $\eta = 0.5$ ,  $\xi = 1.0$  in equation (6) (except for the cases with SNR source distribution). This form adequately reproduces the small observed gamma ray-based gradient for all  $z_{h}$ ; a more detailed discussion is given in §4.

# 3.1. Diffusion/Convection Models

The main parameters for this model are  $z_{h}$ ,  $D_{0}$ ,  $\delta_{1}$ ,  $\delta_{2}$ ,  $\rho_{0}$ , and  $dV / dz$ . We treat  $z_{h}$  as the main unknown quantity, and consider values of 1-20 kpc. The parameters of these models are summarized in Table 1. For a given  $z_{h}$ , we show B/C for a series of models with different  $dV / dz$ .

Figure 3 shows the case with no break,  $\delta_{1} = \delta_{2}$ ; for each  $dV / dz$ , the remaining parameters  $D_0$ ,  $\delta_{1}$ , and  $\rho_0$  are adjusted to fit the data as well as possible. It is clear that a good fit is not possible; the basic effect of convection is to reduce the variation of B/C with energy, and although this improves the fit at low energies, the characteristic peaked shape of the measured B/C cannot be reproduced. Although modulation makes the comparison with the low-energy Voyager data

somewhat uncertain, Figure 3 shows that the fit is unsatisfactory; the same is true even if we use a very low modulation parameter of  $300\mathrm{MV}$  in an attempt to improve the fit. This modulation is near the minimum value for the entire Voyager 17 yr period (cf. the average value of  $500\mathrm{MV}$ ; Webber et al. 1996). The failure to obtain a good fit is an important conclusion, since it shows that the simple inclusion of convection cannot solve the problem of the low-energy falloff in B/C.

Since the inclusion of a convective term is nevertheless of interest for independent astrophysical reasons (Galactic wind), we can force a fit to the data by allowing a break in  $D_{xx}(p)$ , with  $\delta_1 \neq \delta_2$ . Figure 4 shows cases with a break; here the parameters  $D_0, \delta_1, \delta_2$ , and  $\rho_0$  are adjusted. In the absence of convection, the falloff in  $\mathbf{B} / \mathbf{C}$  at low energies requires that the diffusion coefficient increase rapidly below  $\rho_0 = 3\mathrm{GV}(\delta_1 \sim -0.6)$ , reversing the trend from higher energies  $(\delta_2 \sim +0.6)$ . Inclusion of the convective term does not reduce the size of the ad hoc break in the diffusion coefficient; in fact, it rather exacerbates the problem by requiring a larger break.

Figure 5 shows the predicted and measured  $^{10}\mathrm{Be} / ^{9}\mathrm{Be}$  ratio; here we use the models with a break in  $D_{xx}(p)$ , since these do have the correct B/C ratio in the few 100 MeV nucleon  $^{-1}$  range where the Be measurements are available, and are therefore appropriate for this comparison independ-

<sup>5</sup> Note that the dependence of interaction rate on particle velocity itself is not sufficient to cause the full observed low-energy falloff. In leaky-box treatments, the low-energy behavior is modeled by adopting a constant path length below a few GeV nucleon  $^{-1}$ , without attempting to justify this physically. A convective term is often invoked, but our treatment shows that this alone is not sufficient.

![](images/89669c4fd1ea7e8c1e35002a0cb0c16779d770495fcddf99f021f9ac3d5070b1.jpg)

![](images/692fdfc97234c7e4b9114a118e8d19481ac4d27c777417be184640da1285e666.jpg)

![](images/b357e9598675fabef6499bcc850352aea108cba82987312ed3a994ee0800f28e.jpg)  
FIG. 3.—B/C ratio for diffusion/convection models without a break in the diffusion coefficient, for  $dV/dz = 0$  (solid lines), 5 (dotted lines), and 10 (dashed lines)  $\mathrm{km~s^{-1}~kpc^{-1}}$ . The cases shown are (top left)  $z_{h} = 1$  kpc, (top right)  $z_{h} = 3$  kpc, and (bottom)  $z_{h} = 10$  kpc. Solid lines, interstellar ratio; shaded area, modulated to  $300 - 500\mathrm{MV}$ . For the data, vertical bars are from HEAO 3 and Voyager (Webber et al. 1996); filled circles are from Ulysses (DuVernois et al. 1996:  $\Phi = 600$ , 840, and  $1080\mathrm{MV}$ ). Parameters are given in Table 1.

dently of the situation at higher energies. For our final evaluation, we use  $^{10}\mathrm{Be} / ^{9}\mathrm{Be}$  data from Ulysses, which has the highest statistics.

Figure 6 summarizes the limits on  $z_{h}$  and  $dV / dz$ , using the  $^{10}\mathrm{Be} / ^{9}\mathrm{Be}$  ratio at the interstellar energy of 525 MeV nucleon  $^{-1}$  appropriate to the Ulysses data (Connell 1998). For  $z_{h} < 4$  kpc, the predicted ratio is always too high, even for no convection; no convection is allowed for such  $z_{h}$  values, since this increases  $^{10}\mathrm{Be} / ^{9}\mathrm{Be}$  still further. For  $z_{h} \geq 4$  kpc, agreement with  $^{10}\mathrm{Be} / ^{9}\mathrm{Be}$  is possible, provided that  $0 < dV / dz < 7$  km s  $^{-1}$  kpc  $^{-1}$ . We conclude from Figure 6a that in the absence of convection, 4 kpc  $< z_{h} < 12$  kpc, and if convection is allowed, the lower limit remains but no

upper limit can be set. It is interesting that an upper as well as a lower limit on  $z_{h}$  is obtained in the case of no convection, although  $^{10}\mathrm{Be}/^9\mathrm{Be}$  approaches asymptotically a constant value for large halo sizes and becomes insensitive to the halo dimension. From Figure 6b,  $dV/dz < 7 \, \mathrm{km} \, \mathrm{s}^{-1} \, \mathrm{kpc}^{-1}$ , and this figure places upper limits on the convection parameter for each halo size. These limits are rather strict, and a finite wind velocity is only allowed in any case for  $z_{h} > 4 \, \mathrm{kpc}$ . Note that these results are not very sensitive to modulation, since the predicted  $^{10}\mathrm{Be}/^9\mathrm{Be}$  is fairly constant from 100 to 1000 MeV nucleon  $^{-1}$ .

Our results can be compared with those of other studies:  $z_{h} \geq 7.8$  kpc (Freedman et al. 1980),  $z_{h} \leq 3$  kpc (Bloemen et

![](images/36066ba71a607b732be159ab063c0f54a001ae1b198e15cc24bb851f034d861b.jpg)

![](images/02d1d4d0ff20c894f275950a99efb559d55242d19e537cb36d54575cc039ebf2.jpg)

![](images/3abc6e80fba58caeb7285a2b2c0d0d72a88e054a6e65e6e55bb60e282a317d65.jpg)  
FIG. 4.—B/C ratio for diffusion/convection models with a break in the diffusion coefficient, for  $dV/dz = 0$  (solid lines), 5 (dotted lines), and 10 (dashed lines)  $\mathrm{km~s^{-1}~kpc^{-1}}$ . The cases shown are (top left)  $z_{h} = 1\mathrm{kpc}$ , (top right)  $z_{h} = 5\mathrm{kpc}$ , and (bottom)  $z_{h} = 20\mathrm{kpc}$ . Lower lines, interstellar ratio; upper lines, modulated to  $500\mathrm{MV}$ . Parameters are given in Table 1. Data are as in Fig. 3.

al. 1993), and  $z_{h} \leq 4$  kpc (Webber et al. 1992). Most recently, Lukasiak et al. (1994a) found  $1.9$  kpc  $< z_{h} < 3.6$  kpc (for no convection) based on Voyager Be data and using the Webber et al. (1992) models. We believe our new limits to be an improvement, first because of the improved Be data from Ulysses, and second because of our treatment of energy losses (see § 3.2) and the generally more realistic astrophysical details in our model. The papers cited also did not consider the low-energy B/C data, which we have shown are in fact a problem for diffusion/convection models.

The cosmic ray-driven wind models of Zirakashvili et al. (1996) have values of  $dV / dz \approx 10\mathrm{km~s}^{-1}\mathrm{kpc}^{-1}$ , somewhat larger than our upper limits. Since their models differ from ours in many respects, this is not significant, but it suggests

that it would be useful to carry out calculations like those in the present paper for such models, to provide a critical test of their viability.

# 3.2. Diffusive Reacceleration Models

The main parameters for this model are  $z_{h}$ ,  $D_{0}$ , and  $v_{\mathrm{A}}$  ( $\rho_{0}$  is arbitrary, since  $\delta$  is constant). Again, we treat  $z_{h}$  as the main unknown quantity. The evaluation is simpler than for convection models, since the number of free parameters is smaller. The parameters of these models are summarized in Table 2. Figure 7 illustrates the effect on B/C of varying  $v_{\mathrm{A}}$  from  $v_{\mathrm{A}} = 0$  (no reacceleration) to  $v_{\mathrm{A}} = 30 \, \mathrm{km} \, \mathrm{s}^{-1}$ , for  $z_{h} = 5 \, \mathrm{kpc}$ . This shows how the initial form becomes modified to produce the characteristic peaked shape. Reacceleration

![](images/c0e0b66195f8a0b1505b3d695f0cc45c94ec9d2f095dee35837c7b5562cf906a.jpg)

![](images/51b8c76c374489652ca15187295de7d936ac199f94b186831334ee56d214d88f.jpg)

![](images/25d0b755c76b7b5032d1b32268767f96337dea3dde3cc96d9d4db08e0de2b971.jpg)  
FIG. 5.  ${}^{10}\mathrm{Be}/{}^{9}\mathrm{Be}$  ratio for diffusion/convection models, for  $dV/dz = 0$  (solid lines), 5 (dotted lines), and 10 (dashed lines)  $\mathrm{km~s^{-1}~kpc^{-1}}$ . The cases shown are  $(a) z_h = 1\mathrm{kpc}$ ,  $(b) z_h = 5\mathrm{kpc}$ , and  $(c) z_h = 20\mathrm{kpc}$ . Data points are from Lukasiak et al. (1994a) (square, Voyager 1 and 2; open circle, IMP 7/8; triangle, ISEE 3), and Connell (1998) (filled circle, Ulysses). Parameters are given in Table 1.

models thus lead naturally to the observed peaked form of B/C, as pointed out by several previous authors (e.g., Letaw et al. 1993; Seo & Ptuskin 1994; Heinbach & Simon 1995).

Figure 8 shows B/C for  $z_{h} = 1 - 20$  kpc. Our value of  $v_{\mathrm{A}} \approx 20$  km s $^{-1}$  is consistent with the value obtained by Seo & Ptuskin (1994), which they also derived from B/C; since for stable nuclei the leaky-box and diffusion treatments are equivalent, this is a good test of the operation of our code. The value of  $v_{\mathrm{A}}$  is typical of the warm ionized phase of the interstellar gas (Seo & Ptuskin 1994). The exact low-energy form of B/C depends on details of the modulation, so that

an exact fit here is not attempted; note, however, that  $v_{\mathrm{A}}$  and  $D_0$  can be (and indeed were) determined from the high-energy B/C alone; the low-energy agreement is then satisfactory. Figure 9 shows  $^{10}\mathrm{Be} / ^{9}\mathrm{Be}$  for the same models, panel (a) as a function of energy for various  $z_h$ , and panel (b) as a function of  $z_h$  at 525 MeV nucleon  $^{-1}$ , corresponding to the Ulysses measurement. Comparing with the Ulysses data

<sup>6</sup> Since we are considering a ratio at the same rigidity, the effect of modulation is confined to a deceleration of  $\approx 200$  MeV nucleon<sup>-1</sup> (cf. spectra where absolute intensity changes are important).

![](images/6abb7cc7ca975a0adef09d1c2e12040f7f2c8926f66fa2f69e610b30bdfc20b4.jpg)  
FIG. 6.—Predicted  $^{10}\mathrm{Be} / ^{9}\mathrm{Be}$  ratio as function of (a)  $z_{h}$  for  $dV/dz = 0$ , 5, and  $10\mathrm{km~s^{-1}~kpc^{-1}}$ , (b)  $dV/dz$  for  $z_{h} = 1 - 20\mathrm{kpc}$  at  $525\mathrm{MeV}$  nucleon $^{-1}$ , corresponding to the mean interstellar value for the Ulysses data (Connell 1998); the Ulysses experimental limits are shown as horizontal dashed lines. The shaded regions show the parameter ranges allowed by the data.

![](images/c83b8ab1a083ea97ee3697e3ba3d0d0eb5e28e76f246e4bf16ee3479836bd508.jpg)

TABLE 2 PARAMETERS OF DIFFUSIVE REACCELERATION MODELS  

<table><tr><td>Best-fit 
Modelsa</td><td>Models with 
No Energy Lossesa</td><td>Models with SNR 
Source 
Distributionb</td><td>zh(kpc)</td><td>D0cm2s-1)</td><td>vA(km s-1)</td></tr><tr><td>01500......</td><td>01510</td><td>01511</td><td>1</td><td>1.7</td><td>20</td></tr><tr><td>02500......</td><td>02510</td><td>02511</td><td>2</td><td>3.2</td><td>20</td></tr><tr><td>03500......</td><td>03510</td><td>03511</td><td>3</td><td>4.6</td><td>20</td></tr><tr><td>04500......</td><td>04510</td><td>04511</td><td>4</td><td>6.0</td><td>20</td></tr><tr><td>05500......</td><td>05510</td><td>05511</td><td>5</td><td>7.7</td><td>20</td></tr><tr><td>10500......</td><td>10510</td><td>10511</td><td>10</td><td>12</td><td>20</td></tr><tr><td>15500......</td><td>15510</td><td>15511</td><td>15</td><td>15</td><td>20</td></tr><tr><td>20500......</td><td>20510</td><td>20511</td><td>20</td><td>16</td><td>18</td></tr><tr><td colspan="6">Effect of varying vA:</td></tr><tr><td>05501......</td><td>...</td><td>...</td><td>5</td><td>7.7</td><td>0</td></tr><tr><td>05502......</td><td>...</td><td>...</td><td>5</td><td>7.7</td><td>5</td></tr><tr><td>05503......</td><td>...</td><td>...</td><td>5</td><td>7.7</td><td>10</td></tr><tr><td>05504......</td><td>...</td><td>...</td><td>5</td><td>7.7</td><td>15</td></tr><tr><td>05505......</td><td>...</td><td>...</td><td>5</td><td>7.7</td><td>20</td></tr><tr><td>05506......</td><td>...</td><td>...</td><td>5</td><td>7.7</td><td>25</td></tr><tr><td>05507......</td><td>...</td><td>...</td><td>5</td><td>7.7</td><td>30</td></tr></table>

NOTE. For all reacceleration models,  $\rho_0 = 3\mathrm{GV}$ ,  $\delta = 1/3$  (see §2 for details).  
a Parameters of the source distribution (eq. [6]):  $\eta = 0.5$ ,  $\xi = 1.0$ .  
$^{\mathrm{b}}$  Parameters of the SNR distribution (eq. [6]):  $\eta = 1.69$ ,  $\xi = 3.33$ .

point, we conclude that  $4\mathrm{kpc} < z_h < 12\mathrm{kpc}$ . Again, the result is not very sensitive to modulation, since the predicted  $^{10}\mathrm{Be}/^9\mathrm{Be}$  is fairly constant from 100 to  $1000\mathrm{MeV}$  nucleon  $^{-1}$ .

Figure 10 illustrates the importance of energy losses on the  $^{10}\mathrm{Be} / ^{9}\mathrm{Be}$  ratio; for reacceleration cases with  $z_{h} = 1 - 20$  kpc, we show the ratio with and without losses. Losses attenuate the flux of stable nuclei much more than radioactive nuclei, and hence lead to an increase in  $^{10}\mathrm{Be} / ^{9}\mathrm{Be}$ . The effect can be simply illustrated as follows. The ionization loss rate on neutral gas is  $\sim 1.8 \times 10^{-7}Z^{2}\langle n_{\mathrm{H}}\rangle \beta^{-1} \mathrm{eV} \mathrm{s}^{-1}$ , where  $\beta = v / c$  is the nucleon speed and  $\langle n_{\mathrm{H}}\rangle$  is the average interstellar gas density. Thus, for Be nuclei of  $300 \mathrm{MeV}$

nucleon $^{-1}$  and for a gas disk with  $0.2\mathrm{kpc}$  thickness and density  $1\mathrm{cm}^{-3}$ ,  $\langle n_{\mathrm{H}}\rangle = 0.2 / z_{h}\mathrm{cm}^{-3}$ , which gives a loss time of  $\sim 3\times 10^{8}$  yr for  $z_{h} = 5$  kpc. Coulomb losses on the ionized gas in the halo increase the losses further (see Fig. 13); although the density is low, the wide  $z$ -extent means that the losses occur over large regions of the halo. For the same  $z_{h}$ , the diffusion time is  $\approx 4\times 10^{8}$  yr, so the stable  $^9\mathrm{Be}$  is significantly attenuated. For the radioactive  $^{10}\mathrm{Be}$  ( $\tau_{1/2} = 1.6\times 10^{6}$  yr), the energy losses are negligible. Hence, losses significantly increase  $^{10}\mathrm{Be}/^9\mathrm{Be}$ . As can be seen in Figure 10, the relative effect is largest for large halos and becomes a dominant effect only for  $z_{h} > 3$  kpc. Although we illustrate this for the reacceleration case, the same effect applies to

![](images/b08cc867c31850777f12e0c5bcf1b1b73e08c96e0f35675a4af53a92e16d8433.jpg)  
FIG. 7.—B/C ratio for diffusive reacceleration models with  $z_{h} = 5$  kpc,  $v_{\mathrm{A}} = 0$  (dotted line), 15 (dashed line), 20 (thin solid line), and 30 (thick solid line) km s $^{-1}$ . Parameters are given in Table 2. In each case, the interstellar ratio and the ratio modulated to 500 MV is shown. Data are as in Fig. 3.

![](images/9821d2fedf1eb76c00739396e53ce56cc90263b303323664131b876fa6f8c06b.jpg)  
FIG. 8.—B/C ratio for diffusive reacceleration models:  $z_{h} = 1$  (dotted line), 5 (dashed line), 10 (thin solid line), and 20 kpc (thick solid line). Parameters are given in Table 2. In each case, the interstellar ratio and the ratio modulated to  $500\mathrm{MV}$  is shown. Data are as in Fig. 3.

![](images/f2bab34bf73f62d17809956a0468f8cedcf8a95ee60e9c1e015309f5fec7a0c8.jpg)  
FIG. 9.  ${}^{10}\mathrm{Be}/{}^{9}\mathrm{Be}$  ratio for diffusive reacceleration models: (a) as function of energy for (from top to bottom)  $z_{h} = 1, 2, 3, 4, 5, 10, 15,$  and  $20\mathrm{kpc}$ , with data points as in Fig. 5; (b) as function of  $z_{h}$  at  $525\mathrm{MeV}$  nucleon  ${}^{-1}$ , corresponding to the mean interstellar value for the Ulysses data (Connell 1998); the Ulysses experimental limits are shown as horizontal dashed lines. Parameters are given in Table 2.

![](images/af710464e25a17d98c09b2d99ecf07a20b2ff042155fbd607ef57e333183ddac.jpg)

diffusion/convection models. Clearly, if losses are ignored, the predicted ratio will be too low and the derived value of  $z_{h}$  will be too small, since  $z_{h}$  will have to be reduced to fit the observations.

The proton, helium, and positron spectra were presented in Paper II for the case of  $z_{h} = 3$  kpc using the same model as used here, and the injection spectra were derived. The effect of varying the halo size is small for these spectra, so we do not extend that calculation to different  $z_{h}$ .

# 4. COSMIC-RAY GRADIENTS

An important constraint on any model of cosmic-ray propagation is provided by gamma-ray data that give information on the radial distribution of cosmic rays in the Galaxy. For a given source distribution, a large halo will give a smaller cosmic-ray gradient. It is generally believed that supernova remnants (SNRs) are the main sources of cosmic rays (see Webber 1997 for a recent review), but unfortunately the distribution of SNRs is poorly known because of selection effects. Nevertheless, it is interesting to compare quantitatively the effects of halo size on the gradient for a plausible SNR source distribution. For illustration, we use the SNR distribution from Case &

![](images/148ffd789cabd43936ba2959a368a414de90a8a5f95f655591d3444e5aad2561.jpg)  
FIG. 10. $^{10}\mathrm{Be} / ^{9}\mathrm{Be}$  ratio for diffusive reacceleration model, showing the influence of energy losses, for  $z_{h} = 1$  (dotted lines), 5 (solid line), and 20 kpc (dashed line). In each case, the upper curve is with energy losses, the lower curve without. Parameters are given in Table 2. Data points are as in Fig. 5.

Bhattacharya (1996), which is peaked at  $R = 4 - 5$  kpc and has a steep falloff toward larger  $R$ .

Figure 11 shows the effect of halo size on the resulting radial distribution of  $3\mathrm{GeV}$  cosmic-ray protons for the reacceleration model. For comparison, we show the cosmic-ray distribution deduced by model fitting to EGRET gamma-ray data  $(>100\mathrm{MeV})$  from Strong & Mattox (1996), which is dominated by the  $\pi^o$ -decay component generated by GeV nucleons; the analysis by Hunter et al. (1997), based on a different approach, gives a similar result. The cosmic-ray distribution predicted using the SNR source function is too steep even for large halo sizes; in fact,

![](images/84dddda3c226eee1f84a7332484fbc506f7af0d05c9474bd6b1f1e9ae073fc8d.jpg)  
FIG. 11.—Radial distribution of 3 GeV protons at  $z = 0$ , for diffusive reacceleration model with halo sizes  $z_{h} = 1, 3, 5, 10, 15$ , and  $20 \mathrm{kpc}$  (solid curves). The source distribution is that for SNRs given by Case & Bhattacharya (1996), shown as a dashed line. The cosmic-ray distribution deduced from EGRET  $> 100 \mathrm{MeV}$  gamma rays (Strong & Mattox 1996) is shown as a histogram. Parameters are as in Table 2.

the halo size has a relatively small effect on the distribution. Other related distributions, such as pulsars (Taylor, Manchester, & Lyne 1993; Johnston 1994), have an even steeper falloff. Only for  $z_{h} = 20$  kpc does the gradient approach that observed, and in this case the combination of a large halo and a slightly less steep SNR distribution could give a satisfactory fit. For diffusion/convection models the situation is similar, with more convection tending to make the gradient follow the sources more closely. A larger halo ( $z_{h} \gg 20$  kpc), apart from being excluded by the  $^{10}\mathrm{Be}$  analysis presented here, would in fact not improve the situation much, since Figure 11 shows that the gradient approaches an asymptotic shape that hardly changes beyond a certain halo size. This is a consequence of the nature of the diffusive process, which even for an unlimited propagation region still retains the signature of the source distribution.

Based on these results, we must conclude, in the context of the present models, that the distribution of sources is not as expected from the (highly uncertain; see Green 1991) distribution of SNRs. This conclusion is similar to what has been previously found by others (Webber et al. 1992; Bloemen et al. 1993). In view of the difficulty of deriving the SNR distribution, this is perhaps not a serious shortcoming; if SNRs are indeed cosmic-ray sources, then it is possible that the gamma-ray analysis gives the best estimate of their Galactic distribution. Therefore, in our standard model we have obtained the source distribution empirically by requiring consistency with the high-energy gamma-ray results.

Figure 12 shows the source distribution adopted in the present work and the resulting  $3\mathrm{GeV}$  proton distribution, again compared to that deduced from gamma rays. The gradients are now consistent, especially considering that

![](images/aeea1eb5b000dc30c806246799760cba122f83c1f2bcb57d674cb07d9a24f5f6.jpg)  
FIG. 12.—Radial distribution of 3 GeV protons at  $z = 0$ , for diffusive reacceleration model with various halo sizes,  $z_{h} = 1, 3, 5, 10, 15$ , and  $20\mathrm{kpc}$  (solid curves). The source distribution used is shown as a dashed line, and is that adopted to reproduce the cosmic-ray distribution deduced from EGRET  $>100\mathrm{MeV}$  gamma rays (Strong & Mattox 1996), shown as a histogram. Parameters are as in Table 2.

some systematic effects, arising for example from unresolved gamma-ray sources, are present in the gamma-ray results.

Measurements of cosmic-ray anisotropy in the 1-100 TeV range provide an independent argument for reacceleration (e.g., Seo & Ptuskin 1994), since the slower increase of the diffusion coefficient with energy avoids the large anisotropies predicted by non-reacceleration models. Our models reproduce this behavior, the reacceleration models giving anisotropies of  $\sim 10^{-3}$  at 1 TeV, while the nonreacceleration models give  $>10^{-2}$ . The observed values  $(\sim 10^{-3})$  largely reflect the local structure of the interstellar magnetic field in the part of the Galaxy near the Sun, and hence do not give useful constraints on the large-scale propagation that our model addresses (see Berezinskii et al. 1990). In particular, it is not possible to test the large-scale cosmic-ray gradients at such energies by this method. It is sufficient to note that the reacceleration models are consistent with the observations, while the non-reacceleration models are not, in accord with previous authors' conclusions.

# 5. CONCLUSIONS

We have shown that simple diffusion/convection models have difficulty accounting for the observed form of the B/C ratio without special assumptions chosen to fit the data, and do not obviate the need for an ad hoc form for the diffusion coefficient. On the other hand, we confirm the conclusion of other authors that models with reacceleration account naturally for the energy dependence over the whole observed range, with only two free parameters. Combining these results points rather strongly in favor of the reacceleration picture. In this case,  $v_{\mathrm{A}} \approx 20 \, \mathrm{km} \, \mathrm{s}^{-1}$ , with little dependence on  $z_{h}$ .

For the first time,  $^{10}\mathrm{Be} / ^{9}\mathrm{Be}$  has also been computed with reacceleration. We take advantage of the recent Ulysses Be measurements to improve limits on the halo size. We emphasize the crucial importance of the treatment of energy losses in the evaluation of the  $^{10}\mathrm{Be} / ^{9}\mathrm{Be}$  ratio. The halo height with reacceleration is  $4\mathrm{kpc} < z_{h} < 12\mathrm{kpc}$ . Our new limits should be an improvement on previous estimates, because of the more accurate Be data, our treatment of energy losses, and the inclusion of more realistic astrophysical details (such as, e.g., the gas distribution) in our model.

In case reacceleration is not important, the halo size limits are still  $4\mathrm{kpc} < z_h < 12\mathrm{kpc}$  for the case of no convection, while only the lower limit holds if convection is allowed. The upper limit on the convection velocity gradient is  $dV / dz < 7\mathrm{km~s^{-1}~kpc^{-1}}$ , this value being allowed for large  $z_h$  only.

The gradient of protons derived from gamma rays is smaller than expected for SNR sources, the closest approach to consistency being for  $z_{h} = 20$  kpc; we therefore adopt a flatter source distribution in order to meet the gamma-ray constraints.

The anisotropy at  $\sim 1$  TeV predicted by our reacceleration models is consistent with observations, while the nonreacceleration model predicts a larger value than observed. This reflects the general property of such models (e.g., Seo & Ptuskin 1994). The large-scale propagation is, however, not significantly constrained by anisotropy measurements at the energies considered in this paper, since local interstellar effects may dominate.

The large  $z_{h}$  values found here would have very significant implications for gamma rays at high Galactic latitudes, giving a larger inverse Compton intensity than normally considered. Gamma-rays will be addressed in detail in Paper IV.

We are grateful to the referee for useful suggestions. We thank J. J. Connell for help with the Ulysses Be data and for providing data prior to publication. We thank D. Breitschwerdt and V. Ptuskin for useful discussions.

# APPENDIX A

# PROPAGATION EQUATION

The propagation equation is written in the form

$$
\frac {\partial \psi}{\partial t} = q (\boldsymbol {r}, p) + \nabla \cdot \left(D _ {x x} \nabla \psi - V \psi\right) + \frac {\partial}{\partial p} p ^ {2} D _ {p p} \frac {\partial}{\partial p} \frac {1}{p ^ {2}} \psi - \frac {\partial}{\partial p} \left[ \dot {p} \psi - \frac {p}{3} (\nabla \cdot V) \psi \right] - \frac {1}{\tau_ {f}} \psi - \frac {1}{\tau_ {r}} \psi , \tag {A1}
$$

where  $\psi = \psi (r,p,t)$  is the density per unit of total particle momentum,  $\psi (p)dp = 4\pi p^2 f(p)$  in terms of phase-space density  $f(p)$ ,  $q(r,p)$  is the source term,  $D_{xx}$  is the spatial diffusion coefficient,  $V$  is the convection velocity, reacceleration is described as diffusion in momentum space and is determined by the coefficient  $D_{pp}$ ,  $\dot{p} \equiv dp / dt$  is the momentum loss rate,  $\tau_f$  is the timescale for fragmentation, and  $\tau_r$  is the timescale for the radioactive decay. The details of the numerical scheme are described in Appendix B.

We use particle momentum as the kinematic variable, since it greatly facilitates the inclusion of the diffusive reacceleration terms. The injection spectrum of primary nucleons is assumed to be a power law in momentum for the different species,  $dq(p) / dp \propto p^{-\Gamma}$  for the injected density, as expected for diffusive shock acceleration (e.g., Blandford & Ostriker 1980); the value of  $\Gamma$  can vary with species. The injection spectrum for  $^{12}\mathrm{C}$  and  $^{16}\mathrm{O}$  was taken as  $dq(p) / dp \propto p^{-2.35}$  for the case of no reacceleration, and  $p^{-2.25}$  with reacceleration. These values are consistent with Engelmann et al. (1990), who give an injection index of  $2.23 \pm 0.05$ . The same indexes reproduce the observed proton and  $^4\mathrm{He}$  spectra, as was shown in Paper II. For primary electrons, the injection spectrum is adjusted to reproduce direct measurements, gamma-ray, and synchrotron data; details are given in the other papers of this series (Papers I, II, and IV).

For secondary nucleons, the source term is  $q(r, \bar{p}) = \beta c \psi_p(r, p) [\sigma_{\mathrm{H}}^{ps}(p) n_{\mathrm{H}}(r) + \sigma_{\mathrm{He}}^{ps}(p) n_{\mathrm{He}}(r)]$ , where  $\sigma_{\mathrm{H}}^{ps}(p)$  and  $\sigma_{\mathrm{He}}^{ps}(p)$  are the production cross sections for the secondary from the progenitor on H and He targets,  $\psi_p$  is the progenitor density, and  $n_{\mathrm{H}}$  and  $n_{\mathrm{He}}$  are the interstellar hydrogen and helium number densities, respectively.

To compute  $\mathrm{B / C}$  and  $^{10}\mathrm{Be} / ^9\mathrm{Be}$ , it is sufficient for our purposes to treat only one principal progenitor and compute weighted cross sections based on the observed cosmic-ray abundances, which we took from Lukasiak et al. (1994b). Explicitly, for a principal primary with abundance  $I_{p}$ , we use for the production cross section  $\bar{\sigma}^{ps} = \sum_{i}\sigma^{is}I_{i} / I_{p}$ , where  $\sigma^{is}$  and  $I_{i}$  are the cross sections and abundances, respectively, of all species producing the given secondary. For the case of boron, the nitrogen progenitor is secondary but only accounts for  $\approx 10\%$  of the total boron production, so that the approximation of weighted cross sections is sufficient.

For the fragmentation cross sections we use the formula given by Letaw et al. (1983). For the secondary production cross sections we use the Webber, Kish, & Schrier (1990) and Silberberg & Tsao (1990; see also Garcia-Munoz et al. 1987) parameterizations in the form of code obtained from the Transport Collaboration (Guzik et al. 1997). Comparison of the results from these different versions of the cross sections gives a useful estimate of the uncertainty from this source. For the important  $\mathrm{B} / \mathrm{C}$  ratio, we take the  $^{12}\mathrm{C},^{16}\mathrm{O}\rightarrow{}^{10}\mathrm{B},^{10}\mathrm{C},^{11}\mathrm{B},$  and  $^{11}\mathrm{C}$  cross sections from the fit to experimental data given by Heinbach & Simon (1995). Since for Be the values of the cross sections are particularly important, we give for reference the values actually used for the abundance-weighted cross sections at  $500\mathrm{MeV}$  nucleon $^{-1}$ , including interstellar He:  $\bar{\sigma} (^{12}\mathrm{C}\to{}^9\mathrm{Be}) = 18.2\mathrm{mb},\bar{\sigma} (^{12}\mathrm{C}\to{}^{10}\mathrm{Be}) = 8.6\mathrm{mb}.$  For radioactive decay,  $\tau_{r} = \gamma \tau_{1 / 2} / \ln 2,$  where  $\tau_{1 / 2} = 1.6\times 10^{6}$  yr for  $^{10}\mathrm{Be}$

For electrons and positrons, the same propagation equation is valid when the appropriate energy loss terms (ionization, bremsstrahlung, inverse Compton, or synchrotron) are used. Since this paper is intended to complete the description of the full model, we include the formulae for these loss mechanisms in Appendix C.2. A detailed description of the source function for secondary electrons and positrons was given in Paper II.

# APPENDIX B

# NUMERICAL SOLUTION OF PROPAGATION EQUATION

The diffusion, reacceleration, convection, and loss terms given in equation (A1) can all be finite-differenced for each dimension  $(R, z, p)$  in the form

$$
\frac {\partial \psi_ {i}}{\partial t} = \frac {\psi_ {i} ^ {t + \Delta t} - \psi_ {i} ^ {t}}{\Delta t} = \frac {\alpha_ {1} \psi_ {i - 1} ^ {t + \Delta t} - \alpha_ {2} \psi_ {i} ^ {t + \Delta t} + \alpha_ {3} \psi_ {i + 1} ^ {t + \Delta t}}{\Delta t} + q _ {i}, \tag {B1}
$$

TABLE 3 COEFFICIENTS FOR THE CRANK-NICHOLSON METHOD  

<table><tr><td>Process</td><td>Coordinate</td><td>α1/Δt</td><td>α2/Δt</td><td>α3/Δt</td></tr><tr><td rowspan="2">Diffusion</td><td>R</td><td>Dxx2Ri-ΔR/2Ri(ΔR)2</td><td>Dxx2Ri/Ri(ΔR)2</td><td>Dxx2Ri+ΔR/2Ri(ΔR)2</td></tr><tr><td>z</td><td>Dxx/(Δz)2</td><td>2Dxx/(Δz)2</td><td>Dxx/(Δz)2</td></tr><tr><td rowspan="3">Convectiona</td><td>z&gt;0 (V&gt;0)</td><td>V(zi-1)/Δz</td><td>V(zi)/Δz</td><td>0</td></tr><tr><td>z&lt;0 (V&lt;0)</td><td>0</td><td>-V(zi)/Δz</td><td>-V(zi+1)/Δz</td></tr><tr><td>p(dV/dz&gt;0)</td><td>0</td><td>-1/3 pi dV/dz Pi-1</td><td>-1/3 pi+1 dV/dz Pi+1</td></tr><tr><td>Diffusive reaccelerationa</td><td>p</td><td>2Dpp,i-1Pi+1-1(Pi-1+1)/P1-1</td><td>2/Pi+1-1(Dpp,i+1/Pi+1+1)+Dpp,i-1/Pi-1)</td><td>2Dpp,i+1/Pi+1-1(Pi+1-1)/P1+1</td></tr><tr><td>Energy lossa</td><td>p</td><td>0</td><td>p̂i/Pi+1</td><td>p̂i+1/Pi+1</td></tr><tr><td>Fragmentation</td><td>R, z, p</td><td>0</td><td>1/3τf</td><td>0</td></tr><tr><td>Radioactive decay</td><td>R, z, p</td><td>0</td><td>1/3τr</td><td>0</td></tr></table>

a  $P_{j}^{i}\equiv p_{i} - p_{j}$

where all terms are functions of  $(R,z,p)$

In the Crank-Nicholson implicit method (Press et al. 1992), the updating scheme is

$$
\psi_ {i} ^ {t + \Delta t} = \psi_ {i} ^ {t} + \alpha_ {1} \psi_ {i - 1} ^ {t + \Delta t} - \alpha_ {2} \psi_ {i} ^ {t + \Delta t} + \alpha_ {3} \psi_ {i + 1} ^ {t + \Delta t} + q _ {i} \Delta t. \tag {B2}
$$

The tridiagonal system of equations,

$$
- \alpha_ {1} \psi_ {i - 1} ^ {t + \Delta t} + (1 + \alpha_ {2}) \psi_ {i} ^ {t + \Delta t} - \alpha_ {3} \psi_ {i + 1} ^ {t + \Delta t} = \psi_ {i} ^ {t} + q _ {i} \Delta t, \tag {B3}
$$

is solved for  $\psi_i^{t + \Delta t}$  by the standard method (Press et al. 1992). Note that for energy losses we use "upwind" differencing to enhance stability, which is possible since we have only loss terms (adiabatic energy gain is not included here).

The three spatial boundary conditions

$$
\psi (R, z _ {h}, p) = \psi (R, - z _ {h}, p) = \psi \left(R _ {h}, z, p\right) = 0 \tag {B4}
$$

are imposed at each iteration. No boundary conditions are imposed or required at  $R = 0$  or in  $p$ . Grid intervals are typically  $\Delta R = 1$  kpc,  $\Delta z = 0.1$  kpc; for  $p$ , a logarithmic scale with a typical ratio of 1.2 is used. Although the model is symmetric around  $z = 0$ , the solution is generated for  $-z_h < z < z_h$ , since this is required for the tridiagonal system to be valid.

Since we have a three-dimensional  $(R, z, p)$  problem, we use operator splitting to handle the implicit solution, as follows. We apply the implicit updating scheme alternately for the operator in each dimension in turn, keeping the other two coordinates fixed. To account for the substeps,  $q_i / 3$  and  $1 / 3\tau$  are used instead of  $q_i$ ,  $1 / \tau$ . The coefficients of the Crank-Nicholson scheme we use are given in Table 3.

The method was found to be stable for all  $\alpha$ , and this property can be exploited to advantage by starting with  $\alpha \gg 1$  (see below). The standard alternating direction implicit (ADI) method, in which the full operator is used to update each dimension implicitly in turn, is more accurate, but was found to be unstable for  $\alpha > 1$ . This is a disadvantage when treating problems with many timescales, but can be used to generate an accurate solution from an approximation generated by the non-ADI method.

A check for convergence is performed by computing the timescale  $\psi / (\partial \psi / \partial t)$  from equation (A1) and requiring that this be large compared to all diffusive and energy-loss timescales. The main problem in applying the method in practice is the wide range of timescales, especially for the electron case, ranging from  $10^{4}$  yr for energy losses to  $10^{9}$  yr for diffusion around 1 GeV in a large halo. Use of a time step  $\Delta t$  appropriate to the smallest timescales guarantees a reliable solution, but requires a prohibitively large number of steps to reach long timescales. The following technique was found to work well: start with a large  $\Delta t$ , appropriate for the longest scales, and iterate until a stable solution is obtained. This solution is then accurate only for cells with  $\alpha \ll 1$ ; for other cells, the solution is stable but inaccurate. Then reduce  $\Delta t$  by a factor (0.5 was adopted) and continue the solution. This process is repeated until  $\alpha \ll 1$  for all cells, when the solution is accurate everywhere. It is found that the inaccurate parts of the solution quickly decay as soon as the condition  $\alpha < 1$  is reached for a cell. As soon as all cells satisfy  $\alpha < 1$ , the solution is continued with the ADI method to obtain maximum accuracy. A typical run starts with  $\Delta t = 10^{9}$  yr and ends with  $\Delta t = 10^{4}$  yr for nucleons and  $10^{2}$  yr for electrons, performing  $\sim 60$  iterations per  $\Delta t$ . In this way it is possible to obtain reliable solutions with reasonable computer resources, although the CPU required is still considerable. All results are output as FITS data sets for subsequent analysis.

More details, including the software and data sets, can be found at the authors' web site.8

# B1. DIFFUSION IN  $R$

As an example, the coefficients for the radial diffusion term are derived here.

$$
\frac {1}{R} \frac {\partial}{\partial R} \left(R D _ {x x} \frac {\partial \psi}{\partial R}\right) = \frac {2}{R _ {i}} \frac {D _ {x x}}{R _ {i + 1} - R _ {i - 1}} \left(R _ {i + 1} \frac {\psi_ {i + 1} - \psi_ {i}}{R _ {i + 1} - R _ {i}} - R _ {i - 1} \frac {\psi_ {i} - \psi_ {i - 1}}{R _ {i} - R _ {i - 1}}\right). \tag {B5}
$$

Setting  $R_{i+1} - R_i = R_i - R_{i-1} = \Delta R$ , one can obtain the following expressions in terms of our standard form (eq. [B1]):

$$
\frac {\alpha_ {1}}{\Delta t} = D _ {x x} \frac {2 R _ {i} - \Delta R}{2 R _ {i} (\Delta R) ^ {2}}, \quad \frac {\alpha_ {2}}{\Delta t} = D _ {x x} \frac {2 R _ {i}}{R _ {i} (\Delta R) ^ {2}}, \quad \frac {\alpha_ {3}}{\Delta t} = D _ {x x} \frac {2 R _ {i} + \Delta R}{2 R _ {i} (\Delta R) ^ {2}}. \tag {B6}
$$

# B2. DIFFUSIVE REACCELERATION

In terms of three-dimensional momentum phase-space density  $f(p)$ , the diffusive reacceleration equation is

$$
\frac {\partial f (\boldsymbol {p})}{\partial t} = \boldsymbol {\nabla} _ {p} \cdot \left[ D _ {p p} \boldsymbol {\nabla} _ {p} f (\boldsymbol {p}) \right] = \frac {1}{p ^ {2}} \frac {\partial}{\partial p} \left[ p ^ {2} D _ {p p} \frac {\partial f (p)}{\partial p} \right]. \tag {B7}
$$

The distribution is assumed isotropic, so  $f(p) = f(p)$  where  $p = |p|$ . First we rewrite the equation in terms of  $\psi(p) = 4\pi p^2 f(p)$ , instead of  $f(p)$ , and expand the inner differential:

$$
\frac {\partial \psi}{\partial t} = \frac {\partial}{\partial p} \left(p ^ {2} D _ {p p} \frac {\partial}{\partial p} \frac {\psi}{p ^ {2}}\right) = \frac {\partial}{\partial p} D _ {p p} \left(\frac {\partial \psi}{\partial p} - \frac {2 \psi}{p}\right). \tag {B8}
$$

The differencing scheme is then

$$
\frac {2}{p _ {i + 1} - p _ {i - 1}} \left[ D _ {p p, i + 1} \left(\frac {\psi_ {i + 1} - \psi_ {i}}{p _ {i + 1} - p _ {i}} - \frac {2 \psi_ {i + 1}}{p _ {i + 1}}\right) - D _ {p p, i - 1} \left(\frac {\psi_ {i} - \psi_ {i - 1}}{p _ {i} - p _ {i - 1}} - \frac {2 \psi_ {i - 1}}{p _ {i - 1}}\right) \right]. \tag {B9}
$$

In terms of our standard form (eq. [B1]), the coefficients for reacceleration are then

$$
\begin{array}{l} \frac {\alpha_ {1}}{\Delta t} = \frac {2 D _ {p p , i - 1}}{p _ {i + 1} - p _ {i - 1}} \left(\frac {1}{p _ {i} - p _ {i - 1}} + \frac {2}{p _ {i - 1}}\right), \quad \frac {\alpha_ {2}}{\Delta t} = \frac {2}{p _ {i + 1} - p _ {i - 1}} \left(\frac {D _ {p p , i + 1}}{p _ {i + 1} - p _ {i}} + \frac {D _ {p p , i - 1}}{p _ {i} - p _ {i - 1}}\right), \\ \frac {\alpha_ {3}}{\Delta t} = \frac {2 D _ {p p , i + 1}}{p _ {i + 1} - p _ {i - 1}} \left(\frac {1}{p _ {i + 1} - p _ {i}} - \frac {2}{p _ {i + 1}}\right). \tag {B10} \\ \end{array}
$$

# APPENDIX C

# ENERGY LOSSES

For nucleon propagation in the ISM, the losses are mainly due to ionization, Coulomb scattering, fragmentation, and radioactive decay. For electrons, the important processes are ionization, Coulomb scattering, bremsstrahlung in the neutral and ionized medium, and Compton and synchrotron losses. Although all these processes are well known, the formulae for the different cases are scattered throughout the literature; hence, for completeness we summarize the formulae used below.

Figure 13 illustrates the energy-loss timescales,  $E(dE/dt)^{-1}$ , for electrons and nucleons in pure hydrogen. The losses are shown for equal neutral and ionized gas number densities,  $n_{\mathrm{H}} = n_{\mathrm{HII}} = 0.01 \, \mathrm{cm}^{-3}$ , and equal energy densities of photons and

![](images/967f23f445291342fcc1c2c5daf58c628f73c04bed01bb526d89ee2b878abd40.jpg)  
FIG. 13.—Energy-loss timescales of (a) nucleons and (b) electrons in neutral and ionized hydrogen. The curves are computed for gas densities  $n_{\mathrm{H}} = n_{\mathrm{HI}} = 0.01 \, \mathrm{cm}^{-3}$ , and equal energy densities of photons and magnetic field  $U = U_{B} = 1 \, \mathrm{eV} \, \mathrm{cm}^{-3}$  (in the Thomson limit). In panel (a), solid lines show ionization losses and dashed lines show Coulomb losses; dotted line is for protons.

![](images/36cc79e61bfc89d02977f71f0db68fe8dd71fbf7cdeac09efee918d9b2943b76.jpg)

the magnetic field,  $U = U_{B} = 1 \mathrm{eV} \mathrm{cm}^{-3}$  (in the Thomson limit). These gas and energy densities are chosen to characterize the average values seen by cosmic rays during propagation.

# C1. NUCLEON ENERGY LOSSES

The Coulomb collisions in a completely ionized plasma are dominated by scattering off the thermal electrons. The corresponding energy losses are given by (Mannheim & Schlickeiser 1994; see their eqs. [4.16] and [4.22])

$$
\left(\frac {d E}{d t}\right) _ {\text {C o u l}} \approx - 4 \pi r _ {e} ^ {2} c m _ {e} c ^ {2} Z ^ {2} n _ {e} \ln \Lambda \frac {\beta^ {2}}{x _ {m} ^ {3} + \beta^ {3}}, \tag {C1}
$$

where  $r_e$  is the classical electron radius,  $m_e$  is the electron rest mass,  $c$  is the velocity of light,  $Z$  is the projectile charge,  $\beta = v / c$  is the nucleon speed,  $n_e$  is the electron number density in plasma,  $x_m \equiv [3(\pi)^{1/2} / 4]^{1/3}(2kT_e / m_ec^2)^{1/2}$ , and  $T_e$  is the electron temperature. The Coulomb logarithm in the cold plasma limit is given by (e.g., Dermer 1985)

$$
\ln \Lambda \approx \frac {1}{2} \ln \left(\frac {m _ {e} ^ {2} c ^ {4}}{\pi r _ {e} \hbar^ {2} c ^ {2} n _ {e}} \frac {M \gamma^ {2} \beta^ {4}}{M + 2 \gamma m _ {e}}\right), \tag {C2}
$$

where  $h \equiv h / 2\pi$  is the Planck constant,  $M$  is the projectile mass, and  $\gamma$  is the Lorentz factor. For the appropriate number density  $n_e \sim 10^{-1} - 10^{-3} \, \mathrm{cm}^{-3}$  and total energy  $E \sim 10^3 - 10^4 \, \mathrm{MeV}$ , the typical value of the Coulomb logarithm  $\ln \Lambda$  lies within the interval  $\sim 40 - 50$ , instead of usually adopted value of 20.

For the ionization losses, we use a general formula (Mannheim & Schlickeiser 1994, their eq. [4.24]):

$$
\left(\frac {d E}{d t}\right) _ {I} (\beta \geq \beta_ {0}) = - 2 \pi r _ {e} ^ {2} c m _ {e} c ^ {2} Z ^ {2} \frac {1}{\beta} \sum_ {s = \mathrm {H}, \mathrm {H e}} n _ {s} \left[ B _ {s} + B ^ {\prime} \left(\alpha_ {f} Z / \beta\right) \right], \tag {C3}
$$

where  $\alpha_{f}$  is the fine-structure constant,  $n_{s}$  is the number density of the corresponding species in the ISM,  $\beta_0 = 1.4e^2 /\hbar c = 0.01$  is the characteristic velocity determined by the orbital velocity of the electrons in hydrogen, and

$$
B _ {s} = \left[ \ln \left(\frac {2 m _ {e} c ^ {2} \beta^ {2} \gamma^ {2} Q _ {\operatorname* {m a x}}}{\tilde {I} _ {s} ^ {2}}\right) - 2 \beta^ {2} - \frac {2 C _ {s}}{z _ {s}} - \delta_ {s} \right], \tag {C4}
$$

where  $\gamma$  is the Lorentz factor of the ion. The largest possible energy transfer from the incident particle to the atomic electron is defined by kinematics, $^9$

$$
Q _ {\max } \approx \frac {2 m _ {e} c ^ {2} \beta^ {2} \gamma^ {2}}{1 + (2 \gamma m _ {e} / M)}, \tag {C5}
$$

where  $M \gg m_{e}$  is the nucleon mass and  $\tilde{I}_{s}$  denotes the geometric mean of all ionization and excitation potentials of the atom. Mannheim & Schlickeiser (1994) give the values  $\tilde{I}_{\mathrm{H}} = 19 \, \mathrm{eV}$  and  $\tilde{I}_{\mathrm{He}} = 44 \, \mathrm{eV}$ . The shell correction term  $C_{s} / z_{s}$ , the density correction term  $\delta_{s}$ , and the  $B'$  correction term (for large  $Z$  or small  $\beta$ ) in equations (C3) and (C4) can be neglected for our purposes.

Fragmentation and radioactive decay are addressed in Appendix A.

# C2. ELECTRON ENERGY LOSSES

Ionization losses in the neutral hydrogen and helium are given by the Bethe-Bloch formula (Ginzburg 1979, p. 360),

$$
\left(\frac {d E}{d t}\right) _ {I} = - 2 \pi r _ {e} ^ {2} c m _ {e} c ^ {2} \frac {1}{\beta} \sum_ {s = \mathrm {H}, \mathrm {H e}} Z _ {s} n _ {s} \left\{\ln \left[ \frac {(\gamma - 1) \beta^ {2} E ^ {2}}{2 I _ {s} ^ {2}} \right] + \frac {1}{8} \right\}, \tag {C6}
$$

where  $Z_{s}$  is the nucleus charge,  $n_{s}$  is the gas number density,  $I_{s}$  is the ionization potential (we use  $I_{\mathrm{H}} = 13.6 \, \mathrm{eV}$ ,  $I_{\mathrm{He}} = 24.6 \, \mathrm{eV}$ , although the exact numbers are not very important),  $E$  is the total electron energy, and  $\gamma$  and  $\beta = v / c$  are the electron Lorentz factor and speed, respectively.

The Coulomb energy losses in the fully ionized medium in the cold plasma limit are described by (Ginzburg 1979, p. 361)

$$
\left(\frac {d E}{d t}\right) _ {\text {C o u l}} = - 2 \pi r _ {e} ^ {2} c m _ {e} c ^ {2} Z n \frac {1}{\beta} \left[ \ln \left(\frac {E m _ {e} c ^ {2}}{4 \pi r _ {e} \hbar^ {2} c ^ {2} n Z}\right) - \frac {3}{4} \right], \tag {C7}
$$

where  $Zn \equiv n_{e}$  is the electron number density. For an accurate treatment of the electron energy losses in the plasma of an arbitrary temperature, see, e.g., Dermer & Liang (1989) and Moskalenko & Jourdain (1997).

The energy losses due to  $ep$ -bremsstrahlung in the cold plasma are given by the expression (von Stickforth 1961)

$$
\left(\frac {d E}{d t}\right) _ {e p} = - \frac {2}{3} \alpha_ {f} r _ {e} ^ {2} c m _ {e} c ^ {2} Z ^ {2} n \left\{ \begin{array}{l l} 8 \gamma \beta [ 1 - 0. 2 5 (\gamma - 1) + 0. 4 4 9 3 5 (\gamma - 1) ^ {2} - 0. 1 6 5 7 7 (\gamma - 1) ^ {3} ], & \quad \gamma \leq 2 \\ \beta^ {- 1} [ 6 \gamma \ln (2 \gamma) - 2 \gamma - 0. 2 9 0 0 ], & \quad \gamma \geq 2. \end{array} \right. \tag {C8}
$$

For the  $ee$ -bremssstrahlung, one can obtain (Haug 1975; Moskalenko & Jourdain 1997)

$$
\left(\frac {d E}{d t}\right) _ {e e} = - \frac {1}{2} \alpha_ {f} r _ {e} ^ {2} c m _ {e} c ^ {2} Z n \beta \gamma^ {*} Q _ {\mathrm {c m}} (\gamma^ {*}), \tag {C9}
$$

where

$$
Q _ {\mathrm {c m}} (\gamma^ {*}) = 8 \frac {p ^ {* 2}}{\gamma^ {*}} \left[ 1 - \frac {4 p ^ {*}}{3 \gamma^ {*}} + \frac {2}{3} \left(2 + \frac {p ^ {* 2}}{\gamma^ {* 2}}\right) \ln (p ^ {*} + \gamma^ {*}) \right], \quad \gamma^ {*} = \sqrt {(\gamma + 1) / 2}, \quad p ^ {*} = \sqrt {(\gamma - 1) / 2},
$$

and the asterisk denotes center-of-mass variables. The total bremsstrahlung losses in the ionized gas is the sum  $(dE / dt)_{BI} = (dE / dt)_{ep} + (dE / dt)_{ee}$ . A good approximation gives the expression (Ginzburg 1979, p. 408)

$$
\left(\frac {d E}{d t}\right) _ {B I} = - 4 \alpha_ {f} r _ {e} ^ {2} c m _ {e} c ^ {2} Z (Z + 1) n E \left[ \ln (2 \gamma) - \frac {1}{3} \right]. \tag {C10}
$$

Bremsstrahlung energy losses in neutral gas can be obtained by integration over the bremsstrahlung luminosity (Koch & Motz 1959; see also Paper IV)

$$
\left(\frac {d E}{d t}\right) _ {B 0} = - c \beta \sum_ {s = H, H e} n _ {s} \int d k k \frac {d \sigma_ {s}}{d k}. \tag {C11}
$$

A suitable approximation (maximum  $10\%$  error near  $E \sim 70 \mathrm{MeV}$ ) for equation (C11) gives the combination (cf. eq. [C10])

$$
\left(\frac {d E}{d t}\right) _ {B 0} = \left\{ \begin{array}{l l} - 4 \alpha_ {f} r _ {e} ^ {2} c m _ {e} c ^ {2} E \left[ \ln (2 \gamma) - \frac {1}{3} \right] \sum_ {s = H, H e} n _ {s} Z _ {s} \left(Z _ {s} + 1\right), & \gamma \lesssim 1 0 0 \\ - c E \sum_ {s = H, H e} \frac {n _ {s} M _ {s}}{T _ {s}}, & \gamma \gtrsim 8 0 0, \end{array} \right. \tag {12}
$$

(see Ginzburg 1979, pp. 386, 409), with a linear connection in between. Here  $M_{s}$  is the atomic mass and  $T_{s}$  is the radiation length  $(T_{\mathrm{H}}\simeq 62.8\mathrm{gcm}^{-2},T_{\mathrm{He}}\simeq 93.1\mathrm{gcm}^{-2})$

The Compton energy losses are calculated using the Klein-Nishina cross section (Jones 1965; Moskalenko & Jourdain 1997),

$$
\frac {d E}{d t} = \frac {\pi r _ {e} ^ {2} m _ {e} c ^ {3}}{2 \gamma^ {2} \beta} \int_ {0} ^ {\infty} d \omega f _ {\gamma} (\omega) [ S (\gamma , \omega , k ^ {+}) - S (\gamma , \omega , k ^ {-}) ], \tag {C13}
$$

where the background photon distribution,  $f_{\gamma}(\omega)$ , is normalized on the photon number density as  $n_{\gamma} = \int d\omega \omega^{2}f_{\gamma}(\omega)$ ,  $\omega$  is the energy of the background photon taken in the electron rest-mass units,  $k^{\pm} = \omega \gamma (1\pm \beta)$

$$
\begin{array}{l} S (\gamma , \omega , k) = \omega \left\{\left(k + \frac {3 1}{6} + \frac {5}{k} + \frac {3}{2 k ^ {2}}\right) \ln (2 k + 1) - \frac {1 1}{6} k - \frac {3}{k} + \frac {1}{1 2 (2 k + 1)} + \frac {1}{1 2 (2 k + 1) ^ {2}} + L i _ {2} (- 2 k) \right\} \\ - \gamma \left\{\left(k + 6 + \frac {3}{k}\right) \ln (2 k + 1) - \frac {1 1}{6} k + \frac {1}{4 (2 k + 1)} - \frac {1}{1 2 (2 k + 1) ^ {2}} + 2 L i _ {2} (- 2 k) \right\}, \tag {C14} \\ \end{array}
$$

and  $Li_{2}$  is the dilogarithm

$$
\begin{array}{l} L i _ {2} (- 2 k) = - \int_ {0} ^ {- 2 k} d x \frac {1}{x} \ln (1 - x) \\ = \left\{ \begin{array}{l l} \sum_ {i = 1} ^ {\infty} (- 2 k) ^ {i} / i ^ {2}, & k \leq 0. 2, \\ - 1. 6 4 4 9 3 4 1 + \frac {1}{2} \ln^ {2} (2 k + 1) - \ln (2 k + 1) \ln (2 k) + \sum_ {i = 1} ^ {\infty} i ^ {- 2} (2 k + 1) ^ {- i}, & k \geq 0. 2. \end{array} \right. \tag {C16} \\ \end{array}
$$

The synchrotron energy losses are given by

$$
\left(\frac {d E}{d t}\right) _ {S} = - \frac {3 2}{9} \pi r _ {e} ^ {2} c U _ {B} \gamma^ {2} \beta^ {2}, \tag {C17}
$$

where  $U_{B} = \mathbf{H}^{2} / 8\pi$  is the energy density of the magnetic field.

# REFERENCES

Barwick, S. W., et al. 1997, ApJ, 482, L191

1998,ApJ,498,779

Berezinskii, V. S., et al. 1990, Astrophysics of Cosmic Rays (Amsterdam: North Holland)

Blandford, R. D., & Ostriker, J. P. 1980, ApJ, 237, 793

Bloemen, H., Dogiel, V. A., Dorman, V. I., & Ptuskin, V. S. 1993, A&A, 267, 372

Bronfman, L., et al. 1988, ApJ, 324, 248

Case,G.,&Bhattacharya,D.1996,A&AS,120C,437

Connell, J. J. 1998, ApJ, 501, L59

Cordes, J. M., et al. 1991, Nature, 354, 121

Cox,P.,Krugel,E.,&Mezger,P.G.1986,A&A,155,380

Dermer, C. D. 1985, ApJ, 295, 28

Dermer, C. D., & Liang, E. P. 1989, ApJ, 339, 512

DuVernois, M. A., Simpson, J. A., & Thayer, M. R. 1996, A&A, 316, 555 -1990,A&A,233,96  
Freedman, I., Kearsey, S., Osborne, J. L., & Giler, M. 1980, A&A, 82, 110  
Garcia-Munoz, M., et al. 1987, ApJS, 64, 269  
Ginzburg, V. L. 1979, Theoretical Physics and Astrophysics (Oxford: Pergamon)  
Ginzburg, V. L., Khazan, Ya. M., & Ptuskin, V. S. 1980, Ap&SS, 68, 295  
Gleeson, L. J., & Oxford, W. I. 1968, ApJ, 154, 1011  
Gordon, M. A., & Burton, W. B. 1976, ApJ, 208, 346  
Green, D. A. 1991, PASP, 103, 209  
Grevesse, N., Noels, A., & Sauval A. J. 1996, in ASP Conf. Ser. 99, Cosmic Abundances, ed. S. S. Holt & G. Sonneborn (San Francisco: ASP), 117  
Guzik, T. G., et al. 1997, Proc. 25th Int. Cosmic-Ray Conf. (Durban), 4, 317  
Haug,E.1975,Z.Naturforsch.,30a,1546  
Heinbach, U., & Simon, M. 1995, ApJ, 441, 209  
Hernandez, F. P., & Christensen-Dalsgaard, J. 1994, MNRAS, 269, 475  
Hunter, S. D., et al. 1997, ApJ, 481, 205  
Johnston,S.1994,MNRAS,268,595  
Jokipii, J. R. 1976, ApJ, 208, 900  
Jones, F. C. 1965, Phys. Rev., 137, B1306. 1979, ApJ, 229, 747  
Koch,H.W.,&Motz,J.W.1959,Rev.Mod.Phys.,31,920  
Lerche,I.,& Schlickeiser,R.1982,A&A,107,148  
Letaw, J. R., Silberberg, R., & Tsao, C. H. 1983, ApJS, 51, 271. 1993, ApJ, 414, 601  
Lukasiak, A., Ferrando, P., McDonald F. B., & Webber, W. R. 1994a, ApJ, 423, 426  
1994b, ApJ, 426, 366  
Mannheim, K., & Schlickeiser, R. 1994, A&A, 286, 983  
Meyer, J.-P., Drury, L. O'C., & Ellison, D. C. 1997, ApJ, 487, 182  
Moskalenko,I.V.,&Jourdain,E.1997,A&A,325,401  
Moskalenko, I. V., & Strong, A. W. 1998a, ApJ, 493, 694 (Paper II)

Moskalenko, I. V., & Strong, A. W. 1998b, in preparation (Paper IV)  
Owens,A.J.,&Jokipii,J.R.1977a,ApJ,215,677 1977b,ApJ,215,685  
Phillipps,S.,et al.1981,A&A,103,405  
Porter, T. A., & Protheroe, R. J. 1997, J. Phys. G. (Nucl. Part. Phys.), 23, 1765  
Press, W. H., et al. 1992, Numerical Recipes in FORTRAN (2d Ed.; Cambridge: Cambridge Univ. Press)  
Ptuskin, V. S., Volk, H. J., Zirakashvili, V. N., & Breitschwerdt, D. 1997, A&A, 321, 434  
Reynolds, R. J. 1989, ApJ, 339, L29  
Seo,E.S.,&Ptuskin,V.S.1994,ApJ,431,705  
Silberberg,R.,& Tsao,C.H.1990,Phys.Rep.,191,351  
Simon,M.,&Heinbach,U.1996,ApJ,456,519  
Simpson, J. A., & Garcia-Munoz, M. 1988, Space Sci. Rev., 46, 205  
Strong,A.W.1996,SpaceSci.Rev.,76,205  
Strong, A. W., & Mattox, J. R. 1996, A&A, 308, L21  
Strong, A. W., & Moskalenko, I. V. 1997, in AIP Conf. Proc. 410, Fourth Compton Symposium, ed. C. D. Dermer, M. S. Strickman, & J. D. Kurfess (New York: AIP), 1162 (Paper I)  
Strong, A. W., & Youssefi, G. 1995, Proc. 24th Int. Cosmic-Ray Conf. (Roma), 3, 48  
Taylor, J.H., Manchester, R.N., & Lyne, A.G. 1993, ApJS, 88, 529  
Webber, W. R. 1997, Space Sci. Rev., 81, 107  
Webber, W. R., Kish, J. C., & Schrier, D. A. 1990, Phys. Rev. C, 41, 566  
Webber, W. R., Lee, M. A., & Gupta, M. 1992, ApJ, 390, 96  
Webber, W. R., Lukasiak, A., McDonald, F. B., & Ferrando, P. 1996, ApJ, 457, 435  
von Stickforth, J. 1961, Z. Phys., 164, 1  
Zirakashvili, V. N., Breitschwerdt, D., Ptuskin, V. S., & Volk, H. J. 1996, A&A, 311, 113

Note added in proof.—Since the acceptance of this paper, two other recent papers addressing radioactive cosmic-ray nuclei have come to our attention: W. R. Webber & A. Soutoul, ApJ, 506, 335 (1998) and V. S. Ptuskin & A. Soutoul, A&A, 337, 859 (1998). The values obtained for the halo size in these papers (2–4 kpc,  $4.9_{-2}^{+4}$  kpc, respectively, are consistent with the present work.

An extension of our model to the cosmic-ray antiproton spectrum in connection with diffuse gamma rays and the nucleon spectrum can be found in I. V. Moskalenko, A. W. Strong, & O. Reimer, A&A, 338, L75 (1998).