# Unscrambling entanglement through a complex medium

Natalia Herrera Valencia  $①$ ☑, Suraj Goel  $①$ , Will McCutcheon $^{1,2}$ , Hugo Defienne  $③$  and Mehul Malik  $①$ ,

The transfer of quantum information through a noisy environment is a central challenge in the fields of quantum communication, imaging and nanophotonics. In particular, high-dimensional quantum states of light enable quantum networks with significantly higher information capacities and noise robustness as compared with qubits. However, although qubit entanglement has been distributed over large distances through free space and fibre, the transport of high-dimensional entanglement is hindered by the complexity of the channel, which encompasses effects such as free-space turbulence or mode mixing in multimode waveguides. Here, we demonstrate the transport of six-dimensional spatial-mode entanglement through a 2-m-long, commercial multimode fibre with  $84.4\%$  fidelity. We show how the entanglement can itself be used to measure the transmission matrix of the complex medium, allowing the recovery of quantum correlations that were initially lost. Using a unique property of entangled states, the medium is rendered transparent to entanglement by carefully 'scrambling' the photon that did not enter it, rather than unscrambling the photon that did. Our work overcomes a primary challenge in the fields of quantum communication and imaging, and opens a new pathway towards the control of complex scattering processes in the quantum regime.

In recent years, the precise control of light propagation through disordered media has unlocked a range of new possibilities for biomedical imaging and optical telecommunications<sup>1</sup>. The ability to turn a strongly scattering sample into a lens or send an image down an optical fibre no thicker than a human hair promises exciting new technologies such as non-invasive endoscopes and ultra-dense communication systems<sup>2-4</sup>. The key to achieving such control over light is the ability to measure the transmission matrix of a complex medium—a matrix of complex numbers that describes how the medium maps a set of input modes to a set of output modes<sup>5</sup>. Enabled by the availability of highly tunable digital arrays, the transmission matrix is routinely measured today via the response of the medium to a set of probe states sent one at a time (Fig. 1a). Bringing this powerful technique to the domain of quantum information promises significant advances in quantum state transport and control. Recent experiments have demonstrated this potential by harnessing disorder for the manipulation of photon pairs<sup>6-8</sup> and transporting quantum correlations in a weak scattering regime<sup>9</sup>.

Quantum entanglement plays a central role in the rapidly advancing field of quantum technologies $^{10}$ , enabling techniques such as quantum error correction and device-independent quantum communication $^{11,12}$ . High-dimensional entangled states of light $^{13-16}$  offer vastly improved information capacities $^{17,18}$  and greater resistance to noise $^{19,20}$  over qubit-based quantum communication systems, and serve as a resource in quantum imaging protocols that allow one to image below the shot-noise level $^{21}$  or in an interaction-free manner $^{22}$ . High-dimensional entanglement can also tolerate large amounts of loss in loophole-free tests of nonlocality, holding immense potential for the realization of device-independent quantum communication $^{23,24}$ .

A primary problem to be overcome in all of these applications is the preservation of the delicate quantum correlations found in

entanglement after transmission through a channel. State-of-the-art demonstrations of entanglement transport include the distribution of qubit entanglement over  $1,200\mathrm{km}$  of free space and  $300\mathrm{km}$  of single-mode fibre[25,26], and dispersion-compensated qutrit entanglement over  $1\mathrm{km}$  of few-mode fibre[27]. However, the transport of entanglement through a complex scattering channel such as a multimode fibre (MMF) or biological tissue remains a challenge. Such media involve the complex interplay of hundreds to millions of modes, and the effects of scattering must be overcome in a manner that preserves higher-order quantum coherence between all modes of interest.

Here, we demonstrate the transport of high-dimensional entanglement through a complex medium consisting of a short length of commercial MMF. In our experiment, the effects of scattering on entanglement are reversed by manipulating only the photon that did not enter the medium. To achieve this, we develop a new technique for measuring the transmission matrix of the fibre using the entangled state itself. In contrast to the classical technique of measuring a response function one state at a time, our method exploits the parallelism of entanglement by mapping the entire transmission matrix onto a single, high-dimensionally entangled state. This is known as the Choi-Jamiolkowski isomorphism in quantum mechanics, which says that statements about a channel can be mapped onto statements about a state $^{28-30}$ . Previous experiments have used this isomorphism to characterize qubit processes $^{31}$  and quantum channels through classically non-separable states $^{32}$ . Here we apply it to complex, multimode scattering channels using high-dimensional entangled states, which are natural candidates for it.

One particle of a maximally entangled two-particle state  $|\Phi^{+}\rangle = \frac{1}{\sqrt{d}}\sum_{i}|i\rangle$  is sent through the complex medium with transmission matrix  $\dot{T} = \sum_{ij}t_{ji}|j\rangle \langle i|$  (Fig. 1b). As a result, the two-particle entangled state undergoes a transformation into the pure state

![](images/0c5ef748b605815ff6cce02f1ee9c94beeeb726ad8bacfcf517a577b618a7a64.jpg)

![](images/4fd57524d4981df3c215f22f258d6abbe940e966f5c2407789509ef8261132f7.jpg)

Fig. 1 | Basic principle. a, Classical methods for reconstructing a  $d^2$ -dimensional transmission matrix  $T$  of a complex medium involve the measurement of a response function to a set of  $d$  input probe states  $\{|i\rangle\}$ .  
![](images/50a9b036414721c9482bfa462d49e0e34dd447b0e880c70649d4ef94da9013f3.jpg)  
b, Alternatively, the entire transmission matrix can be mapped onto a single maximally entangled state  $|\varPhi^{+}\rangle$  of equal dimension. c, Information about  $T$  can be used to reverse the effects of scattering by finding a set of propagation-invariant states  $\{\left|\vec{I}\right\rangle\}$ , allowing one to send information through the medium. In the classical case, this involves applying an inverse operator such as  $T^{-1}$  before or after the medium. To reverse the effects of scattering on entanglement, a suitable inverse operator can be applied on the photon that did not enter the medium at all.

![](images/d96b1a145cb6e152d6d160252f6bee7c26add2fae8b76e0dd10df96ca20c3347.jpg)

$$
\left| \Phi \right\rangle_ {T} = (\mathbb {I} \otimes \hat {T}) \left| \Phi^ {+} \right\rangle = \frac {1}{\sqrt {d}} \sum_ {i j} t _ {j i} | i j \rangle \tag {1}
$$

which captures the entire knowledge of the medium's transmission matrix. Upon measuring  $|\varPhi\rangle_T$ , one obtains the complex coefficients corresponding to  $T$ . The transmission matrix is thus obtained by characterizing only one entangled state after it passes through the medium. As a result, this method requires  $d$  times fewer settings for characterizing a complex medium than classical techniques, which require the preparation of  $d$  separate probe states before the medium (Fig. 1a). Interestingly, entanglement is not strictly necessary for this method to work; however, it does provide optimal results<sup>31</sup>.

Once the transmission matrix of a complex medium is known, one can use it to reverse the effects of light scattering through the medium. This is done by either constructing a set of propagation-invariant states or eigenmodes $^{3,33}$  obtained by diagonalizing  $T$  (Fig. 1c), or using the knowledge of  $T$  to directly invert the scrambled light measured after the medium $^{34}$ . Extending this methodology to the problem of unscrambling entanglement through a complex medium leads to an interesting revelation—one can invert the action of the complex medium by either unscrambling the photon that went through it or by carefully 'scrambling' the photon that did not (Fig. 1b). This results from a unique property of maximally entangled states where operations on the state can be equivalently expressed as being applied on either of its two parts $^{35}$ :

$$
\begin{array}{l} \left(\mathbb {I} \otimes T ^ {- 1}\right) \left| \Phi \right\rangle_ {T} = \left(\mathbb {I} \otimes T ^ {- 1} T\right) \left| \Phi^ {+} \right\rangle = \left| \Phi^ {+} \right\rangle \tag {2} \\ = \left(\left(T ^ {- 1}\right) ^ {T} \otimes T\right) \left| \Phi^ {+} \right\rangle = \left| \Phi^ {+} \right\rangle \\ \end{array}
$$

Thus, two-particle correlations lost due to one particle scattering through the medium are recovered by only manipulating the particle

that did not enter the medium at all. This can also be understood as a consequence of the invariance of state  $|\Phi^{+}\rangle$  under transformations  $(U\otimes U^{*})$  for any unitary operator  $U$ , which has been implicit in previous work on two-photon speckle<sup>36</sup> and used for the nonlocal cancellation of dispersion and weak scattering<sup>37,38</sup>.

Although inverting the transmission matrix in this manner allows us to regain correlations in one basis, it does not guarantee that the state is entangled. To certify entanglement, one must be able to measure correlations in at least two complementary observables or mutually unbiased bases (MUBs) of the state Hilbert space $^{39,40}$ . Our measurement of  $T$  relies on the assumption that the entangled state after the medium is pure  $\left|\varPhi \right\rangle_T$  in equation (1). Once  $T$  is estimated, we must drop this assumption and use the measured  $T$  to check how close to pure the transmitted state  $(\rho_{T})$  actually is. To do so, we rotate our measured transmission matrix to any MUB, that is  $T_{M} = M^{*}TM^{T}$ , where  $M$  is a complex matrix that performs the specified MUB transformation. Next, we use  $T_{M}$  to construct a second 'scrambling' operator on Alice, that should, in principle, allow us to recover correlations in the basis  $M$  after transmission through the complex medium:

$$
\left(\left(T _ {M} ^ {- 1}\right) ^ {T} M \otimes M ^ {*}\right) | \Phi \rangle_ {T} = | \Phi^ {+} \rangle \tag {3}
$$

Measurements in two or more mutually unbiased bases allow the use of a recently developed entanglement witness for certifying high-dimensional entanglement<sup>14</sup>. Using this witness, we are able to lower bound the fidelity of the state to a given pure target state via measurements in two MUBs and certify entanglement dimensionality via a Schmidt number bound<sup>41</sup>. Measurements in all MUBs allow us to calculate the exact fidelity to the target state, while also providing better noise performance.

We perform an experimental test of our technique with states entangled in discretized transverse-position modes, also known as 'pixel' entanglement<sup>42</sup>. As shown in Fig. 2a, photon pairs entangled in their transverse position-momentum are produced in a nonlinear crystal via the process of spontaneous parametric downconversion and separated by a polarizing beamsplitter. One photon is input into a commercial MMF and sent to Bob, while its entangled partner is kept with Alice. The MMF used in our experiment is a 2-m graded-index fibre (Thorlabs GIF50E) that supports  $\sim 400$  modes. Projective spatial-mode measurements of the resulting state at Alice and Bob are made with phase-only spatial light modulators (SLMs), single-mode fibres and avalanche photodiodes<sup>43</sup>.

The Pixel basis used in our experiment is composed of seven individual circular macro-pixels defined on the SLM. Figure 2b shows examples of diffractive holograms implemented on the SLMs for measuring states in the Pixel basis and first Pixel MUB. A particular mode  $|m\rangle$  ( $|n\rangle$ ) at Alice (Bob) is measured by displaying the corresponding macro-pixel hologram on their SLM. We can also define a family of orthonormal bases that are constructed from the Pixel basis using a transformation  $\mathbf{M} = M_{\mathrm{A}} \otimes M_{\mathrm{B}}^{*}$ , where  $M$  takes us from the standard (Pixel) basis  $\{|m\rangle\}_{m=0,\ldots,d-1}$  to a new basis  $\{|f_k\rangle\}_{k=0,\ldots,d-1}^r$  given by

$$
\left| f _ {k} ^ {r} \right\rangle = \frac {1}{\sqrt {d}} \sum_ {m = 0} ^ {d - 1} \omega^ {k m + r m ^ {2}} | m \rangle \tag {4}
$$

with  $k$  indexing a state in the new basis and  $r = 0,\dots,d - 1$  indexing the basis itself. This construction follows the one introduced by Wootters and Fields<sup>39</sup>, which provides a set of bases mutually unbiased with respect to each other for prime dimensions.

In the absence of a complex medium, two-photon correlations measured in the Pixel basis and first Pixel (Fourier) MUB, respectively (Fig. 3a,b), certify a fidelity of  $F \geq 94.1 \pm 1.2\%$  to a seven-dimensional (7D) maximally entangled state<sup>14</sup>. Figure 3c,d shows measured correlations in these two bases after one photon

![](images/3c1f525f3f6019f12b7171b778bcdf4a802f9a40398182c1aab86e07ac6ecfb9.jpg)  
Fig. 2 | Experimental set-up and measurement holograms. a, A grating-stabilized ultraviolet laser is used to pump a nonlinear ppKTP crystal (NLC), producing pairs of photons entangled in their transverse position-momentum, which are separated by a polarizing beamsplitter (PBS). One photon is sent into a 2-m-long commercial multimode fibre (MMF, Thorlabs GIF50E) and directed towards Bob, while its entangled twin is kept locally with Alice. Projective measurements of the resulting quantum state in any rotated Pixel basis are performed with spatial light modulators (SLMs), single-mode fibres and avalanche photodiodes (not shown). b, Examples of holograms for measuring photonic states in the Pixel basis and its first mutually unbiased basis (Pixel MUB). As can be seen, the MUB hologram is made up of a coherent superposition of all seven macro-pixels. c, Real and imaginary parts of the transmission matrix measured in the Pixel MUB ( $T_{M}$ ) and an example of a 'scrambled' basis hologram calculated from it. The scrambled basis hologram is displayed on Alice's SLM for unscrambling entanglement through the MMF.

![](images/22619bf3bfc0e6e28b4f5b7e152d8ba7f35907dbacc6180a379446138d342766.jpg)

![](images/74cca3978bb582f9e69175ebe0338047f759edb3fbde492f311529647a91bffc.jpg)

![](images/42a7bb953adb3bc98eca9e2c92daf7ad87db6be0163cfa83506c4874d08a6dd1.jpg)  
Fig. 3 | Entanglement before and after a complex medium. a,b, In the absence of the MMF, two-photon correlations measured in the Pixel basis (a) and its first mutually unbiased basis (Pixel MUB) (b) result in a fidelity to the 7D maximally entangled state of  $F \geq 94.1 \pm 1.2\%$ , certifying the presence of 7D entanglement. The error on the fidelity bound is given by three times its standard deviation. c,d, Pixel (c) and first Pixel MUB (d) correlations after one photon from the entangled state is sent through a 2-m-long MMF, resulting in the loss of entanglement. Interestingly, even though the correlations are completely scrambled, the resulting data contain information about the transmission matrix in each basis ( $|T|^{2}$  and  $|T_{M}|^{2}$ ) via state-channel duality (equation (1)).

![](images/21788c40b646c0787a665480a2af66c1880d40e711ff0ebbf40cea154bcbea6a.jpg)

from the state is sent through the MMF, as shown in Fig. 2a. Correlations in both bases are completely lost, resulting in a trivial bound. Measurements in all eight MUBs after transmission through the fibre (Extended Data Fig. 1) result in an exact fidelity of  $F(\rho_{\mathrm{P}}\Phi^{+}) = 5.4 \pm 1.0\%$ , which is lower than the bound of  $F_{2} = 1 / 7$  for two-dimensional entanglement (see Methods for more details). Interestingly, although the measurements in Fig. 3c,d do not show any entanglement, they contain information about the absolute value of the fibre transmission matrix (equation (1)), measured in the Pixel basis and Pixel MUB  $|T|^2$  and  $|T_M|^2$ , respectively.

A key challenge is retrieving the phase information of the transmission matrix elements using only intensity measurements. Here, we borrow a classical trick for doing so, where an internal reference mode is co-propagated through the medium and interfered with all the modes of interest<sup>5</sup>. We use the space between our seven macro-pixels as a reference mode and vary its phase in four steps. The reference is characterized in a similar manner (see Methods for more details). To maximize our count rates and minimize noise, we perform this procedure in the Pixel MUB instead of the Pixel basis. Via this phase-stepping holography, we are able to recover the complex values of the transmission matrix  $(T_M)$ , and subsequently rotate to the other Pixel bases to certify entanglement. Figure 2c shows the real and imaginary parts of the measured transmission matrix, and an example of a 'scrambled' basis hologram calculated from  $\left(T_M^{-1}\right)^T$  and displayed at Alice<sup>43</sup>. In this manner, entanglement is recovered by only manipulating the photon that did not enter the MMF.

![](images/009bb7853f8a09ec3c7349b431c51cc8f77294a7c8e2cd1925f09b0947c42d05.jpg)  
a

![](images/4afa00b5071e639a0e76004a4691fdc882f110d5ddcd9fbc4cedc12d65052211.jpg)  
b

![](images/c873fef5fb48a4ed0717b6b8a8f5cc1a34cf45728dfc2ce4ac0d6472a3dea3d3.jpg)  
c

![](images/d9f261c56b3bf17afecf41ad79e528ca2fdf48e884d6adba3f3c878586d30610.jpg)  
d

![](images/2895a6ab66f9df3c289534eb9b175714575d5e3723577c9e3e198e676e484bd4.jpg)  
e  
Fig. 4 | High-dimensional entanglement unscrambled through a complex medium. a-h, Experimental data showing quantum correlations recovered in the Pixel (a) and seven 'tilted' Pixel (b-h) bases after transmission through the MMF. The Pixel basis measurements allow us to nominate a target state  $|\Psi \rangle = \sum \lambda_i |ii\rangle$  and subsequently use its Schmidt coefficients  $\lambda_i$  to construct MUB-like 'tilted' bases following a recently developed entanglement certification technique<sup>14</sup>. Using these measurements, we can calculate the exact fidelity of the transported two-photon state  $(\rho_{\mathrm{T}})$  to the target state  $(|\Psi \rangle)$  to be  $F(\rho_{T}, \Psi) = 84.4 \pm 1.8\%$ , certifying the presence of 6D entanglement. The error on the fidelity is given by three times its standard deviation.

![](images/bb2a96dcc104b1b64e6609df7c2c1b808421f1687894df157082c7c77d127094.jpg)  
f

![](images/956f5ba1325e1c313e42c6390fd98c55f0271ef82e0b8250d50bb24e85f67b0f.jpg)  
g

![](images/8bd63cc27fad0b3b85ce95561d1d75b5bb5b7650b1ff0f4f80cc06b799f6ff1e.jpg)  
h

Measurements showing the recovered state and its correlations in eight different bases are shown in Fig. 4. Here, we use a recently developed adaptive witness that constructs MUB-like 'tilted' bases to calculate the fidelity of the transmitted state  $\rho_{T}$  to a non-maximally entangled target state  $|\Psi \rangle = \sum_{m}\lambda_{m}|mm\rangle$  (ref. 14). The  $r$ th tilted basis is defined by generalizing the definition of a MUB (equation (4)) in the following manner:

$$
\left| \tilde {f} _ {k} ^ {r} \right\rangle = \frac {1}{\sqrt {\sum_ {n} \lambda_ {n}}} \sum_ {m = 0} ^ {d - 1} \omega^ {k m + r m ^ {2}} \sqrt {\lambda_ {m}} | m \rangle \tag {5}
$$

where  $\lambda_{m}$  refer to the Schmidt coefficients of the non-maximally entangled target state. Notice that, for  $\sum_{m}\lambda_{m}^{2} = 1$ , the basis vectors  $\left|\tilde{f}_k^r\right\rangle$  are normalized but not necessarily orthogonal. Our recovered state after the MMF (Fig. 4a) is non-maximally entangled owing to the non-unitarity of the channel, while still retaining its purity. The tilted-basis witness and an appropriately chosen target state are thus quite suitable for certifying entanglement in this scenario (see Methods for more details). Using the measurements shown in Fig. 4, we are able to calculate an exact fidelity to the target state estimated from Fig. 4a of  $F(\rho_T,\Psi) = 84.4\pm 1.8\%$  certifying the presence of six-dimensional entanglement. The uncertainty in the fidelity is calculated assuming Poisson counting statistics and propagating the error via a Monte-Carlo simulation of the experiment.

To achieve the transport of high-dimensional entanglement through an MMF, our experiment made use of single-outcome spatial-mode measurements that were scanned through the basis of interest. This limits the speed with which the complex medium or entangled state can be characterized. Furthermore, our MMF was quite short, limiting the effects of spatial-mode dispersion. Rapid progress in the development of quantum technologies, such as generalized mode transformers $^{44}$ , single-photon detector arrays $^{45}$  and spatio-temporal wavefront-shaping approaches $^{46}$ , should allow our technique to be used for entanglement transport through highly dynamic scattering samples, such as living biological tissue or km-long MMFs $^{1}$ . Furthermore, our work can be generalized to the case of both

photons travelling through two independent channels, with only one particle being manipulated (see Supplementary Information for more details). Such an ability could be useful in quantum network scenarios $^{47}$  or for non-invasive biological imaging $^{48}$ , where access to all parts of the complex system may be limited. Our results thus have immediate ramifications for the fields of quantum communication and imaging $^{49,50}$ , where the transport and control of quantum states of light through complex media remains a pressing challenge.

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41567-020-0970-1.

Received: 28 November 2019; Accepted: 19 June 2020  
Published online: 3 August 2020

# References

1. Rotter, S. & Gigan, S. Light fields in complex media: mesoscopic scattering meets wave control. Rev. Mod. Phys. 89, 015005 (2017).  
2. Papadopoulos, I. N., Farahi, S., Moser, C. & Psaltis, D. High-resolution, lensless endoscope based on digital scanning through a multimode optical fiber. Biomed. Opt. Exp. 4, 260-270 (2013).  
3. Ploschner, M., Tyc, T. & Cizmár, T. Seeing through chaos in multimode fibres. Nat. Photon. 9, 529-535 (2015).  
4. Turtaev, S. et al. High-fidelity multimode fibre-based endoscopy for deep brain in vivo imaging. Light Sci. Appl. 7, 92 (2018).  
5. Popoff, S. M. et al. Measuring the transmission matrix in optics: an approach to the study and control of light propagation in disordered media. Phys. Rev. Lett. 104, 100601 (2010).  
6. Leedurongwatthanakun, S. et al. Programmable linear quantum networks with a multimode fibre. Nat. Photon. 14, 139-142 (2020).  
7. Defienne, H., Barbieri, M., Walmsley, I. A., Smith, B. J. & Gigan, S. Two-photon quantum walk in a multimode fiber. Sci. Adv. 2, e1501054 (2016).  
8. Wolterink, T. A. W. et al. Programmable two-photon quantum interference in  $10^{3}$  channels in opaque scattering media. Phys. Rev. A 93, 53817 (2016).

9. Defenne, H., Reichert, M. & Fleischer, J. W. Adaptive quantum optics with spatially entangled photon pairs. Phys. Rev. Lett. 121, 233601 (2018).  
10. Gisin, N. & Thew, R. Quantum communication. Nat. Photon. 1, 165-171 (2007).  
11. Kelly, J. et al. State preservation by repetitive error detection in a superconducting quantum circuit. Nature 519, 66-69 (2015).  
12. Acin, A. et al. Device-independent security of quantum cryptography against collective attacks. Phys. Rev. Lett. 98, 230501 (2007).  
13. Krenn, M., Malik, M., Erhard, M. & Zeillinger, A. Orbital angular momentum of photons and the entanglement of Laguerre-Gaussian modes. Philos. Trans. R. Soc. A 375, 20150442 (2017).  
14. Bavaresco, J. et al. Measurements in two bases are sufficient for certifying high-dimensional entanglement. Nat. Phys. 14, 1032-1037 (2017).  
15. Erhard, M., Malik, M., Krenn, M. & Zeilinger, A. Experimental Greenberger-Horne-Zeilinger entanglement beyond qubits. Nat. Photon. 12, 759-764 (2018).  
16. Schneeloch, J., Tison, C. C., Fanto, M. L., Alsing, P. M. & Howland, G. A. Quantifying entanglement in a 68-billion-dimensional quantum state space. Nat. Commun. 10, 2785 (2019).  
17. Mirhosseini, M. et al. High-dimensional quantum cryptography with twisted light. N. J. Phys. 17, 33033 (2015).  
18. Islam, N. T., Lim, C. C. W., Cahall, C., Kim, J. & Gauthier, D. J. Provably secure and high-rate quantum key distribution with time-bin quids. Sci. Adv. 3, e1701491 (2017).  
19. Ecker, S. et al. Overcoming noise in entanglement distribution. Phys. Rev. X 9, 041042 (2019).  
20. Zhu, F., Tyler, M., Valencia, N. H., Malik, M. & Leach, J. Are high-dimensional entangled states robust to noise? Preprint at https://arxiv.org/pdf/1908.08943v1.pdf (2019).  
21. Brida, G., Genovese, M. & Berchera, I. R. Experimental realization of sub-shot-noise quantum imaging. Nat. Photon. 4, 227-230 (2010).  
22. Lemos, G. B. et al. Quantum imaging with undetected photons. Nature 512, 409-412 (2014).  
23. Vertesi, T., Pironio, S. & Brunner, N. Closing the detection loophole in Bell experiments using quids. Phys. Rev. Lett. 104, 60401 (2010).  
24. Bavaresco, J. et al. Most incompatible measurements for robust steering tests. Phys. Rev. A 96, 22110 (2017).  
25. Yin, J. et al. Satellite-based entanglement distribution over 1,200 kilometers. Science 356, 1140-1144 (2017).  
26. Inagaki, T., Matsuda, N., Tadanaga, O., Asobe, M. & Takesue, H. Entanglement distribution over  $300\mathrm{km}$  of fiber. Opt. Exp. 21, 23241-23249 (2013).  
27. Cao, H. et al. Distribution of high-dimensional orbital angular momentum entanglement over a 1-km few-mode fiber. Optica 7, 232-237 (2020).  
28. Jamiolkowski, A. Linear transformations which preserve trace and positive semidefiniteness of operators. Rep. Math. Phys. 3, 275-278 (1972).  
29. D'Ariano, G. M. & Lo Presti, P. Quantum tomography for measuring experimentally the matrix elements of an arbitrary quantum operation. Phys. Rev. Lett. 86, 4195-4198 (2001).  
30. Konrad, T. et al. Evolution equation for quantum entanglement. Nat. Phys. 4, 99-102 (2007).

31. Altepeter, J. B. et al. Ancilla-assisted quantum process tomography. Phys. Rev. Lett. 90, 193601 (2003).  
32. Ndagano, B. et al. Characterizing quantum channels with non-separable states of classical light. Nat. Phys. 13, 397-402 (2017).  
33. Carpenter, J., Eggleton, B. J. & Schröder, J. Observation of Eisenbud-Wigner-Smith states as principal modes in multimode fibre. Nat. Photon. 9, 751-757 (2015).  
34. Popoff, S., Lerosey, G., Fink, M., Boccara, A. C. & Gigan, S. Image transmission through an opaque material. Nat. Commun. 1, 81 (2010).  
35. Klyshko, D. N. A simple method of preparing pure states of an optical field, of implementing the Einstein-Podolsky-Rosen experiment, and of demonstrating the complementarity principle. Sov. Phys. Usp. 31, 74-85 (1988).  
36. Peeters, W. H., Moerman, J. J. D. & van Exter, M. P. Observation of two-photon speckle patterns. Phys. Rev. Lett. 104, 173601 (2010).  
37. Franson, J. D. Nonlocal cancellation of dispersion. Phys. Rev. A 45, 3126-3132 (1992).  
38. Black, A. N. et al. Quantum nonlocal aberration cancellation. Phys. Rev. Lett. 123, 143603 (2019).  
39. Wootters, W. & Fields, B. Optimal state-determination by mutually unbiased measurements. Ann. Phys. 191, 363-381 (1989).  
40. Friis, N., Vitagliano, G., Malik, M. & Huber, M. Entanglement certification from theory to experiment. Nat. Rev. Phys. 1, 72-87 (2019).  
41. Malik, M. et al. Multi-photon entanglement in high dimensions. Nat. Photon. 10, 248-252 (2016).  
42. Valencia, N. H. et al. High-dimensional pixel entanglement: efficient generation and certification. Preprint at https://arxiv.org/pdf/2004.04994.pdf (2020).  
43. Bouchard, F. et al. Measuring azimuthal and radial modes of photons. Opt. Exp. 26, 31925-31941 (2018).  
44. Fontaine, N. K. et al. Laguerre-Gaussian mode sorter. Nat. Commun. 10, 1865 (2019).  
45. Wollman, E. E. et al. Kilopixel array of superconducting nanowire single-photon detectors. Opt. Exp. 27, 35279-35289 (2019).  
46. Mounaix, M. et al. Spatiotemporal coherent control of light through a multiple scattering medium with the multispectral transmission matrix. Phys. Rev. Lett. 116, 253901 (2016).  
47. Epping, M., Kampermann, H., Macchiavello, C. & Bruß, D. Multi-partite entanglement can speed up quantum key distribution in networks. New J. Phys. 19, 093012 (2017).  
48. Kang, S. et al. Imaging deep within a scattering medium using collective accumulation of single-scattered waves. Nat. Photon. 9, 253-258 (2015).  
49. Diamanti, E., Lo, H.-K., Qi, B. & Yuan, Z. Practical challenges in quantum key distribution. npj Quantum Inf. 2, 16025 (2016).  
50. Moreau, P.-A., Toninelli, E., Gregory, T. & Padgett, M. J. Imaging with quantum states of light. Nat. Rev. Phys. 1, 367-380 (2019).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2020

# Methods

Mapping the MMF channel onto an entangled state. A complex medium such as an MMF acts as a scattering channel. If one particle of a bipartite high-dimensional entangled state enters the channel, its quantum correlations are affected by mode mixing and crosstalk. To reverse this effect, we will show how the information of the channel is mapped onto the output state, allowing us to determine the transmission matrix that characterizes the scattering process in the fibre.

Let us consider a general bipartite state

$$
\left| \psi_ {\mathrm {i}} \right\rangle = \sum_ {i j} C _ {i j} \hat {a} _ {i} ^ {\dagger} \hat {b} _ {j} ^ {\dagger} | \text {v a c} \rangle = \sum_ {i j} C _ {i j} | i \rangle_ {\mathrm {A}} | j \rangle_ {\mathrm {B}} \tag {6}
$$

where  $i$  and  $j$  label the spatial modes of the biphoton state shared by two parties, Alice and Bob. The state lives in a Hilbert space of dimension  $d = 7$ , which is smaller than the number of modes supported by the MMF channel. Let us thus divide the state space into a logical subspace, corresponding to the modes that we measure, and environmental/loss modes, which are not considered in this process. Adding two extra indices  $n$  and  $m$  to our initial state to indicate whether the mode is in the logical or environmental subspace, we can write

$$
\begin{array}{l} \left| \psi_ {i} \right\rangle = \sum_ {i n j m} C _ {i n j m} \hat {a} _ {i n} ^ {\dagger} \hat {b} _ {j m} ^ {\dagger} | \mathrm {v a c} \rangle \tag {7} \\ = \sum_ {i n j m} C _ {i n j m} | i n \rangle_ {\mathrm {A}} | j m \rangle_ {\mathrm {B}} \\ \end{array}
$$

where a given  $i, j$  mode is in the logical subspace if  $m, n = 1$ , or in the environmental subspace otherwise.

In our system, Bob's modes go through the MMF and undergo the unitary transformation

$$
\hat {U} _ {\mathrm {M M F}} = \sum_ {k l r s} U _ {k l r s} | k l \rangle \langle r s | \tag {8}
$$

The matrix  $U$  is given by elements  $U_{klrs}$  that describe how the modes  $|rs\rangle$  scatter to modes  $|kl\rangle$ . The action of the scattering on our initial state is given by

$$
\hat {b} _ {j m} ^ {\dagger} \xrightarrow {U} \hat {U} \hat {b} _ {j m} ^ {\dagger} \hat {U} ^ {\dagger} = \sum_ {k l} U _ {k l j m} \hat {b} _ {k l} ^ {\dagger} \tag {9}
$$

After the MMF, we perform measurements in the  $d$ -dimensional logical subspace. This measurement and postselection, which result in a state conditioned on both photons being in the logical subspace  $(n,m = 1)$ , can be described using the following projector:

$$
\begin{array}{l} \hat {H} = \sum_ {p q} \hat {a} _ {p 1} ^ {\dagger} \hat {b} _ {q 1} ^ {\dagger} | \text {v a c} \rangle \langle \text {v a c} | \hat {b} _ {q 1} \hat {a} _ {p 1} \tag {10} \\ = \sum_ {p q} | p 1 \rangle_ {\mathrm {A}} | q 1 \rangle_ {\mathrm {B B}} \langle p 1 | _ {\mathrm {A}} \langle q 1 | \\ \end{array}
$$

This occurs in general with non-unit success probability, resulting in the subnormalized state after the MMF given by

$$
\begin{array}{l} | \psi \rangle_ {\mathrm {M M F}} := \hat {H} (\hat {I} _ {\mathrm {A}} \otimes \hat {U} _ {\mathrm {M M F}}) | \psi_ {\mathrm {i}} \rangle \\ = \sum_ {i j m k} U _ {k 1 j m} C _ {i l j m} | i 1 \rangle_ {\mathrm {A}} | k 1 \rangle_ {\mathrm {B}} \tag {11} \\ := \sum_ {i k} t _ {k i} \left\langle t _ {\mathrm {A}} \right\rangle \left\langle k \right\rangle_ {\mathrm {B}} \\ \end{array}
$$

where we define the coefficients characterizing the state after the fibre as  $t_{ki} \coloneqq \sum_{jm} U_{k1jm} C_{i1jm}$ . Notice that these coefficients encode the information of both the MMF and the state.

As shown in the main text, the state we produce through spontaneous parametric downconversion is very close to the maximally entangled state:

$$
\left| \Psi^ {+} \right\rangle = \frac {1}{\sqrt {d}} \sum_ {i} | i \rangle_ {\mathrm {A}} | i \rangle_ {\mathrm {B}} \tag {12}
$$

We find in this case that the action of the unitary channel representing the MMF, followed by postselection onto states with photons detected in the logical subspace, is characterized by the operator  $\hat{T}$  with elements  $t_{ki} = U_{k1i}$ :

$$
\hat {T} _ {\mathrm {M M F}} = \sum_ {k i} U _ {k 1 i 1} | k \rangle \langle i | \tag {13}
$$

whose coefficients describe how the logical mode  $i$  scatters into the logical mode  $k$ . This is not a unitary operation (because it is only a submatrix of the full unitary transformation) and is not trace-preserving (as the postselection happens in general with non-unit success).

In this sense, even though our MMF is a unitary channel on all the modes that the fibre can support, because we are interested only in the logical modes, the operator  $\hat{T}$  acts as the relevant non-unitary transmission matrix of the fibre. Because this operator is non-unitary, it has the effect of changing the entanglement in the state, despite only acting locally on Bob's modes.

If our initial state is maximally entangled as in equation (12), and we consider this operator that represents the scattering effect of the fibre on all the modes in Bob's space (logical and environmental), the state after one of the photons of the entangled pair goes through the fibre is given by

$$
\left| \psi_ {\mathrm {M M F}} \right\rangle = (\hat {I} \otimes \hat {T}) \left| \psi^ {+} \right\rangle = \sum_ {i k} U _ {k 1 i 1} | i \rangle_ {\mathrm {A}} | k \rangle_ {\mathrm {B}} \tag {14}
$$

This is precisely the Choi-Jamiolkowski isomorphism, where the channel representing the fibre is imprinted onto the initial entangled state.

We note that this subnormalized state is pure despite having undergone a non-unitary transformation. In the absence of postselection, one could instead model the trace-preserving channel acting only on the logical modes by including the vacuum state in the output Hilbert space. In the Kraus representation, this trace-preserving channel is given by the Kraus operators

$$
\begin{array}{l} A _ {0} \quad = U _ {k 1 r 1} | k \rangle \langle r | \\ A _ {m} = U _ {m 2 r 1} | \operatorname {v a c} \rangle \langle r | \tag {15} \\ \end{array}
$$

$$
\text {s o t h a t} \quad \sum_ {\forall m ^ {\prime}} A _ {m} ^ {\dagger} A _ {m} = \hat {I}
$$

which is clearly not a pure channel if any  $U_{m2r1} \neq 0$ , that is, if there is any loss, as the output state is a mixture with the vacuum. However, after postselection on the existence of a photon, only the term originating from  $A_0$  survives, resulting in a postselected subnormalized pure state.

It is clear from equations (11) and (14) that considering the initial state to be a general entangled state, or the maximally entangled state, leads to analogous resulting states after the fibre  $|\psi_{\mathrm{MMF}}\rangle$ . Even more, if one attributes the effect of coefficients  $C_{ij}$  to the channel  $U$ , the two cases are the same. Because of this, we consider our initial state to be  $|\Psi^{+}\rangle$ .

Experimental details. A continuous-wave grating-stabilized laser (Toptica DL Pro HP) at  $405\mathrm{nm}$  pumps a periodically poled potassium titanyl phosphate (ppKTP) crystal  $(1\mathrm{mm} \times 2\mathrm{mm} \times 5\mathrm{mm})$  at  $75\mathrm{mW}$  to generate a pair of orthogonally polarized photons at  $810\mathrm{nm}$  entangled in their position-momentum degree of freedom through the process of type-II spontaneous parametric downconversion. Phase-matching conditions are achieved by temperature-tuning the crystal in a custom-built oven that keeps it at  $30^{\circ}\mathrm{C}$ . A 5:1 telescope system of lenses is used to shape the pump beam and focus it on the crystal with a  $1/e^{2}$  beam diameter of  $400\mu\mathrm{m}$ . A dichroic mirror removes the pump after the crystal, while the pair of produced photons are separated by a polarizing beamsplitter. The reflected photon (corresponding to Alice) has its polarization rotated from vertical to horizontal with a half-wave plate and made incident on a phase-only SLM (Hamamatsu X10468-02) that is placed in the Fourier plane of the crystal using a  $250\mathrm{-mm}$  lens. The transmitted photon (corresponding to Bob) is shaped with lenses to effectively couple modes in our 7D Hilbert space of interest into a  $2\mathrm{-m}$  graded-index MMF (Thorlabs M116L02) with a core diameter of  $50\mu\mathrm{m}$  that supports around 400 spatial modes at  $810\mathrm{nm}$ . After going through the fibre, the photon is launched onto another phase-only SLM.

Measurements in the position-momentum degree of freedom of the photons are made with computer-generated holograms displayed by the parallel-aligned liquid-crystal-on-silicon layer of the SLMs, which has an effective area of  $15.8 \times 12 \mathrm{~mm}^2$ , pixel pitch of  $20 \mu \mathrm{m}$ , resolution of  $792 \times 600$ , reflection efficiency of  $\sim 90\%$  and diffraction efficiency of  $\sim 75\%$ . The computer-generated hologram in combination with a single-mode fibre allows us to projectively measure whether the incident photons are in a particular spatial mode in any given basis. The accuracy of the projections performed with the combo of SLM and single-mode fibre is ensured through the use of an intensity flattening telescope[43]. This technique removes the Gaussian component introduced by the use of a single-mode fibre by afocally decreasing the size of the mode propagating from the SLM to the objective lens, thus recovering the orthogonality relation between spatial modes of a given basis. The single-mode fibres guide the filtered photons to single-photon avalanche detectors (Excelitas SPCM-AQRH-14-FC) with an efficiency of  $60\%$  at  $810 \mathrm{~nm}$ . The detectors are connected to a coincidence counting logic (UQD Logic16) that records time-coincident events within a window of  $0.2 \mathrm{~ns}$ .

Measurement of the transmission matrix. As discussed in the main text, when one of the photons of a high-dimensional entangled biphoton state is sent through the MMF, the effect of this scattering channel is encoded onto the complex coefficients  $t_{ij}$  characterizing the output state  $|\psi_{\mathrm{MMF}}\rangle$ . These coefficients form a matrix  $T$  that we consider as the effective or relevant transmission matrix for the modes of the  $d$ -dimensional subspace in which we measure.

We use a phase-stepping technique to determine  $T$ . To do so, let us define a mode number 0 as our internal reference mode. The reference mode in our experiment was taken to be a 'background' mode, which is defined by all the SLM pixels that lie between the macro-pixel modes. The phase-stepping process is implemented by displaying a relative phase  $\theta$  between the basis and the reference modes. In this manner, when Alice scans mode  $m$ , the reference mode is displayed simultaneously with a controlled phase difference. On Bob's side, we will simply display mode  $n$  (Extended Data Fig. 2).

The state we are projecting on with each measurement of one element of the correlation matrix is given by

$$
\left| \chi_ {m n} \right\rangle = \left(\mathrm {e} ^ {i \theta} | 0 \rangle + | m \rangle\right) _ {\mathrm {A}} \otimes | n \rangle_ {\mathrm {B}} \tag {16}
$$

where  $m, n = 1, \dots, d$  represent basis elements of the Pixel basis. From these measurements, we can construct a matrix  $R$  with coefficients of the form

$$
R _ {m n} (\theta) = \left| \left\langle \chi_ {m n} \right| \Psi_ {\mathrm {M M F}} \right\rangle | ^ {2} = \left| t _ {n 0} \mathrm {e} ^ {- i \theta} + t _ {n m} \right| ^ {2} \tag {17}
$$

Setting  $\theta$  in steps of  $\pi /2$  going from 0 to  $3\pi /2$  we obtain

$$
\begin{array}{l} S _ {m n} := \frac {1}{4} \left[ R _ {m n} ^ {0} - R _ {m n} ^ {\pi} + i \left(R _ {m n} ^ {\pi / 2} - R _ {m n} ^ {3 \pi / 2}\right) \right] \tag {18} \\ = t _ {n 0} t _ {n m} ^ {*} = E _ {n} t _ {n m} ^ {*} \\ \end{array}
$$

The resulting matrix  $S$  is not exactly equal to the transmission matrix  $T$ , but is related to it as follows:

$$
S = \left( \begin{array}{c c c} t _ {1 1} ^ {*} & \dots & t _ {d 1} ^ {*} \\ \vdots & \ddots & \vdots \\ t _ {1 d} ^ {*} & \dots & t _ {d d} ^ {*} \end{array} \right) \left( \begin{array}{c c c} t _ {1 0} & \dots & 0 \\ \vdots & t _ {j 0} & \vdots \\ 0 & \dots & t _ {d 0} \end{array} \right) = T ^ {\dagger} E \tag {19}
$$

where  $E$  is a diagonal matrix related to the mixing of the reference with the basis modes after going through the MMF. Determining  $E$  is crucial for fully recovering the correlations of our entangled state. To do so, we again use the phase-stepping technique, where we now only display the reference mode on Alice, while Bob simultaneously displays a basis and reference mode (Extended Data Fig. 3):

$$
\left| \chi \right\rangle_ {m} = \left| 0 \right\rangle_ {\mathrm {A}} \otimes \left(\mathrm {e} ^ {i \theta} | 0 \rangle + | m \rangle\right) _ {\mathrm {B}} \tag {20}
$$

The results of these measurements are given by

$$
R _ {m} ^ {\theta} = \left| \left\langle \chi_ {m} \right| \Psi_ {\mathrm {M M F}} \right\rangle \left| ^ {2} \right. = \left| t _ {0 0} \mathrm {e} ^ {i \theta} + t _ {m 0} \right| ^ {2} \tag {21}
$$

Performing the measurement for different relative phases, we recover the terms

$$
\begin{array}{l} \tilde {E} _ {m} = \frac {1}{4} \left[ \left(R _ {m} ^ {0} - R _ {m} ^ {\pi} + i \left(R _ {m} ^ {\pi / 2} - R _ {m} ^ {3 \pi / 2}\right) \right] \right. \tag {22} \\ = t _ {0 0} f _ {m 0} ^ {*} = t _ {0 0} E _ {m} ^ {*} \\ \end{array}
$$

Building a diagonal matrix from the terms  $\tilde{E}_m$ , we have

$$
\tilde {E} = t _ {0 0} \left( \begin{array}{c c c} E _ {1} ^ {*} & \dots & 0 \\ \vdots & E _ {j} ^ {*} & \vdots \\ 0 & \dots & E _ {d} ^ {*} \end{array} \right) = t _ {0 0} E ^ {*} \tag {23}
$$

The matrix  $\tilde{E}$  is equal to the conjugate of matrix  $E$  with a factor of  $t_{00}$  that we neglect because it only adds a global amplitude and phase. After determining both  $S$  and  $E$ , we can calculate the  $T$  matrix characterizing the effect of the MMF as follows:

$$
T = \left(S E ^ {- 1}\right) ^ {\dagger} \tag {24}
$$

It is important to notice that, because we are using localized transverse spatial (or momentum) modes, the single-outcome measurements we have been describing are limited by their projection onto the collection mode, leading to lower counts when using the standard basis than when using any of the MUBs $^{42}$ . To have a faster and less noisy measurement of the transmission matrix, we thus use the first MUB basis (corresponding to  $r = 0$  in the Wootters-Fields construction of equation (4)) for the phase-stepping process.

It can easily be proven that using a basis different from the standard when following the steps described above simply results in a rotation of the transmission matrix. In our case, the obtained transmission matrix corresponding to measurements in the first MUB is given by

$$
T _ {M _ {0}} = M _ {0} ^ {*} T M _ {0} ^ {T} \tag {25}
$$

where  $T$  is the transmission matrix that one would determine had the measurement been made in the standard basis and  $M_0$  is the MUB transformation matrix.

Unscrambling entanglement. The knowledge of the transmission matrix of the fibre allows us to construct a new set of measurement bases that invert the mixing process of the modes of the entangled state, thus recovering or 'unscrambling' the quantum correlations present in  $|\psi_{\mathrm{i}}\rangle$ . First, we will consider the case in which the transmission matrix was determined in the standard basis, and then we will generalize for any rotation of  $T$ .

Interestingly, this new set of bases can be used either by Alice or Bob for recovering the state. Instead of unscrambling the mode mixing on Bob's side, we choose to 'scramble' the modes on Alice's side to show that even though Bob's photon is the one going through the MMF, by performing the right measurements on Alice, the correlations of the entangled biphoton state are recovered.

The biphoton state after propagation through the fibre is described by the state

$$
\left| \psi_ {\mathrm {M M F}} \right\rangle = \left(\hat {I} _ {\mathrm {A}} \otimes \hat {T}\right) \left| \Psi^ {+} \right\rangle \tag {26}
$$

Reversing the action of  $T$  on the entangled state can be done simply by applying the inverse operation on the photon going through the fibre:

$$
\left(\hat {I} _ {\mathrm {A}} \otimes \hat {T} ^ {- 1}\right) \left| \psi_ {\mathrm {M M F}} \right\rangle = \left| \Psi^ {+} \right\rangle \tag {27}
$$

Of course, since  $\hat{T} \preccurlyeq \hat{I}$  (the singular values of the matrix  $T$  are all less than 1), the inverse does not constitute a physical channel, and must be appropriately normalized. We defer this discussion to the Supplementary Information. Because we want to manipulate only the state on Alice's side, we consider the following property:

$$
(\hat {A} \otimes \hat {B}) | \Psi^ {+} \rangle = (\hat {B} ^ {T} \hat {A} \otimes \hat {I}) | \Psi^ {+} \rangle = (\hat {I} \otimes \hat {B} \hat {A} ^ {T}) | \Psi^ {+} \rangle \tag {28}
$$

Hence, to invert the action of the MMF, one can use equation (24) to generate an operator on Alice's side:

$$
W _ {\mathrm {A}} = \left(T ^ {- 1}\right) ^ {T} = \left(\left(\left(S E ^ {- 1}\right) ^ {\dagger}\right) ^ {- 1}\right) ^ {T} \tag {29}
$$

In this manner, we can define a composite operator  $\mathbf{W} = \hat{W}_{\mathrm{A}}\otimes \hat{I}_{\mathrm{B}}$  that converts the output state of the MMF to the initial maximally entangled state:

$$
\begin{array}{l} | \psi \rangle_ {\mathrm {u}} = \mathbf {W} | \psi_ {\mathrm {M M F}} \rangle \\ = (\hat {W} _ {\mathrm {A}} \otimes \hat {I} _ {\mathrm {B}}) | \psi_ {\mathrm {M M F}} \rangle \\ = \left(\left(\hat {T} ^ {- 1}\right) ^ {T} \otimes \hat {I} _ {\mathrm {B}}\right) \left| \psi_ {\mathrm {M M F}} \right\rangle \tag {30} \\ = (\hat {I} _ {\mathrm {A}} \otimes \hat {T} ^ {- 1}) | \psi_ {\mathrm {M M F}} \rangle \\ = | \Psi^ {+} \rangle \\ \end{array}
$$

Although on Bob's side we use the standard basis, the rows of the operator  $\hat{W}_{\mathrm{A}}$  constitute a new basis to be used by Alice. Strong correlations should appear in the crosstalk matrix obtained from measuring two-photon coincidences with these bases.

The second step for certifying entanglement is to recover correlations in a mutually unbiased or a tilted basis. Using  $\hat{W}_{\mathrm{A}}$  and either of the transformations  $M_{r}$ $(r = 0,\dots ,d - 1)$  or  $\tilde{M}_r$ $(r = 0,\dots ,d - 1)$ , which define the states given by equation (4) and equation (5) respectively, we can define a new operator to unscramble the correlations in the  $r$ th mutually unbiased basis:

$$
\begin{array}{l} \mathbf {V} = \mathbf {M} _ {\mathbf {r}} \mathbf {W} \\ = \left(\hat {M} _ {r} \otimes \hat {M} _ {r} ^ {*}\right) \left(\hat {W} _ {\mathrm {A}} \otimes \hat {I} _ {\mathrm {B}}\right) \\ = (\hat {M} _ {r} \hat {W} _ {\mathrm {A}} \otimes \hat {M} _ {r} ^ {*}) \\ = \left(\hat {V} _ {\mathrm {A}} \otimes \hat {M} _ {r} ^ {*}\right) \\ \end{array}
$$

If we use  $\tilde{M}_r$  instead of  $M_r$ , we unscramble the correlations in the  $r$ th tilted basis. Using the rows of  $\hat{V}_{\mathrm{A}}$  as a new measurement basis for Alice leads to recovered correlations of the initial state in the MUB or tilted basis. Measuring in the new bases defined by  $\hat{W}_{\mathrm{A}}$  and  $\hat{V}_{\mathrm{A}}$  at Alice, and the standard and mutually unbiased basis at Bob, should result in strong correlations in two bases that allow us to certify high-dimensional entanglement.

If one uses a basis different from the standard basis for the phase-stepping process, the transmission matrix recovered is a rotated version of the transmission matrix in the standard basis  $T$ . In this case, the construction of the new bases used for recovering quantum correlations must also include a rotation back to the basis that is being used on Bob.

The transmission matrix in the standard basis can be expressed in terms of  $T_{M}$  as  $T = M^T T_M M^*$ , and thus, the operator  $\mathbf{W}$  can be written as

$$
\mathbf {W} = \left(\left(\left(M ^ {T} T _ {M} M ^ {*}\right) ^ {- 1}\right) ^ {T} \otimes \hat {I} _ {\mathrm {B}}\right) = \left(M ^ {\dagger} \left(T _ {M} ^ {- 1}\right) ^ {T} M \otimes \hat {I} _ {\mathrm {B}}\right) \tag {32}
$$

Notice that performing the measurements with  $\mathbf{W}$  for getting the correlations in the standard basis would require one to use standard basis modes on Bob's side, which, as we mentioned before, leads to lower counts.

As an alternative, one can consider an operator where the rotation of the transmission matrix to the standard basis is made partially on Alice, while in Bob one uses the MUB:

$$
\mathbf {W} _ {\mathbf {M}} = \left(\left(T _ {M} ^ {- 1}\right) ^ {T} M \otimes M ^ {*}\right) \tag {33}
$$

In this case, both SLMs display multiple pixels and we get a higher level of counts for this measurement. Applying this unscrambling operator to the MMF state equivalently leads to the maximally entangled state:

$$
\begin{array}{l} | \psi \rangle_ {\mathrm {u}} = \mathbf {W} _ {\mathbf {M}} | \psi_ {\mathrm {M M F}} \rangle \\ = \left(\left(T _ {M} ^ {- 1}\right) ^ {T} M \otimes M ^ {*}\right) \left| \psi_ {\mathrm {M M F}} \right\rangle \\ = \left(\left(T _ {M} ^ {- 1}\right) ^ {T} M \otimes M ^ {*}\right) \left(I _ {\mathrm {A}} \otimes \hat {T}\right) | \Psi^ {+} \rangle \\ = \left(\left(T _ {M} ^ {- 1}\right) ^ {T} M \otimes M ^ {*} T\right) | \Psi^ {+} \rangle \tag {34} \\ = \left(I _ {\mathrm {A}} \otimes M ^ {*} T M ^ {T} \left(T _ {M} ^ {- 1}\right)\right) | \Psi^ {+} \rangle \\ = \left(I _ {\mathrm {A}} \otimes T _ {M} \left(T _ {M} ^ {- 1}\right)\right) | \Psi^ {+} \rangle \\ = | \Psi^ {+} \rangle \\ \end{array}
$$

Analogous to  $\mathbf{W}$ , using the operator  $\mathbf{W}_{\mathrm{M}}$  results in an unscrambled state that is maximally entangled. This means that the unscrambled state in the

standard basis can also be recovered by partially rotating the transmission matrix at Alice and completing the rotation by measuring in a MUB at Bob. The normalized two-photon coincidences obtained in this case are given by

$$
\begin{array}{l} N _ {w v} = | \langle w v | \psi_ {\mathrm {M M F}} \rangle | ^ {2} \\ = \left| \langle m n | \mathbf {W} _ {\mathbf {M}} | \psi_ {\mathrm {M M F}} \rangle \right| ^ {2} \tag {35} \\ = | \langle m n | \psi_ {u} \rangle | ^ {2} \\ \end{array}
$$

where the new scrambled basis elements  $|w\rangle$  (for Alice) and  $|\nu \rangle$  (For Bob) are calculated by applying the operator  $\mathbf{W}_{\mathbf{M}}$  to the standard basis elements  $|m\rangle$  and  $|n\rangle$ . The crosstalk matrix resulting from these measurements should show strong correlations that correspond to the ones in the standard basis.

For the second measurement, let us consider that we measured the transmission matrix in the basis indexed by  $r = 0$ . In this case, the operator  $\mathbf{V}$  that recovers correlations in a basis  $r$  can be written in terms of  $T_{M_0}$  as

$$
\mathbf {V} _ {\mathbf {M}} = \mathbf {M} _ {\mathbf {r}} \mathbf {W} _ {\mathbf {M}} = \left(M _ {r} \otimes M _ {r} ^ {*}\right) \left(\left(T _ {M _ {0}} ^ {- 1}\right) ^ {T} M _ {0} \otimes M _ {0} ^ {*}\right) \tag {36}
$$

where we simply add to the first measurement the  $\mathbf{M}_{\mathrm{r}}$  transformation corresponding to the basis in which we want to recover the correlations. The normalized two-photon coincidences are given in this case by

$$
\begin{array}{l} \tilde {N} _ {w v} = | \langle g _ {w} g _ {v} | \psi_ {\mathrm {M M F}} \rangle | ^ {2} \\ = \left| \langle m n | \mathbf {V} _ {\mathbf {M}} | \psi_ {\mathrm {M M F}} \rangle \right| ^ {2} (37) \\ = \left| \right.\left\langle \right. f _ {m} f _ {n} \left. \right| \mathbf {W} _ {\mathbf {M}} \mid \psi_ {\mathrm {M M F}} \left. \right\rangle\left. \right| ^ {2} (57) \\ = \left| \left\langle f _ {m} f _ {n} \mid \psi_ {u} \right\rangle \right| ^ {2} \\ \end{array}
$$

Notice that the basis elements used at Alice  $(|g_w\rangle)$  and Bob  $(|g_v\rangle)$  are calculated by applying the operator  $\mathbf{V}_{\mathbf{M}}$  to the elements of the MUB basis  $|f_m\rangle$  and  $|f_n\rangle$ . If one uses the tilted basis, that is,  $\tilde{\mathbf{M}}_{\mathbf{r}}$  instead of  $\mathbf{M}_{\mathbf{r}}$ , the new basis elements are  $|\tilde{g}_w\rangle$  and

$\left|\tilde{g}_{\nu}\right\rangle$  , which are calculated by applying the operator  $\mathbf{V}_{\mathbf{M}}$  to the elements of the tilted basis  $\left|\hat{f}_m\right\rangle$  and  $\left|\hat{f}_n\right\rangle$

# Data availability

Data that support the plots within this paper and other findings of this study are available from the corresponding authors upon reasonable request. Source data are provided with this paper.

# Acknowledgements

We thank M. Huber, N. Friis, D. Phillips, S. Leedumrongwatthanakun and A. Fedrizzi for helpful discussions. This work was made possible by financial support from the QuantERA ERA-NET Co-fund (FWF Project I3773-N36) and the UK Engineering and Physical Sciences Research Council (EP/P024114/1). H.D. acknowledges funding from the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement no. 840958.

# Author contributions

M.M. conceived the research and supervised the project. M.M. and H.D. designed the experiment. N.H.V. and S.G. performed the experiment. All authors developed theoretical methods, analysed the data and contributed to writing the manuscript.

# Competing interests

The authors declare no competing interests.

# Additional information

Extended data is available for this paper at https://doi.org/10.1038/s41567-020-0970-1.

Supplementary information is available for this paper at https://doi.org/10.1038/s41567-020-0970-1.

Correspondence and requests for materials should be addressed to N.H.V. or M.M.

Reprints and permissions information is available at www.nature.com/reprints.

![](images/6608394be79939c1d11aa9745fd76bdb24821438a6cfe0b570f985059479bc2c.jpg)  
a)

![](images/c3c3ada7fe2d05a3d2bdd68f7a3983708a205606b6cff8ce194afce5224a878c.jpg)  
b)

![](images/305a0b3038aa8655d20b76454baeeea3ead460818a256d0622c7d0463fbb8728.jpg)  
c)

![](images/1b4dcda9ac2120612c943ed01334a5052e4d6f3dd35c241b609c472f5b87c32b.jpg)  
d)

![](images/097bf5558d84b01e967ce3ea2f24b3eb6138311a75e61b197c8fea0b45716970.jpg)  
e)  
Extended Data Fig. 1 | 'Scrambled' correlations of the output state  $|\psi_{\mathrm{MMF}}\rangle$ . Two-photon coincidence counts in the 7-dimensional Pixel basis  $\{|m\rangle, |n\rangle\}_{m,n'}$  and its 7 mutually unbiased bases  $\{|f_m\rangle, |f_n\rangle\}_{m,n}$  at the output of the multimode fibre. For this set of measurements, we obtained a fidelity to the maximally entangled state of  $\tilde{F}(\rho_T, \psi^+) = 5.4 \pm 1.0\%$ , that is, no entanglement can be certified.

![](images/7cce072762ab35d8fcaf74e1c0d9ad89097608f0bb7065d7fef822d790ea0358.jpg)  
f)

![](images/c74e1144820a9624e9dda27de2164368b95fb64722d4a6f90f42c3a2e886f4e3.jpg)  
g)

![](images/eab85596ec4f662d11a51e0f548301e12317c45542def55add7bd954189d165f.jpg)  
h)

![](images/e886dcf4c2f4a429e60a007ddf5a8937cdf4747d855d54b87c4e5b750bf7a4f7.jpg)  
a)

![](images/79e346ecb2b95016100ae48b62088b8d62e6ab53c2057532ab75051ca9fd479e.jpg)  
b)

![](images/5a8c5b614f861e6b4a89319cbc919e721e91ca9635e4fa1e2bf5088c897519e2.jpg)  
Extended Data Fig. 2 | S matrix measurement. Examples of computer-generated holograms displayed on the SLMs corresponding to (a) Alice and (b) Bob, when measuring a given matrix element  $R_{mn}^{\theta}$ . Changing the relative phase  $\theta$ , we obtain matrices  $R^{\theta}$  that allow us to calculate the elements  $S_{mn}$  through Eq. (17). The absolute value of the matrix  $S$  is shown in (c).  
c)  
n

![](images/e2785ccbf2e3cfd8cfde003542e6ca439009c1806fec2152a26ff4db25c7904a.jpg)  
a)

![](images/549851aa7eb882d6316b42fe0e03f3b3a2662615707579ef4379682dc650238c.jpg)  
b)

![](images/d030a1c3e11dfb6a3d1aac4a950e027870f3f1ba6956c8e4e119906a24e39bcf.jpg)  
Extended Data Fig. 3 | E matrix measurement. Examples of computer-generated holograms displayed on the SLMs corresponding to (a) Alice and (b) Bob, when measuring matrix elements  $R_{m}^{\theta}$ . We change the relative phase  $\theta$  via a phase-stepping process to determine the diagonal elements  $(m = n)$  of the matrix  $E$ . The absolute value of this diagonal matrix is shown in (c).  
c)