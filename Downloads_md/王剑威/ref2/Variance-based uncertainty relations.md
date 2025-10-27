# Variance-based uncertainty relations

Yichen Huang

Department of Physics, University of California, Berkeley, Berkeley, California 94720, USA

(Received 21 June 2012; published 10 August 2012)

Uncertainty relations are fundamental in quantum mechanics. Here I propose state-independent variance-based uncertainty relations for two or more arbitrary observables in finite dimensional spaces. The uncertainty relations provide near-optimal lower bounds in some typical examples, and are useful for entanglement detection.

DOI: 10.1103/PhysRevA.86.024101

PACS number(s): 03.65.Ca, 03.65.Ta, 03.65.Aa

# I. INTRODUCTION

Uncertainty relations are fundamental in quantum mechanics, underlying many conceptual differences between classical and quantum theories. They reveal by rigorous inequalities that incompatible observables cannot be measured to arbitrarily high precision simultaneously. They are useful in many areas related or even unrelated to quantum mechanics: entanglement detection [1-4], quantum cryptography [5], signal processing [6], etc.

The Heisenberg uncertainty relation [7] reads

$$
V (A) V (B) \geqslant | \langle \Psi | [ A, B ] | \Psi \rangle | ^ {2} / 4, \tag {1}
$$

where  $V(A), V(B)$  are the variances of the Hermitian operators  $A, B$ . The formulation of the Heisenberg uncertainty relation is not always satisfactory. For instance, the lower bound is trivial when  $\langle \Psi | [A, B] | \Psi \rangle$  happens to be zero, which in finite dimensional spaces is always possible. Also, the lower bound depends on the state  $|\Psi \rangle$ , while in some applications a state-independent lower bound is needed [3]. It is thus necessary to derive state-independent variance-based uncertainty relations. Note that no nontrivial state-independent lower bounds on the sum of the variances of two or more arbitrary observables are known, even if this formulation of uncertainty relations is precisely what is called for in literature [3].

Entropic uncertainty relations provide state-independent lower bounds on the sum of the entropies of two or more observables. They are especially useful in quantum cryptography [5]. A lot of entropic uncertainty relations are proposed for observables in both finite [5,8-10] and infinite [11-13] dimensional spaces.

Here I propose state-independent variance-based uncertainty relations. Section II derives state-independent lower bounds on the sum of the variances of two or more arbitrary observables in finite dimensional spaces. Section III concludes with some typical examples in which the lower bounds are near-optimal and with the application to entanglement detection. The Appendix briefly surveys entropic uncertainty relations, which are useful in formulating the main theorems.

# II. MAIN THEOREMS

Let  $\{\{|a_i^j\rangle |j = 1,2,\dots ,n\} |i = 1,2,\dots ,m\}$  be a set of  $m$  orthonormal bases of an  $n$  -dimensional Hilbert space, and  $A_{i} = \sum_{j = 1}^{n}a_{i}^{j}|a_{i}^{j}\rangle \langle a_{i}^{j}|$  be  $m$  Hermitian operators, where  $a_{i}^{j}\in$ $\mathbf{R}$  and  $|a_i^j\rangle$  are the eigenvalues and the eigenvectors of  $A_{i}$  respectively. For notational simplicity, let  $p_i^j = |\langle a_i^j |\Psi \rangle |^2$

The Shannon entropy of  $A_{i}$  is

$$
H \left(A _ {i}\right) = - \sum_ {j = 1} ^ {n} p _ {i} ^ {j} \ln p _ {i} ^ {j}. \tag {2}
$$

From now on, assume the entropic uncertainty relation

$$
\sum_ {i = 1} ^ {m} H \left(A _ {i}\right) \geqslant C. \tag {3}
$$

Let  $\alpha$  be a variational parameter. All the inequalities below hold for any  $\alpha \in \mathbf{R}$ .

Lemma.

$$
\alpha V \left(A _ {i}\right) \geqslant H \left(A _ {i}\right) - \ln \sum_ {j = 1} ^ {n} e ^ {- \alpha \left(a _ {i} ^ {j} - \left\langle A _ {i} \right\rangle\right) ^ {2}}. \tag {4}
$$

Proof. Using the basic inequality  $e^x \geqslant 1 + x$  with  $x = -\alpha (a_i^k - \langle A_i \rangle)^2 - \ln p_i^k \sum_{j=1}^{n} e^{-\alpha (a_i^j - \langle A_i \rangle)^2}$ ,

$$
\begin{array}{l} 1 = \sum_ {k = 1} ^ {n} p _ {i} ^ {k} \times \frac {e ^ {- \alpha \left(a _ {i} ^ {k} - \left\langle A _ {i} \right\rangle\right) ^ {2}}}{p _ {i} ^ {k} \sum_ {j = 1} ^ {n} e ^ {- \alpha \left(a _ {i} ^ {j} - \left\langle A _ {i} \right\rangle\right) ^ {2}}} \\ \geqslant \sum_ {k = 1} ^ {n} p _ {i} ^ {k} \left(1 - \alpha \left(a _ {i} ^ {k} - \langle A _ {i} \rangle\right) ^ {2} - \ln p _ {i} ^ {k} \sum_ {j = 1} ^ {n} e ^ {- \alpha \left(a _ {i} ^ {j} - \langle A _ {i} \rangle\right) ^ {2}}\right) \\ = \sum_ {k = 1} ^ {n} p _ {i} ^ {k} - \alpha \sum_ {k = 1} ^ {n} p _ {i} ^ {k} \left(a _ {i} ^ {k} - \langle A _ {i} \rangle\right) ^ {2} - \sum_ {k = 1} ^ {n} p _ {i} ^ {k} \ln p _ {i} ^ {k} \\ - \left(\sum_ {k = 1} ^ {n} p _ {i} ^ {k}\right) \ln \sum_ {j = 1} ^ {n} e ^ {- \alpha \left(a _ {i} ^ {j} - \langle A _ {i} \rangle\right) ^ {2}} \\ = 1 - \alpha V \left(A _ {i}\right) + H \left(A _ {i}\right) - \ln \sum_ {j = 1} ^ {n} e ^ {- \alpha \left(a _ {i} ^ {j} - \langle A _ {i} \rangle\right) ^ {2}}. \tag {5} \\ \end{array}
$$

Theorem 1. State-dependent variance-based uncertainty relations. Add Eq. (4) for  $i = 1,2,\dots,m$ :

$$
\alpha \sum_ {i = 1} ^ {m} V \left(A _ {i}\right) \geqslant C - \sum_ {i = 1} ^ {m} \ln \sum_ {j = 1} ^ {n} e ^ {- \alpha \left(a _ {i} ^ {j} - \left\langle A _ {i} \right\rangle\right) ^ {2}}. \tag {6}
$$

Theorem 2. State-independent variance-based uncertainty relations. Note  $\min_k a_i^k \leqslant \langle A_i \rangle \leqslant \max_k a_i^k$ :

$$
\alpha \sum_ {i = 1} ^ {m} V \left(A _ {i}\right) \geqslant C - \sum_ {i = 1} ^ {m} \ln \max  _ {\min  _ {k} a _ {i} ^ {k} \leqslant \beta_ {i} \leqslant \max  _ {k} a _ {i} ^ {k}} \sum_ {j = 1} ^ {n} e ^ {- \alpha \left(a _ {i} ^ {j} - \beta_ {i}\right) ^ {2}}. \tag {7}
$$

Usually the maximum in Eq. (7) cannot be computed analytically, but it is easy to compute numerically. Theorems 1

and 2 hold more generally for positive-operator valued measures provided with the corresponding entropic uncertainty relations for positive-operator valued measures.

# III. EXAMPLES, APPLICATIONS, AND CONCLUSIONS

A set of  $m$  orthonormal bases of an  $n$ -dimensional Hilbert space is mutually unbiased if

$$
\left| \left\langle a _ {i} ^ {j} \right| a _ {l} ^ {k} \right\rangle \left| = (1 - \delta_ {i l}) / \sqrt {n} + \delta_ {i l} \delta_ {j k} \right. \tag {8}
$$

for  $i,l = 1,2,\ldots ,m;j,k = 1,2,\ldots ,n$  .Mutually unbiased bases are especially useful in quantum cryptography [5].

Example 1. The eigenvectors of the Pauli matrices are mutually unbiased bases. Equation (A3) shows  $C = 2 \ln 2$ . The optimal choice of the variational parameter is  $\alpha = 0.597$ :

$$
V \left(\sigma_ {x}\right) + V \left(\sigma_ {y}\right) + V \left(\sigma_ {z}\right) > 1. 7 2 4 3. \tag {9}
$$

Example 2. The eigenvectors of the matrices

$$
\begin{array}{l} \sigma_ {0} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right), \quad \sigma_ {1} = \frac {i}{\sqrt {3}} \left( \begin{array}{c c c} 0 & - 1 & 1 \\ 1 & 0 & - 1 \\ - 1 & 1 & 0 \end{array} \right), \\ \sigma_ {2} = \frac {1}{\sqrt {3}} \left( \begin{array}{c c c} 0 & \omega^ {1 1} & \omega^ {9} \\ \omega & 0 & \omega^ {7} \\ \omega^ {3} & \omega^ {5} & 0 \end{array} \right), \quad \sigma_ {3} = \frac {1}{\sqrt {3}} \left( \begin{array}{c c c} 0 & \omega & \omega^ {3} \\ \omega^ {1 1} & 0 & \omega^ {5} \\ \omega^ {9} & \omega^ {7} & 0 \end{array} \right) \tag {10} \\ \end{array}
$$

are mutually unbiased bases, where  $\omega = e^{\pi i / 6}$ . Equation (A3) shows  $C = 4$  in 2. The optimal choice of the variational parameter is  $\alpha = 1.92$ :

$$
V \left(\sigma_ {0}\right) + V \left(\sigma_ {1}\right) + V \left(\sigma_ {2}\right) + V \left(\sigma_ {3}\right) > 0. 9 0 8 3. \tag {11}
$$

The lower bounds in Eqs. (9) and (11) are near-optimal since the optimal lower bounds are 2 and 1, respectively.

The state-independent variance-based uncertainty relation Eq. (7) is precisely in the formulation that is called for in the literature of entanglement detection [3]. Entanglement detection is an important problem as entanglement plays a key role in quantum information. Among many detection schemes [1,2], the entanglement criterion based on local uncertainty relations [3] is well-known. It is a necessary condition for separability:

$$
\sum_ {i} V \left(A _ {i} + B _ {i}\right) \geqslant U _ {A} + U _ {B}, \tag {12}
$$

where  $A_{i}$  and  $B_{i}$  are Hermitian operators on the first and the second subspaces, respectively, with  $U_{A}, U_{B}$  given by the state-independent variance-based uncertainty relations:

$$
\sum_ {i} V \left(A _ {i}\right) \geqslant U _ {A}, \quad \sum_ {i} V \left(B _ {i}\right) \geqslant U _ {B}. \tag {13}
$$

Section II in [3] appreciates the importance of  $U_A$ ,  $U_B$  in formulating the criterion, but how to evaluate  $U_A$ ,  $U_B$  remains unclear, which is very inconvenient for users. The state-independent variance-based uncertainty relation Eq. (7) precisely fills the gap.

In conclusion, I have proposed state-independent variance-based uncertainty relations for two or more arbitrary observables in finite dimensional spaces. The uncertainty relations provide near-optimal lower bounds in some typical examples, and are useful for entanglement detection.

# APPENDIX: BRIEF SURVEY OF ENTROPIC UNCERTAINTY RELATIONS

Entropic uncertainty relations are useful in formulating the main theorems. See [5] for a recent comprehensive survey.

The entropic uncertainty relation for two Hermitian operators [8] reads

$$
H \left(A _ {1}\right) + H \left(A _ {2}\right) \geqslant - 2 \ln \max  _ {1 \leqslant j, k \leqslant n} \left| \left\langle a _ {1} ^ {j} \mid a _ {2} ^ {k} \right\rangle \right|, \tag {A1}
$$

and the lower bound is improved for  $\max_{1\leqslant j,k\leqslant n}|\langle a_1^j |a_2^k\rangle |\geqslant$ $1 / \sqrt{2}$  [9]. Equation (A1) reduces to

$$
H \left(A _ {1}\right) + H \left(A _ {2}\right) \geqslant \ln n \tag {A2}
$$

for mutually unbiased bases. The entropic uncertainty relation for  $n + 1$  mutually unbiased bases [10] reads

$$
\sum_ {i = 1} ^ {n + 1} H \left(A _ {i}\right) \geqslant \left[ \frac {n + 1}{2} \right] \ln \left[ \frac {n + 1}{2} \right] + \left[ \frac {n + 2}{2} \right] \ln \left[ \frac {n + 2}{2} \right], \tag {A3}
$$

where  $[\cdot ]$  denotes the floor function. The entropic uncertainty relation for the position and the momentum operators  $x,p$  [11,12] reads

$$
H (x) + H (p) \geqslant 1 + \ln \pi . \tag {A4}
$$

Its multimode generalization is given in [13].

[1] R. Horodecki, P. Horodecki, M. Horodecki, and K. Horodecki, Rev. Mod. Phys. 81, 865 (2009).  
[2] O. Guhne and G. Toth, Phys. Rep. 474, 1 (2009).  
[3] H. F. Hofmann and S. Takeuchi, Phys. Rev. A 68, 032103 (2003).  
[4] Y. Huang, Phys. Rev. A 82, 012335 (2010); 82, 069903(E) (2010).  
[5] S. Wehner and A. Winter, New J. Phys. 12, 025009 (2010).  
[6] E. Candes, J. Romberg, and T. Tao, IEEE Trans. Inf. Theory 52, 489 (2006).

[7] H. P. Robertson, Phys. Rev. 34, 163 (1929).  
[8] H. Maassen and J. B. M. Uffink, Phys. Rev. Lett. 60, 1103 (1988).  
[9] J. I. de Vicente and J. Sanchez-Ruiz, Phys. Rev. A 77, 042110 (2008); G. M. Bosyk, M. Portesi, A. Plastino, and S. Zozor, ibid. 84, 056101 (2011).  
[10] J. Sanchez-Ruiz, Phys. Lett. A 201, 125 (1995).  
[11] W. Beckner, Ann. Math. 102, 159 (1975).  
[12] I. Bialynicki-Birula and J. Mycielski, Commun. Math. Phys. 44, 129 (1975).  
[13] Y. Huang, Phys. Rev. A 83, 052124 (2011).