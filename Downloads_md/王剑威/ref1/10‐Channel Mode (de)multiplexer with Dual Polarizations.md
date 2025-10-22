# 10-Channel Mode (de)multiplexer with Dual Polarizations

Daoxin Dai,\* Chenlei Li, Shipeng Wang, Hao Wu, Yaocheng Shi, Zhihang Wu, Shiming Gao, Tingge Dai, Hui Yu, and Hon-Ki Tsang

A dual-polarization 10-channel mode (de)multiplexer is proposed and realized with cascaded dual-core adiabatic tapers on a silicon-on-insulator (SOI) platform. The mode demultiplexer has a  $2.3\mu \mathrm{m}$ -wide multimode bus waveguide, which supports six mode-channels of TE polarization and four mode-channels of TM polarization. These ten mode-channels are (de)multiplexed with five cascaded dual-core adiabatic tapers based on SOI nanowires. The widths for these dual-cores are chosen optimally according to the dispersion curves of the dual-core SOI nanowire, so that the desired highest-order modes of TE- and TM-polarizations are extracted simultaneously. These two extracted mode-channels are coupled very efficiently to the fundamental modes of TE- and TM-polarizations ( $T E_{0}$  and  $T M_{0}$ ) in the narrow waveguide, respectively, which are then separated by using a polarization beam splitter based on bent directional couplers. A chip consisting of a pair of 10-channel mode (de)multiplexers is fabricated and then tested with data transmission of 30Gbps/channel. The measurement results show that all TM- and TE mode-channels have low crosstalks ( $-15\sim -25$  dB) and low excess losses ( $0.2\sim 1.8$  dB) over a broad wavelength band of  $\sim 90$  nm, which makes it WDM (wavelength-division-multiplexing)-compatible and thus suitable for high capacity on-chip optical interconnects.

# 1. Introduction

Advanced multiplexing technologies have been playing very important roles to satisfy the increasing demands of high capacity of optical interconnects.[1-8] Wavelength-division-multiplexing (WDM) is one of the most successful technologies, and uses different wavelength-channels to carry different signals in a single optical fiber/waveguide simultaneously.[1] In order to

Prof. D. Dai, C. Li, S. Wang, H. Wu, Prof. Y. Shi, Z. Wu, Prof. S. Gao

Centre for Optical and Electromagnetic Research

State Key Laboratory for Modern Optical Instrumentation

Zhejiang Provincial Key Laboratory for Sensing Technologies

Zhejiang University

Zijingang Campus

Hangzhou 310058, China

E-mail: dxdai@zju.edu.cn

T. Dai, Prof. H. Yu

College of Information Science and Electronic Engineering

Zhejiang University

Hangzhou 310027, China

Prof. H.-K. Tsang

Department of Electronic Engineering

the Chinese University of Hong Kong

Shatin, N. T., Hong Kong, S. A. R., China

DOI: 10.1002/lpor.201700109

further increase the link capacity of optical interconnects, one approach is to further enhance the capacity for each wavelength carrier.[3] Further multiplexing technologies have been developed, e.g., space-division-multiplexing (SDM) with multiple cores,[4] mode-division-multiplexing (MDM) with multiple guided-modes,[9] and polarization-division multiplexing (PDM) with dual polarizations.[10,11] These additional multiplexing approaches help not only to save the physical space but can also reduce the cost of the system. Furthermore, these multiplexing approaches have independent degrees of freedom and can be used simultaneously to form a hybrid multiplexing technology, so that the capacity of an optical communication system increases even to Peta-bit/s.[6-8]

Optical multiplexers and demultiplexers are one of the most important elements in any multiplexed optical interconnects/networks. Silicon photonics has attracted much attention as a very promising platform for the realization of

The ADC-based mode (de)multiplexers have been proposed to be used in on-chip (de)multiplexers, because of its advantages resulting from the leveraging of CMOS (complementary metal-oxide-semiconductor) processes for large volume and high yield manufacture.[12-15] Various silicon-based on-chip (de)multiplexers have been demonstrated in the past years,[6] including arrayed-waveguide gratings for WDM,[17] and on-chip polarization-handling devices for PDM,[18] as well as mode (de)multiplexers for MDM.[19-21] In particular, mode (de)multiplexer for MDM have been proposed by utilizing multimode interferometers,[22] asymmetric Y-junctions,[23,24] topology structures,[25] adiabatic couplers,[26,27] and asymmetric directional couplers (ADCs),[28-30] etc. Among them, ADC-based mode (de)multiplexers are popular[30] because of the structural simplicity, the scalability, and the flexibility to excite a desired high-order mode from a launched fundamental mode. Previously we have proposed and demonstrated a compact ADC-based 4-channel silicon mode multiplexer operating for TM polarization with low loss and low crosstalk.[30] Later a grating-assisted ADC was also designed to realize 4-channel narrow-band mode multiplexer.[31] The ADC-based mode (de)multiplexers have also been used to realize hybrid (de)multiplexers by integrating with other WDM devices. For example, a three-channel multiplexer combining ADCs and microrings for simultaneous MDM and WDM has been realized to expand the link capacity.[32,33] A 64-channel

hybrid (de)multiplexer was also developed to enable MDM and WDM simultaneously by integrating a four-channel broadband ADC mode (de)multiplexer and 16-channel arrayed-waveguide gratings (AWGs).[34,35]

One might notice that most of the mode (de)multiplexers demonstrated previously work for a single polarization only (i.e., TE- or TM-polarization modes).[22-30] Further increase in data transmission capacity can be realized if dual polarizations are introduced. For WDM systems, a wavelength-division-multiplexer with dual-polarizations has been demonstrated.[36,37] Similarly, for MDM, more mode-channels are available in a multimode bus waveguide with a given core width when dual polarizations are introduced. Furthermore, a broadband mode (de)multiplexer with dual polarizations is desired to be WDM-compatible, so that it is possible to combine WDM, MDM as well as PDM together to form multi-dimensional hybrid (de)multiplexing technologies, which is needed for the ultra-high capacity optical interconnects in the future.[6] Previously, we realized a 8-channel mode (de)multiplexer with dual polarizations for a  $2.36\mu \mathrm{m}$  wide multimode bus waveguide by introducing six cascaded different ADCs and a polarization beam splitter (PBS).[38] There are four channels of TE-polarization modes and four channels of TM-polarization modes involved. These six ADCs were designed to deal with the higher-order modes  $\mathrm{(TE_1,TE_2,TE_3,TM_1}$ ,  $\mathrm{TM}_2$  and  $\mathrm{TM}_3)$  while the PBS was used to combine/separate the  $\mathrm{TE_0}$  and  $\mathrm{TM}_0$  modes. For this 8-channel (de)multiplexer, it is shown that there is some crosstalk due to the undesired coupling from the orthogonal polarization modes. Fortunately, polarization crosstalk can be filtered out effectively by a polarizer.[39] Nevertheless, it is still a challenge to realize a high-performance mode (de)multiplexer with more than 10 channels.

In order to enable more mode-channels and improve the performances as well, in this paper we propose and demonstrate a novel structure for realizing a broadband multi-channel mode (de)multiplexer with dual polarizations, which enables MDM and PDM simultaneously. The proposed approach for mode (de)multiplexer is to utilize cascaded dual-core adiabatic tapers as well as PBSs. With the dual-core adiabatic taper, it is possible to simultaneously extract a TE mode-channel and a TM mode-channel from the multimode bus waveguide. This approach simplifies the layout and offers improved performances in comparison with the structure reported previously in.[40] In this paper, we present a dual-polarization 10-channel mode (de)multiplexer which operates with six TE mode-channels and four TM mode-channels and is formed by the monolithic integration of five cascaded dual-core adiabatic tapers and six integrated PBSs.

# 2. Structure, Fabrication and Characterization

Figure 1(a) shows the proposed mode (de)multiplexer, which is realized by utilizing cascaded dual-core adiabatic tapers and integrated PBSs. With such a novel architecture, a broadband dual-polarization multi-channel mode (de)multiplexer is realized to enable MDM and PDM simultaneously. For each dual-core adiabatic taper, as shown in Figure 1(b), the lengths  $(L_{i01}, L_{i12}$  and  $L_{i23})$  and the widths  $(w_{ia0}, w_{ia1}, w_{ia2}$  and  $w_{ia3}; w_{ib0}, w_{ib1}, w_{ib2}$  and  $w_{ib3})$  for the dual cores are chosen optimally, so that one can extract the desired TE mode-channel and TM mode-channel from the

multimode bus waveguide simultaneously. These two extracted mode-channels are then separated by using an integrated PBS. The PBSs are realized with the design based on bent DCs, which work near-perfectly in an ultra-wide wavelength-band as demonstrated recently.[40]

As an example, we consider the design for a hybrid MDM-PDM (de)multiplexer with 10 channels, including six mode-channels of TE-polarization and four mode-channels of TM-polarization, which are supported in a  $2.3\mu \mathrm{m}$  wide and  $220~\mathrm{nm}$  thick multimode bus waveguide. As shown in Figure 1(a), the 10-channel mode (de)multiplexer is designed with six PBSs and five cascaded dual-core adiabatic tapers. For the integrated PBS, the cascaded bent DCs have widths  $(w_{1},w_{2})$  and bending radii  $(R_{1},R_{2})$  which are chosen according to the phase-matching condition for TM polarization.[40,41] Here all the PBSs have the same design parameters as given in.[40] As demonstrated in,[40] such a PBS works very well with a extinction ratio of  $>30$  dB and an excess loss of  $<  0.5$  dB in a bandwidth as large as  $70~\mathrm{nm}$  while the footprint is as compact as  $\sim 6.9\times 20\mu \mathrm{m}^2$

For the  $i$ -th adiabatic taper based on a dual-core waveguide, there are three sections, as shown in Figure 1(b). The first section, consisting of a straight wide multimode waveguide and a S-bending narrow waveguide gradually brings the dual cores closer. Their widths are kept constant (i.e.,  $w_{ia0} = w_{ia1}$ , and  $w_{ib0} = w_{ib1}$ ) while the gap between them is reduced from  $w_{ig0}$  to  $w_{ig1}$  gradually. The length  $L_{i01}$  of the narrow waveguide is chosen to be large enough so that the dual-core waveguide system is adiabatic. Similarly to the first section, the third section consists of a straight wide multimode waveguide and a S-bending narrow waveguide which gradually separates the dual cores, with the gap increasing from  $w_{ig2}$  to  $w_{ig3}$  gradually while their widths are kept constant (i.e.,  $w_{ia2} = w_{ia3}$ , and  $w_{ib2} = w_{ib3}$ ). The length  $L_{i23}$  of the narrow waveguide is chosen to be large enough so that the dual-core waveguide system is adiabatic. The second section is the key part, which consists of a wide core and a narrow core. For this section, the wide core is tapered down from  $w_{ia1}$  to  $w_{ia2}$  and the narrow core is tapered up from  $w_{ib1}$  to  $w_{ib2}$ , while the gap between them is kept constant (i.e.,  $w_{ig1} = w_{ig2}$ ). The design rules for determining the parameters of the adiabatic taper are described below.

(1) Core widths  $(w_{ia0}, w_{ia1}, w_{ia2}$  and  $w_{ia3}; w_{ib0}, w_{ib1}, w_{ib2}$  and  $w_{ib3})$ : Here we set  $w_{ia0} = w_{ia1}$ ,  $w_{ia2} = w_{ia3}$ ,  $w_{ib0} = w_{ib1}$ , and  $w_{ib2} = w_{ib3}$ . We assume that  $w_{ib1} < w_{ib2}$ , and  $w_{ia1} < w_{ia2}$ .  
(i) At the input end of the second section, the narrow-core width  $w_{\mathrm{ib1}}$  should be minimized so that all the guided super-modes of the dual-core are localized in the wide-core, which is possible when  $w_{\mathrm{ib1}} \ll w_{\mathrm{ia1}}$  according to the coupled mode theory. For example, we choose a minimal narrow-core width as  $w_{\mathrm{ib1}} = 120$  nm according to the requirement of the fabrication process. For the tapered wide-core, the end width  $w_{\mathrm{ia1}}$  is chosen to be large enough to support the  $p$ -th guided super-mode, which is desired to be dropped. Meanwhile, the width  $w_{\mathrm{ia1}}$  should be chosen so that the  $(p + 1)$ -th guided super-mode is cut-off almost, which helps reduce the inter-mode crosstalk.  
(ii) At the output end of the second section, the core widths  $(w_{ia2}, w_{ib2})$  should be chosen optimally, so that the highest-order supermodes of TE- and TM-polarizations are localized in the narrow core while the other lower

![](images/31a64523c7fc3081100089659fa7a502d12d62169b4c3ffe01a140a7ea7f2302.jpg)

![](images/01c0d1c35a8291e1e1fe92f281b634b4c54b52babe33a07486fcaeb2b22ba63d.jpg)  
Figure 1. a) Schematic configuration of the present 10-channel mode (de)multiplexer with dual polarizations based on cascaded dual-core adiabatic tapers; b) An adiabatic taper based on a dual-core waveguide; c) A PBS based on a structure with cascaded bent DCs.

![](images/06aad2bc136a0178d3388040cbf1f39418b3441c0ff46d9f3f698983354114d0.jpg)

![](images/d2df20107ad747f963af29947fd1f8bc82e1656e3274d9d8b7ed163cfea866a5.jpg)  
(a)

![](images/b09ad80ac3c6e3dae7e8a0e5310c2a3047d330927eff93cee3e3f2c26dbb5230.jpg)  
Figure 2. a) Cross section of an single-core SOI nanowire with  $h_{\mathrm{co}} = 220 \, \mathrm{nm}$ ; b) Calculated effective indices of eigen-modes of  $220 \, \mathrm{nm}$ -thick SOI nanowires. Here the circled-curves and the thick solid curves are for TE and TM polarizations, respectively.  
(b)  
1 wco (um) 1

super-modes are confined dominantly in the wide core. For stage #i, one should choose the core-widths  $w_{ia2}$  and  $w_{ib2}$  as follows. When it is desired to drop the  $p$ -th TE mode-channel, the core-widths  $w_{ia2}$  and  $w_{ib2}$  should be chosen so that  $n_{\mathrm{eff\_TE}}(w_{ia2}, p) < n_{\mathrm{eff\_TE}}(w_{ib2}, 0) < n_{\mathrm{eff\_TE}}(w_{ia2}, p-1)$ , where  $n_{\mathrm{eff\_TE}}(w, p)$  is the effective index of the  $p$ -th TE polarization mode in a single-core SOI nanowire when its core-width is  $w$ . If the  $q$ -th TM mode is dropped together, the core-widths  $w_{ia2}$  and  $w_{ib2}$  should be chosen optimally to make  $n_{\mathrm{eff\_TM}}(w_{ia2}, q) < n_{\mathrm{eff\_TM}}(w_{ib2}, 0) < n_{\mathrm{eff\_TM}}(w_{ia2}, q-1)$  satisfied simultaneously, where  $n_{\mathrm{eff\_TM}}(w, q)$  is the effective index of the  $q$ -th TM polarization mode in a single-core SOI nanowire when its core-width is  $w$ . In this way, the highest-order supermodes of TE- and TM-polarizations are localized in the narrow core, and thus can be dropped easily.

(2) Gap widths  $(w_{ig0}, w_{ig1}, w_{ig2}$  and  $w_{ig3})$ : Here we set  $w_{ig1} = w_{ig2}$ , which should be small to achieve a short taper length. However, the minimal gap width is usually limited by the fabrication technology. For example, we choose  $w_{ig1} = w_{ig2} =$

120 nm in the paper. The gap width  $w_{\mathrm{ig0}}$  should be large enough so that no mode is excited in the narrow core at the input end of the first section, which can be determined by the super-mode confinement factor in the narrow core for the dual-core waveguide. The gap width  $w_{\mathrm{ig3}}$  should be large enough so that there is no coupling between the narrow core and the wide core at the output end of the third section. This can be determined by the confinement factor in the narrow core for the dropped super-mode of the dual-core waveguide.

(3) Taper lengths  $(L_{i01}, L_{i12}$  and  $L_{i23})$ : All the three sections should be long enough to be adiabatic, which can be determined by numerically simulating the light propagation in the sections.

The core widths  $(w_{ia1}, w_{ia2}, w_{ib1}$ , and  $w_{ib2}$ ) should be chosen appropriately according to the dispersion curves of the guided-modes supported in a single-core SOI waveguide as well as a dual-core waveguide. For a 220 nm-thick single-core SOI nanowire (see Figure 2(a)), we calculate the effective indices  $n_{\mathrm{eff\_TE}}(w, p)$  and  $n_{\mathrm{eff\_TM}}(w, q)$  of eigen-modes as the core width  $w$  varies by using a mode-solver, as shown in Figure 2(b). Here the

Table 1. The parameters of the designed dual-core adiabatic tapers (Unit:  $\mu \mathrm{m}$  ).  

<table><tr><td rowspan="2">Stage #</td><td rowspan="2">Dropped modes</td><td colspan="4">The wide-core widths</td><td colspan="4">The narrow-core widths</td><td colspan="4">The gap widths</td><td colspan="3">The taper lengths</td></tr><tr><td>wia0</td><td>wia1</td><td>wia2</td><td>wia3</td><td>wib0</td><td>wib1</td><td>wib2</td><td>wib3</td><td>wig0</td><td>wig1</td><td>wig2</td><td>wig3</td><td>Lio1</td><td>Lio2</td><td>Lio3</td></tr><tr><td>1</td><td>TE1</td><td>0.72</td><td>0.72</td><td>0.48</td><td>0.48</td><td>0.12</td><td>0.12</td><td>0.26</td><td>0.26</td><td>0.5</td><td>0.12</td><td>0.12</td><td>1.2</td><td>5</td><td>15</td><td>19</td></tr><tr><td>2</td><td>TE2, TM1</td><td>1.15</td><td>1.15</td><td>0.78</td><td>0.78</td><td>0.12</td><td>0.12</td><td>0.3</td><td>0.3</td><td>0.5</td><td>0.12</td><td>0.12</td><td>1.2</td><td>11</td><td>27</td><td>38</td></tr><tr><td>3</td><td>TE3, TM2</td><td>1.4</td><td>1.4</td><td>1.15</td><td>1.15</td><td>0.12</td><td>0.12</td><td>0.3</td><td>0.3</td><td>0.9</td><td>0.12</td><td>0.12</td><td>1.2</td><td>16</td><td>40</td><td>21</td></tr><tr><td>4</td><td>TE4</td><td>1.95</td><td>1.95</td><td>1.7</td><td>1.7</td><td>0.12</td><td>0.12</td><td>0.32</td><td>0.32</td><td>0.9</td><td>0.12</td><td>0.12</td><td>1.2</td><td>24</td><td>71</td><td>50</td></tr><tr><td>5</td><td>TE5, TM3</td><td>2.3</td><td>2.3</td><td>1.8</td><td>1.8</td><td>0.12</td><td>0.12</td><td>0.28</td><td>0.28</td><td>0.9</td><td>0.12</td><td>0.12</td><td>1.2</td><td>24</td><td>50</td><td>60</td></tr></table>

![](images/fb26092e6505cf2dc94e06ade147da26cce8f21ad516647a5fbedbe6125633a1.jpg)

![](images/72c3e07ce8893b292c8fb631389b3a9325a7c02e4aea66ac46173b489be5cdcb.jpg)

![](images/42a49e5f396f33769d21b0691d1f03033d8236040d1e086ede5d4e09e9b5a0d0.jpg)

![](images/84fe305749a250b2a9968aac22a776e61b597b4b8be47e99380b603a59f892f3.jpg)

![](images/5234172fc9761f47b73f5e4861dfba6f3d9f196aebceb94957eb501cdacd68f5.jpg)

![](images/9e26b68f52909763adedac9415114e2a0b15585707b9b6c0637fb2c71e172e1e.jpg)  
Figure 3. Simulated light propagation in the designed dual-core adiabatic taper for stage #5 when any one of the mode-channel is launched from the input side of the wide bus waveguide. a) the  $\mathrm{TE}_0$  mode; b) the  $\mathrm{TE}_1$  mode; c) the  $\mathrm{TE}_2$  mode; d) the  $\mathrm{TE}_3$  mode; e) the  $\mathrm{TE}_4$  mode; f) the  $\mathrm{TE}_5$  mode; g) the  $\mathrm{TM}_0$  mode; h) the  $\mathrm{TM}_1$  mode; i) the  $\mathrm{TM}_2$  mode; j) the  $\mathrm{TM}_3$  mode. The taper lengths are  $L_{i01} = 24\mu m$ ,  $L_{i12} = 50\mu m$ , and  $L_{i23} = 60\mu m$ .

![](images/47e0df3c16022b7371e71a5e8ac807f3decdf35cdcf15339598eaba0298cc293.jpg)

![](images/983520922a8d25a0cce105a9bf3e41f568bf46f5176743cfe715b234773e9a45.jpg)

![](images/c4e793d8bd57a48ace92eddb36a95336cae5be05f9a0118615aba1c8c2930ccf.jpg)

![](images/a960125d03bcd1b79bf8617b956798fc7c4d0bfb8adba3447e795c6f0cba9b1a.jpg)

circled-curves and the thick solid curves are for TE and TM polarizations, respectively. From this figure, it can be seen that the core width should be  $w_{\mathrm{co}} > 2 \mu \mathrm{m}$  in order to support more than ten guided-modes, including six TE-polarization modes (i.e., the  $\mathrm{TE}_0$ ,  $\mathrm{TE}_1$ ,  $\mathrm{TE}_2$ ,  $\mathrm{TE}_3$ ,  $\mathrm{TE}_4$ , and  $\mathrm{TE}_5$  modes) and four TM-polarization modes (i.e., the  $\mathrm{TM}_0$ ,  $\mathrm{TM}_1$ ,  $\mathrm{TM}_2$ , and  $\mathrm{TM}_3$  modes). According to the dispersion curves shown in Figure 2(b), the dual-polarization 10-channel mode (de)multiplexer is designed with six stages, which comprise four stages which handle dual polarizations and two stages which have TE-polarization only, as shown in Table 1. Here the  $\mathrm{TE}_5$  and  $\mathrm{TM}_3$  mode-channels are dropped by stage #5, the  $\mathrm{TE}_4$  mode-channel are dropped by stage #4, the  $\mathrm{TE}_3$  and  $\mathrm{TM}_2$  mode-channels are dropped by stage #3, the  $\mathrm{TE}_2$  and  $\mathrm{TM}_1$  mode-channels are dropped by stage #2, the  $\mathrm{TE}_1$  mode-channel is dropped by stage #1, and the  $\mathrm{TE}_0$  and  $\mathrm{TM}_0$  mode-channels are dropped by stage #0. For stages #5, #3, and #2, a PBS is cascaded to separate the two mode-channels with dual polarizations dropped together. At stage #0, the  $\mathrm{TE}_0$  and  $\mathrm{TM}_0$  mode-channels are separated by a PBS. For stages #4 and #1, even though there is only one mode-channel of TE-polarization dropped, a PBS is still cascaded to remove any possible polarization crosstalk.

As an example, for stage #5 (i.e.,  $i = 5$ ), we choose  $w_{\mathrm{ia0}} = w_{\mathrm{ia1}} = 2.3 \mu \mathrm{m}$  so that six TE-polarizations mode and four TM-polarization modes are confined well in the core region. The  $\mathrm{TE}_5$  mode is the highest-order TE mode while the  $\mathrm{TM}_3$  mode is the highest-order TM mode. According to the design rules given above, the widths  $w_{\mathrm{ia2}}$  and  $w_{\mathrm{ia3}}$  are chosen as  $w_{\mathrm{ia2}} = w_{\mathrm{ia3}} = 1.8 \mu \mathrm{m}$ , so that the  $\mathrm{TE}_5$  and  $\mathrm{TM}_3$  modes are cut-off at the narrow end of the wide-core waveguide (see Figure 2(b)). Meanwhile, the width  $w_{\mathrm{ib2}}$  should be large enough to support the  $\mathrm{TE}_0$  and  $\mathrm{TM}_0$  modes

at the wide end of the narrow-core waveguide, and also satisfy the following two conditions:  $n_{\mathrm{eff,TE}}(w_{\mathrm{ia2}},5) < n_{\mathrm{eff,TE}}(w_{\mathrm{ib2}},0) < n_{\mathrm{eff,TE}}(w_{\mathrm{ia2}},4)$ , and  $n_{\mathrm{eff,TM}}(w_{\mathrm{ia2}},4) < n_{\mathrm{eff,TM}}(w_{\mathrm{ib2}},0) < n_{\mathrm{eff,TM}}(w_{\mathrm{ia2}},3)$ , as discussed in the design rule. For example, here we choose  $w_{\mathrm{ib3}} = w_{\mathrm{ib2}} = 0.28 \mu \mathrm{m}$ . According to the design rule, the gap widths  $w_{\mathrm{ig0}}$ , and  $w_{\mathrm{ig3}}$  should be chosen large enough. Here we choose  $w_{\mathrm{ig0}} = 0.5 \mu \mathrm{m}$ , and  $w_{\mathrm{ig3}} = 1.2 \mu \mathrm{m}$  from the calculation of the confinement factor in the narrow core for the target super-mode at the input end and the confinement factor in the wide core for the dropped super-mode of the dual-core waveguide at the output end. Finally, the lengths  $(L_{i01}, L_{i12}$  and  $L_{i23})$  for the tapers should be chosen to be adiabatic as required. The taper lengths are determined easily from the simulated transmission of the supermodes to be dropped in the tapers as the taper length increases. In the design for stage #5, we choose  $L_{i01} = 24 \mu \mathrm{m}$ ,  $L_{i12} = 50 \mu \mathrm{m}$ , and  $L_{i23} = 60 \mu \mathrm{m}$ , so that the transmission of the target super-mode is higher than  $99\%$ . Figure 3(a)-(j) shows the simulated light propagation in the designed dual-core adiabatic taper for stage #5 when any one of the mode-channels is launched from the input side of the wide bus waveguide. From these figures, it can be seen clearly that the  $\mathrm{TE}_5$  mode and the  $\mathrm{TM}_3$  mode are respectively converted to the  $\mathrm{TE}_0$  mode and the  $\mathrm{TM}_0$  mode at the narrow core with high efficiencies (see Figure 3(f), and Figure 3(j)). Meanwhile, all the other mode-channels (i.e.,  $\mathrm{TE}_4 \sim \mathrm{TE}_0$  and  $\mathrm{TM}_2 \sim \mathrm{TM}_0$ ) are still confined in the wide bus waveguide and will be demultiplexed by the following stages.

In a similar way, all the core widths, the gap widths, and the taper lengths for stages #1~#4 are determined, as shown in Table 1. Figure 4 shows the simulated light propagation in these designed dual-core adiabatic tapers for stages #4, #3, #2,

![](images/a3c7f23a8c7d6d02b3d7e4bbc1fa13f61c7f4e957f7e1ef175193da93b470bd1.jpg)  
Figure 4. Simulated light propagation in the designed dual-core adiabatic tapers for stage #4, #3, #2, and #1 when any one of the mode-channel is launched for the input side of the wide bus waveguide.

![](images/786d2922ccd9d7ee2b01ba5fe5315cc6274dff074424d6db7eb7c47644bff0c4.jpg)  
Figure 5. Calculated wavelength dependence of the designed dual-core adiabatic taper for stage #5 when the  $\mathrm{TE}_5$  mode a) and the  $\mathrm{TM}_3$  mode is launched, respectively. Inset: the field distribution of the launched mode and the light propagation in the taper at the central wavelength  $1.55\mu m$ .

![](images/8707d31ec8b1d9b35ee58ceee1517942d5b24a7b1bc284d036d9fdfa45116e05.jpg)

and #1 when any one of the mode-channel is launched from the input side of the wide bus waveguide. As shown in this figure, the  $\mathrm{TE}_4$  mode is dropped by stage #4, the  $\mathrm{TE}_3$  and  $\mathrm{TM}_2$  modes are dropped simultaneously by stage #3, the  $\mathrm{TE}_2$  and  $\mathrm{TM}_1$  modes are dropped simultaneously by stage #2, and the  $\mathrm{TE}_1$  mode is dropped by stage #1. Finally the  $\mathrm{TE}_0$  and  $\mathrm{TM}_0$  modes are left in the wide-core waveguide. As illustrated in Figure 2, each narrow-core waveguide is connected to a PBS, which separates the orthogonal polarizations. The PBS ensures low polarization crosstalk. For the PBSs, in this paper we use the design with cascaded bent DCs demonstrated in our previous paper.[40] With this PBS, the measurement results show that the excess loss is very low ( $< 0.5\mathrm{dB}$ ) and the extinction ratio is higher than  $30\mathrm{dB}$  in a broad wavelength-band of over  $70\mathrm{nm}$  for both polarizations.

Figure 5(a)-(b) show the calculated wavelength dependence of the designed dual-core adiabatic taper for stage #5 when the  $\mathrm{TE}_5$  mode and the  $\mathrm{TM}_3$  mode are launched, respectively. It can be seen that the excess losses for the target modes to be dropped are very low over the broad wavelength range from  $1.48\mu \mathrm{m}$  to  $1.62\mu \mathrm{m}$ . The undesired power coupled to any other super-modes

is very low, which indicates the inter-mode crosstalk is very low. It can be seen that the crosstalk becomes higher slightly when operating at shorter wavelength. The reason is that the mode conversion efficiency in the dual-core adiabatic taper decreases slightly due to the stronger optical confinement. Nevertheless, in the present design, the inter-mode crosstalk is less than  $-20\mathrm{dB}$  theoretically in the wavelength range from  $1.49\mu \mathrm{m}$  to  $1.62\mu \mathrm{m}$ , which allows compatibility with WDM technology. It is possible to develop a multi-dimensional hybrid (de)multiplexing technology enabling WDM, MDM as well as PDM simultaneously by integrating the present 10-channel mode (de)multiplexer with AWGs or microring resonators (MRRs). For example, more than 1000 channels in total can be obtained when 100 wavelength-channels with a channel-spacing of  $\Delta \lambda_{\mathrm{ch}} = 0.8\mathrm{nm}$  are introduced, as allowed by the bandwidth of the present 10-channel mode (de)multiplexer. This will be very attractive for enhancing the link capacity of on chip optical interconnects.

The designed multi-channel mode multiplexer was fabricated on a SOI wafer with a  $220\mathrm{nm}$ -thick top silicon layer and a  $2\mu \mathrm{m}$ -thick buried dioxide layer. The fabrication processes include: (1)

![](images/fcdd2d297fa6b4317d47bece7eceb33b8a1d120a1931381693d03b6df4e6f90f.jpg)  
Figure 6. a) The optical image of the fabricated silicon PIC including a hybrid multiplexer, the multimode bus waveguide and a hybrid demultiplexer; b) Microscope image of the mode (de)multiplexer; c) Microscope image for a dual-core adiabatic taper; d) SEM pictures for PBS.

E-beam lithography for defining the resist-pattern of the waveguides and grating couplers; (2) An ICP (inductively coupled plasma) etching process for etching the top-silicon layer down to the buried oxide layer; (3) A PECVD (plasma-enhanced chemical vapor deposition) deposition process for making a  $2\mu \mathrm{m}$ -thick  $\mathrm{SiO}_2$  upper-cladding. As shown in Figure 6(a), the fabricated photonic integrated circuit (PIC) includes a 10-channel mode multiplexer (with input ports  $\mathrm{I}_1\sim \mathrm{I}_{10}$ ), a  $2.3\mu \mathrm{m}$ -wide and  $100\mu \mathrm{m}$ -long multimode bus waveguide, and a 10-channel mode demultiplexer (with output ports  $\mathrm{O}_1\sim \mathrm{O}_{10}$ ). Figure 6(b)-(d) shows the microscope image and the scanning electron microscope (SEM) pictures of the fabricated mode (de)multiplexer, a dual-core adiabatic taper, and the PBS, respectively.

In order to characterize the present 10-channel mode (de)multiplexer with dual polarizations, the TE-type and TM-type waveguide grating couplers were used for convenient coupling between the fiber and the chip. A tunable laser from  $1520\mathrm{nm}$  to  $1610\mathrm{nm}$  was used as the light source and a polarization-controller was used to generate TE- or TM-polarized light. For the characterization of the PIC consisting of a  $10\times 1$  mode multiplexer, a wide multimode bus waveguide, and a  $1\times 10$  mode demultiplexer, the transmissions at all the output ports  $(\mathrm{O}_1\sim \mathrm{O}_{10})$  were measured when light was launched from any one of the input port  $\mathrm{I}_i$ $(i = 1,2,\dots,10)$  to excite the  $\mathrm{TE}_0,\mathrm{TE}_1,\mathrm{TE}_2,\mathrm{TE}_3,\mathrm{TE}_4,$ $\mathrm{TE}_5,\mathrm{TM}_0,\mathrm{TM}_1,\mathrm{TM}_2,$  and  $\mathrm{TM}_3$  modes, respectively. The measured transmissions at output ports  $\mathrm{O}_1\sim \mathrm{O}_{10}$  are shown in Figure 7(a)-(j), respectively. These results are normalized by the transmission of a straight singlemode waveguide on the same chip. It can be seen that the fabricated 10-channel mode (de)multiplexers have a low excess loss and a low crosstalk within the wavelength-band covering  $1525\sim 1610\mathrm{nm}$ .

From the measurement results shown in Figure 7(a)-(j), the excess losses (@  $1555\mathrm{nm}$ ) for a pair of 10-channel (de)multiplexers are about 0.68 dB, 0.14 dB, 0.43 dB, 0.85 dB, 1.80 dB, 0.27 dB, 0.83 dB, 0.73 dB, 0.3 dB and 0.1d B for the  $\mathrm{TE}_0$ ,  $\mathrm{TE}_1$ ,  $\mathrm{TE}_2$ ,  $\mathrm{TE}_3$ ,  $\mathrm{TE}_4$ ,  $\mathrm{TE}_5$ ,  $\mathrm{TM}_0$ ,  $\mathrm{TM}_1$ ,  $\mathrm{TM}_2$ , and  $\mathrm{TM}_3$  mode-channels, respectively. The excess loss is mainly caused by the scattering loss and incomplete mode conversion in the dual-core adiabatic tapers due to the fabrication imperfections. The maximal crosstalks from the other mode-channels to the

$\mathrm{TE}_0, \mathrm{TE}_1, \mathrm{TE}_2, \mathrm{TE}_3, \mathrm{TE}_4, \mathrm{TE}_5, \mathrm{TM}_0, \mathrm{TM}_1, \mathrm{TM}_2,$  and  $\mathrm{TM}_3$  mode-channels are respectively about  $-18.2\mathrm{dB}$ ,  $-23.8\mathrm{dB}$ ,  $-18.6\mathrm{dB}$ ,  $-32.3\mathrm{dB}$ ,  $-19.1\mathrm{dB}$ ,  $-20.1\mathrm{dB}$ ,  $-28.1\mathrm{dB}$ ,  $-27.0\mathrm{dB}$ ,  $-25.8\mathrm{dB}$  and  $-22.0\mathrm{dB}$  around  $1555\mathrm{nm}$ , as shown in Figure 7(a)-(j). From these figure, one might notice that there are high crosstalks around  $1520\mathrm{nm}$ , which is mainly due to the limitation of the detection sensitivity of the optical spectrum analyzer and the bandwidth of the grating couplers. Nevertheless, the measurement results show that all TM- and TE mode-channels have low crosstalks  $(-15\sim -25\mathrm{dB})$  and low excess loss  $(0.2\sim 1.8\mathrm{dB})$  over a broad wavelength band of  $\sim 90\mathrm{nm}$  (covering the C-band  $1530\sim 1565\mathrm{nm}$ ). Regarding that the present dual-polarization hybrid (de)multiplexer works well over a broad wavelength-band, it is possible to be used together with WDM filters to realize a kind of multi-dimensional hybrid multiplexing technology to further improve the link capacity.

Finally, we check the data transmissions in the fabricated 10-channel (de)multiplexers by using the setup shown in Figure 8. Here there were only two wavelengths used in the experiment, i.e.,  $(\lambda_{1},\lambda_{2}) = (1546.92,1554.13)$  nm, due to the limitation of the laser sources available in the lab. The two wavelengths are chosen to be aligned to the central wavelengths of the AWG's channels. The AWG used here has a channel spacing of  $0.8\mathrm{nm}$  and the  $0.5\mathrm{dB}$  -bandwidth is about  $0.25\mathrm{nm}$ . As shown in Figure 8, these two wavelength-channels are multiplexed into a single-mode fiber by a  $3\mathrm{dB}$ -coupler and then modulated with a bit rate of 30 Gbps by a high-speed electro-optic modulator. The data rate was limited by the pattern generator available. A time-delay was introduced to delay one of the two wavelength-channels by inserting a  $1.5\mathrm{m}$ -long optical fiber, in order to generate non-identical data for these two wavelength-channels  $(\lambda_{1},\lambda_{2})$ . Finally, these two channels of data are combined again by a  $3\mathrm{dB}$ -coupler and go through an erbium-doped fiber amplifier (EDFA) and a polarization controller. Finally, the data are coupled into the PIC with 10-channel (de)multiplexers from the  $i$ -th input port  $\mathbf{I}_i$  through a grating coupler. Here we did not make the characterization for the chip when operating with the 10 mode-channels simultaneously because there is no 10-channel fiber array available in the lab for efficient fiber-chip coupling. Therefore, the chip was characterized with one of the mode-channels. As an example, here

![](images/c195ec7f746b1024c863f682f7703a03e91e9f9e5784422488f3fa6e33f7116f.jpg)

![](images/2924c8dbbf849ed4360cafa987393a8fcf041c728304054f0fcf90e997b8eb65.jpg)

![](images/ae36218200aecbd651398f5c153c0a9e72464c0799cf99865639eb8465217a34.jpg)

![](images/7a492c4279780e6cd6c61f3fd5b95363942236e35e1930fad2445ad8e1806088.jpg)

![](images/229cab54615f26dc8c81ce4433460e62f262e8b6683e812d4234d474ae7a8dad.jpg)

![](images/581e3233dbaf80596db08715f94184c1c0079b1edc45d997a8709ba7a0c8b4a7.jpg)

![](images/a6b2b0066a8f3fbb9e7266df9582b522f8d5167321719bbf98e190794b790c25.jpg)

![](images/36c15fcdc8a311367b820a2188a806341f14a5c34ae5fb6e8ace4ea589e2b466.jpg)

![](images/c8e42c71e4609e00942472eac6d456d7273bfe2a02f33d043923fa09331e5194.jpg)

![](images/3437488466ad06ffda73c31e1e9b8f9ff9326d270c38b9075ac2333d960d6b38.jpg)  
Figure 7. Measured transmissions at the then output ports of the mode demultiplexer when light is launched from port a)  $I_1$ , b)  $I_2$ , c)  $I_3$ , d)  $I_4$ , e)  $I_5$ , f)  $I_6$ , g)  $I_7$ , h)  $I_8$ , i)  $I_9$ , j)  $I_{10}$  of the mode multiplexer, respectively.

we choose to inject the data carried by the two wavelengths  $(\lambda_{1}$  and  $\lambda_{2})$  from ports  $\mathrm{I}_1,\mathrm{I}_3,\mathrm{I}_6$  ,and  $\mathrm{I_8}$  , corresponding to the  $\mathrm{TM}_0$ $\mathrm{TM}_1$ $\mathrm{TM}_2$  , and  $\mathrm{TM}_3$  mode-channels, respectively. As a result, a clear eye-diagram was observed at output port  $\mathrm{O_1}$ $\mathrm{O_3}$ $\mathrm{O_6}$  ,and  $\mathrm{O_8}$  for the data carried by the two wavelength-channels, respectively, as shown in Figure 9. For these measured TM-mode channels, the extinction ratio of the eye-diagrams is  $4.5\sim 5.5$  dB, which is similar to th at of the measured eye-diagram for the data transmission through a straight waveguide on the same chip. For the six TE-mode channels of the current chip, unfortunately there is some trouble when measuring the eye-diagrams due to the low coupling efficiency of the TE-type grating couplers. As described above, the present chip was fabricated with a single deep-etching process in order to simplify the fabrication. However, the deeplyetched TE-type grating coupler has much higher coupling loss than the deeply-etched TM-type grating coupler. As a result, an additional EDFA is needed to achieve sufficiently high optical power for the receiver, which however introduces to much noise

to get clear eye-diagrams. As it is well known, one can achieve a efficient coupling for TE polarization by using a shallowly-etched grating coupler. In this way, one can definitely get eye-diagrams similar to those presented for TM-polarization. As demonstrated in Figure 9, the present 10-channel (de)multiplexer works well in a broad band, more than 100 wavelength-channels are allowed to work compatibly when choosing a channel-spacing of  $\Delta \lambda_{\mathrm{ch}} = 0.8 \mathrm{~nm}$ . Therefore, it is possible to develop a multi-dimensional hybrid (de)multiplexing technology with more than 1000 channels by combining WDM, MDM as well as PDM simultaneously.

# 3. Conclusion

In conclusion, we have proposed and demonstrated a novel compact mode (de)multiplexer which can handle dual polarizations and 10 channels. A novel architecture combining cascaded dual-core adiabatic tapers and integrated PBSs has been introduced.

![](images/89f1b2e991d0e1fde07387385a23699f254ff98f3233ecf2675b5e1ff82d306a.jpg)  
Figure 8. Experiment setup including tunable lasers, polarization controllers (PC), 3 dB couplers, AWGs, an electro-optic modulator (Mod.), a pattern generator (PG), EDFAs, a digital communications analyzer (DCA), an optical receiver (Recv.).

![](images/fdf8282d9dabfe396d65f80eb1af5773360e01336e5bbc8b9f3d0a0747ea337b.jpg)  
(a)  $\mathsf{TM}_0$ -ch  
(c)  $\mathsf{TM}_2$ -ch

![](images/2d24d8a8b7d08d37ed123d80324aebb0ffd53d53fb937a31daedeb10d6ee915f.jpg)

![](images/3fae35016692be95769cdf4f1ebac2c345e5707d0f14926aa363ad2fb42bf9b2.jpg)  
(b)  $\mathsf{TM}_1$ -ch

![](images/084ed029bbedad9db1943118f3b00405072045ea6907ee586fff7dca78e54d22.jpg)

![](images/a61d6f3899faa1351157aeefb4e78404a8ad866a338f662dabf80db2db2e6299.jpg)  
Figure 9. Measured eye-diagram with the PIC consisting of a  $10 \times 1$  mode multiplexer with three input ports ( $\mathrm{I}_1 \sim \mathrm{I}_{10}$ ), a wide multimode bus waveguide, and a  $1 \times 10$  mode demultiplexer with three output ports ( $\mathrm{O}_1 \sim \mathrm{O}_{10}$ ). Here the wavelengths are chosen as  $(\lambda_1, \lambda_2) = (1546.92, 1554.13)$  nm, and the mode channel is chosen as a) the  $\mathrm{TM}_0$  mode-channel, b) the  $\mathrm{TM}_1$  mode-channel, c) the  $\mathrm{TM}_2$  mode-channel, and d) the  $\mathrm{TM}_3$  mode-channel, respectively.

![](images/45d969930646e22e9acb295828fc51fa459a19116b2ecd88c53fd887c84c0bdf.jpg)

![](images/ad1643fc0ccad712b811e81622bdb63df9ceb8078d86fff748a5922a6f4c577e.jpg)  
(d)  $\mathsf{TM}_3$ -ch

![](images/a6e9ca4bddab7362d0691a7a75e57117ae3f54a622e0421b02bdf13930b63469.jpg)

The mode (de)multiplexer has a  $2.3\mu \mathrm{m}$  wide bus waveguide, which supports six mode-channels of TE polarization and four mode-channels of TM polarizations. These ten mode-channels are (de)multiplexed with five cascaded dual-core adiabatic tapers and six integrated PBSs. Each of the adiabatic dual-core tapers can simultaneously drop a TE mode-channel and a TM mode-channel from the multimode bus waveguide to the singlemode narrow waveguide. The TE and TM mode-channels are then separated out using the integrated PBS. The experimental results show robust performance of the 10-channel (de)multiplexer, with a low optical crosstalk ( $\sim -20$  dB) over a large wavelength range from  $1525~\mathrm{nm}$  to  $1610~\mathrm{nm}$  (covering the C-band). The excess loss and the crosstalk can be reduced further by improving the fabrication. The mode (de)-multiplexer can significantly enhance the data capacity per wavelength light carrier in a hybrid MDM-PDM-WDM optical link.

# Acknowledgements

This project was partially supported by National Natural Science Foundation of China (NSFC) (61725503, 61431166001, 61422510, and 61475138), Zhejiang Provincial Natural Science Foundation of China (Z18F050002), National Key Research and Development Plan (2016YFB0402502) and NSFC/RGC Joint Research Grant N CUHK404/14.

# Conflict of Interest

The authors have declared no conflict of interest.

# Keywords

adiabatic taper; mode multiplexing; nanowire; polarization; silicon

Received: April 28, 2017

Revised: September 28, 2017

Published online: November 20, 2017

[1] M. J. Paniccia, Optik  $\alpha$  hotonik 2011, 6, 34.  
[2] P. J. Winzer, Nature Photon. 2014, 8, 345.  
[3] R. G. H. van Uden, R. Amezcua Correa, E. Antonio Lopez, F. M. Huijskens, C. Xia, G. Li, A. Schulzgen, H. de Waardt, A. M. J. Koonen, C. M. Okonkwo, Nature Photon. 2014, 8, 865.  
[4] D. J. Richardson, J. M. Fini, L. E. Nelson, Nature Photon. 2013, 7, 354.  
[5] N. Zhao, X. Li, G. Li, J. M. Kahn, Nature Photon. 2015, 9, 822.  
[6] D. Dai, J. E Bowers, Nanophoton. 2014, 3, 283.  
[7] E. Agrell, M. Karlsson, A. R. Chraplyvy, D. J. Richardson, P. M. Krummrich, P. Winzer, K. Roberts, J. K. Fischer, S. J. Savory, B. J. Eggleton, M. Secondini, F. R. Kschischang, A. Lord, J. Prat, I. Tomkos, J. E Bowers, S. Srinivasan, M. Brandt-Pearce, N. Gisin, J. Opt. 2016, 18, 063002.  
[8] K. Igarashi, D. Soma, Y. Wakayama, K. Takeshima, Y. Kawaguchi, N. Yoshikane, T. Tsuritani, I. Morita, M. Suzuki, Opt. Express 2016, 24, 10213.  
[9] Y. Yadin, M. Orenstein, J. Lightwave Technol. 2006, 24, 380.  
[10] C. R. Doerr, T. Taunay, IEEE Photon. Tech. Lett. 2011, 23, 597.  
[11] C. R. Doerr, P. J. Winzer, Y. Chen, S. Chandrasekhar, M. S. Rasras, L. Chen, T.-Y. Liow, K.-W. Ang, G.-Q. Lo, J. Lightwave Technol. 2010, 28, 520.

[12] R. Soref. IEEE J. Sel. Top. Quant. Electron. 2006, 12, 1678.  
[13] D. Thomson, A. Zilkie, J. E Bowers, T. Komljenovic, G. T Reed, L. Vivien, D. Harris-Morini, E. Cassan, L. Virot, J.-M. Fédéli, J.- M. Hartmann, J. H. Schmid, D.-X. Xu, F. Boeuf, P. O'Brien, G. Z. Mashanovich, M. Nedeljkovic, J. Opt. 2016, 18, 073003.  
[14] W. Bogaerts, S. K. Selvaraja, P. Dumon, J. Brouckaert, K. De Vos, D. Van Thourhout, R. Baets, IEEE J. Sel. Top. Quant. Electron. 2010, 16, 33.  
[15] D. Dai, J. Lightwave Technol. 2017, 35, 572.  
[16] K. Xu, C. Y. Wong, L. Zhang, L. Liu, N. Liu, C. W. Chow, H. K. Tsang, Conference on Lasers and Electro-Optics, OSA Technical Digest (2016), Optical Society of America, 2016. paper STu1G.7.  
[17] W. Bogaerts, P. Dumon, D. V. Thouhout, D. Taillaert, P. Jaenen, J. Wouters, S. Beckx, V. Wiaux, R. G. Baets, IEEE J. Sel. Top. Quantum Electron. 2006, 12, 1394.  
[18] D. Dai, J. Bauters, J. E Bowers, Light Sci. Appl. 2012, 1, 1.  
[19] D. Dai, J. Wang, S. He. Prog. Electromagn. Res. 2013, 143, 773.  
[20] C. Williams, B. Banan, G. Cowan, O. Liboiron-Ladouceur, IEEE J. Sel. Top. Quant. Electron. 2016, 22, 473.  
[21] H. Jia, L. Zhang, J. Ding, L. Zheng, C. Yuan, L. Yang, Opt. Express 2017, 25, 422.  
[22] T. Uematsu, Y. Ishizaka, Y. Kawaguchi, K. Saitoh, M. Koshiba, J. Light-wave Technol. 2012, 30, 2421.  
[23] J. Driscoll, R. Grote, B. Souhan, J. Dadap, M. Lu, R. Osgood, Opt. Lett. 2013, 38, 1854.

[24] W. Chen, P. Wang, J. Yang, Opt. Express 2013, 21, 25113.  
[25] L. F. Frellsen, Y. Ding, O. Sigmund, L. H. Frandsen, Opt. Express 2016, 24, 16866.  
[26] J. Xing, Z. Li, X. Xiao, J. Yu, Y. Yu, Opt. Lett. 2013, 38, 3468.  
[27] C. Sun, Y. Yu, G. Chen, X. Zhang, Opt. Lett. 2016, 41, 5511.  
[28] M. Greenberg, M. Orenstein, Opt. Express 2005, 13, 9381.  
[29] Y. Ding, J. Xu, F. Da Ros, B. Huang, H. Ou, C. Peucheret, Opt. Express 2013, 21, 10376.  
[30] D. Dai, J. Wang, Y. Shi, Opt. Lett. 2013, 38, 1422.  
[31] H. Qiu, H. Yu, T. Hu, G. Jiang, H. Shao, P. Yu, J. Yang, X. Jiang. Opt. Express 2013, 21, 17904.  
[32] L. W. Luo, N. Ophir, C. P. Chen, L. H. Gabrielli, C. B. Poitras, K. Bergmen, M. Lipson, Nature Commun. 2014, 5, 3069.  
[33] Y. Yang, Y. Li, Y. Huang, A. Poon, Opt. Express 2014, 22, 22172.  
[34] J. Wang, S. Chen, D. Dai, Opt. Lett. 2014, 39, 6993.  
[35] D. Dai, J. Wang, S. Chen, S. Wang, S. He, Laser Photon. Rev. 2015, 9, 339.  
[36] W. Bogaerts, D. Taillaert, P. Dumon, D. Van Thourhout, R. Baets, E. Pluk, Opt. Express 2007, 15, 1567.  
[37] S. Chen, Y. Shi, S. He, D. Dai. Opt. Express 2015, 23, 12840.  
[38] J. Wang, S. He, D. Dai, Laser Photon. Rev. 2014, 8, L18.  
[39] J. Wang, P. Chen, S. Chen, Y. Shi, D. Dai, Opt. Express 2014, 22, 12799.  
[40] H. Wu, Y. Tan, D. Dai, Opt. Express 2017, 25, 6069.  
[41] D. Dai, J. E Bowers, Opt. Express 2011, 19, 18614.