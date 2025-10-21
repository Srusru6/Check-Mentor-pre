# Anderson Localization and Nonlinearity in One-Dimensional Disordered Photonic Lattices

Yoav Lahini, $^{1,*}$  Assaf Avidan, $^{1}$  Francesca Pozzi, $^{2}$  Marc Sorel, $^{2}$  Roberto Morandotti, $^{3}$  Demetrios N. Christodoulides, $^{4}$  and Yaron Silberberg $^{1}$

$^{1}$ Department of Physics of Complex Systems, The Weizmann Institute of Science, Rehovot, Israel  
 $^{2}$ Department of Electrical and Electronic Engineering, University of Glasgow, Glasgow, Scotland  
 $^{3}$ Institut national de la recherche scientifique, Université du Québec, Varennes, Québec, Canada  
 $^{4}$ CREOL/College of Optics, University of Central Florida, Orlando, Florida, USA  
(Received 19 April 2007; revised manuscript received 10 August 2007; published 10 January 2008)

We experimentally investigate the evolution of linear and nonlinear waves in a realization of the Anderson model using disordered one-dimensional waveguide lattices. Two types of localized eigenmodes, flat-phased and staggered, are directly measured. Nonlinear perturbations enhance localization in one type and induce delocalization in the other. In a complementary approach, we study the evolution on short time scales of  $\delta$ -like wave packets in the presence of disorder. A transition from ballistic wave packet expansion to exponential (Anderson) localization is observed. We also find an intermediate regime in which the ballistic and localized components coexist while diffusive dynamics is absent. Evidence is found for a faster transition into localization under nonlinear conditions.

DOI: 10.1103/PhysRevLett.100.013906

PACS numbers: 42.25.Dd, 42.65.Tg, 72.15.Rn

The propagation of waves in periodic and disordered structures is at the foundation of modern condensed-matter physics. Anderson localization is a key concept, formulated to explain the spatial confinement due to disorder of quantum mechanical wave functions that would spread over the entire system in an ideal periodic lattice [1-4]. Although Anderson localization was studied experimentally, the underlying phenomena—the emergence of localized eigenmodes and the suppression of wave packet expansion—were rarely observed directly [5,6]. Instead, localization was usually studied indirectly by measurements of macroscopic quantities such as conductance [2], backscattering [7,8], and transmission [9,10].

An interesting issue concerns the effect of nonlinearity on Anderson localization. Nonlinear interactions between the propagating waves and nonlinearly accumulated phases can significantly change interference properties, thus fundamentally affecting localization. The theoretical study of the nonlinear problem advanced using several approaches: the study of the transmission problem [11], the study of the effect of nonlinear perturbations on localized eigenmodes [12], and the study of the effect of nonlinearity on wave packet expansion in the presence of disorder [13]. Only a few experiments were reported [5]. Recently, optical studies enabled the study of wave evolution in nonlinear disordered lattices [14-16], using a scheme discussed in [17,18]. In particular, Schwartz et al. [16] reported the observation of Anderson localization of expanding wave packets in 2D lattices.

In this work we investigate directly linear and nonlinear wave evolution in one-dimensional (1D) disordered photonic lattices, using two different approaches. In the first part of this work, all the localized eigenmodes of a weakly disordered lattice are selectively excited. Nonlinearity is then introduced in a controlled manner, to examine its effect on localized eigenmodes. The second part of this

work presents a study of the effect of disorder on the evolution of  $\delta$ -like wave packets (single site excitations). A transition from free ballistic wave packet expansion to exponential localization is observed, as well as an intermediate regime of coexistence. We then measure the effect of nonlinearity on this process.

Our experimental setup is a one-dimensional lattice of coupled optical waveguides patterned on an AlGaAs substrate [19,20], illustrated in Fig. 1(a). Light is injected into one or a few waveguides at the input and can coherently tunnel between neighboring waveguides as it propagates along the  $z$  axis. Light distribution is then measured at the output [see, for example, Fig. 1(b)-1(d)].

The equations describing light dynamics in these structures are identical (in the linear limit) to the equations describing the time evolution of a single electron in a lattice under the tight binding approximation [19], i.e., a set of coupled discrete Schrödinger equations:

![](images/8eae5e40bab4da65bf32842b62473f845c210c9e4c298288b960adc218e77f31.jpg)  
FIG. 1 (color online). (a) Schematic view of the sample used in the experiments. The red arrow indicates the input beam. (b)-(d) Images of output light distribution, when the input beam covers a few lattice sites: (b) in a periodic lattice, (c) in a disordered lattice, when the input beam is coupled to a location which exhibits a high degree of expansion, and (d) in the same disordered lattice when the beam is coupled to a location in which localization is clearly observed.

$$
- i \frac {\partial U _ {n}}{\partial z} = \beta_ {n} U _ {n} + C _ {n, n \pm 1} \left(U _ {n + 1} + U _ {n - 1}\right) + \gamma | U _ {n} | ^ {2} U _ {n}. \tag {1}
$$

Here  $n = 1, \dots, N$ , where  $N$  is the number of lattice sites (waveguides),  $U_{n}$  is the wave amplitude at site  $n$ ,  $\beta_{n}$  is the eigenvalue (propagation constant) associated with the  $n$ th site,  $C_{n,n\pm 1}$  are the tunneling rates between two adjacent sites, and  $z$  is the longitudinal space coordinate. The last term in Eq. (1) describes the nonlinear dependence of the refractive index on the light intensity, where  $\gamma$  is the Kerr parameter, positive for our system  $(\gamma > 0)$ . The nonlinear term can be discarded for low light intensities. For typical experimental parameters see, for example, [20].

Disorder is introduced to the lattice by randomly changing the width of each waveguide in a finite range  $W \pm \delta$  where  $W$  is the mean value (typically  $4\mu \mathrm{m}$  in our samples). The parameters  $\beta_{n}$  and  $C_{n,n\pm 1}$  can be calculated numerically from the waveguides' width and from the separation between neighboring waveguides. As a result of disorder the parameters  $\beta_{n}$  become random in the range  $\beta_{0} \pm \Delta$ . By keeping the lattice periodic on average (the site's centers still have the lattice periodicity), the parameters  $C_{n,n\pm 1}$  become independent of  $n$  to a very good approximation, meeting the conditions assumed by Anderson in his original model (diagonal disorder) [1]. A measure of disorder is then given by the ratio  $\Delta / C$  [4].

We now turn to the first set of experiments, designed to excite and measure individually all the localized eigenmodes of a disordered lattice, and to study the effect of nonlinear perturbations on them. For this purpose we have fabricated a lattice with  $N = 99$  sites and disorder level  $\Delta /C = 1$ . The disordered lattice eigenmodes and eigenvalues can be calculated by diagonalizing a set of  $N$  equations (1) in the linear limit, substituting the calculated values of  $\beta_{n}$  and  $C_{n,n\pm 1}$  for this specific realization. Results are shown in Fig. 2(a). The resulting band of

eigenvalue deviates only slightly from the cosine-shaped band of a perfectly ordered lattice [19]. Several eigenmodes with eigenvalues near the edges of the band become exponentially localized in space, even though the density of states near the band edges is not significantly lower from the one at the band center [4]. Localized eigenmodes near the bottom of the band are flat phased; i.e., their wave functions amplitude is in phase at all sites (see inset 1)[21], while the localized eigenmodes at the top of the band are staggered; i.e., their wave function's amplitude has a  $\pi$  phase flip between adjacent sites (inset 2). Notably, these localized eigenmodes are localized at well-separated regions in space and have a similar width of about 10 lattice sites. Eigenmodes near the band center remain extended in the finite system (see inset 3). These modes will be localized in an infinite system, but on a much larger length scale [22]. As disorder  $(\Delta /C)$  is increased, a larger fraction of the modes becomes localized within the finite lattice.

In order to excite localized eigenmodes of this lattice we inject a wide beam (covering several lattice sites) at different locations across the lattice. At some input positions, we observe significant expansion of the beam at the output, similar in width to the expansion observed in a periodic lattice with the same average parameters [see Figs. 1(b) and 1(c)]. At specific locations, however, wave expansion is suppressed and prominent localization is evident [Fig. 1(d)]. In these cases, the input beam overlap significantly with a single localized eigenmode of the lattice, while the overlap with the other modes of the lattice is eliminated. Optimized localized output distributions were achieved using an input beam that covers about 10 lattice sites, corresponding to the typical width of the localized eigenmodes in this disorder level.

While scanning the input position we observe several localized light distributions at the output. We compare the obtained localized intensity profiles to calculated localized eigenmodes of the lattice in Fig. 2(b). There is a clear

![](images/d4effcdb2f9e844d033a2213b57c9773e54bc7869b790f2fa604ec0495f63267.jpg)  
FIG. 2 (color online). Measurements of localized eigenmodes of a disordered lattice. (a) Calculated eigenmodes and eigenvalues of the weakly disordered lattice used in the experiments. The band of eigenvalues deviates slightly from the cosine-shaped band of a periodic lattice. Localized modes are formed, associated with eigenvalues near the edges of the band (insets 1,2), while modes near the band center remain extended (inset 3). (b) Measurements of pure flat-phase Anderson localized modes. Panels show a comparison between measurements (blue) and the corresponding calculated eigenmodes of the lattice (red). (c) Same for staggered localized eigenmodes. In all cases no fitting procedures are used.

![](images/bc8eb429a46aac60224d10586c2b6a1b984c7d57a5babe647394876ec86951df.jpg)

![](images/d8c96a233e9d31f176c36f21e7d587064bc1cd7ca383f611adbe5d5e83abfbd1.jpg)

![](images/bb4ff38a0579bd4ddc83ec570ab7fed8744512ab2cc486588598acde808b203b.jpg)  
FIG. 3 (color online). The effect of weak nonlinearity on pure localized eigenmodes: cross sections of the output light intensities (horizontal axis) at different power levels (vertical axis), showing that (a) flat phased localized modes tend to become more localized as nonlinearity is increased, while (b) staggered localized modes tend to delocalize. All cross sections are normalized to unit maximum.

correspondence between the experimentally observed localizations and the location and shape of all the calculated flat phased localized eigenmodes associated with the bottom of the eigenvalue band. To excite the staggered modes associated with the top of the band, the input beam was tilted with respect to the lattice to induce a  $\pi$  phase difference in the excitation of adjacent waveguides [19]. The results of this excitation scheme are presented in Fig. 2(c). Again, a clear correspondence is found to the calculated localized staggered modes of the lattice. These results demonstrate the ability to excite pure Anderson localized eigenmodes.

The effect of nonlinear perturbations on localized eigenmodes is studied by exciting a pure localized mode and increasing the input beam power. The intensities are kept way below those required to exhibit self-focusing in a periodic lattice with the same average parameters [20],

keeping the experiments in the weak nonlinear regime. Some localized modes are found to exhibit significant response to nonlinearity. The results of two such experiments are shown in Fig. 3, showing that weak positive nonlinearity tends to further localize flat phased localized modes, but tends to delocalize staggered modes.

These results can be understood on the basis of the theory developed in [12], which have shown that nonlinear shifts of a localized eigenmode's frequency (represented here by the parameter  $\beta$ ) can lead to delocalization if the frequency crosses a resonance with other modes of the lattice. This condition can be satisfied in the case of weak disorder for the staggered localized modes, as nonlinearity shifts them from the edge of the band into the linear spectrum. Conversely, the flat phased modes at the other edge of the band are shifted by nonlinearity out of the linear spectrum; thus, they remain localized (see also discussion in [15]).

We now turn to the second set of experiments, aimed to study the effect of disorder on wave packet evolution in the linear and nonlinear regimes. This aspect is studied by injecting light into a single lattice site, thus exciting a tight  $\delta$ -like wave packet of all eigenmodes having nonvanishing overlap with the excited site. The wave packet then evolves in the lattice, and the light distribution is measured at the output. We average the output patterns obtained, by separately exciting each site in the lattice while keeping the measurement window centered about the input site position. The results of such measurements in the linear regime, taken in 5-mm-long samples with different disorder levels, are shown in Fig. 4(a)–4(d). Without disorder, single site excitation results in ballistic propagation (wave packet width grows linearly with time), recognized

![](images/4aa786a4bf1989caec0816239c37c86be91d55e016beefa3fc2ef9d527866bc1.jpg)  
FIG. 4 (color online). The effect of disorder on wave packet expansion in the linear and the nonlinear regimes. The results shown are normalized lattice averages of the output light distribution, when initially a single site is excited (see discussion in the text). A measure of localization is given by the mean square displacement from the input site  $\sigma$ , and by the intensity at the origin site  $I_{o}$ . (a)-(d) Measurements in the linear case show the transition from ballistic transport to exponential (Anderson) localization as a function of disorder in: (a)  $\Delta / C = 0$ , (b)  $\Delta / C = 1$ , (c)  $\Delta / C = 1.5$ , and (d)  $\Delta / C = 3$ . Note the transition from ballistic transport in (a) to localization in (d) through the buildup of a central component and the suppression of the ballistic side lobes. Inset in (d) shows the localized distribution in semilog scale, demonstrating the exponential tails. (e)-(h) Measurements of the same lattices in the nonlinear case, showing that on average nonlinearity tends to increase localization for intermediate disorder levels [e.g., compare (b) and (f)].

by a characteristic signature of two separated lobes [19,20] [Fig. 4(a)]. At moderate disorder, a second component emerges, localized around the input site position [Fig. 4(b) and 4(c)]. The localized and the ballistic components coexist in this regime. At high disorder a highly localized, exponentially decaying distribution is observed [Fig. 4(d)]. This exponential decay of the expansion profile is a hallmark of Anderson localization.

These results offer a first direct look at the short time evolution of wave packets in 1D disordered systems. It is known that for infinite disordered 1D systems and for long time scales, wave packet expansion is always fully suppressed. However, on short time scales, wave packets do evolve [17,23]. The results in Fig. 4(a)–4(d) reveal how localization is reached in the 1D case; localization emerges from ballistic expansion through the continues buildup of a localized component and the suppression of a ballistic component. This dynamics is fundamentally different from the one observed in 2D systems [15,16], or that was indirectly measured in quasi-1D experiments [10]. In these cases the expansion turns quickly from ballistic to diffusive and becomes localized after much longer propagation times. In the 1D case the diffusive dynamics is absent, as discussed, for example, in [23].

To study the effect of nonlinearity on wave packet expansion we repeat these measurements at increased light intensities. Again, we remain in the weak nonlinear regime. Results are shown in Fig. 4(e)–4(h). On average, the results indicate increased localization at intermediate disorder levels; the intensity in the ballistic component is lower and the intensity in the localized component is higher under nonlinear conditions. This suggests that the buildup of the localized component and the suppression of the ballistic component happen faster under nonlinear conditions. This description holds for short time scales in which the ballistic component is still present. On much longer time scales, subdiffusive delocalization due to nonlinearity was predicted to take over [13].

In conclusion, we have directly studied localized eigenmodes and wave packet expansion in disordered 1D lattices that are described by the nonlinear version of the Anderson model. Two types of localized eigenmodes were measured, and nonlinear perturbations were shown to enhance localization in one type and induce delocalization in the other. The study of the expansion of wave packets on short time scales in the presence of disorder has enabled a direct measurement of the transition from ballistic wave packet expansion to exponential localization. It was shown that in 1D systems a ballistic and a localized component can coexist at intermediate times, while diffusive wave packet expansion, observed in 2D and quasi-1D systems, is absent in the 1D case. In the nonlinear regime, evidence is found for a faster transition into localization under nonlinear conditions.

We thank Y. Imry, M. Aizenman, and H. S. Eisenberg for useful discussions. This work was supported by the

German-Israeli Project Cooperation (DIP), NSERC and CIPI (Canada), and EPRSC (UK). Y.L. is supported by the Adams Program of the Israel Academy of Sciences and Humanities.

*yoav.lahini@weizmann.ac.il  
[1] P.W. Anderson, Phys. Rev. 109, 1492 (1958).  
[2] P.A. Lee and T.V. Ramakrishnan, Rev. Mod. Phys. 57, 287 (1985).  
[3] S. John, Phys. Rev. Lett. 53, 2169 (1984).  
[4] P. Sheng, Introduction to Wave Scattering, Localization, and Mesoscopic Phenomena (Springer, New York, 2006).  
[5] J.D. Maynard, Rev. Mod. Phys. 73, 401 (2001).  
[6] R. Dalichaouch et al., Nature (London) 354, 53 (1991); K. Yu. Bliokh et al., Phys. Rev. Lett. 97, 243904 (2006).  
[7] M.P. VanAlbada and A. Lagendijk, Phys. Rev. Lett. 55, 2692 (1985); P.E. Wolf and G. Maret, Phys. Rev. Lett. 55, 2696 (1985); E. Akkermans and R. Maynard, J. Phys. Lett. 46, L1045 (1985).  
[8] X. Zhang and Z.Q. Zhang, Phys. Rev. B 65, 155208 (2002); 65, 245115 (2002).  
[9] M.V. Berry and S. Klein Sheng, Eur. J. Phys. 18, 222 (1997); D.S. Wiersma et al., Nature (London) 390, 671 (1997); A.A. Chabanov et al., Nature (London) 404, 850 (2000); M. Storzer et al., Phys. Rev. Lett. 96, 063904 (2006).  
[10] A. A. Chabanov and A. Z. Genack, Phys. Rev. E 56, R1338 (1997); A. Garcia-Martin et al., Appl. Phys. Lett. 71, 1912 (1997); Phys. Rev. Lett. 84, 3578 (2000).  
[11] A. Trombettoni et al., Phys. Rev. Lett. 88, 173902 (2002); K.O. Rasmussen et al., Europhys. Lett. 47, 421 (1999); S.A. Gredeskul and Y.S. Kivshar, Phys. Rep. 216, 1 (1992); B. Doucot and R. Rammal, Europhys. Lett. 3, 969 (1987); P. Devillard and B. Souillard, J. Stat. Phys. 43, 423 (1986).  
[12] G. Kopidakis and S. Aubry, Phys. Rev. Lett. 84, 3236 (2000); Physica (Amsterdam) 139D, 247 (2000); 130D, 155 (1999); C. Albanese and J. Frohlich, Commun. Math. Phys. 138, 193 (1991).  
[13] D.L. Shepelyansky, Phys. Rev. Lett., 70, 1787 (1993); M.I. Molina, Phys. Rev. B 58, 12547 (1998); T. Kottos and M. Weiss, Phys. Rev. Lett. 93, 190604 (2004); A.P. Pikovsky and D.L. Shepelyansky, arXiv:0708.3315; G. Kopidakis et al., arXiv:0710.2621.  
[14] H. S. Eisenberg, Ph.D. thesis, Weizmann Institute, 2002.  
[15] T. Pertsch et al., Phys. Rev. Lett. 93, 053901 (2004).  
[16] T. Schwartz et al., Nature (London) 446, 52 (2007).  
[17] H. De Raedt et al., Phys. Rev. Lett. 62, 47 (1989).  
[18] S.S. Abdullaev and F.Kh. Abdullaev, Izvestiya Vuz. Radiofizika 23, 766 (1980).  
[19] D.N. Christodoulides et al., Nature (London) 424, 817 (2003).  
[20] H. S. Eisenberg et al., Phys. Rev. Lett. 81, 3383 (1998).  
[21] The band here is inverted in respect to the usual convention in waveguide lattices.  
[22] A.R. McGurn et al., Phys. Rev. B 47, 13120 (1993).  
[23] F.M. Izrailev et al., Phys. Rev. E 55, 4951 (1997); E.P. Nachmedov et al., Sov. Phys. JETP 65, 1202 (1987).