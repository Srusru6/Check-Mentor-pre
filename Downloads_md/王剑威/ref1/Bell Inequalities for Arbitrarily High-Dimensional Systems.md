# Bell Inequalities for Arbitrarily High-Dimensional Systems

Daniel Collins, $^{1,2}$  Nicolas Gisin, $^{3}$  Noah Linden, $^{4}$  Serge Massar, $^{5}$  and Sandu Popescu $^{1,2}$

<sup>1</sup>H. H. Wills Physics Laboratory, University of Bristol, Tyndall Avenue, Bristol BS8 1TL, United Kingdom

$^{2}$ BRIMS, Hewlett-Packard Laboratories, Stoke Gifford, Bristol BS12 6QZ, United Kingdom

<sup>3</sup>Group of Applied Physics, University of Geneva, 20, rue de l'Ecole-de-Médecine, CH-1211 Geneva 4, Switzerland

$^{4}$ Department of Mathematics, Bristol University, University Walk, Bristol BS8 1TW, United Kingdom

$^{5}$ Service de Physique Théorique, Université Libre de Bruxelles, CP 225, Boulevard du Triomphe, B1050 Bruxelles, Belgium

(Received 23 July 2001; published 10 January 2002)

We develop a novel approach to Bell inequalities based on a constraint that the correlations exhibited by local variable theories must satisfy. This is used to construct a family of Bell inequalities for bipartite quantum systems of arbitrarily high dimensionality which are strongly resistant to noise. In particular, our work gives an analytic description of previous numerical results and generalizes them to arbitrarily high dimensionality.

DOI: 10.1103/PhysRevLett.88.040404

PACS numbers: 03.65.Ud, 03.67.-a

One of the most remarkable aspects of quantum mechanics is its predicted correlations. Indeed, the correlations between outcomes of measurements performed on systems composed of several parts in an entangled state have no classical analog. The most striking aspect of this characteristic feature of quantum physics is revealed when the parts are spatially separated: no classical theory based on local variables can reproduce the quantum correlations. Historically, this became known as the Einstein-Podolsky-Rosen paradox and was formulated in terms of measurable quantities by Bell [1] and by Clauser, Horne, Shimony, and Holt [2] as the nowadays famous inequalities. Other aspects of quantum correlation were analyzed in the form of paradoxes, such as Schrödinger's cat and the measurement problem. In recent years, these paradoxical aspects have been overthrown by a more effective approach: let us exploit "quantum strangeness" to perform tasks that are classically impossible has become the new leitmotiv. From this "conceptual revolution," the field of quantum information emerged. Old words became fashionable, such as "entanglement." Old questions were revisited, such as the classifications of quantum correlations.

The variety of known partial results, in particular, about entanglement measures, makes it today obvious that there is no one-parameter classification of entanglement. This Letter concerns classifications related to what is called "quantum nonlocality," i.e., the impossibility to reproduce quantum correlations with theories based on local variables (often called "local realistic theories"). Specifically we develop a powerful new approach to Bell inequalities which we then use to write several families of Bell inequalities for higher-dimensional systems.

Local variable theories cannot exhibit arbitrary correlations. Rather the conditions these correlations must obey can always be written as inequalities (the Bell inequalities) which the joint probabilities of outcomes must satisfy. Our approach to Bell inequalities is based on a logical constraint the correlations must satisfy in the case of local

variable theories. In order to introduce this constraint, let us suppose that one of the parties, Alice, can carry out two possible measurements,  $A_{1}$  or  $A_{2}$ , and that the other party, Bob, can carry out two possible measurements,  $B_{1}$  or  $B_{2}$ . Each measurement may have  $d$  possible outcomes:  $A_{1}, A_{2}, B_{1}, B_{2} = 0, \ldots, d - 1$ . Without loss of generality a local variable theory can be described by  $d^{4}$  probabilities  $c_{jklm}$  ( $j, k, l, m = 0, \ldots, d - 1$ ) that Alice's local variable ( $jk$ ) specifies that measurement  $A_{1}$  gives outcome  $j$  and measurement  $A_{2}$  gives outcome  $k$  and that Bob's local variable ( $lm$ ) specifies that measurement  $B_{1}$  gives outcome  $l$  and measurement  $B_{2}$  gives outcome  $m$ . (In this formulation Alice and Bob's strategy is deterministic since it is completely determined by the value of their variables  $jk$  and  $lm$ . Any nondeterministic local theory can be rephrased in the above way by incorporating the local randomness in the probabilities  $c_{jklm}$ ; see, for instance, [3].) Since the probabilities  $c_{jklm}$  are positive ( $c_{jklm} \geq 0$ ) and sum to one ( $\sum_{jklm} c_{jklm} = 1$ ). The joint probabilities take the form  $P(A_{1} = j, B_{1} = l) = \sum_{km} c_{jklm}$ , and similarly for  $P(A_{1} = j, B_{2} = m)$ ,  $P(A_{2} = k, B_{1} = l)$  and  $P(A_{2} = k, B_{2} = m)$ .

Let us consider a particular choice of local variables  $jklm$  (this choice occurs with probability  $c_{jklm}$ ). Since  $A_1 = j$ ,  $A_2 = k$ ,  $B_1 = l$ ,  $B_2 = m$  we have

$$
r ^ {\prime} \equiv B _ {1} - A _ {1} = l - j,
$$

$$
s ^ {\prime} \equiv A _ {2} - B _ {1} = k - l, \tag {1}
$$

$$
t ^ {\prime} \equiv B _ {2} - A _ {2} = m - k,
$$

$$
u ^ {\prime} \equiv A _ {1} - B _ {2} = j - m.
$$

We see that the difference,  $r'$ , between  $A_{1}$  and  $B_{1}$  can be freely chosen by choosing  $j$  and  $l$ . Similarly the difference,  $s'$ , between  $B_{1}$  and  $A_{2}$  and the difference,  $t'$ , between  $A_{2}$  and  $B_{2}$  can be freely chosen. But then the difference  $u'$  between  $B_{2}$  and  $A_{1}$  is constrained since we necessarily have

$$
r ^ {\prime} + s ^ {\prime} + t ^ {\prime} + u ^ {\prime} = 0. \tag {2}
$$

Thus in a local variable theory the relation between three pairs of operators can be freely chosen, but then the last relation is constrained.

This constraint plays a central role in our Bell inequalities. Indeed they are written in such a way that their maximum value can be attained only if this constraint is frustrated. The simplest such Bell expression is

$$
\begin{array}{l} I \equiv P \left(A _ {1} = B _ {1}\right) + P \left(B _ {1} = A _ {2} + 1\right) \\ + P \left(A _ {2} = B _ {2}\right) + P \left(B _ {2} = A _ {1}\right), \tag {3} \\ \end{array}
$$

where we have introduced the probability  $P(A_{a} = B_{b} + k)$  that the measurements  $A_{a}$  and  $B_{b}$  have outcomes that differ, modulo  $d$ , by  $k$ :

$$
P \left(A _ {a} = B _ {b} + k\right) \equiv \sum_ {j = 0} ^ {d - 1} P \left(A _ {a} = j, B _ {b} = j + k \bmod d\right). \tag {4}
$$

Because the difference between  $A_{a}$  and  $B_{b}$  is evaluated modulo  $d$ , all the outcomes of  $A_{a}$  and  $B_{b}$  are treated on an equal footing. As we see in Eq. (3) this symmetrization is the key to reducing Bell inequalities to the logical constraint that is imposed by local variable theories. Indeed because of the constraint Eq. (2) any choice of local variables  $jklm$  can satisfy only three of the relations appearing in Eq. (3), e.g.,  $A_{1} = B_{1}$ ,  $B_{1} = A_{2} + 1$ , etc. Hence  $I(\text{local realism}) \leq 3$ . On the other hand, nonlocal correlations can attain  $I = 4$  since they can satisfy all four relations.

In the case of two-dimensional systems the inequality  $I(\text{local variable}) \leq 3$  is equivalent to the Clauser-Horne-Shimony-Holt (CHSH) inequality [2]. But the power of our reformulation is already apparent since this inequality generalizes the CHSH inequality to arbitrarily large dimensions. In fact, the above formulation of the constraint imposed by local realistic theories allows one to write in a unified way all previously known Bell inequalities [4]. It can also serve to write completely new Bell inequalities and this is the subject of the present Letter. Specifically we have generalized in a nontrivial way [see Eqs. (5) and (6) below] the Bell expression (3) to  $d$ -dimensional systems (for any  $d \geq 2$ ).

One of the interests of these new Bell expressions is that they are highly resistant to noise. Indeed Bell inequalities are sensitive to the presence of noise and above a certain

amount of noise the Bell inequalities will cease to be violated by a quantum system. However, it has been shown by numerical optimization [5] that using higher-dimensional systems can increase the resistance to noise. The measurements that are carried out on the quantum system in order to obtain an increased violation have been described analytically in [6]. And an analytical proof of the greater robustness of quantum systems of dimension 3 was given in [7]. One of the interests of our new Bell inequalities is that when we apply them to the quantum state and measurement described in [6] for those dimensions ( $d \leq 16$ ) for which a numerical optimization was carried out in [6], we obtain the same resistance to noise as in [6].

The first generalization of the Bell expression Eq. (3) is

$$
\begin{array}{l} I _ {3} \equiv + [ P (A _ {1} = B _ {1}) + P (B _ {1} = A _ {2} + 1) \\ + P \left(A _ {2} = B _ {2}\right) + P \left(B _ {2} = A _ {1}\right) ] \\ - \left[ P \left(A _ {1} = B _ {1} - 1\right) + P \left(B _ {1} = A _ {2}\right) \right. \\ + P \left(A _ {2} = B _ {2} - 1\right) + P \left(B _ {2} = A _ {1} - 1\right) ]. \tag {5} \\ \end{array}
$$

The maximum value of  $I_{3}$  for nonlocal theories is 4 since a nonlocal theory could satisfy all four relations that have a + sign in (5). On the other hand, for a local variable theory  $I_{3} \leq 2$ . This should be compared to the constraint  $I(\text{local variable}) \leq 3$  for the expression (3). The origin of this difference is the - signs in (5). Indeed we have seen when analyzing (3) that only three of the relations with a + sign can be satisfied by local realistic theories. But if three relations with + are satisfied in (5), then necessarily one relation with - is also satisfied giving a total of  $I_{3} = 2$ . Alternatively one can satisfy two relations with + and two relations with weight zero (if the dimension is larger than 2), once more giving a total of  $I_{3} = 2$ .

For  $d = 2$  the inequality  $I_{3}(\text{local variable}) \leq 2$  is equivalent to the inequality  $I(\text{local variable}) \leq 3$  and therefore to the CHSH inequality. But for  $d \geq 3$  the inequality based on  $I_{3}$  is not equivalent to that based on  $I$ . For the quantum measurement described below (when  $d \geq 3$ ) the inequality based on  $I_{3}$  (and its generalizations  $I_{d}$  given below) is more robust than that based on  $I$ .

The Bell expression  $I_{3}$  can be further generalized when the dimensionality is greater than 3 by adding extra terms. The extra terms in  $I_{d}$  do not change the maximum value attainable by local variable theories  $[I_{d}^{\max}(\text{local variable}) = 2]$ , nor do they change the maximum value attainable by completely nonlocal theories  $(I_{d}^{\max} = 4)$ . However, these extra terms allow a better exploitation of the correlations exhibited by quantum systems.

These new Bell expressions have the form

$$
\begin{array}{l} I _ {d} \equiv \sum_ {k = 0} ^ {[ d / 2 ] - 1} \left(1 - \frac {2 k}{d - 1}\right) \{+ [ P (A _ {1} = B _ {1} + k) + P (B _ {1} = A _ {2} + k + 1) + P (A _ {2} = B _ {2} + k) + P (B _ {2} = A _ {1} + k) ] \\ - \left[ P \left(A _ {1} = B _ {1} - k - 1\right) + P \left(B _ {1} = A _ {2} - k\right) + P \left(A _ {2} = B _ {2} - k - 1\right) \right. \\ + P \left(B _ {2} = A _ {1} - k - 1\right) \rbrack \}. \tag {6} \\ \end{array}
$$

As mentioned above the maximum value of  $I_{d}$  is 4. This follows immediately from the fact that the maximum weight of the terms in (6) is  $+1$ . And the maximum value of  $I_{d}$  for local variable theories is 2. We now prove this last result.

The proof consists of enumerating all the possible relations between  $A_{1}$ ,  $B_{1}$ ,  $A_{2}$ ,  $B_{2}$  allowed by the constraints (2). This is most easily done by first changing notation. We do not use the coefficients  $r^{\prime}, s^{\prime}, t^{\prime}, u^{\prime}$  defined in (1), but we use new coefficients  $r, s, t, u$  defined by the relation

$$
A _ {1} = B _ {1} + r, \quad B _ {1} = A _ {2} + s + 1, \tag {7}
$$

$$
A _ {2} = B _ {2} + t, \quad B _ {2} = A _ {1} + u,
$$

which obey the constraint

$$
r + s + t + u + 1 = 0 \bmod d. \tag {8}
$$

Furthermore we restrict (without loss of generality)  $r, s, t, u$  to lie in the interval

$$
- [ d / 2 ] \leq r, s, t, u \leq [ (d - 1) / 2 ]. \tag {9}
$$

With this notation the value of the Bell inequality for a given choice of  $r, s, t, u$  is

$$
I _ {d} (r, s, t, u) = f (r) + f (s) + f (t) + f (u), \tag {10}
$$

where  $f$  is given by

$$
f (x) = \left\{ \begin{array}{l l} - \frac {2 x}{d - 1} + 1, & x \geq 0, \\ - \frac {2 x}{d - 1} - \frac {d + 1}{d - 1}, & x <   0. \end{array} \right. \tag {11}
$$

We now consider different cases according to the signs of  $r, s, t, u$ .

1.  $r, s, t, u$  are all positive. Then (8) and (9) imply that  $r + s + t + u = d - 1$ . Inserting into (10) and using (11) one finds  $I_d = 2$ .  
2. Three of the numbers  $r, s, t, u$  are positive, one is strictly negative. Then (8) and (9) imply that either  $r + s + t + u = d - 1$  or  $r + s + t + u = -1$ . Inserting into (10) and using (11) one finds either  $I_d = -2 / (d - 1)$  or  $I_d = 2$ .  
3. Two of the numbers  $r, s, t, u$  are positive, two are strictly negative. Then (8) and (9) imply that  $r + s + t + u = -1$ . Inserting into (10) and using (11) one finds  $I_d = -2 / (d - 1)$ .

4. One of the numbers  $r, s, t, u$  is positive, three are strictly negative. Then (8) and (9) imply that either  $r + s + t + u = -1$  or  $r + s + t + u = -d - 1$ . Inserting into (10) and using (11) one finds either  $I_d = -2(d + 1) / (d - 1)$  or  $I_d = -2 / (d - 1)$ .  
5. The numbers  $r, s, t, u$  are all strictly negative. Then (8) and (9) imply that  $r + s + t + u = -d - 1$ . Inserting into (10) and using (11) one finds  $I_d = -2(d + 1) / (d - 1)$ .

(Note that for small dimensions  $d$  not all the possibilities enumerated above can occur. For instance, for  $d = 2$ , the only possible values are  $I_d = \pm 2$ .) Thus for all possible choices of  $r, s, t, u, I_d(\text{local realism}) \leq 2$ . This concludes the proof.

Let us now consider the maximum value that can be attained for the Bell expressions  $I_{d}$  for quantum measurements on an entangled quantum state. We have carried out a numerical search for the optimal measurements. It turns out that the best measurements that we have found numerically give the same value as the measurements described in [6]. We do not have a proof that these measurements are optimal, but our numerical work and the numerical work that inspired [6] suggests that this is the case.

We therefore first recall the state and the measurement described in [6]. The quantum state is the maximally entangled state of two  $d$ -dimensional systems

$$
\psi = \frac {1}{\sqrt {d}} \sum_ {j = 0} ^ {d - 1} | j \rangle_ {A} \otimes | j \rangle_ {B}. \tag {12}
$$

Let the operators  $A_{a}$ ,  $a = 1,2$ , measured by Alice and  $B_{b}$ ,  $b = 1,2$ , measured by Bob have the nondegenerate eigenvectors

$$
| k \rangle_ {A, a} = \frac {1}{\sqrt {d}} \sum_ {j = 0} ^ {d - 1} \exp \left(i \frac {2 \pi}{d} j (k + \alpha_ {a})\right) | j \rangle_ {A}, \tag {13}
$$

$$
| l \rangle_ {B, b} = \frac {1}{\sqrt {d}} \sum_ {j = 0} ^ {d - 1} \exp \left(i \frac {2 \pi}{d} j (- l + \beta_ {b})\right) | j \rangle_ {B},
$$

where  $\alpha_{1} = 0$ ,  $\alpha_{2} = 1/2$ ,  $\beta_{1} = 1/4$ , and  $\beta_{2} = -1/4$ . These measurements can be viewed as being carried out in two steps: First Alice and Bob give each of the states  $|j\rangle_{A}$  and  $|j\rangle_{B}$  a variable phase depending on the measurement they want to perform; then Alice measures in the Fourier transform basis and Bob in the inverse Fourier basis. Thus the joint probabilities are

$$
\begin{array}{l} P _ {Q M} (A _ {a} = k, B _ {b} = l) = \frac {1}{d ^ {3}} \left| \sum_ {j = 0} ^ {d - 1} \exp \left[ i \frac {2 \pi j}{d} (k - l + \alpha_ {a} + \beta_ {b}) \right] \right| ^ {2} = \frac {1}{d ^ {3}} \frac {\sin^ {2} [ \pi (k - l + \alpha_ {a} + \beta_ {b}) ]}{\sin^ {2} [ \pi (k - l + \alpha_ {a} + \beta_ {b}) / d ]} \\ = \frac {1}{2 d ^ {3} \sin^ {2} \left[ \pi \left(k - l + \alpha_ {a} + \beta_ {b}\right) / d \right]}, \tag {14} \\ \end{array}
$$

where in the last line we have used the values of  $\alpha_{a}$  and  $\beta_{b}$  given above.

Equation (14) shows that these joint probabilities have several symmetries. First of all we have the relation

$$
P _ {Q M} \left(A _ {a} = k, B _ {b} = l\right) = P _ {Q M} \left(A _ {a} = k + c, B _ {b} = l + c\right)
$$

for all integers  $c$ . This symmetry property justifies us considering, as in (4), only the probabilities that  $A_{a}$  and  $B_{b}$  differ by a given constant integer  $c$ :

$$
\begin{array}{l} P _ {Q M} (A _ {a} = B _ {b} + c) = \sum_ {j = 0} ^ {d - 1} P _ {Q M} (A _ {a} = j + c, B _ {b} = j) \\ = d P _ {Q M} \left(A _ {a} = c, B _ {b} = 0\right). \tag {15} \\ \end{array}
$$

Furthermore we have the relation

$$
\begin{array}{l} P _ {Q M} \left(A _ {1} = B _ {1} + c\right) = P _ {Q M} \left(B _ {1} = A _ {2} + c + 1\right) \\ = P _ {Q M} \left(A _ {2} = B _ {2} + c\right) \\ = P _ {Q M} \left(B _ {2} = A _ {1} + c\right). \tag {16} \\ \end{array}
$$

Using Eqs. (14)-(16) we can rank these probabilities by decreasing order. Let us denote

$$
\begin{array}{l} q _ {c} = P _ {Q M} \left(A _ {1} = B _ {1} + c\right) \\ = 1 / \left\{2 d ^ {3} \sin^ {2} \left[ \pi (c + 1 / 4) / d \right] \right\}. \tag {17} \\ \end{array}
$$

Then we have

$$
\begin{array}{l} q _ {0} > q _ {- 1} > q _ {1} > q _ {- 2} > q _ {2} > \dots > q _ {- [ d / 2 ]} \tag {18} \\ \left(\geq q _ {\left[ d / 2 \right]}\right), \\ \end{array}
$$

where  $[x]$  denotes the integer part of  $x$  and the last term between parentheses occurs only for odd dimension  $d$ . This suggests that the quantum probabilities violate the constraints imposed by local variable theories. Indeed the probabilities in (16) are maximized by taking  $c = 0$ , but then the four relations that appear in (16) are incompatible with local realism. In fact, replacing the above probabilities in the expression (3) yields a value  $I_{QM} = 4dq_0 > 3$  for all dimensions  $d$ .

However, a stronger violation is obtained if instead of using the Bell expression  $I$ , one uses the Bell expressions  $I_d$ . In fact, for a  $d$ -dimensional quantum system, one can use all the Bell expressions  $I_k$  for  $k \leq d$ , but the strongest violation is obtained by using the Bell expression  $I_d$ . This value, denoted  $I_d(QM)$ , is given by

$$
I _ {d} (Q M) = 4 d \sum_ {k = 0} ^ {[ d / 2 ] - 1} \left(1 - \frac {2 k}{d - 1}\right) \left(q _ {k} - q _ {- (k + 1)}\right). \tag {19}
$$

For instance, we find

$$
I _ {3} (Q M) = 4 / (- 9 + 6 \sqrt {3}) \simeq 2. 8 7 2 9 3,
$$

$$
I _ {4} (Q M) = \frac {2}{3} (\sqrt {2} + \sqrt {1 0 - \sqrt {2}}) \simeq 2. 8 9 6 2 4,
$$

$$
\begin{array}{l} \lim  _ {d \rightarrow \infty} I _ {d} (Q M) = \frac {2}{\pi^ {2}} \sum_ {k = 0} ^ {\infty} \frac {1}{(k + 1 / 4) ^ {2}} - \frac {1}{(k + 3 / 4) ^ {2}} \\ = 3 2 \times \text {C a t a l a n} / \pi^ {2} \simeq 2. 6 9 8 1, \\ \end{array}
$$

where Catalan  $\simeq 0.9159$  is Catalan's constant.

In the presence of uncolored noise the quantum state becomes

$$
\rho = p \left| \psi \right\rangle \langle \psi | + (1 - p) \frac {1}{d ^ {2}}, \tag {20}
$$

where  $p$  is the probability that the state is unaffected by noise. The value of the Bell inequality for the state  $\rho$  is

$$
I _ {d} (\rho) = p I _ {d} (Q M). \tag {21}
$$

Hence the Bell inequality  $I_{d}$  is certainly violated if

$$
p > \frac {2}{I _ {d} (Q M)} = p _ {d} ^ {\min } \tag {22}
$$

(If there is a quantum measurement giving a value of  $I_{d}$  greater than that given by Eq. (19), then of course the Bell inequality would be violated with even more noise. This remark applies to the various  $p^{\mathrm{min}}$  below.)

As a function of  $d$  one finds that  $p_d^{\min}$  is a decreasing function of  $d$ . For instance,

$$
p _ {3} ^ {\min } = (6 \sqrt {3} - 9) / 2 \simeq 0. 6 9 6 1 5,
$$

$$
p _ {4} ^ {\min } = 3 / (\sqrt {2} + \sqrt {1 0 - \sqrt {2}}) \simeq 0. 6 9 0 5 5,
$$

$$
\lim  _ {d \rightarrow \infty} p _ {d} ^ {\min } (d) = \pi^ {2} / (1 6 \times \text {C a t a l a n}) \simeq 0. 6 7 3 4 4.
$$

For  $d = 3$  this reproduces the analytical result of [7]. And combining Eqs. (19) and (22) reproduces the numerical results of [6] for all dimensions ( $2 \leq d \leq 16$ ) for which a numerical optimization was carried out.

In summary, our reformulation of Bell inequalities in terms of a logical constraint local variable theories must satisfy has provided the basis for constructing a large family of Bell inequalities for systems of large dimension. The numerical work of [5,6] and a numerical search of our own suggest that these Bell inequalities are optimal in the same sense that the CHSH inequality is optimal for two-dimensional systems, namely, both the resistance to noise and the amount by which the inequality is violated are maximal. For this reason we hope that the Bell inequalities presented here will have as much interest for physicists studying entanglement of systems of large dimensionality as the CHSH inequalities have had for bidimensional systems.

We acknowledge funding by the European Union under project EQUIP (IST-FET program).

Note added.—While completing this Letter we learned of a Bell inequality for qutrits [8] that exhibits the same resistance to noise as that obtained in [5-7].

[1] J. S. Bell, Physics (Long Island City, N.Y.) 1, 195 (1964).  
[2] J.F. Clauser, M.A. Horne, A. Shimony, and R.A. Holt, Phys. Rev. Lett. 23, 880 (1969).  
[3] I. Percival, Phys. Lett. A 244, 495 (1998).  
[4] D. Collins, N. Gisin, N. Linden, S. Popescu, and V. Scarani (to be published).  
[5] D. Kaszlikowski, P. Gnacinski, M. Zukowski, W. Miklaszewski, and A. Zeilinger, Phys. Rev. Lett. 85, 4418 (2000).  
[6] T. Durt, D. Kaszlikowski, and M. Zukowski, Phys. Rev. A 64, 024101 (2001).  
[7] J.-L. Chen, D. Kaszlikowski, L.C. Kwek, M. Zukowski, and C.H. Oh, quant-ph/0103099.  
[8] D. Kaszlikowski, L.C. Kwek, J.-L. Chen, M. Zukowski, and C.H. Oh, quant-ph/0106010.