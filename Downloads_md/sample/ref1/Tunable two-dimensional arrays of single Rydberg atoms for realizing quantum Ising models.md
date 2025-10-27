# Tunable two-dimensional arrays of single Rydberg atoms for realizing quantum Ising models

Henning Labuhn $^{1*}$ , Daniel Barredo $^{1*}$ , Sylvain Ravets $^{1}$ , Sylvain de Leseleuc $^{1}$ , Tommaso Macri $^{2}$ , Thierry Lahaye $^{1}$  & Antoine Browaeys $^{1}$

Spin models are the prime example of simplified many-body Hamiltonians used to model complex, strongly correlated real-world materials<sup>1</sup>. However, despite the simplified character of such models, their dynamics often cannot be simulated exactly on classical computers when the number of particles exceeds a few tens. For this reason, quantum simulation<sup>2</sup> of spin Hamiltonians using the tools of atomic and molecular physics has become a very active field over the past years, using ultracold atoms<sup>3</sup> or molecules<sup>4</sup> in optical lattices, or trapped ions<sup>5</sup>. All of these approaches have their own strengths and limitations. Here we report an alternative platform for the study of spin systems, using individual atoms trapped in tunable two-dimensional arrays of optical microtraps with arbitrary geometries, where filling fractions range from 60 to 100 per cent. When excited to high-energy Rydberg D states, the atoms undergo strong interactions whose anisotropic character opens the way to simulating exotic matter<sup>6</sup>. We illustrate the versatility of our system by studying the dynamics of a quantum Ising-like spin-1/2 system in a transverse field with up to 30 spins, for a variety of geometries in one and two dimensions, and for a wide range of interaction strengths. For geometries where the anisotropy is expected to have small effects on the dynamics, we find excellent agreement with ab initio simulations of the spin-1/2 system, while for strongly anisotropic situations the multilevel structure of the D states has a measurable influence<sup>7,8</sup>.

Our findings establish arrays of single Rydberg atoms as a versatile platform for the study of quantum magnetism.

Rydberg atoms have recently attracted a lot of interest for quantum information processing and quantum simulation. In this work, we use individual Rydberg atoms to realize quantum Ising magnets, with unprecedented flexibility in the geometry of the arrays. By shining on the atoms lasers that are resonant with the transition between the ground state  $|g\rangle$  and a chosen Rydberg state  $|r\rangle$  (Fig. 1a), we implement the Ising-like Hamiltonian

$$
H = \sum_ {i} \frac {\hbar \Omega}{2} \sigma_ {x} ^ {i} + \sum_ {i <   j} V _ {i j} n ^ {i} n ^ {j} \tag {1}
$$

which acts on the pseudo-spin states  $|\downarrow \rangle_{i}$  and  $|\uparrow \rangle_{i}$  corresponding to states  $|g\rangle$  and  $|r\rangle$  of atom  $i$ , respectively. Here,  $\Omega$  is the Rabi frequency of the laser coupling, the  $\sigma_{\alpha}^{i} (\alpha = x, y, z)$  are the Pauli matrices acting on atom  $i$ , and  $n^{i} = (1 + \sigma_{z}^{i}) / 2$  is the number of Rydberg excitations (0 or 1) on site  $i$ . The term  $V_{ij}$  arises from the van der Waals interaction between atoms  $i$  and  $j$  when they are both in  $|r\rangle$ , and scales as  $C_6(\theta)|\boldsymbol{r}_i - \boldsymbol{r}_j|^{-6}$  with the separation between the atoms  $\boldsymbol{r}_i - \boldsymbol{r}_j$ . Moreover, for  $|r\rangle = |n\mathrm{D}_{3/2}, m_j = 3/2\rangle$ , the van der Waals coefficient  $C_6$  is anisotropic[7,11], varying by  $\sim 3$  when the angle  $\theta$  between the interatomic axis and the quantization axis  $\hat{z}$  changes from 0 to  $\pi/2$  (Fig. 1a

![](images/d35ecd5af5a26750ad813daceb9a30b71e2a3922ea94b1a6937dd9c3e6e700c6.jpg)

![](images/efb0feb610aa9cb54d52687924945e2f1da9274fc1672cce924e2f7e0fd4c349.jpg)

![](images/2581c2986db9c3bca8adfd8451fcebd6ef6f9cf85c5f7001621288eac1cf3d6c.jpg)

![](images/7ec698ed1cfd2d9b47c81b2be9daf84b7da765bf8e6382b713d38c5e295f013d.jpg)  
Figure 1 | Many-body dynamics of Rydberg atoms and experimental platform. a, Rydberg blockade between two atoms (main panel, lower right), each considered as a two-level system (grey inset): owing to strong interactions between the Rydberg states  $|r\rangle$ , the excitation of two nearby atoms (within the blockade radius  $R_{\mathrm{b}}$ ) is inhibited. The use of  $n\mathrm{D}_{3/2}$  states for  $|r\rangle$  gives rise, when the description of the atoms is reduced to a two-level model, to an anisotropic effective van der Waals potential  $C_6(\theta)/R^6$  (see inset). b, For a value of  $R_{\mathrm{b}}$  comparable to the distance between adjacent atoms (top), the dynamics becomes richer. Configurations where two neighbouring atoms are excited are energetically forbidden (red crosses), yielding strong correlations between the Rydberg excitations in the allowed configurations (green ticks). c, An array of microtraps is created by imprinting an appropriate phase on a dipole-trap beam. Site-resolved fluorescence of the atoms, at  $780\mathrm{nm}$ , is imaged on an electron-multiplying charge-coupled device (EMCCD) camera using a dichroic mirror (DM). Rydberg excitation beams at 795 and  $475\mathrm{nm}$  are shone onto the atoms. Inset, measured light intensity for an array of  $N_{\mathrm{t}} = 19$  traps.

![](images/c03070a311e56fefa91a5c8b89a75fc823bbd1b60d79cc1e0f8a71ccf30628b2.jpg)

![](images/532a1129733eacdeaa82c6adc5b52bbd14abbbfb13c36e4c9f4872c556227364.jpg)

![](images/b348f31779ddeecaf56ac145abd0167248524b32a9b96fb84c048f22ad9706ba.jpg)

![](images/12f2a850093de585bd481a27d7284f943af5f0af4f01016022e7e0e6b25af69b.jpg)  
Figure 2 | Collective oscillations in the full Rydberg blockade regime. a, Probability  $P_0$  for all  $N$  atoms to be in  $|g\rangle$  after an excitation pulse of area  $\Omega\tau$ , for five values of  $N$  from 1 to 15. Red points, fully loaded arrays,  $n = 82$ ; blue points, partially loaded triangular arrays of  $N_{\mathrm{t}} = 19$  traps,  $n = 100$  (error bars show the quantum projection noise for  $\sim 100$  repetitions of the experiment). Solid lines are fits by damped sines of frequency  $\Omega_N$ . The right panels depict the atomic positions. b, Collective oscillation frequency  $\Omega_N / \Omega$  versus  $N$  (error bars, sometimes smaller than the symbol size, are s.d.; colour code for points as in a). The solid line is the expected  $\sqrt{N}$  enhancement.

inset). The strong interactions between the Rydberg states induce correlations in the positions of the excitations (Fig. 1b), as we study experimentally below.

Our set-up (Fig. 1c) has been described in refs 12 and 13. We trap cold  $(T\approx 30\mu \mathrm{K})$  single  $^{87}\mathrm{Rb}$  atoms in optical traps with a  $1\mu \mathrm{m}$  waist from a magneto-optical trap (MOT). Using a spatial light modulator (SLM), we create arbitrary, two-dimensional arrays containing  $1\leq N_{\mathrm{t}}\leq 50$  traps, separated by distances  $a > 3\mu \mathrm{m}$ . The atomic fluorescence at  $780\mathrm{nm}$  is imaged onto a camera. We observe, in the single-atom regime<sup>12</sup>, that the level of fluorescence for each trap alternates randomly between two levels, corresponding to the presence of 0 or 1 atom. The analysis of these  $N_{\mathrm{t}}$  fluorescence traces allows us to record, with a time resolution of  $50\mathrm{ms}$ , the current number  $N$  of single atoms in the array.

As soon as  $N$  exceeds a predefined threshold, we trigger the following experimental sequence. First, the loading of the array is stopped, and a fluorescence image is acquired to record the initial configuration of the atoms, that is, which traps are filled. A 6 G magnetic field is then switched on along the  $z$  axis and defines the quantization axis. After initializing all the atoms in  $|g\rangle = |5S_{1 / 2},F = 2,m_F = 2\rangle$  by optical pumping, a two-photon Rydberg excitation pulse of duration  $\tau$  is shone onto the atoms; the Rabi frequency  $(\varOmega\approx 2\pi\times 1\mathrm{MHz})$  is uniform to within  $10\%$  over the array. We then acquire a fluorescence image of the final

configuration by switching on the MOT beams. Atoms excited to  $|r\rangle$  quickly escape the trapping region, and thus we observe only the atoms that were in  $|g\rangle$  after excitation. The atoms that have been lost between the initial and final images are thus assigned to Rydberg states. This detection method has a high efficiency: it only gives a small number of 'false positives', as an atom also has a probability  $\varepsilon \approx (3\pm 1)\%$  of being lost, independently of its internal state (Methods).

We first test our system in the conceptually simple situation of fully Rydberg-blockaded ensembles (that is, with at most one Rydberg excitation) containing up to  $N = 15$  atoms. Figure 2a shows, for various arrays, the probability  $P_0$  that all  $N$  atoms are in  $|g\rangle$  at the end of the sequence. We observe high-contrast coherent oscillations, with a frequency enhanced by a factor  $\sqrt{N}$  with respect to the single-atom case (Fig. 2b). This characteristic collective oscillation is the hallmark of Rydberg blockade[14-17], where multiple excitations are inhibited within a blockaded volume (which, owing to the anisotropy, is close to an ellipsoid, with a major radius  $R_{\mathrm{b}}$  defined by  $\hbar \varOmega = |C_6(0)| / R_{\mathrm{b}}^6$ , and a small 'flattening'  $3^{1/6} \approx 1.2$ ). This observation is a first step towards the creation of long-lived  $|W\rangle$  entangled states (the symmetric combination of the  $N$  states with a single excitation) in the ground state[9].

The fully blockaded regime remains easy to describe theoretically as the blockade naturally truncates the size of the Hilbert space. In contrast, a more challenging regime corresponds to the Rydberg blockade being effective only between nearest neighbours, such that for long enough excitation times, the number of excitations becomes  $\sim N / 2$ . It is therefore desirable to be able to vary the ratio  $\alpha = R_{\mathrm{b}} / a$  of the blockade radius to the distance  $a$  between sites: for very small or large values of  $\alpha$ , the dynamics is simple and the system can easily be compared to numerics, while, for intermediate values of  $\alpha$ , the dynamics is challenging to calculate and experimental quantum simulation becomes relevant. Our set-up is particularly adapted to this goal, as we can vary easily both  $a$  (reconfiguring the SLM) and  $R_{\mathrm{b}}$  (changing the principal quantum number  $n$ , we tune  $C_6$  which scales approximately as  $n^{11}$ ).

This versatility is illustrated in Fig. 3, where we use a fully loaded ring-shaped array of  $N = 8$  traps, thus realizing a small spin chain with periodic boundary conditions (PBC). By varying both  $a$  and  $n$ , we tune the system all the way from independent atoms  $(\alpha \ll 1)$ , where each atom undergoes a Rabi oscillation at frequency  $\Omega$ , resulting in a Rydberg fraction  $f_{\mathrm{R}}$  (defined as the average number of Rydberg excitations divided by  $N$ ) periodically reaching  $\sim 1$  (Fig. 3a), to a fully blockaded array  $(\alpha \gg 1$ , Fig. 3c) characterized by collective oscillations at frequency  $\sqrt{N} \Omega$  and a maximum  $f_{\mathrm{R}} = 1 / N$ . In between (Fig. 3b, where  $\alpha \approx 1.5$ ), the evolution of  $f_{\mathrm{R}}(\tau)$  shows oscillations resulting from the beating of the incommensurate eigenfrequencies of the many-body Hamiltonian, equation (1). Our system allows us to detect the state of each atom, and thus to measure correlation functions. Figure 3d shows the dynamics of the Rydberg-Rydberg pair correlation function:

$$
g ^ {(2)} (k) = \frac {1}{N _ {\mathrm {t}}} \sum_ {i} \frac {\left\langle n _ {i} n _ {i + k} \right\rangle}{\left\langle n _ {i} \right\rangle \left\langle n _ {i + k} \right\rangle} \tag {2}
$$

The averaging over all traps does not wash out correlations despite the fact that the system is not fully invariant by translation (Methods). We observe a strong suppression of  $g^{(2)}(k)$  for  $k = 1$  and  $k = 7$ , that is, a clear signature of nearest-neighbour blockade. For some times (see for example,  $\Omega \tau = 3.1$ ), we observe an antiferromagnetic-like staggered correlation function, while the average density is uniform (Methods).

The solid lines in all panels of Fig. 3 are obtained by solving the Schrödinger equation governed by equation (1) using the independently measured experimental parameters, and then including the effects of the finite detection errors  $\varepsilon$  (Methods). One observes an overall agreement with the data, although some small discrepancies can clearly be noticed, especially at longer times. We attribute them to the Zeeman structure of Rydberg D states, which is not taken into account in our modelling by a spin-  $1 / 2$ : for  $\theta \neq 0$ , the van der Waals interaction

![](images/2a1ec7f779597cbc728a4f15ac199ac4247bc312c98e0484d222a0dc0e88e9d3.jpg)  
a

![](images/5174f289a02ad0cab02d27286c8ef5d1e0209c10d054bb788964bf0074cfbb59.jpg)  
b

![](images/2f712653a75983f7dc5267d47779282b1cc0d3600cf708c9b61e851d209fbdbb.jpg)  
Figure 3 | Tuning interactions in an eight-spin chain with PBC. a, Independent atoms  $(R_{\mathrm{b}} < a)$ . Right, the Rydberg fraction  $f_{\mathbb{R}}$  oscillates between  $\sim 0$  and  $\sim 1$  with the single-atom Rabi frequency  $\Omega$ . b, Strongly correlated regime  $(R_{\mathrm{b}} \approx 1.5a)$ . Right, the Rydberg fraction shows an oscillatory behaviour involving several frequencies. c, Fully blockaded regime:  $f_{\mathbb{R}}$  oscillates at  $\sqrt{N}\Omega$  (right), and reaches a maximum of  $1/N$ . In a-c, the left diagram shows the eight spin chain, and the shaded ellipsoids illustrate the (anisotropic) blockade volume. d, The Rydberg-Rydberg pair correlation function, for the parameters of b, is shown for increasing values of  $\Omega\tau$  (top to bottom). In all plots, the solid lines are obtained by numerically solving the time-dependent Schrödinger equation, and then including detection errors ( $\varepsilon = 3\%$ ). Error bars (often smaller than symbol size) denote s.e.m.

![](images/94349959c2933a25d42b40f12527aa0d7bc596268813cc426d3a8f60c57b5c9c.jpg)

![](images/215a1b994a455ad8f9290e56feafc44720320d55f80c52c91a37b1a5507e9ee9.jpg)  
C

![](images/474e7005cf960d644941280f35986350e5ffead7885739ed272c3a9e22d2b329.jpg)

![](images/00a03baed1457329b1a322969719dc2c986c2122fbb26b4b76c8fd2844565906.jpg)

![](images/e07469d8c3cfad47331ed4edb53efdd24f4fdec86714a807cc314ffb72d0ab44.jpg)

![](images/e18276cd15a3bc4f069aa61c7090eade10a84797838c501ce0ec2d790e9d8017.jpg)

![](images/5e3fcb7bf4ae735278130e149db9612ee28b098daca7f99ec4f69067ae413529.jpg)

![](images/f34ee8b384582f293522c338738e5cf399030e442c761fb76d539a6ebf98bb5d.jpg)

couples  $|r\rangle$  to other Zeeman states, leading to a slow increase in the number of excitations (Methods).

We now study two systems containing a larger number of atoms. We first consider a one-dimensional spin chain with PBC comprising  $N_{\mathrm{t}} = 30$  traps and partially loaded with  $N = 20 \pm 1.5$  atoms (Fig. 4a; we have checked that the  $67\%$  filling fraction does not change qualitatively the physics as compared to a perfect filling, see Methods). Its 'racetrack' shape was chosen to optimize homogeneity of the Rabi frequency over

the array. We chose parameters such that  $\alpha \approx 4.3(1)$ . The Rydberg fraction  $f_{\mathrm{R}}(\tau)$  shows initial oscillations before reaching a steady state (Fig. 4b) due to the dephasing of the many incommensurate eigenfrequencies of equation (1) for this large value of  $N$ . The pair correlation function (shown in Fig. 4c for  $\Omega \tau \approx 2.0$ ) is strongly suppressed for  $k < \alpha$ , as expected from blockade physics, before oscillating towards the asymptotic value  $g^{(2)}(k \gg a) = 1$  (refs 18, 19). A similar liquid-like correlation function has been observed in two dimensions[20]. The solid

![](images/025c8b3eb8186180408767fed6cbf59a5643e818f9de5192c0f6776713399af0.jpg)  
d

![](images/63d5dca1a3f1724c0dd93370fc762bd4ad36644b601556f015b4f95e20e60f52.jpg)

![](images/2b21d1eea4f4193faed28fe7a1f0f5bca1944b1c5a0f057e409805eb61bb40b9.jpg)  
Figure 4 | Ising dynamics in large spin ensembles. a, Racetrack-shaped array with  $N_{\mathrm{t}} = 30$  traps, loaded with  $N = 20 \pm 1.5$  atoms. The blockade radius  $R_{\mathrm{b}}$  is about  $4.3a$  (shaded ellipsoid). b, c, Properties of system shown in a. b, Time evolution of the Rydberg fraction  $f_{\mathrm{R}}$ . c, Rydberg pair correlation function  $g^{(2)}(k)$  for  $\Omega \tau \approx 2.0$ , showing a strong depletion for  $k < R_{\mathrm{b}}$  and contrasted oscillations around the asymptotic value 1 (the data are shown only for  $k > 0$ , as they are symmetric under the transformation  $k \rightarrow -k$ ). Error bars (most of the time smaller than symbol size) denote the s.e.m. Solid lines are the simulation results without any adjustable parameters. d, Square array of  $7 \times 7$  traps loaded with  $N = 28 \pm 1.6$  atoms. The blockade radius is about  $2.6a$ . e, f, Properties of system shown in d. e, Evolution of  $f_{\mathrm{R}}$ . Error bars (most of the time smaller than symbol size) denote s.e.m. Solid lines are the simulation results without any adjustable parameters. f, Rydberg-Rydberg correlation function  $g^{(2)}(k,l)$  for  $\Omega \tau = 5.3$ .

![](images/5326736508e5c5f0b03b17dbc5fd577d8852037860cbfc5643ff109b9277c34f.jpg)

![](images/03fc8253c230ab6c80da3af87125e60706200d8835f5e90f9e4ff4f10f9d1748.jpg)

![](images/6058ad1a64ce2e7545a6575798e7066155cee36e4ee4f1ddbfd4edcc1c9b5d7a.jpg)

lines in Fig. 4b,c give the result of a full numerical simulation, without any adjustable parameters. Here the agreement with the spin-1/2 model is excellent, as many atom pairs are aligned along the quantization axis, thus making the effects of the anisotropy small. We included the finite value of  $\varepsilon$ , which has a strong effect on the pair correlations for  $k < \alpha$  as  $g^{(2)}(k)$  increases from 0 to  $2\varepsilon /f_{\mathrm{R}}$  (Methods).

As a final setting, we use a  $N_{\mathrm{t}} = 7\times 7$  two-dimensional square array (Fig. 4d), loaded with  $N = 28\pm 1.6$  atoms  $(57\%)$  filling), for  $\alpha = 2.6$  The dynamics of  $f_{\mathbb{R}}$  now appears monotonous (Fig. 4e), without the initial oscillations seen above for smaller systems (Figs 3b and 4b). This suggests that with  $N\approx 30$  atoms, the behaviour of the system is already close to the many-body behaviour observed in large ensembles21, with a fast initial rise of the Rydberg fraction, before it saturates. The simulation captures the initial rise of  $f_{\mathbb{R}}$  well, but does not reproduce the slow increase observed at long times, which we attribute again to multilevel effects (that are indeed expected to be strong in this array where the internuclear axes of many pairs lie at a large  $\theta$  ). Figure 4f shows the two-dimensional Rydberg-Rydberg correlation function

$$
g ^ {(2)} (k, l) = \frac {1}{N _ {\mathrm {t}}} \sum_ {i, j} \frac {\left\langle n _ {i , j} n _ {i + k , j + l} \right\rangle}{\left\langle n _ {i , j} \right\rangle \left\langle n _ {i + k , j + l} \right\rangle} \tag {3}
$$

where  $n_{i,j}$  refers to the site with coordinates (ia, ja). Although the system has open boundaries and thus does not show translational invariance, the averaging over the traps in equation (3) does not wash out correlations as  $R_{\mathrm{b}}$  is small compared to the system size. We observe a depletion of the correlation function close to the origin due to blockade. The anisotropy of the interaction is visible, as the depletion region is elliptical, with a flattening close to the expected value 1.2. We observe, in the full time evolution of the correlation function (Methods), that blockade volumes become more densely packed with increasing time.

The wide tunability of geometry and interactions demonstrated here opens the way to investigating the physics of spin systems with tens of particles. Our platform, especially when combined with quasi-deterministic loading of optical tweezers as demonstrated recently[22,23], will be ideally suited for studying the transition from few- to many-body physics[24], thermalization in strongly interacting closed quantum systems[25], or the dynamical emergence of entanglement following a quantum quench[26]. Using resonant dipole-dipole interactions between different Rydberg states[27], XY Hamiltonians with long-range couplings[28] could also be implemented. Finally, exploiting the Zeeman structure of Rydberg states holds the promise of implementing more complex Hamiltonians, to explore for instance the physics of higher spins[29], or to realize topological insulators[30].

Online Content Methods, along with any additional Extended Data display items and Source Data, are available in the online version of the paper; references unique to these sections appear only in the online paper.

# Received 12 January; accepted 11 April 2016.  
Published online 1 June 2016.

1. Auerbach, A. Interacting Electrons and Quantum Magnetism (Springer, New York, 1994).  
2. Georgescu, I. M., Ashhab, S. & Nori, F. Quantum simulation. Rev. Mod. Phys. 86, 153-185 (2014).  
3. Bloch, I., Dalibard, J. & Nascimbène, S. Quantum simulations with ultracold quantum gases. Nature Phys. 8, 267-276 (2012).  
4. Yan, B. et al. Observation of dipolar spin-exchange interactions with lattice-confined polar molecules. Nature 501, 521-525 (2013).  
5. Blatt, R. & Roos, C. F. Quantum simulations with trapped ions. Nature Phys. 8, 277-284 (2012).

6. Glaetzle, A. W. et al. Quantum spin-ice and dimer models with Rydberg atoms. Phys. Rev. X 4, 041037 (2014).  
7. Vermersch, B., Glaetzle, A. W. & Zoller, P. Magic distances in the blockade mechanism of Rydberg P and D states. Phys. Rev. A 91, 023411 (2015).  
8. Tresp, C. et al. Dipolar dephasing of Rydberg D-state polaritons. Phys. Rev. Lett. 115, 083602 (2015).  
9. Saffman, S., Walker, T. G. & Mølmer, K. Quantum information with Rydberg atoms. Rev. Mod. Phys. 82, 2313-2363 (2010).  
10. Weimer, H., Müller, M., Lesanovsky, I., Zoller, P. & Buchler, H. P. A Rydberg quantum simulator. Nature Phys. 6, 382-388 (2010).  
11. Barredo, D. et al. Demonstration of a strong Rydberg blockade in three-atom systems with anisotropic interactions. Phys. Rev. Lett. 112, 183002 (2014).  
12. Béguin, L., Vernier, A., Chicireanu, R., Lahaye, T. & Browaeys, A. Direct measurement of the van der Waals interaction between two Rydberg atoms. Phys. Rev. Lett. 110, 263201 (2013).  
13. Nogrette, F. et al. Single-atom trapping in holographic 2D arrays of microtraps with arbitrary geometries. Phys. Rev. X 4, 021034 (2014).  
14. Dudin, Y. O., Li, L., Bariani, F. & Kuzmich, A. Observation of coherent many-body Rabi oscillations. Nature Phys. 8, 790-794 (2012).  
15. Ebert, M. et al. Atomic Fock state preparation using Rydberg blockade. Phys. Rev. Lett. 112, 043602 (2014).  
16. Ebert, M., Kwon, M., Walker, T. G. & Saffman, M. Coherence and Rydberg blockade of atomic ensemble qubits. Phys. Rev. Lett. 115, 093601 (2015).  
17. Zeiher, J. et al. Microscopic characterization of scalable coherent Rydberg superatoms. Phys. Rev. X 5, 031015 (2015).  
18. Ates, C. & Lesanovsky, I. Entropic enhancement of spatial correlations in a laser-driven Rydberg gas. Phys. Rev. A 86, 013408 (2012).  
19. Petrosoyan, D., Honing, M. & Fleischhauer, M. Spatial correlations of Rydberg excitations in optically driven atomic ensembles. Phys. Rev. A 87, 053414 (2013).  
20. Schauß, P. et al. Observation of spatially ordered structures in a two-dimensional Rydberg gas. Nature 491, 87-91 (2012).  
21. Löw, R. et al. Universal scaling in a strongly interacting Rydberg gas. Phys. Rev. A 80, 033422 (2009).  
22. Lester, B. J., Luick, N., Kaufman, A. M., Reynolds, C. M. & Regal, C. A. Rapid production of uniformly-filled arrays of neutral atoms. Phys. Rev. Lett. 115, 073003 (2015).  
23. Fung, Y. H. & Andersen, M. F. Efficient collisional blockade loading of single atom into a tight microtrap. New J. Phys. 17, 073011 (2015).  
24. Gaj, A. et al. From molecular spectra to a density shift in dense Rydberg gases. Nature Commun. 5, 4546 (2014).  
25. Ates, C., Garrahan, J. P. & Lesanovsky, I. Thermalization of a strongly interacting closed spin system: from coherent many-body dynamics to a Fokker-Planck equation. Phys. Rev. Lett. 108, 110603 (2012).  
26. Hazzard, K. R. A. et al. Quantum correlations and entanglement in far-from-equilibrium spin systems. Phys. Rev. A 90, 063622 (2014).  
27. Barredo, D. et al. Coherent excitation transfer in a spin chain of three Rydberg atoms. Phys. Rev. Lett. 114, 113002 (2015).  
28. Hauke, P. et al. Complete devil's staircase and crystal-superfluid transitions in a dipolar XXZ spin chain: a trapped ion quantum simulation. New J. Phys. 12, 113037 (2010).  
29. Senko, C. et al. Realization of a quantum integer-spin chain with controllable interactions. Phys. Rev. X 5, 021026 (2015).  
30. Peter, D. et al. Topological bands with a Chern number  $C = 2$  by dipolar exchange interactions. Phys. Rev. A 91, 053617 (2015).

Acknowledgements We thank H. Busche for contributions in the early stages of the experiment, I. Lesanovsky, H. P. Buchler and T. Pohl for discussions, and Y. Sortais for a reading of the manuscript. This work benefited from financial support by the EU (FET-Open Xtrack Project HAIRS, H2020 FET-PROACT Project RySQ, and EU Marie-Curie Program ITN COHERENCE FP7-PEOPLE-2010-ITN-265031 (H.L.), by the 'PALM' Labex (project QUANTICA) and by the Région Île-de-France in the framework of DIM Nano-K.

Author Contributions All authors made critical contributions to the work, discussed the results, and contributed to the writing of the manuscript.

Author Information Reprints and permissions information is available at www.nature.com/reprints. The authors declare no competing financial interests. Readers are welcome to comment on the online version of the paper. Correspondence and requests for materials should be addressed to T.L. (thierry.lahaye@institutoptique.fr).

Reviewer Information Nature thanks C. F. Roos and the other anonymous reviewer(s) for their contribution to the peer review of this work.

# METHODS

Loading of trap arrays. In the single-atom loading regime of optical microtraps, the probability of having a given trap filled with a single atom is  $p \approx 1 / 2$ . Therefore, when we monitor the number of loaded traps in view of triggering the experiment (Extended Data Fig. 1a),  $N$  fluctuates in time around a mean value  $N_{\mathrm{t}} / 2$ , with fluctuations  $\sim \sqrt{N_{\mathrm{t}}}$ .

When the number of traps is small, we can impose, as the triggering criterion, waiting until all traps are filled. The average triggering time  $T_{N}$  then increases exponentially with  $N$ , as can be seen in Extended Data Fig. 1b. We used this 'full-loading mode' for the data of Fig. 1 ( $1 \leq N \leq 9$ ) and Fig. 3 ( $N = 8$ ). This exponential scaling sets a practical limit of  $N \approx 9$  for fully loaded arrays. For  $N = 9$ , the experimental duty cycle already exceeds one minute.

Because of this, for larger  $N_{\mathrm{t}}$  we use partially-loaded arrays. We set the triggering threshold in the tail of the binomial distribution of  $N$ , that is, close to  $N_{\mathrm{t}} / 2 + \sqrt{N_{\mathrm{t}}}$ . This allows us to keep a fast repetition rate for the experiment, of the order of  $1 \, \mathrm{s}^{-1}$ , enabling fast data collection. Extended Data Fig. 1c shows the distribution of loaded traps for the 'racetrack' array with  $N_{\mathrm{t}} = 30$  (resp. the  $N_{\mathrm{t}} = 7 \times 7$  square array), where we set the triggering condition to  $N = 20$  (resp.  $N = 30$ ). Using this triggering procedure, we thus end up with a narrow distribution of atom numbers  $N = 20 \pm 1.5$  (resp.  $N = 28 \pm 1.6$ ), corresponding to a filling fraction of  $67\%$  (resp.  $57\%$ ), significantly above the average  $N_{\mathrm{t}} / 2$ . These strongly subpoissonian distributions of atom numbers are such that the variation in  $N$  from experiment to experiment has a negligible effect on the physics studied in Fig. 4; moreover, as for each experiment the initial configuration image is saved, one can if needed post-select experiments where an exact number of atoms was involved (this is how the data in Fig. 2 for  $N \geq 10$  were obtained).

Recently, several experiments[22,23] demonstrated quasi-deterministic loading of single atoms in optical tweezers, reaching  $p \approx 90\%$  using modified light-assisted collisions that lead to the loss of only one of the colliding atoms instead of both. A preliminary implementation of these ideas on our set-up gave  $p \approx 80\%$  for a single trap. In future work, by using such loading in combination with the real-time triggering based on the measured number of loaded traps, it seems realistic to reach, even in large arrays, filling fractions in excess of 0.9, that is, approaching those obtained in quantum gas microscope experiments using Mott insulators.

Experimental parameters. Extended Data Table 1 summarizes the various values of the parameters of the arrays of traps and of the Rydberg states used for the data presented in the main text, and the resulting values of the dimensionless parameter  $\alpha$ . It illustrates the wide tunability offered by the system.

Finite detection errors. Our way to detect that a given atom has been excited to a Rydberg state relies on the fact that we do not detect fluorescence from the corresponding trap in the final configuration image. There is however a small probability  $\varepsilon$  of losing an atom during the sequence, even if it was in the ground state, thus incorrectly inferring its excitation to a Rydberg state<sup>11</sup>. These 'false positive' detection events affect the measured populations of the  $N$ -atom system. One can show that, if  $P_q$  is the observed probability of having  $q$  Rydberg excitations, and  $\tilde{P}_p$  the actual probability of having  $p$  Rydberg excitations:

$$
P _ {q} = \sum_ {p = 0} ^ {q} \binom {N - p} {q - p} \varepsilon^ {q - p} (1 - \varepsilon) ^ {N - q} \widetilde {P} _ {p} \tag {4}
$$

In principle, one can invert the above linear system relating the observed and actual probabilities<sup>31</sup>, to correct the experimental data for the detection errors. Here we have chosen on the contrary to show the uncorrected populations, and to include detection errors on the theoretical curves instead.

In order to determine the experimental value of  $\varepsilon$ , we use the initial data points  $(\tau = 0)$  of the data of Fig. 2. Since no Rydberg pulse is sent, we have  $\widetilde{P}_0 = 1$ , and from equation (4) the observed probability  $P_0(\tau = 0)$  reads  $(1 - \varepsilon)^N$ . Extended Data Fig. 2a shows the variation of  $P_0(0)$  as a function of  $N$ , together with a fit which allows us to extract  $\varepsilon = (3 \pm 1)\%$ , the value we use for the theoretical curves in the main text (see below).

Extended Data Fig. 2b shows the effect of this finite value of  $\varepsilon$  on the probabilities  $P_0$ ,  $P_1$  and  $P_2$  in the full blockade regime, for atom numbers  $N = 3, 9$  and 15, clearly illustrating that the 'false positive' detection events: first, yield non-zero (and increasing with  $N$ ) double excitation probabilities (that oscillate in phase with  $P_1$ ); second, multiply the amplitude of  $P_0$  by a factor  $(1 - \varepsilon)^N$ ; and third, reduce the contrast of the  $P_1$  oscillations. Globally, the experimental data (see Extended Data Fig. 3) show these features, superimposed with other imperfections such as damping, not related to the finite value of  $\varepsilon$ .

Finally, we mention the effect of the detection errors on the correlation functions. In the fully blockaded region  $k < \alpha$ , one ideally expects a vanishing  $g^{(2)}$  for  $\varepsilon = 0$ . However, even for a small  $\varepsilon$ , this value is increased substantially (see, for example, Fig. 4c) to  $2\varepsilon /f_{\mathrm{R}}$  where  $f_{\mathrm{R}}$  is the Rydberg fraction. Indeed,  $g^{(2)}(k = 1)$  is given by an average of quantities of the form  $\langle n_i n_{i + 1}\rangle /\langle n_i\rangle \langle n_{i + 1}\rangle$ . For  $\varepsilon = 0$ , the

numerator vanishes due to blockade; the only possibility of having a non-zero value comes from detection errors. To lowest order in  $\varepsilon$ , the probability of getting a nonzero value for  $n_i n_{i+1}$  is that either atom  $i$  is in  $|r\rangle$  (probability  $f_{\mathrm{R}}$ ) and atom  $i+1$  is lost (probability  $\varepsilon$ ), or vice versa. This results in a value of  $2\varepsilon f_{\mathrm{R}}$  for the numerator, while for the denominator we can use the zeroth-order values  $\langle n_i \rangle = \langle n_{i+1} \rangle = f_{\mathrm{R}}$ , thus giving  $g^2(1) \approx 2\varepsilon / f_{\mathrm{R}}$ , which experimentally can be as large as 0.5.

Additional experimental data. Full Rydberg blockade. Extended Data Fig. 3 shows additional data in the full blockade regime (Fig. 2). In Extended Data Fig. 3a, the arrays of 1 to 9 traps are fully loaded, while in Extended Data Fig. 3b, the 19-trap triangular array is partially loaded with 10 to 15 atoms. In both panels, the left column shows the time evolution of the probability  $P_0$  of recapturing all atoms at the end of the sequence, the middle column shows  $P_1$ , and the right column shows  $P_2$ . The points in Fig. 2a corresponding to  $N = 8$  and  $N = 9$  in partially loaded arrays were taken in a similar configuration as for  $N = 10$  to 15, but the array contained only  $N_{\mathrm{t}} = 17$  traps. The curves (not shown here) do not show any noticeable difference with other sets of data. We draw attention to the following.

First, we recognize the effects of the finite detection errors  $\varepsilon \neq 0$  on the amplitude and contrast of the collective oscillations discussed above.

Second, the oscillations exhibit some damping, which seems to increase with  $N$ . To quantify this, we fit the data by the function

$$
P (\tau) = a \mathrm {e} ^ {- \gamma \tau} \left(\cos^ {2} \left(\Omega_ {N} \tau / 2\right) + b\right) + c \tag {5}
$$

where  $a, b, c, \gamma$  and  $\Omega_N$  are adjustable parameters (solid lines). This functional form was chosen to account in a simple way for the asymmetry in the damping. Extended Data Fig. 3c shows the damping rates  $\gamma$ , extracted from the probabilities  $P_0$  as a function of  $N$ . We observe an initial increase in the damping rates, which then saturates above  $N = 5$ . An increase with  $N$  of the damping rate was observed in other similar blockade experiments[14-16]. However, even for large number of atoms, the damping rates are small enough that the coherent dynamics dominates over the relevant experimental timescales. We therefore emphasize that in all the other figures of the paper (main text and methods), the theory curves are obtained by disregarding completely any damping, that is, by solving the Schrödinger equation, not a master equation.

Third, we observe that  $P_{2}$  slowly increases over time for some specific values of  $N$  (see in particular  $N = 4, 6, 9, 13$ ), corresponding to particular geometries.

We do not have a full understanding of these last two observations, but they may originate from the breaking of the blockade due to the Zeeman structure of the Rydberg states  $n\mathrm{D}_{3/2}$  (see discussion below).

Eight-atom ring. Extended Data Fig. 4 shows that, within statistical fluctuations, the density of excitations on the eight-atom ring is homogeneous (this remains true at all times), and that the antiferromagnetic-like or crystal-like features obtained for some times, for example, for  $\Omega \tau = 3.1$ , can only be observed in the correlation functions. This illustrates the interest of our set-up, in which spin chains with PBC can be realized easily. On the contrary, in a one-dimensional chain with open boundary conditions, 'pinning' of the excitations at specific sites would occur due to edge effects.

Racetrack-shaped array. Extended Data Fig. 5a shows the full evolution of the time correlation function for the data of Fig.  $4\mathrm{a} - \mathrm{c}$  ( $R_{\mathrm{b}} = 4.3a$ ). Extended Data Fig. 5b corresponds to the same settings except for the fact that one now has  $R_{\mathrm{b}} = 2.4a$ .

Square array of  $7 \times 7$  traps. Extended Data Fig. 6 shows the full time evolution of the two-dimensional Rydberg-Rydberg correlation function  $g^{(2)}(k,l)$  for the  $7 \times 7$  square lattice of Fig. 4d-f. Note that the two-dimensional pair correlation function is calculated using equation (3), which implies that, due to the finite size of the array, the number of terms included in the sum decreases when  $k,l$  increase. The normalization takes this variation into account.

Mapping equation (1) on the quantum Ising Hamiltonian. To show the link between Hamiltonian, equation (1), reproduced below,

$$
H = \sum_ {i} \frac {\hbar \Omega}{2} \sigma_ {x} ^ {i} + \sum_ {i <   j} V _ {i j} n ^ {i} n ^ {j} \tag {6}
$$

and the quantum Ising model, we simply rewrite the operators  $n^i$  as  $(1 + \sigma_z^i) / 2$ . Omitting a constant term, we get:

$$
H = \sum_ {i} \frac {\hbar \Omega}{2} \sigma_ {x} ^ {i} + \sum_ {i} B _ {i} \sigma_ {z} ^ {i} + \sum_ {i <   j} \frac {V _ {i j}}{4} \sigma_ {z} ^ {i} \sigma_ {z} ^ {j} \tag {7}
$$

This is the quantum Ising model, with a transverse field proportional to  $\varOmega$ , and a local longitudinal field  $B_{i} = \sum_{j}V_{ij} / 2$  arising from the interactions. In a system with open boundary conditions, this collective longitudinal field is inhomogeneous, and can have observable effects<sup>32</sup>. In an infinite lattice, or in a system with periodic boundary conditions as realized here in one dimension, the longitudinal field is

homogeneous and could be compensated for by applying a global detuning of the excitation laser.

Anisotropy of the interaction. For a pair of atoms in a  $n\mathrm{D}_{3/2}$  Rydberg state with the internuclear axis not aligned with the quantization axis, the rigorous description of the van der Waals interaction requires the inclusion of all various Zeeman sublevels; the interaction then takes the form of a  $16 \times 16$  matrix. To keep the description of a system of  $N$  atoms tractable, one can, in the blockade regime, define an effective, anisotropic van der Waals potential<sup>7</sup> reducing the previous matrix to a single scalar. For  $n\mathrm{D}_{3/2}$  states, the anisotropy reported in refs 7 and 11 is well reproduced by the simple expression

$$
V _ {\text {e f f}} (r, \theta) = \frac {C _ {6} (0)}{r ^ {6}} \left(\frac {1}{3} + \frac {2}{3} \cos^ {4} \theta\right) \tag {8}
$$

with  $\theta$  the angle between the quantization axis and the internuclear axis, giving a reduction by a factor of three in interaction strength when  $\theta$  goes from 0 to  $\pi /2$  (see inset of Fig. 1a).

Owing to the anisotropy in equation (8), the shape of the blockade volume centred on a Rydberg atom is also anisotropic. However, because of the  $r^6$ -scaling of the interaction, the surface  $r(\theta)$  defined by  $V_{\mathrm{eff}}(r,\theta) = \hbar \varOmega$  is quite well approximated by a prolate spheroid with an aspect ratio of  $3^{1 / 6}\approx 1.2$ . In the Figs 1, 3, 4, the shaded regions depicting the blockade volume have the polar equation  $r(\theta) = R_{\mathrm{b}}\left(\frac{1}{3} +\frac{2}{3}\cos^4\theta\right)^{1 / 6}$ .

Numerical simulation of the dynamics. Our theoretical description of the system is based on the mapping of its dynamics into a pseudo-spin  $1/2$  model with anisotropic long range interactions. We therefore neglect the rich Zeeman structure of the  $n\mathrm{D}_{3/2}$  states. The numerical calculations rest on the solution of the Schrödinger equation for the Hamiltonian of equation (1) of the main text in a reduced Hilbert space  $\mathcal{H}$ . We first write the wavefunction  $|\psi\rangle$  of the system with  $N$  atoms in terms of states with a fixed number of Rydberg excitations and ground state atoms, which correspond to the eigenstates of the Hamiltonian with vanishing Rabi frequency  $\Omega$  (refs 17, 33). Then the truncation procedure is based on two complementary steps: first we define the maximum number of Rydberg excitations  $N_r^{\max}$  that we include in our basis, then second we eliminate those states which display excitations closer than a fixed distance  $R_0$ . Both  $N_r^{\max}$  and  $R_0$  are adjusted to ensure the convergence of the dynamics. For small samples (Fig. 3) we performed simulations including all 256 basis states, whereas for the racetrack configurations we typically set  $R_0$  smaller than the lattice constant but include up to  $N_r^{\mathrm{math}} = 10$  excitations at most, reducing the dimension of  $\mathcal{H}$  from  $2^{20} \approx 10^6$  to  $\sum_{q=0}^{N_r^{\max}} \binom{20}{q} \approx 6 \times 10^5$ . For the  $7 \times 7$  square array with 30 atoms, we set  $R_0 = 1.3a$  (much smaller than the blockade radius  $R_b = 2.6a$ ), thus reducing the dimension of  $\mathcal{H}$  to  $\sim 3 \times 10^6$  (the full Hilbert space is of dimension  $2^{30} \approx 10^9$ , and using only the truncation criterion on the number of excitations would reduce it to about  $5 \times 10^7$ , still intractably large). The Schrödinger equation within the truncated Hilbert space is then solved with a standard split-step method for the two non-commuting parts of the Hamiltonian of equation (1). All these calculations were repeated for several realizations of the loading of the arrays (50 realizations for the squared  $7 \times 7$  configurations and 200 realizations for the case with fewer traps), taking into account the anisotropic interparticle interaction of equation (8). The comparison with experimental data of the average fraction of excitations  $f_{\mathrm{R}} = \sum_{q=0}^{N} qP_q / N$  is done by including the "false positive" detection events as described by equation (4).

The calculation of the  $g^{(2)}(k)$  correlation function in Figs 3d and 4c follows the definition of equation (2). However, in contrast with the calculation of the average fraction of the excitations it is not possible to derive an analytical formula for  $g^{(2)}(k)$  to properly take into account the detection efficiency of Rydberg excitations (unless  $k < \alpha$  as described in section 'Finite detection errors'). Therefore we implement a standard Monte Carlo algorithm to perform the average of the correlation function over randomly generated configurations which are weighted in  $g^{(2)}(k)$  with the initial (quantum) probability extracted from the real time dynamics of the Schrödinger equation. For example, the state  $|r_i r_j\rangle$  which contains  $N_{\mathrm{t}} = 2$  Rydberg excitations and amplitude  $c_{ij}(t)$  can wrongly be detected as the state  $|r_i r_j r_q\rangle$  with probability  $P = \varepsilon (1 - \varepsilon)^{N - 2}$ . If the latter state is generated from our sampling algorithm then its weight in the correlation function corresponds to  $|c_{ij}(t)|^2$ . Finally we average over several hundred randomly generated configurations to obtain well converged results for the correlation function.

Effect of partial loading of large arrays on the observed dynamics. Using the simulations described above, we explore to what extent the partial loading of our larger arrays may change the observed dynamics as compared to the ideal case of full loading.

Extended Data Fig. 7 shows, for the 'racetrack' array of Fig. 4a-c, the results of simulations for the experimentally relevant case of partial loading (solid lines, filling fraction  $\eta \approx 0.67$ ) and for the ideal, full loading case (thin dashed lines):

First, Extended Data Fig. 7a also shows the time evolution of the Rydberg fraction  $f_{\mathrm{R}}$ . The dynamics is qualitatively similar in the two situations, with initial oscillations that rapidly get damped owing to the dephasing of the many incommensurate eigenenergies of the Hamiltonian. Quantitatively, the initial oscillations are faster in the fully loaded case: this is expected, as each blockade volume contains  $1 / \eta$  as many atoms, and thus, due to the scaling of the collective Rabi frequency with the number of atoms in a blockade volume, we expect an enhancement of the oscillation frequency by  $\sim \eta^{-1 / 2} \approx 1.2$ , close to what we observe. In the same way, the asymptotic Rydberg fraction when  $\tau \to \infty$  is reduced by a factor close to the expected factor  $\eta$ .

Second, Extended Data Fig. 7b shows the pair correlation function  $g^{(2)}(k)$  for  $\Omega \tau \approx 2.0$ . Here again, the changes are moderate, although the oscillations of the correlation function for  $k > \alpha$  would be slightly more contrasted for the fully loaded array.

Simulations for the other large array settings give similar results, allowing us to safely conclude that the partial loading of our largest arrays does not affect significantly the observed dynamics. This conclusion would be different for other types of experiments, for instance the transport of a spin excitation in the case of resonant-dipole-dipole interactions.

Approximate translational invariance. For the one-dimensional configurations of the main text (eight-atom ring of Fig. 3b and racetrack-shaped array of 30 traps of Fig. 4a) we plot the spatially averaged pair correlation function

$$
g ^ {(2)} (k) = \frac {1}{N _ {\mathrm {t}}} \sum_ {i} \frac {\left\langle n _ {i} n _ {i + k} \right\rangle}{\left\langle n _ {i} \right\rangle \left\langle n _ {i + k} \right\rangle} \tag {9}
$$

where the subscripts label sites. For a system invariant by translation, all terms in the sum are identical, and the averaging over  $i$  simply improves the signal to noise ratio. However, our systems are not translationally invariant, in particular because of the anisotropy of the interaction, and a natural question to address is whether the averaging reduces the contrast of the correlation functions. To answer this question, we have calculated the dynamics of the pair correlation function for the eight-atom ring, taking or not taking into account the anisotropy of the interaction (Extended Data Fig. 8). We observe that the contrast reduction due to averaging is very small, thereby validating our choice to perform it for the data shown in the main text.

Effective loss mechanism arising from anisotropic interactions of D states. The agreement between our measurements and the results of the simulations is not perfect for the largest excitation times, in particular for some settings (for example, for some configurations in the full blockade regime, for the eight-atom ring in the partial blockade regime, and for the  $7 \times 7$  square array), where we observe a gradual increase in the number of measured Rydberg excitations.

These effects could be qualitatively reproduced if the detection errors  $\varepsilon$  would increase in time. However, the main reason for these losses is that the microtraps are switched off during the excitation (to avoid inhomogeneous light-shifts), and as they are off for a fixed amount of time ( $3\mu s$ ), independent of  $\tau$ , we do not, at first sight, expect  $\varepsilon$  to increase in time. One could imagine however that the presence of the Rydberg excitation lasers may induce extra loss (due to off-resonant scattering for instance), and in this case one would end up having an  $\varepsilon$  increasing with  $\tau$ . We have experimentally ruled out this possibility by measuring the recapture probability when shining the Rydberg excitation lasers, detuned from the Rydberg line by  $\sim 100\mathrm{MHz}$ , for the full  $3\mu s$ , without measuring any detrimental effect.

A second possible reason would be the motion of the atoms. Owing to their finite temperature, the atoms move during free flight with a velocity  $\nu \approx 50\mathrm{nm}\mu \mathrm{s}^{-1}$ . Now, strictly speaking, the terms corresponding to the laser coupling in equation (1) of the main text are not  $\varOmega\sigma_{x}^{i}$ , but  $\varOmega\mathrm{e}^{\mathrm{i}k\cdot r_i(t)}\sigma_+^i +\mathrm{h.c.}$ , where  $\pmb{k}$  is the sum of the wavevectors of the excitation lasers at 795 and  $475\mathrm{nm}$ , and  $\boldsymbol {r}_i(t)$  the position of atom  $i$ . Thus, because of the motion, the phase factors of the couplings become time-dependent, which for example, yields a dephasing of the spin wave corresponding to  $|W\rangle$  states. However, a numerical simulation of this effect shows that the induced dephasing rates are negligible for our parameters.

We thus believe that the cause of the observed extra losses lies in the large number of interacting Zeeman sublevels when two atoms are excited to  $n\mathrm{D}_{3/2}$  states: for  $\theta \neq 0$ , all 16 pair state Zeeman sublevels are coupled together by the van der Waals interaction. For a large number of atoms, this may lead to an effective loss rate from the targeted  $|r\rangle$  states into a quasi-continuum comprising all other (weakly interacting) Zeeman states, and hence to a gradual increase of population of the Rydberg manifold. Qualitatively, this interpretation is corroborated by the fact that the observed increase in the number of excitations depends quite strongly on the array geometry: for instance, the data from the racetrack-shaped array (Fig. 4b), for which a majority of interacting atom pairs are almost aligned along the quantization axis  $z$ , are well reproduced by the simulations even at long times, unlike in the case of the eight-atom ring or the  $7 \times 7$  square array

(Figs 3b and 4e), for which many interacting pairs have their internuclear axes strongly inclined with respect to  $z$ .

A full simulation of the dynamics of  $N$  atoms including the full Zeeman structure of  $n\mathrm{D}_{3 / 2}$  states is challenging (neglecting hyperfine structure, the dimension of the Hilbert space is  $5^{N}$ , as we have 5 states per atom: the ground state and the four Zeeman sublevels of the Rydberg state), and is beyond the scope of this paper. However, in order to test the hypothesis described above, we have simulated the following minimal 'toy model' displaying the effect of a Zeeman structure: we consider a system of  $N = 6$  atoms in a line, aligned either along the quantization axis  $z(\theta = 0)$  or along  $y(\theta = \pi /2)$ , and excited to the Rydberg state  $n\mathrm{P}_{1 / 2}$ . The Hilbert space is then of size  $3^6$ , and we can perform exact diagonalization. The van der Waals Hamiltonian between two atoms (a  $4\times 4$  matrix which depends on  $\theta$ ) was taken from equations (4) and (5) of ref. 7.

The red solid lines in Extended Data Fig. 9 show the time evolution of the fraction of Rydberg atoms (whatever the Zeeman state)  $f_{\mathrm{R}}$ , calculated using this Hamiltonian with the full Zeeman structure. The black dotted lines show  $f_{\mathrm{R}}(t)$  when modelling the system by an assembly of spin-1/2 particles, with an interaction given by the effective potential analogous to equation (8) but calculated for  $n\mathrm{P}_{1 / 2}$  states following ref. 7 (for the parameters of the figure, the effective potential is four times as high when  $\theta = \pi /2$  as when  $\theta = 0$ ). As expected, for  $\theta = 0$ , the two approaches give exactly the same results (Extended Data Fig. 9a). However, for  $\theta = \pi /2$ , we observe that the two simulations, while giving similar results at short times, disagree significantly at larger times, with the  $n\mathrm{P}_{1 / 2}$  structure yielding (as observed in some of our experiments, see for example, Fig. 4e) an increased Rydberg fraction, as the population of the Zeeman state not directly coupled to  $|g\rangle$  by the laser (blue dashed line) slowly increases. On the basis of this simulation,

we can thus conclude that in some cases, the anisotropic character of the interaction and the complex Zeeman structure can lead to the observed discrepancy between our data and the modelling by spin-1/2 particles interacting via an effective potential.

We note however that this behaviour is not universal and that, for a given geometry and a given Rabi frequency, varying the value of  $n$ , as well as that of the magnetic field, affects the degree of agreement between the exact dynamics and the simplified spin-1/2 model. In Extended Data Fig. 9, for instance, we chose  $n = 30$ ,  $B = 0.2\mathrm{G}$ , and a spacing between the atoms of  $a = 2$  or  $1.6\mu \mathrm{m}$ , to display a behaviour qualitatively similar to that of Figs 3b and 4e. This non-universal character suggests that for  $n\mathrm{D}_{3 / 2}$  states also, a careful choice of parameters ( $n$ , spacing,  $B$  field) may allow a very good agreement between the observed dynamics and that of a spin-1/2 model with anisotropic interactions even in geometries where many pairs lie at a large angle from the quantization axis. A comprehensive study of those conditions, along the lines of refs 7, 8, 34, is very important in view of quantum simulation applications, but it is however beyond the scope of this paper and will be the subject of future work.

31. Shen, C. & Duan, L.-M. Correcting detection errors in quantum state engineering through data processing. New J. Phys. 14, 053053 (2012).  
32. Zeiher, J. et al. Many-body interferometry of a Rydberg-dressed spin lattice. http://www.arXiv.org/abs/1602.06313 (2016).  
33. Schauß, P. et al. Crystallization in Ising quantum magnets. Science 347, 1455-1458 (2015).  
34. Derviananko, A., Komar, P., Topcu, T., Kroeze, R. M. & Lukin, M. D. Effects of molecular resonances on Rydberg blockade. Phys. Rev. A 92, 063419 (2015).

![](images/ec3f75cb30095db70a9189f326ec01306e759b332159136e9dda6a3bb5d031c7.jpg)  
a

![](images/2d3285c794f943c71c0b223c74686ced8860c3af78b72cde61cb2d0e8964ce48.jpg)  
b

![](images/e6867827f764e10c46e2af31f084fb37edbe40099ca37b03d42d7f1d65268dda.jpg)  
Extended Data Figure 1 | Full and partial loading of arrays. a, Sketch of the experimental sequences. During loading, the camera images are analysed continuously to extract the number of loaded traps. As soon as a triggering criterion is met, the loading is stopped and an image of the initial configuration is acquired. After Rydberg excitation, a final image is acquired, revealing the atoms excited to Rydberg states (green disks at bottom right). b, Average triggering time  $T_{N}$  when the triggering criterion is set to  $N = N_{\mathrm{t}}$ : achieving full loading requires an exponentially long time, limiting the method in practice to  $N_{\mathrm{t}} \leq 9$ . The triggering times  
C  
can vary substantially depending on the density of the magneto-optical trap used to load the array, and the data points shown here correspond to typical conditions used for the data of the main text. Error bars, s.e.m. c, Probability  $p_N$  of having a number  $N$  of loaded traps in the partially loaded regime for the 30-trap 'racetrack' (left) and the 49-trap square array (right; blue dots). The shaded distributions correspond to what would be observed with random triggering. For this partial loading regime, the triggering rate of the experiment is about  $1\mathrm{s}^{-1}$ .

![](images/3256be869b18d28fe4e79a69d5aa635e987b01a6e08c20a822d06f6572a5fce6.jpg)

![](images/d8394743ab22b14d3aafbb024d1b6a778c19dc7d7b6254c1c2d6e0b958a3fe38.jpg)  
a

![](images/0e4451cbf0b934b8d06efd6373ff6a8a1dfe1eb54bfd8bab5d36fb671f2df27c.jpg)  
Extended Data Figure 2 | Effect of detection errors. a, Experimental determination of  $\varepsilon$ . From the data of the full blockade experiments (Fig. 2 of main text), we plot the probability  $P_0$  of recapturing all  $N$  atoms for  $\tau = 0$ . The solid line is a fit to the expected dependence  $(1 - \varepsilon)^{N}$ , giving  
b  
$\varepsilon = 3\%$  (the shaded area corresponds to  $2\% < \varepsilon < 4\%$ ). Error bars, s.e.m. b, Calculated probabilities of observing 0,1 or 2 excitations (columns 1-3) as a function of the excitation pulse area  $\Omega t$ , assuming a perfect blockade and  $\varepsilon = 3\%$ , for atom numbers  $N = 3,9,15$  (rows 1-3).

![](images/9489de6c4816344ed725f4d3c68abe1603df87d3e53fca887e26a6d7fb3d89c6.jpg)  
a  
Extended Data Figure 3 | Full data set for the Rydberg blockade data. a, Fully loaded arrays of 1 to 9 traps  $(n = 82)$ . b, Partially loaded array of  $N_{\mathrm{t}} = 19$  traps, containing from  $N = 10$  to  $N = 15$  atoms  $(n = 100)$ . The column on the left shows the probability  $P_0$  of recapturing all atoms, the centre column the probability  $P_{1}$  of losing just one atom out of  $N$ , and

![](images/b509236d36c4327a5a50be240606155dd25bb5532e0c1f89d678f07a39699a96.jpg)  
the column on the right the probability  $P_{2}$  of losing two atoms out of  $N$ . The solid lines are fits by equation (5). Error bars, s.e.m. c, Damping rate  $\gamma$  extracted from the  $P_{0}$  data as a function of the number of atoms in the array. Error bars, s.d.

![](images/c790de2e4d9e75334f1feba628ebe7fe58e9d768bc612c7f97630714420ad767.jpg)  
Extended Data Figure 4 | Homogeneous excitation in the eight-atom ring. a, For  $\Omega \tau = 3.1$ , we observe strongly contrasted oscillations in the pair correlation function  $g^2(k)$ . b, The average density of Rydberg excitations, however, is approximately the same on every site. The horizontal dashed line indicates the mean over all sites. Error bars, s.e.m.

![](images/2ffae6137dbe99b506e6c6fc2624c9ce301c3921cb7e4cfbf248874843680e16.jpg)

![](images/a339ea93f2c45cfa28391b01372bb7431a8c4ab57cb8a44e578d0e20f0b0ec6a.jpg)  
a

![](images/13da291e9982ddc6091fec06aa3b3e23a076ebf75d1cc2e205931ca4729371fe.jpg)

![](images/876bb18923280c1da39790a6de8fb22f7f987734611287b4dde44b5b05619b75.jpg)

![](images/2da3ade4e3394a192ccf868432f7bd8c8da6e130ee5fd75e934d5e82fa0a888a.jpg)  
b

![](images/0752b9dbc2e9563fbed1350ff2c671f113fb2164700b1e57478556cf580d4249.jpg)  
Extended Data Figure 5 | Full time evolution of the correlation functions for the 30-trap, racetrack-shaped chain. a, Same as for Fig. 3a-c. The right panel is the time evolution of the pair correlation function, clearly showing that, for times longer than a few  $\Omega^{-1}$ , the pair correlation function does not evolve significantly. The vertical dashed line indicates the value of the blockade radius. b, The principal quantum number is now

![](images/e4badf7b5943c57d8d282eca698292e96ebd9f1adfb8ea607177a1bb9deb71f3.jpg)  
$n = 57$ , and the Rabi frequency  $\Omega = 2\pi \times 1.7\mathrm{MHz}$ , such that  $R_{\mathrm{b}} = 2.4a$ . The central panel shows the time evolution of the Rydberg fraction, and the right panel the time evolution of the pair correlation function. For both a and b,  $f_{\mathrm{R}}$  approaches, at long times, the close-packing limit  $a / R_{\mathrm{b}}$  of hard rods of length  $R_{\mathrm{b}}$  (dashed horizontal lines).

![](images/e50c8bdb591fe5c54b5ef1e523bd10d4d46247eee0c39e5b643f910110a35195.jpg)  
1

![](images/d1cf0ffcfc321a65060fb71aec24c7c2ee3d6603a55ec62f6b508d377039c4e1.jpg)

![](images/4ffbddee97bbc39c25daa68950d73d05f0bbc64ab23afb68f2d002d62a0469ae.jpg)

![](images/5ccfbf755ae6ffaabf722e2a154e0b2e5a6232fc1af259f3e8085261520c7c2c.jpg)

![](images/a426ac123629911a2bc1b9ffe3a08c32553df6a36162498c8c49e2d86058ffb4.jpg)

![](images/e58fd56ba4b51751a990635f732ba7006e0c754de25ae4999c0deeaed0eb375d.jpg)

![](images/cb81e7480fc340e75b85ce95bcf4b9ff9a2a692685d32007c0542419f15dfea8.jpg)

![](images/c61acfa273e2e02a6a6862cbb5e71af92afc428264ce3877384b2c8168247083.jpg)

![](images/b29113a8dad3a3f86c7e4c7e9ce1cf23dfd48431c4e2d9232aa5a7aceea34d78.jpg)  
k  
/  
Extended Data Figure 6 | Full time evolution of the experimental correlation function for the  $7 \times 7$  square array. One observes the blockaded region around  $(k, l) = (0, 0)$ , with a slight flattening reflecting the anisotropy of the interaction. After a few  $\Omega^{-1}$ , the correlation function  $g^{(2)}(k, l)$  does not evolve any more.

![](images/e2d0757daac6cf1c14af1fd848b298a87a9bce7ddda83d0ed784cd317ac3da3a.jpg)  
k

![](images/12114c350e7e166ef4c55fa5484c4a1d34b113925d78e197205f577775bdd151.jpg)  
k

![](images/0b89a5057ebe3fd14428ddc9d660225f920682db1856e0a5416b03e2788b2bcd.jpg)  
k

![](images/226a55871e60d6b4d9cc383ba80d39a945393a5c225dcafd6a9994560a40f9d3.jpg)  
k

![](images/90272ffca328f810aaf9ca96e1b4ca8eee46f2eadf83f42293821394c7d7f0b4.jpg)  
K

![](images/b47b23ed572b3e4b13dbc91a8525ea289fba0636862b37583cf723470100a344.jpg)  
K

![](images/bbd79e9442b1fdda1c55d29f7699205990ddf3fa2c538529c5fa835a74f3b3e6.jpg)  
Extended Data Figure 7 | Full versus partial loading for the dynamics and correlations in the case of Fig. 4a-c. a, Rydberg fraction as a function of time for the partially loaded (solid line) or fully loaded (thin dashed line) 30-trap array. b, Pair correlation function  $g^{(2)}(k)$  for  $\Omega \tau \approx 2.0$ , for the partially loaded (solid line) or fully loaded (thin dashed line) 30-trap array. In both cases, the effect of detection errors  $(\varepsilon = 3\%)$  is included.

![](images/16d13ebac4f4afd31d1c437709676d4f080463bbd5c66b3becbce86af0f4ffbd.jpg)

![](images/9af875a09f2308934df56b7c0137405819af8352e91a6c6d9edfc2a833a81cfb.jpg)

![](images/ba17c69fc9bba356f549109838e721e25baf1080bc6f11c9b916567d085586d6.jpg)

![](images/f809b3d526086712c0ca30a49e1591802743c7fae595434036737be2993f51d6.jpg)

![](images/553aa8baf23defacdc54dc9004b0b479557f2f2d6c01be4a0b0db5210d4a180e.jpg)

![](images/cf0aef7afc009a37501e2b14901bd3182afc969ff53ae25aa0522224761af009.jpg)

![](images/a800d7fc05f181a45d312a68011a5960ac92adc6f3e8a3f438edf909f012e6fd.jpg)  
Extended Data Figure 8 | Assessing the validity of the approximation of translational invariance in the eight-atom ring. Calculated pair correlation function  $g^{(2)}(k)$  as a function of the excitation time for the eight-atom ring. a, Simulation using the experimentally relevant anisotropic interaction, which breaks translational invariance.

![](images/22b9cba30be77220b03bb01f470d4704c444b864b0c09d538202e743406f1367.jpg)

![](images/3cfe391c7140f1557e2e86c87a7128c2115e364538ba42697c100a159bc4224d.jpg)  
b, Simulation with the same parameters as in a, except that the angular dependence is neglected (we replace equation (8) by its value for  $\theta = 0$ ), thus re-establishing translational invariance. We observe that the contrast in a is reduced, as expected, but only in a marginal way.

![](images/9bb10cc26b4e9111effbab9e01f4961bcb541bbd245f680f3b41757025666f9f.jpg)

![](images/461db2e9d6e68fee42676bd88b785b8503cc7ef35712b281897c4a2a02a73e97.jpg)

![](images/554270d97fa385b6b388a21ad701b26e932295c3c5b1f7e3f55751cd1e40acda.jpg)  
Extended Data Figure 9 | Effect of the Zeeman structure of the Rydberg states on the dynamics of the Rydberg fraction  $f_{\mathrm{R}}$ . We use the toy model of  $n\mathrm{P}_{1/2}$  Rydberg states discussed in Methods, with  $n = 30$  and  $B = 0.2$  G. a, The atoms are aligned along the quantization axis  $z$ , and spaced by  $a = 1.6\mu \mathrm{m}$  (inset). In this case, the full solution including the Zeeman structure (red solid line) agrees perfectly with the solution of the effective spin-1/2 model with an anisotropic effective potential (as used in all the rest of the paper, black dotted line). b, The atoms are aligned

![](images/86b9fad56f9fd695bf174a79358c54c15bc5a3404cb81aafa11529f0f8e743c0.jpg)  
perpendicularly to  $z$ , with  $a = 2\mu \mathrm{m}$  (inset; thus keeping the same effective potential interaction between adjacent atoms as in a). The full (red solid line) and approximate (black dotted line) solutions agree at short times, but for longer times some population builds up in the other Zeeman sublevel that is not directly coupled to  $|g\rangle$  by the laser (blue dashed line), resulting in a slowly increasing excess of Rydberg fraction similar to what is observed experimentally for some configurations.

Extended Data Table 1 | Experimental parameters used for the data presented in the main text  

<table><tr><td rowspan="2">Figure</td><td colspan="4">Trap array parameters</td><td colspan="4">Rydberg state parameters</td></tr><tr><td>Spacing \( a \) (μm)</td><td>\( {N}_{\mathrm{t}} \)</td><td>\( N \)</td><td>\( n \)</td><td>Calculated \( {C}_{6}/h \) (GHz \( \mu {\mathrm{m}}^{6} \) )</td><td>\( \Omega /\left( {{2\pi }}\right) \) (MHz)</td><td>\( {R}_{\mathrm{b}} \) (μm)</td><td>\( \alpha \)</td></tr><tr><td>2a (full)</td><td>3.0</td><td>1-9</td><td>\( {N}_{\mathrm{t}} \)</td><td>82</td><td>\( - {8.9} \times  {10}^{3} \)</td><td>1.5</td><td>14</td><td>4.5</td></tr><tr><td>2a (partial)</td><td>3.2</td><td>19</td><td>10-15</td><td>100</td><td>\( - {8.0} \times  {10}^{4} \)</td><td>1.1</td><td>20</td><td>6.4</td></tr><tr><td colspan="9"></td></tr><tr><td>3a</td><td>6.3</td><td>8</td><td>8</td><td>54</td><td>-6.7</td><td>1.6</td><td>4.0</td><td>0.63</td></tr><tr><td>3b</td><td>6.3</td><td>8</td><td>8</td><td>61</td><td>\( - {7.6} \times  {10}^{2} \)</td><td>1.3</td><td>9.1</td><td>1.4</td></tr><tr><td>3c</td><td>3.8</td><td>8</td><td>8</td><td>100</td><td>\( - {8.0} \times  {10}^{4} \)</td><td>0.95</td><td>21</td><td>5.5</td></tr><tr><td colspan="9"></td></tr><tr><td>4a,b,c</td><td>3.1</td><td>30</td><td>\( {20} \pm  {1.5} \)</td><td>79</td><td>\( - {6.0} \times  {10}^{3} \)</td><td>1.0</td><td>13.5</td><td>4.3</td></tr><tr><td>4d,e,f</td><td>3.5</td><td>49</td><td>\( {28} \pm  {1.6} \)</td><td>61</td><td>\( - {7.6} \times  {10}^{2} \)</td><td>1.4</td><td>9.1</td><td>2.6</td></tr></table>

Wide tuning of  $\alpha = R_{\mathrm{b}} / a$  over one order of magnitude, is achieved by a combination of changes in  $a$  and  $n$  (while  $\Omega$  is kept almost constant).