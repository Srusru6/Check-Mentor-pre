# Boson Sampling with 20 Input Photons and a 60-Mode Interferometer in a  $10^{14}$ -Dimensional Hilbert Space

Hui Wang, $^{1,2}$  Jian Qin, $^{1,2}$  Xing Ding, $^{1,2}$  Ming-Cheng Chen, $^{1,2}$  Si Chen, $^{1,2}$  Xiang You, $^{1,2}$  Yu-Ming He, $^{1,2}$  Xiao Jiang, $^{1,2}$  L. You, $^{3}$  Z. Wang, $^{3}$  C. Schneider, $^{4}$  Jelmer J. Renema, $^{5}$  Sven Höfling, $^{4,6,1}$  Chao-Yang Lu $^{1,2}$  and Jian-Wei Pan $^{1,2}$

<sup>1</sup>Hefei National Laboratory for Physical Sciences at Microscale and Department of Modern Physics, University of Science and Technology of China, Hefei 230026, People's Republic of China

$^{2}$ Shanghai Branch, CAS Center for Excellence and Synergetic Innovation Center in Quantum Information and Quantum Physics, University of Science and Technology of China, Shanghai 201315, People's Republic of China

$^{3}$ State Key Laboratory of Functional Materials for Informatics, Shanghai Institute of Microsystem and Information Technology (SIMIT), Chinese Academy of Sciences, 865 Changning Road, Shanghai 200050, China

$^{4}$ Technische Physik, Physikalisches Institut und Wilhelm Conrad Rontgen-Center for Complex Material Systems, Universität Würzburg, Am Hubland, D-97074 Würzburg, Germany

$^{5}$ Adaptive Quantum Optics Group, Mesa+ Institute for Nanotechnology, University of Twente, P.O. Box 217, 7500 AE Enschede, Netherlands

$^{6}$ SUPA, School of Physics and Astronomy, University of St. Andrews, St. Andrews KY16 9SS, United Kingdom

![](images/f8505044b262b8f121e793d58ead67109110c6f2136752ed48b6baf2255576ad.jpg)

(Received 31 October 2019; revised manuscript received 19 November 2019; published 18 December 2019)

Quantum computing experiments are moving into a new realm of increasing size and complexity, with the short-term goal of demonstrating an advantage over classical computers. Boson sampling is a promising platform for such a goal; however, the number of detected single photons is up to five so far, limiting these small-scale implementations to a proof-of-principle stage. Here, we develop solid-state sources of highly efficient, pure, and indistinguishable single photons and 3D integration of ultralow-loss optical circuits. We perform experiments with 20 pure single photons fed into a 60-mode interferometer. In the output, we detect up to 14 photons and sample over Hilbert spaces with a size up to  $3.7 \times 10^{14}$ , over 10 orders of magnitude larger than all previous experiments, which for the first time enters into a genuine sampling regime where it becomes impossible to exhaust all possible output combinations. The results are validated against distinguishable samplers and uniform samplers with a confidence level of  $99.9\%$ .

DOI: 10.1103/PhysRevLett.123.250503

There has been significant progress in demonstrating the fundamental building blocks of quantum computers [1-11] and quantum algorithms [12-15]. Beyond small-scale demonstrations, the field of quantum computing is heading toward a new regime with increasing size and complexity, where the results cannot be efficiently simulated by classical means [16,17]. Such a goal has been referred to as quantum computational supremacy [18] and noisy intermediate-scale quantum technologies [19]. To this end, experimental efforts have been devoted to increase both the quality and quantity of qubits in various physical systems [6-11].

Boson sampling [20] is considered as a strong candidate for demonstrating the quantum computational supremacy. It is performed by sending  $n$  identical bosons into an  $m$ -mode ( $m > n$ ) Haar-random interferometer and sampling the output distribution in the photon number basis from the output Hilbert space of the final state. Because of the bosonic statistics, the probability amplitudes of the final state are related to the permanent of submatrices of the matrix  $U$  which describes the interferometer. It is strongly

believed that a moderate-size boson sampling machine will be intractable to be simulated with state-of-the-art classical computers [20-22]. It was very recently proposed that the first application of quantum supremacy would be the generation of verified random numbers [23,24].

So far, all implementations of boson sampling, using parametric down-conversion [25-35] or quantum dots [6,36-38], involved at most up to five detected single photons and 16 modes. In those proof-of-principle experiments, the full output photon distribution was easily calculated and could be completely verified, with even the earliest classical computers. An important goal is to scale up the boson sampling into a new, computationally interesting, regime. To this end, the roadmap is to construct multiphoton boson sampling machines with increasingly larger photon and mode numbers and faster sampling rates. For a boson sampler that is large enough to demonstrate a quantum advantage, the possible number of outputs will be so large that the output samples will be sparse; i.e., each output will be observed only once in any reasonable experiment. The size of the output Hilbert spaces, which

![](images/48588bb0a0ecd3d218fd8526d2076ba1b90ae227e754cf8cebd927ce4ed02761.jpg)  
FIG. 1. Experimental setup of boson sampling. A single InAs/GaAs quantum dot, resonantly coupled to a microcavity yielding a Purcell factor of  $\sim 18$ , is used to create pulsed resonance fluorescence single photons. For demultiplexing, 19 pairs of Pockels cells (PCs) and polarized beam splitters (PBSs) are used to actively translate a stream of photon pulses into 20 spatial modes. Optical fibers with different lengths are used to compensate time delays. The 20 input single photons are injected into a 3D integrated, 60-mode ultralow-loss photonic circuit (see Fig. 3 for more details), which consists of 396 beam splitters and 108 mirrors. Finally, the output single photons are detected by 60 superconducting nanowire single-photon detectors with efficiencies ranging from 0.6 to 0.82. All coincidence are recorded by a 64-channel coincidence count unit (not shown).

is one of the manifestations of the highly complex, high-entropy nature of boson sampling, is a function of both the photon and the mode number and can be calculated by  $\binom{m+n-1}{n}$ . The size of the Hilbert space also determines the number of random bits generated by a verified random number generator. The output state spaces ranged from 20 to 15504 in the previous experiments [6,25-38], in which all the possible output events were collected for proof-of-principle studies. But those sizes are still much smaller from the actual sampling regime in which quantum supremacy can be demonstrated.

In this work, we scale up the boson sampling with 20 photons injecting into a 60-mode interferometer where the output Hilbert space reaches  $3.7 \times 10^{14}$ , which is over 10 orders of magnitude larger than the previous work. In such an exponentially large Hilbert space, for the first time, it becomes impossible in a boson sampling experiment to exhaust all possible output combinations.

We start by describing the experimental setup of our boson sampling machines, which is illustrated in Fig. 1 for an overview. Pulsed single-photon streams are produced from an InAs/GaAs quantum dot cooled to  $4\mathrm{K}$  and deterministically coupled to a micropillar cavity [39,40]. Under pulsed resonant laser excitation [41], a clear Rabi oscillation of the resonance fluorescence single-photon counts as a function of the pump power is shown in Fig. 2(a). At a pulse with a repetition rate of  $76\mathrm{MHz}$ , we eventually detect  $\sim 16$  million counts per second single-mode fiber-coupled photon counts on a superconducting nanowire single-photon detector with an efficiency of  $82\%$ . The single-photon purity of the solid-state source is characterized by Hanbury Brown-Twiss measurements, which reveal a second-order correlation of 0.025(1) at zero-time delay [Fig. 2(b)], indicating a single-photon

purity of  $97.5\%$ . The photon indistinguishability is then measured by Hong-Ou-Mandel interferometers with two photon emission time separation up to  $\sim 6.5~\mu \mathrm{s}$ . The measured photon indistinguishability is 0.954(1) at a short time separation of  $\sim 13$  ns, which slightly drops to a plateau of 0.923(1) between  $\sim 1$  and  $\sim 6.5~\mu \mathrm{s}$  [Fig. 2(c)]. Such a semiconductor source of polarized, high-brightness, high-purity, and near-transform-limited single photons is the central quantum resource for boson sampling.

The single-photon stream is then deterministically demultiplexed into 20 spatial modes using fast optical switches, arranged in a treelike structure (see Fig. 1). Each switch consists of a polarizing beam splitter (with an extinction ratio  $>2000:1$ ) and an active Pockels cell that is synchronized to the laser pulses and on demand rotates the photon polarization (with an extinction ratio  $>100:1$ ). The measured average system efficiency of the switches (including the transmission efficiency, single-mode fiber coupling efficiency, and extinction ratio of Pockels cells) is  $83\%$  [42]. After finely compensating for their relative time delay, these 20 demultiplexed modes are fed into a fully connected 60-port linear optical network. Finally, the 60 output ports are fed into 60 superconducting nanowire single-photon detectors with their efficiencies varying from  $60\%$  to  $82\%$ .

Multimode interferometers are usually constructed by beam splitters and phase shifters in a triangular [6,46] or rectangular [38,47] configuration. Here, we put forward a new, more compact 3D design that combines phase stability, full connectivity, matrix randomness, near-perfect wavepacket overlap, and near-unity transmission rate simultaneously [see Figs. 3(a) and 3(b) and its caption] but at the cost of nonuniversality and nonreconfigurability. Such an optical network consists of 396 beam splitters and 108

![](images/2cb7ba4561956b6a0c9b92838ded019742dd43d2121d4915014248b75bf31622.jpg)  
FIG. 2. Characterization of the single-photon source. (a) By varying the amplitude of the pumping laser field, a Rabi oscillation up to 4 is observed. At  $\pi$  pulse,  $\sim 16.3$  million single photons per second are recorded by a superconducting nanowire single-photon detector. (b) Characterization of single-photon purity using the second-order correlation function. The strongly antibunched peak at zero-time delay reveals  $g^{2}(0) = 0.025(1)$  (c) Measurement of photon indistinguishability by Hong-Ou-Mandel interference between two photons with different emission time separations. The extracted photon indistinguishabilities are  $0.954(1)$ ,  $0.948(1)$ ,  $0.933(1)$ ,  $0.929(1)$ ,  $0.922(1)$ , and  $0.923(1)$  at emission time separations of 13 ns, 39 ns, 210 ns, 395 ns,  $1.8\mu s$ , and  $6.5\mu s$ , respectively. The data are fitted by a model considering Markov noise.

![](images/bfa0358b037acd7ebbfd73644871e4dc0827501c11a6ccd26705e629bc5f6cb7.jpg)

![](images/46c4ef1166ad725a02d345a0b0b3baeaa994f046d08a85d95e924fc1fe060fac.jpg)

mirrors and can be used to implement  $60 \times 60$  unitary transformations. We use Mach-Zehnder-type interferometry to calibrate spatial overlap between any two input ports, which shows an average visibility above  $99.9\%$ . From all 20 input ports, the transmission rate of the whole optical network is measured to be 0.987(2), and the average coupling efficiency in all 60 output ports is 0.902(37).

We use a narrow-band laser to reconstruct the corresponding unitary matrix of the 3D  $60 \times 60$  interferometer [48]. The measured elements of the amplitudes and phases are shown in Figs. 3(c) and 3(d), respectively. If the generated matrix is unitary, the product of this matrix and its Hermitian conjugate should be an identity matrix. The result is plotted in Fig. 3(e), showing that the average of the nondiagonal elements is 0.01(1), thus confirming the high degree of unitarity of the generated matrix. Moreover, for the hardness arguments regarding boson sampling to hold, the matrix should be randomly drawn according to the Haar measure. We compare our measured elements with ideal Haar-random matrix elements. Figure 3f [3(g)] shows the statistical frequency of the measured 1200 elements of amplitude (phase), in which the distribution of phase agrees with the predication from the Haar-random matrix, while the distribution of amplitude has an overlap with that expected from the Haar-random case of 0.78(7).

We use fidelity  $(F)$  and total variation distance  $(D)$  to quantify the performance of the boson samplers, which are defined by  $F = \sum_{i}\sqrt{q_i p_i}$  and  $D = (1 / 2)\sum_{i}|q_{i} - p_{i}|$  ( $p_i$  and  $q_{i}$  denote the theoretical and experimental probability of the ith basis, respectively). For a perfect boson sampler, the fidelity should equal to 1 and the distance should be 0. To test that the boson sampling setup works properly, we first analyze arbitrary two-photon input configurations, of which there are 190 in the 20-input setup. We obtain  $\sim 300000$  samples for each configuration ( $\sim 170$  times larger than the state spaces). The measured fidelities and distances between the experimental and ideal cases are

illustrated in Fig. 4(a), from which an average fidelity of 0.995(3) and distance of 0.043(5) are extracted. If we use the Clifford-Clifford sampling algorithm [49] to generate the same number of samples on a classical computer, the fidelity (total variation distance) is 0.998 (0.035), which is only slightly better than those from the quantum machine. This indicates a high level of interference between any two modes in the 60-mode interferometer. The small error in the two-photon test is mainly from the finite sample number and statistics. Next, we register the whole output distributions of the noncollision events from three- and four-photon boson sampling, which are plotted in Figs. 4(b) and 4(c), respectively. The measured fidelities and distances are 0.988(1) and 0.095(1) for the former and 0.984(1) and 0.143(1) for the latter. These results are in excellent agreement with the theory taking into account the realistic single-photon source and optical network [45,50-53], which confirms that the boson-sampler works properly.

As the photon number increases, the output Hilbert spaces expand exponentially, which makes it infeasible to register the whole distribution—but only sampling is possible, a regime long waited for in boson sampling experiments. Meanwhile, due to the passive nature of the boson sampling protocol, the output multiphoton coincidence rate drops exponentially. In our experiment, when the photon number exceeds four, the registered distributions become sparse; that is, most of the output combinations record zero events.

We operate both the standard Aaronson-Arkhipov model [20] and Aaronson-Brod model of boson sampling [54] with photon loss. In the former, all the  $n$  input photons are detected in the output. In the latter,  $n + k$  photons are sent in, but in the output only  $n$ -fold coincidences are detected. The sampling rate of the latter is enhanced by a factor of approximately  $\binom{n+k}{n}$  compared to the former. Ongoing complexity analysis [45,50,54] shows that the loss rate in Aaronson-Brod sampling should be under a certain

![](images/5ad62c090461fd067a4f1dd0d540a9903e12862246c1cbcb0a27bc2127e2fa3b.jpg)

![](images/0bf182bd3ca507b50d9f7d20af7be82b9660741dc5445e60a22aa7b502d1c314.jpg)

![](images/dd8d9d0941d0f683b27d9644f250129ebb8a697ed133e497300f8a98daf9985a.jpg)

![](images/730b1bc3b50b9a2f541acf4a5ddb8f2ccf56f8fed05aca134b98dfb53335aa00.jpg)

![](images/1b3bb535866495169a1499358eb98a58350dda993d62aa04ff3c36d782107f46.jpg)

![](images/1225b55af334b1dec614ba441d50ceea61c7921bfd8206622efba477cf80e898.jpg)  
FIG. 3. Construction and characterization of the 60-mode photonic network. (a) The 60-mode interferometer consists of one rectangular piece and two triangular pieces. The rectangular is fabricated by bonding (through intermolecular force) six trapezoidal pieces with a size of  $28.28 \times 28.28 \times 4.00 \mathrm{~mm}^3$ . The triangular is constructed in a similar way, with a size of  $24.00 \times 24.00 \times 20.00 \mathrm{~mm}^3$ . The bonding interfaces are coated with random polarization-dependent beam-splitting ratio. The trapezoidal pieces are cut and bounded with a dimension tolerance of  $<5 \mu \mathrm{m}$  and parallel precision better than  $5^{\prime \prime}$ . The design ensures that any possible spatial mismatch is much smaller than the coherence length of the quantum-dot single photons ( $\sim 30 \mathrm{~mm}$ ). (b) Illustration of light propagation inside the 3D photonic circuit. The rectangular piece has six horizontal ten-mode layers, while the two triangular ones have ten vertical six-mode layers. In the rectangular piece, only the photons in the same horizontal layer can interfere with each other but not with vertically different layers. After that, ten vertical layers are incorporated, which are to make the photons from different horizontal layers interfere with each other. Therefore, the interferometer is fully connected. (c) The measured 1200 elements of amplitude. These values are determined by the recorded counts of the 60 single-photon detectors when we inject photons in every input port one by one. (d) The measured 1200 elements of amplitude. These elements are measured using Mach-Zehnder-type interference with a narrow-band laser. (e) Unitarity test of the reconstructed matrix. All output probabilities are normalized to unity, corresponding to 20 diagonal elements. The average of all off-diagonal elements is as small as 0.01(1), confirming that the matrix is well reconstructed. (f) Statistical histogram of 1200 elements of amplitude. (g) Statistical histogram of 1200 elements of phase. The phase is uniformly distributed from  $-\pi$  to  $\pi$ .

![](images/b976b46d0da501ec49eecdfbc5392e319d5194d4d6f729bdbf8755e1b00e7901.jpg)

threshold to achieve a quantum advantage. In this work, we perform the standard model of boson sampling for coincidence detection of 10 photons or below, and the lossy boson sampling in the regime of more involved photons up to 20 input and 14 detected photons. As plotted in Fig. 4(d), the coincidence rate in the standard boson sampling is  $295\mathrm{Hz}$  for five photons, which is 60 times higher than in Ref. [6], and drops to  $0.01\mathrm{Hz}$  for ten-photon coincidence. Tolerating one-photon loss can give rise to an

approximately 3-10 times enhancement in the sampling rate, as plotted in Fig. 4(d). For 20 input photons with six lost, we detect a 14-photon coincidence rate of  $\sim 6$  per hour, which allows us to obtain 150 samples after a collection time of  $26\mathrm{h}$ . In all settings, we obtain at least a few hundred samples to characterize our multiphoton boson sampler.

Using the boson sampling parameters in this experiment, we calculate the state spaces and plot them in Fig. 4(e).

![](images/f85c04aa921b3ed315761fbac919dbff7587385f867d8f2049b6801e3aba71c1.jpg)

![](images/a46d070e6a4a1e5a2b85fb94bcfecc5fee3a8639d9e3920437fb048eb8089737.jpg)

![](images/6da21deb479a647e49bcad7ab4509b0978bc1df54d75d64df57d1874ecc9a0d7.jpg)

![](images/4b97ef573e12beb20bf781f0baf54c07ae3bfc8b1aced4a5fd502ca25d111e19.jpg)

![](images/82e00ae27571bdbb3da28103c282bd1ba5aece00fe7f33e37af7972231823fbf.jpg)  
FIG. 4. (a) Summary of distance (purple) and fidelity (orange) of all 190 possible two-photon boson sampling tests. The averaged distance and distance are 0.043(7) and 0.996(1), respectively. (b) Reconstructed three-photon distribution for an input combination (2,10,12). (c) Reconstructed four-photon distribution for an input combination (1,2,4,7). (d) Boson sampling rates with different settings of input photons and lost photons. (e) Summary of the dimensions of output Hilbert space of all previous work and this experiment (red dots).

While the previous experiments were limited to state spaces between 20 and 15 504, our work achieves Hilbert space dimensions up to  $3.7 \times 10^{14}$  in the 20-photon-input 14-output boson sampling, which is more than 10 orders of magnitude larger than before. With such enormous output state spaces, it is no longer possible to collect the full distribution as in the previous small-scale experiments [6,25-38]. In fact, theoretically calculating the full probability distribution in the 20-photon-input 14-output boson sampling will take hours using supercomputers.

While full certification of large-scale boson sampling is also strongly conjectured to be intractable for classical computation [55], there are methods for validating boson sampling that can provide supporting or circumstantial evidence for the correct operation of this protocol. We use two broadly implemented statistical tests among the various validation protocols developed [6,29-38,56-63] to first rule out a possible hypothesis that the input photons are distinguishable, which is very relevant to the experimental implementations, because single-photon indistinguishability is most susceptible to the decoherence. We

perform Bayesian analysis [29] for various input-output configurations. Typical results with 14-20 input photons are plotted in Fig. 5(a), showing an increasing difference between indistinguishable bosons (solid) and distinguishable bosons (hollow). With  $\sim 50$  samples, these analyses already reach confidence levels of  $\sim 99.9\%$  that these results are more likely from indistinguishable bosons. The validation data using the likelihood ratio test [29] and that for other photon numbers can be found in Ref. [42]. Second, we aim to rule out uniform distribution; that is, the samples scatter uniformly to the overall distribution. We employed the row-norm estimator test [56], where the increasing difference between experimental data (solid) and simulated uniform samples (hollow) indicates that our results cannot be reproduced by a uniform sampler [Fig. 5(b)]. We hope our experiment will inspire new theoretical methods for quantitative characterizations for large-scale boson sampling, for example, to develop validation schemes which have some degree of computational security against spoofing, or to improve the existing classical simulation strategies for realistic boson samplers.

![](images/14ba41811237efd6b813b6405ed951793b8e3dc0af87178e63091e8dbf5b4704.jpg)  
FIG. 5. Validation of the boson sampling results. (a) Bayesian analysis of typical 11- to 14-photon boson sampling results. The solid points are from Bayesian analysis by updating every experimental data, which reach a level of  $99.9\%$  with only  $\sim 50$  samples. The open dots are from Bayesian analysis by updating simulated data of distinguishable bosons, which quickly converge to 0. These results confirm that the experimental events are from a genuine boson sampler, rather than a distinguishable sampler. (b) Designed row-norm estimator to discriminate experimental data from a uniform sampler. The solid dots are updated by the experimental data, while the open dots are from a simulated uniform sampler. The increasing differences between them can exclude the uniform sampling hypothesis. For clarity, in each panel, the four different datasets are displayed with an offset in the  $x$  axis.

![](images/c30cb7e3da8dcac278af8f6d0cfdb8916480f2f9bbcae64b0908db56f6c10744.jpg)

Our results show that we can experimentally access quantum states of 20 photons in a  $60 \times 60$  interferometer and use it to perform a quantum computational task increasingly difficult for classical computers with a growing number of photons. To bring the current work in relation with other general photonic qubit experiments, the Hilbert space size of our experiment is  $3.7 \times 10^{14} \sim 2^{48}$  (equivalent to 48 qubits), which is orders of magnitude larger than all previous work [7,33,64,65]. The mode dimension of the 3D interferometer in our design can be directly doubled by using spatial-polarization encoding and scaled up to a few hundreds. With ongoing improvements of single-photon source [66] and detection efficiency, our experimental approach points a way to the noisy intermediate-scale quantum regime through boson sampling.

This work was supported by the National Natural Science Foundation of China, the Chinese Academy of Science, the Anhui Initiative in Quantum Information Technologies, the Science and Technology Commission of Shanghai Municipality, the National Fundamental Research Program, the State of Bavaria, and NWO veni.

H. W., J. Q., X. D., and M.-C. C. contributed equally to this work.

Note added.—Recently, we became aware of a related work on random circuit sampling with 53 superconducting qubits [67].

[1] D. Leibfried, R. Blatt, C. Monroe, and D. Wineland, Rev. Mod. Phys. 75, 281 (2003).

[2] P. Kok, W. J. Munro, K. Nemoto, T. C. Ralph, J. P. Dowling, and G. J. Milburn, Rev. Mod. Phys. 79, 135 (2007).  
[3] J. Clark and F. K. Wilhelm, Nature (London) 453, 1031 (2008).  
[4] T. D. Ladd, F. Jelezko, R. Laflamme, Y. Nakamura, C. Monroe, and J. L. OBrien, Nature (London) 464, 45 (2010).  
[5] J.-W. Pan, Z.-B. Chen, C.-Y. Lu, H. Weinfurter, A. Zeilinger, and M. Zukowski, Rev. Mod. Phys. 84, 777 (2012).  
[6] H. Wang et al., Nat. Photonics 11, 361 (2017).  
[7] X.-L. Wang et al., Phys. Rev. Lett. 120, 260502 (2018).  
[8] C. Neill et al., Science 360, 195 (2018).  
[9] N. Friis et al., Phys. Rev. X 8, 021012 (2018).  
[10] A. Omran et al., Science 365, 570 (2019).  
[11] C. Song et al., Science 365, 574 (2019).  
[12] P. W. Shor, in Proceedings of the 35th Annual Symposium on Foundations of Computer Science, Santa Fe, NM, USA (IEEE, 1994).  
[13] L. K. Grover, Phys. Rev. Lett. 79, 325 (1997).  
[14] A. W. Harrow, A. Hassidim, and S. Lloyd, Phys. Rev. Lett. 103, 150502 (2009).  
[15] A. Peruzzo, J. McClean, P. Shadbolt, M.-H. Yung, X.-Q. Zhou, P. J. Love, A. Aspuru-Guzik, and J. L. O'Brien, Nat. Commun. 5, 4213 (2014).  
[16] A. W. Harrow and A. Montanaro, Nature (London) 549, 203 (2017).  
[17] A. P. Lund, M. J. Bremner, and T. C. Ralph, Quantum Inf. Comput. 3, 15 (2017).  
[18] J. Preskill, in Proceedings of the Rapporteur Talk at the 25th Solvay Conference on Physics, Brussels (World Scientific, 2012).  
[19] J. Preskill, Quantum 2, 79 (2018).  
[20] S. Aaronson and A. Arkhipov, in Proceedings of the ACM Symposium on Theory of Computing (ACM, New York, 2011), pp. 333-243.  
[21] A. Neville, C. Sparrow, R. Clifford, E. Johnston, P.M. Birchall, A. Montanaro, and A. Laing, Nat. Phys. 13, 1153 (2017).

[22] J. Wu et al., Natl. Sci. Rev. 5, 715 (2018).  
[23] S. Aaronson and L. Chen, arXiv:1612.05903.  
[24] S. Aaronson, Certified randomness from quantum supremacy, see https://www.scottaarsonson.com/talks/.  
[25] M. A. Broome, A. Fedrizzi, S. Rahimi-Keshari, J. Dove, S. Aaronson, T. C. Ralph, and A. G. White, Science 339, 794 (2013).  
[26] J. B. Spring et al., Science 339, 798 (2013).  
[27] M. Tillmann, B. Dakic, R. Heilmann, S. Nolte, A. Szameit, and P. Walther, Nat. Photonics 7, 540 (2013).  
[28] A. Crespi, R. Osellame, R. Ramponi, D.J. Brod, E.F. Galvão, N. Spagnolo, C. Vitelli, E. Maiorino, P. Mataloni, and F. Sciarrino, Nat. Photonics 7, 545 (2013).  
[29] N. Spagnolo et al., Nat. Photonics 8, 615 (2014).  
[30] J. Carolan et al., Nat. Photonics 8, 621 (2014).  
[31] J. Carolan et al., Science 349, 711 (2015).  
[32] M. Bentivegna et al., Sci. Adv. 1, e1400255 (2015).  
[33] H.-S. Zhong et al., Phys. Rev. Lett. 121, 250505 (2018).  
[34] H.-S. Zhong et al., Sci. Bull. 64, 511 (2019).  
[35] S. Paesani, Y. Ding, R. Santagati, L. Chakhmakhchyan, C. Vigliar, K. Rottwitt, L. K. Oxenlowe, J. Wang, M. G. Thompson, and A. Laing, Nat. Phys. 15, 925 (2019).  
[36] Y. He et al., Phys. Rev. Lett. 118, 190501 (2017).  
[37] J. C. Lrecordo, M. A. Broome, P. Hilaire, O. Gazzano, I. Sagnes, A. Lemaitre, M. P. Almeida, P. Senellart, and A. G. White, Phys. Rev. Lett. 118, 130503 (2017).  
[38] H. Wang et al., Phys. Rev. Lett. 120, 230502 (2018).  
[39] X. Ding et al., Phys. Rev. Lett. 116, 020401 (2016).  
[40] N. Somaschi et al., Nat. Photonics 10, 340 (2016).  
[41] Y.-M. He, Y. He, Y.-J. Wei, D. Wu, M. Atature, C. Schneider, S. Hofling, M. Kamp, C.-Y. Lu, and J.-W. Pan, Nat. Nanotechnol. 8, 213 (2013).  
[42] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevLett.123.250503 for detailed descriptions of the single-photon source, the demultiplexers, the 3D interferometer, validation and the relevant supporting data, which includes Refs. [31,43-45].  
[43] D.J. Brod, E.F. Galvao, A. Crespi, R. Osellame, N. Spagnolo, and F. Sciarrino, Adv. Opt. Photonics 1, 034001 (2019).  
[44] J. Renema, V. Shchesnovich, and R. Garcia-Patron, arXiv: 1809.01953.

[45] J. J. Renema, A. Menssen, W. R. Clements, G. Triginer, W. S. Kolthammer, and I. A. Walmsley, Phys. Rev. Lett. 120, 220502 (2018).  
[46] M. Reck, A. Zeilinger, H. J. Bernstein, and P. Bertani, Phys. Rev. Lett. 73, 58 (1994).  
[47] W. R. Clements, P. C. Humphreys, B. J. Metcalf, W. S. Kolthammer, and I. A. Walmsley, Optica 3, 1460 (2016).  
[48] S. Rahimi-Keshari, M. A. Broome, R. Fichler, A. Fedrizzi, T. C. Ralph, and A. G. White, Opt. Express 21, 13450 (2013).  
[49] P. Clifford and R. Clifford, arXiv:1706.01260.  
[50] M. Oszmaniec and D.J. Brod, New J. Phys. 20, 092002 (2018).  
[51] P.P. Rohde and T.C. Ralph, Phys. Rev. A 85, 022332 (2012).  
[52] M. C. Tichy, Phys. Rev. A 91, 022316 (2015).  
[53] V. S. Shchesnovich, Phys. Rev. A 91, 013844 (2015).  
[54] S. Aaronson and D.J. Brod, Phys. Rev. A 93, 012335 (2016).  
[55] D. Hangleiter, M. Kliesch, J. Eisert, and C. Gogolin, Phys. Rev. Lett. 122, 210502 (2019).  
[56] S. Aaronson and A. Arkhipov, Quantum Inf. Comput. 14, 1383 (2014).  
[57] M. C. Tichy, K. Mayer, A. Buchleitner, and K. Mølmer, Phys. Rev. Lett. 113, 020502 (2014).  
[58] M. Walschaers, J. Kuipers, J.-D. Urbina, K. Mayer, M.C. Tichy, K. Richter, and A. Buchleitner, New J. Phys. 18, 032001 (2016).  
[59] T. Giordani et al., Nat. Photonics 12, 173 (2018).  
[60] I. Agresti, N. Viggianiello, F. Flamini, N. Spagnolo, A. Crespi, R. Osellame, N. Wiebe, and F. Sciarrino, Phys. Rev. X 9, 011013 (2019).  
[61] D.J. Brod, E.F. Galvao, N. Viggianiello, F. Flamini, N. Spagnolo, and F. Sciarrino, Phys. Rev. Lett. 122, 063602 (2019).  
[62] M. Walschaers, arXiv:1908.08370.  
[63] F. Flamini, N. Spagnolo, and F. Sciarrino, Rep. Prog. Phys. 82, 016001 (2019).  
[64] J. Wang et al., Science 360, 285 (2018).  
[65] M. Krenn, M. Huber, R. Fickler, R. Lapkiewicz, S. Ramelow, and A. Zeilinger, Proc. Natl. Acad. Sci. U.S.A. 111, 6243 (2014).  
[66] H. Wang et al., Nat. Photonics 13, 770 (2019).  
[67] F. Arute et al., Nature (London) 574, 505 (2019).