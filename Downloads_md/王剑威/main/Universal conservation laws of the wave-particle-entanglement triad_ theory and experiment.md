# ARTICLE

# Open Access

# Universal conservation laws of the wave-particle-entanglement triad: theory and experiment

Ziheng Ding<sup>1</sup>, Yaohao Deng<sup>2,3</sup>, Shao-Ming Fei<sup>4,5</sup>, Si-Qi Zhou<sup>1</sup>, Xiaojiong Chen<sup>2</sup>, Ziwen Rui<sup>6</sup>, Zhihao Ma<sup>1,7,8*</sup>, Yunlong Xiao<sup>9,10*</sup> and Jianwei Wang<sup>2*</sup>

# Abstract

When observed, a quantum system exhibits either wave-like or particle-like properties, depending on how it is measured. However, this duality is affected by the entanglement of the system with its quantum memory, raising a fundamental question: how are wave-particle duality and entanglement related? Here, we broaden the scope of wave-particle duality to include entanglement, introduce universal conservation laws for the wave-particle-entanglement triad, and perform demonstrations on silicon-integrated nanophotonic quantum chips. Our experiments not only mark the first confirmation of universal conservation laws but also highlight the potential of integrated photonics for exploring complex quantum phenomena in high-dimensional systems.

# Introduction

The nature of light has been a subject of debate for centuries, with conflicting views emerging in the late 17th century. Newton argued for a particle nature, whereas Huygens advocated for a wave-centric perspective. Experimental evidence, notably from Young's double-slit interferometer and Einstein's photoelectric effect, revealed the dualistic nature of light. In a broader sense, extending beyond photons, all particles exhibit wave properties. The more we know about the wave-like properties of a particle, the less we know about its particle-like properties, and vice versa. This is the essence of wave-particle duality<sup>1-7</sup>, which has been observed across diverse matter, such as photons<sup>8</sup>, neutrons<sup>9</sup>, atoms<sup>10</sup>, and molecules<sup>11</sup>. The traditional view holds that it is impossible to observe both aspects at the same time. However, recent experiments have demonstrated that both the wave nature and particle nature can be observed

simultaneously $^{12-15}$ . Therefore, further investigation on wave-particle duality is necessary.

Heisenberg's uncertainty principle $^{16}$ , another cornerstone of quantum mechanics, limits how precisely one can measure two incompatible observables, such as position and momentum, of a quantum system. This phenomenon is closely related to wave-particle duality, as both reflect the inherent complementarity of quantum phenomena. In fact, it has been shown that wave-particle duality and entropic uncertainty relations are equivalent $^{17,18}$ . Consequently, the strategies employed to study uncertainty relations can be extended to investigate wave-particle duality $^{19-22}$ . This raises intriguing questions: how does quantum memory, which can reduce uncertainty $^{23-25}$ , affect wave-particle duality? Is there a link between the entanglement of the system and its quantum memory or the wave-particle duality exhibited by the system $^{26,27}$ ?

We address these questions by introducing a conservation law governing the relations among wave behaviour, particle behaviour and entanglement (wave-particle-entanglement triad) through resource monotones. Through the variability of these monotones, we obtain an array of conservation laws. Our results suggest that increasing the entanglement between a system and its memory will reduce the wave-particle duality that can be observed. Additionally, we discover a threefold

complementarity among coherence, purity, and entanglement, shedding light on the interplay of these fundamental quantum resources. Finally, we demonstrate the wave-particle-entanglement triad in both qubit and qudit systems via a silicon-integrated nanophotonic quantum chip[28]. Our experiments address the missing piece of wave-particle duality, entanglement, and confirm the universal conservation laws.

# Results

# Universal conservation laws

To begin our investigation, we explore the particle behaviour of a system. Consider an  $n$ -path interferometer, where the state encountering the  $k$ -th path is represented by  $|k\rangle$ . For the real-valued function  $\mathfrak{P}$  to be a valid measure of particle behaviour, it should satisfy[29-31] the following: (P1) It equals one iff a path is traversed with certainty. (P2) It vanishes when the state is equally likely to occur across all possible paths. (P3) It remains unchanged by path relabelling. (P4) It can only decrease under mixing. Given any differentiable, strictly convex, real-valued function  $f$ , it is proven that a modification coefficient  $c_{1}$  exists such that

$$
\mathfrak {P} (\rho) := c _ {1} \left(\operatorname {T r} [ f (\Delta (\rho)) ] - n f \left(\frac {1}{n}\right)\right) \tag {1}
$$

forms a metric for the particle behaviour. Here,  $\Delta (\cdot): = \sum_{k = 0}^{n - 1}|k\rangle \langle k|\cdot |k\rangle \langle k|$  represents the completely dephasing channel. In Eq. (1), we naturally extend the function  $f$  to Hermitian matrices. For example, consider a matrix  $M$  with spectral decomposition  $M = \sum_{k}\lambda_{k}|\lambda_{k}\rangle \langle \lambda_{k}|$ , where  $f(M)$  takes the form  $\sum_{k}f(\lambda_{k})|\lambda_{k}\rangle \langle \lambda_{k}|$ . The particle behaviour essentially measures the ability to predict the path of a photon. From the perspective of information theory, the convex function  $f$  can be given by any entropy functions such as the von Neumann entropy,  $f(x) = x\log x$ . The first term in the right hand side of Eq. (1), up to the constant  $c_{1}$ , indicates the information retained by the state after the measurement  $\Pi = \{|k\rangle \langle k|\}_{k = 0}^{n - 1}$ , and the second term represents the maximum information obtainable from the whole system. Thus, the particle behaviour  $\mathfrak{P}(\rho)$  in Eq. (1) quantifies the information accessible through the measurement  $\Pi$ . For example, if  $\mathfrak{P}(\rho) = 0$ , no information can be inferred from the measurement  $\Pi$ , meaning that the photon path cannot be identified at all.

Continuing our exploration, we analyse the wave behaviour of a state, pinpointing the foundational prerequisites that a metric  $\mathfrak{W}$  must satisfy $^{29-31}$ : (W1) It equals one when the state has an equal probability of occurring across all pathways. (W2) It vanishes when the state remains unchanged under a completely dephasing channel. (W3) It remains invariant under the relabelling

of interferometric paths. (W4) It is convex. In this context, a differentiable, strictly convex, and real-valued function  $g$  introduces a modification coefficient  $c_{2}$ , defining the metric

$$
\mathfrak {W} (\rho) := c _ {2} \operatorname {T r} [ g (\rho) - g (\Delta (\rho)) ] \tag {2}
$$

which meets (W1) to (W3); however, to comply with (W4),  $\mathfrak{W}$  should also fulfil (W5) for  $0\leq \lambda \leq 1$  the monotonicity  $\mathfrak{W}(\lambda \rho)\leq \lambda \mathfrak{W}(\rho)$  holds, and (W6) it is nonincreasing under incoherent operations. Similarly, the wave behaviour  $\mathfrak{W}(\rho)$  in Eq. (2) quantifies the difference between the information associated with the quantum state and the information available when the state is measured.

Transitioning to entanglement, we focus on the case of a pure bipartite state  $\psi_{AB}$  with  $\dim \mathcal{H}_A = \dim \mathcal{H}_B = n$ . The reduced state  $\rho_A := \mathrm{Tr}_B[\psi_{AB}]$  then fully specifies the entanglement between systems, and we can define the entanglement monotone as

$$
\mathfrak {E} \left(\psi_ {A B}\right) := c _ {3} (h (1) + (n - 1) h (0) - \operatorname {T r} [ h \left(\rho_ {A}\right) ]) \tag {3}
$$

with  $h$  being a differentiable, strictly convex, and real-valued function. The term  $h(1) + (n - 1)h(0)$  makes  $\mathfrak{E}$  zero for separable states. Additionally, the coefficient  $c_3$  sets the range of  $\mathfrak{E}$  to [0, 1]. Further details on  $\mathfrak{P}, \mathfrak{W}$ , and  $\mathfrak{E}$  are provided in Sec. I of the Supplementary Information.

Having provided the preliminary information, we now introduce our main results. A sketch diagram is provided in Fig. 1.

Theorem 1. Consider a pure bipartite state  $\psi_{AB}$ . When we assign  $f = g = h$  (see Eqs. (1), (2) and (3)), we have

![](images/c998f1bee8f3902287bdda781c90fc1ab61643d90b49085cd090abfe77b08581.jpg)  
Fig. 1 Diagrammatic sketch of the conservation laws. In the conventional approach for exploring wave-particle duality, predictability  $P$  (particle behaviour) and visibility  $V$  (wave behaviour) are constrained by the inequality  $P^2 + V^2 \leq 1^3$ . Our theorem introduces a missing element—entanglement—which leads to a more comprehensive conservation law. By varying the resource measures of wave behaviour, particle behaviour, and entanglement, we obtain an infinite family of conservation laws. Hence, we refer to it as universal conservation laws

$c_{1} = c_{2} = c_{3},$  and these metrics satisfy the following equation:

$$
\mathfrak {P} \left(\rho_ {A}\right) + \mathfrak {W} \left(\rho_ {A}\right) + \mathfrak {E} \left(\psi_ {A B}\right) = c \tag {4}
$$

where  $c$  depends on  $f$  and  $n$ .

Given that any single system state can be extended to a pure bipartite state, a process known as purification, where the additional system acts as the environment, we can view wave-particle duality as a special case of our conservation law when the environment is ignored. Exploiting flexibility in selecting  $f$ , Eq. (4) yields an infinite set of conservation laws, which are therefore called universal conservation laws. We present some examples to demonstrate the generality of this equation.

Example 1. After choosing  $f(x) = x \log x$  and applying a scalar,  $\mathfrak{V}(\rho_A)$  becomes the quantum relative entropy of  $\Delta (\rho_{A})$  with respect to the maximally mixed state  $\mathbb{1} / n$ ; i.e.,  $\mathcal{P}_{rel}(\Delta (\rho_A)) := D(\Delta (\rho_A)||\mathbb{1} / n)$ , where  $D(\cdot ||\cdot)$  denotes the quantum relative entropy. Here,  $\mathcal{P}_{rel}$  forms a purity monotone. Moreover,  $\mathfrak{W}(\rho_A)$  corresponds to the relative entropy of coherence<sup>32</sup>; i.e.,  $\mathcal{C}_{rel}(\rho_A) := \min_{\sigma \in \mathcal{T}} D(\rho_A||\sigma)$ ,

where  $\mathcal{I}$  represents the set of all incoherent states. In this case,  $\mathfrak{E}(\psi_{AB})$  is the entanglement entropy  $H(\rho_A)^{33 - 35}$ , and Eq. (4) takes the form

$$
\mathcal {P} _ {r e l} \left(\Delta \left(\rho_ {A}\right)\right) + \mathcal {C} _ {r e l} \left(\rho_ {A}\right) + H \left(\rho_ {A}\right) = \log n \tag {5}
$$

which shows that the sum of purity, coherence, and entanglement is a constant.

Example 2. With  $f(x) = x^{2}$ ,  $\mathcal{P}(\Delta(\rho_{A})) \coloneqq (n - 1)\mathfrak{P}(\rho_{A}) / n$  becomes a purity monotone for  $\Delta(\rho_{A})$ , while  $C_{l_{2}}(\rho_{A}) \coloneqq (n - 1)\mathfrak{W}(\rho_{A}) / n$  is the  $l_{2}$ -norm coherence of  $\rho_{A}^{32}$ , and  $C_{A}(\psi_{AB}) \coloneqq \sqrt{2(n - 1)\mathfrak{E}(\rho_{A}) / n}$  represents the concurrence of  $\psi_{AB}^{33}$ . Eq. (4) now implies

$$
\mathcal {P} \left(\Delta \left(\rho_ {A}\right)\right) + \mathcal {C} _ {l _ {2}} \left(\rho_ {A}\right) + \frac {C _ {A} ^ {2} \left(\psi_ {A B}\right)}{2} = 1 - \frac {1}{n} \tag {6}
$$

Again, this indicates complementarity among purity, coherence, and entanglement.

Here, we make two remarks: (i) Thm. 1 mainly concerns bipartite pure states. For mixed states, Eq. (4) becomes an inequality. Further details are provided in Sec. I.C of the Supplementary Information. (ii) The complementarity of the wave-particle-entanglement triad is more general than Thm. 1 suggests. An alternative framework for the conservation laws of path predictability (particle behaviour), interference visibility (wave behaviour), and entanglement is presented in

Sec. I.E of the Supplementary Information. Two illustrative examples are given below.

Example 3. In  $n$ -path interference, path predictability indicates the accuracy of inferring the photon trajectory. It is quantified by the optimal probability of correctly discerning whether the photon traverses path  $\{|k\rangle\}_{k=0}^{n-1}$ . For state  $\rho_{A}$ , the particle behaviour is then quantified by  $\mathfrak{P}(\rho_{A}) := 1 - (\sum_{i \neq j} \sqrt{\rho_{ii} \rho_{jj}}) / (n-1)$ . Moreover, the  $I_{1}$ -norm coherence reflects the interference visibility; i.e., the wave behaviour is characterized by  $\mathfrak{W}(\rho_{A}) := C_{I_{1}}(\rho_{A}) / (n-1)$ . Entanglement is measured by a monotone function  $h$  of  $I$  concurrence  $C_{I}^{37,38}$ . These quantities satisfy

$$
\mathfrak {P} \left(\rho_ {A}\right) + \mathfrak {W} \left(\rho_ {A}\right) + h \left(C _ {I} \left(\psi_ {A B}\right)\right) = 1 \tag {7}
$$

The definitions of  $l_{1}$ -norm coherence and  $I$  concurrence are provided in Sec. I.E of the Supplementary Information. Eq. (7) is not covered by Thm. 1, because  $h(C_I(\psi_{AB}))$  does not have the form specified in Eq. (3).

Example 4. In  $n$ -path interference, path predictability is assessed by computing the average success probability of predicting the photon trajectory, which is expressed as  $\mathfrak{P}^2(\rho_A) \coloneqq n\left(\sum_i \rho_{ii}^2 - 1/n\right) / (n - 1)^{29}$ . The interference visibility is quantified by the  $l_2$ -norm coherence, i.e.,  $\mathfrak{W}^2(\rho_A) \coloneqq n\mathcal{C}_{l_2}(\rho_A) / (n - 1)$ , along with  $I$  concurrence, resulting in<sup>40</sup>:

$$
\mathfrak {P} ^ {2} \left(\rho_ {A}\right) + \mathfrak {W} ^ {2} \left(\rho_ {A}\right) + C _ {I} ^ {2} \left(\psi_ {A B}\right) = 1 \tag {8}
$$

Here, Eq. (8) is not covered by Thm. 1, as it involves a higher-order resource monotone.

# Experimental setup

Figure 2 illustrates the silicon-integrated nanophotonic quantum chip used in our experiments. This device supports arbitrary controlled unitaries, as shown in Fig. 2a, and represents an advanced iteration of earlier designs $^{41,42}$ . The chip is engineered to enable the generation of wave-particle transitions, as well as the measurement of properties associated with wave-particle behaviour and entanglement. On the chip, we first prepare a maximally entangled state of the form  $(|0\rangle_c|0\rangle_t + |1\rangle_c|1\rangle_t) / \sqrt{2}$  via a pair of integrated SFWM sources, where  $|i\rangle_{c}$  and  $|i\rangle_{t}$ $(i = 0,1)$  represent the path-encoded logical states of the control and target photons. The control photon directs the target photon through either the upper green or lower red circuit, creating a superposition in two distinct waveguide layers, as shown in Fig. 2b. By either passing through an  $n$ -BS (lower red) or not passing through it (upper green), the target photon can be in one of two states:  $|p\rangle \coloneqq |0\rangle$ , exhibiting a full-particle nature, or  $|w\rangle \coloneqq (\sum_i|i\rangle) / \sqrt{n}$ , exhibiting maximal

![](images/5f8d02eb4024141fafd1e5039b31d9da8adef63946befa6663bb0bc7c5c5c435.jpg)  
a

![](images/cf6c7477152c1f89c4a979dd9fc4a820d59941bd5de6834e5357f71a81f44ce6.jpg)  
Fig. 2 A silicon-integrated nanophotonic quantum chip for demonstrating universal conservation laws. a Quantum circuit for the controlled quantum Fourier transform. The unitary operators and detectors constitute the measurement apparatuses  $\hat{M}_{c,t}$ . b Simplified schematic for the quantum chip, consisting of four main components: an entangled photon-pair source, a quantum-controlled  $n$ -path beamsplitter ( $n$ -BS),  $n$ -path Mach-Zehnder interferometers ( $n$ -MZIs), and an  $n$ -mode eraser, with off-chip detectors. Integrated spontaneous four-wave mixing (SFWM) sources generate path-entangled signal (blue) and idler (orange) photons. The signal photon acts as the control, whereas the idler photon acts as the target. Depending on the control photon, the target photon exhibits particle behaviour (upper green circuits), wave behaviour (lower red circuits), or a superposition. Measurement apparatuses  $\hat{M}_{c,t}$  perform unitary operations to project photons onto a specific basis. The quantum eraser ensures process indistinguishability. Single photons are detected via fibre-coupled superconducting-nanowire single-photon detectors (SNSPDs)  
b

wave behaviour. The resulting state is  $\left|\psi_0\right\rangle_{ct} \coloneqq \left(|0\rangle_c|p\rangle_t + |1\rangle_c|w\rangle_t\right) / \sqrt{2}$ . Using our chip, we generate two families of quantum states from  $\left|\psi_0\right\rangle_{ct}$  to demonstrate conservation laws. The first family,  $|\psi_1\rangle_{ct} \coloneqq |0\rangle_c \otimes (\sin \frac{\alpha}{2}|p\rangle_t + \cos \frac{\alpha}{2}|w\rangle_t)$ , represents a coherent (quantum) superposition of  $|p\rangle$  and  $|w\rangle$  on the target system. The second family,  $|\psi_2\rangle_{ct} \coloneqq \sin \frac{\alpha}{2}|0\rangle_c|p\rangle_t + \cos \frac{\alpha}{2}|1\rangle_c|w\rangle_t$ , represents a probabilistic (classical) mixture of  $|p\rangle$  and  $|w\rangle$  on the target system. Both are controlled by the rotation angle  $\alpha$ . The details of the state preparation and measurement methods are discussed in the Methods and Sec. II of the Supplementary Information.

# Experimental test of generalized multipath conservation laws

We first observe the behaviour of the full-wave state at  $\alpha = \pi$  and the full-particle state at  $\alpha = 0$  in the  $n$ -path experiment. In the measurement apparatus  $\hat{M}_t$ , we apply phases  $\{\theta_k = k\theta\}_{k=0}^{n-1}$  to the target photon paths and project them into  $|w\rangle = (\sum_i |i\rangle) / \sqrt{n}$ . By scanning  $\theta$ , we observe an  $n$ -path interference fringe for the full-wave and full-particle states, shown in Fig. 3a, b.

Our first experiment investigates the complementary nature of purity, coherence, and entanglement in qubit cases, as detailed in Ex. 1. To demonstrate Eq. (5), we extract the diagonal elements and eigenvalues of the reduced state  $\rho_{i} := \mathrm{Tr}_{c}[\psi_{i}]$  ( $i = 1, 2$ ). The diagonal elements of  $\rho_{i}$  are obtained directly via computational basis measurements. The eigenvalues,  $\lambda_{\pm}(\rho_{i})$ , are calculated via the  $I$  concurrence  $C_I(\psi_i)$  as  $\lambda_{\pm}(\rho_{i}) = (1 \pm \sqrt{1 - C_{I}^{2}(\psi_{i})}) / 2$ , which can be derived from Pauli measurements  $\{\sigma_0 = \mathbb{1}, \sigma_x, \sigma_y, \sigma_z\}$ [43]

directly:  $C_I^2 (\psi_i) = (1 + \langle \sigma_z\sigma_z\rangle^2 -\langle \sigma_z\sigma_0\rangle^2 -\langle \sigma_0\sigma_z\rangle^2 - \langle \sigma_0\sigma_x\rangle^2 +\langle \sigma_z\sigma_x\rangle^2 -\langle \sigma_0\sigma_y\rangle^2 +\langle \sigma_z\sigma_y\rangle^2) / 2.$  The experimental data depicted in Fig. 3c agree with our theoretical results.

We next illustrate how a nonhomogeneous polynomial of path predictability, interference visibility, and concurrence captures wave-particle-entanglement complementarity (see Eq. (6)). To assess  $\mathrm{Tr}[\rho_i^2]$  for path predictability and concurrence, we measure the Gell-Mann matrices  $\varLambda_{j}^{44}$  in our experiments, as described by  $\mathrm{Tr}[\rho_i^2] = 1 / n + \sum_{j=1}^{n^2 - 1} \langle \Lambda_j \rangle^2 / 2$ . To measure interference visibility, we use the fringe visibility  $V_{i,jk} := 2|\rho_{i,jk}| / (\rho_{i,jj} + \rho_{i,kk})$  between paths  $j$  and  $k$ , which is more practical for the experiments. By introducing an additional phase in the  $j$ -th path and measuring the target photon in the basis  $(|j\rangle + |k\rangle) / \sqrt{2}$ , we observe an interference fringe between paths  $j$  and  $k$ . Abstracting the visibility involves fitting the fringe with a general cosine curve, represented as  $\mathcal{C}_{l_2}(\rho_i) = n\sum_{j < k} (\rho_{i,jj} + \rho_{i,kk})^2 V_{ijk}^2 / 2(n - 1)$ . Our experiments, depicted in Fig. 3d, align with the theoretical predictions, affirming the conservation laws outlined in Ex.2.

We next report the complementarity of wave-particle-entanglement by quantifying path predictability, interference visibility, and  $I$  concurrence, as shown in Ex. 3 for both qubit and qudit ( $n = 3, 4$ ) systems. To extend our findings to qudit systems, we present a generalized form of Eq. (7) that is applicable to any finite-dimensional system in Sec. I.E of the Supplementary Information. Path predictability is derived from computational basis measurements conducted on the target

![](images/71f0d38c4d914faf95c18bf907afe657e0bcd4033d9e28dfe0b89cce8fddfc06.jpg)  
a

![](images/4b31bf9602c457330f8c86f819a4b62c69f8148b19f8da4202a99cc60c7eb221.jpg)  
C

![](images/a8e37859eae63b0ab12c1992996fd7299c3006b33ecf572c0def0f00b4d70adb.jpg)  
d

![](images/adc37a9814311c200324c2e28a876e2f3e93b3d6250aa6fee454aa1dcffe0413.jpg)  
e

![](images/b1c839d129e5ff9197e5d38db49db68a3eafae4089996aa9d25a03c40dcb9458.jpg)  
b  
Fig. 3 Experimental data of the conservation laws. a, b Quantum fringes after  $n$ -BS for the full-wave state  $|w\rangle$  and full-particle state  $|p\rangle$  for  $n = 2, 3, 4$ . The wave-like interference fringe becomes sharper for higher dimensions, and the particle-like distribution results in a  $1/n$  probability at the output. c The 2-path complementarity relation, shown in Ex. 1, pertains to the states  $|\psi_1\rangle_{ct}$  and  $|\psi_2\rangle_{ct}$ . d, e Complementarity relations, as shown in Ex. 2 and Ex. 3, apply to the states  $|\psi_1\rangle_{ct}$  and  $|\psi_2\rangle_{ct}$  for the 2-path experiments. The results for the 3, 4-path experiments can be found in Sec. III of the Supplementary Information. The conserved resources are highlighted in orange. This validates the universal conservation laws across various  $\{n, a\}$  configurations, including both quantum-superposition  $|\psi_1\rangle_{ct}$  and classical-mixture  $|\psi_2\rangle_{ct}$  instances of wave-particle duality. The error bars  $(\pm \sigma)$  are estimated from the photon Poissonian statistics

![](images/a789aa941a2bebcb7f3278e497ce5c7f1d25399b5cc9c0202a829f4ba924d528.jpg)

![](images/27120cfbb36d05808767a945f682fc8a8529e13111765d404145a54f985a9839.jpg)

![](images/47d20199de7248a9bcd7eccec650b5711be5933d9705a77529ea58462a4a3447.jpg)

![](images/eebb1de41301c3fc1cd2f8e71ec2290ea5045f25d7776ec9ebcd16c69e815e2c.jpg)

system. Interference visibility, on the other hand, is expressed as a function of the incoherence intensity  $I_{\mathrm{inc}} \coloneqq (\sum_{j} \rho_{i,j j}) / n$  ( $\rho_{i,j j}$  denotes element  $(j, j)$  of the reduced state  $\rho_{i}$ ) and the maximal  $n$ -path interference fringe  $I_{\mathrm{max}}$ ; i.e.,  $\mathcal{C}_{l_1}(\rho_i) = (I_{\mathrm{max}} - I_{\mathrm{inc}}) / ((n - 1)I_{\mathrm{inc}})$ . We determine the maximal interference fringe  $I_{\mathrm{max}}$  via the measurement apparatus  $\hat{M}_t$ . After applying phases  $\{\theta_k\}_{k=0}^{n-1}$  to the target photon paths, we project them onto the state  $|w\rangle = (\sum_{i}|i\rangle) / \sqrt{n}$ . By scanning these phases, we observe an  $n$ -path interference fringe, with  $I_{\mathrm{max}}$  marking its peak. To isolate a submatrix  $\rho_i^{jk}$  in the target system, we block all interference paths except the  $j$ -th and  $k$ -th paths. Denoting  $\rho_{i,00}^{jk}$  and  $\rho_{i,11}^{jk}$  as its diagonal elements, we define  $C_I^{jk}(\psi_i)$  as the  $(j, k)$ -concurrence of the state  $\psi_i$ . Now, the entanglement monotone of Eq. (7) is expressed as  $h(C_I(\psi_i)) = \sum_{j \neq k} E^{jk} / (n - 1)$ , with  $E^{jk} := \sqrt{\rho_{i,00}^{jk} \rho_{i,11}^{jk}} - \sqrt{\rho_{i,00}^{jk} \rho_{i,11}^{jk} - \frac{1}{4} (\rho_{i,00}^{jk} + \rho_{i,11}^{jk})^2 (C_I^{jk}(\psi_i))^2}$ . In this case, the  $(i, j)$ -concurrence is determined by performing Pauli measurements on the target system, as  $(C_I^{jk}(\psi_i))^2 = 1 - \langle \sigma_x\rangle^2 - \langle \sigma_y\rangle^2 - \langle \sigma_z\rangle^2$ . Figure 3e shows close agreement between our experimental data and the theoretical predictions, confirming that path predictability, interference visibility, and entanglement collectively converge to a constant value.

In our last experiment, we investigate the impact of noise on conservation laws. Our theoretical analysis reveals that when the bipartite state shared between the control system and the target system is a mixed state, the conservation laws are violated. We take the conservation law in Eq. (8) as an example. By adding white noise, which is controlled by the error parameter  $\epsilon$ , we obtain the state

$(1 - \epsilon)\big|\psi_0\rangle \big{\langle}\psi_0\big|_{ct} + \epsilon I_{ct} / (\dim \mathcal{H}_c\dim \mathcal{H}_t).$  The total amount of path predictability, interference visibility, and  $I$  concurrence decreases as the error increases, as demonstrated in Fig. 4. When the state becomes a maximally mixed state, namely,  $\epsilon = 1$ , the total path predictability, interference visibility, and  $I$  concurrence vanishes.

# Discussion

Wave-particle duality reveals the distinctive nature of quantum mechanics, demonstrating that classical concepts such as particles and waves cannot fully describe quantum entities $^{13,45,46}$ . However, our exploration has shown that this model is incomplete. When a target system is entangled with a control system, the entanglement between them is the key missing element, complementing the wave-particle duality to yield a comprehensive framework: conservation laws for the wave-particle-entanglement triad. Rather than presenting a single conservation law, we adopt a resource-theoretical approach, introducing general resource monotones for wave-like and particle-like behaviours, as well as for quantum entanglement. This approach enables us to determine the overarching connections among these elements and derive a family of conservation laws that govern the wave-particle-entanglement triad.

We tested our findings on a nanophotonic chip and verified the related conservation laws. In addition to conventional qubit-based quantum systems, the highly controllable multidimensional quantum devices and systems on large-scale integrated quantum photonics platforms enable us to extend our experiments to qudit systems. Furthermore, we examined the effect of noise on these conservation laws, showing that increased error

![](images/bc6e875fdbd8fb594932660e497289de036092f03fed6d39e9641a3f7596b2bc.jpg)  
Fig. 4 Impact of noise on conservation laws. The sum of wave, particle, and entanglement properties equals one for Ex. 4 (with mixture ratio  $\epsilon = 0$ ), and this sum gradually decreases as the noise increases. When the system becomes completely noisy (with mixture ratio  $\epsilon = 1$ ), their combined total diminishes to zero. The theoretical predictions and observed data are indicated in orange. The inset diagram displays the measured density matrices for the pure state  $|\psi_0\rangle_{ct}$  and for the state subjected to white noise. These matrices are reconstructed through quantum-state tomographic measurements. The heights and colours of the bars represent the absolute values and phases of the matrix elements, respectively. The quantum state fidelities are calculated as 0.977(8) for the pure state ( $\epsilon = 0$ ) and 0.994(1) for the noisy state ( $\epsilon = 1$ ). Here, fidelity is quantified by the formula  $F(\rho, \rho_0) \coloneqq \left(\mathrm{Tr} \sqrt{\sqrt{\rho_0} \rho \sqrt{\rho_0}}\right)^2$ , where  $\rho$  denotes the reconstructed state and  $\rho_0$  denotes the ideal state

leads to a decrease in path predictability $^{40}$ , interference visibility $^{36}$ , and  $I$  concurrence.

This work not only deepens our understanding of quantum theory but also highlights numerous avenues for future inquiry. For example, it prompts exploration into the way wave-particle behaviours correlate with quantum system interactions when multiple systems are considered. Moreover, in dealing with mixed states, there is a need to devise inequalities that describe wave-particle duality, particularly in the presence of quantum memory $^{23,47}$ . Entanglement is pivotal in advancing communication $^{48}$ , cryptography $^{49}$ , and quantum computing $^{50}$ . Its connection to wave-particle duality raises questions about practical applications. Bridging theoretical developments with experimental realizations holds promise for advancing quantum information science and technologies.

# Materials and methods

# Device fabrication

The silicon nanophotonic quantum chip is fabricated with  $180\mathrm{nm}$  standard complementary metal-oxide-semiconductor (CMOS) processes on a  $200\mathrm{mm}$  silicon-on-insulator (SOI) wafer with a  $3\mu \mathrm{m}$ -thick buried oxide layer and a  $220\mathrm{nm}$ -thick top silicon layer. The waveguide circuit patterns are defined by  $248\mathrm{nm}$  deep ultraviolet (DUV) photolithography and then transferred by double inductively coupled plasma (ICP) etching processes from

the photoresist layer to the silicon layer. Above the waveguide layer, a  $1\mu \mathrm{m}$ -thick silicon dioxide  $(\mathrm{SiO}_2)$  layer is deposited via plasma-enhanced chemical vapour deposition (PECVD) to isolate the resistive heaters and optical waveguides. Finally, a  $50\mathrm{nm}$ -thick titanium nitride (TiN) layer is deposited, patterned, and etched to form resistive thermal-optic phase shifters. Single photons are generated and guided in silicon waveguides with a cross-section of  $450\times 220\mathrm{nm}$  and propagation loss of  $1 - 2\mathrm{dB}/$  cm. As the optical input/output (I/O), the grating couplers consist of shallow etching waveguides with an etched depth of  $70\mathrm{nm}$  and a coupling loss of approximately  $3 - 4\mathrm{dB}$ /facet.

# Experimental setup

The chip is injected by a tuneable continuous-wave (CW) laser (EXFO) at a wavelength of  $1550.11\mathrm{nm}$ , which is amplified to approximately  $100\mathrm{mW}$  by an erbium-doped fibre amplifier (EDFA). Before injection, a fibre-based polarization controller (PC) is adopted to optimize the polarization of the pumped light in the fibre and ensure transverse electric mode excitations in the silicon waveguides. Entangled photon pairs (signal photons at a wavelength of  $1545.32\mathrm{nm}$  and idler photons at a wavelength of  $1554.94\mathrm{nm}$ ) are generated in integrated sources through the spontaneous four-wave mixing (SFWM) process and then spatially separated by asymmetric Mach-Zehnder

interferometers (AMZIs). Single photons are routed off-chip and detected by an array of fibre-coupled superconducting nanowire single-photon detectors (SNSPDs) with an average efficiency of  $85\%$ . Twofold photon coincidence counts are recorded by a multichannel time interval analyser (TIA). The quantum chip is packaged on a printed circuit board (PCB) and wire bonded. All phase shifters can be accessed and controlled individually by multichannel electronic drivers with 16-bit precision and  $\mathrm{kHz}$  speed. To stabilize the quantum operations and suppress thermal noise and thermal crosstalk, the chip is temperature monitored and stabilized.

# General measurements of wave-particle transitions

Our quantum photonic chip incorporates an entangled photon source, a controllable  $n$ -BS, measurement apparatuses denoted as  $\hat{M}_{c,t}$ , an  $n$ -mode quantum eraser, and a control qubit projector. This configuration facilitates the preparation and measurement of states that exhibit wave-particle duality transitions. The initial Bell state  $(|0\rangle_c|0\rangle_t + |1\rangle_c|1\rangle_t) / \sqrt{2}$  is prepared through the coherent excitation of a pair of SFWM sources at a two-photon coincidence count rate of approximately  $100 / s$ . Following generation, the signal and idler photons are separated by an on-chip AMZI and directed along distinct paths, serving as control and target photons, respectively. The subsequent operation of a controlled  $n$ -BS leads to the maximally entangled wave-particle state  $(|0\rangle_c|p\rangle_t + |1\rangle_c|w\rangle_t) / \sqrt{2}$ . The measurement apparatuses  $\hat{M}_{c,t}$  implement state-dependent unitary matrices  $U_{c,0/1}$  and  $U_{t,p/w}$  on the control and target photons, respectively. Notably, when the control photon is injected into the first port of  $\hat{M}_c$ , an additional Pauli gate  $\sigma_x$  is necessary for the state  $|1\rangle_c$ , completing the overall state

$$
\frac {1}{\sqrt {2}} \left(U _ {c, 0} | 0 \rangle_ {c} \otimes U _ {t, p} | p \rangle_ {t} + U _ {c, 1} \cdot \sigma_ {x} | 1 \rangle_ {c} \otimes U _ {t, w} | w \rangle_ {t}\right) \tag {9}
$$

The control photon is projected and measured in the basis

$$
\left. \left\{\sin \frac {\alpha}{2} | 0 \rangle + e ^ {i \delta} \cos \frac {\alpha}{2} | 1 \rangle , \cos \frac {\alpha}{2} | 0 \rangle - e ^ {i \delta} \sin \frac {\alpha}{2} | 1 \rangle \right\} \right. \tag {10}
$$

and the target photon is symmetrically partitioned by the quantum eraser. The coincidences recorded between detectors  $\{D_{c,0}, D_{c,1}\}$  and  $\{D_{t,j}\}_{j=0}^{n-1}$  indicate the state

$$
\sin \frac {\alpha}{2} \left(U _ {c, 0} | 0 \rangle_ {c} \otimes U _ {t, p} | p \rangle_ {t}\right) + e ^ {i \delta} \cos \frac {\alpha}{2} \left(U _ {c, 1} | 0 \rangle_ {c} \otimes U _ {t, w} | w \rangle_ {t}\right) \tag {11}
$$

and the coincidences between  $\{D_{c,0}, D_{c,1}\}$  and  $\{D_{t,j}^{\prime}\}_{j=0}^{n-1}$  correspond to the state

$$
\sin \frac {\alpha}{2} \left(U _ {c, 0} | 0 \rangle_ {c} \otimes U _ {t, p} | p \rangle_ {t}\right) - e ^ {i \delta} \cos \frac {\alpha}{2} \left(U _ {c, 1} | 0 \rangle_ {c} \otimes U _ {t, w} | w \rangle_ {t}\right) \tag {12}
$$

We obtain a wave-particle transition by systematically varying the parameters  $\{\alpha, \delta\}$ . The quantum properties

inherent in the control-target system can be experimentally extracted through the strategic selection of the unitary matrices  $U_{c,0/1}$  and  $U_{t,p/w}$ . The extraction of most properties can be reduced to the measurement of an expectation value  $\langle \mathcal{O}_s \mathcal{O}_i \rangle$ . By choosing appropriate unitary matrices, each expectation value measurement takes 20 seconds at the given counting rate.

# Acknowledgements

We would like to thank Varun Narasimhachar, Mile Gu, and Jun Ye for fruitful discussions. This work is supported by the Fundamental Research Funds for the Central Universities, the National Natural Science Foundation of China (nos. 12371132, 12325410, 61975001, 12075159, and 12171044), the Innovation Program for Quantum Science and Technology (2021ZD0301500), the National Key R&D Program of China (2019YFA0308702), and the specific research fund of the Innovation Platform for Academicians of Hainan Province under Grant No. YSPTZX202215. Y. X. acknowledges support from the National Research Foundation of Singapore and A\*STAR under its Quantum Engineering Programme (NRF2021-QEP2-02-P03), and from A\*STAR under its Central Research Funds and grant C230917003.

# Author details

$^{1}$ School of Mathematical Sciences, MOE-LSC, Shanghai Jiao Tong University, Shanghai 200240, China.  $^{2}$ State Key Laboratory for Mesoscopic Physics, School of Physics, Peking University, Beijing 100871, China.  $^{3}$ Beijing Academy of Quantum Information Sciences, Beijing 100871, China.  $^{4}$ School of Mathematical Sciences, Capital Normal University, Beijing 100048, China.  $^{5}$ Max Planck Institute for Mathematics in the Sciences, Leipzig 04103, Germany.  $^{6}$ Department of Physics and Astronomy, Stony Brook University, New York, NY 11794-3800, USA.  $^{7}$ Shanghai Seres Information Technology Co., Ltd, Shanghai 200040, China.  $^{8}$ Shenzhen Institute for Quantum Science and Engineering, Southern University of Science and Technology, Shenzhen 518055, China.  $^{9}$ A*STAR Quantum Innovation Centre (Q.InC), Agency for Science, Technology and Research (A*STAR), 2 Fusionopolis Way, Innovis \#08-03, Singapore 138634, Republic of Singapore.  $^{10}$ Institute of High Performance Computing (IHPC), Agency for Science, Technology and Research (A*STAR), 1 Fusionopolis Way, Connexis \#16-16, Singapore 138632, Republic of Singapore

# Author contributions

J.W. conceived the project. Z.D., Y.D., and S.-M.F. contributed equally to this work. Y.D. and X.C. built the setup and carried out the experiments. Z.D., S.-Q.Z., Z.R., Z.M., and Y.X. developed the theoretical framework. Z.M., Y.X., and J.W. managed the project. All the authors contributed through in-depth discussion. Y.X., Z.M., and J.W. wrote the manuscript with contributions from all the authors.

# Data availability

The data that support the findings of this study are available from the corresponding author upon reasonable request.

# Conflict of interest

The authors declare no competing interests.

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41377-025-01759-4.

Received: 23 August 2024 Revised: 1 January 2025 Accepted: 14 January 2025

Published online: 12 February 2025

# References

1. Wootters, W. K. & Zurek, W. H. Complementarity in the double-slit experiment: Quantum nonseparability and a quantitative statement of bohr's principle. Phys. Rev. D. 19, 473-484 (1979).  
2. Jaeger, G., Shimony, A. & Vaidman, L. Two interferometric complementarities. Phys. Rev. A 51, 54-67 (1995).

3. Englert, B. G. Fringe visibility and which-way information: An inequality. Phys. Rev. Lett. 77, 2154-2157 (1996).  
4. Qian, X. F. & Agarwal, G. S. Quantum duality: A source point of view. Phys. Rev. Res. 2, 012031 (2020).  
5. Liu, K et al. A twofold quantum delayed-choice experiment in a superconducting circuit. Sci. Adv. 3, e1603159 (2017).  
6. Xiao, Y. et al. Observing momentum disturbance in double-slit "which-way" measurements. Sci. Adv. 5, eaav9547 (2019).  
7. Chen, D. X. et al. Experimental investigation of wave-particle duality relations in asymmetric beam interference. npj Quantum Inf. 8, 101 (2022).  
8. Grangier, P., Roger, G. & Aspect, A. Experimental evidence for a photon anticorrelation effect on a beam splitter: a new light on single-photon interferences. Europhys. Lett. 1, 173-179 (1986).  
9. Zeilinger, A., Gähler, R., Shull, C. G., Treimer, W. & Mampe, W. Single- and double-slit diffraction of neutrons. Rev. Mod. Phys. 60, 1067-1073 (1988).  
10. Durr, S., Nonn, T. & Rempe, G. Origin of quantum-mechanical complementarity probed by a 'which-way' experiment in an atom interferometer. Nature 395, 33-37 (1998).  
11. Gerlich, S. et al. Quantum interference of large organic molecules. Nat. Commun. 2, 263 (2011).  
12. Tang, J. S. et al. Realization of quantum wheeler's delayed-choice experiment. Nat. Photonics 6, 600-604 (2012).  
13. Wang, K., Xu, Q., Zhu, S. & Ma, X.-s Quantum wave-particle superposition in a delayed-choice experiment. Nat. Photonics 13, 872-877 (2019).  
14. Chen, X. J. et al. A generalized multipath delayed-choice experiment on a large-scale quantum nanophotonic chip. Nat. Commun. 12, 2712 (2021).  
15. Li, J. K. et al. Experimental demonstration of separating the wave-particle duality of a single photon with the quantum cheshire cat. Light Sci. sAppl. 12, 18 (2023).  
16. Heisenberg, W. Über den anschaulichen inhalt der quantentheoretischen kinematik und mechanik. Z. f.ur. Phys. 43, 172-198 (1927).  
17. Coles, P. J., Kaniewski, J. & Wehner, S. Equivalence of wave-particle duality to entropic uncertainty. Nat. Commun. 5, 5814 (2014).  
18. Coles, P. J. Entropic framework for wave-particle duality in multipath interferometers. Phys. Rev. A 93, 062111 (2016).  
19. Durr, S. & Rempe, G. Can wave-particle duality be based on the uncertainty relation? Am. J. Phys. 68, 1021-1024 (2000).  
20. Rudnicki, L., Puchala, Z. & Žyczkowski, K. Strong majorization entropic uncertainty relations. Phys. Rev. A 89, 052115 (2014).  
21. Xiao, Y. L., Yang, Y., Wang, X., Liu, Q. & Gu, M. Quantum uncertainty principles for measurements with interventions. Phys. Rev. Lett. 130, 240201 (2023).  
22. Yuan, Y. et al. Strong majorization uncertainty relations and experimental verifications. npj Quantum Inf. 9, 65 (2023).  
23. Berta, M., Christandl, M., Colbeck, R., Renes, J. M. & Renner, R. The uncertainty principle in the presence of quantum memory. Nat. Phys. 6, 659-662 (2010).  
24. Xiao, Y. L., Jing, N., Fei, S.-M. & Li-Jost, X. Improved uncertainty relation in the presence of quantum memory. J. Phys. A: Math. Theor. 49, 49LT01 (2016).  
25. Xiao, Y. L., Xiang, Y., He, Q. & Sanders, B. C. Quasi-fine-grained uncertainty relations. N. J. Phys. 22, 073063 (2020).  
26. Jakob, M. & Bergou, J. A. Quantitative complementarity relations in bipartite systems: Entanglement as a physical reality. Opt. Commun. 283, 827-830 (2010).

27. Qian, X. F., Varnivakas, A. N. & Eberly, J. H. Entanglement limits duality and vice versa. Optica 5, 942-947 (2018).  
28. Wang, J. W., Sciarrino, F., Laing, A. & Thompson, M. G. Integrated photonic quantum technologies. Nat. Photonics 14, 273-284 (2020).  
29. Durr, S. Quantitative wave-particle duality in multibeam interferometers. Phys. Rev. A 64, 042113 (2001).  
30. Englert, B. G., Kaszlikowski, D., Kwek, L. C. & Chee, W. H. Wave-particle duality in multi-path interferometers: General concepts and three-path interferometers. Int. J. Quantum Inf. 6, 129-157 (2008).  
31. Lu, X. Quantitative wave-particle duality as quantum state discrimination. Phys. Rev. A 102, 022201 (2020).  
32. Baumgratz, T., Cramer, M. & Plenio, M. B. Quantifying coherence. Phys. Rev. Lett. 113, 140401 (2014).  
33. Wootters, W. K. Entanglement of formation of an arbitrary state of two qubits. Phys. Rev. Lett. 80, 2245-2248 (1998).  
34. Plenio, M. B. & Virmani, S. An introduction to entanglement measures. Quantum Inf. Comput. 7, 1-51 (2007).  
35. Horodecki, R., Horodecki, P., Horodecki, M. & Horodecki, K. Quantum entanglement. Rev. Mod. Phys. 81, 865-942 (2009).  
36. Biswas, T., Garcia Diaz, M. & Winter, A. Interferometric visibility and coherence. Proc. R. Soc. A: Math., Phys. Eng. Sci. 473, 20170170 (2017).  
37. Rungta, P. & Caves, C. M. Concurrence-based entanglement measures for isotropic states. Phys. Rev. A 67, 012307 (2003).  
38. Rungta, P., Bužek, V., Caves, C. M., Hillery, M. & Milburn, G. J. Universal state inversion and concurrence in arbitrary dimensions. Phys. Rev. A 64, 042315 (2001).  
39. Qureshi, T. Interference visibility and wave-particle duality in multipath interference. Phys. Rev. A 100, 042105 (2019).  
40. Roy, A. K., Pathania, N., Chandra, N. K., Panigrahi, P. K. & Qureshi, T. Coherence, path predictability, and I concurrence: A triality. Phys. Rev. A 105, 032209 (2022).  
41. Wang, J. W. et al. Experimental quantum hamiltonian learning. Nat. Phys. 13, 551-555 (2017).  
42. Chi, Y. L. et al. A programmable audit-based quantum processor. Nat. Commun. 13, 1166 (2022).  
43. Fei, S. M., Zhao, M.-J., Chen, K. & Wang, Z.-X. Experimental determination of entanglement for arbitrary pure states. Phys. Rev. A 80, 032320 (2009).  
44. Karimi, N., Heshmati, A., Yahyavi, M., Jafarizadeh, M. & Mohammadzadeh, A. Measurability of D-concurrence. Sci. Rep. 9, 19415 (2019).  
45. Björk, G. & Karlsson, A. Complementarity and quantum erasure in welcher Weg experiments. Phys. Rev. A 58, 3477-3483 (1998).  
46. Ma, X. S., Kofler, J. & Zeilinger, A. Delayed-choice gedanken experiments and their realizations. Rev. Mod. Phys. 88, 015005 (2016).  
47. Prevedel, R., Hamel, D. R., Colbeck, R., Fisher, K. & Resch, K. J. Experimental investigation of the uncertainty principle in the presence of quantum memory and its application to witnessing entanglement. Nat. Phys. 7, 757-761 (2011).  
48. Gisin, N. & Thew, R. Quantum communication. Nat. Photonics 1, 165-171 (2007).  
49. Pirandola, S. et al. Advances in quantum cryptography. Adv. Opt. Photonics 12, 1012-1236 (2020).  
50. O'Brien, J. L. Optical quantum computing. Science 318, 1567-1570 (2007).