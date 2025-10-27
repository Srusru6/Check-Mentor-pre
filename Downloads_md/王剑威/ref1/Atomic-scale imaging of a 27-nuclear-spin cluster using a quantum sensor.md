# Atomic-scale imaging of a 27-nuclear-spin cluster using a quantum sensor

https://doi.org/10.1038/s41586-019-1834-7

Received: 10 May 2019

Accepted: 6 September 2019

Published online: 18 December 2019

M. H. Abobeih $^{1,2}$ , J. Randall $^{1,2}$ , C. E. Bradley $^{1,2}$ , H. P. Bartling $^{1,2}$ , M. A. Bakker $^{1,2}$ , M. J. Degen $^{1,2}$ , M. Markham $^{3}$ , D. J. Twitchen $^{3}$  & T. H. Taminiau $^{1,2*}$

Nuclear magnetic resonance (NMR) is a powerful method for determining the structure of molecules and proteins<sup>1</sup>. Whereas conventional NMR requires averaging over large ensembles, recent progress with single-spin quantum sensors<sup>2-9</sup> has created the prospect of magnetic imaging of individual molecules<sup>10-13</sup>. As an initial step towards this goal, isolated nuclear spins and spin pairs have been mapped<sup>14-21</sup>. However, large clusters of interacting spins—such as those found in molecules—result in highly complex spectra. Imaging these complex systems is challenging because it requires high spectral resolution and efficient spatial reconstruction with sub-angstrom precision. Here we realize such atomic-scale imaging using a single nitrogen vacancy centre as a quantum sensor, and demonstrate it on a model system of 27 coupled<sup>13</sup>C nuclear spins in diamond. We present a multidimensional spectroscopy method that isolates individual nuclear–nuclear spin interactions with high spectral resolution (less than 80 millihertz) and high accuracy (2 millihertz). We show that these interactions encode the composition and inter-connectivity of the cluster, and develop methods to extract the three-dimensional structure of the cluster with sub-angstrom resolution. Our results demonstrate a key capability towards magnetic imaging of individual molecules and other complex spin systems<sup>9-13</sup>.

The nitrogen vacancy (NV) centre in diamond has emerged as a powerful quantum sensor $^{2-13,22,23}$ . The NV electron spin provides long coherence times $^{5,6,20}$  and high-contrast optical readout $^{5,24,25}$ , enabling high sensitivity over a large range of temperatures $^{5,6,20,25,26}$ . Pioneering experiments with near-surface NV centres have demonstrated spectroscopy of small ensembles of nuclear spins in nanoscale volumes $^{2,3,5-8}$  and electron-spin-labelled proteins $^{4}$ . Furthermore, single-nuclear-spin sensitivity has been demonstrated, and isolated individual nuclear spins and spin pairs have been mapped $^{14-21}$ . Together, these results have established the NV centre as a promising platform for magnetic imaging of complex spin systems and single molecules $^{10-13}$ .

Here, we realize a key step towards that goal: the three-dimensional (3D) imaging of large nuclear-spin structures with atomic resolution. The main idea behind our method is to obtain structural information by accessing the couplings between individual nuclear spins. Our approach has three key elements: (1) realizing high spectral resolution so that small couplings can be accessed, (2) isolating such couplings from complex spectra, and (3) transforming the revealed connectivity into a 3D spatial structure with sub-ångström precision.

The basic elements of our experiment are illustrated in Fig. 1a. We consider a cluster of  $^{13}\mathrm{C}$  nuclear spins in the vicinity of a single NV centre in diamond at  $4\mathrm{K}$ . This cluster provides a model system for the magnetic imaging of single molecules and spin structures external to the diamond. Each  $^{13}\mathrm{C}$  spin has a shifted frequency owing to the hyperfine interaction with the electron spin, resembling a chemical shift in traditional  $\mathsf{NMR}^{1,27}$ . These shifts allow us to distinguish different nuclear spins in the cluster.

We use the NV electron spin as a sensor to probe nuclear-nuclear interactions (Fig. 1b). Inspired by NMR spectroscopy $^{1,27}$ , we develop sequences that employ spin-echo double-resonance techniques to isolate and measure individual couplings with high spectral resolution. First, we polarize a nuclear 'probe' spin (frequency RF1) using recently developed quantum sensing sequences that can detect spins in any direction from the NV, enabling access to a large number of spins (see Methods) $^{28}$ . Second, we let this probe spin evolve for a time  $t$  and apply  $N$  echo pulses that decouple it from the other spins and from environmental noise. Simultaneously, pulses on a 'target' spin in the cluster (frequency RF2) re-couple it to the probe spin, selecting the interaction between these two spins. Finally, a second sensing sequence detects the resulting polarization of the probe spin through high-contrast readout of the electron spin (see Methods), which enables fast data collection. This double-resonance sequence provides a high spectral resolution through a long nuclear phase accumulation time. Importantly, the resolution is not limited by the relatively short coherence time of the electron-spin sensor (see Methods) $^{24,29}$ .

It is instructive to first consider the case without echo pulses  $(N = 0)$ . In such a Ramsey-type measurement $^{24-26,29,30}$ , all couplings act simultaneously. This results in complex spectra that indicate the presence of multiple spins and many nuclear-nuclear spin interactions in the cluster (Fig. 1c). However, this one-dimensional (1D) measurement gives no direct information on the connectivity between spins. Additionally, the underlying structure of individual spins and couplings is obscured by the many frequencies  $(2^j$  for coupling to  $j$  spins) and by

![](images/1b23f0fad93567fdebe5e2a49bbe6370e23555f073369494d33dcaf495ba573f.jpg)  
a

![](images/9f5e3ab4b49cf3d2357b1578e5754a1a3cd90c210cdd1f132492aad6fa35706a.jpg)  
b

![](images/a8360dce0a661bd8956eb2c1333784a18a6583057a5a074ce82d1009057e2aad.jpg)  
C

![](images/2a6ca4eb2699d64965eca0702a9e9e4abf5d1f84a917ba71fc077b138e2be07a.jpg)  
d

![](images/00df5f47e942609929d2df6bd98eeda4ac089869e71e1caf01b1efba5bc1bc03.jpg)  
e

![](images/a5836cea0e761c4b8532774e88405cd715a9f836c85d81d8c7cc4ca43734303a.jpg)  
f

![](images/d6f4d9d47286ee1d21d1d25957fe96ddaeb4e2ab395338052701a70ca47c0778.jpg)  
Fig.1|Basic concepts of the experiment.a, We consider an individual cluster of  $^{13}\mathrm{C}$  nuclear spins near a single NV centre in diamond. To obtain the 3D structure of the cluster we use the NV electron spin as a quantum sensor to measure nuclear-nuclear spin couplings. b, Experimental sequence. The NV sensor is used to polarize and detect the probe'spin(s) at frequency RF1 (see Methods). A double-resonance sequence of N echo pulses is applied simultaneously on the probe spin(s) (RF1) and the target'spin(s) (RF2), so that the coupling between these spins is selectively detected. See Extended Data Fig. 1 for the detailed sequence. c, A Ramsey signal  $(N = 0)$  for a nuclear spin in the cluster (detuning  $f_{0} = 5\mathrm{kHz}$  relative to  $\mathrm{RF1} = 455.37\mathrm{kHz})$  . Because all couplings are probed simultaneously, the power spectral density (PSD) yields a complex non-resolvable spectrum. See Extended Data Fig. 2 for more

![](images/c05668e477cb0a2732d4eddc8dc60f2a720ee54df81aaf8b40de5da2a62d6765.jpg)

![](images/ed23ea3f8bd28a0dc10925be17bcac71d7445830b9c530c38a18347c0c15f2da.jpg)  
examples. d, Double-resonance spectroscopy  $(N = 1)$ . Sweeping the target frequency (RF2) reveals all spins that couple to the probe spin(s). For larger  $t$ , more peaks appear as weaker couplings become visible. Here, RF1 = 463.27 kHz. e, Sweeping the evolution time  $t$  for a fixed RF1 and RF2 reveals the coupling strength between spins. This example reveals a 235.96(1) Hz coupling between two spins with a spectral resolution of 1.807(7) Hz FWHM. Here, RF1 = 463.27 kHz and RF2 = 455.37 kHz. f, An example with  $N = 256$  echo pulses showing a coherence time of 10.9(5) s, which enables selective measurements of sub-hertz couplings with high spectral resolution (78(1) mHz) and precision (2 mHz). Here, RF1 = 408.32 kHz and RF2 = 413.48 kHz. See Methods for the fit functions of all graphs. Error bars are one standard deviation. a.u., arbitrary units.

![](images/c97e87d43c133c6aea697e1fac7cc89e8b5a533b59a66ebc0761c7cf117b0026.jpg)

the low spectral resolution of  $>30\mathrm{Hz}$  full-width at half-maximum (FWHM), which is set by the dipolar-broadened linewidth of the nuclear spins and is inversely proportional to the dephasing time,  $T_{2}^{*}$ .

By contrast, our double-resonance sequence enables couplings between specific spins to be isolated and measured with high resolution. We first scan the target frequency RF2 for a fixed probe frequency RF1 (Fig. 1d). This reveals the spectral positions of nuclear spins coupled to the probe spin. We then sweep the evolution time  $t$  and apply a Fourier transform to the signal to quantify the coupling strengths (Fig. 1e). For a single pulse ( $N = 1$ ), the nuclear-spin coherence time is  $T_{2} = 0.58(2)$  s (all given uncertainties are one standard deviation), yielding a spectral resolution of 1.807(7) Hz and a centre frequency accuracy of 10 mHz. The spectral resolution is set by the coherence of the sample spins and can be further enhanced by applying more echo pulses. For  $N = 256$ , a resolution of 78(1) mHz and an accuracy of 2 mHz are obtained, making it possible to detect sub-hertz interactions (Fig. 1f). The obtained resolution is improved by a factor about  $10^{3}$  compared with Ramsey-type spectroscopy on the same type of sample (Fig. 1c) $^{18-21,24,26,29}$  and is an order of magnitude higher than that achieved in previous experiments on other spin samples $^{6-8,25,30,31}$ .

To characterize the entire cluster, we perform 3D spectroscopy by varying the probe frequency RF1, the target frequency RF2 and the evolution time  $t$ . The combinations of RF1 and RF2 reveal the spectral positions of the spins in the cluster. The coupling between spins is

retrieved from the Fourier transform along the time dimension  $t$ . This yields a 3D dataset that in principle encodes the composition and connectivity of the spin cluster (Fig. 2).

In general, multiple spins can have (near-) identical precession frequencies. This has two consequences. First, the echo pulses will invert these spins simultaneously, so that multiple couplings are probed at the same time. Figure 3a shows an example with one probe spin and three target spins. This example illustrates that, although the resulting spectra are more complex, the high spectral resolution of our method enables retrieval of the underlying nuclear-nuclear couplings, even when several spins overlap spectrally.

Second, to determine the number of spins in the cluster and to assign the measured couplings to them, we need to resolve the ambiguity introduced by the fact that multiple spins can overlap spectrally. For example, the observation of a coupling between frequencies  $\{\mathrm{RF1},\mathrm{RF2}\} = \{f_{\mathrm{a}},f_{\mathrm{c}}\}$  and a coupling between frequencies  $\{f_{\mathrm{b}},f_{\mathrm{c}}\}$  is by itself not enough to determine if there are one or two spins with frequency  $f_{\mathrm{c}}$ . Our method resolves such ambiguities by extracting an over-determined dataset with many couplings that together constrain the problem. This enables individual spins to be uniquely identified from their connections to the rest of the cluster (see Fig. 3b for an example).

Transforming the 3D spectra into a spatial structure requires a precise relation between the measured couplings and the relative positions

![](images/3ecc6bc9a6f5c63ea71f7b445cae5bc02c2e9b90a2c2cfb59ad1eaa01c99c278.jpg)  
Fig. 2 | 3D spectroscopy. By varying the probe frequency RF1, the target frequency RF2 and the evolution time  $t$ , we obtain a 3D dataset that encodes the composition of the spins in the cluster and their couplings. The observation of a signal at {RF1, RF2} indicates the presence of one or more spins at both frequencies and a coupling between them. The Fourier transform along the time dimension  $t$  reveals the spin-spin coupling strengths. Examples for three different RF1 values are shown.

of the spins. A complication is that the presence of electronic spins can modify the nuclear couplings $^{32}$ , causing the measured value to deviate from a basic dipole-dipole coupling. We use perturbation theory to derive a set of many-body corrections that depend on the electron-nuclear and nuclear-nuclear couplings and on the magnetic-field direction (see Methods). For the type of cluster considered here, the corrections could be non-negligible. However, the signs of the leading terms depend on the electron spin state. By averaging the measured couplings for the  $m_{s} = +1$  and  $m_{s} = -1$  states ( $m_{s}$ , spin projection), the deviations are strongly reduced. Together with the use of a novel method to align the magnetic field along the NV axis to within  $0.07^{\circ}$  (see Methods), this enables us to approximate the nuclear-nuclear couplings as dipolar.

Finally, we determine the structure of the spin cluster. Figure 4a summarizes all extracted couplings. We identify  $M = 27$  nuclear spins and retrieve 171 pairwise couplings out of the total of  $M(M - 1) / 2 = 351$  couplings. The structure of the cluster is fully described by  $3M - 4 = 77$  spatial coordinates (see Methods), so the problem is over-determined. However, owing to the large number of parameters and local minima, a direct least-squares minimization<sup>10</sup> is challenging. Instead, we build the structure sequentially by progressively adding spins while keeping track of all possible structures that match the measured couplings within a certain tolerance.

We use two different methods. The first method constrains the spin coordinates to the diamond lattice. The second method discretizes space in a general cubic lattice, with voxel spacing as low as  $5 \times 10^{-3} \mathrm{~nm}$  (about 1/70 of the lattice constant; see Methods). Although this second method is more computationally intensive, it uses minimum a priori knowledge and can be applied to arbitrary spin systems. We run these analyses in parallel with the measurements, so that sets of the most

![](images/314cd93d881aa67b41b6c77e885d899cef3172dc8823027d530267f6ea3b6d1f.jpg)

![](images/bad6ac6c02744e358b9ce0e10c7a281cf7cd3cf1c7aa6354235c5ffa780f5e10.jpg)  
Fig. 3 | Spectrally overlapping spins. a, Retrieving couplings when multiple spins are re-coupled simultaneously. Example in which the echo pulses invert three target spins (quadruple resonance). The PSD reveals a complex, yet resolvable, spectrum. Red lines indicate the eight frequencies  $f = \pm f_{1} \pm f_{2} \pm f_{3}$ , where  $f_{1} = 17.17(2) \, \text{Hz}, f_{2} = 7.05(3) \, \text{Hz}$  and  $f_{3} = 3.21(4) \, \text{Hz}$  are the extracted couplings of the probe spin to three target spins. Grey dotted (dot-dashed) lines mark additional frequency components that appear owing to failures to invert one (two) of the target spins (see Supplementary Fig. 1 for detailed analysis). b, Overcoming ambiguity in identifying spins and assigning couplings. Shown is an example from the data. Spins C2, C3, C6, C14, C15 and C18 all yield a coupling signal to the same RF2 frequency. Because the couplings between these six spins reveal that they are part of two spatially separated sub-clusters, it follows that the signals at RF2 must originate from two distinct spins (C24 and C27).

promising spin assignments and structures are regularly created. These yield predictions for which unmeasured couplings (combinations of RF1 and RF2) are required to choose between different assignments and structures, which we use to guide the experiments and reduce the total measurement time (see Methods).

Figure 4b shows the structure obtained for the 27 spins using the diamond lattice. The blue lines show the strongest couplings  $(>3\mathrm{Hz})$  and visualize the inter-connectivity of the cluster. The cubic-lattice method yields a nearly identical structure (see Methods); the average distance between the spin positions for the two solutions is  $0.58\AA$ , a fraction of the bond length of about  $1.54\AA$ . As a final step, we use these structures as inputs for least-squares minimization, where the  $x,y,z$  coordinates are allowed to relax to any value. The solution obtained lies close to the initial guess, with an average distance of  $0.46\AA$ . The uncertainties for the spatial coordinates  $(\delta x,\delta y,\delta z)$  are below one diamond bond length for all 27 spins (Fig. 4c, d), indicating atomic-scale imaging of the complete 27-spin cluster.

Additionally, we determine the position of the NV sensor relative to the cluster. Although not required to reconstruct the cluster, this provides a control experiment. We measure the coupling of the  $^{14}\mathrm{N}$  nuclear spin to 12 of the  $^{13}\mathrm{C}$  spins (Extended Data Fig. 4). This unambiguously determines the location of both the  $^{14}\mathrm{N}$  atom and the vacancy (fit uncertainties  $< 0.3\AA$ ). We can now compare the electron-  $^{13}\mathrm{C}$  hyperfine couplings to previous density functional theory (DFT) calculations for 5 of our spins<sup>33</sup>. All 5 couplings agree with the DFT calculations (Extended Data Fig. 4), providing an independent corroboration of the extracted structure, as well as a direct test of the DFT calculations.

![](images/aae06a8d07d4596ad459b7a8c3cfc3c445279b46099c944c9e774430c30ee363.jpg)  
a

![](images/29450085f7673e85df79644ce059b5a4b35b98ec853c56bc468e44c8b63f3a96.jpg)

![](images/20f2aeeccd4c57b03229398ace0309ed3a9686e59af44664ff91122f526de51b.jpg)

![](images/fdc7a58f59c7f261c1b76b36cd3d95d3b02a209bd9407ee8cb0826f286166b41.jpg)  
Fig. 4 | Atomic-scale imaging of the 27-nuclear-spin cluster. a, Two-dimensional (2D) plot summarizing all couplings between the 27 spins identified by 3D spectroscopy (Fig. 2), including identification of spins with overlapping frequencies. The size and colour of each point indicate the strength of the measured coupling, averaged over the electron  $m_{\mathrm{s}} = +1$  and  $m_{\mathrm{s}} = -1$  states. Dashed grey lines indicate the nuclear spin frequencies ( $m_{\mathrm{s}} = -1$  state). Solid grey lines indicate the bare  $^{13}\mathrm{C}$  Larmor frequency. Total measurement time,  $\sim 400$  h. See Supplementary Tables 2-4 for numerical values and uncertainties. b, 3D structure of the nuclear spins, obtained using the diamond-lattice method (see text). Blue lines indicate couplings greater

![](images/9d46438df250850b07408f602fd31d4202d0fe71aebcaaa5c5a46104cda3eaa8.jpg)  
d  
than  $3\mathrm{Hz}$  and illustrate the connectivity of the cluster. See Supplementary Video 1 for a visualization and Extended Data Fig. 3 for zoom-ins of strongly coupled subclusters. c, Distance  $\Delta r$  between the obtained spin positions from the diamond-lattice method (see text) and from a least-squares optimization. Deviations are generally below one diamond bond length (-1.54 Å, dashed line). d, The uncertainties for the 77 spatial coordinates of the cluster from a least-squares optimization are smaller than the bond length, indicating atomic-scale resolution. See Supplementary Figs. 4-6 and Supplementary Table 5 for in-depth comparisons between the structures and uncertainties obtained with different methods.

Looking beyond quantum sensing, this precise microscopic characterization of the NV environment provides new opportunities for improved control of quantum bits for quantum information $^{20,24,28,31,32}$  and for investigating many-body physics in coupled spin systems.

In our method, the NV sensor spin is exclusively used to create and detect polarization (Fig. 1b). Therefore, the two main requirements for the sensor spin are (1) a high-contrast readout to keep measurement times manageable and (2) that it does not limit the spectral resolution by disturbing the evolution of the nuclear spins through relaxation[25,30,31]. We satisfy these requirements by working at  $4\mathrm{K}$ , so that the electron relaxation is negligible  $(T_{1} = 3.6(3)\times 10^{3}\mathrm{s})^{20}$ , and high-fidelity readout is obtained through resonant optical excitation (see Methods). Recent experiments have demonstrated both these requirements up to room temperature[5,25,26,30,31]. The electron-spin relaxation—milliseconds at room temperature—can be decoupled from the sample spins through laser illumination[30,31] or sequential weak measurements[25,26]. High-contrast readout has been demonstrated by using a nuclear spin as a memory that can be read out repeatedly[5,30]. Nuclear spins themselves are well isolated from temperature effects[31]. Therefore, when combined with those methods, the ideas presented here could be extended to ambient conditions.

In conclusion, we have developed and demonstrated 3D atomic-scale imaging of large clusters of nuclear spins using a single-spin quantum sensor. Our approach is compatible with room-temperature operation $^{25,26,30,31}$  and could be extended to larger structures, as the number of required measurements scales linearly with the number of spins. Future improvements in the data acquisition and the computation of 3D structures can further reduce time requirements. In particular, recent methods to polarize and measure nuclear spins are expected to improve sensitivity $^{25,26}$ , especially for samples with weak couplings to

the NV sensor. Optimized sampling of the measurements and adaptive algorithms based on real-time structure analysis can further reduce the total number of required measurements. Therefore, when combined with recent advances in nanoscale NMR with near-surface NV centres $^{2-8}$ , our results provide a path towards magnetic imaging of individual molecules and complex spin structures external to diamond $^{10-13}$ .

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41586-019-1834-7.

1. Rule, G. S. & Hitchens, T. K. Fundamentals of Protein NMR Spectroscopy Vol. 5 (Springer Science & Business Media, 2006).  
2. Mamin, H. et al. Nanoscale nuclear magnetic resonance with a nitrogen-vacancy spin sensor. Science 339, 557-560 (2013).  
3. Staudacher, T. et al. Nuclear magnetic resonance spectroscopy on a (5-nanometer)3 sample volume. Science 339, 561-563 (2013).  
4. Shi, F. et al. Single-protein spin resonance spectroscopy under ambient conditions. Science 347, 1135-1138 (2015).  
5. Lovchinsky, I. et al. Nuclear magnetic resonance detection and spectroscopy of single proteins using quantum logic. Science 351, 836-841 (2016).  
6. Aslam, N. et al. Nanoscale nuclear magnetic resonance with chemical resolution. Science 357, 67-71 (2017).  
7. Glenn, D. R. et al. High-resolution magnetic resonance spectroscopy using a solid-state spin sensor. Nature 555, 351-354 (2018).  
8. Smits, J. et al. Two-dimensional nuclear magnetic resonance spectroscopy with a microfluidic diamond quantum sensor. Sci. Adv. 5, eaaw7895 (2019).  
9. Lovchinsky, I. et al. Magnetic resonance spectroscopy of an atomically thin material using a single-spin qubit. Science 355, 503-507 (2017).

10. Ajoy, A., Bissbort, U., Lukin, M. D., Walsworth, R. L. & Cappellaro, P. Atomic-scale nuclear spin imaging using quantum-assisted sensors in diamond. Phys. Rev. X 5, 011001 (2015).  
11. Kost, M., Cai, J. & Plenio, M. B. Resolving single molecule structures with nitrogen-vacancy centers in diamond. Sci. Rep. 5, 11007 (2015).  
12. Perunicic, V., Hill, C., Hall, L. & Hollenberg, L. A quantum spin-probe molecular microscope. Nat. Commun. 7, 12667 (2016).  
13. Wang, Z.-Y., Haase, J. F., Casanova, J. & Plenio, M. B. Positioning nuclear spins in interacting clusters for quantum technologies and bioimaging. Phys. Rev. B 93, 174104 (2016).  
14. Sushkov, A. et al. Magnetic resonance detection of individual proton spins using quantum reporters. Phys. Rev. Lett. 113, 197601 (2014).  
15. Müller, C. et al. Nuclear magnetic resonance spectroscopy with single spin sensitivity. Nat. Commun. 5, 4703 (2014).  
16. Shi, F. et al. Sensing and atomic-scale structure analysis of single nuclear-spin clusters in diamond. Nat. Phys. 10, 21-25 (2014).  
17. Zopes, J. et al. Three-dimensional localization spectroscopy of individual nuclear spins with sub-angstrom resolution. Nat. Commun. 9, 4678 (2018).  
18. Zopes, J., Herb, K., Cujia, K. S. & Degen, C. L. Three-dimensional nuclear spin positioning using coherent radio-frequency control. Phys. Rev. Lett. 121, 170801 (2018).  
19. Sasaki, K., Itoh, K. M. & Abe, E. Determination of the position of a single nuclear spin from free nuclear precessions detected by a solid-state quantum sensor. Phys. Rev. B 98, 121405 (2018).  
20. Abobeih, M. H. et al. One-second coherence for a single electron spin coupled to a multi-qubit nuclear-spin environment. Nat. Commun. 9, 2552 (2018).  
21. Yang, Z. et al. Structural analysis of nuclear spin clusters via two-dimensional nanoscale nuclear magnetic resonance spectroscopy. Preprint at https://arxiv.org/abs/1902.05676v2 (2019).

22. Rosenfeld, E. L., Pham, L. M., Lukin, M. D. & Walsworth, R. L. Sensing coherent dynamics of electronic spin clusters in solids. Phys. Rev. Lett. 120, 243604 (2018).  
23. Knowles, H. S., Kara, D. M. & Atature, M. Demonstration of a coherent electronic spin cluster in diamond. Phys. Rev. Lett. 117, 100802 (2016).  
24. Cramer, J. et al. Repeated quantum error correction on a continuously encoded qubit by real-time feedback. Nat. Commun. 7, 11526 (2016).  
25. Pfender, M. et al. High-resolution spectroscopy of single nuclear spins via sequential weak measurements. Nat. Commun. 10, 594 (2019).  
26. Cujia, K., Boss, J., Herb, K., Zopes, J. & Degen, C. Tracking the precession of single nuclear spins by weak measurements. Nature 571, 230-233 (2019).  
27. Slichter, C. Principles of Magnetic Resonance (Springer, 1996).  
28. Bradley, C. E. et al. A ten-qubit solid-state spin register with quantum memory up to one minute. Phys. Rev. X 9, 031045 (2019).  
29. Laraoui, A. et al. High-resolution correlation spectroscopy of  $^{13}\mathrm{C}$  spins near a nitrogen-vacancy centre in diamond. Nat. Commun. 4, 1651 (2013).  
30. Pfender, M. et al. Nonvolatile nuclear spin memory enables sensor-unlimited nanoscale spectroscopy of small spin clusters. Nat. Commun. 8, 834 (2017).  
31. Maurer, P. C. et al. Room-temperature quantum bit memory exceeding one second. Science 336, 1283-1286 (2012).  
32. Dutt, M. G. et al. Quantum register based on individual electronic and nuclear spin qubits in diamond. Science 316, 1312-1316 (2007).  
33. Nizovtsev, A. P. et al. Non-flipping  $^{13}\mathrm{C}$  spins near an NV center in diamond: hyperfine and spatial characteristics by density functional theory simulation of the  $\mathrm{C}_{510}[\mathrm{NV}] \mathrm{H}_{252}$  cluster. New J. Phys. 20, 023022 (2018).

© The Author(s), under exclusive licence to Springer Nature Limited 2019

# Article

# Methods

# Sample and NV centre sensor

We use a naturally occurring NV centre in a diamond grown homoepitaxially by chemical vapour deposition with a  $1.1\%$  (natural) abundance of  ${}^{13}\mathrm{C}$  and a  $\langle 111\rangle$  crystal orientation (Element Six). The NV is placed in a solid-immersion lens to enhance the photon-collection efficiency[34]. The NV centre was selected for the absence of  ${}^{13}\mathrm{C}$  spins with hyperfine couplings  $>500~\mathrm{kHz}$ . The NV electron-spin dephasing time is  $T_{2}^{*} = 4.9(2)\mu s$  and the echo coherence time is  $T_{2} = 1.182(5)\mathrm{ms}$ . We work at  $4\mathrm{K}$ , so that the electron relaxation is negligible ( $T_{1} = 3.6(3)\times 10^{3}\mathrm{s}$ )[20] and use high-fidelity readout through resonant optical excitation (average fidelity  $F = 94.5\%$ [34].

The observed nuclear-spin dephasing times range from  $T_{2}^{*} = 3$  msto  $17$  ms, corresponding to an inhomogeneous linewidth of about  $30 - 150$  Hz. Owing to the frequency differences between nuclear spins in  $m_{\mathrm{s}} = \pm 1$  (Supplementary Table1), spin diffusion is strongly suppressed and the longitudinal relaxation of the nuclear spins is  $T_{1} > 6$  min (ref. 28).

# Magnetic-field alignment

A magnetic field of  $-403\mathrm{G}$  is applied using a room-temperature permanent magnet, which is installed on an XYZ translation stage to control the strength and the direction of the magnetic field. Our methods use echo pulses and are therefore robust against slow fluctuations in the magnetic-field strength. Although magnetic-field drift has a negligible effect on the measured nuclear-nuclear couplings, we stabilize the magnetic field to  $< 3\mathrm{mG}$  using temperature stabilization of the magnet and an automatic re-calibration procedure (every few hours).

We align the magnetic field along the NV axis to avoid electron-mediated shifts that cause the measured couplings to deviate from nuclear-nuclear dipolar coupling (see Supplementary Information section III). We use a 'thermal' echo sequence, which was previously used to measure the temperature $^{35}$  (see Extended Data Fig. 5). In this sequence, the electron evolves half of the time in a superposition of the states  $m_{\mathrm{s}} = 0$  and  $m_{\mathrm{s}} = -1$  and the other half in a superposition of  $m_{\mathrm{s}} = 0$  and  $m_{\mathrm{s}} = +1$ . Because the energies of the states  $m_{\mathrm{s}} = \pm 1$  are shifted by equal and opposite amounts by Hamiltonian terms proportional to the spin operator  $S_{z}$ , the effects of such terms are cancelled. However, Hamiltonian terms that shift the energies of  $m_{\mathrm{s}} = \pm 1$  in the same way (such as the magnetic field perpendicular to  $z$ ) do not cancel. Therefore, the sequence decouples the main source of noise (the magnetic-field fluctuations along  $z$  from the surrounding spin bath) while remaining sensitive to shifts caused by a non-zero magnetic field in the  $x, y$  directions. This sequence extends the sensing time from the dephasing time  $T_{2}^{*} \approx 5 \mu s$  to the echo coherence time  $T_{2} \approx 1 \mathrm{~ms}$ , resulting in an uncertainty of  $0.07^{\circ}$  in the alignment (Extended Data Fig. 5).

# Quantum sensing sequences

We employ two different sensing sequences (see the polarization and detection blocks in Fig. 1b). Sequence A consists of dynamical decoupling sequences of  $N'$  equally spaced  $\pi$  pulses on the electron spin of the form  $^{36-38}(\tau_{\mathrm{r}} - \pi - \tau_{\mathrm{r}})^{N'}$ . This sequence is sensitive only to nuclear spins with a substantial electron-nuclear hyperfine component perpendicular to the applied magnetic field  $^{36}$ . The inter-pulse spacing  $2\tau_{\mathrm{r}}$  determines the spin frequency that is being probed.

Sequence B is a recently developed method, described in detail in Bradley et al.28, that interleaves the dynamical decoupling sequence with radiofrequency (RF) pulses. This method enables the detection of spins with a weak or negligible perpendicular hyperfine component28,30 For this sequence, the frequency of the RF pulse sets the targeted spin frequency, whereas  $\tau_{\mathrm{r}}$  can be chosen freely28. Importantly, the amplitudes and phases of the RF pulses are set so that together they build up to the desired evolution28. The added RF field imprints a deterministic phase on the electron-spin sensor28, which we compensate by calibrating the phase of the electron  $\pi /2$  pulses.

# Electron-nuclear spectroscopy

As a starting point, we use the electron spin as a sensor to roughly characterize some of the nuclear spins in the cluster. We perform spectroscopy by sweeping the interpulse delay  $\tau_{\mathrm{r}}$  in sequence A (see, for example, Abobeih et al. $^{20}$ ) and the RF frequency for sequence B (ref. $^{28}$ ). This identifies the frequency range in which spins are present in the cluster and provides the parameters to polarize and detect several spins $^{24}$ . We note that the resolution of this spectroscopy technique is limited by the electron spin  $T_{2}$  and the nuclear spin  $T_{2}^{*}$ .

# Nuclear-nuclear double-resonance spectroscopy

The sequence for the double-resonance experiments is shown in Fig. 1b and Extended Data Fig. 1. To polarize and detect the probe spin, we use either sequence A (without the RF1 pulses in the dashed box) or sequence B (with the RF1 pulses), depending on whether the perpendicular hyperfine coupling to the electron spin is sufficiently large or not. For sequence A, we set the interpulse delay as  $\tau_{\mathrm{r}} = (2k - 1)\pi /(\omega_0 + \mathrm{RF1})$  with  $k$  an integer and  $\omega_0$  the  $^{13}\mathrm{C}$  Larmor frequency for the  $m_{\mathrm{s}} = 0$  electron state, and calibrate the number of pulses  $N^{\prime}$  to maximize the signal<sup>36</sup>. For sequence B we calibrate the RF power to maximize the signal.

We create nuclear polarization by projective measurements $^{24}$ . First the electron is prepared in a superposition state through resonant excitation $^{34}$  and a  $\pi/2$  pulse. Second, the sensing sequence correlates the phase of the electron with the nuclear spin state. Finally, the electron is read out so that the nuclear spin is projected to a polarized state $^{24}$ . To enhance the signal-to-noise ratio and to ensure that the electron measurement does not disturb the nuclear-spin evolution, we perform the double-resonance sequence only if a photon is detected during the electron readout $^{24}$ . The resulting signal contrast for different spins varies from  $20\%$  to  $96\%$ .

Because the correlation data are read out and stored in the electronics, the ultimate limit for the spectral resolution of our method—that is, when applied on hypothetical signals with infinitesimal spectral width—is set by the precision of the 10-MHz reference clock used for the timing of the waveform generator[7,39,40]. For the double-resonance sequence, the phases of the RF1 echo pulses are calibrated so that their phase difference is 0 or  $\pi/2$  with respect to the polarization axis, which is determined by the direction of the hyperfine interaction[18,19,41]. For the target spins, the phase of the RF2 pulse does not affect the signal and is set arbitrarily.

To mitigate pulse errors, we alternate the phases of the pulses following the XY8 scheme $^{42}$ , for both the electron and nuclear spins. For the electron spin, we use Hermite pulse envelopes $^{43}$  with a Rabi frequency of  $-14\mathrm{MHz}$  to obtain effective microwave pulses without initialization of the intrinsic  $^{14}\mathrm{N}$  nuclear spin. The nuclear-spin Rabi frequencies are in the range  $0.3 - 0.7\mathrm{kHz}$ .

# Data analysis

We extract the spin-spin couplings  $f$  and their uncertainties from fitting the time-domain double-resonance signals (for example, Fig. 1e, f, top) with  $S = a + A\mathrm{e}^{-(t / T_2)^n}\cos (2\pi ft + \phi)$ , where  $a$ ,  $A$ ,  $\varphi$  and  $T_{2}$  are fit parameters that account for the offset, amplitude, phase and coherence time of the signal, respectively. The PSD is obtained from a Fourier transform of the time-domain signal with zero filling<sup>1</sup> and the d.c. component filtered out (for example, Fig. 1e, f, bottom). The spectral resolution (FWHM) is obtained from a Gaussian fit of the PSD. Alternatively, we can define the spectral resolution (FWHM) directly from the time-domain signal as  $2\sqrt{\ln 2} /(\pi T_2)$ . This yields a spectral resolution of  $0.91(3)\mathrm{Hz}$  for Fig. 1e. For the spin in Fig. 1f, using  $N = 1$  yields a spectral resolution of  $0.8(1)\mathrm{Hz}$  and using  $N = 256$  yields  $49(2)\mathrm{mHz}$ . We note that no saturation is observed in the improvement of the spectral resolution with the number of pulses. Therefore, with more pulses (and longer measurement times) higher spectral resolutions and more precise measurements are feasible.

# Electron-mediated interactions

We calculate corrections to the nuclear-nuclear couplings caused by the presence of the electron spin using perturbation theory up to second order. The effect of other nuclear spins on nuclear-nuclear couplings was found by numerical simulations to be negligible (of the order of millihertz). In contrast to previous results for strong electron-nuclear couplings $^{32,44}$ , here many-body interactions due to non-secular nuclear-nuclear couplings must be taken into account. The resulting frequency in a double-resonance experiment is of the form (see Supplementary Information section III)

$$
f _ {\mathrm {D R}} \left(m _ {\mathrm {s}} = \pm 1\right) \approx \frac {1}{4 \pi} \left| C + \Delta \lambda_ {1} \left(m _ {\mathrm {s}}\right) + \Delta \lambda_ {2} \left(m _ {\mathrm {s}}\right) + \Delta \lambda_ {3} \left(m _ {\mathrm {s}}\right) \right| \tag {1}
$$

where  $C$  is the parallel (zz) component of the dipole-dipole interaction between the nuclear spins and  $\Delta \lambda_{i}$  are correction terms accounting for the presence of the electron spin. See Supplementary Information for the full analysis of all terms.

The dominant correction for our parameter regime is  $\Delta \lambda_{2}$ , which depends on both the electron-nuclear and nuclear-nuclear interactions. We make a Taylor expansion up to first order in  $A_{zz}^{(j)} / (\gamma_cB_z)$ , where  $A_{zz}^{(j)}$  is the parallel electron-nuclear hyperfine coupling for spin  $j$ ,  $\gamma_{c}$  is the nuclear gyromagnetic ratio and  $B_{z}$  is the component of the magnetic field along the NV axis. This yields an expression of the form  $\Delta \lambda_2(m_s)\approx m_s\Delta \lambda_2^{(0)} + \Delta \lambda_2^{(1)}$ , where the leading (zeroth-order) correction  $m_{s}\Delta \lambda_{2}^{(0)}$  is given by

$$
\Delta \lambda_ {2} ^ {(0)} = \frac {\left(A _ {z x} ^ {(1)} + A _ {z x} ^ {(2)}\right) C _ {z x} + \left(A _ {z y} ^ {(1)} + A _ {z y} ^ {(2)}\right) C _ {z y}}{\gamma_ {\mathrm {c}} B _ {z}} \tag {2}
$$

where  $A_{zx}^{(j)}(C_{zx})$  and  $A_{zy}^{(j)}(C_{zy})$  are the perpendicular electron-nuclear (nuclear-nuclear) coupling components. We cancel this term by averaging the double-resonance frequencies measured for the  $m_{\mathrm{s}} = \pm 1$  electron-spin projections.

The remaining electron-mediated corrections depend on the angles of the electron–nuclear hyperfine interactions. Because these angles are unknown, we estimate the maximum possible shift for each spin-spin interaction by maximizing over all angles. For our cluster (Fig. 4), most of these maximum possible shifts are small (their average value is  $-0.03\mathrm{Hz}$ ). In rare cases, the maximum possible correction runs up to  $0.6\mathrm{Hz}$  (see Supplementary Information section IV) but, as the locations of the involved spins are already precisely fixed through strong ( $>20\mathrm{Hz}$ ) interactions with several other spins, this would have a negligible effect on the obtained structure. Therefore, we can base the structural analysis on dipole-dipole interactions.

# 3D structure analysis

The 3D structure of the nuclear spins is obtained using the dipole-dipole coupling formula, which relates the  $zz$  couplings  $C_{ij}$  to the spatial coordinates  $x,y,z$  of spins  $i$  and  $j$  as

$$
C _ {i j} = \frac {\alpha_ {i j}}{\Delta r _ {i j} ^ {3}} \left[ \frac {3 \left(z _ {j} - z _ {i}\right) ^ {2}}{\Delta r _ {i j} ^ {2}} - 1 \right] \tag {3}
$$

where  $\Delta r_{ij} = \sqrt{(x_j - x_i)^2 + (y_j - y_i)^2 + (z_j - z_i)^2}$ ,  $\alpha_{ij} = \mu_0\gamma_i\gamma_j\hbar /(4\pi)$ ,  $\mu_0$  is the permeability of free space,  $\gamma_{i}$  is the gyromagnetic ratio of nuclear spin  $i$ , and  $\hbar$  is the reduced Planck constant.

The goal is to minimize the sum of squares  $\xi = \sum_{i < j} |\Delta f_{ij}|^2$ , where  $\Delta f_{ij} = f_{ij} - [|C_{ij}|/(4\pi)]$  are the residuals and  $f_{ij}$  are the measured coupling frequencies. For  $M = 27$  spins, there are  $3M - 4 = 77$  free coordinates and  $M(M - 1)/2 = 351$  pairwise couplings, of which 171 were determined in this work.  $\xi$  can in principle be minimized using standard fitting methods; however, tests with randomly generated spin clusters indicate that the initial guess for the coordinates should be within  $-0.5\AA$  in order for the fit to converge to the correct solution. For 27 spins, this

corresponds to an intractable  $\sim 10^{100}$  possible initial guesses. Instead, we sequentially build the structure by adding spins one by one.

For the diamond-lattice positioning method, we first use the strongest measured coupling to any spin that is already positioned to reduce the position of a new spin to a number of possible lattice coordinates. For each possible coordinate, we then check if the predicted couplings to all other spins satisfy  $\Delta f_{ij} < T$ , where  $T = 1.1$  Hz is a tolerance that is chosen to ensure that all promising configurations are included while maintaining reasonable computation time. Configurations are discarded if they do not satisfy this requirement for one or more of the pairwise couplings. If more than  $X_{\mathrm{cutoff}} = 5,000$  possible configurations are identified, only the best  $X_{\mathrm{cutoff}}$  solutions are kept, according to their  $\xi$  values.

For the cubic-lattice positioning method, the same procedure is followed, with the key difference being that the lattice is adaptively generated depending on the strongest coupling to a spin already positioned in the cluster (see Supplementary Information section III). This ensures that in each case the lattice spacing is fine enough to appropriately sample the volume associated with the dipole-dipole coupling between the nuclear spins.

# Robustness of the analysis

The method is robust to failure. The problem is generally highly overdetermined, so that discarding the correct configuration because of  $X_{\mathrm{cutoff}}$  will lead to no solution at all, instead of an erroneous solution. Given enough computational resources, a correct solution is always expected to be found. As a test, we used the cubic-lattice reconstruction method on 17 randomly generated 30-spin clusters with added noise, and no erroneous structures were returned (see Supplementary Information section IV).

# Comparison to 1D Ramsey spectroscopy

Extended Data Fig. 2 compares the 1D Ramsey signal with spectra reconstructed using 3D spectroscopy. This comparison illustrates our method's effective resolution improvement and its ability to resolve dense spectra. We note that, apart from the spectral resolution, the signals should not be compared directly, because the Ramsey experiment is difficult to interpret quantitatively. First, the Ramsey signals probably contain contributions from multiple spins, due to both spectral overlap and higher-order contributions $^{36-38}$ . Second, any inadvertent polarization of other spins in the cluster or the environment modifies the spectrum. These effects are difficult to separate from actual nuclear-nuclear couplings, and the fact that the spectra are asymmetric indicates that they play a non-negligible role. Our 3D spectroscopy method resolves these issues.

# Finding the position of the NV centre

Because the NV electron wavefunction is not known a priori, we cannot use the electron-nuclear couplings to find the NV position. In particular, DFT calculations[33] indicate that for electron-nuclear couplings in the range observed here, assuming a point-dipole model for the electron spin can lead to large discrepancies and is therefore not justified.

Our approach is to measure the couplings between the  $^{13}\mathrm{C}$  spins and the NV nitrogen nuclear spin, for which the point-dipole approximation is accurate. The nitrogen-  $^{13}\mathrm{C}$  couplings can be measured using a double-resonance procedure similar to that used for measuring  $^{13}\mathrm{C}-^{13}\mathrm{C}$  couplings. We use the nitrogen spin as the probe spin, which gives better spectral resolution owing to its longer coherence time  $(T_{2} = 2.3(2)\mathrm{s})^{28}$ . We initialize the nitrogen spin in the state  $m_{\mathrm{i}} = 0$  using measurement-based initialization[34] and manipulate the spin state using RF pulses ( $m_{\mathrm{i}}$ , nuclear-spin projection). Extended Data Fig. 4b shows the measured couplings between the nitrogen and  $^{13}\mathrm{C}$  spins.

Using the couplings, the nitrogen spin is added to the  $^{13}\mathrm{C}$  nuclear-spin cluster using the diamond-lattice positioning method, with  $\gamma_{j} \rightarrow \gamma_{\mathrm{n}} = 2\pi \times 0.3077\mathrm{kHzG}^{-1}(\gamma_{\mathrm{n}}$  is the nitrogen gyromagnetic ratio), in equation (3). Determining the nitrogen lattice site also allows the

# Article

vacancy site to be determined on the basis of the known NV distance and the alignment with the magnetic field along  $z$ , thereby giving the location and the orientation of the NV centre with respect to the  ${}^{13}\mathrm{C}$  nuclear-spin cluster. The resulting 3D plot of the best solution is shown in Extended Data Fig. 4a. The nitrogen spin coordinate is the same for all 5,000 configurations identified. Extended Data Fig. 4c gives the results of a least-squares fit.

# Comparison to DFT

Now that we have independently determined the position of the  $^{13}\mathrm{C}$  spins relative to the NV centre, we can compare the hyperfine couplings to DFT calculations without any prior assumptions. In Nizovtsev et al. [33], hyperfine couplings are calculated for 510 lattice sites surrounding the NV centre. Extended Data Fig. 4d shows the lattice positions given in ref. [33], along with the coordinates of the  $^{13}\mathrm{C}$  spins found in this work. To match the coordinate frames, the  $^{13}\mathrm{C}$  spin coordinates are mirrored ( $z \rightarrow -z$ ) and transformed so that the nitrogen spin is at the origin. Additionally, a scaling factor of 1.02 is applied, which was found by comparing the 510 lattice sites from ref. [33] with the same sites in our work. Five of the 27 spins identified in this work were calculated in ref. [33]. The remaining spins cannot yet be compared with DFT calculations. Extended Data Fig. 4e shows the measured electron-  $^{13}\mathrm{C}$  hyperfine couplings (see Supplementary Table 1), as well as those predicted in ref. [33], for the five spins. For the DFT results, we take the average of the predicted couplings for the possible  $C_{3v}$  symmetric lattice sites. Additionally, we take the negative of the predicted parallel component of the electron-nuclear coupling  $A_{\parallel}$  for all spins (a global minus sign is possible because of the unknown orientation of the magnetic field along  $z$ ).

# Data availability

The data that support the findings of this study are available from the corresponding author upon request.

34. Robledo, L. et al. High-fidelity projective read-out of a solid-state spin quantum register. Nature 477, 574-578 (2011).

35. Toyli, D. M., de las Casas, C. F., Christie, D. J., Dobrovitski, V. V. & Awschalom, D. D. Fluorescence thermometry enhanced by the quantum coherence of single spins in diamond. Proc. Natl Acad. Sci. USA 110, 8417-8421 (2013).  
36. Taminiau, T. H. et al. Detection and control of individual nuclear spins using a weakly coupled electron spin. Phys. Rev. Lett. 109, 137602 (2012).  
37. Kolkowitz, S., Unterreithmeier, Q. P., Bennett, S. D. & Lukin, M. D. Sensing distant nuclear spins with a single electron spin. Phys. Rev. Lett. 109, 137601 (2012).  
38. Zhao, N. et al. Sensing single remote nuclear spins. Nat. Nanotechnol. 7, 657-662 (2012).  
39. Boss, J. M., Cujia, K., Zopes, J. & Degen, C. L. Quantum sensing with arbitrary frequency resolution. Science 356, 837-840 (2017).  
40. Schmitt, S. et al. Submillihertz magnetic spectroscopy performed with a nanoscale quantum sensor. Science 356, 832-837 (2017).  
41. Laraoui, A., Pagliero, D. & Meriles, C. A. Imaging nuclear spins weakly coupled to a probe paramagnetic center. Phys. Rev. B 91, 205410 (2015).  
42. Gullion, T., Baker, D. B. & Conradi, M. S. New, compensated Carr-Purcell sequences. J. Magn. Reson. 89, 479-484 (1990).  
43. Warren, W. S. Effects of arbitrary laser or NMR pulse shapes on population inversion and coherence. J. Chem. Phys. 81, 5437-5448 (1984).  
44. Zhao, N., Hu, J.-L., Ho, S.-W., Wan, J. T. K. & Liu, R. B. Atomic-scale magnetometry of distant nuclear spin clusters via nitrogen-vacancy spin in diamond. Nat. Nanotechnol. 6, 242-246 (2011).

Acknowledgements We thank V. V. Dobrovitski, T. van der Sar, W. Hahn, M. Scheer and R. Zia for valuable discussions. We thank R. F. L. Vermeulen and R. N. Schouten for assistance with the RF electronics, and M. Eschen for assistance with the experimental setup. We acknowledge support from the Netherlands Organisation for Scientific Research (NWO/OCW) through a Vidi grant, as part of the Frontiers of Nanoscience (NanoFront) programme and as part of the Quantum Software Consortium programme (project number 024.003.037/3368).

Author contributions M.H.A. and T.H.T. devised the experiments. M.H.A. performed the experiments. J.R. developed the 3D structure analysis method. M.H.A., J.R. and T.H.T. analysed the data. M.H.A., J.R., M.J.D. and C.E.B. prepared the experimental apparatus. C.E.B. and J.R. developed the RF electronics. H.P.B. and M.A.B. performed preliminary experiments. M.H.A., M.J.D., J.R., C.E.B. and T.H.T. developed the magnetic-field alignment procedure and the  $^{14}\mathrm{N}$  echo spectroscopy. M.M. and D.J.T. grew the diamond sample. M.H.A., J.R. and T.H.T. wrote the manuscript with input from all authors. T.H.T. supervised the project.

Competing interests The authors declare no competing interests.

# Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s41586-019-1834-7.  
Correspondence and requests for materials should be addressed to T.H.T.  
Peer review information Nature thanks Nir Bar-Gill, Vidya Praveen Bhallamudi and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.  
Reprints and permissions information is available at http://www.nature.com/reprints.

![](images/60e09d18b16bd2a2500bb04a81334dc458c29e3ecd98351265bea6ced75fafaa.jpg)  
Extended Data Fig.1|Experimentalsequence. The pulse sequence consists of five parts: sensor preparation, sensor initialization, polarization of the probe spin, double resonance, and detection of the probe spin. Sensor preparation: the NV centre is prepared by excitation with two 637-nm lasers for  $150~\mu \mathrm{s}$  and counting of the detected photons (read-out (RO) laser resonant with the  $E_{x}$  transition and initialization (Init) laser resonant with the  $E^{\prime}$  transition) $^{24,34}$ . If the number of photons exceeds a certain threshold, the NV is in the negative charge state and resonant with both lasers, and we proceed to the next step. If not, we apply a 515-nm laser (charge reset (RS) laser, 1 ms) and repeat the process $^{24,34}$ . Sensor initialization: the NV electron spin is initialized in the  $m_{s} = 0$  state through spin pumping (Init laser,  $100~\mu \mathrm{s})^{34}$ . Polarization of the probe spin: first, the NV sensor is brought into a superposition state using a  $\pi /2$  pulse. Then, a dynamical decoupling sequence of  $N^{\prime}$  equally spaced  $\pi$  pulses of the  
form  $(\tau_{\mathrm{r}} - \pi - \tau_{\mathrm{r}})^{N'}$  is applied to the electron spin. This sequence correlates the state of the nuclear spin(s) with the phase of the electron spin. We use two different sequences (see Methods). For sequence B, the microwave (MW)  $\pi$  pulses are interleaved with RF pulses (RF1) that resonantly drive the probe spin(s) (dashed box); see Bradley et al. [28] for details. A second  $\pi/2$  pulse maps the electron phase to the population and the electron spin is read out (RO laser). Double resonance:  $N$  echo pulses are applied simultaneously on the probe spin(s) (RF1) and the target spin(s) (RF2), so that the coupling between these spins is isolated. To mitigate pulse errors, we alternate the phases of the pulses following the XY8 scheme [42]. Detection of the probe spin: the detection sequence is the same as the polarization sequence except for the final RO laser pulse, which is applied for  $10~\mu s$  and with higher power.

![](images/4ae1a6af315fa11c4a448e2395c670a84385e64a1e20a11ff72bd05cbb1b39c0.jpg)  
a

![](images/60fe3d059f502558c099a0004303b1a5f5f1841765c796c6366f1cbf9daa6038.jpg)  
b

![](images/818a212719fe7059c784e02a57f99b5e8f4d0beb51196aaffae5c2ef9b17a1dd.jpg)

![](images/de56a0315d5e43518b439fb829d64a6f86ac6d7606be936417390842f0a2d225.jpg)  
C  
d

![](images/0616ca92a0815a3c92b070cf140eec9403593af76bed0a9931b63a5a2976f24c.jpg)

![](images/f0d92b9abf30bbb53eefe4d927fcbc516927d4998a058bd8d2e87cd5620d8f75.jpg)

![](images/46b2c7615e4b9d57f2812468e5d06033c3daf0b583c36c2ff27a1c9baf178718.jpg)

e  
Extended Data Fig. 2 | Ramsey experiments and reconstructed spectra.  
Free evolution time (ms)  
![](images/e6654f8b6d7f6655bf40b6b5a5c82129b49a8f40648df38e7d0a27b3b9e3354d.jpg)  
based on the seven strongest coupling strengths extracted from our high-resolution double-resonance spectroscopy (Supplementary Table 4). These frequencies are given by  $f_0 \pm f_1 \pm f_2 \pm f_3 \pm f_4 \pm f_5 \pm f_6 \pm f_7$ , where  $f_1$  to  $f_7$  are the seven largest measured coupling strengths for C2. c-e, The same experiment for C3 (c; -5 kHz detuning), C15 (d; -1 kHz detuning) and C5 (e; -2 kHz detuning).

![](images/4ea1a88ea34f7e5bd13e831190fe3cb6e1d0ec88e8aa26dd3f4c30113b7a7433.jpg)  
a, Schematic of the pulse sequence used in the Ramsey experiment (equivalent to correlation spectroscopy); see Methods and Extended Data Fig. 1 for details.  
b, Ramsey signal for C2 and the corresponding PSD (5 kHz detuning). The red line represents the central frequency  $f_{0}$ . Green lines are the  $2^{7}$  frequencies

![](images/4f174e7e438f9697844aba5c89bb67c4c3e16c1dcadfd5e0ce0792ecb5012a3e.jpg)

![](images/f1bb3e39100283c95cb7d248aab0861e0e8da2716b1c56e938a3815d182ccff6.jpg)  
Extended Data Fig. 3 | Strongly coupled subclusters. 3D plots showing the structure of two strongly coupled subclusters (orange boxes) within the larger cluster (shown in the centre). Ramsey measurements performed on spins within these subclusters show clear beating signals within their dephasing time  
$T_{2}^{*}$  (see, for example, Extended Data Fig. 2). a, Eight-spin subcluster. b, Four-spin subcluster. Couplings above  $3\mathrm{Hz}$  are marked blue, above  $20\mathrm{Hz}$  green and above  $50\mathrm{Hz}$  red. Grey points show the 2D projections of the diamond-lattice coordinates.

![](images/532382d9686bff76f709714adda49204281cafc4cdb06797e944757a092666d4.jpg)

![](images/fec3ec57d15274146b506161d4073a2b198138337495f9a7b80b504ef1184f2a.jpg)

![](images/dad8da13d1e7836fbe80cdb3b882ca9ef8216e8b9fa04f19c64f1d8139f6d5a2.jpg)

![](images/b9295e94fc908d3ea18009550b20342c075d2af6a5e9ffa328c149f62a303b36.jpg)

![](images/f4385219384ee88b3af199616d98056cbda5b7ae21a16ea2bc507dcec0b685b1.jpg)  
Extended Data Fig. 4 | Finding the position of the NV centre. a, 3D plot showing the 27-nuclear-spin cluster shown in Fig. 4, with the position of the nitrogen spin (green) and vacancy (purple) lattice sites calculated from the measured nitrogen $^{-13}$ C couplings. The grey dots show the 2D projections of the diamond-lattice coordinates. b, Bar plot showing the measured couplings  $f_{iN}$  between  ${}^{13}\mathrm{C}$  spin  $i$  and the nitrogen spin (grey), as well as the theoretically calculated couplings  $|C_{iN}| / 4\pi$  (green). Error bars are one standard deviation. See Supplementary Table 4 for the numerical values. c, Bar plots of  $\Delta r$  for the fitted position of the nitrogen spin (black) and fit errors  $\delta x$  (blue),  $\delta y$  (orange)

![](images/bb203963e9d6a6525beffc20faa89ab0f7e075c771416eb3f573e815014a1f3f.jpg)  
and  $\delta z$  (green), where the  $^{13}\mathrm{C}$  spins are fixed at the diamond-lattice solution. d, Plot of  $z$  versus  $r_{xy} = \sqrt{x^2 + y^2}$  for all lattice positions used in the DFT calculation from Nizovtsev et al. [33] (blue) and for the appropriately transformed  $^{13}\mathrm{C}$  coordinates found in this work (orange). Spins 5, 6, 9, 12 and 19 match a DFT lattice position, whereas the rest of the identified spins are outside the 510 lattice sites simulated. e, Measured electron-  $^{13}\mathrm{C}$  parallel (top) and perpendicular (bottom) hyperfine couplings for the five spins that are within the DFT calculation volume (red; from Supplementary Table 1), compared with the DFT results from ref. [33] (blue).

![](images/ea6fa15b33104fe56d6a75e3ba01444aa23d6c6739895cba9ac2e407a70a1af4.jpg)  
a

![](images/c4367fe9dc5f881865d9346398589d94064b891d605d7a318aaf3e3f276b8be6.jpg)  
b

![](images/c3294d1d51cec52fc7ef68c520be3e36852fa0ac6d73b5cf7fcfc5a8bd065874.jpg)  
C

![](images/1bff76afd9ec8613ba6e317266b8d96b488f3d31d0e5ebe0537a0b5f3622b0ef.jpg)

# Extended Data Fig. 5 | Aligning the magnetic field using a thermal echo

sequence. a, Pulse sequence used for the thermal echo measurement<sup>35</sup>. The electron spin is prepared in a superposition of the states  $m_{\mathrm{s}} = 0$  and  $m_{\mathrm{s}} = -1$  in the first half of the sequence and then swapped to a superposition of  $m_{\mathrm{s}} = 0$  and  $m_{\mathrm{s}} = +1$  for the second half, using a sequence of three closely spaced  $\pi$  pulses. By sweeping  $\tau$ , the average frequency  $f_{\mathrm{TE}} = (f_{+1} + f_{-1}) / 2$  is obtained, which is minimized when  $B_{\perp} = 0$ .  $f_{\pm 1}$  are the  $m_{\mathrm{s}} = 0 \leftrightarrow m_{\mathrm{s}} = \pm 1$  transition frequencies. The NV nitrogen spin is initialized in  $m_{\mathrm{l}} = 0$  (ref. <sup>34</sup>). b, Magnetic-field alignment by scanning the magnet position in two orthogonal directions. The obtained

thermal echo frequencies are fitted with a parabolic function to find the optimum position (that is,  $\mathrm{minimal}f_{\mathrm{TE}}$ ). The plots show the frequency difference  $f_{\mathrm{TE}} - 2.877652\mathrm{GHz}$ . c, The magnet is placed at the optimum position and the measurement is repeated 200 times (over a 10-h period). The obtained average frequency difference is  $0.13\mathrm{kHz}$ , with a standard deviation of  $0.27\mathrm{kHz}$  which is consistent with the statistical measurement error. Therefore, the total uncertainty for the magnet alignment is  $-0.4\mathrm{kHz}$ , which corresponds to a perpendicular field of  $0.5\mathrm{G}$  or a misalignment angle of  $0.07^{\circ}$ .