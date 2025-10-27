# Anomalous Edge States and the Bulk-Edge Correspondence for Periodically Driven Two-Dimensional Systems

Mark S. Rudner, $^{1,2,3}$  Netanel H. Lindner, $^{3,4}$  Erez Berg, $^{2,5}$  and Michael Levin $^{6}$

<sup>1</sup>The Niels Bohr International Academy, Niels Bohr Institute, Blegdamsvej 17, DK-2100 Copenhagen, Denmark

$^{2}$ Department of Physics, Harvard University, Cambridge, Massachusetts 02138, USA

$^{3}$ Institute of Quantum Information and Matter, California Institute of Technology, Pasadena, California 91125, USA

$^{4}$ Department of Physics, California Institute of Technology, Pasadena, California 91125, USA

$^{5}$ Department of Condensed Matter Physics, Weizmann Institute of Science, Rehovot 76100, Israel

6Condensed Matter Theory Center, Department of Physics, University of Maryland, College Park, Maryland 20742, USA

(Received 14 January 2013; published 23 July 2013)

Recently, several authors have investigated topological phenomena in periodically driven systems of noninteracting particles. These phenomena are identified through analogies between the Floquet spectra of driven systems and the band structures of static Hamiltonians. Intriguingly, these works have revealed phenomena that cannot be characterized by analogy to the topological classification framework for static systems. In particular, in driven systems in two dimensions (2D), robust chiral edge states can appear even though the Chern numbers of all the bulk Floquet bands are zero. Here, we elucidate the crucial distinctions between static and driven 2D systems, and construct a new topological invariant that yields the correct edge-state structure in the driven case. We provide formulations in both the time and frequency domains, which afford additional insight into the origins of the "anomalous" spectra that arise in driven systems. Possibilities for realizing these phenomena in solid-state and cold-atomic systems are discussed.

DOI: 10.1103/PhysRevX.3.031005

Subject Areas: Atomic and Molecular Physics, Condensed Matter Physics, Topological Insulators

# I. INTRODUCTION

The discovery of the quantized Hall effect [1] revealed the existence of a powerful new class of extremely robust quantum phenomena that can be observed with high fidelity, largely independent of sample size, shape, and composition, up to macroscopic (millimeter) scales. The robust nature of these phenomena can be linked to the presence of energy gaps for bulk excitations, combined with the existence of nontrivial topological structures associated with the systems' ground-state wave functions [2]. Recently, these ideas were used to predict the existence of new classes of materials [3,4], the topological insulators, which were found experimentally [5,6] shortly thereafter.

Meanwhile, a wide variety of new experimental tools has been developed for actively controlling and probing the behavior of electronic, cold-atomic, and purely photonic systems. For cold atoms, various methods have been proposed for creating "synthetic gauge fields," which mimic the effects of magnetic fields [7-9] or spin-orbit coupling [10,11] for neutral atoms. Several groups have also suggested the possibility of using microwave and optical techniques in solids to realize topologically nontrivial effective band structures in "trivial" materials [12-19]. Topological phenomena have been identified for strongly

driven [20-28] or dissipative quantum systems [29,30], as well. Analogues of topological phenomena in driven systems have even recently been observed in photonic experiments [31,32]. These advances motivate the detailed study of topological phenomena in periodically driven systems.

Here, we focus our attention on topological features of the single-particle properties of two-dimensional (2D) translationally invariant tight-binding systems. In the static case, where the Hamiltonian is constant in time, the topological properties of these systems are well understood. When no additional symmetries are present, a complete topological characterization is provided by the set of values of an integer topological invariant, the Chern number, evaluated for each band [2,33,34].

One of the most striking applications of this topological characterization is to the edge physics of these systems. In a geometry with an edge, a two-dimensional system may support chiral edge modes that propagate at energies within a bulk band gap. Remarkably, the values of the Chern numbers can be used to predict the net number of chiral edge modes traversing each bulk gap (counted according to their chirality). This edge-state count is significant because it is a robust property that is independent of the fine details of the system and of the edge. In the case of the quantized Hall effect, the guaranteed existence of these modes provides a powerful framework for explaining a variety of complex phenomena [35].

Given the power of this approach, we seek to generalize these results to periodically driven systems. In the driven case, the analogue of the energy spectrum is the Floquet

spectrum—the set of eigenvalues of the time evolution operator, evaluated over one complete cycle of driving. The eigenvalues of the unitary evolution operator are unit modulus complex numbers, which are defined on a circle. We express them in terms of a “quasienergy”  $\varepsilon$  as  $e^{-i\varepsilon T}$ , where  $T$  is the driving period. The spectrum is thus  $2\pi / T$  periodic in  $\varepsilon$ .

There are many close analogies between static and periodically driven systems. In particular, the Floquet spectrum can be organized into quasienergy bands with associated Chern numbers, just as in the static case. Also, driven systems may exhibit chiral edge modes when defined in a finite geometry with a boundary. Despite these similarities, however, the Chern numbers employed in the static case do not give a full characterization of the topological properties of periodically driven systems. In particular, for driven systems, these invariants do not uniquely determine the number of chiral edge modes within each bulk band gap.

Recently, new types of edge modes, which cannot be accounted for using the invariants developed for static systems, were discovered in the Floquet spectra of one- and two-dimensional periodically driven systems [22,23,31]. A schematic picture showing an example of such "anomalous" edge modes in a two-band two-dimensional system is shown in Fig. 1. Here, two sets of copropagating chiral edge modes are found, despite the fact that the Chern numbers associated with both bands are zero. This situation cannot occur in static systems, where such edge modes are only produced at the boundaries of systems characterized by nonzero Chern numbers.

In this paper, we develop a more complete understanding of this behavior and identify appropriate topological

![](images/213b04a4aaab6516f2e971bab08bed0a5a1ae263769a539875831cc13c79fb16.jpg)  
FIG. 1. Topologically protected Floquet edge modes in a two-band system with trivial Chern indices  $\mathcal{C} = 0$ . This situation is made possible due to the periodicity of the quasienergy  $\varepsilon$ : In addition to the edge modes that cross the gap near  $\varepsilon = 0$ , a second branch of edge modes crosses through  $\varepsilon = \pi / T$ , thus connecting the top of the upper Floquet band to the bottom of the lower Floquet band and closing the quasienergy cycle. The Chern numbers correctly yield the differences between the numbers of chiral modes above and below every band but cannot be used to uniquely determine the edge-state spectrum of a periodically driven system.

invariants (winding numbers) for characterizing these new phenomena. In contrast to the Floquet band Chern numbers, which only depend on the evolution operator evaluated over one complete driving cycle, the winding numbers utilize the information in the evolution operator for all times within a single driving period. We show that the winding numbers fully determine the chiral edge-mode counts in each of the Floquet gaps. Thus, our construction provides a complete "bulk-edge correspondence" for periodically driven, two-dimensional, single-particle systems.

The paper is organized as follows. Section II gives a general discussion of the bulk-edge correspondence for both static and periodically driven systems. In Sec. III, we introduce a simple model of a strongly driven system, similar to the one considered in Ref. [22], which supports a Floquet band structure like the one depicted in Fig. 1. Then, in Sec. IV, we provide a general analysis and construct the winding numbers of the time-dependent evolution operator, which fully characterize the topological features of the system. The relationship between the winding numbers and the Chern numbers of the Floquet bands is discussed in Sec. IV C. In Sec. V, we give a complementary approach for deriving the edge-state spectrum, which utilizes an analysis in the frequency domain. We demonstrate this approach for the case of weak, harmonic driving, as considered in Refs. [12,13,15-17]. Finally, in Sec. VI, we discuss possible experimental realizations of these new topological spectra and prospects for future investigation. Technical aspects of the derivations are provided in the Appendixes.

# II. BULK-EDGE CORRESPONDENCE IN STATIC AND DRIVEN SYSTEMS

One of the main goals of this paper is to explain how the standard correspondence between the edge-state spectrum and the values of bulk topological invariants is modified for periodically driven systems. Specifically, our goal is to identify topological invariants for bulk systems (i.e., for systems without edges) that give the numbers of protected modes that appear in geometries with edges. Toward this aim, we begin this section with a brief review of Floquet band theory in order to define what we mean by the "band structure" of a periodically driven system. We then compare and contrast the static and driven cases, and give a concrete example that demonstrates the situation where intuition from the static case breaks down.

In general, the evolution of a system governed by a time-dependent Hamiltonian  $H(t)$  may be quite complicated. However, in the case where the Hamiltonian depends periodically on time,  $H(t + T) = H(t)$  for some driving period  $T$ , Floquet theory provides a powerful framework for analysis. In analogy with the usual expansion in terms of stationary eigenstates of a static Hamiltonian, here the evolution is conveniently described in terms of a basis of Floquet states. These states are solutions to the time-dependent Schrödinger equation of the form

$|\psi(t)\rangle = |\Phi(t)\rangle e^{-i\varepsilon t}$ , where  $|\Phi(t + T)\rangle = |\Phi(t)\rangle$ . Under the action of the evolution operator  $U(T)$  over one complete period of driving, each Floquet state is mapped onto itself up to a phase:  $|\psi(T)\rangle = U(T)|\psi(0)\rangle = e^{-i\varepsilon T}|\psi(0)\rangle$ . In a stroboscopic sense, the Floquet states play the role of stationary states for  $U(T)$ . The parameter  $\varepsilon$  called the quasienergy, is uniquely defined up to integer multiples of  $\omega = 2\pi/T$ : Any given solution with quasienergy  $\varepsilon$  can also be associated with a quasienergy  $\tilde{\varepsilon} = \varepsilon + p\omega$ , where  $p$  is an integer, through the relation  $|\tilde{\Phi}(t)\rangle = e^{ip\omega t}|\Phi(t)\rangle$ . Similar to the crystal momentum of a system with discrete translational symmetry, the quasienergy can be thought of as a periodic variable defined on a quasienergy Brillouin zone  $-\pi/T < \varepsilon \leq \pi/T$ . When a system has both discrete time and spatial translation symmetries, the Floquet states are labeled by  $\varepsilon$  and the crystal momentum  $\mathbf{k}$ . The Floquet spectrum then consists of a set of bands  $\{\varepsilon_n(\mathbf{k})\}$ , where  $n$  is a band index.

We now explore the ways in which the topological properties of Floquet bands are similar to, and different from, those of the conventional bands of static systems. Consider first a static (nondriven) two-band system, such as the Haldane model [36], which exhibits a well-defined band gap. A Chern number can be defined for each band  $n$  by integrating the Berry curvature associated with the two-component spinor eigenstates  $\{|u_n(\mathbf{k})\rangle \}$  over the Brillouin zone [2]. If the parameters are such that the Chern numbers of the two bands are nonzero, we will find chiral edge modes traversing the band gap when the system is defined in a geometry with an edge. The existence of these edge modes is "protected," in the sense that the modes cannot be destroyed by any continuous changes of parameters unless the band gap closes.

Mathematically, the Chern number of a band is equal to the difference between the numbers of chiral edge modes entering the band from below and exiting above. Because the spectrum of a static system is bounded, there can never be any chiral edge modes extending beyond the bottom of the lowest band or above the top of the uppermost band. Therefore, in a static two-band system, the Chern number uniquely defines the net number of chiral edge states crossing the band gap.

Now, consider a periodically driven system. We can define a Chern number for each Floquet band  $n$  in the same way as in the static case: The Chern number is obtained by integrating the Berry curvature associated with the Floquet states  $\{|\psi_{n}(\mathbf{k},t)\rangle \}$ , evaluated at any fixed time  $t$ , over the crystal-momentum Brillouin zone (see Sec. IVC for a precise definition). For concreteness, we typically evaluate the Chern numbers using the Floquet-state wave functions at time  $t = 0$ . However, the Chern number is in fact independent of the time at which the Floquet states are evaluated [12,22].

Like the static case, the Chern number of a Floquet band is equal to the difference between the numbers of chiral

modes above and below a given Floquet band. However, due to the periodicity of quasienergy, the Floquet spectrum is not bounded. In particular, in a two-band system, a chiral edge mode that extends out above the top of the "upper" band can pass through the quasienergy Brillouin-zone edge at  $\varepsilon = \pi /T$  and enter the bottom of the "lower" band from below. Using the rule that the Chern number gives the difference between the numbers of edge states above and below a band, we see that chiral edge states can be found between the two bands of a system with zero Chern numbers, provided that a "winding" edge state also connects them through the quasienergy-zone edge.

To understand how such a situation can arise in a periodically driven system, it is useful to consider the following thought experiment. Suppose we start with a system in which the Floquet bands have vanishing Chern numbers, and in which there are no chiral edge modes in a finite geometry. An explicit model for such a system will be described in Sec. III (see Fig. 2). The band structure of a strip, as a function of the momentum  $k_{\parallel}$  along the strip, may resemble the one shown schematically in Fig. 3(a). Note that, as discussed above, there are two gaps to consider between the two bands: the gap centered at zero quasienergy and the gap centered at  $\varepsilon = \pi / T$ . Now, imagine that we tune some parameters in the Hamiltonian. As parameters are changed, one of these gaps, e.g., the one at  $\varepsilon = \pi / T$ , may close and reopen, in such a way that the Chern numbers of both bands become nonzero. After the reopening of the gap, the quasienergy spectrum will look like the one in Fig. 3(b), with chiral edge modes crossing the  $\varepsilon = \pi / T$  gap. As parameters are varied further, the  $\varepsilon = 0$  gap may close and reopen, bringing the Chern numbers of both bands back to zero. However, the chiral edge modes in the  $\varepsilon = \pi / T$  gap cannot disappear during this process, since the  $\varepsilon = \pi / T$  gap remains open throughout it. Therefore, after reopening the  $\varepsilon = 0$  gap, another chiral edge mode must appear around  $\varepsilon = 0$  [Fig. 3(c)] such that the difference of the number of chiral edge modes below and above each band is zero. Thus, we may obtain the situation where chiral edge modes exist, despite all Chern numbers being zero.

The example above shows that the bulk Floquet operator  $U(T)$  does not carry sufficient information to predict the number of chiral Floquet edge modes. [Note that the edge-state spectrum will of course be exhibited explicitly if  $U(T)$  is evaluated directly for a system with boundaries.] Here, we construct new invariants defined in terms of the full time-dependent bulk evolution operator  $U(t)$ , evaluated for all intermediate times within the driving period. These invariants contain the missing information needed to predict the complete Floquet edge-state spectrum.

# III. MODEL OF ANOMALOUS EDGE STATES

In this section, we illustrate the breakdown of the traditional bulk-edge correspondence for a Floquet system by

analyzing an explicit two-dimensional tight-binding model. This model is chosen for conceptual simplicity; a more realistic model for experimental implementations will be discussed in Sec. V. Consider a tight-binding model on a bipartite square lattice, with hopping amplitudes varied in a spatially homogeneous but time-periodic way, as shown in Fig. 2(a). In addition to the cyclic modulation of hopping amplitudes, a constant sublattice potential  $\delta_{AB} = \varepsilon_A - \varepsilon_B$  that distinguishes between  $A$  and  $B$  sites (filled and empty circles, respectively) may be applied. The system's evolution is generated by the time-dependent Hamiltonian

$$
\begin{array}{l} H (t) = \sum_ {\mathbf {k}} \Bigl ( \begin{array}{c c} c _ {\mathbf {k}, A} ^ {\dagger} & c _ {\mathbf {k}, B} ^ {\dagger} \end{array} \Bigr) H (\mathbf {k}, t) \Biggl ( \begin{array}{c} c _ {\mathbf {k}, A} \\ c _ {\mathbf {k}, B} \end{array} \Biggr), \\ H (\mathbf {k}, t) = - \sum_ {n = 1} ^ {4} J _ {n} (t) \left(e ^ {i \mathbf {b} _ {n} \cdot \mathbf {k}} \sigma^ {+} + e ^ {- i \mathbf {b} _ {n} \cdot \mathbf {k}} \sigma^ {-}\right) + \delta_ {A B} \sigma_ {z}. \tag {1} \\ \end{array}
$$

Here,  $c_{\mathbf{k},\alpha}^{\dagger}$  creates a particle in a Bloch state with crystal momentum  $\mathbf{k}$  on sublattice  $\alpha = \{A,B\}$ , and  $J_{n}$  controls hopping from each  $B$  site to its neighboring  $A$  site along the highlighted bond in step  $n$ , shown in Fig. 2(a). The Pauli matrices  $\sigma_z$  and  $\sigma^{\pm} = (\sigma_x\pm i\sigma_y) / 2$  act in the sublattice space. The vectors  $\{\mathbf{b}_i\}$  are given by  $\mathbf{b}_1 = -\mathbf{b}_3 = (a,0)$  and  $\mathbf{b}_2 = -\mathbf{b}_4 = (0,a)$ .

One driving cycle consists of five segments of duration  $T / 5$  each, where  $T$  is the driving period. During the  $n$ th segment of the cycle, where  $n = 1, \ldots, 4$ , the hopping

![](images/7f23f106c762a24de0068effba01b19ab6a17aa3266a3ce16caba3d09c8e2b5e.jpg)  
FIG. 2. Two-dimensional tight-binding model exhibiting anomalous Floquet edge modes. (a) Driving protocol. Hopping amplitudes are varied in a spatially homogeneous but chiral, time-periodic way. A sublattice potential  $\delta_{AB}$  differentiating the two types of sites in the bipartite lattice (filled and open circles) is applied throughout. During four of the five equal-length phases of the cycle, hopping along one of the four distinct bond types is allowed, with amplitude  $J$  (bold lines). During the fifth phase, all hopping amplitudes are zero, while the sublattice potential remains constant. (b) In the simple case  $JT = 5\pi /2$ ,  $\delta_{AB} = 0$ , particles in the bulk move in closed trajectories encircling plaquettes, and the Floquet operator is the identity. Chiral edge modes propagate along the boundaries. (c) Floquet spectrum for the case described in (b).

![](images/85519958d15d63ffb8ad2ab99feb2a9da3111dc74dd0fb828f2c6beab0360458.jpg)

amplitude  $J_{n}$  is set to a value  $J$ , while the other three hopping amplitudes are set to 0. During step 5, all hopping amplitudes are set to 0, but the sublattice potential is still allowed to act. This "holding period" is needed in order to ensure that the model has a sufficiently rich phase diagram to fully illustrate the topological classification that we will develop below. The driving protocol is inherently chiral, as the cycle can be executed in two inequivalent patterns  $(1 - 2 - 3 - \dots$  or  $5 - 4 - 3 - \dots$ ).

For an infinite system (or a finite system with periodic boundary conditions), translational invariance can be exploited to reduce the problem of finding the Floquet operator for this system to multiplying a small number of Pauli matrices. The simplest case, illustrated in Figs. 2(b) and 2(c), occurs when  $JT / 5 = \pi /2$  and  $\delta_{AB} = 0$ . Here, a particle moves with probability 1 between neighboring sites during each hopping step of the cycle. As shown by the light blue trajectory in Fig. 2(b), over one complete driving cycle, each particle makes a loop around a plaquette and returns to its initial position. Therefore, the bulk Floquet operator for this case is simply the identity. The Floquet spectrum features two degenerate bands collapsed at quasenergy zero. Because the bands are fully collapsed, none of the standard invariants for two-dimensional systems can take nontrivial values.

What happens in a finite system with an edge? Naively, it appears that the Floquet operator  $U(T) = 1$  describes the trivial stroboscopic dynamics of a system with an effective Hamiltonian  $H_{\mathrm{eff}} = 0$ . However, using the strip geometry shown in Fig. 2(b), it is straightforward to check that the system supports chiral propagating edge modes localized on the boundaries. Over each complete driving cycle, a particle moves by one unit cell along the edge. These modes appear in the spectrum as two linearly dispersing branches with group velocities  $d\varepsilon /dk = \pm 1 / T$ ; see Fig. 2(c).

Now, consider the time-reversed cycle  $(5 - 4 - 3 - \dots)$ , which has the opposite chirality. Here, although particles circle around the plaquettes in the anticlockwise direction, the Floquet operator (which is still identity) is the same as that of the original cycle. Thus, the information about the circulation direction, which is contained in the bulk evolution operator for intermediate times within the driving cycle, is absent in the Floquet operator. Physically, this information is of crucial importance, however, as it determines the propagation direction of the edge states when the system is terminated. Thus, it is clear that a full topological characterization of these new phases requires an invariant defined in terms of the evolution operator evaluated throughout the entire driving period.

# IV. CONSTRUCTION OF THE INVARIANT

In this section, we define an integer invariant that can be used to correctly predict the edge-state spectrum for a two-dimensional periodically driven system. We begin by

setting up the problem. Let us consider a periodically driven, tight-binding model defined on a 2D lattice with  $N$  sites per unit cell—i.e., a generalization of Eq. (1). Suppose that the hopping amplitudes are translationally invariant and have finite range. Working in  $\mathbf{k}$  space, the Hamiltonian can be written as

$$
H (t) = \sum_ {\mathbf {k}, \alpha \alpha^ {\prime}} c _ {\mathbf {k}, \alpha} ^ {\dagger} H _ {\alpha \alpha^ {\prime}} (\mathbf {k}, t) c _ {\mathbf {k}, \alpha^ {\prime}}, \tag {2}
$$

where  $\alpha, \alpha' = 1, \ldots, N$  label the sites in each unit cell and  $\mathbf{k}$  lies in the first Brillouin zone. All of the bulk properties of the system are encoded in the  $N \times N$  Hermitian matrix  $H(\mathbf{k}, t)$ . In particular, the bulk time evolution operator can be computed as

$$
U (\mathbf {k}, t) = \mathcal {T} \exp \left(- i \int_ {0} ^ {t} d t ^ {\prime} H (\mathbf {k}, t ^ {\prime})\right), \tag {3}
$$

where  $\mathcal{T}$  denotes time ordering. The bulk Floquet operator corresponds to the special case  $U(\mathbf{k},T)$ .

Let us suppose that the Floquet spectrum has a gap extending over some finite interval  $[\varepsilon - \Delta \varepsilon, \varepsilon + \Delta \varepsilon]$ . Then, if we define the model in a geometry with an edge, any Floquet eigenstates with eigenvalues lying in this interval must be localized near the boundary. These eigenstates correspond to edge modes. In analogy with the time-independent case, we expect that the number of these edge modes—counted with a sign corresponding to their chirality—is completely determined by the bulk time evolution operator  $U$ . Therefore, one should be able to compute the number of chiral edge modes at quasenergy  $\varepsilon$ , given only  $U(\mathbf{k}, t)$ . We will now construct an explicit formula, defined in terms of  $\{U(\mathbf{k}, t), \varepsilon\}$ , that gives exactly this number. [Here,  $\{U(\mathbf{k}, t)\}$  denotes the set of evolution operators for all times within a driving period  $0 \leq t \leq T$ .]

# A. The case of a trivial Floquet operator

Our construction proceeds in two steps. First, we consider the special case where the (bulk) Floquet operator is simply the identity, i.e.,  $U(\mathbf{k}, T) = \mathbf{1}$  for all  $\mathbf{k}$ , as in the example described in Sec. III. We then generalize to arbitrary Floquet operators.

If the Floquet operator is the identity, then the Floquet spectrum is gapped everywhere except at  $\varepsilon = 0$ . Therefore, to each  $\{U(\mathbf{k},t)\}$ , we should be able to unambiguously associate an integer  $n_{\mathrm{edge}}$  that counts the number of edge modes propagating across the gap (i.e., winding around the quasienergy Brillouin zone). Furthermore, this integer must be invariant under smooth deformations of  $U$  that preserve the condition  $U(\mathbf{k},T) = \mathbf{1}$ , since the number of edge modes cannot change under a deformation in which the gap remains open.

Purely mathematical considerations suggest a natural guess: Notice that  $U$  is periodic in  $k_x, k_y$ , and  $t$  [since  $U(0) = U(T) = 1$  by assumption]. Thus,  $U$  defines a map from  $S^1 \times S^1 \times S^1 \to U(N)$ . Such maps are known to be

classified by an integer topological invariant or "winding number" defined by [37]

$$
\begin{array}{l} W [ U ] = \frac {1}{8 \pi^ {2}} \int d t d k _ {x} d k _ {y} \\ \times \operatorname {T r} \left(U ^ {- 1} \partial_ {t} U \left[ U ^ {- 1} \partial_ {k _ {x}} U, U ^ {- 1} \partial_ {k _ {y}} U \right]\right). \tag {4} \\ \end{array}
$$

It is natural to guess that  $n_{\mathrm{edge}}$  is related to  $W[U]$  in some way. In Appendix A, we show that this guess is correct—in fact, the two integers are identical:

$$
n _ {\text {e d g e}} = W [ U ]. \tag {5}
$$

The winding number  $W[U]$ , defined in Eq. (4), differs crucially from the familiar Chern number invariant. The winding number depends on the full time evolution, throughout the driving cycle, through the unitary evolution operator  $U(t)$ . In contrast, the Chern number depends only on projectors onto a band of Floquet states [see Eq. (13) below]. The relationship between the winding numbers and the Chern numbers of the Floquet bands is discussed in more detail in Sec. IV C.

# B. The general case

Next, we consider the general case, where the Floquet operator  $U(\mathbf{k}, T)$  can be arbitrary. We would like to compute the number of edge modes at a quasienergy value  $\varepsilon$  lying within a Floquet gap. One way to perform this computation is to reduce the problem to the previous case. The idea is to construct another time evolution operator  $U_{\varepsilon}$  satisfying several properties. The first property is that  $U_{\varepsilon}$  has a trivial Floquet operator:  $U_{\varepsilon}(\mathbf{k}, T) = \mathbf{1}$  for all  $\mathbf{k}$ . The second property is that there exists a one-parameter family of evolution operators  $\{U_s : s \in [0, 1]\}$  that smoothly interpolates between  $U$  and  $U_{\varepsilon}$ :

$$
U _ {s = 0} (\mathbf {k}, t) = U (\mathbf {k}, t), \quad U _ {s = 1} (\mathbf {k}, t) = U _ {\varepsilon} (\mathbf {k}, t). \tag {6}
$$

Finally, and most importantly, we require that the interpolation  $U_{s}(\mathbf{k},T)$  maintains a gap around some quasienergy value  $\varepsilon_{s}$  that changes smoothly in  $s$  and satisfies  $\varepsilon_{s = 0} = \varepsilon$  and  $\varepsilon_{s = 1} = \pi /T$ .

If we can construct an evolution operator  $U_{\varepsilon}$  with these properties, then we can immediately compute the number of chiral edge modes of  $U$  at quasenergy  $\varepsilon$ :

$$
n _ {\text {e d g e}} (\varepsilon) = W \left[ U _ {\varepsilon} \right]. \tag {7}
$$

The validity of this identification comes from the fact that the gap does not close during the interpolation process (by assumption). Therefore, the number of edge modes of  $U$  at quasienergy  $\varepsilon$  must be the same as the number of edge modes of  $U_{\varepsilon}$  at quasienergy  $\pi / T$ . The latter quantity is then given by  $W[U_{\varepsilon}]$ , using the formula in Eq. (5).

All that remains is to construct an appropriate  $U_{\varepsilon}$  and a corresponding interpolation. There is some arbitrariness here, since  $U_{\varepsilon}$  is far from unique. The result, however, will not depend on our particular choice. We will define  $U_{\varepsilon}$  by

$$
U _ {\varepsilon} (\mathbf {k}, t) = \left\{ \begin{array}{l l} U (\mathbf {k}, 2 t) & \text {i f} 0 \leq t \leq T / 2 \\ V _ {\varepsilon} (\mathbf {k}, 2 T - 2 t) & \text {i f} T / 2 \leq t \leq T, \end{array} \right. \tag {8}
$$

where

$$
V _ {\varepsilon} (\mathbf {k}, t) = e ^ {- i H _ {\mathrm {e f f}} (\mathbf {k}) t}, \quad H _ {\mathrm {e f f}} (\mathbf {k}) = \frac {i}{T} \log U (\mathbf {k}, T). \tag {9}
$$

Here, we choose the branch cut of the logarithm to lie along the direction  $e^{-i\varepsilon T}$ . That is, we choose a branch with

$$
\log e ^ {- i \varepsilon T + i 0 ^ {-}} = - i \cdot \varepsilon T, \tag {10}
$$

$$
\log e ^ {- i \varepsilon T + i 0 ^ {+}} = - i \cdot \varepsilon T - 2 \pi i.
$$

This choice of branch is important and provides the only dependence of  $U_{\varepsilon}$  on  $\varepsilon$ .

Physically,  $V_{\varepsilon}$  can be viewed as a trivial "return map" that is used to connect the Floquet operator  $U(\mathbf{k}, T)$  to the identity. The quantity  $H_{\mathrm{eff}}$  appearing in the exponent plays the role of a static effective Hamiltonian that generates a bulk time evolution that, when examined stroboscopically at integer multiples of the driving period  $T$ , is identical to that of  $U(\mathbf{k}, T)$  [22]. By concatenating the driving cycle with an evolution generated by  $-H_{\mathrm{eff}}$ , the net effect of the combined evolution becomes trivial.

We now check that the above definition of  $U_{\varepsilon}$  satisfies all of our requirements. It is clear that  $U_{\varepsilon}(\mathbf{k}, T) = \mathbf{1}$ ; the crucial question is to find an appropriate interpolation connecting  $U$  and  $U_{\varepsilon}$ . The following interpolation does the job:

$$
U _ {s} (\mathbf {k}, t) = \left\{ \begin{array}{l l} U [ \mathbf {k}, (1 + s) t ] & \text {i f} 0 \leq t \leq T / (1 + s) \\ V _ {\varepsilon} [ \mathbf {k}, 2 T - (1 + s) t ] & \text {i f} T / (1 + s) \leq t \leq T. \end{array} \right.
$$

Indeed, using Eq. (9), it is easy to check that the Floquet gap remains open around  $\varepsilon_{s} \equiv (1 - s)(\varepsilon + \pi / T) - \pi / T$ , using the fact that

$$
U _ {s} (\mathbf {k}, T) = U (\mathbf {k}, T) ^ {1 - s}. \tag {11}
$$

Also, we can see that  $\varepsilon_{s=0} = \varepsilon$  and  $\varepsilon_{s=1} = \pi / T$  (mod  $2\pi / T$ ). Thus, the interpolation  $U_s$  satisfies all of the conditions listed above.

# C. Relation with Chern number

As discussed in Sec. II, the Chern number of a Floquet band  $n$  is defined by integrating the Berry curvature of the Floquet eigenstates  $|\psi_{n}(\mathbf{k},t)\rangle$  over the crystal-momentum Brillouin zone, at a fixed time  $t$ :

$$
\mathcal {C} _ {n} = - \frac {1}{2 \pi} \int d k _ {x} d k _ {y} (\nabla \times \mathcal {A} _ {n}), \tag {12}
$$

where  $\mathcal{A}_n = \langle \psi_n(\mathbf{k},t)|i\nabla |\psi_n(\mathbf{k},t)\rangle$ . Equivalently,  $\mathcal{C}$  can be written as

$$
\mathcal {C} _ {n} = \frac {1}{2 \pi i} \int d k _ {x} d k _ {y} \operatorname {T r} \left(P _ {n} \left[ \partial_ {k _ {x}} P _ {n}, \partial_ {k _ {y}} P _ {n} \right]\right), \tag {13}
$$

where  $P_{n}(\mathbf{k}) = |\psi_{n}(\mathbf{k},t)\rangle \langle \psi_{n}(\mathbf{k},t)|$  is a projector onto the Floquet eigenstate  $|\psi_n(\mathbf{k},t)\rangle$

Not surprisingly, there is a close mathematical relationship between the winding number  $W[U_{\varepsilon}]$  defined above and the Chern numbers  $\{\mathcal{C}_n\}$  of the Floquet bands. This relationship becomes clear when one considers the difference between winding numbers evaluated at two different quasienergies. More specifically, it is possible to show that

$$
W \left[ U _ {\varepsilon^ {\prime}} \right] - W \left[ U _ {\varepsilon} \right] = \mathcal {C} _ {\varepsilon \varepsilon^ {\prime}}, \tag {14}
$$

where  $\mathcal{C}_{\varepsilon \varepsilon'}$  denotes the sum of the Chern numbers of all Floquet bands that lie in between  $\varepsilon$  and  $\varepsilon'$  (see Appendix B for a derivation). This identity is very natural from a physical point of view. Indeed, identifying  $W[U_{\varepsilon}]$  with  $n_{\mathrm{edge}}(\varepsilon)$ , Eq. (14) is simply the statement that the difference between the numbers of edge modes at two quasienergies  $\varepsilon$  and  $\varepsilon'$  is equal to the total Chern number of the intermediate bands.

# D. Phases of the modulated square lattice model

We now briefly illustrate the utility of the winding number by examining the phase diagram of the model introduced in Sec. III. Away from the special point  $\delta_{AB} = 0$ ,  $JT / 5 = \pi /2$ , the Floquet operator  $U(T)$  is not equal to the identity. Thus, the return-map construction described above must be used to compute the winding numbers for the Floquet gaps around quasenergy values 0 and  $\pi$ .

In the general case, the evolution operator  $U(t)$  for  $0 \leq t \leq T$  is straightforward to calculate. The Hamiltonian in Eq. (1) is piecewise constant in time through five equal-length segments of duration  $T / 5$ . Let  $H_{n}$  denote the Hamiltonian within the interval  $(n - 1)T / 5 \leq t \leq nT / 5$ . Then, for  $t < T / 5$ , we have  $U(t) = \exp(-iH_{1}t)$ ; for  $T / 5 \leq t < 2T / 5$ ,  $U(t) = e^{-iH_{2}(t - T / 5)}e^{-iH_{1}T / 5}$ , and so on. Because the Bloch Hamiltonians  $\{H_{n}(\mathbf{k})\}$  are  $2 \times 2$  matrices, their exponentials are easily obtained directly. The evolution operator  $U(\mathbf{k}, t)$  is then given by a handful of  $2 \times 2$  matrix exponentiations and multiplications. The return map  $V_{\varepsilon}(\mathbf{k}, t)$  [Eq. (9)] is defined through the logarithm of  $U(\mathbf{k}, T) = e^{-iH_{5}T / t} \cdots e^{-iH_{1}T / 5}$ . Using these results, the winding number  $W[U_{\varepsilon}]$  [see Eqs. (4) and (7)] can then be calculated explicitly.

Using direct numerical calculations, we solve for Floquet spectra in both periodic and strip geometries [see, e.g., Figs. 3(a)-3(c)] and map out the approximate phase diagram, shown in Fig. 3(d). Example spectra from each of the three phases confirm the correspondence between the winding number, calculated from the bulk evolution operator in the periodic geometry, and the edge-state count in each gap in the strip geometry. Figure 3(c) provides an explicit example of the phenomenon discovered in Ref. [22] and shown in Fig. 1: Chiral edge modes appear for the finite system, despite the fact that the Chern numbers of both bands are zero.

![](images/76268fb8f89ec558ac9c714d35f37bbfb0b559101e3c286db2497abfbd6de47d.jpg)

![](images/60723fee03fa8841519eda50c51b15718479b35f087ea9969f81a864e0b2fef6.jpg)

![](images/25aff9126d08190e15041ad4f0e6b9e319846c8cc5aa3167f944b1a54550d29c.jpg)  
FIG. 3. Phases of the square lattice model in Sec. III. (a)-(c) Example Floquet spectra for each of the three phases, calculated in a strip geometry (unit cell  $2a$ ), with sublattice potential  $\delta_{AB} = 0.5\pi /T$  and hopping amplitudes (a)  $J = 0.5\pi /T$ , (b)  $J = 1.5\pi /T$ , and (c)  $J = 2.5\pi /T$ . The winding numbers  $W_{0}$  and  $W_{\pi}$  correctly yield the numbers of edge states in the two gaps. The asymmetry in  $k_{\parallel}$  is due to the breaking of inversion symmetry by the sublattice potential  $\delta_{AB}$ . (d) Phase diagram indicating the winding numbers  $W_{0}$  and  $W_{\pi}$ , calculated in the gaps at quasienergies 0 and  $\pi /T$ , and Chern number  $\mathcal{C}$  of the upper band. Note the existence of two topologically distinct phases with  $\mathcal{C} = 0$ .

![](images/0e83eecd265c34561ec3d296cbf5c9aebe230a37fcc94054670e722c5efa4384.jpg)

# V. FREQUENCY-DOMAIN FORMULATION

In this section, we discuss an alternative approach for deriving the edge-state spectrum of the Floquet operator and its relation to the Chern numbers of the bulk Floquet bands. This approach is based on an analysis in the frequency domain instead of the time domain. The information obtained from the frequency-domain analysis is equivalent to that obtained from the winding numbers in Sec. IV. Specifically, both methods predict the number of chiral edge modes in each Floquet gap. In practice, the frequency-domain technique provides a simpler computational route for systems in which the driving field is weak and has a narrow power spectrum.

# A. Repeated zone analysis

We start from the Schrödinger equation with Hamiltonian (2) for the Floquet state in band  $n$ , with crystal momentum  $\mathbf{k}$ . Using a basis of states labeled by  $\alpha$ , we write  $|\psi_{n}(\mathbf{k},t)\rangle = \sum_{\alpha = 1}^{N}\psi_{n\alpha}(\mathbf{k},t)c_{\mathbf{k},\alpha}^{\dagger}|0\rangle$ , where  $|0\rangle$  is the vacuum. The amplitudes  $\{\psi_{n\alpha}(\mathbf{k},t)\}$  evolve according to

$$
i \partial_ {t} \psi_ {n \alpha} (\mathbf {k}, t) = \sum_ {\alpha^ {\prime} = 1} ^ {N} H _ {\alpha \alpha^ {\prime}} (\mathbf {k}, t) \psi_ {n \alpha^ {\prime}} (\mathbf {k}, t). \tag {15}
$$

Employing the Floquet theorem, we write

$$
\psi_ {n \alpha} (\mathbf {k}, t) = e ^ {- i \varepsilon_ {n} (\mathbf {k}) t} \sum_ {m = - \infty} ^ {\infty} \varphi_ {n \alpha} ^ {(m)} (\mathbf {k}) e ^ {i m \omega t}, \tag {16}
$$

where  $\omega = 2\pi /T$ . Below, we suppress all  $\mathbf{k}$  indices for notational simplicity. The coefficients  $\varphi_{n\alpha}^{(m)}$  satisfy the (time-independent) eigenvalue equation

$$
\sum_ {\alpha^ {\prime}, m ^ {\prime}} \mathcal {H} _ {\alpha \alpha^ {\prime}} ^ {m m ^ {\prime}} \varphi_ {n \alpha^ {\prime}} ^ {(m ^ {\prime})} = \varepsilon_ {n} \varphi_ {n \alpha} ^ {(m)}, \tag {17}
$$

where the "Floquet Hamiltonian"  $\mathcal{H}_{\alpha \alpha^{\prime}}^{mm^{\prime}}$  is given by

$$
\mathcal {H} _ {\alpha \alpha^ {\prime}} ^ {m m ^ {\prime}} = m \omega \delta_ {\alpha \alpha^ {\prime}} \delta_ {m m ^ {\prime}} + \frac {1}{T} \int_ {0} ^ {T} d t e ^ {- i (m - m ^ {\prime}) \omega t} H _ {\alpha \alpha^ {\prime}} (t). \tag {18}
$$

For each  $\mathbf{k}$ , Eq. (17) has solutions throughout  $-\infty < \varepsilon_{n} < \infty$ . However, as discussed in Sec. II, if  $\varepsilon_{n}$  is an eigenvalue of Eq. (17) corresponding to the eigenstate with amplitudes  $\{\varphi_{n\alpha}^{(m)}\}$ , then  $\tilde{\varepsilon}_{n} = \varepsilon_{n} + p\omega$  (where  $p$  is any integer) is also an eigenvalue corresponding to an eigenstate with amplitudes given by  $\tilde{\varphi}_{n\alpha}^{(m+p)} = \varphi_{n\alpha}^{(m)}$ . In fact, as seen by direct substitution into Eq. (16), all of these solutions correspond to the same time-dependent solution of the Schrödinger equation. Therefore, the Floquet states are uniquely and completely parametrized by quasienergies in the "first quasienergy Brillouin zone"  $-\pi / T \leq \varepsilon_{n} < \pi / T$ . Equation (17) is the temporal analogue of a "repeated zone" scheme for conventional band-structure calculations.

To illustrate the structure of Eqs. (17) and (18), we now consider the case where

$$
H (t) = H _ {0} + \Delta e ^ {i \omega t} + \Delta^ {\dagger} e ^ {- i \omega t}. \tag {19}
$$

In this case, the matrix  $\mathcal{H}_{\alpha \alpha^{\prime}}^{mm^{\prime}}$  has the block tridiagonal form, shown schematically in Fig. 4(a), where each block is an  $N\times N$  matrix. As noted above, it suffices to solve for the Floquet bands within the first quasienergy Brillouin zone  $-\pi /T\leq \varepsilon_{n} < \pi /T.$  In the limit of weak driving (small  $\Delta$  ), this solution can be attained using perturbation theory.

As sketched in Fig. 4(b), the zeroth-order (in  $\Delta$ ) spectrum of the Floquet Hamiltonian (18) consists of an array of copies of the original spectrum of  $H_0$ , shifted up and down by integer multiples of the drive frequency  $\omega$ . In the Floquet picture, the harmonic driving  $(\Delta e^{i\omega t} + \mathrm{H.c.})$  induces hopping between levels with  $m$  values differing by one. Processes where  $m$  increases (decreases) by one correspond to transitions accompanied by the absorption (emission) of a photon from the driving field. When the range  $\Lambda$  of the spectrum of  $H_0$  is greater than  $\omega$ , resonant transitions (associated with degeneracies between levels with neighboring values of  $m$ ) may occur for some values of  $\mathbf{k}$ . To leading order, degenerate perturbation theory shows that the driving  $(\Delta e^{i\omega t} + \mathrm{H.c.})$  opens gaps at these resonances [see Fig. 5(b)].

![](images/06caeab2968797382984c62db0546cd4f50f0e274cc7b80ab63912d35f0020d9.jpg)

![](images/01a12e869f6e7b197f5701390a85a2bcc0d4556b353c021f792bc2a6f5b4a5ba.jpg)  
FIG. 4. Floquet Hamiltonian and level diagram in the repeated zone scheme. (a) When the driving  $\Delta(t)$  consists of a single harmonic with angular frequency  $\omega$ , the Floquet Hamiltonian  $\mathcal{H}(\mathbf{k})$  [see Eq. (18)] assumes a block-tridiagonal form. Each block is an  $N\times N$  matrix, where  $N$  is the number of bands in the unperturbed Hamiltonian  $H_0$ . The off-diagonal blocks labeled by  $\Delta$  and  $\Delta^{\dagger}$  describe transitions accompanied by the absorption and emission of a driving field photon, respectively. (b) Schematic Floquet level diagram. The  $N$ -level spectrum of  $H_0(\mathbf{k})$ , which spans an energy range  $\Lambda$ , is copied and rigidly shifted by  $m\omega$  for each value of  $m$ . The harmonic driving  $\Delta$  induces transitions between neighboring copies with  $m$  values differing by 1. Analogous to Wannier-Stark states, the Floquet eigenstates in the first quasienergy Brillouin zone (gray shaded region) are localized in  $m$ , with amplitudes highly suppressed for  $|m|\gg \Lambda /\omega$ .

# B. Edge-state count via the truncated Floquet Hamiltonian

An important property of Floquet eigenstates is that they are localized in  $m$ , decaying rapidly for  $|m - m_0|\omega \gg \Lambda$  where  $m_0$  is the center of a given localized state. This localization in frequency space is analogous to the well-known localization of Wannier-Stark states in real space. Starting from this observation, we now describe an alternative method for computing edge-state spectra of Floquet systems—complementary to the winding-number approach of Sec. IV.

The first step is to truncate the Floquet Hamiltonian (18) so that  $m$  and  $m'$  run over a large but finite range  $-M \leq m, m' \leq M$ , where  $M$  is much greater than the frequency-space localization range of the Floquet states. Making use of the localization of the Floquet states in  $m$ , we note that the spectrum of the truncated Floquet Hamiltonian will

![](images/a414fcaa1d24c55c1e7f56d8fc694b0606594659841630b57a4f8ce54fb0e2d2.jpg)  
FIG. 5. Floquet bands for a two-band model in the truncated repeated zone scheme. Representative one-dimensional cuts through the two-dimensional crystal-momentum Brillouin zone are shown. (a) For  $\Delta = 0$ , the unperturbed bands of  $H_0$  are each copied and shifted up and down one time;  $m = -1, 0, 1$ . The bands have Chern numbers  $\mathcal{C} = \pm C_0$ . The crossings between bands with  $m$  values differing by 1 correspond to points in the Brillouin zone where the driving field resonantly couples the two bands. (b) For  $\Delta \neq 0$ , a generic driving field opens avoided crossings at the resonance points. After coupling, the Chern numbers of the crossed bands are changed to  $\mathcal{C} = \pm C_F$ . In the truncated scheme, the appearance of Floquet edge states at a particular quasienergy in the first quasienergy Brillouin zone (gray regions) can be predicted by adding up the Chern numbers of all bands below it.

![](images/305a0ee3a61bda744906339038aa7b5936c4980c7550c16c83420902b07ebc62.jpg)

be a good approximation to the exact result within the first few quasienergy zones centered around  $m = 0$ . In particular, if we consider a geometry with a boundary, then the edge-state spectrum of the truncated Hamiltonian will closely match the exact Floquet edge-state spectrum within these central few quasienergy zones.

The key observation is that there is actually a straightforward way to determine the edge-state spectrum using Chern numbers of the bands of the truncated Floquet Hamiltonian. Interpreting the truncated Floquet Hamiltonian as the static Hamiltonian of some new  $(2M + 1)\times N$ -band system, we apply the standard bulk-edge correspondence to deduce that the net number of chiral edge modes (counterclockwise minus clockwise) crossing any particular gap is given by the sum of the Chern numbers of all bands below this gap. In this way, we have a simple procedure for deriving the edge-state spectra of Floquet systems: To find the number of chiral edge modes crossing a given quasienergy gap within the first quasienergy Brillouin zone, i.e., within the interval  $-\pi /T\leq \varepsilon_{n} < \pi /T$  we truncate the Floquet Hamiltonian and then count Chern numbers of the resulting bands below the gap in which we are interested. Note that, as in Sec. IV C, the difference between the numbers of chiral edge modes at quasienergies  $\varepsilon$  and  $\varepsilon^{\prime}$  within the first quasienergy zone is equal to the sum of the Chern numbers of all Floquet bands between  $\varepsilon$  and  $\varepsilon^{\prime}$ .

As an example, we study the case of harmonic driving introduced in Eq. (19). We take  $H_0$  to be a general two-band Hamiltonian

![](images/abd3bf2b36ea0d6c68260117bcfd9e26ff60594860d6df4ec5ba72866f9f67a9.jpg)

![](images/a22a66a6ea167d20889d260139201b9ff957f0d0999c681b2886d14bfd71885a.jpg)

![](images/1a3bddec8b60e983119e034f104bf079f492717575435771c6a598a531916776.jpg)  
FIG. 6. Anomalous edge states in a weakly driven two-band system, with Hamiltonian  $H_0$  given by Eqs. (20) and (21). The Chern numbers of the unperturbed bands are  $C_0 = \pm 1$ . (a) Spectrum of  $H_0$  with periodic boundary conditions, showing the resonance curve (purple line) in the valence and conduction bands. The color scheme indicates  $\langle \sigma_z \rangle$  for the corresponding eigenstates in the two bands. (b) Spectrum of  $H_0$  for a cylindrical geometry, with periodic boundary conditions in the  $x$  direction and open boundary conditions in the  $y$  direction. (c) Spectrum of the truncated Floquet Hamiltonian [Eq. (18)] in the cylindrical geometry. The isolated bands at the top and bottom of the figure do not participate in any resonances and are nearly identical to the original bands of  $H_0$ . The Floquet bands have zero Chern numbers, while edge states traverse both gaps, centered around  $\varepsilon = 0$  and  $\varepsilon = \pi / T$ . The parameters used are  $J / \mu = b / \mu = 1.5$ ,  $a / \mu = 4$ ,  $\Delta_0 / \mu = 1$ , and  $\Delta_0 / \omega = 0.07$ .

$$
H _ {0} (\mathbf {k}) = e (\mathbf {k}) + \mathbf {d} (\mathbf {k}) \cdot \boldsymbol {\sigma}, \tag {20}
$$

where  $\sigma = (\sigma_x, \sigma_y, \sigma_z)$  is the vector of Pauli matrices, and  $\mathbf{d}(\mathbf{k})$  is a three-dimensional vector. The bands are characterized by Chern numbers  $\mathcal{C} = \pm C_0$ , as indicated in Fig. 5(a). For simplicity, we assume that the periodic drive creates a single resonance between the valence and conduction bands of  $H_0$ . This resonance occurs simultaneously for all  $\mathbf{k}$  values that satisfy  $\omega = 2|\mathbf{d}(\mathbf{k})|$ . We further assume that this resonance condition is satisfied along a single closed curve in the crystal-momentum Brillouin zone [see Fig. 6(a)].

Consider the corresponding Floquet Hamiltonian  $\mathcal{H}_{\alpha \alpha^{\prime}}^{mm^{\prime}}$  [see Eq. (18)], which is truncated to the range  $-1\leq m$ $m^{\prime}\leq 1$  . The band structure of the truncated Floquet Hamiltonian is shown schematically in Fig. 5. For  $\Delta = 0$  the valence band of block  $m$  and the conduction band from block  $m - 1$  are degenerate on the resonance curve (appearing as two points on the sections shown in Fig. 5). The driving terms mix the two bands, generically opening gaps

at the crossing points. The resulting bands have Chern numbers  $C_F$  and  $-C_F$ , as indicated in Fig. 5(b). Because of the truncation, however, two isolated bands are left, at the top and bottom of the spectrum. These bands do not participate in any resonances, and their Chern numbers remain equal to  $\pm C_0$ ; see Fig. 5(b).

Examining the gap centered at quasienergy  $-\pi /T$  we see that the Chern numbers of all bands below it sum to  $C_0 + C_F$ . Therefore, we expect to find  $C_0 + C_F$  chiral edge modes spanning this gap. For the same reason, the gaps centered at quasienergy values  $\varepsilon = 0$  and  $\varepsilon = \pi /T$  support  $C_0$  and  $C_0 + C_F$  chiral edge modes, respectively.

The value of  $C_F$  that is obtained in any particular model depends on the details of  $H_0(\mathbf{k})$ ,  $\Delta$ , and  $\omega$ . In particular, in Sec. VC below and in Fig. 6, we describe a specific model that gives  $C_F = 0$ , while nonetheless exhibiting robust chiral edge modes.

Importantly, the method outlined above for determining the number of chiral edge modes in each gap of the Floquet spectrum can be applied to more general periodically driven systems and is not restricted to the weakly driven, single harmonic limit discussed in the above example. It works, provided that one keeps sufficiently many copies of  $H_0$  in the truncation and that the driving power spectrum decays sufficiently rapidly for higher harmonics. If the driving is strong, the relationship between the Floquet bands and the original bands may be more complicated than in the example considered above, but the results of this procedure are still guaranteed to converge for large enough  $M$ .

# C. Anomalous edge states in a weakly driven two-band lattice system

We consider a two-band model with a Hamiltonian of the form (20), with  $e(\mathbf{k}) = 0$  and with the components of  $\mathbf{d}(\mathbf{k})$  given by

$$
d _ {x} (\mathbf {k}) = a \sin \left(k _ {x}\right), \quad d _ {y} (\mathbf {k}) = a \sin \left(k _ {y}\right),
$$

$$
\begin{array}{l} d _ {z} (\mathbf {k}) = (\mu - J) - 2 b [ 2 - \cos (k _ {x}) - \cos (k _ {y}) ] \\ + J \cos \left(k _ {x}\right) \cos \left(k _ {y}\right). \tag {21} \\ \end{array}
$$

In the parameter regime  $\mu, b, J > 0$  and  $\mu / b < 4$ , the unperturbed bands of  $H_0$  have Chern numbers  $C_0 = \pm 1$ , as indicated in Fig. 6(a). This result can easily be obtained by direct integration of the Berry curvature using Eq. (12). More simply, recall that for a general two-band system of the form (20), the Chern number is determined by the degree of the map  $\hat{\mathbf{d}}(\mathbf{k}) = \mathbf{d}(\mathbf{k}) / |\mathbf{d}(\mathbf{k})|$  from the Brillouin zone to the unit (Bloch) sphere  $S^2$ , i.e., by the number of times this map "covers"  $S^2$ . The result  $C_0 = \pm 1$  follows simply by noting that the vector  $\hat{\mathbf{d}}(\mathbf{k})$  maps exactly one point in the Brillouin zone to a point close to the north pole of the unit sphere, as indicated by the colored shading in Fig. 6(a) (see Ref. [38] for more details).

We now add a time-dependent perturbation of the form  $\Delta (t) = \Delta_0\sigma_z\cos (\omega t)$ . The hopping  $J$  and frequency  $\omega$  can be tuned such that only a single resonance occurs in the Brillouin zone, on a closed curve around  $\mathbf{k} = 0$ , as shown in Fig. 6(a). Note that here we take parameters to provide the simplest situation, containing only a single resonance, for the purposes of clearest illustration; similar considerations apply in other parameter regimes, allowing for more resonances.

To see that this driving results in trivial Floquet bands with  $C_F = 0$ , we perform degenerate perturbation theory in the off-diagonal matrix elements of the Floquet Hamiltonian; see Eq. (17). Consider an isolated pair of crossing bands, such as the red and blue bands labeled  $m = -1$  and  $m = 0$  in Fig. 5(a), respectively. To lowest order in  $\Delta_0$ , the corresponding two new hybridized bands are described as the eigenstates of an effective Hamiltonian

$$
H _ {\text {e f f}} ^ {(0)} = \left(\left| \mathbf {d} (\mathbf {k}) \right| - \omega / 2\right) \hat {\mathbf {d}} (\mathbf {k}) \cdot \boldsymbol {\sigma} + \tilde {\Delta} (\mathbf {k}) \cdot \boldsymbol {\sigma}, \tag {22}
$$

where  $\tilde{\Delta} (\mathbf{k}) = \Delta_0[\hat{\mathbf{z}} -\hat{d}_z(\mathbf{k})\hat{\mathbf{d}} (\mathbf{k})]$ . Note that  $H_{\mathrm{eff}}^{(0)}$  is in fact a leading-order approximation to the effective Hamiltonian introduced in Eq. (9). As indicated in Fig. 5(b), the bands of  $H_{\mathrm{eff}}^{(0)}$  are inverted relative to those of  $H_{0}$  in the region around  $\mathbf{k} = 0$ .

How do we see that these bands have trivial Chern indices? Consider the map from the Brillouin zone to  $S^2$  defined by the projector onto the lower-energy band of  $H_{\mathrm{eff}}^{(0)}$  in Eq. (22). Writing this projector as  $\frac{1}{2} [1 - \mathbf{d}_{\mathrm{eff}}(\mathbf{k})]$ , a necessary requirement for obtaining a nonzero Chern number is that every point on the Bloch sphere must be reached by  $\mathbf{d}_{\mathrm{eff}}(\mathbf{k})$  for at least one value of  $\mathbf{k}$  in the Brillouin zone. For small  $\Delta_0$  and for  $\omega$  such that the resonance curve winds around  $\mathbf{k} = 0$ , there is a region surrounding the north pole of  $S^2$  that is not accessed by  $\mathbf{d}_{\mathrm{eff}}(\mathbf{k})$  for any points in the Brillouin zone. Therefore, its bands must have zero Chern numbers.

In Fig. 6(c), we plot the spectrum of the truncated Floquet Hamiltonian for the model described above, defined in a cylindrical geometry. This figure clearly exhibits chiral edge states traversing each of the gaps, including those associated with the isolated bands at the top and bottom of the truncation window. As described above, these bands are not strongly hybridized and are nearly identical to the unperturbed bands of  $H_{0}$  [see Fig. 6(b)].

The analysis above provides an alternative picture for understanding how edge states can appear in periodically driven systems, even when all of the Floquet bands have vanishing Chern numbers. The fact that the bands carry zero Chern numbers only guarantees that the numbers of chiral edge states in the two gaps surrounding each Floquet band are equal. In the truncated Floquet Hamiltonian picture, the edge states owe their existence to bands near the truncation boundaries that carry anomalous (i.e., nonvanishing) Chern numbers. These bands retain the history about the topological properties of the original bands of  $H_0$ , as well as the structure of the resonances that transform

them into the Floquet bands. Note that anomalous edge states can also be obtained in a model when the unperturbed Hamiltonian  $H_0(\mathbf{k})$  contains only trivial bands, provided that additional resonances (e.g., due to multiphoton processes) are allowed.

# VI.DISCUSSION

In this paper, we discussed the correspondence between bulk topological invariants and the edge-state spectra of two-dimensional periodically driven systems. In both static and periodically driven systems, the Chern number of a given band is equal to the difference between the number of chiral edge states above and below the band. Because the spectrum of a static system is bounded from below, knowledge of the Chern numbers of all bands up to a particular energy is sufficient to uniquely determine the number of chiral edge modes at that energy. For driven systems, however, the spectrum is defined on a circle, and hence is not bounded. Knowing the Chern numbers of all Floquet bands is therefore not sufficient to determine the edge-state structure. Our main result in this work is the construction of a new invariant that fully captures the edge-state spectrum for periodically driven systems.

The most striking example of the difference between the static and driven cases occurs when a driven system supports robust chiral edge states, even when the Chern numbers of all of its Floquet bands are zero. Can such systems be realized experimentally? In the analysis above, we introduced two lattice models: one with strongly modulated hopping amplitudes and one with a weak driving field applied on top of a convenient band structure. While the first model was constructed primarily for mathematical demonstration, a class of models similar to the second, involving weak, uniform driving, should be accessible in cold-atomic, solid-state, or all-photonic systems.

A promising route for implementing models of the second type is to utilize Cooper's optical flux-lattice systems [9]. There, weak periodic modulations of the optical fields that create the flux lattice could be used to produce the resonances necessary for obtaining a nontrivial Floquet spectrum. A modulated flux lattice with anomalous edge states could be achieved either by starting with topologically nontrivial unperturbed bands, as in Sec. VC, or even by starting with topologically trivial bands and employing two (or more) photon resonances.

Solid-state implementations are also possible (see, e.g., Refs. [39,40] for some experimental preliminaries). Typically, the frequency  $\omega$  will be at least a few times smaller than the total width  $\Lambda$  of the two central bands of interest (e.g., the conduction and valence bands). In this case, the Floquet band structure is complicated by quasienergy-zone folding, which leads to additional band crossings corresponding to multiphoton resonances. Generically, for  $\omega / \Lambda \ll 1$ , one can find bulk states coming from a sufficiently high-order folding at any quasienergy.

Therefore, strictly speaking, there is no gap in the Floquet spectrum at any quasienergy. If there are chiral edge states in a gap that corresponds to a first-order (single-photon) resonance, they acquire a finite lifetime due to scattering into bulk states with the same quasienergy. However, these scattering processes involve high-order resonances (multiphoton processes). For sufficiently weak driving, the lifetime broadening of the Floquet edge states is parametrically smaller than the size of the gap in which they reside. Therefore, the chiral Floquet edge states are still well-defined excitations.

Throughout this work, we have focused on the topological characteristics of the single-particle spectra of periodically driven two-dimensional systems. Notably, we have not discussed the filling of these states for fermionic (or bosonic) systems. Many-body physics in these systems is a very interesting and challenging problem of its own, which is beyond the scope of this work. However, future studies on the phenomenology of periodically driven multiparticle systems will need to address this issue in detail.

The invariants presented in this paper give a complete topological description of the Floquet band structures of periodically driven, two-dimensional noninteracting systems, if no additional symmetries are imposed. In static systems, the presence of additional symmetries leads to a rich topological characterization of noninteracting systems [33,34]. In the case of periodically driven systems, some robust topological phenomena have been demonstrated to be stabilized by additional symmetries such as an effective time-reversal symmetry [12,15,17]. A full topological classification for driven systems is yet to be developed and is an interesting direction for further study.

# ACKNOWLEDGMENTS

We thank Gil Refael, Daniel Podolsky, and P. Zoller for helpful discussions. This work was supported by NSF Grants No. DMR-090647 and No. PHY-0646094 (M.R.), as well as Grants No. DMR-1103860 and No. DMR-0705472 (E.B.). E.B. also acknowledges support from the ISF under Grant No. 7113640101. M.L. acknowledges support from the Alfred P. Sloan Foundation. N.L. acknowledges support by DARPA under Grant No. N66001-12-1-4034. N.L. and M.R. acknowledge support provided by the Institute for Quantum Information and Matter (IQIM), an NSF Physics Frontiers Center with support of the Gordon and Betty Moore Foundation.

# APPENDIX A: DERIVATION OF THE RELATIONSHIP BETWEEN EDGE MODES AND WINDING NUMBER

In this section, we prove Eq. (5): We show that the number of Floquet edge modes is given by the winding number, i.e.,  $n_{\mathrm{edge}} = W[U]$ , for any system in which the bulk Floquet operator is the identity. Our derivation is inspired by an analogous derivation in Ref. [41].

The precise statement we will prove is as follows. Let  $H$  be a translationally invariant, periodically driven Hamiltonian with a time evolution operator  $U$ . Suppose that  $U$  has a trivial Floquet operator—that is,  $U(\mathbf{k}, T) = \mathbf{1}$ . Now, consider a cylindrical geometry with periodic boundary conditions in the  $y$  direction and open boundary conditions at  $x = 1$  and  $x = L_x$ . (Here,  $x$  and  $y$  are integers labeling lattice sites.) Consider a Hamiltonian  $\tilde{H}$  that is identical to  $H$  in the interior of the cylinder but can take any form near the boundaries as long as it is local and translationally invariant in the  $y$  direction. Let  $\tilde{U}$  be the corresponding time evolution operator. What we will show is that the number of edge modes of  $\tilde{U}(\mathbf{k}, T)$  is given by the winding number  $W[U]$ .

The first step is to find a formal mathematical expression for the number of Floquet edge modes  $n_{\mathrm{edge}}$ . To this end, it is convenient to describe  $\tilde{H}$  and  $\tilde{U}$  in mixed  $x$ ,  $k_y$  space. In this description, we denote the Hamiltonian by  $\tilde{H}_{xx'}(k_y, t)$  and the time evolution operator by  $\tilde{U}_{xx'}(k_y, t)$ . Here, we drop the additional indices  $\alpha$  and  $\alpha'$  corresponding to the sites within the unit cell, so that  $\tilde{H}_{xx'}(k_y, t)$  and  $\tilde{U}_{xx'}(k_y, t)$  are actually  $N \times N$  matrices for each  $x$ ,  $x'$ ,  $k_y$ , and  $t$ .

The time evolution operator  $\tilde{U}_{xx'}(k_y, t)$  satisfies several important properties. The first property is that it is quasidiagonal in  $x$ :  $\tilde{U}_{xx'}(k_y, t) \to 0$  as  $|x - x'| \to \infty$ . To see that  $\tilde{U}$  is quasidiagonal, note that  $\tilde{U}_{xx'}$  can be thought of as a propagator for single-particle states. Furthermore, the velocity of these states is bounded during the course of the time evolution:  $|\nu| \leq c$  for some  $c$ . It then follows that  $\tilde{U}_{xx'}$  vanishes exponentially if  $x$  and  $x'$  are separated by a distance greater than  $c \cdot t$ .

Another important property of  $\tilde{U}$  is that the Floquet operator  $\tilde{U}_{xx'}(k_y,T)$  reduces to the identity matrix  $\delta_{xx'}$  unless  $x$  and  $x'$  are near  $x = 1$  or  $x = L_x$  (i.e., within distance  $c\cdot T$  of one of the boundaries). This property follows from the same reasoning as above: As long as  $x$  and  $x'$  are far from the boundaries, the amplitude to propagate between them must be identical to that in the translationally invariant system [where  $U(T) = \mathbf{1}$ ]. Therefore,

$$
\tilde {U} _ {x x ^ {\prime}} \left(k _ {y}, T\right) = U _ {x x ^ {\prime}} \left(k _ {y}, T\right) = \delta_ {x x ^ {\prime}}, \tag {A1}
$$

unless  $x$  and  $x'$  are near one of the boundaries.

It is illuminating to write out the matrix  $\tilde{U}(k_y, T)$  more explicitly. All together, the matrix  $\tilde{U}(k_y, T)$  has dimension  $NL_x \times NL_x$ , since the lattice index  $x$  runs from 1 to  $L_x$ , and the band index  $\alpha$  runs from 1 to  $N$ . Let us list the rows and columns in order  $x = 1, \ldots, L_x$ , with the band index running from 1 to  $N$  for each value of  $x$ . Then, it follows from the above two properties that  $\tilde{U}(k_y, T)$  (approximately) takes the block diagonal form

$$
\tilde {U} \left(k _ {y}, T\right) = \left( \begin{array}{c c c} \tilde {U} _ {1} \left(k _ {y}\right) & 0 & 0 \\ 0 & \mathbf {1} & 0 \\ 0 & 0 & \tilde {U} _ {3} \left(k _ {y}\right) \end{array} \right), \tag {A2}
$$

where  $\tilde{U}_1(k_y)$  and  $\tilde{U}_3(k_y)$  are unitary matrices describing the action of  $\tilde{U}$  near the two boundaries and  $\mathbf{1}$  describes the action of  $\tilde{U}$  in the interior of the cylinder. To rigorously derive Eq. (A2), imagine we partition the lattice sites  $x$  into three groups: those with  $x \leq L_x / 3$ , those with  $L_x / 3 < x < 2L_x / 3$ , and finally those with  $x \geq 2L_x / 3$ . In the thermodynamic limit,  $\tilde{U}(k_y, T)$  will be block diagonal with respect to these three groups—up to corrections that are exponentially small in  $L_x$ . Furthermore,  $\tilde{U}$  will act like the identity matrix  $\mathbf{1}$  on the middle group of sites  $L_x / 3 < x < 2L_x / 3$ . Thus, we can define the three diagonal blocks  $\{\tilde{U}_1(k_y), \mathbf{1}, \tilde{U}_3(k_y)\}$  to be  $NL_x / 3 \times NL_x / 3$  matrices that describe the action of  $\tilde{U}$  within these three groups of sites.

Using the above matrix representation for  $\tilde{U}$ , we can write down a simple expression for the number of edge modes  $n_{\mathrm{edge}}$  on the  $x = L_x$  edge. In particular, we claim that

$$
n _ {\text {e d g e}} = - \frac {1}{2 \pi i} \int d k _ {y} \operatorname {T r} \left[ \tilde {U} \left(k _ {y}, T\right) ^ {- 1} \partial_ {k _ {y}} \tilde {U} \left(k _ {y}, T\right) Q \right], \tag {A3}
$$

where  $Q$  is an operator defined by

$$
Q _ {x x ^ {\prime}} = g (x) \delta_ {x x ^ {\prime}}, \tag {A4}
$$

and  $g$  is any function satisfying

$$
g (x) = \left\{ \begin{array}{l l} 0 & \text {i f} x \leq L _ {x} / 3 \\ 1 & \text {i f} x \geq 2 L _ {x} / 3. \end{array} \right. \tag {A5}
$$

The trace in Eq. (A3) is taken over the band indices  $\alpha$  and  $\alpha'$  and the site indices  $x$  and  $x'$ .

To understand where (A3) comes from, imagine we replace  $Q$  by the identity operator 1. Then, the above integral reduces to  $-\frac{1}{2\pi i}\int dk_y\mathrm{Tr}(\tilde{U}^{-1}\partial_{k_y}\tilde{U})$ , which counts the total number of chiral modes propagating in the  $y$  direction—both at  $x = L_x$  and  $x = 1$  [22]. Our claim is that, when we include the operator  $Q$  in the expression, we effectively count the edge modes near the  $x = L_x$  boundary and throw out the contribution from the  $x = 1$  boundary.

To see this counting explicitly, let us write out the matrix for  $Q$  using the same notation as Eq. (A2):

$$
Q = \left( \begin{array}{c c c} \mathbf {0} & 0 & 0 \\ 0 & Q _ {2} & 0 \\ 0 & 0 & \mathbf {1} \end{array} \right). \tag {A6}
$$

Here,  $Q_{2}$  describes the action of  $Q$  on the sites with  $L_{x} / 3 < x < 2L_{x} / 3$ , while  $\mathbf{0}$  and  $\mathbf{1}$  describe the action of  $Q$  on the sites with  $x \leq L_{x} / 3$  and  $x \geq 2L_{x} / 3$ , respectively. From the matrix representations for  $Q$  and  $\tilde{U}$ , we can see that the only contribution to  $\mathrm{Tr}(\tilde{U}^{-1}\partial_{k_y}\tilde{U} \cdot Q)$  comes from the sites near the  $x = L_{x}$  boundary:

$$
\operatorname {T r} \left(\tilde {U} ^ {- 1} \partial_ {k _ {y}} \tilde {U} \cdot Q\right) = \operatorname {T r} \left[ \tilde {U} _ {3} ^ {- 1} \left(k _ {y}\right) \partial_ {k _ {y}} \tilde {U} _ {3} \left(k _ {y}\right) \right]. \tag {A7}
$$

Clearly, when we integrate this expression over  $k_{y}$  and take the trace, the result is simply the number of chiral edge

modes localized near the  $x = L_{x}$  boundary, as claimed above.

The next step is to write (A3) as an integral over  $t$ :

$$
n _ {\text {e d g e}} = - \frac {1}{2 \pi i} \int d t d k _ {y} \partial_ {t} \operatorname {T r} \left(\tilde {U} ^ {- 1} \partial_ {k _ {y}} \tilde {U} \cdot Q\right). \tag {A8}
$$

We then add the total derivative  $\partial_{k_y}\mathrm{Tr}(-\tilde{U}^{-1}\partial_t\tilde{U}\cdot Q)$  to the integrand, thereby deriving

$$
n _ {\text {e d g e}} = \frac {1}{2 \pi i} \int d t d k _ {y} \operatorname {T r} \left(\tilde {U} ^ {- 1} \partial_ {k _ {y}} \tilde {U} [ Q, \tilde {U} ^ {- 1} \partial_ {t} \tilde {U} ]\right).
$$

Next, we note that the integrand only receives contributions from the interior of the cylinder, since  $g(x)$  in Eq. (A4) is constant near the boundaries, and hence the commutator  $[Q, \tilde{U}^{-1}\partial_t\tilde{U}]$  vanishes there. In the interior of the cylinder, however,  $\tilde{U}$  is identical to  $U$ . We are therefore free to replace  $\tilde{U} \rightarrow U$ :

$$
n _ {\text {e d g e}} = \frac {1}{2 \pi i} \int d t d k _ {y} \operatorname {T r} \left(U ^ {- 1} \partial_ {k _ {y}} U [ Q, U ^ {- 1} \partial_ {t} U ]\right). \tag {A9}
$$

To proceed further, let  $A \equiv U^{-1} \partial_{k_y} U$  and  $B \equiv U^{-1} \partial_t U$ . Exploiting the translational invariance of  $A$  and  $B$ , we have

$$
\begin{array}{l} \operatorname {T r} (A [ Q, B ]) = \sum_ {x x ^ {\prime}} A _ {x x ^ {\prime}} B _ {x ^ {\prime} x} [ g (x ^ {\prime}) - g (x) ] \\ = \sum_ {x s} A _ {0 s} B _ {s 0} [ g (x + s) - g (x) ]. \\ \end{array}
$$

Next, we use the identity  $\sum_{x} [g(x + s) - g(x)] = s$  to write the above equation as

$$
\operatorname {T r} (A [ Q, B ]) = \sum_ {s} A _ {0 s} B _ {s 0} \cdot s = \frac {i}{2 \pi} \int d k _ {x} A \left(k _ {x}\right) \partial_ {k _ {x}} B \left(k _ {x}\right),
$$

where the last equality comes from taking the Fourier transform. Substituting this expression into (A9), we have

$$
n _ {\text {e d g e}} = \frac {1}{4 \pi^ {2}} \int d t d k _ {x} d k _ {y} \operatorname {T r} \left[ U ^ {- 1} \partial_ {k _ {y}} U \cdot \partial_ {k _ {x}} \left(U ^ {- 1} \partial_ {t} U\right) \right].
$$

The final step is to massage this expression into the desired form (5) by adding a derivative with respect to  $k_x, k_y$ , and  $t$  to the integrand. In particular, we add

$$
\begin{array}{l} - \frac {1}{2} \partial_ {k _ {x}} \operatorname {T r} \left(U ^ {- 1} \partial_ {k _ {y}} U \cdot U ^ {- 1} \partial_ {t} U\right) + \frac {1}{2} \partial_ {k _ {y}} \operatorname {T r} \left(U ^ {- 1} \partial_ {k _ {x}} \partial_ {t} U\right) \\ - \frac {1}{2} \partial_ {t} \operatorname {T r} \left(U ^ {- 1} \partial_ {k _ {x}} \partial_ {k _ {y}} U\right). \\ \end{array}
$$

Adding this term and simplifying gives

$$
\begin{array}{l} n _ {\text {e d g e}} = \frac {1}{8 \pi^ {2}} \int d t d k _ {x} d k _ {y} \operatorname {T r} \left(U ^ {- 1} \partial_ {k _ {x}} U \cdot U ^ {- 1} \partial_ {k _ {y}} U \cdot U ^ {- 1} \partial_ {t} U\right) \\ - \left(k _ {x} \leftrightarrow k _ {y}\right) \\ = W [ U ], \tag {A10} \\ \end{array}
$$

as claimed.

# APPENDIX B: DERIVATION OF EQ. (14)

In this section, we derive relation (14) between the winding number  $W[U_{\varepsilon}]$  and the Chern numbers of the Floquet bands. Let  $U(\mathbf{k}, T)$  be the Floquet operator with gaps at  $\varepsilon$  and  $\varepsilon'$ . We wish to compute the difference in the winding numbers  $W[U_{\varepsilon'}] - W[U_{\varepsilon}]$ . A simple way to compute this difference is to note that  $W[U_{\varepsilon'}] - W[U_{\varepsilon}]$  is equal to the winding number of a map  $U$  that "glues"  $V_{\varepsilon'}$  and  $V_{\varepsilon}$  together with opposite orientations. To be precise,

$$
W \left[ U _ {\varepsilon^ {\prime}} \right] - W \left[ U _ {\varepsilon} \right] = W [ U ], \tag {B1}
$$

where

$$
U (\mathbf {k}, t) = \left\{ \begin{array}{l l} V _ {\varepsilon} (\mathbf {k}, 2 t) & \text {i f} 0 \leq t \leq T / 2 \\ V _ {\varepsilon^ {\prime}} (\mathbf {k}, 2 T - 2 t) & \text {i f} T / 2 \leq t \leq T. \end{array} \right. \tag {B2}
$$

To compute  $W[U]$ , we use the fact that it is invariant under continuous deformations of  $U$ . We note that the above map  $U$  can be continuously deformed into  $\bar{U}$ , where

$$
\bar {U} (\mathbf {k}, t) = V _ {\varepsilon} (\mathbf {k}, t) \cdot V _ {\varepsilon^ {\prime}} / (\mathbf {k}, t) ^ {- 1}. \tag {B3}
$$

For example, the following interpolation does the job:

$$
U _ {s} (\mathbf {k}, t) = \left\{ \begin{array}{l l} V _ {\varepsilon} (\mathbf {k}, 2 t) \cdot V _ {\varepsilon^ {\prime}} (\mathbf {k}, 2 t) ^ {- s} & \text {i f} 0 \leq t \leq T / 2 \\ V _ {\varepsilon^ {\prime}} (\mathbf {k}, 2 T - 2 t) ^ {1 - s} & \text {i f} T / 2 \leq t \leq T, \end{array} \right.
$$

for  $0\leq s\leq 1$

The problem reduces to computing the winding number  $W[\bar{U}]$ . Note that  $V_{\varepsilon}$  and  $V_{\varepsilon'}$  differ only in the position of the branch cut of the logarithm in definition (9), which affects only the quasienergy eigenvalues but not the eigenvectors. These two operators can therefore be simultaneously diagonalized, and commute. From the definition, we see that

$$
\bar {U} (\mathbf {k}, t) = V _ {\varepsilon} (\mathbf {k}, t) \cdot V _ {\varepsilon^ {\prime}} (\mathbf {k}, t) ^ {- 1} = e ^ {(2 \pi i t / T) P _ {\varepsilon \varepsilon^ {\prime}} (\mathbf {k})}, \tag {B4}
$$

where  $P_{\varepsilon \varepsilon'}(\mathbf{k})$  is the projector onto the Floquet eigenstates with crystal momentum  $\mathbf{k}$ , and with eigenvalues between  $\varepsilon$  and  $\varepsilon'$ . Therefore, according to the calculation of Appendix C, the corresponding winding number is  $W[\bar{U}] = \mathcal{C}_{\varepsilon \varepsilon'}$ , where  $\mathcal{C}_{\varepsilon \varepsilon'}$  is the total Chern number of all the Floquet bands with eigenvalues between  $\varepsilon$  and  $\varepsilon'$ . We conclude that

$$
W \left[ U _ {\varepsilon^ {\prime}} \right] - W \left[ U _ {\varepsilon} \right] = W [ \bar {U} ] = \mathcal {C} _ {\varepsilon \varepsilon^ {\prime}}, \tag {B5}
$$

as we set out to show.

# APPENDIX C: WINDING NUMBER FOR TIMEINDEPENDENT, FLAT-BAND HAMILTONIANS

In this section, we compute the value of  $W[U]$  for time-independent, flat-band Hamiltonians of the form

$$
H (\mathbf {k}) = - \frac {2 \pi}{T} P (\mathbf {k}), \tag {C1}
$$

where  $P(\mathbf{k})$  is an  $N \times N$  Hermitian matrix, all of whose eigenvalues are either 0 or 1 (i.e.,  $P$  is a projection operator). Note that the prefactor  $\frac{2\pi}{T}$  guarantees that the corresponding Floquet operator is trivial, i.e.,  $U(T) = e^{-iHT} = \mathbf{1}$ . For concreteness, we assume that  $P(\mathbf{k})$  has  $M$  eigenvalues equal to 1 and  $N - M$  eigenvalues equal to 0, where  $M < N$ . Thus, the Hamiltonian  $H$  has  $M$  bands with energy  $-2\pi / T$  and  $N - M$  bands with energy 0. We will show that  $W[U]$  is given by the total Chern number  $C$  of the bands with energy  $-2\pi / T$ .

First, we note that the time evolution operator  $U = e^{(2\pi it / T)P(\mathbf{k})}$  satisfies the identities

$$
U = \left(e ^ {2 \pi i t / T} - 1\right) P + 1, \tag {C2}
$$

$$
U ^ {- 1} = (e ^ {- 2 \pi i t / T} - 1) P + 1,
$$

from which it follows that

$$
\begin{array}{l} U ^ {- 1} \partial_ {k _ {x}} U = (e ^ {- 2 \pi i t / T} - 1) (e ^ {2 \pi i t / T} - 1) P \partial_ {k _ {x}} P \\ + \left(e ^ {2 \pi i t / T} - 1\right) \partial_ {k _ {x}} P \\ \equiv a \left(\frac {2 \pi t}{T}\right) P \partial_ {k _ {x}} P + b \left(\frac {2 \pi t}{T}\right) \partial_ {k _ {x}} P. \tag {C3} \\ \end{array}
$$

Here,

$$
a (\theta) = 2 - 2 \cos (\theta), \quad b (\theta) = e ^ {i \theta} - 1. \tag {C4}
$$

Similarly, we have

$$
\begin{array}{l} U ^ {- 1} \partial_ {k _ {y}} U = a \left(\frac {2 \pi t}{T}\right) P \partial_ {k _ {y}} P + b \left(\frac {2 \pi t}{T}\right) \partial_ {k _ {y}} P, \\ U ^ {- 1} \partial_ {t} U = \frac {2 \pi i}{T} P. \tag {C5} \\ \end{array}
$$

Combining these results, we find

$$
\begin{array}{l} \operatorname {T r} \left(\left[ U ^ {- 1} \partial_ {t} U \right] \left[ U ^ {- 1} \partial_ {k _ {x}} U \right] \left[ U ^ {- 1} \partial_ {k _ {y}} U \right]\right) \\ = \operatorname {T r} \left(\frac {2 \pi i}{T} P [ a \cdot P \partial_ {k _ {x}} P + b \cdot \partial_ {k _ {x}} P ] \right. \\ \times \left[ a \cdot P \partial_ {k _ {y}} P + b \cdot \partial_ {k _ {y}} P \right]. \\ \end{array}
$$

Next, we make use of the identity

$$
(P \partial_ {i} P) P = [ \partial_ {i} (P ^ {2}) - \partial_ {i} P P ] P = \partial_ {i} P \cdot P - \partial_ {i} P \cdot P = 0
$$

to reduce the expression to

$$
\begin{array}{l} \operatorname {T r} \left(\left[ U ^ {- 1} \partial_ {t} U \right] \left[ U ^ {- 1} \partial_ {k _ {x}} U \right] \left[ U ^ {- 1} \partial_ {k _ {y}} U \right]\right) \\ = \frac {2 \pi i}{T} (a + b) b \cdot \operatorname {T r} \left(P \partial_ {k _ {x}} P \partial_ {k _ {y}} P\right). \\ \end{array}
$$

Substituting in the above expressions for  $a$  and  $b$ , we find

$$
\begin{array}{l} \operatorname {T r} \left(\left[ U ^ {- 1} \partial_ {t} U \right] \left[ U ^ {- 1} \partial_ {k _ {x}} U \right] \left[ U ^ {- 1} \partial_ {k _ {y}} U \right]\right) \\ = \frac {2 \pi i}{T} [ 2 \cos (2 \pi t / T) - 2 ] \operatorname {T r} \left(P \partial_ {k _ {x}} P \partial_ {k _ {y}} P\right). \tag {C6} \\ \end{array}
$$

We are now ready to compute the winding number corresponding to  $U$ :

$$
\begin{array}{l} W [ U ] = \frac {1}{8 \pi^ {2}} \int d t d k _ {x} d k _ {y} \operatorname {T r} ([ U ^ {- 1} \partial_ {t} U ] \\ \times \left[ U ^ {- 1} \partial_ {k _ {x}} U \right] \left[ U ^ {- 1} \partial_ {k _ {y}} U \right]) - \left(k _ {x} \leftrightarrow k _ {y}\right) \\ = \frac {1}{8 \pi^ {2}} \int d t d k _ {x} d k _ {y} \frac {2 \pi i}{T} [ 2 \cos (2 \pi t / T) - 2 ] \\ \times \operatorname {T r} (P [ \partial_ {k _ {x}} P, \partial_ {k _ {v}} P ]) \\ = \frac {1}{2 \pi i} \int d k _ {x} d k _ {y} \operatorname {T r} \left(P \left[ \partial_ {k _ {x}} P, \partial_ {k _ {y}} P \right]\right). \tag {C7} \\ \end{array}
$$

The latter expression is precisely the Chern number  $\mathcal{C}$  [Eq. (13)] of the bands with quasienergy  $\varepsilon = -2\pi /T$

It is also possible to derive Eq. (C7) from simple physical considerations. To this end, let us calculate the number of Floquet edge modes  $n_{\mathrm{edge}}$  corresponding to  $U$  in two different ways. On one hand, we know that  $n_{\mathrm{edge}} = W[U]$ . On the other hand, it follows from the special form of  $U$  that the number of Floquet edge modes is equal to the number of edge modes of  $H$  with quasienergies between  $-2\pi / T$  and 0. The latter number is equal to the total Chern number  $\mathcal{C}$  of the  $\varepsilon = -2\pi / T$  bands of  $H$ . In this way, we deduce that  $n_{\mathrm{edge}} = \mathcal{C}$ . Combining these two results, the identity (C7) follows immediately.

[1] K. von Klitzing, G. Dorda, and M. Pepper, New Method for High-Accuracy Determination of the Fine-Structure Constant Based on Quantized Hall Resistance, Phys. Rev. Lett. 45, 494 (1980).  
[2] D.J. Thouless, M. Kohmoto, M.P. Nightingale, and M. den Nijs, Quantized Hall Conductance in a Two-Dimensional Periodic Potential, Phys. Rev. Lett. 49, 405 (1982).  
[3] C.L. Kane and E.J. Mele,  $Z_{2}$  Topological Order and the Quantum Spin Hall Effect, Phys. Rev. Lett. 95, 146802 (2005).  
[4] B. A. Bernevig, T. L. Hughes, and S.-C. Zhang, Quantum Spin Hall Effect and Topological Phase Transition in HgTe Quantum Wells, Science 314, 1757 (2006).  
[5] M. König, S. Wiedmann, C. Brune, A. Roth, H. Buhmann, L. W. Molenkamp, X.-L. Qi, and S.-C. Zhang, Quantum Spin Hall Insulator State in HgTe Quantum Wells, Science 318, 766 (2007).  
[6] D. Hsieh, D. Qian, L. Wray, Y. Xia, Y. S. Hor, R. J. Cava, and M. Z. Hasan, A Topological Dirac Insulator in a Quantum Spin Hall Phase, Nature (London) 452, 970 (2008).  
[7] A. L. Fetter, Rotating Trapped Bose-Einstein Condensates, Rev. Mod. Phys. 81, 647 (2009).  
[8] J. Dalibard, F. Gerbier, G. Juzeliūnas, and P. Öhberg, Colloquium: Artificial Gauge Potentials for Neutral Atoms, Rev. Mod. Phys. 83, 1523 (2011).  
[9] N. R. Cooper, Optical Flux Lattices for Ultracold Atomic Gases, Phys. Rev. Lett. 106, 175301 (2011).

[10] D.L. Campbell, G. Juzeliūnas, and I.B. Spielman, Realistic Rashba and Dresselhaus Spin-Orbit Coupling for Neutral Atoms, Phys. Rev. A 84, 025602 (2011).  
[11] Y.-J. Lin, K. Jiménez-García, and I. B. Spielman, Spin-Orbit-Coupled Bose-Einstein Condensates, Nature (London) 471, 83 (2011).  
[12] N.H. Lindner, G. Refael, and V. Galitski, Floquet Topological Insulator in Semiconductor Quantum Wells, Nat. Phys. 7, 490 (2011).  
[13] T. Oka and H. Aoki, Photovoltaic Hall Effect in Graphene, Phys. Rev. B 79, 081406(R) (2009).  
[14] J.-I. Inoue and A. Tanaka, Photoinduced Transition between Conventional and Topological Insulators in Two-Dimensional Electronic Systems, Phys. Rev. Lett. 105, 017401 (2010).  
[15] T. Kitagawa, T. Oka, A. Brataas, L. Fu, and E. Demler, Transport Properties of Nonequilibrium Systems under the Application of Light: Photoinduced Quantum Hall Insulators without Landau Levels, Phys. Rev. B 84, 235108 (2011).  
[16] Z. Gu, H.A. Fertig, D.P. Arovas, and A. Auerbach, Floquet Spectrum and Transport through an Irradiated Graphene Ribbon, Phys. Rev. Lett. 107, 216601 (2011).  
[17] N. H. Lindner, D. L. Bergman, G. Refael, and V. Galitski, Topological Floquet Spectrum in Three Dimensions via a Two-Photon Resonance, Phys. Rev. B 87, 235131 (2013).  
[18] E. Suárez Morell and L. E. F. Foa Torres, Radiation Effects on the Electronic Properties of Bilayer Graphene, Phys. Rev. B 86, 125449 (2012).  
[19] Y.T. Katan and D. Podolsky, Modulated Floquet Topological Insulators, Phys. Rev. Lett. 110, 016802 (2013).  
[20] W. Yao, A. H. MacDonald, and Q. Niu, Optical Control of Topological Quantum Transport in Semiconductors, Phys. Rev. Lett. 99, 047401 (2007).  
[21] T. Kitagawa, M.S. Rudner, E. Berg, and E. Demler, Exploring Topological Phases with Quantum Walks, Phys. Rev. A 82, 033429 (2010).  
[22] T. Kitagawa, E. Berg, M. Rudner, and E. Demler, Topological Characterization of Periodically Driven Quantum Systems, Phys. Rev. B 82, 235114 (2010).  
[23] L. Jiang, T. Kitagawa, J. Alicea, A.R. Akhmerov, D. Pekker, G. Refael, J.I. Cirac, E. Demler, M.D. Lukin, and P. Zoller, Majorana Fermions in Equilibrium and Driven Cold-Atom Quantum Wires, Phys. Rev. Lett. 106, 220402 (2011).  
[24] J.P. Dahlhaus, J.M. Edge, J. Tworzydlo, and C.W.J. Beenakker, Quantum Hall Effect in a One-Dimensional Dynamical System, Phys. Rev. B 84, 115133 (2011).  
[25] D.E. Liu, A. Levchenko, and H.U. Baranger, Floquet Majorana Fermions for Topological Qubits, arXiv:1211.1404.  
[26] B. Dóra, J. Cayssol, F. Simon, and R. Moessner, Optically Engineering the Topological Properties of a Spin Hall Insulator, Phys. Rev. Lett. 108, 056602 (2012).  
[27] J. Cayssol, B. Dóra, F. Simon, and R. Moessner, Floquet Topological Insulators, Phys. Status Solidi RRL 7, 101 (2013).  
[28] A.A. Reynoso and D. Frustaglia, Unpaired Floquet Majorana Fermions without Magnetic Fields, Phys. Rev. B 87, 115420 (2013).

[29] M. S. Rudner and L. S. Levitov, Topological Transition in a Non-Hermitian Quantum Walk, Phys. Rev. Lett. 102, 065703 (2009).  
[30] S. Diehl, E. Rico, M. A. Baranov, and P. Zoller, Topology by Dissipation in Atomic Quantum Wires, Nat. Phys. 7, 971 (2011).  
[31] T. Kitagawa, M. A. Broome, A. Fedrizzi, M. S. Rudner, E. Berg, I. Kassal, A. Aspuru-Guzik, E. Demler, and A. G. White, Observation of Topologically Protected Bound States in Photonic Quantum Walks, Nat. Commun. 3, 882 (2012).  
[32] M. C. Rechtsman, J. M. Zeuner, Y. Plotnik, Y. Lumer, D. Podolsky, F. Dreisow, S. Nolte, M. Segev, and A. Szameit, Photonic Floquet Topological Insulators, Nature (London) 496, 196 (2013).  
[33] A. P. Schnyder, S. Ryu, A. Furusaki, and A. W. W. Ludwig, Classification of Topological Insulators and Superconductors in Three Spatial Dimensions, Phys. Rev. B 78, 195125 (2008).  
[34] A. Kitaev, in Advances in Theoretical Physics, edited by V. Lebedev and M. Feigel'man, AIP Conf. Proc. No. 1134 (AIP, New York, 2009), p. 22.

[35] B.I. Halperin, Quantized Hall Conductance, Current-Carrying Edge States, and the Existence of Extended States in a Two-Dimensional Disordered Potential, Phys. Rev. B 25, 2185 (1982).  
[36] F.D.M. Haldane, Model for a Quantum Hall Effect without Landau Levels: Condensed-Matter Realization of the "Parity Anomaly," Phys. Rev. Lett. 61, 2015 (1988).  
[37] R. Bott and R. Seeley, Some Remarks on the Paper of Callias: “Axial Anomalies and Index Theorems on Open Spaces,” Commun. Math. Phys. 62, 235 (1978).  
[38] Z. Wang, X.-L. Qi, and S.-C. Zhang, Equivalent Topological Invariants of Topological Insulators, New J. Phys. 12, 065007 (2010).  
[39] Q.T. Vu, H. Haug, O.D. Mücke, T. Tritschler, M. Wegener, G. Khitrova, and H.M. Gibbs, Light-Induced Gaps in Semiconductor Band-to-Band Transitions, Phys. Rev. Lett. 92, 217403 (2004).  
[40] J. W. McIver, D. Hsieh, H. Steinberg, P. Jarillo-Herrero, and N. Gedik, Control over Topological Insulator Photocurrents with Light Polarization, Nat. Nanotechnol. 7, 96 (2012).  
[41] A. Yu. Kitaev, Anyons in an Exactly Solved Model and Beyond, Ann. Phys. (Amsterdam) 321, 2 (2006).