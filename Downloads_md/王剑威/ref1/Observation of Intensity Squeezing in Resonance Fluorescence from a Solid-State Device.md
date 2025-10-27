# Observation of Intensity Squeezing in Resonance Fluorescence from a Solid-State Device

Hui Wang, $^{1,2}$  Jian Qin, $^{1,2}$  Si Chen $^{1,2}$  Ming-Cheng Chen, $^{1,2}$  Xiang You, $^{1,2}$  Xing Ding, $^{1,2}$  Y.-H. Huo, $^{1,2}$  Ying Yu, $^{3}$  C. Schneider, $^{4}$  Sven Hofling, $^{1,4,5}$  Marlan Scully, $^{6,7,8}$  Chao-Yang Lu $^{1,2}$  and Jian-Wei Pan $^{1,2}$

$^{1}$ Hefei National Laboratory for Physical Sciences at Microscale, University of Science and Technology of China, Hefei 230026, China

$^{2}$ Shanghai Branch, CAS Center for Excellence and Synergetic Innovation Center in Quantum Information and Quantum Physics, University of Science and Technology of China, Shanghai 201315, China

${}^{3}$  State Key Laboratory of Optoelectronic Materials and Technologies,

School of Electronics and Information Technology, Sun Yat-sen University, Guangzhou 510000, China

$^{4}$ Technische Physik, Physikalisches Institut und Wilhelm Conrad Rontgen-Center for Complex Material Systems, Universität Würzburg, Am Hubland, D-97074 Würzburg, Germany

$^{5}$ SUPA, School of Physics and Astronomy, University of St. Andrews, St. Andrews KY16 9SS, United Kingdom

$^{6}$ Institute for Quantum Science and Engineering, Texas A&M University, College Station, Texas 77843, USA

$^{7}$ Department of Physics, Baylor University, Waco, Texas 76798, USA

$^{8}$ Department of Mechanical and Aerospace Engineering, Princeton University, Princeton, New Jersey 08544, USA

![](images/d91c30b76c8c4de9b2510945dda822b95d7eaab5c93815baa11b4a3439a06453.jpg)

(Received 27 June 2020; accepted 2 September 2020; published 7 October 2020)

Intensity squeezing—i.e., photon number fluctuations below the shot-noise limit—is a fundamental aspect of quantum optics and has wide applications in quantum metrology. It was predicted in 1979 that intensity squeezing could be observed in resonance fluorescence from a two-level quantum system. However, its experimental observation in solid states was hindered by inefficiencies in generating, collecting, and detecting resonance fluorescence. Here, we report the intensity squeezing in a single-mode fiber-coupled resonance fluorescence single-photon source based on a quantum dot-micropillar system. We detect pulsed single-photon streams with  $22.6\%$  system efficiency, which show sub-shot-noise intensity fluctuation with an intensity squeezing of  $0.59\mathrm{dB}$ . We estimate a corrected squeezing of  $3.29\mathrm{dB}$  at the first lens. The observed intensity squeezing provides the last piece of the fundamental picture of resonance fluorescence, which can be used as a new standard for optical radiation and in scalable quantum metrology with indistinguishable single photons.

DOI: 10.1103/PhysRevLett.125.153601

A fundamental tool in optical quantum information science is the single-photon source [1,2], which ideally should emit one, and only one, indistinguishable light quantum on demand. The absence of two-or-more-photon components gives rise to antibunching—a highly non-classical behavior—which is relevant for quantum cryptography applications [3]. The indistinguishability between independent single photons, which can be measured by two-photon Hong-Ou-Mandel quantum interference [4], lies at the heart of quantum teleportation [5], quantum networks [6], and linear optical quantum computing [7,8].

In principle, an ideal single-photon device is also useful for quantum metrology [9-11]. For example, there is a growing interest in redefining the international standard base unit of luminous intensity, the candela, by counting the number of fundamental light quanta, photons [12]. Compared to conventional light sources, such as lasers or light-emitting diodes, an ideal single-photon source has the unique quantum advantage that its intensity uncertainty can be greatly suppressed, thus offering a way to beat the

fundamental shot-noise limit [13,14]. Such a feature would find applications in various fields, such as imaging or measurement in the ultralow-power regime of light-sensitive biological samples [15,16].

While the high single-photon purity, indistinguishability, and extraction efficiency have been demonstrated [17-19], the simultaneous observation of intensity squeezing in a single-photon source remains challenging. This is due to the inevitable photon loss from generation, transmission, collection, and detection in experiments, such that, in each time slot, there is much more often vacuum rather than one photon detected. While the low overall efficiency only affects the data accumulation time in measurements of the single-photon purity and indistinguishability, the intensity squeezing, which heavily relies on the overall efficiency, can be diminished by the low efficiency and washed out in the presence of fluctuation of the experimental parameters. Therefore, there have rarely been observations of intensity squeezing in single-photon sources. The first observation, with a very small squeezing of  $\sim 0.00183 \pm 0.00038$  dB, dated back to 1983 from a single atom [13]. Recently, a

single molecule embedded inside a metallodielectric antenna was designed for a strong enhancement of photon collection efficiency and showed a squeezing of  $2.2\mathrm{dB}$  [20]. However, these single photons were not in a single mode, and due to the incoherent excitation, they were distinguishable. A related work reported intensity squeezing with confined polaritons in semiconductor micropillars [21].

Recently, semiconductor quantum dots embedded in microcavities emerged as a scalable solid-state platform for quantum information technologies [22,23]. Pulsed and resonant excitations of the single quantum dots were used to efficiently generate single photons with near-unity purity and indistinguishability [24]. Polarized microcavities were deterministically coupled to the emitters and efficiently funneled the single photons into a single spatial mode [19]. In all physical systems, the long-sought-after goal of observing intensity squeezing in pulsed resonance fluorescence remained a challenge. Here, we report the first single-mode fiber-coupled semiconductor source of indistinguishable single photons with subshot-noise intensity fluctuation.

The reduction of the intensity fluctuation in a single-photon source compared to the shot noise can be expressed as [20]

$$
\frac {N _ {\mathrm {S P S}}}{N _ {\mathrm {S N}}} = \sqrt {1 - \rho T}, \tag {1}
$$

where  $\rho$  is the internal efficiency of the quantum emitter (including its quantum efficiency and excited-state preparation efficiency), and  $T$  denotes the total external efficiency (including extraction efficiency and the overall transmission efficiency in the experiment setup). Due to the quantum uncertainty principle, when the uncertainty of the intensity is smaller than the shot noise, the uncertainty of its conjugate variable—phase—is accordingly increased.

In our experiment, we use a self-assembled semiconductor InAs/GaAs quantum dot coupled in a  $2 - \mu \mathrm{m}$ -diameter micropillar cavity. The sample is cooled at  $4\mathrm{K}$  where the emitter is resonant with the cavity, so that both the efficiency and indistinguishability are improved due to the Purcell effect. A confocal microscope is utilized to excite the emitter and collect resonance fluorescence single photons. A cross-polarization setup suppresses the laser leakage with an extinction ratio of  $\sim 10^{7}:1$ .

First, we study the resonance fluorescence single photons under continuous-wave (CW) laser excitation. Due to the high photon flux and the limited recovery time ( $\sim 5$  ns) of the superconducting nanowire single-photon detectors used, we attenuate the single-photon stream by 1000 times. The corrected single-photon count rate as a function of laser power is shown in Fig. 1(a), from which we extract a saturation power of  $P_{\mathrm{sat}} = 4.9 \mathrm{nW}$  and a saturated photon flux of  $I_{\infty} = (1.87 \pm 0.03) \times 10^{9} / \mathrm{s}$ . This is so far the

brightest single-photon source reported in any physical system.

A CW laser can prepare the emitter in its excited state with a maximal probability of  $50\%$  in the limit of high laser power [25]. The theoretically predicted single-photon flux is  $1 / 2T_{1}$ , where  $T_{1}$  is the excited-state lifetime. Figure 1(b) shows a time-resolved resonance fluorescence measurement which gives  $T_{1} = 58.60 \pm 0.02$  ps. Thus, the overall single-photon efficiency is  $I_{\infty} / (1 / 2T_{1}) = 0.219 \pm 0.004$ . Compared to the average lifetime of many quantum dots in the slab,  $T_{\mathrm{slab}} = 1.08$  ns, we estimate the Purcell factor to be  $\sim 18.4$ .

Next, we resonantly pump the quantum dot by a pulsed laser with a bandwidth of  $\sim 50\mathrm{GHz}$  to match the cavity mode. The detected single-photon counts show a Rabi oscillation as a function of excitation power, as plotted in Fig. 1(c). At  $\pi$  pulse, with a repetition rate of  $76\mathrm{MHz}$ , we finally detect  $17.2\times 10^{6}$  single photons per second on a superconducting nanowire single-photon detector with an efficiency of  $\sim 86\%$ . The corresponding overall single-photon efficiency is  $22.6\%$ , in good agreement with the value  $(21.9\%)$  extracted from the CW excitation.

The single-photon nature of generated resonance fluorescence is demonstrated by a Hanbury Brown and Twiss measurement that shows  $g_{2}(0) = 0.025(1)$  at a  $\pi$  pulse. Figure 1(d) is the measured high-resolution spectrum of the resonance fluorescence single photons, showing a full width at half maximum of  $2.74 \pm 0.02 \mathrm{GHz}$ . By fast Fourier transformation, the fitted coherent time is  $T_{2} = 108.8 \pm 0.9$  ps. This allows us to estimate that  $T_{2} / 2T_{1} = 0.928 \pm 0.008$ , indicating that the pulsed single photons are at  $92.8\%$  of the Fourier transform limit. This is in good agreement with the measured photon indistinguishability via Hong-Ou-Mandel interferences that show a corrected visibility of  $0.935(1)$  for two single photons separated by  $\sim 10 \mu \mathrm{s}$ .

We now examine the intensity squeezing of resonance fluorescence. The single photons are directly detected by a superconducting nanowire single-photon detector, and the arrival time is recorded by a time-to-digit converter. Figure 2(a) is the real-time monitoring of resonance fluorescence single-photon counts at  $\pi$  pulse with a time bin of  $1.0~\mu \mathrm{s}$ . The average count per time bin is  $17.5 / \mu \mathrm{s}$ . The corresponding histogram is plotted in Fig. 2(b). The directly observed standard deviation of photon counts is  $N_{\mathrm{SPS}} = 3.65$ , which is significantly below the shot-noise limit of  $N_{\mathrm{SN}} = \sqrt{17.48} = 4.18$ . Therefore, the directly measured intensity squeezing is  $N_{\mathrm{SPS}} / N_{\mathrm{SN}} = 87.32\%$  (0.59 dB) at the  $\pi$  pulse. This value is very close to, but slightly smaller than the theoretically predicted value of  $87.75\%$ . This is due to the imperfect recovery time of the detector (see the Supplemental Material). As a comparison experiment, we replace the single-photon source with a CW laser attenuated to an average count rate of  $\sim 17.2\times 10^{6}$  per second and send it into the same detector. The observed

![](images/b2027274092977dc54b3dcc45a9cd58d04703d5a15721837bafd7c5c1f1ba75b.jpg)

![](images/9bae05d55499d9bd15fab37a302f7d43ecd81f95aef96e47fc0a1df03c9eddfa.jpg)

![](images/51fa0bdfa4277815394d82b41552c1c0fd642206c6b670f3fe0508018015d674.jpg)  
FIG. 1. (a) Single-photon counts with CW laser resonant excitation. The saturation count is  $1.87 \times 10^{9}$  per second. The data are fitted by Eq. (8) in the Supplemental Material. (b) Time-resolved measurement of the resonance fluorescence by a superconducting nanowire single-photon detector with a time resolution of  $\sim 20$  ps. The fitted lifetime of the quantum dot is  $T_{1} = 58.60 \pm 0.02$  ps. Comparing this to the quantum dot lifetime in the slab ( $\sim 1.08$  ns), the Purcell factor is 18.4. (c) Rabi oscillation under pulsed resonant excitation. At  $\pi$  pulse,  $17.2 \times 10^{6}$  pure single photons are detected per second [22], by a superconducting nanowire single-photon detector with an efficiency of 0.86. (d) High-resolution spectrum of resonance fluorescence measured by a Fabry-Perot cavity with a frequency resolution of  $220\mathrm{MHz}$  and a free spectral range of  $37.4\mathrm{GHz}$ . The data is fitted by a Voigt function (red line), and the linewidth is  $2.74 \pm 0.02\mathrm{GHz}$ .

![](images/8304de3d751970483c6ef4fe77e7d3ab7c5e6e210128a66858ceda581bf0b19e.jpg)

standard deviation is  $99.98\%$  of the short noise limit. This indicates that the observed sub-shot-noise intensity fluctuation indeed comes from the single photons.

In Fig. 2(b), the occurrences at different single-photon counts are plotted (deep blue) and fitted by a binomial function (see the Supplemental Material [26]), which is

![](images/1cd68b90df0ccf2ff924423ac9eab103156e37d591e7ba2907a3c38bf475f177.jpg)  
FIG. 2. (a) Real-time monitoring of resonance fluorescence single-photon counts at  $\pi$  pulse with a time bin of  $1.0\mu s$ . The average count per time bin is  $17.5 / \mu s$ . (b) The corresponding histogram, where the frequency of observed counts (i.e., the intensity fluctuation, shown as deep blue dots) is fitted by a binomial function. Comparing this to the shot-noise-limited source with the same intensity (green line), the quantum dot single-photon source shows a  $12.68\%$  reduction of histogram linewidth—that is, intensity fluctuation noise. The blue line displays the corrected intensity squeezing at the first lens (see the main text). (c) Intensity squeezing parameter as a function of the excitation laser amplitude. At  $\pi$  pulse, the intensity squeezing reaches a minimal value of  $87.32\%$ . The black dotted line is the normalized shot-noise limit.

![](images/2c555f2f94fd16d3fdb046a5f48b423d39b38f49c7a8e0b98ad9f5793a557424.jpg)

![](images/7715dd6d292ca12f10e43a7e3944e394894de1cdbd9e2004016488724eecf38d.jpg)

reduced by  $12.68\%$  compared to the shot-noise limit (green). Considering the optical transmission loss, cross-polarization filtering loss, coupling loss into the single-mode fiber, and the detection efficiency at the detector, the intensity squeezing out of the first lens should be 3.29 dB (light blue). Figure 2(c) shows the amount of intensity squeezing as a function of the excitation laser amplitude. As expected, by tuning the laser power gradually to  $\pi$  pulse, the excited-state population—proportional to the single-photon generation efficiency—grows, which increases the amount of intensity squeezing.

It is clear that the intensity squeezing critically relies on the overall efficiency. We analyze the photon loss budget in detail. First, we estimate the external efficiency, which accounts for all photon loss from the first lens to the single-photon detector: collection efficiency by the first objective, polarization filtering, single-mode fiber coupling, and detection. To estimate the single-mode fiber coupling efficiency, we performed a separate experiment using multimode fibers (with diameters of  $100\mu \mathrm{m}$  and  $200\mu \mathrm{m}$ , which give the same counts, indicating the efficiency is saturated and equal to unity). The ratio of the single-photon count using a single-mode fiber is measured to be  $74\%$  of that using multimode fibers, which determines the single-mode coupling efficiency. The overall transmission efficiency of the optical path (including the first lens, optical window, polarized beam splitter, and two wave plates) is measured to be  $83\%$ . The first lens collection efficiency is estimated to be  $78\%$ . The superconducting nanowire single-photon detection efficiency is  $86\%$ . The micropillar cavity shows a small mode splitting due to a slight ellipticity of its cross section. In this case, the intensity of one eigenmode will be higher than that of another one [28]. By measuring the single-photon counts in two modes respectively, the determined polarization filtering efficiency is  $55\%$ .

The internal efficiency of the quantum dot-micropillar system includes the quantum efficiency of the emitter (QE), excited-state preparation efficiency (ESPE), and the photon extraction efficiency (PEE) of the micropillar. The QE and ESPE can be affected by power-induced [29] and phonon-induced damping [30] in quantum dots. The PEE accounts for the losses due to the side leakage and the part not coupled to the fundamental mode of the microcavity, which can be estimated by [31]

$$
\eta_ {c} = \frac {F _ {p}}{F _ {p} + 1} \frac {Q}{Q _ {0}}, \tag {2}
$$

where  $F_{p}$  is the Purcell factor,  $Q$  is the quality factor, and  $Q_{0}$  is the quality factor of the planar microcavity. In this experiment,  $F_{p} = 18.4$ ,  $Q = 6800$ , and  $Q_{0} = 7600$ , so the photon extraction efficiency by the microcavity is  $\sim 85\%$ . This result is consistent with the numerically simulated

number of  $87\%$  using the finite difference time domain. The product of QE and ESPE is estimated to be  $92\%$ .

In summary, we have directly observed the first intensity squeezing in pulsed resonance fluorescence, in a single-mode fiber-coupled highly indistinguishable solid-state single-photon source. The uncorrected squeezing at the output of the single-mode fiber is  $0.59\mathrm{dB}$ , and the corrected intensity squeezing at the first lens is  $3.29\mathrm{dB}$ . From a fundamental perspective, our work fills a long-sought-after missing element in textbook quantum optical phenomena [25] using quantum dots. This is addition to the previously reported antibunching [32], two-photon interference [33], weak [28] and strong [34,35] coupling, Rabi oscillation [36], Autler-Townes splitting [37], coherent population trapping [38], Mollow triplet [39,40], and quadrature squeezing [41]. For practical applications, our work combines for the first time high levels of single-photon efficiency, purity, and indistinguishability together with intensity squeezing in a semiconductor chip. The intensity squeezing can be further improved by driving the quantum dot with dichromatic laser pulses [42] and/or coupling the quantum dot to polarized microcavities [19]. We note that such an intensity-squeezed single-photon source with subshot noise fluctuations has natural application in benchmarking single-photon detector efficiency [43], redefining the standard base unit of luminous intensity at an ultralow power level [44], and the optical spectroscopy of light-sensitive biological samples [15,16].

This work was supported by the National Natural Science Foundation of China (No. 91836303), the National Key R&D Program of China (No. 2019YFA0308701), the Chinese Academy of Science, the Anhui Initiative in Quantum Information Technologies, the Science and Technology Commission of Shanghai Municipality (Grant No. 2019SHZDZX01), and the State of Bavaria.

H. W., J. Q., S. C., and M.-C. C. contributed equally to this work.

[1] B. Lounis and M. Orrit, Rep. Prog. Phys. 68, 1129 (2005).  
[2] A.J. Shields, Nat. Photonics 1, 215 (2007).  
[3] C. H. Bennett and G. Brassard, Theor. Comput. Sci. 560, 7 (2014).  
[4] C.-K. Hong, Z.-Y. Ou, and L. Mandel, Phys. Rev. Lett. 59, 2044 (1987).  
[5] C. H. Bennett, G. Brassard, C. Crépeau, R. Jozsa, A. Peres, and W. K. Wootters, Phys. Rev. Lett. 70, 1895 (1993).  
[6] H. J. Kimble, Nature (London) 453, 1023 (2008).  
[7] P. Kok, W. J. Munro, K. Nemoto, T. C. Ralph, J. P. Dowling, and G. J. Milburn, Rev. Mod. Phys. 79, 135 (2007).  
[8] J.-W. Pan, Z.-B. Chen, C.-Y. Lu, H. Weinfurter, A. Zeilinger, and M. Zukowski, Rev. Mod. Phys. 84, 777 (2012).  
[9] A.N. Boto, P. Kok, D.S. Abrams, S.L. Braunstein, C.P. Williams, and J. P. Dowling, Phys. Rev. Lett. 85, 2733 (2000).

[10] V. Giovannetti, S. Lloyd, and L. Maccone, Phys. Rev. Lett. 96, 010401 (2006).  
[11] V. Giovannetti, S. Lloyd, and L. Maccone, Nat. Photonics 5, 222 (2011).  
[12] J. Cheung, C. Chunnilall, E. Woolliams, N. Fox, J. Mountford, J. Wang, and P. Thomas, J. Mod. Opt. 54, 373 (2007).  
[13] R. Short and L. Mandel, Phys. Rev. Lett. 51, 384 (1983).  
[14] L. Mandel, Opt. Lett. 4, 205 (1979).  
[15] M. A. Taylor, J. Janousek, V. Daria, J. Knittel, B. Hage, H.-A. Bachor, and W. P. Bowen, Nat. Photonics 7, 229 (2013).  
[16] R. Tenne, U. Rossman, B. Rephael, Y. Israel, A. Krupinski-Ptaszek, R. Lapkiewicz, Y. Silberberg, and D. Oron, Nat. Photonics 13, 116 (2019).  
[17] X. Ding et al., Phys. Rev. Lett. 116, 020401 (2016).  
[18] N. Somaschi et al., Nat. Photonics 10, 340 (2016).  
[19] H. Wang et al., Nat. Photonics 13, 770 (2019).  
[20] X.-L. Chu, S. Götzinger, and V. Sandoghdar, Nat. Photonics 11, 58 (2017).  
[21] T. Boulier et al., Nat. Commun. 5, 3260 (2014).  
[22] H. Wang et al., Phys. Rev. Lett. 123, 250503 (2019).  
[23] P. Senellart, G. Solomon, and A. White, Nat. Nanotechnol. 12, 1026 (2017).  
[24] Y.-M. He, Y. He, Y.-J. Wei, D. Wu, M. Atature, C. Schneider, S. Hofling, M. Kamp, C.-Y. Lu, and J.-W. Pan, Nat. Nanotechnol. 8, 213 (2013).  
[25] M. O. Scully and M. S. Zubairy, Quantum Optics (Cambridge University Press, Cambridge, England, 1997).  
[26] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.125.153601 for detailed descriptions of the intensity squeezing, the RF single photon, and the effect of an imperfect detector, which includes Ref. [27].  
[27] D.F. Walls and G.J. Milburn, Quantum Optics (Springer-Verlag, Berlin Heidelberg, 2008).  
[28] J.M. Gérard, B. Sermage, B. Gayral, B. Legrand, E. Costard, and V. Thierry-Mieg, Phys. Rev. Lett. 81, 1110 (1998).

[29] D. Mogilevtsev, A. P. Nisovtsev, S. Kilin, S. B. Cavalcanti, H. S. Brandi, and L. E. Oliveira, Phys. Rev. Lett. 100, 017401 (2008).  
[30] A. J. Ramsay, A. V. Gopal, E. M. Gauger, A. Nazir, B. W. Lovett, A. M. Fox, and M. S. Skolnick, Phys. Rev. Lett. 104, 017402 (2010).  
[31] W. Barnes, G. Björk, J. Gérard, P. Jonsson, J. Wasey, P. Worthing, and V. Zwiller, Eur. Phys. J. D 18, 197 (2002).  
[32] P. Michler, A. Kiraz, C. Becher, W. Schoenfeld, P. Petroff, L. Zhang, E. Hu, and A. Imamoglu, Science 290, 2282 (2000).  
[33] C. Santori, D. Fattal, J. Vučković, G. S. Solomon, and Y. Yamamoto, Nature (London) 419, 594 (2002).  
[34] T. Yoshie, A. Scherer, J. Hendrickson, G. Khitrova, H. Gibbs, G. Rupper, C. Ell, O. Shchekin, and D. Deppe, Nature (London) 432, 200 (2004).  
[35] J. P. Reithmaier, G. Sek, A. Löffler, C. Hofmann, S. Kuhn, S. Reitzenstein, L. V. Keldysh, V. D. Kulakovskii, T. L. Reinecke, and A. Forchel, Nature (London) 432, 197 (2004).  
[36] T. H. Stievater, X. Li, D. G. Steel, D. Gammon, D. S. Katzer, D. Park, C. Piermarocchi, and L. J. Sham, Phys. Rev. Lett. 87, 133603 (2001).  
[37] X. Xu, B. Sun, P.R. Berman, D.G. Steel, A.S. Bracker, D. Gammon, and L.J. Sham, Science 317, 929 (2007).  
[38] X. Xu, B. Sun, P.R. Berman, D.G. Steel, A.S. Bracker, D. Gammon, and L. Sham, Nat. Phys. 4, 692 (2008).  
[39] A. N. Vamivakas, Y. Zhao, C.-Y. Lu, and M. Atatüre, Nat. Phys. 5, 198 (2009).  
[40] E. B. Flagg, A. Muller, J. Robertson, S. Founta, D. Deppe, M. Xiao, W. Ma, G. Salamo, and C.-K. Shih, Nat. Phys. 5, 203 (2009).  
[41] C. H. Schulte, J. Hansom, A. E. Jones, C. Matthiesen, C. Le Gall, and M. Atature, Nature (London) 525, 222 (2015).  
[42] Y.-M. He et al., Nat. Phys. 15, 941 (2019).  
[43] R. H. Hadfield, Nat. Photonics 3, 696 (2009).  
[44] S. V. Polyakov and A. L. Migdall, J. Mod. Opt. 56, 1045 (2009).