# On-chip quantum interference between silicon photon-pair sources

J. W. Silverstone<sup>1</sup>, D. Bonneau<sup>1</sup>, K. Ohira<sup>2</sup>, N. Suzuki<sup>2</sup>, H. Yoshida<sup>2</sup>, N. Iizuka<sup>2</sup>, M. Ezaki<sup>2</sup>, C. M. Natarajan<sup>3</sup>, M. G. Tanner<sup>4</sup>, R. H. Hadfield<sup>4</sup>, V. Zwiller<sup>5</sup>, G. D. Marshall<sup>1</sup>, J. G. rarity<sup>1</sup>, J. L. O'Brien<sup>1</sup> and M. G. Thompson<sup>1*</sup>

Large-scale integrated quantum photonic technologies $^{1,2}$  will require on-chip integration of identical photon sources with reconfigurable waveguide circuits. Relatively complex quantum circuits have been demonstrated already $^{1-7}$ , but few studies acknowledge the pressing need to integrate photon sources and waveguide circuits together on-chip $^{8,9}$ . A key step towards such large-scale quantum technologies is the integration of just two individual photon sources within a waveguide circuit, and the demonstration of high-visibility quantum interference between them. Here, we report a silicon-on-insulator device that combines two four-wave mixing sources in an interferometer with a reconfigurable phase shifter. We configured the device to create and manipulate two-colour (non-degenerate) or same-colour (degenerate) path-entangled or path-unentangled photon pairs. We observed up to  $100.0 \pm 0.4\%$  visibility quantum interference on-chip, and up to  $95 \pm 4\%$  off-chip. Our device removes the need for external photon sources, provides a path to increasing the complexity of quantum photonic circuits and is a first step towards fully integrated quantum technologies.

To date, most quantum waveguide circuits have been fabricated from glass-based materials, which offer low propagation loss, a wide transparency window and efficient coupling to optical fibre, but also limit device functionality and suffer from large circuit footprints. The silicon-on-insulator (SOI) photonics platform, recently developed for classical applications $^{10,11}$ , has several advantages over glass-based systems, including a high component density, a strong  $\chi^{(3)}$  optical nonlinearity, mature fabrication techniques, fast optical modulators $^{12}$  and compatibility with both  $1,550~\mathrm{nm}$  telecom optics and complementary metal oxide semiconductor (CMOS) electronics. As such, SOI quantum photonic circuits $^{13}$  and spontaneous photon-pair sources $^{14-18}$  have been developed recently.

Our SOI photonic device is presented in Fig. 1a. Inside the device are two photon-pair sources, each of which comprises a spiralled silicon waveguide  $5.2\mathrm{mm}$  long in which the  $\chi^{(3)}$  spontaneous four-wave mixing (SFWM) process is possible (region II, Fig. 1a). SFWM creates a signal-idler photon pair by annihilating two photons from a bright pump beam (Fig. 1b). Non-degenerate pairs are created by a single-wavelength pump, and degenerate pairs require a dual-wavelength scheme[19,20]. In our experiments, two amplified continuous-wave lasers produced the required pump field. Pump distribution and single-photon interference were achieved using  $2\times 2$  multimode interference (MMI) couplers (reflectivity  $\sim 50\%$ ), and a thermal phase shifter modified the

on-chip quantum and bright-light states. Off-chip wavelength-division multiplexers (WDMs) were used to separate the signal, idler and pump channels before the photon pairs were finally measured by two superconducting single-photon detectors (dark count rate  $1\mathrm{kHz}$ , gate width 650 ps).

Evolution of the degenerate quantum and bright-light states proceeded as follows (Fig. 1a, regions I-IV). The bright pump was split equally by the first MMI coupler (I) between the two sources (II). By operating in the weak pump regime (so that only one pair was likely to be generated), the simultaneous pumping of both sources yielded a path-entangled  $N00N$  state,  $(|20\rangle - |02\rangle) / \sqrt{2}$ . The relative phase was then dynamically controlled via a thermal phase shifter in one arm (III), which applied a  $\phi$  shift to the bright-light pump and a  $2\phi$  shift to the entangled biphoton state,  $(|20\rangle - e^{i2\phi}|02\rangle) / \sqrt{2}$ . Finally, the bright-light and biphoton states were interfered on a second MMI coupler (IV) to yield Mach-Zehnder interference fringes in the bright pump transmission, and half-period  $(\lambda/2$ -like) fringes[21] in the photon pair statistics, of the form

$$
| \Psi_ {\text {o u t}} \rangle = \cos \phi | \Psi_ {\text {b u n c h}} \rangle + \sin \phi | \Psi_ {\text {s p l i t}} \rangle \tag {1}
$$

Here, the  $|\Psi_{\mathrm{bunch}}\rangle$  state describes photons bunched together (coalesced) in either output mode  $A$  or  $B$ , and the  $|\Psi_{\mathrm{split}}\rangle$  state describes pair splitting, with one photon in each mode[20]. By considering the degenerate pair case, and specifically setting  $\phi = 0$  or  $\phi = \pi /2$ , we can obtain either state at the output:

$$
| \Psi_ {\text {o u t}} \rangle = \left\{ \begin{array}{l l} | \Psi_ {\text {b u n c h}} \rangle = \frac {1}{\sqrt {2}} (| 2 0 \rangle - | 0 2 \rangle), & \text {f o r} \phi = 0 \\ | \Psi_ {\text {s p l i t}} \rangle = | 1 1 \rangle , & \text {f o r} \phi = \frac {\pi}{2} \end{array} \right. \tag {2}
$$

When non-degenerate pairs are created, signal-idler exchange symmetry leads to identical quantum evolution and non-classical interference, as in equations (1) and (2). The corresponding  $|\Psi_{\mathrm{bunch}}\rangle$  and  $|\Psi_{\mathrm{split}}\rangle$  states for non-degenerate SFWM are:

$$
\left| \Psi_ {\text {b u n c h}} \right\rangle = \frac {1}{\sqrt {2}} \left(\left| 1 _ {s} 1 _ {i} \right\rangle_ {A} \left| 0 _ {s} 0 _ {i} \right\rangle_ {B} - \left| 0 _ {s} 0 _ {i} \right\rangle_ {A} \left| 1 _ {s} 1 _ {i} \right\rangle_ {B}\right) \tag {3}
$$

$$
\left| \Psi_ {\text {s p l i t}} \right\rangle = \frac {1}{\sqrt {2}} \left(\left| 1 _ {s} 0 _ {i} \right\rangle_ {A} \left| 0 _ {s} 1 _ {i} \right\rangle_ {B} + \left| 0 _ {s} 1 _ {i} \right\rangle_ {A} \left| 1 _ {s} 0 _ {i} \right\rangle_ {B}\right)
$$

where  $s$  and  $i$  indicate signal and idler wavelengths, respectively (for more detail, see Supplementary Section 4). We show experimentally

![](images/8e3b1d27b67c85e1b05c63767688734e2c5ec9422f8466e01803eadc22117494.jpg)  
a

![](images/20a778f2bc2e084933762aef3b709c0b02a102c811623eb550468562a6680b79.jpg)  
b  
Figure 1 | Mode of operation, mechanism of photon-pair generation and physical structure of the device. a, Schematic of device operation. A bright pump laser is coupled to the SOI chip using a lensed optical fibre and on-chip spot-size converters (not shown). The pump is distributed between two modes via a  $2 \times 2$  MMI coupler (I), and excites the  $\chi^{(3)}$  SFWM effect within each spiralled SOI waveguide source (II) to produce signal-idler photon pairs in the two-photon entangled state  $(|20\rangle - |02\rangle)/\sqrt{2}$ . The pairs are thermo-optically phase shifted  $(\phi, \mathrm{III})$  and interfered on a second coupler (IV) to yield either bunching or splitting over the two output modes, depending on  $\phi$ . b, Energy diagrams of both types of SFWM, showing the time-reversal symmetry between the non-degenerate and degenerate processes. c, SOI waveguide cross-section, with the thermal phase shifter on top.

![](images/544598c7485c51f8e99abfdb75c8726fda7f0e6108f5a4e156719ee7f56987f6.jpg)  
C

that these non-degenerate colour-entangled[22,23] states behave like degenerate pairs.

High-visibility quantum interference (the non-classical interference between two photons[24] on a beamsplitter) underpins all of photonic quantum information science and technology. Quantum interference within our device was quantified by the splitting and bunching probabilities at the output,  $P_{\mathrm{split}}$  and  $P_{\mathrm{bunch}}$ , as the on-chip phase  $(\phi)$  was varied; classical interference was observed in the transmission of the bright pump through the interferometer. First, we manipulated the on-chip path entanglement of the two-colour (non-degenerate) pairs. The experimental apparatus is pictured in Fig. 2a, and detailed in Supplementary Section 1. WDMs separated the monochromatic  $1,549.6 \mathrm{~nm}$  pump from the nondegenerate signal and idler photons (detuned by  $\delta = 6.4 \mathrm{~nm}$ ) such that signal-idler coincidences and pump transmission could be measured at the same time. Detector coincidences  $A_s \times B_i$  and  $B_s \times A_i$  were measured for  $P_{\mathrm{split}}$ , and  $A_s \times A_i$  and  $B_s \times B_i$  were measured for  $P_{\mathrm{bunch}}$ . The rates of classical transmission, as well as  $P_{\mathrm{split}}$  and  $P_{\mathrm{bunch}}$ , are recorded in Fig. 2b-d, respectively. In all cases, high-visibility interference was observed, and both the  $P_{\mathrm{split}}$  and  $P_{\mathrm{bunch}}$  two-photon fringes exhibited a phase doubling compared to their classical counterparts (a signature of path-entangled two-photon N00N states).

According to equation (1), the splitting rate should follow  $P_{\mathrm{split}} \propto \sin^2 \phi$  (curves, Fig. 2c). This model works well, with the data exhibiting net visibilities of  $99.1 \pm 0.5\%$  for  $A_i \times B_s$ , and  $98.8 \pm 1.2\%$  for  $A_s \times B_i$ , where we compute the visibility  $V = (N_{\mathrm{max}} - N_{\mathrm{min}}) / N_{\mathrm{max}}$  from the maximum,  $N_{\mathrm{max}}$ , and minimum,  $N_{\mathrm{min}}$ , values of each fit. The uncorrected visibilities for these measurements remained around  $96\%$  (all raw visibilities, including those for the following measurements, are listed in Supplementary Section 7). Meanwhile, for the bunching rate, equation (1) predicts  $P_{\mathrm{bunch}} \propto \cos^2 \phi$ , but instead an asymmetric behaviour is observed (Fig. 2d). This behaviour can be explained by considering spurious SFWM pairs in the device's

![](images/0fa8f7e8fcf5089e4af408e83d6527ee846c2080c409b26408d432009db47680.jpg)  
a

![](images/f93fe99177cec22133d810b792837192fff892ab9e195abcef5733ce15cd763c.jpg)

![](images/09bf8d8b3c6b7e196d7ca5eabbf5eeef3236120a63ba997313ae9337c96569fe.jpg)  
Figure 2 | On-chip quantum and classical interference measurements, varying the internal phase  $\phi$ . a, Apparatus showing the coupling of light from a bright pump laser into the device via fibre lenses, and the separation of signal (blue), idler (red) and pump (violet) wavelength channels using WDMs. b, Transmission of the bright pump laser shows classical interference. c, Measurement of signal-idler photon splitting between modes A and B, showing quantum interference. d, Measurement of signal-idler photon bunching, with signal and idler both in mode A or mode B. Fringe asymmetry arises from spurious SFWM pairs generated in the I/O waveguides (see text). e, Photon splitting as in b, but with monochromatic photon pairs, created via degenerate SFWM. Coincidence data have accidental coincidences subtracted.

input and output (I/O) waveguides, identical in cross-section to the source waveguides (Fig. 1c). We calculated corrected bunching probabilities,  $P_{\text{bunch}}^{A}$  and  $P_{\text{bunch}}^{B}$ , at the two output modes  $A$  and  $B$  as

$$
P _ {\text {b u n c h}} ^ {A} = \left| \left(\Gamma_ {0} + \Gamma_ {\mathrm {I} / \mathrm {O}}\right) \cos \phi \mp \Gamma_ {\mathrm {I} / \mathrm {O}} \right| ^ {2} \tag {4}
$$

where  $\Gamma_0$  is the base SFWM rate of the spiral sources, and  $\Gamma_{\mathrm{I/O}}$  quantifies the generation rate of spurious pairs inside the I/O waveguides (see Supplementary Section 5). Equation (4) describes the  $P_{\mathrm{bunch}}$  data well (curves in Fig. 2c). We extracted the spurious pair rate  $\Gamma_{\mathrm{I/O}}^2$ , and found that such pairs accounted for a small fraction of the total:  $\Gamma_{\mathrm{I/O}}^2 / \Gamma_0^2 = 2.5\%$  for  $P_{\mathrm{bunch}}^A$  and  $2.1\%$  for  $P_{\mathrm{bunch}}^B$ . As SFWM efficiency scales quadratically with interaction length  $(\Gamma^2 \propto L^2$ , see Supplementary Section 3), we compared these ratios with the I/O-to-source waveguide-length ratio squared,  $L_{\mathrm{I/O}}^2 / L_0^2 = 2.0\%$ , and found good agreement. The  $\Gamma_{\mathrm{I/O}}^2 / \Gamma_0^2$  ratio is of considerable importance—it measures the amount of  $|\Psi_{\mathrm{bunch}}\rangle$  contamination when the device is configured to produce only  $|\Psi_{\mathrm{split}}\rangle$ . In our experiments, spurious pairs limited the observable off-chip quantum interference visibility to  $V < 98\%$  (Supplementary Section 6). This noise could be suppressed by modifying the waveguide geometry outside the source regions or by moving to resonant sources[17].

To show how our  $|\Psi_{\mathrm{split}}\rangle$  pairs could be used in an external circuit, and to explore the implications of the colour entanglement of our non-degenerate pairs, we performed several off-chip Hong-Ou-Mandel-type (HOM) quantum interference measurements[25] for various values of the signal-idler detuning  $\delta$ . The modified apparatus is pictured in Fig. 3a. We configured the device to generate  $|\Psi_{\mathrm{split}}\rangle$  at the chip output (by setting  $\phi = \pi /2$ ), then sent one photon to a tunable delay line and the other to a polarization controller. Thus, the optical path and polarization of the two photons could be matched precisely, and we could introduce distinguishability in the arrival time degree of freedom. The photon pairs then interfered on a fibre beamsplitter  $(R = 50.2\%)$ , and we recorded coincidences as we varied the arrival time (via the free-space displacement,  $x$ ).

The phase-stable two-colour  $|\Psi_{\mathrm{split}} \rangle$  state yielded HOM interference fringes (Fig. 3b-d) that exhibited a beating between the nondegenerate signal and idler wavelengths[22,26] (with detuning  $\delta$ ). Owing to the colour entanglement present in  $|\Psi_{\mathrm{split}} \rangle$ , the filtered biphoton spectrum has two lobes, one lobe from each of the signal- and idler-channel filters (Fig. 3b-d insets). As the time-domain HOM interference pattern is effectively the Fourier transform of this spectrum, we can calculate the coincidence probability after the beamsplitter to be

$$
P _ {\mathrm {H O M}} = \frac {1}{2} - \frac {V}{2} \cos \left(2 \pi x \frac {\delta}{\lambda_ {\mathrm {p}} ^ {2}}\right) \operatorname {s i n c} \left(2 \pi x \frac {w}{\lambda_ {\mathrm {p}} ^ {2}}\right) \tag {5}
$$

where  $x$  is the delay displacement,  $\lambda_{\mathrm{p}}$  is the pump wavelength,  $w$  is the WDM channel width and  $\delta$  is the signal-idler channel spacing. As we tuned  $\delta \rightarrow 0$ , the beat frequency decreased (Fig. 3b-d), as predicted by equation (5). Off-chip HOM interference visibilities were measured for each value of  $\delta$ :  $V_{9.6\mathrm{nm}} = 94 \pm 4\%$ ,  $V_{6.4\mathrm{nm}} = 95 \pm 4\%$  and  $V_{3.2\mathrm{nm}} = 92 \pm 3\%$ . These results show that our device would perform well as an on-chip two-photon source.

Traditionally, multiphoton experiments have used degenerate photon pairs at (near) visible wavelengths in discrete spatial modes to allow arbitrary multipair interference[27]. As a route towards such experiments on a silicon chip at telecom wavelengths, we produced degenerate photons via degenerate SFWM (the time-reversed version of the non-degenerate process), which requires a two-colour pump (Fig. 1b; see Supplementary Section 1 for apparatus details). Using degenerate SFWM with a detuning of  $22.4\mathrm{nm}$  between the two pump wavelengths, we observed an on-chip

![](images/a2b0211d94fae994dcc2503f438134451ead0d8c4a8ec45e557e3c5fe2ce4482.jpg)

![](images/92dd4772276bf5f6dda71f5d7a16f9b14728b5c60799ea0c2e3c64a4621994ae.jpg)

Figure 3 | Off-chip HOM quantum interference measurements of  $|\Psi_{\mathrm{split}}\rangle$  
![](images/a6936d5bbc0ed9d449ae7d3a868c5afc7e47f2244d4459bf891bf656dac91b20.jpg)  
a, Experimental schematic: photon pairs in the  $|\Psi_{\mathrm{split}}\rangle$  state exit the chip, one is delayed by a displacement  $x$  and the other is polarization matched, and then the pair is interfered on a beamsplitter. Two detectors measure coincidences at different signal-idler detunings  $\delta$ . b, Detuning  $\delta = 9.6 \mathrm{~nm}$ . c, Detuning  $\delta = 6.4 \mathrm{~nm}$ . d, Detuning  $\delta = 3.2 \mathrm{~nm}$ . e. Degenerate SFWM, no detuning. Beating within each fringe is explained by the signal-idler detuning,  $\delta$ , as plotted in insets to b-e. Coincidence data have accidental coincidences subtracted. Error bars are Poissonian, based on raw coincidences.

quantum interference fringe with  $V = 100.0 \pm 0.4$  (Fig. 2e), and measured off-chip HOM interference with  $V = 95 \pm 4\%$  (Fig. 3e). The oscillation-free HOM fringe corresponded to equation (5) with  $\delta = 0$ .

Using both degenerate and non-degenerate SFWM, we observed high-visibility quantum interference, both on- and off-chip (Figs 2 and 3). We observed visibilities on-chip higher than those measured off-chip, and two explanations are, first, as mentioned, the off-chip visibility was limited by spurious pair generation in the I/O waveguides, and second, the HOM interference measurements required both the on-chip phase and the off-chip polarization to be controlled precisely, and drifts in both parameters reduced the visibility. Regardless, the HOM visibilities were still high, and we consider that the even higher on-chip visibilities show great promise for future high-fidelity $^{28}$  source-circuit integrations.

Despite these high visibilities, the measured count rates were low because of poor system efficiency (see Methods) and low source brightness. To extract the source brightness, we examined an isolated spiral waveguide: we measured  $2.7 \pm 0.4 \mathrm{kHz} \mathrm{~nm}^{-1} \mathrm{mW}^{-2}$  for non-degenerate pairs, and a similar  $2.5 \pm 0.6 \mathrm{kHz} \mathrm{~nm}^{-1} \mathrm{mW}^{-2}$  for degenerate pairs, per units bandwidth and launched power. Corresponding coincidence-to-accidental ratios were 290 and 45 (at  $100 \mathrm{kHz}$  generation rates, see Supplementary Section 2). Brightness can be improved by further engineering our spiral sources, that is optimizing the spiral length, or moving to resonant[17,29] or slow-light[18] SFWM enhancement. Even with the current brightness, though, we have shown that our device can fill the on-chip role that external crystal- or fibre-based sources have taken traditionally.

Scalability is the ultimate goal for any integrated quantum system. Bulk crystal spontaneous pair sources have been used successfully in the largest optical quantum information experiments to date[27], including the production[30] and manipulation[31] of eight-photon entanglement. These spontaneous sources can, in principle, be scaled beyond this eight-photon limit by using the techniques of active multiplexing and feed forward[32,33]. These schemes will require integrated fast switches, single-photon detectors, a high system efficiency and many identical and bright on-chip photon-pair sources. We have shown that two identical SFWM sources can be integrated monolithically in a waveguide circuit and made to interfere with high visibility. This takes us one step closer to integrated quantum circuits capable of generating and manipulating large photonic states.

# Methods

System efficiency. Using the quadratic non-degenerate SFWM power dependence, we can extract the on-chip SFWM rate, together with the associated channel efficiencies,  $\eta_{s}$  and  $\eta_{i}$ , where

$$
\eta_ {s} = \frac {R _ {\mathrm {C C}}}{R _ {\mathrm {i}}} = - 2 4. 2 \mathrm {d B}, \quad \text {a n d} \quad \eta_ {i} = \frac {R _ {\mathrm {C C}}}{R _ {\mathrm {s}}} = - 2 5. 5 \mathrm {d B}
$$

and  $R_{\mathrm{CC}}$ ,  $R_{\mathrm{i}}$  and  $R_{\mathrm{s}}$  are, respectively, the coincidence, idler channel and signal channel rates. These values quantify the total loss experienced by a photon from its generation to detection at detector  $s$  or  $i$ , respectively. Both detector efficiencies were measured at  $8\%$  (-11.00 dB). From a cut-back measurement on the same wafer we estimate the propagation loss as  $4.1~\mathrm{dB~cm}^{-1}$ , although much lower loss is possible[34]. Using  $\eta_{s}$  and  $\eta_{l}$ , and bright-light measurements, we calculated the combined MMI and facet loss as  $7.3~\mathrm{dB}$ . We were unable to separate the MMI losses from those of the facet, although very low-loss MMI designs exist[35].

Optical apparatus. We used two continuous-wave tunable lasers to generate the required pump field (one or two colours). These lasers were amplified by an erbium-doped fibre amplifier to produce a total power of  $80\mathrm{mW}$  (in the two-colour case, this was divided between two spectral peaks), then filtered (50 dB extinction) and the remaining  $15\mathrm{mW}$  was edge-coupled onto the chip using  $2.5\mu \mathrm{m}$  beam-waist lensed fibres and on-chip polymer spot-size converters. Fibre alignment was maintained using piezo-controlled feedback on the bright pump transmission. Filtering was used to both clean the pump before the chip and to separate the pump from the single photons afterwards (see Supplementary Section 1 for further details).

Off-chip HOM fringe optimization. The apparatus was configured as in Fig. 3a. We used the interferometer, formed between the chip and the fibre beamsplitter, to determine the zero path length difference point on the free-space delay. We input amplified noise to this interferometer, and observed white-light fringes as we varied the delay, with fringe maxima at the zero-difference point (and also the HOM fringe centre). Then, we optimized the polarization controller using the classical fringe visibility.

Electrical apparatus. An electrical probe was used to interface electrically between the chip and an ultra low noise d.c. power supply. We applied voltages up to  $2.3\mathrm{V}$  to our thermo-optic phase modulator, for a maximum load of  $36\mathrm{mA}$ . Similar devices exhibited fuse voltages around  $2.7\mathrm{V}$ . We correlated electrical power with thermo-optic phase, with good results (Fig. 2b, Supplementary Fig. 3).

Device fabrication. The silicon nanowire waveguides were fabricated from a SOI wafer with a  $220\mathrm{nm}$  slab thickness. The waveguides were designed to be single moded, having a width of  $470\mathrm{nm}$  with a silicon dioxide upper cladding. I/O coupling was achieved using spot-size converters that comprised a  $300\mu \mathrm{m}$  long inverse taper with a  $200\mathrm{nm}$  wide tip beneath a  $4\times 4\mu \mathrm{m}^2$  polyimide waveguide. Structures were defined by deep ultraviolet photolithography  $(248~\mathrm{nm})$  and dry etching.

Received 30 May 2013; accepted 12 November 2013; published online 15 December 2013

# References

1. O'Brien, J. L., Furusawa, A. & Vuckovic, J. Photonic quantum technologies. Nature Photon. 3, 687-695 (2009).  
2. Tanzilli, S. et al. On the genesis and evolution of integrated quantum optics. Las. Photon. Rev. 1, 115-143 (2012).  
3. Peruzzo, A. et al. Quantum walks of correlated photons. Science 329, 1500-1503 (2010).  
4. Shadbolt, P. J. et al. Generating, manipulating and measuring entanglement and mixture with a reconfigurable photonic circuit. Nature Photon. 6, 45-49 (2012).  
5. Metcalf, B. J. et al. Multiphoton quantum interference in a multiport integrated photonic device. Nature Commun. 4, 1356 (2013).  
6. Tillmann, M. et al. Experimental boson sampling. Nature Photon. 7, 540-544 (2013).  
7. Crespi, A. et al. Anderson localization of entangled photons in an integrated quantum walk. Nature Photon. 7, 322-328 (2013).  
8. Matsuda, N. et al. A monolithically integrated polarization entangled photon pair source on a silicon chip. Sci. Rep. 2, 817 (2012).  
9. Martin, A., Alibart, O., DeMicheli, M. P., Ostrowsky, D. B. & Tanzilli, S. A quantum relay chip based on telecommunication integrated optics technology. New J. Phys. 14, 025002 (2012).  
10. Soref, R. The past, present, and future of silicon photonics. J. Sel. Top. Quant. Electron. 12, 1678-1687 (2006).  
11. Sun, J., Timurdogan, E., Yaacobi, A., Hosseini, E. S. & Watts, M. R. Large-scale nanophotonic phased array. Nature 493, 195-199 (2013).  
12. Reed, G. T., Mashanovich, G., Gardes, F. Y. & Thomson, D. J. Silicon optical modulators. Nature Photon. 4, 518-526 (2010).  
13. Bonneau, D. et al. Quantum interference and manipulation of entanglement in silicon wire waveguide quantum circuits. New J. Phys. 14, 045003 (2012).  
14. Sharping, J. E. et al. Generation of correlated photons in nanoscale silicon waveguides. Opt. Express 14, 12388-12393 (2006).  
15. Clemmen, S. et al. Continuous wave photon pair generation in silicon-on-insulator waveguides and ring resonators. Opt. Express 17, 16558-16570 (2009).  
16. Takesue, H. et al. Generation of polarization entangled photon pairs using silicon wire waveguide. Opt. Express 16, 5721-5727 (2008).  
17. Azzini, S. et al. Ultra-low power generation of twin photons in a compact silicon ring resonator. Opt. Express 20, 23100-23107 (2012).  
18. Xiong, C. et al. Slow-light enhanced correlated photon pair generation in a silicon photonic crystal waveguide. Opt. Lett. 36, 3413-3415 (2011).  
19. Garay-Palmett, K., U'ren, A., Rangel-Rojo, R., Evans, R. & Camacho-López, S. Ultrabroadband photon pair preparation by spontaneous four-wave mixing in a dispersion-engineered optical fiber. Phys. Rev. A 78, 043827 (2008).  
20. Chen, J., Lee, K. F. & Kumar, P. Deterministic quantum splitter based on time-reversed Hong-Ou-Mandel interference. Phys. Rev. A 76, 031804(R) (2007).  
21. Matthews, J. C. F., Politi, A., Stefanov, A. & O'Brien, J. L. Manipulation of multiphoton entanglement in waveguide quantum circuits. Nature Photon. 3, 346-350 (2009).  
22. Rarity, J. G. & Tapster, P. R. Two-color photons and nonlocality in fourth-order interference. Phys. Rev. A 41, 5139-5146 (1990).  
23. Ramelow, S., Ratschbacher, L., Fedrizzi, A., Langford, N. K. & Zeilinger, A. Discrete tunable color entanglement. Phys. Rev. Lett. 103, 253601 (2009).  
24. Pittman, T. et al. Can two-photon interference be considered the interference of two photons? Phys. Rev. Lett. 77, 1917-1920 (1996).

25. Hong, C. K., Ou, Z. Y. & Mandel, L. Measurement of subpicosecond time intervals between two photons by interference. Phys. Rev. Lett. 59, 2044-2046 (1987).  
26. Ou, Z. Y. & Mandel, L. Observation of spatial quantum beating with separated photodetectors. Phys. Rev. Lett. 61, 54-57 (1988).  
27. Pan, J-W. et al. Multiphoton entanglement and interferometry. Rev. Mod. Phys. 84, 777-838 (2012).  
28. Laing, A. et al. High-fidelity operation of quantum photonic circuits. Appl. Phys. Lett. 97, 211109 (2010).  
29. Azzini, S. et al. Stimulated and spontaneous four-wave mixing in silicon-on-insulator coupled photonic wire nano-cavities. Appl. Phys. Lett. 103, 031117 (2013).  
30. Yao, X.-C. et al. Observation of eight-photon entanglement. Nature Photon. 6, 225-228 (2012).  
31. Yao, X.-C. et al. Experimental demonstration of topological error correction. Nature 482, 489-494 (2012).  
32. Ma, X.-S., Zotter, S., Kofler, J., Jennewein, T. & Zeilinger, A. Experimental generation of single photons via active multiplexing. Phys. Rev. A 83, 043814 (2011).  
33. Mower, J. & Englund, D. Efficient generation of single and entangled photons on a silicon photonic integrated chip. Phys. Rev. A 84, 052326 (2011).  
34. Gnan, M., Thoms, S., Macintyre, D., De La Rue, R. M. & Sorel, M. Fabrication of low-loss photonic wires in silicon-on-insulator using hydrogen silsesquioxane electron-beam resist. *Electron. Lett.* 44, 115-116 (2008).  
35. Sheng, Z. et al. A compact and low-loss MMI coupler fabricated with CMOS technology. IEEE Photon. J. 4, 2272-2277 (2012).

# Acknowledgements

We thank A. Politi for useful discussions, and F. Melloti for experimental assistance. This work was supported by the Engineering and Physical Science Research Council (UK), the European Research Council, the Bristol Centre for Nanoscience and Quantum Information, the European FP7 project QUANTIP and the European FP7 project BBOI. J.W.S. acknowledges support from the Natural Sciences and Engineering Research Council of Canada. R.H.H. acknowledges a Royal Society University Research Fellowship. V.Z. acknowledges support from the Dutch Foundation for Fundamental Research on Matter. G.D.M. acknowledges the FP7 Marie Curie International Incoming Fellowship scheme. J.L.O'B. acknowledges a Royal Society Wolfson Merit Award and a Royal Academy of Engineering Chair in Emerging Technologies. M.G.Th. acknowledges support from the Toshiba Research Fellowship scheme.

# Author contributions

J.W.S. and D.B. contributed equally to this work. J.W.S., D.B., J.G.R., J.L.O'B. and M.G.Th. conceived and designed the experiments. J.W.S., D.B. and M.G.Th. analysed the data. K.O., N.S., H.Y., N.I. and M.E. fabricated the device. R.H.H., V.Z., C.M.N. and M.G.Ta. built the single-photon detector system. J.W.S., D.B. and G.D.M. performed the experiments. J.W.S., D.B., G.D.M., J.G.R., J.L.O'B. and M.G.Th. wrote the manuscript.

# Additional information

Supplementary information is available in the online version of the paper. Reprints and permissions information is available online at www.nature.com/reprints. Correspondence and requests for materials should be addressed to M.G.Th.

# Competing financial interests

J.W.S., D.B., J.L.O'B. and M.G.Th. declare UK patent application number 1302895.6.