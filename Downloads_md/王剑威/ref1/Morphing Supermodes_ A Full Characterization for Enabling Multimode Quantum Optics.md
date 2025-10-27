# Morphing Supermodes: A Full Characterization for Enabling Multimode Quantum Optics

Élie Gouzien<sup>1</sup>, Sebastien Tanzilli<sup>1</sup>, Virginia D'Auria<sup>1</sup>, and Giuseppe Patera<sup>2,*</sup>  
<sup>1</sup>Université Cote d'Azur, CNRS, Institut de Physique de Nice, Parc Valrose, 06108 Nice Cedex 2, France  
<sup>2</sup>Université Lille, CNRS, UMR 8523—PhLAM—Physique des Lasers Atomes et Molécules, F-59000 Lille, France

(Received 4 February 2020; accepted 5 August 2020; published 31 August 2020)

In this Letter, we present a universal approach enabling the full characterization of the quantum properties of a multimode optical system in terms of squeezing and morphing supermodes. These are modes undergoing a continuous evolution that allow uncoupling the system dynamics in terms of statistically independent physical observables. This dynamical feature, never considered so far, enables the description and investigation of an extremely broad variety of key resources for experimental quantum optics, ranging from optical parametric oscillators to silicon-based microring resonators, as well as optomechanical systems.

DOI: 10.1103/PhysRevLett.125.103601

Multimode quantum optics in a continuous variables (CVs) regime is at the heart of a multitude of quantum applications, encompassing quantum communication [1,2] and quantum metrology [3], as well as quantum computation [4] via cluster states [5-7].

Commonly, the treatment of multimode optical systems is based on the identification of the so-called supermodes [8-10]. These are coherent superpositions of the original modes that diagonalize the system dynamics and permit one to rewrite multimode CV entangled states as a collection of independent squeezed states [11]. The knowledge of supermodes allows us to optimize the detection of the nonclassical information on the state [8,9,12], generating and exploiting CV cluster states in optical frequency combs [13-15] or in multimode spatial systems [16], as well as engineering complex multimode quantum states [17,18]. In experiments, as they are statistically independent, supermodes can be measured with a single homodyne detector, thus considerably reducing the experimental overhead [15].

The ongoing development of new devices and platforms for quantum optics is enlarging the range of situations requiring a multimode dynamics-decoupling treatment. Traditional theoretical methods, however, are not always adequate and leave uncovered a large set of situations that are relevant for quantum technologies. This is, for instance, the case of the third order nonlinear interactions at the heart of integrated quantum photonics platforms in silicon and silicon nitride [19,20]. Our work develops a universal approach able to deal with this increasing variety of multimode optical systems. The enabling key concept is the observation that supermodes must be, in general, considered as dynamic function of a continuous parameter connected to the space or the time and frequency degrees of freedom. The image of a

continuous transformation of supermode shape suggests us to call them "morphing supermodes". This theoretical work explores and characterizes the temporal and spectral properties as well as the quantum properties of these new powerful objects. We observe that the notion of continuously evolving supermodes is unexplored by traditional theoretical approaches, which are, in general, applied to systems under stringent a priori hypotheses, such as the absence of linear and/or nonlinear dispersion phenomena, preventing observation of these features [10].

We focus here on a generic below-threshold resonant system that can present linear and nonlinear dispersion. Nevertheless, our approach covers any multimode system evolving under the most general quadratic Hamiltonian, including when obtained from a perturbative development. It can treat also single pass configurations [21,22] for which, in general, the supermode structure is studied at the output end of the nonlinear crystal and no attention is paid to spatial propagation effects. Our approach sheds light on the problem of adequate detection choices in the experimental measurement of multimode quantum features. Moreover, in general, it has a major impact on the investigation of multiple scenarios: these encompass low-dimensional systems, such as single- or double-mode squeezing in detuned devices [23-25] and in optomechanical cavities [26,27] or spatial entanglement in waveguide arrays [16], and highly multimode devices, such as those used for the generation of squeezed light via four-wave mixing in integrated systems on silicon photonics [19,28], as well as problems related to condensed matter [29,30].

Multimode Langevin equations.-We consider the most general time-independent quadratic Hamiltonian describing the dynamics of  $N$  boson modes  $\hat{a}_n$  in the interaction picture

$$
H = \hbar \sum_ {m, n} G _ {m, n} a _ {m} ^ {\dagger} a _ {n} + \frac {\hbar}{2} \sum_ {m, n} \left[ F _ {m, n} a _ {m} ^ {\dagger} a _ {n} ^ {\dagger} + \mathrm {H . c .} \right]. \tag {1}
$$

In this expression, the matrix  $F$  is a complex symmetric matrix  $F = F^T$ , while  $G$  is a Hermitian complex matrix, verifying  $G = G^\dagger$  [31]. Boson operators  $a_n$  and  $a_n^\dagger$  satisfy the commutation relations  $[a_n, a_m^\dagger] = \delta_{n,m}$  and  $[a_n, a_m] = 0$ . In practical situations, the matrix  $F$  is of the same kind as the one describing spontaneous parametric down-conversion in  $\chi^{(2)}$  or  $\chi^{(3)}$  interactions, under the approximation of undepleted pumps [10,32]. The very general shape of the matrix  $G$  allows taking into account frequency conversion processes [21], self- and cross-phase-modulation in  $\chi^{(3)}$  media [32], and, in resonant systems, it can also include the mode detunings from perfect resonance and linear dispersion effects.

For a cavity-based system, boson operators  $\hat{a}_n$  and  $\hat{a}_n^\dagger$  label the intracavity modes. In the Heisenberg representation, the Hamiltonian operator  $H$  permits one to derive a set of linear coupled quantum Langevin equations describing the dynamics of the system observables below the oscillation threshold. In terms of amplitude and phase quadratures,  $x_{n} = (1 / \sqrt{2})(a_{n}^{\dagger} + a_{n})$  and  $y_{n} = (\mathrm{i} / \sqrt{2})(a_{n}^{\dagger} - a_{n})$ , Langevin equations read, in a compact matrix form

$$
\frac {d \boldsymbol {R} (t)}{d t} = (- \Gamma + \mathcal {M}) \boldsymbol {R} (t) + \sqrt {2 \Gamma} \boldsymbol {R} _ {\text {i n}} (t). \tag {2}
$$

In the previous expression,  $\pmb{R}(t) = (x_1(t),\dots,x_N(t)|y_1(t),\dots,y_N(t))^T$  is a column vector of quadrature operators,  $\Gamma = \mathrm{diag}\{\gamma_1,\dots,\gamma_N|\gamma_1,\dots,\gamma_N\}$  is a diagonal matrix containing the mode-dependent cavity dampings.  $\pmb{R}_{\mathrm{in}}(t)$  is the quadrature vector of input modes entering the system via losses. We stress that the quadratures of the cavity output fields  $\pmb{R}_{\mathrm{out}}(t)$  can be straightforwardly obtained with the input-output relations  $\pmb{R}_{\mathrm{in}}(t) + \pmb{R}_{\mathrm{out}}(t) = \sqrt{2\Gamma}\pmb{R}(t)$  [33]. The mode interaction matrix  $\mathcal{M} \in \mathbb{R}^{2N\times 2N}$  explicitly depends on the matrices  $F$  and  $G$  that appear in the Hamiltonian operator (1) via the relation

$$
\mathcal {M} = \left( \begin{array}{c c} \operatorname {I m} [ G + F ] & \operatorname {R e} [ G - F ] \\ \hline - \operatorname {R e} [ G + F ] & - \operatorname {I m} [ G + F ] ^ {T} \end{array} \right), \tag {3}
$$

where matrices  $\operatorname{Re}[G - F]$  and  $\operatorname{Re}[G + F]$  are both symmetric. We note that the system threshold is defined by the eigenvalue  $\lambda_0$  of  $\mathcal{M} - \Gamma$  with the highest real part for which  $\operatorname{Re}[\lambda_0] = 0$ .

Finding the system supermodes corresponds to identifying the linear combinations of the original  $a_{n}$  and  $a_{n}^{\dagger}$  that permit one to diagonalize  $\mathcal{M}$ , so as to uncouple the evolution equations, while preserving the symplectic structure of the problem [9,10]. However, in general,  $\mathcal{M}$  cannot be diagonalized by symplectic unitary transformations apart from special cases for which the matrix  $G$  is null [34]. As a

consequence, the system does not admit, in general, a set of supermodes in the traditional sense that do not change their shape during the system evolution. We show that the problem of the characterization of its quantum properties in terms of statistically independent physical observables can be achieved in terms of morphing supermodes, provided we adopt a novel approach. As a matter of fact, besides low-dimension systems whose equations can be solved directly [35], the traditional analysis of resonant systems is confined to those presenting  $\chi^{(2)}$  nonlinearities and mode-independent detuning [36]. These limitations arise from the fact that standard symplectic diagonalization methods, such as Bloch-Messiah decomposition (BMD) [37,38], limit their analysis to problems for which dynamic evolution can be disregarded. Conversely, in a general situation, as we are analyzing, pertinent transformations are matrix-valued functions of space, frequency or time and demand an adequate extension of symplectic approach.

Generalized symplectic approach.-As a first step, we show that, even in the most general case considered here, the transformation associated with Eqs. (2) and connecting the input and output modes is indeed symplectic in a more general sense. By doing so, we can then apply to it a generalized version of BMD.

Steady-state solutions of Eqs. (2) can be obtained in the frequency domain by application of the Fourier transform to the slowly varying envelopes [33]

$$
\boldsymbol {R} (\omega) = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {+ \infty} e ^ {- i \omega t} \boldsymbol {R} (t) d t. \tag {4}
$$

The quadratures of the output modes read as

$$
\boldsymbol {R} _ {\text {o u t}} (\omega) = S (\omega) \boldsymbol {R} _ {\text {i n}} (\omega), \tag {5}
$$

where  $S(\omega)$  is the transfer function of the linear system (2)

$$
S (\omega) = \sqrt {2 \Gamma} (i \omega \mathbb {I} + \Gamma - \mathcal {M}) ^ {- 1} \sqrt {2 \Gamma} - \mathbb {I}, \tag {6}
$$

where  $\mathbb{I}$  is the identity matrix of  $\mathbb{R}^{2N\times 2N}$ . This is a complex matrix-valued function, verifying  $S(-\omega) = S^{*}(\omega)$ , which assures the reality of  $S$  in the time domain. In matrix form, the commutators of input mode quadratures can be written as  $[R_{\mathrm{in}}(\omega), R_{\mathrm{in}}^T(\omega')] = \Omega \delta(\omega + \omega')$ , where  $\Omega = \begin{pmatrix} 0 & I \\ -I & 0 \end{pmatrix}$ , is the  $N$ -mode "symplectic form" and  $I$  is the identity matrix of  $\mathbb{R}^{N\times N}$  [38]. In order to guarantee that the commutators are preserved for  $R_{\mathrm{out}}(\omega)$ , the transformation  $S(\omega)$  must verify

$$
\forall \omega \in \mathbb {R} \colon S (\omega) \Omega S ^ {T} (- \omega) = \Omega . \tag {7}
$$

In the case we are dealing with, this condition is easily verified (see the Supplemental Material [39]) by noticing that the matrix  $\mathcal{M}$  of Eq. (3) is a Hamiltonian matrix, i.e., it

verifies the relation  $(\Omega \mathcal{M})^T = \Omega \mathcal{M}$  and that the matrix  $\Gamma$  is skew Hamiltonian  $(\Omega \Gamma)^T = -\Omega \Gamma$ . Expression (7) extends the standard symplecticity condition known in the literature [38]. More precisely, it defines a set of transformations that depend on a real continuous parameter—the frequency  $\omega$ —and such that every matrix obtained from  $S(\omega)$  with  $\omega$  assigned belongs to the "conjugate symplectic group"  $Sp^{*}(2N,\mathbb{C})$  [40],

$$
\mathbb {S} _ {\omega} = \left\{S (\omega) \in \mathcal {C} _ {\omega} \mid \forall \omega \in \mathbb {R}, S (\omega) \in S p ^ {*} (2 N, \mathbb {C}) \right\}, \tag {8}
$$

where  $\mathcal{C}_{\omega}$  is the set of matrix-valued functions in  $\mathbb{C}^{2N\times 2N}$  that are smooth with respect to  $\omega$ . For the sake of simplicity, we will refer to transformations belonging to  $\mathbb{S}_{\omega}$  as “ $\omega$  symplectic.”

In a general way,  $\omega$  symplectic transformations admit a decomposition that is a smooth function of the real parameter, as expected to describe the mode continuous evolution in time and frequency. In other words, for any element of  $\mathbb{S}_{\omega}$ , there exists an analytical Bloch-Messiah decomposition (ABMD) (see Supplemental Material [39])

$$
S (\omega) = U (\omega) D (\omega) V ^ {\dagger} (\omega), \tag {9}
$$

where  $U(\omega), D(\omega)$ , and  $V(\omega)$  are smooth matrix-valued functions such that, for any assigned value of  $\omega$ ,  $U(\omega), V(\omega) \in Sp^{*}(2N, \mathbb{C}) \cap \mathcal{U}(2N)$ , with  $\mathcal{U}(2N)$  the unitary group. The matrix  $D(\omega) = \mathrm{diag}\{d_{1}(\omega), \ldots, d_{N}(\omega)|d_{1}^{-1}(\omega), \ldots, d_{N}^{-1}(\omega)\}$  with  $d_{m}(\omega) \geq 1$  for  $m = \{1, \ldots, N\}$ , for all  $\omega \in \mathbb{R}$ . We note that these matrix-valued functions can be chosen, after conjugating Eq. (9), so to verify the same property as  $S^{*}(\omega) = S(-\omega)$ .

Expression (9) shows that a BMD for  $S(\omega)$ , in the case of a generic quadratic Hamiltonian, exists and depends on a continuous parameter. From it, the quadrature of supermodes of system (2) can be obtained as  $R_{\mathrm{out}}'(\omega) = U^{\dagger}(\omega)R_{\mathrm{out}}(\omega)$ , where we have assumed input vacuum state. We remark that the shape of the supermodes themselves depends on the continuous parameter: this result shows that, in practical situations, the optimal detection modes change with the analysis frequency  $\omega$ . The connection with Bogoliubov transformations [41,42] is discussed in the Supplemental Material [39].

To conclude, we note that Eqs. (7) and (9) have counterparts in the time domain. The matrix-valued Green's function  $S(t)$  of (2), corresponding to the inverse Fourier transform of  $S(\omega)$ , is symplectic in the sense that  $\forall t, t' \in \mathbb{R}$ ,

$$
\int_ {- \infty} ^ {+ \infty} S (t - \tau) \Omega S ^ {T} \left(t ^ {\prime} - \tau\right) d \tau = \Omega \delta \left(t - t ^ {\prime}\right), \tag {10}
$$

and its ABMD reads

$$
S (t) = \int_ {- \infty} ^ {+ \infty} U (\tau) D \left(t - \tau + \tau^ {\prime}\right) V \left(\tau^ {\prime}\right) d \tau d \tau^ {\prime}, \tag {11}
$$

where  $U(t)$  and  $V(t)$  are real matrix-valued Green's functions. They are symplectic in the sense of (10) and orthogonal in the sense  $(U\star U^{T})(t) = \mathbb{I}\delta (t)$  and  $(V\star V^{T})(t) = \mathbb{I}\delta (t)$ , with  $\star$  as the cross-correlation product. The Green's function  $D(t)$  is the diagonal matrix-valued obtained as the inverse Fourier transform of  $D(\omega)$ . It is real and even, since  $D(\omega)$  is real and even.

Spectrum of quantum noise.-We now characterize the quantum statistical properties of the output steady states  $\pmb{R}_{\mathrm{out}}$  and of their supermodes  $\pmb{R}_{\mathrm{out}}^{\prime}$ . To this purpose, we consider a generic linear combination  $Z_{\theta}$  of  $\pmb{R}_{\mathrm{out}}$  specified by the normalized line vector  $Q(\pmb{\theta})$  consisting of real coefficients

$$
Z _ {\boldsymbol {\theta}} = \boldsymbol {Q} (\boldsymbol {\theta}) \boldsymbol {R} _ {\text {o u t}}, \tag {12}
$$

where  $\pmb{\theta}$  are the  $2N - 1$  angles parametrizing  $\mathbf{Q}(\pmb {\theta})$

The spectrum of quantum noise can be expressed by means of the Wiener-Khinchin theorem in terms of the self-correlation of  $Z_{\theta}$  as

$$
\Sigma_ {\boldsymbol {\theta}} (\omega) = \int_ {- \infty} ^ {+ \infty} e ^ {- i \omega \tau} \left\langle Z _ {\boldsymbol {\theta}} (t + \tau) Z _ {\boldsymbol {\theta}} (t) \right\rangle d \tau . \tag {13}
$$

By making use of expression (12) in the frequency domain, Eq. (13) can be written as

$$
\Sigma_ {\boldsymbol {\theta}} (\omega) = \boldsymbol {Q} (\boldsymbol {\theta}) \sigma_ {\text {o u t}} (\omega) \boldsymbol {Q} (\boldsymbol {\theta}) ^ {T}, \tag {14}
$$

where

$$
\sigma_ {\text {o u t}} (\omega) = \frac {1}{2 \sqrt {2 \pi}} S (\omega) S ^ {T} (- \omega) \tag {15}
$$

is the Fourier transform of the covariance matrix of the output state  $\sigma_{\mathrm{out}}(\tau) = \frac{1}{2}\langle R_{\mathrm{out}}(0)R_{\mathrm{out}}^T (\tau) + (R_{\mathrm{out}}(\tau)R_{\mathrm{out}}^T (0))^T\rangle$  , which depends only on time differences  $\pmb{\tau}$  , as we are considering a stationary regime [43]. In Eq. (15), we used (5) and the fact that for vacuum input state  $\sigma_{\mathrm{in}}(\tau) = (\mathbb{I} / 2)\delta (\tau)$

Equation (15) can be rewritten by making use of the ABMD in Eq. (9). We obtain

$$
\sigma_ {\text {o u t}} (\omega) = \frac {1}{2 \sqrt {2 \pi}} U (\omega) D ^ {2} (\omega) U ^ {\dagger} (\omega). \tag {16}
$$

By replacing (16) into (14) it is clear that, in general, optimal squeezing (respectively, antisqueezing) cannot be reached by any linear combination  $Q(\pmb{\theta})$  apart from those cases in which  $U(\omega)$  is real. In this case, optimality could be reached only at a given value of  $\omega$ , by choosing  $Q(\pmb{\theta})$  equal to one column of  $U^{\dagger}(\omega)$ , as we will show in the next

section. In experiments, the supermodes properties, and in turn their squeezing features, can be obtained by replacing  $Q(\pmb{\theta})$  by a complex line vector-valued function  $\pmb{Q}(\pmb{\theta}(\omega))$  equal to the  $i$ th column of  $U^{\dagger}(\omega)$ . With this choice,

$$
\Sigma_ {\boldsymbol {\theta}} (\omega) = \frac {1}{2 \sqrt {2 \pi}} d _ {i} ^ {2} (\omega). \tag {17}
$$

Based on this expression, the elements of the diagonal matrix  $D^{2}(\omega)$  give directly the variances of supermodes quadratures and they can be interpreted as their antisqueezing  $\{d_1(\omega),\dots,d_N(\omega)\}$  and squeezing levels  $\{d_1^{-1}(\omega),\dots,d_N^{-1}(\omega)\}$ . We note that assigning  $Q(\pmb{\theta}(\omega))$  corresponds to designate a particular shape of the local oscillator (LO) of a homodyne detection scheme. As a consequence, in order to retrieve the optimal information on supermodes, the LO itself must depend on  $\omega$  and be chosen according to the analyzing frequency. The shaping of the LO could be implemented, for example, by a passive interferometer with memory effect.

Single-mode squeezing in detuned optical cavity.-The case of a single-mode squeezed state generated in a detuned optical parametric oscillator (OPO) is already illustrative of the relevance of a continuous-parameter symplectic approach. In this case, the vector of field quadratures is  $\pmb{R} = (x,y)^T$  and the matrix  $\mathcal{M}$  associated with this system is

$$
\mathcal {M} = \left( \begin{array}{c c} g & \Delta \\ - \Delta & - g \end{array} \right), \tag {18}
$$

where  $g$  accounts for the parametric gain and  $\Delta$  is the detuning from cavity resonance of the squeezed mode.

The system has two singular values  $d_{1}(\omega)$  and  $d_{1}^{-1}(\omega)$  and, associated with these, two supermodes. As the supermode quadratures are found to have real coefficients, we can write them as  $R_{\mathrm{out},i}' = \cos [\theta_i(\omega)]x_{\mathrm{out}} + \sin [\theta_i(\omega)]y_{\mathrm{out}}$  with  $i = 1,2$ . The quadrature angles are frequency dependent and verify  $\theta_2(\omega) = \theta_1(\omega) + \pi /2$ . At  $\omega = 0$ ,  $\theta_{1}(0) = \arctan [(g_{1} + \sqrt{g_{2}g_{3}}) / 2\Delta \gamma]$ , where  $g_{1} = g^{2} - \Delta^{2} + \gamma^{2}$ ,  $g_{2} = (g - \Delta)^{2} + \gamma^{2}$ , and  $g_{3} = (g + \Delta)^{2} + \gamma^{2}$ . In Fig. 1 (top), we trace  $d_{1}^{2}(\omega)$  (solid) and  $d_{1}^{-2}(\omega)$  (dashed), as functions of the analysis frequency  $\omega$  and we compare them to the standard quantum limit (SQL). The figure also shows (in gray) normalized-to-SQL spectra  $\Sigma_{\theta}$  of field quadratures,  $Z_{\theta} = \cos \theta x_{\mathrm{out}} + \sin \theta y_{\mathrm{out}}$ , calculated for several values of the angle  $\theta$ , with  $\theta$  frequency independent. These quadratures are obtained by imposing in Eq. (12) a real and constant  $Q(\pmb{\theta})$ . Regardless the choice of  $\theta$ , the curves  $\Sigma_{\theta}$  exhibit a (local or asymptotic) minimum but do not reach the optimal squeezing for all values of  $\omega$ . Conversely, the function  $d_{1}^{-2}(\omega)$  corresponds the envelope of  $\Sigma_{\theta}$  minima, thus confirming that the optimal squeezing spectrum is the one computed for the morphing supermodes. A similar observation holds for the antisqueezing  $d_{1}^{2}(\omega)$ .

![](images/e91bf98f360555dc735f43fe6c3ffbdc44ad0eed44ebaec64caffb12ee711da9.jpg)  
FIG. 1. Top: frequency-dependent singular values  $d_1^2(\omega)$  and  $d_1^{-2}(\omega)$ . They quantify the degree of antisqueezing (dashed black) and squeezing (solid black), respectively. Solid gray curves represent the normalized-to-SQL spectrum of quantum noise  $\Sigma_{\theta}$  of quadratures  $Z_{\theta}$  for several values of  $\theta$ , in agreement with the existing literature on detuned single-mode OPO [23-25]. Bottom: color density plot represents  $\Sigma_{\theta}$  with respect to analysis frequency  $\omega$  and quadrature angle  $\theta$ . Dashed and solid black lines represent the frequency-dependent angles  $\theta_i(\omega)$  associated with supermodes  $R_{\mathrm{out},i}'$ . They represent the set of points in the space  $(\omega, \theta)$  for which  $\Sigma_{\theta}$  is minimum (squeezing) or maximum (antisqueezing).

Figure 1 (bottom) shows the angles  $\theta_{1}(\omega)$  and  $\theta_{2}(\omega)$  that give the supermode coefficients. The color code indicates quadrature noise levels normalized to SQL as functions of  $\omega$  and of the quadrature angle  $\theta$ . As expected, when  $\omega$  changes, the frequency dependent angles  $\theta_{1}(\omega)$  and  $\theta_{2}(\omega)$  associated with supermodes correctly give the superpositions of  $x_{\mathrm{out}}$  and  $y_{\mathrm{out}}$  that lead to optimal antisqueezing and squeezing levels. We note that the dependence of the optimal quadrature angle with respect to analysis frequency is in agreement with the result obtained by directly solving the one-dimension Langevin equations, either in detuned OPO [23-25] or optomechanical cavities [26,27].

Four-mode system.-To conclude, we discuss a case that is complex enough to demonstrate the efficacy of the generalized symplectic approach and the ABMD. We chose a multimode system with  $N = 4$  in the case of both  $F$  and  $G$  non-null. The structure of these two matrices is chosen as

$$
F = \left( \begin{array}{c c} \tilde {F} & 2 \tilde {F} \\ \hline 2 \tilde {F} & \tilde {F} \end{array} \right), \quad G = \left( \begin{array}{c c} 2 \tilde {G} & \tilde {G} \\ \hline \tilde {G} & 2 \tilde {G} \end{array} \right), \tag {19}
$$

![](images/c7288a3a4cf6bb3023c9a58fb43d231d21f656e2671b87ef6f0e1c1c52a66202.jpg)  
FIG. 2. Top: frequency-dependent singular values  $d_{i}(\omega)$  and  $d_{i}^{-2}(\omega)$ , for  $i = 1, \dots, 4$ , quantifying the degree of antisqueezing (dashed) and squeezing (solid) of corresponding supermode. Level of noise equal to one corresponds to SQL. Bottom: frequency-dependent (real) coefficients  $U_{3,j}(\omega)$  of one ( $i = 3$ ) of the eight supermodes obtained from ABMD.

with  $\tilde{F} = \left( \begin{array}{cc}0 & a\\ a & 0 \end{array} \right)$  and  $\tilde{G} = \left( \begin{array}{cc}b & 0\\ 0 & b \end{array} \right)$ . This scenario is, for instance, the one of a  $\chi^{(3)}$  process driven by two strong pumps that give origin to both parametric and frequency conversions, including self- and cross-phase-modulation of signal and idler waves. For this system, the ABMD gives eight singular values and eight supermodes that are smooth with respect to  $\omega$ . In Fig. 2 (top), we trace the frequency-dependent singular values that, for this specific case, are two by two degenerate. The solid lines represent the square of  $d_{i}(\omega)$  [respectively,  $d_{i}^{-1}(\omega)$ ] for  $i = 1,\ldots ,4$  and they are compared to SQL. They correctly provide the minimum (respectively, maximum) degree of squeezing (respectively, antisqueezing) produced by the system at a given value of the analysis frequency  $\omega$ . In Fig. 2 (bottom), we represent the eight frequency-dependent coefficients of one of the supermodes ( $i = 3$ ).

Conclusions.-In this Letter, we illustrated that morphing supermodes naturally emerge from the dynamics of multimode systems in the most general case of quadratic Hamiltonians without a priori hypotheses. In order to fully characterize their dynamical and quantum properties, we developed a universal symplectic approach. The presented strategy allows for covering the analysis of many optical systems that are relevant for quantum technologies but that cannot be easily analyzed by standard symplectic diagonalizations. We introduced the analytical Bloch-Messiah decomposition that allows treating symplectic transformations that depend on a continuous parameter, such as the

frequency  $\omega$ . As a result of the decomposition, supermodes and their associated singular values are, in the most general case, dependent on the continuous parameter. Our approach will allow treating easily systems with a very large number of degrees of freedom, hence enabling a better harvesting and control of their quantum properties. This feature is of crucial importance for application in the domain of quantum technologies with a major impact in the development of bulk and integrated quantum optics.

We acknowledge L. Dieci and L. Lopez for useful discussions about analytical decompositions and C. Navarrete-Benlloch for useful discussions about the spectral covariance matrix. This work has been conducted within the framework of the project HyLight (ANR-17-CE30-0006-01) granted by the Agence Nationale de la Recherche (ANR). The authors also acknowledge financial support from the French government through its program Investments for the Future under the Université Côte d'Azur UCA-JEDI project (under the label Quantum@UCA) managed by the ANR (Grant No. ANR-15-IDEX-01).

giuseppe.patera@univ-lille.fr  
[1] C. Weedbrook, S. Pirandola, R. García-Patron, N. J. Cerf, T. C. Ralph, J. H. Shapiro, and S. Lloyd, Gaussian quantum information, Rev. Mod. Phys. 84, 621 (2012).  
[2] A. Ferraro, S. Olivares, and M. G. A. Paris, Gaussian States in Quantum Information, Napoli Series on Physics and Astrophysics, No. 8 (Bibliopolis, Naples, 2005).  
[3] V. Giovannetti, S. Lloyd, and L. Maccone, Quantum-enhanced measurements: Beating the standard quantum limit, Science 306, 1330 (2004).  
[4] S. L. Braunstein and P. van Loock, Quantum information with continuous variables, Rev. Mod. Phys. 77, 513 (2005).  
[5] J. Zhang and S. L. Braunstein, Continuous-variable Gaussian analog of cluster states, Phys. Rev. A 73, 032318 (2006).  
[6] N. C. Menicucci, P. van Loock, M. Gu, C. Weedbrook, T. C. Ralph, and M. A. Nielsen, Universal Quantum Computation with Continuous-Variable Cluster States, Phys. Rev. Lett. 97, 110501 (2006).  
[7] J.-i. Yoshikawa, S. Yokoyama, T. Kaji, C. Sornphiphatphong, Y. Shiozawa, K. Makino, and A. Furusawa, Generation of one-million-mode continuous-variable cluster state by unlimited time-domain multiplexing, APL Photonics 1, 060801 (2016).  
[8] W. Wasilewski, A.I. Lvovsky, K. Banaszek, and C. Radzewicz, Pulsed squeezed light: Simultaneous squeezing of multiple modes, Phys. Rev. A 73, 063819 (2006).  
[9] G.J. de Valcárcel, G. Patera, N. Treps, and C. Fabre, Multimode squeezing of frequency combs, Phys. Rev. A 74, 061801(R) (2006).  
[10] G. Patera, N. Treps, C. Fabre, and G. J. De Valcárcel, Quantum theory of Synchronously Pumped type I Optical Parametric Oscillators: Characterization of the squeezed supermodes, Eur. Phys. J. D 56, 123 (2010).

[11] S. L. Braunstein, Squeezing as an irreducible resource, Phys. Rev. A 71, 055801 (2005).  
[12] R. S. Bennink and R. W. Boyd, Improved measurement of multimode squeezed light via an eigenmode approach, Phys. Rev. A 66, 053815 (2002).  
[13] N. C. Menicucci, S. T. Flammia, H. Zaidi, and O. Pfister, Ultracompact generation of continuous-variable cluster states, Phys. Rev. A 76, 010302(R) (2007).  
[14] G. Patera, C. Navarrete-Benlloch, G. J. de Valcarcel, and C. Fabre, Quantum coherent control of highly multipartite continuous-variable entangled states by tailoring parametric interactions, Eur. Phys. J. D 66, 241 (2012).  
[15] J. Roslund, R. M. de Araujo, S. Jiang, C. Fabre, and N. Treps, Wavelength-multiplexed quantum networks with ultrafast frequency combs, Nat. Photonics 8, 109 (2014).  
[16] D. Barral, M. Walschaers, K. Bencheikh, V. Parigi, J. A. Levenson, N. Treps, and N. Belabas, A versatile photonic entanglement synthesizer in the spatial domain, arXiv:1912.11154.  
[17] G. Ferrini, J. Roslund, F. Arzani, Y. Cai, C. Fabre, and N. Treps, Optimization of networks for measurement-based quantum computation, Phys. Rev. A 91, 032314 (2015).  
[18] J. Nokkala, F. Arzani, F. Galve, R. Zambrini, S. Maniscalco, J. Piilo, N. Treps, and V. Parigi, Reconfigurable optical implementation of quantum complex networks, New J. Phys. 20, 053024 (2018).  
[19] M. Kues, C. Reimer, P. Roztocki, L. R. Cortes, S. Sciara, B. Wetzel, Y. Zhang, A. Cino, S. T. Chu, B. E. Little, D. J. Moss, L. Caspani, J. Azana, and R. Morandotti, On-chip generation of high-dimensional entangled quantum states and their coherent control, Nature (London) 546, 622 (2017).  
[20] L. Helt and N. Quesada, Degenerate squeezing in waveguides: A unified theoretical approach, J. Phys. Photonics 2, 035001 (2020).  
[21] A. Christ, B. Brecht, W. Mauerer, and C. Silberhorn, Theory of quantum frequency conversion and type-  $\{\mathrm{II}\}$  parametric down-conversion in the high-gain regime, New J. Phys. 15, 053038 (2013).  
[22] T. Lipfert, D. B. Horoshko, G. Patera, and M. I. Kolobov, Bloch-Messiah decomposition and Magnus expansion for parametric down-conversion with monochromatic pump, Phys. Rev. A 98, 013815 (2018).  
[23] C. Fabre, É. Giacobino, A. Heidmann, and S. Reynaud, Noise characteristics of a non-degenerate Optical Parametric Oscillator - Application to quantum noise reduction, J. Phys. 50, 1209 (1989).  
[24] C. Fabre, É. Giacobino, A. Heidmann, L. Lugiato, S. Reynaud, M. Vadacchino, and W. Kaige, Squeezing in detuned degenerate optical parametric oscillators, Quantum Opt. 2, 159 (1990).  
[25] A. Porzio, C. Altucci, P. Aniello, C. de Lisio, and S. Solimeno, Resonances and spectral properties of detuned {OPOs} pumped by fluctuating sources, Appl. Phys. B 75, 655 (2002).  
[26] C. Fabre, M. Pinard, S. Bourzeix, A. Heidmann, É. Giacobino, and S. Reynaud, Quantum-noise reduction using a cavity with a movable mirror, Phys. Rev. A 49, 1337 (1994).

[27] S. Mancini and P. Tombesi, Quantum noise reduction by radiation pressure, Phys. Rev. A 49, 4055 (1994).  
[28] Z. Vernon, N. Quesada, M. Liscidini, B. Morrison, M. Menotti, K. C. Tan, and J. E. Sipe, Scalable Squeezed-Light Source for Continuous-Variable Quantum Sampling, Phys. Rev. Applied 12, 064024 (2019).  
[29] P.-G. De Gennes, Superconductivity of Metals and Alloys, 1st ed. (CRC Press, Boca Raton, FL, 2018).  
[30] I. Bloch, J. Dalibard, and W. Zwerger, Many-body physics with ultracold gases, Rev. Mod. Phys. 80, 885 (2008).  
[31] We are using the following notation:  $[\cdot ]^T$  for the transpose,  $[\cdot ]^{*}$  for the complex conjugate, and  $[\cdot ]^{\dagger}$  for the Hermitian transpose.  
[32] Y.K. Chembo, Quantum dynamics of Kerr optical frequency combs below and above threshold: Spontaneous four-wave mixing, entanglement, and squeezed states of light, Phys. Rev. A 93, 033820 (2016).  
[33] C.W. Gardiner and P. Zoller, Quantum Noise, 3rd ed., Springer Series in Synergetics (Springer, New York, 2004).  
[34] The problem can be greatly simplified in some special cases for which  $\mathcal{M}$  could be block diagonalized or put into a canonical Jordan form via symplectic and unitary matrices.  
[35] V.D. Vaidya, B. Morrison, L.G. Helt, R. Shahrokhshahi, D.H. Mahler, M.J. Collins, K.Y. Tan, J. Lavoie, A. Repingon, M. Menotti, N. Quesada, R.C. Pooser, A.E. Lita, T. Gerrits, S.W. Nam, and Z. Vernon, Broadband quadrature-squeezed vacuum and nonclassical photon number correlations from a nanophotonic device, arXiv: 1904.07833.  
[36] S. Jiang, N. Treps, and C. Fabre, A time/frequency quantum analysis of the light generated by synchronously pumped optical parametric oscillators, New J. Phys. 14, 043006 (2012).  
[37] Arvind, B. Dutta, N. Mukunda, and R. Simon, The real symplectic groups in quantum mechanics and optics, *Pramana* 45, 471 (1995).  
[38] G. Adesso, S. Ragy, and A. R. Lee, Continuous variable quantum information: gaussian states and beyond, Open Syst. Inf. Dyn. 21, 1440001 (2014).  
[39] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.125.103601 for the proof of the  $\omega$  simplicity of  $S(\omega)$  (first section), a discussion about connections with Bogoliubov canonical transformations (second section) and the proof of the existence of the analytical Bloch-Messiah decomposition for an  $\omega$  symplectic transformation (third section).  
[40] D. S. Mackey, N. Mackey, and F. Tisseur, Structured tools for structured matrices, Electron. J. Linear Algebra 10, 106 (2003).  
[41] N. N. Bogoliubov, On the theory of superfluidity, J. Phys. 11, 23 (1947).  
[42] J.-P. Blaizot and G. Ripka, Quantum Theory of Finite Systems (MIT Press, Cambridge, MA, 1986).  
[43] M. I. Kolobov and G. Patera, Spatiotemporal multipartite entanglement, Phys. Rev. A 83, 050302(R) (2011).