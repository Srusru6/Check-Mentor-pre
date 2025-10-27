# Realization of a Quantum Integer-Spin Chain with Controllable Interactions

C. Senko, $^{1}$  P. Richerme, $^{1}$  J. Smith, $^{1}$  A. Lee, $^{1}$  I. Cohen, $^{2}$  A. Retzker, $^{2}$  and C. Monroe $^{1}$

$^{1}$ Joint Quantum Institute, University of Maryland Department of Physics and National

Institute of Standards and Technology, College Park, Maryland 20742, USA

$^{2}$ Racah Institute of Physics, The Hebrew University of Jerusalem, Jerusalem 91904, Givat Ram, Israel

(Received 6 October 2014; revised manuscript received 16 March 2015; published 17 June 2015)

The physics of interacting integer-spin chains has been a topic of intense theoretical interest, particularly in the context of symmetry-protected topological phases. However, there has not been a controllable model system to study this physics experimentally. We demonstrate how spin-dependent forces on trapped ions can be used to engineer an effective system of interacting spin-1 particles. Our system evolves coherently under an applied spin-1  $XY$  Hamiltonian with tunable, long-range couplings, and all three quantum levels at each site participate in the dynamics. We observe the time evolution of the system and verify its coherence by entangling a pair of effective three-level particles ("qutrits") with  $86\%$  fidelity. By adiabatically ramping a global field, we produce ground states of the  $XY$  model, and we demonstrate an instance where the ground state cannot be created without breaking the same symmetries that protect the topological Haldane phase. This experimental platform enables future studies of symmetry-protected order in spin-1 systems and their use in quantum applications.

DOI: 10.1103/PhysRevX.5.021026

Subject Areas: Atomic and Molecular Physics,

Condensed Matter Physics,

Quantum Physics

# I. INTRODUCTION

A major area of current research is devoted to developing experimentally controllable systems that can be used for quantum computation, quantum communication, and quantum simulation of many-body physics. To date, most experiments have focused on the use of two-level systems ("qubits") for computation and communication [1,2] and for the study of spin-  $1 / 2$  (or spinless) many-body phenomena [3,4]. However, there are a variety of motivations for performing experiments in higher-dimensional Hilbert spaces. Contrary to the intuition that enlarging the spin degree simplifies calculations by making them semiclassical [5], spin  $>1 / 2$  systems inherently have more complexity and cost exponentially more resources to classically simulate. For instance, it is computationally easy to find the ground-state energy of a spin-  $1 / 2$  chain with nearest-neighbor-only interactions in one dimension; for systems with spin  $7 / 2$  or higher, the problem is known to belong to the QMA-complete complexity class, which is a quantum analog of the classical NP-complete class [6,7]. The difficulty of this problem for intermediate spin values, such as spin 1, is still an open question. From a more practical point of view, controllable three-level systems ("qutrits") are useful for quantum logic, since they can

substantially simplify certain operations within quantum algorithms [8,9] and can enhance the efficiency of quantum communication protocols [10].

When individual three-level systems are coupled together, they can be used to encode the physics of interacting spin-1 particles. Such systems have attracted a great deal of theoretical interest following Haldane's conjecture that antiferromagnetic Heisenberg spin-1 chains, as opposed to spin-  $1 / 2$  systems, have a finite energy gap that corresponds to exponentially decaying correlation functions [11,12]. This so-called Haldane phase possesses a doubly degenerate entanglement spectrum [13] and a nonlocal string order [14,15], which is related to the order appearing in spin liquids [16] and in the fractional quantum Hall effect. These characteristics suggest that the Haldane phase is one of the simplest known examples of a symmetry-protected topological phase of matter [14].

In addition to their interesting many-body properties, topological phases may be exploited in a more applied setting. The Haldane phase is useful for quantum operations (for instance, as a perfect quantum wire) [17,18] and can be destroyed only by crossing a phase transition. The finite energy gap in topological spin-1 systems makes them a potential candidate for long-lived, robust quantum memories [19], and schemes using symmetry-protected spin-1 phases for measurement-based quantum computation have also been proposed [20,21].

Several groups have developed controllable three-level quantum systems by using pairs of photons [22], superconducting circuits [23], or dressed states in trapped ions

[24] to implement qutrits, or by using spinor Bose-Einstein condensates (BECs) to study quantum magnetism [25-28]. However, no platform has yet used multiple interacting qutrits for quantum information protocols or for simulating lattice spin models. In this paper, we use trapped atomic ions to simulate a chain of spin-1 particles with tunable, long-range  $XY$  interactions [29]. Our system performs the same basic tasks that are commonly used in spin-1/2 quantum simulations [4,30-46], such as observing dynamical state evolution [44,45], measuring coherence and certifying entanglement [31,40], and adiabatically preparing nontrivial ground states [42]. With two spin-1 particles, we observe coherent evolution under the  $XY$  interactions among states in a "decoherence-free" subspace [47,48]. For certain states generated by the  $XY$  Hamiltonian, we can verify entanglement between a pair of three-level systems with fidelities of up to  $86\%$ . Adding a time-dependent global field allows us to adiabatically prepare the ground state of the  $XY$  model for even numbers of spins, as we demonstrate with two-spin and four-spin chains. For odd numbers of spins, producing the calculated ground state is not possible with a simple adiabatic ramp since it requires crossing a first-order phase transition, hinting at the existence of a symmetry-protected phase. We observe with a three-spin chain that this protection of the ground state is preserved even in the presence of experimental imperfections. It is straightforward to extend our techniques to larger collections of integer spins, providing a route to accessing higher-dimensional Hilbert spaces experimentally. Additionally, the tools demonstrated here could enable future studies of symmetry-protected order and can be extended to SU(3) models and other systems of higher symmetry [49].

# II. EXPERIMENTAL IMPLEMENTATION

The spin-1 chain is represented by a string of  $^{171}\mathrm{Yb}^{+}$  atoms held in a linear Paul trap. Three hyperfine levels in the  $^2 S_{1 / 2}$  ground manifold of each atom are used to encode the spin-1 states:  $| + \rangle \equiv |F = 1, m_F = 1\rangle$ ,  $|- \rangle \equiv |F = 1, m_F = -1\rangle$ , and  $|0\rangle \equiv |F = 0, m_F = 0\rangle$ , with frequency splittings of  $\omega_{\pm}$  between the  $|0\rangle$  and  $|\pm \rangle$  states, as shown in Fig. 1. Here,  $| + \rangle$ ,  $|- \rangle$ , and  $|0\rangle$  are the eigenstates of  $S_z$  with eigenvalues  $+1, -1$ , and 0, respectively;  $F$  and  $m_F$  are quantum numbers associated with the total angular momentum of the atom and its projection along the quantization axis, defined by a magnetic field of  $\sim 5\mathrm{G}$ .

We apply global laser beams to the ion chain with a wave vector difference along a principal axis of transverse motion, polarized to drive stimulated Raman transitions between the  $|0\rangle$  and  $| - \rangle$  states and between the  $|0\rangle$  and  $| + \rangle$  states with equal Rabi frequencies  $\Omega_{i}$  on ion  $i$ , as shown in Fig. 1(a) and Fig. 1(b) [50]. To generate spin-1  $XY$  interactions, we apply two beat frequencies at  $\omega_{-} + \mu$  and  $\omega_{+} - \mu$  to these respective transitions, where  $\mu$  is slightly detuned from the transverse motional frequencies, as shown in Fig. 1(c). Under the rotating wave approximations  $\omega_{\pm} \gg \mu \gg \Omega_{i}$  and within the

![](images/1223057678635da49ee4d499eb954fefccfbaaf0ac7682684033b7ad374cdf0f.jpg)  
FIG. 1. (a) Level diagram for  $^{171}\mathrm{Yb}^{+}$ , highlighting relevant states. (b) Sketch of experimental geometry, showing the directions of the laser wave vectors and the real magnetic field relative to the ion chain. Both beams are linearly polarized, one along the  $\vec{B}$  field (providing  $\pi$  light) and one orthogonal to the  $\vec{B}$  field (providing an equal superposition of  $\sigma^{+}$ and  $\sigma^{-}$ light). Multiple beat notes are applied by imprinting multiple frequencies onto one beam (in this case, the  $\pi$ -polarized beam). (c) Detailed level diagram of the  $^2 S_{1/2}$  ground state, showing Raman beat notes in relation to Zeeman splittings and motional sidebands for the center-of-mass mode. Level splittings are not to scale.

![](images/9d3f258d148ca1003ec51bc6614e546226d0a977c746148d10b80ba19049acbf.jpg)

Lamb-Dicke regime ( $\Delta k\langle \hat{x}_i\rangle \ll 1$ , with  $\Delta k$  the wave vector difference of the Raman beams and  $\hat{x}_i$  the position operator of the  $i$ th ion), the resulting interaction Hamiltonian (with  $h = 1$ ) is

$$
H = \sum_ {i, m = 1} ^ {N} \frac {i \eta_ {i , m} \Omega_ {i}}{2 \sqrt {2}} \left(- S _ {+} ^ {i} a _ {m} e ^ {i (\mu - \omega_ {m}) t} + S _ {-} ^ {i} a _ {m} ^ {\dagger} e ^ {- i (\mu - \omega_ {m}) t}\right). \tag {1}
$$

Here,  $a_{m}$  and  $a_{m}^{\dagger}$  are the phonon operators of the normal mode  $m$  with frequency  $\omega_{m},\eta_{i,m} = b_{i,m}\sqrt{\hbar(\Delta k)^{2} / (2M\omega_{m})}$  is the Lamb-Dicke factor (where  $b_{i,m}$  is the normal mode transformation matrix [51] and  $M$  is the mass of a single ion), and the spin raising and lowering operators  $S_{\pm}^{i}$  satisfy the commutation relations  $[S_{+}^{i},S_{-}^{j}] = 2S_{z}^{i}\delta_{ij}$ . In the limit where the beat notes are far detuned ( $\eta_{i,m}\Omega_{i}\ll |\mu -\omega_{m}|$ ) and the phonons are only virtually excited, this results in an effective Hamiltonian with  $XY$ -type spin-spin interactions and spin-phonon couplings:

$$
\begin{array}{l} H _ {\text {e f f}} = \sum_ {i <   j} \frac {J _ {i , j}}{4} \left(S _ {+} ^ {i} S _ {-} ^ {j} + S _ {-} ^ {i} S _ {+} ^ {j}\right) \\ + \sum_ {i, m} V _ {i, m} \left[ \left(2 a _ {m} ^ {\dagger} a _ {m} + 1\right) S _ {z} ^ {i} - \left(S _ {z} ^ {i}\right) ^ {2} \right]. \tag {2} \\ \end{array}
$$

The pure spin-spin interaction in the first term of Eq. (2) follows the same formula as for generating spin-1/2 Ising interactions [50]:

$$
J _ {i, j} = \Omega_ {i} \Omega_ {j} \sum_ {m} \frac {\eta_ {i , m} \eta_ {j , m}}{2 (\mu - \omega_ {m})}. \tag {3}
$$

When  $\mu$  is larger than the transverse center-of-mass frequency,  $J_{i,j}$  falls off with distance as roughly  $J_{i,j} \sim J_0 / |i - j|^{\alpha}$ , where  $J_0$  is of order  $\approx 1\mathrm{kHz}$  and  $\alpha$  can be tuned between 0 and 3 using trap and laser parameters [41,52].

The  $V_{i,m}$  term in Eq. (2) is given by a similar formula:

$$
V _ {i, m} = \frac {\left(\eta_ {i , m} \Omega_ {i}\right) ^ {2}}{8 \left(\mu - \omega_ {m}\right)}. \tag {4}
$$

For very long-ranged spin-spin interactions  $(\alpha \lesssim 0.5)$ , or for small numbers of ions, the  $V_{i,m}$  terms are approximately uniform across the spin chain. In these instances, the  $V_{i,m}$  coefficient can be factored out of the sum over ions in Eq. (2), leaving only global  $S_z^i$  and  $(S_z^i)^2$  effective field terms, where the magnitude of the  $S_z^i$  field is dependent on the number of phonons in each mode. The phonon dependence can be ignored by restricting the dynamics to the  $\sum_{i}S_{z}^{i} = 0$  subspace, as discussed below. For short-range interactions or for longer chain lengths, the  $V_{i,m}$  terms can be eliminated completely by adding an additional set of beat frequencies at  $\omega_{-} - \mu$  and  $\omega_{+} + \mu$ , which would generate Ising-type interactions between effective spin-1 particles using the Mølmer-Sørensen gate [53]. As has been demonstrated in spin-1/2 systems, such Ising interactions (along with a strong effective magnetic field) can themselves be utilized to study the dynamics of  $XY$  interactions [44,45].

The ions are initialized before each experiment by cooling the transverse modes near their ground state of motion ( $\bar{n} \approx 0.05$ ) and optically pumping the spins to the  $|00\dots\rangle$  state. After applying the Hamiltonian in Eq. (2) for varying lengths of time, we measure the population of the state  $|0\rangle$  at each site by imaging spin-dependent fluorescence [54] onto an intensified CCD camera and observing which ions are "dark." Because both of the  $|\pm\rangle$  states appear "bright" during the detection process and are scattered into an incoherent mixture of the  $|F = 1\rangle$  states, our current setup does not allow discrimination among all three possible spin states in a single experiment. However, we can measure the population of either  $|+ \rangle$  or  $|- \rangle$  by repeating the experiment and applying a  $\pi$  rotation to the appropriate  $|0\rangle \leftrightarrow |\pm\rangle$  transition before the fluorescence imaging. For instance, measuring an ion in the dark state after a  $\pi$  pulse between  $|0\rangle \leftrightarrow |+ \rangle$  indicates that the spin was in the  $|+ \rangle$  state before detection. This binary discrimination is not a fundamental limit to future experiments, since populations could be "shelved" into atomic states that do not participate in the detection cycle.

Since the ions are initialized to the  $|00\dots \rangle$  state, and because the spin-spin interactions in Eq. (2) conserve the quantity  $\sum_{i}S_{z}^{i}\equiv S_{z}$ , the dynamics are restricted to the set

of states with  $S_{z} = 0$ . The  $S_{z} = 0$  subspace is protected against fluctuations in the real magnetic field  $\Delta B(t)$ , which would otherwise result in an unwanted noise term  $\mu_B\Delta B(t)\mathcal{S}_z$  (where  $\mu_B$  is the Bohr magneton). For instance, the  $T_{2}$  coherence times of the  $|0\rangle \leftrightarrow |\pm \rangle$  transitions are measured to be  $0.5\mathrm{ms}$ , limited by magnetic field noise. Nevertheless, the data in Figs. 2 and 3 exhibit coherence and entanglement for several milliseconds (limited by laser intensity noise), demonstrating the robustness of this decoherence-protected subspace against time-varying

![](images/e44e3171491ec134bd7532f43d693ae7ac8660b47106dcbc837744aea104f38d.jpg)

![](images/7af0cc74db7ad73d96a835e66b3607032cd61a26dc6d95d290e44755ad7a57bd.jpg)

![](images/01efb4697757db03b29ba0a46c436f22d0c0b8a9c72e14b4a4d731295a99ba61.jpg)  
FIG. 2. Dynamics of two spin-1 particles evolving under the  $XY$  Hamiltonian in Eq. (2). (a) We measure the populations for each ion to be in the state  $|0\rangle$ . The probability of both ions to be in  $|0\rangle$  (black diamonds), only the left ion in  $|0\rangle$  (blue triangles), only the right ion in  $|0\rangle$  (green squares), and neither ion in  $|0\rangle$  (red circles) are plotted together. Similar plots for the  $| - \rangle$  state (b) and  $| + \rangle$  state (c) are also shown, with a different symbol order emphasizing that the red circles represent the same state in all three graphs. The dynamics resemble Rabi flopping between the state  $|00\rangle$  and the symmetric superposition  $(| + - \rangle + | - + \rangle)/\sqrt{2}$ . Solid lines represent theoretical predictions, with the only free parameters being the magnitude of the  $S_{z}$  and  $(S_{z})^{2}$  gradients discussed in the text. In (c), the interaction  $J_{1,2}$  drifts at long times compared to that estimated from Eq. (3), consistent with an observed drift in radial trap frequencies during the data collection. Error bars (1s.d.) show the statistical uncertainty based on 500 repetitions of the experiment.

![](images/234349bee1b1cb240ae1c497dfcb89485a452dc1d6876d49fb16f1d1807ee1ee.jpg)  
FIG. 3. (a) Illustration of the rotations performed before measuring the parity, where rotations by  $\theta$  and  $\varphi$  are defined in Eq. (5). Also shown are the ideal initial state and the states produced after each step. (b) The parity of the final state oscillates as a function of the final pulse phase  $\varphi$ . Fitting the function  $C - A\cos 2\varphi + B\sin 2\varphi$  (red dashed line) to the data results in an amplitude  $A = 0.86 > 0.5$ , demonstrating entanglement. (c) Amplitude of the parity oscillation after various durations of the spin-spin interaction, showing the peak amplitude for each time  $\sim (2n + 1) / (2\sqrt{2} J_{1,2})$ . The data in (b) correspond to the highest-contrast point in (c). The dashed line is a guide to the eye, suggesting the expected behavior of sinusoidal oscillations between a product state and an entangled state, along with decay due to decoherence at longer times. The chosen durations are not evenly spaced past  $0.6\mathrm{ms}$ : for each point, the duration is chosen such that the population in  $|00\rangle$  is at a local minimum, and drifts in the radial trap frequencies lead to small changes in  $J_{1,2}$ .

magnetic fields. We expect that, independent of laser-induced decoherence, the coherence times within this subspace could reach seconds [54], since the magnetic field noise  $\Delta B(t)$  will introduce the same second-order effects as in the case of the hyperfine "clock" qubit. This improved coherence does not require any extra overhead for either initialization, readout, or generation of spin-spin interactions. Additionally, remaining within the  $S_{z} = 0$  subspace does not substantially limit the size of the accessible Hilbert space, since the number of states in the  $S_{z} = 0$  subspace of  $N$  spin-1 particles scales as

$\sim 3^{N} / (2\sqrt{N})$  for large  $N$ , which is exponentially greater than the  $2^{N}$  states accessible in a spin-1/2 system.

Our implementation of a decoherence-protected subspace is closely analogous to techniques that have been used for extending the coherence time of certain spin-  $1/2$  quantum simulations [45], and for creating a logical qubit that is robust to environmental perturbations [48], for which a universal gate set has been demonstrated [55]. In addition to the quantum simulations discussed in this work, our approach could potentially be used in quantum logic to encode a logical qutrit using two physical qutrits. For example, we would encode  $|+ \rangle_{L} \equiv |+ - \rangle$ ,  $|0 \rangle_{L} \equiv |00 \rangle$ , and  $| - \rangle_{L} \equiv |- + \rangle$ . Such a logical qutrit could be trivially initialized, deterministically measured in a single shot, without recourse to shelving techniques, by measuring the  $|+\rangle$  or  $|-\rangle$  components of the physical qutrits (using  $\pi$  rotations from  $| \pm \rangle$  to  $|0\rangle$ ), and operated upon using the  $XY$ -type interactions demonstrated here (which would be equivalent to a logical  $S_{x}$  or  $S_{y}$ , depending on laser phases) or a local  $S_{z}$  applied to one of the physical qutrits (equivalent to a logical  $S_{z}$ ). A conditional phase gate between two logical qutrits, which (along with single-qutrit manipulations) permits a universal gate set for quantum computation with qutrits [56], could be accomplished by the application of an Ising-type  $(S_{z}^{i} S_{z}^{j})$  interaction involving one physical qutrit from each pair. These operations could be accomplished on similar time scales to those for typical two-qubit gates in trapped ions, on the order of hundreds of  $\mu s$ . We note that a complementary technique has been demonstrated for encoding a decoherence-resistant qutrit (or qubit) in a single atom, at the expense of requiring the continuous application of microwave dressing fields [24,57].

# III. COHERENT DYNAMICS OF TWO SPINS AND ENTANGLEMENT VERIFICATION

For a system of two spins, dynamical evolution under the Hamiltonian in Eq. (2) can be understood as Rabi flopping between the  $|00\rangle$  and  $(|+ - \rangle +| - + \rangle) / \sqrt{2}$  states with Rabi frequency  $\sqrt{2} J_{1,2}$ . This behavior is shown in Fig. 2, where Figs. 2(a)-2(c) show the probability of each ion to be in the  $|0\rangle$ ,  $| - \rangle$ , and  $|+\rangle$  states, respectively. The population remains in the  $S_{z} = 0$  subspace, as expected: Fig. 2(a) shows the absence of the  $S_{z}\neq 0$  states  $(|0 + \rangle ,|0 - \rangle ,| + 0\rangle$  and  $| - 0\rangle)$ , while Figs. 2(b) and 2(c), respectively, show the absence of the other  $S_{z}\neq 0$  states  $| - - \rangle$  and  $| + + \rangle$ . The drift in  $J_{1,2}$  evidenced in Fig. 2(c) could be stabilized in future experiments by feeding back to the trap rf voltage to better stabilize the radial trap frequencies.

The different ions  $i$  can experience position-dependent  $S_{z}^{i}$  and  $(S_z^i)^2$  shifts, whose effects are visible in the slight divergence of the blue and green curves in Figs. 2(b) and 2(c). We attribute this effect to a micromotion gradient, since the shifts can be compensated by adjustments of the voltages on the dc trap electrodes, and since (based on

calibration experiments with three ions in which we measure the transition energies from  $|000\rangle$  to other states in the  $S_{z} = 0$  subspace in the presence of an uncompensated gradient) the energy levels are consistent with a linear gradient in position.

The calculation overlaid in Fig. 2 includes the site-dependent terms  $(200\mathrm{Hz})S_z^{(2)} + (150\mathrm{Hz})(S_z^{(2)})^2$ , which were left as free-fitting parameters when numerically evolving the Schrödinger equation under the Hamiltonian in Eq. (2), since the calibrations mentioned above have a precision of only  $\sim 200\mathrm{Hz}$ . The plotted curves assume strictly unitary evolution (i.e., no decoherence) over the time scale of the experiments.

At a time  $t = 0.5 / (\sqrt{2} J_{1,2})$ , which is roughly  $0.27\mathrm{ms}$  in Fig. 2, the system is left approximately in the entangled state  $(| + - \rangle + | - + \rangle) / \sqrt{2}$ . To verify entanglement in the system, one could use spin-1 analogs of Bell-type inequalities [58], which require many local rotations but are sensitive to maximally entangled states like  $(|00\rangle + | + - \rangle + | - + \rangle) / \sqrt{3}$ . However, for the class of states generated by the  $XY$  interactions, a much simpler series of global rotations is sufficient to verify entanglement. The analysis consists of performing three sequential rotations on the  $|0\rangle$  to  $|\pm \rangle$  transitions,

$$
R _ {0 \pm} (\theta , \phi) = e ^ {\left[ (i \theta / 2) \sum_ {k} \left[ e ^ {\pm i \phi} (| \pm \rangle \langle 0 |) _ {k} + e ^ {\mp i \phi} (| 0 \rangle \langle \pm |) _ {k} \right] \right]}, \tag {5}
$$

before measuring the population in  $|0\rangle$ . The rotation sequence is given by  $R_{0+}(\pi/2, \varphi)R_{0+}(\pi/2, 0)R_{0-}(\pi, 0)$ , with the rotations applied from right to left. The first two rotations map the state  $(|+-\rangle + |-+\rangle) / \sqrt{2}$  to  $(|00\rangle + |++\rangle) / \sqrt{2}$ , while the phase of the third rotation is varied to analyze the entanglement of this resulting state [59]. The parity  $\Pi = \sum_{j=0}^{2} (-1)^{j} P_{j}$  (with  $P_{j}$  the probability of  $j$  atoms in  $|0\rangle$ ) oscillates as a function of the phase  $\varphi$  of the third pulse, and the amplitude of its oscillation depends on the off-diagonal density matrix elements:

$$
\begin{array}{l} \Pi (\varphi) = C + \frac {1}{2} \cos 2 \varphi (P _ {- -} + P _ {+ +} - P _ {+ -} - P _ {- +} \\ - 2 | \rho_ {+ -, - +} | - 2 | \rho_ {- -, + +} |) + \frac {1}{2} \sin 2 \varphi (2 | \rho_ {- +, + +} | \\ + 2 | \rho_ {+ -, + +} | - 2 | \rho_ {- -, - +} | - 2 | \rho_ {- +, - -} |), \tag {6} \\ \end{array}
$$

where  $P_{i}$  is the population in state  $|i\rangle$ $(|i\rangle = | - - \rangle ,| - + \rangle$  etc.),  $\rho_{i,j}$  is the off-diagonal density matrix element quantifying the coherence between  $|i\rangle$  and  $|j\rangle$ , and  $C$  is a constant offset that depends on the various density matrix elements but not on the phase  $\varphi$  of the final rotation. The populations in  $| + + \rangle$  and  $| - - \rangle$  are negligible, simplifying this expression:

$$
\Pi (\varphi) \approx C - A \cos 2 \varphi , \tag {7}
$$

where the oscillation amplitude

$$
A = \frac {1}{2} \left(P _ {+ -} + P _ {- +} + 2 \left| \rho_ {+ -, - +} \right|\right) \tag {8}
$$

is akin to the entanglement fidelity  $\mathcal{F}$  of Greenberger-Horne-Zeilinger (GHZ) states in two-level systems [59]. Measuring the amplitude  $A$  of the parity oscillation  $\Pi(\varphi)$  then allows us to verify entanglement for certain classes of states. According to an analysis analogous to that in Ref. [59], the following inequality holds for all separable qutrit states:

$$
2 A + P _ {0 0} + 2 \left| \rho_ {+ -, 0 0} \right| + 2 \left| \rho_ {- +, 0 0} \right| \leq 1. \tag {9}
$$

Hence, violation of this inequality demonstrates entanglement between spin-1 particles or qubits, and measuring an amplitude of  $A > 1 / 2$  is sufficient to violate the inequality.

Figure 3(b) shows an example of the measured parity curve used to extract the amplitude  $A$  and verify entanglement between the qutrit pair. Such measurements can be repeated for different durations of exposure to the  $XY$  Hamiltonian. At times  $t = (2n + 1) / (2\sqrt{2} J_{1,2})$  ( $n = 0,1,2,\ldots$ ), the system should again be in the state  $(|+ - \rangle + |- + \rangle) / \sqrt{2}$ , while at times  $t = n / (\sqrt{2} J_{1,2})$ , it should return to the unentangled product state  $|00\rangle$ . The result is plotted in Fig. 3(c).

Two known sources of dephasing contribute to the observed loss of coherence in the experiment. First, laser intensity fluctuations and pointing instability cause noise in the spin-spin coupling term, leading to apparent dephasing when many repetitions are averaged together. These fluctuations could be compensated in future experiments by variants of the method of composite pulses [60,61]. The second dephasing source results from inhomogeneities in the  $V_{i,m}$  term [Eq. (2)] across the chain, which will cause different spins to acquire phases at different rates. This is mainly a concern in chains longer than two ions (although inhomogeneous Rabi frequencies  $\Omega_{i}$  can cause  $V_{i,m}$ -induced dephasing even for two spins), and could be compensated by adding an extra driving term to cancel the inhomogeneities or by applying a series of echo pulses [62,63]. Fluctuating external magnetic fields and off-resonant coupling to the carrier transition would ordinarily add dephasing noise along the  $\hat{z}$  direction, but these have been suppressed here by working in the  $S_{z} = 0$  subspace.

# IV. GROUND STATE PRODUCTION

We can also add an effective  $(S_z^i)^2$  field term,  $D\sum_{i = 1}^{N}(S_{z}^{i})^{2}$ , to the Hamiltonian by shifting the beat frequencies of the Raman lasers to  $\omega_{+} - \mu - D$  and  $\omega_{-} + \mu - D$ . This  $(S_z^i)^2$  term can be used to adiabatically prepare the ground state of the  $XY$  Hamiltonian in Eq. (2). As before, the spins are prepared in  $|00\dots\rangle$ , which is the

![](images/b4cfc760418330e58de4620bb7752d92b05c8408ef2141456a4f835e871478aa.jpg)  
FIG. 4. Measurements of the prepared two-spin states (narrow blue bars) after ramping an  $(S_z)^2$  field, compared to the values expected for the calculated ground state (gray bars). As in Fig. 2(a)-(c) show the measured populations when the dark state is set to be  $|0\rangle$ ,  $| - \rangle$ , or  $| + \rangle$ , respectively.

approximate ground state of Eq. (2) in the presence of a large  $(5\mathrm{kHz})$ $(S_z^i)^2$  field. This field is then ramped down slowly according to  $D(t) = (5\mathrm{kHz})e^{-t / (0.167~\mathrm{ms})}$ . Figures 4 and 5 show the populations measured at the end of the  $(S_z^i)^2$  ramp for two and four spins, which match reasonably well with the calculated ground state.

Measurements of populations in the  $S_{z}$  basis necessarily discard phase information about components of the final

![](images/da7db8366fe3b8f66cafc17fea464da938c2666115c6c89ca2fc57bb433d4b4e.jpg)

![](images/09b3314e512c39137184e69ea2bf7e59c9f263876b2c43f72b154c0d44171ae7.jpg)

![](images/3eb55e79f7b5697a9226842bcc6d99b75898518f952711a1762672fb9fcd9b0c.jpg)  
FIG. 5. Measurements of the prepared four-spin states (narrow blue bars) after ramping an  $(S_z)^2$  field, compared to the values expected for the calculated ground state (gray bars). Again, (a)-(c) show the measured populations when the dark state is set to be  $|0\rangle$ ,  $|-\rangle$ , or  $|+\rangle$ , respectively. Here, the interaction range is given by  $J_{i,j} \sim 1 / |i - j|^{0.3}$ .

![](images/b07b2e358c99146c1dee30a95cc9426974c7d54f6fd97a9bb2e43064adde63b2.jpg)  
FIG. 6. Following an adiabatic ramp, the parity of the final state is measured as a function of the final rotation phase  $\varphi$  (see text for rotation protocol). Dashed and dot-dashed lines represent the theoretically expected values for the ground state,  $|00\rangle/\sqrt{2} - (| - + \rangle + | + - \rangle)/2$ , and highest excited state,  $|00\rangle/\sqrt{2} + (| - + \rangle + | + - \rangle)/2$ , respectively. The phase of the oscillation reveals that the relative phases in the prepared state are consistent with the expected ground state.

state. This can be important in many spin models, including the  $XY$  model, where such measurements alone cannot discriminate between different eigenstates. For example, the ground state of an  $XY$  model with two spin-1 particles is  $\left|00\rangle / \sqrt{2} - \left(|-+\rangle + |+-\rangle\right) / 2$ , while the highest excited state is  $\left|00\rangle / \sqrt{2} + \left(|-+\rangle + |+-\rangle\right) / 2$ , differing by only a relative phase. We check that we are creating the ground state after our adiabatic protocol by applying a pair of rotations,  $R_{0-}(\pi/2, \varphi) R_{0+}(\pi/2, 0)$ , and measuring the parity  $\Pi$ , as was done in the entanglement analysis. This is expected to result in  $\Pi(\varphi) = (3/8) \pm (1/2) \cos \varphi$ , where  $+$  and  $-$  correspond to the ground and highest excited states, respectively. As shown in Fig. 6, our measurements are consistent with having prepared the two-spin ground state.

![](images/79041e479c77c4791fe9e6a430164d746f9f4ef0ff081377435742eb8605208c.jpg)  
FIG. 7. Measurements when the  $|0\rangle$  state is set dark (a), the  $|+\rangle$  state is dark (b), and the  $|-\rangle$  state is dark (c), of the prepared three-spin state after adiabatically ramping a global  $(S_z^i)^2$  field (narrow blue bars). The data agree closely with the calculated populations in the first excited state (gray bars), while showing little overlap with the expected populations in the ground state (wide, hatched red bars).

# V. TOWARD HALDANE PHYSICS

A more long-term goal for spin-1 quantum simulations is to produce and study ground states in the Haldane phase [29]. It is known that an  $XY$  model with both nearest-neighbor and next-nearest-neighbor interactions can exhibit a symmetry-protected Haldane phase [64], and it remains an open question whether a generic long-range  $XY$  model would show the same behavior. Already with our experimentally implemented Hamiltonian, we find a useful test case where the symmetry of the ground state prevents it from being created via the simple adiabatic protocol described above.

The ground state  $|\psi \rangle_{\mathrm{gs}}$  of a long-range  $XY$  model can be calculated exactly for three spins. For our experimental coupling strengths  $J_{i,j} \sim 1 / |i - j|^{0.36}$ ,

$$
\begin{array}{l} \left| \psi \right\rangle_ {\mathrm {g s}} = \sqrt {0 . 1 6} \left(\left| 0 - + \right\rangle - \left| 0 + - \right\rangle + \left| - + 0 \right\rangle - \left| + - 0 \right\rangle\right) \\ + \sqrt {0 . 1 8} (| + 0 - \rangle - | - 0 + \rangle). \tag {10} \\ \end{array}
$$

This state has a  $99.9\%$  overlap with a three-spin Affleck-Kennedy-Lieb-Tasaki (AKLT) state [65], which is the canonical example of a ground state in the Haldane phase that can be written in closed form for any number of spins. The state in Eq. (10) is antisymmetric with respect to the same symmetries that govern the Haldane phase, such as left-right spatial inversion of the chain or a global rotation about  $S_{x}$  by  $\pi$  (which sends  $|+\rangle$  to  $|->$  and vice versa). However, since the starting state  $|000\rangle$  and the applied Hamiltonian are symmetric with respect to these operations, we should be unable to reach the antisymmetric ground state with a simple adiabatic ramp. Indeed, we find numerically that a first-order phase transition separates the symmetric and antisymmetric ground states, which cannot be adiabatically connected without breaking inversion and rotational symmetry. For the three-spin experiment in Fig. 7, we, hence, prepare a state close to the first excited state rather than the ground state. This observation suggests that even in the presence of various experimental imperfections, the ground state of our three-spin  $XY$  model enjoys the same symmetry protection as the Haldane phase.

In this paper, we demonstrate the basic ingredients that are needed for the implementation of quantum simulations with spins greater than  $1/2$ , using a platform in which there are no fundamental limitations to scaling toward larger spin chains. We believe that this work opens paths for studying the exciting physics beyond spin-1/2 systems, and we have already taken the first steps towards exploring the richness of topological phases. In particular, for a long-range spin-1  $XY$  model, we demonstrate coherent Schrödinger evolution and the capability to create symmetric ground states. We observe that for odd numbers of spins, symmetry considerations prevent us from creating ground states that bear a close resemblance to AKLT states and, hence, may belong to the Haldane phase. Future work will address the

questions of how to add a Heisenberg term and symmetry-breaking perturbations to the Hamiltonian so as to prepare antisymmetric ground states [29], which will allow us to create and probe interesting edge states in the Haldane phase.

# ACKNOWLEDGMENTS

We thank Brian Neyenhuis, Paul Hess, Alexey Gorshkov, and Zhe-Xuan Gong for critical discussions. A.R. acknowledges the support of the European Commission STREP EQuaM, Emulators of Quantum frustrated Magnetism, Grant Agreement No. 323714. This work is supported by the ARO Atomic Physics Program, the AFOSR MURI on Quantum Measurement and Verification, the DARPA Optical Lattice Emulator Program, the IARPA MQCO Program, and the NSF Physics Frontier Center at JQI. Funding for Open Access provided by the UMD Libraries Open Access Publishing Fund.

[1] V. Scarani, H. Bechmann-Pasquinucci, N.J. Cerf, M. Dusek, N. Lutkenhaus, and M. Peev, The Security of Practical Quantum Key Distribution, Rev. Mod. Phys. 81, 1301 (2009).  
[2] T. D. Ladd, F. Jelezko, R. Laflamme, Y. Nakamura, C. Monroe, and J. L. O'Brien, Quantum Computers, Nature (London) 464, 45 (2010).  
[3] I. Bloch, J. Dalibard, and S. Nascimbene, Quantum Simulations with Ultracold Gases, Nat. Phys. 8, 267 (2012).  
[4] R. Blatt and C. F. Roos, Quantum Simulations with Trapped Ions, Nat. Phys. 8, 277 (2012).  
[5] A. Auerbach, Interacting Electrons and Quantum Magnetism (Springer, New York, 1994).  
[6] D. Aharonov, D. Gottesman, S. Irani, and J. Kempe, in Proceedings of the 48th Annual IEEE Symposium on Foundations of Computer Science, 2007 (FOCS '07) (IEEE, New York, 2007), pp. 373-383.  
[7] S. Hallgren, D. Nagaj, and S. Narayanaswami, The Local Hamiltonian Problem on a Line with Eight States is QMA-Complete, Quantum Inf. Comput. 13, 0721 (2013).  
[8] T. C. Ralph, K. J. Resch, and A. Gilchrist, Efficient Toffoli Gates Using Qudits, Phys. Rev. A 75, 022313 (2007).  
[9] B.P. Lanyon, M. Barbieri, M.P. Almeida, T. Jennewein, T.C. Ralph, K.J. Resch, G.J. Pryde, J.L. O'Brien, A. Gilchrist, and A.G. White, Simplifying Quantum Logic Using Higher-Dimensional Hilbert Spaces, Nat. Phys. 5, 134 (2009).  
[10] C. Brukner, M. Zukowski, and A. Zeilinger, Quantum communication complexity protocol with two entangled qutrits, Phys. Rev. Lett. 89, 197901 (2002).  
[11] F. D. M. Haldane, Continuum Dynamics of the 1-D Heisenberg Antiferromagnet: Identification with the  $O(3)$  Nonlinear Sigma Model, Phys. Lett. A 93, 464 (1983).  
[12] F.D.M. Haldane, Nonlinear Field Theory of Large-Spin Heisenberg Antiferromagnets: Semiclassically Quantized

Solitons of the One-Dimensional Easy-Axis Néel State, Phys. Rev. Lett. 50, 1153 (1983).  
[13] F. Pollmann, A.M. Turner, E. Berg, and M. Oshikawa, Entanglement Spectrum of a Topological Phase in One Dimension, Phys. Rev. B 81, 064439 (2010).  
[14] T. Kennedy and H. Tasaki, Hidden  $z_{2} \times z_{2}$  Symmetry Breaking in Haldane-Gap Antiferromagnets, Phys. Rev. B 45, 304 (1992).  
[15] T. Kennedy and H. Tasaki, Hidden Symmetry Breaking and the Haldane Phase in  $s = 1$  Quantum Spin Chains, Commun. Math. Phys. 147, 431 (1992).  
[16] L. Balents, Spin Liquids in Frustrated Magnets, Nature (London) 464, 199 (2010).  
[17] A. S. Darmawan and S. D. Bartlett, Optical Spin-1 Chain and Its Use as a Quantum-Computational Wire, Phys. Rev. A 82, 012328 (2010).  
[18] M. Asoudeh and V. Karimipour, Perfect State Transfer on Spin-1 Chains, Quantum Inf. Process. 13, 601 (2014).  
[19] D.V. Else, S.D. Bartlett, and A.C. Doherty, Symmetry Protection of Measurement-Based Quantum Computation in Ground States, New J. Phys. 14, 113016 (2012).  
[20] G. K. Brennen and A. Miyake, Measurement-Based Quantum Computer in the Gapped Ground State of a Two-Body Hamiltonian, Phys. Rev. Lett. 101, 010502 (2008).  
[21] D. V. Else, I. Schwarz, S. D. Bartlett, and A. C. Doherty, Symmetry-Protected Phases for Measurement-Based Quantum Computation, Phys. Rev. Lett. 108, 240505 (2012).  
[22] B. P. Lanyon, T. J. Weinhold, N. K. Langford, J. L. O'Brien, K. J. Resch, A. Gilchrist, and A. G. White, Manipulating Biphotonic Qutritis, Phys. Rev. Lett. 100, 060504 (2008).  
[23] R. Bianchetti, S. Filipp, M. Baur, J.M. Fink, C. Lang, L. Steffen, M. Boissonneault, A. Blais, and A. Wallraff, Control and Tomography of a Three Level Superconducting Artificial Atom, Phys. Rev. Lett. 105, 223601 (2010).  
[24] J. Randall, S. Weidt, E. D. Standing, K. Lake, S. C. Webster, D. F. Murgia, T. Navickas, K. Roth, and W. K. Hensinger, Efficient Preparation and Detection of Microwave Dressed-State Qubits and Qutrits with Trapped Ions, Phys. Rev. A 91, 012322 (2015).  
[25] M.-S. Chang, Q. Qin, W. Zhang, L. You, and M.S. Chapman, Coherent Spinor Dynamics in a Spin-1 Bose Condensate, Nat. Phys. 1, 111 (2005).  
[26] D.M. Stamper-Kurn and M. Ueda, Spinor Bose Gases: Symmetries, Magnetism, and Quantum Dynamics, Rev. Mod. Phys. 85, 1191 (2013).  
[27] C. V. Parker, L.-C. Ha, and C. Chin, Direct Observation of Effective Ferromagnetic Domains of Cold Atoms in a Shaken Optical Lattice, Nat. Phys. 9, 769 (2013).  
[28] D. L. Campbell, R. M. Price, A. Putra, A. Valdes-Curiel, D. Trypogeorgos, and I. B. Spielman, Itinerant Magnetism in Spin-Orbit Coupled Bose gases, arXiv:1501.05984.  
[29] I. Cohen and A. Retzker, Proposal for Verification of the Haldane Phase Using Trapped Ions, Phys. Rev. Lett. 112, 040503 (2014).  
[30] A. Friedenauer, H. Schmitz, J. T. Glueckert, D. Porras, and T. Schaetz, Simulating a Quantum Magnet with Trapped Ions, Nat. Phys. 4, 757 (2008).  
[31] K. Kim, M.-S. Chang, S. Korenblit, R. Islam, E. E. Edwards, J. K. Freericks, G.-D. Lin, L.-M. Duan, and C. Monroe,

Quantum Simulation of Frustrated Ising Spins with Trapped Ions, Nature (London) 465, 590 (2010).  
[32] R. Gerritsma, G. Kirchmair, F. Zaehringer, E. Solano, R. Blatt, and C.F. Roos, Quantum Simulation of the Dirac Equation, Nature (London) 463, 68 (2010).  
[33] E. E. Edwards, S. Korenblit, K. Kim, R. Islam, M.-S. Chang, J. K. Freericks, G.-D. Lin, L.-M. Duan, and C. Monroe, Quantum Simulation and Phase Diagram of the TransverseField Ising Model with Three Atomic Spins, Phys. Rev. B 82, 060412 (2010).  
[34] R. Gerritsma, B. P. Lanyon, G. Kirchmair, F. Zähringer, C. Hempel, J. Casanova, J. J. Garcia-Ripoll, E. Solano, R. Blatt, and C. F. Roos, Quantum Simulation of the Klein Paradox, Phys. Rev. Lett. 106, 060503 (2011).  
[35] R. Islam, E. E. Edwards, K. Kim, S. Korenblit, C. Noh, H. Carmichael, G.-D. Lin, L.-M. Duan, C.-C. Joseph Wang, J. K. Freericks, and C. Monroe, Onset of a Quantum Phase Transition with a Trapped Ion Quantum Simulator, Nat. Commun. 2, 377 (2011).  
[36] B. Lanyon, C. Hempel, D. Nigg, M. Mueller, R. Gerritsma, F. Zaehringer, P. Schindler, J. T. Barreiro, M. Rambach, G. Kirchmair, M. Hennrich, P. Zoller, R. Blatt, and C. F. Roos, Universal Digital Quantum Simulation with Trapped Ions, Science 334, 57 (2011).  
[37] K. Kim, S. Korenblit, R. Islam, E. E. Edwards, M.-S. Chang, C. Noh, H. Carmichael, G.-D. Lin, L.-M. Duan, C.-C. Joseph Wang, J. K. Freericks, and C. Monroe, Quantum Simulation of the Transverse Field Ising Model with Trapped Ions, New J. Phys. 13, 105003 (2011).  
[38] J. T. Barreiro, M. Mueller, P. Schindler, D. Nigg, T. Monz, M. Chwalla, M. Hennrich, C. F. Roos, P. Zoller, and R. Blatt, An Open-System Quantum Simulator with Trapped Ions, Nature (London) 470, 486 (2011).  
[39] J. W. Britton, B. C. Sawyer, A. C. Keith, C.-C. J. Wang, J. K. Freericks, H. Uys, M. J. Biercuk, and J. J. Bollinger, Engineered Two-Dimensional Ising Interactions in a Trapped-Ion Quantum Simulator with Hundreds of Spins, Nature (London) 484, 489 (2012).  
[40] A. Khromova, Ch. Piltz, B. Scharfenberger, T. F. Gloger, M. Johanning, A. F. Varon, and Ch. Wunderlich, Designer Spin Pseudomolecule Implemented with Trapped Ions in a Magnetic Gradient, Phys. Rev. Lett. 108, 220502 (2012).  
[41] R. Islam, C. Senko, W.C. Campbell, S. Korenblit, J. Smith, A. Lee, E.E. Edwards, C.-C.J. Wang, J.K. Freericks, and C. Monroe, Emergence and Frustration of Magnetic Order with Variable-Range Interactions in a Trapped Ion Quantum Simulator, Science 340, 583 (2013).  
[42] P. Richerme, C. Senko, J. Smith, A. Lee, S. Korenblit, and C. Monroe, Experimental Performance of a Quantum Simulator: Optimizing Adiabatic Evolution and Identifying Many-Body Ground States, Phys. Rev. A 88, 012334 (2013).  
[43] P. Richerme, C. Senko, S. Korenblit, J. Smith, A. Lee, R. Islam, W. C. Campbell, and C. Monroe, Quantum Catalysis of Magnetic Phase Transitions in a Quantum Simulator, Phys. Rev. Lett. 111, 100506 (2013).  
[44] P. Richerme, Z.-X. Gong, A. Lee, C. Senko, J. Smith, M. Foss-Feig, S. Michalakis, A. V. Gorshkov, and C. Monroe, Non-local Propagation of Correlations in Quantum Systems

with Long-Range Interactions, Nature (London) 511, 198 (2014).  
[45] P Jurcevic, B. P. Lanyon, P. Hauke, C. Hempel, P. Zoller, R. Blatt, and C. F. Roos, Quasiparticle Engineering and Entanglement Propagation in a Quantum Many-Body System, Nature (London) 511, 202 (2014).  
[46] C. Senko, J. Smith, P. Richerme, A. Lee, W. C. Campbell, and C. Monroe, Coherent Imaging Spectroscopy of a Quantum Many-Body Spin System, Science 345, 430 (2014).  
[47] D. A. Lidar, I. L. Chuang, and K. B. Whaley, Decoherence-Free Subspaces for Quantum Computation, Phys. Rev. Lett. 81, 2594 (1998).  
[48] D. Kielpinski, V. Meyer, M. A. Rowe, C. A. Sackett, W. M. Itano, C. Monroe, and D. J. Wineland, A Decoherence-Free Quantum Memory Using Trapped Ions, Science 291, 1013 (2001).  
[49] T. Grass, B. Julia-Diaz, M. Kus, and M. Lewenstein, Quantum Chaos in SU(3) Models with Trapped Ions, Phys. Rev. Lett. 111, 090404 (2013).  
[50] K. Kim, M.-S. Chang, R. Islam, S. Korenblit, L.-M. Duan, and C. Monroe, Entanglement and Tunable Spin-Spin Couplings between Trapped Ions Using Multiple Transverse Modes, Phys. Rev. Lett. 103, 120502 (2009).  
[51] D. F. V. James, Quantum Dynamics of Cold Trapped Ions with Application to Quantum Computation, Appl. Phys. B 66, 181 (1998).  
[52] D. Porras and J.I. Cirac, Effective Quantum Spin Systems with Trapped Ions, Phys. Rev. Lett. 92, 207901 (2004).  
[53] K. Molmer and A. Sorensen, Multiparticle Entanglement of Hot Trapped Ions, Phys. Rev. Lett. 82, 1835 (1999).  
[54] S. Olmschenk, K.C. Younge, D.L. Moehring, D.N. Matsukevich, P. Maunz, and C. Monroe, Manipulation and Detection of a Trapped  $\mathrm{Yb^{+}}$  Hyperfine Qubit, Phys. Rev. A 76, 052314 (2007).  
[55] D. Leibfried, E. Knill, S. Seidelin, J. Britton, R.B. Blakesstad, J. Chiaverini, D.B. Hume, W.M. Itano, J.D.

Jost, C. Langer, R. Ozeri, R. Reichle, and D. J. Wineland, Creation of a Six-Atom "Schroedinger Cat" State, Nature (London) 438, 639 (2005).  
[56] A. B. Klimov, R. Guzmán, J. C. Retamal, and C. Saavedra, *Qutrit Quantum Computer with Trapped Ions*, Phys. Rev. A 67, 062313 (2003).  
[57] N. Timoney, I. Baumgart, M. Johanning, A. F. Varon, M. B. Plenio, A. Retzker, and Ch. Wunderlich, Quantum Gates and Memory Using Microwave-Dressed States, Nature (London) 476, 185 (2011).  
[58] D. Collins, N. Gisin, N. Linden, S. Massar, and S. Popescu, Bell Inequalities for Arbitrarily High-Dimensional Systems, Phys. Rev. Lett. 88, 040404 (2002).  
[59] C. A. Sackett, D. Kielpinski, B.E. King, C. Langer, V. Meyer, C. J. Myatt, M. Rowe, Q. A. Turchette, W. M. Itano, D. J. Wineland, and C. Monroe, Experimental Entanglement of Four Particles, Nature (London) 404, 256 (2000).  
[60] K. R. Brown, A. W. Harrow, and I. L. Chuang, Arbitrarily Accurate Composite Pulse Sequences, Phys. Rev. A 70, 052318 (2004).  
[61] A. Albrecht, G. Koplovitz, A. Retzker, F. Jelezko, S. Yochelis, D. Porath, Y. Nevo, O. Shoseyov, Y. Paltiel, and M. B. Plenio, Self-Assembling Hybrid Diamond-Biological Quantum Devices, New J. Phys. 16, 093002 (2014).  
[62] J.-M. Cai, B. Naydenov, R. Pfeiffer, L.P. McGuinness, K.D. Jahnke, F. Jelezko, M.B. Plenio, and A. Retzker, Robust Dynamical Decoupling with Concatenated Continuous Driving, New J. Phys. 14, 113023 (2012).  
[63] M. J. Biercuk, H. Uys, A. P. VanDevender, N. Shiga, W. M. Itano, and J. J. Bollinger, Experimental Uhrig Dynamical Decoupling Using Trapped Ions, Phys. Rev. A 79, 062324 (2009).  
[64] T. Murashima, K. Hijii, K. Nomura, and T. Tonegawa, Phase Diagram of  $S = 1$  XXZ Chain with Next-Nearest-Neighbor Interaction, J. Phys. Soc. Jpn. 74, 1544 (2005).  
[65] I. Affleck, T. Kennedy, E. H. Lieb, and H. Tasaki, Valence Bond Ground States in Isotropic Quantum Antiferromagnets, Commun. Math. Phys. 115, 477 (1988).