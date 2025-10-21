# Chip-scale simulations in a quantum-correlated synthetic space

Received: 14 November 2022

Accepted: 19 May 2023

Published online: 22 June 2023

![](images/dd8c6eed6c90c60be56e6c9bb1a867f2209263b7ce4fefd0dc11af1bcd372cd9.jpg)

Check for updates

Usman A. Javid  $①$ , Raymond Lopez-Rios $^{1}$ , Jingwei Ling  $②$ , Austin Graf $^{1}$ , Jeremy Staffa  $①$  & Qiang Lin $^{1,2}$

An efficient simulator for quantum systems is one of the original goals for the efforts to develop a quantum computer. In recent years, synthetic dimensions in photonics have emerged as a potentially powerful approach for simulation that is free from the constraint of geometric dimensionality. Here we demonstrate a quantum-correlated synthetic crystal that is based on a coherently controlled broadband quantum frequency comb produced in a chip-scale, dynamically modulated lithium niobate microresonator. The time-frequency entanglement inherent with the comb modes greatly extends the dimensionality of the synthetic space, creating a massive, nearly  $400 \times 400$  synthetic lattice with electrically controlled tunability. With such a system, we are able to utilize the evolution of quantum correlations between entangled photons to perform a series of simulations, demonstrating quantum random walks, Bloch oscillations and multilevel Rabi oscillations in the time and frequency correlation space (demonstrated in a  $5 \times 5$  mode subspace). The device combines the simplicity of monolithic nanophotonic architecture, high dimensionality of a quantum-correlated synthetic space and on-chip coherent control, which opens up an avenue towards chip-scale implementation of large-scale analogue quantum simulation and computation in the time-frequency domain.

Despite decades of effort, a fully configurable and error-corrected optical quantum computer remains out of reach. The non-interacting nature of photons, weak nonlinearities and unavoidable losses prevent efficient implementation of logic gates and protocols for fault-tolerant computation. However, it is still possible to achieve a quantum advantage in simulation using non-interacting particles, even in the presence of noise and loss $^{1,2}$ . Such intermediate-scale machines are specifically designed to simulate one physical system, sacrificing universality much like an analogue computer. To that end, linear optical circuits have been widely implemented $^{3-12}$ , where the position or path information of photons is employed for the simulation. This approach, however, faces challenges in scaling up for simulating complex problems, which require ever-increasing physical space (sometimes needing hundreds of elements with both optical and electrical interconnects $^{12-14}$ ) that would

impose impractical requirements on the fabrication and its precision of the underlying photonic integrated circuits.

An alternate approach harnesses a so-called synthetic dimension. The frequency space is a good example of this<sup>15</sup>. Here the simulation runs on photons moving between distinct frequency modes, all of which can occupy the same physical space, for example, a spatial mode of a cavity. Increasing the dimensions of the system requires a minimal increase in the complexity of the architecture. Furthermore, the frequency domain provides a complete equivalent to linear optical quantum computing (LOQC)<sup>16</sup>, with all operations available through frequency-mixing interactions. Investigations on these synthetic spaces have recently attracted considerable interest due to their potential for simulating a variety of condensed-matter phenomena and topological effects<sup>17-23</sup>. The experimental implementations have so far

$^{1}$ Institute Of Optics, University of Rochester, Rochester, NY, USA.  $^{2}$ Department of Electrical and Computer Engineering, University of Rochester, Rochester, NY, USA.  $\times$  e-mail: qiang.lin@rochester.edu

![](images/275bb220deb7dc0707b0d58d2e5e6ef33cecd0b44959030cb1fd8dd86b874a5a.jpg)  
Fig. 1 | Concept of a quantum-correlated synthetic crystal. a–d, A nanophotonic lithium niobate racetrack resonator (a). The synthetic lattice is constructed in two steps. First a periodically poled region in the resonator generates pairs of time–frequency entangled photons within a frequency comb, creating the nodes of the synthetic lattice (b). An electro-optic modulator directly  
embedded inside of the resonator then creates coupling within the comb lines forming a tight-binding lattice for each photon (c). Combining these two effects creates a 2D quantum-correlated synthetic lattice (d). The grey shaded area is to illustrate movement of spectral correlations in the lattice.

been limited to the classical regime, where light from a laser populates the synthetic frequency lattice $^{24-35}$ . Simulations based on non-classical light, however, would provide unique insights into transport phenomena at the quantum scale $^{36,37}$  and bring advantages offered by quantum mechanics that are inaccessible to classical simulation spaces $^{23,38-41}$ . The primary challenge lies in producing a synthetic space that is capable of generating quantum states of light while simultaneously being able to coherently control their evolution depending on the specific simulation problem. In particular, realization of such a synthetic space on a chip-scale platform would offer tremendous benefits in resource efficiency, system scalability and operational stability $^{12}$ , which are challenging for table-top systems $^{24-33}$ .

Here we demonstrate an on-chip quantum-correlated synthetic crystal that is characterized by non-classical correlations between lattice sites. Such a crystal greatly extends the dimensionality of the synthetic space via quantum correlations inherent with energy-time entangled photons, in contrast to the sole frequency degree of freedom that is available in the classical regime $^{24-35}$ . We implement this concept using a coherently controlled quantum optical frequency comb (QOFC) composed of  $\sim 800$  single-photon comb modes, produced inside of a dynamically modulated thin-film lithium niobate microresonator. The time-frequency entanglement associated with the spontaneous parametric down-conversion (SPDC) process introduces long-range quantum correlations between the signal and idler frequency combs, whereas an electro-optic modulation implemented within the QOFC generation process produces nearest-neighbour coupling, eventually creating a tight-binding quantum-correlated synthetic crystal (Fig. 1).

With such a system, we are able to utilize the evolution of the generated quantum correlations to perform a series of simulations in the time and frequency correlation space created by the entangled photons. We demonstrate two-particle quantum random walks simulated on the biphoton spectral correlation space. We further simulate Bloch oscillations of an electron in a crystal lattice in the presence of

an external gauge potential, on the biphoton temporal correlation space. Finally, we drive the lattice sites into the strong coupling regime and observe multilevel Rabi oscillations where adjacent lattice sites exchange energy faster than the lifetime of photons inside of the resonator. Although these simulations represent well-understood phenomena, this proof-of-principle experiment demonstrates the versatility of the device for performing diverse simulations. The considerable scalability of the quantum-correlated synthetic space—together with the electrically controlled tunability, dispersion-engineering flexibility and simplicity of the nanophotonic architecture—opens a path towards running complex large-scale simulations and computations for near-term analogue quantum simulators.

# Results

# Device design and the synthetic space

Figure 1 shows the schematic of the device concept. The synthetic lattice is formed by the frequency modes of an optical cavity containing both a QOFC generator and a high-speed phase modulator. Experimentally, we implement this system on a nanophotonic lithium niobate chip with a racetrack resonator (Fig. 1a). There are three design requirements to be able to run simulations in this space. First, the entire synthetic space has to be able to be populated with quantum light, which is realized by dispersion engineering the resonator geometry for broadband SPDC $^{42}$ . A section of the resonator is periodically poled to match the refractive index gap between the pump frequency and the frequency of the generated photons. This creates a biphoton frequency comb that forms the skeleton for our synthetic space (Fig. 1b). Second, we establish a tight-binding crystal by implementing nearest-neighbour coupling with frequency modulation. For this we place a pair of electrodes designed to operate at microwave frequencies (Fig. 1c). When the material refractive index is modulated at a frequency that matches the free spectral range (FSR) of the cavity, light can scatter to adjacent modes using sum and difference frequency interactions, creating a

![](images/0f9372558d702e90c8b824bbb55b2816803d4995f4df400721420eb3e6c0637c.jpg)  
a

![](images/96dac50d7bf7ddbe45d981d5a4f6ea52fbbf817cf9ed2323e1317418bee7e393.jpg)

![](images/1240db5616ac9ec55f0874df28581ae1d56bd24573a34f93734e5e1f7790b14d.jpg)  
b

![](images/ff8b3eb0a2a7702c4175596a88919c987f1e172c16d8d15b779cb96e27b78f89.jpg)  
C  
Wavelength (nm)

![](images/6b0440af89e8028e671d8d45b7085bdbbd3f44e336cd24ebc14b69df569db7e9.jpg)  
d  
Fig. 2 | Characterization of the biphoton QOFC. a, Microscope image of a fabricated device, where I, II and III indicate a section of the embedded electro-optic modulator, the periodically poled waveguide region for QOFC generation, and the pulley coupling waveguide for broadband external coupling, respectively. b, Schematic showing the correlation measurement where the spectral correlation of the photon pairs is performed by scanning a pair of single-photon detectors through the comb modes and counting the coincidence events with a time correlator. c, Recorded spectrum of produced QOFC in blue, showing discrete comb modes lighting up with a 50 GHz mode spacing (inset) when pumped at a resonance at  $776~\mathrm{nm}$ . The detector cuts off at  $189\mathrm{THz}$ $(1,590\mathrm{nm})$  preventing spectral measurement at longer wavelengths. We estimate that the  
comb spectrum reaches  $\sim 1,800\mathrm{nm}$  on the longer wavelength side, as indicated by the left-most vertical dashed line. The spectrum is also measured at another resonance at  $780\mathrm{nm}$ , detuned away from the phase-matching wavelength to obtain a baseline. d,e, Coincidence histogram (d) for different signal-idler mode pairs, each of which has signal and idler frequencies equally spaced from the the centre of the generated spectrum. Strong coincidences are measured due to energy conservation of signal-idler photon pairs in the SPDC process. This presents as a bright diagonal in a 2D JSI plot (e). When the detectors are aligned to off-diagonal mode pairs, there are no measurable coincidences as expected from a pure SPDC process.

![](images/e31f6282e80b948110dae7305d796ce3e21aed27b89edaa97b8d82222391d1be.jpg)  
e

tight-binding system with a coupling strength determined by the modulation depth. This effect has been recently used to produce electro-optic frequency combs with a laser input $^{43-45}$ . Here, however, it is used to couple quantum frequency modes, which creates a 2D synthetic space for running simulations with the dimensions created by the chain of resonances formed by the signal and idler photons as shown in Fig. 1d (see Supplementary Section I for a detailed theoretical treatment). This space is unique as it uses both classical and quantum correlation from frequency modulation and SPDC, respectively, to create a lattice, and is therefore capable of investigating both classical and quantum simulation phenomena. Finally, we must be able to couple light out of each mode of the resonator with the same efficiency for the entire bandwidth of the lattice. This is implemented by using a coupling waveguide with an optimized wrap-around geometry placed aside with the resonator (see Supplementary Section II for details).

With this design, the device is fabricated on a thin-film lithium niobate chip. Figure 2a shows a microscope image of a fabricated device. The resonator modes in the telecom wavelength region are critically coupled with an intrinsic quality factor of  $10^{6}$ . For the pump wavelengths in the near-infrared region, the modes have an intrinsic

quality factor of  $3 \times 10^{5}$  and an external quality factor of  $1.5 \times 10^{6}$ . The Methods section provides details on device fabrication, whereas Supplementary Section II presents a characterization of its linear properties. When the device is pumped at a resonance at  $776\mathrm{nm}$ , we obtain a broadband QOFC in the telecom band, with a 3 dB half-width of  $19.5\mathrm{THz}$  centred at  $1,552\mathrm{nm}$  (Fig. 2c) and  $50\mathrm{GHz}$  mode spacing (see inset). Due to the detector's cutoff wavelength at  $1,590\mathrm{nm}$ , we only have access to the signal (blue) side of the spectrum. However, the energy conservation constraint of the SPDC process implies that the spectral extent of the comb should be symmetric around its centre wavelength, which infers a 3 dB spectral bandwidth of  $39\mathrm{THz}$  containing approximately 780 modes of the resonator. This provides a massive higher-dimensional space to construct a synthetic crystal for simulations or computational experiments, utilizing coherent control of the comb lines implemented directly within the generation process, which has been inaccessible in other quantum frequency comb platforms[46]. To verify that the photons are indeed produced through SPDC, we detune the laser to a resonance at  $780\mathrm{nm}$ , away from the phase-matching wavelength. The data obtained show that the spectrum is quenched within this bandwidth, demonstrating that there are no

![](images/7ba3a4bf43683e6a1cfa3d72152e5c506d8c1961f134429d8af6b7f03924678b.jpg)  
Fig. 3 | Quantum random walk of correlated photons in the synthetic lattice. a, The microwave signal frequency  $\Omega$  is tuned to match the FSR of the resonator at  $50\mathrm{GHz}$ , and the modulation amplitude  $V_{0}$  is varied. b-f, Measured JSI of the photon pairs in a  $5\times 5$  mode space for increasing microwave signal amplitude with the signal modes on the  $x$ -axis and the idler modes on the  $y$ -axis.  
The bar plots below the JSI show the values along the secondary diagonal of the matrices indicating the spread of the JSI. g, The s.d. of the random walk for each modulation amplitude along with a linear fit to the applied root-mean-square voltage  $V_{\mathrm{rms}}$ . Error bars indicate 1 s.d. of uncertainty using Poisson statistics.

parasitic effects. We further characterize the frequency correlations for a small 18-mode subspace by filtering pairs of modes that are symmetric around the spectral centre and recording coincidence counts between the mode pair, as illustrated in Fig. 2b. As shown in Fig. 2d, all of the mode pairs exhibit fairly uniform correlation amplitudes, indicating an equal probability of producing biphotons across the QOFC spectrum. We also measure these correlations for pairs of modes that are not frequency matched in a  $5 \times 5$  matrix, obtaining a joint-spectral intensity (JSI) map as shown in Fig. 2e. The results presented in Fig. 2e clearly show the well-known anti-correlation of the photon-pair modes expected from SPDC, indicating strong frequency correlations and a clean photon-pair generation process. Details on the experimental set-up are provided in Supplementary Section III.

# Simulations in the time-frequency correlation space

Quantum random walks of correlated photons. With the strong quantum correlations of the produced QOFC modes, we are in a position to create a tight-binding synthetic crystal. This is realized by turning on a microwave drive and matching its frequency with the resonator FSR at 50 GHz. The first experiment is a quantum random walk of a particle in a tight-binding crystal. This is a natural outcome of this system as, at any given mode, a photon has an equal probability of scattering to either a lower or a higher frequency mode, with an amplitude that can be controlled with the microwave power. This creates a continuous-time random walk for the two photons in a 1D chain of modes; however, the biphoton frequency correlation is a 2D space, as shown in the JSI plot in Fig. 2e. We will track the trajectory of the JSI during the random walk by measuring coincidences at each pair of modes in a  $5 \times 5$  space with

increasing modulation amplitude. Although we make measurements in a small subspace of the total available bandwidth due to time constraints (see Methods for details), the rest of the synthetic lattice will behave in the same way. Figure 3 shows the results of this measurement. As we increase the modulation amplitude, the biphoton correlation starts to spread perpendicular to the anti-diagonal, and the spread increases with increasing microwave signal power. From the initial state in Fig. 3b, we can observe photons jumping multiple modes within their lifetime before escaping the resonator, sometimes jumping up to four modes at strong modulation powers. The random walk of the photon pairs tends to reduce their frequency correlation, moving them from a strongly correlated state towards a separable state. This is also inline with the theoretical treatment of this system (see Supplementary Section I). Figure 3g plots the standard deviation (s.d.) of the JSI as a function of the modulation voltage. The s.d. is scaled such that an unmodulated SPDC process gives a zero spread (see Methods for details). The data fit well with a line as expected from a quantum random walk $^{47,48}$ . The slight deviation from linearity at the highest modulation amplitude is due to the onset of nonlinearity in the gain of the microwave amplifier used in the experiment as well as modulation on the pump laser (see Supplementary Section IA for a note on this discrepancy). It is known that random walks with quantum states of light have features that are not available to random walks with classical states (for example, see ref. 49). This can be put in mathematical terms by violation of a classical inequality for a random walk. We have performed this measurement using the data in Fig. 3 and obtained a violation of 7 s.d. from measurement uncertainty (see Supplementary Section IC, and Supplementary Figs. 6 and 7 for details). It is important

![](images/b9ca95f2b1ca4eea45b3efe09cfb80fe139318e7740bc4c39fb76fa2467a52cb.jpg)  
a

![](images/b54f41159087d3114bea9faf7cd25ef0ca0c913d9b86ef4aa3bda80266fa693b.jpg)  
b

![](images/7219a863a60200b9c6856abd53488efb1e2aadf01cfea6ba5fcf8b6aba916dc7.jpg)

![](images/a7d86662d07cfc52f62e4ec44d3488cf43894611e2a57faadfc82df2064e5b7a.jpg)  
C

![](images/7aa63f6ac80ee2e611482f115aa5104c91574dbc0699eb287ad1c18356918b7a.jpg)  
f

g  
![](images/eb5e4cde8800fdc7555c154b49d3af73c26806f986237a25f6979ae9842df98f.jpg)  
a, The modulation signal is detuned from the resonator FSR by an amount  $\Delta$  while  $V_{0}$  is kept constant. A lattice site (orange) one position away from the main SPDC diagonal (green) is picked to measure the biphoton temporal correlations for varying  $\Delta$ . Arrows indicate the oscillatory movements of the biphoton correlations with detuning. b-f, Biphoton temporal correlations obtained by

d  
Fig. 4 | Simulating Bloch oscillations on the biphoton temporal correlations.  
![](images/b4324e716fa8d9e021460c9021ba49134f989e353ebe96b1cd9107d4301afa8e.jpg)  
accumulating coincidence histograms for differences in arrival time  $(\delta T)$  of the two photons for increasing values of  $\Delta$ . Orange lines are theoretical fittings of the data.  $\mathbf{g}$ , The ratio of the measured oscillation frequency to the detuning obtained by a sinusoidal fit of the coincidence histogram after correcting for the exponential decay envelope. Error bars indicate a  $95\%$  confidence bound on the frequency fit.

![](images/d5cb95d03d1d98bde7f49a49fe0b1e9050f3f44527d149d4f683524236e39f0a.jpg)  
e

![](images/5f7f962379952bc9dc7a4bd5625498d0c69bbacdc9cf875bc9cef8ecfa5395dd.jpg)

to note that this evolution of the spectral correlations is realized within the SPDC generation process without any post-processing, in contrast with other similar random walk experiments that have to rely on complex circuit structures such as a network of beam splitters or waveguides $^{50}$  or post-processing tools such as pulse shapers and filters $^{48,51}$  to perform the random walk. This experiment provides a much simpler architecture—an optical cavity with a time-dependent length, for these experiments. Moreover, the fully integrated device approach indicates the possibility for a tunable photon pair source with active control over the time-frequency entanglement.

Synthetic electric fields and Bloch oscillations. Apart from the modulation amplitude, the high-speed phase modulator embedded in the microresonator enables free tuning of the microwave signal frequency,  $\Omega$ . Physically, a detuning  $\Delta = \mathrm{FSR} - \Omega$  imparts a phase on the coupling in the tight-binding model (see Supplementary Section IB for details), which is directly equivalent to the presence of an external gauge potential applied on a solid-state system[52]. For a constant detuning, this corresponds to the simulation of a constant electric field acting on electrons in the crystal lattice, which leads to Bloch oscillations. By introducing this detuning, we can simulate an effective electric field for the photon pairs, forcing them into oscillations. Simulations of Bloch oscillations have been realized in many experiments in the past (see, for example, refs. 53,54). However, our system creates a unique situation in which all of the modes in the synthetic space are equally likely to be populated with a photon, and they all exchange photons between them at the same rate. This means that, on average, photon flux in each mode has no time dependence, and no net movement of photons can be observed with intensity measurements. The temporal dynamics of the oscillation are revealed only in the second-order intensity correlation of the QOFC modes. To observe such Bloch oscillations, we pick an off-diagonal term in the frequency space which, ordinarily, will not

frequency match SPDC, as shown in Fig. 4a. Any coincidences in this mode pair will only occur when the biphoton frequency correlations spread due to the random walk. For this simulation, we collect a histogram of coincidence counts for differences in arrival times between the two photons. This gives the biphoton temporal correlation function, which typically shows an exponentially decaying envelope corresponding to the photon lifetime of the loaded resonator; this is all we see at zero detuning (Fig. 4b). When detuning is introduced, oscillations emerge with a period matching the detuning frequency, as shown in the coincidence histograms in Fig. 4c–f, indicating an oscillatory probability of detecting a photo pair in the selected mode pair. The modulation signal initially causes the biphoton correlations to spread, but at a characteristic time corresponding to  $\pi / \Delta$ , the effective electric field forces the photons to backtrack their movement, returning to the original correlated spectrum. This process repeats until the photons escape the resonator and this movement is imprinted onto the coincidence histogram. The simulation of Bloch oscillations is therefore run in the temporal correlation space, in which the effective electric field forces the photon pairs to oscillate between a strongly correlated and an uncorrelated state in the frequency space. Figure 4g plots the ratio of the oscillation frequency measured by a sinusoidal fit of the coincidence histogram to the microwave signal detuning (see Methods for details), which shows good agreement. A theoretical treatment for this oscillatory evolution of the biphoton correlations is presented in the Supplementary Section IB.

Strong coupling regime and Rabi oscillations. In systems of coupled modes, Rabi oscillations emerge when the rate at which the modes exchange energy exceeds the system's decay rate. Typically seen in coherently driven atomic two-level systems $^{55}$ , Rabi oscillations are characterized by the energy levels splitting into dressed states. The synthetic lattice can simulate these effects when the coupling strength

![](images/0fb7be3e0edb25212c9a0133911cfdd382202060d9128100e6a1059baaa6374a.jpg)

![](images/4c6bb972b6853a488c664e5d135c386abf5284a175785cc4cee85c91d2f0d24a.jpg)

![](images/241d1ca7a2eec1483a8c88553adc4ee2ff54f60d15c484eeb0b8d20de306271f.jpg)

![](images/762e9f2e41f27b27123eff708879cc572fb5bdc5b648adfa7b820697bf284818.jpg)  
Fig. 5 | Strong coupling and Rabi oscillations. a, The microwave signal frequency  $\Omega$  is tuned again to the resonator FSR and  $V_{0}$  (represented here as the effective mode coupling strength,  $G / 2$ ) is varied. When the coupling strength exceeds the resonator linewidth, the resonator modes split into two dressed modes that are spaced from each other by  $2G$ , indicating the onset of a strong coupling regime. We pick a site corresponding to a signal-idler mode pair on the main SPDC diagonal (orange) for the biphoton temporal correlation

![](images/f5ddb15c56d91ed9863e21c68c4669c57e6631c649e42df8084b8d1a0588db43.jpg)  
measurement. Arrows indicate an exchange of photons between adjacent lattice sites, highlighted in green. b,c, Transmission spectrum of a signal-mode cold-cavity resonance is plotted for two coupling strengths that indicate weak (b) and strong (c) coupling regimes, with a mode splitting clearly visible. d,e, The corresponding biphoton coincidence histograms for the chosen lattice site. Here we observe Rabi oscillations in the strong coupling regime. Orange lines indicate theoretical results.

of the signal and idler modes exceeds their linewidth. In this case, the lattice sites exchange energy several times before the photons escape the resonator. These oscillations, like Bloch oscillations, are imprinted in the biphoton temporal correlations (at zero detuning of the microwave frequency,  $\Delta = 0$ , and a sufficiently strong driving amplitude). We used a different device with a smaller linewidth than the one used in the previous two experiments to demonstrate this phenomenon. Figure 5 shows the results for a pair of comb modes on the central correlation diagonal. These modes have a loaded linewidth ( $\gamma_{t} = 200\mathrm{MHz}$ ). When the mode coupling strength  $G$  proportional to the microwave signal amplitude, is small, the system falls within the weak coupling regime as evident by the transmission spectrum of a cold-cavity resonance (Fig. 5b). Here, the effective mode coupling strength, given by  $G / 2$ , is  $140\mathrm{MHz}$ , which is less than the  $200\mathrm{MHz}$  linewidth of the modes. Accordingly, the recorded coincidence histogram of the mode pairs exhibits a normal exponentially decaying envelope (Fig. 5d); however, we achieved a coupling strength of  $G / 2 = 380\mathrm{MHz}$  when using a strong microwave driving amplitude. This gives a coupling-to-loss ratio of  $G / 2\gamma_{t} = 1.9$ , which is nearly twice the linewidth of the cavity, as is evident by the large mode splitting of the cold-cavity resonance shown in Fig. 5c. Consequently, the recorded coincidence histogram becomes oscillatory in this strong coupling regime (Fig. 5e). The measured correlations are in good agreement with the theoretical expectations, and the oscillation period of 0.65 ns in Fig. 5e matches the -12 pm mode splitting in Fig. 5c. The Rabi oscillations observed here are unique given that we are dealing with a multilevel system instead of the traditional two-level system where these effects are typically studied. Here the generated photons oscillate between three adjacent coupled modes. We also obtain a mode splitting that is close to twice the coupling strength—double that of a two-level system. Supplementary Section ID provides a detailed theoretical treatment for the strong coupling regime.

Overall, the three experiments characterized on the biphoton spectral and temporal correlations demonstrate the versatility and richness of the device physics available to us with active control over the time-frequency domain.

# Discussion

The ability to scale a quantum system to include enough particles and dimensions to the point at which the computation becomes

advantageous over a classical computer has become a critical metric for competing architectures. In this regard, this work demonstrates several useful properties of the monolithic lithium niobate nanophotonic platform and the fabricated device. First, the device design requires only a single microresonator with a time-varying optical path length to create the synthetic space. Together with dispersion engineering, we are able to create a nearly 800-dimensional coupled-mode network. Second, the resonator is capable of generating quantum-correlated photons across the entire space, requiring only a single-mode laser and a microwave signal as inputs to generate and coherently control a QOFC, and without the need for post-processing optics. This allows us to run both classical and quantum simulations on this device. As stated earlier, the quantum random walk of correlated photons has features that are not present in random walks with classical states. On the other hand, Bloch oscillations can be simulated on classical systems. The simplicity in the device design is also beneficial for scaling up this proof-of-principal demonstration to run complex computations. For instance, we have shown that the microwave signal can provide flexible control over the nature of the synthetic space. Taking this further, a multitone excitation can create short and long-range coupling in the lattice, and amplitude/phase modulation can be used to explore complex lattices. Furthermore, the highly multidimensional nature of the SPDC process in the lattice can be used for multiphoton generation, approaching the continuous variable regime in which the squeezing parameter is reasonably large. In this scenario, the correlation imparted by SPDC can be complemented by the correlation that results from the resonator mode coupling to create cluster states for one-way computation<sup>56</sup>. Our device is well-suited to this task. The pump spectral profile can also be used to create an additional layer of complexity in the lattice, for example, by implementing SPDC though multiple pump modes.

Finally, we can consider the limitations of the current device. First, the demultiplexing of each frequency mode required for measurement causes substantial losses (see Supplementary Section III for details). It limits the size of the lattice than can be measured within a reasonable time. This can be resolved by further optimizing the device design for a higher SPDC efficiency as well as a lower chip-to-fibre coupling loss. Second, we are currently focused on a square lattice with uniform coupling, which limits the physics that can be explored. Multitone microwave driving signals and dispersion control of the mode spacing

can allow creation of more complex lattices. Finally, the photon lifetime in the resonator and the saturation voltage limit the maximum number of modes that a photon can hop through before exiting the resonator to approximately ten. This can also be increased with multitone microwave signals, reduced FSR and improving fabrication to reduce material loss. We expect that the device would be able to run more complex simulations with these improvements.

To conclude, we have demonstrated on-chip generation and coherent control of an ultra-broadband biphoton QOFC on the lithium niobate integrated photonic platform. We have used this QOFC to create a quantum-correlated synthetic lattice with a nearly  $400 \times 400$  mode space. We have demonstrated the capability of this system by running three simulations—(1) a two-particle quantum random walk, (2) generation of a synthetic electric field and Bloch oscillations, and (3) multilevel Rabi oscillations—on the biphoton spectral and temporal correlation functions. The device presented here combines the simplicity of monolithic nanophotonic structure, a high-dimensional quantum-correlated synthetic space and electrically controlled tunability, which now opens up an avenue towards running complex large-scale simulations and computational tasks. We envision this work will motivate further investigations into chip-scale implementations of analogue quantum simulation and computation in the time-frequency domain.

# Online content

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41566-023-01236-7.

# References

1. Aaronson, S. & Arkhipov, A. The computational complexity of linear optics. In Proc. 43rd Annual ACM Symposium on Theory of Computing 333-342 (2011).  
2. Rohde, P. P. & Ralph, T. C. Error tolerance of the boson-sampling model for linear optics quantum computing. Phys. Rev. A 85, 022332 (2012).  
3. Zhong, H.-S. et al. Phase-programmable gaussian boson sampling using stimulated squeezed light. Phys. Rev. Lett. 127, 180502 (2021).  
4. Wang, H. et al. High-efficiency multiphoton boson sampling. Nat. Photon. 11, 361-365 (2017).  
5. Wang, H. et al. Boson sampling with 20 input photons and a 60-mode interferometer in a  $10^{14}$ -dimensional hilbert space. Phys. Rev. Lett. 123, 250503 (2019).  
6. Spring, J. B. et al. Boson sampling on a photonic chip. Science 339, 798-801 (2013).  
7. Broome, M. A. et al. Photonic boson sampling in a tunable circuit. Science 339, 794-798 (2013).  
8. Kraus, Y. E., Lahini, Y., Ringel, Z., Verbin, M. & Zilberberg, O. Topological states and adiabatic pumping in quasicrystals. Phys. Rev. Lett. 109, 106402 (2012).  
9. Verbin, M., Zilberberg, O., Kraus, Y. E., Lahini, Y. & Silberberg, Y. Observation of topological phase transitions in photonic quasicrystals. Phys. Rev. Lett. 110, 076403 (2013).  
10. Madsen, L. S. et al. Quantum computational advantage with a programmable photonic processor. Nature 606, 75-81 (2022).  
11. Aspuru-Guzik, A. & Walther, P. Photonic quantum simulators. Nat. Phys. 8, 285-291 (2012).  
12. Wang, J., Sciarrino, F., Laing, A. & Thompson, M. G. Integrated photonic quantum technologies. Nat. Photon. 14, 273-284 (2020).  
13. Wang, J. et al. Multidimensional quantum entanglement with large-scale integrated optics. Science 360, 285-291 (2018).  
14. Arrazola, J. M. et al. Quantum circuits with many photons on a programmable nanophotonic chip. Nature 591, 54-60 (2021).

15. Yuan, L., Lin, Q., Xiao, M. & Fan, S. Synthetic dimension in photonics. Optica 5, 1396-1405 (2018).  
16. Lukens, J. M. & Lougovski, P. Frequency-encoded photonic qubits for scalable quantum information processing. Optica 4, 8-16 (2017).  
17. Lin, Q., Sun, X.-Q., Xiao, M., Zhang, S.-C. & Fan, S. A three-dimensional photonic topological insulator using a two-dimensional ring resonator lattice with a synthetic frequency dimension. Sci. Adv. 4, eaat2774 (2018).  
18. Luo, X.-W. et al. Quantum simulation of 2D topological physics in a 1D array of optical cavities. Nat. Commun. 6, 1-8 (2015).  
19. Yuan, L., Shi, Y. & Fan, S. Photonic gauge potential in a system with a synthetic frequency dimension. Opt. Lett. 41, 741-744 (2016).  
20. Ozawa, T., Price, H. M., Goldman, N., Zilberberg, O. & Carusotto, I. Synthetic dimensions in integrated photonics: from optical isolation to four-dimensional quantum hall physics. Phys. Rev. A 93, 043827 (2016).  
21. Yuan, L. & Fan, S. Three-dimensional dynamic localization of light from a time-dependent effective gauge field for photons. Phys. Rev. Lett. 114, 243901 (2015).  
22. Yuan, L., Shi, Y. & Fan, S. Photonic gauge potential in a system with a synthetic frequency dimension. Opt. Lett. 41, 741-744 (2016).  
23. Bartlett, B., Dutt, A. & Fan, S. Deterministic photonic quantum computation in a synthetic time dimension. Optica 8, 1515-1523 (2021).  
24. Dutt, A. et al. A single photonic cavity with two independent physical synthetic dimensions. Science 367, 59-64 (2020).  
25. Lustig, E. et al. Photonic topological insulator in synthetic dimensions. Nature 567, 356-360 (2019).  
26. Dutt, A. et al. Creating boundaries along a synthetic frequency dimension. Nat Commun. 13, 3377 (2022).  
27. Li, G. et al. Dynamic band structure measurement in the synthetic space. Sci. Adv. 7, eabe4335 (2021).  
28. Regensburger, A. et al. Parity-time synthetic photonic lattices. Nature 488, 167-171 (2012).  
29. Wang, K. et al. Generating arbitrary topological windings of a non-hermitian band. Science 371, 1240-1245 (2021).  
30. Dutt, A. et al. Experimental band structure spectroscopy along a synthetic dimension. Nat. Commun. 10, 3122 (2019).  
31. Wang, K. et al. Multidimensional synthetic chiral-tube lattices via nonlinear frequency conversion. Light Sci. Appl. 9, 132 (2020).  
32. Wang, K., Dutt, A., Wojcik, C. C. & Fan, S. Topological complex-energy braiding of non-hermitian bands. Nature 598, 59-64 (2021).  
33. Chalabi, H. et al. Guiding and confining of light in a two-dimensional synthetic space using electric fields. Optica 7, 506-513 (2020).  
34. Hu, Y., Reimer, C., Shams-Ansari, A., Zhang, M. & Loncar, M. Realization of high-dimensional frequency crystals in electro-optic microcombs. Optica 7, 1189-1194 (2020).  
35. Balčytis, A. et al. Synthetic dimension band structures on a Si CMOS photonic platform. Sci. Adv. 8, eabk0468 (2022).  
36. Plenio, M. B. & Huelga, S. F. Dephasing-assisted transport: quantum networks and biomolecules. New J. Phys. 10, 113019 (2008).  
37. Caruso, F., Spagnolo, N., Vitelli, C., Sciarrino, F. & Plenio, M. B. Simulation of noise-assisted transport via optical cavity networks. Phys. Rev. A 83, 013811 (2011).  
38. Liberman, L., Israel, Y., Poem, E. & Silberberg, Y. Quantum enhanced phase retrieval. Optica 3, 193-199 (2016).  
39. Sansoni, L. et al. Two-particle bosonic-fermionic quantum walk via integrated photonics. Phys. Rev. Lett. 108, 010502 (2012).  
40. Lanyon, B. P. et al. Towards quantum chemistry on a quantum computer. Nat. Chem. 2, 106-111 (2010).

41. Ma, X.-s, Dakic, B., Naylor, W., Zeilinger, A. & Walther, P. Quantum simulation of the wavefunction to probe frustrated heisenberg spin systems. Nat. Phys. 7, 399-405 (2011).  
42. Javid, U. A. et al. Ultrabroadband entangled photons on a nanophotonic chip. Phys. Rev. Lett. 127, 183601 (2021).  
43. Zhang, M. et al. Broadband electro-optic frequency comb generation in a lithium niobate microring resonator. Nature 568, 373-377 (2019).  
44. Hu, Y. et al. High-efficiency and broadband on-chip electro-optic frequency comb generators. Nat. Photo. 16, 679-685 (2022).  
45. Kourogi, M., Enami, T. & Ohtsu, M. A monolithic optical frequency comb generator. IEEE Photon. Technol. Lett. 6, 214-217 (1994).  
46. Kues, M. et al. Quantum optical microcombs. Nat. Photon. 13, 170-179 (2019).  
47. Tang, H. et al. Experimental two-dimensional quantum walk on a photonic chip. Sci. Adv. 4, eaat3174 (2018).  
48. Imany, P., Lingaraju, N. B., Alshaykh, M. S., Leaird, D. E. & Weiner, A. M. Probing quantum walks through coherent control of high-dimensionally entangled photons. Sci. Adv. 6, eaba8066 (2020).  
49. Bromberg, Y., Lahini, Y., Morandotti, R. & Silberberg, Y. Quantum and classical correlations in waveguide lattices. Phys. Rev. Lett. 102, 253904 (2009).  
50. Gräfe, M. et al. Integrated photonic quantum walks. J. Opt. 18, 103002 (2016).  
51. Haldar, R. et al. Steering of quantum walks through coherent control of high-dimensional bi-photon quantum frequency combs with tunable state entropies. Preprint at https://arxiv.org/abs/2210.06305 (2022).

52. Luttinger, J. The effect of a magnetic field on electrons in a periodic potential. Phys. Rev. 84, 814 (1951).  
53. Morandotti, R., Peschel, U., Aitchison, J., Eisenberg, H. & Silberberg, Y. Experimental observation of linear and nonlinear optical Bloch oscillations. Phys. Rev. Lett. 83, 4756 (1999).  
54. Preiss, P. M. et al. Strongly correlated quantum walks in optical lattices. Science 347, 1229-1233 (2015).  
55. Kaluzny, Y., Goy, P., Gross, M., Raimond, J. & Haroche, S. Observation of self-induced rabi oscillations in two-level atoms excited inside a resonant cavity: the ringing regime of superradiance. Phys. Rev. Lett. 51, 1175 (1983).  
56. Zhu, X. et al. Hypercubic cluster states in the phase-modulated quantum optical frequency comb. Optica 8, 281-290 (2021).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

© The Author(s), under exclusive licence to Springer Nature Limited 2023

# Methods

# Device fabrication and poling

The device was fabricated on a  $600\mathrm{nm}$ -thick x-cut lithium niobate thin film on a  $4.7\mu \mathrm{m}$  silicon dioxide bottom cladding layer and a silicon substrate (NanoLN). The waveguide was first patterned with electron-beam resist (ZEP-520A) via electron-beam lithography, which was then transferred to the lithium niobate layer by  $300\mathrm{nm}$  etching using  $\mathrm{Ar^{+}}$  ion milling. After resist removal, a second electron-beam exposure was performed to pattern the electrode structures. The electrodes ( $20\mathrm{nm}$  titanium/400 nm gold) were then deposited via electron-gun evaporation, which was then followed by a standard lift-off process. After fabrication, the resonator was poled using a sequence of  $240\mathrm{V}, 10\mathrm{ms}$  square-wave electrical pulses applied to the periodically patterned electrodes. The poling efficiency was monitored heuristically by optimizing second-harmonic generation. A tunable laser was scanned through the resonator while the poling pulses were applied (these were applied until the second-harmonic signal power saturated). To further increase the quality factor for measurements in the strong coupling regime in Fig. 5, a fabricated device was annealed after fabrication. Annealing the devices can boost the quality factor by recovering the damage caused during fabrication and remove absorptive contaminants like O-H bonds; it can also help in mitigating the photo-refractive effect in lithium niobate. Annealing was performed at  $450^{\circ}\mathrm{C}$  for  $1\mathrm{h}$  with oxygen flow, which doubled the intrinsic quality factor and reduced the loaded linewidth to  $200\mathrm{MHz}$ .

# Data acquisition

The QOFC spectrum in Fig. 2c was obtained directly using an infrared spectrometer. The spectrometer camera captures a  $70~\mathrm{nm}$  bandwidth in a single exposure. The full spectrum covering  $1,300 - 1,600\mathrm{nm}$  was pieced together by rotating the diffraction grating to change the centre wavelength by  $60~\mathrm{nm}$  each time, and capturing a spectrum with a  $1\mathrm{min}$  integration time. The spectrum in Fig. 2c was normalized to the average peak of the spectrum at approximately 10,000 counts. The spectral correlation measurements were made by scanning two tunable filters over the resonator modes. Typical coincidence rates on the detectors were around  $85\mathrm{Hz}$ . The normalization in Fig. 2d was performed at a peak value of 5,130 counts per  $60~s$ . The coincidence-to-accidental ratio for a pair of modes in the comb was approximately 500 (varying from 400 to 600), limited by the losses in the experiment that total to 15 dB per channel. A detailed analysis of coincidence-to-accidental ratio of individual comb modes and the full SPDC spectrum is provided in Supplementary Section IE and Supplementary Fig. 9.

For the random-walk data in Fig. 3, each point on the JSI was taken for a integration time varying from 2 to 8 min depending on the modulation depth. This is because the generation efficiency was much lower at high modulation due to the pump scattering away into unwanted frequencies that do not phase-match SPDC, as well as the spreading of the JSI to off-diagonal modes, reducing detection probability per mode pair. The measurement time for the random-walk matrices in Fig. 3 scales as the square of the number of signal modes. We therefore limited our measurement to a  $5 \times 5$  space, which could be measured within  $3.5\mathrm{h}$  for the highest modulation amplitude. The JSI value at each data point in the matrices in Fig. 3 was obtained by integrating within the envelope of the coincidence histogram for the corresponding mode pair. Each colour map was normalized to the peak value in the matrix. The Bloch oscillation plots were obtained for integration times varying from  $30\mathrm{min}$  to  $1\mathrm{h}$  for the highest frequency oscillations. All temporal correlation plots in Figs. 4 and 5 are normalized to the peak correlation value at  $\delta t = 0$ . See Supplementary Section III for details on the full experimental set-up.

The random-walk variance can be calculated as

$$
s. d. ^ {2} = \frac {\sum_ {X , Y} d _ {X , Y} ^ {2} J S I _ {X , Y}}{\sum_ {X , Y} J S I _ {X , Y}}, \tag {1}
$$

where  $d_{x,y}$  is the diagonal distance of each point on the JSI from the main matrix diagonal in integer units. Equation (1) was used to evaluate spread of the random walk in Fig. 3g. The Bloch oscillation frequencies were measured by first correcting the coincidence histogram for the exponential decay envelope and then numerically fitting the flattened oscillations with a sinusoidal function. The frequency of the fitting function is varied until the RMS error of the fit reaches a minimum. The resulting frequency is plotted in Fig. 4g, in which the error bars represent a  $95\%$  confidence bound on the frequency parameter.

# Data availability

Data and information supporting the results in the article and its conclusions, and to reproduce the experiment are provided in the main article and the Supplementary Information.

# References

57. Shams-Ansari, A. et al. Reduced material loss in thin-film lithium niobate waveguides. *APL Photon.* 7, 081301 (2022).  
58. Xu, Y. et al. Mitigating photorefractive effect in thin-film lithium niobate microring resonators. Opt. Express 29, 5497-5504 (2021).

# Acknowledgements

We thank O. Pfister (University of Virginia) for useful discussions. This work is supported in part by the National Science Foundation (NSF) (grant nos. OMA-2138174 and ECCS-2231036), the Defense Threat Reduction Agency-Joint Science and Technology Office for Chemical and Biological Defense (grant no. HDTRA11810047), and the Defense Advanced Research Projects Agency (DARPA) QuICC programme under agreement no. FA8650-23-C-7312 and LUMOS programme under agreement no. HR001-20-2-0044. This work was performed in part at the Cornell NanoScale Facility, a member of the National Nanotechnology Coordinated Infrastructure (NNCI), which is supported by the National Science Foundation (grant no. NNCI-2025233). The project or effort depicted was or is sponsored by the Department of the Defense, Defense Threat Reduction Agency. The content of the information does not necessarily reflect the position or the policy of the federal government, and no official endorsement should be inferred.

# Author contributions

Q.L. and U.A.J. conceived the experiment. U.A.J. and J.S. conducted theoretical analysis and ran simulations for device design. U.A.J. and J.L. fabricated the device. U.A.J., R.L.-R. and A.G. set up and ran the experiment. U.A.J. conducted data analysis and wrote the manuscript with contributions from all authors. Q.L. supervised the project.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41566-023-01236-7.

Correspondence and requests for materials should be addressed to Qiang Lin.

Peer review information Nature Photonics thanks the anonymous reviewers for their contribution to the peer review of this work.

Reprints and permissions information is available at www.nature.com/reprints.