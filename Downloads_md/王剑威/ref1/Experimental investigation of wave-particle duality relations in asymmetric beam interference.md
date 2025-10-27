# ARTICLE OPEN

Check for updates

# Experimental investigation of wave-particle duality relations in asymmetric beam interference

Dong-Xu Chen  $1,2$  Yu Zhang  $1,2$  Jun-Long Zhao  $1$  Qi-Cheng Wu  $1$  Yu-Liang Fang  $1$  Chui-Ping Yang  $1,3$  and Franco Nori  $4,5,6$

Wave-particle duality relations are fundamental for quantum physics. Previous experimental studies of duality relations mainly focus on the quadratic relation  $D^2 + V^2 \leq 1$ , based on symmetric beam interference, while a linear form of the duality relation, predicated earlier theoretically, has never been experimentally tested. In addition, the difference between the quadratic form and the linear form has not been explored yet. In this work, with a designed asymmetric beam interference and by utilizing the polarization degree of freedom of the photon as a which-way detector, we experimentally confirm both forms of the duality relations. The results show that more path information is obtained in the quadratic case. Our findings reveal the difference between the two duality relations and have fundamental implications in better understanding these important duality relations.

npj Quantum Information (2022)8:101; https://doi.org/10.1038/s41534-022-00610-7

# INTRODUCTION

Bohr's complementarity principle initially conceptualized the controversial nature of light. It states that a photon possesses two mutually exclusive properties, wave and particle, i.e., the wave-particle duality. It is well known that this duality can be formulated by duality relations, which quantitatively describe the trade-off between wave and particle behaviours, i.e., the emergence of one behaviour will suppress the appearance of the other. In the past years, the duality relations have drawn increasing attention because they are fundamental in quantum physics. Experimental and theoretical interests in duality relations have never vanished since the early days of quantum theory $^{1-14}$ .

The authors in<sup>15</sup> quantified the wave-particle duality in a double-slit interference scenario and concluded that the simultaneous observation of wave and particle behaviours was possible. The complementarity relation  $P^2 + V_0^2 \leq 1$ , where  $P$  is the predictability of the photon passing through the two paths and  $V_0$  is the a priori interference visibility, was derived in<sup>16</sup> and<sup>17</sup>. Also, ref.<sup>17</sup> considered the case in which a which-way detector (WWD) was involved, and obtained the inequality

$$
D _ {\mathrm {m}} ^ {2} + V ^ {2} \leq 1, \tag {1}
$$

where  $P$  was replaced by the distinguishability  $D_{\mathrm{m}}$ , and  $V_{0}$  was replaced by the fringe visibility  $V$  at the output. The predictability  $P$  is different from the distinguishability  $D_{\mathrm{m}}$  in that  $P$  is the difference of the probabilities of the photon taking the two paths, while  $D_{\mathrm{m}}$  is the which-way information stored in the WWD, which depends on the final states of the WWD and the way which we apply to retrieve the information. The distinguishability quantified in<sup>17</sup> is the maximum likelihood for guessing the way right, which coincides with the minimum error discrimination (MED) of the WWD's states.

Applying different strategies to distinguish the WWD's states gives different amounts of which-way information. Another strategy of retrieving which-way information from the WWD is the unambiguous quantum state discrimination (UQSD), which

has been applied to study the wave-particle duality relation in recent years $^{18-23}$ . Reference $^{18}$  quantified the distinguishability by the upper bound of the probability of an unambiguous result and obtained the linear duality relation

$$
D _ {u} + V = 1, \tag {2}
$$

where  $D_{\mathrm{u}}$  is the distinguishability derived from the UQSD strategy. A similar relation was obtained in multipath interference[21-23].

The quadratic relation (1) based on the MED strategy has been experimentally confirmed using various systems $^{6,24-31}$ . However, the linear relation in Eq. (2), which is based on the UQSD strategy, has not been experimentally tested so far. Existing studies on the duality relation mostly focus on the case of symmetric beam interference, where the photon is equally likely to go through both paths. Nevertheless, the asymmetric case, where the beam splitters (BSs) are not balanced or the photon suffers from loss on the BSs, has not been investigated as much as the symmetric case. Over the past years, several theoretical analyses of asymmetric interference with a WWD have been presented $^{18,32-35}$ .

In this work, we experimentally realize asymmetric beam interference with a WWD to study the wave-particle duality. The WWD is implemented by utilizing the polarization degree of freedom of the photon. The visibility  $V$  is characterized by the fringe emerging after the interferometer. We quantify the distinguishability in two ways. One corresponds to the probability of obtaining an unambiguous result, i.e., by adopting the UQSD strategy to discriminate the WWD's states; while the other corresponds to the maximum likelihood for guessing the right path, i.e., by adopting the MED strategy to discriminate the WWD's states.

In our experiment, both quadratic and linear forms of the duality relation, described by Eqs. (1) and (2), are confirmed with different degrees of asymmetry of the beam interference and different degrees of nonorthogonality of the WWD's states. We show that the amounts of which-way information, gained through the two strategies, are different. Our experiment demonstrates the

linear duality relation and also investigates the difference between the two duality relations.

# RESULTS

# Theory

In quantum physics, quantum states, which are orthogonal to each other, can be discriminated via a single measurement. While for nonorthogonal quantum states, one is unable to discriminate them within a single measurement. To retrieve information from nonorthogonal quantum states, different strategies are applied with different objectives. The  $\mathsf{UQSD}^{36-40}$  and the MED $^{41,42}$  are the two most investigated strategies.

Assume that one is told to discriminate two nonorthogonal states  $|d_1\rangle = |h\rangle$  and  $|d_2\rangle = \sin 2\theta |h\rangle -\cos 2\theta |v\rangle$  of a photon, with a priori probabilities  $p_1$  and  $p_2$ , respectively. Here, the state  $|h\rangle (|v\rangle)$  denotes the horizontal (vertical) polarization state, and the probabilities satisfy  $p_1 + p_2 = 1$ . Without loss of generality, we assume  $p_2\leq p_1$ . The UQSD and the MED follow different procedures as follows.

In UQSD, an unambiguous result is possible by allowing an inconclusive result. The polarization degree of freedom of the photon is coupled with another degree of freedom to form a higher dimensional space. Then  $|d_1\rangle$  and  $|d_2\rangle$  are projected onto the orthogonal basis

$$
\left| d _ {1} \right\rangle = \alpha \left| q _ {1} \right\rangle + \beta \left| q _ {2} \right\rangle , \left| d _ {2} \right\rangle = \gamma \left| q _ {3} \right\rangle + \delta \left| q _ {2} \right\rangle , \tag {3}
$$

where  $|\langle q_i|q_j\rangle | = \delta_{ij}, |q_1\rangle$  and  $|q_{3}\rangle$  correspond to unambiguous results,  $|q_{2}\rangle$  corresponds to an inconclusive result. The geometric representation of the principle of UQSD is shown in Fig. 1a. The probability of obtaining an unambiguous result is  $D_{\mathrm{u}} = p_{1}|a|^{2} + p_{2}|\gamma |^{2}$ , and it is given by<sup>43</sup>

$$
D _ {u} = 1 - 2 \sqrt {p _ {1} p _ {2}} \sin 2 \theta , p _ {2} / p _ {1} > \sin^ {2} 2 \theta , \tag {4}
$$

$$
D _ {u} = p _ {1} \left(1 - \sin^ {2} 2 \theta\right), p _ {2} / p _ {1} \leq \sin^ {2} 2 \theta . \tag {5}
$$

![](images/578665881b989ce8fffb7f6970e7f8f111c4da723a5391c66d843114fa92365a.jpg)

![](images/bfa5abfbacf5b84e081e00946b0dc99e43b9243235457c51f424c63cae80721d.jpg)  
Fig. 1 Geometric representation of the principles of nonorthogonal state discrimination. Principles of (a) unambiguous quantum state discrimination (UQSD) and (b) minimum error discrimination (MED) strategies. The moduli of the vectors represent the square roots of the a priori probabilities of the states. In UQSD, the states  $|d_1\rangle$  and  $|d_2\rangle$  are first rotated, then the horizontal component is separated into two parts, one is the common state  $|q_2\rangle$  corresponding to an inconclusive result. The residuals,  $|q_1\rangle$  and  $|q_3\rangle$ , are orthogonal, which can be discriminated by a positive operator-valued measure. In MED, the states  $|d_1\rangle$  and  $|d_2\rangle$  are rotated, then a positive operator-valued measure is performed to project the states onto the basis states  $|h\rangle$  and  $|v\rangle$ . When we detect the photon in the  $|h\rangle$  state, we guess the state is  $|d_2\rangle$ , otherwise we guess it as  $|d_1\rangle$ . Since the measurement result is probabilistic, there is a probability of guessing wrongly.

On the other hand, in MED, each measurement returns a result, and the quantum state is determined by the best guess. The protocol aims at minimizing the guessing error. The principle of MED is shown in Fig. 1b. The maximum probability of correctly guessing the quantum state is given by the Helstrom bound<sup>44</sup>

$$
P _ {\mathrm {r}} = \frac {1}{2} \left(1 + \sqrt {1 - 4 p _ {1} p _ {2} \sin^ {2} 2 \theta}\right). \tag {6}
$$

Research on the wave-particle duality is generally based on two scenarios, the double-slit interference and the standard Mach-Zehnder interferometer (MZI) (see Fig. 2). In the double-slit interference, the light passes through two separated slits, behind which a screen is placed. One can observe fringes on the screen, which are not simply the sum of the light passing through an individual slit when the other is blocked. In the standard MZI, the input light is separated by a symmetric beam splitter (BS), then the light travelling along the two arms interferes on the second BS. Changing the phase of the light in one arm gives rise to a change of the intensity of the output light. When the second BS is removed, the phase change will not induce the change of the output intensity. In this case, we declare that the photons reveal particle behaviour in an open interferometer. The double-slit interference is more often employed to intuitively show the interference of photons, while the standard MZI is more suitable in practical experiments. In studies of wave-particle duality, these two scenarios are equivalent.

The scenario we consider is an MZI with a WWD inserted in the interferometer (Fig. 2b). The first BS is unbalanced, such that it causes the photon to propagate along two paths with unequal probabilities,  $p_1$  and  $p_2$ . The WWD is a quantum detector, which interacts with the photon and then gets correlated with the photon's path.

Assume now that the initial state of the WWD is  $|d_0\rangle$ , and the state of the photon after passing through the unbalanced BS is  $\sqrt{p_1} |0\rangle +\sqrt{p_2} |1\rangle$ , where  $|0\rangle$  and  $|1\rangle$  denote the two path states. The interaction between the WWD and the photon leads to a

![](images/8c26115d2102bb818b933460bf91ae15f840d78b5ff41d5f6b07cc1b6dc72e04.jpg)  
Fig. 2 Scenarios for studying wave-particle duality. a Double-slit interference setup includes a double-slit and a screen for observing the fringes. b A Mach-Zehnder interferometer consists of two beam splitters. WWD which-way detector.

![](images/1e5b220b8c364a99fc1286bfee7e773c4306a50a85ed7d705fc9ea4924cfd643.jpg)  
Fig. 3 Schematic of the experiment. (1): asymmetric interference. The photon transmits through the first PBS and is then rotated by the first half-wave plate H1. The blue half of the cBS works as a PBS to split different polarization components. The photon traverses the two paths in the Sagnac-like structure and recombines on the black half of the cBS. H2 and H3 determine the final states of the WWD. PP introduces a phase between the two paths. (2): polarization measurement. The polarization of the photon is analysed in the Sagnac-like structure. See Methods for the details of the implementation. The inset shows that the cBS is equivalent to an assembly of a PBS and a NPBS. When the photon is incident on the blue region, it works as a PBS; while when the photon is incident on the black region, it works as a NPBS. PBS polarization beam splitter, NPBS non-polarizing beam splitter, PP phase plate, cBS cubic beam splitter, M mirror, H1~H7 half-wave plates, Dv, D0, D1, and D2 single-photon detectors.

controlled-unitary transformation

$$
\left.\left(\sqrt {p _ {1}} | 0 \rangle + \sqrt {p _ {2}} | 1 \rangle\right) | d _ {0} \rangle \rightarrow \sqrt {p _ {1}} | 0 \rangle | d _ {1} \rangle + \sqrt {p _ {2}} | 1 \rangle | d _ {2} \rangle . \right. \tag {7}
$$

To distinguish the paths of the photon is equivalent to distinguish the final states of the WWD. Note that  $|d_1\rangle$  and  $|d_2\rangle$  are not necessarily orthogonal. When  $|\langle d_1|d_2\rangle | = 1$ , which means  $|d_1\rangle$  and  $|d_2\rangle$  are identical, no path information can be retrieved from the WWD. When  $|\langle d_1|d_2\rangle | = 0$ ,  $|d_1\rangle$  and  $|d_2\rangle$  can be perfectly distinguished. In the intermediate case, i.e.,  $|\langle d_1|d_2\rangle | = \sin 2\theta$ , one can only obtain a partial which-way information by means of nonorthogonal quantum state discrimination.

We utilize the photon's polarization degree of freedom as the WWD. Let the initial state of the WWD be  $|h\rangle$ . The polarization of the photon in path 1 is rotated due to the interaction between the WWD and the photon. The quantum state after the interaction becomes  $\sqrt{p_1} |0,h\rangle +\sqrt{p_2} |1,s\rangle$ , where  $|s\rangle = \sin 2\theta |h\rangle -\cos 2\theta |v\rangle$ . After the second balanced BS, the probability of detecting the photon at path 0 is  $p = (1 + 2\sqrt{p_1p_2}\sin 2\theta \cos \varphi) / 2$ . Here  $\varphi$  is the phase between the two paths. Thus the visibility is given by

$$
V = \frac {p _ {\max} - p _ {\min}}{p _ {\max} + p _ {\min}} = 2 \sqrt {p _ {1} p _ {2}} \sin 2 \theta . \tag {8}
$$

To retrieve the which-way information, one could perform the UQSD strategy on the polarization of the photon. The maximum probability of unambiguously discriminating the polarization states is given by Eqs. (4) and (5). We now have

$$
D _ {u} + V = 1, p _ {2} / p _ {1} > \sin^ {2} 2 \theta , \tag {9}
$$

$$
D _ {u} + V = p _ {1} \cos^ {2} 2 \theta + 2 \sqrt {p _ {1} p _ {2}} \sin 2 \theta , p _ {2} / p _ {1} \leq \sin^ {2} 2 \theta . \tag {10}
$$

Equations (9) and (10) coincide with the results in ref. 18 which considers a double-slit scenario.

On the other hand, the which-way information can also be retrieved by the MED strategy. The probability of the correct guess is given by Eq. (6). Thus the distinguishability becomes  $D_{\mathrm{m}} = 2P_{\mathrm{r}} - 1$ . Using Eq. (8), we recover

$$
D _ {\mathrm {m}} ^ {2} + V ^ {2} = 1. \tag {11}
$$

Since we consider a pure state as the input, the duality relation is an equality. If we consider a more general case (e.g., the input being a mixed state), it would be an inequality. In recent years, constraints of the entanglement on the duality relation Eq. (11) have been fruitfully discussed in both classical and quantum domains[45-51]. In particular, ref.[52] demonstrated the constraints of the purity of the photon source on the duality relation Eq. (11) from a source point of view[53] by adjusting the amplitudes of the seed laser, where the photon source was generated through an entangled nonlinear bi-photon source model.

# Experimental setup

To implement the forementioned asymmetric beam interference, our experimental setup consists of two Sagnac-like structures. The first Sagnace loop realizes the asymmetric beam interference, while the second one realizes the polarization measurement, as is shown in Fig. 3. The photon source is a single photon generated through a nonlinear process (See Methods for details). The polarization of the photon is prepared to be horizontal by the first polarization beam splitter (PBS). A half-wave plate (H1)

and a cubic beam splitter (CBS) work as a variable beam splitter. The cBS, which is part of the Sagnac-like structure, is customized such that the coating inside the crystal consists of two parts, a blue part and a black part. It functions as a PBS when the photon is incident on the blue half of the crystal, while it functions as a non-polarizing beam splitter when the photon is incident on the black half. The cBS is functionally equivalent to an assembly of a PBS and a non-polarizing beam splitter, as is shown in the inset. Such a compact structure enables relative stability of the Sagnac-like structure. Therefore, when H1 is oriented at  $\theta_{\mathrm{a}}$  and the photon is incident on the blue half of the cBS, the photon travels along path 0 or path 1, depending on the polarization, with probabilities  $p_1 = \cos^2 2\theta_{\mathrm{a}}$  and  $p_2 = \sin^2 2\theta_{\mathrm{a}}$ , respectively. The photon in path 0 is vertically polarized while the photon in path 1 is horizontally polarized. The split ratio  $p_2 / p_1 = \tan^2 2\theta_{\mathrm{a}}$  determines the asymmetry of the interference. At this step, since the polarization correlates with the path, the polarization is regarded as the WWD.

Inside the first Sagnac loop, a half-wave plate H2 oriented at  $\theta_{\mathrm{n}}$  is inserted in path 1 to set the nonorthogonality of the final states of the WWD. To maintain the coherent superposition of the two paths, another half-wave plate (H3) oriented at  $0^{\circ}$  is inserted in path 0 to compensate the optical path. The photon from the two paths interferes on the black half of the cBS. The output states, which correspond to the two exits of the cBS, are given by

$$
\left| \psi_ {\mathrm {v}} \right\rangle = \frac {1}{\sqrt {2}} \left(\cos 2 \theta_ {\mathrm {a}} \left| d _ {1} \right\rangle - e ^ {i \varphi} \sin 2 \theta_ {\mathrm {a}} \left| \bar {d} _ {2} \right\rangle\right), \tag {12}
$$

$$
\left| \psi_ {\mathrm {d}} \right\rangle = \frac {1}{\sqrt {2}} \left(\cos 2 \theta_ {\mathrm {a}} \left| d _ {1} \right\rangle + e ^ {i \varphi} \sin 2 \theta_ {\mathrm {a}} \left| d _ {2} \right\rangle\right), \tag {13}
$$

where  $|d_1\rangle = |h\rangle$  and  $|d_2\rangle = \sin 2\theta_{\mathrm{n}}|h\rangle -\cos 2\theta_{\mathrm{n}}|\nu \rangle$  are the final states of the WWD, whose nonorthogonality is determined by  $|\langle d_1|d_2\rangle | = \sin 2\theta_{\mathrm{n}};$  and  $|\overline{d}_2\rangle = \sin 2\theta_{\mathrm{n}}|h\rangle +\cos 2\theta_{\mathrm{n}}|\nu \rangle$ . The state  $|\psi_{\mathrm{v}}\rangle$  is detected immediately by  $D_{\mathrm{v}}$  for measurement of the visibility

$$
V = \frac {\operatorname* {m a x} (N) - \operatorname* {m i n} (N)}{\operatorname* {m a x} (N) + \operatorname* {m i n} (N)}, \tag {14}
$$

where  $N$  is the photon count at  $\mathsf{D}_{\mathrm{v}}$ ,  $\max(\cdot)$  and  $\min(\cdot)$  are the extreme values with respect to  $\varphi$ , which is the phase introduced by the phase plate in path 1. Afterwards, the photon in the state  $|\psi_{\mathrm{d}}\rangle$  enters the second Sagnac-like structure for the distinguishability measurement. The which-way information of the photon implies the path along which the photon travels in the first Sagnac loop.

# Experimental linear and quadratic duality relations

We now perform a nonorthogonal state discrimination on the states  $|d_1\rangle$  and  $|d_2\rangle$  to measure the distinguishability. We first quantify the distinguishability as the probability of an error-free result, i.e., by adopting the UQSD strategy. The procedure is analogous to discriminating two nonorthogonal states with equal a priori probabilities apart from additional basis rotations[54]. The half-wave plates H4~H7 are properly rotated to realize the basis transformation (See Methods for details). Here, a click at  $D_2$  corresponds to an inconclusive result, indicating that the photon may come from path 0 or path 1. A click at  $D_1$  indicates that the photon deterministically comes from path 1, and a click at  $D_0$  indicates the photon deterministically comes from path 0. In this setup, the photon count of path 0 is  $N_{20} + N_{00}$ , and the photon count of path 1 is  $N_{21} + N_{11}$ , where  $N_{ij}$  is the photon count at  $D_i$  when path  $j$  is open in the first Sagnac loop. The photon count, corresponding to an unambiguous result, is  $N_{11} + N_{00}$ . The distinguishability  $D_u$  is quantified by the

probability of getting an unambiguous result

$$
D _ {u} = \frac {N _ {0 0} + N _ {1 1}}{\left(N _ {2 0} + N _ {0 0}\right) + \left(N _ {2 1} + N _ {1 1}\right)}. \tag {15}
$$

Figure 4 shows the photon counts at  $D_0$ ,  $D_1$ , and  $D_2$  with respect to  $\varphi$  when (a)  $\tan 2\theta_{\mathrm{a}} = 0.38$ ,  $\sin 2\theta_{\mathrm{n}} = 0.2$  and (b)  $\tan 2\theta_{\mathrm{a}} = 0.28$ ,  $\sin 2\theta_{\mathrm{n}} = 0.9$ . The sinusoidal change of the photon count at  $D_2$  is due to the interference between the common parts of  $|d_1\rangle$  and  $|d_2\rangle$ . In Fig. 4a, when  $\tan 2\theta_{\mathrm{a}} > \sin 2\theta_{\mathrm{n}}$ , the minimum photon count at  $D_2$  is zero. This implies that the common part is equally likely to come from  $|d_1\rangle$  or  $|d_2\rangle$  (equal lengths of the common parts in Fig. 1a). While in Fig. 4b, when  $\tan 2\theta_{\mathrm{a}} \leq \sin 2\theta_{\mathrm{n}}$ , the minimum photon count at  $D_2$  is zero since the photon in the common part is more likely to come from path 0; in other words, some which-way information is stored in the common part.

Next we perform the MED strategy to extract the which-way information. As illustrated in Fig. 1b, to realize the MED strategy, the H4 first rotates the polarization suitably. The H5 and the H7 are constantly kept at  $0^{\circ}$  (see Methods for details). Under such configuration,  $|d_1\rangle$  and  $|d_2\rangle$  are first rotated and then projected onto the  $|h\rangle$  and  $|v\rangle$  basis. The horizontal component is detected by  $\mathsf{D}_2$  and the vertical component is detected by  $\mathsf{D}_0$ . When  $\mathsf{D}_2$  clicks, we guess the photon comes from path 0; while when  $\mathsf{D}_0$  clicks, we guess the photon comes from path 1. Thus, a right guess, with photon count of  $N_{01} + N_{20}$ , means either  $\mathsf{D}_2$  clicks when the photon comes from path 0, or  $\mathsf{D}_0$  clicks when the photon comes from path 1; while a wrong guess is the opposite, with photon count of  $N_{00} + N_{21}$ . The distinguishability is quantified by the difference between the right guess and the wrong guess

$$
D _ {\mathrm {m}} = \frac {N _ {0 1} + N _ {2 0} - N _ {0 0} - N _ {2 1}}{N _ {0 1} + N _ {2 0} + N _ {0 0} + N _ {2 1}}. \tag {16}
$$

Figure 5 shows our experimental results, where the horizontal label symmetry signifies the symmetry of the interference and it is quantified by  $\tan 2\theta_{\mathrm{a}}$ . We test the two cases when (i) the linear form applies (Fig. 5a), and (ii) the linear form does not apply (Fig. 5b), when using the UQSD strategy. For comparison, we also test the quadratic form by using the MED strategy with the same configurations in Fig. 5c and d, respectively. Note that the applicability of the linear form requires  $\sin 2\theta_{\mathrm{n}} \leq \tan 2\theta_{\mathrm{a}}$ ; therefore, we set  $\sin 2\theta_{\mathrm{n}} = 0.2$  in this case to ensure a relatively wide range in which the value of  $\tan 2\theta_{\mathrm{a}}$  could be set. One can see from Fig. 5a that the experimental summation of  $(V + D_{\mathrm{u}})$  is close to 1 with small deviations.

On the other hand, for the case where the linear relation does not apply, we set  $\sin 2\theta_{\mathrm{n}} = 0.9$  in Fig. 5b, since the inequality

![](images/d81b624891d97d23b39e1daae2623e1c4193706d471e7d56dd4f0ae661175749.jpg)  
Fig. 4 Normalized photon counts at D0, D1, and D2. a tan  $2\theta_{a} = 0.38$ , sin  $2\theta_{n} = 0.2$  and (b) tan  $2\theta_{a} = 0.28$ , sin  $2\theta_{n} = 0.9$ . The photon counts are divided by the total photon count of  $\mathsf{D}_{\mathsf{v}} + \mathsf{D}_{0} + \mathsf{D}_{1} + \mathsf{D}_{2}$ . The dots are the experimental data, while the solid lines are the theoretical values. The error of the photon count at  $\mathsf{D}_{1}$  in (b) is  $\sim \mathcal{O}(10^{-4})$ , thus the error bar is almost invisible in the figure. The error bars indicate one standard deviation.

![](images/28a3860de66a488b98ae5230aca8186a1496a1f3b4a6bb1f92c3c7da43af9f8b.jpg)

![](images/1ab9e785e6405b69cd587d611004742cf6064e233d7170348cbcc38cfd6820b0.jpg)

![](images/2a6289faeddd8b8f55e25d8e50506da3d35a000f503d9f1d90cf5d84190ad920.jpg)  
Fig. 5 Experimental results. Duality relations when the nonorthogonality of the final states of the WWD is  $(\mathbf{a}, \mathbf{c})$  sin  $2\theta_{\mathrm{n}} = 0.2$  and  $(\mathbf{b}, \mathbf{d})$  sin  $2\theta_{\mathrm{n}} = 0.9$ .  $(\mathbf{a}, \mathbf{b})$ : Confirmation of the linear duality relation.  $(\mathbf{c}, \mathbf{d})$  Confirmation of the quadratic duality relation. The experimental visibility in  $(\mathbf{c}, \mathbf{d})$  is the same as that in  $(\mathbf{a}, \mathbf{b})$ , both are calculated through Eq. (14). The label symmetry signifies the symmetry of the interference and it is quantified by  $\tan 2\theta_{\mathrm{a}}$ . The dots are experimental values while the solid lines are theoretical values. The error bars indicate one standard deviation.

![](images/56bf73e9c676958b376edb2ec0cac69fcb92b6de0a6963bb2dd81b4b1d1e4527.jpg)

$\sin 2\theta_{\mathrm{n}} > \tan 2\theta_{\mathrm{a}}$  should be satisfied. One could see that the linear relation is no longer valid in this case, because partial which-way information is stored in the common part when the degree of asymmetry is larger than the degree of nonorthogonality. On the contrary, in Fig. 5(c, d), the quadratic relation always applies. One notices that the  $(V + D_{\mathrm{u}})$  and  $(V^{2} + D_{\mathrm{m}}^{2})$  in Fig. 5 exceed the theoretical maximum at some data points, this is because the visibility and the distinguishability are not measured with the same photons. The visibility is measured through the statistics of photon counts at detector  $D_{\mathrm{v}}$  while varying the phase  $\varphi$ ; whereas the distinguishability is measured through the polarization analysis in the second Sagnac loop. On the other hand, the non-ideal coating of the cBS on the black half (i.e., the part acting as an NPBS) causes errors to the measurements of the visibility and the distinguishability. Therefore, the measured  $(V + D_{\mathrm{u}})$  and  $(V^{2} + D_{\mathrm{m}}^{2})$  may exceed the theoretical maximum.

# Relation between the two forms of the duality relation

The linear duality relation characterized by Eqs. (9) and (10) is tighter than the quadratic duality relation characterized by Eq. (11). This can be seen from the mutual information gained after performing the measurement. The mutual information between Alice (A) and Bob (B) is

$$
H (A: B) = \sum_ {i j} p _ {i} \operatorname {T r} \left(\hat {\rho} _ {i} \hat {\pi} _ {j}\right) \log \left(\frac {\operatorname {T r} \left(\hat {\rho} _ {i} \hat {\pi} _ {j}\right)}{\operatorname {T r} \left(\hat {\rho} \hat {\pi} _ {j}\right)}\right), \tag {17}
$$

where the quantum state  $\hat{\rho}_i$  is prepared by Alice with a priori probability  $p_i$ , and Bob performs a positive operator-valued measure  $\{\hat{\pi}_j\}$  with  $\sum_j \hat{\pi}_j = \mathbb{I}$  and  $\hat{\rho} = \sum_i p_i \hat{\rho}_i$ . The mutual information given by Eq. (17) quantifies how much information is obtained by Bob through the measurement (See Methods). The UQSD strategy is closely related to the maximum confidence strategy for quantum state discrimination<sup>55</sup>, which maximizes the conditional probability  $P(\hat{\rho}_i | i)$ , i.e., the probability that the state is  $\hat{\rho}_i$  when obtaining the result  $i$ . The MED strategy minimizes the guessing error and in some cases it coincides with the maximum mutual information strategy<sup>56,57</sup>. Figure 6 shows the mutual

![](images/d099a40ff0f70574738a6b619a04b293028975330eda59d37c577c755d765ebf.jpg)  
Fig. 6 Mutual information gained via MED and UQSD strategies. The nonorthogonality is (a)  $\sin 2\theta_{\mathrm{n}} = 0.2$  and (b)  $\sin 2\theta_{\mathrm{n}} = 0.9$ . The dots are experimental values, while the solid lines are theoretical values. The error bars indicate one standard deviation.

![](images/a6d94182af047c75208f6fcc0173e48e12b1924f485c8576204494302d40e037.jpg)

information obtained by using USQD and MED strategies. We can see that the mutual information obtained through the MED strategy is more than that obtained through the UQSD strategy. This means that more which-way information is extracted through the MED strategy.

# DISCUSSION

In our work, we measure the visibility by changing the relative phase between the two paths of the first Sagnac loop, while the distinguishability is measured through the polarization measurement in the second Sagnac loop. The visibility and the distinguishability are measured with different photon samples. This, in some sense, implies that they are measured with different setups. While the essence of the duality relations emphasizes the complementarity between the wave behaviour and the particle behaviour of the same photon, we remark that such a method to measure the two quantities has been employed in the study of duality relations $^{29,30}$ . Due to the destruction of the photon at the detector, we are not able to measure the distinguishability and the visibility with the same photon.

We have realized an asymmetric beam interference experiment to study the wave-particle duality by utilizing the polarization degree of freedom of the photon as a which-way detector. In our experiment, both the linear duality relation and the quadratic duality relation have been confirmed. We have shown that the distinguishability in the linear form corresponds to the probability of obtaining an unambiguous result, while the distinguishability in the quadratic duality relation corresponds to the maximum likelihood for the right guess. We have also shown that the difference between the UQSD strategy and the MED strategy can be understood by calculating the mutual information gained through the measurements. Since less mutual information is gained in the UQSD strategy, the linear form is tighter than the quadratic form. Our results reveal the difference between the two duality relations, which will have fundamental implications in better understanding the duality relation quantitatively. Furthermore, since the distinguishability is closely related to the discrimination of the states of the which-way detector, our work might motivate future studies on quantum state discrimination in duality relations and may have other potential applications in quantum information science and technology.

# METHODS

# Details of the experiment

The single-photon source is generated through spontaneous parametric down-conversion process by pumping a type-I phase matched nonlinear  $\beta$ -barium-borate crystal. The pump laser is a CW single frequency laser operating at a center wavelength of  $404~\mathrm{nm}$  with power of  $130~\mathrm{mW}$ . The photon pair with wavelength of  $808~\mathrm{nm}$  is filtered by a pair of interference

filters with a  $3\mathrm{nm}$  bandwidth. The idler photon is detected by a single-photon detector for coincidence counting. The signal photon is thus heralded and delivered to the experimental setup shown in Fig. 3. The averaged photon count is approximately 10,000 per second.

The interference visibility of both Sagnac loops is higher than  $98.67\%$ . The photon counts are measured five times for calculating the deviations, with duration of 0.5 s for each measurement. The error bars in Figs. 4-6 are small because the fluctuation of the photon count is relatively small.

# Settings for performing UQSD and MED strategies

We follow Fig. 1 in the main text to clarify the measurement settings for performing the nonorthogonal quantum state discrimination strategies, UQSD and MED.

(i) UQSD strategy. When  $\tan 2\theta_{\mathrm{a}} > \sin 2\theta_{\mathrm{n}}$ , the H4 rotates the polarization suitably such that the line connecting the endpoints of the state vectors is perpendicular to the horizontal line, thus maximizing the probability of obtaining an unambiguous result. In this way, the states  $|d_1\rangle$  and  $|d_2\rangle$  have the same amount of horizontal component, as shown in Supplementary Fig. 1a. Then H5 separates the horizontal components of both states into two parts. One part corresponds to the common state  $|q_2\rangle$  (an inconclusive result); while the other, when superposed with the vertical components, turns the states  $|d_1\rangle$  and  $|d_2\rangle$  into orthogonal states  $|q_1\rangle$  and  $|q_3\rangle$ . The H6 is fixed at  $45^\circ$ . Finally,  $|q_1\rangle$  and  $|q_3\rangle$  are unambiguously discriminated by a projective measurement consisting of H7 and a PBS. The angles of H4, H5 and H7 are

$$
\theta_ {4} = \frac {1}{2} \arctan \frac {\sin 2 \theta_ {\mathrm {n}} - \cot 2 \theta_ {\mathrm {a}}}{\cos 2 \theta_ {\mathrm {n}}}, \tag {18}
$$

$$
\theta_ {5} = \frac {1}{2} \arccos  \frac {\sqrt {\tan 2 \theta_ {\mathrm {a}} \sin 2 \theta_ {\mathrm {n}}}}{\cos 2 \theta_ {4}}, \tag {19}
$$

$$
\theta_ {7} = \frac {1}{2} \operatorname {a r c c o t} \frac {\sin 2 \theta_ {4}}{\cos 2 \theta_ {4} \sin 2 \theta_ {5}}, \tag {20}
$$

where  $\theta_{\mathrm{a}}$  and  $\theta_{\mathrm{n}}$  are the orientations of H1 and H2, respectively. Here, we omit the reflections on the mirrors. When tan  $2\theta_{\mathrm{a}} < \sin 2\theta_{\mathrm{n}}$ , the H4 transforms  $|d_2\rangle$  to  $|h\rangle$ , as is shown in Supplementary Fig. 1d. The H5~H7 are fixed at  $0^{\circ}$ ,  $45^{\circ}$  and  $0^{\circ}$ , respectively. Both of these states have a horizontal component, thus a detection of the  $|h\rangle$  state (i.e.,  $D_{2}$  clicks) signifies an inconclusive result. While  $D_{0}$  clicks if and only if the state is  $|d_1\rangle$ . The orientation of H4 is

$$
\theta_ {4} = \theta_ {\mathrm {n}} - \frac {\pi}{4}. \tag {21}
$$

(ii) MED strategy. As shown in Supplementary Fig. 1e, to realize the MED strategy, the polarization is suitably rotated by H4, followed by a projective measurement. Note that though a simpler setup is sufficient to realize the MED strategy: we maintain the setup unchanged such that it is the same as the one when performing the UQSD strategy. Thus, the H5 ~ H7 are fixed at  $0^{\circ}$ ,  $45^{\circ}$  and  $0^{\circ}$ , respectively. The orientation of H4 is

$$
\theta_ {4} = \frac {1}{4} \left(\frac {\pi}{2} - \phi\right), \tag {22}
$$

where

$$
\phi = \arctan \frac {\cos^ {2} 2 \theta_ {\mathrm {a}} + \sin^ {2} 2 \theta_ {\mathrm {a}} \cos 4 \theta_ {\mathrm {n}}}{\sin^ {2} 2 \theta_ {\mathrm {a}} \sin 4 \theta_ {\mathrm {n}}}. \tag {23}
$$

# Evaluation of the mutual information

We evaluate the mutual information obtained through the polarization measurement for two nonorthogonal states  $|d_1\rangle = |h\rangle$  and  $|d_2\rangle = \sin 2\theta_{\mathrm{n}}|h\rangle -\cos 2\theta_{\mathrm{n}}|v\rangle$ , with a priori probabilities  $p_1 = \cos^2 2\theta_{\mathrm{a}}$  and  $p_2 = \sin^2 2\theta_{\mathrm{a}}$ , respectively. For UQSD, the states  $|d_1\rangle$  and  $|d_2\rangle$  are projected onto a three-dimensional space spanned by the basis states  $\{|q_1\rangle ,|q_2\rangle ,|q_3\rangle \}$ , with the projective operators  $\tilde{\pi}_1 = |q_1\rangle \langle q_1|, \tilde{\pi}_2 = |q_2\rangle \langle q_2|$  and  $\tilde{\pi}_3 = |q_3\rangle \langle q_3|$ . The basis states have the following forms

$$
\left| q _ {1} \right\rangle = R _ {\mathrm {H} 4} ^ {\dagger} \left(\hat {P} _ {v} \hat {\sigma} _ {1} \hat {P} _ {h} + \hat {P} _ {h} R _ {\mathrm {H} 5} ^ {\dagger} \hat {P} _ {v}\right) R _ {\mathrm {H} 7} ^ {\dagger} | h \rangle_ {r}, \tag {24}
$$

$$
\left| q _ {2} \right\rangle = R _ {\mathrm {H} 4} ^ {\dagger} \hat {P} _ {h} R _ {\mathrm {H} 5} ^ {\dagger} | h \rangle_ {I}, \tag {25}
$$

$$
\left| q _ {3} \right\rangle = R _ {\mathrm {H} 4} ^ {\dagger} \left(\hat {P} _ {v} \hat {\sigma} _ {1} \hat {P} _ {h} + \hat {P} _ {h} R _ {\mathrm {H} 5} ^ {\dagger} \hat {P} _ {v}\right) R _ {\mathrm {H} 7} ^ {\dagger} | V \rangle_ {r}, \tag {26}
$$

where  $\hat{\sigma}_{1}$  is the Pauli operator,  $\hat{P}_{h(v)}$  projects the state onto  $|h(v)\rangle$ , and  $R_{(\bullet)}^{\dagger}$  is the Hermitian conjugate of the Jones matrix of the half-wave plate. The subscripts  $l$  and  $r$  indicate different paths in the three-dimensional space, because the path degree of freedom of the photon is coupled with the polarization degree of freedom to form a higher space. The eigenvalue of  $\hat{n}_2$  corresponds to an inconclusive result, while the eigenvalues of  $\hat{n}_1$  and  $\hat{n}_3$  correspond to unambiguous results that the photon comes from path 0 and path 1, respectively.

While for MED, the projective operators are

$$
\hat {\pi} _ {1} = R _ {\mathrm {H} 4} ^ {\dagger} | h \rangle \langle h | R _ {\mathrm {H} 4}, \tag {27}
$$

$$
\hat {\pi} _ {2} = R _ {\mathrm {H} 4} ^ {\dagger} | v \rangle \langle v | R _ {\mathrm {H} 4}, \tag {28}
$$

which means that the states are projected onto the basis states  $|h\rangle$  and  $|v\rangle$  after transformed by H4.

# DATA AVAILABILITY

All relevant data are available from the corresponding authors upon reasonable request.

# CODE AVAILABILITY

All relevant codes are available from the corresponding authors upon reasonable request.

Received: 4 May 2022; Accepted: 2 August 2022

Published online: 02 September 2022

# REFERENCES

1. Berthold-Georg, E., Marlan, O. S. & Walther, H. The Duality in Matter and Light. Sci. Am. 271, 86-92 (1994).  
2. Berthold-Georg, E., Marlan, O. S. & Walther, H. Complementarity and uncertainty. Nature 375, 367-368 (1995).  
3. Zou, X. Y., Wang, L. J. & Mandel, L. Induced coherence and indistinguishability in optical interference. Phys. Rev. Lett. 67, 318-321 (1991).  
4. Wang, L. J., Zou, X. Y. & Mandel, L. Induced coherence without induced emission. Phys. Rev. A 44, 4614-4622 (1991).  
5. Agarwal, G. S. & Tara, K. Nonclassical properties of states generated by the excitations on a coherent state. Phys. Rev. A 43, 492-497 (1991).  
6. Yoon-Ho, K., Yu, R., Kulik. S. P., Shih, Y. & Marlan, O.S. Delayed "Choice" quantum eraser. Phys. Rev. Lett. 84, 1-5 (2000).  
7. Marlan, O. S. & Walther, H. Quantum optical test of observation and complementarity in quantum mechanics. Phys. Rev. A 39, 5229-5236 (1989).  
8. Marlan, O. S., Berthold-Georg, E. & Walther, H. Quantum optical tests of complementarity. Nature 351, 111-116 (1991).  
9. Berthold-Georg, E., Walther, H. & Scully, M. Quantum optical Ramsey fringes and complementarity. Appl. Phys. B 54, 366-368 (1992).  
10. Scully, M. O. & Zubairy, M. S. Quantum Optics. https://doi.org/10.1017/CBO9780511813993 (Cambridge University Press, 1997).  
11. Agarwal, G. S. Quantum Optics. https://doi.org/10.1017/CBO9781139035170 (Cambridge University Press, 2012).  
12. Berthold-Georg, E., Marlan, O. S. & Walther, H. On mechanisms that enforce complementarity. J. Mod. Opt. 47, 2213-2220 (2000).  
13. Schleich, W. P. Wave-particle dualism in action, in Optics in Our Time, edited by M. D. Al-Amri, M. El-Gomati, and M. S. Zubairy. https://doi.org/10.1007/978-3-319-31903-2_19 (Springer International Publishing, Cham, 2016) pp. 483-504.  
14. Qin, W., Miranowicz, A., Long, G., You, J. & Nori, F. Proposal to test quantum wave-particle superposition on massive mechanical resonators. npj Quantum Inf. 5, 1 (2019).  
15. William, K. W. & Wojciech, H. Z. Complementarity in the double-slit experiment: Quantum nonseparability and a quantitative statement of Bohr's principle. Phys. Rev. D. 19, 473-484 (1979).  
16. Jaeger, G., Shimony, A. & Vaidman, L. Two interferometric complementarities. Phys. Rev. A 51, 54-67 (1995).  
17. Berthold-Georg, E. Fringe visibility and which-way information: An inequality. Phys. Rev. Lett. 77, 2154-2157 (1996).  
18. Keerthy, K. M. & Qureshi, T. Wave-particle duality in asymmetric beam interference. Phys. Rev. A 98, 022130 (2018).  
19. Yink, L. L., Dai, J., Berthold-Georg, E. & Leonid, A. K. Unambiguous path discrimination in a two-path interferometer. Phys. Rev. A 98, 022110 (2018).

20. Amico, M. & Dittel, C. Simulation of wave-particle duality in multipath interferometers on a quantum computer. Phys. Rev. A 102, 032605 (2020).  
21. Manabendra, N. B., Qureshi, T., Mohd, A. S. & Arun, K. P. Duality of quantum coherence and path distinguishability. Phys. Rev. A 92, 012118 (2015).  
22. Qureshi, T. Interference visibility and wave-particle duality in multipath interference. Phys. Rev. A 100, 042105 (2019).  
23. Mohd, A. S. & Qureshi, T. Multipath wave-particle duality with a path detector in a quantum superposition. Phys. Rev. A 103, 022219 (2021).  
24. Hellmuth, T., Walther, H., Zajonc, A. & Schleich, W. Delayed-choice experiments in quantum interference. Phys. Rev. A 35, 2532-2541 (1987).  
25. Baldzuhn, J., Mohler, E. & Martienssen, W. A wave-particle delayed-choice experiment with a single-photon state. Z. Phys. 77, 347-352 (1989).  
26. B. J., Lawson-Daku et al. Delayed choices in atom stern-gerlach interferometry. Phys. Rev. A 54, 5042-5047 (1996).  
27. Jacques, V. et al. Experimental realization of Wheeler's delayed-choice gedanken experiment. Science 315, 966-968 (2007).  
28. Jacques, V. et al. Delayed-choice test of quantum complementarity with interfering single photons. Phys. Rev. Lett. 100, 220402 (2008).  
29. Kaiser, F., Coudreau, T., Milman, P., Daniel, B. O. & Tanzilli, S. Entanglement-enabled delayed-choice experiment. Science 338, 637-640 (2012).  
30. John, S. T. et al. Realization of quantum Wheeler's delayed-choice experiment. Nat. Photon. 6, 600-604 (2012).  
31. Manning, A. G., Khakimov, R. I., Dall, R. G. & Truscott, A. G. Wheeler's delayed-choice gedanken experiment with a single atom. Nat. Phys. 11, 539-542 (2015).  
32. Li, L., Liu, N. L. & Yu, S. Duality relations in a two-path interferometer with an asymmetric beam splitter. Phys. Rev. A 85, 054101 (2012).  
33. Jia, A. J., Huang, J.-H., Zhang, T.-C., & Zhu, S.-Y. Influence of losses on the wave-particle duality. Phys. Rev. A 89, 042103 (2014).  
34. Liu, Y., Lu, J. & Zhou, L. Complementarity via error-free measurement in a two-path interferometer. *Laser Phys. Lett.* 14, 055204 (2017).  
35. Liu, Y., Lu, J., Peng, Z., Zhou, L. & Zheng, D. Fringe visibility and distinguishability in two-path interferometer with an asymmetric beam splitter. Chin. Phys. B 28, 030303 (2019).  
36. Ivanovic, I. D. How to differentiate between non-orthogonal states. Phys. Lett. A 123, 257-259 (1987).  
37. Peres, A. How to differentiate between non-orthogonal states. Phys. Lett. A 128, 19 (1988).  
38. Dieks, D. Overlap and distinguishability of quantum states. Phys. Lett. A 126, 303-306 (1988).  
39. Mohseni, M., A. M., S. & J. A., B. Optical realization of optimal unambiguous discrimination for pure and mixed quantum states. Phys. Rev. Lett. 93, 200403 (2004).  
40. Agnew, M., Bolduc, E., K. J., R., Franke-Arnold, S. & Leach, J. Discriminating single-photon states unambiguously in high dimensions. Phys. Rev. Lett. 113, 020501 (2014).  
41. Waldherr, G. et al. Distinguishing between nonorthogonal quantum states of a single nuclear spin. Phys. Rev. Lett. 109, 180501 (2012).  
42. Solis-Prosser, M. A.Fernandes, M. F., Jimenez, O., Delgado, A. & Neves, L. Experimental minimum-error quantum-state discrimination in high dimensions. Phys. Rev. Lett. 118, 100501 (2017).  
43. Jaeger, G. & Shimony, A. Optimal distinction between two non-orthogonal quantum states. Phys. Lett. A 197, 83-87 (1995).  
44. Helstrom, C. W. Quantum detection and estimation theory, Vol. 84. https://doi.org/10.1007/BF01007479 (Academic Press, New York, 1976).  
45. Qian, X.F., Malhotra, T., Vamivakas. A. N. & Eberly, J. H. Coherence Constraints and the Last Hidden Optical Coherence. Phys. Rev. Lett. 117, 153901 (2016).  
46. Qian, X. F., Vamivakas, A. & Eberly, J. Entanglement limits duality and vice versa. Optica 5, 942-947 (2018).  
47. De Zela, F. Hidden coherences and two-state systems. Optica 5, 243-250 (2018).  
48. De Zela, F. Generalizing Wave-Particle Duality: Two-Qubit Extension of the Polarization Coherence Theorem. Quantum Rep. 2, 501-513 (2020).  
49. Norrman, A., Ari, T. F. & Leuchs, G. Vector-light quantum complementarity and the degree of polarization. Optica 7, 93-97 (2020).  
50. Qian, X. F. et al. Turning off quantum duality. Phys. Rev. Res. 2, 012016(R) (2020).  
51. Schwaller, N., M.-A., D. & Javerzac-Galy, C. Evidence of the entanglement constraint on wave-particle duality using the IBM Q quantum computer. Phys. Rev. A 103, 022409 (2021).  
52. Yoon, T. H. & Cho, M. Quantitative complementarity of wave-particle duality. Sci. Adv. 7, eabi9268 (2021).

53. Qian, X. F. & Agarwal, G. S. Quantum duality: A source point of view. Phys. Rev. Res. 2, 012031(R) (2020).  
54. Roger, B. M. C., Chefles, A., Stephen, M. B. & Riis, E. Experimental demonstration of optimal unambiguous state discrimination. Phys. Rev. A 63, 040305(R) (2001).  
55. Peter, J. M., Croke, S., Ian, A. W. & Stephen, M. B. Experimental realization of maximum confidence quantum state discrimination for the extraction of quantum information. Phys. Rev. Lett. 97, 193601 (2006).  
56. Levitin, L. B. Optimal quantum measurements for two pure and mixed states, in Quantum Communications and Measurement. 439-448. https://doi.org/10.1007/978-1-4899-1391-3_43 (Springer, 1995).  
57. Barnett, S. M. & Croke, S. Quantum state discrimination. Adv. Opt. Photonics 1, 238-278 (2009).

# ACKNOWLEDGEMENTS

This work is partly supported by the National Natural Science Foundation of China (NSFC) (Grants Nos. 11774076, 11804228, U21A20436), Jiangxi Natural Science Foundation (Grant Nos. 20192ACBL20051, 20212BAB211018). F.N. is supported in part by: Nippon Telegraph and Telephone Corporation (NTT) Research, the Japan Science and Technology Agency (JST) [via the Quantum Leap Flagship Program (Q-LEAP), and the Moonshot R&D Grant Number JPMJMS2061], the Japan Society for the Promotion of Science (JSPS) [via the Grants-in-Aid for Scientific Research (KAKENHI) Grant No. JP20H00134], the Army Research Office (ARO) (Grant No. W911NF-18-1-0358), the Asian Office of Aerospace Research and Development (AOARD) (via Grant No. FA2386-20-1-4069), and the Foundational Questions Institute Fund (FQXi) via Grant No. FQXi-IAF19-06.

# AUTHOR CONTRIBUTIONS

D.X.C. and Y.Z. conceived the project. D.X.C. performed the experiment with the help from Y.Z. and J.L.Z. All authors contributed to the numerical results and the writing of the paper. C.P.Y. and F.N. supervised the project.

# COMPETING INTERESTS

The authors declare no competing interests

# ADDITIONAL INFORMATION

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41534-022-00610-7.

Correspondence and requests for materials should be addressed to Dong-Xu Chen, Chui-Ping Yang or Franco Nori.

Reprints and permission information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/39dc6530c6025e1a312592c1e5c9b6a8ea12fabb8037e1f2f9885069df575ce4.jpg)

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing,

adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2022