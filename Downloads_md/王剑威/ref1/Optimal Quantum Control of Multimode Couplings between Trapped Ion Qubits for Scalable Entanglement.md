# Optimal Quantum Control of Multimode Couplings between Trapped Ion Qubits for Scalable Entanglement

T. Choi, $^{1,*}$  S. Debnath, $^{1}$  T. A. Manning, $^{1}$  C. Figgatt, $^{1}$  Z.-X. Gong, $^{1,2}$  L.-M. Duan, $^{2}$  and C. Monroe $^{1}$ $^{1}$ Joint Quantum Institute, University of Maryland Department of Physics and National Institute of Standards and Technology, College Park, Maryland 20742, USA  
 $^{2}$ Department of Physics, University of Michigan, Ann Arbor, Michigan 48109, USA (Received 7 January 2014; published 14 May 2014)

We demonstrate entangling quantum gates within a chain of five trapped ion qubits by optimally shaping optical fields that couple to multiple collective modes of motion. We individually address qubits with segmented optical pulses to construct multipartite entangled states in a programmable way. This approach enables high-fidelity gates that can be scaled to larger qubit registers for quantum computation and simulation.

DOI: 10.1103/PhysRevLett.112.190502

PACS numbers: 03.67.-a, 37.10.Ty

Trapped atomic ion crystals are the leading architecture for quantum information processing, with their unsurpassed level of qubit coherence and near perfect initialization and detection efficiency [1,2]. Moreover, trapped ion qubits can be controllably entangled through their Coulomb-coupled motion by applying external fields that provide a qubit state-dependent force [3-6]. However, scaling to large numbers of ions  $N$  within a single crystal is complicated by the many collective modes of motion, which can cause gate errors from mode crosstalk. Such errors can be mitigated by coupling to a single motional mode, at a cost of significantly slowing the gate operation. The gate time  $\tau_{g}$  must generally be much longer than the inverse of the frequency splitting of the motional modes, which for axial motion in a linear chain implies  $\tau_{g} \gg 1/\omega_{z} > N^{0.86}/\omega_{x}$ , where  $\omega_{z}$  and  $\omega_{x}$  are the center-of-mass axial and transverse mode frequencies [7]. For gates using transverse motion in a linear chain [8], we find  $\tau_{g} \gg \omega_{x}/\omega_{z}^{2} > N^{1.72}/\omega_{x}$ . In either case, the slowdown with qubit number  $N$  can severely limit the practical size of trapped ion qubit crystals. Shuttling ions between separate trapping zones may mitigate this problem [9], but even in that architecture it will be useful to increase the number of qubits per zone.

In this letter, we address this scaling problem by applying qubit state-dependent optical forces that simultaneously couple to multiple modes of motion. We address subsets of ions immersed in a five-ion linear crystal and engineer laser pulse shapes to entangle pairs of ions. This suppression of mode crosstalk provides high gate fidelity without slowing the gate [8,10]. The precalculated pulse shapes optimize theoretical gate fidelity, achieving unity for sufficiently complex pulses. In the experiment, we concatenate these shaped gates to entangle multiple pairs of qubits and directly measure multiqubit entanglement in the crystal. Extensions of this approach can be scaled to larger ion chains and also incorporate higher levels of

pulse shaping to reduce sensitivity to particular experimental errors and drifts [11-13].

In the experiment, five  $^{171}\mathrm{Yb}^+$  ions are confined in a three-layer linear rf trap [14] with transverse center-of-mass (CM) frequency ranging from  $\omega_{x} / 2\pi = 2.5 - 4.5\mathrm{MHz}$  and axial CM frequency  $\omega_z / 2\pi = 310 - 550\mathrm{kHz}$ , with a minimal ion separation of  $\sim 5\mu \mathrm{m}$ . Each qubit is represented by the  $^2 S_{1 / 2}$  hyperfine "clock" states within  $^{171}\mathrm{Yb}^+$ , denoted by  $|0\rangle$  and  $|1\rangle$  and having a splitting of  $\omega_0 / 2\pi = 12.642821\mathrm{GHz}$  [15]. We initialize each qubit by optically pumping to state  $|0\rangle$  using laser light resonant with the  $^2 S_{1 / 2}\leftrightarrow^2 P_{1 / 2}$  transition near  $369.5\mathrm{nm}$ .

We then coherently manipulate the qubits with a mode-locked laser at  $355\mathrm{nm}$  whose frequency comb beat notes drive stimulated Raman transitions between the qubit states and produce qubit state-dependent forces [16,17]. The Raman laser is split into two beams, one illuminating the entire chain and the other focused to a waist of  $\sim 3.5\mu \mathrm{m}$  for addressing any subset of adjacent ion pairs in the chain, with a wave vector difference  $\Delta k$  aligned along the  $x$  direction of transverse motion. We finally measure the state of each qubit by applying resonant laser light near 369.5 nm that results in state-dependent fluorescence [15] that is imaged onto a multichannel photomultiplier tube for individual qubit state detection. We repeat each experiment at least 300 times and extract state populations by fitting to previously measured fluorescence histograms [18].

When a constant state-dependent force is applied to the ion qubits, the multiple incommensurate modes generally remain entangled with the qubits following the interaction, thereby degrading the quantum gate fidelity. However, more complex optical pulses can be created that satisfy a set of constraints for disentangling every mode of motion following the gate. This optimal control problem involves engineering a sufficiently complex laser pulse that can in principle achieve near-unit fidelity.

The qubit state-dependent optical force is applied by generating bichromatic beat notes near the upper and lower motional sideband frequencies at  $\omega_0 \pm \mu$ , where the detuning  $\mu$  is in the neighborhood of the motional mode frequencies. Using the rotating wave approximation in the Lamb-Dicke and resolved-sideband limits, the evolution operator of the dipole interaction Hamiltonian becomes [10,19-21]

$$
\hat {U} (\tau) = \exp \left[ \sum_ {i} \hat {\phi} _ {i} (\tau) \hat {\sigma} _ {x} ^ {(i)} + i \sum_ {i, j} \chi_ {i, j} (\tau) \hat {\sigma} _ {x} ^ {(i)} \hat {\sigma} _ {x} ^ {(j)} \right]. \tag {1}
$$

The first term corresponds to the qubit-motion coupling on ion  $i$ , where  $\hat{\phi}_i(\tau) = \sum_m[\alpha_{i,m}(\tau)\hat{a}_m^\dagger -\alpha_{i,m}^* (\tau)\hat{a}_m]$ ,  $\hat{a}_m^\dagger (\hat{a}_m)$  is the raising (lowering) operator of mode  $m$ , and  $\hat{\sigma}_x^{(i)}$  is the Pauli-  $X$  operator of the  $i$ th qubit, where we define the  $x$  axis of the qubit Bloch sphere according to the phase of the bichromatic beatnotes [22]. This is a state-dependent displacement of the ion  $i$  such that the  $|0\rangle \pm |1\rangle$  states follow the trajectories  $\pm \alpha_{i,m}(\tau)$  in phase space of the  $m$ th motional mode according to [10]

$$
\alpha_ {i, m} (\tau) = i \eta_ {i, m} \int_ {0} ^ {\tau} \Omega_ {i} (t) \sin (\mu t) e ^ {i \omega_ {m} t} d t. \tag {2}
$$

Here,  $\eta_{i,m} = b_{i,m}\cdot \Delta k\sqrt{\hbar / 2M\omega_m}$  is the Lamb-Dicke parameter,  $b_{i,m}$  is the normal mode transformation matrix for ion  $i$  and mode  $m$  [23],  $\omega_{m}$  is the frequency of the mth motional mode, and  $M$  is the mass of a single  $^{171}\mathrm{Yb^{+}}$  ion. The second term of Eq. (1) describes the entangling interaction between qubits  $i$  and  $j$ , with [10]

$$
\begin{array}{l} \chi_ {i, j} (\tau) = 2 \sum_ {m} \eta_ {i, m} \eta_ {j, m} \int_ {0} ^ {\tau} \int_ {0} ^ {t ^ {\prime}} \Omega_ {i} (t) \Omega_ {j} \left(t ^ {\prime}\right) \\ \times \sin (\mu t) \sin (\mu t ^ {\prime}) \sin [ \omega_ {m} (t ^ {\prime} - t) ] d t d t ^ {\prime}. \tag {3} \\ \end{array}
$$

In Eqs. (2)-(3), the time-dependent Rabi frequency  $\Omega_{i}(t)$  on the  $i$ th ion is used as a control parameter for optimization of the gate and is assumed to be real without loss of generality. (We could alternatively vary the detuning  $\mu$  [24] or the beatnote phase [25] over time for control.)

In order to perform an entangling  $XX$  gate on two ions  $a$  and  $b$  in a chain of  $N$  ions, we apply identical state-dependent forces to just these target ions and realize  $\hat{U} (\tau_g) = \exp [i\pi \hat{\sigma}_x^{(a)}\hat{\sigma}_x^{(b)} / 4]$ . This requires  $\chi_{a,b}(\tau_g) = \pi /4$  along with the  $2N$  conditions  $\alpha_{a,m}(\tau_g) = 0$  so that the phase space trajectories of all  $N$  motional modes return to their origin and disentangle the qubits from their motion [4-6]. These constraints can be satisfied by evenly partitioning the pulse shape  $\Omega_{a}(t) = \Omega_{b}(t)$  into  $2N + 1$  segments [8,10], reducing the problem to a system of linear equations with a guaranteed solution. The detuning and

gate duration become independent parameters so that in principle, the gate can be performed with near-unit fidelity at any detuning  $\mu \neq \omega_{m}$  on any two ions in a chain, given sufficient optical power.

Figure 1(a) shows theoretical and measured fidelity of the entangled state  $\hat{U} (\tau_g)|00\rangle = |00\rangle +i|11\rangle$  for both a simple constant pulse and a five-segment pulse on a two-ion chain, as a function of detuning  $\mu$  for a fixed gate time  $\tau_{g} = 104~\mu \mathrm{s}$ . For two ions, the five segments provide full control  $(2N + 1 = 5)$ , meaning that a pulse shape can be calculated at each detuning that should yield unit fidelity in theory. As seen in Fig. 1(a), a constant pulse can be optimized to achieve high fidelity, but only at detunings  $\mu$  whose frequency difference from the two modes is commensurate [20], which in this case has many solutions spaced by  $1 / \tau_{g}$ . The observed fidelity of the constant pulse follows theory, with uniformly lower fidelities consistent with known errors in the system. On the other hand, relatively high fidelities of the 5-segment pulse are observed over a wide range of detunings for the same gate time, with the details of a particular pulse sequence shown in Fig. 1(b)-(c). We measure the fidelity by first observing the populations of the  $|00\rangle$  and  $|11\rangle$  states, then extracting their coherence by repeating the experiment with an additional global  $\pi /2$  analysis rotation  $R(\pi /2,\phi)$  and measuring the contrast in qubit parity as the phase  $\phi$  is scanned [26].

![](images/a8ee93fc6d3d3df4c05909fb56047bb4e3623fd94778bfc1f25455ba5220e20f.jpg)

![](images/6084433886df41c3e9aefbe4c8547619461e6dad590d0ee734c04d163c97fc6a.jpg)  
FIG. 1 (color online). Improvement of entangled state creation using pulse shaping on  $N = 2$  trapped ion qubits. (a) Comparison of Bell state entanglement fidelity for a constant pulse (black) versus a five-segment pulse (red) over a range of detuning  $\mu$ , showing significant improvement with the segmented gate. (b) The segmented pulse pattern, parameterized by the Rabi frequency  $\Omega_{i}(t)$  with the particular detuning  $\mu$  near the 2nd ("tilt") motional mode [arrow in (a)] and measured state fidelity  $\geq 94(2)\%$ . (c) Phase space trajectories (arbitrary units) subject to pulse sequence in (b) for both CM and tilt modes of the two ions. The thickness of the curves from each segmented pulse is alternated to guide the trajectories. The five-segment pulse pattern brings the two trajectories back to their origins, simultaneously disentangling both modes of motion from the qubits.

![](images/5c84198702349216e13730cabde8cdedfe1fed83c073ca427d740fd9689dba78.jpg)

When the number of ions in a chain increases to  $N > 2$ , it becomes difficult to find detunings  $\mu$  of a constant pulse whose difference frequencies  $\mu - \omega_{m}$  from all modes are nearly commensurate, without significantly slowing the gate. Figure 2(a)-(b) compares the measured parity curves using a constant versus a nine-segment pulse for performing the XX gate on an ion pair 1 and 2 within a five ion chain, while maintaining the same gate time  $(\tau_{g} = 190~\mu s)$ . The measured state fidelity increases from  $82(3)\%$  for a constant pulse to  $95(2)\%$  for the segmented pulse, even though fewer than  $2N + 1 = 11$  control parameters are utilized. Much of this gain in fidelity from the segmented pulse appears to stem from its relative insensitivity to detuning fluctuations, as discussed below. Using a different nine-segment pulse solution, we also achieve a fidelity of  $95(2)\%$  for an ion pair 2 and 3 as seen in Fig. 2(c). In this overconstrained case, the calculation becomes an optimization problem, where more weight is given to the closing of more influential phase space trajectories [Fig. 2(d)]. Therefore, a judicious choice of detuning can often reduce

![](images/fc5de95b6289e52afb4e4ac441740bb84dca0df3c25edd99cd63d5ba53dc4c02.jpg)

![](images/ed1ae5a598642285d4363deed23cf4deb459d5094cf172faea6a167079843236.jpg)

![](images/e6b86527ed2194f4581c9aed08990fc756cacb378477f2f6d6c6cf9b11f02185.jpg)  
FIG. 2 (color online). Entanglement of qubit pairs within a chain of  $N = 5$  trapped ions. (a) Applied pulse pattern and measured parity oscillations for a constant pulse used to entangle ions 1 and 2. The gate time is  $\tau_g = 190~\mu \mathrm{s}$  and the detuning is set to  $\mu = \omega_{x} + 2\pi /\tau_{g}$ , which should exhibit the highest fidelity; we measure  $F = 82(3)\%$ . (b) Same as (a), but with a nine-segment pulse. The gate time is again  $\tau_g = 190~\mu \mathrm{s}$ , and the detuning is set close to the tilt mode; we measure  $F = 95(2)\%$ . (c) Different nine-segment pulse pattern used to entangle ions 2 and 3 with same gate time, and the detuning is set close to the 5th mode; we measure  $F = 95(2)\%$ . (d) Phase space trajectories (arbitrary units but all on same scale) for the pulse pattern applied to the ion pair 1 and 2 at the detuning used in (b).

![](images/7e829c41052eaae53728830f110f234389555aef73c01b93e283b8ffc9732b13.jpg)

![](images/4a5c97c683f1cd0c36465fad7e7209b5f1eec8cf703c1bb32f5832646403d194.jpg)

![](images/521c9d9034f2fa877f6302a5ad7c151ee736bec33369ecbb10ec2c666c7aac57.jpg)

![](images/9c7ed04da23c53d65f1a6999283f54b6d528c1c1da6474141b847fcdf5d0ec60.jpg)  
FIG. 3 (color online). (a) Theoretical entanglement gate fidelity for the first two ions as a function of total number of ions in a chain using a constant (black), a five-segment (blue), and a nine-segment (red) pulse. The gate time is fixed to  $\sim 90~\mu \mathrm{s}$  and the minimum (central) ion spacing is  $\sim 5~\mu \mathrm{m}$ . The advantages of the pulse segmentation are clearly seen for larger numbers of ions. (b) Theoretical entanglement gate fidelity for the first two ions as a function of detuning error  $\Delta \mu$  in a chain of 5 ions. The solid black (red) line corresponds to a constant (nine-segment) pulse on the two ions, where the pulse power is optimized at each value of the detuning offset. The dashed black (red) line corresponds to a constant (nine-segment) pulse optimized for  $\Delta \mu = 0$ . We see that the segmented pulse not only allows high-fidelity solutions at any detuning (solid line), but even when the detuning drifts, the segmented pulses mitigate this error (dashed line).

the number of parameters required to achieve near-unit gate fidelities [8,10].

Figure 3(a) shows the theoretical maximum gate fidelity using a constant, a five-segment, and a nine-segment pulse for entangling the first two ions as a function of the total number of ions in a chain. We use a fixed gate time  $\tau_{g} \sim 90~\mu \mathrm{s}$  and minimal (central) ion spacing  $\sim 5~\mu \mathrm{m}$ . The improvement of the segmented gates becomes significant as the number of ions grows, as there are more modes that must be considered [8,10].

A further advantage of using multisegment pulses is their relative insensitivity to fluctuations in detuning  $\mu$  and trap frequency  $\omega_{m}$ . For conventional constant pulses, such noise strongly affects the simple phase space trajectories, and the fidelity degrades quickly. Segmented pulses also show errors, but because of the complex phase space trajectories [Fig. 2(d)], these errors are higher order, admitting solutions that do not change rapidly with detuning. As seen in Fig. 3(b), a constant pulse is expected to degrade the fidelity by  $\sim 15\%$  for a  $1\mathrm{kHz}$  drift in detuning, which is consistent with the measured state fidelity of  $82(3)\%$ . However, the nine-segment pulse is expected to degrade the fidelity by only  $1\%$  for the same drift, which compares to the observed fidelity of  $95(2)\%$ . Other sources of the infidelity in the experiment are Rabi frequency fluctuations from intensity noise in the tightly focused Raman laser beam ( $\sim 3\%$ ), optical Raman laser beam spillover ( $\sim 1\%$ ), and optical crosstalk of the multichannel photomultiplier tube used for qubit detection ( $\sim 1\%$ ).

To demonstrate pulse-shaped gates on subsets of qubits in a linear crystal, we produce tripartite entangled states by concatenating two  $XX$  gates in a five ion chain [see Fig. 4(a)].

![](images/ed6b3f9f3a78985548864f0286abef4dd6b734ce48b8e77ce273425027d86209.jpg)

![](images/94c46054cbe303905e4c8678da8f07407f96524f3b544172f6af14c018ee9cc6.jpg)

![](images/62ba792851625a884e323a72b6de49dccf8593d2fc75e9d966caa719b627fc8b.jpg)

![](images/f0b1e9bdf71955712299c65a5fb7e9699accda5d7af606ed1938c8f2286cccfa.jpg)

![](images/d9f1d1066523337c80990751d28a2467e7a23bfdf1c852b444e5e40b2809f8be.jpg)

![](images/ef33f531206db038cc9fda539e52bd16772fcb3a0269d8eaf99358998e1e7321.jpg)

![](images/a6498dd9efa009e726ca627a96c97f201f93f8d7d5b4604af9c5bd27d380960e.jpg)

![](images/7c5d89c5f08690b0c28ea5920da18b9b9ffbbd67aef67580de722541490c75a8.jpg)  
FIG. 4 (color online). Programmable quantum operations to create tripartite entanglement. (a) Circuit for concatenated  $XX$  gates between ions 1&2 and 2&3 and  $\pi/2$  analysis rotations of ions 1&2 with phase  $\phi$ . (b) Measured population after  $XX$  gates on ions 1&2 and 2&3, where  $P_N$  denotes the probability of finding  $N$  ions in the  $|1\rangle$  state. (c) Parity oscillations of ions 1&2 with the phase  $\phi$  of the  $\pi/2$  analysis rotations, after postselecting the state of the third ion, with periods  $\pi$  (left) and  $2\pi$  (right) for the two states  $|0\rangle_3$  and  $|1\rangle_3$ , respectively [see Eq. (4)]. (d) Schematic for creating a GHZ "cat" state using two  $XX$  gates on ions 1&2 and 2&3 as before, with additional individual qubit rotations, followed by  $\pi/2$  analysis rotations of all three ions with phase  $\phi$ . (e) Three-ion parity oscillation with phase  $\phi$  of the  $\pi/2$  analysis rotations. The red solid line is fit to the data with period  $2\pi/3$ , while the blue dashed line is the expected signal assuming a perfect cat state with known systematic measurement errors.

We adiabatically shuttle the ions across the fixed laser beams in order to address nearest neighbor pairs of the three target ions and ideally create a GHZ-type state,

$$
\left| \right. 0 0 0 \left. \right\rangle\rightarrow \left| \right. 0 0 0 \left. \right\rangle + i \left| \right. 1 1 0 \left. \right\rangle + i \left| \right. 0 1 1 \left. \right\rangle - \left| \right. 1 0 1 \left. \right\rangle . \tag {4}
$$

The measured state populations are consistent with the above state, as shown in Fig. 4(b).

In order to measure the coherences of the three-qubit subsystem, we apply analysis rotations  $R(\pi /2,\phi)$  to any two of the three qubits, then measure their parity as before. As the phase  $\phi$  of the analysis rotations is scanned, the parity should oscillate with period  $\pi$  or  $2\pi$  when the third

ion is postselected to be in state  $|0\rangle$  or  $|1\rangle$ , respectively, as seen in Fig. 4(c) for one of the pairs. By measuring the contrasts of the two parity curves for each of the three possible pairs conditioned upon the measured value of the third, we obtain the six coherences of the final state. Combined with the state populations [Fig. 4(b)], we calculate a quantum state fidelity of  $79(4)\%$  with respect to Eq. (4). This level of fidelity is consistent with the compounded XX gate fidelities ( $\sim 95\%$  each) and the discrimination efficiency ( $\sim 93\%$ ) for postselection of the third qubit.

To prove genuine tripartite entanglement within the five ion chain, we use single qubit rotations to transform the state given by Eq. (4) into a GHZ "cat" state  $|000\rangle +i|111\rangle$  [27]. As shown in the circuit of Fig. 4(d), this is achieved by applying a  $Z$ -rotation operation  $R_{z}(-\pi /2) = R(-\pi /2,0)$ $R(\pi /2,\pi /2)R(\pi /2,0)$  to the middle ion only followed by  $R(\pi /2,0)$  rotations to all three ions. We finally measure the parity of all three qubits while scanning the phases of subsequent  $R(\pi /2,\phi)$  analysis pulses, and the oscillation with period  $2\pi /3$  with a contrast of over  $70\%$  [Fig. 4(e)] verifies genuine tripartite entanglement [26]. This is a conservative lower limit to the entanglement fidelity, given known errors and crosstalk in the rotations and the measurement process. The simulated blue dashed curve in the same figure depicts what we expect to measure given our known errors and assuming a perfect initial state.

We have shown how a single control parameter can be used to mitigate multimode couplings between a collection of qubits, but this approach can be expanded to include additional parameters, such as spectral, phase, or spatial addressing of each qubit [24,25,28]. This could allow for the efficient implementation of more complicated quantum circuits, such as Toffoli [29] and other gates involving more than two qubits, or global operations for quantum simulations of particular Hamiltonian models [30]. The optimal quantum control we demonstrate here could apply to any quantum information and simulation architectures that entangle subsets of qubits through a bosonic quantum bus having multimode components, such as cavity QED [31] and superconducting circuits [32].

This work is supported by the U.S. Army Research Office (ARO) Award No. W911NF0710576 with funds from the DARPA Optical Lattice Emulator Program, ARO Award No. W911NF0410234 with funds from the IARPA MQCO Program, ARO MURI Award No. W911NF0910406, and the NSF Physics Frontier Center at JQI.

$^{*}$ tchoi12@umd.edu

[1] R. Blatt and D. Wineland, Nature (London) 453, 1008 (2008).  
[2] C. Monroe and J. Kim, Science 339, 1164 (2013).  
[3] J. I. Cirac and P. Zoller, Phys. Rev. Lett. 74, 4091 (1995).

[4] K. Molmer and A. Sorensen, Phys. Rev. Lett. 82, 1835 (1999).  
[5] E. Solano, R. L. de Matos Filho, and N. Zagury, Phys. Rev. A 59, R2539 (1999).  
[6] G.J. Milburn, S. Schneider, and D.F.V. James, Fortschr. Phys. 48, 801 (2000).  
[7] J.P. Schiffer, Phys. Rev. Lett. 70, 818 (1993).  
[8] S.-L. Zhu, C. Monroe, and L.-M. Duan, Phys. Rev. Lett. 97, 050505 (2006).  
[9] D. Kielpinski, C. Monroe, and D.J. Wineland, Nature (London) 417, 709 (2002).  
[10] S.-L. Zhu, C. Monroe, and L.-M. Duan, Europhys. Lett. 73, 485 (2006).  
[11] G. Kirchmair, J. Benhelm, F. Zähringer, R. Gerritsma, C. F. Roos, and R. Blatt, New J. Phys. 11, 023002 (2009).  
[12] D. Hayes, S. M. Clark, S. Debnath, D. Hucul, I. V. Inlek, K. W. Lee, Q. Quraishi, and C. Monroe, Phys. Rev. Lett. 109, 020503 (2012).  
[13] Y. Tomita, J. T. Merrill, and K. R. Brown, New J. Phys. 12, 015002 (2010).  
[14] W. K. Hensinger, S. Olmschenk, D. Stick, D. Hucul, M. Yeo, M. Acton, L. Deslauriers, C. Monroe, and J. Rabchuk, Appl. Phys. Lett. 88, 034101 (2006).  
[15] S. Olmschenk, K.C. Younge, D.L. Moehring, D.N. Matsukevich, P. Maunz, and C. Monroe, Phys. Rev. A 76, 052314 (2007).  
[16] D. Hayes, D. N. Matsukevich, P. Maunz, D. Hucul, Q. Quraishi, S. Olmschenk, W. Campbell, J. Mizrahi, C. Senko, and C. Monroe, Phys. Rev. Lett. 104, 140501 (2010).

[17] W.C. Campbell, J. Mizrahi, Q. Quraishi, C. Senko, D. Hayes, D. Hucul, D.N. Matsukevich, P. Maunz, and C. Monroe, Phys. Rev. Lett. 105, 090502 (2010).  
[18] M. Acton, K.-A. Brickman, P.C. Haljan, P.J. Lee, L. Deslauriers, and C. Monroe, Quantum Inf. Comput. 6, 465 (2006).  
[19] S.-L. Zhu and Z.D. Wang, Phys. Rev. Lett. 91, 187902 (2003).  
[20] K. Kim M.-S. Chang, R. Islam, S. Korenblit, L.-M. Duan, and C. Monroe, Phys. Rev. Lett. 103, 120502 (2009).  
[21] A.M. Steane, G. Imreh, J.P. Home, and D. Leibfried, arXiv:1312.5645.  
[22] P.J. Lee, K-A Brickman, L. Deslauriers, P.C. Haljan, L.-M. Duan, and C. Monroe, J. Opt. B 7, S371 (2005).  
[23] D.F.V. James, Appl. Phys. B 66, 181 (1998).  
[24] S. Korenblit et al., New J. Phys. 14, 095024 (2012).  
[25] T. Green and M. Biercuk (private communication).  
[26] C. Sackett et al., Nature (London) 404, 256 (2000).  
[27] W. Dür, J. I. Cirac, and R. Tarrach, Phys. Rev. Lett. 83, 3562 (1999).  
[28] C. Shen, Z.-X. Gong, and L.-M. Duan, Phys. Rev. A 88, 052325 (2013).  
[29] T. Monz, K. Kim, W. Hänsel, M. Riebe, A. S. Villar, P. Schindler, M. Chwalla, M. Hennrich, and R. Blatt, Phys. Rev. Lett. 102, 040501 (2009).  
[30] R. Feynman, Int. J. Theor. Phys. 21, 467 (1982).  
[31] H. Walther, B. T. H. Varcoe, B.-G. Englert, and T. Becker, Rep. Prog. Phys. 69, 1325 (2006).  
[32] M. H. Devoret and R. J. Schoelkopf, Science 339, 1169 (2013).