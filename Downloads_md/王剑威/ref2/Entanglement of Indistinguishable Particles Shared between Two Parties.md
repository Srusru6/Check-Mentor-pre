# Entanglement of Indistinguishable Particles Shared between Two Parties

H. M. Wiseman $^{1,*}$  and John A. Vaccaro $^{1,2}$

<sup>1</sup>Centre for Quantum Computer Technology, Centre for Quantum Dynamics, School of Science, Griffith University, Brisbane, Queensland 4111 Australia

$^{2}$ Division of Physics and Astronomy, University of Hertfordshire, Hatfield AL10 9AB, United Kingdom (Received 1 October 2002; published 26 August 2003)

Using an operational definition we quantify the entanglement,  $E_P$ , between two parties who share an arbitrary pure state of  $N$  indistinguishable particles. We show that  $E_P \leq E_M$ , where  $E_M$  is the bipartite entanglement calculated from the mode-occupation representation. Unlike  $E_M$ ,  $E_P$  is superadditive. For example,  $E_P = 0$  for any single-particle state, but the state  $|1\rangle |1\rangle$ , where both modes are split between the two parties, has  $E_P = 1/2$ . We discuss how this relates to quantum correlations between particles, for both fermions and bosons.

DOI: 10.1103/PhysRevLett.91.097902

Entanglement lies at the heart of quantum mechanics, and is profoundly important in quantum information (QI) [1]. It might be thought that there is nothing new to be said about bipartite entanglement if the shared state  $|\Psi_{AB}\rangle$  is pure. In ebits, the entanglement is simply [2]

$$
E \left(\left| \Psi_ {A B} \right\rangle\right) = S \left(\rho_ {A}\right). \tag {1}
$$

Here  $S(\rho)$  is the binary von Neumann entropy  $-\mathrm{Tr}[\rho \log_2\rho]$ , and (since we will use unnormalized kets)

$$
\rho_ {A} = \operatorname {T r} _ {B} [ | \Psi_ {A B} \rangle \langle \Psi_ {A B} | ] / \langle \Psi_ {A B} | \Psi_ {A B} \rangle . \tag {2}
$$

However, in the context of indistinguishable particles, a little consideration reveals a less than clear situation, which has been the subject of recent controversy [3-7].

Consider, for example, a single particle in an equal superposition of being with Alice and with Bob. In the mode-occupation, or Fock, representation, the state is

$$
\left| 0, 1 \right\rangle + \left| 1, 0 \right\rangle . \tag {3}
$$

Here we are following the conventions of writing Alice's occupation number(s) followed by Bob's, separated by a comma, and of omitting any modes that are unoccupied. On the face of it, this is an entangled state with one ebit, and such a state has been argued to show nonlocality of a single photon [8,9]. However, the particle's wave function, in the coordinate representation, is of the form

$$
\psi_ {A} (x) + \psi_ {B} (x), \tag {4}
$$

where the subscripts indicate where the wave packets are localized in coordinate  $(x)$  space. In this representation, the above entanglement is not apparent, and indeed it has been argued that nonlocality cannot be a single-particle effect [10] (although see Ref. [11]).

As a second example, consider a two-particle state where Alice has one particle and Bob the other. In the mode-occupation picture, the state is  $|1,1\rangle$ , which appears unentangled. But since these are identical particles, the wave function must be symmetrized as

$$
\psi_ {A} (x) \psi_ {B} (y) \pm \psi_ {A} (y) \psi_ {B} (x), \tag {5}
$$

PACS numbers: 03.67.Mn, 03.65.Ud, 03.75.-b, 05.30.-d

for bosons and fermions, respectively. This has the appearance of an entangled state.

Finally, consider another two-particle state, but this time where the two particles are prepared and shared as in the first example, but in different modes. In the Fock representation, this state is entangled:

$$
\begin{array}{l} (| 0, 1 \rangle + | 1, 0 \rangle) (| 0, 1 \rangle + | 1, 0 \rangle) \\ = | 0 0, 1 1 \rangle + | 0 1, 1 0 \rangle + | 1 0, 0 1 \rangle + | 1 1, 0 0 \rangle . \tag {6} \\ \end{array}
$$

The corresponding wave function

$$
\begin{array}{l} \left[ \psi_ {A 1} (x) + \psi_ {B 1} (x) \right] \left[ \psi_ {A 2} (y) + \psi_ {B 2} (y) \right] \\ \pm \left[ \psi_ {A 1} (y) + \psi_ {B 1} (y) \right] \left[ \psi_ {A 2} (x) + \psi_ {B 2} (x) \right] \tag {7} \\ \end{array}
$$

also has the appearance of an entangled state.

In this Letter we give an operational definition of entanglement between two parties who share an arbitrary pure state of indistinguishable particles. Applying this to the three states introduced above yields an entanglement (in ebits) of 0, 0, and  $1/2$ , respectively.

To justify these (nonobvious) answers, we proceed as follows. First we define precisely what we mean when we use the term particle. Next we review two previous measures of entanglement. The first, as championed in Refs [3,4] for example, we call entanglement of modes. The second, following Paškauskas and You (PY) [5] and others, we call the quantum correlation between two particles. Then we introduce our own concept, the entanglement of particles. We show that (at least for bosons) our criterion for entanglement is stronger than both previous criteria, and even their conjunction. We illustrate our measure with several examples, and finally prove a number of its properties including superadditivity.

Definition of "particle". For the purpose of our analysis, a particle is a discrete entity which is indistinguishable from other particles of the same type, and for which conservation laws imply a particle number superselection rule (SSR). That is, the creation of superpositions of a different number eigenstates by any means

(including measurements) is forbidden. Examples of such "genuine" particles are: electrons; and hydrogen atoms in a particular electronic state. Note that the conservation law need not be for the particle number itself. For example, composite particles such as atoms can be constructed from their constituents and so their number is not conserved. Nevertheless, there is still a SSR because of the fundamental conservation laws of baryon and lepton numbers of the constituents [12] and this is all we need here. However, it is usual in QI processing for the number of particles to be conserved [13]. Thus, without loss of generality, we will assume a conservation law for particle number. Note also that such a law does not apply to the quanta of excitation (which are always bosonic) of oscillators which can be excited classically, such as photons or excitons.

Previous measures. One measure of entanglement of identical particles is what we call the entanglement of modes  $E_{M}$ . This is simply determined by calculating Eq. (1) for the bipartite state in the Fock representation. Since we are concerned only with genuine particles, we will henceforth assume that the joint state  $|\Psi_{AB}\rangle$  contains exactly  $N$  particles. Clearly  $E_{M}$  is independent of whether the particles are bosons or fermions, but in the latter case the occupation numbers are limited to 0 or 1.

A completely different concept can be considered for the case where  $N = 2$ , namely, whether one particle is entangled with the other [5-7]. This is conceptually quite different from both the entanglement between two spatially separated parties, and the entanglement between two distinguishable particles (which in principle could be separated, unlike identical particles). To emphasize these differences, PY [5] follow Schliemann et al. [6] in referring instead to quantum correlations (QC) between particles. Since there is no notion of spatial separation, we drop for now the  $AB$  subscript on the state  $|\Psi \rangle$ .

The QC as defined by PY is different for bosons and fermions. The QC between bosons is given in bits as

$$
S _ {b} = S [ \rho^ {(1)} ], \tag {8}
$$

where  $S$  is the binary entropy as above, and where  $\rho^{(1)}$  is the single-particle mixed state. In some particular mode basis, the state matrix is

$$
\left[ \rho^ {(1)} \right] _ {\mu^ {\prime} \mu} = \langle \Psi | c _ {\mu} ^ {\dagger} c _ {\mu^ {\prime}} | \Psi \rangle / \sum_ {\nu} \langle \Psi | c _ {\nu} ^ {\dagger} c _ {\nu} | \Psi \rangle , \tag {9}
$$

where  $c_{\mu}$  is the boson annihilation operator for mode  $\mu$ . It turns out that for bosons it is always possible to find a basis where the two-particle state can be written as

$$
| \Psi \rangle = \sum_ {\mu} \beta_ {\mu} \frac {1}{\sqrt {2}} \left(c _ {\mu} ^ {\dagger}\right) ^ {2} | \mathbf {0} \rangle , \tag {10}
$$

where  $|\mathbf{0}\rangle$  is the state containing no particles, and where the  $1 / \sqrt{2}$  corrects a typographical error in Ref. [5]. From this it can be shown that [5]  $S_{b} = H(\{\left|\beta_{\mu}\right|^{2}\}_{\mu})$ , where here  $H$  is the binary Shannon entropy [1] for the probability

distribution  $\{|\beta_{\mu}|^2\}_{\mu}$ . Only the state  $|2\rangle$ , with both bosons in one mode, is uncorrelated.

For fermions, the single-particle mixed state and its entropy are defined in precisely the same way, but where the  $c_{\mu} s$  are fermion annihilation operators. However, PY say the QC between fermions is, in bits,  $S_f - 1$ . This curious difference from the bosonic case is motivated as follows. For fermions it is always possible to find a basis where the two-particle state can be written as

$$
| \Psi \rangle = \sum_ {\nu} \phi_ {\nu} c _ {2 \nu} ^ {\dagger} c _ {2 \nu - 1} ^ {\dagger} | \mathbf {0} \rangle . \tag {11}
$$

From this it can be shown that  $S_{f} - 1 = H(\{| \phi_{\nu}|^{2}\}_{\nu})$ . The least-correlated state is a state of the form  $|1\rangle |1\rangle$ , with one fermion in each of two modes. This state has an entropy of 1, but a QC of 0 according to PY. Thus one has the curious situation that the "same" state, such as  $|1\rangle |1\rangle$  would be considered quantum correlated for bosons but uncorrelated for fermions.

Entanglement of particles. We wish to define the entanglement  $E_{P}$  between two distant parties, Alice and Bob, who share some state of  $N$  indistinguishable particles. An obvious question is, what is wrong with  $E_{M}$  as defined above? The answer is that it fails to take into account the SSR for particle number. To fully use the supposed entanglement  $E_{M}$  they share, Alice and Bob in general must be able to arbitrarily measure and manipulate their local systems. Unless Alice's (and hence Bob's) state happens to be a state of definite particle number, this will mean violating the SSR for particle number. For example, the teleportation protocol in Ref. [4] relies upon such forbidden operations. Thus  $E_{M}$  in general overestimates the available entanglement  $E_{P}$ .

To be specific, say that in addition to all of the indistinguishable particles which Alice and Bob may use in the experiment, their quantum state  $|\Psi_{AB}\rangle$  includes a conventional quantum register each, initially in a product state. The operational definition of  $E_P$  is the maximal amount of entanglement which Alice and Bob can produce between their quantum registers by local operations (LOs) [14]. Since the registers of Alice and Bob consist of distinguishable qubits, this entanglement can be computed by the standard measure. As a consequence of the particle number SSR, this entanglement will be given not by the mode entanglement of  $|\Psi_{AB}\rangle$ , but by

$$
E _ {P} \left(\left| \Psi_ {A B} \right\rangle\right) \equiv \sum_ {n} P _ {n} E _ {M} \left(\left| \Psi_ {A B} ^ {(n)} \right\rangle\right). \tag {12}
$$

Here  $|\Psi_{AB}^{(n)}\rangle$  is  $|\Psi_{AB}\rangle$  projected into the subspace of fixed local particle number ( $n$  for Alice,  $N - n$  for Bob),

$$
\left| \Psi_ {A B} ^ {(n)} \right\rangle = \Pi_ {n} \left| \Psi_ {A B} \right\rangle , \tag {13}
$$

and  $P_{n}$  is the probability  $\langle \Psi_{AB}^{(n)}|\Psi_{AB}^{(n)}\rangle /\langle \Psi_{AB}|\Psi_{AB}\rangle$

To see this explicitly, say Alice and Bob perform the optimal LOs to change  $|\Psi_{AB}\rangle$  into  $|\Psi_{AB}^{\prime}\rangle$  in which their registers have entanglement  $E_P$ . Alice could now measure

her local particle number  $\hat{n}$ , and this would not affect  $E_{P}$  on average. But since LOs conserve local particle number this would be true even if Alice were to measure  $\hat{n}$  before applying the LOs. This measurement would collapse the state  $|\Psi_{AB}\rangle$  into the state  $|\Psi_{AB}^{(n)}\rangle$ , with probability  $P_{n} = \langle \Psi_{AB}^{(n)}|\Psi_{AB}^{(n)}\rangle$ , where  $n$  is the measurement result. Now since this is a state of definite local particle number for both parties, there are no conservation laws that prevent local unitaries from transferring all of its entanglement,  $E_{M}(|\Psi_{AB}^{(n)}\rangle)$  to the quantum registers. To obtain  $E_{P}$  as defined above one simply averages over the result  $n$ , yielding Eq. (12).

We can relate  $E_{P}$  to both previous concepts defined above. First, since projecting onto the local particle number eigenspace is a local operation, it can only decrease entanglement [2]. It follows that

$$
E _ {P} \left(\left| \Psi_ {A B} \right\rangle\right) \leq E _ {M} \left(\left| \Psi_ {A B} \right\rangle\right), \tag {14}
$$

so that the entanglement of modes is necessary for the entanglement of particles.

Second, it turns out (for bosons at least) that QC between particles is also necessary for entanglement of particles. Recall that the QC was defined by YP only for two particles. If the QC between two bosons is zero then there is some choice of modes such that they are in the same mode. In general this mode will be split between an Alice mode and a Bob mode, with coefficients  $\alpha$  and  $\beta$ . Then in the Fock picture, the two-boson state is

$$
\begin{array}{l} \frac {1}{\sqrt {2}} \left(\alpha a ^ {\dagger} + \beta b ^ {\dagger}\right) ^ {2} | 0, 0 \rangle = \alpha^ {2} | 2, 0 \rangle + \sqrt {2} \alpha \beta | 1, 1 \rangle \\ + \beta^ {2} | 0, 2 \rangle , \tag {15} \\ \end{array}
$$

where  $a$  and  $b$  are the annihilation operators for the relevant mode on Alice's and Bob's side, respectively. Since the three terms here have different local particle number,  $E_P = 0$ . Thus entanglement of particles  $(E_P > 0)$  implies QC between bosons.

For fermions, the situation is not so clear-cut. Consider the two-particle state (6). Applying Eq. (12), Alice and Bob share half an ebit through these two identical particles. Using modes split between Alice and Bob (as in the preceding paragraph), this state can be rewritten as  $|1\rangle |1\rangle$ . As a bosonic state, this would be considered by PY as exhibiting QC, but not so as a fermionic state. As discussed, the justification for the latter categorization is the desire to have the least-correlated two-fermion state have no QC, like the least-correlated two-boson state. Our analysis shows that what is more relevant to bipartite entanglement of particles is that the one-particle entropy of this state,  $S_{f} = S_{b} = 1$ , is nonzero.

This conclusion is strengthened in that the entanglement of particles, as we have quantified it, reduces in the two-particle case to a modified version of the single-particle entropy  $S_{b}$  or  $S_{f}$ , as defined by PY. It does not reduce to  $S_{f} - 1$ , as they define the QC between fermions to be. We would expect the QC between the two particles

to correspond to the entanglement between Alice and Bob only if Alice has just one of the particles. Therefore we modify the QC between particles of PY by defining the single-particle state matrix to be

$$
\left[ \rho_ {A} ^ {(1)} \right] _ {k ^ {\prime} k} = \left. \langle \Psi_ {A B} ^ {(1)} \mid a _ {k} ^ {\dagger} a _ {k ^ {\prime}} \mid \Psi_ {A B} ^ {(1)} \rangle \right/ \sum_ {l} \langle \Psi_ {A B} ^ {(1)} \mid a _ {l} ^ {\dagger} a _ {l} \mid \Psi_ {A B} ^ {(1)} \rangle . \tag {16}
$$

Here the operators  $a_{k}$  are those acting on Alice's modes only. It is then easy to verify that the weighted single-particle entropy  $P_{1}S[\rho_{A}^{(1)}]$  is identical to the entanglement of particles as defined above. This is because  $[\rho_A^{(1)}]_{k'k}$  is the same state matrix as  $\mathrm{Tr}_B[|\Psi_{AB}^{(1)}\rangle \langle \Psi_{AB}^{(1)}|]$  in the basis  $|k\rangle = a_k^\dagger |\mathbf{0}\rangle$ , and the contributions to  $E_P$  from the  $|\Psi^{(0)}\rangle$  and  $|\Psi^{(2)}\rangle$  terms are zero. This result holds for either fermions or bosons.

Examples.-To illustrate our measure  $E_P$  we have tabulated it, as well as  $E_M$ , and (where appropriate)  $S_b$  and  $S_f$ , for various states in Table I. A number of features are worth noting. First, as proven above,  $E_P \leq E_M$ , so that  $E_P > 0 \longrightarrow E_M > 0$ . Second, where the single-particle entropy  $S$  is defined, it is identical for bosons and fermions ( $S_b = S_f$ ), and satisfies  $E_P < S$ . This is consistent with the result we have proven that  $E_P > 0 \longrightarrow S > 0$ . Third, even if  $E_M > 0$  and  $S > 0$ , this does not imply that  $E_P > 0$ , so our concept cannot be derived from these previous concepts.

All of the numbers in Table I are trivial to calculate from the above definitions, except for the asymptotic result. This is the entanglement between Alice and Bob if  $N$  indistinguishable particles are prepared independently in  $N$  different modes, each of which is split equally between Alice and Bob. For large  $N$ , standard statistical mechanics arguments [15] yields

$$
\begin{array}{l} E _ {P} [ (| 0, 1 \rangle + | 1, 0 \rangle) ^ {\otimes N} ] = 2 ^ {- N} \sum_ {n = 0} ^ {N} \binom {N} {n} \log_ {2} \binom {N} {n} \\ \sim N - \frac {1}{2} \log_ {2} (N) - \delta , \tag {17} \\ \end{array}
$$

where  $\delta = (-1 + \log_2\pi + 1 / \ln 2) / 2 \approx 1.047096$ .

Properties.-The astute reader will have noticed that our measure of entanglement fails to satisfy the postulate of partial additivity identified in Ref. [2]. That is,

$$
E _ {P} \left(\left| \Psi \right\rangle^ {\otimes C}\right) \neq C E _ {P} \left(\left| \Psi \right\rangle\right). \tag {18}
$$

The reason is that the states  $|\Psi \rangle$  in the tensor product are not truly independent of each other due to the indistinguishability of the particles. If the subsequent terms in the tensor product represented states of different species of particle, the entanglement would be additive.

In fact, for arbitrary pure states of indistinguishable particles, the entanglement is superadditive:

$$
E _ {P} (| \Psi \rangle \otimes | \Phi \rangle) \geq E _ {P} (| \Psi \rangle) + E _ {\mathrm {P}} (| \Phi \rangle). \tag {19}
$$

This can be seen as follows. Say  $|\Psi \rangle$  and  $|\Phi \rangle$  are states with  $N$  and  $M$  particles, respectively. We use  $\rho_A^{(n)}$  and  $\sigma_A^{(m)}$

TABLE I. Entanglement or related measures (in bits) for various states under various measures. Three dots indicate that the measure is inapplicable to that state.  $E_{M}$  is the bipartite entanglement of modes,  $S_{b}$  ( $S_{f}$ ) the single-particle entropies for a two-particle system of bosons (fermions), and  $E_{P}$  the bipartite entanglement of particles proposed here. All states are given in the Fock representation, with a comma separating the occupation numbers for Alice's modes from those of Bob.

<table><tr><td>State</td><td>EM</td><td>Sb</td><td>Sf</td><td>EP</td></tr><tr><td>|0,1) + |1,0)</td><td>1</td><td>...</td><td>...</td><td>0</td></tr><tr><td>|1,1)</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>(|0,1) + |1,0))(|0,1) + |1,0))</td><td>2</td><td>1</td><td>1</td><td>1/2</td></tr><tr><td>|0,2) + |2,0)</td><td>1</td><td>1</td><td>...</td><td>0</td></tr><tr><td>|0,2) + √2|1,1) + |2,0)</td><td>3/2</td><td>0</td><td>...</td><td>0</td></tr><tr><td>|01,10) + |10,01)</td><td>1</td><td>2</td><td>2</td><td>1</td></tr><tr><td>|11,00) + |00,11)</td><td>1</td><td>2</td><td>2</td><td>0</td></tr><tr><td>(|0,1) + |1,0))⊗N</td><td>N</td><td>...</td><td>...</td><td>~N</td></tr></table>

for the reduced state of  $|\Psi^{(n)}\rangle$  and  $|\Phi^{(m)}\rangle$ , respectively, and  $p$  for the total particle number, on Alice's side. Then, defining  $w_{nmp} = \delta_{p,n+m}\langle\Psi^{(n)}|\Psi^{(n)}\rangle\langle\Phi^{(m)}|\Phi^{(m)}\rangle$ , Eq. (12) implies that  $E_P(|\Psi\rangle \otimes |\Phi\rangle)$  equals

$$
\sum_ {p = 0} ^ {N + M} S \left[ \frac {\sum_ {n , m} w _ {n m p} \rho_ {A} ^ {(n)} \otimes \sigma_ {A} ^ {(m)}}{\sum_ {n , m} w _ {n m p}} \right] \sum_ {n, m} w _ {n m p}. \tag {20}
$$

Using the concavity of the entropy [1], we obtain

$$
\begin{array}{l} E _ {P} \geq \sum_ {p = 0} ^ {N + M} \sum_ {n, m} w _ {n m p} S \left[ \rho_ {A} ^ {(n)} \otimes \sigma_ {A} ^ {(m)} \right], (21) \\ = \sum_ {p = 0} ^ {N + M} \sum_ {n, m} w _ {n m p} \left\{S \left[ \rho_ {A} ^ {(n)} \right] + S \left[ \sigma_ {A} ^ {(m)} \right] \right\}. (22) \\ \end{array}
$$

Applying Eq. (12) to  $|\Psi \rangle$  and  $|\Phi \rangle$ , this expression reduces to the right-hand side of Eq. (19).

Now the inequality in Eq. (21) is an equality iff (if and only if) all states in the sum are identical [1]. But actually they are orthogonal, so the equality in Eq. (19) is satisfied iff there is only one element in the sum. That is, iff at least one of  $V_{\Psi}$  or  $V_{\Phi}$  is 0. Here  $V_{\Theta}$  is the variance in the number of particles on Alice's side for state  $|\Theta\rangle$ .

The above results also suggest that with a large number of copies  $C$ , the mode entanglement is recovered:

$$
\lim  _ {C \rightarrow \infty} E _ {P} \left(| \Psi \rangle^ {\otimes C}\right) / E _ {\mathrm {M}} \left(| \Psi \rangle^ {\otimes C}\right) = 1. \tag {23}
$$

This can be established using the same techniques [15] that gave Eq. (17). From the central limit theorem, the number of significant terms in  $|\Psi \rangle^{\otimes C}$  with different particle number  $n$  on Alice's side is of the order of  $\sqrt{CV_{\Psi}}$ . For this state, the entropy of a typical  $\rho_A^{(n)}$  is therefore of order  $\log_2(\sqrt{CV_{\Psi}})$  smaller than the entropy of  $\rho_A$ . That is,

$$
E _ {P} \left(\left| \Psi \right\rangle^ {\otimes C}\right) \sim C E _ {M} \left(\left| \Psi \right\rangle\right) - \frac {1}{2} \log_ {2} \left(V _ {\Psi} C\right) + O (1), \tag {24}
$$

from which Eq. (23) follows.

In conclusion, from an operational definition we have quantified  $E_P$ , the entanglement of  $N$  indistinguishable particles shared between two parties. Our criterion for entanglement of particles ( $E_P > 0$ ) is stronger (in a mathematical sense) even than the conjunction of two previous concepts in this area. These are the following: the entanglement of modes ( $E_M > 0$ ); and, for the two-particle case, correlations between the particles ( $S > 0$ , where  $S$  is the single-particle entropy). For asymptotically many copies of the state,  $E_P \rightarrow E_M$ . However, unlike  $E_M$ ,  $E_P$  is superadditive. This unusual characteristic of  $E_P$  reflects the indistinguishability of the particles. It has implications for QI processing and Bell-type nonlocality, and requires further investigation (see, for comparison, Ref. [13]). The generalization of our work to multipartite entanglement is another area for future exploration.

We are grateful for discussions with J. Ruostekoski, T. Osborne, M. Nielsen, J. Dodd, and M. Bremner. This work was supported by the Australian Research Council.

*Electronic address: H.Wiseman@griffith.edu.au

[1] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, 2000).  
[2] M. Horodecki, P. Horodecki, and R. Horodecki, Phys. Rev. Lett. 84, 2014 (2000).  
[3] P. Zanardi, Phys. Rev. A 65, 042101 (2002); P. Zanardi and X. Wang, J. Phys. A 35, 7947 (2002).  
[4] J. R. Gittings and A. J. Fisher, Phys. Rev. A 66, 032305 (2002).  
[5] R. Paškauskas and L. You, Phys. Rev. A 64, 042310 (2001).  
[6] J. Schliemann, J. I. Cirac, M. Kus, M. Lewenstein, and D. Loss, Phys. Rev. A 64, 022303 (2001).  
[7] Y.S. Li, B. Zeng, X.S. Liu, and G.L. Long, Phys. Rev. A 64, 054302 (2001).  
[8] S. M. Tan, D. F. Walls, and M. J. Collett, Phys. Rev. Lett. 66, 252 (1991).  
[9] L. Hardy, Phys. Rev. Lett. 73, 2279 (1994).  
[10] D. M. Greenberger, M. A. Horne, and A. Zeilinger, Phys. Rev. Lett. 75, 2064 (1995).  
[11] G. Björk, P. Jonsson, and L. L. Sánchez-Soto, Phys. Rev. A 64, 042106 (2001).  
[12] A. Sudbery, Quantum Mechanics and the Particles of Nature (Cambridge University Press, Cambridge, 1986).  
[13] F. Verstraete and J. I. Cirac, Phys. Rev. Lett. 91, 010404 (2003).  
[14] Classical communication makes no difference here.  
[15] C. Kittel and H. Kroemer, Thermal Physics (Freeman, New York, 1980).