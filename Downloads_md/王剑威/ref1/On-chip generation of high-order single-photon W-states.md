# On-chip generation of high-order single-photon W-states

Markus Gräfe<sup>1†</sup>, René Heilmann<sup>1†</sup>, Armando Perez-Leija<sup>1†</sup>, Robert Keil<sup>1,2</sup>, Felix Dreisow<sup>1</sup>, Matthias Heinrich<sup>1,3</sup>, Hector Moya-Cessa<sup>4</sup>, Stefan Nolte<sup>1</sup>, Demetrios N. Christodoulides<sup>3</sup> and Alexander Szameit<sup>1*</sup>

Quantum superposition is the quantum-mechanical property of a particle whereby it inhabits several of its possible quantum states simultaneously. Ideally, this permissible coexistence of quantum states, as defined on any degree of freedom, whether spin, frequency or spatial, can be used to fully exploit the information capacity of the associated physical system. In quantum optics, single photons are the quanta of light, and their coherence properties allow them to establish entangled superpositions between a large number of channels, making them favourable for realizations of quantum information processing schemes. In particular, single-photon W-states (that is, states exhibiting a uniform distribution of the photons across multiple modes) represent a class of multipartite maximally-entangled quantum states that are highly robust to dissipation. Here, we report on the generation and verification of single-photon W-states involving up to 16 spatial modes, and exploit their underlying multi-mode superposition for the on-chip generation of genuine random numbers.

Entanglement is one of the cornerstones of quantum mechanics. Its ability to inextricably link two or more seemingly separate entities lies at the heart of some of the most counter-intuitive quantum-inspired applications such as teleportation and quantum cryptography $^{1-4}$ . Yet, despite its profound and multi-faceted implications, entanglement may often be a fragile quality when losses are involved. It is precisely for this reason that a certain class of maximally entangled multipartite configurations—the so-called W-states—has recently attracted considerable attention in the field of quantum computing and information science. These W-states are characterized by a coherent superposition of all the qubits involved, with equal probability amplitudes. As it turns out, such configurations exhibit the remarkable property of being intrinsically robust with respect to decoherence. Initially introduced for a three-qubit system $^{5}$ , this concept can be readily generalized to ensembles of  $N$  entangled qubits $^{6}$ . By virtue of their unique characteristics, quantum-optical W-states have since been suggested as a testbed for exploring fundamental aspects associated with the non-locality of single-particle quantum states $^{7-15}$ . In their quantum optical representation, W-states describe configurations where single photons are coherently distributed among  $N$  spatially separated paths, or modes $^{16,17}$ . In combination with the field coherence afforded by optics, such spatial quantum 'parallelism' holds great promise for a number of applications, ranging from complex quantum networks to robust quantum key distribution and communication schemes $^{17}$ . Along similar lines, it was recently demonstrated that single-photon W-states, when used as non-classical probes, can in principle facilitate the error-free readout of an arbitrary number of classical bits $^{18}$ . Up to now, the preparation of higher-order W-states of light has remained a challenging task, often involving complex bulk-optical set-ups $^{16,18-20}$ . Clearly of interest will be the development of new

strategies through which quantum optical W-states can be reliably and efficiently synthesized on an integrated platform.

In the present work, we experimentally realize high-order W-states by judiciously manipulating the dynamic evolution of photons in systems of evanescently coupled waveguides[21,22]. In doing so, we transform a single photon launched at the input of the device into a uniform coherent superposition of spatial modes. As a result, the initially localized photon emerges through any of the  $N$  output ports of the integrated device with exactly the same probability. To this end, two complementary approaches are presented that are capable of producing either even or odd single-photon W-states of, in principle, arbitrarily large order. Finally, we propose, implement and verify a W-state-based scheme for the direct generation of random bit sequences without the need for post-processing, and the capability for high bit rates due to the multiple output modes[23-27].

# Generation of single-photon W-states

The uniform coherent distribution of a single photon over an ensemble of  $N$  channels corresponding to a quantum optical W-state  $|W_{N}\rangle$  can be described in terms of the bosonic creation operators  $a_{n}^{\dagger}$  of the respective waveguide's modes  $n = 1\ldots N$  as  $|W_{N}\rangle = N^{-1 / 2}\sum_{n = 1}^{N}\exp (i\phi_{n})a_{n}^{\dagger}|0\rangle$ . In this context,  $\phi_{n}$  are arbitrary relative phases and  $|0\rangle$  denotes the vacuum state of the system. Let us first consider the case of an odd number  $N = 2c - 1$  of channels. By virtue of the coupling taking place between adjacent channels, a single photon state  $a_{c}^{\dagger}|0\rangle$  launched into the central waveguide  $c$  is gradually distributed across the lattice. This propagation along the longitudinal coordinate  $z$  is governed by the evolution operator,  $U(z) = \exp (-iz\mathcal{M})$ , where  $\mathcal{M}$  represents the  $z$ -invariant coupling matrix. This formalism is identical to the one employed in continuous-time quantum walks[21,28]. The resulting state at a given  $z$  is characterized by the

![](images/687dc35913b4e4bf08e43d2419c4ca5667488e5cd45d79d8371581d7528ab556.jpg)  
Figure 1 | Schematic of the experimental set-up. A heralded single-photon source at a wavelength of  $815\mathrm{nm}$  was implemented by means of spontaneous parametric downconversion from a pump laser at  $407.5\mathrm{nm}$ . Photons emerging at the output of the device were collected via a fibre array and subsequently fed into single-photon detectors (avalanche photodiodes, APDs) triggered by the herald.

complex probability amplitudes  $U_{c,n}(z)$

$$
| \psi (z) \rangle = \left(\sum_ {n = 1} ^ {N} U _ {c, n} (z) a _ {n} ^ {\dagger}\right) | 0 \rangle \tag {1}
$$

Evidently,  $|\psi \rangle$  becomes a W-state when  $\left|U_{c,1}(z_{\mathrm{W}})\right|^2 = \dots = \left|U_{c,N}(z_{\mathrm{W}})\right|^2$ ; that is, the probability of detecting this photon is the same for all sites at a specific propagation distance  $z_{\mathrm{W}}$ . As recently shown, this condition can indeed be fulfilled for any arbitrary odd number of elements  $N$  by appropriately varying the coupling strengths in a symmetric fashion around site  $c$  (ref. 29).

Naturally, in systems with an even number  $N$  of channels, no such central site exists around which a symmetric evolution  $U_{c,n}(z) = U_{c,N - n + 1}(z)$  may be realized. To overcome this challenge, we break the  $z$ -invariance of the system by selectively enabling or suppressing the tunnelling of photons between specific lattice sites. In doing so, we make use of the fact that the coherent evolution in a pair of coupled waveguides periodically gives rise to entangled states of the type  $|\psi (z_{\mathrm{BS}} / 2)\rangle = 2^{-1 / 2}(|10\rangle +i|01\rangle)$ . We note that one can therefore obtain the state  $|W_2\rangle$  by terminating the interaction between the channels at half a beating length  $z_{\mathrm{BS}}$ . It readily follows that any even-numbered W-state  $|W_N\rangle$  with  $N = 2^m$  can be generated directly by cascading  $m$  stages of such integrated 50/50 couplers, or 'beamsplitters<sup>30</sup>, without the need for any post-selection process.

To demonstrate the feasibility of these approaches, we implemented systems for the generation of single-photon W-states spanning  $N = 2,4,5,8$  and 16 channels, respectively, by means of the femtosecond laser writing technique in fused silica glass[22,31-34]. The devices were used in conjunction with heralded single photons obtained by spontaneous parametric downconversion[35] in a  $\mathrm{BiB}_3\mathrm{O}_6$  crystal. A commercial V-groove fibre array was used to collect the photons from the individual output ports to be counted and then feed them to the respective avalanche photodiodes (Fig. 1). Subsequently, the photon probability distribution  $P_{n} = \langle a_{n}^{\dagger}a_{n}\rangle$  was obtained from the count rates. We determined the ratio of two count events compared to single click events to be  $10^{-4}$  at the output of the system used for  $N = 2,4$  and 8, which guarantees that multiphoton events have no significant influence on the measured statistics. As the ratio of single clicks to zero-photon events (that is, isolated detections of a herald photon) was measured to be 0.03, the possibility of weak coherent input states can be faithfully excluded. Similar ratios were obtained for the other devices. Moreover, by applying a herald as trigger, the ratio of dark counts to heralded counts is  $10^{-9}$ , so the dark counts have a negligible influence on the

measurements. All arrangements were fabricated to match the standard fibre array spacing of  $127\mu \mathrm{m}$  at the output facet. In the case of the  $N = 5$  configuration, this was achieved by means of a three-dimensional fan-out interface structure designed to effectively suppress any additional crosstalk between the guides (Fig. 2a). Following the method outlined in ref. 29, the inter-channel coupling coefficients in the  $N = 5$  arrangement were chosen in accordance with a length  $z_{\mathrm{W}} = 5\mathrm{cm}$  of the functional region. Figure 2c shows the photon probability distribution measured at the output facet, illustrating the high fidelity of the device with  $\bar{P}_{N=5}=(20.0\pm0.9)\%$

Taking into account the hierarchical nature of the even-  $N$  configuration, we designed a discrete network of integrated 50/50 couplers that allows for the synthesis of two-, four- or eight-partite W-states by selecting the appropriate input channel of the device (Fig. 2b). For instance, if a single photon is coupled to input port 1, it encounters a single beamsplitter, yielding  $|W_{2}\rangle = 2^{-1 / 2}(a_{1}^{\dagger} + ia_{2}^{\dagger})|0\rangle$ . Input port 2, on the other hand, conveys the photon to two consecutive stages of couplers. The output state is thus given by  $|W_{4}\rangle = 4^{-1 / 2}(ia_{1}^{\dagger} + a_{2}^{\dagger} + ia_{3}^{\dagger} - a_{4}^{\dagger})|0\rangle$ . Similarly, input port 3 yields the state

$$
\left| W _ {8} \right\rangle = 8 ^ {- 1 / 2} \left(- a _ {1} ^ {\dagger} + i a _ {2} ^ {\dagger} + a _ {3} ^ {\dagger} + i a _ {4} ^ {\dagger} - a _ {5} ^ {\dagger} + i a _ {6} ^ {\dagger} - a _ {7} ^ {\dagger} - i a _ {8} ^ {\dagger}\right) | 0 \rangle \tag {2}
$$

Making use of the vertical degree of freedom, we realized a network facilitating the entanglement of 16 modes in two planes connected via a vertical coupler. Note that, in contrast to discrete-step quantum walks $^{33,36}$ , no interference occurs between the individual instances during the build-up of the W-state. Figure 2c shows the experimentally measured photon number probability distributions for  $|W_{2}\rangle$ ,  $|W_{4}\rangle$ ,  $|W_{8}\rangle$  and  $|W_{16}\rangle$ . As in the  $|W_{5}\rangle$  device, the high uniformity in the output probabilities, that is,  $\bar{P}_{N=2} = (50.0 \pm 0.5)\%$ ,  $\bar{P}_{N=4} = (25.0 \pm 0.5)\%$ ,  $\bar{P}_{N=8} = (12.5 \pm 0.7)\%$  and  $\bar{P}_{N=16} = (6.25 \pm 0.8)\%$ , is indicative of the fidelity of the device. The standard deviations given here represent the deviations from the ideal uniform probability distribution, which are mainly caused by the fabrication tolerances of the device. In contrast, the Poissonian count statistics would yield much smaller uncertainties, for example,  $\pm 0.02\%$  in the case of  $N = 8$ .

# Verification of multipartite entanglement

Conventionally, W-states are identified by means of state tomography. Given that the complexity of this approach dramatically increases with the number of entangled qubits, it is desirable to find an alternative characterization scheme with more favourable scaling behaviour.

![](images/b1efb3f7a9cd6368abaa4c97fac54fcccd85e1576135574d23334676dc5bae26.jpg)

![](images/9e4a92a5109772d81fd2c161a227553d865ea43292b37d2cdaf64d2bacbaac42.jpg)  
Figure 2 | Generation of high-order photonic W-states on an integrated platform. a, Odd number  $N$  of entangled channels. Here, the  $|W_5\rangle$  state is obtained through the coherent evolution of a single photon injected into the central site of a lattice comprising  $N$  identical waveguides. Appropriately engineered couplings continuously transform the initially localized photon into the desired equal superposition of all  $N$  channels after distance  $z_{\mathrm{W}}$ . Subsequently, a fan-out section designed to arrest the propagation dynamics serves as an interface to the output ports. b, Even number  $N$  of entangled channels. A hierarchical network of 50/50 couplers transforms the single-photon input state into W-states of order  $N = 2^m$ , where  $m$  is the number of sequential couplers. The specific structure shown here is capable of producing any of states  $|W_2\rangle$ ,  $|W_4\rangle$  and  $|W_8\rangle$ , depending on the choice of input port. c, Experimentally obtained probability distributions of states  $|W_2\rangle$ ,  $|W_4\rangle$ ,  $|W_5\rangle$ ,  $|W_8\rangle$  and  $|W_{16}\rangle$ . In the  $N = 5$  case, the length of the functional section was  $z_{\mathrm{W}} = 5 \mathrm{~cm}$ . The system used to synthesize the  $N = 16$  state consisted of a pair of realizations of the structure in b arranged in parallel horizontal planes and connected to the input by a vertical 50/50 coupler. Standard deviations (from the uniform distribution) of the individual measurements are shown as horizontal bars.

To this end, we make use of our a priori knowledge that the output state is the result of the evolution of a single-photon state. To provide unequivocal evidence that the produced states are indeed W-states (that is, coherent superpositions of single-photon states), we therefore verify that coherence is preserved during propagation. In other words, if W-states are considered as an input for a linear optical system (for example, an optical interferometer), the response in terms of the average photon number distribution will be given by the modulus square of the coherent sum of that system's Green's functions. This impulse response describes the individual output distributions corresponding to each single-mode state of which the W-state is composed[16,37]. In contrast, when the same optical system is excited by an incoherent mixture of single-waveguide Fock states, its response will be described by the incoherent sum of the average photon number distributions arising from the individual Fock state excitations of the system.

Along these lines, we make use of interferometric arrangements based on coupled waveguides. Interestingly, the very unitary  $U(z_{\mathrm{W}})$  used to synthesize the  $N = 5$  state displays a high sensitivity with respect to the coherence of an input state (Fig. 3a). The analytical model shows that an incoherent excitation would result in a uniform distribution over all channels at the interferometer output (Fig. 3b, top right). Due to the symmetry of  $U(z_{\mathrm{W}})$ , this condition can be experimentally mimicked by separately injecting (at  $z = 0$ ) single photons into all input channels of the interferometer and

summing all individually measured average photon number distributions at  $z = 2z_{\mathrm{W}}$  (Fig. 3b, bottom right). In contrast, after propagating a distance  $z_{\mathrm{W}}$ , the coherent W-state should yield the characteristic interference pattern shown in Fig. 3b (top left). Indeed, the measured average photon number distribution (Fig. 3b, bottom left) closely matches the theoretical predictions, strongly indicating that the device in fact produces the desired W-state  $|W_5\rangle$ .

Following a different approach in the even- $N$  arrangement, we directly verify multipartite entanglement for  $W$ -state  $|W_8\rangle$ . For this purpose we follow a scheme similar to the one described in ref. 38, where one applies a projection into a basis of  $N$  orthogonal  $W$ -states (all varying in their phase distribution), including the desired state (equation (2)). This is achieved by a unitary transformation  $U$ , which maps each of the  $W$ -states to a specific output channel, in our case the desired state to the eighth mode  $U|W_8\rangle = |0_1,0_2,\dots,1_8\rangle = a_8^\dagger |0\rangle$ . The density matrix of an unknown state  $\rho$  will evolve as  $\tilde{\rho} = U\rho U^{\dagger}$ , such that its fidelity with  $|W_8\rangle$  is given by the count rate in the eighth channel:

$$
\begin{array}{l} \mathcal {F} = \left\langle W _ {8} | \rho | W _ {8} \right\rangle = \left\langle W _ {8} | U ^ {\dagger} U \rho U ^ {\dagger} U | W _ {8} \right\rangle \\ = \left\langle 0 _ {1}, 0 _ {2}, \dots , 1 _ {8} \right| \tilde {p} \left| 0 _ {1}, 0 _ {2}, \dots , 1 _ {8} \right\rangle = \tilde {\rho} _ {8 8} \tag {3} \\ \end{array}
$$

It can be shown that all biseparable states have to satisfy the condition  $\mathcal{F} \leq (N - 1) / N$  (refs 39,40). Hence, a violation of this

![](images/bd1c9f596f4c8dc20d67e340bc3e35994a8713bb5c80970f287cc748f8c3d2a7.jpg)  
a

![](images/e5870a31478ecd7b1115a243d7dcf55ec8734d65b1e337deda4c325f5c9555ae.jpg)  
b

![](images/0ddc95047b4c3edb7f8ee864c5886ae1386b448427b4e5538067062b92488770.jpg)  
Incoherent mixture

![](images/d9e6e993b9047fba86c5749420cc14a1a45884fc08123a680ce345b4dd93fe74.jpg)  
Figure 3 | Interferometric validation of W-states, given a priori knowledge of a single-photon input state. a, To demonstrate coherence between the outputs of the  $N = 5$  device, we allowed the created state to undergo interference while propagating through a second section of length  $z_{\mathrm{W}}$  before separating the channels in the fan-out arrangement. b, Theoretical probability distributions (top row) assuming coherent (left) or fully incoherent (right) conditions at the end of the functional section. The measured interferogram (bottom, left) proves a coherent superposition of the channels, that is, state  $|W_5\rangle$ . As a comparison, the incoherent case, with its characteristic absence of interference, was observed by subsequently launching single photons into each channel of the array (alternating colour) and adding the probability distributions, incoherently (bottom right). c, In the  $N = 8$  case, an additional sequence of integrated 50/50 couplers were attached to verify entanglement of the  $|W_8\rangle$  output. d, The theoretical output probability distribution of this arrangement under perfect conditions exhibits a projection to only one output (top); the experimental results clearly exceed the required fidelity condition of 7/8 (bottom).

![](images/8a59dfa4509204037a594d4a3d86a57a724edaef8ec7f678630894a5b6be83b1.jpg)  
d

fidelity criterion is a sufficient condition for the presence of genuine  $N$ -mode entanglement in state  $\rho$ .

In this vein we fabricated an interferometric set-up to provide unitary  $U$  (Fig. 3c). The fidelity is then simply given by the detection probability in channel eight. By attaching the interferometer to the chip used for the generation of  $|W_8\rangle$ , we experimentally obtained  $\mathcal{F} = 0.918 \pm 0.004 > 7/8$ , which clearly violates the criterion and thus proves the eight-mode entanglement of the  $|W_8\rangle$  state. Note that, although the deviation from unity is mainly caused by deviations from the uniform probability distribution, the uncertainty of the fidelity is determined by the Poissonian count statistics in the output channels of the verification device.

# Generation of genuine random numbers

Finally, we demonstrate a direct application of the W-state generation scheme by exploiting the intrinsic uncertainty in the uniform photon number distribution of the synthesized state  $|W_8\rangle$  for the generation of genuine random numbers. To this end, we associate a number  $m = n - 1$ , with  $n\in [1,8]$ , to every successful detection of a photon at output port  $n$ , which corresponds to a three-digit binary number. It follows that random numbers with more than three digits can be readily obtained by concatenating the results of multiple measurements. We note that, for a given

number of output channels  $N$ , the largest number presentable by  $M$  measurements scales as  $N^M$ . In our  $|W_8\rangle$  arrangement, a measurement of merely three photons can yield a random number between 0 and  $8^3 - 1 = 511$ , whereas by using a  $|W_{16}\rangle$  state one could span the range 0 ... 4,095. In comparison to existing two-mode schemes[25], this provides the advantage of an increased bit rate for a given photon flux. Moreover, as the latter cannot be increased arbitrarily due to detector saturation, the multimodal scheme offers a larger maximally attainable bit rate for a given detector technology. Importantly, this method for W-state-based random bit generation only requires the conversion from photon counting to the digital format, and no post-processing. The maximum deviation from the ideal 50/50 ratio between 'zeros' and 'ones' in our experiment was found to be  $3.444 \times 10^{-4}$  for a sample sequence of 1 Mbit at an average rate of  $60~\mathrm{kbit~s^{-1}}$ . The true statistical randomness of this implementation was verified by using the standard statistical test suite for random number generators provided by NIST[41] to characterize an arbitrarily chosen bit sequence (see Supplementary Information). We emphasize that the bit-generation rate in our setting is limited only by the fluence of the single-photon source and the speed of the photon-counting circuitry, and not by the photonic system utilized in generating the W-states. Hence, the bit-generation rate can be readily improved

by several orders of magnitude, as brighter single-photon sources and gigahertz single-photon sources and photon-counting circuitry become more available<sup>42</sup>.

# Conclusions

We have successfully demonstrated the generation of high-order optical single-photon W-states for odd  $(N = 5)$  as well as even  $(N = 2, 4, 8, 16)$  numbers of entangled channels. Our approach provides a robust, monolithically integrated solution to this task, and the number of modes can be readily tuned. For the case of  $N = 8$ , we measured a fidelity of  $91.8\%$  between the output and target state  $|W_8\rangle$ . This exceeds the upper bound for biseparable states, thus verifying entanglement among all modes. Subsequently, we utilized the intrinsic properties of multipartite W-states to generate quantum-based random numbers. Our results may pave the way towards the robust and versatile sources needed for the wide-scale deployment of quantum-cryptographic communication protocols.

Received 6 December 2013; accepted 23 July 2014; published online 31 August 2014; corrected online 18 September 2014

# References

1. Walter, M., Doran, B., Gross, D. & Christandl, M. Entanglement polytopes: multipartite entanglement from single-particle information. Science 340, 1205-1208 (2013).  
2. Afek, I., Ambar, O. & Silberberg, Y. High-NOON states by mixing quantum and classical light. Science 328, 879-881 (2010).  
3. Riedel, M. F. et al. Atom-chip-based generation of entanglement for quantum metrology. Nature 464, 1170-1173 (2010).  
4. Carteret, H. A., Linden, N., Popescu, S. & Sudbery, A. Multiparticle entanglement. Found. Phys. 29, 527-552 (1999).  
5. Dur, W., Vidal, G. & Cirac, J. I. Three qubits can be entangled in two inequivalent ways. Phys. Rev. A 62, 062314 (2000).  
6. Häffner, H. et al. Scalable multiparticle entanglement of trapped ions. Nature 438, 643-646 (2005).  
7. Morin, O. et al. Witnessing trustworthy single-photon entanglement with local homodyne measurements. Phys. Rev. Lett. 110, 130401 (2013).  
8. Brask, J. B., Chaves, R. & Brunner, N. Testing nonlocality of a single photon without a shared reference frame. Phys. Rev. A 88, 012111 (2013).  
9. Cunningham, J. & Vedral, V. Nonlocality of a single particle. Phys. Rev. Lett. 99, 180404 (2007).  
10. Aharonov, Y. & Vaidman, L. Nonlocal aspects of a quantum wave. Phys. Rev. A 61, 052108 (2000).  
11. Banaszek, K. & Wódkiewicz, K. Testing quantum nonlocality in phase space. Phys. Rev. Lett. 82, 2009-2013 (1999).  
12. Yuan, H. et al. Deterministic secure quantum communication with four-qubit W states. Int. J. Quant. Inf. 9, 607-614 (2011).  
13. Shi, B. & Tomita, A. Teleportation of an unknown state by W state. Phys. Lett. A 296, 161-164 (2002).  
14. Joo, J., Park, Y., Oh, S. & Kim, J. Quantum teleportation via a W state. New J. Phys. 5, 136 (2005).  
15. Bruß, D. et al. Optimal universal and state-dependent quantum cloning. Phys. Rev. A 57, 2368-2378 (1998).  
16. Rai, A. & Agarwal, G. S. Possibility of coherent phenomena such as Bloch oscillations with single photons via W states. Phys. Rev. A 79, 053849 (2009).  
17. Fujii, K., Maeda, H. & Yamamoto, K. Robust and scalable scheme to generate large-scale entanglement webs. Phys. Rev. A 83, 050303 (2011).  
18. Guha, S. & Shapiro, J. H. Reading boundless error-free bits using a single photon. Phys. Rev. A 87, 062306 (2013).  
19. Papp, S. B. et al. Characterization of multipartite entanglement for one photon shared among four optical modes. Science 324, 764-768 (2009).  
20. Choi, K. S., Goban, A., Papp, S. B., van Enk, S. J. & Kimble, H. J. Entanglement of spin waves among four quantum memories. Nature 468, 412-416 (2010).  
21. Bromberg, Y., Lahini, Y., Morandotti, R. & Silberberg, Y. Quantum and classical correlations in waveguide lattices. Phys. Rev. Lett. 102, 253904 (2009).

22. Szameit, A., Dreisow, F., Pertsch, T., Nolte, S. & Tünnermann, A. Control of directional evanescent coupling in fs laser written waveguides. Opt. Express 15, 1579-1587 (2007).  
23. Uchida, A. et al. Fast physical random bit generation with chaotic semiconductor lasers. Nature Photon. 2, 728-732 (2008).  
24. Kanter, I., Aviad, Y., Reidler, I., Cohen, E. & Rosenbluh, M. An optical ultrafast random bit generator. Nature Photon. 4, 58-61 (2010).  
25. Jennewein, T., Achleitner, U., Weihs, G., Weinfurter, H. & Zeilinger, A. A fast and compact quantum random number generator. Rev. Sci. Instrum. 71, 1675-1680 (2000).  
26. Pironio, S. et al. Random numbers certified by Bell's theorem. Nature 464, 1021-1024 (2010).  
27. Kwon, O., Cho, Y. W. & Kim, Y. H. Quantum random number generator using photon-number path entanglement. Appl. Opt. 48, 1774-1778 (2009).  
28. Di Giuseppe, G. et al. Einstein-Podolsky-Rosen spatial entanglement in ordered and Anderson photonic lattices. Phys. Rev. Lett. 110, 150503 (2013).  
29. Perez-Leija, A., Hernandez-Herrejon, J. C., Moya-Cessa, H., Szameit, A. & Christodoulides, D. N. Generating photon-encoded W states in multiport waveguide-array systems. Phys. Rev. A 87, 013842 (2013).  
30. Politi, A., Cryan, M. J., Rarity, J. G., Yu, S. & O'Brien, J. L. Silica-on-silicon waveguide quantum circuits. Science 320, 646-649 (2008).  
31. Itoh, K., Watanabe, W., Nolte, S. & Schaffer, C. B. Ultrafast processes for bulk modification of transparent materials. MRS Bull. 31, 620-625 (2006).  
32. Marshall, G. D. et al. Laser written waveguide photonic quantum circuits. Opt. Express 17, 12546-12554 (2009).  
33. Sansoni, L. et al. Two-particle bosonic-fermionic quantum walk via integrated photonics. Phys. Rev. Lett. 108, 010502 (2012).  
34. Heilmann, R., Grafé, M., Nolte, S. & Szameit, A. Arbitrary photonic wave plate operations on chip: realizing Hadamard, Pauli-X, and rotation gates for polarisation qubit. Sci. Rep. 4, 4118 (2014).  
35. Abouraddy, A. F., Nasr, M. B., Saleh, B. E. A., Sergienko, A. V. & Teich, M. C. Demonstration of the complementarity of one- and two-photon interference. Phys. Rev. A 63, 063803 (2001).  
36. Kitagawa, T. et al. Observation of topologically protected bound states in photonic quantum walks. Nature Commun. 3, 882 (2012).  
37. Mandel, L. Coherence and indistinguishability. Opt. Lett. 16, 1882-1883 (1991).  
38. Lougovski, P. et al. Verifying multipartite mode entanglement of W states. New J. Phys. 11, 063029 (2009).  
39. Nha, H. Linear optical scheme to demonstrate genuine multipartite entanglement for single-particle W states. Phys. Rev. A 77, 062328 (2008).  
40. Gühne, O. & Toth, G. Entanglement detection. Phys. Rep. 474, 1-75 (2009).  
41. Rukhin, A. et al. A Statistical Test Suite for Random and Pseudorandom Number Generators for Cryptographic Applications (revised) (National Institute of Standards and Technology (U.S.) Special Publication 800-22rev1, 2010); available at http://csrc.nist.gov/groups/ST/toolkit/rng/documentation/software.html.  
42. Murphy, T. E. & Roy, R. Chaotic lasers: the world's fastest dice. Nature Photon. 2, 714-715 (2008).

# Acknowledgements

The authors thank K. Schwaiger, B. Kraus and G. Weihs for helpful discussions. Financial support by the German Ministry of Education and Research (Center for Innovation Competence programme, grant no. 03Z1HN31), the Thuringian Ministry for Education, Science and Culture (Research group Spacetime, grant no. 11027-514), the Deutsche Forschungsgemeinschaft (grant no. NO462/6-1), the German-Israeli Foundation for Scientific Research and Development (grant no. 1157-127.14/2011) and the M. Heinrich was supported by the German National Academy of Sciences Leopoldina (grant no. LPDS 2012-01) is gratefully acknowledged.

# Author contributions

M.G., R.H., A.P.-L. and D.N.C. conceived the idea. M.G., R.H and R.K. designed the samples and performed the measurements. A.P.-L., M.G., R.H and R.K. analysed the data. A.S. supervised the project. All authors discussed the results and co-wrote the manuscript.

# Additional information

Supplementary information is available in the online version of the paper. Reprints and permissions information is available online at www.nature.com/reprints. Correspondence and requests for materials should be addressed to A.S.

# Competing financial interests

The authors declare no competing financial interests.

# CORRIGENDUM

# On-chip generation of high-order single-photon W-states

Markus Grafe, René Heilmann, Armando Perez-Leija, Robert Keil, Felix Dreisow, Matthias Heinrich, Hector Moya-Cessa, Stefan Nolte, Demetrios N. Christodoulides and Alexander Szameit

Nature Photonics 8, 791-795 (2014); published online 31 August 2014; corrected online 18 September 2014.

In the version of this Article originally published, the contribution of Demetrios N. Christodoulides to conceiving the idea behind the work was not acknowledged in the Author Contributions section. This error has now been corrected in the HTML and PDF versions of the Article.