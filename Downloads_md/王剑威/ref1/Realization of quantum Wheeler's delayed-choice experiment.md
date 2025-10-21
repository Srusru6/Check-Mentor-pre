# Realization of quantum Wheeler's delayed-choice experiment

Jian-Shun Tang, Yu-Long Li, Xiao-Ye Xu, Guo-Yong Xiang, Chuan-Feng Li* and Guang-Can Guo

Light is believed to exhibit wave-particle duality<sup>1</sup> depending on the detecting devices, according to Bohr's complementarity principle<sup>2</sup>, as has been demonstrated by the 'delayed-choice experiment' with classical detecting devices<sup>3-9</sup>. A recent proposal<sup>10</sup> suggests that the detecting device can also occupy a quantum state, and a quantum version of the delayed-choice experiment can be performed. Here, we experimentally realize the quantum delayed-choice experiment and observe the wave-particle morphing phenomenon of a single photon. We also illustrate, for the first time, the behaviour of the quantum wave-particle superposition state of a single photon. We find that the quantum wave-particle superposition state is distinct from the classical mixture state because of quantum interference between the wave and particle states. Our work reveals the deep relationship between the complementarity principle and the superposition principle, and it may be helpful in furthering understanding of the behaviour of light.

Consideration of the dual wave-particle nature of light has a long history that can be traced back to the age of Aristotle. After centuries of debate $^{11-13}$ , it was finally confirmed that light is both a wave and a particle (wave-particle duality) $^{1}$ . A well-known experiment that provides evidence for this is Young's double-slit experiment $^{14}$ , where interference fringes are created on a screen behind two narrow openings. This phenomenon clearly demonstrates the wave nature of light. However, when the screen is removed, the detector behind the screen only detects photons coming from a single slit at a time $^{3}$ , illustrating the particle property of light. In other words, the detecting device appears to determine which property of light will be exhibited. Bohr explains this phenomenon with the complementarity principle, which states that the property of an object to be shown depends on the arrangement of the detecting setup $^{2}$ . There is an alternative viewpoint, where the photon somehow knows the type of detecting device, and sets its property to the corresponding one so as to go through the slits. To examine this idea, Wheeler (first mentioned by von Weizsacker $^{15,16}$ ) proposed an experiment in which the detection mode was revealed only after the photon had passed the slits; this is known as the delayed-choice thought experiment $^{3,17,18}$ . Since then, some modified versions of this experiment have been conducted $^{4-7}$ , for example using low-velocity atoms $^{4}$  or the delayed-choice quantum eraser $^{5}$ . The original version of this experiment was first realized using a fast electronic device $^{8,9}$ , and the delayed-choice entanglement swapping experiment, which studies the entanglement-separability duality for two photons, was also realized $^{19}$ . The results of these works concur with Bohr's theory and deny the idea that there is some hidden information by which the photon knows what property to exhibit before it reaches the slits.

Recently, a quantum version of the delayed-choice experiment was proposed $^{10,20}$  that uses a quantum detection device in place of the classical one. The logic diagrams of the 'classical' and 'quantum' delayed-choice experiments are shown in Fig. 1, with Fig. 1a

corresponding to the classical case and Fig. 1b the quantum case. Details about the advantage of the quantum delayed-choice experiment are provided in Supplementary Section S2.

In this Letter, we experimentally demonstrate the quantum delayed-choice experiment with a series of single photons emitted from an InAs/GaAs self-assembled quantum dot (SAQD) $^{21}$ . We observe the morphing between the wave and particle properties of these photons. More strikingly, we derive the quantum superposition of the wave and particle properties by selecting the quantum detecting device in the superposition state rather than the eigenstates (in a Mach-Zehnder interferometer (MZI), the eigenstates are the presence or absence of the second beamsplitter (BS)). We show that the quantum wave-particle superposition can be very different from the classical mixture by comparing their interference fringes under various conditions.

The theoretical frame and experimental set-up (Fig. 2) are described in the Methods, and the results are shown in Fig. 3. In Fig. 3a-h,  $\alpha$  (Fig. 2) takes the values of  $j\pi /8$  ( $j = 0 - 7$ ). The red symbols are the results of the classical wave-particle mixture, and the red lines show the corresponding theoretical fit. The theoretical formula is directly derived from equation (2) (see Methods) by calculating the probability that the photons take path 1. Unsurprisingly, the photons all go through the wave layer in Fig. 3a, so we observe an oscillation with a visibility of 0.957.

In Fig. 3e, the photons all go through the particle layer, so the detected probability remains  $\sim 0.5$ , with a visibility of 0.016. In this case,  $g^{(2)}(0)$  is measured to be  $0.167 \pm 0.062$ , clearly showing the particle property of the photon. The non-ideal value of  $g^{(2)}(0)$  is caused by the impurity of the SAQD photoluminescence. We also measure the distinguishability of path 1 to be

![](images/26557937837e09d40ecd357fc0aacf5e04b8b3a744e97af1c5710d338471975c.jpg)  
Figure 1 | Logic diagrams of the classical and quantum delayed-choice experiments. a,b, The classical (a) and quantum (b) experiments. The first H (Hadamard) gate corresponds to the splitting of the two paths, after which a  $\varphi$  phase is added. The second H gate corresponds to the detecting device, which is controlled by an ancilla. The set-ups differ in the following way. In a, the ancilla  $|pol\rangle = \sin \alpha |V\rangle +\cos \alpha |H\rangle$  is first detected on the basis of  $\{|H\rangle ,|V\rangle \}$  to generate a series of random numbers,  $p,$  and these numbers are used to control the second H gate. In b, the ancilla  $|pol\rangle$  is directly used to control the second H gate, placing the gate in a quantum-superposition state of producing and not producing interference fringes. QRNG represents a quantum random number generator.

![](images/38a346e2e849ba0ca8f3299e84d831d934df01379398162247c00c754020e644.jpg)

![](images/962b9a3c98afa98f2e44c645864c3f5c28b6b5ce5a8a19c861a8aced3407f593.jpg)  
Figure 2 | Experimental set-up. The set-up includes four parts: single photons generated by the SAQD (not shown), the opened (closed) MZI (quartz, BD1, BD3, HWP1 (HWP2), BD4), the quantum-control apparatus ( $\alpha$ , BD2, particle layer, wave layer, BD5), and the detection apparatus (movable polarizer, APDs and the counter and time analyser, which are not shown). Note: the arrows are used to represent the photon polarizations, and the HWPs are not shown; 'Layer' in the lower figure represents a detailed sketch of the particle and wave layers.

$D = 0.973 \pm 0.003$ , which is defined as

$$
D = \frac {\left| N _ {0 1} - N _ {1 1} \right|}{N _ {0 1} + N _ {1 1}}
$$

where  $N_{ij}$ $(i,j = 0,1)$  is the detected photon number of path  $j$  when path  $i$  is unblocked (and the other path blocked). The which-path information is almost fully extracted. Further details of the definition and distinguishability for other cases have been addressed elsewhere[22].

We see a mixing of Fig. 3a and Fig. 3e in the intermediate cases. The visibilities become small, but the centres (that is, the average of the maximum and minimum) and the curve shapes do not change. The differences between the experimental and theoretical values are caused by the counting statistics, the dark and background counts, and the tiny instability of the MZIs.

However, the situation is different for the quantum wave-particle superposition, as shown by the blue symbols in Fig. 3. The blue lines show the corresponding theoretical fit, derived from equation (3) (see Methods). The fitting parameters  $\delta_0$  and  $\delta_{1}$  change very little, which further illustrates the stability of our experimental set-up. Except in the cases of  $\alpha = 0$  and  $\pi /2$ , in which the photons all go through the particle layer or the wave layer, the curves are strikingly different between the quantum-superposition and classical-mixture cases.

To show these differences more comprehensively, we extracted three quantities from Fig. 3: the centre of the curve, the visibility and the ratio of the rise period to the total period ('centre', 'visibility' and 'ratio' for short). The results are shown in Fig. 4. The red symbols show the classical wave-particle mixture, and the blue symbols the quantum superposition. The larger symbols show the experimental results taken from Fig. 3, and the smaller symbols the theoretical simulation results. More analyses are found in Supplementary Section S3.

We should note that, although we use terminology that refers to the 'classical mixture' and the 'quantum superposition' of wave-particle properties due to equation (2) and equation (3) (see Methods), both terms reflect the results of the quantum delayed-choice experiment because the primary character of the

'quantum' here is the use of a quantum detecting device (pc-BS). When the single photon reaches BD2 (beam displacer) it has completely passed BD1, because the 3 ns delay is somewhat larger than the 0.563 ns time duration of this photon. The photon makes a choice, but because the pc-BS remains at a quantum superposition of the eigenstates (presence and absence, corresponding to  $|H\rangle$  and  $|V\rangle$ , respectively), the photon can never know which choice it has made, even after it has passed the pc-BS; that choice is only revealed when the state of the pc-BS is detected on the eigenstates. Therefore, in this scheme, the photon cannot know the state of the detecting device before it passes BD1 in order to adjust itself to exhibit the corresponding property. The hidden-information theory is denied once again.

By tracing out the pc-BS states, the results of the collapse for both the presence state and the absence state are summed. Because of this summation, it is convenient for us to detect directly the number of whole photons in the same path, without splitting them with a horizontally placed polarization beamsplitter and then summing them again. This process produces the classically mixed results that we presented previously, that is, the morphing between oscillation and non-oscillation states.

It is interesting to consider what will happen if the pc-BS is not collapsed to the eigenstates, but to a superposition state, such as  $(1 / \sqrt{2})(|presence\rangle + |absence\rangle)$  (corresponding to  $|+\rangle$ ). This is a novel scenario that can be realized with a quantum beamsplitter experiment. equation (3) (see Methods) shows that the result is a quantum superposition of the wave and particle states of the photon, as opposed to a classical statistical mixture of the two states. The experimental results give a completely different result from the classical mixture, because there is quantum interference between the wave and particle properties. This phenomenon has not previously been revealed, and brings a whole new meaning to the concept of wave-particle duality.

The application of a quantum detecting device leads to a reinterpretation of the complementarity principle $^{10}$ , because the detecting device should be classical according to the regular concept. The same problem also appears in many experiments that are the foundations of quantum mechanics, such as the Bell inequality test $^{23}$ , the Kochen-Specker inequality test $^{24}$ , and

![](images/0935ce027db7b39dab6ff0fead20add66166ed99354b0a6894a0552efc127d9b.jpg)

![](images/a97477c7458f99068efce34a8830dbb8243c41d383d4f1a4f76e747de4a5c352.jpg)

![](images/2fb1b86f531d5536eac654e5dbafd283aeb000d61f2e55677c9327fd01fb3fcb.jpg)

![](images/618503d0eed53835c2e8b2392f7507bc9cc4ff77566a9f1df906d1687b7a12d2.jpg)

![](images/9c6ce49b0b1e6b4d9754221e592d7e476850eeb9d7d4c517975bb0e1d51b7ea4.jpg)

![](images/56907d160a765b034291c4ab1b9ff43626f135999722b2416d1dc44f45057511.jpg)

![](images/0f4e5b7ae851c22aa79fc48657e8d7fe1e8aa9caa5231a4ae55c0c4f2bc28e3c.jpg)  
Figure 3 | Probabilities of finding a photon in path 1. From a to h,  $\alpha = j\pi /8$  ( $j = 0$  to 7). The red symbols are the results of the classical wave-particle mixture, and the blue symbols the quantum superposition. The lines show the corresponding theoretical fit.

![](images/77affaf0ce90987b850be8d271632085df7082e7a638d4ef67b6acab8f9751c3.jpg)

so on. Using a quantum detecting device instead of a classical device, these experiments may be extended to further studies on new concepts. For example, in the regular experiment testing the complementarity principle, the classical detecting device leads to two types of inequality[9,25-27]. One is the Englert-Greenberger duality relation, that is,  $V^2 + D^2 \leq 1$ . However, the interference between the wave and particle properties introduced by the quantum detecting device will make a small generalization for this duality relation and cause an extension of the complementarity principle[22].

In summary, we have realized the quantum delayed-choice experiment with single photons. Moreover, we have observed the quantum wave-particle duality of these photons, and compared the results with those for a classical wave-particle mixture. We found that the quantum wave-particle superposition is distinct from the classical mixture because of quantum interference between the wave and particle properties of the photon. We conclude that these two properties can not only morph from one another, but can also exist in a quantum superposition.

![](images/0c69bdb1bd3cd1c9327770aa23c3838f438a0dd3fee9ab0959043dc2f7a9ea4d.jpg)

![](images/280750dfeca625a9ea714319f1384a2bcf5cec9af941b7fab05934155b6812b7.jpg)

![](images/e2f5ef6e950d9dad9fa81b79d9b83cefd65b72aeadcd1fa890c3f4b3a85e065f.jpg)  
Figure 4 | Three quantities (centre, visibility and ratio) derived from Fig. 3.

a, 'Centre' is the average of the maximum and minimum probabilities.  
b, 'Visibility' is the ratio of the oscillation amplitude to the sum of the maximum and minimum probabilities. c, 'Ratio' indicates the ratio of the rise period to the total period. The larger symbols are experimental results and the smaller symbols the theoretical simulation results.

# Methods

Theoretical frame. In the present experiment the polarization state was taken as the ancilla. The horizontally polarized photons  $(|H\rangle)$  can pass through a second beamsplitter (closed MZI), but there is no second beamsplitter in the path of the vertically polarized photons  $(|V\rangle)$  (open MZI). We refer to this configuration as a polarization-controlled beamsplitter (pc-BS). As stated in ref. 10 (Fig. 1), when the ancilla state is chosen to be  $|pol\rangle = \sin \alpha |V\rangle +\cos \alpha |H\rangle$ , the total state of the photon will be

$$
| \psi \rangle = \sin \alpha | p a r t i c l e \rangle | V \rangle + \cos \alpha | w a v e \rangle | H \rangle \tag {1}
$$

where  $\alpha$  is the polarization angle of  $|pol\rangle$ ,  $|particle\rangle = (1 / \sqrt{2})(|0\rangle + e^{i\varphi}|1\rangle)$  is the particle state, and  $|wave\rangle = e^{i(\varphi / 2)}\cos (\varphi / 2)|0\rangle e^{i\delta_0} - i\sin (\varphi / 2)|1\rangle e^{i\delta_1}$  is the wave state. As in the usual MZI set-up,  $|0\rangle$  and  $|1\rangle$  are the path states of the photon and  $\varphi$  is the phase difference between these two paths.  $\delta_0$  and  $\delta_1$  are two additional constant phases introduced by the experimental set-up.

Here, we should explain the meanings of the notations of 'particle' and 'wave'. As emphasized in ref. 10, the classical concepts of particle and wave do not perfectly translate into quantum language. So, following this reference, we also adopt the operational definitions of 'particle' and 'wave' as representing the 'inability' and 'ability' to produce interference, respectively[6,28]. As  $\varphi$  varies, the probability that we find a photon in path 1 is  $1/2$  and  $\sin^2\varphi/2$  for the particle and wave states, respectively. Moreover, in the case of a completely particle state—that is, when  $\alpha = \pi/2$ —we also measure the antibunching of the single photons ( $g^{(2)}(0)$  should be 0) between the paths of  $|0\rangle$  and  $|1\rangle$  in order to reconfirm the particle property of the

photons, because any theory in which light is treated as a classical wave cannot reproduce the same result. However, this method is not operational for all cases, because for intermediate cases, or even in the completely wave-state case, the  $g^{(2)}(0)$  all remain 0.

Now, if we keep the different polarization states in equation (1) as the man-made labels for the wave and particle properties, we can derive the classical mixture of these two properties by simply tracing out the polarization part. This state can be written as

$$
\rho_ {c} = \sin^ {2} \alpha | \text {p a r t i c l e}) \langle \text {p a r t i c l e} | + \cos^ {2} \alpha | \text {w a v e}) \langle \text {w a v e} | \tag {2}
$$

More importantly, we can also erase this man-made label to recover the superposition state of the photon by post-selecting only the  $| + \rangle = \frac{1}{\sqrt{2}} (|H\rangle + |V\rangle)$  component of the ancilla in equation (1). Hence, we derive the quantum superposition of the wave and particle states as

$$
\left| \psi_ {q} \right\rangle = \sin \alpha | p a t i c l e \rangle + \cos \alpha | w a v e \rangle \tag {3}
$$

Experimental set-up. Our experimental set-up is shown in Fig. 2, constructed to operate according to Fig. 1b and the previous equations (some notes are located in Supplementary Section S5). This set-up can be divided into four parts. First, single photons are generated by our InGa/GaAs SAQD $^{21}$  and separated by a grating $^{29}$ . By fitting the Hanbury-Brown-Twiss (HBT) experimental result (not shown), we derived the time duration for each photon to be 0.563 ns (ref. 30). The second part is the closed and open MZIs corresponding to the two eigenstates of the detecting device. BD1 (associated with the first H gate in Fig. 1b) splits the light equally into two paths with horizontal and vertical polarizations. Because of the polarization difference, we can scan the phase  $\varphi$  by simply tilting the quartz plates before BD1. The second beamsplitter (corresponding to the second H gate) in the closed (open) MZI is provided by BD3, BD4 and HWP2 (HWP1). 'Layer' represents a detailed sketch of the particle layer and the wave layer. For HWP2 in the wave layer, the optical-axis direction  $(\theta)$  is set to  $22.5^{\circ}$  and interference appears, demonstrating the wave property of the photon (closed MZI). For HWP1 in the particle layer  $(\theta = 0^{\circ})$ , the MZI is open. This configuration shows the particle property of the photon.

The third part of the experimental set-up is the quantum-control apparatus. Single photons are prepared with the polarization state  $|pol\rangle$  before BD2, and then controlled by the polarization to go through the particle layer or the wave layer. Each layer corresponds to an eigenstate of the detecting device. The two layers are then combined by BD5, with the photon states exactly coincident with equation (1).

The last part of the set-up performs the detection operation. For the classical wave-particle mixture, we directly count the photon numbers of path 0 and path 1 and calculate the probability of finding a photon in path 1. For the quantum wave-particle superposition, we insert a  $45^{\circ}$  polarizer to post-select the  $|+\rangle$  terms, then count and calculate the probability. Moreover, for the completely particle case, we send electrical pulses generated by the two single-photon avalanche photodiodes (APDs) to a time analyser to test the antibunching  $(g^{(2)}(0))$  of the single photons, reconfirming the particle property of the photons.

# Received 27 January 2012; accepted 20 June 2012; published online 19 August 2012

# References

1. Greiner, W. Quantum Mechanics: An Introduction (Springer, 2001).  
2. Bohr, N. in Quantum Theory and Measurement (eds Wheeler, J. A. & Zurek, W. H.) 9-49 (Princeton University Press, 1984).  
3. Wheeler, J. A. in Mathematical Foundations of Quantum Theory (eds Marlow, A.R.) 9-48 (Academic Press, 1978).  
4. Lawson-Daku, B. J. et al. Delayed choices in atom Stern-Gerlach interferometry. Phys. Rev. A 54, 5042-5047 (1996).  
5. Kim, Y. H., Yu, R., Kulik, S. P., Shih, Y. & Scully, M. O. Delayed 'choice' quantum eraser. Phys. Rev. Lett. 84, 1-5 (2000).  
6. Hellmut, T., Walther, H., Zajonc, A. G. & Schleich, W. Delayed-choice experiments in quantum interference. Phys. Rev. A 35, 2532-2541 (1987).  
7. Baldzuhn, J., Mohler, E. & Martienssen, W. A wave-particle delayed-choice experiment with a single-photon state. Z. Phys. B 77, 347-352 (1989).  
8. Jacques, V. et al. Experimental realization of Wheeler's delayed-choice gedanken experiment. Science 315, 966-968 (2007).  
9. Jacques, V. et al. Delayed-choice test of quantum complementarity with interfering single photons. Phys. Rev. Lett. 100, 220402 (2008).  
10. Ioniciou, R. & Terno, D. R. Proposal for a quantum delayed-choice experiment. Phys. Rev. Lett. 107, 230406 (2011).  
11. Buchwald, J. Z. The Rise of the Wave Theory of Light: Optical Theory and Experiment in the Early Nineteenth Century (University of Chicago Press, 1989).  
12. Planck, M. On the law of distribution of energy in the normal spectrum. Annalen der Physik 4, 553-563 (1901).  
13. Einstein, A. On a heuristic viewpoint concerning the production and transformation of light. Annalen der Physik 17, 132-148 (1905).  
14. Young, T. Experimental demonstration of the general law of the interference of light. Phil. Trans. R. Soc. Lond. 94, 1-16 (1804).

15. von Weizsäcker, C. F. Ortsbestimmung eines elektrons durch ein mikroskop. Z. Phys. 70, 114-130 (1931).  
16. von Weizsäcker, C. F. Zur Deutung der Quantenmechanik. Z. Phys. 118, 489-509 (1941).  
17. Wheeler, J. A. in Quantum Theory and Measurement (eds Wheeler, J. A. & Zurek, W. H.) 182-213 (Princeton University Press, 1984).  
18. Leggett, A. J. in Compendium of Quantum Physics (eds Greenberger, D., Hentschel, K. & Weinert, F.) 161-166 (Springer, 2009).  
19. Ma, X. S. et al. Experimental delayed-choice entanglement swapping. Nature Phys. 8, 479-484 (2012).  
20. Schirber, M. Focus: another step back for wave-particle duality. Physics 4, 102-104 (2011).  
21. Tang, J. S. et al. Direct observation of single InAs/GaAs quantum dot spectrum without mesa or mask. Phys. E 41, 797-800 (2009).  
22. Tang, J. S., Li, Y. L., Li, C. F. & Guo, G. C. Revisiting Bohr's principle of complementarity using a quantum device. Preprint at http://arxiv.org/abs/1204.5304v1 (2012).  
23. Freedman, S. J. & Clauser, J. F. Experimental test of local hidden-variable theories. Phys. Rev. Lett. 28, 938-941 (1972).  
24. Huang, Y. F., Li, C. F., Zhang, Y. S., Pan, J. W. & Guo, G. C. Experimental test of the Kochen-Specker theorem with single photons. Phys. Rev. Lett. 90, 250401 (2003).  
25. Greenberger, D. M. & Yasin, A. Simultaneous wave and particle knowledge in a neutron interferometer. Phys. Lett. A 128, 391-394 (1988).  
26. Jaeger, G., Shimony, A. & Vaidman, L. Two interferometric complementarities. Phys. Rev. A 51, 54-67 (1995).  
27. Englert, B. G. Fringe visibility and which-way information: an inequality. Phys. Rev. Lett. 77, 2154-2157 (1996).

28. Greenstein, G. & Zajonc, A. in The Quantum Challenge: Modern Research on the Foundations of Quantum Mechanics Ch. 2 (Jones & Bartlett, 1997).  
29. Li, C. F., Tang, J. S., Li, Y. L. & Guo, G. C. Experimentally witnessing the initial correlation between an open quantum system and its environment. Phys. Rev. A 83, 064102 (2011).  
30. Chen, G. et al. Convenient exciton lifetime measurement of quantum dots with high resolution. Physica E 42, 196-199 (2009).

# Acknowledgements

The authors thank H.-Q. Ni for sample growth. This work was supported by the National Fundamental Research Program, National Natural Science Foundation of China (grant nos 60921091, 10874162 and 10734060).

# Author contributions

C-F.L. and J-S.T. planned and designed the experiments. J-S.T., Y-L.L. and G-Y.X. implemented the experiments. G-C.G., J-S.T. and X-Y.X. carried out the theoretical analysis and developed the interpretation. C-F.L. and J-S.T. wrote the paper and all authors discussed its contents. C-F.L. supervised the project.

# Additional information

Supplementary information is available in the online version of the paper. Reprints and permission information is available online at http://www.nature.com/reprints. Correspondence and requests for materials should be addressed to C.F.L.

# Competing financial interests

The authors declare no competing financial interests.