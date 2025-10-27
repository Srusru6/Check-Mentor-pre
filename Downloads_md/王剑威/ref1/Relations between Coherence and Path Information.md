# Relations between Coherence and Path Information

Emilio Bagan, $^{1,3}$  János A. Bergou, $^{1,2}$  Seth S. Cottrell, $^{4}$  and Mark Hillary $^{1,2}$

$^{1}$ Department of Physics and Astronomy, Hunter College of the City University of New York, 695 Park Avenue, New York, New York 10065, USA

2Graduate Center of the City University of New York, 365 Fifth Avenue, New York, New York 10016, USA

Fisica Teorica: Informacion i Fenomens Quantics, Departament de Fisica, Universitat Autonoma de Barcelona, 08193 Bellaterra (Barcelona), Spain

$^{4}$ Department of Mathematics, New York City College of Technology, 300 Jay Street, Brooklyn, New York 11201, USA (Received 20 September 2015; revised manuscript received 10 December 2015; published 22 April 2016)

We find two relations between coherence and path information in a multipath interferometer. The first builds on earlier results for the two-path interferometer, which used minimum-error state discrimination between detector states to provide the path information. For visibility, which was used in the two-path case, we substitute a recently defined  $l_{1}$  measure of quantum coherence. The second is an entropic relation in which the path information is characterized by the mutual information between the detector states and the outcome of the measurement performed on them, and the coherence measure is one based on relative entropy.

DOI: 10.1103/PhysRevLett.116.160406

Recently a theory of quantum coherence as a resource for quantum information processing was proposed along with two possible coherence measures, an entropic measure and an  $l_{1}$  measure [1]. This has led to a renewed interest in the properties of quantum coherence [2,3]. The  $l_{1}$  measure is of interest, because it is, in principle, observable. It depends on the magnitudes of off-diagonal density matrix elements, whose real and imaginary parts can be estimated. The entropic measure is the difference between the von Neumann entropies of a density matrix and a diagonal density matrix formed from its diagonal elements. In this Letter we focus on the duality relations between these coherence measures and the which-path information for a particle going through an interferometer with two or more internal paths.

It is well known that a particle going through an interferometer can exhibit wave or particle properties. The particle properties are characterized by how much information one has about which path the particle took through the device. The wave properties determine the visibility of the interference pattern. There is a trade-off between the particle and wave properties: the stronger one is, the weaker the other is. This was studied for interferometers with two internal paths in a quantitative way by Wootters and Zurek [4]. The relation was put into an elegant form by Greenberger and YaSin [5],

$$
D ^ {2} + V ^ {2} \leq 1, \tag {1}
$$

where  $D$  is a measure of path information and  $V$  is the visibility of the interference pattern. This work was carried further by Jaeger et al. [6], who proposed a possible definition for path information for interferometers with more than two paths. Wootters and Zurek employed a path detector in their analysis but did not derive a relation of the form given in Eq. (1). In the subsequent work [5,6], which

did derive a path-visibility relation, the path information is related not to information from a detector but to the preparation of the particle state, i.e., whether it is more likely to be in one path rather than in the other. In a seminal study, Englert [7] combined these approaches. He introduced detectors into the problem in order to define the path information and derived a relation between this type of path information and the visibility that took the form of Eq. (1). In his model, a system of detectors, one in each path, is coupled to the paths such that when the particle passes through the interferometer correlations are produced between the path states and the detector states. Path information is then related to the distinguishability of the detector states. If the detector states are orthogonal, one has perfect path information, but if they are not, then the information one can obtain about the path is smaller.

The first derivation of a path-visibility relation for more than two paths is due to Durr [8]. Expressing the density matrix of the particle inside the interferometer in a path basis, in which each path corresponds to one of a set of orthonormal states, his measure of path information depended on the diagonal elements of the density matrix, and his measure of visibility depended on the off-diagonal elements. Some difficulties with the definition introduced by Durr were pointed out in Ref. [9], and this, in turn, following the earlier discussion in Ref. [10], led to proper definitions of the quantities that are free of the difficulties [11] and also to some alternative definitions [12]. A duality relation using information quantities was presented by Angelo and Ribeiro [13]. It uses a different measure of which-path information than the one we will present here.

We emphasize that in Refs. [8-12] an  $l_{2}$  measure of coherence was employed. Hence, the results presented there are relations between second moments that, in turn, are closely connected to uncertainty relations. As argued in

Ref. [1], a proper operational definition of coherence must be related to first moments, i.e., an  $l_{1}$  measure. There they defined the  $l_{1}$  coherence of a density matrix  $\rho$  to be

$$
C _ {l _ {1}} (\rho) = \sum_ {\substack {i, j = 1 \\ i \neq j}} ^ {N} | \rho_ {i j} |. \tag{2}
$$

Here we shall consider a normalized version of this quantity given by  $X = (1 / N)C_{l_1}(\rho)$ , which has the property that  $0\leq X\leq (N - 1) / N$ . There is also an entropic measure of coherence that satisfies the criteria in Ref. [1], which, as we shall see, also leads to a duality relation. Both definitions of coherence are basis dependent. We will treat the case of the  $l_{1}$  measure first.

It is natural to search for a duality relation between path coherence and path information. The first approach to this problem using the  $l_{1}$  measure and a detector in each path was taken by Bera et al. [14]. The discrimination of the detector states can be done in a number of ways, and the fact that the states are not orthogonal means it cannot be done perfectly. Bera et al. used unambiguous discrimination, in which one never obtains a wrong answer, but the procedure can sometimes fail, providing no information about the detector state. They found that the linear sum of the path coherence and an upper bound to the probability of successfully discriminating the detector states is less than or equal to one. This does not produce a relation of the form given in Eq. (1). Furthermore, unambiguous discrimination is not possible when the detector states are linearly dependent. When Englert derived his relation, which did take the form of Eq. (1), he used minimum-error state discrimination [7], which is always possible, even if the detector states are linearly dependent. In this procedure, one always obtains a result, but it can be wrong, though the probability of making an error is minimized. The probability of successfully identifying the detector states  $P_{s}$  quantifies the available path information via optimized measurements.

In this Letter we study the duality in the  $N$ -path interferometer between coherence and path information. Our first result is a relation between these two quantities that has a form similar to Eq. (1):

$$
\left(P _ {s} - \frac {1}{N}\right) ^ {2} + X ^ {2} \leq \left(1 - \frac {1}{N}\right) ^ {2}. \tag {3}
$$

If we normalize the quantities appearing on the lhs to their maximum, then, in terms of the normalized quantities,  $D = (P_{s} - 1 / N) / (1 - 1 / N)$  and  $C = X / (1 - 1 / N)$ , such that  $0 \leq C, D \leq 1$ , the relation is exactly of the form given in Eq. (1). Equation (1) corresponds to the first quadrant of the unit circle in the  $D, C$  plane. The relation given by Bera et al. [14], on the other hand, can be written as  $D_{Q} + C \leq 1$  (using a measure of distinguishability  $D_{Q}$  obtained, as mentioned above, by unambiguous discrimination of the detector states). It corresponds to the region of the same

quadrant under the line  $D + C = 1$ . Clearly, the area of the quadrant above the line is excluded by the linear inequality, so it misses a region where wave and particle properties are compatible.

Furthermore, the relation is actually an equality for  $N = 2$ . The quantity  $P_{s} - (1 / N)$  is the measure of how much better one can do by using prior information and detectors than by just random guessing. If we readout the detectors and use prior information, our probability of being right is  $P_{s}$ . Note that if the detector states are orthogonal to each other, the two sides of the inequality are equal, so the right-hand side of the inequality can be attained. Note also that if the priors are known, the optimal guessing strategy is the pure strategy when one always guesses the most likely state.

In order to derive Eq. (3) we start with a particle entering an  $N$ -port interferometer via a generalized beam splitter that puts it in the superposition state:

$$
| \psi \rangle = \sum_ {i = 1} ^ {N} \sqrt {p _ {i}} | i \rangle . \tag {4}
$$

The orthonormal basis states,  $|i\rangle$ ,  $i = 1,2,\dots,N$ , correspond to the  $N$  possible paths and span the  $N$ -dimensional Hilbert space  $\mathcal{H}_p$ . Equation (4) represents the most general state of the particle inside the interferometer.

While in the interferometer, the particle interacts with another system, called the detector. The detector starts in a global state  $|\eta_0\rangle$ . The interaction of the particle with the detector is described by the controlled unitary  $U(|i\rangle |\eta_0\rangle) = |i\rangle |\eta_i\rangle$ , which entangles the path degree of freedom  $|i\rangle$  of the particle with the detector state  $|\eta_i\rangle$ . After the particle has interacted with the detector, the state of the entire system is

$$
| \Psi \rangle = \sum_ {i = 1} ^ {N} \sqrt {p _ {i}} | i \rangle | \eta_ {i} \rangle . \tag {5}
$$

We want to point out that this is a generalization of the approach in Ref. [7] into a more powerful scenario. We do not necessarily have to place individual detectors in each path, but, instead, the detectors could be in a global (maybe even entangled) state and interaction with the particle would change it into a different (but maybe not perfectly distinguishable) global state that depends on  $|i\rangle$ . This is done in the same spirit as collective measurements generalize fixed, adaptive, or Local operations and classical communication (LOCC) measurements.

Tracing out the detector, we find that the particle density matrix is given by

$$
\rho = \operatorname {T r} _ {\det } (| \Psi \rangle \langle \Psi |) = \sum_ {i, j = 1} ^ {N} \sqrt {p _ {i} p _ {j}} \langle \eta_ {j} | \eta_ {i} \rangle | i \rangle \langle j |, \tag {6}
$$

which, in turn, yields for our coherence measure  $X$

$$
X = \frac{1}{N} C_{l_{1}}(\rho) = \frac{1}{N}\sum_{\substack{i,j = 1\\ i\neq j}}^{N}\sqrt{p_{i}p_{j}} |\langle \eta_{j}|\eta_{i}\rangle |. \tag{7}
$$

Since path information is encoded in the detector states, we also need to introduce the detector density matrix  $\rho_{\mathrm{det}}$ . Tracing out the particle states, we find

$$
\rho_ {\mathrm {d e t}} = \operatorname {T r} _ {\text {p a r t i c l e}} (| \Psi \rangle \langle \Psi |) = \sum_ {i = 1} ^ {N} p _ {i} \rho_ {i}, \tag {8}
$$

where  $\rho_{i} = |\eta_{i}\rangle \langle \eta_{i}|$ . The set of possible detector states is assumed to be known so, in order to obtain which-path information, we need to discriminate among the states  $\{|\eta_i\rangle \}$ , which appear with probabilities  $\{p_i\}$ . To this end, we will employ the minimum-error strategy. For  $N$  states, we have an  $N$ -element Positive operator valued measure (POVM) with elements  $\Pi_{i}\geq 0$ , which satisfy  $\sum_{i = 1}^{N}\Pi_{i} = \mathbb{I}$ . The probability that detector  $i$  clicks, if we are given the state  $|\eta_i\rangle$ , is  $\langle \eta_i|\Pi_i|\eta_i\rangle$ . We identify a click in detector  $i$  with the detection of the state  $|\eta_i\rangle$ , so the average probability of successfully identifying the state is

$$
P _ {s} = \sum_ {i = 1} ^ {N} p _ {i} \langle \eta_ {i} | \Pi_ {i} | \eta_ {i} \rangle = \sum_ {i = 1} ^ {N} p _ {i} \operatorname {T r} \left(\Pi_ {i} \rho_ {i}\right). \tag {9}
$$

In minimum-error state discrimination, we seek to find a POVM that maximizes  $P_{s}$ . The solution to the problem is known in complete generality for two states [15], but only in special cases for more than two states. Here we shall employ an upper bound on the success probability to obtain our main result.

There are several upper bounds on the success probability for minimum-error state discrimination [16-20]. However, for our goals we find that another one, which we first state and later prove, is more useful. If we have  $N$  density matrices,  $\{\rho_i|i = 1,2,\dots,N\}$ , where  $\rho_{i}$  appears with probability  $p_i$ , then the success probability for minimum-error state discrimination obeys

$$
P _ {s} \leq \frac {1}{N} + \frac {1}{2 N} \sum_ {i, j = 1} ^ {N} \| \Lambda_ {i j} \| _ {1}, \tag {10}
$$

where  $\Lambda_{ij} = p_i\rho_i - p_j\rho_j$  is the Helstrom matrix of the pair of states  $\rho_{i},\rho_{j}$ , and the norm in this inequality is the trace norm. In the case of pure states,  $\rho_{i} = |\eta_{i}\rangle \langle \eta_{i}|$ , we find, by diagonalizing the operator  $\Lambda_{ij} = p_i|\eta_i\rangle \langle \eta_i| - p_j|\eta_j\rangle \langle \eta_j|$ , that

$$
\left\| \Lambda_ {i j} \right\| _ {1} = 2 \sqrt {\left(\frac {p _ {i} + p _ {j}}{2}\right) ^ {2} - p _ {i} p _ {j} | \langle \eta_ {i} | \eta_ {j} \rangle | ^ {2}}. \tag {11}
$$

This implies that the average probability of successfully identifying the detector state, entangled with a given path, is bounded above by Eq. (10), with  $\| \Lambda_{ij} \|_1$  given by Eq. (11). The quantity  $X$ , which describes the coherence, is given in Eq. (7). This gives us the upper bound for the expression on the lhs of Eq. (3):

$$
\begin{array}{l} \left(P_{s} - \frac{1}{N}\right)^{2} + X^{2}\leq \frac{1}{N^{2}}\sum_{\substack{i,j = 1\\ i\neq j}}^{N}\sum_{\substack{k,l = 1\\ k\neq l}}^{N}\left(\frac{1}{4}\| \Lambda_{ij}\|_{1}\| \Lambda_{kl}\|_{1}\right. \\ \left. + \sqrt {p _ {i} p _ {j}} | \langle \eta_ {i} | \eta_ {j} \rangle | \sqrt {p _ {k} p _ {l}} | \langle \eta_ {k} | \eta_ {l} \rangle |\right). \tag {12} \\ \end{array}
$$

For fixed  $i$  and  $j$ , the pair  $\left(\frac{1}{2}\|\Lambda_{ij}\|_1, \sqrt{p_i p_j} |\langle \eta_i|\eta_j\rangle|\right)$  can be viewed as a bra vector  $\langle v_{ij}|$  of length  $(p_i + p_j) / 2$  (and, similarly, for fixed  $k$  and  $l$ ). The term in parentheses on the rhs of Eq. (12) is the scalar product,  $\langle v_{ij}|v_{kl}\rangle$ , of two such vectors. Using the Schwarz inequality, the rhs can be bounded above by

$$
\frac {1}{N ^ {2}} \left(\sum_ {\substack {i, j = 1 \\ i \neq j}} ^ {N} \frac {p _ {i} + p _ {j}}{2}\right) ^ {2} = \left(1 - \frac {1}{N}\right) ^ {2}, \tag{13}
$$

and we recover Eq. (3).

We now give the proof of Eq. (10). The success probability of the  $N$ -element POVM was introduced in Eq. (9). An upper bound for the individual terms in the success probability can be found as

$$
\begin{array}{l} p _ {i} \operatorname {T r} \left(\Pi_ {i} \rho_ {i}\right) = p _ {j} \operatorname {T r} \left(\Pi_ {i} \rho_ {j}\right) + \operatorname {T r} \left(\Pi_ {i} \Lambda_ {i j}\right) \\ \leq p _ {j} \operatorname {T r} \left(\Pi_ {i} \rho_ {j}\right) + \max  _ {0 \leq \Pi \leq \mathbb {I}} \operatorname {T r} \left(\Pi \Lambda_ {i j}\right) \\ = p _ {j} \operatorname {T r} \left(\Pi_ {i} \rho_ {j}\right) + \operatorname {T r} \left(\Lambda_ {i j, +}\right) \\ = p _ {j} \operatorname {T r} \left(\Pi_ {i} \rho_ {j}\right) + \frac {p _ {i} - p _ {j} + \| \Lambda_ {i j} \| _ {1}}{2}, \tag {14} \\ \end{array}
$$

where the subscript "+" stands for the positive part of the operator; i.e., if  $P_{+}$  is the projection onto the space of eigenvectors of the Hermitian operator  $\Lambda_{ij}$  with positive eigenvalues, then  $\Lambda_{ij, + } = P_{+}\Lambda_{ij}P_{+}$ . Similarly, if  $P_{-}$  is the projection onto the space of eigenvectors with nonpositive eigenvalues, then we define  $\Lambda_{ij, - } = P_{-}\Lambda_{ij}P_{-}$ . For the inequality in the second line, we have used the fact that for  $\Lambda_{ij}$  one has  $\mathrm{Tr}(\Pi_i\Lambda_{ij})\leq \max_{0\leq \Pi \leq \mathbb{I}}\mathrm{Tr}(\Pi \Lambda_{ij})$ , since the maximization is over the set of positive operators less than the identity, which contains  $\Pi_{i}$ . The equality in the third line results from choosing  $\Pi$  to be the projector onto the positive part of  $\Lambda_{ij}$  and noting that  $\mathrm{Tr}(\Pi \Lambda_{ij})\leq$ $\mathrm{Tr}(\Pi \Lambda_{ij, + })\leq \mathrm{Tr}(\Lambda_{ij, + })$  for a positive operator  $\Pi$  with operator norm less than or equal to 1. The equality in the last line uses the fact that  $\mathrm{Tr}(\Lambda_{ij}) = p_i - p_j =$ $\mathrm{Tr}(\Lambda_{ij, + }) + \mathrm{Tr}(\Lambda_{ij, - })$ , and  $\| \Lambda_{ij}\| _1 = \mathrm{Tr}(\Lambda_{ij, + }) - \mathrm{Tr}(\Lambda_{ij, - })$

from which  $\mathrm{Tr}(\Lambda_{ij, + }) = (p_i - p_j + \| \Lambda_{ij}\| _1) / 2$  follows. Taking now the sum over  $i,j;i\neq j$  of both sides in the inequality Eq. (14), we find

$$
(N - 1) P _ {s} \leq 1 - P _ {s} + \frac {1}{2} \sum_ {\substack {i, j = 1 \\ i \neq j}} ^ {N} \| \Lambda_ {i j} \| _ {1}. \tag{15}
$$

Noting that  $\| \Lambda_{ij}\| _1 = 0$  for  $i = j$ , the sum in the last term can be extended to include the  $i = j$  terms, immediately yielding Eq. (10). We want to point out that for  $N = 2$ , Eq. (10) is actually an equality; it reproduces the Helstrom bound. Our bound generalizes this for arbitrary  $N$ . The first term on the rhs of Eq. (10) would be the result of random guessing, so the second term can be regarded as the gain provided by the measurement that takes into account the available prior information.

It is also possible to derive a duality relation using the entropic definition of coherence. The relative entropy coherence measure for a density matrix  $\rho$  is given by

$$
C _ {\text {r e l e n t}} (\rho) = S \left(\rho_ {\text {d i a g}}\right) - S (\rho), \tag {16}
$$

where  $\rho_{\mathrm{diag}}$  is a diagonal density matrix in the specified basis whose diagonal elements are the same as those of  $\rho$ , and  $S$  denotes the von Neumann entropy, with the logarithms taken base 2. In our case the relevant density matrix is given by Eq. (6). This gives us

$$
C _ {\text {r e l e n t}} (\rho) = H \left(\left\{p _ {j} \right\}\right) - S (\rho), \tag {17}
$$

where  $H(\{p_j\}) = -\sum_{j=1}^{N} p_j \log p_j$  is the Shannon entropy.

For path information we can consider the mutual information between the detector states labeling the paths and the results of probing them. The detector density matrix was introduced in Eq. (8), so  $\rho_{i}$  appears with a probability of  $p_i$ . Let  $D$  be a random variable corresponding to the detector states; it takes the value  $i \in \{1, 2, \dots, N\}$ , corresponding to  $\rho_{i}$ , with probability  $p_i$ . Its information content is  $H(D) = H(\{p_i\})$ . We probe the detector states with a POVM,  $\mathcal{M} = \{\Pi_i | i = 1, \dots, N\}$  in order to identify them, and thereby identify the path. Let the random variable corresponding to the measurement result be  $M$ . It takes values in the set  $\{1, 2, \dots, N\}$ . When outcome  $i$  is found, we guess that the state is  $\rho_{i}$ . Its information content is  $H(M) = H(\{q_i\})$ , where  $q_i \equiv p(M = i) = \mathrm{Tr}(\Pi_i \rho_{\mathrm{det}})$  is the probability that  $\Pi_i$  "clicks." The joint distribution for the two variables is given by  $p_{ij} \equiv p(M = i, D = j) = \mathrm{Tr}(\Pi_i \rho_j) p_j$ . Note that this situation is analogous to one in which Alice sends the state  $\rho_{i}$  with a probability of  $p_i$  to Bob, and Bob performs a state discrimination measurement in order to determine what state he received. We will quantify the path information by the mutual information  $H(M:D)$ , where

$$
H (M: D) = H (D) + H (M) - H \left(\left\{p _ {i j} \right\}\right). \tag {18}
$$

If the random variables are perfectly correlated, this is  $H(D)$ , while if they are uncorrelated, this is equal to zero.

In this situation we can make use of the Holevo bound [21], which states that if Alice sends  $\rho_{i}$  with probability  $p_i$ , and Bob measures the state he receives, then

$$
H (M: D) \leq S \left(\rho_ {\mathrm {d e t}}\right) - \sum_ {i = 1} ^ {N} p _ {i} S \left(\rho_ {i}\right). \tag {19}
$$

We recall that in our case  $\rho_{i} = |\eta_{i}\rangle \langle \eta_{i}|$ , which means that the second term above is zero so that  $H(M:D)\leq S(\rho_{\mathrm{det}})$ . Now  $\rho$  and  $\rho_{\mathrm{det}}$  are reduced density matrices of the same pure state [recall Eqs. (6) and (8)], and, therefore,  $S(\rho) = S(\rho_{\mathrm{det}})$ . Consequently, we have that

$$
C _ {\text {r e l e n t}} (\rho) + H (M; D) \leq H (\{p _ {i} \}), \tag {20}
$$

which is an entropic version of the coherence-path-information duality relation. The relation is tight, because the bound is attained when the detector states are orthogonal.

Since the bound Eq. (20) holds for any measurement, it also holds for the accessible information, defined as  $\mathrm{Acc}(D) = \max_{\mathcal{M}} H(M:D)$ , where the maximization is over all POVMs. Thus, we can also write

$$
C _ {\text {r e l e n t}} (\rho) + \operatorname {A c c} (D) \leq H \left(\left\{p _ {i} \right\}\right). \tag {21}
$$

We also note that our bound based on the  $l_{1}$  coherence measure holds for any deterministic discrimination protocol, for which all outcomes give a conclusive answer about the identity of the detector states, not just for the optimal measurement, with minimum discrimination error. The rhs of the above inequality is further upper bounded by  $\log (N)$ , the result corresponding to random guessing with no prior information. Therefore, the entropic equalities, Eqs. (20) and (21), are tighter than the  $l_{1}$  relation, Eq. (3).

In summary, we have derived two relations relating the path information about a particle inside a multipath interferometer to two recently defined measures of the coherence of a quantum system. The first of these provides a generalization of the visibility-path-information relation derived by Englert for the two-path case. Previous studies used a number of different quantities as multipath generalizations of the visibility, but our results here suggest that the recently defined  $l_{1}$  and entropic coherence measures are strong candidates.

This work was made possible through the support of a grant from the John Templeton Foundation. The opinions expressed in this Letter are those of the authors and do not necessarily reflect the views of the John Templeton Foundation. Partial financial support by a grant from PSC-CUNY is also gratefully acknowledged. The research

of E.B. was additionally supported by the Spanish MICINN, through Contract No. FIS2013-40627-P, the Generalitat de Catalunya CIRIT, Contract No. 2014SGR966, and ERDF (European Regional Development Fund). E.B. also thanks Hunter College for the hospitality extended to him during his research stay.  
[1] T. Baumgratz, M. Cramer, and M. B. Plenio, Phys. Rev. Lett. 113, 140401 (2014).  
[2] A. Winter and D. Yang, Phys. Rev. Lett. 116, 120404 (2016).  
[3] S. Cheng and M. J. Hall, Phys. Rev. A 92, 042101 (2015).  
[4] W. K. Wootters and W. H. Zurek, Phys. Rev. D 19, 473 (1979).  
[5] D. M. Greenberger and A. YaSin, Phys. Lett. A 128, 391 (1988).  
[6] G. Jaeger, A. Shimony, and L. Vaidman, Phys. Rev. A 51, 54 (1995).  
[7] B.-G. Englert, Phys. Rev. Lett. 77, 2154 (1996).  
[8] S. Durr, Phys. Rev. A 64, 042113 (2001).  
[9] G. Bimonte and R. Musto, J. Phys. A 36, 11481 (2003).

[10] B.-G. Englert and J. A. Bergou, Opt. Commun. 179, 337 (2000).  
[11] M. Jakob and J.A. Bergou, Phys. Rev. A 76, 052107 (2007).  
[12] B.-G. Englert, D. Kaszlikowski, L.C. Kwek, and W.H. Chee, Int. J. Quantum. Inform. 06, 129 (2008).  
[13] R. M. Angelo and A. D. Ribeiro, Found. Phys. 45, 1407 (2015).  
[14] M. N. Bera, T. Qureshi, M. A. Siddiqui, and A. K. Pati, Phys. Rev. A 92, 012118 (2015).  
[15] C. W. Helstrom, Quantum Detection and Estimation Theory (Academic Press, New York, 1976).  
[16] D. W. Qiu, Phys. Rev. A 77, 012328 (2008).  
[17] A. Montanaro, in Proceedings of the IEEE Information Theory Workshop, ITW08 (IEEE, Piscataway, NJ, 2008), p. 378.  
[18] J. Tyson, J. Math. Phys. (N.Y.) 50, 032106 (2009).  
[19] D.W. Qiu and L. Li, Phys. Rev. A 81, 042329 (2010).  
[20] W.-Y. Hwang and J. Bae, J. Math. Phys. (N.Y.) 51, 022202 (2010).  
[21] M. Nielsen and I. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, England, 2000).