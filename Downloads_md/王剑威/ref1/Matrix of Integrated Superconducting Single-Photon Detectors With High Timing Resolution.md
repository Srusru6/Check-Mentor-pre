# Matrix of Integrated Superconducting Single-Photon Detectors With High Timing Resolution

Carsten Schuck, Wolfram H. P. Pernice, Olga Minaeva, Mo Li, Gregory Gol'stman, Alexander V. Sergienko, and Hong X. Tang

(Invited Paper)

Abstract—We demonstrate a large grid of individually addressable superconducting single photon detectors on a single chip. Each detector element is fully integrated into an independent waveguide circuit with custom functionality at telecom wavelengths. High device density is achieved by fabricating the nanowire detectors in traveling wave geometry directly on top of silicon-on-insulator waveguides. Our superconducting single photon detector matrix includes detector designs optimized for high detection efficiency, low dark count rate, and high timing accuracy. As an example, we exploit the high timing resolution of a particularly short nanowire design to resolve individual photon round-trips in a cavity ring-down measurement of a silicon ring resonator.

Index Terms—Optical waveguides, quantum computing, silicon on insulator technology, superconducting photodetectors.

# I. INTRODUCTION

INTEGRATED SINGLE photon detectors are key components for enabling functionality in nanophotonics and on-chip quantum optical technology. In particular quantum information processing requires efficient interfacing of photonic circuitry with single photon detectors for scalable implementations [1]. On the one hand, optical waveguide technology is one of the most promising routes to build complex quantum optical systems on-chip [2], [3]. On the other hand, nanowire superconducting single photon detectors (SSPD) are emerging as the photon-counting technology best suited for integrated

Manuscript received October 12, 2012; accepted January 2, 2013. Date of publication January 11, 2013; date of current version February 15, 2013. This work was supported in part by the Packard Foundation and in part by a CAREER award from National Science Foundation.

C. Schuck and H. X. Tang are with the Department of Electrical Engineering, Yale University, New Haven, CT 06511 USA (e-mail: carsten.schuck@yale.edu; hong.tang@yale.edu).

W. H. P. Pernice was with Yale University, New Haven, CT 06511 USA. He is now with Karlsruhe Institute of Technology, D-76128 Karlsruhe, Germany (e-mail: wolfram.pernice@kit.edu).

O. Minaeva and A. V. Sergienko are with the Department of Electrical and Computer Engineering, Boston University, Boston, MA 02215 USA (e-mail: ominaeva@bu.edu; alexserg@bu.edu).

M. Li was with Yale University, New Haven, CT 06511 USA. He is now with the Department of Electrical and Computer Engineering, University of Minnesota, Minneapolis, MN 55455 USA (e-mail: moli@umn.edu).

G. Gol'tsman is with the Department of Physics, Moscow State Pedagogical University, Moscow 119992, Russia (e-mail: goltsman@rplab.ru).

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/TASC.2013.2239346

quantum information technology [4]. High timing accuracy, low noise and high sensitivity at telecom wavelengths show the potential to satisfy the demands of quantum technology [5].

Most of today's SSPDs are however designed for standalone operation and typically consist of a single detector device coupled to a single mode optical fiber [6], [7]. While the compatibility of quantum waveguide circuits and SSPDs has been successfully demonstrated [8] the coupling of photons from a chip to a separate detector limits the performance of this approach. More complex [9] or larger scale [10] nanophotonic networks thus require a complementary detector architecture—ideally embedded directly into the waveguide circuitry.

Here we present a grid of hundreds of nanowire SSPDs fully integrated with nanophotonic waveguide circuits on a silicon chip. One chip contains a large number of detector designs which can all be individually addressed and characterized. On the same chip we also implement various waveguide circuits which are scalable to photonic on-chip networks. This allows us to equip each circuit with application specific SSPD designs, optimized for particular detector benchmark parameters, e.g., detection efficiency, dark count rate, timing resolution, speed, etc.

To achieve small device footprint we fabricate the optical waveguides from silicon-on-insulator substrates. The high refractive index contrast of silicon waveguides on oxide substrate layers results in strong light confinement and thus allows for very compact circuit layouts.

The SSPDs are realized as NbN nanowires patterned directly on top of the waveguides. This traveling wave design [11], [12] allows for achieving very large interaction length of an incident photon with a nanowire. Traditional meander-type detectors absorb incident photons in a thin-film of a few nanometer height under normal incidence. In the travelling wave design instead, incoming light is coupled to the NbN-film along the length of the nanowire (tens of micrometers) leading to significantly increased absorption for much shorter overall wire length as compared to a meander-type SSPDs. The detection mechanism happens on picosecond timescales and is highly efficient [13]. In our case high photon absorption efficiency therefore directly translates to an increase in on-chip detection efficiency (OCDE).

Here we also show how to exploit the high timing accuracy of our detectors to observe ballistic photon transport in cavity

![](images/a76feb72dc4fcd019ec00b8506874bbf02551b6a20a2b8d1a46d752018fbd1d6.jpg)  
Fig. 1. (a) SSPD grid of NbN-nanowire detectors. An individual waveguide/ detector element of the matrix is shown in top and side view as an inset. It consists of three main components: (b) Grating couplers to guide light from an optical fiber into a Si-waveguide as also shown in the side-view, (c) a waveguide splitter to direct  $50\%$  of the light to the SSPD and the other half toward a reference output for detector calibration purposes, and (d) the NbN-nanowire SSPD (white), which absorbs incident photons traveling in a Si-waveguide (blue). The electrical output pulse is read out by engaging an RF probe to the electrode pads (yellow).

![](images/1e50ec403823d81443ebbc471ae8eb224ec8a6a87738467b021dfaf3bb3f309c.jpg)

![](images/4cf71fc8268db55f55c9f332cf7f86e6e87291ed1080fbdaf8463cedf717e215.jpg)

![](images/f83a401e9a0309939b24641374696a88bf8099e54420cea2b79168824ed0456a.jpg)

ring-down measurements. Variable photon delay on-chip, as demonstrated here with Si-microring resonators, has interesting applications in feed-forward schemes [14] and for photon number resolving detection [15].

# II. WAVEGUIDE INTEGRATED SSPD-MATRIX

# A. Device Layout

In our layout, a single chip accommodates 240 SSPDs organized in 20 columns and 12 rows of devices which can all be addressed individually. Fig. 1(a) shows an optical micrograph of a section of such a detector-grid. A single element of the SSPD-matrix used for detector characterization is shown as an inset in Fig. 1(a). It consists of three main components: optical grating couplers, balanced waveguide splitters and a nanowire SSPD, all connected by low-loss waveguides.

The optical grating couplers [Fig. 1(b)] are used to couple light from a fiber array into the single-mode waveguides on the chip and vice versa. By adjusting the grating period and filling factor we optimize the coupling efficiency for a given wavelength. On each chip we include up to five different grating coupler designs for center wavelengths in the  $1520 - 1570\mathrm{nm}$  range with a bandwidth of about  $30~\mathrm{nm}$  each. These grating couplers are optically reciprocal devices, i.e., the coupling loss at the input- and output ports is designed to be identical,

which we confirmed on separate calibration coupler devices. To confirm correct coupler operation all devices were prescreened and discarded in case they show transmission behavior deviating significantly from the set  $(>100)$  of reference calibration couplers. The coupler transmission of each individual device under test is then calibrated independently by using a reference output in every circuit. This calibration procedure is repeated for all measurement runs to precisely determine the number of photons propagating inside the waveguide towards the detector. A typical grating coupler shows a coupling loss of  $-13\mathrm{dB}$  at the wavelength of maximal transmission for this design.

We use a  $50:50$  waveguide splitter [Fig. 1(c)] to route the light in equal parts from the input to the reference output and the SSPD. Such splitter devices are a standard component of the nanophotonic toolbox and yield the desired intensities at the output within  $0.2\mathrm{dB}$  around  $1550~\mathrm{nm}$ . Both splitting ratio and splitter loss have previously been evaluated in Mach-Zehnder interferometers exhibiting interference with  $33\mathrm{dB}$  extinction and no discernible loss [16], [17].

The SSPD is a single U-shaped NbN-nanowire patterned directly on top of a waveguide [Fig. 1(d)]. Each end of the wire is connected via triangular NbN strips to large electrode pads. These pads are made of a  $200\mathrm{nm}$  gold layer on top of a  $5\mathrm{nm}$  Cr adhesion layer defined in an electron beam lithography step and subsequent lift-off process. Electrical contact with the electrodes is established via an RF probe to current bias the nanowire and for readout. In our SSPD-matrix we employ twelve different detector designs with varying nanowire widths  $(70 - 100\mathrm{nm})$  and total lengths  $(20 - 80\mu \mathrm{m})$ . For an absorption rate of  $1\mathrm{dB} / \mu \mathrm{m}$  of the U-shaped NbN thin-film on top of a Si-waveguide (determined in a separate transmission measurement with  $100\mathrm{nm}$  wire width) all detectors achieve long interaction length while maintaining small device footprint.

# B. Measurement Setup

Our measurement setup is illustrated in Fig. 2. Light from a tunable laser source or alternatively from a pulsed laser source is optically attenuated to provide a pre-determined photon flux. The optical attenuators are carefully calibrated both at typical laser output levels (0–10 dBm) using a calibrated photodetector as well as at single photon levels using a single-photon detector module (id200 by IDQ). The sample is mounted inside a He4-flow cryostat, which allows for reaching temperatures down to  $1.4\mathrm{K}$ . The attenuated light is coupled into the device using a single mode optical fiber array, which provides eight optical input/output ports for simultaneous excitation and readout. Light collected at the reference port is recorded with a calibrated photodetector. The number of photons arriving at the detector is then determined from the transmission through the device (grating coupler calibration at the reference port), taking into account the waveguide splitter and the external attenuation.

Electrical connection is established with a multi-contact RF probe. The nanowires are current-biased with a low-noise (battery-powered) current source. The recorded signal is amplified by two stages of electrical amplifiers and analyzed either

![](images/e89c8639c9d482e25583834311abaf3a2a8772605bc8c91394d30172f2a526f9.jpg)  
Fig. 2. Measurement setup. The sample is mounted in a liquid helium cryostat and can be optically and electrically addressed via a fiber array and an RF probe, respectively. The fabricated nanowire devices typically show a critical current of  $10.5\mathrm{K}$ . Optical part: continuous wave or picosecond-pulsed laser sources (optionally) launch light via calibrated, adjustable optical attenuators into the optical input of a liquid helium cryostat. The optical output is detected with a calibrated photo-detector; electrical part: a current source (battery powered) supplies the bias current for the SSPD; the output pulses (see oscilloscope inset) are amplified with broadband, low-noise amplifiers (LNA) and registered either with a high-bandwidth oscilloscope or a time correlated single photon counting system (TCSPC, PicoQuant).

with a time-correlated single photon counting module or a fast digital oscilloscope.

The fiber array and RF probe in our current setup allow us to simultaneously address two neighboring devices in the matrix at a time. Other devices are reached by repositioning the sample with respect to the fibers (RF probe) using low-temperature compatible translation stages. We are thus able to screen a large number of fabricated devices for their photon detection efficiency, dark count rate as well as their timing performance. Note that simultaneous operation of a larger number of devices on this chip can be achieved using existing RF-probes and fiber arrays with more elements.

Here we are mainly interested in the integration of highly efficient single photon detectors with optical waveguides. Hence, the main focus of our work lies on optimizing the coupling of light traveling inside a waveguide to the nanowire detector for efficient absorption as desired in fully integrated photonic circuit applications. The on-chip detection efficiency we measure here should therefore not be confused with the system detection efficiency usually quoted for stand-alone SSPDs. In case more efficient coupling from an optical fiber into the waveguide was desired it is possible to adapt our grating coupler design for higher efficiency (less than 1 dB loss) at the cost of a somewhat less robust fabrication procedure [18].

In our measurement configuration we do not detect appreciable levels of stray light with our detectors. To evaluate the influence of background light during measurement conditions we confirm that the detector count rate drops to the dark count level (i.e., no incident light) once the fiber array is displaced with respect to the grating couplers. Optical crosstalk between neighboring devices  $(250\mu \mathrm{m}$  separation) is analyzed by launching light into one device while monitoring

![](images/548f7d7e5c7ce31883bec2d5b506b1e77b9b45b9c1a1b7da7a45a92e653b68de.jpg)

![](images/b63895c1131a822760ae983ab77d68e240660d4e0062aafa0f8fa2b856964502.jpg)  
Fig. 3. Surface morphology of a NbN-nanowire detector on top of a Si-waveguide. SEM and AFM images: (a) a resist-covered NbN-nanowire of  $85\mathrm{nm}$  width is visible on top of a  $750\mathrm{-nm}$ -wide silicon waveguide; (b) zoom-in of the detector region where photons are incident on the U-shaped nanowire; (c) AFM scan of the deposited NbN thin-film showing RMS roughness of  $1.6\AA$ ; and (d) AFM image of a section of the nanowire detector protected by resist (HSQ).

![](images/30b439ff84c5cb8e3848ebf0af466442e3b3011a8c0f4385af4fb32b02285be2.jpg)

![](images/cf4ce16be092c91550851b7fb880b4cf143eac360e25cc926f33128b8a14a872.jpg)

the count rate of its neighboring detector which sees no input light otherwise. Again, no increase from the dark count level is observed unless the input power is increased by at least  $30~\mathrm{dB}$ . Stray light photons coupled into the substrate or reflected off the chip into the sample chamber only have a negligible chance to strike one of the detectors due to their tiny device footprints.

# III. DEVICE FABRICATION AND SURFACE MORPHOLOGY

Our devices are fabricated from silicon-on-insulator substrates (SOITEC) with a  $110\mathrm{nm}$  silicon top layer on a buried oxide layer of  $3\mu \mathrm{m}$  thickness. A  $3.5\mathrm{nm}$  NbN thin-film is then deposited on the wafer using DC magnetron sputtering. The electrode pads and alignment marks for subsequent layers are defined in a first electron beam lithography (ebeam) step using PMMA as a lift-off resist. In a second ebeam step we employ hydrogen silsesquioxane (HSQ) resist in  $3\%$  concentration to define the nanowire detectors with high resolution. Following the development we use carefully timed reactive ion etching (RIE) in CF4 chemistry to remove the exposed NbN thin-film without attacking the silicon layer underneath. In a third and final ebeam lithography step we then pattern the waveguide circuits using HSQ in  $6\%$  concentration. The resulting resist thickness is sufficient to hold up during the subsequent RIE and inductively coupled plasma etching step in a chlorine atmosphere.

The fabricated nanowire detectors are shown in Fig. 3. High-resolution scanning electron microscopy (SEM) images reveal an alignment accuracy better than  $50~\mathrm{nm}$  of the NbN-nanowire [85 nm wire width shown in Fig. 3(b)] on top of the  $750~\mathrm{nm}$  wide Si-waveguide. Note that the nanowire is buried under the HSQ masking layer which remained after etching. We inspect a large number of devices for wire uniformity and do not find lateral defects that are significant compared to the nanowire

![](images/22468f92d260a244d2c4fc066961e3dec1dde81e9e82d809dba8dd6d99003898.jpg)  
Fig. 4. Measured detection efficiency and dark count rate for a  $70\mathrm{-nm}$  -wide and  $80~\mu \mathrm{m}$  long detector device measured at 1.4, 1.64, and  $4\mathrm{K}$ . At  $1.64\mathrm{K}$ , we find a detection efficiency of  $88\%$  when the detector is biased close to  $I_{c}$ , which decreases to  $59\%$  at  $4\mathrm{K}$ .

dimensions. In order to assess the thickness uniformity of the film we perform high-resolution atomic force microscopy (AFM). As a reference we measure the surface roughness of the bare SOI-substrate and obtain an RMS value of  $1.1\AA$ . After sputter deposition we repeat the AFM scan [see Fig. 3(c)] and find an average RMS surface roughness of  $1.6\AA$  indicating that the NbN thickness variations do not exceed a few percent. The absolute value of the NbN film thickness  $(3.5 - 4\mathrm{nm})$  was determined from calibrated deposition rate measurements which were independently confirmed by transmission electron microscopy. Fig. 3(d) shows an AFM scan of a nanowire section after the second lithography step. A layer of HSQ resist protects the NbN thin film from degrading during subsequent nanofabrication steps. From the SEM and AFM inspections we conjecture that our NbN nanowires are highly uniform both in lateral and medial dimensions.

# IV. DETECTOR PERFORMANCE

An ideal nanowire SSPD should feature high detection efficiency, low noise, high speed and short timing jitter. However, often high performance in one of these disciplines comes at the cost of another. Here we have various detector geometries available within our SSPD-matrix to achieve a wide variety of performance characteristics. In this way different on-chip detector requirements can be optimally addressed by choosing the corresponding detector design: while quantum cryptography protocols require detectors with very low dark count rate, detector speed and efficiency may be a bigger concern in photon correlation experiments.

In Fig. 4 we present the results for a  $70~\mathrm{nm}$  wide and  $80~\mu \mathrm{m}$  long SSPD which has high performance in terms of on-chip detection efficiency reaching a maximum value of  $88\%$ $(+ / - 5.9\%)$  when operated at  $1.64\mathrm{K}$ . The error value reflects the uncertainty of the absolute photon number arriving at the detector considering the contributions from all external and on-chip photonic components. Due to its small wire width

the detector reaches high efficiency already when biased significantly below its critical current. This plateau behavior is characteristic of detectors with extremely narrow wires where the size of the hotspot originating from photon absorption approaches the nanowire width. In accordance with previous reports we here observe the onset of such a plateau at  $1.64\mathrm{K}$  for telecom wavelength photons (Fig. 4). A more pronounced plateau has only been observed with ultranarrow nanowires but not for wider nanowires [19]. Note, that the high absolute on-chip detection efficiency is a result of the travelling wave design used here, allowing for very efficient absorption of photons, rather than increased quantum efficiency.

In terms of dark count rate the performance of this device is reasonable with  $450\mathrm{Hz}$  at  $1.4\mathrm{K}$  when biased at  $99\%$  of the critical current. Lower rates are typically found in wider and shorter wires which however did not reach equally high detection efficiency (for comparison we report a  $85\mathrm{nm}$  wide,  $60~{\mu\mathrm{m}}$  long device with  $50\mathrm{Hz}$  dark count rate reaching  $55\%$  detection efficiency; not shown). We also examine the performance close to the LHe temperature at  $4\mathrm{K}$  and find the expected increase of dark count rate accompanied by a reduction of the on-chip detection efficiency to  $59\%$ .

Since this device is one of the longest ones in the matrix it has much higher kinetic inductance than shorter detectors resulting in a decay time of 1.4 ns. For high speed applications it will thus be advantageous to use the shortest detectors (20  $\mu$ m in total length) in the matrix reaching 455 ps decay time.

Furthermore, we characterize a large number of detectors in terms of critical current for the  $1.4\mathrm{K}$  to  $4\mathrm{K}$  temperature range. Generally high critical currents are desirable because it allows for operating the SSPD at higher bias current yielding higher output pulse amplitudes. Since the amplitude of the electrical noise is not affected by the bias current higher signal-to-noise ratios are achievable at high bias current. We estimate the critical current of nanowires with different wire widths by measuring their switching current. The results are shown in Fig. 5 where we also compare our devices to critical current values reported in the literature for state-of-the-art NbN-nanowire detectors. For our devices we observe high switching values which allow us to operate them in the high signal-to-noise regime where pulse discrimination is possible without sacrificing detection efficiency. Our results compare favorably with values measured in meander-type SSPDs which we attribute to the reduced length of our devices. The high observed critical current values also support our conjecture of high nanowire uniformity drawn in the previous section since constricted devices should switch to the normal state at lower bias currents.

Finally, the timing performance of our devices is discussed in the following section.

# V. ON-CHIP PHOTON DELAY

To demonstrate the potential of waveguide integrated SSPD grids for custom functionality we study on-chip photon delay. For this purpose our matrix includes SSPDs with particularly high timing accuracy at the output of microring resonator

![](images/5ab122bea482da7a9ce9b9e0d421ae48ab7d4b2c3e90712b566f4ed91a3badd8.jpg)  
Fig. 5. Typical critical current values measured for SSPDs with nanowire widths of 70, 85, and  $100\mathrm{nm}$  (green squares). For comparison, we plot critical current values for NbN-nanowire SSPDs reported in the literature (blue dots). For similar nanowire dimensions our devices generally show higher critical current values than previously reported meander-type devices.

![](images/40a218a1687ec7a5a1acd79b93db3119a967493caeb2ab9b9595664e4f0f9fc2.jpg)  
Fig. 6. (a) Setup for the ballistic photon transport measurement with single photon detectors. (b) Transmission spectrum of undercoupled and overcoupled ring resonators.

devices. We use these detectors to perform cavity ring-down measurements resolving individual photon round-trips. The measurement setup is shown in Fig. 6.

The microring resonators couple evanescently to the waveguide leading to the detection region. By varying the gap be

tween waveguide and cavity the optical coupling strength can be adjusted, allowing us to operate the ring in either the under- or overcoupled regime. Typical transmission spectra measured in the through port of the device are shown in Fig. 6(b), illustrating the features of whispering-gALLERY resonances with optical quality factors on the order of a few tens of thousands. The free-spectral range of the resonator is small, because the length of the ring was chosen as  $5.8\mathrm{mm}$  in order to provide a cavity roundtrip time exceeding the detector jitter.

# A. Jitter Measurement

In a first step we characterize the timing performance of a  $20\mu \mathrm{m}$  long,  $100\mathrm{nm}$  wide nanowire detector in a waveguide circuit similar to the one shown in Fig. 1. In order to resolve the intrinsic detector jitter we employ a picosecond pulsed laser (Pritel), a  $20\mathrm{GHz}$  bandwidth InGaAs photodetector (Agilent 83440) and a  $20\mathrm{GSa / s}$  digital oscilloscope with  $6\mathrm{GHz}$  real-time bandwidth (Agilent 54855A infiniium). As shown in Fig. 6, the pulsed laser output is split into two arms. The pulses in the upper arm are detected with the  $20\mathrm{GHz}$  detector to provide a reference to the oscilloscope. This trigger signal is then compared to the SSPD output pulses after detecting a photon from a strongly attenuated pulse coupled into the sample chip via the lower arm. Running the oscilloscope in histogram mode allows for jitter measurements with true picosecond time resolution. Using the  $20\mathrm{GHz}$  detector reference trigger as a start signal, the histogram is filled with stop signals triggered at the point of the maximum slope of the SSPD pulses ( $8\mu \mathrm{V / ps}$  before amplification). Using electrical amplifiers of more than  $10\mathrm{GHz}$  bandwidth we find a SSPD jitter value of  $18.4~\mathrm{ps}$  by fitting the histogram distribution with a Gaussian function. In this case the intrinsic instrument jitter is limited by the oscilloscope bandwidth of  $6\mathrm{GHz}$ .

# B. Cavity Ring-Down for Ballistic Photons

We then move on to a ring resonator device which allows us to examine its ring-down behavior in the time domain. Considering a resonator with a ring down time  $\tau_0$  larger than the pulse width  $T_{p}$  of the picosecond laser we have to treat the pulses as ballistic particles inside the resonator. Hence, the optical power circulating inside the cavity does not build up. A pulse of input intensity  $I_{\mathrm{in}}$  launched into the device will couple to the resonator and emerge in the through port as a train of pulses separated by the cavity round trip time, see Fig. 7. After passing the resonator the leading pulse will have an intensity  $I_0 = t^2 I_{\mathrm{in}}$ , where  $t$  is the transmission coefficient. Similarly, we can write the intensity of subsequent pulses emerging from the through port as  $I_{n} = (1 - t^{2})^{2}t^{2n - 2}e^{-\alpha nL}I_{\mathrm{in}}$ , where  $L$  is the cavity circumference and  $\alpha$  describes the linear absorption inside the cavity, which is small for high optical quality factor resonators.

To achieve the  $\tau_0 > T_p$  condition for the ballistic photon case, we utilize ring resonators with circumference of  $5.8\mathrm{mm}$  giving rise to round-trip time of 73 ps—larger than both the detector jitter of 18.4 ps and 1.2 ps laser pulse duration.

![](images/bf209e8e1c9800e3723eb274713bb7ed134f37e40c7cd75b70d47aa5a732251f.jpg)  
Fig. 7. Ballistic transport measurement. Top: ring resonator in the overcoupled case (100 nm gap); (a) time-domain trace of the transmission in the through port for the overcoupled case; (b) time-domain trace of the photons detected by the SSPD in the drop port for the overcoupled case. An exponential fit (purple) to the data (green) yields a decay time of 19 ps; (c) time-domain trace of the transmission in the through port for the undercoupled case; and (d) time-domain trace of the photons detected by the SSPD in the drop port for the undercoupled case. An exponential fit (red) to the data (blue) yields a decay time of 38 ps; Bottom: ring resonator in the undercoupled case (200 nm gap). The ring circumference is 5.8 mm, which corresponds to a photon round trip time of 73 ps.

We consider two cases, an undercoupled and an overcoupled resonator.

# C. Overcoupled Resonator

To realize the overcoupled case we launch the pulsed laser into a device with  $100\mathrm{nm}$  gap between the microring and the waveguides in the through and drop ports, see Fig. 7 (top). Here the transmission coefficient is small and the majority of the light is coupled from the feeding waveguide directly into the resonator. Hence, the leading pulse emerging from the through port has smaller amplitude than the first pulse coupled out after one round-trip [Fig. 7(a)].

The SSPD, with the same dimensions as the one used in the jitter measurement, is then employed to record the time-domain traces in the drop port. We bias the detector at  $86\%$  of the critical current which yields fair detection efficiency  $(15\%)$

at dark count rates below  $1\mathrm{Hz}$ . Fig. 7(b) shows the fast decay of photons in the ring resonator which are efficiently coupled out already after just one round-trip such that only two peaks are clearly discernible. A cavity decay time of 19 ps is extracted from an exponential fit to the data in the overcoupled case, corresponding to an optical quality factor of 11 900.

For comparison the optical quality factor of the resonator is also determined from optical transmission spectra recorded at the through port using a tunable laser source. The spectrum shown in Fig. 6 (b) (upper blue curve) exhibits optical resonance dips separated by a small free spectral range corresponding to the large ring circumference. A Lorentzian fit yields a quality factor of 14000 in good agreement with the value extracted from the cavity decay.

# D. Undercoupled Resonator

The undercoupled case is realized in a microring device with  $200\mathrm{nm}$  coupling gap such that less light is coupled from the feeding waveguide into the ring resonator, see Fig. 7 (bottom). Otherwise the measurement configuration is the same as before (Fig. 6). Here the transmission coefficient is large and most of the light is directly transmitted in the through port leading to large intensity of the leading pulse [Fig. 7(c)]. On the contrary the light which entered the cavity now decays much slower from the cavity and we observe longer pulse trains in the drop ports as shown in Fig. 7(d). The separation of the pulses again confirms the cavity round-trip time of 73 ps. An exponential fit to the four observed pulse fronts yields a cavity decay time of 38 ps for the undercoupled case, corresponding to an optical quality factor of 23 000.

For comparison we again record transmission spectra in the through port and find optical resonances with quality factors of 24000, in good agreement with the cavity decay time.

# VI. CONCLUSION

We have demonstrated a grid of SSPDs fully embedded with waveguide circuits on a silicon platform. Manufacturing waveguide integrated SSPDs in such large grids offers the possibility to use this platform as a test-bed for detector development as well as for photonic circuit characterization. Our chip contains a large variety of detector geometries and waveguide designs optimized for application specific functionality. The individually addressable detectors show optimal performance for example in terms of high on-chip detection efficiency (88%), or low dark count rate ( $< 100\mathrm{Hz}$ ), or high timing resolution ( $< 20~\mathrm{ps}$ ), or combinations thereof. The integration of nanophotonic circuits with large numbers of customizable detector designs on a scalable platform will allow for satisfying many of the needs of the quantum information and photonics community [1].

As an example how a photonic circuit can be optimally characterized using a tailor-made detector design we examined time-domain multiplexing in microring resonators. We resolve individual cavity round-trips of strongly attenuated optical pulses. We expect that reducing the propagation loss [20] brings on-chip photon buffering, feed-forward schemes [14] and photon number resolving detection [15], [21] within reach.

# REFERENCES

[1] J. L. O'Brien, "Optical quantum computing," Science, vol. 318, no. 5856, pp. 1567-1570, Dec. 2007.  
[2] A. Politi, J. C. F. Matthews, M. G. Thompson, and J. L. O'Brien, "Integrated quantum photonics," IEEE J. Sel. Topics Quantum Electron., vol. 15, no. 6, pp. 1673-1684, Nov./Dec. 2009.  
[3] C. Schaeff, R. Polster, R. Lapkiewicz, R. Fickler, S. Ramelow, and A. Zeilinger, "Scalable fiber integrated source for higher-dimensional path-entangled photonic quNits," Opt. Exp., vol. 20, no. 15, pp. 16 145-16 153, Jul. 2012.  
[4] R. H. Hadfield, "Single-photon detectors for optical quantum information applications," Nat. Photon., vol. 3, no. 12, pp. 696-705, Dec. 2009.  
[5] C. M. Natarajan, M. G. Tanner, and R. H. Hadfield, "Superconducting nanowire single-photon detectors: Physics and applications," Supercond. Sci. Technol., vol. 25, no. 6, pp. 063001-1-063001-16, Jun. 2012.  
[6] W. Slysz, M. Wegrzecki, J. Bar, P. Grabiec, M. Gorska, V. Zwiller, C. Latta, P. Bohi, I. Milostnaya, O. Minaeva, A. Antipov, O. Okunev, A. Korneev, K. Smirnov, B. Voronov, N. Kaurova, G. Gol'stman, A. Pearlman, A. Cross, I. Komissarov, A. Verevkin, and R. Sobolewski, "Fiber-coupled single-photon detectors based on NbN superconducting nanostructures for practical quantum cryptography and photon-correlation studies," Appl. Phys. Lett., vol. 88, no. 26, pp. 261113-1-261113-3, Jun. 2006.  
[7] A. Korneev, Y. Vachtomin, O. Minaeva, A. Divochiy, K. Smirnov, O. Okunev, G. Gol'tsman, C. Zioni, N. Chauvin, L. Balet, F. Marsili, D. Bitauld, B. Alloing, L. Li, A. Fiore, L. Lunghi, A. Gerardino, M. Halder, C. Jorel, and H. Zbinden, "Single-photon detection system for quantum optics applications," IEEE J. Sel. Topics Quantum Electron., vol. 13, no. 4, pp. 944-951, Jul./Aug. 2007.  
[8] C. M. Natarajan, A. Peruzzo, S. Miki, M. Sasaki, Z. Wang, B. Baek, S. Nam, R. R. H. Hadfield, and J. L. O'Brien, "Operating quantum waveguide circuits with superconducting single-photon detectors," Appl. Phys. Lett., vol. 96, no. 21, pp. 211101-1-211101-3, May 2010.  
[9] P. J. Shadbolt, M. R. Verde, A. Peruzzo, A. Politi, A. Laing, M. Lobino, J. C. F. Matthews, M. G. Thompson, and J. L. O'Brien, "Generating, manipulating and measuring entanglement and mixture with a reconfigurable photonic circuit," Nat. Photon., vol. 6, no. 1, pp. 45-49, Jan. 2012.  
[10] A. Peruzzo, M. Lobino, J. C. F. Matthews, N. Matsuda, A. Politi, K. Poulios, X.-Q. Zhou, Y. Lahini, N. Ismail, K. Wörhoff, Y. Bromberg, Y. Silberberg, M. G. Thompson, and J. L. O'Brien, "Quantum walks of correlated particles," Science, vol. 329, no. 5998, pp. 1500-1503, Sep. 2010.  
[11] X. Hu, C. W. Holzwarth, D. Masciarelli, E. A. Dauler, and K. K. Berggren, "Efficiently coupling light to superconducting nanowire single-photon detectors," IEEE Trans. Appl. Supercond., vol. 19, no. 3, pp. 336-340, Jun. 2009.

[12] J. P. Sprengers, A. Gaggero, D. Sahin, S. Jahanmirinejad, G. Frucci, F. Mattioli, R. Leoni, J. Beetz, M. Lerner, S. Hoefling, R. Sanjines, and A. Fiore, "Waveguide superconducting single-photon detectors for integrated quantum photonic circuits," Appl. Phys. Lett., vol. 99, no. 18, pp. 181110-1-181110-3, Oct. 2011.  
[13] G. N. Gol'tsman, O. Okunev, G. Chulkova, A. Lipatov, A. Semenov, K. Smirnov, B. Voronov, A. Dzardanov, C. Williams, and R. Sobolewski, "Picosecond superconducting single-photon optical detector," Appl. Phys. Lett., vol. 79, no. 6, pp. 705-707, Aug. 2001.  
[14] D. Bonneau, M. Lobino, P. Jiang, C. M. Natarajan, M. G. Tanner, R. H. Hadfield, S. N. Dorenbos, V. Zwiller, M. G. Thompson1, and J. L. O'Brien, "Fast path and polarization manipulation of telecom wavelength single photons in lithium niobate waveguide devices," Phys. Rev. Lett., vol. 108, no. 5, pp. 053601-1-053601-5, Feb. 2012.  
[15] A. Divochiy, F. Marsili, D. Bitauld, A. Gaggero, R. Leoni, F. Mattioli, A. Korneev, V. Seleznev, N. Kaurova, O. Minaeva, G. Gol'sman, K. G. Lagoudakis, M. Benkhaoul, F. Levy, and A. Fiore, "Superconducting nanowire photon-number-resolving detector at telecommunication wavelengths," Nat. Photon., vol. 2, no. 5, pp. 302-306, 2008.  
[16] M. Li, W. H. P. Pernice, C. Xiong, T. Baehr-Jones, M. Hochberg, and H. X. Tang, "Harnessing optical forces in integrated photonic circuits," Nature, vol. 456, no. 7221, pp. 480-484, Nov. 2008.  
[17] M. Li, W. H. P. Pernice, and H. X. Tang, "Tunable bipolar optical interactions between guided light waves," Nat. Photon., vol. 3, no. 8, pp. 464-468, Aug. 2009.  
[18] D. Taillaert, P. Bienstman, and R. Baets, "Compact efficient broadband grating coupler for silicon-on-insulator waveguides," Opt. Lett., vol. 29, no. 23, pp. 2749-2751, Dec. 2004.  
[19] F. Marsili, F. Najafi, E. Dauler, F. Bellei, X. Hu, M. Csete, R. J. Molnar, K. K. Berggren, F. Marsili, F. Najafi, E. Dauler, F. Bellei, X. Hu, M. Csete, R. J. Molnar, and K. K. Berggren, "Single-photon detectors based on ultranarrow superconducting nanowires," Nano Lett., vol. 11, no. 5, pp. 2048-2053, May 2011.  
[20] J. F. Bauters, M. J. R. Heck, D. D. John, J. S. Barton, C. M. Bruinink, A. Leinse, R. G. Heideman, D. J. Blumenthal, and J. E. Bowers, "Planar waveguides with less than 0.1 dB/m propagation loss fabricated with wafer bonding," Opt. Exp., vol. 19, no. 24, pp. 24090-24 101, Nov. 2011.  
[21] D. Achilles, C. Silberhorn, C. Sliwa, K. Banaszek, and I. A. Walmsley, "Fiber-assisted photon-number resolving detector," Opt. Lett., vol. 28, no. 23, pp. 2387-2389, Dec. 2003.