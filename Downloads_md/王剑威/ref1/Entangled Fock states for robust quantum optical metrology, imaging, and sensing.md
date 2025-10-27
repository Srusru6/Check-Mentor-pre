# Entangled Fock states for robust quantum optical metrology, imaging, and sensing

Sean D. Haver, * Christoph F. Wildfeuer, and Jonathan P. Dowling  
Hearne Institute for Theoretical Physics, Department of Physics and Astronomy, Louisiana State University, Baton Rouge, Louisiana 70803, USA

(Received 6 May 2008; revised manuscript received 17 November 2008; published 17 December 2008)

We propose a class of path-entangled photon Fock states for robust quantum optical metrology, imaging, and sensing in the presence of loss. We model propagation loss with beam splitters and derive a reduced density-matrix formalism from which we examine how photon loss affects coherence. It is shown that particular entangled number states, which contain a special superposition of photons in both arms of a Mach-Zehnder interferometer, are resilient to environmental decoherence. We demonstrate an order of magnitude greater visibility with loss than possible with path-entangled  $|N,0\rangle +|0,N\rangle$  states. We also show that the effectiveness of a detection scheme is related to super-resolution visibility.

DOI: 10.1103/PhysRevA.78.063828

PACS number(s): 42.50.Dv, 03.65.Ud, 03.67.Bg, 42.50.Lc

# I. INTRODUCTION

Quantum states of light, such as squeezed states or entangled states, can be used for metrology, image production, and object ranging, with greater precision, resolution, and sensitivity than what is possible classically [1-4]. In 2000, one of the authors introduced a path-entangled number state  $|N,0\rangle +|0,N\rangle$ , known as the  $N00N$  state, which is an entangled two-mode state that has either all  $N$  photons in one path  $a$  of a Mach-Zehnder interferometer or the other path  $b$ . The state may be written as  $|N\because 0\rangle_{a,b} = (|N,0\rangle_{a,b} + |0,N\rangle_{a,b}) / \sqrt{2}$ . With this state, one can achieve superresolution as well as Heisenberg-limited supersensitivity in interferometry and imaging [5,6], where supersensitivity is defined as the ability of a particular quantum system to perform better than the shot-noise limit, and super-resolution as performing better than the Rayleigh diffraction limit. The super-resolution effect was demonstrated for  $N = 2$  in a proof-of-principle experiment by Shih in 2001 [7]. In 2004, the Steinberg group demonstrated super-resolution for  $N = 3$ , and the Zeilinger group did so for  $N = 4$  [8-10]. Finally, in 2007 a joint Japanese-British collaboration demonstrated both super-resolution and sensitivity in a single  $N = 4$  experiment [11]. A large amount of publications also investigated alternative states and detection schemes to obtain supersensitivity and super-resolution.  $N00N$  states served for many years as a standard model for the newly emerging fields of quantum optical metrology, imaging, and sensing. Consequently, a few authors investigated the effects of loss on the performance of quantum interferometers with  $N00N$  states. It turns out that  $N00N$  states undergoing loss decohere very rapidly, making it difficult to achieve supersensitivity and resolution in an environment with loss [12-14].

In this paper, we address how environmental interaction brings about decoherence for a more generalized state with photons in both modes, and we have discovered a class of states that improve drastically on the performance of  $N00N$  states when loss is present. We find with these new states that while minimum sensitivity is decreased slightly, robustness against decoherence is increased greatly.

For practical purposes, phase sensitivity is typically obtained by the linear error propagation method (see, however, Ref. [6]), where  $\hat{O}$  represents the operator for the detection scheme being used,

$$
\delta \phi = \frac {\Delta \hat {O}}{\left| \partial \langle \hat {O} \rangle / \partial \phi \right|}, \tag {1}
$$

and  $\Delta \hat{O}_N = \sqrt{\langle\hat{O}^2\rangle - \langle\hat{O}\rangle^2}$ . Equation (1), for a  $N00N$  state with no loss, and a detection operator  $\hat{A}_N = |0,N\rangle \langle N,0| + |N,0\rangle \langle 0,N|$ , which can be implemented with coincidence measurements [10], reduces to the Heisenberg limit,  $\delta \phi = 1 / N$ , which is a  $\sqrt{N}$  improvement over the shot-noise limit.

# II. THE INPUT STATE

The state we now wish to examine is the following:

$$
\left| m:: m ^ {\prime} \right\rangle_ {a, b} = \frac {1}{\sqrt {2}} \left(\left| m, m ^ {\prime} \right\rangle_ {a, b} + \left| m ^ {\prime}, m \right\rangle_ {a, b}\right), \tag {2}
$$

where we demand that  $m > m'$ . Such states can be produced, for example, by postselecting on the output of a pair of optical parametric oscillators [15]. Our setup in Fig. 1 is a Mach-Zehnder or an equivalent Michelson interferometer where the details of our source and detection (such as beam splitters, detectors, etc.) are contained in their respective boxes. Here we are concerned primarily with how the state evolves with respect to loss, which is typically modeled by additional beam splitters coupled to the environment [16].

Similar to the approach of Ref. [13], we model loss in the interferometer with fictitious beam splitters, but in our case these are added to both arms of the interferometer. However, we assume unit detection efficiency for the detectors. We develop the photon statistics as a function of beam-splitter transmittance as well as derive a reduced density matrix, which characterizes the propagation losses inside of the interferometer. Loss is represented by photons being reflected into the environment [17]. The beam splitter transforms the modes according to [18]

$$
\hat {a} ^ {\prime} = t _ {a} \hat {a} + r _ {a} ^ {*} \hat {a} _ {v},
$$

![](images/09d06e0cb13004593dfdc46d8fd45152da8c97bbca660b0e9fca5f233363babd.jpg)  
FIG. 1. (Color online) Interferometer with loss modeled by beam splitters in both arms. The reflectance of the beam splitters determines how many photons one lost. An accumulated unknown phase  $\phi$  is obtained due to a path length difference between the arms. The unitary operator for the phase shift is given by  $\hat{U} = \exp (i\hat{b}^{\dagger}\hat{b}\phi)$ . A simple proof shows that this operator commutes with the beam-splitter operation. The placement of the beam splitter before the phase shift has been acquired, therefore, leads to the same result.

$$
\hat {b} ^ {\prime} = t _ {b} \hat {b} + r _ {b} ^ {*} \hat {b} _ {v}, \tag {3}
$$

where  $t_{u} = \sqrt{T_{u}}\exp (i\varphi_{u})$  and  $r_u = \sqrt{R_u}\exp (i\psi_u), u = a,b$  are the complex transmission and reflectance coefficients for modes  $a$  and  $b$ , respectively. The  $|m\because m^{\prime}\rangle$  input state acquires an unknown phase shift  $\phi$ , and the beam-splitter transformations are applied. We then trace over the environmental modes to model the photons lost, and we obtain the reduced density matrix  $\hat{\rho}_{a^{\prime},b^{\prime}} = \mathrm{Tr}_{v_a,v_b}[|\psi \rangle \langle \psi |]$ , which leads to

$$
\begin{array}{l} \hat {\rho} _ {a ^ {\prime}, b ^ {\prime}} = \sum_ {k = 0} ^ {m} \sum_ {l, l ^ {\prime} = 0} ^ {m ^ {\prime}} | a _ {k, l} | ^ {2} | m - k, m ^ {\prime} - l \rangle \langle m - k, m ^ {\prime} - l | \\ + \left| b _ {k, l} \right| ^ {2} \left| m ^ {\prime} - l, m - k \right\rangle \left\langle m ^ {\prime} - l, m - k \right| \\ + a _ {l, l ^ {\prime}} ^ {*} b _ {l ^ {\prime}, l} \left| m ^ {\prime} - l, m - l ^ {\prime} \right\rangle \left\langle m - l, m ^ {\prime} - l ^ {\prime} \right| \\ + a _ {l ^ {\prime}, l} b _ {l, l ^ {\prime}} ^ {*} | m - l ^ {\prime}, m ^ {\prime} - l \rangle \langle m ^ {\prime} - l ^ {\prime}, m - l |. \tag {4} \\ \end{array}
$$

Here the  $a_{k,l}$  and  $b_{k,l}$  coefficients are defined as

$$
\left| a _ {k, l} \right| ^ {2} \equiv \gamma_ {k, l} ^ {2} T _ {a} ^ {m - k} R _ {a} ^ {k} T _ {b} ^ {m ^ {\prime} - l} R _ {b} ^ {l},
$$

$$
\left| b _ {k, l} \right| ^ {2} \equiv \gamma_ {k, l} ^ {2} T _ {a} ^ {m ^ {\prime} - l} R _ {a} ^ {l} T _ {b} ^ {m - k} R _ {b} ^ {k},
$$

$$
\begin{array}{l} a _ {l, l ^ {\prime}} ^ {*} b _ {l ^ {\prime}, l} \equiv \gamma_ {l, l ^ {\prime}} \gamma_ {l ^ {\prime}, l} T _ {a} ^ {(m + m ^ {\prime} - 2 l) / 2} R _ {a} ^ {l} T _ {b} ^ {(m + m ^ {\prime} - 2 l ^ {\prime}) / 2} \\ \times R _ {b} ^ {l ^ {\prime}} e ^ {- i (m - m ^ {\prime}) (\phi + \varphi_ {b} - \varphi_ {a})}, \\ \end{array}
$$

$$
\begin{array}{l} a _ {l ^ {\prime}}, b _ {l, l ^ {\prime}} ^ {*} \equiv \gamma_ {l ^ {\prime}, l} \gamma_ {l, l ^ {\prime}} T _ {a} ^ {(m + m ^ {\prime} - 2 l ^ {\prime}) / 2} R _ {a} ^ {l ^ {\prime}} T _ {b} ^ {(m + m ^ {\prime} - 2 l) / 2} \\ \times R _ {b} ^ {l} e ^ {i (m - m ^ {\prime}) \left(\phi + \varphi_ {b} - \varphi_ {a}\right)}, \tag {5} \\ \end{array}
$$

and

$$
\gamma_ {k, l} \equiv \frac {1}{\sqrt {2 m ! m ^ {\prime} !}} \binom {m} {k} \binom {m ^ {\prime}} {l} [ (m - k)! k! (m ^ {\prime} - l)! l! ] ^ {1 / 2}. \tag {6}
$$

Without loss of generality, we can set the transmission phases of the two beam splitters  $\varphi_{a} = \varphi_{b} = 0$ .

The reduced density matrix in Eq. (4) appears as an incoherent mixture plus interference terms, which survive with loss in either mode up to the limit of  $m'$ . The surviving interference terms all carry amplified phase information in the quantity  $(m - m')\phi$ . Thus the best-case minimum phase sensitivity, under no loss, is reduced from the Heisenberg limit,  $\delta \phi_{N00N} = 1 / N$ , to  $\delta \phi_{m,m'} = 1 / (m - m')$ . Although this sensitivity is less than what  $N00N$  states are capable of achieving (in the absence of loss), the fact that many more interference terms survive than with  $N00N$  states suggests that these states are more robust against photon loss.

# III. OPERATOR SELECTION AND VISIBILITY

To maximize phase information, we choose a detection operator of the form

$$
\begin{array}{l} \hat {A} = \sum_ {r, s = 0} ^ {m ^ {\prime}} | m ^ {\prime} - r, m - s \rangle \langle m - r, m ^ {\prime} - s | \\ + \left| m - r, m ^ {\prime} - s \right\rangle \langle m ^ {\prime} - r, m - s |, \tag {7} \\ \end{array}
$$

which we will show is theoretically optimal. This operator is a more general summation over all possible cases up to  $m'$  photons in either arm than the  $\hat{A}_N$  operator (traditionally used for N00N states [1]). The reduced density matrix for an N00N state is easily obtained by setting  $m = N$  and  $m' = 0$  in Eq. (4). We then obtain for the expectation value of  $\hat{A}_N$

$$
\langle \hat {A} _ {N} \rangle = \operatorname {T r} \left[ \hat {A} _ {N} \hat {\rho} _ {a ^ {\prime}, b ^ {\prime}} \right] = 2 \operatorname {R e} \left(a _ {0, 0} ^ {*} b _ {0, 0}\right) = \left(T _ {a} T _ {b}\right) ^ {N / 2} \cos (N \phi). \tag {8}
$$

The expectation value of the operator  $\hat{A}$  given in Eq. (7) for the  $|m::m^{\prime}\rangle$  state shows the benefit of having many more interference terms compared to the N00N state,

$$
\begin{array}{l} \langle \hat {A} \rangle = \operatorname {T r} [ \hat {A} \hat {\rho} _ {a ^ {\prime}, b ^ {\prime}} ] = 2 \operatorname {R e} \left(\sum_ {l, l ^ {\prime} = 0} ^ {m ^ {\prime}} a _ {l, l ^ {\prime}} ^ {*} b _ {l ^ {\prime}, l}\right) \\ = 2 \sum_ {l, l ^ {\prime} = 0} ^ {m ^ {\prime}} \left| a _ {l, l ^ {\prime}} ^ {*} b _ {l ^ {\prime}, l} \right| \cos [ (m - m ^ {\prime}) \phi ]. \tag {9} \\ \end{array}
$$

To prove that we have chosen the best possible theoretical operator, we use the work of Mandel, who showed that the visibility of any pure or attenuated mixed state in an interferometer may be expressed as a function of the off-diagonal terms in the reduced density matrix from Eq. (4) [19],

$$
V _ {\mathrm {f}} = 2 \left| \rho_ {1, 2} \right| = 2 \left| \sum_ {l, l ^ {\prime} = 0} ^ {m ^ {\prime}} a _ {l, l ^ {\prime}} ^ {*} b _ {l ^ {\prime}, l} \right| = 2 \sum_ {l, l ^ {\prime} = 0} ^ {m ^ {\prime}} \left| a _ {l, l ^ {\prime}} ^ {*} b _ {l ^ {\prime}, l} \right|, \tag {10}
$$

where we call  $V_{\mathrm{f}}$  the fundamental visibility and  $\rho_{1,2}$  is taken from one of the off-diagonal terms in the density matrix in Eq. (4). Our task now is to choose an operator capable of sensing at the fundamental visibility limit. Any detection operator  $\hat{O}$  exhibiting an amplitude smaller than  $V_{\mathrm{f}}$ , i.e.,  $V_{\mathrm{f}} \geqslant \langle \hat{O} \rangle_{\Phi = 0}$ , is not using all available off-diagonal terms, and

![](images/9113e2cabc78fd95078a9f0a61ad9da23e98476850304a0c799197fcfb4372ed.jpg)  
FIG. 2. (Color online) Phase sensitivity  $\delta \phi$  for a  $|20::10\rangle$ $|m::m^{\prime}\rangle$  state (curved black solid line) versus a  $|10::0\rangle$  N00N state (curved blue dashed line) undergoing loss. Loss is  $40\%$  in the long arm and zero in the delay arm. Bottom black solid line is the Heisenberg limit for  $|20::10\rangle$ ,  $1/(m+m')$ . The red solid line is the Heisenberg limit for the  $|10::0\rangle$  N00N state and lossless limit for  $|20::10\rangle$ ,  $1/(m-m')$ . The black dotted line is the shot-noise limit for  $|20::10\rangle$ , while the blue dashed line is the shot-noise limit for  $|10::0\rangle$ . The N00N state is no longer below its shot-noise limit while the minimum phase sensitivity for the  $|m::m^{\prime}\rangle$  state  $|20::10\rangle$  is at its respective shot-noise limit.

thus not optimal. From Eqs. (9) and (10) we see that the expectation value of  $\hat{A}$  may be written as  $\langle \hat{A} \rangle = V_{\mathrm{f}}$  cos  $[(m - m')\phi]$ . We call the visibility of a particular detection scheme the detection visibility,  $V_{\mathrm{det}} = \langle \hat{O} \rangle_{\phi=0}$ . We see that the  $\hat{A}_N$  operator, and its more general form  $\hat{A}$  in Eq. (7), are both optimal for N00N and  $|m : m'\rangle$  states, respectively, and give a detection visibility equivalent to the fundamental visibility. The fundamental visibility for a N00N state is simply  $V_{\mathrm{f}} = (T_a T_b)^{N/2}$ , which is just the probability the N00N state arrives at the detector with no loss.

# IV. INCREASED ROBUSTNESS TO LOSS

The  $|m \vdots m^{\prime} \rangle$  states, with  $m - m^{\prime} = N$ , are capable of producing the same resolution as an  $N$ -photon  $N00N$  state, but at

![](images/da4f6319ba13c31225efaf5658d37f8469a466f31ebe756400dc847adfabae1b.jpg)  
FIG. 3. (Color online) Phase resolution for a  $|20::10\rangle$ $|m::m'\rangle$  state (curved black solid line) versus a  $|10::0\rangle N00N$  state (curved blue dashed line) undergoing 3 dB of loss. Loss is 3 dB in the long arm, zero in the delay arm. The amplitude of  $\langle \hat{A} \rangle$ , and hence the visibility of the super-resolving sub-Rayleigh fringes, for a  $|20::10\rangle$  state is  $41\%$ , while the  $|10::0\rangle N00N$  state visibility is  $3.1\%$ .

the cost of requiring  $m'$  more photons to do so, and thus they operate at a smaller shot-noise limit. As we will show, in the presence of loss, however, many  $|m\because m'\rangle$  states operate below their own shot-noise limit, while N00N states of the same resolving power do not.

To compare a certain  $|m \because m' \rangle$  to a N00N state we choose the state such that  $m - m' = N$ , so the amount of phase information is the same for either state. This way our minimum phase sensitivity also starts from the same point,  $1 / (m - m') = 1 / N$ . The true Heisenberg limit for an  $|m \because m' \rangle$  state, however, is determined by the total photon number in the state and is therefore given by  $1 / (m + m')$ . The shot-noise limit for an  $|m \because m' \rangle$  state is  $1 / \sqrt{m + m'}$ , while the N00N state is the usual  $1 / \sqrt{N}$ .

As would be the case in a practical quantum sensor, we assume loss in the long arm  $b$  of the interferometer to be much greater than that of the delay arm  $a$ , which we assume to be under controlled loss conditions. Figure 2 is an example of an  $|m: m^{\prime}\rangle$  state showing more robustness to loss in phase sensitivity than an equivalent N00N state. A N00N state of  $N = 10$  degrades to the shot-noise limit at approxi

![](images/af2290779af1964e7bebc7e93937e7d6923b2efef0af6878a49ebec7c02eb326.jpg)  
FIG. 4. (Color online) (a) Visibility for  $|10::0\rangle$  as a function of loss in the delay and long arms,  $L_{a}$  and  $L_{b}$ , respectively. Contour lines represent the value of the visibility. (b) Same as (a) for the state  $|20::10\rangle$ .

![](images/69cf36dfeb0e1a00a8e71627a7025996ee20de5ba8e910961bbb2d6704f9dc1b.jpg)

TABLE I. Comparison of visibility and minimum detectable phase for  $N = 10 = m - {m}^{\prime }{N00N}$  state versus various  $\left| {m :  : {m}^{\prime }}\right\rangle$  states. Values are for long arm loss  $3\mathrm{{dB}}$  ,and zero loss in the delay arm. Heisenberg (HL)  $\left\lbrack  {1/\left( {m + {m}^{\prime }}\right) }\right\rbrack$  and shot-noise (SNL)  $\left( {1/\sqrt{m + {m}^{\prime }}}\right)$  limits are given.  

<table><tr><td>m</td><td>m&#x27;</td><td>Visibility</td><td>δφmin</td><td>HL</td><td>SNL</td></tr><tr><td>10</td><td>0</td><td>3.13%</td><td>2.264</td><td>0.100</td><td>0.316</td></tr><tr><td>11</td><td>1</td><td>6.74%</td><td>1.051</td><td>0.083</td><td>0.289</td></tr><tr><td>12</td><td>2</td><td>10.96%</td><td>0.652</td><td>0.071</td><td>0.267</td></tr><tr><td>14</td><td>4</td><td>19.85%</td><td>0.372</td><td>0.056</td><td>0.236</td></tr><tr><td>16</td><td>6</td><td>28.11%</td><td>0.279</td><td>0.045</td><td>0.213</td></tr><tr><td>18</td><td>8</td><td>35.19%</td><td>0.238</td><td>0.038</td><td>0.196</td></tr><tr><td>20</td><td>10</td><td>41.11%</td><td>0.254</td><td>0.033</td><td>0.183</td></tr></table>

mately  $26\%$  loss in the long arm (zero loss in the delay arm), whereas a  $|20::10\rangle |m::m^{\prime}\rangle$  state degrades to its respective shot-noise limit at larger loss,  $40\%$  loss in the long arm (zero loss in the delay arm).

Also important is to note how  $\langle \hat{A}\rangle$ , and by extension the visibility, evolve with loss. Under lossless conditions, the visibility of a  $N00N$  or  $|m: m^{\prime}\rangle$  state is always 1, and hence so is the amplitude of  $\langle \hat{A}\rangle$ . Figure 3 shows a comparison of  $\langle \hat{A}\rangle$  for  $|20::10\rangle$  and  $|10::0\rangle$  under  $50\% = 3$  dB loss in the long arm (zero in the delay arm).

We can examine the visibility as a function of loss in both arms directly with contour plots. Figures 4(a) and 4(b) show an order of magnitude increase in visibility for the  $|20::10\rangle$ $|m::m^{\prime}\rangle$  state over the  $|10::0\rangle$ $N00N$  state.

The improvement in visibility is greater than that seen in minimum phase sensitivity in Fig. 2. This suggests that the  $|m\because m^{\prime}\rangle$  states are much better suited than N00N states for resolving interference fringes under loss.

A heuristic way to understand the improvement of  $|m \because m^{\prime} \rangle$  states over  $N00N$  states is to consider "which-path" information available to the environment after photon loss. For example, even a single photon lost in mode  $b$  projects the  $N00N$  state from  $|N,0\rangle + e^{iN\phi}|0,N\rangle \rightarrow e^{iN\phi}|0,N - 1\rangle$ . That is, a single photon in environmental mode  $b$  provides complete which-path information—the environment "knows" with certainty it cannot have the  $|0\rangle$  component of the  $N00N$  state, which collapses the state into the separable state  $|0,N - 1\rangle$ . In contrast, an  $|m \because m^{\prime} \rangle$  state may lose up to  $m^{\prime}$  photons to the environment without complete knowledge of whether the  $m$  or  $m^{\prime}$  component was present, and hence com

plete "which-path" information is not available, and a great deal of coherence is hence preserved.

In comparing the  $|m\because m^{\prime}\rangle$  states to  $N00N$  states, there emerges a delicate tradeoff in sensor performance from adding  $m^{\prime}$  photons to increase the number of available output states, which contain phase information. Add too few  $m^{\prime}$  photons and there will not be significant improvement. Add too many  $m^{\prime}$  photons and the total number of photons required to carry the phase information for an equivalent  $N00N$  state rises, causing the shot-noise limit to be lowered further and reached quicker under conditions of loss (see Table I).

# V. CONCLUSION

We have shown that the class of entangled Fock states with photons in both modes,  $|m::m^{\prime}\rangle$  states, is more robust to loss than  $N00N$  states possessing all photons in either mode. The visibility for an  $|m::m^{\prime}\rangle$  state under loss may be an order of magnitude or more greater than  $N00N$  states, as well as having attenuated minimum phase sensitivities that are lower and more likely to be less than the shot-noise limit than a  $N00N$  state. While the  $|m::m^{\prime}\rangle$  states are not capable of reaching the Heisenberg limit of  $1/N$ , it seems unlikely that any state is capable of reaching this precision in the limit of practical sensing with appreciable photon loss. While  $|m::m^{\prime}\rangle$  states are more robust, they do appear to have loss-induced limitations as well. For many  $|m::m^{\prime}\rangle$  states, visibility drops to approximately  $10\%$  around the  $70\%$  loss level in one arm, assuming perfect transmission in the other.

Other issues that need consideration are how to produce  $|m::m^{\prime}\rangle$  states and how to optimally detect them. As of yet there is no efficient, on demand, Fock number state generator. However, the output from an optical parametric amplifier (OPA) is essentially a summation of many  $|m::m^{\prime}\rangle$  states as well as several  $N00N$  states. While we know what the optimal operators look like mathematically, it is also currently unknown how to produce these in the lab. We are currently analyzing the sensing capabilities for the entire output state of an OPA, as well as schemes for generating  $|m::m^{\prime}\rangle$  states from an OPA output with postselection.

# ACKNOWLEDGMENTS

We would like to acknowledge support from the Defense Advanced Research Projects Agency, the Army Research Office, and the Intelligence Advanced Research Projects Activity, as well as helpful discussions with H. Lee and G. A. Durkin.

[1] H. Lee, P. Kok, and J. P. Dowling, J. Mod. Opt. 49, 2325 (2002).  
[2] C. M. Caves, Phys. Rev. D 23, 1693 (1981).  
[3] K. T. Kapale, L. D. Didomenico, H. Lee, P. Kok, and J. P. Dowling, Concepts Phys. 2, 225 (2005).  
[4] V. Giovannetti, S. Lloyd, and L. Maccone, Science 306, 1330 (2004).

[5] A. N. Boto, P. Kok, D. S. Abrams, S. L. Braunstein, C. P. Williams, and J. P. Dowling, Phys. Rev. Lett. 85, 2733 (2000).  
[6] G. A. Durkin and J. P. Dowling, Phys. Rev. Lett. 99, 070801 (2007).  
[7] M. D'Angelo, M. V. Chekhova, and Y. Shih, Phys. Rev. Lett. 87, 013602 (2001).  
[8] D. Bouwmeester, Nature (London) 429, 139 (2004).

[9] P. Walther, J.-W. Pan, M. Aspelmeyer, R. Ursin, S. Gasparoni, and A. Zeilinger, Nature (London) 429, 158 (2004).  
[10] M. W. Mitchell, J. S. Lundeen, and A. M. Steinberg, Nature (London) 429, 161 (2004).  
[11] T. Nagata, R. Okamoto, J. L. O'Brien, K. Sasaki, and S. Takeuchi, Science 316, 726 (2007).  
[12] G. Gilbert, M. Hamrick, and Y. S. Weinstein, Proc. SPIE 6573, 65730K (2007).  
[13] M. A. Rubin and S. Kaushik, Phys. Rev. A 75, 053805 (2007).  
[14] A. D. Parks, S. E. Spence, J. E. Troupe, and N. J. Rodecap,

Rev. Sci. Instrum. 76, 043103 (2005).  
[15] R. T. Glasser, H. Cable, J. P. Dowling, F. DeMartini, F. Sciarrino, and C. Vitelli, Phys. Rev. A 78, 012339 (2008).  
[16] H. P. Yuen and J. H. Shapiro, IEEE Trans. Inf. Theory 24, 6 (1978).  
[17] C. W. Gardiner and P. Zoller, Quantum Noise (Springer, Berlin, 2004).  
[18] C. C. Gerry and P. L. Knight, Introductory Quantum Optics (Cambridge University Press, Cambridge, 2005).  
[19] L. Mandel, Opt. Lett. 16, 1882 (1991).