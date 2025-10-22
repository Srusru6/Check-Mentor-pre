# A 100-pixel photon-number-resolving detector unveiling photon statistics

Received: 27 June 2022

Accepted: 27 October 2022

Published online: 19 December 2022

![](images/289a4d6801a12be0ddffeb3b7a2a249512a86216a26fcffd4793fb0953142a04.jpg)

Check for updates

Risheng Cheng $^{1,3}$ , Yiyu Zhou $^{1,2,3}$ , Sihao Wang $^{1}$ , Mohan Shen $^{1}$ , Towsif Taher $^{1}$  & Hong X. Tang $^{1,2}$

Single-photon detectors are ubiquitous in quantum information science and quantum sensing. They are key enabling technologies for numerous scientific discoveries and fundamental tests of quantum optics. Photon-number-revolving detectors are the ultimate measurement tool of light; however, few detectors so far can provide high-fidelity photon number resolution at few-photon levels. Here we demonstrate an on-chip detector that can resolve up to 100 photons by spatiotemporally multiplexing an array of superconducting nanowires along a single optical waveguide. The unparalleled photon number resolution paired with the high-speed response exclusively allows us to unveil the quantum photon statistics of a true thermal light source at an unprecedented level, which is realized by direct measurement of the higher-order correlation function  $g^{(N)}$  (with values of  $N$  up to 15), observation of photon-subtraction-induced photon number enhancement and quantum-limited state discrimination against a coherent light source. Our detector provides a viable route towards various important applications, including photonic quantum computation and quantum metrology.

The observation and application of intriguing quantum optical effects have long relied on high-performance photon-number-resolving (PNR) detectors<sup>1</sup>. An ideal PNR detector should have unity detection efficiency, high-speed, low-timing jitter, negligible dark counts, and the ability to resolve photon numbers with a large dynamic range and high fidelity. Although transition edge sensors<sup>2-6</sup> and microwave kinetic inductance detectors<sup>7,8</sup> have demonstrated their inherent photon number resolution as well as excellent low readout noise, their performances are mainly limited in terms of low count rate (typically below 1 MHz), large timing jitter (nanosecond level) and the need for ultra-low operation temperatures  $(-100\mathrm{mK})$ . On the other hand, superconducting nanowire single-photon detectors (SNSPDs)<sup>9</sup> are a cutting-edge technology, with high efficiency  $(>98\%)$ <sup>10,11</sup>, gigahertz-level count rate<sup>12</sup>, picosecond-level timing jitter<sup>13</sup>, subhertz dark count noise<sup>14</sup>, and an elevated operation temperature  $(2 - 4\mathrm{K})$ ; however, the main drawback of SNSPDs is their limited photon number resolution. Although some modified readout schemes have been proposed to extend the PNR ability by either integrating impedance transformer<sup>15</sup> or

employing a wide-band cryogenic amplifier $^{16}$ , the maximum resolvable photon number still remains at 3-4.

Alternative approaches to construct a PNR-SNSPD include temporal- and spatial-multiplexing $^{17-25}$ , which have been used in ensemble measurements with only a few detector pixels; however, when a single-shot determination of the photon number is required, a sufficiently large pixel number is critical to minimize the probability of more than one photon simultaneously firing the same detector pixel, and thus to achieve high PNR fidelity $^{25-30}$ . Multiplexed detectors are thus also referred to as quasi-PNR detectors. The general limitation in the temporal-multiplexing scheme is the bulky set-up consisting of multiple stages of long fibres to provide nanosecond-level delay, which is difficult to integrate on a single chip and thus has limited scalability. In comparison, the spatial-multiplexed array of SNSPDs have shown PNR capability with a high dynamic range up to 24 photons $^{20}$ , while maintaining a simple readout scheme by series- or parallel-connecting all of the detector pixels. Nevertheless, as the detected photon number increases, the resolution of the output voltage proportional

<sup>1</sup>Department of Electrical Engineering, Yale University, New Haven, CT, USA. <sup>2</sup>Ryle Quantum Institute, Yale University, New Haven, CT, USA. <sup>3</sup>These authors contributed equally: Risheng Cheng and Yiyu Zhou. e-mail: hong.tang@yale.edu

![](images/40769be2400142e4e83e0ac879d542d74596732e082a01a8175b51bd42cc9355.jpg)  
a

![](images/9bebaf6287bc16a46af61abc3815aac165128edc37e60bd1df60992836bc474a.jpg)  
b

![](images/0c4d0d65707a557abcb4b739ff06df8ab0fd0ae2ab118e4616cdcf7c19889a2d.jpg)  
C

![](images/bd8e431745df4a2f74aadd8718ab20b8b5fa674ac98cd3f578ac5914a3984095.jpg)  
d

![](images/d301dce60e9e9835b43fd02fff88e8f65eb695a45058e42d9b7123d7014869e0.jpg)  
e

![](images/7b69c357857fd165e61bf59a94f10479e9a942a8dcbc08005d6f93c2eb4640ae.jpg)  
f

![](images/e42a545923ee4b6b265817728732d77e9a785566c56ba941d442f594cc37c47b.jpg)  
g  
Fig. 1 | Device architecture and operation principle. a, Schematic illustration of the 100-pixel quasi-PNR detector structure based on the spatiotemporal-multiplexed SNSPD array. The high-frequency detector signals are read out through the bus line consisting of the series-connected nanowire detectors and delay-line sections (blue colour), whereas the bias currents of the fired detector pixels are recovered via the low-frequency reset loop formed by the on-chip inductor and resistor (orange colour). b, Overview optical micrograph image of the device. The image is taken before finishing device fabrication for better visibility (see Methods). c, Expanded view of the grating coupler. d, Expanded view of the delay-line sections located at the lower left corner of the  
device. e, Expanded optical micrograph and false-colour scanning-electron micrograph view of the nanowire detectors with the leads passing through the waveguide bridges. f, Expanded view of the on-chip resistors, inductors and part of the impedance tapers. g, Persistence oscilloscope traces of electrical pulses generated from each pixel of the detector. The presence/absence of the pulses combined with the arrival time of the pulse peaks can be used to provide both the total detected photon number and the pixel number information of the fired pixels. The gradually reduced peak height of the pulses for the higher pixel numbers is due to the ohmic loss introduced by the top metal ground of the microwave transmission line (see Methods).

to the photon number degrades considerably due to the limited signal-to-noise ratio, thus limiting further scalability. Furthermore, both of these multiplexing schemes are lacking in spatial resolution, which is highly desired in some quantum applications to resolve the spatial modes of the input photons.

Here we demonstrate the design and experimental implementation of a waveguide-integrated, hybrid spatiotemporal-multiplexed SNSPD array, which features simultaneous photon number- and position-resolving capability, high scalability and a simple readout scheme. Furthermore, the high timing resolution combined with the large-dynamic-range PNR capability of the detector allows us to analyse the photon number statistics of a true thermal light source. Thermal light played a critical role in the development of quantum optics as it triggered the invention of the intensity correlation measurement  $g^{(2)}$  in the work by Hanbury Brown and Twiss<sup>31</sup>. Although

thermal light has been studied extensively $^{32-35}$ , most experiments use a pseudo-thermal light source that is artificially generated by passing a coherent laser light through a rotating ground glass $^{36,37}$ . This is because true thermal light sources typically have a broad bandwidth and thus a short coherence time, which places extreme demand on the timing resolution of the single-photon detectors $^{38-41}$ . With the unprecedented photon number resolution as well as the high-speed responses of our detector, we are able to observe the photon statistics transition from a Bose-Einstein distribution to a Poisson distribution by tuning the pulse width of a true thermal light source. Our detector also permits a convenient direct measurement of the higher-order correlation function  $g^{(N)}$  (ref. 5), with  $N$  up to 15 in our experiment, which is only limited by the data acquisition rate of our test equipment, rather than the detector itself. We also implement the quantum-limited discrimination of a thermal and a coherent state

![](images/d25e04f888abeb847902d44ffb228de5ff970c546dd75a67f7c063ea9ed682c1.jpg)  
a

![](images/82a83c41ca21c0bdcc768a2b0972f411db126b240ce6e1ee945992cc7654359d.jpg)  
b

![](images/fc10652814e9b8f0d064aeb01ed6ca095a58f022087f39469de89544f9ce40e2.jpg)  
C  
Fig. 2 | Photon statistics measurement. a,b, Example instance of the oscilloscope trace (upper panels), measurement sequences (lower panels) and detected counts of photon number (right panels) for thermal light with an experimentally measured mean photon number  $\bar{n}_{\mathrm{exp}} = 5.97 \pm 0.30$ , (a) and coherent light with  $\bar{n}_{\mathrm{exp}} = 53.63 \pm 0.02$ , (b), where data are represented by mean values  $\pm 1$  SEM. The photon number and position information on the fired pixels can be found by measuring the presence/absence of the pulses after an appropriate threshold (red dashed lines) in each time slot, which corresponds to the individual pixel of the detector. c,d, Photon number probability distribution for thermal light with  $\bar{n}_{\mathrm{exp}} = 5.97 \pm 0.30$ , (c) and  $\bar{n}_{\mathrm{exp}} = 18.10 \pm 0.33$ , (d). The blue

![](images/9727ac978f7de4549c12df7e1764ee5a93af5eb122c07ec50ebe2b0cf73aead9.jpg)  
d

![](images/bced57a3675e76902e49178e49e1fd6d2b00ab0b05effe657877945259b1d84b.jpg)  
e  
bars are the experimental data when EDFAs are used as the thermal light source; these agree well with the red dots following the theoretical Bose-Eisenstein distribution. The experimentally measured variance  $\Delta n_{\mathrm{exp}}^2$  is shown above the data. e,f, Photon number probability distribution for coherent light with  $\bar{n}_{\mathrm{exp}} = 6.18 \pm 0.01(\mathbf{e})$  and  $\bar{n}_{\mathrm{exp}} = 53.63 \pm 0.02(\mathbf{f})$ . The Poisson-fitting deviates from the experimental data in f due to the detector saturation effect. We take into account the effect by Monte Carlo simulation (green diamond markers), and the simulation result agrees with the experimental data (see Extended Data Fig. 2). The sample size used in c-f is 3,000.

![](images/94474a89a8e0cb9e4b10beab89c37c98235c9987ff1476c4006802bac9dc3135.jpg)  
f

approaching the Helstrom bound $^{42}$  to showcase the potential of our detector in quantum metrology applications.

# Results

# Operation principle of the detector

Figure 1a illustrates the basic operation principle of the spatiotemporal-multiplexed SNSPD array, whereas Fig. 1b–f shows device images. Further images and device yields are presented in Supplementary Note 1. The incident photons are guided by the waveguide and spatially distributed to the nanowire detector pixels of incremental length integrated atop the waveguide. All of the detector pixels are series connected with identical sections of nanosecond-level delay lines embedded between neighbouring pixels. Each pixel is shunted by an on-chip inductor and resistor for the local reset of the bias current after firing. The fired pixel generates a pair of positive/negative electrical pulses that propagate along the opposite direction of the high-frequency bus line, which consists of the detector pixels and the delay-line sections (blue colour). The signals are then read out in a time sequence using the temporal-multiplexing method (Fig. 1g).

The impedance tapers are attached at both ends of the bus line to match the impedance between the delay lines and the reading electronics, which is critical for minimizing reflections of the readout signals, and thus preserving clear and fast-rising/falling edges $^{43,44}$ . Furthermore, the presence of the resistively shunted inductors prevents the high-frequency signals entering the low-frequency reset loop (orange colour), rendering the readout and reset of the individual detector pixels separated.

One advantage of this device design is that the nanowire detectors, on-chip inductors, microwave delay lines and impedance tapers could all be implemented in a single ultra-thin niobium nitride (NbN) superconducting layer $^{45}$  (Fig. 1b–f), thus greatly simplifying the fabrication process. Moreover, a compact design of an ultra-slow microwave transmission line based on high-kinetic-inductance NbN nanowires and a high- $k$  dielectric layer (see Methods) is employed here instead of bulky optical delay lines for the temporal-multiplexed readout, and thus a high scalability of the detector pixel number is expected. More importantly, this hybrid spatiotemporal-multiplexing scheme enables position-resolving capability; that is, in addition to the information of

![](images/44f8a272172a1d6da9b153a8557142db3149deafcf47035b1f937d325ac0e2ff.jpg)  
a

![](images/e674abed4a62bf81df451e181bfd79454ce9507cd0d52edeb496b19d1f36dcba.jpg)  
b

![](images/20cbb43d1267c35cf6c62a4abb5c5d35bb87a0803c7f5e5abe3ee89134098a9e.jpg)  
C

![](images/7821eb865100d77b00fe210e044e95368b97b1b308c79330a59f93563d31f167.jpg)  
d

![](images/5d1f372621dbcb66d7d18985bb1cd641df39cc40ec7af54159ceefd5f234f92c.jpg)  
e  
Fig. 3 | Photon statistics and higher-order correlation measurement. a,

f  
![](images/afa5653a09fa877af1343d9b6cd3b82932fbb5b39d976ba2ee4f7f0be3e31824.jpg)  
Simplified schematic of the experimental set-up. A full schematic is presented in Supplementary Note 2. b-d, Photon number probability distribution measured with spectrally filtered EDFAs used as the thermal light source. We change the EOM pulse width  $\tau$  to tune the time-bandwidth product  $\pi B\tau$  between 0.0.5 (b), 0.52 (c) and 10.21 (d). The sample size used in b-d is 3,000.e, Comparison between the conventional method and our implementation to measure  $g^{(N)}$ . In our implementation, we split the 100-pixel detector into  $N$  groups and use the separate sum of photon counts in the  $N$  groups for coincidence measurement.  
This method is equivalent to the conventional method in which the input light beam is split by a beam-splitter tree into  $N$  paths, each of which is detected by a PNR detector. f, Measured mean values of  $g^{(N)}$  with  $N$  up to 15 (dots) in comparison with the theoretical calculation (solid curves). Error bars indicate 1 SEM, and the asymmetric error bars are due to the log scale representation. The type and parameters used for the light source are labelled beside each corresponding curves. In particular, we experimentally measure  $g^{(2)} = 1.962 \pm 0.007$  for  $\pi B\tau = 0.05$ . The sample size used in f is  $10^4$ .

photon number, the readout scheme could also provide position information on the fired detector pixels. This distinct property combined with a timing jitter as low as 50 ns (see Extended Data Fig. 1) makes our detector a highly versatile platform to perform various quantum optics experiments on a chip.

# Photon statistics and correlation measurement

We first demonstrate the potential of our detector in quantum optics applications by measuring the photon statistics of thermal and coherent states of light. A high-speed oscilloscope is used to acquire electrical pulse signals generated by the detector and amplified by low-noise amplifiers (see Supplementary Note 2 for more details on the measurement set-up). One instance of the oscilloscope trace produced by detecting a thermal light source from erbium-doped fibre amplifiers (EDFAs) is shown in Fig. 2a, and the result for a coherent state is shown in Fig. 2b. The presence/absence of the pulses in each time slot—which correspond to the individual pixels of the detector—can be used to provide the total detected photon number as well as the position information of the fired pixels. The lower panels in Fig. 2a,b show ten measurement sequences and the corresponding photon number count in each measurement is presented at the end of each sequence. By collecting a sufficient number of measurements, the histogram of the detected photon numbers can be constructed to obtain the photon number probability distribution; panels c and d in Fig. 2 show the photon number probability distributions of a thermal light with experimentally measured mean photon numbers of  $\bar{n}_{\mathrm{exp}} = 5.97 \pm 0.30$  and  $18.10 \pm 0.33$ , respectively, where  $\bar{n}_{\mathrm{exp}}$  is represented by the mean value  $\pm 1$  standard error of the mean (SEM). It can be seen that the experimental data agree well with the Bose-Einstein fitting. The statistics measurement of a coherent laser source with  $\bar{n}_{\mathrm{exp}} = 6.18 \pm 0.01$  is shown in Fig. 2e, and a much higher photon number  $(\bar{n}_{\mathrm{exp}} = 53.63 \pm 0.02)$  is demonstrated in Fig. 2f to showcase the large-dynamic-range PNR capability of our detector. Both traces from

the coherent source follow the Poisson distribution, and the counts of photon number fluctuate much less strongly than that of the thermal state due to the lack of photon bunching (see Supplementary Videos 1 and 2). It is also worth noting that as the total detected photon number increases, the peak-to-background ratio deteriorates, particularly for the signals from the second half of the pixels. This is due to the reduced peak height of the pulses (Fig. 1g) along with the accumulated low-frequency background ripples from the preceding fired pixel signals, which is also captured in our simulation (Supplementary Note 3). To mitigate this problem, we can use both output channels of our detector and separately collect the signals for 1-50 and 51-100 pixels. In a future upgrade, a higher-permittivity dielectric layer such as  $\mathrm{SrTiO_3}$  (ref. [46]) can be employed to greatly reduce the propagation speed of the microwave signals and thus increase the delay time between neighbouring pulse signals to help better differentiate them. The use of a high-permittivity material also makes it possible to further boost the pixel number by one or more orders of magnitude on a compact-sized chip. Moreover, waveform processing schemes more advanced than simple pulse peaks counting could be developed in the future to better extract the detection information. It is also worth noting that the measured statistics of a coherent state with a high mean photon number  $\bar{n}_{\mathrm{exp}} = 53.63 \pm 0.02$  starts to deviate from the Poisson distribution. This is caused by the fact that one detector pixel is likely to be fired by more than one photon when the photon number is high [27], and thus some photons are missing and not registered. We model this effect by Monte Carlo simulation (see Methods and Extended Data Fig. 2), and the simulation result agrees with the experiment (see green diamond markers in Fig. 2f).

We next use our detector to investigate the effect of pulse width on the quantum statistics of a true thermal light source and compare it with that of a coherent counterpart. A simplified schematic of the experimental set-up is shown in Fig. 3a (see Supplementary Note 2 for a complete schematic). The spectrally filtered amplified spontaneous

![](images/710532f8b1f9c32bdd5fdeadf5bd48794704c9c4e3a4ad6d0142256fd8d40f7d.jpg)  
a

![](images/86f2854ae338ff40e6282a21ac2f93f73216ec61810d567e8a996190ee6f20fe.jpg)

![](images/7d212abd137508ed4d27d741ab8916a1bbf645942f5ce45b89af8f8fc9c084f0.jpg)  
b  
Fig. 4 | Photon subtraction experiment. a, Comparisons between the conventional method and our implementation to measure the photon number statistics for a photon-subtracted thermal light. The conventional method employs a beam-splitter and measures photon numbers  $n_{\mathrm{R}}$  and  $n_{\mathrm{T}}$  at the reflection and transmission ports, respectively, using two PNR detectors. In our implementation, we split the 100-pixel detector into two groups and measure the photon number probability of group T in the event of  $n_{\mathrm{R}} = M$ , where  $M$  is the

![](images/2e0eedacd688b9ad39f1e51176dd09ddb91d7b7af381b01daa4807d39aba4cc8.jpg)  
C

![](images/a96c664cad5194b82df75d5d8603029c44526f4170f5f1682ddef699217c8460.jpg)  
d

![](images/9c115180b0fdfd7683faa9265bfee6df8997f3adc75dcf86003796774a8f56cf.jpg)  
subtracted photon number.  $\mathbf{b} - \mathbf{d}$ , Photon number probability distribution with various subtracted photon numbers  $n_{\mathrm{R}} = 0$  ( $\mathbf{b}$ ), 2 ( $\mathbf{c}$ ) and 4 ( $\mathbf{d}$ ). The spectrally filtered EDFAs with  $\pi B\tau = 0.05$  are used as the thermal light source.  $\mathbf{e}$ , Mean values of photon number enhancement (solid dots) and theoretical calculation (solid curves). The error bars indicate 1 SEM. The type and parameters used for the light source are labelled beside each corresponding curves. The sample size is  $10^{4}$ .  
e

emission from EDFAs and the narrow-bandwidth coherent-state light from a continuous-wave laser are used separately as light sources, with the variable optical attenuators (VOAs) tuning the light intensity and thus the mean photon number  $\bar{n}$ . Both of the sources are followed by the temporal gating through the electro-optic modulator (EOM) to make them pulsed sources. The photon number probability distribution of a thermal light measured by a PNR detector can be described by a negative binomial distribution as $^{48-50}$

$$
\begin{array}{l} P _ {\mathrm {N B}} (n; \pi B \tau , \bar {n}) = \binom {n + \pi B \tau} {n} \left(\frac {\pi B \tau + 1}{\bar {n} + \pi B \tau + 1}\right) ^ {\pi B \tau + 1} \tag {1} \\ \times \left(\frac {\bar {n}}{\bar {n} + n B \tau + 1}\right) ^ {n}, \\ \end{array}
$$

where  $\bar{n}$  is the mean photon number,  $B$  is the full-width at half-maximum (FWHM) bandwidth of the Lorentzian optical spectral filter $^{51}$ , and  $\tau$  the pulse width. When the time-bandwidth product  $\pi B\tau \ll 1$ , equation (1) reduces to the Bose-Einstein distribution  $P_{\mathrm{BE}}(n;\bar{n}) = \frac{1}{\bar{n} + 1}\left(\frac{\bar{n}}{\bar{n} + 1}\right)^{n}$ . On the other hand, when  $\pi B\tau \gg 1$ , it becomes the Poisson distribution  $P_{\mathrm{p}}(n;\bar{n}) = \bar{n}^{n}\mathrm{e}^{-\bar{n}} / n!$ . The spectral filter used in our experiment has a bandwidth of  $B = 65\mathrm{MHz}$ , and the pulse width is tuned by the EOM from 0.24 ns to 100 ns. The photon number probability distributions for  $\pi B\tau = 0.05$ , 0.52, 10.21 are shown in Fig. 3b-d. It can be clearly seen that the photon statistics gradually transits from the Bose-Einstein distribution to the Poisson distribution, which agrees well with the theoretical calculation by equation (1).

Our detector's position-resolving capability also aids convenient and direct measurement of  $g^{(N)} = \langle n_1n_2\ldots n_N\rangle /\langle n_1\rangle \langle n_2\rangle \dots \langle n_N\rangle$ , where  $\langle \cdot \rangle$  indicates the ensemble average. Conventional measurement of  $g^{(N)}$  is typically realized by splitting an optical beam into  $N$  parts and subsequently using  $N$  single-photon detectors for coincidence counting<sup>5</sup>. By contrast, we can flexibly split 100 pixels of our detector into  $N$  groups without modifying the experiment set-up and count the sum photon number in each group for coincidence measurement, as illustrated in Fig. 3e. The theoretical value of  $g^{(N)}$  for the EDFA thermal light source can be calculated as<sup>52</sup>

$$
g ^ {(N)} = \frac {\Gamma (\pi B \tau + N + 1)}{\Gamma (\pi B \tau + 1) (\pi B \tau + 1) ^ {N}}, \tag {2}
$$

where  $\Gamma (\cdot)$  is the gamma function. In the limit of  $\pi B\tau \ll 1$ , we have  $g^{(N)}\rightarrow N!$  which agrees with the result of the Bose-Einstein distribution<sup>53</sup>. At the other extreme of  $\pi B\tau \gg 1$ , it follows that  $g^{(N)}\rightarrow 1$ , which is a well-known result of the Poisson distribution. The experimental results for  $g^{(N)}$  with  $N$  up to 15 are shown in Fig. 3f, which agree well with the theoretical prediction. When  $\pi B\tau$  decreases, we can see that the value of  $g^{(N)}$  increases considerably. By contrast, the value of  $g^{(N)}$  remains unity when a coherent laser is used as the light source. It should be noted that the measurement of  $g^{(N)}$  with  $N > 15$  is limited by the slow data acquisition rate of the oscilloscope ( $\sim 30\mathrm{Hz}$ ) used in our experiment, rather than the detector itself, as an exponentially larger sample number is needed to minimize the variance of  $g^{(N)}$  as  $N$  increases. A dedicated gigahertz-level fast pulse counter could be employed in a future experiment to further unlock the performance of our detector.

# Photon subtraction experiment

We then further investigate the capability of our detector by performing photon subtraction experiment. Conventional photon subtraction entails using a beam-splitter to probabilistically subtract a certain number of photons at the reflection port, as shown in Fig. 4a. In our experiment, we split the 100-pixel detector into two groups (that is, groups R and T), and a splitting ratio  $\mathrm{R:T} = 20:80\%$  is achieved by adjusting the number of pixels in each group. Due to the bunching effect of thermal light, higher mean photon numbers will be detected at the transmission port as the number of photons subtracted at the reflection port increases[54,55]. This effect can be potentially useful for applications such as quantum-enhanced interferometry[34] and quantum-state engineering[35]. Assuming that the input photon number probability distribution can be described by a negative binomial distribution  $P_{\mathrm{NB}}^{\mathrm{in}}(n;\pi B\tau ,\bar{n}_{\mathrm{in}})$  with a mean photon number of  $\bar{n}_{\mathrm{in}}$ , the photon number probability distribution at the transmission port can be described by another negative binomial distribution  $P_{\mathrm{NB}}^{\mathrm{T}}(n;\pi B\tau +n_{\mathrm{R}},\bar{n}_{\mathrm{T}})$ , whose mean photon number  $\bar{n}_{\mathrm{T}}$  becomes[50]

$$
\bar {n} _ {\mathrm {T}} = \frac {(1 - R) \left(n _ {\mathrm {R}} + \pi B \tau + 1\right)}{R \bar {n} _ {\mathrm {i n}} + \pi B \tau + 1} \bar {n} _ {\mathrm {i n}}, \tag {3}
$$

where  $n_{\mathrm{R}}$  is the subtracted photon number at the reflection port. When  $R \to 0$ ,  $\pi B\tau \ll 1$ , and  $n_{\mathrm{R}} = 1$ , we have  $\bar{n}_{\mathrm{T}} = 2\bar{n}_{\mathrm{in}}$ , which is the well-known

Fig. 5 | Quantum-limited discrimination of coherent and thermal states.  
![](images/56a04556d583566f21081d3c8daaf2bb4ef2bc4dc3320e1b5190446be6df5a43.jpg)  
The theoretical values of the discrimination error probability are represented by solid lines, while the experimentally measured mean values are represented by dots. The error bars indicate 1SEM, and the sample size is 1,000. The insets show simplified schematics for the corresponding measurement methods.

result that the mean photon number of a thermal state at the transmission port will be doubled when a single photon is annihilated at the reflection port of a low-reflection beam-splitter $^{33}$ . It is also worth noting that the time-bandwidth product of the negative binomial distribution at the transmission port increases from  $\pi B\tau$  to  $\pi B\tau + n_{\mathrm{R}}$ ; thus, if the input beam follows the Bose-Einstein statistics with  $\pi B\tau \ll 1$ , the photon number distribution at the transmission port will transit to Poisson-like statistics when the annihilated photon number  $n_{\mathrm{R}}$  is large. These theoretical predictions agree well with our experimental data as shown in Fig. 4b-d, where  $n_{\mathrm{R}} = 0, 2, 4$  respectively. For these measurements, the spectrally filtered EDFA is used as the light source with  $\pi B\tau = 0.05$ .

We next investigate the photon number enhancement effect of photon subtraction, and we use

$$
\frac {\bar {n} _ {\mathrm {T}} \mid_ {n _ {\mathrm {R}} = M}}{\bar {n} _ {\mathrm {T}} \mid_ {n _ {\mathrm {R}} = 0}} = \frac {\pi B \tau + M + 1}{\pi B \tau + 1} \tag {4}
$$

as the metric to quantify the photon number enhancement, where  $M$  is the subtracted photon number at the reflection port. The experimental results of photon number enhancement are shown in Fig. 4e, which illustrates that the photon number enhancement increases linearly as  $M$  increases. By contrast, there is no enhancement for the coherent light source from the laser, indicating the photon states at the two output ports of the beam-splitter are uncorrelated for a coherent state input<sup>33</sup>.

# Quantum-limited discrimination of photon states

As another application of our detector, we perform quantum-limited discrimination between a thermal state and a coherent state of light $^{42}$ . Here the mean photon number  $\bar{n}$  of the light source is assumed to be known, but its quantum state, either a thermal state or a coherent state, remains to be discriminated. The minimum possible discrimination error is known as the Helstrom bound $^{56}$ , which can be computed as  $P_{\mathrm{err}}^{\mathrm{H}}(\bar{n}) = 0.5 - 0.25||\rho_{\mathrm{th}}(\bar{n}) - \rho_{\mathrm{coh}}(\bar{n})||_1$ , where  $\rho_{\mathrm{th}}(\bar{n})$  is the density matrix of a thermal state,  $\rho_{\mathrm{coh}}(\bar{n}) = |\alpha = \sqrt{\bar{n}}\rangle \langle \alpha|$  is the density matrix of a coherent state, and  $||\cdot ||_1$  is the trace distance.

The most straightforward method for discrimination is the direct detection, which entails using a PNR detector to measure the photon number emitted by the source. When  $n$  photons are measured, its quantum state is discriminated to be a thermal state if  $P_{\mathrm{BE}}(n; \bar{n}) > P_{\mathrm{P}}(n; \bar{n})$ . On the other hand, if  $P_{\mathrm{BE}}(n; \bar{n}) \leq P_{\mathrm{P}}(n; \bar{n})$ , the quantum state is discriminated to be a coherent state. The error probability of discrimination can thus be calculated as  $P_{\mathrm{direct}}^{\mathrm{err}}(\bar{n}) = \sum_{n} \min(P_{\mathrm{BE}}(n; \bar{n}), P_{\mathrm{P}}(n; \bar{n})) / 2$ ; however, this method cannot approach the Helstrom bound. The Kennedy receiver can outperform the direct detection by using homodyne detection. A high-transmission

beam-splitter ( $T \approx 1$ ) is used to reduce the loss for the signal to be discriminated. The Kennedy detection entails using a local oscillator with a mean photon number of  $\bar{n} T / (1 - T)$  and a relative  $\pi$  phase shift with respect to the coherent state light source, whose density matrix can be expressed as  $\rho_{\mathrm{LO}} = |-\alpha_{\mathrm{LO}}\rangle \langle -\alpha_{\mathrm{LO}}|$  with  $\alpha_{\mathrm{LO}} = \sqrt{\bar{n}}$ . If the source is a coherent state, the transmission port will present a vacuum state due to the destructive interference. If the source is a thermal state, the state at the transmission port possesses a Laguerre statistics<sup>42,48</sup>

$P_{\mathrm{L}}(n) = \frac{(\bar{n}T)^n}{(1 + \bar{n}T)^{n + 1}}\exp (-\frac{\bar{n}T}{1 + \bar{n}T})L_n(-\frac{1}{1 + \bar{n}T})$  where  $L_{n}(\cdot)$  is the Laguerre polynomial of order  $n$ . The discrimination error probability is thus  $P_{\mathrm{K}}^{\mathrm{err}}(\bar{n}) = P_{\mathrm{L}}(0) / 2$ . The Kennedy detection, however, can be further generalized to approach the Helstrom bound by changing  $\alpha_{\mathrm{LO}}$  to  $\alpha_{\mathrm{LO}} = \sqrt{\bar{n} + \Delta n}$ , where the value of  $\Delta n$  depends on  $\bar{n}$  and can be computed by numerical optimization[42]. In this case, if the source is a coherent state, the detected statistics becomes a Poisson distribution  $P_{\mathrm{p}}(n;\Delta n)$  with a mean photon number of  $\Delta n$ . If the source is a thermal state, the detected statistics becomes a Laguerre distribution

$P_{\mathrm{L}}(n,\Delta n) = \frac{(\bar{n}T)^n}{(1 + \bar{n}T)^{n + 1}}\exp (-\frac{(\bar{n} + \Delta n)T}{1 + \bar{n}T})L_n(-\frac{\bar{n} + \Delta n}{\bar{n}(1 + \bar{n}T)})$  and thus the discrimination error probability is  $P_{\mathrm{GK}}^{\mathrm{err}}(\bar{n}) = \sum_{n}\min (P_{\mathrm{P}}(n;\Delta n),P_{\mathrm{L}}(n,\Delta n)) / 2$

The experimental results measured by the different methods are shown in Fig. 5, which demonstrate that the generalized Kennedy detection closely approaches the Helstrom bound and is the best discrimination method that has been reported $^{42}$ .

# Discussion

In this Article we have demonstrated a waveguide-integrated and large-dynamic-range quasi-PNR detector that employs a hybrid spatiotemporal-multiplexing scheme to read out a 100-pixel SNSPD array. In addition to inheriting all aspects of the excellent performances of single-pixel SNSPDs, this scheme also enables readout of the position information on the fired detector pixels. This distinct functionality makes our detector a versatile platform to perform various quantum optics experiments on a chip at an unprecedented level, such as the photon statistics measurement, the direct measurement of  $g^{(N)}$  with  $N$  up to 15, the photon subtraction experiment with the subtracted photon number up to 7, and the quantum-limited photon state discrimination. In particular, these measurements present a comprehensive characterization of the quantum statistical properties of a true thermal light source for the first time, which is exclusively enabled by the simultaneous availability of high photon number resolution and fast detector response. We envision that our novel detector technology can boost a variety of cutting-edge applications in the near future, such as large-scale Boson sampling $^{57}$ , photonic quantum computing $^{58}$  and quantum metrology $^{59}$ .

# Online content

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41566-022-01119-3.

# References

1. Hadfield, R. H. Single-photon detectors for optical quantum information applications. Nat. Photon. 3, 696-705 (2009).  
2. Miller, A. J., Nam, S. W., Martinis, J. M. & Sergienko, A. V. Demonstration of a low-noise near-infrared photon counter with multiphoton discrimination. Appl. Phys. Lett. 83, 791 (2003).  
3. Lita, A. E., Miller, A. J. & Nam, S. W. Counting near-infrared single-photons with  $95\%$  efficiency. Opt. Express 16, 3032-3040 (2008).

4. Calkins, B. et al. High quantum-efficiency photon-number-resolving detector for photonic on-chip information processing. Opt. Express 21, 22657 (2013).  
5. Harder, G. et al. Single-mode parametric-down-conversion states with 50 photons as a source for mesoscopic quantum optics. Phys. Rev. Lett. 116, 143601 (2016).  
6. Eaton, M. et al. Resolving 100 photons and quantum generation of unbiased random numbers. Preprint at https://arxiv.org/abs/2205.01221 (2022).  
7. Guo, W. et al. Counting near infrared photons with microwave kinetic inductance detectors. Appl. Phys. Lett. 110, 212601 (2017).  
8. Day, P. K., LeDuc, H. G., Mazin, B. A., Vayonakis, A. & Zmuidzinas, J. A broadband superconducting detector suitable for use in large arrays. Nature 425, 817-821 (2003).  
9. Natarajan, C. M., Tanner, M. G. & Hadfield, R. H. Superconducting nanowire single-photon detectors: physics and applications. Supercon. Sci. Technol. 25, 063001 (2012).  
10. Reddy, D. V., Nerem, R. R., Nam, S. W., Mirin, R. P. & Verma, V. B. Superconducting nanowire single-photon detectors with 98% system detection efficiency at 1550 nm. Optica 7, 1649-1653 (2020).  
11. Chang, J. et al. Detecting telecom single photons with  $\left(99.5_{-2.07}^{+0.5}\right)$  % system detection efficiency and high time resolution. APLPhoton. 6, 036114 (2021).  
12. Zhang, W. et al. A 16-pixel interleaved superconducting nanowire single-photon detector array with a maximum count rate exceeding 1.5 GHz. IEEE Trans. Appl. Supercond. 29, 1 (2019).  
13. Korzh, B. et al. Demonstration of sub-3 ps temporal resolution with a superconducting nanowire single-photon detector. Nat. Photon. 14, 250-255 (2020).  
14. Shibata, H., Shimizu, K., Takesue, H. & Tokura, Y. Ultimate low system dark-count rate for superconducting nanowire single-photon detector. Opt. Lett. 40, 3428-3431 (2015).  
15. Zhu, D. et al. Resolving photon numbers using a superconducting nanowire with impedance-matching taper. Nano Lett. 20, 3858-3863 (2020).  
16. Cahall, C. et al. Multi-photon detection using a conventional superconducting nanowire single-photon detector. Optica 4, 1534-1535 (2017).  
17. Natarajan, C. M. et al. Quantum detector tomography of a time-multiplexed superconducting nanowire single-photon detector at telecom wavelengths. Opt. Express 21, 893-902 (2013).  
18. Divochiy, A. et al. Superconducting nanowire photon-number-resolving detector at telecommunication wavelengths. Nat. Photon. 2, 302-306 (2008).  
19. Cheng, R. et al. Photon-number-resolving detector based on superconducting serial nanowires. IEEE Trans. Appl. Supercond. 23, 2200309 (2013).  
20. Mattioli, F. et al. Photon-counting and analog operation of a 24-pixel photon number resolving detector based on superconducting nanowires. Opt. Express 24, 9067-9076 (2016).  
21. Schmidt, E. et al. Characterization of a photon-number resolving SNSPD using Poissonian and sub-Poissonian light. IEEE Trans. Appl. Supercond. 29, 1 (2019).  
22. Wollman, E. E. et al. Kilopixel array of superconducting nanowire single-photon detectors. Opt. Express 27, 35279 (2019).  
23. Elshaari, A. W. et al. Dispersion engineering of superconducting waveguides for multi-pixel integration of single-photon detectors. *APL Photon.* 5, 111301 (2020).  
24. Schapeler, T. & Bartley, T. J. Information extraction in photon-counting experiments. Phys. Rev. A 106, 013701 (2022).  
25. Tiedau, J. et al. A high dynamic range optical detector for measuring single photons and bright light. Opt. Express 27, 1-15 (2019).

26. Provaznik, J., Lachman, L., Filip, R. & Marek, P. Benchmarking photon number resolving detectors. Opt. Express 28, 14839-14849 (2020).  
27. Worsley, A. et al. Absolute efficiency estimation of photon-number-resolving detectors using twin beams. Opt. Express 17, 4397-4412 (2009).  
28. Sperling, J., Vogel, W. & Agarwal, G. S. True photocounting statistics of multiple on-off detectors. Phys. Rev. A 85, 023820 (2012).  
29. Jonsson, M. & Björk, G. Photon-counting distribution for arrays of single-photon detectors. Phys. Rev. A 101, 013815 (2020).  
30. Schapeler, T. & Bartley, T. J. Information extraction in photon-counting experiments. Phys. Rev. A 106, 013701 (2022).  
31. Hanbury Brown, R. & Twiss, R. Q. Correlation between photons in two coherent beams of light. Nature 177, 27-29 (1956).  
32. Bennink, R. S., Bentley, S. J. & Boyd, R. W. 'Two-photon' coincidence imaging with a classical source. Phys. Rev. Lett. 89, 113601 (2002).  
33. Zavatta, A., Parigi, V., Kim, M. & Bellini, M. Subtracting photons from arbitrary light fields: experimental test of coherent state invariance by single-photon annihilation. New J. Phys. 10, 123006 (2008).  
34. Rafsanjani, S. M. H. et al. Quantum-enhanced interferometry with weak thermal light. Optica 4, 487-491 (2017).  
35. Magaña-Loaiza, O. S. et al. Multiphoton quantum-state engineering using conditional measurements. npj Quantum Inform. 5, 80 (2019).  
36. Goodman, J. W. Statistical Optics (John Wiley & Sons, 2015).  
37. Martienssen, W. & Spiller, E. Coherence and fluctuations in light beams. Am. J. Phys. 32, 919 (1964).  
38. Zhai, Y.-H., Chen, X.-H., Zhang, D. & Wu, L.-A. Two-photon interference with true thermal light. Phys. Rev. A 72, 043805 (2005).  
39. Liu, X.-F. et al. Lensless ghost imaging with sunlight. Opt. Lett. 39, 2314-2317 (2014).  
40. Tan, P. K., Yeo, G. H., Poh, H. S., Chan, A. H. & Kurtsiefer, C. Measuring temporal photon bunching in blackbody radiation. Astrophys. J. Lett. 789, L10 (2014).  
41. Deng, Y.-H. et al. Quantum interference between light sources separated by 150 million kilometers. Phys. Rev. Lett. 123, 080401 (2019).  
42. Habif, J. L., Jagannathan, A., Gartenstein, S., Amory, P. & Guha, S. Quantum-limited discrimination of laser light and thermal light. Opt. Express 29, 7418-7427 (2021).  
43. Zhao, Q.-Y. et al. Single-photon imager based on a superconducting nanowire delay line. Nat. Photon. 11, 247-251 (2017).  
44. Cheng, R. et al. Broadband on-chip single-photon spectrometer. Nat. Commun. 10, 4104 (2019).  
45. Cheng, R., Wang, S. & Tang, H. X. Superconducting nanowire single-photon detectors fabricated from atomic-layer-deposited NbN. Appl. Phys. Lett. 115, 241101 (2019).  
46. Santavicca, D. F., Colangelo, M., Eagle, C. R., Warusawithana, M. P. & Berggren, K. K. 50 Ohm transmission lines with extreme wavelength compression based on superconducting nanowires on high-permittivity substrates. Appl. Phys. Lett. 119, 252601 (2021).  
47. Zhu, D. et al. A scalable multi-photon coincidence detector based on superconducting nanowires. Nat. Nanotech. 13, 596-601 (2018).  
48. Karp, S., Gagliardi, R. M., Moran, S. E. & Stotts, L. B. Optical Channels: Fibers, Clouds, Water, and the Atmosphere (Springer, 2013).  
49. Agarwal, G. Negative binomial states of the field-operator representation and production by state reduction in optical processes. Phys. Rev. A 45, 1787 (1992).

50. Katamadze, K., Avosopiants, G., Bogdanova, N., Bogdanov, Y. I. & Kulik, S. Multimode thermal states with multiphoton subtraction: Study of the photon-number distribution in the selected subsystem. Phys. Rev. A 101, 013811 (2020).  
51. Mandel, L. & Wolf, E. The measures of bandwidth and coherence time in optics. Proc. Phys. Soc. Lond. 80, 894 (1962).  
52. Zhai, Y. et al. Photon-number-resolved detection of photon-subtracted thermal light. Opt. Lett. 38, 2171-2173 (2013).  
53. Stevens, M. J. et al. High-order temporal coherences of chaotic and laser light. Opt. Express 18, 1430-1437 (2010).  
54. Parigi, V., Zavatta, A., Kim, M. & Bellini, M. Probing quantum commutation rules by addition and subtraction of single photons to/from a light field. Science 317, 1890-1893 (2007).  
55. Barnett, S. M., Ferenczi, G., Gilson, C. R. & Speirits, F. C. Statistics of photon-subtracted and photon-added states. Phys. Rev. A 98, 013809 (2018).  
56. Helstrom, C. W. Quantum Detection and Estimation Theory (Academic, 1976).

57. Tillmann, M. et al. Experimental boson sampling. Nat. Photon. 7, 540-544 (2013).  
58. Kok, P. et al. Linear optical quantum computing with photonic qubits. Rev. Mod. Phys. 79, 135 (2007).  
59. Matthews, J. C. et al. Towards practical quantum metrology with photon counting. npj Quantum Inform. 2, 16023 (2016).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

© The Author(s), under exclusive licence to Springer Nature Limited 2022

# Methods

# Device fabrication

The fabrication of the device involves six high-resolution (100 kV) e-beam lithography (EBL) steps, and a subsequent etching or deposition/lift-off process. First, alignment markers are pre-fabricated on top of a 100-mm-diameter, 330-nm-thick LPCVD- $\mathrm{Si}_3\mathrm{N}_4/3.3$ - $\mu$ m-thick thermal oxide/silicon wafer by the standard double-layer polymethyl methacrylate (PMMA) patterning process, e-beam evaporation of 10/100 nm Cr/Au layers, and subsequent lift-off in acetone. Second, a high-uniformity, 8-nm-thick NbN superconducting thin film is deposited by atomic layer deposition[45], followed by e-beam patterning of the negative-tone 6% hydrogen silsesquioxane (HSQ) resist. It is worth noting that the spinning and patterning of the HSQ resist immediately after the fresh NbN film deposition is critical to maintaining excellent adhesion of the resist on the film. In the third EBL step, the electrode and contact pads for the on-chip resistors are defined by another double-layer PMMA patterning, e-beam evaporation of 5/25 nm Cr/Au, and the subsequent lift-off process. The HSQ pattern is later transferred to the NbN layer in a timed reactive-ion etching step employing tetrafluoromethane chemistry, which defines the nanowire detector pixels, delay lines, on-chip inductors and impedance tapers. In the fourth EBL step, we pattern the positive-tone AR-P 6200 (CSAR 62) resist for the photonic microstructures, including gratings couplers, Y-splitters and waveguides. The patterns are then transferred to the  $\mathrm{Si}_3\mathrm{N}_4$  film via carefully timed reactive-ion etching in fluoroform  $(\mathrm{CHF}_3)$ . The remaining resist is removed with gentle oxygen plasma and hot  $N$ -methylpyrrolidone. In the fifth EBL step, we define the on-chip resistors by patterning double-layer PMMA and e-beam evaporation of 80/5 nm Cr/Au with lift-off process. Finally, the 80-nm-thick alumina  $(\mathrm{AlO}_x)$  dielectric spacing layer and 100-nm-thick aluminium top ground layer are fabricated by double-layer PMMA patterning, e-beam evaporation and lift-off for making the low-speed microwave transmission line. The remaining HSQ mask on top of NbN in the delay-line area is removed by 1:100 diluted hydrofluoric acid after opening the PMMA window (lighter area in Fig. 1b) and before the deposition of  $\mathrm{AlO}_x/\mathrm{Al}$  layers. The resulting device is shown in Fig. 1b–f, and additional device images as well as the fabrication yield are presented in Supplementary Note 1.

# Device design

As shown in Fig. 1b, the photons are launched into the  $\mathrm{Si}_3\mathrm{N}_4$  waveguide from a fibre through the input grating coupler. The waveguide is then split into two branches, one of which is attached to the output grating coupler for power calibration and alignment, whereas the other one is adiabatically tapered from  $1.2\mu \mathrm{m}$  to  $8\mu \mathrm{m}$  width, and then connected to a series of 100 NbN nanowire detector pixels placed above the waveguide. All of the active detector pixels are made up of hairpin-shaped 80-nm-wide NbN nanowires that guarantee saturated internal efficiency at the  $1,550~\mathrm{nm}$  telecommunication wavelength. Each nanowire is shunted by a  $5 - \mu \mathrm{m}$ -wide and  $50 - \mu \mathrm{m}$ -long Cr/Au on-chip resistor (60 Ω resistance at  $1.7\mathrm{K}$ ), along with an on-chip inductor made of a 400-nm-wide NbN meander wire (200 nH inductance). All of the nanowires are series-connected with long-meandered 800-nm-wide NbN delay lines embedded in between, as visualized in Fig. 1b. Both ends of the nanowire-detector-delay-line chain are connected to the impedance tapers consisting of meandered NbN wires with a gradually varying width from  $800\mathrm{nm}$  to  $9.2\mu \mathrm{m}$ , which follow the Klopfenstein design to match the impedance between the delay lines (hundreds of ohms) and the external reading electronics ( $50\Omega$ ). The total length of each impedance taper is  $24\mathrm{mm}$ , which allows for a  $<50\mathrm{MHz}$  lower cut-off frequency. The long impedance tapers here play an important role in preserving the fast-rising edges and clear shapes of the photon-excited detector pulses by suppressing multiple reflections between the device and external readout electronics. At the ends of the impedance tapers, the microstrip lines are converted to coplanar waveguides to match the modes of ground-signal-ground radiofrequency probes.

By engineering the nanowire length and the distance of the nanowire from the edge of the waveguide, we could tune the photon absorption efficiency of each nanowire and thus ensure the input photons are evenly distributed over the detector pixels. In the etched clearance area for the waveguide, a  $1.2\text{-}\mu \mathrm{m}$  wide bridges are designed for the connection of each nanowire detector to the delay-line sections that are positioned outside the waveguide area (Fig. 1e). The 3D finite-difference time-domain simulation study shows that the total scattering loss introduced by 100 of such bridges is lower than  $0.2\mathrm{dB}$ . We further confirm the results by investigating the quality factors of  $\mathrm{Si}_3\mathrm{N}_4$  racetrack resonators with varying number of bridges embedded in the straight waveguide sections.

The parts of NbN delay lines and the impedance tapers are capped by a high-dielectric-constant (high- $k$ )  $\mathrm{AlO}_x$  layer and a top metal ground made of an aluminium layer (lighter green area in Fig. 1b), which helps substantially slow down the propagation speed of the photon-excited microwave signals, thereby enabling a very compact device design and also reducing the cross-talk between the transmission lines. Due to the high kinetic inductance of the superconducting wires made of NbN thin film and the high capacitance introduced by the thin high- $k$  layer, the propagation speed could be achieved as low as  $1.07\%$  of  $c$  (vacuum speed of light), despite the very wide delay lines compared with the nanowire detector. Each delay-line section is designed to be  $3.4\mathrm{mm}$  long and introduces a 1.09 ns propagation time delay between neighbouring detector pixels (Fig. 1g).

# Device characterization set-up

The sample chip containing tens of detector devices is mounted on a 3-axis stack of stages (Attocube) inside a low-vibration closed-cycle refrigerator (Cryomech) and cooled down to a base temperature of  $1.7\mathrm{K}$ . We drive the stages to move the sample chip and make the electrode contact with a multi-channel radiofrequency probe, which is used to direct current bias the detector device and read out the photon-excited electrical pulses. In the meantime, the grating couplers are aligned to the single-mode fibre array by optimizing the optical transmission through the device (see Fig. 1). The photons are coupled into the waveguide from one of the fibre through the input grating coupler, while parts of them are output from the other calibration grating coupler, collected with another optical fibre in the same fibre array, and finally detected with a calibrated room-temperature photodetector. This cryogenic optical set-up not only guarantees multiple optical and radiofrequency channels input/output, but also allows for the measurement of multiple devices in a single round of cool-down.

The pulsed coherent light source is generated by gating a tunable continuous-wave laser (New Focus 6427 Vidia-Discrete) with the cascaded EOMs and acoustic-optic modulator, which guarantees subnanosecond narrow pulse width combined with a  $>100$  dB extinction ratio to efficiently suppress the background photons. The thermal light source is generated by employing the same gating method but with the EDFA/narrow-bandwidth spectral filter chain to replace the continuous-wave laser part. A more detailed description on the measurement set-up can be found in Supplementary Note 2.

# Timing jitter characterization

We use a femtosecond laser (Toptica FemtoFiber pro IR) to characterize the timing jitter of each detector pixel. A beam-splitter along with a high-speed photodetector are used to provide the synchronization signal of the laser, and a high-speed oscilloscope (Teledyne LeCroy HDO9404-MS) is employed to measure and build the histogram for the arrival time difference between the synchronization signal and the pulses generated by the detector pixels. The histogram is shown in Extended Data Fig. 1a, where each peak corresponds to the 100 individual pixels. The zoomed-in data for the 1st, 50th and 100th pixels are also shown in Extended Data Fig. 1b-d. It can be seen that the timing jitter, which is defined by the FWHM of the histogram peak, is

relatively small (~50 ps) for low pixel numbers and large (~90 ps) for high pixel numbers. This is because the signals from the detector of high pixel numbers have relatively lower peak voltage, which is caused by the larger ohmic loss from the top metal ground of the microwave transmission line after longer propagation (see Fig. 1g of the main text). The lower peak voltage in turn leads to lower signal-to-noise ratio and thus increases the noise-induced jitter. In a future work, the current aluminium ground of the transmission line could be replaced by other superconducting materials at the operation temperature of the device (such as niobium or NbN) to minimize the propagation loss of the detector signals.

# On-chip detection efficiency and dark count rate characterization

We use the EDFAs and a bandwidth-tunable filter (Oz Optics BTF-11) to generate a 3-nm-bandwidth thermal light to characterize the grating coupler efficiency as well as the on-chip detection efficiency of the detector. A relatively broadband light source is used here because of its short coherence length to mitigate the reflection-induced interference between two grating couplers. As shown in Extended Data Fig. 2a, we use a symmetric design to facilitate the efficiency measurement. Here we assume that both of the grating couplers and Y-splitters perform identically. The total optical transmission between the two grating couplers is measured to be  $T_{\mathrm{tot}} = 0.088\%$ , including two Y-splitters, and thus the fibre-to-detector transmission efficiency through one Y-splitter is  $T_{\mathrm{det}} = \sqrt{T_{\mathrm{tot}}} = 2.97\%$ . Based on this result, we can estimate the on-chip optical power carried by the waveguide and further infer the on-chip input mean photon number  $\bar{n}_{\mathrm{in}}$  with the calibrated attenuation by the optical attenuators. The on-chip detection efficiency can then be calculated as  $(\bar{n}_{\mathrm{det}} - n_{\mathrm{dark}}) / \bar{n}_{\mathrm{in}}$ , where  $\bar{n}_{\mathrm{det}}$  and  $n_{\mathrm{dark}}$  are the mean number of pulses detected by the PNR detector and the dark count rates, respectively. Extended Data Fig. 2b illustrates the measured on-chip detection efficiency and dark count rates versus the bias current  $I_{\mathrm{b}}$  applied to the detector. The efficiency is measured with a relatively low input photon number  $n_{\mathrm{in}} = 1.2$  and recorded as  $88.5\%$  at the bias current of  $I_{\mathrm{b}} = 18~\mu \mathrm{A}$ , where the dark count is still at few-hertz level. The maximum efficiency reaches  $95.5\%$  and saturates, when the bias current is applied very close to the switching current  $(I_{\mathrm{sw}} = 19.5~\mu \mathrm{A})$ . By using thinner NbN film and narrower nanowire width, detectors can be made with wider saturation plateau in the efficiency curve[45], and thus they can provide near-unity efficiency while operating in the regime of low dark count rate. The typical bias current used for the detector in the photon statistical measurement is  $18~\mu \mathrm{A}$ .

We measure the individual pixel detection efficiency by calculating the total counts  $C_i$ , where  $i = 1, 2, \dots, 100$  for each detector pixel via summing up the counts for each histogram peaks in Extended Data Fig. 1a. The individual pixel efficiency is thus calculated by  $E_i = C_i / \sum_{j=1}^{100} C_j$  and plotted in Extended Data Fig. 2c. The efficiency drops substantially for the middle 49th to 52nd pixels, as the nanowire detectors of these pixels are located at the end of the optical waveguide, and thus the absorption is limited by the finite length of the nanowires (see Fig. 1b of the main text). The uniformity of the pixel efficiencies could be further improved by better engineering of the nanowire detector length and position in the future. It requires a series of dedicated experimental tests, such as detailed measurement of the nanowire absorption efficiency versus the width, length, thickness, and the position of the nanowire on the waveguide. The results could then be compared with the simulation to obtain a more exact nanowire absorption efficiency model that could be applied in the future device design.

The detected mean photon number as a function of the input mean photon number  $\bar{n}_{\mathrm{in}}$  at the fixed bias current  $I_{\mathrm{b}} = 18~\mu \mathrm{A}$  is shown in Extended Data Fig. 2d. The detected mean photon number saturates as  $\bar{n}_{\mathrm{in}}$  increases, due to the increased probability of more than

two photons hitting identical pixels increases $^{27}$ . Some of the photons are missing in this case, as each detector pixel can only output one electrical pulse for multi-photon excitation. We verify this hypothesis by performing Monte Carlo simulations, in which we model the detector with 101 pixels, and the 101st pixel is the loss channel. For a single input photon, the probability of each pixel for detecting this photon is  $P_{i}$ , where  $i = 1, 2, \ldots, 101$ . We thus have  $P_{101} = 11.5\%$  and  $P_{i} = 0.885E_{i}$ , where  $i = 1, 2, \ldots, 100$  and  $E_{i}$  is the single-pixel efficiency as shown in Extended Data Fig. 2c. For a single input photon, we can generate a random number  $1 \leq k \leq 101$  following the probability distribution of  $P_{i}$  to determine which pixel will detect this photon. When the input pulse contains  $N$  photons, we generate  $N$  random numbers  $k_{1}, k_{2}, \ldots, k_{N}$  and then count how many pixels (except the 101st pixel) are fired. As a specific example, when  $N = 4$ , the numerically generated random numbers are  $k_{1} = 4$ ,  $k_{2} = 4$ ,  $k_{3} = 5$  and  $k_{4} = 101$ , which means that the fourth and fifth pixels are fired while one photon is annihilated due to loss. As two pixels are fired, the detected photon number is two. We repeat this process many times and thus we can get a probability distribution  $U_{i,j=N}(i = 0, 1, 2, \ldots)$ . The value of  $U_{i,j=N}$  represents the probability of detecting  $i$  photons when the input pulse contains  $j = N$  photons. Obviously, we have  $U_{i,j=N} = 0$  when  $i > N$  and  $\sum_{i=0}^{N} U_{i,j=N} = 1$ . We next scan the value of  $j$  and finally arrive at a two-dimensional matrix  $U_{ij}$ . When the input pulse follows a Poisson statistics as  $P_{j} = P_{\mathrm{P}}(n = j; \bar{n}_{in})$  where  $\bar{n}_{in}$  is the input mean photon number, the detected photon number probability distribution can be computed as  $P_{\mathrm{det}}(n = i) = \sum_{j} U_{ij} P_{j}$ . The detected mean photon number is  $\bar{n}_{\mathrm{det}} = \sum_{n} n P_{\mathrm{det}}(n)$ . For an ideal detector with  $100\%$  efficiency and perfect PNR capability, we have  $U_{ij} = I$ , where  $I$  is the identity matrix and the detected photon number distribution is shown as a function of the input mean photon number in Extended Data Fig. 2e. For our detector, we use Monte Carlo simulation to numerically compute  $U_{ij}$ , and the simulated probability distribution is shown Extended Data Fig. 2f, which agrees well with our experimental data shown in Extended Data Fig. 2g. It can be seen that the detector saturation effect transforms a Poisson distribution to a sub-Poisson distribution, and the detected mean photon number is lower than the actual input mean photon number.

# Data availability

The data are available via Zenodo at https://doi.org/10.5281/zenodo.7240400.

# Code availability

The Monte Carlo simulation code for Extended Data Fig. 2f is available via Zenodo at https://doi.org/10.5281/zenodo.7240400.

# Acknowledgements

This work is funded by the National Science Foundation (NSF) through ERC Center for Quantum Networks (CQN) grant (grant no EEC-1941583). We acknowledge early funding support for this project from DARPA DETECT program through an ARO grant (grant no. W911NF-16-2-0151) and NSF EFRI grant (grant no. EFMA-1640959). Y.Z. acknowledges the support from the Yale Quantum Institute fellowship. We would like to thank Y. Sun, S. Rinehart, K. Woods and M. Rooks for their assistance provided in the device fabrication. The fabrication of the devices was done at the Yale School of Engineering and Applied Science (SEAS) Cleanroom and the Yale Institute for Nanoscience and Quantum Engineering (YINQE).

# Author contributions

R.C., Y.Z. and H.X.T. conceived the idea and experiment. R.C. designed and fabricated the devices. R.C., Y.Z., S.W., M.S. and T.T. performed the measurements. R.C. and Y.Z. analysed the data. R.C., Y.Z. and H.X.T. wrote the manuscript with inputs from all authors. H.X.T. supervised the project.

# Competing interests

The authors declare no competing interests.

# Additional information

Extended data is available for this paper at https://doi.org/10.1038/s41566-022-01119-3.

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41566-022-01119-3.

Correspondence and requests for materials should be addressed to Hong X. Tang.

Peer review information Nature Photonics thanks Tim Bartley and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permissions information is available at www.nature.com/reprints.

![](images/c0f3e16356b485367af4a3d67ccfd5d67ca9c2beecc9f2aeba104149650dee01.jpg)

![](images/c7624bbab7b87f36699052089583ee9ed1e144f988c48be0b7cef68fc439caf7.jpg)  
Extended Data Fig. 1 | Timing jitter characterization. a, Histogram measured for the arrival time difference between the laser synchronization signal and the detector pulses from 100 individual pixels. The full width at half maximum

![](images/e6a23e2afca00435c8714259e3d73ac294ceb4c31dc2110bf811dab9c42683b9.jpg)  
(FWHM) of each peak defines the timing jitter of the corresponding detector pixel. b-d, Zoom-in histogram data of the (b) 1st, (c) 50th, and (d) 100th detector pixel.

![](images/680e767b367f68aadaf4e9e24c18e818899d03ec1465cfd95761ba6c503ba3d8.jpg)

![](images/db58e6997f49b997a210ec91084e4bf3136635a81a1f027fac98577a4d4f8fb5.jpg)

![](images/0c2311dd4bfa9ab3e94cc2186766bc95bd5dc343038f27d7452fa2b1fbc2a767.jpg)

![](images/821be987a209c624e701e4baa301108b4da57bd0d4f55cd1c3d478485fb912a0.jpg)

![](images/0a6c29f97c69f9aea95dea18a3ac7ba645b187e54e149bc482692232a3911489.jpg)  
Extended Data Fig. 2 | On-chip detection efficiency and dark count rate characterization. a, Grating coupler pair design for the measurement of on-chip detection efficiency of the device. b, On-chip detection efficiency and dark count rates measured as a function of the bias current  $I_{\mathrm{b}}$ . c, Detection efficiency measured for individual 100 detector pixels. d, Detected mean photon number as a function of the input mean photon number  $\bar{n}_{\mathrm{in}}$ . The measurement is

![](images/1d39418cbece7f9745d23b68c81bdd30124cd720be3fe5df8186a824875998e8.jpg)  
performed with the bias current  $I_{\mathrm{b}} = 18\mu \mathrm{A}$ , and the measured results agree well with the Monte Carlo simulation. e-g, Detected photon number distribution versus input mean photon number  $\bar{n}_{\mathrm{in}}$ , e, Calculated results for an ideal detector assuming  $100\%$  detection efficiency and infinite photon number resolution, f, Monte Carlo simulation for a 100-pixel detector taking into account the saturation effect. g, Experimentally measured data.

![](images/83bc21bca3762c9323bbb56c11bbdca8168f39b1bd66bf5dd7289ce8e31f0982.jpg)

![](images/6d4519a4a03863776520f70f7c4afd9425b6a5a6badcd9000cd6eb983a96808a.jpg)