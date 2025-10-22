# Quantifying Coherence

T. Baumgratz, M. Cramer, and M. B. Plenio  
Institut für Theoretische Physik, Albert-Einstein-Allee 11, Universität Ulm, 89069 Ulm, Germany  
(Received 24 February 2014; revised manuscript received 18 July 2014; published 29 September 2014)

We introduce a rigorous framework for the quantification of coherence and identify intuitive and easily computable measures of coherence. We achieve this by adopting the viewpoint of coherence as a physical resource. By determining defining conditions for measures of coherence we identify classes of functionals that satisfy these conditions and other, at first glance natural quantities, that do not qualify as coherence measures. We conclude with an outline of the questions that remain to be answered to complete the theory of coherence as a resource.

DOI: 10.1103/PhysRevLett.1.13.140401

PACS numbers: 03.65.Aa, 03.67.Mn

Introduction.—Coherence, being at the heart of interference phenomena, plays a central role in physics as it enables applications that are impossible within classical mechanics or ray optics. The rise of quantum mechanics as a unified picture of waves and particles further strengthened the prominent role of coherence in physics. Indeed, in conjunction with energy quantization and the tensor product structure of state space, coherence underlies phenomena such as multiparticle interference and entanglement that play a central role in applications of quantum physics and quantum information science.

Quantum optical methods provide an important set of tools for the manipulation of coherence, and indeed, at its basis lies the formulation of the quantum theory of coherence [1,2]. Here, coherence is studied in terms of phase space distributions and multipoint correlation functions to provide a framework that relates closely to classical electromagnetic phenomena. While this is helpful in drawing intuition from classical wave mechanics and identifies those aspects for which quantum coherence deviates from classical coherence phenomena, it does not provide a rigorous and unambiguous framework. The development of such a quantitative framework for coherence gains further urgency in the light of recent discussions concerning the role of coherence in biological systems [3] which can benefit from a more rigorous approach to the quantification of coherence properties.

The development of quantum information science over the last two decades has led to a reassessment of quantum physical phenomena such as entanglement, elevating them from mere tools to "subtly humiliate the opponents of quantum mechanics" [4] to resources that may be exploited to achieve tasks that are not possible within the realm of classical physics. This viewpoint, then, motivates the development of a quantitative theory that captures this resource character in a mathematically rigorous fashion. The formulation of such resource theories was initially pursued with the quantitative theory of entanglement [5,6] which led to the view that constraints [e.g., the restriction to local operations and classical communication (LOCC)] that prevent certain

physical operations to be realized define resources (e.g., entangled states) that help to overcome the imposed constraints [7,8]. This viewpoint has proven fruitful not only for the development of applications, but also in providing the impetus for theory to establish a unified and rigorously defined framework for a quantitative theory of physical resources by addressing the three principal issues: (i) the characterization, (ii) the quantification, and (iii) the manipulation of quantum states under the imposed constraints [9,10]. This framework is being explored for entanglement [5,6], thermodynamics [11,12], and reference frames [13] and has led to the recognition of deep interrelations between the theories of entanglement and the second law [7,8].

In contrast, a wide variety of measures of coherence is in use (often functions of a density matrix' off-diagonal entries) whose use tends to be justified principally on the grounds of physical intuition. Here, we put such measures on a sound footing by establishing a quantitative theory of coherence as a resource following the approach that has been established for entanglement in Refs. [6-8] and for reference frames in Ref. [13]. We present the basic assumptions of our approach and use these to identify various quantitative and easy-to-compute valid measures of coherence while rejecting others.

Results. At the heart of our discussion lies the characterization of incoherent states together with the notion of incoherent operations, i.e., quantum operations that map the set of incoherent states onto itself. We distinguish between quantum operations with and without subselection. These technical definitions lead to an operationally well-defined maximally coherent state which may serve as a unit for coherence. We collect a set of conditions any proper measure of coherence should satisfy. Prime among them is the requirement of monotonicity under incoherent operations. We, then, discuss several examples—some of which take the form of easy to evaluate analytical expressions. For instance, we find that the relative entropy of coherence

$$
C _ {\text {r e l . e n t .}} (\hat {q}) = S (\hat {q} _ {\text {d i a g}}) - S (\hat {q}), \tag {1}
$$

where  $S$  is the von Neumann entropy and  $\hat{Q}_{\mathrm{diag}}$  denotes the state obtained from  $\hat{\varrho}$  by deleting all off-diagonal elements, and the intuitive  $l_{1}$  norm of coherence

$$
C _ {l _ {1}} (\hat {\varrho}) = \sum_ {\substack {i, j \\ i \neq j}} | \varrho_ {i, j} |, \tag{2}
$$

are both proper measures of coherence. In contrast, we find that the sum of the squared absolute values of all off-diagonal elements violates monotonicity.

Incoherent states.-The first step to defining a coherence measure is to agree which states are incoherent. A natural definition is to fix a particular basis,  $\{|i\rangle \}_{i = 1,\dots,d}$ , of the  $d$ -dimensional Hilbert space  $\mathcal{H}$  in which we consider our quantum states [14]. We call all density matrices that are diagonal in this basis incoherent and, henceforth, label this set of quantum states by  $\mathcal{I} \subset \mathcal{H}$  [15]. Hence, all density operators  $\hat{\delta} \in \mathcal{I}$  are of the form

$$
\hat {\delta} = \sum_ {i = 1} ^ {d} \delta_ {i} | i \rangle \langle i |. \tag {3}
$$

Incoherent operations.-The definition of coherence monotones (and, thus, coherence quantifiers) requires the definition of operations that are incoherent--just as in entanglement theory the definition of entanglement monotones requires a definition of nonentangling operations. There, this definition is determined by practical considerations, namely locality constraints, which leads to the definition of LOCC operations. Here, we characterize the set of incoherent physical operations as follows. Quantum operations are specified by a set of Kraus operators  $\{\hat{K}_n\}$  satisfying  $\sum_{n}\hat{K}_{n}^{\dagger}\hat{K}_{n} = \mathbb{1}$ . We require the incoherent operators to fulfil  $\hat{K}_n\mathcal{I}\hat{K}_n^\dagger \subset \mathcal{I}$  for all  $n$  [16]. This definition guarantees that in an overall quantum operation  $\hat{\varrho}\mapsto \sum_{n}\hat{K}_{n}\hat{\varrho}\hat{K}_{n}^{\dagger}$ , even if one does not have access to individual outcomes  $n$ , no observer (e.g., one who does have access to these outcomes) would conclude that coherence has been generated from an incoherent state. Hence, we do not allow, not even probabilistically, that in any of the arms of the quantum operation coherence is generated from incoherent input states.

We distinguish two classes of quantum operations. (A) The incoherent completely positive and trace preserving quantum operations  $\Phi_{\mathrm{ICPTP}}$ , which act as  $\Phi_{\mathrm{ICPTP}}(\hat{\varrho}) = \sum_{n}\hat{K}_{n}\hat{\varrho}\hat{K}_{n}^{\dagger}$ , where the Kraus operators  $\hat{K}_n$  are all of the same dimension  $d_{\mathrm{out}}\times d_{\mathrm{in}}$  and satisfy  $\hat{K}_n\mathcal{I}\hat{K}_n^\dagger \subset \mathcal{I}$ . Note that this formulation of quantum operations implies the loss of information about the measurement outcome which may, however, be available in principle.

This leads us to the second class of operations. (B) Quantum operations for which measurement outcomes are retained (depending on the context, called measuring, selective, or stochastic operations) and, therefore, permit

subselection according to these measurement outcomes. These are also defined by Kraus operators  $\hat{K}_n$  with  $\sum_{n}\hat{K}_{n}^{\dagger}\hat{K}_{n} = \mathbb{1}$ , which now, however, may each have a different output dimension ( $\hat{K}_n$  is a  $d_n\times d_{\mathrm{in}}$  matrix) and are again required to fulfil  $\hat{K}_n\mathcal{I}\hat{K}_n^\dagger \subset \mathcal{I}$  for each  $n$ . Retaining the knowledge of outcomes of the measurement, the state corresponding to outcome  $n$  is given by  $\hat{q}_n = \hat{K}_n\hat{\varrho}\hat{K}_n^\dagger /p_n$  and occurs with probability  $p_n = \mathrm{tr}[\hat{K}_n\hat{\varrho}\hat{K}_n^\dagger ]$ .

Incoherent Kraus operators that are of particular importance for decoherence mechanisms of single qubits are, e.g., the ones that define the depolarizing, the phasedamping, and the amplitude-damping channels [17,18]. Moreover, permutations of modes of dual-rail qubits in linear optics experiments are examples of incoherent operations. With this, we set the framework for a resource theory for quantum coherence. All that follows is deduced from these physically well motivated definitions.

Maximally coherent state. We start by identifying a  $d$ -dimensional maximally coherent state as a state that allows for the deterministic generation of all other  $d$ -dimensional quantum states by means of incoherent operations. Note that this definition (i) is independent of a specific measure for the coherence and (ii) allows us to identify a unit for coherence to which all measures may be normalized. A maximally coherent state is given by

$$
| \Psi_ {d} \rangle := \frac {1}{\sqrt {d}} \sum_ {i = 1} ^ {d} | i \rangle , \tag {4}
$$

because by means of incoherent operations [of type (A) or (B)] alone, any  $d \times d$  state  $\hat{Q}$  may be prepared from  $|\Psi_d\rangle$  with certainty. We show this by explicitly constructing an incoherent operation that achieves the transformation in the Supplemental Material [19].

Two natural questions arise immediately. First, is this maximally coherent state a resource which, when consumed, allows for the generation of all other coherent operations by means of incoherent operations? We demonstrate in the Supplemental Material [19] that this is, indeed, the case: Provided with  $|\Psi_2\rangle$ , every unitary operation on a qubit may be implemented by incoherent operations. Second, one may ask whether incoherent operations introduce an order on the set of quantum states, i.e., whether, given two states  $\hat{\varrho}$  and  $\hat{\sigma}$ , either  $\hat{\varrho}$  can be transformed into  $\hat{\sigma}$  or vice versa. We have to leave this as an open question, but report small progress in the Supplemental Material [19], for which we note the analogy to the single copy conversion protocol for entangled pure states presented in [24,25].

Coherence measures. We now collect defining properties that any functional  $C$  mapping states to the nonnegative real numbers should satisfy in order for it to be a proper coherence measure. First of all, we demand that it vanishes on the set of incoherent states:  $(C1) C(\hat{\delta}) = 0$  for

all  $\hat{\delta} \in \mathcal{I}$ ; i.e., it should be zero for all incoherent states. One may also think of requiring a stronger condition:  $(C1')$ $C(\hat{\delta}) = 0$  iff  $\hat{\delta} \in \mathcal{I}$ , which implies nonzero  $C(\hat{\varrho})$  whenever  $\hat{\varrho}$  contains coherence. Obviously,  $(C1')$  implies  $(C1)$ .

Crucially, any proper coherence measure should not increase under incoherent operations of type (A) or (B): (C2a) Monotonicity under incoherent completely positive and trace preserving maps, i.e.,  $C(\hat{\varrho}) \geq C\big(\Phi_{\mathrm{ICPTP}}(\hat{\varrho})\big)$  for all  $\Phi_{\mathrm{ICPTP}}$ . Recall that this ignores the possibility of subselection based on measurement outcomes. Retaining measurement outcomes leads to: (C2b) Monotonicity under selective measurements on average, i.e.,  $C(\hat{\varrho}) \geq \sum_{n} p_{n} C(\hat{\varrho}_{n})$  for all  $\{\hat{K}_n\}$  with  $\sum_{n} \hat{K}_n^\dagger \hat{K}_n = \mathbb{1}$  and  $\hat{K}_n \mathcal{I} \hat{K}_n^\dagger \subset \mathcal{I}$ .

It should be noted that, besides the requirement of monotony under operations of type (A) and (B), one may argue that subselection based on measurement outcomes is described by adding a classical flag to the relevant quantum states  $\hat{\varrho}_n$ , which introduces a third monotonicity requirement. We further comment on this in the Supplemental Material [19], where we show that the relative entropy of coherence and the  $l_{1}$  norm of coherence are also monotonic under these operations, further strengthening their pivotal role.

Ideally, one would like to identify measures that fulfil both conditions (C2a) and (C2b). We would consider monotonicity under (C2b) more important as it allows for subselection, a process available in well controlled quantum experiments. We will see, however, that (C2b) is often harder to verify while (C2a) is automatically satisfied for a wide class of coherence measures.

Moreover, from a physical point of view, one would like to ensure that coherence can only decrease under mixing. This leads to our final condition: (C3) Nonincreasing under mixing of quantum states (convexity), i.e.,  $\sum_{n}p_{n}C(\hat{\varrho}_{n})\geq C(\sum_{n}p_{n}\hat{\varrho}_{n})$  for any set of states  $\{\hat{\varrho}_n\}$  and any  $p_n\geq 0$  with  $\sum_{n}p_{n} = 1$

Now, coherence measures that satisfy conditions (C2b) and (C3) imply condition (C2a)—again, highlighting the importance of (C2b). This can be seen as follows:

$$
C \big (\Phi_ {\mathrm {I C P T P}} (\hat {\varrho}) \big) = C \Bigg (\sum_ {n} p _ {n} \hat {\varrho} _ {n} \Bigg) ^ {(C 3)} \leq \sum_ {n} p _ {n} C \big (\hat {\varrho} _ {n} \big) ^ {(C 2 \mathrm {b})} \leq C (\hat {\varrho}).
$$

In the following, we study natural candidates for coherence measures. All are based on distance measures.

Distance measures.-For any distance measure between quantum states  $\mathcal{D}$ , we may define candidate coherence measures by

$$
C _ {\mathcal {D}} (\hat {\varrho}) = \min  _ {\hat {\delta} \in \mathcal {I}} \mathcal {D} (\hat {\varrho}, \hat {\delta}), \tag {5}
$$

i.e., the minimal distance (in the sense of  $\mathcal{D}$ ) of  $\hat{q}$  to the set of incoherent quantum states  $\mathcal{I}$ . By definition,  $(C1')$  is

automatically fulfilled for all  $\mathcal{D}$  with  $\mathcal{D}(\hat{\varrho},\hat{\delta}) = 0$  iff  $\hat{\varrho} = \hat{\delta}$ , which holds, e.g., if  $\mathcal{D}$  is a metric.

In analogy to the theory of entanglement [26], we may immediately identify an entire class of distance measures  $\mathcal{D}$  for which  $C_{\mathcal{D}}$  fulfils (C2a): Whenever  $\mathcal{D}$  is contracting under CPTP maps, i.e., such that  $\mathcal{D}(\hat{\varrho},\hat{\sigma})\geq \mathcal{D}(\Phi_{\mathrm{CPTP}}(\hat{\varrho}),$ $\Phi_{\mathrm{CPTP}}(\hat{\sigma}))$  for any completely positive trace preserving map  $\Phi_{\mathrm{CPTP}}$ , it induces a functional fulfilling (C2a) as then

$$
\begin{array}{l} C _ {\mathcal {D}} (\hat {\varrho}) = \mathcal {D} (\hat {\varrho}, \hat {\delta} _ {*}) \geq \mathcal {D} \left(\Phi_ {\mathrm {I C P T P}} (\hat {\varrho}), \Phi_ {\mathrm {I C P T P}} (\hat {\delta} _ {*})\right) \\ \geq \min  _ {\hat {\delta} \in \mathcal {I}} \mathcal {D} \left(\Phi_ {\mathrm {I C P T P}} (\hat {\varrho}), \hat {\delta}\right) = C _ {\mathcal {D}} \left(\Phi_ {\mathrm {I C P T P}} (\hat {\varrho})\right), \tag {6} \\ \end{array}
$$

where we used that  $\Phi_{\mathrm{ICPTP}}(\mathcal{I})\subset \mathcal{I}$  and denoted by  $\hat{\delta}_{*}$  the incoherent state minimizing the distance to  $\hat{\varrho}$ .

Whenever  $\mathcal{D}$  is jointly convex, the induced coherence monotone  $C_{\mathcal{D}}$  fulfils condition (C3)

$$
\begin{array}{l} C _ {\mathcal {D}} \left(\sum_ {n} p _ {n} \hat {\varrho} _ {n}\right) \leq \mathcal {D} \left(\sum_ {n} p _ {n} \hat {\varrho} _ {n}, \sum_ {n} p _ {n} \hat {\delta} _ {n} ^ {*}\right) \\ \leq \sum_ {n} p _ {n} \mathcal {D} \left(\hat {q} _ {n}, \hat {\delta} _ {n} ^ {*}\right) = \sum_ {n} p _ {n} C _ {\mathcal {D}} \left(\hat {q} _ {n}\right), \tag {7} \\ \end{array}
$$

where, for all  $n$ ,  $\hat{\delta}_n^*$  minimizes the distance to  $\hat{Q}_n$ . If  $\mathcal{D}(\hat{\varrho},\hat{\delta}) = \| \hat{\varrho} -\hat{\delta}\|$  with  $\| \cdot \|$  any matrix norm, (C3) is automatically implied by the triangle inequality and absolute homogeneity.

Condition (C2b) seems to be much harder to decide. A good starting point for showing (C2b) would be to check whether  $\mathcal{D}$  fulfils the conditions given in Ref. [6]. We proceed by considering specific examples.

Relative entropy of coherence. Consider the quantum relative entropy,  $S(\hat{q} \| \hat{\sigma}) = \mathrm{tr}[\hat{q}\log (\hat{q})] - \mathrm{tr}[\hat{q}\log (\hat{\sigma})]$ , and denote the induced measure by  $C_{\mathrm{rel,ent}}$ . It clearly fulfils (C1) and also (C1'). Further, it is known that the relative entropy is contracting under CPTP maps and jointly convex [27,28]; i.e.,  $C_{\mathrm{rel,ent}}$  satisfies (C2a) and (C3). It also fulfils (C2b), which can be shown following the approach of [6] for general selective measurements (see the Supplemental Material [19]). In addition to fulfilling all our requirements for a coherence measure,  $C_{\mathrm{rel,ent}}$  permits a closed form solution, avoiding the minimization: Let  $\hat{\delta} = \sum_{i}\delta_{i}|i\rangle \langle i|\in \mathcal{I}$  and for given  $\hat{q} = \sum_{i,j}\varrho_{i,j}|i\rangle \langle j|$  denote  $\hat{q}_{\mathrm{diag}} = \sum_{i}\varrho_{i,i}|i\rangle \langle i|$ . Then,  $S(\hat{q}\| \hat{\delta}) = S(\hat{q}_{\mathrm{diag}}) - S(\hat{q}) + S(\hat{q}_{\mathrm{diag}}\| \hat{\delta})$ , and hence,

$$
C _ {\text {r e l . e n t .}} (\hat {q}) = S (\hat {q} _ {\text {d i a g}}) - S (\hat {q}). \tag {8}
$$

Employing this formula, we can easily find the maximum possible value of coherence in a state: For any state  $\hat{\varrho}$ , one has  $C_{\mathrm{rel. ent.}}(\hat{\varrho}) \leq S(\hat{\varrho}_{\mathrm{diag}}) \leq \log(d)$  and this bound is attained for the maximally coherent state defined above. Note that this relative entropy measure was also considered in similar contexts such as, e.g., to quantify superposition

and frameness [29-34]. Notably, monotonicity of  $C_{\mathrm{rel.ent}}$  under (C2a) is a special case of a result of Ref. [29].

$l_{p}$  norms.-A very intuitive quantification of coherence would certainly be related to the off-diagonal elements of the considered quantum state. Therefore, quantifying the coherence by a functional depending on the off-diagonal elements is desirable. A widely used quantifier of coherence is given by

$$
C _ {l _ {1}} (\hat {\varrho}) = \sum_ {\substack {i, j \\ i \neq j}} | \varrho_ {i, j} |. \tag{9}
$$

But is it a proper coherence measure in the sense of  $(C1) - (C3)$ ? If so, it would constitute another intuitive coherence monotone with an easy closed form. It is the measure induced by the  $l_{1}$  matrix norm [35],  $\mathcal{D}_{l_1}(\hat{\varrho},\hat{\delta}) =$ $\| \hat{\varrho} -\hat{\delta}\|_{l_1} = \sum_{i,j}|\varrho_{i,j} - \delta_{i,j}|$ , and as such fulfils  $(C1^{\prime})$  and  $(C3)$ . What is more, (C2b) can be shown directly (see the Supplemental Material [19]) such that (C2a) is implied (see the discussion above). Hence, the  $l_{1}$  norm of coherence, together with the relative entropy of coherence, are the most general coherence monotones established in this Letter.

One may now ask whether measures induced by other  $l_{p}$  matrix norms serve as proper coherence monotones as well. For instance, consider the measure induced by the squared Hilbert-Schmidt norm; that is

$$
C _ {l _ {2}} (\hat {\varrho}) = \min  _ {\hat {\delta} \in \mathcal {I}} \| \hat {\varrho} - \hat {\delta} \| _ {l _ {2}} ^ {2} = \sum_ {\substack {i, j \\ i \neq j}} | \varrho_ {i, j} | ^ {2}. \tag{10}
$$

In the Supplemental Material [19], we show that  $C_{l_2}$  does not satisfy (C2b), i.e., that there are incoherent operations of type (B), under which  $C_{l_2}$  increases. This shows that care must be taken when quantifying coherence: While  $C_{l_2}$  might intuitively seem like a good candidate due to its simple structure related to the off-diagonal elements of the quantum state, it does not constitute a valid coherence monotone.

We discuss other potential candidates such as the measures induced by the fidelity and trace norm in the Supplemental Material [19].

Outlook.—In the preceding, we have provided the foundations for a theory of coherence as a resource as well as first results specifically concerning the quantification of coherence. Completion of this theory is a sizeable task that requires a thorough consideration of the questions of the manipulation, quantification, and exploitation of coherence under this resource viewpoint.

In this Letter, we have determined the notion of a maximally coherent state, but we have not yet provided a full theory of the interconversion of coherent states by means of incoherent operations. This has two principal aspects. On the one hand, the setting of single copies of coherent states is of considerable interest from the practical point of view as this is most readily accessible in the laboratory. We expect that a theory can be established that

proceeds along analogous developments in entanglement theory. There, the concept of majorization provided the relevant structure that determined the interconvertibility of states [24,25,36] and enabled the exploration of concepts such as catalysis [37]. Some progress in this direction has been reported in Ref. [38] for a specific setup but with a different class of allowed quantum operations. Whether such a phenomenon also occurs for this resource theory of coherence or whether a total order on quantum states can be established needs to be explored.

On the other hand, the asymptotic limit of infinitely many identically prepared copies of a coherent state and its interconversion by incoherent operations is of interest as it may provide a link to thermodynamical concepts such as the second law [7,8,39], by enabling reversible interconversion of coherent resources and, by invoking natural continuity requirements such as asymptotic continuity [40], it may lead to the identification of a unique coherence measure. The latter we expect to be realized by the relative entropy of coherence in close analogy to the development in entanglement theory [7,8]. Reference [34] takes steps in this direction and provides a thermodynamic interpretation of the relative entropy measure of coherence in the context of thermodynamic equilibria for decoherence processes.

A second aspect of the manipulation of coherence concerns its exploitation as a resource when only incoherent operations and a supply of coherent states is available [38,41]. In a first step, we have demonstrated that any (coherent) unitary operation can be realized in this fashion. The resource optimal protocols and the generation of the most general quantum operation from these resources has not yet been established. This in turn motivates questions such as the coherence cost of quantum operations and the dual question of coherence power of operations, again closely mirroring analogous developments in entanglement theory [41,42].

It is likely that each of the three lines of enquiry above will lead to the definition of sensible and good coherence measures, each of which will be related to the efficiency of certain coherence transformations. This will then provide a well rounded picture of the quantification of coherence as a resource.

All of the considerations above implicitly assumed the finite dimensional setting, but this is neither necessary nor desirable as there are very relevant physical situations that require infinite dimensional systems for their description. Most notable the quantum states of light, that is quantum optics, with its bosonic character requires infinite dimensional systems, harmonic oscillators, for their description. Hence, a quantum theory of coherence in infinite dimensional systems is needed. Again, closely mirroring the development of entanglement theory mathematical problems concerning continuity that are inevitably emerging can be addressed by requiring energy constraints [43] or by considering special, experimentally relevant, subclasses such as Gaussian states [44].

Conclusions.-In this Letter, we introduced the notion of incoherent states (in a fixed basis) which then allowed us to identify incoherent operations [45]. We explicitly distinguished between incoherent operations (A) with and (B) without subselection and established the maximally coherent state as the element from which all quantum states (mixed or pure) can be generated only by means of these operations [either type (A) or type (B)]. We gave a set of properties which every proper measure of coherence should satisfy and identified the relative entropy of coherence and the  $l_{1}$  norm of coherence as the most general and easy to use quantifiers. The questions that we formulated in the outlook of this work are of considerable interest to complete this resource theory of coherence.

We acknowledge discussions with Susana Huelga that helped to motivate the development of the present work, and discussions with Nathan Killoran and Robert Spekkens. This work was supported by the Alexander von Humboldt Foundation, the EU Integrating Project SIQS, the EU STREP PAPETS, and the BMBF Verbundprojekt QuoReP.

Note added.-Recently, we became aware of the related Ref. [46], in which questions of monotonicity under incoherent operations are also discussed.

[1] R.J. Glauber, Phys. Rev. 131, 2766 (1963).  
[2] E. C. G. Sudarshan, Phys. Rev. Lett. 10, 277 (1963).  
[3] S. F. Huelga and M. B. Plenio, Contemp. Phys. 54, 181 (2013).  
[4] C. H. Bennett (private communication).  
[5] M. B. Plenio and S. Virmani, Quantum Inf. Comput. 7, 1 (2007).  
[6] V. Vedral and M. B. Plenio, Phys. Rev. A 57, 1619 (1998).  
[7] F. G. S. L. Brandão and M. B. Plenio, Nat. Phys. 4, 873 (2008).  
[8] F. G. S. L. Brandão and M. B. Plenio, Commun. Math. Phys. 295, 829 (2010).  
[9] I. Devetak, A. W. Harrow, and A. J. Winter, IEEE Trans. Inf. Theory 54, 4587 (2008).  
[10] M. Horodecki and J. Oppenheim, Int. J. Mod. Phys. B 27, 1345019 (2013).  
[11] F. G. S. L. Brandão, M. Horodecki, J. Oppenheim, J. M. Renes, and R. W. Spekkens, Phys. Rev. Lett. 111, 250404 (2013).  
[12] G. Gour, M. P. Müller, V. Narasimhachar, R. W. Spekkens, and N. Yunger Halpern, arXiv:1309.6586.  
[13] G. Gour and R. W. Spekkens, New J. Phys. 10, 033023 (2008); I. Marvian and R. W. Spekkens, New J. Phys. 15, 033001 (2013).  
[14] Note that we do not specify the Hilbert space structure. In particular,  $\mathcal{H}$  may describe compound quantum systems, e.g.,  $\mathcal{H} = \mathbb{C}^2\otimes \ldots \otimes \mathbb{C}^2$  for a set of qubits.  
[15] To simplify notation, we do not specify the dimension  $d$ ; the context should make this unambiguous.

[16] Note the close relation to  $\mathrm{U}(1)$ -covariant operations considered in the resource theory of reference frames [13]. These operations are incoherent in the sense that they map diagonal states to diagonal states; they are, however, a smaller set of operations, in particular, they do not allow for certain permutations.  
[17] M. Avalle and A. Serafini, Phys. Rev. Lett. 112, 170403 (2014).  
[18] J. Preskill, "Quantum Information and Computation," California Institute of Technology, 1998 (unpublished).  
[19] See the Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.113.140401, which includes Refs. [20,21,22,23], for proofs and further information.  
[20] A. Uhlmann, Rep. Math. Phys. 9, 273 (1976).  
[21] H. Barnum, C.M. Caves, C.A. Fuchs, R. Jozsa, and B. Schumacher, Phys. Rev. Lett. 76, 2818 (1996).  
[22] J. A. Miszczak, Z. Puchala, P. Horodecki, A. Uhlmann, and K. Zyczkowski, Quantum Inf. Comput. 9, 103 (2009).  
[23] D. Pérez-García, M. M. Wolf, D. Petz, and M. B. Ruskai, J. Math. Phys. (N.Y.) 47, 083506 (2006).  
[24] G. Vidal, Phys. Rev. Lett. 83, 1046 (1999).  
[25] D. Jonathan and M. B. Plenio, Phys. Rev. Lett. 83, 1455 (1999).  
[26] V. Vedral, M. B. Plenio, M. A. Rippin, and P. L. Knight, Phys. Rev. Lett. 78, 2275 (1997).  
[27] G. Lindblad, Commun. Math. Phys. 40, 147 (1975).  
[28] M. B. Ruskai, J. Math. Phys. (N.Y.) 43, 4358 (2002).  
[29] J. Åberg, arXiv:quant-ph/0612146.  
[30] G. Gour, I. Marvian, and R. W. Spekkens, Phys. Rev. A 80, 012307 (2009).  
[31] M. Horodecki, P. Horodecki, R. Horodecki, J. Oppenheim, A. Sen, U. Sen, and B. Synak-Radtke, Phys. Rev. A 71, 062307 (2005).  
[32] J. A. Vaccaro, F. Anselmi, H. M. Wiseman, and K. Jacobs, Phys. Rev. A 77, 032114 (2008).  
[33] R. M. Angelo and A. D. Ribeiro, arXiv:1304.2286.  
[34] C. A. Rodríguez-Rosario, T. Frauenheim, and A. Aspuru-Guzik, arXiv:1308.1245.  
[35] R. A. Horn and C. R. Johnson, Matrix Analysis (Cambridge University Press, Cambridge, England, 1991).  
[36] M. A. Nielsen, Phys. Rev. Lett. 83, 436 (1999).  
[37] D. Jonathan and M. B. Plenio, Phys. Rev. Lett. 83, 3566 (1999).  
[38] J. Åberg, arXiv:1304.1060.  
[39] S. Popescu and D. Rohrlich, Phys. Rev. A 56, R3319 (1997).  
[40] G. Vidal, J. Mod. Opt. 47, 355 (2000).  
[41] J. Eisert, K. Jacobs, P. Papadopoulos, and M. B. Plenio, Phys. Rev. A 62, 052317 (2000).  
[42] P. Zanardi, C. Zalka, and L. Faoro, Phys. Rev. A 62, 030301 (2000).  
[43] J. Eisert, C. Simon, and M. B. Plenio, J. Phys. A 35, 3911 (2002).  
[44] J. Eisert and M. B. Plenio, Int. J. Quantum. Inform. 01, 479 (2003).  
[45] The incoherent states discussed in this Letter may be regarded as fully incoherent—opposed to block diagonal structures that have, for example, been considered in Ref. [29]. Notably, for given nontrivial subspaces, the quantum operations that leave the fully incoherent states and the block diagonal structures invariant are not subsets of one another.  
[46] F. Levi and F. Mintert, New J. Phys. 16, 033007 (2014).