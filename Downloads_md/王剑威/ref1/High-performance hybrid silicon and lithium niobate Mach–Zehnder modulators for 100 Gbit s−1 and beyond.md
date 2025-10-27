# High-performance hybrid silicon and lithium niobate Mach-Zehnder modulators for 100 Gbits $^{-1}$  and beyond

Mingbo He $^{1}$ , Mengyue Xu $^{1}$ , Yuxuan Ren $^{2}$ , Jian Jian $^{1}$ , Ziliang Ruan $^{2}$ , Yongsheng Xu $^{2}$ , Shengqian Gao $^{1}$ , Shihao Sun $^{1}$ , Xueqin Wen $^{2}$ , Lidan Zhou $^{1}$ , Lin Liu $^{1}$ , Changjian Guo $^{2}$ , Hui Chen $^{1}$ , Siyuan Yu $^{1}$ , Liu Liu $^{1*}$  and Xinlun Cai $^{1*}$

Optical modulators are at the heart of optical communication links. Ideally, they should feature low loss, low drive voltage, large bandwidth, high linearity, compact footprint and low manufacturing cost. Unfortunately, these criteria have been achieved only on separate occasions. Based on a silicon and lithium niobate hybrid integration platform, we demonstrate Mach-Zehnder modulators that simultaneously fulfil these criteria. The presented device exhibits an insertion loss of 2.5 dB, voltage-length product of  $2.2\mathrm{Vcm}$  in single-drive push-pull operation, high linearity, electro-optic bandwidth of at least 70 GHz and modulation rates up to 112 Gbit s $^{-1}$ . The high-performance modulator is realized by seamless integration of a high-contrast waveguide based on lithium niobate—a popular modulator material—with compact, low-loss silicon circuitry. The hybrid platform demonstrated here allows for the combination of 'best-in-breed' active and passive components, opening up new avenues for future high-speed, energy-efficient and cost-effective optical communication networks.

Global data traffic has witnessed continuous growth over the past three decades due to the insatiable demands of modern society<sup>1</sup>. This rapid expansion is placing a serious challenge on transceivers in all levels of optical networks—how to significantly increase data rates while reducing energy consumption and cost<sup>2,3</sup>. To address this challenge, silicon photonics on the silicon-on-insulator (SOI) platform has emerged as the leading technology due to the possibility of low-cost and high-volume production of photonic integrated circuits (PICs) in CMOS foundries<sup>4-8</sup>.

Optical modulators are key components serving as the information encoding engines from the electrical domain to the optical domain. Optical modulation in silicon relies mainly on the free-carrier dispersion effect[9-14]. Unfortunately, free-carrier dispersion is intrinsically absorptive and nonlinear, which degrades the optical modulation amplitude (OMA) and may lead to signal distortion when using advanced modulation formats.

Tremendous efforts have been made towards realizing high-performance optical modulators in various material platforms[15-26]. Among them, lithium niobate (LN) remains a preferred material due to its excellent electro-optic (EO) modulation properties originating from the Pockels effect[27,28]. LN modulators show unrivaled results for the generation of high-baud-rate multilevel signals and are still the best choice for ultra-long-haul links[29]. Conventional LN modulators are formed by low-index-contrast waveguides with weak optical confinement, and the microwave electrodes must be placed far away from the optical waveguide to minimize absorption losses, which leads to an increased drive voltage. As a result, conventional LN modulators are bulky in size and low in modulation efficiency  $(V_{\pi}L > 10\mathrm{Vcm})$ . Recently, LN membranes on insulator (LNOI) has emerged as a promising platform to form waveguide

devices with good confinement $^{29-40}$ , and LNOI modulators with a low drive voltage and ultrahigh EO bandwidth have been recently demonstrated $^{39,41,42}$ .

An alternative approach—hybrid integration of LN membranes onto SOI PICs—has also attracted considerable interest[43,44]. The hybrid silicon/LN material system combines the scalability of silicon photonics with the excellent modulation performance of LN. A few demonstrations of hybrid Si/LN optical modulators have been reported, all of which rely on a supermode waveguide structure consisting of an unpatterned LN membrane on top of a silicon waveguide. This structure is designed to support a distributed optical mode that resides in both the LN and the underlying silicon waveguide (that is only part of the modal power overlaps with the LN region), which compromises the modulation efficiency. In fact, the hybrid Si/LN optical modulators demonstrated so far show either low EO bandwidth or high operation voltage.

Here, we demonstrate hybrid Si/LN Mach-Zehnder modulators (MZMs) that employ two layers of hybrid integrated waveguides and vertical adiabatic couplers (VACs). The VACs transfer the optical power fully, rather than partially, between the silicon waveguide and LN membrane waveguide. This approach efficiently utilizes the LN membrane and overcomes the trade-off in the previous approaches. The proposed devices show a large EO bandwidth, high modulation efficiency, low on-chip insertion loss and high linearity. On-off keying (OOK) modulation up to  $100\mathrm{Gbits}^{-1}$  and four-level pulse amplitude modulation (PAM-4) up to  $112\mathrm{Gbits}^{-1}$  are successfully demonstrated.

# Results

Design of hybrid silicon and LN MZMs. The devices were fabricated based on benzocyclobuten (BCB) adhesive die-to-wafer

![](images/cd43b36a0161c34c44e30366cdbbad151c729dc0dc33a0d3678736c0bbe1ca8b.jpg)  
a  
f

![](images/ca1e30a839a7df79c40bbce4f225a94cf303652879cc0b1f7c9b8db1b5e7a729.jpg)  
b

![](images/96375fbe5d122a1fe4bce80e8c5f32e0097c27fc6626d92f2ae421c4e7c4e8f3.jpg)  
C

![](images/bfdfa88e1898d7e057128e760e2be9599981924fe7ffb8f7ad755133a826635e.jpg)  
d

![](images/52c04866ed2c3bb2ce2c35203fbc2ad1b26090be7df6bef37e8d85585494f962.jpg)  
e  
Fig. 1 | Structure of the hybrid Si/LN MZM. a, Schematic of the structure of the whole circuit. b, Schematic of the cross-section of the hybrid waveguide. c, Scanning electron microscopy (SEM) image of the cross-section of the LN waveguide. d, SEM image of the metal electrodes and the optical waveguide. e, Schematic of the VAC. f, SEM images of the cross-sections of the VAC at different positions (A, B, C) and calculated mode distributions associated with the cross-sections. A rainbow style colour map is used to represent the mode-field intensities, where the red indicates the strongest intensity.

![](images/626b9ba8fe620cc03226eda2e859b788ff442e772835e80fcd96409cc2ed9845.jpg)

![](images/2e2ff651085b21477a5e66d18a80ba298b29c103c9ad4466aae66e35ceda21be.jpg)

![](images/e6b943b2b9117cbc3693d43057b1b8b5c6de788d3f016197efd5a743c79bece7.jpg)

![](images/8663bf9848725e1698bbedb921ea247a1b5dabb5ea17c828060b12fe5a59e07c.jpg)  
A  
B

![](images/7788d81444cfab88675651a41754f13933d6ab1564929ed4bb08d4720f55b03e.jpg)  
C

![](images/ff383b3a5166da71e4fc7a30d6b1b5e174bde45353dc7e17b996c6731c0628e2.jpg)

![](images/d486e7eda8f1318e660927f1510e6af1227beade927201caa9e1e26cca8b82b7.jpg)  
Fig. 2 | Static EO performance. a, Normalized optical transmission of the  $3\mathrm{mm}$  and  $5\mathrm{mm}$  devices as a function of the applied voltage, showing  $V_{\pi}$  values of  $7.4\mathrm{V}$  and  $5.1\mathrm{V}$ , respectively. The inset shows the measured extinction ratio (ER) on a logarithmic scale. b, Measured spectral response of the MZM biased at quadrature, indicating broadband operation of the device. a.u., arbitrary units.

![](images/cea5a6e9e661c041dd303f9a3e14b6c86ea6229c491bd09b5ef3d4a0d8ee7fab.jpg)  
b

bonding and LN dry-etching techniques. Figure 1a shows the schematic view of the present Si/LN hybrid MZM, consisting of two waveguide layers and VACs. The top waveguides, formed by dry-etching of an X-cut LN membrane, serve as phase modulators

where EO interactions (Pockels effect) occur. The bottom SOI circuit supports all other passive functions, consisting of two 3dB multimode interference (MMI) couplers that split and combine the optical power, and two grating couplers for off-chip coupling.

![](images/796475c6eb78aecf9eba918c130621fbd8fcee30886fbcd7f4d775ccc39ef781.jpg)  
a

![](images/77b07c7af5a7c2928f1ac61bc01a9659d1f15520e5e6d13c649f229c8dcaefc9.jpg)  
c

![](images/3542ac92bd190519299544560dffc8524e6ce9e4e3aee338390aeb6c479050ce.jpg)  
b

![](images/c394a3b8312bec903166e2cf065fa1fd0c9923091f8e7d4f4c4ecffb25064f04.jpg)  
d

![](images/6f070b81dd215d585bc0aa029b23541ff2889ef646a1f4c1ba687b14bce85e9e.jpg)  
Fig. 3 | EO bandwidth and linearity. a, Experimental set-up for measuring the EO bandwidth. VNA, vector network analyser; EDFA, erbium-doped fiber amplifier; BPF, bandpass filter; PD, photodetector; PC, polarization controller. b, EO bandwidths  $(S_{21}$  parameter) of MZMs with lengths of  $3\mathrm{mm}$  and  $5\mathrm{mm}$ . The 3 dB bandwidths of both devices are beyond the measurement limit of the VNA (70 GHz). c, Experimental set-up for measuring the IMD3 SFDR. d, RF output power of the fundamental and IMD3 components as a function of RF input power for our device at 1GHz and 10 GHz, and for a commercially available LN MZM at 1GHz. The noise floor is in 1Hz bandwidth, limited by the RF spectral analyser.

The VACs, which were formed by silicon inverse tapers and superimposed LN waveguides, serve as interfaces to couple light up and down between the two layers. This hybrid integration architecture offers two distinct advantages. First, since the task of routing light across the chip is placed on the underlying silicon waveguides, only simple, straight waveguides need to be fabricated in the LN membrane. This allows for a more compact device footprint and greater flexibility in the LN waveguide design, compared with that of devices based on the pure LNOI platform. Second, the VACs, together with the dry-etched LN waveguide design, facilitate high overlap between the optical modes and active material, as well as good optical confinement in LN waveguides. This enables more efficient utilization of the LN active region, in contrast to other hybrid Si/LN hybrid devices with unpatterned LN membranes. The schematic of the cross-section of the hybrid waveguide is illustrated in Fig. 1b.

The LN waveguide is the most critical part of the present device and has to be optimized to achieve high modulation efficiency and low optical loss. The fabricated waveguides have a top width of  $w = 1\mu \mathrm{m}$ , a slab thickness of  $s = 420\mathrm{nm}$ , a rib height of  $h = 180\mathrm{nm}$  and a sidewall angle of  $60^{\circ}$  (Fig. 1c). The lithography and etching processes were optimized to yield smooth sidewalls and the LN waveguide features a measured propagation loss of  $0.98\mathrm{dBcm}^{-1}$  (Supplementary Section III). The gap between the waveguides and electrodes was set to  $2.75\mu \mathrm{m}$ . These parameters are designed to achieve a good balance between the modulation efficiency and optical losses (including both metal absorption and sidewall scattering loss) (Supplementary Section I). The electrodes are configured in a ground-signal-ground (GSG) form, where the two LN waveguides lie in the two gaps between the

ground and signal metals. To achieve a large EO bandwidth, the electrodes are operated in a travelling wave manner and optimized for impedance matching, as well as velocity matching of the microwave and light signals (Supplementary Section II). The thickness of electrodes was set to  $t = 600\mathrm{nm}$ , and the widths of signal and ground electrodes were designed as  $w_{s} = 19.5\mu \mathrm{m}$  and  $w_{o} = 30\mu \mathrm{m}$ , respectively (Fig. 1b,d).

The VAC is another important part of the device (Fig. 1e) and must be optimized for high efficiency. The width of the silicon waveguide tapers from  $500\mathrm{nm}$  to  $80\mathrm{nm}$  over a length of  $150\mu \mathrm{m}$ , whereas the width of the LN waveguide remains constant at  $1\mu \mathrm{m}$ . The thickness of the BCB is  $\sim 300\mathrm{nm}$  (that is, the gap between the bottom of the LN waveguide and the top of the silicon waveguide is  $80\mathrm{nm}$ ), which is sufficiently robust with respect to the variations induced by the fabrication processes. The measured coupling efficiency of the VAC is  $>97\%$  (loss of  $\sim 0.19\mathrm{dB}$  per VAC) (Supplementary Section III). It should be noted that simulation indicates that the silicon taper tip width can be as large as  $200\mathrm{nm}$  with negligible degradation in coupling efficiency, which means the present design is compatible with standard mass production processes (Supplementary Section III). Figure 1f presents snapshots of the optical intensity patterns for various cross-sections of the VAC, which illustrates the process of mode transfer.

Static EO performance. Fabricated MZM devices with arm lengths of  $3\mathrm{mm}$  and  $5\mathrm{mm}$  were measured in detail. The devices are driven in a single-drive push-pull configuration, so that applied voltage induces a positive phase shift in one arm and a negative phase shift in the other. Figure 2a shows the half-wave voltage measurements for both devices with a  $100\mathrm{kHz}$  triangular voltage sweep; the half-wave

![](images/ec53ba7db83eefec284293c55a2f58a38618a71e1c107b602231205faa413219.jpg)

![](images/501923498dbfb8924e7e15a7e3d865c7216ae4062314917267b71e02e5e26d04.jpg)  
56 Gbs-1OOK

![](images/f3eb478ebe601f9df743e59cb8e0ae202652e868d90910f3386807c9f1613702.jpg)

![](images/365014ce369fe7fe4d79d0acf9482c1417c63e6f899375a54a65e6d912a03479.jpg)

![](images/0fb6063cf69c3ef1f5fe8aa5a4d36b9fa814cea0cbe7691836290ce315528030.jpg)  
56 Gbs-1PAM-4 (28 Gbaud)  
112 Gbs-1 PAM-4 (56 Gbaud)

![](images/7581334616779070efd0c9da6c15106d4b1bd32f8983919b5a8928696d7b5e38.jpg)  
72 Gbs-1OOK

![](images/2f4067453bd2fef53b6fa6a971c42ed05486932121050fb701967abf99e56637.jpg)  
Received optical power (dBm)

![](images/0cca77722a10e58365a0f9b2c7ed8c8bedee1d150dcd756c96a97c2299a0f964.jpg)  
84 Gbs-1OOK  
Fig. 4 | Data transmission testing. a, Experimental set-up for measuring the eye diagram. AWG, arbitrary waveform generator. b-e, Optical eye diagrams for OOK signal at data rates of  $56\mathrm{Gbs}^{-1}$  (b),  $72\mathrm{Gbs}^{-1}$  (c),  $84\mathrm{Gbs}^{-1}$  (d) and  $100\mathrm{Gbs}^{-1}$  (e). The dynamic extinction ratios are 11.8 dB, 6.0 dB, 5.5 dB and 5.0 dB, respectively. f,g, Measured PAM-4 modulation optical eye diagrams at 28 Gbaud  $(50\mathrm{Gbs}^{-1})$  (f) and 56 Gbaud  $(112\mathrm{Gbs}^{-1})$  (g). h, Measured curves of BER versus the received optical power for 28 Gbaud  $(56\mathrm{Gbs}^{-1})$  and 56 Gbaud  $(112\mathrm{Gbs}^{-1})$  PAM-4 signal.  
100 Gb s $^{-1}$  OOK

voltages  $V_{\pi}$  for the  $3\mathrm{mm}$  and  $5\mathrm{mm}$  devices are  $7.4\mathrm{V}$  and  $5.1\mathrm{V}$ , corresponding to voltage-length products of  $2.2\mathrm{Vcm}$  and  $2.5\mathrm{Vcm}$ , respectively. It should be noted that the voltage-length products are measured in a single-drive push-pull configuration and the value measured in a single arm will be increased by a factor of two. The inset of Fig. 2a shows the optical transmission on a logarithmic scale, indicating a measured extinction ratio of greater than  $40\mathrm{dB}$  for the  $3\mathrm{mm}$  device. Figure 2b shows the measured spectral response of the MZM biased at quadrature, indicating broadband operation of the

device in the whole C-band. The  $V_{\pi}$  value of the present device can be further reduced by simply increasing the device length, as an LNOI modulator with  $V_{\pi} = 1.4\mathrm{V}$  was recently achieved with a device length of  $2\mathrm{cm}$  (ref. [39]). For the proposed Si/LN hybrid modulator,  $V_{\pi}$  of about  $1\mathrm{V}$  is expected with a similar length. This would enable driverless modulation from direct CMOS output without compromising the extinction ratio. In addition, a device with such a length can also fit in some common transceiver packages like QSFP (Quad Small Form-factor Pluggable) and can be adopted for future  $400\mathrm{G}$  applications[45].

Table 1 | Comparison of several performance metrics for hybrid silicon MZM  

<table><tr><td></td><td>Loss</td><td>Vπ</td><td>EO bandwidth</td><td>OOK data rate</td><td>Length of modulation area</td></tr><tr><td>SOI10</td><td>5.4 dB</td><td>7 V</td><td>58 GHz</td><td>90 Gbs-1</td><td>2 mm</td></tr><tr><td>SOH20</td><td>11 dB</td><td>22 V</td><td>&gt;100 GHz</td><td>NA</td><td>0.5 mm</td></tr><tr><td>SOH47</td><td>&gt;11 dBa</td><td>0.9 V</td><td>25 GHz</td><td>100 Gbs-1</td><td>1.1 mm</td></tr><tr><td>SOH plasmonic48</td><td>12 dB</td><td>&gt;40 Vb</td><td>&gt;65 GHz</td><td>40 Gbs-1</td><td>29 μm</td></tr><tr><td>Si/BTO plasmonic49</td><td>30 dBc</td><td>25 V</td><td>&gt;100 GHz</td><td>72 Gbs-1</td><td>10 μm</td></tr><tr><td>Si/BTO50</td><td>3.3 dBd</td><td>20 V</td><td>800 MHz</td><td>300 Mb s-1</td><td>0.75 mm</td></tr><tr><td>This work</td><td>2.5 dB</td><td>5.1 V</td><td>&gt;70 GHz</td><td>100 Gbs-1</td><td>5 mm</td></tr></table>

${}^{a}$  The value is calculated from  ${20}\mathrm{\;{dB}}$  fibre-to-fibre loss and  $9\mathrm{\;{dB}}$  off-chip coupling loss.  ${}^{b}$  The value is calculated from the reported  ${V}_{ * }L$  of  ${1.3}\mathrm{\;V}\mathrm{\;{mm}}$  and length of  ${29\mu }\mathrm{m}$  .  ${}^{c}$  The value is calculated from propagation loss of  $2\mathrm{{dB}}{\mu }_{\mathrm{m}}{}^{-1}$  with  ${10\mu }\mathrm{m}$  length,and  ${10}\mathrm{\;{dB}}$  loss for two photonic-plasmonic converters.  ${}^{d}$  The value is calculated from propagation loss of  ${44}\mathrm{\;{dB}}{\mathrm{\;{cm}}}^{-1}$  with  ${0.75}\mathrm{\;{mm}}$  length. NA,not available.

EO bandwidth and linearity. We then characterized the small-signal EO bandwidth  $(S_{21}$  parameter) of the fabricated devices using the set-up shown in Fig. 3a. The measured 3 dB EO bandwidths of both devices are greater than  $70\mathrm{GHz}$  (Fig. 3b), which is beyond the measurement limits of our vector network analyser (VNA). The measured EO bandwidth is much higher than that of pure silicon-based modulators. We believe that the EO bandwidth of the present device could be extended beyond  $100\mathrm{GHz}$  by further optimizing the travelling-wave electrode (Supplementary Section II).

To characterize the linearity of the present device, we further examine the third-order intermodulation (IMD3) spurious free dynamic range (SFDR) performance of the  $3\mathrm{mm}$  device using the set-up shown in Fig. 3c. To provide a comparative study, we also measured the IMD3 SFDR of a commercially available LN MZM (Fujitsu FTM7937EZ) with the same measurement system. Both devices are biased at quadrature and the optical power reaching the photodetector after pre-amplification is kept at  $0\mathrm{dBm}$ . For our device, the measured IMD3 SFDR is  $99.6\mathrm{dBHz}^{2/3}$  at  $1\mathrm{GHz}$  (Fig. 3d), which is slightly better than that achieved by the commercial LN MZM  $(94.9\mathrm{dBHz}^{2/3})$ . At  $10\mathrm{GHz}$ , the measured SFDR decreases slightly to  $95.2\mathrm{dBHz}^{2/3}$ , mainly due to a higher noise floor of the measurement system. The SFDR value can be increased further by increasing the received optical power.

Data transmission testing. Next, we evaluated the performance of the  $3\mathrm{mm}$  device for high-speed digital data transmission, as depicted in Fig. 4a. First, the OOK modulations were applied to the device. Figure 4b-e summarizes the optical eye diagrams at 56, 72, 84 and  $100\mathrm{Gb}\mathrm{s}^{-1}$ . The measured extinction ratios are 11.8, 6.0, 5.5 and  $5.0\mathrm{dB}$ , respectively. It is noteworthy that at  $100\mathrm{Gb}\mathrm{s}^{-1}$  the whole measurement system is already limited by the bandwidth of the radiofrequency (RF) probe and cables. PAM-4 modulation experiments were also carried out with the same experimental set-up. The optical PAM-4 eye-diagrams at 28Gbaud and 56Gbaud are shown in Fig. 4f,g. The back to back (B2B) bit-error rate (BER) curves at both PAM-4 data rates, shown in Fig. 4h, decrease linearly as the received optical power before pre-amplification increases. No error floor is observed in the measured power range, and the error rates are also well below the hard-FEC limit of  $3.8\times 10^{-3}$ .

# Discussion

As presented above, the hybrid Si/LN MZMs demonstrated here can achieve excellent optical modulation characteristics, while maintaining the key advantages of SOI photonic circuits. LN active waveguides can be bonded and fabricated with lithographic precision and alignment accuracy in a back-end process after the SOI fabrication. This manufacturing procedure is highly scalable and fully CMOS-compatible. Therefore, our approach potentially provides a new generation of compact, high-performance optical modulators for telecommunications and data-interconnects.

It should be noted that approaches of combining silicon with other materials exhibiting Pockels effects, such as organic materials and barium titanate (BTO), have also been reported. In Table 1, we compare the performance of the present device with the state-of-the-art, including silicon-organic-hybrid (SOH) MZMs, SOH plasmonic MZMs and BTO/Si plasmonic MZMs. Here, we focus on MZMs with either large EO bandwidth or high operation speed, and results of pure silicon modulators operating in the carrier depletion mode are also included as a benchmark. As shown in Table 1, the present device in this work is the only one in which low  $V_{\pi}$  and low insertion loss are achieved simultaneously. In particular, the insertion loss of the present device is much lower than that of all others, and to the best of our knowledge, this is the lowest insertion loss ever achieved in optical modulators operating above  $40\mathrm{Gbits^{-1}}$  on silicon. The demonstrated  $V_{\pi}$  of the present device is also promising, which is only surpassed by the SOH modulator with a much higher insertion loss. As discussed above,  $V_{\pi}$  can be further engineered to be about  $1\mathrm{V}$  while maintaining an insertion loss of less than  $4\mathrm{dB}$ . A low  $V_{\pi}$  is critical for a travelling-wave type of modulator, since the energy consumption per bit is proportional to the square of the driving voltage. For the data transmission experiments in Fig.4, the energy consumption of the present device of  $3\mathrm{mm}$  length is estimated to be about  $170\mathrm{fJ}$  per bit (see Supplementary Section II). It has been recently proved that tens of aJ per bit energy consumption can be achieved for LN thin film modulators, although at a compromised BER[39]. We believe that a similar performance can be expected for the present Si/LN hybrid device, since the cross-section structures of the phase shifter section are very similar for the two cases. Another approach for decreasing the energy consumption is to use a resonant device with lumped electrodes instead of a travelling-wave design[32,35], but the working wavelength band, in this case, is limited.

The underlying silicon waveguides not only route light with low losses across the chip, but also allow integration of the present modulator with the complete suite of silicon photonic components. This makes the proposed Si/LN platform highly desirable for new emerging applications. For instance, future integrated microwave photonic (MwP) systems would require on-chip linear modulators featuring high-fidelity electronic-to-optical conversion. The present device is ideal for this scenario and can be envisaged to be co-integrated with passive SOI structures, such as Bragg gratings or microresonators, to form sophisticated integrated MwP circuits. Another possible application area could be linear optical quantum computing (LOQC) $^{46}$ . LOQC relies on universal quantum gates, which could be implemented by adding auxiliary photons and by using rapid, time-of-flight feedforward. In practice, a feedforward step requires large-scale, low-loss, rapidly reconfigurable (in the gigahertz range) optical circuits capable of low-noise pure phase modulation—requirements that are attainable on our platform. The present platform is also amenable to further integration with lasers and detectors, as well as high-speed electronic drivers based on CMOS

technology, offering fully integrated solutions for future terabit-per-second datacom and interconnect applications. The fabrication process can also be adapted for materials such as  $\mathrm{Si}_3\mathrm{N}_4$ , which enables ultralow-loss PICs and is a potential platform for exploring nonlinear optical processes.

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, statements of data availability and associated accession codes are available at https://doi.org/10.1038/s41566-019-0378-6.

Received: 27 May 2018; Accepted: 1 February 2019

Published online: 4 March 2019

# References

1. Cisco Cisco Visual Networking Index: Forecast and Methodology 2015-2020 (Cisco, 2016).  
2. Tkach, R. W. Scaling optical communications for the next decade and beyond. Bell Labs Tech. J. 14, 3-10 (2010).  
3. Kilper, D. C. & Rastegarfar, H. Energy challenges in optical access and aggregation networks. Phil. Trans. R. Soc. A. 374, 20140435 (2016).  
4. Miller, D. Device requirements for optical interconnects to CMOS silicon chips. In Photonics in Switching PMB3 (OSA, 2010).  
5. Reed, G. T., Mashanovich, G., Gardes, F. Y. & Thomson, D. J. Silicon optical modulators. Nat. Photon. 4, 518-526 (2010).  
6. Heck, M. J. et al. Hybrid silicon photonics for optical interconnects. IEEE J. Sel. Top. Quantum Electron. 17, 333-346 (2011).  
7. Bogaerts, W. et al. Nanophotonic waveguides in silicon-on-insulator fabricated with CMOS technology. J. Lightwave Technol. 23, 401-412 (2005).  
8. Sun, C. et al. Single-chip microprocessor that communicates directly using light. Nature 528, 534-538 (2015).  
9. Xu, Q., Schmidt, B., Pradhan, S. & Lipson, M. J. Micrometre-scale silicon electro-optic modulator. Nature 435, 325-327 (2005).  
10. Li, M. et al. Silicon intensity Mach-Zehnder modulator for single lane 100Gb/s applications. Photon. Res. 6, 109-116 (2018).  
11. Ding, R. et al. High-speed silicon modulator with slow-wave electrodes and fully independent differential drive. J. Lightwave Technol. 32, 2240-2247 (2014).  
12. Dong, P. et al. Monolithic silicon photonic integrated circuits for compact  $100+$  Gb/s coherent optical receivers and transmitters. IEEE J. Sel. Top. Quantum Electron. 20, 150-157 (2014).  
13. Samani, A. et al. Experimental parametric study of 128 Gb/s PAM-4 transmission system using a multi-electrode silicon photonic Mach Zehnder modulator. Opt. Express 25, 13252–13262 (2017).  
14. Timurdogan, E. et al. An ultralow power athermal silicon modulator. Nat. Commun. 5, 4008 (2014).  
15. Xiong, C. et al. Aluminum nitride as a new material for chip-scale optomechanics and nonlinear optics. New J. Phys. 14, 20 (2012).  
16. Zhang, C. et al. Ultralinear heterogeneously integrated ring-assisted Mach-Zehnder interferometer modulator on silicon. Optica 3, 1483-1488 (2016).  
17. Tang, Y. et al. 50Gb/s hybrid silicon traveling-wave electroabsorption modulator. Opt. Express 19, 5811-5816 (2011).  
18. Haffner, C. et al. All-plasmonic Mach-Zehnder modulator enabling optical high-speed communication at the microscale. Nat. Photon. 9, 525-528 (2015).  
19. Haffner, C. et al. Low-loss plasmon-assisted electro-optic modulator. Nature 556, 483-486 (2018).  
20. Alloatti, L. et al. 100 GHz silicon-organic hybrid modulator. Light Sci. Appl. 3, e173 (2014).  
21. Lee, M. et al. Broadband modulation of light by using an electro-optic polymer. Science 298, 1401-1403 (2002).  
22. Han, J.-H. et al. Efficient low-loss InGaAsP/Si hybrid MOS optical modulator. Nat. Photon. 11, 486-490 (2017).  
23. Kikuchi, N., Yamada, E., Shibata, Y. & Ishii, H. High-speed InP-based Mach-Zehnder modulator for advanced modulation formats. In Compound Semiconductor Integrated Circuit Symposium (CSICS) 1-4 (IEEE, 2012).  
24. Phare, C. T., Lee, Y. H. D., Cardenas, J. & Lipson, M. Graphene electro-optic modulator with 30GHz bandwidth. Nat. Photon. 9, 511-514 (2015).  
25. Liu, M. et al. A graphene-based broadband optical modulator. Nature 474, 64-67 (2011).  
26. Sorianello, V. et al. Graphene-silicon phase modulators with gigahertz bandwidth. Nat. Photon. 12, 40-44 (2018).  
27. Chen, A. Broadband Optical Modulators: Science, Technology, and Applications (CRC Press, 2011).  
28. Wooten, E. L. et al. A review of lithium niobate modulators for fiber-optic communications systems. IEEE J. Sel. Top. Quantum Electron 6, 69-82 (2000).  
29. Raybon, G. et al. Single carrier high symbol rate transmitter for data rates up to 1.0 Tb/s. In Optical Fiber Communication Conference Th3A.2 (OSA, 2016).

30. Janner, D., Tulli, D., García-Granda, M., Belmonte, M. & Pruneri, V. Micro-structured integrated electro-optic  $\mathrm{LiNbO}_3$  modulators. *Laser Photon. Rev.* 3, 301-313 (2009).  
31. Poberaj, G., Hu, H., Sohler, W. & Gunter, P. Lithium niobate on insulator (LNOI) for micro-photonics devices. *Laser Photon. Rev.* 6, 488-503 (2012).  
32. Guarino, A., Poberaj, G., Rezzonico, D., Degl'Innocenti, R. & Gunter, P. Electro-optically tunable microring resonators in lithium niobate. Nat. Photon. 1, 407-410 (2007).  
33. Jin, S., Xu, L., Zhang, H. & Li, Y.  $\mathrm{LiNbO}_3$  thin-film modulators using silicon nitride surface ridge waveguides. IEEE Photon. Technol. Lett. 28, 736-739 (2016).  
34. Rao, A. et al. High-performance and linear thin-film lithium niobate Mach-Zehnder modulators on silicon up to 50 GHz. Opt. Lett. 41, 5700-5703 (2016).  
35. Wang, J. et al. High- $Q$  lithium niobate microdisk resonators on a chip for efficient electro-optic modulation. Opt. Exp. 23, 23072-23078 (2015).  
36. Cai, L., Kang, Y. & Hu, H. Electric-optical property of the proton exchanged phase modulator in single-crystal lithium niobate thin film. Opt. Exp. 24, 4640-4647 (2016).  
37. Chang, L. et al. Thin film wavelength converters for photonic integrated circuits. Optica 3, 531-535 (2016).  
38. Chang, L. et al. Heterogeneous integration of lithium niobate and silicon nitride waveguides for wafer-scale photonic integrated circuits on silicon. Opt. Lett. 42, 803-806 (2017).  
39. Wang, C. et al. Integrated lithium niobate electro-optic modulators operating at CMOS-compatible voltages. Nature 562, 101-104 (2018).  
40. Boes, A., Corcoran, B., Chang, L., Bowers, J. & Mitchell, A. Status and potential of lithium niobate on insulator (LNOI) for photonic integrated circuits. Laser Photon. Rev. 12, 1700256 (2018).  
41. Mercante, A. J. et al. Thin film lithium niobate electro-optic modulator with terahertz operating bandwidth. Opt. Exp. 26, 14810-14816 (2018).  
42. Rao, A. & Fathpour, S. Compact lithium niobate electrooptic modulators. IEEE J. Sel. Top. Quantum Electron. 24, 1-14 (2018).  
43. Chen, L., Xu, Q., Wood, M. G. & Reano, R. M. Hybrid silicon and lithium niobate electro-optical ring modulator. Optica 1, 112-118 (2014).  
44. Weigel, P. O. et al. Bonded thin film lithium niobate modulator on a silicon photonics platform exceeding 100 GHz 3-dB electrical modulation bandwidth. Opt. Exp. 26, 23728-23739 (2018).  
45. QSFP-DD Hardware Specification for QSFP Double Density 8X Pluggable Transceiver Rev. 4.0 (QSFP-DD MSA, 2018); http://www.qsfp-dd.com/wp-content/uploads/2018/09/QSFP-DD-Hardware-rev4p0-9-12-18-clean.  
46. Kok, P. et al. Linear optical quantum computing with photonic qubits. Rev. Mod. Phys. 79, 135-174 (2007).  
47. Wolf, S. et al. Silicon-organic hybrid (SOH) Mach-Zehnder modulators for 100 Gbit/s on-off keying. Sci. Rep. 8, 2598 (2018).  
48. Melikyan, A. et al. High-speed plasmonic phase modulators. Nat. Photon. 8, 229-233 (2014).  
49. Messner, A. et al. Integrated ferroelectric  $\mathrm{BaTiO_3 / Si}$  plasmonic modulator for 100 Gbit/s and beyond. In Optical Fiber Communication Conference M2I.6 (OSA, 2018).  
50. Xiong, C. et al. Active silicon integrated nanophotonics: ferroelectric  $\mathrm{BaTiO}_3$  devices. Nano Lett. 14, 1419-1425 (2014).

# Acknowledgements

This work was supported by the National Natural Science Foundation of China (NSFC) (11690031, 61675069, 61575224, 61622510); Guangzhou Science and Technology Program (201707010444, 201701010096). X.C. would like to acknowledge helpful discussions with P. Jiang.

# Author contributions

X.C. developed the idea. X.C. and L.L. conceived device design. M.H. and J.J. carried out the LN fabrication. M.H., S.G., H.C., L.Z., L.L. and S.S. carried out the silicon fabrication. M.H. and Y.R. carried out the bonding process. M.X., Z.R., Y.X., X.W. and C.G., carried out the measurement. L.L. and X.C. carried out the data analysis. All authors contributed to the writing. X.C. finalized the paper. S.Y., L.L. and X.C. supervised the project.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s41566-019-0378-6.

Reprints and permissions information is available at www.nature.com/reprints.

Correspondence and requests for materials should be addressed to L.L. or X.C.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2019

# Methods

Fabrication. A standard SOI processing including e-beam lithography (EBL) and dry-etching processes was used to fabricate the grating coupler, 3 dB MMIs and silicon inverse tapers. An LNOI sample with silicon substrate was flip-bonded to the SOI wafer using the BCB adhesive bonding process. The substrate of the LNOI was removed by mechanical grinding and dry etching. Afterwards, hydrogen silsesquioxane (HSQ, FOX-16 by Dow Corning) was spin-coated on the LN thin film for EBL. The waveguide patterns were transferred into LN with optimized argon plasma etching in an inductively coupled plasma (ICP) etching system. The physical etching by an argon plasma results in a sidewall angle of  $\sim 60^{\circ}$ . Finally, the travelling wave electrodes were patterned through a liftoff process.

Dynamic measurement. The set-up for EO bandwidth, linearity and data transmission measurements are shown in Figs. 3 and 4, respectively. The electrical signal is fed to the device electrode through a 67-GHz-bandwidth RF probe (GGB 67A). A second RF probe (not shown) is also attached to the end of the travelling-wave electrode, and a  $50\Omega$  termination is applied to the second probe for impedance matching. For the optical signal, light from a tunable laser is coupled into and collected from the SOI grating couplers using single-mode fibres. A polarization controller is used to ensure TE input polarization. The received optical signal is pre-amplified and filtered through an erbium-doped fibre amplifier (EDFA) and a bandpass filter (BPF) before detection. A VNA is used for

bandwidth measurement, and the frequency response of the PD (XPDV4120R) is deduced from the measured  $S_{21}$  response. For linearity measurement, the input electrical signal consists of a DC bias and two RF tones with frequencies separated by 10 MHz and centred at the desired frequency. An RF spectrum analyser is used to analyse frequency components of the received electrical signal. For data transmission measurement, an arbitrary waveform generator (AWG, Micram) with a sampling rate of 100 gigasample per second is used to generate the electrical signals. A 50 GHz broadband amplifier (SHF 807) with an output saturation  $V_{\mathrm{pp}}$  of 4 V is used to amplify the driving signal to the modulator together with a DC bias. For OOK eye diagram measurements, the bias voltage is 0.7 V lower than the quadrature point to achieve better extinction ratios and the resultant additional loss is less than 0.5 dB. For PAM-4 eye diagram measurements, the modulator is biased at the quadrature point and the levels of the driving signals are deduced from an inverse trigonometric function to compensate the typical sinusoidal response of the Mach-Zehnder interferometer. Digital low-pass filters are also applied to limit the signal bandwidth. For the bit-error rate measurements, the detected signal is sampled by a real-time oscilloscope (Tektronics DPO73304) and analysed using an off-line DSP, including resampling, equalization and symbol decision (see Supplementary Section IV).

# Data availability

The data that support the plots within this paper and other findings of this study are available from the corresponding author upon reasonable request.