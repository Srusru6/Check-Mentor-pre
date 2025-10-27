# Experimental Realization of Multipartite Entanglement of 60 Modes of a Quantum Optical Frequency Comb

Moran Chen, $^{1}$  Nicolas C. Menicucci, $^{2,*}$  and Olivier Pfister $^{1,\dagger}$

$^{1}$ Department of Physics, University of Virginia, Charlottesville, Virginia 22903, USA

$^{2}$ School of Physics, The University of Sydney, Sydney, New South Wales 2006, Australia

(Received 11 November 2013; revised manuscript received 31 January 2014; published 26 March 2014)

We report the experimental realization and characterization of one 60-mode copy and of two 30-mode copies of a dual-rail quantum-wire cluster state in the quantum optical frequency comb of a bimodally pumped optical parametric oscillator. This is the largest entangled system ever created whose subsystems are all available simultaneously. The entanglement proceeds from the coherent concatenation of a multitude of Einstein, Podolsky, and Rosen pairs by a single beam splitter, a procedure which is also a building block for the realization of hypercubic-lattice cluster states for universal quantum computing.

DOI: 10.1103/PhysRevLett.112.120505

PACS numbers: 03.67.Bg, 03.67.Mn, 42.50.Dv, 42.50.Ex

Introduction.—Initially identified by Einstein, Podolsky, and Rosen (EPR) [1] as central to testing the completeness of quantum mechanics, entanglement is also crucial to exponential speedups of quantum computing [2-5]. In the race to build a practical quantum computer [6], the ability to create very large quantum registers and entangle them is paramount, along with the ability to address the issue of decoherence. The study of large-scale entanglement—i.e., multipartite entanglement between numerous subsystems—is in itself an intriguing topic at the forefront of current research, as such systems have yet to be studied in laboratories.

Until recently, the largest entangled state of any sort involved 14 trapped ions [7]. Quantum optical systems, which suffer less from decoherence but are harder to entangle, have shown progress, with photon-based, discrete-variable implementations of a 4-qubit "compiled," nonscalable version of Shor's algorithm [8,9], including in an integrated optics platform [10], 4-qubit blind quantum computing [11], and 8-qubit topological quantum error correction [12].

With particular regard to scalability, the field-based, continuous-variable (CV) flavor of quantum optics has high potential [13-17], in particular by enabling "top down," rather than "bottom up," entangling approaches of quantum field modes. It is also important to note the relevance of continuous variables to universal quantum computing, with the recent discovery of a fault tolerance threshold for quantum computing with CV cluster states and non-Gaussian error correction [18].

In 2011, 15 independent 4-mode cluster states were generated simultaneously over 60 modes of the quantum optical frequency comb (QOFC) of a single optical parametric oscillator (OPO) [19]. In 2013, 10-mode entanglement was observed in a synchronously pumped OPO [20], and 10 000 modes were sequentially entangled into a dual-rail cluster state [21] following a time-domain protocol

[22,23] in which the modes are emitted in pairs and detected in turn, with only a few modes accessible at any given time.

In this Letter, we report the experimental multipartite entanglement of 60 adjacent modes of the QOFC of a single OPO, all simultaneously available. The number of entangled modes was limited by our measurement technique, not by the generation process (which we estimate [24] yielded in excess of 6,000 entangled modes). This is the largest entangled state ever created in which all constituent systems are simultaneously available and addressable. Moreover, the entanglement is not of an arbitrary type (e.g., largely due to experimental convenience [19,20]) but a carefully engineered, sophisticated resource—a continuous-variable dual-rail quantum wire [25]—that has direct applications in quantum computing [26,27] and in experimental studies of topological order in quantum many-body systems [28], a novel quantum phenomenon that has yet to be revealed experimentally. Beyond these immediate applications, it also forms a basic building block for much larger entangled states with rich, regular-lattice structure [27], some of which could not otherwise be embedded in three-dimensional space. The intrinsic scalability of the experimental design paves the way for a new program of experimental research into the properties and applications of these richly entangled multipartite quantum systems.

Principle of the experiment.-The QOFC was formed by the resonant modes of the optical cavity of a doubly resonant OPO. The OPO contained periodically poled  $\mathrm{KTiOPO_4}$  (PPKTP) nonlinear crystals that quasi-phase-matched  $zzz$  parametric down-conversion (PDC)—the concurrent annihilation of a  $z$ -polarized pump photon at the  $532~\mathrm{nm}$  wavelength and creation of a  $z$ -polarized photon pair at the  $1064~\mathrm{nm}$  wavelength. Because of the cavity's resonant enhancement, the signal pair frequencies, adding up to the pump frequency, are the cavity

![](images/a703dc66d4524600060f264f1231c1d1ff7d739ea91a38016dab903265e15e27.jpg)

![](images/eb482a40287e0178d71ad926e8cd01a31c2e33e0e29bd41954d55f02b5d735ea.jpg)  
FIG. 1 (color online). Generation of a dual-rail quantum wire in the QOFC. (a) EPR pairs created by  $zzz$  and  $yyy$  interactions in the QOFC of a polarization-degenerate OPO (at each frequency  $n$  the  $z$  and  $y$  modes are denoted by the double black lines). The vertical arrows mark the half-frequencies of the pumps; the curved arrows denote the  $zzz$  (bottom) and  $yyy$  (top) EPR pairs. (b) Quantum graph states [30]: The initial EPR pairs from the OPO (top) turn, after a single beam splitter (gray ellipses), into a dual-rail CV cluster state (bottom), whose  $\pm 1/2$ -weight edges are color coded (contrary to the qubit case, weighted cluster CV states are still stabilizer states [30,31]).

eigenfrequencies, at which higher-photon-flux PDC yields two-mode squeezing, the bipartite entanglement mechanism of EPR pairs [29]. Our OPO was polarization degenerate: its two identical,  $x$ -cut PPKTP crystals were oriented  $90^{\circ}$  from each other in the  $(yz)$  plane, leading to the generation of two distinct sets of EPR pairs,  $zzz$  and  $yyy$ , as depicted in Fig. 1(a). We label the modes in the QOFC by integer  $n$  such that  $\omega_{n} = \omega_{0} + n\Delta \omega$ , with  $\omega_{0}$  an arbitrary origin and  $\Delta \omega$  the OPO free spectral range (FSR). The PDC phase-matching condition for EPR pair  $(n_{1}, n_{2})$  gives  $\omega_{p} = \omega_{n_{1}} + \omega_{n_{2}} = 2\omega_{0} + p\Delta \omega$ , where  $p = n_{1} + n_{2}$  is the pump index. For  $|p_{y} - p_{z}| = 2$ , i.e., pump frequencies differing by exactly twice the OPO FSR, all EPR pairs concatenate into the frequency sequence  $(\dots, -6, 5, -4, 3, -2, 1, 0, -1, 2, -3, 4, -5, \dots)$  [Fig. 1(a)] that extends to the whole phase-matching bandwidth in the QOFC. We recently measured the latter to be more than  $3.2\mathrm{THz}$  wide [24]. Hence, we estimate that our entangled QOFC, of mode spacing  $\Delta \omega = 0.95\mathrm{GHz}$ , extends over at least  $2N = 6$ , 700 modes (counting both polarizations).

This frequency sequence yields frequency-staggered EPR pairs in Fig. 1(b), top. As was shown for sequential CV entanglement [21,23], a balanced beam splitter entangles EPR pairs (which are also CV cluster states, up to local phase shifts), temporally staggered by an optical delay line, into the dual-rail CV cluster state depicted in Fig. 1(b), bottom. In our work, the staggering of the EPR pairs is spectral, caused by the decoherence-free pump frequency splitting.

To verify entanglement, we measured the joint squeezed operators called variance-based entanglement witnesses

[32] and nullifiers [31], which are the solutions of our OPO's Heisenberg equations. Nullifiers are directly related to the stabilizers of the generated cluster state (see the Supplemental Material [33]) and are also used in a more general entanglement check by the van Loock-Furusawa criterion [34]. Their derivation in the Heisenberg picture (see also Refs. [21,23,27]) uses the OPO's interaction-picture Hamiltonian,

$$
H = i \hbar \left[ \kappa_ {z} \sum_ {k = n _ {z}} ^ {N / 2} a _ {k} ^ {(z) \dagger} a _ {p _ {z} - k} ^ {(z) \dagger} + \kappa_ {y} \sum_ {l = n _ {y}} ^ {N / 2} a _ {l} ^ {(y) \dagger} a _ {p _ {y} - l} ^ {(y) \dagger} \right] + H. c., \tag {1}
$$

where  $n_{z,y} = \lceil p_{z,y} / 2\rceil$ , whose well-known solutions are the EPR nullifiers  $[Q_n^{(j)} - Q_{p_j - n}^{(j)}]e^{-r_j}$  and  $[P_n^{(j)} + P_{p_j - n}^{(j)}]e^{-r_j}$ ,  $j = y, z$ , where  $r_j = \kappa_j t$  are the squeezing parameters. A  $45^\circ$  polarization rotation matrix  $\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} / \sqrt{2}$ , applied to annihilation operators  $(a_n^{(z)}, a_n^{(y)})^T$ , transforms the EPR nullifiers into

$$
Q _ {p _ {z} - n, n} (r _ {z}) = \left\{\left[ Q _ {n} ^ {(z)} + Q _ {n} ^ {(y)} \right] - \left[ Q _ {p _ {z} - n} ^ {(z)} + Q _ {p _ {z} - n} ^ {(y)} \right] \right\} e ^ {- r _ {z}}, \tag {2}
$$

$$
P _ {p _ {z} - n, n} (r _ {z}) = \left\{\left[ P _ {n} ^ {(z)} + P _ {n} ^ {(y)} \right] + \left[ P _ {p _ {z} - n} ^ {(z)} + P _ {p _ {z} - n} ^ {(y)} \right] \right\} e ^ {- r _ {z}}, \tag {3}
$$

$$
Q _ {p _ {y} - n, n} \left(r _ {y}\right) = \left\{\left[ Q _ {p _ {y} - n} ^ {(z)} - Q _ {p _ {y} - n} ^ {(y)} \right] - \left[ Q _ {n} ^ {(z)} - Q _ {n} ^ {(y)} \right] \right\} e ^ {- r _ {y}}, \tag {4}
$$

$$
P _ {p _ {y} - n, n} \left(r _ {y}\right) = \left\{\left[ P _ {p _ {y} - n} ^ {(z)} - P _ {p _ {y} - n} ^ {(y)} \right] + \left[ P _ {n} ^ {(z)} - P _ {n} ^ {(y)} \right] \right\} e ^ {- r _ {y}}. \tag {5}
$$

Assuming (see the Supplemental Material [33] for an analysis of deviations from this case)  $r_z = r_y = r$ , taking the sum and difference of Eqs. (2) and (4) and applying a Fourier transform—a.k.a. a local  $\pi/2$  optical phase shift—to mode  $n$  yields the standard CV graph nullifiers [Eqs. (3) and (5) are unused for graph node  $n$  and for all others of the same parity ( $n \pm 2 \ldots$ ). They are the sole starting point for the nullifier derivations for graph nodes of opposite parity ( $n \pm 1 \ldots$ )

$$
\left[ P _ {n} ^ {(z)} - \frac {1}{2} \left(Q _ {p _ {z} - n} ^ {(y)} + Q _ {p _ {z} - n} ^ {(z)} + Q _ {p _ {y} - n} ^ {(z)} - Q _ {p _ {y} - n} ^ {(y)}\right) \right] e ^ {- r}, \tag {6}
$$

$$
\left[ P _ {n} ^ {(y)} - \frac {1}{2} \left(Q _ {p _ {z} - n} ^ {(y)} + Q _ {p _ {z} - n} ^ {(z)} - Q _ {p _ {y} - n} ^ {(z)} + Q _ {p _ {y} - n} ^ {(y)}\right) \right] e ^ {- r}, \tag {7}
$$

which correspond exactly to Fig. 1(b), bottom [30,31]. The measurement of these nullifiers requires homodyne detection at three different optical frequencies. However, one may also measure the more convenient observables of Eqs. (2)-(5), displayed in Fig. 2, which only require the two-tone homodyne detection implemented in Ref. [19].

A remarkable feature of our frequency-domain implementation is that merely tuning the pump spacing  $|p_y - p_z| = 2m$  yields  $m$  disjoint frequency sequences and,

![](images/c74f10fc7a7070017d1832166ff6080ceae03312d2eec53ff90d029a65ce279f.jpg)  
FIG. 2 (color online). Visualization of the measured nullifiers of Eqs. (2)-(5) [blue (left) and red (right) boxes] on the dual-rail graph state of Fig. 1(b). As shown in the text, simultaneous squeezing of  $Q_{-2,3}(r_z)$  and  $Q_{-2,1}(r_y)$  is equivalent to squeezing of the canonical nullifiers of Eqs. (6) and (7).

hence,  $m$  independent dual-rail cluster states. See Fig. 3 for  $m = 2$ , implemented in this work along with  $m = 1$  (Fig. 1). Note that all nullifier measurements are two tone in both cases, a simplification of the experimental procedure that is central to our proposed generalization of this work to the generation of CV cluster states with hypercubic lattices [27].

Experimental setup.-Our polarization-degenerate OPO had a bow-tie cavity (Fig. 4) of FSR  $\Delta \omega = 945.66\mathrm{MHz}$ . The OPO cavity length was actively stabilized by locking to a weak counterpropagating beam via a Pound-Drever-Hall (PDH) servo loop. The cavity eigenmode had two waist, where we placed the two PPKTP crystals, one  $(31\mu \mathrm{m})$  between the curved mirrors and one  $(131\mu \mathrm{m})$  between the flat mirrors. Great care was taken to suppress polarization cross talk between the crystals as well as resonant retroreflection from the OPO cavity (Supplemental Material [33]).

Two frequency-doubled, ultrastable continuous-wave (cw) Nd:YAG lasers, of frequency linewidth  $1\mathrm{kHz}$  at  $532~\mathrm{nm}$ , were used for the pump fields. The lasers were phaselocked together at a frequency difference  $2m\Delta \omega$  with  $m = 1$  or  $m = 2$ . The two pump beams entered the OPO through different paths to make a single pass through the yyy and zzz PPKTP crystals separately. To realize  $r_y = r_z$ , the pump powers were independently adjusted to compensate for the different waist at each crystal.

To test the dual-rail wire structure, the 4-mode nullifiers were measured, at all frequencies, by a two-tone balanced

![](images/55e1b7e1f16530c091e76c4c9583c5df7a3351a62b89c0c79e98d151c322879c.jpg)  
FIG. 3 (color online). Generation of two dual-rail quantum wires. The only difference with Fig. 1(a) is that the pump frequency difference is  $4\Delta \omega$  instead of  $2\Delta \omega$ . The frequency sequences of the wires are totally distinct:  $(\ldots, -8, 7, -4, 3, 0, -1, 4, -5, 8, \ldots)$  for the orange wire and  $(\ldots, -7, 6, -3, 2, 1, -2, 5, -6, 9, \ldots)$  for the purple wire.

homodyne detection system whose local oscillator (LO) was provided by another Nd:YAG cw laser, phasedlocked at (and sometimes offset from) the half-frequency of one of the pumps. The two LO tones were then generated by a phase electro-optic modulator (EOM) at a frequency  $\Omega = (n + \frac{1}{2})\Delta \omega$ , such that  $\omega_{LO} + \Omega = \omega_{n}$  and  $\omega_{LO} - \Omega = \omega_{p_y - n}$  for example. The EOM's  $\Omega_{\mathrm{max}} = 14$  GHz bandwidth yielded  $n_{\mathrm{max}} = 14$ , i.e.,  $2\times 15$  measurable modes (starting from  $n = 0$ ) for each polarization. (Replacing this EOM system with two phasedlocked, widely tunable  $1064~\mathrm{nm}$  diode lasers will give us access to the aforementioned 6,700 modes instead of the current 60). The first-order EOM sidebands were subsequently bandpass-filtered by a cavity of FSR  $\Delta \omega$ , PDH locked on the LO laser. The LO phase was adjusted by a piezoelectric transducer mirror and an electronic splitter-combiner network was used to form the nullifier signals.

Results.-We conducted three types of experimental tests: (i) measurements of the squeezed nullifiers of Eqs. (2)-(5), (ii) tests of the van Loock-Furusawa CV multipartite entanglement criterion [34], and (iii) tests of non-nullifying observables. The Supplemental Material [33] contains the entire data for all 60 measured modes for  $m = 1, 2$ . We present here a qualitative summary of the results. For (i), the LO was phaselocked exactly at half the frequency of the  $y$  pump to measure  $Q_{ij}(r_y)$ ,  $P_{ij}(r_y)$ , and likewise for  $z$ . In two-mode balanced homodyne detection, both the LO phase mirror and the phase  $\theta_o$  of the EOM drive (Fig. 4) contribute to determining the measured observable (Supplemental Material [33]). In practice, switching between Eqs. (2) and (3) [and between Eqs. (4) and (5)] was done by tuning  $\theta_o$  by  $\pm \pi / 2$  by simply changing the length of a coaxial cable, yielding identical squeezing signals.

![](images/2ee6f6fa9e5fdd1b246350f86a1dde8c389526d08a22731c63fb11c056cc9ffc.jpg)  
FIG. 4 (color online). Experimental setup. PLL: phaselock loop; HWP: half wave plate; PZT: piezoelectric transducer; PBS: polarizing beam splitter; SA: spectrum analyzer; AOM: acousto-optic modulator; EOM: electro-optic modulator; PDH: Pound-Drever-Hall lock loop.

![](images/d77c2757c7512d8b1c99258140cab977f510aa6277ef7cb008b2b0007a2f5fb4.jpg)

![](images/31f1a898365e02293a95f8dffb1a89ec7bd69609ea646bdd9ae0b443c32423b4.jpg)

![](images/fc26458c939aa0536a7b08d8ab185e7c135f098953639cdced09a96935b4dfff.jpg)

![](images/39d0c71a1c71c1271fa5df2e701c8d27ae11166a5eba71f791177d1fc5493e4b.jpg)

![](images/89b44e4e8e5de29e4c99182cd38f67662e11afdbc25ee64414a2df7afdd99aad.jpg)  
FIG. 5 (color online). Zero-span spectrum analyzer traces of raw squeezing measurements for  $m = 1$  and  $m = 2$  quantum wires. For each case, the QOFC is at the top, with the pump half-frequencies denoted by the blue (left) and red (right) arrows, and the quantum graph is beneath it. The highlighted modes indicate the LO sidebands. The black traces indicate the vacuum noise level. Center frequency:  $1.25\mathrm{MHz}$ . Resolution bandwidth:  $30\mathrm{kHz}$ . Video bandwidth:  $30\mathrm{Hz}$ .

![](images/ca9a8f4ad81c33ba3eb5b80984e36dddbce42768a92d2bf26fde36499d724e13.jpg)

Figure 5 displays typical squeezing signals in several crucial cases that evidence the graph structure. First, Figs. 5(a) and 5(b) prove a "unit cell" of the graph, i.e., which verifies Eqs. (6) and (7) for  $n = 1$  and  $m = 1$ . The uncorrected squeezing level was  $-3.2 \pm 0.2$  dB throughout our measurements. Deconvolving the "dark" electronic noise floor of  $-96$  dBm,  $-13$  dB from the vacuum noise level (the LO power was  $2$  mW at each photodiode), yielded an actual squeezing level of  $-3.4 \pm 0.2$  dB [33], enough to satisfy the van Loock-Furusawa inseparability criterion level of  $-3$  dB (Supplemental Material [33]). The last step (iii) was to check incorrect graph nodes, exemplified by

Fig. 5(e). The LO was phaselocked at an offset from half the frequency of one pump, which allowed us to measure nullifier observables over the "wrong" modes. Phase-independent excess quantum noise was observed, in good agreement with theoretical predictions (see the Supplemental Material [33]), proving that the measured observable is not a nullifier in this case. The complete set of such checks is prohibitively large, but all of the ones we tested gave the predicted negative result. All of these measurements demonstrate that a 60-mode dual-rail cluster state was generated in the QOFC.

As predicted above, changing the pump splitting to  $m = 2$  should yield two identical wires. Figures 5(c) and 5(d) show measurements demonstrating the unit cell of one of the wires. Note, in particular, that the successful nullifier measurement of Fig. 5(c) is the same as that of Fig. 5(e), which was not a nullifier for the  $m = 1$  pump splitting. Another such "devil's advocate" check is displayed in Fig. 5(f), in which cross correlations between the two wires are shown to be absent, even though this very same measurement yielded squeezing for  $m = 1$  [Fig. 5(b)]. We confirmed that two identical copies of a 30-mode dual-rail cluster state were generated in the QOFC.

Conclusion.-We demonstrated the ultracompact generation, in a single optical parametric oscillator, of recordsize cluster entanglement, thereby realizing the scalability potential of continuous variables in the quantum optical frequency comb. The number of verified entangled modes was limited to 60 by our EOM sideband generation bandwidth. On the basis of the exceptional  $zzz$  phasematching bandwidth measured in PPKTP at the particular wavelength of  $1064\mathrm{nm}$  [24], we have strong reason to believe that the maximum number of entangled modes in our experiment is at least 6,700. The OPO is pumped by only two frequencies, in contrast to the complicated spectrum required in our previous proposals [15,16]. In addition, simply tuning the pump frequency difference provides a decoherence-free method for creating multiple independent copies of the same state. The squeezing levels for the one-wire case and two-wire case were identical, showing that the number of copies does not affect their quality. On the basis of the  $60\mathrm{GHz}$  emission range of a typical frequency-doubled Nd:YAG pump laser, one can estimate that  $m = 30$  wires, of  $N / 30$  modes each, can be created in a  $1\mathrm{GHz}$ -FSR OPO. (Note that using amplified semiconductor lasers as pumps could significantly increase these figures.) We have also shown that interfering several OPOs identical to the one featured in this work should allow one to generate cluster states with hypercubic lattices [27]. Finally, another interesting feature of the multiple-copy generation is the availability of states whose entangled modes are widely frequency spaced (up to  $30\mathrm{GHz}$  in the above estimation), making them accessible for quantum information processing without requiring very high resolution dispersers [35].

We thank Pei Wang, Niranjan Sridhar, Matthew Pysher, and Wenjiang Fan for stimulating discussions. This work was supported by the U.S. National Science Foundation under Grants No. PHY-1206029 and No. PHY-0855632. N. C. M. was supported by the Australian Research Council under Grant No. DE120102204.

*ncmenicucci@gmail.com
†opfister@virginia.edu

[1] A. Einstein, B. Podolsky, and N. Rosen, Phys. Rev. 47, 777 (1935).  
[2] R. P. Feynman, Int. J. Theor. Phys. 21, 467 (1982).  
[3] P.W. Shor, in Proceedings, 35th Annual Symposium on Foundations of Computer Science, edited by S. Goldwasser (IEEE Press, Los Alamitos, CA, Santa Fe, NM, 1994), pp. 124-134.  
[4] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, U.K., 2000).  
[5] S. Hallgren, J. ACM 54, 4 (2007).  
[6] T.D. Ladd, F. Jelezko, R. Laflamme, Y. Nakamura, C. Monroe, and J.L. O'Brien, Nature (London) 464, 45 (2010).  
[7] T. Monz, P. Schindler, J. T. Barreiro, M. Chwalla, D. Nigg, W. A. Coish, M. Harlander, W. Hänsel, M. Hennrich, and R. Blatt, Phys. Rev. Lett. 106, 130506 (2011).  
[8] B. P. Lanyon, T. J. Weinhold, N. K. Langford, M. Barbieri, D. F. V. James, A. Gilchrist, and A. G. White, Phys. Rev. Lett. 99, 250505 (2007).  
[9] C.-Y. Lu, D. E. Browne, T. Yang, and J.-W. Pan, Phys. Rev. Lett. 99, 250504 (2007).  
[10] A. Politi, J. C. F. Matthews, and J. L. O'Brien, Science 325, 1221 (2009).  
[11] S. Barz, E. Kashefi, A. Broadbent, J.F. Fitzsimons, A. Zeilinger, and P. Walther, Science 335, 303 (2012).  
[12] X.-C. Yao, T.-X. Wang, W.-B. G. Hao-Ze Chen, A. G. Fowler, R. Raussendorf, Z.-B. Chen, N.-L. Liu, C.-Y. Lu, Y.-J. Deng, Y.-A. Chen, and J.-W. Pan, Nature (London) 482, 489 (2012).  
[13] O. Pfister, S. Feng, G. Jennings, R. Pooser, and D. Xie, Phys. Rev. A 70, 020302 (2004).  
[14] N.C. Menicucci, S.T. Flammia, H. Zaidi, and O. Pfister, Phys. Rev. A 76, 010302(R) (2007).

[15] N. C. Menicucci, S. T. Flammia, and O. Pfister, Phys. Rev. Lett. 101, 130501 (2008).  
[16] S. T. Flammia, N. C. Menicucci, and O. Pfister, J. Phys. B, 42, 114009 (2009).  
[17] G. Patera, C. Navarrete-Benlloch, G. de Valcárcel, and C. Fabre, Eur. Phys. J. D 66, 241 (2012).  
[18] N. C. Menicucci, preceding Letter, Phys. Rev. Lett. 112, 120504 (2014).  
[19] M. Pysher, Y. Miwa, R. Shahrokhshahi, R. Bloomer, and O. Pfister, Phys. Rev. Lett. 107, 030505 (2011).  
[20] J. Roslund, R. Medeiros de Araujo, S. Jiang, C. Fabre, and N. Treps, Nat. Photonics 8, 109 (2014).  
[21] S. Yokoyama, R. Ukai, S.C. Armstrong, C. Sornphiphatphong, T. Kaji, S. Suzuki, J. ichi Yoshikawa, H. Yonezawa, N.C. Menicucci, and A. Furusawa, Nat. Photonics 7, 982 (2013).  
[22] N.C. Menicucci, X. Ma, and T.C. Ralph, Phys. Rev. Lett. 104, 250503 (2010).  
[23] N.C. Menicucci, Phys. Rev. A 83, 062314 (2011).  
[24] P. Wang, W. Fan, and O. Pfister (to be published).  
[25] R. N. Alexander, S.C. Armstrong, R. Ukai, and N. C. Menicucci, arXiv:1311.3538.  
[26] N. C. Menicucci, P. van Loock, M. Gu, C. Weedbrook, T. C. Ralph, and M. A. Nielsen, Phys. Rev. Lett. 97, 110501 (2006).  
[27] P. Wang, M. Chen, N.C. Menicucci, and O. Pfister, arXiv:1309.4105.  
[28] T.F. Demarie, T. Linjordet, N.C. Menicucci, and G.K. Brennen, arXiv:1305.0409.  
[29] Z. Y. Ou, S. F. Pereira, H. J. Kimble, and K. C. Peng, Phys. Rev. Lett. 68, 3663 (1992).  
[30] N. C. Menicucci, S. T. Flammia, and P. van Loock, Phys. Rev. A 83, 042335 (2011).  
[31] M. Gu, C. Weedbrook, N.C. Menicucci, T.C. Ralph, and P. van Loock, Phys. Rev. A 79, 062318 (2009).  
[32] P. Hyllus and J. Eisert, New J. Phys. 8, 51 (2006).  
[33] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.112.120505 for all experimental data for all 60 modes, as well as experimental methods and the detail of entanglement checks.  
[34] P. van Loock and A. Furusawa, Phys. Rev. A 67, 052315 (2003).  
[35] S. A. Diddams, L. Hollberg, and V. Mbele, Nature (London) 445, 627 (2007).