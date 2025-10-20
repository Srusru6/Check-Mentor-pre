# Heisenberg-limited Hamiltonian learning for interacting bosons

Check for updates

Haoya Li $^{1,5}$ , Yu Tong  ${}^{\text{已}}$ , Tuvia Gefen $^{2,3}$ , Hongkang Ni $^{4}$  & Lexing Ying $^{1,4}$

We develop a protocol for learning a class of interacting bosonic Hamiltonians from dynamics with Heisenberg-limited scaling. For Hamiltonians with an underlying bounded-degree graph structure, we can learn all parameters with root mean square error  $\epsilon$  using  $\mathcal{O}(1 / \epsilon)$  total evolution time, which is independent of the system size, in a way that is robust against state-preparation and measurement error. In the protocol, we only use bosonic coherent states, beam splitters, phase shifters, and homodyne measurements, which are easy to implement on many experimental platforms. A key technique we develop is to apply random unitaries to enforce symmetry in the effective Hamiltonian, which may be of independent interest.

Many tasks in quantum metrology and quantum sensing can be reduced to the task of learning the Hamiltonian  $H$  of a quantum system, whose evolution is described by the operator  $e^{-iHt}$  [1-9]. We call this task Hamiltonian learning, a name that is commonly used in the literature[10-24]. Besides quantum metrology and quantum sensing, Hamiltonian learning is also useful for quantum device engineering[25-30], and quantum many-body physics[10,11,31-36].

Previous works on Hamiltonian learning for many-body quantum systems are generally subject to the standard quantum limit (SQL), where to estimate the parameters in the Hamiltonian to precision  $\epsilon$ ,  $\mathcal{O}(\epsilon^{-2})$  samples are required[12-24,37-39]. On the other hand, for simple systems such as those consisting of a single spin, the Heisenberg limit can be achieved, where to obtain  $\epsilon$  precision, only  $\mathcal{O}(\epsilon^{-1})$  total amount of resources is needed. Achieving the Heisenberg limit requires using quantum-enhanced protocols that either use  $\mathcal{O}(\epsilon^{-1})$  entangled probes[3-5] or coherent evolution for  $\mathcal{O}(\epsilon^{-1})$  time[1,40,41]. The resources consumed are the number of probes and the length of time evolution, respectively.

The natural question is, can we achieve the Heisenberg limit for many-body quantum systems? When applying the existing quantum-enhanced protocols to the many-body setting, one quickly encounters difficulties. When many entangled probes are used, one needs many copies of the quantum system with the same parameters that can evolve simultaneously without interacting with each other. It is often unclear how to create these copies, except for certain scenarios, such as when many probes undergo evolution under the same field strength. For long coherent time-evolution, the many-body nature of the quantum systems becomes problematic as subsystems undergo open-system dynamics, and phenomena such as thermalization prevent local observables from having enough sensitivity to achieve the Heisenberg limit. One can consider performing entangled

measurements across all parts of the many-body system. Still, the difficulty in simulating the system makes finding a good measurement strategy extremely difficult.

Recently, a method was proposed in $^{42}$  to perform Hamiltonian learning for many-body spin systems with Heisenberg-limited scaling. The main technique is to apply quantum control in the form of random Pauli operators during time evolution so that the system evolves with an effective Hamiltonian that is easy to learn and, at the same time, preserves the parameters that one wants to learn. Another recent work proved that some form of quantum control is necessary for achieving the Heisenberg limit in this task $^{43}$ .

The above works are all focused on qubit systems, and Heisenberg-limited Hamiltonian learning for bosonic systems is relatively less studied. Bosonic systems, such as superconducting circuits $^{44-46}$ , integrated photonic circuits $^{47}$  and optomechanical platforms $^{48,49}$  are widely used for quantum sensing, communication, and computing $^{50-53}$ . These quantum applications require efficient calibration $^{16}$ , and it is thus highly desirable to develop optimal algorithms for characterizing bosonic Hamiltonians. For example, quantum computing and sensing with transmons require learning the energy levels and interactions between the transmons and microwave resonators.

For bosonic systems, there is a different set of "easy" quantum states, unitaries, and measurements than for spins. This work assumes that one can prepare coherent states, apply phase shifters and beam splitters, and perform the homodyne measurement. We note that although we may use terms from quantum optics, such as "phase shifters", we do not constrain our discussion to the optical setting. Additionally, in our protocol, we do not require any squeezing, which can be experimentally difficult to implement[54-57]. Using these resources, we present a protocol to learn a class

$^{1}$ Department of Mathematics, Stanford University, Stanford, CA, 94305, USA.  $^{2}$ Institute for Quantum Information and Matter, California Institute of Technology, Pasadena, CA, 91125, USA.  $^{3}$ Racah Institute of Physics, The Hebrew University of Jerusalem, Jerusalem, 91904 Givat Ram, Israel.  $^{4}$ Institute for Computational and Mathematical Engineering, Stanford University, Stanford, CA, 94305, USA.  $^{5}$ These authors contributed equally: Haoya Li, Yu Tong. e-mail: lexing@stanford.edu

of interacting bosonic Hamiltonians with Heisenberg-limited scaling. Our protocol can also tolerate a constant amount of noise in the state preparation and measurement (SPAM) procedures and has a small classical post-processing cost. We numerically demonstrate that our method is effective within experimentally feasible parameter ranges.

In our method, we apply random unitaries during time evolution to reshape the Hamiltonian into an effective Hamiltonian that is easier to learn. This follows the same high-level idea as<sup>42</sup> but is specifically tailored to the bosonic setting. Moreover, we can interpret the procedure as enforcing a target symmetry in the effective Hamiltonian, thus putting constraints on the dynamics. We believe this technique may be useful for other problems in quantum simulation as well<sup>58,59</sup>. In analyzing the deviation from the effective dynamics, the unboundedness of the bosonic Hamiltonian terms poses a challenge, as the analysis in<sup>42</sup> requires Hamiltonian terms to be bounded. We use more involved techniques to overcome this difficulty in ref. 60, Section 5.

The Hamiltonian reshaping technique used in this work is similar in spirit to the commonly used dynamical decoupling technique $^{61,62}$ . In fact, for quantum systems with simple geometry, such as a 1D chain, dynamical decoupling can be readily used to decouple it into isolated clusters, which is one of the goals we want to achieve in our procedure. However, this does not mean that our procedure is a simple application of dynamical decoupling. For more complicated geometry on a general graph with a constant degree, decoupling the system while still preserving the information to be learned already involves a graph coloring problem, which we discuss in depth in ref. 60, Section 4. For each isolated cluster obtained from this decoupling procedure, we will want to learn the Hamiltonian associated with it, which generally requires preparing the eigenstates in order to achieve the Heisenberg limit. $^{42}$  solves this problem by reshaping the Hamiltonian so that the eigenstates are all product states, while this approach no longer works in the bosonic scenario. In fact, the eigenstates are not even Gaussian states because we cannot completely remove the quartic interaction term, and it is, therefore, unreasonable to assume that we can efficiently prepare them. To solve this problem, we design a protocol that does not require an eigenstate and can still achieve the Heisenberg limit, as discussed in Section "Learning an anharmonic oscillator". We can see from these comparisons that the bosonic Hamiltonian learning problem requires very different tools and analysis compared to the qubit version.

# Results

In this work, we focus on quantum systems on  $N$  bosonic modes forming a  $d$ -dimensional lattice, with the Hamiltonian of the form

$$
H = \sum_ {\langle i, j \rangle} h _ {i j} b _ {i} ^ {\dagger} b _ {j} + \sum_ {i} \omega_ {i} b _ {i} ^ {\dagger} b _ {i} + \sum_ {i} \frac {\xi_ {i}}{2} n _ {i} (n _ {i} - 1), \tag {1}
$$

where  $b_{i} \left(b_{i}^{\dagger}\right)$  are bosonic annihilation (creation) operators, and  $n_i = b_i^\dagger b_i$ .  $\langle i,j\rangle$  means that the summation is over sites  $i,j$  that are adjacent to each other.  $h_{ij} = h_{ij}^{*}$ , and each  $\xi_{i}$  and  $\omega_{i}$  is a real number. We also assume that  $|h_{ij}|, |\omega_i|, |\xi_i|\leq 1$ . This class of Hamiltonians is relevant for superconducting quantum processors $^{16}$ , arrays of coupled cavities $^{63}$ , and phonon dynamics in ion crystals $^{64,65}$ . We will present a protocol that generates estimates  $\hat{h}_{ij},\hat{\omega}_i$  and  $\hat{\xi}_i$  such that

$$
\mathbb {E} [ | \hat {h} _ {i j} - h _ {i j} | ^ {2} ], \mathbb {E} [ | \hat {\omega} _ {i} - \omega_ {i} | ^ {2} ], \mathbb {E} [ | \hat {\xi} _ {i} - \xi_ {i} | ^ {2} ] \leq \epsilon^ {2}. \tag {2}
$$

The protocol has the following properties:

1. The total evolution time is  $\mathcal{O}(\epsilon^{-1})$ ;  
2. The number of experiments is  $\mathcal{O}(\mathrm{polylog}(\epsilon^{-1}))$ ;  
3. A constant amount of SPAM error can be tolerated.

More precisely, our protocol consists of  $N_{\mathrm{exp}} = \mathcal{O}(\mathrm{polylog}(\epsilon^{-1}))$  experiments, which we number by  $1,2,\dots ,N_{\mathrm{exp}}$ . In the  $j$ th experiment, we will initialize each bosonic mode in the system in a coherent state, let the system evolve for time  $t_j > 0$ , and perform homodyne measurement for the

bosonic modes. During time evolution, we will apply random beam splitters (on two modes) or phase shifters (on one mode). The total evolution time is defined to be  $\sum_{j=1}^{N_{\mathrm{exp}}} t_j$ , which is the amount of time required to run all the experiments. We assume that after we prepare the initial state and before we perform the measurement, the system goes through error channels  $\mathcal{E}_1$  and  $\mathcal{E}_2$ , which model the SPAM error. If  $\|\mathcal{E}_1 - \mathcal{I}\|_\diamond + \|\mathcal{E}_2 - \mathcal{I}\|_\diamond$  is upper-bounded by a small constant, then our protocol will still be able to reach arbitrary precision  $\epsilon$ . Here  $\|\cdot\|_\diamond$  is the diamond norm<sup>66</sup>, and  $\mathcal{I}$  is the identity channel. Our protocol also works in the case where the noise channels are only locally close to the identity, but are independent for each bosonic mode. We will explain this in more detail in Section "Learning an N-mode system". The precision is measured by the mean square error (MSE). We are using the big- $\mathcal{O}$  notation to hide the constants for simplicity, and we note that these constants never depend on the system size. Our protocol generates  $\mathcal{O}(NN_{\mathrm{exp}}) = \mathcal{O}(N\mathrm{polylog}(\epsilon^{-1}))$  classical data and it takes a similar amount of time to process these data to compute the estimates.

Below, we will describe the protocol in detail. We will start with a protocol to learn a single anharmonic oscillator, which forms the basic building block for more complex situations.

# Learning an anharmonic oscillator

We first consider the simple case in which

$$
H _ {\mathrm {A H O}} = \omega n + \frac {\xi}{2} n (n - 1), \tag {3}
$$

where  $n = b^{\dagger}b$ . We want to estimate the coefficients  $\omega$  and  $\xi$  with root mean square error (RMSE) at most  $\epsilon$ .

This is a quantum sensing problem with two parameters to be estimated. In quantum sensing, one usually calculates the quantum Cramer-Rao bound (QCRB) that provides a lower bound on the MSE of unbiased estimators. Because the two parameters correspond to Hamiltonian terms that commute with each other, the QCRB scales inverse quadratically with time, allowing us to achieve the Heisenberg-limited scaling. This bound, however, is valid only for local estimation where the prior distribution of the estimators is already concentrated around the exact value. Here, we provide an estimation protocol that achieves this scaling without any prior knowledge of the parameters.

Our protocol builds upon a robust frequency estimation algorithm similar to the robust phase estimation algorithm proposed in ref. 41 as well as the alternative version in ref. 67. In the robust phase estimation algorithm, we assume that through performing certain experiments that we will specify when introducing our protocol, we have access to a random variable  $Z_{\delta}(t)$  from measurement results, such that  $|Z_{\delta}(t) - e^{-i\omega t}|\leq 1$  with probability at least  $1 - \delta$ , and generating such a random variable requires time evolution  $\mathcal{O}(t\log (\delta^{-1}))$ . With multiple samples of this variable for different values of  $t$  and  $\delta$ , we can generate an estimate of  $\omega$  with RMSE at most  $\epsilon$  using  $\mathcal{O}(\epsilon^{-1})$  total evolution time. The algorithm proceeds by iteratively obtaining estimates with increasing accuracy through longer time evolution until the target precision is achieved. A detailed description of the algorithm and proof of its correctness can be found in ref. 60, Section 1.

We initialize the system in a coherent state  $|\alpha \rangle = e^{-|\alpha|^2 /2}\sum_k(\alpha^k /\sqrt{k!})|k\rangle$ , and let the system evolve under the Hamiltonian  $H_{\mathrm{AHO}}$ . In the end we perform homodyne measurements with quadrature operators  $X = (b + b^{\dagger}) / \sqrt{2}$  and  $P = i(b^{\dagger} - b) / \sqrt{2}$  in separate experiments. With these measurement results we will be able to estimate  $\langle b\rangle_{\alpha ,t} = \langle \alpha |e^{iH_{\mathrm{AHO}}t}be^{-iH_{\mathrm{AHO}}t}|\alpha \rangle$ , which can be exactly computed to be

$$
\langle b \rangle_ {\alpha , t} = \alpha e ^ {- | \alpha | ^ {2}} e ^ {- i \omega t} e ^ {| \alpha | ^ {2} e ^ {- i \xi t}}. \tag {4}
$$

We perform this calculation in ref. 60, Section 2.

Using (4), we can extract the values of  $\omega$  and  $\xi$  from  $\langle b\rangle_{\alpha ,t}$ . For  $\omega$ , note that  $\langle b\rangle_{\alpha ,t} / \alpha = e^{-i\omega t} + \mathcal{O}(|\alpha |^2)$ , and therefore we can choose  $|\alpha|$  to be

below a small constant so that an estimate for  $\langle b\rangle_{\alpha ,t} / \alpha$  will be close to  $e^{-i\omega t}$  within some small constant distance, which enables us to apply the robust frequency estimation algorithm to estimate  $\omega$  with RMSE at most  $\epsilon$  using total evolution time  $\mathcal{O}(\epsilon^{-1})$ . It is worth emphasizing that  $\alpha$  does not need to approach 0 thanks to the robust frequency estimation protocol and only needs to be chosen as a constant. More specifically, we only require that  $|\alpha |^2 < \pi /3$ , and therefore one can for example choose  $\alpha = \sqrt{\pi / 6}$ . The value of  $\xi$  does not affect the choice of parameters in this procedure.

For  $\xi$ , we can extract its value by constructing a periodically oscillating signal through

$$
e ^ {- i \xi t} = \frac {1}{| \alpha_ {1} | ^ {2} - | \alpha_ {2} | ^ {2}} \log \left(\frac {\alpha_ {2} \langle b \rangle_ {\alpha_ {1} , t}}{\alpha_ {1} \langle b \rangle_ {\alpha_ {2} , t}}\right) + 1. \tag {5}
$$

This enables us to estimate  $\xi$  using the robust frequency estimation algorithm. Note that, once again,  $\langle b\rangle_{\alpha_1,t}$  and  $\langle b\rangle_{\alpha_2,t}$  only need to be estimated to constant precision, rather than  $\epsilon$  precision which would result in an  $\mathcal{O}(\epsilon^{-2})$  scaling that would destroy the Heisenberg-limited scaling.

In the above procedure, we need to estimate the expectation of  $X$  and  $P$  operators, which are unbounded operators that can infinitely amplify any error in the quantum state. Fortunately, we found that we can replace them with operators  $X\mathbf{1}_{\{|X|\leq M\}}$  and  $P\mathbf{1}_{\{|P|\leq M\}}$ , where  $\mathbf{1}_{\{|X|\leq M\}} = \int_{|x|\leq M}|x\rangle \langle x|\mathrm{d}x$  and  $\mathbf{1}_{\{|P|\leq M\}}$  is similarly defined. This means truncating the eigenvalues of these operators at a threshold  $M$ . It is worth pointing out that  $M$  is chosen as a constant that is independent of all problem parameters. In practice, we can simply discard any  $X$  and  $P$  samples that are above the threshold  $M$  to implement these truncated operators. This fact, together with the error tolerance in the robust frequency estimation algorithm, enables us to tolerate a constant amount of error from SPAM and time evolution. The combined error from all sources should be below a small constant, which is sufficient for achieving arbitrarily high precision.

# Learning two coupled anharmonic oscillators

Next, we consider a system consisting of two coupled anharmonic oscillators, where the Hamiltonian is of the following form:

$$
\begin{array}{l} H = \omega_ {1} b _ {1} ^ {\dagger} b _ {1} + \omega_ {2} b _ {2} ^ {\dagger} b _ {2} + h _ {1 2} b _ {1} ^ {\dagger} b _ {2} + h _ {2 1} b _ {2} ^ {\dagger} b _ {1} + \frac {\xi_ {1}}{2} n _ {1} \left(n _ {1} - 1\right) \tag {6} \\ + \frac {\xi_ {2}}{2} n _ {2} \left(n _ {2} - 1\right) \\ \end{array}
$$

The goal is to learn all the coefficients  $\omega_{1},\omega_{2},\xi_{1},\xi_{2}$  , and  $h_{12}(h_{21} = h_{12}^{*})$

We first focus on learning the single-mode coefficients  $\omega_{1},\omega_{2},\xi_{1}$ , and  $\xi_{2}$ . To do this, we will insert random unitaries during time evolution to decouple the bosonic modes from each other. In other words, the time evolution operator undergoes the following transformation

$$
e ^ {- i H t} \mapsto \prod_ {j = 1} ^ {r} U _ {j} ^ {\dagger} e ^ {- i H \tau} U _ {j} = \prod_ {j = 1} ^ {r} e ^ {- i U _ {j} ^ {\dagger} H U _ {j} \tau}, \tag {7}
$$

where the  $U_{j}, j = 1,2,\dots,r$ , are the random beam splitters or phase shifters that we insert,  $r = t / \tau$ , and the product goes from right to left. Each  $U_{j}$  is independently drawn from a distribution that we denote by  $\mathcal{D}$ . In the limit of  $\tau \to 0$ , the dynamics can be described by an effective Hamiltonian

$$
H _ {\text {e f f e c t i v e}} = \mathbb {E} _ {U \sim \mathcal {D}} U ^ {\dagger} H U. \tag {8}
$$

This can be seen by considering the Taylor expansion of the time-evolved state in a small time step:

$$
\begin{array}{l} \mathbb {E} _ {U \sim \mathcal {D}} [ e ^ {- i U ^ {\dagger} H U \tau} \rho e ^ {i U ^ {\dagger} H U \tau} ] = \rho - i \tau \mathbb {E} _ {U \sim \mathcal {D}} [ [ U ^ {\dagger} H U, \rho ] ] + \mathcal {O} (\tau^ {2}) \tag {9} \\ = e ^ {- i \mathbb {E} _ {U \sim \mathcal {D}} [ U ^ {\dagger} H U ] \tau} \rho e ^ {i \mathbb {E} _ {U \sim \mathcal {D}} [ U ^ {\dagger} H U ] \tau} + \mathcal {O} (\tau^ {2}). \\ \end{array}
$$

Note that the above is not a rigorous proof because the  $\mathcal{O}(\tau^2)$  residue is an unbounded operator. We provide a rigorous bound of how far the actual

dynamics deviate from the limiting effective dynamics with finite  $\tau > 0$  in ref. 60, Section 5.

To learn all the single mode coefficients, we let the unitary  $U$  drawn from the distribution  $\mathcal{D}$  be

$$
U = e ^ {- i \theta n _ {1}}, \quad \theta \sim \mathcal {U} ([ 0, 2 \pi ]). \tag {10}
$$

Here  $\mathcal{U}([0,2\pi])$  is the uniform distribution over  $[0,2\pi]$ . We can then compute the effective Hamiltonian

$$
\begin{array}{l} H _ {\text {e f f e c t i v e}} = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} e ^ {i \theta n _ {1}} H e ^ {- i \theta n _ {1}} d \theta = \omega_ {1} n _ {1} + \omega_ {2} n _ {2} + \frac {\xi_ {1}}{2} n _ {1} (n _ {1} - 1) \\ + \frac {\xi_ {2}}{2} n _ {2} \left(n _ {2} - 1\right). \tag {11} \\ \end{array}
$$

In other words, the coupling term  $h_{12}b_1^\dagger b_2 + h_{21}b_2^\dagger b_1$  is canceled in the process, due to the equality  $e^{i\theta n_1}b_1e^{-i\tilde{\theta} n_1} = e^{-i\theta}b_1$ . We can interpret this procedure as enforcing a particle number conservation on the first bosonic mode. In the effective Hamiltonian, the two bosonic modes are no longer coupled together, and therefore, we can apply the learning algorithm described in Section "Learning an anharmonic oscillator" to learn the parameters of the two modes separately. For a more detailed description of the protocol, see ref. 60, Section 3.1.

Next, we will learn the coupling coefficient  $h_{12}$ . We will use the following unitaries

$$
U _ {x} (\theta) = e ^ {i \theta \left(b _ {1} ^ {\dagger} b _ {2} + b _ {2} ^ {\dagger} b _ {1}\right)}, \quad U _ {y} (\theta) = e ^ {\theta \left(b _ {1} ^ {\dagger} b _ {2} - b _ {2} ^ {\dagger} b _ {1}\right)}. \tag {12}
$$

Our protocol is based on the observation that under a single-particle basis rotation,  $h_{12}$  can be estimated from the new single-mode coefficients. More precisely, we let  $\tilde{b}_1 = U_y(\pi /4)b_1U_y^\dagger (\pi /4),$ $\tilde{b}_{2} = U_{y}(\pi /4)b_{2}U_{y}^{\dagger}(\pi /4)$ , and the new bosonic modes will be related to the old ones through

$$
\binom {\tilde {b} _ {1}} {\tilde {b} _ {2}} = \binom {\cos (\pi / 4)} {- \sin (\pi / 4)} \binom {b _ {1}} {b _ {2}}. \tag {13}
$$

We will then rewrite the Hamiltonian (6) in terms of  $\tilde{b}_1$  and  $\tilde{b}_{2\dagger}$ . The quadratic part of  $H$  can be written as  $\tilde{\omega}_1\tilde{b}_1^\dagger\tilde{b}_1 + \tilde{\omega}_2\tilde{b}_2^\dagger\tilde{b}_2 + \tilde{h}_{12}\tilde{b}_1\tilde{b}_2 + \tilde{h}_{21}\tilde{b}_2^\dagger\tilde{b}_1$ , where

$$
\tilde {\omega} _ {1} = \frac {\omega_ {1} + \omega_ {2}}{2} + \operatorname {R e} h _ {1 2}. \tag {14}
$$

Therefore,  $\operatorname{Re} h_{12}$  can be estimated if we can learn  $\tilde{\omega}_1$ . The quartic part becomes more complicated, but the procedure we describe next will yield an effective Hamiltonian of a simpler form.

In our protocol for learning  $\mathrm{Re}\, \mathrm{h}_{12}$ , we will let the random unitaries  $U_{j}$  in (7) be

$$
U _ {j} = U _ {x} (- \theta / 2), \quad \theta \sim \mathcal {U} ([ 0, 2 \pi ]), \tag {15}
$$

where  $\mathcal{U}([0,2\pi])$  denotes the uniform distribution on  $[0,2\pi]$ . Note that  $e^{-i\theta \tilde{n}_1} = e^{-i(\theta /2)(n_1 + n_2)}U_x(-\theta /2)$  where  $\tilde{n}_1 = \tilde{b}_1^\dagger \tilde{b}_1$ , and because the total particle number  $n_1 + n_2$  is conserved, the random unitary  $U_{x}(-\theta /2)$  is equivalent to  $e^{-i\theta \tilde{n}_1}$  up to a global phase. This random unitary, as in (11), results in an effective Hamiltonian in which  $\tilde{n}_1$  is conserved. The effective Hamiltonian can be written as the following

$$
H _ {\text {e f f e c t i v e}} = \tilde {\omega} _ {1} \tilde {n} _ {1} + \tilde {\omega} _ {2} \tilde {n} _ {2} + \frac {\tilde {\xi} _ {1 1}}{2} \tilde {n} _ {1} (\tilde {n} _ {1} - 1) + \frac {\tilde {\xi} _ {2 2}}{2} \tilde {n} _ {2} (\tilde {n} _ {2} - 1) + \tilde {\xi} _ {1 2} \tilde {n} _ {1} \tilde {n} _ {2}. \tag {16}
$$

For a derivation of this effective Hamiltonian see ref. 60, Eqs. (68)-(71). In this effective Hamiltonian, the two bosonic modes  $\tilde{b}_{1}$  and  $\tilde{b}_{2}$  are still coupled through the term  $\tilde{\xi}_{12}\tilde{n}_1\tilde{n}_2$ . However, because the particle numbers on both modes are conserved, we can initialize the system with no particle on the mode  $\tilde{b}_{2}$ , and the coupling term will have no effect. More specifically, the initial state we use is  $U_{y}(\pi /4)|\alpha \rangle |0\rangle$ , which is an  $\alpha$ -eigenstate for  $\tilde{b}_{1}$  and a 0-eigenstate for  $\tilde{b}_{2}$ . The effective Hamiltonian can then be further reduced to

$$
H _ {\text {e f f e c t i v e}} ^ {\prime} = \tilde {\omega} _ {1} \tilde {n} _ {1} + \frac {\tilde {\xi} _ {1 1}}{2} \tilde {n} _ {1} (\tilde {n} _ {1} - 1). \tag {17}
$$

This enables us to learn  $\tilde{\omega}_{1}$  using the single-mode protocol in Section "Learning an anharmonic oscillator", which then gives us  $\mathrm{Re}h_{12}$  through (14). When performing homodyne measurement in the end, we also need to apply  $U_{y}(-\pi /4)$  to rotate back to the original single-particle basis. We write down the quantum state we get right before measurement to summarize the whole procedure:

$$
U _ {y} \left(- \frac {\pi}{4}\right) \prod_ {j = 1} ^ {r} \left(U _ {x} \left(\frac {\theta_ {j}}{2}\right) e ^ {- i H \tau} U _ {x} \left(- \frac {\theta_ {j}}{2}\right)\right) U _ {y} \left(\frac {\pi}{4}\right) | \alpha \rangle | 0 \rangle , \tag {18}
$$

where all  $\theta_{j}$  are independently drawn from the uniform distribution over  $[0, 2\pi]$ .

The above procedure yields  $\mathrm{Re}h_{12}$ . For  $\operatorname{Im}h_{12}$ , we only need to switch the roles of  $U_x(\theta)$  and  $U_y(\theta)$  and go through the same procedure. For a more detailed discussion, see ref. 60, Section 3.2.

# Learning an  $N$ -mode system

So far, we have concerned ourselves with learning small systems with one or two modes, but the protocol we develop can be easily generalized to  $N$ -mode systems. This section will focus on  $N$  bosonic modes arranged on a 1D chain. For the more general situation with a bounded degree graph, e.g.,  $D$ -dimensional square lattice, Kagome lattice, etc., see ref. 60, Section 4. The Hamiltonian is described by (1), where the bosonic modes are labeled  $1, 2, \dots, N$ , and  $i$  and  $j$  are adjacent only when  $j = i \pm 1$ .

For this  $N$ -mode system, we consider a divide-and-conquer approach. We will apply random unitaries so that in the effective dynamics, the system is divided into clusters of one or two modes, each of which does not interact with the rest of the system. In this way, we can learn the parameters associated with each cluster independently and in parallel using our protocol in Section "Learning two coupled anharmonic oscillators".

More specifically, we apply random unitaries in the same way as described in (7). The random unitary  $U_{j}$  is first chosen to be

$$
U _ {j} = \prod_ {k = 1} ^ {\lfloor N / 3 \rfloor} e ^ {- i \theta_ {3 k} n _ {3 k}}, \tag {19}
$$

where the random variables  $\theta_{3k}$  are independently drawn from  $\mathcal{U}([0,2\pi])$ , the uniform distribution over  $[0,2\pi]$ . Randomly applying the unitaries from this distribution enforces particle number conservation on sites with indices that are integer multiples of 3. Therefore, any Hamiltonian term  $b_i^\dagger b_j$  that involves sites 3, 6, 9, ... are canceled. The effective Hamiltonian is

$$
\begin{array}{l} H _ {\text {e f f e c t i v e}} = \omega_ {1} n _ {1} + \omega_ {2} n _ {2} + h _ {1 2} b _ {1} ^ {\dagger} b _ {2} + h _ {2 1} b _ {2} ^ {\dagger} b _ {1} \\ + \omega_ {4} n _ {4} + \omega_ {5} n _ {5} + h _ {4 5} b _ {4} ^ {\dagger} b _ {5} + h _ {5 4} b _ {3} ^ {\dagger} b _ {4} + \dots \tag {20} \\ + \sum_ {i} ^ {\xi_ {i}} n _ {i} (n _ {i} - 1). \\ \end{array}
$$

In this Hamiltonian, the two modes 1 and 2 form a cluster: they only interact with each other but not with the rest of the system. The same is true for modes 5 and 6, 7 and 8, etc. We can then apply the two-mode protocol in Section "Learning two coupled anharmonic oscillators" to learn all

coefficients associated with modes 1, 2, 5, 6, ... . Note that coefficients associated with different clusters can be learned in parallel in the same experiment.

Other coefficients remain to learn, such as  $\omega_{3}$ ,  $h_{23}$ , and  $h_{34}$ . We can adopt the same strategy but choose the random unitary  $U_{j} = \prod_{k=0}^{\lfloor N/3 \rfloor-1} e^{-i\theta_{3k+1}n_{3k+1}}$  so that modes 2 and 3, 5 and 6, etc. now form clusters. Similarly, we can let modes 3 and 4, 6 and 7, etc., form clusters. In this way, we can learn all the coefficients in the Hamiltonian using three different clustering schemes. The total evolution time required for carrying out all experiments will only be three times the cost of a two-mode protocol because different clusters can be learned in parallel.

Next, we will show that our protocol is robust against extensive SPAM error: i.e., every local state preparation and measurement procedure involves a constant amount of error. More precisely, after we prepare the initial state, each bosonic mode goes through a noise channel  $\mathcal{E}_P$ , so that the entire system goes through a channel  $\mathcal{E}_P^{\otimes N}$ . Similarly, we assume that before the measurement each bosonic mode also goes through a noise channel  $\mathcal{E}_M$ , so that globally we have  $\mathcal{E}_P^{\otimes N}$ . We will show that the observable error can be controlled by local errors  $\| \mathcal{E}_P - \mathcal{I} \|_{\diamond} + \| \mathcal{E}_M - \mathcal{I} \|_{\diamond}$ , rather than the global error  $\| \mathcal{E}_P^{\otimes N} - \mathcal{I}^{\otimes N} \|_{\diamond} + \| \mathcal{E}_M^{\otimes N} - \mathcal{I}^{\otimes N} \|_{\diamond}$ .

To see this, we observe that, in the parallel learning procedure described above, we decompose the system into  $J = \Theta(N)$  different clusters that do not interact with each other in the effective Hamiltonian, and the initial state, as well as the observables that we want to measure, are also local to each cluster. This means we can write the initial state as  $\rho = \bigotimes_{j=1}^{J} \rho_{j}$ , and the effective Hamiltonian as  $H_{\text{effective}} = \sum_{j=1}^{J} H_{j}$ , with each  $H_{j}$  supported only on the  $j$ th cluster. We are only interested in the expectation of truncated local observables  $\tilde{X}_{i} = X_{i} \mathbf{1}_{\{|X_{i}| \leq M\}}$  and  $\tilde{P}_{i} = P_{i} \mathbf{1}_{\{|P_{i}| \leq M\}}$ . Now let us focus on site  $i$  in the  $j$ th cluster, and we want to measure the expectation value of  $\tilde{X}_{i}$ . The ideal expectation value is

$$
\operatorname {t r} \left[ \tilde {X} _ {i} e ^ {- i H _ {\text {e f f e c t i v e}} t} \rho e ^ {i H _ {\text {e f f e c t i v e}} t} \right] = \operatorname {t r} \left[ \tilde {X} _ {i} e ^ {- i H _ {j} t} \rho_ {j} e ^ {i H _ {j} t} \right], \tag {21}
$$

where we have used the fact that  $e^{-iH_{\mathrm{effective}}t} = \bigotimes_{j=1}^{J}e^{-iH_{j}t}$ . With the noise channels  $\mathcal{E}_P$  and  $\mathcal{E}_M$ , what we actually get will be

$$
\left. \operatorname {t r} \left[ \tilde {X} _ {i} \mathcal {E} _ {M} ^ {\otimes N} \left(e ^ {- i H _ {\text {e f f e c t i v e}} t} \mathcal {E} _ {P} ^ {\otimes N} (\rho) e ^ {i H _ {\text {e f f e c t i v e}} t}\right) \right] = \operatorname {t r} \left[ \tilde {X} _ {i} \mathcal {E} _ {M} \left(e ^ {- i H _ {f} t} \mathcal {E} _ {P} \left(\rho_ {j}\right) e ^ {i H _ {f} t}\right) \right] \right. \tag {22}
$$

From this we can see that the difference between the ideal expectation value and the expectation value we actually get is upper bounded by

$$
\| \tilde {X} _ {i} \| (\| \mathcal {E} _ {P} - \mathcal {I} \| _ {\diamond} + \| \mathcal {E} _ {M} - \mathcal {I} \| _ {\diamond}) \leq M (\| \mathcal {E} _ {P} - \mathcal {I} \| _ {\diamond} + \| \mathcal {E} _ {M} - \mathcal {I} \| _ {\diamond}). \tag {23}
$$

In the robust frequency estimation protocol, we can tolerate a constant amount of error in the signal. Because the truncation threshold  $M$  is chosen to be some constant, we only need  $\| \mathcal{E}_P - \mathcal{I}\|_{\diamond} + \| \mathcal{E}_M - \mathcal{I}\|_{\diamond}$  to be below a certain small constant (independent of the system size) to reach arbitrarily high precision. Following the same argument, we can also show that the above conclusion holds for noise channels that are tensor products of error channels on each individual cluster (rather than sites). We conjecture that this result can be extended to a wider range of noise channels that preserve locality.

More generally, we consider a system whose interaction can be described by a bounded-degree graph. We can design similar clustering schemes based on an appropriate coloring of its link graph, i.e., the graph whose vertices are the edges of the original graph. The overhead introduced will be quadratic in the degree of the original graph and independent of the system size  $N$ . This is discussed in more detail in ref. 60, Section 4.

# Numerical examples

In this section, we simulate the protocol for a one-dimensional chain of bosonic modes with nearest neighbor interactions. We first study the case of

![](images/b996fea2399d40f8e93b081c1cddcd28ed924116570d11d630080e93261601f2.jpg)  
Fig. 1 | Estimation errors and Trotter errors in various cases. The left and middle plots correspond to a Hamiltonian that contains only linear terms. The right plot corresponds to the full Hamiltonian with non-linear terms. Left: Average estimation error per measurement of the  $\{h_{i,j}\}$  parameters.  $m$  denotes the number of samples used to estimate the parameters, here  $m = 500$ . The number of modes is  $N = 20$ , and the initial state is a product of coherent states with  $\alpha = 1$ . Solid blue line: the ideal statistical error  $(1 / (2t))$ . The estimation error with  $\tau = 2$  ns (orange squares),  $\tau = 5$  ns

![](images/0d25c06026265e20ed55ff4061c4a92cfe3435346e1fe3e75e3039d33ad7ccaf.jpg)  
(yellow squares),  $\tau = 10$  ns (purple squares) are compared to the ideal statistical error. Deviations are due to the Trotter errors. Inset: systematic errors due to Trotter for different  $\tau$ 's (without shot noise). Middle: estimation errors of the  $\{\omega_{i}\}$  parameters, same values of  $m, N, \alpha$  as above. Right: estimation error of the  $\{h_{i,j}\}$  terms, where the Hamiltonian contains also non-linear terms and  $N = 4$ . Here, the initial state is a product of coherent states with  $\alpha = 0.5$ .

![](images/8d2feb9bd7245f4ad0f865ebbeb169594c1920c6256ae2eb1953292f5e64ce28.jpg)

a linear-optics Hamiltonian for which numerical simulation and analysis are simple, and then present numerical results also for the general, non-linear case. Starting with the linear case, the Hamiltonian we want to learn is of the form

$$
H = \sum_ {i} h _ {i, i + 1} b _ {i} ^ {\dagger} b _ {i + 1} + h _ {i, i + 1} ^ {*} b _ {i + 1} ^ {\dagger} b _ {i} + \omega_ {i} n _ {i}. \tag {24}
$$

In our numerical examples, we apply Gaussian unitaries at fixed interval  $\tau$  in a deterministic fashion rather than stochastically, which is also simpler for implementation and works equally well for simple geometry. The Hamiltonian parameters,  $\omega_{i}$ ,  $\mathrm{Re}h_{\mathrm{i},\mathrm{j}}$ ,  $\mathrm{Im}h_{\mathrm{i},\mathrm{j}}$ , are chosen at random from the interval [0, 10 MHz]. These values are comparable to experimental values of microwave photons and superconducting devices<sup>16</sup>. The time steps  $\tau$  are taken to be between 2 and 10 ns.

To estimate  $\mathrm{Re}h_{\mathrm{i,j}}$ ,  $\mathrm{Im}h_{\mathrm{i,j}}$  we simulated the following (deterministic) pulse sequence: for  $\mathrm{Re}h_{\mathrm{i,j}}$ :

$$
U _ {\mathrm {t o t}} = \left[ U _ {X} ^ {\dagger} \left(U _ {Z} ^ {\dagger} e ^ {- i H \tau} U _ {Z} e ^ {- i H \tau}\right) U _ {X} \left(U _ {Z} ^ {\dagger} e ^ {- i H \tau} U _ {Z} e ^ {- i H \tau}\right) \right] ^ {N _ {\mathrm {s t e p s}}}, \tag {25}
$$

with  $U_{Z} = \Pi_{k}e^{i\pi n_{3k}}$ ,  $U_{X} = \Pi_{k}e^{i\pi (b_{3k + 1}b_{3k + 2}^{\dagger} + \mathrm{h.c.})}$ . The above pulse sequence makes the system evolve first under the Hamiltonian  $H$ , and then under  $U_Z^\dagger H U_Z$ ,  $U_X^\dagger H U_X$ , and  $U_Z^\dagger U_X^\dagger H U_X U_Z$ , each for time  $\tau$ . The above time evolution can be thought of as the Trotter decomposition due to the effective Hamiltonian

$$
H _ {\text {e f f e c t i v e}} = \frac {1}{4} \left(H + U _ {Z} ^ {\dagger} H U _ {Z} + U _ {X} ^ {\dagger} H U _ {X} + U _ {Z} ^ {\dagger} U _ {X} ^ {\dagger} H U _ {X} U _ {Z}\right). \tag {26}
$$

The application of  $U_Z$  and  $U_Z^\dagger$  removes all hopping terms involving sites 3, 6, 9, ..., resulting in an effective Hamiltonian of the form (20). Focusing on the bosonic modes 1 and 2, the effective Hamiltonian governing their evolution is

$$
\begin{array}{l} \frac {\omega_ {1} + \omega_ {2}}{2} \left(n _ {1} + n _ {2}\right) + \operatorname {R e} h _ {1 2} \left(b _ {1} ^ {\dagger} b _ {2} + b _ {2} ^ {\dagger} b _ {1}\right) + i \operatorname {I m} h _ {1 2} \left(b _ {1} ^ {\dagger} b _ {2} - b _ {2} ^ {\dagger} b _ {1}\right) \\ + \frac {\omega_ {1} - \omega_ {2}}{2} \left(n _ {1} - n _ {2}\right). \tag {27} \\ \end{array}
$$

These four terms correspond to the  $I, X, Y,$  and  $Z$  matrix, respectively. Applying  $U_{X}$  and  $U_{X}^{\dagger}$  will further remove the  $Y$  and  $Z$  terms because they fail to commute with  $U_{X}$ . Thus the effective Hamiltonian for modes 1 and 2 is

$\frac{\omega_1 + \omega_2}{2} (n_1 + n_2) + \mathrm{Re}\mathrm{h}_{12}(\mathrm{b}_1^\dagger \mathrm{b}_2 + \mathrm{b}_2^\dagger \mathrm{b}_1)$ . We can then estimate  $\mathrm{Re}\mathrm{h}_{12}$  from it using a two-mode coherent state as discussed in Section "Learning two coupled anharmonic oscillators", with the information of  $\omega_{1}$  and  $\omega_{2}$  (we will discuss how to estimate  $\omega_{i}$  which is in fact much simpler than  $h_{ij}$ ). Likewise we can estimate all the  $\mathrm{Re}\mathrm{h}_{3\mathrm{k} + 1,3\mathrm{k} + 2}$  terms. The rest of the real part terms are obtained by varying the pulses in  $U_{Z}$ . Im  $h_{i,j}$  are obtained by replacing  $U_{X}$  with  $U_{Y} = \Pi k e^{\pi (b_{3k + 1}b_{3k + 2}^{\dagger} - h.c.)}$  in the sequence.

The average estimation error of the  $h_{i,j}$  parameters is shown in Fig. 1 for different values of  $\tau$ . These estimation errors are compared to the ideal statistical error,  $\Delta (h_{i,j})_{\mathrm{ideal}} = 1 / (2t)$  (see ref. 60 Section 6 for derivation of this expression). The error in the numerics consists of two terms:  $\Delta (h_{i,j})^2 = \frac{1}{m}\Delta (h_{i,j})_{\mathrm{ideal}}^2 +\epsilon_T^2$ , where  $\epsilon_{T}$  is the bias due to finite step size, or in other words, the estimation error in the absence of shot noise but only with Trotter error, and  $m$  is the number of samples used to estimate the parameters. The estimation error thus coincides with the ideal Heisenberg limit expression as long as  $\epsilon_T < \frac{\Delta(h_{i,j})_{\mathrm{ideal}}}{\sqrt{m}}$ . We observe that  $\epsilon_T\sim w^3\tau^2$ , where  $w = 10\mathrm{MHz}$  is the order of magnitude of the Hamiltonian terms. Note that the first-order Trotter error in fact vanishes, and we analyze this in ref. 60, Section 6.

To estimate the  $\omega_{i}$  terms, we perform the following pulse sequence:

$$
U _ {\text {t o t}} = \left[ U _ {Z} ^ {\dagger} e ^ {- i H \tau} U _ {Z} e ^ {- i H \tau} \right] ^ {N _ {\text {s t e p s}}}, \tag {28}
$$

where now  $U_{Z} = \Pi ke^{i\pi n_{2k}}$ . These pulses suppress all the nearest neighbor interactions. As a result, the effective Hamiltonian is

$$
H _ {\text {e f f e c t i v e}} = \sum_ {i} \omega_ {i} n _ {i}. \tag {29}
$$

The average estimation error of the  $\omega_{i}$  parameters is shown in Fig. 1 for different values of  $\tau$ . We find that  $\epsilon_{T}$  has an interesting behavior: at short times it goes as  $\sim w^{2}\tau$  and at longer times as  $\sim \frac{w\tau}{t}$ . We explain this error behavior in ref. 60, Section 6.

We perform a similar analysis with the general Hamiltonian of (1) that also includes the non-linear terms. The non-linear case requires some modifications compared to the linear case. The deterministic pulse sequence used for estimating the  $\{\mathrm{Re}h_{i,j}\}_{i,j}$  terms (Eq. (25)) is modified to

$$
U _ {\mathrm {t o t}} = \left[ \left(U _ {Z} U _ {X} ^ {(- \pi / 2)}\right) ^ {\dagger} U U _ {Z} U _ {X} ^ {(- \pi / 2)} U _ {X} ^ {(\pi / 2) \dagger} U U _ {X} ^ {(\pi / 2)} \left(U _ {Z} U _ {X} ^ {(\pi)}\right) ^ {\dagger} U U _ {Z} U _ {X} ^ {(\pi)} U \right] ^ {N _ {\mathrm {a t e s}}},
$$

![](images/b4cfb3dbdae4702a11e4b82640ed56df7e44a80725f4edcfb3dc81e5caab93ff.jpg)  
Fig. 2 | Estimating  $\omega$  under SPAM error on a single mode. We provide the target error and the actual error (evaluated as the mean absolute error of 20 independent runs) as a function of both the total evolution time (left, the cumulative time needed to run all experiments) and the maximum evolution time (right, the maximum time needed for one experiment). The gray dashed lines indicate error scaling as  $10^{3} / t_{\mathrm{total}}$  and  $1 / t_{\mathrm{max}}$  in the left and right figures respectively. Here  $\omega = 0.15\mathrm{MHz}$  and  $\xi = 1.0\mathrm{MHz}$ . We use coherent state  $|\alpha\rangle$  where  $\alpha = 0.5$ , and model SPAM error by letting

![](images/11d08aea9b2f893cb736baa97dd320ef640ae3492ae16a302d6c46ee6084737b.jpg)  
the actual initial state be  $|\alpha_{\mathrm{actual}}\rangle$  for  $\alpha_{\mathrm{actual}}$  drawn from a Gaussian distribution with mean  $\alpha + 0.03 + 0.03i$  and standard deviation 0.1 on the real part. For the expectation value  $\langle b\rangle$ , we add a further systematic error  $0.02 + 0.02i$  to model the effect of truncating with a threshold  $M$  on top of the shot noise (modeled as Gaussian), even though for a single model no such truncation is needed. No knowledge of the noise or  $\xi$  is used in the estimation protocol.

where  $U_{X}^{(\theta)} = \Pi_{k}e^{i\theta \left(b_{3k + 1}b_{3k + 2}^{\dagger} + \mathrm{h.c.}\right)}$  and the similarly for  $\{\operatorname {Im}\mathfrak{h}_{\mathrm{i},\mathrm{j}}\}_{i,j}$  where  $U_{Y}^{(\theta)} = \Pi_{k}e^{\theta \left(b_{3k + 1}b_{3k + 2}^{\dagger} - \mathrm{h.c.}\right)}$  replaces  $U_{X}^{(\theta)}$

The numerical results are plotted in Fig. 1c. We observe that the behavior of the estimation Trotter errors remains the same as in the linear case, where it scales as  $w^3\tau^2$ . The behavior of the statistical error slightly changes due to the non-linear terms; it becomes larger by a factor of at most  $\exp (2|\alpha |^2)$  given an initial state of  $|\alpha \rangle$ . However, by an appropriate tuning of the measurement time in each block we can get rid of this factor and retrieve the statistical error in the linear case (see details in supplemental material).

In Fig. 2, we numerically demonstrate that our protocol is robust to the SPAM error. We focus on the single-mode case for simplicity, where the Hamiltonian is  $H = \omega n + (\xi / 2)n(n - 1)$ . In this simulation, we assume no prior knowledge of  $\omega$  except that  $|\omega| \leq 1 \mathrm{MHz}$ . We model the SPAM error in the following way: each time we prepare the coherent state  $|\alpha\rangle$ , we assume that we obtain a different coherent state  $|\alpha_{\mathrm{actual}}\rangle$  where  $\alpha_{\mathrm{actual}}$  is equal to  $\alpha$  plus Gaussian noise, which can have a systematic bias. The initial state, therefore, undergoes a random displacement error channel, where we assume no knowledge of the properties of this channel, e.g., the variance and bias of the displacement. We also include the shot noise and error coming from the truncation of  $X$  and  $P$  quadratures in our simulation. For specific parameters, see the caption of Fig. 2. We assume no knowledge of these parameters, or of  $\xi$ , in our estimation protocol.

# Discussion

In this work, we propose a protocol to learn a class of interacting bosonic Hamiltonians with Heisenberg-limited scaling. Our protocol uses only elements of linear optics that are easy to implement on many experimental platforms. Besides achieving the Heisenberg-limited scaling, our protocol can also tolerate a constant amount of noise thanks to the robust frequency estimation subroutine discussed in Section "Learning an anharmonic oscillator". As a part of the protocol, we also propose a method to enforce symmetry on the effective Hamiltonian governing the system's evolution.

To our knowledge, our work is the first to propose a method that learns non-interacting bosonic Hamiltonians with Heisenberg-limited scaling in a scalable way. However, many open problems remain to be solved in this research direction. In this work, we only consider the particle-number preserving Hamiltonian in (1), but realistic Hamiltonians may contain terms that do not preserve the particle number, such as the coupling term in the Jaynes-Cummings model[68]. Also, higher-order anharmonic effects beyond the fourth order may be non-negligible in certain quantum systems.

In our protocol, we need to apply random unitaries with a frequency that depends on the target precision. For higher precision, the speed of applying these unitaries will also need to be faster, which may be a problem for experimental implementation. In ref. 60, Theorem 7, we proved that it suffices to apply the random unitaries with a frequency scaling as  $\mathcal{O}(N^2/\epsilon)$ , but we have reasons to believe that this rigorous bound is over-pessimistic.

In the spin scenario, using the Lieb-Robinson bound, one can show that a frequency of  $\mathcal{O}(1 / \epsilon)$  suffices, which is independent of the system size, and one can further improve it to  $\mathcal{O}(1 / \sqrt{\epsilon})$  using Trotterization<sup>42</sup>. Since the Lieb-Robinson bound is also available for the Bose-Hubbard model<sup>69</sup>, one would expect that a similar scaling also holds for the present setting. In fact, we numerically show that a system-size-independent scaling is sufficient, at least for the non-interacting case in ref. 60, Fig. 1. However, technical difficulties with the unbounded operators in the Hamiltonian prevented us from obtaining this scaling in a rigorous way. If we are allowed to apply non-Gaussian operations, then one may be able to reduce the required frequency further following<sup>43,70</sup>. Moreover, since our protocol requires letting the system evolve coherently for  $\mathcal{O}(\epsilon^{-1})$  times to reach  $\epsilon$  precision, the achievable precision will be limited by quantum noise such as dephasing and photon losses that limit the coherence time of most experimental Bosonic systems. It would be therefore interesting to explore whether noise suppression techniques such as quantum error correction<sup>71,77-82</sup> can mitigate this limitation and whether they can be incorporated into our protocol in a useful and scalable way. In this work, the goal is to learn all the parameters in the Hamiltonian, but if we only want to learn a function of these terms, as is relevant for the quantum sensing setting in refs. 72-74,83, we may also consider whether the operations employed in our protocol can lead to practical benefits.

Another limitation of our method is that in order to implement the random unitaries used in our protocol, one would need some knowledge of the underlying quantum system $^{75,76}$ . This means that our method is likely more suitable for obtaining high-precision estimates of the system parameters using low-precision prior knowledge, rather than directly estimating the parameters in a completely unknown quantum system.

# Methods

# Enforcing symmetry using random unitaries

This section will describe how to enforce symmetry using random unitaries. This strategy is similar in spirit to the symmetry protection strategies in refs. 58,59, but is easier to scale to an  $N$ -mode system in the current setting.

Let us first consider the general case where we have a compact Lie group  $G$  that describes the symmetry we want in the quantum system. Our quantum system is evolving under a Hamiltonian  $H$  that does not necessarily satisfy this symmetry, i.e., there may exist  $g \in G$  such that  $gHg^{-1} \neq H$ . We want to have the system evolve under an effective Hamiltonian  $H_{\mathrm{effective}}$  that satisfies the symmetry, i.e.,

$$
g H _ {\text {e f f e c t i v e}} g ^ {- 1} = H _ {\text {e f f e c t i v e}}. \tag {30}
$$

We achieve this by inserting random unitaries in the same way as in (7), which gives us an effective Hamiltonian according to (8). The distribution from which we draw the random unitaries is the Haar measure on  $G$ , which

we denote by  $\mu$ . The effective Hamiltonian can be computed as

$$
H _ {\text {e f f e c t i v e}} = \int g H g ^ {- 1} \mu (\mathrm {d} g). \tag {31}
$$

When the Hamiltonian  $H$  is unbounded, the above equality may only hold in a weak sense. We can verify that this effective Hamiltonian satisfies the desired symmetry because

$$
g ^ {\prime} H _ {\text {e f f e c t i v e}} g ^ {\prime - 1} = \int g ^ {\prime} g H \left(g ^ {\prime} g\right) ^ {- 1} \mu (\mathrm {d} g) = \int g ^ {\prime} g H \left(g ^ {\prime} g\right) ^ {- 1} \mu (\mathrm {d} \left(g ^ {\prime} g\right)) = H _ {\text {e f f e c t i v e}}. \tag {32}
$$

Here, we have used the property of the Haar measure that  $\mu (\mathrm{d}(g^{\prime}g)) = \mu (\mathrm{d}g)$

It may not be easy to apply elements from the symmetry group  $G$  randomly. Still, in our learning protocol, we will only enforce symmetries that are either  $\mathrm{U}(1)$  or  $\mathrm{U}(1) \times \mathrm{U}(1) \times \dots \times \mathrm{U}(1) = U(1)^{\times N}$ , where sampling can easily be done for each  $\mathrm{U}(1)$  group separately.

We also remark that oftentimes one does not need to implement  $g$  very precisely, and our protocol is robust against certain types of errors in the implementation. To see this, let us consider the case where we would like to enforce a particle number conservation on site  $i$ , by applying a series of random phase shifts  $e^{-i\theta n_i}$  for random  $\theta \sim \mathcal{U}([- \pi, \pi])$  so that the effective Hamiltonian is

$$
H _ {\text {e f f e c t i v e}} = \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} \mathrm {d} \theta e ^ {i \theta n _ {i}} H e ^ {- i \theta n _ {i}}.
$$

Now consider if every time we want to apply  $e^{-i\theta n_i}$  we actually get  $e^{-i(\theta + \Delta \theta)n_i}$  with a random Gaussian error  $\Delta \theta \sim \mathcal{N}(\mu, \sigma^2)$  in the rotation angle, then the actual effective Hamiltonian will be

$$
\begin{array}{l} H _ {\text {e f f e c t i v e}} ^ {\prime} = \frac {1}{2 \pi \sqrt {2 \sigma^ {2}}} \int_ {- \infty} ^ {\infty} d \Delta \theta e ^ {- \frac {(\Delta \theta - \mu) ^ {2}}{2 \sigma^ {2}}} \int_ {- \pi} ^ {\pi} d \theta e ^ {i (\theta + \Delta \theta) n _ {i}} H e ^ {- i (\theta + \Delta \theta) n _ {i}} \\ = \frac {1}{\sqrt {2 \sigma^ {2}}} \int_ {- \infty} ^ {\infty} d \Delta \theta e ^ {- \frac {(\Delta \theta - \mu) ^ {2}}{2 \sigma^ {2}}} e ^ {i \Delta \theta n _ {i}} H _ {\text {e f f e c t i v e}} e ^ {- i \Delta \theta n _ {i}}. \\ \end{array}
$$

We will show that  $H_{\mathrm{effective}}' = H_{\mathrm{effective}}$ . First, we note that

$$
e ^ {i \Delta \theta n _ {i}} H _ {\mathrm {e f f e c t i v e}} e ^ {- i \Delta \theta n _ {i}} = H _ {\mathrm {e f f e c t i v e}}.
$$

Therefore, integrating the left-hand side with the Gaussian distribution for  $\Delta \theta$  (or in fact any other distribution) results in the same  $H_{\mathrm{effective}}$ . From this, we can see that having a potentially large error  $\Delta \theta$  (large both in its magnitude and in its uncertainty) in the phase shift does not affect the result at all. This argument is also true for random beam splitters.

# Data availability

The data supporting the findings of this study are available from the corresponding author upon reasonable request.

# Code availability

The code supporting the findings of this study are available from the corresponding author upon reasonable request.

Received: 24 January 2024; Accepted: 26 August 2024

Published online: 11 September 2024

# References

1. de Burgh, M. & Bartlett, S. D. Quantum methods for clock synchronization: Beating the standard quantum limit without entanglement. Phys. Rev. A 72, 042301 (2005).  
2. Valencia, A., Scarcelli, G. & Shih, Y. Distant clock synchronization using entangled photon pairs. Appl. Phys. Lett. 85, 2655-2657 (2004).

3. Leibfried, D. et al. Toward heisenberg-limited spectroscopy with multiparticle entangled states. Science 304, 1476-1478 (2004).  
4. Bollinger, J. J., Itano, W. M., Wineland, D. J. & Heinzen, D. J. Optimal frequency measurements with maximally correlated states. Phys. Rev. A 54, R4649 (1996).  
5. Lee, H., Kok, P. & Dowling, J. P. A quantum Rosetta stone for interferometry. J. Mod. Opt. 49, 2325-2338 (2002).  
6. McKenzie, K., Shaddock, D. A., McClelland, D. E., Buchler, B. C. & Lam, P. K. Experimental demonstration of a squeezing-enhanced power-recycled michelson interferometer for gravitational wave detection. Phys. Rev. Lett. 88, 231102 (2002).  
7. Holland, M. & Burnett, K. Interferometric detection of optical phase shifts at the heisenberg limit. Phys. Rev. Lett. 71, 1355 (1993).  
8. Wineland, D. J., Bollinger, J. J., Itano, W. M., Moore, F. & Heinzen, D. J. Spin squeezing and reduced quantum noise in spectroscopy. Phys. Rev. A 46, R6797 (1992).  
9. Caves, C. M. Quantum-mechanical noise in an interferometer. Phys. Rev. D. 23, 1693 (1981).  
10. Wiebe, N., Granade, C., Ferrie, C. & Cory, D. Quantum hamiltonian learning using imperfect quantum resources. Phys. Rev. A 89, 042314 (2014).  
11. Wiebe, N., Granade, C., Ferrie, C. & Cory, D. G. Hamiltonian learning and certification using quantum resources. Phys. Rev. Lett. 112, 190501 (2014).  
12. Li, Z., Zou, L. & Hsieh, T. H. Hamiltonian tomography via quantum quench. Phys. Rev. Lett. 124, 160502 (2020).  
13. Che, L. et al. Learning quantum hamiltonians from single-qubit measurements. Phys. Rev. Res. 3, 023246 (2021).  
14. Haah, J., Kothari, R. & Tang, E. Learning quantum Hamiltonians from high-temperature Gibbs states and real-time evolutions. Nat. Phys. 20, 1027-1031 (2024).  
15. Yu, W., Sun, J., Han, Z. & Yuan, X. Practical and efficient Hamiltonian learning. Quantum 7, 1045 (2023).  
16. Hangleiter, D., Roth, I., Eisert, J. & Roushan, P. Precise hamiltonian identification of a superconducting quantum processor. Preprint at https://arxiv.org/abs/2108.08319 (2021).  
17. Franca, D. S., Markovich, L. A., Dobrovitski, V., Werner, A. H. & Borregaard, J. Efficient and robust estimation of many-qubit hamiltonians. Preprint at https://arxiv.org/abs/2205.09567 (2022).  
18. Zubida, A., Yitzhaki, E., Lindner, N. H. & Bairey, E. Optimal short-time measurements for hamiltonian learning. Preprint at https://arxiv.org/abs/2108.08824 (2021).  
19. Bairey, E., Arad, I. & Lindner, N. H. Learning a local hamiltonian from local measurements. Phys. Rev. Lett. 122, 020504 (2019).  
20. Bairey, E., Guo, C., Poletti, D., Lindner, N. H. & Arad, I. Learning the dynamics of open quantum systems from their steady states. N. J. Phys. 22, 032001 (2020).  
21. Granade, C. E., Ferrie, C., Wiebe, N. & Cory, D. G. Robust online hamiltonian learning. N. J. Phys. 14, 103013 (2012).  
22. Gu, A., Cincio, L. & Coles, P.J. Practical Hamiltonian learning with unitary dynamics and Gibbs states. Nat Commun. 15, 312 (2024).  
23. Wilde, F. et al. Scalably learning quantum many-body hamiltonians from dynamical data. Preprint at https://arxiv.org/abs/2209.14328 (2022).  
24. Krastanov, S., Zhou, S., Flammia, S. T. & Jiang, L. Stochastic estimation of dynamical variables. Quantum Sci. Technol. 4, 035003 (2019).  
25. Boulant, N., Havel, T. F., Pravia, M. A. & Cory, D. G. Robust method for estimating the Lindblad operators of a dissipative quantum process from measurements of the density operator at multiple time points. Phys. Rev. A 67, 042322 (2003).  
26. Innocenti, L., Banchi, L., Ferraro, A., Bose, S. & Paternostro, M. Supervised learning of time-independent Hamiltonians for gate design. N. J. Phys. 22, 065001 (2020).

27. Ben Av, E., Shapira, Y., Akerman, N. & Ozeri, R. Direct reconstruction of the quantum-master-equation dynamics of a trapped-ion qubit. Phys. Rev. A 101, 062305 (2020).  
28. Shulman, M. D. et al. Suppressing qubit dephasing using real-time Hamiltonian estimation. Nat. Commun. 5, 5156 (2014).  
29. Sheldon, S., Magesan, E., Chow, J. M. & Gambetta, J. M. Procedure for systematically tuning up cross-talk in the cross-resonance gate. Phys. Rev. A 93, 060302 (2016).  
30. Sundaresan, N. et al. Reducing Unitary and Spectator Errors in Cross Resonance with Optimized Rotary Echoes. PRX Quantum 1, 020318 (2020).  
31. Verdon, G., Marks, J., Nanda, S., Leichenauer, S. & Hiday, J. Quantum Hamiltonian-based models and the variational quantum thermalizer algorithm. Preprint at https://arxiv.org/abs/1910.02071 (2019).  
32. Burgarth, D. & Ajoy, A. Evolution-Free Hamiltonian Parameter Estimation through Zeeman Markers. Phys. Rev. Lett. 119, 030402 (2017).  
33. Wang, J. et al. Experimental quantum hamiltonian learning. Nat. Phys. 13, 551-555 (2017).  
34. Kwon, H. Y. et al. Magnetic Hamiltonian parameter estimation using deep learning techniques. Sci. Adv. 6, eabb0872 (2020).  
35. Wang, D. et al. Machine Learning Magnetic Parameters from Spin Configurations. Adv. Sci. 7, 2000566 (2020).  
36. Huang, H.-Y., Kueng, R. & Preskill, J. Predicting many properties of a quantum system from very few measurements. Nat. Phys. 16, 1050-1057 (2020).  
37. Caro, M. C. Learning quantum processes and Hamiltonians via the Pauli transfer matrix. ACM Trans. Quantum Comput. 5, 1-53 (2024).  
38. Möbus, T., Bluhm, A., Caro, M. C., Werner, A. H. & Rouzé, C. Dissipation-enabled bosonic hamiltonian learning via new information-propagation bounds. Preprint at https://arxiv.org/abs/2307.15026 (2023).  
39. Holzäpfel, M., Baumgratz, T., Cramer, M. & Plenio, M. B. Scalable reconstruction of unitary processes and hamiltonians. Phys. Rev. A 91, 042129 (2015).  
40. Higgins, B. L., Berry, D. W., Bartlett, S. D., Wiseman, H. M. & Pryde, G. J. Entanglement-free heisenberg-limited phase estimation. Nature 450, 393-396 (2007).  
41. Kimmel, S., Low, G. H. & Yoder, T. J. Robust calibration of a universal single-qubit gate set via robust phase estimation. Phys. Rev. A 92, 062315 (2015).  
42. Huang, H.-Y., Tong, Y., Fang, D. & Su, Y. Learning many-body hamiltonians with heisenberg-limited scaling. Phys. Rev. Lett. 130, 200403 (2023).  
43. Dutkiewicz, A., O'Brien, T. E. & Schuster, T. The advantage of quantum control in many-body Hamiltonian learning. Preprint at https://arxiv.org/abs/2304.07172 (2023).  
44. Krantz, P. et al. A quantum engineer's guide to superconducting qubits. Appl. Phys. Rev. 6, 021318 (2019).  
45. Clerk, A., Lehnert, K., Bertet, P., Petta, J. & Nakamura, Y. Hybrid quantum systems with circuit quantum electrodynamics. Nat. Phys. 16, 257-267 (2020).  
46. Blais, A., Grimsmo, A. L., Girvin, S. M. & Wallraff, A. Circuit quantum electrodynamics. Rev. Mod. Phys. 93, 025005 (2021).  
47. Wang, J., Sciarrino, F., Laing, A. & Thompson, M. G. Integrated photonic quantum technologies. Nat. Photonics 14, 273-284 (2020).  
48. Aspelmeyer, M., Kippenberg, T. J. & Marquardt, F. Cavity optomechanics. Rev. Mod. Phys. 86, 1391 (2014).  
49. Metcalfe, M. Applications of cavity optomechanics. Appl. Phys. Rev. 1, 031105 (2014).  
50. Blais, A., Huang, R.-S., Wallraff, A., Girvin, S. M. & Schoelkopf, R. J. Cavity quantum electrodynamics for superconducting electrical circuits: An architecture for quantum computation. Phys. Rev. A 69, 062320 (2004).

51. Clerk, A. A., Devoret, M. H., Girvin, S. M., Marquardt, F. & Schoelkopf, R. J. Introduction to quantum noise, measurement, and amplification. Rev. Mod. Phys. 82, 1155 (2010).  
52. Chamberland, C. et al. Building a fault-tolerant quantum computer using concatenated cat codes. PRX Quantum 3, 010329 (2022).  
53. Adhikari, R. X. Gravitational radiation detection with laser interferometry. Rev. Mod. Phys. 86, 121 (2014).  
54. Qin, W., Miranowicz, A. & Nori, F. Beating the 3 db limit for intracavity squeezing and its application to nondemolition qubit readout. Phys. Rev. Lett. 129, 123602 (2022).  
55. Dassonneville, R. et al. Dissipative stabilization of squeezing beyond 3 db in a microwave mode. PRX Quantum 2, 020323 (2021).  
56. Kronwald, A., Marquardt, F. & Clerk, A. A. Arbitrarily large steady-state bosonic squeezing via dissipation. Phys. Rev. A 88, 063833 (2013).  
57. Wiseman, H. & Milburn, G. Squeezing via feedback. Phys. Rev. A 49, 1350 (1994).  
58. Nguyen, N. H. et al. Digital quantum simulation of the schwinger model and symmetry protection with trapped ions. PRX Quantum 3, 020324 (2022).  
59. Halimeh, J. C., Lang, H., Mildenberger, J., Jiang, Z. & Hauke, P. Gauge-symmetry protection using single-body terms. PRX Quantum 2, 040311 (2021).  
60. See supplemental material for details of our protocol and the proof of the main results.  
61. Viola, L. & Lloyd, S. Dynamical suppression of decoherence in two-state quantum systems. Phys. Rev. A 58, 2733 (1998).  
62. Viola, L., Knill, E. & Lloyd, S. Dynamical decoupling of open quantum systems. Phys. Rev. Lett. 82, 2417 (1999).  
63. Hartmann, M. J., Brandao, F. G. & Plenio, M. B. Quantum many-body phenomena in coupled cavity arrays. *Laser Photonics Rev.* 2, 527-556 (2008).  
64. Porras, D. & Cirac, J. I. Bose-einstein condensation and strong-correlation behavior of phonons in ion traps. Phys. Rev. Lett. 93, 263602 (2004).  
65. Shen, C., Zhang, Z. & Duan, L.-M. Scalable implementation of boson sampling with trapped ions. Phys. Rev. Lett. 112, 050504 (2014).  
66. Watrous, J. The theory of quantum information (Cambridge University Press, 2018).  
67. Ni, H., Li, H. & Ying, L. On low-depth algorithms for quantum phase estimation. Quantum 7, 1165 (2023).  
68. Jaynes, E. T. & Cummings, F. W. Comparison of quantum and semiclassical radiation theories with application to the beam maser. Proc. IEEE 51, 89-109 (1963).  
69. Kuwahara, T., Van Vu, T. & Saito, K. Optimal light cone and digital quantum simulation of interacting bosons. Preprint at https://arxiv.org/abs/2206.14736 (2022).  
70. Bakshi, A., Liu, A., Moitra, A. & Tang, E. Structure learning of Hamiltonians from real-time evolution. Preprint at https://arxiv.org/abs/2405.00082 (2024).  
71. Zhou, S., Zhang, M., Preskill, J. & Jiang, L. Achieving the heisenberg limit in quantum metrology using quantum error correction. Nat. Commun. 9, 78 (2017).  
72. Qian, T., Bringewatt, J., Boettcher, I., Bienias, P. & Gorshkov, A. V. Optimal measurement of field properties with quantum sensor networks. Phys. Rev. A 103, L030601 (2021).  
73. Bringewatt, J., Boettcher, I., Niroula, P., Bienias, P. & Gorshkov, A. V. Protocols for estimating multiple functions with quantum sensor networks: Geometry and performance. Phys. Rev. Res. 3, 033011 (2021)  
74. Ehrenberg, A., Bringewatt, J. & Gorshkov, A. V. Minimum entanglement protocols for function estimation. Preprint at https:// arxiv.org/abs/2110.07613 (2021).  
75. Heeres, R. W. et al. Cavity state manipulation using photon-number selective phase gates. Phys. Rev. Lett. 115, 137002 (2015).  
76. McKay, D. C., Wood, C. J., Sheldon, S., Chow, J. M. & Gambetta, J. M. Efficient Zgates for quantum computing. Phys. Rev. A 96, 022330 (2017).

77. Dur, W., Skotiniotis, M., Fröwis, F. & Kraus, B. Improved quantum metrology using quantum error correction. Phys. Rev. Lett. 112, 080801 (2014).  
78. Arrad, G., Vinkler, Y., Aharonov, D. & Retzker, A. Increasing sensing resolution with error correction. Phys. Rev. Lett. 112, 150801 (2014).  
79. Kessler, E. M., Lovchinsky, I., Sushkov, A. O. & Lukin, M. D. Quantum error correction for metrology. Phys. Rev. Lett. 112, 150802 (2014).  
80. Herrera-Martí, D. A., Gefen T., Aharonov, D., Katz, N. & Retzker A. Quantum error-correction-enhanced magnetometer overcoming the limit imposed by relaxation. *Phy. Rev. Lett.* 115, 200501 (2015).  
81. Sekatski, P., Skotiniotis, M., Kołodyński, J. & Dür, W. Quantum metrology with full and fastquantum control. Quantum 1, 27 (2017).  
82. Demkowicz-Dobrzański, R., Czajkowski, J. & Sekatski, P. Adaptive quantum metrology under general markovian noise. *Phy. Rev. X* 7, 041009 (2017).  
83. Hainzer, H., Kiesenhofer, D., Ollikainen, T., Bock, M., Kranzl, F., Joshi, M. K., Yoeli, G., Blatt, R., Gefen, T. & Roos, C. F. Correlation spectroscopy with multiquubit-enhanced phase estimation. Phys. Rev. X 14, 011033 (2024).

# Acknowledgements

Y.T. acknowledges funding from the U.S. Department of Energy Office of Science, Office of Advanced Scientific Computing Research (DE-NA0003525 and DE-SC0020290). Work supported by DE-SC0020290 is supported by the DOE QuantISED program through the theory consortium "Intersections of QIS and Theoretical Particle Physics" at Fermilab. The Institute for Quantum Information and Matter is an NSF Physics Frontiers Center. The work of H.L. and L.Y. is partially supported by the National Science Foundation under awards DMS-2011699 and DMS-2208163. T.G. acknowledges funding provided by the Institute for Quantum Information and Matter and the Quantum Science and Technology Scholarship of the Israel Council for Higher Education.

# Author contributions

H.L. and Y.T. contributed equally to this work. H.L., Y.T., H.N., and L.Y. designed the learning protocol and wrote the mathematical proof. T.G. and

Y.T. conducted the numerical experiments and T.G. performed the corresponding theoretical analysis. L.Y. supervised this project.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41534-024-00881-2.

Correspondence and requests for materials should be addressed to Lexing Ying.

Reprints and permissions information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

© The Author(s) 2024