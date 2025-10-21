# Characterizing quantum channels with non-separable states of classical light

Bienvenu Ndagano<sup>1</sup>, Benjamin Perez-Garcia<sup>1,2</sup>, Filippus S. Roux<sup>1,3</sup>, Melanie McLaren<sup>1</sup>, Carmelo Rosales-Guzman<sup>1</sup>, Yingwen Zhang<sup>4†</sup>, Othmane Mouane<sup>1</sup>, Raul I. Hernandez-Aranda<sup>2</sup>, Thomas Konrad<sup>5</sup> and Andrew Forbes<sup>1*</sup>

High-dimensional entanglement with spatial modes of light promises increased security and information capacity over quantum channels. Unfortunately, entanglement decays due to perturbations, corrupting quantum links that cannot be repaired without performing quantum tomography on the channel. Paradoxically, the channel tomography itself is not possible without a working link. Here we overcome this problem with a robust approach to characterize quantum channels by means of classical light. Using free-space communication in a turbulent atmosphere as an example, we show that the state evolution of classically entangled degrees of freedom is equivalent to that of quantum entangled photons, thus providing new physical insights into the notion of classical entanglement. The analysis of quantum channels by means of classical light in real time unravels stochastic dynamics in terms of pure state trajectories, and thus enables precise quantum error correction in short- and long-haul optical communication, in both free space and fibre.

Quantum correlations are an ubiquitous resource in short- and long-range communication using photons as carriers of quantum information (qubits). The most significant developments in quantum communication have been realized using polarization as the degree of freedom (DoF) of choice $^{1-4}$ ; the two components of the polarization vector of a photon are robust against atmospheric perturbations, and can easily be controlled with wave plates and polarizing elements. Polarization-based quantum communication is, however, limited to a bandwidth of a single qubit per photon due to the low dimensionality of polarization, and requires the sender and receiver to share a frame of reference.

Employing other degrees of freedom of light in quantum protocols allows for more information to be packed into single photons<sup>5</sup>. The use of spatial modes of light to realize high dimensions has seen many notable advances, with orbital angular momentum (OAM) being the preferred DoF<sup>6-9</sup>. OAM forms a convenient basis, is easy to measure with phase-only holograms<sup>10</sup>, and is conserved down to the single-photon level<sup>11</sup>. However, in free-space quantum channels, spatial modes are adversely affected by atmospheric turbulence<sup>12,13</sup>, which reduces the probability of detecting photons<sup>14-16</sup>, while the induced scattering among spatial modes<sup>17,18</sup> leads to a loss of entanglement in the final state measured in a given subspace<sup>19,20</sup>. To circumvent the deleterious effects of turbulence, as well as the need for a shared reference frame, hybrid OAM and polarization qubit states have been put forward as possible carriers for more robust communication. These hybrid states are rotation invariant, and have been used to demonstrate alignment-free, robust quantum communication, where qubits are encoded in the two DoFs that are entangled<sup>21-24</sup>.

To date, channels with two-dimensional quantum states have been demonstrated over  $144\mathrm{km}$  with polarization<sup>1</sup>, and with hybrid OAM and polarization states over  $210\mathrm{m}$  in a controlled environment to minimize turbulence<sup>23</sup>, as well as recently over  $3\mathrm{km}$

across Vienna $^{25}$ . Fibre channels with two-dimensional entangled spatial modes languish at the centimetre scale $^{26,27}$ , and no study to date has managed to report on the transport of high-dimensional entanglement in any practical sense, in either free space or fibre. To advance further requires characterization schemes that allow one to gain information on the channel, predict the effects of perturbations, and implement error correction in real time.

Process tomography is an essential tool to obtain knowledge about the action of a channel in general, and its effects on the propagation of entangled states in particular[28]. At the single-photon level, this characterization is difficult to do, especially with entangled states: one needs the quantum link to work before it can be characterized, but having it characterized would be immensely helpful in getting it to work. Thus, the process tomography of quantum channels in which (entangled) spatial modes are used remains topical but challenging.

Classical states of light have been employed to mimic path correlated photons in wave guides $^{29-31}$ , while so-called classically entangled light $^{32-38}$  has been used in various applications, notably metrology.

Here we demonstrate a simple approach to characterize a quantum channel using classical light. We exploit the non-separability property of vector beams to show that the state evolution of two classically and two quantum entangled degrees of freedom is in one-to-one correspondence in the case where the channel for both systems acts only on a single DoF. This proves that beyond the mathematical resemblance to its quantum counterpart, classical entanglement does hold physical significance. As an example, we demonstrate that the transport and decay of the classical entanglement of vector beams and the quantum entanglement of a photon pair are identical in a channel perturbed by atmospheric turbulence. Moreover, we show that the one-to-one correspondence between one-sided channels and entangled states, the so-called Choi-Jamiolkowski

isomorphism $^{39}$ , is also valid for classical light fields with arbitrary degree of entanglement. Thus, a full characterization of quantum channels can be obtained via state tomography of classically entangled light beams. This new technique enables one, for example, to determine the action of turbulence, and other channels, on pairs of spatial modes for quantum and classical states of light, and replaces the usual process tomography in both cases. Finally, we demonstrate the applicability of the tools in a proof-of-principle communication experiment employing classically entangled states, showing that the characterization of the channel allows for information recovery and robust data transfer.

# Results

Concept. Consider a typical scenario where quantum information is shared between two parties (Alice and Bob), as shown in Fig. 1a. Alice generates two photons entangled in their spatial DoF, which we will take to be the OAM DoF. Her bi-photon state can then be written as:  $|\varPsi_{\ell}\rangle_{\mathrm{in}} = |\ell \rangle_{\mathrm{A}}| - \ell \rangle_{\mathrm{B}} + | - \ell \rangle_{\mathrm{A}}|\ell \rangle_{\mathrm{B}}$ . She sends one photon to Bob, which passes through the channel; in this study we will consider a free-space link through a turbulent atmosphere as our example, but the concept is not restricted to this particular case and can be adapted to different channels. It has been shown, theoretically and experimentally, that perturbations due to such a channel negatively affect the correlations between the photons, thereby decreasing the efficiency and security of the quantum communication link. In this scenario, photon A experiences the channel while photon B does not. The resulting state  $|\varPsi_{\ell}\rangle_{\mathrm{out}}$  of the photon pair carries the complete information about the channel. This is due to the so-called Choi-Jamiolkowski isomorphism, and could be experimentally verified by teleporting states of single photons using the photon pair in state  $|\varPsi_{\ell}\rangle_{\mathrm{out}}$  as an entanglement resource. The resulting teleportation channel would reproduce the same state changes as the turbulence channel<sup>40</sup>.

We claim that this quantum scenario has a classical equivalent, depicted in Fig. 1b. Here Alice prepares a classical beam that is nonseparable in OAM and polarization:  $|\Psi_{\ell}\rangle_{\mathrm{in}} = |\ell \rangle_{\mathrm{A}}|R\rangle_{\mathrm{B}} + |\neg \ell \rangle_{\mathrm{A}}|L\rangle_{\mathrm{B}}$ , sending the entire beam to Bob through the same channel. In this formalism  $A$  and  $B$  now refer to the two degrees of freedom in the non-separable light field, and not to two photons in the entangled system. But polarization is not affected by turbulence, so the DoF that experiences the deleterious effects of the channel is that of the spatial mode (A). In both cases only the states  $|\ell \rangle_{\mathrm{A}}$  and  $|\neg \ell \rangle_{\mathrm{A}}$  are affected.

The equivalence of the quantum and classical scenarios, together with the fact that the outgoing state in the quantum case contains the full information about the channel, strongly suggest that such non-separable states of light may be used to characterize the effect of the channel on the quantum state, an idea which we later validate theoretically and experimentally.

Classically entangled states. Our hybrid encoding space, described by the higher-order Poincaré sphere $^{41}$ , is formed from the tensor product of the infinite dimensional OAM and the two-dimensional polarization Hilbert spaces. We are interested in states of the form

$$
\left| \Psi_ {\ell} \right\rangle_ {\text {i n}} = \alpha \left| \ell \right\rangle_ {\mathrm {A}} \left| - \ell \right\rangle_ {\mathrm {B}} + \beta | - \ell \rangle_ {\mathrm {A}} \left| \ell \right\rangle_ {\mathrm {B}} \tag {1}
$$

$$
\left| \Psi_ {\ell} \right\rangle_ {\mathrm {i n}} = \alpha \left| \ell \right\rangle_ {\mathrm {A}} \left| R \right\rangle_ {\mathrm {B}} + \beta | - \ell \rangle_ {\mathrm {A}} \left| L \right\rangle_ {\mathrm {B}} \tag {2}
$$

where  $|\alpha|^2 + |\beta|^2 = 1$ . Equation (1) defines a two-photon entanglement system expressed in the OAM basis,  $\{| - \ell \rangle, | \ell \rangle \}$ , with each photon carrying  $\ell$  quanta  $\hbar$  of  $\mathrm{OAM}^{42}$ . Equation (2) defines a vector vortex mode, which here will be the classical equivalent to the system defined in equation (1). The basis states  $\{|L\rangle, |R\rangle \}$  correspond the left and right circular polarization states, respectively.

![](images/04be8b651f42d50f1df827b02aeddc193030539a6d9546008c5cc43492cdc92c.jpg)

![](images/bf9f476331bc916ee45b6627868f2a00392ef62043aa4b87cdd462b4c00639cb.jpg)  
Quantum Perturbed eigenstates  $\{\left|\ell \rangle_{\mathrm{A}}, - \ell \rangle_{\mathrm{A}}\}$

![](images/79a489ac9ad04f52e8eecb9f05e3b4d148acaa6e5ecc2303aabbbdf134030e83.jpg)

![](images/844e85abec8d1988e5a625ecd14ef2d013a09e9ddbc33ff2a41461995c6c560f.jpg)

![](images/432fa31d39d8c02668bb0e2bdeb140fd6dd5577072745e0b8a727c6901a349ff.jpg)  
Classical Perturbed eigenstates  $\{\left|\ell \rangle_{\mathrm{A}^{\prime}} - \ell \rangle_{\mathrm{A}}\}$

![](images/77a9d2428179191ebe6a8e9771331a459b7dee10c6fd486de8b41e152c4cde1c.jpg)  
Figure 1 | Illustration of the concept. a, Alice generates two entangled photons using a SPDC process (see Methods), and sends one photon (Photon A) to Bob through a free-space turbulent channel, which affects the quantum correlations due to perturbations to photon A. b, Equivalently, Alice sends information to Bob using a classically entangled bright light field (laser beam). The spatial DoF (DoF A) is affected by the channel, whereas the polarization (DoF B) is not. APD, avalanche photodiode; BBO, beta barium borate (nonlinear optical crystal); SLM, spatial light modulator and CCD, charge-coupled device.

We choose the concurrence as our measure of entanglement, as it has been shown to be effective in quantifying the degree of quantum and classical entanglement $^{43,44}$ . For qubit pairs defined as in equations (1) and (2), the concurrence is given by:

$$
\mathcal {C} \left(\left| \Psi_ {\ell} \right\rangle_ {\text {i n}}\right) = 2 \left| \alpha \beta \right| \tag {3}
$$

Channel tomography for turbulence. We consider an OAM state passing through turbulence that causes modal dispersion and thus broadens the OAM spectrum. Here, for each instance of the stochastically varying turbulence, the state evolution is a different unitary transformation that maps pure states onto pure states and takes the form (see Supplementary Information):

$$
| \ell \rangle \rightarrow \sum_ {\ell^ {\prime}} p _ {\ell - \ell^ {\prime}} | \ell^ {\prime} \rangle \tag {4}
$$

where  $p_{\ell - \ell'}$  are the modal weightings. Thus, a given input vector vortex mode  $|\Psi_{\ell}\rangle_{\mathrm{in}}$  propagating through a turbulent channel will be transformed as follows:

$$
\begin{array}{l} \left| \right. \Psi_ {\ell} \left. \right\rangle_ {\text {i n}} \rightarrow \alpha \sum_ {\ell^ {\prime}} p _ {\ell - \ell^ {\prime}} \left| \right. \ell^ {\prime} \left. \right\rangle\left| \right. R \left. \right\rangle + \beta \sum_ {\ell^ {\prime}} p _ {- \ell - \ell^ {\prime}} \left| \right. \ell^ {\prime} \left. \right\rangle\left| \right. L \left. \right\rangle (5) \\ = \alpha p _ {0} | \ell \rangle | R \rangle + \alpha p _ {2 \ell} | - \ell \rangle | R \rangle + \beta p _ {- 2 \ell} | \ell \rangle | L \rangle \\ + \beta p _ {0} | - \ell \rangle | L \rangle + \sum (\dots) (6) \\ \end{array}
$$

Note that we omit the subscripts A and B for simplicity of notation. Filtering for OAM values  $-\ell$  and  $\ell$  yields the un-normalized final state

$$
\left| \Psi_ {\ell} \right\rangle_ {\text {o u t}} = \alpha p _ {0} | \ell \rangle | R \rangle + \beta p _ {- 2 \ell} | \ell \rangle | L \rangle + \alpha p _ {2 \ell} | - \ell \rangle | R \rangle + \beta p _ {0} | - \ell \rangle | L \rangle \tag {7}
$$

Since in this state the polarization serves as record of the original OAM value,  $(R,L)$  for  $(\ell , - \ell)$ , we can now read off the operator M that describes the action  $|\Psi_{\ell}\rangle_{\mathrm{in}}\rightarrow |\Psi_{\ell}\rangle_{\mathrm{out}} = \mathrm{M}\otimes \mathbb{1}|\Psi_{\ell}\rangle_{\mathrm{in}}$  of the channel on the OAM DoF:

$$
\mathrm {M} = p _ {0} | \ell \rangle \langle \ell | + p _ {- 2 \ell} | \ell \rangle \langle - \ell | + p _ {2 \ell} | - \ell \rangle \langle \ell | + p _ {0} | - \ell \rangle \langle - \ell | \tag {8}
$$

![](images/3a829cd485ac7e2c6652ef5df322302c889bc468aa46b90e5a3506bce7afbf1e.jpg)

![](images/148fb3b7ed86269f0ac55b6e796855fbff4ffac28bf170c45a3af73462d9cfa7.jpg)

![](images/1ec7861e5df2577a503408a7b3c0e4f9781a6239c14d8bd6512192e31909fb4c.jpg)  
Figure 2 | Experimental set-up. a, The entangled qubits were encoded using a  $q$ -plate and propagated through the turbulent conditions simulated with single Kolmogorov phase screens. The output state was analysed using a vector mode sorter that performs a decomposition into vector states. b, Full state tomography of the perturbed state was performed by projecting polarization states, selected with the quarter or half-wave plate, onto OAM states encoded on a spatial light modulator. The outputs of the projections were observed in the far field using a camera. c, Vector vortex modes are (de)multiplexed using two Mach-Zehnder interferometers, with the  $q$ -plates used to (de)encode hybrid qubits. PBS, polarizing beam splitter.

![](images/92097481891a48372a37bc63fbc7021a44eb641d7a4f4d0a3e20591748729f3e.jpg)

The one-to-one correspondence between the state (equation (7)) of the vector beam and the Kraus operator (equation (8)) for the OAM channel established here for classical light fields, is a manifestation of the Choi-Jamiolkowski isomorphism known to also connect the quantum OAM channel (same operator M) and the state of the qubit pair obtained from equation (1). It follows that the matrix elements of the quantum channel operator, M, typically determined by process tomography requiring many measurements on single photons, can now be monitored by a state tomography of the classical output state  $|\varPsi_{\ell}\rangle_{\mathrm{out}}$  in real time (single measurement of many photons).

Decay of classical entanglement in turbulence. The entanglement of the final state (equation (7)) is given by the concurrence  $\mathcal{C}(|\Psi_{\ell}\rangle_{\mathrm{out}}) = 2|\alpha \beta ||p_0^2 -p_{2\ell}p_{-2\ell}| / p$  which can be expressed in terms of the entanglement of the input state by

$$
\mathcal {C} \left(\left| \Psi_ {\ell} \right\rangle_ {\text {o u t}}\right) = \mathcal {C} _ {\mathrm {c h}} \mathcal {C} \left(\left| \Psi_ {\ell} \right\rangle_ {\text {i n}}\right) \tag {9}
$$

where  $0 \leq \mathcal{C}_{\mathrm{ch}} = |p_0^2 - p_{2\ell}p_{-2\ell}| / p \leq 1$  equals the fraction of entanglement preserved by the channel and is given by the output concurrence obtained from an initially maximally entangled state with probability  $p = (2|p_0|^2 + |p_{2\ell}|^2 + |p_{-2\ell}|^2) / 2$ . For example, in relatively strong turbulence, where  $|p_{2\ell}p_{-2\ell}| \approx |p_0^2|$ , the concurrence  $\mathcal{C}(|\Psi_\ell\rangle_{\mathrm{out}})$  vanishes, and with it all entanglement. The relation in equation (9) has been derived in ref. 45 for entangled pairs of two-level systems. Note that for the channel under present investigation,

the decay of the concurrence can be modelled as a function of the turbulence strength according to the following relation<sup>19</sup>

$$
\mathcal {C} \left(\left| \Psi_ {\ell} \right\rangle_ {\text {o u t}}\right) = \frac {\mathrm {S R}}{\mathrm {S R} ^ {2} - \mathrm {S R} + 1} \tag {10}
$$

where SR is a measure of the turbulence strength known as the Strehl ratio (see Methods for more details).

The broadening of the OAM spectrum described by equation (5) leads to intermodal coupling among vector modes, resulting in a loss of entanglement with increasingly strong perturbations. Within the subspace of vector modes with  $|\ell| = 1$ , this coupling can be analysed using the Bell basis $^{46}$ , known as optical fibre modes in waveguide theory:

$$
\left| \mathrm {T M} \right\rangle_ {1} = \frac {1}{\sqrt {2}} (| 1 \rangle | R \rangle + | - 1 \rangle | L \rangle) \tag {11}
$$

$$
\left| \mathrm {T E} \right\rangle_ {1} = \frac {1}{\sqrt {2}} (| 1 \rangle | R \rangle - | - 1 \rangle | L \rangle) \tag {12}
$$

$$
\left| \mathrm {H E} ^ {\mathrm {e}} \right\rangle_ {1} = \frac {1}{\sqrt {2}} (| 1 \rangle | L \rangle + | - 1 \rangle | R \rangle) \tag {13}
$$

$$
\left| \mathrm {H E} ^ {\circ} \right\rangle_ {1} = \frac {1}{\sqrt {2}} (| 1 \rangle | L \rangle - | - 1 \rangle | R \rangle) \tag {14}
$$

By way of example, consider a  $|\mathrm{TM}\rangle_{1}$  mode propagating in a strong turbulence regime. In the special case where  $p_0 = p_{2\ell} = p_{-2\ell}$  (strong coupling), the final state reduces to

$$
\begin{array}{l} \left| \Psi_ {1} \right\rangle_ {\text {o u t}} = \frac {1}{\sqrt {2}} p _ {0} [ | 1 \rangle | R \rangle + | - 1 \rangle | L \rangle + | 1 \rangle | L \rangle + | - 1 \rangle | R \rangle ] (15) \\ = \frac {1}{\sqrt {2}} p _ {0} \left[ | \mathrm {T M} \rangle_ {1} + | \mathrm {H E} ^ {\mathrm {e}} \rangle_ {1} \right] (16) \\ = \frac {1}{\sqrt {2}} p _ {0} (| 1 \rangle + | - 1 \rangle) \otimes (| R \rangle + | L \rangle) (17) \\ \end{array}
$$

which is separable (not entangled), that is, the spatial and polarization DoFs can be factorized. Equivalently in the quantum case, perturbations incurred by one of the two photons (modal dispersion and projection onto a subspace) will transform an initial entangled state into a final factorizable (separable) state.

Classical and quantum experiments. Here we demonstrate experimentally the equivalence between the evolution of classical and quantum entanglement in turbulence. Our classical experimental set-up is illustrated in Fig. 2, and comprises creation, propagation and detection stages. In the creation step, the vector vortex mode is prepared either directly from a 'spiral laser'47, or by using wave plates and  $q$ -plates48 to transform a linearly polarized Gaussian beam into a vector vortex mode. We passed our vector mode through a turbulent channel (turbulence phase screen) that was made to vary with time, and analysed the output beam with two detection systems: a vector mode sorter to uniquely detect each of the maximally entangled modes, thus evaluating the amount of intermodal coupling, and a tomography detector44 to evaluate the concurrence (see Methods). In the quantum experiment, we used spontaneous parametric down conversion (SPDC) to produce two photons entangled in OAM, of which one was sent through a turbulent channel (see Methods). A state tomography of the two photons was performed to determine the evolution of the concurrence as a function of the turbulence strength.

In Fig. 3a we show the measured dependence of the concurrence of our quantum and classical states as a function of the degree of turbulence in the channel, together with the theoretical prediction from equation (10). We used a  $|\mathrm{TM}\rangle_{1}$  vector mode and an  $|\ell| = 1$  maximally entangled OAM state as our equivalent classical and quantum systems, respectively. The experimental results for both the classical and quantum cases are in excellent agreement with the theory. Hence, the agreement between the classical and quantum experiments validates the equivalence of the quantum and classical models depicted in Fig. 1. The inset in Fig. 3a shows the variation in the measured fidelity of a  $|\mathrm{TM}\rangle_{1}$  vector mode in turbulence, computed with respect to a maximally entangled state. Furthermore, by varying the concurrence of the input vector mode in Fig. 3b, we experimentally confirmed, for the first time for spatial modes, the decay law of entanglement[45] as summarized for pure states in equation (9); that is, that there is a linear relationship between  $\mathcal{C}(|\Psi_{\ell}\rangle_{\mathrm{out}})$  and  $\mathcal{C}(|\Psi_{\ell}\rangle_{\mathrm{in}})$ . This provides physical meaning for the notion of entanglement at the classical level; that is, beyond the mathematical non-separability of the DoFs, nature does not distinguish between classical and quantum entanglement in one-sided channels.

The observed decay of entanglement with increasing turbulence, as predicted by equation (10), is explained by examining the effects of turbulence on the mode spectrum: for example, in the classical case, with increasing turbulence strength, the scattering among vector vortex modes is increased, as seen in Fig. 4a-e. This is due to the spreading of the OAM spectrum, as shown in Fig. 4f and g, which leads to crosstalk among vector vortex modes, as described by equation (7), and similarly for the quantum case.

![](images/acfda6f9a93a0d9afe1f0be64743c4b5e66a24d93b264d443b7be963c9138fd1.jpg)

![](images/086a01cb857a60eb34683387c746cce53833b5f1752d6be3060aea5800b5ee5e.jpg)  
Figure 3 | Evolution of classical entanglement in turbulence. a, The measured concurrence variation after propagation through turbulence screens of various SR strengths (increasing from high to low SR values) for the classical (red markers) and quantum (blue markers) states, correctly follow the theoretical prediction for one of two entangled photons going through a turbulent channel (green dashed line). The fluctuations in SR arise from the statistical averaging of the turbulence screen for an encoded SR value. The inset shows the decay in fidelity of the output state with respect to a maximally entangled state, as a function of the turbulence strength. b, The measured concurrence obeys the predicted linear mapping to the concurrence of the input state. Here we have shown this for three channels with  $\mathrm{SR} = 1.00$ , 0.70 and 0.45. The error bars represent the standard errors in the averages over the multiple turbulence realizations.

Having characterized the impact of the channel on the states to be propagated, we used the set-up to show a proof-of-principle data transmission over the channel. It has been recently shown that the non-separability of vector vortex beams can be used to encode two bits of information simultaneously on the entangled DoFs $^{46}$ . In our scheme, we (de)multiplexed the four maximally entangled vector modes as shown in Fig. 2c. This allowed us to perform a four-bit encoding scheme based on these states. The encoded image in Fig. 5a was transmitted through one particular instance of a turbulence channel with turbulence strength  $\mathrm{SR} = 0.3$ . Without any correction, the received image shows significant amounts of distortion, resulting in a  $64.2\%$  correlation coefficient with respect to the encoded image (Fig. 5c). This is due to the intermodal coupling corrupting the encoded bits sequences, and resulting in state errors measured at the receiver's end. A practical advantage of studying the decoherence induced by a channel is the ability to mitigate perturbations through pre- or post-processing of the data. After propagation through a perturbing medium, the input and output states can be related by

$$
\left| \Psi_ {\ell} \right\rangle_ {\text {o u t}} = \mathrm {M} \otimes \mathbb {1} \left| \Psi_ {\ell} \right\rangle_ {\text {i n}} \tag {18}
$$

where  $M$  is the channel operator of the system that contains all the information about the crosstalk induced by the medium. The complete tomography data to determine the matrix  $\mathbf{M} \otimes \mathbb{1}$  is graphically represented in Fig. 5b. A simplified visualization of the tomography data is given in terms of the coupling amplitudes between orthogonal vector modes, which is shown in the

![](images/cd0b340d395f275477acb570d210ce53be1460c6feb12ec0a99f0aacefd2d13d.jpg)  
Figure 4 | Evolution of the mode spectrum in turbulence. a-e, Vector mode dispersion for the four vector vortex modes of the  $|\ell| = 1$  subspace for average SR values of 1.0, 0.7, 0.5, 0.4 and 0.3 respectively. The matrices show the evolution of the power distribution among the four-vector detector for a given input mode. f,g, Effect of the turbulence on the spatial DoF, measured by modal decomposition of the  $|-1\rangle |L\rangle$  and  $|1\rangle |R\rangle$  input qubit states, respectively. The scattering of the OAM eigenstates is observed through a redistribution of energy between OAM modes with increasing SR.

Supplementary Information. Thus, the perturbation can be cancelled by correcting the final state,  $|\Psi_{\ell}\rangle_{\mathrm{out}}$ , with  $\mathbf{M}^{-1} \otimes \mathbb{1}$  when processing the measurement data, or by physically implementing a conjugate filter (see Supplementary Information). Using this correction technique, we obtained an image with an increased correlation coefficient of 98.9%, as shown in Fig. 5d.

# Discussion

The characterization of quantum channels is a sine qua non to the implementation of practical quantum communication protocols. Using vector vortex modes, so-called classically entangled light, and a pair of entangled photons, we demonstrated that the evolution of two entangled DoFs, one of which is affected by atmospheric turbulence, is the same for classical and quantum light. We have shown this for OAM in atmospheric turbulence, but the approach can easily be generalized to other spatial modes and perturbations.

The decay of classical entanglement we observed demonstrates that vector vortex modes are not resilient to atmospheric turbulence. This is further supported by the measured decay in fidelity between the final and the original state (see Methods), as shown in the inset of Fig. 3a. Both results are not in contradiction with the possibility to recover qubits encoded in two rotationally symmetric vector states[22] that was tested against the influence of turbulence[24]. This method uses a filter (post-selection) to eliminate all spatial crosstalk components generated by weak turbulence, resulting in the loss of photons. However, it does not provide a measure of resilience to turbulence, as all modes can be recovered using this technique.

In the quantum realm, a channel tomography requires multiple measurements to be performed on an ensemble of systems, in our case on photons consecutively passing the stochastic channel over an extended period of time—this is what here gives rise to mixed states despite the unitary evolution of each single photon. In fact,

![](images/6a638ff4a83428c2a3c8c1f859e61b60e7165629f56e16098aa4ab9d0d594314.jpg)

![](images/85179c29d462abf5627fdbfaedb64df138c8e5a44476e2973a0e2a9adb65a8c7.jpg)

![](images/341539c1e7055ffaf1e2531551eef492f64c3b30c4aa50140a7c47b8ac8e4a5e.jpg)  
Figure 5 | Experimental results for data transmission over turbulent channel. a, Using a four-bit encoding technique with four multiplexed vector modes, a  $425 \times 513$  pixels image of Maxwell was transmitted through a turbulent channel with  $SR = 0.3$ , and demultiplexed at the receiver's end. A threshold at  $15\%$  of the maximum received signal was applied to the data to filter noise signals. b, Characterization of the channel with a full tomography of the classically entangled light. c, The channel perturbation resulted in a distorted image at the receiver's end with a correlation coefficient of  $64.2\%$ . d, Correcting the image with the inverse channel matrix increased the correlation coefficient to  $98.9\%$ . Maxwell image credit: Bettmann/Contributor/Bettmann/Getty Images.

![](images/9cbf73d0ae0dcd2ec189bc39a08a6c4cc9e3c5dc2c966b3fda45b7ea779a51ea.jpg)

the unitary evolution of a single photon cannot be detected directly, just as the state of a single photon cannot. However, for classical light, these restrictions do not exist, allowing a channel tomography

and error correction in real time, implemented in quantum links. The resulting ability to detect the specific realizations of stochastic perturbations classically, enables an unravelling of the otherwise mixed quantum state dynamics in terms of pure states and to reinstall the original state of the photon.

We point out that this approach differs from the standard classical communications correction tools, where multiple orthogonal modes are sent sequentially through the channel to infer the crosstalk matrix. Rather, our approach allows a single maximally entangled state to be sent, followed by a complete tomography measurement, to infer the evolution of the quantum state in real time.

# Methods

Methods, including statements of data availability and any associated accession codes and references, are available in the online version of this paper.

Received 25 May 2016; accepted 29 November 2016; published online 23 January 2017; corrected online 31 March 2017

# References

1. Ursin, R. et al. Entanglement-based quantum communication over  $144\mathrm{km}$ . Nat. Phys. 3, 481-486 (2007).  
2. Ma, X.-S. et al. Quantum teleportation over 143 kilometres using active feed-forward. Nature 489, 269-273 (2012).  
3. Yin, J. et al. Quantum teleportation and entanglement distribution over 100-kilometre free-space channels. Nature 488, 185-188 (2012).  
4. Herbst, T. et al. Teleportation of entanglement over  $143\mathrm{km}$ . Proc. Natl Acad. Sci. USA 112, 14202-14205 (2015).  
5. Cerf, N. J., Bourennane, M., Karlsson, A. & Gisin, N. Security of quantum key distribution using  $d$ -level systems. Phys. Rev. Lett. 88, 127902 (2002).  
6. Dada, A. C., Leach, J., Buller, G. S., Padgett, M. J. & Andersson, E. Experimental high-dimensional two-photon entanglement and violations of generalized Bell inequalities. Nat. Phys. 7, 677-680 (2011).  
7. Romero, J., Giovannini, D., Franke-Arnold, S., Barnett, S. & Padgett, M. Increasing the dimension in high-dimensional two-photon orbital angular momentum entanglement. Phys. Rev. A 86, 012334 (2012).  
8. Fickler, R. et al. Interface between path and orbital angular momentum entanglement for high-dimensional photonic quantum information. Nat. Commun. 5, 4502 (2014).  
9. Zhang, Y. et al. Engineering two-photon high-dimensional states through quantum interference. Sci. Adv. 2, e1501165 (2016).  
10. Forbes, A., Dudley, A. & McLaren, M. Creation and detection of optical modes with spatial light modulators. Adv. Opt. Photon. 8, 200-227 (2016).  
11. Mair, A., Vaziri, A., Weihs, G. & Zeilinger, A. Entanglement of the orbital angular momentum states of photons. Nature 412, 313-316 (2001).  
12. Malik, M. et al. Influence of atmospheric turbulence on optical communications using orbital angular momentum for encoding. Opt. Express 20, 13195-13200 (2012).  
13. Rodenburg, B. et al. Influence of atmospheric turbulence on states of light carrying orbital angular momentum. Opt. Lett. 37, 3735-3737 (2012).  
14. Paterson, C. Atmospheric turbulence and orbital angular momentum of single photons for optical communication. Phys. Rev. Lett. 94, 153901 (2005).  
15. Gopaul, C. & Andrews, R. The effect of atmospheric turbulence on entangled orbital angular momentum states. New J. Phys. 9, 94 (2007).  
16. Tyler, G. A. & Boyd, R. W. Influence of atmospheric turbulence on the propagation of quantum states of light carrying orbital angular momentum. Opt. Lett. 34, 142-144 (2009).  
17. Chen, C., Yang, H., Tong, S. & Lou, Y. Changes in orbital-angular-momentum modes of a propagated vortex Gaussian beam through weak-to-strong atmospheric turbulence. Opt. Express 24, 6959-6975 (2016).  
18. Neo, R. et al. Measurement and limitations of optical orbital angular momentum through corrected atmospheric turbulence. Opt. Express 24, 2919-2930 (2016).  
19. Roux, F. S., Wellens, T. & Shatokhin, V. N. Entanglement evolution of twisted photons in strong atmospheric turbulence. Phys. Rev. A 92, 012326 (2015).  
20. Ibrahim, A. H., Roux, F. S., McLaren, M., Konrad, T. & Forbes, A. Orbital-angular-momentum entanglement in turbulence. Phys. Rev. A 88, 012312 (2013).  
21. Souza, C. et al. Quantum key distribution without a shared reference frame. Phys. Rev. A 77, 032345 (2008).  
22. D'Ambrosio, V. et al. Complete experimental toolbox for alignment-free quantum communication. Nat. Commun. 3, 961 (2012).

23. Vallone, G. et al. Free-space quantum key distribution by rotation-invariant twisted photons. Phys. Rev. Lett. 113, 060503 (2014).  
24. Farias, O. J. et al. Resilience of hybrid optical angular momentum qubits to turbulence. Sci. Rep. 5, 8424 (2015).  
25. Krenn, M., Handsteiner, J., Fink, M., Fickler, R. & Zeilinger, A. Twisted photon entanglement through turbulent air across Vienna. Proc. Natl Acad. Sci. USA 112, 14197-14201 (2015).  
26. Löffler, W. et al. Fiber transport of spatially entangled photons. Phys. Rev. Lett. 106, 240505 (2011).  
27. Kang, Y. et al. Measurement of the entanglement between photonic spatial modes in optical fibers. Phys. Rev. Lett. 109, 020502 (2012).  
28. Mohseni, M., Rezakhani, A. T. & Lidar, D. A. Quantum-process tomography: resource analysis of different strategies. Phys. Rev. A 77, 032322 (2008).  
29. Bromberg, Y., Lahini, A., Morandotti, F. & Silberberg, Y. Quantum and classical correlations in waveguide lattices. Phys. Rev. Lett. 102, 253904 (2009).  
30. Keil, R. et al. Photon correlations in two-dimensional waveguide arrays and their classical estimate. Phys. Rev. A 81, 023834 (2010).  
31. Keil, R. et al. Classical characterization of biphoton correlation in waveguide lattices. Phys. Rev. A 83, 013808 (2011).  
32. Spreeuw, R. J. C. A classical analogy of entanglement. Found. Phys. 28, 361 (1998).  
33. Pereira, L. J., Khoury, A. Z. & Dechoum, K. Quantum and classical separability of spin-orbit laser modes. Phys. Rev. A 90, 053842 (2014).  
34. Töppel, F., Aiello, A., Marquardt, C., Giacobino, E. & Leuchs, G. Classical entanglement in polarization metrology. New. J. Phys. 16, 073019 (2014).  
35. Guzman-Silva, D. et al. Demonstration of local teleportation using classical entanglement. *Laser Photon. Rev.* **10**, 317–321 (2016).  
36. Karimi, E. & Boyd, R. W. Classical entanglement? Science 350, 1172-1173 (2015).  
37. D'Ambrosio, V. et al. Photonic polarization gears for ultra-sensitive angular measurements. Nat. Commun. 4, 2432 (2013).  
38. Karimi, E. et al. Spin-orbit hybrid entanglement of photons and quantum contextuality. Phys. Rev. A 82, 022115 (2010).  
39. Jiang, M., Luo, S. & Fu, S. Channel-state duality. Phys. Rev. A 87, 022310 (2013).  
40. Dur, W., Hein, M., Cirac, J. I. & Briegel, H. J. Standard forms of noisy quantum operations via depolarization. Phys. Rev. A 72, 052326 (2005).  
41. Milione, G., Sztul, H., Nolan, D. & Alfano, R. Higher-order Poincaré sphere, Stokes parameters, and the angular momentum of light. Phys. Rev. Lett. 107, 053601 (2011).  
42. Allen, L., Beijersbergen, M. W., Spreeuw, R. J. C. & Woerdman, J. P. Orbital angular momentum of light and the transformation of Laguerre-Gaussian laser modes. Phys. Rev. A 45, 8185-8189 (1992).  
43. Wootters, W. Entanglement of formation and concurrence. Quant. Inf. Comput. 1, 27-44 (2001).  
44. McLaren, M., Konrad, T. & Forbes, A. Measuring the nonseparability of vector vortex beams. Phys. Rev. A 92, 023833 (2015).  
45. Konrad, T. et al. Evolution equation for quantum entanglement. Nat. Phys. 4, 99-102 (2008).  
46. Milione, G., Nguyen, T. A., Leach, J., Nolan, D. A. & Alfano, R. R. Using the nonseparability of vector beams to encode information for optical communication. Opt. Lett. 40, 4887-4890 (2015).  
47. Naidoo, D. et al. Controlled generation of higher-order Poincaré sphere beams from a laser. Nat. Photon. 10, 327-332 (2016).  
48. Marrucci, L., Manzo, C. & Papro, D. Optical spin-to-orbital angular momentum conversion in inhomogeneous anisotropic media. Phys. Rev. Lett. 96, 163905 (2006).

# Acknowledgements

We express our gratitude to L. Marrucci for providing us with  $q$ -plates. B.N. acknowledges financial support from the National Research Foundation of South Africa and the African Laser Centre. C.R.-G. acknowledges Claude Leon Foundation. B.P.-G., C.R.-G. and R.I.H.-A. acknowledge support from CONACyT.

# Author contributions

The conceptual idea was formulated by A.F. and T.K. The theoretical formalism was laid out by A.F., T.K., F.S.R., B.N. and B.P.-G. The classical experiments were carried out by B.N., B.P.-G., O.M. and C.R.-G., while the quantum experiment was carried out by Y.Z. All authors contributed to the data analysis and interpretation of the results. B.N. wrote the manuscript with inputs from all the authors. A.F. supervised the project.

# Additional information

Supplementary information is available in the online version of the paper. Reprints and permissions information is available online at www.nature.com/reprints.

Correspondence and requests for materials should be addressed to A.F.

# Competing financial interests

The authors declare no competing financial interests.

# Methods

Generation and detection of vector vortex beams using a  $q$ -plate. The generation of vector vortex beams has been made convenient with the invention of  $q$ -plates. These are phase plates with locally varying birefringence that gives rise to a coupling between SAM and OAM through the Pancharatnam-Berry geometric phase[48]. The encoding of entangled qubits with a  $q$ -plate is summarized by the following transformation rules:

$$
\left| \ell , L \right\rangle \xrightarrow {q \cdot \text {p l a t e}} \left| \ell + 2 q, R \right\rangle \tag {19}
$$

$$
\left| \ell , R \right\rangle \xrightarrow {q \cdot \text {p l a t e}} \left| \ell - 2 q, L \right\rangle \tag {20}
$$

where  $q$  is the topological charge of the  $q$ -plate. The four vector vortex modes of a given  $|\ell|$  subspace are non-separable superpositions of qubit states generated as in equations (19) and (20) with the  $|L\rangle$  and  $|R\rangle$  input components phase shifted by 0 or  $\pi$ . By transforming a linearly polarized Gaussian beam, the  $|\mathrm{TE}_{\ell}\rangle$  and  $|\mathrm{TM}_{\ell}\rangle$  are generated with a  $q$ -plate with  $+|q|$  topological charge, whereas the  $|\mathrm{HE}_{\ell}^{e}\rangle$  and  $|\mathrm{HE}_{\ell}^{o}\rangle$  are generated with one having  $-|q|$  topological charge.

In addition to their encoding function,  $q$ -plates can also be used as decoders. This is achieved by simply reversing the generation process outlined in equations (19) and (20)

$$
\left| \ell + 2 q, R \right\rangle \xrightarrow {q \text {- p l a t e}} \left| \ell + 2 \left(q - q ^ {\prime}\right), L \right\rangle \tag {21}
$$

$$
\left| \ell - 2 q, L \right\rangle \xrightarrow {q \cdot \text {p l a t e}} \left| \ell - 2 \left(q - q ^ {\prime}\right), R \right\rangle \tag {22}
$$

Thus, one recovers the information encoded when the encoding and decoding  $q$ -plates have identical topological charges ( $q = q'$ ). This technique is in principle identical to the modal decomposition of scalar modes with spatial light modulators (SLMs) (see Supplementary Information for further details): a mode is directed onto the SLM, where an inner product of the incident field with a match filter hologram is performed, and the on-axis intensity is measured by a camera situated after a Fourier lens<sup>10</sup>. When the input mode matched the filter, a bright on-axis intensity was observed; otherwise a zero on-axis intensity was measured. Thus, the modal content of the state exiting the turbulence plate was efficiently measured.

Sorting vector modes using  $q$ -plates. Consider an arbitrary vector mode  $\left|\Psi \right\rangle_{\ell}$  generated by passing a linearly polarized field Gaussian field  $A(\mathbf{r})\hat{i}$  through a  $q$ -plate, where the position vector  $\mathbf{r} = (r,\phi)$  is expressed in standard polar coordinates, and the unit vector  $\hat{i}$  represents the polarization direction. The Gaussian field is transformed by a  $q$ -plate, which can be represented by the following Hermitian operator,

$$
\hat {Q} _ {q} = \left[ \begin{array}{c c} \cos (2 q \phi) & \sin (2 q \phi) \\ \sin (2 q \phi) & - \cos (2 q \phi) \end{array} \right] \tag {23}
$$

where  $q$  is the topological charge of the  $q$ -plate. Subsequently, passing  $|\Psi\rangle$  through a second  $q$ -plate with topological charge  $q'$ , and measuring the linear polarization state results in the following output:

$$
T = \langle j | \hat {Q} _ {q ^ {\prime}} ^ {\dagger} \hat {Q} _ {q} A (\mathbf {r}) | i \rangle = A (\mathbf {r}) \langle j | \hat {Q} _ {q ^ {\prime}} ^ {\dagger} \hat {Q} _ {q} | i \rangle = \langle \Phi | \Psi \rangle \tag {24}
$$

where  $|\Phi \rangle$  is a vector state. Let  $|r\rangle$  be a two-dimensional normalized position vector. By projecting equation (24) into position space, we obtain

$$
T (r) = \langle \Phi | \mathbb {1} | \Psi \rangle = \int \mathrm {d} r \langle \Phi | r \rangle \langle r | \Psi \rangle = \Phi^ {*} (r) \Psi (r) \tag {25}
$$

Using a lens, the field observed in the Fourier plane is given by

$$
T (k) = \int \mathrm {d} r \Phi^ {*} (r) \Psi (r) \exp (i \mathbf {k} \cdot \mathbf {r}) \tag {26}
$$

From the orthogonality of OAM modes and polarization, the on-axis intensity in the Fourier plane will be given by

$$
\left| T (0) \right| ^ {2} = \left| A (\mathbf {0}) \right| ^ {2} \delta_ {q, q ^ {\prime}} \delta_ {i, j} \tag {27}
$$

This means that measuring the on-axis intensity will yield a non-zero value if and only if the two  $q$ -plates have the same topological charge  $q$ , and the polarization measured is that of the initial field that generated  $|\Psi \rangle$ .

Concurrence of entangled qubit pairs. In general, the concurrence of an arbitrary qubit state (pure or mixed) can be computed from its density matrix  $\rho$  (ref. 43)

$$
\mathcal {C} (\rho) = \max  \left\{0, \sqrt {\lambda_ {1}} - \sqrt {\lambda_ {2}} - \sqrt {\lambda_ {3}} - \sqrt {\lambda_ {4}} \right\} \tag {28}
$$

where  $\lambda_{i}$  are the eigenvalues in decreasing order of the Hermitian matrix  $R = \rho (\sigma_2\otimes \sigma_2)\rho^* (\sigma_2\otimes \sigma_2)$ , and  $\sigma_{2}$  is the Pauli matrix  $\sigma_{2} = \left[ \begin{array}{cc}0 & -i\\ i & 0 \end{array} \right]$ . The density matrix,  $\rho$ , of a qubit state, can be expressed in terms of the Pauli matrices:

$$
\rho = \frac {1}{4} \sigma_ {0} \otimes \sigma_ {0} + \sum_ {\substack {n, m = 0 \\ n \neq m = 0}} ^ {3} \rho_ {n, m} \sigma_ {n} \otimes \sigma_ {m} \tag{29}
$$

where  $\rho_{n,m}$  are complex coefficients,  $\sigma_0$  is the identity matrix and  $\sigma_{n}$  are the Pauli matrices. To account for fluctuations in the number of photons and other experimental errors, we used an over-complete set of measurements (36 rather than the minimum of 16) to reconstruct the density matrix (see Methods). However, it is possible to perform the state tomography by other approaches with fewer measurements, for example, a minimum of eight measurements corresponding to the four complex coefficients of equation (25). We used equations (28) and (29) to evaluate experimentally the concurrence of classical and quantum states plotted in Fig. 3a and b.

Measuring the non-separability of vector vortex modes. We applied a tomographic tool to reconstruct the density matrix for the state, so as to analyse the perturbed vector modes. Figure 2a illustrates the experimental set-up used. After passing through the turbulence screen, projective measurements were first performed on the polarization state using a half- and quarter-wave plate, while the OAM DoF was measured using holograms encoded onto the SLM. As SLMs are polarization sensitive, a linear polarizer could not be used to measure the polarization states, as is commonly performed. Instead, a half-wave plate was inserted before the SLM and rotated to specific orientations to realize a filter for the linear polarization states: horizontal, vertical, diagonal and anti-diagonal. By inserting a quarter-wave plate, the two circularly polarized components were also filtered, resulting in a total of six polarization measurements. Similarly, we created six different holograms on the SLM to represent the two pure OAM modes as well as four orientations of the superposition states:  $|\ell = 1\rangle + \exp(i\theta)|\ell = -1\rangle$ , for  $\theta = 0,\pi /2,\pi ,3\pi /2$ . A modal decomposition was performed for each polarization state. This tomographic method produces an over-complete set of 36 measurements, which can be used to minimize the  $\chi$ -square quantity and reconstruct the density matrix  $\rho$  (ref. 49). The concurrence can then be calculated from equation (28).

Computing the fidelity between two states. In quantum mechanics, the fidelity is a measure of the degree of similitude between an arbitrary state with density matrix  $\rho$ , and a target state with density matrix  $\rho_{t}$ . It is defined as

$$
F \left(\rho , \rho_ {t}\right) = \left[ \operatorname {T r} \left\{\sqrt {\sqrt {\rho_ {t}} \rho \sqrt {\rho_ {t}}} \right\} \right] ^ {2} \tag {30}
$$

In our case, we measured the fidelity of a perturbed state  $|\Psi_{\ell}\rangle_{\mathrm{out}}$  with respect to a maximally entangled Bell state  $|\Phi\rangle$ , for which the density matrix  $\rho_{t} = |\Phi\rangle \langle \Phi|$ , reducing the expression of the fidelity to

$$
F (\rho , \rho_ {t}) = \langle \Phi | \rho | \Phi \rangle \tag {31}
$$

Modelling the concurrence with respect to the turbulence strength. The decay of the concurrence of our quantum state can be modelled in terms of the turbulence strength of the channel. Here we consider a turbulence model based on Kolmogorov's theory, and use the Strehl ratio (SR) as our measure of the turbulence strength. This parameter is defined as the ratio of the on-axis mean irradiance from a point source measured at the plane of a receiver in the presence of turbulence, to that with no turbulence. Assuming weak irradiance fluctuations, we express the turbulence strength SR as<sup>50</sup>

$$
\mathrm {S R} \approx \frac {1}{1 + \left(D / r _ {0}\right) ^ {5 / 3}} \tag {32}
$$

where SR is the Strehl ratio,  $D$  is the diameter of the receiving aperture, and  $r_0$  is the Fried parameter $^{51}$ , given by

$$
r _ {0} = 0. 1 8 5 \left(\frac {\lambda^ {2}}{C _ {n} ^ {2} z}\right) ^ {3 / 5} \tag {33}
$$

Although equation (32) is valid for weak irradiance fluctuations, it has not been derived for a single-phase-screen scenario, which is the case for the current experimental set-up. One can compute the Strehl ratio for a single phase screen, using the quadratic structure function approximation<sup>52</sup>. The resulting expression

$$
\mathrm {S R} = \frac {1}{1 + 6 . 8 8 \left(w _ {0} / r _ {0}\right) ^ {2}} \tag {34}
$$

is similar to equation (32). Here  $w_{0}$  is the beam radius of the input beam. We will assume that, without the quadratic structure function approximation, the relationship is of the form

$$
\mathrm {S R} = \frac {1}{1 + 6 . 8 8 \left(w _ {0} / r _ {0}\right) ^ {5 / 3}} \tag {35}
$$

The concurrence of a photon pair that has an initial entangled state (Bell state)

$$
\left| \Psi^ {+} \right\rangle = \frac {1}{\sqrt {2}} (| \ell \rangle | - \ell \rangle + | - \ell \rangle | \ell \rangle) \tag {36}
$$

and where only one photon propagates through single-phase-screen turbulence, evolves according to

$$
\mathcal {C} \left(\left| \Psi^ {+} \right\rangle\right) = \frac {X + 1}{X ^ {2} + X + 1} \tag {37}
$$

where

$$
X = 6. 8 8 \left(w _ {0} / r _ {0}\right) ^ {5 / 3} \tag {38}
$$

Using equation (35), we can express  $X$  in terms of the Strehl ratio

$$
X = \frac {1}{\mathrm {S R}} - 1 \tag {39}
$$

so that equation (37) becomes

$$
\mathcal {C} \left(\left| \Psi^ {+} \right\rangle\right) = \frac {\mathrm {S R}}{\mathrm {S R} ^ {2} - \mathrm {S R} + 1} \tag {40}
$$

Quantum experiment: single photon through turbulence. The quantum results in Fig. 3a were obtained by performing an experiment similar to that in ref. 20. A  $3\mathrm{mm}$  BBO crystal was pumped with a picosecond laser with wavelength of  $355\mathrm{nm}$  and an average power of  $350\mathrm{mW}$  to produce non-collinear, degenerate entangled photon pairs with type I phase matching via SPDC. Each photon was directed onto a SLM where the conjugate of the modes to be measured and the turbulence was encoded. The modulated beams were then coupled into single-mode fibres (SMF), which extract the Gaussian profile from the beams. Avalanche photodiodes were used to register the presence of photon pairs from the SMFs via a coincidence counter.

Data availability. The data that support the plots within this paper and other findings of this study are available from the corresponding author upon reasonable request.

# References

49. Jack, B., Leach, J., Ritsch, H., Barnett, S. & Padgett, M. Precise quantum tomography of photon pairs with entangled orbital angular momentum. New J. Phys. 811, 103024 (2009).  
50. Andrews, L. C. & Phillips, R. L. Laser Beam Propagation through Random Media (SPIE Press, 1998).  
51. Fried, D. L. Optical resolution through a randomly inhomogeneous medium for very long and very short exposures. J. Opt. Soc. Am. 56, 1372-1379 (1966).  
52. Leader, J. C. Atmospheric propagation of partially coherent radiation. J. Opt. Soc. Am. 68, 175-185 (1978).