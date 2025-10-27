# Entanglement in Quantum Critical Phenomena

G. Vidal, $^{1}$  J. I. Latorre, $^{2}$  E. Rico, $^{2}$  and A. Kitaev $^{1}$

$^{1}$ Institute for Quantum Information, California Institute of Technology, Pasadena, California 91125, USA  
 $^{2}$ Departament d'Estructura i Constituents de la Materia, Universitat de Barcelona, 08028, Barcelona, Spain (Received 5 December 2002; published 2 June 2003)

Entanglement, one of the most intriguing features of quantum theory and a main resource in quantum information science, is expected to play a crucial role also in the study of quantum phase transitions, where it is responsible for the appearance of long-range correlations. We investigate, through a microscopic calculation, the scaling properties of entanglement in spin chain systems, both near and at a quantum critical point. Our results establish a precise connection between concepts of quantum information, condensed matter physics, and quantum field theory, by showing that the behavior of critical entanglement in spin systems is analogous to that of entropy in conformal field theories. We explore some of the implications of this connection.

DOI: 10.1103/PhysRevLett.90.227902

PACS numbers: 03.67.Mn, 03.65.Ud, 05.50.+q, 05.70.Jk

Entanglement, or the exhibition of nonclassical correlations between separate systems, has since long stood up among the trademarks of quantum mechanics for its nonlocal connotations [1]. Recently, its study has also become a main goal of quantum information science [2], where it is regarded as a resource for processing information in novel ways. For instance, an entangled state  $|\Psi_{\mathrm{AB}}\rangle$  of systems  $A$  and  $B$  can be used to teleport or send quantum information [3]. Similarly, entanglement is useful for quantum cryptography and quantum computation [4,5]. From this resource-oriented perspective, the entropy of entanglement [6]

$$
E \left(\Psi_ {A B}\right) = - \operatorname {t r} \left(\rho_ {A} \log_ {2} \rho_ {A}\right), \tag {1}
$$

where  $\rho_{A}$  denotes the state of system  $A$ , measures the entanglement contained in  $|\Psi_{\mathrm{AB}}\rangle$

On the other hand, entanglement is appointed to play a central role in the study of strongly correlated quantum systems [7-9], since a highly entangled ground state is at the heart of a large variety of collective quantum phenomena. Milestone examples are the ground states used to explain superconductivity and the fractional quantum Hall effect, namely, the BCS ansatz [10] and the Laughlin ansatz [11]. Ground-state entanglement is, most promisingly, also a key factor to the understanding of quantum phase transitions, where it is responsible for the appearance of long-range correlations at zero temperature [12]. Consequently, a gain of insight into phenomena including, among others, Mott insulator-superfluid transitions, quantum magnet-paramagnet transitions, and phase transitions in a Fermi liquid [13] is expected by studying the structure of entanglement in the corresponding underlying ground states.

In this Letter we present a computation of the ground-state entanglement in spin chains near and at a quantum critical point. Such a computation determines the scaling laws of entanglement in one-dimensional spin systems, while explicitly uncovering an accurate correspondence

between critical entanglement in condensed matter systems and the entropy of the vacuum in conformal field theories. Furthermore, such a connection can be exploited to unveil a fundamental law for entanglement in spin systems — namely, that quantum correlations do not increase under renormalization group transformations.

More specifically, we shall analyze the entanglement in two spin-1/2 chains, the so-called XXZ and  $XY$  models, with corresponding Hamiltonians

$$
H _ {X X Z} = \sum_ {l = 0} ^ {N - 1} \left(\sigma_ {l} ^ {x} \sigma_ {l + 1} ^ {x} + \sigma_ {l} ^ {y} \sigma_ {l + 1} ^ {y} + \Delta \sigma_ {l} ^ {z} \sigma_ {l + 1} ^ {z} - \lambda \sigma_ {l} ^ {z}\right), \tag {2}
$$

$$
H _ {X Y} = - \sum_ {l = 0} ^ {N - 1} \left(\frac {a}{2} \left[ (1 + \gamma) \sigma_ {l} ^ {x} \sigma_ {l + 1} ^ {x} + (1 - \gamma) \sigma_ {l} ^ {y} \sigma_ {l + 1} ^ {y} \right] + \sigma_ {l} ^ {z}\right). \tag {3}
$$

These models consider a variety of spin-spin interactions between first neighbors as well as the effect of an external magnetic field along the  $z$  direction, and are used to describe a large range of one-dimensional quantum systems [13]. We recall that the  $H_{XXZ}$  Hamiltonian for  $\Delta = 1$  describes spins with antiferromagnetic isotropic Heisenberg interaction, whereas the  $H_{XY}$  Hamiltonian corresponds, for  $\gamma = 1$ , to the quantum Ising chain, and that both Hamiltonians coincide for  $\Delta = \gamma = 0$ , where they become the XX model.

Osterloh et al. [14] and Osborne and Nielsen [12] have recently considered the entanglement in the  $XY$  spin model, Eq. (3), in the neighborhood of a quantum phase transition. Their analysis, focused on single-spin entropies [12] and on two-spin quantum correlations [12,14], suggestively shows that these one- and two-spin entanglement measures display a peak either near or at the critical point.

Here, alternatively, we undertake the study of the entanglement between a block of  $L$  contiguous spins and the rest of the chain, when the spin chain is in its ground state

$\left|\Psi_{\mathrm{g}}\right\rangle$  . Thus, the aim in the following is to compute the entropy of entanglement, Eq. (1), for the state  $\left|\Psi_{\mathrm{g}}\right\rangle$  according to bipartite partitions parametrized by  $L$

$$
S _ {L} \equiv - \operatorname {t r} \left(\rho_ {L} \log_ {2} \rho_ {L}\right), \tag {4}
$$

where  $\rho_{L} \equiv \mathrm{tr}_{\bar{\mathcal{B}}_{L}}|\Psi_{\mathrm{g}}\rangle \langle \Psi_{\mathrm{g}}|$  is the reduced density matrix for  $\mathcal{B}_L$ , a block of  $L$  spins. The motivation behind the present approach is straightforward: by considering the entanglement  $S_{L}$  of a spin block as a function of its size  $L$ , and by characterizing it for large  $L$ , one expects to capture the large-scale behavior of quantum correlations at a critical regime.

We start off with a description of the calculations, to then move to the analysis and discussion of the results, a summary of which is provided by Fig. 1. The XXZ model, Eq. (2), can be analyzed by using the Bethe ansatz [15]. We have numerically determined the ground state  $|\Psi_{\mathrm{g}} \rangle$  of  $H_{XXZ}$  for a chain of up to  $N = 20$  spins, from which  $S_{L}$  can be computed. We recall that in the XXZ model, and due to level crossing, the nonanalyticity of the ground-state energy characterizing a phase transition already occurs for a finite chain. Correspondingly, already for a chain of  $N = 20$  spins it is possible to observe a distinct, characteristic behavior of  $S_{L}$  depending on whether the values  $(\Delta, \lambda)$  in Eq. (2) belong or not to a critical regime.

![](images/bcd3808b707af36eafba659463c0db2cf012c8622a00074865a526715f8de1ba.jpg)  
FIG. 1. Noncritical entanglement is characterized by a saturation of  $S_{L}$  as a function of the block size  $L$ : noncritical Ising chain (empty squares),  $H_{XY}(a = 1.1, \gamma = 1)$ ; noncritical XXZ chain (filled squares),  $H_{XXZ}(\Delta = 2.5, \lambda = 0)$ . Instead, the entanglement of a block with a chain in a critical model displays a logarithmic divergence for large  $L$ :  $S_{L} \sim \log_{2}(L)/6$  (stars) for the critical Ising chain,  $H_{XY}(a = 1, \gamma = 1)$ ;  $S_{L} \sim \log_{2}(L)/3$  (triangles) for the critical XX chain with no magnetic field,  $H_{XY}(a = \infty, \gamma = 0)$ ; in a finite XXX chain of  $N = 20$  spins without magnetic field (diamonds),  $H_{XXZ}(\Delta = 1, \lambda = 0)$ ,  $S_{L}$  combines the critical logarithmic behavior for low  $L$  with a finite-chain saturation effect. We have also added the lines  $[(c + \bar{c})/6][\log_{2}(L) + \pi]$  [cf. Eq. (12)] both for free conformal bosons (critical XX model) and free conformal fermions (critical Ising model) to highlight their remarkable agreement with the numerical diagonalization.

The  $XY$  model, Eq. (3), is an exactly solvable model (see for instance [13]) and this allows us to consider an infinite chain,  $N\rightarrow \infty$ . The calculation of  $S_{L}$ , as sketched next, also uses the fact that the ground state  $|\Psi_{\mathrm{g}}\rangle$  of the chain and the density matrices  $\rho_{L}$  for blocks of spins are Gaussian states that can be completely characterized by means of certain correlation matrix of second moments.

For each site  $l$  of the  $N$ -spin chain, we consider two Majorana operators,  $c_{2l}$  and  $c_{2l+1}$ , defined as

$$
c _ {2 l} \equiv \left(\prod_ {m = 0} ^ {l - 1} \sigma_ {m} ^ {z}\right) \sigma_ {l} ^ {x}; \quad c _ {2 l + 1} \equiv \left(\prod_ {m = 0} ^ {l - 1} \sigma_ {m} ^ {z}\right) \sigma_ {l} ^ {y}. \tag {5}
$$

Operators  $c_{m}$  are Hermitian and obey the anticommutation relations  $\{c_m, c_n\} = 2\delta_{mn}$ . Hamiltonian  $H_{XY}$  can be diagonalized by first rewriting it in terms of these new variables,  $H_{XY}(\{\sigma_l^\alpha\}) \to H_{XY}(\{c_m\})$ , and by then canonically transforming the operators  $c_{m}$ . The expectation value of  $c_{m}$  when the system is in the ground state, i.e.,  $\langle c_m \rangle \equiv \langle \Psi_g | c_m | \Psi_g \rangle$ , vanishes for all  $m$  due to the  $\mathcal{Z}_2$  symmetry  $(\sigma_l^x, \sigma_l^y, \sigma_l^z) \to (-\sigma_l^x, -\sigma_l^y, \sigma_l^z) \forall l$  of the original Hamiltonian  $H_{XY}$ . In turn, the expectation values  $\langle c_m c_n \rangle = \delta_{mn} + i\Gamma_{mn}$  completely characterize  $|\Psi_g\rangle$ , for any other expectation value can be expressed, through Wick's theorem, in terms of  $\langle c_m c_n \rangle$ . Matrix  $\Gamma$  reads [16]

$$
\Gamma = \left[ \begin{array}{c c c c} \Pi_ {0} & \Pi_ {1} & \dots & \Pi_ {N - 1} \\ \Pi_ {- 1} & \Pi_ {0} & & \vdots \\ \vdots & & \ddots & \vdots \\ \Pi_ {1 - N} & \dots & \dots & \Pi_ {0} \end{array} \right], \tag {6}
$$

$$
\Pi_ {l} = \left[ \begin{array}{c c} 0 & g _ {l} \\ - g _ {- l} & 0 \end{array} \right],
$$

with real coefficients  $g_{l}$  given, for an infinite chain  $(N\to \infty)$ , by

$$
g _ {l} = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} d \phi e ^ {- i l \phi} \frac {a \cos \phi - 1 - i a \gamma \sin \phi}{\left| a \cos \phi - 1 - i a \gamma \sin \phi \right|}. \tag {7}
$$

From Eqs. (6) and (7) we can extract the entropy  $S_{L}$  of Eq. (4) as follows. First, from  $\Gamma$ , and by eliminating the rows and columns corresponding to those spins of the chain that do not belong to the block  $\mathcal{B}_L$ , we compute the correlation matrix of the state  $\rho_{L}$ , namely  $\delta_{mn} + i(\Gamma_L)_{mn}$  where

$$
\Gamma_ {L} = \left[ \begin{array}{c c c c} \Pi_ {0} & \Pi_ {1} & \dots & \Pi_ {L - 1} \\ \Pi_ {- 1} & \Pi_ {0} & & \vdots \\ \vdots & & \ddots & \vdots \\ \Pi_ {1 - L} & \dots & \dots & \Pi_ {0} \end{array} \right]. \tag {8}
$$

Now, let  $V \in \mathrm{SO}(2L)$  denote an orthogonal matrix that brings  $\Gamma_L$  into a block-diagonal form [19], that is

$$
\tilde {\Gamma} _ {L} = V \Gamma_ {L} V ^ {T} = \oplus_ {m = 0} ^ {L - 1} \nu_ {m} \left[ \begin{array}{c c} 0 & 1 \\ - 1 & 0 \end{array} \right], \qquad \nu_ {m} \geq 0. \tag {9}
$$

Then the set of  $2L$  Majorana operators  $d_{m}\equiv \sum_{n = 0}^{2L - 1}V_{mn}c_{n}$  have a block-diagonal correlation matrix  $\langle d_m d_n\rangle$  given by  $\delta_{mn} + i(\tilde{\Gamma}_L)_{mn}$ . It follows that the  $L$  fermionic operators  $b_{l}\equiv (d_{2l} + id_{2l + 1}) / 2$ , obeying  $\{b_m,b_n\} = 0$  and  $\{b_m^\dagger b_n\} = \delta_{mn}$ , have expectation values

$$
\langle b _ {m} \rangle = 0, \quad \langle b _ {m} b _ {n} \rangle = 0, \quad \langle b _ {m} ^ {\dagger} b _ {n} \rangle = \delta_ {m n} \frac {1 + v _ {m}}{2}. \tag {10}
$$

That is, Eq. (10) indicates that the above fermionic modes are in a product or uncorrelated state,  $\rho_{L} = \otimes_{m=0}^{L-1}\varrho_{m}$ , where  $\varrho_{m}$  denotes the mixed state of mode  $m$ . Therefore the entropy of  $\rho_{L}$  is simply the sum of the entropy  $H_{2}[(1 + \nu_{m}) / 2]$  of each mode [here  $H_{2}(x) = -x\log_{2}x - (1 - x)\log_{2}(1 - x)$  denotes the binary entropy] and thus reads

$$
S _ {L} = \sum_ {m = 0} ^ {L - 1} H _ {2} \left(\frac {1 + v _ {m}}{2}\right). \tag {11}
$$

Summarizing, for arbitrary values of  $(a,\gamma)$  in  $H_{XY}$  and in the thermodynamic limit corresponding to an infinite chain  $(N\to \infty)$ , one can evaluate Eq. (7) numerically, diagonalize  $\Gamma_L$  in Eq. (8) to obtain  $\nu_{m}$ , and then evaluate  $S_{L}$  using Eq. (11). The computational effort involved grows only polynomially with  $L$  and produces reliable values for blocks with up to several tens of spins.

The general picture emerging from the above computations is that there is a clear distinction between noncritical and critical entanglement, corresponding to two forms of structurally inequivalent ground states.

Noncritical regime. For all those values  $(\Delta, \lambda)$  and  $(a, \gamma)$  for which the spin chains (2) and (3) are noncritical [13], the entropy of entanglement  $S_{L}$  either vanishes for all  $L$  [e.g., when a sufficiently strong magnetic field aligns all spins into a product, unentangled state] or grows monotonically as a function of  $L$  until it reaches a saturation value for a certain block size  $L_{0}$ .

Noncritical ground-state entanglement corresponds, thus, to a weak, semilocal form of entanglement driven by the appearance of a length scale  $L_{0}$ , due, e.g., to a mass gap in the Hamiltonian. For any  $L$ , the reduced density matrix  $\rho_{L}$  is effectively supported on just a small, bounded subspace of the Hilbert space of the  $L$  spins. We call such entanglement semilocal because a good approximation to  $\rho_{L}$  can be obtained by diagonalizing the Hamiltonian corresponding to the block  $\mathcal{B}_L$  and only a few extra neighboring spins, as skillfully exploited in White's density matrix renormalization group (DMRG) techniques [20].

Critical regime. In critical chains, on the contrary, the entropy  $S_{L}$  diverges logarithmically with  $L$ . Critical ground-state entanglement corresponds to a stronger form

of entanglement, one that embraces the system at all length scales simultaneously.

DMRG techniques have reportedly failed to reproduce quantum critical behavior [21] and we may, in view of the divergent character of  $S_{L}$ , be in a position to understand why. Indeed, more generally we encounter that the support or number of relevant eigenvectors of  $\rho_{L}$  unboundedly grows with  $L$ . If, as is the case in DMRG schemes, only a limited number of eigenvectors can be retained, then a local computation of  $\rho_{L}$  for sufficiently large  $L$  is bound to fail from the outset (arguably, even in an approximate sense).

An exciting, far-reaching feature of the above results is that, for critical regimes,  $S_{L}$  fully coincides with entropy computations performed in conformal field theory [22]. There, a geometric or fine-grained entropy analogous to Eq. (4) but for continuous field theories has been considered by several authors, including Srednicki [23], Callan and Wilczek [24], Holzhey, Larsen, and Wilczek [25] and Fiola et al. [26]. As derived in Ref. [25], in a  $1 + 1$  conformal field theory the entropy of a subregion of length  $L$  reads

$$
S _ {L} \approx \frac {c + \bar {c}}{6} \log_ {2} (L) + k, \tag {12}
$$

with a coefficient given by the holomorphic and antiholomorphic central charges  $c$  and  $\bar{c}$  of the theory. In other words, starting from nonrelativistic spin chain models and by performing a microscopic analysis of a relevant quantity in quantum information, we have obtained a scaling law for entanglement that is in full agreement with previous findings in the context of, say, black-hole thermodynamics in  $1 + 1$  dimensions [25,26].

What we encounter, however, is a clear manifestation of universality in critical systems: the results of the scaling limit (e.g., the logarithmic behavior of  $S_{L}$ ) are not sensitive to the precise microscopic model being used (interacting spins with an external magnetic field). Scaling, instead, is dictated only by the universality class to which the original system belongs, through the conformal field theory associated to the phase transition. In the present case, the dependence of  $S_{L}$  is only on the central charges of the relevant theory. Thus, critical Ising and  $XY$  ( $\forall \gamma \neq 0$ ) models correspond to a free fermionic field theory, with central charges  $c_{f} = \bar{c}_{f} = 1/2$ , whereas the critical regimes of the XX and XXZ models are described by a free bosonic field theory,  $c_{b} = \bar{c}_{b} = 1$  (see Fig. 1).

One may regard the above connection—between an entanglement measure from quantum information and the entropy of the vacuum in quantum field theories—as conceptually satisfactory. Its practical relevance, however, will depend on whether one can use this correspondence to exchange results between the two disciplines. We finish by mentioning some contexts where this exchange is possible.

Srednicki [23] has obtained the behavior of entropy in  $2 + 1$  ( $3 + 1$ ) conformal field theories. For a region  $\mathcal{R}$  in 2 (respectively 3) spatial dimensions, the entropy of  $\mathcal{R}$  is proportional to the size  $\sigma(\mathcal{R})$  of its boundary,

$$
S _ {\mathcal {R}} \approx \kappa \sigma (\mathcal {R}). \tag {13}
$$

That is, the entropy per unit of boundary area,  $\kappa = S_{\mathcal{R}} / \sigma (\mathcal{R})$  , is independent of the size of  $\mathcal{R}$  [in sharp contrast with the same quantity in a  $1 + 1$  theory, where the boundary of a region  $\mathcal{R}$  consists of two points and  $S_{\mathcal{R}} / \sigma (\mathcal{R})$  diverges logarithmically with the length  $L$  of  $\mathcal{R}$  , as it follows from Eq. (12)]. We can now import to, say, spin systems. Then we have that Eq. (13) also describes the scaling behavior of critical ground-state entanglement of spin lattices in two and three dimensions.

On the other hand, the coefficient in control of the divergent behavior of  $S_{L}$  at critical points, Eq. (12), is the central charge, which is subject to Zamolodchikov's  $c$  theorem [27-29]. The  $c$  theorem states that the central charges associated to the ultraviolet and infrared end points of renormalization group flows, labeled by  $C_{\mathrm{UV}}$  and  $C_{\mathrm{IR}}$ , obey the inequality  $C_{\mathrm{UV}} > C_{\mathrm{IR}}$  for unitary theories. This powerful result establishes an irreversible arrow as renormalization group transformations are performed. The translation of this idea to the quantum information setting is that entanglement decreases along renormalization group flows. An infrared theory carries less global entanglement than the ultraviolet theory where it flowed from. The  $c$  theorem seems natural as renormalization group transformations integrate out short distance degrees of freedom, accompanied with their quantum correlations. Yet, it is not at all trivial due to, first, the infinite degrees of freedom (needing regularization) existing in a quantum field theory and, second, the rescaling step in the renormalization group transformation, where (possibly entangled) degrees of freedom are introduced.

It is noteworthy, then, that entanglement in spin systems decreases both under local operations and classical communication and along renormalization group trajectories. The former case corresponds to local manipulation of an entangled system while the second is made out of a block-spin transformation followed by a rescaling of the system. Both actions do reduce quantum correlations and become irreversible [27,30].

This work was supported by the Spanish Grants No. GC2001SGR-00065 and No. MCYT FPA2001-3598, by the National Science Foundation of USA under Grant No. EIA-0086038, and by the European Union under Grant No. ISF1999-11053.

[1] A. Einstein, B. Podolsky, and N. Rosen, Phys. Rev. 47, 777 (1935).

[2] For an introductory review, see the Special Issue on Quantum Information [Phys. World 11, 33 (1998)].  
[3] C.H. Bennett, G. Brassard, C. Crépeau, R. Jozsa, A. Peres, and W.K. Wootters, Phys. Rev. Lett. 70, 1895 (1993).  
[4] C.H. Bennett and D.P. DiVincenzo, Nature (London) 404, 247 (2000).  
[5] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Communication (Cambridge University Press, Cambridge, 2000).  
[6] C. H. Bennett, H. J. Bernstein, S. Popescu, and B. Schumacher, Phys. Rev. A 53, 2046 (1996).  
[7] J. Preskill, J. Mod. Opt. 47, 127 (2000).  
[8] T. J. Osborne and M. A. Nielsen, Quantum Inf. Process. 1, 45-53 (2002).  
[9] P. Zanardi and X. Wang, J. Phys. A 35, 7947 (2002).  
[10] J. Bardeen, L. N. Cooper, and J. R. Schrieffer, Phys. Rev. 108, 1175 (1957).  
[11] R. B. Laughlin, Phys. Rev. Lett. 50, 1395 (1983).  
[12] T. J. Osborne and M. A. Nielsen, Phys. Rev. A 66, 032110 (2002).  
[13] S. Sachdev, Quantum Phase Transitions (Cambridge University Press, Cambridge, 1999).  
[14] A. Osterloh, L. Amico, G. Falci, and R. Fazio, Nature (London) 416, 608 (2002).  
[15] H. A. Bethe, Z. Phys. 71, 205 (1931).  
[16] Most of these manipulations can be reconstructed from [17]. See [18] for a more detailed analysis. We note that, for the sake of simplicity, we do not discuss finite  $N$  corrections to Eq. (6). In the thermodynamic limit,  $N \to \infty$ , they do not contribute to Eq. (8) for finite  $L$ , and therefore do not affect the computation of  $S_L$ .  
[17] E. Lieb, T. Schultz, and D. Mattis, Ann. Phys. (N.Y.) 16, 407 (1961); E. Barouch and B. M. McCoy, Phys. Rev. A 3, 786 (1971).  
[18] J. I. Latorre, E. Rico, and G. Vidal, quant-ph/0304098.  
[19] R. A. Horn and C. R. Johnson, Matrix Analysis (Cambridge University Press, Cambridge, United Kingdom, 1985), Chap. 4.4, p. 217, Ex. 25.  
[20] S. R. White, Phys. Rev. B 48, 10345 (1993).  
[21] S. Rommer and S. Östlund, in Proceedings of Density Matrix Renormalization, Dresden, 1998 (Springer, Berlin, 1999), pp. 67-89.  
[22] P. Ginsparg, in Fields, Strings and Critical Phenomena, Proceedings of the Les Houches Summer School, Session XLIX, 1988, edited by E. Brezin and J. Zinn Justin, 1989 (hep-th/9108028).  
[23] M. Srednicki, Phys. Rev. Lett. 71, 666 (1993).  
[24] C.G. Callan and F. Wilczek, Phys. Lett. B 333, 55 (1994).  
[25] C. Holzhey, F. Larsen, and F. Wilczek, Nucl. Phys. B424, 443 (1994).  
[26] T. M. Fiola, J. Preskill, A. Strominger, and S. P. Trivedi, Phys. Rev. D 50, 3987 (1994).  
[27] A. B. Zamolodchikov, JETP Lett. 43, 730 (1986).  
[28] A. Cappelli, D. Friedman, and J. I. Latorre, Nucl. Phys. B352, 616 (1991).  
[29] S. Forte and J. I. Latorre, Nucl. Phys. B535, 709 (1998).  
[30] G. Vidal and J. I. Cirac, Phys. Rev. Lett. 86, 5803 (2001).