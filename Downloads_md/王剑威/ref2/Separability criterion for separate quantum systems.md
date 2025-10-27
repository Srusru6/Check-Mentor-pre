# Separability criterion for separate quantum systems

M. G. Raymer* and A. C. Funk

Oregon Center for Optics and Department of Physics, University of Oregon, Eugene, Oregon 97403

B. C. Sanders

Department of Physics and Centre for Advanced Computing-Algorithms and Cryptography, Macquarie University,

Sydney, New South Wales 2109, Australia

H. de Guise

Department of Physics, Lakehead University, Thunder Bay, Ontario, Canada P7B 5E1

(Received 9 October 2002; published 27 May 2003)

Entanglement, or quantum inseparability, is a crucial resource in quantum information applications, and therefore the experimental generation of separated yet entangled systems is of paramount importance. Experimental demonstrations of inseparability with light are not uncommon, but such demonstrations in physically well-separated massive systems, such as distinct gases of atoms, are new and present significant challenges and opportunities. Rigorous theoretical criteria are needed for demonstrating that given data are sufficient to confirm entanglement. Such criteria for experimental data have been derived for the case of continuous-variable systems obeying the Heisenberg-Weyl (position-momentum) commutator. To address the question of experimental verification more generally, we develop a sufficiency criterion for arbitrary states of two arbitrary systems. When applied to the recent study by Julsgaard, Kozhekin, and Polzik [Nature 413, 400 (2001)] of spin-state entanglement of two separate, macroscopic samples of atoms, our criterion confirms the presence of spin entanglement.

DOI: 10.1103/PhysRevA.67.052104

PACS number(s): 03.65.Ud, 03.67.-a, 42.50.-p

Entanglement, or quantum inseparability, is a profound property of nature that enables information to be stored, communicated, and processed in a decidedly nonclassical fashion [1]. Entanglement has long been observed in the states of small numbers of microscopic objects such as electrons or photons. Only recently have there been efforts to create and observe entanglement in the state of massive macroscopic objects, such as the collective spins of two separate atomic vapors [2,3]. It is important therefore to develop a sufficient criterion, which, if satisfied, would unambiguously verify that an experiment has displayed entanglement.

Previous significant work has been done to find a sufficiency criterion that is valid for continuous-variable systems obeying the Heisenberg-Weyl (HW) commutator, valid for position-momentum variables and, similarly, for light-field amplitudes [4,5]. Such a condition is not strictly valid, however, for collective-spin systems, although an approximate correspondence was proposed for certain special spin states and used to analyze a recent experiment by Julsgaard, Kozhekin, and Polzik (JKP) [2]. This study was aimed at demonstrating spin-state entanglement for two separate, macroscopic samples of atoms containing around  $10^{12}$  atoms each. We derive a sufficiency condition for the existence of entanglement between two arbitrary quantum systems, including spin systems, in pure or mixed states. This allows us, for example, to confirm rigorously the presence of entanglement in the experiment of JKP. This criterion is general, and so may find application in other experimental studies.

Two distinct quantum systems 1 and 2 are said to be entangled if their joint density operator  $\hat{\rho}$  is inseparable, that is,

if  $\hat{\rho}$  cannot be represented as a convex sum of density operators  $\hat{\rho}_{1i}$  and  $\hat{\rho}_{2i}$  for the two physically separated systems [6,7],

$$
\hat {\rho} = \sum_ {i} p _ {i} \hat {\rho} _ {1 i} \otimes \hat {\rho} _ {2 i}, \tag {1}
$$

with  $p_i$  a set of non-negative, normalized probabilities. If their joint state is separable (not entangled), then it must be possible to express the density operator in the form Eq. (1). One physical interpretation of entanglement is that it represents a correlation between two systems that is stronger than can exist in any classical (local, realistic) theory [8].

A convincing demonstration of entanglement would prove a violation of the separability condition Eq. (1). In attempting to demonstrate inseparability between the spin variables of two separated atomic samples, JKP employ nonlocal Bell measurements on the spin variables and relate these spin variables to canonical position and momspectrum operators obeying the Heisenberg-Weyl (HW) commutator  $[\hat{q}_j,\hat{p}_k] = i\delta_{jk}$ $(j,k = 1,2)$ . By establishing this approximate correspondence, JKP then adapt a criterion by Duan et al. [4] and by Simon [5], which applies to coupled oscillators (and specifically to squeezed light). The "HW" criterion that is sufficient for inseparability is [4,5]

$$
\operatorname {v a r} \left(\hat {q} _ {1} + \hat {q} _ {2}\right) + \operatorname {v a r} \left(\hat {p} _ {1} - \hat {p} _ {2}\right) \geqslant 2, \tag {2}
$$

the assumption that for certain states spin operators can be approximately replaced by canonical position and momentum operators.

Although the shortcut proposed by JKP offers an appealing connection between criteria for demonstrating entanglement in squeezed-light systems and in spin ensembles, the validity of this correspondence is far from obvious, and can lead to misconceptions regarding transformations between different bases that are quite distinct from the Fourier transform nature of the canonical position-momentum transformations. Before returning to a consideration of entanglement in collective-spin systems, we first establish a criterion for inseparability that is applicable to any algebra, including that for spin. We do this by generalizing the calculations of Duan et al. [4] and of Berry and Sanders [9].

We consider two systems 1 and 2, and two observables for each,  $\hat{A}_1$ ,  $\hat{B}_1$  for system 1 and  $\hat{A}_2$ ,  $\hat{B}_2$  for system 2, that obey  $[\hat{A}_i,\hat{B}_j] = \delta_{i,j}\hat{C}_j$ . Define linear combinations,

$$
\hat {u} = \alpha \hat {A _ {1}} + \beta \hat {A _ {2}},
$$

$$
\hat {v} = \alpha \hat {B} _ {1} - \beta \hat {B} _ {2}, \tag {3}
$$

for  $\alpha$ ,  $\beta$  arbitrary real coefficients. Equation (1) implies for the variance

$$
\operatorname {v a r} (\hat {u}) = \sum_ {i} p _ {i} \left[ \alpha^ {2} \left\langle \left(\Delta \hat {A} _ {1}\right) ^ {2} \right\rangle_ {i} + \beta^ {2} \left\langle \left(\Delta \hat {A} _ {2}\right) ^ {2} \right\rangle_ {i} \right] + S, \tag {4}
$$

where  $\Delta \hat{A}_k = \hat{A}_k - \langle \hat{A}_k\rangle_{\rho}$  and  $\langle \dots \rangle_{\rho}$  denotes an average over  $\hat{\rho}$ . The quantity  $S$  is  $S = \Sigma_i p_i\langle \hat{u}\rangle_i^2 - (\Sigma_i p_i\langle \hat{u}\rangle_i)^2$ , where  $\langle \dots \rangle_i$  denotes the average over the product density operator  $\hat{\rho}_{1i} \otimes \hat{\rho}_{2i}$ . The Schwarz inequality implies, in general, that  $S \geqslant 0$ . Doing the same for  $\hat{v}$  and adding the results gives

$$
\begin{array}{l} \operatorname {v a r} (\hat {u}) + \operatorname {v a r} (\hat {v}) \geqslant \sum_ {i} p _ {i} \left[ \alpha^ {2} \left\langle \left(\Delta \hat {A} _ {1}\right) ^ {2} \right\rangle_ {i} + \beta^ {2} \left\langle \left(\Delta \hat {A} _ {2}\right) ^ {2} \right\rangle_ {i} \right] \\ + \sum_ {i} p _ {i} \left[ \alpha^ {2} \left\langle \left(\Delta \hat {B} _ {1}\right) ^ {2} \right\rangle_ {i} + \beta^ {2} \left\langle \left(\Delta \hat {B} _ {2}\right) ^ {2} \right\rangle_ {i} \right], \tag {5} \\ \end{array}
$$

or

$$
\begin{array}{l} \operatorname {v a r} (\hat {u}) + \operatorname {v a r} (\hat {v}) \geqslant \alpha^ {2} \left[ \left\langle \left(\Delta \hat {A} _ {1}\right) ^ {2} \right\rangle_ {\rho} + \left\langle \left(\Delta \hat {B} _ {1}\right) ^ {2} \right\rangle_ {\rho} \right] \\ + \beta^ {2} \left[ \left\langle \left(\Delta \hat {A} _ {2}\right) ^ {2} \right\rangle_ {\rho} + \left\langle \left(\Delta \hat {B} _ {2}\right) ^ {2} \right\rangle_ {\rho} \right]. \tag {6} \\ \end{array}
$$

Equation (6) is always satisfied for any separable state, with respect to any variables (discrete or continuous) belonging to any algebra. If one can measure all the corresponding quantities and find a violation of Eq. (6), then one demonstrates that the state is inseparable.

The general commutator  $[\hat{A}_i,\hat{B}_j] = \delta_{ij}\hat{C}_j$  implies the uncertainty relation  $\Delta A_i\Delta B_i\geqslant (1 / 2)C_i$  , where  $C_i = |\langle \hat{C}_i\rangle |$ $= |\mathrm{Tr}(\hat{\rho} [\hat{A}_i,\hat{B}_i])|(i = 1,2)$  . This implies the less restrictive

relation  $\Delta A_i^2 + \Delta B_i^2 \geqslant C_i$ , with equality only for  $\Delta A_i^2 = C_i / 2$ . Inserting this into Eq. (6) gives, for any separable state,

$$
\operatorname {v a r} (\hat {u}) + \operatorname {v a r} (\hat {v}) \geqslant \alpha^ {2} C _ {1} + \beta^ {2} C _ {2}. \tag {7}
$$

This is our main result. A related criterion has been recently found for the case of pure states of spin systems [9]. In the special case  $\alpha = \beta = 1$ , Eq. (7) gives

$$
\operatorname {v a r} \left(\hat {A} _ {1} + \hat {A} _ {2}\right) + \operatorname {v a r} \left(\hat {B} _ {1} - \hat {B} _ {2}\right) \geqslant C _ {1} + C _ {2}. \tag {8}
$$

Equation (7) is not a tight bound. That is, it is necessary for any separable state to satisfy Eq. (7), but it need not be violated for every entangled (i.e., inseparable) state. So Eq. (7) is a necessary but not sufficient condition for separability. A sufficient and necessary criterion that is experimentally accessible for spin ensembles is not known. For the special case of Gaussian states of Heisenberg-Weyl systems with  $C_1 = C_2 = 1$ , Eq. (8) reduces to Eq. (2), which has been shown by Duan et al. [4] and Simon [5] to be a sufficient and necessary condition for separability in this case.

In the JKP study, the variables of interest are the projections  $\hat{J}_x,\hat{J}_y,\hat{J}_z$  of the collective spins of two atomic samples, 1 and 2. The experiment [2] can be analyzed by choosing  $\hat{A}_1 = \hat{J}_{y1}$ ,  $\hat{B}_1 = \hat{J}_{z1}$ ,  $\hat{A}_2 = \hat{J}_{y2}$ ,  $\hat{B}_2 = -\hat{J}_{z2}$ . Then  $C_1 + C_2 = |\langle \hat{J}_{x1}\rangle | + |\langle -\hat{J}_{x2}\rangle | = 2|\langle \hat{J}_{x1}\rangle |$ , and separability requires, from Eq. (8),

$$
\left. \operatorname {v a r} \left(\hat {J} _ {y 1} + \hat {J} _ {y 2}\right) + \operatorname {v a r} \left(\hat {J} _ {z 1} + \hat {J} _ {z 2}\right) \geqslant 2 \mid \langle \hat {J} _ {x 1} \rangle \right|. \tag {9}
$$

Equation (9) yields a rigorous criterion: if this inequality is violated, then entanglement has been demonstrated.

This result is similar in form to JKP's Eq. (1), reviewed below, but is distinct in several important respects. The first is that our criterion for demonstrating inseparability is expressed entirely in terms of the spin operators and does not entail any approximations. This result is valid even without the restriction that a large number of atoms is required. There is no recourse, nor any need for recourse, to canonical position and momentum operators or to the criterion for squeezed oscillators. The second difference is that Eq. (9) is a valid criterion for arbitrary states not only for certain extremum states as in the criterion of JKP. The final difference is that the right-hand side of Eq. (9) is the expectation value with respect to the state under investigation, rather than being determined by a quantity defined in terms of some "classical" value.

The present result puts on a firm theoretical ground the criterion used by JKP as a necessary criterion for separability. The violation of Eq. (9) by the data in the JKP study can be taken as an indication of the breakdown of separability. Nevertheless, the question of an experimentally accessible, sufficient condition, even for special classes of states (e.g., the Gaussian ones for the case of HW systems), is still an open one for the case of spin systems.

Here, we present arguments that one cannot take the approximate correspondence between spin variables and HW variables too literally, as it can lead to errors if care is not

![](images/6109736449481262dc33a136214f2d282b9fe8238cbd1bf58a9a02770d424e66.jpg)  
FIG. 1. "Extremum" angular-momentum states having large total  $J$  and total  $J_{x} \widetilde{=} J$  can be visualized as occupying the shaded region tightly concentrated near the  $J_{x}$  "pole" in a space with axes  $J_{x}, J_{y}, J_{z}$ . The quasicontinuous variables  $Q$  and  $P$  can be thought of as forming approximately the Cartesian coordinates of the tangent plane touching the sphere with radius  $J$ .

taken. (Our approach avoids the problematic extrapolation of HW results.) For example, large errors occur when calculating a change of basis if one uses eigenstates of  $\hat{J}_y$  and  $\hat{J}_z$  as basis states and assumes that these transform approximately as HW variables do. These errors persist even for the extremum states considered by JKP.

To review JKP's analysis, the collective-spin vector operator  $\hat{J}$  (total angular momentum) of a collection of  $N$  atoms (where  $N$  may be known or statistically distributed) is defined to have  $x$  component  $\hat{J}_x = \sum_{i=1}^{N} \hat{J}_x^{(i)}$ , and similarly for  $\hat{J}_y$  and  $\hat{J}_z$ . These components obey the algebra  $[\hat{J}_y, \hat{J}_z] = i\hat{J}_x$ , etc., and commute with  $\hat{J}^2$ ; the number of atoms  $N$  determines the corresponding irreducible representation. For  $N = 2j$ , one choice for an orthonormal basis comprises  $|j, m_x\rangle_x$  that satisfy the eigenvalue relations  $\hat{J}^2 |j, m_x\rangle_x = j(j + 1)|j, m_x\rangle_x$  and  $\hat{J}_x|j, m_x\rangle_x = m_x|j, m_x\rangle_x$ . For  $\bar{J}_x$  equal to some "large classical" real number ( $>0$ ), JKP define operators  $\hat{Q} = \hat{J}_y / \sqrt{\bar{J}_x}$  and  $\hat{P} = \hat{J}_z / \sqrt{\bar{J}_x}$  satisfying  $[\hat{Q}, \hat{P}] = i\hat{J}_x / \bar{J}_x$  [10].

Consider extremum states  $|\Psi \rangle$  having narrow support over approximately equal values of  $m_x \cong \overline{J}_x$ , where  $\overline{J}_x$  is a large, state-independent real number. Such extremum states can be visualized as tightly concentrated near the  $J_x$  "pole" in a space with axes  $J_x, J_y, J_z$ , as illustrated in Fig. 1. JKP suggest that for such states one can approximate  $\hat{J}_x / \overline{J}_x$  by the unity operator to obtain  $[\hat{Q}, \hat{P}] = i$ . This commutator, along with Eq. (2), would lead directly to the necessary criterion for separability in the form of JKP's Eq. (1). This result is correct in a restricted sense, as noted above.

Nevertheless, there are difficulties with taking this approximate approach too literally. This is evidenced by the fact that a basis transformation between the eigenstates of  $\hat{Q} = \hat{J}_y / \sqrt{\bar{J}_x}$  and  $\hat{P} = \hat{J}_z / \sqrt{\bar{J}_x}$  is not given by a Fourier transform, despite the commutator between the operators being forced to be a constant, which seemingly implies that the

eigenstates have overlap  $\langle P|Q\rangle \propto \exp (-iPQ)$ . The inapplicability of the Fourier transform is apparent by attempting this transformation. In the  $J_{y}$  basis,

$$
\begin{array}{l} | \Psi \rangle = \sum_ {2 j = 0} ^ {\infty} \sum_ {m _ {y} = - j} ^ {j} | j, m _ {y} \rangle_ {y y} \langle j, m _ {y} | \Psi \rangle \\ = \sum_ {2 j = 0} ^ {\infty} \sum_ {m _ {y} = - j} ^ {j} | j, m _ {y} \rangle_ {y} C _ {y} (j, m _ {y}), \tag {10} \\ \end{array}
$$

and the summation notation means sum  $j$  over non-negative half-integers. For the extremum states, with large mean- $j$  value  $\overline{j}$  (say  $10^{12}$ ), the coefficients  $C_{y}(j,m_{y})$  are nonnegligible only in the vicinity of  $m_{y} = 0$ .

The same state represented in the  $J_{z}$  basis is

$$
\left| \Psi \right\rangle = \sum_ {2 j = 0} ^ {\infty} \sum_ {m _ {z} = - j} ^ {j} C _ {z} (j, m _ {z}) \left| j, m _ {z} \right\rangle_ {z}. \tag {11}
$$

The two sets of coefficients are related by

$$
C _ {z} (j, m _ {z}) = \sum_ {m _ {y} = - j} ^ {j _ {z}} _ {z} \left\langle j, m _ {z} \right| j, m _ {y} \rangle_ {y} C _ {y} (j, m _ {y}). \tag {12}
$$

Angular-momentum algebra gives  $\sum_{z} \langle j, m_z | j, m_y \rangle_y = d_{m_z, m_y}^j (\pi / 2)$ , where the elements of the rotation matrix (reduced Wigner function) are [11]

$$
\begin{array}{l} d _ {m m ^ {\prime}} ^ {j} (\pi / 2) = 2 ^ {- j} \sqrt {\frac {(j + m ^ {\prime}) ! (j - m ^ {\prime}) !}{(j + m) ! (j - m) !}} \sum_ {k = 0} ^ {j - m} \binom {j + m} {j + m ^ {\prime} - k} \\ \times \binom {j - m} {k} (- 1) ^ {m - m ^ {\prime} + k}. \tag {13} \\ \end{array}
$$

The basis transformation Eq. (12) is entirely different from a Fourier transformation, in which the  $m_y, m_z$  values would be replaced by quasicontinuous variables  $m_y \rightarrow J_y = Q\sqrt{\overline{J}_x}$ ,  $m_z \rightarrow J_z = P\sqrt{\overline{J}_z}$ , and the transformation would be

$$
C _ {z} (P) = \int_ {- \infty} ^ {\infty} d Q (1 / 2 \pi) ^ {1 / 2} \exp (- i P Q) C _ {y} (Q). \tag {14}
$$

The asymptotic form of the reduced Wigner function Eq. (13) is given in the Appendix, where it is seen not to be approximated by the Fourier transform kernel. Furthermore, these transformations differ in a qualitative way: Whereas the transformation kernel of Eq. (14) is necessarily complex, there exists a choice of phase that makes the correct kernel real, as in Eq. (13).

A concrete example, given in the Appendix, illustrates the large errors that can result from using the Fourier transform. There we consider a specific state satisfying the assumed extremum properties  $(\overline{J}_y,\overline{J}_z\ll \overline{J}_x)$ , which would presumably make the commutator  $[\hat{Q},\hat{P} ] = i$  approximately correct. Upon making a basis change from the  $J_{y}$  basis to the  $J_{z}$  basis, we find, using the correct Eq. (12), that the mean value of  $\hat{J}_{z}$  is given by a formula consistent with  $\overline{J}_z\ll \overline{J}_x$ . However,

when (provisionally) using the Fourier transform for the basis change calculation we compute a mean value  $\bar{J}_z = -(\pi /2)\bar{J}_x$ . This is incorrect, as for this state  $\bar{J}_z$  must be much smaller than  $\bar{J}_x$ . This demonstrates the complete breakdown of a simple, direct replacement of the spin-operator algebra by the HW algebra, leading to the need for the more careful derivation we provided in the first half of this paper.

In conclusion, Eq. (7) provides a necessary condition for separability for arbitrary states of two general systems. This condition is accessible to experimental tests in that it involves measurements of only several low-order moments. When applied to collective angular-momentum variables in macroscopic atomic systems, the criterion confirms the one used by JKP in their experimental study [2]. The problem of finding sufficient conditions for special classes of angular-momentum states remains to be solved.

The complete replacement, for all purposes, of the collective angular-momentum algebra by the simpler HW (position-momentum) algebra is not valid, even for extremum states that are nearly confined to a small region in angular-momentum space, corresponding to highly polarized atomic samples. We do not intend to imply that the use of the approximate commutator  $[\hat{Q},\hat{P}] = i$  will always lead to large errors. If one evaluates operator moments involving only states confined to the proper extremum region, then only small errors are incurred, as is well known. We caution, however, that one cannot assume the validity of state expansions in basis states having the same properties as  $Q$  and  $P$  eigenstates.

Another extension of the method of Ref. [4] to the SU(2) spin operators for a different configuration (inseparability criterion of particle entanglement in one ensemble) is derived in Sørensen et al. [12]. In contrast to the present study, Sørensen et al. considered a collection of atoms with a single (local) set of operators (angular-momentum operators in their case). They found that a squeezing condition for these local operators implies nonseparability of the state for all the component subsystems (atoms). In our study we consider two separated systems that can be measured independently, and we effectively establish a two-mode (as opposed to one-mode in Sørensen et al.) squeezing criterion for establishing a "bipartite" inseparability. Our work and that of Sørensen et al. are distinct but complementary. It does not appear that they are equivalent, in the sense that the results of one could be derived directly from the other.

Finally, it is interesting to address the question—what states, if any, are conjugate to the  $|j,m\rangle_y$  states through a Fourier transformation? The answer is the SU(2) phase states. In the SU(2) phase formulation [13] one constructs the  $(2j + 1)$ -dimensional basis from phase states, defined as  $|j,\theta_k\rangle_y = (2j + 1)^{-1 / 2}\Sigma_m^j = -j e^{im\theta_k} |j,m\rangle_y$ , with  $\theta_{k} = k\pi /(2j + 1)$ . From this, we obtain the desired Fourier transform kernel  $_y\langle j,\theta |j,m\rangle_y = e^{im\theta} / \sqrt{2j + 1}$ . Even though the basis change from  $|j,m\rangle_y$  states to phase states is a (discrete) Fourier transformation, the phase operators  $\hat{\phi}_y$  constructed for this representation do not naturally yield a commutator

$[\hat{J}_y,\hat{\phi}_y] = i$  . Therefore, there is not an exact way to use this correspondence to construct an equivalent HW algebra.

We wish to thank Stephen Bartlett and Dominic Berry for helpful discussions, and Peter Braun for a tip on arriving at Eq. (A1). Support for this project has been provided by the National Science Foundation Grants No. PHY-0140370 and ECS-9977127, the Army Research Office Grant No. DAAD19-99-1-0344, an Australian Research Council International Research Exchange Scheme grant, and an Australian Research Council Large Grant. H.dG. acknowledges support from NSERC of Canada.

# APPENDIX

When  $j$  is large and  $m, m' \ll j$  the reduced Wigner function Eq. (13) is well approximated by using Stirling's formula to give

$$
\begin{array}{l} d _ {m m ^ {\prime}} ^ {j} (\pi / 2) \cong \sqrt {\frac {2}{\pi j}} \exp (+ | m ^ {2} - m ^ {\prime 2} | / 2 j) \\ \times \cos \left((j + m - m ^ {\prime}) \frac {\pi}{2}\right). \tag {A1} \\ \end{array}
$$

This does not approximate to the Fourier transform kernel.

As an illustration of the large errors that can arise when using the Fourier transform to execute a basis change between  $J_{y}$  and  $J_{z}$  bases, consider the state with

$$
C _ {y} (j, m _ {y}) = \frac {\exp (- \bar {j}) \alpha_ {1} ^ {j + m _ {y}} \alpha_ {2} ^ {j - m _ {y}}}{\sqrt {(j + m _ {y}) ! (j - m _ {y}) !}}, \tag {A2}
$$

where  $\alpha_{k} = |\alpha_{k}|\exp (i\phi_{k})$  . The mean values for this state are  $\overline{j} = (|\alpha_1|^2 +|\alpha_2|^2) / 2,\qquad \overline{m}_y = \overline{J}_y = (|\alpha_1|^2 -|\alpha_2|^2) / 2,\qquad \overline{J}_z$ $= |\alpha_{1}\alpha_{2}|\cos (\phi_{2} - \phi_{1})$  , and  $\bar{J}_{x} = |\alpha_{1}\alpha_{2}|\sin (\phi_{2} - \phi_{1})$  . We consider states such that  $\phi_2 - \phi_1\cong \pi /2$  and  $|\alpha_{1}|^{2} - |\alpha_{2}|^{2}$ $\ll |\alpha_1|^2 +|\alpha_2|^2$  , and hence are in the considered extremum class, with  $\overline{J}_y,\overline{J}_z\ll \overline{J}_x$

In the  $J_{z}$  basis this same state is represented exactly by [using Eqs. (12) and (13)]

$$
C _ {z} (j, m _ {z}) = \frac {\exp (- \bar {j}) \beta_ {1} ^ {j + m _ {z}} \beta_ {2} ^ {j - m _ {z}}}{\sqrt {(j + m _ {z}) ! (j - m _ {z}) !}}, \tag {A3}
$$

with  $\beta_{1} = (\alpha_{2} + \alpha_{1}) / \sqrt{2}$  and  $\beta_{2} = (\alpha_{2} - \alpha_{1}) / \sqrt{2}$ . The mean values  $\bar{J}_x, \bar{J}_y, \bar{J}_z$  are unchanged by the change of basis, but we now have  $\tilde{m}_{z} = \bar{J}_{z} = |\alpha_{1}\alpha_{2}|\cos (\phi_{2} - \phi_{1})$ .

How does this exact result compare with that obtained by assuming that the HW commutator is valid, which requires that we transform Eq. (A2) by the Fourier relation? To carry this out, we first find an accurate approximation to Eq. (A2), using Stirling's formula, which gives, for  $j \cong \overline{j}$  large (e.g.,  $10^{12}$ ) and  $m_y, \overline{m}_y \ll \overline{j}$  (and arbitrary phases  $\phi_1, \phi_2$ ),

$$
\begin{array}{l} C _ {y} (j, m _ {y}) \cong C (j) (\pi \bar {j}) ^ {- 1 / 4} \exp \left[ - \left(m _ {y} - \bar {m} _ {y}\right) ^ {2} / 2 \bar {j} \right] \\ \times \exp [ i (\phi_ {1} - \phi_ {2}) m _ {y} ], \tag {A4} \\ \end{array}
$$

with  $C(j) = \sqrt{\exp(-2\overline{j})(2\overline{j})^{2j} / (2j)!}\exp [i(\phi_1 + \phi_2)j]$ , which is a relatively narrow function of  $j$ .

Using Eq. (14) to transform Eq. (A4), we find (with the provisional result indicated by the tilde)

$$
\begin{array}{l} \widetilde {C} _ {z} (j, m _ {z}) \cong C (j) \left(\frac {\bar {j}}{\pi \bar {J} _ {x} ^ {2}}\right) ^ {1 / 4} \exp \left[ \frac {- \left(m _ {z} - \tilde {m} _ {z}\right) ^ {2}}{2 \left(\bar {J} _ {x} ^ {2} / \bar {j}\right)} \right] \\ \times \exp \left[ - i \left(\frac {m _ {z} \bar {m} _ {y}}{\bar {J} _ {x}} - \left(\phi_ {1} - \phi_ {2}\right) \bar {m} _ {y}\right) \right], \tag {A5} \\ \end{array}
$$

which means that the mean value of  $\hat{J}_z$  is given provisionally by  $\bar{J}_z = \tilde{m}_z = (\phi_1 - \phi_2)\bar{J}_x$ . This predicted value for  $\bar{J}_z$  is quite incorrect. As an example consider  $\phi_2 - \phi_1 = \pi / 2$ . Equation

(A3) predicts (correctly and exactly) that  $\overline{J}_z$  has a mean value  $\overline{J}_z = 0$ , while Eq. (A5) predicts a mean value  $\overline{J}_z = \widetilde{m}_z = -(\pi /2)\overline{J}_x$ . This is incorrect, as for this state  $\overline{J}_z$  must be much smaller than  $\overline{J}_x$ .

For completeness, the correct Eq. (A3) for the state in the  $J_{z}$  basis can be well approximated using Stirling's formula, (since  $|\beta_1|^2 - |\beta_2|^2 \ll |\beta_1|^2 + |\beta_2|^2$ ), giving

$$
\widetilde {C} _ {z} (j, m _ {z}) \cong C (j) \exp \left[ - \left(m _ {z} - \bar {m} _ {z}\right) ^ {2} / 2 \bar {j} \right] \exp \left[ i \left(\phi_ {1} ^ {\prime} - \phi_ {2} ^ {\prime}\right) m _ {z} \right], \tag {A6}
$$

where  $\phi_k' = \arg [\beta_k]$ . Equations (A6) and (A5) differ in two important ways—both in the phase structure and in the predicted mean value of  $m_z$ .

[1] M.A. Nielsen and I.L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, 2000).  
[2] B. Julsgaard, A. Kozhekin, and E.S. Polzik, Nature (London) 413, 400 (2001).  
[3] N.P. Bigelow, Acta Phys. Pol. A 101, 449 (2002).  
[4] L.M. Duan, G. Giedke, J.I. Cirac, and P. Zoller, Phys. Rev. Lett. 84, 2722 (2000).  
[5] For an alternative derivation of the same separability criterion see R. Simon, Phys. Rev. Lett. 84, 2726 (2000). For a consideration of the conditions under which the sparability criterion holds, see B.-G. Englert and K. Wodkiewicz, Phys. Rev. A 65, 054303 (2002).  
[6] R.F. Werner, Phys. Rev. A 40, 4277 (1989).  
[7] M. Lewenstein, D. Bruss, J.I. Cirac, B. Kraus, M. Kus, J. Sam

sonowicz, A. Sanpera, and R. Tarrach, J. Mod. Opt. 47, 2481 (2000).  
[8] J.S. Bell, Speakable and Unspeakable in Quantum Mechanics (Cambridge University Press, Cambridge, 1988).  
[9] D.W. Berry and B.C. Sanders, New J. Phys. 4, 8 (2002).  
[10] We have rewritten the operators and commutator using the usual right-hand coordinate system convention, rather than the left-handed system used by JKP.  
[11] D.A. Varshalovich, A.N. Moskalev, and V.K. Khersonskii, Quantum Theory of Angular Momentum (World Scientific, Singapore, 1988).  
[12] A. Sørensen, L.M. Duan, J.I. Cirac, and P. Zoller, Nature (London) 409, 63 (2001).  
[13] A. Vourdas, Phys. Rev. A 41, 1653 (1990).