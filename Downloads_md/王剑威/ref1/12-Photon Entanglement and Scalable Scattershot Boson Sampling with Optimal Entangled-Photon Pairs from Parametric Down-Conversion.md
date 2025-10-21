# 12-Photon Entanglement and Scalable Scattershot Boson Sampling with Optimal Entangled-Photon Pairs from Parametric Down-Conversion

Han-Sen Zhong, $^{1,2}$  Yuan Li, $^{1,2}$  Wei Li, $^{1,2}$  Li-Chao Peng, $^{1,2}$  Zu-En Su, $^{1,2}$  Yi Hu, $^{1,2}$  Yu-Ming He, $^{1,2}$  Xing Ding, $^{1,2}$

Weijun Zhang, $^{3}$  Hao Li, $^{3}$  Lu Zhang, $^{3}$  Zhen Wang, $^{3}$  Lixing You, $^{3}$  Xi-Lin Wang, $^{1,2}$  Xiao Jiang, $^{1,2}$  Li Li, $^{1,2}$

Yu-Ao Chen, $^{1,2}$  Nai-Le Liu, $^{1,2}$  Chao-Yang Lu, $^{1,2}$  and Jian-Wei Pan $^{1,2}$

$^{1}$ Hefei National Laboratory for Physical Sciences at Microscale and Department of Modern Physics,

University of Science and Technology of China, Hefei, Anhui 230026, China

$^{2}$ CAS Centre for Excellence and Synergetic Innovation Centre in Quantum Information and Quantum Physics,

University of Science and Technology of China, Hefei, Anhui 230026, China

${}^{3}$  State Key Laboratory of Functional Materials for Informatics,Shanghai Institute of Microsystem

and Information Technology (SIMIT), Chinese Academy of Sciences,

865 Changning Road, Shanghai 200050, China

![](images/2ad0992548c53fa96baf4c7826c6deb8ed4784c669c3820dd90e14a262902926.jpg)

(Received 10 October 2018; published 21 December 2018)

Entangled-photon sources with simultaneously near-unity heralding efficiency and indistinguishability are the fundamental elements for scalable photonic quantum technologies. We design and realize a degenerate telecommunication wavelength entangled-photon source from an ultrafast pulsed laser pumped spontaneous parametric down-conversion (SPDC), which shows simultaneously  $97\%$  heralding efficiency and  $96\%$  indistinguishability between independent single photons without narrow-band filtering. Such a beamlike and frequency-uncorrelated SPDC source allows generation of the first 12-photon genuine entanglement with a state fidelity of  $0.572 \pm 0.024$ . We further demonstrate a blueprint of scalable scattershot boson sampling using 12 SPDC sources and a  $12 \times 12$  mode interferometer for three-, four-, and five-boson sampling, which yields count rates more than 4 orders of magnitude higher than all previous SPDC experiments.

DOI: 10.1103/PhysRevLett.121.250505

Spontaneous parametric down-conversion (SPDC) [1] has been the most widely used workhorse for producing entangled-photon pairs, which was exploited for tests of Bells inequalities [2-4], quantum key distribution [5-7], and dense coding [8]. The development of multiphoton interferometry [9], which relied on quantum interference between independent photons, opened the way to coherent control of a large number of photonic qubits. This allowed the generation of Greenberger-Horne-Zeilinger (GHZ) entanglement [10-17] and tests of GHZ theorem [18] and found many applications in quantum information protocols, such as quantum teleportation [19-21], quantum metrology [22-24], quantum simulation [25], and boson sampling [26-32].

In the past two decades, the number of genuinely multiparticle entangled photons from SPDC has been increased up to ten [15,16]. Yet, a more scalable implementation remained challenging, largely due to the lack of a perfect entangled-photon source produced by ultrafast laser pumped SPDC, where the photonic entanglement fidelity, the collection efficiency, and the indistinguishability between independent photons are simultaneously engineered to close to unity. Such a perfect source can immediately enable previously formidable tasks, for example, scalable scattershot boson sampling [33], heralded

two-photon entanglement at distant locations for Bell test and device-independent quantum key distribution [34-36], and serve as a scalable building block for multiplexing [37-39] that can overcome the probabilistic nature of SPDC.

In the SPDC [40], the conservation of energy and momentum can naturally induce strong correlations in multiple degrees of freedom between the two converted photons, including their polarization, frequency, and time. In the view of quantum engineering, the single photons should be efficiently prepared in a pure state with a single degree of freedom. However, usually the uncontrolled entanglement in the frequency and/or time can significantly degrade the entanglement in the polarization. In the early experiments, to eliminate the spectral correlation of the photon pairs, the most straightforward way was passive narrow-band (typical linewidth  $\sim 3\mathrm{nm}$ ) spectral filtering, which significantly sacrificed the brightness and collection efficiency of the entangled photons [10-13]. A more efficient method was to employ the interferometric Bell-state synthesizer [41] to separate the correlation between the polarization and the spectral bandwidth, allowing for a more selective (3-nm linewidth for  $e$ -polarized and 8-nm for  $o$ -polarized photons) and thus more economical narrow-band filtering [14]. Further, beamlike SPDC [42]

was developed with the photon pairs in the form of two separate Gaussian-like beams, which had higher brightness and efficiency coupling into a single spatial mode [15,43] than those from the noncollinear SPDC, where the collection was at intersections of the two down-converted photon rings. We note that, however, in these previous multiphoton entanglement experiments [10-16], the  $e-$  and  $o$ -polarized photons were frequency correlated, as evident from the observed tilted two-photon joint spectral intensity distribution, which caused a trade-off between the efficiency and the indistinguishability. There has been important progress in preparing heralded single photons in frequency-uncorrelated pure quantum state [44-46], yet the simultaneous combination of near-unity entanglement fidelity, indistinguishability, and collection efficiency remained an outstanding goal.

Here, we design and experimentally realize an optimal SPDC source of entangled photons at telecommunication wavelength by combining the techniques of frequency-uncorrelated and beamlike SPDC. For the photon pair free from any correlation in their spatiotemporal degrees of freedom, it is necessary that the two-photon joint amplitude function is factorable [47]. We find a suitable parameter regime that fulfills the condition using a BBO crystal with a thickness of  $6.3\mathrm{mm}$ , pump laser wavelength of  $775~\mathrm{nm}$  (generating photon pairs centered around  $1550~\mathrm{nm}$ ), and pulsed laser bandwidth of  $5.5\mathrm{nm}$  (see Supplemental Material [48]). Our design of the entangled-photon source in a beamlike SPDC configuration is illustrated in Fig. 1(a). The pulsed laser passes through an arrangement of two  $\mathrm{YVO_4}$  beam displacers (BDs) and half-wave plates (HwPs) to separate the laser beam into two paths by  $2.6\mathrm{mm}$  apart. The two beams focus on one  $\beta$ -barium-borate (BBO) crystal to generate two identical photon pairs in the states  $|V_{1}\rangle |H_{2}\rangle$  and  $|V_{1^{\prime}}\rangle |H_{2^{\prime}}\rangle$  via beamlike type-II SPDC, where the subscripts denote the spatial modes as drawn in Fig. 1(a). The  $|V_{1^{\prime}}\rangle |H_{2^{\prime}}\rangle$  pair is then rotated using a HWP to its orthogonal state  $|H_{1^{\prime}}\rangle |V_{2^{\prime}}\rangle$  and recombined with  $|V_{1}\rangle |H_{2}\rangle$  into a single spatial mode using two BDs. Tilting the two BDs allows for precise temporal tuning and fine spatial compensation of the photon pairs that prepares them into an entangled Bell state:  $(|H_1\rangle |V_2\rangle +|V_1\rangle |H_2\rangle) / \sqrt{2}$ , with a measured visibility above 0.997 in the basis of  $|\pm \rangle = (|H\rangle +|V\rangle) / \sqrt{2}$ .

We use  $30\mathrm{-nm}$  bandpass filters to remove the small sidebands and measure the joint spectral intensity distribution shown in Fig. 1(b), from which we extract a spectral purity of 0.99. Further, due to the group delay dispersion of the  $\mathrm{YVO_4}$  crystals  $(310~\mathrm{fs}^2 /\mathrm{mm})$  and the BBO crystals  $(79~\mathrm{fs}^2 /\mathrm{mm})$ , we employ four pairs of dispersion-compensating prisms to eliminate the dispersion. To test the photon indistinguishability, we perform a Hong-Ou-Mandel quantum interference [56] between two independent SPDC photons. As shown in Fig. 1(c), at zero delay, the fourfold coincidence count shows a dip with a raw visibility of  $0.962\pm 0.011$ , without using inefficient

![](images/01cdc3f7b6904d9f338a11818de3c95f3bace72e47e507ed87bbb2ac5b66f399.jpg)  
(a)

![](images/e207a3063858282cf20ad906bc9c2dad5ef21dfeecc7dc089b01b09c4323d36f.jpg)  
(b)

![](images/97be5bb6440b69153ef6ec14524aee4efd03d10a0a83924c9b1a9a00c13be68d.jpg)  
(c)  
FIG. 1. The design and performance of our new SPDC entangled-photon source. (a) The interferometric two-photon entanglement source. The laser beam is split into two beams by two  $775\mathrm{-nm}$  BDs and HWPs and focused on a BBO crystal at two different spot to generate photon pairs via type-II beamlike SPDC. The green (red) lines represent  $H(V)$  polarization. (b) The measured joint spectrum of the photon pair, indicating the two photons are free of frequency correlations. (c) Hong-OuMandel-type interference of two photons from two independent SPDC, measured without narrow-band filtering. (d) The measured heralding efficiency and photon-pair brightness as a function of the pump beam waist.

![](images/4e41441a4cf87e9c0f90baa4ff0b8fb34f89f62c897287083cd2bfa37cd6afc8.jpg)  
(d)

narrow-band spectral filtering. Its slight deviation from the predicted visibility of 0.99 from Fig. 1(b) could be caused by residual dispersion of the pump laser.

Another important requirement is the simultaneously high heralding efficiency and brightness. Generally, due to conservation of momentum in SPDC, a lower momentum uncertainty of pump beam can lead to a higher collection efficiency. However, a larger pump beam waist could result in a lower pump energy density. Thus, there is a trade-off between the collection efficiency and brightness. We measure the heralding efficiency and brightness of the new SPDC source as a function of pump beam waist. As shown in Fig. 1(d), at a pump beam waist of  $260\mu \mathrm{m}$  we obtain a two-photon count rate of  $7100\mathrm{Hz / mW}$  and a heralding efficiency of  $85\%$ . At a pump beam waist of  $1.9\mathrm{mm}$ , the brightness decreases to  $170\mathrm{Hz / mW}$ , whereas the heralding efficiency increases to  $94\%$ . Subtracting the channel loss in the optical path from the BBO to the single-mode fiber, we estimate a corrected heralding efficiency of  $97\%$  at  $1.9\mathrm{-mm}$  waist.

This high-performance entangled-photon source immediately makes it possible to perform the first 12-photon entanglement experiment. By successively passing the laser through six BBO crystals (see Fig. 2), we first prepare six

![](images/8784794ac5c71705045e4307e51f67d6be055fc1d72942b66dbca0ced85fd5ba.jpg)  
FIG. 2. Experimental setup for generating the 12-photon entanglement. Six SPDC entanglement sources [as shown in Fig. 1(a)] are pumped by laser pulses with a central wavelength of  $775~\mathrm{nm}$ , a bandwidth of  $5.5~\mathrm{nm}$ , and a repetition of  $80~\mathrm{MHz}$ . Dispersion of the laser pulses caused by  $\mathrm{YVO_4}$  crystals and BBO crystals is precompensated by four prism pairs. The 24 superconducting nanowire single-photon detectors have an average efficiency of  $75\%$  at  $1550~\mathrm{nm}$ .

pairs of entangled photons. One photon from each pair is combined with the other five photons on a linear optical array of five polarization beam splitters (PBSs) that transmit  $H$  and reflect  $V$  polarization. Under this arrangement, postselecting 12-photon coincidences implies that the output photons are either all  $H$  or  $V$  polarized. The two cases are quantum mechanically indistinguishable, thus projecting them into a 12-photon GHZ state in the form of  $(|H\rangle^{\otimes 12} + |V\rangle^{\otimes 12}) / \sqrt{2}$ .

To analyze the generated 12-photon state, we use a combination of wave plates and PBSs to measure the polarization of each individual photon and use 24 superconducting nanowire single-photon detectors to register the 12-channel coincidence counts. We use a suitable laser power of  $1.8\mathrm{W}$  and a focal waist of  $0.55\mathrm{mm}$ , where the photon-pair generation probability is  $\sim 0.05$ , the detected two-photon count rate is  $2.0\mathrm{MHz}$ , and the 12-photon coincidence is about one per hour (corresponding to a probability of  $3.5\times 10^{-12}$  per pulse). To validate the 12-photon entanglement, we first measure the 12-photon events in the  $H / V$  basis [see data in Fig. 3(a)] to calculate the population of  $(|H\rangle \langle H|)^{\otimes 12} + (|V\rangle \langle V|)^{\otimes 12}$  over all possible  $2^{12}$  combinations. From Fig. 3(a), we extract the population  $P = 0.732\pm 0.024$ . We further measure all the photons in the basis of  $(|H\rangle \pm e^{i\theta}|V\rangle) / \sqrt{2}$  to estimate the expectation value of the observable  $M_{\theta}^{\otimes N} = (\cos \theta \sigma_x + \sin \theta \sigma_y)^{\otimes N}$ , where  $\theta = k\pi /12$ ,  $k = 0,1,2,\ldots,11$ . The coherence of the GHZ state, determined by the two off-diagonal elements of its density matrix, can be calculated by  $C = (1 / 12)\sum_{k = 0}^{11}(-1)^{k}\langle M_{(k\pi /12)}^{\otimes 12}\rangle$ . From Fig. 3(b), we calculate  $C = 0.419\pm 0.041$ . We can then determine the state fidelity of the generated 12-photon GHZ state by  $(P + C) / 2 = 0.576\pm 0.024$ , which exceeds the threshold 0.5 more than 3 standard deviations and is sufficient to prove the presence of a genuine 12-qubit entanglement [57].

![](images/17ef0a2567b59d9b8bea015f5ca86240fd5adc4ce4c69596d0fd77b3ab1ad2b1.jpg)

![](images/ba340b90577f1ef6abb4e18398172b418fc324341d0faec19358f46b9271dee4.jpg)  
FIG. 3. Experimental result for the 12-photon GHZ state. (a) The measured 12-photon counts in the  $H / V$  basis. (b) Experimentally extracted expectation values of the observables  $M_{\theta}^{\otimes N} = (\cos \theta \sigma_x + \sin \theta \sigma_y)^{\otimes N}$ , which is calculated from registered 12-photon coincidence events in the  $(|H\rangle \pm e^{i\theta}|V\rangle) / \sqrt{2}$  basis. Error bars stand for one standard deviation based on binomial distribution statistics.

Multiplexing can, in principle, overcome the intrinsically probabilistic nature of the SPDC. For a scalable multiplexing with practical advantage, however, it is crucial that the SPDC pair, which serves as the fundamental building block for multiplexing, should possess simultaneously near-unity heralding efficiency and photon indistinguishability as we have demonstrated here. By combining our SPDC source with time- or spatial-multiplexing, assisted by fast and low-loss switches and suitable optical memories [37-39], it is possible to significantly enhance the overall efficiency.

For applications in boson sampling [55] considered as a promising candidate of quantum computational supremacy, there is a more convenient protocol to overcome the probabilistic problem of the SPDC. The standard boson

![](images/7ce677d88cd21a17653f36271769c0f5e61dbd5caa152763ca2de023d33311f0.jpg)

![](images/ad4cd39df4d372f19e1f0ba53ebaf9f4d57dd0befc9c3d67864f940a6fcdcb6c.jpg)  
FIG. 4. Experimental setup and results for high-efficiency scattershot boson sampling. (a) The signal photons from the same crystal are combined into one path by using the same method illustrated in Fig. 1(a) and guided into a 12-mode optical interferometer. Here we choose a pump beam waist of  $0.8\mathrm{mm}$  and a two-photon count rate of  $0.5\mathrm{MHz}$ . (b) The measured similarity and distance for the three-boson sampling. (c) Extended likelihood ratio test between the experimental data and simulated distinguishable sampler for the three-, four-, and five-photon experiments. (d) A comparison of the three-boson sampling rate with previous experiments using SPDC and quantum dots. The data points are labeled with their references.

![](images/e821839fe499cddbe7e23ac43ed3876ec756cffd4695add51d050032abee31b9.jpg)

![](images/df5f45f5725e827f6c3d5942c2344f6a72c6e76f279d61fb5334c048c0335507.jpg)

sampling is usually realized by sending  $n$  indistinguishable single photons through an  $m$  mode ( $m > n$ ) interferometer and registering the  $n$ -photon counts. Using  $n$  heralded single photons as input from  $n$  SPDC photon-pair sources, each with a generation probability of  $\varepsilon$  per pulse and a heralding efficiency of  $\eta$ , the eventual  $n$ -photon count rate would scale as  $(\varepsilon \eta)^n$ . The key idea of scattershot boson sampling [33] is to use  $k(k \gg n)$  heralded single-photon sources connecting to different input modes of the interferometer, which can achieve an exponential  $\binom{k}{n}$  times increase in the  $n$ -photon count rate to compete against the intrinsic probabilistic loss  $\sim \varepsilon^n$ . A proof-of-principle demonstration of scattershot boson sampling has been reported previously [58], however, using inefficient SPDC sources with low  $\eta$ , which limited the scalability to larger number of photons.

We exploit our SPDC source with simultaneously nearunity indistinguishability and heralding efficiency to demonstrate a blueprint of scalable scattershot boson sampling. As shown in Fig. 4(a), we use 12 SPDC sources to feed into a multimode interferometer encoded with both spatial and polarization degrees of freedom [27]. HwPs and quarter-wave plates (QwPs) are placed before and after the interferometer, respectively, with randomly set angles

[see Fig. S2(a)]. The evolution of the interferometer is modified by the wave plates. Such an arrangement produces a fully connected  $12 \times 12$  matrix, as shown in the measured random matrix in the Supplemental Material [Figs. S2(b) and S2(c) [48]]. For each SPDC source, the idler photons are detected to herald the presence of the signal photons, which are combined into one path by two BDs and fed into the interferometer. There are 220, 495, and 792 different no-collision input combinations for the three-, four-, and five-photon boson sampling, which implies that our scattershot boson sampling is expected to yield 220, 495, and 792 times enhancement of the efficiency over standard boson sampling, respectively.

We measure the three-, four-, and five-photon sampling rate of  $3.9\mathrm{kHz}$ $44\mathrm{Hz}$  ,and  $0.3\mathrm{Hz}$  , respectively. To qualify the sampling performance, we calculate the similarity, defined as  $S = \sum \sqrt{p_iq_i}$  , and the distance, defined as  $D = (1 / 2)\sum |p_i - q_i|$  , where  $p_i$  and  $q_{i}$  represent the experimental data and theoretical prediction, respectively. For the three-boson sampling, averaging over the  $220\times 220$  input-output combinations, we obtain a similarity of  $0.982\pm 0.004$  and a distance of  $0.122\pm 0.018$  . Such a characterization method is, however, not scalable to a larger number of photons. For example, for the four- and five-boson

sampling, the input-output combinations reach  $495 \times 495$  and  $792 \times 792$ , respectively, such that the counting events in each combination are extremely scarce. Therefore, a more efficient method is adopted to validate the boson sampling data. We apply a likelihood ratio test to rule out the distinguishable photon hypothesis (see Supplemental Material [48]). The results are shown in Fig. 4(c), with significant deviations between the experimental data (requiring only a few hundreds of samples) and the simulated distinguishable sampling.

The combination of our optimal SPDC source and the scattershot boson sampling yields a significantly enhanced multiphoton count rate. For example, the measured  $3.9\mathrm{-kHz}$  three-photon count rate is more than 4 orders of magnitude higher than the best previous boson sampling experiments based on SPDC [26-29,58] and comparable to the work using state-of-the-art quantum-dot single photons [see Fig. 4(d) for a summary of the count rate of the three-boson sampling experiments]. We expect to further increase the efficiency by using more SPDC crystals, higher-efficiency detectors, and combining the protocol of photon-loss-tolerant boson sampling [59].

In summary, we have developed an optimal SPDC entangled-photon source with simultaneously near-unity indistinguishability and heralding efficiency, which allowed us to demonstrate the first 12-photon genuine entanglement and perform high-efficiency scattershot boson sampling. Our work has established a near-optimal multiphoton platform and will enable previously challenging experiments, such as the generations of high-NOON states and remote heralded two- and multiphoton entangled states. Our SPDC source is also ready to be combined with multiplexing to overcome its probabilistic scaling, opening up a new pathway towards scalable photonic quantum technologies.

This work was supported by the National Natural Science Foundation of China (No. 91836303), the Chinese Academy of Sciences, the National Fundamental Research Program, and the Anhui Initiative in Quantum Information Technologies.

[1] P.G. Kwiat, K. Mattle, H. Weinfurter, A. Zeilinger, A.V. Sergienko, and Y. Shih, Phys. Rev. Lett. 75, 4337 (1995).  
[2] G. Weihs, T. Jennewein, C. Simon, H. Weinfurter, and A. Zeilinger, Phys. Rev. Lett. 81, 5039 (1998).  
[3] M. Giustina et al., Phys. Rev. Lett. 115, 250401 (2015).  
[4] L. K. Shalm et al., Phys. Rev. Lett. 115, 250402 (2015).  
[5] C.-Z. Peng, T. Yang, X. H. Bao, J. Zhang, X. M. Jin, F. Y. Feng, B. Yang, J. Yang, J. Yin, Q. Zhang, N. Li, B. L. Tian, and J. W. Pan, Phys. Rev. Lett. 94, 150501 (2005).  
[6] R. Ursin et al., Nat. Phys. 3, 481 (2007).  
[7] S.-K. Liao et al., Nature (London) 549, 43 (2017).  
[8] K. Mattle, H. Weinfurter, P.G. Kwiat, and A. Zeilinger, Phys. Rev. Lett. 76, 4656 (1996).  
[9] J.-W. Pan, Z.-B. Chen, C.-Y. Lu, H. Weinfurter, A. Zeilinger, and M. Zukowski, Rev. Mod. Phys. 84, 777 (2012).

[10] D. Bouwmeester, J.-W. Pan, M. Daniell, H. Weinfurter, and A. Zeilinger, Phys. Rev. Lett. 82, 1345 (1999).  
[11] J.-W. Pan, M. Daniell, S. Gasparoni, G. Weihs, and A. Zeilinger, Phys. Rev. Lett. 86, 4435 (2001).  
[12] Z. Zhao, Y.-A. Chen, A.-N. Zhang, T. Yang, H. J. Briegel, and J.-W. Pan, Nature (London) 430, 54 (2004).  
[13] C.-Y. Lu, X.-Q. Zhou, O. Ghne, W.-B. Gao, J. Zhang, Z.-S. Yuan, A. Goebel, T. Yang, and J.-W. Pan, Nat. Phys. 3, 91 (2007).  
[14] X.-C. Yao, T.-X. Wang, P. Xu, H. Lu, G.-S. Pan, X.-H. Bao, C.-Z. Peng, C.-Y. Lu, Y.-A. Chen, and J.-W. Pan, Nat. Photonics 6, 225 (2012).  
[15] X.-L. Wang, L.-K. Chen, W. Li, H.-L. Huang, C. Liu, C. Chen, Y.-H. Luo, Z.-E. Su, D. Wu, Z.-D. Li, H. Lu, Y. Hu, X. Jiang, C.-Z. Peng, L. Li, N.-L. Liu, Y.-A. Chen, C.-Y. Lu, and J.-W. Pan, Phys. Rev. Lett. 117, 210502 (2016).  
[16] L.-K. Chen et al., Optica 4, 77 (2017).  
[17] X.-L. Wang, Y.-H. Luo, H.-L. Huang, M.-C. Chen, Z.-E. Su, C. Liu, C. Chen, W. Li, Y.-Q. Fang, X. Jiang, J. Zhang, L. Li, N.-L. Liu, C.-Y. Lu, and J.-W. Pan, Phys. Rev. Lett. 120, 260502 (2018).  
[18] J.-W. Pan, D. Bouwmeester, M. Daniell, H. Weinfurter, and A. Zeilinger, Nature (London) 403, 515 (2000).  
[19] D. Bouwmeester, J.-W. Pan, K. Mattle, M. Eibl, H. Weinfurter, and A. Zeilinger, Nature (London) 390, 575 (1997).  
[20] X.-L. Wang, X.-D. Cai, Z.-E. Su, M.-C. Chen, D. Wu, L. Li, N.-L. Liu, C.-Y. Lu, and J.-W. Pan, Nature (London) 518, 516 (2015).  
[21] J.-G. Ren et al., Nature (London) 549, 70 (2017).  
[22] A. N. Boto, P. Kok, D. S. Abrams, S. L. Braunstein, C. P. Williams, and J. P. Dowling, Phys. Rev. Lett. 85, 2733 (2000).  
[23] P. Walther, J.-W. Pan, M. Aspelmeyer, R. Ursin, S. Gasparoni, and A. Zeilinger, Nature (London) 429, 158 (2004).  
[24] I. Afek, O. Ambar, and Y. Silberberg, Science 328, 879 (2010).  
[25] C. Y. Lu, W. B. Gao, O. Guhne, X. Q. Zhou, Z. B. Chen, and J. W. Pan, Phys. Rev. Lett. 102, 030502 (2009).  
[26] J. B. Spring et al., Science 339, 798 (2013).  
[27] M. A. Broome, A. Fedrizzi, S. Rahimi-Keshari, J. Dove, S. Aaronson, T. C. Ralph, and A. G. White, Science 339, 794 (2013).  
[28] M. Tillmann, B. Daki, R. Heilmann, S. Nolte, A. Szameit, and P. Walther, Nat. Photonics 7, 540 (2013).  
[29] A. Crespi, R. Osellame, R. Ramponi, D.J. Brod, E.F. Galvo, N. Spagnolo, C. Vitelli, E. Maiorino, P. Mataloni, and F. Sciarrino, Nat. Photonics 7, 545 (2013).  
[30] H. Wang et al., Nat. Photonics 11, 361 (2017).  
[31] J.C. Loredo, M.A. Broome, P. Hilaire, O. Gazzano, I. Sagnes, A. Lemaitre, M.P. Almeida, P. Senellart, and A.G. White, Phys. Rev. Lett. 118, 130503 (2017).  
[32] Yu He, X. Ding, Z.-E. Su, H.-L. Huang, J. Qin, C. Wang, S. Unsleber, C. Chen, H. Wang, Y.-M. He, X.-L. Wang, W.-J. Zhang, S.-J. Chen, C. Schneider, M. Kamp, L.-X. You, Z. Wang, S. Hofling, C.-Y. Lu, and J.-W. Pan, Phys. Rev. Lett. 118, 190501 (2017).  
[33] A. P. Lund, A. Laing, S. Rahimi-Keshari, T. Rudolph, J. L. OBrien, and T. C. Ralph, Phys. Rev. Lett. 113, 100502 (2014).

[34] A. Acin, N. Brunner, N. Gisin, S. Massar, S. Pironio, and V. Scarani, Phys. Rev. Lett. 98, 230501 (2007).  
[35] BIG Bell Test Collaboration, Nature (London) 557, 212 (2018).  
[36] Y. Cao, Y.-H. Li, W.-J. Zou, Z.-P. Li, Q. Shen, S.-K. Liao, J.-G. Ren, J. Yin, Y.-A. Chen, C.-Z. Peng, and J.-W. Pan, Phys. Rev. Lett. 120, 140405 (2018).  
[37] T. B. Pittman, B. C. Jacobs, and J. D. Franson, Phys. Rev. A 66, 042303 (2002).  
[38] A. L. Migdall, D. Branning, and S. Castelletto, Phys. Rev. A 66, 053805 (2002).  
[39] F. Kaneda and P.G. Kwiat, arXiv:1803.04803.  
[40] Y.-H. Kim and W.P. Grice, J. Mod. Opt. 49, 2309 (2002).  
[41] Y.-H. Kim, S. P. Kulik, M. V. Chekhova, W. P. Grice, and Y. Shih, Phys. Rev. A 67, 010301 (2003).  
[42] S. Takeuchi, Opt. Lett. 26, 843 (2001).  
[43] O. Kwon, Y.-W. Cho, and Y.-H. Kim, Phys. Rev. A 78, 053825 (2008).  
[44] P. J. Mosley, J. S. Lundeen, B. J. Smith, P. Wasylczyk, A. B. URen, C. Silberhorn, and I. A. Walmsley, Phys. Rev. Lett. 100, 133601 (2008).  
[45] F. Kaneda, K. Garay-Palmett, A. B. URen, and P. G. Kwiat, Opt. Express 24, 10733 (2016).  
[46] C. Chen, C. Bo, M. Y. Niu, F. Xu, Z. Zhang, J. H. Shapiro, and F. N. C. Wong, Opt. Express 25, 7300 (2017).  
[47] W. P. Grice, A. B. URen, and I. A. Walmsley, Phys. Rev. A 64, 063815 (2001).  
[48] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.121.250505 for a

comparison of SPDC entangled photon pair sources, joint spectrum without filters, and more details about the optical interferometer and validation, which includes Refs. [3,4,13-16,45-47,49-55].  
[49] B.G. Christensen, K.T. McCusker, J.B. Altepeter, B. Calkins, T. Gerrits, A.E. Lita, A. Miller, L.K. Shalm, Y. Zhang, S.W. Nam, N. Brunner, C.C.W. Lim, N. Gisin, and P.G. Kwiat, Phys. Rev. Lett. 111, 130406 (2013).  
[50] C. Zhang, Y.-F. Huang, Z. Wang, B.-H. Liu, C.-F. Li, and G.-C. Guo, Phys. Rev. Lett. 115, 260402 (2015).  
[51] M. M. Weston et al., Opt. Express 24, 10869 (2016).  
[52] G. Harder, V. Ansari, B. Brecht, T. Dirmeier, C. Marquardt, and C. Silberhorn, Opt. Express 21, 13975 (2013).  
[53] P. B. Dixon, D. Rosenberg, V. Stelmakh, M. E. Grein, R. S. Bennink, E. A. Dauler, A. J. Kerman, R. J. Molnar, and F. N. C. Wong, Phys. Rev. A 90, 043804 (2014).  
[54] N. Bruno, A. Martin, T. Guerreiro, B. Sanguinetti, and R. T. Thew, Opt. Express 22, 17246 (2014).  
[55] S. Aaronson and A. Arkhipov, Theory Comput. 9, 143 (2013).  
[56] C. K. Hong, Z. Y. Ou, and L. Mandel, Phys. Rev. Lett. 59, 2044 (1987).  
[57] O. Ghne and G. Tth, Phys. Rep. 474, 1 (2009).  
[58] M. Bentivegna et al., Sci. Adv. 1, e1400255 (2015).  
[59] H. Wang, W. Li, X. Jiang, Y.-M. He, Y.-H. Li, X. Ding, M.-C. Chen, J. Qin, C.-Z. Peng, C. Schneider, M. Kamp, W.-J. Zhang, H. Li, L.-X. You, Z. Wang, J. P. Dowling, S. Hofling, C.-Y. Lu, and J.-W. Pan, Phys. Rev. Lett. 120, 230502 (2018).