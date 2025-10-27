# Supplementary Information:

# Quantum optical emulation of molecular vibronic spectroscopy using a trapped-ion device

Yangchao Shen $^{1}$ , Yao Lu $^{1}$ , Kuan Zhang $^{1}$ , Junhua Zhang $^{1}$ , Shuaining Zhang $^{1}$ , Joonsuk Huh $^{2*}$  and Kihwan Kim $^{1\dagger}$ $^{1}$ Center for Quantum Information, Institute for Interdisciplinary Information Sciences, Tsinghua University, Beijing 100084, P. R. China.  $^{2}$ Department of Chemistry, Sungkyunkwan University, Suwon 16419, Korea.

(Dated: October 24, 2017)

# A. QUANTUM OPTICAL OPERATORS

We define, herein, the quantum optical operators we have used in our work.  $\pmb{a}$  and  $\pmb{a}^{\dagger}$  are  $N$ -dimensional column vectors for the bosonic annihilation and creation operators, respectively. That is,

$$
\boldsymbol {a} \equiv (a _ {1}, a _ {2}, \dots , a _ {N}) ^ {\mathrm {T}}, \boldsymbol {a} ^ {\dagger} \equiv (a _ {1} ^ {\dagger}, a _ {2} ^ {\dagger}, \dots , a _ {N} ^ {\dagger}) ^ {\mathrm {T}} \tag {1}
$$

where  $[a_i, a_j^\dagger] = \delta_{ij}$ .

The  $N$ -mode displacement operator is defined as below with the displacement vector  $\alpha = (\alpha_{1},\alpha_{2},\dots,\alpha_{N})$

$$
\hat {D} _ {N} (\boldsymbol {\alpha}) = \exp \left\{\boldsymbol {\alpha} \boldsymbol {a} ^ {\dagger} - \boldsymbol {\alpha} ^ {*} \boldsymbol {a} \right\}. \tag {2}
$$

The  $N$ -mode squeezing operator is defined as below with the squeezing parameter matrix  $\zeta = \mathrm{diag}(\zeta_1, \zeta_2, \dots, \zeta_N)$ .

$$
\hat {S} _ {N} (\boldsymbol {\zeta}) = \exp \left\{\frac {\boldsymbol {a} ^ {\mathrm {T}} \boldsymbol {\zeta} ^ {\dagger} \boldsymbol {a}}{2} - \frac {(\boldsymbol {a} ^ {\dagger}) ^ {\mathrm {T}} \boldsymbol {\zeta} \boldsymbol {a} ^ {\dagger}}{2} \right\}. \tag {3}
$$

The  $N$ -mode rotation operator is defined as below with a unitary matrix  $\pmb{U}$ ,

$$
\hat {R} _ {N} (\boldsymbol {U}) = \exp \left\{\left(\boldsymbol {a} ^ {\dagger}\right) ^ {\mathbf {T}} \ln (\boldsymbol {U}) \boldsymbol {a} \right\}. \tag {4}
$$

# B. EXPERIMENTAL PARAMETERS FOR QUANTUM OPTICAL OPERATIONS

We present, here, the parameters used in the trapped-ion device for the quantum optical operations. The displacement operator with two modes is rewritten as follows,

$$
\begin{array}{l} \hat {D} _ {2} (\alpha) = \hat {D} \left(\alpha_ {\mathrm {X}}, \alpha_ {\mathrm {Y}}\right) \\ = \exp \left\{\alpha_ {\mathrm {X}} a _ {\mathrm {X}} ^ {\dagger} - \alpha_ {X} ^ {*} a _ {\mathrm {X}} \right\} \exp \left\{\alpha_ {\mathrm {Y}} a _ {\mathrm {Y}} ^ {\dagger} - \alpha_ {\mathrm {Y}} ^ {*} a _ {\mathrm {Y}} \right\}. \tag {5} \\ \end{array}
$$

As seen in Eq. 5, the displacement operations of the X and Y modes can be implemented independently.

The squeezing operator with the two mode parameter  $\zeta = \mathrm{diag}(\ln \sqrt{\omega_1},\ln \sqrt{\omega_2}) = \mathrm{diag}(\zeta_{\mathrm{X}},\zeta_{\mathrm{Y}})$  can be rewritten as follows,

$$
\begin{array}{l} \hat {S} _ {2} (\zeta) = \hat {S} (\operatorname {d i a g} \left(\zeta_ {\mathrm {X}}, \zeta_ {\mathrm {Y}}\right)) \\ = \exp \left\{\frac {\zeta_ {\mathrm {X}}}{2} \left(a _ {\mathrm {X}} a _ {\mathrm {X}} - a _ {\mathrm {X}} ^ {\dagger} a _ {\mathrm {X}} ^ {\dagger}\right) \right\} \exp \left\{\frac {\zeta_ {\mathrm {Y}}}{2} \left(a _ {\mathrm {Y}} a _ {\mathrm {Y}} - a _ {\mathrm {Y}} ^ {\dagger} a _ {\mathrm {Y}} ^ {\dagger}\right) \right\}. \tag {6} \\ \end{array}
$$

* Author to whom correspondence should be addressed: joonsukhuh@skku.edu  
† Author to whom correspondence should be addressed: kimkihwan@mail.tsinghua.edu.cn

In the trapped-ion experiment, the squeezing operations are limited to the range of  $\zeta_{\mathrm{X}}(\zeta_{\mathrm{Y}}) \leq 4$  in Eq. (6). Since  $\hat{U}_{\mathrm{Dok}}$  involves the squeezing and inverse squeezing operations, we can freely rescale the squeezing parameters with a single arbitrary constant. In our experiment, we rescale the squeezing parameters by a factor of  $1/25$ ,  $\mathrm{diag}(\zeta_{\mathrm{X}}, \zeta_{\mathrm{Y}}) = \mathrm{diag}(\ln(\sqrt{\omega_1}/25), \ln(\sqrt{\omega_2}/25))$  for the first squeezing operation and  $\mathrm{diag}(\zeta_{\mathrm{X}}', \zeta_{\mathrm{Y}}') = \mathrm{diag}(\ln(\sqrt{\omega_1'}/25), \ln(\sqrt{\omega_2'}/25))$  for the anti-squeezing in the Eq. (2) of the main text. As discussed in Ref [1], the Doktorov operation  $\hat{U}_{\mathrm{Dok}}$  in Eq. (2) of the main text can be expressed in terms of the ladder operators as

$$
\boldsymbol {a} ^ {\prime \dagger} = \frac {1}{2} \left(\boldsymbol {J} - \left(\boldsymbol {J} ^ {t}\right) ^ {- 1}\right) \boldsymbol {a} + \frac {1}{2} \left(\boldsymbol {J} + \left(\boldsymbol {J} ^ {t}\right) ^ {- 1}\right) \boldsymbol {a} ^ {\dagger} + \frac {1}{\sqrt {2}} \boldsymbol {\alpha} \tag {7}
$$

where  $J = \zeta' U \zeta^{-1}$ . Since  $J$  is invariant for the parameter sets  $(\zeta', \zeta)$  and  $(\zeta'/25, \zeta/25)$  as an example, the resulting  $\hat{U}_{\mathrm{Dok}}$  is maintained.

The two mode rotation operation can be written simply with a rotation angle  $\theta$ ,

$$
\hat {R} _ {2} (\boldsymbol {U}) = \hat {R} (\theta) = e ^ {\theta \left(\hat {a} _ {\mathrm {X}} ^ {\dagger} \hat {a} _ {\mathrm {Y}} - \hat {a} _ {\mathrm {X}} \hat {a} _ {\mathrm {Y}} ^ {\dagger}\right)} \tag {8}
$$

where  $\mathbf{U} = \begin{pmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{pmatrix}$  becomes the unitary rotation matrix. The rotation angle  $\theta$  is controlled by Raman laser beams in the trapped-ion simulation.

TABLE I. Parameters for the trapped-ion simulation of  $\mathrm{SO}_2\rightarrow \mathrm{SO}_2^+$  and  $\mathrm{SO}_2^- \rightarrow \mathrm{SO}_2$  

<table><tr><td></td><td>SO2→SO2+</td><td>SO2-→SO2</td></tr><tr><td>αX, αY</td><td>(-0.026, 1.716)</td><td>(1.360, -0.264)</td></tr><tr><td>ω1&#x27;, ω2&#x27;</td><td>(1112.7, 415)</td><td>(1178.4, 518.9)</td></tr><tr><td>ζX&#x27;,ζY&#x27;</td><td>(0.288, -0.204)</td><td>(0.317, -0.093)</td></tr><tr><td rowspan="2">U</td><td>(0.982 0.188)</td><td>(0.998 0.065)</td></tr><tr><td>-0.188 0.982)</td><td>-0.065 0.998)</td></tr><tr><td>θ</td><td>0.1892</td><td>0.065</td></tr><tr><td>ω1, ω2</td><td>(1178.4, 518.9)</td><td>(989.5, 451.4)</td></tr><tr><td>ζX,ζY</td><td>(0.317, -0.093)</td><td>(0.229, -0.162)</td></tr></table>

# C. QUANTUM OPTICAL OPERATIONS IN TRAPPED-ION SYSTEM

We implement the quantum optical operations  $(\hat{D},\hat{S}$  and  $\hat{R})$  via controlling Raman laser beams. Fig. 1 shows the energy diagram of a trapped  $^{171}\mathrm{Yb}^+$ . The two levels in hyperfine structure of  $^{2}\mathrm{S}_{1 / 2}$  manifold are usually used to realize

a qubit, which are denoted as  $|\downarrow \rangle \equiv |\mathrm{F} = 0,\mathrm{m}_{\mathrm{F}} = 0\rangle$  and  $|\uparrow \rangle \equiv |\mathrm{F} = 1,\mathrm{m}_{\mathrm{F}} = 0\rangle$ . The red color (mode X) and blue color (mode Y) harmonic oscillators stand for the motional degrees of freedom. The Raman process is implemented via the virtual energy level, which is  $10.8\mathrm{THz}$  detuned from  $\mathrm{P}_{1 / 2}$  level,  $|e\rangle$ .

![](images/d73d0d1d731ea83db6360e8a722a49ba1f8d426232230fc647221a7d182e86bf.jpg)  
FIG. 1. Energy level diagram of  $^{171}\mathrm{Yb}^{+}$  with two motional modes and basic Raman transitions. The electronic levels  $(|\uparrow \rangle, |\downarrow \rangle)$  with the difference  $\omega_{\mathrm{hf}}$ , and the phonon levels of modes X and Y with the frequencies of  $\omega_{\mathrm{X}}$  and  $\omega_{\mathrm{Y}}$  are involved in the Raman process. By controlling the frequency difference of Raman1 and Raman2, we can implement single mode and two modes quantum operations.

Our quantum optical operations are implemented in a way that the phase coherence among them are well preserved. All the operations are internal-state dependent, which requires one frequency in Raman 1,  $\omega_{\mathrm{R1}}$ , and two frequencies and phases in Raman 2,  $\omega_{\mathrm{R2,1}}$  and  $\omega_{\mathrm{R2,2}}$ , where Raman 1 and Raman 2 are counter-propagating towards the ion. Here, we show how the quantum optical operations are implemented with these laser beams. We start from the light-matter interaction Hamiltonian as shown in the following equation,

$$
\begin{array}{l} H = \frac {\hbar \omega_ {\mathrm {h f}}}{2} \sigma_ {\mathrm {Z}} + \hbar \omega_ {\mathrm {X}} \left(a _ {\mathrm {X}} ^ {\dagger} a _ {\mathrm {X}} + \frac {1}{2}\right) + \hbar \omega_ {\mathrm {Y}} \left(a _ {\mathrm {Y}} ^ {\dagger} a _ {\mathrm {Y}} + \frac {1}{2}\right) \\ + \sum_ {j = 1, 2} \frac {\hbar g}{2} \left(\sigma_ {+} + \sigma_ {-}\right) \left(e ^ {i (\vec {k} \cdot \vec {r} - \omega_ {L, j} t + \phi_ {j})} + e ^ {- i (\vec {k} \cdot \vec {r} - \omega_ {L, j} t + \phi_ {j})}\right), \tag {9} \\ \end{array}
$$

where  $g$  is the Rabi frequency,  $\sigma_{+} = |\uparrow \rangle \langle \downarrow|$  and  $\sigma_{-} = |\downarrow \rangle \langle \uparrow|$ , effective laser frequencies  $\omega_{L,j} = \omega_{R1} - \omega_{R2,j}$ , phases  $\phi_j$  and  $\vec{k} \cdot \vec{r} = k_{\mathrm{X}}x + k_{\mathrm{Y}}y$ .

The interaction Hamiltonian with respect to  $H_0 = \frac{\hbar\omega_{\mathrm{hf}}}{2}\sigma_{\mathrm{Z}} + \hbar \omega_{\mathrm{X}}(a_{\mathrm{X}}^{\dagger}a_{\mathrm{X}} + \frac{1}{2}) + \hbar \omega_{\mathrm{Y}}(a_{\mathrm{Y}}^{\dagger}a_{\mathrm{Y}} + \frac{1}{2})$  with rotating wave approximation and the Lamb-Dicke approximation  $\eta_{\mathrm{X(Y)}}^{2}(2\langle n\rangle +1)\ll 1$ , where Lamb-Dicke parameters  $\eta_{\mathrm{X}} = \sqrt{2} k_{\mathrm{X}}\sqrt{\hbar / 2M_{\mathrm{Yb}}\omega_{\mathrm{X}}} = 0.080$  and  $\eta_{\mathrm{Y}} =$

$\sqrt{2} k_{\mathrm{Y}}\sqrt{\hbar / 2M_{\mathrm{Yb}}\omega_{\mathrm{Y}}} = 0.087$  can be written as

$$
\begin{array}{l} H _ {I} = \sum_ {j = 1, 2} \frac {\hbar g}{2} \sigma_ {+} \left\{1 + i \eta_ {\mathrm {X}} \left(a _ {\mathrm {X}} e ^ {- i \omega_ {\mathrm {X}} t} + a _ {\mathrm {X}} ^ {\dagger} e ^ {i \omega_ {\mathrm {X}} t}\right) \right. \\ + i \eta_ {\mathrm {Y}} (a _ {\mathrm {Y}} e ^ {- i \omega_ {\mathrm {Y}} t} + a _ {\mathrm {Y}} ^ {\dagger} e ^ {i \omega_ {\mathrm {Y}} t}) \\ \left. - \eta_ {\mathrm {X}} \eta_ {\mathrm {Y}} \left(a _ {\mathrm {X}} e ^ {- i \omega_ {\mathrm {X}} t} + a _ {\mathrm {X}} ^ {\dagger} e ^ {i \omega_ {\mathrm {X}} t}\right) \left(a _ {\mathrm {Y}} e ^ {- i \omega_ {\mathrm {Y}} t} + a _ {\mathrm {Y}} ^ {\dagger} e ^ {i \omega_ {\mathrm {Y}} t}\right) \right\} \\ e ^ {- i \delta_ {j} t} e ^ {i \phi_ {j}} + \mathrm {h . c .}, \tag {10} \\ \end{array}
$$

where  $\delta_{j} = \omega_{L,j} - \omega_{\mathrm{hf}}$

When we consider the resonant terms, we have the following effective Hamiltonian. By setting  $\delta_1 = \omega_{\mathrm{X}}$ ,  $\delta_2 = -\omega_{\mathrm{X}}$  as shown in Fig. 2a, the displacement operation  $\hat{D}$  of a single mode (here, mode X as an example) is written as

$$
\begin{array}{l} \hat {D} (\alpha_ {\mathrm {X}}, 0) \\ = \exp \left\{- i \alpha_ {\mathrm {X}} \left(\sigma_ {+} e ^ {i \phi_ {A}} - \sigma_ {-} e ^ {- i \phi_ {\mathrm {A}}}\right) \left(a _ {\mathrm {X}} ^ {\dagger} e ^ {- i \phi_ {\mathrm {B}}} + a _ {\mathrm {X}} e ^ {i \phi_ {B}}\right) \right\}, \tag {11} \\ \end{array}
$$

where  $\alpha_{\mathrm{X}} = tg_{D} = t\frac{\eta_{\mathrm{X}}\hbar g}{2}$ ,  $\phi_{\mathrm{A}} = \phi_{1} + \phi_{2}$  and  $\phi_{\mathrm{B}} = \phi_{2} - \phi_{1}$ . When  $\phi_{1} = \phi_{2} = \pi / 2$ ,  $\hat{D}(\alpha_{\mathrm{X}}, 0)$  becomes  $\sigma_{x}$ -dependent displacement operation. We change it to  $\sigma_{z}$ -dependent displacement operation with additional  $\pi / 2$  carrier rotation pulses (along  $\sigma_{y}$  and  $\sigma_{-y}$  axis) before and after  $\sigma_{x}$ -dependent displacement.

Similarly, by setting  $\delta_{1} = \omega_{\mathrm{X}} - \delta_{\mathrm{S}}$ ,  $\delta_{2} = -\omega_{\mathrm{X}} - \delta_{\mathrm{S}}$ , as shown in Fig. 2b, the squeezing operation  $\hat{S}$  of a single mode (here, mode X as an example) is written as

$$
\hat {S} \left(\zeta_ {\mathrm {X}}, 0\right) = \exp \left\{- i \zeta_ {\mathrm {X}} \left(a _ {\mathrm {X}} ^ {\dagger} a _ {\mathrm {X}} ^ {\dagger} e ^ {i \phi_ {\mathrm {B}}} + a _ {\mathrm {X}} a _ {\mathrm {X}} e ^ {- i \phi_ {\mathrm {B}}}\right) \sigma_ {z} \right\}, \tag {12}
$$

where  $\zeta_{\mathrm{X}} = tg_{S} = t\frac{\hbar\eta_{\mathrm{X}}^{2}g^{2}}{8}\left(\frac{1}{\delta_{1}} -\frac{2}{\delta_{1} - \omega_{\mathrm{X}}} +\frac{1}{\delta_{1} - 2\omega_{\mathrm{X}}}\right)$  and  $\phi_{\mathrm{B}} = \phi_{2} - \phi_{1}$ . In our experiment, the  $\delta_{\mathrm{S}}$  is set as five times of anti-Jaynes-Cummings coupling Rabi frequency  $(\eta_{\mathrm{X}}g)$ .

For rotation operation  $\hat{R}$ , we set  $\delta_{1} = -\omega_{X} - \delta_{\mathrm{R}}$ ,  $\delta_{2} = -\omega_{Y} - \delta_{\mathrm{R}}$ , which leads the configuration shown in Fig. 2c. In our experiment, the  $\delta_{\mathrm{R}}$  is also set as five times of anti-Jaynes-Cummings coupling Rabi frequency ( $\eta_{\mathrm{X}}g$ ).

$$
\hat {R} (\theta) = \exp \left\{- i \theta \left(a _ {\mathrm {X}} ^ {\dagger} a _ {\mathrm {Y}} e ^ {- i \phi_ {\mathrm {B}}} + a _ {\mathrm {X}} a _ {\mathrm {Y}} ^ {\dagger} e ^ {i \phi_ {\mathrm {B}}}\right) \sigma_ {z} \right\}. \tag {13}
$$

where  $\theta = t g_{R} = t \frac{\hbar \eta_{\mathrm{X}} \eta_{\mathrm{Y}} g^{2}}{4} \left( \frac{1}{-\delta_{1}} + \frac{1}{-\delta_{1} + \omega_{\mathrm{X}} - \omega_{\mathrm{Y}}} + \frac{1}{\delta_{1} - \omega_{\mathrm{X}}} + \frac{1}{\delta_{1} + \omega_{\mathrm{Y}}} \right)$  and  $\phi_{\mathrm{B}} = \phi_{2} - \phi_{1}$ .

When we only consider the Hilbert space with electronic state  $|\downarrow \rangle$ , all the above  $\sigma_z$  dependent force can be simplified to the quantum optical operations shown in Appendix B. The optical phase instability between Raman 1 and Raman 2 caused by the beam fluctuation does not influence the coherence of quantum operations, since all the phases  $\phi_{\mathrm{B}}$  of all these quantum operations are controlled by RF sources on Raman 2.

![](images/07adaf2a057f694d7a4c788cbe9f740a83a2ca2b8210dd4a5060843026308a69.jpg)  
(a)

![](images/577ab8df0ac6d0234d03e6c67bde1622dd933eaaf58d6219fb16ea38ce9f2d09.jpg)  
(b)

![](images/0f4251f17e0d8a22ade1b05e727f7afb13a102a3efe123241e0aacc04cd2703f.jpg)  
FIG. 2. Trapped-ion implementation of the quantum optical operations. The Hilbert space is composed of two phonon modes of X and Y and the internal electronic state  $|\uparrow \rangle$  and  $|\downarrow \rangle$ . The quantum operations are implemented via control the frequency and phase of  $\omega_{\mathrm{R2,1}}$  and  $\omega_{\mathrm{R2,2}}$ . (a) Coherent displacement operation  $\hat{D}$  and (b) squeezing operation  $\hat{S}$  on X mode as an example. (c) Rotation operation  $\hat{R}$  between X and Y modes.  
(c)

We confirm the phase coherence between  $\hat{D}$  and  $\hat{S}$  by experimentally reconstructing the Wigner function of a coherent displacement state and a squeezed vacuum state. The comparisons with theoretical calculation are shown in Fig. 3. We reconstruct the Wigner function by using the iterative maximum-likelihood algorithm on the phonon number distribution for eight different angles in the phase space[2, 3]. The phonon number distribution is construct in three steps: (i) prepare the initial coherent state or squeezed vacuum state, (ii) coherent push the initial state with eight different angles, (iii) apply the standard Jaynes Cummings coupling and resolve the distribution through the fitting of the observed oscillations.

# D. METHOD FOR COLLECTIVE PROJECTION MEASUREMENTS

We explain in this section the pulse sequence for the detection of population in an arbitrary phonon state  $|\Sigma, \mathrm{n_X}, \mathrm{n_Y}\rangle$ , where we indicate the internal qubit state  $\Sigma$  ( $\downarrow$  or  $\uparrow$ ) of the phonon state  $(|\mathrm{n_X}, \mathrm{n_Y}\rangle)$ .

The first step is to transfer the population in the target state  $|\downarrow, \mathrm{n_X}, \mathrm{n_Y}\rangle$  to  $|\downarrow, 0, 0\rangle$ : it is performed by applying a sequence of  $\pi$ -pulse transitions, as shown in Fig. 4a, i.e., with the following steps,

$$
\begin{array}{l} \mathbf {a}: | \downarrow , n _ {X}, n _ {Y} \rangle \xrightarrow {\pi - C a r r i e r} | \uparrow , n _ {X}, n _ {Y} \rangle \\ \xrightarrow {\pi - \operatorname {B l u e X}} | \downarrow , n _ {X} - 1, n _ {Y} \rangle \\ \dots \longrightarrow \dots | \downarrow , 0, n _ {Y} \rangle \\ \xrightarrow {\pi - \text {C a r r i e r}} | \uparrow , 0, n _ {Y} \rangle \\ \xrightarrow {\pi - \text {B l u e Y}} | \downarrow , 0, n _ {Y} - 1 \rangle \\ \dots \longrightarrow \dots | \downarrow , 0, 0 \rangle \tag {14} \\ \end{array}
$$

The second step is to obtain the population in  $|\downarrow, 0, 0\rangle$  by using the sequence as shown in Fig. 4b-f. The important technique used in this process is called uniform red sideband transition, which is a full population transfer independent of the initial motion state[2], it exchanges the state population between  $|\downarrow, \mathrm{n_X} + 1, \mathrm{n_Y}\rangle$  and  $|\uparrow, \mathrm{n_X}, \mathrm{n_Y}\rangle$  when it is uniform red sideband on mode X, or  $|\downarrow, \mathrm{n_X}, \mathrm{n_Y} + 1\rangle$  and  $|\uparrow, \mathrm{n_X}, \mathrm{n_Y}\rangle$  when it is uniform red sideband on mode Y. In the real experiment setting, the maximum phonon number are restricted to  $n_{\mathrm{X(Y)}} < 10$ .

b: Apply the fluorescence detection and record the event  $M_{1}$  of detecting photons or no photons.  
c: Apply a uniform red sideband transition on mode X, which transfers all the states of  $|\downarrow ,\mathrm{n_X} > 0,\mathrm{n_Y}\rangle$  to  $|\uparrow \rangle$  state.  
d: Apply the fluorescence detection and record the event  $M_2$  of detecting photons or no photons.  
e: Apply a uniform red sideband transition on Y mode, which transfers all the states of  $|\downarrow, \mathrm{n_X}, \mathrm{n_Y} > 0 \rangle$  to  $|\uparrow \rangle$  state.

![](images/f013346f1e8f678ea8bdba7abc60fd2fdbb89e9a1e2b429547d1c569f691f75f.jpg)  
Coherent displacement state

![](images/465551b833dd91143787eb5a1b63a373423b9f57da77bfea7c7a363c2e3c2cb3.jpg)

![](images/492776a2f764f081b3592afbaac2d365dd693c69be2339257eb18c5d1adfe094.jpg)  
Squeezed vacuum state

![](images/12e78e56311c268ecb7ad4e2fad5252ccc236bd8ba9b0d1d477aa3fc0f7db39f.jpg)

![](images/deb0e6a9982ffd3b94652df1c36806886752aa9d0e955035057b6f6b82048602.jpg)  
FIG. 3. Coherent displacement and squeezed vacuum state Wigner functions. (a) and (b) represents for the coherent displacement state with  $\alpha_{\mathrm{X}} = 0.5$ . c. and d. represents for the squeezed vacuum state with  $\zeta_{\mathrm{X}} = 0.5$  
FIG. 4. Detection method for the example of state  $|\downarrow, n_{\mathrm{X}} = 2, n_{\mathrm{Y}} = 2\rangle$ . The lower (purple grid) and the upper (orange grid) layers represent the internal states of  $|\downarrow\rangle$  and  $|\uparrow\rangle$ . The internal states have no fluorescence and fluorescence, respectively, during the internal state detection.

f: Apply the fluorescence detection and record the event  $M_3$  of detecting photons or no photons.

In the above multiple-detection stages, there are four situations for the recorded data  $M_{1}M_{2}M_{3}$

$$
\left\{\mathrm {B} \forall \forall , \mathrm {D B} \forall , \mathrm {D D B}, \mathrm {D D D} \right\}\rightarrow \left\{P _ {1}, P _ {2}, P _ {3}, P _ {4} \right\}. \tag {15}
$$

Here, D means detecting no photons, B means detecting photons,  $\forall$  stands for both situations. Typically, we repeat the experiments for 2000 times to get the probability for each case noted as  $P_{1}, P_{2}, P_{3}, P_{4}$ . The population of the target state is the probability of case  $P_{4}$ .

Within the above collective projection measurements, Fig. 3c shows the experimentally measured result for the fidelity of the detection sequence of an arbitrary state  $|\mathrm{n_X},\mathrm{n_Y}\rangle$

noted as  $F_{D.M}$ . The infidelity mainly comes from the imperfection of  $\pi$ -pulse and uniform red-transition on  $X$  and  $Y$  mode.

# E. MEASUREMENT-ERROR CORRECTIONS FOR THE EXPERIMENTAL RAW DATA

We mainly consider two error sources to correct the experimental raw data: i) the inefficiency of fluorescence detection of internal states; ii) the infidelity of the collective projection measurement discussed in section D.

Our fluorescence detection can distinguish the internal states  $|\uparrow \rangle$  and  $|\downarrow \rangle$  with the corresponding detection fidelities are  $\eta_{\uparrow \rightarrow \uparrow}$ $(97.2\%)$  state and  $\eta_{\downarrow \rightarrow \downarrow}$ $(99.3\%)$  for state, respectively. To correct this inefficiency, we use the value of  $P_4$

![](images/f44f895479d95c80dc8c89b9585f860a2a7d8924a632126eefdc55eb5d0f4988.jpg)  
FIG. 5. Comparison between the raw and the corrected experimental data for the spectroscopy of  $\mathrm{SO}_2\rightarrow \mathrm{SO}_2^+$ . The horizontal axis is the Fock state  $|n_{\mathrm{X}'}$ $n_{\mathrm{Y}'}$  and the vertical axis is the transition intensity to the state from the  $|0,0\rangle$  state.

which is obtained by  $1 - (P_{1} + P_{2} + P_{3})$ . The real population  $(P_R)$  of detecting photons scattered from the  $|\uparrow\rangle$  state is not exactly same to the measured population  $(P_M)$ . The relation between them is given as  $P_M = P_R \eta_{\uparrow \rightarrow \uparrow} + (1 - P_R)(1 - \eta_{\downarrow \rightarrow \downarrow})$ , thus

For the correction of the second part, as discussed in the Appendix C, we have to include the fidelity  $F_{D,M}$ .

In order to correct the raw experimental data, we consider these two imperfections. For the experiment raw data, our corrected data is written accordingly as,

$$
P _ {R} \equiv \operatorname {C o r r} \left(P _ {M}\right) = \frac {P _ {M} - \left(1 - \eta_ {\downarrow \rightarrow \downarrow}\right)}{\eta_ {\downarrow \rightarrow \downarrow} + \eta_ {\uparrow \rightarrow \uparrow} - 1} \tag {16}
$$

$$
P _ {4} ^ {\prime} = \frac {1 - \operatorname {C o r r} \left(P _ {1} + P _ {2} + P _ {3}\right)}{F _ {D . M}} \tag {17}
$$

Fig. 5 compares the raw experimental data and corrected data for the photoelectron spectroscopy of  $\mathrm{SO}_2$ .

[1] J. Huh, G. G. Guerreschi, B. Peropadre, J. R. McClean and A. Aspuru-Guzik, Nature Photon., 2015, 9, 615-620.  
[2] M. Um, J. Zhang, D. Lv, Y. Lu, S. An, J.-N. Zhang, H. Nha, M. S. Kim and K. Kim, Nat. Commun., 2016, 7, 11410.

[3] D. M. Meekhof, C. Monroe, B. E. King, W. M. Itano and D. J. Wineland, Phys. Rev. Lett., 1996, 76, 1796-1799.