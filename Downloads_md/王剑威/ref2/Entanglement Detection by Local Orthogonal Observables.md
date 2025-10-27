# Entanglement Detection by Local Orthogonal Observables

Sixia Yu and Nai-le Liu

Department of Modern Physics & Hefei National Laboratory for Physical Sciences at Microscale, University of Science and Technology of China, Hefei, Anhui 230026, People's Republic of China (Received 6 January 2005; published 7 October 2005)

We propose a family of entanglement witnesses and corresponding positive maps that are not completely positive based on local orthogonal observables. As applications the entanglement witness of a  $3 \times 3$  bound entangled state [P. Horodecki, Phys. Lett. A 232, 333 (1997)] is explicitly constructed and a family of  $d \times d$  bound entangled states is introduced, whose entanglement can be detected by permuting local orthogonal observables. The proposed criterion of separability can be physically realized by measuring a Hermitian correlation matrix of local orthogonal observables.

DOI: 10.1103/PhysRevLett.95.150504

Introduction. Entangled states are valuable resources for quantum computation and communication. However the boundary between the entangled states and the separable states, states that can be prepared by means of local operations and classical communications [1], is still not well characterized. Entanglement detection turns out to be a rather tantalizing problem.

There have been many approaches to the problem such as the partial transposition criterion [2,3], the realignment criterion [4,5], the symmetric extension criterion [6,7], and the equation-solving method [8], to name a few. Many criteria such as the partial transposition criterion and the reduction criterion arise from positive maps that are not completely positive (non-CP). A state is separable if and only if the state keeps its positivity under all non-CP maps [3]. The entangled states with positive partial transposition (PPT) belong to bound entangled states [9] while the states violating the reduction criterion can be distilled, or are free entangled [10]. The non-CP maps are not very easy to find and they are not physically realizable. There are also some physical approaches including Bell inequalities [11-13], local uncertainty relationships [14-16], and entanglement witnesses [10,12]. A 3-setting Bell-like inequality is found to be a sufficient and necessary condition for the  $2 \times 2$  system [14]. A local uncertainty relation is found to be violated by bound entangled states [15,16].

In this Letter we shall at first construct a family of entanglement witnesses, from which a generalization of the reduction criterion can be derived, based on local orthogonal observables. Then we apply our criterion of separability to several bound entangled states, including a family of bound entangled states where the criterion is sufficient and necessary. Finally, we reformulate the criterion in terms of physically measurable quantities, namely, Hermitian correlation matrices.

Local orthogonal observables.-We consider a  $d \times d$  system, a bipartite system with two  $d$ -level subsystems labeled by  $A$  and  $B$ , whose Hilbert space is spanned by  $|m, n\rangle = |m\rangle \otimes |n\rangle$ ,  $(m, n = 1, 2, \ldots, d)$ . For each system a complete set of local orthogonal observables (LOOs) is a set of  $d^2$  observables  $A_\mu (\mu = 1, 2, \ldots, d^2)$  of this system

PACS numbers: 03.67.Mn, 03.65.Ta, 03.65.Ud

satisfying orthogonal relations

$$
\mathrm {T r} \left(A _ {\mu} A _ {\nu}\right) = \delta_ {\mu \nu}, \qquad (\mu , \nu = 1, 2, \ldots , d ^ {2}). \qquad (1)
$$

The set of LOOs is complete in two senses. First, they form an orthonormal basis for all the operators in the Hilbert space of a  $d$ -level system. For example, a density matrix  $\varrho_{A}$  may have an expansion  $\varrho_{A} = \sum_{\mu} \mathrm{Tr}(\varrho_{A} A_{\mu}) A_{\mu}$ . Second,  $d^{2}$  states  $|A_{\mu}\rangle \equiv A_{\mu}|\Phi\rangle$  form an orthonormal basis for the composite system, where  $|\Phi\rangle = \sum_{m} |m, m\rangle$  and  $A_{\mu}$  act on the first subsystem.

In the case of qubits, a typical complete set of LOOs can be  $\{I,\sigma_x,\sigma_y,\sigma_z\} /\sqrt{2}$ . For later use, we define a standard complete set of LOOs  $\{\lambda_{\mu}\} = \{\lambda_m = |m\rangle \langle m|,\lambda_{mn}^{\pm}\}$ $(m,n = 1,2,\ldots ,d)$  where

$$
\lambda_ {m n} ^ {+} = \frac {| m \rangle \langle n | + | n \rangle \langle m |}{\sqrt {2}} \quad (m <   n), \tag {2a}
$$

$$
\lambda_ {m n} ^ {-} = \frac {| m \rangle \langle n | - | n \rangle \langle m |}{i \sqrt {2}} \quad (m <   n). \tag {2b}
$$

As testing observables  $\lambda_{m}$  stand for 2-outcome tests while the rest of the observables represent 3-outcome tests ( $d \geq 3$ ). In this standard basis, an arbitrary complete set of LOOs is characterized by an orthogonal  $d^{2} \times d^{2}$  real matrix  $O$  such that

$$
\lambda_ {\mu} ^ {o} = \sum_ {\nu = 1} ^ {d ^ {2}} O _ {\mu \nu} \lambda_ {\nu}. \tag {3}
$$

Specially,  $\{\lambda_{\mu}^{u} = u\lambda_{\mu}u^{\dagger}\}$  with  $u$  being unitary is also a complete set of LOOs. Not all LOOs can be generated by unitary transformations. For example, there is no  $u$  such that  $\lambda_{\mu}^{T} = \lambda_{\mu}^{u}$ , where  $\lambda_{\mu}^{T}$  denotes the transposition of the standard LOOs.

Entanglement witness.—Entanglement witness (EW) is an observable of the composite system that has (i) nonnegative expectation values in all separable states and (ii) at least one negative eigenvalue. We call an observable a candidate of EW if it satisfies the condition (i).

If we choose an arbitrary set of LOOs  $\{\lambda_{\mu}^{o}\}$  for system  $A$  and the transposition of the standard set  $\{\lambda_{\mu}^{T}\}$  for system  $B$ ,

then the observable defined as

$$
E _ {O} = I \otimes I - \sum_ {\mu = 1} ^ {d ^ {2}} \lambda_ {\mu} ^ {o} \otimes \lambda_ {\mu} ^ {T} \tag {4}
$$

is an EW candidate for all orthogonal  $O$ . This is because in any product state  $\rho = \varrho_{1} \otimes \varrho_{2}$  we have

$$
\begin{array}{l} \operatorname {T r} \left(\rho E _ {O}\right) = 1 - \sum_ {\mu} \left\langle \lambda_ {\mu} ^ {o} \right\rangle_ {1} \left\langle \lambda_ {\mu} ^ {T} \right\rangle_ {2} \\ \geq 1 - \sqrt {\sum_ {\mu} \langle \lambda_ {\mu} ^ {o} \rangle_ {1} ^ {2}} \sqrt {\sum_ {\mu} \langle \lambda_ {\mu} ^ {T} \rangle_ {2} ^ {2}} \\ = 1 - \sqrt {\operatorname {T r} \varrho_ {1} ^ {2} \operatorname {T r} \varrho_ {2} ^ {2}} \geq 0 \tag {5} \\ \end{array}
$$

by using the Cauchy inequality, the orthogonality and completeness of the LOOs. If the complete set of LOOs is so chosen that the EW candidate  $E_O$  does possess at least one negative eigenvalue then we obtain an EW. From the proof of the inequality above it is obvious that instead of  $O$  being orthogonal the condition  $OO^T \leq 1$  is enough for the construction of an EW candidate. We shall encounter this kind of EW in the following example.

It should be noted that the transposition in the definition of our EW as in Eq. (4) is not crucial since the orthogonal  $O_{\mathrm{c}}$

$$
A _ {1} = \frac {1}{\sqrt {3}} (\lambda_ {1} + \lambda_ {2} + \lambda_ {3}) = B _ {1}, A _ {2} = \frac {1}{\sqrt {2}} (\lambda_ {1} - \lambda_ {2}), B _ {2} = \frac {1}{\sqrt {2}} (\lambda_ {3} - \lambda_ {1}), A _ {3} = \frac {1 + 2 a}{\sqrt {6} (2 + a)} (2 \lambda_ {3} - \lambda_ {1} - \lambda_ {2}) - \frac {\sqrt {3 (1 - a ^ {2})}}{2 + a} \lambda_ {1 3} ^ {+},
$$

$$
B _ {3} = \frac {1}{\sqrt {6}} (\lambda_ {1} + \lambda_ {3} - 2 \lambda_ {2}), \quad A _ {4} = \frac {1 + 2 a}{2 + a} \lambda_ {1 3} ^ {+} + \frac {\sqrt {1 - a ^ {2}}}{\sqrt {2} (2 + a)} (2 \lambda_ {3} - \lambda_ {1} - \lambda_ {2}), \quad B _ {4} = \lambda_ {1 3} ^ {+}, \quad A _ {5} = \lambda_ {1 3} ^ {-} = B _ {5},
$$

$$
A _ {6} = \lambda_ {1 2} ^ {+} = B _ {6}, \quad A _ {7} = \lambda_ {1 2} ^ {-} = B _ {7}, \quad A _ {8} = \lambda_ {2 3} ^ {+} = B _ {8}, \quad A _ {9} = \lambda_ {2 3} ^ {-} = B _ {9}. \tag {7}
$$

We note that  $A_{1} = B_{1}$  is proportional to the identity matrix and other 8 observables  $B_{i}$  ( $i = 2,3,\ldots ,9$ ) of system  $B$  are exactly those 8 Gell-Mann matrices, and observables  $A_{i}$  ( $i = 2,3,\ldots ,9$ ) of system  $A$  are Gell-Mann matrices with an interchanging of energy levels 2 and 3 and a certain rotation. A similar choice of local observables has also been used to detect the entanglement of  $\rho_{a}$  by a local uncertainty relationship [15]. Then we expand the density matrix  $\rho_{a}$  in the basis  $\{A_{\mu}\otimes B_{\nu}^{T}\}$  with coefficients  $\rho_{\mu \nu} = \mathrm{Tr}(\rho_{a}A_{\mu}\otimes B_{\nu}^{T})$ . In fact the LOOs Eq. (7) are designed to make  $\sum_{\mu}\rho_{\mu \mu} = 1$ . Now we define a real matrix  $M$  with only the following elements

$$
M _ {\mu \mu} = \frac {1}{\sqrt {1 + n ^ {2}}}, \quad M _ {1 \nu} = - M _ {\nu 1} = \frac {n _ {\nu}}{\sqrt {1 + n ^ {2}}} \tag {8}
$$

nonzero, where the vector defined by  $n_{\nu} = \rho_{1\nu} - \rho_{\nu 1}$  with  $\nu = 2,\ldots ,9$  has a nonzero norm

$$
n ^ {2} = \sum_ {\nu = 2} ^ {9} n _ {\nu} ^ {2} = \frac {(1 - a) a ^ {2}}{(2 + a) (1 + 8 a) ^ {2}}. \tag {9}
$$

Obviously, we have  $M^T M \leq 1$ . So we have an EW candidate

$$
E _ {a} = I \otimes I - \sum_ {\mu , \nu = 1} ^ {d ^ {2}} M _ {\mu \nu} A _ {\mu} \otimes B _ {\nu} ^ {T}. \tag {10}
$$

matrix is arbitrary. However, as we see later, the appearance of the partial transposition will render the positive map corresponding to our EW into a simpler form. Furthermore, under the operator basis  $\{\lambda_{\mu} \otimes \lambda_{\nu}^{T}\}$  the density matrix of the maximally entangled state  $|\Phi\rangle$  is proportional to the identity matrix.

As an application, we shall construct explicitly an EW for the  $3 \times 3$  bound entangled state introduced in Ref. [17]. In the basis  $\{|m,n\rangle\}$  arranged in the ordering  $3(m - 1) + n$ , the density matrix reads

$$
\rho_ {a} = \frac {1}{1 + 8 a} \left( \begin{array}{c c c c c c c c c} a & 0 & 0 & 0 & a & 0 & 0 & 0 & a \\ 0 & a & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & a & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & a & 0 & 0 & 0 & 0 & 0 \\ a & 0 & 0 & 0 & a & 0 & 0 & 0 & a \\ 0 & 0 & 0 & 0 & 0 & a & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & \frac {1 + a}{2} & 0 & \frac {\sqrt {1 - a ^ {2}}}{2} \\ 0 & 0 & 0 & 0 & 0 & 0 & \frac {0}{2} & a & 0 \\ a & 0 & 0 & 0 & a & 0 & \frac {\sqrt {1 - a ^ {2}}}{2} & 0 & \frac {1 + a}{2} \end{array} \right). \tag {6}
$$

The state  $\rho_{a}$  has PPT while being entangled for all  $0 < a < 1$ . At first we choose special sets of LOOs  $\{A_{\mu}\}$  and  $\{B_{\mu}\}$  for systems  $A$  and  $B$ , respectively, as follows:

$$
\lambda_ {3} - \lambda_ {1}), \quad A _ {3} = \frac {1 + 2 a}{\sqrt {6} (2 + a)} (2 \lambda_ {3} - \lambda_ {1} - \lambda_ {2}) - \frac {\sqrt {3 (1 - a ^ {2})}}{2 + a} \lambda_ {1 3} ^ {+},
$$

$$
\frac {- a ^ {2}}{+ a)} (2 \lambda_ {3} - \lambda_ {1} - \lambda_ {2}), \quad B _ {4} = \lambda_ {1 3} ^ {+}, \quad A _ {5} = \lambda_ {1 3} ^ {-} = B _ {5},
$$

$$
, \quad A _ {9} = \lambda_ {2 3} ^ {-} = B _ {9}. \tag {7}
$$

Its expectation values in separable states are all nonnegative while its expectation value in the state  $\rho_{a}$  reads

$$
\operatorname {T r} \left(\rho_ {a} E _ {a}\right) = 1 - \sqrt {1 + n ^ {2}} <   0 \tag {11}
$$

for all  $0 < a < 1$ . Therefore we obtain explicitly an EW for the state  $\rho_{a}$ . Of course the entanglement of  $\rho_{a}$  can also be detected by the non-CP map corresponding to the EW  $E_{a}$ .

O-reduction criterion.-To each EW candidate  $E_{O}$  we can associate a positive map through the Jamiołkowski isomorphism [18] as follows

$$
\begin{array}{l} \mathcal {O} (\varrho) = \operatorname {T r} _ {B} (I \otimes \varrho^ {T} E _ {O}) = I \operatorname {T r} \varrho - \sum_ {\mu} \langle \lambda_ {\mu} \rangle_ {\varrho} \lambda_ {\mu} ^ {o} \\ \equiv I \operatorname {T r} \varrho - \varrho^ {o}. \tag {12} \\ \end{array}
$$

Thus we have a separability criterion: if a state  $\rho$  of the composite system is separable then

$$
\mathcal {O} \otimes I (\rho) = \operatorname {T r} _ {A} \rho - \rho^ {o _ {A}} \geq 0, \tag {13}
$$

for all orthogonal  $O$ , where

$$
\rho^ {o _ {A}} = \sum_ {\mu , v = 1} ^ {d ^ {2}} \left\langle \lambda_ {\mu} \otimes \lambda_ {\nu} ^ {T} \right\rangle_ {\rho} \lambda_ {\mu} ^ {o} \otimes \lambda_ {\nu} ^ {T}. \tag {14}
$$

Not all choices of  $O$  will result in a non-CP map. For example if the orthogonal  $O$  is generated by the trans

position, then the resulting map is completely positive. If the orthogonal  $O$  is generated by a unitary transformation, then we obtain the reduction map  $I\operatorname{Tr}\varrho - \varrho$ . Thus we refer to the above separability criterion as  $O$ -reduction criterion. It turns out that it is exactly the LOOs which cannot be generated by unitary transformations that are crucial to the detection of bound entanglement.

As is well known the reduction map is a decomposable non-CP map, i.e., a composition of the transposition and a completely positive map. The construction of indecomposable non-CP maps is somewhat involved, e.g., based on some maximization or minimization procedures [19], or dependent on some special states [20]. Here we shall see that some simple non-CP maps induced by the permutation of LOOs are not decomposable, i.e., they can be used to detect bound entangled states with PPT.

We consider an arbitrary permutation  $\lambda_{\mu} \mapsto \lambda_{\sigma(\mu)}$  of the standard LOOs. In the state  $|\Phi\rangle$  (not normalized) the expectation value of the induced EW candidate

$$
E _ {\sigma} = I \otimes I - \sum_ {\mu = 1} ^ {d ^ {2}} \lambda_ {\sigma (\mu)} \otimes \lambda_ {\mu} ^ {T} \tag {15}
$$

reads  $d - \sum_{\mu} \operatorname{Tr}(\lambda_{\sigma(\mu)} \lambda_{\mu})$ , which is negative if the permutation leaves more than  $d$  observables unchanged; i.e., map  $\mu \mapsto \sigma(\mu)$  has at least  $d + 1$  fix points. In this case we obtain an EW and a non-CP map  $I \operatorname{Tr}\varrho - \varrho^{\sigma}$ .

More specifically we consider a permutation among  $d$  observables  $\lambda_{m}$  in the standard set of LOOs  $\lambda_{\mu}$  while all other LOOs remain unchanged. This permutation of LOOs corresponds to a permutation of the diagonal elements of the density matrix in the basis  $\{|m\rangle \}$ . Since there are  $d^{2} - d > d(d\geq 3)$  LOOs left unchanged, the positive map  $I\mathrm{Tr}\varrho -\varrho^{\sigma}$  is not completely positive.

In the following we shall demonstrate the detection power of these non-CP maps for some entangled states with PPT. This, on the other hand, proves that these maps are indecomposable non-CP positive maps. Let us introduce a state of  $d$ -level bipartite system as follows:

$$
\rho = \frac {a _ {1}}{d} | \Phi \rangle \langle \Phi | + \sum_ {k = 1, i = 2} ^ {d} \frac {a _ {i}}{d} \lambda_ {k} \otimes \lambda_ {k + i - 1}, \tag {16}
$$

where the positive numbers  $a_{i}$  satisfy  $\sum_{i}a_{i} = 1$ . In the case of  $d = 3$  and  $a_1 = 2 / 7$  the state has been discussed in [6,21]. It is not difficult to check that (i) If  $a_{i}\geq a_{1}(i\neq 1)$  the state is separable; (ii) If  $a_{i + 1}a_{d - i + 1}\geq a_1^2$  then the state is a PPT state. Here the conventions  $\lambda_{d + k} = \lambda_k$  and  $a_{d + k} = a_{k}$  have been used.

Let us consider  $d - 1$  cyclic permutations of the diagonal elements according to rules  $\sigma^l (m) = (m + l)$  mod  $d(l = 1,2,\ldots ,d - 1)$ . Applying these permutations to the first subsystem we obtain

$$
\rho^ {\sigma_ {A} ^ {l}} = \rho + \frac {1}{d} \sum_ {k, i = 1} ^ {d} \left(a _ {i - l} - a _ {i}\right) \lambda_ {k} \otimes \lambda_ {k + i - 1}. \tag {17}
$$

By applying the  $O$ -reduction criteria, i.e., if the state is

separable then  $\mathrm{Tr}_A\rho -\rho^{\sigma_A^l}\geq 0$ , we have to require  $1 - a_{i}\geq (d - 1)a_{1}$  for all  $i = 1,2,\ldots ,d$ . Now we consider a special case where  $a_{i} = a_{1}$  for  $i\neq 2,d$ . The constraints on the separable states from  $O$  reduction criterion become  $a_2\geq a_1$  and  $a_{d}\geq a_{1}$ . In this special case the  $O$  reduction criterion is a necessary and sufficient one for the separability. As a result we can picture the entanglement of the state in Eq. (16) according to its independent parameters  $a_1$  and  $a_2$  in a diagram, Fig. 1.

Hermitian correlation matrix. One dilemma of entanglement detection is that the entanglement can be detected only by non-CP maps, but non-CP maps are physically not realizable. Now we realize the  $O$ -reduction criterion by measuring the correlation of LOOs.

Let us take LOOs  $\{\lambda_{\mu}^{o}\}$  as testing observables for system  $A$  and LOOs  $\{\lambda_{\mu}^{T}\}$  as testing observables for system  $B$ . Their correlations behave differently for separable states and entangled states. For example the EW candidate  $E_{O}$  imposes a constraint on the correlations of LOOs in a separable state  $\rho$  as

$$
\sum_ {\mu = 1} ^ {d ^ {2}} \left\langle \lambda_ {\mu} ^ {o} \otimes \lambda_ {\mu} ^ {T} \right\rangle_ {\rho} \leq 1. \tag {18}
$$

If the inequality above is maximized over all possible orthogonal  $O$  we have  $\mathrm{Tr}\sqrt{TT^T} \leq 1$  where  $T$  is a  $d^2 \times d^2$  real correlation matrix with elements  $T_{\mu \nu} = \langle \lambda_\mu \otimes \lambda_\nu^T\rangle_\rho$ . This is equivalent to the realignment criterion for separability, as soon we notice that the realigned matrix  $\tilde{\rho}$  defined by  $\langle m,n|\tilde{\rho}|k,l\rangle = \langle m,k|\rho |n,l\rangle$  satisfies  $\tilde{\rho} = \sum_{\mu \nu}T_{\mu \nu}|\lambda_{\mu}\rangle \langle \lambda_{\nu}|$ . Therefore, the realignment criterion is reformulated in terms of the correlation function on the left-hand side of inequality equation (18).

The inequality equation (18) also holds true for the correlations of more general local observables  $\lambda_{\mu}^{o}$  where  $O$  satisfies  $OO^T \leq 1$ . However, if the inequality equation (18) for any orthogonal  $O$  fails to identify the entanglement of a state then the inequality equation (18) for any

![](images/27dc17702abd8faad7fd1748f0fd1e8078846be3e8eb8cd4bf2c5c22590e0be7.jpg)  
FIG. 1. The states in the region delineated by the curve  $a_2a_d \geq a_1^2$  have PPT, the states within the triangle inside the curve are separable, and the states outside the curve are free entangled with the states in the triangle outside the curve violating the reduction criterion. Therefore the states within the gray-colored region are bound entangled states.

nonorthogonal  $O$  fails too since  $|\mathrm{Tr}(TO)| \leq \mathrm{Tr}\sqrt{TT^T}$  as long as  $OO^T \leq 1$ .

There are limitations of inequality equation (18), e.g., there exist entangled states in  $2 \times 2$  systems that cannot be detected by the realignment criterion [4]. However, they can be detected by the  $O$ -reduction criterion because the latter includes the reduction criterion as a special case. In fact, the realignment criterion is absolutely weaker than the  $O$ -reduction criterion, as can be seen from the fact that

$$
\langle \Phi | \mathcal {O} \otimes I (\rho) | \Phi \rangle = 1 - \operatorname {T r} \left(T O ^ {T}\right), \quad \forall O. \tag {19}
$$

There exist cases in which  $|\mathrm{Tr}(TO)| \leq 1$  for all orthogonal  $O$ , but not all operators  $O \otimes I(\rho)$  are positive.

To achieve a physical detection of entanglement more efficient than Eq. (18), one has to examine the correlations of local observables more closely. In stead of a single function of correlation function as in the left-hand side of inequality equation (18), one can build a  $d \times d$  Hermitian correlation matrix  $X = \sum_{\mu} \operatorname{Tr}(X \lambda_{\mu}) \lambda_{\mu}$  for the correlations of LOOs  $\{\lambda_{\mu}^{o}\}$  and  $\{\lambda_{\nu}^{u} = u \lambda_{\nu} u^{\dagger}\}$  in state  $\rho$  as follows:

$$
\operatorname {T r} \left(X \lambda_ {m}\right) = \left\langle \left(I - \lambda_ {m} ^ {o}\right) \otimes \lambda_ {m} ^ {u} \right\rangle_ {\rho}, \tag {20a}
$$

$$
\operatorname {T r} \left(X \lambda_ {m n} ^ {+}\right) = \frac {- 1}{\sqrt {2}} \left\langle \lambda_ {m n} ^ {+ o} \otimes \lambda_ {m n} ^ {+ u} - \lambda_ {m n} ^ {- o} \otimes \lambda_ {m n} ^ {- u} \right\rangle_ {\rho}, \quad (2 0 b)
$$

$$
\operatorname {T r} \left(X \lambda_ {m n} ^ {-}\right) = \frac {- 1}{\sqrt {2}} \left\langle \lambda_ {m n} ^ {+ o} \otimes \lambda_ {m n} ^ {- u} + \lambda_ {m n} ^ {- o} \otimes \lambda_ {m n} ^ {+ u} \right\rangle_ {\rho}. \quad (2 0 c)
$$

Now we are able to present our main result:

Theorem.-If the state  $\rho$  is separable then the Hermitian correlation matrix is positive, i.e.,  $X\geq 0$ , for arbitrary unitary  $u$  and orthogonal  $O$ , which is equivalent to the  $O$ -reduction criterion  $\mathcal{O}\otimes I(\rho)\geq 0$  for all orthogonal  $O$ .

Proof. - It suffices to prove the second part of the theorem. We introduce another  $d$ -level system  $C$  as an ancilla and define an unnormalized state  $|\Phi \rangle_{ABC} = \sum_{m}|m,m,m\rangle$ , then we have the following relation between the Hermitian correlation matrix defined above and the  $O$ -reduction map

$$
X = \operatorname {T r} _ {A B} \left(\mathcal {O} ^ {T} \otimes \mathcal {U} (\rho) | \Phi \rangle \langle \Phi | _ {A B C}\right), \tag {21}
$$

where  $\mathcal{O}^T (\varrho) = I\mathrm{Tr}\varrho -\varrho^{o^T}$  and  $\mathcal{U}(\sigma) = u^{\dagger}\sigma u$  . It is obvious that if the  $o$  -reduction criterion is satisfied then  $X\geq 0$  . On the other hand,  $X\geq 0$  means that for any real  $s_m$  we have  $\sum_{mn}s_m s_n X_{mn}\geq 0$  . This ensures that  $\mathcal{O}\otimes I(\rho)$  is non-negative in any pure state that is related to  $\sum_{m}s_{m}|m,m\rangle$  by local unitary transformations, which in fact can be any pure state. Thus  $\mathcal{O}\otimes I(\rho)\geq 0$  if  $X\geq 0$  for all unitary  $u$  and orthogonal  $o$

Now let us look at two important special cases. First, the positivity of the Hermitian correlation matrix  $X \geq 0$  means that  $X$  is positive in any state, especially in the state  $\sum_{m} |m\rangle$ . As a result we obtain Eq. (18). Second, if  $d = 2$  then  $2 \times 2$  correlation matrix  $X \geq 0$  is equivalent to the inequality derived in [14]. That is,  $X \geq 0$  is a sufficient and necessary condition for the  $2 \times 2$  case.

Summary and discussion.-Through local orthogonal observables we have constructed effective entanglement

witnesses and non-CP maps for states with positive partial transposition. A family of bound entangled states can be well characterized by the non-CP maps induced by the permutation of local orthogonal observables. Finally, these physically not implementable maps can be realized physically by measuring the Hermitian correlation matrix, whose negative eigenvalue (if it exists) provides a signature of entanglement.

Our construction of the entanglement witnesses distinguishes itself in that it is based on the local uncertainty relationship among local orthogonal observables and is state independent, while previous constructions of entanglement witnesses, apart from few simple cases, always involve some extremization procedures and are state dependent. The detailed characterization of the entangled states that can be detected by our  $O$ -reduction criterion is still under investigation.

Y.S. acknowledges the financial support of National Natural Science Foundation of China (Grant No. 90303023). N.L. gratefully thanks P.T. Leung for his invaluable support and encouragement, and acknowledges the support of the State Education Ministry of China and the Chinese Academy of Sciences.

[1] R. F. Werner, Phys. Rev. A 40, 4277 (1989).  
[2] A. Peres, Phys. Rev. Lett. 77, 1413 (1996).  
[3] M. Horodecki, P. Horodecki, and R. Horodecki, Phys. Lett. A 223, 1 (1996).  
[4] K. Chen and L. A. Wu, Quantum Inf. Comput. 3, 193 (2003).  
[5] O. Rudolph, J. Phys. A 33, 3951 (2000).  
[6] A.C. Doherty, P.A. Parrilo, and F.M. Spedalieri, Phys. Rev. Lett. 88, 187904 (2002).  
[7] A.C. Doherty, P.A. Parrilo, and F.M. Spedalieri, Phys. Rev. A 69, 022308 (2004).  
[8] S.-J. Wu, X.-M. Chen, and Y.-D. Zhang, Phys. Lett. A 275, 244 (2000).  
[9] M. Horodecki, P. Horodecki, and R. Horodecki, Phys. Rev. Lett. 80, 5239 (1998).  
[10] M. Horodecki and P. Horodecki, Phys. Rev. A 59, 4206 (1999).  
[11] J.S. Bell, Speakable and Unspeakable in Quantum Mechanics (Cambridge University Press, Cambridge, England, 1987).  
[12] B.M. Terhal, Phys. Lett. A 271, 319 (2000).  
[13] S. Yu, Z.-B Chen, J.-W. Pan, and Y.-D Zhang, Phys. Rev. Lett. 90, 080401 (2003).  
[14] S. Yu, J.-W. Pan, Z.-B Chen, and Y.-D Zhang, Phys. Rev. Lett. 91, 217903 (2003).  
[15] H.F. Hofmann, Phys. Rev. A 68, 034307 (2003).  
[16] O. Gühne, Phys. Rev. Lett. 92, 117903 (2004).  
[17] P. Horodecki, Phys. Lett. A 232, 333 (1997).  
[18] A. Jamiołkowski, Rep. Math. Phys. 3, 275 (1972).  
[19] M. Lewenstein, B. Kraus, P. Horodecki, and J.I. Cirac, Phys. Rev. A 63, 044304 (2001).  
[20] K. Chen and L. A. Wu, Phys. Rev. A 69, 022312 (2004).  
[21] P. Horodecki, M. Horodecki, and R. Horodecki, Phys. Rev. Lett. 82, 1056 (1999).