# Entanglement of Pure States for a Single Copy

Guifre Vidal*

Departament d'Estructura i Constituents de la Materia, Universitat de Barcelona, Diagonal 647, E-08028 Barcelona, Spain (Received 25 March 1999)

An optimal local conversion strategy between any two pure states of a bipartite system is presented. It is optimal in that the probability of success is the largest achievable if the parties which share the system, and which can communicate classically, are only allowed to act locally on it. The study of optimal local conversions sheds some light on the entanglement of a single copy of a pure state. We propose a quantification of such an entanglement by means of a finite minimal set of new measures from which the optimal probability of conversion follows.

PACS numbers: 03.67.-a, 03.65.Bz

A proper quantification of entanglement is a priority in quantum information theory, for many of its applications [1] rely on quantum correlations as a necessary resource. Such a quantification of the nonlocal resources of a state should provide us with a detailed account of which tasks can be accomplished with it, or more specifically—since we are in the quantum kingdom—with the probability with which a given task can be accomplished.

Our work addresses the quantification of the entanglement of pure states shared by two parties. So far its complete quantification has been achieved only in a very specific limit, namely, when the parties share infinitely many identical copies of a given state [2,3]. On the other hand some authors [4-8] have initiated the study of the entanglement of a finite number of copies of pure states. This finite framework, which is the one involved in the realistic situations one encounters in a lab, will also be the objective of this work. The approach taken here relies on the study of optimal local transformations and of magnitudes that have a monotone behavior under any local manipulation of the system, which will be referred to as entanglement monotones [5]. We present a new set of such entanglement monotones and argue that they together quantify uniquely the entanglement of pure states in a physically relevant fashion.

Our starting question is the following: suppose that Alice and Bob share a pure entangled state  $\Psi$  and that they would like to convert it into another pure entangled state  $\Phi$ . Which is the greatest probability of success in such a conversion if the two parties, which are classically communicated, are only allowed to act on the system locally?

We present here the answer to this question [see Eq. (3)] [9], together with an explicit local strategy achieving the optimal probability. We also investigate, and refute, a possible ordering on the set of pure states induced by such probability. Finally some considerations regarding the nature of entanglement are made, and reversibility of optimal conversions, additivity of entanglement, and uniqueness of their measure are argued not to hold.

Let us start by considering the most general pure state of a bipartite system  $\Psi \in C^n\otimes C^n$  and its Schmidt decomposition

$$
\begin{array}{l} \left| \Psi \right\rangle = \sum_ {i = 1} ^ {n} \sqrt {\alpha_ {i}} \left| i _ {A} i _ {B} \right\rangle , \quad \alpha_ {i} \geq \alpha_ {i + 1} \geq 0, \\ \sum_ {i = 1} ^ {n} \alpha_ {i} = 1, \tag {1} \\ \end{array}
$$

where  $\{\sqrt{\alpha_i}\}$  are the Schmidt coefficients of  $\Psi$  and  $|i_A i_B\rangle$  stands for  $|i_A\rangle \otimes |i_B\rangle$ ,  $\{|i_A\rangle\}_{i=1}^n$  and  $\{|i_B\rangle\}_{i=1}^n$  being two local orthonormal bases depending on  $\Psi$ . Since Alice and Bob are allowed to perform local unitary transformations, and these are locally reversible, any two states with the same Schmidt coefficients are locally equivalent. Thus only the Schmidt coefficients are relevant as far as nonlocality is concerned, and we may study, without loss of generality, the optimal local conversion of  $\Psi$  into  $\Phi$  satisfying

$$
\begin{array}{l} | \Phi \rangle = \sum_ {i = 1} ^ {n} \sqrt {\beta_ {i}} | i _ {A} i _ {B} \rangle , \quad \beta_ {i} \geq \beta_ {i + 1} \geq 0, \\ \sum_ {i = 1} ^ {n} \beta_ {i} = 1. \tag {2} \\ \end{array}
$$

Theorem: Let us call  $P(\Psi \to \Phi)$  the maximal probability of obtaining the state  $\Phi$  from  $\Psi$  by means of any local strategy. Then, in terms of the Schmidt coefficients of  $\Psi$  and  $\Phi$ , we have

$$
P (\Psi \rightarrow \Phi) = \min  _ {l \in [ 1, n ]} \frac {\sum_ {i = l} ^ {n} \alpha_ {i}}{\sum_ {i = l} ^ {n} \beta_ {i}}. \tag {3}
$$

Before proving this result, let us note that for  $|\Phi \rangle = \sum_{i=1}^{m} \left( \frac{1}{\sqrt{m}} \right) |i_A i_B \rangle$  we recover the results obtained by Lo and Popescu in [4]. Our result is also a generalization of Nielsen's theorem [6], which provided the conditions for  $P(\Psi \to \Phi) = 1$ . Finally,  $E_{k=2}$  in Eq. (4) reduces, for the two-qubit case (that is,  $n = 2$ ), to the entanglement of single pair purification introduced by Bose, Vedral, and Knight in [7], conserved on average in a purification process via entanglement swapping.

Proof: Optimality of Eq. (3) will be proved by showing an explicit local strategy which converts  $\Psi$  into  $\Phi$  successfully with such probability, and by introducing a family of entanglement monotones, denoted by  $E_{k}(\rho)$ ,  $k = 1,\ldots ,n$ , and defined over the set of pure states as

$$
E _ {k} (\Psi) \equiv \sum_ {i = k} ^ {n} \alpha_ {i}, \tag {4}
$$

whose monotonicity sets the upper bound

$$
P (\Psi \rightarrow \Phi) \leq \min  _ {l \in [ 1, n ]} \frac {\sum_ {i = l} ^ {n} \alpha_ {i}}{\sum_ {i = l} ^ {n} \beta_ {i}} = \min  _ {l \in [ 1, n ]} \frac {E _ {l} (\Psi)}{E _ {l} (\Phi)}. \tag {5}
$$

Indeed, suppose that there is a local strategy with probability of success  $P'$  greater than this upper bound, and that the minimum in Eq. (5) is for  $l = l_{\star}$ . Before the conversion the amount of the monotone  $E_{l_{\star}}$  is  $E_{l_{\star}}(\Psi)$ , and after the conversion it would be, on average, at least—since we may be neglecting positive contributions coming from unsuccessful conversions— $P' E_{l_{\star}}(\Phi) > E_{l_{\star}}(\Psi)$ , which would mean an increase of this (nonincreasing) entanglement monotone, and would lead therefore to a contradiction.

That Eq. (4), together with the convex roof extension of  $E_{k}$  to mixed states,

$$
E _ {k} (\rho) \equiv \min  _ {\mathrm {Y} _ {\rho}} \sum_ {j} p _ {j} E _ {k} \left(\psi_ {j}\right) \tag {6}
$$

(here the minimization is to be performed over all the pure-state ensembles  $\Upsilon_{\rho} = \{p_j,\psi_j\}$  realizing  $\rho$ , i.e., such that  $\rho = \sum_{j}p_{j}|\psi_{j}\rangle \langle \psi_{j}|)$ , defines an entanglement monotone for each  $k$  follows from the fact that  $E_{k}(\Psi)$  can be written as

$$
E _ {k} (\Psi) = f _ {k} \left(\operatorname {T r} _ {A} | \Psi \rangle \langle \Psi |\right), \tag {7}
$$

where  $f_{k}(\sigma) \equiv \sum_{i=k}^{n} \alpha_{i}$  — that is the sum of the  $n - k + 1$  smallest eigenvalues of  $\sigma$  — is a unitarily invariant, concave function of  $\sigma$ , and from Theorem 2 in [5]. That  $f_{k}(\sigma)$  is a concave function follows from the "Ky Fan's maximum principle" [10]. Therefore what remains to be shown is that there is a local conversion strategy compatible with Eq. (3).

Notice, first, that Eq. (5) implies that if the number of nonzero Schmidt coefficients of  $\Psi$  is smaller than that of  $\Phi$ , then  $P(\Psi \rightarrow \Phi) = 0$ , as it is already well known [4]. Therefore we will assume from now on that  $\Psi$  has at least as many nonvanishing Schmidt coefficients as  $\Phi$ . We will also assume, for simplicity sake, that  $\alpha_{n} > 0$  (by lowering the dimension  $n$  of the original local Hilbert spaces if needed).

The optimal local conversion strategy we present here consists of two steps. In the first one the parties convert, with certainty, the initial state  $\Psi$  into a temporary pure state  $\Omega$ , by making use of a local strategy recently proposed by Nielsen [6]. In a second step  $\Omega$  is converted

into  $\Phi$  by means of a local measurement,  $P(\Psi \to \Phi)$  being the probability that this last conversion be successful.

Let us thus call  $l_{1}$  the smallest integer  $\in [1, n]$  such that

$$
\frac {\sum_ {i = l _ {1}} ^ {n} \alpha_ {i}}{\sum_ {i = l _ {1}} ^ {n} \beta_ {i}} = \min  _ {l \in [ 1, n ]} \frac {\sum_ {i = l} ^ {n} \alpha_ {i}}{\sum_ {i = l} ^ {n} \beta_ {i}} \equiv r _ {1} \quad (\leq 1). \tag {8}
$$

It may happen that  $l_{1} = r_{1} = 1$ . If not, it follows from the equivalence

$$
\frac {a}{b} <   \frac {a + c}{b + d} \Leftrightarrow \frac {a}{b} <   \frac {c}{d} (a, b, c, d > 0) \tag {9}
$$

that for any integer  $k \in [1, l_1 - 1]$

$$
\frac {\sum_ {i = k} ^ {l _ {1} - 1} \alpha_ {i}}{\sum_ {i = k} ^ {l _ {1} - 1} \beta_ {i}} > r _ {1}. \tag {10}
$$

Let us then define  $l_{2}$  as the smallest integer  $\in [1, l_{1} - 1]$  such that

$$
r _ {2} \equiv \frac {\sum_ {i = l _ {2}} ^ {l _ {1} - 1} \alpha_ {i}}{\sum_ {i = l _ {2}} ^ {l _ {1} - 1} \beta_ {i}} = \min  _ {l \in [ 1, l _ {1} - 1 ]} \frac {\sum_ {i = l} ^ {l _ {1} - 1} \alpha_ {i}}{\sum_ {i = l} ^ {l _ {1} - 1} \beta_ {i}} \quad (> r _ {1}). \tag {11}
$$

Repeating this process until  $l_{k} = 1$  for some  $k$ , we obtain a series of  $k + 1$  integers  $l_{0} > l_{1} > l_{2} > \dots > l_{k}$  ( $l_{0} \equiv n + 1$ ) and  $k$  positive real numbers  $0 < r_{1} < r_{2} < \dots < r_{k}$ , by means of which we define our temporary (normalized) state  $|\Omega\rangle = \sum_{i=1}^{n} \sqrt{\gamma_{i}} |i_{A}i_{B}\rangle$ , where

$$
\gamma_ {i} \equiv r _ {j} \beta_ {i} \quad \text {i f} i \in [ l _ {j}, l _ {j - 1} - 1 ], \tag {12}
$$

i.e.,

$$
\vec {\gamma} = \left[ \begin{array}{c} r _ {k} \left[ \begin{array}{c} \beta_ {l _ {k}} \\ \vdots \\ \beta_ {l _ {k - 1} - 1} \end{array} \right] \\ \vdots \\ r _ {2} \left[ \begin{array}{c} \beta_ {l _ {2}} \\ \vdots \\ \beta_ {l _ {1} - 1} \end{array} \right] \\ r _ {1} \left[ \begin{array}{c} \beta_ {l _ {1}} \\ \vdots \\ \beta_ {l _ {0} - 1} \end{array} \right] \end{array} \right]. \tag {13}
$$

Notice that by construction

$$
\sum_ {i = k} ^ {n} \alpha_ {i} \geq \sum_ {i = k} ^ {n} \gamma_ {i} \quad \forall k \in [ 1, n ] \tag {14}
$$

(or, equivalently,  $\sum_{i=1}^{k} \alpha_{i} \leq \sum_{i=1}^{k} \gamma_{i} \forall k \in [1, n]$ , that is to say,  $\vec{\alpha}$  is majorized by  $\vec{\gamma}$ ). Consequently Nielsen's local strategy shown in [6] can be applied in order for the parties to obtain the state  $\Omega$  from  $\Psi$  with certainty.

Let us consider now the positive operator  $\hat{M}: C^n \to C^n$

$$
\hat {M} \equiv \left[ \begin{array}{c c c c} \hat {M} _ {k} & & & \\ & \ddots & & \\ & & \hat {M} _ {2} & \\ & & & \hat {M} _ {1} \end{array} \right] = \hat {M} ^ {\dagger}, \tag {15}
$$

where

$$
\hat {M} _ {j} \equiv \sqrt {\frac {r _ {1}}{r _ {j}}} \hat {I} _ {[ l _ {j - 1} - l _ {j} ]}, \quad j = 1, \dots , k, \tag {16}
$$

is proportional to the identity in a  $(l_{j-1} - l_j)$ -dimensional subspace of  $C^n$ . It satisfies that  $0 \leq \hat{M} \leq I$ , so that together with  $\hat{N} \equiv \sqrt{1 - \hat{M}^2}$  it defines a generalized measurement of two outcomes  $(\hat{M}, \hat{N} \geq 0; \hat{M}^\dagger \hat{M} + \hat{N}^\dagger \hat{N} = \hat{I})$  that Alice (for instance) can perform locally. Since  $\hat{M} \otimes \hat{I}_B|\Omega\rangle = \sqrt{r_1}|\Phi\rangle$ , the whole local strategy allows one to obtain the pure state  $\Phi$  from  $\Psi$  with (optimal) probability  $P(\Psi \rightarrow \Phi) = r_1$ . Notice that  $\hat{N} \otimes \hat{I}_B|\Omega\rangle$  is an unnormalized, pure (often entangled) state with less nonvanishing coefficients than  $\Phi$ , so that, as expected, one cannot use it to obtain  $\Phi$ . This ends the proof of Eq. (3).

Notice that this strategy can be minimally implemented, for instance, with local measurements on Alice's side, one way classical communication (from Alice to Bob), and local unitary transformations on both sides, these three types of allowed operations being performed several times (the number of operations will depend on the two states, but is of order  $n$ ). Notice also that this strategy is not the simplest optimal one since optimal local conversion strategies must exist involving only one measurement on Alice's side, plus one transmission of classical bits from Alice to Bob, plus one locally unitary transformation on each side (see [4]).

Let us briefly consider an alternative scenario where Eq. (3) can be applied. Suppose that, as before, the parties start sharing the pure state  $\Psi$ , but that now their aim is to obtain (on average) the greatest number of copies of the state  $\Phi$ , say,  $m_{\Psi \rightarrow \Phi}^{\max}$ . In this case the optimal strategy involves, if possible, local conversions into several copies of  $\Phi$ , and this is not ruled in general by Eq. (3). However, there are circumstances in which  $m_{\Psi \rightarrow \Phi}^{\max} = P(\Psi \rightarrow \Phi)$ . Indeed, let  $n_{\psi}$  denote the number of nonvanishing Schmidt coefficients of the entangled state  $\psi$ , and recall that  $n_{\psi^{\otimes N}} = n_{\psi}^{N}$ . Then,

$$
n _ {\Psi} <   n _ {\Phi} ^ {2} \rightarrow P (\Psi \rightarrow \Phi^ {\otimes N}) = 0 \quad \forall N \geq 2 \tag {17}
$$

implies that the greatest number  $m_{\Psi \to \Phi}^{\max}$  of copies of  $\Phi$  the parties can obtain locally from  $\Psi$  is also given by  $P(\Psi \rightarrow \Phi)$  when  $n_{\Psi} < n_{\Phi}^{2}$ .

Let us move to consider now the following question: Is there any order in the space of entangled pure states that can be derived from Eq. (3)? In Ref. [6] a partial

order on the entangled pure states was obtained according to whether, given two states  $\Psi_{1}$  and  $\Psi_{2}$ , one of them can be converted locally into the other with certainty, say,  $\Psi_{1}$  into  $\Psi_{2}$ . If so,  $\Psi_{1}$  can be said to contain at least as much entanglement as  $\Psi_{2}$ , in the sense that any nonlocal resource that  $\Psi_{2}$  may contain, it is automatically contained, in at least the same amount, also in  $\Psi_{1}$ , and, again, the nonlocal resources needed to obtain  $\Psi_{1}$  suffice to create  $\Psi_{2}$ . But if on the contrary  $\Psi_{1}$  and  $\Psi_{2}$  are such that none of them can be converted into the other with certainty, then their entanglement is incommensurable according to this criteria. One might be tempted to extend such a partial order to the whole set of pure states by saying that the state  $\Psi_{1}$  is more entangled than  $\Psi_{2}$  if, and only if,  $P(\Psi_{1} \rightarrow \Psi_{2}) > P(\Psi_{2} \rightarrow \Psi_{1})$ . However, the following example shows that this order would be ill defined: consider three states  $\Psi_{k} \in C^{4} \otimes C^{4}$ , the square of the Schmidt coefficients of the  $k$ th state being  $\vec{\alpha}_{k}$ , where

$$
\begin{array}{l} \vec {\alpha} _ {k = 1} \equiv \frac {1}{1 4 4} (1 0 8, 1 2, 1 2, 1 2), \\ \vec {\alpha} _ {k = 2} \equiv \frac {1}{1 4 4} (6 6, 6 6, 6, 6), \\ \vec {\alpha} _ {k = 3} \equiv \frac {1}{1 4 4} (4 7, 4 7, 4 7, 3). \tag {18} \\ \end{array}
$$

Then such an ordering relation leads to the following contradiction:

$$
\Psi_ {1} <   \Psi_ {2} <   \Psi_ {3} <   \Psi_ {1}. \tag {19}
$$

Finally, we would like to analyze what conclusions can be drawn from Eq. (3) regarding the quantification of entanglement of a shared state, understood in relation to the nonlocal resources that characterize it. One can consider, e.g., both how many such nonlocal resources are needed to create the state and how many of them can be extracted from it, in terms of other shared states.

For pure states of a bipartite system the entropy of entanglement  $E(\Psi^{\otimes N})$  [2], and therefore one sole, and unique [11], parameter, quantifies asymptotically the nonlocal resources of a huge number  $N$  of copies of a given shared state  $\Psi$ . It turns out that in such a context optimal local conversions are reversible, and that entanglement behaves as an additive property of the quantum world.

We have considered in the present Letter the optimal local conversion of single copies of pure states, which falls far from the large- $N$  asymptotic case. This finite scenario is relevant in the light of the state of present technology, for it is not clear yet how to perform certain local transformations in the space of a large number of copies which are a necessary ingredient in the asymptotic conversions so far exposed [3]. But even if one knows how such local transformations can be performed in a lab, the finite scenario is important on its own, since

it describes the local resources involved in any local manipulation of a finite number of copies of pure states. Equation (3) teaches us the following qualitative facts about entanglement.

(1) Irreversibility: the optimal local conversion between any two states with nonidentical Schmidt coefficients is always an irreversible process. Here irreversible means that the parties cannot, with certainty, convert locally one state into another and then get the initial state back. This general result, which was proved in [5] and follows also from [6], does not hold asymptotically.

(2) More than one measure: the quantification of entanglement, in the sense exposed above, requires more than just one measure [5]. For pure states in  $C^n \otimes C^n$ , the  $n - 1$  entanglement monotones  $E_{k}(k = 2,\ldots ,n)$  are a minimal set of nonincreasing parameters providing a detailed and straightforward account of their nonlocal resources. They can be regarded as the measures of the entanglement of pure states in a similar sense as the entropy of entanglement is their measure in the asymptotic limit.

(3) Nonadditivity: the nonlocal resources of entangled states are not additive in general, in that, for instance, two parties can often extract more such resources from two copies of a given shared state  $\Psi$ , i.e., from  $\Psi \otimes \Psi$ , than twice what they can obtain from one single copy  $\Psi$  [12]. From this point of view it is artificial to take additivity as an a priori requirement for any good measure of entanglement [5]. Thus additivity of the entanglement of pure states in the asymptotic limit is a remarkable result, rather than an a priori constraint, which follows from the additivity of the entropy of entanglement and from the existence of reversible asymptotic conversions (as the ones in [3]).

Summarizing, given two pure shared states  $\Psi$  and  $\Phi$ , the highest probability  $P(\Psi \rightarrow \Phi)$  of success in the conversion of  $\Psi$  into  $\Phi$  by means of any local strategy can be used to quantify their entanglement. We have shown that for pure states of a bipartite system the entanglement monotones  $E_{k}$  provide  $P(\Psi \rightarrow \Phi)$ , since this probability is the greatest one compatible with the monotonicity of  $E_{k}$ . The explicit expression for  $P(\Psi \rightarrow \Phi)$  shows that the entanglement of a pure state  $\Psi$  behaves essentially differently from that of  $\Psi^{\otimes N}$  for very large  $N$ .

There are many open problems regarding finite entanglement. It would be interesting to derive equivalent results for pure states shared by three or more parties, and, also, to extend the results presented here to mixed states [13]. A way to proceed is by studying concrete local

conversion strategies, which mean lower bounds on the optimal probability of success in the conversion, and by identifying new entanglement monotones, since each one implies an upper bound. In this scheme it becomes reasonable to demand, as an a priori requirement, only monotonicity under local manipulations in order for a magnitude to be a candidate for a measure of entanglement.

The author is most grateful to Rolf Tarrach for his thorough reading of the manuscript, comments, and suggestions. Comments are also acknowledged to Maciej Lewenstein. The author thanks Maciej Lewenstein, Anna Sanpera, and Christel Franko for their hospitality in Hannover. Financial support from CIRYT, Contract No. AEN98-0431, CIRIT, Contract No. 1998SGR00026, and CIRIT, Grant No. 1997FI-00068 PG, are also acknowledged.

*Email address: guifre@ecm.ub.es  
[1] See, for instance, Phys. World March (1998).  
[2] CH. Bennett, D.P. DiVincenzo, J.A. Smolin, and W.K. Wootters, Phys. Rev. A 54, 3824 (1996).  
[3] CH. Bennett, H. J. Bernstein, S. Popescu, and B. Schumacher, Phys. Rev. A 53, 2046 (1996).  
[4] H.-K. Lo and S. Popescu, quant-ph/9707038.  
[5] G. Vidal, quant-ph/9807077 [J. Mod. Opt. (to be published)].  
[6] M. A. Nielsen, Phys. Rev. Lett. 83, 436 (1999).  
[7] S. Bose, V. Vedral, and P. L. Knight, quant-ph/9812013.  
[8] D. Jonathan and M. Plenio, quantum-ph/9903054 [Phys. Rev. Lett. (to be published)].  
[9] Notice that in Ref. [4] the same question was already answered when the final state is of the form  $|\Phi \rangle = \sum_{i=1}^{m} (1 / \sqrt{m}) |i_A i_B \rangle$  for any  $m$ .  
[10] See, for instance, R. Bhatia, Matrix Analysis (Springer-Verlag, New York, 1997), p. 24.  
[11] S. Popescu and D. Rohrlich, Phys. Rev. A 56, R3319 (1997).  
[12] Take, as a concrete example,  $|\Psi \rangle = (1 / \sqrt{2})(|1_A1_B\rangle + |2_A2_B\rangle)$  and  $|\Phi \rangle = (1 / \sqrt{3})(|1_A1_B\rangle + |2_A2_B\rangle + |3_A3_B\rangle)$ . Then, for instance,  $1 = P(\Psi \otimes \Psi \to \Phi) > 2P(\Psi \to \Phi) = 0$ .  
[13] In the particular case of a two-qubit system  $(C^2\otimes C^2)$ , a closed expression for the optimal probability of locally converting any pure state  $\Psi$  into any mixed state  $\rho$  has been obtained. It reads  $P(\Psi \rightarrow \rho) = \min \left(\frac{E_2(\Psi)}{E_2(\rho)},1\right)$ , where  $E_{2}(\rho)$  is an explicit expression of  $\rho$ . This result, together with an optimal local strategy for such a conversion, will be presented somewhere else.