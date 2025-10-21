# Toward Scalable Boson Sampling with Photon Loss

Hui Wang, $^{1,2,3}$  Wei Li, $^{1,2,3}$  Xiao Jiang, $^{1,2,3}$  Y.-M. He, $^{1,2,3}$  Y.-H. Li, $^{1,2,3}$  X. Ding, $^{1,2,3}$  M.-C. Chen, $^{1,2,3}$  J. Qin, $^{1,2,3}$

C.-Z. Peng, $^{1,2,3}$  C. Schneider, $^{4}$  M. Kamp, $^{4}$  W.-J. Zhang, $^{5}$  H. Li, $^{5}$  L.-X. You, $^{5}$  Z. Wang, $^{5}$  J. P. Dowling, $^{6,7}$

S. Hofling, $^{1,4,8}$  Chao-Yang Lu, $^{1,2,3,*}$  and Jian-Wei Pan $^{1,2,3,\dagger}$

$^{1}$ Shanghai Branch, National Laboratory for Physical Sciences at Microscale, University of Science and Technology of China,

Shanghai 201315, China

$^{2}$ CAS Center for Excellence and Synergetic Innovation Center in Quantum Information and Quantum Physics,

University of Science and Technology of China, Hefei, Anhui 230026, China

$^{3}$ CAS-Alibaba Quantum Computing Laboratory, Shanghai 201315, China

$^{4}$ Technische Physik, Physikalisches Institut und Wilhelm Conrad Rontgen-Center for Complex Material Systems, Universitat Würzburg, Am Hubland, D-97074 Wüzburg, Germany

${}^{5}$  State Key Laboratory of Functional Materials for Informatics,Shanghai Institute of Microsystem and

Information Technology (SIMIT), Chinese Academy of Sciences, 865 Changning Road, Shanghai 200050, China

$^{6}$ Hearne Institute for Theoretical Physics and Department of Physics and Astronomy, Louisiana State University,

Baton Rouge, Louisiana 70803, USA

$^{7}$ NYU-ECNU Institute of Physics at NYU Shanghai, Shanghai 200062, China

$^{8}$ SUPA, School of Physics and Astronomy, University of St Andrews, St Andrews KY16 9SS, United Kingdom

![](images/ee698815a563ead61484a79615517cafe40057cebde8e2e6db23e4d524782ac0.jpg)

(Received 16 January 2018; published 6 June 2018)

Boson sampling is a well-defined task that is strongly believed to be intractable for classical computers, but can be efficiently solved by a specific quantum simulator. However, an outstanding problem for large-scale experimental boson sampling is the scalability. Here we report an experiment on boson sampling with photon loss, and demonstrate that boson sampling with a few photons lost can increase the sampling rate. Our experiment uses a quantum-dot-micropillar single-photon source demultiplexed into up to seven input ports of a  $16 \times 16$  mode ultralow-loss photonic circuit, and we detect three-, four- and fivefold coincidence counts. We implement and validate lossy boson sampling with one and two photons lost, and obtain sampling rates of 187, 13.6, and  $0.78\mathrm{kHz}$  for five-, six-, and seven-photon boson sampling with two photons lost, which is 9.4, 13.9, and 18.0 times faster than the standard boson sampling, respectively. Our experiment shows an approach to significantly enhance the sampling rate of multiphoton boson sampling.

DOI: 10.1103/PhysRevLett.120.230502

Boson sampling [1] is considered as a strong candidate to demonstrate quantum computational supremacy [2,3]. It only requires indistinguishable single-photon sources, a passive linear network, and single-photon detection. However, it is strongly believed to be intractable for classical computers under some computational complexity assumptions. Its relatively simple design attracts a number of proof-of-principle experiments [4-7], using probabilistic heralded single photons produced by spontaneous parametric downconversion (SPDC) [8]. Recently, high-performance single-photon sources based on quantum-dot micropillars were developed [9-12] and applied to multiphoton boson sampling, which significantly increased the photon number and sampling rate [13-15].

In the photonic experiments the major obstacle to scaling up is the unavoidable photon loss, which can happen in the source, interferometer, and detectors. Recently, Aaronson and Brod have investigated boson sampling with photons lost [16]. In standard boson sampling, we send  $n$  single photons into an  $m$ -port ( $n \ll m$ ) passive linear network,

and then sample from the output distribution. Although serious losses in the single-photon source, linear networks, and detectors, we can postselect  $n$ -fold coincidence counts and compare to the theoretical distribution given by calculating permanents of submatrices. However, in the new variation of the scheme of boson sampling—lossy boson sampling, the only difference is that we postselect  $(n - k)$ -fold coincidence counts, where the  $k$  is the number of lost photons.

Aaronson and Brod have shown that, if  $k$  is constant, lossy boson sampling cannot be simulated in classical polynomial time, just under exactly the same complexity assumptions used for standard boson sampling [16]. This theoretical work indicates that boson sampling is a very robust model under experimental imperfections. Importantly, in the lossy scenario, the sampling rate can exponentially grow with  $k$ , which can make boson sampling more feasible in order to demonstrate quantum supremacy. Here, we experimentally investigate the first lossy boson sampling using a quantum-dot single-photon source with an extraction

(system) efficiency of  $82.2\%$ $(33.7\%)$  [13], a  $16\times 16$  mode ultralow-loss  $(< 1\%)$  photonic network [17,18], and inefficient single-photon detectors with an average efficiency of  $53\%$ . Reference [16] only considered random path-independent loss that happens at the single-photon source. Here we give a result on a more realistic model that losses happen anywhere except the interferometer [19].

As shown in Fig. 1, a single self-assembled InAs/GaAs QD was embedded inside a micropillar cavity with a diameter of  $2\mu \mathrm{m}$ . Under  $\pi$  pulse excitation [23] with a repetition rate of  $76\mathrm{MHz}$ , the QD-micropillar emits  $25.6\mathrm{MHz}$  polarized single photons at the end of the single-mode fiber, which are directly used for boson sampling without any spectral filtering [13]. The measured second-order correlation function  $g^{2}(0)$  and photon indistinguishability are 0.027(1) and 0.939(3), respectively. The high quality of single photons benefits from a large Purcell enhancement (a factor of 7.6) of the microcavity which enhances the radiative rate [10]. The cavity  $Q$  factor is  $\sim 6400$  which is helpful to suppress the phonon sidebands [24].

We actively demultiplexed the single-photon pulse stream into seven different spatial modes (see Fig. 1 and Ref. [19]). The demultiplexers consist of six cascaded Pockels cells and polarizing beam splitters (PBSs). Driven by half-wave voltage  $(\sim 1800\mathrm{V})$ , a Pockels cell (with its axis aligned at  $\pi /4$ ) can rotate the polarization by  $90^{\circ}$ , and a

PBS is used to separate the single-photon stream. With the demultiplexers operated at a repetition rate of  $0.775\mathrm{MHz}$ , every 98 pulses are separated into seven segments equally. That is, 14 sequential pulses will go out from each of seven different spatial modes [19]. Then we use seven single-mode fibers with different lengths to ensure that each segment of the pulse trains arrive at the interferometer simultaneously. Translation stages were used to finely adjust the arrival time with a precision of 0.03 ps. Owing to the high transmission rate ( $>99\%$ ) of the Pockels cells, an extinction ratio of 100:1, and the high single-mode fiber coupling efficiency ( $92\%$ ), the average efficiency of the demultiplexers is  $\sim 85\%$ .

The single photons are fed into a  $16 \times 16$  mode square-shaped photonic network [18], which has the feature of high stability, ultralow loss, and matrix randomness (see Fig. 1 and Ref. [19]). Comparing to the triangle-shaped design by Reck et al. [17], this square-shaped design achieves minimal optical depth, which requires less beam splitters and phase shifters, and has less optical losses. On the other hand, this symmetry design is more robust to the optical losses [18]. It has a size of  $50.91 \mathrm{~mm} \times 45.25 \mathrm{~mm} \times 4.00 \mathrm{~mm}$  which was fabricated by bonding 16 tiny trapezoids together. Every surface between a pair of trapezoids is optically coated with polarization-dependent beam-splitting thin films, while the top and bottom surfaces were total-reflecting coated. This network equivalently

![](images/8e62d71986edeb327df4bcffe55ad16de83613b27d5fdcb1147a4ea5fce6c692.jpg)  
FIG. 1. (a) Experimental setup for lossy boson sampling. The setup contains four parts. The first part is a single-photon source from a quantum-dot micropillar. It is placed inside a  $4.2\mathrm{K}$  cryostat, and a confocal microscopy is used to excite the quantum dot and collect its resonance fluorescence. The second part is six cascaded demultiplexers that separate the single photon stream into seven different spatial modes. Seven single-mode fibers with different lengths are used to compensate the time delay among seven different modes. The third part is the ultralow-loss photonic network; the demultiplexed single photons are injected into a  $16\times 16$  mode square-shaped photonic network, which contains 113 beam splitters and 14 mirrors. The last part is the detection; 13 superconducting nanowire single-photon detectors and 3 silicon-based avalanche detectors are used to detect photons, and a homemade coincidence-count unit registers all nocollision events (not shown). (b) The equivalent photonic circuit of our  $16\times 16$  mode interferometer, which is fully connected and has a transmission rate above  $99\%$ . (c) Enlarged ultralow-loss photonic network with a size of  $50.91\mathrm{mm}\times 45.25\mathrm{mm}\times 4.00\mathrm{mm}$ .

contains 113 beam splitters and 14 mirrors, which act as a unitary transformation to the input Fock states. Note that our photonic circuit has a negligible loss (transmission rate  $>99\%$ ). In this case, it is reasonable to consider it as a unitary matrix, which avoids the complex computation caused by path-dependent loss in the photonic network. Recently, we noticed that two works [25,26] already talked about the path-dependent loss in the photonic circuit.

Thirteen superconducting nanowire single-photon detectors and three silicon-based avalanche detectors are used to detect the photons, and a 64-channel homemade coincidence counting unit is applied to register all no-collision events. We classify losses in the photonic paths into two groups: loss at the source—all losses before the photonic network, and loss at the detectors—all losses after the photonic network. Imagine that we have  $n + k$  input ports in front of photonic circuit, but we only detect  $n$ -fold coincidence counts. So,  $k$  photons may randomly be lost at the source, or at the detectors, or both can happen. Random loss at the single-photon source has been

discussed in Ref. [16], and the output probability is given by  $\Phi(A) = (1 / |S|)\sum_{S}|\mathrm{Perm}(A_S)|^2$ , where  $A$  is an  $n \times n$  submatrix,  $S$  are all the input combinations, and  $|S|$  equals  $\binom{n+k}{n}$ . It is intuitive that, in this case, the output distribution is exactly the average of all possibilities that come from different input combinations. In this work, we give a clear formulation of the output probability when photons are lost at the detectors or both at single-photon sources and detectors [19]. We give theoretical and numerical evidence that, path-independent loss, wherever it happens, is equivalent to a uniform loss at the single-photon source. Note that path-independent losses include all coupling loss through the optical path and the inhomogeneous loss at the detectors. So, for the following experiments, we just calculate  $\Phi(A)$  and then modified it with the efficiency of the corresponding input ports and output ports, as in the theoretical distribution.

We first studied boson sampling with one photon lost. We sent four, five, and six photons into the sixteen-mode photonic network, but only extracted three-, four- and

![](images/90d19758855f213df8462712329cfcae7aa00aac0b509213e055ca07b9aec20f.jpg)

![](images/b37477c55c38e2b78798513e3055ad60debe146780889f15b2812b8a37884338.jpg)

![](images/95fed58ce22df5cb1a4a41379694cbedc88f962662d37f64d133bf09f500dab1.jpg)  
FIG. 2. Experimental results for four-, five-, and six-photon boson sampling with one photon lost. The upper part of each graph are the experimental results, and the bottom part are the theoretical results, given by calculating permanents. All no-collision output combinations are denoted by  $\{i,j,\ldots\}$  where  $i,j$  is the  $i$ th,  $j$ th, ... output port. There are 560, 1820, and 4368 output combinations for the four- (a), five- (b), and six-photon (c) boson sampling with one photon lost; the measured distances are 0.085(1), 0.106(2), and 0.201(3), and measured similarities are 0.994(1), 0.989(2), and 0.960(4), respectively.

fivefold coincidence counts at the output ports of the interferometer. There are 560, 1820, and 4368 no-collision output combinations for four-, five-, and six-boson sampling with one photon lost. The observed probability corresponding to each output combination is shown in the upper part of Fig. 2, while the bottom part is the theoretical probability given by calculating the corresponding submatrix.

A total of 402 586 three-photon events, 198 920 four-photon events, and 33 587 five-photon events were obtained in an accumulation time of 5, 50, and  $150\mathrm{s}$ , respectively. To quantify the match between experimental distribution  $(q_{i})$  and theoretical distribution  $(p_i)$ , we calculated the total variation distance, defined as  $D = (1 / 2)\sum_{i}|q_{i} - p_{i}|$ , and the similarity, defined as  $F = \sum_{i}\sqrt{q_{i}p_{i}}$ . The obtained  $D$  is 0.085(1), 0.106(2), 0.201(3), and the  $F$  is 0.994(1), 0.989(2), 0.960(4) for four-, five-, and six-photon boson sampling with one photon lost, respectively. These two measures provide a first confirmation of the correct operation of the quantum devices.

Next, we study the boson sampling with two photons lost. In our study, we sent five, six, and seven photons into the interferometer, and at the output, we registered three-, four-, and five-photon events (the detailed data of the distribution can be seen in Ref. [19]). We found the measures of distance are 0.071(1), 0.097(2), and 0.178(3), and measures of similarity are 0.996(1), 0.992(2), and 0.967(4) for the five-, six-, and seven-photon boson sampling with two photons lost, respectively.

To give further supporting evidence that our experimental results are from genuine boson sampling, we applied several statistical tests to rule out possible alternative hypotheses. We first excluded the hypothesis that distinguishable single photons or spatial-mode mismatched interferometers were used, by performing a new version of a standard likelihood ratio test [27,28]. The correctness of this method was shown by the

simulated results [19]. Figure 3(a) shows an increasing difference between experimental data and simulated data by distinguishable bosons. The Aaronson and Arkhipov test, or row-norm estimator (RNE), is designed to distinguish boson sampling from a uniform distribution [28,29]. Here, we extend it to the lossy boson sampling [19], and Fig. 3(b) clearly shows the difference between boson sampler and uniform sampler.

Like scattershot boson sampling [30,31], lossy boson sampling is expected to show a speed-up over standard boson sampling. In our experiments, the rate of three-photon boson sampling is  $19.9\mathrm{kHz}$ , which is over  $10^{5}$  times faster than all previous boson sampling experiments based on the SPDC sources. When we increase the number of lost photons from one to four, the rates change to 87.8, 187.9, 357.7, 673.0 kHz, which are 4.4, 9.4, 17.9, 33.8 times faster than standard boson sampling, respectively. In Fig. 4(a), we present the sampling rates of all conditions up to six-photon boson sampling, and the data are in excellent agreement with theoretical prediction. Next, we will discuss 50-photon boson sampling with photon loss. The assumed realistic parameters of efficiency are 0.8 for single-photon sources, 0.9 for a interferometer by our integrated bulk optics approach (including the efficiency of coupling the photons into single-mode fibers), and 0.9 for single-photon detectors. In this condition, the rate for standard 50-photon boson sampling is  $10^{-6}\mathrm{Hz}$ . However, if we have 52 input ports, and allow two photon loss, the rate becomes  $\sim 0.005\mathrm{Hz}$ , which is already feasible to do such an experiment. In Fig. 4(b), we present sampling rate of lossy boson sampling with up to five photons lost, which is likely to be a scalable approach to demonstrate quantum supremacy.

Last but not the least, we discuss the open theoretical questions in lossy boson sampling. As discussed in Ref. [16], if  $k$  is fixed, lossy boson sampling remains in

![](images/7187c41e4755d11c1732d4e46fb67f0673f49cbaed8d5810f5a02b3553034d85.jpg)  
FIG. 3. Validation of lossy boson sampling. (a) Extended likelihood ratio test to discriminate experimental data from a distinguishable sampler. (b) Application of extended RNE test to exclude the uniform distribution. The solid lines in (a) and (b) are tests applied on experimental data, and the dotted lines in (a) and (b) are tests applied on simulated data generated from a distinguishable sampler and a uniform sampler, respectively. The increasing difference between them indicates that experimental data are highly likely from a genuine boson sampler.

![](images/dc9fd2e0b3d1a78c03ec464b7a1cf87aff2e33b0de9c1f86e65b658fd56fe945.jpg)

![](images/29099352835f115289098b6c29e22fc97e45c31b5ad29d49918ab928981274b3.jpg)  
FIG. 4. (a) The count rate comparison between experimental data and theoretical predictions. The excellent matches show that lossy boson sampling will have an exponential speed-up over the standard scenario by a factor of  $\binom{n+k}{n}$ . (b) The sampling rate of a 50-photon boson sampling when the number of lost photons increase from zero to five. Note that the assumed parameters of efficiency are 0.8 for single-photon sources, 0.9 for interferometer, and 0.9 for single-photon detectors, respectively. Allowing two photons lost will make this experiment feasible, while it is not realistic to perform a standard boson sampling experiment with the same efficiency parameters. (c) Ascending ordered distributions of three-photon standard boson sampling (red), five-photon boson sampling with two photons lost (black), and seven-photon boson sampling with four photons lost (blue). If more photons are lost, the distribution will be closer to uniform distribution (pink).

![](images/1fa2473b44300eae2048919dcbb8de0d6564f6f009172b3948deffc24292135b.jpg)

![](images/61697daa4169de8a7c0b4ac30c23ae9feff646f8b5e4ba29528b0b100565cc05.jpg)

the same complexity class as standard boson sampling in the limit  $n \to \infty$ . However, it is still an open question what complexity it retains in a realistic loss regime, say,  $k = \sqrt{n}$  or  $k = \ln(n)$ . What will happen when the number of lost photons  $k$  increases? Intuitively, it will make the problem easier since the dimension of the submatrices become smaller. On the other hand, since the sum is taken over  $\binom{n+k}{n}$  input combinations, the distribution will be much flatter than standard boson sampling, so there may exist some approximate algorithms to simulate this distribution. As an example, we sent up to seven photons into interferometer and only detected threefold coincidence counts. Figure 4(c) is the reordered distribution (ascending order) of three-photon boson sampling with three (red), five (black), and seven (blue) input ports, respectively. It shows that, when the number of lost photons increases, the distribution will be closer to the uniform distribution (pink). Where is the threshold value of  $k$  so that lossy boson sampling is intractable for classical computers is an important open question, since  $k$  is the key for the least demanding efficiency. Our experiment shows a possible way to increase the multiphoton boson sampling efficiency which could be helpful to achieve quantum supremacy with single photons and linear optics. We hope that our experiment will inspire more work on lossy boson sampling.

We thank S. Aaronson, B. Sanders, and J.-Z. Wu for helpful discussions. This work was supported by the National Natural Science Foundation of China, the Chinese Academy of Science, the Science and Technology Commission of Shanghai Municipality, the National Fundamental Research Program, the State of Bavaria, and the U.S. National Science Foundation.

$^{*}$ cylu@ustc.edu.cn  
† pan@ustc.edu.cn

[1] S. Aaronson and A. Arkhipov, Proceedings of the ACM Symposium on Theory of Computing (ACM, New York, 2011), p. 333.  
[2] J. Preskill, arXiv:1203.5813.  
[3] A. W. Harrow and A. Montanaro, Nature (London) 549, 203 (2017).  
[4] M. A. Broome, A. Fedrizzi, S. Rahimi-Keshari, J. Dove, S. Aaronson, T. C. Ralph, and A. G. White, Science 339, 794 (2013).  
[5] J. B. Spring et al., Science 339, 798 (2013).  
[6] M. Tillmann, B. Dakic, R. Heilmann, S. Nolte, A. Szameit, and P. Walther, Nat. Photonics 7, 540 (2013).  
[7] A. Crespi, R. Osellame, R. Ramponi, D.J. Brod, E.F. Galvão, N. Spagnolo, C. Vitelli, E. Maiorino, P. Mataloni, and F. Sciarrino, Nat. Photonics 7, 545 (2013).  
[8] P.G. Kwiat, K. Mattle, H. Weinfurter, A. Zeilinger, A.V. Sergienko, and Y. Shih, Phys. Rev. Lett. 75, 4337 (1995).  
[9] X. Ding, Phys. Rev. Lett. 116, 020401 (2016).  
[10] H. Wang et al., Phys. Rev. Lett. 116, 213601 (2016).  
[11] N. Somaschi et al., Nat. Photonics 10, 340 (2016).  
[12] S. Unsleber, Y.-M. He, S. Gerhardt, S. Maier, C.-Y. Lu, J.-W. Pan, N. Gregersen, M. Kamp, C. Schneider, and S. Höfling, Opt. Express 24, 8539 (2016).  
[13] H. Wang et al., Nat. Photonics 11, 361 (2017).  
[14] Y. He et al., Phys. Rev. Lett. 118, 190501 (2017).  
[15] J.C. Lrecordo, M.A. Broome, P. Hilaire, O. Gazzano, I. Sagnes, A. Lemaitre, M.P. Almeida, P. Senellart, and A.G. White, Phys. Rev. Lett. 118, 130503 (2017).  
[16] S. Aaronson and D.J. Brod, Phys. Rev. A 93, 012335 (2016).  
[17] M. Reck, A. Zeilinger, H. J. Bernstein, and P. Bertani, Phys. Rev. Lett. 73, 58 (1994).  
[18] W. R. Clements, P. C. Humphreys, B. J. Metcalf, W. S. Kolthammer, and I. A. Walmsley, Optica 3, 1460 (2016).

[19] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.120.230502 for more information on the single-photon sources, demultiplexers, fabrication, and characterization of the photonic networks, analysis of the lossy boson sampling, validation and experimental results of boson sampling with two photons lost, which includes the Refs. [13,16,18,20-22].  
[20] S. Rahimi-Keshari, M. A. Broome, R. Fichler, A. Fedrizzi, T. C. Ralph, and A. G. White, Opt. Express 21, 13450 (2013).  
[21] R. Júlia, Asymptotics of random unitaries, PhD thesis, 2005, https://pdfssemanticscholar.org/30d2/025f17d0369fcde39a1034bd41c8fa448890.pdf.  
[22] M. Ozols, How to generate a random unitary matrix, 2009, http://home.lu.lv/~sd20008/papers/essays/Random%20unitary%20[paper].pdf.

[23] Y.-M. He, Y. He, Y.-J. Wei, D. Wu, M. Atatüre, C. Schneider, S. Hofling, M. Kamp, C.-Y. Lu, and J.-W. Pan, Nat. Nanotechnol. 8, 213 (2013).  
[24] J. Iles-Smith, D. S. McCutcheon, A. Nazir, and J. Mork, Nat. Photonics 11, 521 (2017).  
[25] R. García-Patrón, J.J. Renema, and V. Shchesnovich, arXiv:1712.10037.  
[26] M. Oszmaniec and D. J. Brod, arXiv:1801.06166.  
[27] T.M. Cover and J.A. Thomas, Elements of Information Theory, 2nd ed. (Wiley-Interscience, Hoboken, NJ, 2006).  
[28] N. Spagnolo et al., Nat. Photonics 8, 615 (2014).  
[29] S. Aaronson and A. Arkhipov, Quantum Inf. Comput. 14, 1383 (2014).  
[30] A. P. Lund, A. Laing, S. Rahimi-Keshari, T. Rudolph, J. L. OBrien, and T. C. Ralph, Phys. Rev. Lett. 113, 100502 (2014).  
[31] M. Bentivegna et al., Sci. Adv. 1, e1400255 (2015).