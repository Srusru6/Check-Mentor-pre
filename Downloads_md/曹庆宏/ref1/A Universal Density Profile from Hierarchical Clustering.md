# A UNIVERSAL DENSITY PROFILE FROM HIERARCHICAL CLUSTERING

JULIO F. NAVARRO<sup>1</sup>

Steward Observatory, 933 North Cherry Avenue, University of Arizona, Tucson, AZ 85721-0065; jnavarro@as.arizona.edu.

CARLOS S. FRENK

Department of Physics, University of Durham, South Road, Durham DH1 3LE, England; c.s.frenk@uk.ac.durham

AND

SIMON D. M. WHITE

Max-Planck-Institut für Astrophysik, Karl-Schwarzschild-Strasse 1, 85740, Garching bei München, Germany;

swhite@mpa-garching.mpg.de

Received 1996 November 13; accepted 1997 July 15

# ABSTRACT

We use high-resolution  $N$ -body simulations to study the equilibrium density profiles of dark matter halos in hierarchically clustering universes. We find that all such profiles have the same shape, independent of the halo mass, the initial density fluctuation spectrum, and the values of the cosmological parameters. Spherically averaged equilibrium profiles are well fitted over two decades in radius by a simple formula originally proposed to describe the structure of galaxy clusters in a cold dark matter universe. In any particular cosmology, the two scale parameters of the fit, the halo mass and its characteristic density, are strongly correlated. Low-mass halos are significantly denser than more massive systems, a correlation that reflects the higher collapse redshift of small halos. The characteristic density of an equilibrium halo is proportional to the density of the universe at the time it was assembled. A suitable definition of this assembly time allows the same proportionality constant to be used for all the cosmologies that we have tested. We compare our results with previous work on halo density profiles and show that there is good agreement. We also provide a step-by-step analytic procedure, based on the Press-Schechter formalism, that allows accurate equilibrium profiles to be calculated as a function of mass in any hierarchical model.

Subject headings: cosmology: theory - dark matter - galaxies: halos - methods: numerical

# 1. INTRODUCTION

It has been 25 years since the discovery that galaxies are surrounded by extended massive halos of dark matter. A variety of observational probes—disk rotation curves, stellar kinematics, gas rings, motions of globular clusters, planetary nebulae and satellite galaxies, hot gaseous atmospheres, gravitational lensing effects—are now making it possible to map halo mass distributions in some detail. These distributions are intimately linked to the nature of the dark matter, to the way halos formed, and to the cosmological context of halo formation.

Insight into these links came first from analytic studies. Building on the early work of Gunn & Gott (1972), similarity solutions were obtained by Fillmore & Goldreich (1984) and Bertschinger (1985) for the self-similar collapse of spherical perturbations in an Einstein-de Sitter universe. Such solutions necessarily resemble power laws in the virialized regions. Hoffman & Shaham (1985) and Hoffman (1988) extended this analysis by considering open universes, and by modeling as scale-free spherical perturbations the objects that form by hierarchical clustering from power-law initial density perturbation spectra  $[P(k)\propto k^n ]$ . They argued that isothermal structure  $(\rho \propto r^{-2})$  should be expected in an Einstein-de Sitter universe if  $n\leq -2$ , and that steeper profiles should be expected for larger  $n$  and in open universes.

Despite the schematic nature of these arguments, their general predictions were verified as numerical data became available from  $N$ -body simulations of hierarchical cosmologies. Power-law fits to halo density profiles in a variety of

simulations all show a clear steepening as  $n$  increases or the density of the universe decreases (Frenk et al. 1985, 1988; Quinn, Salmon, & Zurek 1986; Efstathiou et al. 1988; Zurek, Quinn, & Salmon 1988; Warren et al. 1992; Crone, Evrard, & Richstone 1994). An apparent exception was the work of West, Dekel, & Oemler (1987), who found that galaxy cluster density profiles show no clear dependence on  $n$ .

Significant departures from power-law behavior were first reported by Frenk et al. (1988), who noted that halo profiles in cold dark matter (CDM) simulations steepen progressively with increasing radius. Efstathiou et al. (1988) found similar departures—at odds with the analytic predictions—in their simulations of scale-free hierarchical clustering. They also noted that these departures were most obvious in their best resolved halos. Similar effects were noted by Dubinski & Carlberg (1991) in a high-resolution simulation of a galaxy-sized CDM halo. These authors found their halo to be well described by a density profile with a gently changing logarithmic slope, specifically the one proposed by Hernquist (1990).

In earlier papers of this series, we used high-resolution simulations to study the formation of CDM halos with masses spanning about 4 orders of magnitude, ranging from dwarf galaxy halos to those of rich galaxy clusters (Navarro, Frenk, & White 1995, 1996). This work showed that the equilibrium density profiles of CDM halos of all masses can be accurately fitted over two decades in radius by the simple formula

$$
\frac {\rho (r)}{\rho_ {\mathrm {c r i t}}} = \frac {\delta_ {c}}{(r / r _ {s}) (1 + r / r _ {s}) ^ {2}}, \tag {1}
$$

where  $r_s$  is a scale radius,  $\delta_c$  is a characteristic (dimensionless) density, and  $\rho_{\mathrm{crit}} = 3H^2 /8\pi G$  is the critical density for closure. This profile differs from the Hernquist (1990) model only in its asymptotic behavior at  $r\gg r_s$  (it tends to  $r^{-3}$  instead of  $r^{-4}$ ). Power-law fits over a restricted radial range have slopes that depend on the range fitted, steepening from  $-1$  near the center to  $-3$  at large  $r / r_s$ .

This similarity between CDM halos of widely differing mass is surprising in view of the strong dependence on power spectrum shape reported in earlier studies. The effective slope of the CDM power spectrum varies from  $n_{\mathrm{eff}} \approx -2$  on galactic scales to  $n_{\mathrm{eff}} \approx -1$  on cluster scales, and so one might have expected shallower profiles in galaxy halos than in clusters. In fact, the opposite is true; low-mass halos are denser, i.e., they have higher values of  $\delta_{c}$ , than high-mass halos. This property reflects the higher collapse redshift of the smaller systems. Power-law fits actually yield steeper slopes for less massive halos both when carried out at a fixed radius and when carried out at a fixed fraction of the virial radius (see Figs. 3 and 4 of Navarro et al. 1996).

We argue below that the apparent relationship between profile shape and initial power spectrum seen in earlier work results from systematic differences in the characteristic density of the halos chosen when comparing different models. This interpretation is reinforced by the recent work of Cole & Lacey (1996) and Tormen, Bouchet, & White (1997), who find that the profiles of massive halos formed from power-law spectra are well described by equation (1). They also confirm the strong correlation between  $\delta_{c}$  and halo mass seen in our earlier work, and they find that, at a given mass, halos are denser when  $n$  is larger. Thus, the spectral index  $n$  seems to control the exact relationship between characteristic density and halo mass, rather than the effective slope of the density profile.

It is clear from this discussion that a comprehensive study of this problem needs to consider the role of at least three factors: the halo mass, the power spectrum of initial density fluctuations, and the values of the cosmological parameters. In this paper, we present the results of a large set of  $N$ -body simulations designed specifically to address these issues. We consider a variety of hierarchical clustering models, including CDM and power-law initial fluctuation spectra, as well as different values of the cosmological parameters  $\Omega_0$  and  $\Lambda$ . In each cosmology, we study halos spanning a large range in mass, carefully choosing numerical parameters so that all systems are simulated with comparable numerical resolution.

The plan of the paper is as follows. Our numerical experiments are described in § 2. In § 3, we present our results, and in § 4 we discuss them in the context of earlier work. In § 5, we summarize our main conclusions. In the Appendix, we lay out the formulae necessary to calculate analytically the density profile of an equilibrium halo of any mass in any hierarchical cosmology.

# 2. NUMERICAL EXPERIMENTS

# 2.1. Cosmological Models

We analyze the structure of dark matter halos in eight different cosmologies. Five are Einstein-de Sitter  $(\Omega_0 = 1)$  models with various power spectra: the standard biased CDM spectrum (SCDM model:  $\Omega_0 = 1$ ,  $h = 0.5$ ,  $\sigma_8 = 0.63$ ) and four power-law or "scale-free" spectra with indices  $n = 0$ ,  $-0.5$ ,  $-1$ , and  $-1.5$ . Two additional models also

have power-law spectra ( $n = 0$  and  $-1$ ), but in an open universe ( $\Omega_0 = 0.1$ ). The last model we consider is a low-density CDM model with a flat geometry (CDM:  $\Omega_0 = 0.25$ ,  $\Lambda = 0.75$ ,  $h = 0.75$ ,  $\sigma_8 = 1.3$ ). (Here and throughout this paper, we express the cosmological constant  $\Lambda$  in units of  $3H_0^2$ , so that a low-density universe with a flat geometry has  $\Omega_0 + \Lambda = 1$ . We also adopt the standard convention of writing the present Hubble constant as  $H_0 = 100h\mathrm{km~s}^{-1}$ $\mathrm{Mpc}^{-1}$ .)

The normalization of the CDM models is specified by  $\sigma_{8}$ , the rms mass fluctuation in spheres of radius  $8h^{-1}$  Mpc. Because of self-similarity, the normalization of the scale-free models is arbitrary. The evolutionary state of these models may be fully specified by a single parameter, the current value of the "nonlinear mass,"  $M_{*}(z)$ . This mass scale is defined by requiring that the variance of the linear overdensity field at redshift  $z = 0$ , smoothed with a top-hat filter enclosing a mass  $M = M_{*}$ , should equal the square of the critical density threshold for spherical collapse by redshift  $z$ :  $\Delta_0^2 [M_*(z)] = \delta_{\mathrm{crit}}^2 (z,\Omega_0,\Lambda)$  (see the Appendix for details on the computation of  $\delta_{\mathrm{crit}}$ ). This definition provides a "natural" way to scale the scale-free simulations to physical units and to compare different cosmological models. In scale-free models, the mass scale defined by  $M_{*}(z)$  is the only physical scale, and therefore the structure of halos can depend on mass only through the ratio  $M / M_{*}$ .

# 2.2. Simulations

Large cosmological  $N$ -body simulations are required to simulate the evolution of dark matter halos in their full cosmological context. However, such simulations are not generally well suited to explore a large range of halo masses. This is true for the following reason: systems of differing mass formed in a single simulation are resolved to differing degrees. More massive systems are better resolved because they contain more particles and because the gravitational softening is a smaller fraction of the virial radius. These systematic differences can introduce insidious numerical artifacts in the mass trends that we wish to investigate. We circumvent this problem by using the procedure outlined by Navarro et al. (1996). Halos are first identified in cosmological  $N$ -body simulations of large periodic boxes and then resimulated individually at higher resolution. During the resimulation, the remainder of the original simulation is treated only to the accuracy needed to model tidal effects on the halo of interest. The advantage of this procedure is that numerical parameters can be tuned so that all halos are simulated with comparable resolution. Its main disadvantage is that only one halo is modeled per simulation, so that many simulations are needed to compile a representative halo sample.

# 2.2.1. Cosmological Simulations

The cosmological simulations were carried out using the  $\mathbf{P}^3\mathbf{M}$  code of Efstathiou et al. (1985). The desired initial power spectrum was generated by using the Zeldovich approximation to displace particles from a uniform initial load. The uniform load we used was either a "glass" configuration (White 1996) or a cubic grid. For simulations with power-law power spectra, the amplitude of the initial displacements was chosen by setting the power of the perturbed density field to the white-noise level at the Nyquist frequency of the particle grid. These simulations followed

![](images/36d84b3d342e10f73f6c1a7a1c8620c66cd110c95c179d26353d28b3d47d4e4b.jpg)  
FIG. 1. Particle plots illustrating the time evolution of halos of different mass in an  $\Omega_0 = 1$ ,  $\Lambda = 0$ , and  $n = -1$  cosmology. The box sizes of each column are chosen so as to include approximately the same number of particles. At  $z_0 = 0$ , the box size corresponds to about  $6r_{200}$ . Time runs from top to bottom. Each snapshot is chosen so that  $M_*$  increases by a factor of 4 between each row. Low-mass halos assemble earlier than their more massive counterparts. This is true for every cosmological scenario in our series.

$10^{6}$  particles on a  $128^{3}$  mesh and were stopped when the nonlinear mass,  $M_{*}$ , corresponded to 1000-2000 particles. We identify this time with the present  $(z = 0)$ . Since clustering evolves faster for more negative values of  $n$ , an expansion factor of 9.5 was sufficient for  $n = -1.5$ , whereas an expansion factor of 90 was required for  $n = 0$  ( $\Omega_0 = 1$ ). Open models require even longer integrations, an expansion factor exceeding 150 for  $n = 0$  and  $\Omega_0 = 0.1$ . These simulations used the time-stepping and numerical scheme described in Efstathiou et al. (1988). (Note, however, that the definition of  $M_{*}$  in that paper differs from the one we use here.)

We ran two  $\mathbf{P}^3\mathbf{M}$  simulations for each of our CDM models. The SCDM runs followed  $64^{3}$  particles in periodic boxes of 180 and  $15h^{-1}\mathrm{Mpc}$  and were stopped when  $\sigma_{8} = 0.63$  ( $M_{*} \approx 1.6 \times 10^{13}h^{-1}M_{\odot}$ ), the time that we identify with the present. The CDMA runs followed  $10^{6}$  particles in boxes of 140 and  $46.67h^{-1}\mathrm{Mpc}$ , until  $\sigma_{8} = 1.3$  ( $M_{*} \approx 4.1 \times 10^{13}h^{-1}M_{\odot}$ ).

# 2.2.2. Individual Halo Simulations

The halos that were to be resimulated at higher resolution were selected randomly at  $z = 0$  from a list of clumps identified using a friends-of-friends group finder with linking length set to  $10\%$  of the mean interparticle

separation. We chose masses in the range  $0.1 - 10M_{*}$  for the power-law models and  $0.01 - 100M_{*}$  for the CDM models. (The mass range is larger for the CDM models because, in this case, halos were chosen from two parent cosmological simulations with different box sizes.) Because we are interested the structure of equilibrium halos, we were careful not to choose for analysis any halo that is far from virial equilibrium. In practice, we analyze each resimulated halo at the time between redshifts 0.05 and 0 when it is closest to dynamical equilibrium, defined as the time when the ratio of kinetic to potential energy is closest to 0.5 for material within the virial radius. [Throughout this paper, we measure halo masses,  $M_{200}$ , within a virial radius,  $r_{200}$ , defined as the radius of a sphere of mean interior density  $200\rho_{\mathrm{crit}}$ . Halo circular speeds,  $V_{200} = (GM_{200} / r_{200})^{1/2}$ , are also measured at this radius unless otherwise specified. Numerical experiments show that for  $\Omega = 1$ , this radius approximately separates the virialized and infall regions (Cole & Lacey 1996). For convenience, we continue to use these definitions when  $\Omega_0 \neq 1$ .]

Once a halo is chosen for resimulation, the particles within its virial radius are traced back to the initial conditions, where a small box containing all of them is drawn. This box is filled with  $\sim 32^3$  particles on a cubic grid; these particles are then perturbed using the waves of the original

![](images/31d6a22a500eab9d5f1269a646738b550bb61c91aacbb7e1062cd535d6db7a86.jpg)  
FIG. 2.-Density profiles of one of the most massive halos and one of the least massive halos in each series. In each panel, the low-mass system is represented by the leftmost curve. In the SCDM and CDMΛ models, radii are given in kiloparsecs (scale at top), and densities are in units of  $10^{10}M_{\odot}\mathrm{kpc}^{-3}$ . In all other panels, the units are arbitrary. The density parameter,  $\Omega_0$ , and the value of the spectral index,  $n$ , are given in each panel. The solid lines are fits to the density profiles using eq. (1). The arrows indicate the value of the gravitational softening. The virial radius of each system is in all cases 2 orders of magnitude larger than the gravitational softening.

$\mathbf{P}^3\mathbf{M}$  simulation, together with extra high frequency waves added to fill out the power spectrum between the Nyquist frequencies of the old and new particle grids. The regions beyond the "high-resolution" box are coarsely sampled with a few thousand particles of radially increasing mass in order to account for the large-scale tidal fields present in the original simulation.

This procedure ensures the formation of a clump similar in all respects to the one selected in the  $\mathbf{P}^3\mathbf{M}$  run, except for the improved numerical resolution. The size of the high-resolution box scales naturally with the total mass of each system, and as a result all resimulated halos have about the same number of particles within the virial radius at  $z = 0$ , typically between 5000 and 10,000. The extensive tests presented in Navarro et al. (1996) indicate that this number of particles is adequate to resolve the structure of a halo over approximately two decades in radius. We therefore choose the gravitational softening,  $h_g$ , to be  $1\%$  of the virial radius in all cases. (This is the scale length of a spline softening; see Navarro & White 1993 for a definition.) The tree code

carries out simulations in physical, rather than comoving, coordinates and uses individual time steps for each particle. The minimum time-step depends on the maximum density resolved in each case, but it was typically  $10^{-5}H_0^{-1}$ .

As discussed in Navarro et al. (1996), numerically convergent results require that the initial redshift of each run,  $z_{\mathrm{init}}$ , should be high enough that all resolved scales in the initial box are still in the linear regime. In order to satisfy this condition, we chose  $z_{\mathrm{init}}$  so that the median initial displacement of particles in the high-resolution box was always less than the mean interparticle separation. Problems with this procedure may arise if  $z_{\mathrm{init}}$  is so high that the gravitational softening (which is kept fixed in physical coordinates) becomes significantly larger than the mean initial interparticle separation. We found this to be a problem only for the smallest masses,  $M \lesssim M_*$ , in the  $n = 0$ ,  $\Omega_0 = 0.1$  model. In this case, the initial redshift prescribed by the median displacement condition is  $z_{\mathrm{init}} > 700$ , and the gravitational softening is then a significant fraction of the initial box. This can affect the collapse of the earliest

![](images/457a776ff12e64434d86ca0920ea6ee52b168dfd6af08ed272757d8bd9818864.jpg)  
FIG. 3.-The fits to the density profiles of Fig. 2, scaled to the virial radius,  $r_{200}$ , of each system and to the critical density of the universe at  $z = 0$ . The solid and dashed lines correspond to the low- and high-mass systems, respectively. Note that low-mass systems are denser than high-mass systems near the center, indicating that the characteristic density of a halo increases as the halo mass decreases.

progenitors of these systems and thus introduce spurious effects. We therefore limit our investigation to  $M \gtrsim M_*$  in this particular cosmological model. Further tests of the effects of particle number, time-step size, and gravitational softening are given by Tormen et al. (1997). Their results confirm that the numerical parameters chosen here are adequate to give stable and accurate results.

# 3. RESULTS

# 3.1. Time Evolution

Figure 1 illustrates the time evolution of halos of different mass selected from the  $\Omega_0 = 1$ ,  $n = -1$  series. Time runs from top to bottom, and mass increases from left to right. The box size in each column is chosen so as to contain always approximately the same number of particles. The redshifts of each snapshot have been chosen so that the nonlinear mass  $M_*$  increases by factors of 4 from  $z_2$  to  $z_1$  and from  $z_1$  to  $z_0 = 0$ . This figure illustrates convincingly that low-mass halos complete their assembly earlier than more massive systems.

# 3.2. Density Profiles

Figure 2 shows spherically averaged density profiles at

$z = 0$  for one of the least and one of the most massive halos for each set of cosmological parameters. These halos span almost 4 orders of magnitude in mass in the case of the CDM models, and about 2 orders of magnitude in mass in the power-law models. Radial units are in kiloparsecs for CDM models (scale at the top) and are arbitrary in the power-law panels. Density is in units of  $10^{10}M_{\odot}\mathrm{kpc}^{-3}$  in the CDM models and in arbitrary units in the others. The solid lines are fits to each halo profile using equation (1). This simple formula provides a good fit to the structure of all halos over about two decades in radius, from the gravitational softening (indicated by arrows in Fig. 2) to about the virial radius. The quality of the fit is essentially independent of halo mass or cosmological model and implies a remarkable uniformity in the equilibrium structure of dark matter halos in different hierarchical clustering models.

The solid and dashed lines in Figure 3 show the profile fits of Figure 2, but with the radius scaled to the virial radius of each halo. This scaling removes the intrinsic dependence of size on mass (more massive halos are bigger) and allows a meaningful comparison between halos of different mass. From the definition of virial radius, the "concentration" of a halo,  $c = r_{200} / r_s$ , and the characteristic density,  $\delta_c$ , are

![](images/2ad6b8903c368285450ec05d0a57fa3a5b395a0168cc63ae5e59f8e0fe18cb4b.jpg)  
FIG. 4.—The circular velocity profiles of the halos shown in Fig. 2. Radii are in units of the virial radius, and circular speeds are normalized to the value at the virial radius. The solid lines show the data from the simulations. All curves have the same shape: they rise near the center, until they reach a maximum, and then decline at the outer edge. Low-mass systems have higher maximum circular velocities in these scaled units because of their higher central concentrations. The dashed lines are fits using eq. (3). In each panel, the dotted line is the fit to the low-mass halo using a Hernquist profile. Note that this model fits rather well the inner regions of the halos but underestimates the circular velocity near the virial radius.

linked by the relation

$$
\delta_ {c} = \frac {2 0 0}{3} \frac {c ^ {3}}{\left[ \ln (1 + c) - c / (1 + c) \right]}. \tag {2}
$$

Thus, at given halo mass (specified by  $M_{200}$ ), there is a single free parameter in equation (1), which may be expressed either as the characteristic density,  $\delta_c$ , or as the concentration parameter,  $c$ . This free parameter varies systematically with mass; Figure 3 shows that  $c$  and  $\delta_c$  decrease with increasing halo mass.

A universal density profile implies a universal circular velocity profile,  $V_{c}(r) = [GM(r) / r]^{1 / 2}$ . This is illustrated in Figure 4, where we plot  $V_{c}$ -profiles for the same systems shown in Figure 2. As in Figure 3, radii are plotted in units of the virial radius; circular speeds have been normalized to the value at the virial radius,  $V_{200}$ . The circular velocity curve implied by equation (1) is

$$
\left[ \frac {V _ {c} (r)}{V _ {2 0 0}} \right] ^ {2} = \frac {1}{x} \frac {\ln (1 + c x) - (c x) / (1 + c x)}{\ln (1 + c) - c / (1 + c)}, \tag {3}
$$

where  $x = r / r_{200}$  is the radius in units of the virial radius. Circular velocities rise near the center, reach a maximum  $(V_{\mathrm{max}})$  at  $x_{\mathrm{max}} \sim 2 / c$ , and decline near the virial radius. More centrally concentrated halos (higher  $\delta_c$  or higher  $c$ ) are characterized by higher values of  $V_{\mathrm{max}} / V_{200}$ . The dashed lines in Figure 4 show plots of equation (3) with parameter values derived from the fits to the density profiles of Figure 2. The dotted lines are fits using a Hernquist (1990) model constrained to match the location of the maximum of the  $V_{c}$ -curve. The two fits are indistinguishable near the center, but the Hernquist model underestimates  $V_{c}$  near the virial radius. This disagreement becomes more pronounced in lower mass systems, for which  $\delta_c$  and  $V_{\mathrm{max}} / V_{200}$  are larger.

# 3.3. Mass Dependence of Halo Structure

The mass-density dependence pointed out above is further illustrated in Figure 5, where we plot  $\delta_{c}$  versus mass (expressed in units of  $M_{*}$ ) for all the systems in each series. An equivalent plot, illustrating the mass dependence of the concentration,  $c$ , is shown in Figure 6 (the upper left panel,

![](images/56fea4098b5170c89ebc1957fd6a5c4eccd17e1e7cb50487382d09167f620731.jpg)  
FIG. 5.-The correlation between the mass of a halo and its characteristic density. Masses are given in units of the nonlinear mass scale  $M_{*}$  (see text for a definition). Densities are relative to the critical value. Three curves are shown in each panel for different values of the parameter  $f$  (see eq. [5]). The fits are normalized to intersect at  $M_{200} = M_{*}$  in the case  $\Omega = 1$ . This normalization is then used for the low-density models  $(\Omega_0 < 1)$ . Note that for  $f = 0.01$ , this procedure results in good fits to the results of the simulations in all cases.

corresponding to the SCDM model, is equivalent to Fig. 7 of Navarro et al. 1996). The characteristic density of a halo increases toward lower masses in all the cosmological models considered. This result supports the idea that the  $M_{200} - \delta_c$  relation is a direct result of the higher redshift of collapse of less massive systems, and it suggests a simple model to describe the mass-density relation. This model assigns to each halo of mass  $M$  (identified at  $z = 0$ ) a collapse redshift,  $z_{\mathrm{coll}}(M,f)$ , defined as the time at which half the mass of the halo was first contained in progenitors more massive than some fraction  $f$  of the final mass. With this definition,  $z_{\mathrm{coll}}$  can be computed by simply using the Press-Schechter formalism (e.g., Lacey & Cole 1993),

$$
\operatorname {e r f c} \left\{\frac {\delta_ {\operatorname {c r i t}} \left(z _ {\operatorname {c o l l}}\right) - \delta_ {\operatorname {c r i t}} ^ {0}}{\sqrt {2 \left[ \Delta_ {0} ^ {2} (f M) - \Delta_ {0} ^ {2} (M) \right]}} \right\} = \frac {1}{2}, \tag {4}
$$

where  $\Delta_0^2 (M)$  is the linear variance of the power spectrum at  $z = 0$  smoothed with a top-hat filter of mass  $M$ ,  $\delta_{\mathrm{crit}}(z)$  is the density threshold for spherical collapse by redshift  $z$ , and  $\delta_{\mathrm{crit}}^{0} = \delta_{\mathrm{crit}}(0)$ . [This definition can be extended to halos

identified at any redshift  $z_0$  by replacing  $\delta_{\mathrm{crit}}^0$  by  $\delta_{\mathrm{crit}}(z_0)$  in eq. (4).] Assuming that the characteristic density of a halo is proportional to the density of the universe at the corresponding  $z_{\mathrm{coll}}$  then implies

$$
\delta_ {c} (M \mid f) = C \Omega_ {0} \left[ 1 + z _ {\operatorname {c o l l}} (M, f) \right] ^ {3}, \tag {5}
$$

where  $C$  is a proportionality constant that might, in principle, depend on  $f$  and on the power spectrum.

We will see below that  $f \ll 1$  is needed for this argument to give a good fit to our simulation data. In this limit,  $\Delta_0^2(fM) \gg \Delta_0^2(M)$ , and equation (4) reduces to

$$
\delta_ {\text {c r i t}} \left(z _ {\text {c o l l}}\right) = \delta_ {\text {c r i t}} ^ {0} + C ^ {\prime} \Delta_ {0} (f M), \tag {6}
$$

where  $C' \approx 0.7$ . For  $f \ll 1$ ,  $\delta_{\mathrm{crit}}(z_{\mathrm{coll}}) \gg \delta_{\mathrm{crit}}^{0}$  for all masses in the range of interest, so that  $\delta_{\mathrm{crit}}(z_{\mathrm{coll}}) \propto \Delta_0(fM)$ . Since  $M_{*}(z_{\mathrm{coll}})$  is defined by  $\Delta_0[M_{*}(z_{\mathrm{coll}})] = \delta_{\mathrm{crit}}(z_{\mathrm{coll}})$ , this equation implies that the characteristic density of a halo is proportional to the mean density of the universe at the time when  $M_{*} \approx fM$ , i.e., when the characteristic nonlinear mass is a fixed small fraction of the final halo mass. For scale-free

![](images/cdea579e97a65f918ba595541d9b15a7b9591d2492d7d5e7baac54e97673ea7d.jpg)  
FIG. 6.-Same as Fig. 5, but for the concentration parameter  $c$

models, this implies  $\delta_c \propto M^{-(n + 3) / 2}$ , the same scaling that links  $M_{*}(z)$  and the mean cosmic density at redshift  $z$ .

Figure 5 shows the correlations predicted from equation (5) for three values of the parameter  $f$ : 0.5, 0.1, and 0.01. The value of the proportionality constant,  $C(f)$ , is chosen in each case in order to match the results of the Einstein-de Sitter simulations for  $M = M_{*}$ . These values are given in Table 1. The same values of  $C(f)$  are used to plot the curves in the panels corresponding to the low-density models. Some interesting results emerge from an inspection of Figure 5 and Table 1. They are as follows:

1. The agreement between the mass-density dependence predicted by equation (5) and the results of the Einstein-de Sitter simulations improves for smaller values of  $f$ . This is also true for the low-density models. Once  $C(f)$  is fixed by matching the results of the Einstein-de Sitter models, the same value of  $C(f)$  provides a good match to the low-density models only if  $f \lesssim 0.01$ . Interestingly, for  $f = 0.01$ , approximately the same value of the proportionality constant,  $C \approx 3 \times 10^3$ , seems to fit all our simulations.  
2. The characteristic density of  $M_*$  halos decreases systematically for more negative values of the spectral index  $n$ .

At  $M = M_{*}$ , SCDM halos are the least dense in our  $\Omega_0 = 1$  series, less concentrated still than those corresponding to  $n = -1.5$ . This is consistent with the general trend because, according to equations (4) and (5), the characteristic density of a halo of mass  $M_{*}$  is controlled by the shape of the power spectrum on scales  $\sim fM_{*}$ . This is about  $\sim 10^{11}M_{\odot}$  for  $f \approx 0.01$ , and the effective slope of the CDM spectrum on this mass scale is  $n_{\mathrm{eff}} \sim -2$ .

3. For the power-law models with  $n = 0$  and  $-1$ , the characteristic density at a given  $M / M_{*}$  increases as  $\Omega_0$  decreases. Such a trend is plausible since we expect the collapse redshift of halos of a given mass to increase as  $\Omega_0$  decreases. On the other hand, halos formed in the low-density CDM universe are actually less dense than those formed in the standard biased CDM model because  $\delta_c$  depends not only on collapse redshift but also on  $\Omega_0$  (see eq. [5]). Although reducing  $\Omega_0$  increases the collapse redshift, the increase in  $\delta_c$  from the  $(1 + z_{\mathrm{coll}})^3$  factor can be outweighed by the change in  $\Omega_0$ . In the CDMΛ model, the two effects can combine to give a reduction in  $\delta_c$  as  $\Omega_0$  decreases. (We remind the reader that  $\delta_c$  is defined relative to the critical density rather than the mean density.)

![](images/d9b79fac4405964e5af78518e4c13b0b3d45eb86aa804d16b1680b48c07f9dcb.jpg)  
FIG. 7. The mass dependence of the maximum circular velocity of a halo. Velocity units are arbitrary in the power-law panels and  $\mathrm{km~s^{-1}}$  in the CDM models (scale at top). Mass is in units of  $10^{10}M_{\odot}$  for CDM halos and in units of  $M_{*}$  in the other panels. Power-law fits of the form  $M\propto V_{\mathrm{max}}^{\alpha}$  are shown. The value of  $\alpha$  and the rms scatter in the mass around the fit are indicated in each panel. Note that the  $M - V_{\mathrm{max}}$  dependence steepens for larger values of the spectral index  $n$ . The effect of the cosmological parameters on  $\alpha$  seems to be rather small.

4. Each halo has a characteristic maximum circular speed,  $V_{\mathrm{max}}$  (see eq. [3]), that is strongly correlated with its mass. This is shown in Figure 7, where we also plot least-squares fits of the form  $M_{200} \propto V_{\mathrm{max}}^{\alpha}$  to the data in each series. Consistent with the trends shown in Figures 5 and 6, the correlation steepens as  $n$  increases; we find  $\alpha \sim 3.2 - 3.3$  for CDM models and  $\alpha > 5$  for  $n = 0$ . Note also that the correlations are extremely tight; the rms scatter in  $\log M_{200}$  is less than  $\sim 0.1$  in all cases. This is in part a consequence of the generally good fit of the density profile of equation (1). The ratio  $V_{\mathrm{max}} / V_{200}$  increases only logarithmically with the central concentration of the halo and changes only by about a factor of 2 as  $\delta_c$  varies by 4 orders of magnitude between  $10^3$  and  $10^7$ . As a result, the  $M_{200} - V_{\mathrm{max}}$  relation does not deviate much from the  $M_{200} - V_{200}$  relation that, by definition, has zero scatter. This has important consequences for the expected tightness of empirical correlations between mass and characteristic velocity, such as the Tully-Fisher relation. We intend to return to this issue in future work.

The results in Figures 5-7 support our conclusion that the characteristic density of a halo is controlled mainly by the mean matter density of the universe at a suitably defined time of collapse. One important test of this interpretation is to measure  $z_{\mathrm{coll}}$  directly in the simulations and to compare the result to equation (5). To do this, we identify clumps at every output time using our friends-of-friends group finder with linking length set to  $20\%$  of the current mean interparticle separation. We then trace the particles in the most massive clump identified at  $z = 0$  (which typically has a mean overdensity of  $\sim 200$ ) and, at each redshift, add up the total mass in clumps that contain any of these particles and that are individually more massive than  $10\%$  of the final mass. We identify  $z_{\mathrm{coll}}$  with the redshift at which this mass first exceeds half of the final mass. This is roughly equivalent to the analytic procedure outlined in equation (4) for  $f = 0.1$ . (We decided to use  $f = 0.1$  rather than  $f = 0.01$  because the smaller value results in very high collapse redshifts, often before the first output in the simulation.) The main difference is that some of the mass from the high

![](images/91d788e0e83e353c5ec17b4917b1f5f77b10939415f0cce02c0bd2bdd7c4bcd9.jpg)  
FIG. 8.—The characteristic density of all halos in our series as a function of the redshift at which half of the final mass is in collapsed progenitors more massive than  $10\%$  of the final mass. The filled circles correspond to all our runs with  $\Omega_0 = 1$ , the open circles to our runs with  $\Omega_0 = 0.1$  and  $\Lambda = 0$ , and the asterisks to the CDMA runs ( $\Omega_0 = 0.25$ ,  $\Lambda = 0.75$ ). The solid line shows the "natural" scaling,  $\delta_c \propto \Omega_0 (1 + z)^3$ , expected if the characteristic density of a halo is directly proportional to the mean matter density of the universe at the time of collapse.

redshift progenitors ends up outside the virial radius at  $z = 0$ . This causes a slight bias of the measured collapse redshifts toward higher values than the Press-Schechter predictions.

TABLE 1 PARAMETERS IN EQUATION (5) USED TO PLOT THE FITS IN FIGURE 5  

<table><tr><td>P(k)</td><td>Ω0</td><td>Λ</td><td>f</td><td>C(f)</td></tr><tr><td rowspan="3">CDM...........................</td><td>1.0</td><td>0.0</td><td>0.5</td><td>1.75 × 104</td></tr><tr><td>1.0</td><td>0.0</td><td>0.1</td><td>7.44 × 103</td></tr><tr><td>1.0</td><td>0.0</td><td>0.01</td><td>3.41 × 103</td></tr><tr><td rowspan="3">CDMA...........................</td><td>0.25</td><td>0.75</td><td>0.5</td><td>1.75 × 104</td></tr><tr><td>0.25</td><td>0.75</td><td>0.1</td><td>7.44 × 103</td></tr><tr><td>0.25</td><td>0.75</td><td>0.01</td><td>3.41 × 103</td></tr><tr><td rowspan="3">n = -1.5........................</td><td>1.0</td><td>0.0</td><td>0.5</td><td>3.00 × 104</td></tr><tr><td>1.0</td><td>0.0</td><td>0.1</td><td>1.08 × 104</td></tr><tr><td>1.0</td><td>0.0</td><td>0.01</td><td>3.15 × 103</td></tr><tr><td rowspan="6">n = -1.0........................</td><td>1.0</td><td>0.0</td><td>0.5</td><td>5.00 × 104</td></tr><tr><td>1.0</td><td>0.0</td><td>0.1</td><td>1.38 × 104</td></tr><tr><td>1.0</td><td>0.0</td><td>0.01</td><td>2.50 × 103</td></tr><tr><td>0.1</td><td>0.0</td><td>0.5</td><td>5.00 × 104</td></tr><tr><td>0.1</td><td>0.0</td><td>0.1</td><td>1.38 × 104</td></tr><tr><td>0.1</td><td>0.0</td><td>0.01</td><td>2.50 × 103</td></tr><tr><td rowspan="3">n = -0.5........................</td><td>1.0</td><td>0.0</td><td>0.5</td><td>1.25 × 105</td></tr><tr><td>1.0</td><td>0.0</td><td>0.1</td><td>2.81 × 104</td></tr><tr><td>1.0</td><td>0.0</td><td>0.01</td><td>2.81 × 103</td></tr><tr><td rowspan="6">n = 0.0........................</td><td>1.0</td><td>0.0</td><td>0.5</td><td>4.00 × 105</td></tr><tr><td>1.0</td><td>0.0</td><td>0.1</td><td>6.66 × 104</td></tr><tr><td>1.0</td><td>0.0</td><td>0.01</td><td>4.00 × 103</td></tr><tr><td>0.1</td><td>0.0</td><td>0.5</td><td>4.00 × 105</td></tr><tr><td>0.1</td><td>0.0</td><td>0.1</td><td>6.66 × 104</td></tr><tr><td>0.1</td><td>0.0</td><td>0.01</td><td>4.00 × 103</td></tr></table>

The correlation between  $\delta_{c} / \Omega_{0}$  and  $(1 + z_{\mathrm{coll}})^{3}$  obtained by using this procedure is shown in Figure 8. All the halos in the Einstein-de Sitter models are shown as filled circles, those in open universes as open circles, and those in the CDMA model as asterisks. The solid line is the relation predicted by equation (5) for  $C = 5\times 10^{3}$ . This is clearly an excellent approximation to the results of the numerical simulations and confirms that the mean matter density of the universe at the time of collapse is the main factor determining the characteristic density of a halo. Note that the value of the proportionality constant is slightly lower than the values given in Table 1 for  $f = 0.1$ . This difference compensates for the slight bias toward higher collapse redshifts introduced by our numerical procedure.

A summary of our results is presented in Figure 9. The panels on the left compile the fits (for  $f = 0.01$ ) to the mass dependence of  $\delta_{c}$  and  $c$  in the Einstein-de Sitter models. The panels on the right compare the Einstein-de Sitter results with those for low-density models. As noted above, the typical density of  $M_{*}$  halos increases with  $n$ . However, the difference between models becomes less pronounced at higher masses and is almost negligible at  $M \gtrsim 10M_{*}$ . Halos of a given  $M / M_{*}$  in low-density universes can have either lower or higher characteristic densities than their Einstein-de Sitter counterparts, depending on the competing effects of the collapse redshift and the value of  $\Omega_0$ . Note that all the curves in Figure 9 use the same value,  $f = 0.01$ , and essentially the same value of the proportionality constant  $C \approx 3 \times 10^3$  (see eq. [5]). Thus, once calibrated for an Einstein-de Sitter model, it is possible to apply equations (4) and (5) to predict the characteristic density of halos formed in other hierarchically clustering models. In the Appendix, we provide a detailed description of how to compute  $\delta_{c}(M)$  numerically for a variety of cosmologies.

# 3.4. Scatter in the Correlations

We now examine the origin of the scatter in the correlations presented above. In particular, we explore whether at fixed mass the dispersion in the measured values of  $\delta_{c}$  is due to variations in the collapse redshift or in the global angular momentum of the system. As shown by Figures 10 and 11, the bulk of the scatter in  $\delta_{c}$  at a given  $M / M_{*}$  can be attributed to small differences in the redshift of collapse. Figure 10 shows that the  $\delta_{c}$ -deviations from the solid-line fits in Figure 5 (i.e., those for  $f = 0.01$ ) correlate strongly with deviations in the redshift of collapse. [The latter are measured from least-squares fits to the  $M_{200}$  vs.  $(1 + z_{\mathrm{coll}})$  correlations measured directly from the simulations.] Furthermore, the two residuals seem to correlate just as expected from equation (5), i.e.,  $\Delta \log \delta_{c} = 3\Delta \log (1 + z_{\mathrm{coll}})$ . (We note that the magnitude of this scatter may not be fully representative of the dispersion in halo properties corresponding to each cosmological model, since the sample has been selected so as to minimize departures from equilibrium.) This relation is indicated by the solid line and is seen to reproduce very well the trend observed in Figure 10. Figure 11 shows the same  $\delta_{c}$ -residuals of Figure 10, but now as a function of the scatter in the mass-rotation parameter  $(M_{200}$  vs.  $\lambda$ ) correlation. (The rotation parameter is defined by  $\lambda = J|E|^{1/2}/GM^{5/2}$ , where  $J$  is the angular momentum and  $E$  is the binding energy of the halo. The median  $\lambda$  in our series is  $\sim 0.04$ , in good agreement with previous studies.) We find no discernible correlation between  $M / M_{*}$  and  $\lambda$ , or between the  $\delta_{c}$ - and  $\lambda$ -residuals (Fig. 11). This provides

![](images/e799dfbe81bfdcc494e5578ad2810c3b1850e09a969eaeb07e3ce9b2392845c8.jpg)  
FIG. 9.—A summary of the mass dependence of  $\delta_{c}$  and  $c$  in our different cosmological models. Mass is given in units of the nonlinear mass scale  $M_{*}$ . The curves are labeled in the upper plots, and the same line types are used in the bottom plots. The symbols in the lower right panel show the correlation between  $c$  and mass found by Cole & Lacey (1996), with open squares for  $n = -1$ ,  $\Omega_0 = 1$  and filled squares for  $n = 0$ ,  $\Omega_0 = 1$ . These results should be compared with the lower dashed curve and the lower dot-dashed curve in the same panel, respectively. Because of their poorer numerical resolution, Cole & Lacey's halos are significantly less concentrated than the ones in our study.

further evidence supporting our contention that the redshift of collapse is the primary factor determining the characteristic density of a halo.

# 4. COMPARISON WITH PREVIOUS WORK

The main conclusion of our study, that the shape of halo density profiles is independent of cosmological context, appears to contradict previous work on this subject. As discussed in § 1, a strong dependence of the slope of the density profile on the spectral index  $n$  and the density parameter  $\Omega_0$  has been established by a number of analytic and numerical studies. We now show that our results actually include and extend those of previous workers, and we offer an attractive explanation for some discrepancies found in the literature.

We first address the claim by Quinn et al. (1986), Efstathiou et al. (1988), Zurek et al. (1988), and Warren et al. (1992) that halo density profiles steepen with increasing values of the spectral index  $n$  in an Einstein-de Sitter universe. This claim is based on the discovery that circular velocity profiles of galaxy-sized halos are relatively flat for

$n \approx -2$  (or for SCDM; Frenk et al. 1985) but decline progressively faster at large  $r$  for larger  $n$ . Figure 12 shows that we find the same trend if we analyze our data in the same fashion as these authors. In this figure, we plot, in linear units, the  $V_{c}$ -profile of an  $M_{*}$  halo for different values of  $n$ . Each curve has been computed using equation (3) and the values of  $c$  obtained from the fits presented in Figure 9. Since all these halos have the same mass, they also have the same virial radius and circular speed,  $r_{200}$  and  $V_{200}$ , respectively, which we have used as normalizing factors. The linear units in Figure 12 obscure the fact that the form of the curves is the same in all cases, and these linear units encourage one to conclude, as did previous authors, that halo rotation curves steepen with increasing  $n$ . In fact, this trend is present because  $M_{*}$  halos collapse earlier, and so are denser, for larger values of  $n$ .

We note that the trend with  $n$  in Figure 12 is sensitive to the choice of halo mass. If we had used halos with  $M < M_{*}$ , the trend would have been stronger. On the other hand, very massive halos ( $M \gtrsim 10M_{*}$ ) have similar characteristic densities, irrespective of  $n$  (see Fig. 9). Thus, if we had

![](images/77b48355e2ee3ced45b5cfec4460651bafbca75b7e656a69c5af9050ac398c45.jpg)  
FIG. 10.-The  $\delta_c$ -deviation from the fits shown in Fig. 5 (for  $f = 0.01$ ) plotted vs. the deviation from the mean relation between the collapse redshift,  $1 + z_{\mathrm{coll}}$  (Fig. 8), and the mass of a system. Note that systems assembled earlier (later) than the average tend to have characteristic densities above (below) the mean. The correlation between the  $\delta_c$  and  $1 + z_{\mathrm{coll}}$  residuals follows the "natural" scaling,  $\Delta \log \delta_c = 3\Delta \log (1 + z_{\mathrm{coll}})$ , as shown by the solid line. Only the results corresponding to  $\Omega_0 = 1$  are shown.

plotted very massive halos in Figure 12, we would have concluded that the density profile depends only weakly on  $n$  (at least for  $\Omega_0 = 1$ ). This is reminiscent of the claim by West et al. (1987) that the structure of galaxy cluster halos is independent of  $n$  in Einstein-de Sitter universes. Our analysis suggests an explanation for this apparently discrepant result. By considering only the most massive systems in

![](images/3fd185682786ff5bde2e6b53aaaa63b7a5f126994590fcc9d7e263662f3a2460.jpg)  
FIG. 11.-The  $\delta_{c}$ -residuals in Fig. 5 relative to the solid curve fit  $(f = 0.01)$  plotted vs. the residuals in the  $M_{200} - \lambda$  correlation. This figure shows that the scatter in  $\delta_{c}$  at a given mass cannot be attributed to the effects of rotation. All halos with  $\Omega_0 = 1$  are included in this plot.

![](images/9c9d317013353f6afa67628cc6b23dd69e94fdf46b9e835f402be870110a042e.jpg)  
FIG. 12.-Circular velocity profiles of  $M_{*}$  halos formed in simulations with different power spectra in an Einstein-de Sitter universe. The curves were computed using eq. (3), and the values of the concentration  $c$  were obtained from the fits in Fig. 9. Radii are in units of the virial radius, and circular speeds in units of the circular velocity at the virial radius. Note that, because of the use of linear units, the fact that all curves have the same shape (eq. [3]) is not immediately apparent.

their simulations, West et al. focused on a mass range where the dependence of  $\delta_{c}$  on  $n$  is minimal, and so they concluded (correctly) that cluster profiles depend very weakly on the initial power spectrum.

A similar explanation accounts for the weak dependence of the halo density profile on the spectral index  $n$  and on  $\Omega_0$  reported by Crone et al. (1994). These authors chose to combine the 35 most massive clumps in each of their cosmological simulations in order to produce an "average" density profile for each value of  $n$  and  $\Omega_0$ . They then fitted power laws of the form  $\rho(r) \propto r^\gamma$  to these profiles in the radial range corresponding to density contrasts between 100 and 3000. For  $\Omega_0 = 1$ , this procedure yielded  $\gamma$ -values that decrease from -2.2 to -2.5 as  $n$  increases from -2 to 0 (see the curve labeled "EdS" in their Fig. 4). Our results show that this weak trend is a consequence of the averaging procedure they adopted. The shape of the halo mass function depends strongly on  $n$  and is increasingly peaked around  $M \approx M_*$  for larger values of  $n$ . Thus, combining the 35 most massive clumps in a simulation results in different "effective" masses for different values of  $n$ , with a bias toward larger values of  $M / M_*$  for more negative values of  $n$ . By applying the same selection procedure as Crone et al. to our own cosmological simulations, we find that the median mass of these halo ensembles increases from  $\sim M_*$  for  $n = 0$  to  $\sim 6M_*$  for  $n = -1.5$ . As illustrated in Figure 13, fitting power laws to the density profiles of these "average" halos results in a weak steepening with  $n$  similar to the trend reported by Crone et al. The slopes of  $\gamma \sim -3$  that they found for low-density models are also easily understood, since in these cases they fit a radial range that extends well outside our nominal virial radius  $r_{200}$ .

Our results are also in agreement with the recent work by Cole & Lacey (1996) and Tormen et al. (1997), who

![](images/2cc86d9690d5a4e6fd4bbda08df5c66d514579d3e0edcc8291ae6340769eeb0b.jpg)  
FIG. 13.—A comparison between our density profiles and the power-law fits of Crone et al. (1994). The region fitted by these authors, corresponding to densities between 100 and 3000, is shown by the dotted lines. Over this region, our results (solid lines) and the power-law parameterization adopted by Crone et al. (dashed lines) are consistent. The profiles shown by the solid lines correspond to  $M = 6M_{*}$  ( $n = -1.5$ ),  $M = 4M_{*}$  ( $n = -1$ ),  $M = 2M_{*}$  ( $n = -0.5$ ), and  $M = M_{*}$  ( $n = 0$ ), as discussed in the text.

analyzed the structure of massive halos ( $M > M_{*}$ ) in scale-free universes. The general correlations with mass that they report (more massive halos tend to be less centrally concentrated than less massive halos) agree well with the results we present in § 3. At a given halo mass, however, Cole & Lacey's halos are significantly less concentrated than ours. For example, for  $M_{*}$  halos, they find  $c \sim 12$  and  $\sim 17$  for  $n = -1$  and 0, respectively ( $\Omega_0 = 1$ ), compared with  $c \sim 17$  and  $\sim 30$  in our simulations (see connected symbols in the lower right panel of Fig. 9). On the other hand, the results of Tormen et al. (1997) are in very good agreement with ours; they find  $c \sim 10$  for a  $10M_{*}$  halo formed in an  $n = -1$ ,  $\Omega_0 = 1$  universe, which compares well with  $c \sim 9$  that we find for a similar system.

As discussed in detail by Tormen et al., the discrepancy between our results and those of Cole & Lacey is likely to be due in part to the poorer numerical resolution of their simulations. Indeed, their simulations used gravitational softenings that are 2-3 times larger than ours and time steps that are also significantly longer than the typical values in our simulations. Both of these effects can artificially lower the central concentration of a halo. A concurrent factor may be the averaging procedure adopted by Cole & Lacey.

These authors constructed average density profiles by coadding all halos of similar mass identified in their cosmological simulations, regardless of their dynamical state. This sample contains a number of unrelaxed systems and ongoing mergers where substructure and double centers can bias the results of the fitting procedure toward lower concentrations.

We can test directly for the effects of these various factors by applying the averaging procedure of Cole & Lacey to halos identified in our own  $\mathbf{P}^3\mathbf{M}$  cosmological simulations (see § 2.2.1) and comparing them with the results of the individual halo runs. We restrict this comparison to the most massive halos in each run,  $M \gtrsim 10M_*$ , since these systems have a large number of particles and a comparable numerical resolution to that of Cole & Lacey. The comparison confirms that the central concentration of halos can be significantly underestimated as a result of the factors mentioned above. The magnitude of the effect is sensitive to  $n$  and  $\Omega_0$ ; the concentration  $c$  can be underestimated by up to a factor of  $\sim 3$  for  $n = 0$  and  $\Omega_0 = 0.1$ , but by less than  $\sim 1.5$  for  $n = -1$  and  $\Omega_0 = 1$ . We conclude that the disagreement between our results and those of Cole & Lacey is likely to be the result of the combined effect of their halo selection

and averaging procedures and their poorer numerical resolution.

# 5. DISCUSSION

Our results suggest that equilibrium dark halos formed through dissipationless hierarchical clustering have density profiles with a universal shape that does not depend on their mass, on the power spectrum of initial fluctuations, or on the cosmological parameters  $\Omega_0$  and  $\Lambda$ . It appears that mergers and collisions during halo formation act as a "relaxation" mechanism to produce an equilibrium that is largely independent of initial conditions. This mechanism must operate rapidly since the similarity between profiles extends to the virial radius. These properties are characteristic of the "violent relaxation" process proposed by Lynden-Bell (1967) to explain the regularities observed in the structure of elliptical galaxies, and it is interesting to note that our universal profile is similar to the Hernquist profile that gives a good description of elliptical galaxy photometry. The two differ significantly only at large radii, perhaps because ellipticals are relatively isolated systems whereas dark halos are not. Syer & White (1996) suggest that a universal profile may be understood as a fixed point for a process of repeated mergers between unequal objects. Their analysis of this process predicts a dependence on the initial power spectrum that seems stronger, however, than that seen in our numerical data.

Our simulations suggest that the density profile of an isolated equilibrium halo can be specified quite accurately by giving two parameters: the halo mass and the halo characteristic density. Furthermore, in any particular hierarchical model, these parameters are related in such a way that the characteristic density is proportional to the mean cosmic density at the time when the mass of typical nonlinear objects was some fixed small fraction of the halo mass. The characteristic density thus reflects the density of the universe at the collapse time of the objects that merge to form the halo core. With this interpretation, we are able to fit the mass-density relation for equilibrium halos in all the cosmological models we have considered. In addition, it is possible to calculate the mass-density relation in any other hierarchical model (see the Appendix). It is difficult to

imagine a simpler situation—halos of all masses in all hierarchical cosmologies look the same, and their characteristic densities are just proportional to the cosmic density at the time they "formed."

Our results extend the radial range over which dark halo structure can reliably be determined to more than two decades. The central regions of our models have densities of order  $10^{6}\rho_{\mathrm{crit}}$ , comparable to those in the luminous parts of galaxies and in the central cores of galaxy clusters. As a result, a variety of direct observational tests of our predictions are available. In Navarro et al. (1996), we discussed several of these in the context of the standard CDM cosmogony—rotation curves of giant and dwarf galaxies, satellite galaxy dynamics, hot gaseous atmospheres around galaxies and in clusters, strong and weak gravitational lensing. All provide interesting constraints. We will not pursue these issues here, however, because they would take us too far from our primary goal, namely, the presentation of a simple and apparently general theoretical result: hierarchical clustering leads to a universal halo density profile just as it leads to universal distributions of halo axial ratios and halo spins; none of these properties depend strongly on the power spectrum, on  $\Omega$ , or on  $\Lambda$  (see Cole & Lacey 1996 and references therein). Of course, a comparison of the predicted halo structure with observation should provide strong constraints on the parameters that define particular hierarchical cosmogonies, and perhaps on the hierarchical clustering paradigm itself. We expect to come back to these issues in future work.

We are grateful for the hospitality of the Institute for Theoretical Physics of the University of California at Santa Barbara, where some of the work presented here was carried out. J. F. N. is also grateful for the hospitality of the Max-Planck-Institut für Astrophysik in Garching, Germany, where this project was started. In addition, he would like to acknowledge useful discussions with Cedric Lacey. Special thanks are due to Shaun Cole for making the data shown in Figure 9 available in electronic form. This work was supported in part by the PPARC and by the NSF under grant PHY94-07194 to the Institute for Theoretical Physics of the University of California at Santa Barbara.

# APPENDIX

# STEP-BY-STEP CALCULATION OF THE DENSITY PROFILE OF A DARK MATTER HALO

In this Appendix, we describe in detail the calculation of the parameters that specify the density profile of a dark halo of mass  $M$ . This calculation is applicable to Einstein-de Sitter  $(\Omega_0 = 1, \Lambda = 0)$ , open  $(\dot{\Omega}_0 < 1, \Lambda = 0)$ , and flat  $(\Omega_0 + \Lambda = 1)$  universes. We provide approximate fitting formulae that are valid for power-law and CDM initial density fluctuation spectra.

A halo of mass  $M$  identified at  $z = z_0$  can be characterized by its virial radius,

$$
r _ {2 0 0} = 1. 6 3 \times 1 0 ^ {- 2} \left(\frac {M}{h ^ {- 1} M _ {\odot}}\right) ^ {1 / 3} \left[ \frac {\Omega_ {0}}{\Omega (z _ {0})} \right] ^ {- 1 / 3} \left(1 + z _ {0}\right) ^ {- 1} h ^ {- 1} k p c, \tag {A1}
$$

or by its circular velocity,

$$
V _ {2 0 0} = \left(\frac {G M}{r _ {2 0 0}}\right) ^ {1 / 2} = \left(\frac {r _ {2 0 0}}{h ^ {- 1} \mathrm {k p c}}\right) \left[ \frac {\Omega_ {0}}{\Omega (z _ {0})} \right] ^ {1 / 2} \left(1 + z _ {0}\right) ^ {3 / 2} \mathrm {k m} \mathrm {s} ^ {- 1}. \tag {A2}
$$

The density profile of this system is fully specified by its characteristic density  $\delta_{c}$  and is given by (see eq. [1])

$$
\rho (r) = \frac {3 H _ {0} ^ {2}}{8 \pi G} \left(1 + z _ {0}\right) ^ {3} \frac {\Omega_ {0}}{\Omega \left(z _ {0}\right)} \frac {\delta_ {c}}{c x \left(1 + c x\right) ^ {2}}, \tag {A3}
$$

where  $x = r / r_{200}$  and  $c$  is the concentration parameter, a function of  $\delta_c$  given in equation (2). The corresponding circular velocity profile,  $V_{c}(r)$ , is given by

$$
\left[ \frac {V _ {c} (r)}{V _ {2 0 0}} \right] ^ {2} = \frac {1}{x} \frac {\ln (1 + c x) - (c x) / (1 + c x)}{\ln (1 + c) - c / (1 + c)}, \tag {A4}
$$

using the concentration  $c$  as a parameter.

The characteristic density is determined by the collapse redshift  $z_{\mathrm{coll}}$ , which is given by (see eq. [4])

$$
\frac {\delta_ {\mathrm {c r i t}} \left(z _ {\mathrm {c o l l}}\right)}{\delta_ {\mathrm {c r i t}} \left(z _ {0}\right)} = \frac {\delta_ {\mathrm {c r i t}} ^ {0} \left[ \Omega \left(z _ {\mathrm {c o l l}}\right) \right]}{\delta_ {\mathrm {c r i t}} ^ {0} \left[ \Omega \left(z _ {0}\right) \right]} \frac {D \left(z _ {0} , \Omega_ {0} , \Lambda\right)}{D \left(z _ {\mathrm {c o l l}} , \Omega_ {0} , \Lambda\right)} = 1 + \frac {0 . 4 7 7}{\delta_ {\mathrm {c r i t}} \left(z _ {0}\right)} \sqrt {2 \left[ \Delta_ {0} ^ {2} (f M) - \Delta_ {0} ^ {2} (M) \right]}. \tag {A5}
$$

Here  $D(z,\Omega_0,\Lambda)$  is the linear growth factor (normalized to unity at  $z = 0$ ) and can be written as

$$
D (z, \Omega_ {0}, \Lambda) = \left\{ \begin{array}{l l} 1 / (1 + z) & \text {i f} \Omega_ {0} = 1 \text {a n d} \Lambda = 0, \\ F _ {1} (w) / F _ {1} \left(w _ {0}\right) & \text {i f} \Omega_ {0} <   1 \text {a n d} \Lambda = 0, \\ F _ {2} (y) F _ {3} (y) / F _ {2} \left(y _ {0}\right) F _ {3} \left(y _ {0}\right) & \text {i f} \Omega_ {0} + \Lambda = 1, \end{array} \right. \tag {A6}
$$

where we have used the following auxiliary definitions:

$$
w _ {0} = \frac {1}{\Omega_ {0}} - 1, \tag {A7}
$$

$$
w = \frac {w _ {0}}{1 + z}, \tag {A8}
$$

$$
F _ {1} (u) = 1 + \frac {3}{u} + \frac {3 (1 + u) ^ {1 / 2}}{u ^ {3 / 2}} \ln \left[ (1 + u) ^ {1 / 2} - u ^ {1 / 2} \right], \tag {A9}
$$

$$
y _ {0} = \left(2 w _ {0}\right) ^ {1 / 3}, \tag {A10}
$$

$$
y = \frac {y _ {0}}{1 + z}, \tag {A11}
$$

$$
F _ {2} (u) = \frac {\left(u ^ {3} + 2\right) ^ {1 / 2}}{u ^ {3 / 2}}, \tag {A12}
$$

and

$$
F _ {3} (u) = \int_ {0} ^ {u} \left(\frac {u ^ {\prime}}{u ^ {\prime 3} + 2}\right) ^ {3 / 2} d u ^ {\prime}. \tag {A13}
$$

A good numerical approximation to the critical threshold for spherical collapse is given by

$$
\delta_ {\mathrm {c r i t}} ^ {0} (\Omega) = \left\{ \begin{array}{l l} 0. 1 5 (1 2 \pi) ^ {2 / 3} & \text {i f} \Omega_ {0} = 1 \text {a n d} \Lambda = 0, \\ 0. 1 5 (1 2 \pi) ^ {2 / 3} \Omega^ {0. 0 1 8 5} & \text {i f} \Omega_ {0} <   1 \text {a n d} \Lambda = 0, \\ 0. 1 5 (1 2 \pi) ^ {2 / 3} \Omega^ {0. 0 0 5 5} & \text {i f} \Omega_ {0} + \Lambda = 1, \end{array} \right. \tag {A14}
$$

which can be used to compute  $\delta_{\mathrm{crit}}(z_0) = \delta_{\mathrm{crit}}^0 [\Omega (z_0)] / D(z_0,\Omega_0,\Lambda)$ . Finally, equation (A5) requires  $\Delta_0^2 (M)$ , the variance of the power spectrum on mass scale  $M$ , extrapolated linearly to  $z = 0$ . In the case of a power-law spectrum of initial density fluctuations,  $P(k)\propto k^n$ , this is simply

$$
\Delta_ {0} ^ {2} (M) = \delta_ {\mathrm {c r i t}} ^ {0} \left[ \frac {M}{M _ {*} (z = 0)} \right] ^ {- (n + 3) / 6}, \tag {A15}
$$

where we have normalized the spectrum by  $M_{*}(z = 0)$ , the present nonlinear mass. A CDM spectrum is usually normalized by  $\sigma_{8}$ , the rms mass fluctuations within a sphere of radius  $8h^{-1}$  Mpc, and its variance can be approximated by

$$
\Delta_ {0} (M) = \sigma_ {8} F _ {4} \left(M _ {8}\right) / F _ {4} \left(M _ {h}\right), \tag {A16}
$$

where we have used the following definitions:

$$
M _ {8} = 6. 0 0 5 \times 1 0 ^ {1 4} \left(h \Omega_ {0}\right) ^ {3}, \tag {A17}
$$

$$
M _ {h} = \left(\frac {M}{h ^ {- 1} M _ {\odot}}\right) h ^ {3} \Omega_ {0} ^ {2}, \tag {A18}
$$

and

$$
F _ {4} (u) = A _ {1} u ^ {0. 6 7} \left[ 1 + \left(A _ {2} u ^ {- 0. 1} + A _ {3} u ^ {- 0. 6 3}\right) ^ {p} \right] ^ {1 / p}, \tag {A19}
$$

with  $A_{1} = 8.6594 \times 10^{-12}$ ,  $A_{2} = 3.5$ ,  $A_{3} = 1.628 \times 10^{9}$ , and  $p = 0.255$ .  
Equations (A6)-(A19) can be used to solve equation (A5) and find the collapse redshift,  $z_{\mathrm{coll}}$ , corresponding to a halo of mass  $M$ . As noted when discussing Figure 5, we recommend using  $f = 0.01$  when solving equation (A5), since this value seems to reproduce well the results of all our numerical experiments.  
Once  $z_{\mathrm{coll}}(M)$  has been found, the characteristic density of the halo (expressed in units of the critical density at  $z = z_0$ ) can be computed from (see eq. [5] and Table 1)

$$
\delta_ {c} \left(M, z _ {0}\right) \sim 3 \times 1 0 ^ {3} \Omega \left(z _ {0}\right) \left(\frac {1 + z _ {\mathrm {c o l l}}}{1 + z _ {0}}\right) ^ {3}, \tag {A20}
$$

where we have assumed  $f = 0.01$ .

A FORTRAN subroutine that implements the procedure described here and returns  $\delta_c(M, z_0)$  for all the cosmologies we discuss is available from the authors upon request.

# REFERENCES

Bertschinger,E.1985,ApJS,58,39  
Cole, S., & Lacey, C. 1996, MNRAS, in press (astro-ph 9510147)  
Crone, M., Evrard, A. E., & Richstone, D. O. 1994, ApJ, 434, 402  
Dubinski, J., & Carlberg, R. 1991, ApJ, 378, 496  
Efstathiou, G. P., Davis, M., Frenk, C. S., & White, S. D. M. 1985, ApJS, 57, 241  
Efstathiou, G. P., Frenk, C. S., White, S. D. M., & Davis, M. 1988, MNRAS, 235, 715  
Fillmore, J. A., & Goldreich, P. 1984, ApJ, 281, 1  
Frenk, C. S., White, S. D. M., Davis, M., & Efstathiou, G. P. 1988, ApJ, 327, 507  
Frenk, C. S., White, S. D. M., Efstathiou, G. P., & Davis, M. 1985, Nature, 317, 595  
Gunn,J.,&Gott,J.R.1972,ApJ,176,1  
Hernquist,L.1990,ApJ,356,359  
Hoffman,Y.1988,ApJ,328,489

Hoffman,Y.,&Shaham,J.1985,ApJ,297,16  
Lacey, C. G., & Cole, S. M. 1993, MNRAS, 262, 627  
Lynden-Bell, D. 1967, MNRAS, 136, 101  
Navarro, J. F., Frenk, C. S., & White, S. D. M. 1995, MNRAS, 275, 720  
1996,ApJ,462,563  
Navarro, J. F., & White, S. D. M. 1993, MNRAS, 265, 271  
Quinn, P. J., Salmon, J. K., & Zurek, W. H. 1986, Nature, 322, 329  
Syer, D., & White, S. D. M. 1996, MNRAS, submitted (astro-ph 9611065)  
Tormen, G., Bouchet, F. R., & White, S. D. M. 1997, MNRAS, 286, 865  
Warren, M. S., Quinn, P. J., Salmon, J. K., & Zurek, W. H. 1992, ApJ, 399, 405  
West, M. J., Dekel, A., & Oemler, A., Jr. 1987, ApJ, 316, 1  
White, S. D. M. 1996, in Les Houches Session LX, Cosmology and LargeScale Structure, ed. R. Schaeffer, J. Silk, M. Spiro, J. Zinn-Justin (Amsterdam: North Holland), 349  
Zurek,W.H.,Quinn,P.J.,&Salmon,J.K.1988,ApJ,330,519