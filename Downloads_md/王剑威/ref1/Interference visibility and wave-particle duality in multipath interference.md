# Interference visibility and wave-particle duality in multipath interference

Tabish Qureshi

Centre for Theoretical Physics, Jamia Millia Islamia, New Delhi 110025, India

![](images/491e0f174505e2ba50949fd11ebce70469579b0d14ffb0a834f3ecfb2d648e4e.jpg)

(Received 13 May 2019; published 8 October 2019)

Wave-particle duality in multipath interference is fraught with issues despite substantial progress in recent years. It was experimentally shown that in certain specific conditions, getting path information in a multipath experiment can actually increase the visibility of interference. As a result, it was argued that in multipath interference experiments, visibility of interference and which-path information are not always complementary observables. In the present paper, an alternative wave-particle duality relation is presented, based on a sum of visibilities of interference from individual pairs of paths. This relation is always respected, even in the kinds of specific situations mentioned above. This sum of visibilities turns out to be related to a recently introduced measure of coherence. As one of the consequences, it provides an alternative way of experimentally measuring coherence in a multipath interference experiment. As another consequence, this relation suggests a simple way of measuring path-distinguishability in multipath interference. In addition, it resolves several outstanding issues concerning wave-particle duality in multipath interference.

DOI: 10.1103/PhysRevA.100.042105

# I. INTRODUCTION

The last two decades have seen lot of research activity in the area of complementarity or wave-particle duality in multipath interference [1-17]. After Englert derived a duality relation  $\mathcal{D}^2 +\mathcal{V}^2\leqslant 1$ , for a two-path interference, which puts a bound on how much path information can be obtained from a quanton and the sharpness of interference it can show [18], it was natural to look for a similar duality relation for multislit interference. A breakthrough came with the derivation of the duality relation  $\mathcal{D}_Q + C\leqslant 1$  [9], between a path-distinguishability  $\mathcal{D}_Q$  based on unambiguous quantum state discrimination (UQSD) [19], and a quantity quantum coherence  $C$ , based on quantification of coherence by Baumgratz et al. [20].

Despite this tremendous progress, several issues still remained. One was how coherence  $C$ , which is just based on the  $l_{1}$ -norm of the off-diagonal elements of the density matrix of the quanton, can be measured in an experiment. A way to measure  $C$  from interference has been suggested [15], but that does not work in all scenarios, especially the kind described in the following. Mei and Weitz carried out multipath interference experiments where a controlled decoherence was introduced only in selected paths [3]. In addition, the phase of one of the paths was flipped by  $\pi$ . In such a situation, they saw that increasing decoherence, which could also amount to getting path information, actually increased the visibility or contrast of the interference. The visibility  $\mathcal{V}$ , it may be recalled, is simply Michelson's expression for fringe contrast  $\mathcal{V} = \frac{I_{\max} - I_{\min}}{I_{\max} + I_{\min}}$ , where  $I_{\max}, I_{\min}$  refer to the maximum and minimum intensities of interference, respectively [21]. This is in clear contradiction with the spirit of the Bohr's principle of complementarity [22]. Based on this result, several authors

argued that the interference visibility is not a good measure of interference or wave nature [4,5]. It was even argued that there exist path measurements which do not degrade interference [4]. In this kind of scenario, coherence  $C$  can be shown to always decrease with increasing decoherence, and appears to capture the wave nature of a quanton well. However, in such a scenario,  $C$  cannot be measured from interference by the method suggested in Ref. [15]. Thus, it remains an open question whether a measure of the wave nature can be gotten from interference in a multipath experiment [23]. The main result of this paper is the following duality relation for an unbiased  $n$ -path interference:

$$
\frac {2}{n (n - 1)} \sum_ {\text {p a i r s}} \mathcal {D} _ {Q _ {i j}} + \frac {2}{n (n - 1)} \sum_ {\text {p a i r s}} \mathcal {V} _ {i j} \leqslant 1, \tag {1}
$$

where  $\mathcal{V}_{ij}^{\prime}$  is the interference visibility if only the  $i$ th and  $j$ th slits are open, and the rest are blocked, and  $\mathcal{D}_{Q_{ij}}$  is the maximum probability of unambiguously distinguishing between the  $i$ th and  $j$ th paths in such a scenario. It may be useful to recall that  $n(n - 1)/2$  is the total number of slit pairs, making the two terms, the average of two-path distinguishability, and the average of two-path visibility, with the average taken over all path pairs. It will be shown that this inequality will hold in all situations, even the one described by Mei and Weitz's experiments [3]. There are several extremely useful consequences of this result, which will also be discussed in the following.

# II. INTERFERENCE VISIBILITY FROM PAIRS OF PATHS

We begin by writing a general pure state of a quantum passing through an  $n$ -slit or an  $n$ -path interferometer. If  $|\psi_k\rangle$  represents the state corresponding to the quantum taking the  $k$ th path, the general state is given by

$$
| \Psi \rangle = c _ {1} | \psi_ {1} \rangle + c _ {2} | \psi_ {2} \rangle + \dots + c _ {n} | \psi_ {n} \rangle , \tag {2}
$$

where  $|c_k|^2$  represents the probability of the quanton taking the  $k$ th path. The states  $\{|\psi_i\rangle\}$  can be assumed to form an orthonormal set, without loss of generality. If we are talking about an experiment in which a path detector is in place, which attempts to know which path the quantum followed, the basic requirement of the theory of quantum measurement is that certain path-detector states should get entangled with the states  $\{|\psi_i\rangle\}$ ,

$$
| \Psi \rangle = c _ {1} | \psi_ {1} \rangle | d _ {1} \rangle + c _ {2} | \psi_ {2} \rangle | d _ {2} \rangle + \dots + c _ {n} | \psi_ {n} \rangle | d _ {n} \rangle , \tag {3}
$$

where  $\{|d_i\rangle \}$  represent certain normalized states of the path detector which may not necessarily be orthogonal to each other. In case they are orthogonal to each other, measuring an observable of the path detector, which they are eigenstates of, will reveal which path the particle followed, e.g.,  $|\Psi \rangle \xrightarrow{\mathrm{measurement}} |\psi_k\rangle |d_k\rangle$  (say). The density matrix for the above entangled state, after tracing over the path-detector states, can be written as

$$
\rho = \operatorname {T r} _ {d} [ | \Psi \rangle \langle \Psi | ] = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} c _ {i} c _ {j} ^ {*} | \psi_ {i} \rangle \langle \psi_ {j} | \langle d _ {j} | d _ {i} \rangle . \tag {4}
$$

If the quanton were in a mixed state, for some reason, before encountering the path detector, a general form of the state would be given by

$$
\rho = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \rho_ {i j} | \psi_ {i} \rangle \langle \psi_ {j} | \langle d _ {j} | d _ {i} \rangle . \tag {5}
$$

In the subsequent discussion, we will assume the above to be the general form of the density operator, and will specify  $\rho_{ij} = c_i c_j^*$  for a pure quantum state.

Let us suppose that we block all the paths except the paths  $i, j$ . Then the effective density matrix of the quantum part will look like

$$
\rho^ {(2)} = \frac {1}{\rho_ {i i} + \rho_ {j j}} \left( \begin{array}{c c} \rho_ {i i} & \rho_ {i j} \\ \rho_ {j i} & \rho_ {j j} \end{array} \right), \tag {6}
$$

where the prefactor has been introduced to renormalize this  $2 \times 2$  matrix. The actual density matrix of the quantum will additionally have  $\langle d_j | d_i \rangle$  in the off-diagonal elements. For a two-slit interference, it is well known that the fringe visibility is given by twice the absolute value of the off-diagonal matrix elements. Hence we can write the visibility of interference from slits  $i$ ,  $j$  as

$$
\mathcal {V} _ {i j} = \frac {2 | \rho_ {i j} | | \langle d _ {j} | d _ {i} \rangle |}{\rho_ {i i} + \rho_ {j j}}. \tag {7}
$$

Since  $|d_i\rangle, |d_j\rangle$  are not in general orthogonal, one can do a UQSD measurement [19] to determine whether the path-detector state is  $|d_i\rangle$  or  $|d_j\rangle$ . The specific aspect of UQSD measurements is that if the method succeeds, one can tell for sure if the state is  $|d_i\rangle$  or  $|d_j\rangle$ . But sometimes the method fails, giving no result. If two states  $|d_i\rangle, |d_j\rangle$  occur with probabilities  $p_1, p_2$ , respectively, the optimal probability of a successful distinguishing between the two is given by  $P_{\mathrm{max}} = 1 - 2\sqrt{p_1p_2} |\langle d_j|d_i\rangle|$  [19]. In our two-slit interference, the probability of the state  $|d_i\rangle, |d_j\rangle$  occurring is  $\frac{\rho_{ii}}{\rho_{ii} + \rho_{jj}}, \frac{\rho_{jj}}{\rho_{ii} + \rho_{jj}}$ , respectively. So the optimal probability of successfully distinguishing between the two path-detector states is  $P_{\mathrm{max}} =$

$1 - \frac{2\sqrt{\rho_{ii}\rho_{jj}}}{\rho_{ii} + \rho_{jj}} |\langle d_j|d_i\rangle |.$  Consequently, this is also the optimal probability of successfully telling whether the quantum followed path  $i$  or  $j$ . This optimal probability is what we define our path distinguishability as. Thus, the path distinguishability for this two-slit interference is given by

$$
\mathcal {D} _ {\mathcal {Q} _ {i j}} = 1 - 2 \frac {\sqrt {\rho_ {i i} \rho_ {j j}}}{\rho_ {i i} + \rho_ {j j}} | \langle d _ {j} | d _ {i} \rangle |. \tag {8}
$$

Using Eqs. (7) and (8), we can write

$$
\mathcal {V} _ {i j} + \mathcal {D} _ {Q _ {i j}} + 2 \frac {\sqrt {\rho_ {i i} \rho_ {j j}} - | \rho_ {i j} |}{\rho_ {i i} + \rho_ {j j}} | \langle d _ {j} | d _ {i} \rangle | = 1. \tag {9}
$$

Since the density matrix given by Eq. (6) is positive semidefinite, one can write  $\sqrt{\rho_{ii}\rho_{jj}} - |\rho_{ij}| \geqslant 0$ . Thus, the above equation implies

$$
\mathcal {D} _ {\mathcal {Q} _ {i j}} + \mathcal {V} _ {i j} \leqslant 1. \tag {10}
$$

This is a wave-particle duality relation for two-path interference [24]. For a pure quantum state,  $\rho_{ij} = c_i c_j^*$  leads to  $\sqrt{\rho_{ii} \rho_{jj}} - |\rho_{ij}| = 0$ , and the duality relation saturates to an equality

$$
\mathcal {D} _ {\mathcal {Q} _ {i j}} + \mathcal {V} _ {i j} = 1. \tag {11}
$$

The result is that if all but two slits are closed, the effectively two-slit interference follows a tight duality relation Eq. (10), which saturates for the pure case.

This same procedure can be followed for all pairs of slits, thus yielding  $\mathcal{V}_{ij}$  and  $\mathcal{D}_{Q_{ij}}$  for all pairs  $i,j$ . Adding Eq. (10) for all pairs of slits, we get

$$
\sum_ {\text {p a i r s}} \mathcal {D} _ {Q _ {i j}} + \sum_ {\text {p a i r s}} \mathcal {V} _ {i j} \leqslant \frac {n (n - 1)}{2}, \tag {12}
$$

because for  $n$  slits, there are  $\frac{n(n - 1)}{2}$  pairs. Dividing both sides by  $\frac{n(n - 1)}{2}$ , we get the required duality relation

$$
\frac {2}{n (n - 1)} \sum_ {\text {p a i r s}} \mathcal {D} _ {Q _ {i j}} + \frac {2}{n (n - 1)} \sum_ {\text {p a i r s}} \mathcal {V} _ {i j} \leqslant 1, \tag {13}
$$

which, for a pure quantum state, will reduce to an equality. A skeptic may be excused for asking if the above relation, obtained by selectively opening only one pair of paths at a time, has anything to do with genuine multipath interference. After all, we know that even for a three-slit experiment, the three-slit interference pattern cannot be obtained simply as a sum of the interference patterns from various pairs of slits. To address this criticism, we delve deeper into Eq. (13) to understand its meaning.

# III. INTERFERENCE VISIBILITY AND COHERENCE

We first consider the case where all the paths are equally probable, which implies that  $\rho_{ii} = \frac{1}{n}$ ,  $i = 1, n$ . Two-path distinguishability and visibility, in this situation, are given by

$$
\mathcal {D} _ {\mathcal {Q} _ {i j}} = 1 - n \sqrt {\rho_ {i i} \rho_ {j j}} | \langle d _ {j} | d _ {i} \rangle |,
$$

$$
\mathcal {V} _ {i j} = n | \rho_ {i j} | | \langle d _ {j} | d _ {i} \rangle |. \tag {14}
$$

We substitute these expressions for  $\mathcal{D}_{Q_{ij}}$  and  $\mathcal{V}_{ij}^{\prime}$  into Eq. (13) to get

$$
1 - \frac {1}{n - 1} \sum_ {i \neq j} \sqrt {\rho_ {i i} \rho_ {j j}} | \langle d _ {j} | d _ {i} \rangle |) + \frac {1}{n - 1} \sum_ {i \neq j} | \rho_ {i j} | | \langle d _ {j} | d _ {i} \rangle | \leqslant 1, \tag {15}
$$

where we have used the fact that  $\sum_{i\neq j} = 2\sum_{\mathrm{pairs}}$ . From an earlier study of wave-particle duality in  $n$ -path interference, we recall [9]

$$
\mathcal {D} _ {Q} = 1 - \frac {1}{n - 1} \sum_ {i \neq j} \sqrt {\rho_ {i i} \rho_ {j j}} | \langle d _ {j} | d _ {i} \rangle |),
$$

$$
C = \frac {1}{n - 1} \sum_ {i \neq j} | \rho_ {i j} | | \langle d _ {j} | d _ {i} \rangle |, \tag {16}
$$

where  $\mathcal{D}_Q$  is the path distinguishability defined earlier for  $n$ -path interference and  $C$  is the coherence defined again for  $n$ -path interference. Using Eq. (16), the duality relation Eq. (13) assumes the form

$$
\mathcal {D} _ {\mathcal {Q}} + \mathcal {C} \leqslant 1, \tag {17}
$$

which is exactly the duality relation derived in Ref. [9]. So, for symmetric multipath interference, we get a very elegant connection of the path distinguishability and coherence of  $n$ -path interference with the path distinguishability and visibility of two-path interference of pairs of slits or paths:

$$
\mathcal {D} _ {Q} = \frac {2}{n (n - 1)} \sum_ {\text {p a i r s}} \mathcal {D} _ {Q _ {i j}}, \quad C = \frac {2}{n (n - 1)} \sum_ {\text {p a i r s}} \mathcal {V} _ {i j}. \tag {18}
$$

The immense usefulness of this connection will become clear in the following analysis, which also applies to the case of unequal intensities in different paths, which is discussed later.

What Eqs. (18) imply for coherence is that in an  $n$ -path interference with equal intensities in all beams, coherence  $C$  can be obtained simply by opening only a pair of paths at a time and measuring visibility by the conventional method, and then averaging this visibility over all the pairs of paths. Thus, Eqs. (18) provides a simple way of directly obtaining coherence from the interference pattern, although by the special procedure mentioned above. The other important consequence of Eqs. (18) is that in the kind of experiment hooked up by Mei and Weitz [3], flipping the phase of one path by  $\pi$  will have no effect on the visibility of interference from any two paths, if all other paths are blocked. Thus  $n$ -path coherence can be measured as easily in Mei and Weitz's experiment as in any normal multipath interference. This method then provides good measure of the wave nature of a quanton, which can be obtained from the interference from various path pairs. Not only is coherence  $C$  a good measure of wave nature, it can be obtained from the interference in all situations, contrary to the pessimistic view taken by some authors [4,5].

In earlier studies on wave-particle duality in multipath interference [8,10], the distinguishability  $\mathcal{D}_Q$  is defined as an upper bound on the probability with which the  $n$  paths can be unambiguously distinguished from each other. One problem with this upper bound is that it is not the optimal probability,

meaning there is no guaranty that this limit will be achievable for a give set of states  $\{|d_i\rangle\}$ . The second problem with  $\mathcal{D}_Q$  is that UQSD for more than two states works only for a linearly independent set  $\{|d_i\rangle\}$ . If the states are linearly dependent, UQSD cannot be used, and there is no meaning one can assign to the expression Eqs. (16) for  $\mathcal{D}_Q$ . The relations Eqs. (18) solve this problem. Even if the states are linearly dependent, Eqs. (18) gives a well-defined meaning to  $\mathcal{D}_Q$ , in terms of the sum distinguishabilities of different pairs of paths. Two-path distinguishability is based on UQSD involving only two states and is the optimal probability of distinguishing the two states. Therefore,  $\mathcal{D}_Q$  as defined by Eqs. (18) is always experimentally attainable. The third problem is that UQSD has only been experimentally demonstrated for two states [25]. No one knows how to implement it for more than two states. Since the present method represents the distinguishability in terms of two-path UQSD, it can be experimentally implemented.

Next we look at the more general case where all paths may not be equally probable. Here, instead of summing the two-path distinguishabilities and visibilities as done in Eq. (13), we multiply the duality relation Eq. (10) for each path-pair with the sum of probabilities of the two paths involved, and then sum over all  $i$ ,  $j$ $(i \neq j)$ :

$$
\sum_ {i \neq j} \left(\rho_ {i i} + \rho_ {j j}\right) \mathcal {D} _ {Q _ {i j}} + \sum_ {i \neq j} \left(\rho_ {i i} + \rho_ {j j}\right) \mathcal {V} _ {i j} ^ {\prime} \leqslant \sum_ {i \neq j} \rho_ {i i} + \rho_ {j j}. \tag {19}
$$

A duality relation for the asymmetric multipath interference can then be written from the above as

$$
\frac {1}{(n - 1)} \sum_ {\text {p a i r s}} \left(\rho_ {i i} + \rho_ {j j}\right) \mathcal {D} _ {Q _ {i j}} + \frac {1}{(n - 1)} \sum_ {\text {p a i r s}} \left(\rho_ {i i} + \rho_ {j j}\right) \mathcal {V} _ {i j} \leqslant 1. \tag {20}
$$

Substituting Eqs. (7) and (8) in the above, we again get the known duality relation Eq. (17). So we see that the new duality relation Eq. (20), for asymmetric  $n$ -path interference, is the same as Eq. (17), with the following connection:

$$
\mathcal {D} _ {Q} = \frac {1}{n - 1} \sum_ {\text {p a i r s}} (\rho_ {i i} + \rho_ {j j}) \mathcal {D} _ {Q _ {i j}},
$$

$$
C = \frac {1}{n - 1} \sum_ {\text {p a i r s}} \left(\rho_ {i i} + \rho_ {j j}\right) \mathcal {V} _ {i j}. \tag {21}
$$

As a consistency check, for all equally probable paths,  $(\rho_{ii} + \rho_{jj}) = \frac{2}{n}$ , and Eq. (20) reduces to Eq. (13).

It is clear from the preceding analysis that in a general multipath interference, where the paths may not be equally probable, the multipath distinguishability and multipath coherence can be experimentally measured by carrying out a series of experiments where only one pair of paths is open, and the visibility of interference is measured. However, here one also needs to measure the relative intensity of each path in the multipath experiment. One can then use Eq. (21) to get the coherence  $C$ . Similarly, if one is able to set up an experiment to measure path distinguishability of a pair of paths, one can use

Eqs. (21) to get the path distinguishability  $\mathcal{D}_Q$  for the multislit interference.

# IV. CONCLUSION

To summarize, we have introduced an alternative way of studying wave-particle duality in multipath interference by opening only one pair of paths at a time, and measuring conventional visibility and using UQSD to measure the distinguishability  $\mathcal{D}_{Q_{ij}}$ . The multislit path distinguishability  $\mathcal{D}_Q$  and multipath coherence  $C$  (for symmetric paths) can then be obtained as the average of  $\mathcal{D}_{Q_{ij}}$  and the average of  $\mathcal{V}_{ij}$  over all path pairs, respectively. For a multipath interference where the paths may not be equally probable, the same method works, but the average has to be taken with each term weighted with the total intensity from the two paths of the pair. This method resolves various outstanding issues in wave-particle duality in multipath interference, which are listed below.

(1) A way of measuring coherence in multipath interference is provided which works even for the experiment of Mei and Weitz [3], where interference visibility was shown to increase with increasing path knowledge.  
(2) The method shows that wave nature can always be characterized using interference, and that it is complementary to path information, even in multipath interference, contrary to existing belief [4,5].  
(3) Multipath coherence has been given an alternative meaning in terms of interference visibilities of path pairs.  
(4) Path distinguishability in multipath interference is given a new meaning in terms of path distinguishability for a pair of paths.  
(5) Path distinguishability in multipath interference continues to hold even in the situation when path-detector states form a linearly dependent set.  
(6) We have provided a way to measure path-distinguishability  $\mathcal{D}_Q$  in a multipath interference.

[1] S. Durr, Quantitative wave-particle duality in multibeam interferometers, Phys. Rev. A 64, 042113 (2001).  
[2] G. Bimonte and R. Musto, Comment on "Quantitative wave-particle duality in multibeam interferometers," Phys. Rev. A 67, 066101 (2003).  
[3] M. Mei and M. Weitz, Controlled Decoherence in Multiple Beam Ramsey Interference, Phys. Rev. Lett. 86, 559 (2001).  
[4] A. Luis, Complementarity in multiple beam interference, J. Phys. A: Math. Gen. 34, 8597 (2001).  
[5] G. Bimonte and R. Musto, On interferometric duality in multi-beam experiments, J. Phys. A: Math. Gen. 36, 11481 (2003).  
[6] B.-G. Englert, D. Kaszlikowski, L. C. Kwek, and W. H. Chee, Wave-particle duality in multi-path interferometers: General concepts and three-path interferometers, Int. J. Quantum Inform. 6, 129 (2008).  
[7] K. von Prillwitz, L. Rudnicki, and F. Mintert, Contrast in multipath interference and quantum coherence, Phys. Rev. A 92, 052114 (2015).  
[8] M. A. Siddiqui and T. Qureshi, Three-slit interference: A duality relation, Prog. Theor. Exp. Phys. 2015, 083A02 (2015).  
[9] M. N. Bera, T. Qureshi, M. A. Siddiqui, and A. K. Pati, Duality of quantum coherence and path distinguishability, Phys. Rev. A 92, 012118 (2015).  
[10] T. Qureshi and M. A. Siddiqui, Wave-particle duality in  $N$ -path interference, Ann. Phys. 385, 598 (2017).  
[11] P. Roy and T. Qureshi, Path predictability and quantum coherence in multi-slit interference, Phys. Scr. 94, 095004 (2019).  
[12] E. Bagan, J. A. Bergou, S. S. Cottrell, and M. Hillary, Relations between Coherence and Path Information, Phys. Rev. Lett. 116, 160406 (2016).  
[13] P. J. Coles, Entropic framework for wave-particle duality in multi-path interferometers, Phys. Rev. A 93, 062111 (2016).  
[14] T. Biswas, M. G. Díaz, and A. Winter, Interferometric visibility and coherence, Proc. R. Soc. A 473, 20170170 (2017).

[15] T. Paul and T. Qureshi, Measuring quantum coherence in multislit interference, Phys. Rev. A 95, 042110 (2017).  
[16] A. Venugopalan, S. Mishra, and T. Qureshi, Monitoring decoherence via measurement of quantum coherence, Physica A 516, 308 (2019).  
[17] M. Afrin and T. Qureshi, Quantum coherence and path-distinguishability of two entangled particles, Eur. Phys. J. D 73, 31 (2019).  
[18] B.-G. Englert, Fringe Visibility and Which-Way Information: An Inequality, Phys. Rev. Lett. 77, 2154 (1996).  
[19] I. D. Ivanovic, How to differentiate between non-orthogonal states, Phys. Lett. A 123, 257 (1987); D. Dieks, Overlap and distinguishability of quantum states, ibid. 126, 303 (1988); A. Peres, How to differentiate between non-orthogonal states, ibid. 128, 19 (1988); G. Jaeger and A. Shimony, Optimal distinction between two non-orthogonal quantum states, ibid. 197, 83 (1995).  
[20] T. Baumgratz, M. Cramer, and M. B. Plenio, Quantifying Coherence, Phys. Rev. Lett. 113, 140401 (2014).  
[21] M. Born and E. Wolf, Principles of Optics, 3rd ed. (Pergamon, New York, 1965).  
[22] N. Bohr, The quantum postulate and the recent development of atomic theory, Nature (London) 121, 580 (1928).  
[23] T. Qureshi, Coherence, interference and visibility, Quanta 8, 24 (2019).  
[24] K. K. Menon and T. Qureshi, Wave-particle duality in asymmetric beam interference, Phys. Rev. A 98, 022130 (2018).  
[25] R. B. M. Clarke, A. Chefles, S. M. Barnett, and E. Riis, Experimental demonstration of optimal unambiguous state discrimination, Phys. Rev. A 63, 040305(R) (2001); M. Mohseni, A. M. Steinberg, and J. A. Bergou, Optical Realization of Optimal Unambiguous Discrimination for Pure and Mixed Quantum States, Phys. Rev. Lett. 93, 200403 (2004).