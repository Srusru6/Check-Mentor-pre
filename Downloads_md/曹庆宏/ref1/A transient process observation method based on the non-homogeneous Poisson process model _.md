PAPER

# A transient process observation method based on the non-homogeneous Poisson process model

To cite this article: Kuo Zhao et al 2021 Chinese Phys. C 45 045001

View the article online for updates and enhancements.

# You may also like

Zipf law: an extreme perspective  
Iddo Eliazar  
- Demand Forecast of Restoring Air Material of Helicopter Based on NHPP and Weibull Model  
Penghui Niu, Zhen Wang, Suyong Liu et al.  
- Nitrogen-doped hollow porous carbon nanospheres coated with  $\mathrm{MnO}_2$  nanosheets as excellent sulfur hosts for Li-S batteries

Xiaolong Zhang, He Yang, Junling Guo et al.

# A transient process observation method based on the non-homogeneous Poisson process model*

Kuo Zhao(赵括)1 Xiao-Ping Ouyang(欧阳晓平) $^{2,3}$  Hui-Ping Guo(过惠平) $^{1}$  Liang Chen(陈亮) $^{2\dagger}$  Lei-Dang Zhou(周磊荡) $^{4}$  Jin-Lu Ruan(阮金陆) $^{2}$  Han Wang(王涵) $^{1}$  Ning Lv(吕宁) $^{1}$  Run-Long Gao(高润龙) $^{4}$ $^{1}\mathrm{Xi}^{\prime}$  an Research Institute of Hi-Tech, Xi'an 710025, China  $^{2}$  Northwest Institute of Nuclear Technology, Xi'an 710024, China  $^{3}$  Department of Engineering Physics, Tsinghua University, Beijing 100084, China  $^{4}$  Xi'an Jiaotong University, Xi'an 710049, China

Abstract: The current-mode-counting method is a new approach to observing transient processes, especially in transient nuclear fusion, based on the non-homogeneous Poisson process (NHPP) model. In this paper, a new measurement process model of the pulsed radiation field produced by transient nuclear fusion is built based on the NHPP. A simulated measurement is performed using the model, and the current signal from the detector is obtained by simulation based on Poisson process thinning. The neutron time spectrum is reconstructed and is in good agreement with the theoretical value, with its maximum error of a characteristic parameter less than  $2.3\%$ . Verification experiments were carried out on a CPNG-6 device at the China Institute of Atomic Energy, with a detection system with a nanosecond response time. The experimental charge amplitude spectra are in good agreement with those obtained by the traditional counting mode, and the characteristic parameters of the time spectrum are in good agreement with the theoretical values. This shows that the current-mode-counting method is effective for the observation of transient nuclear fusion processes.

Keywords: non-homogeneous poisson process, pulsed radiation field, current-mode-counting method

DOI: 10.1088/1674-1137/abde30

# I. INTRODUCTION

In the fields of astrophysics and nuclear physics, it is important to observe some transient processes which indicate important physical information. Accurate observation of the pulse arrival time of a pulsar is expected to be used to monitor and modify the long-term frequency stability of atomic clocks [1]. The neutron time spectrum of nuclear fusion indicates the nuclear reaction process [2]. The processes of solar flares erupting [3] and nuclear explosions [4] are all transient, with the total number of neutrons increasing at the beginning and then decreasing.

In recent years, pulsed radiation sources have become very important in the defense and nuclear energy industries because they can produce high intensity radiation particles in a short time [5, 6]. The output of those devices is discontinuous when operated in pulsed mode or at relatively long intervals [7]. Typical examples are pulsed accelerator neutron sources [8, 9], Tokamak devices [10], and spallation neutron sources [11-13]. As is well-known, the energy spectrum and number of neut

rons produced by fusion reactions can be used to characterize the temperature and the total amount of reaction products [14, 15]. The pulsed neutron flux [16], energy spectrum [17, 18] and time structure [19, 20] are the most important parameters in measuring a pulsed neutron process.

Traditionally, two modes are used in observation: counting mode and current mode [1]. The main characteristics and the equivalent circuit diagrams of these two modes are given in Table 1. In counting mode, the amplitude of a signal pulse is proportional to the charge generated in the detector, which means this method is suitable for pulse amplitude spectra indicating the total energy measurement [21, 22]. Because the response time of the measuring device is usually longer than the interval time of the particle pulse, the loop current  $I(t)$  is the average of the interaction effect between the particle flux and the detector [23]. The current output is proportional to the energy deposited in the detector by the particles. For the detection of single-energy particles, the total deposition energy is directly proportional to the number of particles.

Table 1. Main features of counting mode and current mode.  

<table><tr><td></td><td colspan="2">counting mode</td><td colspan="2">current mode</td></tr><tr><td>Equivalent circuit</td><td>Detector</td><td>C=R V(t)</td><td>Detector</td><td>I(t)</td></tr><tr><td>Output category</td><td colspan="2">Voltage</td><td colspan="2">Current</td></tr><tr><td>Output size</td><td colspan="2">Vmax = Q/C</td><td colspan="2">I0 = rQ = rE/Wq</td></tr><tr><td>Typical applications</td><td colspan="2">Energy spectrum measurement</td><td colspan="2">Time spectrum measurement</td></tr><tr><td>Measurement object</td><td colspan="2">Single particle</td><td colspan="2">Particle flux</td></tr><tr><td>Output characteristic</td><td colspan="2">Output is proportional to the deposition energy</td><td colspan="2">Output is proportional to the number of particles and the energy of particles</td></tr><tr><td>Limitations</td><td colspan="2">Dead time, low counting rate (≤10^6 s^-1)</td><td colspan="2">Single particle information lost</td></tr></table>

In counting mode,  $R$  is the equivalent resistance of the measuring circuit,  $C$  is the equivalent capacitance,  $V(t)$  is the output signal of the detector, and  $Q$  is the charge generated by a single particle in the detector. In current mode,  $r$  is the event rate,  $Q = Eq / W$  is the amount of charge produced by particles interacting with the detector,  $E$  is the deposition energy,  $W$  is the mean ionization energy, and  $q$  is  $1.60 \times 10^{-19}$  C.

Therefore, the particle intensity can be characterized by the output current [24, 25].

For the beginning and end stages of a high-intensity pulse, such as fusion ignition of a Tokamak, these phases often reflect important physical processes, so their flux measurement is very important [26]. If current-mode detectors are used directly, the results of these phases cannot meet the statistics requirements due to the small number of particles in the instantaneous measurement, and only the peak phases can meet the statistical requirements. In order to obtain an accurate neutron signal and reduce the uncertainty from accompanying  $\gamma$  rays, it is necessary to discriminate neutrons from  $\gamma$  rays. Current mode cannot address this measurement. If counting mode is used, the detection efficiency cannot be high, otherwise the counting channel will be blocked. For a pulsed field with a short pulse duration whose process is irreversible, the number of particles entering the detector is low, and the results are insufficient to meet the necessary statistical precision. The traditional counting mode and current mode therefore both have disadvantages. For the scenario when the neutron intensity is between the steady-state radiation field and the high-intensity pulsed radiation field, it is no longer appropriate to use these methods.

In order to solve the measurement dilemmas of the above two methods, the current-mode-counting method was proposed [27, 28]. The current-mode-counting method is a detector operation mode in which the detection system is formed by a current-mode detector and a high-bandwidth current amplifier, and an independent current waveform is measured for each particle. Since a single particle corresponds to an independent current waveform, the arrival time, energy and type of the incident particles can be obtained simultaneously. The waveform width is determined by the detector. The response time for a single particle is of the order of nanoseconds or picoseconds when fast-response detectors are used. This

method can improve the effective counting rate compared with the counting mode.

# II. THEORETICAL MODEL DESCRIPTION

For a steady-state radiation field, such as the radiation field produced by an isotope source, the measurement within a short time can be described by a Poisson process, and the decay constant  $\lambda$  is used to represent the number of particles emitted per unit time [1]. Similarly, the number of signals in the detector generated by the pulsed source in a very short time window can be regarded as the result of one Poisson sampling, and the short time window can be represented by  $[t_i - 0.5\triangle T, t_i + 0.5\triangle T](\triangle T \to 0)$ . For different time windows, the measurement process is independent. Let the independent incremental process be represented by  $\{Y(t), t \geqslant 0\}$ . If there is a function  $\lambda(t)$  and two random moments  $s, t$  ( $s < t$ ) and  $\{Y(t), t \geqslant 0\}$  obeys the Poisson distribution with the representation

$$
\int_ {s} ^ {t} \lambda (u) \mathrm {d} u, \tag {1}
$$

then  $\{Y(t), t \geqslant 0\}$  is called a non-homogeneous Poisson process (NHPP) with the parameter  $\lambda(t)$  [29].

By setting the time spectrum of the pulsed neutron source as  $y(t)$ , which represents the number of neutrons emitted per unit time, then the total number of neutrons is represented by

$$
Y (t) = \int_ {0} ^ {t} y (t) \mathrm {d} t. \tag {2}
$$

When  $\eta$  represents the absolute detection efficiency (the ratio of the absolute signal number produced in the detector to the number of neutrons emitted from the pulsed source), then the actual time spectrum of neutrons interacting with the detector can be described by

$$
y _ {1} (t) = \eta y (t). \tag {3}
$$

Let  $f(\mathrm{GHz})$  be the sampling frequency of the detection system. In the time window close to the occurrence of  $t_i$  with a width of  $\triangle T$ , the detection process takes  $y_1(t)$  as the parameter for Poisson sampling, and the theoretical number of particles observed is

$$
N _ {1} \left(t _ {i}\right) = \int_ {t _ {i} - 0. 5 \Delta T} ^ {t _ {i} + 0. 5 \Delta T} y _ {1} (t) \mathrm {d} t = \int_ {t _ {i} - 0. 5 \Delta T} ^ {t _ {i} + 0. 5 \Delta T} \eta y (t) \mathrm {d} t. \tag {4}
$$

For the detection process of recording the neutrons, each time window is independent. Therefore,  $N_{1}(t)$  can be regarded as a sampling of the NHPP in the duration  $T$  of the pulsed radiation field. The value of  $N_{1}(t_{i})$  is determined by the width of the observing window  $\triangle T$ , the intensity of the time spectrum  $y(t_{i})$ , and the absolute detection efficiency  $\eta$ . When the neutron arrives, it produces an impulse function  $\delta (t)$  (whose amplitude equals 1). The total number in each  $\triangle T$  is limited to less than or equal to 1 by improving the sampling frequency and controlling the detection efficiency. When the particles enter the detector, an impulse sequence combined with multiple impulses is obtained. The function  $g(y,f,\eta)$  is defined as the above non-homogeneous Poisson sampling process. Using that definition, the above process can be expressed as

$$
y (t) \xrightarrow [ \eta ]{f} \text {区} \rightarrow x (t). \tag {5}
$$

The function  $x(t)$  is used to represent the impulse sequence (whose value is either 0 or 1) formed by the above process. Obviously, near a certain moment, the denser value 1 is, the stronger the pulsed source is. The response function of the detector to the single particle is denoted by  $h(t)$ . After a neutron enters the detector at  $t_i$ , the detector responds to the  $\delta(t_i)$  with an independent current waveform. After the particle flux enters the detector, the detector output can be expressed as

$$
F (t) = g (y (t), f, \eta) * h (t), \tag {6}
$$

where the symbol  $\text{串} ^ { \text{串} }$  represents a convolution.

In the current-mode-counting method, a pulsed radiation field measurement uses the characteristic parameter  $y(t)$  from the measured result  $F(t)$ . The original information  $y(t)$  of the pulsed neutron radiation field is reconstructed based on the reverse process of the above model, as shown in the simulation verification and experimental verification.

# III. SIMULATION VERIFICATION

# A. Simulation of the response process of organic

# scintillator detector to pulsed radiation field

The output of the pulse radiation field in the detector can be simulated based on the NHPP simulation method. The current-mode-counting mode was verified by using the above ideas after the detector output was simulated. Non-homogeneous Poisson sampling results were obtained by using Poisson process thinning [30]. The single particle impulse signal was converted into a detector output according to the response function described by Eq. (6).

The simulation process is represented by Figs. 1 and 2. First, one sets the time spectrum as  $y(t)$ , which represents the number of neutrons emitted from the pulsed radiation source per unit time. It is also the intensity function of the NHPP. Then, the absolute detection efficiency  $\eta$  is introduced and the response time spectrum  $y_{1}(t)$  of the detector obtained, which represents the number of neutrons reacting with the detector. The measured impulse sequence  $x(t)$  is then obtained based on Poisson process thinning. The amplitude 1 indicates that a neutron entered the detector and produced a signal output at that moment.

In this paper, the given time spectrum of the pulsed neutron source is described by Eq. (7):

$$
y = A \times e ^ {- \frac {\left(t - t _ {c}\right) ^ {2}}{2 \times \sigma^ {2}}}. \tag {7}
$$

![](images/8b4136136e8d263050780a0d097a5bf6ce926900fa0b3d8b9ae2e7630dc5573a.jpg)  
Fig. 1. Flow diagram of the simulation of pulsed radiation field impact detectors.

![](images/adab9b6696c79829f0720748e6256f7be7303147707fd62271237b8453e4002c.jpg)  
Fig. 2. Flow diagram of detector response to the shock sequence  $x(t)$ .

The time spectrum is Gaussian, the sampling duration is  $\mathrm{T} = 20~\mu \mathrm{s}$ , the peak appears at  $t_c = 8~\mu \mathrm{s}$ , full width at half maximum (FWHM) is  $2.94~\mu \mathrm{s}$  and this pulsed source produces a total of  $2.5\times 10^{7}$  neutrons.

The neutron single particle pulse amplitude is defined according to the neutron pulse amplitude distribution function  $H_{n}(t)$ . Near the neutron signal, a gamma signal with random amplitude  $H_{\gamma}(t)$  is generated according to the probability ratio of  $n / \gamma$  (0.2 in used in this paper). The delay time  $\triangle t$  of the  $n / \gamma$  peak is also described by a random distribution. After the above process, the output  $F(t)$  is obtained and the results of the simulation are shown in Fig. 3. An oscilloscope with high bandwidth and high sampling rate is used as the analog signal acquisition system. The highest sampling rate of the oscilloscope is  $f = 10 \mathrm{GHz}$ . Figure 3 show the simulated output of detectors with absolute detection efficiency of  $2 \times 10^{-6}$  when the equivalent resistance of the output circuit is  $50 \Omega$ .

# B. Pulsed radiation field information reconstruction

According to the model, the time spectrum  $y(t)$  can be created with the following steps:

1. Obtaining the particle signal  $F(t)$  of pulsed neutron radiation field from the detector array

For a Poisson process, it has been shown mathematically that the mean value of many multiple sampling results is the maximum likelihood estimation of the waveform process parameter  $\lambda$ . The average value of multiple experiments can be obtained by repeated pulse measurements in a repeatable pulse radiation field, such as at the China Spallation Neutron Source (CSNS). If the neutron is produced by an unrepeatable pulse, the signals can be collected by placing multiple detectors.  $\tilde{y}_1(t_1)$ , which estimates  $y_{1}(t)$ , can be expressed as follows:

$$
\tilde {y} _ {1} \left(t _ {i}\right) = \frac {\sum_ {1} ^ {j} \hat {y} _ {1 , j} \left(t _ {i}\right)}{j} = \frac {\sum_ {1} ^ {j} \hat {N} _ {1 , j} \left(t _ {i}\right)}{j \Delta T}, \tag {8}
$$

where  $j$  is the number of the detectors with an identical detection efficiency or the repetition number of the repeatable pulsed neutron source.

To collect as many particles as possible in a limited time and reduce particle pile-up, the detector's response time to a single particle should be as short as possible. In addition, the detection system should be able to discriminate neutrons from  $\gamma$  rays. A detection system consisting of stilbene crystals and photomultiplier tubes can be used for experimental measurements based on the current-mode-counting mode. At this step, the output signal  $F(t)$  was obtained as shown in Fig. 3.

2. Information acquisition of particle flux based on waveform digitization technology

After accumulating multiple impulses in the time dimension, the output signal is represented as  $\widehat{F}(t)$ . The peak finding,  $n/\gamma$  discrimination, peak height interpretation and peak position identification was carried out by waveform digitization processing. After peak finding for a single particle, the amplitude value and arrival time can be obtained directly and the charge can be obtained by integrating the particle waveform.

Theoretically, the impulse of a single particle can be obtained by deconvolution as

$$
x (t) = g (y (t), f, \eta) = \mathcal {F} ^ {- 1} \left[ Y _ {F} (\omega) / H (\omega) \right], \tag {9}
$$

![](images/0a44203a8aa01f41cb40969a61b98d22167542e3b896a4fc1e8d31946edb9681.jpg)  
Fig. 3. (color online) Simulation detector output obtained by only one detector at detection efficiency of  $2 \times 10^{-6}$ .

where  $Y_{F}(\omega)$  and  $H(\omega)$  are the frequency domain transformation of  $F(t)$  and  $h(t)$ , and  $\mathcal{F}^{-1}$  is the identifier of deconvolution. However, the pulse amplitudes are random and the deconvolution operation is very complicated. A simple approach is to assign a  $\delta (t)$  pulse directly at the peak location of a single particle and convert the output signal  $\widehat{F} (t)$  to an impulse sequence,  $\widehat{x} (t)$ . At the same time, in the waveform digitization process, the neutron amplitude information is reserved for the calculation of the pulse amplitude spectrum, and the charge information of the neutron is reserved for the calculation of the charge amplitude spectrum. For time spectrum  $y(t)$ , after this step,  $\widehat{x} (t)$  is as shown in Fig. 4.

3. Calculation of characteristic parameters  $y(t)$  of pulse radiation field based on a statistical algorithm

There is an amplitude for every  $\triangle T = 1 / f$  (ns) in the impulse sequence  $\widehat{x} (t)$  as shown in Fig.4. The result is so discrete that it cannot directly reflect the change of pulse source intensity with time. Therefore, a time spectrum reconstruction algorithm is needed. Two reconstruction algorithms are proposed in this paper. The first is the window-by-window statistics algorithm (WWS) and the second is wavelet packet transformation (WPT).

When using the WWS algorithm, a time window with a width is set and represented by the midpoint of the window. The total number of neutrons is counted for each window. Then, a series of points  $[t_i,\widehat{N}_1(t_i)]$  is obtained. In this algorithm, one sets the width of the statistical window as  $t_\mathrm{w}$ , the pulse duration is  $T$ , and the step size of each window moving backward is  $\triangle \tau$ . Then, one lets  $n_0$  represent the number of points of the reconstructed time spectrum where  $n_0 = T / \triangle \tau$ . For  $[t_i,\widehat{N}_1(t_i)]$ , except for the elements in the first statistical window  $t_\mathrm{w}^1$  and the last window  $t_\mathrm{w}^{n_0}$ , each point in other time windows of the intermediate moment is used  $m$  (equal to  $t_\mathrm{w} / \triangle \tau$ ) times in the summation calculation. Therefore, in order to ensure the accuracy of calculation, the value of  $T$  should be longer than the pulse duration so that  $\widehat{N}_1(t_i)$  at the beginning and end is zero. Then, the neutron time spectrum observed by the detector is

$$
\hat {y} _ {1} (t) = \frac {\hat {N} _ {1} \left(t _ {k}\right)}{m \Delta T}. \tag {10}
$$

The basic principle of the WPT algorithm is that energy is conserved in each wavelet packet transformation

[31]. The impulse sequence  $x(t)$  is transformed into an energy sequence  $xx(t)$  as

$$
x x (t) = \left\{ \begin{array}{c} \sqrt {x (t)}, \quad x (t) > 1 \\ x (t), \quad \text {o t h e r s .} \end{array} \right. \tag {11}
$$

Energy conservation can be expressed as follows:

$$
\int_ {- \infty} ^ {+ \infty} x x ^ {2} (t) \mathrm {d} t = \frac {1}{C _ {p}} \int_ {- \infty} ^ {+ \infty} \left| W _ {p} ^ {2} (\omega) \right| ^ {2} \mathrm {d} \omega , \tag {12}
$$

where  $W_{p}(\omega)$  is the wavelet packet transform coefficient of  $xx(t)$ ,  $p$  is the basis function of the wavelet packet transform, and  $C_p$  is a constant and equal to one. The basis function, which is close to the single particle waveform, is selected such that the wavelet system of the Daubechies multilayer wavelet packet transformation can be performed. When the decomposition layer number is  $q$ , the total number of nodes in this layer is  $2^q$  and the number of coefficients corresponding to each node is represented by  $n_q$ . The ordinate of the time spectrum is obtained by summation of the coefficients squared of the same position at each node. Therefore, the reconstructed time spectrum is composed of  $n_q$  discrete points.

# 4. Absolute detection efficiency correction

The absolute detection efficiency  $\eta$  of the detector can be obtained based on Monte Carlo simulation when the emission angle of the pulsed neutron, detector distance, particle energy, crystal type and size and other detection conditions are known. On the other hand, the absolute detection efficiency of a single energy point can be obtained by calibration. The time spectrum of the pulsed radiation source is obtained after  $\hat{y}_1(t)$  is divided by the absolute detection efficiency  $\eta$ , and the total number of neutrons  $\hat{Y}$  is obtained by integrating the full spectrum  $\hat{y}(t)$ .

Both WWS and WPT algorithms were used in this simulation. The parameters of the WWS algorithm were set to  $t_{\mathrm{w}} = 0.8 \, \mu \mathrm{s}$  and  $\triangle \tau = 20 \, \mathrm{ns}$ . The counting time is  $20 \, \mu \mathrm{s}$ ,  $n_0 = 1000$ ,  $m = 40$ . For the WPT algorithm,  $q = 12$ , "db3" (the third basis function of the Daubechies series) [32] was used as the basis function, and the time spectrum  $\hat{y}_1(t)$  was reconstructed by Eq. (12). A Gaussian fitting tool was used to fit the reconstructed time spectrum

![](images/8d98a6a02a4ad84a5df41d9dc92648b2decfcc3fcc8a7fbee37bfb4101c18bbe.jpg)  
Fig. 4. (color online) The impulse sequence  $\widehat{x}(t)$  from  $F(t)$  after step (a) in Fig. 3.

of these two algorithms to obtain the parameters in Eq. (7). Comparing the theoretical parameters and simulation results, the maximum error of those characteristic parameters is less than  $2.3\%$ , which is the relative error of  $\sigma$  obtained by the WWS algorithm. As shown in Fig. 5, both algorithms can effectively reconstruct the neutron time spectrum. The simulation results show that the current-mode-counting method can be used to effectively measure the pulsed radiation field.

# IV. EXPERIMENTAL VERIFICATION

# A. Neutron source

At the China Institute of Atomic Energy, the CIAE 600-kV nanosecond-pulse neutron generator (CPNG-6) can work in pulsed mode by using its deuterium ion source [33]. A verification experiment was carried out based on the pulsed neutron radiation field generated by CPNG-6. Neutrons are generated from D-D or D-T nuclear fusion, when the deuterium ion beam bombs a deuterium/tritium target. The ion beam cutter has good stability and can produce a deuterium beam with a width of 5  $\mu$ s at a frequency of  $1\mathrm{Hz}$ . According to the principles of nuclear reactions, a pulsed neutron beam with a width of

![](images/ebf8ec4f6938378eb1c93558b7aea30ec732f278a217dbfda9333338ee886dde.jpg)  
Fig. 5. (color online) Comparison of time spectrum obtained by two algorithms, with the theoretical value.

$5\mu \mathrm{s}$  can be produced.

# B. Experimental setup

The experimental layout is shown in Fig. 6. A square wave signal was sent to the oscilloscope as an external trigger signal and time base zero point when the ion source cutter opened the door. The detector output and the external trigger signal in the time window between -1 and  $9\mu \mathrm{s}$  were stored by the oscilloscope. Stilbene crystals were near the entry windows of the photomultipliers (PMTs, model ETL-9815), sealed in stainless steel sleeves to shield them from light and electromagnetic interference. In order to obtain fine signal details, a HDO8108A oscilloscope manufactured by Teledyne LeCroy was used, with a maximum sampling rate of  $10\mathrm{GHz}$  and bandwidth of 12 bits. The detector was placed on the same horizontal plane as the beam channel. In order to prevent the detector from losing the single particle waveform signal when it was saturated at a high flux, the detector was situated a distance  $D$  away from the central axis, and a distance  $L$  from the target head. In this experiment, a deuterium ion beam was used to bombard the tritium target. It produced a  $14.1\mathrm{MeV}$  monoenergetic neutron beam. More detailed experimental conditions are presented in Section IV.C. After a certain amount of data was accumulated, the information of the pulsed radiation field was reconstructed.

# C. Experimental results and discussion

# 1. Neutron / gamma discrimination

The experimental conditions and  $n / \gamma$  discrimination results are listed in Table 2, and the  $n / \gamma$  distribution is shown in Fig. 7. The charge integral method [34] was used for waveform discrimination. For each particle waveform, the integral time was zero at the peak moment.  $Q_{\mathrm{total}}$  was the current integral result from -10 ns to +60 ns, and  $Q_{\mathrm{slow}}$  the result from +10 ns to +60 ns. The peak-seeking algorithm could not find the second peak in the range of (-10, 60) ns after the first peak was found. The PSD charge distribution graph was obtained after thou

![](images/027f18dd048268558726c7e0541b69cdae7d1c360236765f0ad419185d260cbe.jpg)  
Fig. 6. (color online) Experimental layout.

sands of pulses and the result is shown in Fig. 7. In the process of analysis, only the waveform, voltage and charge of single particles that could be completely separated were counted. The waveforms of the pile-up signals were not counted, and are denoted "pile-up signal".

The detector for group (c) was closer to the central axis of deuterium ion beam, had a higher neutron yield, and a larger neutron probability than the other groups. The other three positions were the same, so the neutron probability was similar, about  $60\%$ . In order to improve the signal-to-noise ratio in Fig. 7(c) and 7(d), higher detector thresholds were set than in Fig. 7(a) and 7(b) so there are fewer low  $Q$  events in the pile-up strip. Based on the  $\mathrm{n} / \gamma$  discrimination result, the neutron signals were detected separately to reconstruct the charge amplitude spectra and neutron time spectra.

# 2. Charge amplitude spectrum

In the charge amplitude spectrum, the abscissa is the charge value while the ordinate is the neutron count. For

an organic scintillator, the charge value generated by the reaction is directly related to the energy of the incident particle. After the energy calibration, it is promising to obtain the neutron energy spectra by the differentiation unfolding method [35]. The charge value  $(Q_{\mathrm{total}})$  of a particle can be obtained from the stored single particle current waveform. The count of the amplitude spectra was normalized to each deuterium ion beam pulse for comparison.

In order to verify the correctness of the experimental results obtained by the current-mode-counting method, an online acquisition system based on the traditional counting mode was built, composed of CAMAC modules (QDC-7166 by Philips), a  $n / \gamma$  discrimination module (2160A by Canberra) and several NIM modules. The charge amplitude spectrum after  $n / \gamma$  discrimination can be obtained in real time by the online acquisition system. In the comparative experiment, the cutter of the particle source was removed and the same detector parameters

Table 2.  $\mathrm{n}/\gamma$  discrimination results based on the charge integral method.  

<table><tr><td>Group</td><td>Detector size/mm2</td><td>L/cm</td><td>D/cm</td><td>Number of pulses</td><td>Neutron count</td><td>Neutron probability</td></tr><tr><td>a</td><td>Φ15×5</td><td>50</td><td>10</td><td>1000</td><td>1405</td><td>59.31%</td></tr><tr><td>b</td><td>Φ25×10</td><td>50</td><td>10</td><td>1005</td><td>3513</td><td>56.15%</td></tr><tr><td>c</td><td>Φ50×10</td><td>60</td><td>10</td><td>1107</td><td>3665</td><td>69.44%</td></tr><tr><td>d</td><td>Φ50×5</td><td>50</td><td>10</td><td>1500</td><td>6453</td><td>59.85%</td></tr></table>

![](images/5cfd82b4e029bee2fe75e8ea8edee2e6e072936e5113e2e8ce4bd5b810298e11.jpg)

![](images/7c774772eeba488b96356df6f12046e71ef9f376946f61b87426a0cd7f472223.jpg)

![](images/65a2df9bc381d43dbecc8367ee011a8fc71a714ba06b50048e3c941e48a2417b.jpg)  
Fig. 7. (color online)  $n / \gamma$  discrimination results.

![](images/fd09ca0bc6e36caa3e642beec08fc8f58be8021dc410e4d79af0873c3743f21f.jpg)

used at the same position. The logic of the online collection system is based on that of Ref. [36]. Charge multichannel calibration was carried out before this experiment, and a signal generator was used to produce square waves with different charge values. The charge multichannel calibration result can be expressed as follows:

$$
Q = 0. 1 5 1 6 4 M _ {c} + 1. 0 0 0 8 9, \tag {13}
$$

where  $M_{c}$  is the charge multichannel address and  $\mathcal{Q}$  (pC) is the charge generated by a single particle in the detector.

In order to measure the background counts during operation of the accelerator, a shadow cone was placed between the accelerator target and the detectors, to shield the direct neutrons. The absolute count from the online acquisition system was obtained after the background was subtracted from the total signal. The charge amplitude spectrum of the QDC was normalized according to the results of current-mode-counting method shown in Fig. 9. Besides  $\Phi 15\times 5$  crystals, the experimental results for the other three crystals are also shown.

As shown in Fig. 8, the amplitude spectrum (in a log scale) formed by the 1405 neutrons of the group (a) experiment shows the amplitude spectrum of the organic scintillator. An amplitude edge of the maximum appears. The two kinds of experimental results show good agree

ment in Fig. 8 (b) and (d). The results of the current-mode-counting method fluctuated. This is because the count was limited but not as much as the QDC. In Fig. 8 (c), the charge amplitude spectrum obtained by the current-mode-counting method deviates slightly from that of the online acquisition at its edges, but the overall trend is consistent with the online acquisition. The thresholds of both curves are not exactly the same and the charge amplitude spectrum obtained by current-mode-counting was lower than the red one.

In Fig. 8, the output of the online acquisition system is the absolute count after the background was subtracted. The subtraction is unnecessary in the current-mode-counting method because the neutrons in the experiment hall have a very low probability of entering the detector in the active time window between  $-1$  and  $9\mu s$ . As a result, they can easily be removed, which is one of the advantages of the current-mode-counting method.

Compared with traditional CAMAC acquisition system based on counting mode, the detector system structure of the current-mode-counting method is more simple. Each particle corresponds to an independent waveform, with a response time of the order of a ns. Theoretically, the counting rate of the system can reach as high as  $10^{8}\mathrm{s}^{-1}$ . With faster scintillation crystals and other photomultiplier tubes, the theoretical counting rate can be

![](images/bdac5a60509abc8df17df0cf8a86d79cdf6f1df5d8a5b5b1c09e480c651fe9d5.jpg)

![](images/577701e708bcdc9ea3f761e2e26da5605cef0e430b8c05683feffde8988affe3.jpg)

![](images/409f1339701547d1a030110ed22109e2aa533f237201462754b02e87aa39df26.jpg)  
Fig. 8. (color online) Comparison of the charge amplitude spectra obtained by the two methods for (a)  $\Phi 15\times 5$ , (b)  $\Phi 25\times 10$ , (c)  $\Phi 50\times 10$ , and (d)  $\Phi 50\times 5$ . The red solid line is the charge amplitude spectrum obtained by the online acquisition system. The blue dotted line is the charge amplitude spectrum obtained by the current-mode-counting method. The black error bar represents the uncertainty of the experimental results (68% confidence).

![](images/3dfbc549ee61c832d09b6d8238da97ab311671662854031c27b6ae36d148ef1e.jpg)

![](images/ab841be375a61bfb911e3d9fe1e3ba7c7e20950f2a57f4a0278fe2e9ff9e3562.jpg)

![](images/99358731ac0d523fa9b926c528081a059e759be045e96904946bb13190e69e72.jpg)

![](images/37dd8d22306f513f996fe9c2503167342a7c84d1f6c6085f021603b47c15c87e.jpg)  
Fig. 9. Time spectra of the pulsed neutrons obtained by current-mode-counting method.

![](images/53cb558c0b4c339341851892613709ba7f44cf7d12e6694d4122c0df93f2d493.jpg)

higher. What is more, the charge of each particle was obtained directly by integration without the process of calibration. That is one of the advantages of the current-mode-counting mode.

# 3. Neutron time spectrum

The time spectrum of the pulse source can be characterized by the measured neutron time spectrum, because the neutron flight distance does not exceed  $60~\mathrm{cm}$  and the flight time spread is negligible [37]. Due to time constraints, the neutron detection efficiency calibration had not been carried out at the same position. Therefore, the absolute neutron detection efficiency cannot be obtained. The neutron time spectrum in this section was used to characterize the relative change of neutron intensity with time. The WWS algorithm was used in this section,  $t_w = 200$  ns and  $\triangle \tau = 10$  ns. The neutron time spectrum of the above four experiments is shown in Fig. 9.

The main parameters of neutron time structure obtained from the four experiments are listed in Table 3. The deviation from the theoretical value  $(5\mu s)$  is given in parentheses after the time value. It can be seen from this table that the half width of neutron time structure can be effectively measured based on the current-mode counting method, which is consistent with the theoretical value. Theoretically, the neutron count should be a stable straight line in the duration of the pulse. In practice, the electric tension and current of CPNG-6 target had jitter, which made it difficult to maintain a constant intensity of the emitted deuterium beam [38]. As the number of neutrons increases, the time spectra of groups a through d gradually becomes smooth, as shown in Fig. 9 (d). As can been seen in the figure, the slope is close to a straight line.

Table 3. The parameters of the neutron time spectra obtained by the current-mode-counting method.  

<table><tr><td>Group</td><td>Bottom width/μs</td><td>Half width/μs</td><td>Time start/μs</td></tr><tr><td>a</td><td>5.30(+6.0%)</td><td>5.06(+1.2%)</td><td>1.46</td></tr><tr><td>b</td><td>5.29(+5.8%)</td><td>4.99(-0.2%)</td><td>1.46</td></tr><tr><td>c</td><td>5.40(+8.0%)</td><td>5.05(+1.0%)</td><td>1.45</td></tr><tr><td>d</td><td>5.46(+9.2%)</td><td>5.05(+1.0%)</td><td>1.47</td></tr></table>

# V. CONCLUSION

The current-mode-counting method is a method in which the detection system is designed so that each particle produces an independent current waveform. Since a single particle corresponds to the independent current waveform, the arrival time, energy and type of the incident particles can be obtained simultaneously.

In this paper, the response process model of the detectors to a pulsed neutron radiation field was established. Based on the current-mode-counting method, a measurement process for a pulsed radiation field was designed. In the verification experiment, the original current waveform generated by the pulsed radiation field was stored. Based on the current-mode-counting mode, the  $n / \gamma$  discrimination results, neutron charge amplitude spectra and time spectra were simultaneously obtained. The charge amplitude spectra agreed well with the output of the CAMAC online acquisition system working in counting mode. Experimental results showed that the current-mode-counting method is an effective way to measure the pulsed neutron radiation field.

Compared with traditional detectors operating in counting mode and current mode, each particle corresponds to a current waveform, and the response time of a single particle is in the order of nanoseconds. The effective counting rate of the detection system can be increased to  $10^{8}\mathrm{s}^{-1}$  with the appropriate hardware. The waveform, arrival time and energy information of the particle can be obtained at the same time, which can be used for PSD, amplitude spectrum and time spectrum reconstruction. This current-mode-counting method is of great significance for the measurement of the rising and

falling phases of the intense pulsed radiation field. It also provides a reference model for the particle detection process of solar flare observation, pulsar navigation signal acquisition and spaceborne nuclear explosion detection.

# ACKNOWLEDGMENTS

The authors acknowledge the China Institute of Atomic Energy (CIAE) for providing the pulsed neutron source. They appreciate Kai Zhang and Hong-Tao Chen for the operation of the neutron generator and assistance in these experiments.

# References

[1] X. L. Ning, Y. Q. Yang, M. Z. Gui et al., Acta Astronaut 142, 57-63 (2018)  
[2] L. S. Huang, L. Q. Hu, M. J. Zhou et al., Fusion Eng. Des 153, 111487 (2020)  
[3] D. S. Tusinski, S. Szpigel, C. G. Giménez de Castro et al., Sol. Phys. 294, 103 (2019)  
[4] B. M. van der Ende, L. Li, D. Godin et al., Nat. Commun. 10, 1959 (2019)  
[5] G. F. Knoll, Radiation detection and measurements, John Wiley and Sons, Inc., New York U.S.A (2010)  
[6] J. Reijonen, Nucl. Instrum. Methods Phys. Res., Sect. B 261(1-2), 272-276 (2007)  
[7] C. H. Westcott, Proc. R. Soc. Lon. Ser-A 194, 508-526 (1948)  
[8] T. F. Wang, A. Meaze, M. U. Khandaker et al., Nucl. Instrum. Methods Phys. Res., Sect. A 266(4), 561-569 (2008)  
[9] K. Watanabe, M. Yamanaka, T. Endo et al., J. Nucl. Sci. Technol. 57(2), 136-144 (2020)  
[10] G. Liu, L. Hu, G. Zhong et al., IEEE Trans. Plasma Sci 47(4), 1859-1863 (2019)  
[11] X. Y. Liu, Y. W. Yang, Rong Liu et al., Nucl. Sci. Tech 30, 139 (2019)  
[12] Y. Chen, G. Luan, J. Bao et al., Eur. Phys. J. A. 55, 115 (2019)  
[13] H. T. Jing, J. Y. Tang, H. Q. Tang et al., Nucl. Instrum. Methods Phys. Res., Sect. A 621(1-3), 91-96 (2010)  
[14] V. Y. Glebov, D. D. Meyerhofer, T. C. Sangster et al., Rev. Sci. Instrum 77(10), (2006)  
[15] R. Katano, M. Yamanaka, and C. H. Pyeon, Nucl. Sci. Tech. Eng 193(12), 1394-1402 (2019)  
[16] W. T. Heller, M. Cuneo, L. Debeer-Schmitt et al., J. Appl. Crystallogr 51(2), 242-248 (2018)  
[17] M. Girolami and A. Bellucci, P. Calvani and et al. Phys. Status Solidi A 212(11), 2424-2430 (2015)  
[18] J. Hu, J. L. Liu, Z. B. Zhang et al., Sci. Rep 8(1), 13363 (2018)

[19] M. Rebai, A. Fazzi, C. Cazzaniga et al., Diamond Relat. Mater 61, 1-6 (2016)  
[20] J. Wu, Y. Jiang, M. Li et al., Rev. Sci. Instrum 88(8), 083301 (2017)  
[21] F. Ryan and K. Lynne, Appl. Radiat. Isot, 159 (2020)  
[22] H. J. Fu, L. J. Wang, H. W. Wang et al., Nucl. Techniq 42(02), 020501 (2019)  
[23] X. P. Ouyang, Z. F. Li, G. G. Zhang et al., Acta Phys. Sin, 1502-1505 (2002)  
[24] X. P. Ouyang, Z. F. Li, Q. S. WANG et al., Chin. Phys. C 29(4), 399-403 (2005)  
[25] J. L. Ruan and X. P. Ouyang, B. Liu et al. Rev. Sci. Instrum 89(12), 123306 (2018)  
[26] W. F. Liang, Y. Lu, J. Wu et al., Nucl. Instrum. Methods Phys. Res., Sect. A 827, 161-164 (2016)  
[27] J. X. Chen, X. P. Ouyang, W. K. Zhu et al., Nucl. Electron. Detect. Technol 30(3), 357-361 (2010)  
[28] G. Tian, X. P. Ouyang, J. L. Liu et al., At. Energy Sci. Technol 49(9), 1678-1684 (2015)  
[29] P. Reynaud-Bouret, Probab. Theor. Relat. Fields 126(1), 103-153 (2003)  
[30] D. Schuhmacher, Electron. Electronic J. Probab 10(5), 165-201 (2005)  
[31] T. Nishitani, K. Ogawa, M. Isobe et al., Fusion Eng. Des, 210-214 (2018)  
[32] Z. L. He, J. Su, and F. Qin, Smart Grid 3(2), 129-132 (2015)  
[33] X. P. Zhang, J. F., Zhang, Y. Y., Cheng et al., At. Energy Sci. Technol 52(10), 1847-1854 (2018)  
[34] C. L. Wang and R. A. Riedel, Rev. Sci. Instrum 87(1), 013301 (2016)  
[35] R. H. Johnson, Nucl. Instrum. Methods 179(2), 301-307 (1981)  
[36] K. Zhao, L. Chen, H. P. Guo et al., J. Instrum 13(10), P10001 (2018)  
[37] K. Zhao, H. P. Guo, L. Chen et al., Nucl. Instrum. Methods Phys. Res., Sect. A 973, 164165 (2020)  
[38] W. Yin, S. Wang, H. Li et al., Nucl. Techniq 42(04), 040201 (2019)