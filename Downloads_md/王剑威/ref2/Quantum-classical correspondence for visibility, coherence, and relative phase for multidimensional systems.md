# Quantum-classical correspondence for visibility, coherence, and relative phase for multidimensional systems

Alfredo Luis*

Departamento de Optica, Facultad de Ciencias Fisicas, Universidad Complutense, 28040 Madrid, Spain

(Received 21 October 2007; revised manuscript received 14 May 2008; published 8 August 2008)

We develop a thorough connection between visibility, coherence, and phase statistics for  $N$ -dimensional quantum systems and  $N$  classical waves.

DOI: 10.1103/PhysRevA.78.025802

PACS number(s): 42.25.Kb, 42.50.Ar, 03.65.Ca

# I. INTRODUCTION

Coherence and visibility of interference fringes are key concepts in physics. Their physical origin is fruitfully ascribed to phase relationships between waves. This applies equally well to quantum physics and classical optics, so that many fruitful parallels can be drawn between these two areas. Unfortunately, such a quantum-classical correspondence has been developed exclusively and extensively for the interference of just two beams.

The main objective of this work is to complete this theory by elaborating a quantum-classical correspondence concerning visibility, coherence, phase, and intensity for an arbitrary number of waves. This correspondence can be of interest in relation with basic open problems in quantum and classical physics, such as the meaning of coherence for classical partially polarized waves [1-3], the proper meaning of the phase variable in the quantum domain [4], and the relation between complementarity and uncertainty relations [5-11]. All these issues can benefit from the multidisciplinary framework developed in this work. More specifically, the main original contributions of this paper are as follows.

(i) Visibility and coherence are formulated as Hilbert-Schmidt distances in terms of the quantum density matrix or the classical cross-spectral density tensor.  
(ii) Fringe visibility of diverse classical multibeam interferometers parallels the statistics of quantum-phase operators.  
(iii) A suitable degree of coherence for multidimensional systems emerges as the maximum visibility achievable for given input fields. In the quantum domain this becomes a measure of information while in the classical domain it becomes a degree of polarization.  
(iv) The degree of coherence for multidimensional systems is a weighted average of two-dimensional degrees of coherence between pairs of components.  
(v) Quantum complementarity can be suitably expressed in terms of the Pythagoras theorem.  
(vi) Quantum wave-particle duality is explained as an example of natural relations between coherence, visibility, and intensity distribution in classical multibeam interferometers.

# II. TWO-DIMENSIONAL CASE

We begin by recalling the definitions of two-beam visibility  $v$ , degree of coherence  $\mu$ , and degree of polarization  $P$  in

classical optics for two scalar electromagnetic components  $E_{1,2}$ . We refer without distinctions to two different physical situations: two-beam interference when  $E_{1,2}$  are waves with the same state of polarization, and two-dimensional polarization when  $E_{1,2}$  are orthogonal components of a transversal vectorial wave  $\mathbf{E} = (E_1,E_2)$ . The standard definitions of  $v$ ,  $\mu$ , and  $P$  are

$$
v = 2 \left| \mu \right| \frac {\sqrt {I _ {1} I _ {2}}}{I _ {1} + I _ {2}}, \quad \mu = \frac {\left\langle E _ {1} ^ {*} E _ {2} \right\rangle}{\sqrt {I _ {1} I _ {2}}}, \tag {2.1}
$$

$$
P ^ {2} = \frac {\left(I _ {1} - I _ {2}\right) ^ {2} + 4 \left| \langle E _ {1} ^ {*} E _ {2} \rangle \right| ^ {2}}{\left(I _ {1} + I _ {2}\right) ^ {2}}, \tag {2.2}
$$

where  $I_{1,2} = \langle |E_{1,2}|^2 \rangle$  are the intensities and the angle brackets denote ensemble averages. Note that  $P \geqslant |\mu| \geqslant v$ . This holds even after unitary transformations  $U$  are applied to the original beams  $\mathbf{E}_U = U\mathbf{E}$ , so that  $\mu$  and  $v$  depend on  $U$  while  $P$  is  $U$ -invariant and  $P \geqslant |\mu(U)| \geqslant v(U)$ . These transformations are  $2 \times 2$  unitary matrices  $U^\dagger U = U U^\dagger = \mathcal{I}$ , where  $\mathcal{I}$  is the  $2 \times 2$  identity, that preserve the total intensity  $I_1(U) + I_2(U) = \text{const}$ , although the individual intensities  $I_j(U)$  may depend on  $U$  (as in the case of a lossless beam splitter, for example [12]). Thus  $P$  is the maximum visibility and coherence  $v_{\max} = |\mu|_{\max} = P$  that can be obtained when  $U$  is varied. The maximum is reached when the intensity is uniformly distributed between the beams  $I_1(U) = I_2(U)$  [2]. This nominates  $P$  as an intrinsic degree of coherence for the pair  $(E_1, E_2)$ .

# III. VISIBILITY AND COHERENCE FOR MULTIDIMENSIONAL WAVES

From now on we focus on  $N$  classical beams with complex amplitudes  $E_{m}$ ,  $m = 1,2,\ldots ,N$ . This approach can be applied to any multibeam situation. For the sake of illustration we refer to an elementary diffraction grating with  $N$  narrow enough slits,  $E_{m}$  being the field amplitudes at the slits. This analogy extends to other gratings provided that a single complex amplitude  $E_{m}$  is enough to describe the wave within each period of the grating.

The standard quantum translation of  $N$  classical beams is an  $N$ -dimensional Hilbert space. Let us consider a given basis of orthonormal vectors  $|\psi_m\rangle$ ,  $m = 1,2,\ldots,N$ , that represent the slits. For example, the particular case of deterministic amplitudes  $E_{m}$  is represented by the vector

$$
\left| \psi \right\rangle = \mathcal {N} \sum_ {m = 1} ^ {N} E _ {m} \left| \psi_ {m} \right\rangle , \quad \mathcal {N} = \left(\sum_ {\ell = 1} ^ {N} \left| E _ {\ell} \right| ^ {2}\right) ^ {- 1 / 2}, \tag {3.1}
$$

or, equivalently, by the density matrix  $\rho = |\psi\rangle\langle\psi|$ . Fluctuating fields are no longer represented by a vector but by a density matrix with  $\mathrm{tr}(\rho^2) < (\mathrm{tr}\rho)^2$ . The quantum-classical analogy is fully realized by identifying quantum density matrices  $\rho$  with cross-spectral density tensors  $W$ , i.e.,  $\langle \psi_{\ell}|\rho |\psi_{m}\rangle = W_{\ell,m} = \langle E_{\ell}E_{m}^{*}\rangle$ . Throughout we refer both to  $\rho$  and  $W$  simply as  $\rho$ , in the understanding that all results can be applied equally well to the quantum or classical domains. Without loss of generality we consider properly intensity-normalized fields  $\Sigma_{m=1}^{N}I_{m}=1$ , where  $I_{m} = \langle |E_{m}|^{2}\rangle = \langle \psi_{m}|\rho |\psi_{m}\rangle$ .

The variable  $m$  that indexes the beams can be represented by a single operator  $M$  defined as a  $N \times N$  diagonal matrix in the basis  $|\psi_m\rangle$ , so that  $|\psi_{m}\rangle$  are its eigenvectors.  $M$  represents how the intensity is distributed among the beams, so that the classical field intensities  $I_{m}$  become in the quantum domain the probabilities of the outcomes of a measurement of  $M$ .

There is no unique definition of visibility for nonharmonic fringes produced by the interference of multiple beams. For example, we have the classic normalized difference between the maxima and minima of the intensity, and more elaborate approaches such as the contrast of speckle patterns in terms of the variance of the intensity distribution [13]. The approach developed here is closer to this last possibility, as shown below in Eq. (4.7). A suitable multibeam generalization of Eq. (2.1) is provided by the Hilbert-Schmidt distance between the matrices  $\rho$  and  $\rho_{M}$  [9,10]

$$
v _ {M} ^ {2} = \frac {N}{N - 1} \operatorname {t r} \left[ \left(\rho - \rho_ {M}\right) ^ {2} \right] = \frac {N}{N - 1} \left[ \operatorname {t r} \left(\rho^ {2}\right) - \sum_ {m = 1} ^ {N} I _ {m} ^ {2} \right], \tag {3.2}
$$

or, equivalently,  $v_{M}^{2} = [N / (N - 1)]\Sigma_{\ell \neq m}|\langle E_{\ell}E_{m}^{*}\rangle |^{2}$ , where  $\rho_{M}$  is derived from  $\rho$  by removing all phase relationships in the  $|\psi_m\rangle$  basis,  $\langle \psi_{\ell}|\rho_{M}|\psi_{m}\rangle = I_{m}\delta_{\ell ,m},$

$$
\rho_ {M} = \left( \begin{array}{c c c} I _ {1} & 0 & \dots \\ 0 & I _ {2} & \dots \\ \vdots & \vdots & \ddots \end{array} \right). \tag {3.3}
$$

This can be physically understood as the result of phase randomization  $E_{\ell} \rightarrow E_{\ell} e^{i\varphi_{\ell}}$ , where  $\varphi_{\ell}$  are fully random and uncorrelated phase shifts.

For  $N = 2$  we have that  $v_{M}$  fully agrees with  $\upsilon$  in Eq. (2.1). In the general case maximum visibility  $v_{M}|_{\mathrm{max}} = 1$  is obtained provided that two necessary and sufficient conditions are fulfilled:  $\rho$  must be of the form  $\rho = |\psi \rangle \langle \psi |$  so that  $\operatorname {tr}\rho^2 = 1$  , and the intensity distribution must be uniform  $I_{m} = 1 / N$  . The minimum  $v_{M}|_{\min} = 0$  occurs for  $\rho = \rho_{M}$

A key point is that  $v_{M}$  and  $\rho_{M}$  depend both on  $\rho$  and on the basis  $|\psi_m\rangle$ , so these quantities are indexed by  $M$ , since  $|\psi_m\rangle$  are the eigenvectors of  $M$ . This is the analog of the dependence of  $\mu$  and  $v$  on  $U$  in Sec. II. The statistics of  $M$  appears explicitly in Eq. (3.2) in the form of a suitable measure of fluctuations  $C_M$  alternative to variance, which may be referred to as certainty [7],

![](images/4c1c7266d6555b4bc956d98829de6fab75d8899aeaa4f9d918d430e4606850c7.jpg)  
FIG. 1. Pythagoras theorem in Eq. (3.5).

$$
C _ {M} ^ {2} = \frac {N}{N - 1} \operatorname {t r} \left[ \left(\rho_ {M} - \frac {1}{N} \mathcal {T}\right) ^ {2} \right] = \frac {N}{N - 1} \sum_ {m = 1} ^ {N} \left(I _ {m} - \frac {1}{N}\right) ^ {2}, \tag {3.4}
$$

where  $\mathcal{I}$  is the  $N\times N$  identity matrix.  $C_M$  represents the degree of certainty one can have concerning the  $m$  variable. The maximum  $C_M = 1$  occurs when the distribution is concentrated in a single value,  $I_{m} = \delta_{m,n}$  (full certainty about  $m$  and the quantum measurement of  $M$  always provides the same outcome). The minimum  $C_M = 0$  occurs when the distribution is uniform  $I_{m} = 1 / N$  (full uncertainty about  $m$ , and all the outcomes of the measurement of  $M$  are equally probable). With this definition Eq. (3.2) can be expressed as

$$
v _ {M} ^ {2} + C _ {M} ^ {2} = P ^ {2}, \tag {3.5}
$$

where

$$
P ^ {2} = \frac {N}{N - 1} \operatorname {t r} \left[ \left(\rho - \frac {1}{N} \mathcal {I}\right) ^ {2} \right] = \frac {N}{N - 1} \operatorname {t r} \left(\rho^ {2}\right) - \frac {1}{N - 1} \tag {3.6}
$$

is independent of  $M$ . Let us note that Eq. (3.5) is a version of the Pythagoras theorem as illustrated in Fig. 1, since  $\rho - \rho_{M}$  and  $\rho_{M} - \mathcal{I} / N$  are orthogonal  $\mathrm{tr}[(\rho - \rho_{M})(\rho_{M} - \mathcal{I} / N)] = 0$ .

Let us dwell briefly on the multiple meanings of  $P$ . In quantum mechanics Eq. (3.5) has been considered as expressing wave-particle duality, by regarding  $C_M^2$  as a measure of the amount of information about the path followed by the interfering particle. In this regard  $P$  has been proposed as a measure of total information [9,11].

From the classical-optics perspective,  $P$  is exactly the degree of polarization of the  $N$ -dimensional wave  $\mathbf{E} = (E_1, \dots, E_N)$  [3].  $P$  has been also proposed as a measure of the degree of coherence conveyed by multidimensional waves [2].

$P$  can be expressed also as an average of two-beam coherence. This is because in every basis  $|\psi_m\rangle$ ,  $\mathrm{tr}(\rho^2) = \Sigma_{k,m=1}^{N} |\langle \psi_k | \rho | \underline{\psi}_m \rangle|^2 = \Sigma_{k,m=1}^{N} I_k I_m |\mu_{k,m}|^2$ , where  $\mu_{k,m} = \langle \psi_k | \rho | \psi_m \rangle / \sqrt{I_k I_m}$ , so that  $\mathrm{tr}(\rho^2)$  and  $P$  are given by an intensity-weighted average of the two-beam degrees of coherence in Eq. (2.1) between all pairs of beams. In the limit  $N \to \infty$  we have that  $P$  becomes the overall degree of coherence in Ref. [14].

The interpretation of  $P$  as an intrinsic degree of coherence agrees well with the two-beam case in Sec. II since  $v_{M}|_{\max} = P$ , and the maximum visibility occurs when  $I_{m}$  is uniformly distributed and  $C_{M} = 0$ . The maximum can be reached for every  $\rho$  since we can find always operators  $\widetilde{M}$  with  $C_{\widetilde{M}} = 0$ . For example, this is the case of the operator  $\widetilde{M}$  diagonal in

the basis  $|\widetilde{\psi}_m\rangle = (1 / \sqrt{N})\Sigma_{j = 1}^N\exp (i\frac{2\pi jm}{N})|\lambda_j\rangle$ , where  $|\lambda_j\rangle$  is the orthonormal basis of eigenvectors of  $\rho$ , so that  $\rho$  and  $\widetilde{M}$  are complementary.

# IV. COHERENCE, VISIBILITY, AND PHASE STATISTICS

Next we elaborate on the relation between visibility, coherence, and phase statistics. To this end, let us note the existence of an uncertainty relation extremely similar to Eq. (3.5) involving the certainties of  $M$  and its complementary operator  $K$  [7,11],

$$
P ^ {2} \geqslant C _ {K} ^ {2} + C _ {M} ^ {2}, \tag {4.1}
$$

where  $K$  is the phase operator defined by its eigenstates (phase states) [4]  $|\phi_k\rangle = (1 / \sqrt{N})\Sigma_{m = 1}^N\exp (im\phi_k)|\psi_m\rangle$ $\phi_{k}$ $= 2\pi k / N + \phi_0$  , where  $\phi_0$  is an arbitrary phase. Thus  $C_K$  is the phase certainty

$$
C _ {K} ^ {2} = \frac {N}{N - 1} \sum_ {k = 1} ^ {N} \left(J _ {k} - \frac {1}{N}\right) ^ {2}, \tag {4.2}
$$

where  $J_{k}$  is the phase distribution  $J_{k} = \langle \phi_{k}|\rho |\phi_{k}\rangle$  . In most situations the discreteness of the phase variable  $\phi_{k}$  can be troublesome, especially due to the arbitrariness of the parameter  $\phi_0$  . More practical relations are obtained if we define the phase distribution as a function of a continuous variable  $\phi$  in the form  $I(\phi) = \langle \phi |\rho |\phi \rangle$  , where [4]

$$
| \phi \rangle = \frac {1}{\sqrt {2} \pi} \sum_ {m = 1} ^ {N} \exp (i m \phi) | \psi_ {m} \rangle . \tag {4.3}
$$

The associated certainty

$$
C _ {\phi} ^ {2} = \frac {N}{N - 1} \int_ {2 \pi} d \phi \left(I (\phi) - \frac {1}{2 \pi}\right) ^ {2} \tag {4.4}
$$

can be embodied in an uncertainty relation by integrating Eq. (4.1) on  $\phi_0$  over a  $2\pi /N$  interval, leading to

$$
P ^ {2} \geqslant C _ {\phi} ^ {2} + C _ {M} ^ {2}. \tag {4.5}
$$

We can propose two meanings for  $C_{\phi}$ . On the quantum side this is a measure of the width of the phase distribution  $I(\phi)$ . This has been used, for example, to demonstrate the enforcement of complementarity by the randomization of relative phase produced even by the most subtle observations of quantum interference [8]. In the classical domain  $I(\phi) = \langle \phi |\rho |\phi \rangle$  is the intensity distribution in the far plane produced by a diffraction grating,  $\phi$  being the relative phase between consecutive beams [see Fig. 2(a)]. Therefore  $C_{\phi}$  represents a suitable assessment of visibility measured as the distance between  $I(\phi)$  and the uniform distribution  $1 / (2\pi)$  [15].

From Eqs. (3.5), (4.1), and (4.5) we get the following chains of inequalities  $P \geqslant v_{M} \geqslant C_{K}$  and  $P \geqslant v_{M} \geqslant C_{\phi}$ . Let us elucidate their meaning by relating them with a series of increasingly general interferometers. We have already noticed that  $C_{\phi}$  is the visibility of far-field fringes produced by a diffraction grating with a definite phase difference  $\phi$  between consecutive beams [Fig. 2(a)]. More general interfer

![](images/2aff52d456679a39cd15d37996ef2a4944ce11a53335574b43b3d6b54e8f0471.jpg)  
FIG. 2. Interferometric schemes whose visibilities are (a)  $C_{\phi}$ , (b)  $v_{M}$ , and (c)  $P$ .

![](images/743bda25b32afc6fe2960445d11151a70af26a7bc9fdffc6b5b76b241dfea4ad.jpg)

![](images/10be8f5b4b16cd73d923199838b8a4c79e0ddc268f38b8508bbd88f88eb0f63a.jpg)

ometers are obtained when the phase shifts  $\phi_{m}$  experienced by each beam are independent variables  $\phi_{m} \neq m\phi$ , as illustrated in Fig. 2(b). This leads to a multidimensional fringe pattern  $I(\Phi) = \langle \Phi |\rho |\Phi \rangle$ , where  $|\Phi \rangle$  are the vector phase states [16]

$$
\left| \Phi \right\rangle = \frac {1}{\sqrt {(2 \pi) ^ {N}}} \sum_ {m = 1} ^ {N} \exp (i \phi_ {m}) \left| \psi_ {m} \right\rangle , \tag {4.6}
$$

and  $v_{M}$  can be expressed as the distance between  $I(\Phi)$  and the uniform distribution  $1 / (2\pi)^{N}$  [9,15],

$$
v _ {M} ^ {2} = \frac {N (2 \pi) ^ {N}}{N - 1} \int d \Phi \left[ I (\Phi) - \frac {1}{(2 \pi) ^ {N}} \right] ^ {2}, \tag {4.7}
$$

with  $d\Phi = d\phi_{1}\dots d\phi_{N}$ . Thus the inequality  $v_{M} \geqslant C_{\phi}$  can be ascribed to the fact that  $v_{M}$  is the visibility of interferometers with a larger number of degrees of freedom. Finally,  $P \geq v_{M}$  holds since  $P$  is the largest fringe visibility reached when considering the most arbitrary linear energy-conserving interferometer. This is illustrated in Fig. 2(c), where a  $N \times N$  lossless beam splitter (BS) [12] combines the input amplitudes so that both the phases and the intensities of the interfering waves are independent variables.

# V. CONCLUSIONS

We have developed a complete connection between coherence and visibility for multidimensional systems in the classical and quantum domains, leaving aside naturally fundamental differences between both theories in other aspects. More specifically, the quantum-classical connection refers to the following points. Quantum complementarity and uncertainty relations become equivalent to classic relations between coherence, visibility, and intensity distributions in the classical domain. Quantum phase distribution parallels the fringes of a classical grating in the far field, so that quantum-phase uncertainty becomes a measure of fringe visibility. The classical degree of polarization of multidimensional waves becomes an intrinsic degree of coherence as the maximum fringe visibility and a suitable measure of information. This degree is also the weighted average of the two-beam degree of coherence for pairs of components.

# ACKNOWLEDGMENT

This work has been supported by Project No. PR1-A/07-15378 of the Universidad Complutense.

[1] H. M. Ozaktas, S. Yüksel, and M. A. Kutay, J. Opt. Soc. Am. A 19, 1563 (2002); E. Wolf, Phys. Lett. A 312, 263 (2003); J. Tervo, T. Setälä, and A. T. Friberg, Opt. Express 11, 1137 (2003); P. Réfrégier and F. Goudail, ibid. 13, 6051 (2005).  
[2] A. Luis, J. Opt. Soc. Am. A 24, 1063 (2007).  
[3] R. Barakat, Opt. Commun. 23, 147 (1977); J. C. Samson and J. V. Olson, SIAM J. Appl. Math. 40, 137 (1981).  
[4] T. S. Santhanam, Phys. Lett. 56A, 345 (1976); M. Grabowski, Int. J. Theor. Phys. 28, 1215 (1989); A. Luis and L. L. Sánchez-Soto, Phys. Rev. A 48, 4702 (1993).  
[5] P. Busch and Ch. Shilladay, Phys. Rep. 435, 1 (2006).  
[6] M. Mei and M. Weitz, Phys. Rev. Lett. 86, 559 (2001); A. Luis, J. Phys. A 34, 8597 (2001); Phys. Rev. Lett. 88, 230401 (2002); G. Bimonte and R. Musto, Phys. Rev. A 67, 066101 (2003); J. Phys. A 36, 11481 (2003).  
[7] E. J. Heller, Phys. Rev. A 35, 1360 (1987); H. Maassen and J. B. M. Uffink, Phys. Rev. Lett. 60, 1103 (1988); U. Larsen, J. Phys. A 23, 1041 (1990); A. Luis, Phys. Rev. A 67, 032108 (2003).

[8] A. Luis and L. L. Sánchez-Soto, Phys. Rev. Lett. 81, 4031 (1998).  
[9] S. Durr, Phys. Rev. A 64, 042113 (2001).  
[10] F. Herbut, J. Phys. A 38, 2959 (2005).  
[11] C Brukner and A. Zeilinger, Phys. Rev. A 63, 022113 (2001).  
[12] By lossless beam splitters we refer to any device whose action on  $N$  input waves can be described by a  $N\times N$  unitary matrix  $U$  relating input and output complex amplitudes  $E_{j}(U) = \Sigma_{k = 1}^{N}U_{j,k}E_{k}$  so that the output waves carry the same total intensity as the input waves  $\Sigma_{j = 1}^{N}|E_{j}(U)|^{2} = \Sigma_{k = 1}^{N}|E_{k}|^{2}$ . For  $N = 2$  this includes standard lossless beam splitting in basic two-beam interferometers.  
[13] J. W. Goodman, Statistical Optics (Wiley, New York, 1985).  
[14] M. J. Bastiaans, J. Opt. Soc. Am. A 3, 1227 (1986).  
[15] A. Luis, J. Phys. A 35, 8805 (2002).  
[16] B. C. Sanders, H. de Guise, D. J. Rowe, and A. Mann, J. Phys. A 32, 7791 (1999).