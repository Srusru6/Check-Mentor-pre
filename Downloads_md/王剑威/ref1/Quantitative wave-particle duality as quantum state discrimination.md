# Quantitative wave-particle duality as quantum state discrimination

Xin Lu

School of Physics and Electrical Engineering, Liupanshui Normal University, Minghu Lu, Liupanshui 553004, Guizhou, China

![](images/1c52e67af8e64f6cda44f4d172c4374aabcbd376354cb226a4c15c6e4b475db8.jpg)

(Received 5 August 2019; accepted 20 July 2020; published 4 August 2020)

We consider the problem of quantitative wave-particle duality from the perspective of quantum state discrimination. Specifically, we obtain quantifiers of both the particle aspect and the wave aspect from state discrimination. We show that the familiar one-bet duality relation coincides with the relation obtained from considerations of ambiguous discrimination, and the quantifiers suggested by unambiguous discrimination provide us with additional duality relations. In contrast to earlier similar works, the path asymmetry of the interferometer provides the ensemble to be discriminated, and therefore there is no need to introduce which-path detectors.

DOI: 10.1103/PhysRevA.102.022201

# I. INTRODUCTION

Wave-particle duality, or the more general Bohr's principle of complementarity [1], is one of the most fundamental facts in quantum mechanics. The effort of quantifying it was started by Wootters and Zurek in 1979 [2], which was further developed by many other authors [3-20]. Notably, Jaeger et al. [4] and Englert [5] proposed the following duality relation,

$$
P ^ {2} + V ^ {2} \leqslant 1, \tag {1}
$$

where  $P$  is the predictability that measures the particle aspect, while  $V$  is the visibility that measures the wave aspect. Relation (1) is now the standard quantitative statement of wave-particle duality in two-path interferometers. In practice, it is possible to obtain more path information by employing a which-path detector, i.e., entangling the quantum state with an ancillary quantum degree of freedom (e.g., by polarizing the light in each path with different polarizations) and performing measurements on that ancillary degree of freedom (e.g., measuring the polarization). An important property of the duality relation (1) is that such use of which-path detectors will not enlarge the upper bound. A detailed discussion in this direction is provided by Englert and Bergou [6]. Consequently, relation (1) quantifies the limit of simultaneous obtainable information of the particle and wave aspects.

In the general case of  $n$ -path interferometers, Durr first derived a similar relation [7]. Besides Durr's work, there were also other efforts. For example, Englert et al. [11] proposed several proper duality measures in  $n$ -path interferometers from different perspectives. Unlike in two-path interferometers, there are various widely accepted wave-particle duality relations in the case of  $n$  paths, such as the Durr's relation [7], the one-bet relation [3,4,11], and the entropic relation [2,11]. The essential difficulty of quantifying wave-particle duality is to find proper quantifiers of the wave aspect and the particle aspect. Durr and Englert et al. have proposed similar criteria for a proper quantifier separately in Refs. [7,11], which mainly consist of the following three points: Normalization,

convexity, and invariant under relabeling. The objective of this paper is to generate proper quantifiers of wave-particle duality systematically from the perspective of quantum state discrimination (see, for example, Refs. [21-25] for an overview on this topic).

The possible link between wave-particle duality and quantum state discrimination has already been noticed by some authors recently [16,18-20,26]. For example, Bera et al. [16] quantify the particle aspect using unambiguous discrimination on the which-path detector degree of freedom, and therefore establish the duality between path distinguishability and coherence. In contrast to the previous widely accepted results [7,11], these recent works fail to be intrinsic, i.e., instead of considering the quantum state of the interferometer system itself, the which-path detector degree of freedom has to be involved in order to introduce state discrimination. Moreover, the quantum state is restricted to the special form  $\sum \sqrt{p_i|i\rangle} |\eta_i\rangle$  in their discussion. In this paper, by introducing the path permutation matrix  $X$ , the problem is considered intrinsically and generally. In particular, we show that both the particle aspect and wave aspect can be quantified via state discrimination, and the criteria mentioned in Refs. [7,11] are automatically satisfied by the construction. We consider both ambiguous discrimination and unambiguous discrimination, and show that the quantifiers in the one-bet measure [3,4,11] are exactly the quantifiers obtained from ambiguous discrimination. In this way, we provide the familiar one-bet wave-particle duality measure an operation meaning from the perspective of state discrimination, and therefore justify our claim that state discrimination can be applied to the problem of quantitative wave-particle duality in a more intrinsic way. The consideration of unambiguous discrimination also returns additional valid duality relations. In conclusion, our results show that the wave-particle duality, or the more general complementarity properties, can be quantified based on state discrimination in a more general fashion than in earlier works.

We briefly describe the general problem of quantitative wave-particle duality and list explicitly the criteria of proper

quantifiers in Sec. II. Then, by introducing the path permutation matrix  $X$ , the explicit form of the quantum states to be discriminated is given in Sec. III. We also show in this section that such discrimination will produce proper quantifiers automatically. The corresponding duality relations are discussed in Sec. IV. The paper is closed with a summary.

# II. QUANTITATIVE WAVE-PARTICLE DUALITY

We consider a general  $n$ -path interferometer, and set the particle mode basis  $\{|k\rangle ,k = 0,\dots ,n - 1\}$  as the computational basis, such that the ket  $|k\rangle$  is the state when the particle takes the  $k$ th path. The density matrix  $\rho$  of the quantum state in consideration is expressed in this basis, so that only its diagonal entries are relevant for path information. In general, one defines the predictability [3-5,7,11], which quantifies the particle aspect, as a continuous function  $P$  of the diagonal entries of  $\rho$ . Physical considerations require that the function  $P$  should satisfy [7,11] the following:

(1)  $P = 1 \iff \rho_{jj} = 1$  for one  $j$ , which implies that the path is certain;  
(2)  $P = 0 \Longleftrightarrow \rho_{jj} = 1 / n$  for all  $j$ , which implies that the path is completely uncertain;  
(3)  $P$  is invariant under relabeling of the  $n$  paths;  
(4)  $P$  is convex.

We note that the convexity condition ensures that any application of which-path detectors cannot decrease the path information obtained. Rigorously, the above conditions are weaker than those proposed in Ref. [7], which requires that any change toward equalization of the diagonal entries of  $\rho$  should decrease  $P$ . The conditions here only imply that such a change cannot increase  $P$ .

The wave aspect is quantified using the off-diagonal entries of  $\rho$ , and the corresponding continuous function visibility  $V$  should similarly satisfy the following [7,11]:

(1)  $V = 1 \iff \rho = \sum_{j,k} |j\rangle \langle k|e^{i(\theta_j - \theta_k)} / n,$  or equivalently, the state is pure and with equal diagonal entries;  
(2)  $V = 0 \iff \rho_{jk} = 0$  for any  $j \neq k$ ;  
(3)  $V$  is invariant under relabeling of the  $n$  paths;  
(4)  $V$  is convex.

For example, in the well-known duality relation (1) for two-path interferometry, the predictability is defined as [3-5]

$$
P = \left| \rho_ {0 0} - \rho_ {1 1} \right|, \tag {2}
$$

and the visibility is defined as [3-5]

$$
V = 2 \left| \rho_ {0 1} \right|. \tag {3}
$$

The listed criteria are readily verified. We also note that these two quantifiers have a clear physical significance:  $P$  corresponds to the probability of guessing the path correctly, while  $V$  corresponds to interference strength.

One way to generalize the above quantification to higher dimensions is the so-called one-bet measure [3,4,11], where the two quantifiers are defined as

$$
P _ {\text {b e t}} = \frac {n \max  _ {j} \rho_ {j j} - 1}{n - 1}, \tag {4}
$$

so that  $P_{\mathrm{bet}}$  depends only on the greatest diagonal entry, and

$$
V _ {\text {b e t}} = \frac {1}{n - 1} \sum_ {j} \sum_ {k \neq j} | \rho_ {j k} |, \tag {5}
$$

so that  $V_{\mathrm{bet}}$  is proportional to the  $l_{1}$ -norm of coherence [27]

$$
c _ {l _ {1}} (\rho) = \sum_ {j} \sum_ {k \neq j} | \rho_ {j k} |. \tag {6}
$$

The positivity of density matrices implies that

$$
P _ {\text {b e t}} ^ {2} + V _ {\text {b e t}} ^ {2} \leqslant 1, \tag {7}
$$

or the one-bet duality relation in general  $n$ -path interferometers. When  $n = 2$ , the one-bet relation reduces to the standard relation (1); when  $n > 2$ , we note that the one-bet relation is not tight, i.e., except at the extreme points  $P_{\mathrm{bet}} = 1$  or  $V_{\mathrm{bet}} = 1$ , the upper bound one in (7) is not saturated. It is possible to establish tighter duality relations by adjusting the one-bet measure [18]. As its name suggests, the quantifiers in one-bet measure are derived from betting strategies. In the following, we will give this measure a completely different operational meaning.

# III. PATH DISCRIMINATION AND PHASE DISCRIMINATION

After briefly describing the problem of quantitative wave-particle duality, we move on to the topic of quantum state discrimination. As claimed in the Introduction, we would like to obtain proper quantifiers, i.e., the predictability  $P$  and the visibility  $V$  from considerations of state discrimination. Unlike similar works [16,18], state discrimination is not introduced by which-path detectors, instead, we analyze the intrinsic path asymmetry of the interferometer by introducing the following permutation matrix,

$$
X = \sum_ {j = 0} ^ {n - 1} | j \oplus 1 \rangle \langle j |, \tag {8}
$$

with  $\oplus$  denoting summation modulo  $n$ . In the following, we will show that the predictability can be derived from discrimination of the following ensemble,

$$
\left\{\rho_ {j} = X ^ {j} \rho_ {\mathrm {d i a g}} X ^ {- j}, 1 / n \right\} _ {j = 0} ^ {n - 1}, \tag {9}
$$

where  $\rho_{\mathrm{diag}}$  is the diagonal matrix with the same diagonal entries as  $\rho$ , and each permuted state  $\rho_{j}$  has equal weight  $1 / n$  in the ensemble. Note that  $\rho_{j} = \rho_{k}$  for any indices  $j$  and  $k$  if and only if all the diagonal entries of  $\rho$  are  $1 / n$ , which implies total symmetry of the paths, or the path is totally uncertain.

The two most common discrimination strategies, ambiguous discrimination (also called minimum-error discrimination) and unambiguous discrimination, are considered. Ambiguous state discrimination of a given ensemble  $\{\rho_j,p_j\}_{j = 0}^{n - 1}$ , where  $p_j$  is the weight of the corresponding state  $\rho_{j}$ , is to maximize the average success probability

$$
p _ {s} = \sum_ {j = 0} ^ {n - 1} p _ {j} \operatorname {T r} \left(M _ {j} \rho_ {j}\right), \tag {10}
$$

by finding the optimal positive-operator-valued measurement (POVM)  $\{M_j\}_{j = 0}^{n - 1}$  with  $n$  outcomes. On the other hand,

unambiguous state discrimination of a given ensemble  $\{\rho_j, p_j\}_{j=0}^{n-1}$  is to find the optimal POVM  $\{M_j\}_{j=0}^n$  with  $n+1$  outcomes such that the probability  $p_f$  (the failure probability) of inconclusive discrimination,

$$
p _ {f} = \sum_ {j = 0} ^ {n - 1} p _ {j} \operatorname {T r} \left(M _ {n} \rho_ {j}\right), \tag {11}
$$

is minimized under the unambiguous condition

$$
\operatorname {T r} \left(M _ {j} \rho_ {k}\right) = \delta_ {j k} \operatorname {T r} \left(M _ {k} \rho_ {k}\right), \quad \forall j, k = 0, \dots , n - 1. \tag {12}
$$

Practically, the above condition (12) requires that the discrimination is conclusive whenever  $j \neq n$ , i.e., when the  $j$ th measurement outcome happens with  $j \neq n$ , it is certain that the state is  $\rho_{j}$ . Unlike ambiguous discrimination, where the success probability  $p_{s}$  is at least  $1 / n$ , the failure probability  $p_{f}$  can reach one, which suggests that such unambiguous discrimination is impossible. For discrimination of the ensemble (9), we would like to use either  $p_{s}$  in (10) or  $1 - p_{f}$  in (11) as the definition of the predictability, and therefore obtain a quantifier of the particle aspect from ambiguous discrimination or unambiguous discrimination, respectively. To do so, we need to check that the criteria listed in Sec. II are fulfilled.

For ambiguous discrimination, since  $p_s \in [1/n, 1]$ , a normalization is required to ensure  $P_{\mathrm{asd}} \in [0, 1]$

$$
P _ {\mathrm {a s d}} = \frac {n p _ {s} - 1}{n - 1}, \tag {13}
$$

so that  $p_s = 1 / n$  corresponds to  $P = 0$ . Since the weights in (9) are all  $1 / n$ , the invariance property is clearly satisfied. Finally, by the definition of the success probability in (10),

$$
\max  _ {\left\{M _ {j} \right\}} \sum_ {j = 0} ^ {n - 1} \operatorname {T r} \left(M _ {j} \sum_ {k} w _ {k} \rho_ {k j}\right) \leqslant \sum_ {k} w _ {k} \max  _ {\left\{M _ {k j} \right\}} \sum_ {j = 0} ^ {n - 1} \operatorname {T r} \left(M _ {k j} \rho_ {k j}\right),
$$

so that the convexity is automatically satisfied.

In the case of unambiguous discrimination, the only difference is that the failure probability  $p_f \in [0, 1]$  and therefore no normalization is necessary. One can directly define

$$
P _ {\mathrm {u s d}} = 1 - p _ {f}. \tag {14}
$$

The convexity also follows straightforward from the definition (11) of  $p_f$ . In conclusion, discrimination of the ensemble (9) provides us proper quantifiers of the particle aspect.

Similarly as in Ref. [11], we switch to the wave mode by considering Hadamard transformations. Specifically, the  $k$ th vector in the wave mode basis is

$$
| \tilde {k} \rangle = \frac {1}{\sqrt {n}} \sum_ {j} | j \rangle e ^ {i \theta_ {j k}}, \tag {15}
$$

so that the transform matrix

$$
H = \frac {1}{\sqrt {n}} \sum_ {j, k} | j \rangle e ^ {i \theta_ {j k}} \langle k | \tag {16}
$$

is a Hadamard. The above procedure for matrix  $\rho$  is repeated for the transformed matrix  $H\rho H^{\dagger}$  to obtain the ensemble

$$
\{\tilde {\rho} _ {j} = X ^ {j} \left(H \rho H ^ {\dagger}\right) _ {\text {d i a g}} X ^ {- j}, 1 / n \} _ {H} \tag {17}
$$

for discrimination. The subscript  $H$  in (17) is to show the dependence of the ensemble on the Hadamard matrix  $H$ . Explicitly, for the Hadamard matrix in (16), the  $j$ th diagonal entry of  $\tilde{\rho}$  is

$$
\tilde {\rho} _ {j j} = \frac {1}{n} \left(1 + \sum_ {k \neq l} | \rho_ {k l} | \cos \left(\theta_ {j k} - \theta_ {j l} + \arg \rho_ {k l}\right)\right). \tag {18}
$$

As a consequence, a maximization over all  $n$ -dimensional Hadamard matrices is necessary to obtain a unique discrimination result. We remark that  $\tilde{\rho}_j = \tilde{\rho}_k$  for any indices  $j$  and  $k$  if a single diagonal entry of  $\rho$  is one, which is the situation where complete path information is known.

By the same argument before, we conclude that the visibility can be quantified by the success probability  $\tilde{p}_s^{(H)}$  of ambiguous discrimination of the ensemble (17) as

$$
V _ {\mathrm {a s d}} = \max  _ {H} \frac {n \tilde {p} _ {s} ^ {(H)} - 1}{n - 1}, \tag {19}
$$

or by the failure probability  $\tilde{p}_f^{(H)}$  of unambiguous discrimination of the same ensemble,

$$
V _ {\mathrm {u s d}} = \max  _ {H} 1 - \tilde {p} _ {f} ^ {(H)}. \tag {20}
$$

Therefore we treat the particle mode and the wave mode on equal footing, which not only simplifies the calculation, but also emphasizes the complementary relation between them.

# IV. WAVE-PARTICLE DUALITY RELATIONS

We present the wave-particle duality relations expressed by the quantifiers obtained in the last section. First, we analytically solve the problem of ambiguous discrimination and recover the one-bet relation. Then, we give two additional duality relations from considerations of unambiguous discrimination, and discuss the relation between our relation with the duality proposed by Bera et al. [16].

# A. Ambiguous discrimination

Due to the simple form of  $\rho_{j}$  defined in (9), the problem of ambiguous discrimination for the ensemble  $\{\rho_j,1 / n\}$  can be analytically solved. Indeed, since the state  $\rho_{j}$  is diagonal for any index  $j$  , we need only analyze diagonal POVM  $\{M_j\}$  .Let

$$
M _ {j} = \sum_ {k} m _ {j k} | k \rangle \langle k |, \tag {21}
$$

because  $p_j = 1/n$  for any index  $j$ , and  $\sum_{j,k} m_{jk} = n$  by the requirement of POVM, we obtain

$$
p _ {s} = \frac {1}{n} \sum_ {j, k} m _ {j k} \rho_ {k \ominus j, k \ominus j} \leqslant \max  _ {k} \rho_ {k k}. \tag {22}
$$

Without loss of generality, we may assume  $\max_k\rho_{kk} = \rho_{00}$  (our indices always start at zero), i.e., the first path is the most probable one, then the POVM that attains this maximum can be constructed as  $\{M_j = |j\rangle \langle j|\}$ .

Likewise we calculate the success probability for the phase discrimination  $\{\tilde{\rho}_j, 1/n\}_H$ . Using (18), we obtain

$$
\tilde {p} _ {s} \leqslant \max  _ {H, k} \left(H \rho H ^ {\dagger}\right) _ {k k} \leqslant \frac {1}{n} \left[ 1 + c _ {l _ {1}} (\rho) \right], \tag {23}
$$

where  $c_{l_1}(\rho)$  is the  $l_{1}$ -norm of coherence [27],

$$
c _ {l _ {1}} (\rho) = \sum_ {j = 0} ^ {n - 1} \sum_ {k \neq j} | \rho_ {j k} |. \tag {24}
$$

As a result, the corresponding quantifiers are

$$
P _ {\mathrm {a s d}} = \frac {n \max  _ {j} \rho_ {j j} - 1}{n - 1}, \tag {25}
$$

$$
V _ {\mathrm {a s d}} = \frac {1}{n - 1} \sum_ {j} \sum_ {k \neq j} | \rho_ {j k} |. \tag {26}
$$

We thus recover the quantifiers in the one-bet measure as promised, and the duality relation thus obtained is merely the familiar one-bet relation. Note that instead of considering the problem as a betting strategy, the duality relation (7) is now given a clear operational meaning in terms of ambiguous state discrimination.

# B. Unambiguous discrimination

The problem of unambiguous discrimination is more involved, and we are unable to find the analytical solution despite the simple form of (9). Nevertheless, there exist several lower bounds of the failure probability  $p_f$  that still provide us duality relations. For example, we employ the lower bound established by Feng et al. [28] in terms of the fidelity  $F$  [29,30],

$$
p _ {f} \geqslant \left(\frac {n}{n - 1} \sum_ {j} \sum_ {k \neq j} p _ {j} p _ {k} F \left(\rho_ {j}, \rho_ {k}\right)\right) ^ {\frac {1}{2}}, \tag {27}
$$

where the fidelity is defined as

$$
F \left(\rho_ {j}, \rho_ {k}\right) = \left[ \operatorname {T r} \left(\sqrt {\sqrt {\rho_ {j}} \rho_ {k} \sqrt {\rho_ {j}}}\right) \right] ^ {2}, \tag {28}
$$

so it is the square of the fidelity defined in Ref. [31]. For our ensemble  $\{\rho_j, 1/n\}$ , this bound implies that

$$
\begin{array}{l} p _ {f} ^ {2} \geqslant \frac {1}{n (n - 1)} \sum_ {j} \sum_ {k \neq j} \left(\sum_ {l} \sqrt {\rho_ {l \oplus j , l \oplus j} \rho_ {l \oplus k , l \oplus k}}\right) ^ {2} \\ = \frac {1}{n - 1} \sum_ {k \neq 0} \left(\sum_ {l} \sqrt {\rho_ {l l} \rho_ {k \oplus l , k \oplus l}}\right) ^ {2} \\ \geqslant \frac {1}{(n - 1) ^ {2}} \left(\sum_ {k \neq 0} \sum_ {l} \sqrt {\rho_ {l l} \rho_ {k \oplus l , k \oplus l}}\right) ^ {2} \\ = \frac {1}{(n - 1) ^ {2}} \left[ \left(\sum_ {j} \sqrt {\rho_ {j j}}\right) ^ {2} - 1 \right] ^ {2}, \\ \end{array}
$$

where the Cauchy-Schwartz inequality is applied in the third line. As a result, the predictability  $P_{\mathrm{usd}}$ , which is  $1 - p_f$ , is bounded above by

$$
P _ {\mathrm {u s d}} \leqslant \frac {n}{n - 1} - \frac {1}{n - 1} \left(\sum_ {j} \sqrt {\rho_ {j j}}\right) ^ {2}. \tag {29}
$$

A direct calculation of the upper bound for the visibility  $V_{\mathrm{usd}}$  is much more tedious, so we instead try to link  $V_{\mathrm{usd}}$  with  $V_{\mathrm{asd}}$ . Let  $\{M_j\}_{j=0}^n$  be the optimal measurement satisfying the unambiguous condition (12), then  $\{M_j + M_n / n\}_{j=0}^{n-1}$  is a measurement with  $n$  outcomes, and by the definition of  $p_s$ ,

$$
\begin{array}{l} p _ {s} \geqslant \sum_ {j = 0} ^ {n - 1} p _ {j} \operatorname {T r} [ (M _ {j} + M _ {n} / n) \rho_ {j} ] \\ = \operatorname {T r} \left(\sum_ {j = 0} ^ {n - 1} M _ {j} \sum_ {k = 0} ^ {n - 1} p _ {k} \rho_ {k}\right) + p _ {f} / n \\ = \operatorname {T r} \left[ \left(\mathbb {1} - M _ {n}\right) \sum_ {k = 0} ^ {n - 1} p _ {k} \rho_ {k} \right] + p _ {f} / n \\ = 1 - \frac {n - 1}{n} p _ {f}, \\ \end{array}
$$

where the equality in the second line is due to the unambiguous condition (12) and the third line is by the requirement of a POVM. As a result,

$$
V _ {\mathrm {a s d}} = \frac {n p _ {s} - 1}{n - 1} \geqslant 1 - p _ {f} = V _ {\mathrm {u s d}}, \tag {30}
$$

so by (26),  $V_{\mathrm{usd}}$  is bounded above by

$$
V _ {\mathrm {u s d}} \leqslant \frac {1}{n - 1} \sum_ {j} \sum_ {k \neq j} | \rho_ {j k} |. \tag {31}
$$

Putting (29) and (31) together, the positivity of the density matrix  $\rho$  implies immediately that

$$
P _ {\mathrm {u s d}} + V _ {\mathrm {u s d}} \leqslant 1, \tag {32}
$$

and consequently, although the exact forms of  $P_{\mathrm{usd}}$  and  $V_{\mathrm{usd}}$  are unknown for general states, their sum is guaranteed to be less than or equal to one, which may be considered as a wave-particle duality relation.

However, the implicit form of  $P_{\mathrm{usd}}$  and  $V_{\mathrm{usd}}$  makes the corresponding duality relation not as useful as the one obtained from ambiguous discrimination, i.e., the one-bet relation. On the other hand, it is clear that the respective upper bounds in (29) and (31) satisfy all the requirements for the proper quantifiers described in Sec. II, and therefore by setting

$$
P _ {\text {b u r}} = \frac {n}{n - 1} - \frac {1}{n - 1} \left(\sum_ {j} \sqrt {\rho_ {j j}}\right) ^ {2}, \tag {33}
$$

$$
V _ {\mathrm {a s d}} = \frac {1}{n - 1} \sum_ {j} \sum_ {k \neq j} | \rho_ {j k} |, \tag {34}
$$

we obtain an additional explicit duality relation

$$
P _ {\text {b u r}} + V _ {\text {a s d}} \leqslant 1. \tag {35}
$$

The visibility function  $V$  in (34) is proportional to the  $l_{1}$ -norm of coherence and thus has a clear physical significance. One can also associate the predictability  $P$  in (33) a clear physical meaning by expressing it via the average squared Bures distance [32,33] [since all the matrices  $\{\rho_j\}$  in (9) are diagonal, it is equivalent to the average squared Hellinger distance, which measures the similarity between two probability

distributions] as

$$
P _ {\text {b u r}} (\rho) = \frac {1}{2 n (n - 1)} \sum_ {j} \sum_ {k \neq j} D _ {B} ^ {2} \left(\rho_ {j}, \rho_ {k}\right), \tag {36}
$$

where, by definition,  $D_B^2 (\rho_j,\rho_k) = 2 - 2\sqrt{F(\rho_j,\rho_k)}$ . In conclusion, the predictability  $P_{\mathrm{bur}}$  (33) corresponds to the average squared Bures distance of the permuted states  $\rho_{j}$ , which is a reasonable measure of the asymmetry of the paths.

We remark that the relation (35) has already been hinted at in Refs. [16,19]. Instead of our abstract approach, they concentrated on the special state  $|\Phi \rangle = \sum_{i} |i\rangle \otimes |d_{i}\rangle_{\mathrm{w}}\lambda_{i}$ , where the subscript w denotes the which-path detector degree of freedom. The corresponding  $\rho$  in our consideration is obtained by taking the partial trace over the which-path detector degree of freedom. Explicitly,

$$
\rho = \operatorname {T r} _ {\mathrm {w}} | \Phi \rangle \langle \Phi | = \sum_ {i, j} | i \rangle \langle j | \langle d _ {j} | d _ {i} \rangle_ {\mathrm {w}} \lambda_ {i} \lambda_ {j}. \tag {37}
$$

They define path distinguishability by considering unambiguous discrimination of the  $n$  pure states  $\{|d_i\rangle_{\mathrm{w}},|\lambda_i|^2\}$  in the which-path detector degree of freedom. To achieve that, they employ an upper bound for unambiguous discrimination given in Ref. [34], which is a weaker form of our bound [28]. Although the physical picture is clear, their work does not fit into the established framework of the quantitative wave-particle duality, where the distinguishability  $D$  is defined after the predictability  $P$ . Specifically, as discussed in Ref. [6], performing a measurement  $\{\Pi_i\}$  on the which-path detector amounts to a sorting of the state  $\rho$  in (37) into subensembles  $\{\rho^{(i)},w_i\}$  such that

$$
\rho = \sum_ {i} w _ {i} \rho^ {(i)}, \tag {38}
$$

where  $w_{i}$  is the probability of the  $i$ th measurement outcome on the which-path detector. Then the distinguishability  $D$  is defined to be the maximal possible average predictability of the subsembles as

$$
D _ {\text {b u r}} (\rho) = \max  _ {\{\Pi_ {i} \}} \sum_ {i} w _ {i} P _ {\text {b u r}} \left(\rho^ {(i)}\right). \tag {39}
$$

Let us consider the optimal measurement  $\{M_j\}_{j=0}^n$  of unambiguous discrimination, then the unambiguous condition implies that

$$
P _ {\text {b u r}} (\rho^ {(j)}) = 1 \quad \text {f o r a n y} j \neq n. \tag {40}
$$

As a result,

$$
D _ {\text {b u r}} (\rho) \geqslant \sum_ {j = 0} ^ {n - 1} w _ {j} + w _ {n} P _ {\text {b u r}} \left(\rho^ {(n)}\right) \geqslant 1 - p _ {f}, \tag {41}
$$

since

$$
\sum_ {j = 0} ^ {n - 1} w _ {j} = 1 - w _ {n} \tag {42}
$$

and  $w_{n}$  is exactly the failure probability  $p_f$  defined in (11). On the other hand, by the convexity of  $V_{\mathrm{asd}}$  and relation (35),

$$
D _ {\text {b u r}} (\rho) + V _ {\text {a s d}} (\rho) \leqslant \sum_ {i} w _ {i} = 1. \tag {43}
$$

Now (41) and (43) imply immediately the lower bound,

$$
p _ {f} \geqslant 1 - \frac {1}{n - 1} \sum_ {i} \sum_ {j \neq i} | \langle d _ {j} | d _ {i} \rangle_ {\mathrm {w}} \lambda_ {i} \lambda_ {j} |, \tag {44}
$$

which plays the central role in Ref. [16]. Moreover, there is no reason to restrict the above discussion to the special state  $|\Phi \rangle$  in (37), and similarly, one can actually recover the more general lower bound derived in Ref. [34]. In this sense, we show that nonorthogonal states that cannot be discriminated perfectly are consistent with the fact that any application of which-path detectors cannot enlarge the bound of simultaneous obtainable information of the wave aspect and particle aspect.

We hope the preceding discussion is sufficient to convince the reader that the old scheme of quantitative wave-particle duality discussed in Ref. [6] should not be forgotten when linking wave-particle duality with state discrimination, so that the general and intrinsic duality relation (35) is a useful generalization of the known results. Of course, this brief example also suggests that not only does state discrimination offer valid quantifiers of the wave-particle duality relation, but a suitable duality relation also provides information about unambiguous discrimination, a direction that is worthy of further investigations.

# V. CONCLUSION

We have shown that proper quantifiers of wave-particle duality can be obtained from discrimination of the ensembles (9) and (17), and hence shown that quantitative wave-particle duality can be considered from state discrimination in an intrinsic way. Three duality relations, i.e., the known one-bet relation (7), the relation that follows from unambiguous discrimination (32), and a more explicit relation (35), are derived to support this claim. In contrast to previous similar works, the introduction of the permutation matrix (8) enables us to study the asymmetry of the paths and therefore relate wave-particle duality with state discrimination without invoking which-path detectors. Finally, our work also suggests that wave-particle duality relations can be used to study state discrimination.

# ACKNOWLEDGMENTS

The author is funded by the Young Scientific Talents Growth Project, Department of Education of Guizhou Province (QJHKYZ[2018]377, QJHKYZ[2019]141), and the High-level Talents Fund of Liupanshui Normal University (LPSSYKYJJ201813).

[1] N. Bohr, The quantum postulate the recent development of atomic theory, Nature (London) 121, 580 (1928).  
[2] W. K. Wootters and W. H. Zurek, Complementarity in the double-slit experiment: Quantum nonseparability and a quantitative statement of Bohr's principle, Phys. Rev. D 19, 473 (1079).  
[3] D. M. Greenberger and A. Yasin, Simultaneous wave and particle knowledge in a neutron interferometer, Phys. Lett. A 128, 391 (1988).  
[4] G. Jaeger, A. Shimony, and L. Vaidman, Two interferometric complementarities, Phys. Rev. A 51, 54 (1995).  
[5] B.-G. Englert, Fringe Visibility and Which-Way Information: An Inequality, Phys. Rev. Lett. 77, 2154 (1996).  
[6] B. G. Englert and J. A. Bergou, Quantitative quantum erasure, Opt. Commun. 179, 337 (2000).  
[7] S. Durr, Quantitative wave-particle duality in multibeam interferometers, Phys. Rev. A 64, 042113 (2001).  
[8] G. Bimonte, and R. Musto, Comment on "Quantitative wave-particle duality in multibeam interferometers", Phys. Rev. A 67, 066101 (2003).  
[9] G. Bimonte and R. Musto, On interferometric duality in multi-beam experiments, J. Phys. A: Math. Gen. 36, 11481 (2003).  
[10] M. Jakob and J. A. Bergou, Complementarity and entanglement in bipartite qudit systems, Phys. Rev. A 76, 052107 (2007).  
[11] B.-G. Englert, D. Kaszlikowski, L. C. Kwek, and W. H. Chee, Wave-particle duality in multi-path interferometers: General concepts and three-path interferometers, Int. J. Quantum Inf. 06, 129 (2008).  
[12] M. Jakob and J. A. Bergou, Quantitative complementarity relations in bipartite systems: Entanglement as a physical reality, Opt. Commun. 283, 827 (2010).  
[13] L. Li, N.-L. Liu, and S. Yu, Duality relations in a two-path interferometer with an asymmetric beam splitter, Phys. Rev. A 85, 054101 (2012).  
[14] J. H. Huang, S. Wölk, S. Y. Zhu, and M. S. Zubairy, Higher-order wave-particle duality, Phys. Rev. A 87, 022107 (2013).  
[15] R. M. Angelo and A. D. Ribeiro, Wave-particle duality: An information-based approach, Found. Phys. 45, 1407 (2015).  
[16] M. N. Bera, T. Qureshi, M. A. Siddiqui, and A. K. Pati, Duality of quantum coherence and path distinguishability, Phys. Rev. A 92, 012118 (2015).  
[17] P. J. Coles, Entropic framework for wave-particle duality in multipath interferometers, Phys. Rev. A 93, 062111 (2016).

[18] E. Bagan, J. A. Bergou, S. S. Cottrell, and M. Hillary, Relations between Coherence and Path Information, Phys. Rev. Lett. 116, 160406 (2016).  
[19] T. Qureshi and M. A. Siddiqui, Wave-particle duality in  $N$ -path interference, Ann. Phys. 385, 598 (2017).  
[20] E. Bagan, J. Calsamiglia, J. A. Bergou, and M. Hillery, Duality Games and Operational Duality Relations, Phys. Rev. Lett. 120, 050402 (2018).  
[21] C. W. Helstrom, Quantum Detection and Estimation Theory (Academic, New York, 1976).  
[22] A. Chefles, Quantum state discrimination, Contemp. Phys. 41, 401 (2000).  
[23] J. A. Bergou, U. Herzog, and M. Hillary, Discrimination of quantum states, in Quantum State Estimation, edited by M. Paris and J. Reháček, Lecture Notes in Physics Vol. 649 (Springer, Berlin, 2004), pp. 417-465.  
[24] J. A. Bergou, Quantum state discrimination and selected applications, J. Phys.: Conf. Ser. 84, 012001 (2007).  
[25] J. Bae and L. C. Kwek, Quantum state discrimination and its applications, J. Phys. A: Math. Gen. 48, 083001 (2015).  
[26] X. Lu, Coherence and path information, Acta Phys. Sin. 69, 070301 (2020).  
[27] T. Baumgratz, M. Cramer, and M. B. Plenio, Quantifying Coherence, Phys. Rev. Lett. 113, 140401 (2014).  
[28] Y. Feng, R. Duan, and M. Ying, Unambiguous discrimination between mixed quantum states, Phys. Rev. A 70, 012308 (2004).  
[29] A. Uhlmann, The "transition probability" in the state space of a *-algebra, Rep. Math. Phys. 9, 273 (1976).  
[30] R. Jozsa, Fidelity for mixed quantum states, J. Mod. Opt. 41, 2315 (1994).  
[31] M. Nielsen and I. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, UK, 2000).  
[32] D. Bures, An extension of Kakutani's theorem on infinite product measures to the tensor product of semifinite  $w^{*}$ -algebras, Trans. Am. Math. Soc. 135, 199 (1969).  
[33] I. Bengtsson and K. Žyczkowski, Geometry of Quantum States: An Introduction to Quantum Entanglement (Cambridge University Press, Cambridge, UK, 2006).  
[34] S. Zhang, Y. Feng, X. Sun, and M. Ying, Upper bound for the success probability of unambiguous discrimination among quantum states, Phys. Rev. A 64, 062103 (2001).