# One-Way Quantum Computing in the Optical Frequency Comb

Nicolas C. Menicucci, $^{1,2}$  Steven T. Flammia, $^{3}$  and Olivier Pfister $^{4}$

$^{1}$ Department of Physics, Princeton University, Princeton, New Jersey 08544, USA  
 $^{2}$ Department of Physics, University of Queensland, Brisbane, Queensland 4072, Australia

$^{3}$ Perimeter Institute for Theoretical Physics, Waterloo, Ontario, N2L 2Y5 Canada  
 $^{4}$ Department of Physics, University of Virginia, Charlottesville, Virginia 22903, USA (Received 7 May 2008; published 22 September 2008)

One-way quantum computing allows any quantum algorithm to be implemented easily using just measurements. The difficult part is creating the universal resource, a cluster state, on which the measurements are made. We propose a scalable method that uses a single, multimode optical parametric oscillator (OPO). The method is very efficient and generates a continuous-variable cluster state, universal for quantum computation, with quantum information encoded in the quadratures of the optical frequency comb of the OPO.

DOI: 10.1103/PhysRevLett.101.130501

PACS numbers: 03.67.Lx, 03.67.Pp, 42.50.Dv, 42.65.Yj

Introduction.-Quantum computing (QC) is a fascinating endeavor, ripe with promises of exponential speedup of particular mathematical problems such as quantum system simulation [1] and integer factoring [2]. Because implementing QC requires exquisite control of each single quantum memory unit (e.g., qubit) in a large-size register, practical QC is therefore faced with the daunting challenges of overcoming decoherence and achieving scalability [3]. Recently, the invention of one-way quantum computing introduced a new paradigm for quantum information processing [4] based on teleportation alone [5]. In the traditional "circuit" QC model [6], physical quantum systems carry quantum information and undergo controlled unitary evolution; in the one-way QC model, quantum information exists virtually in a cluster state [7] and is manipulated through a sequence of local measurements. The choice of measurement basis and the measurement results fully determine the quantum algorithm.

The appeal of one-way QC is that it consolidates most of the challenging work into creating the universal resource—the cluster state—and that it only requires local measurements. In addition, some one-way QC schemes admit very high fault-tolerance thresholds [8], and experimental realizations with four qubits have already been achieved [9,10]. Efficient methods of creating large-scale cluster states are still needed, however, for practical implementation to be realistic. Here, we describe a new approach to scalability: a "top-down" method to produce large continuous-variable (CV) cluster states using a compact experimental setup. The interest of CVs is their natural implementation by squeezing (quantum noise reduction) in quantum optical systems. Photons are also less prone to decoherence than, say, atoms, due to their lower propensity to interact with the environment. Several studies have established the use of photonic CVs for teleportation [11,12], QC [13], quantum error correction [14], cluster states [15-18], and one-way QC [16].

CV cluster states from a single OPO.—Initial proposals for constructing CV cluster states [15,16] involved inline squeezers (seeded OPOs) [19], which are difficult to implement. A more viable method relies on the Bloch-Messiah decomposition [20] and uses  $N$  vacuum squeezers followed by an  $\mathcal{O}(N^2)$ -port interferometer [21]. Our method improves further, requiring only a single OPO and no interferometer [17], and provides huge scaling potential.

The OPO combines two essential elements. The first one is an optical cavity (e.g., two facing mirrors) whose spectrum of resonant frequencies forms an optical frequency comb (OFC), so called because of the equal spacing between modes. Considered as a quantum system, the OFC is a large collection of independent quantum harmonic oscillator modes, or "quumodes" (a term used in analogy with "qubit"). Quantum information is encoded in the quadrature field variables of the OFC, analogs of position and momentum for a mechanical oscillator. The OFC can comprise millions of modes and has outstanding classical coherence properties that have found groundbreaking applications in the revolutionary and now ubiquitous use of mode- and carrier-envelope-phase-locked femtosecond lasers in time or frequency metrology [22,23].

The second crucial element of the OPO is the nondissipative nonlinear medium placed in the cavity. In a basic OPO, this medium is pumped by a monochromatic field and promotes down-conversion, i.e., the simultaneous absorption of a pump photon at frequency  $\omega_{p}$  and emission of a photon pair at OFC frequencies  $\omega_{m}$  and  $\omega_{n}$  such that  $\omega_{p} = \omega_{m} + \omega_{n}$ , as well as up-conversion, the reverse process. Such interactions yield bipartite CV entanglement of the OFC qumodes at frequencies  $\omega_{m}$  and  $\omega_{n}$  [24]. In the OPO we propose to use, the nonlinear medium is specifically engineered to quasiphasematch [25,26] several such interactions simultaneously [27]. This, along with a polychromatic pump, allows one to "write" an entangled network onto the OFC using pairwise couplings. We show in

this Letter that this network can be made to precisely constitute a large CV cluster state, universal for one-way QC, and whose scaling requires no increase in pump complexity (number of frequencies) and only linear increases in pump intensity and nonlinear gain bandwidth.

A CV cluster state [15,16] is defined as any member of a family of squeezed states indexed by an overall squeezing parameter  $r > 0$  for which the variance of each component of  $(\mathbf{p} - A\mathbf{q})$  tends to 0 as  $r \to \infty$  [21]. Here,  $\mathbf{q} = (q_1, \dots, q_N)^T$  and  $\mathbf{p} = (p_1, \dots, p_N)^T$  are vectors of amplitude and phase quadrature operators, respectively, and  $A$  is the (weighted, undirected) adjacency matrix of the cluster state's  $N$ -node graph [17]. The infinite-squeezing limit is not achievable by any finite-energy state, an important point we address later.

We consider an OPO that implements the following Hamiltonian, in the interaction picture and assuming a classical undepleted pump [17,28]:

$$
\mathcal {H} (A) = i \hbar \kappa \sum_ {m, n} A _ {m n} \left(a _ {m} ^ {\dagger} a _ {n} ^ {\dagger} - a _ {m} a _ {n}\right), \tag {1}
$$

where  $\kappa > 0$  is an overall nonlinear coupling strength (squeezing parameter per unit time). The nodes of the graph described by  $A$  correspond to OPO qumodes and any  $(m, n)$  edge is weighted by  $A_{mn}$ , whose magnitude is the qumode coupling strength in units of  $\kappa$  and whose sign indicates down-conversion if positive and up-conversion if negative. In previous work [17], we showed that  $\mathcal{H}(A)$  always generates a CV cluster state whose graph is generally not given by  $A$ . If  $A$  is an orthogonal matrix, though, the graph is given by  $A$  — a fact we previously used to construct an  $\mathcal{H}(A)$  that generates large sets of very small  $(2 \times 2$  or  $2 \times 3)$  CV cluster states [29]. Being disconnected, these cluster states are not universal for QC, but requiring orthogonality is a useful simplification. Here, we construct an orthogonal  $A$  for which  $\mathcal{H}(A)$  generates a QC-universal CV cluster state.

Labeling rows and columns of  $A$  by sequential OFC modes,  $\mathcal{H}(A)$  is easy to implement experimentally when  $A$  is a Hankel matrix (i.e., has constant skew diagonals). Any pump frequency  $\omega_{p}$  satisfying  $\omega_{p} = \omega_{m} + \omega_{n}$ , together with the assumption of a constant interaction strength, generates a constant skew diagonal in  $A$  and sets all its entries to the same value, fixed by the pump power. Additional pump frequencies generate additional skew diagonals, resulting in  $A$  having Hankel form. This connection, along with a useful shorthand for Hankel matrices, is illustrated in Fig. 1 and in Ref. [30].

$QC$ -universal  $CV$  cluster state. We desire a CV cluster state that is universal for one-way QC [16], whose graph is bicolorable [17], and whose adjacency matrix is orthogonal and Hankel for experimental simplicity [29]. Orthogonality of the adjacency matrix  $(AA^T = 1)$  for an undirected graph  $(A = A^T)$  yields  $A^2 = 1$ , or

$$
\left(A ^ {2}\right) _ {j k} = \sum_ {l} A _ {j l} A _ {l k} = \delta_ {j k}. \tag {2}
$$

![](images/7b9d78a5435d07df6514a8b0aa6fc30144f42c04af8108691871bfe5cfc93359.jpg)  
FIG. 1 (color). Hankel shorthand and pump specification. A Hankel matrix is uniquely specified by the entries along the top and down the right side. We collect these entries into a shorthand vector, representing the entire matrix itself, with the top-right entry set off with slashes. When  $A$  is Hankel, its shorthand vector immediately specifies the pump spectrum required to implement  $\mathcal{H}(A)$ . Each nonzero entry in the shorthand vector denotes the amplitude of a frequency in the pump, each of which generates CV entanglement between pairs of qumodes in the OFC symmetric about half that frequency. This accounts for all couplings prescribed by  $A$ .

Equation (2) has a geometric interpretation:  $(A^n)_{jk}$  represents the sum of the weights of all  $n$ -length paths from node  $j$  to node  $k$ , where the weight of such an "  $n$ -path" equals the product of all edge weights along the path. Equation (2) requires that all 2-paths that begin and end on the same node have weights that sum to 1, while those that link different nodes have weights that cancel out.

The usual candidate for a QC-universal graph is the square lattice [4]. This graph is irregular at the boundaries, so Eq. (2) cannot be satisfied for any real-valued weighting of it. Applying toroidal boundary conditions will make it regular, but orthogonality is still prohibited because there exist pairs of distinct nodes connected by only one 2 path, for which the sum in Eq. (2) collapses to one nonzero term.

While real-valued weights cannot satisfy Eq. (2) for a toroidal square lattice, matrix-valued weights can. In such a case, Eq. (2) becomes  $\sum_{l}A_{jl}A_{lk} = \delta_{jk}1$ , where the "entries"  $A_{jl}$  are themselves  $m\times m$  matrices. This means  $A$  is now an adjacency matrix on an  $(mN)$ -node graph. On the other hand, treating the  $m\times m$  blocks as single entries,  $A$  is the matrix-weighted adjacency matrix for what we call a supergraph, which has macronodes consisting of  $m$  individual nodes each. Figure 2 illustrates the meaning of matrix-weighted edges between macronodes for the simple case of a ring supergraph, where  $m = 2$ .

We henceforth promote the toroidal square lattice to a supergraph, illustrated in Fig. 3. The lattice has degree four, so we choose our matrix-valued weights to be four mutually orthogonal rank-one projectors onto  $\mathbb{R}^4$ :

$$
\begin{array}{l l} \Pi^ {0} = \pi^ {+} \otimes \pi^ {+}, & \quad \Pi^ {1} = \pi^ {+} \otimes \pi^ {-}, \\ - 2 & - 3 \end{array} \tag {3}
$$

$$
\Pi^ {2} = \pi^ {-} \otimes \pi^ {+}, \qquad \Pi^ {3} = \pi^ {-} \otimes \pi^ {-},
$$

where

![](images/bd3eee6b4c76519d015c714947c670d35fc9d10dc29c75c8c086d4e84e4bc8ae.jpg)  
FIG. 2 (color). Matrix-valued weights and supergraphs. Matrix-valued weights connect the macronodes of a "ring" supergraph (left). The entries in  $\pi^{\pm}$  (see text) specify the real-valued weights in the actual "crown" graph (right) that connects the underlying physical nodes. Measuring  $q$  for each of the physical nodes in the top layer of the crown leaves the bottom layer in a uniformly weighted ring-graph CV cluster state.

$$
\pi^ {\pm} = \frac {1}{2} \left( \begin{array}{c c} 1 & \pm 1 \\ \pm 1 & 1 \end{array} \right).
$$

Note that the toroidal embedding in Fig. 3 involves a twist of one unit in both dimensions, a subtlety of little physical consequence but which allows for a Hankel  $A$  at the supergraph level (using the Hankel shorthand defined in Fig. 1):

$$
A = \left[ \mathbf {0} ^ {u}, \Pi^ {1}, \mathbf {0} ^ {v}, \Pi^ {0}, \mathbf {0} ^ {u}, \Pi^ {3}, 0 / \Pi^ {2} / \mathbf {0} ^ {u}, \Pi^ {1}, \mathbf {0} ^ {v}, \Pi^ {0}, \mathbf {0} ^ {u}, - \Pi^ {3}, 0 \right], \tag {4}
$$

where  $\mathbf{0}^k$  is a list of  $k$  zero matrices, the size of which is governed by context ( $4 \times 4$  in this case), there are  $M^2$  macronodes (with  $M$  even),  $u = M - 1$ , and  $\nu = M^2 - 2M - 3$ . Orthogonality  $(AA^T = 1)$  is easily verified.

![](images/3fc1f788f9fa09666627d444964f04a8b88721e5715062caba9ca379b11d027c.jpg)  
FIG. 3 (color). Toroidal lattice supergraph and underlying graph structure. Each macronode in the supergraph (left) consists of four physical nodes, and each color corresponds to one of the four matrix-valued weights  $\Pi^j$  from Eq. (3). Entries in  $\Pi^j$  specify the real-valued weights connecting the underlying physical nodes (right). Measuring  $q$  on each physical node in three of the four "layers" leaves the remaining layer in a uniformly weighted QC-universal toroidal lattice cluster state.

The  $M$ -indexed family of these cluster states is universal for CV one-way QC. To see this, first measure  $q$  on three physical nodes per macronode to reduce the supergraph to a uniformly-weighted graph with the same structure (see Fig. 3). Then cut open the toroidal lattice by measuring  $q$  along two orthogonal meridians to form an ordinary lattice, known to be universal [16].

The matrix  $A$ , while Hankel at the supergraph level, is block-Hankel (with  $4 \times 4$  blocks) at physical node level. A suitable renumbering of nodes will reduce the blocks to  $2 \times 2$  while maintaining the block-Hankel structure:

$$
A \cong [ \mathbf {0} ^ {s}, \pi^ {-}, \mathbf {0} ^ {t}, \pi^ {+}, \mathbf {0} ^ {s}, \pi^ {+}, 0, \pi^ {-}, \mathbf {0} ^ {s}, \pi^ {-}, \mathbf {0} ^ {t}, \pi^ {+}, \mathbf {0} ^ {s}, \pi^ {-}, 0 / \pi^ {+} / \mathbf {0} ^ {s}, \pi^ {-}, \mathbf {0} ^ {t}, \pi^ {+}, \mathbf {0} ^ {s}, \pi^ {+}, 0, \pi^ {-}, \mathbf {0} ^ {s}, \pi^ {-}, \mathbf {0} ^ {t}, \pi^ {+}, \mathbf {0} ^ {s}, \pi^ {\prime} ^ {-}, 0 ], \tag {5}
$$

where  $s = 2M - 1$ ,  $t = M^2 - 4M - 3$ , and  $\cong$  indicates equality up to node renumbering [to which the negative sign on  $\Pi^3$  in Eq. (4) is crucial]. These cluster states are QC-universal, bicolorable, and orthogonal—but still only block-Hankel. This is nevertheless sufficient for simple experimental implementation.

Experimental implementation.-In Eq. (5), each  $\pi^{\pm}$  block corresponds to a single pump frequency. Such couplings can be implemented using the two orthogonal polarizations of an optical field at a given frequency, as was experimentally demonstrated by simultaneously quasiphasematching polarization-sensitive interactions ZZZ, ZYY, and YZY/YYZ (first letter is pump polarization) in a periodically poled  $\mathrm{KTiOPO_4}$  (KTP) crystal [27]. The difference between  $\pi^{-}$  and  $\pi^{+}$  is thus a  $180^{\circ}$  phase-shift in the  $Y$ -polarized pump mode. A narrowband pump polarized at  $\pm 45^{\circ}$  in the (ZY) plane implements a  $\pi^{\pm}$  skew-diagonal band in  $A$ . Equation (5) therefore translates into a single OPO pumped by exactly 15 frequencies. Interactions with OFC modes outside the desired subset must also be strictly suppressed, which can be done by cavity

mirror design and/or by quasiphasematching design [26]. While the pump spectrum is relatively complex, requiring 15 frequencies, that number is constant with respect to the lattice size, making this construction extremely scalable.

Note that, in principle, additional physical parameters like wave vector direction or transverse mode structure could be used to directly implement block-Hankel  $A$ 's with larger blocks (e.g.,  $4 \times 4$ ). This would reduce pump complexity but require a more sophisticated OPO.

Finally, we provide realistic estimates for the scaling potential of the CV cluster state with  $N$  macronodes ( $N = M^2$ ) and constant overall coupling strength  $\kappa$ . The pump spectrum complexity and the OFC are independent of  $N$ . Only two quantities scale linearly with  $N$ : the overall pump power and the bandwidth of the nonlinear coupling. The number of pump photons must increase with the number of entangled qumode pairs (number of graph edges), which grows linearly with  $N$  in a square lattice. Two-mode CV entanglement can be obtained at a few milliwatts pump power, with the upper limit being the optical damage limit, which in KTP is at least several watts (focused,

continuous-wave), thus yielding 3 orders of magnitude of scaling range. The bandwidth of the nonlinear coupling (100 GHz to 1 THz) must encompass the whole desired set of qumodes, separated by the cavity's free spectral range (100 MHz for a 1.5-meter-long cavity), which yields 3 or 4 orders of magnitude. These figures reflect ordinary—rather than state-of-the-art—performance and do not account for other interesting avenues such as implementing nonlinear couplings in slow light media. These estimates show our approach has a realistic potential for significant scaling.

Finite squeezing and CV fault tolerance.-The finite-squeezing approximation is a special case of more general considerations of error correction and fault-tolerance for one-way QC using CV cluster states. Certainly, more squeezing is preferable to less, but the amount required for any particular QC task remains an open question, and it's unclear how the nonlinear coupling strength  $\kappa$  in Eq. (1) will need to scale with  $N$  for any particular QC application. Our results are nonetheless compelling because as  $N$  increases, the new interactions generated have the same squeezing strength as existing ones-- i.e., existing squeezing is not "redistributed" to the new pairings as the lattice and pump power grow. Moreover, scalability does enable quantum encoding redundancy. While finite-squeezing errors can be mitigated in medium-sized proof-of-principle experiments with CV cluster states [16], and some work also addresses CV error correction in general [14,31], the task of rigorously establishing a fault-tolerance threshold for CV one-way QC is an important open problem. We hope to spur further investigations along these lines.

Conclusion.-We have presented a theoretical result that opens the door to large-scale experimental generation of a universal one-way quantum computing resource, using existing technology. The entangled states produced by this method will also be objects of interest in the study of entanglement at mesoscopic scales.

This method of entangling—in one fell swoop—a large optical frequency comb into a continuous-variable cluster state is the first "top-down" approach proposed for one-way quantum computation using optical encodings of information in either discrete or continuous variables. While open questions remain about the effects of finite squeezing on scalability for particular quantum computing tasks, the unprecedented scalability of this method encourages further theoretical research. Experimental implementation is already underway.

We thank Carl Caves and Tom Gallagher for comments on the manuscript. O. P. was supported by National Science Foundation Grants No. PHY-0555522 and No. CCF-0622100. N. C. M. was supported by the National Science Foundation. O. P. and N. C. M. were supported in part by the Perimeter Institute for Theoretical Physics, which they thank for hospitality during stimulating visits. S. T. F. was supported by the Perimeter Institute for Theoretical Physics. Research at Perimeter is supported by the Government of Canada through Industry Canada and by

the Province of Ontario through the Ministry of Research & Innovation.

[1] R. P. Feynman, Int. J. Theor. Phys. 21, 467 (1982).  
[2] P.W. Shor, Proceedings, 35th Annual Symposium on Foundations of Computer Science, edited by S. Goldwasser (IEEE Press, Los Alamitos, CA, 1994).  
[3] Scalable Quantum Computers. Paving the Way to realization, edited by S. Braunstein and H. Lo (Wiley, New York, 2001).  
[4] R. Raussendorf and H. J. Briegel, Phys. Rev. Lett. 86, 5188 (2001).  
[5] D. Gottesman and I. L. Chuang, Nature (London) 402, 390 (1999).  
[6] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, U.K., 2000).  
[7] H. J. Briegel and R. Raussendorf, Phys. Rev. Lett. 86, 910 (2001).  
[8] C.M. Dawson, H.L. Haselgrove, and M.A. Nielsen, Phys. Rev. Lett. 96, 020501 (2006).  
[9] P. Walther et al., Nature (London) 434, 169 (2005).  
[10] M. Tame et al., Phys. Rev. Lett. 98, 140501 (2007).  
[11] A. Furusawa et al., Science 282, 706 (1998).  
[12] H. Yonezawa, T. Aoki, and A. Furusawa, Nature (London) 431, 430 (2004).  
[13] S. Lloyd and S. L. Braunstein, Phys. Rev. Lett. 82, 1784 (1999).  
[14] S.L. Braunstein, Nature (London) 394, 47 (1998).  
[15] J. Zhang and S.L. Braunstein, Phys. Rev. A 73, 032318 (2006).  
[16] N.C. Menicucci et al., Phys. Rev. Lett. 97, 110501 (2006).  
[17] N.C. Menicucci, S.T. Flammia, H. Zaidi, and O. Pfister, Phys. Rev. A 76, 010302(R) (2007).  
[18] X. Su et al., Phys. Rev. Lett. 98, 070502 (2007).  
[19] B. Yurke, J. Opt. Soc. Am. B 2, 732 (1985).  
[20] S.L. Braunstein, Phys. Rev. A 71, 055801 (2005).  
[21] P. van Loock, C. Weedbrook, and M. Gu, Phys. Rev. A 76, 032321 (2007).  
[22] J.L. Hall, Rev. Mod. Phys. 78, 1279 (2006).  
[23] T. W. Hänsch, Rev. Mod. Phys. 78, 1297 (2006).  
[24] S.L. Braunstein and P. van Loock, Rev. Mod. Phys. 77, 513 (2005).  
[25] J. A. Armstrong, N. Bloembergen, J. Ducuing, and P. S. Pershan, Phys. Rev. 127, 1918 (1962).  
[26] M.M. Fejer, G.A. Magel, D.H. Jundt, and R.L. Byer, IEEE J. Quantum Electron. 28, 2631 (1992).  
[27] R.C. Pooser and O. Pfister, Opt. Lett. 30, 2635 (2005).  
[28] O. Pfister, S. Feng, G. Jennings, R. Pooser, and D. Xie, Phys. Rev. A 70, 020302 (2004).  
[29] H. Zaidi et al., Laser Phys. 18, 659 (2008).  
[30] See EPAPS Document No. E-PRLTAO-101-039839 for an animation that illustrates the correspondence between the mathematical adjacency matrix and the physical entangling interactions in the optical frequency comb. For more information on EPAPS, see http://www.aip.org/pubservs/epaps.html.  
[31] D. Gottesman, A. Kitaev, and J. Preskill, Phys. Rev. A 64, 012310 (2001).