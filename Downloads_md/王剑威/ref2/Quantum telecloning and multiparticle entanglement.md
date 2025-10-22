# Quantum telecloning and multiparticle entanglement

M. Murao, $^{1}$  D. Jonathan, $^{1}$  M. B. Plenio, $^{1}$  and V. Vedral $^{2}$

<sup>1</sup>Optics Section, The Blackett Laboratory, Imperial College, London SW7 2BZ, United Kingdom

$^{2}$ Centre for Quantum Computing, Clarendon Laboratory, University of Oxford, Parks Road, Oxford OX1 3PU, United Kingdom (Received 24 June 1998)

A quantum telecloning process combining quantum teleportation and optimal quantum cloning from one input to  $M$  outputs is presented. The scheme relies on the establishment of particular multiparticle entangled states, which function as multiuser quantum information channels. The entanglement structure of these states is analyzed and shown to be crucial for this type of information processing. [S1050-2947(99)07301-1]

PACS number(s): 03.67.Hk, 89.70.+c

# I. INTRODUCTION

Quantum information-processing systems display many features that are unknown in the classical world. Well-known examples include teleportation [1], superdense coding [2], and the ability to support qualitatively different cryptographic and computational protocols [3,4]. Central to many of these applications is the existence of entanglement between a pair of distant quantum systems [5]. For instance, in the case of teleportation, the establishment of a maximally entangled state of two distant quantum bits (qubits) allows an arbitrary unknown one-qubit state to be conveyed from one distant party to another with perfect fidelity.

The consequences of multiparticle entanglement involving several distant parties have not yet been explored as extensively. An early application was the use of Greenberger-Horne-Zeilinger (GHZ) states to provide inequality-free tests of quantum mechanics versus local hidden-variable theories [6]. More recently, multiparticle correlations have been shown to decrease the communication complexity of certain calculations involving two parties (i.e., to reduce the amount of communication needed to realize a computation involving data from several distant parties) [7]. Recent developments also include state purification protocols for multiparticle systems [8], schemes for basic manipulation of multiparticle states via entanglement swapping [9], and quantum secret sharing [10].

Another important application of multiparticle entanglement is in distributed quantum computing [11], where several distant parties (Alice, Bob, Claire, etc.) share an initial entangled state and are asked to perform a given computational task using only local operations and classical communication. The problem is to find a protocol that completes the task with a given precision using the least possible resources (in particular, the minimum amount of initial nonlocal entanglement, which is an "expensive" resource).

In this paper we investigate the following scenario. Alice holds an unknown one-qubit quantum state  $|\phi \rangle$  and wishes to transmit identical copies of it to  $M$  associates (Bob, Claire, etc.). Of course, the quantum no-cloning theorem [12] implies that these copies cannot be perfect. The best Alice can do is to send optimal quantum clones of her state (the most faithful copies allowed by quantum mechanics [13-19]; see also Sec. II B), which we assume are sufficient for her pur

poses. The computational task Alice must perform is therefore to generate  $M$  optimal quantum clones of a one-qubit input and distribute them among distant parties.

The most straightforward protocol available to Alice would be to generate the optimal clones locally using an appropriate quantum network [14,16] and then teleport each one to its recipient by means of previously shared maximally entangled pairs. This would require  $M$  units of initial entanglement ( $e$ -bits), as well as the sending of  $M$  independent two-bit classical messages (one for each measurement result). It would also require Alice to run a computationally expensive local network involving several extra qubits and two-qubit operations. In contrast, as we shall see ahead, far cheaper strategies can be found [requiring only  $O(\log_2 M)$ $e$ -bits], provided Alice and her associates share particular multiparticle entangled states. In this case, it is possible to simultaneously convey all  $M$  copies by means of a single measurement on Alice's qubit. Alice only needs to publicly broadcast the two bits that determine her measurement result, after which each recipient performs an appropriate local rotation conditioned on this information. This "telecloning" is reminiscent of the well-known teleportation protocol of Bennett et al. [1]. Indeed, it can be seen as the natural generalization of teleportation to the many-recipient case.

At this point, we should note that a similar proposal for telecloning  $M = 2$  copies has been put forth by Bruß et al. [17]. In their case, however, the procedure is not directly scalable to  $M > 2$ . Moreover, the correct clones are obtained only after a deliberate discarding of information, by averaging over all the possible outcomes of a measurement. In contrast, the scheme we present, which is strongly based on the optimal cloning transformation given in [15], allows any number  $M$  of clones to be generated. The significant difference with respect to the scheme in [17] is the introduction of an ancilla, which makes the averaging procedure unnecessary.

Our work is organized as follows. In Sec. II we give a summary of relevant results concerning teleportation and optimal universal quantum cloning. In Sec. III we present our telecloning protocol. Section IV is devoted to analyzing the entanglement properties of the multiparticle telecloning states. Open questions raised by our study are discussed in Sec. V. Finally, in Sec. VI we present our conclusions.

# II. PRELIMINARIES

# A. Teleportation

The teleportation protocol [1] allows an unknown state  $|\phi \rangle_{X}$  of a quantum system  $X$  to be faithfully transmitted between two spatially separated parties (a sender, Alice, and a receiver, Bob). The essential steps of this procedure (say in the simplest case where  $X$  is a one-qubit system) are as follows. First and foremost, Alice and Bob must share a maximally entangled state of two qubits  $S$  (sender) and  $R$  (receiver), such as  $|\Phi^{+}\rangle = (1 / \sqrt{2})(|00\rangle_{SR} + |11\rangle_{SR})$ . Next Alice performs a joint measurement of the two-qubit system  $X \otimes S$  in the Bell basis:

$$
\left| \Phi^ {\pm} \right\rangle = \frac {1}{\sqrt {2}} \left(\left| 0 0 \right\rangle \pm \left| 1 1 \right\rangle\right), \tag {1}
$$

$$
\left| \Psi^ {\pm} \right\rangle = \frac {1}{\sqrt {2}} \left(\left| 0 1 \right\rangle \pm \left| 1 0 \right\rangle\right). \tag {2}
$$

Finally, Alice sends a two-bit message to Bob informing him of her measurement result. Bob then rotates his qubit using one of the unitary operators  $\mathbf{1}$ ,  $\sigma_z$ ,  $\sigma_x$ , or  $\sigma_y$ , according to whether Alice's result was respectively  $|\Phi^{+}\rangle$ ,  $|\Phi^{-}\rangle$ ,  $|\Psi^{+}\rangle$ , or  $|\Psi^{-}\rangle$ . The final state of Bob's qubit is then equal to the original state  $|\phi\rangle_X$ , regardless of the measurement result. This insensitivity to measurement results is the crucial property of the teleportation protocol and one that we shall also require for our telecloning scheme.

# B. Optimal universal quantum cloning

While teleportation aims to transmit quantum information faithfully, optimal cloning seeks to spread it among several parties in the most efficient way possible. The "no-cloning" theorem [12] prevents this spreading from being perfect; nevertheless, it is still reasonable to ask how accurately such copies can be made [13]. If the quality of the copies (measured, for instance, by their fidelity with respect to the original state  $|\phi \rangle_{X}$ ) is chosen to be independent of  $|\phi \rangle_{X}$ , then the answer is given by the so-called  $N\to M$  universal quantum cloning machines [15,18,19].

These "machines" are unitary transformations that transform  $N$  input systems, identically prepared in state  $|\phi \rangle_{X}$  onto  $M$  output systems ( $M \geqslant N$ ), each of which ends up in a mixed state described by the reduced density operator

$$
\rho_ {o u t} = \gamma | \phi \rangle_ {X} \langle \phi | + (1 - \gamma) | \phi^ {\perp} \rangle_ {X} \langle \phi^ {\perp} | \tag {3}
$$

(where  $|\phi^{\perp}\rangle_{X}$  is a state orthogonal to  $|\phi \rangle_X$ ) [15,16]. The fidelity factor  $\gamma$  of these imperfect copies has a definite upper limit imposed by quantum mechanics. In the case where each input system consists of one qubit, this optimal value is given by [15,18,19]

$$
\gamma = \frac {M (N + 1) + N}{M (N + 2)}. \tag {4}
$$

Unitary transformations that realize this bound have also been explicitly constructed [15]. In general, they involve the  $N$  "original" qubits,  $M - N$  "blank paper" qubits  $B$  (ini

tially prepared in some fixed state  $|0\cdots 0\rangle_B)$ , and an ancilla system  $A$  containing at least  $M - N + 1$  levels [15] (also initially in some fixed state  $|0\cdots 0\rangle_A$ ). In this paper we shall be mainly interested in the situation where only one original qubit  $X$  is available, that is,  $N = 1$ . In this case, the cloning transformation  $U_{1M}$  is defined as follows: For an initial state  $|\phi \rangle_X = a|0\rangle_X + b|1\rangle_X$ , we have

$$
U _ {1 M} \left(\left| \phi \right\rangle_ {X} \otimes \left| 0 \dots 0 \right\rangle_ {A} \mid 0 \dots 0 \right\rangle_ {B}) = a \left| \phi_ {0} \right\rangle_ {A C} + b \left| \phi_ {1} \right\rangle_ {A C}, \tag {5}
$$

where

$$
\begin{array}{l} | \phi_ {0} \rangle_ {A C} = U _ {1 M} | 0 \rangle_ {X} | 0 \dots 0 \rangle_ {A} | 0 \dots 0 \rangle_ {B} \\ = \sum_ {j = 0} ^ {M - 1} \alpha_ {j} | A _ {j} \rangle_ {A} \otimes | \{0, M - j \}, \{1, j \} \rangle_ {C}, \tag {6} \\ \end{array}
$$

$$
\begin{array}{l} \left| \phi_ {1} \right\rangle_ {A C} = U _ {1 M} \left| 1 \right\rangle_ {X} \left| 0 \dots 0 \right\rangle_ {A} \left| 0 \dots 0 \right\rangle_ {B} \\ = \sum_ {j = 0} ^ {M - 1} \alpha_ {j} \left| A _ {M - 1 - j} \right\rangle_ {A} \otimes \left| \{0, j \}, \{1, M - j \} \right\rangle_ {C}, \tag {7} \\ \end{array}
$$

$$
\alpha_ {j} = \sqrt {\frac {2 (M - j)}{M (M + 1)}}, \tag {8}
$$

and  $C$  denotes the  $M$  qubits holding the copies (originally the  $X$  and  $B$  qubits). Here  $|A_j\rangle_A$  are  $M$  orthogonal normalized states of the ancilla and  $|\{0,M - j\}, \{1,j\}\rangle$  denotes the symmetric and normalized state of  $M$  qubits where  $M - j$  of them are in state  $|0\rangle$  and  $j$  are in the orthogonal state  $|1\rangle$ . For example, for  $M = 3$  and  $j = 1$ ,

$$
\left| \{0, 2 \}, \{1, 1 \} \right\rangle = \frac {1}{\sqrt {3}} \left(\left| 0 0 1 \right\rangle + \left| 0 1 0 \right\rangle + \left| 1 0 0 \right\rangle\right). \tag {9}
$$

We note that, even though the minimum number of ancilla qubits required to support the  $M$  levels  $\left|A_j\right\rangle_A$  is of the order of  $\log_2 M$ , these can be more conveniently represented as the symmetrized states of  $M - 1$  qubits [15]:

$$
\left| A _ {j} \right\rangle_ {A} \equiv \left| \{0, M - 1 - j \}, \{1, j \} \right\rangle_ {A}. \tag {10}
$$

In this form, states  $|\phi_0\rangle$  and  $|\phi_1\rangle$  above become  $(2M - 1)$ -qubit states, obeying the simple symmetries

$$
\left. \sigma_ {z} \otimes \dots \otimes \sigma_ {z} \mid \phi_ {0} \right\rangle = \left| \phi_ {0} \right\rangle , \tag {11}
$$

$$
\sigma_ {z} \otimes \dots \otimes \sigma_ {z} | \phi_ {1} \rangle = - | \phi_ {1} \rangle , \tag {12}
$$

$$
\sigma_ {x} \otimes \dots \otimes \sigma_ {x} | \phi_ {0 (1)} \rangle = | \phi_ {1 (0)} \rangle . \tag {13}
$$

In other words, the states  $|\phi_i\rangle$  transform under simultaneous action of the Pauli operators on all  $2M - 1$  qubits just as a single qubit transforms under the corresponding single Pauli operator. We also note that these operations are strictly local, that is, factorized into a product of independent rotations on each qubit. As we will see in the next section, these local symmetries play a crucial role, allowing cloning to be realized remotely via multiparticle entanglement.

# III. QUANTUM TELECLONING

In this section we present a telecloning scheme that combines cloning and teleportation. This is accomplished as follows. Alice holds an (unknown) one-qubit state  $|\phi \rangle_{X}$  that she wishes to teleclone to M associates Bob, Claire, etc. We assume that they all share a multiparticle entangled state  $|\psi_{TC}\rangle$  as a starting resource. This state must be chosen so that, after Alice performs a local measurement and informs the other parties of its result, the latter can each obtain an optimal copy given by Eq. (3) using only local rotations.

A choice of  $\left|\psi_{TC}\right\rangle$  with these properties is the  $2M$ -qubit state

$$
\left| \psi_ {T C} \right\rangle = \left(\left| 0 \right\rangle_ {P} \otimes \left| \phi_ {0} \right\rangle_ {A C} + \left| 1 \right\rangle_ {P} \otimes \left| \phi_ {1} \right\rangle_ {A C}\right) / \sqrt {2}, \tag {14}
$$

where  $|\phi_0\rangle_{AC}$  and  $|\phi_1\rangle_{AC}$  are the optimal cloning states obtained in [15] and given by Eqs. (6) and (7). Here  $C$  denotes the  $M$  qubits that shall hold the copies, each of which is held by one of Alice's associates. For convenience, we shall refer to them collectively as the "receivers" (though it should be kept in mind that they may all be far away from each other).  $P$  represents a single qubit held by Alice, which we shall refer to as the "port" qubit. Finally,  $A$  denotes an  $(M - 1)$ -qubit ancilla, which for convenience we will also assume to be on Alice's side (even though, once again, each qubit may in reality be at a different location).

The tensor product of  $|\psi_{TC}\rangle$  with the unknown state  $|\phi \rangle_{X} = a|0\rangle_{X} + b|1\rangle_{X}$  held by Alice is a  $(2M + 1)$ -qubit state. Rewriting it in a form that singles out the Bell basis of qubits  $X$  and  $P$ , we get

$$
\begin{array}{l} \left| \psi \right\rangle_ {X P A C} = \left| \Phi^ {+} \right\rangle_ {X P} (a \left| \phi_ {0} \right\rangle_ {A C} + b \left| \phi_ {1} \right\rangle_ {A C}) / 2 \\ + \left| \Phi^ {-} \right\rangle_ {X P} \left(a \mid \phi_ {0} \right\rangle_ {A C} - b \mid \phi_ {1} \rangle_ {A C}) / 2 \\ + \left| \Psi^ {+} \right\rangle_ {X P} (b | \phi_ {0} \rangle_ {A C} + a | \phi_ {1} \rangle_ {A C}) / 2 \\ + \left| \Psi^ {-} \right\rangle_ {X P} \left(b \mid \phi_ {0} \right\rangle_ {A C} - a \mid \phi_ {1} \rangle_ {A C}) / 2. \tag {15} \\ \end{array}
$$

The telecloning of  $|\phi \rangle_X$  can now be accomplished by the following simple procedure.

(i) Alice performs a Bell measurement of qubits  $X$  and  $P$ , obtaining one of the four results  $|\Psi^{\pm}\rangle_{XP},|\Phi^{\pm}\rangle_{XP}$ . If the result is  $|\Phi^{+}\rangle_{XP}$ , then subsystem  $AC$  is projected precisely into the optimal cloning state given in Eq. (5). In this case, our task is accomplished.  
(ii) In case one of the other Bell states is obtained, we can still recover the correct state of  $AC$  by exploiting the symmetries of states  $|\phi_0\rangle_{AC}$  and  $|\phi_1\rangle_{AC}$  under the Pauli matrix operations [Eqs. (11)-(13)]. Specifically, if  $|\Phi^{-}\rangle_{XP}$  is obtained, we must perform  $\sigma_z$  on each of the  $2M - 1$  qubits in  $AC$ ; similarly, if  $|\Psi^{+}\rangle_{XP}$  or  $|\Psi^{-}\rangle_{XP}$  is obtained, they must all be rotated by  $\sigma_x$  and  $\sigma_x\sigma_z = i\sigma_y$ , respectively. This procedure is illustrated in Fig. 1 for the case of  $M = 2$  copies.

We stress that, apart from Alice's Bell measurement, only local one-qubit operations are required in this telecloning procedure. In this way, all of the qubits except the input  $X$  and the port  $P$  can be spatially separated from each other. It is also worthwhile to add that rotating the ancilla qubits in step (ii) above is not strictly necessary. The correct copy states of each output [given by Eq. (3)] are obtained at the

![](images/b68604b43edb15f8627935e99ed6da1e777054cf0364d41a4b651cfbe19bd883.jpg)  
FIG. 1. Quantum telecloning  $M = 2$  copies of an unknown one-qubit state. Alice and her associates Bob and Claire (the 'receivers') initially share a multiparticle entangled state [Eq. (14)] consisting of the qubits  $P$  (the "port"),  $A_0$  (the ancilla), and  $C_1$  and  $C_2$  (outputs, or "copy" qubits). The solid lines indicate the existence of entanglement between pairs of qubits when the remaining ones are traced out. Alice performs a Bell measurement of the port along with the input qubit  $X$ ; subsequently, the receivers perform appropriate rotations on the output qubits, obtaining two optimal quantum clones. Since these rotations are independent, each clone can be at a different location.

output regardless of these operations since local rotations on one qubit cannot affect another qubit's reduced density operator.

We thus see that, given the telecloning state in Eq. (14) and using only local operations and classical communication, we are able to optimally transfer information from one to several qubits. In the following section we study in detail the entanglement properties of this state that allow this to happen.

# IV. THE ENTANGLEMENT STRUCTURE OF THE TELECLONING STATE

The procedure we have described in the preceding section performs the same task as a unitary  $1 \to M$  cloning machine, but uses only local operations and classical communication. In the former case, information about the input state is conveyed to the output copies by means of global entangling operations (this is explicitly shown in the cloning network of Ref. [14]). In telecloning, the same transfer is realized through the multiparticle entanglement of the state in Eq. (14). In this section we investigate the structure of this entanglement. It is important to remark that at present there is no known way of uniquely quantifying the entanglement of a general multiparticle state [20]. For the purpose of understanding the flow of information in the telecloning procedure, we find it convenient to perform this analysis from two points of view, which we refer to as the "total" and "two-qubit" pictures. The first of these involves all  $2M$  particles (hence total) and refers to the entanglement between the  $M$  qubits on Alice's side (the port and ancilla) and the  $M$  on the receivers' side (the outputs); the second considers the entanglement of a single pair of qubits after tracing over all other qubits.

Let us first consider the total picture. We begin by rewriting the telecloning state so that the qubits on Alice's and the receivers' sides are explicitly separated

$$
\begin{array}{l} \left| \psi_ {T C} \right\rangle = \frac {1}{\sqrt {M + 1}} \sum_ {j = 0} ^ {M} \left| \{0, M - j \}, \{1, j \} \right\rangle_ {P A} \\ \otimes \left| \left\{0, M - j \right\}, \left\{1, j \right\} \right\rangle_ {C}. \tag {16} \\ \end{array}
$$

This form highlights the high degree of symmetry of the telecloning state: It is completely symmetric under the permutation of any two particles on the same side and also under the exchange of both sides. This implies that, in fact, any of the  $2M$  qubits can be used as the telecloning port, with the clones being created on the opposite side. Another implication is that, instead of using all  $2^M$  levels of the  $M$  qubits on each side, we only need to take into account their  $M + 1$  symmetric states. These can be associated with the states of an  $(M + 1)$ -level particle by the relabeling

$$
\left| j \right\rangle \equiv \left| \{0, M - j \}, \{1, j \} \right\rangle . \tag {17}
$$

[We note that this property arises from the choice of symmetric ancilla states in Eq. (10).] Noting the exchange symmetry of both sides of Eq. (16), this state can then be conveniently rewritten as the maximally entangled state of two  $(M + 1)$ -level particles [21]

$$
\left| \psi_ {T C} \right\rangle = \frac {1}{\sqrt {M + 1}} \sum_ {j = 0} ^ {M} \left| j \right\rangle_ {P A} \otimes \left| j \right\rangle_ {C}. \tag {18}
$$

The corresponding amount of entanglement, given by the von Neumann entropy of each side's reduced density operator, is  $\varepsilon (\left|\psi_{TC}\right\rangle) = \log_2(M + 1)$ .

We now show that this is in fact the minimum amount necessary for any telecloning scheme based on the cloning transformation defined by Eq. (5). To see this, suppose that the input qubit  $X$  is already maximally entangled with another qubit  $D$

$$
\left| \phi_ {i n} \right\rangle = \frac {1}{\sqrt {2}} \left(\left| 0 \right\rangle_ {D} \left| 0 \right\rangle_ {X} + \left| 1 \right\rangle_ {D} \left| 1 \right\rangle_ {X}\right). \tag {19}
$$

Then the linearity of transformation (5) implies that the output of the cloning procedure must be

$$
\left| \right. \phi_ {o u t} \left. \right\rangle = \frac {1}{\sqrt {2}} \left( \right.\left| \right. 0 \left. \right\rangle_ {D} \mid \phi_ {0} \left. \right\rangle_ {A C} + \left| \right. 1 \left. \right\rangle_ {D} \mid \phi_ {1} \left. \right\rangle_ {A C}), \tag {20}
$$

which is precisely our telecloning state  $|\psi_{TC}\rangle$ . Therefore, a telecloning scheme where  $AD$  and  $C$  are spatially separated allows the creation of at least  $\log_2(M + 1)$ $e$ -bits, between two distant parties. We know, however, that entanglement cannot be increased only by local operations and classical communication [20]. We must conclude then that any telecloning scheme based on Eq. (5) requires at least  $\log_2(M + 1)$ $e$ -bits between these parties as an initial resource. The scheme we have described above is therefore optimal in this sense.

In contrast, if Alice used a local unitary network to obtain  $M$  clones and then teleported each one separately to its recipient, the amount of entanglement required would be  $M$  e-bits. Thus telecloning realizes the same task with a much more efficient use of entanglement. Of course, in the case where only one "clone" is produced ( $M = 1$ ), the telecloning state is just a maximally entangled state of two two-level systems (in other words, a Bell state). In this case, our scheme reduces to the usual teleportation protocol.

While entanglement between the two sides gives a measure of the resources necessary to accomplish telecloning, the "two-qubit" entanglement between an arbitrary pair of

particles helps track how information from Alice's unknown state is conveyed to the clones. To see this, we first calculate the reduced density matrix of each pair of qubits. Due to the symmetries of the telecloning state, there are only two different classes of pairs: those where both qubits are on opposite sides (Alice's and the receivers') and those where they are on the same side.

In the first case, the reduced joint density matrix of the two qubits in the  $\{|00\rangle ,|01\rangle ,|10\rangle ,|11\rangle \}$  basis is

$$
\rho_ {P C} = \frac {1}{6 M} \left( \begin{array}{c c c c} 2 M + 1 & 0 & 0 & M + 2 \\ 0 & M - 1 & 0 & 0 \\ 0 & 0 & M - 1 & 0 \\ M + 2 & 0 & 0 & 2 M + 1 \end{array} \right). \tag {21}
$$

The Peres-Horodecki theorem [22,23] provides us with a simple algorithm for determining whether or not a general two-qubit state is entangled. All that is necessary is to calculate the eigenvalues of the partial transpose of the state's density matrix. According to the theorem, a two-qubit state is entangled if and only if at least one of these eigenvalues is negative. The partial transpose of Eq. (21) is

$$
\rho_ {P C} ^ {T _ {2}} = \frac {1}{6 M} \left( \begin{array}{c c c c} 2 M + 1 & 0 & 0 & 0 \\ 0 & M - 1 & M + 2 & 0 \\ 0 & M + 2 & M - 1 & 0 \\ 0 & 0 & 0 & 2 M + 1 \end{array} \right). \tag {22}
$$

The smallest eigenvalue of this matrix is  $-1 / 2M$ , so that state  $\rho_{PC}$  is always entangled for all  $M$ . Thus, any pair of qubits on opposite sides of the telecloning state (in particular, the ones used as port and outputs) will be entangled and by the same amount. On the other hand, the reduced density matrix for two qubits that are both on the same side is

$$
\rho_ {P A} = \frac {1}{6} \left( \begin{array}{l l l l} 2 & 0 & 0 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 2 \end{array} \right). \tag {23}
$$

This reduced density matrix is independent of  $M$  and the minimum eigenvalue of its partial transpose is  $1/6$ . Thus any two qubits on the same side of the telecloning state are disentangled. However, their von Neumann mutual information

$$
I _ {v N} = 2 \ln 2 + \frac {1}{3} \ln \frac {1}{5 4} = 0. 0 8 1 7 \tag {24}
$$

is nonzero, which indicates that the copies on the receivers' side are still classically correlated, although these correlations are weak.

The particular structure of the telecloning state can be justified qualitatively in the following way. First of all, we certainly expect Alice's port qubit to be entangled with the outputs since without entanglement quantum information cannot be sent using only a classical channel. In addition,

![](images/c93a1b00576da7f45f25a3f423c3b95d828a103396da7c8c28cad08f6d11133e.jpg)  
FIG. 2. The telecloning state for  $M = 3$ , consisting of one port qubit  $(P)$ , two ancilla qubits  $(A_{1}$  and  $A_{2})$ , and three output qubits  $(C_{1-3})$ . Solid lines indicate the existence of two-qubit entanglement. Due to the symmetries of the state, the roles of the port and ancilla qubits may be interchanged, as well as those of the transmitting and receiving sides.

since all clones should be equal, the state should be symmetric under permutations of the output qubits; in particular, they should all be equally entangled with the port. Furthermore, in order to optimize the transfer of information the entanglement of the receiving and transmitting sides should be as large as possible. Since the clones are symmetrized, and therefore occupy only  $M + 1$  levels of their Hilbert space, the Schmidt decomposition then implies that the total "two-side" entanglement should be precisely that of two maximally entangled  $(M + 1)$ -level particles. Finally, since the ancilla states on Alice's side may be freely chosen (as long as they are orthogonal), it is natural to assume them to be symmetrized, so that both sides are invariant under permutation.

The calculations above also allow us to view the telecloning state as a "network" of entangled qubits, each of which is only connected to the  $M$  qubits on the opposite side (so the total number of "links" is  $M^2$ ; see Fig. 2). Essentially, we may think of these two-qubit connections as "communication channels" through which quantum information may travel (in the same sense that Bennett et al. referred to the Bell state in the original teleportation scheme as an "Einstein-Podolsky-Rosen (EPR) channel" [1]). In this sense, the multiparticle entanglement structure functions as a multiuser channel, allowing quantum information from Alice's input state to be conveyed to all the output clones. This is emphasized by the fact that any qubit in the network can be used as a port for the transmission.

# V. OPEN QUESTIONS

Our work leaves a number of open questions, which we now briefly discuss. First of all, what is the most efficient way of generating the telecloning state? In particular, we would like to find a way for Alice and other users to create this state just by starting with  $\log (M + 1)$  singlets and operating only locally with the aid of classical communication. If

Alice prepares the state locally and then distributes the particles to other users, these will in general travel through a noisy channel. Then it would be important to find a purification scheme to distill a "good" telecloning state. The second open question is whether our telecloning protocol is the most efficient one or if there exists a way to use even less entanglement. This might be possible if there exists a cloning transformation that produces the same reduced density matrix for the copies as in Eqs. (3) and (4) but with less entanglement between them and the ancilla. It is very important to try to save on entanglement as much as we can because this is the resource that is hardest to manipulate and maintain in practice. A further task would be to generalize our scheme to telecloning of  $N$  to  $M$  particles. Yet another generalization would be the telecloning of  $d$ -dimensional registers [19].

# VI. SUMMARY

We have presented a telecloning scheme that generalizes teleportation by combining it with optimal quantum cloning. This allows the optimal broadcasting of quantum information from one sender (Alice) to  $M$  spatially separated recipients, requiring only a single measurement by Alice followed by classical communication and local one-qubit rotations. Our scheme works by exploiting the multiparticle entanglement structure of particular joint states of  $2M$  particles. This structure can be seen as a multiuser network connecting each qubit on Alice's side to each on the receivers' side in such a way that any node can be used to broadcast quantum information to all those on the opposing side. The resulting state requires only  $\log_2(M + 1)$ $e$ -bits of entanglement between the two sides, representing a much more efficient use of entanglement than the more straightforward approach where Alice first clones her particle  $M$  times and then uses  $M$  singlets to transmit these states to the different receivers.

In closing, we note that our scheme can also be applied to the realization of a "quantum secret sharing" protocol as introduced recently in [10]. This refers to the situation where Alice wishes to teleport a one-qubit state in such a way that it can only be reconstructed at the receiving end of the teleportation channel if two or more separate parties agree to collaborate. In our case, this is accomplished by leaving both the ancilla and output qubits on the receivers' side. Then Alice's original state may be reconstructed if and only if all the output clones and ancilla qubits are brought together to the same location and acted upon by the inverse of the cloning transformation  $U_{1M}$  given in Eq. (5).

# ACKNOWLEDGMENTS

The authors thank Peter Knight and John Smolin for useful discussions and comments. This work was supported in part by the Japan Society for the Promotion of Science, the Brazilian agency Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq), the Overseas Research Student Award Scheme, the United Kingdom Engineering and Physical Sciences Research Council, the Knight Trust, the Elsag-Bailey Company, and the European Community.

[1] C. H. Bennett, G. Brassard, C. Crépeau, R. Jozsa, A. Peres, and W. K. Wootters, Phys. Rev. Lett. 70, 1895 (1993).  
[2] C. H. Bennett and S. J. Wiesner, Phys. Rev. Lett. 69, 2881 (1992).  
[3] C.H. Bennett and G. Brassard, in Proceedings of the IEEE International Conference on Computers, Systems, and Signal Processing, Bangalore, India (IEEE, New York, 1984); A. K. Ekert, Phys. Rev. Lett. 67, 661 (1991).  
[4] A. Ekert and R. Jozsa, Rev. Mod. Phys. 68, 733 (1996); V. Vedral and M. B. Plenio, Prog. Quantum Electron. 22, 1 (1998).  
[5] M. B. Plenio and V. Vedral, e-print quant-ph/9804075.  
[6] D. M. Greenberger, M. A. Horne, A. Shimony, and A. Zeilinger, Am. J. Phys. 58, 1131 (1990).  
[7] R. Cleve and H. Buhrman, Phys. Rev. A 56, 1201 (1997).  
[8] M. Murao, M. B. Plenio, S. Popescu, V. Vedral, and P. L. Knight, Phys. Rev. A 57, R4075 (1998).  
[9] S. Bose, V. Vedral, and P. L. Knight, Phys. Rev. A 57, 822 (1998).  
[10] M. Hillary, V. Buzek, and A. Berthiaume, e-print quant-ph/9806063.  
[11] L. K. Grover, e-print quant-ph/9704012; J. I. Cirac, A. Ekert, S. F. Huelga, and C. Macchiavello, e-print quant-ph/9803017.

[12] W. K. Wootters and W. H. Zurek, Nature (London) 299, 902 (1982).  
[13] V. Buzek and M. Hillary, Phys. Rev. A 54, 1844 (1996).  
[14] V. Buzek, S. L. Braunstein, M. Hillary, and D. Bruß, Phys. Rev. A 56, 3446 (1997).  
[15] N. Gisin and S. Massar, Phys. Rev. Lett. 79, 2153 (1997).  
[16] V. Buzek and M. Hillary, e-print quant-ph/9801009.  
[17] D. Bruß, D. P. DiVincenzo, A. Ekert, C. A. Fuchs, C. Macchiavello, and J. A. Smolin, Phys. Rev. A 57, 2368 (1998).  
[18] D. Bruß, A. Ekert, and C. Macchiavello, Phys. Rev. Lett. 81, 2598 (1998).  
[19] R. Werner, Phys. Rev. A 58, 1827 (1998); P. Zanardi, ibid. 58, 3484 (1998).  
[20] V. Vedral, M. B. Plenio, M. A. Rippin, and P. L. Knight, Phys. Rev. Lett. 78, 2275 (1997); V. Vedral, M. B. Plenio, K. Jacobs, and P. L. Knight, Phys. Rev. A 56, 4452 (1997); V. Vedral and M. B. Plenio, ibid. 57, 1619 (1998).  
[21] For  $M = 2$  this state was found in a different context by N. Cerf, e-print quant-ph/9803058.  
[22] A. Peres, Phys. Rev. Lett. 77, 1413 (1996).  
[23] M. Horodecki, P. Horodecki, and R. Horodecki, Phys. Lett. A 223, 1 (1996).