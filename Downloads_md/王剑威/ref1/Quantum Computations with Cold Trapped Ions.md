# Quantum Computations with Cold Trapped Ions

J. I. Cirac and P. Zoller*

Institut für Theoretische Physik, Universität Innsbruck, Technikerstrasse 25, A-6020 Innsbruck, Austria (Received 30 November 1994)

A quantum computer can be implemented with cold ions confined in a linear trap and interacting with laser beams. Quantum gates involving any pair, triplet, or subset of ions can be realized by coupling the ions through the collective quantized motion. In this system decoherence is negligible, and the measurement (readout of the quantum register) can be carried out with a high efficiency.

PACS numbers: 89.80.+h, 03.65.Bz, 12.20.Fv, 32.80.Pj

A quantum computer (QC) obeys the laws of quantum mechanics, and its unique feature is that it can follow a superposition of computation paths simultaneously and produce a final state depending on the interference of these paths [1]. Recent results in quantum complexity theory and the development of algorithms indicate that quantum computers can solve some problems efficiently which are considered intractable on classical Turing machines. An example is the factorization of large composite numbers into primes [2], a problem which is the basis of the security of many classical key cryptosystems.

The task of designing a QC is equivalent to finding a physical implementation of quantum gates between quantum bits (or qubits), where a qubit refers to a two-state system  $\{|0\rangle, |1\rangle\}$  [3]. It has been shown [4] that any operation can be decomposed into controlled-NOT gates between two qubits and rotations on a single qubit, where a controlled-NOT is defined by  $\hat{C}_{12}: |\epsilon_1\rangle|\epsilon_2\rangle \rightarrow |\epsilon_1\rangle|\epsilon_1 \oplus \epsilon_2\rangle$  with  $\epsilon_{1,2} = 0,1$ , and  $\oplus$  denoting addition modulo 2. While there exist promising proposals to demonstrate the basic principle of gates in cavity QED [4], the experimental steps necessary to realize even a controlled-NOT gate indicate that extended networks would be exceedingly difficult to build. On the other hand, a number of interactions have been proposed for the construction of quantum computers [1,5], but so far no explicit physical system has been shown to serve as a realistic model. The main obstacle for a practical realization is the existence of decoherence processes due to the interaction of the system (the QC) with the environment [6].

In this Letter we show that a set of  $N$  cold ions interacting with laser light and moving in a linear trap [7] provides a realistic physical system to implement a quantum computer. The distinctive features of this system are (i) it allows the implementation of  $n$ -bit quantum gates between any set of (not necessarily neighboring) ions, (ii) decoherence can be made negligible during the whole computation, and (iii) the final readout can be performed with unit efficiency.

The basic elements of the computer (i.e., the qubits) are the ions themselves. The two states of the  $n$ th qubit are identified with two of the internal states of the corresponding ion; for example, a ground state  $|g\rangle_{n} \equiv |0\rangle_{n}$

and an excited state  $|e\rangle_{n} \equiv |1\rangle_{n}$ . The state of the QC is a macroscopic superposition

$$
| \psi \rangle = \sum_ {x = 0} ^ {2 ^ {N} - 1} c _ {x} | x \rangle \equiv \sum_ {\underline {{x}} = \{0, 1 \} ^ {N}} c _ {\underline {{x}}} | \underline {{x}} \rangle
$$

of quantum registers  $|x\rangle = |x_{N - 1}\rangle_{N - 1}\dots |x_0\rangle_0$  with  $x = \sum_{n = 0}^{N - 1}x_n2^n$  the binary decomposition of  $x$ . In this system independent manipulation of each individual qubit is accomplished by directing different laser beams to each of the ions. The quantum controlled-NOT, and, more generally, the (controlled) $^n$ -NOT gate between  $n$  arbitrary ions in the trap can be implemented by exciting the collective quantized motion of the ions with lasers [8]. The coupling of the motion of the ions is provided by the Coulomb repulsion which is much stronger than any other interaction for typical separations between the ions of a few optical wavelengths. Decoherence in an ion trap is due to spontaneous decay of the internal atomic states and damping of the motion of the ion. Application of stored ions in ultrahigh precision spectroscopy and time and frequency standards [9,10] shows that this decoherence time can be extremely long, much longer than the time required to perform many operations in a QC. Spontaneous emission is suppressed using metastable transitions [10]. Collisions with background atoms can be avoided at sufficiently low pressures for very long times, and other couplings that affect the moving charges can be made sufficiently small [9]. Furthermore, the final readout of the quantum register (state measurement of the individual qubits) at the end of the computation can be accomplished using the quantum jumps technique with unit efficiency [11].

The situation we have in mind is depicted in Fig. 1.  $N$  ions are confined in a linear trap, and interact with different laser beams [Fig. 1(a)] in standing wave configurations [12]. The confinement of the motion along  $X,Y$ , and  $Z$  directions can be described by an (anisotropic) harmonic potential of frequencies  $\nu_{x} \ll \nu_{y}, \nu_{z}$ . Nonharmonic traps can also be used leading to very similar results. The ions have been previously laser cooled in all three dimensions so that they undergo very small oscillations around the equilibrium position. In this case, the

![](images/1989a7d99609d49915ed0c8679c94b3dfcfba8c5cc43b5c1cbb1ea9e8df1bb96.jpg)

![](images/b110dc46c3047da8a624215bc4fef8953c3923812563e63ce3784f9ded3966ad.jpg)  
FIG. 1. (a)  $N$  ions in a linear trap interacting with  $N$  different laser beams; (b) atomic level scheme.

motion of the ions is described in terms of normal modes. Furthermore, we will assume that sideband cooling has left all the normal modes in their corresponding (quantum) ground states [13]. For this to be possible, one has to assume that the Lamb-Dicke limit (LDL) holds for all the modes [10]. This implies that their frequency is larger than the photon recoil frequency corresponding to the transition used for laser cooling. For example, for the  $S_{1/2} \rightarrow D_{5/2}$  dipole-forbidden transition of a barium ion, this requires  $\nu_{x,y,z} \gg 3 \mathrm{kHz}$ ; in typical situations  $\nu_{y,z} \gg \nu_x \sim 2\pi \times 50 \mathrm{kHz}$  [7]. The minimum frequency is that of the center-of-mass (CM) mode moving in the  $X$  direction, and coincides with  $\nu_x$ . The next frequency is  $\sqrt{3}\nu_x$ , and all the others are larger. A remarkable feature of this system is that the frequency spacing is independent of the number of ions  $N$  in the trap.

Figure 1(b) shows a typical level scheme for an alkaline earth ion, corresponding to an electric dipole-forbidden transition [10]. The two-level system that we choose as the qubit is marked with thicker lines  $(|g\rangle$  and  $|e_0\rangle$ ). The other levels do not disturb the computation process. On the contrary, some of them are needed for implementing quantum gates, as we will show below.

When a laser beam acts on one of the ions, it induces transitions between its (internal) ground and excited levels and can change the state of the collective normal modes. However, in the LDL and for sufficiently low intensities, the laser beam will only cause transitions that modify the state of one of the modes. For example, with a laser frequency so that the detuning equals minus the CM mode frequency  $(\delta_{n} = -\nu_{x})$ , one excites the CM mode exclusively. This is so since the frequencies of the different normal modes are well separated in the excitation spectrum. This fact allows one to control the interactions between the ions through the CM motion, by selecting appropriately the frequency of the lasers.

Let  $\tilde{H}_0$  be the Hamiltonian for the system in the absence of any laser field. Now, consider that the laser acting on the  $n$ th ion is turned on. Obviously, this laser will leave the internal state of all the other ions unaffected. The laser frequency is chosen such that  $\delta_{n} = -\nu_{x}$  and

the equilibrium position of the ion coincides with the node of the laser standing wave [12]. The Hamiltonian describing this situation in an interaction picture defined by the operator  $\exp (-i\hat{H}_0t)$  is  $(\hbar = 1)$

$$
\hat {H} _ {n, q} = \frac {\eta}{\sqrt {N}} \frac {\Omega}{2} \left[ | e _ {q} \rangle_ {n} \langle g | a e ^ {- i \phi} + | g \rangle_ {n} \langle e _ {q} | a ^ {\dagger} e ^ {i \phi} \right]. \tag {1}
$$

Here  $a^\dagger$  and  $a$  are the creation and annihilation operators of CM phonons, respectively,  $\Omega$  is the Rabi frequency,  $\phi$  is the laser phase, and  $\eta = [\hbar k_{\theta}^2 /(2M\nu_x)]^{1 / 2}$  is the LDL parameter  $[k_{\theta} = k\cos (\theta)$ , with  $k$  the laser wave vector and  $\theta$  the angle between the  $X$  axis and the direction of propagation of the laser]. The subscript  $q = 0,1$  refers to the transition excited by the laser, which depends on the laser polarization [see Fig. 1(b)]. Equation (1) can be derived as a generalization of the single ion Hamiltonian for the case of a linear trap [14]. Physically, the factor  $\sqrt{N}$  appears since the effective mass of the CM motion is  $NM$ , and the amplitude of the mode scales like  $1 / \sqrt{NM}$  (Mössbauer effect). A careful analysis shows that the model Hamiltonian (1) is valid for  $(\Omega /2\nu_{x})^{2}\eta^{2}\ll 1$ . Note that in the LDL  $\eta \ll 1$ . On the other hand, corrections to this Hamiltonian can be made arbitrarily small for sufficiently low laser intensities.

If the laser beam is on for a certain time  $t = k\pi /(\Omega \eta /\sqrt{N})$  (i.e., using a  $k\pi$  pulse), the evolution of the system will be described by the unitary operator

$$
\hat {U} _ {n} ^ {k, q} (\phi) = \exp \left[ - i k \frac {\pi}{2} \left(| e _ {q} \rangle_ {n} \langle g | a e ^ {- i \phi} + \mathrm {H . c .}\right) \right]. \tag {2}
$$

It is easy to prove that this transformation keeps the state  $|g\rangle_{n}|0\rangle$  unaltered, whereas

$$
\left| g \right\rangle_ {n} | 1 \rangle \longrightarrow \cos (k \pi / 2) \left| g \right\rangle_ {n} | 1 \rangle - i e ^ {i \phi} \sin (k \pi / 2) \left| e _ {q} \right\rangle_ {n} | 0 \rangle ,
$$

$$
\left| e \right\rangle_ {n} | 0 \rangle \longrightarrow \cos (k \pi / 2) \left| e _ {q} \right\rangle_ {n} | 0 \rangle - i e ^ {- i \phi} \sin (k \pi / 2) \left| g \right\rangle_ {n} | 1 \rangle ,
$$

where  $|0\rangle (|1\rangle)$  denotes a state of the CM mode with no (one) phonon.

Let us now show how a two-bit gate can be performed using this interaction. We consider the following three-step process [see Fig. 1(b)]. (i) A  $\pi$  laser pulse with polarization  $q = 0$  and  $\phi = 0$  excites the  $m$ th ion. The evolution corresponding to this step is given by  $\hat{U}_m^{1,0} \equiv \hat{U}_m^{1,0}(0)$ . (ii) The laser directed on the  $n$ th ion is then turned on for a time of a  $2\pi$  pulse with polarization  $q = 1$  and  $\phi = 0$ . The corresponding evolution operator  $\hat{U}_n^{2,1}$  changes the sign of the state  $|g\rangle_n|1\rangle$  (without affecting the others) via a rotation through the auxiliary state  $|e_1\rangle_n|0\rangle$ . (iii) Same as (i). Thus the unitary operation for the whole process is  $\hat{U}_{m,n} \equiv \hat{U}_m^{1,0}\hat{U}_n^{2,1}\hat{U}_m^{1,0}$  which is represented diagrammatically as follows:

$$
\begin{array}{c c c c c c} & \hat {U} _ {m} ^ {1, 0} & & \hat {U} _ {n} ^ {2, 1} & & \hat {U} _ {m} ^ {1, 0} \\ | g \rangle_ {m} | g \rangle_ {n} | 0 \rangle & \longrightarrow & | g \rangle_ {m} | g \rangle_ {n} | 0 \rangle & \longrightarrow & | g \rangle_ {m} | g \rangle_ {n} | 0 \rangle & \longrightarrow & | g \rangle_ {m} | g \rangle_ {n} | 0 \rangle , \\ | g \rangle_ {m} | e _ {0} \rangle_ {n} | 0 \rangle & \longrightarrow & | g \rangle_ {m} | e _ {0} \rangle_ {n} | 0 \rangle & \longrightarrow & | g \rangle_ {m} | e _ {0} \rangle_ {n} | 0 \rangle & \longrightarrow & | g \rangle_ {m} | e _ {0} \rangle_ {n} | 0 \rangle , \\ | e _ {0} \rangle_ {m} | g \rangle_ {n} | 0 \rangle & \longrightarrow & - i | g \rangle_ {m} | g \rangle_ {n} | 1 \rangle & \longrightarrow & i | g \rangle_ {m} | g \rangle_ {n} | 1 \rangle & \longrightarrow & | e _ {0} \rangle_ {m} | g \rangle_ {n} | 0 \rangle , \\ | e _ {0} \rangle_ {m} | e _ {0} \rangle_ {n} | 0 \rangle & \longrightarrow & - i | g \rangle_ {m} | e _ {0} \rangle_ {n} | 1 \rangle & \longrightarrow & - i | g \rangle_ {m} | e _ {0} \rangle_ {n} | 1 \rangle & \longrightarrow & - | e _ {0} \rangle_ {m} | e _ {0} \rangle_ {n} | 0 \rangle . \end{array} \tag {3}
$$

The effect of this interaction is to change the sign of the state only when both ions are initially excited. Note that the state of the CM mode is restored to the vacuum state  $|0\rangle$  after the process. Equation (3) is equivalent to a controlled-NOT gate. To show this, let us denote by  $|\pm \rangle = (|g\rangle \pm |e_0\rangle) / \sqrt{2}$ . Then, this procedure can be summarized as  $|g\rangle_m|\pm \rangle_n\rightarrow |g\rangle_m|\pm \rangle_n$  and  $|e_0\rangle_m|\pm \rangle_n\rightarrow |e_0\rangle_m|\mp \rangle_n$ . With an appropriate individual (one-bit) rotation applied to the nth ion this procedure then yields the controlled-NOT. These individual rotations acting on a single ion (without modifying the CM motion) can be performed using a laser frequency on resonance with the internal transition ( $\delta_{n} = 0$ ), polarization  $q = 0$ , and with the equilibrium position of the ion coinciding with the antinode of the laser standing wave. In this case, the Hamiltonian is

$$
\hat {H} _ {n} = (\Omega / 2) \big [ | e _ {0} \rangle_ {n} \langle g | e ^ {- i \phi} + | g \rangle_ {n} \langle e _ {0} | e ^ {i \phi} \big ]. \qquad (4)
$$

For an interaction time  $t = k\pi /\Omega$  (i.e., using a  $k\pi$  pulse), this process is described by the following unitary evolution operator:

$$
\hat {V} _ {n} ^ {k} (\phi) = \exp \left[ - i k \frac {\pi}{2} \left(| e _ {0} \rangle_ {n} \langle g | e ^ {- i \phi} + \mathrm {H . c .}\right) \right], \tag {5}
$$

so that

$$
| g \rangle_ {n} \longrightarrow \cos (k \pi / 2) | g \rangle_ {n} - i e ^ {i \phi} \sin (k \pi / 2) | e _ {0} \rangle_ {n},
$$

$$
\left| e _ {0} \right\rangle_ {n} \longrightarrow \cos (k \pi / 2) \left| e _ {0} \right\rangle_ {n} - i e ^ {- i \phi} \sin (k \pi / 2) \left| g \right\rangle_ {n}.
$$

Thus the complete controlled-NOT gate for the states  $|\pmb{\epsilon}_m\rangle |\pmb{\epsilon}_n\rangle$ $(\pmb{\epsilon}_{m,n} = g,e_0)$  is given by  $\hat{C}_{mn} = \hat{V}_n^{1 / 2}(\frac{\pi}{2})\hat{U}_{m,n}\hat{V}_n^{1 / 2}(-\frac{\pi}{2})$  [15].

Nonlocal three-bit gates can be implemented in a similar way between ions  $n$ ,  $m$ , and  $l$ . The process takes place in five steps: (j) Same as (i); (jj) same as (ii), but with a  $\pi$  pulse; (jjj) same as step (ii) but with ion  $l$ ; (jv) same as (jj); (v) same as (j). The corresponding unitary operation for this process is  $\hat{U}_m^{1,0}\hat{U}_n^{1,1}\hat{U}_l^{2,1}\hat{U}_n^{1,1}\hat{U}_m^{1,0}$ . This procedure only changes the sign of the state if all three ions were initially excited. One can easily generalize this procedure to the case of many ions. For example, a (control) $^p$ -NOT gate acting on ions  $n_1,n_2,\ldots ,n_q$  corresponds to the unitary evolution

$$
\hat {V} _ {p} ^ {\frac {1}{2}} \left(\frac {\pi}{2}\right) \hat {U} _ {n _ {1}} ^ {1, 0} \left[ \prod_ {j = 2} ^ {p - 1} \hat {U} _ {n _ {j}} ^ {1, 1} \right] \hat {U} _ {n _ {p}} ^ {2, 1} \left[ \prod_ {j = p - 1} ^ {2} \hat {U} _ {n _ {j}} ^ {1, 1} \right] \hat {U} _ {n _ {1}} ^ {1, 0} \hat {V} _ {p} ^ {\frac {1}{2}} \left(- \frac {\pi}{2}\right).
$$

Using similar ideas with different laser phases and interaction times one can implement other  $n$ -bit gates [8].

In summary, the two key elements behind the above implementation of quantum gates are as follows. First, nonlocal entanglement between individual qubits is achieved by transferring the internal atomic coherence to and from the CM motion shared by all the ions  $(\hat{U}_n^{k = 1,q = 0})$ . Second, as an intermediate step we "hide atomic amplitudes" corresponding to the qubits in a third internal atomic level  $|e_1\rangle$ $(\hat{U}_n^{k = 1,q = 1})$ , and induce  $2\pi$  rotations via this state to selectively change the sign of atomic amplitudes  $(\hat{U}_n^{k = 2,q = 1})$ . We note that no population is left in these auxiliary atomic and CM levels after the complete gate operation. Any population left in these states is an indication of an imprecise realization. This could be used to implement an error detection scheme by probing the population of these intermediate states, for example, with a laser inducing fluorescence after each gate operation [16].

The core of Shor's factorization scheme [2] is the high efficiency of a QC to find the period  $r$  of a given function by doing a discrete Fourier transform (FT) on a periodic state vector of the form  $|\Psi\rangle \propto \sum_{l} |lr + k\rangle$ . Here  $k$  is an integer number and  $l = 0, \ldots, [(2^N - k)/r]$  with  $[ \ldots ]$  the integer part. The FT is defined by the operation

$$
\hat {F T} | x \rangle = 1 / \sqrt {2 ^ {N}} \sum_ {y} e ^ {2 \pi i x y / 2 ^ {N}} | y \rangle
$$

on the quantum registers. This FT can be decomposed into a sequence of one- and two-bit operations [17,18]. The probability to measure the state  $|y\rangle$  of the quantum register is then  $P_{y} = |\langle y|\hat{F T} |\Psi \rangle |^{2}$ . Shor has shown that this measurement gives with high probability an outcome that allows one to calculate  $r$ .

To show the capabilities of an ion trap as a QC, and to analyze how experimental uncertainties may affect the final results [6], we have simulated the above scheme on a (digital) computer. Figure 2 shows a comparison

![](images/611053c30e01e9d1e3066d9a72eb0e95a0ffc566f1ddb7379353badf43c6df66.jpg)  
FIG. 2. Probability distribution  $P_{y}$  after FT (see text): (a) exact, (b) ion trap simulation, (c) simulation with  $5\%$  errors.

between the exact results [Fig. 2(a)] for  $P_{y}$  and the ion trap simulation [Figs. 2(b) and 2(c)] for a state with  $k = 4$ ,  $r = 7$ , and eight ions. The existence of peaks in this spectrum (separated by  $\simeq 2^{N} / r = 256 / 7$ ) allows one to determine the period  $r$ . Similar to Ref. [17] one can show that this probability distribution  $P_{y}$  can be obtained from the physical process corresponding to the sequence of operations  $\hat{V}_{0}\hat{W}_{0}\hat{W}_{1}\hat{V}_{1}\dots \hat{W}_{N - 2}\hat{V}_{N - 1}$ . Here  $\hat{W}_n = \hat{W}_n^{N - 1}\hat{W}_n^{N - 2}\dots \hat{W}_n^{n + 1}$  is a sequence of two-bit operations  $\hat{W}_n^m = \hat{U}_m^{1,0}[\pi (1 - 2^{(n - m)})]\hat{U}_n^{1,1}[\pi (1 - 2^{(n - m)})]\hat{U}_n^{1,1}\hat{U}_m^{1,0}$  ( $n < m$ ), and  $\hat{V}_n\equiv \hat{V}_n^{1 / 2}(-\pi /2)$  is a one-ion rotation [see (2) and (5)]. The specific form of the pulse sequence can be directly deduced from the definition of the operators  $W$ , and requires two- and one-bit gates between the ions. The simulation has been performed with the full Hamiltonian (to all orders in the Lamb-Dicke expansion) for  $N = 8\mathrm{Ba}^{+}$ ions in a trap with  $\nu_{x} = 2\pi \times 50\mathrm{kHz}$ . The Rabi frequencies have been chosen as follows:  $\Omega = 2\pi \times 1.5\mathrm{kHz}$  for resonant excitations (at the antinode) and  $\Omega = 2\pi \times 15\mathrm{kHz}$  for off-resonant excitations (at the node). The rest of the parameters correspond to those of the  $\mathrm{Ba}^{+}$ ions. As shown in Fig. 2(b), with these realistic parameters, the result is nearly indistinguishable from the exact one. From our numerical simulations we could see that this result can even be improved by increasing the trap frequency (or decreasing the Rabi frequencies), in agreement with a perturbation theory analysis for the terms neglected in (1) and (4). Note that the total time required for the whole operation is about  $35~\mathrm{ms}$ , much smaller than the decoherence time due to spontaneous emission (the lifetime of the metastable state of  $\mathrm{Ba}^{+}$ is about  $45~\mathrm{s}$ , so that the decoherence time is  $\simeq 6~\mathrm{s}$ ). To analyze how experimental uncertainties affect the final results we have carried out numerical simulations assuming a  $5\%$  error in all the interaction times involved in the operation,  $1\mathrm{kHz}$  of error in all the laser detunings, and a  $5\% \pi /2$  error in all the angles in the problem (situation of the standing waves with respect to the position of the ions, and phases of the lasers). Figure 2(c) shows that even with all these errors the peaks in the distribution are still maintained, and the system of ions is remarkably robust to perform quantum computations.

Apart from one- and two-bit operations, (5) and (2), one can also prepare the most general entangled state of  $N$  ions [9,19]. For example, the maximal entangled state

$$
\begin{array}{l} | \Psi \rangle = 1 / \sqrt {2} (| - \rangle_ {N - 1} \dots | - \rangle_ {1} \\ \times | - \rangle_ {0} - | + \rangle_ {N - 1} \dots | + \rangle_ {1} | + \rangle_ {0}) \\ \end{array}
$$

can be obtained starting from  $|g\rangle_{N - 1}|g\rangle_{N - 2}\dots |g\rangle_0$  (as obtained after sideband cooling), by using the operations  $\hat{V}_0\hat{U}_{N - 1,0}\dots \hat{U}_{2,0}\hat{U}_{1,0}\hat{V}_{N - 1}\dots \hat{V}_1\hat{V}_0$  [18].

In summary, linear ion traps are well suited to implement a QC. This is due to the negligible decoherence in these systems [9], as well as the possibility to manipulate the internal and CM degrees of freedom with external fields,

and to perform efficient state measurements. We have shown how to implement  $n$ -bit gates between  $n$  arbitrary ions, and have illustrated the performance of such a system with a numerical simulation. We believe that the present system provides a realistic implementation of a QC which can be built with present or planned technology.

We thank R. Blatt, A. Ekert, M. Lewenstein, and D. Wineland for helpful comments. This work was supported by the Austrian Science Foundation.

*Permanent address: Departamento de Física, Universidad de Castilla-La Mancha, 13071 Ciudad Real, Spain.  
[1] For a review, see A. Ekert, in Proc. ICAP '94. edited by S. Smith, C. Wieman, and D. Wineland (to be published).  
[2] P. W. Shor, in Proceedings of the 35th Annual Symposium on the Foundations of Computer Science, Los Alamitos, CA (IEEE Computer Society Press, New York, 1994), p. 124.  
[3] D. Deutsch, Proc. R. Soc. London A 425, 73 (1989).  
[4] T. Sleator and H. Weinfurter, Phys. Rev. Lett. 74, 4087 (1995).  
[5] K. Obermayer, W.G. Teich, and G. Mahler, Phys. Rev. B 37, 8096 (1988); S. Lloyd, Science 261, 1569 (1993); D.P. Di Vincenzo, Phys. Rev. A 50, 1015 (1995).  
[6] R. Landauer, Proc. R. Soc. London A (to be published); W.G. Unruh (to be published).  
[7] M.G. Raizen et al., Phys. Rev. A 45, 6493 (1992); H. Walther, Adv. At. Mol. Opt. Phys. 32, 379 (1994).  
[8] Although a (controlled) $^n$ -NOT can be decomposed into a finite number of controlled-NOT gates plus one-bit rotations, this may require many operations. [H. Weinfurter (private communication)] Thus a direct implementation of the (controlled) $^n$ -NOT gate may be interesting from a practical point of view.  
[9] D.J. Wineland et al., Phys. Rev. A 50, 67 (1994); 46, R6797 (1992).  
[10] R. Blatt, in Proc. ICAP '94, Ref. [1].  
[11] W. Nagourney et al., Phys. Rev. Lett. 56, 2797 (1986); J.C. Bergquist et al., ibid. 56, 1699 (1986); Th. Sauter et al., ibid. 56, 1696 (1986).  
[12] A similar scheme can be used with traveling wave configurations. However, the standing wave minimizes the effects of unwanted transitions; see Ref. [14].  
[13] F. Diedrich et al., Phys. Rev. Lett. 62, 403 (1989); here only the CM has to be cooled to the ground state.  
[14] J.I. Cirac et al., Phys. Rev. Lett. 70, 762 (1993).  
[15] The two-bit gate (3) (instead of the controlled-NOT) together with single bit rotations are sufficient to generate arbitrary unitary operations.  
[16] Nonobservation of fluorescence corresponds to a projection of the state vector on  $|g\rangle$ ,  $|e_0\rangle$ . This might be the basis of a partial error correction scheme.  
[17] D. Coppersmith, IBM Research Report No. RC19642, 1994.  
[18] FT and the preparation of general entangled states could be performed more efficiently using general  $n$ -bit gates (instead of a sequence of two-bit gates).  
[19] D.M. Greenberger et al., Am. J. Phys. 58, 1131 (1990); see also N.D. Mermin, ibid. 58, 8 (1990).