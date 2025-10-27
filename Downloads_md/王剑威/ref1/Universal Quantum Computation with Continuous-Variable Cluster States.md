# Universal Quantum Computation with Continuous-Variable Cluster States

Nicolas C. Menicucci, $^{1,2,*}$  Peter van Loock, $^{3}$  Mile Gu, $^{1}$  Christian Weedbrook, $^{1}$  Timothy C. Ralph, $^{1}$  and Michael A. Nielsen $^{1}$

$^{1}$ Department of Physics, The University of Queensland, Brisbane, Queensland 4072, Australia

$^{2}$ Department of Physics, Princeton University, Princeton, New Jersey 08544, USA

$^{3}$ National Institute of Informatics, 2-1-2 Hitotsubashi, Chiyoda-ku, Tokyo 101-8430, Japan

(Received 30 May 2006; published 13 September 2006)

We describe a generalization of the cluster-state model of quantum computation to continuous-variable systems, along with a proposal for an optical implementation using squeezed-light sources, linear optics, and homodyne detection. For universal quantum computation, a nonlinear element is required. This can be satisfied by adding to the toolbox any single-mode non-Gaussian measurement, while the initial cluster state itself remains Gaussian. Homodyne detection alone suffices to perform an arbitrary multimode Gaussian transformation via the cluster state. We also propose an experiment to demonstrate cluster-based error reduction when implementing Gaussian operations.

DOI: 10.1103/PhysRevLett.97.110501

PACS numbers: 03.67.Lx, 42.50.Dv

Introduction. One-way quantum computation [1] provides the ability to perform universal quantum computation (QC) using only single-qubit projective measurements, given a specially prepared and highly entangled cluster state. This is in contrast to the traditional circuit model, where unitary evolution and coherent control of individual qubits are required [2]. Apart from its conceptual importance, the cluster-state approach can also lead to practical advantages. For example, the resources required for QC using linear optics [3] can be significantly reduced by first creating photonic cluster states via nondeterministic gates [4-6]. Recently, a four-qubit cluster state has been demonstrated optically in the single-photon regime [7].

While qubits are typically used in QC, Lloyd and Braunstein [8] proposed the use of continuous variables for QC and proved that only a finite set of continuous-variable (CV) gates are needed for universal QC. In the CV approach, the continuous degree of freedom may be used directly or lower-dimensional systems may be encoded within the modes, such as in the Gottesman-Kitaev-Preskill (GKP) proposal [9], which encodes one qubit into each mode. This allows, for instance, for the application of standard qubit protocols to CV systems. The optical modes of the electromagnetic field provide an experimental test bed for these ideas [10].

In this Letter, we describe a model of universal QC using CV cluster states. We also propose an optical implementation of our scheme where squeezed-light sources serve as the nodes of the cluster. The main advantage of this approach is that not only can computations with the cluster be performed deterministically, but also the preparation of the cluster state, including connecting the nodes, can be done unconditionally. This is in contrast to the discrete-variable linear-optics schemes [4,6,11], where cluster states are created probabilistically. Therefore, the CV approach appears to be particularly suited for further experimental demonstration of the general principles of cluster-state QC.

In our optical implementation, once the cluster state has been created, single-mode homodyne detection alone will allow for any multimode Gaussian transformation to be performed on the information contained within the cluster. Analogously to the implementation of Clifford gates using qubit clusters, the homodyne detections can be done in any order, a property known as parallelism. For universal QC, in addition, only one single-mode non-Gaussian projective measurement (e.g., photon counting) is required. However, parallelism no longer applies to non-Gaussian measurements, because the choice of subsequent measurement bases will depend on the outcome of earlier measurements. This adaptiveness of the measurement bases is again analogous to the qubit case when computing non-Clifford gates. While CV cluster states have been described previously in [12], it is claimed there that such states are an insufficient resource for universal QC because of their Gaussian character [13]. In fact, they are sufficient as long as we can perform a non-Gaussian measurement. An analogous result holds for qubit cluster states, which can be created entirely using Clifford group operations [14] but are nevertheless universal once a non-Clifford measurement is allowed.

Although CV cluster states can be built deterministically, it will be impossible to create perfect CV cluster states due to the finite degree of squeezing obtainable in the laboratory. This results in distortions to the quantum information as it propagates through the cluster state. We discuss these distortions (along with other errors) and propose an experiment that demonstrates how parallelism and postselection can be used to mitigate these effects when implementing Gaussian operations.

Continuous-variable cluster states. Other authors [15-17] have extended the cluster-state formalism to  $d$ -level systems (quids). Here we generalize these results to CVs. Our use of CVs for QC follows the standard prescription given in [13]. The Pauli  $X$  and  $Z$  operators are generalized to the Weyl-Heisenberg group, which is the group of phase

space displacements. For CVs, this group is a Lie group with generators  $\hat{q}$  and  $\hat{p}$ . These operators satisfy the canonical commutation relation  $[\hat{q},\hat{p}] = i$  (with  $\hbar = 1$ ) and when exponentiated give the finite phase-space translation operators,  $X(s) = e^{-is\hat{p}}$  and  $Z(t) = e^{it\hat{q}}$ , with  $s,t\in \mathbb{R}$ .  $X(s)$  acts on a continuously indexed computational basis state  $|q\rangle_q$ , an eigenstate of  $\hat{q}$ , as  $X(s)|q\rangle_q = |q + s\rangle_q$ . Eigenstates of  $\hat{p}$  transform similarly:  $Z(t)|p\rangle_p = |p + t\rangle_p$ . Transformation between the position and momentum basis is given by the Fourier transform operator  $F = \exp [i(\pi /4)(\hat{q}^2 +\hat{p}^2)]$ , with  $F|s\rangle_q = |s\rangle_p$ . This is the generalization of the Hadamard gate for qubits. The controlled operations CNOT and CPHASE are generalized to controlled- $X$  ( $C_X$ ) and controlled- $Z$  ( $C_Z$ ), respectively. These operators effect a phase-space displacement on the target by an amount determined by the position eigenvalue of the control:  $C_X = \exp (-i\hat{q}\otimes \hat{p})$  and  $C_Z = \exp (i\hat{q}\otimes \hat{q})$ , where the order of the systems is (control  $\otimes$  target).

The essence of the qubit cluster-state model of QC lies in the one-qubit teleportation circuit [18,19]. This circuit gives the ability to teleport operations diagonal in the computational basis onto the state in question after the cluster has been prepared. This allows dynamics to be performed solely through measurement. The CV analog of the one-qubit teleportation circuit is

$$
\begin{array}{l} | \psi \rangle \\ | 0 \rangle_ {p} \end{array} \begin{array}{c} \boxed {D} - \boxed {F ^ {\dagger}} - \boxed {\not \wedge} = s \\ \hline X (s) F D | \psi \rangle . \end{array} \tag {1}
$$

In this diagram,  $|0\rangle_p = (2\pi)^{-1/2} \int dq |q\rangle_q$  is a zero-momentum eigenstate (the generalization of  $|+ \rangle$ ), the controlled operation indicated is a  $C_Z$  gate, and  $D$  is any operator diagonal in the computational basis (i.e., of the form  $\exp[if(\hat{q})]$ ). The projective measurement is of  $\hat{q}$  and yields a real number  $s$ , which becomes the argument of the displacement  $X(\dots)$  at the output of the circuit. The essential feature of this circuit is that the  $C_Z$  gate commutes with any diagonal operator  $D$ . This means that even though  $D$  is applied after the  $C_Z$  gate, it acts as if it had been applied before. Since the operations  $D$  and  $F^\dagger$  followed by computational basis measurement are equivalent to a single measurement of  $D^\dagger \hat{p}D$ , manipulating quantum information in the CV cluster is possible through projective measurements alone. Concatenation of these circuits makes it possible to implement any single-mode unitary [8].

As is the case for qubits [20], every CV cluster state has a graph state representation, where each node in the graph is a separate CV mode, and each link in the graph represents a  $C_Z$  that has been performed between the corresponding nodes (systems). Linear graphs, where each node has at most two links, can be used for single-mode evolutions, but not multimode gates. The simplest implementation of a  $C_Z$  gate involves a graph state with a link between two adjacent quantum wires:

$$
\begin{array}{c} - ① - ③ \\ \Bigg \downarrow \\ - ② - ④ \end{array} \tag {2}
$$

The lines to the left of nodes 1 and 2 indicate that a bipartite state  $|\psi \rangle$  will be teleported down two quantum wires to arrive at nodes 1 and 2. Measuring  $\hat{p}$  on nodes 1 and 2 leaves  $[X(s_{1})F \otimes X(s_{2})F]C_{Z}|\psi \rangle$  on nodes 3 and 4.

A small set of Hamiltonians that are polynomials in  $\hat{q}$  (e.g.,  $\{\hat{q},\hat{q}^2 /2\}$ ), along with the Fourier transform, are sufficient to implement any single-mode Gaussian [8]. Furthermore, adding the ability to perform a  $C_Z$  operation (as described above) allows implementation of all multimode Gaussians. While this is not sufficient for universal QC, given an encoding that maps all qubit Clifford operations to CV Gaussian operations (the GKP encoding being one example [9]), this would be sufficient for many quantum error correction protocols [21]. Adding to the toolbox any single non-Gaussian projective measurement allows for universal QC using CV cluster states [8].

Optical implementation.-Since each mode of the electromagnetic field behaves as an independent harmonic oscillator, we can use these modes as CV systems for our CV cluster state. To do this, we choose the computational basis to be the "position" (amplitude) quadrature of quantum optics for each mode. The "momentum" (phase) quadrature for each mode becomes the conjugate basis. The commutation relations  $[a, a^{\dagger}] = 1$  and  $[\hat{q}, \hat{p}] = i$  are satisfied by the definitions  $\hat{q} = (a + a^{\dagger}) / \sqrt{2}$  and  $\hat{p} = -i(a - a^{\dagger}) / \sqrt{2}$  for each mode. In this unitless convention, the variance of the vacuum state (which can be measured experimentally using homodyne detection) is given by  $\langle \hat{q}^2 \rangle = \langle \hat{p}^2 \rangle = 1/2$ .

Construction of an ideal CV cluster state requires zero-momentum eigenstates, which cannot be normalized and are thus unphysical. In this optical model, they represent infinitely squeezed vacuum states, which require infinite energy. We can approximate them, though, by finitely squeezed vacuum states:

$$
\left| 0, \Omega \right\rangle_ {p} := (\pi \Omega^ {2}) ^ {- 1 / 4} \int d p e ^ {- p ^ {2} / 2 \Omega^ {2}} | p \rangle_ {p}, \tag {3}
$$

with  $\Omega^2 < 1$  being the variance of a Gaussian wave packet in momentum space (with  $\langle \hat{p}^2\rangle = \Omega^2 /2$ ). The states  $|0,\Omega \rangle_{q}$  are defined analogously with  $p\rightarrow q$  in Eq. (3). Note that  $|0,\Omega \rangle_{p} = |0,\Omega^{-1}\rangle_{q}$ . The fact that these states are finitely squeezed means that we will not have perfect fidelity while propagating quantum information through our cluster. This will be addressed later. Given the graph state that we wish to create, we need one independently squeezed mode per node, and we need the ability to perform a  $C_Z$  gate between modes in accordance with the graph. This operation is a quantum nondemolition (QND) interaction [22] and can be implemented using two beam splitters and two in-line squeezers [23]. Alternatively, it could be directly realized via a linearized optical-fiber

cross-Kerr interaction [24]. (See also Sec. III of Ref. [12] for further ideas.)

Propagation down a quantum wire  $(D = I)$  is achieved through momentum-quadrature homodyne detection. As discussed previously, multimode Gaussian operations require only that we can apply  $D = e^{is\hat{q}}$  and  $D = e^{it\hat{q}^2 /2}$  for all  $s,t\in \mathbb{R}$ . Applying a gate  $D$  to the encoded state is achieved by measuring the operator  $D^{\dagger}\hat{p} D$ . Thus, the  $Z(s) = e^{is\hat{q}}$  gate is implemented by measuring the operators  $Z(-s)\hat{p} Z(s) = \hat{p} -s$ . This is trivial to implement: simply measure  $\hat{p}$  and subtract  $s$  from the result. The gate denoted  $P(t) = \exp (it\hat{q}^2 /2)$  is implemented by measuring  $P(-t)\hat{p} P(t) = \hat{p} +t\hat{q}$ . Notice, however, that by defining  $\theta = \tan^{-1}(-t)$ , we can rewrite this operator as  $(\hat{p}\cos \theta -\hat{q}\sin \theta) / (\cos \theta)$ , which is simply homodyne detection in a rotated quadrature basis, followed by a rescaling of the measurement results by a factor of  $\cos \theta = (1 + t^2)^{-1 / 2}$ . Thus, once the cluster has been prepared, we are able to perform all multimode Gaussian operations simply through homodyne detection.

Furthermore, analogously to implementing Clifford group operations on qubit cluster states, all multimode Gaussian operations may be implemented on CV clusters with the appropriate measurements made in any order. Performing the measurements in a different order is equivalent to commuting Gaussian operations through the (Gaussian) measurement-dependent corrections, resulting in different corrections, but leaving the measurement bases unchanged. This is known as parallelism in cluster-state QC [25]. Non-Gaussian operations in general cannot be parallelized, since later measurement bases will depend on current measurement results, a property known as adaptiveness.

Universal QC requires the ability to implement at least one non-Gaussian operation [8]. In our case, this will be achieved through a measurement in a non-Gaussian basis. While one can, in principle, use the continuous degree of freedom directly for QC, it will almost certainly be more practical (considering experimental errors) to encode finite dimensional systems in the CV modes, e.g., as in the GKP proposal [9], which encodes one qubit into each oscillator. In this case, the optimal non-Gaussian operation would be tailored to implement a desirable non-Clifford unitary in the qubit space. Photon counting is one possibility and fits nicely into the cluster formalism since it is already a projective measurement. Another option is to measure in a nonlinear polynomial basis, such as that corresponding to the observable  $\hat{p} + u\hat{q}^2$  for any one particular choice of  $u$ . This is equivalent, in the language of Circuit (1), to implementing the gate  $D = e^{iu\hat{q}^3 /3}$ . The GKP proposal discusses both options in more detail. We leave the questions of encoding scheme and non-Gaussian measurement to future work.

Experimental errors.—Possible sources of experimental error include the finite squeezing of the input states, mixed input states (but still Gaussian), and distortions due to the

QND operation used to form the cluster. Since any physical implementation of our protocol will be forced to use finitely squeezed states (because of finite energy requirements), we will consider the effects of finite squeezing in some detail.

Finite squeezing in Eq. (3) modifies the output of the circuit in Circuit (1) to  $\mathcal{M}X(s)FD|\psi\rangle$ , where  $\mathcal{M}$  is a distortion that applies a Gaussian envelope in position space with zero mean and variance  $\Omega^{-2}$ :

$$
\mathcal {M} | \psi \rangle \propto \int d q e ^ {q ^ {2} \Omega^ {2} / 2} | q \rangle_ {q q} \langle q | \psi \rangle . \tag {4}
$$

Notice that this is not a unitary transformation, and the state must be renormalized after this envelope is applied. This is also equivalent to convolution in momentum space by a Gaussian with variance  $\Omega^2$ . Mixed input states can be accommodated in this analysis (in the Wigner representation) simply by allowing the convolution width to be independent of the width of the Gaussian envelope. Thus, the transformation implemented by each measurement, which used to consist solely of  $F$ 's,  $D$ 's, and phase-space displacements, now includes a ubiquitous distortion at each step in the evolution. The severity of this distortion depends inversely on the amount by which the sources are squeezed.

Concatenated circuits of the form (1) apply the transformation  $\cdots \mathcal{M}X(s_2)FD_2\mathcal{M}X(s_1)FD_1|\psi\rangle$  to the input. Alternatively, we can gather the fixed distortions to one end of the operation and transform this into the useful form  $U_0(s_1,\ldots,s_n)\tilde{\mathcal{M}}(s_1,\ldots,s_n)|\psi\rangle$ , where  $U_0$  is the unitary that would be applied in the case of an ideal cluster, and  $\tilde{\mathcal{M}}(s_1,\ldots,s_n)|\psi\rangle$  is a distorted initial state, with the distortion now depending on both the measurement results and the gate to be implemented. The effect is the same for multimode gates: at each measurement step, a fixed distortion  $\mathcal{M}$  is applied to each mode. Specifically, in the case of the  $C_Z$  gate, the resulting output is  $(\mathcal{M}X(s_1)F\otimes \mathcal{M}X(s_2)F)C_Z|\psi\rangle$ . The distortion operations in the multimode case can similarly be gathered to the right while becoming measurement and gate dependent. Errors in the QND operation can be modeled as additive Gaussian noise, which has a similar distorting effect, the strength of which scales as the number of links in the cluster's graph.

Experimental proposal for cluster-based error reduction.-Parallelism, which is a feature particular to cluster-state QC, along with postselection, can be used to reduce the impact of the errors described in the last section when implementing Gaussian operations. We propose an experiment to demonstrate this. For concreteness, consider a linear cluster of five nodes (although any number greater than three will suffice):

$$
- ① - ② - ③ - ④ - ⑤ \tag {5}
$$

(The line to the left of the first node indicates where this cluster might be attached to another one.) Many simple

Gaussian operations may be implemented on this cluster through homodyne detection on the first four nodes. With each such measurement there is the possibility of the resulting distortion severely affecting the quantum state in a measurement-dependent way (see the previous section). However, if we choose to delay applying the QND operation that connects node 1 to node 2, we can isolate nodes 2-5 into a "mini-cluster," which is separate from the quantum state to be acted upon. By measuring nodes 3 and 4 before attaching the mini-cluster to the input state, we can calculate the effect of the distortion from these two nodes before that distortion ever affects the state. If this distortion does not preserve the Wigner phase-space region likely to be occupied by the input state (which depends on the chosen encoding), we discard this mini-cluster and try again. If it does, we perform the QND operation to attach nodes 1 and 2. We now have only two "dangerous" measurements to make (on the newly attached nodes) instead of four, with the output appearing on node 5. State tomography can be used to compare the fidelity of these two approaches.

This technique generalizes easily to multiqubit operations and can, in fact, be applied to mini-clusters implementing any Gaussian operation. The greatest benefit will be for Gaussians that require many measurements. While we have "bent the rules" of cluster-state QC a bit by delaying attachment of the mini-cluster and by postselecting mini-clusters based on measurement results, this may yet prove to be a practical procedure for dealing with experimental errors. This result has the flavor of Ref. [26], wherein it is shown that through postselection the reliability of an error-correcting ancilla cluster (called a "telecorrector") can be guaranteed before it is attached to the state to be corrected. Finally, we note that this protocol will most likely require a non-Gaussian encoding although an in-principle demonstration could be made with Gaussian inputs.

Conclusion. We have generalized the notion of universal cluster-state quantum computation to continuous-variable systems. We have proposed an optical implementation that uses squeezed-light sources and quantum nondemolition operations to build a Gaussian cluster state. Homodyne detection alone suffices to implement all multimode Gaussian operations using the cluster state, with the addition of one non-Gaussian measurement allowing for universal quantum computation. Many of the properties of qubit cluster computation also apply to the continuous-variable case, including parallelism and adaptiveness. Within the continuous-variable approach, a lower-dimensional encoding scheme will most likely be required for experimental viability. Because of their Gaussian nature and deterministic method of construction, we expect that continuous-variable cluster states will allow for further experimental demonstrations of the principles of cluster-state quantum computation. We have proposed such an

experiment to demonstrate improvement in the fidelity of Gaussian operations using postselection and parallelism.

We thank Gerard Milburn for help with the details of the optical implementation, as well as Mark de Burgh, Mark Dowling, Henry Haselgrove, and Kae Nemoto for useful discussions. We also thank the Australian Research Council for their support of this work. N.C.M. was supported by the U.S. Department of Defense, and P.v.L. acknowledges funding from MIC in Japan.

*Electronic address: nmen@princeton.edu  
[1] R. Raussendorf and H. J. Briegel, Phys. Rev. Lett. 86, 5188 (2001).  
[2] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, UK, 2000).  
[3] E. Knill, R. Laflamme, and G.J. Milburn, Nature (London) 409, 46 (2001).  
[4] M. A. Nielsen, Phys. Rev. Lett. 93, 040503 (2004).  
[5] L.-M. Duan and R. Raussendorf, Phys. Rev. Lett. 95, 080503 (2005).  
[6] D. E. Browne and T. Rudolph, Phys. Rev. Lett. 95, 010501 (2005).  
[7] P. Walther, K. J. Resch, T. Rudolph, E. Schenck, H. Weinfurter, V. Vedral, M. Aspelmeyer, and A. Zeilinger, Nature (London) 434, 169 (2005).  
[8] S. Lloyd and S.L. Braunstein, Phys. Rev. Lett. 82, 1784 (1999).  
[9] D. Gottesman, A. Kitaev, and J. Preskill, Phys. Rev. A 64, 012310 (2001).  
[10] S.L. Braunstein and P. van Loock, Rev. Mod. Phys. 77, 513 (2005).  
[11] P. Kok, W.J. Munro, K. Nemoto, T.C. Ralph, J.P. Dowling, and G.J. Milburn, quant-ph/0512071.  
[12] J. Zhang and S. L. Braunstein, Phys. Rev. A 73, 032318 (2006).  
[13] S.D. Bartlett, B.C. Sanders, S.L. Braunstein, and K. Nemoto, Phys. Rev. Lett. 88, 097904 (2002).  
[14] D. Gottesman, quant-ph/9807006.  
[15] D. L. Zhou, B. Zeng, Z. Xu, and C. P. Sun, Phys. Rev. A 68, 062303 (2003).  
[16] S. Clark, J. Phys. A 39, 2701 (2006).  
[17] W. Hall, quant-ph/0512130.  
[18] X. Zhou, D. W. Leung, and I. L. Chuang, Phys. Rev. A 62, 052316 (2000).  
[19] M. A. Nielsen, Rep. Math. Phys. 57, 147 (2006).  
[20] M. Hein, J. Eisert, and H.J. Briegel, Phys. Rev. A 69, 062311 (2004).  
[21] D. Gottesman, quant-ph/9705052.  
[22] D.F. Walls and G.J. Milburn, Quantum Optics (Springer, Berlin, 1994).  
[23] S.L. Braunstein, Phys. Rev. A 71, 055801 (2005).  
[24] F. König, B. Buchler, T. Rechtenwald, G. Leuchs, and A. Sizmann, Phys. Rev. A 66, 043810 (2002).  
[25] R. Raussendorf, D.E. Browne, and H.J. Briegel, J. Mod. Opt. 49, 1299 (2002).  
[26] C. M. Dawson, H. L. Haselgrove, and M. A. Nielsen, Phys. Rev. Lett. 96, 020501 (2006).