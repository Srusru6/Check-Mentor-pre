# Quantum State Transfer and Entanglement Distribution among Distant Nodes in a Quantum Network

J. I. Cirac, $^{1,2}$  P. Zoller, $^{1,2}$  H. J. Kimble, $^{1,3}$  and H. Mabuchi $^{1,3}$

$^{1}$ Institute for Theoretical Physics, University of California at Santa Barbara, Santa Barbara, California 93106-4030

$^{2}$ Institut für Theoretische Physik, Universität Innsbruck, Technikerstrasse 25, A-6020 Innsbruck, Austria

$^{3}$ Norman Bridge Laboratory of Physics 12-33, California Institute of Technology, Pasadena, California 91125

(Received 12 November 1996)

We propose a scheme to utilize photons for ideal quantum transmission between atoms located at spatially separated nodes of a quantum network. The transmission protocol employs special laser pulses that excite an atom inside an optical cavity at the sending node so that its state is mapped into a time-symmetric photon wave packet that will enter a cavity at the receiving node and be absorbed by an atom there with unit probability. Implementation of our scheme would enable reliable transfer or sharing of entanglement among spatially distant atoms. [S0031-9007(97)02983-9]

PACS numbers: 89.70.+c, 03.65.Bz, 42.50.Lc

We consider a quantum network consisting of spatially separated nodes connected by quantum communication channels. Each node is a quantum system that stores quantum information in quantum bits and processes this information locally using quantum gates [1]. Exchange of information between the nodes of the network is accomplished via quantum channels. A physical implementation of such a network could consist, e.g., of clusters of trapped atoms or ions representing the nodes, with optical fibers or similar photon "conducts" providing the quantum channels. Atoms and ions are particularly well suited for storing qubits in long-lived internal states, and recently proposed schemes for performing quantum gates between trapped atoms or ions provide an attractive method for local processing within an atom/ion node [2-4]. On the other hand, photons clearly represent the best qubit carrier for fast and reliable communication over long distances [5,6], since fast and internal-state-preserving transportation of atoms or ions seems to be technically intractable.

To date, no process has actually been identified for using photons (or any other means) to achieve efficient quantum transmission between spatially distant atoms [7]. In this Letter we outline a scheme to implement this basic building block of communication in a distributed quantum network. Our scheme allows quantum transmission with (in principle) unit efficiency between distant atoms 1 and 2 (see Fig. 1). The possibility of combining local quantum processing with quantum transmission between the nodes of the network opens the possibility for a variety of novel applications ranging from entangled-state cryptography [8], teleportation [9], and purification [10], and is interesting from the perspective of distributed quantum computation [11].

The basic idea of our scheme is to utilize strong coupling between a high- $Q$  optical cavity and the atoms [5] forming a given node of the quantum network. By applying laser beams, one first transfers the internal state of an atom at the first node to the optical state of the cavity mode. The generated photons leak out of the cavity, propagate

as a wave packet along the transmission line, and enter an optical cavity at the second node. Finally, the optical state of the second cavity is transferred to the internal state of an atom. Multiple-qubit transmissions can be achieved by sequentially addressing pairs of atoms (one at each node), as entanglements between arbitrarily located atoms are preserved by the state-mapping process.

The distinguishing feature of our protocol is that by controlling the atom-cavity interaction, one can absolutely avoid the reflection of the wave packets from the second cavity, effectively switching off the dominant loss channel that would be responsible for decoherence in the communication process. For a physical picture of how this can be accomplished, let us consider that a photon leaks out of an optical cavity and propagates away as a wave packet. Imagine that we were able to "time reverse" this wave packet and send it back into the cavity; then this would restore the original (unknown) superposition state of the atom, provided we would also reverse the timing of the laser pulses. If, on the other hand, we are able to drive the atom in a transmitting cavity in such a way that the outgoing pulse were already symmetric in time, the wave packet entering a receiving cavity would "mimic" this time reversed process, thus "restoring" the state of the first atom in the second one.

The simplest possible configuration of quantum transmission between two nodes consists of two atoms 1 and 2 which are strongly coupled to their respective cavity modes (see Fig. 1). The Hamiltonian describing the interaction of each atom with the corresponding cavity mode

![](images/54329023021c0c4c9349ff3f633fb9f5050bda4c1263014cf20cb7ed1062ef53.jpg)  
FIG. 1. Schematic representation of unidirectional quantum transmission between two atoms in optical cavities connected by a quantized transmission line (see text for explanation).

$$
\text {i s} (\hbar = 1)
$$

$$
\begin{array}{l} \hat {H} _ {i} = \omega_ {c} \hat {a} _ {i} ^ {\dagger} \hat {a} _ {i} + \omega_ {0} | r \rangle_ {i i} \langle r | + g (| r \rangle_ {i i} \langle g | \hat {a} _ {i} + \mathrm {H . c .}) + \frac {1}{2} \\ \times \Omega_ {i} (t) \left[ e ^ {- i \left[ \omega_ {L} t + \phi_ {i} (t) \right]} | r \rangle_ {i i} \langle e | + H. c. \right] \quad (i = 1, 2). \tag {1} \\ \end{array}
$$

Here,  $\hat{a}_i$  is the destruction operator for cavity mode  $i$  with frequency  $\omega_c$ ,  $|g\rangle$ ,  $|r\rangle$ , and  $|e\rangle$  form a three-level system of excitation frequency  $\omega_0$  (Fig. 1), and the qubit is stored in a superposition of the two degenerate ground states. The states  $|e\rangle$  and  $|g\rangle$  are coupled by a Raman transition [3,4,12], where a laser of frequency  $\omega_L$  excites the atom from  $|e\rangle$  to  $|r\rangle$  with a time-dependent Rabi frequency  $\Omega_i(t)$  and phase  $\phi_i(t)$ , followed by a transition  $|r\rangle \rightarrow |e\rangle$  which is accompanied by emission of a photon into the corresponding cavity mode, with coupling constant  $g$ . In order to suppress spontaneous emission from the excited state during the Raman process, we assume that the laser is strongly detuned from the atomic transition  $|\Delta |\gg \Omega_{1,2}(t), g,\dot{|\phi_{1,2}|}$  (with  $\Delta = \omega_L - \omega_0$ ). In such a case, one can eliminate adiabatically the excited states  $|r\rangle_{i}$ . The new Hamiltonian for the dynamics of the two ground states becomes, in a rotating frame for the cavity modes at the laser frequency,

$$
\begin{array}{l} \hat {H} _ {i} = - \delta \hat {a} _ {i} ^ {\dagger} \hat {a} _ {i} + \frac {g ^ {2}}{\Delta} \hat {a} _ {i} ^ {\dagger} \hat {a} _ {i} | g \rangle_ {i i} \langle g | + \delta \omega_ {i} (t) | e \rangle_ {i i} \langle e | \\ - i g _ {i} (t) \left[ e ^ {i \phi_ {i} (t)} | e \rangle_ {i i} \langle g | a _ {i} - \mathrm {H . c .} \right] \quad (i = 1, 2). \tag {2} \\ \end{array}
$$

The first term involves the Raman detuning  $\delta = \omega_{L} - \omega_{c}$ . The next two terms are ac-Stark shifts of the ground states  $|g\rangle$  and  $|e\rangle$  due to the cavity mode and laser field, respectively, with  $\delta \omega_{i}(t) = \Omega_{i}(t)^{2} / (4\Delta)$ . The last term is the familiar Jaynes-Cummings interaction, with an effective coupling constant  $g_{i}(t) = g\Omega_{i}(t) / (2\Delta)$  [13]. The notation  $|e\rangle$  as "excited" and  $|g\rangle$  as "ground" state is motivated by this analogy.

Our goal is to select the time-dependent Rabi frequencies and laser phases [14] to accomplish the ideal quantum transmission

$$
\begin{array}{l} \left(c _ {g} | g \rangle_ {1} + c _ {e} | e \rangle_ {1}\right) | g \rangle_ {2} \otimes | 0 \rangle_ {1} | 0 \rangle_ {2} | \mathrm {v a c} \rangle \\ \rightarrow | g \rangle_ {1} \left(c _ {g} | g \rangle_ {2} + c _ {e} | e \rangle_ {2}\right) \otimes | 0 \rangle_ {1} | 0 \rangle_ {2} | \text {v a c} \rangle , \tag {3} \\ \end{array}
$$

where  $c_{g,e}$  are complex numbers; in general, they have to be replaced by unnormalized states of other "spectator" atoms in the network. In (3),  $|0\rangle_{i}$  and  $|\mathrm{vac}\rangle$  represent the vacuum state of the cavity modes and the free electromagnetic modes connecting the cavities. Transmission will occur by photon exchange via these modes.

In a quantum stochastic description employing the input-output formalism the cavity mode operators obey the quantum Langevin equations [15]:

$$
\frac {d \hat {a} _ {i}}{d t} = - i [ \hat {a} _ {i}, \hat {H} _ {i} (t) ] - \kappa \hat {a} _ {i} - \sqrt {2 \kappa} \hat {a} _ {\text {i n}} ^ {(i)} (t) \quad (i = 1, 2). \tag {4}
$$

The first term on the right-hand side (RHS) of this equation gives the systematic evolution due to the interaction

with the atom, while the last two terms correspond to photon transmission through the mirror with loss rate  $\kappa$ , and (white) quantum noise of the vacuum field incident on the cavity  $i$ , respectively. The output of each cavity is given by the equation [15]

$$
\hat {a} _ {\text {o u t}} ^ {(i)} (t) = \hat {a} _ {\text {i n}} ^ {(i)} (t) + \sqrt {2 \kappa} \hat {a} _ {i} (t), \tag {5}
$$

which expresses the outgoing field at the mirror as a sum of the incident field plus the field radiated from the cavity. The output field of the first cavity constitutes the input for the second cavity with an appropriate time delay, i.e.,  $\hat{a}_{\mathrm{in}}^{(2)}(t) = \hat{a}_{\mathrm{out}}^{(1)}(t - \tau)$ , where  $\tau$  is a constant related to retardation in the propagation between the mirrors. The output field of the second cavity is, therefore,

$$
\hat {a} _ {\text {o u t}} ^ {(2)} (t) = \hat {a} _ {\text {i n}} ^ {(1)} (t - \tau) + \sqrt {2 \kappa} [ \hat {a} _ {1} (t - \tau) + \hat {a} _ {2} (t) ]. \tag {6}
$$

Introducing this relation in Eq. (4) we obtain

$$
\frac {d \hat {a} _ {1}}{d t} = - i [ \hat {a} _ {1}, \hat {H} _ {1} (t) ] - \kappa \hat {a} _ {1} - \sqrt {2 \kappa} \hat {a} _ {\text {i n}} ^ {(1)} (t), \tag {7a}
$$

$$
\begin{array}{l} \frac {d \hat {a} _ {2}}{d t} = - i [ \hat {a} _ {2}, \hat {H} _ {2} (t) ] - \kappa \hat {a} _ {2} - 2 \kappa \hat {a} _ {1} (t - \tau) \\ - \sqrt {2 \kappa} \hat {a} _ {\text {i n}} ^ {(1)} (t - \tau). \tag {7b} \\ \end{array}
$$

Note that the first equation is decoupled from the second one; i.e., we consider here only a unidirectional coupling between the cavities (see Fig. 1) [16]. The present model is a particular example of a cascaded quantum system and can be described within the formalism developed by Gardiner and Carmichael [17,18]. We can eliminate the time delay  $\tau$  in these equations by defining "time delayed" operators for the first system (atom + cavity), e.g.,  $\tilde{a}(t) \equiv \hat{a}(t - \tau)$ , etc.; in a similar way we redefine the Rabi frequency  $\tilde{\Omega}_1(t) = \Omega_1(t - \tau)$ , and phase  $\tilde{\phi}_1(t) = \phi_1(t - \tau)$ . In the following we will assume that we have performed these transformations, and for simplicity of notation we will omit the tilde. This amounts to setting  $\tau \rightarrow 0$  in all these equations. Equations (7a) and (7b) have to be solved with the corresponding equations for the atomic operators and with the condition that the field incident on the first cavity is in the vacuum state, i.e.,  $\hat{a}_{\mathrm{in}}^{(1)}(t) |\Psi_0\rangle = 0 \forall t$ .

In the present context, it is convenient to adopt the language of quantum trajectories [18,19]. Let us consider a fictitious experiment where the output field of the second cavity is continuously monitored by a photodetector (see Fig. 1). The evolution of the quantum system under continuous observation, conditional to observing a particular trajectory of counts, can be described by a pure state wave function  $|\Psi_c(t)\rangle$  in the system Hilbert space (where the radiation modes outside the cavity have been eliminated). During the time intervals when no count is detected, this wave function evolves according to a Schrödinger equation with the non-Hermitian effective Hamiltonian

$$
\hat {H} _ {\text {e f f}} (t) = \hat {H} _ {1} (t) + \hat {H} _ {2} (t) - i \kappa \left(\hat {a} _ {1} ^ {\dagger} \hat {a} _ {1} + \hat {a} _ {2} ^ {\dagger} \hat {a} _ {2} + 2 \hat {a} _ {2} ^ {\dagger} \hat {a} _ {1}\right). \tag {8}
$$

The detection of a count at time  $t_r$  is associated with a quantum jump according to  $|\Psi_c(t_r + dt)\rangle \propto \hat{c} |\Psi_c(t_r)\rangle$ , where  $\hat{c} = \hat{a}_1 + \hat{a}_2$  [17,19]. The probability density for a jump (detector click) to occur during the time interval from  $t$  to  $t + dt$  is  $\langle \Psi_c(t)|\hat{c}^\dagger \hat{c} |\Psi_c(t)\rangle dt$  [17,19].

We wish to design the laser pulses in both cavities in such a way that ideal quantum transmission condition (3) is satisfied. A necessary condition for the time evolution is

that a quantum jump (detector click; see Fig. 1) never occurs, i.e.,  $\hat{c} |\Psi_c(t)\rangle = 0\forall t$ , and thus the effective Hamiltonian will become a Hermitian operator. In other words, the system will remain in a dark state of the cascaded quantum system. Physically, this means that the wave packet is not reflected from the second cavity. We expand the state of the system as

$$
\left| \Psi_ {c} (t) \right\rangle = c _ {g} | g g \rangle | 0 0 \rangle + c _ {e} \left[ \alpha_ {1} (t) e ^ {- i \phi_ {1} (t)} | e g \rangle | 0 0 \rangle + \alpha_ {2} (t) e ^ {- i \phi_ {2} (t)} | g e \rangle | 0 0 \rangle + \beta_ {1} (t) | g g \rangle | 1 0 \rangle + \beta_ {2} (t) | g g \rangle | 0 1 \rangle \right]. \tag {9}
$$

Ideal quantum transmission (3) will occur for

$$
\alpha_ {1} (- \infty) = \alpha_ {2} (+ \infty) = 1, \quad \phi_ {1} (- \infty) = \phi_ {2} (+ \infty) = 0. \tag {10}
$$

The first term on the RHS of (9) does not change under the time evolution generated by  $H_{\mathrm{eff}}$ . Defining symmetric and antisymmetric coefficients  $\beta_{1,2} = (\beta_s + \beta_a) / \sqrt{2}$ , we find the following evolution equations

$$
\dot {\alpha} _ {1} (t) = g _ {1} (t) \beta_ {a} (t) / \sqrt {2}, \tag {11a}
$$

$$
\dot {\alpha} _ {2} (t) = - g _ {2} (t) \beta_ {a} (t) / \sqrt {2}, \tag {11b}
$$

$$
\dot {\beta} _ {a} (t) = - g _ {1} (t) \alpha_ {1} (t) / \sqrt {2} + g _ {2} (t) \alpha_ {2} (t) / \sqrt {2}, \tag {11c}
$$

where we have chosen the laser frequencies  $\omega_{L} + \dot{\phi}_{1,2}(t)$  so that  $\delta = g^{2} / \Delta$  and

$$
\dot {\phi} _ {1, 2} (t) = \delta \omega_ {i} (t) \tag {12}
$$

in order to compensate the ac-Stark shifts; thus Eqs. (11a), (11b), and (11c) are decoupled from the phases. The dark state condition implies  $\beta_{s}(t) = 0$ , and therefore

$$
\dot {\beta} _ {s} (t) = g _ {1} (t) \alpha_ {1} (t) / \sqrt {2} + g _ {2} (t) \alpha_ {2} (t) / \sqrt {2} + \kappa \beta_ {a} (t) \equiv 0, \tag {13}
$$

as well as the normalization condition

$$
\left| \alpha_ {1} (t) \right| ^ {2} + \left| \alpha_ {2} (t) \right| ^ {2} + \left| \beta_ {a} (t) \right| ^ {2} = 1. \tag {14}
$$

We note that the coefficients  $\alpha_{1,2}(t)$  and  $\beta_s(t)$  are real.

The mathematical problem is now to find pulse shapes  $\Omega_{1,2}(t) \propto g_{1,2}(t)$  such that the conditions (10), (11a), (11b), (11c), and (13) are fulfilled. In general this is a difficult problem, as imposing conditions (10) and (13) on the solutions of the differential equations [(11a), (11b), and (11c)] give functional relations for the pulse shape whose solution are not obvious. We shall construct a class of solutions guided by the physical expectation that the time evolution in the second cavity should reverse the time evolution in the first one. Thus, we look for solutions satisfying the symmetric pulse condition

$$
g _ {2} (t) = g _ {1} (- t) \quad (\forall t). \tag {15}
$$

This implies  $\alpha_{1}(t) = \alpha_{2}(-t)$ , and  $\beta_{a}(t) = \beta_{a}(-t)$ . The latter relation leads to a symmetric shape of the photon wave packet propagating between the cavities.

Suppose that we specify a pulse shape  $\Omega_1(t) \propto g_1(t)$  for the second half of the pulse in the first cavity ( $t \geq 0$ ) [20].

We wish to determine the first half  $\Omega_1(-t) \propto g_1(-t)$  (for  $t > 0$ ), such that the conditions for ideal transmission (3) are satisfied. From (13) and (10) we have

$$
g _ {1} (- t) = - \frac {\sqrt {2} \kappa \beta_ {a} (t) + g _ {1} (t) \alpha_ {1} (t)}{\alpha_ {2} (t)} \quad (t > 0). \tag {16}
$$

Thus, the pulse shape is completely determined provided we know the system evolution for  $t \geq 0$ . However, a difficulty arises when we try to find this evolution, since it depends on the yet unknown  $g_{2}(t) = g_{1}(-t)$  for  $t > 0$  [see Eqs. (11a), (11b), and (11c)]. In order to circumvent this problem, we use (13) to eliminate this dependence in Eqs. (11a) and (11c). This gives

$$
\dot {\alpha} _ {1} (t) = g _ {1} (t) \beta_ {a} (t) / \sqrt {2}, \tag {17a}
$$

$$
\dot {\beta} _ {a} (t) = - \kappa \beta_ {a} (t) - \sqrt {2} g _ {1} (t) \alpha_ {1} (t) \tag {17b}
$$

for  $t \geq 0$ . These equations have to be integrated with the initial conditions

$$
\alpha_ {1} (0) = \left[ \frac {2 \kappa^ {2}}{g _ {1} (0) ^ {2} + \kappa^ {2}} \right] ^ {\frac {1}{2}}, \tag {18a}
$$

$$
\beta_ {a} (0) = \left[ 1 - 2 \alpha_ {1} (0) ^ {2} \right] ^ {\frac {1}{2}}, \tag {18b}
$$

which follow immediately from  $\alpha_{1}(0) = \alpha_{2}(0)$ , and (14) and (13) at  $t = 0$ . Given the solution of Eqs. (17a) and (17b), we can determine  $\alpha_{2}(t)$  from the normalization (14). In this way, the problem is solved since all the quantities appearing on the RHS of Eq. (16) are known for  $t \geq 0$ . It is straightforward to find analytical expressions for the pulse shapes, for example, by specifying  $\Omega_{1}(t) = \mathrm{const}$  for  $t > 0$ , as will be done in the following.

As an illustration, we have numerically integrated the full time-dependent Schrödinger equation with the effective Hamiltonian (8). The results are displayed in Fig. 2(a). We have used a pulse shape calculated using the above procedure, with  $g_{1}(t) = 2\delta \omega_{1}(t) = \kappa \equiv \mathrm{const}$  for  $t > 0$  [see Fig. 2(b)]. As Fig. 2 shows, the quantum transmission is ideal.

In practice there will be several sources of imperfections. First, there is the possibility of spontaneous emission from the excited state during the Raman pulses. Its effects can be accounted for in the effective Hamiltonian (8) by the replacement  $\Delta \rightarrow \Delta + i\Gamma / 2$ , where  $\Gamma$  is the

![](images/6e6d539b1d4956c4e0831d604e920efd486ce8fe5c04085c5f61ff4d07fc20a3.jpg)  
FIG. 2. Populations  $\alpha_{1,2}(t)^2$  and  $\beta_{a}(t)^{2}$  for the ideal transmission pulse  $g_{1}(t) = g_{2}(-t)$  given in the inset, specified by  $g_{1}(t\geq 0) = 2\delta \omega_{1}(t\geq 0) = \kappa = \mathrm{const}$ .

decay rate from level  $|r\rangle$ . If we denote by  $\tau$  [≈max ×  $(1 / \kappa, 1 / g_{1,2})$ ] the effective pulse duration, the probability for a spontaneous emission is of the order of  $\Gamma (\Omega_{1,2}^2 + 4g^2) / (8\Delta^2)\tau \ll 1$ . For  $g_1 \approx \kappa$  this probability scales like  $1 / \Delta$ , so that the effects of spontaneous emission are suppressed for sufficiently large detunings. A second source of decoherence will be losses in the mirror and during propagation. They can be taken into account by adding a term  $-i\kappa'(\hat{a}_1^\dagger \hat{a}_1 + \hat{a}_2^\dagger \hat{a}_2)$  in  $H_{\mathrm{eff}}$  (8), where  $\kappa'$  is the additional loss rate. Typically, we expect  $\kappa' \ll \kappa$ . Nevertheless, one can overcome the effects of photon losses by error correction [21]. We have included these imperfections in our numerical simulations. Figure 3 shows the probability of a faithful transmission  $\mathcal{F}$  as a function of  $\kappa'/\kappa$  for different values of  $\Gamma/\Delta$  for the same parameters and pulse shapes as in Fig. 2.

In conclusion, we have proposed for the first time a protocol to accomplish ideal quantum transmission between

![](images/1e5cdb5300fead43c3674ea6224519d23cb79e5432fd319a9b4337977341a1fa.jpg)  
FIG. 3. Fidelity of transmission  $\mathcal{F}$  including the effects of mirror losses and spontaneous emission as a function of  $\kappa' / \kappa$  for  $\Gamma / \Delta = 0$ , 0.01, and 0.05 (solid, dashed, and dot-dashed lines, respectively). Other parameters are as in Fig. 2.

two nodes of a quantum network. Our scheme has been tailored to a potential network implementation in which trapped atoms or ions constitute the nodes, and photon transmission lines provide communication channels between them. Extensions of the present scheme will be presented elsewhere [11], including error correction and new quantum gates in cavity quantum electrodynamics.

We thank the members of the ITP program Quantum Computers and Quantum Coherence for discussions. This work was supported in part by the Österreichischer Fonds zur Förderung der wissenschaftlichen Forschung, by the European TMR network ERB4061PL95-1412, by NSF PHY94-07194 and PHY-93-13668, by DARPA/ARO through the QUIC program, and by the ONR.

[1] D. P. DiVincenzo, Science 270, 255 (1995).  
[2] J.I. Cirac and P. Zoller, Phys. Rev. Lett. 74, 4091 (1995).  
[3] T. Pellizzari et al., Phys. Rev. Lett. 75, 3788 (1995).  
[4] C. Monroe et al., Phys. Rev. Lett. 75, 4714 (1995).  
[5] Q. Turchette et al., Phys. Rev. Lett. 75, 4710 (1995); M. Brune et al., Phys. Rev. Lett. 77, 4887 (1996).  
[6] K. Mattle et al., Phys. Rev. Lett. 76, 4656 (1996).  
[7] In the context of quantum cryptography, long distance transmission of (correlated) photon states is achieved (see Ref. [8]). In contrast, here we are interested in the interface between atoms and photons.  
[8] C.H. Bennett, Phys. Today 48, No. 10, 24 (1995); A.K. Ekert, Phys. Rev. Lett. 67, 661 (1991).  
[9] C. H. Bennet et al., Phys. Rev. Lett. 70, 1895 (1993).  
[10] C.H. Bennet et al., Phys. Rev. Lett. 76, 722 (1996); D. Deutsch et al., Phys. Rev. Lett. 77, 2818 (1996); N. Gisin, Phys. Lett. A 210, 151 (1996).  
[11] J.I. Cirac et al. (to be published).  
[12] C.K. Law and J.H. Eberly, Phys. Rev. Lett. 76, 1055 (1996).  
[13] We ignore for the moment the small effects produced by spontaneous emission during the Raman process. Its effects will be studied in the context of Fig. 3.  
[14] One could also modulate the cavity transmission, but this is technically more difficult.  
[15] C.W. Gardiner, Quantum Noise (Springer-Verlag, Berlin, 1991).  
[16] In a perfect realization of the present scheme no light field will be reflected from the second mirror, and therefore the assumption of unidirectional propagation is not needed.  
[17] C.W. Gardiner, Phys. Rev. Lett. 70, 2269 (1993).  
[18] H. J. Carmichael, Phys. Rev. Lett. 70, 2273 (1993).  
[19] For a review, see P. Zoller and C.W. Gardiner, in "Quantum Fluctuations," Proceedings of the Les Houches Summer School, edited by E. Giacobino et al. (Elsevier, New York, to be published).  
[20]  $\Omega_1(t)$  has to be such that  $\alpha_{1}(\infty) = 0$ . This is fulfilled if  $\Omega_1(\infty) > 0$ , which also guarantees that the denominator in (16) does not vanish for  $t > 0$ .  
[21] P. W. Shor, Phys. Rev. A 52, R2493 (1995); A. M. Steane, Phys. Rev. Lett. 77, 793 (1996); J. I. Cirac, T. Pellizzari, and P. Zoller, Science 273, 1207 (1996); P. Shor, Report No. quant-ph/9605011; D. DiVincenzo and P. W. Shor, Phys. Rev. Lett. 77, 3260 (1996).