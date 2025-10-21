# Experimental generation of four-mode continuous-variable cluster states

Mitsuyoshi Yukawa, $^{1,2}$  Ryuji Ukai, $^{1,2}$  Peter van Loock, $^{3}$  and Akira Furusawa $^{1,2}$

$^{1}$ Department of Applied Physics, School of Engineering, The University of Tokyo, 7-3-1 Hongo, Bunkyo-ku, Tokyo 113-8656, Japan

$^{2}$ CREST, Japan Science and Technology (JST) Agency, 5, Sanbancho, Chiyoda-ku, Tokyo 102-0075, Japan

<sup>3</sup>Optical Quantum Information Theory Group, Institute of Theoretical Physics I and Max-Planck Research Group, Institute of Optics, Information and Photonics, Universität Erlangen-Nürnberg, Staudstrasse 7/B2, 91058 Erlangen, Germany

(Received 2 April 2008; published 1 July 2008)

Continuous-variable Gaussian cluster states are a potential resource for universal quantum computation. They can be efficiently and unconditionally built from sources of squeezed light using beam splitters. Here we report on the generation of three different kinds of continuous-variable four-mode cluster states. In our realization, the resulting cluster-type correlations are such that no corrections other than simple phase-space displacements would be needed when quantum information propagates through these states. At the same time, the inevitable imperfections from the finitely squeezed resource states and from additional thermal noise are minimized, as no antisqueezing components are left in the cluster states.

DOI: 10.1103/PhysRevA.78.012301

PACS number(s): 03.67.Lx, 03.65.Ud

# I. INTRODUCTION

The one-way quantum computation model [1] is a conceptually interesting alternative to the standard circuit model. One-way quantum computation can be carried out with the help of a specially prepared entangled state, a so-called cluster state. Quantum information is then processed solely through measurements on the cluster state. Universal quantum gates can be achieved by choosing different measurement bases and using feedforward.

Small-scale discrete-variable (DV) cluster computations have been demonstrated already with single photons [2]. An alternative approach to, in particular, an optical implementation of cluster-based quantum computation is based upon continuous variables. Continuous-variable (CV) one-way quantum computation [3] relies upon CV cluster states [4]. Various ways for generating CV cluster-type states are known [3-7]. The method employed in this work is to combine beams of off-line squeezed light at beam splitters [5]. Once CV cluster states are available, quantum information encoded into an optical mode can be manipulated via homodyne and non-Gaussian measurements on the CV cluster [3,8]. As the elementary routine for cluster computation is quantum teleportation, first steps towards the implementation of CV cluster computation have been achieved already, including the realization of a quantum teleportation network [9], entanglement swapping [10], teleportation of squeezing [11], sequential quantum teleportation [12], and high-fidelity teleportation [13]. Here we report on the optical creation of four-mode CV cluster states suitable for small-scale implementations of CV one-way quantum computation.

The quadrature correlations of cluster-type states are such that in the limit of infinite squeezing, the states become zero eigenstates of a set of quadrature combinations,

$$
\left(\hat {p} _ {a} - \sum_ {b \in N _ {a}} \hat {x} _ {b}\right)\rightarrow 0, \quad \forall a \in G. \tag {1}
$$

Here,  $\hat{x}_a$  and  $\hat{p}_a$  correspond to "position" and "momentum" operators for an optical mode  $a$  with annihilation operator  $\hat{a}_a = \hat{x}_a + i\hat{p}_a(\hbar = \frac{1}{2})$ . Every mode  $a \in G$  represents a vertex of

the graph  $G$  (representing the cluster or graph state). The modes  $b \in N_{a}$  are the nearest neighbors of mode  $a$ .

A possible way to obtain CV cluster states is to entangle a corresponding number of optical modes, each initially in a squeezed state, through quantum nondemolition (QND) interactions [4], in analogy to the creation of qubit cluster states via controlled sign gates. We may refer to this specific type of cluster states as canonical cluster states [5]. Experimentally, the optical CV QND gates for every single link of the cluster state can be realized with two beam splitters and two on-line squeezers [14] for each link. Alternatively, the initial squeezing transformations can be absorbed into the entire QND network; after Bloch-Messiah reduction [14] only off-line squeezed states and linear optics are effectively needed then to produce a canonical cluster state [5].

In another approach for building CV cluster-type states from squeezed light using linear optics [5], the beam splitter network is carefully chosen such that, by construction, all antisqueezing components are completely eliminated in the output operator combinations,  $\hat{p}_a - \Sigma_{b\in N_a}\hat{x}_b$  ; hence these combinations, being proportional to the squeezing factor,  $\hat{p}_a - \Sigma_{b\in N_a}\hat{x}_b\propto e^{-r}$  , automatically satisfy the conditions of Eq. (1) in the limit of infinite squeezing  $r\to \infty$  . Moreover, generating cluster-type states in this way requires smaller degrees of input squeezing than needed for making the canonical states with the same quality of correlations [5].

The complete removal of antisqueezing components is particularly beneficial, as in the actual experiment, the antisqueezing levels are typically greater than the squeezing levels due to experimental imperfections such as losses and fluctuations in the phase locking. By employing the abovementioned method for eliminating the antisqueezing components in our experiment, we can observe that the single-mode squeezing levels of the input states before the generation of the cluster states are effectively reproduced in the multimode squeezing levels of the resulting cluster states. This is in contrast to the experiments of Refs. [15,16], where the antisqueezing components are not completely suppressed. Another advantage of our approach here is that the resulting quadrature correlations are precisely those occurring in the

![](images/192954b65c9abaf858774447a645eb7029352f3ad168c10b363dc54dc497659a.jpg)  
FIG. 1. The created four-mode cluster states. Each cluster node, corresponding to an optical mode, is represented by a circle. Neighboring nodes are connected by lines.

excess noise terms when quantum information propagates through a CV Gaussian cluster state [3]. Suppressing this excess noise efficiently means reducing the errors in cluster-based quantum computations.

# II. GAUSSIAN FOUR-MODE CLUSTER STATES

According to the efficient method proposed in Ref. [5], we created three kinds of four-mode CV cluster states in this experiment, including a linear cluster state, a square cluster state, and a T-shape cluster state (see Fig. 1).

In general, four-mode CV graph states can be built from four off-line squeezed states using up to six beam splitters [5,17]. For the linear four-mode cluster state, three beam splitters have been shown to be sufficient [5]. Similarly, only three beam splitters are needed to produce the square and the T-shape cluster states. The optical setups are described in detail below.

In order to create these cluster states, four  $p$ -squeezed states, with mode operators  $\hat{a}_i = e^{+r_i}\hat{x}_i^{(0)} + ie^{-r_i}\hat{p}_i^{(0)} (i = 1,\dots ,4)$ , are prepared first. A superscript (0) denotes initial vacuum modes and  $r_i$  is the squeezing parameter of the  $i$ th mode. For a unitary matrix  $U$  representing a sequence of beam splitters, the output mode operators  $\hat{a}_i^\prime$  can be obtained according to  $\hat{a}_i^\prime = \Sigma_j U_{ij} \hat{a}_j$ .

A possible solution for the matrix  $U_{\mathrm{L}}$ , giving the linear cluster state, is [5]

$$
U _ {\mathrm {L}} = \left( \begin{array}{c c c c} \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {1 0}} & \frac {2 i}{\sqrt {1 0}} & 0 \\ \frac {i}{\sqrt {2}} & - \frac {i}{\sqrt {1 0}} & \frac {2}{\sqrt {1 0}} & 0 \\ 0 & - \frac {2}{\sqrt {1 0}} & \frac {i}{\sqrt {1 0}} & \frac {i}{\sqrt {2}} \\ 0 & - \frac {2 i}{\sqrt {1 0}} & - \frac {1}{\sqrt {1 0}} & \frac {1}{\sqrt {2}} \end{array} \right). \tag {2}
$$

With this matrix, the quadrature quantum correlations of the output state become

$$
\hat {p} _ {\mathrm {L 1}} - \hat {x} _ {\mathrm {L 2}} = \sqrt {2} e ^ {- r _ {1}} \hat {p} _ {1} ^ {(0)},
$$

$$
\hat {p} _ {\mathrm {L 2}} - \hat {x} _ {\mathrm {L 1}} - \hat {x} _ {\mathrm {L 3}} = \sqrt {\frac {5}{2}} e ^ {- r _ {3}} \hat {p} _ {3} ^ {(0)} + \frac {1}{\sqrt {2}} e ^ {- r _ {4}} \hat {p} _ {4} ^ {(0)},
$$

$$
\hat {p} _ {\mathrm {L 3}} - \hat {x} _ {\mathrm {L 2}} - \hat {x} _ {\mathrm {L 4}} = \frac {1}{\sqrt {2}} e ^ {- r _ {1}} \hat {p} _ {1} ^ {(0)} - \sqrt {\frac {5}{2}} e ^ {- r _ {2}} \hat {p} _ {2} ^ {(0)},
$$

$$
\hat {p} _ {\mathrm {L} 4} - \hat {x} _ {\mathrm {L} 3} = \sqrt {2} e ^ {- r _ {4}} \hat {p} _ {4} ^ {(0)}. \tag {3}
$$

All these linear combinations are proportional to the squeezing factors, approaching zero in the limit of infinite squeezing. Hence, the output state is a linear four-mode cluster state, in agreement with Eq. (1).

The matrix  $U_{\mathrm{L}}$  can be decomposed into  $U_{\mathrm{L}} = F_4S_{12}F_1^{\dagger}B_{34}^{+}(1 / \sqrt{2})B_{21}^{+}(1 / \sqrt{2})B_{23}^{-}(1 / \sqrt{5})F_3F_4$ . Here,  $F_k$  denotes the Fourier transform (90° rotation in phase space) of mode  $k$ ,  $\hat{a}_k \rightarrow i\hat{a}_k$ .  $B_{ij}^{\pm}(t)$  corresponds to a beam splitter transformation of modes  $i$  and  $j$  with transmittance parameter  $t$ ; it is equivalent to the four-mode identity matrix except for  $(B_{ij}^{\pm})_{ii} = t$ ,  $(B_{ij}^{\pm})_{ij} = \sqrt{1 - t^2}$ ,  $(B_{ij}^{\pm})_{ji} = \pm \sqrt{1 - t^2}$  and  $(B_{ij}^{\pm})_{jj} = \mp t$ .  $S_{ij}$  is the swapping operation of modes  $i$  and  $j$ . As a result, two symmetric beam splitters and one 1:4 beam splitter can be used.

Let us consider next the square cluster state. A possible solution for the unitary matrix  $U_{\mathrm{S}}$  is

$$
U _ {\mathrm {S}} = \left( \begin{array}{c c c c} - \frac {1}{\sqrt {2}} & - \frac {1}{\sqrt {1 0}} & - \frac {2 i}{\sqrt {1 0}} & 0 \\ \frac {1}{\sqrt {2}} & - \frac {1}{\sqrt {1 0}} & - \frac {2 i}{\sqrt {1 0}} & 0 \\ 0 & - \frac {2 i}{\sqrt {1 0}} & - \frac {1}{\sqrt {1 0}} & - \frac {1}{\sqrt {2}} \\ 0 & - \frac {2 i}{\sqrt {1 0}} & - \frac {1}{\sqrt {1 0}} & \frac {1}{\sqrt {2}} \end{array} \right). \tag {4}
$$

The correlations of the output state are

$$
\hat {p} _ {\mathrm {S} 1} - \hat {x} _ {\mathrm {S} 3} - \hat {x} _ {\mathrm {S} 4} = - \frac {1}{\sqrt {2}} e ^ {- r _ {1}} \hat {p} _ {1} ^ {(0)} - \sqrt {\frac {5}{2}} e ^ {- r _ {2}} \hat {p} _ {2} ^ {(0)},
$$

$$
\hat {p} _ {\mathrm {S} 2} - \hat {x} _ {\mathrm {S} 3} - \hat {x} _ {\mathrm {S} 4} = \frac {1}{\sqrt {2}} e ^ {- r _ {1}} \hat {p} _ {1} ^ {(0)} - \sqrt {\frac {5}{2}} e ^ {- r _ {2}} \hat {p} _ {2} ^ {(0)},
$$

$$
\hat {p} _ {\mathrm {S} 3} - \hat {x} _ {\mathrm {S} 1} - \hat {x} _ {\mathrm {S} 2} = - \sqrt {\frac {5}{2}} e ^ {- r _ {3}} \hat {p} _ {3} ^ {(0)} - \frac {1}{\sqrt {2}} e ^ {- r _ {4}} \hat {p} _ {4} ^ {(0)},
$$

$$
\hat {p} _ {\mathrm {S} 4} - \hat {x} _ {\mathrm {S} 1} - \hat {x} _ {\mathrm {S} 2} = - \sqrt {\frac {5}{2}} e ^ {- r _ {3}} \hat {p} _ {3} ^ {(0)} + \frac {1}{\sqrt {2}} e ^ {- r _ {4}} \hat {p} _ {4} ^ {(0)}, \tag {5}
$$

all of which approach zero in the limit of infinite squeezing.

We find that the matrix  $U_{\mathrm{S}}$  is equal to  $U_{\mathrm{add}}U_{\mathrm{L}}$ , with  $U_{\mathrm{add}} = \mathrm{diag}(-1, -i, i, 1)$ . Thus, the square cluster state can be obtained from the linear cluster state via local Fourier transforms. In the experiment, the local Fourier transforms can be easily achieved by changing the locking phase of the local oscillator beams. Therefore, the optical setup for the square cluster state is more or less identical to that for the linear cluster state. Using the identities,  $\hat{p}_{\mathrm{S1}} - \hat{x}_{\mathrm{S3}} - \hat{x}_{\mathrm{S4}} = -\hat{p}_{\mathrm{L1}} + \hat{p}_{\mathrm{L3}} - \hat{x}_{\mathrm{L4}}, \quad \hat{p}_{\mathrm{S2}} - \hat{x}_{\mathrm{S3}} - \hat{x}_{\mathrm{S4}} = -\hat{x}_{\mathrm{L2}} + \hat{p}_{\mathrm{L3}} - \hat{x}_{\mathrm{L4}}, \quad \hat{p}_{\mathrm{S3}} - \hat{x}_{\mathrm{S1}} - \hat{x}_{\mathrm{S2}} = \hat{x}_{\mathrm{L1}} - \hat{p}_{\mathrm{L2}} + \hat{x}_{\mathrm{L3}}, \quad \hat{p}_{\mathrm{S4}} - \hat{x}_{\mathrm{S1}} - \hat{x}_{\mathrm{S2}} = \hat{x}_{\mathrm{L1}} - \hat{p}_{\mathrm{L2}} + \hat{p}_{\mathrm{L4}}$ , the measurement of the correlations of the linear cluster state and the square cluster state can be performed in a single experiment.

Finally, the  $\mathsf{T}$ -shape cluster state can be obtained from four  $p$ -squeezed states followed by a unitary transform,

$$
U _ {\mathrm {T}} = \left( \begin{array}{c c c c} \frac {i}{\sqrt {2}} & \frac {1}{2} & \frac {i}{2} & 0 \\ \frac {1}{\sqrt {2}} & \frac {i}{2} & - \frac {1}{2} & 0 \\ 0 & \frac {i}{2} & \frac {1}{2} & \frac {1}{\sqrt {2}} \\ 0 & \frac {i}{2} & \frac {1}{2} & - \frac {1}{\sqrt {2}} \end{array} \right). \tag {6}
$$

This can be also decomposed into  $U_{\mathrm{T}} = F_{1}^{\dagger}B_{34}^{+}(1 / \sqrt{2})B_{21}^{+}(1 / \sqrt{2})B_{32}^{-}(1 / \sqrt{2})F_{2}$ . Thus, this time, the optical setup has to be modified, but three beam splitters are still sufficient. The quantum correlations of the output state are

$$
\hat {p} _ {\mathrm {T 1}} - \hat {x} _ {\mathrm {T 2}} - \hat {x} _ {\mathrm {T 3}} - \hat {x} _ {\mathrm {T 4}} = 2 e ^ {- r _ {2}} \hat {p} _ {2} ^ {(0)},
$$

$$
\hat {p} _ {\mathrm {T 2}} - \hat {x} _ {\mathrm {T 1}} = \sqrt {2} e ^ {- r _ {1}} \hat {p} _ {1} ^ {(0)},
$$

$$
\hat {p} _ {\mathrm {T 3}} - \hat {x} _ {\mathrm {T 1}} = \frac {1}{\sqrt {2}} e ^ {- r _ {2}} \hat {p} _ {2} ^ {(0)} + e ^ {- r _ {3}} \hat {p} _ {3} ^ {(0)} + \frac {1}{\sqrt {2}} e ^ {- r _ {4}} \hat {p} _ {4} ^ {(0)},
$$

$$
\hat {p} _ {\mathrm {T} 4} - \hat {x} _ {\mathrm {T} 1} = \frac {1}{\sqrt {2}} e ^ {- r _ {2}} \hat {p} _ {2} ^ {(0)} + e ^ {- r _ {3}} \hat {p} _ {3} ^ {(0)} - \frac {1}{\sqrt {2}} e ^ {- r _ {4}} \hat {p} _ {4} ^ {(0)}. \tag {7}
$$

They all approach zero in the limit of infinite squeezing. Hence, the output state is a T-shape cluster state, according to Eq. (1). Note that up to local Fourier transforms, the T-shape cluster state is equivalent to a four-mode GHZ-type state [18].

# III. EXPERIMENTAL IMPLEMENTATION

The schematic of our optical setups is shown in Fig. 2. We use a continuous-wave Ti:sapphire laser (Coherent MBR110,  $\lambda = 860\mathrm{nm}$ ) as a light source. In order to generate squeezed states, optical parametric oscillators (OPOs) are used via optical degenerate parametric downconversion. Periodically poled  $\mathrm{KTiOPO_4}$  (PPKTP) crystals are employed as nonlinear optical media. Each OPO is pumped by a second harmonic beam obtained from a cavity which contains a potassium niobate  $(\mathrm{KNbO}_3)$  crystal for second harmonic generation. The pump powers range from 76 to  $96\mathrm{mW}$ .

Weak coherent beams are also injected into the OPOs and the emitted beams are set to  $2\mu \mathrm{W}$ . On each beam, phase modulations are applied for locking, with  $140\mathrm{kHz}$  for OPO2,  $210\mathrm{kHz}$  for OPO3, and  $98\mathrm{kHz}$  for OPO1 and OPO4. In this experiment, a  $1\mathrm{MHz}$  sideband is chosen for the measurements, so the phase modulations do not affect these measurements.

An output state is measured via homodyne detection with a strong beam around  $5\mathrm{mW}$  used as a local oscillator. The homodyne detector gives a voltage signal of the measurement result. After electronically combining the outputs of the

![](images/597c46a9cfc352ab03e0a3b9983c52837fcddcfc194a6bcf95a78db1235461f0.jpg)

![](images/30aa5889acec62eda8feb1736b3065957f4f16fdb71c4d3ccb725db2a3bb94e2.jpg)  
FIG. 2. The schematic of the optical setups to create the linear cluster state (top) and T-shape cluster state (bottom). Four squeezed states are generated by OPOs (optical parametric oscillators). HBS is half beam splitter and  $20\%$  is 1:4 beam splitter. Boxes including  $i$  are Fourier transforms ( $90^{\circ}$  rotations in phase space), and  $-i$  is a  $-90^{\circ}$  rotation. LO is local oscillator for homodyne detection of the output states.

homodyne detectors, the signals of the correlations can be obtained. The signals are sent to a spectrum analyzer in order to get the measurement data.

Figures 3 and 4 show the results of the measurements. Theoretically, the correlations should be proportional to the squeezing levels. Every graph shows the results with squeezing and without squeezing. For the linear cluster state and the square cluster state,  $\langle [\Delta (\hat{p}_{\mathrm{L1}} - \hat{x}_{\mathrm{L2}})]^2\rangle = -5.4\pm 0.2$  dB,  $\langle [\Delta (\hat{p}_{\mathrm{L2}} - \hat{x}_{\mathrm{L1}} - \hat{x}_{\mathrm{L3}})]^2\rangle = \langle [\Delta (\hat{p}_{\mathrm{S3}} - \hat{x}_{\mathrm{S1}} - \hat{x}_{\mathrm{S2}})]^2\rangle = -5.8\pm 0.2$  dB,  $\langle [\Delta (\hat{p}_{\mathrm{L3}} - \hat{x}_{\mathrm{L2}} - \hat{x}_{\mathrm{L4}})]^2\rangle = \langle [\Delta (\hat{p}_{\mathrm{S2}} - \hat{x}_{\mathrm{S3}} - \hat{x}_{\mathrm{S4}})]^2\rangle = -5.3\pm 0.2$  dB,  $\langle [\Delta (\hat{p}_{\mathrm{L4}} - \hat{x}_{\mathrm{L3}})]^2\rangle = -5.8\pm 0.2$  dB,  $\langle [\Delta (\hat{p}_{\mathrm{S1}} - \hat{x}_{\mathrm{S3}} - \hat{x}_{\mathrm{S4}})]^2\rangle = -5.2\pm 0.2$  dB,  $\langle [\Delta (\hat{p}_{\mathrm{S4}} - \hat{x}_{\mathrm{S1}} - \hat{x}_{\mathrm{S2}})]^2\rangle = -5.9\pm 0.2$  dB are obtained. We point out again that only six measurements are sufficient to detect the eight correlations of these two states.

For the T-shape cluster state, the results of the measurements are  $\langle [\Delta (\hat{p}_{\mathrm{T1}} - \hat{x}_{\mathrm{T2}} - \hat{x}_{\mathrm{T3}} - \hat{x}_{\mathrm{T4}})]^2\rangle = -6.0\pm 0.2$  dB,  $\langle [\Delta (\hat{p}_{\mathrm{T2}} - \hat{x}_{\mathrm{T1}})]^2\rangle = -5.2\pm 0.2$  dB,  $\langle [\Delta (\hat{p}_{\mathrm{T3}} - \hat{x}_{\mathrm{T1}})]^2\rangle = -4.9\pm 0.2$  dB and  $\langle [\Delta (\hat{p}_{\mathrm{T4}} - \hat{x}_{\mathrm{T1}})]^2\rangle = -5.2\pm 0.2$  dB.

Various ways for constructing multi-party entanglement witnesses (i.e., observables for detecting the presence of multi-party entanglement) are known in the regime of CV multi-mode states [19,20]. We employ the method of Ref. [19] using a set of sufficient conditions for the full insepara

![](images/8fce5c95e21c09ea8dce710015e65239ee25f2cfaab3ba914bb635e0b62feed6.jpg)

![](images/08ba9da5cae1c166339261921999a0c1810aea4481aca16e215359c72514d66f.jpg)

![](images/611560a42274e46f4d227de7972a3c1c5c78f93192905698909d630dd4447a3a.jpg)

![](images/65c27e56980d7abd480e5a3d20b675cb5dd029e21ed68a80a003542880ac41d5.jpg)

![](images/777623bb12117b4acb8a01caefb7030ca610f01fb46037eeb755a9fa2df29684.jpg)  
FIG. 3. In all graphs, the measurement variances without squeezing (upper) and with squeezing (lower) are shown. The graphs of the first row are the results of  $\langle [\Delta (\hat{p}_{\mathrm{L1}} - \hat{x}_{\mathrm{L2}})]^2\rangle$  and  $\langle [\Delta (\hat{p}_{\mathrm{L2}} - \hat{x}_{\mathrm{L1}} - \hat{x}_{\mathrm{L3}})]^2\rangle = \langle [\Delta (\hat{p}_{\mathrm{S3}} - \hat{x}_{\mathrm{S1}} - \hat{x}_{\mathrm{S2}})]^2\rangle$ . Those of the second row are for  $\langle [\Delta (\hat{p}_{\mathrm{L3}} - \hat{x}_{\mathrm{L2}} - \hat{x}_{\mathrm{L4}})]^2\rangle = \langle [\Delta (\hat{p}_{\mathrm{S2}} - \hat{x}_{\mathrm{S3}} - \hat{x}_{\mathrm{S4}})]^2\rangle$  and  $\langle [\Delta (\hat{p}_{\mathrm{L4}} - \hat{x}_{\mathrm{L3}})]^2\rangle$ , and those of the third row are for  $\langle [\Delta (\hat{p}_{\mathrm{S1}} - \hat{x}_{\mathrm{S3}} - \hat{x}_{\mathrm{S4}})]^2\rangle$  and  $\langle [\Delta (\hat{p}_{\mathrm{S4}} - \hat{x}_{\mathrm{S1}} - \hat{x}_{\mathrm{S2}})]^2\rangle$ . The measurement frequency is  $1\mathrm{MHz}$ , resolution bandwidth is  $30\mathrm{kHz}$ , and video bandwidth is  $300\mathrm{Hz}$ . All results are obtained with 20 times averaging.

![](images/5f04a64e0db6401370807473c36f485b6898d4d0f605ca63602d6cf53ce6c580.jpg)

bility of a multi-mode state which can be easily tested with our experimental results. The corresponding inequalities to be satisfied are shown below. Recall that if the linear cluster state is confirmed to be fully inseparable, the full inseparability of the square cluster state is verified at the same time, as the square and linear cluster states are locally equivalent up to local Fourier transforms. For the linear cluster state, we obtain

$$
\left. \right.\left\langle\left[ \Delta \left(\hat {p} _ {\mathrm {L} 1} - \hat {x} _ {\mathrm {L} 2}\right)\right] ^ {2} \right\rangle + \left\langle\left[ \Delta \left(\hat {p} _ {\mathrm {L} 2} - \hat {x} _ {\mathrm {L} 1} - \hat {x} _ {\mathrm {L} 3}\right)\right] ^ {2} \right\rangle <   1,
$$

$$
\left. \right.\left\langle\left[ \Delta \left(\hat {p} _ {\mathrm {L} 3} - \hat {x} _ {\mathrm {L} 2} - \hat {x} _ {\mathrm {L} 4}\right)\right] ^ {2} \right\rangle + \left\langle\left[ \Delta \left(\hat {p} _ {\mathrm {L} 2} - \hat {x} _ {\mathrm {L} 1} - \hat {x} _ {\mathrm {L} 3}\right)\right] ^ {2} \right\rangle <   1,
$$

$$
\left\langle \left[ \Delta \left(\hat {p} _ {\mathrm {L} 3} - \hat {x} _ {\mathrm {L} 2} - \hat {x} _ {\mathrm {L} 4}\right) \right] ^ {2} \right\rangle + \left\langle \left[ \Delta \left(\hat {p} _ {\mathrm {L} 4} - \hat {x} _ {\mathrm {L} 3}\right) \right] ^ {2} \right\rangle <   1. \tag {8}
$$

For the  $\mathsf{T}$ -shape cluster state, we have

$$
\left. \right.\left\langle\left[ \Delta \left(\hat {p} _ {\mathrm {T} 2} - \hat {x} _ {\mathrm {T} 1}\right)\right] ^ {2} \right\rangle + \left\langle\left[ \Delta \left(\hat {p} _ {\mathrm {T} 1} - \hat {x} _ {\mathrm {T} 2} - \hat {x} _ {\mathrm {T} 3} - \hat {x} _ {\mathrm {T} 4}\right)\right] ^ {2} \right\rangle <   1,
$$

$$
\left\langle \left[ \Delta (\hat {p} _ {\mathrm {T} 3} - \hat {x} _ {\mathrm {T} 1}) \right] ^ {2} \right\rangle + \left\langle \left[ \Delta (\hat {p} _ {\mathrm {T} 1} - \hat {x} _ {\mathrm {T} 2} - \hat {x} _ {\mathrm {T} 3} - \hat {x} _ {\mathrm {T} 4}) \right] ^ {2} \right\rangle <   1,
$$

$$
\langle \left[ \Delta \left(\hat {p} _ {\mathrm {T} 4} - \hat {x} _ {\mathrm {T} 1}\right) \right] ^ {2} \rangle + \langle \left[ \Delta \left(\hat {p} _ {\mathrm {T} 1} - \hat {x} _ {\mathrm {T} 2} - \hat {x} _ {\mathrm {T} 3} - \hat {x} _ {\mathrm {T} 4}\right) \right] ^ {2} \rangle <   1. \tag {9}
$$

Note that the variances of a vacuum state are  $\langle [\Delta \hat{x}_{\mathrm{vac}}]^2\rangle$ $= \langle [\Delta \hat{p}_{\mathrm{vac}}]^2\rangle = \frac{1}{4}$

The values of the left-hand-sides of the inequalities are  $0.34 \pm 0.02$ ,  $0.42 \pm 0.02$ , and  $0.35 \pm 0.02$  for Eq. (8), respectively, and  $0.42 \pm 0.02$ ,  $0.43 \pm 0.02$ , and  $0.42 \pm 0.02$  for Eq. (9), respectively. Thus, all inequalities are simultaneously satisfied and hence the full inseparability of the created cluster states is verified [19].

Besides confirming the inseparability of the cluster states, we also verified that the measured correlations correspond to the squeezing levels of the input states. It is possible to de

![](images/e6ff19992c62f19baaf6cbb657e95cdf69c8df4838d467fdd1e9efce1826e7d8.jpg)

![](images/cb2de64b0cdef93c607dccee430dd82f6c141415307e0c9711325f86d9cb5627.jpg)

![](images/3bad04242b47ddbbfd64dd0189d3c34951c9a216ff4ed6efbc49284884273333.jpg)  
FIG. 4. Upper graphs are  $\langle [\Delta (\hat{p}_{\mathrm{T1}} - \hat{x}_{\mathrm{T2}} - \hat{x}_{\mathrm{T3}} - \hat{x}_{\mathrm{T4}})]^2\rangle$  and  $\langle [\Delta (\hat{p}_{\mathrm{T2}} - \hat{x}_{\mathrm{T1}})]^2\rangle$ . Bottom graphs are  $\langle [\Delta (\hat{p}_{\mathrm{T3}} - \hat{x}_{\mathrm{T1}})]^2\rangle$  and  $\langle [\Delta (\hat{p}_{\mathrm{T4}} - \hat{x}_{\mathrm{T1}})]^2\rangle$ . The conditions of the measurements are the same as in Fig. 3.

![](images/107f5ff9a89426c7c337158cadcae405cac78751d72ea0f0fc9e09e68d39e179.jpg)

tect the squeezing levels by removing the beam splitters. The measured squeezing levels range from  $-5.5$  to  $-6.3\mathrm{dB}$  and the antisqueezing levels are between  $+9.1$  and  $+11.9\mathrm{dB}$ . After removing the beam splitters needed for generating the cluster states, the signal at this stage of the experiment is free of fluctuations in phase locking. Therefore, the squeezing levels are slightly better than the measured correlations. Nonetheless, our results demonstrate the efficient generation of the desired quadrature quantum correlations through cancellation of all antisqueezing components of the light fields involved.

# IV. CONCLUSION

In conclusion, we have demonstrated the generation of three kinds of CV four-mode cluster states. Our method for cluster-state generation is very efficient, because it completely suppresses the presence of antisqueezing components in the output states. Thus, the input squeezing levels are almost perfectly transferred onto the outgoing quadrature quantum correlations.

The approach here can be easily extended to other cluster states, including higher numbers of modes and more complex graph states suitable for multi-mode, multi-step quantum operations. In order to perform a specific quantum op

eration on an input state through one of the cluster states, the input state must be attached to that cluster state. This could be done for arbitrary input states using a QND gate from off-line squeezing. Such a QND gate has been experimentally realized already [21]. For processing the input state, measurements have to be performed on most of the modes of the cluster state. For universal quantum gates, non-Gaussian measurements are needed and, in addition, feedforward operations including active, conditional basis changes between the measurement steps.

With the linear cluster state, single-mode four-step operations are possible. The same state can be also used as a horseshoe cluster for two-mode quantum operations [2]. With the square cluster state, two-mode quantum operations can be performed, and by employing it as a diamond state, it can be used in a redundant encoding scheme for error filtration [5].

# ACKNOWLEDGMENTS

This work was partly supported by SCF and GIA commissioned by the MEXT of Japan, and Research Foundation for Opto-Science and Technology. P.v.L. acknowledges support from the DFG under the Emmy Noether program. The authors acknowledge Seiji Armstrong for assistance with the editing of this paper.

[1] R. Raussendorf and H.-J. Briegel, Phys. Rev. Lett. 86, 5188 (2001).  
[2] P. Walther, K. J. Resch, T. Rudolph, E. Schenck, H. Weinfurter, V. Vedral, M. Aspelmeyer, and A. Zeilinger, Nature (London) 434, 169 (2005).  
[3] N. C. Menicucci, P. van Loock, M. Gu, C. Weedbrook, T. C. Ralph, and M. A. Nielsen, Phys. Rev. Lett. 97, 110501 (2006).  
[4] J. Zhang and S. L. Braunstein, Phys. Rev. A 73, 032318 (2006).  
[5] P. van Loock, Christian Weedbrook, and Mile Gu, Phys. Rev. A 76, 032321 (2007).  
[6] N. C. Menicucci, S. T. Flammia, H. Zaidi, and O. Pfister, Phys. Rev. A 76, 010302(R) (2007).  
[7] H. Zaidi, N. C. Menicucci, S. T. Flammia, R. Bloomer, M. Pysher, and O. Pfister, Laser Phys. 18, 659 (2008).  
[8] P. van Loock, J. Opt. Soc. Am. B 24, 340 (2007).  
[9] H. Yonezawa, T. Aoki, and A. Furusawa, Nature (London) 431, 430 (2004).  
[10] N. Takei, H. Yonezawa, T. Aoki, and A. Furusawa, Phys. Rev. Lett. 94, 220502 (2005).  
[11] H. Yonezawa, S. L. Braunstein, and A. Furusawa, Phys. Rev.

Lett. 99, 110503 (2007).  
[12] H. Yonezawa, A. Furusawa, and P. van Loock, Phys. Rev. A 76, 032305 (2007).  
[13] M. Yukawa, H. Benichi, and A. Furusawa, Phys. Rev. A 77, 022314 (2008).  
[14] S. L. Braunstein, Phys. Rev. A 71, 055801 (2005).  
[15] X. Su, A. Tan, X. Jia, J. Zhang, C. Xie, and K. Peng, Phys. Rev. Lett. 98, 070502 (2007).  
[16] A. Tan, Y. Wang, X. Jin, X. Su, X. Jia, J. Zhang, C. Xie, and K. Peng, e-print arXiv:quant-ph/0803.1724.  
[17] M. Reck, A. Zeilinger, H. J. Bernstein, and P. Bertani, Phys. Rev. Lett. 73, 58 (1994).  
[18] P. van Loock and S. L. Braunstein, Phys. Rev. Lett. 84, 3482 (2000).  
[19] P. van Loock and A. Furusawa, Phys. Rev. A 67, 052315 (2003).  
[20] P. Hyllus and J. Eisert, New J. Phys. 8, 51 (2006).  
[21] J. Yoshikawa, Y. Miwa, A. Huck, U. L. Andersen, P. van Loock, and A. Furusawa, Technical Digest of CLEO/QELS2008, QThK6 (Optical Society of America, San Jose, 2008).