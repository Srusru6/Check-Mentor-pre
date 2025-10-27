# Groverian measure of entanglement for mixed states

Daniel Shapira, Yishai Shimoni, and Ofer Biham  
Racah Institute of Physics, The Hebrew University, Jerusalem 91904, Israel  
(Received 18 March 2005; revised manuscript received 27 February 2006; published 5 April 2006)

The Groverian entanglement measure, introduced earlier for pure quantum states of multiple qubits [O. Biham, M.A. Nielsen, and T. Osborne, Phys. Rev. A 65, 062312 (2002)], is generalized to the case of mixed states. The Groverian measure of a mixed state of  $n$  qubits is obtained by a purification procedure into a pure state of  $2n$  qubits, followed by an optimization process, before the resulting state is fed into Grover's search algorithm. It is expressed in terms of the maximal success probability of the algorithm and in this sense provides an operational measure of entanglement.

DOI: 10.1103/PhysRevA.73.044301

PACS number(s): 03.67.Lx, 89.70.+c

The potential speedup offered by quantum computers is exemplified by Shor's factoring algorithm [1], Grover's search algorithm [2,3], and algorithms for quantum simulation [4]. Although the origin of this speed-up is not fully understood, there are indications that quantum entanglement plays a crucial role in making quantum algorithms efficient [5,6]. In particular, it was shown that quantum algorithms that do not create entanglement can be simulated efficiently on a classical computer [7]. It is therefore of interest to quantify the entanglement produced by quantum algorithms and examine its correlation with their efficiency. This requires developing measures of entanglement, suitable for quantum states of multiple qubits, such as those which appear in quantum algorithms. These include pure states as well as mixed states, which inevitably appear when decoherence effects are taken into account.

The special case of bipartite entanglement has been studied extensively in recent years and suitable entanglement measures were introduced. It was established that bipartite entanglement can be considered as a resource for teleportation [8]. The entanglement of bipartite pure states can be evaluated by the von Neumann entropy of the reduced density matrix, traced over one of the parties. For bipartite mixed states, several measures were proposed [9-11] and for the special case of states of two qubits an exact formula for the entanglement of formation was obtained [12,13]. For mixed states of multiple qubits, entanglement measures based on distance measures in Hilbert space were proposed [14-16].

Consider a mixed quantum state  $\rho$  of  $n$  qubits. The state is nonentangled, or separable, if its density matrix can be written in the form  $\rho = \Sigma_{\mu}P_{\mu}\rho_{\mu}^{1}\otimes \dots \otimes \rho_{\mu}^{n}$ , where  $\rho_{\mu}^{k}$ ,  $k = 1,\ldots ,n$  is a density operator of a pure state of the  $k$ th qubits, namely  $\rho_{\mu}^{k} = |\psi_{\mu}^{k}\rangle \langle \psi_{\mu}^{k}|$  and  $\Sigma_{\mu}P_{\mu} = 1$ . In the special case that  $\rho$  is a pure state, all probabilities vanish except for  $P_{1} = 1$ , and the state can be expressed by  $|\psi \rangle = |\psi^1\rangle \otimes \dots \otimes |\psi^n\rangle$ . Such states are called tensor-product states. In order to evaluate the entanglement of a quantum state,  $\rho$ , one needs a scalar function  $E(\rho)$  [or  $E(\psi)$  for pure states], called an entanglement measure, that satisfies [14-18] (a)  $E(\rho) = 0$  if and only if  $\rho$  is a separable state; (b) assuming that each qubit is held by a different party, it is not possible to increase  $E(\rho)$  by local operations and classical communication (LOCC) between

the parties. Consider the special case of local unitary operators. Such operators cannot decrease  $E(\rho)$  because if they could then the inverse operators (which are also unitary) would increase it and thus contradict the second condition above. The conclusion is that local unitary operators cannot change  $E(\rho)$ .

The Groverian entanglement measure,  $G(\psi)$ , defined for pure states of multiple qubits, is expressed in terms of the success probability of Grover's search algorithm when the state  $|\psi\rangle$  is used as the initial state [19]. A preprocessing stage is allowed in which an arbitrary local unitary operator is applied to each qubit. These operators are optimized in order to obtain the maximal success probability of the algorithm,  $P_{\max}(\psi)$ . The Groverian measure is given by  $G(\psi) = \sqrt{1 - P_{\max}(\psi)}$ .

In this paper we generalize the Groverian entanglement measure to the case of mixed states. The Groverian measure,  $G(\rho)$ , of a given mixed state  $\rho$ , of  $n$  qubits, is obtained by its purification into a pure state of  $2n$  qubits. An optimization procedure based on Uhlmann's theorem [20] is then applied before the resulting pure state is fed into Grover's algorithm.  $G(\rho)$  is then expressed in terms of the maximal success probability  $P_{\mathrm{max}}(\rho)$ , as described above for pure states. It is noted that  $G(\rho)$  vanishes for separable (mixed) states, and is therefore an entanglement measure, and not merely a monotone.

Consider Grover's search algorithm on a search space  $D$  containing  $N$  elements, where, for convenience,  $N = 2^n$  and  $n$  is an integer. This way, the elements of  $D$  can be represented by an  $n$ -qubit register  $|x\rangle = |x_1,x_2,\dots ,x_n\rangle$ , with the computational basis states  $|i\rangle$ ,  $i = 0,\ldots ,N - 1$ . We assume that one element in the search space is marked, namely it is the solution of the search problem. The distinction between the marked and unmarked elements is expressed by a suitable function,  $f:D\to \{0,1\}$ , such that  $f = 1$  for the marked element, and  $f = 0$  for the rest. The search for the marked element now becomes a search for the element for which  $f = 1$ . To solve this problem on a classical computer one needs to evaluate  $f$  for each element, one by one, until a marked state is found. Thus, on average,  $N / 2$  evaluations of  $f$  are required and  $N$  in the worst case. For a quantum computer, on which  $f$  is evaluated coherently, it was shown that a sequence of unitary operations, called Grover's algorithm and denoted by  $U_{G}$ , can locate the marked element using only  $O(\sqrt{N})$  coherent queries of  $f$  [2,3].

Starting with the equal superposition state,  $|\eta \rangle = \Sigma |i\rangle /\sqrt{N}$  and applying the operator  $U_{G}$  one obtains  $U_{G}|\eta \rangle = |m\rangle$ $+O(1 / N)$  , where  $|m\rangle$  is the marked state. Thus, the success probability of the algorithm is almost unity [2,3]. With this performance, Grover's algorithm was shown to be optimal [21] namely, it is as efficient as theoretically possible [22]. The adjoint equation takes the form

$$
\langle \eta | = \langle m | U _ {G} + O (1 / N), \tag {1}
$$

where the error is due to the discreteness of the Grover iterations [23]. If an arbitrary pure state,  $|\psi \rangle$ , is used as the initial state instead of the state  $|\eta \rangle$ , the success probability is reduced [24-26], and is given by  $|\langle m|U_G|\psi \rangle|^2 + O(1 / N)$ . Using Eq. (1) we obtain  $P_{s}(\psi) = |\langle \eta |\psi \rangle |^{2} + O(1 / N)$ , namely, the success probability is determined by the overlap between  $|\psi \rangle$  and  $|\eta \rangle$ .

Consider Grover's search algorithm, in which an arbitrary pure state  $|\psi \rangle$  is used as the initial state. Before applying the operator  $U_{G}$ , there is a preprocessing stage in which arbitrary local unitary operators,  $U_{1}, U_{2}, \ldots, U_{n}$ , are applied on the  $n$  qubits in the register. These operators are chosen such that the success probability of the algorithm would be maximized. The maximal success probability is thus given by  $P_{\max}(\psi) = \max |\langle m|U_G(U_1 \otimes \dots \otimes U_n)|\psi \rangle|^2$ , where the maximization is over the local unitaries  $U_{1}, U_{2}, \ldots, U_{n}$ . Using Eq. (1), this can be rewritten as  $P_{\max}(\psi) = \max |\langle \eta |U_1 \otimes \dots \otimes U_n|\psi \rangle|^2$  or as  $P_{\max}(\psi) = \max_{|\phi \rangle \in T}|\langle \phi |\psi \rangle|^2$ , where  $T$  is the space of all tensor product states of the form  $|\phi \rangle = |\phi_1\rangle \otimes \dots \otimes |\phi_n\rangle$ . The Groverian measure is given by [19]

$$
G (\psi) = \sqrt {1 - P _ {\max } (\psi)}. \tag {2}
$$

For the case of pure states, for which  $G(\psi)$  is defined, it is closely related to an entanglement measure introduced in Refs. [14-16], where  $\langle \phi | \psi \rangle$  is replaced by the fidelity. This measure was shown to be an entanglement monotone both for pure and for mixed states. It can be interpreted as the distance between the given state and the nearest separable state and expressed in terms of the fidelity of the two states. Based on these results, it was shown [19] that  $G(\psi)$  satisfies (a)  $G(\psi) \geq 0$ , with equality only when  $|\psi \rangle$  is a product state; (b)  $G(\psi)$  cannot be increased using local operations and classical communication (LOCC). Therefore,  $G(\psi)$  is an entanglement measure for pure states. A related result was obtained in Ref. [27], where it was shown that the evolution of the quantum state during the iteration of Grover's algorithm corresponds to the shortest path in Hilbert space using a suitable metric.

The operational interpretation that relates  $G(\psi)$  to the success probability of a quantum algorithm cannot be directly generalized to the case of mixed states. This is due to the fact that the resulting measure does not satisfy the conditions for an entanglement monotone [19]. The difficulty is that the operational interpretation given here amounts to finding the overlap of the initial state with the nearest product state. To make an entanglement monotone for mixed states, one needs to use the fidelity, which essentially evaluates the overlap of the initial state with the nearest separable state [14-16].

To obtain the Groverian measure,  $G(\rho)$ , for a mixed state

$\rho$  of  $n$  qubits, we introduce a pure state  $|\psi \rangle$  of  $2n$  qubits, which is a purification of  $\rho$ . Similarly,  $|\phi \rangle$  is a purification of a separable mixed state  $\sigma$ . As in the case of pure states, we introduce a preprocessing stage before the state is inserted into Grover's algorithm. During preprocessing an optimization is performed over a certain class of unitary operators  $U_{\phi}$ , which apply in the space of  $2n$  qubits. These operators satisfy  $|\phi \rangle = U_{\phi}^{\dagger}|\eta \rangle$ , where  $|\phi \rangle$  is a purification of a separable state  $\sigma$  of  $n$  qubits. These operators cannot be expressed as a tensor product of local unitary operators. This is due to the fact that a pure state,  $|\phi \rangle$ , of  $2n$  qubits, which is a purification of a mixed state  $\sigma$ , of  $n$  qubits, is not, in general, a product state. When the preprocessing is followed by Grover's search algorithm (still in the space of  $2n$  qubits), the maximal success probability is given by  $P_{\max}(\rho) = \max_{\sigma \in S} \max_{|\phi\rangle} \max_{|\psi\rangle} |\langle m|U_G U_\phi|\psi\rangle|^2$ . Using Eq. (1) we obtain  $P_{\max}(\rho) = \max_{\sigma \in S} \max_{|\phi\rangle} \max_{|\psi\rangle} |\langle \eta|U_\phi|\psi\rangle|^2$ , where  $S$  is the set of separable states of  $n$  qubits. The maximization is over all separable states  $\sigma$  of  $n$  qubits, and for each of them, over all possible purifications  $|\phi\rangle$  of  $2n$  qubits. This can be rewritten as

$$
P _ {\max } (\rho) = \max  _ {| \phi \rangle} \max  _ {| \psi \rangle} | \langle \phi | \psi \rangle | ^ {2}. \tag {3}
$$

The first maximization is over all possible states  $|\phi \rangle$  of  $2n$  qubits which are purifications of separable states  $\sigma$  of  $n$  qubits. The second maximization is over all states  $|\psi \rangle$  of  $2n$  qubits which are purifications of  $\rho$ . According to Uhlmann's theorem, the fidelity of any two states  $\rho$  and  $\sigma$  of  $n$  qubits satisfies  $F^2 (\rho ,\sigma) = \max_{|\phi \rangle}\max_{|\psi \rangle}|\langle \phi |\psi \rangle |^2$ , where  $|\phi \rangle$  and  $|\psi \rangle$ , of  $2n$  qubits, are purifications of  $\rho$  and  $\sigma$ , respectively [20]. Note that  $P_{\mathrm{max}}(\rho) = F^{2}(\rho ,\sigma)$ . A useful corollary (presented in Exercise 9.15 on p. 411 of Ref. [4]) enables us to remove the optimization on  $|\psi \rangle$ , leading to  $F^2 (\rho ,\sigma) = \max_{|\phi \rangle}|\langle \phi |\psi \rangle |^2$ , where  $|\psi \rangle$  is an arbitrary purification of  $\rho$ . Using this corollary we find that

$$
G (\rho) = \sqrt {1 - \max  _ {\sigma \in S} F ^ {2} (\rho , \sigma)}. \tag {4}
$$

To prove that the conditions for an entanglement monotone are satisfied, we introduce a complete set of operators, defined by  $\{M_i\}_{i=1}^m$ , where  $M_i = M_i(1) \otimes \dots \otimes M_i(n)$  and  $\sum_{i=1}^m M_i M_i^\dagger = I$ . In this notation, the conditions are that  $G(\rho) = 0$  only for separable states, and that for every density matrix  $\rho$ ,

$$
G \left(\sum_ {i = 1} ^ {m} M _ {i} \rho M _ {i} ^ {\dagger}\right) \leqslant G (\rho). \tag {5}
$$

As shown in Refs. [14-16], functions of the form of  $G(\psi)$  satisfy the conditions for an entanglement monotone. More specifically, there exists two specific purifications,  $|\phi_0\rangle$  and  $|\psi_0\rangle$ , for which  $F^2 (\rho ,\sigma) = |\langle \phi_0|\psi_0\rangle |^2$ . Thus,  $G(\rho) = 0$  if and only if  $F^{2}(\rho ,\sigma) = 1$ . In this case  $|\langle \phi_0|\psi_0\rangle |^2 = 1$ , or  $|\phi_0\rangle = e^{i\alpha}|\psi_0\rangle$ , thus  $\rho = \sigma$ . Since  $\sigma$  is separable then so is  $\rho$ , and the first condition is satisfied.

To prove that the second condition is satisfied we use the monotonicity of the fidelity under trace preserving operations [4]. This means that for every complete set of operators

$F(\rho, \sigma) \leqslant F(\Sigma_i M_i \rho M_i^\dagger, \Sigma_i M_i \sigma M_i^\dagger)$ , where the separable state  $\sigma$  remains separable under the transformation. As a result,

$$
\max  _ {\sigma \in S} F (\rho , \sigma) \leqslant \max  _ {\sigma \in S} F \left(\sum_ {i} M _ {i} \rho M _ {i} ^ {\dagger}, \sigma\right). \tag {6}
$$

Therefore,  $G(\rho)$  cannot increase under such transformations.

Consider a mixed state  $\sigma$  of  $n$  qubits. The state  $\sigma$  can be purified into a pure state of  $2n$  qubits, half of them associated with the original subspace  $Q$  and the rest with the added subspace  $R$  [4]. Such purification takes the form  $|\phi \rangle = (U_R \otimes \sqrt{\sigma} U_Q)\Sigma_i|i_R\rangle|i_Q\rangle$ , where  $\{|i_R\rangle\}$  and  $\{|i_Q\rangle\}$  are orthonormal basis states and  $U_R$  and  $U_Q$  are unitary operators, in  $R$  and  $Q$ , respectively.

For any separable mixed state,  $\sigma$  of  $n$  qubits, the unitary operators  $U_{R}$  and  $U_{Q}$  and the operator  $\sqrt{\sigma}$  provide a convenient parametrization of the pure state  $|\phi\rangle$ . This follows from the fact that the density matrix of a separable state can also be expressed as  $\sigma = \sum_{\mu} \sigma_{\mu}^{1} \otimes \dots \otimes \sigma_{\mu}^{n}$ , where  $\sigma_{\mu}^{k}$ ,  $k = 1, \ldots, n$  is the density operator of a mixed state of the  $k$ th qubit. To obtain the operator  $\sqrt{\sigma}$ , one needs to diagonalize  $\sigma$ , according to  $V \sigma V^{\dagger} = D$ , where  $V$  is a suitable unitary operator, resulting in a diagonal matrix  $D$ . Taking its square root one obtains another diagonal matrix  $d$  with matrix elements  $d_{ii} = \sqrt{D_{ii}}$ . The process is completed by  $\sqrt{\sigma} = V^{\dagger} dV$ . The operator  $\sqrt{\sigma}$  is not a required to be unitary and is not used in the quantum circuit.

In order to complete the construction of the quantum circuit, one needs the operator  $U_{\phi}^{\dagger}$  that transforms  $|\eta\rangle$  into a purification  $|\phi\rangle$  of a separable state  $\sigma$ . To this end we construct two bases of the space spanned by  $2n$  qubits. The first basis is obtained from the computational basis,  $|i\rangle$  by applying the Hadamard transform on all qubits, namely  $|\eta_i\rangle = H^{\otimes 2n}|i\rangle$ . Note that  $|\eta_0\rangle = |\eta\rangle$ . The second basis,  $|\phi_i\rangle$ , can be constructed using the Gram-Schmidt algorithm, starting with  $|\phi_0\rangle = |\phi\rangle$ . The unitary operator  $U_{\phi}^{\dagger} = \Sigma_i|\phi_i\rangle \langle \eta_i|$  transforms the state  $|\eta\rangle$  into the state  $|\phi\rangle$ , which is a purification of a separable state,  $\sigma$ , of  $n$  qubits.

It might seem surprising that in order to evaluate the entanglement of an  $n$ -qubit system one needs a search space of  $2n$  qubits. This can be explained by considering mixed states as open systems, where, in some cases, the mixture represents an effective entanglement with external qubits. Purification of the mixed state  $\rho$  to  $2n$  qubits enables us to create a closed system with no entanglement to any external qubits, in which all the relevant information is maintained.

Quantum algorithms are designed to start with a well defined initial state. The final state, just before the measurement is taken, can be either a basis state or a superposition of basis states. For example, in Grover's algorithm with a single marked state, the desired final state (namely the marked state) is a basis state. In Grover's algorithm with several marked states, as well as in Shor's factoring algorithm, the desired final state is a superposition. The analysis presented

in this paper can be generalized by replacing Grover's algorithm by some other quantum algorithm. If in the replacement algorithm the desired final state is a basis state,  $G(\rho)$  will not depend on the specific algorithm. However, for algorithms such as Shor's algorithm, the maximal success probability may not coincide with the expression used in the Groverian measure. Yet, in the special case of Grover's algorithm with several marked states, the Groverian measure still holds [26].

Recently, the Groverian measure was applied in order to evaluate the entanglement in certain pure quantum states of multiple qubits [28]. A convenient parametrization was developed that enables analytical calculations of  $G(\psi)$  for some pure states of high symmetry. Using a numerical procedure, the entanglement of intermediate states, generated during the evolution of Grover's algorithm, was calculated. It was found that even if the initial state and the target state are product states, in intermediate stages of the algorithm, highly entangled states are generated, in agreement with earlier studies in which other measures were used [27,29]. This result is interesting in the context of attempts to examine the role of entanglement in quantum algorithms and specifically in Grover's search algorithm. In particular, recent studies have shown that an implementation of Grover's algorithm using classical media, namely, in which quantum entanglement does not play a role, would require an exponentially larger overhead compared to the quantum case [30,31].

Unlike the case of pure states of two qubits, multiple qubit states support a large number of different measures [27,29,32-34]. It seems that the issue of what measure is relevant depends on the specific physical or operational context in which it is used. In particular, the Groverian entanglement measure is motivated by a quantum algorithm. It thus appears to be a suitable measure for the evaluation of the entanglement that is produced during the evolution of quantum algorithms. The actual evaluation of entanglement measures turns out to be a difficult computational problem. This is due to the fact that these measures are typically defined as an extremum of some multivariable function. A singular result in this context is the explicit formula for the entanglement of formation of mixed states of two qubits, obtained in Refs. [12,13].

A related operational interpretation of the fidelity, which is also based on Uhlmann's theorem, was introduced in Ref. [35]. In that case the fidelity  $F(\rho, \sigma)$  of the output states of a noisy channel provides an upper bound on the overlap of the input states, under the assumption that they were pure.

The generalization of the Groverian measure to mixed states may provide further insight into the role of entanglement in making quantum algorithms powerful. It would be interesting to use this measure to evaluate the entanglement generated by quantum algorithms using mixed states, particularly when decoherence effects are taken into account.

[1] P. W. Shor, in Proceedings of the 35th Annual Symposium on the Foundations of Computer Science, edited by S. Goldwasser (IEEE Computer Society, Los Alamitos, CA, 1994), p. 124.  
[2] L. K. Grover, in Proceedings of the Twenty-Eighth Annual Symposium on the Theory of Computing (ACM, New York, 1996), p. 212.  
[3] L. K. Grover, Phys. Rev. Lett. 79, 325 (1997).  
[4] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, 2000).  
[5] R. Jozsa and N. Linden, Proc. R. Soc. London, Ser. A 459, 2011 (2003).  
[6] G. Vidal, Phys. Rev. Lett. 91, 147902 (2003).  
[7] D. Aharonov and M. Ben-Or, in Proceedings of the 37th Annual Symposium on the Foundations of Computer Science, edited by S. Goldwasser (IEEE Computer Society, Los Alamitos, 1996), p. 46.  
[8] C. H. Bennett, G. Brassard, C. Crepeau, R. Jozsa, A. Peres, and W. K. Wootters, Phys. Rev. Lett. 70, 1895 (1993).  
[9] C. H. Bennett, H. J. Bernstein, S. Popescu, and B. Schumacher, Phys. Rev. A 53, 2046 (1996).  
[10] C. H. Bennett, D. P. DiVincenzo, J. A. Smolin, and W. K. Wootters, Phys. Rev. A 54, 3824 (1996).  
[11] S. Popescu and D. Rohrlich, Phys. Rev. A 56, R3319 (1997).  
[12] S. Hill and W. K. Wootters, Phys. Rev. Lett. 78, 5022 (1997).  
[13] W. K. Wootters, Phys. Rev. Lett. 80, 2245 (1998).  
[14] V. Vedral, M. B. Plenio, M. A. Rippin, and P. L. Knight, Phys. Rev. Lett. 78, 2275 (1997).  
[15] V. Vedral and M. B. Plenio, Phys. Rev. A 57, 1619 (1998).  
[16] V. Vedral, M. B. Plenio, K. Jacobs, and P. L. Knight, Phys. Rev. A 56, 4452 (1997).  
[17] G. Vidal, J. Mod. Opt. 47, 355 (2000).  
[18] M. Horodecki, P. Horodecki, and R. Horodecki, Phys. Rev. Lett. 84, 2014 (2000).

[19] O. Biham, M. A. Nielsen, and T. J. Osborne, Phys. Rev. A 65, 062312 (2002).  
[20] A. Uhlmann, Rep. Math. Phys. 9, 273 (1976).  
[21] C. Zalka, Phys. Rev. A 60, 2746 (1999).  
[22] C. H. Bennett, E. Bernstein, G. Brassard, and U. Vazirani, SIAM J. Comput. 26, 1510 (1997).  
[23] D. Shapira, Y. Shimoni, and O. Biham, Phys. Rev. A 71, 042320 (2005).  
[24] D. Biron, O. Biham, E. Biham, M. Grassl, and D. A. Lidar, "Generalized Grover search algorithm for arbitrary initial amplitude distribution," in Proceedings of the 1st NASA International Conference on Quantum Computing and Quantum Communications, Palm Springs, California, February 17-20, 1998, Lecture Notes in Computer Science 1509, edited by C. P. Williams (Springer-Verlag, Berlin, 1998), p. 140.  
[25] E. Biham, O. Biham, D. Biron, M. Grassl, and D. A. Lidar, Phys. Rev. A 60, 2742 (1999).  
[26] O. Biham, D. Shapira, and Y. Shimoni, Phys. Rev. A 68, 022326 (2003).  
[27] A. Miyake and M. Wadati, Phys. Rev. A 64, 042317 (2001).  
[28] Y. Shimoni, D. Shapira, and O. Biham, Phys. Rev. A 69, 062303 (2004).  
[29] D. A. Meyer and N. R. Wallach, J. Math. Phys. 43, 4273 (2002).  
[30] S. Lloyd, Phys. Rev. A 61, 010301(R) (1999).  
[31] D. A. Meyer, Phys. Rev. Lett. 85, 2014 (2000).  
[32] T.-C. Wei and P. M. Goldbart, Phys. Rev. A 68, 042307 (2003).  
[33] H. Barnum and N. Linden, J. Phys. A 34, 6787 (2001).  
[34] T. C. Wei and P. M. Goldbart, Phys. Rev. A 68, 042307 (2003).  
[35] J. L. Dodd and M. A. Nielsen, Phys. Rev. A 66, 044301 (2002).