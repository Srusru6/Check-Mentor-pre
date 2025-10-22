# Bell-Type Inequalities to Detect True  $n$ -Body Nonseparability

Daniel Collins, $^{1,2}$  Nicolas Gisin, $^{3}$  Sandu Popescu, $^{1,2}$  David Roberts, $^{1}$  and Valerio Scarani $^{3}$

<sup>1</sup>H.H. Wills Physics Laboratory, University of Bristol, Tyndall Avenue, Bristol BS8 1TL, United Kingdom

$^{2}$ BRIMS, Hewlett-Packard Laboratories, Stoke Gifford, Bristol BS12 6QZ, United Kingdom

<sup>3</sup>Group of Applied Physics, University of Geneva, 20 rue de l'Ecole-de-Médecine, CH-1211 Geneva 4, Switzerland

(Received 1 February 2002; published 12 April 2002)

We analyze the structure of correlations among more than two quantum systems. We introduce a classification of correlations based on the concept of nonseparability, which is different a priori from the concept of entanglement. Generalizing a result of Svetlichny [Phys. Rev. D 35, 3066 (1987)] on three-particle correlations, we find an inequality for  $n$ -particle correlations that holds under the most general separability condition and that is violated by some quantum-mechanical states.

DOI: 10.1103/PhysRevLett.88.170405

PACS numbers: 03.65.Ud, 03.67.-a

Quantum mechanics (QM) predicts remarkable correlations between the outcomes of measurements on subsystems (particles) of a composed system. This prediction is a consequence of the linearity of QM, which allows one to build superposition states that cannot be written as products of states of each subsystem. Such states are called entangled. Entanglement is at the heart of some of the most puzzling features of QM: the Einstein-Podolski-Rosen argument, the measurement problem, the paradox of Schrödinger cat .... In the past decade, it has been noticed that entanglement is also a resource that allows one to perform tasks that would be classically impossible. This new, more effective standpoint caused a renewed interest in the study of quantum correlations [1].

The correlations among more than two quantum systems have been the object of several recent studies, also motivated by the fact that experiments aimed to check such correlations are becoming feasible. Usually, the structure of correlation has been classified according to entanglement. In this Letter, we propose a complementary classification, in terms of nonseparability. Before entering the technicalities, it is useful to explain why the concepts of entanglement and of nonseparability are a priori different concepts. We do this on the simplest case, that of correlations between three particles.

The classification through entanglement presupposes that the system of three particles admits a quantum-mechanical description. Thus, any state of the system is described by a density matrix  $\rho$ . To classify a given  $\rho$  in terms of entanglement, one must consider all possible decompositions of the state as a mixture of pure states  $\rho = \sum_{i} p_{i} |\Psi_{i}\rangle \langle \Psi_{i}|$ . Then, (i) if there exists a decomposition for which all  $|\Psi_{i}\rangle$  are product states  $|\psi_{i}^{1}\rangle |\psi_{i}^{2}\rangle |\psi_{i}^{3}\rangle$ , then  $\rho$  is not entangled at all; that is, it can be prepared by acting on each subsystem separately. For this situation, we use the acronym  $1/1/1$ QM. (ii) If all  $|\Psi_{i}\rangle$  can be written as either  $|\psi_{i}^{12}\rangle |\psi_{i}^{3}\rangle$  or  $|\psi_{i}^{13}\rangle |\psi_{i}^{2}\rangle$  or  $|\psi_{i}^{23}\rangle |\psi_{i}^{1}\rangle$ , and at least one of the  $|\psi_{i}^{jk}\rangle$  is not a product state, then  $\rho$  is entangled, but there is no true three-particle entanglement. We shall say that  $\rho$  exhibits two-particle entanglement,

and use the acronym 2/1QM to refer to it. (iii) Finally, if for any decomposition there is at least one  $|\Psi_i\rangle$  that shows three-particle entanglement, then to prepare  $\rho$  one must act on the three subsystems:  $\rho$  exhibits true three-particle entanglement (acronym 3QM).

It is difficult to establish to which class a given  $\rho$  belongs, because, in principle, one should write down all the possible decompositions of  $\rho$  onto pure states. In fact, to date no general criterion is known. However, we know a sufficient criterion: There exists an operator  $\mathcal{M}_3$  such that (a) if  $\mathrm{Tr}(\rho \mathcal{M}_3) > 1$ , then certainly  $\rho$  is entangled; (b) if  $\mathrm{Tr}(\rho \mathcal{M}_3) > \sqrt{2}$ , then certainly  $\rho$  exhibits true three-particle entanglement. The operator  $\mathcal{M}_3$  is the Bell operator that defines the so-called Mermin inequality [2]; we shall come back to it later.

The classification through nonseparability (or nonlocality) does not presuppose that the system of three particles admits a quantum-mechanical description. Rather, we have the following cases:

(i) Each particle separately carries a script  $\lambda$ , which determines the outcome of each possible measurement. When the experiment is repeated, the script can be different—the script  $\lambda$  occurring with probability  $\rho(\lambda)$ . This is the so-called local variables ( $l\nu$ ) model, which we will also denote as  $1/1/1S$ . More exactly, in the  $l\nu$  model, the joint probabilities  $P(a_{1},a_{2},a_{3})$  that an arbitrary experiment  $A_{1}$  performed on particle 1 yields the result  $a_{1}$ , while the measurement  $A_{2}$  performed on particle 2 yields  $a_{2}$  and the measurement  $A_{3}$  on particle 3 yields  $a_{3}$ , is given by

$$
P \left(a _ {1}, a _ {2}, a _ {3}\right) = \int d \lambda \rho (\lambda) P _ {1} \left(a _ {1} \mid \lambda\right) P _ {2} \left(a _ {2} \mid \lambda\right) P _ {3} \left(a _ {3} \mid \lambda\right), \tag {1}
$$

where  $P_{1}(a_{1}|\lambda)$  is the probability that when particle 1 carrying the script  $\lambda$  is subjected to a measurement of  $A_{1}$  it yields the result  $a_{1}$ , and similarly for  $P_{2}$  and  $P_{3}$ . Note that  $l\nu$  is more general than  $1/1/1\mathrm{QM}$ . For instance, in  $l\nu$  one can build a state such that the measurement of the spin of particle 1 along both directions  $\hat{z}$  and  $\hat{x}$  gives  $+1$  with certainty, while such a state does not exist in QM.

(ii) The intermediate case, first considered by Svetlichny [3], is a hybrid local-nonlocal model: for each triple of particles, we allow an arbitrary (i.e., nonlocal) correlation between two of the three particles, but only local correla

tions between these two particles and the third one; which pair of particles is nonlocally correlated may be different in each repetition of the experiment. If we define  $p_{i,j}$  to be the probability that particles  $i$  and  $j$  are nonlocally correlated, then in this model

$$
P _ {1, 2, 3} \left(a _ {1}, a _ {2}, a _ {3}\right) = \sum_ {k = 1} ^ {3} p _ {i, j} \int d \lambda \left[ \rho_ {i, j} (\lambda) P _ {i, j} \left(a _ {i}, a _ {j} \mid \lambda\right) P _ {k} \left(A _ {k} = a _ {k} \mid \lambda\right) \right], \tag {2}
$$

where  $\{i,j,k\}$  is an even permutation of  $\{1,2,3\}$ . We refer to this situation by the acronym  $2/1S$ . Note again that  $2/1S$  is more general than  $2/1QM$ , since we do not require that the two correlated particles are correlated according to QM.

(iii) The last situation (3S) is the one without constraints: We allow all three particles to share an arbitrary correlation.

It is not evident a priori whether three-particle entanglement 3QM is stronger, equivalent, or weaker than  $2/1S$ . The proof that 3QM is actually stronger than  $2/1S$  was given some years ago by Svetlichny [3], who found an inequality for three particles that holds for  $2/1S$  and is violated by QM. In this Letter, we are going to exhibit a generalized Svetlichny inequality for an arbitrary number of particles  $n$ , that is, an inequality that allows one to discriminate  $n$ -particle entanglement  $n\mathrm{QM}$  from any hybrid model  $k/(n-k)S$ .

The plan of the paper is as follows. First, we introduce the family of the Mermin-Klyshko (MK) inequalities [2,4], which will be the main tool for this study. With this tool, we rederive Svetlichny's inequality for three particles and compare it to Mermin's. We move then to the case of four particles, and show that the MK inequality plays the role of generalized Svetlichny inequality. Finally, we generalize our results for an arbitrary number of particles  $n$ .

We consider, from now on, an experimental situation in which two dichotomic measurements  $A_{j}$  and  $A_{j}^{\prime}$  can be performed on each particle  $j = 1,\dots ,n$ . The outcomes of these measurements are written  $a_{j}$  and  $a_{j}^{\prime}$ , and can take the values  $\pm 1$ . Letting  $M_{1} = a_{1}$ , we can define recursively the MK polynomials as

$$
M _ {n} = \frac {1}{2} M _ {n - 1} \left(a _ {n} + a _ {n} ^ {\prime}\right) + \frac {1}{2} M _ {n - 1} ^ {\prime} \left(a _ {n} - a _ {n} ^ {\prime}\right), \tag {3}
$$

where  $M_k'$  is obtained from  $M_k$  by exchanging all the primed and nonprimed  $a$ 's. In particular, we have

$$
M _ {2} = \frac {1}{2} \left(a _ {1} a _ {2} + a _ {1} ^ {\prime} a _ {2} + a _ {1} a _ {2} ^ {\prime} - a _ {1} ^ {\prime} a _ {2} ^ {\prime}\right), \tag {4}
$$

$$
M _ {3} = \frac {1}{2} \left(a _ {1} a _ {2} a _ {3} ^ {\prime} + a _ {1} a _ {2} ^ {\prime} a _ {3} + a _ {1} ^ {\prime} a _ {2} a _ {3} - a _ {1} ^ {\prime} a _ {2} ^ {\prime} a _ {3} ^ {\prime}\right). \tag {5}
$$

The recursive relation (3) gives, for all  $1 \leq k \leq n - 1$ ,

$$
M _ {n} = \frac {1}{2} M _ {n - k} \left(M _ {k} + M _ {k} ^ {\prime}\right) + \frac {1}{2} M _ {n - k} ^ {\prime} \left(M _ {k} - M _ {k} ^ {\prime}\right). \tag {6}
$$

We shall interpret these polynomials as sums of expectation values; e.g., we shall interpret  $M_2$  as

$$
\frac {1}{2} \left[ E \left(A _ {1} A _ {2}\right) + E \left(A _ {1} ^ {\prime} A _ {2}\right) + E \left(A _ {1} A _ {2} ^ {\prime}\right) - E \left(A _ {1} ^ {\prime} A _ {2} ^ {\prime}\right) \right], \tag {7}
$$

where  $E(A_{1}A_{2})$  is the expectation value of the product  $A_{1}A_{2}$  when  $A_{1}$  and  $A_{2}$  are measured (note that  $A_{1}$  and  $A_{1}'$  cannot be measured at the same time). We call quantities such as  $E(A_{1}A_{2}A_{3})$  correlation coefficients. We shall look at the values of these polynomials under QM and hybrid local/nonlocal variable models, and show that they give generalized Bell inequalities.

We shall first look at hybrid local/nonlocal variable models. For technical simplicity, throughout this paper we consider only deterministic versions of the hybrid variable models, which means that the script  $\lambda$  in Eqs. (1) and (2) completely determines the outcome of the measurements [i.e., the probabilities  $P_{1}(X = x|\lambda)$  and similar are either zero or one]. It is known that any nondeterministic local variable model can be made deterministic by adding additional variables [5]. In addition, we can also use the script  $\lambda$  to determine which particles are allowed to communicate nonlocally: e.g., for three parties, the probabilities are now given simply by

$$
P \left(a _ {1}, a _ {2}, a _ {3}\right) = \int d \lambda \rho (\lambda) P \left(a _ {1}, a _ {2}, a _ {3} \mid \lambda\right), \tag {8}
$$

where for each  $\lambda$  the probabilities must factorize as some  $2/1$  grouping (though not necessarily the same for different  $\lambda$ ). Now, for any  $\lambda$ , the outcomes of all products  $A_{1}A_{2}A_{3}$  etc. are fixed, and so we can define the fixed quantity  $M_{n}^{\lambda}$ . The value of  $M_{n}$  is just the probabilistic average over  $\lambda$  of  $M_{n}^{\lambda}$ . Thus, if we can put a bound upon all possible  $M_{n}^{\lambda}$ , then we have a bound upon  $M_{n}$ . For example, it can be shown that, for any  $lv$  model,  $M_{n} \leq 1$ . This can be easily seen from (3) using a recursive argument, noting that for any script of local variables it holds that either  $a_{n} = a_{n}^{\prime}$  or  $a_{n} = -a_{n}^{\prime}$ . In particular,  $M_{2} \leq 1$  for  $lv$  is the Clauser-Horne-Shimony-Holt inequality for two particles [6]. On the opposite side, if we consider the model without constraints  $nS$ , then  $M_{n}$  can reach the so-called algebraic limit  $M_{n}^{\mathrm{alg}}$ , achieved by setting at  $+1$  (respectively  $-1$ ) all the correlation coefficients that appear in  $M_{n}$  with a positive (respectively negative) sign. So, for example,  $M_{2}^{\mathrm{alg}} = M_{3}^{\mathrm{alg}} = 2$ .

Turning to QM, since we consider dichotomic measurements, we can restrict to the case of two-dimensional systems (qubits) [7]. In this case, the observable that describes the measurement  $A_{j}$  can be written as  $\vec{a}_j\cdot \vec{\sigma}\equiv \sigma_{a_j}$  with  $\vec{a}_j$  a unit vector and  $\vec{\sigma}$  the Pauli matrices. The equivalent of  $M_{n}$  is the expectation value of the operator  $\mathcal{M}_n$  obtained by replacing all  $a$ 's by the corresponding  $\sigma_{a}$ . It is thus known that QM violates the inequality

$\mathrm{Tr}(\rho \mathcal{M}_n) \leq 1$ . More precisely, it is known [4] that (I) the maximal value achievable by QM is  $\mathrm{Tr}(\rho \mathcal{M}_n) = 2^{(n - 1) / 2}$ , reached by the generalized Greenberger-Horne-Zeilinger (GHZ) states  $(1 / \sqrt{2})(|0\dots 0\rangle + |1\dots 1\rangle)$ ; (II) if  $\rho$  exhibits  $m$ -particle entanglement, with  $1 \leq m \leq n$ , then  $\mathrm{Tr}(\rho \mathcal{M}_n) \leq 2^{(m - 1) / 2}$  [8]. In other words, if we have a state of  $n$  qubits  $\rho$  such that  $\mathrm{Tr}(\rho \mathcal{M}_n) > 2^{(m - 1) / 2}$ , we know that this state exhibits at least  $(m + 1)$ -particle entanglement. This means that the MK polynomials allow a classification of correlations according to entanglement. But do they allow also the classification according to nonseparability? The answer to this question: yes for  $n$  even, no for  $n$  odd. As announced, we demonstrate this statement first for  $n = 3$ , then for  $n = 4$ , and finally for all  $n$ .

Three particles. Let us take the Mermin polynomial  $M_3$  given in (5). We have already discussed the following bounds:  $M_3^{lv} = 1$ ,  $M_3^{2/1\mathrm{QM}} = \sqrt{2}$ ,  $M_3^{3\mathrm{QM}} = M_3^{\mathrm{alg}} = 2$ . We lack the bound for  $2/1S$ . This is easily calculated: Consider a script in which particles 1 and 2 are correlated in the most general way, and particle 3 is uncorrelated with the others. Then we use (3), which reads  $M_3 = \frac{1}{2}M_2(a_3 + a_3') + \frac{1}{2}M_2'(a_3 - a_3')$ . For any particular script, as we said above,  $a_3$  can only be equal to  $\pm a_3'$ . Without loss of generality, we choose  $a_3 = a_3' = 1$ , whence  $M_3^{2/1S} = \max M_2$ . Since particles 1 and 2 can have the highest correlation,  $\max M_2 = M_2^{\mathrm{alg}}$  here. In conclusion,  $M_3^{2/1S} = 2$ . Thus, for Mermin's polynomial,

$$
M _ {3} ^ {2 / 1 S} = M _ {3} ^ {3 \mathrm {Q M}} = M _ {3} ^ {\mathrm {a l g}} = 2. \tag {9}
$$

The Mermin polynomial does not discriminate between the deterministic variable models  $2/1S$  and  $3S$ , and the quantum-mechanical correlation due to three-particle entanglement. The deep reason for this behavior lies in the fact that  $M_3$  has only four terms: The correlations  $a_1a_2a_3$ ,  $a_1'a_2a_3$ ,  $a_1'a_2a_3'$ , and  $a_1a_2'a_3'$  do not appear in  $M_3$  given in (5). But these correlations are those that appear in  $M_3'$ ; thus we are led to check the properties of the polynomial,

$$
S _ {3} = \frac {1}{2} \left(M _ {3} + M _ {3} ^ {\prime}\right) = \frac {1}{2} \left(M _ {2} a _ {3} ^ {\prime} + M _ {2} ^ {\prime} a _ {3}\right). \tag {10}
$$

For both  $l\nu$  and  $2/1S$ , the calculation goes as follows: We choose  $a_3 = a_3' = 1$ , and we are left with  $S_3^{\mathrm{~~\ddots~}} = \frac{1}{2}\max (M_2 + M_2')$ . But  $M_2 + M_2' = a_1a_2' + a_1'a_2$ , which can take the value of 2 in both  $l\nu$  and  $2/1S$ . Therefore  $S_3^{l\nu} = S_3^{2/1S} = 1$ , and this implies immediately  $S_3^{2/1\mathrm{QM}} = 1$  since  $2/1\mathrm{QM}$  is more general than  $l\nu$  and is a particular case of  $2/1S$ . The algebraic maximum is obviously  $S_3^{\mathrm{alg}} = 2$ . We have to find  $S_3^{3\mathrm{QM}}$ . As above, we define an operator  $S_3$  by replacing the  $a$ 's in the polynomial  $S_3$  with Pauli matrices. On the one hand, we have

$$
\operatorname {T r} \left(\rho S _ {3}\right) = \frac {1}{2} \left[ \operatorname {T r} \left(\rho \mathcal {M} _ {2} \sigma_ {a _ {3} ^ {\prime}}\right) + \operatorname {T r} \left(\rho \mathcal {M} _ {2} ^ {\prime} \sigma_ {a _ {3}}\right) \right] \leq \sqrt {2}, \tag {11}
$$

since by the Cirel'son theorem [9] each term of the sum is bounded by  $\sqrt{2}$ . On the other hand, we know [10] that the eigenvector associated to the maximal eigenvalue for such an operator is the GHZ state  $(1 / \sqrt{2})(|000\rangle + |111\rangle)$ . For some settings [11], we have  $\langle \mathrm{GHZ}|S_3|\mathrm{GHZ}\rangle = \sqrt{2}$ : The bound can be reached; that is,  $S_3^{3\mathrm{QM}} = \sqrt{2}$ . Thus, the GHZ state generates genuine three-party nonseparability (non-locality). We note that, in fact,  $S_3$  is one of Svetlichny's two inequalities [the second inequality is equivalent, and is associated to  $\frac{1}{2} (M_3 - M_3')$ ].

The results for Mermin's and Svetlichny's inequalities for three particles are summarized in Table I. We see that combining Mermin's and Svetlichny's inequalities one can discriminate between the five models for correlations that we consider in this paper. This concludes our study of the case of three particles.

Four particles. As above, we begin by considering the MK polynomial  $M_4$ . Like  $M_2$ , and unlike  $M_3$ , the polynomial  $M_4$  is a linear combination of the correlation coefficients of all measurements. From the general properties of the MK inequalities [4], the following bounds are known:  $M_4^{lv} = 1$ ,  $M_4^{1/1/2\mathrm{QM}} = M_4^{2/2\mathrm{QM}} = \sqrt{2}$ ,  $M_4^{3/1\mathrm{QM}} = 2$ ,  $M_4^{4\mathrm{QM}} = 2\sqrt{2}$ . The algebraic limit is  $M_4^{\mathrm{alg}} = 4$  (sixteen terms in the sum, and a factor  $\frac{1}{4}$  in front of all).

Now we have to provide the bounds for  $1/1/2S$ ,  $2/2S$ , and  $3/1S$ . This last one can be calculated in the same way as above: using (3), we have  $M_4 = \frac{1}{2} M_3(a_4 + a_4') + \frac{1}{2} M_3'(a_4 - a_4')$ ; we set  $a_4 = a_4' = 1$ , and, since we allow the most general correlation between the first three particles, we have  $\max M_3 = M_3^{\mathrm{alg}} = 2$ . Therefore  $M_4^{3/1S} = 2$ .

One must be more careful in the calculation of  $1/1/2S$  and  $2/2S$ . This goes as follows: Using (6), we have  $M_4 = \frac{1}{2} M_{1,2}(M_{3,4} + M_{3,4}') + \frac{1}{2} M_{1,2}'(M_{3,4} - M_{3,4}')$ , where to avoid confusion we wrote  $M_{i,j}$  instead of  $M_2$ , with  $i$  and  $j$  the labels of the particles. Now,  $M_{3,4} + M_{3,4}' = a_3a_4' + a_3'a_4$ , and  $M_{3,4} - M_{3,4}' = a_3a_4 - a_3'a_4'$ . So, if we allow the most general correlation between particles 3 and 4, these two quantities are independent and can both reach their algebraic limit, which is 2. Consequently, for both  $1/1/2S$  and  $2/2S$  we obtain  $M_4'' = \max(M_{1,2} + M_{1,2}')$ , which is again 2 in both cases. So, finally,

$$
M _ {4} ^ {1 / 1 / 2 S} = M _ {4} ^ {2 / 2 S} = M _ {4} ^ {3 / 1 S} = 2 <   M _ {4} ^ {4 \mathrm {Q M}} = 2 \sqrt {2}. \tag {12}
$$

TABLE I. Maximal values of  $M_3$  and  $S_3$  under different assumptions for the nature of the correlations (see text). The last line is the product of the two values.  

<table><tr><td></td><td>lν</td><td>2/1QM</td><td>2/1S</td><td>3QM</td><td>3S
(algebraic)</td></tr><tr><td>M3</td><td>1</td><td>√2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>S3</td><td>1</td><td>1</td><td>1</td><td>√2</td><td>2</td></tr><tr><td>product</td><td>1</td><td>√2</td><td>2</td><td>2√2</td><td>4</td></tr></table>

For four particles, the MK polynomial  $M_4$  detects both four-particle entanglement (this was known) and four-particle nonseparability, and is therefore the natural generalization of Svetlichny's inequality.

Arbitrary number of particles. For a given number of particles  $n$ , we discuss only the maximal value allowed by QM, that is the case  $n\mathrm{QM}$ , against any possible partition in two subsets of  $k$  and  $n - k$  particles, respectively, with  $1 \leq k \leq n - 1$ , that is the case  $k / (n - k)S$ . Partitions in a bigger number of smaller subsets are clearly special cases of these bilateral partitions. We are going to prove the following.

Proposition: Define the generalized Svetlichny polynomial  $\mathbf{S}_{\mathfrak{n}}$  as

$$
S _ {n} = \left\{ \begin{array}{l l} M _ {n}, & n \text {e v e n} \\ \frac {1}{2} \left(M _ {n} + M _ {n} ^ {\prime}\right), & n \text {o d d}. \end{array} \right. \tag {13}
$$

Then all the correlations  $\mathrm{k / (n - k)S}$  give the same bound  $\mathbf{S}_{\mathfrak{n}}^{\mathbf{k}}$  , and the bound that can be reached by QM is higher by a factor  $\sqrt{2}$  ..

$$
S _ {n} ^ {n \mathrm {Q M}} = \sqrt {2} S _ {n} ^ {k}. \tag {14}
$$

The tools for the demonstration are the generalization to all the MK polynomials of the properties of  $M_2$  and  $M_3$  that we used above: namely, (I) the algebraic limit of  $M_k$  is  $M_k^{\mathrm{alg}} = 2^{k/2} = M_k^{k\mathrm{QM}}\sqrt{2}$  for  $k$  even, and  $M_k^{\mathrm{alg}} = 2^{(k-1)/2} = M_k^{k\mathrm{QM}}$  for  $k$  odd. (IIa) For  $k$  even,  $M_k$  and  $M_k'$  are different combinations of all the correlation coefficients;  $M_k + M_k'$  and  $M_k - M_k'$  contain each one-half of the correlation coefficients, and the algebraic limit for both is  $M_k^{\mathrm{alg}}$ . (IIb) For  $k$  odd,  $M_k$  and  $M_k'$  contain each one-half of the correlation coefficients. These properties are not usually given much stress, but can indeed be found in [4], or easily verified by direct inspection.

Let us first prove the proposition for  $n$  even. In this case, the QM bound is known to be  $S_{n}^{n\mathrm{QM}} = 2^{(n - 1) / 2}$ . As in the case of four particles, to calculate  $S_{n}^{k}$  we must distinguish two cases.

(i) For  $k$  and  $n - k$  even: in (6), both  $M_{k} + M_{k}^{\prime}$  and  $M_{k} - M_{k}^{\prime}$  can be maximized independently because of property (IIa) above; therefore, we replace them by  $M_{k}^{\mathrm{alg}}$ . We are left with  $S_{n}^{k} = \frac{1}{2} M_{k}^{\mathrm{alg}}\max (M_{n - k} + M_{n - k}^{\prime})$  and this maximum is again  $M_{n - k}^{\mathrm{alg}}$ . So, finally,  $S_{n}^{k} = \frac{1}{2} M_{k}^{\mathrm{alg}}M_{n - k}^{\mathrm{alg}} = 2^{(n - 2) / 2}$ .

(ii) For  $k$  and  $n - k$  odd: in (6),  $M_{n - k}$  and  $M_{n - k}^{\prime}$  can be optimized independently because of (IIb) above. We have then  $S_{n}^{k} = M_{n - k}^{\mathrm{alg}}\max M_{k} = M_{n - k}^{\mathrm{alg}}M_{k}^{\mathrm{alg}} = 2^{(n - 2) / 2}$ .

Thus, we have proven the proposition for  $n$  even.

To prove the proposition for  $n$  odd, we must calculate both  $S_{n}^{k}$  and  $S_{n}^{n\mathrm{QM}}$ . We begin with  $S_{n}^{k}$ . Inserting (6) in the definition of  $S_{n}$  for  $n$  odd, we find

$$
S _ {n} = \frac {1}{2} M _ {n - k} M _ {k} ^ {\prime} + \frac {1}{2} M _ {n - k} ^ {\prime} M _ {k}. \tag {15}
$$

Without loss of generality, we can suppose  $k$  odd and  $n - k$  even. Therefore, if we assume correlations  $k / (n -$

$k)S,M_{k}$  and  $M_k^\prime$  can both reach the algebraic limit due to property (IIb). So  $S_{n}^{k} = \frac{1}{2} M_{k}^{\mathrm{alg}}\max (M_{n - k} + M_{n - k}^{\prime})$  ; and due to property (IIa) this maximum is  $M_{n - k}^{\mathrm{alg}}$  . Thus  $S_{n}^{k} =$ $2^{(n - 3) / 2}$  . Let us calculate  $S_{n}^{n\mathrm{QM}}$  . From the polynomial  $S_{n}$  given by (15), we define the operator  $S_{n}$  in the usual way. Therefore for the particular case  $k = 1$  we have

$$
\operatorname {T r} \left(\rho S _ {n}\right) = \frac {1}{2} \left[ \operatorname {T r} \left(\rho \mathcal {M} _ {n - 1} \sigma_ {a _ {n} ^ {\prime}}\right) + \operatorname {T r} \left(\rho \mathcal {M} _ {n - 1} ^ {\prime} \sigma_ {a _ {n}}\right) \right], \tag {16}
$$

which is bounded by  $2^{(n - 2) / 2}$  because each of the terms in the sum is bounded by that quantity. This bound is reached by generalized GHZ states, for suitable settings [11]. Therefore  $S_{n}^{n\mathrm{QM}} = 2^{(n - 2) / 2}$  for  $n$  odd, and we have proven the proposition also for  $n$  odd.

In conclusion,  $n$ -particle entanglement and  $n$ -particle nonseparability are a priori different concepts. We have shown that it is possible to discriminate quantum entanglement, not only against local variable models, but also against all possible hybrid models  $k / (n - k)S$ , allowing arbitrarily strong correlations inside each subset but no correlation between different subsets. Experiments aimed at demonstrating  $n$ -particle entanglement should be analyzed using the generalized Svetlichny inequalities described in this Letter [12].

This work was partially supported by the European Union project EQUIP (IST-1999-11053) and by an ESF Short Scientific Visit Grant.

[1] See, for instance, G. Alber et al., Quantum Information: An Introduction to Basic Theoretical Concepts and Experiments, Springer Tracts in Modern Physics Vol. 173 (Springer-Verlag, Berlin, 2001).  
[2] N.D. Mermin, Phys. Rev. Lett. 65, 1838 (1990).  
[3] G. Svetlichny, Phys. Rev. D 35, 3066 (1987).  
[4] A.V. Belinskii and D.N. Klyshko, Phys. Usp. 36, 653 (1993); N. Gisin and H. Bechmann-Pasquinucci, Phys. Lett. A 246, 1 (1998); R.F. Werner and M.M. Wolf, Phys. Rev. A 61, 062102 (2000).  
[5] See, for instance, I. Percival, Phys. Lett. A 244, 495 (1998).  
[6] J.F. Clauser, M.A. Horne, A. Shimony, and R.A. Holt, Phys. Rev. Lett. 23, 880 (1969).  
[7] R.F. Werner and M.M. Wolf, Phys. Rev. A 64, 032112 (2001).  
[8] Note that this implies that the bound for  $l\nu$  is equal to the bound for  $1/1/\ldots/1$ QM (product states in QM). From now on, we shall not distinguish these two cases anymore.  
[9] B. S. Cirel'son, Lett. Math. Phys. 4, 83 (1980).  
[10] V. Scarani and N. Gisin, J. Phys. A 34, 6043 (2001).  
[11] To maximize  $\frac{1}{2}\langle \mathcal{M}_n + \mathcal{M}_n' \rangle_{\mathrm{GHZ}}$  for  $n$  odd, the  $\sigma_{a_j}$  are taken of the form  $\cos \alpha_j \sigma_x + \sin \alpha_j \sigma_y$ . One possible choice for the settings is  $\alpha_k = \alpha_k' + \frac{\pi}{2}$  for all  $k$ ,  $\alpha_1' = \dots = \alpha_{n-1}' = 0$ ,  $\alpha_n' = \frac{\pi}{4}$ . For such settings, each correlation coefficient becomes equal to  $1/\sqrt{2}$  in modulus, with the good sign. See [12].  
[12] P. Mitchel, S. Popescu, and D. Roberts (to be published).