# Terabit free-space data transmission employing orbital angular momentum multiplexing

Jian Wang $^{1,2\star}$ , Jeng-Yuan Yang $^{1}$ , Irfan M. Fazal $^{1}$ , Nisar Ahmed $^{1}$ , Yan Yan $^{1}$ , Hao Huang $^{1}$ , Yongxiong Ren $^{1}$ , Yang Yue $^{1}$ , Samuel Dolinar $^{3}$ , Moshe Tur $^{4}$  and Alan E. Willner $^{1\star}$

The recognition in the 1990s that light beams with a helical phase front have orbital angular momentum has benefited applications ranging from optical manipulation to quantum information processing. Recently, attention has been directed towards the opportunities for harnessing such beams in communications. Here, we demonstrate that four light beams with different values of orbital angular momentum and encoded with  $42.8 \times 4$  Gbit s $^{-1}$  quadrature amplitude modulation (16-QAM) signals can be multiplexed and demultiplexed, allowing a 1.37 Tbit s $^{-1}$  aggregated rate and 25.6 bit s $^{-1}$  Hz $^{-1}$  spectral efficiency when combined with polarization multiplexing. Moreover, we show scalability in the spatial domain using two groups of concentric rings of eight polarization-multiplexed  $20 \times 4$  Gbit s $^{-1}$  16-QAM-carrying orbital angular momentum beams, achieving a capacity of 2.56 Tbit s $^{-1}$  and spectral efficiency of 95.7 bit s $^{-1}$  Hz $^{-1}$ . We also report data exchange between orbital angular momentum beams encoded with 100 Gbit s $^{-1}$  differential quadrature phase-shift keying signals. These demonstrations suggest that orbital angular momentum could be a useful degree of freedom for increasing the capacity of free-space communications.

Angular momentum, sometimes described as the rotational analogue of linear momentum, is one of the most fundamental physical quantities in both classical and quantum mechanics<sup>1</sup>. Angular momentum can be divided into spin angular momentum (SAM) and orbital angular momentum (OAM) in paraxial beams<sup>2,3</sup>. SAM is associated with photon spin and manifested as circular polarization, as anticipated by Poynting in 1909<sup>4</sup> and demonstrated by Beth in 1936<sup>5</sup>. In contrast, OAM is linked to the spatial distribution<sup>2</sup>. It was shown by Allen in 1992<sup>6</sup> that helically phased beams comprising an azimuthal phase term  $\exp(i\ell\theta)$ , have an OAM of  $\ell\hbar$  per photon (where  $\ell$  is topological charge,  $\theta$  is azimuthal angle, and  $\hbar$  is Plank's constant  $h$  divided by  $2\pi$ ). OAM is a natural property of various types of helically phased beams, ranging from electron beams to radio waves<sup>7-15</sup>. It has given rise to many developments in optical manipulation, optical trapping, optical tweezers, optical vortex knots, imaging, astronomy and quantum information processing<sup>7,8,16-27</sup>.

In addition to these established areas, OAM has recently seen applications in free-space information transfer and communications[28]. In contrast to SAM, which has only two possible values of  $\pm \hbar$ , the theoretically unlimited values of  $\ell$ , in principle, provide an infinite range of possibly achievable OAM states. OAM therefore has the potential to tremendously increase the capacity of communication systems, either by encoding information as OAM states of the beam or by using OAM beams as information carriers for multiplexing[28-36]. In this Article, we consider the latter option of using OAM beams for multiplexing, which can be regarded as the analogue of various other multiplexing technologies in optical fibre communications, such as wavelength-division multiplexing (WDM)[37-39], optical time-division multiplexing (OTDM)[40], polarization-division multiplexing (PDM)[37-41], spatial-division multiplexing (SDM)[41] and mode-division multiplexing (MDM)[42].

Note that recent advances in optical communication systems in relation to multilevel amplitude/phase modulation formats, coherent detection and electronic digital signal processing have facilitated dramatic increases in capacity and spectral efficiency $^{37-43}$ . Hence, a valuable goal would be to use OAM beams to carry information with multilevel amplitude/phase modulation formats, resulting in yet another increase of capacity and spectral efficiency, gained by the multiplexing of OAM beams. Moreover, when using OAM beams to carry different data information, a potentially desirable operation for flexible data processing would be data exchange between OAM beams.

Here, we demonstrate multiplexing/demultiplexing of four polarization-multiplexed (pol-muxed) OAM beams, each carrying a  $42.8 \times 4$  Gbit  $\mathrm{s}^{-1}$  (4 bits per symbol) quadrature amplitude modulation (16-QAM) signal, thereby achieving a capacity of 1,369.6  $(42.8 \times 4 \times 4 \times 2)$  Gbit  $\mathrm{s}^{-1}$  (4 bits per symbol for the 16-QAM, with 4 OAM beams and 2 polarization states) with a spectral efficiency of  $25.6\mathrm{bit~s}^{-1}\mathrm{Hz}^{-1}$  (50 GHz grid). Moreover, we show scalability in the spatial domain using two groups of concentric rings of eight pol-muxed OAM beams, each carrying a  $20 \times 4$  Gbit  $\mathrm{s}^{-1}$  16-QAM signal, for which a capacity of 2,560  $(20 \times 4 \times 8 \times 2 \times 2)$  Gbit  $\mathrm{s}^{-1}$  (4 bits per symbol for the 16-QAM, with 8 OAM beams, 2 polarization states and 2 groups of concentric rings) is achieved together with a spectral efficiency of  $95.7\mathrm{bit~s}^{-1}\mathrm{Hz}^{-1}$  (25 GHz grid). Finally, we demonstrate data exchange between two OAM beams, each carrying a  $100\mathrm{Gbit~s}^{-1}$  differential quadrature phase-shift keying (DQPSK) signal.

# Multiplexing of information-carrying OAM beams

Figure 1a,b presents a schematic representation of the generation and back-conversion of an information-carrying OAM beam, where a light beam with OAM serves as a carrier of information, which

![](images/514ca2ba37a7d31f50e13d88c5a72928336b53e9e9f6e752e3a4c624b78ac3f0.jpg)  
a

![](images/59d15cba70d6fe89347be65536f80159846c831963fa70b2a7a07151fb4edb88.jpg)  
b

![](images/4fa5785720806b902ca293bd229196609ad031269e62a99e284043efd760967f.jpg)  
c  
Figure 1 | Concept and principle. a, Generation of an information-carrying OAM beam with a helical phase front. b, Recovery of an information-carrying beam with a planar phase front. c, Multiplexing/demultiplexing of information-carrying OAM beams together with polarization multiplexing/demultiplexing (middle panel). For multiplexing, OAM beams with 'doughnut'-shaped intensity profiles (left panel, third column) are spatially multiplexed. For demultiplexing, one of the OAM beams is converted into a beam with a high intensity at the centre (right panel, second column), which can be separated from other updated OAM beams with 'doughnut' shapes (right panel, third column) by spatial filtering. 16-QAM, quadrature amplitude modulation; Mux, multiplexing; Demux, demultiplexing; Pol-muxed, polarization-multiplexed.

emerges in a multilevel amplitude/phase modulation format (for example, 16-QAM). A spiral phase mask (for example,  $\ell = +4$ ; Fig. 1a) converts a planar phase front into a helical one, resulting in the generation of an information-carrying OAM beam from an information-carrying Gaussian beam. Conversely (Fig. 1b), an inverse spiral phase mask (for example,  $\ell = -4$ ) recovers an information-carrying beam with a planar phase front from an information-carrying OAM beam with a helical phase front. Owing to their inherent orthogonality, OAM beams can be used to enable a variety of optical communication applications, such as multiplexing/demultiplexing of information-carrying OAM beams to achieve an increase in capacity and spectral efficiency, and data exchange between OAM beams for flexible data processing.

A conceptual diagram of the multiplexing/demultiplexing of OAM beams is presented in Fig. 1c. In optical communications,

OAM can be considered as an additional degree of freedom, where the multiplexing of information-carrying OAM beams provides yet another dimension in the ever-continuing effort to increase the capacity and spectral efficiency of communication links. The capacity and spectral efficiency can be increased further by making use of polarization multiplexing. For example, as shown in Fig. 1c, four Gaussian beams carrying four independent channels of data information (Data1X, Data2X, Data3X, Data4X) are transformed into four OAM beams (OAM1, OAM2, OAM3, OAM4) for multiplexing by adding spiral phase masks with different charges  $(\ell = +4, +8, -8, +16)$ . Upon propagation, the intensity profiles of these OAM beams develop 'doughnut' shapes, consisting of bright rings with no intensity at the centre (third column, left panel of Fig. 1c). The multiplexing of OAM beams can be considered as a form of spatial multiplexing of beams. By

![](images/f5af591ff224aee78b8c23d8d4d7ada637f4eb4f8a24837bb38f75b37503f4e9.jpg)  
Figure 2 | Block diagram of the experimental set-up. Multiplexing/demultiplexing of information-carrying OAM beams.

introducing polarization multiplexing, four more independent channels of data information (Data1Y, Data2Y, Data3Y, Data4Y) can be carried by the same OAM beams (OAM1, OAM2, OAM3, OAM4). As a result, four pol-muxed OAM beams can allow for the multiplexing of eight independent channels of data information on the same wavelength (Fig. 1c, middle panel), which provides an eightfold improvement in capacity and spectral efficiency. It is expected that multiplexing OAM beams, in combination with polarization multiplexing, will increase the capacity and spectral efficiency by a factor of  $2N$ , where  $N$  is the number of OAM beams. To demultiplex an OAM beam  $(\ell)$  of interest, an inverse spiral phase mask with a specified charge  $(- \ell)$  is used to remove the azimuthal phase term  $\exp(i \ell \theta)$  of the OAM beam, which is therefore converted back to a beam with a planar phase front. This beam has a bright high-intensity spot at the centre (second column, right panel of Fig. 1c), which is separable from other OAM beams with updated charges and 'doughnut' shapes (third column, right panel of Fig. 1c) by means of spatial filtering.

Figure 2 presents a block diagram of the experimental set-up (see Supplementary Section I for implementation details). Four Gaussian beams  $(1,550.12\mathrm{nm})$  with planar phase fronts, each carrying a 16-QAM signal, are converted into four OAM beams (for

example,  $\mathrm{OAM}_{+4}$ ,  $\mathrm{OAM}_{+8}$ ,  $\mathrm{OAM}_{-8}$ ,  $\mathrm{OAM}_{+16}$  with helical phase fronts by adding different spiral phase masks using four reflective nematic liquid-crystal-based spatial light modulators (SLMs). The SLMs have dimensions of  $7.68 \times 7.68 \mathrm{~mm}$ ,  $512 \times 512$  pixels, a wavelength range of  $1,505 - 1,650 \mathrm{~nm}$ , and a fast response ( $< 20 \mathrm{~ms}$ ), providing phase modulation for linearly polarized light with a high efficiency of  $90 - 95\%$ . After multiplexing of the OAM beams using non-polarizing beamsplitters and polarization multiplexing with polarizing beamsplitters, a significant increase in capacity and spectral efficiency can be achieved as a result of the combined use of a multilevel amplitude/phase modulation format (16-QAM) and degrees of orbital angular momentum and polarization. The OAM beams propagate in free space over a metre-length scale. For demultiplexing, the pol-muxed OAM beams are first polarization-demultiplexed by a polarizer. Another SLM, loaded with a specific spiral phase mask, is then used to demultiplex one of the OAM beams back to a beam with a planar phase front for coherent detection.

We first demonstrate the multiplexing/demultiplexing of four OAM beams  $(\mathrm{OAM}_{-8}, \mathrm{OAM}_{+10}, \mathrm{OAM}_{+12}, \mathrm{OAM}_{-14})$  (Supplementary Section II). The polarization multiplexing stage in Fig. 2 is not used. Figure 3 shows the experimental and theoretical results. The observed intensity profiles of four OAM beams are

![](images/4504813558101f982b24c71c911c6c3adaba676df78aade2a49f2812906fa258.jpg)  
g

![](images/6a92bec08dff6663e71ee74ce3b5e18238d055fa3c1121e171dd3af117c05145.jpg)

![](images/c1fac3107a6bcaf0368335db56a27afa47752740876be78959f4c7277371b17a.jpg)  
Figure 3 | Experimental and theoretical results of multiplexing/demultiplexing of four OAM beams. a1-a5, Observed intensity profiles of OAM $_{-8}$  beam (a1), OAM $_{+10}$  beam (a2), OAM $_{+12}$  beam (a3) and OAM $_{-14}$  beam (a4), as well as their multiplexing (a5). b1-b4, Measured interferograms produced from interference between OAM beams (a1-a4) and a Gaussian beam reference. c1, Demultiplexing of OAM $_{-8}$  beam with other OAM beams off (without crosstalk). c2, Crosstalk of demultiplexing (OAM $_{-8}$  beam off, other OAM beams on). c3, Demultiplexing of OAM $_{-8}$  beam with all OAM beams on (with crosstalk). d1-d5,e1-e4,f1-f3, Simulated results corresponding to a1-a5,b1-b4,c1-c3, respectively. g, Measured spectra for demultiplexing of  $10.7 \times 4$  Gbit s $^{-1}$  16-QAM-carrying OAM beams. h, Measured BER curves for demultiplexing of  $10.7 \times 4$  Gbit s $^{-1}$  16-QAM-carrying OAM beams (OAM $_{-8}$ , OAM $_{-14}$ ). w/, with; w/o, without.

![](images/723b7d581d473e38f74eb2b2cf4d300a657f4a2674eb4e55727c267e8f08fee7.jpg)

presented in Fig. 3a1-a4, and have 'doughnut' shapes. Figure 3a5 shows the observed superposition of the four OAM beams after multiplexing. To verify the charge of the generated OAM beams, interference between each OAM beam and a Gaussian beam reference is recorded, resulting in the interferograms in Fig. 3b1-b4. In these interferograms, the number of twists indicates the magnitude of  $\ell$ , with the sign implied by the twist direction. The observed interferograms indicate that the four OAM beams for multiplexing are  $\mathrm{OAM}_{-8}$ ,  $\mathrm{OAM}_{+10}$ ,  $\mathrm{OAM}_{+12}$  and  $\mathrm{OAM}_{-14}$ . Figure 3c1-c3 shows an example of the demultiplexing of an OAM beam ( $\mathrm{OAM}_{-8}$ ). Shown in Fig. 3c1 is the observed intensity profile (with a bright high-intensity spot at the centre) of the back-converted beam from the  $\mathrm{OAM}_{-8}$  beam with other OAM beams blocked (without crosstalk). The crosstalk of the demultiplexing is shown in Fig. 3c2 as the  $\mathrm{OAM}_{-8}$  beam is blocked and other OAM beams are on. Negligible intensity is observed near the centre. When all OAM beams are on (with crosstalk), the observed intensity profile is as shown in Fig. 3c3, and includes crosstalk from the other OAM beams. Spatial filtering is expected to remove the crosstalk surrounding the centre of the back-converted beam. We also theoretically analyse the multiplexing/demultiplexing of OAM beams using an angular-spectrum propagation method, with the same parameters as those adopted in the experiment (Supplementary Sections II, SV). The simulation results are depicted in Fig. 3d1-d5, e1-e4,f1-f3, and are in good agreement with the corresponding experimental results of Fig. 3a1-a5,b1-b4,c1-c3.

For the multiplexing/demultiplexing of information-carrying OAM beams, measured spectra for back-converted beams from

different  $10.7 \times 4$  Gbit  $\mathrm{s}^{-1}$  16-QAM-carrying OAM beams are shown in Fig. 3g. These spectra overlap with one another, occupying the same bandwidth. A power suppression of  $\sim 30$  dB is achieved at an offset frequency of  $12.5\mathrm{GHz}$  from the centre. For  $10.7 \times 4$  Gbit  $\mathrm{s}^{-1}$  16-QAM signals over four OAM beams (12.5 GHz grid<sup>38</sup>, a capacity of 171.2 ( $10.7 \times 4 \times 4$ ) Gbit  $\mathrm{s}^{-1}$  is obtained, with a spectral efficiency of  $12.8$  bit  $\mathrm{s}^{-1}\mathrm{Hz}^{-1}$ , including the  $7\%$  forward error correction (FEC) overhead. The plots in Fig. 3h are bit-error rate (BER) curves for demultiplexing of the OAM beams without and with crosstalk (using OAM<sub>-8</sub> and OAM<sub>-14</sub> as examples). An optical signal-to-noise ratio (OSNR) penalty of  $< 1.2$  dB at a BER of  $2 \times 10^{-3}$  (enhanced FEC (EFEC) threshold) is measured without crosstalk. With crosstalk, a  $< 2.2$  dB OSNR penalty is observed at the same BER.

We also demonstrate the multiplexing/demultiplexing of four pol-muxed OAM beams  $(\mathrm{OAM}_{+4},\mathrm{OAM}_{+8}$ $\mathrm{OAM}_{-8}$  and  $\mathrm{OAM}_{+16})$  (Supplementary Section III). Figure 4a1-a4 presents the observed intensity profiles of four pol-muxed OAM beams with 'doughnut' shapes, and Fig. 4a5 shows the intensity profile for four superposed pol-muxed OAM beams. Interferograms are measured to indicate the charge of the OAM beams (Fig. 4b1-b4), from which it is verified that the four pol-muxed OAM beams for multiplexing are  $\mathrm{OAM}_{+4}$ $\mathrm{OAM}_{+8}$ $\mathrm{OAM}_{-8}$  and  $\mathrm{OAM}_{+16}$  respectively. Figure 4c presents the measured spectra for demultiplexing  $(\mathrm{OAM}_{+4},\mathrm{OAM}_{+16})$  from four pol-muxed OAM beams (eight channels in total), with each channel carrying a  $42.8\times 4$  Gbit s $^{-1}$  16-QAM signal. A power suppression of  $\sim 30$  dB is achieved at a frequency offset of  $50~\mathrm{GHz}$  from the centre. A spectral efficiency of  $25.6$  bit s $^{-1}$  Hz $^{-1}$  is therefore

![](images/4cf180de3469436a9c4ec566901f10b301bdc34dd881102e763ad5ef7b6c5cac.jpg)  
C

![](images/b5a025ba8c335dabfb83a952dbdff556d1c28d1504a4ae7fcbe62fcae6c28f80.jpg)  
Polarization-multiplexed OAM beams

![](images/083be75cb68f60b076d5392e72750d44ae6dc4bd176eae60c80da2a8dd878540.jpg)

![](images/8f0c71bbe5b178336955aa872327af91ce5f69b3e14904430eec726744dfa19c.jpg)

![](images/2a41f74d9a10c68336cd14c4344166545eada61f59e7ba38e9ff0721371ac48e.jpg)

![](images/c58374f8a3be669fc48df4ed9e35eea59d726324a5f9d6213079109a88ba4b69.jpg)

![](images/a085eb84b1ccb4d39de570d5892df8e14dd60ecb31a640103e43722d547fe79e.jpg)

![](images/b88ef87889945b8fdd90a7679f273d8114eec1c787e76ac37ed64e11ce81c318.jpg)

![](images/4612f2a46808d1fc5f9c09be71e593ae93625d21b9df7666330fb8232316bb8f.jpg)

![](images/edd26119eed94e1fcf225f90606fdb016b0f6c7e09d62c01efbf99a065e0a6da.jpg)

![](images/5f1b9e6efef06328fa98868b8d51af47e8849eb5c706c84ca4104209f79239e5.jpg)  
d1

![](images/48ccbc8de4dddf324554baa0237cc0af247542c66146a24c9400fc64034954d6.jpg)  
d2

![](images/a09596e3c114315875e5c2028e5cf461dea60357412a51a2601649ca530b54d7.jpg)  
Two groups of concentric rings  
g

![](images/27bb2df14a39441bdeeb46e1a170e702b1b3cc9260e98b413fc7903ee9ded7de.jpg)

![](images/044719349aec669b7654f6a6426e49c44b8f5608a0a2829aba8bd84ddeff9169.jpg)

![](images/43bcc349b70458a101b7658888e0195f25091f05bb809fd413cabcddb75f07b6.jpg)

![](images/fe543abceea38fd62f801a0d66bc41d6bc6d1a9a42d6c312007d605b69bce683.jpg)

![](images/d0c3fae6f11c268e664825f174385551cdc31181b657bd28fc3ae4aad32e105d.jpg)  
Figure 4 | Experimental results of 16-QAM signals over pol-muxed OAM beams. a1-a5, Observed intensity profiles of pol-muxed OAM $_{+4}$  beam (a1), OAM $_{+8}$  beam (a2), OAM $_{-8}$  beam (a3), OAM $_{+16}$  beam (a4) and their multiplexing (a5). b1-b4, Measured interferograms corresponding to OAM $_{+4}$ , OAM $_{+8}$ , OAM $_{-8}$  and OAM $_{+16}$  beams. c,d1,d2 Measured spectra (c) and BER curves (d1,d2) for demultiplexing of pol-muxed  $42.8 \times 4$  Gbit s $^{-1}$  16-QAM-carrying OAM beams. e, Schematic diagram of spatially multiplexed pol-muxed OAM beams with groups of concentric rings. f1-f3, Observed intensity profiles for two multiplexed groups of concentric rings of eight pol-muxed OAM beams (OAM $_{\pm 10}$ , OAM $_{\pm 12}$ , OAM $_{\pm 14}$ , OAM $_{\pm 16}$ ) (32 channels) (f1), demultiplexed inner rings (f2) and outer rings (f3). g, Measured spectra for demultiplexing of x-polarized  $20 \times 4$  Gbit s $^{-1}$  16-QAM-carrying OAM $_{-12}$  beam in the outer rings. h, OSNR penalties for all 32 channels. x-pol., x-polarization; y-pol., y-polarization. w/, with; w/o, without.

![](images/53581a723bce7adc7063209dc2846c05941bd2c144587d4861fbbcc59a253fd6.jpg)

obtained for a total capacity of 1,369.6  $(42.8\times 4\times 4\times 2)$  Gbit  $\mathrm{s}^{-1}$ , that is,  $42.8\times 4$  Gbit  $\mathrm{s}^{-1}$  16-QAM signals over four pol-muxed OAM beams (50 GHz grid $^{37}$ ), including the  $7\%$  FEC overhead. Figure 4d1,d2 plots the measured BER curves for the demultiplexing of pol-muxed OAM beams along the  $x-$  and  $y$ -polarizations without ( $x-$  or  $y$ -polarization of only one pol-muxed OAM beam is on) and with (all four pol-muxed OAM beams are on) crosstalk. OSNR penalties of  $<1.5$  dB without crosstalk and  $<3.0$  dB with crosstalk are observed at a BER of  $2\times 10^{-3}$ .

The scalability of multiplexing/demultiplexing OAM beams in the spatial domain (Supplementary Section IV) is also demonstrated. Two groups of OAM beams with the same charges but different beam sizes—that is, one group (outer rings) is expanded compared to the other (inner rings)—can be spatially multiplexed

together as concentric rings (Fig. 4e). Figure 4f1 presents the observed intensity profile for the two multiplexed groups of concentric rings of eight pol-muxed OAM beams  $(\mathrm{OAM}_{\pm 10},$ $\mathrm{OAM}_{\pm 12}$ $\mathrm{OAM}_{\pm 14}$ $\mathrm{OAM}_{\pm 16})$  . Spatial filtering is used to enable the demultiplexing of the two groups of concentric rings. The intensity profiles of the demultiplexed inner and outer rings are shown in Fig. 4f2,f3, respectively. Figure 4g shows typical spectra for demultiplexing  $(\mathrm{OAM}_{-12}$  beam,  $x$  -polarization, in outer rings) two groups of concentric rings of eight pol-muxed OAM beams (that is, 32 channels in total), with each channel carrying a  $20\times 4$  Gbit s-1 16-QAM signal. A power suppression of  $\sim 30$  dB is obtained at a  $25\mathrm{GHz}$  frequency offset from the centre. A spectral efficiency of  $95.7\mathrm{bit}s^{-1}\mathrm{Hz}^{-1}$  is therefore achieved for a capacity of 2,560  $(20\times 4\times 8\times 2\times 2)$  Gbit s-1, that is,  $20\times 4$  Gbit s-1 16-QAM

![](images/ca3413de3fa06335e7ad9002adca9ad5c06b59507e4942034d7a13529f7b73eb.jpg)  
a  
Signal A

![](images/9c4fdf525cbafaf6b6de0c8c892e3e6d8391879670a32a8cb131f58e1e1d7ca2.jpg)  
Signal B

![](images/36ce98e667554d16e316aa9a1d9f56c0b2f155e7b725e90f4a5a2ed8dfbb2d5a.jpg)  
Figure 5 | Data exchange between OAM beams. a, Conceptual diagram showing that two information-carrying OAM beams are exchanged (OAM $_{\ell_1} \leftrightarrow$  OAM $_{\ell_2}$ ) after reflecting off a spiral phase mask with a charge of  $\ell_R = -(\ell_1 + \ell_2)$ . b1-b3,c1,c2,d1-d3,e1,e2, Observed intensity profiles (b1-b3,d1-d3) and interferograms (c1,c2,e1,e2) showing that OAM $_{+8}$  (b1,c1) and OAM $_{+6}$  (b2,c2) beams become OAM $_{+6}$  (d1,e1) and OAM $_{+8}$  (d2,e2) beams after exchange. b3,d3, Superposition of two OAM beams before (b3) and after (d3) exchange. f1,f2,g1,g2, Measured interferograms showing that OAM $_{+10}$  (f1) and OAM $_{+6}$  (f2) beams become OAM $_{+6}$  (g1) and OAM $_{+10}$  (g2) beams after exchange.

![](images/21a978609c5ad12ffa70cb38c4a518b754da61ea1ffe3dcc5772ed716a294ede.jpg)  
$\mathrm{OAM}_{+8}\longleftrightarrow \mathrm{OAM}_{+6}$

![](images/0574a41e654e87c01babaf58be83a35a5d58540c3f8ee03812daab232b2dc9c0.jpg)

![](images/fce59d23e3f3df1c1396112e2db09854d0dcef07446fbd7e403debd76aaf8ac8.jpg)

![](images/a11c2b877d5a1535887f0e250025b051e40765b99cd52bfe0242bdf8d57c6cb3.jpg)

![](images/18695ae8279b3d520d3333689bfc41631916dc93f9add598bc0ce433c7d1865d.jpg)

![](images/9bfa1bb7c063d0bec0247677186215d001f19182dce81cf19189a89a5513ba0e.jpg)

![](images/491a64c61aeb1b7e6c0883b21ae1847ac482dfb80def02bb2f682b5fb1bf4001.jpg)

![](images/9bcdee2315205579e4668eb3bb9872b806b8b45040c3d2cd5b0dd126b63bf46c.jpg)

![](images/191a522b792e7614c878565e6966e7134e6e2455f5c7effffde56e0c9b971bc5.jpg)

![](images/affe5ce2527eb30c0e8b2525e7dd0e5aa063609e585223a9be84a04b419bc01b.jpg)  
$\mathrm{OAM}_{+10}\longleftrightarrow \mathrm{OAM}_{+6}$

![](images/91a67921cf529cbcef09d5694540f445259ef4469b10c60334264d1a96136801.jpg)

![](images/3774cc87dd0b3766ae2f60b8adbf4358d9e3a4611062fe27cdc29dbb0f0acc58.jpg)

![](images/cbda51f72e9bc1f42efa297b8bc431d60202e5f5856b42a56c09767d17df0b6b.jpg)

signals over eight pol-muxed OAM beams in two groups of concentric rings (25 GHz grid $^{39}$ ), with a  $7\%$  FEC overhead. All 32 channels can achieve a BER of  $< 2 \times 10^{-3}$ . The measured OSNR penalties at a BER of  $2 \times 10^{-3}$  due to the crosstalk of (de)multiplexing are depicted in Fig. 4h, with the average OSNR penalties for the inner and outer rings being 2.7 and 3.6 dB, respectively.

# Data exchange between OAM beams

Figure 5a illustrates conceptually the data exchange between OAM beams. Two superposed OAM beams  $(\mathrm{OAM}_{\ell_1}, \mathrm{OAM}_{\ell_2})$ , each carrying different data information (signal A, signal B), shine on a reflective-type SLM loaded with a spiral phase mask with a charge of  $\ell_{\mathrm{R}} = -(\ell_{1} + \ell_{2})$ . After reflecting off the SLM, this phase mask adds an azimuthal phase term  $\exp (i\ell_{\mathrm{R}}\theta)$  to the two OAM beams and converts them into  $\mathrm{OAM}_{-\ell_2}$  and  $\mathrm{OAM}_{-\ell_1}$ , which are further transformed into  $\mathrm{OAM}_{\ell_2}$  and  $\mathrm{OAM}_{\ell_1}$  due to reflection of the SLM, which flips the charge sign[44]. As a result, data exchange between two OAM beams is implemented. For another input of two OAM beams with varied charges, reconfigurable data exchange is available by updating the phase mask loaded into the reflective-type SLM. Figure 5a presents an example of data exchange between DQPSK-carrying OAM beams  $(\mathrm{OAM}_{+8}, \mathrm{OAM}_{+6})$ .

The observed intensity profiles of the two OAM beams before exchange and their superposition are presented in Fig. 5b1-b3. The interferograms in Fig. 5c1,c2 indicate that the charges of the

two OAM beams before exchange are  $+8$  and  $+6$ . Figure 5d1-d3 shows the intensity profiles of the OAM beams and their superposition after exchange. The interferograms in Fig. 5e1,e2 verify that the charges of two OAM beams after exchange become  $+6$  and  $+8$  (Supplementary Section I). Figure 5f1,f2,g1,g2 presents measured results for the reconfigurable data exchange between another two OAM beams  $(\mathrm{OAM}_{+10}$  and  $\mathrm{OAM}_{+6})$  by updating the spiral phase mask loaded into the SLM.

Figures 6a1,a2 plots measured BER curves for data exchange between two  $100\mathrm{Gbit}s^{-1}$  return-to-zero DQPSK (RZ-DQPSK) carrying OAM beams  $(\mathrm{OAM}_{+8}$  and  $\mathrm{OAM}_{+6})$  with a power penalty of  $<  2.1$  dB at a BER of  $1\times 10^{-9}$  .Measured BER curves for a reconfigurable data exchange between another two OAM beams  $(\mathrm{OAM}_{+10}$  and  $\mathrm{OAM}_{+6})$  are shown in Fig. 6b1,b2, with a power penalty of  $<  1.9$  dB at a BER of  $1\times 10^{-9}$  .We measure the temporal waveforms and balanced eyes of the demodulated inphase (Ch. I) and quadrature (Ch. Q) components of  $100\mathrm{Gbit}s^{-1}$  RZ-DQPSK signals. As shown in Fig. 6c, the observed temporal waveforms confirm the successful implementation of data exchange between the two OAM beams  $(\mathrm{OAM}_{+10}$  and  $\mathrm{OAM}_{+6})$

# Discussion

These proof-of-concept experiments demonstrate the multiplexing/demultiplexing of information-carrying OAM beams for terabit free-space data transmission, as well as data exchange

![](images/1f08b54eeeaf90ab58134724431c9727b1d3c44afc03db35d7488e78625a7118.jpg)

![](images/1a7c1cfc32e07b77d4fabbea1f6c2b20488b07704442f58e5ff35174b4f9cbfe.jpg)

![](images/0f0dec1a29d86e2fbfda3ea8164bf56df90e67f2e7b798ebe79352ec9b8fc172.jpg)

![](images/10e0f0766e7c4483bf1302d0d37c2c71fba54c7a3ed0db0446656dc05aef0f0a.jpg)

![](images/7ce5f1f00749a9bd07701f322137544e12b3b5f4b2075336e4bc09fc0e73beb7.jpg)

![](images/c87b688caedac1e6a544b02f3686bea3f40eb881b9f464bd404ab135bb0f8cf7.jpg)

![](images/2bdcd19ace9e89aaf8d3b5cf822a993c347f37fa3cbf183a9e42595ee8216cb1.jpg)  
Figure 6 | Data exchange between 100 Gbit s $^{-1}$  RZ-DQPSK-carrying OAM beams. a1,a2, Measured BER curves for data exchange between OAM $_{+8}$  and OAM $_{+6}$  beams (a1,a2) as well as between OAM $_{+10}$  and OAM $_{+6}$  beams (b1,b2). c, Observed waveforms and balanced eyes of demodulated in-phase (Ch. I) and quadrature (Ch. Q) components of 100 Gbit s $^{-1}$  RZ-DQPSK signals for data exchange between OAM $_{+10}$  and OAM $_{+6}$  beams. Ref. ex., before exchange; Aft. ex., after exchange.

![](images/8ce5eabd8dc42c894c04b05413d0dc1ca5192322fd8e1f3565ac2b550f9cbcfc.jpg)

between OAM beams for flexible data processing. Although a short free-space link over a metre-length scale is shown here, further improvements might lead to the use of OAM as an additional degree of freedom with a view to achieving high-capacity and high-spectral-efficiency optical communication systems. Additionally, the techniques demonstrated here are generally orthogonal to other multiplexing techniques; for example,

each wavelength in WDM signals can contain multiple OAM beams<sup>34</sup>.

For free-space propagation, a key challenge is the sensitivity of the spatial structure of light to atmospheric conditions such as turbulence $^{45,46}$ . There may be solutions that overcome these problems using adaptive optics (for example, the phase correction method) $^{47}$ . For short distances ( $\sim \mathrm{km}$ ) the harmful effects of

atmospheric turbulence can be tolerated or compensated. Accordingly, information-carrying OAM multiplexing might be used in practical free-space propagation systems to achieve high transmission capacity in combination with other degrees of freedom, such as polarization and wavelength multiplexing. In addition, information-carrying OAM multiplexing could potentially be used in future deep-space and near-Earth optical communications, where some alternative approaches, using low-density parity-check (LDPC) codes, together with multiple-input multiple-output (MIMO) and equalization techniques, might be considered to deal with the atmospheric turbulence<sup>30</sup>.

In addition to free-space propagation, another area of potential interest would be to transmit OAM beams in fibre. Although regular fibres might not guide OAM beams stably because of intermodal couplings, some recent reports have shown potential solutions using a specially designed fibre with high-index annular rings[48,49]. For example, the transmission of OAM states of light through  $0.9\mathrm{km}$  of specially designed fibre has been reported[49]. In the future, fibre-based transmission of multiplexed information-carrying OAM beams might provide an opportunity to increase the capacity of optical fibre transmission systems.

# Methods

Generation of information-carrying OAM beams. An OAM beam  $U(r,\theta)$  can be formed by attaching a spiral phase mask (exp(i  $\ell \theta$ ) to a Gaussian beam,

$$
U (r, \theta) = A (r) \cdot \exp (i \ell \theta) \tag {1}
$$

where  $A(r)\propto \exp (-r^2 /\omega_0^2)$  is the complex electric field amplitude at the waist of the Gaussian beam,  $r$  is the radial distance from the centre axis of the Gaussian beam,  $\omega_0$  is the waist size,  $\ell$  is the topological charge of the OAM, and  $\theta$  is the azimuthal angle. Such an OAM beam has a helical phase structure, with its wavefronts resembling an  $\ell$ -fold corkscrew (Fig. 1a). When encoded with data information, the information-carrying OAM beam  $(U_{\mathrm{S}}(r,\theta ,t))$  can be described as

$$
U _ {\mathrm {S}} (r, \theta , t) = S (t) \cdot A (r) \cdot \exp (i \ell \theta) \tag {2}
$$

where  $S(t)$  is the applied data information. Clearly, an inverse spiral phase mask,  $\exp [i(-\ell)\theta ]$ , can remove the azimuthal phase dependence of an OAM beam, as shown in Fig. 1b.

Multiplexing/demultiplexing of information-carrying OAM beams. For the multiplexing of  $N$  information-carrying OAM beams  $(U_{Sp}(r,\theta ,t) = S_p(t)\cdot A_p(r)\cdot$ $\exp (i\ell_p\theta),p = 1,2,3,\ldots ,N)$  , the resultant field is given by

$$
U _ {\mathrm {M U X}} (r, \theta , t) = \sum_ {p = 1} ^ {N} S _ {p} (t) \cdot A _ {p} (r) \cdot \exp (i \ell_ {p} \theta) \tag {3}
$$

where  $A_{p}(r)$  can be identical or distinct for different  $p$ . Although  $N$  OAM beams are superposed on one another, each OAM beam carrying its own data information is, in principle, distinguishable from the others due to its unique orbital angular momentum. Furthermore, the propagation through free space and spherical lenses does not modify the orbital angular momentum of the individual OAM beam $^{50}$ . Hence, the field of the received (Rx) superposed OAM beams can be written as

$$
U _ {\mathrm {M U X}} ^ {\mathrm {R x}} (r, \theta , t) = \sum_ {p = 1} ^ {N} S _ {p} (t) \cdot A _ {p} ^ {\mathrm {R x}} (r) \cdot \exp (i \ell_ {p} \theta) \tag {4}
$$

For the demultiplexing of information-carrying OAM beams, an inverse spiral phase mask  $\exp [i(-\ell_q)\theta ]$  is used to transform the superposed OAM beams as follows:

$$
\begin{array}{l} U _ {\text {D E M U X}} (r, \theta , t) = \exp [ i (- \ell_ {q}) \theta ] \cdot \sum_ {p = 1} ^ {N} S _ {p} (t) \cdot A _ {p} ^ {\mathrm {R x}} (r) \cdot \exp (i \ell_ {p} \theta) \tag {5} \\ = S _ {q} (t) \cdot A _ {q} ^ {\mathrm {R x}} (r) + \sum_ {p = 1, p \neq q} ^ {N} S _ {p} (t) \cdot A _ {p} ^ {\mathrm {R x}} (r) \cdot \exp \left(i \ell_ {p} ^ {\prime} \theta\right) \\ \end{array}
$$

where  $\ell_p' = \ell_p - \ell_q$ . It is easily seen that only one of the superposed information-carrying OAM beams (charge,  $\ell_q$ ) is converted back to a beam with the azimuthal phase term removed. The others are still OAM beams, but with updated charge values from  $\ell_p$  to  $\ell_p'$ . After free-space propagation and transmission through a

spherical lens, the back-converted beam forms a bright high-intensity spot, separable from the other OAM beams, which have 'doughnut' shapes with no intensity at the centre.

Data exchange between OAM beams. For data exchange between two OAM beams, a specified spiral phase mask,  $\exp [i[-(\ell_1 + \ell_2)]\theta ]$  , converts two informationcarrying OAM beams

$$
U _ {\mathrm {S} 1} (r, \theta , t) = S _ {1} (t) \cdot A _ {1} (r) \cdot \exp (i \ell_ {1} \theta) \tag {6a}
$$

$$
U _ {\mathrm {S} 2} (r, \theta , t) = S _ {2} (t) \cdot A _ {2} (r) \cdot \exp (i \ell_ {2} \theta) \tag {6b}
$$

into

$$
\begin{array}{l} U _ {S 1} ^ {\mathrm {T m p}} (r, \theta , t) = \exp [ i [ - (\ell_ {1} + \ell_ {2}) ] \theta ] \cdot S _ {1} (t) \cdot A _ {1} (r) \cdot \exp (i \ell_ {1} \theta) \tag {7a} \\ = S _ {1} (t) \cdot A _ {1} (r) \cdot \exp [ i (- \ell_ {2}) \theta ] \\ \end{array}
$$

$$
\begin{array}{l} U _ {S 2} ^ {\mathrm {T m p}} (r, \theta , t) = \exp [ i [ - (\ell_ {1} + \ell_ {2}) ] \theta ] \cdot S _ {2} (t) \cdot A _ {2} (r) \cdot \exp (i \ell_ {2} \theta) \tag {7b} \\ = S _ {2} (t) \cdot A _ {2} (r) \cdot \exp [ i (- \ell_ {1}) \theta ] \\ \end{array}
$$

Under reflection from a reflective-type SLM, equations (7a) and (7b) are further transformed into<sup>44</sup>

$$
U _ {S 1} ^ {\operatorname {E x}} (r, \theta , t) \propto S _ {1} (t) \cdot A _ {1} (r) \cdot \exp (i \ell_ {2} \theta) \tag {8a}
$$

$$
U _ {S 2} ^ {\operatorname {E x}} (r, \theta , t) \propto S _ {2} (t) \cdot A _ {2} (r) \cdot \exp (i \ell_ {1} \theta) \tag {8b}
$$

By comparing equations (6a) and (6b) with equations (8a) and (8b), we confirm the implementation of data exchange between two OAM beams.

# Received 26 January 2012; accepted 14 May 2012; published online 24 June 2012

# References

1. Mandel, L. & Wolf, E. Optical Coherence and Quantum Optics (Cambridge Univ. Press, 1995).  
2. Jackson, J. D. Classical Electrodynamics (Wiley, 1962).  
3. Cohen-Tannoudji, C., Dupont-Roc, J. & Grynberg, G. Photons and Atoms: Introduction to Quantum Electrodynamics (Wiley, 1989).  
4. Poynting, J. H. The wave motion of a revolving shaft, and a suggestion as to the angular momentum in a beam of circularly polarised light. Proc. R. Soc. Lond. A 82, 560-567 (1909).  
5. Beth, R. Mechanical detection and measurement of the angular momentum of light. Phys. Rev. 50, 115-125 (1936).  
6. Allen, L., Beijersbergen, M. W., Spreeuw, R. J. C. & Woerdman, J. P. Orbital angular momentum of light and the transformation of Laguerre-Gaussian laser modes. Phys. Rev. A 45, 8185-8189 (1992).  
7. Franke-Arnold, S., Allen, L. & Padgett, M. Advances in optical angular momentum. *Laser Photon. Rev.* 2, 299-313 (2008).  
8. Yao, A. M. & Padgett, M. J. Orbital angular momentum: origins, behavior and applications. Adv. Opt. Photon. 3, 161-204 (2011).  
9. Uchida, M. & Tonomura, A. Generation of electron beams carrying orbital angular momentum. Nature 464, 737-739 (2010).  
10. McMorran, B. J. et al. Electron vortex beams with high quanta of orbital angular momentum. Science 331, 192-195 (2011).  
11. Sasaki, S. & McNulty, I. Proposal for generating brilliant X-ray beams carrying orbital angular momentum. Phys. Rev. Lett. 100, 124801 (2008).  
12. Marrucci, L., Manzo, C. & Paparo, D. Optical spin-to-orbital angular momentum conversion in inhomogeneous anisotropic media. Phys. Rev. Lett. 96, 163905 (2006).  
13. Turnbull, G. A., Roberson, D. A., Smith, G. M., Allen, L. & Padgett, M. J. The generation of free-space Laguerre-Gaussian modes at millimetre-wave frequencies by use of a spiral phaseplate. Opt. Commun. 127, 183-188 (1996).  
14. Thide, B. et al. Utilization of photon orbital angular momentum in the low-frequency radio domain. Phys. Rev. Lett. 99, 087701 (2007).  
15. Tamburini, F. et al. Encoding many channels on the same frequency through radio vorticity: first experimental test. New J. Phys. 14, 033001 (2012).  
16. Dholakia, K. & Cizmár, T. Shaping the future of manipulation. Nature Photon. 5, 335-342 (2011).  
17. Paterson, L. et al. Controlled rotation of optically trapped microscopic particles. Science 292, 912-914 (2001).  
18. MacDonald, M. P. et al. Creation and manipulation of three-dimensional optically trapped structures. Science 296, 1101-1103 (2002).

19. Padgett, M. & Bowman, R. Tweezers with a twist. Nature Photon. 5, 343-348 (2011).  
20. Dennis, M. R., King, R. P., Jack, B., O'Holleran, K. & Padgett, M. J. Isolated optical vortex knots. Nature Phys. 6, 118-121 (2010).  
21. Bernet, S., Jesacher, A., Furhapter, S., Maurer, C. & Ritsch-Marte, M. Quantitative imaging of complex samples by spiral phase contrast microscopy. Opt. Express 14, 3792-3805 (2006).  
22. Elias, N. M. II Photon orbital angular momentum in astronomy. *Astron. Astrophys.* 492, 883-922 (2008).  
23. Mair, A., Vaziri, A., Weihs, G. & Zeilinger, A. Entanglement of the orbital angular momentum states of photons. Nature 412, 313-316 (2001).  
24. Molina-Terriza, G., Torres, J. P. & Torner, L. Twisted photons. Nature Phys. 3, 305-310 (2007).  
25. Barreiro, J. T., Wei, T.-C. & Kwiat, P. G. Beating the channel capacity limit for linear photonic superdense coding. Nature Phys. 4, 282-286 (2008).  
26. Nagali, E. et al. Optimal quantum cloning of orbital angular momentum photon qubits through Hong-Ou-Mandel coalescence. Nature Photon. 3, 720-723 (2009).  
27. Leach, J. et al. Quantum correlations in optical angle-orbital angular momentum variables. Science 329, 662-665 (2010).  
28. Gibson, G. et al. Free-space information transfer using light beams carrying orbital angular momentum. Opt. Express 12, 5448-5456 (2004).  
29. Shapiro, J. H., Guha, S. & Erkmen, B. I. Ultimate channel capacity of free-space optical communications. J. Opt. Netw 4, 501-516 (2005).  
30. Djordjevic, I. B. Deep-space and near-Earth optical communications by coded orbital angular momentum (OAM) modulation. Opt. Express 19, 14277-14289 (2011).  
31. Awaji, Y., Wada, N. & Toda, Y. Demonstration of spatial mode division multiplexing using Laguerre-Gaussian mode beam in telecom-wavelength in Proceedings of the IEEE Photonics Conference paper WBB2, PHO 2010, Denver (IEEE Photonics Society, 2010).  
32. Wang, J. et al. Demonstration of 12.8-bit/s/Hz spectral efficiency using 16-QAM signals over multiple orbital-angular-momentum modes, in Proceedings of the European Conference on Optical Communications paper We.10.P1.76, ECOC 2011, Geneva (Optical Society of America, 2011).  
33. Wang, J. et al. 25.6-bit/s/Hz spectral efficiency using 16-QAM signals over pol-mixed multiple orbital-angular-momentum modes, in Proceedings of the IEEE Photonics Conference paper WW2, PHO 2011, Denver (IEEE Photonics Society, 2011).  
34. Fazal, I. M. et al. Demonstration of 2-Tbit/s data link using orthogonal orbital-angular-momentum modes and WDM, in Proceedings of the Frontiers in Optics paper FTuT1, FiO/LS 2011, San Jose (Optical Society of America, 2011).  
35. Wang, J. et al. Experimental demonstration of 100-Gbit/s DQPSK data exchange between orbital-angular-momentum modes, in Proceedings of the Optical Fiber Communication Conference paper OW11.5, OFC/NFOEC 2012, Los Angeles (Optical Society of America, 2012).  
36. Doerr, C. R. et al. Silicon photonic integrated circuit for coupling to a ring-core multimode fiber for space-division multiplexing, in Proceedings of the European Conference on Optical Communications paper Th.13.A.3, ECOC 2011, Geneva (Optical Society of America, 2011).  
37. Gnauck, A. H. et al. Spectrally efficient long-haul WDM transmission using 224-Gb/s polarization-multiplexed 16-QAM. J. Lightwave Technol. 29, 373-377 (2011).

38. Zhou, X. et al. 64-Tb/s, 8 b/s/Hz, PDM-36QAM transmission over  $320\mathrm{km}$  using both pre- and post-transmission digital signal processing. J. Lightwave Technol. 29, 571-577 (2011).  
39. Sano, A. et al. Ultra-high capacity WDM transmission using spectrally-efficient PDM 16-QAM modulation and C- and extended L-band wideband optical amplification. J. Lightwave Technol. 29, 578-586 (2011).  
40. Richter, T. et al. Transmission of single-channel 16-QAM data signals at terabaud symbol rates. J. Lightwave Technol. 30, 504-511 (2012).  
41. Liu, X. et al. 1.12-Tb/s 32-QAM-OFDM superchannel with  $8.6\mathrm{-b / s / Hz}$  intrachannel spectral efficiency and space-division multiplexed transmission with  $60\mathrm{-b / s / Hz}$  aggregate spectral efficiency. Opt. Express 19, B958-B964 (2011).  
42. Ryf, R. et al. Mode-division multiplexing over  $96\mathrm{km}$  of few-mode fiber using coherent  $6\times 6$  MIMO processing. J. Lightwave Technol. 30, 521-531 (2012).  
43. Hillerkuss, D. et al. 26 Tbit  $s^{-1}$  line-rate super-channel transmission utilizing all-optical fast Fourier transform processing. Nature Photon. 5, 364-371 (2011).  
44. Walborn, S. P., de Oliveira, A. N., Pádua, S. & Monken, C. H. Multimode Hong-Ou-Mandel Interference. Phys. Rev. Lett. 90, 143601 (2003).  
45. Paterson, C. Atmospheric turbulence and orbital angular momentum of single photons for optical communication. Phys. Rev. Lett. 94, 153901 (2005).  
46. Anguita, J. A., Neifeld, M. A. & Vasic, B. V. Turbulence-induced channel crosstalk in an orbital angular momentum-multiplexed free-space optical link. Appl. Opt. 47, 2414-2429 (2008).  
47. Zhao, S. M., Leach, J., Gong, L. Y., Ding, J. & Zheng, B. Y. Aberration corrections for free-space optical communications in atmosphere turbulence using orbital angular momentum states. Opt. Express 20, 452-461 (2012).  
48. Ramachandran, S., Kristensen, P. & Yan, M. F. Generation and propagation of radially polarized beams in optical fibers. Opt. Lett. 34, 2525-2527 (2009).  
49. Bozinovic, N., Kristensen, P. & Ramachandran, S. Long-range fiber-transmission of photons with orbital angular momentum, in Proceedings of the Conference on Lasers and Electro-Optics paper CTuB1, CLEO 2011 (Optical Society of America, 2011).  
50. Kogelnik, H. & Li, T. Laser beams and resonators. Appl. Opt. 5, 1550-1567 (1966).

# Acknowledgements

The authors thank A. Bozovich, B. Shamee, L. Zhang, K. Birnbaum, J. Choi, B. Erkmen, M. Neifeld and R. Willis for very fruitful discussions. This work was supported by the Defense Advanced Research Projects Agency (DARPA) under the InPho (Information in a Photon) programme.

# Author contributions

J.W., J.Y.Y., I.M.F., H.H., Y.Y., S.D., M.T. and A.E.W. developed the concept and conceived the experiments. J.W. performed the theoretical and numerical analyses. J.W., J.Y.Y., I.M.F., N.A., Y.Y., H.H., Y.R. and Y.Y. carried out the measurements and analysed the data. S.D., M.T. and A.E.W. provided technical support. All authors contributed to writing and finalizing the Article.

# Additional information

The authors declare no competing financial interests. Supplementary information accompanies this paper at www.nature.com/naturephotonics. Reprints and permission information is available online at http://www.nature.com/reprints. Correspondence and requests for materials should be addressed to J.W. and A.E.W.

# ERRATUM

# Speckle-free laser imaging using random laser illumination

Brandon Redding, Michael A. Choma & Hui Cao

Nature Photon. 6, 355-359 (2012); published online 29 April 2012; corrected after print 14 June 2012.

The received date of this Letter was incorrect. This error has been corrected in the HTML and PDF versions of the Letter.