# Boson Sampling on a Photonic Chip

Justin B. Spring, $^{1}$  Benjamin J. Metcalf, $^{1}$  Peter C. Humphreys, $^{1}$  W. Steven Kolthammer, $^{1}$  Xian-Min Jin, $^{1,2}$  Marco Barbieri, $^{1}$  Animesh Datta, $^{1}$  Nicholas Thomas-Peter, $^{1}$  Nathan K. Langford, $^{1,3}$  Dmytro Kundys, $^{4}$  James C. Gates, $^{4}$  Brian J. Smith, $^{1}$  Peter G. R. Smith, $^{4}$  Ian A. Walmsley $^{1*}$

$^{1}$ Clarendon Laboratory, Department of Physics, University of Oxford, OX1 3PU, UK.  $^{2}$ Department of Physics, Shanghai Jiao Tong University, Shanghai 200240, PR China.  $^{3}$ Department of Physics, Royal Holloway, University of London, TW20 0EX, UK.  $^{4}$ Optoelectronics Research Centre, University of Southampton, Southampton, SO17 1BJ, UK.

*To whom correspondence should be addressed; E-mail: i.walmsley1@physics.ox.ac.uk

While universal quantum computers ideally solve problems such as factoring integers exponentially more efficiently than classical machines, the formidable challenges in building such devices motivate the demonstration of simpler, problem-specific algorithms that still promise a quantum speedup. We construct a quantum boson sampling machine (QBSM) to sample the output distribution resulting from the nonclassical interference of photons in an integrated photonic circuit, a problem thought to be exponentially hard to solve classically. Unlike universal quantum computation, boson sampling merely requires indistinguishable photons, linear state evolution, and detectors. We benchmark our QBSM with three and four photons and analyze sources of sampling inaccuracy. Scaling up to larger devices could offer the first definitive quantum-enhanced computation.

Universal quantum computers require physical systems that are well-isolated from the decohering effects of their environment, while at the same time allowing precise manipulation during computation. They also require qubit-specific state initialization, measurement, and the generation of quantum correlations across the system (1-4). Although there has been substantial progress in proof-of-principle demonstrations of quantum computation (5-8), simultaneously meeting these demands has proven difficult. This motivates the search for schemes that can demonstrate quantum-enhanced computation under more favorable experimental conditions. Investigating the space between classical and universal quantum computers has attracted broad interest (9-11).

Boson sampling has recently been proposed as a specific quantum computation that is more efficient than its classical counterpart but only requires indistinguishable bosons, low decoherence linear evolution, and measurement (12). The distribution of bosons that have undergone a unitary transformation  $U$  is thought to be exponentially hard to sample from classically (12). The probability amplitude of obtaining a certain output is directly proportional to the permanent of a corresponding submatrix of  $U$  (13). The permanent expresses the wavefunction of identical bosons, which are symmetric under exchange (14, 15); in contrast, the Slater determinant expresses the wavefunction of identical fermions, which are antisymmetric under exchange. While determinants can be evaluated efficiently, permanents have long been believed to be hard to compute (16); the best known algorithm scales exponentially with the size of the matrix.

One can envision a race between a classical and a quantum machine to sample the boson distribution given an input state and  $U$ . The classical machine would evaluate at least part of the probability distribution, which requires the computation of matrix permanents. An ideal QBSM instead creates indistinguishable bosons, physically implements  $U$ , and records the outputs. While the QBSM is not believed to efficiently estimate any individual matrix permanent, for a sufficiently large system it

is expected to beat the classical computer in sampling over the entire distribution (12).

Photonics is a natural platform to implement boson sampling since sources of indistinguishable photons are well-developed (17), and integrated optics offers a scalable route to low decoherence linear transformations over many modes (18). Such circuits can be rapidly reconfigured to sample from a user-defined operation (19, 20). Importantly, boson sampling requires neither nonlinearities nor on-demand entanglement, unlike photonic approaches to universal quantum computation (21). This clears the way for experimental boson sampling with existing photonic technology, building on the extensively studied two-photon Hong-Ou-Mandel (HOM) interference effect (22).

A QBSM (Fig. 1) samples the output distribution of a multi-particle bosonic quantum state  $|\Psi_{\mathrm{out}}\rangle$ , prepared from a specified initial state  $|\mathbf{T}\rangle$  and linear transformation  $\Lambda$ . Unavoidable losses in the system imply  $\Lambda$  will not be unitary, though lossy QBSMs can still surpass classical computation (12, 23). A trial begins with the input state

$\left|\mathbf{T}\right\rangle = \left|T_{1}\dots T_{M}\right\rangle \propto \Pi_{i = 1}^{M}\left(\hat{a}_{i}^{\dagger}\right)^{T_{i}}\left|0\right\rangle$  , which describes  $N = \sum_{i = 1}^{M}T_{i}$  particles distributed in  $M$  input modes in the occupation-number representation. The output state  $|\Psi_{\mathrm{out}}\rangle$  is generated according to the linear map between input and output mode creation operators  $\hat{a}_i^\dagger = \sum_{j = 1}^{M}\Lambda_{ij}\hat{b}_j^\dagger$  , where  $\pmb{\Lambda}$  is an  $M\times M$  matrix. Finally, the particles in each of the  $M$  output modes are counted. The probability of a particular measurement outcome  $|\mathbf{S}\rangle =$ $|S_{1}\ldots S_{M}\rangle$  is given by

$$
P (\mathbf {S} \mid \mathbf {T}) = \left| \left\langle \mathbf {S} \mid \Psi_ {\text {o u t}} \right\rangle \right| ^ {2} = \frac {\left| \operatorname {P e r} \left(\boldsymbol {\Lambda} ^ {(\mathrm {S} , \mathrm {T})}\right) \right| ^ {2}}{\prod_ {j = 1} ^ {M} S _ {j} ! \prod_ {i = 1} ^ {M} T _ {i} !} \tag {1}
$$

where the  $N\times N$

submatrix  $\mathbf{\Lambda}^{(\mathbf{s},\mathbf{t})}$  is obtained by keeping  $S_{j}(T_{i})$  copies of the  $j^{th}$  column  $(i^{th}$  row) of  $\pmb{\Lambda}$  (13).

Our QBSM consists of sources of indistinguishable single photons, a multiport linear optical circuit, and single-photon counting detectors. Two parametric down-conversion (PDC) pair sources (24) are used to inject up to four photons into a silica-on-silicon integrated photonic circuit, fabricated by UV writing (19, 25). The circuit is shown in Fig. 2A and consists of  $M = 6$  input and output spatial modes coupled by a network of ten beam splitters (18). The output state is measured with single-photon avalanche photodiodes on each mode. We only consider outcomes in which the number of detections equals the intended number of input photons (13).

Our central result of three- and four-boson sampling is shown in Fig. 3. In the first case, we repeatedly inject three photons in the input state  $|\mathbf{T}\rangle = |011010\rangle$ , monitor all outputs, and collect all three-fold coincident events. In the four-photon experiment, we use the input  $|\mathbf{T}\rangle = |202000\rangle$  and record all four-fold events (26). For each experiment, the measured relative frequencies  $P_{s}^{\mathrm{exp}}$  for every allowed outcome  $|\mathbf{S}\rangle$  are shown along with their observed statistical variation. The corresponding theoretical  $P_{s}^{\mathrm{th}}$ , calculated using the right-hand side of Eq. 1, are shown along with

their uncertainties arising from the characterization of  $\Lambda$ , described below.

We reconstruct  $\Lambda$  with a series of one- and two-photon transmission measurements to determine its complex-valued elements  $\Lambda_{ij} = \tau_{ij}e^{i\phi_{ij}}$  (27). The characterization results for the circuit used in the three-photon experiment are shown in Fig. 2, B and C. To obtain the magnitude  $\tau_{ij}$ , single photons are injected in mode  $i$ . The probability of a subsequent detection in mode  $j$  is given by  $P_{1}(j,i) = |\Lambda_{ij}|^{2} = \tau_{ij}^{2}$ . The phases  $_{ij}$  are determined from two-photon quantum interference measurements. The probability that a photon is detected in each of modes  $j_{1}$  and  $j_{2}$  when they are injected in modes  $i_{b}$  and  $i_{2}$  is given by  $P_{2}(j_{1},j_{2},i_{1},i_{2}) = |\Lambda_{i_{1}j_{1}}\Lambda_{i_{2}j_{2}} + \Lambda_{i_{2}j_{1}}\Lambda_{i_{1}j_{2}}|^{2}$ . This expression is used to find the relevant phases  $_{ij}$  given the previously determined magnitudes  $\tau_{ij}$  (13).

To analyze the performance of our QBSM we compare our results to an ideal machine. We quantify the match of two sets of relative frequencies  $\mathbf{P}^{(1)}$  and  $\mathbf{P}^{(2)}$  by calculating the  $L_{1}$  distance  $d^{(N)}\left(\mathbf{P}^{(1)},\mathbf{P}^{(2)}\right) = \frac{1}{2}\sum_{S}\left|P_{S}^{(1)} - P_{S}^{(2)}\right|$ , where  $N$  denotes the number of photons in a sample (28). Identical and maximally dissimilar distributions correspond to  $d = 0$  and  $d = 1$ , respectively. For our experiments we calculate  $d^{(N)}(\mathbf{P}^{\mathrm{exp}},\mathbf{P}^{\mathrm{th}})$  to give  $d^{(3)} = 0.094 \pm 0.014$  and  $d^{(4)} = 0.097 \pm 0.004$  (Fig. 3). Even in an ideal QBSM with perfect state preparation and detection, the statistical variations result in nonzero  $d$ . If we substitute for our experimental data a Monte Carlo sampling of  $\mathbf{P}^{\mathrm{th}}$  with sample size equivalent to our experiments, we instead calculate  $d^{(3)} = 0.043 \pm 0.012$  and  $d^{(4)} = 0.059 \pm 0.022$ . This suggests there are appreciable contributions to  $d(\mathbf{P}^{\mathrm{exp}},\mathbf{P}^{\mathrm{th}})$  beyond statistical deviation.

Due to experimental limitations, our QBSM occasionally samples distributions other than  $\mathbf{P}^{\mathrm{th}}$ . The dominant sources of this sampling inaccuracy in our experiment are multi-photon emission and partial distinguishability amongst the photons. In practice, all single-photon sources produce multiple photons with a finite probability (17). For our PDC sources, the output state is approximately  $|00\rangle + \lambda |11\rangle + \lambda^2 |22\rangle$ , with  $\lambda << 1$ . Both single-photon and undesired multiphoton terms increase with  $\lambda$ . In our three-photon experiments, for example, multiphoton emission from the two PDC sources can lead to input states  $|\mathbf{T}\rangle = |021010\rangle$  or  $|012020\rangle$ , which contribute to three-fold coincident events if photons are lost or emerge in the same output mode. In addition, partial distinguishability of the photons contaminates the distribution sampled by the QBSM by mixing in one- and two-photon interference effects (29).

We form a new distribution  $\mathbf{P}^{\mathrm{mod}}$  that accounts for the effects of multiphoton emission and photon distinguishability (13). The distance  $d(\mathbf{P}^{\mathrm{exp}},\mathbf{P}^{\mathrm{mod}})$  shown by the green point (insets of Fig. 4, A and B), is found to be consistent with the statistical variation due to a finite sample size, for both the three- and four-photon experiments. This suggests we have correctly identified and modeled the sources of inaccuracy. To investigate how the performance of our QBSM depends on  $\lambda$  and photon distinguishability, we calculate  $d(\mathbf{P}^{\mathrm{mod}},\mathbf{P}^{\mathrm{th}})$  for a range of operating parameters (Fig. 4, C and D). In terms of  $\lambda$ , a clear tradeoff is presented between data rate and inaccuracy due to multiphoton emission, which is an intrinsic consequence of using PDC sources. Improvement in photon indistinguishability increases the fidelity to the ideal machine, and additionally is thought to enhance the computational power of a QBSM (29).

Our results demonstrate that boson sampling is related to the computation of matrix permanents, a problem believed to be classically hard. Our successful diagnosis of the source and magnitude of the principal sampling errors, as validated by a reduction in  $d(\mathbf{P}^{\mathrm{exp}},\mathbf{P}^{\mathrm{mod}})$  to within the statistical variation of a perfect QBSM, will inform the design of next-generation devices. While investigations into quantum-enhanced computation in the presence of errors is ongoing, it already appears that the boson sampling model makes less stringent demands on device performance than universal photonic quantum computers (12, 23, 29). There is thus reason for optimism that ongoing advances in integrated photonics

such as reduced transmission loss, efficient number-resolving detectors (30), and multiplexed (31, 32) or single-emitter (17) photon sources, will enable larger QBSMs that outperform classical computers. Beyond the specific boson sampling problem, such a device would provide clear evidence for the computational power of quantum mechanics.

# References and Notes

1. D. P. DiVincenzo, The Physical Implementation of Quantum Computation. Fortschr. Phys. 48, 771 (2000). doi:10.1002/1521-3978(200009)48:9/11<771::AID-PROP771>3.0.CO;2-E  
2. R. Raussendorf, H. J. Briiegel, A one-way quantum computer. Phys. Rev. Lett. 86, 5188 (2001). doi:10.1103/PhysRevLett.86.5188 Medline  
3. M. A. Nielsen, Quantum computation by measurement and quantum memory. Phys. Lett. A 308, 96 (2003). doi:10.1016/S0375-9601(02)01803-0  
4. A. M. Childs, Universal computation by quantum walk. Phys. Rev. Lett. 102, 180501 (2009). doi:10.1103/PhysRevLett.102.180501 Medline  
5. P. Walther et al., Experimental one-way quantum computing. Nature 434, 169 (2005). doi:10.1038/nature03347 Medline  
6. C.-Y. Lu, D. E. Browne, T. Yang, J.-W. Pan, Demonstration of a compiled version of Shor's quantum factoring algorithm using photonic qubits. Phys. Rev. Lett. 99, 250504 (2007). doi:10.1103/PhysRevLett.99.250504 Medline  
7. B. P. Lanyon et al., Universal digital quantum simulation with trapped ions. Science 334, 57 (2011). doi:10.1126/science.1208001 Medline  
8. E. Lucero et al., Computing prime factors with a Josephson phase qubit quantum processor. Nat. Phys. 8, 719 (2012). doi:10.1038/nphys2385  
9. E. Knill, R. Laflamme, Power of One Bit of Quantum Information. Phys. Rev. Lett. 81, 5672 (1998). doi:10.1103/PhysRevLett.81.5672  
10. S. P. Jordan, Quant. Inf. Comput. 10, 470 (2010).  
11. D. Shepherd, M. J. Bremner, Temporally unstructured quantum computation. Proc. R. Soc. Ser. A 465, 1413 (2009). doi:10.1098/rspa.2008.0443  
12. S. Aaronson, A. Arkhipov, Proceedings of ACM Symposium on the Theory of Computing, STOC (2011).  
13. Materials and methods are available as supplementary material on Science Online.  
14. E. Caianiello, On quantum field theory — I: explicit solution of Dyson's equation in electrodynamics without use of feynman graphs. Nuovo Cim. 10, 1634 (1953). doi:10.1007/BF02781659  
15. L. Troyansky, N. Tishby, Proceedings of PhysComp (1996).  
16. L. G. Valiant, The complexity of computing the permanent. Theor. Comput. Sci. 8, 189 (1979). doi:10.1016/0304-3975(79)90044-6  
17. M. D. Eisaman, J. Fan, A. Migdall, S. V. Polyakov, Invited review article: Single-photon sources and detectors. Rev. Sci. Instrum. 82, 071101 (2011). doi:10.1063/1.3610677 Medline  
18. B. J. Metcalf et al., arXiv:1208.4575v2 (2012).  
19. B. J. Smith, D. Kundys, N. Thomas-Peter, P. G. R. Smith, I. A. Walmsley, Opt. Express 17, 264 (2009).  
20. P. J. Shadbolt et al., Generating, manipulating and measuring entanglement and mixture with a reconfigurable photonic circuit. Nat. Photonics 6, 45 (2011). doi:10.1038/nphoton.2011.283  
21. E. Knill, R. Laflamme, G. J. Milburn, A scheme for efficient quantum computation with linear optics. Nature 409, 46 (2001). doi:10.1038/35051009 Medline  
22. C. K. Hong, Z. Y. Ou, L. Mandel, Measurement of subpicosecond time intervals between two photons by interference. Phys. Rev. Lett. 59, 2044 (1987). doi:10.1103/PhysRevLett.59.2044 Medline  
23. P. P. Rohde, T. C. Ralph, Error tolerance of the boson-sampling model for linear optics quantum computing. Phys. Rev. A 85, 022332 (2012). doi:10.1103/PhysRevA.85.022332  
24. P. J. Mosley et al., Heralded generation of ultrafast single photons in pure quantum States. Phys. Rev. Lett. 100, 133601 (2008). doi:10.1103/PhysRevLett.100.133601 Medline  
25. D. O. Kundys, J. C. Gates, S. Dasgupta, C. Gawith, P. G. R. Smith, Use of Cross-Couplers to Decrease Size of UV Written Photonic Circuits. IEEE Photon. Technol. Lett. 21, 947 (2009). doi:10.1109/LPT.2009.2021071  
26. Eq. 1 is expected to hold for any  $|\mathbf{S}\rangle$  and  $|\mathbf{T}\rangle$ , however the classical hardness of sampling  $P(\mathbf{S}|\mathbf{T})$  is maximized when  $S_{j}, T_{i} \in \{0,1\}$  for a given  $N$  and  $\Lambda$ .  
27. A. Laing, J. L. O'Brien, arXiv:1208.2868v1 (2012).  
28. A. Gilchrist, N. K. Langford, M. A. Nielsen, Distance measures to compare real and ideal quantum processes. Phys. Rev. A 71, 062310 (2005).

doi:10.1103/PhysRevA.71.062310  
29. P. P. Rohde, Optical quantum computing with photons of arbitrarily low fidelity and purity. Phys. Rev. A 86, 052321 (2012). doi:10.1103/PhysRevA.86.052321  
30. T. Gerrits et al., On-chip, photon-number-resolving, telecommunication-band detectors for scalable photonic information processing. Phys. Rev. A 84, 060301 (2011). doi:10.1103/PhysRevA.84.060301  
31. A. L. Migdall, D. Branning, S. Castelletto, Tailoring single-photon and multiphoton probabilities of a single-photon on-demand source. Phys. Rev. A 66, 053805 (2002). doi:10.1103/PhysRevA.66.053805  
32. J. Nunn et al., arXiv:1208.1534v1 (2012).  
33. S. Rahimi-Keshari et al., arXiv:1210.6463v1 (2012).  
34. S. Scheel, arXiv:0406127v1 (2004).  
35. N. Thomas-Peter et al., Integrated photonic sensing. New J. Phys. 13, 055024 (2011). doi:10.1088/1367-2630/13/5/055024  
36. M. A. Nielsen, I. L. Chuang, Quantum Computation and Quantum Information (Cambridge Series on Information and the Natural Sciences) (Cambridge University Press, 2004).  
37. B. J. Smith, P. Mahou, O. Cohen, J. S. Lundeen, I. A. Walmsley, Photon pair generation in birefringent optical fibers. Opt. Express 17, 23589 (2009). doi:10.1364/OE.17.023589 Medline  
Acknowledgments: We thank Josh Nunn for valuable insights. This work was supported by the EPSRC (EP/C013840/1), the EC project Q-ESSENCE (248095), the Royal Society, and the AFOSR EOARD. XMJ is supported by an EU Marie-Curie Fellowship (PIIF-GA-2011-300820). JS acknowledges support from the United States Air Force Institute of Technology. The views expressed in this article are those of the authors and do not reflect the official policy or position of the United States Air Force, Department of Defense, or the U.S. Government.

Supplementary Materials

www.sciencemag.org/cgi/content/full/science.1231692/DC1

Materials and Methods

Supplementary Text

References (33-37)

18 October 2012; accepted 03 December 2012

Published online 20 December 2012

10.1126/science.1231692

![](images/bf0b294e37bddb6241df72f299ffe9ef47bb756b8b594895ba2e56d7ab4ff630.jpg)  
Fig. 1. Model of quantum boson sampling. Given a specified initial number state  $|\mathbf{T}\rangle = |T_1\dots T_M\rangle$  and linear transformation  $\pmb{\Lambda}$ , a quantum boson sampling machine efficiently samples from the distribution  $P(\mathbf{S}|\mathbf{T})$  of possible outcomes  $|\mathbf{S}\rangle = |S_{1}\dots S_{M}\rangle$ .

![](images/54798a428d13216808081facf33bcb2f29e2470e8dbe9d731027f57d354299ab.jpg)  
Fig. 2. Schematic and characterization of the photonic circuit. (A) The silica-on-silicon waveguide circuits consist of  $M = 6$  accessible spatial modes (labeled 1-6). For the three-photon experiment, we launch photons into inputs  $i = 2, 3$  and 5 from two parametric down-conversion sources which produce near-single photons and postselect outcomes in which three detections are registered amongst the output modes  $j$ . For the four-photon experiment, which is implemented on a different chip of identical geometry, we inject a double photon pair from a single source into the modes  $i = 1, 3$  and postselect on four detection events. (B-C) Measured elements of the linear transformation  $\Lambda_{ij} = \tau_{ij} e^{i\phi_{ij}}$  linking the input mode  $i$  to the output mode  $j$  of our three-photon apparatus. The circuit geometry dictates that several  $\tau_{ij}$  are zero, and our phase-insensitive input states and detection methods imply only six nonzero  $i_j$ . Since only relative values are needed due to post-selection, we rescale each row of  $\tau$  so that its maximum value is unity.

![](images/6f021d1f445cb94fd1cb2846f47ca72e4148ba3fe1e01efacb5eaa7eb8d1a724.jpg)  
Fig. 3. Boson sampling results. The measured relative frequencies  $\mathbf{P}^{\mathrm{exp}}$  of outcomes in which the photons are detected in distinct modes are shown in red for (A) three- and (B) four-photon experiments. Each data set is collected over 160 hours, and statistical variations in counts are shown by the red shaded bars. The theoretical distributions  $\mathbf{P}^{\mathrm{th}}$  (blue) are obtained from the permanents of submatrices constructed from the full transformation  $\Lambda$ , as depicted in the inset. The blue error bars arise from uncertainties in the characterization of  $\Lambda$ .

![](images/6f6d7ec061f53256163784dfb894e014a583c89ebb7d8e5f44bbf73dbe3a0006.jpg)

![](images/43145d290b648ffa55f28c545b5d4a1ffbfbd3d595e893a399619ca05ddb833c.jpg)

![](images/1c96140c8c21314af47d1ef8f5ee8d760e4d9861f6774d853e9516a28c34ff4e.jpg)  
Fig. 4. Sampling accuracy. We consider several boson distributions: the experimental samples  $\mathbf{P}^{\mathrm{exp}}$ , the ideal predictions of the matrix permanent  $\mathbf{P}^{\mathrm{th}}$ , and the predictions of the full model  $\mathbf{P}^{\mathrm{mod}}$  that includes higher-order emission and photon distinguishability. (A) The  $L_{1}$  distance  $d$  between  $\mathbf{P}^{\mathrm{th}}$  and a Monte Carlo simulation of an ideal machine that samples  $\mathbf{P}^{\mathrm{th}}$  a finite number of times for our three- and (B) four-photon cases. The errors in this case are solely a result of the finite number of samples collected by the ideal machine. The inset histograms show the variation in  $d$  expected for a sample size corresponding to the 1421 and 405 counts collected in our three- and four-photon experiments. The distance  $d(\mathbf{P}^{\mathrm{exp}}, \mathbf{P}^{\mathrm{th}})$  (red) suggests an underlying systematic inaccuracy as it falls outside the range of outputs of an ideal machine indicated in the histogram. Our full model is validated by the distance  $d(\mathbf{P}^{\mathrm{exp}}, \mathbf{P}^{\mathrm{mod}})$  (green) which is consistent with statistical variation. The red and green dot positions correspond to the  $L_{1}$  axis only. (C) The predicted variation in  $d(\mathbf{P}^{\mathrm{th}}, \mathbf{P}^{\mathrm{mod}})$  is shown as a function of  $\lambda$  and the photon distinguishabilities, represented by the reduction in two-photon interference visibility  $V$ , for the three- and (D) four-photon cases. Our experimental conditions are marked (red dot).

![](images/708a866e664af371c0cf533a650efb24c78e92d2d858b92eb2792dadfb074c1c.jpg)

![](images/ed54277941f59e2323c7d2105d36ad53964360b2a3594a53c08957b77efc70ec.jpg)