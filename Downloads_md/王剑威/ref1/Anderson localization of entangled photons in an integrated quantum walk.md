# Anderson localization of entangled photons in an integrated quantum walk

Andrea Crespi $^{1,2}$ , Roberto Osellame $^{1,2\star}$ , Roberta Ramponi $^{1,2}$ , Vittorio Giovannetti $^{3}$ , Rosario Fazio $^{3,4}$ , Linda Sansoni $^{5}$ , Francesco De Nicola $^{5}$ , Fabio Sciarrino $^{5,6\star}$  and Paolo Mataloni $^{5,6}$

First predicted for quantum particles in the presence of a disordered potential, Anderson localization is a ubiquitous effect, observed also in classical systems, arising from the destructive interference of waves propagating in static disordered media. Here we report the observation of this phenomenon for pairs of polarization-entangled photons in a discrete quantum walk affected by position-dependent disorder. By exploiting polarization entanglement of photons to simulate different quantum statistics, we experimentally investigate the interplay between the Anderson localization mechanism and the bosonic/fermionic symmetry of the wavefunction. The disordered lattice is realized by an integrated array of interferometers fabricated in glass by femtosecond laser writing. A novel technique is used to introduce a controlled phase shift into each unit mesh of the network. This approach yields great potential for quantum simulation and for implementing a computational power beyond the one of a classical computer in the 'hard-to-simulate' scenario.

In 1958, P.W. Anderson<sup>1</sup> predicted that the wavefunction of a quantum particle can be localized in the presence of a static disordered potential. As a consequence, it is expected that particle and energy transport through a disordered medium should be strongly suppressed and that an initially localized wave packet should not spread out with time. More than 50 years after its discovery, Anderson localization is still widely studied and it has pervaded many different areas of physics ranging from condensed matter and cold atoms to wave dynamics and quantum chaos<sup>2</sup>.

This phenomenon emerges quite generically in the behaviour of waves in complex media, and it has been experimentally observed in a variety of different systems, including Bose-Einstein condensates $^{3,4}$ , light in semiconductor powders $^{5}$ , inverted opals $^{6}$  and photonic lattices $^{7-9}$ , single photons in bulk optics $^{10}$  and fibre loops $^{11}$ , microwaves in strongly scattering samples $^{12}$ , as well as ultrasound waves in a three-dimensional elastic system $^{13}$ . Anderson localization arises from destructive interference among different scattering paths of a quantum particle propagating in a static disordered medium. As such, it is intrinsically a single-particle effect. However, when multiple particles co-propagate in the same medium, quantum correlations, present in the initial state or induced by the quantum statistics of the involved particles, may influence the overall wavefunction evolution in a way that is not dissimilar from the bunching/antibunching mechanisms observed in interferometric experiments $^{14-17}$ . Such sensitivity to quantum correlations is not related to the presence of interactions between the co-propagating walkers. Therefore, a direct interaction between the walkers should be avoided in order to investigate the pure effect of quantum correlations.

In this work we experimentally study the localization properties of a pair of non-interacting particles obeying bosonic/fermionic statistics $^{18}$  by simulating a one-dimensional quantum walk (QW) of a two-photon polarization-entangled state in a disordered medium. To implement different quantum statistics we exploit a formal mapping, developed in ref. 14, which links the symmetry

of the polarization-entangled biphoton input state to the bosonic/fermionic symmetry of the wavefunction of two particles. The experimental investigation of these complex interference effects is enabled by the perfect phase stability provided by miniaturized integrated waveguide circuits $^{19}$ . After briefly reviewing some basic concepts about QWs, we will detail the peculiarities of our experimental implementation, reserving the second part of the Article to the discussion of the observed results.

# One-dimensional quantum walks

A one-dimensional  $\mathrm{QW^{20}}$  is an extension of the classical random walk, where the walker goes back and forth along a line and the direction at each step depends on the result of a fair coin flip. At the quantum level, interference and superposition phenomena lead to a non-classical behaviour of the walker, giving rise to new interesting effects that can be harnessed to exponentially speed up search algorithms[21] and to realize universal quantum computation[22]. QWs have also been proposed to analyse energy transport in biological systems[23,24]. Different experimental implementations of single-particle QWs have been demonstrated with trapped atoms[25], ions[26,27], energy levels in NMR schemes[28], photons in waveguide structures[29], in bulk optics[10,30], and in a fibre loop configuration[11,31]. Very recently, QWs of two identical photons have been demonstrated, but only in ordered structures[19,32,33].

A physical realization of a one-dimensional discrete QW can be provided by photons passing through a cascade of balanced beamsplitters arranged in a network of Mach-Zehnder interferometers, as represented conceptually in Fig. 1. Each beamsplitter simultaneously implements the quantum coin operation (that is, the choice of direction in which the particle will move) and the step operator, which shifts the walker in the direction fixed by the quantum coin state. The time evolution is simulated stroboscopically<sup>19</sup>. Accordingly, every output of a beamsplitter of the network corresponds to a given point in the space-time of the QW, with the

![](images/982bde2de65b4ec0200d9ea6eea42ed1e4d82f7af2e43ec812cbf86410973405.jpg)  
Figure 1 | Concept scheme of cascaded beamsplitters to implement photonic QWs. Disorder is introduced by phase shifters placed at each beamsplitter's output port, before entering the next one.

horizontal rows of the setup (scheme in Fig. 1) representing different time steps. In this scenario, disorder can be added in the QW evolution by simply introducing (randomly selected) phase shifts in the Mach-Zehnder interferometer arms. In particular, the time-independent, static, disorder needed to enforce Anderson localization on the photonic walker is obtained by fixing the same phases for all the Mach-Zehnder interferometers corresponding to the same lattice site. Making sure that the response of the device is polarization-independent, the evolution of two non-interacting particles can now be simulated by injecting into two different ports of the device—namely  $A$  and  $B$  in Fig. 2a—a two-photon polarization-entangled state generated via spontaneous parametric downconversion.

# Integrated circuits for photonic QWs

The above approach would be extremely hard to implement with bulk optics, mainly because of size and very challenging stability

issues. However, in the last few years integrated photonics has proven to be a highly promising experimental platform for quantum information science $^{34}$ . Integrated waveguide circuits have been used recently for quantum applications, to realize two-qubit gates $^{35-38}$ , quantum algorithms $^{39}$ , QWs on a chip $^{19,32,33,40}$  and quantum interferometry experiments $^{41-43}$ . In particular, femtosecond laser waveguide writing $^{44-46}$  is emerging as a powerful technology for realizing such circuits $^{19,33,37,38,43}$ . This technology exploits the nonlinear absorption of femtosecond pulses, focused below the surface of a transparent dielectric substrate, to obtain a permanent and localized refractive index increase. Translation of the sample under the laser beam along the desired path enables the fabrication of optical waveguide circuits with arbitrary three-dimensional design. Circuits with different designs can thus be fabricated with unequalled rapidity and versatility, and without the costs of lithographic masks. Furthermore, femtosecond laser-written waveguides are known to support the propagation of polarization-entangled states $^{19,37}$ . To study disorder-induced effects, such as Anderson localization, for polarization-entangled photons, an important step forward is required in the currently available experimental platforms, namely to conjugate in the same setup polarization-independent elements, interferometric structures and a proven capability to implement a controlled phase shift in different points of the QW circuit. As will be shown here, our devices integrate all these features.

In our experiment the setup of Fig. 1 was realized by integrated waveguide circuits fabricated by femtosecond laser writing, according to the layout depicted in Fig. 2. Beamsplitter elements were replaced by directional couplers. The discrete  $m$ -axis indicates the different sites of the QW, while the discrete  $n$ -axis identifies the different time steps. To obtain a totally polarization-independent behaviour, the three-dimensional geometry detailed in ref. 19 was adopted. The controlled phase shifts were implemented by deforming one of the S-bent waveguides at the output of each directional coupler (green or red segments in Fig. 2b), to stretch the optical path. The phase shift  $[- \pi, \pi]$  in each Mach-Zehnder cell was implemented by lengthening the optical path either in the green segment to introduce a  $[0, \pi]$

![](images/a0b6759a6a7c2aad25c0e3afbdbe898120ec4fb1c5e6946708efb26c037a4b46.jpg)  
b

![](images/20e8d66a68bdfc2f997f0ad01047eaf7dbb41181a119d8c829b6216a6af5d643.jpg)

![](images/5349bb0d576b5dfa8f26a1318bae29caa10eeef96b02c09a76f3b054fc3cbc04.jpg)

![](images/2465f47c20e49f0e91970d8668b5dd8a1a06006002f61d43f8a81b3cfa4af86e.jpg)  
d

![](images/ab1bf5a420be15264aca5dd1b7ff4acea43f44663b773724f7596c133b580ca8.jpg)  
Figure 2 | Integrated circuit for disordered QW. a, Scheme of the network of directional couplers implementing an eight-step one-dimensional QW with static disorder. Different colours indicate different phase shifts and violet waveguides represent the accessible paths for photons injected from inputs A and B. b, Controlled deformation of either of the two S-bent waveguides at the output of each directional coupler extends the optical path and is equivalent to the application of a phase shifter. c, The deformation is given by a nonlinear coordinate transformation, which is a function of deformation coefficient  $d$  (Supplementary Section SIV). The graph shows the undeformed S-bend (solid line), together with a deformed one (dashed). d, Schematic of the Mach-Zehnder structure, representing the unit cell of the directional couplers network, fabricated for calibrating the phase shift induced by the deformation. e, Phase shift induced by the deformation: theoretical curve calculated from the nominal geometric deformation (solid line), and experimental measurements (diamonds).

Table 1 | Similarities for single-particle QW distributions.  

<table><tr><td>Steps</td><td>Input A</td><td>Input B</td></tr><tr><td>Ordered</td><td></td><td></td></tr><tr><td>4</td><td>0.991±0.002</td><td>0.992±0.002</td></tr><tr><td>6</td><td>0.994±0.003</td><td>0.987±0.003</td></tr><tr><td>8</td><td>0.951±0.004</td><td>0.946±0.005</td></tr><tr><td>Static disorder</td><td></td><td></td></tr><tr><td>4</td><td>0.980±0.003</td><td>0.976±0.002</td></tr><tr><td>6</td><td>0.985±0.002</td><td>0.976±0.003</td></tr><tr><td>8</td><td>0.938±0.004</td><td>0.957±0.004</td></tr></table>

The values are calculated as the mean average of distributions of single photons in different polarization states, so the reported deviations quantify the similarity of these distributions.

phase shift, or in the red segment to span the complementary range  $[- \pi, 0]$ . In this way, small deformations, always of the same kind (lengthening of the path), are capable of providing the full range of phase shifts. Figure 2c shows both an undeformed and a deformed S-bend.

To test our technique and calibrate the achieved phase shift as a function of the imposed deformation  $d$  (see Supplementary Section SVI for a detailed definition) several Mach-Zehnder interferometers were fabricated with the design of Fig. 2d, reproducing exactly the unit cell of the QW network. Each interferometer had one S-bend (the one coloured in the figure) deformed with a different value of  $d$ . Laser light at a wavelength of  $\lambda = 806~\mathrm{nm}$  was injected into the interferometers, and the induced phase shift was then retrieved from the measured light distribution at the output. Figure 2e reports the experimentally measured phase shifts as a function of the deformation parameter  $d$ . The experimental points

are in good agreement with the phase shift predicted by evaluating numerically the geometric lengthening  $\Delta l$  of the deformed S-bend,  $\varphi_{\mathrm{theo}} = \frac{2\pi}{\lambda} n\Delta l$ . The designed phase shift is actually achieved with an accuracy of about  $\lambda / 30$ .

# Experimental one- and two-photon Anderson localization

We implemented a lattice with static disorder by imposing the same phase shift to the Mach-Zehnder cells corresponding to a fixed site of the QW line as in Fig. 2a  $(\varphi_{m,n} = \varphi_m,\forall n)$ . QW circuits composed of four, six and eight steps, affected by static disorder, were realized in a way that the four-step phase pattern was embedded within the six-step phase pattern and, in turn, this was embedded within the eight-step one. A set of four-, six- and eight-step QW circuits implementing an ordered structure was also realized (that is, with perfectly symmetric Mach-Zehnder cells), to enable comparison to the corresponding disordered one.

We first measured the single particle distributions so as to demonstrate the polarization insensitivity of the integrated QWs. We repeated this measurement by injecting single photon states with different polarizations and compared the obtained results with the expected ones by calculating the associated similarity function (that is, with the generalization of the classical fidelity between two distributions  $D$  and  $D'$  defined as  $S = (\sum_{j,k} \sqrt{D_{jk}D_{jk}'})^2 / \sum_{j,k} D_{jk} \sum_{j,k} D_{jk}'$ ). The obtained mean values are reported in Table 1 for the ordered QW circuits and for QWs with static disorder. These high values and low deviations highlight once more the fabrication control and polarization insensitivity of our integrated devices.

As a second step we carried out the investigation of two-particle QWs. By adopting the experimental apparatus described in detail in

![](images/a7ef12baef65714d7469b75bdbd5c96d0efcc2e450f45cd1890ba9ccf01f4db9.jpg)

![](images/6b2a67c589037a96b14c48644ae2a6365a87c1bf3c503f11c12baa3ee2c70a92.jpg)

![](images/83fc8bc97f4e45dbbc029c7969496a0a6bd730f170b3b27aa6506bf9ffd45065.jpg)

![](images/5f2bd85543136c81ffcf74028112226c9883027c65b2a0f659c0af9af074ef67.jpg)

![](images/eb97499a725ff5db1818b29866f77fee3f3c495b7edc18fc1b5ce4d6a603690b.jpg)

![](images/4e87eba5a0ba3027798a2788c16b011b9242d53c71cb935eacaccb9445b49603.jpg)

![](images/2629c78daf28e9c25876f52b5f562eb300507d68eb5c99ceb52d7ac7ca1aa6a5.jpg)

![](images/7435a23f9dce381322be9a8a37baff8cc2916f990145b1ec674be64acffedcdf.jpg)  
Figure 3 | Measured output probabilities for QWs with order and static disorder. a-r, Single- and two-photon symmetric distributions  $P_{j}^{(\mathrm{sym})}$  and  $P_{j,k}^{(\pm,\mathrm{sym})}$  (each normalized to its maximum) for bosons and fermions in an ordered QW (a-i) and in a QW in the presence of static disorder (j-r). Single-particle density distributions have been computed by tracing out the position of one of the particles (summing over the columns of the two-photon probability distribution matrices).

![](images/4b842ac8d46f7d138d898fa554863ae288577e42419309b91f21268225f962c2.jpg)

![](images/fdd5cbbe69a00d8db0ac458c423e0d7f178669314a14a23920c24d981d493b2d.jpg)

![](images/4e7b1982737645e587e1c16232f70de30c4e77fabc0bf78b4130a5ef42ca70c9.jpg)

![](images/6d472b3120847b036c7bc587108fc1ab2c6f0e5e3bf8d4084522e0a680b49e07.jpg)

Table 2 | Similarities between the experimental distributions of Fig. 3 and the expected ones.  

<table><tr><td>Steps</td><td>Bosons</td><td>Fermions</td><td>Single</td></tr><tr><td>Ordered</td><td></td><td></td><td></td></tr><tr><td>4</td><td>0.948±0.003</td><td>0.923±0.003</td><td>0.997±0.001</td></tr><tr><td>6</td><td>0.943±0.003</td><td>0.866±0.003</td><td>0.997±0.001</td></tr><tr><td>8</td><td>0.768±0.006</td><td>0.780±0.007</td><td>0.957±0.004</td></tr><tr><td>Static disorder</td><td></td><td></td><td></td></tr><tr><td>4</td><td>0.934±0.003</td><td>0.904±0.004</td><td>0.993±0.001</td></tr><tr><td>6</td><td>0.905±0.007</td><td>0.914±0.004</td><td>0.986±0.002</td></tr><tr><td>8</td><td>0.830±0.004</td><td>0.802±0.004</td><td>0.954±0.002</td></tr></table>

Uncertainties arise from the Poisson distribution of counting statistics.

Supplementary Section SV, polarization-entangled photon pairs, generated via spontaneous parametric downconversion, were simultaneously injected into arms  $A$  and  $B$  of the four-, six- and eight-step QW circuits. As anticipated in the introduction and illustrated in ref. 14, different quantum statistics of two test particles can be simulated through the polarization entanglement of a biphoton state (for the sake of completeness full details on this theoretical construction are reported in Supplementary Section SII). In particular, by setting the phase  $\varphi$  of the state  $|\Psi (\varphi)\rangle = \frac{1}{\sqrt{2}}\left[|\psi_A;H\rangle |\psi_B;V\rangle +e^{i\varphi}|\psi_B;H\rangle |\psi_A;V\rangle \right]$  to  $\varphi = 0$  or  $\varphi = \pi$ , bosonic or fermionic QWs were observed, respectively.

The graphs in Fig. 3 show, for different numbers of steps, the experimentally measured symmetric joint probabilities  $P_{j,k}^{(\pm,\mathrm{sym})} = P_{k,j}^{(\pm,\mathrm{sym})}$  of detecting one particle in the output port  $j$  and the other in the output port  $k$  independently from their polarization, when a bosonic  $(|\Psi^{(+)}\rangle = |\Psi(0)\rangle)$  or a fermionic  $(|\Psi^{(-)}\rangle = |\Psi(\pi)\rangle)$  two-particle input state is injected into the device. The different panels compare the ordered and disordered cases for input states with symmetric and antisymmetric wavefunctions. The case of single photons is also retrieved by tracing out the position of one of the particles of the entangled pair obtaining the distributions  $P_j^{(\pm)} = \sum_k P_{j,k}^{(\pm,\mathrm{sym})}$ , which do not depend upon the symmetry of the input state (see Supplementary Section SII for details). Whereas in the case of an ordered system the walkers spread ballistically with increasing number of steps, particle propagation is progressively quenched in the case of static disorder; Anderson localization implies that the wave packets remain localized around the central sites. This is indeed what we observe, leading to a difference between the ordered and disordered case that is most evident for the eight-step QW (compare Fig. 3g,h with Fig. 3p,q). In addition, qualitatively different correlation patterns are observed for input states with bosonic or fermionic symmetry, showing a marked influence of the quantum statistics on the localization of the particle pair. The agreement of the experimental data with theoretical predictions, again quantified by the similarities, is reported in Table 2. One may note that in the ordered case  $S$  is slightly worse for the eight-step QW. This discrepancy, due to some unavoidable uncertainty in beamsplitter realization, is milder in the disordered case. Here, as expected, additional phase shift to the 'intentionally chosen' random one will have less effect due to localization.

# Localization properties of bosonic and fermionic pairs

Different figures of merit have been adopted in the literature to provide a quantitative estimate of the localization properties, such as localization length $^{47}$  or variance of the single-particle distribution $^{11,48}$ . The latter proved to be particularly useful for comparing the effects of different kinds of disorder $^{49}$ . However, when a pair of particles is concerned, different parameters may be adopted. The state of a system composed of two indistinguishable particles walking on a line can be described by two coordinates: their mean position  $x_{\mathrm{M}} = (j + k) / 2$  ( $j$  and  $k$  label different sites) and their relative distance  $R = j - k$ . It turns out to be very convenient to measure

the spread of the collective wavefunction through the variance of both quantities. Figure 4a,b,d,e shows the variance of  $x_{\mathrm{M}}$  and  $R$ , calculated from the probability distributions  $P_{j,k}^{(\pm ,\mathrm{sym})}$  of Fig. 3 as a function of the number of steps. Although in the case of an ordered QW the two quantities grow quadratically with the number of steps  $n$ , due to the ballistic spread of the wavefunction<sup>14</sup>, they become only slightly dependent on  $n$  in the case of static disorder, indicating that the system tends towards localization

![](images/0138b0e38feb2d210ffab8fcbbc2b37c9ace842c0aec4a6d8180f54340101985.jpg)

![](images/539750fb20e310c15599a6af46484f890381df37f74f1544cf3924ef2f4bf7f3.jpg)

![](images/cdc19f494fc9a94f0d1e322dbd536779216d3965cc1667f282781acd66df1087.jpg)

![](images/3a86242240ecee185c802b00306367a90598d90b51df76cbbfae4470d8036e41.jpg)

![](images/d5e414dc5cbf493592b59c43a026648c8499ecd8ff961adaaa3561b5c5264638.jpg)

![](images/dfb288ea5dde0f142e993cfe65c07bb85a96de0ab9c59711b6aef96bf167e581.jpg)

![](images/29debc9cd6055db8de5a593c07c40e68e84552d07135b208e1a7d1d3c4ef27f5.jpg)  
Figure 4 | Localization properties of two-photon wave packets. a-f, Variance of the two-photon mean position  $x_{\mathrm{M}} = (j + k) / 2$  (a-c) and of the relative distance  $R = j - k$  (d-f) shown as a function of the number of steps. Experimental results are reported for bosons (circles) and fermions (squares). Open symbols correspond to ordered QWs, and filled symbols to QWs with static disorder. Error bars are smaller than the size of the symbols. Curves represent theoretical behaviours, and are calculated by taking into account QW networks presenting the nominal pattern of phases implemented on each chip. The slight mismatch between theoretical values and experimental data is due both to non-perfect chip fabrication and input state preparation.

![](images/75c6cf1e7c8c9c3fa97e60b0718576da8db6119d55c40561bde311465192f415.jpg)

![](images/3709e74fec685face030f0506406e8445bd8915175aac596964879dcf09ec2c1.jpg)

![](images/b93a06e91452e0a16b6becd2b32fd282c6ddc4967dd14c92e968831d913a6a01.jpg)  
Figure 5 | Relative distance of two-photon walkers. a-d, Probability distributions of the absolute value of the relative distance  $|R|$  for bosonic (left) and fermionic (right) two-photon eight-step QWs for the case of an ordered QW (a,b) and in the presence of static disorder (c,d).

![](images/942c8d64df21ce3c0c9cb2950b1e922ccd4fb2f4c40cc29327e99a21e99fcbd8.jpg)

(see, for instance, ref. 48 for a similar analysis in the context of dynamical localization). Numerical simulations, performed by considering discrete time QWs with random configurations of static disorder, show that the tendency to localization is generally visible

even with a relatively small number of steps. A fully localized state is predicted for  $n \approx 100$ , currently out of reach for any technological platform. Anyway, the difference observed in our experiment between ordered and disordered QWs confirms that the onset of Anderson localization can already be observed after a small number of steps.

Figure 4c,f compares, in the same graphs, data for the bosonic and fermionic symmetry of the input state. Interestingly, it can be observed that the 'centre of mass'  $x_{\mathrm{M}}$  of two fermions undergoes stronger localization, in the same disordered potential, if compared to two bosons (Fig. 4c); the opposite is observed for the relative distance  $R$ . The latter feature can also be appreciated from Fig. 5, which reports the measured distribution of the absolute value of this quantity (that is,  $|R|$ ) in the eight-step QW case. Again, one can observe how the distribution of  $|R|$  spreads more in the ordered QW (Fig. 5a,b) than in the statically disordered one (Fig. 5c,d), where the stronger contributions for small values of  $|R|$  indicate the localization trend. More notably, when an antisymmetric two-particle state is injected, the probability associated with  $|R| = 0$  drops (Fig. 5d) because of the Pauli exclusion principle. This explains why, in the presence of Anderson localization, a less pronounced contraction of the final two-particle distribution is observed in the case of the fermionic symmetry of the input state.

A deeper comprehension of these different localization properties of fermionic states with respect to bosonic ones can be achieved by calculating the general expressions of the variance of  $x_{\mathrm{M}}$  and  $R$

![](images/4ecd57c3c90caa59fbd980e6289a1d2f7563b673f46c2ba98d640277f0d3af36.jpg)

![](images/14a57641cb78251ad2683bf25de6f00e3138a88031e3cec435fbd1b5fdda3610.jpg)

![](images/174df48639c98edf3fa5d316b92a3d74528b41a2a473d768855517761fa32449.jpg)

![](images/f65e2066682ca64bef545ed75d27724750cb124a301d2644f5d3956c531eb127.jpg)

![](images/405acff3e1b8173b52bf2f5fb7195ba5bb9ea918bd3e8ca03d875babcc54aad6.jpg)

![](images/5f9b19c19cac8349ea54859462ef678da642eaef62cc21c65b1cce0dc34998d0.jpg)

![](images/9ea04189846c7db2d0dfd4e6320ce9bf048adc917e6bf183de0fe278a215426f.jpg)  
Figure 6 | Measured output probabilities for QWs with dynamic disorder. a-f, Single- and two-particle distributions for a six-step QW in the presence of space-correlated (a-c) and completely uncorrelated (d-f) dynamic disorder (each normalized to its maximum). Single-particle distributions were computed by tracing out the position of one of the particles (summing over the columns of the probability distribution matrices). The similarities for bosons, fermions and a single particle with the expected distributions are, respectively,  $S_{\mathrm{Bos}}^{D} = 0.874 \pm 0.003$ ,  $S_{\mathrm{Fe}}^{D} = 0.812 \pm 0.006$  and  $S_{\mathrm{Sing}}^{D} = 0.977 \pm 0.003$  for the QW circuit with space-correlated dynamic disorder and  $S_{\mathrm{Bos}}^{F} = 0.935 \pm 0.004$ ,  $S_{\mathrm{Fe}}^{D} = 0.870 \pm 0.003$  and  $S_{\mathrm{Sing}}^{F} = 0.993 \pm 0.002$  for the chip with uncorrelated dynamic disorder.

for bosonic and fermionic input states. As discussed explicitly in Supplementary Section SIII these can be expressed as

$$
\mathrm {V a r} ^ {(\pm)} (x _ {\mathrm {M}}) = [ \Delta_ {A} ^ {2} + \Delta_ {B} ^ {2} \pm \Delta_ {A B} ^ {2} ] / 2
$$

$$
\mathrm {V a r} ^ {(\pm)} (R) = \Delta_ {A} ^ {2} + \Delta_ {B} ^ {2} \mp \Delta_ {A B} ^ {2} + [ x _ {A} - x _ {B} ] ^ {2}
$$

the  $\pm$  sign being associated with the simulation of bosonic  $(\Psi^{+})$  or fermionic  $(\Psi^{-})$  statistics. In these equations,  $x_{Q}$  and  $\Delta_Q^2$  are, respectively, the mean position and the position spread one would obtain if only one particle was injected into the setup from the input port  $Q = A$ ,  $B$ , while  $\Delta_{AB}^{2}$  is a non-negative term arising from two-particle interference. We notice that, independently of the specific properties of the single-particle contribution terms, the two functionals respond quite differently at the particle statistics. As a consequence of the positivity of the interference term  $\Delta_{AB}^{2}$ , one has, for the variance of the mean position,

$$
\mathrm {V a r} ^ {(+)} (x _ {\mathrm {M}}) \geq \mathrm {V a r} ^ {(-)} (x _ {\mathrm {M}})
$$

Hence, the centre of mass of two fermions is better localized than that of two bosons. In contrast, for the relative distance  $R$ , in agreement with what one would expect from the Pauli principle, one has

$$
\operatorname {V a r} ^ {(-)} (R) \geq \operatorname {V a r} ^ {(+)} (R)
$$

which is smaller in the bosonic case than in the fermionic case, reflecting their bunching/antibunching tendency.

# QW with dynamic disorder

So far, we have discussed the case of static, time-independent disorder. However, different types of disorder, in which a time dependence is also considered, affect the evolution of the entangled pair wavefunction differently. As our technology is capable of implementing arbitrary phase maps in the QWs, we studied two more cases, namely two six-steps QWs with different dynamic disorder configurations (for more details see Supplementary Section SI). In the first, we applied the same (random) phase shift to the beamsplitters belonging to the same time step of the walk  $(\varphi_{m,n} = \varphi_n,\forall m)$ ; a fully space-correlated randomness may simulate the dephasing effect of a time-varying external environment on a spatially ordered structure. In the second case we applied a completely uncorrelated map of phase shifts  $\varphi_{m,n}$  to the beamsplitter network; this simulates external decoherence effects on spatially disordered lattices.

Experimental single- and two-photon output distributions are summarized in Fig. 6 for the bosonic and fermionic cases separately. Comparing Fig. 6a,b to the output distributions of the ordered case (Fig. 3d,e) it is clear that the effect of space-correlated randomness is to destroy the ballistic spread and force the system towards a diffusive behaviour. On the other hand, comparing Fig. 6c,d to the output distributions of the static case (Fig. 3m,n), we observe that the onset of dynamic disorder actually quenches the Anderson localization effects, and the distribution is far less localized. As a matter of fact, simulations with a high number of steps and different random phase maps show that the limit distribution is, for both types of disorder, a binomial centred in the middle of the spatial axis, with width growing with the square root of the number of steps. This means that, in both cases, the system evolution converges to a diffusion process, equivalent to a purely classical random walk. However, the early evolution qualitatively differs in the two cases, as appears clearly by comparing Fig. 6a,b and Fig. 6c,d.

Let us note that the experiments presented in this work were performed on a single phase map realization of each disorder. Although there are still features that are linked to the particular choice of the (randomly picked) phase maps, the number of beamsplitters is large

enough to observe the differences between ballistic, diffusive and localized regimes.

# Discussion

We have reported on the experimental realization of a quantum simulator based on discrete quantum walks of entangled particles in integrated photonic circuits. By properly engineering the phase shifts at the output ports of the beamsplitters and by changing the number of QW steps, we were able to follow in real time the evolution towards Anderson localization. The symmetry of the total wavefunction (Fermi- or Bose-like) clearly affects the localization properties. The quantum simulation we performed will help to ascertain the efficiency of quantum algorithms with entangled particles on realistic QWs. The capability of our technology to implement arbitrary phase maps in QWs will enable the experimental quantum simulation of the quantum dynamics of multiparticle correlated systems and its ramifications towards the implementation of realistic universal quantum computation with QWs. We envisage the development of an integrated photonic system that implements arbitrary phase and reflectivity maps, enabling the realization of any kind of unitary transformation within the optical network. This will pave the way towards genuine hard-to-simulate, scalable quantum linear optical circuits[50].

# Methods

Fabrication of the photonic circuits. For the fabrication of the integrated photonic circuits used in these experiments, pulses with  $220\mathrm{nJ}$  energy,  $\sim 300$  fs duration and  $1\mathrm{MHz}$  repetition rate from a Yb:KYW cavity dumped oscillator were focused by a  $\times 50$ , 0.6 NA microscope objective. The substrate was Corning EAGLE2000 borosilicate glass. The translation speed of the sample for inscribing the waveguides was fixed at  $40\mathrm{mm~s^{-1}}$ . Waveguides were fabricated  $170~{\mu\mathrm{m}}$  below the sample surface. The low birefringence  $(\sim 7\times 10^{-5})$  of this kind of waveguide has proven to allow the propagation of polarization-encoded qubits preserving coherence and entanglement<sup>37</sup>.

Received 24 July 2012; accepted 18 January 2013; published online 3 March 2013

# References

1. Anderson, P. Absence of diffusion in certain random lattices. Phys. Rev. 109, 1492-1505 (1958).  
2. Abrahams, E. 50 years of Anderson Localization (World Scientific, 2010).  
3. Roati, G. et al. Anderson localization of a non-interacting Bose-Einstein condensate. Nature 453, 895-898 (2008).  
4. Billy, J. et al. Direct observation of Anderson localization of matter waves in a controlled disorder. Nature 453, 891-894 (2008).  
5. Wiersma, D. S., Bartolini, P., Lagendijk, A. & Righini, R. Localization of light in a disordered medium. Nature 390, 671-673 (1997).  
6. Conti, C. & Fratalocchi, A. Dynamic light diffusion, three-dimensional Anderson localization and lasing in inverted opals. Nature Phys. 4, 794-798 (2008).  
7. Pertsch, T. et al. Nonlinearity and disorder in fiber arrays. Phys. Rev. Lett. 93, 053901 (2004).  
8. Schwartz, T., Bartal, G., Fishman, S. & Segev, M. Transport and Anderson localization in disordered two-dimensional photonic lattices. Nature 446, 52-55 (2007).  
9. Lahini, Y. et al. Anderson localization and nonlinearity in one-dimensional disordered photonic lattices. Phys. Rev. Lett. 100, 013906 (2008).  
10. Broome, M. A. et al. Discrete single-photon quantum walks with tunable decoherence. Phys. Rev. Lett. 104, 153602 (2010).  
11. Schreiber, A. et al. Decoherence and disorder in quantum walks: from ballistic spread to localization. Phys. Rev. Lett. 106, 180403 (2011).  
12. Störzer, M., Gross, P., Aegerter, C. M. & Maret, G. Observation of the critical regime near Anderson localization of light. Phys. Rev. Lett. 96, 063904 (2006).  
13. Hu, H., Strybulevych, A., Page, J. H., Skipetrov, S. E. & van Tiggelen, B. A. Localization of ultrasound in a three-dimensional elastic network. Nature Phys. 4, 945-948 (2008).  
14. Omar, Y., Paunkovic, N. & Bose, L. S. S. Quantum walk on a line with two entangled particles. Phys. Rev. A 74, 042304 (2006).  
15. Beenakker, C., Venderbos, J. & van Exter, M. Two-photon speckle as a probe of multi-dimensional entanglement. Phys. Rev. Lett. 102, 193601 (2009).  
16. Lahini, Y., Bromberg, Y., Christodoulides, D. N. & Silberberg, Y. Quantum correlations in two-particle Anderson localization. Phys. Rev. Lett. 105, 163905 (2010).

17. Bromberg, Y., Lahini, Y., Morandotti, R. & Silberberg, Y. Quantum and classical correlations in waveguide lattices. Phys. Rev. Lett. 102, 253904 (2009).  
18. Shepelyansky, D. Coherent propagation of two interacting particles in a random potential. Phys. Rev. Lett. 73, 2607-2610 (1994).  
19. Sansoni, L. et al. Two-particle bosonic-fermionic quantum walk via integrated photonics. Phys. Rev. Lett. 108, 010502 (2012).  
20. Kempe, J. Quantum random walks: an introductory overview. Contemp. Phys. 44, 307-327 (2003).  
21. Potocek, V., Gabris, A., Kiss, T. & Jex, I. Optimized quantum random-walk search algorithms on the hypercube. Phys. Rev. A 79, 012325 (2009).  
22. Childs, A. M. Universal computation by quantum walk. Phys. Rev. Lett. 102, 180501 (2009).  
23. Mohseni, M., Rebentrost, P., Lloyd, S. & Aspuru-Guzik, A. Environment-assisted quantum walks in photosynthetic energy transfer. J. Chem. Phys. 129, 174106 (2008).  
24. Rebentrost, P., Mohseni, M., Kassal, I., Lloyd, S. & Aspuru-Guzik, A. Environment-assisted quantum transport. New J. Phys. 11, 033003 (2009).  
25. Karski, M. et al. Quantum walk in position space with single optically trapped atoms. Science 325, 174-177 (2009).  
26. Schmitz, H. et al. Quantum walk of a trapped ion in phase space. Phys. Rev. Lett. 103, 090504 (2009).  
27. Zahringer, F. et al. Realization of a quantum walk with one and two trapped ions. Phys. Rev. Lett. 104, 100503 (2010).  
28. Ryan, C. A., Laforest, M., Boileau, J. C. & Laflamme, R. Experimental implementation of a discrete-time quantum random walk on an NMR quantum-information processor. Phys. Rev. A 72, 062317 (2005).  
29. Perets, H. B. et al. Realization of quantum walks with negligible decoherence in waveguide lattices. Phys. Rev. Lett. 100, 170506 (2008).  
30. Kitagawa, T. et al. Observation of topologically protected bound states in photonic quantum walks. Nature Commun. 3, 882 (2012).  
31. Schreiber, A. et al. A 2D quantum walk simulation of two-particle dynamics. Science 336, 55-58 (2012).  
32. Peruzzo, A. et al. Quantum walks of correlated photons. Science 329, 1500-1503 (2010).  
33. Owens, J. O. et al. Two-photon quantum walks in an elliptical direct-write waveguide array. New J. Phys. 13, 075003 (2011).  
34. O'Brien, J. L., Furusawa, A. & Vuckovic, J. Photonic quantum technologies. Nature Photon. 3, 687-695 (2009).  
35. Politi, A., Cryan, M. J., Rarity, J. G., Yu, S. & O'Brien, J. L. Silica-on-silicon waveguide quantum circuits. Science 320, 646-649 (2008).  
36. Laing, A. et al. High-fidelity operation of quantum photonic circuits. Appl. Phys. Lett. 97, 211108 (2010).  
37. Sansoni, L. et al. Polarization entangled state measurement on a chip. Phys. Rev. Lett. 105, 200503 (2010).  
38. Crespi, A. et al. Integrated photonic quantum gates for polarization qubits. Nature Commun. 2, 566 (2011).  
39. Politi, A., Matthews, J. C. F. & O'Brien, J. L. Shor's quantum factoring algorithm on a photonic chip. Science 325, 1221 (2009).  
40. Matthews, J. C. F. et al. Simulating quantum statistics with entangled photons: a continuous transition from bosons to fermions. Preprint at http://lanl.arxiv.org/abs/1106.1166 (2011).

41. Smith, B. J., Kundys, D., Thomas-Peter, N., Smith, P. G. R. & Walmsley, I. A. Phase-controlled integrated photonic quantum circuits. Opt. Express 17, 13516-13525 (2009).  
42. Matthews, J. C. F., Politi, A., Stefanov, A. & O'Brien, J. L. Manipulation of multiphoton entanglement in waveguide quantum circuits. Nature Photon. 3, 346-350 (2009).  
43. Crespi, A. et al. Measuring protein concentration with entangled photons. Appl. Phys. Lett. 100, 233704 (2012).  
44. Osellame, R., Cerullo, G. & Ramponi, R. Femtosecond Laser Micromachining: Photonic and Microfluidic Devices in Transparent Materials, Topics in Applied Physics Vol. 123 (Springer, 2012).  
45. Gattass, R. R. & Mazur, E. Femtosecond laser micromachining in transparent materials. Nature Photon. 2, 219-225 (2008).  
46. Della Valle, G., Osellame, R. & Laporta, P. Micromachining of photonic devices by femtosecond laser pulses. J. Opt. A 11, 049801 (2009).  
47. Molinari, D. & Fratalocchi, A. Route to strong localization of light: the role of disorder. Opt. Express 20, 18156-18164 (2012).  
48. Terraneo, M. & Shepelyansky, D. L. Dynamical localization and repeated measurements in a quantum computation process. Phys. Rev. Lett. 92, 037902 (2004).  
49. Yin, Y., Katsanos, D. E. & Evangelou, S. N. Quantum walks on a random environment. Phys. Rev. A 77, 022302 (2008).  
50. Aaronson, S. & Arkhipov, A. The computational complexity of linear optics. Preprint at http://lanl.arxiv.org/abs/1011.3245 (2010).

# Acknowledgements

This project was supported by FIRB (Fondo per gli investimenti della ricerca di base) - Futuro in Ricerca HYTEQ (Hybrid Technologies for Quantum Information Processing), PRIN 2009 (Progetti di Ricerca di Interesse Nazionale 2009), IP-SOLID (Integrated Project 'Solid State Systems for Quantum Information Processing', grant agreement no. FP7 248629) and ERC (European Research Council)—Starting Grant 3D-QUEST (3D-Quantum Integrated Optical Simulation; grant agreement no. 307783).

# Author contributions

L.S., F.D.N., F.S., P.M., A.C., R.O. and R.R. conceived the experimental approach for simulation of the Anderson localization. A.C., R.O. and R.R. fabricated the integrated devices and performed the characterization with classical light. L.S., F.D.N., F.S. and P.M. carried out the quantum experiments. V.G. and R.F. contributed to the theoretical analysis on how statistics influences localization. All authors discussed the experimental implementation and results and contributed to writing the paper.

# Additional information

Supplementary information is available in the online version of the paper. Reprints and permissions information is available online at www.nature.com/reprints. Correspondence and requests for materials should be addressed to R.O. and F.S.

# Competing financial interests

The authors declare no competing financial interests.