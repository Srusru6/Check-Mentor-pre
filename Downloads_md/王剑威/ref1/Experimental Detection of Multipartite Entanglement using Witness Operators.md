# Experimental Detection of Multipartite Entanglement using Witness Operators

Mohamed Bourennane, $^{1,2}$  Manfred Eibl, $^{1,2}$  Christian Kurtsiefer, $^{2}$  Sascha Gaertner, $^{1,2}$  Harald Weinfurter, $^{1,2}$  Ottfried Gühne, $^{3}$  Philipp Hyllus, $^{3}$  Dagmar Bruß, $^{3}$  Maciej Lewenstein, $^{3}$  and Anna Sanpera $^{3}$ $^{1}$ Max-Planck-Institut für Quantenoptik, D-85748 Garching, Germany  
 $^{2}$ Sektion Physik, Ludwig-Maximilians-Universität, D-80797 München, Germany  
 $^{3}$ Institut für Theoretische Physik, Universität Hannover, D-30167 Hannover, Germany  
(Received 31 August 2003; published 26 February 2004)

We present the experimental detection of genuine multipartite entanglement using entanglement witness operators. To this aim, we introduce a canonical way of constructing and decomposing witness operators so that they can be directly implemented with present technology. We apply this method to three- and four-qubit entangled states of polarized photons, giving experimental evidence that the considered states contain true multipartite entanglement.

DOI: 10.1103/PhysRevLett.92.087902

Entanglement is one of the most puzzling features of quantum theory and of great importance for the new field of quantum information theory. The determination of whether a given state is entangled or not is one of the most challenging open problems of this field. For the experimental detection of entanglement Bell inequalities [1] are widely used. However, even for two-qubit systems there exist entangled states which do not violate any Bell inequality [2]. The tool of choice in this case is the Peres-Horodecki criterion [3,4] as it gives a simple sufficient and necessary condition for entanglement. Yet, the situation is much more complicated for higher dimensional and multipartite systems, where simple necessary and sufficient conditions are not known [5].

In the analysis of multipartite systems, it is important to distinguish between genuine multipartite entanglement and biseparable (triseparable, etc.) entanglement. Genuine multipartite entangled pure states cannot be created without participation of all parties. Conversely, for pure biseparable states of  $n$  parties, a group of  $m < n$  parties can be found which are entangled among each other, but not with any member of the other group of  $n - m$  parties [6]. Distinction and detection of genuine multipartite entanglement poses an important challenge in quantum information science. Bell inequalities are not suited to this aim in general. Multiseparable and biseparable states violate known Bell inequalities less than  $n$ -partite Greenberger-Horne-Zeilinger (GHZ) states. However, for  $n > 3$ , there exist even pure  $n$ -partite entangled states with a lower violation than biseparable states [7]. Only recently, significant progress in classifying multipartite entanglement has been achieved using entanglement witnesses [4,8]. These observables can always be used to detect various forms of multipartite entanglement, when some a priori knowledge about the states under investigation is provided [9]; they are in this sense more powerful than Bell inequalities.

A witness of genuine  $n$ -partite entanglement is an observable which has a positive expectation value on states with  $n - 1$  partite entanglement and a negative expecta

PACS numbers: 03.67.Mn, 03.65.Ud, 42.50.Dv

tion value on some  $n$ -partite entangled states. The latter states and their entanglement, respectively, are said to be detected by  $\mathcal{W}$ . Witnesses provide sufficient criteria for entanglement and for distinguishing the various classes of genuine multipartite entangled states.

The goal of this Letter is twofold. First, we introduce a general scheme for the construction of multipartite witness operators and their decomposition into locally measurable observables. In this way, we demonstrate how witness operators can be implemented experimentally in a straightforward way by using local projective measurements, even for multipartite systems [10]. Then, we apply this scheme to certain states and perform the experimental detection of their multipartite entanglement, which could not be revealed by known Bell inequalities. In particular, we use this method for the characterization of the three-qubit  $W$  state [11], and the four-qubit state  $|\Psi^{(4)}\rangle$  [12].

A witness operator that detects genuine multipartite entanglement of a pure state  $|\psi \rangle$  (and of states that are close to  $|\psi \rangle$ , e.g., in the presence of noise) is given by

$$
\mathcal {W} = \alpha \mathbb {1} - | \psi \rangle \langle \psi |, \tag {1}
$$

where  $\mathbb{1}$  is the identity operator,

$$
\alpha = \max  _ {| \phi \rangle \in B} | \langle \phi | \psi \rangle | ^ {2}, \tag {2}
$$

and  $B$  denotes the set of biseparable states. This construction guarantees that  $\mathrm{Tr}(\mathcal{W}\rho_B) \geq 0$  for all biseparable states  $\rho_B$ , and that  $\mathrm{Tr}(\mathcal{W}|\psi\rangle\langle\psi|) < 0$ . Thus, a negative expectation value of the observable  $\mathcal{W}$  clearly signifies that the state  $|\psi\rangle$  carries multipartite entanglement. Determining  $\alpha$  in Eq. (2) is a difficult task, when the maximization of the overlap with any biseparable state is performed explicitly. However, a simple method based on the Schmidt decomposition of bipartite partitions was found; details are described in the Appendix.

For the experimental implementation of the witness (1), it is necessary to decompose it into a number of local von Neumann (or projective) measurements [13]

$$
\mathcal {W} = \sum_ {k = 1} ^ {K} M _ {k}, \tag {3}
$$

where

$$
M _ {k} = \sum_ {l _ {1}, \dots , l _ {n}} d _ {l _ {1}, \dots , l _ {n}} ^ {(k)} \left| a _ {l _ {1}} ^ {(k, 1)} \right\rangle \left\langle a _ {l _ {1}} ^ {(k, 1)} \right| \otimes \dots \otimes \left| a _ {l _ {n}} ^ {(k, n)} \right\rangle \left\langle a _ {l _ {n}} ^ {(k, n)} \right|. \tag {4}
$$

Here  $n$  is the number of parties,  $|a_{l_m}^{(k,m)}\rangle$  are orthogonal vectors for a fixed  $(k,m)$ , and  $d_{l_1\dots l_n}^{(k)}$  are real weighting coefficients. An observable  $M_{k}$  can be measured with one setting of the measuring devices of the parties. We call the local decomposition (3) "optimal" when  $K$  is minimal.

For demonstrating the power of multipartite witnesses, we choose states with nonmaximal multipartite entanglement. The first one is the three-qubit  $W$  state [11,14]

$$
| W \rangle = \sqrt {\frac {1}{3}} (| 0 0 1 \rangle + | 0 1 0 \rangle + | 1 0 0 \rangle). \tag {5}
$$

$$
\begin{array}{l} \mathcal {W} _ {W} ^ {(1)} = \frac {2}{3} \mathbb {1} - | W \rangle \langle W | \\ = \frac {1}{2 4} \left[ 1 7 \cdot \mathbb {1} ^ {\otimes 3} + 7 \sigma_ {z} ^ {\otimes 3} + 3 \left(\sigma_ {z} \mathbb {1} \mathbb {1} + \mathbb {1} \sigma_ {z} \mathbb {1} + \mathbb {1} \mathbb {1} \sigma_ {z}\right) + 5 \left(\sigma_ {z} \sigma_ {z} \mathbb {1} + \sigma_ {z} \mathbb {1} \sigma_ {z} + \mathbb {1} \sigma_ {z} \sigma_ {z}\right) - \left(\mathbb {1} + \sigma_ {z} + \sigma_ {x}\right) ^ {\otimes 3} \right. \\ - \left(\mathbb {1} + \sigma_ {z} - \sigma_ {x}\right) ^ {\otimes 3} - \left(\mathbb {1} + \sigma_ {z} + \sigma_ {y}\right) ^ {\otimes 3} - \left(\mathbb {1} + \sigma_ {z} - \sigma_ {y}\right) ^ {\otimes 3} ]. \tag {7} \\ \end{array}
$$

Its expectation value is positive on biseparable and fully separable states. It thus detects all states belonging to the two classes of states with genuine tripartite entanglement, the  $W$  class and the GHZ class, but without distinguishing between them. The factor  $2/3$  corresponds to the maximal squared overlap between the  $W$  state and biseparable states. From this we also see that a mixture of  $|W\rangle$  and white noise,  $\rho = p|W\rangle\langle W| + (1 - p)\mathbb{1}/8$  exhibits tripartite entanglement for a noise contribution of up to  $p > 13/21$ . We introduced a short notation for tensor products, i.e.,  $\mathbb{1}\sigma_i\sigma_j \coloneqq \mathbb{1} \otimes \sigma_i \otimes \sigma_j$ , where  $\mathbb{1}$  and  $\sigma_i$  are the identity and Pauli matrices. This decomposition requires five measurement settings, namely,  $\sigma_z^{\otimes 3}$  and  $((\sigma_z \pm \sigma_i)/\sqrt{2})^{\otimes 3}$ ;  $i = x, y$ , see also Fig. 2 (below). Finding such a decomposition and proving its optimality is technically demanding (for details see [9]).

A witness that detects genuine tripartite entanglement and, with the same set of local measurements, allows one to distinguish between the  $W$  and GHZ states, is given by [16]

$$
\mathcal {W} _ {W} ^ {(2)} = \frac {1}{2} \mathbb {1} - | \overline {{\mathrm {G H Z}}} \rangle \langle \overline {{\mathrm {G H Z}}} | = \frac {1}{1 6} [ 6 \cdot \mathbb {1} ^ {\otimes 3} + 4 \sigma_ {z} ^ {\otimes 3} - 2 (\sigma_ {y} \sigma_ {y} \mathbb {1} + \sigma_ {y} \mathbb {1} \sigma_ {y} + \mathbb {1} \sigma_ {y} \sigma_ {y}) - (\sigma_ {z} + \sigma_ {x}) ^ {\otimes 3} - (\sigma_ {z} - \sigma_ {x}) ^ {\otimes 3} ], \tag {8}
$$

where  $|\overline{\mathrm{GHZ}}\rangle = (|\bar{0}\bar{0}\bar{0}\rangle + |\bar{1}\bar{1}\bar{1}\rangle) / \sqrt{2} = (|000\rangle + |001\rangle + |010\rangle + |100\rangle)$  with  $|\bar{0}\rangle = (|0\rangle + i|1\rangle) / \sqrt{2}$  and  $|\bar{1}\rangle = -(|0\rangle - i|1\rangle) / \sqrt{2}$ . This witness is constructed slightly differently from above; namely, here  $1/2$  is the maximal squared overlap between  $|\overline{\mathrm{GHZ}}\rangle$  and any biseparable state. Furthermore, since the maximum overlap between  $|\overline{\mathrm{GHZ}}\rangle$  and any  $W$  state is  $3/4$  [16], the operator  $\mathcal{W}_{\mathrm{GHZ}} = 3/4 \cdot \mathbb{1} - |\overline{\mathrm{GHZ}}\rangle \langle \overline{\mathrm{GHZ}}|$  is a GHZ witness, i.e., it has a negative expectation value for GHZ states, but is positive for states belonging to the class of  $W$  states. Therefore we can prove with the witness (8) that a state  $\rho$  is fully tripartite entangled if  $\operatorname{Tr}[\mathcal{W}_W^{(2)}\rho] < 0$ . If  $\operatorname{Tr}[\mathcal{W}_W^{(2)}\rho] < -1/4$ , then the state  $\rho$  does not belong to the  $W$  state class. Theoretically, one expects  $\operatorname{Tr}(\mathcal{W}_W^{(1)}|W\rangle \langle W|) = -1/3$  and  $\operatorname{Tr}(\mathcal{W}_W^{(2)}|W\rangle \langle W|) = -1/4$ .

For the four-qubit entangled state (6), we use the witness

$$
\begin{array}{l} \mathcal {W} _ {\Psi^ {(4)}} = \frac {3}{4} \mathbb {1} - | \Psi^ {(4)} \rangle \langle \Psi^ {(4)} | \\ = \frac {1}{4 8} \left(3 \left(\sigma_ {x} \sigma_ {x} \sigma_ {y} \sigma_ {y} + \sigma_ {y} \sigma_ {y} \sigma_ {x} \sigma_ {x} + \sigma_ {x} \sigma_ {x} \sigma_ {z} \sigma_ {z}\right) + 3 \left(\sigma_ {z} \sigma_ {z} \sigma_ {x} \sigma_ {x} + \sigma_ {y} \sigma_ {y} \sigma_ {z} \sigma_ {z} + \sigma_ {z} \sigma_ {z} \sigma_ {y} \sigma_ {y}\right) \right. \\ - (\sigma_ {x} + \sigma_ {y}) ^ {\otimes 4} - (\sigma_ {x} - \sigma_ {y}) ^ {\otimes 4} - (\sigma_ {x} + \sigma_ {z}) ^ {\otimes 4} - (\sigma_ {x} - \sigma_ {z}) ^ {\otimes 4} - (\sigma_ {x} + \sigma_ {z}) ^ {\otimes 4} - (\sigma_ {y} - \sigma_ {z}) ^ {\otimes 4} + 3 3 \cdot \mathbb {1} ^ {\otimes 4} \\ \left. - \sum_ {i = x, y, z} \left[ \sigma_ {i} \sigma_ {i} \mathbb {1} \mathbb {1} + \mathbb {1} \mathbb {1} \sigma_ {i} \sigma_ {i} - \sigma_ {i} ^ {\otimes 4} - 2 \left(\sigma_ {i} \mathbb {1} \sigma_ {i} \mathbb {1} + \sigma_ {i} \mathbb {1} \mathbb {1} \sigma_ {i} + \mathbb {1} \sigma_ {i} \sigma_ {i} \mathbb {1} + \mathbb {1} \sigma_ {i} \mathbb {1} \sigma_ {i}\right) \right]\right). \\ \end{array}
$$

This decomposition requires 15 measurement settings. The witness  $\mathcal{W}_{\Psi^{(4)}}$  has a positive expectation value on all triseparable, biseparable, and fully separable states. Here, the theoretical expectation value is given by  $\mathrm{Tr}[\mathcal{W}_{\Psi^{(4)}}\rho_{\Psi^{(4)}}] = -1/4$ . All of the above witnesses can detect the desired states mixed with not too large noise.

Let us now proceed with the experimental demonstration. We have chosen multiphoton states as the test bench of the entanglement witness. For these experiments, the qubits are represented by the polarization of the photons, with “0”  $\equiv$  horizontal (H) and “1”  $\equiv$  vertical (V) linear polarization. The process of spontaneous parametric down-conversion (SPDC) is used to generate a polarization-entangled four-photon state in the arms  $a_0$  and  $b_0$  [12,17] (Fig. 1). For enabling four observers in the arms  $a$ ,  $b$ ,  $c$ , and  $d$  to analyze the  $\Psi^{(4)}$  state, it suffices to distribute the four photons using semitransparent beam splitters (BS) [Fig. 1(a)]. To transform the initial state into the  $W$  state, we employ two-photon interference at a BS when distributing the photons into arms  $a$ ,  $b$ , and  $c$  [Fig. 1(b)] [18]. Provided each of the three (four) observers receive one photon, they obtain the three-photon state  $|W\rangle$ , or the four-photon state  $|\Psi^{(4)}\rangle$ , respectively. The general principle and the experimental techniques to observe multiphoton entangled states are described in detail in [15,19]; let us here focus on detecting their entanglement.

For implementing the witness observable polarization analyzers (PA) are used. A quarter(QWP)- and a half-wave-plate (HWP) together with a PBS allow to set and to analyze any arbitrary polarization direction of each of the photons. As the computational basis of the qubit "0"/"1" and thus the spin observable  $\sigma_z$  corresponds to a measurement of the H/V linear polarization,  $\sigma_x(\sigma_y)$  corresponds to the analysis of  $\pm 45^{\circ}$  linear polarization (left/right circular polarization). Registration of a photon in one of the two detectors of a PA signals the observation of the corresponding eigenstate of the spin operator. Every possible observable of the type  $|a_{l_1}^{(k,1)}\rangle \langle a_{l_1}^{(k,1)}|\otimes \dots \otimes |a_{l_n}^{(k,n)}\rangle \langle a_{l_n}^{(k,n)}|$  (4) corresponds to one of the  $2^n$  possible detection events where each of the  $n$  observers registers one photon, either with eigenvalue  $l_i = +1$  or  $-1$ . From the probability of these multiphoton detections,  $P[a^{(k,1)},\ldots ,a^{(k,n)}]_{l_1,\ldots ,l_n}$ , we then can compute the various terms  $\mathrm{Tr}[M_k\rho) =$

![](images/40fff548020fdce69d55a8feb9c6f92e18cca48dd98b1786e000354efe2124c4.jpg)  
(a)

![](images/9663a6af2fd46a00c7760f7b2feb0e8435a3c7f6798775268d6825865b50d011.jpg)  
(b)

![](images/dd1d179768a5250d8ded961d6d28b259f53b208b7f81ced43d060911ff3b3858.jpg)  
FIG. 1 (color online). Experimental setups to demonstrate (a) four-photon entanglement of the  $\Psi^{(4)}$  state and (b) three-photon entanglement of the  $W$  state; (c) polarization analysis (PA) setup.  
(c)

$\sum_{l_1,\dots,l_n = \pm 1}d_{l_1,\dots,l_n}^{(k)}P(a^{(k,1)},\dots,a^{(k,n)}]_{l_1,\dots,l_n}$  of the entanglement witness expectation value.

The multiphoton detection probabilities for the three-qubit state  $|W\rangle$  are shown in Fig. 2. From the experimental results, we obtain

$$
\operatorname {T r} \left(\mathcal {W} _ {W} ^ {(1)} \rho_ {W}\right) _ {\exp} = - 0. 1 9 7 \pm 0. 0 1 8, \tag {10}
$$

$$
\operatorname {T r} \left(\mathcal {W} _ {W} ^ {(2)} \rho_ {W}\right) _ {\exp} = - 0. 1 3 9 \pm 0. 0 3 0. \tag {11}
$$

This clearly proves with high statistical significance that the observed state is truly tripartite entangled. We want to emphasize that the evaluation of a three-photon Bell inequality failed to signify tripartite entanglement for the same experimental settings and noise [19], indicating the superiority of the witnesses.

For the detection of the genuine four-partite entanglement of the state  $|\Psi^{(4)}\rangle$ , 15 different analyzer settings are required. This is comparable with the 16 settings required for evaluating a four-photon Bell inequality [12]. However, for  $|\Psi^{(4)}\rangle$  all known Bell inequalities give a violation which is lower than the maximum one of biseparable states, therefore only tripartite entanglement could be shown by those violations. Thus, it is only the witness  $\mathcal{W}_{\Psi^{(4)}}$  which can prove the four-partite entanglement of  $|\Psi^{(4)}\rangle$ . The observed fourfold detection probabilities (Fig. 3) result in an expectation value of

$$
\operatorname {T r} \left(\mathcal {W} _ {\Psi^ {(4)}} \rho_ {\Psi^ {(4)}}\right) _ {\exp} = - 0. 1 5 1 \pm 0. 0 1, \tag {12}
$$

which finally confirms the genuine multipartite entanglement beyond any doubt.

In conclusion, we have developed a generic scheme to easily construct witness operators distinguishing genuine multipartite entangled states from biseparable states or states with even lower multipartite entanglement. This allowed one to analyze the entanglement of three- and four-photon entangled states based on local measurements only. Whereas the evaluation of generalized multiphoton Bell inequalities fell short of ruling out biseparability [15,19], the experimentally obtained

![](images/7cf2b496f827dd57cd5a3207a8b9bb057d0188c080110de4cb57549856473684.jpg)  
FIG. 2 (color online). Three-photon detection probabilities for six settings of the polarization analyzers as required for the detection of three-photon entanglement using the witness operators  $\mathcal{W}_W^{(1)}$  and  $\mathcal{W}_W^{(2)}$ .

![](images/2d9b2857762d9c81db78652c29c1f6b7bb07af21eedffb11fb3cc5b61e48ab74.jpg)  
FIG. 3 (color online). Four-photon detection probabilities for fifteen settings of polarization analyzers as required for the detection of four-photon entanglement using the witness operators  $\mathcal{W}_{\Psi^{(4)}}$ .

values of the respective witnesses clearly prove the genuine multipartite entanglement of the observed states. After solving the problem of analyzing bipartite entanglement [3,4], we now have also a well-suited tool at hand for the experimental analysis of genuine multipartite entangled quantum systems.

We thank A. Acín, A. Ekert, C. Macchiavello, A. Miyake, and F. Verstraete for discussions and acknowledge support from the Deutsche Forschungsgemeinschaft, the Bavarian quantum information initiative, and the EU (Program RamboQ and QUPRODIS).

Appendix. In this Appendix, we show how to calculate the overlap  $\alpha$  of Eq. (2). We first fix a bipartite splitting  $B_{1}$ , and consider only states  $|\phi\rangle \in B_{1}$  which are product vectors with respect to this partition. We choose an orthonormal product basis  $|ij\rangle$  for this partition, thus  $|\psi\rangle = \sum_{ij}c_{ij}|ij\rangle$  and  $|\phi\rangle = |a\rangle|b\rangle = \sum_{ij}a_ib_j|ij\rangle$ . The coefficient matrix is denoted by  $C = (c_{ij})$  and the normalized coefficient vectors by  $\vec{a} = (a_i)$  and  $\vec{b} = (b_i)$ . Then

$$
\begin{array}{l} \max  _ {| \phi \rangle \in B _ {1}} | \langle \phi | \psi \rangle | = \max  _ {a _ {i}, b _ {j}} \left| \sum_ {i j} \left(a _ {i} ^ {*} c _ {i j} b _ {j} ^ {*}\right) \right| = \max  _ {\vec {a}, \vec {b}} | \langle \vec {a} | C | \vec {b} ^ {*} \rangle | \\ = \max  _ {k} \left\{\lambda_ {k} (C) \right\}, \tag {13} \\ \end{array}
$$

where  $\lambda_{k}(C)$  denotes the singular values of  $C$ , i.e., the

roots of the eigenvalues of  $CC^\dagger$ . In other words,  $\lambda_k(C)$  are the Schmidt coefficients of  $|\psi\rangle$  with respect to a fixed bipartite splitting. Therefore,  $\alpha$  is given by the square of the Schmidt coefficient which is maximal over all possible bipartite partitions of  $|\psi\rangle$ .

[1] J. S. Bell, Physics (Long Island City, N.Y.) 1, 195 (1964); N. D. Mermin, Phys. Rev. Lett. 65, 1838 (1990).  
[2] R. F. Werner, Phys. Rev. A 40, 4277 (1989).  
[3] A. Peres, Phys. Rev. Lett. 77, 1413 (1996).  
[4] M. Horodecki, P. Horodecki, and R. Horodecki, Phys. Lett. A 223, 1 (1996).  
[5] With the exception of Gaussian states in continuous variable systems; G. Giedke, B. Kraus, M. Lewenstein, and J. I. Cirac, Phys. Rev. Lett. 87, 167904 (2001).  
[6] A mixed state is called biseparable if it is a mixture of biseparable pure states; the mixture may contain terms corresponding to different partitions. For triseparable pure states, etc., the whole state can be partitioned into three or more such groups with consequently decreasing genuine multipartite entanglement.  
[7] D. Collins et al., Phys. Rev. Lett. 88, 170405 (2002).  
[8] B.M. Terhal, Phys. Lett. A 271, 319 (2000); M. Lewenstein et al., Phys. Rev. A 62, 052310 (2000); D. Bruß et al., J. Mod. Opt. 49, 1399 (2002).  
[9] O. Gühne and P. Hyllus, Int. J. Theor. Phys. 42, 1001 (2003).  
[10] Note that the experimental realization of two-photon entanglement witness was recently reported; M. Barbieri et al., Phys. Rev. Lett. 91, 227901 (2003).  
[11] W. Dur, G. Vidal, and J. I. Cirac, Phys. Rev. A 62, 062314 (2000).  
[12] H. Weinfurter and M. Žukowski, Phys. Rev. A 64, 010102 (2001).  
[13] B.M. Terhal, Theor. Comput. Sci. 287, 313 (2002); O. Gühne et al., Phys. Rev. A 66, 062305 (2002).  
[14] N. Kiesel et al., J. Mod. Opt. 50, 1131 (2003).  
[15] M. Eibl et al., Phys. Rev. Lett. 90, 200403 (2003); S. Gaertner et al., Appl. Phys. B (to be published).  
[16] A. Acín, D. Bruß, M. Lewenstein, and A. Sanpera, Phys. Rev. Lett. 87, 040401 (2001).  
[17] P.G. Kwiat et al., Phys. Rev. Lett. 75, 4337 (1995).  
[18] The basic idea of how to observe the  $|W\rangle$  is as follows: If one photon is registered by the trigger detector  $t$  in the reflected output of the polarizing beam splitter (PBS), and the others in arms  $a$ ,  $b$ , and  $c$ , then two of those three photons have horizontal polarization, with the third being vertically polarized. For having twice the probability of observing horizontally polarized photons compared to vertically polarized ones, we place a polarization dependent beam splitter (PDBS) in arm  $a_0$  (with transmissions  $t_H = 2t_V$ ). The remaining two photons are interfered at a 50-50 beam splitter (BS) and distributed into arms  $b$  and  $c$  by a second BS [14,19].  
[19] M. Eibl et al., Phys. Rev. Lett. 92, 077901 (2004).