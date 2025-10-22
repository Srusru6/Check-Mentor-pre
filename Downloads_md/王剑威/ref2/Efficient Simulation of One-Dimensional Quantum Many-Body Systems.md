# Efficient Simulation of One-Dimensional Quantum Many-Body Systems

Guifré Vidal

Institute for Quantum Information, California Institute of Technology, Pasadena, California 91125, USA (Received 10 February 2004; published 19 July 2004)

We present a numerical method to simulate the time evolution, according to a generic Hamiltonian made of local interactions, of quantum spin chains and systems alike. The efficiency of the scheme depends on the amount of entanglement involved in the simulated evolution. Numerical analysis indicates that this method can be used, for instance, to efficiently compute time-dependent properties of low-energy dynamics in sufficiently regular but otherwise arbitrary one-dimensional quantum many-body systems. As by-products, we describe two alternatives to the density matrix renormalization group method.

DOI: 10.1103/PhysRevLett.93.040502

Since the early days of quantum theory, progress in understanding the physics of quantum many-body systems has been hindered by a serious, well-known computational obstacle. The number of parameters required to describe an arbitrary state of  $n$  quantum systems grows exponentially with  $n$ , a fact that renders the simulation of generic quantum many-body dynamics intractable.

A number of techniques have been developed to analyze specific quantum many-body problems. Exactly and quasiexactly solvable models [1] offer valuable insight in particular cases, and their solutions can be used as the basis for perturbative studies. With quantum Monte Carlo (QMC) calculations [2], static properties of the ground state of a large class of many-body Hamiltonians can be evaluated. In one-dimensional settings, including quantum spin chains, ground-state expectation values for local observables, such as the energy and two-point correlation functions, can also be computed with extraordinary accuracy with the density matrix renormalization group (DMRG) [3].

The importance and ingenuity of these methods cannot be overstated. However, solvable models and their extensions using perturbation theory apply to a very restricted class of physical systems, whereas QMC and DMRG calculations produce reliable outcomes mainly only for static properties of certain ground states. In particular, the efficient simulation of time-dependent properties remains an open problem in most nonperturbative cases. In addition to severely limiting our understanding of quantum collective phenomena, such as high- $T_{C}$  superconductivity and quantum phase transitions, the inability to efficiently simulate quantum dynamics has deep implications in quantum information science [4]. It is also a practical obstacle for the development of technology based on engineered quantum systems.

In this Letter, we describe a numerical scheme to simulate certain quantum many-body dynamics. We explain how to efficiently simulate Hamiltonian evolutions in one-dimensional arrays of quantum systems, such as quantum spin chains, with a computational cost that grows linearly in the number of systems. We also propose

PACS numbers: 03.67.Mn, 02.70.-c, 05.50.+q

two alternatives to the DMRG scheme. The key idea is to exploit the fact that, in one spatial dimension, low energy quantum dynamics are often only slightly entangled. We employ a technique developed in the context of quantum computation [5]—thereby illustrating how tools from quantum information science may find applications in other areas of quantum physics (see also [6-9]). The present numerical method can be used, for instance, to determine the time-dependent vacuum expectation value

$$
\langle O _ {x, t} ^ {\dagger} O _ {0, 0} \rangle , \tag {1}
$$

where  $O$  is a local Heisenberg operator. In some cases, and for specific choices of  $O$ , the Fourier transform  $S(k,\omega)$  of (1) is accessible experimentally, e.g., through neutron scattering for phonon dynamics in a solid. This allows for a direct comparison of experimental and simulated data.

We consider a one-dimensional array of quantum systems, labeled by index  $l$ ,  $l \in \{1, \ldots, n\}$ , each one described by a local Hilbert space  $\mathcal{H}_d$  of finite dimension  $d$ . Given a pure state  $|\Psi\rangle \in \mathcal{H}_d^{\otimes n}$  of the  $n$  systems, we characterize the entanglement between a block  $A$  containing the  $m$  first systems,  $l \in \{1, \ldots, m\}$ , and a block  $B$  containing the  $n - m$  remaining systems by  $\chi_A$ , the rank of the reduced density matrix  $\rho_A$  for block  $A$ ,

$$
\chi_ {A} \equiv \operatorname {r a n k} (\rho_ {A}), \quad \rho_ {A} \equiv \operatorname {t r} _ {B} (| \Psi \rangle \langle \Psi |). \tag {2}
$$

Central in the present discussion is parameter  $\chi$ ,

$$
\chi \equiv \max  _ {m} \chi_ {A}, \tag {3}
$$

the maximum, over the size  $m \in \{1, \dots, n - 1\}$  of block  $A$ , of the entanglement between blocks  $A$  and  $B$  [10].

We focus on the numerical simulation of a collective evolution of the  $n$  systems according to a generic (possibly time-dependent) Hamiltonian  $H_{n}$  made of local interactions [11]. The essential requirement for the numerical method to be efficient will be that the entanglement  $\chi$  (in practice a related, effective parameter  $\chi_{\epsilon}$ ) remains "small" during the simulated dynamics, in a sense to be specified later. In addition, for the sake of

simplicity, here we consider only Hamiltonians made of arbitrary single-body and two-body terms, with the interactions restricted to nearest neighbors,

$$
H _ {n} = \sum_ {l = 1} ^ {n} K _ {1} ^ {[ l ]} + \sum_ {l = 1} ^ {n - 1} K _ {2} ^ {[ l, l + 1 ]}. \tag {4}
$$

The simulation scheme is based on an efficient decomposition for slightly entangled states and on a protocol to efficiently update this decomposition when a unitary transformation is applied to one or two (nearest neighbor) systems, as described in the next paragraphs.

Efficient decomposition. State  $|\bar{\Psi}\rangle \in \mathcal{H}_d^{\otimes n}$  can be expressed in terms of  $\mathcal{O}(nd\chi^2)$  parameters by first expanding it in a product basis,

$$
| \Psi \rangle = \sum_ {i _ {1} = 1} ^ {d} \dots \sum_ {i _ {n} = 1} ^ {d} c _ {i _ {1} \dots i _ {n}} | i _ {1} \rangle \otimes \dots \otimes | i _ {n} \rangle , \tag {5}
$$

and by then writing the  $d^n$  complex coefficients  $c_{i_1\dots i_n}$  in terms of  $n$  tensors  $\Gamma^{[l]}$  and  $n - 1$  vectors  $\lambda^{[l]}$ ,

$$
c _ {i _ {1} i _ {2} \dots i _ {n}} = \sum_ {\alpha_ {1}, \dots , \alpha_ {n - 1}} \Gamma_ {\alpha_ {1}} ^ {[ 1 ] i _ {1}} \lambda_ {\alpha_ {1}} ^ {[ 1 ]} \Gamma_ {\alpha_ {1} \alpha_ {2}} ^ {[ 2 ] i _ {2}} \lambda_ {\alpha_ {2}} ^ {[ 2 ]} \Gamma_ {\alpha_ {2} \alpha_ {3}} ^ {[ 3 ] i _ {3}} \dots \Gamma_ {\alpha_ {n - 1}} ^ {[ n ] i _ {n}}, \tag {6}
$$

where each  $\alpha$  runs from one to  $\chi$ . We refer to [5] for a detailed explanation on how to obtain this decomposition, denoted  $\mathcal{D} \equiv \{\Gamma^{[l]}, \lambda^{[l]}\}$  from now on.

Decomposition  $\mathcal{D}$  has two important precedents. Except for a number of technical details, it corresponds to a construction introduced by Fannes, Nachtergaele, and Werner to study the so-called finitely correlated states [12]—in turn a generalization of valence bond states as analyzed by Affleck, Kennedy, Lieb, and Tasaki [13]—and to Ostlund and Rommer's description of matrix product states [14] used to analytically study the fixed points of the DMRG method. Thus, the present simulation algorithm can be understood as an extension of these previous works to include time dependence [15].

Vector  $\lambda^{[l]}$  in Eq. (6) contains the decreasingly ordered coefficients  $\lambda_1^{[l]} \geq \lambda_2^{[l]} \geq \dots \geq \lambda_\chi^{[l]} \geq 0$  of the Schmidt decomposition [16] of  $|\Psi\rangle$  according to the splitting  $A:B$ , where  $A = [1, \ldots, l]$ ,

$$
| \Psi \rangle = \sum_ {\alpha = 1} ^ {\chi} \lambda_ {\alpha} ^ {[ l ]} | \Phi_ {\alpha} ^ {[ 1 \dots l ]} \rangle | \Phi_ {\alpha} ^ {[ (l + 1) \dots n ]} \rangle . \tag {7}
$$

In a generic case  $\chi$  grows exponentially with  $n$ . However, in one-dimensional settings it is sometimes possible to obtain a good approximation to  $|\Psi\rangle$  by considering only the first  $\chi_{\epsilon}$  terms in (7), with  $\chi_{\epsilon} \ll \chi$ ,

$$
| \Psi \rangle \approx \left[ \sum_ {\alpha = 1} ^ {\chi_ {\epsilon}} | \lambda_ {\alpha} ^ {[ l ]} | ^ {2} \right] ^ {- (1 / 2)} \sum_ {\alpha = 1} ^ {\chi_ {\epsilon}} \lambda_ {\alpha} ^ {[ l ]} | \Phi_ {\alpha} ^ {[ 1 \dots l ]} \rangle | \Phi_ {\alpha} ^ {[ (l + 1) \dots n ]} \rangle . \tag {8}
$$

This is due to the following remarkable facts involving the ground state  $|\Psi_{gr}\rangle$  and low energy excitations  $|\Psi_{(k)}\rangle$  of

040502-2

a sufficiently regular, one-dimensional Hamiltonian  $H_{n}$  as in Eq. (4) [17].

Observation 1: Numerical analysis shows that the Schmidt coefficients  $\lambda_{\alpha}^{[l]}$  of the ground state  $|\Psi_{gr}\rangle$  of  $H_{n}$  decay (roughly) exponentially with  $\alpha$ :

$$
\lambda_ {\alpha} ^ {[ l ]} \sim \exp (- K \alpha), \quad K > 0. \tag {9}
$$

Observation 2: Numerical analysis shows that during a low-energy evolution, as given by vector  $|\Psi_t\rangle = \sum_k c_k(t) |\Psi_{(k)}\rangle$ , the Schmidt coefficients  $\lambda_{\alpha}^{[l]}(t)$  also decay (roughly) exponentially with  $\alpha$ .

The first observation is at the root of the success of the DMRG in one dimension [7,18]. The second observation implies that, in certain one-dimensional problems, a good approximation to  $|\Psi_t\rangle$  can be obtained by keeping only a small number  $\chi_{\epsilon}$  of terms in its Schmidt decomposition, leading to an efficient time-dependent decomposition  $\mathcal{D}_t$ .

Simulation protocol. Our aim is to simulate the evolution of the  $n$  systems, initially in state  $|\Psi_0\rangle$ , for a time  $T$  according to the Hamiltonian  $H_{n}$  of Eq. (4). We next sketch (i) how to construct the initial decomposition  $\mathcal{D}_0$  for state  $|\Psi_0\rangle$  and (ii) how to update the decomposition  $\mathcal{D}_t$  of the time-evolved state  $|\Psi_t\rangle$  for increasing values of a discretized time  $t \in \{\delta, 2\delta, \dots, T\}$ ,  $\delta / T \ll 1$ .

(i) Initialization: When  $|\Psi_0\rangle$  is related to the ground state  $|\Psi_{gr}\rangle$  of Hamiltonian  $H_{n}$  by a sufficiently local transformation  $Q$  [19],

$$
| \Psi_ {0} \rangle = Q | \Psi_ {g r} \rangle , \tag {10}
$$

$\mathcal{D}_0$  can be obtained from decomposition  $\mathcal{D}_{gr}$  for  $|\Psi_{gr}\rangle$  by simulating the action of  $Q$  on  $|\Psi_{gr}\rangle$ . In turn,  $\mathcal{D}_{gr}$  can be obtained through one of the following three methods: (i1) by extracting it from the solution of the DMRG method; (i2) by considering any product state,

$$
\left| \Phi_ {\otimes} \right\rangle \equiv \left| \phi^ {[ 1 ]} \right\rangle \otimes \dots \otimes \left| \phi^ {[ n ]} \right\rangle , \quad \langle \Phi_ {\otimes} | \Psi_ {g r} \rangle \neq 0 \tag {11}
$$

[for which  $\mathcal{D}$  is trivial] and by using the present scheme to simulate an evolution in imaginary time  $\tau$  according to  $H_{n}$ ,

$$
| \Psi_ {g r} \rangle = \lim _ {\tau \rightarrow \infty} \frac {\exp (- H _ {n} \tau) | \Phi_ {\otimes} \rangle}{\| \exp (- H _ {n} \tau) | \Phi_ {\otimes} \rangle \|}; \tag {12}
$$

or (i3) by simulating an adiabatic evolution from some product state  $|\Phi_{\otimes}^{\prime}\rangle$  to  $|\Psi_0\rangle$  through a time-dependent Hamiltonian that smoothly interpolates between a local Hamiltonian  $H_{n}^{\prime}$  such that it has  $|\Phi_{\otimes}^{\prime}\rangle$  as its ground state and Hamiltonian  $H_{n}$ . Thus, methods (i2) and (i3) rely on simulating a Hamiltonian evolution (see below) from a product state and constitute two alternatives to the DMRG scheme [15].

(ii) Evolution: For simplicity, we assume that  $H_{n}$  does not depend on time [20]. After a time interval  $T$ , the evolved state  $|\Psi_T\rangle$  is given by

$$
| \Psi_ {T} \rangle = \exp (- i H _ {n} T) | \Psi_ {0} \rangle . \tag {13}
$$

It is convenient to decompose  $H_{n}$  as  $H_{n} = F + G$ ,

040502-2

$$
F \equiv \sum_ {\text {e v e n} l} F ^ {[ l ]} \equiv \sum_ {\text {e v e n} l} \left(K _ {1} ^ {[ l ]} + K _ {2} ^ {[ l, l + 1 ]}\right), \tag {14}
$$

$$
G \equiv \sum_ {\text {o d d} l} G ^ {[ l ]} \equiv \sum_ {\text {o d d} l} \left(K _ {1} ^ {[ l ]} + K _ {2} ^ {[ l, l + 1 ]}\right), \tag {15}
$$

where  $[F^{[l]}, F^{[l']}] = 0$  ([G[l], G[l'] = 0) for even (odd)  $l, l'$ , but possibly  $[F, G] \neq 0$ . For a small  $\delta > 0$ , the Trotter expansion of order  $p$  for  $\exp(-iH_nT)$  reads [21]

$$
e ^ {- i (F + G) T} = [ e ^ {- i (F + G) \delta} ] ^ {T / \delta} \approx [ f _ {p} (U _ {F \delta}, U _ {G \delta}) ] ^ {T / \delta}, \tag {16}
$$

where  $U_{F\delta} \equiv e^{-iF\delta}$ ,  $U_{G\delta} \equiv e^{-iG\delta}$ , and where  $f_{1}(x,y) = xy$ ,  $f_{2}(x,y) = x^{1/2}yx^{1/2}$  for first and second order expansions (see [21] for  $p = 3,4$ ). Equation (16) approximates the evolution operator  $\exp(-iH_nT)$  by a product of  $\mathcal{O}(T/\delta)$ $n$ -body transformations  $U_{F\delta}$  and  $U_{G\delta}$ , which in turn can be expressed as a product of two-body gates  $V_{2}^{[I]}$  and  $W_{2}^{[I]}$ :

$$
U _ {F \delta} = \prod_ {\text {e v e n} l} V _ {2} ^ {[ l ]}, \quad V _ {2} ^ {[ l ]} \equiv e ^ {- i F ^ {[ l ]} \delta} \quad \text {e v e n} l, \tag {17}
$$

$$
U _ {G \delta} = \prod_ {\text {o d d} l} W _ {2} ^ {[ l ]}, \quad W _ {2} ^ {[ l ]} \equiv e ^ {- i G ^ {[ l ]} \delta} \quad \text {o d d} l. \tag {18}
$$

The simulation of the time evolution (13) is then accomplished by iteratively applying gates  $U_{F\delta}$  and  $U_{G\delta}$  to  $|\Psi_0\rangle$  a number  $\mathcal{O}(T / \delta)$  of times, and by updating decomposition  $\mathcal{D}$  at each step. If  $|\tilde{\Psi}_t\rangle$  denotes the approximate evolved state at time  $t$ , then we have

$$
\left| \tilde {\Psi} _ {t + \delta} \right\rangle = f _ {p} \left(U _ {F \delta}, U _ {G \delta}\right) \left| \tilde {\Psi} _ {t} \right\rangle , \tag {19}
$$

where  $f_{p}(U_{F\delta}, U_{G\delta})$  consists of a product of  $\mathcal{O}(n)$  two-body gates  $V_{2}^{[l]}$  and  $W_{2}^{[l]}$ , and where we use lemma 2 in [5] to update  $\mathcal{D}$  after each of these gates.

Errors and computational cost. The main source of errors in the scheme are the truncation (8) and the Trotter expansion (16). We use the fidelity error

$$
\epsilon (t) \equiv 1 - | \langle \Psi_ {t} | \tilde {\Psi} _ {t} \rangle | ^ {2} \tag {20}
$$

to measure how similar the simulated  $|\tilde{\Psi}_t\rangle$  and the exact  $|\Psi_t\rangle$  are. The truncation error  $\epsilon_{1}$  incurred in replacing (7) with (8) reads

$$
\epsilon_ {1} = \sum_ {\alpha = \chi_ {\epsilon} + 1} ^ {\chi} (\lambda_ {\alpha} ^ {[ l ]}) ^ {2}. \tag {21}
$$

Truncation errors accumulate additively with time during the simulation of a unitary evolution. On the other hand, the order- $p$  Trotter expansion neglects corrections  $\epsilon_{2}$  that scale as [22]

$$
\epsilon_ {2} \sim \delta^ {2 p} T ^ {2}. \tag {22}
$$

A straightforward generalization of lemma 2 in [5] implies that updating  $\mathcal{D}$  after a two-body gate requires  $\mathcal{O}(d^3\chi^3)$  basic operations [and  $\mathcal{O}(d^2\chi^2)$  memory space]. Gates  $U_{F\delta}$  and  $U_{G\delta}$  are applied  $\mathcal{O}(T / \delta)$  times and each of them decomposes into about  $n$  two-body gates. Therefore  $\mathcal{O}[n(d\chi)^3 T / \delta]$  operations are required to apply (16) on

$|\Psi_0\rangle$ . If no truncation takes place, so that the error  $\epsilon$  is due only to the Trotter expansion, it follows from (22) that the number of basic operations or computational time  $T_{c}$  scales as

$$
T _ {c} \sim n (d \chi) ^ {3} \left(\frac {T ^ {1 + p}}{\epsilon^ {1 / 2}}\right) ^ {1 / p}. \tag {23}
$$

Example. The numerical scheme has been tested extensively using MATLAB code in a Pentium IV at  $1.2\mathrm{GHz}$  both to find an approximation to the ground state  $|\Psi_{gr}\rangle$  of a number of Hamiltonians  $H_{n}$  of the form (4) [23] and to simulate time evolutions of local perturbations of  $|\Psi_{gr}\rangle$ . Results addressing specific one-dimensional settings of interest will be presented elsewhere. Figure 1 illustrates with a simple example the performance of the method by comparing an exact time evolution and the corresponding simulation. It considers a spin  $1/2$  ferromagnetic chain,

$$
H _ {n} = - B \sum_ {l = 1} ^ {n} \sigma_ {z} ^ {[ l ]} - J \sum_ {l = 1} ^ {n - 1} \vec {\sigma} ^ {[ l ]} \cdot \vec {\sigma} ^ {[ l + 1 ]}, \tag {24}
$$

for which the ground state is the product state  $|\Psi_{gr}\rangle = |0\rangle^{\otimes n}$  and, most conveniently, the exact time evolution of

![](images/edc58dc0145a5828b8c91a706222fc07b989e77b6a4e2a716559eb1c683df080.jpg)  
FIG. 1 (color online). Propagation of a spin wave in the ferromagnetic chain (24) with  $n = 30$  spins,  $B = J = 1$ ,  $T = 25$ , and  $\delta = 0.005$ . The eigenvalues  $p_{\alpha} = |\lambda_{\alpha}^{[15]}|^{2}$ ,  $\alpha = 1, \ldots, 17$ , of the reduced density matrix  $\rho_{A}$  for half a chain [see Eq. (7)] are plotted as a function of time (thin, irregular, rapidly oscillating lines). Notice the exponential decay of  $p_{\alpha}$  in  $\alpha$  for any fixed value of  $t / J$ , a seemingly common feature of low-energy dynamics in sufficiently regular, but otherwise arbitrary local models in one dimension. The time scale is such that the spin wave, originating at the left end of the open chain [see state  $|\Psi_0\rangle$  after Eq. (24)] travels along the open chain 7 times, bouncing backward each time it reaches one of the extremes of the chain. The figure shows the error fidelity  $\epsilon(t)$  corresponding to keeping all 17 terms in (7) in an order  $p = 2$  Trotter expansion. Notice that, as predicted by Eq. (22),  $\epsilon(t)$  grows quadratically in the simulated time. Errors  $\epsilon'(t)$  and  $\epsilon''(t)$  correspond to keeping  $\chi_{\epsilon} = 12$  and  $\chi_{\epsilon} = 8$  terms in Eq. (8). Truncation errors are of the order of the neglected eigenvalues  $p_{\alpha}$ .

the state  $|\Psi_0\rangle = |1\rangle^{\otimes 2}\otimes |0\rangle^{\otimes n - 2}$  can be computed efficiently, since the dynamics are confined to a subspace of  $\mathcal{H}_2^{\otimes n}$  of dimension  $n(n - 1) / 2$ . In addition,  $\chi$  in Eq. (7) is at most  $n / 2 + 2$ . Thus, for this system we can compare the exact solution  $|\Psi_T\rangle$  in (13) with the approximation  $|\tilde{\Psi}_T\rangle$  obtained through simulation. When  $\chi_{\epsilon} = n / 2 + 2$ , also a confirmation of (23) can be obtained for different values of  $n$ ,  $T$ , and  $\delta$ .

Discussion.-In this Letter, we have shown how to efficiently simulate low energy dynamics in one-dimensional arrays of  $n$  quantum systems by using  $\mathcal{O}(n)$  parameters. It may at first seem difficult to reconcile this result with the fact that  $\mathcal{O}(\exp(n))$  parameters are required to describe a generic state of  $n$  systems. However, the locality of the interactions and the (one-dimensional) geometry of the problem make the Hamiltonian  $H_{n}$  highly nongeneric. It is thus conceivable that, correspondingly, the dynamics generated by  $H_{n}$  are constrained to occur in (or can be well approximated by states from) a submanifold of  $\mathcal{H}_{d}^{\otimes n}$  with remarkably small dimension.

Further generalizations to Hamiltonians with long-range interactions, to momentum space, to bosonic and fermionic systems, and a specific scheme to address critical systems will be presented elsewhere. These results have also been generalized to slightly correlated mixed-state dynamics, and, in particular, to finite temperature quantum many-body dynamics in one dimension.

The author thanks Dave Bacon, Ignacio Cirac, and David DiVincenzo for valuable advice, and Sergey Bravyi and Miguel Angel Martin-Delgado for drawing attention to Refs. [12,14] after this work was mostly completed. Support from the U.S. National Science Foundation under Grant No. EIA-0086038 is acknowledged.

[1] See, for instance, S. Albeverio, F. Gesztesy, R. Hoegh-Krohn, and H. Holden, Solvable Models in Quantum Mechanics, Texts and Monographs in Physics (Springer-Verlag, New York, 1988); A.G. Ushveridze, Quasi-Exactly Solvable Models in Quantum Mechanics (Institute of Physics Publishing, London, 1994).  
[2] M. Suzuki, Quantum Monte Carlo Methods in Equilibrium and Nonequilibrium Systems, Springer Series in Solid-State Sciences (Springer-Verlag, Berlin, 1986).  
[3] S.R. White, Phys. Rev. B 48, 10345 (1993); S. Rommer and S. Östlund, Density Matrix Renormalization (Springer-Verlag, Berlin, 1999).  
[4] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, England, 2000).  
[5] G. Vidal, Phys. Rev. Lett. 91, 147902 (2003).  
[6] J. Preskill, J. Mod. Opt. 47, 127 (2000).  
[7] G. Vidal, J. I. Latorre, E. Rico, and A. Kitaev, Phys. Rev. Lett. 90, 227902 (2003).  
[8] H. L. Haselgrove, M. A. Nielsen, and T. J. Osborne, quant-ph/0308083.

[9] F. Verstraete, M. Popp, and J. I. Cirac, quant-ph/0307009.  
[10] The definition of  $\chi$  in the present work, Eq. (3), differs from that of Eq. (3) in [5]. In the latter the maximization of  $\chi_{A}$  considered all possible blocks  $A$  and not just those containing the  $m$  first systems. Therefore the condition that  $\chi$  be small is here significantly less demanding, as a restriction on entanglement, than the analogous condition in [5].  
[11] We could in general consider a Hamiltonian  $H_{n}$  that is a sum of terms, each one involving at most  $k$  systems, for a small  $k$  independent of  $n$ . Physically reasonable Hamiltonians are of this form. However, Hamiltonian (4) contains some additional constraints.  
[12] M. Fannes, B. Nachtergaele, and R. F. Werner, Commun. Math. Phys. 144, 443 (1992); J. Funct. Anal. 120, 511 (1994).  
[13] I. Affleck, T. Kennedy, E. H. Lieb, and H. Tasaki, Phys. Rev. Lett. 59, 799 (1987); Commun. Math. Phys. 155, 477 (1988).  
[14] S. Östlund and S. Rommer, Phys. Rev. Lett. 75, 3537 (1995).  
[15] See A. J. Daley, C. Kollath, U. Schollwoeck, and G. Vidal, J. Stat. Mech. P04005 (2004), http://www.iop.org/EJ/abstract/1742-5468/2004/04/P04005, for a comparison between DMRG and the present simulation algorithm.  
[16] E. Schmidt, Math. Ann. 63, 433 (1907); A. Ekert and P.L. Knight, Am. J. Phys. 63, 415 (1995); A. Peres, Quantum Theory: Concepts and Methods (Kluwer Academic Publishers, Dordrecht, 1995).  
[17] The conditions under which such an exponential decay occurs are presently under investigation.  
[18] See I. Peschel, J. Phys. A 36, L205 (2003), and references therein.  
[19] Operator  $Q = Q_{p}\dots Q_{2}Q_{1}$  could be the product of a small number  $p$  of operators  $Q_{m}$ , where each  $Q_{m}$  is at most a two-body transformation, and such that for  $m = 1,\ldots ,p$ , vector  $Q_{m}\dots Q_{1}|\Psi_{0}\rangle \in H_{d}^{\otimes n}$  can be efficiently described using  $\mathcal{D}$ . Examples are given by a product of operators  $\sigma^{+}\equiv (\sigma_{x} - i\sigma_{y}) / 2$  acting on several sites of a spin chain, or a product of (real space) creation operators  $a^\dagger$  in a 1D bosonic or fermionic system.  
[20] If  $H_{n}$  depends on time, we consider time intervals  $\Delta T$  such that  $H_{n}$  is approximately constant between  $t$  and  $t + \Delta T$ , and to each interval we apply the same reasoning as in the time-independent case.  
[21] M. Suzuki, Phys. Lett. A 146, 319 (1990); J. Math. Phys. (N.Y.) 32, 400 (1991). For third and fourth order expansions, see also A. T. Sornborger and E. D. Stewart, quant-ph/9809009.  
[22] The error  $\zeta \equiv \mathrm{tr}|e^{-iH_nT} - f_p^{T / \delta}|$  [cf. Eqs. (13) and (16)] scales as  $T / \delta$  times  $\delta^p$  [21] for an order  $p$  Trotter expansion. The approximated state  $|\tilde{\Psi}_{\mathrm{T}}\rangle$  is, up to a phase,  $|\tilde{\Psi}_{\mathrm{T}}\rangle = [1 - \mathcal{O}(\zeta^2)]|\Psi_{\mathrm{T}}\rangle +\mathcal{O}(\zeta)|\Psi^{\perp}(\mathrm{T})\rangle$  so that  $\epsilon \equiv 1 - |\langle \Psi |\tilde{\Psi}\rangle |^2$  scales as  $\zeta^2\sim \delta^{2p}T^2$  
[23] An approximation to the ground state of a noncritical spin chain, with  $n = 80$  spins, local dimension  $d = 2$ ,  $\chi_{\epsilon_1} = 20$ , and a sufficiently regular (but otherwise arbitrary)  $H_{n}$  with nearest neighbor interactions can be obtained in half an hour by evolving some product state in imaginary time as in (12), until decomposition  $\mathcal{D}_{\tau}$  converges within an accuracy  $1 - |\langle \tilde{\Psi}_{\tau}|\tilde{\Psi}_{\tau +\tau^{\prime}}\rangle |^{2} < 10^{-10}$ .