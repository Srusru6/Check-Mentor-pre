# Experimental determination of entanglement for arbitrary pure states

Shao-Ming Fei, $^{1,2}$  Ming-Jing Zhao, $^{1}$  Kai Chen, $^{3}$  and Zhi-Xi Wang $^{1}$

$^{1}$ School of Mathematical Sciences, Capital Normal University, Beijing 100048, China

$^{2}$ Max-Planck-Institute for Mathematics in the Sciences, 04103 Leipzig, Germany

$^{3}$ Hefei National Laboratory for Physical Sciences at Microscale and Department of Modern Physics,

University of Science and Technology of China, Hefei, Anhui 230026, China

(Received 10 June 2009; published 21 September 2009)

We present a way of experimentally determining the concurrence in terms of the expectation values of local observables for arbitrary multipartite pure states. Instead of the joint measurements on two copies of a state in the experiment for two-qubit systems [S. P. Walborn et al., Nature (London) 440, 20 (2006)], we only need one copy of the state in every measurement for any arbitrary dimensional multipartite systems, avoiding the preparation of twin states or the imperfect copy of the state.

DOI: 10.1103/PhysRevA.80.032320

PACS number(s): 03.67.Mn, 03.65.Ud, 42.50.Ex

# I. INTRODUCTION

Quantum entanglement is one of the most fascinating features of quantum theory [1]. To characterize and quantify the entanglement some well defined measures such as entanglement of formation (EOF) [2,3] and concurrence [4,5] have been used. For given two-quibt or some special symmetric states explicit analytic formulas for EOF and concurrence have been found [6-11]. For arbitrary given states the entanglement can be estimated by analytic lower bounds [12-21].

Nevertheless, for unknown quantum states, to characterize the entanglement one needs experimental measurements. An important approach to detect entanglement is the Bell-type inequalities [22-26]. For instance, Gisin proved that all two-qubit pure entangled states violate the Clauser-Horne-Shimony-Holt (CHSH) inequality [24] and Chen et al. presented a Bell-type inequality that would be violated by all three-qubit pure entangled states [25]. For general mixed two-qubit states, Yu et al. [26] proposed a Bell-type inequality that gives a sufficient and necessary criterion for separability. Another experimentally plausible approach is the entanglement witness [27], which could also be used to detect certain kinds of entangled states with the present technology [28].

However, to detect the entanglement in terms of Bell-type inequalities one needs expectation values of two or more observables (two or more setting measurements) per party. And one has to do infinitely many dichotomic measurements theoretically. Moreover until now we still have no necessary and sufficient Bell inequalities to detect the entanglement for general multiqubit systems. Certain entanglement witness works only for some special states.

In fact the concurrence is defined for both bipartite and multipartite states and gives rise to not only the separability but also the degree of entanglement (at least for arbitrary dimensional bipartite states). The problem is how to use this measure to determine the entanglement for unknown quantum states experimentally.

In [29] Mintert et al. proposed a method to measure the concurrence directly by using joint measurements on two copies of a pure state. Then Walborn et al. presented an

experimental determination of concurrence for two-qubit states [30,31], where only one-setting measurement is needed, but two copies of the state have to be prepared in every measurement.

In this paper, we give a way of experimental determination of concurrence for two-qubit and multiqubit states, such that only one copy of the state is needed in every measurement. To determine the concurrence of the two-qubit state used in [30,31], also one-setting measurement is needed, which avoids the preparation of the twin states or the imperfect copy of the unknown state, and the experimental difficulty is dramatically reduced. As examples general two-qubit and three-qubit systems and generalized multiqubit GHZ states  $|\psi \rangle = a_0|0\dots 0\rangle +a_1|1\dots 1\rangle$  are investigated explicitly. The results are then generalized to the case of arbitrary dimensional multipartite pure states.

# II. CONCURRENCE FOR  $N$ -QUBIT SYSTEM

For a  $N$ -partite  $M$ -dimensional pure state  $|\psi \rangle = \sum_{i_1, \ldots, i_N = 0}^{M - 1} a_{i_1, \ldots, i_N} |i_1, \ldots, i_N\rangle$ ,  $a_{i_1, \ldots, i_N} \in \mathbb{C}$ , the concurrence is given by [32]

$$
C (| \psi \rangle) = 2 ^ {1 - N / 2} \sqrt {(2 ^ {N} - 2) - \sum_ {i} \operatorname {t r} \rho_ {i} ^ {2}}, \tag {1}
$$

where the summation goes over all  $2^{N} - 2$  subsets of the  $N$  subsystems and  $\rho_{i}$  is the corresponding reduced density matrix with respect to the  $i$ th bipartite decomposition.

Up to a constant factor,  $C(|\psi \rangle)$  can also be written as [5]

$$
C \left(\left| \psi \right\rangle\right) = \sqrt {\sum_ {p} \sum_ {\left\{\alpha , \alpha^ {\prime} , \beta , \beta^ {\prime} \right\}} ^ {M} \left| a _ {\alpha \beta} a _ {\alpha^ {\prime} \beta^ {\prime}} - a _ {\alpha \beta^ {\prime}} a _ {\alpha^ {\prime} \beta} \right| ^ {2}}, \tag {2}
$$

where  $\alpha$  and  $\alpha'$  ( $\beta$  and  $\beta'$ ) are subsets of the subindices of  $a$ , associated with the same sub-Hilbert spaces but with different summing indices.  $\alpha$  ( $\alpha'$ ) and  $\beta$  ( $\beta'$ ) span the whole space of a given subindex of  $a$ .  $\Sigma_p$  stands for the summation over all possible combinations of the indices of  $\alpha$  and  $\beta$ .

Our main aim is to re-express the concurrence in terms of the expectation values of local observables. We first give a general proof that this can be always done: the

squared concurrence of  $N$ -qubit pure state  $|\psi \rangle$ ,  $C^2 (|\psi \rangle)$ , can be expressed by the real linear summation of  $\langle \psi |\sigma_{i_1}\sigma_{i_2}\dots \sigma_{i_N}|\psi \rangle \langle \psi |\sigma_{j_1}\sigma_{j_2}\dots \sigma_{j_N}|\psi \rangle$

$$
\begin{array}{l} C ^ {2} (| \psi \rangle) = \sum_ {i _ {1}, \dots , i _ {N}; j _ {1}, \dots , j _ {N} = 0} ^ {3} x _ {i _ {1}, \dots , i _ {N}; j _ {1}, \dots , j _ {N}} \\ \times \langle \psi | \sigma_ {i _ {1}} \sigma_ {i _ {2}} \dots \sigma_ {i _ {N}} | \psi \rangle \langle \psi | \sigma_ {j _ {1}} \sigma_ {j _ {2}} \dots \sigma_ {j _ {N}} | \psi \rangle , \tag {3} \\ \end{array}
$$

where the coefficients  $x_{i_1,\dots ,i_N,j_1,\dots ,j_N}$  are real,  $\sigma_0$  is the  $2\times 2$  identity matrix, and  $\sigma_{1} = \left( \begin{array}{cc}0 & 1\\ 1 & 0 \end{array} \right),\sigma_{2} = \left( \begin{array}{cc}0 & i\\ -i & 0 \end{array} \right)$ , and  $\sigma_3 = \left( \begin{array}{cc}1 & 0\\ 0 & -1 \end{array} \right)$  are the Pauli matrices.

We only need to show that each term in the squared  $C(|\psi \rangle)$  of Eq. (2) can be written in the form of the right-hand side of Eq. (3). Note that

$$
\begin{array}{l} \left| a _ {\alpha \beta} a _ {\alpha^ {\prime} \beta^ {\prime}} - a _ {\alpha \beta^ {\prime}} a _ {\alpha^ {\prime} \beta} \right| ^ {2} \\ = \left| a _ {\alpha \beta} a _ {\alpha^ {\prime} \beta^ {\prime}} \right| ^ {2} + \left| a _ {\alpha \beta^ {\prime}} a _ {\alpha^ {\prime} \beta} \right| ^ {2} - a _ {\alpha \beta} ^ {*} a _ {\alpha^ {\prime} \beta^ {\prime}} ^ {*} a _ {\alpha \beta^ {\prime}} a _ {\alpha^ {\prime} \beta} \\ - a _ {\alpha \beta} a _ {\alpha^ {\prime} \beta^ {\prime}} a _ {\alpha \beta^ {\prime}} ^ {*} a _ {\alpha^ {\prime} \beta} ^ {*}. \tag {4} \\ \end{array}
$$

Set  $A^{(11)} = |\alpha \beta \rangle \langle \alpha \beta |, A^{(21)} = |\alpha' \beta' \rangle \langle \alpha' \beta'|, A^{(12)} = |\alpha \beta' \rangle \langle \alpha \beta'|, A^{(22)} = |\alpha' \beta\rangle \langle \alpha' \beta|$ , then

$$
\begin{array}{l} \left| a _ {\alpha \beta} a _ {\alpha^ {\prime} \beta^ {\prime}} \right| ^ {2} + \left| a _ {\alpha \beta^ {\prime}} a _ {\alpha^ {\prime} \beta} \right| ^ {2} \\ = \langle \psi | A ^ {(1 1)} | \psi \rangle \langle \psi | A ^ {(2 1)} | \psi \rangle + \langle \psi | A ^ {(1 2)} | \psi \rangle \langle \psi | A ^ {(2 2)} | \psi \rangle . \tag {5} \\ \end{array}
$$

$A^{(ij)}$ $i,j = 1,2$  , obviously has the form  $A^{(ij)} = |i_1\rangle \langle i_1|\otimes \dots$ $\otimes |i_N\rangle \langle i_N|$  , where  $i_1,\ldots ,i_N$  take value O or 1. As  $|0\rangle \langle 0|$ $= \frac{1}{2} (\sigma_0 + \sigma_3)$  and  $|1\rangle \langle 1| = \frac{1}{2} (\sigma_0 - \sigma_3)$  , we have

$$
\begin{array}{l} \left| a _ {\alpha \beta} a _ {\alpha^ {\prime} \beta^ {\prime}} \right| ^ {2} + \left| a _ {\alpha \beta^ {\prime}} a _ {\alpha^ {\prime} \beta} \right| ^ {2} \\ = \sum_ {i _ {1}, \dots , i _ {N} \cdot j _ {1}, \dots , j _ {N} = 0, 3} x _ {i _ {1}, \dots , i _ {N} \cdot j _ {1}, \dots , j _ {N}} \langle \psi | \sigma_ {i _ {1}} \sigma_ {i _ {2}} \dots \sigma_ {i _ {N}} | \psi \rangle \\ \times \langle \psi | \sigma_ {j _ {1}} \sigma_ {j _ {2}} \dots \sigma_ {j _ {N}} | \psi \rangle \\ \end{array}
$$

for some real coefficients  $x_{i_1,\dots ,i_N,j_1,\dots ,j_N}$

Denote further  $A^{(13)} = \frac{1}{\sqrt{2}} (|\alpha \beta \rangle \langle \alpha \beta^{\prime}| + |\alpha \beta^{\prime}\rangle \langle \alpha \beta |),$ $A^{(23)}$

$$
= \frac {1}{\sqrt {2}} \left(| \alpha^ {\prime} \beta \rangle \langle \alpha^ {\prime} \beta^ {\prime} | + | \alpha^ {\prime} \beta^ {\prime} \rangle \langle \alpha^ {\prime} \tilde {\beta} |\right), \quad A ^ {(1 4)} = \frac {i}{\sqrt {2}} (| \alpha \beta \rangle \langle \alpha \beta^ {\prime} |
$$

$-|\tilde{\alpha}\beta^{\prime}\rangle \langle \alpha \beta |)$ $A^{(24)} = \frac{i}{\sqrt{2}} (|\alpha^{\prime}\beta \rangle \langle \alpha^{\prime}\beta^{\prime}| - |\alpha^{\prime}\beta^{\prime}\rangle \langle \alpha^{\prime}\beta |)$  , then

$$
\begin{array}{l} - a _ {\alpha \beta} ^ {*} a _ {\alpha^ {\prime} \beta^ {\prime}} ^ {*} a _ {\alpha \beta^ {\prime}} a _ {\alpha^ {\prime} \beta} - a _ {\alpha \beta} a _ {\alpha^ {\prime} \beta^ {\prime}} a _ {\alpha \beta^ {\prime}} ^ {*} a _ {\alpha^ {\prime} \beta} ^ {*} \\ = - \left(\langle \psi | A ^ {(1 3)} | \psi \rangle \langle \psi | A ^ {(2 3)} | \psi \rangle + \langle \psi | A ^ {(1 4)} | \psi \rangle \langle \psi | A ^ {(2 4)} | \psi \rangle\right). \tag {6} \\ \end{array}
$$

It is clear that  $|\alpha \rangle \langle \alpha|, |\alpha' \rangle \langle \alpha'|, |\beta \rangle \langle \beta'|$ , and  $|\beta' \rangle \langle \beta|$  are tensor products of  $|0\rangle \langle 0|, |1\rangle \langle 1|, |0\rangle \langle 1| = \frac{1}{2} (\sigma_1 - i\sigma_2)$ , and  $|1\rangle \langle 0| = \frac{1}{2} (\sigma_1 + i\sigma_2)$ . Without loss of generality we assume  $A^{(13)} = |i_1\rangle \langle i_1| \otimes \dots \otimes |i_s\rangle \langle i_s| \otimes (|i_{s+1}\rangle \langle j_{s+1}| \otimes \dots \otimes |i_N\rangle \langle j_N|$  
$+|j_{s + 1}\rangle \langle i_{s + 1}|\otimes \dots \otimes |j_N\rangle \langle i_N|)$  , where  $1\leq s <   N$ $i_k,j_k$  take values O or 1, and  $i_k\neq j_k$  for each  $s + 1\leq k\leq N$  . The part  $|i_1\rangle \langle i_1|\otimes \dots \otimes |i_s\rangle \langle i_s|$  is the real linear summation of tensor products of  $\sigma_0$  and  $\sigma_3$  .The rest part  $T\equiv |i_{s + 1}\rangle \langle j_{s + 1}|\otimes \dots$ $\otimes |i_N\rangle \langle j_N| + |j_{s + 1}\rangle \langle i_{s + 1}|\otimes \dots \otimes |j_N\rangle \langle i_N|$  can be written as

$$
\frac {1}{2 ^ {N - s}} \bigotimes_ {l = s + 1} ^ {N} [ \sigma_ {1} + i (- 1) ^ {p _ {l}} \sigma_ {2} ] + \frac {1}{2 ^ {N - s}} \bigotimes_ {l = s + 1} ^ {N} [ \sigma_ {1} + i (- 1) ^ {1 - p _ {l}} \sigma_ {2} ],
$$

where  $p_l$  takes values 0 or 1 for each  $l$ .  $T$  is further of the form

$$
\begin{array}{l} \frac {1}{2 ^ {N - s}} \sum_ {l = 0} ^ {N - s} \sum_ {\left\{\text {N o .} l \text {o f} h _ {j} \text {i s} 1, \text {t h e o t h e r s a r e} 2 \right\}} i ^ {N - s - l} \\ N - s \\ \times \bigotimes_ {j = 1} \sigma_ {h _ {j}} [ (- 1) ^ {l _ {m}} + (- 1) ^ {N - s - l - l _ {m}} ], \\ \end{array}
$$

$0 \leq l_{m} \leq N - s - l$ . If  $N - s - l$  is even, then  $i^{N - s - l}$  is real and each factor of  $\otimes_{j = 1}^{N - s}\sigma_{h_j}$  is real. If  $N - s - l$  is odd, then  $(-1)^{l_m} + (-1)^{N - s - l - l_m} = 0$ . Hence  $A^{(13)}$  is the real linear summation of the tensor products of  $\sigma_i$ ,  $0 \leq i \leq 3$ .

Similarly one can show that  $A^{(14)}$ ,  $A^{(23)}$ , and  $A^{(24)}$  are real linear summation of tensor products of  $\sigma_{i}$ ,  $0 \leq i \leq 3$ . Thus  $-a_{\alpha \beta}^{*}a_{\alpha' \beta'}^{*}a_{\alpha \beta'}a_{\alpha' \beta} - a_{\alpha \beta}a_{\alpha' \beta'}a_{\alpha \beta'}^{*}a_{\alpha' \beta}^{*}$  and Eq. (4) can be expressed in the form of real linear summation of  $\langle \psi | \sigma_{i_1} \sigma_{i_2} \dots \sigma_{i_N} | \psi \rangle \langle \psi | \sigma_{j_1} \sigma_{j_2} \dots \sigma_{j_N} | \psi \rangle$ .

Therefore the squared concurrence of  $N$ -qubit pure states  $C^2(|\psi\rangle)$  can be expressed as the expectation values of tensor products of  $\sigma_i$  ( $0 \leq i \leq 3$ ), though such expressions may be not unique. [From Eqs. (5) and (6) one sees that it is possible to find an expression that is invariant under the permutations of the  $N$  observables.]

# A. Concurrence for two-qubit system

For any two-qubit state  $|\psi \rangle = a_{00}|00\rangle +a_{01}|01\rangle +a_{10}|10\rangle +a_{11}|11\rangle, |a_{00}|^2 +|a_{11}|^2 +|a_{10}|^2 +|a_{01}|^2 = 1,$

$$
C ^ {2} = 4 \left| a _ {0 0} a _ {1 1} - a _ {0 1} a _ {1 0} \right| ^ {2}, \tag {7}
$$

which can be expressed as

$$
\begin{array}{l} C ^ {2} = \frac {1}{2} (1 + \langle \sigma_ {3} \sigma_ {3} \rangle^ {2} - \langle \sigma_ {3} \sigma_ {0} \rangle^ {2} - \langle \sigma_ {0} \sigma_ {3} \rangle^ {2} - \langle \sigma_ {0} \sigma_ {1} \rangle^ {2} + \langle \sigma_ {3} \sigma_ {1} \rangle^ {2} \\ - \left\langle \sigma_ {0} \sigma_ {2} \right\rangle^ {2} + \left\langle \sigma_ {3} \sigma_ {2} \right\rangle^ {2}). \tag {8} \\ \end{array}
$$

Therefore for experimental determination of the concurrence, one only needs to measure  $\langle \sigma_3\sigma_3\rangle ,\langle \sigma_3\sigma_1\rangle$  and  $\langle \sigma_3\sigma_2\rangle$  . One may also find alternative expressions with symmetry under the exchange of the two qubits [34].

For states in Schmidt decomposition,  $|\psi \rangle = a_0|00\rangle +a_1|11\rangle$ $|a_0|^2 +|a_1|^2 = 1$  , we have

$$
C ^ {2} = \frac {1}{8} \left(1 + \left\langle \sigma_ {3} \sigma_ {3} \right\rangle^ {2} - \left\langle \sigma_ {0} \sigma_ {3} \right\rangle^ {2} - \left\langle \sigma_ {3} \sigma_ {0} \right\rangle^ {2}\right). \tag {9}
$$

In this case experimentally we only need to measure  $\langle \sigma_3\sigma_3\rangle$  or simply count the probability  $P(++)$ ,  $P(-)$  of projections  $|++\rangle \langle ++|$ ,  $|- - \rangle \langle - - |$  with  $| + \rangle = \frac{1}{\sqrt{2}} (|0\rangle +|1\rangle)$  and  $| - \rangle = \frac{1}{\sqrt{2}} (|0\rangle -|1\rangle)$ , respectively, since  $C^2 = 16P(+ + )P(- - )$ . For the state  $\alpha |01\rangle +\beta |10\rangle$  used in [30], it is also true that only one-setting measurement is needed. But here we only need one copy of the state in every measurement, while in [30] joint measurements on two copies of the state are needed in every measurement.

For small deviation  $|\psi^{\prime}\rangle = \sqrt{1 - \epsilon} |\psi \rangle +\sqrt{\epsilon} |\phi \rangle$  from an ideal pure state  $|\psi \rangle$  due to imperfect preparation, where  $\epsilon \in \mathrm{IR}$  and

$|\phi \rangle$  is an arbitrary pure state, our protocol shows that the concurrence obtained from the experiment is exactly the one of  $|\psi^{\prime}\rangle$ . Hence if the parameter  $\epsilon$  is small enough, the difference of the concurrence between  $|\psi \rangle$  and  $|\psi^{\prime}\rangle$  would be small enough. For a two-crystal type-I down-conversion source, with improper spatial mode matching and spectral filtering, the imperfect preparation procedure could result in mixed states,  $\rho = (1 - \epsilon) |\psi \rangle \langle \psi| + \epsilon (|\alpha|^2 |HH\rangle \langle HH| + |\beta|^2 |VV\rangle \langle VV|)$ , instead of the ideal pure state  $|\psi \rangle = \alpha |HH\rangle + \beta |VV\rangle$ , where  $H$  and  $V$  stand for horizontal and vertical linear polarizations, respectively. That is, the phase coherence between  $|HH\rangle$  and  $|VV\rangle$  is reduced by  $1 - \epsilon$ . Therefore the actual concurrence of  $\rho$  is smaller than that of  $|\psi \rangle$ ,  $C(\rho) = (1 - \epsilon) |\alpha \beta| [6,31]$ . If we still measure the state according to Eq. (8) or (9), we have  $C(\rho) = |\alpha \beta|$ . Thus the relative error due to mixing is linear in  $\epsilon$ .

Remark. In principle one can always use tomography to reconstruct the unknown state. However it requires a large number of measurements. In particular one needs  $3^{N}$ -setting measurements to reconstruct an arbitrary  $N$ -qubit density matrix. To obtain all 16 expectation values of the two-qubit density matrix, nine-setting measurements have to be used [33]. From (8) we only need three-setting measurements to quantify the entanglement of the state, which is much simpler than tomography approach.

# B. Concurrence for three-qubit system

For any pure three-qubit state  $|\psi \rangle = \sum_{i,j,k=0}^{1} a_{ijk} |ijk \rangle$ , the squared concurrence is of the form

$$
\begin{array}{l} C ^ {2} = 4 \left(\left| a _ {0 0 0} a _ {1 1 1} - a _ {0 0 1} a _ {1 1 0} \right| ^ {2} + \left| a _ {0 0 0} a _ {1 1 1} - a _ {0 1 0} a _ {1 0 1} \right| ^ {2} \right. \\ + \left| a _ {0 0 0} a _ {1 1 1} - a _ {0 1 1} a _ {1 0 0} \right| ^ {2} + \left| a _ {0 0 1} a _ {1 1 0} - a _ {0 1 0} a _ {1 0 1} \right| ^ {2} \\ + \left| a _ {0 0 1} a _ {1 1 0} - a _ {0 1 1} a _ {1 0 0} \right| ^ {2} + \left| a _ {0 1 0} a _ {1 0 1} - a _ {0 1 1} a _ {1 0 0} \right| ^ {2}) \\ + 8 \left(\left| a _ {0 0 0} a _ {0 1 1} - a _ {0 0 1} a _ {0 1 0} \right| ^ {2} + \left| a _ {0 0 0} a _ {1 0 1} - a _ {0 0 1} a _ {1 0 0} \right| ^ {2} \right. \\ + \left| a _ {0 0 0} a _ {1 1 0} - a _ {0 1 0} a _ {1 0 0} \right| ^ {2} + \left| a _ {0 0 1} a _ {1 1 1} - a _ {0 1 1} a _ {1 0 1} \right| ^ {2} \\ + \left| a _ {0 1 0} a _ {1 1 1} - a _ {0 1 1} a _ {1 1 0} \right| ^ {2} + \left| a _ {1 0 0} a _ {1 1 1} - a _ {1 0 1} a _ {1 1 0} \right| ^ {2}). \tag {10} \\ \end{array}
$$

Up to a constant factor,  $C^2$  can be expressed as

$$
\begin{array}{l} C ^ {2} = \frac {1}{4} (9 - 5 \langle \sigma_ {0} \sigma_ {3} \sigma_ {0} \rangle^ {2} - 5 \langle \sigma_ {0} \sigma_ {0} \sigma_ {3} \rangle^ {2} - 5 \langle \sigma_ {3} \sigma_ {0} \sigma_ {0} \rangle^ {2} \\ + \langle \sigma_ {0} \sigma_ {3} \sigma_ {3} \rangle^ {2} + \langle \sigma_ {3} \sigma_ {3} \sigma_ {0} \rangle^ {2} + \langle \sigma_ {3} \sigma_ {0} \sigma_ {3} \rangle^ {2} + 3 \langle \sigma_ {3} \sigma_ {3} \sigma_ {3} \rangle^ {2} \\ - 3 \langle \sigma_ {0} \sigma_ {0} \sigma_ {1} \rangle^ {2} - 3 \langle \sigma_ {0} \sigma_ {1} \sigma_ {0} \rangle^ {2} - 3 \langle \sigma_ {1} \sigma_ {0} \sigma_ {0} \rangle^ {2} - \langle \sigma_ {0} \sigma_ {3} \sigma_ {1} \rangle^ {2} \\ - \left\langle \sigma_ {1} \sigma_ {0} \sigma_ {3} \right\rangle^ {2} - \left\langle \sigma_ {3} \sigma_ {1} \sigma_ {0} \right\rangle^ {2} + 3 \left\langle \sigma_ {0} \sigma_ {1} \sigma_ {3} \right\rangle^ {2} + 3 \left\langle \sigma_ {3} \sigma_ {0} \sigma_ {1} \right\rangle^ {2} \\ + 3 \left\langle \sigma_ {1} \sigma_ {3} \sigma_ {0} \right\rangle^ {2} + \left\langle \sigma_ {3} \sigma_ {3} \sigma_ {1} \right\rangle^ {2} + \left\langle \sigma_ {3} \sigma_ {1} \sigma_ {3} \right\rangle^ {2} + \left\langle \sigma_ {1} \sigma_ {3} \sigma_ {3} \right\rangle^ {2} \\ - 3 \langle \sigma_ {0} \sigma_ {0} \sigma_ {2} \rangle^ {2} - 3 \langle \sigma_ {0} \sigma_ {2} \sigma_ {0} \rangle^ {2} - 3 \langle \sigma_ {2} \sigma_ {0} \sigma_ {0} \rangle^ {2} - \langle \sigma_ {0} \sigma_ {3} \sigma_ {2} \rangle^ {2} \\ - \left\langle \sigma_ {2} \sigma_ {0} \sigma_ {3} \right\rangle^ {2} - \left\langle \sigma_ {3} \sigma_ {2} \sigma_ {0} \right\rangle^ {2} + 3 \left\langle \sigma_ {0} \sigma_ {2} \sigma_ {3} \right\rangle^ {2} + 3 \left\langle \sigma_ {3} \sigma_ {0} \sigma_ {2} \right\rangle^ {2} \\ + 3 \left\langle \sigma_ {2} \sigma_ {3} \sigma_ {0} \right\rangle^ {2} + \left\langle \sigma_ {3} \sigma_ {3} \sigma_ {2} \right\rangle^ {2} + \left\langle \sigma_ {3} \sigma_ {2} \sigma_ {3} \right\rangle^ {2} + \left\langle \sigma_ {2} \sigma_ {3} \sigma_ {3} \right\rangle^ {2}), \tag {11} \\ \end{array}
$$

which is invariant under the permutations of the three qubits. For experimental determination of the concurrence for arbitrary three-qubit states, seven quantities are needed to be

measured:  $\langle \sigma_3\sigma_3\sigma_3\rangle ,\langle \sigma_3\sigma_3\sigma_1\rangle ,\langle \sigma_3\sigma_1\sigma_3\rangle ,\langle \sigma_1\sigma_3\sigma_3\rangle ,$ $\langle \sigma_3\sigma_3\sigma_2\rangle ,\langle \sigma_3\sigma_2\sigma_3\rangle ,$  and  $\langle \sigma_{2}\sigma_{3}\sigma_{3}\rangle$

In particular for the three-qubit generalized GHZ state,  $|\psi \rangle = a_0|000\rangle +a_1|111\rangle$ ,  $|a_0|^2 +|a_1|^2 = 1$ , and the generalized  $W$  state,  $|\psi \rangle = a_0|001\rangle +a_1|010\rangle +a_2|100\rangle$ ,  $|a_0|^2 +|a_1|^2 +|a_2|^2 = 1$ , their squared concurrence are  $12|a_0a_1|^2$  and  $8(|a_0a_1|^2 +|a_0a_2|^2 +|a_1a_2|^2)$ , respectively. The concurrence of both generalized GHZ states and generalized  $W$  states can be measured according to the following formula:

$$
\begin{array}{l} C ^ {2} = \frac {1}{4} (9 - 5 \langle \sigma_ {0} \sigma_ {3} \sigma_ {0} \rangle^ {2} - 5 \langle \sigma_ {0} \sigma_ {0} \sigma_ {3} \rangle^ {2} - 5 \langle \sigma_ {3} \sigma_ {0} \sigma_ {0} \rangle^ {2} \\ + \left\langle \sigma_ {0} \sigma_ {3} \sigma_ {3} \right\rangle^ {2} + \left\langle \sigma_ {3} \sigma_ {3} \sigma_ {0} \right\rangle^ {2} + \left\langle \sigma_ {3} \sigma_ {0} \sigma_ {3} \right\rangle^ {2} + 3 \left\langle \sigma_ {3} \sigma_ {3} \sigma_ {3} \right\rangle^ {2}). \tag {12} \\ \end{array}
$$

Equation (12) shows that for experimental determination of entanglement for these states, one needs only one-setting measurement,  $\langle \sigma_3\sigma_3\sigma_3\rangle$

Similar results can be obtained for multiqubit systems such as  $N$ -qubit generalized GHZ state  $|\psi \rangle = a_0|0\dots 0\rangle +a_1|1\dots 1\rangle$ ,  $|a_0|^2 +|a_1|^2 = 1$  or  $N$ -qubit generalized  $W$  state  $|\psi \rangle = a_0|0\dots 01\rangle +a_1|0\dots 10\rangle +\dots +a_{N - 1}|10\dots 0\rangle$ ,  $|a_0|^2 +|a_1|^2 +\dots +|a_{N - 1}|^2 = 1$ . For instance for the generalized GHZ state, the concurrence is  $|a_0a_1|$  up to a constant. Its squared concurrence can be expressed as follows:

$$
\begin{array}{l} C ^ {2} = 1 + \sum_ {k, k ^ {\prime} \text {e v e n}} ^ {1 \leq k, k ^ {\prime} \leq N} \langle \sigma_ {3} ^ {(i _ {1} \dots i _ {k})} \rangle \langle \sigma_ {3} ^ {(j _ {1} \dots j _ {k ^ {\prime}})} \rangle \\ 1 \leq l, l ^ {\prime} \leq N \\ - \sum_ {l, l ^ {\prime} \text {o d d}} \left\langle \sigma_ {3} ^ {\left(i _ {1} \dots i _ {l}\right)} \right\rangle \left\langle \sigma_ {3} ^ {\left(j _ {1} \dots j _ {l ^ {\prime}}\right)} \right\rangle , \tag {13} \\ \end{array}
$$

where  $\langle \sigma_3^{(i_1\dots i_k)}\rangle$  denotes the expectation value of the local operators such that the  $i_{1}\mathrm{th},\ldots ,i_{k}\mathrm{th}$  are  $\sigma_{3}$  operators and the rest are identities.

# III. CONCURRENCE FOR  $N$ -PARTITE M-DIMENSIONAL SYSTEM

Besides qubit systems, our approach can also be used for arbitrary  $M$ -dimensional cases. Instead of the Pauli operators, one can use the  $\mathrm{SU}(M)$  generators as observables,

$$
\lambda_ {0} = \sum_ {j = 0} ^ {M - 1} | j \rangle \langle j |,
$$

$$
\lambda_ {s} = \sum_ {j = 0} ^ {s - 1} | j \rangle \langle j | - s | s \rangle \langle s |, \quad 1 \leq s \leq M - 1,
$$

$$
\lambda_ {s} = \left| j \right\rangle \langle k | + \left| k \right\rangle \langle j |, \quad s = M, \dots , \frac {1}{2} (M + 2) (M - 1),
$$

$$
\lambda_ {s} = - i (| j \rangle \langle k | - | k \rangle \langle j |), \quad s = \frac {1}{2} (M + 1) M, \dots , M ^ {2} - 1,
$$

where  $0 \leq j < k \leq M - 1$ . Note that

$$
\begin{array}{l} \left| 0 \right\rangle \langle 0 \mid = \frac {1}{M} \lambda_ {0} + \frac {1}{M (M - 1)} \lambda_ {M - 1} + \frac {1}{(M - 1) (M - 2)} \lambda_ {M - 2} + \dots \\ + \frac {1}{3 \times 2} \lambda_ {2} + \frac {1}{2} \lambda_ {1}, \\ \end{array}
$$

$$
\begin{array}{l} \left| 1 \right\rangle \langle 1 \mid = \frac {1}{M} \lambda_ {0} + \frac {1}{M (M - 1)} \lambda_ {M - 1} + \frac {1}{(M - 1) (M - 2)} \lambda_ {M - 2} + \dots \\ + \frac {1}{3 \times 2} \lambda_ {2} - \frac {1}{2} \lambda_ {1}, \\ \end{array}
$$

：

$$
\left| M - 2 \right\rangle \left\langle M - 2 \right| = \frac {1}{M} \lambda_ {0} + \frac {1}{M (M - 1)} \lambda_ {M - 1} - \frac {1}{M - 1} \lambda_ {M - 2},
$$

$$
\left| M - 1 \right\rangle \left\langle M - 1 \right| = \frac {1}{M} \lambda_ {0} - \frac {1}{M} \lambda_ {M - 1},
$$

and for  $0 \leq j < k \leq M - 1$ ,  $|j\rangle \langle k| = \frac{1}{2} (\lambda_s + i\lambda_{s'})$  and  $|k\rangle \langle j| = \frac{1}{2} (\lambda_s - i\lambda_{s'})$  for some  $M \leq s \leq \frac{1}{2}(M + 2)(M - 1)$  and  $\frac{1}{2}(M + 1)M \leq s' \leq M^2 - 1$ . Similar to the proof of  $N$ -qubit system, it is direct to show that the squared concurrence of the  $N$ -partite  $M$ -dimensional pure state  $|\psi\rangle$  can be expressed in terms of real linear summation of  $\langle \psi | \lambda_{i_1} \lambda_{i_2} \dots \lambda_{i_N} | \psi \rangle \langle \psi | \lambda_{j_1} \lambda_{j_2} \dots \lambda_{j_N} | \psi \rangle$ ,

$$
\begin{array}{l} C ^ {2} (| \psi \rangle) = \sum_ {i _ {1}, \dots , i _ {N}; j _ {1}, \dots , j _ {N} = 0} ^ {M ^ {2} - 1} x _ {i _ {1}, \dots , i _ {N}; j _ {1}, \dots , j _ {N}} \langle \psi | \lambda_ {i _ {1}} \lambda_ {i _ {2}} \dots \lambda_ {i _ {N}} | \psi \rangle \\ \times \langle \psi | \lambda_ {j _ {1}} \lambda_ {j _ {2}} \dots \lambda_ {j _ {N}} | \psi \rangle , \tag {14} \\ \end{array}
$$

where  $x_{i_1,\dots ,i_N,j_1,\dots ,j_N}$  are real.

# IV. CONCLUSIONS

We have proposed a method for experimentally determining the concurrence in terms of the expectation value of local observables, which gives not only sufficient and necessary conditions for separability of the quantum states but also the relative degree of entanglement. Moreover unlike the case of Bell-type inequalities where measurements are needed with respect to infinitely many observables, we need only mean value of a few observables. And instead of the joint measurement on two copies of the state needed in the experiment [29-31] for two-qubit states, we need only the usual measurements on one copy of the state in every measurement for any arbitrary dimensional multipartite states, which dramatically simplifies the experiment and reduces the error rates and the imperfectness in the preparation of the states. Compared with entanglement witnesses, for which some a priori knowledge about the states under investigation is needed, we do not need any information before measuring the state in experiment.

# ACKNOWLEDGMENTS

This work is supported by the NSFC 10675086, NSFC 10875081, NSFC 10871227,KZ200810028013,and NKBRPC (2004CB318000).

[1] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, 2000).  
[2] C. H. Bennett, D. P. DiVincenzo, J. A. Smolin, and W. K. Wootters, Phys. Rev. A 54, 3824 (1996); M. B. Plenio and S. Virmani, Quantum Inf. Comput. 7, 1 (2007).  
[3] M. Horodecki, Quantum Inf. Comput. 1, 3 (2001); D. Bruß, J. Math. Phys. 43, 4237 (2002).  
[4] A. Uhlmann, Phys. Rev. A 62, 032307 (2000); P. Rungta, V. Buzek, C. M. Caves, M. Hillary, and G. J. Milburn, ibid. 64, 042315 (2001).  
[5] S. Albeverio and S. M. Fei, J. Opt. B: Quantum Semiclassical Opt. 3, 223 (2001).  
[6] W. K. Wootters, Phys. Rev. Lett. 80, 2245 (1998).  
[7] B. M. Terhal and Karl Gerd H. Vollbrecht, Phys. Rev. Lett. 85, 2625 (2000).  
[8] S. M. Fei, J. Jost, X. Q. Li-Jost, and G. F. Wang, Phys. Lett. A 310, 333 (2003).  
[9] S. M. Fei and X. Q. Li-Jost, Rep. Math. Phys. 53, 195 (2004).  
[10] S. M. Fei, Z. X. Wang, and H. Zhao, Phys. Lett. A 329, 414 (2004).  
[11] P. Rungta and C. M. Caves, Phys. Rev. A 67, 012307 (2003).  
[12] F. Mintert, M. Kus, and A. Buchleitner, Phys. Rev. Lett. 92, 167902 (2004).  
[13] K. Chen, S. Albeverio, and S. M. Fei, Phys. Rev. Lett. 95, 210501 (2005).

[14] K. Chen, S. Albeverio, and S. M. Fei, Phys. Rev. Lett. 95, 040504 (2005).  
[15] H. P. Breuer, J. Phys. A 39, 11847 (2006).  
[16] H. P. Breuer, Phys. Rev. Lett. 97, 080501 (2006).  
[17] J. I. de Vicente, Phys. Rev. A 75, 052320 (2007).  
[18] C. J. Zhang, Y. S. Zhang, S. Zhang, and G. C. Guo, Phys. Rev. A 76, 012334 (2007).  
[19] X. H. Gao, S. M. Fei, and K. Wu, Phys. Rev. A 74, 050303(R) (2006).  
[20] E. Gerjuoy, Phys. Rev. A 67, 052308 (2003).  
[21] Y. C. Ou, H. Fan, and S. M. Fei, Phys. Rev. A 78, 012311 (2008).  
[22] J. S. Bell, Physics (Long Island City, N.Y.) 1, 195 (1964).  
[23] J. Clauser, M. Horne, A. Shimony, and R. Holt, Phys. Rev. Lett. 23, 880 (1969).  
[24] N. Gisin, Phys. Lett. A 154, 201 (1991).  
[25] J. L. Chen, C. F. Wu, L. C. Kwek, and C. H. Oh, Phys. Rev. Lett. 93, 140407 (2004).  
[26] S. Yu, J. W. Pan, Z. B. Chen, and Y. D. Zhang, Phys. Rev. Lett. 91, 217903 (2003).  
[27] M. Horodecki, P. Horodecki, and R. Horodecki, Phys. Lett. A 223, 1 (1996); B. M. Terhal, ibid. 271, 319 (2000).  
[28] M. Bourennane, M. Eibl, C. Kurtsiefer, S. Gaertner, H. Weinfurter, O. Gühne, P. Hyllus, D. Bruß, M. Lewenstein, and A. Sanpera, Phys. Rev. Lett. 92, 087902 (2004).  
[29] F. Mintert, M. Kuš, and A. Buchleitner, Phys. Rev. Lett. 95, 260502 (2005).

[30] S. P. Walborn, P. H. Souto Ribeiro, L. Davidovich, F. Mintert, and A. Buchleitner, Nature (London) 440, 1022 (2006).  
[31] S. P. Walborn, P. H. Souto Ribeiro, L. Davidovich, F. Mintert, and A. Buchleitner, Phys. Rev. A 75, 032338 (2007).  
[32] L. Aolita and F. Mintert, Phys. Rev. Lett. 97, 050501 (2006).  
[33] C. F. Roos, G. P. T. Lancaster, M. Riebe, H. Häffner, W.

Hänsel, S. Gulds, C. Becher, J. Eschner, F. Schmidt-Kaler, and R. Blatt, Phys. Rev. Lett. 92, 220402 (2006).  
[34] For instance,  $C^2 = \frac{1}{16} (2 + 2\langle \sigma_3\sigma_3\rangle^2 - 2\langle \sigma_3\sigma_0\rangle^2 - 2\langle \sigma_0\sigma_3\rangle^2$  
-  $\langle \sigma_0\sigma_1\rangle^2 -\langle \sigma_1\sigma_0\rangle^2 +\langle \sigma_3\sigma_1\rangle^2 +\langle \sigma_1\sigma_3\rangle^2 -\langle \sigma_0\sigma_2\rangle^2 -\langle \sigma_2\sigma_0\rangle^2$  
+  $\langle \sigma_3\sigma_2\rangle^2 +\langle \sigma_2\sigma_3\rangle^2)$