# Quantum computational advantage using photons

Han-Sen Zhong $^{1,2*}$ , Hui Wang $^{1,2*}$ , Yu-Hao Deng $^{1,2*}$ , Ming-Cheng Chen $^{1,2*}$ , Li-Chao Peng $^{1,2}$ , Yi-Han Luo $^{1,2}$ , Jian Qin $^{1,2}$ , Dian Wu $^{1,2}$ , Xing Ding $^{1,2}$ , Yi Hu $^{1,2}$ , Peng Hu $^{3}$ , Xiao-Yan Yang $^{3}$ , Wei-Jun Zhang $^{3}$ , Hao Li $^{3}$ , Yuxuan Li $^{4}$ , Xiao Jiang $^{1,2}$ , Lin Gan $^{4}$ , Guangwen Yang $^{4}$ , Lixing You $^{3}$ , Zhen Wang $^{3}$ , Li Li $^{1,2}$ , Nai-Le Liu $^{1,2}$ , Chao-Yang Lu $^{1,2}$ , Jian-Wei Pan $^{1,2+}$

<sup>1</sup>Hefei National Laboratory for Physical Sciences at Microscale and Department of Modern Physics, University of Science and Technology of China, Hefei, Anhui 230026, China. <sup>2</sup>CAS Centre for Excellence and Synergetic Innovation Centre in Quantum Information and Quantum Physics, University of Science and Technology of China, Shanghai 201315, China. <sup>3</sup>State Key Laboratory of Functional Materials for Informatics, Shanghai Institute of Microsystem and Information Technology, Chinese Academy of Sciences, Shanghai 200050, China. <sup>4</sup>Department of Computer Science and Technology and Beijing National Research Center for Information Science and Technology, Tsinghua University, Beijing 100084, China.

*These authors contributed equally to this work.

†Corresponding author. Email: pan@ustc.edu.cn

Quantum computers promises to perform certain tasks that are believed to be intractable to classical computers. Boson sampling is such a task and is considered as a strong candidate to demonstrate the quantum computational advantage. We perform Gaussian boson sampling by sending 50 indistinguishable single-mode squeezed states into a 100-mode ultralow-loss interferometer with full connectivity and random matrix—the whole optical setup is phase-locked—and sampling the output using 100 high-efficiency single-photon detectors. The obtained samples are validated against plausible hypotheses exploiting thermal states, distinguishable photons, and uniform distribution. The photonic quantum computer generates up to 76 output photon clicks, which yields an output state-space dimension of  $10^{30}$  and a sampling rate that is  $\sim 10^{14}$  faster than using the state-of-the-art simulation strategy and supercomputers.

The Extended Church-Turing Thesis is a foundational tenet in computer science, which states that a probabilistic Turing machine can efficiently simulate any process on a realistic physical device (1). In the 1980s, Richard Feynman observed that many-body quantum problems seemed difficult for classical computers due to the exponentially growing size of the quantum state Hilbert space. He proposed that a quantum computer would be a natural solution.

A number of quantum algorithms have since been devised to efficiently solve problems believed to be classically hard, such as Shor's factoring algorithm (2). Building a fault-tolerant quantum computer to run Shor's algorithm, however, still requires long-term efforts. Quantum sampling algorithms (3-6), based on plausible computational complexity arguments, were proposed for near-term demonstrations of quantum computational speedup in solving certain well-defined tasks compared to current supercomputers. If the speedup appears overwhelming such that no classical computer can perform the same task in a reasonable amount of time and is unlikely overturned by classical algorithmic or hardware improvements, it was called quantum computational advantage or quantum supremacy (7, 8). Here, we use the first term.

A very recent experiment on a 53-qubit processor has generated a million noisy ( $\sim 0.2\%$  fidelity) samples in 200 s (8), while a supercomputer would take 10,000 years. It was soon argued that the classical algorithm can be improved to cost only a few days to compute all the  $2^{53}$  quantum probability amplitudes and generate ideal samples (9). Thus, if the competition were to generate a much larger size of samples, for example,  $\sim 10^{10}$ , the quantum advantage would be reversed provided with sufficient storage. This sample-size-dependence of the comparison—an analog to loopholes in Bell tests (10)—suggests that quantum advantage would require long-term competitions between faster classical simulations and improved quantum devices.

Boson sampling, proposed by Aaronson and Arkhipov (5), was the first feasible protocol for quantum computational advantage. In boson sampling and its variants (11, 12), non-classical light is injected into a linear optical network, and in the output highly random, photon-number- and path-entangled state is measured by single-photon detectors. The dimension of the entangled state grows exponentially with both the number of photons and the modes, which fast renders the storage of the quantum probability amplitudes impossible. The state-of-the-art classical simul

tion algorithm is to calculate one probability amplitude (Permanent of the submatrix) at a time. The Permanent is classically hard and at least one Permanent should be evaluated for each sample (13, 14), thus the sample size loophole can be avoided. In addition, boson samplers use photons which can be operated at room temperature and are robust to decoherence.

Early proof-of-principle demonstrations of boson sampling (15, 16) used probabilistic, post-selected pseudo-single photons from parametric down-conversion (PDC) (17). Improved single-photon sources based on quantum dots were developed and employed to increase the multi-photon count rates, which culminated at 14-photon detection (18). However, scaling up boson sampling to a computationally interesting regime remained an outstanding experimental challenge.

Recently, Gaussian boson sampling (GBS) (11, 12) has emerged as a new paradigm that can not only provide a highly-efficient approach to large-scale implementations but also offer potential applications in graph-based problems (19) and quantum chemistry (20). Instead of using single photons, GBS makes full use of the Gaussian nature of the PDC sources and utilizes single-mode squeezed states (SMSS) as input nonclassical light sources which can be deterministically prepared. Sending  $k$  SMSSs through an  $m$ -mode interferometer and sampling the output scattering events using threshold detectors (see fig. S1), it has been shown that the output distribution is related to a matrix function called Torontoonian (12) which is related to Permanent. Computing the Torontoonian appears a computationally hard problem in the complexity class #P. It was shown recently that it takes about two days to evaluate a Torontoonian function for a 50-photon click pattern (21).

Although there were small-scale demonstrations of GBS with up to five photons (22, 23), implementing a large-scale GBS faced significant challenges. First, it requires arrays of SMSSs with sufficiently high squeezing parameters, photon indistinguishability, and collection efficiency, simultaneously. Second, large interferometers are needed with full connectivity, matrix randomness, near-perfect wave-packet overlap and phase stability, and near-unity transmission rate, simultaneously. Third, in contrast to the Aaronson-Arkhipov boson sampling where there is no phase relation between single photons, GBS requires phase control of all the photon number states in the SMSSs. Fourth, high-efficiency detectors are needed to sample the output distribution. Finally, the obtained sparse samples from a huge output state-space should be validated, and the performance of the GBS should be benchmarked and compared with a supercomputer.

We start by describing the quantum light source arrays. Transform-limited laser pulses, with an average power of 1.4

W at a repetition rate of  $250\mathrm{kHz}$  (figs. S1 and S2), is split into 13 paths and focused on 25 PPKTP crystals (Fig. 1A and figs. S3 and S4) to produce 25 two-mode squeezed states (TMSSs), which is equivalent to 50 SMSSs using a hybrid encoding as discussed later. The relative phase and squeezing parameter for each pair are shown in Fig. 1B. The PPKTP crystals are designed and temperature-controlled (fig. S5) to generate degenerate and frequency-uncorrelated photon pairs, as confirmed by joint spectrum in Fig. 1C which predicts a spectral purity of 0.98. The purity is increased to 0.99 using a 12-nm filtering (figs. S6 and S7). A second estimation of the pairwise purity is by unheralded second-order correlation measurements (24). The measured purities are plotted in Fig. 1D, with an average of 0.938. The decrease of the purity compared to the prediction from the joint spectra is mainly due to self-phase modulation. Figure 1E shows that average collection efficiency is 0.628.

The whole optical setup—from the 25 PPKTPs to the 100-mode interferometer—must be locked to a fixed phase in the presence of various environmental perturbations. To this aim, we develop an active phase locking (Fig. 2A) over the whole optical path and passive stabilization inside the interferometer (Fig. 2B) (25). For the active locking, a typical time trace of the observed phase stability is shown in the upper panel of Fig. 2B, which locks the phase of the  $776\mathrm{nm}$  laser with a standard deviation of 0.04 rad  $[\sim 5\mathrm{nm}$ , see (25)]. For the passive stabilization, the drift is controlled to be within  $\lambda /180$  in 3.5 hours (see bottom panel of Fig. 2B). For the whole system, as shown in Fig. 2D, the high-frequency noise standard deviation is  $\lambda /350$  and the low-frequency drift is  $\lambda /63$  within 1 hour, a time sufficient for completing the sampling and characterizations. We estimate that the photon interference visibilities drop are less than  $1\%$  due to the phase instability.

We make use of both the photons' spatial and polarization degree of freedom to realize a  $100 \times 100$  unitary transformation (15, 26). Here, the mode mapping is  $\{1, 2, \ldots, 100\} = \{|H\rangle_1|V\rangle_1|H\rangle_2|V\rangle_2 \ldots |H\rangle_{50}|V\rangle_{50}\}$ , where  $H(V)$  denotes horizontal (vertical) polarization, and the subscripts denote the spatial mode in the interferometer. We develop a compact 3D design for the 50-spatial-mode interferometer, which simultaneously fulfills near-perfect phase stability and wave-packet overlap, full connectivity, random matrix, and near-unity transmission rate (Fig. 2C) (25). This optical network effectively consists of 300 beam splitters and 75 mirrors (see fig. S9). The transmission rate of the interferometer is measured to be  $97.7\%$ , and the average coupling efficiency in all the output ports is  $\sim 90\%$ . We estimate the mode mismatch causes a  $\sim 0.2\%$  drop of the interference visibility between independent photons.

Contrary to the Aaronson-Arkhipov boson sampling where the sampling matrix is given solely by the interfer-

ometer, the GBS matrix absorbs both the unitary transformation of the interferometer and the squeezing parameters and phases of the Gaussian input state. We reconstruct the corresponding unitary matrix of the spatial-polarization hybrid encoded  $100 \times 100$  interferometer as plotted in Fig. 2, E and F for the elements of amplitudes and phases, respectively. Further analysis shows that the obtained matrix is unitary (see fig. S14) and Haar-random (see fig. S15).

We name our GBS machine Jiuzhang. We start describing the experimental results from the easy regime where we can obtain the full output distribution. We test with three pairs of input TMSSs and 2-photon click in the output. The obtained distribution is plotted in Fig. 3A. We use fidelity  $(F)$  and total variance distance  $(D)$  to characterize the obtained distribution, defined by:  $F = \sum_{i} \sqrt{p_i q_i}$ , and  $D = \sum_{i} |p_i - q_i| / 2$  ( $p_i$  and  $q_i$  denote the theoretical and experimental probability of  $i$ -th basis, respectively). For a perfect bosonsampler, the fidelity should equal to 1 and the distance should be 0. The measured average fidelities and distances are 0.990(1) and 0.103(1). The data for all the 23 different input configurations are shown in Fig. 3B, which confirms that the GBS works properly.

Next we move to the sparse and intractable regime. Using 25 TMSSs input, the output photon number distribution using threshold detectors is plotted in Fig. 3C. The average click number is 43. Within 200 s, we obtain 3,097,810 events of 43-photon coincidence, and one 76-photon coincidence. The state-space dimension of our experiment is plotted in Fig. 3D, reaching up to  $10^{30}$ , which is 14 and 16 orders of magnitude larger than the previous experiments using superconducting qubits (8) and single photons (18).

While a full verification of the results in the large photon number regime is unlikely due to the nature of the sampling problem, we hope to provide strong evidence that the large-scale GBS continues to be governed by quantum mechanics when it reaches quantum advantage regime. The credibility of the certification processes (27-32) relies on gathering circumstantial evidence while ruling out possible hypotheses plausibly to occur in this experiment. We validate the desired input TMSSs against input photons that are thermal states—which would result from excessive photon loss—and distinguishable—which would be caused by mode mismatch.

First, we compare the obtained output distribution with the hypotheses using thermal light and distinguishable SMSSs. Figure 3E shows evidently strong deviations in their line shapes and peak positions, which support that the obtain distribution indeed arises from genuine multi-photon quantum interference. Second, we investigate two-point correlation (32), which is derived from the Hanbury-Brown-Twiss experiment, to reveal the nonclassical properties of the output light field. Here, the two-point correlation be

tween the mode  $i$  and the mode  $j$  is defined as:  $C_{i,j} = \left\langle \Pi_1^i\Pi_1^j\right\rangle -\left\langle \Pi_1^i\right\rangle \left\langle \Pi_1^j\right\rangle$ , where  $\Pi_1^i = \mathbf{I} - \left|0\right\rangle_i\left\langle 0\right|_i$  represent a click in mode  $i$ . We calculate the distribution of all  $C_{ij}$  for the experimentally obtained samples, which is then compared with those from theoretical predictions, thermal states hypothesis and distinguishable SMSSs hypothesis. As shown in Fig. 3F, the statistics of experimental samples significantly diverges from the two hypotheses and agrees with the theoretical prediction.

Having studied the whole distribution, third, we closely look into each subspace with a specific photon click number. We develop a method called heavy output generation (HOG) ratio test (25). Figure 3G and fig. S23 shows typical examples of HOG analysis for photon clicks from 26 to 38, which show a stark difference between TMSS with thermal states. We emphasize that the tested 26-38 click regime—which shares the same as higher photon number—is in the post-selected subspace that effectively suffers from more photon loss than in the regime with a larger number of clicks which we deduce can be validated against the thermal state hypothesis with higher confidence.

Fourth, we continue to rule out another important hypothesis that boson sampling output would be operationally indistinguishable from a uniform random outcome, one of the earliest criticisms (27) to boson sampling. In stark contrast, due to constructive and destructive interference, an ideal boson-sampler is expected to generate samples with lognormal-like distribution (4, 27). We develop a method (25) to reconstruct the theoretical probability distribution curve for the 40-photon case, as shown in Fig. 3H. We can match each obtained sample to the theoretical curve, as illustrated by the blue data points and vertical blue lines in Fig. 3H (see fig. S24 for more data). The frequency of occurrence of the blue lines is in a good agreement with the probability curve, which intuitively indicates that our results cannot be reproduced by a uniform sampler.

Finally, we estimate the classical computational cost to simulate an ideal GBS device. We have benchmarked the GBS on Sunway TaihuLight (21) using a highly optimized algorithm (33). The time cost to calculate one Torontonian scales exponentially as a function of output photon clicks. Moreover, to obtain one sample, one usually needs to calculate  $\sim 100$  Torontonians of the candidate samples (13). The GBS simultaneously generates samples of different photon-number coincidences (Fig. 3C), which can be seen as a high-throughput sampling machine. For each output channel and the registered counts in Fig. 3C, we calculate the corresponding time cost for the supercomputer (Fig. 4). Summing over the data points in Fig. 4, we estimate that the required time cost for the TaihuLight (Fugaku) to generate the same amount of samples in  $200\mathrm{s}$  with the GBS device would be  $8\times 10^{16}\mathrm{s}$  ( $2\times 10^{16}\mathrm{s}$ ), which is 2.5 (0.6) billion years. We hope

this work will inspire new theoretical efforts to quantitatively characterize large-scale GBS, improve the classical simulation strategies optimized for the realistic parameters (33, 34), and challenge the observed quantum computational advantage of  $\sim 10^{14}$ .

# REFERENCES AND NOTES

1. E. Bernstein, U. Vazirani, in Proceedings of the 25th Annual ACM Symposium on Theory of Computing (1993). doi:10.1145/167088.167097  
2. P. W. Shor, in Proceedings of the 35th Annual Symposium on Foundations of Computer Science (1994). doi:10.1109/SFCS.1994.365700  
3. B. M. Terhal, D. P. DiVincenzo, Adaptive Quantum Computation, Constant Depth Quantum Circuits and Arthur-Merlin Games. arXiv 0205133 [quant-ph] (11 March 2004).  
4. S. Aaronson, A. Arkhipov, in Proceedings of the 43rd Annual ACM Symposium on Theory of Computing (2011). doi:10.1145/1993636.1993682  
5. S. Aaronson, L. Chen, in Proceedings of the 32nd Computational Complexity Conference (2017).  
6. M. J. Bremner, A. Montanaro, D. J. Shepherd, Average-Case Complexity Versus Approximate Simulation of Commuting Quantum Computations. Phys. Rev. Lett. 117, 080501 (2016). doi:10.1103/PhysRevLett.117.080501 Medline  
7. J. Preskill, Rapporteur talk at the 25th Solvay Conference on Physics, Brussels (2012).  
8. F. Arute, K. Arya, R. Babbush, D. Bacon, J. C. Bardin, R. Barends, R. Biswas, S. Boixo, F. G. S. L. Brandao, D. A. Buell, B. Burkett, Y. Chen, Z. Chen, B. Chiaro, R. Collins, W. Courtney, A. Dunsworth, E. Farhi, B. Foxen, A. Fowler, C. Kidney, M. Giustina, R. Graff, K. Guerin, S. Habegger, M. P. Harrigan, M. J. Hartmann, A. Ho, M. Hoffmann, T. Huang, T. S. Humble, S. V. Isakov, E. Jeffrey, Z. Jiang, D. Kafri, K. Kechedzhi, J. Kelly, P. V. Klimov, S. Knysh, A. Korotkov, F. Kostritsa, D. Landhuis, M. Lindmark, E. Lucero, D. Lyakh, S. Mandra, J. R. McClean, M. McEwen, A. Megrant, X. Mi, K. Michielsen, M. Mohseni, J. Mutus, O. Naaman, M. Neeley, C. Neill, M. Y. Niu, E. Ostby, A. Petukhov, J. C. Platt, C. Quintana, E. G. Rieffel, P. Roushan, N. C. Rubin, D. Sank, K. J. Satzinger, V. Smelyanskiy, K. J. Sung, M. D. Trevithick, A. Vainsencher, B. Villalonga, T. White, Z. J. Yao, P. Yeh, A. Zalcman, H. Neven, J. M. Martinis, Quantum supremacy using a programmable superconducting processor. Nature 574, 505-510 (2019). doi:10.1038/s41586-019-1666-5 Medline  
9. E. Pednault, J. A. Gunnels, G. Nannicini, L. Horesh, R. Wisnieff, Leveraging Secondary Storage to Simulate Deep 54-qubit Sycamore Circuits. arXiv 1910.09534 [quant-ph] (22 October 2019).  
10. A. W. Harrow, A. Montanaro, Quantum computational supremacy. Nature 549, 203-209 (2017). doi:10.1038/nature23458 Medline  
11. C. S. Hamilton, R. Kruse, L. Sansoni, S. Barkhofen, C. Silberhorn, I. Jex, Gaussian Boson Sampling. Phys. Rev. Lett. 119, 170501 (2017). doi:10.1103/PhysRevLett.119.170501 Medline  
12. N. Quesada, J. M. Arrazola, N. Killoran, Gaussian boson sampling using threshold detectors. Phys. Rev. A 98, 062322 (2018). doi:10.1103/PhysRevA.98.062322  
13. A. Neville, C. Sparrow, R. Clifford, E. Johnston, P. M. Birchall, A. Montanaro, A. Laing, Classical boson sampling algorithms with superior performance to nearterm experiments. Nat. Phys. 13, 1153-1157 (2017). doi:10.1038/nphys4270  
14. P. Clifford, R. Clifford, in Proceedings of the 29th Annual ACM-SIAM Symposium on Discrete Algorithms (2018).  
15. M. A. Broome, A. Fedrizzi, S. Rahimi-Keshari, J. Dove, S. Aaronson, T. C. Ralph, A. G. White, Photonic boson sampling in a tunable circuit. Science 339, 794-798 (2013). doi:10.1126/science.1231440 Medline  
16. J. B. Spring, B. J. Metcalf, P. C. Humphreys, W. S. Kolthammer, X.-M. Jin, M. Barbieri, A. Datta, N. Thomas-Peter, N. K. Langford, D. Kundys, J. C. Gates, B. J. Smith, P. G. R. Smith, I. A. Walmsley, Boson sampling on a photonic chip. Science

339.798-801 (2013). doi:10.1126/science.1231692 Medline  
17. P. G. Kwiat, K. Mattle, H. Weinfurter, A. Zeilinger, A. V. Sergienko, Y. Shih, New high-intensity source of polarization-entangled photon pairs. Phys. Rev. Lett. 75, 4337-4341 (1995). doi:10.1103/PhysRevLett.75.4337 Medline  
18. H. Wang, J. Qin, X. Ding, M.-C. Chen, S. Chen, X. You, Y.-M. He, X. Jiang, L. You, Z. Wang, C. Schneider, J. J. Renema, S. Hofling, C.-Y. Lu, J.-W. Pan, Boson Sampling with 20 Input Photons and a 60-Mode Interferometer in a  $10^{14}$ -Dimensional Hilbert Space. Phys. Rev. Lett. 123, 250503 (2019). doi:10.1103/PhysRevLett.123.250503 Medline  
19. J. M. Arrazola, T. R. Bromley, Using Gaussian Boson Sampling to Find Dense Subgraphs. Phys. Rev. Lett. 121, 030503 (2018). doi:10.1103/PhysRevLett.121.030503 Medline  
20. J. Huh, G. G. Guerreschi, B. Peropadre, J. R. McClean, A. Aspuru-Guzik, Boson sampling for molecular vibronic spectra. Nat. Photonics 9, 615-620 (2015). doi:10.1038/nphoton.2015.153  
21. X. Li et al., Benchmarking 50-Photon Gaussian Boson Sampling on the Sunway TaihuLight. arXiv 2009.01177 [cs.DC] (2 September 2020).  
22. H.-S. Zhong, L.-C. Peng, Y. Li, Y. Hu, W. Li, J. Qin, D. Wu, W. Zhang, H. Li, L. Zhang, Z. Wang, L. You, X. Jiang, L. Li, N.-L. Liu, J. P. Dowling, C.-Y. Lu, J.-W. Pan, Experimental Gaussian Boson sampling. Sci. Bull. 64, 511-515 (2019). doi:10.1016/j.scib.2019.04.007  
23. S. Paesani, Y. Ding, R. Santagati, L. Chakhmakhchyan, C. Vigliar, K. Rottwitt, L. K. Oxenlowe, J. Wang, M. G. Thompson, A. Laing, Generation and sampling of quantum states of light in a silicon chip. Nat. Phys. 15, 925-929 (2019). doi:10.1038/s41567-019-0567-8  
24. A. Christ, K. Laiho, A. Eckstein, K. N. Cassemiro, C. Silberhorn, Probing multimode squeezing with correlation functions. New J. Phys. 13, 033027 (2011). doi:10.1088/1367-2630/13/3/033027  
25. See supplementary materials.  
26. I. Dhand, S. K. Goyal, Realization of arbitrary discrete unitary transformations using spatial and internal modes of light. Phys. Rev. A 92, 043813 (2015). doi:10.1103/PhysRevA.92.043813  
27. S. Aaronson, A. Arkhipov, BosonSampling is far from uniform. Quantum Inf. Comput. 14, 1383 (2014).  
28. M. C. Tichy, K. Mayer, A. Buchleitner, K. Mølmer, Stringent and efficient assessment of boson-sampling devices. Phys. Rev. Lett. 113, 020502 (2014). doi:10.1103/PhysRevLett.113.020502 Medline  
29. M. Walschaers, J. Kuipers, J.-D. Urbina, K. Mayer, M. C. Tichy, K. Richter, A. Buchleitner, Statistical benchmark for BosonSampling. New J. Phys. 18, 032001 (2016). doi:10.1088/1367-2630/18/3/032001  
30. N. Spagnolo, C. Vitelli, M. Bentivegna, D. J. Brod, A. Crespi, F. Flamini, S. Giacomini, G. Milani, R. Ramponi, P. Mataloni, R. Osellame, E. F. Galvão, F. Sciarrino, Experimental validation of photonic boson sampling. Nat. Photonics 8, 615-620 (2014). doi:10.1038/nphoton.2014.135  
31. J. Carolan, J. D. A. Meinecke, P. J. Shadbolt, N. J. Russell, N. Ismail, K. Wörhoff, T. Rudolph, M. G. Thompson, J. L. O'Brien, J. C. F. Matthews, A. Laing, On the experimental verification of quantum complexity in linear optics. Nat. Photonics 8, 621-626 (2014). doi:10.1038/nphoton.2014.152  
32. D. S. Phillips, M. Walschaers, J. J. Renema, I. A. Walmsley, N. Treps, J. Sperling, Benchmarking of Gaussian boson sampling using two-point correlators. Phys. Rev. A 99, 023836 (2019). doi:10.1103/PhysRevA.99.023836  
33. N. Quesada, J. M. Arrazola, Exact simulation of Gaussian boson sampling in polynomial space and exponential time. Phys. Rev. Res. 2, 023005 (2020). doi:10.1103/PhysRevResearch.2.023005  
34. H. Qi, D. J. Brod, N. Quesada, R. García-Patrón, Regimes of Classical Simulability for Noisy Gaussian Boson Sampling. Phys. Rev. Lett. 124, 100502 (2020). doi:10.1103/PhysRevLett.124.100502 Medline  
35. S. M. Barnett, P. M. Radmore, Methods in Theoretical Quantum Optics (Oxford Science, 1997).

36. W. P. Grice, A. B. U'Ren, I. A. Walmsley, Eliminating frequency and space-time correlations in multiphoton states. Phys. Rev. A 64, 063815 (2001). doi:10.1103/PhysRevA.64.063815  
37. P. B. Dixon, J. H. Shapiro, F. N. C. Wong, Spectral engineering by Gaussian phase-matching for quantum photonics. Opt. Express 21, 5879-5890 (2013). doi:10.1364/OE.21.005879 Medline  
38. S. Rahimi-Keshari, M. A. Broome, R. Fickler, A. Fedrizzi, T. C. Ralph, A. G. White, Direct characterization of linear-optical networks. Opt. Express 21, 13450-13458 (2013). doi:10.1364/OE.21.013450 Medline  
39. H. Wang, Y. He, Y.-H. Li, Z.-E. Su, B. Li, H.-L. Huang, X. Ding, M.-C. Chen, C. Liu, J. Qin, J.-P. Li, Y.-M. He, C. Schneider, M. Kamp, C.-Z. Peng, S. Hofling, C.-Y. Lu, J.-W. Pan, High-efficiency multiphoton boson sampling. Nat. Photonics 11, 361-365 (2017). doi:10.1038/nphoton.2017.63  
40. W. J. Zhang, L. X. You, H. Li, J. Huang, C. L. Lv, L. Zhang, X. Y. Liu, J. J. Wu, Z. Wang, X. M. Xie, NbN superconducting nanowire single photon detector with efficiency over  $90\%$  at 1550 nm wavelength operational at compact cryocooler temperature. Sci. China Phys. Mech. Astron. 60, 120314 (2017). doi:10.1007/s11433-017-9113-4  
41. S. Rahimi-Keshari, A. P. Lund, T. C. Ralph, What can quantum optics say about computational complexity theory? Phys. Rev. Lett. 114, 060501 (2015). doi:10.1103/PhysRevLett.114.060501 Medline  
42. M. Tillmann, B. Dakic, R. Heilmann, S. Nolte, A. Szameit, P. Walther, Experimental boson sampling. Nat. Photonics 7, 540-544 (2013). doi:10.1038/nphoton.2013.102  
43. A. Crespi, R. Osellame, R. Ramponi, D. J. Brod, E. F. Galvão, N. Spagnolo, C. Vitelli, E. Maiorino, P. Mataloni, F. Sciarrino, Integrated multimode interferometers with arbitrary designs for photonic boson sampling. Nat. Photonics 7, 545-549 (2013). doi:10.1038/nphoton.2013.112  
44. J. Carolan, C. Harrold, C. Sparrow, E. Martin-Lopez, N. J. Russell, J. W. Silverstone, P. J. Shadbolt, N. Matsuda, M. Oguma, M. Itoh, G. D. Marshall, M. G. Thompson, J. C. F. Matthews, T. Hashimoto, J. L. O'Brien, A. Laing, Universal linear optics. Science 349, 711-716 (2015). doi:10.1126/science.aab3642 Medline  
45. Y. He, X. Ding, Z.-E. Su, H.-L. Huang, J. Qin, C. Wang, S. Unsleber, C. Chen, H. Wang, Y.-M. He, X.-L. Wang, W.-J. Zhang, S.-J. Chen, C. Schneider, M. Kamp, L.-X. You, Z. Wang, S. Hofling, C.-Y. Lu, J.-W. Pan, Time-Bin-Encoded Boson Sampling with a Single-Photon Device. Phys. Rev. Lett. 118, 190501 (2017). doi:10.1103/PhysRevLett.118.190501 Medline  
46. J. C. Loredo, M. A. Broome, P. Hilaire, O. Gazzano, I. Sagnes, A. Lemaitre, M. P. Almeida, P. Senellart, A. G. White, Boson Sampling with Single-Photon Fock States from a Bright Solid-State Source. Phys. Rev. Lett. 118, 130503 (2017). doi:10.1103/PhysRevLett.118.130503 Medline  
47. H. Wang, W. Li, X. Jiang, Y.-M. He, Y.-H. Li, X. Ding, M.-C. Chen, J. Qin, C.-Z. Peng C. Schneider, M. Kamp, W.-J. Zhang, H. Li, L-X. You, Z. Wang, J. P. Dowling, S. Hofling, C.-Y. Lu, J.-W. Pan, Toward Scalable Boson Sampling with Photon Loss. Phys. Rev. Lett. 120, 230502 (2018). doi:10.1103/PhysRevLett.120.230502 Medline  
48. M. Bentivegna, N. Spagnolo, C. Vitelli, F. Flamini, N. Viggianiello, L. Latmiral, P. Mataloni, D. J. Brod, E. F. Galvão, A. Crespi, R. Ramponi, R. Osellame, F. Sciarrino, Experimental scattershot boson sampling. Sci. Adv. 1, e1400255 (2015). doi:10.1126/sciadv.1400255 Medline  
49. H.-S. Zhong, Y. Li, W. Li, L.-C. Peng, Z.-E. Su, Y. Hu, Y.-M. He, X. Ding, W. Zhang, H. Li, L. Zhang, Z. Wang, L. You, X.-L. Wang, X. Jiang, L. Li, Y.-A. Chen, N.-L. Liu, C.-Y. Lu, J.-W. Pan, 12-Photon Entanglement and Scalable Scattershot Boson Sampling with Optimal Entangled-Photon Pairs from Parametric Down-Conversion. Phys. Rev. Lett. 121, 250505 (2018). doi:10.1103/PhysRevLett.121.250505 Medline  
50. I. Agresti, N. Viggianiello, F. Flamini, N. Spagnolo, A. Crespi, R. Osellame, N. Wiebe, F. Sciarrino, Pattern Recognition Techniques for Boson Sampling Validation. Phys. Rev. X 9, 011013 (2019). doi:10.1103/PhysRevX.9.011013

# ACKNOWLEDGMENTS

This work is dedicated to the people in the fight against the COVID-19 outbreak during which the final stage of this experiment was carried out. We thank Jelmer Renema, J.P. Dowling, Christian Weedbrook, Nicolas Quesada, Yi Jiang, Jin-Wei Jiang, SiQiu Gong, Bai-Bo Wang, Yu-Huai Li, Hao-Wen Cheng, Qi Shen, Yuan Cao, Yaojian Chen, Haitian Lu, Haohuan Fu, and Teng-Yun Chen for very helpful discussions and assistance. Funding: This work was supported by the National Natural Science Foundation of China, the National Key R&D Program of China, the Chinese Academy of Sciences, the Anhui Initiative in Quantum Information Technologies, and the Science and Technology Commission of Shanghai Municipality. Author contributions: C.-Y.L. and J.-W.P. designed and supervised the research. H.-S.Z., M.-C.C. and J.Q. developed the theory. H.-S.Z., H.W., Y.-H.D., L.-C.P., Y.-H.L., J.Q., D.W., X.D., L.-L., N.L. and C.-Y.L. carried out the optical experiment and collect the data. Y.H. and X.J. designed the 100-channel counter. M.-C.C., Y.L., P.H., L.G., and G.Y. performed data analysis and validation on a supercomputer. P.H., X.-Y.Y., W.-J.Z., H.L., L.Y., and Z.W. developed single-photon detectors. H.-S.Z., M.-C.C., C.-Y.L. and J.-W.P. analyzed the data and prepared the manuscript. All authors discussed the results, and reviewed the manuscript. Competing interests: The authors declare no competing interests. Data and materials availability: All data are available in the manuscript or the supplementary materials. Requests for materials should be addressed to C.-Y.L. or J.-W.P.

# SUPPLEMENTARY MATERIALS

science.sciencemag.org/cgi/content/full/science.eabe8770/DC1

Materials and Methods

Supplementary Text

Figs. S1 to S28

Tables S1 to S3

References (35-50)

19 September 2020; accepted 19 November 2020

Published online 3 December 2020

10.1126/science.abe8770

![](images/0b81eb0776dd6b8ea810595c998063d074dbbce63b41d85ba00075c91ce069da.jpg)

![](images/f0270c210a2331c9cb6b347666ef7bc01849390f65db785090d65cc0744eafe0.jpg)

![](images/c86c04604cddd93416b13df9417b702071926bc2db2a63623f1ea9852e00ae76.jpg)  
Fig. 1. Quantum light sources for the GBS. (A) An illustration of the experimental setup for generating squeezed states. A custom-designed laser system consisting of a Mira 900, a pulse shaper, and a RegA 9000 is used to generate the pump laser, which was spectrally and spatially shaped to reach transform limit (figs. S1 and S2). The pulsed laser is split into 13 paths (figs. S3 and S4) and focused onto 25 PPKTP crystals. Each crystal is placed on a thermoelectric cooler (TEC) for wavelength tuning. The down-converted photons are separated from the pumping laser by a dichromic mirror (DM), the time walk between different polarizations are compensated by a KTP crystal. (B) Wigner functions of all the 25 sources. The squeezing parameter  $r$  and phase  $\phi$  of each source is presented as  $(r, \phi)$  in each panel. (C) The measured joint spectrum of the photon pairs indicates that the two photons are frequency uncorrelated. (D) The purity of the 25 photon sources. The measured average purity is 0.938, obtained by unheraldised second-order correlation measurement. (E) The measured collection efficiencies with an average of 0.628.

![](images/c03fe034667f9fbf73f1dc0388e70a7c045c8f04a010826ab831db5077e60804.jpg)

![](images/95deefef28809e5b76260856aa73c0de9459fb731122416771d5918a9e52200c.jpg)

![](images/b3201dde1c6aabfeed1382c98b61e60ab38c9f15a0ddf6043f310cfcc512e247.jpg)

![](images/c941eda6d8d40100538189e22d4292862fa678efcaf83176e19c2564f74e9a73.jpg)

![](images/efea69cf85e0eb0e4e0f40a861bb262b052bdb75ad0f1ee1ffae3c012a6ef437.jpg)

![](images/8f177a8b2657913506f259a95ca7649a02d3ab1c192730e6c257446edf7f9163.jpg)

![](images/67fe9a52662fd63605292df5de1630f7246e274cf6c8cd5f423291bca26e65b3.jpg)  
Fig. 2. Phase-locking from the photon sources to the interferometer. (A) Schematic diagram of the active phase-locking system. A pump laser beam is used as a reference for all the squeezed states. After propagating through a  $\sim 2$ -m free space and  $20\mathrm{-m}$  optical fiber, a  $\sim 10~\mu \mathrm{W}$  pump laser which shares the same propagation path as the down-converted photons is separated by a dichromatic mirror, which are then combined on a beam splitter with the reference laser pulse. A balanced detection scheme, which is insensitive to laser power fluctuation, is used to read out the phase information. To overcome the path length fluctuates, we wind 5-m-length optical fiber around a piezoelectric cylinder which has a sensitivity of  $1.5\mathrm{rad} / \mathrm{V}$ , a resonance frequency of  $18.3\mathrm{kHz}$  and a dynamical range of  $300\mathrm{rad}$ . (B) Phase stability tests. The upper (bottom) panel is a typical monitoring of phase fluctuation of active (passive) phase locking over 3.5 hours. The measured standard deviation of the phase is as small as  $0.02\mathrm{rad}$  ( $\lambda / 150$ ) (0.017 rad ( $\lambda / 180$ )). (C) We apply passive phase stabilization to the interferometer by adhering the devices onto an ultralow-expansion glass plate which is temperature stabilized within  $0.02^{\circ}\mathrm{C}$ . The blue light paths are for the interference of the 25 pumping lasers with the reference laser. The red light paths are the input and output of the photonic network. (D) A typical phase stability measurement of the whole system in one hour. (E) The diagram of the measured 5000 amplitudes of the matrix. (F) The diagram of the measured 5000 phases of the matrix.

![](images/5343b0dbdc799cd435733ec772815e1c2591635b43cd1797fac1c834862bb03e.jpg)

![](images/cc48896f0916efb1fabe9d2f83d392a664f7a7242de6e313e448a621ea8a4dea.jpg)

![](images/25c27e6f27dd6008d7ae56fe796d35421a48e2a1766c66828e54443e0365bbc4.jpg)

![](images/5862b76046f2965dc6831410f60265b66da469d5996b0c0ffcc1060d6b132b0d.jpg)

![](images/5cf1c0dbb3977536dc71e3c7e861b0ade28e2dcf03e3057ca8c2069e201ee162.jpg)

![](images/d22453ff8f6a7874c62b3e6e3042d6d0deea849410af5fa7a8b2379fb3c04c07.jpg)  
Fig. 3. Experimental validation of the GBS. (A) Experimental (red) and theoretical (blue) two-photon distribution with three TMSSs input. (B) Summary of statistical fidelity and total variation distance of two-photon distribution for 23 different input sets. (C) The output photon number distribution with all 25 TMSSs in. The average detected photon number is 43, while the maximal detected photon number is 76. (D) Summary of the output state-space dimension. (E) The photon-number distributions of the experimental result (red), from thermal state (blue) and distinguishable SMSS (purple), respectively. The deviations of the line shape and peak positions indicate that our experiment is far from these two hypotheses. (F) Two-photon correlation statistics for all 2-mode combinations. The statistic of the experimental results (red) highly overlap with the theoretical predictions (orange), and deviate significantly from the thermal state hypothesis (blue) and the distinguishable SMSS hypothesis (purple). (G) Validation against thermal-state hypothesis with detected photon number ranging from 26 to 30. (H) Validation against uniform distribution.

![](images/1b0eff6b82876850c25d8d69d099f10f964d2ec99976c80b482699fadff70012.jpg)

![](images/84080148ec3a96083c3386bc36e3d2bdc3fff83b75ebcceca842ce760d31d7b3.jpg)

![](images/d92eefc5804246277ee6db5900e23eda706399dcbbade3193919484598947c8a.jpg)

![](images/66081825ff4cbfb7cc2f4bf118a7a5d833ed739fd8a0297aafa6b1291f1ee97b.jpg)  
Fig. 4. Classical computational cost. The estimated time cost on Sunway TaihuLight supercomputer. The error bar is calculated from Poissonian counting statistics of the raw detected events.

# Quantum computational advantage using photons

Han-Sen Zhong, Hui Wang, Yu-Hao Deng, Ming-Cheng Chen, Li-Chao Peng, Yi-Han Luo, Jian Qin, Dian Wu, Xing Ding, Yi Hu, Peng Hu, Xiao-Yan Yang, Wei-Jun Zhang, Hao Li, Yuxuan Li, Xiao Jiang, Lin Gan, Guangwen Yang, Lixing You, Zhen Wang, Li Li, Nai-Le Liu, Chao-Yang Lu and Jian-Wei Pan

published online December 3, 2020

# ARTICLE TOOLS

http://science.sciencemag.org/content/early/2020/12/02/science.abe8770

# SUPPLEMENTARY MATERIALS

http://science.sciencemag.org/content/suppl/2020/12/02/science.abe8770.DC1

# REFERENCES

This article cites 42 articles, 4 of which you can access for free http://science.sciencemag.org/content/early/2020/12/02/science.abe8770#BIBL

# PERMISSIONS

http://www.sciencemag.org/help/reprints-and-permissions

Use of this article is subject to the Terms of Service