# High-efficiency multiphoton boson sampling

Hui Wang $^{1,2\dagger}$ , Yu He $^{1,2\dagger}$ , Yu-Huai Li $^{1,2\dagger}$ , Zu-En Su $^{1,2}$ , Bo Li $^{1,2}$ , He-Liang Huang $^{1,2}$ , Xing Ding $^{1,2}$ , Ming-Cheng Chen $^{1,2}$ , Chang Liu $^{1,2}$ , Jian Qin $^{1,2}$ , Jin-Peng Li $^{1,2}$ , Yu-Ming He $^{1,2,3}$ , Christian Schneider $^{3}$ , Martin Kamp $^{3}$ , Cheng-Zhi Peng $^{1,2}$ , Sven Höfling $^{1,3,4}$ , Chao-Yang Lu $^{1,2\star}$  and Jian-Wei Pan $^{1,2\star}$

Boson sampling is considered as a strong candidate to demonstrate 'quantum computational supremacy' over classical computers. However, previous proof-of-principle experiments suffered from small photon number and low sampling rates owing to the inefficiencies of the single-photon sources and multiport optical interferometers. Here, we develop two central components for high-performance boson sampling: robust multiphoton interferometers with  $99\%$  transmission rate and actively demultiplexed single-photon sources based on a quantum dot-micropillar with simultaneously high efficiency, purity and indistinguishability. We implement and validate three-, four- and five-photon boson sampling, and achieve sampling rates of  $4.96\mathrm{kHz}$ ,  $151\mathrm{Hz}$  and  $4\mathrm{Hz}$ , respectively, which are over 24,000 times faster than previous experiments. Our architecture can be scaled up for a larger number of photons and with higher sampling rates to compete with classical computers, and might provide experimental evidence against the extended Church-Turing thesis.

Quantum computers<sup>1</sup> can, in principle, solve certain problems faster than classical computers. Despite substantial progress in the past two decades<sup>2-4</sup>, building quantum machines that can actually outperform classical computers for some specific tasks —an important milestone termed 'quantum supremacy'—remains challenging. In the quest of demonstrating quantum supremacy, boson sampling, an intermediate (that is, non-universal) quantum computer model proposed by Aaronson and Arkhipov<sup>5</sup>, has received considerable interest as it requires fewer physical resources than building universal optical quantum computers<sup>6</sup>.

A quantum boson-sampling machine can be realized by sending  $n$  indistinguishable single photons through a passive  $m$ -mode ( $m > n$ ) interferometer, and sampling from the probabilistic output distribution. Mathematically, the probability amplitude of each output outcome is proportional to the permanent of a corresponding  $n \times n$  submatrix, which is strongly believed to be intractable because calculating the permanent is a so-called #P-complete problem. Note that, however, boson sampling is itself not a #P-complete problem, that is, the matrix permanent cannot be efficiently calculated. For a specifically defined task of sampling over the entire distribution, it is expected that a sufficiently large quantum boson-sampling machine cannot be efficiently simulated by classical computers[5,7,8]. In principle, a large-scale boson-sampling machine would constitute an effective disproof against a foundational tenet in computer science: the extended Church-Turing thesis, which postulates that all realistic physical systems can be efficiently simulated with a (classical) probabilistic Turing machine.

To this end, an experimental roadmap for demonstrating quantum supremacy is to construct multiphoton boson-sampling machines with increasing number of input photons and faster sampling rates to compete with classical computers. However, the overall performance of previous proof-of-principle boson-sampling experiments[9-17] was limited due to the lack of high-quality single-photon sources and low-loss multimode circuits. For example, the most commonly used pseudo-single photonics created using

spontaneous parametric down-conversion $^{18}$  (SPDC) were intrinsically probabilistic and mixed with multiphoton components. The SPDC probability was kept low (about a few per cent) to suppress the unwanted two-photon emission. The frequency correlation of the SPDC photon pairs and the inefficient collection into single-mode fibres further reduced the single-photon heralding efficiency to typically a low level of  $\sim 1\%$  in previous work $^{9-16}$  (Supplementary Table 1). In addition, the boson-sampling rate was significantly reduced due to the coupling and propagation loss in the multimode photonic circuits. In an attempt to solve the intrinsic probabilistic problem of SPDC, spatial or temporal multiplexing $^{19,20}$  and scattershot boson sampling $^{21}$  schemes were proposed and demonstrated $^{14}$ . Yet, so far, all previous quantum optical boson-sampling machines $^{9-17}$  have demonstrated only up to three single photons with arbitrary input configurations and 4-6 photons in special Fock states, and the obtained sampling rates were several orders of magnitude too low to even outperform some of the earliest classical computers.

# Indistinguishable single photons

Scaling up boson sampling to a large number of photons and with high sampling rates represents a nontrivial experimental challenge. Importantly, it requires high-performance single quantum emitters $^{22-24}$  that can deterministically produce only one photon under each pulsed excitation. The generated photons must simultaneously have high single-photon purity (that is, the multiphoton probability should be vanishingly small), high indistinguishability (that is, photons are quantum mechanically identical to each other), and high collection efficiency into a single spatial mode $^{25-27}$ . These three key features are simultaneously realized in our experiment using pulsed  $s$ -shell resonant excitation $^{28}$  of a single self-assembled InAs/GaAs quantum dot embedded inside a micropillar cavity $^{29-31}$  (Fig. 1 and Supplementary Information).

At  $\pi$  pulse excitation with a repetition rate of  $76\mathrm{MHz}$ , the quantum dot-micropillar emits  $\sim 25.6$  million polarized, resonance

![](images/1ad6dcc5a81dc90773fa9796d4ebc593af2cdf5097e6ccceefb7752e23183b16.jpg)  
Figure 1 | Experimental set-up for multiphoton boson-sampling. The set-up includes four key parts: the single-photon device, demultiplexers, ultra-low-loss photonic circuit and detectors. The single-photon device is a single InAs/GaAs quantum dot coupled to a  $2\text{-}\mu \mathrm{m}$  diameter micropillar cavity, which yields a Purcell factor of 7.63(23) at resonance. The quantum dot is coherently pumped by a picosecond laser. A confocal microscope is operated in a cross-polarization configuration to extinguish laser background. The resonance fluorescence single photons collected into a single-mode fibre are sent to active demultiplexers, which consist of Pockels cells and polarizing beam splitters, and separated into five spatial modes. The five photons are then fed into a tailormade ultra-low-loss photonic circuit that consists of 36 beam splitters. Finally, the output of the interferometer is measured by nine single-photon detectors and the multiphoton coincidence analysed by a time-to-digit converter (TDC).

fluorescence single photons per second at the output of a single-mode fibre, of which  $\sim 6.5$  million are eventually detected on a silicon single-photon detector. Considering the detector dead time of  $\sim 42$  ns, the actual count rate should be corrected to  $9\mathrm{MHz}$  (Fig. 2a). This is the brightest single-photon source reported in all physical systems to date. These single photons are directly used—without any spectral filtering—for the photon correlation and interference measurements, and for boson sampling. We measured second-order correlation of the photon source, and observed  $g^{2}(0) = 0.027(1)$  at zero time delay, which confirmed the high purity of the single-photon Fock state. We performed Hong-Ou-Mandel interference as a function of the emission time separation between two single photons<sup>31</sup>. With a time separation of  $13~\mathrm{ns}$  and  $14.7~\mu \mathrm{s}$ , photon indistinguishabilities of 0.939(3) and 0.900(3) were measured, respectively (Fig. 2b and Supplementary Information). Thanks to the pulsed resonant excitation method that eliminates dephasings and time jitter<sup>28</sup>, we obtained long streams of near-transform-limited single photons that are sufficient for multiphoton experiments on a semiconductor chip for the first time.

# Efficient multiphoton source

Next, we demultiplexed the single-photon stream into different spatial modes using fast optical switches that consist of Pockels cells (with a transmission rate  $>99\%$  and extinction ratio  $>100:1$ ) and polarizing beam splitters (with an extinction ratio  $>1,200:1$ ). The Pockels cells, synchronized to the pulsed laser and operated at  $0.76 \mathrm{MHz}$  with a rise time of 8 ns, converted the single-photon pulse train into 3, 4, or 5 separate beams (Supplementary Information and Supplementary Fig. 5). The largest time separation between two demultiplexed photons is  $\sim 1.05 \mu \mathrm{s}$  (80 pulses), where the photon indistinguishability remains 0.923 (Fig. 2b).

To ensure that these pulses arrived simultaneously at a multi-mode interferometer, optical fibres of different lengths and a translation stage were used to finely adjust their arrival time. The average efficiency of the optical switches is  $\sim 84.5\%$ , which was mainly due to the coupling efficiency and propagation loss in the optical fibres. The efficiency can be improved in the future by using faster Pockels cells (Supplementary Information). Thus, we eventually

obtained five separate single-photon sources with end-user efficiencies of about  $28.4\%$ . Note that the active demultiplexing method eliminates the need to overcome the inhomogeneity of independent self-assembled quantum dots to build many identical sources<sup>32</sup>.

# Ultra-low-loss photonic circuit

Another important ingredient for reliable and fast boson-sampling is a multimode interferometric linear optical network that is phase stable, has high transmission rate and can implement a Haar random unitary matrix. While previously demonstrated waveguide-based photonic chips showed promise for large-scale integration $^{10-16}$ , the coupling and propagation loss in these chips seriously limited the overall efficiencies to  $\sim 30\%$  so far (Supplementary Table 1).

Here, we put forward a new circuit design that simultaneously combines stability, matrix randomness and ultra-low transmission loss. As shown in Fig. 1 (see also Supplementary Fig. 6), a  $9 \times 9$  mode interferometer is constructed, using a bottom-up approach, from individual tiny trapezoids. The surfaces of the trapezoids are optically coated with polarization-dependent beam-splitting ratios (Supplementary Information). This network consists of 36 beam splitters and 9 mirrors, and implements a near-unitary transformation to input states (Fig. 2c,d). Thanks to the antireflection coating, the overall transmission efficiency (from input to output) is measured to be above  $99\%$ . Through Mach-Zehnder-type coherence measurements, the spatial-mode overlap is determined to be better than  $99.9\%$ . The interferometer is housed on a temperature-stabilized baseplate, and remains stable for at least weeks (for a test of its robustness, see Supplementary Fig. 7). Such a design can be further improved[33] and scaled up to reasonably larger dimensions, which can be sufficient for the near-term goal of demonstrating quantum supremacy through boson sampling.

# Experimental results and validation

We sent three, four and five single photons into the nine-mode interferometer, and measured the output multiphoton events (Fig. 3). We used nine silicon single-photon avalanche detectors (efficiency  $\sim 32\%$ ), one in each output of the interferometer, to register the no-collision (one photon per output-mode) events, which

![](images/cd763fe0bc8ca38dc0309cd6d3980298885941ee63ce277f1684c1d1c57d061c.jpg)

![](images/fffa917bb427a5fa742ed7a1bafbb25b43c1307b4f97d25f3b6949b232d05278.jpg)

![](images/e12c7750a23b7cc0bca21ad9bda511128ab2ee2f8d27fbb8e201c35633b09738.jpg)  
Figure 2 | The single-photon source and interferometer for boson sampling. a, Observed Rabi oscillation by pulsed resonant excitation of the quantum dot. The blue dots denote single-photon counts directly measured by silicon detectors, whereas the red dots represent the counts after being corrected by the dead time of the detectors. The single-photon counts reach maximum at the  $\pi$  pulse power, which is  $1.6\mathrm{nW}$ . b, The measured photon indistinguishability drops slightly from 0.939(3) at 13 ns to a plateau of 0.900(3) at  $>10~\mu \mathrm{s}$  separation, fitted with a decaying time constant of  $2.1~\mu \mathrm{s}$ , assuming a non-Markovian noise model. The blue arrow indicates the regime in our current work where two photons are maximally separated by a time of  $1.05~\mu \mathrm{s}$  due to demultiplexing. The error bars denote one standard deviation, deduced from propagated Poissonian counting statistics of the raw photon detection events. c,d, Measured elements (amplitude (c) and phase (d)) of the unitary transformation of the optical network.

![](images/b3e1fe39219e1dce924baf67e5aeae5f269b36062b2ebbe3fb1869bed1279faa.jpg)

![](images/b7715045cada1a784cfec82ae2be17d24b497e69a231cefb1c1b795671727219.jpg)

![](images/af088410dd4ef5d2b118ab3eac5a7890966439432a4e4f2653f7747808be7741.jpg)

![](images/87d4f8ea6dbda7285432fdc2547ade526cd8b5d2b42217e838df2e10a1bbbc54.jpg)  
Figure 3 | Experimental results for the three-, four- and five-boson sampling. a-c. The measured relative frequencies of all no-collision output combinations, denoted by  $(i,j,\dots)$  where there is one photon detected in each output mode  $i,j,\ldots$ . The solid bars are the normalized coincidence rate of different output distribution. The empty bars are theoretical calculations in the ideal case. The error bars are one standard deviation deduced from Poissonian counting statistics.

![](images/65f072a0db564f433a28a0e1d12966aeb1a8e6258e302438804914b86fc327ca.jpg)  
Figure 4 | Validating boson-sampling results. The open points in a and the dotted lines in b are tests applied on simulated data generated from the two alternative hypotheses, sampling from a uniform distribution and distinguishable particles, respectively. And the solid points in a and solid lines in b are tests applied on the experimental data. A counter is updated for every event and a positive value validates the data being obtained from a genuine boson sampler. a, Application of the Bayesian analysis to test against uniform distribution. b, Discrimination of the data from a distinguishable sampler using a standard likelihood ratio test.

![](images/466f2ab62bff7b26d1db4c3f9be3a8b5274c0f20f2f50c4c88a9c68c48ab828b.jpg)

have 84, 126 and 126 different output distributions for the three-, four- and five-boson sampling, respectively. A total of 446,084 three-photon events (Fig. 3a), 36,261 four-photon events (Fig. 3b) and 11,660 five-photon events (Fig. 3c) were obtained in accumulation times of  $90~\mathrm{s}$ ,  $240~\mathrm{s}$  and  $2,900~\mathrm{s}$ , respectively. The obtained data (solid bars, denoted as  $q_{i}$ ) are plotted together with the ideal probability distribution (empty bars, denoted as  $p_i$ ) in Fig. 3. We quantified the match between these two sets of distributions using the measure of similarity, defined as  $F = \sum_{i} \sqrt{p_i q_i}$ , and the measure of distance, defined as  $D = (1/2) \sum_{i} |p_i - q_i|$ . From the data in Fig. 3, we calculated similarities of 0.984(1), 0.979(5) and 0.973(9), and distances of 0.125(1), 0.141(3) and 0.178(5) for the three-, four- and five-boson sampling, respectively.

For a large-scale boson-sampling device, not only the calculation of its outcome, but also a full certification of the outcome is strongly conjectured to be intractable for classical computation. There have been proposals $^{34-36}$  and demonstrations $^{15,16}$  for validating boson sampling that can provide supporting or circumstantial evidence for the correct operation of this protocol. In our work, we first employed Bayesian analysis $^{35}$  to rule out uniform distribution (Fig. 4a). With only  $\sim 20$  events, we can reach a confidence level of  $99.8\%$  that these outcomes are from genuine boson-samplers. Another possible hypothesis is using distinguishable single photons (classical particles) or spatial-mode mismatched interferometers. This hypothesis can be excluded by applying a standard likelihood ratio test $^{36}$ . Figure 4b shows an increasing difference between indistinguishable bosons (solid) and distinguishable bosons (dotted lines) as experimental events increase, and thus the distinguishable hypothesis is ruled out with only  $\sim 50$  events (Supplementary Information).

# Conclusion and outlook

We developed a high-efficiency source of highly indistinguishable single photons and ultra-low-loss photonic circuits, and demonstrated a three-boson sampling rate of  $4.96\mathrm{kHz}$ , which is  $\sim 27,000$  times faster than the best previous experiments using  $\mathrm{SPDC}^{9-16}$  and  $\sim 24,000$  times faster than recent work[17] using passive demultiplexing (thus intrinsically inefficient) of quantum-dot single photons using incoherent excitation that limited the photon indistinguishability to  $52 - 64\%$ . We also achieved the first four- and five-boson sampling using a single-photon Fock state—which were formidable challenges—and obtained high sampling rates of  $151\mathrm{Hz}$  and  $4\mathrm{Hz}$ , respectively. These multiphoton boson-sampling machines have also reached a computational complexity that can

compete with early classical computers. Under the specific racing rule in refs 5, 9 and 10, we could compare the required time for obtaining one output sample using the quantum machines with the simulated time for calculating one permanent using the published data of the early classical computers (Supplementary Information). As shown in Supplementary Table II, the quantum photonic machines are provably faster for the boson-sampling task than ENIAC and TRADIC, the first electronic computer and transistorized computer, respectively.

Our work has demonstrated a clear, realistic pathway to build boson-sampling machines with many photons and fast rates. Using superconducting nanowire single-photon detectors[37,38] with reported efficiency of  $\sim 95\%$  and antireflection optical coating, one can straightforwardly increase the three-, four- and five-boson sampling rates to  $130~\mathrm{kHz}$ ,  $12~\mathrm{kHz}$  and  $1\mathrm{kHz}$ , respectively, and implement 14-boson sampling with a count rate of  $5\mathrm{h}^{-1}$  (Supplementary Information). A remaining challenge is to remove the cross-polarization in the confocal set-up (used to extinguish the laser background), which reduced the single-photon source efficiency by half. Future work will focus on deterministic dot-micropillar coupling[39] and developing side excitation[40] to boost the single-photon source efficiency to over  $74\%$ , in which case we can expect a 20-boson sampling rate of  $\sim 130\mathrm{h}^{-1}$ , and an increasing quantum advantage over classical computation for a larger number of photons.

Data availability. The data that support the plots within this paper and other findings of this study are available from the corresponding author upon reasonable request.

Received 7 December 2016; accepted 3 April 2017; published online 1 May 2017

# References

1. Ladd, T. D. et al. Quantum computers. Nature 464, 45-53 (2010).  
2. Pan, J.-W. et al. Multiphoton entanglement and interferometry. Rev. Mod. Phys. 84, 777-838 (2012).  
3. Barends, R. et al. Superconducting quantum circuits at the surface code threshold for fault tolerance. Nature 508, 500-503 (2014).  
4. Monz, T. et al. Realization of a scalable Shor algorithm. Science 351, 1068-1070 (2016).  
5. Aaronson, S. & Arkhipov, A. The computational complexity of linear optics. In Proc. 43rd Annual ACM Symp. Theory of Computing 333-342 (ACM, 2011).  
6. Kok, P. et al. Linear optical quantum computing with photonic qubits. Rev. Mod. Phys. 79, 135-174 (2007).  
7. Rohde, P. R. & Ralph, T. C. Error tolerance of boson-sampling model for linear optical quantum computing. Phys. Rev. A 85, 022332 (2012).

8. Wu, J.-J. et al. Computing permanents for boson sampling on Tianhe-2 supercomputer. Preprint at https://arxiv.org/abs/1606.05836 (2016).  
9. Broome, M. A. et al. Photonic boson sampling in a tunable circuit. Science 339, 794-798 (2013).  
10. Spring, J. B. et al. Boson sampling on a photonic chip. Science 339, 798-801 (2013).  
11. Tillmann, M. et al. Experimental boson sampling. Nat. Photon. 7, 540-544 (2013).  
12. Crespi, A. et al. Integrated multimode interferometers with arbitrary designs for photonic boson sampling. Nat. Photon. 7, 545-549 (2013).  
13. Carolan, J. et al. Universal linear optics. Science 349, 711-716 (2015).  
14. Bentivegna, M. et al. Experimental scattershot boson sampling. Sci. Adv. 1, e1400255 (2015).  
15. Carolan, J. et al. On the experimental verification of quantum complexity in linear optics. Nat. Photon. 8, 621-626 (2014).  
16. Spagnolo, N. et al. Experimental validation of photonic boson sampling. Nat. Photon. 8, 615-620 (2014).  
17. Loredo, J. C. et al. Boson sampling with single photon Fock states from a bright solid-state source. Preprint at https://arxiv.org/abs/1603.00054 (2016).  
18. Kwiat, P. G. et al. New high-intensity source of polarization-entangled photon pairs. Phys. Rev. Lett. 75, 4337-4341 (1995).  
19. Pittman, T., Jacobs, B. & Franson, J. Single photons on pseudodemand from stored parametric down-conversion. Phys. Rev. A 66, 042303 (2002).  
20. Kaneda, F. et al. Time-multiplexed heralded single-photon source. Optica 2, 1010-1013 (2015).  
21. Lund, A. P. et al. Boson sampling from a Gaussian state. Phys. Rev. Lett. 113, 100502 (2014).  
22. Lounis, B. & Orrit, M. Single photon sources. Rep. Prog. Phys. 68, 1129-1179 (2005).  
23. Michler, P. et al. A quantum dot single-photon turnstile device. Science 290, 2282-2285 (2000).  
24. Santori, C., Fattal, D., Vuckovic, J., Solomon, G. S. & Yamamoto, Y. Indistinguishable photons from a single photon device. Nature 419, 594-597 (2002).  
25. Tillmann, M. et al. Generalized multiphoton quantum interference. Phys. Rev. X 5, 041015 (2015).  
26. Shchesnovich, V. S. Partial indistinguishability theory of multiphoton experiments in multiport devices. Phys. Rev. A 91, 013844 (2015).  
27. Tichy, M. C. Sampling of partially distinguishable bosons and the relation to multidimensional permanent. Phys. Rev. A 91, 022316 (2015).  
28. He, Y.-M. et al. On-demand semiconductor single-photon source with nearunity indistinguishability. Nat. Nanotech. 8, 213-217 (2013).  
29. Ding, X. et al. On-demand single photons with high extraction efficiency and near-unity indistinguishability from a resonantly driven quantum dot in a micropillar. Phys. Rev. Lett. 116, 020401 (2016).  
30. Somaschi, N. et al. Near-optimal single-photon sources in the solid state. Nat. Photon. 10, 340-345 (2016).

31. Wang, H. et al. Near-transform-limited single photons from an efficient solid-state quantum emitter. Phys. Rev. Lett. 116, 213601 (2016).  
32. Patel, R. B. et al. Two-photon interference of the emission from electrically tunable remote quantum dots. Nat. Photon. 4, 632-635 (2010).  
33. Clements, W. R., Humphreys, P. C., Metcalf, B. J., Kolthammer, W. S. & Walmsley, I. A. An optimal design for universal quantum multiport interferometers. Preprint at https://arxiv.org/abs/1603.08788 (2016).  
34. Aaronson, S. & Arkhipov, A. Boson sampling is far from uniform. Quant. Inf. Comp. 14, 1383-1432 (2014).  
35. Bentivegna, M. et al. Bayesian approach to boson sampling validation. Int. J. Quant. Inf. 12, 1560028 (2014).  
36. Cover, T. M. & Thomas, J. A. Elements of Information Theory (John Wiley & Sons, 2006).  
37. Lita, A. E., Miller, A. J. & Nam, S. W. Counting near-infrared single-photons with  $95\%$  efficiency. Opt. Express 16, 3032-3040 (2008).  
38. Zadeh, I. E. et al. Single-photon detectors combining near unity efficiency, ultrahigh detection-rates, and ultra-high time resolution. Preprint at https://arxiv.org/abs/1611.02726 (2016).  
39. Unsleber, S. et al. Highly indistinguishable on-demand resonance fluorescence photons from a deterministic quantum dot micropillar device with  $74\%$  extraction efficiency. Opt. Express 24, 8539-8546 (2016).  
40. Muller, A. et al. Resonant fluorescence from a coherent driven semiconductor quantum dot in a cavity. Phys. Rev. Lett. 99, 187402 (2007).

# Acknowledgements

We thank S. Aaronson, B. Sanders and P. Rohde for helpful discussions. This work was supported by the National Natural Science Foundation of China, the Chinese Academy of Sciences, the National Fundamental Research Program and the State of Bavaria.

# Author contributions

C.-Y.L. and J.-W.P. conceived and designed the experiment, C.S., M.K. and S.H. grew and fabricated the quantum dot samples. H.W., Y.H., Y.-H.L., Z.-E.S., B.L., H.-L.H., X.D., M.-C.C., C.L., J.Q., J.-P.L., Y.-M.H., C.S., M.K., C.-Z.P., S.H. and C.-Y.L. performed the experiment, S.H., C.-Y. L. and J.-W.P. analysed the experimental data. C.-Y.L. and J.-W.P. wrote the paper.

# Additional information

Supplementary information is available in the online version of the paper. Reprints and permissions information is available online at www.nature.com/reprints. Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. Correspondence and requests for materials should be addressed to C.Y.L. and J.W.P.

# Competing financial interests

The authors declare no competing financial interests.