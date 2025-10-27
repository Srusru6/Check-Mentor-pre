# Strong majorization entropic uncertainty relations

Lukasz Rudnicki, $^{1,2,*}$  Zbigniew Puchała, $^{3,4}$  and Karol Žyczkowski $^{4,2}$

$^{1}$ Freiburg Institute for Advanced Studies, Albert-Ludwigs University of Freiburg, Albertstrasse 19, 79104 Freiburg, Germany

$^{2}$ Center for Theoretical Physics, Polish Academy of Sciences, Aleja Lotników 32/46, PL-02-668 Warsaw, Poland

$^{3}$ Institute of Theoretical and Applied Informatics, Polish Academy of Sciences, Baltycka 5, 44-100 Gliwice, Poland

$^{4}$ Institute of Physics, Jagiellonian University, ul Reymonta 4, 30-059 Kraków, Poland

(Received 21 February 2014; published 15 May 2014)

We analyze entropic uncertainty relations in a finite-dimensional Hilbert space and derive several strong bounds for the sum of two entropies obtained in projective measurements with respect to any two orthogonal bases. We improve the recent bounds by Coles and Piani [P. Coles and M. Piani, Phys. Rev. A 89, 022112 (2014)], which are known to be stronger than the well-known result of Maassen and Uffink [H. Maassen and J. B. M. Uffink, Phys. Rev. Lett. 60, 1103 (1988)]. Furthermore, we find a bound based on majorization techniques, which also happens to be stronger than the recent results involving the largest singular values of submatrices of the unitary matrix connecting both bases. The first set of bounds gives better results for unitary matrices close to the Fourier matrix, while the second one provides a significant improvement in the opposite sectors. Some results derived admit generalization to arbitrary mixed states, so that corresponding bounds are increased by the von Neumann entropy of the measured state. The majorization approach is finally extended to the case of several measurements.

DOI: 10.1103/PhysRevA.89.052115

PACS number(s): 03.65.Ta, 03.65.Aa

# I. INTRODUCTION

Fundamental differences between the classical and quantum physics are highlighted by quantum uncertainty relations. The original version of the relations by Heisenberg, Kennard, and Robertson deals with the sum of uncertainties characterizing two measurements of observables which do not commute. The right-hand sides of these inequalities are proportional to the size of the Planck constant  $\hbar$  as in the classical case the bounds tend to zero.

In this paper we focus on probably the most popular representatives of uncertainty relations there are nowadays, given in terms of information entropies. One uses the standard Shannon entropy, with a clear operational meaning, or the generalized quantities of Rényi and Tsallis (for reviews on entropic uncertainty relations see [1,2]). One may observe a growing interest in these issues of the community working on the theory of quantum information processing [3-7] and on applications to, for example, quantum memory [8] or Einstein-Podolsky-Rosen steering inequalities [9]. Our aim is thus to classify recent improvements of various entropic uncertainty relations and provide several new results outperforming the previous ones.

Before we start let us introduce the notation. For a probability distribution  $p = \{p_i\}$  its Rényi entropy of order  $\alpha$  is given by the formula

$$
H _ {\alpha} (p) = \frac {1}{1 - \alpha} \ln \sum_ {i} p _ {i} ^ {\alpha}. \tag {1}
$$

In the limit  $\alpha \to 1$  the above definition recovers the Shannon entropy  $H(p) = -\sum_{i}p_{i}\ln p_{i}$ . Looking from a general perspective, Rényi entropies of any order are Schur-concave functions. In fact, every function  $F(p)$  which is Schur concave is in position to be a reasonable measure of uncertainty since it is maximized by a uniform probability distribution,

while its minimum is provided by concentrated probabilities  $p_c^\downarrow = (1,0,\ldots ,0)$ . The symbol  $\downarrow$  denotes the decreasing order, so that  $(p^{\downarrow})_i\geqslant (p^{\downarrow})_j$  whenever  $i\leqslant j$ . Among other Schur-concave functions let us only mention the so-called Havrda-Charvat-Tsallis entropy [10]:

$$
T _ {\alpha} (p) = \frac {1}{1 - \alpha} \left(\sum_ {i} p _ {i} ^ {\alpha} - 1\right). \tag {2}
$$

Describing the quantum state of the system we use a mixed state  $\rho$  acting on a  $d$ -dimensional Hilbert space  $\mathcal{H}$ . We consider two nondegenerate, noncommuting observables  $\hat{A}$  and  $\hat{B}$  with corresponding eigenstates denoted by  $|a_i\rangle$  and  $|b_j\rangle$ , respectively. The above eigenstates obviously provide two orthonormal bases in  $\mathcal{H}$ . We then define the probability distributions in the usual manner:

$$
p _ {i} = \langle a _ {i} | \rho | a _ {i} \rangle , \quad q _ {j} = \langle b _ {j} | \rho | b _ {j} \rangle . \tag {3}
$$

The history of the entropic uncertainty relations in finite-dimensional Hilbert spaces (continuous case had been developed before [11]) started with the paper by Deutsch [12] who proved that

$$
H (p) + H (q) \geqslant - 2 \ln C \equiv B _ {\mathrm {D}}, \tag {4}
$$

with  $C = (1 + \sqrt{c_1}) / 2$  and  $c_{1} = \max_{i,j}|\langle a_{i}|b_{j}\rangle |^{2}$  being the maximal overlap between the bases  $\{|a_i\rangle \}$  and  $\{|b_j\rangle \}$ . This seminal but rather weak lower bound for the sum of two Shannon entropies was further significantly improved and generalized by Maassen and Uffink in 1988 when they derived their famous uncertainty relation [13]

$$
H _ {\mu} (p) + H _ {v} (q) \geqslant - \ln c _ {1} \equiv B _ {\mathrm {M U}}, \tag {5}
$$

valid, however, only for conjugated parameters  $1 / \mu + 1 / \nu = 2$ . In the case of a single qubit more general bounds for the arbitrary pair  $(\mu, \nu)$  were recently studied in [14].

A natural range for the parameter  $c_{1}$  is of the form  $1 / d \leqslant c_{1} \leqslant 1$ . Comparing both bounds (4) and (5) in two opposite regimes of  $c_{1}$  one can observe the following.

(i) The Maassen-Uffink bound is substantially stronger  $(B_{\mathrm{MU}}\gg B_{\mathrm{D}})$  in the regime of small  $c_{1}\gtrsim 1 / d$  , when both bases are almost mutually unbiased.  
(ii) In the second case when  $c_{1} \lesssim 1$  both bounds provide almost the same quantitative description of uncertainty; however, bound (5) is always a bit stronger than (4),  $B_{\mathrm{MU}} \gtrsim B_{\mathrm{D}}$ .

In fact, when  $c_{1} = 1 / d$  and the bases  $\{|a_i\rangle\}$  and  $\{|b_j\rangle\}$  are related via discrete Fourier transformation, the bound in Eq. (5) equal to  $\ln d$  is optimal. At this point let us mention that the two bases in question are in general related by the unitary transformation  $U \in \mathcal{U}(d)$ , with matrix elements equal to  $U_{ij} = \langle a_i|b_j\rangle$ , so that  $c_{1} = \max_{i,j}|U_{ij}|^{2}$ .

In the years 1988-2013 only one example of a general state-independent improvement of the lower bound (5), valid and significant in the regime of large  $c_{1}$ , has been communicated [15,16]. Several results were, however, devoted to particular studies of, e.g., qubits [17-19], described by the case  $d = 2$ .

This work is organized as follows. After we review the recent progress in the context of entropic uncertainty relations, we derive in Sec. II the three new, hybrid bounds for the sum of two Shannon entropies. To this end we use both techniques of relative-entropy monotonicity [6] and the majorization entropic uncertainty relations [4,5,20]. In Sec. III we introduce yet another majorization-based approach, which happens to outperform the previous one [4,5] (see Appendix B). After we compare in Sec. IV all bounds for the sum of two Shannon entropies which are currently available, we extend in Sec. V the majorization uncertainty relations derived in Sec. III to the case of several measurements.

# A. Recent results

Surprisingly, the Maassen-Uffink bound has been recently improved in the whole range of the parameter  $c_{1}$ . First of all, Coles and Piani [6] have provided a state-independent bound (note that we use the natural logarithm instead of  $\log_2$ )

$$
H (p) + H (q) \geqslant - \ln c _ {1} + (1 - C) \ln \frac {c _ {1}}{c _ {2}} \equiv B _ {\mathrm {C P 1}}, \tag {6}
$$

with  $C = (1 + \sqrt{c_1}) / 2$ , the same as before, and  $c_{2}$  being the second largest value among  $|U_{ij}|^2$ . Since  $c_{2} \leqslant c_{1}$  the second term in Eq. (6) is a non-negative correction to Eq. (5). The above example shows that the improvements of Eq. (5) shall rely on more overlaps between the bases. An intermediate step in the derivation of Eq. (6) leads to a stronger but implicit bound [6],

$$
H (p) + H (q) \geqslant \max  _ {0 \leqslant \kappa \leqslant 1} \lambda_ {\min } (- 2 \Delta) \equiv B _ {\mathrm {C P} 2} \geqslant B _ {\mathrm {C P} 1}, \tag {7}
$$

involving the  $d\times d$  matrix  $\Delta$  with matrix elements  $\Delta_{mn}$  being

$$
\kappa \delta_ {m n} \ln \max  _ {k} | U _ {m k} | + (1 - \kappa) \sum_ {j} U _ {m j} U _ {n j} ^ {*} \ln \max  _ {k} | U _ {k j} |. \tag {8}
$$

$\lambda_{\mathrm{min}}(\cdot)$  denotes here the minimum eigenvalue. The above results have been derived only in the case of the Shannon entropy, since they utilize the relative entropy:

$$
D (\rho | | \sigma) = \operatorname {T r} \rho \ln \rho - \operatorname {T r} \sigma \ln \sigma . \tag {9}
$$

While both bounds (6) and (7) are never worse than  $B_{\mathrm{MU}}$ , they seem to provide more accurate improvements for  $c_1 \gtrsim$

$1 / d$  [note the factor  $1 - C$  in Eq. (6)] than for the case  $c_{1} \lesssim 1$ . In this second regime another approach based on majorization techniques comes into play. The idea that majorization can be used to quantify uncertainty [20] has been developed in [4,5] giving the bound

$$
F (p \otimes q) \geqslant F (Q), \tag {10}
$$

valid for any Schur-concave function  $F$ . By  $Q$  we denote any vector of probabilities that majorizes  $r \prec Q$ , the distribution  $r = p \otimes q$  (we call the above result the tensor-product majorization relation). Unless otherwise stated we assume that the vector  $Q$  is sorted in a decreasing order. The majorization relation  $r \prec Q$  means that for all  $n < d^2$  we necessarily have  $\sum_{k=1}^{n} r_k^\downarrow \leqslant \sum_{k=1}^{n} Q_k$  and due to the probability conservation  $\sum_{k=1}^{d^2} r_k = \sum_{k=1}^{d^2} Q_k = 1$ . As long as  $c_1 < 1$  there exist nontrivial vectors  $Q \neq Q^{(0)} = (1,0,\dots,0)$ . It also happens that the majorizing probability vector  $Q$  possesses at most  $d$  nonzero elements. In [4] we derived a full hierarchy of  $d - 1$  majorizing vectors  $Q^{(k)}, k = 1,\dots,d - 1$ , such that

$$
Q ^ {(0)} \succ Q ^ {(1)} \succ Q ^ {(2)} \succ \dots \succ Q ^ {(d - 1)} \succ r, \tag {11}
$$

which are expressed by singular values of certain submatrices selected from the  $d \times d$  unitary matrix  $U$ .

In particular, an additivity property of the Rényi entropies  $H_{\alpha}(p \otimes q) = H_{\alpha}(p) + H_{\alpha}(q)$  immediately provide the bound utilizing the majorizing vector presented in [4]:

$$
H _ {\alpha} (p) + H _ {\alpha} (q) \geqslant H _ {\alpha} \left(Q ^ {(d - 1)}\right) \equiv B _ {\mathrm {M a j} 1}. \tag {12}
$$

While in the regime  $c_{1} \gtrsim 1 / d$  the bound  $B_{\mathrm{Maj1}}$  might be weaker than that in Eq. (5), it happens that for  $d = 5$  it is stronger than the result of Maassen and Uffink with a probability larger than  $98\%$  [4].

# II. STRONG BOUNDS FOR THE SHANNON ENTROPY

In this section we derive three state-independent bounds  $B_{\mathrm{RPZ}k}(\rho)$ ,  $k = 1,2,3$ , for the sum of two Shannon entropies utilizing both the relative entropy approach and the majorization technique. We call the bounds state independent; however, they all contain a non-negative state-dependent term equal to the von-Neumann entropy  $S(\rho) \geqslant 0$ . To get state-independent bounds in a strict meaning [denoted consistently by  $B_{\mathrm{RPZ}k}(\phi)$ ] one must simply choose the state  $\rho$  to be pure.

We start recalling first steps from the derivation of Eq. (7) used by Coles and Piani [6] which concern an arbitrary initial state  $\rho$ ,

$$
\begin{array}{l} H (q) + \operatorname {T r} \rho \ln \rho = D \left(\rho \left\| \sum_ {j} q _ {j} | b _ {j} \rangle \langle b _ {j} |\right)\right) \\ \geqslant D \left(\sum_ {i} p _ {i} | a _ {i} \rangle \langle a _ {i} | \left\| \sum_ {j, k} q _ {j} \left| U _ {j k} \right| ^ {2} \mid a _ {k} \right\rangle \langle a _ {k} |\right). \tag {13} \\ \end{array}
$$

The inequality is a consequence of the monotonicity of the relative entropy with respect to the quantum channel:

$$
\rho \mapsto \sum_ {i} | a _ {i} \rangle \langle a _ {i} | \rho | a _ {i} \rangle \langle a _ {i} |. \tag {14}
$$

We now rewrite the above inequality in the form

$$
H (p) + H (q) \geqslant - \sum_ {i} p _ {i} \ln \left(\sum_ {j} q _ {j} \left| U _ {i j} \right| ^ {2}\right) + S (\rho). \tag {15}
$$

The second term appearing on the right-hand side is equal to the von Neumann entropy  $S(\rho) = -\mathrm{Tr}\rho \ln \rho$  of the state  $\rho$ . Performing the same step as in Eq. (13), but starting from  $H(p)$  one derives the following counterpart of Eq. (15) [6]:

$$
H (p) + H (q) \geqslant - \sum_ {j} q _ {j} \ln \left(\sum_ {i} p _ {i} \left| U _ {i j} \right| ^ {2}\right) + S (\rho). \tag {16}
$$

# A. First application of the tensor-product majorization relation

With the help of the convexity property of  $-\ln(\cdot)$  both intermediate bounds (15) and (16) can be estimated in the same way, giving

$$
H (p) + H (q) \geqslant - \ln \left(\sum_ {i, j} p _ {i} q _ {j} \left| U _ {i j} \right| ^ {2}\right) + S (\rho). \tag {17}
$$

Let us now denote by  $c = (c_{1}, c_{2}, \ldots, c_{d^{2}})$  the  $d^{2}$ -dimensional vector of elements  $|U_{ij}|^{2}$  sorted in decreasing order. Recalling the notion of the vector  $Q \succ r$  majorizing the  $d^{2}$ -dimensional vector  $r = p \otimes q$  we immediately get

$$
H (p) + H (q) \geqslant - \ln (Q \cdot c) + S (\rho) \equiv B _ {\mathrm {R P Z I}}, \tag {18}
$$

where  $Q$  is by definition sorted in decreasing order while  $Q \cdot c$  denotes the scalar product of the vectors  $Q$  and  $c$ . In order to prove the above result we simply note that the argument inside the logarithm in Eq. (17) is less than  $r \cdot c$  and  $-\ln(r \cdot c)$  is a Schur-concave function with respect to  $r$ .

# 1. The simplest estimations

Obviously, every  $r = p \otimes q$  is majorized by  $Q^{(0)}$ . For that choice the bound (18) boils down to  $B_{\mathrm{MU}}$  with a nonnegative correction provided by the von Neumann entropy term  $-\mathrm{Tr}\rho \ln \rho$ .

As a first nontrivial case we can take [4]  $Q^{(1)} = (C^2, 1 - C^2, 0, \ldots, 0)$ . This choice leads to a simple and strong, new state-independent bound:

$$
H (p) + H (q) \geqslant - \ln \left[ c _ {1} C ^ {2} + c _ {2} \left(1 - C ^ {2}\right) \right] + S (\rho) \equiv B _ {\mathrm {R P Z 2}}. \tag {19}
$$

# B. Implicit bounds from the tensor-product majorization relation

As a first step we take the arithmetic mean of Eqs. (15) and (16) and reexpress the resulting inequality in the form

$$
\begin{array}{l} H (p) + H (q) \\ \geqslant - \frac {1}{2} \sum_ {k, l} p _ {k} q _ {l} \ln \left(\sum_ {i, j} p _ {i} q _ {j} \left| U _ {k j} \right| ^ {2} \left| U _ {i l} \right| ^ {2}\right) + S (\rho). \tag {20} \\ \end{array}
$$

For each pair of indices  $(k,l)$  we next introduce a  $d^2$ -dimensional vector  $h_{kl}$  given by the elements  $|U_{kj}|^2 |U_{il}|^2$

sorted in decreasing order with respect to the pair  $(i,j)$ . We immediately get

$$
- \ln \left(\sum_ {i, j} p _ {i} q _ {j} \left| U _ {k j} \right| ^ {2} \left| U _ {i l} \right| ^ {2}\right) \geqslant - \ln (Q \cdot h _ {k l}). \tag {21}
$$

In the second step, we introduce the vector  $f$  of length  $d^2$ , given by the elements  $f_{kl} = -\ln (Q \cdot h_{kl})$  sorted in decreasing order with respect to the pair  $(k,l)$ . Finally (using the same arguments as before) we obtain the implicit (two sortings required) relation

$$
H (p) + H (q) \geqslant - \frac {1}{2} Q f + S (\rho) \equiv B _ {\mathrm {R P Z 3}}. \tag {22}
$$

The above considerations enable us to formulate the following hybrid entropic uncertainty relations, based both on majorization techniques and on monotonicity of the relative entropy.

Theorem 1. The entropic uncertainty relations presented in Eqs. (18), (19), and (22), valid for an arbitrary mixed state  $\rho$ , have the form

$$
H (p) + H (q) \geqslant B _ {\mathrm {R P Z} k} (\rho) \geqslant B _ {\mathrm {R P Z} k} (\phi) + S (\rho), \tag {23}
$$

for  $k = 1,2,3$

# III. DIRECT-SUM MAJORIZATION RELATIONS

Let  $U$  be a unitary matrix of size  $d$ . By  $\mathcal{SU}\mathcal{B}(U,k)$  we denote the set of all its submatrices of class  $k$  defined by

$$
\mathcal {S U B} (U, k) = \{M: \# \operatorname {c o l s} (M) + \# \operatorname {r o w s} (M) = k + 1
$$

$$
\text {a n d} M \text {i s a s u b m a t r i x o f} U \}. \tag {24}
$$

The symbols  $\# \mathrm{cols}(\cdot)$  and  $\# \mathrm{rows}(\cdot)$  denote the number of columns and the number of rows, respectively. Following [4] we define the coefficients

$$
s _ {k} = \max  [ \| M \|: M \in \mathcal {S U B} (U, k) ], \tag {25}
$$

with  $\| M\|$  being the operator norm equal to the maximal singular value of  $M$ . With this notation we can state the following result.

Theorem 2 (Direct-sum majorization relation). For the Rényi entropies of order  $\alpha \leqslant 1$  (and thus also for the Shannon entropy) we have

$$
H _ {\alpha} (p) + H _ {\alpha} (q) \geqslant H _ {\alpha} (W) \equiv B _ {\text {M a j 2}}, \tag {26}
$$

where  $W = (s_{1}, s_{2} - s_{1}, \ldots, s_{d} - s_{d-1})$ .

While the tensor-product majorization [4] is based on the relation  $p \otimes q \prec Q$ , its counterpart, giving the meaning to the vector  $W$  is of the direct-sum form

$$
p \oplus q \prec \{1 \} \oplus W, \tag {27}
$$

(see Appendix A for details and the proof of Theorem 2).

In the case  $\alpha > 1$  the relation (26) does not hold; we can, however, establish a bit weaker bound:

$$
H _ {\alpha} (p) + H _ {\alpha} (q) \geqslant \frac {2}{1 - \alpha} \ln \left(\frac {1 + \sum_ {i} W _ {i} ^ {\alpha}}{2}\right). \tag {28}
$$

Surprisingly, a relation of the same kind as Eq. (26) holds for the Tsallis entropy proven in Appendix A.

Theorem 3. For the Tsallis entropy (2) of any order  $\alpha \geqslant 0$ , we have

$$
T _ {\alpha} (p) + T _ {\alpha} (q) \geqslant T _ {\alpha} (W). \tag {29}
$$

To give a particular example of the direct-sum majorization entropic uncertainty relation let us recall that in [4] the singular value  $s_2$  is upper-bounded in the following way:

$$
s _ {2} \leqslant \sqrt {c _ {1} + c _ {2}}. \tag {30}
$$

We can then use this inequality to provide a particular vector,

$$
W ^ {(2)} = \left(\sqrt {c _ {1}}, \sqrt {c _ {1} + c _ {2}} - \sqrt {c _ {1}}, 1 - \sqrt {c _ {1} + c _ {2}}, 0, \dots , 0\right), \tag {31}
$$

that majorizes the vector  $W$ . This vector contains  $2(d - 2)$  zero elements. The above example shows that the same sort of hierarchy as given by Eq. (11) can be constructed in the case of the direct-sum majorization. To this end we simply need to set  $W^{(1)} = (\sqrt{c_1}, 1 - \sqrt{c_1}, 0, \dots, 0)$  and  $W^{(d - 1)} = W$ .

In Appendix B we prove yet another majorization relation,  $W \prec Q^{(d - 1)}$ , which happens to be valid for any unitary matrix  $U$ . This observation implies that the bound  $B_{\mathrm{Maj2}}$  is always stronger,  $B_{\mathrm{Maj2}} \geqslant B_{\mathrm{Maj1}}$ , than the bounds previously derived in [4,5].

# IV. COMPARISON OF BOUNDS

In this section we illustrate our results, showing how the obtained bounds work for selected families of unitary matrices belonging to  $\mathcal{U}(3)$  and  $\mathcal{U}(4)$ . We consider first a family of  $3 \times 3$  matrices defined as

$$
U (\theta) = M (\theta) O _ {3} M (\theta) ^ {\dagger}, \tag {32}
$$

where

$$
M (\theta) = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & \cos \theta & \sin \theta \\ 0 & - \sin \theta & \cos \theta \end{array} \right) \text {a n d} \tag {33}
$$

$$
O _ {3} = \frac {1}{\sqrt {6}} \left( \begin{array}{c c c} \sqrt {2} & \sqrt {2} & \sqrt {2} \\ \sqrt {3} & 0 & - \sqrt {3} \\ 1 & - 2 & 1 \end{array} \right).
$$

The matrix  $O_{3}$ , used in [6] to illustrate the quality of the bounds  $B_{\mathrm{CP1}}$  and  $B_{\mathrm{CP2}}$ , corresponds to the choice  $\theta = 0$ .

In Fig. 1 the bounds discussed in this paper (apart from  $B_{\mathrm{CP2}}$  which requires additional numerical optimization) are

![](images/04f676bc46ff485b988fe992398ef98c745d8db20a6ebefb4cf6708031c4a567.jpg)  
FIG. 1. (Color online) Several bounds for the sum of two entropies for a family of unitary matrices defined in Eq. (32).

TABLE I. Comparison between numerical values of all bounds in the case of  $U = O_{3}$  in the  $\log_2$  units used in [6].  

<table><tr><td>The bound</td><td>Approximate value</td></tr><tr><td>BD</td><td>0.425</td></tr><tr><td>BMU</td><td>0.585</td></tr><tr><td>BCP1</td><td>0.623</td></tr><tr><td>BCP2</td><td>0.641</td></tr><tr><td>BRPZ1</td><td>0.649</td></tr><tr><td>BRPZ2</td><td>0.649</td></tr><tr><td>BRPZ3</td><td>0.676</td></tr><tr><td>BMaj1</td><td>0.669</td></tr><tr><td>BMaj2</td><td>0.688</td></tr></table>

presented for the sum of two entropies for a family of unitary matrices defined in Eq. (32). The bound  $B_{\mathrm{Maj2}}$  provides the best estimation for the sum of two entropies while the majorization bound  $B_{\mathrm{Maj1}}$  gives (as expected) always a worse approximation.  $B_{\mathrm{Maj2}}$  outperforms the Maassen-Uffink bound as well as the bound  $B_{\mathrm{CP2}}$ . The quantities  $B_{\mathrm{RPZ1}}$  and  $B_{\mathrm{RPZ2}}$  do not give a significant improvement. The bound  $B_{\mathrm{RPZ3}}$  performs better than  $B_{\mathrm{MU}}$ , but is typically worse than  $B_{\mathrm{Maj1}}$ . Note that some authors define the entropies with log base 2 while in the present work we in general use the natural logarithm instead. In Table I we, however, switch to  $\log_2$  while presenting numerical comparison of all bounds for the special case  $U = O_3$ .

In Fig. 2 we plot the bounds for  $3 \times 3$  matrices given by

$$
U _ {\beta} = \left(F _ {3}\right) ^ {\beta} \exp [ i (1 - \beta) H ]. \tag {34}
$$

Here  $F_{d}$  denotes the Fourier matrix of order  $d$ , so that  $(F_{d})_{jk} = \exp(2\piijk / d) / \sqrt{d}$ , while our model Hamiltonian  $H$  reads

$$
H = \left( \begin{array}{c c c} 0 & 1 & 2 \\ 1 & 0 & 2 \\ 2 & 2 & 0 \end{array} \right). \tag {35}
$$

This family thus interpolates between the Fourier matrix  $F_{3}$  and  $U_{0} = \exp (iH)$ . In this case the direct-sum majorization bound is substantially better than the Maassen-Uffink bound, while considering matrices laying far away from the Fourier matrix.

In Fig. 3 we study the family of matrices which interpolates between the identity and the Fourier matrix  $F_{4}$ , namely,

![](images/5784a1ea7618d33e22ea1fbdffbf44389b710e89ba9c2cba3052e247684670a5.jpg)  
FIG. 2. (Color online) Bounds for a family of unitary matrices (34).

![](images/0dbf5d232d3ce0a6296572cf8e9bbb5d714780406856a33c06d7b02969698089.jpg)  
FIG. 3. (Color online) Bounds for a family of unitary matrices  $(F_4)^\beta$  interpolating between the identity and the Fourier matrix for  $\beta \in [0,1]$ .

$U(\beta) = (F_4)^\beta$ . Similarly to the prior case the direct-sum majorization relation provides a better bound for matrices which are distant from the Fourier matrix, while in its neighborhood the  $B_{\mathrm{RPZ3}}$  bound gives the best estimate.

# V. SEVERAL MEASUREMENTS

Majorization entropic uncertainty relations derived in Sec. III can be easily generalized to the case of an arbitrary number of  $L$  measurements. The problem is now given by a collection of arbitrary  $L$  unitary matrices,  $U^{(1)},\ldots ,U^{(L)}$ , one of which is usually set to the identity.

Let  $\{|u_i^{(j)}\rangle \}$  be the  $i$ th column of the matrix  $U^{(j)}$ . We consider an entropic uncertainty relation of the form

$$
\sum_ {i = 1} ^ {L} H \left(p ^ {(i)}\right) \geqslant B, \tag {36}
$$

where  $p_i^{(j)} = |\langle u_i^{(j)}|\psi \rangle |^2$ . In order to find a candidate for the bound  $B$  we introduce a majorizing vector in a manner similar to that of the approach presented in Sec. III.

First of all, we define new coefficients  $S_{k}$  as maximal squares of norms calculated for the rectangular matrices of size  $d\times (k + 1)$  formed by  $k + 1$  columns taken from the concatenation of all  $L$  matrices  $\{U^{(j)}\}_{j = 1}^{L}$ , i.e.,

$$
\left. \mathcal {S} _ {k} = \max  \left\{\sigma_ {1} ^ {2} \left(\left| u _ {i _ {1}} ^ {(j _ {1})} \right\rangle , \left| u _ {i _ {2}} ^ {(j _ {2})} \right\rangle , \dots , \left| u _ {i _ {k + 1}} ^ {(j _ {k + 1})} \right\rangle\right) \right\}, \right. \tag {37}
$$

where the maximum ranges over all subsets  $\{(i_1,j_1),(i_2,j_2),\ldots ,(i_{k + 1},j_{k + 1})\}$  of cardinality  $k + 1$  of set  $\{1,2,\dots ,d\} \times \{1,2,\dots ,L\}$ . It is easy to realize that  $\mathcal{S}_0 = 1$ , as all vectors  $u_i^{(j)}$  are normalized.

In the case  $L = 2$  one gets

$$
\mathcal {S} _ {k} = 1 + s _ {k}, \tag {38}
$$

with  $s_k$  defined in Eq. (25).

Using the methods presented in [4] one can show that, for any vector  $|\psi \rangle \in \mathbb{C}^d$ ,

$$
\left\{p _ {i} ^ {(j)} \right\} _ {i, j = 1} ^ {d, L} \prec \{1, \mathcal {S} _ {1} - 1, \mathcal {S} _ {2} - \mathcal {S} _ {1}, \dots \}. \tag {39}
$$

![](images/597de1ea1fad4bae568852f36fca90b2c37195abfd1c7c60bf0f0ebbb95b93f7.jpg)  
FIG. 4. (Color online) Bounds for the sum of three entropies corresponding to measurements in three bases in  $\mathbb{C}^2$  defined by Eq. (41). Curve  $B_{\mathrm{OPT}}$  represents the optimal bound obtained numerically.

The above observation leads to the following entropic uncertainty relation:

$$
\sum_ {i = 1} ^ {L} H \left(p ^ {(i)}\right) \geqslant - \sum_ {i = 1} ^ {d L} \left(\mathcal {S} _ {i} - \mathcal {S} _ {i - 1}\right) \ln \left(\mathcal {S} _ {i} - \mathcal {S} _ {i - 1}\right). \tag {40}
$$

In the case of the Rényi entropies with  $\alpha < 1$  and also the Tsallis entropies one can easily formulate lower bounds similar to Eq. (40).

To illustrate, the case of more than two measurements we employ families which interpolate between identical and mutually unbiased bases. In Fig. 4 we consider three bases, represented by the columns of three unitary matrices of order 2:

$$
U ^ {(1)} = \mathbb {I} _ {2}, U ^ {(2)} = \left( \begin{array}{c c} \cos \theta & \sin \theta \\ \sin \theta & - \cos \theta \end{array} \right), \tag {41}
$$

$$
U ^ {(3)} = \left( \begin{array}{c c} \cos \theta & \sin \theta \\ i \sin \theta & - i \cos \theta \end{array} \right).
$$

In the case of  $\theta = 0$  we obtain bases which give the same measurement probabilities, while in the case of  $\theta = \pi /4$  the three bases are mutually unbiased. In this case the sum (36) of three entropies is larger than  $2\log 2$  -the MUB bound of Sanchez [17], extended for mixed states in [21]. In the neighborhood of  $\theta = \pi /4$  the Maassen-Uffink bound calculated pairwise, labeled by  $B_{\mathrm{MU - pairs}}$  , is obviously larger than the direct-sum majorization bound calculated pairwise,  $B_{\mathrm{Maj2 - pairs}}$  . However, the direct-sum majorization bound (40) performs better than the Maassen-Uffink bound calculated pairwise.

A similar behavior is shown in Fig. 5 obtained for  $L = 4$  bases of size  $d = 3$  defined by

$$
U ^ {(1)} = \mathbb {I} _ {3}, U ^ {(2)} = \left(F _ {3}\right) ^ {4 \theta / \pi}, \tag {42}
$$

$$
U ^ {(3)} = E \left(F _ {3}\right) ^ {4 \theta / \pi}, U ^ {(4)} = E ^ {2} \left(F _ {3}\right) ^ {4 \theta / \pi}, \tag {43}
$$

where  $E = \mathrm{diag}[1, \exp(i2\pi/3), \exp(i2\pi/3)]$ . Note that for  $\theta = 0$  all matrices become diagonal and correspond to the same basis, while for  $\theta = \pi/4$  the bases are mutually unbiased (MUB). In this case the direct-sum majorization bound is close to the optimal bound obtained numerically.

![](images/09a9b166629f6381da879a65c560ebd5cabde62a534ff81b8b9bd4f40b579847.jpg)  
FIG. 5. (Color online) Bounds for the sum of four entropies related to four unitary matrices [Eqs. (42) and (43)]. Sign  $(\times)$  represents the MUB result of Sanchez [17].

Note that the direct-sum majorization bound (40) valid for the collection of  $L$  unitary matrices  $U^{(i)}$  by construction gives results which are generically better and always not worse than using the same bound pairwise for all  $L(L - 1) / 2$  pairs of unitary matrices  $V_{ij} = U^{(i)\dagger}U^{(j)}$ . This statement follows from the fact that in the latter case one performs optimization over a smaller set.

# VI. CONCLUDING REMARKS

In this work we derived several families of universal bounds for the sum of Shannon entropies corresponding to orthogonal measurements of a given quantum state  $\rho$  of size  $d$  in arbitrary  $L$  bases. In the simplest case of  $L = 2$  the problem is set by specifying a single unitary matrix  $U$  of order  $d$ .

If the absolute value of the largest entry of matrix  $U$  is significantly smaller than 1, which is the case, e.g., when  $U$  is close to the Fourier matrix, the most accurate results are obtained by the hybrid bounds  $B_{\mathrm{RPZ1}}$  and  $B_{\mathrm{RPZ3}}$ . In the opposite case, when  $U$  contains some entries of modulus close to unity, the direct-sum majorization bound (26) is generically better than all other bounds. Since when  $c_{1}$  is close to  $1 / d$  the bounds  $B_{\mathrm{RPZ1}}$  and  $B_{\mathrm{RPZ3}}$  seem to be not worse than other known bounds, and bound (26) is always not worse than the tensor-product majorization bound established in [4,5], it is then fair to say that the collection of results derived in this work provides the best set of bounds currently available.

As reported in [4] for  $d = 3,4,5$ , bound (12) applied to a random unitary matrix of order  $d$  is generically stronger than the relation (5) of Maassen-Uffink. However, it can be shown that for large  $d$  the situation changes and the following relation [22] holds asymptotically,  $\langle B_{\mathrm{Maj}1}\rangle_U < \langle B_{\mathrm{MU}}\rangle_U < \langle B_{\mathrm{Maj}2}\rangle_U$ , so bound (26) becomes the strongest one. Here  $\langle B\rangle_U$  denotes the bound  $B$  averaged over the set of unitary matrices of order  $d$  distributed with respect to the Haar measure.

Observe that all three inequalities (18), (19), and (22) work for an arbitrary mixed state  $\rho$ . Furthermore, the analyzed bound for the sum of two entropies characterizing both measurements is enlarged by the von Neumann entropy of the measured state,  $S(\rho) = -\mathrm{Tr}\rho \ln \rho$ , which is equal to zero for any pure state. Although our hybrid bounds are proved in this work for the multipartite case, following Coles and Piani [6] one can also formulate them in a more general, bipartite setup.

An analogous result concerning the generalization of the Maassen-Uffink bound for the mixed states appeared in [8,21] and very recently in [23]. The first term on the right-hand side of Eq. (23), due to the noncommutativity of both measurement bases, is called the quantum uncertainty [23], while the second term, related to the degree of mixing and referred to as the classical uncertainty, vanishes for pure states.

The bounds obtained with the help of the direct-sum majorization can be easily generalized to the case of an arbitrary number of measurements. Analyzing exemplary families of three unitary matrices of size  $d = 2$  and four matrices of size  $d = 3$  which interpolate between  $L$  identity matrices and the set of mutually unbiased bases, we show that the method proposed is applicable in practice for any collection of orthogonal measurements and generically provides stronger results than those known previously.

Strong majorization entropic uncertainty relations, established in this work, can be used complementarily for various problems in the theory of quantum information. Specific applications include separability conditions and characterization of multipartite entanglement [24], estimation of mutual information [6] in the context of Hall's information exclusion principle [25,26], and improved witnessing of quantum entanglement and measurements in the presence of quantum memory [8].

# ACKNOWLEDGMENTS

It is a pleasure to thank Gustavo Bosyk, Patrick Coles, Yuval Gefen, Kamil Korzekwa, Marco Piani, and Alexey Rastegin for stimulating discussions and useful correspondence. Financial support by NCN Grants No. DEC-2011/02/A/ST2/00305 (K.Z.) and No. DEC-2012/04/S/ST6/00400 (Z.P.) and by Grant No. IP2011 046871 of the Polish Ministry of Science and Higher Education (L.R.) is gratefully acknowledged.

# APPENDIX A: DERIVATION OF DIRECT-SUM MAJORIZATION RELATIONS

We first prove the following lemma.

Lemma 1. For probability vectors  $p$  and  $q$  defined in Eq. (3) the following majorization relation holds:

$$
(p _ {1}, p _ {2}, \dots , p _ {d}, q _ {1}, q _ {2}, \dots , q _ {d}) \prec (1, s _ {1}, s _ {2} - s _ {1}, \dots s _ {d} - s _ {d - 1}).
$$

(A1)

Note, that the right-hand side of the above relation concerns the vector  $W$  present in Eq. (27).

Proof. Let us denote  $z = p \oplus q$ . We necessarily have  $z_{i} \leqslant 1$  for all  $i$ , so that the first element of the vector majorizing  $z$  must be equal to 1. If we now consider the sum of two different elements  $z_{i} + z_{j}$  it can be the sum of two probabilities  $p$ , the sum of two probabilities  $q$  (in both cases the sum is bounded by 1), or the mixed sum  $p_{i} + q_{j}$  bounded by  $1 + s_{1}$ . In a similar fashion we obtain more general inequalities:

$$
z _ {i _ {1}} + z _ {i _ {2}} + \dots + z _ {i _ {k}} \leqslant 1 + s _ {k - 1}, \tag {A2}
$$

proven in [4], which gives the relation (A1).

Now we can prove Theorem 2. Let us first consider the case  $\alpha < 1$ . We begin with a simple observation, that for  $x \geqslant 0$  the

function  $\ln (1 + x)$  is subadditive, i.e.,

$$
\ln (1 + x) + \ln (1 + y) \geqslant \ln (1 + x + y). \tag {A3}
$$

Since  $\alpha < 1$  the sum  $\sum_{i} p_{i}^{\alpha}$  and its  $q$  counterpart are greater than 1. By putting  $x = \sum_{i} p_{i}^{\alpha} - 1$  and  $y = \sum_{j} q_{j}^{\alpha} - 1$ , we find that

$$
H _ {\alpha} (p) + H _ {\alpha} (q) \geqslant \frac {1}{1 - \alpha} \ln \left(\sum_ {i} p _ {i} ^ {\alpha} + \sum_ {i} q _ {i} ^ {\alpha} - 1\right). \tag {A4}
$$

Using the fact that the sum  $\sum_{i}x_{i}^{\alpha}$  is Schur concave for  $\alpha < 1$  and utilizing the direct-sum majorization relation  $z\prec \{1\} \oplus W$  we immediately get inequality (26). The case of  $\alpha = 1$  is even simpler, since we do not need to resort to subadditivity. Schur concavity of the Shannon entropy together with the fact that  $-1\ln 1 = 0$  gives the desired result.

In order to prove Eq. (28) we rewrite the sum of two Rényi entropies as

$$
H _ {\alpha} (p) + H _ {\alpha} (q) = H _ {\alpha} (r), \tag {A5}
$$

where  $r = p \otimes q$ . We then use the fact that the geometric mean is smaller than or equal to the arithmetic mean,

$$
\sum_ {i} p _ {i} ^ {\alpha} \sum_ {j} q _ {j} ^ {\alpha} \leqslant \frac {1}{4} \left(\sum_ {i} p _ {i} ^ {\alpha} + \sum_ {j} q _ {j} ^ {\alpha}\right) ^ {2}, \tag {A6}
$$

and apply the direct-sum majorization relation.

The proof of Theorem 3, concerning the Tsallis entropy, relies on the fact that for  $\alpha >0,\alpha \neq 1$ , and  $x_{i}\geqslant 0$  the function  $(1 - \alpha)^{-1}\sum_{i}x_{i}^{\alpha}$  is Schur concave. We have

$$
T _ {\alpha} (p) + T _ {\alpha} (q) = \frac {1}{1 - \alpha} \left(\sum_ {i} z _ {i} ^ {\alpha} - 2\right) \geqslant T _ {\alpha} (W), \tag {A7}
$$

where the last inequality follows from  $z\prec \{1\} \oplus W$

# APPENDIX B: PROOF OF  $B_{\mathrm{Maj2}} \geqslant B_{\mathrm{Maj1}}$

The vector  $Q^{(d - 1)}$  present in Eq. (12) has the general form [4]

$$
Q ^ {(d - 1)} = \left(R _ {1}, R _ {2} - R _ {1}, \dots , R _ {d} - R _ {d - 1}\right), \tag {B1}
$$

with

$$
R _ {i} = \left(\frac {1 + s _ {i}}{2}\right) ^ {2} \tag {B2}
$$

and  $s_i$  defined in Eq. (25). The above vector  $Q^{(d-1)}$  and the vector  $W$  are not necessarily sorted in a decreasing order, which is why the proof of the majorization relation  $W = (s_1, s_2 - s_2, s_3 - s_2, \ldots, s_d - s_{d-1}) \prec Q^{(d-1)}$  is not straightforward.

Let us first show that for any unitary matrix  $U$ , we have  $W_{1} \geqslant W_{k}$  for  $k = 2, \ldots, d$ , i.e.,

$$
s _ {k} - s _ {k - 1} \leqslant s _ {1}. \tag {B3}
$$

By definition (25), there exists a matrix  $A$  of dimension  $n \times m$ , being a submatrix of  $U$ , and two normalized vectors  $|x\rangle$  and  $|y\rangle$  of size  $n$  and  $m$ , respectively, such that  $n + m = k + 1$

and

$$
s _ {k} = | \langle x | A | y \rangle |. \tag {B4}
$$

Without loss of generality we can assume that  $n \geqslant m$ . Since the vector  $|x\rangle$  is normalized there exist  $i \in \{1,2,\dots,n\}$ , such that  $|x_{i}| \leqslant 1 / \sqrt{n}$  (by permuting the indices we may assume that  $|x_{1}| \leqslant 1 / \sqrt{n}$ ). Next we write

$$
\begin{array}{l} s _ {k} = | \langle x | A | y \rangle | = \left| \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} \bar {x} _ {i} A _ {i j} y _ {j} \right| \\ = \left| \sum_ {i = 2} ^ {n} \sum_ {j = 1} ^ {m} \bar {x _ {i}} A _ {i j} y _ {j} + \bar {x _ {1}} \sum_ {j = 1} ^ {m} A _ {1 j} y _ {j} \right| \\ = \left| \langle \tilde {x} | \tilde {A} | y \rangle + \bar {x _ {1}} \langle a _ {1} | y \rangle \right|, \tag {B5} \\ \end{array}
$$

where  $\langle \tilde{x} |$  denotes the bra vector  $\langle x|$  without the first component, while  $\tilde{A}$  denotes the matrix  $A$  without its first row and  $\langle a_1|$  denotes the first row of  $A$ . Next, we bound  $s_k$  with the help of the triangle inequality, the Cauchy-Schwarz inequality, and the fact that the overlap with normalized vectors does not exceed the largest singular value:

$$
\begin{array}{l} s _ {k} = | \langle \tilde {x} | \tilde {A} | y \rangle + \overline {{x _ {1}}} \langle a _ {1} | y \rangle | \leqslant | \langle \tilde {x} | \tilde {A} | y \rangle | + | x _ {1} | | \langle a _ {1} | y \rangle | \\ \leqslant \sqrt {1 - | x _ {1} | ^ {2}} \sigma_ {1} (\tilde {A}) + | x _ {1} | \| a _ {1} \|. \tag {B6} \\ \end{array}
$$

Now using the fact, that  $\max_{i,j}|U_{ij}| = s_1$  we get that  $\| a_1\| \leqslant \sqrt{m} s_1$ ; we also have  $x_{1}\leqslant \frac{1}{\sqrt{n}}$  and  $\sqrt{1 - |x_1|^2}\leqslant 1$ , and by definition  $\sigma_{1}(\tilde{A})\leqslant s_{k - 1}$ . We obtain

$$
\begin{array}{l} s _ {k} \leqslant \sqrt {1 - | x _ {1} | ^ {2}} \sigma_ {1} (\tilde {A}) + | x _ {1} | \| a _ {1} \| \leqslant \sigma_ {1} (\tilde {A}) + \frac {1}{\sqrt {n}} \| a _ {1} \| \\ \leqslant s _ {k - 1} + \frac {\sqrt {m}}{\sqrt {n}} s _ {1} \leqslant s _ {k - 1} + s _ {1}, \tag {B7} \\ \end{array}
$$

which directly implies Eq. (B3).

To prove the majorization relation  $W \prec Q^{(d - 1)}$  we note that for  $k \in \{2, \dots, N\}$  we have  $Q_k^{(d - 1)} \leqslant W_k$ ; to see it we write

$$
\begin{array}{l} R _ {k} - R _ {k - 1} = \frac {1}{4} \left[ s _ {k} ^ {2} - s _ {k - 1} ^ {2} + 2 \left(s _ {k} - s _ {k - 1}\right) \right] \\ = \frac {1}{4} (s _ {k} - s _ {k - 1}) (s _ {k} + s _ {k - 1} + 2) \\ \leqslant \left(s _ {k} - s _ {k - 1}\right). \tag {B8} \\ \end{array}
$$

The last inequality follows from the fact that  $s_{k - 1} \leqslant s_k \leqslant 1$ .

Using inequality (B3) we know that  $W_{1} \geqslant W_{k}$  and  $Q_{1}^{(d - 1)} \geqslant Q_{k}^{(d - 1)}$  for any  $k \in \{1,2,\dots ,N\}$ . This implies that the sums of the smallest elements obey the following inequalities:

$$
(W ^ {\uparrow}) _ {1} \geqslant (Q ^ {\uparrow}) _ {1}
$$

$$
\left(W ^ {\uparrow}\right) _ {1} + \left(W ^ {\uparrow}\right) _ {2} \geqslant \left(Q ^ {\uparrow}\right) _ {1} + \left(Q ^ {\uparrow}\right) _ {2} \tag {B9}
$$

$$
(W ^ {\uparrow}) _ {1} + (W ^ {\uparrow}) _ {2} + (W ^ {\uparrow}) _ {3} \geqslant (Q ^ {\uparrow}) _ {1} + (Q ^ {\uparrow}) _ {2} + (Q ^ {\uparrow}) _ {3}
$$

：

where  $(W^{\uparrow})$  and  $(Q^{\uparrow})$  are vectors  $W$  and  $Q^{(d - 1)}$  ordered increasingly. Since the total sum of both vectors is the same (and equal to 1) we obtain the desired majorization relation  $W\prec Q^{(d - 1)}$ .

[1] S. Wehner and A. Winter, New J. Phys. 12, 025009 (2010).  
[2] I. Bialynicki-Birula and L. Rudnicki, in Statistical Complexity, edited by K. D. Sen (Springer, Berlin, 2011), pp. 1-34.  
[3] A. E. Rastegin, Int. J. Theor. Phys. 51, 1314 (2012).  
[4] Z. Puchala, L. Rudnicki, and K. Žyczkowski, J. Phys. A 46, 272002 (2013).  
[5] S. Friedland, V. Gheorghiu, and G. Gour, Phys. Rev. Lett. 111, 230401 (2013).  
[6] P. J. Coles and M. Piani, Phys. Rev. A 89, 022112 (2014).  
[7] S. Zozor, G. M. Bosyk, and M. Portesi, arXiv:1311.5602.  
[8] M. Berta, M. Christandl, R. Colbeck, J. M. Renes, and R. Renner, Nat. Phys. 6, 659 (2010).  
[9] J. Schneeloch, C. J. Broadbent, and J. C. Howell, Phys. Lett. A 378, 766 (2014).  
[10] J. Havrda and F. Charvat, Kybernetica 3, 30 (1967).  
[11] I. Białynicki-Birula and J. Mycielski, Commun. Math. Phys. 44, 129 (1975).  
[12] D. Deutsch, Phys. Rev. Lett. 50, 631 (1983).  
[13] H. Maassen and J. B. M. Uffink, Phys. Rev. Lett. 60, 1103 (1988).

[14] S. Zozor, G. M. Bosyk, and M. Portesi, J. Phys. A 46, 465301 (2013).  
[15] J. I. de Vicente and J. Sánchez-Ruiz, Phys. Rev. A 77, 042110 (2008).  
[16] G. M. Bosyk, M. Portesi, A. Plastino, and S. Zozor, Phys. Rev. A 84, 056101 (2011).  
[17] J. Sánchez, Phys. Lett. A 173, 233 (1993).  
[18] G. Ghirardi, L. Marinatto, and R. Romano, Phys. Lett. A 317, 32 (2003).  
[19] G. M. Bosyk, M. Portesi, and A. Plastino, Phys. Rev. A 85, 012108 (2012).  
[20] M. H. Partovi, Phys. Rev. A 84, 052117 (2011).  
[21] P. Coles, L. Yu, V. Gheorghiu, and R. Griffiths, Phys. Rev. A 83, 062338 (2011).  
[22] R. Adamczak, R. Latała, Z. Puchała, and K. Žyczkowski (unpublished).  
[23] K. Korzekwa, M. Lostaglio, D. Jennings, and T. Rudolph, Phys. Rev. A 89, 042122 (2014).  
[24] O. Gühne and M. Lewenstein, Phys. Rev. A 70, 022316 (2004).  
[25] M. J. W. Hall, Phys. Rev. Lett. 74, 3307 (1995).  
[26] A. Grudka, M. Horodecki, P. Horodecki, R. Horodecki, W. Klobus, and L. Pankowski, Phys. Rev. A 88, 032106 (2013).