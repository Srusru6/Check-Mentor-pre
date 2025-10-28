# The benefits of diligence: how precise are predicted gravitational wave spectra in models with phase transitions?

Huai-Ke Guo, $^{a}$  Kuver Sinha, $^{a}$  Daniel Vagie $^{a}$  and Graham White $^{b}$

$^a$ Department of Physics and Astronomy, University of Oklahoma,

Norman, OK 73019, U.S.A.

bKavli IPMU (WPI), UTIAS, The University of Tokyo,

Kashiwa, Chiba 277-8583, Japan

E-mail: ghk@ou.edu, kuver.sinha@ou.edu, Daniel.d.vogie-1@ou.edu,

graham.white@ipmu.jp

ABSTRACT: Models of particle physics that feature phase transitions typically provide predictions for stochastic gravitational wave signals at future detectors and such predictions are used to delineate portions of the model parameter space that can be constrained. The question is: how precise are such predictions? Uncertainties enter in the calculation of the macroscopic thermal parameters and the dynamics of the phase transition itself. We calculate such uncertainties with increasing levels of sophistication in treating the phase transition dynamics. Currently, the highest level of diligence corresponds to careful treatments of the source lifetime; mean bubble separation; going beyond the bag model approximation in solving the hydrodynamics equations and explicitly calculating the fraction of energy in the fluid from these equations rather than using a fit; and including fits for the energy lost to vorticity modes and reheating effects. The lowest level of diligence incorporates none of these effects. We compute the percolation and nucleation temperatures, the mean bubble separation, the fluid velocity, and ultimately the gravitational wave spectrum corresponding to the level of highest diligence for three explicit examples: SMEFT, a dark sector Higgs model, and the real singlet-extended Standard Model (xSM). In each model, we contrast different levels of diligence in the calculation and find that the difference in the final predicted signal can be several orders of magnitude. Our results indicate that calculating the gravitational wave spectrum for particle physics models and deducing precise constraints on the parameter space of such models continues to remain very much a work in progress and warrants care.

KEYWORDS: Phenomenological Models

ARXIV EPRINT: 2103.06933

# Contents

# 1 Introduction 1

# 2 Phase transition dynamics 4

2.1 Lowest diligence 5  
2.2 Moderate diligence 6  
2.3 High diligence 7

2.3.1 Calculation of the percolation temperature 8  
2.3.2 Calculation of the nucleation temperature 9  
2.3.3 Calculation of the mean bubble separation 10  
2.3.4 Going beyond the bag model 11  
2.3.5 Gravitational wave spectrum 14

# 3 Test models 16

3.1 SMEFT 16  
3.2 Dark renormalizable models 17  
3.3 xSM 19

# 4 Results 20

4.1 SMEFT 21  
4.2 Dark renormalizable models 24  
4.3 xSM 26  
4.4 Mean bubble separation vs inverse time duration 28

# 5 Summary of results 30

# 6 Conclusion 32

# A Kinetic energy efficiency coefficient 33

# B Toy model 34

B.1 Toy effective potential 34  
B.2 Results for toy model 35

# 1 Introduction

Even the very early Universe is transparent to gravitational waves, making searches for the gravitational wave background of the Universe a unique probe of the cosmos before big bang nucleosynthesis. Ubiquitous in the literature is the generation of a gravitational wave background from an inhomogeneous transition of the ground state (for a review see [1-3]).

In the standard model of particle physics, there is no mechanism for such a gravitational wave background to be produced. Specifically, both the QCD and electroweak transitions are predicted to be smooth [4-9]. This implies that any gravitational wave background resulting from a strong first order phase transition is proof that the standard model is incomplete.

The electroweak transition can be made strongly first order through the introduction of new states at around the electroweak scale [10-43]. The QCD transition can be catalyzed by changing the number of light fermions [44] or having a very large lepton asymmetry [45-47]. Additionally there are strong motivations to believe that the standard model is incomplete and additions to the standard model can also leave cosmic fingerprints. For instance, baryonic matter can only explain a fraction of the matter observed and the missing dark matter can be a part of a hidden sector that undergoes a phase transition [48-65]. Second, the near unification of gauge coupling constants along with conspiracy of gauge anomaly cancellation motivates grand unification which can sequentially break into the standard model gauge group and leave a gravitational wave background [66-72]. Finally, the generation of neutrino masses can arise through a  $B - L$  breaking transition [68, 73-77]. In each case, an observed signal not only sheds light on our cosmic history, but on a range of energy scales spanning from sub-GeV to the PeV scale [78] (even higher scales have been proposed, though technology needs to improve to make the sensitivity cosmologically relevant [79] with the possible exception of NEMO [80]).

Any strong first order transition produces three contributions to a stochastic background (see, e.g., [1-3]).

For a transition in the thermal plasma, only a negligibly small fraction of the energy released will remain in the scalar field when the bubble wall reaches a constant velocity [81], or when it "runs away" [82]. So the bubble collision contribution is negligible when considering transitions in a thermal plasma, though it can become dominant for transitions in vacuum, e.g., those in a dark sector without a thermal bath. In addition, the contribution from magnetohydrodynamic turbulence is subdominant compared with that from sound waves [81, 83, 84], with an efficiency factor that is roughly  $(5\sim 10)\%$  of that for sound waves [85], though its spectrum is highly uncertain as of now [86-92]. Since most transitions in the early universe are highly likely to be proceeding in the thermal plasma, we will focus here on the gravitational wave production from sound waves.

This acoustic contribution has been studied both in simulations and a combination of analytic and numerical techniques and there has been much recent progress.

Given the enormous opportunity to shed light on both cosmology and particle physics, it is worth examining in detail the theoretical underpinnings of any given model in order to enumerate both theoretical uncertainties in basic methods and the degree of benefit in more accurate calculations or, equivalently the cost of various approximations. Approximations can arise in two steps in predicting an observable from a given model as shown in figure 1. First the calculation of macroscopic thermal parameters, including the latent heat and the time scale of the transition, are often calculated using perturbative techniques which can introduce large errors [93] in particular when long wavelength modes are not resummed

![](images/cab119e59cad165a776dc671c9d8cd21f6bf440d37851cd23f7ec11082ba46eb.jpg)  
Figure 1. The uncertainty in linking a particular model with a set of observables is conceptually presented above. The break down of perturbation theory at finite temperature is the dominant error in the prediction of the evolution of the effective potential and ultimately non-perturbative methods might be required to predict macroscopic thermal parameters. The macroscopic thermal parameters of interest are often taken to be the latent heat, the time scale of the transition (usually approximated), the bubble wall velocity and the temperature of percolation, but if one desires to have an accurate prediction one needs the fluid velocity, the wall velocity, the mean bubble separation, the percolation temperature and the lifetime of the acoustic source (see also figure 1 of [96]).

carefully enough [94-97]. The second step, which we focus on in this paper, converts macroscopic thermal parameters into a prediction for the spectrum — in particular the peak frequency and amplitude. Ultimately, both steps will likely require simulations to truly perform precision cosmology on a future hypothetical observation. However, this is impractical for the analysis of large numbers of parameter sets for large numbers of models. We therefore examine several layers of improvement in the prediction of the peak amplitude that have recently arisen in several models involving physics beyond the standard model

- The finite lifetime of the source first estimated in ref. [102] and derived in the sound shell model in an expanding background in ref. [103].  
- Going beyond the bag model approximation in solving the hydrodynamic equations [104, 105].  
- Calculating the mean bubble separation from the evolution of the bubble number density.  
- Calculating the fraction of energy in the fluid from solving the hydrodynamic equations rather than using a fit [106].  
- Including fits for the energy lost to vorticity modes [106].

In this paper we will enumerate the error in a number of models in order to get a broad understanding of the numerical importance of diligence. This avoids model-specific effects where accidental cancellations between different improvements could in principle occur. The models we consider include a toy model introduced for pedagogical purposes, the Standard Model Effective Field Theory (SMEFT), a dark sector Higgs and a real scalar singlet extension (xSM) of the Standard Model. For the benefit of the reader, a

![](images/619bb2420eec432020f27d95646c7c55225d88890ba64c086553440d2ad1eb58.jpg)  
Figure 2. The relative error when using the lowest and modest levels of diligence, compared to the highest level of diligence (for which  $\Delta \Omega / \Omega = 0$ ). The vertical axis shows the peak (frequency-independent) gravitational wave energy density for detonation. The precise definition of  $\Delta \Omega / \Omega$  is given in eq. (4.1). The horizontal axis corresponds to the final temperature  $T_{f}$  when the phase transition ends. Three models are shown: SMEFT, a dark sector Higgs model (Dark RG) and the singlet-extended Standard Model (xSM). The figures employ calculations from eq. [(2.7), (2.15), (2.61)] and eq. (4.1). The temperatures are set to  $T_{n}$  (2.4),  $T_{p}$  (2.11), and  $T_{f}$  (2.27) for the lowest, modest, and highest diligence respectively. Both the modest and highest diligence contain suppression factors due to the lifetime of the source. The highest diligence contains the suppression factor due to vorticity effects in the plasma.

demonstration of the importance of diligence is provided at the outset in figure 2. Here, the relative error in the predicted peak amplitude is shown for SMEFT, the dark sector Higgs model (which we label throughout as "Dark RG") and xSM. Our paper will be devoted to fully explaining figure 2; for now, we provide a feel for the comparative importance of these errors. For the Dark RG, for example, the relative error is far more manageable than what it is for SMEFT. However, even for that model, the relative error is larger<sup>3</sup> than the error from gauge dependence that is introduced in SMEFT in some commonly used methods. Thus, even this case, which may present an unrealistically optimistic picture, still motivates diligence in the calculation.

The structure of this paper is as follows. In section 2 we outline three methods of various levels of diligence that we find used in the literature, including a level of diligence motivated by its use in the recent review [3]. In section 3 we define the models we will use to demonstrate increasing levels of diligence, and in section 4 we will present our results. We will end with our Conclusion.

# 2 Phase transition dynamics

Gravitational waves produced from first order phase transitions is a finite temperature tunneling process, from some false vacuum to the true vacuum. When calculating this

transition with perturbation theory, one needs to track the minima of the effective potential from the temperature at which the energy in each vacuum is degenerate — that is the critical temperature. Below the critical temperature, bubbles of the true phase begin to form at some critical radius where the pressure is strong enough to cause expansion. The probability of such bubbles forming increases as the Universe cools, until the nucleation temperature at which there is an average of one bubble per Hubble volume. Slightly below this temperature is the percolation temperature at which bubble collisions are occurring and the final temperature when the phase transition ends. There are simple analytical expressions for these temperature scales which are the result of approximations used in the equations. However, the gravitational wave spectrum is sensitive to the level of diligence that goes into the computations and reducing the error is paramount to probing phase transitions at future gravitational wave detectors. We will now proceed to analyze the different level of diligence used in the literature.

# 2.1 Lowest diligence

Here we will describe the level of lowest diligence in computing the gravitational wave spectrum. At this stage, we will only introduce the various parameter definitions and wait until the highest diligence section for a more in depth look at the numerical procedure. This level will involve computing all relevant parameters at the nucleation temperature.

The tunneling rate per unit time per unit volume will have the general form

$$
p (T) = \bar {p} _ {0} T ^ {4} e ^ {- S _ {3} / T}, \tag {2.1}
$$

where  $\bar{p}_0$  is a dimensionless number that we will assume is  $\mathcal{O}(1)$  and  $S_{3}$  can be found by solving the bounce solutions that minimize the action given by

$$
S _ {3} (\vec {\phi}, T) = 4 \pi \int d r r ^ {2} \left[ \frac {1}{2} \left(\frac {d \vec {\phi} (t)}{d r}\right) ^ {2} + V _ {\text {e f f}} (\vec {\phi}, T) \right]. \tag {2.2}
$$

The nucleation temperature is defined as the temperature at which the probability of a single bubble being nucleated within a Hubble volume is  $\mathcal{O}(1)$ :

$$
\int_ {0} ^ {t _ {n}} p V _ {H} (t) d t = \int_ {T _ {n}} ^ {\infty} \frac {d T}{T} \left(\frac {2 \xi M _ {\mathrm {p l}}}{T}\right) ^ {4} \exp^ {- S _ {3} / T} \sim \mathcal {O} (1), \tag {2.3}
$$

where  $M_{pl}$  is the Planck mass,  $\xi \sim 3\times 10^{-2}$ , and  $V_{H}(t)$  is the horizon volume. This equation will lead to the simple definition of the nucleation temperature [3, 107-109]

$$
\frac {S _ {3} \left(T _ {n}\right)}{T _ {n}} \approx 1 4 0. \tag {2.4}
$$

It is important to note that the above calculation assumes that the phase transition occurs in a radiation dominated era which is not guaranteed.

The strength of the gravitational wave spectrum will depend on hydrodynamic parameters such as the amount of vacuum energy released during the phase transitions, the inverse time duration of the phase transition, and the fraction of latent heat that goes into

the bulk motion of the plasma (referred to as the kinetic efficiency coefficient). We discuss each of these quantities in turn.

The strength of the phase transition is characterized as

$$
\alpha (T _ {n}) = \frac {1}{\rho_ {\mathrm {r a d}}} \left(\Delta V _ {\mathrm {e f f}} - \frac {1}{4} \frac {d \Delta V _ {\mathrm {e f f}}}{d T}\right) \Bigg | _ {T _ {n}}, \tag {2.5}
$$

where  $V_{\mathrm{eff}}$  is the finite temperature effective potential and the symbol  $\Delta$  signifies the difference in the symmetric phase (false vacuum) and the broken phase (true vacuum). The energy density of radiation is given by  $\rho_{\mathrm{rad}} = \pi^2 / 30 g_* T_n^4$  where  $g_*$  is the number of effective degrees of freedom at  $T_n$ .

The inverse time duration of the phase transition evaluated at the nucleation temperature can be approximated as

$$
\beta = H _ {n} T _ {n} \frac {d \left(S _ {3} / T\right)}{d T}, \tag {2.6}
$$

where  $H_{n}^{2} = 8\pi G\rho_{\mathrm{rad}}(T_{n}) / 3$  is the Hubble parameter at the nucleation temperature. A smaller  $\beta /H$  and larger  $\alpha$  will result in stronger gravitational waves.

The gravitational wave spectrum observed today has a simple broken power law fit [81] in terms of the aforementioned parameters given by

$$
h ^ {2} \Omega_ {\mathrm {G W}} (f) = 8. 5 \times 1 0 ^ {- 6} \left(\frac {1 0 0}{g _ {n}}\right) ^ {1 / 3} \left(\frac {\kappa \alpha}{1 + \alpha}\right) ^ {2} \left(\frac {H _ {n}}{\beta}\right) v _ {w} S _ {\mathrm {S W}} (f), \tag {2.7}
$$

where  $g_{n}$  is the number of degrees of freedom at the nucleation temperature and  $\kappa$  is the efficiency coefficient that represents the fraction of the bulk kinetic energy in the plasma relative to the available vacuum energy. The numerical fits for the kinetic efficiency coefficient,  $\kappa$ , were derived in [110] for the different velocity profile types which we give in appendix A. The spectral shape,  $S_{\mathrm{SW}}$ , and the peak frequency,  $f_{\mathrm{SW}}$  are given by

$$
S _ {\mathrm {S W}} (f) = \left(\frac {f}{f _ {\mathrm {S W}}}\right) ^ {3} \left[ \frac {7}{4 + 3 (f / f _ {\mathrm {S W}}) ^ {2}} \right] ^ {7 / 2}, \tag {2.8}
$$

$$
f _ {\mathrm {S W}} = 1. 9 \times 1 0 ^ {- 5} \frac {1}{v _ {w}} \left(\frac {\beta}{H _ {n}}\right) \left(\frac {T _ {n}}{1 0 0 \mathrm {G e V}}\right) \left(\frac {g _ {n}}{1 0 0}\right) ^ {1 / 6} \mathrm {H z}. \tag {2.9}
$$

The gravitational wave spectrum may be rewritten in terms of the R.M.S velocity,  $U_{f}^{2} = \frac{3}{4}\kappa \alpha$ , with the replacement

$$
\left(\frac {\kappa \alpha}{1 + \alpha}\right)\rightarrow \Gamma U _ {f} ^ {2}, \tag {2.10}
$$

where  $\Gamma \sim 3/4$  is the adiabatic index which is defined as the ratio of the enthalpy and energy density in the symmetric phase. The term in the denominator on the left hand side,  $(1 + \alpha)$ , is the result of the energy density in the symmetric phase.

# 2.2 Moderate diligence

The level of modest diligence is the approach most frequently used in the recent literature (including the recent LISA review [3]). It closely resembles the lowest diligence with the exception that the thermal parameters are defined at the percolation temperature rather

than the nucleation temperature and the finite lifetime of the source is taken into account with an ansatz correction to the peak amplitude. The percolation temperature is here approximated by solving the equation

$$
\frac {S _ {3} (T _ {p})}{T _ {p}} = 1 3 1 - \log (A / T ^ {4}) - 4 \log \left(\frac {T}{1 0 0 \mathrm {G e V}}\right) - 4 \log \left(\frac {\beta (T) / H}{1 0 0}\right) + 3 \log (v _ {w}), \quad (2. 1 1)
$$

where  $\log (A / T^4)\sim 14$  for an electroweak phase transition. Note that the derivative of the left hand side in eq. (2.11) appears on the right hand side, as can be seen from eq. (2.6). The percolation temperature is always below the nucleation temperature and hence closer to the final temperature when the phase transition ends. This makes using the percolation temperature a better approximation to estimate the thermal parameters. However, if the percolation temperature is significantly far away from the nucleation temperature, one should check if the phase transition can even reach completion at all for cases of strong supercooling, since the universe may become vacuum dominated. The strength of the phase transition and the inverse time duration of the phase transition take on the same form as in eq. (2.5)-(2.6) but with the replacement  $T_{n}\rightarrow T_{p}$  such that

$$
\alpha (T _ {p}) = \frac {1}{\rho_ {\mathrm {r a d}}} \left(\Delta V _ {\mathrm {e f f}} - \frac {1}{4} \frac {d \Delta V _ {\mathrm {e f f}}}{d T}\right) \Bigg | _ {T _ {p}}, \tag {2.12}
$$

and

$$
\beta = H _ {p} T _ {p} \frac {d \left(S _ {3} / T\right)}{d T}, \tag {2.13}
$$

where  $H_{p}$  is now the value of the Hubble parameter at the percolation temperature.

The gravitational wave spectrum in eq. (2.7) assumed that the lifetime of the source is approximately one Hubble time,  $H\tau_{sw} = 1$  [85]. It was later pointed out in [74], that a better approximation to the lifetime of the source is

$$
t _ {\mathrm {s w}} = \min  \left[ \frac {1}{H _ {p}}, \frac {R _ {*}}{U _ {f}} \right], \tag {2.14}
$$

where  $R_{*}$  is the mean bubble separation and  $U_{f}$  is the root mean squared velocity defined at  $\alpha (T_{p})$ . The mean bubble separation is related to the inverse time duration using  $R_{*} = (8\pi)^{1 / 3}v_w / \beta$ . We then take into account the finite lifetime of the source in the gravitational wave spectrum through

$$
\Omega_ {\mathrm {s w}} \rightarrow \Omega_ {\mathrm {s w}} t _ {\mathrm {s w}} H, \tag {2.15}
$$

and calculate all temperature dependent quantities at the percolation temperature  $T_{p}$  defined in eq. (2.11).

# 2.3 High diligence

The highest diligence with which one can calculate the gravitational wave spectrum involves a number of improvements to the predictions of the peak frequency and amplitude:

1 Improving on the bag model approximation for the fluid velocity and fraction of energy that is in gravitational waves;

2 Calculating the fluid velocity and efficiency from solving the hydrodynamic equations rather than using fits (related to the first);  
3 Calculating the mean bubble separation from the number density of the bubbles;  
4 Taking into account the finite lifetime of the soundwave source, derived in an expanding universe [103];  
5 Calculating the suppression due to reheated droplets creating friction that slows collisions.

Note that ref. [111] used the bag model in their simulations, so we assume that the suppression factor arising from kinetic energy lost in the fluid is independent of the change in the amplitude from improving on the bag model. Also in the last case, and only the last case, we use fits to estimate this degree of suppression as it relies on a full numerical simulation — methods to approximate this effect we leave to future work. In this section we outline in detail each of the other improvements.

# 2.3.1 Calculation of the percolation temperature

The false vacuum fraction at  $t > t_{c}$  in an expanding universe is defined as

$$
g (t _ {c}, t) = \exp \left[ - \frac {4 \pi}{3} \int_ {t _ {c}} ^ {t} d t ^ {\prime} p (t ^ {\prime}) a ^ {3} (t ^ {\prime}) r (t ^ {\prime}, t) ^ {3} \right] \equiv \exp [ - I (t) ], \qquad (2. 1 6)
$$

where  $I(t)$  represents the volume of nucleated bubbles per comoving volume, double counting the overlapped space between bubbles and virtual bubbles within others [112]. The comoving radius of a bubble nucleated at  $t'$  and measured at  $t$  is

$$
r \left(t ^ {\prime}, t\right) = \int_ {t ^ {\prime}} ^ {t} d t ^ {\prime \prime} \frac {v _ {w}}{a \left(t ^ {\prime \prime}\right)} = v _ {w} \left(\eta^ {\prime} - \eta\right), \tag {2.17}
$$

for FLRW space where  $\eta$  is the conformal time. This form of the comoving radius of the bubble assumes that the initial size of the bubble is negligible and the bubble wall velocity is constant.

The above equations can be recast in terms of integrals over temperature in order to render them more suitable for numerical computations. The scale factor of an expanding universe will have the form  $a = c_{a}t^{n}$  where  $c_{a}$  is a constant and  $n$  is determined by the form of energy that is dominating the expansion, i.e.  $n = 1/2$  and  $n = 2/3$  for radiation and matter respectively. The expansion of the universe may be treated as an adiabatic process so that the entropy  $s_{R}$  in the radiation sector is conserved per comoving volume:

$$
s _ {R} (T) a ^ {3} = \mathrm {c o n s t .} \tag {2.18}
$$

The radiation sector will have  $s_R \propto T^3$  which will typically give  $T \propto 1 / a \propto t^{-n}$ . This is valid for both a radiation dominated universe and a matter dominated universe. However if non-relativistic matter can decay into radiation, the dependence is  $T \propto a^{-3/8}$  [113]. In general, we may assume

$$
T \propto a ^ {- \gamma}, \tag {2.19}
$$

where  $\gamma$  will depend on the amount of entropy injection. The Hubble parameter is related to the rate of change of the scale factor,  $H = \dot{a} / a$ , and we then have

$$
\frac {1}{H} \frac {d T}{d t} = - \gamma T, \tag {2.20}
$$

which allows for rates of change with respect to time to be exchanged with that of temperature. We can also relate the scale factor at the time of the critical temperature,  $a_{c}$ , to the scale factor at a later time by

$$
\frac {a}{a _ {c}} = \left(\frac {T _ {c}}{T}\right) ^ {1 / \gamma}. \tag {2.21}
$$

For an expanding universe in a radiation dominated era, the total energy density is

$$
\rho_ {\text {t o t}} = \rho_ {\text {r a d}} + \Delta V, \tag {2.22}
$$

which consists of the relativistic matter density  $\rho_{\mathrm{rad}}$ , and the vacuum energy released during the phase transition. Accordingly the Hubble parameter in an expanding universe in this notation yields

$$
H (T) ^ {2} = \frac {8 \pi G}{3} \rho_ {\mathrm {t o t}} \left(\frac {1}{y ^ {4}} + \frac {\Delta V}{\rho_ {\mathrm {t o t}}}\right), \tag {2.23}
$$

with  $y = a / a_{c}$ . The above definitions can be used to convert any integral over time to that of temperature so that eq. (2.16)-(2.17) may be written as

$$
r \left(T ^ {\prime}, T\right) = \frac {v _ {w}}{a _ {c}} \int_ {T} ^ {T ^ {\prime}} \frac {d T ^ {\prime \prime}}{T ^ {\prime \prime}} \frac {1}{\gamma H \left(T ^ {\prime \prime}\right)} \left(\frac {T _ {c}}{T ^ {\prime \prime}}\right) ^ {- 1 / \gamma}, \tag {2.24}
$$

$$
I (T) = \frac {4 \pi}{3} \int_ {T} ^ {T _ {c}} \frac {d T ^ {\prime}}{T ^ {\prime}} \frac {1}{\gamma H (T ^ {\prime})} \bar {p} _ {0} T ^ {\prime 4} \exp \left[ - \frac {S _ {3} \left(T ^ {\prime}\right)}{T ^ {\prime}} \right] \left(\frac {T _ {c}}{T ^ {\prime}}\right) ^ {3 / \gamma} \left[ a _ {c} r \left(T ^ {\prime}, T\right) \right] ^ {3}, \tag {2.25}
$$

with  $g(T_c, T) = \exp[-I(T)]$ .

With the false vacuum fraction now defined as a function of temperature, the percolation temperature occurs when the false vacuum fraction is  $70\%$  of the total volume, i.e., when

$$
g \left(T _ {p}\right) = 0. 7. \tag {2.26}
$$

Similarly, the temperature when the phase transition ends occurs at the time when the volume of nucleated bubbles equals the comoving volume, i.e.  $I(t_{f}) = 1$ . This translates into

$$
g \left(T _ {f}\right) = e ^ {- 1}. \tag {2.27}
$$

In most cases, the percolation temperature calculated from eq. (2.26) should roughly coincide with the final temperature calculated from eq. (2.27) and depend on  $v_{w}$  and  $\Delta V$ .

# 2.3.2 Calculation of the nucleation temperature

The evolution of the mean bubble density per proper volume is determined by

$$
\frac {d [ n _ {b} a ^ {3} (t) ]}{d t} = p (t) g \left(t _ {c}, t\right) a ^ {3} (t), \tag {2.28}
$$

which begins at  $n_b(t_c) = 0$  and includes all the bubbles ever formed. We then transform the above result into an integral over temperature:

$$
n _ {b} (T) = \left(\frac {T}{T _ {c}}\right) ^ {3 / \gamma} \int_ {T} ^ {T _ {c}} \frac {d T ^ {\prime}}{T ^ {\prime}} \frac {1}{\gamma H (T ^ {\prime})} \bar {p} _ {0} T ^ {\prime 4} \exp \left[ - \frac {S _ {3} (T ^ {\prime})}{T ^ {\prime}} \right] g (T _ {c}, T ^ {\prime}) \left(\frac {T _ {c}}{T ^ {\prime}}\right) ^ {3 / \gamma}. \tag {2.29}
$$

The nucleation temperature can be numerically calculated as the temperature when there is one bubble per Hubble volume:

$$
\frac {n _ {b} \left(T _ {n}\right)}{H \left(T _ {n}\right) ^ {3}} = 1. \tag {2.30}
$$

The mean bubble density depends on the false vacuum fraction and therefore should change with  $v_{w}$ ,  $\kappa_{m}$ , and  $\Delta V$  as well.

# 2.3.3 Calculation of the mean bubble separation

The mean bubble separation  $R_{*}$  is related to the mean bubble number density and is given by

$$
R _ {*} = \left(\frac {1}{n _ {b}}\right) ^ {1 / 3}. \tag {2.31}
$$

The gravitational wave spectrum is usually written in terms of the inverse time duration of the phase transition where  $R_{*}$  and  $\beta$  are interchangeable. This form of the mean bubble separation can similarly be found in an expanding universe by Taylor expanding eq. (2.1) about  $\eta_0$  with respect to conformal time for exponential nucleation

$$
p (\eta) = p _ {0} \left(\eta_ {0}\right) \exp \left[ - S _ {0} + \beta_ {c} \left(\eta - \eta_ {0}\right) \right], \tag {2.32}
$$

where  $\beta_{c}$  is the comoving inverse time duration of the phase transition:

$$
\beta_ {c} = \left. \frac {d \ln p}{d \eta} \right| _ {\eta = \eta_ {0}}. \tag {2.33}
$$

The above Taylor expansion is valid in the regime where the false vacuum fraction decreases faster than the rate  $p$  increases which occurs when  $I(t)$  becomes order 1 and most of the bubbles are nucleated. The exponent of the false vacuum can be transformed into an integration over conformal time,  $dt = ad\eta$ :

$$
\begin{array}{l} I (\eta) = \frac {4 \pi}{3} \int_ {\eta_ {c}} ^ {\eta} d \eta^ {\prime} a ^ {4} \left(\eta^ {\prime}\right) p \left(\eta^ {\prime}\right) r \left(\eta^ {\prime}, \eta\right) ^ {3} \\ = 8 \pi \frac {v _ {w} ^ {3}}{\beta_ {c} ^ {4}} p _ {0} (\eta_ {0}) e ^ {- S _ {0} + \beta_ {c} (\eta - \eta_ {0})}, \tag {2.34} \\ \end{array}
$$

which can then be used to calculate the false vacuum fraction for  $\eta >\eta_c$ . If we define the comoving bubble number density as  $n_{b,c} = n_b a^3$ , we can rewrite eq. (2.28) in terms of conformal time:

$$
\frac {d \left(n _ {b , c}\right)}{d \eta} = p (\eta) g \left(\eta_ {c}, \eta\right) a ^ {4} (\eta). \tag {2.35}
$$

We now integrate over  $\eta$  to have

$$
n _ {b, c} = \frac {1}{\beta_ {c}} p _ {0} (\eta_ {0}) e ^ {- S _ {0} + \beta_ {c} (\eta_ {f} - \eta_ {0})} = \frac {\beta_ {c} ^ {3} (v _ {w})}{8 \pi v _ {w} ^ {3}}, \tag {2.36}
$$

where we used the relation that  $I(\eta_f) = 1$  for  $\eta_0 \sim \eta_f$ . The relation between the comoving mean bubble density and the mean bubble separation is now

$$
R _ {*, c} = (8 \pi) ^ {1 / 3} \frac {v _ {w}}{\beta_ {c} \left(v _ {w}\right)}, \tag {2.37}
$$

where  $\beta_{c}$  and  $R_{*,c}$  are both functions of the bubble wall velocity. The mean bubble separation at conformal time  $\eta$  is now related to the inverse time duration when the phase transition ends:

$$
R _ {*} (\eta) = \frac {a (\eta)}{a \left(\eta_ {f}\right)} (8 \pi) ^ {1 / 3} \frac {v _ {w}}{\beta \left(v _ {w}\right)}, \tag {2.38}
$$

where  $R_{*,c} = R_{*} / a(\eta)$  and  $\beta_{c} = a(\eta_{f})\beta$ . The above result can be transformed into a function of temperature using a relation similar to eq. (2.21) to give

$$
\frac {a (\eta)}{a \left(\eta_ {f}\right)} = \left(\frac {T _ {f}}{T}\right) ^ {1 / \gamma}. \tag {2.39}
$$

The procedure to calculate the inverse time duration of the phase transition at  $T_{f}$  for a fixed  $v_{w}$  is

1. Find  $T_{f}$  from the false vacuum fraction  $g(T_{c},T)$  for when  $I(T_{f}) = 1$ ;  
2. Calculate  $n_b(T_f)$  
3. Use  $R_{*}(T_{f}) = \left(\frac{1}{n_{b}(T_{f})}\right)^{1 / 3}$  
4. Solve eq. (2.38) using eq. (2.39) to get  $\beta(v_w)$ .

# 2.3.4 Going beyond the bag model

The free energy density  $f$  of a model with  $g_{*}$  degrees of freedom consists of a zero temperature scalar potential and a thermal potential that involves the summation over all relativistic species that interact with the scalar  $\phi$ . In the Standard Model, this involves the standard electroweak Higgs field and degrees of freedom  $g_{\mathrm{SM}} = 106.75$ . The free energy density gives

$$
f = V _ {0} (\phi) + T ^ {4} \left[ \sum_ {B} J _ {B} \left(\frac {M _ {B}}{T}\right) + \sum_ {F} J _ {F} \left(\frac {M _ {F}}{T}\right) \right], \tag {2.40}
$$

where the summations run over all relativistic bosons  $B$  and fermions  $F$  at temperature  $T$ . In the high temperature expansion, the free energy density can be written as

$$
f = - \frac {1}{3} \frac {\pi^ {2}}{3 0} g _ {*} T ^ {4} + V _ {T} (\phi), \tag {2.41}
$$

where  $V_{T}(\phi)$  is the thermal effective Higgs potential and we explicitly separate out the scalar independent terms that go as  $T^4$ . The hydrodynamics of the plasma can be described as a perfect fluid in terms of the energy density  $e$ , pressure  $p$ , and enthalpy  $\omega$ . These thermodynamic quantities can be explicitly calculated from the free energy density through

the relation  $p = -f(\phi, T)$  for the pressure. The energy density and enthalpy are then related to the pressure through

$$
e = T \frac {\partial p}{\partial T} - p, \qquad \omega = e + p = T \frac {\partial p}{\partial T}. \tag {2.42}
$$

These quantities together, along with the velocity of the fluid  $v$ , will give the energy momentum tensor of the plasma

$$
T ^ {\mu \nu} = u ^ {\mu} u ^ {\nu} \omega + g ^ {\mu \nu} p, \tag {2.43}
$$

where  $g^{\mu \nu}$  is the inverse Minkowski spacetime metric and  $u^{\mu}(v)$  is the four velocity of the fluid.

During the period of gravitational wave production, bubbles of the new phase will collide and generate sound waves in the perturbed plasma. The velocity profile around a single bubble is determined by the hydrodynamic quantities and the junction conditions across the bubble wall. We will denote the broken phase inside the bubbles by subscripts “ $b, -$ ” and the symmetric phase outside the bubbles as “ $s, +$ ”. The signs  $-, +$  are used to describe quantities behind and in front of the bubble wall. The continuity equations  $\partial_{\mu}T^{\mu \nu} = 0$  can be integrated in the wall frame across the bubble wall to give the junction conditions

$$
\frac {v _ {+}}{v _ {-}} = \frac {e _ {b} (T _ {-}) + p _ {s} (T _ {+})}{e _ {s} (T _ {+}) + p _ {b} (T _ {-})}, \tag {2.44}
$$

$$
v _ {+} v _ {-} = \frac {p _ {s} (T _ {+}) - p _ {b} (T _ {-})}{e _ {s} (T _ {+}) - e _ {b} (T _ {-})}, \tag {2.45}
$$

where  $v_{\pm}$  and  $T_{\pm}$  corresponds to the velocity and temperature of the fluid behind and in front of the bubble wall. We may assume that  $T_{+} \approx T_{-}$  and expand the thermodynamic quantities about the symmetric phase so that the ratio of velocities about the junction gives

$$
\frac {v _ {+}}{v _ {-}} \simeq \frac {\left(v _ {+} v _ {-} / c _ {s , b} ^ {2} - 1\right) + 3 \alpha_ {\bar {\theta} _ {+}}}{\left(v _ {+} v _ {-} / c _ {s , b} ^ {2} - 1\right) + 3 v _ {+} v _ {-} \alpha_ {\bar {\theta} _ {+}}}, \tag {2.46}
$$

where  $c_{s,b}$  is the speed of sound in the broken phase and  $\alpha_{\bar{\theta}_{+}}$  is the phase transition strength [105]. The speed of sound can be calculated in both the symmetric and broken phase and is defined in terms of the pressure as

$$
c _ {s} ^ {2} = \frac {d p / d T}{d e / d T} = \frac {p ^ {\prime} (T)}{T p ^ {\prime \prime} (T)}, \tag {2.47}
$$

where  $(\ldots)'$  denotes derivatives with respect to temperature. In terms of the free energy density, the pressure in the symmetric phase is  $\phi$  independent with  $p_s = -f(0,T)$  and the pressure in the broken phase is  $p_b = -f(\phi_{\mathrm{min}},T)$  which is evaluated at true vacuum  $\phi_{\mathrm{min}}$ . It is important to keep every term in the free energy density when calculating the speed of sound in order to properly account for the full temperature dependence of the model. This includes keeping all light degrees of freedom that do not acquire field dependent masses

that affect the Higgs effective potential. The new phase transition strength parameter  $\alpha_{\bar{\theta}_{+}}$  is dependent on the speed of sound in the broken phase and has a similar form to the bag parameter built up from the trace anomaly,

$$
\alpha_ {\bar {\theta} _ {+}} = \frac {\bar {\theta} _ {s} (T _ {+}) - \bar {\theta} _ {b} (T _ {+})}{3 \omega_ {s} (T _ {+})}, \mathrm {w i t h} \quad \bar {\theta} = \mathrm {e} - \mathrm {p / c _ {s} ^ {2}} \tag {2.48}
$$

[105]. Going back to the free energy density, we can define the phase transition strength as a function of temperature

$$
\alpha_ {\bar {\theta}} (T) = \frac {1}{3 \omega_ {s}} \left((1 + c _ {s} ^ {- 2}) \Delta V _ {T} - T \frac {d \Delta V _ {T}}{d T}\right), \tag {2.49}
$$

where  $V_{T}$  is the Higgs effective potential defined in eq. (2.40)-(2.41) and  $\Delta$  denotes the difference between the symmetric and broken phase. The phase transition strength has the same form as the bag model  $\alpha_{\theta}$  defined in eq. (2.5) when  $c_s^2 = 1 / 3$  and  $\omega_{s} = 4 / 3\rho_{\mathrm{rad}}$ . The junction conditions to obtain  $v_{\pm}$  will serve as boundary conditions for solving the velocity profile obtained from projecting the continuity equations into the parallel and perpendicular motions of the fluid flow. The hydrodynamic equations become

$$
(\xi - v) \partial_ {\xi} e = \omega \left[ 2 \frac {v}{\xi} + \gamma^ {2} (1 - \xi v) \partial_ {\xi} v \right], \tag {2.50}
$$

$$
(1 - v \xi) \partial_ {\xi} p = \omega \gamma^ {2} (\xi - v) \partial_ {\xi} v, \tag {2.51}
$$

where  $\xi = R / t$  is a self-similar coordinate defined as the ratio between the distance to the bubble center and the time since nucleation. These hydrodynamic equations may be combined to give the enthalpy profile and the velocity profile:

$$
2 \frac {v}{\xi} = \gamma^ {2} (1 - v \xi) \left[ \frac {\mu^ {2}}{c _ {s} ^ {2}} - 1 \right] \partial_ {\xi} v, \tag {2.52}
$$

$$
\partial_ {\xi} \omega = \omega \left(1 + \frac {1}{c _ {s} ^ {2}}\right) \gamma^ {2} \mu (\xi , v) \partial_ {\xi} v, \tag {2.53}
$$

where  $\partial_{\xi} = \partial_{\xi}e + \partial_{\xi}p$  and  $c_s^2 = dp / de$  are used to connect the equations. The Lorentz boost transformation used in the equations is defined in terms of the self-similar coordinate  $\mu (\xi ,v) = (\xi -v)\big / (1 - \xi v)$ . In detonations, the fluid velocity ahead of the bubble wall is always zero so that the hydrodynamic profiles are independent of the speed of sound in the symmetric phase. Deflagrations have a non-zero bubble wall velocity ahead of the bubble wall and the equations will then depend on the speed of sound in the symmetric phase. Both profile types will always depend on the speed of sound in the broken phase through the junction conditions. In detonation, it is sufficient to use  $\alpha_{\bar{\theta}_{+}} = \alpha_{\bar{\theta}}(T)$  with  $T$  usually taken as the nucleation temperature or the percolation temperature. Deflagrations and hybrid modes take  $\alpha_{\bar{\theta}}$  as input and require a shooting method by varying  $\alpha_{\bar{\theta}}$  until  $\alpha_{\bar{\theta}}$  is reached far away from the bubble.

The quantity of interest for the peak gravitational wave energy density is the kinetic energy fraction  $K$  which can be solved by the hydrodynamic equations:

$$
K = \frac {\rho_ {f l}}{e _ {s}}, \tag {2.54}
$$

![](images/1d1873186b86700fee279d187ff1f56f26afb8bbf1babb74ac98322329a83257.jpg)  
Figure 3. Suppression factor with respect to the strength of the phase transition due to vorticity and reheating effects in the plasma.  $\bar{\Omega}$  is the reduced peak gravitational wave energy density and  $\Omega_{\mathrm{exp}}$  is the expected peak gravitational wave energy density. The data is taken from [106].

where  $\rho_{\mathrm{fl}} = 3 / v_w^3\int d\xi \xi^2 v^2\gamma^2\omega$  is the fluid's kinetic energy. We use the publicly available code in [105] to numerically compute the kinetic energy efficiency  $\kappa_{\bar{\theta}}$  for a given set of  $c_s^2$  and  $\alpha_{\bar{\theta}}$  when comparing to calculations in the bag model. The kinetic energy fraction is related to the efficiency parameter through

$$
K = \left(\frac {\bar {\theta} _ {s} - \bar {\theta} _ {b}}{4 e _ {s}}\right) \kappa \left(\alpha_ {\bar {\theta}}, c _ {s, s} ^ {2}, c _ {s, b} ^ {2}\right), \tag {2.55}
$$

where

$$
\kappa = \frac {4 \rho_ {\mathrm {f l}}}{3 \alpha_ {\bar {\theta}} \omega_ {s}} \tag {2.56}
$$

[105]. The quantities  $c_{s,s}, c_{s,b}, e_s, \omega_s, \alpha_{\bar{\theta}}$ , and  $\kappa$  in determining the kinetic energy fraction  $K$  are all calculated at the final temperature  $T_f$  when the phase transition ends. The enthalpy-weight root-mean-square fluid velocity around a single bubble may be found from the kinetic energy fraction,

$$
\bar {U} _ {f} ^ {2} = \frac {e _ {s}}{\omega_ {s}} K, \tag {2.57}
$$

which is evaluated at  $T_{f}$ .

# 2.3.5 Gravitational wave spectrum

The first numerical simulations of strong first order phase transitions for  $\alpha \gtrsim 0.1$  were undertaken in [106] which showed that previous results overestimated the gravitational wave energy density. The rotational component of the fluid velocity, particularly for deflagrations, increases in relative size as the transition strength grows. This reduces the amount of available kinetic energy that can be transferred to the fluid. The rotational component for detonations, however, remains small and constant. The probable explanation for this effect is the formation of reheated droplets of the metastable phase that are produced during the

collisions of the bubble walls. These droplets can then slow down the bubble walls and reheat the surrounding regions. The simulations considered a simple bag equation of state where the results only depend on input parameters of  $v_{w}$  and  $\alpha$ . For a given  $v_{w}$ , we use an interpolation of their results to estimate the corresponding suppression factor to the  $\Omega_{\mathrm{GW}}h^{2}$  as a function of  $\alpha$ . We show the suppression factor in figure 3 for two representative bubble wall velocities. We utilize extrapolation for when  $\alpha$  is out of range. Although the results were performed using a bag equation of state, we numerically compute  $\alpha$  in the beyond the bag model and assume that the suppression from vorticity and reheating derived with a bag model applies without modification. We will test this assumption in future work. Furthermore, the simulations suggest that the RMS fluid velocity  $\bar{U}_{f}$  reaches a maximum that is under-approximated by calculating the expected  $\bar{U}_{f}$  around a single bubble. We use the results of  $\bar{U}_{f,\max} / \bar{U}_{f,\exp}$  to estimate the maximum fluid velocity in the highest diligence after calculating  $\bar{U}_{f}$  in the beyond the bag model.

A careful calculation of the gravitational wave production in an expanding universe will result in a suppression factor of the form

$$
\Upsilon_ {R D} = 1 - \frac {1}{y}, \tag {2.58}
$$

for a radiation dominated era where  $y = a / a_{s}$  is a dimensionless scale factor ratio normalized by when the source of production becomes active. For a radiation dominated era, the time elapsed since some reference time,  $t_{s}$ , is

$$
\left(t - t _ {s}\right) H _ {s} = \frac {y ^ {2} - 1}{2}. \tag {2.59}
$$

Due to the presence of shocks and turbulence in the plasma, the time elapsed is unlikely to last an arbitrarily long time. The effective lifetime of the source is then given by the timescale of turbulence,  $\tau_{\mathrm{sw}} = R_* / \bar{U}_f$ . This was the basis of the suppression factor used in eq. (2.14)-(2.15). We use the estimated maximum of the fluid velocity in the beyond the bag model when calculating the lifetime of the source. The gravitational wave energy density will then be suppressed by

$$
\Upsilon = 1 - \frac {1}{\sqrt {1 - 2 \tau_ {\mathrm {s w}} H _ {s}}}, \tag {2.60}
$$

which approaches the asymptotic value  $\Upsilon = 1$ , the lowest diligence, when  $\tau_{\mathrm{sw}}H_s \to \infty$ . When  $\tau_{\mathrm{sw}}H_s \ll 1$ , the suppression factor is approximately  $\Upsilon = \tau_{\mathrm{sw}}H_s$ , the modest diligence.

The peak gravitational wave energy density after taking into consideration the suppressions arising from vorticity and reheating effects in the plasma as well as the lifetime of source becomes

$$
h ^ {2} \Omega_ {\mathrm {G W}} = 8. 5 \times 1 0 ^ {- 6} \left(\frac {1 0 0}{g _ {*}}\right) ^ {1 / 3} K ^ {2} \left(\frac {H _ {*}}{\beta}\right) v _ {w} \Upsilon \left(\bar {U} _ {f, \max }, R _ {*}\right) \left(\frac {\bar {\Omega} (v _ {w} , \alpha)}{\bar {\Omega} _ {\exp} (v _ {w} , \alpha)}\right), \tag {2.61}
$$

where  $K$  is calculated in the beyond the bag,  $\beta / H_*$  is calculated from the mean bubble separation, and the last factor arises from the vorticity and reheating effects in the plasma.

# 3 Test models

In this section we examine the numerical difference in predictions arising from different levels of diligence in several models

1 The Standard Model Effective Field Theory (SMEFT), itself close to a toy model when it comes to cosmological phase transitions [37], but which allows for a comparison to the uncertainties arising from gauge dependence and the breakdown of perturbation theory as outlined in [93].  
2 Dark Higgs models [50], the simplest phase transition that can occur in a dark sector and has only three free parameters.  
3 A real scalar singlet extension to the standard model (xSM) [114]. A model that allows a tree level barrier, like SMEFT, but is on firmer footing as a physical theory.

Using a spectrum of models gives a realistic account of the size of the relative errors for different level of diligence without being overly sensitive to model specific effects. We will also present a toy model in the appendix B, that has the convenient property that much of the analysis can be done analytically.

# 3.1 SMEFT

SMEFT is a model independent method of examining many extensions of the Standard Model by augmenting it with a tower of high dimensional operators, each suppressed by higher and higher powers of the cutoff scale corresponding to the scale of new physics. Unfortunately, the Standard Model requires such a large change to its potential that the scale of new physics needs to be quite low to augment a strong first order phase transition [37]. In such a case the SMEFT only provides a qualitative description of the UV complete scalar sector, and then only in special circumstances [37]. In the SMEFT the tree level potential is augmented by a single higher dimensional operator

$$
V _ {\mathrm {t r e e}} = \mu_ {h} ^ {2} \phi^ {\dagger} \phi + \lambda (\phi^ {\dagger} \phi) ^ {2} + \frac {1}{M ^ {2}} (\phi^ {\dagger} \phi) ^ {3} + \Delta V, (3. 1)
$$

where  $M$  characterizes the cut off scale,  $\phi$  is the SM Higgs doublet and  $\Delta V_h$  is chosen such that the zero-temperature minimum is shifted to the origin. We will consider the full free energy density at one-loop given by

$$
f (\phi , T) = V _ {\mathrm {t r e e}} + V _ {\mathrm {C W}} + V _ {\mathrm {C T}} + V _ {T}, \tag {3.2}
$$

where  $V_{\mathrm{CW}}$  is the Coleman-Weinberg contribution and  $V_{T}$  is the finite-temperature correction. These are given by

$$
V _ {\mathrm {C W}} (h, \mu) = \frac {1}{6 4 \pi^ {2}} \sum_ {\alpha} N _ {\alpha} M _ {\alpha} ^ {4} (h) \left[ \log \frac {M _ {\alpha} ^ {2} (h)}{\mu^ {2}} - C _ {\alpha} \right], \tag {3.3}
$$

and

$$
\begin{array}{l} V _ {T} (h, T) = \frac {T ^ {4}}{2 \pi^ {2}} \sum_ {\alpha} N _ {\alpha} \int_ {0} ^ {\infty} d x x ^ {2} \log \left[ 1 \pm e ^ {- \sqrt {x ^ {2} + M _ {\alpha} ^ {2} (h) / T ^ {2}}} \right] \qquad (3. 4) \\ + \frac {T}{1 2 \pi} \sum_ {\text {b o s o n s} \alpha} N _ {\alpha} \left[ M _ {\alpha} ^ {3} (h) - M _ {T, \alpha} ^ {3} (h, T) \right], \tag {3.5} \\ \end{array}
$$

where  $N_{\alpha}$  counts the number of degrees of freedom of each particle and  $C_{\alpha}$  is a constant that is 5/6 for gauge bosons and 3/2 for all others. We note that the daisy terms in eq. (3.5) are the result of a high temperature expansion which may cause an IR-divergence in the speed of sound for low temperatures [105]. We explicitly check this by including a Boltzmann suppression term when  $M_{\alpha} \lesssim 2.2T$ . The sums run over the top quark,  $W$  and  $Z$  bosons, and the Higgs boson  $h$ . The total degrees of freedom in SMEFT is the Standard Model value  $g_{\mathrm{SM}} = 106.75$ . The calculation of the speed of sound requires including all the relativistic particle species in the free energy density. We will account for the remaining light particles that were neglected in  $V_{T}$  by including the term:

$$
\delta V _ {T} (h) = - \frac {\pi^ {2}}{9 0} g _ {*} ^ {\prime} T ^ {4}, \tag {3.6}
$$

to the free energy density where  $g_{*}^{\prime} = 345 / 4$ . However, in the bag model, the speed of sound is taken to be  $c_s^2 = 1 / 3$  and the light species can be ignored as they do not affect the phase transition dynamics. The last term in  $V_{T}$  corresponds to the resummation of the daisy terms of the scalar bosons. To calculate the effective potential and the counter-terms at zero-temperature, we fix the zero-temperature  $\overline{\mathrm{MS}}$ -parameters by matching the physical observables at the  $Z$  boson pole mass  $m_Z$  using the full self energies. To go beyond the bag model, we need the absolute pressure in each phase, and not just the relative pressure. We therefore add an overall constant in the potential such that the pressure in the broken phase at zero temperature vanishes at one loop. The scale of the Coleman-Weinberg potential is taken to be at  $\mu \sim T$  for the dynamics of the phase transition and we run the parameters to this scale.

# 3.2 Dark renormalizable models

Here we will consider a dark Higgs model [48, 50, 62, 63] of the type  $\mathrm{SU}(N) / \mathrm{SU}(N - 1)$  with renormalizable operators following the conventions in [50]. The overall scale  $\Lambda$  and the zero temperature vacuum expectation value  $v$  are the only inputs of the model. We can then define the zero temperature parameters such as the tachyonic mass and self coupling as

$$
- \mu^ {2} (0) = - \frac {\Lambda^ {4}}{v ^ {2}}, \tag {3.7}
$$

$$
\lambda (0) = \frac {\Lambda^ {4}}{v ^ {4}}, \tag {3.8}
$$

where factors of  $v / \Lambda$  will control the thermal parameters. The tree level potential is then defined as

$$
V (H) = \Lambda^ {4} \left[ - \frac {1}{2} \left(\frac {h _ {D}}{v}\right) ^ {2} + \frac {1}{4} \left(\frac {h _ {D}}{v}\right) ^ {4} \right] + \Delta V, \tag {3.9}
$$

where  $h_D$  is the dark Higgs of the doublet  $H$  and  $\Delta V$  shifts that potential at the minimum to zero. The degrees of freedom of the full dark sector in consideration are

$$
n _ {H} = 1, n _ {G} = 2 N - 1, n _ {G B} = 3 \times (2 N - 1), n _ {f} = 2 \times N \times N _ {f}, \qquad (3. 1 0)
$$

where  $n_G$  is the number of Goldstone bosons,  $n_{GB}$  are the gauge bosons,  $N_f$  is the number of fermions, and  $N$  is the rank of the group.

The free energy density in consideration is

$$
f (h _ {D}, T) = V _ {\mathrm {t r e e}} + V _ {\mathrm {C W}} + V _ {\mathrm {C T}} + V _ {T} + \delta V _ {T}, \tag {3.11}
$$

where  $V_{\mathrm{CW}}$  and  $V_{T}$  are defined in eq. (3.3)-(3.5). Here the summations now only run over the dark sector particles. This requires us to add on the additional relativistic particles not included in the sum which now include the full degrees of freedom of the Standard Model:

$$
\delta V _ {T} = - \frac {\pi^ {2}}{9 0} g _ {*} T ^ {4}, \tag {3.12}
$$

where  $g_{*} = 106.75$ . We add the term  $\Delta V$  so that the minimum of the tree-level potential is shifted to zero. We choose the scale of the one-loop potential to be at  $\Lambda$ .

The inclusion of the CW-term will shift the zero-temperature vacuum expectation value away from  $v$ . We add the counter-term potential

$$
V _ {\mathrm {C T}} (h _ {D}) = - \frac {\delta \mu^ {2}}{2} h _ {D} ^ {2} + \frac {\delta \lambda}{4} h _ {D} ^ {4} + \delta \Delta V _ {h}, \tag {3.13}
$$

where  $\delta \mu^2$ ,  $\delta \lambda$ , and  $\delta \Delta V_h$  are chosen such that

$$
\left. \frac {\partial f \left(h _ {D} , 0\right)}{\partial h _ {D}} \right| _ {v} = 0, \tag {3.14}
$$

$$
\left. \frac {\partial^ {2} f \left(h _ {D} , 0\right)}{\partial h _ {D} ^ {2}} \right| _ {v} = m ^ {2} (0) \equiv 2 \frac {\Lambda^ {4}}{v ^ {2}}, \tag {3.15}
$$

$$
f (v, 0) = 0, \tag {3.16}
$$

to maintain the tree-level structure of the potential. We work in the Landau gauge where the Goldstone bosons have zero mass at the  $h_D = v$  which causes an IR-divergence in the one-loop potential. This causes an issue in the evaluation of the counter-terms. One prescription is to remove the Goldstone bosons from the sum in the CW potential. For the purpose of this work, we will follow the procedure in [115] to evaluate the counterterms. This shifts the Goldstone mass by its mass at the one-loop level, i.e

$$
m _ {G} \left(h _ {D}\right)\rightarrow m _ {G} \left(h _ {D}\right) + \frac {1}{h _ {D}} \frac {\partial V ^ {(1)}}{\partial h _ {D}}, \tag {3.17}
$$

where

$$
m _ {G} (h _ {D}) = \Lambda^ {4} \left(\frac {h _ {D} ^ {2}}{v ^ {4}} - \frac {1}{v ^ {2}}\right), \tag {3.18}
$$

is the field dependent mass of the Goldstone bosons.

# 3.3 xSM

The singlet extended SM, known as "xSM", consists of the standard SM Higgs doublet  $H^{T} = \left(G^{+},\left(v_{\mathrm{EW}} + h + iG^{0}\right) / \sqrt{2}\right)$  and a real gauge singlet  $S = v_{s} + s$  where the electroweak vacuum is  $(v_{\mathrm{EW}},v_s)$  [28, 38, 116-122]. The tree level potential in this setup is defined as

$$
\begin{array}{l} V (H, S) = - \mu^ {2} H ^ {\dagger} H + \lambda \left(H ^ {\dagger} H\right) ^ {2} + \frac {a _ {1}}{2} H ^ {\dagger} H S \\ + \frac {a _ {2}}{2} H ^ {\dagger} H S ^ {2} + \frac {b _ {2}}{2} S ^ {2} + \frac {b _ {3}}{3} S ^ {3} + \frac {b _ {4}}{4} S ^ {4} + \Delta V, \tag {3.19} \\ \end{array}
$$

where  $\Delta V$  shifts the minimum of the potential to zero. The mass parameters  $\mu^2$  and  $b_{2}$  are related to the other model parameters through the minimization conditions around the electroweak vacuum,

$$
\mu^ {2} = \lambda v _ {\mathrm {E W}} ^ {2} + \frac {1}{2} v _ {s} \left(a _ {1} + a _ {2} v _ {s}\right),
$$

$$
b _ {2} = \frac {1}{4 v _ {s}} \left[ v _ {\mathrm {E W}} ^ {2} \left(a _ {1} + 2 a _ {2} v _ {s}\right) + 4 v _ {s} ^ {2} \left(b _ {3} + b _ {4} v _ {s}\right) \right]. \tag {3.20}
$$

The parameters  $\lambda$ ,  $a_1$ , and  $a_2$  are related to the physical parameters  $\theta$ ,  $m_{h_1}$ , and  $m_{h_2}$  through the mass matrix diagonalization as

$$
\lambda = \frac {m _ {h _ {1}} ^ {2} c _ {\theta} ^ {2} + m _ {h _ {2}} s _ {\theta} ^ {2}}{2 v _ {\mathrm {E W}} ^ {2}},
$$

$$
a _ {1} = \frac {2 v _ {s}}{v _ {\mathrm {E W}} ^ {2}} \left[ 2 v _ {s} ^ {2} \left(2 b _ {4} + \tilde {b} _ {3}\right) - m _ {h _ {1}} ^ {2} - m _ {h _ {2}} + c _ {2 \theta} \left(m _ {h _ {1}} ^ {2} - m _ {h _ {2}} ^ {2}\right) \right],
$$

$$
a _ {2} = - \frac {1}{2 v _ {\mathrm {E W}} ^ {2} v _ {s}} \left[ - 2 v _ {s} \left(m _ {h _ {1}} ^ {2} + m _ {h _ {2}} ^ {2} - 4 b _ {4} v _ {s} ^ {2}\right) + \left(m _ {h _ {1}} ^ {2} - m _ {h _ {2}} ^ {2}\right) \left(2 c _ {2 \theta} v _ {s} - v _ {\mathrm {E W}} s _ {2 \theta} + 4 \tilde {b} _ {3} v _ {s} ^ {3}\right) \right], \tag {3.21}
$$

where  $\tilde{b}_3\equiv b_3 / v_s$  and  $\theta$  is the mixing angle of the physical fields  $h_1$  and  $h_2$  defined as

$$
h _ {1} = c _ {\theta} h + s _ {\theta} s, \quad h _ {2} = - s _ {\theta} h + c _ {\theta} s, \tag {3.22}
$$

with  $s_{\theta} \equiv \sin(\theta)$  and  $c_{\theta} \equiv \cos(\theta)$ . Here we associate  $h_1$  as the SM Higgs and  $h_2$  is some heavier scalar.

The free energy density we consider in the xSM presented here contains only the high temperature expansion approximation of the full finite temperature one loop effective potential since the phase transition is primarily driven by the cubic terms. The free energy is then

$$
\begin{array}{l} f (h, s, T) = - \frac {1}{2} \left[ \mu^ {2} - \Pi_ {h} (T) \right] h ^ {2} - \frac {1}{2} \left[ - b _ {2} - \Pi_ {s} (T) \right] s ^ {2} \\ + \frac {1}{4} \lambda h ^ {4} + \frac {1}{4} a _ {1} h ^ {2} s + \frac {1}{4} a _ {2} h ^ {2} s ^ {2} + \frac {b _ {3}}{3} s ^ {3} + \frac {b _ {4}}{4} s ^ {4} \\ - \frac {1}{3} \frac {\pi^ {2}}{3 0} g _ {*} T ^ {4}, \tag {3.23} \\ \end{array}
$$

where we take  $g_{*} = 106.75$ . The field dependent thermal mass  $\Pi_h(T)$  and  $\Pi_s(T)$  are

$$
\Pi_ {h} (T) = \left(\frac {2 m _ {w} ^ {2} + m _ {z} ^ {2} + 2 m _ {t} ^ {2}}{4 v ^ {2}} + \frac {\lambda}{2} + \frac {a _ {2}}{2 4}\right) T ^ {2},
$$

$$
\Pi_ {s} (T) = \left(\frac {a _ {2}}{6} + \frac {b _ {4}}{4}\right) T ^ {2}, \tag {3.24}
$$

where the physical masses of the  $W$ ,  $Z$ , and  $t$ -quark are used to define the gauge and Yukawa couplings to  $h$ .

# 4 Results

The resulting gravitational wave spectrum is dependent on the level of precision of the thermal parameters. Until recently, the bag model was assumed to compute the phase transition strength and the kinetic energy of the fluid. Going beyond the bag model will require the calculation of the speed of sound in the plasma for both the symmetric and broken phase which should result in a more accurate treatment of the thermal parameters. These quantities are temperature dependent and will change depending on the temperature at which they are computed. Furthermore, the temperature scales of the phase transition such as the nucleation and percolation temperature are also sensitive to level of diligence in the calculations. We use the publicly available codes CosmoTransitions [108] and BubbleProfiler [123] to compute the actions in order to find the relevant transition temperatures.

The lowest diligence level will compute the thermal parameters at the estimated nucleation temperature defined in eq. (2.4). The strength of the phase transition is calculated using eq. (2.5), the inverse time duration of the phase transition is calculated using eq. (2.6), and the peak gravitational wave energy density is calculated using eq. (2.7).

The modest diligence level will compute the thermal parameters at the estimated percolation temperature in eq. (2.11). We will use eq. (2.12), eq. (2.13), and eq. (2.15) to estimate the strength of the phase transition, inverse time duration, and peak gravitational wave spectrum respectively. The lifetime of the source is estimated using eq. (2.14). There is an ambiguity as to which temperature to employ in the calculation of the thermal parameters: the nucleation temperature or the percolation temperature. The true percolation temperature  $T_{p}$ , eq. (2.26), should lie close to the temperature at which the phase transition ends  $T_{f}$ . The inverse time duration should be computed from the mean bubble separation, eq. (2.31) and eq. (2.31), which is evaluated at  $T_{f}$ . The highest diligence will evaluate all thermal parameters at  $T_{f}$  to ensure that all quantities are evaluated at the same temperature as the inverse time duration. From here on out, we will associate  $T_{p}$  with eq. (2.11) when referring to modest diligence. The highest diligence will also utilize the beyond the bag model to calculate the strength of the phase transition eq. (2.49) and the kinetic energy fraction eq. (2.55) which requires the numerically calculated speed of sound in eq. (2.47). The lowest and modest diligence calculations will assume  $c_{s}^{2} = 1 / 3$  as is done in the bag model. The peak gravitational wave spectrum is found from eq. (2.61) which accounts for the lifetime of the source, eq. (2.60), as well as vorticity and reheating

![](images/694f873948b437ac75e22bfab5071e50419927aa58a2a1746f1f78026492e523.jpg)

![](images/ec26cc64bc15846b116779c5bf886592d3ae7460738c99c9846253d783c64fbd.jpg)

![](images/11af273f1b03338f3d6d6fc4e1f099a868b32f42e92d49bc72885b1461962965.jpg)  
Figure 4. SMEFT: the top left panel shows the speed of sound calculated in the symmetric and broken phase using eq. (2.47) at the different levels of diligence. The gray dashed line corresponds to the bag model with  $c_s^2 = 1/3$ . The symmetric phase (solid magenta) is only shown at highest diligence. The top right panel shows the strength of the phase transition at the different levels of diligence using eq. [(2.5), (2.12), (2.49)]. The bottom panel shows the kinetic energy fraction at the different levels of diligence where the lowest and modest diligence use fits for  $\kappa$  to get  $K$  and the highest diligence uses eq. (2.55). The temperatures are set to  $T_n$  (2.4),  $T_p$  (2.11), and  $T_f$  (2.27) for the lowest, modest, and highest diligence respectively. The numerical calculation of the speed of sound only enters in the highest diligence of  $\alpha$ .

effects in the plasma. We note that the suppression factor due to the finite lifetime used in eq. (2.14) is a valid approximation of eq. (2.60) only when  $\tau_{\mathrm{SW}}H\ll 1$

In the following sections, we will compare the different levels of diligence in SMEFT, the dark renormalizable model, and xSM. The error in the peak gravitational wave energy density,

$$
\frac {\Delta \Omega}{\Omega} = \frac {\left| \Omega^ {j} h ^ {2} - \Omega^ {\text {h i g h}} h ^ {2} \right|}{\min  \left[ \Omega^ {j} h ^ {2} , \Omega^ {\text {h i g h}} h ^ {2} \right]}, \tag {4.1}
$$

where  $j = (\mathrm{low}, \mathrm{mod})$  refers to lowest, modest, and highest diligence respectively, will be used to compare the different levels of diligence.

# 4.1 SMEFT

The SMEFT model we consider has the scale of the zero-temperature one loop potential set to  $\mu = T$  as well as temperature dependence in the running of the couplings. This will contribute additional temperature dependence to the speed of sound calculations in the broken phase. We note that ref. [124] also considered the beyond the bag model in

![](images/b1a1205f6ab405c616da3cb893f2ce5a00d221153078ff59399a48cb391ffcda.jpg)  
Figure 5. SMEFT: the left panel shows the inverse time duration of the phase transition at the different levels of diligence using eq. [(2.6), (2.13), (2.37)]. The lowest and modest diligences are estimated using the first derivative of the action  $dS / dT$  and the highest diligence is computed directly from the mean bubble separation, eq. (2.31) and eq. (2.38). The right panel shows the suppression factor due to the lifetime of the source using eq. (2.14) and eq. (2.60) for modest and highest diligence respectively. The lowest diligence corresponds to  $\Upsilon \rightarrow 1$ . The temperatures are set to  $T_{n}$  (2.4),  $T_{p}$  (2.11), and  $T_{f}$  (2.27) for the lowest, modest, and highest diligence respectively.

![](images/d97318dc89fc04480d6cd801586a486ba3caefb36bb4cdb9f89a53304bb9a3db.jpg)

SMEFT using a high temperature expansion of the effective potential. The speed of sound will never reach the bag model with  $c_s^2 = 1/3$  as seen in the top figure left of figure 4. The green curves show the different levels of diligence for the speed of sound in the broken phase and the dashed gray curve represents  $c_s^2 = 1/3$ . The magenta curve is the speed of sound calculated in symmetric phase which is approximately the same in each level and does not deviate far from the bag model. We do not consider any additional relativistic degrees of freedom and thus expect little deviations between the speed of sound in the symmetric phase. As the scale  $M$  grows large, the speed of sound in the broken phase approaches a constant value of  $c_s^2 \sim 0.32$ . There is noticeable disagreement between the different levels below  $M = 600$  where there is mild supercooling. For a given  $M$ , the speed of sound is only a function of temperature. The differences in  $c_s^2$  in the broken phase is the result of these different temperatures at which the speed of sound is set to when calculating the strength of the phase transition  $\alpha_{\bar{\theta}}(c_s^2)$ . The large difference in  $T_p$  and  $T_f$  is due to the approximations of  $T_p$  in eq. (2.11) which is less accurate when  $S_3 / T$  acquires a minimum for smaller  $M$ .

On the top right panel of figure 4 we show the strength of the phase transition computed at the different levels of diligence. Both the lowest and modest diligence curves have  $c_s^2 = 1/3$  whereas the highest diligence curve corresponds to the beyond the bag calculation with  $c_s^2$  shown in the top left panel. Although each level is computed at different temperatures, the lowest diligence is a better approximation of the strength of the phase transition compared to level 2 which over approximates  $\alpha$ . This is a result of  $T_p$  computed in the modest diligence placing far below  $T_f$  which results in a higher estimated  $\alpha$ . The difference between the different levels on the strength of the phase transition is negligible for large  $M$  as a result of the asymptotic behavior observed in  $c_s^2$  and the better approximation of  $T_p$  when there is no barrier present. There is also a dependence on the bubble wall velocity in

![](images/c7336de2c3e23eeebbed30667639d5dda1cb72f59f4649958725e79955642fcc.jpg)  
Figure 6. SMEFT: the relative error when using the lowest and modest levels of diligence, compared to the highest level of diligence (for which  $\Delta \Omega / \Omega = 0$ ). The vertical axis shows the peak (frequency-independent) gravitational wave energy density for detonation. The precise definition of  $\Delta \Omega / \Omega$  is given in eq. (4.1). The horizontal axis corresponds to the cutoff scale  $M$ .  $\Delta \Omega / \Omega$  is displayed for deflagration and detonation at different levels of diligence using eq. [(2.7), (2.15), (2.61)] and eq. (4.1). The temperatures are set to  $T_{n}$  (2.4),  $T_{p}$  (2.11), and  $T_{f}$  (2.27) for the lowest, modest, and highest diligence respectively. Both the modest and highest diligence contains suppression factors due to the lifetime of the source. The highest diligence contains the suppression factor due to vorticity effects in the plasma.

![](images/a049e3c3ef824bb6ea8ec7846f78422d36289c4b0cbabed981cd6502a27feb2b.jpg)

both  $c_s^2$  and  $\alpha$  for the modest and highest diligence curves in computing  $T_p$  and  $T_f$  but we only show detonation with  $v_w = 0.92$  because the difference is minor. The kinetic energy fraction is shown in the bottom panel of figure 4 and should depend on the speed of sound and phase transition strength. Similar to what was seen in  $\alpha$ , the lowest and highest diligence curves are closer together for large  $M$  while the modest diligence curve is the least accurate. For each of the levels, the largest error in both  $\alpha$  and  $K$  occurs for smaller  $M$  where the speed of sound is significantly lower than  $c_s^2 = 1/3$  and  $T_p$  is far from  $T_f$ .

In the left panel of figure 5, we show the inverse time duration  $\beta / H$  of the phase transition for detonation. The largest difference between modest diligence and highest diligence occurs for small  $M$  and is due to the following reason: the minimum formed in the action where  $T_{p}$  calculated in eq. (2.11) along with  $\beta / H$  in eq. (2.13) are inaccurate when there is a minimum present. The lowest diligence is a better approximation than the modest diligence in this regime. The modest and the highest diligence become indistinguishable for large  $M$  when there is no minimum in the action. For small  $M$ , the lowest diligence curve appears to be a good approximation for modest diligence. Although  $\beta / H$  estimated from the action is not accurate when there is a minimum, the error using  $T_{n}$  appears to do better than using the approximation of  $T_{p}$ . Contrary to the  $\alpha$  and  $K$ ,  $\beta$  in the lowest diligence never approaches the highest diligence for large  $M$  where the error appears to get worse. This is due to the inaccuracy in using the approximate  $T_{n}$ . In this regime,  $T_{p}$  is a better approximation of the inverse time duration as there is no minimum present in the action. The right panel of figure 5 shows the suppression factor due to the lifetime of the source in the modest and highest diligence. The error between the two levels gets worse for small  $M$  which is the result of the error in  $T_{p}$ . The error approaches a constant as  $M$  gets large.

![](images/7384494350428486e7cb67873daab60fecd9c94bfa4d8de4952a2baab85153c8.jpg)  
Figure 7. Dark  $RG$ : the left panel shows the speed of sound calculated in the symmetric and broken phase using eq. (2.47) at the different levels of diligence. The gray dashed line corresponds to the bag model with  $c_s^2 = 1/3$ . The symmetric phase (solid magenta) is only shown at highest diligence. The right panel shows the strength of the phase transition at the different levels of diligence using eq. [(2.5), (2.12), (2.49)]. The temperatures are set to  $T_n$  (2.4),  $T_p$  (2.11), and  $T_f$  (2.27) for the lowest, modest, and highest diligence respectively. The numerical calculation of the speed of sound only enters in the highest diligence of  $\alpha$ .

![](images/6501051d884929b708687328363a8a7c3ffbb4d3976f0560078841369c7fd458.jpg)

In figure 6 we show the relative error in the peak gravitational wave spectrum for both deflagration and detonation. The error with respect to the highest diligence is estimated using eq. (4.1). For both deflagration and detonation, the modest diligence spikes to an error of  $\Delta \Omega / \Omega \sim 10^2$  for small M. This is correlated with the large error observed in  $\alpha$ ,  $K$ ,  $\beta$ , and  $\Upsilon$  seen in figure 4 and figure 5. The modest diligence error for both profile types slowly approach a constant value as M grows large which is the result of the minimal error in  $\alpha$ ,  $\beta / H$ ,  $K$ . The error in  $\Upsilon$  appears to become a constant for large  $M$ . The suppression factors due to the lifetime of the source grow to zero as  $M$  grows large which results in the increasing behavior of the peak error in the lowest diligence which does not include any suppression factors. Overall we notice an error in the peak gravitational wave energy density of  $10^{1} - 10^{2}$  for lowest diligence and  $10^{0} - 10^{2}$  for modest diligence.

# 4.2 Dark renormalizable models

The dark renormalizable model considered in the analysis does not couple to the Standard Model and will consist of a  $N = 10$  group, and  $2N - 1$  gauge bosons with charge  $g_{D} = 0.8$ . The scale of the one-loop potential is also  $T$  independent. These will result in a speed of sound in the symmetric phase that differs from the one seen in SMEFT.

We show the speed of sound calculated using eq. (2.47) on the left panel of figure 7 for the different levels of diligence. The differences between the levels of diligence in the speed of sound are only minor. We show only the highest diligence curve for the speed of sound in the symmetric phase. For small  $v / \Lambda$ , the speed of sound in the symmetric phase remains constant with a value slightly above the one given in the bag model. This is attributed to the additional degrees of freedom arising from the dark sector. The speed of sound above  $v / \Lambda = 2.6$  begins to decrease until it reaches a discontinuity near  $v / \Lambda = 2.8$ . It then jumps to  $c_s^2 = 0.336$  where it begins to monotonically increase. This discontinuity is a result of

![](images/d32ba8ff3011171d6cd32a9784939420e47f77b168b57cc431b87eeae167d753.jpg)  
Figure 8. Dark  $RG$ : the inverse time duration of the phase transition at the different levels of diligence using eq. [(2.6), (2.13), (2.37)]. The lowest and modest diligences are estimated using the first derivative of the action  $dS / dT$  and the highest diligence is computed directly from the mean bubble separation. The right panel shows the suppression factor due to the lifetime of the source using eq. (2.14) and eq. (2.60) for modest and highest diligence respectively. The lowest diligence corresponds to  $\Upsilon \rightarrow 1$ . The temperatures are set to  $T_{n}$  (2.4),  $T_{p}$  (2.11), and  $T_{f}$  (2.27) for the lowest, modest, and highest diligence respectively.

![](images/da0edfca60a6559933a252db8721d273a1218f9c135b92ab5b2c4435589df6ae.jpg)

the daisy terms in the effective potential. With out the daisy terms, the speed of sound in the symmetric phase would be smoothly connected and monotonically increasing.

The strength of the phase transition is plotted on the right panel figure 7. The different levels appear to agree very well with each other with the lowest diligence becoming slightly worse at high  $v / \Lambda$ . For most of the parameter space, the highest diligence has the greatest  $\alpha$  because it is computed at the numerically calculated values for  $c_s^2$  in the broken phase which results in a amplification compared to the other two levels. This is due to the factor  $(1 + c_s^{-2})$  in  $\alpha_{\bar{\theta}}$ . The error between the modest and highest diligence begins to decrease as  $v / \Lambda$  increases which is related to the speed of sound approaching  $c_s^2 = 1/3$ . Despite the differences between the different levels, the speed of sound in the broken phase lies between  $c_s^2 \sim 0.325 - 0.330$  and does not contribute a significant source of error to the strength of the phase transition.

The inverse duration of the phase transition is plotted in the left panel of figure 8 for detonation. The lowest diligence calculated using eq. (2.6) consistently over approximates  $\beta / H$  while modest diligence calculated using eq. (2.13) agrees well with the highest diligence found from the mean bubble separation. There were no minima found in the action for any of the parameters in consideration so the difference between  $T_{p}$  calculated using eq. (2.11) in the modest diligence and  $T_{f}$  calculated using eq. (2.27) in the highest diligence is only minor. The dips near  $v / \Lambda > 2.8$  in  $\beta / H$  are the result of the shape of  $S(T) / T$  which causes the highest error between the modest and highest diligence. This dip also effects the suppression factor due to the lifetime of the source as seen in the right panel of figure 8. The modest diligence over-approximates the suppression factor up until  $v / \Lambda \sim 2.8$  where they eventually become approximately equal in magnitude. The large  $v / \Lambda$  regime has a small  $\beta / H$  and large  $\alpha$  which results in a small lifetime of the source  $\tau_{\mathrm{sw}}$ . The modest diligence suppression factor is then an appropriate approximation in this regime.

![](images/1e9410aab0e5e26641f6b6ebfafc83adeebe9f9e35f0e4aaddc710a687b74955.jpg)  
Figure 9. Dark  $RG$ : the relative error when using the lowest and modest levels of diligence, compared to the highest level of diligence (for which  $\Delta \Omega / \Omega = 0$ ). The vertical axis shows the peak (frequency-independent) gravitational wave energy density for detonation. The precise definition of  $\Delta \Omega / \Omega$  is given in eq. (4.1). The horizontal axis corresponds to the ratio of the tree level v.e.v to the cut off scale  $v / \Lambda$ .  $\Delta \Omega / \Omega$  is displayed for deflagration and detonation at different levels of diligence using eq. [(2.7), (2.15), (2.61)] and eq. (4.1). The temperatures are set to  $T_{n}$  (2.4),  $T_{p}$  (2.11), and  $T_{f}$  (2.27) for the lowest, modest, and highest diligence respectively. Both the modest and highest diligence contains suppression factors due to the lifetime of the source. The highest diligence contains the suppression factor due to vorticity effects in the plasma.

![](images/57431a6e5fff2f165d288c2920f2704f9261c902d5d389487b286d8f7d676b9b.jpg)

The error in the gravitational wave spectrum is shown in figure 9 for deflagration and detonation. For both the lowest and modest diligence, the error remains roughly constant until  $v / \Lambda \sim 2.8$  where it exhibits some oscillations. This behavior is related to the dips in figure 8. Past  $v / \Lambda \sim 2.8$ , both the lowest and modest diligence begin to increase. The error in the lowest diligence past this point is dominated by the lack of suppression factor due to the lifetime of the source. The suppression factor remains roughly constant until  $v / \Lambda \sim 2.8$  where it begins to approach zero and as a result increases the error. The increasing behavior in the modest diligence is likely due to the separation in  $\beta / H$  between the modest and highest diligence in figure 8 and the suppression factor from vorticity and reheating effects in the plasma which are stronger for larger  $\alpha$ . The values of the speed of sound in the symmetric and broken phase calculated at  $T_{f}$  are not far from the bag model of  $c_{s}^{2} = 1 / 3$  and we do not consider it a strong source of error in the peak gravitational wave energy density spectrum. Overall we notice an error in the peak gravitational wave energy density of  $10^{1} - 10^{3}$  for lowest diligence and  $10^{-1} - 10^{1}$  for modest diligence.

# 4.3 xSM

We show in the top left panel of figure 10 the speed of sound in the symmetric and broken phase for a scan over the heavy singlet mass in the xSM model while holding all other parameters constant. The speed of sound in the symmetric phase is approximately  $c_s^2 = 1 / 3$  as in the bag model. The speed of sound in broken phase deviates far from the bag model where it approaches zero as  $m_{h_2} \to 0$ . The speed of is strongly correlated with the cubic term that arises from the extra scalar who also acquires a tree level vacuum expectation value. The speed of sound can then be suppressed by increasing the  $b_{3}$  parameter. This strong suppression in the broken phase speed of sound will lead to an amplification in the

![](images/ddbc9d9f608c28db52e58d8ffa42f2a4505e54774cba23315d73b5aea4e2fb1d.jpg)

![](images/c9b280e825dab4863ec35d378b4c63697ff8c380cf4f0004c210550e04c371ef.jpg)

![](images/6dbf6007e0c9cb059d8f08802a31d986d1c47ced5c99dfe9b23732b7d2905eb3.jpg)  
Figure 10.  $xSM$ : the top left panel shows the speed of sound calculated in the symmetric and broken phase using eq. (2.47) at the different levels of diligence. The gray dashed line corresponds to the bag model with  $c_s^2 = 1/3$ . The symmetric phase (solid magenta) is only shown at highest diligence. The top right panel shows the strength of the phase transition at the different levels of diligence using eq. [(2.5), (2.12), (2.49)]. The bottom panel shows the kinetic energy fraction at the different levels of diligence where the lowest and modest diligence use fits for  $\kappa$  to get  $K$  and the highest diligence uses eq. (2.55). The temperatures are set to  $T_n$  (2.4),  $T_p$  (2.11), and  $T_f$  (2.27) for the lowest, modest, and highest diligence respectively. The numerical calculation of the speed of sound only enters in the highest diligence of  $\alpha$ .

strength of the phase transition as seen in the top right panel of figure 10. The strength of the phase transition in the highest diligence grows larger compared to the other levels as the singlet gets heavier. This is directly related to the suppression in the speed of sound in the broken phase. There is a minor difference in the lower singlet mass range. The kinetic energy fraction is shown in the bottom panel of figure 10. The lowest and modest diligence both overestimate  $K$  for the entire range of the parameter space which is not observed in  $\alpha$ . This can be attributed to the approximations used in the kinetic energy fraction pre-factor  $\alpha / (1 + \alpha)$  used in the peak gravitational wave energy density in eq. (2.7) and the speed of sound dependence in solving the beyond the bag model hydrodynamic equations.

The inverse time duration of the phase transition is plotted in figure 11 for the different levels of diligence. The modest diligence is a better approximation than that of the first level for  $\beta / H$  but slightly under-approximates the spectrum for lower mass ranges. The lowest diligence is a poor approximation for  $\beta / H$  for the entire parameter space.

The error in the gravitational wave spectrum compared to the highest diligence for deflagration and detonation is given in figure 12. The largest error in the spectrum occurs

![](images/d1bc422ffe1a2991f0417649ce09da730bd872e890529348cd7a0c41d013cc7e.jpg)  
Figure 11.  $xSM$ : the inverse time duration of the phase transition at the different levels of diligence using eq. [(2.6), (2.13), (2.37)]. The lowest and modest diligences are estimated using the first derivative of the action  $dS / dT$  and the highest diligence is computed directly from the mean bubble separation. The temperatures are set to  $T_{n}$  (2.4),  $T_{p}$  (2.11), and  $T_{f}$  (2.27) for the lowest, modest, and highest diligence respectively.

for the lowest diligence and this is due to the lack of suppression factor for the finite lifetime of the source and the larger uncertainty in  $\beta / H$ . The suppression factor for the modest diligence case is an under-approximation to the finite lifetime of the source particularly in the higher singlet mass regions. Both the lowest and modest diligence receive significant errors from neglecting the beyond the bag contributions to the kinetic energy which over estimates the peak spectrum which also gets worse for higher singlet masses. Overall the range of error in the peak gravitational wave energy density is between  $[10^2 \sim 10^3]$  and  $[10^0 \sim 10^2]$  for the different levels of diligence. All of the points above the range in  $m_{h_2}$  shown are certainly viable points and may even reach higher levels of error. However, this range in  $m_{h_2}$  is chosen such that all the points remain in either deflagration or detonation for both consistency and the lack of numerical simulations for hybrids.

# 4.4 Mean bubble separation vs inverse time duration

The gravitational wave energy density is dependent on determining the mean bubble separation when the phase transition ends at temperature  $T_{f}$ . An approximation to the mean bubble separation can be determined by calculating the inverse time duration,  $\beta / H$ , from the first derivative of the action. This calculation is typically only valid when there is a negligible barrier at zero temperature. However, if there is a barrier at tree level, a minimum in the action will develop near  $T_{f}$  and the second derivative,  $\beta_{2}$  will become relevant while the first derivative will vanish. The bubble nucleation rate can then take on the form

$$
p = p _ {0} \exp \left[ - S _ {*} - \frac {1}{2} \beta_ {2} ^ {2} \left(t - t _ {*}\right) ^ {2} \right], \tag {4.2}
$$

where  $t_*$  is the time when the temperature is near  $T_f$  and  $S_* = S_3(T_*) / T_*$ . The above result will ultimately lead to a new relation between the mean bubble separation  $R_*$  and the inverse time duration of the phase transition  $\beta$ .

![](images/3ae70c7bf20e8c446ce67b88fe38a149765070cef42941c6620f433ffc7f70d1.jpg)  
Figure 12. Dark  $RG$ : the relative error when using the lowest and modest levels of diligence, compared to the highest level of diligence (for which  $\Delta \Omega / \Omega = 0$ ). The vertical axis shows the peak (frequency-independent) gravitational wave energy density for detonation. The precise definition of  $\Delta \Omega / \Omega$  is given in eq. (4.1). The horizontal axis corresponds to the heavy singlet mass  $m_{h_2}$ .  $\Delta \Omega / \Omega$  is displayed for deflagration and detonation at different levels of diligence using eq. [(2.7), (2.15), (2.61)] and eq. (4.1). The temperatures are set to  $T_n$  (2.4),  $T_p$  (2.11), and  $T_f$  (2.27) for the lowest, modest, and highest diligence respectively. Both the modest and highest diligence contains suppression factors due to the lifetime of the source. The highest diligence contains the suppression factor due to vorticity effects in the plasma.

![](images/43eb312395f28ffe555c58f540b4a55d766717152f2e9e6a373e902b3bb50b88.jpg)

This subtlety is not usually taken into account and the relation between  $R_{*}$  and  $\beta$  that is useful for gravitational wave calculations is simply given by the approximate formula

$$
H R _ {*} = (8 \pi) ^ {1 / 3} v _ {w} \left(\frac {H _ {*}}{\beta}\right), \text {w i t h} \quad \beta = H T d S / d T, \tag {4.3}
$$

where  $\beta$  is related to the first derivative of the action regardless of the presence of a barrier. Out of the models we consider, SMEFT and xSM can acquire tree level barriers that result in a minimum in the action. The lowest and modest diligence results presented here assume eq. (4.3) always hold which can result in significant errors for these two models. Furthermore, the percolation temperature at which  $\beta / H$  is estimated is a function of  $\beta / H$ , eq. (2.13), which can also acquire error if the barrier is not sufficiently taken care of. The highest diligence results can side-step these issues by numerically calculating the mean bubble separation from the number bubble density which is independent of any assumptions about the curvature of the action, i.e

$$
H R _ {*} = \left(\frac {n _ {b}}{H ^ {3}}\right) ^ {- 1 / 3}, \tag {4.4}
$$

evaluated at the final temperature  $T_{f}$ . The final temperature as well does not depend on any underlying assumptions about the curvature of the action because it is numerically calculated from the false vacuum fraction. For comparisons between the inverse time durations with respect to the highest diligence, we first calculate  $HR_{*}$  and use eq. (4.3) to determine an effective  $\beta / H$ .

The comparison between  $HR_{*}$  using eq. (4.3) and eq. (4.4) is shown in figure 13 where the left figure corresponds to SMEFT and right figure corresponds to xSM. The solid lines

![](images/474fcaa4b4455e856d8f36d82f4e858134f217b24b680e6639eeb2696422052e.jpg)  
Figure 13. The mean bubble separation times the Hubble parameter for SMEFT (left) and xSM (right). The solid line corresponds to the numerically calculated value defined in eq. (4.4) evaluated at  $T_{f}$  (2.27). The dashed and dotted lines correspond to the estimated value using eq. (4.3) evaluated at  $T_{f}$  (2.27) and  $T_{p}$  (2.11) respectively.

![](images/6bde08b380249c811c94a3d96be7082c70107766226de4bbc6313d8447853442.jpg)

represent the proper mean bubble separation calculated at  $T_{f}$ . The dotted and dashed lines correspond to the mean bubble separation calculated first from  $\beta$  at  $T_{f}$  and  $T_{p}$  respectively. We denote  $T_{p}$  to refer to the estimation given in eq. (2.11). Below  $M = 600\mathrm{GeV}$  in SMEFT, the action acquires a minimum as a result of the tree level barrier at zero temperature which causes  $\beta (T_{p})$  to significantly over-approximate  $HR_{*}$ . As mentioned previously, this is a result of the underlying assumptions in approximating both  $T_{p}$  and  $\beta$  which ignore the barrier. The mean bubble separation calculated from  $\beta (T_{f})$  performs better than  $\beta (T_{p})$  in this regime with nearly identical  $HR_{*}$  predictions compared to  $n_b^{-1 / 3}$ . This is largely due to  $T_{f}$  being independent of any assumptions on the action.

The xSM model consists of a second scalar and several parameters which when varied may induce either first step or second step phase transitions. The bench marks chosen involve scanning of the heavy singlet mass while holding the other model parameters fixed. All of the points resulted in a one step phase transition along with no minimum in the action. On the right of figure 13, we see that all three methods resulted in a roughly consistent approximation of  $HR_{*}$  with slightly better performance from  $\beta (T_{p})$  for large  $m_{h_2}$ . This can be attributed to the lack of minimum in the action observed in the parameter space. We reserve a further analysis of the mean bubble separation in xSM for future work.

# 5 Summary of results

The previous results involved fixing certain characteristics associated with each of the outlined levels of diligence. In this section, we will fix all of the quantities as high diligence while varying the level of a single quantity to determine its impact on the error of  $\Delta \Omega / \Omega$ . Table 1 shows the range of error we observe associated with varying the level of diligence in the calculation of the transition temperature, mean bubble separation, fluid velocity, finite lifetime of the source, and vorticity effects. The base level of comparison will use  $\Omega_{\mathrm{GW}}$  calculated using eq. (2.61) which assumes the transition temperature is at  $T_f$  and includes beyond the bag effects and the suppression factors due to the finite lifetime of the

Table 1. Full range of error of  $\Delta \Omega /\Omega$  for each individual effect comparing the medium diligence and low diligence approaches to the high diligence approach.  

<table><tr><td>Effect</td><td>Range of error (medium)</td><td>Range of error (low)</td><td>Type of error</td></tr><tr><td>Transition temperature</td><td>O(10-4-101)</td><td>O(10-1-100)</td><td>Random</td></tr><tr><td>Mean bubble separation</td><td>O(0-10-1)</td><td>O(10-1-100)</td><td>Suppression</td></tr><tr><td>Fluid velocity</td><td>O(10-2-100)</td><td>O(10-2-100)</td><td>Random</td></tr><tr><td>Finite lifetime</td><td>O(10-3-10-1)</td><td>O(101-103)</td><td>Enhancement</td></tr><tr><td>Vorticity effects</td><td>O(10-1-100)</td><td>-</td><td>Random</td></tr></table>

source and reheating effects in the plasma. We will now proceed to describe how the range of errors are calculated.

The transition temperatures used for the different levels were  $T_{n}$  (2.4) and  $T_{p}$  ((2.11). The frequency independent  $\Omega_{\mathrm{GW}}$  is now calculated at high diligence using eq. (2.61) for both the lowest and modest diligence. This is to show how  $\Omega_{\mathrm{GW}}$  can change purely by the temperature at which the transition is assumed to take place. The lowest diligence will use  $T_{n}$  to calculate  $\Delta \Omega /\Omega$  while the modest diligence will use  $T_{p}$ . The base level comparison is  $\Omega_{\mathrm{GW}}$  at  $T_{f}$  which corresponds to the previously defined high diligence. Varying the transition temperature leads to an error of  $(10^{-1} - 10^{0})$  and  $(10^{-4} - 10^{1})$  for lowest and modest diligence respectively. The modest diligence can experience a larger error than the lowest diligence and this is due to the result of the strong super-cooling observed in SMEFT when  $M\simeq 600$ . The approximations used in calculating  $T_{p}$  break down when a minimum develops in the action and results in the  $10^{1}$  peak in the error for modest diligence. The error in the lowest diligence results in an enhancement in the spectrum which is attributed to  $T_{n} > T_{f}$ . The modest diligence experienced both enhancement and suppression which is due to  $T_{p}$  being much closer to  $T_{f}$ . The lowest diligence primarily had  $\Omega_{\mathrm{GW}}^{\mathrm{low}} < \Omega_{\mathrm{GW}}^{\mathrm{high}}$  and modest diligence had  $\Omega_{\mathrm{GW}}^{\mathrm{med}} > \Omega_{\mathrm{GW}}^{\mathrm{high}}$ . For these reasons, we conclude that the type of error due to the transition temperature is random and dependent on the underlying model.

The estimation of the error due to the mean bubble separation will involve calculating  $R_{*}H$  from the  $\beta / H$  at  $T_{n}$  for the lowest diligence and  $R_{*}H$  from  $n_{b}$  at  $T_{f}$  for modest diligence. We use  $T_{f}$  for the modest diligence in determining the relevant quantities in  $\Omega_{\mathrm{GW}}$  in this case to minimize error which may arise from using the  $T_{p}$  approximation. All quantities in  $\Omega_{\mathrm{GW}}$  are calculated in high diligence at  $T_{n}$  and  $T_{f}$  for lowest and modest diligence respectively. The lowest diligence exhibits the largest error with a range of  $(10^{-1} - 10^{0})$  while modest diligence has the range  $(10^{-3} - 10^{-1})$ . The error in modest diligence observed in the table is only due to the approximation of the mean bubble separation from the inverse time duration but it is expected to be higher if  $T_{p}$  is used as opposed to  $T_{f}$  which helps to correct the error. Both the lowest and modest diligence had mostly  $\Omega_{\mathrm{GW}}^{\mathrm{low,med}} < \Omega_{\mathrm{GW}}^{\mathrm{high}}$  with modest diligence having a couple benchmarks with  $\Omega_{\mathrm{GW}}^{\mathrm{med}} > \Omega_{\mathrm{GW}}^{\mathrm{high}}$ . We denote this type of error as predominately suppression.

The error estimate from the fluid velocity involves comparing the fits for kappa given in appendix A to solving the hydrodynamic profiles numerically. The fluid velocity is

related to the kappa through the kinetic energy fraction  $K$  in eq. (2.10), (2.55), (2.57). The lowest diligence calculates  $\Omega_{\mathrm{GW}}$  at  $T_{f}$  in the highest diligence with the replacement that  $K$  and  $U_{f}$  are now calculated using the fits to  $\kappa$  and the bag calculation for  $\alpha$ . The modest diligence is the same as the lowest diligence except that  $\kappa$  is calculated using the hydrodynamic profiles with  $c_{s}^{2} = 1/3$  in the bag model. The error associated with the different treatments of the fluid velocity is  $(10^{-2} - 10^{0})$  for lowest diligence and  $(10^{-3} - 10^{0})$  for modest diligence. This represents the amount of error that one might expect in these models when performing precise calculations of  $\Omega_{\mathrm{GW}}$  but without taking into consideration the beyond the bag treatment of the speed of sound in the plasma. The type of error we observe for the fluid velocity is random.

To determine the impact of the suppression factor due to the finite lifetime of the source has on the error, we compare  $\Omega_{\mathrm{GW}}$  calculated in eq. (2.61) with out  $\Upsilon$  for the lowest diligence and with the replacement  $\Upsilon \rightarrow \tau_{\mathrm{SW}}H$  corresponding to eq. (2.14) for the modest diligence. All quantities are evaluated at  $T_{f}$ . Modest diligence will also contain the suppression to  $U_{f}$  due to vorticity and reheating effects in the plasma. Note that this suppression is less dramatic than what one might naively expect from ref. [106], as the suppression in the fluid velocity results in a longer lifetime for the soundwaves. For the range of models we consider, the error for modest diligence is in the range  $(10^{-3} - 10^{-1})$  and represents the validity of the approximation used in  $\Upsilon$ . The error in the lowest diligence experiences the highest error with a range of  $(10^{1} - 10^{3})$ . For all of the models,  $\Omega_{\mathrm{GW}}^{\mathrm{low,med}} > \Omega_{\mathrm{GW}}^{\mathrm{high}}$ . This type of error is an enhancement.

The last row in table 1 corresponds to the error in  $\Omega_{\mathrm{GW}}$  calculated using eq. (2.61) without suppression factors arising from vorticity and reheating effects in the plasma. This is compared to the full suppression in highest diligence which uses  $U_{f,\max}$  in the lifetime of the source as well. The range of error we observe is in the range of  $10^{-1} - 10^{1}$ . Neglecting  $U_{f,\max}$  in the suppression factor will contribute at most an error of 0.62. The lowest diligence experienced  $\Omega_{\mathrm{GW}}^{\mathrm{low}} < \Omega_{\mathrm{GW}}^{\mathrm{high}}$  for the all of the models. The modest diligence experienced mostly random error. The primary focus should be on modest diligence so we denote this type of error as random.

# 6 Conclusion

In this work we have examined the cost of various short-cuts and approximations used in the literature when predicting the gravitational wave spectrum generated by a cosmological first order phase transition. Even in the case where some modest diligence has been used in the calculation, we found the cost to often be comparable to problems in finite temperature QFT such as the scale dependence that arises from the break down of perturbation theory as well as the gauge dependence. Assuming detonations, the dominant cost in cases where there is a fair amount of super-cooling is from poor estimates of the percolation temperature in eq. (2.11). The poor estimate of the percolation temperature has a knock on effect in enhancing the errors that arise from using the bag model and an estimate for the suppression factor. In the case where there is no tree-level barrier delaying the nucleation of the phase transition, the dominant error is due to the bag model approximation.

Although the errors are often as large as finite temperature QFT errors, they are arguably easier to reduce. At present, all of these errors can be handled except for the reheating and vorticity effects where we had to rely on interpolations. High diligence calculations for multiple models were considerably more tractable than the two loop calculations required to bring scale dependence at finite temperature under control [93]. We recommend future phenomenological calculations of gravitational wave signals from primordial phase transitions at the very least take the level of theoretical uncertainties into consideration.

# Acknowledgments

HG and KS are supported by DOE Grant desc0009956. GW was supported by World Premier International Research Center Initiative (WPI), MEXT, Japan.

# A Kinetic energy efficiency coefficient

The kinetic energy efficiency coefficient may be solved by integrating over the enthalpy and velocity profiles around a single bubble,

$$
\kappa = \frac {3}{\epsilon v _ {w} ^ {3}} \int_ {0} ^ {\xi_ {\max }} d \xi \xi^ {2} \omega \gamma^ {2} v ^ {2}, \tag {A.1}
$$

where  $\epsilon$  is the bag constant and  $\xi = r / t$  is a self-similar coordinate in terms of the distance form the bubble center  $r$  and the time since nucleation  $t$ . The fits to  $\kappa$  are provided in [110] and are valid in the range  $10^{-3} < \alpha < 10$  to a precision of  $10\%$ . The fits are found by splitting the parameter space of  $v_{w}$  into three regions and four boundary conditions. The boundary conditions are

$$
\kappa_ {A} \simeq v _ {w} ^ {6 / 5} \frac {6 . 9 \alpha}{1 . 3 6 - 0 . 0 3 7 \sqrt {\alpha} + \alpha}, \quad \text {f o r} v _ {w} \ll c _ {s}, \tag {A.2}
$$

$$
\kappa_ {B} \simeq \frac {\alpha^ {2 / 5}}{0 . 0 1 7 + (0 . 9 9 7 + \alpha) ^ {2 / 5}}, \quad \text {f o r} v _ {w} = c _ {s}, \tag {A.3}
$$

$$
\kappa_ {C} \simeq \frac {\sqrt {\alpha}}{0 . 1 3 5 + \sqrt {0 . 9 8} + \alpha}, \quad \text {f o r} v _ {w} = v _ {J} = \frac {\sqrt {\frac {2}{3} \alpha + \alpha^ {2}} + \sqrt {1 / 3}}{1 + \alpha}, \tag {A.4}
$$

$$
\kappa_ {D} \simeq \frac {\alpha}{0 . 7 3 + 0 . 0 8 3 \sqrt {\alpha} + \alpha}, \quad \text {f o r} v _ {w} \rightarrow 1, \tag {A.5}
$$

where  $v_{J}$  is the Jouguet velocity and  $c_{s}$  is the speed of sound. Subsonic deflagrations in the region  $v_{w} \lesssim c_{s}$  have a kinetic energy coefficient approximated by

$$
\kappa \simeq \frac {c _ {s} ^ {1 1 / 5} \kappa_ {A} \kappa_ {B}}{\left(c _ {s} ^ {1 1 / 5} - v _ {w} ^ {1 1 / 5}\right) \kappa_ {B} + v _ {w} c _ {s} ^ {6 / 5} \kappa_ {A}}, \tag {A.6}
$$

and detonations in the region  $v_{w} > v_{J}$  by

$$
\kappa \simeq \frac {\left(v _ {J} - 1\right) ^ {3} v _ {J} ^ {5 / 2} v _ {w} ^ {- 5 / 2} \kappa_ {C} \kappa_ {D}}{\left[ \left(v _ {J} - 1\right) ^ {3} - \left(v _ {w} - 1\right) ^ {3} \right] v _ {J} ^ {5 / 2} \kappa_ {C} + \left(v _ {w} - 1\right) ^ {3} \kappa_ {D}}, \tag {A.7}
$$

Supersonic deflagrations, hybrid, in the region  $c_{s} \lesssim v_{w} \lesssim v_{J}$  can be approximated by

$$
\kappa \simeq \kappa_ {B} + \left(v _ {w} - c _ {s}\right) \delta \kappa + \frac {\left(v _ {w} - c _ {s}\right) ^ {3}}{\left(v _ {J} - c _ {s}\right)} \left[ \kappa_ {C} - \kappa_ {B} - \left(v _ {J} - c _ {s}\right) \delta \kappa \right], \tag {A.8}
$$

where

$$
\delta \kappa \simeq - 0. 9 \log \frac {\sqrt {\alpha}}{1 + \sqrt {\alpha}}. \tag {A.9}
$$

# B Toy model

# B.1 Toy effective potential

A general free energy density of a single scalar field,  $\phi$ , under a high temperature expansion can be written in the form

$$
f (\phi , T) = D \left(T ^ {2} - T _ {0} ^ {2}\right) \phi^ {2} - E T \phi^ {3} + \frac {1}{4} \lambda \phi^ {4} + \Delta V - \frac {1}{3} a T ^ {4}, \tag {B.1}
$$

where  $\Delta V$  is added to the potential to cancel out the zero temperature minimum such that  $f(\phi_{\mathrm{min}},0) = 0$ . The Standard Model effective potential was considered in ref. [125]. We require  $D > 0$ ,  $E > 0$ ,  $\lambda > 0$  to ensure symmetry is broken at low temperature and generate a barrier between the symmetric and broken phase. The vacuum terms are not necessary for determining the phase transition structure of the model, however, they are necessary for determining the temperature dependence of the speed of sound.

The structure of the potential along with the constraints on the parameters allows for simple analytical forms for the minima as a function of temperature. The minimum is found by minimizing eq. (B.1) with respect to the scalar field which results in

$$
\phi_ {\min } = \frac {3 E T \pm \sqrt {9 E ^ {2} T ^ {2} - 8 D \lambda (T _ {0} ^ {2} - T ^ {2})}}{2 \lambda}, \tag {B.2}
$$

where the  $+^{\prime}$  sign gives the local minimum. When  $T$  is large, the global minimum will sit at the origin with  $\phi_{\mathrm{min}} = 0$ . As  $T$  decreases, a second minimum will develop at

$$
T = \sqrt {\frac {T _ {0} ^ {2}}{1 - \frac {9}{8} \frac {E ^ {2}}{\lambda D}}}. \tag {B.3}
$$

This minimum will eventually become degenerate with minimum at the origin at the critical temperature when

$$
T _ {C} = \sqrt {\frac {T _ {0} ^ {2}}{1 - \frac {E ^ {2}}{\lambda D}}}. \tag {B.4}
$$

The Euclidean action of a bounce configuration,  $S_{3}$ , will start from infinity at  $T = T_{c}$  and decrease with temperature. There is an analytical form for the action given by

$$
\frac {S _ {3} (T)}{T} = \frac {M ^ {3}}{4 E ^ {2} T ^ {3}} \tilde {S} _ {3} (\sigma), \tag {B.5}
$$

$$
\tilde {S} _ {3} (\sigma) = 4 \times 4. 8 5 \times \left[ 1 + \frac {\sigma}{4} \left(1 + \frac {2 . 4}{1 - \sigma} + \frac {0 . 2 6}{(1 - \sigma) ^ {2}}\right) \right], \tag {B.6}
$$

where  $\sigma = \lambda M^2 /(2E^2 T^2)$  controls the overall shape of the potential [125]. The critical temperature and the action are necessary to determine the dynamics of the phase transition and calculate the relevant transition temperatures such as  $T_{n},T_{p}$ , and  $T_{f}$  and the mean bubble separation  $R_{*}(v_{w},\beta)$ .

The hydrodynamics of the phase transition are determined by the pressure and energy density in the symmetric and broken phase where  $p_{s} = -f(0,T)$  and  $p_{b} = -f(\phi_{\mathrm{min}},T)$ . The energy density can be computed from the transformation of pressure

$$
e = T \frac {\partial p}{\partial T} - p, \tag {B.7}
$$

which can be evaluated in both the symmetric and the broken phase. From eq. (B.1), the pressure in the symmetric and broken phases are

$$
p _ {s} = - f (0, T) = \frac {1}{3} a T ^ {4} - \Delta V, \tag {B.8}
$$

$$
p _ {b} = - f \left(\Phi_ {\min }, T\right), \tag {B.9}
$$

where the pressure in the broken phase has additional dependence on temperature arising from  $\phi_{\mathrm{min}}$ . The speed of sound may be found from the pressure using eq. (2.47) in both the symmetric and broken phase. The temperature dependence from the minimum of the scalar field will result in a speed sound that is function of the model parameters and its form will depend on the overall shape of the potential.

# B.2 Results for toy model

Here we show the different levels of diligence in calculating the thermal parameters and the gravitation wave spectrum in the toy model. The analysis involves individual scans over the different model parameters  $(E, D, \lambda, T_0)$  while holding the others fixed. A full analysis of the toy model should involve a randomized scan over all of the parameters but we perform the scan this way in hopes to see any trends in varying the different model parameters. In eq. (B.4), the critical temperature is a function of all four model parameters. For this reason,  $T_C$  will be used as a basis for each scan. The first step in the beyond the bag calculations is to compute the speed of sound in the symmetric and broken phase. For the toy model, we only consider detonation,  $v_w = 0.92$ , where the speed of sound in the symmetric phase is set to  $c_s^2 = 1/3$  and the degrees of freedom consist of only the standard model sector. The speed of sound in the broken phase may be found through eq. (2.47). The transition temperatures for the different levels of diligence are  $T_n$  (2.4),  $T_p$  (2.11), and  $T_f$  (2.27). Example calculations for various phase transition quantities used in the high diligence calculations such as the false vacuum fraction, mean bubble separation, lifetime of the source, and  $T_f$  in the toy model may be found in ref. [103].

In figure 14, we calculate the speed of sound in the broken phase for each level of diligence. The gray dashed line corresponds to  $c_s^2 = 1 / 3$ . This involves first calculating the speed of sound as a function temperature using eq. (2.47) and then evaluating it at  $(T_{n}, T_{p}, T_{f})$  computed in the different levels of diligence. We note that in computing the strength of the phase transition only the highest diligence level will involve this calculation.

![](images/4fc618e3a86eb041590f3a89b9c0c53c55ebe33f59ac7da76d30aede27b44e17.jpg)  
Figure 14. Speed of sound computed in the different levels of diligence.

This is merely to show the level of variance in computing the speed of sound at different temperature stages. For specific values and range chosen, there is only minor change to the speed of sound computed in the different levels however how much variance is present is strongly model dependent. We do notice that the speed of sound can have a significant deviation away from  $c_s^2 = 1/3$  in the bag model. The strongest deviation is caused by varying the barrier term,  $E$ , and the quadratic multiplicity term,  $D$  as seen in the green and purple curves. The speed of sound can go as low as  $c_s^2 \sim 0.22$  and as high as  $c_s^2 \sim 0.36$ . Varying the zero temperature mass term,  $T_0$ , did not have any noticeable impact on the speed of sound while the quartic coupling term,  $\lambda$ , had a mild impact on the speed of sound. This is likely due to the temperature independence of the terms that involve  $T_0$  and  $\lambda$ . The parameters  $D$  and  $E$  on the other hand, multiply  $T^2$  and  $T$  respectively and will result in a change in the temperature dependence. The speed of sound in the broken phase is related to the temperature derivatives of the pressure which is evaluated at  $p_b(T) = V_{\mathrm{eff}}(\phi_{\mathrm{min}}(T), T)$  and hence  $D$  and  $E$  will impact the minimum at finite temperature. The smallest speed of sound in the broken phase corresponds to small  $E$  and large  $D$ .

We show in figure 15 the phase transition strength computed in the different level of diligence (left) and the comparison between  $\alpha_{\theta}$  computed in the bag model versus  $\alpha_{\bar{\theta}}$  computed in the beyond the bag model at  $T_{f}$  for both quantities (right). We see in the left figure that going higher in the level of diligence results in an increase in the phase transition strength compared to lowest diligence. This can be attributed to more vacuum energy being released at  $T_{p}$  compared to  $T_{n}$ . On the right, to better compare the difference between the bag model and the beyond the bag model, we compute the ratio of  $\alpha_{\theta}$  and  $\alpha_{\bar{\theta}}$  computed at the same temperature,  $T_{f}$ . For  $T_{c} < 100$ ,  $\alpha_{\theta}$  is less than  $\alpha_{\bar{\theta}}$  which is the result of  $c_{s}^{2} < 1/3$  as seen in figure 14. This has to do with the  $(1 + c_{s}^{-2})$  factor in  $\alpha_{\bar{\theta}}$ . When  $T_{c} > 100$ , we see that the opposite is true when  $c_{s}^{2} > 1/3$ . Similarly, the largest deviations are due to the parameters  $D$  and  $E$ .

![](images/30da4c8b3b89898f7ae133cc467d10e8ff66b10fef8462bd3173e6b398f6ce49.jpg)  
Figure 15. Left: the strength of phase transition computed at the different levels of diligence. Right: the ratio of strength of the phase transition computed at  $T_{f}$  for the bag model  $\alpha_{\theta}$  and the beyond the bag model  $\alpha_{\bar{\theta}}$ .

![](images/7c74d23e4e553eb5ab2e7915e82a94f90c61223792fa980dea28449b7c2b1b8e.jpg)

![](images/e4eebfc022ecbbc619a231aa3ec8af62fbe85dd805014075c4719eb6d8c770ff.jpg)  
Figure 16. Error of the gravitational spectrum computed at the different levels of diligence.

The error in the gravitational wave spectrum of the toy model for different scans in the model parameters is shown in the left of figure 16. The lowest and modest diligence peak gravitational wave energy density  $\Omega_{GW}$  is calculated using eq. (2.7) and eq. (2.15) respectively. The comparison in error is computed with respect to the highest diligence in eq. (2.61). The lowest diligence level has error in the range  $\Delta \Omega / \Omega \sim [10^{1}, 10^{3}]$  for all parameter scans. The modest diligence level is closest to the highest diligence with error in the range  $\Delta \Omega / \Omega \sim [10^{0}, 10^{1}]$  for the different scans. The highest error occurs for  $T_{C} \sim 100$ . This is related to beyond the bag effects which exhibited suppression for the scans in  $(E, D)$ .

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] D.J. Weir, Gravitational waves from a first order electroweak phase transition: a brief review, Phil. Trans. Roy. Soc. Lond. A 376 (2018) 20170126 [arXiv:1705.01783] [INSPIRE].  
[2] A. Mazumdar and G. White, Review of cosmic phase transitions: their significance and experimental signatures, Rept. Prog. Phys. 82 (2019) 076901 [arXiv:1811.01948] [INSPIRE].  
[3] C. Caprini et al., Detecting gravitational waves from cosmological phase transitions with LISA: an update, JCAP 03 (2020) 024 [arXiv:1910.13125] [INSPIRE].  
[4] K. Kajantie, M. Laine, K. Rummukainen and M.E. Shaposhnikov, The Electroweak phase transition: A Nonperturbative analysis, Nucl. Phys. B 466 (1996) 189 [hep-lat/9510020] [INSPIRE].  
[5] K. Kajantie, M. Laine, K. Rummukainen and M.E. Shaposhnikov, Is there a hot electroweak phase transition at  $m(H) \gtrsim m(W)$ ?, Phys. Rev. Lett. 77 (1996) 2887 [hep-ph/9605288] [INSPIRE].  
[6] K. Kajantie, M. Laine, K. Rummukainen and M.E. Shaposhnikov, A Nonperturbative analysis of the finite  $T$  phase transition in  $\mathrm{SU}(2) \times \mathrm{U}(1)$  electroweak theory, Nucl. Phys. B 493 (1997) 413 [hep-lat/9612006] [INSPIRE].  
[7] F. Csikor, Z. Fodor and J. Heitger, Endpoint of the hot electroweak phase transition, Phys. Rev. Lett. 82 (1999) 21 [hep-ph/9809291] [INSPIRE].  
[8] A. Bazavov et al., The chiral and deconfinement aspects of the QCD transition, Phys. Rev. D 85 (2012) 054503 [arXiv:1111.1710] [INSPIRE].  
[9] S. Gupta, X. Luo, B. Mohanty, H.G. Ritter and N. Xu, Scale for the Phase Diagram of Quantum Chromodynamics, Science 332 (2011) 1525 [arXiv:1105.3934] [INSPIRE].  
[10] C. Grojean, G. Servant and J.D. Wells, First-order electroweak phase transition in the standard model with a low cutoff, Phys. Rev. D 71 (2005) 036001 [hep-ph/0407019] [INSPIRE].  
[11] C. Grojean and G. Servant, Gravitational Waves from Phase Transitions at the Electroweak Scale and Beyond, Phys. Rev. D 75 (2007) 043507 [hep-ph/0607107] [INSPIRE].  
[12] C. Delaunay, C. Grojean and J.D. Wells, Dynamics of Non-renormalizable Electroweak Symmetry Breaking, JHEP 04 (2008) 029 [arXiv:0711.2511] [INSPIRE].  
[13] J.M. Cline, G. Laporte, H. Yamashita and S. Kraml, Electroweak Phase Transition and LHC Signatures in the Singlet Majoron Model, JHEP 07 (2009) 040 [arXiv:0905.2559] [INSPIRE].  
[14] M. Carena, N.R. Shah and C.E.M. Wagner, Light Dark Matter and the Electroweak Phase Transition in the NMSSM, Phys. Rev. D 85 (2012) 036003 [arXiv:1110.4378] [INSPIRE].  
[15] G. Gil, P. Chankowski and M. Krawczyk, Inert Dark Matter and Strong Electroweak Phase Transition, Phys. Lett. B 717 (2012) 396 [arXiv:1207.0084] [INSPIRE].  
[16] M. Carena, G. Nardini, M. Quiros and C.E.M. Wagner, MSSM Electroweak Baryogenesis and LHC Data, JHEP 02 (2013) 001 [arXiv:1207.6330] [INSPIRE].  
[17] M. Fairbairn and R. Hogan, Singlet Fermionic Dark Matter and the Electroweak Phase Transition, JHEP 09 (2013) 022 [arXiv:1305.3452] [INSPIRE].

[18] S. Profumo, M.J. Ramsey-Musolf, C.L. Wainwright and P. Winslow, Singlet-catalyzed electroweak phase transitions and precision Higgs boson studies, Phys. Rev. D 91 (2015) 035018 [arXiv:1407.5342] [INSPIRE].  
[19] J. Kozaczuk, S. Profumo, L.S. Haskins and C.L. Wainwright, Cosmological Phase Transitions and their Properties in the NMSSM, JHEP 01 (2015) 144 [arXiv:1407.4134] [INSPIRE].  
[20] V. Vaskonen, Electroweak baryogenesis and gravitational waves from a real scalar singlet, Phys. Rev. D 95 (2017) 123515 [arXiv:1611.02073] [INSPIRE].  
[21] I. Baldes, T. Konstandin and G. Servant, A first-order electroweak phase transition from varying Yukawas, Phys. Lett. B 786 (2018) 373 [arXiv:1604.04526] [INSPIRE].  
[22] G.C. Dorsch, S.J. Huber, T. Konstandin and J.M. No, A Second Higgs Doublet in the Early Universe: Baryogenesis and Gravitational Waves, JCAP 05 (2017) 052 [arXiv:1611.05874] [INSPIRE].  
[23] C.-W. Chiang, M.J. Ramsey-Musolf and E. Senaha, Standard Model with a Complex Scalar Singlet: Cosmological Implications and Theoretical Considerations, Phys. Rev. D 97 (2018) 015005 [arXiv:1707.09960] [INSPIRE].  
[24] Q.-H. Cao, F.P. Huang, K.-P. Xie and X. Zhang, Testing the electroweak phase transition in scalar extension models at lepton colliders, Chin. Phys. C 42 (2018) 023103 [arXiv:1708.04737] [INSPIRE].  
[25] B. von Harling and G. Servant, QCD-induced Electroweak Phase Transition, JHEP 01 (2018) 159 [arXiv:1711.11554] [INSPIRE].  
[26] L. Bian, H.-K. Guo and J. Shu, Gravitational Waves, baryon asymmetry of the universe and electric dipole moment in the CP-violating NMSSM, Chin. Phys. C 42 (2018) 093106 [Erratum ibid. 43 (2019) 129101] [arXiv:1704.02488] [INSPIRE].  
[27] M. Chala, C. Krause and G. Nardini, Signals of the electroweak phase transition at colliders and gravitational wave observatories, JHEP 07 (2018) 062 [arXiv:1802.02168] [INSPIRE].  
[28] A. Alves, T. Ghosh, H.-K. Guo, K. Sinha and D. Vagie, *Collision and Gravitational Wave Complementarity in Exploring the Singlet Extension of the Standard Model*, JHEP 04 (2019) 052 [arXiv:1812.09333] [INSPIRE].  
[29] A. Angelescu and P. Huang, Multistep Strongly First Order Phase Transitions from New Fermions at the TeV Scale, Phys. Rev. D 99 (2019) 055023 [arXiv:1812.08293] [INSPIRE].  
[30] A. Beniwal, M. Lewicki, M. White and A.G. Williams, Gravitational waves and electroweak baryogenesis in a global study of the extended scalar singlet model, JHEP 02 (2019) 183 [arXiv:1810.02380] [INSPIRE].  
[31] S. Bruggisser, B. Von Harling, O. Matsedonskyi and G. Servant, Electroweak Phase Transition and Baryogenesis in Composite Higgs Models, JHEP 12 (2018) 099 [arXiv:1804.07314] [INSPIRE].  
[32] P. Athron, C. Balázs, A. Fowlie, G. Pozzo, G. White and Y. Zhang, *Strong first-order phase transitions in the NMSSM - a comprehensive survey*, JHEP **11** (2019) 151 [arXiv:1908.11847] [INSPIRE].  
[33] K. Kainulainen, V. Keus, L. Niemi, K. Rummukainen, T.V.I. Tenkanen and V. Vaskonen, On the validity of perturbative studies of the electroweak phase transition in the Two Higgs Doublet model, JHEP 06 (2019) 075 [arXiv:1904.01329] [INSPIRE].

[34] S.A.R. Ellis, S. Ipek and G. White, Electroweak Baryogenesis from Temperature-Varying Couplings, JHEP 08 (2019) 002 [arXiv:1905.11994] [INSPIRE].  
[35] J. Ellis, M. Fairbairn, M. Lewicki, V. Vaskonen and A. Wickens, Intergalactic Magnetic Fields from First-Order Phase Transitions, JCAP 09 (2019) 019 [arXiv:1907.04315] [INSPIRE].  
[36] A. Papaefstathiou and G. White, The electro-weak phase transition at colliders: confronting theoretical uncertainties and complementary channels, JHEP 05 (2021) 099 [arXiv:2010.00597] [INSPIRE].  
[37] M. Postma and G. White, Cosmological phase transitions: is effective field theory just a toy?, JHEP 03 (2021) 280 [arXiv:2012.03953] [INSPIRE].  
[38] A. Alves, D. Gonçalves, T. Ghosh, H.-K. Guo and K. Sinha, Di-Higgs Blind Spots in Gravitational Wave Signals, Phys. Lett. B 818 (2021) 136377 [arXiv:2007.15654] [INSPIRE].  
[39] S. Baum, M. Carena, N.R. Shah, C.E.M. Wagner and Y. Wang, *Nucleation is More than Critical—A Case Study of the Electroweak Phase Transition in the NMSSM*, arXiv:2009.10743 [INSPIRE].  
[40] A. Paul, U. Mukhopadhyay and D. Majumdar, Gravitational Wave Signatures from Domain Wall and Strong First-Order Phase Transitions in a Two Complex Scalar extension of the Standard Model, JHEP 05 (2021) 223 [arXiv:2010.03439] [INSPIRE].  
[41] L. Bian, H.-K. Guo, Y. Wu and R. Zhou, Gravitational wave and collider searches for electroweak symmetry breaking patterns, Phys. Rev. D 101 (2020) 035011 [arXiv:1906.11664] [INSPIRE].  
[42] Z. Zhang, C. Cai, X.-M. Jiang, Y.-L. Tang, Z.-H. Yu and H.-H. Zhang, Phase transition gravitational waves from pseudo-Nambu-Goldstone dark matter and two Higgs doublets, JHEP 05 (2021) 160 [arXiv:2102.01588] [INSPIRE].  
[43] B. Laurent, J.M. Cline, A. Friedlander, D.-M. He, K. Kainulainen and D. Tucker-Smith, Baryogenesis and gravity waves from a UV-completed electroweak phase transition, arXiv:2102.12490 [INSPIRE].  
[44] H. Davoudiasl, LIGO/Virgo Black Holes from a First Order Quark Confinement Phase Transition, Phys. Rev. Lett. 123 (2019) 101102 [arXiv:1902.07805] [INSPIRE].  
[45] D.J. Schwarz and M. Stuke, Lepton asymmetry and the cosmic QCD transition, JCAP 11 (2009) 025 [Erratum ibid. 10 (2010) E01] [arXiv:0906.3434] [INSPIRE].  
[46] C. Caprini, R. Durrer and X. Siemens, Detection of gravitational waves from the QCD phase transition with pulsar timing arrays, Phys. Rev. D 82 (2010) 063511 [arXiv:1007.1218] [INSPIRE].  
[47] G. Barenboim and W.-I. Park, A full picture of large lepton number asymmetries of the Universe, JCAP 04 (2017) 048 [arXiv:1703.08258] [INSPIRE].  
[48] P. Schwaller, Gravitational Waves from a Dark Phase Transition, Phys. Rev. Lett. 115 (2015) 181101 [arXiv:1504.07263] [INSPIRE].  
[49] W. Chao, H.-K. Guo and J. Shu, Gravitational Wave Signals of Electroweak Phase Transition Triggered by Dark Matter, JCAP 09 (2017) 009 [arXiv:1702.02698] [INSPIRE].

[50] D. Croon, V. Sanz and G. White, Model Discrimination in Gravitational Wave spectra from Dark Phase Transitions, JHEP 08 (2018) 203 [arXiv:1806.02332] [INSPIRE].  
[51] P. Archer-Smith, D. Linthorne and D. Stolarski, Gravitational Wave Signals from Multiple Hidden Sectors, Phys. Rev. D 101 (2020) 095016 [arXiv:1910.02083] [INSPIRE].  
[52] M. Pandey and A. Paul, Gravitational Wave Emissions from First Order Phase Transitions with Two Component FIMP Dark Matter, arXiv:2003.08828 [INSPIRE].  
[53] A. Mohamadnejad, Gravitational waves from scale-invariant vector dark matter model: Probing below the neutrino-floor, Eur. Phys. J. C 80 (2020) 197 [arXiv:1907.08899] [INSPIRE].  
[54] A.J. Helmboldt, J. Kubo and S. van der Woude, Observational prospects for gravitational waves from hidden or dark chiral phase transitions, Phys. Rev. D 100 (2019) 055025 [arXiv:1904.07891] [INSPIRE].  
[55] D. Croon, R. Houtz and V. Sanz, Dynamical Axions and Gravitational Waves, JHEP 07 (2019) 146 [arXiv:1904.10967] [INSPIRE].  
[56] M. Fairbairn, E. Hardy and A. Wickens, Hearing without seeing: gravitational waves from hot and cold hidden sectors, JHEP 07 (2019) 044 [arXiv:1901.11038] [INSPIRE].  
[57] M. Breitbart, J. Kopp, E. Madge, T. Opferkuch and P. Schwaller, Dark, Cold, and Noisy: Constraining Secluded Hidden Sectors with Gravitational Waves, JCAP 07 (2019) 007 [arXiv:1811.11175] [INSPIRE].  
[58] A. Bhoonah, J. Bramante, S. Nerval and N. Song, Gravitational Waves From Dark Sectors, Oscillating Inflatons, and Mass Boosted Dark Matter, JCAP 04 (2021) 043 [arXiv:2008.12306] [INSPIRE].  
[59] E. Hall, T. Konstandin, R. McGehee and H. Murayama, Asymmetric Matters from a Dark First-Order Phase Transition, arXiv:1911.12342 [INSPIRE].  
[60] M. Li, Q.-S. Yan, Y. Zhang and Z. Zhao, Prospects of gravitational waves in the minimal left-right symmetric model, JHEP 03 (2021) 267 [arXiv:2012.13686] [INSPIRE].  
[61] T. Ghosh, H.-K. Guo, T. Han and H. Liu, Electroweak Phase Transition with an SU(2) Dark Sector, arXiv:2012.09758 [INSPIRE].  
[62] F. Huang, V. Sanz, J. Shu and X. Xue, LIGO as a probe of Dark Sectors, arXiv:2102.03155 [INSPIRE].  
[63] W.-C. Huang, M. Reichert, F. Sannino and Z.-W. Wang, Testing the Dark Confined Landscape: From Lattice to Gravitational Waves, arXiv:2012.11614 [INSPIRE].  
[64] F. Bigazzi, A. Caddeo, A.L. Cotrone and A. Paredes, Dark Holograms and Gravitational Waves, JHEP 04 (2021) 094 [arXiv:2011.08757] [INSPIRE].  
[65] A. Azatov, M. Vanvlasselaer and W. Yin, Dark Matter production from relativistic bubble walls, JHEP 03 (2021) 288 [arXiv:2101.05721] [INSPIRE].  
[66] W. Chao, W.-F. Cui, H.-K. Guo and J. Shu, Gravitational wave imprint of new symmetry breaking, Chin. Phys. C 44 (2020) 123102 [arXiv:1707.09759] [INSPIRE].  
[67] D. Croon, T.E. Gonzalo and G. White, Gravitational Waves from a Pati-Salam Phase Transition, JHEP 02 (2019) 083 [arXiv:1812.02747] [INSPIRE].  
[68] N. Haba and T. Yamada, Gravitational waves from phase transition in minimal SUSY U(1)  $B - L$  model, Phys. Rev. D 101 (2020) 075027 [arXiv:1911.01292] [INSPIRE].

[69] A. Greljo, T. Opferkuch and B.A. Stefanek, Gravitational Imprints of Flavor Hierarchies, Phys. Rev. Lett. 124 (2020) 171802 [arXiv:1910.02014] [INSPIRE].  
[70] V. Brdar, L. Graf, A.J. Helmboldt and X.-J. Xu, Gravitational Waves as a Probe of Left-Right Symmetry Breaking, JCAP 12 (2019) 027 [arXiv:1909.02018] [INSPIRE].  
[71] N. Okada, O. Seto and H. Uchida, Gravitational waves from breaking of an extra U(1) in SO(10) grand unification, PTEP 2021 (2021) 033B01 [arXiv:2006.01406] [INSPIRE].  
[72] W.-C. Huang, F. Sannino and Z.-W. Wang, Gravitational Waves from Pati-Salam Dynamics, Phys. Rev. D 102 (2020) 095025 [arXiv:2004.02332] [INSPIRE].  
[73] L. Marzola, A. Racioppi and V. Vaskonen, Phase transition and gravitational wave phenomenology of scalar conformal extensions of the Standard Model, Eur. Phys. J. C 77 (2017) 484 [arXiv:1704.01034] [INSPIRE].  
[74] J. Ellis, M. Lewicki, J.M. No and V. Vaskonen, Gravitational wave energy budget in strongly supercooled phase transitions, JCAP 06 (2019) 024 [arXiv:1903.09642] [INSPIRE].  
[75] L. Bian, W. Cheng, H.-K. Guo and Y. Zhang, Gravitational waves triggered by  $B - L$  charged hidden scalar and leptogenesis, arXiv:1907.13589 [INSPIRE].  
[76] N. Okada and O. Seto, Probing the seesaw scale with gravitational waves, Phys. Rev. D 98 (2018) 063532 [arXiv:1807.00336] [INSPIRE].  
[77] T. Hasegawa, N. Okada and O. Seto, Gravitational waves from the minimal gauged  $\mathrm{U}(1)_{B-L}$  model, Phys. Rev. D 99 (2019) 095039 [arXiv:1904.03020] [INSPIRE].  
[78] P.S.B. Dev and A. Mazumdar, Probing the Scale of New Physics by Advanced LIGO/VIRGO, Phys. Rev. D 93 (2016) 104001 [arXiv:1602.04203] [INSPIRE].  
[79] N. Aggarwal et al., *Challenges and Opportunities of Gravitational Wave Searches at MHz to GHz Frequencies*, arXiv:2011.12414 [INSPIRE].  
[80] K. Ackley et al., Neutron Star Extreme Matter Observatory: A kilohertz-band gravitational-wave detector in the global network, Publ. Astron. Soc. Austral. 37 (2020) e047 [arXiv:2007.03128] [INSPIRE].  
[81] M. Hindmarsh, S.J. Huber, K. Rummukainen and D.J. Weir, Shape of the acoustic gravitational wave power spectrum from a first order phase transition, Phys. Rev. D 96 (2017) 103520 [Erratum ibid. 101 (2020) 089902] [arXiv:1704.05871] [INSPIRE].  
[82] D. Bödeker and G.D. Moore, Electroweak Bubble Wall Speed Limit, JCAP 05 (2017) 025 [arXiv:1703.08215] [INSPIRE].  
[83] M. Hindmarsh, S.J. Huber, K. Rummukainen and D.J. Weir, Gravitational waves from the sound of a first order phase transition, Phys. Rev. Lett. 112 (2014) 041301 [arXiv:1304.2433] [INSPIRE].  
[84] M. Hindmarsh, Sound shell model for acoustic gravitational wave production at a first-order phase transition in the early Universe, Phys. Rev. Lett. 120 (2018) 071301 [arXiv:1608.04735] [INSPIRE].  
[85] M. Hindmarsh, S.J. Huber, K. Rummukainen and D.J. Weir, Numerical simulations of acoustically generated gravitational waves at a first order phase transition, Phys. Rev. D 92 (2015) 123009 [arXiv:1504.03291] [INSPIRE].  
[86] C. Caprini et al., Science with the space-based interferometer eLISA. II: Gravitational waves from cosmological phase transitions, JCAP 04 (2016) 001 [arXiv:1512.06239] [INSPIRE].

[87] T. Kahniashvili, A. Kosowsky, G. Gogoberidze and Y. Maravin, Detectability of Gravitational Waves from Phase Transitions, Phys. Rev. D 78 (2008) 043003 [arXiv:0806.0293] [INSPIRE].  
[88] T. Kahniaishvili, L. Campanelli, G. Gogoberidze, Y. Maravin and B. Ratra, Gravitational Radiation from Primordial Helical Inverse Cascade MHD Turbulence, Phys. Rev. D 78 (2008) 123006 [Erratum ibid. 79 (2009) 109901] [arXiv:0809.1899] [INSPIRE].  
[89] T. Kahniaishvili, L. Kisslinger and T. Stevens, Gravitational Radiation Generated by Magnetic Fields in Cosmological Phase Transitions, Phys. Rev. D 81 (2010) 023004 [arXiv:0905.0643] [INSPIRE].  
[90] C. Caprini, R. Durrer and G. Servant, The stochastic gravitational wave background from turbulence and magnetic fields generated by a first-order phase transition, JCAP 12 (2009) 024 [arXiv:0909.0622] [INSPIRE].  
[91] L. Kisslinger and T. Kahniaishvili, Polarized Gravitational Waves from Cosmological Phase Transitions, Phys. Rev. D 92 (2015) 043006 [arXiv:1505.03680] [INSPIRE].  
[92] A. Roper Pol, S. Mandal, A. Brandenburg, T. Kahniashvili and A. Kosowsky, Numerical simulations of gravitational waves from early-universe turbulence, Phys. Rev. D 102 (2020) 083512 [arXiv:1903.08585] [INSPIRE].  
[93] D. Croon, O. Gould, P. Schicho, T.V.I. Tenkanen and G. White, Theoretical uncertainties for cosmological first-order phase transitions, JHEP 04 (2021) 055 [arXiv:2009.10080] [INSPIRE].  
[94] K. Kajantie, M. Laine, K. Rummukainen and M.E. Shaposhnikov, Generic rules for high temperature dimensional reduction and their application to the standard model, Nucl. Phys. B 458 (1996) 90 [hep-ph/9508379] [INSPIRE].  
[95] D. Curtin, P. Meade and H. Ramani, Thermal Resummation and Phase Transitions, Eur. Phys. J. C 78 (2018) 787 [arXiv:1612.00466] [INSPIRE].  
[96] P.M. Schicho, T.V.I. Tenkanen and J. Österman, Robust approach to thermal resummation: Standard Model meets a singlet, arXiv:2102.11145 [INSPIRE].  
[97] O. Gould, Real scalar phase transitions: a nonperturbative analysis, JHEP 04 (2021) 057 [arXiv:2101.05528] [INSPIRE].  
[98] H.H. Patel and M.J. Ramsey-Musolf, Baryon Washout, Electroweak Phase Transition, and Perturbation Theory, JHEP 07 (2011) 029 [arXiv:1101.4665] [INSPIRE].  
[99] B. Garbrecht and P. Millington, Self-consistent solitons for vacuum decay in radiatively generated potentials, Phys. Rev. D 92 (2015) 125022 [arXiv:1509.08480] [INSPIRE].  
[100] W.-Y. Ai, J.S. Cruz, B. Garbrecht and C. Tamarit, Gradient effects on false vacuum decay in gauge theory, Phys. Rev. D 102 (2020) 085001 [arXiv:2006.04886] [INSPIRE].  
[101] L. Niemi, M.J. Ramsey-Musolf, T.V.I. Tenkanen and D.J. Weir, Thermodynamics of a Two-Step Electroweak Phase Transition, Phys. Rev. Lett. 126 (2021) 171802 [arXiv:2005.11332] [INSPIRE].  
[102] J. Ellis, M. Lewicki and J.M. No, On the Maximal Strength of a First-Order Electroweak Phase Transition and its Gravitational Wave Signal, JCAP 04 (2019) 003 [arXiv:1809.08242] [INSPIRE].

[103] H.-K. Guo, K. Sinha, D. Vagie and G. White, Phase Transitions in an Expanding Universe: Stochastic Gravitational Waves in Standard and Non-Standard Histories, JCAP 01 (2021) 001 [arXiv:2007.08537] [INSPIRE].  
[104] F. Giese, T. Konstandin and J. van de Vis, Model-independent energy budget of cosmological first-order phase transitions — A sound argument to go beyond the bag model, JCAP 07 (2020) 057 [arXiv:2004.06995] [INSPIRE].  
[105] F. Giese, T. Konstandin, K. Schmitz and J. Van De Vis, Model-independent energy budget for LISA, JCAP 01 (2021) 072 [arXiv:2010.09744] [INSPIRE].  
[106] D. Cutting, M. Hindmarsh and D.J. Weir, Vorticity, kinetic energy, and suppressed gravitational wave production in strong first order phase transitions, Phys. Rev. Lett. 125 (2020) 021302 [arXiv:1906.00480] [INSPIRE].  
[107] M. Quiros, Finite temperature field theory and phase transitions, in ICTP Summer School in High-Energy Physics and Cosmology, (1999) [hep-ph/9901312] [INSPIRE].  
[108] C.L. Wainwright, CosmoTransitions: Computing Cosmological Phase Transition Temperatures and Bubble Profiles with Multiple Fields, Comput. Phys. Commun. 183 (2012) 2006 [arXiv:1109.4189] [INSPIRE].  
[109] M.J. Ramsey-Musolf, The electroweak phase transition: a collider target, JHEP 09 (2020) 179 [arXiv:1912.07189] [INSPIRE].  
[110] J.R. Espinosa, T. Konstandin, J.M. No and G. Servant, Energy Budget of Cosmological First-order Phase Transitions, JCAP 06 (2010) 028 [arXiv:1004.4187] [INSPIRE].  
[111] D. Cutting, M. Hindmarsh and D.J. Weir, Gravitational waves from vacuum first-order phase transitions: from the envelope to the lattice, Phys. Rev. D 97 (2018) 123513 [arXiv:1802.05712] [INSPIRE].  
[112] A.H. Guth and E.J. Weinberg, Cosmological Consequences of a First Order Phase Transition in the SU(5) Grand Unified Model, Phys. Rev. D 23 (1981) 876 [INSPIRE].  
[113] R.J. Scherrer and M.S. Turner, Decaying Particles Do Not Heat Up the Universe, Phys. Rev. D 31 (1985) 681 [INSPIRE].  
[114] D. O'Connell, M.J. Ramsey-Musolf and M.B. Wise, Minimal Extension of the Standard Model Scalar Sector, Phys. Rev. D 75 (2007) 037701 [hep-ph/0611014] [INSPIRE].  
[115] J. Elias-Miro, J.R. Espinosa and T. Konstandin, Taming Infrared Divergences in the Effective Potential, JHEP 08 (2014) 034 [arXiv:1406.2652] [INSPIRE].  
[116] V. Barger, P. Langacker, M. McCaskey, M.J. Ramsey-Musolf and G. Shaughnessy, LHC Phenomenology of an Extended Standard Model with a Real Scalar Singlet, Phys. Rev. D 77 (2008) 035005 [arXiv:0706.4311] [INSPIRE].  
[117] S. Profumo, M.J. Ramsey-Musolf and G. Shaughnessy, Singlet Higgs phenomenology and the electroweak phase transition, JHEP 08 (2007) 010 [arXiv:0705.2425] [INSPIRE].  
[118] A. Alves, D. Gonçalves, T. Ghosh, H.-K. Guo and K. Sinha, Di-Higgs Production in the 4b Channel and Gravitational Wave Complementarity, JHEP 03 (2020) 053 [arXiv:1909.05268] [INSPIRE].  
[119] A. Alves, T. Ghosh, H.-K. Guo and K. Sinha, Resonant Di-Higgs Production at Gravitational Wave Benchmarks: A Collider Study using Machine Learning, JHEP 12 (2018) 070 [arXiv:1808.08974] [INSPIRE].

[120] W. Liu and K.-P. Xie, Probing electroweak phase transition with multi-TeV muon colliders and gravitational waves, JHEP 04 (2021) 015 [arXiv:2101.10469] [INSPIRE].  
[121] C.-W. Chiang, Y.-T. Li and E. Senaha, Revisiting electroweak phase transition in the standard model with a real singlet scalar, Phys. Lett. B 789 (2019) 154 [arXiv:1808.01098] [INSPIRE].  
[122] K. Fuyuto and E. Senaha, Improved sphaleron decoupling condition and the Higgs coupling constants in the real singlet-extended standard model, Phys. Rev. D 90 (2014) 015015 [arXiv:1406.0433] [INSPIRE].  
[123] P. Athron, C. Balázs, M. Bardsley, A. Fowlie, D. Harries and G. White, BubbleProfiler: finding the field profile and action for cosmological phase transitions, Comput. Phys. Commun. 244 (2019) 448 [arXiv:1901.03714] [INSPIRE].  
[124] X. Wang, F.P. Huang and X. Zhang, Energy budget and the gravitational wave spectra beyond the bag model, Phys. Rev. D 103 (2021) 103520 [arXiv:2010.13770] [INSPIRE].  
[125] M. Dine, R.G. Leigh, P.Y. Huet, A.D. Linde and D.A. Linde, Towards the theory of the electroweak phase transition, Phys. Rev. D 46 (1992) 550 [hep-ph/9203203] [INSPIRE].