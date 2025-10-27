# New CMOS-compatible platforms based on silicon nitride and Hydex for nonlinear optics

David J. Moss $^{1\star}$ , Roberto Morandotti $^{2}$ , Alexander L. Gaeta $^{3}$  and Michal Lipson $^{4}$

Nonlinear photonic chips can generate and process signals all-optically with far superior performance to that possible electronically — particularly with respect to speed. Although silicon-on-insulator has been the leading platform for nonlinear optics, its high two-photon absorption at telecommunication wavelengths poses a fundamental limitation. We review recent progress in non-silicon CMOS-compatible platforms for nonlinear optics, with a focus on  $\mathrm{Si}_3\mathrm{N}_4$  and Hydex®. These material systems have opened up many new capabilities such as on-chip optical frequency comb generation and ultrafast optical pulse generation and measurement. We highlight their potential future impact as well as the challenges to achieving practical solutions for many key applications.

All-optical signal generation and processing<sup>1,2</sup> have enabled a vast array of capabilities, such as switching and demultiplexing of signals at unprecedented speeds<sup>3,4</sup>, parametric gain on a chip<sup>5</sup>, Raman lasing<sup>6</sup>, wavelength conversion<sup>7</sup>, optical logic<sup>8</sup>, all-optical regeneration<sup>9,10</sup> and radiofrequency spectroscopy at terahertz speeds<sup>11,12</sup>, as well as entirely new functions such as ultrashort pulse measurement<sup>13,14</sup> and generation<sup>15</sup> on a chip, optical temporal cloaking<sup>16</sup> and many others. Phase-sensitive functions<sup>14,17</sup>, in particular, will probably be critical for telecommunication systems that are already using phase encoding schemes<sup>18,19</sup>. The ability to produce these devices in integrated form — photonic integrated circuits — will reap the greatest dividends in terms of cost, footprint, energy consumption and performance, where demands for greater bandwidth and network flexibility and lower energy consumption and cost must all be met.

The quest for high-performance platforms for integrated nonlinear optics has naturally focused on materials with extremely high nonlinearity, and hence silicon-on-insulator (SOI) has led this field for several years. Its high refractive index allows for tight confinement of light within SOI nanowires that, when combined with its high Kerr nonlinearity  $(n_{2})$ , yields an extremely high nonlinear parameter  $\gamma$  of  $300,000\mathrm{W}^{-1}\mathrm{km}^{-1}$ $(\gamma = (\omega \times n_{2}) / (c\times A_{\mathrm{eff}})$ , where  $A_{\mathrm{eff}}$  is the effective area of the waveguide,  $c$  is the speed of light and  $\omega$  is the pump frequency).

As a platform for linear photonics, SOI has already gained a foothold as a foundation for the silicon photonic chip industry[20] that seeks to replace the large interface cards in optical communication networks; this is because of the ability of SOI to combine electronics and photonics on the same chip. These first-generation silicon photonic chips typically employ photonics for realizing passive splitters, filters and multiplexers. They offer the substantial benefits of exploiting the broadly established global complementary metal-oxide-semiconductor (CMOS) infrastructure, although this is not without its challenges[21,22]. It is clear, however, that any progress made in this direction for these first-generation SOI chips will directly benefit future generation all-optical chips, whether in SOI directly or in other CMOS-compatible platforms. Many of the advantages that make CMOS compatibility compelling for linear passive devices apply equally well to all-optical-processing chips.

The achievements reported over the past ten years for SOI devices fabricated using CMOS technology that exploit both linear and nonlinear optical phenomena $^{2,23}$  are impressive $^{23-39}$ , ranging from optical buffers $^{24}$ , optical interconnects $^{25-27}$ , ring resonators $^{28,29}$ , Raman gain and lasing $^{30-32}$ , time lensing $^{13,33}$ , slow light based on photonic crystals $^{34-36}$ , optical regeneration $^{9}$  and parametric gain $^{5,37-39}$  to the promise of direct optical transitions $^{40,41}$  and even correlated photon-pair generation $^{42}$ .

Indeed, SōI is such an attractive platform for both linear and nonlinear photonics that, were it not for one single issue, the quest for the ideal all-optical platform might already be largely solved. That issue is that bulk crystalline silicon suffers from a high nonlinear absorption because of two-photon absorption (TPA) $^{23,43}$  in all telecommunication bands with wavelengths shorter than about  $2,000~\mathrm{nm}$ . Although the effect of TPA-generated free carriers can be mitigated by, for example, using p-i-n junctions to sweep out carriers $^{44}$ , silicon's intrinsic nonlinear figure of merit (FOM =  $n_2/\beta \times \lambda$ ), where  $\beta$  is the TPA coefficient and  $\lambda$  is the wavelength) is only 0.3 near  $1,550~\mathrm{nm}$  (refs 45-47). This represents a fundamental limitation, being an intrinsic property of silicon's band structure. Consequently, it cannot be compensated for by, for example, engineering waveguide dimensions. The many impressive all-optical demonstrations in silicon despite its low FOM are a testament to how exceptional its linear and nonlinear optical properties are. Nonetheless, the critical impact of silicon's large TPA was illustrated $^{48,49}$  in 2010 by the demonstration of a high parametric gain at wavelengths beyond  $2\mu \mathrm{m}$ , where TPA vanishes. Indeed, it is probable that in the mid-infrared wavelength range (between  $2\mu \mathrm{m}$  and  $6\mu \mathrm{m}$ ), where it is transparent to both one- and two-photon transitions, silicon will undoubtedly remain a highly attractive platform for nonlinear photonics.

For the telecommunication band, however, the search is continuing for the ideal nonlinear platform. Historically, two important platforms have been chalcogenide glasses $^{50}$  and  $\mathrm{AlGaAs}^{51}$ . Chalcogenide glasses have achieved very high performance in nonlinear devices, but realising nanowires with ultrahigh nonlinearity ( $>10,000~\mathrm{W}^{-1}\mathrm{km}^{-1}$ ) has proved elusive because of fabrication challenges, as has the goal of achieving a material reliability comparable to that of semiconductors. AlGaAs was the first platform proposed

![](images/433c013dc2f62de95179b8159c4b6f23e62edab757d84fa045f84283b4cd9ea1.jpg)

![](images/dcac1bc8495d8e3cc7c023f29044f3adbfabcbab3641845188d705e2c222da15.jpg)  
Figure 1 | Silicon nitride nanowires and Hydex waveguides. a, SEM micrograph of silicon nitride nanowires reported in refs 55 and 56. The nanowires are  $500\mathrm{nm}$  thick and  $1\mu \mathrm{m}$  wide. b, Schematic and SEM image of the cross-section of a 45-cm-long spiral Hydex waveguide<sup>14</sup> prior to the final deposition of the  $\mathrm{SiO}_2$  upper cladding. The waveguide core has dimensions of  $1.45\mu \mathrm{m} \times 1.5\mu \mathrm{m}$  and is made from low-loss, high-index ( $n = 1.7$ ) doped silica. It is buried within a  $\mathrm{SiO}_2$  cladding (core-cladding contrast is  $17\%$ ). Figure a reproduced with permission from ref. 55, © 2008 OSA.

for nonlinear optics in the telecommunication band[51] and offers the powerful ability to tune its nonlinearity and FOM by varying the alloy composition. A significant issue for AlGaAs, however, is that nanowire fabrication requires using challenging fabrication methods[52] (particularly etching) in order to realize very high, narrow mesa structures. Nonetheless, both platforms offer significant advantages and will undoubtedly play a role in future all-optical photonic chips.

Another promising approach involves using hybrid integration of SOI nanowires, which usually have a 'slot' cross-section, with nonlinear organic polymers[53,54]. This approach has the advantage of exploiting the ability of the SOI platform to realize extremely efficient mode confinement, while simultaneously forcing a high proportion of the mode field into the polymer-filled slot, thus taking advantage of the high nonlinearity and the high FOM of the polymer.

This review focuses on new platforms $^{55-59}$  recently introduced for nonlinear optics that have achieved considerable success and that also offer CMOS compatibility. They are based on silicon nitride  $(\mathrm{Si}_3\mathrm{N}_4)$  and high-index doped silica (trade-named Hydex). Originally developed for linear optics $^{60-62}$ , these platforms are particularly promising because of their low linear loss, relatively large nonlinearities compared to those of typical fibres and, most significantly, their negligible nonlinear loss at telecommunication wavelengths $^{63}$ . In addition, their high-quality CMOS-compatible fabrication processes, high material stability and the ability to engineer dispersion $^{57}$  make these platforms highly attractive.

Indeed, significant progress has been made within a short time with respect to their nonlinear performance — particularly in the context of optical frequency comb generation in microresonators[64-71]. This field has proliferated after the demonstration of optical frequency combs in  $\mathrm{SiN}^{57}$  and Hydex[58] in 2010. Extremely wideband frequency combs[64-66], sub-100-GHz combs[67], line-by-line arbitrary optical waveform generation[68], ultrashort-pulse generation[15,70] and dual-frequency combs[71] have been reported. In addition, optical

frequency comb harmonic generation $^{72}$  has been observed. These breakthroughs have not been possible in SOI at telecommunication wavelengths because of its low FOM.

Here, we review the substantial progress made towards nonlinear optical applications of these CMOS-compatible platforms and briefly discuss the newly emerging promising platform of amorphous silicon. This review is organized according to application, beginning with basic nonlinear optics including four-wave mixing (FWM) and parametric gain, then considering applications to on-chip optical sources (for example, frequency combs and optical parametric oscillators) and finishing with applications to optical pulse measurement. The high performance, reliability and manufacturability of all these platforms combined with their intrinsic compatibility with electronic-chip manufacturing (CMOS) has raised the prospect of achieving practical platforms for future low-cost nonlinear all-optical photonic integrated circuits.

# Nonlinear optics in nanowires and waveguides

$\mathrm{Si}_3\mathrm{N}_4$  nanowires. Silicon nitride  $(\mathrm{Si}_3\mathrm{N}_4)$ , a CMOS-compatible material well known to the computer chip industry as a dielectric insulator, has been used for some time as a platform for linear integrated optics[60]. However, it has only recently been proposed as a platform for nonlinear optics[55]. Historically, tensile film stress has made it difficult to grow low-loss layers thicker than  $250~\mathrm{nm}$  for SiN optical devices. Achieving such thick layers is critical for nonlinear optics because both high mode confinement and dispersion engineering for phase matching[57] are needed. Thick  $(>500~\mathrm{nm})$  low-loss SiN layers have recently been grown (Fig. 1) by plasma-enhanced chemical vapour deposition[55] and low-pressure chemical vapour deposition[57]. The latter approach employed a thermal cycling process that resulted in very thick  $(700~\mathrm{nm})$  films from which nanowires with a very low propagation loss of  $0.4\mathrm{dBcm}^{-1}$  could be produced.

The first nonlinear optical study of SiN waveguides was reported in  $2008^{55}$  (Fig. 1a); it showed nonlinear shifting of the resonances in 700-nm-thick SiN ring resonators obtained with a continuous-wave optical pump power of  $200\mathrm{mW}$ . Time-resolved measurements enabled the thermal and Kerr contributions to be separated, resulting in an  $n_2$  that was a factor of ten greater than that of silica, which is consistent with Miller's rule[73]. This value has been validated in subsequent studies of nonlinear optics in SiN nanowires and resonators.

Parametric gain in SiN was first demonstrated in low-loss nanowires by centring the pump for the FWM process in the anomalous group-velocity dispersion (GVD) regime near the zero-GVD point[57]. This allowed for broad-bandwidth phase matching, and hence signal amplification, over a wide range of wavelengths. A net gain was achieved in long  $(6\mathrm{cm})$  SiN waveguides with a nonlinear parameter  $\gamma$  of  $1,200\mathrm{W}^{-1}\mathrm{km}^{-1}$  and a zero-GVD point near  $1,560~\mathrm{nm}$ . An on/off signal gain as high as  $3.6\mathrm{dB}$  was observed over a  $150\mathrm{-nm}$  bandwidth; this represents a net parametric amplification because the total propagation loss through the waveguides was  $3\mathrm{dB}$ .

Hydex waveguides. Hydex was developed $^{62}$  as a low-loss CMOS-compatible optical platform primarily for the realization of advanced linear filters. Its refractive-index range of  $n = 1.5$  to 1.9 is slightly lower than that of SiN, being comparable to that of SiON, and so a buried waveguide geometry is typically used rather than nanowires. Nonetheless, the core-cladding contrast of  $17\%$  still allows a relatively tight bend radius of  $20~{\mu\mathrm{m}}$ . The proprietary composition of Hydex reduces the need for high-temperature annealing by mitigating the effect of N-H bonds — the main source of absorption loss in the telecommunication band. This means that as-grown films intrinsically have low loss, making the growth process more compatible with CMOS processes.

![](images/38988c228a7e03496308a3e4c9e0a660c4ecb14d24d641643456f11ced1a946f.jpg)  
a

![](images/d26bcc39adaecd40c4612d1a8121ab514aef0daba7d6e6475744fe21fe9aa384.jpg)  
b

![](images/5f478580f148c302d99a21a3be6408ecfd38e521eccc3146d4cbcaf21f63e251.jpg)  
C

![](images/6375423aa6757f82a6b0ec57267b68a93b508ab56991f1b25763effff6855bce.jpg)  
d  
Figure 2 | Integrated optical-parametric-oscillator multiple-wavelength sources in Hydex and SiN ring resonators. a, Hydex four-port microring resonator $^{58}$  (fibre pigtails not shown) with a Q-factor of  $1.2 \times 10^{6}$  and a diameter of  $270~\mu \mathrm{m}$ . b, Output spectrum of an Hydex hyper-parametric oscillator for a pump power of  $101\mathrm{mW}$  injected on resonance at  $1,544.15\mathrm{nm}$  (transverse magnetic polarization) $^{58}$ . c, SEM image of a SiN microring resonator $^{57}$  ( $58~{\mu\mathrm{m}}$  radius,  $Q = 500,000$ ,  $\mathrm{FSR} = 403\mathrm{GHz}$ ) coupled to a bus waveguide, with a cross-sectional height of  $711\mathrm{nm}$ , a base width of  $1,700\mathrm{nm}$  and a sidewall angle of  $20^{\circ}$ , giving anomalous GVD in the C-band and a zero-GVD point at  $1,610\mathrm{nm}$ . d, Output spectrum of a  $58-\mu \mathrm{m}$ -radius SiN ring-resonator optical parametric oscillator with a single pump wavelength tuned to resonance at  $1,557.8\mathrm{nm}$ . It shows numerous narrow linewidths at precisely defined wavelengths $^{57}$ . The 87 generated wavelengths were equally spaced in frequency, with a FSR of  $3.2\mathrm{nm}$ .

The success of the Hydex platform in nonlinear optics can be primarily attributed to its extraordinarily low losses — both linear and nonlinear. Linear propagation losses as low as  $5 - 7\mathrm{dBm}^{-1}$  have been achieved, allowing for the use of extremely long waveguide spirals[14,63]. Figure 1b shows a schematic of a 45-cm-long spiral waveguide contained in a square area of  $2.5\mathrm{mm}\times 2.5\mathrm{mm}$  and pigtailed to a single-mode fibre via low-loss on-chip beam expanders[14]. It also shows a scanning electron microscope (SEM) image of its cross-section before cladding deposition. The films were fabricated using CMOS-compatible processes that yielded an exceptionally low sidewall roughness in the core layer.

For Hydex, self-phase modulation experiments $^{63}$  yielded a Kerr nonlinearity of  $n_2 = 1.15 \times 10^{-19} \mathrm{~m}^2 \mathrm{W}^{-1}$ , which is approximately 4.6 times greater than that of silica and roughly half that of SiN, with a nonlinearity parameter  $\gamma$  of  $\sim 233 \mathrm{~W}^{-1} \mathrm{~km}^{-1}$  ( $\sim 200$  times that of standard single-mode telecommunication fibres). Like SiN, this enhancement in  $n_2$  is in agreement with Miller's rule $^{73}$ . This implies that the enhancement in  $n_2$  arises solely from the increase in the linear refractive index, and not from the proprietary aspect of the material composition.

Although self-phase modulation measurements are not overly dependent on dispersion when the waveguide length is short compared with the dispersion length, proper dispersion is critical for efficient, broad-bandwidth FWM, including parametric gain[74,75].

Hydex waveguides have been engineered to yield anomalous dispersion over most of the C-band with the zero-GVD points being  $1,600\mathrm{nm}$  for transverse electric polarization and  $1,560\mathrm{nm}$  for transverse magnetic polarization[76]. This resulted in a large FWM wavelength tuning range with an efficient parametric gain of  $+15\mathrm{dB}$  and a signal-to-idler conversion efficiency of  $+16.5\mathrm{dB}$  (ref. 74).

Finally, we note that the broad use of the description 'CMOS compatible' in this context is intended to reflect a general compatibility in terms of growth temperatures  $(< 400^{\circ}\mathrm{C})$  and materials used in the CMOS process (for example, silicon nitride, Hydex and silicon oxynitride). It does not address the complexities and challenges of integrating optical and electronic devices with substantially different size scales; nor does it address the challenges of adapting CMOS production lines for optical device fabrication. Both these issues have been discussed at length[21,22]. A central problem in terms of integrating waveguides and nanowires with electronic components are the relatively large thicknesses of both the core and the cladding films. In this regard, the higher refractive-index contrast of SiN (about 0.5) compared to Hydex (about 0.3) is a significant advantage. Both glasses, however, require considerably thicker core and cladding layers than SOI — this is probably a key area in which SOI outperforms these platforms. Nonetheless, the concept of CMOS compatibility presented here, which these new platforms satisfy, is a powerful one that will go a long way towards enabling the

broad application of CMOS techniques and manufacturing infrastructure to nonlinear photonic chips.

# Microresonator-based frequency combs

The area where these platforms have arguably had the greatest impact is in integrated optical parametric oscillators based on ring resonators. These devices have significant potential for many applications, including spectroscopy and metrology[69,77,78], as well as the ability to provide an on-chip link between the radiofrequency and optical domains. Here, we do not comprehensively review the field of microcavity-based frequency combs as this has recently been done[69]; instead, we highlight the strengths and versatility of these CMOS-compatible platforms in producing frequency combs.

Microcavities effectively enhance nonlinear optical processes, particularly FWM, which involves continuous-wave pump, signal and idler beams with frequencies  $(\omega_{\mathrm{pump}},\omega_{\mathrm{signal}}$  and  $\omega_{\mathrm{idler}}$  respectively) related by energy conservation:  $\omega_{\mathrm{idler}} = 2\omega_{\mathrm{pump}} - \omega_{\mathrm{signal}}$ . This process can occur either classically (with a separate input signal at  $\omega_{\mathrm{signal}}$ ) or spontaneously (without one); the former is the basis for many all-optical signal-processing functionalities. Very-low-power operation was first demonstrated in silica and single-crystal CaF and MgF microtoroids and spheres with  $Q$ -factors ranging from  $10^{7}$  to  $10^{10}$  (refs 69, 77 and 78). Achieving phase matching of the propagation constants for three interacting waves is essential for efficient FWM; for microcavities, this is equivalent to having near-equal resonance spacings or a constant free spectral range (FSR) with due allowance for the Kerr-induced resonance shifts[57]. This results in the pump, signal and idler waves all being in resonance — a triple resonance that greatly reduces the power required for the round-trip parametric gain to exceed the loss, which is needed to produce oscillations. Phase matching, achieved by obtaining low and anomalous waveguide dispersion, can be realised by suitably designing the waveguide cross-section. Once oscillation has been achieved by pure spontaneous (degenerate) FWM (with only a pump present), 'cascaded' FWM among different cavity modes takes over, resulting in the generation of a frequency comb with precisely spaced modes in the frequency domain. However, the field enhancement in the cavity that lowers the oscillation threshold, also enhances the nonlinear losses (for all fields, in the case of phase matching). It is primarily for this reason that oscillation has not been achieved in silicon ring resonators in the telecommunication band, where the FOM is much less than unity.

As a prelude to achieving parametric oscillation in ring resonators, low-power continuous-wave nonlinear optics (FWM) was demonstrated for moderate-  $Q$ -factor (65,000) Hydex ring resonators using only a few milliwatts of continuous-wave pump power[59]. This yielded an idler that was almost exactly on resonance, indicating that the dispersion was indeed negligible. Although the  $\gamma$  factor was much lower than that for SOI ring resonators[79], the negligible nonlinear absorption allows the use of higher pump powers  $(+24~\mathrm{dBm})$ , which are typically used for high-bit-rate all-optical signal processing[80-82].

In early 2010, optical parametric oscillators were simultaneously reported in  $\mathrm{SiN}^{57}$  and Hydex $^{58}$  CMOS-compatible integration platforms with ring resonators having much lower  $Q$ -factors than previous microcavity oscillators. Hence, these devices were much less sensitive to environmental perturbations and did not require delicate tapered fibre coupling.

Figure 2a shows a Hydex four-port microring resonator that has a  $Q$ -factor of  $1.2 \times 10^{6}$ . The optical frequency comb generated by this Hydex device[58] exhibited a very wide spacing of almost  $60~\mathrm{nm}$  when pumped at  $1,544.15~\mathrm{nm}$  in the anomalous GVD regime (Fig. 2b). A plot of the output power against pump power shows a significantly high single-line differential slope efficiency above a threshold of  $7.4\%$ , with a maximum power of  $9\mathrm{mW}$  achieved in all oscillating modes out of both ports — this represents a remarkable absolute

total conversion efficiency of  $9\%$ . When pumped at a wavelength slightly closer to the zero-GVD wavelength (but still in the anomalous regime), the device oscillated with a significantly different spacing of  $28.15~\mathrm{nm}$ . These observations are consistent with a parametric gain based on a combination of FWM and the parametric, or modulational instability, gain described above, where the spacing depends on the waveguide dispersion characteristics and agrees well with calculations. This illustrates the degree of freedom achievable in varying the frequency comb spacing chiefly through dispersion engineering, so that the nonlinear response is not restricted by the FSR of the resonator itself. The trade-off is that modulational-instability-generated combs can themselves further seed subcombs that are poorly related in terms of coherence to the original comb, limiting the degree to which mode locking or ultrashort pulse generation can be achieved[65,68] (see next section).

Figure 2c shows a two-port SiN microring resonator with a  $58 - \mu \mathrm{m}$  -radius resonator (a Q-factor of 500,000 and an FSR of  $403\mathrm{GHz}$ ) with dimensions designed to yield anomalous GVD in the C-band with a zero-GVD point at  $1,610~\mathrm{nm}$ . Optical parametric oscillation was first realized in  $\mathrm{SiN}^{57}$  by resonantly pumping the rings with continuous-wave light near  $1,550~\mathrm{nm}$  using a soft 'thermal-lock' process in which cavity heating is counteracted by diffusive cooling. Oscillation of multiple lines over a very broad  $(>200\mathrm{nm})$  wavelength range was achieved (Fig. 2d) at a pump threshold of  $50\mathrm{mW}$ . A total of 87 new frequencies were generated between  $1,450~\mathrm{nm}$  and  $1,750~\mathrm{nm}$ , corresponding to wavelengths covering the S, C, L and U communication bands. Several designs were employed with different ring radii or FSR. A smaller ring with a Q-factor of 100,000 generated oscillation in 20 resonator modes with terahertz mode spacing when pumped with a modest input power of  $150\mathrm{mW}$ . The observation that these devices oscillated with a frequency spacing equal to the FSR of the resonator (in contrast with the Hydex device that oscillated with a frequency spacing given by the modulational-instability gain peak) can perhaps be better understood in the light of recent studies (see discussion below) on comb formation and dynamics; it is a result of the subtle interplay among the waveguide dispersion, the precise pump power and detuning of the pump wavelength.

# Advanced frequency combs

After these initial demonstrations of multiple-wavelength oscillation, significant progress has been made in the generation of advanced combs, including both very-wide-bandwidth octave-spanning combs[66] and very low (sub-100 GHz) FSR spacing combs[67].

The development of microresonator-based frequency combs with a FSR significantly lower than  $100\mathrm{GHz}$  is critical for providing a direct link between the optical and electrical domains in order to produce highly stable microwave signals[67,83-85] detectable with photodiodes. The challenge is that, because simple ring geometries with sub-100-GHz FSR spacings do not fit on typical single electron-beam lithography fields, novel ring geometries such as spirals need to be employed (Fig. 3a-c). Figure 3 shows spiral ring resonators with unique geometries for different FSRs below  $100\mathrm{GHz}$  (ref. 67), all having a constant semicircular coupling region to enable critical coupling between the bus and the resonator, independent of the path length. Bends in the resonators had radii greater than  $100\mu \mathrm{m}$  to ensure that bend-induced dispersion was negligible — a critical requirement for proper operation of the frequency comb. The experimental spectra for 80, 40 and  $20\mathrm{GHz}$  combs are respectively shown in Fig. 3d-f; typically, a pump power of about  $2\mathrm{W}$  is required to fill the entire comb span.

Octave-spanning frequency combs are of great interest for spectroscopy, precision frequency metrology and optical clocks and they are highly desirable for comb self-stabilization using  $f$ -to-2f interferometry for precision measurement of absolute optical frequencies[85-87]. Figure 3g shows an optical frequency comb in a SiN

![](images/8cefde8c501e053f88bf304e48990426418aa7486c19b911f0093bd73c282545.jpg)

![](images/31215ecd73ed79ab9bbbb499834365cdf2db4ed42faaec423247a7d0871a3890.jpg)

![](images/77ae8f5bf173c4b614021bee88d5a9b27dca109722ddd2697824c5c13715eeed.jpg)

![](images/a6e34adbc40d43c2724a7c1fe22cc1ae2181b13dcdd2b83e6eb03fe96d66866b.jpg)

![](images/6e57dcab18494aef83a7c52cbf36ef43a65dee3d74845d01739e165ce4770d67.jpg)

![](images/c646444ac145355fb92f3ea3316ddc5986efd20cd8e7fcc627898f1d4b5de385.jpg)  
Figure 3 | Advanced frequency combs in SiN ring resonators. a-f, Sub-100-GHz-spacing SiN ring resonators<sup>67</sup>. Micrographs of 80 GHz (a), 40 GHz (b) and 20 GHz (c) FSR resonators. The nanowire cross-sections were 725 nm by 1,650 nm, with a minimum microring bend diameter of 200 μm and a loaded Q of 100,000. d-f, Output spectra are 300 nm wide for the 80 GHz and 40 GHz FSR rings and 200 nm wide for the 20-GHz FSR ring. A 2-nm section of each comb is shown in the inset of each figure to illustrate the spacing of the comb lines. g, Optical spectrum of octave-spanning parametric frequency comb generated in a SiN ring resonator<sup>66</sup>. h, Dispersion simulations for the fundamental transverse electric mode of a SiN waveguide with a height of 730 nm and widths of 1,200, 1,650 and 2,000 nm, respectively. The dashed curve shows the dispersion for bulk silicon nitride<sup>66</sup>. Figure reproduced with permission from: a-f, ref. 67, © 2012 OSA; g-h, ref. 66, © 2011 OSA.

ring resonator spanning more than an octave $^{66}$  from  $1,170~\mathrm{nm}$  to  $2,350~\mathrm{nm}$ , which corresponds to  $128~\mathrm{THz}$ . This is achieved by employing suitable dispersion engineering and high pump powers, detuned slightly from a cavity resonance, of up to  $400~\mathrm{mW}$  (inside the waveguide). Figure 3h shows the simulated dispersion for nanowires with widths of  $1,200~\mathrm{nm}$ ,  $1,650~\mathrm{nm}$  and  $2,000~\mathrm{nm}$ . It indicates that large anomalous-GVD bandwidths spanning nearly an octave are possible with appropriate design. These results represent a significant step towards a stabilized, robust integrated frequency comb source that can be scaled to other wavelengths.

# Supercontinuum generation

Very broadband continuous spectra can be generated by injecting ultrashort mode-locked pulse trains into suitably designed waveguides. These supercontinuum spectra are of interest for similar reasons to octave-spanning frequency combs. Wide-bandwidth supercontinuum generation (SCG) has been demonstrated in microstructured fibres[88], chalcogenide glass waveguides[89], periodically poled lithium niobate[90] and silicon at wavelengths above  $2\mu \mathrm{m}$  (ref. 91). Hydex and SiN offer the advantages of much lower linear and nonlinear losses and transparency well into the visible region. It is interesting to compare the broadband frequency

combs with SCG in Hydex waveguides $^{92}$ , where a spectral width of over  $350~\mathrm{nm}$  was achieved (limited by the experimental measurement capability), and in 1,100-nm-wide SiN nanowires $^{93}$ . When pumped at  $1,335~\mathrm{nm}$  in this platform, SCG results in a spectrum spanning 1.6 octaves (from  $665~\mathrm{nm}$  to  $2,025~\mathrm{nm}$ ). We note that the SiN results represent the broadest recorded SCG to date in a CMOS-compatible chip. Remarkably, both of these results were enabled by a high effective nonlinearity, negligible TPA and, most significantly, very flexible dispersion engineering. SCG is significantly enhanced if the pulse is launched near a zero-GVD point or in the anomalous GVD regime $^{93-96}$ . The former minimizes temporal pulse broadening, thereby preserving high peak powers and thus maintaining a strong nonlinear interaction, whereas the latter enables soliton propagation whose dynamics can contribute to spectral broadening $^{97}$ . The more flexible dispersion engineering in SiN than in Hydex is partly related to its higher available core/ cladding index contrast and it is probably one of its most significant advantages.

# Frequency comb dynamics and coherence

As with conventional mode-locked lasers, parametric frequency combs can also potentially serve as sources of ultrashort laser

![](images/15ea45c01d5774abeb64543debcea3ee749d46ecde0563cc121bacac40dee404.jpg)

![](images/0393485540858b690def3978813dffe34a78c38e1a88fd4301de738dba4a9229.jpg)

![](images/9215131588320200fedaae4bdc2ff1e0008e5f6eef2c807ba73c1912368fc121.jpg)

![](images/bdcfd040d081dd3ffb6bdec9826adfa5dc979b6f3d2b3961cc59e4438e3d5af3.jpg)

![](images/b0305edecd818d214e3e5d7576a22a3257d5df46ba985e868deb7f68ce028798.jpg)  
Figure 4 | Coherence and frequency comb formation dynamics. a-d, Frequency comb coherence properties from ref. 68. The output spectrum generated by a high-Q silicon nitride microring shows the ability of type-I Kerr combs to perform pulse compression (a). Spectrum of the combs after processing with a pulse shaper, together with the phase applied to the liquid-crystal modulator pixels required to achieve optimum SHG signals (a,b). Autocorrelation traces (c,d) corresponding to  $(\mathbf{a},\mathbf{b})^{68}$ . The red lines depict the compressed pulses after applying a phase correction, the blue lines are uncompressed pulses and the black lines are calculated from the spectra shown in a and b by assuming a flat spectral phase. The contrast ratios of the autocorrelations measured after phase compensation are 14:1 (c) and 12:1 (d). Light grey traces show the range of the simulated autocorrelation traces. e-f, Studies of coherence evolution in SiN microring resonators from ref. 65 showing the optical spectra for a transition from a low-phase-noise Kerr comb: (e) state 1 to a high coherence output, (f) state 2 for the two microresonator comb states (pump power: 6 W). State 2 evolves from state 1 as the detuning of the pump laser is reduced. A transition is observed from multiple subcombs to a single subcomb over the bandwidth of the Kerr comb reconstruction. In state 1, all subcombs have the same mode spacing but different offsets that differ by a constant value of 66 MHz. In the transition from state 1 to state 2, the amplitude noise peak resulting from the beating between overlapping offset subcombs disappears[65].

![](images/9422b3eefb797c1ff5cefe8c3bf63d6ba86806cd41d90d87af6c7ceeea657908.jpg)

pulses from the visible to mid-infrared region at repetition rates in the gigahertz to terahertz regimes. The past two years have seen significant breakthroughs in understanding the dynamics and coherence behaviour associated with frequency comb formation[65-70]. These studies have revealed complex and distinct paths to comb formation, which can result in widely varying degrees of coherence, wavelength spacing and radiofrequency stability of these sources. This field has recently been highlighted by the achievement of an ultrastable, ultrashort optical pulse source via mode locking based on an integrated microcavity[15]. Understanding and harnessing the coherence properties of these monolithic frequency comb sources is crucial for exploiting their full potential in

the temporal domain, as well as for bringing this promising technology to practical fruition.

The first investigation of the coherence properties of on-chip oscillators[68] focused on phase tuning of the comb via programmable optical pulse shaping. This 'line-by-line' pulse shaping of micro-resonator frequency combs was enabled by the relatively large mode spacings and represented a significant development in the field of optical arbitrary waveform generation[83-85]. In this approach, transform-limited pulses can be realized for any spectral phase signature of coherent combs by appropriately compensating the relative phase of the different comb lines (Fig. 4a-d). These time-domain experiments revealed different pathways to comb formation in terms of

![](images/93b12212bc82f547a492893c9ffd27145e74e85db1aa5c74ef1af884b869c322.jpg)  
Figure 5 | Microresonator-based mode-locked fibre loop laser. a, Experimental configuration<sup>15</sup> for a fibre-loop mode-locked laser based on filter-driven FWM in a microring resonator, where the resonator performs both linear filtering and nonlinear interaction. b, d, f Results for the unstable operation regime with a long main cavity length ( $L = 33\mathrm{m}$ ,  $\mathrm{FSR} = 6.0\mathrm{MHz}$ )<sup>15</sup>, c, e, g Results for the stable operation regime for a short cavity main length ( $L = 3\mathrm{m}$ ,  $\mathrm{FSR} = 68.5\mathrm{MHz}$ ) laser. Stable oscillation was obtained by adjusting the phase of the cavity modes for the short main cavity length laser relative to the ring resonator modes via a free space delay line<sup>15</sup>. Experimental optical temporal waveforms measured<sup>15</sup> by optical autocorrelation for unstable (b) and stable (c) operation. Autocorrelation plots show theoretical calculations (green lines) obtained by starting from the experimental optical spectra for a fully coherent and transform-limited system and calculated by considering each line in the experimental optical spectra as being perfectly monochromatic and in phase with the others. This yielded an output pulse with a full width at half maximum of 730 fs at the highest excitation power. The measured autocorrelation for the long (unstable) cavity laser (b) exhibits a background that is 50 times greater than that of the calculated autocorrelation. In contrast, the calculated autocorrelation trace for the short-cavity (stable) laser (c) perfectly matches the measured trace, suggesting stable mode locking, and corresponding to a transform-limited pulse width of 2.3 ps (full width at half maximum) with a peak-to-background ratio of 5:1. Radiofrequency temporal output for the unstable (d) and stable (e) configurations. Radiofrequency spectra for the unstable (f) and stable (g) configurations<sup>15</sup>.

![](images/1f06fda66d7c4a3d3dccafb99339de60d95da84299755535539a8fc7a183b593.jpg)

![](images/c6c8b1d19c31c95b386a4dc10a2fca2b29ed1984f16e85dc6dabf53be0bddf8f.jpg)

![](images/ba95328a0d0a0aabd6c3be0d63bdc71ff9fb29429a134d0020bf8ae09b41a5d9.jpg)

![](images/fc30d73ec7c01b1c097d6f3016fdaa0fb938fbaac4dbafbdd834b9c6bbf4d89e.jpg)

![](images/d1eb477ae7df9d2e70ef2516825c78ebd6dfebd7b3348d157c50d744fcf152da.jpg)

![](images/c83bdac4f0f081d2341daade2a18b8f1ba9c60c7d00686c25fd127990e04cd8b.jpg)

phase coherence properties, where the ability to effectively model lock the combs varies significantly with many factors such as the pump conditions and the waveguide dispersion.

More recent studies of the dynamics of comb formation[65] (Fig. 4e-f) have shown that the initial oscillation often begins with frequency spacings near the parametric gain peak, which can vary widely, from as little as the FSR spacing itself to as wide as  $100\mathrm{nm}$  or more. Cascaded FWM then replicates a comb with this initial spacing. More complex dynamics arise when these comb lines seed their own mini-comb bands based on the local dispersion and pumping conditions, often with a spacing at or near the cavity FSR in that wavelength region. Although these 'subcombs' maintain coherence within themselves, they are not coherently related to the subcombs generated by other lines of the initial, more widely spaced, comb, resulting in a limited overall coherence. One approach for obtaining a high overall coherence is to achieve initial comb oscillation at the FSR. Figure 4 shows the output of a ring resonator under different pumping conditions[65]; it reveals the transition from an incoherent state with well-separated frequency subcombs to a coherent state characterized by a much improved ability to lock the modes and thus to produce optical pulses, thus resulting in much lower radiofrequency noise.

Further studies $^{70}$  of the optical and radiofrequency properties of parametric frequency combs in SiN microresonators show a transition to a mode-locked state where ultrashort pulse generation is possible. From a 25-nm filtered section of the 300-nm comb spectrum, sub-200-fs pulses were observed with calculations indicating that the pulse generation process is consistent with soliton mode locking. This is consistent with very recent work involving comb generation in  $\mathrm{MgF}_2$  microresonators $^{98}$  and could be explained by the formation of temporal cavity solitons $^{15,99}$ , where nonlinearity and a coherent driving beam compensate contributions from both dispersion and loss.

# Ultrashort pulse sources

Stable mode locking of a microresonator frequency comb has recently been demonstrated (Fig. 5a) $^{15,71}$  by embedding the resonator in an active fibre loop, where the microresonator is used as both a linear filter and a nonlinear element. This scheme, termed filter-driven FWM, is an advance inspired by dissipative  $\mathrm{FWM}^{100-102}$  where the nonlinear interaction occurs in-fibre and is then 'filtered' separately by a linear Fabry-Pérot filter. This new approach is more efficient and so allows for substantially reduced main cavity lengths that lead in turn to highly stable operation — something that has so far eluded dissipative FWM lasers. In dissipative FWM

a  
![](images/d44969e589135462ceb96dbbb5a410808fc181b11a9e41beb48615402e517bb5.jpg)  
(SPIDER). a, X-SPIIDER based on FWM in a Hydex spiral waveguide. The pulse under test (PUT) is split in two replicas and nonlinearly mixed with a highly chirped pump inside the chip (extracted from the same laser source in these experiments). The resulting output is captured by a spectrometer and numerically processed by a suitable algorithm to extract the complete information (amplitude and phase) of the incident pulse<sup>14</sup>. b, Retrieved phase and amplitude profiles for pulses with TBPs of 5 (ref. 14). c, Retrieved phase and amplitude profiles for pulses with TBPs of 100 (ref. 14). In (b) and (c), the left-hand plots were obtained by the X-SPIIDER device using a standard algorithm, whereas the centre plots were obtained using a new algorithm<sup>14,116</sup> suitable for large-TBP pulses. The plots on the right are the experimentally measured FROG measurements based on second-harmonic generation.

![](images/f4870033faea192795d121ee2b4a2deb4c86f2326bc55437c5fc9fe3019f12c2.jpg)  
b

![](images/3587b77dfabf19dfd4ec02fc1daba1604b94314a30b392154c3c199e48130405.jpg)  
Figure 6 | Phase and amplitude measurement of ultrafast optical pulses using spectral phase interferometry for direct electric-field reconstruction  
c

lasers, the main cavity mode spacing is much finer than that of the microcavity, allowing many cavity modes to oscillate within the filter resonance; this is an unfavourable condition as it gives rise to 'supermode instability'. Filter-driven FWM allows the main cavity length to be substantially reduced so that only a very small number of cavity modes exist within each microresonator resonance, allowing for the possibility of true single-mode operation. Filter-driven FWM has achieved highly stable operation at high repetition rates over a large range of operating conditions and it is robust to external (that is, thermal) perturbations. It also yields much narrower linewidths than ultrashort cavity lasers because it has a much lower Schawlow-Townes phase noise limit $^{103,104}$ .

Figure 5a shows the experimental configuration of the loop laser. It compares the time-resolved optical waveforms measured by autocorrelation (Fig. 5b,c), the radiofrequency temporal output (Fig. 5d,e), the radiofrequency spectra (Fig. 5f,g) and the optical spectra (insets in Fig. 5d,e) of short- and long-cavity lasers. It clearly reveals that the short-cavity laser has a highly stable radiofrequency spectrum. In contrast, the long-cavity length laser not only exhibits large, long-timescale instabilities in the radiofrequency output, but it is also unstable on a short timescale as reflected by the fact that the optical autocorrelation traces show a very limited contrast ratio — a hallmark of unstable oscillation[65,68]. Recently, stable mode-locked laser operation with two modes oscillating within each ring cavity has been demonstrated[71]. It produced a highly pure radiofrequency tone over the mode-locked train, enabling high-resolution radiofrequency spectral measurement of the optical linewidth, which displayed a remarkably narrow width of about  $10\mathrm{kHz}$ .

# Ultrafast phase-sensitive pulse measurements

Coherent optical communications $^{18,19}$  have created a compelling need for ultrafast phase-sensitive measurement techniques

operating at milliwatt peak-power levels. Ultrafast optical signal measurements have been achieved using time-lens temporal imaging on a silicon chip $^{105,106}$  and waveguide-based frequency-resolved optical gating (FROG) $^{107}$ , but these are either phase insensitive or require waveguide-based tunable delay lines, which are difficult to realize. Recently, a device capable of both amplitude and phase characterization of ultrafast optical pulses has been reported $^{14}$ . It employs a novel variation of spectral phase interferometry for direct electric-field reconstruction (SPIDER) $^{108-115}$  based on FWM in Hydex waveguides. Here, pulse reconstruction was performed with the aid of a synchronized incoherently related clock pulse.

SPIDER approaches are ultrafast and single shot and use a simple, direct and robust phase-retrieval procedure. However, they have traditionally employed either three-wave mixing or linear electro-optic modulation; both of these require a high second-order nonlinearity, which CMOS-compatible platforms lack. Furthermore, typical SPIDER methods work best with optical pulses shorter than 100 fs (ref. 114) (small time-bandwidth products (TBPs)) and peak powers of over  $10\mathrm{kW}$ , and hence they are not ideally suited to telecommunications. The device reported in ref. 14 measured pulses with peak powers below  $100\mathrm{mW}$ , with a frequency bandwidth greater than  $1\mathrm{THz}$  and on pulses as wide as  $100\mathrm{ps}$ , yielding a record TBP of over 100 (ref. 115). The technique employed in this device is commonly referred to as X-SPIDER.

Figure 6a shows a schematic of the device. The pulse under test is split into two replicas and nonlinearly mixed with a highly chirped pump inside the chip. The resulting output is then captured by a spectrometer and numerically processed to extract the complete information (amplitude and phase) of the incident pulse. Figure 6b-c compares the results of the X-SPIDER device obtained using both a standard algorithm and an extended (Fresnel) phase-recovery extraction algorithm[14,116] designed for pulses with a large time TBP with results obtained for the same pulses from FROG

Table 1 | Nonlinear parameters for CMOS-compatible optical platforms  

<table><tr><td></td><td>a-Si127</td><td>c-Si2,47</td><td>SiN55-57</td><td>Hydex63,76</td></tr><tr><td>n2(× n of fused silica1)</td><td>700</td><td>175</td><td>10</td><td>5</td></tr><tr><td>γ (W-1m-1)</td><td>1,200</td><td>300</td><td>1.4</td><td>0.25</td></tr><tr><td>βTPA (cm GW-1)</td><td>0.25</td><td>0.9</td><td>Negligible2</td><td>Negligible3</td></tr><tr><td>FOM</td><td>5</td><td>0.3</td><td>&gt;&gt;1</td><td>&gt;&gt;1</td></tr></table>

${}^{1}{n}_{2}$  for fused silica  $= {2.6} \times  {10}^{-{20}}{\mathrm{\;m}}^{2}{\mathrm{\;W}}^{-1}$  (ref. 1)  
2No nonlinear absorption has been observed in SiN nanowires.  
${}^{3}$  No nonlinear absorption has been observed in Hydex waveguides up to intensities of  ${25}\mathrm{{GW}}{\mathrm{{cm}}}^{-2}$  (ref. 63).

measurements based on second-harmonic generation. As expected, for low TBP pulses (short-pulse regime), the SPIDER device yielded identical results when processed with both algorithms, and they also agreed with the FROG spectrogram. For large TBP pulses (highly chirped, large pulsewidths), the X-SPIDER results obtained with the new algorithm agreed very well with the FROG trace, whereas the results obtained using the standard phase-recovery algorithm were unable to reproduce the pulse accurately.

# Future challenges and opportunities

The success of these platforms for nonlinear optics in the telecommunication band has been due to a favourable combination of very low linear loss, negligible TPA, a moderately high nonlinearity, the ability to engineer dispersion, their high-quality growth and fabrication processes, and their excellent material reliability. However, the ideal platform would have a much larger nonlinearity — comparable to, or even larger than, that of silicon — while simultaneously having a much larger FOM than silicon.

Table 1 compares the nonlinear parameters of key CMOS-compatible platforms including crystalline and amorphous silicon, SiN, Hydex and fused silica. It is remarkable that SiN and Hydex perform so well given that their  $n_2$  is typically only five to ten times larger than that of fused silica and that their  $\gamma$  factors range from 200 (SiN) to 1,000 times lower than typical values for SOI nanowires. This fact really highlights how critical low linear, and particularly nonlinear, losses are in all-optical platforms.

Amorphous silicon (a-Si), which has been studied as a nonlinear material $^{117}$  and as a platform for linear photonics for some time $^{118,119}$  has recently been proposed as an alternative to SOI for nonlinear optics in the telecommunication band $^{120}$ . Although initial measurements yielded a FOM no better than that of c-Si  $(\sim 0.5)^{120,121}$ , more recent results have shown FOMs ranging from 1 (ref. 122) to as high as 2 (refs 123,124), allowing for a very high parametric gain  $(+26~\mathrm{dB})$  over the C band $^{125}$ . A key problem for this material has been its lack of stability $^{126}$ , but very recently a-Si nanowires were demonstrated that displayed the combination of a high FOM of 5, a high  $n_2$  (3-4 times that of c-Si) and good material stability at telecommunication wavelengths $^{127}$ . A key goal of all-optical chips is to reduce both the device footprint and the operating power. The dramatic improvement in both FOM and the nonlinearity of a-Si raises the possibility of using slow-light structures $^{128,129}$  to allow devices to operate at milliwatt power levels with submillimetre lengths, and so a-Si remains an extremely promising platform for future all-optical chips.

# Conclusions

We have reviewed the recent progress in two important CMOS-compatible materials that are potential alternatives to SOI for integrated optical platforms for nonlinear optics — silicon nitride and Hydex. These new platforms have enabled the realization of devices that possess many novel all-optical functions at telecommunication wavelengths. The combination of negligible nonlinear (two-photon) absorption, low linear loss, the ability to engineer waveguide dispersion, and moderately high nonlinearities has enabled these platforms

to achieve new capabilities not possible in c-Si because of its low FOM. These platforms will probably have a significant impact on future all-optical devices, complimenting the substantial achievements already made in silicon nanophotonics. Their high performance, reliability and manufacturability, combined with intrinsic compatibility with electronic-chip manufacturing (CMOS), raises the prospect of practical platforms for future low-cost nonlinear all-optical photonic integrated circuits that offer a smaller footprint, lower energy consumption and lower cost than present solutions.

# Received 2 December 2012; accepted 21 June 2013

# References

1. Eggleton, B. J., Moss, D. J. & Radic, S. in Optical Fiber Telecommunications V: Components and Sub-systems (eds Kaminow, I. P., Li, T. & Willner, A. E.) Ch. 20, 759-828 (Academic, 2008).  
2. Leuthold, J., Koos, C. & Freude, W. Nonlinear silicon photonics. Nature Photon. 4, 535-544 (2010).  
3. Ji, H. et al. 1.28-Tb/s Demultiplexing of an OTDM DPSK data signal using a silicon waveguide. IEEE Photon. Tech. Lett. 22, 1762-1764 (2010).  
4. Galili, M. et al. Breakthrough switching speed with an all-optical chalcogenide glass chip: 640 Gbit/s demultiplexing Opt. Express 17, 2182-2187 (2009).  
5. Foster, M. A. et al. Broad-band optical parametric gain on a silicon chip. Nature 441, 960-963 (2006).  
6. Rong, H. et al. A cascaded silicon Raman laser. Nature Photon. 2, 170-174 (2008).  
7. Mathlouthi, W., Rong, H. & Paniccia, M. Characterization of efficient wavelength conversion by four-wave mixing in sub-micron silicon waveguides. Opt. Express 16, 16735-16745 (2008).  
8. Li, F. et al. All-optical XOR logic gate for 40Gb/s DPSK signals via FWM in a silicon nanowire. Opt. Express 19, 20364-20371 (2011).  
9. Salem, R. et al. Signal regeneration using low-power four-wave mixing on a silicon chip. Nature Photon. 2, 35-38 (2008).  
10. Taeed, V. G. et al. Integrated all-optical pulse regeneration in chalcogenide waveguides. Opt. Lett. 30, 2900-2902 (2005).  
11. Pelusi, M. et al. Photonic-chip-based radio-frequency spectrum analyser with terahertz bandwidth. Nature Photon. 3, 139-143 (2009).  
12. Corcoran, B. et al. Silicon nanowire based radio-frequency spectrum analyser. Opt. Express 18, 20190-20200 (2010).  
13. Foster, M. A. et al. Silicon-chip-based ultrafast optical oscilloscope. Nature 456, 81-84 (2008).  
14. Pasquazi, A. et al. Sub-picosecond phase-sensitive optical pulse characterization on a chip. Nature Photon. 5, 618-623 (2011).  
15. Peccianti, M. et al. Demonstration of a stable ultrafast laser based on a nonlinear microcavity. Nat. Commun. 3, 765 (2012).  
16. Fridman, M., Farsi, A., Okawachi, Y. & Gaeta, A. L. Demonstration of temporal cloaking. Nature 481, 62-65 (2012).  
17. Slavik, R. et al. All-optical phase and amplitude regenerator for next-generation telecommunications systems. Nature Photon. 4, 690-695 (2010).  
18. Winzer, P. Beyond 100G Ethernet. IEEE Commun. Mag. 48, 26-30 (2010).  
19. Essiambre, R., Kramer, G., Winzer, P. J., Foschini, G. J. & Goebel, B. Capacity limits of optical fiber networks. J. of Lightwave Technol. 28, 662-701 (2010).  
20. Won, R. Integrating silicon photonics. Nature Photon. 4, 498-499 (2010).  
21. Baehr-Jones, T. et al. Myths and rumours of silicon photonics. Nature Photon. 6, 206-208 (2012).  
22. Hochberg, M. & Baehr-Jones, T. Towards fabless silicon photonics. Nature Photon. 4, 492-494 (2010).  
23. Jalali, B. Nonlinear optics in the mid-infrared. Nature Photon. 4, 506-508 (2010).

24. Xia, F., Sekaric, L. & Vlasov, Y. Ultracompact optical buffers on a silicon chip. Nature Photon. 1, 65-71 (2007).  
25. Alduino, A. & Paniccia, M. Interconnects: Wiring electronics with light. Nature Photon. 1, 153-155 (2007).  
26. Selvaraja, S. K. et al. Fabrication of photonic wire and crystal circuits in silicon-on-insulator using 193-nm optical lithography. J. of Lightwave Technol. 27, 4076-4083 (2009).  
27. Dumon, P., Bogaerts, W., Baets, R., Fedeli, J.-M. & Fulbert, L. Towards foundry approach for silicon photonics: Silicon photonics platform ePIXfab. IEEE Electron. Lett. 45, 581-582 (2009).  
28. Bogaerts, W. et al. Silicon microring resonators. Las. Photon. Rev. 6, 47-73 (2012).  
29. Vlasov, Y., Green, W. M. J. & Xia, F. High-throughput silicon nanophotonic wavelength-insensitive switch for on-chip optical networks. Nature Photon. 2, 242-246 (2008).  
30. Rong, H. et al. Low-threshold continuous-wave Raman silicon laser. Nature Photon. 1, 232-237 (2007).  
31. Rong, H. et al. A continuous-wave Raman silicon laser. Nature 433, 725-728 (2005).  
32. Rong, H. et al. An all-silicon Raman laser. Nature 433, 292-294 (2005).  
33. Jalali, B., Solli, D. R. & Gupta, S. Silicon's time lens. Nature Photon. 3, 8-10 (2009).  
34. Krauss, T. F., De La Rue, R. M. & Brand, S. Two-dimensional photonic-bandgap structures operating at near-infrared wavelengths. Nature 383, 699-702 (1996).  
35. Vlasov, Y. A., Bo, X.-Z., Sturm, J. C. & Norris, D. J. On-chip natural assembly of silicon photonic bandgap crystals. Nature 414, 289-293 (2001).  
36. Vlasov, Y. A., O'Boyle, M., Hamann, H. F. & McNab S. J. Active control of slow light on a chip with photonic crystal waveguides. Nature 438, 65-69 (2005).  
37. Kuyken, B. et al. 50 dB parametric on-chip gain in silicon photonic wires. Opt. Lett. 36, 4401-4403 (2011).  
38. Liu, X., Osgood, R. M. Jr, Vlasov, Y. A. & Green, W. M. J. Mid-infrared optical parametric amplifier using silicon nanophotonic waveguides. Nature Photon. 4, 557-560 (2010).  
39. Zlatanovic, S. et al. Mid-infrared wavelength conversion in silicon waveguides using ultracompact telecom-band-derived pump source. Nature Photon. 4, 561-564 (2010).  
40. Grom, G. F. et al. Ordering and self-organization in nanocrystalline silicon. Nature 407, 358-361 (2000).  
41. Hirschman, K. D., Tsybeskov, L., Duttagupta, S. P. & Fauchet, P. M. Silicon-based visible light-emitting devices integrated into microelectronic circuits. Nature 384, 338-341 (1996).  
42. Clemmen, S. et al. Continuous wave photon pair generation in silicon-on-insulator waveguides and ring resonators. Opt. Express 18, 14107 (2010).  
43. Liang, T. K. & Tsang, H. K. Nonlinear absorption and Raman scattering in silicon-on-insulator optical waveguides. IEEE J. Selected Topics in Quant. Electron. 10, 1149-1153 (2004).  
44. Liu, A., Rong, H., Paniccia, M., Cohen, O. & Hak, D. Net optical gain in a low loss silicon-on-insulator waveguide by stimulated Raman scattering. Opt. Express 12, 4261-4268 (2004).  
45. Gholami, F. et al. Third-order nonlinearity in silicon beyond  $2350\mathrm{nm}$ . Appl. Phys. Lett. 99, 081102 (2011).  
46. Lin, Q. et al. Dispersion of silicon nonlinearities in the near infrared region. Appl. Phys. Lett. 91, 021111 (2007).  
47. Dinu, M., Quochi, F. & Garcia, H. Third-order nonlinearities in silicon at telecom wavelengths. Appl. Phys. Lett. 82, 2954-2956 (2003).  
48. Zlatanovic, S. et al. Mid-infrared wavelength conversion in silicon waveguides using ultracompact telecom-band-derived pump source. Nature Photon. 4, 561-564 (2010).  
49. Liu, X., Osgood, R. M. Jr, Vlasov, Y. A. & Green, W. M. J. Mid-infrared optical parametric amplifier using silicon nanophotonic waveguides. Nature Photon. 4, 557-560 (2010).  
50. Eggleton, B. J., Luther-Davies, B. & Richardson, K. Chalcogenide photonics. Nature Photon. 5, 141-148 (2011).  
51. Aitchison, J. S., Hutchings, D. C., Kang, J. U., Stegeman, G. I. & Villeneuve, A. The nonlinear optical properties of AlGaAs at the half band gap. IEEE J. of Quant. Electron. 33, 341-348 (1997).  
52. Dolgaleva, K., Ng, W. C., Qian, L. & Aitchison, J. S. Compact highly-nonlinear AlGaAs waveguides for efficient wavelength conversion. Optics Exp. 19, 12440-12455 (2011).  
53. Baehr-Jones, T. W. & Hochberg, M. J. Polymer silicon hybrid systems: A platform for practical nonlinear optics. J. Phys. Chem. C 112, 8085-8090 (2008).  
54. Leuthold, J. et al. Silicon organic hybrid technology — A platform for practical nonlinear optics. Proc. IEEE 97, 1304-1316 (2009).

55. Ikeda, K., Saperstein, R. E., Alic, N. & Fainman, Y. Thermal and Kerr nonlinear properties of plasma-deposited silicon nitride/silicon dioxide waveguides. Opt. Express 16, 12987-12994 (2008).  
56. Tan, D. T. H., Ikeda, K., Sun, P. C. & Fainman, Y. Group velocity dispersion and self phase modulation in silicon nitride waveguides. Appl. Phys. Lett. 96, 061101 (2010).  
57. Levy, J. S. et al. CMOS-compatible multiple-wavelength oscillator for on-chip optical interconnects. Nature Photon. 4, 37-40 (2010).  
58. Razzari, L. et al. CMOS-compatible integrated optical hyper-parametric oscillator. Nature Photon. 4, 41-45 (2010).  
59. Ferrera, M. et al. Low-power continuous-wave nonlinear optics in doped silica glass integrated waveguide structures. Nature Photon. 2, 737-740 (2008).  
60. Henry, C. H., Kazarinov, R. F., Lee, H. J., Orlowsky, K. J. & Katz, L. E. Low loss  $\mathrm{Si}_3\mathrm{N}_4\mathrm{-SiO}_2$  optical waveguides on Si. Appl. Opt. 26, 2621-2624 (1987).  
61. Daldosso, N. et al. Comparison among various  $\mathrm{Si}_3\mathrm{N}_4$  waveguide geometries grown within a CMOS fabrication pilot line. IEEE J. Lightwave Technol. 22, 1734-1740 (2004).  
62. Little, B. E. et al. Very high-order microring resonator filters for WDM applications. IEEE Photon. Technol. Lett. 16, 2263-2265 (2004).  
63. Duchesne, D. et al. Efficient self-phase modulation in low loss, high index doped silica glass integrated waveguides. Opt. Express 17, 1865-1870 (2009).  
64. Levy, J. S. et al. High-performance silicon-nitride-based multiple-wavelength source. IEEE Photon. Technol. Lett. 24, 1375-1377 (2012).  
65. Herr, T. et al. Universal formation dynamics and noise of Kerr-frequency combs in microresonators. Nature Photon. 6, 480-487 (2012).  
66. Okawachi, Y. et al. Octave-spanning frequency comb generation in a silicon nitride chip. Opt. Lett. 36, 3398-3400 (2011).  
67. Johnson, A. R. et al. Chip-based frequency combs with sub-100 GHz repetition rates. Opt. Lett. 37, 875-877 (2012).  
68. Ferdous, F. et al. Spectral line-by-line pulse shaping of on-chip microresonator frequency combs. Nature Photon. 5, 770-776 (2011).  
69. Kippenberg, T. J., Holzwarth, R. & Diddams, S. A. Microresonator-based optical frequency combs. Science 332, 555-559 (2011).  
70. Saha, K. et al. Modelocking and femtosecond pulse generation in chip-based frequency combs. Opt. Express 21, 1335-1343 (2012).  
71. Peccianti, M. et al. Dual frequency comb mode-locked laser based on an integrated nonlinear microring resonator. Opt. Express 20, 27355-27363 (2012).  
72. Levy, J. S., Foster, M. A., Gaeta, A. L. & Lipson, M. Harmonic generation in silicon nitride ring resonators. Opt. Express 19, 11415-11421 (2011).  
73. Monro, T. M. et al. Progress in microstructured optical fibers. Annu. Rev. Mater. Res. 36, 467-495 (2006).  
74. Pasquazi, A. et al. Efficient wavelength conversion and net parametric gain via four wave mixing in a high index doped silica waveguide. Opt. Express 18, 7634-7641 (2010).  
75. Lamont, M. R. et al. Net-gain from a parametric amplifier on a chalcogenide optical chip. Opt. Express 16, 20374-20381 (2008).  
76. Ferrera, M. et al. Low power four-wave mixing in an integrated, microring resonator with  $Q = 1.2$  million. Opt. Express 17, 14098-14103 (2009).  
77. Del'Haye, P. et al. Optical frequency comb generation from a monolithic microresonator. Nature 450, 1214-1217 (2007).  
78. Grudinin, I. S., Yu, N. & Maleki, L. Generation of optical frequency combs with a  $\mathrm{CaF}_2$  resonator. Opt. Lett. 34, 878-880 (2009).  
79. Turner, A. C., Foster, M. A., Gaeta, A. L. & Lipson, M. Ultra-low power parametric frequency conversion in a silicon microring resonator. Opt. Express 16, 4881-4887 (2008).  
80. Fukuda, H. et al. Four-wave mixing in silicon wire waveguides. Opt. Express 13, 4629-4637 (2005).  
81. Pasquazi, A. et al. All-optical wavelength conversion in an integrated ring resonator. Opt. Express 18, 3858-3863 (2010).  
82. Morichetti, F. et al. Travelling-wave resonant four-wave mixing breaks the limits of cavity-enhanced all-optical wavelength conversion. Nat. Commun. 2, 296 (2011).  
83. Cundiff, S. T. & Weiner, A. M. Optical arbitrary waveform generation. Nature Photon. 4, 760-766 (2010).  
84. Jiang, Z., Huang, C. B., Leaird, D. E. & Weiner, A. M. Optical arbitrary waveform processing of more than 100 spectral comb lines. Nature Photon. 1, 463-467 (2007).  
85. Khan, M. H. et al. Ultrabroad-bandwidth arbitrary radiofrequency waveform generation with a silicon photonic chip-based spectral shaper. Nature Photon. 4, 117-122 (2010).  
86. Udem, Th., R. Holzwarth, R. & Hansch, T. W. Optical frequency metrology. Nature 416, 233-237 (2002).  
87. Jones, D. et al. Carrier-envelope phase control of femtosecond modelocked lasers and direct optical frequency synthesis. Science 288, 635-639 (2000).

88. Ranka, J. K., Windeler, R. S. & Stentz, A. J., Visible continuum generation in air-silica microstructure optical fibers with anomalous dispersion at  $800\mathrm{nm}$ . Opt. Lett. 25, 25-27 (2000).  
89. Lamont, M. R., Luther-Davies, B., Choi, D.-Y., Madden, S. & Eggleton B. J. Supercontinuum generation in dispersion engineered highly nonlinear  $(\gamma = 10 / \mathrm{W} / \mathrm{m})$  AsS3 chalcogenide planar waveguide. Opt. Express 16, 14938 (2008).  
90. Phillips, C. R. et al. Supercontinuum generation in quasi-phase-matched  $\mathrm{LiNbO}_3$  waveguide pumped by a Tm-doped fiber laser system. Opt. Lett. 36, 3912-3914 (2011).  
91. Koonath, P., Solli, D. R. & Jalali, B. Limiting nature of continuum generation in silicon. Appl. Phys. Lett. 93, 091114 (2008).  
92. Duchesne, D. et al. Supercontinuum generation in a high index doped silica glass spiral waveguide. Opt. Express 18, 923-930 (2010).  
93. Halir, R. et al. Ultrabroadband supercontinuum generation in a CMOS-compatible platform. Opt. Lett. 37, 1685-1687 (2012).  
94. Dudley, J. M., Genty, G. & Coen, S. Supercontinuum generation in photonic crystal fiber. Rev. Mod. Phys. 78, 1135-1184 (2006).  
95. Hsieh, I.-W. et al. Supercontinuum generation in silicon photonic wires. Opt. Express 15, 15242-15249 (2007).  
96. Bartels, A. et al. Femtosecond-laser-based synthesis of ultrastable microwave signals from optical frequency references. Opt. Lett. 30, 667-669 (2005).  
97. Herrmann, J. et al. Experimental evidence for supercontinuum generation by fission of higher-order solitons in photonic fibers. Phys. Rev. Lett. 88, 173901 (2002).  
98. Herr, T. et al. Temporal solitons in optical microresonators. Preprint at http://arxiv.org/abs/1211.0733v3 (2013).  
99. Leo, F. et al. Temporal cavity solitons in one-dimensional Kerr media as bits in an all-optical buffer. Nature Photon. 4, 471-476 (2010).  
100. Quiroga-Teixeiro, M., Balslev Clausen, C., Sorensen, M. P., Christiansen, P. L. & Andrekson, P. A. Passive mode locking by dissipative four-wave mixing. J. Opt. Soc. Am. B 15, 1315-1321 (1998).  
101. Sylvestre, T., Coen, S., Emplit, P. & Haelterman, M. Self-induced modulational instability laser revisited: Normal dispersion and dark-pulse train generation. Opt. Lett. 27, 482-484 (2002).  
102. Schröder, J., Vo, T. D. & Eggleton, B. J. Repetition-rate-selective, wavelength-tunable mode-locked laser at up to 640 GHz. Opt. Lett. 34, 3902-3904 (2009).  
103. Schawlow, A. L. & Townes, C. H. Infrared and optical masers. Phys. Rev. 112, 1940-1949 (1958).  
104. Yoshida, M., Ono, A. & Nakazawa, M. 10 GHz regeneratively modelocked semiconductor optical amplifier fibre ring laser and its linewidth characteristics. Opt. Lett. 32, 3513-3515 (2007).  
105. Foster, M. et al. Silicon-chip-based ultrafast optical oscilloscope. Nature 456, 81-84 (2008).  
106. Pasquazi, A. et al. Time-lens measurement of subpicosecond optical pulses in CMOS compatible high-index glass waveguides. IEEE J. Selected Topics in Quant. Electron. 18, 629-636 (2012).  
107. Trebino, R. Frequency Resolved Optical Gating: The Measurement of Ultrashort Laser Pulses (Kluwer Academic, 2002).  
108. Iaconis, C. & Walmsley, I. A. Spectral phase interferometry for direct electric field reconstruction of ultrashort optical pulses. Opt. Lett. 23, 792-794 (1998).  
109. Iaconis, C. & Walmsley, I. A. Self-referencing spectral interferometry for measuring ultrashort optical pulses. IEEE J. Quant. Electron. 35, 501-509 (1999).  
110. Gallmann, L. et al. Characterization of sub-6-fs optical pulses with spectral phase interferometry for direct electric-field reconstruction. Opt. Lett. 24, 1314-1316 (1999).  
111. Dorrer, C. et al. Single-shot real-time characterization of chirped-pulse amplification systems by spectral phase interferometry for direct electric-field reconstruction. Opt. Lett. 24, 1644-1646 (1999).

112. Bromage, J., Dorrer, C., Begishev, I. A., Usechak, N. G. & Zuegel, J. D. Highly sensitive, single-shot characterization for pulse widths from 0.4 to 85 ps using electro-optic shearing interferometry. Opt. Lett. 31, 3523-3525 (2006).  
113. Dorrer, C. & Bromage, J. High-sensitivity optical pulse characterization using Sagnac electro-optic spectral shearing interferometry. Opt. Lett. 35, 1353-1355 (2010).  
114. Walmsley, I. A. & Dorrer, C. Characterization of ultrashort electromagnetic pulses. Adv. Opt. Photon. 1, 308-437 (2009).  
115. Anderson, M. E., Monmayrant, A., Gorza, S. P., Wasylczyk, P. & Walmsley, I. A. SPIDER: a decade of measuring ultrashort pulses. *Laser Phys. Lett.* 5, 259-266 (2008).  
116. Pasquazi, A., Peccianti, M., Azana, J., Moss, D. J. & Morandotti, R. FLEA: Fresnel-limited extraction algorithm for direct field reconstruction (SPIDER). Opt. Express 21, 5743-5758 (2013).  
117. Moss, D. J., van Driel, H. M. & Sipe, J. E. Third harmonic generation as a structural diagnostic of ion-implanted amorphous and crystalline silicon. Appl. Phys. Lett. 48, 1150 (1986).  
118. Orobchouk, R. et al. in Proc. SPIE 6183, Integrated Optics, Silicon Photonics, and Photonic Integrated Circuits paper 618304 (SPIE, 2006).  
119. Fedeli, J. M. et al. in Proc. 3rd IEEE International Conf. on Group IV Photonics 200-202 (IEEE, 2006).  
120. Ikeda, K., Shen, Y. & Fainman, Y. Enhanced optical nonlinearity in amorphous silicon and its application to waveguide devices. Opt. Express 15, 17761-17771 (2007).  
121. Shoji, Y. et al. Ultrafast nonlinear effects in hydrogenated amorphous silicon wire waveguide. Opt. Express 18, 5668-5673 (2010).  
122. Narayanan, K. & Preble, S. F. Optical nonlinearities in hydrogenated amorphous silicon waveguides. Opt. Express 18, 8998-9905 (2010).  
123. Suda, S. et al. Pattern-effect-free all-optical wavelength conversion using a hydrogenated amorphous silicon waveguide with ultra-fast carrier decay. Opt. Lett. 37, 1382-1384 (2012).  
124. Wang, K.-Y. & Foster, A. C. Ultralow power continuous-wave frequency conversion in hydrogenated amorphous silicon waveguides. Opt. Lett. 37, 1331-1333 (2012).  
125. Kuyken, B. et al. On-chip parametric amplification with 26.5 dB gain at telecommunication wavelengths using CMOS-compatible hydrogenated amorphous silicon waveguides. Opt. Lett. 36, 552-554 (2011).  
126. Kuyken, B. et al. Nonlinear properties of and nonlinear processing in hydrogenated amorphous silicon waveguides. Opt. Express 19, B146-B153 (2011).  
127. Grillet, C. et al. Amorphous silicon nanowires combining high nonlinearity, FOM and optical stability. Opt. Express 20, 22609 (2012).  
128. Corcoran, B. et al. Optical signal processing on a silicon chip at 640Gb/s using slow-light. Opt. Express 18, 7770-7781 (2010).  
129. Monat, C. et al. Slow light enhanced nonlinear optics in silicon photonic crystal waveguides. IEEE J. of Selected Topics in Quant. Elect. 16, 344-356 (2010).

# Acknowledgements

The authors acknowledge financial support from the Australian Research Council Discovery Project and the Centres of Excellence programme, the Canadian Natural Sciences and Engineering Research Council (NSERC), the Defense Advanced Research Projects Agency (DARPA) and the National Science Foundation. We would also like to thank A. Pasquazi and M. Peccianti for proofreading the manuscript.

# Additional information

Reprints and permissions information is available at www.nature.com/reprints. Correspondence and requests for materials should be addressed to D. Moss (dmoss@physics.usyd.edu.au).

# Additional information

The authors declare no competing financial interests.