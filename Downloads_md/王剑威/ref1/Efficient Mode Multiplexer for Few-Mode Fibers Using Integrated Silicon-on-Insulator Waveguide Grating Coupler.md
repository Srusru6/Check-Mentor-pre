# Efficient Mode Multiplexer for Few-Mode Fibers Using Integrated Silicon-on-Insulator Waveguide Grating Coupler

Yeyu Tong, Student Member, IEEE, Wen Zhou, Xinru Wu and Hon Ki Tsang, Fellow, IEEE

Abstract-We propose a novel and highly efficient multimode waveguide grating coupler which can simultaneously launch four channels including two polarizations of the linear polarized (LP) modes,  $\mathrm{LP}_{01}$  and  $\mathrm{LP}_{11}$  of a step-index few-mode fiber (FMF). The waveguide grating coupler on the silicon-on-insulator (SOI) platform is based on a subwavelength structure which was optimized using the genetic optimization approach with 2-dimensional finite-difference time-domain (2-D FDTD) simulations combined with the second-order effective medium theory (EMT). Simulations predicted the coupling efficiencies to be  $-4.3\mathrm{dB}$  for  $\mathrm{LP}_{01}$  mode and  $-5.0\mathrm{dB}$  for the  $\mathrm{LP}_{11}$  mode. The design was fabricated in a multi-project wafer (MPW) run for silicon photonics. Coupling efficiency of  $-4.9\mathrm{dB}$  and  $-6.1\mathrm{dB}$  was experimentally demonstrated for  $\mathrm{LP}_{01}$  mode and  $\mathrm{LP}_{11}$  mode, respectively. The proposed mode multiplexer is entirely passive and suitable for future applications with FMFs in the space-division-multiplexing (SDM) networks.

Index Terms- Integrated optics, diffraction gratings, few-mode fibers, space-division multiplexing.

# I. INTRODUCTION

DRIVEN by the exponential growth of data traffic in recent years, use of the transmission capacity of conventional standard single-mode fiber (SSMF) has already approached the theoretical limit imposed by the Shannon's information theory and nonlinear fiber effects [1], [2]. Dense wavelength-division-multiplexing, polarization multiplexing, and spectrally efficient advanced modulation formats have all been widely exploited to increase the transmission capacity in optical fibers. Introduction of the new dimension of space-division multiplexing (SDM) using the few-mode fibers (FMFs) [3], multi-core single-mode fibers (MC-SMFs) [4] or multi-core few-mode fibers (MC-FMFs) [5] have thus attracted much interest to enable further growth in transmission capacity and meet continued exponential growth in data center traffic.

As one of the key building blocks, a reliable, efficient and

Manuscript received xxx, xxx; revised xxx, xxx; accepted xxx, xxx. Date of publication xxx, xxx; date of current version xxx, xxx. This work was funded by Hong Kong Research Grants Council/NSFC Joint Research Scheme (N CUHK404/14). (Corresponding author: Hon Ki Tsang.)

Y. Tong, W. Zhou, X. Wu and H. K. Tsang are with the Department of Electronic Engineering, the Chinese University of Hong Kong, Shatin, N.T., Hong Kong (e-mail: yytong_ee@link.cuhk.edu.hk; wzhou@ee.cuhk.edu.hk; xrwu@link.cuhk.edu.hk and hktsgang@ee.cuhk.edu.hk).

low-cost mode multiplexer for FMFs is thus highly desired for future SDM applications. Advanced digital signal processing (DSP) techniques such as multiple-input multiple-output (MIMO) [3], or all-optically through a mesh of tunable beam splitters [6] may make it unnecessary to (de)multiplex individual modes with particularly low crosstalk, as mode scrambling is inevitable when light beams propagate through scattering or multimode systems.

Mode multiplexers for FMFs based on the free-space optics, such as using the phase plates [3] and the spatial light modulator [7] have been demonstrated. To reduce the insertion loss and implementation complexity, technologies employing the fiber-based photonic lanterns [8]-[10] and the laser inscribed 3-dimensional (3-D) optical waveguides [11]-[13] have been demonstrated. State-of-art results have been reported with increased degrees of freedom by using the laser inscribed 3-D optical waveguides. Meanwhile, integrated diffraction gratings on silicon-on-insulator (SOI) platform relying on the mature planar lithography methods originally developed for silicon microelectronics are also a promising candidate. The monolithic integration offers advantages of low cost, high reliability, mass-production ability and capability of co-integration with other integrated photonic devices such as transceivers [14], [15].

Previous demonstrations using the integrated diffraction gratings as mode multiplexers include circular gratings for a special ring-core fiber [16], multiple gratings with active phase control [17]–[20] for a standard FMF or a single subwavelength diffraction grating [21], [22]. Employing the standard fibers may have the potential of less fabrication cost. In the scheme of spot-excitation by multiple gratings, the individual grating sizes are limited, and this results in a poor mode matching between the diffracted light field and the mode profile of the fiber. This challenge has meant that the reported experimental coupling efficiency using this approach is typically low, of the order of  $-23\mathrm{dB}$  [18]. A coupling efficiency of  $-10.6\mathrm{dB}$  was demonstrated with the use of an aluminum mirror to enhance the grating directionally [23]. To overcome the issue of mode size mismatch, a single subwavelength grating can be utilized so that the grating size is not restricted. However, due to the symmetry of the diffracted light field perfect vertical coupling is required, which limits the coupling efficiency due to the second-order Bragg reflection [24]–[26]. An efficient coupling scheme utilizing the integrated diffraction gratings for FMFs

has not been previously reported to the best of our knowledge.

In this paper, we present a detailed design approach and experimental measurement results of a novel single diffraction grating [27] for launching different modes from a multimode silicon waveguide into different modes of FMF. The proposed subwavelength waveguide grating coupler was optimized using the genetic optimization algorithm. To reduce simulation time, we used 2-dimensional finite-difference time-domain (2-D FDTD) simulation and second-order effective medium theory (EMT) for design optimization. We realized the first experimental demonstration of an efficient mode multiplexer

![](images/207a63b856988c35b6576289c5cb51aabd9605a153eaa0b7bc268138253947c0.jpg)  
(a)

![](images/e6a2af695a2bd892b06100a0efebd05fc298dfc7654be6d3577d952192de6a86.jpg)  
(b)

![](images/2178bbc62fbf788056ed72e4831071c79d8306019e3701efe4bf62fe1eb4e4e4.jpg)  
(c)

![](images/d0f49df8356e2f23b39747294a314eff8ad2138c6c196dcce97e94d31a0fd6a9.jpg)  
(d)  
Fig. 1. Schematic diagrams of mode excitation in a standard two-mode step-index few-mode fiber (FMF) via a subwavelength waveguide grating. (a)  $\mathrm{LP}_{01 - x}$  mode, (b)  $\mathrm{LP}_{01 - y}$  mode, (c)  $\mathrm{LP}_{11 - x}$  mode and (d)  $\mathrm{LP}_{11 - y}$  mode.

employing a single diffraction grating to launch four channels including two polarizations of the linear polarized (LP) modes  $\mathrm{LP}_{01}$  and  $\mathrm{LP}_{11}$  into a step-index few-mode fiber (FMF), with an experimental coupling efficiency of  $-4.9$  dB and mode-dependent loss of  $-1.2$  dB. The proposed device has a good fabrication tolerance and is compatible with commercial silicon photonics foundry and will thus be suitable for industrial large-volume manufacturing of photonic integrated circuits (PICs) in the future.

# II. DESIGN STRATEGY AND OPTIMIZATION

The multimode waveguide grating coupler based mode multiplexer is designed for interface to an OFS two-mode step-index FMF with a core diameter of  $19.4\mu \mathrm{m}$ . The waveguide grating coupler can launch light into the  $\mathrm{LP}_{01}$  and  $\mathrm{LP}_{11}$  modes of the FMF from the quasi transverse-electric (TE) fundamental  $(\mathrm{TE}_0)$  and first-order  $(\mathrm{TE}_1)$  modes of a silicon waveguide respectively. The principle of mode excitation via a single subwavelength grating is schematically depicted in Figs. 1(a)-1(d).

Efficient coupling of the two TE modes via a single diffraction grating is possible because their effective refractive index in the wide waveguide grating coupler region, which has an expanded width of more than  $10~\mu \mathrm{m}$ , are very similar. An identical design is used to support an equivalent performance in the other orthogonal polarization. The two multimode waveguides are orientating at 90 degrees to each other as shown in Fig. 1, so that four channels can be coupled to the FMF entirely passive by the proposed structure.

The SOI wafer has a 220-nm-thick top silicon layer and a  $2 - \mu \mathrm{m}$ -thick buried-oxide layer. Mode field diameter (MFD) of  $\mathrm{LP}_{01}$  mode and  $\mathrm{LP}_{11}$  mode in the step-index FMF is larger than the typical MFD of the SSMF. Reduced grating strength is thus necessary by employing the  $70\mathrm{-nm}$  shallow-etched subwavelength holes in the standard fabrication process provided by the fabrication foundry [28].

![](images/d89751f00d8fc62023a415487fde8b7eec19bed4d1d1921bdfd5c994ba3622e2.jpg)  
Fig. 2. Schematic diagram of the proposed photonic integrated circuits (PICs), including the standard single-mode grating couplers, asymmetric directional couplers (ADCs), linear tapers and mode multiplexer based on the integrated waveguide grating.

Schematic diagram of the proposed PICs is presented in Fig. 2. Four input optical signals are coupled via the  $10^{\circ}$  off-vertical standard single-mode grating couplers to  $450\mathrm{-nm}$  single-mode waveguides. Asymmetric directional couplers (ADCs) with a  $200\mathrm{-nm}$  coupling gap are utilized for the mode multiplexing of the  $\mathrm{TE}_0$  mode and  $\mathrm{TE}_1$  mode [29], [30]. The  $1 - \mu \mathrm{m}$ -wide multimode waveguide are connected to the wide grating by a  $600 - \mu \mathrm{m}$ -long linear adiabatic taper with negligible loss for both  $\mathrm{TE}_0$  mode and  $\mathrm{TE}_1$  mode.

Due to the diffraction symmetry of the proposed mode multiplexer, perfectly vertical coupling is required to reduce the channel-dependent coupling loss. Typical grating couplers are designed to couple the light at a small angle of about 10 degree relative to the chip-surface normal to suppress the second-order Bragg reflection into the waveguides. Efficient perfect vertical coupling can be realized by chirping the grating structure using the genetic optimization with FDTD simulations [31]. However, the optimization process typically requires thousands of times of simulation to search the best figure of merits (FOMs) in the multiple parameters space. Each 3-dimensional (3-D) FDTD simulation of the proposed device with a footprint larger than dozens of micros requires several hours to finish [32], leading to an extremely long time for convergence of the optimization.

To reduce the simulation time for numerical iterations, 2-D FDTD combined with the second-order EMT is proposed for optimization of the diffraction grating. Indeed that only performance of the fundamental mode in a single polarization can be estimated by using 2-D FDTD simulation as applied for optimization of the single mode grating coupler [31]. But under premise that the  $\mathrm{TE}_1$  mode has a similar effective refractive index with the  $\mathrm{TE}_0$  mode in the grating region based on this polarization-insensitive symmetric design, performance of the

![](images/946cd13409578e9b302b44c7c634ec21f5c148f12eb145355449405d2f641969.jpg)  
Fig. 3. Genetic optimization flow chart.

![](images/07fc44fdd96e7043356ed8d460f2972fdd5c731962e00e9718a7fedab34c27b6.jpg)  
Fig. 4. Evolutionary diagram of the normalized fitness against the number of optimization iterations.

$\mathrm{TE}_1$  mode and modes in the orthogonal polarization in the optimization process can be waived, as theoretically a similar performance would be expected.

The refractive index of subwavelength structure in the 2-D FDTD simulation is estimated using the following second order approximation of the EMT [33], [34],

$$
\begin{array}{l} n _ {T M} ^ {(2)} = n _ {T M} ^ {(0)} \left[ 1 + \frac {\pi^ {2}}{3} \left(\frac {\Lambda_ {\text {a v g}}}{\lambda}\right) ^ {2} f _ {\text {a v g}} ^ {2} \left(1 - f _ {\text {a v g}}\right) ^ {2} \right. \\ \left. \times \left(n _ {\text {s i l i c o n}} ^ {2} - n _ {\text {h o l e (o x i d e)}} ^ {2}\right) ^ {2} \frac {1}{\left(n _ {T M} ^ {(0)}\right) ^ {2}} \right] ^ {\frac {1}{2}}, \tag {1} \\ \end{array}
$$

$$
\begin{array}{l} n _ {T E} ^ {(2)} = n _ {T E} ^ {(0)} \left[ 1 + \frac {\pi^ {2}}{3} \left(\frac {\Lambda_ {\text {a v g}}}{\lambda}\right) ^ {2} f _ {\text {a v g}} ^ {2} \left(1 - f _ {\text {a v g}}\right) ^ {2} \right. \\ \left. \times \left(n _ {\text {s i l i c o n}} ^ {2} - n _ {\text {h o l e (o x i d e)}} ^ {2}\right) ^ {2} \left(n _ {T M} ^ {(0)}\right) ^ {2} \left(\frac {\left(n _ {T E} ^ {(0)}\right) ^ {2}}{n _ {\text {s i l i c o n}} ^ {2} n _ {\text {h o l e (o x i d e)}} ^ {2}}\right) ^ {2} \right] ^ {\frac {1}{2}}, \tag {2} \\ \end{array}
$$

where

$$
n _ {T M} ^ {(0)} = \left[ f _ {\text {a v g}} n _ {\text {h o l e (o x i d e)}} ^ {2} + \left(1 - f _ {\text {a v g}}\right) n _ {\text {s i l i c o n}} ^ {2} \right] ^ {\frac {1}{2}}, \tag {3}
$$

$$
\frac {1}{n _ {T E} ^ {(0)}} = \left[ \frac {f _ {\text {a v g}}}{n _ {\text {h o l e (o x i d e)}} ^ {2}} + \frac {(1 - f _ {\text {a v g}})}{n _ {\text {s i l i c o n}} ^ {2}} \right] ^ {- \frac {1}{2}}, \tag {4}
$$

where  $n_{TM}^{(0)}$  and  $n_{TE}^{(0)}$  are refractive indexes of the TM mode and TE mode derived by the 0th-order approximation.  $n_{silicon}$  and  $n_{hole(oxide)}$  are refractive index of the silicon and silicon oxide.  $\lambda$  is the center wavelength.  $\Lambda_{avg}$  and  $f_{avg}$  are the averaged grating period and filling factor.

Structural parameters including the grating periods, the hole size and the end-reflectors are optimized by the genetic optimization algorithm to suppress the back reflection and improve the coupling efficiency with an optimization flow chart shown in Fig. 3.

The genetic optimization algorithm includes the following procedures as shown in Fig. 3: (i) Initializing the populations with random periodic structural parameters subject to the constraints of the feature size in the standard 193-nm deep-ultraviolet (DUV) photolithography. (ii) Evaluating the fitness of each population with a 2-D FDTD simulation in Lumerical [32]. The fitness  $F$  is denoted by equation (5),

$$
F = \sum_ {i = 1} ^ {N} C E \left(\lambda_ {i}\right) - B R \left(\lambda_ {i}\right) \tag {5}
$$

where  $CE$  is the coupling efficiency and  $BR$  is the back reflection. (iii) Defining the maximum number of iterations. The optimization completes when no progress is obtained in the most-recent 30 generations. (iv) Selecting the populations according to their fitness with the roulette-wheel selection

method [35]. The new generation is acquired after (v) crossover and (vi) mutation. Each of the selected individuals has an  $80\%$  probability to intermix with another individual to generate the two children individuals at a random crossover point. The children individuals have a  $10\%$  probability of mutation where the selected structural parameters are randomly varied. An optimization loop is formed by stepping back to (ii).

40 rows and columns of the shallow-etched holes are utilized to cover an area of about  $22 \times 22 \mu \mathrm{m}^2$  for the multimode waveguide grating to obtain a good mode size match with the modes in the FMF. For ease of calculation, square-shaped hole is used in the 2-D FDTD simulation, which will be converted to the round-shaped hole in fabrication with the same area as round-shaped hole can be fabricated using the standard DUV photolithography with less stringent photolithography requirements [36], [37].

Evolutionary diagrams of the normalized fitness against number of iterations is shown in Fig. 4. Evident convergence progress is observed. For ease of fabrication, the hole size is kept the same to chirp only the grating periods. The optimized length of the grating periods is shown in Fig. 5. The optimized side length of the square-shaped holes is  $286~\mathrm{nm}$ , which corresponds to round-shaped holes with a diameter of  $322~\mathrm{nm}$ . Three rectangular slabs with a width of  $190~\mathrm{nm}$  and a spacing of  $240~\mathrm{nm}$  are used as an end reflector at the end of the grating to

![](images/62d02e5649472a980b2dbb646f36d3d25d5423b41df23ea12fdaf445443366ca.jpg)  
Fig. 5. Optimized length of the grating periods with an etched hole diameter of  $322\mathrm{nm}$ .

![](images/7180238151857d8c45051e0c3294141278547c4c4a5e74e8e82d67e1f54d9307.jpg)  
Fig. 6. Coupling efficiency (CE) and back reflection (BR) of the final-optimized grating coupler obtained by 3-D FDTD simulation.

![](images/9529437057550f1095772d313f3e227a82567c2ce727ebf28f622dd34e6ce81f.jpg)  
Fig. 7. Experimental coupling efficiencies of the multimode waveguide grating for LP01-x, LP01-y, LP11-x and LP11-y, respectively.

improve the coupling efficiency. The minimum feature size of the proposed structure is thus  $\geq 190\mathrm{nm}$  for robust fabrication using  $193\mathrm{nm}$  DUV lithography.

Performances of final-optimized multimode waveguide grating coupler are obtained by 3-D FDTD simulation as presented in Fig. 6.  $\mathrm{TE}_0$  mode has a coupling efficiency of  $-4.3$  dB (36.8%) at a center wavelength of  $1544\mathrm{nm}$ .  $\mathrm{TE}_1$  mode has a coupling efficiency of  $-5.0$  dB (31.8%) at a center wavelength of  $1542\mathrm{nm}$ . The center wavelength shift of about  $2\mathrm{nm}$  is due to the difference of the effective refractive index between the  $\mathrm{TE}_0$  mode and  $\mathrm{TE}_1$  mode. 3-dB bandwidth is about  $20\mathrm{nm}$  for both modes. Reflection into the SOI waveguide is suppressed below  $-11$  dB within C band.

# III. EXPERIMENTAL RESULTS

The coupling efficiency is characterized by measuring the fiber-waveguide-fiber insertion loss with a SSMF as the input and a step-index two-mode FMF as the output. The coupling spectrums of the  $\mathrm{LP}_{01 - x}$ ,  $\mathrm{LP}_{01 - y}$ ,  $\mathrm{LP}_{11 - x}$  and  $\mathrm{LP}_{11 - y}$  using a single multimode waveguide grating are shown in Fig. 7, after

![](images/d61b203e3613fad4fe3e0a4e660307c7e764439469c28036f15eff115b8e20b3.jpg)

![](images/6cee51a8733bba904699c100339cb03cb293b1b6bc6c94ff866cf2b413fc72cb.jpg)

![](images/a9f6996ebae547fe65af93f3454776395c668bcce0df394deb639bfd8133ab0f.jpg)  
Fig. 8. Output field profiles of the FMF when  $\mathrm{LP}_{01 - x}$ ,  $\mathrm{LP}_{01 - y}$ ,  $\mathrm{LP}_{11 - x}$  and  $\mathrm{LP}_{11 - y}$  are selectively launched by the multimode waveguide grating coupler.

![](images/74a9dfe31b6778d2b3983b2d569a8a6bccedb422e708963faef9b5e73df99aad.jpg)

![](images/18e8ce68463c0dc567ee042c0050bfbfc8485bb4f92a555e59dded181ee2a47a.jpg)

![](images/20d01a05c9cdfff0d49c32df82cfe8f6d392194b4c78783b15eb1adf6a33a82c.jpg)  
Fig. 9. (a) SEM image of the single-mode gratings and ADCs with a zoom-in view shown in the inset. (b) SEM image of the fabricated subwavelength grating with a zoom-in view shown in the inset.

normalizing out the loss from the ADC, the linear taper and the single-mode grating coupler fabricated on the same chip. A coupling efficiency of  $-4.9\mathrm{dB}$  is obtained at  $1551.0~\mathrm{nm}$  for  $\mathrm{LP}_{01 - x}$  mode and  $\mathrm{LP}_{01 - y}$  mode.  $\mathrm{LP}_{11 - x}$  mode and  $\mathrm{LP}_{11 - y}$  mode have

a coupling efficiency of  $-6.1$  dB at  $1549.6\mathrm{nm}$ . Experimental 3-dB bandwidth for all the four channels is about  $15\mathrm{nm}$ . Slight discrepancies are observed between the experimental performance and the simulation results, including a red wavelength shift and a narrower 3-dB optical bandwidth. These are due to the shallow-etched hole diameter of the fabricated device is about  $25\mathrm{nm}$  smaller, as confirmed by the zoom-in scanning electron microscope (SEM) images of the grating.

To confirm that the multimode waveguide grating coupler can selectively launch two polarizations of the  $\mathrm{LP}_{01}$  mode and  $\mathrm{LP}_{11}$  mode in the FMF. Output field profiles of the FMF are captured by an infrared camera with a  $40\times$  lens when different modes are selectively excited by the multimode waveguide grating coupler as shown in Figs. 8(a)-8(d).

SEM images of the PICs are obtained by removing the top protective resist of the same chip without oxide deposition. The fabricated ADCs, single-mode input grating couplers and subwavelength grating as the mode multiplexer are shown in Figs. 9(a) and 9(b).

For proof of concept of the use of the multimode waveguide grating for mode division multiplexing, we carried out an experimental demonstration of data communications of 160 Gb/s per wavelength using the four modes of the FMF with the experimental setup in Fig. 10(a). The 40-Gb/s non-return-to-zero on-off keying (NRZ-OOK) signals are generated by a bit pattern generator (BPG) with a commercial  $\mathrm{LiNbO_3}$  Mach-Zehnder modulator (MZM). Wavelength of the tunable laser (TL) is set at  $1550~\mathrm{nm}$ . A single-mode polarization controller (PC) is used to align the polarization of the optical signals to match with the input single-mode grating couplers. The multimode waveguide grating coupler will selectively excite different modes in the FMF for a transmission length of 15 meters. A second photonic chip with the same multimode waveguide grating coupler is utilized at the receiver side to demultiplex the modes in the FMF. The optical polarization before demultiplexing is aligned by a few-mode three-paddle

![](images/f95dc725243b5f822092ddb857a165134fd0e739a51b737ab607481b0b485f03.jpg)  
(b)

![](images/70d4898de739ff9d42d33b1b9d3553bbaa7da602619bf6dedd155b61f56488e6.jpg)  
$\mathbf{L}\mathbf{P}_{01 - \mathbf{x}}$

![](images/c85020fef3f0a9947e16d7edf48ebea4f9c299ea3ce512eaed26990f022a943a.jpg)  
Fig. 10. (a) Experimental setup for  $4 \times 40$  Gb/s On-off-keying signals over 15-m FMF transmission, including bit pattern generator (BPG), RF amplifier (RF Amp.), tunable laser (TL), polarization controller (PC), Mach-Zehnder modulator (MZM), erbium doped fiber amplifier (EDFA), few-mode-fiber (FMF) and photodiode with trans-impedance amplifier (PD+TIA). (b)-(e) 40-Gb/s eye diagrams at a received optical power of  $-5$  dBm for  $\mathrm{LP}_{01 - x}$ ,  $\mathrm{LP}_{01 - y}$ ,  $\mathrm{LP}_{11 - x}$  and  $\mathrm{LP}_{11 - y}$  mode, respectively.  
(c)  
$\mathbf{L}\mathbf{P}_{01 - \mathrm{y}}$

![](images/e6d1278d1cbdea224bf85e0081682dbd2cce9aaa890c85c25053af25e55089cd.jpg)  
(d)  
$\mathbf{LP}_{11 - \mathbf{x}}$

![](images/0d8787f12ce147a988273d3d75bbe4640b2c0c5d490e723ef005d97fcb762c27.jpg)  
(e)  
$\mathbf{LP}_{11 - \mathrm{y}}$

mechanical PC. To compensate the optical power loss before detection, the received optical signals are amplified by an erbium doped fiber amplifier (EDFA).

The mode crosstalk after two photonic chips in the experiment is about  $-6$  dB mainly induced by the multimode waveguide grating coupler and the ADCs. And the polarization crosstalk is around  $-13$  dB at the center wavelength. Clear received eye diagrams were measured as shown in Figs. 10(b)–10(e), demonstrating that the multimode waveguide grating coupler can be used for high-speed optical communication applications.

# IV. DISCUSSIONS

The multimode waveguide grating coupler in this demonstration was fabricated on a commercial MPW run and the multimode waveguide grating coupler is thus suitable for use in for large-volume production of PICs. Unlike previous reported approaches for coupling to multimode fibers using waveguide gratings, no active control on the phase was required to support four channels including two polarizations of the  $\mathrm{LP}_{01}$  mode and  $\mathrm{LP}_{11}$  mode in the FMF. Improved performance may be possible in this future with better diffraction directionality obtained with optimized silicon thickness and etching depth.

The proposed 2-D FDTD simulation with the second-order EMT can drastically reduce the simulation time to about 10 seconds instead of more than 5 hours in 3-D FDTD under the same mesh order. Numerical iterations in the multiple parameter space are thus feasible to search for the device with the best FOM. As confirmed by the 3-D FDTD simulation and the final experimental performance, the proposed approach is suitable for optimization of the polarization-diverse multi-mode subwavelength grating coupler. The optimization method can also be applied to other types of multimode waveguide grating couplers which can couple to more modes or other types of multi-mode fibers. To match the phase distribution of the fiber modes, engineering of the phase and amplitude profile of the waveguide modes passively [20] or actively [21] is necessary. As the MFD of the  $\mathrm{LP}_{01}$  mode and  $\mathrm{LP}_{11}$  mode are slightly different in the step-index FMF, a lower mode-dependent loss may be possible by optimizing the grating width to have extra emphasis on the  $\mathrm{LP}_{11}$  mode. Optical bandwidth of the grating can be improved by using the subwavelength pillar structure and reducing the grating effective index [38]. With the use of perfectly vertical coupling grating designs, the multimode waveguide grating coupler described in this paper can also be compatible with multi-core few-mode fibers (MC-FMFs) [5], [31].

To support future developments of the multimode waveguide grating couplers in SDM communication networks, advanced DSP techniques like MIMO [3], [19] or all-optical method through a mesh of tunable beam splitters [6] can be exploited to undo the linear impairments including dispersion, intermodal crosstalk, differential group delay (DGD), random polarization mixing and coupling effects occurring in the (de)multiplexing and within the fiber between modes.

# V. CONCLUSIONS

To summarize, we proposed a novel design of mode multiplexer for the FMFs employing a single subwavelength multimode waveguide grating on SOI. The mode multiplexer is entirely passive and capable of excitations of the  $\mathrm{LP}_{01 - x}$ ,  $\mathrm{LP}_{01 - y}$ ,  $\mathrm{LP}_{11 - x}$  and  $\mathrm{LP}_{11 - y}$  modes in a step index FMF. An efficient design approach was proposed based on the genetic optimization and 2-D FDTD simulation with the second-order EMT. Coupling efficiency up to  $-4.3$  dB with a mode-dependent loss of  $0.7\mathrm{dB}$  were obtained in simulation. Experimental coupling efficiencies of  $-4.9$  dB and  $-6.1$  dB were demonstrated respectively for two polarizations of the  $\mathrm{LP}_{01}$  mode and the  $\mathrm{LP}_{11}$  mode. To the best of our knowledge, this is the first experimental demonstration of such efficient four-channel mode multiplexer for FMFs using a single multimode waveguide grating coupler on SOI. The demonstrated mode multiplexer is suitable for future high-speed communication applications with FMFs in SDM networks.

# ACKNOWLEDGEMENTS

The authors thank IMEC for the device fabrication and Wen Zhou acknowledges the support from the Postdoctoral Hub-Innovation and Technology Fund (PH-ITF).

# REFERENCES

[1] P. J. Winzer, “Making spatial multiplexing a reality,” Nature Photonics, vol. 8, pp. 345–348, Apr. 2014.  
[2] D. J. Richardson, J. M. Fini, and L. E. Nelson, "Space-division multiplexing in optical fibres," Nature Photonics, vol. 7, no. 5, pp. 354–362, May 2013.  
[3] R. Ryf et al., "Mode-Division Multiplexing Over  $96\mathrm{km}$  of Few-Mode Fiber Using Coherent  $6\times 6$  MIMO Processing," Journal of Lightwave Technology, vol. 30, no. 4, pp. 521-531, Feb. 2012.  
[4] K. Saitoh and S. Matsuo, “Multicore Fiber Technology,” J. Lightwave Technol., JLT, vol. 34, no. 1, pp. 55–66, Jan. 2016.  
[5] Y. Sasaki, K. Takenaga, N. Guan, S. Matsuo, K. Saitoh, and M. Koshiba, "Large-effective-area uncoupled few-mode multi-core fiber," Opt. Express, OE, vol. 20, no. 26, pp. B77-B84, Dec. 2012.  
[6] A. Annoni et al., "Unscrambling light—automatically undoing strong mixing between modes," Light: Science & Applications, vol. 6, no. 12, p. e17110, Dec. 2017.  
[7] M. Salsi et al., "Transmission at  $2 \times 100\mathrm{Gb / s}$ , over Two Modes of 40km-long Prototype Few-Mode Fiber, using LCOS-based Mode Multiplexer and Demultiplexer," in Optical Fiber Communication Conference/National Fiber Optic Engineers Conference 2011 (2011), paper PDPB9, 2011, p. PDPB9.  
[8] N. K. Fontaine, R. Ryf, J. Bland-Hawthorn, and S. G. Leon-Saval, "Geometric requirements for photonic lanterns in space division multiplexing," Opt. Express, OE, vol. 20, no. 24, pp. 27123-27132, Nov. 2012.  
[9] S. G. Leon-Saval, N. K. Fontaine, J. R. Salazar-Gil, B. Ercan, R. Ryf, and J. Bland-Hawthorn, "Mode-selective photonic lanterns for space-division multiplexing," Optics Express, vol. 22, no. 1, p. 1036, Jan. 2014.  
[10] I. P. Giles, R. Chen, and V. Garcia-Munoz, "Fiber based multiplexing and demultiplexing devices for few mode fiber space division multiplexed communications," in OFC 2014, 2014, pp. 1-3.  
[11] N. K. Fontaine and R. Ryf, "Characterization of mode-dependent loss of laser inscribed photonic lanterns for space division multiplexing systems," in 2013 18th OptoElectronics and Communications Conference held jointly with 2013 International Conference on Photonics in Switching (OECC/PS), 2013, pp. 1-2.  
[12] S. Gross and M. J. Withford, "Ultrafast-laser-inscribed 3D integrated photonics: challenges and emerging applications," Nanophotonics, vol. 4, no. 3, pp. 332-352, 2015.

[13] N. Riesen, S. Gross, J. D. Love, Y. Sasaki, and M. J. Withford, "Monolithic mode-selective few-mode multicore fiber multiplexers," Sci Rep, vol. 7, no. 1, pp. 1-9, Aug. 2017.  
[14] G. Roelkens et al., "Bridging the Gap Between Nanophotonic Waveguide Circuits and Single Mode Optical Fibers Using Diffractive Grating Structures," Journal of Nanoscience and Nanotechnology, vol. 10, no. 3, pp. 1551-1562, Mar. 2010.  
[15] G. Roelkens et al., "High efficiency diffractive grating couplers for interfacing a single mode optical fiber with a nanophotonic silicon-on-insulator waveguide circuit," Appl. Phys. Lett., vol. 92, no. 13, p. 131101, Mar. 2008.  
[16] C. R. Doerr, N. K. Fontaine, M. Hirano, T. Sasaki, L. L. Buhl, and P. J. Winzer, "Silicon photonic integrated circuit for coupling to a ring-core multimode fiber for space-division multiplexing," in 2011 37th European Conference and Exhibition on Optical Communication, 2011, pp. 1-3.  
[17] A. M. J. Koonen, H. Chen, H. P. A. van den Boom, and O. Raz, "Silicon Photonic Integrated Mode Multiplexer and Demultiplexer," IEEE Photonics Technology Letters, vol. 24, no. 21, pp. 1961-1964, Nov. 2012.  
[18] Y. Ding, H. Ou, J. Xu, and C. Peucheret, "Silicon Photonic Integrated Circuit Mode Multiplexer," IEEE Photonics Technology Letters, vol. 25, no. 7, pp. 648-651, Apr. 2013.  
[19] N. K. Fontaine et al., "Space-division multiplexing and all-optical MIMO demultiplexing using a photonic integrated circuit," in OFC/NFOEC, 2012, p. PDP5B.1.  
[20] Y. Lai, Y. Yu, S. Fu, J. Xu, P. P. Shum, and X. Zhang, "Compact double-part grating coupler for higher-order mode coupling," Opt. Lett., OL, vol. 43, no. 13, pp. 3172-3175, Jul. 2018.  
[21] B. Wohlfeil, G. Rademacher, C. Stamatiadis, K. Voigt, L. Zimmermann, and K. Petermann, “A Two-Dimensional Fiber Grating Coupler on SOI for Mode Division Multiplexing,” IEEE Photonics Technology Letters, vol. 28, no. 11, pp. 1241–1244, Jun. 2016.  
[22] Y. Ding, H. Ou, J. Xu, M. Xiong, and C. Peucheret, "On-chip mode multiplexer based on a single grating coupler," in IEEE Photonics Conference 2012, 2012, pp. 707-708.  
[23] Y. Ding and K. Yvind, "Efficient silicon PIC mode multiplexer using grating coupler array with aluminum mirror for few-mode fiber," in 2015 Conference on Lasers and Electro-Optics (CLEO), 2015, pp. 1-2.  
[24] G. Roelkens, D. V. Thourhout, and R. Baets, "High efficiency grating coupler between silicon-on-insulator waveguides and perfectly vertical optical fibers," Opt. Lett., OL, vol. 32, no. 11, pp. 1495-1497, Jun. 2007.  
[25] X. Chen, C. Li, and H. K. Tsang, "Fabrication-Tolerant Waveguide Chirped Grating Coupler for Coupling to a Perfectly Vertical Optical Fiber," IEEE Photonics Technology Letters, vol. 20, no. 23, pp. 1914-1916, Dec. 2008.  
[26] L. Liu et al., "Silicon waveguide grating coupler for perfectly vertical fiber based on a tilted membrane structure," Opt. Lett., OL, vol. 41, no. 4, pp. 820-823, Feb. 2016.  
[27] Y. Tong, W. Zhou, X. Wu, and H. K. Tsang, "Efficient Mode Multiplexer for Few-Mode Fibres Using Integrated Silicon-on-Insulator Grating Coupler," presented at the European Conference on Integrated Optics (ECIO, 2019), Ghent, Belgium, 2019.  
[28] X. Chen and H. K. Tsang, "Nanoholes Grating Couplers for Coupling Between Silicon-on-Insulator Waveguides and Optical Fibers," IEEE Photonics Journal, vol. 1, no. 3, pp. 184-190, Sep. 2009.  
[29] X. Wu, C. Huang, K. Xu, C. Shu, and H. K. Tsang, "Mode-Division Multiplexing for Silicon Photonic Network-on-Chip," J. Lightwave Technol., JLT, vol. 35, no. 15, pp. 3223-3228, Aug. 2017.  
[30] D. Dai, J. Wang, and Y. Shi, "Silicon mode (de)multiplexer enabling high capacity photonic networks-on-chip with a single-wavelength-carrier light," Optics Letters, vol. 38, no. 9, p. 1422, May 2013.  
[31] Y. Tong, W. Zhou, and H. K. Tsang, "Efficient perfectly vertical grating coupler for multi-core fibers fabricated with 193-nm DUV lithography," Opt. Lett., OL, vol. 43, no. 23, pp. 5709-5712, Dec. 2018.  
[32] “http://www.lumerical.com/tcad-products/fdtd/.”  
[33] X. Chen and H. K. Tsang, “Polarization-independent grating couplers for silicon-on-insulator nanophotonic waveguides,” Opt. Lett., OL, vol. 36, no. 6, pp. 796–798, Mar. 2011.  
[34] X. Chen, C. Li, and H. K. Tsang, “Two dimensional silicon waveguide chirped grating couplers for vertical optical fibers,” Optics Communications, vol. 283, no. 10, pp. 2146-2149, May 2010.  
[35] M. Mitchell, An Introduction to Genetic Algorithms. Cambridge, MA, USA: MIT Press, 1998.

[36] R. Halir, P. Cheben, S. Janz, D.-X. Xu, I. Molina-Fernández, and J. G. Wangüemert-Pérez, "Waveguide grating coupler with subwavelength microstructures," Opt. Lett., OL, vol. 34, no. 9, pp. 1408-1410, May 2009.  
[37] W. Zhou, Z. Cheng, X. Chen, K. Xu, X. Sun, and H. Tsang, "Subwavelength Engineering in Silicon Photonic Devices," IEEE Journal of Selected Topics in Quantum Electronics, vol. 25, no. 3, pp. 1-13, May 2019.  
[38] X. Chen, K. Xu, Z. Cheng, C. K. Y. Fung, and H. K. Tsang, "Wideband subwavelength gratings for coupling between silicon-on-insulator waveguides and optical fibers," Opt. Lett., OL, vol. 37, no. 17, pp. 3483-3485, Sep. 2012.

Yeyu Tong (S'16) received the B.S. degree from University of Electronic Science of Technology, Chengdu, China, in 2016. He is currently pursuing a Ph.D. degree in electronic engineering from The Chinese University of Hong Kong, Shatin, Hong Kong. His current research interests include silicon photonics, high-speed optical interconnects, and advanced modulation formats for optical communications.

Wen Zhou was born in Wuhan, China. He received the M.S. degree from South China Normal University, Guangzhou, China, in 2014, and the Ph.D. degree in electronic engineering from The Chinese University of Hong Kong, Shatin, Hong Kong, in 2018. He is currently a Postdoctoral Fellow supported by the Postdoctoral Hub—Innovation and Technology Fund. He has authored and coauthored more than 38 papers in technical journals and international conferences. His current research interests include integrated optics, mid-infrared silicon photonics, and hyperunifrom disordered photonics.

Xinru Wu received the B.S. degree from University of Electronic Science of Technology, Chengdu, China, in 2014, and the Ph.D. degree in electronic engineering from The Chinese University of Hong Kong, Shatin, Hong Kong, in 2018. She is currently working in Acacia Communications Inc. Her current research interests include integrated optics and silicon photonics.

Hon Ki Tsang (M'91-SM'04-F'19) received the Bachelor of Arts (Hons.) degree in engineering and the Ph.D. degree from the University of Cambridge, Cambridge, U.K., in 1987 and 1991 respectively. He joined the Chinese University of Hong Kong as a Lecturer in 1993, becoming Associate Professor in 1996 and Professor in 2003. He was R&D Director at Bookham Technology plc (UK) in 2002. He served as the Chairman of the Department of Electronic Engineering from 2010 to 2016 and is currently the Associated Dean (Research) of the Faculty of Engineering. He has coauthored about 400 papers in journals and conferences. His research interests include photonic integrated circuits, silicon photonics, nonlinear waveguides, hybrid integration of two-dimensional materials, optical communications, and integrated quantum photonics. He was the Editor-in-Chief of the IEEE Photonics Society Newsletter from 2012 to 2014. He is the Editor-in-Chief of the IEEE JOURNAL OF QUANTUM ELECTRONICS. He is a Fellow of IEEE and Fellow of OSA.