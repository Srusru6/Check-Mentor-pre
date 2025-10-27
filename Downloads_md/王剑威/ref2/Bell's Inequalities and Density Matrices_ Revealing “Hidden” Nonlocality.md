# PHYSICAL REVIEW LETTERS

VOLUME 74

3 APRIL 1995

NUMBER 14

# Bell's Inequalities and Density Matrices: Revealing "Hidden" Nonlocality

Sandu Popescu*

Department of Physics, Technion-Israel Institute of Technology, 32000 Haifa, Israel

(Received 4 April 1994)

Standard Bell inequalities apply to correlations arising when two or more macroscopically separated systems are each subjected to a single ideal measurement. While these inequalities demonstrate that quantum mechanics and local hidden variable theories yield incompatible predictions for pure states, they fail for mixed states: For mixed states, correlations arising from a single ideal measurement on each system may obey standard Bell inequalities, yet when each system is subjected to a sequence of ideal measurements the correlations are nonlocal. For some situations even this last procedure fails, and we must consider more complex ("nonideal") measurements.

PACS numbers: 03.65.Bz

As is well known, when measurements are performed on two quantum systems separated in space their results are correlated in a manner which, in general, cannot be explained by a local hidden variables model. But 30 years after Bell's pioneering paper [1] we still lack a complete classification of quantum states into local and nonlocal ones. While the case of pure states is completely solved [2,3], for density matrices only partial results have been obtained so far [3-5]. In this Letter I show that for solving this problem we have to change the usual way we think about Bell's inequalities and local hidden variable models.

Bell's original proof and most, if not all, the subsequent alternative proofs [6] (with or without inequalities) have a common aspect: they consider the case in which each of the two systems is subjected to a single ideal local measurement (chosen at random among many possible ideal measurements). For example, in the case of spin- $\frac{1}{2}$  particles one usually considers that each particle is subjected to a single Stern-Gerlach measurement, that is, to a measurement of the spin along some arbitrary direction. More generally, by ideal measurements I mean measurements as defined in the postulates of quantum mechanics (von Neumann, Dirac), that is, when a system is described by an  $n$ -dimensional Hilbert space, the observables to which measurements refer correspond to Hermitian operators acting on this  $n$ -dimensional space, and the only possible results of a measurement are the eigenvalues of the measured operator. After such a measurement the state

of the measured system becomes the projection of the initial state onto the subspace corresponding to the observed eigenvalue. But such an approach is very limited—one could consider that each of the two space-separated systems is subjected to much more complicated experiments. For example, we could bring along with each of the original two particles some supplementary quantum system (called sometimes an "ancilla") prepared in a known initial state and then perform on each side an ideal measurement on the original particle and the corresponding ancilla together. Such a measurement can, in principle, yield more outcomes than  $d$ , the dimension of the Hilbert space of the original particle. This scheme (a nonideal measurement according to the above definition) is known in the literature as the implementation of a positive-valued operator measure (POVM) and it is known that in certain situations it can yield more information about a quantum system than an ideal measurement performed only on the system itself. Moreover, one could consider the case in which each system is subjected to a sequence of measurements instead of a single one. Clearly, to prove that a given quantum state is nonlocal, it is enough to show that it violates some usual Bell inequality (obtained by considering a single ideal measurement performed on each side). On the other hand, to prove that a quantum state is local, one must show that the correlations between the results of any local experiments can be described by a local hidden variables model.

The above being said, the question still remains whether considering general local measurements gives us essential new information about the locality or nonlocality of quantum states. In this Letter I will show that the answer to this question is "yes."

To put things in a better perspective, let us recall first the status of pure states. The basic question of which pure states are classical or not can be answered without going beyond the usual scheme. Indeed, as is well known [2,3], every entangled pure state violates some usual Bell inequality and is therefore nonlocal. The only pure states which do not yield nonlocal correlations when a single ideal measurement is performed on each particle are the direct product states which are obviously local and no further analysis is necessary. Therefore, although it might well be that, even in the case of pure states, considering general measurements will yield new and better inequalities, there is no essential need for such a complication. On the other hand, as I will show, the situation turns out to be different when one deals with mixed states. More precisely, I will give an example in which when each of two systems separated in space is subjected to a single ideal measurement the resulting correlations are classical but, nevertheless, when each system is subjected to more complicated experiments the resulting correlations are nonlocal. The "more complicated experiments" I consider here are simply sequences of two ideal measurements.

The density matrices I analyze in this Letter were discovered by Werner [7]. Consider two systems separated in space, each system living in a  $d$ -dimensional Hilbert space, and let the (mixed) state of the two systems be

$$
W = \frac {1}{d ^ {2}} \left(\frac {1}{d} I ^ {(d \times d)} + 2 \sum_ {i <   j; i, j = 1} ^ {d} | S _ {i j} \rangle \langle S _ {i j} |\right), \tag {1}
$$

where  $I^{(d\times d)}$  is the identity matrix in the  $(d\times d)$  dimensional space of the two systems and  $|S_{ij}\rangle$  is the "spin-  $\frac{1}{2}$  singlet" state

$$
\left| S _ {i j} \right\rangle = \frac {1}{\sqrt {2}} \left(\left| i \right\rangle_ {1} \left| j \right\rangle_ {2} - \left| j \right\rangle_ {1} \left| i \right\rangle_ {2}\right), \tag {2}
$$

where  $\{|i\rangle_1\}$  and  $\{|j\rangle_2\}$  denote orthogonal bases in the Hilbert spaces of particles 1 and 2, respectively. [The form (1) of the matrix  $W$  can be easily obtained from the original form given by Werner by noting that the "flip" operator  $V$  which appears in [5] can be expressed as  $V = I - 2\sum_{i < j}|S_{ij}\rangle \langle S_{ij}|$ .]

An important property of these density matrices is that they cannot be decomposed into mixtures of pure direct product states. As direct products are the only classical pure states, and as Werner's matrices are not mixtures of such states, one feels intuitively that these density matrices are nonclassical. However, Werner has proven that these density matrices do not violate any standard Bell inequality. That is, when each system is subjected to a single ideal measurement the resulting correlations are

classical. (Werner has explicitly written a local hidden variables model which simulates these correlations.) But is there a local hidden variables model which can simulate the results of any measurements performed on the two systems prepared in such a mixed state?

Very recently progress has been made in understanding the properties of these strange states. It has been shown [8] that when two spin- $\frac{1}{2}$  particles are in such a state [Werner's  $(2 \times 2)$ -dimensional matrix] they form a "quantum channel" which can be used for (imperfect) teleportation [9]. Thus the  $(2 \times 2)$ -dimensional Werner matrix has indeed nonclassical aspects. However, teleportation does not involve local measurements performed on each of the spins outside the light cone of each other, so from the fact that such a matrix can be used for teleportation we do not learn immediately anything about the nonlocal correlations it might generate. Nevertheless, this suggests that we should consider more carefully the question of nonlocality of Werner-type matrices and go beyond the usual scheme in which each system is subjected to a single ideal measurement.

In this Letter I will consider Werner-type matrices of dimension  $\geq (5\times 5)$ . Suppose now that each of the two particles is subjected to two consecutive ideal measurements. First, each particle is subjected to a measurement of a two-dimensional projection operator,

$$
P = | 1 \rangle_ {1 1} \langle 1 | + | 2 \rangle_ {1 1} \langle 2 | \tag {3}
$$

on particle 1 and

$$
Q = | 1 \rangle_ {2 2} \langle 1 | + | 2 \rangle_ {2 2} \langle 2 | \tag {4}
$$

on particle 2. After the direct measurement is performed and its result is registered, an observer situated near particle 1 chooses at random to measure one of the two operators  $A$  or  $A'$ , whose exact form will be described below. It is important to note that the decision of which operator to measure is made only after the measurement of  $P$  is completed. Similarly, an observer situated near particle 2 chooses at random between a measurement of  $B$  or  $B'$ . This scheme is almost identical to the one usually used for deriving Bell's inequalities with the difference that  $A, A', B$ , and  $B'$  are not measured directly on the particles in the original state but after the measurements of  $P$  and  $Q$ , respectively.

The operators  $A, A', B$ , and  $B'$  have each three different eigenvalues,  $1, -1$ , and  $0$ . The eigenvalues  $1$  and  $-1$  are nondegenerate and the corresponding eigenstates belong to the subspaces  $\{|1\rangle_1, |2\rangle_1\}$  and  $\{|1\rangle_2, |2\rangle_2\}$ , respectively. The eigenvalue  $0$  is highly degenerate and correspond to the rest of the Hilbert spaces, that is, to  $\{|3\rangle_1, \ldots, |d\rangle_1\}$  and  $\{|3\rangle_2, \ldots, |d\rangle_2\}$ , respectively. The nondegenerate part of these operators is chosen such that they yield maximal violation of the Clauser, Horne, Shimony, and Holt (CHSH) inequality [10] for the singlet state  $|S_{12}\rangle$ , that is,

$$
\langle S _ {1 2} | A B + A B ^ {\prime} + A ^ {\prime} B - A ^ {\prime} B ^ {\prime} | S _ {1 2} \rangle = 2 \sqrt {2}. \tag {5}
$$

Let us see now what happens if we start with an ensemble of pairs of particles in a Werner state  $W^{(d\times d)}$  and subject each particle to the measurements described above. According to the results obtained in the measurements of  $P$  and  $Q$  the original ensemble splits into four subenseb- mles (corresponding to the results  $\{0,0\} ,\{0,1\} ,\{1,0\}$ , and  $\{1,1\}$ ). The most important point is that if the initial ensemble is classical, behaving according to a hidden variables model, then each of these four subensebles is classical. But then we get a contradiction with the quantum mechanical predictions. Indeed, the ensemble corresponding to  $P = 1$  and  $Q = 1$  is described by

$$
W ^ {\prime} = \frac {1}{N} P Q W Q P = \frac {2 d}{2 d + 4} \left(\frac {1}{2 d} I ^ {(2 \times 2)} + | S _ {1 2} \rangle \langle S _ {1 2} |\right), \tag {6}
$$

where  $N$  is a normalization factor, and  $I^{(2\times 2)}$  is a  $2\times$  2 identity matrix acting in the  $\{|1\rangle_1,|2\rangle_1\} \otimes \{|1\rangle_2,|2\rangle_2\}$  subspace and zero in rest. In this state the CHSH inequality is violated. Indeed,

$$
\begin{array}{l} \operatorname {T r} W ^ {\prime} \left(A B + A B ^ {\prime} + A ^ {\prime} B - A ^ {\prime} B ^ {\prime}\right) \\ = \frac {2 d}{2 d + 4} 2 \sqrt {2} \geq 2 \text {f o r} d \geq 5. \tag {7} \\ \end{array}
$$

In conclusion, although a local hidden variables model can simulate all the correlations which arise when only a single, ideal measurement is performed on each of the two particles, such a model cannot account for the correlations which arise when two consecutive measurements are performed on each particle.

To better understand the above result, let us compare the case in which the measurements of  $A$  or  $A'$  and  $B$  or  $B'$  take place directly on the original state  $W$  and the case when  $P$  and  $Q$  were measured first. According to quantum mechanics the correlations between the outcomes of  $A, A', B$ , and  $B'$  are the same in both cases, as all these operators commute with  $P$  and  $Q$ . Still, a local hidden variables model can simulate these correlations in the first case but not in the second one. This happens because for a hidden variables model the two situations are dramatically different. Suppose first that one of the operators  $A$  or  $A'$  is measured on particle 1 directly in the initial state. Then the particle has from the beginning all the information about the detailed question which is asked about the  $\{|1\rangle_1, |2\rangle_1\}$  subspace and it can use this information to avoid "unpleasant" questions. Indeed, quantum mechanics imposes that a measurement of  $A$  yields the outcome 0 with the same probability as a measurement of  $A'$  (as the corresponding eigenspaces are identical). In a local hidden variables model this means that

$$
\int d \lambda \rho (\lambda) P _ {1} (A = 0, \lambda) = \int d \lambda \rho (\lambda) P _ {1} \left(A ^ {\prime} = 0, \lambda\right), \tag {8}
$$

where  $\lambda$  is the hidden variable,  $\rho (\lambda)$  is the probability distribution of  $\lambda$  over the initial ensemble, and  $P_{1}(A =$

$0, \lambda)$  and  $P_{1}(A' = 0, \lambda)$  are the probabilities that particle 1 gives the answers  $A = 0$  and  $A' = 0$ , respectively. But from Eq. (8) it does not follow that

$$
P _ {1} (A = 0, \lambda) = P _ {1} \left(A ^ {\prime} = 0, \lambda\right). \tag {9}
$$

The same is true for the sum of probabilities to obtain the results 1 and  $-1$ , that is,

$$
\begin{array}{l} \int d \lambda \rho (\lambda) \left[ P _ {1} (A = 1, \lambda) + P _ {1} (A = - 1, \lambda) \right] \\ = \int d \lambda \rho (\lambda) \left[ P _ {1} \left(A ^ {\prime} = 1, \lambda\right) + P _ {1} \left(A ^ {\prime} = - 1, \lambda\right) \right], \tag {10} \\ \end{array}
$$

but, in general,

$$
\begin{array}{l} P _ {1} (A = 1, \lambda) + P _ {1} (A = - 1, \lambda) \\ \neq P _ {1} \left(A ^ {\prime} = 1, \lambda\right) + P _ {1} \left(A ^ {\prime} = - 1, \lambda\right). \tag {11} \\ \end{array}
$$

The meaning of these relations is that particle 1, in some pairs of the original ensemble, might have a local hidden variable according to which, if it is subjected to a measurement of  $A$ , say, it will yield one of the answers 1 or -1, but if it is subjected instead to a measurement of  $A'$  it will yield 0. Analogously, similar behavior could characterize also particle 2 in some of the pairs. The freedom to choose between  $\pm 1$  and 0, depending on the measurement to which the particles are subjected, is vital for the success of Werner's local hidden variables model, as he himself remarked. (Actually in Werner's model only particle 1 in some of the pairs uses this freedom, while particle 2 is less sophisticated.) On the other hand, if we first subject particle 1 to a measurement of  $P$ , the particle commits itself to yield, in a subsequent measurement of either  $A$  or  $A'$ , one of the outcomes  $\pm 1$  or 0 before knowing which of these measurements will actually be performed. Indeed,  $P = 1$  forces the particle yield 1 or -1, subsequently, no matter if  $A$  or  $A'$  is measured; the outcome 0 is no longer a valid option. Similarly,  $P = 0$  forces the outcome 0 in a subsequent measurement of either  $A$  or  $A'$ . At this point no local hidden variables model could simulate the quantum mechanical behavior.

Another way of understanding the role of the measurements of  $P$  and  $Q$  is the following: They are used to select a subensemble of pairs from the original ensemble in a way independent of the measurements which are used to test it. Because of this independence one could apply the CHSH inequality directly to this subensemble and conclude that the larger than 2 value of the CHSH correlation predicted by quantum mechanics for this subensemble [Eq. (7)] is incompatible with a local hidden variables model. On the other hand, one could think of measuring  $A$  or  $A'$  and  $B$  or  $B'$  directly on the original ensemble and then selecting the subensemble of pairs for which both particle 1 and particle 2 have yielded  $\pm 1$ . But in a local hidden variables model such as Werner's, the subensemble selected this way depends on the measurements used

to test it. Indeed, suppose that particle 1 in a particular pair has a local hidden variable according to which, if it is subjected to a measurement of  $A$ , it will yield, say, 1, while to a measurement of  $A'$  it will yield 0. Then if it happens that particle 1 is subjected to a measurement of  $A$ , the pair might be included in the selected subensemble (depending on a  $\pm 1$  outcome yielded by particle 2), while if it happens that particle 1 is subjected to a measurement of  $A'$  the pair will not be selected. For such test-dependent subensembles Bell's inequalities cannot be applied directly and, as Werner shows, values larger than 2 for the CHSH correlations can be consistent with local hidden variables models. Other, much more famous, examples of test-dependent subensembles and apparent Bell's inequality violations are the "detector efficiency" problem, and the "space distribution" problem raised by Santos [11]. Another example of this type, probably the simplest possible, has been given by Mermin [12].

There are, of course, many open questions left. In the example presented in this Letter nonlocality was revealed by considering that each of the two spatially separated particles is subjected to a sequence of ideal measurements. It is, however, possible that a single but nonideal measurement performed on each particle suffices. Using non-ideal measurements is obviously necessary in the case of Werner's  $2 \times 2$  matrix. Indeed, in this case the strategy of subjecting each system (spin- $\frac{1}{2}$  particle) to a sequence of ideal measurements does not work, as after the first measurement the systems are left in a direct product state and therefore any subsequent measurements yield classical correlations.

Finally, the big open question is what is the class of classical states. Is it the case that the only classical states are those which can be written as mixtures of direct product states? As a first test case one should probably

attack the remaining Werner-type matrices  $(d\leq 4)$ , which are apparent counterexamples to this conjecture.

It is a pleasure for me to thank Lev Vaidman [8] for raising questions which led to this work. A. Zeilinger for some very illuminating remarks, and also L. Hardy, A. Mann, A. Peres, M. Revzen, D. Rohrlich, and B. Tsirelson (Cirel'son) for very interesting discussions. I would also like to thank the Institute of Theoretical Physics, Technion, Haifa for support during the period of this research.

*Present address: Tel Aviv University, School of Physics and Astronomy, Ramat Aviv, Tel Aviv, Israel.  
[1] J.S. Bell, Physics (Long Island City, N.Y.) 1, 195 (1964).  
[2] N. Gisin, Phys. Lett. A 145, 201 (1991).  
[3] S. Popescu and D. Rohrlich, Phys. Lett. A 166, 293 (1992).  
[4] S. Braunstein, A. Mann, and M. Revzen, Phys. Rev. Lett. 68, 3259 (1992).  
[5] A. Mann, K. Nakamura, and M. Revzen, J. Phys. A 25, L851 (1992).  
[6] For an extensive reference list, see L. Khalfin and B. Tsirelson, Found. Phys. 22, 879 (1992).  
[7] R.F. Werner, Phys. Rev. A 40, 4277 (1989).  
[8] S. Popescu, Phys. Rev. Lett. 72, 797 (1994).  
[9] C. Bennett, G. Brassard, C. Crepeau, R. Jozsa, A. Peres, and W. Wootters, Phys. Rev. Lett. 70, 1895 (1993).  
[10] J. Clauser, M. Horne, A. Shimony, and R. Holt, Phys. Rev. Lett. 23, 880 (1969).  
[11] E. Santos, Phys. Rev. Lett. 66, 1388 (1991); 68, 2702 (1992); Phys. Rev. A 46, 3646 (1992).  
[12] D. Mermin, *Boojums All the Way Through* (Cambridge University Press, New York, 1990), pp. 167-169.