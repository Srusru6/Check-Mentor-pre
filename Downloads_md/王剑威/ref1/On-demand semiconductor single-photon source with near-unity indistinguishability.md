# On-demand semiconductor single-photon source with near-unity indistinguishability

Yu-Ming He $^{1}$ , Yu He $^{1}$ , Yu-Jia Wei $^{1}$ , Dian Wu $^{1}$ , Mete Atature $^{1,2}$ , Christian Schneider $^{3}$ , Sven Höfling $^{3\star}$ , Martin Kamp $^{3}$ , Chao-Yang Lu $^{1,2\star}$  and Jian-Wei Pan $^{1\star}$

Single-photon sources based on semiconductor quantum dots offer distinct advantages for quantum information, including a scalable solid-state platform, ultrabrightness and interconnectivity with matter qubits. A key prerequisite for their use in optical quantum computing and solid-state networks is a high level of efficiency and indistinguishability. Pulsed resonance fluorescence has been anticipated as the optimum condition for the deterministic generation of high-quality photons with vanishing effects of dephasing. Here, we generate pulsed single photons on demand from a single, microcavity-embedded quantum dot under s-shell excitation with 3 ps laser pulses. The  $\pi$  pulse-excited resonance-fluorescence photons have less than  $0.3\%$  background contribution and a vanishing two-photon emission probability. Non-postselective Hong-Ou-Mandel interference between two successively emitted photons is observed with a visibility of 0.97(2), comparable to trapped atoms and ions. Two single photons are further used to implement a high-fidelity quantum controlled-NOT gate.

Single photons have been proposed as promising quantum bits (qubits) for quantum communication<sup>1</sup>, linear optical quantum computing<sup>2,3</sup> and as messengers in quantum networks<sup>4</sup>. These proposals primarily rely on a high degree of indistinguishability between individual photons to obtain the Hong-Ou-Mandel (HOM) type interference<sup>5</sup> that is at the heart of photonic controlled logic gates and photon-interference-mediated quantum networking<sup>1-4</sup>.

Of the different types of single-photon emitters $^{6,7}$  that are available, quantum dots are considered attractive as solid-state devices because they can be embedded into high-quality nanostructure cavities and waveguides to generate ultra-bright sources of single and entangled photons $^{7-10}$ . Quantum dots also provide a light/matter interface $^{11-13}$  and, in principle, can be scaled to large quantum networks $^{14}$ . Two-photon HOM interference experiments using photons from a single quantum dot $^{15-17}$ , as well as from independent sources $^{18,19}$ , have not only demonstrated the potential of quantum dots as single-photon sources, but have also revealed the level of dephasing arising from incoherent excitation. The method of incoherent pumping (via above bandgap or  $p$ -shell excitation) typically produces reduced photon coherence times due to homogeneous broadening of the excited state $^{16}$  and uncontrolled emission time jitter from the non-radiative high-level to  $s$ -shell relaxation $^{20}$ , leading to a decrease in photon indistinguishability.

To eliminate these dephasings, significant effort has been devoted to s-shell resonant optical excitation of quantum dots. The Mollow triplet spectra and photon correlations of the resonance fluorescence (RF) have been measured[21-24]. Under continuous-wave (c.w.) laser excitation, a high degree of indistinguishability for continuously generated RF photons has been demonstrated through post-selective HOM interference[25]. However, in the c.w. regime, because the emission time of the RF photons is uncontrolled, the HOM interference relies on finite single-photon detection time resolution to discriminate and postselect the small fraction of photons that overlap on the beamsplitter at the same time[25-27]. Accordingly, the obtained interference visibility needs to be convoluted with—and is thus limited by—the realistic

detection time response. This limitation, together with the low efficiency of two-photon interference arising due to the unsynchronized photon arrival time, prohibits the direct application of c.w. RF photons in many quantum information protocols $^{1-4}$ . More recent experiments operating in the low excitation regime have shown that the coherent scattering part of the RF could have a coherence comparable to the excitation laser $^{28,29}$ . However, such a single-photon source would suffer from an intrinsically low efficiency.

It has been anticipated $^{17-20,25}$  that pulsed and resonant  $s$ -shell excitation could remedy the above problems and be used for the deterministic generation of time-tagged, highly indistinguishable single photons. In addition, the pulsed and transition-selective RF single photons are also a prerequisite for the much sought-after goal of entangling distant quantum dot spins through photon interference $^{4,30}$ , as well as for the scheme of generating on-demand multiphoton cluster states $^{31}$ . Earlier experiments $^{21,32}$  have used pulsed resonant excitation to demonstrate Rabi oscillation, a hallmark for quantum optics. However, access to a background-free on-demand single-photon source with near-unity indistinguishability has proven elusive.

In this Article, by applying resonant  $s$ -shell optical excitation with picosecond laser pulses we have generated pulsed RF single photons on demand from a single quantum dot embedded in a planar microcavity. Rabi oscillations are visible from the variation of the RF intensity as a function of pump pulse area. Under deterministic  $\pi$ -pulse excitation, the RF photons have less than  $0.3\%$  background contributions and show an antibunching of  $g^2(0) = 0.012(2)$ . We observe non-postselective HOM interference with a raw visibility of 0.91(2) and corrected visibility of 0.97(2) for two RF photons excited by two successive  $\pi$  pulses separated by 2 ns. Finally, the highly indistinguishable RF photons are utilized to demonstrate a quantum controlled-NOT gate.

# Pulsed resonance fluorescence

Our experiments were performed on self-assembled InGaAs quantum dots, which were embedded in a planar microcavity and

![](images/fed6b898f3b63808d3f8bc2b91ed46dbe293676f95607d49ec79a805d0e23a08.jpg)

![](images/065ca8fe0dffe156ce9b087bf2632b3c7a550803d462c0ffd43398212ff7f46c.jpg)  
Figure 1 | Rabi oscillation and antibunching. a, RF intensity versus square root of incident power. The grey line is a guide to eye. Although excitation-induced damping of the Rabi oscillation (there has been an intense debate on its mechanism; see, for example, ref. 36) is visible at higher powers, a  $\pi$ -pulse excitation is obtained with reasonable quality. Our current work only focuses on the  $\pi$ -pulse regime. b, Intensity-correlation histogram of the RF emission from the quantum dot under pulsed s-shell excitation obtained using a Hanbury Brown and Twiss-type set-up. The second-order correlation  $g^{2}(0) = 0.012(2)$  is calculated from the integrated photon counts in the zero time delay peak divided by the average of the adjacent six peaks, and its error (0.002), which denotes one standard deviation, is deduced from propagated Poissonian counting statistics of the raw detection events.

cooled in a cryogen-free bath cryostat at  $4.2\mathrm{K}$  (Supplementary Fig. S1). Laser excitation of a single quantum dot and collection of the emitted fluorescence were carried out with a confocal microscope. The excitation laser was pulsed with a nominal pulse width of 3 ps. The microscope was operated in a cross-polarization configuration, whereby a polarizer is placed in the collection arm with its polarization perpendicular to the excitation light, extinguishing the scattered laser by a factor exceeding  $10^{6}$ . The microcavity had a quality factor of  $\sim 200$ , which increased the fluorescence collection efficiency and reduced the laser power required for excitation of the quantum dots.

Figure 1a shows the detected RF photon counts as a function of the square root of the excitation laser power. The oscillation of the RF intensity is due to the well-known Rabi rotation between the

ground state and the excitonic state. This has been demonstrated previously by quasi-resonant $^{33-35}$  or resonant $^{21,32}$  driving. The RF intensity reaches its first peak at the  $\pi$  pulse. We excited the quantum dot with  $\pi$  pulses at a repetition rate of  $\sim 82\mathrm{MHz}$  and observed  $\sim 230,000$  photon counts on a single-photon detector (with an efficiency of  $22\%$ ). The overall RF collection efficiency was  $\sim 1.3\%$ . After correcting for the fibre coupling efficiency ( $\sim 45\%$ ), polarizer ( $\sim 50\%$ ) and beamsplitter ( $\sim 95\%$ ), we estimate that  $\sim 6\%$  of the photons emitted by the quantum dot were collected into the first lens, which is in good agreement with numerical simulations (see Supplementary Information). To verify that this is indeed a single-photon source, Fig. 1b shows the second-order correlation measurement of the  $\pi$  pulse-driven RF photons. At zero delay, it shows a clear antibunching with a vanishing multiphoton probability of  $g^{2}(0) = 0.012(2)$ . Thus it can be concluded that one and only one RF photon is generated on demand from every  $\pi$ -pulse excitation. However, the photon extraction efficiency needs to be improved drastically for this source to become a deterministic single-photon source.

Figure 2a shows a linear-log plot of the pulsed RF (the sharp central line) together with the residual laser leakage (the broadband feature fitted by the red line), monitored on a spectrometer. Taking advantage of the huge linewidth mismatch between the RF signal and the laser background, we passed the RF through an etalon with a bandwidth of  $\sim 20\mathrm{GHz}$  much wider than that of the RF photons and much narrower than that of the pulsed laser—to further suppress the excitation laser background. This results in a clean RF spectrum, as shown in the inset of Fig. 2a, with an improvement of the signal to background (including the detector dark counts) ratio from 20 to 357 at  $\pi$  pulse excitation. For a range of laser powers, the signal to background ratio was extracted and plotted in Fig. 2b.

A typical example of high-resolution spectra of the pulsed RF measured using a Fabry-Perot scanning cavity is shown in Fig. 2c. It shows a pronounced deviation from the Lorentzian lineshape obtained from c.w. excitation, as shown in Supplementary Fig. S2, and can be fitted with a Voigt profile with a homogeneous linewidth of  $0.4(1)\mathrm{GHz}$  (corresponding to  $T_{2} = 0.7(2)\mathrm{ns}$ ) and an inhomogeneous linewidth of  $1.0(1)\mathrm{GHz}$ . The spontaneous emission lifetime for this quantum dot was measured to be  $T_{1} = 0.41(2)\mathrm{ps}$  (Supplementary Fig. S3), and we estimate a pure dephasing time of  $T_{2}^{*} = 5.7_{3.8}^{\infty}\mathrm{ns}$ . The Gaussian component in this Voigt profile might be caused by spectral diffusion due to pulsed-laser-induced charge fluctuations in the vicinity of the quantum dot (trapping and untrapping of charges in nearby defects and impurities)[37-39]. The inhomogeneous linewidth varies for different quantum dots and typically shows an increase at larger excitation power (Supplementary Fig. S3), which is in qualitative agreement with previous investigations of light-induced spectral diffusion[37].

# Two-photon quantum interference

To perform pulsed two-photon interference, we adopted a similar experimental configuration (Fig. 3a) to that used in ref. 15. Each excitation laser pulse, originally separated by  $\sim 12.5$  ns, was further split into two pulses with a  $2\mathrm{ns}$  delay. Thus, every  $\sim 12.5$  ns, the quantum dot was excited twice, generating two successive single RF photons. The output RF photons were then fed into an unbalanced Mach-Zehnder interferometer with a  $2\mathrm{ns}$  path-length difference (Fig. 3a). The two outputs of this interferometer were detected by single-mode fibre-coupled single-photon counters, and a record of coincidence events was kept to build up a time-delayed histogram (for more details see Supplementary Fig. S4).

Figure 3b,c shows the central cluster of the histogram when the two  $\pi$  pulse-excited single photons, before recombining in the last beamsplitter, were prepared in cross and parallel polarization states, respectively. The five peaks, from left to right, correspond, respectively, to the cases where the two photons arrive at the beamsplitter with a time delay of  $-4$ ,  $-2$ ,  $0$ ,  $2$  and  $4$  ns. For

![](images/19bcc46b1b375081768bb7dc0c6ae5c62eea15375023c7ce78d4ffef61b1009a.jpg)  
Figure 2 | Spectra of the pulsed RF. a, Example of the pulsed RF displayed on a spectrometer and plotted using a linear-log scale. The excitation laser profile (fitted by the red line) is much broader than the RF signal, enabling a second-stage of background filtering based on frequency (see text) that is not possible in the c.w. case. Inset: spectrum after passing the RF photons through a 20 GHz etalon to eliminate the residual laser background. b, Pulsed RF signal-to-background ratio for a range of excitation powers with and without filtering. c, High-resolution RF spectrum when excited by a  $\pi$  pulse. The red line was fitted using a Voigt profile.

![](images/a1d4e822c4b931f2425ad7f6055e16a7123e8e1628227803acbe18fb2750c7a3.jpg)

![](images/b41fa74b741167aa6245a9b28203f99390946f478666a21c463b3c58df05af18.jpg)

![](images/8195ca4f112934799d1068d17dc9c70eabf3a1b0c86bb1a88aff6c24ac301b2b.jpg)

![](images/22be2f68e901c108268c1af0ccdec7ef546ca74ad11efc7be7ab0c32e1ce12e8.jpg)  
Figure 3 | Non-postselective HOM-type interference between two pulsed RF single photons. a, Two unbalanced Mach-Zehnder interferometers with a path-length difference of 2 ns are used both in the excitation arm (not shown) and in the two-photon interference. b,c, The central cluster of the histogram (Supplementary Fig. S4 shows the full histogram) of two-photon detection events with a relative delay time. In b and c, the input two photons are  $\pi$ -pulse excited and prepared in cross and parallel polarizations, respectively. The fitting function for each peak is the convolution of a double exponential decay (exciton decay response) with a Gaussian (single-photon detector time response). Owing to the limited time response, the five peaks have finite overlaps. The area of the fitted central peaks bounded by the red line in b and the blue line in c, respectively, are extracted and used to calculate the visibility.

![](images/e7a987b4fa847acdf704aa723b98d52f6e0a8c099d12442b3696b1a70fba0c57.jpg)

distinguishable photons with different polarization, the expected peak area ratio is 1:2:2:2:1, which is in good agreement with Fig. 3b.

If two perfectly indistinguishable photons are superposed on a beamsplitter, they will always exit the beamsplitter together through the same output port, leading to a zero coincidence rate (the HOM dip<sup>5</sup>, which cannot be explained by classical optics). Figure 3c shows a strong suppression of the coincidence counts at zero delay when the two incoming photons are prepared in the same polarization state. Quantitative evaluation (see the caption of Fig. 3 for details) shows that the probability of the two photons exiting the same channel in a two-photon Fock state (bunching) is  $95.4\%$ . This corresponds to a raw two-photon HOM interference visibility of 0.91(2).

Taking into account the residual two-photon emission probability  $g^{2}(0) = 0.012(2)$  and the optical imperfections of our interferometric set-up (which are measured independently),  $R / T = 1.01$  and  $(1 - \varepsilon) = 0.98$  (where  $R$  and  $T$  are the reflectivity and transmittivity of the beamsplitter and  $(1 - \varepsilon)$  is the first-order interference visibility of the Mach-Zehnder interferometer tested with a c.w. laser), we obtain the corrected degrees of indistinguishability to be 0.97(2). The visibility can be further increased slightly by decreasing the excitation laser power. On another quantum dot, we tested the HOM interference with  $\pi$ , 0.72π and 0.41π pulse excitation and observe visibilities of 0.96(6), 0.97(6) and 0.99(4), respectively (see the data in Supplementary Fig. S4).

Taken together, these are the highest visibilities reported so far for quantum dot-based single-photon sources. These results demonstrate that solid-state pulsed RF single photons in quick

succession are highly indistinguishable, at a level comparable to the best results achieved using well-developed systems such as parametric downconversion $^{1}$ , trapped atoms and ions $^{40-43}$ . The high visibility results indicate a reduction of fast dephasing and elimination of the emission time jitter associated with the pulsed RF when compared with previous incoherent excitation methods. The pure dephasing time  $T_{2}^{*} = 5.7_{3.8}^{\infty}$  ns is considerably larger than 2 ns, and thus should have little effect on the visibility. The spectral diffusion (as shown in Fig. 2c) should also happen at a timescale much longer than the 2 ns separation, which is consistent with previous experiments $^{15,16,37,39}$ .

# Controlled-NOT gate with single photons

We now demonstrate how the on-demand RF single photons can be utilized to implement a quantum controlled-NOT (CNOT) gate. The quantum CNOT gate is a fundamental two-qubit logic gate. If the control qubit is in logic  $|0\rangle_{c}$ , nothing happens to the target qubit, whereas if the control qubit is in logic  $|1\rangle_{c}$ , the target qubit will flip  $(|0\rangle_{t} \rightarrow |1\rangle_{t}, |1\rangle_{t} \rightarrow |0\rangle_{t})$ . The photonic CNOT gate is a basic building block for quantum computing and has been demonstrated many times with downconverted photons[44-47] and, very recently, with  $p$ -shell excited single photons from quantum dots[48].

We prepared two input qubits encoded in the polarization states of the pulsed RF single photons  $|\alpha \rangle_{\mathrm{t}} = a|H\rangle_{\mathrm{t}} + b|V\rangle_{\mathrm{t}}$  and  $|\beta \rangle_{\mathrm{c}} = c|H\rangle_{\mathrm{c}} + d|V\rangle_{\mathrm{c}}$ , where  $H(V)$  denotes horizontal (vertical) polarization and is used to encode 0(1). The two inputs were then fed into the optical circuit for CNOT operation, as shown in Fig. 4a.

![](images/f175f663d616a6dd2d0dbfbb124cdb8ee012e4329a434472a7d3ee69c2f7b1b0.jpg)  
a

![](images/3847bdeda552c739ed40051e7b162da4223272dae0cc9d953d32644dcabeb993.jpg)  
Figure 4 | Realization of a quantum CNOT gate using pulsed RF single photons. a, Optical circuit. The control and target qubits are from the two successively emitted RF photons with a 2 ns delay. The half-wave plates (HwPs) placed at  $\theta = 45^{\circ}$  and  $\theta = 22.5^{\circ}$  are used to realize the unitary rotation:  $|H\rangle \rightarrow \cos(2\theta)|H\rangle + \sin(2\theta)|V\rangle$ ,  $|V\rangle \rightarrow \sin(2\theta)|H\rangle - \cos(2\theta)|V\rangle$ . b,c, Experimentally measured truth table. The coincident count rates are converted to probabilities by normalizing them with the sum of coincidence counts obtained for the respective input state. Ideally, the CNOT truth table in the ZZ basis should give a unity possibility for the input-output combination  $HH \rightarrow HH$ ,  $HV \rightarrow HV$ ,  $VH \rightarrow VV$  and  $VV \rightarrow VH$ , and zero possibility for others. Similarly, in the XX basis, there should be only  $++ \rightarrow ++$ ,  $+- \rightarrow --$ ,  $-- \rightarrow --$ ,  $-- \rightarrow --$ ,  $-- \rightarrow --$ ,  $(|\pm\rangle = (1/\sqrt{2})(|H\rangle \pm |V\rangle)$ . The unwanted combinations are mainly caused by imperfections of the optical elements and the remaining distinguishability of the single photons.

![](images/c489b0b021d7ff3e68f1147f2eaf4bc55c3da43cb0b9f260f9a6599f352eb82d.jpg)

The key element in this optical network is a partial polarizing beamsplitter ( $p$ -PBS) which has a transmission of  $1(1/3)$  and a reflectivity of  $0(2/3)$  for the  $H(V)$  photons. When the two single photons are superimposed on the  $p$ -PBS as shown in Fig. 4a, and if one and only one photon leaves through each output channel, the composite state of the two output photons can be written as

$$
\begin{array}{l} a c | H \rangle_ {\mathrm {t}} | H \rangle_ {\mathrm {c}} + \sqrt {\frac {1}{3}} a d | H \rangle_ {\mathrm {t}} | V \rangle_ {\mathrm {c}} + \sqrt {\frac {1}{3}} b c | V \rangle_ {\mathrm {t}} | H \rangle_ {\mathrm {c}} \\ + \left(\sqrt {\frac {1}{3}} \sqrt {\frac {1}{3}} - \sqrt {\frac {2}{3}} \sqrt {\frac {2}{3}}\right) b d | V \rangle_ {\mathrm {t}} | V \rangle_ {\mathrm {c}} \tag {1} \\ \end{array}
$$

The first term corresponds to the case in which both input photons are  $|H\rangle$  and fully transmitted. The second and third terms correspond to the cases where one photon is in  $|H\rangle$  and fully transmitted while the other photon is in  $|V\rangle$  and partially  $(1 / 3)$  transmitted. It is most important to note the last term  $|V\rangle_{\mathrm{t}}|V\rangle_{\mathrm{c}}$ , where the resulting minus sign of the probability amplitude  $(-1 / 3)$  is due to the quantum interference between two indistinguishable paths, and both photons are transmitted  $(\sqrt{1 / 3}\sqrt{1 / 3})$  or reflected  $(-\sqrt{2 / 3}\sqrt{2 / 3})$ , which requires the indistinguishability of the single photons.

Next, we swap the  $H$  and  $V$  polarizations in equation (1) using half-wave plates and pass the two photons through two other  $p$ -PBSs to compensate the unbalanced coefficient (Fig. 4a), and we can obtain  $(1/3)(ac|H\rangle_{\mathrm{t}}|H\rangle_{\mathrm{c}} + ad|H\rangle_{\mathrm{t}}|V\rangle_{\mathrm{c}} + bc|V\rangle_{\mathrm{t}}|H\rangle_{\mathrm{c}} - bd|V\rangle_{\mathrm{t}}|V\rangle_{\mathrm{c}})$ . This effectively realizes a controlled phase-flip gate with a success probability of  $1/9$ . Finally, after applying two additional Hadamard rotations, it can be transformed into the CNOT gate (see the caption of Fig. 4a and refs 2 and 47 for more details).

We experimentally evaluated the performance of the quantum CNOT gate using an efficient method proposed by Hofmann49. To show the quantum behaviour of the CNOT gate, it was tested for different combinations of input-output states using complementary bases, that is, in both the computational basis \((|0\rangle /|1\rangle)\) and their linear superpositions \((|\pm \rangle = (1 / \sqrt{2})(|0\rangle \pm |1\rangle))\) which are referred to as the ZZ and XX basis using the Pauli matrix language. In the ZZ basis, the CNOT is expected to flip the target qubit if the control qubit is in logic 1. Interestingly, in the XX basis, the target and control qubits are reversed; the control qubit will flip if the target qubit is logic 1. The measurement results of the input-output probabilities of the CNOT gate in the ZZ basis and in the XX basis are shown in Fig. 4b and c, respectively. The fidelity of the CNOT operation (defined as the probability of obtaining the correct output averaged over all four possible inputs) in the XX basis is \(0.9999999999999999999999999999999999999999999999999999999999999999999999999999999999

ZZ basis is  $F_{zz} = 0.85(6)$ , and in the XX basis is  $F_{xx} = 0.85(7)$ . These two complementary fidelities ( $F_{zz}$  and  $F_{xx}$ ) are sufficient to give an upper and lower bound for the full quantum process fidelity  $F_{\mathrm{proc}}$  of the gate according to  $(F_{zz} + F_{xx} - 1) \leq F_{\mathrm{proc}} \leq \min(F_{zz}, F_{xx})$ . Thus, here we have  $0.70(9) \leq F_{\mathrm{proc}} \leq 0.85(7)$ . The process fidelity is directly related to the quantum entangling capability of the CNOT gate; that is, the CNOT gate can produce entangled states from unentangled input states<sup>49</sup>. Here,  $F_{\mathrm{proc}}$  clearly surpasses the threshold of 0.5 that is sufficient to confirm the entangling capability of our CNOT gate.

# Conclusions and outlook

In this Article, we have demonstrated the on-demand generation of near background-free ( $\sim 99.7\%$  purity) and highly indistinguishable RF single photons from a quantum dot in a planar microcavity driven by resonant  $\pi$  pulses. Using two RF photons emitted in 2 ns succession, non-postselective HOM two-photon interference has revealed near-unity visibilities ( $\sim 97\%$ ), and a quantum CNOT gate with entangling capability has been demonstrated successfully.

Such a pulsed RF single-photon source may open the way to new interesting experiments in quantum optics and quantum information. With the high degree of indistinguishability of the RF photons shown here, they can be used to realize various optical quantum-computing algorithms $^{50,51}$ , interference of multiple photons $^{1}$ , and the on-demand generation of a photonic cluster state from a single quantum dot $^{31}$ . In parallel, the RF spectra of a two-level system under strong pulsed laser excitation, which are expected to exhibit novel features beyond the Mellow triplet $^{52}$ , comprise a subject worth studying.

A natural extension is to realize non-postselective high-visibility quantum interference between two pulsed RF single photons from separate quantum dots $^{18,19}$ . Based on this, it is possible to entangle remote, independent quantum dot spins $^{4,30}$ . We note that although the relatively slow spectral diffusion and pure dephasing does not affect the two-photon interference in our present work because of the 2 ns time separation of the photons, it will limit the degree of indistinguishability for photons from independent quantum dots. For future experiments, gate-controlled quantum dots could be used to reduce the spectral diffusion. Alternatively, spectral filtering at the expense of photon rate may be needed.

For quantum information applications, the photon extraction efficiency is a critical issue. So far, we have obtained  $\pi$  pulse-excited single photons with an overall collection efficiency of  $1.3\%$  reaching the single-photon detector. The photon extraction efficiency can be improved, for example, by embedding the quantum

dots in micropillars or photonic-crystal cavities $^{10}$ . Large Purcell effects from these microcavities can be helpful in efficiently funneling the spontaneous emission into a guided mode, to further mitigate the dephasings $^{20}$  and increase the pulse repetition rate to tens of gigahertz. Finally, it is important to note that in the previous pulsed above-bandgap or  $p$ -shell excitation experiment, the photon coherence time had to be much larger than the incoherent carrier relaxation time jitter (on the scale of tens of picoseconds) to obtain a good two-photon interference visibility $^{20}$ , which fundamentally put a limit on the radiative lifetime shortening through the Purcell effect. We emphasize that the true resonant, time jitter-free, pulsed RF technique developed here has no such limitation and can be fully compatible with large Purcell factors to be implemented in the future.

# Received 5 July 2012; accepted 13 December 2012; published online 3 February 2013

# References

1. Pan, J-W. et al. Multi-photon entanglement and interferometry. Rev. Mod. Phys. 84, 777-838 (2012).  
2. Kok, P. et al. Linear optical quantum computing with photonic qubits. Rev. Mod. Phys. 79, 135-174 (2007).  
3. O'Brien, J. L., Furusawa, A. & Vuckovic, J. Photonic quantum technologies. Nature Photon. 3, 687-695 (2009).  
4. Kimble, H. J. The quantum internet. Nature 453, 1023-1030 (2008).  
5. Hong, C. K., Ou, Z. Y. & Mandel, L. Measurement of subpicosecond time intervals between two photons by interference. Phys. Rev. Lett. 59, 2044-2046 (1987).  
6. Lounis, B. & Orrit, M. Single-photon sources. Rep. Prog. Phys. 68, 1129-1179 (2005).  
7. Shields, A. J. Semiconductor quantum light sources. Nature Photon. 1, 215-223 (2007).  
8. Michler, P. et al. A quantum dot single-photon turnstile device. Science 290, 2282-2285 (2000).  
9. Santori, C., Pelton, M., Solomon, G., Dale, Y. & Yamamoto, Y. Triggered single-photons from a quantum dot. Phys. Rev. Lett. 86, 1502-1505 (2001).  
10. Dousse, A. et al. Ultrabright source of entangled photon pairs. Nature 466, 217-220 (2010).  
11. Fushman, I. et al. Controlled phase shifts with a single quantum dot. Science 320, 769-772 (2008).  
12. Yilmaz, S. T., Fallahi, P. & Imamoglu, A. Quantum-dot-spin single-photon interface. Phys. Rev. Lett. 105, 033601 (2010).  
13. Young, A. B. et al. Quantum-dot-induced phase shift in a pillar microcavity. Phys. Rev. A 84, 011803 (2011).  
14. Yao, W., Liu, R. B. & Sham, L. J. Theory of control of the spin-photon interface for quantum networks. Phys. Rev. Lett. 95, 030504 (2005).  
15. Santori, C., Fattal, D., Vuckovic, J., Solomon, G. & Yamamoto, Y. Indistinguishable photons from a single-photon device. Nature 419, 594-597 (2002).  
16. Bennett, A. J. et al. Influence of exciton dynamics on the interference of two photons from a microcavity single-photon source. Opt. Express 13, 7772-7778 (2005).  
17. Weiler, S. et al. Highly indistinguishable photons from a quantum dot in a microcavity. Phys. Status Solidi B 248, 867-871 (2011).  
18. Flagg, E. B. et al. Interference of single photons from two separate semiconductor quantum dots. Phys. Rev. Lett. 104, 137401 (2010).  
19. Patel, R. B. et al. Two-photon interference of the emission from electrically tunable remote quantum dots. Nature Photon. 4, 632-635 (2010).  
20. Santori, C. et al. Single-photon generation with InAs quantum dots. New J. Phys. 6, 89 (2004).  
21. Muller, A. et al. Resonance fluorescence from a coherently driven semiconductor quantum dot in a cavity. Phys. Rev. Lett. 99, 187402 (2007).  
22. Vamivakas, A. N., Zhao, Y., Lu, C. Y. & Atatüre, M. Spin-resolved quantum-dot resonance fluorescence. Nature Phys. 5, 198-202 (2009).  
23. Flagg, E. B. et al. Resonantly driven coherent oscillations in a solid-state quantum emitter. Nature Phys. 5, 203-207 (2009).  
24. Ulhaq, A. et al. Cascaded single-photon emission from the Mollow triplet sidebands of a quantum dot. Nature Photon. 6, 238-242 (2012).  
25. Ates, S. et al. Post-selected indistinguishable photons from the resonance fluorescence of a single quantum dot in a microcavity. Phys. Rev. Lett. 103, 167402 (2009).  
26. Kiraz, A. et al. Indistinguishable photons from a single molecule. Phys. Rev. Lett. 94, 223602 (2005).  
27. Patel, R. B. et al. Postselective two-photon interference from a continuous nonclassical stream of photons emitted by a quantum dot. Phys. Rev. Lett. 100, 207405 (2008).

28. Matthiesen, C., Vamivakas, A. N. & Atature, M. Subnatural linewidth single photons from a quantum dot. Phys. Rev. Lett. 108, 093602 (2012).  
29. Nguyen, H. S. et al. Ultra-coherent single photon source. Appl. Phys. Lett. 99, 261904 (2011).  
30. Barrett, S. D. & Kok, P. Efficient high-fidelity quantum computation using matter qubits and linear optics. Phys. Rev. A 71, 060301 (2005).  
31. Lindner, N. H. & Rudolph, T. Proposal for pulsed on-demand sources of photonic cluster state strings. Phys. Rev. Lett. 103, 113602 (2009).  
32. Melet, R. et al. Resonant excitonic emission of a single quantum dot in the Rabi regime. Phys. Rev. B 78, 073301 (2008).  
33. Zrenner, A. et al. Coherent properties of a two-level system based on a quantum-dot photodiode. Nature 418, 612-614 (2002).  
34. Wang, Q. Q. et al. Decoherence processes during optical manipulation of excitonic qubits in semiconductor quantum dots. Phys. Rev. B 72, 035306 (2005).  
35. Ramsay, A. J. et al. Phonon-induced Rabi-frequency renormalization of optically driven single InGaAs/GaAs quantum dots. Phys. Rev. Lett. 105, 177402 (2010).  
36. Mogilevtsev, D. et al. Driving-dependent damping of Rabi oscillation in two-level semiconductor systems. Phys. Rev. Lett. 100, 017401 (2008).  
37. Robinson, H. D. & Goldberg, B. B. Light-induced spectral diffusion in single self-assembled quantum dots. Phys. Rev. B 61, 5086-5089 (2000).  
38. Berthelot, A. et al. Unconventional motional narrowing in the optical spectrum of a semiconductor quantum dot. Nature Phys. 2, 759-764 (2006).  
39. Houel, J. et al. Probing single-charge fluctuations at a GaAs/AlAs interface using laser spectroscopy on a nearby InGaAs quantum dot. Phys. Rev. Lett. 108, 107401 (2012).  
40. Kuhn, A., Hennrich, M. & Rempe, G. Deterministic single-photon source for distributed quantum networking. Phys. Rev. Lett. 89, 067901 (2002).  
41. McKeever, J. et al. Single photons from one atom trapped in a cavity. Science 303, 1992-1994 (2004).  
42. Beugnon, J. et al. Quantum interference between two single photons emitted by independently trapped atoms. Nature 440, 779-782 (2006).  
43. Maunz, P. et al. Quantum interference of photon pairs from two remote trapped atomic ions. Nature Phys. 3, 538-541 (2007).  
44. O'Brien, J. L., Pryde, G. J., White, A. G., Ralph, T. C. & Branning, D. Demonstration of an all-optical quantum controlled-NOT gate. Nature 426, 264-267 (2003).  
45. Langford, N. K. et al. Demonstration of a simple entangling optical gate and its use in Bell-state analysis. Phys. Rev. Lett. 95, 210504 (2005).  
46. Kiesel, N. et al. Linear optics controlled-phase gate made simple. Phys. Rev. Lett. 95, 210505 (2005).  
47. Okamoto, R. et al. Demonstration of an optical quantum controlled-NOT gate without path interference. Phys. Rev. Lett. 95, 210506 (2005).  
48. Pooley, M. A. et al. Controlled-NOT gate operating with single photons. Appl. Phys. Lett. 100, 021103 (2012).  
49. Hofmann, H. F. Complementary classical fidelities as an efficient criterion for the evaluation of experimentally realized quantum operations. Phys. Rev. Lett. 94, 160504 (2005).  
50. Fattal, D., Diamanti, E., Inoue, K. & Yamamoto, Y. Quantum teleportation with a quantum dot single photon source. Phys. Rev. Lett. 92, 037904 (2004).  
51. Scholz, M., Aichlele, T., Ramelow, S. & Benson, O. Deutsch-Jozsa algorithm using triggered single photons from a single quantum dot. Phys. Rev. Lett. 96, 180501 (2006).  
52. Moelbjerg, A., Kaer, P., Lorke, M. & Mørk, J. Resonance fluorescence from semiconductor quantum dots: beyond the Mollow triplet. Phys. Rev. Lett. 108, 017401 (2012).

# Acknowledgements

The authors thank Y. Yu, Z. Xi, J. Bowles, K. Chen, C. Matthiesen, X-L. Wang, L-J. Wang, N. Vamivakas and Y. Zhao for helpful discussions. This work was supported by the National Natural Science Foundation of China, the Chinese Academy of Sciences (CAS) and the National Fundamental Research Program (grant nos 2011CB921300, 2013CB933300), and the State of Bavaria. M.A. acknowledges the CAS visiting professorship. C-Y.L. acknowledges the Anhui Natural Science Foundation and Youth Qianren Program.

# Author contributions

M.A., C-Y.L. and J-W.P. conceived and designed the experiments. C.S., S.H. and M.K. grew and fabricated the sample. Y-M.H., Y.H., Y-J.W., D.W., M.A. and C-Y.L. carried out the optical experiments. Y-M.H., S.H., C-Y.L. and J-W.P. analysed the data. C-Y.L. wrote the manuscript, with input from all authors. S.H., C-Y.L. and J-W.P. guided the project.

# Additional information

Supplementary information is available in the online version of the paper. Reprints and permission information is available online at http://www.nature.com/reprints. Correspondence and requests for materials should be addressed to S.H., C-Y.L. and J-W.P.

# Competing financial interests

The authors declare no competing financial interests.