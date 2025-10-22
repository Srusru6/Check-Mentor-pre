# Method for Direct Detection of Quantum Entanglement

Pawel Horodecki

Faculty of Applied Physics and Mathematics, Technical University of Gdańsk, 80-952 Gdańsk, Poland

Artur Ekert

Department of Applied Mathematics and Theoretical Physics, University of Cambridge, Cambridge CB3 0WA, United Kingdom (Received 7 February 2002; published 30 August 2002)

Basing on positive maps separability criterion we propose the experimentally viable, direct detection of quantum entanglement. It is efficient and does not require any a priori knowledge about the state. For two qubits it provides a sharp (i.e., "if and only if") separability test and estimation of amount of entanglement. We view this method as a new form of quantum computation, namely, as a decision problem with quantum data structure.

DOI: 10.1103/PhysRevLett.89.127902

PACS numbers: 03.65.Ud, 03.65.Wj, 03.67.Lx

Quantum entanglement, after playing a significant role in the development of the foundations of quantum mechanics [1-3], has been recently rediscovered as a new physical resource with potential commercial applications such as, for example, quantum cryptography [4], better frequency standards [5] or quantum-enhanced positioning, and clock synchronization [6]. On the mathematical side the studies of entanglement have revealed very interesting connections with the theory of positive maps [7,8]. The capacity to generate entangled states is one of the basic requirements for building quantum computers. Hence, efficient experimental methods for detection, verification, and estimation of quantum entanglement are of great practical importance. Here, we propose an experimentally viable, direct detection of quantum entanglement which is efficient and does not require any a priori knowledge about the quantum state. In a particular case of two entangled qubits it provides an estimation of the amount of entanglement. We view this method as a new form of quantum computation, namely, as a decision problem with quantum data structure.

Suppose we are given  $n$  pairs of particles, all in the same quantum state described by some density operator  $\varrho$ , which is unknown. We need to decide whether the particles in each pair are entangled or not. From a mathematical point of view we need to assert whether  $\varrho$  can be written as a convex sum of product states [9],

$$
\varrho = \sum_ {i} ^ {k} p _ {i} | \alpha_ {i} \rangle \langle \alpha_ {i} | \otimes \beta_ {i} \rangle \langle \beta_ {i} |, \tag {1}
$$

with  $|\alpha_i\rangle$  and  $|\beta_{i}\rangle$  pertaining to different particles in the pair, and  $\sum_{i}p_{i} = 1$ . It is assumed that the Hilbert space associated with each particle is of finite dimension  $d$  (taken to be the same for the two particles), so that one can always find  $k\leq d^{2}$ . If  $\varrho$  were known then we could try either to find the decomposition (1) directly or to use one of the mathematical separability criteria [8]. For sufficiently large  $n$  we may indeed start with the quantum state estimation,

however, this involves estimating  $d^4 - 1$  real parameters of  $\varrho$ , most of which are irrelevant in the context of the entanglement detection. In the following we describe a direct method of detecting quantum entanglement without invoking the state estimation.

We construct a measurement, performed on all copies of  $\varrho$ , which is as powerful in detecting quantum entanglement as the best mathematical test based on positive maps [7]. (Special cases of the direct detection of entanglement, restricted to pure states of the combined system, were discussed by Sancho et al. [10] and by Acin et al. [11].) The measurement can be viewed as two consecutive physical operations: first, we construct a transformation which maps  $\varrho$  into an appropriate state  $\varrho'$  and, second, we measure the lowest eigenvalue of  $\varrho'$ . This eigenvalue alone serves as a separability indicator.

A convenient starting point for our construction is the most powerful, albeit purely mathematical and not directly implementable, separability criterion proposed to date. It is based on mathematical properties of linear positive maps acting on matrices [7]. Let  $M_d$  be a space of matrices of dimension  $d$ ; recall that  $\Lambda : M_d \mapsto M_d$  is called positive if  $X \geq 0$  implies  $\Lambda(X) \geq 0$  (expression  $X \geq 0$  means that the matrix  $X$  has a non-negative spectrum). If the induced map  $\mathbb{I} \otimes \Lambda$  is also positive, then  $\Lambda$  is called completely positive, and, as such, it represents a physically allowed transformation of density operators (here  $\mathbb{I}$  denotes the identity map on an auxiliary system of any dimension). Using this terminology the separability criterion reads [7]:  $\varrho$  is separable if and only if

$$
[ \mathbb {I} \otimes \Lambda ] (\varrho) \geq 0, \tag {2}
$$

for all positive but not completely positive maps  $\Lambda : M_d \mapsto M_d$  acting on the second particle. In fact it is sufficient to consider only positive maps  $\Lambda$  such that the maximum of  $\operatorname{Tr} \Lambda(\varrho)$  over all  $\varrho$  is equal to unity. Other positive maps differ only by a positive multiplicative factor which does not affect the condition (2).

Furthermore, in some cases, instead of scanning all positive maps, we can choose just one. For example, all entangled states of two qubits can be detected by choosing  $\Lambda$  to be transposition [7,12]. The snag is that positive maps  $\Lambda$ , such as an antiunitary transposition, and the corresponding induced maps  $\mathbb{I} \otimes \Lambda$  cannot be implemented in a laboratory. Thus, the criterion (2) tacitly assumes prior knowledge of  $\varrho$ . However, there is a way to modify it so that it becomes experimentally viable without involving any state estimation.

If we mix in an appropriate proportion  $[ \mathbb{I} \otimes \Lambda ]$  with a depolarizing map that turns any density matrix into a maximally mixed state then the resulting map can be completely positive. This is because the lowest negative eigenvalues generated by the induced map  $\left[ (\mathbb{I} \otimes \mathbb{I}) \otimes (\mathbb{I} \otimes \Lambda) \right]$  can be offset by the positive eigenvalues of the maximally mixed state generated by the depolarizing map. The most negative eigenvalue  $-\lambda < 0$  is obtained when  $\left[ (\mathbb{I} \otimes \mathbb{I}) \otimes (\mathbb{I} \otimes \Lambda) \right]$  acts on the maximally entangled state of the form  $\frac{1}{\sqrt{d^2}} \sum_{i=1}^{d^2} |i\rangle |i\rangle$ , where each state  $|i\rangle$  pertains to a  $d^2$  dimensional subsystem which itself is composed of two  $d$  dimensional parts. Thus the map,

$$
[ \mathbb {I} \widetilde {\otimes} \Lambda ] (\varrho) = p \frac {I \otimes I}{d ^ {2}} + (1 - p) [ \mathbb {I} \otimes \Lambda ] (\varrho), \tag {3}
$$

is completely positive and therefore physically implementable when the induced map  $\left[(\mathbb{I} \otimes \mathbb{I}) \otimes (\widetilde{\mathbb{I} \otimes \Lambda})\right]$  is positive, which happens for  $p \geq (d^4 \lambda) / (d^4 \lambda + 1)$  [13]. By inserting the threshold value  $p = (d^4 \lambda) / (d^4 \lambda + 1)$  into (3) we can modify the criterion (2) as follows:  $\varrho$  is separable if and only if for all positive maps  $\Lambda$ ,

$$
[ \mathbb {I} \widetilde {\otimes} \Lambda ] (\varrho) \geq \frac {d ^ {2} \lambda}{d ^ {4} \lambda + 1}, \tag {4}
$$

i.e., when the minimal eigenvalue of the transformed state  $\varrho' = [\mathbb{I} \widetilde{\otimes} \Lambda](\varrho)$  is greater than  $(d^2 \lambda) / (d^4 \lambda + 1)$ . In general, for some maps  $\Lambda$ , the related completely positive maps  $\mathbb{I} \widetilde{\otimes} \Lambda$  are not trace preserving and require postselec

tions in their physical implementations. Maps such as  $\mathbb{I} \widetilde{\otimes} \Lambda$  have been referred to as "structural" physical approximations (SPA) to unphysical maps  $\mathbb{I} \otimes \Lambda$ . The notion of SPA was introduced and analyzed recently [13]. Note that the universal NOT gate [14] can be considered as a first example of SPA (the one being approximation to one qubit universal NOT operation).

For example, if we take  $\Lambda$  to be transposition  $T$  (the first positive map used for detecting entanglement), we obtain

$$
[ \mathbb {I} \widetilde {\otimes} T ] (\varrho) = \frac {d}{d ^ {3} + 1} I \otimes I + \frac {1}{d ^ {3} + 1} [ \mathbb {I} \otimes T ] (\varrho). \qquad (5)
$$

In the two-qubit case, where the partial transposition gives the sharp test for entanglement, we obtain

$$
[ \mathbb {I} \widetilde {\otimes} T ] (\varrho) = \frac {2}{9} I \otimes I + \frac {1}{9} [ \mathbb {I} \otimes T ] (\varrho), \tag {6}
$$

which can be represented and implemented as

$$
\frac {1}{3} \Lambda_ {1} \otimes \Lambda_ {2} + \frac {2}{3} \mathbb {I} \otimes \sigma_ {x} \sigma_ {z} \Lambda_ {1} \sigma_ {z} \sigma_ {x}, \tag {7}
$$

with the two channels defined as

$$
\Lambda_ {1} (\varrho) = \frac {1}{3} \sum_ {i = x, y, z} \sigma_ {i} \varrho \sigma_ {i}, \quad \Lambda_ {2} (\varrho) = \frac {1}{4} \sum_ {i = o, x, y, z} \sigma_ {i} \varrho \sigma_ {i}. \tag {8}
$$

The map can be implemented by applying selected products of unitary (Pauli) transformations with the prescribed probabilities. The map is trace preserving; hence it can be implemented without postselections.

Thus, in order to detect entanglement of an arbitrary two-qubit state  $\varrho$  it is enough to estimate a single parameter, i.e., the minimal eigenvalue of  $[\widetilde{\mathbb{I}\otimes T}](\varrho)$ . The state  $\varrho$  is separable if and only if this eigenvalue satisfies  $\lambda_{\min} \geq \frac{2}{9}$ . Let us also point out an extra bonus:  $\lambda_{\min}$  gives us  $-\lambda'$ , the most negative eigenvalue of  $[\mathbb{I}\otimes T](\varrho)$ , which enters the expression for the upper and lower bounds for the entanglement of formation,

$$
H \left(\frac {1 + \sqrt {1 - 4 \lambda^ {\prime 2}}}{2}\right) \leq E (\varrho) \leq H \left(\frac {1 + \sqrt {1 - 4 \left(\sqrt {2 \lambda^ {\prime 2} + \lambda^ {\prime}} - \lambda^ {\prime}}\right)}}{2}\right), \tag {9}
$$

where  $H(x)$  is the Shannon entropy. The above formulas can be derived from the estimations of the concurrence provided by Verstraete et al. [15].

Suppose for a moment that  $\mathbb{I}\widetilde{\otimes}\Lambda$  is trace preserving, e.g., the case of transposition. The first part of our entanglement detection measurement is accomplished by applying  $\mathbb{I}\widetilde{\otimes}\Lambda$  to each of the  $n$  pairs to obtain  $n$  copies of  $\varrho^{\prime} = [\mathbb{I}\widetilde{\otimes}\Lambda](\varrho)$ . Then, following the criterion (4), we need to measure the lowest eigenvalue of  $\varrho^{\prime}$ .

This can be viewed as a special case of the spectrum estimation and possible approaches depend a lot on particular physical realizations of  $\varrho^{\prime}$ . Here, we provide two general solutions. The first one, based on quantum inter

ferometry, is conceptually simple and relies on estimating  $d^2 - 1$  parameters from which the spectrum of  $\varrho'$  can be calculated (this is a significant gain over the state estimation which involves  $d^4 - 1$  parameters). The second solution is a joint measurement on all copies of  $\varrho'$  which gives directly the estimate of the lowest eigenvalue.

We start with the quantum interferometry, presented here as a quantum network shown in Fig. 1. A typical interferometric setup for a single qubit—the Hadamard gate, phase shift  $\phi$ , the Hadamard gate, followed by a measurement—is modified by inserting in-between the Hadamard gates a controlled- $U$  operation, with its control

![](images/6a8d1249e0d821ce439ec981acd94f4d0cfd92191d201e857293bb53bd355847.jpg)  
FIG. 1 (color online). Both the visibility and the shift of the interference patterns of a single qubit (top line) are affected by the controlled-  $U$  operation. This setup allows one to estimate  $\mathrm{Tr}U\rho$ , the average value of  $U$  in state  $\rho$ .

on the qubit and with  $U$  acting on a quantum system described by some unknown density operator  $\rho$ . (N.B. we do not assume anything about the form of  $\rho$ ; it can, for example, describe several entangled or separable subsystems.) The action of the controlled  $U$  on  $\rho$  modifies the interference pattern by the factor,

$$
\operatorname {T r} \rho U = v e ^ {i \alpha}, \tag {10}
$$

where  $\nu$  is the new visibility and  $\alpha$  is the shift of the interference fringes, also known as the Pancharatnam phase [16]. Formula (10) has been derived, in the context of geometric phases, by Sjöqvist et al. [17].

The network can evaluate certain nonlinear functionals of density operators. Indeed, let us choose  $\rho$  to be composed of two subsystems,  $\rho = \varrho_{a}\otimes \varrho_{b}$ , and let  $U$  to be the exchange operator  $V$  such that  $V|\alpha \rangle |\beta \rangle = |\beta \rangle |\alpha \rangle$  for any pure states of the two subsystems. The interference pattern is now modified by the factor  $\mathrm{Tr}V(\varrho_a\otimes \varrho_b) = \mathrm{Tr}\varrho_a\varrho_b$ . For  $\rho = \varrho \otimes \varrho$  we can estimate  $\mathrm{Tr}\varrho^2$ , which gives us an estimate of  $\sum_{i = 1}^{m}\lambda_{i}^{2}$ , where  $\lambda_{i}$  are the eigenvalues of  $\varrho$  (c.f. work by Filip on the quantum optical measurement of  $V$  [18]). N.B.  $\mathrm{Tr}\varrho^2$  is real hence there is no need to sweep the phase  $\varphi$  in the interferometer; it can be fixed at  $\varphi = 0$ .

In general, in order to calculate the spectrum of any  $m \times m$  density matrix  $\varrho$  we need to estimate  $m - 1$  parameters  $\mathrm{Tr}\varrho^2$ ,  $\mathrm{Tr}\varrho^3$ , ...  $\mathrm{Tr}\varrho^m$ . For this we need the controlled-shift operation. Given  $k$  systems of dimension  $m$  we define the shift  $V^{(k)}$  as

$$
V ^ {(k)} | \phi_ {1} \rangle | \phi_ {2} \rangle \dots | \phi_ {k} \rangle = | \phi_ {k} \rangle | \phi_ {1} \rangle \dots | \phi_ {k - 1} \rangle , \tag {11}
$$

for any states  $|\phi \rangle$ . Such an operation can be easily constructed by cascading  $k - 1$  swaps  $V$ . This time, if we prepare  $\rho = \varrho^{\otimes k}$  the interference will be modified by the factor

$$
\operatorname {T r} \varrho^ {\otimes k} V ^ {(k)} = \operatorname {T r} \varrho^ {k} = \sum_ {i = 1} ^ {m} \lambda_ {i} ^ {k}. \tag {12}
$$

Thus measuring the average values of  $V^{(k)}$  for  $k = 2, 3, \ldots, m$  gives us effectively the spectrum of  $\varrho$ . In particular, in our case, we obtain the spectrum (and the lowest eigenvalue) of  $\varrho' = [\mathbb{I} \widetilde{\otimes} \Lambda](\varrho)$  by estimating  $d^2 - 1$  parameters  $\mathrm{Tr}\varrho'^k$ , where  $k = 2 \cdots d^2$ . Again, the phase in the interferometry can be fixed at  $\varphi = 0$ .

The interferometric scheme described above is conceptually simple and experimentally viable; however, if the simplicity of the implementation is not an issue then we can measure the estimate of the lowest eigenvalue directly. This requires a join measurement on all of the  $n$  pairs. We use the Keyl and Werner spectrum estimation method [19], which is based on projections on subspaces invariant under permutations [20]. In the entanglement detection context it works as follows. The  $n$  copies of the  $m \times m$  state  $\varrho'$  (in our case  $m = d^2$ ) form an operator on the  $n$ -fold tensor product space which can be decomposed according to irreducible representations of  $\mathrm{SU}(m)$ , so that each summand, including multiplicities, is labeled by a Young tableau, i.e.,  $n$  boxes arranged in rows of decreasing length. The tableaus give a family of projectors for the spectrum estimation measurement. The normalized row lengths of each tableau are taken as estimates of the ordered sequence of eigenvalues of  $\varrho'$ . The probability that the error is greater than some fixed  $\epsilon$  decreases exponentially with  $n$  [19]. In our particular case, we are interested only in the lowest eigenvalue. We modify the Keyl-Werner scheme by adding together all projectors corresponding to Young tableaus with the fixed length of the last row. The measurement determined by these projectors gives directly the estimate of only one parameter — the lowest eigenvalue of  $\varrho'$ . Such a measurement can be represented as a quantum network implementing projections on the symmetric and on partially symmetric subspaces (see [21] for the network projecting on the symmetric subspace).

Our considerations remain valid, with some minor modifications, when  $\mathbb{I}\widetilde{\otimes}\Lambda$  is not trace preserving. In this case experimental implementations require postselections, which result in  $n' = n\mathrm{Tr}[\mathbb{I}\widetilde{\otimes}\Lambda(\varrho)]$  copies of normalized states  $\mathbb{I}\widetilde{\otimes}\Lambda(\varrho)/\mathrm{Tr}[\mathbb{I}\widetilde{\otimes}\Lambda(\varrho)]$ . The spectrum estimation procedure is not affected; however, before checking the condition (4) the lowest eigenvalue has to be rescaled by the factor  $\mathrm{Tr}[\mathbb{I}\widetilde{\otimes}\Lambda(\varrho)]$ .

Let us summarize our findings. Given  $n$  copies of a bipartite  $d \otimes d$  system described by some unknown density operator  $\varrho$  we can test for entanglement either by estimating  $\varrho$  and applying criterion (2), or, more directly, by performing the measurements we have just described. The state estimation involves estimating  $d^4 - 1$  parameters of  $\varrho$ , most of which are of no relevance for the entanglement detection. The optimal state estimations rely on joint measurements on all copies of  $\varrho$ ; however, one can also construct less efficient but simpler state estimation methods which involve measurements only on individual copies. Our more direct, interferometry based, method requires estimations of only  $d^2 - 1$  parameters and joint operations on  $d$  copies of  $\varrho'$ . The most demanding, from the experimental point of view, is our second method. It is a measurement with an outcome which is an estimate of just one parameter, but, like the optimal state estimation, the measurement involves joint operations on all copies of  $\varrho'$ . Both direct and indirect entanglement detections have their own merits. Depending on the context, applications, and

technologies involved one can choose one or the other. Note that for two qubits the present interferometric method provides a sharp entanglement test involving final measurements of only three ( $d^2 - 1 = 2^2 - 1 = 3$ ) observables.

Direct entanglement detections can be employed as subroutines in quantum computation. For example, one may consider performing or not performing a quantum operation on a given quantum system conditioned on some part of quantum data being entangled or not. In fact direct entanglement detections can be viewed as quantum computations solving an inherently quantum decision problem: given as an input  $n$  copies of  $\varrho$  decide whether  $\varrho$  is entangled. Here the input data are quantum and such a decision problem cannot even be formulated for classical computers. Nonetheless the problem is perfectly well defined for quantum computers. Finally, let us add that the method presented here can be easily generalized to cover all linear maps tests for arbitrary multiparticle entanglement [22] and the so-called  $k$ -positive map tests, which detect Schmidt numbers of density matrices [23]. Further extension of our method to the case of detecting quantum entanglement at a distance, i.e., under restrictions of local operations and classical communication [8], will be considered elsewhere.

For the sake of completeness we should also mention here that there is an important theory of multiparticle observables, called entanglement witnesses, which can detect quantum entanglement in some special cases (see [7,8,24,25]). They have positive mean values on all separable states and negative on some entangled states. Therefore any individual entanglement witness leaves many entangled states undetected. When  $\varrho$  is unknown we need to check infinitely many witnesses, which effectively reduces this approach to the quantum state estimation. Still, in the context of our method, witnesses are useful as they define positive maps which can be used in our test.

To conclude, we have demonstrated that direct and physically implementable methods of entanglement detection are possible. They are equivalent to the most powerful mathematical separability criteria known to date [7]. We have described their possible realizations in the generic terms of quantum gates and networks. These generic components can be implemented using several experimental techniques ranging from trapped ions to quantum dots [26].

This research was supported in part by the European Commission (Project EQUIP No. IST-1999-11053), Elsag Spa, EPSRC, and the Royal Society, London.

[1] Erwin Schrödinger, Naturwissenschaften 48, 807 (1935).  
[2] A. Einstein, B. Podolsky, and N. Rosen. Phys. Rev. 47, 777 (1935).  
[3] J. S. Bell, Physics (Long Island City, New York) 1, 195 (1964).  
[4] A.K. Ekert, Phys. Rev. Lett. 67, 661 (1991).  
[5] J.J. Bollinger, W.M. Itano, D.J. Wineland, and D.J. Heinzen, Phys. Rev. A 54, R4649 (1996).  
[6] V. Giovannetti, S. Lloyd, and L. Maccone, Nature (London) 412, 417 (2001).  
[7] M. Horodecki, P. Horodecki, and R. Horodecki, Phys. Lett. A 223, 1 (1996).  
[8] G. Alber, T. Beth, M. Horodecki, P. Horodecki, R. Horodecki, M. Röttler, H. Weinfurter, R.F. Werner, and A. Zeilinger, Quantum Information: An Introduction to Basic Theoretical Concepts and Experiments, Springer Tracts in Modern Physics Vol. 173 (Springer, New York, 2001).  
[9] R.F. Werner, Phys. Rev. A 40, 4277-4281 (1989).  
[10] J. M. G. Sancho and S. F. Huelga, Phys. Rev. A 61, 042303 (2000).  
[11] A. Acin, R. Tarrach, and G. Vidal, Phys. Rev. A 61, 62 307 (2000).  
[12] A. Peres, Phys. Rev. Lett. 77, 1413-1415 (1996).  
[13] P. Horodecki, quant-ph/0111036.  
[14] V. Buzek, M. Hilery, and R.F. Werner, Phys. Rev. A 60, R2626 (1999).  
[15] F. Verstraete, K. Audenaert, J. Dehaene, and D. de Moor, J. Phys. A 34, 10327 (2002).  
[16] S. Pancharatnam, Proc. Indian Acad. Sci. XLIV, 247 (1956).  
[17] E. Sjöqvist, A.K. Pati, A. Ekert, J.S. Anandan, M. Ericsson, D.K.L. Oi, and V. Vedral, Phys. Rev. Lett. 85, 2845 (2000).  
[18] R. Filip, quant-ph/0108119.  
[19] M. Keyl and R.F. Werner, Phys. Rev. A 64, 052311 (2001).  
[20] J.I. Cirac, A.K. Ekert, and C. Macchiavello, Phys. Rev. Lett. 82, 4344 (1999).  
[21] A. Barenco, A. Berthiaume, D. Deutsch, A. Ekert, R. Jozsa, and C. Macchiavello, SIAM J. Comput. 26, 1541 (1997).  
[22] M. Horodecki, P. Horodecki, and R. Horodecki, Phys. Lett. A 283, 1 (2001).  
[23] B. M. Terhal and P. Horodecki, Phys. Rev. A 61, 040301-040305 (2000).  
[24] B. M. Terhal, quant-ph/0101032.  
[25] D. Bruß, J.I. Cirac, P. Horodecki, F. Hulpke, B. Kraus, M. Lewenstein, and A. Sanpera, J. Mod. Opt. 49, 1399 (2002).  
[26] The Physics of Quantum Information: Quantum Cryptography, Quantum Teleportation, Quantum Computation, edited by Dirk Bouwmeester, Artur K. Ekert, and Anton Zeilinger (Springer, New York, 2000).