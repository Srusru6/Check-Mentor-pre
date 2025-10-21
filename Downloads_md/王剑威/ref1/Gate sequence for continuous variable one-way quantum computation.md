ARTICLE

Received 6 Aug 2013 | Accepted 28 Oct 2013 | Published 25 Nov 2013

DOI: 10.1038/ncomms3828

OPEN

# Gate sequence for continuous variable one-way quantum computation

Xiaolong Su<sup>1</sup>, Shuhong Hao<sup>1</sup>, Xiaowei Deng<sup>1</sup>, Lingyu Ma<sup>1</sup>, Meihong Wang<sup>1</sup>, Xiaojun Jia<sup>1</sup>, Changde Xie<sup>1</sup> & Kunchi Peng<sup>1</sup>

Measurement-based one-way quantum computation using cluster states as resources provides an efficient model to perform computation and information processing of quantum codes. Arbitrary Gaussian quantum computation can be implemented sufficiently by long single-mode and two-mode gate sequences. However, continuous variable gate sequences have not been realized so far due to an absence of cluster states larger than four submodes. Here we present the first continuous variable gate sequence consisting of a single-mode squeezing gate and a two-mode controlled-phase gate based on a six-mode cluster state. The quantum property of this gate sequence is confirmed by the fidelities and the quantum entanglement of two output modes, which depend on both the squeezing and controlled-phase gates. The experiment demonstrates the feasibility of implementing Gaussian quantum computation by means of accessible gate sequences.

Measurement-based one-way quantum computation (QC) performs computation by measurement and classical feedforward on a multipartite cluster entangled state<sup>1</sup>. One-way QC was first demonstrated using four-photon cluster states<sup>2,3</sup>. Besides photonic systems<sup>2-6</sup>, other QC systems with discrete quantum variables, such as ionic<sup>7-10</sup>, superconducting<sup>11-15</sup> and solid state<sup>16-18</sup> systems, have been investigated.

In parallel, the theoretical and experimental explorations on one-way continuous variable (CV) QC have also been developed[19-30]. In contrast to the probabilistic generation of photonic qubits in most cases, CV cluster states are produced in an unconditional fashion and thus the one-way QC with CV cluster states can be implemented deterministically[27-34]. Although individual single-mode and two-mode logical gates towards implementing multimode Gaussian transformation in a one-way CVQC fashion have been experimentally demonstrated by using four-mode cluster entangled states of light[27-30], CV gate sequences consisting of different single logical elements, which are necessary for realizing practical QC, have not been reported up to now. It is now important to investigate the gate sequences for QC as sufficiently large cluster states have recently been prepared, including eight-photon[35,36], eight-quantum mode[37,38] and up to 10,000-quantum mode[39] optical cluster states.

Here, we design and experimentally accomplish a CV gate sequence, in which a single-mode squeezing gate and a two-mode controlled-phase (CZ) gate are cascaded. A vacuum optical input signal is first squeezed by the squeezing gate and successively the squeezed output enters the CZ gate as one of its two inputs. A vacuum state or a squeezed state of light produced by an off-line nondegenerate optical parametric amplifier (NOPA) is used for the other CZ gate input. The experimental result shows that after two independent input states are transformed by the gate sequence, the two output states produced are entangled and their fidelities are better than that obtained by using coherent states as resources. Our experiments also prove that the entanglement degree and the fidelity depend simultaneously on two cascaded logical gates, which manifests the sequence feature of the presented system. Apart from the gate sequences only involving multimode Gaussian transformation, a non-Gaussian operation is required at least[19] for demonstrating universal one-way CVQC. Many theoretical protocols and schemes on the universal CVQC have been proposed[19,20].

# Results

Preparation of six-mode CV cluster states. CV cluster states are defined as $^{21,22}$

$$
\hat {p} _ {a} - \sum_ {b \in N _ {a}} \hat {x} _ {b} \equiv \hat {\delta} _ {a} \rightarrow 0, a \in G. \tag {1}
$$

In the limit of infinite squeezing, the  $N$ -mode cluster states are a simultaneous zero eigenstate of the  $N$  linear combinations in equation (1). Here the amplitude  $(\hat{x})$  and phase  $(\hat{p})$  quadratures of an optical mode  $\hat{a}$  are defined as  $\hat{x} = (\hat{a} + \hat{a}^{\dagger}) / 2$  and  $\hat{p} = (\hat{a} - \hat{a}^{\dagger}) / 2i$ . The modes  $a \in G$  denote the vertices of the graph  $G$ , while the modes  $b \in N_a$  are the nearest neighbours of mode  $\hat{a}$ . One time measurement on the cluster state cannot destroy the entanglement totally, which means that cluster states have strong properties of entanglement persistence.

A general way to build CV cluster states is to implement an appropriate unitary transformation  $(U)$  on a series of input  $\hat{p}$ -squeezed states,  $\hat{a}_l = e^{+r}\hat{x}_l^{(0)} + ie^{-r}\hat{p}_l^{(0)}$ , where  $r$  is the squeezing parameter,  $\hat{x}^{(0)}$  and  $\hat{p}^{(0)}$  represent the quadratures of a vacuum state, which has a noise variance  $\langle \Delta^2\hat{x}^{(0)}\rangle = \langle \Delta^2\hat{p}^{(0)}\rangle = 1/4$ . According to a general linear optics transformation

$\hat{b}_k = \sum_l U_{kl} \hat{a}_l$ , the output modes can be obtained[22]. The transformation matrix  $U$  can be decomposed into a network of beam-splitters, which corresponds to the experimental system for generating the required CV cluster state. We designed the beam-splitter network for producing CV six-mode linear cluster states with three NOPAs, as shown in Fig. 1. A NOPA can simultaneously generate a  $\hat{x}$ -squeezed state and a  $\hat{p}$ -squeezed state[40]. The three  $\hat{x}$ -squeezed states and three  $\hat{p}$ -squeezed states prepared by the three NOPAs, are denoted by  $\hat{a}_1, \hat{a}_3, \hat{a}_5$ ,  $\hat{a}_m = e^{-r} \hat{x}_m^{(0)} + ie^{+r} \hat{p}_m^{(0)}$ ,  $(m = 1, 3, 5)$  for  $\hat{x}$ -squeezed states, and  $\hat{a}_2, \hat{a}_4, \hat{a}_6$ ,  $\hat{a}_n = e^{+r} \hat{x}_n^{(0)} + ie^{-r} \hat{p}_n^{(0)}$ ,  $(n = 2, 4, 6)$  for  $\hat{p}$ -squeezed states, respectively. Here we have assumed that all squeezed states produced by the three NOPAs have identical squeezing degree due to the equality of their configuration (see Methods). We deduce the transformation matrix for generating CV six-mode linear cluster state using three  $\hat{x}$ -squeezed states and three  $\hat{p}$ -squeezed states as input states, which is given by[22]

$$
U _ {6} = \left( \begin{array}{c c c c c c} \frac {i}{\sqrt {2}} & \frac {i}{\sqrt {3}} & - \sqrt {\frac {2}{3 9}} & - \sqrt {\frac {3}{2 6}} & 0 & 0 \\ \frac {- 1}{\sqrt {2}} & \frac {1}{\sqrt {3}} & i \sqrt {\frac {2}{3 9}} & i \sqrt {\frac {3}{2 6}} & 0 & 0 \\ 0 & \frac {i}{\sqrt {3}} & 2 \sqrt {\frac {2}{3 9}} & \sqrt {\frac {6}{1 3}} & 0 & 0 \\ 0 & 0 & - i \sqrt {\frac {6}{1 3}} & 2 i \sqrt {\frac {2}{3 9}} & \frac {- 1}{\sqrt {3}} & 0 \\ 0 & 0 & \sqrt {\frac {3}{2 6}} & - \sqrt {\frac {2}{3 9}} & \frac {i}{\sqrt {3}} & \frac {i}{\sqrt {2}} \\ 0 & 0 & i \sqrt {\frac {3}{2 6}} & - i \sqrt {\frac {2}{3 9}} & \frac {- 1}{\sqrt {3}} & \frac {1}{\sqrt {2}} \end{array} \right). \tag {2}
$$

The matrix can be decomposed into  $U_{6} = F_{1}I_{2}(-1)F_{3}F_{4}$ ,  $F_{5}I_{6}(-1)B_{56}^{+}(1 / 2)F_{5}B_{12}^{+}(1 / 2)B_{45}^{+}(1 / 3)F_{5}B_{23}^{+}(1 / 3)F_{3}B_{34}^{-}(9 / 13)$ , where  $F_{k}$  denotes the Fourier transformation of mode  $k$ , which corresponds to a  $90^{\circ}$  rotation in the phase space;  $B_{kl}^{\pm}\left(T_{j}\right)$  stands for the linearly optical transformation on the  $j$ th beam-splitter with the transmission of  $T_{j}$  ( $j = 1,\ldots,5$ ), where  $\left(B_{kl}^{\pm}\right)_{kk} = \sqrt{1 - T}, \left(B_{kl}^{\pm}\right)_{kl} = \sqrt{T}, \left(B_{kl}^{\pm}\right)_{lk} = \pm \sqrt{T}$ , and  $\left(B_{kl}^{\pm}\right)_{ll} = \mp \sqrt{1 - T}$ , are elements of beam-splitter matrix.  $I_{k}(-1) = e^{i\pi}$  corresponds to a  $180^{\circ}$  rotation of mode  $k$  in phase space. When the transmissions of the five beam-splitters are chosen as  $T_{1} = 9 / 13$ ,  $T_{2} = T_{3} = 1 / 3$ ,  $T_{4} = T_{5} = 1 / 2$ ,

![](images/737e1fdacd31e3866b423bae819924330a71a0d20a82f6c6dfab2d78a22ad9a3.jpg)  
Figure 1 | Schematic of six-mode CV cluster state generation system. T: transmission efficient of beam splitter. Boxes including an  $i$  are Fourier transforms (90° rotations in phase space), and -1 is a 180° rotation. LO, local oscillation beam; HD, homodyne detector.

the six output optical modes construct a six-mode CV linear cluster state. The corresponding excess noise terms for each mode of the CV six-mode linear cluster state are respectively denoted by

$$
\hat {\delta} _ {1} = \sqrt {2} e ^ {- r} \hat {x} _ {1} ^ {(0)},
$$

$$
\hat {\delta} _ {2} = \sqrt {3} e ^ {- r} \hat {p} _ {2} ^ {(0)},
$$

$$
\hat {\delta} _ {3} = \frac {1}{\sqrt {2}} e ^ {- r} \hat {x} _ {1} ^ {(0)} + \sqrt {\frac {1 3}{6}} e ^ {- r} \hat {p} _ {4} ^ {(0)} + \frac {1}{\sqrt {3}} e ^ {- r} \hat {x} _ {5} ^ {(0)},
$$

$$
\hat {\delta} _ {4} = \frac {1}{\sqrt {3}} e ^ {- r} \hat {p} _ {2} ^ {(0)} - \sqrt {\frac {1 3}{6}} e ^ {- r} \hat {x} _ {3} ^ {(0)} + \frac {1}{\sqrt {2}} e ^ {- r} \hat {p} _ {6} ^ {(0)},
$$

$$
\hat {\delta} _ {5} = \sqrt {3} e ^ {- r} \hat {x} _ {5} ^ {(0)},
$$

$$
\hat {\delta} _ {6} = \sqrt {2} e ^ {- r} \hat {p} _ {6} ^ {(0)}. \tag {3}
$$

Obviously, in the ideal case with infinite squeezing  $(r\to \infty)$ , these excess noises will vanish and the better the squeezing, the smaller the noise term will be.

Figure 2 shows the experimental results of the six-mode CV cluster state. Red and black lines correspond to shot-noise level (SNL) and quantum correlation noise, respectively. The measured noises are  $\langle \Delta^2 (\hat{p}_1 - \hat{x}_2)\rangle = -4.04\pm 0.09\mathrm{dB}$ ,  $\langle \Delta^2 (\hat{p}_2 - \hat{x}_1 - \hat{x}_3)\rangle = -4.22\pm$ $0.10\mathrm{dB}$ ,  $\langle \Delta^2 (\hat{p}_3 - \hat{x}_2 - \hat{x}_4)\rangle = -3.80\pm 0.10\mathrm{dB}$ ,  $\langle \Delta^2 (\hat{p}_4 - \hat{x}_3 -$ $\hat{x}_5)\rangle = -3.72\pm 0.09\mathrm{dB}$ ,  $\langle \Delta^2 (\hat{p}_5 - \hat{x}_4 - \hat{x}_6)\rangle = -4.05\pm 0.10\mathrm{dB},$  and  $\langle \Delta^2 (\hat{p}_6 - \hat{x}_5)\rangle = -4.03\pm 0.09\mathrm{dB}$ , respectively.

According to the inseparability criteria for CV multipartite entangled states proposed by van Loock and Furusawa $^{41}$ , we deduced the inseparability criteria for CV six-partite linear cluster

state, which are

$$
\left\langle \Delta^ {2} \left(\hat {p} _ {1} - \hat {x} _ {2}\right) \right\rangle + \left\langle \Delta^ {2} \left(\hat {p} _ {2} - \hat {x} _ {1} - \hat {x} _ {3}\right) \right\rangle <   1, \tag {4}
$$

$$
\left\langle \Delta^ {2} \left(\hat {p} _ {2} - \hat {x} _ {1} - \hat {x} _ {3}\right) \right\rangle + \left\langle \Delta^ {2} \left(\hat {p} _ {3} - \hat {x} _ {2} - \hat {x} _ {4}\right) \right\rangle <   1, \tag {5}
$$

$$
\left\langle \Delta^ {2} \left(\hat {p} _ {3} - \hat {x} _ {2} - \hat {x} _ {4}\right) \right\rangle + \left\langle \Delta^ {2} \left(\hat {p} _ {4} - \hat {x} _ {3} - \hat {x} _ {5}\right) \right\rangle <   1, \tag {6}
$$

$$
\left\langle \Delta^ {2} \left(\hat {p} _ {4} - \hat {x} _ {3} - \hat {x} _ {5}\right) \right\rangle + \left\langle \Delta^ {2} \left(\hat {p} _ {5} - \hat {x} _ {4} - \hat {x} _ {6}\right) \right\rangle <   1, \tag {7}
$$

$$
\left\langle \Delta^ {2} \left(\hat {p} _ {5} - \hat {x} _ {4} - \hat {x} _ {6}\right) \right\rangle + \left\langle \Delta^ {2} \left(\hat {p} _ {6} - \hat {x} _ {5}\right) \right\rangle <   1. \tag {8}
$$

Substituting the measured quantum noise (Fig. 2) into equations (4)-(8), we can calculate the combinations of the correlation variances, which are 0.48, 0.59, 0.63, 0.62 and 0.50, respectively. As all these values are smaller than the boundary of 1, the prepared six quantum modes satisfy the inseparability criteria and form a six-mode cluster entangled state.

Configuration of the gate sequence. As shown in Fig. 3a, we demonstrate the gate sequence of a squeezing gate and a CZ gate using a six-mode cluster state as ancillary state. First, we perform the squeezing gate on input mode  $\alpha$  (target mode) to produce a phase-squeezed state. Then a CZ gate is performed on the output mode from the squeezing gate and the other input mode  $\beta$  (control mode) coming from outside of the sequence.

The single-mode squeezing gate is expressed by  $\hat{S}(r_s) = e^{ir_s(\hat{x}\hat{p} +\hat{p}\hat{x})}$ . The input-output relation of the single-mode squeezing gate is  $\hat{\xi}_j' = \mathbf{S}\hat{\xi}_j$ , where  $\hat{\xi}_j = (\hat{x}_j,\hat{p}_j)^T$  and

$$
\mathbf {S} = \left( \begin{array}{c c} e ^ {r _ {s}} & 0 \\ 0 & e ^ {- r _ {s}} \end{array} \right) \tag {9}
$$

represents the squeezing operation on phase quadrature. The CV CZ gate corresponds to the unitary operator  $\hat{C}_{Zjk} = e^{2i\hat{x}_j\hat{x}_k}$  with

![](images/250e2856fe7f1182722155639c9467059fc776a866dbf68c72027e4af5c1c813.jpg)

![](images/bc80e995f43b7b6aafe9462ecbdaf3f685216800c4418869e55d2b17b5a19dd9.jpg)

![](images/87ac7cd128ebf9a3e67c5d82bdd0aab886d482bf3e2a3bd9f2b9263bb08891dd.jpg)  
Figure 2 | Measured correlation noises of six-mode CV cluster state. Panels a-f are noise powers of  $\langle \Delta^2 (\hat{p}_1 - \hat{x}_2)\rangle$ ,  $\langle \Delta^2 (\hat{p}_2 - \hat{x}_1 - \hat{x}_3)\rangle$ ,  $\langle \Delta^2 (\hat{p}_3 - \hat{x}_2 - \hat{x}_4)\rangle$ ,  $\langle \Delta^2 (\hat{p}_4 - \hat{x}_3 - \hat{x}_5)\rangle$ ,  $\langle \Delta^2 (\hat{p}_5 - \hat{x}_4 - \hat{x}_6)\rangle$  and  $\langle \Delta^2 (\hat{p}_6 - \hat{x}_5)\rangle$ , respectively. The red and black lines in all plots are shot-noise level and correlation variances, respectively. Measurement frequency is  $2\mathrm{MHz}$ , the spectrum analyser resolution bandwidth is  $30\mathrm{kHz}$  and the video bandwidth is  $100\mathrm{Hz}$ .

![](images/422a638cc0d1c224937e0a870959103c99ee61b661e485236f807909bc1c74ff.jpg)

![](images/b86384500c65249bc454b45714868908782a7fdb271ab9a22afb65f84f140879.jpg)

![](images/fb38b4b3f30aea6c36459fbee48ed57a76b6d866f6606a81a9cc3d1771b79663.jpg)

![](images/5616ff8ce8cf634f95adc81a33500a3cfb49f4b94f3ebb6a2432a0407844f895.jpg)  
a

![](images/3c4ef5d7d2097177635e6d321a593f2b699904ecff587e6c4a8942be3b88b47d.jpg)  
b  
Figure 3 | Schematic of the gate sequence. (a) The graph representation. The input state  $\alpha$  is coupled to a six-mode CV cluster state C1-C2-C3-C4-C5-C6. Squeezing operation is performed on input mode  $\alpha$ , then CZ gate is performed on the input state  $\beta$  and output of the squeezing operation. (b) Schematic of the experimental setup. The input states  $\alpha$  and  $\beta$  are coupled to a six-mode CV cluster state via  $50\%$  beam-splitter  $(50\% R)$ . Measurement results from HD systems are fed forward to modes C4 and C5. The output modes  $\mu$  and  $\nu$  are measured by two HD systems. EOMx and EOMp: amplitude and phase EOM.  $99\% R$ , a mirror with  $99\%$  reflection coefficient.

the input-output relation,

$$
\hat {\xi} _ {j k} ^ {\prime} = \left( \begin{array}{c c} \mathbf {I} & \mathbf {C} \\ \mathbf {C} & \mathbf {I} \end{array} \right) \hat {\xi} _ {j k}, \tag {10}
$$

where  $\hat{\xi}_{jk} = \left(\hat{x}_j,\hat{p}_j,\hat{x}_k,\hat{p}_k\right)^T$

$$
\mathbf {C} = \left( \begin{array}{c c} 0 & 0 \\ 1 & 0 \end{array} \right), \tag {11}
$$

and  $\mathbf{I}$  is a  $2\times 2$  identity matrix.

The transformation matrix of the gate sequence is given by

$$
\mathbf {U} = \left( \begin{array}{c c} \mathbf {I} & \mathbf {C} \\ \mathbf {C} & \mathbf {I} \end{array} \right). \left( \begin{array}{c c} \mathbf {S} & 0 \\ 0 & \mathbf {I} \end{array} \right). \tag {12}
$$

The input-output relation of the gate sequence is expressed by  $\hat{\xi}_{\mu \nu} = \mathbf{U}\xi_{\alpha \beta}$  in the ideal case. However, in any practical cases, the excess noise coming from imperfect entanglement of the CV cluster state will inevitably affect the performances of the logical gates, thus a noise term  $\hat{\delta}$  should be added, that is

$$
\hat {\xi} _ {\mu \nu} = \mathbf {U} \hat {\xi} _ {\alpha \beta} + \hat {\delta}, \tag {13}
$$

where  $\hat{\delta} = \left(\hat{\delta}_1 - \hat{\delta}_3, \hat{\delta}_4 - \hat{\delta}_2 - \hat{\delta}_6, -\hat{\delta}_6, \hat{\delta}_1 + \hat{\delta}_5 - \hat{\delta}_3\right)$  represents all excess noises of the gate sequence.

The schematic of experimental setup is shown in Fig. 3b. A six-mode cluster state involving six submodes C1, C2, C3, C4, C5 and

C6 with the squeezing about  $-4.0\mathrm{dB}$  on average is used as the resource (ancillary) state. The input states  $\alpha$  and  $\beta$  are coupled to submodes C1 and C6 by two  $50\%$  beam-splitters, respectively. The measurement results of the output modes from the two  $50\%$  beam-splitters as well as the submodes C2 and C3 are feedforward to submodes C4 and C5 through classical feedforward circuits. In the operation of gate sequence, the measured observables are  $\hat{x}_{d1} = [\cos \theta_{1}(\hat{x}_{\alpha} - \hat{x}_{1}) + \sin \theta_{1}(\hat{p}_{\alpha} - \hat{p}_{1})] / \sqrt{2}, \hat{x}_{d2} = [\cos \theta_{2}(\hat{x}_{\alpha} + \hat{x}_{1}) + \sin \theta_{2}(\hat{p}_{\alpha} + \hat{p}_{1})] / \sqrt{2}, \hat{p}_{2}, \hat{p}_{3}, \hat{x}_{d3} = (\hat{x}_{\beta} - \hat{p}_{6}) / \sqrt{2}$  and  $\hat{p}_{d4} = (\hat{p}_{\beta} - \hat{x}_6) / \sqrt{2}$ . The measurement angle  $\theta_{1}$  and  $\theta_{2}$  in the homodyne detection for  $\hat{x}_{d1}$  and  $\hat{x}_{d2}$  determine the squeezing operation according to the transformation matrix

$$
\mathbf {S} = \left( \begin{array}{c c} \cot \theta_ {2} & 0 \\ 0 & \tan \theta_ {2} \end{array} \right), \tag {14}
$$

if we choose  $\theta_{2} = -\theta_{1}$ .  $\mathbf{S}$  corresponds to a single-mode amplitude and phase squeezing gate when  $\cot \theta_{2} = e^{-r_{s}}$  and  $e^{r_{s}}$ , respectively. The measurement angles  $(\theta_{1},\theta_{2})$  for  $0\mathrm{dB}$ ,  $-3\mathrm{dB}$ ,  $-6\mathrm{dB}$ ,  $-9\mathrm{dB}$  and  $-12\mathrm{dB}$  squeezing are  $(-45.00^{\circ}, 45.00^{\circ})$ ,  $(-35.30^{\circ}, 35.30^{\circ})$ ,  $(-26.62^{\circ}, 26.62^{\circ})$ ,  $(-19.54^{\circ}, 19.54^{\circ})$ , and  $(-14.10^{\circ}, 14.10^{\circ})$ , respectively. These measurement results are feedforwarded to the amplitude and phase quadratures of modes C4 and C5 via electro-optical modulators (EOM), respectively. The corresponding feedforward operation is expressed by  $\hat{X}_{C4}(f1)\hat{Z}_{C4}(f2)\hat{X}_{C5}(f3)\hat{Z}_{C5}(f4)$ , where  $\hat{X}_j(s) = e^{-2is\hat{p}_j}$  and  $\hat{Z}_j(s) = e^{2is\hat{x}_j}$  are the amplitude and phase displacement operators, respectively,  $f1 = -\hat{p}_3 + \frac{\csc\theta_2}{\sqrt{2}}\hat{x}_{d1} + \frac{\csc\theta_2}{\sqrt{2}}\hat{x}_{d2}, f2 = -\hat{p}_2 + \sqrt{2}\hat{x}_{d3} - \frac{\sec\theta_2}{\sqrt{2}}\hat{x}_{d1} + \frac{\sec\theta_2}{\sqrt{2}}\hat{x}_{d2}, f3 = \sqrt{2}\hat{x}_{d3}$ , and  $f4 = -\hat{p}_3 + \sqrt{2}\hat{p}_{d4} + \frac{\csc\theta_2}{\sqrt{2}}\hat{x}_{d1} + \frac{\csc\theta_2}{\sqrt{2}}\hat{x}_{d2}$ . The output modes are detected by two homodyne detection systems. The quadrature components of the output modes for the gate sequence are given by

$$
\begin{array}{l} \left( \begin{array}{c} \hat {x} _ {\mu} \\ \hat {p} _ {\mu} \\ \hat {x} _ {\nu} \\ \hat {p} _ {\nu} \end{array} \right) = \left( \begin{array}{c} \hat {x} _ {C 4} \\ \hat {p} _ {C 4} \\ \hat {x} _ {C 5} \\ \hat {p} _ {C 5} \end{array} \right) + G \left(\left( \begin{array}{c} \hat {p} _ {3} \\ \hat {p} _ {2} \\ \sqrt {2} \hat {x} _ {d 3} \\ \sqrt {2} \hat {p} _ {d 4} \end{array} \right) - \left( \begin{array}{c c} \frac {\csc \theta_ {2}}{\sqrt {2}} & \frac {\csc \theta_ {3}}{\sqrt {2}} \\ \frac {- \sec \theta_ {2}}{\sqrt {2}} & \frac {\sec \theta_ {3}}{\sqrt {2}} \\ 0 & 0 \\ 0 & 0 \end{array} \right) \left( \begin{array}{c} \hat {x} _ {d 1} \\ \hat {x} _ {d 2} \end{array} \right)\right) \\ = \left( \begin{array}{l l l l} 1 & 0 & 0 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c c c c} \cot \theta_ {2} & 0 & 0 & 0 \\ 0 & \tan \theta_ {2} & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c} \hat {x} _ {\alpha} \\ \hat {p} _ {\alpha} \\ \hat {x} _ {\beta} \\ \hat {p} _ {\beta} \end{array} \right) + \left( \begin{array}{c} \hat {\delta} _ {1} - \hat {\delta} _ {3} \\ - \hat {\delta} _ {6} + \hat {\delta} _ {4} - \hat {\delta} _ {2} \\ - \hat {\delta} _ {6} \\ \hat {\delta} _ {5} - \hat {\delta} _ {3} + \hat {\delta} _ {1} \end{array} \right), \tag {15} \\ \end{array}
$$

where

$$
G = \left( \begin{array}{r r r r} - 1 & 0 & 0 & 0 \\ 0 & - 1 & 1 & 0 \\ 0 & 0 & 1 & 0 \\ - 1 & 0 & 0 & 1 \end{array} \right) \tag {16}
$$

is the feedforward gain factor. From equations (14) and (15) we obtain

$$
\hat {x} _ {\mu} = \hat {x} _ {\alpha} e ^ {r _ {s}} + \hat {\delta} _ {1} - \hat {\delta} _ {3},
$$

$$
\hat {p} _ {\mu} = \hat {p} _ {\alpha} e ^ {- r _ {s}} + \hat {x} _ {\beta} - \hat {\delta} _ {2} + \hat {\delta} _ {4} - \hat {\delta} _ {6},
$$

$$
\hat {x} _ {v} = \hat {x} _ {\beta} - \hat {\delta} _ {6},
$$

$$
\hat {p} _ {\nu} = \hat {p} _ {\beta} + \hat {x} _ {\alpha} e ^ {r _ {s}} + \hat {\delta} _ {1} + \hat {\delta} _ {5} - \hat {\delta} _ {3}. \tag {17}
$$

After a vacuum signal  $(\alpha)$  passes through the squeezing gate, its phase  $(\hat{p}_{\alpha})$  and amplitude  $(\hat{x}_{\alpha})$  are squeezed  $(\hat{p}_{\alpha}e^{-r_s})$  and antisqueezed  $(\hat{x}_{\alpha}e^{r_s})$ , respectively. Then, the squeezed signal passes through the CZ gate, as the usual result of CZ gate<sup>30</sup>, the anti-squeezed amplitude signal is transformed into the phase

quadrature  $(\hat{p}_v)$  of the resultant output mode v and its amplitude quadrature  $(\hat{x}_v)$  keeps unchanging in the ideal case without excess noises  $(\delta_{1 - 6} = 0)$ .

Experimental results. As a CZ gate is a two-mode entangling gate, its quantum character can be verified by the sufficient condition of inseparability for a two-mode state $^{42}$ , that is

$$
\left\langle \Delta^ {2} \left(g \hat {p} _ {\mu} - \hat {x} _ {\nu}\right) \right\rangle + \left\langle \Delta^ {2} \left(g \hat {p} _ {\nu} - \hat {x} _ {\mu}\right) \right\rangle <   g, \tag {18}
$$

where  $g$  is the optimal gain factor, which makes the left side of the inequality minimum. By calculating the minimal value of equation (18), the optimal gain is obtained

$$
\frac {e ^ {2 r _ {\beta}} \left(3 + 2 e ^ {2 r} + e ^ {2 r + 2 r _ {\beta}} + e ^ {2 r} \cot^ {2} \theta_ {2}\right)}{8 e ^ {2 r _ {\beta}} + e ^ {2 r + 4 r _ {\beta}} + e ^ {2 r + 2 r _ {\beta}} \left(\cot^ {2} \theta_ {2} + \tan^ {2} \theta_ {2}\right)}, \tag {19}
$$

where  $r_{\beta}$  is the squeezing parameter of the input mode  $\beta$ . Figure 4 shows the dependence of entanglement degree between the two output states of the gate sequence on squeezing degree of the squeezing gate with an input vacuum mode  $\alpha$  for three different  $\beta$  states (blue: vacuum state, red:  $-4$  dB phase-squeezed state, yellow:  $-12$  dB phase-squeezed state). The entanglement degree is quantified by  $E = \langle \Delta^{2}(g\hat{p}_{\mu} - \hat{x}_{\nu})\rangle +\langle \Delta^{2}(g\hat{p}_{\nu} - \hat{x}_{\mu})\rangle -g.$  When  $E < 0$ , the entanglement exists and the smaller the  $E$ , the stronger the entanglement. The solid and dashed lines correspond to  $-4$  and  $-6$  dB squeezing of the six-mode cluster state, respectively. All traces are plotted according to the real loss in our experimental system (see Methods). We can see that the entanglement degree between the output states ( $\mu$  and  $\nu$ ) not only depends on the operation of CZ gate, but also is controlled by the squeezing operation of the squeezing gate. For a given  $\beta$  state, when the squeezing of the squeezing gate increases, the entanglement degree of the output states increases. On the other hand, the operation of the CZ gate also depends on the features of the  $\beta$  state. The phase squeezing of the  $\beta$  state will improve the entanglement degree of the output modes. Of course, the largest influence to the capacity of the gate sequence comes from the quality of the resource state. When the squeezing of the six-mode cluster state increases from  $-4$  dB (solid lines) to  $-6$  dB (dashed lines), the entanglement degree of the output states will be significantly improved. As  $-4$  dB cluster squeezing is available in our experiment, the obtained maximal entanglement degree

![](images/618e8d75fda171a64593ced821caade7b28502116a17899406dc2fbf207d207f.jpg)  
Figure 4 | Dependence of entanglement on squeezing of the squeezing gate. The dependence of the entanglement between the gate sequence output modes on the squeezing of the squeezing gate is plotted here. The blue, red and yellow lines correspond to the input mode  $\beta$  being a vacuum state,  $-4\mathrm{dB}$  and  $-12\mathrm{dB}$  phase-squeezed state, respectively. The solid and dashed lines correspond to  $-4\mathrm{dB}$  and  $-6\mathrm{dB}$  squeezing of the six-mode cluster state, respectively. The black dots represent the experimental data. Error bars represent  $\pm$  one s.d. and are obtained based on the statistics of the measured noise variances.

is only  $-0.005$  for the case of using two vacuum states to be  $\alpha$  and  $\beta$  (solid blue line). If  $\beta$  is a phase-squeezed state (red and yellow lines), the entanglement will increase for the same squeezing degree of the squeezing gate and an identical resource state. The experimentally measured data points obtained under different measurement angles of the squeezing gate are marked by little black dots with error bars, which shows that the experimental results are in reasonable agreement with the theoretical expectation. The experimentally measured entanglement degrees, fidelities and corresponding optimal gain factors are listed in Table 1. The entanglement degree of the output modes depends on both operations of two cascaded gates, which clearly shows that the final results are decided by the gate sequence.

Figure 5 shows the measured noise variances of the quadratures  $(\hat{x}_{\mu},\hat{p}_{\mu},\hat{x}_{\nu},$  and  $\hat{p}_v)$  of the output modes  $(\mu$  and  $\nu$  with a vacuum mode  $\alpha$  and a phase-squeezed state  $\beta$  with squeezing of  $-4\mathrm{dB}$  as two inputs of the gate sequence, where  $-12\mathrm{dB}$  squeezing is implemented on input  $\alpha$  . In the ideal case with the cluster state of infinite squeezing (yellow lines), the noise powers of  $\hat{x}_{\mu}$  and  $\hat{x}_{\nu}$  are 12 and  $4\mathrm{dB}$  above the SNL (black lines), which correspond to the anti-squeezing noises resulting from the

Table 1 | Entanglement and fidelity at experimentally measured data points.  

<table><tr><td>Data point</td><td>g</td><td>E</td><td>Fμ</td><td>Fν</td></tr><tr><td>a</td><td>0.72</td><td>0.112 ± 0.026</td><td>0.832 ± 0.011</td><td>0.873 ± 0.013</td></tr><tr><td>b</td><td>0.81</td><td>0.053 ± 0.033</td><td>0.882 ± 0.011</td><td>0.902 ± 0.014</td></tr><tr><td>c</td><td>0.87</td><td>0.023 ± 0.026</td><td>0.905 ± 0.009</td><td>0.942 ± 0.012</td></tr><tr><td>d</td><td>0.92</td><td>0.004 ± 0.027</td><td>0.888 ± 0.009</td><td>0.951 ± 0.011</td></tr><tr><td>e</td><td>0.95</td><td>-0.005 ± 0.024</td><td>0.886 ± 0.012</td><td>0.956 ± 0.009</td></tr><tr><td>f</td><td>0.83</td><td>0.040 ± 0.026</td><td>0.860 ± 0.013</td><td>0.854 ± 0.013</td></tr><tr><td>g</td><td>0.90</td><td>-0.033 ± 0.029</td><td>0.903 ± 0.014</td><td>0.891 ± 0.013</td></tr><tr><td>h</td><td>0.94</td><td>-0.085 ± 0.024</td><td>0.922 ± 0.009</td><td>0.934 ± 0.009</td></tr><tr><td>i</td><td>0.96</td><td>-0.103 ± 0.031</td><td>0.932 ± 0.011</td><td>0.950 ± 0.010</td></tr><tr><td>j</td><td>0.98</td><td>-0.124 ± 0.022</td><td>0.923 ± 0.006</td><td>0.947 ± 0.006</td></tr></table>

a-e:  $\alpha$  and  $\beta$  are vacuum state, squeezing of the squeezing gate are  $0$ ,  $-3$ ,  $-6$ ,  $-9$  and  $-12\mathrm{dB}$ , respectively. f-j:  $\alpha$  is a vacuum state,  $\beta$  is a  $-4\mathrm{dB}$  phase-squeezed state, squeezing of the squeezing gate are  $0$ ,  $-3$ ,  $-6$ ,  $-9$  and  $-12\mathrm{dB}$ , respectively.

![](images/d462ff1836dc91ede54cf9089ba7d60c43597c39c0ae35ca227eebe6b379d4a6.jpg)  
Figure 5 | Experimentally measured noise powers. The measured noise powers of the output modes with a vacuum and a phase-squeezed state as inputs are plotted here. Black lines are SNL, blue and red lines are output noise power without and with cluster state as ancillary state, yellow lines are ideal output noise power. Squeezing degree of the squeezing gate is  $-12\mathrm{dB}$ . Measurement frequency is  $2\mathrm{MHz}$ , the spectrum analyser resolution bandwidth is  $30\mathrm{kHz}$  and the video bandwidth is  $100\mathrm{Hz}$ .

squeezing gate (12 dB) and the input phase-squeezed state (4 dB), respectively. The noise powers of  $\hat{p}_{\mu}$  and  $\hat{p}_{\nu}$  are 4.1 and  $12.1\mathrm{dB}$  above the SNL due to the effect of CZ gate (see equation (17)). The blue and red lines stand for the output noises without and with the cluster state as ancillary state, respectively. The blue lines are obtained by using a coherent light of identical intensity to replace each of cluster submodes. In this case, the measured values of  $\hat{x}_{\mu}$ ,  $\hat{p}_{\mu}$ ,  $\hat{x}_{\nu}$ , and  $\hat{p}_{\nu}$  are  $12.75 \pm 0.07$ ,  $9.05 \pm 0.09$ ,  $7.76 \pm 0.08$  and  $13.07 \pm 0.09\mathrm{dB}$  above the SNL, respectively. The noise variances of  $\hat{x}_{\mu}$ ,  $\hat{p}_{\mu}$ ,  $\hat{x}_{\nu}$ , and  $\hat{p}_{\nu}$  measured with the existence of the cluster state (red lines) are  $12.34 \pm 0.11$ ,  $7.60 \pm 0.13$ ,  $6.84 \pm 0.12$  and  $12.55 \pm 0.13\mathrm{dB}$  above the SNL, respectively, all of which are lower than the corresponding values without using the cluster resource.

To further verify the general input-output relation of the gate sequence, we employ a coherent state with a 15 dB modulation signal as input state (Fig. 6a-d). Figure 6a shows the noise powers of quadratures of the output modes  $\mu$  and  $\nu$  when input modes  $\alpha$  and  $\beta$  are a coherent state with nonzero amplitude of  $15\mathrm{dB}$  ( $\hat{x}_{\alpha}$ -coherent) and a vacuum state, respectively. The measured noise variance of  $\hat{x}_{\mu}$  (red line) is  $27.01 \pm 0.13\mathrm{dB}$  above SNL (black lines). That is because  $12\mathrm{dB}$  anti-squeezing noise resulting from the squeezing gate is added on the  $15\mathrm{dB}$  input amplitude of  $\hat{x}_{\alpha}$ . In the ideal case (yellow lines), the noise variance of  $\hat{p}_{\mu}$  is a little higher than SNL as  $\hat{x}_{\nu}$  is added on the squeezed noise of  $-12\mathrm{dB}$  and the noise variance of  $\hat{x}_{\nu}$  is at the level of SNL. The measured noise powers of  $\hat{p}_{\mu}$  and  $\hat{x}_{\nu}$  is about  $4.43 \pm 0.16$  and  $2.68 \pm 0.18\mathrm{dB}$  above the SNL because of the effect of excess noises coming from the imperfect entanglement of the cluster state. The measured noise variance of  $\hat{p}_{\nu}$  is  $27.02 \pm 0.11\mathrm{dB}$  above the SNL because the amplitude on  $\hat{x}_{\mu}$  is added to  $\hat{p}_{\nu}$ , which satisfies the input-output relation of the CZ logic gate in equation (17). Figure 6b shows the noise powers of output modes when a coherent state with a modulation signal of  $15\mathrm{dB}$  on  $\hat{p}_{\alpha}$  ( $\hat{p}_{\alpha}$ -coherent) and a vacuum state are used for the input states  $\alpha$  and  $\beta$ , respectively. The measured noise power (red lines) of  $\hat{x}_{\mu}$  is  $12.34 \pm 0.17\mathrm{dB}$

above the corresponding SNL (black line) because of the effect of anti-squeezing noise resulting from the squeezing gate. The noise powers of  $\hat{p}_{\mu}$  and  $\hat{x}_{\nu}$  (red lines) are  $6.72 \pm 0.12 \mathrm{~dB}$  and  $2.68 \pm 0.12 \mathrm{~dB}$  above the corresponding SNL, respectively. The noise power of  $\hat{p}_{\nu}$  is  $12.68 \pm 0.14 \mathrm{~dB}$  above the SNL because the noise of  $\hat{x}_{\mu}$  is added on  $\hat{p}_{\nu}$  (see equation (17)). Figure 6c,d are the noise powers of output modes when the input is the coherent state with the modulation signal of  $15 \mathrm{~dB}$  on  $\hat{x}_{\beta}$  and  $\hat{p}_{\beta}$  ( $\hat{x}_{\beta}$ -coherent and  $\hat{p}_{\beta}$ -coherent), respectively. It is obvious that the measured noise powers of output modes satisfy the input-output relation of the gate sequence in equation (17).

Figure 7 shows the measured correlation noise variances of the output modes with a vacuum mode  $(\alpha)$  and a  $-4\mathrm{dB}$  phase-squeezed mode  $(\beta)$  as the inputs of the sequence, where  $-12\mathrm{dB}$  squeezing is implemented on input  $\alpha$ . The measured noise variance (red lines) of  $\left\langle \Delta^2\left(g\hat{p}_\mu -\hat{x}_\nu\right)\right\rangle$  (a) and  $\left\langle \Delta^2\left(g\hat{p}_\nu -\hat{x}_\mu\right)\right\rangle$  (b) are  $0.53\pm 0.11$  and  $0.65\pm 0.11$  dB below the corresponding SNL (black lines), respectively. The entanglement is quantified by

$$
\left\langle \Delta^ {2} \left(g \hat {p} _ {\mu} - \hat {x} _ {v}\right) \right\rangle + \left\langle \Delta^ {2} \left(g \hat {p} _ {v} - \hat {x} _ {\mu}\right) \right\rangle = 0. 8 5 6 \pm 0. 0 2 2. \tag {20}
$$

For our experimental system, the calculated optimal gain factor is  $g = 0.98$ . The total correlation variances in the left side of equation (18) are smaller than  $g$  and thus satisfy the inseparability criteria, which confirms the quantum entanglement between the two output modes ( $\mu$  and  $\nu$ ) from the gate sequence.

We also use fidelity  $F = \{\mathrm{Tr}[(\sqrt{\hat{\rho}_1}\hat{\rho}_2\sqrt{\hat{\rho}_1})^{1 / 2}]\} ^2$ , which denotes the overlap between the experimentally obtained output state  $\hat{\rho}_{2}$  and the ideal output sate  $\hat{\rho}_{1}$ , to quantify the performance of the gate sequence. The fidelity for two Gaussian states  $\hat{\rho}_{1}$  and  $\hat{\rho}_{2}$  with covariance matrices  $\mathbf{A}_j$  and mean amplitudes  $\alpha_{j}\equiv (\alpha_{jx},\alpha_{jp})$ $(j = 1,2)$  is expressed by43,44

$$
F = \frac {2}{\sqrt {\Delta + \sigma} - \sqrt {\sigma}} \exp \left[ - \epsilon^ {T} \left(\mathbf {A} _ {1} + \mathbf {A} _ {2}\right) ^ {- 1} \epsilon \right], \tag {21}
$$

where  $\Delta = \operatorname*{det}(\mathbf{A}_1 + \mathbf{A}_2),\quad \sigma = (\operatorname*{det}\mathbf{A}_1 - 1)(\operatorname*{det}\mathbf{A}_2 - 1),\quad \epsilon = \alpha_2 - \alpha_1,$ $\mathbf{A}_1$  and  $\mathbf{A}_2$  for the ideal  $(\hat{\rho}_1)$  and experimental  $(\hat{\rho}_2)$

![](images/4dad68ceed68b2534dd02ea75720d3dd5accb4218988717ec683f2a998fddbf0.jpg)

![](images/b8b52ec4406f6311a2608c9ea37d02475c93800162a1d72237d96ba56e96232c.jpg)  
Figure 6 | Experimentally measured noise powers of the output modes with coherent inputs. (a-d):  $\hat{x}_{\alpha}$ ,  $\hat{p}_{\alpha}$ ,  $\hat{x}_{\beta}$  and  $\hat{p}_{\beta}$ -coherent state as input, respectively. Black lines are SNL, red lines are output noise power with cluster state as ancillary state, yellow lines are ideal output noise power. Squeezing degree of the squeezing gate is  $-12$  dB. Measurement frequency is  $2\mathrm{MHz}$ . The spectrum analyser resolution bandwidth is  $30\mathrm{kHz}$  and the video bandwidth is  $100\mathrm{Hz}$ .

![](images/3b61ab919d5e7175601dc6a2a78654da1d45d7e24400314f66d91b2d87471076.jpg)

![](images/b2ed528590147ef145599607925745c3037378d192439d49c85a7ddfc3830c80.jpg)

output states, respectively. The covariance matrices  $\mathbf{A}_j$ $(j = 1,2)$  for target mode are given by

$$
\mathbf {A} _ {\mu 1} = 4 \left[ \begin{array}{c c} \left\langle \Delta^ {2} \hat {x} _ {\mu} \right\rangle_ {1} & 0 \\ 0 & \left\langle \Delta^ {2} \hat {p} _ {\mu} \right\rangle_ {1} \end{array} \right], \tag {22}
$$

$$
\mathbf {A} _ {\mu 2} = 4 \left[ \begin{array}{c c} \left\langle \Delta^ {2} \hat {x} _ {\mu} \right\rangle_ {2} & 0 \\ 0 & \left\langle \Delta^ {2} \hat {p} _ {\mu} \right\rangle_ {2} \end{array} \right]. \tag {23}
$$

The coefficient '4' comes from the normalization of SNL. As the noise of a vacuum state is defined as  $1/4$ , while in the fidelity formula the vacuum noise is normalized to '1', a coefficient '4' appears in the expressions of covariance matrices. Similarly, we

![](images/e77592b2855c009de58468ffc8a908db8df1e57755cdbc1ffe6077b778847ada.jpg)  
Figure 7 | Measured quantum correlation variances. This figure shows the measured quantum correlation variances of the output modes of the gate sequence with a vacuum state and a phase-squeezed state as inputs. a and b are noise power of  $\langle \Delta^2 (g\hat{p}_\mu -\hat{x}_\nu)\rangle$  and  $\langle \Delta^2 (g\hat{p}_\nu -\hat{x}_\mu)\rangle$ , respectively. Black and red lines are SNL and quantum correlation noise, respectively. Squeezing degree of the squeezing gate is  $-12\mathrm{dB}$ . Measurement frequency is  $2\mathrm{MHz}$ , the spectrum analyser resolution bandwidth is  $30\mathrm{kHz}$  and the video bandwidth is  $100\mathrm{Hz}$ .

![](images/d62bac8d5ecb980d03f2a0049652bf99dd3792c76fbd528a30d9e1da404da1c9.jpg)

can write out the covariance matrices for the control mode

$$
\mathbf {A} _ {v 1} = 4 \left[ \begin{array}{c c} \left\langle \Delta^ {2} \hat {x} _ {v} \right\rangle_ {1} & 0 \\ 0 & \left\langle \Delta^ {2} \hat {p} _ {v} \right\rangle_ {1} \end{array} \right], \tag {24}
$$

$$
\mathbf {A} _ {v 2} = 4 \left[ \begin{array}{c c} \left\langle \Delta^ {2} \hat {x} _ {v} \right\rangle_ {2} & 0 \\ 0 & \left\langle \Delta^ {2} \hat {p} _ {v} \right\rangle_ {2} \end{array} \right]. \tag {25}
$$

In case of infinite squeezing, both fidelities for the target and control states,  $F_{\mu}$  and  $F_{\nu}$ , equal to 1, which can be calculated from equation (17) with  $r \to \infty$ .

Figure 8 gives the fidelities of the output modes  $\mu$  and  $\nu$ , as the function of squeezing degree of the squeezing gate based on the experimental data for two different input  $\beta$  states (Fig. 8a is a vacuum state; Fig. 8b is a  $-4$  dB phase-squeezed state). In Fig. 8, black and red lines correspond to fidelity of output modes  $\mu$  and  $\nu$ , respectively. Dashed lines are obtained at the case without the use of the cluster resource (using the coherent states in the same intensity to substitute the cluster states in Fig. 3) and solid lines are completed under the case using the cluster resource state. Obviously, when the cluster state is applied, the fidelity of the output states is higher than that obtained at the case using the coherent state, which is usually called the classical limit in quantum optics. The experimentally measured data (see Table 1) are marked in Fig. 8a,b, and are in reasonable agreement with the theoretical calculation.

# Discussion

We demonstrated a gate sequence in one-way QC fashion by applying a six-mode CV cluster state as quantum resource. The quantum feature of the gate sequence is verified quantitatively by both the inseparability criterion of two-mode entanglement and the fidelities of output states. The entanglement degree of two output modes depends on two cascaded gates, simultaneously, which exhibits the sequence character of the system. Although in our experiment only two gates are linked together, the scheme can be easily extended to construct any large QC gate sequence with a number of gates.

Today, quantum computers have become a physical reality and are continuing to be developed. One-way QC based on quantum teleportation $^{23,24}$  is able to implement secure information processing and accomplish the unbreakable quantum coding $^{45,46}$ . On the other hand, the large cluster states can be prepared only by linearly optical systems if appropriate squeezed states are available. Thus, one-way quantum computers consisting

![](images/254e64522dd55cd7443a6416abc1e5e42e2b70e060d24b8242913d04e63d1968.jpg)  
Figure 8 | Dependence of fidelity on squeezing of the squeezing gate. a and b are the fidelity for the input mode  $\beta$  as a vacuum state and a -4 dB phase-squeezed state, respectively. The solid and dashed lines correspond to fidelity with and without cluster resource, respectively. Black and red lines present the fidelity of output modes  $\mu$  and  $\nu$ , respectively. Error bars represent  $\pm$  one s.d. and are obtained based on the statistics of the measured noise variances.

![](images/f7e1caad92216be547abeda74eef54abb14e1554f21464789d96d7ebc82c2215.jpg)

![](images/dccc0685e355612de868ca011b41be278ffef55c34c7b8a32820e98b55f52345.jpg)  
Figure 9 | Schematic of reverse blind CVQC. The quantum server prepares squeezed states and sends them to any clients in demand. Client prepares CV cluster state with linear optics and then implements quantum computation via measurements and feedforwards on the prepared cluster state.

of this type of gate sequences can be operated in a reverse blind CVQC model to realize the secure QC network (Fig. 9), in which only a server owns the ability of preparing quantum states (such as squeezed states) and all remote clients ask the server to send them necessary squeezed states through a quantum channel $^{47}$ . Then, clients produce the cluster states using linearly optical transformation and perform arbitrary CV one-way Gaussian QC by means of classical measurements and feedforwards on the prepared cluster state at their stations. In this way, the server and any eavesdroppers never know what clients want to do, thus the security of the blind QC is guaranteed by no-signaling principle $^{48}$ . The presented gate sequence for one-way Gaussian CVQC is an essential experimental exploration towards developing universal QC and practical quantum networks.

# Methods

Experimental details. The three  $\hat{x}$ -squeezed and three  $\hat{p}$ -squeezed states are produced by three NOPAs. These NOPAs are pumped by a common laser source, which is a continuous wave intracavity frequency-doubled and frequency-stabilized Nd:YAP/LBO(Nd-doped  $\mathrm{YAlO}_3$  perorskite/lithium triborate) $^{49}$ . The output fundamental wave at  $1,080\mathrm{nm}$  wavelength from the laser is used for the injected signals of NOPAs and the local oscillators of the homodyne detectors. The output second harmonic wave at  $540\mathrm{nm}$  wavelength serves as the pump field of all NOPAs, in which a pair of signal and idler modes with the identical frequency at  $1,080\mathrm{nm}$  and the orthogonal polarizations are generated through an intracavity frequency-down-conversion process $^{50}$ . Each of NOPAs consists of an  $\alpha$ -cut type-II KTP crystal and a concave mirror $^{50}$ . The front face of the KTP was coated to be used for the input coupler and the concave mirror serves as the output coupler of the squeezed states, which is mounted on a piezo-electric transducer (PZT) for locking actively the cavity length of NOPA on resonance with the injected signal at  $1,080\mathrm{nm}$ . The transmissions of the input coupler at  $540\mathrm{nm}$  and  $1,080\mathrm{nm}$  are  $99.8\%$  and  $0.04\%$ , respectively. The transmissions of the output coupler at  $540\mathrm{nm}$  and  $1,080\mathrm{nm}$  are  $0.5\%$  and  $5.2\%$ , respectively. The finesse of the NOPA for  $540\mathrm{nm}$  and  $1,080\mathrm{nm}$  are 3 and 117, respectively. In our experiment, all NOPAs are operated at the parametric deamplification situation, that is, the phase difference between the pump field and the injected signal is  $(2n + 1)\pi$  ( $n$  is an integer). Under this condition, the coupled modes at  $+45^{\circ}$  and  $-45^{\circ}$  polarization directions are the quadrature amplitude and the quadrature phase-squeezed states, respectively $^{31,40}$ .

Three NOPAs are locked individually by means of Pound-Drever-Hall method with a phase modulation of  $56\mathrm{MHz}$  on  $1,080\mathrm{nm}$  laser beam[51]. In the experiment, the relative phase  $(2n + 1)\pi$  locking is completed with a lock-in amplifier, where a signal around  $15\mathrm{kHz}$  is modulated on the pump light by the PZT mounted on a reflection mirror, which is placed in the optical path of the pump laser and then the error signal is fed back to the other PZT, which is mounted on a mirror placed in the optical path of the injected beam. In the beam-splitter network used to prepare six-mode cluster states, the relative phase between two incident beams on  $T_{1}$  and  $T_{4}$  is phase-locked to zero, and that on  $T_{2}, T_{3}$  and  $T_{5}$  is phase-locked to  $\pi / 2$ . The zero phase difference  $(T_{1}$  and  $T_{4})$  between two interfered beams on a beam-splitter is locked by a lock-in amplifier. The  $\pi / 2$  phase difference  $(T_{2}, T_{3}$  and  $T_{5})$  is locked by DC locking technique, where the photocurrent signal of the interference fringe is fed back to the PZT mounted on a mirror, which is placed before the beam-splitter. In the homodyne detection system, zero phase difference

for the measurement of quadrature amplitude is locked by Pound-Drever-Hall technique with a phase modulation of  $10.9\mathrm{MHz}$  on local oscillator beam. The  $\pi /2$  phase for the measurement of quadrature phase is locked with DC locking technique too.

The transmission efficiency of an optical beam from NOPA to a homodyne detector is around  $96\%$ . The quantum efficiency of a photodiode (FD500W-1064, Fermionics) used in the homodyne detection system is  $95\%$ . The interference efficiency on a beam-splitter is about  $99\%$ . The phase fluctuation of the phase locking system is about  $2 - 3^{\circ}$ .

# References

1. Raussendorf, R. & Briegel, H. J. A one-way quantum computer. Phys. Rev. Lett. 86, 5188-5191 (2001).  
2. Walther, P. et al. Experimental one-way quantum computing. Nature 434, 169-176 (2005).  
3. Chen, K. et al. Experimental realization of one-way quantum computing with two-photon four-qubit cluster states. Phys. Rev. Lett. 99, 120503 (2007).  
4. O'Brien, J. L., Pryde, G. J., White, A. G., Ralph, T. C. & Branning, D. Demonstration of an all-optical quantum controlled-not gate. Nature 426, 264-267 (2003).  
5. OBrien, J. L., Furusawa, A. & Vučković, J. Photonic quantum technologies. Nat. Photon. 3, 687-695 (2009).  
6. Tokunaga, Y., Kuwashiro, S., Yamamoto, T., Koashi, M. & Imoto, N. Generation of high-fidelity four-photon cluster state and quantum-domain demonstration of oneway quantum computing. Phys. Rev. Lett. 100, 210501 (2008).  
7. Cirac, J. I. & Zoller, P. Quantum computations with cold trapped ions. Phys. Rev. Lett. 74, 4091-4094 (1995).  
8. Monroe, C., Meekhof, D. M., King, B. E., Itano, W. M. & Wineland, D. J. Demonstration of a fundamental quantum logic gate. Phys. Rev. Lett. 75, 4714-4717 (1995).  
9. Kielpinski, D., Monroe, C. & Wineland, D. J. Architecture for a large-scale ion-trap quantum computer. Nature 417, 709-711 (2002).  
10. Kim, K. et al. Quantum simulation of frustrated Ising spins with trapped ions. Nature 465, 590-593 (2010).  
11. Makhlin, Y., Schön, G. & Shnirman, A. Quantum-state engineering with Josephson-junction devices. Rev. Mod. Phys. 73, 357-400 (2001).  
12. Yamamoto, T., Pashkin, Y. A., Astafiev, O., Nakamura, Y. & Tsai, J. S. Demonstration of conditional gate operation using superconducting charge qubits. Nature 425, 941-944 (2003).  
13. Neeley, M. et al. Emulation of a quantum spin with a superconducting phase qudit. Science 325, 722-725 (2009).  
14. DiCarlo, L. et al. Demonstration of two-qubit algorithms with a superconducting quantum processor. Nature 460, 240-244 (2009).  
15. Bialczak, R. C. et al. Quantum process tomography of a universal entangling gate implemented with Josephson phase qubits. Nat. Phys. 6, 409-413 (2010).  
16. Berezovsky, J., Mikkelsen, M. H., Stoltz, N. G., Coldren, L. A. & Awschalom, D. D. Picosecond coherent optical manipulation of a single electron spin in a quantum dot. Science 320, 349-352 (2008).  
17. Fushman, I. et al. Controlled phase shifts with a single quantum dot. Science 320, 769-772 (2008).  
18. Hanson, R. & Awschalom, D. D. Coherent manipulation of single spins in semiconductors. Nature 453, 1043-1049 (2008).  
19. Menicucci, N. C. et al. Universal quantum computation with continuous-variable cluster states. Phys. Rev. Lett. 97, 110501 (2006).  
20. Weedbrook, C. et al. Gaussian quantum information. Rev. Mod. Phys. 84, 621-669 (2012).  
21. Zhang, J. & Braunstein, S. L. Continuous-variable Gaussian analog of cluster states. Phys. Rev. A. 73, 032318 (2006).  
22. van Loock, P., Woodbrook, C. & Gu, M. Building Gaussian cluster states by linear optics. Phys. Rev. A. 76, 032321 (2007).  
23. van Loock, P. Examples of Gaussian cluster computation. J. Opt. Soc. Am. B. 24, 340-346 (2007).  
24. Gu, M., Weedbrook, C., Menicucci, N. C., Ralph, T. C. & van Loock, P. Quantum computing with continuous-variable clusters. Phys. Rev. A. 79, 062318 (2009).  
25. Zwierz, M., Pérez-Delgado, C. A. & Kok, P. Unifying parameter estimation and the Deutsch-Jozsa algorithm for continuous variables. Phys. Rev. A. 82, 042320 (2010).  
26. Ferrini, G., Gazeau, J. P., Coudreau, T., Fabre, C. & Treps, N. Compact Gaussian quantum computation by multi-pixel homodyne detection. New J. Phys. 15, 093015 (2013).  
27. Miwa, Y., Yoshikawa, J., van Loock, P. & Furusawa, A. Demonstration of a universal one-way quantum quadratic phase gate. Phys. Rev. A. 80, 050303(R) (2009).  
28. Wang, Y. et al. Toward demonstrating controlled-X operation based on continuous-variable four-partite cluster states and quantum teleporters. Phys. Rev. A. 81, 022311 (2010).

29. Ukai, R. et al. Demonstration of unconditional one-way quantum computations for continuous variables. Phys. Rev. Lett. 106, 240504 (2011).  
30. Ukai, R., Yokoyama, S., Yoshikawa, J., van Loock, P. & Furusawa, A. Demonstration of a controlled-phase gate for continuous-variable one-way quantum computation. Phys. Rev. Lett. 107, 250501 (2011).  
31. Su, X. et al. Experimental preparation of quadripartite cluster and Greenberger-Horne-Zeilinger entangled states for continuous variables. Phys. Rev. Lett. 98, 070502 (2007).  
32. Yukawa, M., Ukai, R., van Loock, P. & Furusawa, A. Experimental generation of four-mode continuous-variable cluster states. Phys. Rev. A. 78, 012301 (2008).  
33. Tan, A. et al. Experimental generation of genuine four-partite entangled states with total three-party correlation for continuous variables. Phys. Rev. A. 78, 013828 (2008).  
34. Pysher, M., Miwa, Y., Shahrokhshahi, R., Bloomer, R. & Pfister, O. Parallel generation of quadripartite cluster entanglement in the optical frequency comb. Phys. Rev. Lett. 107, 030505 (2011).  
35. Huang, Y.-F. et al. Experimental generation of an eight-photon Greenberger-- Horne--Zeilinger state. Nat. Commun. 2, 546 (2011).  
36. Yao, X.-C. et al. Observation of eight-photon entanglement. Nat. Photon. 6, 225-228 (2012).  
37. Su, X. et al. Experimental preparation of eight-partite cluster state for photonic qumodes. Opt. Lett. 37, 5178-5180 (2012).  
38. Armstrong, S. et al. Programmable multimode quantum networks. Nat. Commun. 3, 1026 (2012).  
39. Yokoyama, S. et al. Optical generation of ultra-large-scale continuous-variable cluster states. Preprint at http://arxiv.org/abs/1306.3366v1 (2013).  
40. Zhang, Y. et al. Experimental generation of bright two-mode quadrature squeezed light from a narrow-band nondegenerate optical parametric amplifier. Phys. Rev. A. 62, 023813 (2000).  
41. van Loock, P. & Furusawa, A. Detecting genuine multipartite continuous-variable entanglement. Phys. Rev. A. 67, 052315 (2003).  
42. Duan, L., Giedke, G., Cirac, J. I. & Zoller, P. Inseparability criterion for continuous variable systems. Phys. Rev. Lett. 84, 2722-2725 (2000).  
43. Nha, H. & Carmichael, H. J. Distinguishing two single-mode Gaussian states by homodyne detection: an information-theoretic approach. Phys. Rev. A. 71, 032336 (2005).  
44. Scutaru, H. Fidelity for displaced squeezed thermal states and the oscillator semigroup. J. Phys. A. 31, 3659-3663 (1998).

45. Broadbent, A., Fitzsimons, J. & Kashefi, E. in Proceedings of the 50th Annual IEEE Symposium on Foundations of Computer Science 517-527 (IEEE Computer Society, Los Alamitos, USA, 2009).  
46. Barz, S. et al. Demonstration of blind quantum computing. Science 335, 303-308 (2012).  
47. Morimae, T. & Fujii, K. Blind quantum computation in which Alice only makes measurements. Phys. Rev. A. 87, 050301(R) (2013).  
48. Popescu, S. & Rohrlich, D. Quantum nonlocality as an axiom. Found. Phys. 24, 379-385 (1994).  
49. Wang, Y., Zheng, Y., Xie, C. & Peng, K. High-power low-noise Nd:YAP/LBO laser with dual wavelength outputs. IEEE J. Quantum Elect. 47, 1006-1013 (2011).  
50. Wang, Y. et al. Experimental generation of 6 dB continuous variable entanglement from a nondegenerate optical parametric amplifier. Opt. Express 18, 6149-6155 (2010).  
51. Drever, R. W. P. et al. Laser phase and frequency stabilization using an optical resonator. Appl. Phys. B. 31, 97-105 (1983).

# Acknowledgements

This research was supported by the National Basic Research Program of China (Grant No. 2010CB923103), NSFC (Grant Nos. 11174188, 61121064) and OIT.

# Author contributions

X.S. and C.X. conceived the original idea. X.S. and K.P. designed the experiment. X.S., S.H. and X.D. constructed and performed the experiment. L.M. and M.W. participated in part of the experiment. X.S., S.H. and X.J. accomplished theoretical calculation and the data analyses. X.S., C.X. and K.P. wrote the paper.

# Additional information

Conflict of interests: The authors declare no competing financial interest.

Reprints and permission information is available online at http://npg.nature.com/reprintsandpermissions/

How to cite this article: Su, X. et al. Gate sequence for continuous variable one-way quantum computation. Nat. Commun. 4:2828 doi: 10.1038/ncomms3828 (2013).

![](images/09c5c3d6b926e4054ac06b58ea3b2b99617bd88f0313eff35f6809200e290684.jpg)

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. To view a copy of http://creativecommons.org/licenses/by-nc-sa/3.0/