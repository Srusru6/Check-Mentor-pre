# Parallelized telecom quantum networking with anytterbium-171atom array

Received: 14 March 2025

Accepted: 1 August 2025

Published online: 12 September 2025

![](images/afe10f6e2b2f731262412b6ceb8997fa552e5ca12f172d7c0b9471aef0cb0875.jpg)

Check for updates

Lintao Li  $\text{©}$ , Xiye Hu  $\text{©}$ , Zhubing Jia  $\text{©}$ , William Huie, Won Kyu Calvin Sun  $\text{©}$ , Aakash, Yuhao Dong  $\text{©}$ , Narisak Hiri-O-Tuppa & Jacob P. Covey  $\text{©}$

The integration of quantum computers and sensors into a quantum network enables new capabilities in quantum information science. Most networks with atom-like qubits operate at visible or near-ultraviolet wavelengths and require conversion to the telecom band for long-distance communication, which reduces efficiency and potentially introduces noise. Here we report high-fidelity entanglement between ytterbium-171 atoms and optical photons generated directly in the telecommunication band, where fibre loss is low. The nuclear spin of the atom is entangled with a single photon in the time-bin basis, yielding a high atom-measurement-corrected atom-photon Bell state fidelity. This can be further improved by addressing photon measurement errors. By imaging the atom array onto an optical fibre array, we also implement a parallelized networking protocol that can increase the remote entanglement rate proportionately with the number of channels. We also preserve coherence on a memory qubit during operations on communication qubits. These results support the integration of atomic systems into scalable quantum networks.

Quantum networks utilize entanglement shared among many nodes to enable new opportunities for cryptographically secured communication $^{1,2}$ , quantum sensing $^{3,4}$  and timekeeping $^{5,6}$ , and blind $^{7-9}$  or distributed $^{10,11}$  quantum computing. Entanglement between two network nodes is typically generated probabilistically via a Bell state measurement of two photons that are each entangled with a matter-based, atom-like qubit in a node. This technique has been used to realize high-fidelity $^{12}$ , long-distance entanglement $^{13-16}$  between atom-like qubits. The rate and fidelity of entanglement between the nodes is primarily determined by the properties of atom-like qubits and the photonic interface that collects photons into optical fibres $^{17}$ .

Following the development of classical communication technology, quantum networks will benefit from the use of photons in the telecommunication (telecom) wavelength band (approximately  $1.25 - 1.65\mu \mathrm{m}$ ), both because of the minimal attenuation in optical fibre and because of the associated growth of silicon, complementary-metal-oxide-semiconductor-compatible photonic technologies such as fast and efficient switches, modulators and detectors. However, most quantum networks with atom-like qubits operate at visible or near-ultraviolet wavelengths[18-21] and require conversion to the telecom band for

long-distance networking $^{14,15,22,23}$ , which adds complexity and footprint, reduces efficiency, and may add noise and/or extra photons. Although some rare-earth ions embedded in solid-state hosts, for instance, operate directly at telecom wavelengths, their transitions are weak and require substantial Purcell enhancement $^{16,24-26}$ . A platform that combines both highly coherent qubits capable of scalable deterministic quantum logic and a high emission bandwidth directly in the telecom wavelength band has yet to be developed.

Here we demonstrate quantum networking with highly coherent nuclear spin qubits that are directly connected to a strong, telecom band transition at a wavelength  $1,389\mathrm{nm}$ , where the attenuation is  $\sim 0.3\mathrm{dBkm}^{-1}$  in modern telecom fibre (Fig. 1). Using a time-delay interferometer (TDI) with a 560-m fibre on one arm, we perform the tomography of photonic qubits. We observe an atom-measurement-corrected (raw) Bell pair fidelity of  $0.950(9)\pm 0.005(3)_{\mathrm{bound}}$ $(0.90(1)\pm 0.014(3)_{\mathrm{bound}})$  between the metastable nuclear spin qubit of a ytterbium-171 atom and a single photon. Currently, the efficiency is sub-percentage level, limited by the use of a lens for photon collection rather than a cavity. To our knowledge, this fidelity matches the record for entanglement between atom-like emitters and telecom-band

![](images/f748139ffd96188cf339f4f21021ae187a9eee41d0d0023ab67e0c5d79c61e6f.jpg)

![](images/c613f88039f330161060a6df7c3ab50c8a73b30b3fb5aa85b886aa0f5a7f1b77.jpg)  
Fig. 1 | Overview of the platform. a, An imaging system with a high-numerical-aperture objective maps an array of atoms in optical tweezers to an array of single-mode optical fibres. We nominally use an array of 20 tweezers with spacing  $-4.7\mu m$ , but an array of five tweezers with a spacing of  $-20\mu m$  is used for optimal matching with the MFD of the fibre array. The inset shows the image of a typical V-grooved fibre array with ten fibres in a row. b, Our vision for

![](images/ad076aa0fc5ef4aa9e6df9143ebf79c19c246dca7c056499d3bebfb2066243dc.jpg)  
parallelized networking with atom array processors using fibre, detector and BS arrays. c, We utilize time-bin encoding to entangle the metastable nuclear spin of ytterbium-171 atoms (blue pulses) with individual photons with a wavelength of 1,389 nm (red pulses). d, After sending the photons through a 40-m fibre, we utilize a TDI and SNSPDs to characterize the atom-photon Bell state.

photons $^{14}$ , which was performed with wavelength conversion and polarization encoding in rubidium atoms.

Moreover, many applications of quantum networks require fast entanglement generation. The coherence time of the qubits represents a minimal timescale for useful entanglement generation $^{27}$ . However, a more stringent requirement for distributed quantum computing, for instance, is the gate rate in a quantum processor. Ideally, remote entanglement would be established at least this fast, but the attempt rate is fundamentally limited by atomic properties such as the decay rate. Hence, the optimal strategy for increasing the entanglement generation rate is via parallelization. With an array of  $N$  qubits in each node, remote entanglement generation (REG) could be attempted in parallel across  $N$  channels to boost the communication rate by a factor of  $N$  (Fig. 1b). Such spatial multiplexing outperforms temporal multiplexing $^{28-31}$  in short network links for which latency from two-way communication is negligible. Although refs. 28-31 focus on temporal multiplexing with an atom array in a single cavity, our vision for spatial multiplexing is based on a cavity array $^{32-35}$ .

Therefore, we additionally demonstrate a platform for parallelizable networking by coupling our one-dimensional atom array to a lensed fibre array. We show that the atom-photon entanglement fidelities are uniform across the atom/fibre array, with negligible crosstalk between channels. Finally, we demonstrate the ability to preserve coherence on a memory qubit and perform networking operations on communication qubits. Our work sets the stage for parallelizable,

high-fidelity remote entanglement between large-scale neutral atom quantum processors, opening the door to new opportunities for atomic clock networks $^{5,6}$  and distributed quantum computing $^{10,11,28-31,36}$ .

# Multilevel control of a ytterbium-171 atom array

We use a one-dimensional array of up to 20 optical tweezers with a wavelength of  $\sim 760\mathrm{nm}$  and depth  $U / k_{\mathrm{B}}\approx 500~\mu \mathrm{K}$  (Fig. 1a). After loading atoms into optical tweezers, we image the array to learn its occupancy, cool the atoms and perform optical pumping (OP) to the  $m_{F} = -1 / 2$  ground nuclear spin state. Many details of our system are provided elsewhere[37], but we have since added grey molasses cooling[39,40] (Supplementary Information). Electromagnetically induced transparency cooling[39,40] (Supplementary Information). Electromagnetically induced transparency cooling brings the atomic temperature close to the motional ground state, and offers a simpler alternative to sideband cooling for achieving moderately low temperatures. The strong telecom transition in ytterbium is from the metastable 'clock' state  ${}^{3}\mathrm{P}_{0}$  (with a lifetime of 20 s) to the higher-lying  ${}^{3}\mathrm{D}_{1}$  state. Hence, we focus on the nuclear spin qubit in the metastable state, which we directly entangle with a telecom photon. A coherence time of  $T_{2}^{*}\approx 7$  s has been demonstrated for the metastable nuclear spin qubit[40]. More broadly, it is well suited for myriad quantum computing operations[41,42] such as mid-circuit measurements (MCM)[40], leakage error detection[43] and Rydberg-mediated entangling gates[43-45] due to its relatively strong, single-photon coupling to an S-series Rydberg manifold[43,46]. The relevant level structure for our work is shown in Fig. 2a.

![](images/95ad1ddf6d74a8e09e6a33cf8675e5aaf00093acc8f61deec104de40830c78f0.jpg)  
Fig. 2 | Multilevel control of the ytterbium-171 array. a, Relevant level structure that shows the optical clock transition (yellow), the metastable nuclear spin qubit (blue) and the telecom transition for atom-photon entanglement (red). The decay pathways from the  $^3\mathrm{D}_1$  state are shown, where the pathway to  $^3\mathrm{P}_1$  subsequently leads to the ground state in  $-1\mu \mathrm{s}$ . As indicated by the arrow in light red, we realize a magic Rabi frequency on the telecom excitation, such that  $|\downarrow\rangle$  undergoes a detuned  $2\pi$ -rotation whereas a resonant  $\pi$ -pulse is applied on  $|\uparrow\rangle$ . b, Rabi oscillations on the clock transition with a  $\pi$ -pulse time of  $\tau_{\pi}^{0} \approx 4\mu \mathrm{s}$  and

![](images/9b6639a0497cfbffa612380884ebd4d2a3e0fa273f527c7e0a406c2820a13e55.jpg)

![](images/273e6e05d739ca73e03eeffba640ab71a36bff9c15fb163a9d6cd4ff32880f01.jpg)

![](images/8a0d52c3e97226a10c6158042eb4fcb4f6206e5aa9c95b323d5d6505ccc82d6d.jpg)  
corrected  $\pi$ -pulse (2 $\pi$ -pulse) fidelity of 0.985(4) (0.996(4)). c, Rabi oscillations of the metastable nuclear spin qubit with  $\pi$ -pulse time of  $\tau_{\pi}^{\mathrm{m}} \approx 0.6 \mu \mathrm{s}$  and corrected  $\pi$ -pulse fidelity of 0.996(3). d, Rabi oscillations of the telecom transition with  $\pi$ -pulse time of  $\tau_{\pi}^{\mathrm{t}} \approx 16$  ns and corrected  $\pi$ -pulse fidelity of 0.94(5).  $\tau_{\pi}^{\mathrm{t}}$  was chosen to minimize the population in the  $^3\mathrm{D}_1m_F = 1/2$  state (light red loop; see the main text). We detect the population in both  $^1\mathrm{S}_0$  (green) and  $^3\mathrm{P}_0$  (red) after spontaneous emission. Error bars in all of the figures presented in this work, unless otherwise stated, represent the standard error of the mean.

We initialize the clock state via a  $\pi$ -pulse on the  $^1 S_0,m_F = -1 / 2$  to  $^3\mathrm{P}_0,m_F = 1 / 2$  transition with  $\sigma^{+}$  polarization (Methods). We drive the transition with an approximate Hertz-linewidth laser and realize a Rabi frequency of  $\Omega^{\mathrm{o}} / 2\pi \approx 130\mathrm{kHz}$  for which  $\tau_{\pi}^{\mathrm{o}}\approx 4~\mu \mathrm{s}$ . As shown in Fig. 2b, we can drive highly coherent Rabi oscillations on the clock transition, which is enabled by the removal of high-frequency laser noise via active feed-forward[47] (Supplementary Information). We observe a corrected (raw)  $\pi$ -pulse fidelity of 0.985(4) (0.978(5)). Our definition of fidelity and our method for correcting state preparation and measurement errors is described in the Supplementary Information. Our corrected (raw)  $2\pi$ -pulse fidelity of 0.996(4) (0.979(5)) suggests that our measured fidelity is limited by detuning errors rather than Rabi decoherence.

After initializing in the  $m_{F} = 1 / 2$  nuclear spin state of the  ${}^{3}\mathrm{P}_{0}$  clock state, we demonstrate the ability to perform fast, high-fidelity rotations of the metastable nuclear spin qubit since such operations are required for time-bin remote entanglement $^{16,19}$ . We utilize stimulated Raman rotations via the  ${}^{3}\mathrm{D}_{1}$  state—blue-detuned from the  $\mathrm{F} = 3 / 2, m_{F} = 3 / 2$  state by  $612\mathrm{MHz}$ —with an effective two-photon Rabi frequency of  $\Omega^{\mathrm{m}} / 2\pi \approx 1\mathrm{MHz}$ . We operate at a magnetic field of  $120\mathrm{G}$ , for which the metastable nuclear spin Zeeman splitting is  $\Delta_{\mathrm{B}}^{\mathrm{m}} \approx 137\mathrm{kHz}$ —much less than  $\Omega^{\mathrm{m}}$ . We drive the Raman transition with a single monochromatic beam by operating at a 'magic' condition in which the differential light

shift on the qubit states exactly cancels  $\Delta_B^{\mathrm{m}}$  (ref. 42; Methods). As shown in Fig. 2c, we can drive highly coherent Rabi oscillations of the metastable nuclear spin qubit for which  $\tau_{\pi}^{\mathrm{m}} \approx 0.6~\mu \mathrm{s}$ . We measure a corrected (raw)  $\pi$ -pulse fidelity of 0.996(3) (0.987(4)).

Finally, we demonstrate control of the  $^3\mathrm{P}_0 \leftrightarrow {}^3\mathrm{D}_1$  telecom transition. Atom-photon entanglement is based on spontaneous emission from the  $^3\mathrm{D}_1$  state whose lifetime is  $\tau^{3}\mathrm{D}_1 \approx 330$  ns; therefore, we must initialize the  $^3\mathrm{D}_1$  state much faster than 330 ns. We drive the  $^3\mathrm{P}_0$ ,  $m_F = 1/2$  to  $^3\mathrm{D}_1$ ,  $F = 3/2$ ,  $m_F = 3/2$  transition via a  $\sigma^+$ -polarized beam (Methods) with a Rabi frequency  $\Omega^{\mathrm{t}} / 2\pi \approx 30$  MHz, which has a corresponding  $\pi$ -pulse time of  $\tau_{\pi}^{\mathrm{t}} \approx 16$  ns. As shown in Fig. 2d, we drive highly coherent Rabi oscillations, enabled by an acousto-optic modulator with a 5-ns switching time (Methods). As shown in Fig. 2a, the  $^3\mathrm{D}_1$  state decays back to the  $^3\mathrm{P}_0$  clock state with probability  $P_{^3\mathrm{P}_0} \approx 0.64$ , to the  $^3\mathrm{P}_1$  state with probability  $P_{^3\mathrm{P}_1} \approx 0.35$  (which then subsequently decays to the  $^1\mathrm{S}_0$  ground state in  $\sim 1~\mu \mathrm{s}$ ), and to the  $^3\mathrm{P}_2$  state with probability  $P_{^3\mathrm{P}_2} \approx 0.01$  (which is strongly anti-trapped in tweezers of this wavelength). The finite decay probability to  $^3\mathrm{P}_1$  requires the atomic state to be reset frequently within each entanglement attempt loop (Methods), and the finite decay probability to  $^3\mathrm{P}_2$  limits the total number of attempts before atom reloading. We observe Rabi oscillations of the telecom transition by probing both decays back to the ground state ( $P_{^3\mathrm{P}_1}$ ; Fig. 2d, green)

![](images/8a30f339f4ea50d0a8f23525b167ed494c25a04c26f8506c11a57e2adcbfaeb8.jpg)

![](images/8115cd94d2d81d156aadad742bcd760845e130be5bdd4cf31ff4e7e7d0c2fcb0.jpg)

![](images/a548f647c69759cdee3a70d8a3494de26f686587fc834b749d2e3b6e2f40ca4f.jpg)  
Fig. 3 | Atom-photon entanglement. a, Arrival histogram of single photons in excellent agreement with the expected  $\tau^{3}D_{1}\approx 330$  ns. b, Atom-photon measurement correlation plots in the ZZ basis (top) and XX basis (bottom); dashed lines represent ideal correlations. We find a strong correlation between the qubit and photon in the ZZ basis, with a raw correlation of 0.971(4). c, Parity contrast of the atom-photon Bell state versus the qubit readout phase with a raw fringe contrast of 0.83(3).

and by swapping the population between the ground and clock states  $(P_{3}{}_{\mathrm{P_0}};$  Fig.2d,red). The sum of the two is consistent with  $1 - P_{3}\mathrm{p}_{2}\approx 0.99$  Our measurements suggest a corrected  $\pi$  pulse (2π-pulse) fidelity of 0.94(5)(0.96(3)). The Rabi frequency of the  ${}^{3}\mathrm{P}_{0}\leftrightarrow{}^{3}\mathrm{D}_{1}$  telecom transition was chosen to minimize the population in the  ${}^{3}\mathrm{D}_{1},F = 3 / 2,m_{F} = 1 / 2$  state after a  $\pi$  -pulse. This magic Rabi frequency is illustrated in Fig. 2a and described in the Methods.

# Characterizing single photons and atom-photon entanglement

To characterize the photons, we begin by collecting them from the spontaneous emission of atoms in  $|\uparrow \rangle$ , sending them over a 50-m fibre link, and detecting them with a superconducting nanowire single-photon detector (SNSPD). The combined photon collection and transmission efficiency through the 50-m fibre is  $0.5\%$  (Methods). A histogram of the single-photon arrival times (Fig. 3a) shows excellent agreement with the expected  $\tau^{3}\mathrm{D}_{1} \approx 330$  ns.

Time-bin entanglement generates the atom-photon Bell state  $|\psi \rangle = (|\uparrow ,E\rangle +\mathrm{e}^{\mathrm{i}\phi}|\downarrow ,L\rangle) / \sqrt{2}$ , where  $|E\rangle$  and  $|L\rangle$  denote single-photon states in the early and late bins, respectively<sup>19</sup>. Compared with polarization-encoded photonic qubits, time-bin encoding is robust against polarization drifts and is naturally suitable for higher-dimensional (qudit) encoding. As shown in Fig. 1c, the process begins by performing a  $\pi/2$ -pulse on the qubit initialized in  $|\uparrow \rangle$  followed by a  $\pi$ -pulse on the telecom transition. The  $\pi$ -pulse is applied only to  $|\uparrow \rangle$ , which then scatters a telecom photon and returns to  $|\uparrow \rangle$ , generating entanglement between the nuclear spin states  $|\uparrow \rangle$  and  $|\downarrow \rangle$  and the photon number states  $|1\rangle$  and  $|0\rangle$ . We then perform a second round such that both components of the atomic superposition have an associated photon emission. Hence, we perform a  $\pi$ -pulse on the qubit followed by a second  $\pi$ -pulse on the telecom transition. Now, the qubit component that was initially  $|\downarrow \rangle$  has an associated photonic state  $|L\rangle$ , and we have generated the time-bin encoded atom-photon Bell state  $|\psi \rangle$  (up to a  $\pi$ -pulse on the qubit) with a protocol that is robust to photon loss and imperfect detection.

We collect single photons from a single atom with a high-numerical-aperture microscope objective, and image them with a 1:1 telescope onto a single SMF-28 single-mode telecom fibre (Fig. 1a; the fibre array will be discussed below). Single photons generated from the attempt

loop are then sent directly to an SNSPD via a single-mode fibre in which their arrival times are tagged. We observe a combined collection and transmission efficiency of  $\eta_{\mathrm{net}} \approx 0.5\%$  from an atom through a single-mode fibre. For comparison, our imaging system for fluorescence detection has an  $-4\%$  atom-to-camera collection efficiency, but the use of a single-mode fibre introduces another reduction factor since the dipole radiation pattern—particularly for the stretched transition and geometry used here—has limited overlap with a Gaussian mode. Additionally, there are other losses from polarization and wavelength filtering optics.

To perform tomography on the photonic qubits and the atom-photon Bell pairs, we use a TDI (Fig. 1d). The length of the long arm  $L_{\mathrm{d}}$  is chosen to match the time delay between the two bins,  $t_{\mathrm{d}}$  (Fig. 1c).  $t_{\mathrm{d}}$  is primarily limited by the spontaneous emission time of  $^3\mathrm{D}_1$ , as the atom must fully decay from the excited state after each round of excitation. Since  $\tau^{3}\mathrm{D}_{1} \approx 330$  ns, we choose  $t_{\mathrm{d}} = 2.8$  μs such that under the best condition,  $\exp \left(-\left(t_{\mathrm{d}} - \tau_{\pi}^{m}\right) / \tau^{3}\mathrm{D}_{1}\right) \approx 0.002$  with  $\tau_{\pi}^{m} \approx 700$  ns is substantially smaller than the infidelity caused by other imperfections. The concomitant fibre delay length on the long arm is  $L_{\mathrm{d}} = ct_{\mathrm{d}} = 560$  m, where  $c$  is the speed of light in fibre. We note that the motion of the atom during this time would result in a dephasing of the emitted photon between the two bins. Hence, we must either match the time delay with the period of motion of the atom in the trap or choose a time delay that is much shorter than the trap period. We take the second approach, and we expect a reduction in the Bell state fidelity of -0.009 (Methods).

To study atom-photon entanglement—and towards the eventual goal of atom-atomentanglement—we choose atimewindow of  $t_{\mathrm{det}} = 520$  ns in which we count events. The probability of dark counts on the SNSPDs during  $t_{\mathrm{det}}$  is  $P_{\mathrm{d.c.}} \approx 3 \times 10^{-6}$ , and the effective signal-to-noise ratio for ZZ (XX)-basis measurements is 19.6 (11.6) dB (Methods). Note that the TDI, which adds substantial losses, is only required for the XX data.

Next, we use the time-bin protocol and characterize the atom-photon Bell state in the  $Z$  basis for both atom and photon: we measure the atom in  $|\downarrow\rangle$  or  $|\uparrow\rangle$  and the photon in  $|E\rangle$  or  $|L\rangle$ . Details of the attempt loop are provided in the Methods; briefly, we attempt 128 times and the reset protocol between attempts includes  $t_{\mathrm{cool}} = 1.4$  ms of cooling. The success rate of generating atom-photon entanglement is limited by a combination of  $\eta_{\mathrm{net}}$ ,  $t_{\mathrm{cool}}$  and the atom reload time ( $t_{\mathrm{load}} \approx 1.1$  s) between each attempt loop. These factors limit the success rate to sub-Hertz, but many improvements are possible (see the 'Concluding discussion' section) and parallelization can boost the effective rate by a factor of  $N$ . As shown in Fig. 3b (top), we find a strong correlation between the qubit and photon in the ZZ basis. In fact, the infidelity is dominated by the readout error of the qubit (which requires a clock π-pulse back to the ground state). The Methods provide further details.

To completely characterize the atom-photon Bell state fidelity, we must measure the atom and photon in the the XX and YY bases. For the photon, this requires the use of a TDI (Fig. 1d and Methods), as discussed above. To ensure that the  $|E\rangle$ $(|L\rangle)$  component of the photonic state goes through the long (short) arm of the TDI, we use a Pockel's cell at the input to switch the path for each bin. As shown in Fig. 3c, we acquire a visibility fringe by varying the qubit measurement basis. We show the highest XX visibility condition in Fig. 3b (bottom). The fringe combined with the ZZ-basis measurements are sufficient to characterize the atom-photon Bell state fidelity to within a bound (Methods). We obtain a raw fidelity of  $0.90(1) \pm 0.014(3)_{\mathrm{bound}}$ . However, we note that this value is limited by the infidelity of transferring to the readout state (-0.02) and the infidelity of readout itself (-0.03). We, thus, calculate the atom-measurement-corrected Bell state fidelity (Methods) to be  $0.950(9) \pm 0.005(3)_{\mathrm{bound}}$ . Moreover, photon measurement errors contribute -0.037 to our infidelity (Methods) and can be removed with straightforward upgrades.

![](images/8aed540c170d69dfa3ddcf18af7557d2658fa941c7e97d064174dffa16d5ec51.jpg)  
a  
b

![](images/a849c01251847942b75aeb035e43cd0b48c9f8302846832c239a7eee3968accc.jpg)  
C  
Fig. 4 | Parallelization with a fibre array. a,b, We envision two atom array nodes in which the atom arrays in each are mapped to fibre arrays. The fibre arrays are directed to an integrated 50:50 BS array on a photonic chip whose outputs are then directed to arrays of SNSPDs. c, We study the atom-photon entanglement fidelity as a function of site index along the array. The inset shows one example histogram measured for one site. d, We also study the crosstalk between channels by studying the relative photon collection efficiency from an atom on nearby sites. For  $|\Delta x| \geq 1$ , we find an averaged crosstalk of -13.7(4) dB, limited by an estimated noise floor (shaded region) of -13.6(8) dB for this measurement. The inset shows scaled photon counts collected into the fibre array post-selected on atom presence at different tweezer sites.

![](images/c3036dd5759c7cf36e576325af94d35665ce5f57a52268319d530237eb424f7c.jpg)  
d

# Parallelized networking with a fibre array

With a combined photon collection and transmission efficiency through fibre of  $\eta_{\mathrm{net}}$ , parallelization over  $N \approx 1 / \eta_{\mathrm{net}}$  or  $N \approx 1 / \eta_{\mathrm{net}}^2$  channels would ensure a high success probability of establishing atom-photon or atom-atom entanglement in a single attempt, respectively. The attempt rate could be  $\sim 10^{5} \mathrm{s}^{-1}$ , limited by atomic properties such as decay rates and qubit rotation rates. Parallelization could be realized with optical fibre arrays; fibre bundles are ubiquitous in the telecom industry. Since absolute path length (phase) stability is not required for time-bin encoding, we do not anticipate fidelity limitations associated with using an array of fibres.

In the context of remote atom-atom entanglement using two atom arrays (Fig. 4a), we envision the use of a 50:50 beamsplitter (BS) array (Fig. 4b). In the telecom band, it is straightforward to use silicon integrated photonics $^{49,50}$  with two fibre array inputs into the BS array and two fibre array outputs after the BS array to direct the photons to SNSPD arrays $^{51-53}$ . The BS array could even be directly integrated with the SNSPD array. The click pattern on the SNSPD array would indicate which atomic Bell pair(s) succeeded on a given attempt, and the remaining atoms in each array that failed to generate a remote Bell pair could be used as a resource for the subsequent quantum circuit or subsequent attempts.

As a step towards this vision, we show that an array of atoms can be efficiently and independently mapped to an array of single-mode telecom fibres. We use a lensed fibre array to better match the 'form factor' of the atom array with that of the fibre array (Fig. 4a). The core pitch of the fibre array is  $d_{\mathrm{p}} \approx 80~\mu \mathrm{m}$  and the mode field diameter

(MFD) is  $d_{\mathrm{MFD}} \approx 10 \mu \mathrm{m}$ . To match this  $d_{\mathrm{MFD}} / d_{\mathrm{p}} \approx 13\%$  form factor with the atom array given the diffraction-limited spot diameter at  $1,389 \mathrm{~nm}$  of  $\sim 3 \mu \mathrm{m}$ , we choose a tweezer spacing of  $\sim 20 \mu \mathrm{m}$ , which is approximately four times as large as our nominal array spacing (Fig. 1a). We, thus, parallelize over  $N = 5$  channels (although we use a 20-site fibre array).

As shown in Fig. 4c, we find a relatively uniform Bell state fidelity. These data do not include the bound, but we assume that they are again comparable with our statistical uncertainty. Crucially, we do not observe crosstalk between the sites at the  $-13.6(8)$ -dB level corresponding to our average noise floor (Fig. 4d). We characterize the crosstalk by looking at the locations of atoms in the array and the locations of detected photons. With only two SNSPD channels, we study these correlations in a pairwise fashion (Fig. 4d, inset). The furthest pair measured are distanced by three sites, but we note that the crosstalk is already at the noise floor at a distance of one. These techniques are scalable to thousands of sites. Moreover, it is possible to increase the form factor by changing the lens design on the fibre to increase the MFD. With a realistic MFD of  $\sim 30\mu \mathrm{m}$ , the form factor matches that of a typical neutral atom and trapped ion arrays.

# Preserving coherence and establishing remote entanglement

Finally, we demonstrate a technique to enable the preservation of coherence of memory qubits and establishing remote entanglement between communication qubits. In the context of distributed quantum computing, it will be essential to establish entanglement between modules in a 'mid-circuit' manner in which the computations within the modules are ongoing. For long-distance quantum networking with intermediate quantum repeaters, rate optimization requires the ability to store successfully generated Bell pairs as memory and connecting the remaining links. This need is particularly acute for multiplexed approaches[28]. Accordingly, the coherence of the data/memory qubits must be completely unaffected by the operations of the communication qubits. Figure 1b illustrates this vision.

Paralleling the development of techniques for MCM in which some qubits are measured and the coherence of the others is preserved, mid-circuit networking (MCN) can be accomplished in several ways. Four main techniques have emerged for MCM: (1) shelving, in which data qubits are preserved in a portion of the atomic structure that is completely decoupled from the readout operations $^{40,43,54,55}$ ; (2) dual-species approaches in which the transition frequencies are sufficiently different between two species such that the readout of one does not affect the other $^{56,57}$ ; (3) shielding of data qubits with local light shifts that are sufficiently large to decouple them from readout operations $^{58,59}$ ; and (4) zoning techniques by which coherent transport is performed between spatially separated readout and memory zones $^{60,61}$ . Here we demonstrate an approach to MCN based on both shielding with a local light shift at 1,389 nm (Fig. 5a) and shelving.

Although ytterbium-171 is well suited for the shelving technique, our atom-photon entanglement scheme involves both ground state and metastable 'clock' state since the decay probability to the ground state is  $\sim 35\%$  per attempt. As discussed above and shown in Fig. 5b (Methods), each attempt involves a reset operation in the clock state (depumping to the ground state) and the ground state (OP to  $m_{F} = -1 / 2$ ). These are followed by a  $\pi$ -pulse on the optical clock transition to initialize the communication qubits in  ${}^{3}\mathrm{P}_{0}m_{F} = 1 / 2$  (see above). Since both OP and clock operations directly couple to the ground state, they preclude the use of the ground nuclear spin as a data qubit. Our approach uses a light shift by focusing 1,389-nm light onto a single atom (Fig. 5a and Methods) to shield the data qubits during the OP and clock operations. All other networking operations occur in the metastable manifold for which our data qubits are unaffected—the core principle behind the shelving-type MCM approach—and the light shift is off.

The shielding approach relies on a large differential light shift between the two states of interest. In our case, OP is performed on the

![](images/edadb385fb8a74541af853809cf8583ee0715d2518770b9b10c02dc294c85511.jpg)  
a

![](images/83655bdaaa42a5900e6e72244c36c0e83d785d726b84ed148a67cf4acdf9f4be.jpg)  
b  
C  
d

![](images/53b65a143aa8ec4247eddf26a9132fd5a0df712626e5127592048a8df7148af6.jpg)  
Fig. 5 | MCN. a, A local light shift of the  $^3\mathrm{P}_0$  and  $^3\mathrm{P}_1$  states from a tightly focused 1,389-nm beam 'shields' that site (data qubit; red) from the remote entanglement protocol applied to the other sites (communication qubits; blue). b, The remote entanglement protocol contains many operations from the metastable state as well as two operations from the ground state. The local light shift causes those two ground-state operations to be substantially off-resonant for the data qubit that is stored in the ground nuclear spin. c, A Ramsey fringe of the ground nuclear spin qubit for the data site (red; large) and communication sites (blue; inset) with (circle; solid line) and without (square; dashed line) the OP pulse applied. d, A Ramsey fringe of the ground nuclear spin qubit for the data qubit (red; large) with (circle; solid line) and without (square; dashed line) the clock pulse applied. The inset shows the population in the ground state for the data qubit (red) and communication qubits (blue) as the clock pulse is applied.

![](images/cadaa4830db33c669e42bb4b6fb17d0b912360099fcae269a1fb9f73c7387c49.jpg)

${}^{1}\mathrm{S}_{0} \leftrightarrow {}^{3}\mathrm{P}_{1}, F = 3/2$  transition for which the polarizability ratio is  $\alpha_{3\mathrm{P}_{1}} / \alpha_{1\mathrm{S}_{0}} \approx -8$  at  $1,389~\mathrm{nm}$  (ref. 62). Technical issues prevent us from using more than one data qubit and limit our light shift on the OP transition to  $\Delta_{\mathrm{LS}}^{\mathrm{OP}} 2\pi \times 2\mathrm{MHz}$ . Nevertheless, we find this shift to be sufficient to preserve Ramsey coherence of our data qubit. As shown in Fig. 5c, we can look at a Ramsey fringe by delaying the second  $\pi/2$ -pulse on a scale commensurate with the Larmor precession at  $\omega_{\mathrm{g}} \approx 2\pi \times 89\mathrm{kHz}$ . We use a delay time of approximately  $10\mathrm{ms}$ , during which we apply the  $1,389$ -nm shield beam to the data qubit, and conditionally apply the OP pulse for  $20~\mu\mathrm{s}$ . We find that the contrast of the Ramsey fringe of the data qubit has reduced by  $-5(1)\%$  and that the qubit has undergone a phase shift of  $1.01(6)$  rad. Meanwhile, the coherence of all the non-shielded atoms is completely lost.

The shielding of the optical clock pulse, by contrast, requires much lower intensity. We operate the  $1,389\mathrm{-nm}$  beam at a detuning of  $+612\mathrm{MHz}$  from the  ${}^{3}\mathrm{P}_{0}\leftrightarrow{}^{3}\mathrm{D}_{1},F = 3 / 2$  transition, for which the differential polarizability is  $\alpha_{3\mathrm{P_0}} / \alpha_{1\mathrm{S_0}}\approx -2\times 10^5$ . Accordingly, only  $-0.01\mu \mathrm{W}$  is needed to apply a light shift  $\Delta_{\mathrm{LS}}^{\mathrm{Clock}}\approx 2\pi \times 1\mathrm{MHz}$  to the data qubit's clock transition. As shown in Fig. 5d, this is sufficient to completely block the clock transition for the data qubit and leaving the transition for all other sites unaffected. We again show the preservation of Ramsey coherence on the data qubit with and without this clock pulse operation, finding a small reduction in the coherence of  $-0.3(3)\%$ . We are confident that this technique can be readily extended to many data qubits with sufficient power (or by using  $1,539\mathrm{-nm}$  light, close to the

${}^{3}\mathrm{P}_{1}\leftrightarrow{}^{3}\mathrm{D}_{1}$  transition, for shielding from OP and cooling instead of  $1,389~\mathrm{nm})$  , and that a stronger shield would enable the preservation of coherence of the data qubits and undergo tens or hundreds of attempts needed for heralded remote entanglement.

# Concluding discussion

We have demonstrated parallelizable, high-fidelity atom-photon entanglement in the telecom band in an array of ytterbium-171 atoms. There are many straightforward improvements that could increase both rate and fidelity. Although still using a microscope objective to collect photons, the collection efficiency could be improved with better mode matching to the fibre and with aberration correction. Additionally, the number and rate of attempts per loop could potentially be increased if the tweezers could be quickly switched off during the telecom pulses to reduce heating and loss. It is also possible to use a tweezer array reservoir<sup>63</sup> or continuous reloading<sup>64,65</sup> to further mitigate this cost.

The error budget for our atom-photon Bell state is discussed in the Methods. Our atom-measurement-corrected fidelity  $0.950(9) \pm 0.005(3)_{\mathrm{bound}}$  is limited by mundane effects such as detector dark counts ( $\sim 0.021$ ) and finite visibility of the interferometer fringe ( $\sim 0.016$ ). Both would disappear by improving the collection efficiency with an optical cavity and by directly studying atom-atom entanglement. The remaining infidelity ( $\sim 0.013$ ) is dominated by atomic motion between the time bins (0.009) and decay during the Raman pulse (0.0035), which could both be improved by Purcell-enhancing the emission rate with an optical cavity.

The use of anoptical cavity $^{31,59,60,66-68}$  or an array of optical cavities $^{32-35}$  would substantially improve the rate. The collection efficiency could be increased from approximately  $0.5\%$  to  $50\%$ , giving an approximately  $10^{2}$ -fold ( $10^{4}$ -fold) boost to the atom-photon (atom-atom) entanglement rate. Moreover, the Purcell enhancement of the desired decay path would drastically improve the effective branching fraction. These advantages are discussed in detail in the Methods. Additionally, the improved success rate would have the secondary benefit that the effects of heating and loss are mitigated (Methods describes atomic heating and loss throughout the entanglement attempt loop). Our parallelized scheme based on a fibre array is fully compatible with both nanophotonic $^{34}$  and free-space high-numerical-aperture $^{35}$  cavity arrays, for which we anticipate that the atom-atom entanglement rate could approach  $-N \times 10^{5} \mathrm{~s}^{-1}$ , where  $N$  is the number of channels, which quickly surpasses the clock rate of neutral atom processors $^{61,69}$ .

Finally, we envision many new scientific directions that are uniquely enabled by our work. First, our work is a major step towards the quantum networking of atomic processors for distributed $^{10,11}$  or blind $^{7,9}$  quantum computing. Our demonstration of MCN enables the efficient scheduling of algorithms that involve both intra- and intermodule two-qubit gates $^{10,11}$ . Additionally, our use of ytterbium opens the door to establishing a quantum network of optical atomic clocks $^{5,6}$ , which could be used for the quantum-secured dissemination of a time standard $^{5}$  or for the distributed quantum sensing of spatially extended phenomena ranging from gravity $^{70-72}$  to dark matter $^{73,74}$ .

# Online content

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41567-025-03022-4.

# References

1. Gisin, N., Ribordy, G., Tittel, W. & Zbinden, H. Quantum cryptography. Rev. Mod. Phys. 74, 145-195 (2002).  
2. Pirandola, S. et al. Advances in quantum cryptography. Adv. Opt. Photon. 12, 1012 (2020).

3. Gottesman, D., Jennewein, T. & Croke, S. Longer-baseline telescopes using quantum repeaters. Phys. Rev. Lett. 109, 070503 (2012).  
4. Malia, B. K., Wu, Y., Martinez-Rincón, J. & Kasevich, M. A. Distributed quantum sensing with mode-entangled spin-squeezed atomic states. Nature 612, 661-665 (2022).  
5. Kómar, P. et al. A quantum network of clocks. Nat. Phys. 10, 582-587 (2014).  
6. Nichol, B. C. et al. An elementary quantum network of entangled optical atomic clocks. Nature 609, 689-694 (2022).  
7. Wootters, W. K. & Zurek, W. H. A single quantum cannot be cloned. Nature 299, 802-803 (1982).  
8. Barz, S. et al. Demonstration of blind quantum computing. Science 335, 303-308 (2012).  
9. Fitzsimons, J. F. Private quantum computation: an introduction to blind quantum computing and related protocols. npj Quantum Inf. 3, 23 (2017).  
10. Jiang, L., Taylor, J. M., Sorensen, A. S. & Lukin, M. D. Distributed quantum computation based on small quantum registers. Phys. Rev. A 76, 062323 (2007).  
11. Monroe, C. et al. Large-scale modular quantum-computer architecture with atomic memory and photonic interconnects. Phys. Rev. A 89, 022317 (2014).  
12. Stephenson, L. J. et al. High-rate, high-fidelity entanglement of qubits across an elementary quantum network. Phys. Rev. Lett. 124, 110501 (2020).  
13. Hensen, B. et al. Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres. Nature 526, 682-686 (2015).  
14. van Leent, T. et al. Entangling single atoms over 33km telecom fibre. Nature 607, 69-73 (2022).  
15. Krutyanskiy, V. et al. Telecom-wavelength quantum repeater node based on a trapped-ion processor. Phys. Rev. Lett. 130, 213601 (2023).  
16. Uysal, M. T. et al. Spin-photon entanglement of a single  $\mathrm{Er}^{3+}$  ion in the telecom band. Phys. Rev. X 15, 011071 (2025).  
17. Covey, J. P., Weinfurter, H. & Bernien, H. Quantum networks with neutral atom processing nodes. npj Quantum Inf. 9, 90 (2023).  
18. Moehring, D. L. et al. Entanglement of single-atom quantum bits at a distance. Nature 449, 68-71 (2007).  
19. Bernien, H. et al. Heralded entanglement between solid-state qubits separated by three metres. Nature 497, 86-90 (2013).  
20. Bhaskar, M. K. et al. Experimental demonstration of memory-enhanced quantum communication. Nature 580, 60-64 (2020).  
21. Ruskuc, A. et al. Multiplexed entanglement of multi-emitter quantum network nodes. Nature 639, 54-59 (2025).  
22. Stolk, A. et al. Telecom-band quantum interference of frequency-converted photons from remote detuned NV centers. PRX Quantum 3, 020359 (2022).  
23. Bersin, E. et al. Telecom networking with a diamond quantum memory. PRX Quantum 5, 010303 (2024).  
24. Zhong, T. et al. Nanophotonic rare-earth quantum memory with optically controlled retrieval. Science 357, 1392-1395 (2017).  
25. Dibos, A. M., Raha, M., Phenicie, C. M. & Thompson, J. D. Atomic source of single photons in the telecom band. Phys. Rev. Lett. 120, 243601 (2018).  
26. Kindem, J. M. et al. Control and single-shot readout of an ion embedded in a nanophotonic cavity. Nature 580, 201-204 (2020).  
27. Hucul, D. et al. Modular entanglement of atomic qubits using photons and phonons. Nat. Phys. 11, 37-42 (2015).  
28. Hui, W., Menon, S. G., Bernien, H. & Covey, J. P. Multiplexed telecommunication-band quantum networking with atom arrays in optical cavities. Phys. Rev. Res. 3, 043154 (2021).

29. Li, Y. & Thompson, J. D. High-rate and high-fidelity modular interconnects between neutral atom quantum processors. PRX Quantum 5, 020363 (2024).  
30. Canteri, M. et al. A photon-interfaced ten qubit quantum network node. Phys. Rev. Lett. 135, 080801 (2025).  
31. Hartung, L., Seubert, M., Welte, S., Distante, E. & Rempe, G. A quantum-network register assembled with optical tweezers in an optical cavity. Science 385, 179-183 (2024).  
32. Trupke, M. et al. Atom detection and photon production in a scalable, open, optical microcavity. Phys. Rev. Lett. 99, 063601 (2007).  
33. Derntl, C. et al. Arrays of open, independently tunable microcavities. Opt. Express 22, 22111-22120 (2014).  
34. Menon, S. G., Glachman, N., Pompili, M., Dibos, A. & Bernien, H. An integrated atom array-nanophotonic chip platform with background-free imaging. Nat. Commun. 15, 6156 (2024).  
35. Shadmany, D. et al. Cavity QED in a high NA resonator. Sci. Adv. 11, eads8171 (2025).  
36. Sunami, S., Tamiya, S., Inoue, R., Yamasaki, H. & Goban, A. Scalable networking of neutral-atom qubits: nanofiber-based approach for multiprocessor fault-tolerant quantum computer. PRX Quantum 6, 010101 (2025).  
37. Huie, W. et al. Repetitive readout and real-time control of nuclear spin qubits in  $^{171}\mathrm{Yb}$  atoms. PRX Quantum 4, 030337 (2023).  
38. Jenkins, A., Lis, J. W., Senoo, A., McGrew, W. F. & Kaufman, A. M. Ytterbium nuclear-spin qubits in an optical tweezer array. Phys. Rev. X 12, 021027 (2022).  
39. Morigi, G., Eschner, J. & Keitel, C. H. Ground state laser cooling using electromagnetically induced transparency. Phys. Rev. Lett. 85, 4458-4461 (2000).  
40. Lis, J. W. et al. Midcircuit operations using the omg architecture in neutral atom arrays. Phys. Rev. X 13, 041035 (2023).  
41. Barnes, K. et al. Assembly and coherent control of a register of nuclear spin qubits. Nat. Commun. 13, 2779 (2022).  
42. Chen, N. et al. Analyzing the Rydberg-based optical-metastable-ground architecture for  $^{171}\mathrm{Yb}$  nuclear spins. Phys. Rev. A 105, 052438 (2022).  
43. Ma, S. et al. High-fidelity gates and mid-circuit erasure conversion in an atomic qubit. Nature 622, 279-284 (2023).  
44. Peper, M. et al. Spectroscopy and modeling of  $^{171}\mathrm{Yb}$  Rydberg states for high-fidelity two-qubit gates. Phys. Rev. X 15, 011009 (2025).  
45. Muniz, J. A. et al. High-fidelity universal gates in the  $171\mathrm{Yb}$  ground state nuclear spin qubit. PRX Quantum 6, 020334 (2025).  
46. Madjarov, I. S. et al. High-fidelity entanglement and detection of alkaline-earth Rydberg atoms. Nat. Phys. 16, 857-861 (2020).  
47. Li, L., Huie, W., Chen, N., DeMarco, B. & Covey, J. P. Active cancellation of servo-induced noise on stabilized lasers via feedforward. Phys. Rev. Appl. 18, 064005 (2022).  
48. Saha, S. et al. High-fidelity remote entanglement of trapped atoms mediated by time-bin photons. Nat. Commun. 16, 2533 (2025).  
49. Carolan, J. et al. Universal linear optics. Science 349, 711-716 (2015).  
50. Pelucchi, E. et al. The potential and global outlook of integrated photonics for quantum technologies. Nat. Rev. Phys. 4, 194-208 (2021).  
51. Wollman, E. E. et al. Kilopixel array of superconducting nanowire single-photon detectors. Opt. Express 27, 35279-35289 (2019).  
52. Oripov, B. G. et al. A superconducting nanowire single-photon camera with 400,000 pixels. Nature 622, 730-734 (2023).  
53. Fleming, F. et al. High-efficiency, high-count-rate 2D superconducting nanowire single-photon detector array. Opt. Express 33, 27602-27614 (2025).

54. Shaw, A. L. et al. Erasure cooling, control, and hyperentanglement of motion in optical tweezers. Science 388, 845-849 (2025).  
55. Graham, T. M. et al. Mid-circuit measurements on a neutral atom quantum processor. Phys. Rev. X 13, O41051 (2023).  
56. Singh, K. et al. Mid-circuit correction of correlated phase errors using an array of spectator qubits. Science 380, 1265-1269 (2023).  
57. Nakamura, Y. et al. A hybrid atom tweezer array of nuclear spin and optical clock qubits. Phys. Rev. X 14, 041062 (2024).  
58. Norcia, M. A. et al. Midcircuit qubit measurement and rearrangement in a  $^{171}\mathrm{Yb}$  atomic array. Phys. Rev. X 13, 041034 (2023).  
59. Hu, B. et al. Site-selective cavity readout and classical error correction of a 5-bit atomic register. Phys. Rev. Lett. 134, 120801 (2025).  
60. Deist, E. et al. Mid-circuit cavity measurement in a neutral atom array. Phys. Rev. Lett. 129, 203602 (2022).  
61. Bluvstein, D. et al. Logical quantum processor based on reconfigurable atom arrays. Nature 626, 58-65 (2024).  
62. Tang, Z.-M., Yu, Y.-M. & Dong, C.-Z. Determination of static dipole polarizabilities of Yb atom. Chinese Phys. B 27, 063101 (2018).  
63. Endres, M. et al. Atom-by-atom assembly of defect-free one-dimensional cold atom arrays. Science 354, 1024-1027 (2016).  
64. Norcia, M. A. et al. Iterative assembly of  $^{17}\mathrm{Yb}$  atom arrays with cavity-enhanced optical lattices. PRX Quantum 5, 030316 (20  
65. Gyger, F. et al. Continuous operation of large-scale atom arrays in optical lattices. Phys. Rev. Res. 6, 033104 (2024).  
66. Periwal, A. et al. Programmable interactions and emergent geometry in an array of atom clouds. Nature 600, 630-635 (2021).  
67. Peters, M. L. et al. Cavity-enabled real-time observation of individual atomic collisions. Preprint at https://arxiv.org/abs/2411.12622 (2024).

68. Grinkemeyer, B. et al. Error-detected quantum operations with neutral atoms mediated by an optical cavity. Science 387, 1301-1305 (2025).  
69. Graham, T. M. et al. Multi-qubit entanglement and algorithms on a neutral-atom quantum computer. Nature 604, 457-462 (2022).  
70. Pfister, C. et al. A universal test for gravitational decoherence. Nat. Commun. 7, 13022 (2016).  
71. Borregaard, J. & Pikovski, I. Testing quantum theory on curved space-time with quantum networks. Phys. Rev. Research 7, 023192 (2025).  
72. Covey, J. P., Pikovski, I. & Borregaard, J. Probing curved spacetime with a distributed atomic processor clock. PRX Quantum 6, 030310 (2025).  
73. Wcisto, P. et al. New bounds on dark matter coupling from a global network of optical atomic clocks. Sci. Adv. 4, eaau4869 (2018).  
74. Kennedy, C. J. et al. Precision metrology meets cosmology: improved constraints on ultralight dark matter from atom-cavity frequency comparisons. Phys. Rev. Lett. 125, 201302 (2020).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

© The Author(s), under exclusive licence to Springer Nature Limited 2025

# Methods

# Experimental details

Experimental layout. The experimental apparatus is shown in Extended Data Fig. 1, with light paths drawn for components relevant to our multilevel control of the atom array (Fig. 2). Namely, we load atoms into a 20-site linear chain of optical tweezers with a spacing of  $\sim 4.7\mu \mathrm{m}$ , a depth of  $\sim 500\mu \mathrm{K}$  and a wavelength of  $\sim 760\mathrm{nm}$ . The tweezer array is oriented vertically (along  $z$ ). Imaging of the atom array in the ground state is performed by collecting photons scattered through the  $F = 3/2$  manifold of the  ${}^{3}\mathrm{P}_{1}$  transition at  $120\mathrm{G}$  with a microscope objective opposite to an identical objective that is used to form the tweezers. The collected photons are imaged onto an electron-multiplying charge-coupled device. Ref. 37 provides more details.

The clock beam that drives the atom from  $|g_{-}\rangle = |^{1}\mathrm{S}_{0}$ ,  $F = 1/2$ ,  $m_{F} = -1/2$  to  $|\uparrow\rangle = |^{3}\mathrm{P}_{0}$ ,  $F = 1/2$ ,  $m_{F} = 1/2$  is delivered parallel to the magnetic field direction with  $\sigma_{+}$ polarization. Since the tweezer array is orientated along the direction of the magnetic field, the clock beam can be focused down to a waist of approximately  $35\mu \mathrm{m}$  without affecting the homogeneity of the Rabi frequency across the tweezer array. The telecom pulse beam that drives the atom from the  $|\uparrow\rangle$  to the  $|^{3}\mathrm{D}_{1}$ ,  $F = 3/2$ ,  $m_{F} = 3/2$  state propagates in the opposite direction to the clock beam, also with  $\sigma_{+}$ polarization. The waist of the telecom pulse beam is several times larger than that of the clock beam.

The telecom-band single photons are collected through the same objective that generates the tweezer array, which eliminates most of the common-mode mechanical noise from the objective. A dichroic mirror (Thorlabs DMSP1020B) is used to separate the 1,389-nm photons from the 760-nm tweezer light. Nevertheless, we measure a notable amount of noise photons entering the collection path, probably generated through a frequency downconversion process inside the objective. Additional cascaded narrow-band filters (CHROMAR51390/30) were, therefore, placed after the dichroic mirror. In the future, we plan to obviate this problem by quickly blinking off the tweezers during the photon collection window of several hundreds of nanoseconds. The single-photon collection path is a  $4f$  system that images the atom onto the fibre core with a magnification factor of 5. A picomotor-actuated mirror (Newport 8807) is used to adjust the alignment in the Fourier plane.

The Raman beam driving the metastable nuclear transition between  $|\uparrow \rangle$  and  $|\downarrow \rangle = |^3\mathrm{P}_0,F = 1 / 2,m_F = 1 / 2\rangle$  co-propagates with the OP beam. The Raman beam has a diameter of approximately  $1\mathrm{mm}$ , much larger than the length of the tweezer array (approximately  $100~{\mu\mathrm{m}}$ ). A polarizing beamsplitter (PBS) and a quarter-wave plate placed right before the glass cell adjusts the polarization of the Raman beam to a magic angle that maximizes the Rabi frequency and  $\pi$ -pulse fidelity (see the 'Raman gates of the metastable nuclear spin' section for further details).

The 1,389-nm light shift beam for the MCN experiment is sent through the same optical setup used to collect single photons from atoms (see the 'Single-photon detection' section). Currently, we can only provide  $\sim 4\mathrm{mW}$  of the 1,389-nm light to the atoms through the path with our microscope objective. Moreover, because of a focal shift between  $760\mathrm{nm}$  -the wavelength of the tweezers that defines the position of the atoms-and  $1,389\mathrm{nm}$  in our microscope objective, we are unable to focus a 1,389-nm spot to a waist radius smaller than  $\sim 3\mu \mathrm{m}$

Single-photon detection. The telecom-band photons are collected using the same objective lens (Special Optics customized coating including  $556\mathrm{nm}$ ,  $760\mathrm{nm}$  and  $1,389\mathrm{nm}$ ) that generates the tweezer array. Due to a chromatic shift of approximately  $50~{\mu\mathrm{m}}$  between the focus of a  $760\mathrm{-nm}$  beam and a  $1,389\mathrm{-nm}$  beam, the  $1,389\mathrm{-nm}$  photons collected through the objective are weakly divergent, and the 4fimaging system had to be tuned out of focus to compensate for this shift. Even with the focal shift corrected, the chromatic shift still introduces substantial aberrations to the spatial mode of the single photons,

reducing the collection efficiency because of non-optimal coupling to a single-mode fibre.

The magnification of the single-photon collection system is approximately 5 to best match a single-mode fibre (SMF-28) with a  $10 - \mu \mathrm{m}$  MFD, which we use to characterize atom-photon entanglement (Fig. 3).

The customized fibre array (Keystone Photonics) has a quoted MFD of  $30\mu \mathrm{m}$  at  $1,550\mathrm{nm}$ , and a spacing of  $82\mu \mathrm{m}$ , as per the manufacturer's specification. However, we observe an MFD of only  $10\mu \mathrm{m}$ , similar to that of the SMF-28 fibre. The smaller-than-quoted MFD requires the use of a much larger tweezer spacing to match the form factor of the fibre array, limiting the number of parallelized networking tweezer sites to 5 in this work.

We use an SNSPD (Quantum Opus One SN156, D10124) with two channels that work between  $1,300\mathrm{nm}$  and  $1,600\mathrm{nm}$  for single-photon detection. We optimize the bias currents for the two channels such that they operate close to the saturation point of their quantum efficiency without substantially raising the dark count rate. Typically, we measure the dark count rates to be approximately  $11\mathrm{Hz}$  for both channels, which we use as a reference to adjust the bias currents sporadically when needed.

Estimation of photon collection rate and signal-to-noise ratio. To calculate our single-photon collection efficiency, we estimate the number of photons emitted from the atom per attempt loop. For each excitation that drives the atom from  $^3\mathrm{P}_0$  to  $^3\mathrm{D}_1$ , there is a  $64\%$  chance that the atom decays back to  $^3\mathrm{P}_0$  to emit a 1,389-nm single photon, and  $1\%$  chance that the atom decays to the non-trappable  $^3\mathrm{P}_2$  state and is subsequently ejected. In the case where the atom decays to  $^3\mathrm{P}_0$ , there is an approximate  $3\%$  chance that the reset pulses pump the atom to  $^3\mathrm{P}_2$ . Given these loss mechanisms per attempt loop, we expect an exponentially decaying atom survival rate as a function of the number of attempt loops. We then ran Monte Carlo simulations of atom survival and single-photon emission for our typical experimental sequence. We ignore loss mechanisms from heating in the trap and finite vacuum lifetimes since our cooling routines keep the atom temperature well below the trap depth (Extended Data Fig. 2 shows the atomic temperature versus number of attempts), and the entanglement sequence is much shorter than our tweezer lifetime (approximately 10 s). We note that there are several different estimations for the branching ratio from the  $^3\mathrm{D}_1$  state[75-78] and we choose the one that we believe is the most accurate. Using branching ratios of 0.35, 0.64 and 0.01 (ref. 78) from  $^3\mathrm{D}_1$  to  $^3\mathrm{P}_1$ ,  $^3\mathrm{P}_0$  and  $^3\mathrm{P}_2$ , respectively, we simulated that an average of 23 single photons at 1,389 nm are emitted after 128 attempts, with an average atom survival rate of 0.28. We plot the measured photon arrival probabilities alongside the simulated atom survival rate against the number of attempts in Extended Data Fig. 2, which shows good agreement.

Given the expected number of photons to be emitted per experimental sequence, we estimate the photon collection efficiency to be approximately  $0.06\%$  for XX measurements and  $0.3\%$  for ZZ measurements. We note that these numbers represent the overall efficiency from the photon collection path (75%), TDI (20%, XX measurements only), quantum efficiency (70%) of the SNSPD and the truncated time window for photon triggering (520 ns). Taking the finite triggering window and atom survival rate into account, we also estimate the number of dark counts collected given the measured dark rates of the SNSPDs, and calculated the signal-to-noise ratio to be approximately 11.6 dB (19.6 dB) for XX (ZZ) measurements.

Timing and hardware: attempt loop. As mentioned in the 'Estimation of photon collection rate and signal-to-noise ratio' section, due to the low photon collection efficiency and limited atom loading efficiency in a single tweezer  $(-60\%)$ , the normal single-shot measurement is not suitable for the data collection of this experiment. According to the Monte Carlo simulation, the  $1/e$  lifetime of the atom is approximately

40 entanglement generation attempts, and we chose to perform 128 attempts in the experiment.

Each attempt loop can be divided into three parts: atomic state initialization, sub-Doppler cooling and entanglement generation. During state initialization, a depump pulse transfers the atoms in the  $|\uparrow \rangle$  state to the  $|g_{-}\rangle$  or  $|g_{+}\rangle$  state through the  $F = 3/2$  or  $F = 1/2$  manifold of the  $^3\mathrm{D}_1$  state. Then, a metastable Raman  $\pi$ -pulse and another depump pulse transfers atoms in the  $|\downarrow \rangle$  state to the ground state. Another round of metastable Raman  $\pi$ -pulse followed by a depump pulse is applied to remove any residual population in the  $|\downarrow \rangle$  state due to imperfect  $\pi$ -pulse fidelity of the metastable rotation.

Following state initialization, the atom in the ground state is cooled by an in-loop cooling sequence, which comprises grey molasses cooling for  $0.4\mathrm{ms}$  and electromagnetically induced transparency cooling for  $1\mathrm{ms}$ . A detailed description of our sub-Doppler cooling scheme is provided in the Supplementary Information. Without these cooling pulses, the atom temperature rises to approximately  $17~\mu \mathrm{K}$  after 128 attempts, resulting in poor clock pulse fidelity that substantially reduces the entanglement generation rate and atomic state detection fidelity.

During the REG sequence, a clock  $\pi$ -pulse first drives the atom from the  $|g_{-}\rangle$  state to  $|\uparrow\rangle$ . A Raman  $\pi/2$ -pulse then prepares the atom in a superposition state for time-bin entanglement. This Raman  $\pi/2$ -pulse is applied  $5\mu s$  before the first telecom excitation pulse to prevent photon leakage into the TDI during the first photon detection window. A detailed description of the interferometer is provided in the 'TDI' section. The Raman  $\pi$ -pulse is applied approximately  $1.2\mu s$  after the first telecom excitation pulse, such that spin-flip errors caused by spontaneous photon emission during the Raman pulse are suppressed. We estimate the spin-flip error to be approximately  $0.35\%$  for a  $1.2-\mu s$  delay and a  $0.7-\mu s$  Raman  $\pi$ -pulse. The spacing between the first and second telecom excitation pulses is adjusted to match the time delay of the interferometer. We note that the delay between the two telecom excitation pulses is chosen to maintain balance between reducing spin-flip errors (which decrease with a longer delay time) and reducing the dephasing errors from atomic motion (which increase with a longer delay time). Motional effects are further described in the 'Effects from atom motion between time bins' section.

We use real-time decision-making to conditionally branch out of the attempt loop on the detection of a photon in one of the two time bins. A microcontroller (Teensy 4.1) is connected to the single-photon detector to tag the arrival time of the photons relative to the trigger signal sent from the main experimental control system (NI field-programmable-gate-array-based digital I/O module controlled via Entangleware) that marks the detection window. After the successful detection of a photon within the predetermined window time (see the 'Single-photon detection and analysis window' section), the microcontroller makes a decision to run either a Z or an X measurement based on the specific time that a photon arrives. The real-time decision is made within 100 ns after the detection window ends, and a trigger signal is sent from the microcontroller to the home-made field-programmable gate array control system based on a field-programmable gate array evaluation board (Lattice Semiconductor LCMXO2-7000HE-B-EVN). After receiving the trigger signal, the home-made control system takes over a subset of channels from the main experimental control system and executes atomic state detection in the X or Z basis based on the command from the microcontroller. Control is given back to the main experimental control system after the execution of the state detection subroutine.

For atomic state measurements in the Z basis, a clock  $\pi$ -pulse transfers atomic population from  $|\uparrow\rangle$  to  $|g_{-}\rangle$  immediately after the entanglement generation sequence, and atoms in  $|\downarrow\rangle$  will remain in the  $^3\mathrm{P}_0$  state, which is dark to the ground-state imaging pulses. Due to finite atomic temperature, the tweezer depth is adiabatically lowered from  $500~\mu \mathrm{K}$  to  $50~\mu \mathrm{K}$  to improve the clock  $\pi$ -pulse fidelity. To further

improve atomic state readout fidelity, we apply a radio-frequency pulse $^{37}$  to transfer atoms from the  $|g_{-}\rangle$  state to  $|g_{+}\rangle$  and then a second clock  $\pi$ -pulse to transfer residual population in  $|\downarrow\rangle$  to  $|g_{-}\rangle$  that may remain due to limited clock pulse fidelity. To distinguish atom loss from the residual population in  $|\downarrow\rangle$ , a 500- $\mu$ s depump pulse transfers the  $|\downarrow\rangle$  state back to the ground state for a final round of readout. The X-basis measurement differs from the Z-basis measurement only by a Raman  $\pi/2$ -pulse at the beginning of the measurement sequence that rotates the projection axis into X.

Single-photon detection and analysis window. A 1.2-  $\mu$ s delay is placed between the first telecom excitation pulse and the Raman rotation pulse to minimize the spin-flip error from spontaneous decay. We, thus, program a 1.0-  $\mu$ s window immediately after the telecom excitation pulse during which the microcontroller may trigger the home-made control system to take over the main control system for atomic state detection if a single photon is detected. The arrival times of the single photons are tagged, and we post-select on such detections with a narrower time window within the aforementioned 1.0-  $\mu$ s experimental detection window as a part of data analysis. The exact position and width of the analysis window are optimized for best parity visibility (see the 'Atom-photon Bell state fidelity characterization' section for a detailed discussion on atom-photon Bell state fidelity) by reducing leak-through light from the telecom excitation/Raman pulses with a delayed window start, and by maximizing the signal-to-noise ratio with a narrower window width and retaining a number of collection events sufficient for statistical significance. Such analysis is performed separately for XX and ZZ atom-photon measurements due to differences in both experimental sequence and setup, but otherwise applied consistently with the same analysis window for all data measured under the same experimental procedure.

# The 1,389-nm laser system

The 1,389 nm laser is sourced from a Toptica DL pro that is offset-locked to a reference cavity using the Pound-Drever-Hall technique. Although the telecom excitation pulse is fast ( $\Omega \approx 30 \mathrm{MHz}$ ) and shares common-mode phase noise with the Raman pulse, we require laser noise feed-forward to remove differential phase noise in the emitted photons between the early and late time bins, which decreases the XX-basis measurement contrast with the interferometer (see the 'TDI' section for a detailed description of the interferometer). The locking cavity has a finesse of approximately  $5 \times 10^4$ , and approximately  $10~\mu \mathrm{W}$  of transmission light is beat with the laser output for feed-forward phase stabilization, applied after a 10-m delay fibre. We note that the optical delay for feed-forward is shorter than that in the clock laser setup mainly because of group delay difference of the radio-frequency band-pass filter after the photodiode.

REG pulse generation. We estimate that a Rabi frequency of approximately 30 MHz maximizes atom-photon entanglement fidelity at a  $B$  field of 120 G. A detailed analysis is provided in the 'Fidelity estimation of entanglement generation and tomography' section. We, thus, require a  $\pi$ -pulse time of approximately 15 ns for a square pulse, which is typically difficult to achieve with standard acousto-optic modulators (AOMs). At the same time, we wish to minimize leakage through the pulsing AOM on the microsecond scale that the REG loop takes place in. Since the two timescales differ by two orders of magnitude, the required extinction level of the telecom excitation pulse is above  $10\log_{10}[300^2] = 50$  dB.

To achieve both fast modulation and good extinction, we use a fast AOM with a 5.3-ns rise time and a modulation bandwidth of approximately  $100\mathrm{MHz}$  (Brimrose GPM-400-100-1389). However, the extinction ratio of this model is only approximately 30 dB (1,000:1). To achieve better extinction, we double-pass the light through this AOM with a Faraday rotator (Thorlabs II390R5) placed in front of the AOM. We use a

Faraday rotator instead of a quarter-wave plate because this model only works for horizontally polarized light. The efficiency of the double-pass setup is about  $12\%$  with approximately  $2.5\mathrm{mW}$  of 1,389-nm light delivered to the atoms. Due to the double-pass configuration and the limited rise time of the radio-frequency switch (5 ns), the total telecom excitation  $\pi$ -pulse duration is approximately 25 ns, with a 16-ns full-width at half-maximum and a Rabi frequency of approximately  $30\mathrm{MHz}$ .

Stabilized Raman pulse generation. Since the double-passed AOM for the 1,389-nm laser has a relatively low efficiency, the 1,389-nm laser power is divided with time-division multiplexing between the Raman and telecom excitation pulse systems by making use of the zeroth-order output of the excitation-pulse AOM. The zeroth-order light first passes through an intensity servo AOM that stabilizes the Raman pulse power delivered to the experiment.

The intensity-stabilized Raman light is first sent to a pulsing AOM with the output coupled to a short polarization-maintaining fibre that leads to the final set of optics before the atoms. A PBS is placed after the short fibre to ensure the purity of pulse polarization. A slow drift of Raman pulse power after the PBS can be observed due to the limited extinction in the polarization-maintaining fibre. Since the Raman Rabi frequency is directly proportional to the pulse power, slow power drift over an experimental sequence tens of hours long introduces non-negligible pulse errors. To further stabilize the pulse power, we briefly turn the AOM on to send a short pre-pulse at the beginning of every experimental sequence. A fast home-made peak detector with a sample-and-hold circuit measures this pre-pulse and adjusts the Raman pulse intensity servo set point accordingly. With this pulse amplitude feedback enabled, we achieve pulse intensity stability better than  $0.5\%$ .

# Raman gates of the metastable nuclear spin

We perform fast, high-fidelity metastable nuclear spin Raman Rabi oscillations via a single 1,389-nm laser beam perpendicular to the magnetic field. Unlike the previous demonstration in ref. 40, we intend to operate under a magnetic field of  $120\mathrm{G}$  for higher REG and readout fidelity, which can potentially introduce detuning errors during Rabi oscillation. Following our previous analysis in ref. 42, we look for a magic condition under which the differential Stark shift between the two nuclear spin states cancels the nuclear Zeeman splitting, thereby eliminating the detuning error during Raman rotations.

We study the magic condition when driving Raman transitions via the  $^3\mathrm{D}_1$ ,  $F = 3/2$  intermediate states. To minimize destructive interference between the two possible Raman paths, we fix the phase difference between the horizontal and vertical components of the Raman beam to  $\pi/2$  (ref. 38) by rotating the polarization of the Raman light with a quarter-wave plate. Under a magnetic field of  $120\mathrm{G}$  and with a blue-detuning from the  $m_{F} = 3/2$  substate by  $612\mathrm{MHz}$ , we vary the single-photon Rabi frequency  $\Omega$  and the ratio between the amplitude of the horizontal and vertical components  $\Omega_{\mathrm{H}} / \Omega_{\mathrm{V}} \equiv \tan \theta$  (perpendicular and parallel to the  $B$  field, respectively) and found a magic condition that gives  $< 10^{-3}$  infidelity for  $\pi$ -rotations (Extended Data Fig. 4a). The corresponding two-photon Rabi frequency  $\Omega_{\mathrm{eff}}$  under different parameter settings is shown in Extended Data Fig. 4b.

# TDI

Tomography of the time-bin-encoded photonic qubits is performed with a TDI (Extended Data Fig. 6), where a 560-m fibre (SMF-28) erases the which-bin information of the arriving photons.

To maximize the signal-to-noise ratio for XX-basis measurements, we use an amplitude-modulating EOM (Thorlabs EO-AM-NR-C3) to vary the polarization of the single photons, such that photons emitted after the first (second) excitation pulse are directed towards the fibre (free-space) arm of the interferometer (Fig. 1d). Fast modulation of the EOM voltage is driven by a home-made EOM amplifier using a high-voltage operational amplifier (APEX PA194).

The 500-m delay fibre is placed inside an insulated box for improved passive temperature stability. Two locking circuits are used for active stabilization against fluctuations in the relative path length in the interferometer. First, a 1,112-nm reference light (Pound-Drever-Hall-locked to the same cavity that 1,389-nm laser is locked to) of approximately 50 nW is injected with a dichroic mirror. The interference fringe is measured on a home-made InGaAs avalanche photodiode (APD) with a bandwidth of approximately 100 kHz, and subsequently fed into a home-made proportional-integral-derivative circuit to stabilize the phase of the interferometer using a piezoelectric fibre stretcher (Paulsson PZ2 high-efficiency fibre stretcher) with a home-made low-noise piezo driver that achieves a closed-loop bandwidth of about 10 kHz. The 1,112-nm locking beam power is chosen to suppress Raman scattering in the delay fibre to a level substantially below the inherent dark count rate of the SNSPD, which allows the interferometer to be locked to the 1,112-nm reference continuously during the REG loop. An additional free-space delay stage (Thorlabs VCFL35) with a home-made driver and a proportional-integral-derivative servo is used together with the fibre stretcher to remove the long-term drift of the fibre path, which can otherwise exceed the tuning range of the fibre stretcher (4.4 mm). For context, a coefficient of thermal expansion of  $\sim 10^{-5}^{\circ}\mathrm{C}^{-1}$  means that the length of a 600-m fibre will change by  $6\mathrm{mm}^{\circ}\mathrm{C}^{-1}$ .

A slow phase drift of the 1,389-nm light can be observed when the interferometer is locked to the 1,112-nm reference due to the difference in index of refraction between 1,389 nm and 1,112 nm inside the delay fibre. To actively compensate for this differential phase drift, we use another home-made servo with a sample-and-hold circuit involving the injection of a 1,389-nm reference light (Pound-Drever-Hall-locked to the same cavity as the 1,112-nm reference) and a free-space delay stage that shifts only the 1,389-nm path (Extended Data Fig. 6) with a piezo actuator (Thorlabs APF705) driven by a home-made low-noise piezo driver. To minimize loss on the single-photon path, three beam samplers with less than  $1\%$  reflection are used to combine the reference light into the path and sample the beat signals of the two detector paths. A balanced detector is used to maintain the locking point stability against power fluctuation of the reference light. The injection light power is about  $100~\mu \mathrm{W}$ , and less than  $10~\mathrm{nW}$  enters the home-made high-gain differential photodiode with  $100\mathrm{-Hz}$  bandwidth. The seemingly narrow bandwidth of the photodiode is acceptable because of an even slower closed-loop feedback bandwidth (1 Hz). The 1,389-nm reference light is blocked intermittently by shutters, and the servo is briefly paused when collecting single photons from atoms. Additionally, a fast piezo actuator (Thorlabs AE0505D08F) is stacked on the APF705, and is triggered in sequence to vary the measurement phase of the single photon without affecting the locking routine outside of the photon detection window.

Polarization stability is achieved by two radio-control servomotors that are attached to the paddles of the manual fibre polarization controller (Thorlabs FPC030). When the optical power from the PBS reflection rises above a threshold (around  $2\%$ ), the polarization servo is switched on to minimize the PBS reflection through lock-in detection. The status of the polarization and phase servo is recorded synchronously with the experiment, and is analysed to identify and discard experimental shots when the servo misbehaves due to environmental interference, such as temperature fluctuation or mechanical noise. Incidentally, these records also tell us if or when either of our 1,112-nm or 1,389-nm lasers are unlocked or unstable.

With all the locking routines enabled, we send classical 1,389-nm pulses with 400-ns pulse widths through the single-photon collection fibre into the interferometer to measure its visibility. A ramping voltage is applied on the fast piezo actuator to obtain an oscillating fringe that we measure with two classical PDs in place of the SNSPDs after the 50:50 BS. Extended Data Fig. 7 shows the normalized intensity measured with the two PDs, from which we extract an averaged visibility of  $96.7(2)\%$ .

# Atom-photon Bell state fidelity characterization

We characterize the fidelity of the final atom-photon Bell state comparing with a maximally entangled Bell state. The state fidelity is characterized by the joint measurement of the atomic state and the photon arrival time and TDI output port, in both ZZ and XX bases.

Given the atom-photon state density matrix  $\rho$ , the Bell state fidelity is defined as

$$
\mathcal {F} = \frac {1}{2} \left(\rho_ {\uparrow E, \uparrow E} + \rho_ {\downarrow L, \downarrow L} + 2 | \rho_ {\uparrow E, \downarrow L} |\right). \tag {1}
$$

The first two terms,  $\rho_{\uparrow E,\uparrow E}$  and  $\rho_{\downarrow L,\downarrow L}$ , are from measuring the atom-photon state in the ZZ basis, given by the probability of the photon arriving in the early (late) bin and the atom readout giving a  $\uparrow (\downarrow)$  state. As the ZZ correlation between the atom and photon states is classical, one can bypass the interferometer and directly use an SNSPD to measure the arrival time of collected photons. We use this method for ZZ-basis measurement to remove photon loss from the interferometer, which, in turn, improves the rate at which data can be taken.

The last term,  $|\rho_{\uparrow E,\downarrow L}|$ , is obtained by measuring in the XX basis and can be extracted by applying  $\pi/2$ -rotations on both photon and atom qubits before performing the ZZ-basis measurements. The measurement result (parity fringe) can be simplified to

$$
P = 2 \Re \left(\mathrm {e} ^ {\mathrm {i} \left(\phi_ {\mathrm {a}} + \phi_ {\mathrm {p}}\right)} \rho_ {\uparrow E, \downarrow L} + \mathrm {e} ^ {\mathrm {i} \left(\phi_ {\mathrm {a}} - \phi_ {\mathrm {p}}\right)} \rho_ {\uparrow L, \downarrow E}\right), \tag {2}
$$

where  $\phi_{\mathrm{a}}$  and  $\phi_{\mathrm{p}}$  are the phases of the  $\pi /2$ -rotations on the atom and photon qubits, respectively. To extract  $|\rho_{\uparrow E,\downarrow L}|$ , the 'parity scan' method is often implemented by varying  $\phi_{\mathrm{a}}$  and  $\phi_{\mathrm{p}}$  together, that is,  $\phi_{\mathrm{a,p}}\rightarrow \phi_{\mathrm{a,p}} + \Delta \phi$ . Scanning  $\Delta \phi$  from 0 to  $\pi$  gives a sinusoidal oscillation of  $P$ , the amplitude of which is equal to  $|\rho_{\uparrow E,\downarrow L}|$ . Parity scans are commonly used when characterizing two-qubit gate fidelities when the phases of the two  $\pi /2$ -rotations can be precisely controlled.

We control  $\phi_{\mathrm{a}}$  by varying the time delay between the final telecom excitation  $\pi$ -pulse and the Raman  $\pi/2$ -pulse for the parity scan. Since we use a light shift to eliminate the qubit splitting during the metastable state Raman transitions, the time delay introduces a  $\sigma_{Z}$  rotation at the qubit splitting frequency (Larmor precession).  $\phi_{\mathrm{p}}$  can be controlled by changing the phase offset between the two arms of the interferometer. In our case, for experimental simplicity, we instead fix  $\phi_{\mathrm{p}}$  and only scan  $\phi_{\mathrm{a}}$  from 0 to  $2\pi$ . Without loss of generality, we take  $\phi_{\mathrm{p}} = 0$ , and up to a global phase offset, take  $\rho_{\uparrow E,\downarrow L} \rightarrow |\rho_{\uparrow E,\downarrow L}|$  along with  $\rho_{\uparrow L,\downarrow E} \rightarrow |\rho_{\uparrow L,\downarrow E}|e^{i\theta}$ . Then, equation (2) becomes

$$
P _ {0} = 2 \cos \phi_ {\mathrm {a}} | \rho_ {\uparrow E, \downarrow L} | + 2 \cos \left(\phi_ {\mathrm {a}} - \theta\right) | \rho_ {\uparrow L, \downarrow E} |. \tag {3}
$$

Depending on the phase offset  $\theta$ , the amplitude  $A$  of the measured parity fringe curve is bounded by

$$
2 \left| \rho_ {\uparrow E, \downarrow L} \right| - 2 \left| \rho_ {\uparrow L, \downarrow E} \right| \leq A \leq 2 \left| \rho_ {\uparrow E, \downarrow L} \right| + 2 \left| \rho_ {\uparrow L, \downarrow E} \right|. \tag {4}
$$

Finally, noticing that  $|\rho_{\uparrow L,\downarrow E}|\leq \sqrt{\rho_{\uparrow L,\uparrow L}\cdot\rho_{\downarrow E,\downarrow E}}$  , we can upper- and lower-bound  $|\rho_{\uparrow L,\downarrow E}|$  using the ZZ-basis measurement results.

$$
\frac {A}{2} - \sqrt {\rho_ {\uparrow L , \uparrow L} \cdot \rho_ {\downarrow E , \downarrow E}} \leq | \rho_ {\uparrow L, \downarrow E} | \leq \frac {A}{2} + \sqrt {\rho_ {\uparrow L , \uparrow L} \cdot \rho_ {\downarrow E , \downarrow E}} \tag {5}
$$

Substituting equation (5) into equation (2), we can bound the atom-photon Bell state fidelity. As our ZZ measurement gives values of  $\rho_{\uparrow L,\uparrow L}$  and  $\rho_{\downarrow E,\downarrow E}$  close to zero, the upper and lower bounds are reasonably tight—comparable with our statistical uncertainties. We quote our fidelity upper and lower bounds using the format  $\frac{1}{2} (\rho_{\uparrow E,\uparrow E} + \rho_{\downarrow L,\downarrow L} + A) \pm \sqrt{\rho_{\uparrow L,\uparrow L} \cdot \rho_{\downarrow E,\downarrow E}}$  bound with additional statistical uncertainties.

# Fidelity estimation of entanglement generation and tomography

Spontaneous emission and off-resonant telecom excitation. The atom–photon entanglement fidelity is ultimately limited by spontaneous emission during the telecom  $\pi$ -pulse and the residual off-resonant excitation from the  $|\downarrow\rangle$  state to the  $|^3\mathrm{D}_1, F = 3/2, m_F = 1/2\rangle$  state. To suppress spontaneous emission, we note that when the telecom Rabi frequency is comparable with or larger than the transition linewidth, the contribution to infidelity from spontaneous emission during a telecom  $\pi$ -pulse is inversely proportional to the telecom Rabi frequency. This indicates that a larger Rabi frequency with a shorter pulse can reduce the spontaneous emission during a  $\pi$ -pulse.

We want the off-resonant excitation from  $|\downarrow \rangle$  to  $|^3\mathrm{D}_1$ ,  $F = 3 / 2$ ,  $m_{F} = 1 / 2\rangle$  state to be minimized at the  $\pi$ -time of the stretched  $|\uparrow \rangle \leftrightarrow |^3\mathrm{D}_1$ ,  $F = 3 / 2$ ,  $m_{F} = 3 / 2\rangle$  transition, that is, the off-resonant transition should evolve through an integer multiple of  $2\pi$ . This requires the magnetic field  $B$  and Rabi frequency  $\Omega$  on the stretched transition to satisfy

$$
\sqrt {\left(\Omega / \sqrt {3}\right) ^ {2} + \left(g \mu_ {\mathrm {B}} B\right) ^ {2}} \cdot \frac {\pi}{\Omega} = 2 m \pi , m = 1, 2 \dots \tag {6}
$$

Here  $\sqrt{3}$  comes from a Clebsch-Gordan coefficient,  $g = 1/3$  is the Landé  $g$ -factor for the  ${}^{3}\mathrm{D}_{1}$  manifold and  $\mu_{\mathrm{B}}$  is the Bohr magneton. We further assume post-selection on receiving  $\geq 1$  REG photons in the collection window, in agreement with our experiment in practice. Extended Data Fig. 8 shows the simulated minimum entanglement infidelity and relative yield after post-selection under different settings of  $\Omega$  and  $B$ . The multiple regions surrounding the local minima in the fidelity plot correspond to the settings for which the residual off-resonant transition is mitigated, and within one local minimum region, the infidelity decreases as  $\Omega$  and  $B$  increase. We choose to operate at  $\Omega / 2\pi = 30\mathrm{MHz}$  and  $B = 120\mathrm{G}$ , giving a maximum REG fidelity of  $99.7\%$  with post-selection. The remaining infidelity after post-selection is from double excitation within and after the REG attempt loop.

Effects from atom motion between time bins. One specific challenge for time-bin entanglement with atomic qubits, compared with solid-state spin qubits, is the recoil on motional states from photon absorption and emission. Let  $\Delta \vec{k}$  be the change in atom momentum after REG photon absorption and emission (here we set  $\hbar = 1$ ),  $\hat{H}_m = \omega a^\dagger a$  be the Hamiltonian of the harmonic trap potential and  $|\psi_{\mathrm{m}}\rangle$  be the initial motional state of the atom (when the motional state is a mixed state, its evolution can be expressed as the weighted average of the evolution of multiple pure states). Assuming that the early and late bins are separated by time  $\Delta t$  (including photon collection time  $t_{\mathrm{d}}$  and Raman  $\pi$ -time  $\tau_{\pi}^{m}$ ), the atom-photon motion state after the REG sequence is

$$
\frac {1}{\sqrt {2}} \left(| \uparrow , E \rangle e ^ {- i \hat {H} _ {\mathrm {m}} \Delta t} e ^ {i \vec {\Delta k} \cdot \vec {x}} | \psi_ {\mathrm {m}} \rangle + | \downarrow , L \rangle e ^ {i \vec {\Delta k} \cdot \vec {x}} e ^ {- i \hat {H} _ {\mathrm {m}} \Delta t} | \psi_ {\mathrm {m}} \rangle\right). \tag {7}
$$

When  $\mathrm{e}^{\mathrm{i}\vec{\Delta} t\cdot \hat{x}}$  and  $\mathrm{e}^{-\mathrm{i}\hat{H}_{m}\Delta t}$  do not commute, the motional states of the atom can be entangled with the photon qubits and reduce the atom-photon entanglement fidelity (Extended Data Fig. 5a). For fixed  $\Delta t$  and  $\omega$ , a higher temperature leads to increased dephasing in the atom-photon entangled state. The analytical expression of the infidelity is provided in ref. 48.

One way to eliminate this effect is to set  $\Delta t$  to be an integer multiple of the trap period, as used in ref. 48. For tweezers, however, the trap period is much longer than the typical REG sequence length, and inhomogeneity across the array leads to decoherence over the array as the system size increases. Instead, we work in the regime in which  $\Delta t$  is much smaller than the trap period, 'freezing' the atom movement between the early and late time bins. In this regime, the difference between axial and radial motion is negligible at finite temperature. Extended Data Fig. 5b shows the simulated atom-photon Bell state

fidelity as a function of  $\Delta t$  for various axial and radial temperatures. We choose to operate at  $\omega_{\mathrm{radial}} / 2\pi = 32\mathrm{kHz}$ ,  $\omega_{\mathrm{axial}} / 2\pi = 3\mathrm{kHz}$  and  $\Delta t = 2.8~\mu \mathrm{s}$ . Given our expected atom temperature of  $T\approx 2.33~\mu \mathrm{K}$  during our attempt loop, we anticipate the upper limit of our atom-photon Bell state fidelity to be  $\sim 99.1\%$ .

# Bell state fidelity error budget

In Extended Data Table 1, we summarize the major sources of error contributing to the measured Bell state infidelity. The largest source of error is SNSPD dark counts considering the SNSPD dark count rate and our collection efficiency (see the 'Estimation of photon collection rate and signal-to-noise ratio' section), leading to an error contribution of  $2.1(5)\%$ . Imperfect interferometer visibility is expected to reduce fidelity by  $1.6(1)\%$  (see the 'TDI' section). We expect a  $0.9\%$  error to be contributed by the atomic motion between the two time bins at our expected average temperature (see the 'Effects from atom motion between time bins' section). Spontaneous emission during the Raman  $\pi$ -pulse causes a spin-flip error of  $0.35\%$  (see the 'Timing and hardware: attempt loop' section). Double excitation during  $1,389\mathrm{-nm}$  photon generation is expected to contribute  $0.3\%$  (see the 'Spontaneous emission and off-resonant telecom excitation' section).

This total error should be compared with the infidelity of our atom-measurement-corrected Bell state fidelity, that is,  $1 - (0.950(9) \pm 0.005(3)_{\mathrm{bound}}) \approx 0.05$ . We see that the two values are in good agreement.

# Expected performance with an optical cavity

Here we suppose a hypothetical optical cavity to enhance photon collection and estimate the corresponding improvement to the average Bell state generation rate following the methods developed in refs. 29,79.

Cavity-enhanced collection efficiency and branching ratio. Coupling an atomic transition to an optical cavity can improve the overall photon collection efficiency by causing the atom to preferentially emit photons not only into the cavity mode but also along the specific decay pathways resonant with that mode as well[79].

The collection efficiency  $\eta$  of a two-level atom in a resonant cavity is given by

$$
\eta = \left(\frac {C}{C + 1}\right) \left(\frac {\kappa}{\kappa + \Gamma}\right) \left(\frac {T}{T + L}\right),
$$

where  $T$  is the transmission of the output mirror of a one-sided cavity,  $\kappa$  is the photonic mode decay rate of the cavity,  $L$  the total cavity loss and

$$
C = \frac {4 g ^ {2}}{\kappa \Gamma} = \frac {6}{\pi^ {3}} \frac {\lambda^ {2}}{w ^ {2}} F (T, L)
$$

is the single-atom cooperativity with finesse  $F(T, L)$ .

One can optimize the collection  $\eta$  over mirror properties  $(T,L)$ . In our case of interest, considering the telecom transition  $\lambda = 1,389\mathrm{nm}$  with  $\Gamma^{3\mathrm{D}_1} = 1 / \tau^{3\mathrm{D}_1}$ , and a near-concentric Fabry-Pérot cavity with curvature  $R_{\mathrm{c}} = 8\mathrm{mm}$ ,  $g_{\mathrm{cav}} = 1 - L_{\mathrm{cav}} / R_{\mathrm{c}} = -0.9$  (yielding a Gaussian mode waist  $w_0\approx 27.8~{\mu\mathrm{m}}$ ),  $T_{\mathrm{in}} = 20~\mathrm{ppm}$  and assumed loss of  $L = 100~\mathrm{ppm}$ , we find that  $\eta \approx 0.51$  can be achieved for  $T\approx 1,070~\mathrm{ppm}$ , with a corresponding  $C\approx 2.6$ .

Although the above collection considers a single decay channel (as relevant for stretched transitions), for more realistic systems with multiple possible decay channels, the emission along the desired transition is correspondingly reduced. In our case, we have a branching ratio (in free space) of  $f = \{0.64:0.35:0.01\}$ , with relative probability  $f_0 = 0.64$  of emission into the desired path. However, by coupling the telecom transition to the cavity mode, we expect the modified branching rate to be  $f' = \left\{\frac{0.64(1 + C)}{(0.64(1 + C)) + 0.36}, \frac{0.35}{(0.64(1 + C)) + 0.36}, \frac{0.01}{(0.64(1 + C)) + 0.36}\right\}$ . Then, considering the above optimized  $T \approx 1,070 \, \mathrm{ppm}$ , we find  $f_0' \approx 0.86$ , and a corresponding modified collection efficiency of  $\eta' = f_0' \eta \approx 0.44$ .

Expected success probability and rate of remote atom-atom entanglement generation rate. With the cavity-enhanced collection efficiency, we can estimate the expected success probability of remote atom-atom entanglement between two identical experimental setups, given by

$$
P _ {\mathrm {a a}} = \frac {1}{2} \left(\eta^ {\prime} \eta_ {\mathrm {d e t}}\right) ^ {2},
$$

where  $\eta_{\mathrm{det}}$  characterizes the efficiency of the detection path. Given an SNSPD detection efficiency of around  $\eta_{\mathrm{det}} \approx 0.8$  and ignoring the fibre loss for short to intermediate networks at telecom wavelengths,  $P_{\mathrm{aa}} \approx 0.063$  can be reached.

To estimate the resulting remote atom-atom entanglement generation rate, note that the expected binomially distributed process of a successful Bell state measurement will give, on average,  $NP_{\mathrm{aa}}$  out of  $N$  attempts. Thus, in our case, we expect  $N^{*} = 1 / P_{\mathrm{aa}} \approx 17$  attempts per success.

For a single atom coupled to the cavity mode, the required experimental time to generate entanglement can be parameterized as  $T_{\mathrm{aa}} = N_{\mathrm{cycle}}(n_{\mathrm{a}}(T_{\mathrm{init}} + T_{\mathrm{REG}}) + T_{\mathrm{cool}})$ , where  $n_{\mathrm{a}}$  attempts of state initialization and REG (of duration  $(T_{\mathrm{init}} + T_{\mathrm{REG}})$ ) are made before a cooling cycle (of duration  $T_{\mathrm{cool}}$ ), with the requirement  $(N_{\mathrm{cycle}}n_{\mathrm{a}}) = N^{*}$  to successfully generate entanglement on average. As  $T_{\mathrm{cool}} \gg T_{\mathrm{init,REG}}$  for typical systems, even with an optimized cooling time of  $T_{\mathrm{cool}} \approx 0.1$  ms, this sets a ceiling for the entanglement generation rate at  $T_{\mathrm{aa}}^{-1} \lesssim 10^{3} - 10^{4}$  s $^{-1}$ .

However, by combining an array of atoms with local control and leveraging the high collection efficiency afforded by the cavity, it becomes possible to exceed  $T_{\mathrm{aa}}^{-1} \gtrsim 10^{4} \, \mathrm{s}^{-1}$ . In such a case, the large initial time cost (to cool and/or move an array of atoms in parallel) can be compensated by the sufficiently large number of atoms made available to (sequentially) undergo REG attempts. To estimate the average Bell pair generation rate, we adopt the method developed in ref. 29 that envisions an array of a few hundred atoms coupled to the cavity, with strong local light control to far-detune all but a single atom undergoing the REG attempt. Then, the average Bell pair generation rate after  $m$  rounds of array-entangling attempts is given by

$$
R _ {\mathrm {b p}} = \frac {\sum_ {i = 1} ^ {m} N _ {i} P _ {\mathrm {a a}}}{T _ {\mathrm {m o v e}} + m \left(T _ {\mathrm {i n i t}} + T _ {\mathrm {d e p u m p}}\right) + T _ {\mathrm {R E G}} \sum_ {i = 1} ^ {m} N _ {i}},
$$

where  $N_{i} = N_{i - 1}(1 - P_{\mathrm{aa}})$  with  $N_{1} = N_{\mathrm{a}}$

The scheme in ref. 29 utilizes a cooling/moving time of  $T_{\mathrm{move}} \approx 100 \mu \mathrm{s}$  and a reset time (to depump  $^3\mathrm{P}_0$  to  $^1\mathrm{S}_0$  and optically pump in  $^1\mathrm{S}_0$ ) of  $T_{\mathrm{depump}} \approx 6.1 \mu \mathrm{s}$ , as well as an array size of  $N_{\mathrm{a}} = 204$  (chosen to exceed  $- (T_{\mathrm{move}} + T_{\mathrm{init}}) / T_{\mathrm{REG}} \approx 100$  to offset the large initial time cost and maximally filling the cavity mode volume to achieve interaction strength  $g \gtrsim 0.9g_{\mathrm{max}}$ ). Thus, combining the numbers used in this work for atom-photon entanglement, we get

$$
T _ {\text {i n i t}} \quad = t _ {\pi} ^ {\text {c l o c k}} + t _ {\pi / 2} ^ {\text {R a m a n}} \approx 5. 3 \mu \mathrm {s},
$$

$$
T _ {\text {R E G}} = 2 \left(t _ {\pi} ^ {\text {R E G}} + t _ {\text {w a i t}}\right) + t _ {\pi} ^ {\text {R a m a n}} \approx 1. 7 5 2 \mu \mathrm {s},
$$

where we have set  $t_{\mathrm{wait}} = 6.454 / \kappa \approx 0.55 \, \mu \mathrm{s}$  to collect  $\gtrsim 0.99$  of the leaked cavity mode, we find a rate of  $2.6 \times 10^{4} \, \mathrm{s}^{-1}$  after the  $m = 1$  round, reaching a maximum of  $-3.1 \times 10^{4} \, \mathrm{s}^{-1}$  after 5 rounds.

# Data availability

The data that support the findings of this study are available from the corresponding authors upon request.

# Code availability

The analysis codes related to this study are available from the corresponding authors upon request.

# References

75. Cho, J. W. et al. Optical repumping of triplet-P states enhances magneto-optical trapping of ytterbium atoms. Phys. Rev. A 85, 035401 (2012).  
76. Parsev, S. G., Rakhlina, Y. G. & Kozlov, M. G. Electric-dipole amplitudes, lifetimes, and polarizabilities of the low-lying levels of atomic ytterbium. Phys. Rev. A 60, 2781-2785 (1999).  
77. Scazza, F. Probing SU(N)-Symmetric Orbital Interactions with Ytterbium Fermi Gases in Optical Lattices. PhD thesis, LMU Munich (2015)  
78. Bettermann, O. Interorbital Interactions in Ytterbium-171. PhD thesis, LMU Munich (2022).  
79. Young, C. B. et al. An architecture for quantum networking of neutral atom processors. Appl. Phys. B 128, 151 (2022).

# Acknowledgements

We acknowledge H. Bernien, J. Thompson, M. Saffman, E. Goldschmidt and B. DeMarco for stimulating discussions. We thank H. Bernien and A. Kaufman for critical reading of the manuscript. We also thank C. Anderson for generously sharing his SNSPD system. We acknowledge funding from the NSF QLCI for Hybrid Quantum Architectures and Networks (NSF award number 2016136); the NSF PHY Division (NSF award numbers 2112663 and 2339487); the NSF Quantum Interconnects Challenge for Transformational Advances in Quantum Systems (NSF award number 2137642); the ONR Young Investigator Program (ONR award number N00014-22-1-2311); the AFOSR Young Investigator Program (AFOSR award number FA9550-23-1-0059); and the US Department of Energy, Office of Science, National Quantum Information Science Research Centers.

# Author contributions

L.L., X.H., Z.J. and J.P.C. envisioned this experiment. L.L., X.H. and Z.J. led this experiment and analysed the results. All authors contributed to the experimental techniques, the interpretation and analysis of data, and the vision for the parallelized networking architecture. W.H. performed the state preparation and measurement error correction analysis. W.K.C.S., A., Y.D. and N.H.-O.-T. performed the analysis of the optical cavity and contributed to those discussions in the paper. J.P.C. supervised this work, wrote the main text and directed the writing of the Supplementary Information.

# Competing interests

The authors declare no competing interests.

# Additional information

Extended data is available for this paper at https://doi.org/10.1038/s41567-025-03022-4.

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41567-025-03022-4.

Correspondence and requests for materials should be addressed to Lintao Li or Jacob P. Covey.

Peer review information Nature Physics thanks Sebastian Eppelt and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permissions information is available at www.nature.com/reprints.

Extended Data Table 1 | Error budget for entanglement generation and measurement  

<table><tr><td></td><td>Fidelity</td></tr><tr><td>Source of error (see Methods)</td><td>Error</td></tr><tr><td>SNSPD dark counts (Section &quot;Estimation of photon collection rate and signal-to-noise ratio&quot;)</td><td>0.021(5)</td></tr><tr><td>Interferometer visibility (Section &quot;TDI&quot;)</td><td>0.016(1)</td></tr><tr><td>Atom motion between time bins (Section &quot;Effects from atom motion between time bins&quot;)</td><td>0.009</td></tr><tr><td>Spin-flip during Raman (Section &quot;Timing and hardware: attempt loop&quot;)</td><td>0.0035</td></tr><tr><td>REG double-excitation (Section &quot;Spontaneous emission and off-resonant telecom excitation&quot;)</td><td>0.003</td></tr><tr><td>TOTAL</td><td>0.053(5)</td></tr></table>

![](images/d6aa08754fcef7119d6ef602595308cc3e21c60580813b5b6b546b949308a6f6.jpg)  
Extended Data Fig. 1 | Layout of the experiment. The experiment is performed in a glass cell and the magnetic field is oriented vertically. Two microscope objectives are arranged horizontally. The first objective sends in the 760-nm optical tweezer array and collects the emitted telecom photons, and the second objective images the tweezer array for diagnostic purposes and performs fluorescence detection of the atoms. Optical pumping via  ${}^{3}\mathrm{P}_{1}$  is performed  
with a horizontal beam (green) that has horizontal linear polarization $^{37}$ . Raman rotations of the metastable nuclear spin qubit are performed with a horizontal beam (blue) that has near-circular polarization. The clock beam (orange) and telecom beam (red) both propagate along the B-field axis with circular polarization. They propagate in opposite directions.

![](images/4abfd524bc31c0bff24ce22b36ea6f28cbeafa9c875bfb33e1b19c0c90b1cc91.jpg)  
Extended Data Fig. 2 | Measured photon arrival possibility, atom survival simulation, and atomic temperature versus number of attempts. The blue histogram shows the summarized photon arrival versus attempt index of all the X-basis measurements. The orange curve shows the Monte Carlo simulation of the atom survival versus attempt index under same condition, showing good

agreement between the exponential decay rates of the photon arrival probability and the expected atom survival. The green data shows atomic temperature after a number of entanglement attempts measured through release-recapture, solid line shows an exponential fit.

![](images/e9e1a93a5d6c8dd78c9e341c6f850603de7c37547195a5c8cce8a7d5e5e36fcc.jpg)

![](images/073d981d3a2aba2377c3652a38f3c9f320b8a012759f7bf8cf7b18b1eb1024bc.jpg)

![](images/9c61fe06a59810d8cb7fe9c220fdc7ae6e25c16c8e302585d5df0aaee8ad34f4.jpg)

![](images/234b1beb1f7fd2410117f3e8b2b3acb01c655e16c0ecc47b68cd35c2fbd77513.jpg)  
Extended Data Fig. 3 | Experiment sequence for the attempt loop. attempt_loop.pdf (a) Sub-dopper cooling. (b) State initialization to  $|g_{-}\rangle$ . (c) Atomic X(Z)-basis measurement with (without) a Raman  $\pi/2$  pulse before atomic state readout. (d) Atom-photon entanglement generation, a clock pulse transfer the atom from  $|g_{-}\rangle$  to  $|\uparrow\rangle$  at the start.

![](images/4a486746ddce4dadb698213a349a5129b24749ddb2f09d78f84d68f13de3a548.jpg)

![](images/7268daa8117a052820deafe66f95fbf727bb1c7031969476d5c741d5f0e9eee0.jpg)  
(a)

![](images/ab94da5f1d0a4aa119a169114233d199df4f9a2955880a671daf9fe15479cad8.jpg)  
Extended Data Fig. 4 | Magic conditions for metastable Raman transition. (a) Simulated Raman  $\pi$  pulse fidelity under different single-photon Rabi frequencies and phase offsets between horizontal and vertical components. Here we set  $B = 120\mathrm{G},\Delta (3 / 2) = +612\mathrm{MHz}$ . Within the contour we expect the  $\pi$ -pulse fidelity to exceed  $99.9\%$ . (b) The corresponding two-photon Raman Rabi frequency.  
(b)

![](images/98498d1f46c3986eb9c2a72edd5d5623fe371185d85ecd046f8db0e212e39da6.jpg)

![](images/1679267c2d4f0b783198f2a6635d88f8aafa80f30debf0d1ad3909e747edd482.jpg)  
Extended Data Fig. 5 | Atom-photon entanglement fidelity degradation from residual atom-motion entanglement. (a) Illustration of the motion state evolution during REG sequence. The non-commutativity between  $e^{i\Delta k \cdot x}$  and  $e^{-iH_m\Delta t}$  leads to non-overlapping motion wavefunctions associated to the early (blue) and late (red) time bin. (b) Fidelity degradation from radial and axial atom-motion entanglement as a function of time-bin separation. As our  $\Delta k$  has  
components along both radial and axial directions, we calculate effects on the overall atom-photon Bell state fidelity from both axial and radial thermal states for different temperatures. The grey dashed line indicates  $\Delta t = 2.8\mu s$  which we use in our experimental sequence. We expect a  $\approx 0.9\%$  fidelity reduction from both radial and axial motion combined.

![](images/afa59ed45702559c9588de1a949069bfd0bf65360fc114459f83c59c3963c670.jpg)  
Extended Data Fig. 6 | Time-delay interferometer (TDI). An amplitude-modulating EOM directs single photons into either the free-space or the fiber-delay arm of the interferometer. The relative phase of the interferometer  
is locked continuously to a 1112-nm reference, and intermittently to a 1389-nm reference (see text for detail). A motor-driven fiber paddle maintains polarization stability in the fiber.

![](images/a8e69482f049210d15b8f8aa9ab022ac6d72b3a65cb6ec7c4e3ad38c05fe9f52.jpg)  
Extended Data Fig. 7|TDI visibility. Pulse modulated 1389-nm CW light were sent through the same single-photon collection fiber into the short/long arm of the interferometer. A ramping voltage applied to the fast piezo actuator results  
in two interference fringes after the 50:50 BS, and are measured by two regular PDs in place of the SNSPDs, shown in red/blue. From the two fringes we extract an averaged visibility of  $96.7(2)\%$ .

![](images/ea66b590fc724c8d8ac93977eb783cf43a5312c28199b2a004bbfe10bdf4c329.jpg)  
Extended Data Fig. 8 | Atom-photon entanglement infidelity and relative yield under different telecom Rabi frequencies and magnetic fields after postselecting on receiving  $\geq 11389$ -nm photons. We find that using higher Rabi frequency and operating under higher B-field strength result in better atom-

![](images/fc087cc0c4e01344218f707efc747316d32f4b74459610f6c788c0f1e8b53ad3.jpg)  
photon entanglement fidelities. Under a fixed  $B$ -field strength, there exist several local minima of atom-photon entanglement infidelity where the off-resonant transition from  $|\uparrow \rangle$  goes through multiples of  $2\pi$ . The star indicates the settings used our experiment.