# ARTICLE OPEN

Check for updates

# Realization of quantum signal processing on a noisy quantum computer

Yuta Kikuchi  $① ^ { 1 , 2 \text{三} }$  , Conor Mc Keever  $① ^ { 3 }$  , Luuk Coopmans  $① ^ { 3 }$  , Michael Lubasch  $① ^ { 3 }$  and Marcello Benedetti  $① ^ { 3 \text{三} }$

Quantum signal processing (QSP) is a powerful toolbox for the design of quantum algorithms and can lead to asymptotically optimal computational costs. Its realization on noisy quantum computers without fault tolerance, however, is challenging because it requires a deep quantum circuit in general. We propose a strategy to run an entire QSP protocol on noisy quantum hardware by carefully reducing overhead costs at each step. To illustrate the approach, we consider the application of Hamiltonian simulation for which QSP implements a polynomial approximation of the time evolution operator. We test the protocol by running the algorithm on the Quantumium H1-1 trapped-ion quantum computer powered by Honeywell. In particular, we compute the time dependence of bipartite entanglement entropies for Ising spin chains and find good agreements with exact numerical simulations. To make the best use of the device, we determine optimal experimental parameters by using a simplified error model for the hardware and numerically studying the trade-off between Hamiltonian simulation time, polynomial degree, and total accuracy. Our results are the first step in the experimental realization of QSP-based quantum algorithms.

npj Quantum Information (2023)9:93; https://doi.org/10.1038/s41534-023-00762-0

# INTRODUCTION

Several quantum algorithms are known to outperform their classical counterparts by computational costs that asymptotically scale better, e.g., Shor's prime factoring algorithm<sup>1</sup>, Hamiltonian simulation<sup>2,3</sup> and Grover search<sup>4,5</sup>. Their realization on actual quantum computers, however, requires additional qubits and gates to correct errors that naturally occur in real physical devices. Currently available noisy quantum computers are not capable yet of running such quantum algorithms for large problem sizes.

In the context of noisy quantum circuits, there are two regimes in which the classical computational requirements for simulating a quantum computer remain tractable. First, shallow circuits typically generate small amounts of entanglement making them amenable to classical simulation. Second, deep circuits quickly accumulate errors causing decoherence towards a regime which can also be treated efficiently on classical computers[6,7]. Between these two extremes, there is an optimal working point at which maximum non-trivial quantum correlation is attained and where accurate simulation may become challenging for a classical computer[8]. In light of this, a promising route towards achieving a genuine quantum advantage without fault tolerance is to realize the aforementioned algorithms while operating the computer at its optimal working point. In order to design such an algorithm, it is therefore essential to account for the influence of noise on the circuits which implement it.

In this work, we propose to heuristically optimize the depth of quantum circuits and operate where we can make the most out of our noisy quantum computer. With this heuristic approach, we provide the first realization of quantum signal processing (QSP) on a trapped-ion quantum computer. QSP was proposed in $^{9}$  and is now recognized as one of the most powerful frameworks for developing quantum algorithms. It gives a unifying perspective on

seemingly distinct algorithms such as amplitude amplification and the quantum linear systems algorithm and improves on their computational resources $^{10,11}$ . Such flexibility stems from the fact that QSP allows one to apply almost any polynomial transformation to an input scalar or matrix. In the literature, QSP often refers to a polynomial transformation applied to an input scalar, and its generalizations apply a polynomial transformation to eigenvalues (QET) or singular values (QSVT) of an input matrix. Throughout this article, we do not make such a distinction and refer to all these protocols as QSP.

Hamiltonian simulation is an example where QSP provides an improved asymptotic scaling over other algorithms. Since Feynman's seminal proposal $^{12}$ , Hamiltonian simulation has been a fundamental problem of quantum computing. An efficient Hamiltonian simulation algorithm allows us to simulate the real-time dynamics of a quantum system described by a Hamiltonian  $H$  with computational resources scaling at most polynomially in evolution time  $t$ , system size  $n$ , and inverse of required accuracy  $1/\epsilon$ . Extensive studies have been devoted to exploring efficient algorithms for Hamiltonian simulation, which include product formulas $^{2,13-15}$ , quantum walks $^{16}$ , the truncated Taylor-series expansion $^{17}$ , randomized protocols $^{18-22}$ , and making use of classical optimization techniques $^{23-25}$ . Nowadays, the QSP-based algorithm is known to exhibit nearly optimal asymptotic scaling $^{10,26,27}$  (see also $^{28}$  for a comparative survey).

$\mathsf{In}^{29}$ , the authors demonstrate the QSP protocol using random Hamiltonians on a superconducting device for the purpose of benchmarking. The present work takes a step forward by realizing QSP on the Quantumum H1-1 trapped-ion quantum computer and performing the Hamiltonian simulation of physically relevant quantum systems. After the release of the present manuscript, another group demonstrated QSP for the task of quantum channel discrimination<sup>30</sup>.

# RESULTS

# Review of Hamiltonian simulation by quantum signal processing

The Hamiltonian simulation algorithm solves the real-time dynamics of a quantum system by applying a real-time evolution operator  $\mathrm{e}^{-\mathrm{i}Ht}$  to some initial state  $|\psi_0\rangle$ , where the Hamiltonian  $H$  is given by a Hermitian operator in this work. We employ QSP in order to find an approximate real-time evolution operator that can be efficiently implemented on a quantum computer. QSP outputs a degree-  $d$  polynomial  $f \in \mathbb{C}[x]$  using a sequence of unitary operators<sup>9,10,26,27</sup>,

$$
U _ {\mathrm {Q S P}} := \prod_ {k = 1} ^ {d} [ S (\phi_ {k}) W (x) ] = \left( \begin{array}{c c} f (x) & * \\ * & * \end{array} \right), \tag {1}
$$

$$
S (\phi) := \left( \begin{array}{c c} \mathrm {e} ^ {\mathrm {i} \phi} & 0 \\ 0 & \mathrm {e} ^ {- \mathrm {i} \phi} \end{array} \right), \tag {2}
$$

$$
W (x) := \left( \begin{array}{c c} x & \sqrt {1 - x ^ {2}} \\ \sqrt {1 - x ^ {2}} & - x \end{array} \right), \tag {3}
$$

where  $*$  stands for an unspecified entry. Here, we follow the convention of Corollary 8 in $^{10}$  (preprint version), where  $W(x)$  takes the form of a reflection operator. For a polynomial  $f(x)$  that satisfies certain conditions $^{10,11}$  there always exists a set of QSP angles  $\{\phi_k\}$ . The conditions are: (i)  $f$  must have parity-  $(d \bmod 2)$ , (ii)  $|f(x)| \leq 1$  for all  $x \in [-1,1]$ , (iii)  $|f(x)| \geq 1$  for all  $x \in (-\infty, 1] \cup (1,\infty]$ , and (iv)  $f(ix)f^*(ix) \geq 1$  for all  $x \in \mathbb{R}$  if  $d$  is even. The function  $f(x)$  is implemented by computing such angles  $\{\phi_k\}$ , and is encoded in the expectation  $\langle 0|U_{\mathrm{QSP}}|0\rangle$ . It is evident from Eq. (1) that the circuit depth is proportional to the degree  $d$ .

Finding an efficient Hamiltonian simulation algorithm with QSP starts by approximating the function  $\mathrm{e}^{-\mathrm{i}xt}$  with a fixed-degree polynomial on an interval  $I \subseteq [-1, 1]$ . Given time  $t > 0$  and accuracy  $c_{\mathrm{poly}}$ , we find a polynomial  $f$  such that

$$
\max  _ {x \in I} | f (x) - e ^ {- i x t} | \leq \epsilon_ {\text {p o l y}}. \tag {4}
$$

One way to find  $f$  is to consider the polynomial approximation to the exponential function given by the Jacobi-Anger expansion $^{26}$ ,

$$
\mathrm {e} ^ {- \mathrm {i} x t} = \cos (x t) - \mathrm {i} \sin (x t),
$$

$$
\cos (x t) = J _ {0} (t) + 2 \sum_ {k = 1} ^ {\infty} J _ {2 k} (t) T _ {2 k} (x), \tag {5}
$$

$$
\sin (x t) = 2 \sum_ {k = 1} ^ {\infty} J _ {2 k + 1} (t) T _ {2 k + 1} (x),
$$

where  $J_{i}(t)$  is a Bessel function of order  $i$ , and  $T_{i}(x)$  is a Chebyshev polynomial of order  $i$ . Tolerating an error  $\epsilon_{\mathrm{poly}}$ , the polynomial can be truncated at degree

$$
d = \Theta \left(t + \frac {\log \left(1 / \epsilon_ {\text {p o l y}}\right)}{\log \left(\mathrm {e} + \log \left(1 / \epsilon_ {\text {p o l y}}\right) / t\right)}\right), \tag {6}
$$

which is almost linear in  $t$  and logarithmic in  $1 / \epsilon_{\mathrm{poly}}$ . Here, we use the big-  $\Theta$  notation, i.e., for functions  $f$  and  $g$  we write  $f(x) = \Theta(g(x))$  if there exist constants  $c_1, c_2$ , and  $x_0$  such that  $c_1g(x) \leq f(x) \leq c_2g(x)$  for any  $x > x_0$ .

The goal is to apply this polynomial transformation to the eigenvalues of the Hamiltonian  $H$ . This is achieved by block encoding  $H$ , i.e., embedding  $H$  in a unitary operator  $\mathcal{W}(H)$  acting on a larger Hilbert space. A number of block-encoding methods have been proposed in the literature[10,27,31-33] and their applicability depends on the form of the Hamiltonian. For instance, one can employ the linear-combination-of-unitary (LCU) method when  $H$  is given as a weighted sum of unitary operators[34]. Then, by identifying a subspace analogous to a one-qubit space, the block-

encoding unitary  $\mathcal{W}(H)$  and a generalized rotation operator  $S(\phi)$  behave like the single-qubit operations  $W(x)$  and  $S(\phi)$  in Eq. (1).

Our aim is to run a small-scale QSP-based Hamiltonian simulation on a quantum computer with no fault-tolerance mechanism. This is challenging because noise limits the maximum depth of our circuits. We present a practical protocol to run the Hamiltonian simulation by QSP, while taking hardware noise into account.

# Preprocessing

Recall that QSP applies a polynomial transformation to the eigenvalues of the Hamiltonian. The eigenvalues need to be rescaled in a suitable interval so that the Hamiltonian can be encoded as a sub-block of a unitary operator. By unitarity, the largest possible interval in Eq. (4) is  $[-1, 1]$ . However, the protocol is made more efficient if we further narrow the interval down to  $[0, 1]$  and  $\sim e^{-ixt}$  by an even function of  $x^{35}$ . A general preprocessing method to rescale the spectrum of  $H$  in  $[a, b] \subseteq [0, 1]$  is given by

$$
\tilde {H} = \frac {(H - \lambda_ {-} I) (b - a)}{\lambda_ {+} - \lambda_ {-}} + a I, \tag {7}
$$

where  $\lambda_{+}$  and  $\lambda_{-}$  are upper and lower bounds on the eigenvalues, respectively (see Fig. 1A). To recover the desired time evolution, we counterbalance with a time rescaling

$$
\tilde {t} = \frac {t \left(\lambda_ {+} - \lambda_ {-}\right)}{b - a}. \tag {8}
$$

This yields the desired real-time evolution operator up to an irrelevant global phase:  $\mathrm{e}^{-\mathrm{i}tH} = \mathrm{e}^{-\mathrm{i}\phi}\mathrm{e}^{-\mathrm{i}tH}$ , where  $\phi = t(a\lambda_{+} - b\lambda_{-}) / (b - a)$ . The exact minimum  $\lambda_{\min}$  and maximum  $\lambda_{\max}$  eigenvalues are unknown and finding them is computationally intractable in general[36-38]. That is why we resort to bounds. Equation (8) shows that the effective evolution time  $\tilde{t}$  increases as the QSP interval  $[a,b]$  gets smaller, and as the eigenvalue bounds get looser. For example, suppose  $\lambda_{\pm}$  are taken such that  $(\lambda_{+} - \lambda_{\max}) / |\lambda_{\max}| = (\lambda_{\min} - \lambda_{-}) / |\lambda_{\min}| = r \geq 0$ , i.e., the bounds  $\lambda_{+/ - }$  are  $100r\%$  off from  $\lambda_{\max/\min}$ . From Eq. (8) we obtain

$$
\tilde {t} = \frac {t \left(\lambda_ {\max } - \lambda_ {\min }\right)}{b - a} + \frac {r t \left(\left| \lambda_ {\max } \right| + \left| \lambda_ {\min } \right|\right)}{b - a}. \tag {9}
$$

The first term is the smallest effective time achievable, while the second term is extra overhead. Note that  $\tilde{t}$  determines the polynomial degree  $d$  (e.g., Eq. (6) for the truncated Jacobi-Anger expansion), and thus the circuit depth.

When the Hamiltonian is provided as a weighted sum  $H = \sum_{k} c_{k} H_{k}$  of operators  $\{H_{k}\}$ , simple bounds are readily available:  $\lambda_{\pm} = \pm \sum_{k} |c_{k}| \| H_{k} \|$ , where  $\| \cdot \|$  is the spectral norm. Tighter bounds can be obtained by relaxing the ground-state constraints[39,40] and/or exploiting some structure in the Hamiltonian. For translation-invariant systems, the Anderson bound[41], and a particular semi-definite programme relaxation, can provide a lower bound with an error that is independent of system size[42]. Furthermore, for a large class of local Hamiltonians, one can formulate a hierarchy of semi-definite programming constraints with increasing complexity that can be solved numerically with tensor network and renormalization group techniques[43].

# Compressed block-encoding

The second key step of the protocol (Fig. 1B) is to input the Hamiltonian to the quantum computer so that it can be processed. For  $\epsilon_{\mathrm{BE}} \geq 0$ , a block-encoding  $\mathcal{W}$  of  $\tilde{H}$  is defined by

$$
\left\| \tilde {\mathcal {W}} - \tilde {H} \right\| _ {\mathrm {F}} = \epsilon_ {\mathrm {B E}}, \tag {10}
$$

$$
\tilde {\mathcal {W}} := \left(\left\langle 0 ^ {a} \right| \otimes I\right) \mathcal {W} \left(\left| 0 ^ {a} \right\rangle \otimes I\right),
$$

![](images/34f89b6d0d77ea1f32c60e77eb49d9f115274aa581fda6db13c44197792f1bc6.jpg)  
Fig. 1 The proposed protocol for the realization of QSP on a noisy quantum computer. We choose Hamiltonian simulation as the application. We start with a necessary preprocessing step (A) that maps the input parameters to an effective Hamiltonian  $\tilde{H}$  and an effective simulation time  $\tilde{t}$ . In step (B),  $\tilde{H}$  is embedded in a unitary operator. By classically optimizing/compiling a circuit  $\mathcal{W}$  this step produces a compressed version of a block-encoding circuit. Next, in the operator-function design (C), we approximate the real-time evolution function,  $\mathrm{e}^{-\mathrm{i}xt}$ , by a polynomial  $f(x)$  of degree  $d$ . While increasing the degree leads to a more accurate polynomial approximation, the computation suffers from larger noise effects. This is due to the growing depth of the QSP circuit, consisting of  $\mathcal{O}(d)$  primitive gates. By accounting for the error rate  $p_{\mathrm{TQ}}$  of two-qubit gates, we heuristically estimate the optimal degree yielding the smallest combined error. The processing step (D) finally realizes QSP using the compressed block-encoding circuit  $\mathcal{W}$  and the designed polynomial  $f(x)$ . Upon postselection on the ancilla's measurement outcomes, we obtain an approximation to the desired real-time evolution  $\mathrm{e}^{-\mathrm{i}Ht}$ . An error mitigation scheme based on the error rate  $p_{\mathrm{TQ}}$  further reduces the effect of noise on the output.

where  $\| \cdot \|_{\mathrm{F}}$  is the Frobenius norm and the integer  $a$  is the number of ancillary qubits. Note that  $(\langle 0^a |\otimes I)\cdot (|\bar{0}^a\rangle \otimes I)$  projects onto the subspace where the ancillary qubits are in the all-zero state. The accuracy of the block encoding is specified by the parameter  $\epsilon_{\mathrm{BE}}$ .

Depending on the form of  $\tilde{H}$ , there exist different block-encoding methods $^{10,27,31-34}$ . While such generic methods are scalable in principle, the required number of ancillary qubits and the circuit depth may preclude an implementation on current noisy quantum devices. Here, we propose two ways to overcome this by compressing the block-encoding circuit.

First, we use a parameterized quantum circuit  $\mathcal{W} = \mathcal{W}(\pmb{\theta})$  as ansatz and minimize Eq. (10) with respect to the parameters  $\pmb{\theta}$ . The possible presence of barren plateaus in the optimization landscape could prohibit quantum-classical hybrid methods from being efficient at larger system sizes[44-46]. In this case, a fully classical approach is preferable[47]. We thus suggest to use tensor network ansätze that can be efficiently optimized on a classical computer.

Second, we make use of multiplexor circuit compilation to compress the LCU block-encoding circuit $^{48,49}$ . The multiplexor compilation reduces the number of elementary gates required to implement sequential multi-controlled unitary operations which are heavily used in the LCU circuit. Since the compilation adopted here does not introduce approximation error, it provides an exact block-encoding, i.e.,  $\epsilon_{\mathrm{BE}} = 0$ .

In the Methods section we discuss both approaches in more detail.

# Operator-function design

The depth of a QSP circuit is proportional to the degree  $d$  of the polynomial. When using noisy devices, we must fix  $d$  so that the final circuit has a reasonable fidelity. Later on, we provide a heuristic to choose  $d$  as a function of  $\tilde{t}$  and hardware noise. For now, let us assume that  $d$  is fixed and proceed to the function design (Fig. 1C). Instead of using the Jacobi-Anger expansion, we numerically optimize the QSP angles  $\{\phi_k\}$ . The preprocessing step

has rescaled the eigenvalues of  $H$  in  $[a, b] \subseteq [0, 1]$ , so we restrict the optimization to that interval. Furthermore, we can utilize polynomials of even parity, i.e., QSP polynomials of even degree  $d$ . The resulting accuracy is

$$
\epsilon_ {\text {p o l y}} = \min  _ {\left\{\phi_ {k} \right\}} \max  _ {x \in [ a, b ]} \left| \langle 0 | U _ {\mathrm {Q S P}} (\left\{\phi_ {k} \right\}) | 0 \rangle - e ^ {- i x \tilde {t}} \right|. \tag {11}
$$

Figure 2a shows the accuracy for different values of degree and evolution time. For each value of  $d$ , we find the QSP angle sequence using a dedicated python package called pyqsp<sup>50</sup>. As expected, the error decreases as the degree gets larger for a given evolution time. It is also observed that the error increases as the evolution time gets longer for a fixed degree.

The error stemming from both block-encoding Eq. (10) and operator-function design Eq. (11) propagates to the accuracy of the whole algorithm. This is found by expanding the error as<sup>10,31</sup>,

$$
\begin{array}{l} \left\| \mathrm {e} ^ {- \mathrm {i} \tilde {t} \tilde {H}} - f (\tilde {\mathcal {W}}) \right\| \\ \leq \left\| e ^ {- i \tilde {t} \tilde {H}} - e ^ {- i \tilde {t} \tilde {\mathcal {W}}} \right\| + \left\| e ^ {- i \tilde {t} \tilde {\mathcal {W}}} - f (\tilde {\mathcal {W}}) \right\| \tag {12} \\ \leq | \tilde {t} | \| \tilde {H} - \tilde {\mathcal {W}} \| _ {\mathsf {F}} + \left\| e ^ {- i \tilde {t} \tilde {\mathcal {W}}} - f (\tilde {\mathcal {W}}) \right\| \\ = \left| \tilde {t} \right| \epsilon_ {\mathrm {B E}} + \epsilon_ {\mathrm {p o l y}} =: \epsilon_ {\mathrm {Q S P}}, \\ \end{array}
$$

where we have defined  $f(\tilde{\mathcal{W}}) \coloneqq \sum_{\lambda_{\tilde{\mathcal{W}}}} f(\lambda_{\tilde{\mathcal{W}}}) |\lambda_{\tilde{\mathcal{W}}} \rangle \langle \lambda_{\tilde{\mathcal{W}}} |$  with the eigenstates  $\{|\lambda_{\tilde{\mathcal{W}}} \rangle\}$  of  $\tilde{\mathcal{W}}$  such that  $\tilde{\mathcal{W}} |\lambda_{\tilde{\mathcal{W}}} \rangle = \lambda_{\tilde{\mathcal{W}}} |\lambda_{\tilde{\mathcal{W}}} \rangle$ . In the third line, we use inequality  $\| e^{-it\tilde{H}} - e^{-it\tilde{\mathcal{W}}} \| \leq |\tilde{t}| \| \tilde{H} - \tilde{\mathcal{W}} \|_F$  (see Lemma 50 in ref. 31, preprint version) and the fact that the spectral norm is upper bounded by the Frobenius norm.

Let us now incorporate the effect of hardware noise via a simple noise model. This allows us to develop a heuristic for estimating the optimal polynomial degree, given the evolution time and the noise rate of our quantum device. Letting  $|\psi_0\rangle$  be a  $n$ -qubit initial state and  $|0^a\rangle$  be the  $a$ -qubit ancillary state, the quantum

![](images/002c7e8d3d46fc520cbb0e30b9253ec772e8ede26ab2d0028c40a8a01fa8fa57.jpg)  
Fig. 2 Heuristic search of optimal parameters for the five-qubit hardware experiment. a Accuracy of QSP angle optimization, Eq. (11), using pyqsp<sup>50</sup>. b Upper bound to the infidelity, Eq. (16), as a function of degree  $d$  and evolution time  $Jt$ . c For each evolution time, the optimal degree  $d_{\mathrm{opt}}$  is the degree that minimizes the total error  $\epsilon_{\mathrm{total}}$  in  $\mathbf{b}$ .

computation is described by

$$
\sigma = \mathcal {U} _ {\mathrm {Q S P}} \left(\left| 0 ^ {a} \right\rangle \left\langle 0 ^ {a} \right| \otimes \left| \psi_ {0} \right\rangle \left\langle \psi_ {0} \right|\right) \mathcal {U} _ {\mathrm {Q S P}} ^ {\dagger}, \tag {13}
$$

where  $\mathcal{U}_{\mathrm{QSP}}$  represents the unitary implementing the QSP protocol, which will be defined later in Eq. (17). We model the noise effect of the hardware with the depolarizing channel  $\mathcal{D}_p$  acting on the entire system. It alters the state to

$$
\mathcal {D} _ {p} [ \sigma ] = (1 - p) \sigma + p \frac {I}{2 ^ {n + a}}, \tag {14}
$$

where we set  $p = 1 - (1 - p_{\mathrm{TQ}})^{N_{\mathrm{TQ}}}$  with the two-qubit gate infidelity  $p_{\mathrm{TQ}}$  and the number of two-qubit gates  $N_{\mathrm{TQ}}$  in the  $\mathcal{U}_{\mathrm{QSP}}$  circuit. The fidelity between this state and the ideal target state  $|\psi_t\rangle \coloneqq \mathrm{e}^{-\mathrm{i}\tilde{H} t}|\psi_0\rangle$  quantifies the error,

$$
\begin{array}{l} \left(\left\langle \mathbf {0} ^ {a} \right| \otimes \left\langle \psi_ {\tilde {t}} \right|\right) \mathcal {D} _ {p} [ \sigma ] \left(\left| \mathbf {0} ^ {a} \right\rangle \otimes \left| \psi_ {\tilde {t}} \right\rangle\right) \tag {15} \\ = (1 - p) \left| \langle \psi_ {t} | f (\tilde {\mathcal {W}}) | \psi_ {0} \rangle \right| ^ {2} + \frac {p}{2 ^ {n + \sigma}}, \\ \end{array}
$$

Thus, the corresponding infidelity is bounded as

$$
\begin{array}{l} 1 - \left(\left\langle 0 ^ {a} \right| \otimes \left\langle \psi_ {\hat {t}} \right|\right) \mathcal {D} _ {p} [ \sigma ] \left(| 0 ^ {a} \rangle \otimes | \psi_ {\hat {t}} \rangle\right) \\ = 1 - (1 - p) \left| \right. 1 - \left\langle \right. \psi_ {\tilde {t}} \left. \right|\left(e ^ {- i \tilde {H} \tilde {t}} - f (\tilde {\mathcal {W}})\right) \mid \psi_ {0} \left. \right\rangle\left. \right| ^ {2} - \frac {p}{2 ^ {n + a}} \tag {16} \\ \leq 1 - (1 - p) \left(1 - \epsilon_ {\mathrm {Q S P}}\right) ^ {2} - \frac {p}{2 ^ {n + a}} =: \epsilon_ {\text {t o t a l}}. \\ \end{array}
$$

Figure 2b shows the upper bound in Eq. (16) as a function of degree and evolution time, where the algorithmic error  $\epsilon_{\mathrm{QSP}}$  [Eq. (12)] is obtained for the Hamiltonian given in Eq. (23). The two-qubit gate error rate is set to  $p_{\mathrm{TQ}} = 2.577 \times 10^{-3}$  (see Methods for details) and the circuits of degree  $d \in \{2,4,6,8,10,12,14\}$  contain  $N_{\mathrm{TQ}} \in \{52,98,144,190,236,282,328\}$  two-qubit gates, respectively. In contrast to the operator-function design error in Fig. 2a, the total error in Fig. 2b has a sweet spot for each value of  $Jt$ . Intuitively, the increase of the degree reduces the algorithmic error  $\epsilon_{\mathrm{QSP}}$  while making the noise effect more prominent due to the larger circuit depth. This motivates the following heuristic: for a given evolution time, pick the degree that minimizes the upper bound on the total error Eq. (16) (see refs. [51,52], where a similar approach has been applied to Grover's algorithm). Importantly, this step of the protocol does not require the use of a quantum computer. The optimal degree for Eq. (16) is found numerically using classical computation. Additionally, the sweet spot may coincide with the hardware's optimal working point where we expect a classical simulation of the corresponding noisy quantum circuit to be most challenging [6,8], further justifying our heuristic choice.

Figure 2c shows that the optimal degree  $d_{\mathrm{opt}}$  is approximately linear in the evolution time  $t$ . The estimated degrees are corroborated by the complementary numerical study that we carried out and presented in the Methods section. It is important

to emphasize that our approximately linear scaling in time is different from the one expected by noiseless QSP. Our heuristic is designed to run the noisy quantum computer to its full potential, but may still produce large errors. This happens when the simulation parameters  $\{H,t,p_{\mathrm{TQ}}\}$  are not compatible in the first place. For instance, at a fixed error rate  $p_{\mathrm{TQ}}$  and large simulation time  $t$ , it is reasonable to expect a large infidelity. In contrast, Hamiltonian simulation by noiseless QSP achieves linear scaling in time while providing full control over the total error. For example, one can use a perfect block-encoding,  $\epsilon_{\mathrm{BE}} = 0$ , along with the desired approximation error  $\epsilon_{\mathrm{poly}}$  in Eq. (6).

# Processing

In this last step of the protocol, we apply the polynomial  $f$  found in Eq. (11) to the block-encoded Hamiltonian  $\tilde{\mathcal{W}}$  (Fig. 1D). For an even integer  $d$ , the QSP unitary takes the form<sup>10,11</sup>,

$$
\begin{array}{l} \mathcal {U} _ {\mathrm {Q S P}} := \prod_ {k = 1} ^ {d / 2} \left[ \mathcal {S} \left(\phi_ {2 k - 1}\right) \mathcal {W} ^ {\dagger} \mathcal {S} \left(\phi_ {2 k}\right) \mathcal {W} \right] \tag {17} \\ = \bigoplus_ {\lambda_ {\tilde {\mathcal {W}}}} \left( \begin{array}{c c} f (\lambda_ {\tilde {\mathcal {W}}}) & * \\ * & * \end{array} \right) \otimes \left| \lambda_ {\tilde {\mathcal {W}}} \right\rangle \langle \lambda_ {\tilde {\mathcal {W}}} | = \left( \begin{array}{c c} f (\tilde {\mathcal {W}}) & * \\ * & * \end{array} \right), \\ \end{array}
$$

$$
\mathcal {S} (\phi) := \bigoplus_ {\lambda_ {\tilde {\mathcal {W}}}} \left( \begin{array}{c c} \mathrm {e} ^ {\mathrm {i} \phi} & 0 \\ 0 & \mathrm {e} ^ {- \mathrm {i} \phi} \end{array} \right) \otimes \left| \lambda_ {\tilde {\mathcal {W}}} \right\rangle \left\langle \lambda_ {\tilde {\mathcal {W}}} \right|, \tag {18}
$$

where the direct sum is taken over the eigenstates  $\{\left|\lambda_{\tilde{\mathcal{W}}}\right\rangle \}$  of  $\tilde{\mathcal{W}}$  and the upper-left block of the matrices represents the  $|0^a\rangle \langle 0^a|$  component of the corresponding operators. Thus, starting from the initial ancillary state  $|0^{a}\rangle$ , and post-selecting on the ancillary state  $|0^{a}\rangle$  at the end, we obtain

$$
\left(\left\langle 0 ^ {a} \right| \otimes I\right) \mathcal {U} _ {\mathrm {Q S P}} \left(\left| 0 ^ {a} \right\rangle \otimes I\right) = f (\tilde {\mathcal {W}}), \tag {19}
$$

which approximates the desired real-time evolution operator  $\mathrm{e}^{-\mathrm{i}Ht}$ .

Let us now discuss how to post-process the measurement results and mitigate the noise effects on observables. We let the noisy quantum state simulated on the hardware before any measurement be  $\eta$ , which is generally different from the state affected only by the depolarizing channel given by Eq. (14). For simplicity, we consider the expectation value,  $\mathrm{Tr}[\overline{P}\eta]$ , of  $\overline{P} := |0^a\rangle \langle 0^a| \otimes P$ , where  $P$  is a Pauli operator acting on the system register. The variance is  $\mathrm{Var}_{\eta,\overline{P}} = \mathrm{Tr}[\overline{I}\eta] - \mathrm{Tr}[\overline{P}\eta]^2$ . We mitigate the noise effects by modelling it with the depolarizing channel[53-55]. In particular, we use the same noise model that we previously employed when estimating the optimal polynomial degree. The expectation value of  $\overline{P}$  with respect to the state in Eq. (14) is

$$
\operatorname {T r} \left[ \bar {P} \mathcal {D} _ {p} [ \sigma ] \right] = (1 - p) \langle \psi_ {0} | f (\tilde {\mathcal {W}}) ^ {\dagger} P f (\tilde {\mathcal {W}}) | \psi_ {0} \rangle . \tag {20}
$$

where  $p = 1 - (1 - p_{\mathrm{TQ}})^{N_{\mathrm{TQ}}}$ . We infer the noiseless expectation value from the noisy expectation value as

$$
\langle \bar {P} \rangle_ {\eta} ^ {\text {m i t i g}} := \frac {\operatorname {T r} [ \bar {P} \eta ]}{1 - p}. \tag {21}
$$

This is understood as mitigating the depolarizing noise, at the cost of a larger variance,

$$
\operatorname {V a r} _ {\eta , \bar {P}} ^ {\text {m i t i g}} = \frac {\operatorname {V a r} _ {\eta , \bar {P}}}{(1 - p) ^ {2}} = \frac {\operatorname {V a r} _ {\eta , \bar {P}}}{(1 - p _ {\mathrm {T Q}}) ^ {2 N _ {\mathrm {T Q}}}}. \tag {22}
$$

This implies that the number of samples needed to achieve a fixed sampling error increases exponentially in  $N_{\mathrm{TQ}}$ . Therefore, reducing the depth of the circuit is extremely important even though the noise effect on the expectation value  $\langle \overline{P} \rangle_{\eta}^{\mathrm{mitig}}$  is mitigated.

# Hardware experiment

In order to demonstrate the protocol, we perform the QSP-based Hamiltonian simulation experiments on the Quantumum H1-1 trapped-ion quantum computer. We simulate the real-time dynamics of the quantum system described by the one-dimensional Ising spin Hamiltonian

$$
H = - J \sum_ {i = 0} ^ {n - 2} Z _ {i} Z _ {i + 1} - \sum_ {i = 0} ^ {n - 1} h _ {i} X _ {i} - m \sum_ {i = 0} ^ {n - 1} Z _ {i}, \tag {23}
$$

We quantify entanglement growth by bi-partitioning the system into subsystems  $A$  and  $\overline{A}$  and then computing the time dependence of the von Neumann entropy

$$
S _ {\mathrm {v N}} = - \operatorname {T r} \left[ \rho_ {A} \log \rho_ {A} \right], \tag {24}
$$

and the degree-2 Renyi entropy

$$
S _ {R} ^ {(2)} = - \log \operatorname {T r} \left[ \rho_ {A} ^ {2} \right] \tag {25}
$$

on the  $n_A$ -qubit subsystem  $A$ , where  $\rho_A = \mathrm{Tr}_{\bar{A}}[\rho]$ .

We perform state tomography by measuring the Pauli expectation values via

$$
c _ {P} = \frac {\left\langle \bar {P} \right\rangle_ {\eta} ^ {\text {m i t i g}}}{\left\langle \bar {I} \right\rangle_ {\eta} ^ {\text {m i t i g}}}, \tag {26}
$$

for an operator  $P \in \operatorname{Pauli}_A := \{I, X, Y, Z\}^{\otimes n_A} \backslash \{I^{\otimes n_A}\}$  on  $A$  (see Methods), which leads to an estimator of the density matrix,

$$
\rho_ {A} = \frac {I + \sum_ {P \in P a u l i _ {A}} c _ {P} P}{2 ^ {n _ {A}}}. \tag {27}
$$

Since the denominator of Eq. (26) would be one in the absence of algorithmic error and noise effects, the quantity in Eq. (26) approximates the expectation value of the Pauli operator  $P$  as is further discussed in the Methods section. We note that the computation of von Neumann entropy is not scalable in general. However, the current procedure can be straightforwardly applied to the computation of degree-2 Rényi entropy using the swap trick $^{56-61}$  or randomized measurement protocols $^{62-67}$ .

The H1-1 system operates by controlling the  $S_{1/2}$  hyperfine clock states of trapped  $^{171}\mathrm{Yb}^+$  ions, which play the role of qubits $^{68,69}$ ; there are a total of 20 qubits in the system at the time the experiments are conducted (see ref.  ${}^{70}$  for details on the H1-1 system). In addition to single-qubit rotations, a two-qubit native gate  $\exp(-\mathrm{i}\theta Z \otimes Z / 2)$  with  $\theta \in \mathbb{R}$  can be applied to an arbitrary pair of qubits giving the system all-to-all connectivity. This is enabled by the ability of the H1-1 system to move any pair of ions to one of five isolated interaction zones where quantum operations (initialization, gate application, measurement) are executed in a manner that suppresses the rate of crosstalk and allows for high-fidelity two-qubit gates.

![](images/7655ce9b050a9acddc47c5c80a673d65af6bbe8298c0d9a453c41b8167bf05af.jpg)

![](images/1f1bf0fdfe24eeb81b314655361edbdc93086c8fa5f734ef9318d8f9add2cbeb.jpg)  
Fig. 3 Sketch of the setup for the five-qubit experiment. a The system consists of the two-qubit ancillary register (orange ions) and the three-qubit system register. The latter is further partitioned into the one-qubit subsystem A (a red ion) and its complement  $\overline{A}$  (blue ions). b The H1-1 quantum computer operates by manipulating the ions representing the qubits. Each quantum operation (initialization, gate application, measurement) is performed using lasers after the target ions are transported to one of the isolated interaction zones. In the experiments we use five out of the 20 qubits available, and apply up to 328 two-qubit gates.

In the first experiment, we consider the  $n = 3$  Ising spin chain with  $h_{i} / J = -1.05$  for all  $i$  and  $m / J = 0.5$  in Eq. (23). The system is known to display rapid growth of entanglement $^{71,72}$ . We preprocess the Hamiltonian  $H$  given in Eq. (23) to find  $\tilde{H}$  via Eq. (7) with  $a = 0$ ,  $b = 1$ , and  $\lambda_{\pm} = \pm (2J + 3h + 3m)$ . We obtain a compressed block-encoding circuit by variational optimization using two ancillary qubits and  $L = 3$  layers obtaining an error  $\epsilon_{\mathrm{BE}} = 1.8\times 10^{-2}$  (see Methods for details). The subsystem  $A$  is taken to be the zeroth site of the system register (see Fig. 3 for a schematic of this five-qubit experiment).

We consider the real-time evolution with  $Jt \in \{0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7\}$  and starting from the initial state on the system register  $|\psi_0\rangle = |+ \rangle^{\otimes 3}$  where  $|+ \rangle = (|0\rangle + |1\rangle) / \sqrt{2}$ . For each evolution time, the degree  $d$  is set to  $d_{\mathrm{opt}} \in \{0, 4, 4, 6, 8, 10, 10, 14\}$  following the heuristic shown in Fig. 2c. The resulting number of two-qubit gates in each circuit is  $N_{\mathrm{TQ}} \in \{0, 98, 98, 144, 190, 236, 236, 328\}$ . Error-mitigated Pauli expectation values in Eq. (26) are obtained from Eq. (21) with the two-qubit gate infidelity  $p_{\mathrm{TQ}} = 2.577 \times 10^{-3}$ , the number of two-qubit gates  $N_{\mathrm{TQ}}$ , and 1000 measurements.

Figure 4a, b show the growth of entanglement entropies with time for our system. The exact time evolution data (dashed line) is obtained from the exact application of the operator  $\mathrm{e}^{-\mathrm{i}Ht}$  to the initial state  $|\psi_0\rangle$ . The experimental data obtained from H1-1 is reported with error mitigation (orange circles) as well as without error mitigation (green squares). The noiseless QSP simulation data (blue diamonds) is obtained by classically simulating the algorithm without the noise effects. Error bars represent one standard deviation due to sampling error.

The error-mitigated experimental data agree well with the exact values and with the noiseless data up to  $Jt = 0.6$ , while there is a discrepancy between the unmitigated data and the rest from as early as  $Jt = 0.1$ . We also observe that the error-mitigated data show larger sampling errors (error bars) than the unmitigated data as expected from Eq. (22). The experimentally obtained entanglement entropies generally yield larger values than the exact ones due to algorithmic error and noise effects, which induce the

![](images/0906d9e0fd3966742a59288234f840f94464c6eea4a2426e529ac120ca565b44.jpg)

![](images/914e7ec76622cec3e1c9521bbb6469094b3a8229b8571c8650d72e344c9718eb.jpg)

![](images/b0491e98179451a3d13c925451859b0022c5855bd645234f279e16241dcee510.jpg)

![](images/f307f9a781dd99635913a480a44a2f01708d17c254d2bcd34a8dd8f967c72b30.jpg)  
Fig. 4 Experimental results. a The von Neumann entanglement entropy and b the degree-2 Rényi entanglement entropy of the five-qubit experiment on the H1-1 quantum computer. c The von Neumann entanglement entropy and d the degree-2 Rényi entanglement entropy of the seven-qubit experiment. Error bars represent one standard deviation due to sampling error.

![](images/e0fd58562cae387c94b6b16c659bc329dacf936b0a50856172da9bb003929abd.jpg)

interaction among the system register, ancillary register, and environment surrounding the device. Thus, the von Neumann and Rényi entropies computed on the subsystem  $A$  measure the entanglement not only with the system  $\overline{A}$  but also with the ancillary register and environment. Nevertheless, our protocol mitigates these erroneous impacts well. In particular, the agreement between the mitigated experimental data and exact values indicates that our protocol brings both QSP algorithmic error and noise effects under good control for the range of parameters that we assessed.

In the second experiment, we simulate the real-time evolution of the  $n = 4$  Ising spin chain with  $h_1 / J = 1$  and  $h_i / J = m / J = 0$  for  $i \neq 1$  in Eq. (23). We begin by constructing the exact LCU block-encoding circuit  $(\epsilon_{\mathrm{BE}} = 0)$  which uses  $a = 3$  ancillary qubits and 125 two-qubit gates. We compress this circuit using multiplexor compilation and obtain an equivalent circuit with only 44 two-qubit gates. This is a reduction of  $64.8\%$  of the original LCU circuit size (see Methods for details). We evolve the initial state  $|\psi_0\rangle = |+ \rangle^{\otimes 4}$  on the system register and make 1000 measurements to compute each Pauli expectation value [Eq. (26)] at each time  $Jt \in \{0.1, 0.4, 0.7\}$ . We again follow the heuristic in Fig. 1C to find  $d_{\mathrm{opt}} \in \{2, 4, 8\}$  for each evolution time  $Jt$ . However, we use a different two-qubit gate infidelity,  $p_{\mathrm{TQ}} = 2.185 \times 10^{-3}$ , following an update to the H1-1 device after our first experiment. The resulting number of two-qubit gates in each circuit is  $N_{\mathrm{TQ}} \in \{102, 204, 408\}$ .

We choose the zeroth and first sites of the system register to represent subsystem  $A$ . The calculated entanglement entropies are shown in Fig. 4c, d. The discrepancy between the noiseless data (blue diamonds) and exact data (dashed line) is due to the degrees  $d_{\mathrm{opt}}$  being smaller than those found in the first experiment. Indeed, the heuristic has taken into account the increased number of qubits and two-qubit gates for this second experiment. The degrees found by our heuristic lead to a good agreement between the noiseless data and error-mitigated experimental data (orange circles), except for  $Jt = 0.7$ . Note that this parameter setting ( $Jt = 0.7$ ) yields our largest quantum

circuit with as many as 408 two-qubit gates. This experiment exemplifies the importance of finding the optimal working point to balance the algorithmic error, hardware noise, and parameter setting.

# DISCUSSION

We propose a detailed protocol to perform QSP-based Hamiltonian simulation tailored to noisy quantum hardware. Each process is carefully studied to clarify the sources of error in the estimate of target observables, as summarized in Tab. 1. In particular, the polynomial approximation is designed such that the combined error caused by the QSP protocol and noise effect is minimized. The block-encoding circuit is compressed to further reduce the circuit depth for experimental purposes. An error mitigation scheme is used to increase accuracy in the estimate of target expectation values.

We execute the protocol on the Quantumium H1-1 quantum computer. As an illustration, the time evolution of von Neumann and degree-2 Rényi entanglement entropies are computed. The results from the hardware experiments agree not only with those from noiseless simulations but with exactly obtained values, which implies the algorithmic error and noise effects are well controlled in the range of parameters that we chose.

An important question is whether the approach can scale to larger demonstrations. Both our heuristic and error mitigation schemes are derived under a simple noise model for the hardware at hand. A sophisticated error model may be required to obtain more accurate outputs for larger instances. Beyond that, one can use quantum error detection codes (see, e.g., ref. [73] for the code tailored for the Quantumum H1 system) to generate more reliable results at the cost of discarding a portion of the circuit runs, or apply algorithm-level error correction [74] for noisy QSP. Finally, it is noted that there exist block-encoding schemes with asymptotically efficient scaling [10,27,31-33]. Their required quantum resources are, however, still beyond the capability of currently available quantum devices. The techniques employed in this article to

Table 1. Summary of the main sources of error in our QSP protocol and how they can be improved upon.  

<table><tr><td>Step</td><td>Description of the error</td><td>Possible improvements</td></tr><tr><td>Preprocessing</td><td>The spectrum of the Hamiltonian is rescaled using crude upper and lower bounds. This leads to a longer effective evolution time t in Eq. (9).</td><td>T tighter bounds on the spectrum, e.g., using the methods in refs. 39-43.</td></tr><tr><td>Compressed block-encoding</td><td>Imperfect block-encoding if variational optimization of circuit parameters is used. This leads to an error εBE in Eq. (12).</td><td>A more expressive circuit ansatz and a higher performance classical optimizer/compiler, e.g., using the methods in ref. 24.</td></tr><tr><td>Operator-function design</td><td>The real-time evolution operator is approximated by a polynomial of fixed degree. This leads to an error εpoly in Eq. (12).</td><td>A higher degree of the polynomial, e.g., using methods in refs. 79-81.</td></tr><tr><td>Processing</td><td>Each two-qubit gate fails with some probability pTQ. This leads to a reduced fidelity in Eq. (15).</td><td>Quantum error detection, e.g., using the method in ref. 73.</td></tr><tr><td colspan="3">Note, improving upon some errors affects the other errors in non-trivial ways.</td></tr></table>

![](images/bb5173f03c98dd34242699ab29be0ddfa16853720ec630eb3020ca59f65f1254.jpg)

![](images/5ec027b6d7af085056b5749b67542b8a880fad19d595f15b7b8d891f727e7c63.jpg)  
Fig. 5 Quantum circuit diagrams for compressed block-encoding by variational optimization. (Left) An example of  $(a + n)$ -qubit parameterized quantum circuit  $\mathcal{W}(\theta)$  satisfying the qubitization condition. (Right) An example of sub-circuit  $V(\theta)$ . The circuit inside the dashed box is repeated  $L$  times with new variational parameters added for each layer. The single- and two-qubit gates used in the circuit are  $R(\theta) = \exp(-\mathrm{i}\theta^{(3)}X/2)$ ,  $\exp(-\mathrm{i}\theta^{(2)}Z/2)$ ,  $\exp(-\mathrm{i}\theta^{(1)}X/2)$ , and  $R_{ZZ}(\theta) = \exp(-\mathrm{i}\theta Z \otimes Z/2)$ . In our five-qubit experiment, we use the bottom  $n(= 3)$  qubits as the system register and the top  $a(= 2)$  qubits as the ancillary register.

compress block-encoding circuits are potentially useful to perform larger-scale QSP realizations.

While further theoretical improvements are still required to scale up the protocol, the present study has taken the first step in the experimental realization of QSP-based algorithms and applications.

# METHODS

# Compressed block-encoding by variational optimization

Here we elaborate on the block-encoding techniques used in this work. The goal is to optimize a parameterized quantum circuit,  $\mathcal{W}(\pmb{\theta})$ , to minimize the block-encoding error,

$$
\epsilon_ {\mathrm {B E}} = \left\| \tilde {\mathcal {W}} (\boldsymbol {\theta}) - \tilde {H} \right\| _ {\mathrm {F}}, \tag {28}
$$

$$
\tilde {\mathcal {W}} (\boldsymbol {\theta}) = \left(\left\langle 0 ^ {a} \right| \otimes I ^ {\otimes n}\right) \mathcal {W} (\boldsymbol {\theta}) \left(\left| 0 ^ {a} \right\rangle \otimes I ^ {\otimes n}\right),
$$

with  $\theta$  referring to the collection of all the parameters in the circuit. This is equivalent to minimizing the cost function,

$$
F (\boldsymbol {\theta}) = \operatorname {T r} \left(\tilde {\mathcal {W}} ^ {\dagger} \tilde {\mathcal {W}}\right) - 2 \operatorname {R e T r} (\tilde {H} \tilde {\mathcal {W}}), \tag {29}
$$

where we used that  $\tilde{H}$  is a Hermitian operator. Provided that the Hamiltonian is expanded as  $\tilde{H} = \sum_{\ell}c_{\ell}P_{\ell}$  with  $n$  -qubit Pauli operators  $\{P_{\ell}\}_{\ell}$ , the error  $\epsilon_{\mathrm{BE}}$  is obtained from  $F(\pmb{\theta})$  by

$$
\left(\epsilon_ {\mathrm {B E}}\right) ^ {2} = F (\boldsymbol {\theta}) - \operatorname {T r} \left(\tilde {H} ^ {2}\right) = F (\boldsymbol {\theta}) - 2 ^ {n} \sum_ {\ell} c _ {\ell} ^ {2}. \tag {30}
$$

We consider a particular structure for the parameterized quantum circuit which satisfies the reflection condition  $\mathcal{W}(\pmb{\theta})^2 = I^{\otimes n}$ . This condition is not crucial to the construction of

QSP. However, we empirically found that the constraint makes optimization of block encoding easier. One ansatz satisfying the reflection condition is shown in Fig. 5 and given by

$$
\mathcal {W} (\boldsymbol {\theta}) = V (\boldsymbol {\theta}) \bar {C Z} V (\boldsymbol {\theta}) ^ {\dagger}, \tag {31}
$$

where  $V(\theta)$  is a unitary operator specified by the right circuit of Fig. 5, and  $\overline{CZ}$  stands for the sequential application of controlled-Z gates that is shown in the middle of the upper circuit.

The parameterized quantum circuit  $\mathcal{W}(\pmb{\theta})$  shown in Fig. 5 is composed of the following gates:

$$
R _ {X} (\theta) = \exp (- \mathrm {i} \theta X / 2),
$$

$$
R _ {Z} (\theta) = \exp (- \mathrm {i} \theta Z / 2), \tag {32}
$$

$$
R _ {Z Z} (\theta) = \exp (- i \theta Z \otimes Z / 2),
$$

where each gate has an independent variational parameter  $\theta$ . Importantly, these gates are part of the native gate set of the Quantumum H1-1 quantum computer.

In the present work, the optimization of the block-encoding circuit is performed by minimizing the cost function given in Eq. (29) using a classical state-vector simulation and the quasiNewton BFGS method<sup>75</sup>. The optimization is stopped when the gradient norm of the cost function falls below the threshold value  $1 \times 10^{-5}$ . The accuracies of the optimized block encoding circuits for the 3-site and 4-site Ising spin Hamiltonian are shown in Fig. 6. In the experiment of the 3-site Ising spin chain, we use the circuit with  $a = 2$  and  $L = 3$ , which requires  $(a + n - 1)(2L + 1) = 28R_{ZZ}$  gates. The optimized circuit has block-encoding error  $\epsilon_{\mathrm{BE}} = 1.8 \times 10^{-2}$ .

We briefly discuss a classical method based on tensor network techniques. By expressing the cost function [Eq. (29)] as a tensor

![](images/71567ad5fec3e77fb2c5032e0c32981c2696df9efad606f429a90c2917bab998.jpg)

![](images/f0737a9a3b6967a698fb0ec21c1836d5360f10c1e0b2f81c64d4a74a2e3b19da.jpg)  
Fig. 6 Error  $\epsilon_{\mathrm{BE}}$  of the block encoding circuit as a function of the number of layers  $L$  and for each number of ancillary qubits  $a$ . We use the Ising spin Hamiltonian with  $h_i / J = -1.05$  for all  $i$  and  $m / J = 0.5$ . The system size  $n$  is three in a and four in b.

![](images/635a082dde9e849f735c1645caaef8eb43db8446a7dfc1d7fd912b09994f76c8.jpg)

![](images/1a842a02a10d5ad7bd8e19f5da97156feac37f425b7d31b0e44785613d830bd0.jpg)

![](images/0a6af055f51a05a975f3c6cbbde083dc290673b474b7dec761771182365458f6.jpg)

![](images/7d11c53f57fd0444e00a95a2b6e0a67ca424b392c18660358f67ea3cfe95101e.jpg)

![](images/f4271f9d3bb28376c890d7ecfe38ba2f01eb52308bb3224ee3dd78765e631468.jpg)  
Fig. 7 Tensor network contractions for the evaluation of the cost function. a Contraction of  $\mathrm{Tr}(\tilde{\mathcal{W}}^{\dagger}\tilde{\mathcal{W}})$  for  $\tilde{\mathcal{W}}$  of Fig. 5a. b Contraction of  $\mathrm{Tr}(\tilde{\mathcal{W}}^{\dagger}\tilde{H})$  for  $\tilde{\mathcal{W}}$  of Fig. 5a and  $\tilde{H}$  represented by a matrix product operator. Note that the terms in the gradient (34) and Hessian (35) can be evaluated using similar tensor network contractions.

network contraction and using a classical optimizer to find the parameters  $\pmb{\theta}$ , a block-encoding circuit  $\mathcal{W}(\pmb{\theta})$  which minimizes  $\epsilon_{\mathrm{BE}}$  can be found. The terms in the cost function Eq. (29),  $\operatorname{Tr}(\tilde{\mathcal{W}}^{\dagger}\tilde{\mathcal{W}})$  and  $\operatorname{Tr}(\tilde{H}\tilde{\mathcal{W}})$ , can be evaluated using tensor network contractions as illustrated in Fig. 7.

The cost function in Eq. (29) can be variationally optimized using a classical optimizer, for instance, we can employ a gradient-based method as follows. At each iteration  $i$ , we require the

gradient vector  $\mathcal{G}^{(i)}$  of the objective function  $F(\pmb{\theta})$  at  $\pmb{\theta} = \pmb{\theta}^{(i)}$ :

$$
\mathcal {G} _ {k} ^ {(i)} = \frac {\partial F}{\partial \theta_ {k}} = 2 \operatorname {R e} \left[ \operatorname {T r} \left(\tilde {\mathcal {W}} ^ {\dagger} \frac {\partial \tilde {\mathcal {W}}}{\partial \theta_ {k}}\right) \right] - 2 \operatorname {R e} \left[ \operatorname {T r} \left(\tilde {H} \frac {\partial \tilde {\mathcal {W}}}{\partial \theta_ {k}}\right) \right]. \tag {33}
$$

The partial derivatives in each gradient are straightforward to compute via the first of the variational gates given in Eq. (32).

We then iterate

$$
\boldsymbol {\theta} ^ {(i + 1)} = \boldsymbol {\theta} ^ {(i)} - \gamma \mathcal {G} ^ {(i)}, \tag {34}
$$

with some learning parameter  $\gamma > 0$  to update the parameters. The iteration is repeated until the norm of the vector of gradients falls below a predefined convergence threshold.

One could improve the convergence rate by additionally computing the Hessian matrix  $\mathcal{H}^{(i)}$  at the cost of more evaluations of operator expectation values:

$$
\mathcal {H} _ {j, k} ^ {(i)} = \frac {\partial^ {2} F}{\partial \theta_ {j} \partial \theta_ {k}} = 2 \operatorname {R e} \left[ \operatorname {T r} \left(\tilde {\mathcal {W}} ^ {\dagger} \frac {\partial^ {2} \tilde {\mathcal {W}}}{\partial \theta_ {j} \partial \theta_ {k}}\right) \right] + 2 \operatorname {T r} \left(\frac {\partial \tilde {\mathcal {W}} ^ {\dagger}}{\partial \theta_ {j}} \frac {\partial \tilde {\mathcal {W}}}{\partial \theta_ {k}}\right) - 2 \operatorname {R e} \left[ \operatorname {T r} \left(\tilde {H} \frac {\partial^ {2} \tilde {\mathcal {W}}}{\partial \theta_ {j} \partial \theta_ {k}}\right) \right]. \tag {35}
$$

Then, the parameter update in Eq. (34) is replaced with,

$$
\boldsymbol {\theta} ^ {(i + 1)} = \boldsymbol {\theta} ^ {(i)} - \left(\mathcal {H} ^ {(i)}\right) ^ {- 1} \mathcal {G} ^ {(i)}. \tag {36}
$$

For the computation of the inverse of the Hessian matrix, we use the fact that this matrix is Hermitian and since our goal is to minimize the objective function in Eq. (29), we are only interested in its positive eigenvalues.

Therefore we compute the pseudo-inverse via the eigendecomposition of the Hessian matrix and set all eigenvalues  $\mu_{k}$  smaller than some small cutoff  $\epsilon$  to zero, e.g.,  $\epsilon = 1\times 10^{-5}$ . More specifically, the pseudo-inverse is computed by replacing  $\mu_{k}$  by  $1 / \mu_{k}$  in the diagonal matrix of the eigendecomposition using only the positive eigenvalues  $\mu_{k}\geq \epsilon$  (all other eigenvalues are set to zero).

# Compressed block-encoding by multiplexor compilation

As an alternative approach to compressing a block-encoding circuit, we employ the linear-combination-of-unitaries (LCU) method<sup>34</sup> with the help of an efficient compilation of multi-controlled unitary gates (multiplexors). LCU provides a way to block encode  $\tilde{H}$  when it is expressed as a weighted sum of unitary operators,  $\{P_{\ell}\}_{\ell = 1}^{K}$ ,  $\tilde{H} = \sum_{\ell} c_{\ell} P_{\ell}$ . The LCU consists of two unitary operators:

1. an operator  $A$  acting on the ancillary register with  $a = \lceil \log_2K\rceil$  such that  $A|0^{a}\rangle = \frac{1}{\sqrt{c}}\sum_{\ell}\sqrt{c_{\ell}} |\ell \rangle$  with  $c = \Sigma_{\ell}c_{\ell}$ ; and  
2. a controlled operator  $B = \sum_{\ell}\mathrm{sign}(c_{\ell})|\ell \rangle \langle \ell |\otimes P_{\ell}$  with the sign function,  $\mathrm{sign}(c) = +1(-1)$  for  $c\geq 0(c <   0)$

With these,

$$
\mathcal {W} = A ^ {\dagger} B A \tag {37}
$$

givestheexactblockencodingof  $\tilde{H}$  ,i.e.,  $\epsilon_{\mathrm{BE}} = 0$

The bottleneck of this construction is the implementation of  $B$ , which contains a sequential application of multi-controlled- $P_{\ell}$  gates. We make use of the compilation technique of multiplexor, which is developed in[49] based on[76,77], to reduce the gate

complexity without introducing extra ancillary qubits. In the block-encoding of  $\tilde{H}$ , we use  $A = \mathrm{Had}^{\otimes 3}$  with the Hadamard gate, Had, and apply the multiplexor compilation to  $B$  shown in the right panel of Fig. 8. This results in 44  $R_{ZZ}$  gates for the block-encoding circuit  $\mathcal{W}$ . Indeed, the number of  $R_{ZZ}$  gates is significantly reduced relative to the circuit obtained without the compilation, which uses 125  $R_{ZZ}$  gates.

# Heuristic estimation of the optimal degree

One key aspect of this work is the estimation of the optimal degree for the QSP polynomial given a certain noise rate. Our heuristic uses the upper bound  $\epsilon_{\mathrm{total}}$  on the infidelity between the noisy and target states under a simplified noise model. Here we discuss the noise model and provide further numerical results.

For our numerical study, we replace all the two-qubit gates,  $R_{ZZ}(\theta) = \exp(-\mathrm{i}\theta Z \otimes Z / 2)$  for  $\theta \in \mathbb{R}$ , by two-qubit depolarizing channels:

$$
R _ {Z Z} (\theta) \sigma R _ {Z Z} (\theta) ^ {\dagger} \mapsto (1 - p _ {2}) R _ {Z Z} (\theta) \sigma R _ {Z Z} (\theta) ^ {\dagger} + \frac {p _ {2}}{1 5} \sum_ {P \in \{I, X, Y, Z \} ^ {\otimes 2} \backslash \{I ^ {\otimes 2} \}} P \sigma P, \tag {38}
$$

where  $\sigma$  is some quantum state and we use the error parameter  $p_2 = 2.416 \times 10^{-3}$ . This value is the two-qubit fault probability reported in the System Model H1 Emulator Product Data Sheet<sup>70</sup>. In particular, in the System Model H1-1 Emulator, the probability  $p_2$  is chosen such that the faulty  $R_{ZZ}(\pi / 2)$  modelled by the following two-qubit depolarizing channel  $D^{(2)}$  combined with the other noise channels emulates the noise of Quantumum H1-1 quantum computer:

$$
\begin{array}{l} D ^ {(2)} [ \sigma ] = (1 - p _ {2}) R _ {Z Z} (\pi / 2) \sigma R _ {Z Z} (\pi / 2) ^ {\dagger} + \frac {p _ {2}}{1 5} \sum_ {P \in \{I, X, Y, Z \} ^ {\otimes 2} \backslash \{I ^ {\otimes 2} \}} P \sigma P \\ = \left(1 - \frac {1 6 p _ {2}}{1 5}\right) \sigma + \frac {1 6 p _ {2}}{1 5} \operatorname {T r} ^ {(2)} [ \sigma ] \otimes \frac {l ^ {\otimes 2}}{4}, \tag {39} \\ \end{array}
$$

where  $\mathrm{Tr}^{(2)}$  indicates the trace over the two-dimensional subspace which the channel  $D^{(2)}$  acts on. We remark that, in the H1-1 Emulator, the faulty  $R_{ZZ}(\theta)$  is modelled by the channel  $D^{(2)}$  with  $\theta$ -dependent fault probability  $p_2(\theta)$  (see ref. 70 for more details). In the present work, we simplify the noise model by using  $p_2 = 2.416 \times 10^{-3}$  for all the two-qubit gates,  $R_{ZZ}(\theta)$ , independent of the angle  $\theta$  as given by Eq. (38). To clarify the relation between this parameter and the error parameter  $p_{\mathrm{TQ}}$  used throughout our protocol (see Fig. 1), we note that the same channel  $D^{(2)}$  is expressed as

$$
D ^ {(2)} [ \sigma ] = (1 - p _ {\mathrm {T Q}}) \sigma + p _ {\mathrm {T Q}} \operatorname {T r} ^ {(2)} [ \sigma ] \otimes \frac {I ^ {\otimes 2}}{4}. \tag {40}
$$

Therefore, the new error parameter is identified with  $p_{\mathrm{TQ}} = (16 / 15)$ ,  $p_2 = (16 / 15)2.416 \times 10^{-3} = 2.577 \times 10^{-3}$ . This is the error parameter used in our infidelity bound.

![](images/e6862ea051505a7d30d19d18adbdbb10c4af8a2c6fee9c9e133c8505cfedfd09.jpg)  
Fig. 8 Quantum circuit diagrams for compressed block-encoding by multiplexor compilation. (Left) Structure of the LCU-based block encoding  $\mathcal{W}$  given by Eq. (37). The top three and bottom four qubits represent the ancillary and system registers, respectively. (Right) The sub-circuit  $B$  used for block-encoding the  $n = 4$  Ising spin Hamiltonian with  $h_1 / J = 1$  and  $h_i / J = m / J = 0$  for  $i\neq 1$ , before the multiplexor compilation is applied.

![](images/92cdaf39af8e7525aab732b318c24c2c6f08aa9698222d857eeda6fbe61c8f4a.jpg)

![](images/41c56685b79509d7707e4703d582f958a7292135bf5422cb278a892eb274f194.jpg)  
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

![](images/62bd5224394066bf2aac38ee4c96a6315508ed0c42b3f31838d437cb13aa2c33.jpg)  
Fig. 9 Numerical verification of the indelity bound used in this work. a The upper bound of the infidelity between the target and simulated states. b The infidelity between the target state and simulated state with the noise model in Eq. (38). The locations of minima in a and b are close to each other for each time  $Jt$ .

To strengthen our argument, we verify the infidelity bound using exact density matrix emulations of noisy quantum circuits. We let the density matrix numerically obtained by the QSP protocol with the noise channel (38) be  $\eta_{\mathrm{sim}}$ . Figure 9a shows the infidelity bound, while Fig. 9b shows the exact infidelity. It is seen that the locations of minima in Fig. 9a, b are close to each other for each evolution time  $Jt$ . This observation supports that the degree  $d$  minimizing  $\epsilon_{\mathrm{total}}$  is likely to lead to the smallest possible error on noisy hardware. We emphasize that our heuristic does not require the use of a quantum computer beforehand. The optimal degree is found numerically using classical computation.

# Processing with depolarizing error mitigation

In our hardware experiment we employed state tomography to compute the entanglement entropies. To this end, we estimated the expectation value of a Pauli operator  $P$  on the system register by

$$
\frac {\left\langle \bar {P} \right\rangle_ {\eta} ^ {\text {m i t i g}}}{\left\langle \bar {l} \right\rangle_ {\eta} ^ {\text {m i t i g}}}. \tag {41}
$$

This is understood as taking the expectation of  $P$  with the normalized post-selected state. Given an initial quantum state  $|\psi_0\rangle$  on the system register, we wish to approximate the time-evolved state  $\mathrm{e}^{-\mathrm{i}Ht}|\psi_0\rangle \langle \psi_0|\mathrm{e}^{\mathrm{i}Ht}$  by applying the QSP unitary

$$
\sigma = \mathcal {U} _ {\mathrm {Q S P}} \left(\left| 0 ^ {a} \right\rangle \left\langle 0 ^ {a} \right| \otimes \left| \psi_ {0} \right\rangle \left\langle \psi_ {0} \right|\right) \mathcal {U} _ {\mathrm {Q S P}} ^ {\dagger}, \tag {42}
$$

followed by the post-selection. We simulate the protocol on the quantum hardware. Let  $\eta$  be the experimentally obtained state on the system and ancillary registers before any measurements, and let  $\tilde{\eta}$  be the state that is post-selected on the ancillary state  $|0^a\rangle$  and normalized,

$$
\tilde {\eta} = \frac {\left(\left\langle 0 ^ {a} \right| \otimes I ^ {\otimes n}\right) \eta \left(\left| 0 ^ {a} \right\rangle \otimes I ^ {\otimes n}\right)}{\operatorname {T r} \left[ \left(\left| 0 ^ {a} \right\rangle \left\langle 0 ^ {a} \right| \otimes I ^ {\otimes n}\right) \eta \right]}. \tag {43}
$$

Then, the expectation value of a Pauli operator  $P$  with respect to  $\tilde{\eta}$  is

$$
\langle P \rangle_ {\bar {\eta}} = \frac {\operatorname {T r} [ (| 0 ^ {a} \rangle \langle 0 ^ {a} | \otimes P) \eta ]}{\operatorname {T r} [ (| 0 ^ {a} \rangle \langle 0 ^ {a} | \otimes I) \eta ]} = \frac {\left. \overline {{P}} \right\rangle_ {\eta}}{\left. \overline {{I}} \right\rangle_ {\eta}}, \tag {44}
$$

This can be estimated with  $n_{\mathrm{shots}}$  circuit executions with the variance

$$
\left. \operatorname {V a r} _ {\tilde {\eta}, P} = \langle P \rangle_ {\tilde {\eta}} ^ {2} \left(\frac {\operatorname {V a r} _ {\eta , \bar {P}}}{\langle \bar {P} \rangle_ {\eta} ^ {2}} + \frac {\operatorname {V a r} _ {\eta , \bar {I}}}{\langle \bar {I} \rangle_ {\eta} ^ {2}}\right), \right. \tag {45}
$$

where the variances inside the parenthesis are given by  $\mathrm{Var}_{\eta,\overline{P}} = (\langle \bar{l} \rangle_{\eta} - \langle \overline{P} \rangle_{\eta}^2) / (n_{\mathrm{shots}} - 1)$  and

$$
\operatorname {V a r} _ {\eta , \bar {l}} = (\langle \bar {l} \rangle_ {\eta} - \langle \bar {l} \rangle_ {\eta} ^ {2}) / (n _ {\text {s h o t s}} - 1).
$$

To mitigate noise effects, we model them by a depolarizing channel  $D_{p}^{55}$  applied to the entire system. Upon application of  $D_{p}$ , the state  $\sigma$  becomes

$$
D _ {p} [ \sigma ] = (1 - p) \sigma + p \frac {I ^ {\otimes n + a}}{2 ^ {n + a}}, \tag {46}
$$

where  $p = 1 - (1 - p_{\mathrm{TQ}})^{N_{\mathrm{TQ}}}$  with  $N_{\mathrm{TQ}}$  two-qubit gates of gate infidelity  $p_{\mathrm{TQ}}$ . With the state  $D_p[\sigma]$ , the expectation values of  $\bar{P}$  and  $\bar{I}$  take forms,

$$
\left\langle \bar {P} \right\rangle_ {D [ \sigma ]} = (1 - p) \left\langle \bar {P} \right\rangle_ {\sigma}, \tag {47}
$$

$$
\langle \bar {l} \rangle_ {D [ \sigma ]} = (1 - p) \langle \bar {l} \rangle_ {\sigma} + \frac {p}{2 ^ {a}}. \tag {48}
$$

Thus, inverting these equations leads to the expectation values without the depolarizing noise,  $\langle \overline{P}\rangle_{\sigma} = \langle \overline{P}\rangle_{D[\sigma]} / (1 - p)$  and  $\langle \overline{I}\rangle_{\sigma} = (\langle \overline{I}\rangle_{D[\sigma]} - p / 2^a) / (1 - p)$ . Assuming that the dominant source of error in the experimentally obtained state  $\eta$  is depolarizing noise, we infer the noiseless expectation value as,

$$
\langle P \rangle_ {\bar {\eta}} ^ {\text {m i t i g}} = \frac {\left\langle \bar {P} \right\rangle_ {\eta} ^ {\text {m i t i g}}}{\left\langle \bar {I} \right\rangle_ {\eta} ^ {\text {m i t i g}}} = \frac {\left\langle \bar {P} \right\rangle_ {\eta}}{\left\langle \bar {I} \right\rangle_ {\eta} - p / 2 ^ {a}}. \tag {49}
$$

This is Eq. (41) and is understood as mitigating the depolarizing noise, at the cost of a larger variance,

$$
\operatorname {V a r} _ {\hat {\eta}, P} ^ {\text {m i t i g}} = \langle P \rangle_ {\hat {\eta}} ^ {2} \left(\frac {\operatorname {V a r} _ {\eta , \bar {P}}}{\langle \bar {P} \rangle_ {\eta} ^ {2}} + \frac {\operatorname {V a r} _ {\eta , \bar {I}}}{\left(\langle \bar {I} \rangle_ {\eta} - p / 2 ^ {a}\right) ^ {2}}\right). \tag {50}
$$

Note that the quantity in the denominator of the second term evaluates to

$$
\langle \bar {l} \rangle_ {\eta} - \frac {p}{2 ^ {a}} \approx (1 - p) + \frac {p}{2 ^ {a}} - \frac {p}{2 ^ {a}} = (1 - p _ {\mathrm {T Q}}) ^ {N _ {\mathrm {T Q}}}, \tag {51}
$$

where the approximate equality is due to the QSP algorithmic error and other types of noise effects. This implies that the variance, and hence the required number of samples, increases exponentially in  $N_{\mathrm{TQ}}$  to achieve some fixed sampling error.

# DATA AVAILABILITY

The data that support the findings of this study are available at Zenodo<sup>78</sup>.

# CODE AVAILABILITY

The code used to create the figures in this paper is available from the authors upon reasonable request.

Received: 21 April 2023; Accepted: 8 September 2023; Published online: 23 September 2023

# REFERENCES

1. Shor, P. Algorithms for quantum computation: discrete logarithms and factoring. In Proc. 35th Annual Symposium on Foundations of Computer Science, 124-134 (ACM, 1994).  
2. Lloyd, S. Universal quantum simulators. Science 273, 1073-1078 (1996).  
3. Abrams, D. S. & Lloyd, S. Simulation of many-body fermi systems on a universal quantum computer. Phys. Rev. Lett. 79, 2586-2589 (1997).  
4. Grover, L. K. Quantum computers can search rapidly by using almost any transformation. Phys. Rev. Lett. 80, 4329-4332 (1998).  
5. Brassard, G., Høyer, P., Mosca, M. & Tapp, A. Quantum amplitude amplification and estimation. Quantum Comput. Inf. 305, 53-74 (2002).  
6. Zhou, Y., Stoudenmire, E. M. & Waintal, X. What limits the simulation of quantum computers? Phys. Rev. X 10, 041038 (2020).  
7. Stilck Franca, D. & Garcia-Patrón, R. Limitations of optimization algorithms on noisy quantum devices. Nat. Phys. 17, 1221-1227 (2021).  
8. Noh, K., Jiang, L. & Fefferman, B. Efficient classical simulation of noisy random quantum circuits in one dimension. Quantum 4, 318 (2020).  
9. Low, G. H., Yoder, T. J. & Chuang, I. L. Methodology of resonant equiangular composite quantum gates. Phys. Rev. X 6, 041067 (2016).  
10. Gilyén, A., Su, Y., Low, G. H. & Wiebe, N. Quantum singular value transformation and beyond: exponential improvements for quantum matrix arithmetics. arXiv preprint https://doi.org/10.48550/arXiv.1806.01838 (2018).  
11. Martyn, J. M., Rossi, Z. M., Tan, A. K. & Chuang, I. L. Grand unification of quantum algorithms. PRX Quantum 2, 040203 (2021).  
12. Feynman, R. P. Simulating physics with computers. Int. J. Theor. Phys 21, 467 (1982).  
13. Suzuki, M. General theory of fractal path integrals with applications to many-body theories and statistical physics. J. Math. Phys. 32, 400-407 (1991).  
14. Berry, D. W., Ahokas, G., Cleve, R. & Sanders, B. C. Efficient quantum algorithms for simulating sparse Hamiltonians. Commun. Math. Phys 270, 359-371 (2007).  
15. Childs, A. M., Su, Y., Tran, M. C., Wiebe, N. & Zhu, S. Theory of trotter error with commutator scaling. Phys. Rev. X 11, 011020 (2021).  
16. Berry, D. W. & Childs, A. M. Black-box Hamiltonian simulation and unitary implementation. arXiv preprint https://doi.org/10.48550/arXiv.0910.4157 (2009).  
17. Berry, D. W., Childs, A. M., Cleve, R., Kothari, R. & Somma, R. D. Simulating Hamiltonian dynamics with a truncated Taylor series. Phys. Rev. Lett. 114, 090502 (2015).  
18. Poulin, D., Qarry, A., Somma, R. & Verstraete, F. Quantum simulation of time-dependent Hamiltonians and the convenient illusion of Hilbert space. Phys. Rev. Lett. 106, 170501 (2011).  
19. Childs, A. M., Ostrander, A. & Su, Y. Faster quantum simulation by randomization. Quantum 3, 182 (2019).  
20. Campbell, E. Random compiler for fast hamiltonian simulation. Phys. Rev. Lett. 123, 070503 (2019).  
21. Chen, C.-F., Huang, H.-Y., Kueng, R. & Tropp, J. A. Concentration for random product formulas. PRX Quantum 2, 040305 (2021).  
22. Zhao, Q., Zhou, Y., Shaw, A. F., Li, T. & Childs, A. M. Hamiltonian simulation with random inputs. Phys. Rev. Lett. 129, 270502 (2022).  
23. Tepaske, M. S. J., Hahn, D. & Luitz, D. J. Optimal compression of quantum many-body time evolution operators into brickwall circuits. arXiv preprint https://doi.org/10.48550/arXiv.2205.03445 (2022).  
24. Mc Keever, C. & Lubasch, M. Classically optimized Hamiltonian simulation. Phys. Rev. Res. 5, 023146 (2023).  
25. Mansuroglu, R., Eckstein, T., Nützel, L., Wilkinson, S. A. & Hartmann, M. J. Variational Hamiltonian simulation for translational invariant systems via classical preprocessing. Quantum Sci. Technol. 8, 025006 (2023).  
26. Low, G. H. & Chuang, I. L. Optimal Hamiltonian simulation by quantum signal processing. Phys. Rev. Lett. 118, 010501 (2017).  
27. Low, G. H. & Chuang, I. L. Hamiltonian simulation by qubitization. Quantum 3, 163 (2019).  
28. Childs, A. M., Maslov, D., Nam, Y., Ross, N. J. & Su, Y. Toward the first quantum simulation with quantum speedup. Proc. Natl Acad. Sci. USA 115, 9456-9461 (2018).  
29. Dong, Y., Whaley, K. B. & Lin, L. A quantum Hamiltonian simulation benchmark. npj Quantum Inf. 8, 131 (2022).  
30. DeBry, K. et al. Experimental quantum channel discrimination using metastable states of a trapped ion. arXiv preprint https://doi.org/10.48550/arXiv.2305.14272 (2023).

31. Chakraborty, S., Gilyén, A. & Jeffery, S. The power of block-encoded matrix powers: improved regression techniques via faster Hamiltonian simulation. arXiv preprint https://doi.org/10.48550/arXiv.1804.01973 (2018).  
32. Camps, D., Lin, L., Van Beeumen, R. & Yang, C. Explicit quantum circuits for block encodings of certain sparse matrices. arXiv preprint https://doi.org/10.48550/arXiv.2203.10236 (2022).  
33. Camps, D. & Van Beeumen, R. Fable: Fast approximate quantum circuits for block-encodings. In 2022 IEEE International Conference on Quantum Computing and Engineering (QCE), 104-113 (IEEE, 2022).  
34. Childs, A. M. & Wiebe, N. Hamiltonian simulation using linear combinations of unitary operations. Quantum Info. Comput. 12, 901-924 (2012).  
35. Martyn, J. M., Liu, Y., Chin, Z. E. & Chuang, I. L. Efficient fully-coherent quantum signal processing algorithms for real-time dynamics simulation. J. Chem. Phys. 158, 024106 (2023).  
36. Kitaev, A. Y., Shen, A. H. & Vyalyi, M. N. Classical and Quantum Computation. (American Mathematical Society, USA, 2002).  
37. Kempe, J. & Regev, O. 3-local Hamiltonian is QMA-complete. arXiv preprint https://doi.org/10.48550/arXivquant-ph/0302079 (2003).  
38. Kempe, J., Kitaev, A. & Regev, O. The complexity of the local Hamiltonian problem. SIAM J. Comput. 35, 1070-1097 (2006).  
39. Baumgratz, T. & Plenio, M. B. Lower bounds for ground states of condensed matter systems. New J. Phys. 14, 023027 (2012).  
40. Barthel, T. & Hübener, R. Solving condensed-matter ground-state problems by semidefinite relaxations. Phys. Rev. Lett. 108, 200404 (2012).  
41. Anderson, P. W. Limits on the energy of the antiferromagnetic ground state. Phys. Rev. 83, 1260-1260 (1951).  
42. Eisert, J. A note on lower bounds to variational problems with guarantees. arXiv preprint https://doi.org/10.48550/arXiv.2301.06142 (2023).  
43. Kull, I., Schuch, N., Dove, B. & Navascués, M. Lower bounding ground-state energies of local Hamiltonians through the renormalization group. arXiv preprint https://doi.org/10.48550/arXiv.2212.03014 (2022).  
44. McClean, J. R., Boixo, S., Smelyanskiy, V. N., Babbush, R. & Neven, H. Barren plateaus in quantum neural network training landscapes. Nat. Commun. 9, 4812 (2018).  
45. Grant, E., Wossnig, L., Ostaszewski, M. & Benedetti, M. An initialization strategy for addressing barren plateaus in parametrized quantum circuits. Quantum 3, 214 (2019).  
46. Cerezo, M., Sone, A., Volkoff, T., Cincio, L. & Coles, P. J. Cost function dependent barren plateaus in shallow parametrized quantum circuits. Nat. Commun. 12, 1791(2021).  
47. Cervero Martin, E., Plekhanov, K. & Lubasch, M. Barren plateaus in quantum tensor network optimization. Quantum 7, 974 (2023).  
48. Sivarajah, S. et al.  $t|ket >$ : a retargetable compiler for NISQ devices. Quantum Sci. Technol 6, 014003 (2020).  
49. Tang, Y., Dilkes, S., Fitzpatrick, N. & Duncan, R. Reduced CX count for SELECT circuits using quantum multiplexor gates. In preparation.  
50. pyqsp. Python Quantum Signal Processing. https://github.com/ichuang/pyqsp (2023).  
51. Vrana, P., Reeb, D., Reitzner, D. & Wolf, M. M. Fault-ignorant quantum search. New J. Phys 16, 073033 (2014).  
52. Cohn, I., De Oliveira, A. L. F., Buksman, E. & De Lacalle, J. G. L. Grover's search with local and total depolarizing channel errors: Complexity analysis. Int. J. Quantum Inf. 14, 1650009 (2016).  
53. Arute, F. et al. Quantum supremacy using a programmable superconducting processor. Nature 574, 505-510 (2019).  
54. Dalzell, A. M., Hunter-Jones, N. & Brandão, F. G. S. L. Random quantum circuits transform local noise into global white noise. arXiv preprint https://doi.org/10.48550/arXiv.2111.14907 (2021).  
55. Urbanek, M. et al. Mitigating depolarizing noise on quantum computers with noise-estimation circuits. Phys. Rev. Lett. 127, 270502 (2021).  
56. Filip, R. Overlap and entanglement-witness measurements. Phys. Rev. A 65, 062320 (2002).  
57. Ekert, A. K. et al. Direct estimations of linear and nonlinear functionals of a quantum state. Phys. Rev. Lett. 88, 217901 (2002).  
58. Horodecki, P. & Ekert, A. Method for direct detection of quantum entanglement. Phys. Rev. Lett. 89, 127902 (2002).  
59. Moura Alves, C. & Jaksch, D. Multipartite entanglement detection in bosons. Phys. Rev. Lett. 93, 110501 (2004).  
60. Mintert, F. & Buchleitner, A. Observable entanglement measure for mixed quantum states. Phys. Rev. Lett. 98, 140505 (2007).  
61. Johri, S., Steiger, D. S. & Troyer, M. Entanglement spectroscopy on a quantum computer. Phys. Rev. B 96, 195136 (2017).  
62. van Enk, S. J. & Beenakker, C. W. J. Measuring  $\mathrm{Tr}\rho^n$  on single copies of  $\rho$  using random measurements. Phys. Rev. Lett. 108, 110503 (2012).

63. Elben, A., Vermersch, B., Dalmonte, M., Cirac, J. I. & Zoller, P. Renyi entropies from random quenches in atomic Hubbard and spin models. Phys. Rev. Lett. 120, 050406 (2018).  
64. Elben, A., Vermersch, B., Roos, C. F. & Zoller, P. Statistical correlations between locally randomized measurements: a toolbox for probing entanglement in many-body quantum states. Phys. Rev. A 99, 052323 (2019).  
65. Brydges, T. et al. Probing renyi entanglement entropy via randomized measurements. Science 364, 260-263 (2019).  
66. Elben, A. et al. Mixed-state entanglement from local randomized measurements. Phys. Rev. Lett. 125, 200501 (2020).  
67. Elben, A. et al. The randomized measurement toolbox. Nat. Rev. Phys. 5, 9-24 (2023).  
68. Kaushal, V. et al. Shutting-based trapped-ion quantum information processing. AVS Quantum Sci. 2, 014101 (2020).  
69. Pino, J. M. et al. Demonstration of the trapped-ion quantum CCD computer architecture. Nature 592, 209-213 (2021).  
70. Quantumum. System Model H1 Powered by Honeywell. https:// wwwquantinuum.com/hardware/h1 (2023).  
71. Banuls, M. C., Cirac, J. I. & Hastings, M. B. Strong and weak thermalization of infinite non-integrable quantum systems. Phys. Rev. Lett. 106, 050405 (2011).  
72. Shenker, S. H. & Stanford, D. Black holes and the butterfly effect. J. High Energy Phys. https://doi.org/10.48550/arXiv.1306.0622 (2014).  
73. Self, C. N., Benedetti, M. & Amaro, D. Protecting expressive circuits with a quantum error detection code. arXiv preprint https://doi.org/10.48550/arXiv.2211.06703 (2022).  
74. Tan, A. K., Liu, Y., Tran, M. C. & Chuang, I. L. Error correction of quantum algorithms: arbitrarily accurate recovery of noisy quantum signal processing. arXiv preprint https://doi.org/10.48550/arXiv.2301.08542 (2023).  
75. Nocedal, J. & Wright, S. Numerical Optimization. Springer Series in Operations Research and Financial Engineering (Springer New York, 2009).  
76. Shende, V., Bullock, S. & Markov, I. Synthesis of quantum-logic circuits. IEEE Trans. Comput. Aided Des. Integr. Circuits Syst. 25, 1000–1010 (2006).  
77. Bergholm, V., Vartiainen, J. J., Mottonen, M. & Salomaa, M. M. Quantum circuits with uniformly controlled one-qubit gates. Phys. Rev. A 71, 052330 (2005).  
78. Kikuchi, Y., Mc Keever, C., Coopmans, L., Lubasch, M. & Benedetti, M. Research data supporting "Realization of quantum signal processing on a noisy quantum computer". Zenodo https://doi.org/10.5281/zenodo.8313653 (2023).  
79. Haah, J. Product decomposition of periodic functions in quantum signal processing. Quantum 3, 190 (2019).  
80. Chao, R., Ding, D., Gilyen, A., Huang, C. & Szegedy, M. Finding angles for quantum signal processing with machine precision. arXiv preprint https://doi.org/10.48550/arXiv.2003.02831 (2020).  
81. Dong, Y., Meng, X., Whaley, K. B. & Lin, L. Efficient phase-factor evaluation in quantum signal processing. Phys. Rev. A 103, 042419 (2021).

# ACKNOWLEDGEMENTS

We thank Silas Dilkes, Samuel Duffield, Megan Kohagen, Kirill Plekhanov, Ciaran Ryan-Anderson, Yao Tang, Oscar Watts, and Kentaro Yamamoto for helpful discussions. We thank Nathan Fitzpatrick and Matthias Rosenkranz for providing feedback on an earlier version of this paper.

# AUTHOR CONTRIBUTIONS

Y.K., M.L. and M.B. conceived and designed the study. Y.K. performed analytic calculations, and Y.K. and M.B. carried out numerical studies. All authors analysed the data, created the figures, interpreted the results and wrote the manuscript.

# COMPETING INTERESTS

The authors declare no competing interests.

# ADDITIONAL INFORMATION

Correspondence and requests for materials should be addressed to Yuta Kikuchi or Marcello Benedetti.

Reprints and permission information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/d15e47ef16e23a515869f038eed76637dda4c2f9408adbee69408d765d6c2665.jpg)

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing,

adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2023