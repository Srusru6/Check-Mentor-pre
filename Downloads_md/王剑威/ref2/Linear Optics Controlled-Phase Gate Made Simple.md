# Linear Optics Controlled-Phase Gate Made Simple

Nikolai Kiesel, $^{1,2}$  Christian Schmid, $^{1,2}$  Ulrich Weber, $^{1,2}$  Rupert Ursin, $^{3}$  and Harald Weinfurter $^{1,2}$

<sup>1</sup>Max-Planck-Institut für Quantenoptik, D-85748 Garching, Germany

$^{2}$ Department für Physik, Ludwig-Maximilians-Universität, D-80797 München, Germany

$^{3}$ Institut für Experimentalphysik, Universität Wien, A-1090 Wien, Austria

(Received 30 June 2005; published 18 November 2005)

Linear optics quantum logic gates are the best tool to generate multiphoton entanglement. Simplifying a recent approach [Phys. Rev. A 65, 062324 (2002); 66, 024308 (2002); Nature (London) 426, 264 (2003); Phys. Rev. Lett. 93, 080502 (2004)], we were able to implement the conditional phase gate with only one second-order interference at a polarization dependent beam splitter, thereby significantly increasing its stability. The improved quality of the gate is evaluated by analyzing its entangling capability and by performing full process tomography. The achieved results ensure that this device is well suited for implementation in various multiphoton quantum information protocols.

DOI: 10.1103/PhysRevLett.95.210505

PACS numbers: 03.67.Lx, 42.65.Lm

The quantum computer is one of the most promising and desirable goals in quantum information science. Its implementation relies strongly on the capability to engineer entanglement in the quantum system of choice. For qubits, it was shown that entangling gates (such as the C-phase gate or the CNOT) together with single qubit operations are sufficient to create any kind of quantum network.

Photons are well suited for quantum information tasks, as their interaction with the environment is small, guaranteeing low decoherence. While the creation of entangled photon pairs via spontaneous parametric down-conversion became a standard technique, its control is still a major challenge, due mainly to low nonlinear interaction efficiencies. One solution to this problem is using linear optics components and introducing the nonlinearity via ancillary single photons and photon number resolving detectors [1]. Initial demonstrations showed that such gates can be implemented, once the necessary sources and detectors become available on a larger scale [2]. Another solution, requiring much less resources, becomes possible if one focuses on performing only a limited number of quantum logic operations. Then one can control the action of the gate by conditioning it to the detection of one photon in each of the output ports. This will occur only with a certain probability, which, however, might be larger than the one achievable with the first method and equivalent resources. In particular, a controlled-phase (C-phase) gate was introduced recently [3], which uses a combination of first- and second-order interference to obtain C-phase action in  $1/9$  of the cases. Yet, since first-order interference requires stability of the setup on the order of less than the photon's wavelength, for multiphoton experiments [4] more simple and stable implementations surely are desirable.

Here we introduce a linear optics C-phase gate, which uses only a single two-photon interference at a polarization dependent beam splitter. The stability requirements are thereby relaxed to the coherence length of the detected photons ( $\approx 150~\mu \mathrm{m}$ ) and can easily be fulfilled without additional stabilization equipment. To characterize the C-

phase gate, we first study the entangling capability of the gate by determining the fidelity and negativity of the output for four different input states. Second, we use linear quantum process tomography (QPT) [5,6] to analyze the gate operation. As imperfect interference reduces the quality of the gate and induces state-selective incoherence, we had to account for the non-trace-preserving character of the gate. Instead of the usual maximum likelihood approach, we use prior knowledge of the intrinsic features of our setup, in order to obtain physical and easily understandable parameters for characterizing the gate and estimating its performance.

The ideal C-phase gate acts on two-qubit input states

$$
\left| \psi_ {\text {i n}} \right\rangle = \left(c _ {H H} | H H \rangle + c _ {H V} | H V \rangle + c _ {V H} | V H \rangle + c _ {V V} | V V \rangle\right) \tag {1}
$$

and applies a relative  $\pi$ -phase shift to the contribution  $VV$  only, such that

$$
\left| \psi_ {\text {o u t}} \right\rangle = \left(c _ {H H} | H H \rangle + c _ {H V} | H V \rangle + c _ {V H} | V H \rangle - c _ {V V} | V V \rangle\right). \tag {2}
$$

Here we encode the logical 0 (1) in the linear horizontal  $H$  (vertical  $V$ ) polarization of single photons.  $c_{HH}$  denotes the amplitude of the  $|HH\rangle$  term (for the other terms accordingly).

The application of the phase shift relies on second-order interference of indistinguishable photons at a polarization dependent beam splitter (PDBS [7]) (Fig. 1) [8,9]. Two input modes  $a$  and  $b$  are overlapped at  $\mathrm{PDBS}_0$ . The transmission of  $1/3$  for vertical polarization results in a total amplitude of  $-1/3$  for the  $|VV\rangle$  output terms, as can be seen by adding the amplitudes for a coincident detection:

$$
\left(t _ {V} ^ {a} t _ {V} ^ {b}\right) + \left(i r _ {V} ^ {a} i r _ {V} ^ {b}\right) = \sqrt {\frac {1}{3}} \sqrt {\frac {1}{3}} - \sqrt {\frac {2}{3}} \sqrt {\frac {2}{3}} = - 1 / 3, \tag {3}
$$

where  $t_i^x (r_i^x)$  is the amplitude for transmission (reflection) of state  $|i\rangle$  in mode  $x$ . Perfect transmission of horizontal polarization causes that no interference happens on the

![](images/18994b5a3b7f429adf397ec836d4f21ccaa79f9349fde5b880383206c1dbc78f.jpg)  
FIG. 1 (color online). Experimental setup for the C-phase gate. The phase is introduced by a second-order interference at a polarization dependent beam splitter  $\mathrm{PDBS}_0$ . To obtain equal output amplitudes for any input polarization, state polarization dependent beam splitters with reversed splitting ratio  $\mathrm{PDBS}_{a / b}$  are placed in each mode. The gate operation is applied in case of a coincidence detection between modes  $a$  and  $b$ . The resulting output state is analyzed via half- and quarter-wave plates  $\lambda /2$ ,  $\lambda /4$  and a polarizing beam splitter.

contributions  $|HH\rangle$ ,  $|HV\rangle$ , and  $|VH\rangle$ . As the absolute values of the amplitudes need to be equal for any input, we still need to attenuate the contributions that include horizontal polarization. This is achieved by  $\mathrm{PDBS}_{a / b}$  with the transmission  $1 / 3$  for horizontal polarization and perfect transmission for vertical polarization in both output modes. Altogether, we find a probability of  $1 / 9$  to obtain a coincidence in the outputs and, thus, a gate operation with perfect fidelity.

Working with real components results in deviations from the theoretical derivation. A detailed calculation with arbitrary transmission and reflection amplitudes at  $\mathrm{PDBS_O}$  and  $\mathrm{PDBS}_{a,b}$  shows how their parameters influence the gate operation. In general, we obtain from  $|\psi_{\mathrm{in}}\rangle$

$$
\begin{array}{l} | \psi_ {\mathrm {o u t}} \rangle = (c _ {H H} t _ {H} ^ {a} t _ {H} ^ {b} a _ {H} b _ {H} - c _ {H H} r _ {H} ^ {a} r _ {H} ^ {b} a _ {H} b _ {H}) | H H \rangle \\ + \left(c _ {H V} t _ {h} ^ {a} t _ {V} ^ {b} a _ {H} b _ {V} - c _ {V H} r _ {V} ^ {a} r _ {H} ^ {b} a _ {H} b _ {V}\right) | H V \rangle \\ + \left(c _ {V H} t _ {V} ^ {a} t _ {H} ^ {b} a _ {V} b _ {H} - c _ {H V} r _ {H} ^ {a} r _ {V} ^ {b} a _ {V} b _ {H}\right) | V H \rangle \\ \left. + \left(c _ {V V} t _ {V} ^ {a} t _ {V} ^ {b} a _ {V} b _ {V} - c _ {V V} r _ {V} ^ {a} r _ {V} ^ {b} a _ {V} b _ {V}\right) | V V \rangle\right), \tag {4} \\ \end{array}
$$

where  $a_{i}(b_{i})$  are the transmission amplitudes of  $|i\rangle$  in mode  $a$  ( $b$ ). To obtain the expected C-phase gate operation, one has to fulfill several conditions, which give an insight in how the setup has to be built. First,  $(r_V^a r_V^b) / (t_V^a t_V^b) = 2$ , which is approximately achieved by slightly varying the angle of incidence at PDBS $_0$ . Experimentally, we reach a value of  $2.018 \pm 0.003$ . Second,  $r_H^a = 0 = r_H^b$ , which requires the reflection of the horizontal polarization at the overlap beam splitter to be zero. The third condition,  $t_H^a a_H = t_V^a a_V$  and  $t_H^b b_H = t_V^b b_V$ , respectively, determines the setting for the attenuation at PDBS $_{a,b}$ .

To experimentally test the gate operation, we used photon pairs emitted from spontaneous parametric down-

conversion. A  $2\mathrm{mm}$  thick  $\beta$ -barium borate crystal was pumped by UV pump pulses with a central wavelength of  $390~\mathrm{nm}$  and an average power of  $700~\mathrm{mW}$  from a frequency-doubled mode-locked Ti:sapphire laser (pulse length 130 fs). The pulsed operation is not necessary when working only with photon pairs, but, as the gate is intended to work in multiphoton applications, we preferred to characterize it for this mode of operation. The emission is filtered with polarizers to prepare input product states with high quality. We couple the photon pairs into single mode fibers for selection of the spatial modes. This guarantees identical beam modes, which eases the alignment of spatial mode matching at  $\mathrm{PDBS_O}$ . The spectral mode selection is improved via  $2\mathrm{nm}$  bandwidth filters behind the gate.

To ensure the same optical path length between the crystal and the overlap beam splitter for both photons, one of the output couplers of the single mode fibers is mounted on a translation stage. The position of zero delay is determined from the minimum of the coincidence rate for  $|VV\rangle$  input (Hong-Ou-Mandel [8], "HOM" dip in Fig. 2). In each output mode of the C-phase gate, the polarization is analyzed via quarter- and half-wave plates and a polarizing beam splitter with single photon avalanche photodiodes. For the analysis of the final two-photon states, the coincidence count rates for each of the four contributions have to be corrected for the different detection efficiencies. The errors on all quantities are deduced from propagated Poissonian counting statistics of the raw detection events and efficiencies.

The HOM measurement shown in Fig. 2 also gives information about the indistinguishability of the photons at the PDBS. For large delay, the two photons are completely distinguishable due to their time of arrival. The probability to get a coincidence from a  $|VV\rangle$  input is then  $5/9$ . In case of perfectly indistinguishable photons at zero delay, the probability drops to  $1/9$ . The dip visibility is

![](images/d87136891dc42b0a42a1be9fbb11a11bc3e2e957fd3b5278a34afc5ab7bc518e.jpg)  
FIG. 2 (color online). HOM interference at the polarization dependent overlap beam splitter in the phase gate for a  $|VV\rangle$  input. In case of perfect interference, the count rate should drop down to  $20\%$ , leading to a theoretically achievable dip visibility of  $80\%$ .

defined by  $\mathcal{V} = (c_{\infty} - c_0) / c_{\infty}$ , where  $c_{0}$  is the count rate at zero delay and  $c_{\infty}$  at positions with big delay. From the above considerations, we obtain a theoretical value of  $\mathcal{V}_{\mathrm{th}} = 80\%$ , and, experimentally, applying a least-squares fit, we find  $\mathcal{V}_{\mathrm{exp}} = 72.8\% \pm 0.7\%$ . We call  $\mathcal{Q} = \mathcal{V}_{\mathrm{exp}} / \mathcal{V}_{\mathrm{th}} = 91.0\% \pm 0.9\%$  the overlap quality. We can conclude that about  $9\%$  of the detected photon pairs are distinguishable and, therefore, not interfering. This effect is visible as an additional admixture of vertically polarized photons pairs (further referred to as  $|VV\rangle \langle VV|$  noise), as only the probability of the  $VV$  detections is raised by worse interference.

As a first step in the analysis of the performance of our gate, we look at its capability to entangle. We choose  $| + + \rangle ,| + L\rangle ,|L + \rangle$ , and  $|LL\rangle$ , with  $|\pm \rangle = 1 / \sqrt{2} (|H\rangle \pm |V\rangle)$  and  $|L\rangle = 1 / \sqrt{2} (|H\rangle +i|V\rangle)[|R\rangle = 1 / \sqrt{2} (|H\rangle -i|V\rangle)]$ , as input product states and perform state tomography on the output states [10]. We use linear tomography as the resulting matrices all have eigenvalues greater than or equal to  $-0.02$ , i.e., are almost physical without corrections. For an ideal C-phase gate, one would obtain a maximally entangled output for these input states, for example,

$$
\left| L + \right\rangle = 1 / 2 \left(\left| H H \right\rangle + i | V H \rangle + \left| H V \right\rangle + i | V V \rangle\right)
$$

$$
\begin{array}{l} \overline {{P G}} | L + \rangle = 1 / 2 \left(| H H \rangle + i | V H \rangle + | H V \rangle - i | V V \rangle\right) \tag {5} \\ = 1 / \sqrt {2} (| L H \rangle + | R V \rangle). \\ \end{array}
$$

The experimentally observed fidelities relative to the expected output states are all better  $F_{\mathrm{exp}} \geq 80.5\% \pm 0.6\%$ . Figure 3 exemplarily shows the experimental result for  $|L + \rangle$  input ( $F_{\mathrm{exp}}^{L+} = 87.8\% \pm 0.6\%$ ). Note that, for states with a fidelity larger than  $(2 + 3\sqrt{2}) / 8 = 0.78$ , Bell inequalities are violated [11], which is the case for all of our

![](images/0a7b28c9cbb4e6ef00d8f7dd6cf8aa4a7234344b112bdcb1bc1f9a4520deb52c.jpg)

![](images/92c7ce5a093ea5630d3b459d26d6356afd413ab7225554c3d072ce1906945611.jpg)

![](images/6b6e9723475f152022841519dce787308876f07dbf536fc8a0aa608ef9b159bb.jpg)  
FIG. 3 (color online). (a) Theoretically expected and (b) experimentally obtained gate output density matrix for the  $|L + \rangle$  input state.

![](images/0bc426b9d172f6c85ba82031d116c102612b3b5b2f0b4ab48b05fcf123f84849.jpg)

examples. To quantify the entanglement, we also calculated the logarithmic negativity—for all output states, we find  $\mathcal{N}_{\mathrm{exp}} \geq 0.73 \pm 0.02$  ( $\mathcal{N}_{\mathrm{exp}}^{L+} = 0.75 \pm 0.02$ ) [12].

For a complete characterization of an arbitrary unknown process, one can use QPT. For QPT, the process is represented by a superoperator  $\mathcal{E}$ , which is decomposed in a linear combination of a basis of unitary transformations  $E_{i}$ :

$$
\mathcal {E} \left(\rho_ {\text {i n}}\right) = \sum_ {i, j} \chi_ {i j} E _ {i} \rho_ {\text {i n}} E _ {j} ^ {\dagger}. \tag {6}
$$

The matrix  $\chi$  completely describes the process. In order to obtain all components  $\chi_{ij}$ , the normalized output density matrices  $\rho_{\mathrm{out}}^k$  for a tomographic set of, usually separable, input states are measured, in our case for the inputs  $(|HH\rangle, |HV\rangle, |H+\rangle, |H-\rangle, |VH\rangle, |VV\rangle, |V+\rangle, |VL\rangle, |+H\rangle, |+V\rangle, |++\rangle, |+L\rangle, |LH\rangle, |LV\rangle, |L+\rangle, |LL\rangle)$ . As the contribution of the  $|VV\rangle\langle VV|$  noise is input state dependent, our process is non-trace-preserving (i.e., this noise does not occur for  $|HH\rangle$  input). This means that the outcomes occur with different probabilities  $p_k$  [5] for the different input states  $\rho_{\mathrm{in}}^k \operatorname{Tr}(\mathcal{E}(\rho_{\mathrm{in}}^k))$ :

$$
\rho_ {\text {o u t}} ^ {k} = \frac {\mathcal {E} \left(\rho_ {\text {i n}} ^ {k}\right)}{\operatorname {T r} \left(\mathcal {E} \left(\rho_ {\text {i n}} ^ {k}\right)\right)} \Rightarrow \mathcal {E} \left(\rho_ {\text {i n}} ^ {k}\right)) = \operatorname {T r} \left(\mathcal {E} \left(\rho_ {\text {i n}} ^ {k}\right)\right) \rho_ {\text {o u t}} ^ {k} = p k \rho_ {\text {o u t}} ^ {k}. \tag {7}
$$

We determine these probabilities from the diagonal entries of all measured output density matrices. The normalized density matrices together with the corresponding probabilities can be used to evaluate  $\chi_{ij}$  via Eqs. (6) and (7). To account for the probabilistic nature of the gate, an overall normalization is performed such that  $p_{HH} = 1 / 9$ .

Figure 4(a) shows the process matrix  $\chi_{\mathrm{th}}$  of the ideal linear optics phase gate. It represents the decomposition of the C-phase gate into unitary operations, for our choice of  $E_{i}$  resulting in

$$
\overline {{P G}} _ {\text {i d e a l}} = \left(\mathbb {1} \otimes \mathbb {1} + \sigma_ {z} \otimes \mathbb {1} + \mathbb {1} \otimes \sigma_ {z} - \sigma_ {z} \otimes \sigma_ {z}\right) / 3. \tag {8}
$$

The four peaks in the diagonal of  $\chi_{\mathrm{th}}$  show the equal weights of the contributions, while the negative entries at the edges represent the negative sign at  $\sigma_z\otimes \sigma_z$ . This matrix now can be compared with the experimentally obtained one [Fig. 4(b)]. Only the real parts are shown since the imaginary parts are close to zero (average  $0.0\pm 0.002$ ). As the introduced noise is not too big, the experimentally measured process matrix still demonstrates nicely the features of the gate operation. The main differences are the lower nondiagonal terms indicating reduced coherence in the system. From the estimated process tomography matrix, we calculated a process fidelity of  $F_{p} = \mathrm{Tr}(\chi_{\mathrm{th}}\chi_{\mathrm{exp}}) / (\mathrm{Tr}(\chi_{\mathrm{th}})\mathrm{Tr}(\chi_{\mathrm{exp}})) = 81.8\%$ . Still, due to Poissonian counting statistics,  $\chi_{\mathrm{exp}}$  has nonphysical, negative eigenvalues, and the above value has to be treated with care. To circumvent this problem, one can use the maximum likelihood approach, where a physical process matrix is fitted to the observed data. Yet, the process is not

![](images/4763cb50e4c9e04a60630a7d959b9c10bf428ec42d1d08e23f822156b81decbb.jpg)

![](images/05fd762af2145cf89555a9b234463828be500a2bfb6c175c8d3e26c078a914d8.jpg)

![](images/c0295edd0e7159743e6fce6e677f68c8242ec855064fdc8c7b679cc784361e05.jpg)  
FIG. 4 (color online). (a)  $\chi$  matrix of the QPT for an ideal phase gate, (b) for the experimentally realized gate, and (c) for a theoretical model fit to the experimental data. The imaginary part of the experimentally obtained  $\chi$  consists of noise only, which is comparable to the one in the real part.

really unknown to us and we can try to describe it via a theoretical model according to Eq. (4).

The transformation of the phase gate consists of interference between both photons transmitted or both photons reflected  $\overline{PG}_{\mathrm{gen}} = M_{tt} + M_{rr}$ , where both  $M_{tt}$  and  $M_{rr}$  are matrices with components given by the coefficients of Eq. (4). For simplicity, we assume  $t_V^a = t_V^b$  and  $r_H^a = r_H^b = 0$ .  $M_{rr} = |r_V|^2 |VV\rangle \langle VV|$  reduces then to only one nonvanishing matrix element. The state dependent noise originates from the fact that interference occurs only with a probability according to the quality parameter  $\mathcal{Q}'$  and is incoherent otherwise, which finally yields

$$
\begin{array}{l} \overline {{P G}} _ {\mathrm {m o d}} \rho \overline {{P G}} _ {\mathrm {m o d}} ^ {\dagger} = Q ^ {\prime} \left(M _ {t t} + M _ {r r}\right) \rho \left(M _ {t t} + M _ {r r}\right) ^ {\dagger} \\ + (1 - \mathcal {Q} ^ {\prime}) \left(M _ {t t} \rho M _ {t t} ^ {\dagger} + M _ {r r} \rho M _ {r r} ^ {\dagger}\right). \tag {9} \\ \end{array}
$$

From this ansatz, we obtain a model QPT matrix  $\chi_{\mathrm{mod}}$  by minimizing the sum of the absolute squared values of all the matrix elements of  $\chi_{\mathrm{mod}} - \chi_{\mathrm{exp}}$  numerically [see Fig. 4(c)]. The obtained quality value  $Q' = 0.904$  is in very good agreement with  $Q$  obtained from the fit to the HOM dip [13]. This indicates that it is indeed mainly imperfect overlap at the beam splitter which causes the state dependent noise. In order to compare the model with the real setup, we calculate the fidelities between the predicted and the experimentally measured output density matrices, obtaining an average value of  $\mathrm{F}_{\mathrm{mod}Q'}^{\mathrm{exp}} = 96.6\% \pm 1.7\%$ . An alternative model including depolarization in the gate did not significantly change the figure; the resulting white noise was negligible.

In conclusion, we have presented a C-phase gate acting on the polarization degree of freedom of photons. The gate relies only on one second-order interference at a polarization dependent beam splitter and, thus, significantly simplifies previous approaches. We have demonstrated the entangling quality of the gate for various input states. A linear quantum process tomography allowed us to match a model of the gate to the experimental data. The resulting fit proofs the assumption that the main deviation from optimal performance is due to distinguishability of incident photons at the overlap beam splitter. By means of further filtering, this can be improved on the cost of count rate. The results ensure that this gate is ready to be used in various quantum information processing tasks such as complete Bell state analysis in quantum teleportation and

entanglement swapping experiments or generating multiphoton entanglement. Of particular interest for the latter is the possibility to join several EPR pairs to multiphoton cluster states.

We acknowledge stimulating discussions with A. Zeilinger. This work was supported by the Deutsche Forschungsgemeinschaft and the European Commission through the EU Project RamboQ (IST-2001-38864).

[1] E. Knill, R. Laflamme, and G.J. Milburn, Nature (London) 409, 46 (2001).  
[2] T. B. Pittman, M. J. Fitch, B. C. Jacobs, and J. D. Franson, Phys. Rev. A 68, 032316 (2003); K. Sanaka, T. Jennewein, J. W. Pan, K. Resch, and A. Zeilinger, Phys. Rev. Lett. 92, 017902 (2004); S. Gasparoni, J. W. Pan, P. Walther, T. Rudolph, and A. Zeilinger, Phys. Rev. Lett. 93, 020504 (2004).  
[3] T.C. Ralph, N.K. Langford, T.B. Bell, and A.G. White, Phys. Rev. A 65, 062324 (2002); H.F. Hofmann and S. Takeuchi, Phys. Rev. A 66, 024308 (2002); J.L. O'Brien, G.J. Pryde, A.G. White, T.C. Ralph, and D. Branning, Nature (London) 426, 264 (2003); J.L. O'Brien et al., Phys. Rev. Lett. 93, 080502 (2004).  
[4] C. Schmid et al. (to be published); N. Kiesel et al., quantph/0508128 [Phys. Rev. Lett. (to be published)].  
[5] I. L. Chuang and M. A. Nielsen, J. Mod. Opt. 44, 2455 (1997); J. F. Poyatos, J. I. Cirac, and P. Zoller, Phys. Rev. Lett. 78, 390 (1997).  
[6] M. W. Mitchell, C. W. Ellenor, S. Schneider, and A. M. Steinberg, Phys. Rev. Lett. 91, 120402 (2003).  
[7] For each PDBS, we use a custom made beam splitter with dielectric coating designed for the purpose. The  $\mathrm{PDBS_O}$  is realized as a beam splitting cube, while  $\mathrm{PDBS}_{a / b}$  are plates.  
[8] C. K. Hong, Z. Y. Ou, and L. Mandel, Phys. Rev. Lett. 59, 2044 (1987).  
[9] R.A. Campos, B.E.A. Saleh, and M.C. Teich, Phys. Rev. A 42, 4127 (1990).  
[10] D. F. V. James, P. G. Kwiat, W. J. Munro, and A. G. White, Phys. Rev. A 64, 052312 (2001).  
[11] C.H. Bennett, G. Brassard, S. Popescu, B. Schumacher, J.A. Smolin, and W.K. Wootters, Phys. Rev. Lett. 76, 722 (1996).  
[12] G. Vidal and R.F. Werner, Phys. Rev. A 65, 032314 (2002).  
[13] Other parameters are determined as:  $t_V^2 / r_V^2 = 2.035$ ,  $a_H t_H = 1.0a_V t_V$ ,  $b_H t_H = 1.16b_V t_V$ .