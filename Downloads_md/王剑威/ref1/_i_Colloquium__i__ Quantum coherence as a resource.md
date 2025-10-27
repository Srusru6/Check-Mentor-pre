# Colloquium: Quantum coherence as a resource

Alexander Streltsov*

Faculty of Applied Physics and Mathematics, Gdańsk University of Technology, 80-233 Gdańsk, Poland,

National Quantum Information Centre in Gdańsk, 81-824 Sopot, Poland

Dahlem Center for Complex Quantum Systems, Freie Universität Berlin,

D-14195 Berlin, Germany

and ICFO—Institut de Ciencies Fotòniques, The Barcelona Institute of Science and

Technology, ES-08860 Castelldefels, Spain

Gerardo Adesso

Centre for the Mathematics and Theoretical Physics of Quantum Non-Equilibrium Systems

(CQNE), School of Mathematical Sciences, The University of Nottingham,

University Park, Nottingham NG7 2RD, United Kingdom

Martin B. Plenio‡

Institute of Theoretical Physics and IQST, Ulm University,

Albert-Einstein-Allee 11, D-89069 Ulm, Germany

(published 30 October 2017)

The coherent superposition of states, in combination with the quantization of observables, represents one of the most fundamental features that mark the departure of quantum mechanics from the classical realm. Quantum coherence in many-body systems embodies the essence of entanglement and is an essential ingredient for a plethora of physical phenomena in quantum optics, quantum information, solid state physics, and nanoscale thermodynamics. In recent years, research on the presence and functional role of quantum coherence in biological systems has also attracted considerable interest. Despite the fundamental importance of quantum coherence, the development of a rigorous theory of quantum coherence as a physical resource has been initiated only recently. This Colloquium discusses and reviews the development of this rapidly growing research field that encompasses the characterization, quantification, manipulation, dynamical evolution, and operational application of quantum coherence.

DOI: 10.1103/RevModPhys.89.041003

# CONTENTS

I. Introduction 2

II. Resource Theories of Quantum Coherence 3

A. Constraints, operations, and resources 3

1.Incoherent states 4  
2.Classes of incoherent operations 4

B. Coherence as a resource 6

1. Maximally coherent states and state transformations via incoherent operations 6  
2. States and maps 7

C. Quantum coherence in distributed scenarios 7  
D. Connection between coherence and entanglement theory 8

III. Quantifying Quantum Coherence 9

A. Postulates for coherence monotones and measures 9  
B. Distillable coherence and coherence cost 10  
C. Distance-based quantifiers of coherence 10  
1. Relative entropy of coherence 11

2. Coherence quantifiers based on matrix norms 11  
3. Geometric coherence 12

D. Convex roof quantifiers of coherence 12  
E. Coherence monotones from entanglement 13  
F. Robustness of coherence 13  
G. Coherence quantifiers from interferometric visibility 14  
H. Coherence of assistance 14

I. Coherence and quantum correlations beyond entanglement 15

J. Coherence in continuous variable systems 15  
K. Coherence, asymmetry, and nonclassicality 16

1. Asymmetry monotones 16  
2. Quantifying superpositions 17

3. Coherence rank and general quantifiers of nonclassicality 17  
4. Optical coherence and nonclassicality 17

L. Multipartite settings 18

1. General distance-based coherence quantifiers 18  
2.Quantum-incoherent relative entropy 18  
3. Distillable coherence of collaboration 19  
4. Recoverable coherence 19  
5. Uncertainty relations and monogamy of coherence 19

IV. Dynamics of Quantum Coherence 20

A. Freezing of coherence 20

B. Coherence in non-Markovian evolutions 21

C. Cohering power of quantum channels and evolutions 21

D. Average coherence of random states and typicality 22

1. Average relative entropy of coherence 22  
2. Average  $l_{1}$  norm of coherence 23  
3. Average recoverable coherence 23

E.Quantum speed limits 23

V. Applications of Quantum Coherence 24

A.Quantum thermodynamics 24

1. Thermal operations 24  
2. State transformations via thermal operations 25  
3. Work extraction and quantum thermal machines 25

B.Quantum algorithms 26  
C.Quantum metrology 26  
D.Quantum channel discrimination 27  
E. Witnessing quantum correlations 27  
F.Quantum biology and transport phenomena 28  
G.Quantum phase transitions 28

VI. Conclusions 29

Acknowledgments 29

References 30

# I. INTRODUCTION

Coherence marks the departure of today's theories of the physical world from the principles of classical physics. The theory of electromagnetic waves, which may exhibit optical coherence and interference, represents a radical departure from classical ray optics. Energy quantization and the rise of quantum mechanics as a unified picture of waves and particles in the early part of the 20th century have further amplified the prominent role of coherence in physics. Indeed, by combination of energy quantization and the tensor product structure of the state space, coherence underlies phenomena such as quantum interference and multipartite entanglement that play a central role in the applications of quantum physics and quantum information science.

The investigation and exploitation of coherence of quantum optical fields has a long-standing history. It has enabled the realization of now mature technologies, such as the laser and its applications, that are often classified as "Quantum Technologies 1.0" as they rely mainly on single particle coherence. At the mathematical level the coherence of quantum optical fields is described in terms of phase space distributions and multipoint correlation functions, approaches that find their roots in classical electromagnetic theory (Glauber, 1963; Sudarshan, 1963; Mandel and Wolf, 1965).

However, quantum coherence is not restricted to optical fields. More importantly, as the key ingredient that drives quantum technologies, it is highly desirable to be able to precisely quantify the usefulness of coherence as a resource for such applications. These pressing questions are calling for further development of the theory of quantum coherence.

The emergence of quantum information science over the last three decades has, among other insights, led to a reassessment of quantum physical phenomena as resources that may be exploited to achieve tasks that are otherwise not possible within the realm of classical physics. This resource-driven viewpoint has motivated the development of a quantitative theory that captures the resource character of physical traits in a mathematically rigorous fashion.

In a nutshell, any such theory first considers constraints that are imposed on us in a specific physical situation (e.g., the inability to perform joint quantum operations between distant laboratories due to the impossibility to transfer quantum systems from one location to the other while preserving their quantum coherence, and thus restricting us to local operations and classical communication). Executing general quantum operations under such a constraint then requires quantum states that contain a relevant resource (e.g., entangled states that are provided to us at a certain cost) and can be consumed in the process. The formulation of such resource theories was in fact initially pursued with the quantitative theory of entanglement (Plenio and Virmani, 2007; Horodecki et al., 2009) but has since spread to encompass a wider range of operational settings (Horodecki and Oppenheim, 2013b; del Rio, Kraemer, and Renner, 2015; Coecke, Fritz, and Spekkens, 2016).

The theory of quantum coherence as a resource is a case in point. Following an early approach to quantifying superpositions of orthogonal quantum states by Åberg (2006) and progressing alongside the independent yet related resource theory of asymmetry (Gour and Spekkens, 2008; Vaccaro et al., 2008; Gour, Marvian, and Spekkens, 2009; Marvian and Spekkens, 2014a, 2014b), a resource theory of coherence was primarily proposed by Baumgratz, Cramer, and Plenio (2014) and Levi and Mintert (2014) and further developed by Chitambar and Gour (2016a, 2016b, 2017), Winter and Yang (2016), and Yadin et al. (2016). Such a theory asks the question what can be achieved and at what resource cost when the devices that are available to us are essentially classical, that is, they cannot create coherence in a preferred basis. This analysis, currently still under development, endeavors to provide a rigorous framework to describe quantum coherence in analogy with what has been done for quantum entanglement and other nonclassical resources (Plenio and Virmani, 2007; Horodecki et al., 2009; Modi et al., 2012; Horodecki and Oppenheim, 2013b; Sperling and Vogel, 2015; Streltsov, 2015; Adesso, Bromley, and Cianciaruso, 2016). Within such a framework, recent progress has shown that a growing number of applications can be certified to rely on various incarnations of quantum coherence as a primary ingredient, and appropriate figures of merit for such applications can be precisely linked back to specific coherence monotones, providing operational interpretations for the latter.

These applications include so-called "Quantum Technologies 2.0," such as quantum-enhanced metrology and communication protocols, and extend farther into other fields, such as thermodynamics and even certain branches of biology. Beyond such application-driven viewpoints, which may provide new insights into all these areas, one can also consider the theory of coherence as a resource as a novel approach toward the demarcation of the fundamental difference between classical and quantum physics in a quantitative manner: a goal that may eventually lead to a better understanding of the classical-quantum boundary.

This Colloquium collected the most up-to-date knowledge on coherence in single and composite quantum systems from a modern information theory perspective. We reviewed this fascinating and fundamental subject in an accessible manner, yet without compromising any rigor.

![](images/7ed27d208ce7e9551c3e3b4b252efe133ba3c89c3f50df5ae2fe356562c90ef1.jpg)  
FIG. 1. Plan of the Colloquium. (Top) Sec. II: Resource theories of quantum coherence; the inset depicts a comparison between some classes of incoherent operations. Adapted from Chitambar and Gour, 2016b. (Right) Sec. III: Quantifying quantum coherence; the inset depicts the construction of coherence monotones from entanglement. Adapted from Streltsov et al., 2015. (Bottom) Sec. IV: Dynamics of quantum coherence; the inset depicts an illustration of coherence freezing under local incoherent channels. Adapted from Bromley, Cianciaruso, and Adesso, 2015. (Left) Sec. V: Applications of quantum coherence; the insets depicts a schematic of a quantum phase discrimination protocol. Adapted from Napoli et al., 2016. The Introduction (Sec. I) and Conclusions (Sec. VI) complete the Colloquium.

The Colloquium is organized as follows (see Fig. 1). Section II gives a comprehensive overview of recent developments to construct a resource theory of quantum coherence, including a hierarchy of possible classes of incoherent operations, and the conditions to which any valid coherence quantifier should abide. It also discusses established links with other resource theories, most prominently those of asymmetry and quantum entanglement. Section III presents a compendium of recently proposed monotones and measures of quantum coherence, based on different physical approaches endowed with different mathematical properties, in single and multipartite systems; interplays with other measures of non-classicality are highlighted as well. Section IV reviews the phenomenology of quantum coherence in the dynamical evolution of open quantum systems, further reporting results on the average coherence of random states, and on the cohering power of quantum channels. Section V focuses on the plethora of applications and operational interpretations highlighted so far for quantum coherence in thermodynamics, interference phenomena, quantum algorithms, metrology and discrimination, quantum biology, many-body physics, and the detection of quantum correlations. Section VI concludes with a summary and discussion of some currently open issues in the theoretical description of coherence and its role in quantum physics and beyond.

We emphasize that, due to limitations in space and focus, this Colloquium cannot cover all ramifications of the concept of quantum coherence. It is nevertheless our expectation that this Colloquium, while being self-contained, can stimulate the interested reader to undertake further research toward achieving a fully satisfactory and physically consistent characterization of the wide-interest topic of coherence as a resource in quantum systems of arbitrary dimensions. This, we hope, may also lead to the formulation of novel direct applications of coherence (or an optimization of existing ones) in a variety of physical and biological contexts of high technological interest.

# II. RESOURCE THEORIES OF QUANTUM COHERENCE

Coherence is a property of the physical world that is used to drive a wide variety of phenomena and devices. Hence coherence adopts the quality of a resource, as it may be provided at a certain cost, manipulated by otherwise incoherent means and consumed to achieve useful tasks. The quantitative study of these processes and their attainable efficiencies requires careful definitions of the accessible operations and gives rise to a framework that has become known as a resource theory. In line with earlier developments in quantum information science, for example, in the context of entanglement (Vedral and Plenio, 1998; Plenio and Virmani, 2007; Brandão and Plenio, 2008, 2010; Horodecki et al., 2009), quantum thermodynamics (Ruch, 1975; Janzing et al., 2000; Brandão et al., 2013; Gour et al., 2015; Goold et al., 2016), purity (Horodecki, Horodecki, and Oppenheim, 2003), and reference frames (Gour and Spekkens, 2008; Gour, Marvian, and Spekkens, 2009; Marvian and Spekkens, 2014a), the formulation of the resource theory of coherence (Åberg, 2006; Baumgratz, Cramer, and Plenio, 2014; Levi and Mintert, 2014; Winter and Yang, 2016) extends the family of resources theories of knowledge (del Rio, Kraemer, and Renner, 2015).

# A. Constraints, operations, and resources

A resource theory is fundamentally determined by constraints that are imposed on us and which determine the set of the freely accessible quantum operations  $\mathcal{F}$ . These constraints may be due to either fundamental conservation laws, such as superselection rules and energy conservation, or constraints due to the practical difficulty of executing certain operations, e.g., the restriction to local operations and classical communication (LOCC) which gives rise to the resource theory of entanglement (Plenio and Virmani, 2007; Horodecki et al., 2009).

The states that can be generated from the maximally mixed state<sup>1</sup> by the application of free operations in  $\mathcal{F}$  alone, are considered to be available free of charge, forming the set  $\mathcal{I}$  of free states. All the other states attain the status of a resource, whose provision carries a cost. These resource states may be

used to achieve operations that cannot be realized by using only members of  $\mathcal{F}$ . Alternatively, one may also begin by defining the set of free states  $\mathcal{I}$ , and then consider classes of operations that map this set into itself and use this to define  $\mathcal{F}$ . For the purposes of the present exposition of the resource theory of coherence, we begin by adopting the latter point of view and then proceed to require additional desirable properties of our classes of free operations.

# 1. Incoherent states

Coherence is naturally a basis dependent concept, which is why we first need to fix the preferred or reference basis in which to formulate our resource theory. The reference basis may be dictated by the physics of the problem under investigation (e.g., one may focus on the energy eigenbasis when addressing coherence in transport phenomena and thermodynamics) or by a task for which coherence is required (e.g., the estimation of a magnetic field in a certain direction within a quantum metrology setting). Given a  $d$ -dimensional Hilbert space  $\mathcal{H}$  (with  $d$  assumed finite, even though some extensions to infinite  $d$  can be considered), we denote its reference orthonormal basis by  $\{|i\rangle \}_{i = 0,\dots,d - 1}$ . The density matrices that are diagonal in this specific basis are called incoherent, i.e., they are accessible free of charge and form the set  $\mathcal{I} \subset \mathcal{B}(\mathcal{H})$ , where  $\mathcal{B}(\mathcal{H})$  denotes the set of all bounded trace class operators on  $\mathcal{H}$ . Hence, all incoherent density operators  $\varrho \in \mathcal{I}$  are of the form

$$
\varrho = \sum_ {i = 0} ^ {d - 1} p _ {i} | i \rangle \langle i | \tag {1}
$$

with probabilities  $p_i$ .

In the case of more than one party, the preferred basis with respect to which coherence is studied will be constructed as the tensor product of the corresponding local reference basis states for each subsystem. General multipartite incoherent states are then defined as convex combinations of such incoherent pure product states (Bromley, Cianciaruso, and Adesso, 2015; Streltsov et al., 2015; Winter and Yang, 2016).

For example, if the reference basis for a single qubit is taken to be the computational basis  $\{|0\rangle, |1\rangle\}$ , i.e., the eigenbasis of the Pauli  $\sigma_z$  operator, then any density matrix with a nonzero off-diagonal element  $|\varrho_{01}| = |\langle 0|\varrho |1\rangle| \neq 0$  is outside the set  $\mathcal{I}$  of incoherent states, and hence has a resource content. Similarly, for an  $N$ -qubit system, the set of incoherent states  $\mathcal{I}$  is formed by all and only the density matrices  $\varrho$  diagonal in the composite computational basis  $\{|0\rangle, |1\rangle\}^{\otimes N}$ , with any other state being coherent, that is, resourceful.

Note that some frameworks of coherence may allow for a larger set of free states. This is, in particular, the case for the resource theory of asymmetry (Gour and Spekkens, 2008; Gour, Marvian, and Spekkens, 2009; Marvian and Spekkens, 2014a, 2014b), where the set of free states is defined by all states which commute with a given Hamiltonian  $H$ . If the Hamiltonian is nondegenerate, the corresponding set of free states is exactly the set of incoherent states described, where the incoherent basis is defined by the eigenbasis of the Hamiltonian. However, the situation changes if the Hamiltonian has degeneracies, in which case any

superposition of the eigenstates corresponding to the degenerate subspaces is also considered as free. This has important implications in quantum thermodynamics as described in more detail in Sec. V.A. In the following, whenever we refer to incoherent states, we explicitly mean states of the form (1).

# 2. Classes of incoherent operations

The definition of free operations for the resource theory of coherence is not unique and different choices, often motivated by suitable practical considerations, are being examined in the literature. Here we present the most important classes and briefly discuss their properties and relations among each other.

We start with the largest class, the maximally incoherent operations (MIO) (Åberg, 2006) (also known as incoherence preserving operations), which are defined as any trace preserving completely positive and nonselective quantum operations  $\Lambda \colon \mathcal{B}(\mathcal{H}) \mapsto \mathcal{B}(\mathcal{H})$  such that

$$
\Lambda [ \mathcal {I} ] \subseteq \mathcal {I}. \tag {2}
$$

As with every quantum operation, this mathematically natural set of operations can also always be obtained by a Stinespring dilation, i.e., the provision of an ancillary environment in some state  $\sigma$ , a subsequent unitary operation  $U$  between system and environment, followed by the tracing out of the environment,

$$
\Lambda [ \varrho ] = \operatorname {T r} _ {E} [ U (\varrho \otimes \sigma) U ^ {\dagger} ]. \tag {3}
$$

If an operation can be implemented as in Eq. (3) by using an incoherent state  $\sigma$  of the environment and a global incoherent unitary  $U$  (a unitary that is diagonal in the preferred basis), we say that the operation has a free dilation. Note that despite the fact that MIO cannot create coherence, these operations in general do not have a free dilation<sup>2</sup> (Chitambar and Gour, 2016a, 2016b, 2017; Marvian and Spekkens, 2016).

A smaller and more relevant class of free operations for the theory of coherence is that of incoherent operations (IO) (B Baumgratz, Cramer, and Plenio, 2014) which are characterized as the set of trace preserving completely positive maps  $\Lambda \colon \mathcal{B}(\mathcal{H})\mapsto \mathcal{B}(\mathcal{H})$  admitting a set of Kraus operators such that  $\sum_{n}K_{n}^{\dagger}K_{n} = \mathbb{1}$  (trace preservation) and, for all  $n$  and  $\varrho \in \mathcal{I}$ ,

$$
\frac {K _ {n} Q K _ {n} ^ {\dagger}}{\operatorname {T r} \left[ K _ {n} Q K _ {n} ^ {\dagger} \right]} \in \mathcal {I}. \tag {4}
$$

This definition of IO ensures that, in any of the possible outcomes of such an operation, coherence can never be generated from an incoherent input state, not even

probabilistically. $^{4}$  Also this class of operations does not admit a free dilation in general (Chitambar and Gour, 2016a, 2016b, 2017; Marvian and Spekkens, 2016).

In the previous two definitions, the focus was placed on the inability of incoherent operations to generate coherence. One may, however, be more stringent by adding further desirable properties to the set of free operations. One such approach requires that admissible operations are not capable of making use of coherence in the input state. Defining the dephasing operation

$$
\Delta [ \varrho ] = \sum_ {i = 0} ^ {d - 1} | i \rangle \langle i | \varrho | i \rangle \langle i |, \tag {5}
$$

an operation  $\Lambda$  is called strictly incoherent (SIO) (Winter and Yang, 2016; Yadin et al., 2016) if it can be written in terms of a set of incoherent Kraus operators  $\{K_n\}$ , such that the outcomes of a measurement in the reference basis applied to the output are independent of the coherence of the input state, i.e.,

$$
\langle i | K _ {n} \varrho K _ {n} ^ {\dagger} | i \rangle = \langle i | K _ {n} \Delta [ \varrho ] K _ {n} ^ {\dagger} | i \rangle \tag {6}
$$

for all  $n$  and  $i$ . Equivalently, SIO can be characterized as those operations that have an incoherent Kraus decomposition  $\{K_n\}$  such that the operators  $K_{n}^{\dagger}$  are also incoherent (Winter and Yang, 2016; Yadin et al., 2016). As shown by Chitambar and Gour (2016a, 2016b, 2017), SIO in general do not admit a free dilation either. Nevertheless, a special type of dilation for SIO of the form (3) was provided by Yadin et al. (2016), which consists of (i) unitary operations on the environment controlled by the incoherent basis of the system  $\sum_{j}|j\rangle \langle j|\otimes U_{j}$  (ii) measurements on the environment in any basis, and (iii) incoherent unitary operations on the system conditioned on the measurement outcome  $\sum_{j}e^{i\theta_{j}}|\pi (j)\rangle \langle j|$ , with  $\{| \pi (j) \rangle \}$  denoting a permutation of the reference basis of the system.

The classes of operations defined so far include permutations of the reference basis states for free. This is natural when any such operation is considered from a passive point of view, amounting to a relabeling of the states. Viewed from an active point of view instead, i.e., asking for a unitary operation that realizes this permutation, it may be argued that such an operation does in fact cost coherence resources in order to be performed in the laboratory. This suggests that, from an operational point of view, permutations should be excluded from the free operations, as is done in the more stringent set of translationally invariant operations (TIO). The latter are defined as those commuting with phase randomization (Gour and Spekkens, 2008; Gour, Marvian, and Spekkens, 2009; Marvian and Spekkens, 2013, 2014a, 2014b, 2016; Marvian, Spekkens, and Zanardi, 2016). More precisely, given a Hamiltonian  $H$ , an operation  $\Lambda$  is translationally invariant with respect to  $H$  if it fulfills the condition (Gour, Marvian,

and Spekkens, 2009; Marvian and Spekkens, 2014a; Marvian, Spekkens, and Zanardi, 2016)

$$
e ^ {- i H t} \Lambda [ \varrho ] e ^ {i H t} = \Lambda [ e ^ {- i H t} \varrho e ^ {i H t} ]. \tag {7}
$$

TIO play an important role in the resource theory of asymmetry (see Sec. III.K.1) and quantum thermodynamics (see Sec. V.A). Interestingly, Marvian and Spekkens (2016) showed that TIO have a free dilation if one additionally allows postselection with an incoherent measurement on the environment.

As mentioned, the sets MIO, IO, and SIO in general do not have a free dilation, i.e., they cannot be implemented by coupling the system to an environment in an incoherent state followed by a global incoherent unitary. Motivated by this observation, Chitambar and Gour (2016a, 2016b, 2017) introduced the set of physical incoherent operations (PIO). These are all operations which can instead be implemented in the aforementioned way, additionally allowing for incoherent measurements on the environment and classical postprocessing of the measurement outcomes.

Clearly, MIO is the largest set of free operations for a resource theory of coherence, and all other sets listed are strict subsets of it. Inclusion relations between each of these sets are nontrivial in general. Here we mention that (see also Fig. 1, top panel)

$$
\mathrm {P I O} \subset \mathrm {S I O} \subset \mathrm {I O} \subset \mathrm {M I O}, \tag {8}
$$

and refer the interested reader to Chitambar and Gour (2016a, 2016b, 2017) and de Vicente and Streltsov (2017) for more detailed discussions.

Another interesting set is given by dephasing-covariant incoherent operations (DIO), which were introduced independently by Chitambar and Gour (2016a, 2016b, 2017) and Marvian and Spekkens (2016). These are all operations  $\Lambda$  which commute with the dephasing map Eq. (5), i.e.,  $\Lambda[\Delta[\varrho]] = \Delta[\Lambda[\varrho]]$ . It is an interesting open question whether DIO have a free dilation.

We also mention genuinely incoherent operations (GIO) and fully incoherent operations (FIO) (de Vicente and Streltsov, 2017). GIO are operations which preserve all incoherent states, i.e.,  $\Lambda[\varrho] = \varrho$  for any incoherent state  $\varrho$ . In particular, every GIO is incoherent regardless of the particular Kraus decomposition, i.e., for every experimental realization of the operation. Since GIO do not allow for transformations between different incoherent states, notably, for example, between the energy eigenstates (when coherence is measured with respect to the eigenbasis of the Hamiltonian of the system), they capture the framework of coherence in the presence of additional constraints, such as energy conservation. FIO are in turn the most general set of operations which are incoherent for every Kraus decomposition (de Vicente and Streltsov, 2017). The GIO framework is closely related to the concept of resource destroying maps introduced by Liu, Hu, and Lloyd (2017). The latter studies quantum operations which transform any quantum state onto a free state and moreover preserve all free states. If the set of free states is

taken to be incoherent, any such coherence destroying map is also GIO.

The role of energy in the context of coherence was also investigated by Chiribella and Yang (2015). In particular, Chiribella and Yang (2015) defined the class of energy preserving operations (EPO) as all operations which have a free dilation as in Eq. (3), with the additional requirement that the unitary commutes with the Hamiltonian of the system and environment individually. Note that the set of EPO is a strict subset of TIO (Chiribella and Yang, 2015).

That there is such a wide variety of possible definitions of incoherent operations should not come as a surprise as it mirrors the situation in entanglement theory where the set LOCC is operationally well defined, although mathematically cumbersome, while larger sets such as separable operations (Vedral and Plenio, 1998) and positive partial transpose preserving operations (Rains, 2001) have mathematically very convenient properties, but in general do require a finite amount of free entanglement for their implementation (Bennett et al., 1999). Nevertheless, they are very useful as they provide bounds on achievable efficiencies for transformations under the difficult to handle LOCC constraints. Equally, the wealth of definitions for alternative incoherent operations can be expected to provide both conceptual and quantitative insights into the properties of coherence as a resource.

A classification of the different frameworks of coherence, motivated by the notion of speakable and unspeakable information (Peres and Scudo, 2002; Bartlett, Rudolph, and Spekkens, 2007), was proposed by Marvian and Spekkens (2016). Speakable information includes any type of information for which the means of encoding is not relevant, while unspeakable information depends on the way of encoding. In general, a framework of coherence is speakable, if it allows for a free transformation between the states  $(|0\rangle + |1\rangle) / \sqrt{2}$  and  $(|0\rangle + |2\rangle) / \sqrt{2}$ . Otherwise, the framework of coherence is unspeakable (Marvian and Spekkens, 2016). In Table I we summarize the aforementioned frameworks of coherence according to this classification.

Before we move on, we want to discuss two possible extensions of incoherent operations which also apply to other classes that were already presented. First, motivated by observations in entanglement theory (Jonathan and Plenio, 1999), one might define the set of catalytic incoherent operations (Baumgratz, Cramer, and Plenio, 2014) by allowing for the use of an additional physical system of arbitrary dimension, the catalyst, in a state  $\eta$  which has to be returned unchanged after the transformation. That is, for arbitrary states  $\varrho$  and  $\sigma$  of the system and (bipartite) incoherent operations  $\Lambda$  we require

$$
\Lambda [ \varrho \otimes \eta ] = \sigma \otimes \eta . \tag {9}
$$

TABLE I. Classification of different frameworks of coherence into speakable and unspeakable types (Marvian and Spekkens, 2016).  

<table><tr><td></td><td colspan="6">Sets of free operations</td></tr><tr><td>Speakable coherence</td><td>FIO</td><td>PIO</td><td>SIO</td><td>IO</td><td>DIO</td><td>MIO</td></tr><tr><td>Unspeakable coherence</td><td>GIO</td><td>EPO</td><td>TIO</td><td></td><td></td><td></td></tr></table>

Indeed, in the theory of entanglement the addition of catalysts is known to confer additional power in that it makes possible state transformations that would otherwise be impossible under LOCC alone (Jonathan and Plenio, 1999). As shown by Bu, Singh, and Wu (2016), these results also hold in the resource theory of coherence: catalytic incoherent operations allow for pure state transformations which cannot be achieved with incoherent operations alone. The role of catalysts for the class TIO has also been discussed by Marvian and Spekkens (2013) and Marvian and Lloyd (2016).

Concerning the second possible extension, up until this point we have considered only exact state transformations, an idealization which, arguably, cannot be achieved in the real world. Hence, already from this practical consideration, one should also permit approximate state transformations such that, instead of the exact map  $\Lambda[\varrho] = \sigma$ , one would be satisfied with achieving  $\| \Lambda[\varrho] - \sigma \|_1 \leq \epsilon$  for some small  $\epsilon$ , where  $\| M \|_1 = \operatorname{Tr} \sqrt{M^\dagger M}$  denotes the trace norm. Beyond the mere practical motivation, allowing for approximate transformations has some relevance because it can considerably change the set of available state transformations. In particular, when permitting small errors to occur in catalysts their power may increase further, in fact so much that any state transformation may potentially become possible through embezzling of quantum states (van Dam and Hayden, 2003). Stronger constraints such as substituting  $\epsilon$  by  $\epsilon / \log D$  where  $D = \dim[\eta]$  and  $\eta$  is the state of the catalyst can prevent embezzling [see Brandão et al. (2015) for examples in quantum thermodynamics]. On the other hand, the class of asymptotically exact incoherent operations becomes particularly relevant when one wants to consider the mapping  $\varrho \mapsto \sigma$  not for a single copy, but starting from  $N$  copies,  $\varrho^{\otimes N}$ . In this case, one typically asks for the minimal rate  $r$  such that  $\lim_{N \to \infty} \{\inf_{\Lambda} \| \Lambda[\varrho^{\otimes [rN]}] - \sigma^{\otimes N} \|_1\} = 0$ , where  $r$  is the asymptotic cost of  $\sigma$  in terms of  $\varrho$ , and  $[x]$  denotes the largest integer lower than or equal to the real number  $x$ . Indeed, Winter and Yang (2016) carried out such a program defining the appropriate quantities and obtaining results that are presented in more detail in Sec. III.B. Approximate transformations for the class TIO were also investigated recently by Marvian and Lloyd (2016).

# B. Coherence as a resource

We now explore the use of coherence as a resource for enabling operations that would not otherwise be possible if only incoherent operations were accessible to the experimenter.

# 1. Maximally coherent states and state transformations via incoherent operations

We start by identifying a  $d$ -dimensional maximally coherent state as a state that allows for the deterministic generation of all other  $d$ -dimensional quantum states by means of the free operations. Note that this definition is independent of a specific coherence quantifier and allows one to identify a unit for coherence (a coherence bit, or cobit)<sup>5</sup> to which all

measures may be normalized; see also Sec. III for more details on quantifying coherence. The canonical example of a maximally coherent state is

$$
\left| \Psi_ {d} \right\rangle = \frac {1}{\sqrt {d}} \sum_ {i = 0} ^ {d - 1} | i \rangle \tag {10}
$$

as it is easy to see that by IO, any  $d$ -dimensional state  $\varrho$  may be prepared from  $|\Psi_d\rangle$  with certainty (Baumgratz, Cramer, and Plenio, 2014). We note that not all frameworks of coherence that were discussed in Sec. II.A.2 have a maximally coherent state, i.e., a state from which all other states can be created via the corresponding set of operations. In particular, such a state does not exist for PIO (Chitambar and Gour, 2016a, 2016b, 2017), GIO, and FIO (de Vicente and Streltsov, 2017).

The full set of maximally coherent states is obtained as the orbit of  $|\Psi_d\rangle$  under all incoherent unitaries (Bai and Du, 2015). For coherence theory the maximally coherent state  $|\Psi_d\rangle$  plays a role analogous to the maximally entangled state in entanglement theory. As we shall see later, both concepts are very closely related. One may also determine maximally coherent states under certain additional constraints, such as the degree of mixedness, which gives rise to the class of maximally coherent mixed states (Singh, Bera, Dhar, and Pati, 2015). For a  $d$ -dimensional system and any fixed spectrum  $\{p_n\}_{n=1}^d$ , Streltsov, Kampermann et al. (2016) proved that the state  $\varrho_{\mathrm{max}} = \sum_{n=1}^{d} p_n |n_+\rangle \langle n_+|$ , where  $\{|n_+\rangle\}$  denotes a mutually unbiased basis with respect to the incoherent basis  $\{|i\rangle\}$  (that is,  $|\langle i|n_+\rangle|^2 = 1/d$ ), is a universal maximally coherent mixed state with respect to any coherence monotone under the set MIO. Complementarity relations between measures of purity and coherence were further investigated by Cheng and Hall (2015), Xi, Li, and Fan (2015), Giorda and Allegra (2016a), Streltsov, Kampermann et al. (2016), and Kumar (2017).

The interconversion of pure states via incoherent operations was studied by Du, Bai, and Guo (2015, 2017), Chitambar and Gour (2016a, 2016b, 2017), Winter and Yang (2016), and Zhu et al. (2017). In particular, a pure state  $|\phi \rangle$  can be converted into another pure state  $|\psi \rangle$  via IO or SIO if and only if  $\Delta [|\psi \rangle \langle \psi |]$  majorizes  $\Delta [|\phi \rangle \langle \phi |]$  (Winter and Yang, 2016; Zhu et al., 2017), i.e.,

$$
\Delta [ | \psi \rangle \langle \psi | ] \succ \Delta [ | \phi \rangle \langle \phi | ] \tag {11}
$$

is a necessary and sufficient condition for the transformation  $|\phi \rangle \mapsto |\psi \rangle$  via IO or SIO. Here the majorization relation for density matrices  $\varrho >\sigma$  means that their spectra  $\mathrm{spec}(\varrho) = (p_1\geq \dots \geq p_d)$  and  $\mathrm{spec}(\sigma) = (q_1\geq \dots \geq q_d)$  fulfill the relation  $\sum_{i = 1}^{t}p_{i}\geq \sum_{j = 1}^{t}q_{j}$  for all  $t < d$  and

$\sum_{i=1}^{d} p_{i} = \sum_{j=1}^{d} q_{j}$ . Note that a similar majorization condition is also known in entanglement theory (Nielsen, 1999).

Less progress has been made for the single copy transformations of mixed coherent states and only isolated results are known. A notable result in this context was provided by Chitambar and Gour 2016a, 2016b, 2017), who gave a full characterization of single-qubit state conversion via SIO, DIO, IO, or MIO. In particular, a single-qubit state with Bloch vector  $\mathbf{r} = (r_x,r_y,r_z)^T$  can be converted into another singlequbit state with Bloch vector  $\mathbf{s} = (s_x,s_y,s_z)^T$  via SIO, DIO, IO, or MIO if and only if the following inequalities are fulfilled (Streltsov, Rana, Boes, and Eisert, 2017):

$$
s _ {x} ^ {2} + s _ {y} ^ {2} \leq r _ {x} ^ {2} + r _ {y} ^ {2}, \tag {12}
$$

$$
\frac {1 - s _ {z} ^ {2}}{s _ {x} ^ {2} + s _ {y} ^ {2}} \geq \frac {1 - r _ {z} ^ {2}}{r _ {x} ^ {2} + r _ {y} ^ {2}}. \tag {13}
$$

In the asymptotic setting, any state which is not incoherent allows for the distillation of maximally coherent states via IO (Winter and Yang, 2016). The optimal rate for this process can be evaluated analytically; see Sec. III.B for more details, where also the asymptotic state formation from maximally coherent states is discussed.

# 2. States and maps

A more complex task beyond state preparation is that of the generation of a general quantum operation from a supply of coherent states and incoherent operations. Just as the maximally entangled state allows for the generation of all quantum operations (Eisert et al., 2000) via LOCC, so does the maximally coherent state allow for the generation of all quantum operations via IO. The explicit construction for an arbitrary single-qubit unitary can be found in Baumgratz, Cramer, and Plenio (2014), and the extension to general quantum operations of arbitrary dimension was studied by Chitambar and Hsieh (2016) and Ben Dana et al. (2017). In particular, Ben Dana et al. (2017) showed that any quantum operation acting on a Hilbert space of dimension  $d$  can be implemented via IO by consuming a maximally coherent state of dimension  $d$ . The corresponding construction makes use of maximally coherent states even if the targeted quantum operation may only be very slightly coherent. It is an open question how much coherence is required for creating an arbitrary unitary or an arbitrary quantum operation in general. However, by virtue of the monotonicity of coherence quantifiers under incoherent operations, lower bounds to the amount of coherence required to implement a quantum operation can be provided (Mani and Karimipour, 2015; Ben Dana et al., 2017; Bu et al., 2017).

# C. Quantum coherence in distributed scenarios

Based on the framework of LOCC known from entanglement theory (Plenio and Virmani, 2007; Horodecki et al., 2009), one can introduce the framework of local incoherent operations and classical communication (LICC) (Chitambar and Hsieh, 2016; Streltsov, Rana, Bera, and Lewenstein, 2017). In both concepts one has two separated parties,

Alice and Bob, who are connected via a classical channel (such as a telephone). While in the LOCC framework Alice and Bob are allowed to locally perform any quantum operation which is compatible with the laws of quantum mechanics, in the framework of LICC the parties are restricted to local incoherent operations only.

While LICC operations in general have a difficult mathematical structure, it is possible to introduce the more general class of separable incoherent (SI) operations which has a simple mathematical form (Streltsov, Rana, Bera, and Lewenstein, 2017):

$$
\Lambda \left[ q ^ {A B} \right] = \sum_ {i} \left(A _ {i} \otimes B _ {i}\right) q ^ {A B} \left(A _ {i} ^ {\dagger} \otimes B _ {i} ^ {\dagger}\right), \tag {14}
$$

where  $A_{i}$  and  $B_{i}$  are local incoherent operators. General quantum operations of the form in Eq. (14), but without the incoherence restriction, have been studied extensively in entanglement theory, where they are called separable operations (Vedral and Plenio, 1998). It is an interesting open question whether the intersection of LOCC and SI operations is equal to LICC operations (Streltsov, Rana, Bera, and Lewenstein, 2017).

Asymmetric scenarios where only one of the parties is restricted to IO locally have also been considered (Chitambar et al., 2016; Streltsov, Rana, Bera, and Lewenstein, 2017). In the case where the second party (Bob) is restricted to incoherent operations, the corresponding sets of operations are called local quantum-incoherent operations and classical communication (LQICC) and separable quantum-incoherent operations (SQI), respectively. LQICC operations are, in particular, important for the tasks of incoherent quantum state merging (Streltsov, Chitambar et al., 2016) (see also Sec. II.D) and assisted coherence distillation (Chitambar et al., 2016; Streltsov, Rana, Bera, and Lewenstein, 2017). The latter task was also performed experimentally (Wu et al., 2017) and will be discussed in more detail in Sec. III.L.3.

A related set of operations was presented by Matera et al. (2016) in the context of a resource theory of control of quantum systems, and called global operations incoherent on  $B$  (GOIB). Those operations allow for incoherent operations on the subsystem  $B$ , and moreover they also allow for controlled operations in the incoherent reference basis from  $B$  to  $A$ . The latter amount to arbitrary control unitaries of the form  $U_{\mathrm{C}} = \sum_{i}U_{i}^{A}\otimes |i\rangle \langle i|^{B}$  (Matera et al., 2016). Moreover, the framework also allows one to attach or discard subsystems of  $A$  and to perform measurements with postselection on this subsystem (Matera et al., 2016).

The sets LQICC, SQI, and GOIB lead to the same set  $\mathcal{Q}\mathcal{I}$  of free states, which are called quantum-incoherent states (Chitambar et al., 2016; Matera et al., 2016; Streltsov, Rana, Bera, and Lewenstein, 2017) and take the form

$$
\varrho = \sum_ {i} p _ {i} \sigma_ {i} ^ {A} \otimes | i \rangle \langle i | ^ {B}. \tag {15}
$$

Here  $\sigma_{i}^{A}$  are arbitrary states on the subsystem  $A$ , while  $|i\rangle^{B}$  are incoherent states on the subsystem  $B$ . Moreover, LQICC is a strict subset of SQI (Streltsov, Rana, Bera, and Lewenstein, 2017) and GOIB (Matera et al., 2016). In turn, the latter is a strict subset of the maximal set of operations mapping the set of quantum-incoherent states onto itself, defined by Ma et al. (2016). Note that GOIB can also create entanglement while using up coherence (Matera et al., 2016), which is not possible for LQICC and SQI operations. Finally, note that the free states under LICC and SI operations are bipartite incoherent states, i.e., convex combinations of incoherent product states (Streltsov, Rana, Bera, and Lewenstein, 2017).

# D. Connection between coherence and entanglement theory

The resource theory of coherence exhibits several connections to the resource theory of entanglement. One of the first approaches in this direction was presented by Streltsov et al. (2015), where it was shown that any state with nonzero coherence can be used for entanglement creation via bipartite incoherent operations; see Sec. III.E for a detailed discussion. These results were generalized to quantum discord (Ma et al., 2016) and general types of nonclassicality (Killoran, Steinhoff, and Plenio, 2016); see Secs. III.I and III.K.3 for more details.

The interplay between coherence and entanglement in distributed scenarios was first studied by Chitambar and Hsieh (2016), who investigated state formation and distillation of entanglement and local coherence via LICC operations. Interestingly, it was shown that a bipartite state has distillable entanglement if and only if entanglement can be distilled via LICC (Chitambar and Hsieh, 2016).

Another relation between entanglement and coherence was provided by Streltsov, Chitambar et al. (2016), where they introduced and studied the task of incoherent quantum state merging. The latter is an incoherent version of standard quantum state merging (Horodecki, Oppenheim, and Winter, 2005, 2007), where two parties aim to merge their parts of a tripartite quantum state while preserving correlations with a third party. While standard quantum state merging can lead to a gain of entanglement (Horodecki, Oppenheim, and Winter, 2005, 2007), no merging protocol can lead to a gain of entanglement and coherence simultaneously (Streltsov, Chitambar et al., 2016).

Finally, we mention that the resource theory of coherence shares many similarities with the resource theory of entanglement, if the latter is restricted to maximally correlated states (Chitambar et al., 2016; Winter and Yang, 2016). In particular, given a quantum state  $\varrho = \sum_{ij}\varrho_{ij}|i\rangle \langle j|$ , we can assign to it a bipartite maximally correlated state as  $\varrho_{\mathrm{mc}} = \sum_{ij}\varrho_{ij}|ii\rangle \langle jj|$ . An important open question in this context is whether any of the aforementioned classes of incoherent operations  $\Lambda_{\mathrm{i}}$  is equivalent to LOCC operations  $\Lambda_{\mathrm{LOCC}}$  on maximally correlated states, i.e.,

$$
\sigma = \Lambda_ {\mathrm {i}} [ \varrho ] \stackrel {?} {\Leftrightarrow} \sigma_ {\mathrm {m c}} = \Lambda_ {\mathrm {L O C C}} [ \varrho_ {\mathrm {m c}} ]. \tag {16}
$$

Partial answers to this question were presented for IO by Chitambar et al. (2016) and Winter and Yang (2016) and for

GIO by de Vicente and Streltsov (2017). As we will also discuss in the following section, several quantifiers of coherence known today coincide with their equivalent entanglement quantifiers for the corresponding maximally correlated state.

# III. QUANTIFYING QUANTUM COHERENCE

# A. Postulates for coherence monotones and measures

The first axiomatic approach to quantify coherence was presented by Åberg (2006), and an alternative framework was more recently developed by Baumgratz, Cramer, and Plenio (2014). The latter approach can be seen as parallel to the axiomatic quantification of entanglement, first introduced two decades ago (Vedral et al., 1997; Vedral and Plenio, 1998). The basis of the axiomatic approach consists of the following postulates that any quantifier of coherence  $C$  should fulfill (Åberg, 2006; Baumgratz, Cramer, and Plenio, 2014; Levi and Mintert, 2014):

(C1) Non-negativity:

$$
C (\varrho) \geq 0 \tag {17}
$$

in general, with equality if and only if  $\varrho$  is incoherent.

(C2) Monotonicity:  $C$  does not increase under the action of incoherent operations, i.e.,

$$
C (\Lambda [ \varrho ]) \leq C (\varrho) \tag {18}
$$

for any incoherent operation  $\Lambda$ .

(C3) Strong monotonicity:  $C$  does not increase on average under selective incoherent operations, i.e.,

$$
\sum_ {i} q _ {i} C \left(\sigma_ {i}\right) \leq C (\varrho) \tag {19}
$$

with probabilities  $q_{i} = \mathrm{Tr}[K_{i}\varrho K_{i}^{\dagger}]$ , postmeasurement states  $\sigma_{i} = K_{i}\varrho K_{i}^{\dagger} / q_{i}$ , and incoherent Kraus operators  $K_{i}$ .

(C4) Convexity:  $C$  is a convex function of the state, i.e.,

$$
\sum_ {i} p _ {i} C \left(\varrho_ {i}\right) \geq C \left(\sum_ {i} p _ {i} \varrho_ {i}\right). \tag {20}
$$

At this point it is instrumental to compare conditions C2 and C3 to the corresponding conditions in entanglement theory (Vedral et al., 1997; Vedral and Plenio, 1998; Plenio and Virmani, 2007; Horodecki et al., 2009). There C2 is equivalent to the requirement that an entanglement quantifier  $E$  should not increase under LOCC. Similarly, C3 is equivalent to the requirement that  $E$  should not increase on average under selective LOCC operations, i.e., when the communicating parties are able to store their measurement outcomes.

Conditions C1 and C2 can be seen as minimal requirements: any quantity  $C$  should at least fulfill these two conditions in order to be a meaningful resource quantifier for some coherence-based task. Condition C3 quantifies the intuition that coherence should not increase under incoherent measurements even if one has access to the individual measurement outcomes. This condition C3, when combined with convexity C4, implies monotonicity C2 (Baumgratz, Cramer, and Plenio, 2014). The reason for this overcompleteness comes from entanglement theory: there are meaningful quantifiers of entanglement which satisfy only some of these conditions (Plenio and Virmani, 2007; Horodecki et al., 2009).

Following standard notions from entanglement theory (Plenio and Virmani, 2007), we call a quantity  $C$  which fulfills condition C1 and either condition C2 or C3 (or both) a coherence monotone. A quantity  $C$  is further called a coherence measure if it fulfills C1-C4 together with the following two additional conditions.

(C5) Uniqueness for pure states: For any pure state  $|\psi \rangle$ ,  $C$  takes the form

$$
C (| \psi \rangle \langle \psi |) = S (\Delta [ | \psi \rangle \langle \psi | ]), \tag {21}
$$

where  $S(\varrho) = -\mathrm{Tr}[\varrho \log_2\varrho ]$  is the von Neumann entropy.

(C6) Additivity:  $C$  is additive under tensor products, i.e.,

$$
C (\varrho \otimes \sigma) = C (\varrho) + C (\sigma). \tag {22}
$$

We remark that the terminology adopted here differs from the one used in some recent literature, which is mainly based on Baumgratz, Cramer, and Plenio (2014). In particular, several authors required that a coherence measure fulfills only conditions C1-C4. With the more stringent approach presented here, inspired from entanglement theory, we aim to distinguish two important coherence quantifiers: distillable coherence (which is equal to the relative entropy of coherence) and coherence cost (which is equal to the coherence of formation). As seen in the following, these two quantities fulfill all conditions C1-C6 and are thus elevated to the status of measures. Most of the other coherence quantifiers presented in this Colloquium remain coherence monotones in the sense that they fulfill conditions C1 and C2; several of them also turn out to fulfill C3 and C4, however most violate C5 and C6.

Finally, we note that alternative or additional desirable requirements for coherence monotones may be proposed. In particular, as shown by Yu, Zhang, Xu, and Tong (2016), for the set IO the conditions C3 and C4 can be replaced by the following single requirement of additivity on block-diagonal states:

$$
C (p \varrho \oplus (1 - p) \sigma) = p C (\varrho) + (1 - p) C (\sigma). \tag {23}
$$

When combining Eq. (23) with C1 and C2, these three conditions are equivalent to C1-C4 (Yu, Zhang, Xu, and Tong, 2016). Furthermore, Peng, Jiang, and Fan (2016) postulated that any valid coherence quantifier should be maximal only on the set of pure maximally coherent states  $|\Psi_d\rangle$ , a property satisfied, in particular, by the two coherence measures mentioned; however, such states do not represent a golden unit in all versions of the resource theory of coherence, as remarked in Sec. II.B.1.

In the following sections, we review the most relevant coherence monotones and measures defined in the current literature, as well as other recent quantitative studies of coherence—and nonclassicality more broadly—in single and multipartite quantum systems.

# B. Distillable coherence and coherence cost

The distillable coherence is the optimal number of maximally coherent single-qubit states  $|\Psi_2\rangle$  which can be obtained per copy of a given state  $\varrho$  via incoherent operations in the asymptotic limit. The formal definition of distillable coherence can be given as follows (Yuan et al., 2015; Winter and Yang, 2016):

$$
C _ {d} (\varrho) = \sup  \left\{R: \lim  _ {n \rightarrow \infty} \left(\inf  _ {\Lambda_ {\mathrm {i}}} \| \Lambda_ {\mathrm {i}} [ \varrho^ {\otimes n} ] - | \Psi_ {2} \rangle \langle \Psi_ {2} | ^ {\otimes \lfloor n R \rfloor} \| _ {1}\right) = 0 \right\}. \tag {24}
$$

From this definition it is tempting to believe that exact evaluation of distillable coherence is out of reach. Surprisingly, this is not the case, and a simple expression for distillable coherence of an arbitrary mixed state, with  $\Lambda_{\mathrm{i}}$  belonging to the set IO, was given by Winter and Yang (2016):

$$
C _ {d} (\varrho) = S (\Delta [ \varrho ]) - S (\varrho). \tag {25}
$$

For pure states this result was independently found by Yuan et al. (2015). Interestingly, the distillable coherence also coincides with the relative entropy of coherence which was introduced by Baumgratz, Cramer, and Plenio (2014) and will be discussed in Sec. III.C.1. Since the relative entropy of coherence is a coherence measure (Baumgratz, Cramer, and Plenio, 2014), the same is true for the distillable coherence, i.e., it fulfills all requirements C1-C6.

Another important quantifier is the coherence cost (Yuan et al., 2015; Winter and Yang, 2016): it quantifies the minimal rate of maximally coherent single-qubit states  $|\Psi_2\rangle$  required to produce a given state  $\varrho$  via incoherent operations in the asymptotic limit. Its formal definition is similar to that of entanglement cost and can be given as follows:

$$
C _ {c} (\varrho) = \inf  \left\{R: \lim  _ {n \rightarrow \infty} \left(\inf  _ {\Lambda_ {\mathrm {i}}} \| \varrho^ {\otimes n} - \Lambda_ {\mathrm {i}} [ | \Psi_ {2} \rangle \langle \Psi_ {2} | ^ {\otimes \lfloor n R \rfloor} ] \| _ {1}\right) = 0 \right\}. \tag {26}
$$

Interestingly, restricting again  $\Lambda_{\mathrm{i}}$  to the set IO, the coherence cost admits a single-letter expression. In particular, it is equal to the coherence of formation (Winter and Yang, 2016):

$$
C _ {c} (\varrho) = C _ {f} (\varrho). \tag {27}
$$

The coherence of formation is defined and discussed in detail in Sec. III.D. The result in Eq. (27) can be seen as parallel to the well-known fact that the entanglement cost is equal to the regularized entanglement of formation (Hayden, Horodecki, and Terhal, 2001). However, in the case of coherence no regularization is required, which significantly simplifies the evaluation of  $C_c$ .

The coherence cost is a coherence measure, i.e., it fulfills all conditions C1-C6. Conditions C1-C4 follow from Eq. (27) and the fact that the coherence of formation fulfills C1-C4 (Yuan et al., 2015). Condition C5 also follows from Eq. (27) and the definition of coherence of formation; see Sec. III.D. Moreover, the coherence cost is additive, i.e., condition C6 is also satisfied (Winter and Yang, 2016).

In general, the distillable coherence cannot be larger than the coherence cost

$$
C _ {d} (\varrho) \leq C _ {c} (\varrho). \tag {28}
$$

For pure states this inequality becomes an equality, which implies that the resource theory of coherence is reversible for pure states. In particular, any state  $|\psi_1\rangle$  with a distillable coherence of  $c_{1}$  cobits can be asymptotically converted into any other state  $|\psi_2\rangle$  with a distillable coherence of  $c_{2}$  cobits at a rate  $c_{1} / c_{2}$ . However, there exist mixed states with  $C_d$  strictly smaller than  $C_c$  (Winter and Yang, 2016). Nevertheless, this phenomenon does not appear in its extremal form, i.e., there are no states with zero distillable coherence but nonzero coherence cost (Winter and Yang, 2016). Therefore, in contrast to entanglement theory (Horodecki, Horodecki, and Horodecki, 1998), there is no "bound coherence" within the resource theory of coherence based on the set IO (Winter and Yang, 2016).

Notice instead that, if one considers the maximal set MIO of incoherent operations, the corresponding resource theory of coherence becomes reversible also for mixed states, as the general framework of Brandão and Gour (2015) applies in this case (Winter and Yang, 2016). This means that the distillable coherence under MIO remains equal to the relative entropy of coherence, i.e., Eq. (25) still holds under the largest set of free operations, while the coherence cost under MIO also reduces to the same quantity  $C_c(\varrho) = C_d(\varrho)$ , thus closing the irreversibility gap. $^{10}$  Note further that not all sets of operations presented in Sec. II.A.2 allow for free coherence distillation; this is further discussed in Sec. VI.

# C. Distance-based quantifiers of coherence

A general distance-based coherence quantifier is defined as (Baumgratz, Cramer, and Plenio, 2014)

$$
C _ {D} (\varrho) = \inf  _ {\sigma \in \mathcal {I}} D (\varrho , \sigma), \tag {29}
$$

where  $D$  is a distance and the infimum is taken over the set of incoherent states  $\mathcal{I}$ . Clearly, any quantity defined in this way fulfills C1 for any distance  $D(\varrho, \sigma)$  which is non-negative and zero if and only if  $\varrho = \sigma$ . Monotonicity C2 is also fulfilled for any set of operations discussed in Sec. II.A.2 if the distance is contractive (Baugratz, Cramer, and Plenio, 2014),

$$
D (\Lambda [ \varrho ], \Lambda [ \sigma ]) \leq D (\varrho , \sigma) \tag {30}
$$

for any quantum operation  $\Lambda$ .

Moreover, any distance-based coherence quantifier fulfills convexity C4 whenever the corresponding distance is jointly convex (Baumgratz, Cramer, and Plenio, 2014),

$$
D \left(\sum_ {i} p _ {i} \varrho_ {i}, \sum_ {j} p _ {j} \sigma_ {j}\right) \leq \sum_ {i} p _ {i} D \left(\varrho_ {i}, \sigma_ {i}\right). \tag {31}
$$

In the following, we explicitly discussed three important distance-based coherence quantifiers.

# 1. Relative entropy of coherence

If the distance is chosen to be the quantum relative entropy

$$
S (\varrho \| \sigma) = \operatorname {T r} [ \varrho \log_ {2} \varrho ] - \operatorname {T r} [ \varrho \log_ {2} \sigma ], \tag {32}
$$

the corresponding quantifier is known as the relative entropy of coherence $^{11}$  (Bamgratz, Cramer, and Plenio, 2014):

$$
C _ {r} (\varrho) = \min  _ {\sigma \in \mathcal {I}} S (\varrho \| \sigma). \tag {33}
$$

The relative entropy of coherence fulfills conditions C1, C2, and C4 for any set of operations discussed in Sec. II.A.2. For the set IO it also fulfills C3 (Baumgratz, Cramer, and Plenio, 2014). Moreover, it is equal to the distillable coherence  $C_d$ , and therefore both quantities admit the same closed expression (Gour, Marvian, and Spekkens, 2009; Baumgratz, Cramer, and Plenio, 2014; Winter and Yang, 2016)

$$
C _ {r} (\varrho) = C _ {d} (\varrho) = S \left(\Delta [ \varrho ]\right) - S (\varrho), \tag {34}
$$

where  $\Delta[\varrho]$  is the dephasing operation defined in Eq. (5). The proof of this equality is remarkably simple: it is enough to note that the relative entropy between an arbitrary state  $\varrho$  and another incoherent state  $\sigma \in \mathcal{I}$  can be written as

$$
S (\varrho \| \sigma) = S (\Delta [ \varrho ]) - S (\varrho) + S (\Delta [ \varrho ] \| \sigma), \tag {35}
$$

which is straightforward to prove using the relation  $\mathrm{Tr}[\varrho \log_2\sigma ] = \mathrm{Tr}[\Delta [\varrho ]\log_2\sigma ]$  . Minimizing the right-hand side of Eq. (35) over all incoherent states  $\sigma \in \mathcal{I}$  we immediately see that the minimum is achieved for  $\sigma = \Delta [\varrho ]$  , which completes the proof of Eq. (34). From Eq. (34) it also follows that the relative entropy of coherence fulfills conditions C5 and C6.

As further shown by Singh, Bera, Misra, and Pati (2015), the relative entropy of coherence can also be interpreted as the minimal amount of noise required for fully decohering the state  $\varrho$ . Moreover, Rodríguez-Rosario, Frauenheim, and Aspuru-Guzik (2013) showed that the relative entropy of coherence is related to the deviation of the state from thermal equilibrium.

Possible extensions of the relative entropy of coherence to quantifiers based on the relative Rényi and Tsallis entropies were also discussed (Chitambar and Gour, 2016a, 2016b, 2017; Rastegin, 2016).

# 2. Coherence quantifiers based on matrix norms

We now consider coherence quantifiers based on matrix norms, i.e., such that the corresponding distance has the form  $D(\varrho, \sigma) = \| \varrho - \sigma \|$  with some matrix norm  $\| \cdot \|$ . Note first that any such distance is jointly convex, i.e., fulfills Eq. (31), as long as the corresponding norm  $\| \cdot \|$  fulfills the triangle inequality and absolute homogeneity $^{12}$  (Baumgratz, Cramer, and Plenio, 2014). Thus, any matrix norm with the aforementioned properties gives rise to a convex coherence quantifier. Relevant norms with these properties are the  $l_p$  norm  $\| \cdot \|_{l_p}$  and the Schatten  $p$  norm  $\| \cdot \|_p$ :

$$
\left\| M \right\| _ {l _ {p}} = \left(\sum_ {i, j} \left| M _ {i j} \right| ^ {p}\right) ^ {1 / p}, \tag {36}
$$

$$
\| M \| _ {p} = \left\{\operatorname {T r} \left[ \left(M ^ {\dagger} M\right) ^ {p / 2} \right] \right\} ^ {1 / p} \tag {37}
$$

with  $p \geq 1$ . The corresponding coherence quantifiers will be denoted by  $C_{l_p}$  and  $C_p$ , respectively.

The  $l_{1}$  norm of coherence  $C_{l_1}$  was first introduced and studied by Baumgratz, Cramer, and Plenio (2014). In particular,  $C_{l_1}$  fulfills the conditions C1-C4 for the set IO and has the following simple expression (Baumgratz, Cramer, and Plenio, 2014):

$$
C _ {l _ {1}} (\varrho) = \min  _ {\sigma \in \mathcal {I}} \| \varrho - \sigma \| _ {l _ {1}} = \sum_ {i \neq j} | \varrho_ {i j} |. \tag {38}
$$

For the maximally coherent state  $C_{l_1}$  takes the value  $C_{l_1}(|\Psi_d\rangle) = d - 1$ , which also means that  $C_{l_1}$  does not fulfill conditions C5 and C6. It was also shown by Bu and Xiong (2016) that  $C_{l_1}$  is a DIO and MIO monotone for  $d = 2$ , while it violates the monotonicity condition C2 for DIO and MIO for  $d > 2$ .

For  $p = 1$  the corresponding Schatten norm reduces to the trace norm. Since the trace norm is contractive under quantum operations, the corresponding coherence quantifier  $C_1$  satisfies the conditions C1, C2, and C4 for any set of operations discussed in Sec. II.A.2. However,  $C_1$  violates the condition C3 for the set IO, as shown by Yu, Zhang, Xu, and Tong (2016) based on the violation of property in Eq. (23). Nevertheless, for single-qubit states  $C_1$  is equivalent to  $C_{l_1}$ , and thus the condition C3 is fulfilled in this case (Shao et al., 2015). Similar results were obtained for general  $X$  states: also in this case  $C_1$  is equivalent to  $C_{l_1}$ , and condition C3 is fulfilled for the set IO (Rana, Parashar, and Lewenstein, 2016). The characterization of the closest incoherent state with respect to the trace norm is nontrivial in general, and partial results for pure states and  $X$  states were obtained by Chen, Grogan et al. (2016) and Rana, Parashar, and Lewenstein (2016).

For  $p = 2$  the Schatten norm is equivalent to the Hilbert-Schmidt norm and also equal to the  $l_{2}$  norm. In this context, Baumgratz, Cramer, and Plenio (2014) studied the case where coherence is quantified via the squared Hilbert-Schmidt norm. They found that the coherence quantifier obtained in this way violates strong monotonicity C3 for the set IO. For any  $p \geq 1$ ,  $C_p$  is a convex coherence monotone for all single-qubit states, i.e., it fulfills C1, C2, and C4 for the set IO (Rana, Parashar, and Lewenstein, 2016). However, in general  $C_{l_p}$  and  $C_p$  violate conditions C2 and C3 for the set IO for all  $p > 1$  in higher-dimensional systems (Rana, Parashar, and Lewenstein, 2016). Interestingly,  $C_p$  is a coherence monotone for the set GIO for all  $p \geq 1$  (de Vicente and Streltsov, 2017).

# 3. Geometric coherence

Here we consider the geometric coherence defined by Streltsov et al. (2015) as follows:

$$
C _ {g} (\varrho) = 1 - \max  _ {\sigma \in \mathcal {I}} F (\varrho , \sigma) \tag {39}
$$

with the fidelity  $F(\varrho, \sigma) = \| \sqrt{\varrho} \sqrt{\sigma} \|_1^2$ . The geometric coherence fulfills conditions C1, C2, and C4 for any set of operations discussed in Sec. II.A.2. Additionally, it also fulfills C3 for the set IO (Streltsov et al., 2015). For pure states, the geometric coherence takes the form  $C_g(|\psi\rangle) = 1 - \max_i |\langle i|\psi\rangle|^2$ , which means that  $C_g$  does not meet conditions C5 and C6.

If  $\varrho$  is a single-qubit state,  $C_g$  admits the following closed expression (Streltsov et al., 2015):

$$
C _ {g} (Q) = \frac {1}{2} \left(1 - \sqrt {1 - 4 \left| Q _ {0 1} \right| ^ {2}}\right), \tag {40}
$$

where  $\varrho_{01} = \langle 0|\varrho |1\rangle$  is the off-diagonal element of  $\varrho$  in the incoherent basis. Note that for all single-qubit states we have  $C_1 = C_{l_1} = 2|\varrho_{01}|$ , and thus  $C_g$  is a simple function of these quantities in the single-qubit case. As seen in the following sections,  $C_g$  can also be considered as a convex roof quantifier of coherence and is also closely related to the geometric entanglement. Upper and lower bounds on the geometric coherence were investigated by H.-J. Zhang et al. (2017).

Another related quantity was introduced by Baumgratz, Cramer, and Plenio (2014) and studied by Shao et al. (2015) where it was called fidelity of coherence:  $C_F(\varrho) = 1 - \max_{\sigma \in \mathcal{I}} \sqrt{F(\varrho, \sigma)}$ . While  $C_F$  fulfills conditions C1, C2, and C4 for any set of operations discussed in Sec. II.A.2, it violates the strong monotonicity condition C3 for IO (Shao et al., 2015).

# D. Convex roof quantifiers of coherence

Provided that a quantifier of coherence has been defined for all pure states, it can be extended to mixed states via the standard convex roof construction (Yuan et al., 2015):

$$
C (q) = \inf  _ {\left\{p _ {i}, | \psi_ {i} \rangle \right\}} \sum_ {i} p _ {i} C (| \psi_ {i} \rangle), \tag {41}
$$

where the infimum is taken over all pure state decompositions of  $\varrho = \sum_{i}p_{i}|\psi_{i}\rangle \langle \psi_{i}|$ . Constructions of this type were previously introduced and widely studied in entanglement theory (Bennett et al., 1996; Uhlmann, 1998).

If for pure states the amount of coherence is quantified by the distillable coherence  $C_d(|\psi \rangle) = S(\Delta [|\psi \rangle \langle \psi |])$ , as in Eq. (21), the corresponding convex roof quantifier is known as the coherence of formation (Åberg, 2006; Yuan et al., 2015; Winter and Yang, 2016):

$$
C _ {f} (q) = \inf  _ {\left\{p _ {i}, | \psi_ {i} \rangle \right\}} \sum_ {i} p _ {i} S (\Delta [ | \psi_ {i} \rangle \langle \psi_ {i} | ]). \tag {42}
$$

As already noted in Sec. III.B,  $C_f$  is equal to the coherence cost under IO. As shown by Yuan et al. (2015), the coherence of formation<sup>13</sup> fulfills conditions C1-C4 for the set IO. By definition,  $C_f$  also fulfills C5, and additivity C6 was proven by Winter and Yang (2016). Remarkably,  $C_f$  violates monotonicity C2 for the class MIO (Hu, 2016).

For a general state  $\varrho = \sum_{ij}\varrho_{ij}|i\rangle \langle j|$ , the coherence of formation is equal to the entanglement of formation (Bennett et al., 1996) of the corresponding maximally correlated state  $\varrho_{\mathrm{mc}} = \sum_{ij}\varrho_{ij}|ii\rangle \langle jj|$  (Winter and Yang, 2016):

$$
C _ {f} (q) = E _ {f} \left(q _ {\mathrm {m c}}\right). \tag {43}
$$

Using the formula for the entanglement of formation of two-qubit states (Wootters, 1998), Eq. (43) implies that the coherence of formation can be evaluated exactly for all single-qubit states (Yuan et al., 2015):

$$
C _ {f} (\varrho) = h \left(\frac {1 + \sqrt {1 - 4 \left| \varrho_ {0 1} \right| ^ {2}}}{2}\right), \tag {44}
$$

where  $h(x) = -x\log_2x - (1 - x)\log_2(1 - x)$  is the binary entropy. If we compare this expression with the expression for the geometric coherence in Eq. (40), it follows that  $C_f = h(1 - C_g)$  holds for any single-qubit state. Thus,  $C_f$  is also a simple function of  $C_1$  and  $C_{l_1}$  in this case.

The coherence concurrence was defined by Qi, Gao, and Yan (2016) as the convex roof of the  $l_{1}$  norm of coherence,

$$
C _ {c _ {1}} (\varrho) = \inf  _ {\left\{p _ {i}, \mid \psi_ {i} \right\}} \sum_ {i} p _ {i} C _ {l _ {1}} \left(\left| \psi_ {i} \right\rangle \langle \psi_ {i} |\right). \tag {45}
$$

It follows by definition that  $C_{c_1}(|\psi \rangle \langle \psi |) = C_{l_1}(|\psi \rangle \langle \psi |)$  for any pure state  $|\psi \rangle$ , while  $C_{c_1}(\varrho) \geq C_{l_1}(\varrho)$  for an arbitrary mixed state  $\varrho$ . The coherence concurrence satisfies properties C1-C4 for the set IO as proven by Qi, Gao, and Yan (2016), but it violates C5 and C6. The relation between coherence concurrence and entanglement concurrence (Wootters, 1998) was also investigated by Qi, Gao, and Yan (2016). In particular, for a single-qubit state  $\varrho$ ,  $C_{c_1}(\varrho) = C_{l_1}(\varrho) = 2|\varrho_{01}|$ , which means that the coherence concurrence of  $\varrho$  is equal to the entanglement concurrence of the corresponding maximally correlated two-qubit state  $\varrho_{\mathrm{mc}}$ , and that the functional relation between  $C_f$  and  $C_{c_1}$  for a qubit, obtained from Eq. (44), is the same as that between the entanglement of formation and the entanglement concurrence for two qubits, established by Wootters (1998).

The geometric coherence  $C_g$  introduced in Eq. (39) can also be regarded as a convex roof quantifier:

$$
C _ {g} (\varrho) = \inf  _ {\left\{p _ {i}, | \psi_ {i} \rangle \right\}} \sum_ {i} p _ {i} C _ {g} (| \psi_ {i} \rangle). \tag {46}
$$

This can be proven using a general theorem in Streltsov, Kampermann, and Bruß (2010) (see Theorem 2 in the appendix there). Moreover, Eq. (43) also holds for the geometric coherence and entanglement  $C_g(\varrho) = E_g(\varrho_{\mathrm{mc}})$ , where the geometric entanglement is defined as  $E_g(\varrho) = 1 - \max_{\sigma \in S} F(\varrho, \sigma)$ , and  $S$  is the set of separable states (Wei and Goldbart, 2003; Streltsov, Kampermann, and Bruß, 2010).

# E. Coherence monotones from entanglement

An alternative approach to quantify coherence was introduced by Streltsov et al. (2015). In particular, they showed that any entanglement monotone  $E$  gives rise to a coherence monotone  $C_E$  via the following relation:

$$
C _ {E} \left(q ^ {S}\right) = \lim  _ {d _ {A} \rightarrow \infty} \left\{\sup  _ {\Lambda_ {\mathrm {i}}} E ^ {S: A} \left(\Lambda_ {\mathrm {i}} \left[ q ^ {S} \otimes | 0 \rangle \langle 0 | ^ {A} \right]\right)\right\}. \tag {47}
$$

Here  $\varrho^S$  is a state of the system  $S$ , and  $A$  is an additional ancilla of dimension  $d_A$ . The supremum is performed over all bipartite incoherent operations  $\Lambda_{\mathrm{i}} \in \mathrm{IO}$ , i.e., such that the corresponding Kraus operators map the product basis  $|k\rangle |l\rangle$  onto itself.

The intuition behind the entanglement-based coherence quantifiers  $C_E$  is the following: if the state  $\varrho^S$  is incoherent, then the total state  $\Lambda_{\mathrm{i}}[\varrho^S \otimes |0\rangle \langle 0|^A]$  will remain separable for any bipartite incoherent operation  $\Lambda_{\mathrm{i}}$ . However, if the state  $\varrho^S$  has nonzero coherence, some incoherent operation  $\Lambda_{\mathrm{i}}$  can in fact create entanglement between the system  $S$  and the ancilla  $A$  (see also Fig. 1, right panel). This finding is quantified in Eq. (47):  $C_E$  is a coherence monotone whenever  $E$  is an entanglement monotone. In particular,  $C_E$  fulfills conditions

C1-C4 for the set IO whenever  $E$  fulfills the corresponding conditions in entanglement theory (Streltsov et al., 2015).

In various situations  $C_E$  admits an explicit formula. In particular, if  $E$  is the distillable entanglement,  $C_E$  amounts to the distillable coherence (Streltsov et al., 2015):

$$
C _ {E _ {d}} (q) = C _ {d} (q). \tag {48}
$$

If  $E$  is the relative entropy of entanglement,  $C_E$  is the relative entropy of coherence, which again is equal to  $C_d$ . A similar relation can be found for the geometric entanglement and the geometric coherence  $C_{E_g}(\varrho) = C_g(\varrho)$  (Streltsov et al., 2015). For distillable entanglement, relative entropy of entanglement, and geometric entanglement, the supremum in Eq. (47) is achieved when  $\Lambda_{\mathrm{i}}$  is the generalized CNOT operation, i.e., the optimal incoherent operation is the unitary

$$
U _ {\mathrm {C N O T}} | i \rangle | 0 \rangle = | i \rangle | i \rangle . \tag {49}
$$

It is not known if this unitary is the optimal incoherent operation for all entanglement monotones  $E$ .

If entanglement is quantified via the distance-based approach (Vedral et al., 1997),

$$
E _ {D} (\varrho) = \inf  _ {\sigma \in \mathcal {S}} D (\varrho , \sigma) \tag {50}
$$

with a contractive distance  $D$ , it was further shown by Streltsov et al. (2015) that the creation of entanglement from a state  $Q^S$  via incoherent operations is bounded above by its distance-based coherence:

$$
E _ {D} ^ {S: A} \left(\Lambda_ {\mathrm {i}} \left[ \varrho^ {S} \otimes | 0 \rangle \langle 0 | ^ {\Lambda} \right]\right) \leq C _ {D} \left(\varrho^ {S}\right). \tag {51}
$$

While this result was originally proven for  $\Lambda_{\mathrm{i}} \in \mathrm{IO}$  by Streltsov et al. (2015), it generalizes to any set of incoherent operations presented in Sec. II.A.2. In case the distance  $D$  is chosen to be the quantum relative entropy, there exists an incoherent operation saturating the bound for any state  $\varrho^S$  as long as  $d_A \geq d_S$ . The same is true if the distance is chosen as  $D(\varrho, \sigma) = 1 - F(\varrho, \sigma)$ . In both cases, the bound is saturated by the generalized CNOT operation; see Eq. (49). These results also imply that a state  $\varrho^S$  can be used to create entanglement via incoherent operations if and only if  $\varrho^S$  has nonzero coherence (Streltsov et al., 2015).

# F. Robustness of coherence

Another coherence monotone was introduced by Napoli et al. (2016) and Piani et al. (2016) and termed robustness of coherence. For a given state  $\varrho$ , it quantifies the minimal mixing required to make the state incoherent:

$$
R _ {C} (\varrho) = \min  _ {\tau} \left\{s \geq 0 \left| \frac {\varrho + s \tau}{1 + s} \in \mathcal {I} \right. \right\}, \tag {52}
$$

where the minimum is taken over all quantum states  $\tau$ . A similar quantity was studied earlier in entanglement theory under the name robustness of entanglement (Vidal and Tarrach, 1999; Steiner, 2003). The robustness of coherence

fulfills C1, C2, and C4 for all sets of operations discussed in Sec. II.A.2, and additionally it also fulfills C3 for IO (Napoli et al., 2016; Piani et al., 2016). Moreover,  $R_{C}$  coincides with the  $l_{1}$  norm of coherence for all single-qubit states, all  $X$  states, and all pure states. The latter result also implies that  $R_{C}$  does not comply with C5 and C6.

The robustness of coherence has an operational interpretation which is related to the notion of coherence witnesses. A coherence witness is defined in a similar way as an entanglement witness in entanglement theory: it is a Hermitian operator  $W$  such that  $\mathrm{Tr}[W\sigma] \geq 0$  is true for all incoherent states  $\sigma \in \mathcal{I}$ . Under the additional constraint  $W \leq \mathbb{1}$  it was shown by Napoli et al. (2016) and Piani et al. (2016) that the following inequality holds true:

$$
R _ {C} (\varrho) \geq \max  \{0, - \operatorname {T r} [ \varrho W ] \}. \tag {53}
$$

Interestingly, for any state  $\varrho$  there exists a witness  $W$  saturating this inequality. On the one hand, this result means that the robustness of coherence is accessible in laboratory by measuring the expectation value of a suitable witness  $W$ , as recently demonstrated in a photonic experiment (Wang et al., 2017). It also means that  $R_{C}$  can be evaluated via a semidefinite program. The robustness of coherence is moreover a figure of merit in the task of quantum phase discrimination; see Sec. V.D for its definition and detailed discussion. Moreover, the results presented by Napoli et al. (2016) and Piani et al. (2016) also carry over to the resource theory of asymmetry, which is discussed in Sec. III.K.1.

# G. Coherence quantifiers from interferometric visibility

Clearly, quantum coherence is required for the observation of interference patterns, e.g., in the double slit experiment. Recently, this idea was formalized by von Prillwitz, Rudnicki, and Mintert (2015), where they studied the problem to determine coherence properties from interference patterns. Similar ideas were also put forth by Bera et al. (2015), where they studied the role of the  $l_{1}$  norm of coherence in general multislit experiments. Bagan et al. (2016) derived two exact complementarity relations between quantifiers of coherence and path information in a multipath interferometer, using, respectively, the  $l_{1}$  norm and the relative entropy of coherence. Studies on the quantification of interference and its relationship with coherence were also performed earlier; see, e.g., Braun and Georgeot (2006).

Biswas, García-Díaz, and Winter (2017) recently presented a general framework to quantify coherence from visibility in interference phenomena. Consider a multipath interferometer, in which a single particle can be in one of  $d$  paths, denoting the path variable by a set of orthogonal vectors  $\{|j\rangle\}_{j=0}^{d-1}$  which define the reference basis. If a local phase shift  $\varphi_{j}$  is applied in each arm, the output state of the particle can be written as  $\varrho(\vec{\varphi}) = U(\vec{\varphi})\varrho U^{\dagger}(\vec{\varphi})$ , where  $\varrho$  is the input state and  $U(\vec{\varphi}) = \sum_{j}e^{i\varphi_{j}}|j\rangle\langle j|$ . Then by placing an output detector which implements a measurement described by a positive-operator valued measure  $M = (M_{\omega})$ , one observes outcomes  $\omega$  sampled from the Born probability  $p_{M|\varrho}(\omega|\vec{\varphi}) = \mathrm{Tr}[\varrho(\vec{\varphi})M_{\omega}]$ , which constitute the interference pattern. One

can then define suitable visibility functionals  $V[p_{M|q}]$ , which intuitively capture the degree of variability of the interference pattern as a function of the phases  $\{\varphi_j\}$ . It was then shown by Biswas, García-Díaz, and Winter (2017) that, for any visibility functional  $V$  satisfying certain physical requirements, the corresponding optimal visibility (maximized over all output measurements  $M$ ) defines a valid interference-based coherence quantifier,

$$
C _ {V} (\varrho) = \sup  _ {M} V [ p _ {M | \varrho} ], \tag {54}
$$

which satisfies properties C1-C3 for the set SIO, and also C4 if  $V$  is convex in  $p$ . Various examples of visibility functionals and the corresponding coherence monotones were further discussed by Biswas, García-Díaz, and Winter (2017), showing, in particular, that the robustness of coherence presented in Sec. III.F can be alternatively interpreted (up to a normalization factor) as an interference-based quantifier of the form (54) for a suitable  $V$ , and that one can also obtain variants of the asymmetry monotones such as the Wigner-Yanase skew information discussed in Sec. III.K.1, which satisfy the necessary monotonicity requirements for coherence (with respect to the set SIO). These results establish important links between the somehow more abstract aspects in the resource theory of coherence and operational notions in the physics of interferometers.

# H. Coherence of assistance

The coherence of assistance was introduced by Chitambar et al. (2016) as follows:

$$
C _ {a} (Q) = \sup  _ {\left\{p _ {i}, \mid \psi_ {i} \right\rangle \}} \sum_ {i} p _ {i} S \left(\Delta \left[ \left| \psi_ {i} \right\rangle \langle \psi_ {i} \right]\right), \tag {55}
$$

where the maximum is taken over all pure state decompositions of  $\varrho = \sum_{i}p_{i}|\psi_{i}\rangle \langle \psi_{i}|$ . This quantity is dual to the coherence of formation defined in Eq. (42) as the minimum over all decompositions. If the state  $\varrho$  is the maximally mixed single-qubit state, it can be written as a mixture of the maximally coherent states  $|\pm \rangle = (|0\rangle \pm |1\rangle) / \sqrt{2}$  with equal probabilities. For this reason we get  $C_a(1 / 2) = 1$ , i.e., the coherence of assistance is maximal for the maximally mixed state. On the one hand, this means that the coherence of assistance is not a coherence monotone, as it indeed violates condition C1. On the other hand, the coherence of assistance plays an important role for the task of assisted coherence distillation; see Sec. III.L.3 for a detailed discussion.

While finding a closed expression for the coherence of assistance seems difficult in general, its regularization admits the following simple expression (Chitambar et al., 2016):

$$
C _ {a} ^ {\infty} (\varrho) = \lim  _ {n \rightarrow \infty} \frac {1}{n} C _ {a} \left(\varrho^ {\otimes n}\right) = S \left(\Delta [ \varrho ]\right). \tag {56}
$$

Moreover, for all single-qubit states  $\varrho$  the coherence of assistance is  $n$ -copy additive and thus can be written as  $C_{a}(\varrho) = S(\Delta [\varrho])$ . Further, there is a close relation between the coherence of assistance and the entanglement of assistance

introduced by DiVincenzo et al. (1999). In particular, the coherence of assistance of a state  $\varrho = \sum_{ij}\varrho_{ij}|i\rangle \langle j|$  is equal to the entanglement of assistance of the corresponding maximally correlated state  $\varrho_{\mathrm{mc}} = \sum_{ij}\varrho_{ij}|ii\rangle \langle jj|$  (Chitambar et al., 2016):

$$
C _ {a} (\varrho) = E _ {a} \left(\varrho_ {\mathrm {m c}}\right). \tag {57}
$$

# I. Coherence and quantum correlations beyond entanglement

Quantum discord (Zurek, 2000; Henderson and Vedral, 2001; Ollivier and Zurek, 2001) is a measure of quantum correlations going beyond entanglement (Oppenheim et al., 2002; Modi et al., 2012; Streltsov, 2015; Adesso, Bromley, and Cianciaruso, 2016). A bipartite quantum state  $\varrho^{AB}$  is said to have zero discord (with respect to the subsystem  $A$ ) if and only if it can be written as

$$
\varrho_ {\mathrm {c q}} ^ {A B} = \sum_ {i} p _ {i} | e _ {i} \rangle \langle e _ {i} | ^ {A} \otimes \varrho_ {i} ^ {B}, \tag {58}
$$

where the states  $\{|e_i\rangle \}$  form an orthonormal basis, but are not necessarily incoherent. The states of Eq. (58) are also known as classical quantum (Piani, Horodecki, and Horodecki, 2008), and the corresponding set will be denoted by  $\mathcal{CQ}$ . Correspondingly, a state  $q^{AB}$  is called (fully) classically correlated, or classical-classical, if and only if it can be written as (Piani, Horodecki, and Horodecki, 2008)

$$
q _ {\mathrm {c c}} ^ {A B} = \sum_ {i, j} p _ {i j} | e _ {i} \rangle \langle e _ {i} | ^ {A} \otimes | e _ {j} \rangle \langle e _ {j} | ^ {B}, \tag {59}
$$

and the corresponding set will be denoted by  $\mathcal{CC}$ . If a state is not fully classically correlated, we say that it possesses nonzero general quantum correlations. This notion can be straightforwardly extended to more than two parties (Piani et al., 2011).

The amount of discord in a given state can be quantified via a distance-based approach similar to the distance-based approach for coherence presented in Sec. III.C. In particular, one can define general distance-based quantifiers of discord  $\delta_D^{A|B}$  and quantumness  $Q_D^{A|B}$  as follows (Modi et al., 2012; Adesso, Bromley, and Cianciaruso, 2016; Roga, Spehner, and Illuminati, 2016):

$$
\delta_ {D} ^ {A | B} \left(\varrho^ {A B}\right) = \inf  _ {\sigma^ {A B} \in \mathcal {C Q}} D \left(\varrho^ {A B}, \sigma^ {A B}\right), \tag {60}
$$

$$
Q _ {D} ^ {A | B} \left(\varrho^ {A B}\right) = \inf  _ {\sigma^ {A B} \in \mathcal {C C}} D \left(\varrho^ {A B}, \sigma^ {A B}\right) \tag {61}
$$

with some distance  $D$ . If  $D$  is chosen to be the quantum relative entropy, the corresponding quantities are, respectively, known as the relative entropy of discord and of quantumness (Modi et al., 2010; Piani et al., 2011).

Recently, Ma et al. (2016) studied the role of coherence for creating general quantum correlations. They showed that the creation of general quantum correlations from a state  $\varrho$  is bounded above by its coherence. In particular, if  $D$  is a

contractive distance, the following relation holds for any pair of quantifiers  $Q_{D}$  and  $C_{D}$  (Ma et al., 2016):

$$
Q _ {D} ^ {S | A} \left(\Lambda_ {\mathrm {i}} \left[ \varrho^ {S} \otimes \sigma^ {A} \right]\right) \leq C _ {D} \left(\varrho^ {S}\right). \tag {62}
$$

Here  $S$  is a system in an arbitrary state  $\varrho^S$  and  $A$  is an ancilla in an incoherent state  $\sigma^A$ . While this result was originally proven for  $\Lambda_{\mathrm{i}} \in \mathrm{IO}$  by Ma et al. (2016), it generalizes to any set of operations discussed in Sec. II.A.2. These results are parallel to the discussion on creation of entanglement from coherence presented by Streltsov et al. (2015); see also Sec. III.E. In particular, any state  $\varrho^S$  with nonzero coherence can be used for creating discord via incoherent operations, since any such state can be used for the creation of entanglement (Streltsov et al., 2015).

A general framework to define quantifiers of discord and quantumness in a bipartite system from corresponding quantifiers of quantum coherence, by minimizing the latter over all local bases for one or both subsystems, respectively, was formalized recently by Adesso, Bromley, and Cianciaruso (2016).

# J. Coherence in continuous variable systems

The resource theory framework for quantum coherence adopted in this Colloquium assumes a finite-dimensional Hilbert space. However, some of the previously listed quantifiers of coherence have also been studied in continuous variable systems and specifically in bosonic modes of the radiation field. These systems are characterized by an infinite-dimensional Hilbert space, spanned by the Fock basis  $\{|n\rangle\}_{n=0}^{\infty}$  of eigenstates of the particle number operator  $a^\dagger a$  (Braunstein and van Loock, 2005).

Similarly to what was done by Eisert, Simon, and Plenio (2002) in entanglement theory, Y.-R. Zhang et al. (2016) imposed a finite mean energy constraint  $\langle a^{\dagger}a\rangle \equiv \bar{n} < \infty$  to address the quantification of coherence in such systems with respect to the Fock reference basis. The relative entropy of coherence (see Sec. III.C.1) was found to maintain its status as a valid measure of coherence, in particular, reaching a finite maximum  $C_r^{\mathrm{max}} = (\bar{n} + 1)\log (\bar{n} + 1) - \bar{n}\log \bar{n} < \infty$  for any state with finite mean energy  $\bar{n} < \infty$ . On the contrary, it was shown that the  $l_{1}$  norm of coherence  $C_{l_1}$  (see Sec. III.C.2) admits no finite maximum and can diverge even on states with finite mean energy (Y.-R. Zhang et al., 2016). This suggests that the  $l_{1}$  norm does not provide a suitable quantifier of coherence in continuous variable systems.

Xu (2016) focused on the quantification of coherence in bosonic Gaussian states of infinite-dimensional systems, which form an important subset of states entirely specified by their first and second moments and useful for theoretical and experimental investigations of continuous variable quantum information processing (Adesso and Illuminati, 2007; Weedbrook et al., 2012). In particular, Xu (2016) defined a Gaussian relative entropy of coherence for a Gaussian state  $\varrho$  (with respect to the Fock basis) as the relative entropy difference between  $\varrho$  and the closest incoherent Gaussian state, which is a thermal state expressible in terms of the first and second moments of  $\varrho$ . However, this is only an upper

bound on the true relative entropy of coherence of a Gaussian state  $\varrho$ , which is still given by Eq. (34) for any  $\varrho$  with finite mean energy (Y.-R. Zhang et al., 2016), since the closest incoherent state to  $\varrho$  given by its diagonal part  $\Delta[\varrho]$  in the Fock basis is not in general a Gaussian state. More recently, Buono et al. (2016) studied geometric quantifiers of coherence for Gaussian states in terms of Bures and Hellinger distance from the set of incoherent Gaussian states (thermal states); once more, these are upper bounds to the corresponding distance-based coherence monotones as defined in Sec. III.C.

Relations between coherence, optical nonclassicality, and entanglement in continuous variable systems were investigated recently by Vogel and Sperling (2014), Sperling and Vogel (2015), and Killoran, Steinhoff, and Plenio (2016) and are discussed in the next section.

# K. Coherence, asymmetry, and nonclassicality

# 1. Asymmetry monotones

The relation between coherence and the framework of asymmetry was discussed most recently by Marvian and Spekkens 2014a, 2014b, 2016), Marvian, Spekkens, and Zanardi (2016), and Piani et al. (2016). This framework is based on the notion of TIO, which were already introduced in Sec. II.A.2.

Marvian, Spekkens, and Zanardi (2016) proposed postulates for quantifying the asymmetry of a state with respect to time translations  $e^{-iHt}$  induced by a given Hamiltonian  $H$ . Any asymmetry monotone<sup>14</sup>  $A$  should vanish for all states which are invariant under time translations, i.e., which are incoherent in the eigenbasis of  $H$ . If we denote the latter set by  $\mathcal{I}_H$ , we have

$$
A (\varrho) = 0 \Leftrightarrow \varrho \in \mathcal {I} _ {H}. \tag {63}
$$

Moreover,  $A$  should not increase under translationally invariant operations  $\Lambda \in \mathrm{TIO}$  [see Eq. (7)]:

$$
A (\Lambda [ \varrho ]) \leq A (\varrho). \tag {64}
$$

For nondegenerate Hamiltonians, the set IO is strictly larger than the set TIO (Marvian, Spekkens, and Zanardi, 2016). It follows that the set of coherence monotones (intended as IO monotones) is a strict subset of the set of asymmetry monotones (intended as TIO monotones).

An example for an asymmetry monotone which is not a coherence monotone is the Wigner-Yanase skew information

$$
W (\varrho , H) = - \frac {1}{2} \operatorname {T r} \left[ [ H, \sqrt {\varrho} ] ^ {2} \right], \tag {65}
$$

where  $[X,Y] = XY - YX$  is the commutator. This quantity was first introduced by Wigner and Yanase (1963) as a measure of information and was proven to be an asymmetry monotone in Marvian (2012), Girolami (2014), and Marvian and Spekkens (2014a). While Girolami (2014) originally proposed the skew information as a coherence monotone, it was later shown that such a quantity can instead increase

under IO, in particular, under permutations of the reference basis states, hence violating C2 for this set of operations (Du and Bai, 2015; Marvian, Spekkens, and Zanardi, 2016).

The quantity in Eq. (65) can be generalized to the class of Wigner-Yanase-Dyson skew informations (Wigner and Yanase, 1963; Wehrl, 1978)

$$
W _ {a} (\varrho , H) = \operatorname {T r} [ \varrho H ^ {2} ] - \operatorname {T r} [ \varrho^ {a} H \varrho^ {1 - a} H ], \tag {66}
$$

with  $0 < a < 1$ , which are also asymmetry monotones (Marvian, 2012; Marvian and Spekkens, 2014a), reducing to Eq. (65) for  $a = 1/2$ . In particular, the average monotone  $\bar{W}(\varrho, H) = \int_0^1 daW_a(\varrho, H)$ , branded as the quantum variance, has recently found applications in quantum many-body systems (Frérot and Roscilde, 2016).

Another instance of an asymmetry monotone is given by the quantum Fisher information (Braunstein and Caves, 1994; Marvian and Spekkens, 2014a; C. Zhang et al., 2016; Girolami and Yadin, 2017), which can be defined (under a smoothness hypothesis) as

$$
I (\varrho , H) = - 2 \frac {\partial^ {2} F \left(\varrho_ {t} , \varrho_ {t + \varepsilon}\right)}{\partial \varepsilon^ {2}} \Bigg | _ {\varepsilon \rightarrow 0}, \tag {67}
$$

where  $F$  denotes the fidelity defined after Eq. (39), and  $\varrho_{t} = e^{-iHt}\varrho e^{iHt}$ . The quantum Fisher information quantifies the sensitivity of the state  $\varrho$  to a variation in the parameter  $t$  characterizing a unitary dynamics generated by  $H$ , hence playing a central role in quantum metrology (Braunstein and Caves, 1994; Giovannetti, Lloyd, and Maccone, 2011).

The Wigner-Yanase-Dyson skew information [Eq. (66)] and the quantum Fisher information [Eq. (67)] can be seen as special instances of the entire family of quantum generalizations of the classical Fisher information (Petz and Ghinea, 2011), which are defined in terms of the Riemannian contractive metrics on the quantum state space as classified by Morozova and Cencov (1991) and Petz (1996). All these quantities have been proven to be asymmetry monotones, i.e., worthwhile quantifiers of unspeakable coherence, in C. Zhang et al. (2016). Further details on the applications of these asymmetry monotones in the contexts of quantum speed limits, quantum estimation, and discrimination (Pires, Celeri, and Soares-Pinto, 2015; Marvian and Spekkens, 2016; Marvian, Spekkens, and Zanardi, 2016; Mondal, Datta, and Sazim, 2016; Napoli et al., 2016; Piani et al., 2016; Pires et al., 2016) are reported in Secs. IV.E and V.C.

The concept of asymmetry is closely related to the concept of quantum reference frames (Bartlett, Rudolph, and Spekkens, 2007; Gour and Spekkens, 2008; Vaccaro et al., 2008; Gour, Marvian, and Spekkens, 2009). Initially, these two concepts were defined for an arbitrary Lie group  $G$ . If  $U(g)$  is a unitary representation of the group with  $g \in G$ , the set of invariant states  $\mathcal{G}$  consists of all states which are invariant under the action of all  $U(g)$ . The relative entropy of asymmetry (also known as relative entropy of frameness) is then defined as (Gour, Marvian, and Spekkens, 2009)

$$
A _ {r} (\varrho) = \min  _ {\sigma \in \mathcal {G}} S (\varrho \| \sigma). \tag {68}
$$

Remarkably, Gour, Marvian, and Spekkens (2009) showed that the relative entropy of asymmetry admits the following expression, first independently introduced as  $G$  asymmetry by Vaccaro et al. (2008):

$$
A _ {r} (\varrho) = S (\Gamma [ \varrho ]) - S (\varrho) = S (\varrho \| \Gamma [ \varrho ]), \tag {69}
$$

where  $\Gamma[\varrho] = \int dgU(g)\varrho U^{\dagger}(g)$  is the average with respect to the Haar measure  $dg$ . If the unitary representation of the group is given by  $\{e^{-iHt} : t \in \mathbb{R}\}$  with a Hermitian nondegenerate matrix  $H = \sum_{i}h_{i}|i\rangle \langle i|$ , the set  $\mathcal{G}$  of invariant states is precisely the set  $\mathcal{I}$  of states which are incoherent in the eigenbasis  $\{|i\rangle\}$  of  $H$ . Thus, in this case the relative entropy of asymmetry  $A_{r}$  is equal to the relative entropy of coherence  $C_{r}$  with respect to the eigenbasis of  $H$  taken as a reference basis.

The robustness of asymmetry with respect to an arbitrary Lie group  $G$  is an asymmetry monotone defined by Napoli et al. (2016) and Piani et al. (2016) as

$$
R _ {A} (\varrho) = \min  _ {\tau} \left\{s \geq 0 \left| \frac {\varrho + s \tau}{1 + s} \in \mathcal {G} \right. \right\}. \tag {70}
$$

If the unitary representation of the group is given by  $e^{-iHt}$ , then the robustness of asymmetry  $R_{A}$  reduces to the robustness of coherence  $R_{C}$  with respect to the eigenbasis of  $H$ , defined in Eq. (52).

# 2. Quantifying superpositions

A very general approach to quantify coherence was presented by Åberg (2006) within the framework of quantum superposition. In this approach, the Hilbert space  $\mathcal{H}$  is divided into  $K$  subspaces  $\mathcal{L}_1,\ldots ,\mathcal{L}_K$  such that  $\oplus_{k = 1}^{K}\mathcal{L}_{k} = \mathcal{H}$ . If  $P_{k}$  is the projector corresponding to the subspace  $\mathcal{L}_k$ , the total operation  $\Pi$  is defined as

$$
\Pi [ \varrho ] = \sum_ {k = 1} ^ {K} P _ {k} \varrho P _ {k}. \tag {71}
$$

If the projectors  $P_{k}$  all have rank 1, the total operation  $\Pi$  corresponds to the total dephasing  $\Delta$ . However, in general the projectors  $P_{k}$  can have rank larger than 1.

Aberg (2006) also proposed a set of conditions a faithful quantifier of superposition ought to satisfy and showed that the relative entropy of superposition fulfills these conditions. The latter is defined as follows:

$$
S _ {r} (\varrho) = S \left(\Pi [ \varrho ]\right) - S (\varrho). \tag {72}
$$

The relative entropy of superposition is a special case of the relative entropy of asymmetry presented in Sec. III.K.1 and admits the following expression (Aberg, 2006):

$$
S _ {r} (\varrho) = \min  _ {\Pi [ \sigma ] = \sigma} S (\varrho \| \sigma) = S (\varrho \| \Pi [ \varrho ]). \tag {73}
$$

# 3. Coherence rank and general quantifiers of nonclassicality

An alternative approach was taken by Killoran, Steinhoff, and Plenio (2016), Mukhopadhyay et al. (2017), Regula et al.

(2017), and Theurer et al. (2017), who investigated a very general form of nonclassicality, also going beyond the framework of coherence. In particular, depending on the task under consideration, it can be useful to identify a set of pure states  $\{|c_i\rangle\}$  as classical. These states do not have to be mutually orthogonal in general. As an example, in entanglement theory those are all states of the product form  $|c\rangle = |\alpha \rangle \otimes |\beta \rangle$

Killoran, Steinhoff, and Plenio (2016) introduced the coherence rank of a general pure state. Analogously to the Schmidt rank in entanglement theory, the coherence rank counts the minimal number of classical states needed in the expansion of the general state  $|\psi \rangle$ :

$$
r _ {C} (| \psi \rangle) = \min  \left\{R: | \psi \rangle = \sum_ {i = 0} ^ {R - 1} a _ {i} | c _ {i} \rangle \right\}. \tag {74}
$$

Killoran, Steinhoff, and Plenio (2016) then proved that non-classicality can always be converted into entanglement in the following sense: if the set of classical states  $\{|c_i\rangle\}$  is linearly independent, there always exists a unitary operation which converts each state  $|\psi\rangle$  with coherence rank  $r_C$  into a bipartite state  $|\tilde{\psi}\rangle$  with the same Schmidt rank. Regula et al. (2017) extended this result to the multipartite setting by constructing a unitary protocol for converting nonclassicality of a  $d$ -level system, prepared in any input state with coherence rank  $2 \leq r_C \leq d$ , into genuine  $(r_C + 1)$ -partite entanglement between the system and up to  $d$  ancillary qubits.

A concept related to the coherence rank was discussed by Levi and Mintert (2014) in the specific context of coherent delocalization. In this framework, a state  $|\psi \rangle$  is called  $k$  coherent if it can be written as  $|\psi \rangle = \sum_{i=0}^{k-1}a_i|i\rangle$  with all coefficients  $a_i$  being nonzero. Here the integer  $k$  corresponds to the coherence rank  $r_C(|\psi \rangle)$ , where the set of classical states  $\{|c\rangle_i\}$  in the definition of Eq. (74) is identified with the reference basis of incoherent states  $\{|i\rangle\}$ . Levi and Mintert (2014) also proposed quantifiers for this concept of  $k$  coherence and showed that these quantifiers do not grow under incoherent channels in their framework. Note, however, that the incoherent channels of Levi and Mintert (2014) are in general different from the IO defined by Baumgratz, Cramer, and Plenio (2014) and can be rather identified with the SIO (Winter and Yang, 2016; Yadin et al., 2016). We also note that a related framework was presented recently by Yadin and Vedral (2016) to quantify macroscopic coherence. The possibility to establish superpositions of unknown quantum states via universal quantum protocols was investigated by Oszmaniec et al. (2016).

# 4. Optical coherence and nonclassicality

The framework of Killoran, Steinhoff, and Plenio (2016) and Theurer et al. (2017) is partly motivated by the seminal theory of optical coherence in continuous variable systems

(Glauber, 1963; Sudarshan, 1963; Mandel and Wolf, 1965). In this theory, the pure classical states are identified with the Glauber-Sudarshan coherent states  $|\alpha \rangle$  of the radiation field, defined (for a single bosonic mode) as the right eigenstates of the annihilation operator  $a|\alpha \rangle = \alpha |\alpha \rangle$  with  $\alpha \in \mathbb{C}^2$ . These states form an overcomplete, nonorthogonal basis for the infinite-dimensional Hilbert space. Any quantum state  $q$  which cannot be written as a mixture of Glauber-Sudarshan coherent states is hence regarded as nonclassical. We highlight a semantic subtlety here: a Glauber-Sudarshan coherent state  $|\alpha \rangle$  (with  $\alpha \neq 0$ ) is in fact coherent if one is interested in characterizing coherence with respect to the Fock basis  $\{|n\rangle\}$  as in Sec. III.J, since it can be written as a superposition thereof:

$$
| \alpha \rangle = e ^ {- | \alpha | ^ {2} / 2} \sum_ {n = 0} ^ {\infty} \frac {\alpha^ {n}}{\sqrt {n !}} | n \rangle .
$$

However, in the theory of optical coherence the Glauber-Sudarshan coherent states play rather the role of classical, or free, states (i.e., the analogous of incoherent states in the resource theory of coherence discussed so far), as they can be generated by classical currents acting on a quantum field (Louisell, 1973). Hence it is well motivated that they form the reference set with respect to which the resource of optical nonclassicality is defined and quantified.

A general resource theory of nonclassicality, as suggested by Brandão and Plenio (2008), has not been completely formalized yet. In particular, determining the suitable set of free operations for the theory of optical coherence stands as one of the most pressing open questions. The set  $\mathcal{CO}$  of classical operations, defined as the maximal set of operations preserving a reference set of (not mutually orthogonal) classical states, was studied by Sperling and Vogel (2015), where it was shown that  $\mathcal{CO}$  is convex and obeys the semigroup property. If the set of classical states is identified with the convex hull of Glauber-Sudarshan coherent states, as in the theory of optical coherence, then the corresponding  $\mathcal{CO}$  includes so-called passive operations, i.e., operations preserving the mean energy  $\langle a^{\dagger}a\rangle$ , which can be implemented by linear optical elements such as beam splitters and phase shifters.

A series of works investigated the conversion from optical nonclassicality into entanglement by means of passive operations (Kim et al., 2002; Wolf, Eisert, and Plenio, 2003; Asboth, Calsamiglia, and Ritsch, 2005; Vogel and Sperling, 2014; Sperling and Vogel, 2015), serving as an inspiration for the more recent studies of Streltsov et al. (2015), and Killoran, Steinhoff, and Plenio (2016), and Theurer et al. (2017) reviewed in the previous sections.

In particular, Asbóth, Calsamiglia, and Ritsch (2005) proposed to quantify optical nonclassicality for a single-mode state  $\varrho$  in terms of the maximum two-mode entanglement that can be generated from  $\varrho$  using linear optics, auxiliary classical states, and ideal photodetectors. Any output entanglement monotone  $E$  defines a corresponding nonclassicality quantifier  $P_{E}$  for the input state  $\varrho$ , referred to as entanglement potential. Asbóth, Calsamiglia, and Ritsch (2005) considered, in particular, the quantities  $P_{E}$  derived by choosing  $E$  to be the

logarithmic negativity or the relative entropy of entanglement. The definition of entanglement-based coherence monotones by Streltsov et al. (2015) as presented in Sec. III.E can be seen as the finite-dimensional counterpart to the study of Asbóth, Calsamiglia, and Ritsch (2005).

Furthermore, Vogel and Sperling (2014) independently defined a notion analogous to the coherence rank  $r_C$  of Eq. (74) for optical nonclassicality, i.e., with  $\{|c_i\rangle\}$  being a subset of (linearly independent) Glauber-Sudarshan coherent states. They then showed that a single-mode state  $|\psi\rangle$  with nonclassicality rank  $r_C$  can always be mapped into a two-mode entangled state with the same Schmidt rank, by means of a balanced beam splitter acting on the input mode and a vacuum ancillary mode. This can be seen as a special instance of the general theorem of Killoran, Steinhoff, and Plenio (2016) presented in Sec. III.K.3.

Finally, a connection between optical nonclassicality and the theory of coherence as reviewed in Sec. II with respect to the set IO was recently established by Tan et al. (2017). They introduced an orthogonalization procedure, according to which one can define quantifiers of optical nonclassicality  $P_{C}$ , i.e., coherence with respect to the nonorthogonal basis of Glauber-Sudarshan coherent states, in terms of any coherence monotone  $C$  applied to  $N$ -dimensional subspaces of the Hilbert space, in a suitable limit  $N \to \infty$ ; details of the mapping can be found in Tan et al. (2017). They then proved that any such  $P_{C}$  is a monotone under linear optical passive operations if the corresponding  $C$  is an IO monotone. This demonstrates that continuous variable states exhibiting optical nonclassicality can be seen essentially as the limiting case of the same resource states identified by Baumgratz, Cramer, and Plenio (2014), when the incoherent basis is chosen as the set of Glauber-Sudarshan coherent states.

# L. Multipartite settings

# 1. General distance-based coherence quantifiers

In the bipartite setting it is possible to obtain coherence monotones  $C_D$  by using the distance-based approach as in Eq. (29), where  $\mathcal{I}$  is now the set of bipartite incoherent states, i.e., convex combinations of states of the form  $|k\rangle |l\rangle$ , with  $\{|k\rangle\}$  and  $\{|l\rangle\}$  the incoherent reference bases for each subsystem, respectively (Bromley, Cianciaruso, and Adesso, 2015; Streltsov et al., 2015). It is instrumental to compare the quantities obtained in this way to other corresponding distance-based quantifiers of bipartite nonclassicality such as quantumness  $Q_D$  and entanglement  $E_D$ . Because of the inclusion relation  $\mathcal{I} \subset \mathcal{CC} \subset \mathcal{S}$ , the aforementioned quantities are related via the following inequality (Yao et al., 2015):

$$
C _ {D} (\varrho) \geq Q _ {D} (\varrho) \geq E _ {D} (\varrho). \tag {75}
$$

These results can be straightforwardly generalized to more than two parties (Yao et al., 2015).

# 2. Quantum-incoherent relative entropy

The quantum-incoherent relative entropy was defined by Chitambar et al. (2016) as follows:

$$
C _ {r} ^ {A | B} \left(\varrho^ {A B}\right) = \min  _ {\sigma^ {A B} \in \mathcal {Q I}} S \left(\varrho^ {A B} \| \sigma^ {A B}\right), \tag {76}
$$

where the minimum is taken over the set of quantum-incoherent states  $\mathcal{Q}\mathcal{I}$  defined in Eq. (15). As further discussed by Chitambar et al. (2016), the quantum-incoherent relative entropy admits the following closed expression:

$$
C _ {r} ^ {A | B} \left(\varrho^ {A B}\right) = S \left(\Delta^ {B} \left[ \varrho^ {A B} \right]\right) - S \left(\varrho^ {A B}\right), \tag {77}
$$

where  $\Delta^B$  denotes a dephasing operation on subsystem  $B$  only. As seen in the following, the quantum-incoherent relative entropy is a powerful upper bound on the distillable coherence of collaboration.

# 3. Distillable coherence of collaboration

The distillable coherence of collaboration was introduced and studied by Chitambar et al. (2016) as the figure of merit for the task of assisted coherence distillation. In this task Alice and Bob share a bipartite state  $\varrho^{AB}$  and aim to extract maximally coherent single-qubit states  $|\Psi_2\rangle$  on Bob's side via LQICC operations. The distillable coherence of collaboration is the highest achievable rate for this procedure (Chitambar et al., 2016):

$$
C _ {\mathrm {L Q I C C}} ^ {A | B} (\varrho) = \sup  \left\{R: \lim  _ {n \rightarrow \infty} \left(\inf  _ {\Lambda} \| \operatorname {T r} _ {A} [ \Lambda [ \varrho^ {\otimes n} ] ] - \tau^ {\otimes [ R n ]} \| _ {1}\right) = 0 \right\}. \tag {78}
$$

Here the infimum is taken over all LQICC operations  $\Lambda$ , and  $\tau = |\Psi_2\rangle \langle \Psi_2|^B$  is the maximally coherent single-qubit state on Bob's subsystem. As shown by Chitambar et al. (2016) for a pure state  $|\psi \rangle^{AB}$  the distillable coherence of collaboration is equal to the regularized coherence of assistance of Bob's reduced state:

$$
C _ {\mathrm {L Q I C C}} ^ {A | B} \left(\psi^ {A B}\right) = C _ {a} ^ {\infty} \left(\varrho^ {B}\right) = S \left(\Delta \left[ \varrho^ {B} \right]\right). \tag {79}
$$

It is interesting to compare this result to the distillable coherence of Bob's local state  $C_d(\varrho^B) = S(\Delta^B [\varrho^B ]) - S(\varrho^B)$ . This means that assistance provides an improvement on the distillation rate given exactly by the local von Neumann entropy  $S(\varrho^{B})$ . Remarkably, this improvement does not depend on the particular choice of the incoherent reference basis.

Streltsov, Rana, Bera, and Lewenstein (2017) extended this framework to other sets of operations, such as LICC, SI, and SQI; see Sec. II.C for their definitions. In general, if  $X$  is one of these sets, then the distillable coherence of collaboration can be generalized as follows (Streltsov, Rana, Bera, and Lewenstein, 2017):

$$
C _ {X} ^ {A | B} (\varrho) = \sup  \left\{R: \lim  _ {n \rightarrow \infty} \left(\inf  _ {\Lambda \in X} \| \operatorname {T r} _ {A} [ \Lambda [ \varrho^ {\otimes n} ] ] - \tau^ {\otimes [ R n ]} \| _ {1}\right) = 0 \right\}. \tag {80}
$$

Interestingly, for any mixed state  $\varrho = \varrho^{AB}$  the quantities  $C_{\mathrm{SI}}^{A|B}$  and  $C_{\mathrm{SQI}}^{A|B}$  are equal, and all quantities  $C_X^{A|B}$  are between  $C_{\mathrm{LICC}}^{A|B}$  and  $C_r^{A|B}$  (Streltsov, Rana, Bera, and Lewenstein, 2017):

$$
C _ {\mathrm {L I C C}} ^ {A | B} \leq C _ {\mathrm {L Q I C C}} ^ {A | B} \leq C _ {\mathrm {S I}} ^ {A | B} = C _ {\mathrm {S Q I}} ^ {A | B} \leq C _ {r} ^ {A | B}. \tag {81}
$$

Moreover, for bipartite pure states  $|\psi \rangle^{AB}$ , Eq. (79) generalizes as follows (Streltsov, Rana, Bera, and Lewenstein, 2017):

$$
\begin{array}{l} C _ {\mathrm {L I C C}} ^ {A | B} \left(\left| \psi \right\rangle^ {A B}\right) = C _ {\mathrm {L Q I C C}} ^ {A | B} \left(\left| \psi \right\rangle^ {A B}\right) = C _ {\mathrm {S I}} ^ {A | B} \left(\left| \psi \right\rangle^ {A B}\right) = C _ {\mathrm {S Q I}} ^ {A | B} \left(\left| \psi \right\rangle^ {A B}\right) \\ = C _ {r} ^ {A | B} \left(| \psi \rangle^ {A B}\right) = C _ {a} ^ {\infty} \left(\varrho^ {B}\right) = S \left(\Delta \left[ \varrho^ {B} \right]\right). \tag {82} \\ \end{array}
$$

Very recently Wu et al. (2017) provided the first experimental demonstration of assisted coherence distillation. The experiment used polarization-entangled photon pairs for creating pure entangled states and also mixed Werner states. After performing a suitable measurement on one of the photons, the second photon was found in a state with a larger amount of coherence.

Finally, we note that the distillable coherence of collaboration can be regarded as the coherence analog of the entanglement of collaboration presented by Gour and Spekkens (2006).

# 4. Recoverable coherence

The recoverable coherence was introduced by Matera et al. (2016) in the context of a resource theory of control of quantum systems. It is defined in the same way as the distillable coherence of collaboration in Eq. (78), but with the set of LQICC operations replaced by GOIB; see Sec. II.C for their definition. Following the analogy to distillable coherence of collaboration, we denote the recoverable coherence by  $C_{\mathrm{GOIB}}^{A|B}$ . As shown by Matera et al. (2016), the recoverable coherence is additive, convex, monotonic on average under GOIB operations, and upper bounded by the quantum-incoherent relative entropy. Since LQICC is a subset of GOIB operations, we get the following inequality:

$$
C _ {\mathrm {L Q I C C}} ^ {A | B} \leq C _ {\mathrm {G O I B}} ^ {A | B} \leq C _ {r} ^ {A | B}. \tag {83}
$$

Notably the recoverable coherence has an operational interpretation, as it is directly related to the precision of estimating the trace of a unitary via the deterministic quantum computation with one qubit (DQC1) quantum algorithm (Matera et al., 2016); see also Sec. V.B for a more general discussion on the role of coherence in quantum algorithms. Additionally, minimizing the recoverable coherence over all local bases leads to an alternative quantifier of discord (Matera et al., 2016).

# 5. Uncertainty relations and monogamy of coherence

Uncertainty relations for quantum coherence, both for a single party and for multipartite settings, have been studied by Peng et al. (2016) and Singh, Pati, and Bera (2016). If coherence is defined with respect to two different bases  $\{|i\rangle\}$  and  $\{|a\rangle\}$ , the corresponding relative entropies of coherence  $C_r^i$  and  $C_r^a$  fulfill the following uncertainty relation (Singh, Pati, and Bera, 2016):

$$
C _ {r} ^ {i} (\varrho) + C _ {r} ^ {a} (\varrho) \geq - 2 \log_ {2} \left(\max  _ {i, a} | \langle i | a \rangle |\right) - S (\varrho). \tag {84}
$$

For bipartite states  $\varrho^{XY}$ , Singh, Pati, and Bera (2016) derived the following uncertainty relation for the bipartite relative entropies of coherence  $C_r^{ij}$  and  $C_r^{ab}$ :

$$
C _ {r} ^ {i j} \left(\varrho^ {X Y}\right) + C _ {r} ^ {a b} \left(\varrho^ {X Y}\right) \leq 2 \log_ {2} d _ {X Y} - 2 K \left(\varrho^ {X Y}\right). \tag {85}
$$

Here  $d_{XY}$  is the dimension of the composite Hilbert space, and  $K(\varrho^{XY})$  arises from the Lewenstein-Sanpera decomposition $^{16}$ $K(\varrho^{XY}) = \lambda S(\varrho_s^{XY}) + (1 - \lambda)S(\varrho_e^{XY})$ .

The discussion on monogamy of quantum coherence is also inspired by results from entanglement theory (Coffman, Kundu, and Wootters, 2000; Horodecki et al., 2009). In particular, a coherence quantifier  $C$  is called monogamous with respect to the subsystem  $X$  for a tripartite state  $\varrho^{XYZ}$  if (Yao et al., 2015; Kumar, 2017)

$$
C \left(\varrho^ {X Y Z}\right) \geq C \left(\varrho^ {X Y}\right) + C \left(\varrho^ {X Z}\right). \tag {86}
$$

As shown by Yao et al. (2015) and Kumar (2017), the relative entropy of coherence is not monogamous in general, although it can be monogamous for certain families of states. Further results on monogamy of coherence were also presented by Radhakrishnan et al. (2016).

# IV. DYNAMICS OF QUANTUM COHERENCE

Quantum coherence is typically recognized as a fragile feature: the vanishing of coherence in open quantum systems exposed to environmental noise, commonly referred to as decoherence (Breuer and Petruccione, 2002; Zurek, 2003; Schlosshauer, 2005), is perhaps the most distinctive manifestation of the quantum-to-classical transition observed at our macroscopic scales. Numerous efforts have been invested into devising feasible control schemes to preserve coherence in open quantum systems, with notable examples including dynamical decoupling (Viola, Knill, and Lloyd, 1999), quantum feedback control (Rabitz et al., 2000), and error correcting codes (Shor, 1995).

In this section we review more recent work concerning the dynamical evolution of coherence quantifiers (defined in Sec. III) subject to relevant Markovian or non-Markovian evolutions. Coherence effects in biological systems and their potential functional role are discussed in Sec. V. Here we also discuss generic properties of coherence in mixed quantum states, the cohering (and decohering) power of quantum channels, and the role played by coherence quantifiers in defining speed limits for closed and open quantum evolutions.

# A. Freezing of coherence

One of the most interesting phenomena observed in the dynamics of coherence is the possibility for its freezing, that is, complete time invariance without any external control, in the presence of particular initial states and noisy evolutions.

Bromley, Cianciaruso, and Adesso (2015) identified a set of dynamical conditions under which all distance-based coherence monotones  $C_D$  obeying postulates C1, C2 (for the set IO), and C4 stay simultaneously frozen for indefinite time (see also Fig. 1, bottom panel). We summarize these conditions as follows.

Let us consider an open quantum system of  $N$  qubits, each subject to a nondissipative Markovian decoherence channel, representing dephasing the eigenbasis of the  $k$ th Pauli matrix  $\sigma_{k}$ , where  $k = 1$  corresponds to bit flip noise,  $k = 2$  to bit-phase flip noise, and  $k = 3$  to phase flip noise (the latter equivalent to conventional phase damping in the computational basis). Such "  $k$ -flip" channels on each qubit are described by a set of Kraus operators (Nielsen and Chuang, 2010)  $K_{0}(t) = \sqrt{1 - q(t) / 2}\mathbb{1}$ ,  $K_{i,j\neq k}(t) = 0$ , and  $K_{k}(t) = \sqrt{q(t) / 2}\sigma_{k}$ , where  $\{i,j,k\}$  is a permutation of  $\{1,2,3\}$  and  $q(t) = 1 - e^{-\gamma t}$  is the strength of the noise, with  $\gamma$  the decoherence rate. Any such dynamics, mapping a  $N$ -qubit state  $\varrho(0)$  into  $\varrho(t) = \sum_{m_1,\ldots,m_N=0}^{3}[K_{m_1}(t)\otimes \dots \otimes K_{m_N}(t)]\varrho(0)[K_{m_1}(t)\otimes \dots \otimes K_{m_N}(t)]^\dagger$ , is incoherent (in particular, strictly incoherent) with respect to any product basis  $\{|m\rangle\}_{m=0}^{\otimes N}$ , with  $\{|m\rangle\}$  being the eigenbasis of any of the three canonical Pauli operators  $\sigma_m$  on each qubit.

Let us now consider a family of  $N$ -qubit mixed states with all maximally mixed marginals, defined by

$$
\varrho (t) = \frac {1}{2 ^ {N}} \left(\mathbb {1} ^ {\otimes N} + \sum_ {j = 1} ^ {3} c _ {j} (t) \sigma_ {j} ^ {\otimes N}\right), \tag {87}
$$

with  $c_{j} = \mathrm{Tr}[\varrho \sigma_{j}^{\otimes N}]$ . For any even  $N$ , these states span a tetrahedron with vertices  $\{1, (-1)^{N/2}, 1\}$ ,  $\{-1, -(-1)^{N/2}, 1\}$ ,  $\{1, -(-1)^{N/2}, -1\}$ , and  $\{-1, (-1)^{N/2}, -1\}$  in the three-dimensional space of the correlation functions  $\{c_{1}, c_{2}, c_{3}\}$ . In the special case  $N = 2$ , they reduce to Bell diagonal states of two qubits, that is, arbitrary convex mixtures of the four maximally entangled Bell states. Freezing of coherence under  $k$ -flip channels then manifests for the subclass of states of Eq. (87) with initial condition  $c_{i}(0) = (-1)^{N/2} c_{j}(0) c_{k}(0)$  for any even  $N \geq 2$ . For all such states, and for any distance functional  $D(\varrho, \sigma)$  being zero for  $\sigma = \varrho$ , contractive under quantum channels, and jointly convex, one has

$$
C _ {D} (\varrho (t)) = C _ {D} (\varrho (0)) \quad \forall t \geq 0, \tag {88}
$$

where  $C_D$  is a corresponding distance-based quantifier of coherence (see Sec. III.C), and coherence is measured with respect to the product eigenbasis  $\{|j\rangle\}^{\otimes N}$  of the Pauli operator  $\sigma_j^{\otimes N}$  (Bromley, Cianciaruso, and Adesso, 2015; Silva et al., 2016). Notice that the freezing extends as well to the  $l_1$  norm of coherence, as it amounts to the trace distance of coherence in the considered states (up to a normalization factor). For odd  $N$ , including the general case of a single qubit, no measure-independent freezing of coherence can occur instead for the states of Eq. (87), apart from trivial instances; this means that, for all nontrivial evolutions preserving, e.g., the  $l_1$  norm of coherence  $C_{l_1}$ , some other quantifier such as the relative

entropy of coherence  $C_r$  is strictly decreasing (Bromley, Cianciaruso, and Adesso, 2015).

Yu, Zhang, Liu, and Tong (2016) found the relative entropy of coherence to play in fact a special role in identifying conditions such that any coherence monotone is frozen at all times. Specifically, all coherence monotones (respecting, in particular, property C2 for the set SIO) are frozen for an initial state subject to a strictly incoherent channel if and only if the relative entropy of coherence is frozen for such initial state (Yu, Zhang, Liu, and Tong, 2016). In formulas,

$$
C (\varrho (t)) = C (\varrho (0)) \quad \forall C \Leftrightarrow C _ {r} (\varrho (t)) = C _ {r} (\varrho (0)), \tag {89}
$$

where  $\varrho(t) = \Lambda_t[\varrho(0)]$  with  $\Lambda_t \in \mathrm{SIO}$  (see Sec. II.A.2). Using this criterion, one can identify other classes of initial states exhibiting measure-independent frozen coherence under local  $k$ -flip channels (Yu, Zhang, Liu, and Tong, 2016).

We remark that the described freezing effect differs from an instance of decoherence-free subspace (Lidar, 2014), where an open system dynamics acts effectively as a unitary evolution on a subset of quantum states, preserving their informational properties. Here, instead, the purity of the involved states is degraded with time, but their coherence in the chosen reference basis remains unaffected. Other signatures of quantumness such as measures of discord-type correlations can also freeze under the same dynamical conditions (Mazzola, Piilo, and Maniscalco, 2010; Modi et al., 2012; Cianciaruso et al., 2015), albeit only for a finite time in the case of Markovian dynamics. A unified geometric analysis of these phenomena is given in Bromley, Cianciaruso, and Adesso (2015), Cianciaruso et al. (2015), and Silva et al. (2016).

Liu et al. (2016) theoretically explored freezing of coherence for a system of two-level atoms interacting with the vacuum fluctuations of an electromagnetic field bath. A more comprehensive analysis of the dynamics of the  $l_{1}$  norm of coherence for one qubit subject to various types of common noisy channels was reported by Pozzobom and Maziero (2017). The dynamics of the  $l_{1}$  norm of coherence for general  $d$ -dimensional systems was further investigated by M.-L. Hu and Fan (2016), where a factorization relation for the evolution equation of  $C_{l_1}$  was derived, leading, in particular, to a condition for its freezing.

The phenomenon of frozen quantum coherence was demonstrated experimentally in a room temperature nuclear magnetic resonance setup (Silva et al., 2016), with two-qubit and four-qubit ensembles prepared in states of the form (87).

# B. Coherence in non-Markovian evolutions

Some attention has been devoted to the study of coherence in non-Markovian dynamics. Addis et al. (2014) studied the phenomenon of coherence trapping in the presence of non-Markovian dephasing. Namely, for a single qubit subject to non-Markovian pure dephasing evolutions (i.e., a  $k$ -flip channel with  $\gamma t$  replaced by a nonmonotonic function of  $t$ ), the stationary state at  $t \to \infty$  may retain a nonzero coherence in the eigenbasis of  $\sigma_{k}$ , as quantified, e.g., by the  $l_{1}$  norm of coherence. This can occur only in the presence of non-Markovian dynamics and is different from the previously

discussed case of coherence freezing, in which coherence is measured instead with respect to a reference basis transversal to the dephasing direction. Addis et al. (2014) showed that the specifics of coherence trapping depend on the environmental spectrum: its low-frequency band determines the presence or absence of information backflow, while its high-frequency band determines the maximum coherence trapped in the stationary state. Zhang et al. (2015) studied the coherence in the stationary state of a qubit initially correlated with a zero-temperature Ohmic-like bath, realizing a non-Markovian pure dephasing channel. The best dynamical conditions were identified (in terms of initial qubit-bath correlations and bath spectral density) to optimize coherence trapping, that is, to maximize coherence in the stationary qubit state and to minimize the evolution time toward such a state.

The dynamics of the  $l_{1}$  norm of coherence for two qubits globally interacting with a harmonic oscillator bath was investigated by Bhattacharya, Banerjee, and Pati (2016), finding that non-Markovianity slows down the coherence decay. A proposal to witness non-Markovianity of incoherent evolutions via a temporary increase of coherence quantifiers was discussed by Chanda and Bhattacharya (2016), inspired by more general approaches to witness and measure non-Markovianity based on revivals of distinguishability, entanglement, or other informational quantifiers (Rivas, Huelga, and Plenio, 2014; Breuer et al., 2016).

# C. Cohering power of quantum channels and evolutions

The cohering power of a quantum channel (Baumgratz, Cramer, and Plenio, 2014; Mani and Karimipour, 2015) can be defined as the maximum amount of coherence that the channel can create when acting on an incoherent state

$$
\mathcal {P} _ {C} (\Lambda) = \max  _ {\varrho \in \mathcal {I}} C (\Lambda [ \varrho ]), \tag {90}
$$

where  $\mathcal{I}$  denotes the set of incoherent states (with respect to a chosen reference basis) and  $C$  is any quantifier of coherence. In a similar way, Mani and Karimipour (2015) defined the decohering power of a quantum channel  $\Lambda$  as the maximum amount by which the channel reduces the coherence of a maximally coherent state

$$
\mathcal {D} _ {C} (\Lambda) = \max  _ {\varrho \in \mathcal {M}} \left\{C (\varrho) - C (\Lambda [ \varrho ]) \right\}, \tag {91}
$$

where  $\mathcal{M}$  denotes the set of maximally coherent states (with respect to a chosen reference basis) and  $C$  is any quantifier of coherence. If  $C$  is chosen to be convex (i.e., respecting property C4), then the optimizations in Eqs. (90) and (91) are achieved by pure (respectively, incoherent and maximally coherent) states, simplifying the evaluation of the cohering and decohering powers of a quantum channel.

Mani and Karimipour (2015), Xi et al. (2015), Bu and Wu (2016), García-Díaz, Egloff, and Plenio (2016), Situ and Hu (2016), and Bu et al. (2017) calculated the cohering and decohering powers of various unitary and nonunitary quantum channels adopting different quantifiers of coherence. In particular, Mani and Karimipour (2015) showed that  $\mathcal{P}_C(\Lambda) = \mathcal{D}_C(\Lambda)$  for all single-qubit unitary channels when adopting the

Wigner-Yanase skew information as a quantifier of coherence  $C$ .<sup>17</sup> Bu et al. (2017) derived a closed expression for the cohering power of a unitary channel  $U$  when adopting the  $l_{1}$  norm as a quantifier of coherence

$$
\mathcal {P} _ {C _ {l _ {1}}} (U) = \| U \| _ {1 \rightarrow 1} ^ {2} - 1, \tag {92}
$$

where  $\| U\|_{1\to 1} = \max_{\| x\| _1 = 1}\| Ux\| _1$  denotes the maximum column sum matrix norm. This implies that, for the cohering power of a tensor product of unitaries  $\otimes_{j}U_{j}$  with respect to a product basis, one has  $\mathcal{P}_{C_{l_1}}(\otimes_jU_j) + 1 = \prod_j[\mathcal{P}_{C_{l_1}}(U_j) + 1]$ , which generalizes an expression already obtained by Mani and Karimipour (2015) in the case of all equal  $U_{j}$ . Bu et al. (2017) proved that the  $N$ -qubit unitary operation with the maximal  $l_{1}$ -norm cohering power (even including arbitrary global unitaries) is the tensor product  $H^{\otimes N}$  of  $N$  single-qubit Hadamard gates, with  $\mathcal{P}_{C_{l_1}}(H^{\otimes N}) = 2^N -1$ . Further examples of cohering and decohering powers of quantum channels with respect to the  $l_{1}$  norm, relative entropy, and other coherence quantifiers were presented by Xi et al. (2015), Garcia-Diaz, Egloff, and Plenio (2016), Situ and Hu (2016), and Bu et al. (2017).

Bu et al. (2017) provided an operational interpretation for the cohering power. Given a quantum channel  $\Lambda \colon \mathcal{B}(\mathcal{H})\to \mathcal{B}(\mathcal{H})$  acting on a principal system, it is said to be implementable by incoherent operations supplemented by an ancillary quantum system if there exists an incoherent operation IO  $\ni \Lambda_{\mathrm{i}}\colon \mathcal{B}(\mathcal{H}\otimes \mathcal{H}^{\prime})\to \mathcal{B}(\mathcal{H}\otimes \mathcal{H}^{\prime})$  and states  $\sigma ,\sigma^{\prime}\in \mathcal{B}(\mathcal{H}^{\prime})$  of the ancilla such that, for any state  $\varrho \in \mathcal{B}(\mathcal{H})$  of the principal system, one has  $\Lambda_{\mathrm{i}}[\varrho \otimes \sigma ] = \Lambda [\varrho ]\otimes \sigma^{\prime}$ . In this setting, the cohering power of  $\Lambda$  quantifies the minimum amount of coherence to be supplied in the ancillary state  $\sigma$  to make  $\Lambda$  implementable by incoherent operations  $C(\sigma)\geq \mathcal{P}_C(\Lambda)$ , where  $C$  is any coherence monotone fulfilling C1-C4.

On the other hand, García-Díaz, Egloff, and Plenio (2016) and Bu et al. (2017) considered a more general definition of cohering power of a quantum channel  $\Lambda$ , given by the maximum increase of coherence resulting from the action of the channel on an arbitrary state

$$
\tilde {\mathcal {P}} _ {C} (\Lambda) = \max  _ {\varrho} \left\{C (\Lambda [ \varrho ]) - C (\varrho) \right\}, \tag {93}
$$

where  $C$  is any quantifier of coherence and, unlike Eq. (90),  $\varrho$  is not restricted to be an incoherent state. By definition,  $\mathcal{P}_C(\Lambda) \leq \tilde{\mathcal{P}}_C(\Lambda)$ . When considering unitary channels  $U$  and adopting the  $l_{1}$  norm, Garcia-Diaz, Egloff, and Plenio (2016) and Bu et al. (2017) proved that  $\mathcal{P}_C(U) = \tilde{\mathcal{P}}_C(U)$  in the case of a single qubit, but  $\mathcal{P}_C(U) < \tilde{\mathcal{P}}_C(U)$  strictly in any dimension larger than 2. These results were then shown to hold for arbitrary nonunitary channels  $\Lambda$  in Bu and Wu (2016), meaning that in general the maximum coherence gain due to a qubit channel is obtained when acting on an input state with already nonzero coherence.

In addition to channels one may also consider evolutions that are generated by a Hamiltonian  $H$  or a Lindbladian  $\mathcal{L}$  (García-Díaz, Egloff, and Plenio, 2016). For a time evolution  $\Phi_t = e^{\mathcal{L}t}$  we determine the coherence rate

$$
\Upsilon (\mathcal {L}) = \lim  _ {\Delta t \rightarrow 0} \frac {1}{\Delta t} \max  _ {\varrho} [ C (e ^ {\mathcal {L} \Delta t} \varrho) - C (\varrho) ] \tag {94}
$$

and in case of unitary evolutions  $U(t) = e^{-iHt}$  we write

$$
Y (H) = \lim  _ {\Delta t \rightarrow 0} \frac {1}{\Delta t} \max  _ {\varrho} [ C (e ^ {- i H \Delta t} \varrho e ^ {i H \Delta t}) - C (\varrho) ]. \tag {95}
$$

Further alternative approaches to define and quantify the cohering power of quantum channels were pursued recently by Zanardi, Styliaris, and Campos Venuti (2017a, 2017b). Finally, we mention that similar studies have been done in entanglement theory (Zanardi, Zalka, and Faoro, 2000; Linden, Smolin, and Winter, 2009). In particular, Linden, Smolin, and Winter (2009) showed that entangling and disentangling powers of unitaries are not equivalent in general.

# D. Average coherence of random states and typicality

While some dynamical properties of coherence may be dependent on specific channels and initial states, it is also interesting to study typical traits of coherence quantifiers on randomly sampled pure or mixed states. Note that generic random states, exhibiting the typical features of coherence summarized in the following, can be in fact generated by a dynamical model of a quantized deterministic chaotic system, such as a quantum kicked top (Puchała, Pawela, and Žyczkowski, 2016).

Singh, Zhang, and Pati (2016) showed that the relative entropy of coherence (equal to the distillable coherence), the coherence of formation, and the  $l_{1}$  norm of coherence all exhibit the concentration of measure phenomenon, meaning that, with increasing dimension of the Hilbert space, the overwhelming majority of randomly sampled pure states have coherence (according to those quantifiers) taking values very close to the average coherence over the whole Hilbert space. This was proven rigorously resorting to Lévy's lemma, hence showing that states with coherence bounded away from its average value occur with exponentially small probability.

# 1. Average relative entropy of coherence

The exact average of the relative entropy of coherence for pure  $d$ -dimensional states  $|\psi \rangle \in \mathbb{C}^d$  sampled according to the Haar measure was computed by Singh, Zhang, and Pati (2016) finding

$$
\mathbb {E} C _ {r} (| \psi \rangle) = H _ {d} - 1, \tag {96}
$$

where  $H_{d} = \sum_{k=1}^{d}(1/k)$  is the  $d$ th harmonic number. Puchała, Pawela, and Žyczkowski (2016) showed that for large dimension  $d \gg 1$  the average in Eq. (96) tends to  $\mathbb{E}C_{r}(|\psi\rangle) \simeq \log d - (1 - \gamma)$ , with  $\gamma \approx 0.5772$  denoting the Euler constant. This shows that random pure states have

relative entropy of coherence close to (but strictly smaller than by a constant value) the maximum log  $d$  (Puchala, Pawela, and Zyczkowski, 2016; Singh, Zhang, and Pati, 2016).

Typicality of the relative entropy of coherence for random mixed states was investigated by Puchała, Pawela, and Zyczkowski (2016), Zhang (2017), and Zhang, Singh, and Pati (2017). Considering the probability measure induced by partial tracing, that is, corresponding to random mixed states  $\varrho = \mathrm{Tr}_{\mathbb{C}^{d^{\prime}}}|\psi\rangle\langle\psi|$ , with  $|\psi\rangle \in \mathbb{C}^{d} \otimes \mathbb{C}^{d^{\prime}}$  ( $d \leq d^{\prime}$ ) sampled according to the Haar measure, Zhang (2017) and Zhang, Singh, and Pati (2017) derived a compact analytical formula for the average  $\mathbb{E}C_r(\varrho)$ , given by  $\mathbb{E}C_r(\varrho) = (d - 1)/(2d^{\prime})$ . In particular, when considering the flat Hilbert-Schmidt measure (obtained by setting  $d^{\prime} = d$  in the previous expression), one gets

$$
\mathbb {E} C _ {r} (\varrho) = \frac {1}{2} - \frac {1}{2 d}, \tag {97}
$$

which tends asymptotically to a constant  $1/2$  for  $d \to \infty$ . Equation (97) was also independently calculated by Puchała, Pawela, and Zyczkowski (2016), in the limit of large dimension  $d \gg 1$ . The concentration of measure phenomenon for  $C_r$  was then proven by Puchała, Pawela, and Zyczkowski (2016) and Zhang, Singh, and Pati (2017). These results show that random mixed states have significantly less (relative entropy of) coherence than random pure states.

# 2. Average  $l_{1}$  norm of coherence

Concerning the  $l_{1}$  norm of coherence, Singh, Zhang, and Pati (2016) derived a bound to the average  $\mathbb{E}C_{l_1}(|\psi \rangle)$  for pure Haar-distributed  $d$  -dimensional states  $|\psi \rangle$  , exploiting a relation between the  $l_{1}$  norm of coherence and the so-called classical purity (Cheng and Hall, 2015). Then Puchała, Pawela, and Zyczkowski (2016) obtained exact results for the average  $C_{l_1}$  of pure and mixed states in large dimension  $d\gg 1$  , respectively, distributed according to the Haar and Hilbert-Schmidt measures, finding

$$
\mathbb {E} C _ {l _ {1}} (| \psi \rangle) \simeq (d - 1) \frac {\pi}{4}, \quad \mathbb {E} C _ {l _ {1}} (\varrho) \simeq \sqrt {d} \frac {\sqrt {\pi}}{2}. \tag {98}
$$

This shows that, for asymptotically large  $d$ , the  $l_{1}$  norm of coherence of random pure states scales linearly with  $d$  and stays smaller than the maximal value  $(d - 1)$  by a factor  $\pi /4$ , while the  $l_{1}$  norm of coherence of random mixed states scales only with the square root of  $d$ .

# 3. Average recoverable coherence

Matto et al. (2015) considered a qubit interacting with a  $d$ -dimensional environment, of which an  $a$ -dimensional subset is considered accessible, while the remaining  $k$ -dimensional subset (with  $d = ak$ ) is unaccessible. For illustration, one can think of the environment being constituted by  $N$  additional qubits, of which  $N_A$  are accessible and  $N_K = N - N_A$  are unaccessible; in this case  $d = 2^N$ ,  $a = 2^{N_A}$ ,  $k = 2^{N_k}$ . While for  $d \gg 1$  such an interaction leads to decoherence of the principal qubit, its coherence can be partially recovered by quantum erasure, which entails measuring (part of) the

environment in an appropriate basis to erase the information stored in it about the system, hence restoring coherence of the latter. They considered random pure states  $|\psi \rangle \in \mathbb{C}^2 \otimes \mathbb{C}^d$  of the system plus environment composite and studied the average recoverable  $l_{1}$  norm of coherence  $\mathbb{E}C_{l_1}(\varrho)$  of the marginal state  $\varrho$  of the principal qubit, following an optimal measurement on the accessible  $a$ -dimensional subset of the environment. They found that the average recoverable coherence<sup>18</sup> stays close to zero if  $a < k$ , scaling as  $\mathbb{E}C_{l_1}(\varrho) \propto 1 / \sqrt{k}$ , but it transitions to a value close to unity as soon as at least half of the environment becomes accessible, scaling linearly as  $\mathbb{E}C_{l_1}(\varrho) = 1 - k / (4a)$  for  $a \geq k$ . With increasing dimension  $d$ , the transition at  $a = k$  becomes sharper and the distribution of  $C_{l_1}(\varrho)$  becomes more concentrated near its average value, the latter converging to 1 in the limit  $d \to \infty$ . By virtue of typicality, this means that, regardless of how a high-dimensional environment is partitioned, suitably measuring half of it generically suffices to project a qubit immersed in such environment onto a near-maximally coherent state, a fact reminiscent of the quantum Darwinism approach to decoherence (Zurek, 2009; Brandão, Piani, and Horodecki, 2015).

# E. Quantum speed limits

In the dynamics of a closed or open quantum system, quantum speed limits dictate the ultimate bounds imposed by quantum mechanics on the minimal evolution time between two distinguishable states of the system. In particular, consider a quantum system which evolves, according to a unitary dynamics generated by a Hamiltonian  $H$ , from a pure state  $|\psi \rangle$  to a final orthogonal state  $|\psi_{\perp}\rangle = e^{-iH\tau_{\perp} / \hbar}|\psi \rangle$  with  $\langle \psi_{\perp}|\psi \rangle = 0$ . Then seminal investigations showed that the evolution time  $\tau_{\perp}$  is bounded from below as follows:

$$
\tau_ {\perp} (| \psi \rangle) \geq \max  \left\{\pi \hbar / (2 \Delta E), \pi \hbar / (2 E) \right\}, \tag {99}
$$

where  $(\Delta E)^{2} = \langle H^{2}\rangle_{\psi} - \langle H\rangle_{\psi}^{2}$  and  $E = \langle H\rangle_{\psi} - E_0$  (with  $E_0$  the ground state energy), and the two bounds on the right-hand side of Eq. (99) are due to Mandelstam and Tamm (1945) and Margolus and Levitin (1998), respectively. In the last seven decades, a great deal of work has been devoted to identifying more general speed limits, for pure as well as mixed states, and unitary as well as nonunitary evolutions; see, e.g., Taddei et al. (2013), del Campo et al. (2013), and Pires et al. (2016) and references therein. Recent studies have shown, in particular, that quantifiers of coherence, or more precisely of asymmetry, play a prominent role in the determination of quantum speed limits.

Marvian, Spekkens, and Zanardi (2016) studied, for any  $\epsilon > 0$ , the minimum time  $\tau_{\epsilon}^{D}$  necessary for a state  $\varrho$  to evolve under the Hamiltonian  $H$  into a partially distinguishable state  $\varrho_{t} = e^{-iHt}\varrho e^{iHt}$ , such that  $D(\varrho, \varrho_{t}) \geq \epsilon$  according to a distance functional  $D$ . In formula

$$
\tau_ {\epsilon} ^ {D} (\varrho) = \left\{ \begin{array}{l l} \infty , & \text {i f} D \left(\varrho , \varrho_ {t}\right) <   \epsilon \forall t > 0; \\ \min  _ {t > 0} \{t: D \left(\varrho , \varrho_ {t}\right) \geq \epsilon \}, & \text {o t h e r w i s e .} \end{array} \right. \tag {100}
$$

Then for any  $\epsilon > 0$  and for any distance  $D$  which is contractive and jointly convex, Marvian, Spekkens, and Zanardi (2016) proved that  $1 / \tau_{\epsilon}^{D}(\varrho)$ , which represents the average speed of evolution, is an asymmetry monotone of  $\varrho$  with respect to time translations generated by the Hamiltonian  $H$ , being, in particular, monotonically nonincreasing under the corresponding TIO. Interestingly, for pure states, even the inverses of the Mandelstam-Tamm and Margolus-Levitin quantities appearing on the right-hand side of Eq. (99) are themselves asymmetry monotones, bounding the asymmetry monotone given by  $1 / \tau_{\perp}(|\psi\rangle)$ . Marvian, Spekkens, and Zanardi (2016) then derived new Mandelstam-Tamm-type quantum speed limits for unitary dynamics based on various measures of distinguishability, including a bound featuring the Wigner-Yanase skew information with respect to  $H$  (obtained when  $D$  is set to the relative Rényi entropy of order  $1/2$ ), which was also independently obtained by Mondal, Datta, and Sazim (2016).

Pires et al. (2016) developed a general approach to Mandelstam-Tamm-type quantum speed limits for all physical processes. Given a metric  $g$  on the quantum state space, let  $\ell_{\Lambda}^{g}(\varrho ,\varrho_{\tau})$  denote the length of the path connecting an initial state  $\varrho$  to a final state  $\varrho_{\tau} = \Lambda [\varrho ]$  under a (generally open) dynamics  $\Lambda$ . Quantum speed limits then ensue from a simple geometric observation, namely, that the geodesic connecting  $\varrho$  to  $\varrho_{\tau}$ , whose length can be indicated by  $\mathcal{L}^g (\varrho ,\varrho_\tau)$ , is the path of shortest length among all physical evolutions between the given initial and final states  $\mathcal{L}^g (\varrho ,\varrho_\tau)\leq \ell_{\Lambda}^g (\varrho ,\varrho_\tau)\forall \Lambda$ . Then Pires et al. (2016) considered the infinite family of quantum speed limits derived from this geometric principle, with  $g$  denoting any possible quantum Riemannian contractive metric (Morozova and Cencov, 1991; Petz, 1996; Petz and Ghinea, 2011), including two prominent asymmetry monotones: quantum Fisher information and Wigner-Yanase skew information (see Sec. III.K.1). For any given dynamics  $\Lambda$  and pair of states  $\varrho ,\varrho_{\tau}$ , one can identify the tightest speed limit as the one corresponding to the metric  $g$  such that the length of the dynamical path  $\ell_{\Lambda}^{g}$  is the closest to the corresponding geodesic length. In formula, the tightest speed limit is obtained by minimizing the ratio

$$
\delta_ {\Lambda} ^ {g} = \frac {\ell_ {\Lambda} ^ {g} (\varrho , \varrho_ {\tau}) - \mathcal {L} ^ {g} (\varrho , \varrho_ {\tau})}{\mathcal {L} ^ {g} (\varrho , \varrho_ {\tau})}, \tag {101}
$$

over the metric  $g$ . Several examples are presented by Pires et al. (2016), demonstrating the importance of choosing different information metrics for open system dynamics, as well as clarifying the roles of classical populations versus quantum coherences in the determination and saturation of the speed limits. In particular, in the case of a single qubit, while for any unitary dynamics the speed limit based on the quantum Fisher information (Taddei et al., 2013) is always tighter than the one based on the Wigner-Yanase skew information, this is no longer true when considering nonunitary dynamics.

Specifically, for parallel and transversal dephasing, as well as amplitude damping dynamics, Pires et al. (2016) derived new tighter speed limits based on the Wigner-Yanase skew information. We finally mention that looser speed limits involving the skew information were also recently presented by Pires, Céleri, and Soares-Pinto (2015) and Mondal, Datta, and Sazim (2016).

The speed of a two-qubit photonic system—quantified by the family of asymmetry monotones associated with the quantum Riemannian contractive metrics—undergoing a controlled unitary evolution, was measured experimentally by C. Zhang et al. (2016), by means of an all-optical direct detection scheme requiring less measurements than full state tomography.

# V. APPLICATIONS OF QUANTUM COHERENCE

In this section we discuss applications of quantum coherence to a variety of fields, ranging from quantum information processing to quantum sensing and metrology, thermodynamics, and biology. Particular emphasis is given to those settings in which a specific coherence monotone introduced in Sec. III acquires an operational interpretation, hence resulting in novel insights stemming from the characterization of quantum coherence as a resource.

# A. Quantum thermodynamics

Recently, the role of coherence in quantum thermodynamics was discussed by several authors. We review the main concepts in the following, being in large part based on the resource theory of quantum thermodynamics (Brandão et al., 2013; Gour et al., 2015; Goold et al., 2016) defined by the framework of thermal operations (Janzing et al., 2000).

# 1. Thermal operations

In the following, we considered a system  $S$  and an environment  $E$  with a total Hamiltonian  $H_{SE} = H_{S} + H_{E}$ . Given a state of the system  $\varrho^{S}$ , a thermal operation on this state is defined as (Janzing et al., 2000)

$$
\Lambda_ {\mathrm {t h}} \left[ Q ^ {S} \right] = \operatorname {T r} _ {E} \left[ U Q ^ {S} \otimes \gamma^ {E} U ^ {\dagger} \right], \tag {102}
$$

where  $\gamma^{E} = e^{-\beta H_{E}} / \mathrm{Tr}[e^{-\beta H_{E}}]$  is a thermal state of the environment with the inverse temperature  $\beta = 1 / k_{\mathrm{B}}T$  and we demand that the unitary  $U$  commutes with the total Hamiltonian  $[U, H_{SE}] = 0$ .

The importance of thermal operations arises from the fact that they are consistent with the first and second laws of thermodynamics (Lostaglio et al., 2015). In particular, since the unitary  $U$  commutes with the total Hamiltonian, these operations preserve the total energy of the system and environment. Moreover, they do not increase the Helmholtz free energy<sup>19</sup>

$$
F \left(\varrho^ {S}\right) = \operatorname {T r} \left[ \varrho^ {S} H _ {S} \right] - k _ {\mathrm {B}} T S \left(\varrho^ {S}\right), \tag {103}
$$

i.e., for any two states  $\varrho^S$  and  $\sigma^S = \Lambda_{\mathrm{th}}[\varrho^S]$  it holds that  $F(\sigma^{S})\leq F(\varrho^{S})$

Thermal operations also have two other important properties (Lostaglio, Jennings, and Rudolph, 2015; Lostaglio et al., 2015). First, they are TIO with respect to the Hamiltonian  $H_{S}$ , i.e.,

$$
\Lambda_ {\mathrm {t h}} \left[ e ^ {- i H _ {S} t} \varrho^ {S} e ^ {i H _ {S} t} \right] = e ^ {- i H _ {S} t} \Lambda_ {\mathrm {t h}} \left[ \varrho^ {S} \right] e ^ {i H _ {S} t}. \tag {104}
$$

Second, they preserve the Gibbs state  $\Lambda_{\mathrm{th}}[\gamma^S] = \gamma^S$ . As discussed by Lostaglio, Jennings, and Rudolph (2015) and Lostaglio et al. (2015), these two properties are related to the first and second laws of thermodynamics, respectively. In particular, preservation of the Gibbs state implies that no work can be extracted from a thermal state.

A closely related concept is known as Gibbs-preserving operations (Ruch and Mead, 1976; Faist, Oppenheim, and Renner, 2015). Here preservation of the thermal state is the only requirement on the quantum operation. Interestingly, Faist, Oppenheim, and Renner (2015) showed that these maps are strictly more powerful than thermal operations. In particular, Gibbs-preserving operations can create coherence from incoherent states, while this cannot be done via thermal operations.

# 2. State transformations via thermal operations

Several recent works studied necessary and sufficient conditions for two states  $\varrho$  and  $\sigma$  to be interconvertible via thermal operations. In the absence of coherence, i.e., if  $\varrho^S$  is diagonal in the eigenbasis of  $H_{S}$ , such conditions were presented by Horodecki and Oppenheim (2013a) and termed thermomajorization.[20] More general conditions which allow for the addition of ancillas and catalytic conversions (Jonathan and Plenio, 1999), known as the second laws of quantum thermodynamics, were presented by Brandão et al. (2015). They can also be applied to the situation where the state  $\varrho^S$  has coherence. Interestingly, for interconversion of single-qubit states via thermal operations, Čwiklínski et al. (2015) found a simple set of necessary and sufficient conditions, in terms of a so-called damping matrix positivity. Similar considerations were also presented for other classes of operations such as enhanced thermal operations (Čwiklínski et al., 2015) and cooling maps (Narasimhachar and Gour, 2015).

In the previous discussion the state of the environment  $\gamma^{E}$  was assumed to be a thermal state. In the recent literature on quantum thermodynamics, this constraint has been relaxed, allowing  $\gamma^{E}$  to be a general state of the environment. As discussed by Lostaglio, Jennings, and Rudolph (2017), it is important to distinguish between two cases: namely, whether the state  $\gamma^{E}$  is incoherent, or has nonzero coherence, with respect to the eigenbasis of  $H_{E}$ .

In both cases it is also assumed that an arbitrary number of copies of  $\gamma^{E}$  are available, which is a usual assumption from the point of view of resource theories. An important result in this respect was obtained by Lostaglio et al. (2015). There it was shown that by allowing for an arbitrary number of copies of the Gibbs state together with some other incoherent state  $\gamma^{E}$ , the operation in Eq. (102) can be used to approximate any incoherent state of the system, i.e., any state which is diagonal in the eigenbasis of the Hamiltonian  $H_{S}$ . Moreover, in this case it is possible to implement any TIO (Lostaglio et al., 2015). Although these processes can be used to perform an arbitrary amount of work, they are still limited in the sense that they cannot create coherence (Lostaglio, Jennings, and Rudolph, 2017). The situation changes if the state  $\gamma^{E}$  has coherence. In this case the process in Eq. (102) can also be used to perform an arbitrary amount of work, and apart from that the process can also create coherence in the system. However, even in this case the theory is nontrivial, i.e., not all transformations are possible (Lostaglio et al., 2015; Lostaglio, Jennings, and Rudolph, 2017).

The role of coherence in quantum thermodynamics was further studied by Misra et al. (2016), where they analyzed the physical situation in which the resource theories of coherence and thermodynamics play competing roles. In particular, they investigated the creation of coherence for a quantum system (with respect to the eigenbasis of its Hamiltonian  $H$ ) via unitary operations from a thermal state and also explored the energy cost for such coherence creation. Given an initial thermal state  $\varrho_{T} = e^{-\beta H} / \mathrm{Tr}[e^{-\beta H}]$  at temperature  $T = 1 / \beta$  (setting  $k_{\mathrm{B}} = 1$ ), Misra et al. (2016) showed that there always exists a unitary transformation (in fact, a real orthogonal one) which maps  $\varrho_{T}$  into a state  $\varrho^{\prime}$  such that its diagonal  $\Delta [\varrho^{\prime}] = \varrho_{T^{\prime}}$  amounts to a thermal state at temperature  $T^{\prime} > T$ . This creates the maximal relative entropy of coherence  $C_{r,\max}^{\Delta E} = S(\varrho_{T^{\prime}}) - S(\varrho_{T})$ , at the cost of spending an amount of energy  $\Delta E = \mathrm{Tr}[H(\varrho_{T^{\prime}} - \varrho_{T})]$ .

# 3. Work extraction and quantum thermal machines

Interestingly, coherence cannot be converted to work in a direct way. This phenomenon is known as work locking (Horodecki and Oppenheim, 2013a; Skrzypczyk, Short, and Popescu, 2014; Lostaglio, Jennings, and Rudolph, 2015) and can be formalized as follows (Korzekwa et al., 2016):

$$
\langle W \rangle \left(\varrho^ {S}\right) \leq \langle W \rangle \left(\Pi \left[ \varrho^ {S} \right]\right). \tag {105}
$$

Here  $\langle W\rangle (\varrho^S)$  denotes the amount of work that can be extracted from the state  $\varrho^S$ , and  $\Pi [\varrho^S] = \sum_i\mathrm{Tr}[\Pi_i\varrho^S ]\Pi_i$  where  $\Pi_{i}$  are projectors onto the eigenspaces of  $H_{S}$ . Note that the operation  $\Pi$  is in general different from the full dephasing  $\Delta$  defined in Eq. (5), since the latter removes all off-diagonal elements, while  $\Pi$  preserves some off-diagonal elements if the Hamiltonian  $H_{S}$  has degeneracies. A detailed study of this problem was also presented by Korzekwa et al. (2016), where it was shown that work extraction from coherence is still possible in certain scenarios. This relies on the repeated use of a coherent ancilla in a catalytic way as shown by Åberg (2014). Further results on the role of coherence for work extraction have also been presented by

Kammerlander and Anders (2016). Moreover, it was shown by Vacanti, Elouard, and Auffeves (2015) that work is typically required for keeping coherent states out of thermal equilibrium. The role of coherence in determining the distribution of work done on a quantum system was also studied by Solinas and Gasparinetti (2015, 2016).

The role played by coherence in the operation of quantum thermal machines, such as heat engines and refrigerators, was investigated recently (Scully et al., 2011; Rahav, Harbola, and Mukamel, 2012). Various authors have explored the use of optical coherence, in the form of squeezing in a thermal bath, to push the performance of nanoscale heat engines and quantum absorption refrigerators beyond their classical limitations (Abah and Lutz, 2014; Correa et al., 2014; Roßnagel et al., 2014; Manzano et al., 2016; Niedenzu et al., 2016). However, the advantages found in these studies are not directly related to a processing of coherence, but originate at least in part from the fact that, in energetic terms, a squeezed bath has an energy content which is equivalent to that of a thermal bath at a higher effective temperature. Quantum coherence was also shown to be useful for transient cooling in absorption refrigerators (Mitchison et al., 2015). More generally, Uzdin, Levy, and Kosloff (2015) established the thermodynamical equivalence of all engine types in the quantum regime of small action (compared to  $\hbar$ ). They then identified generic coherent and incoherent work extraction mechanisms and showed that coherence enables power outputs that can reach significantly beyond the power of incoherent (i.e., stochastic) engines.

It is noteworthy that the control of any engine, especially an autonomous device, requires a clock in order to switch on and off an interaction at specified moments in time, and thereby control the device. At the quantum level, such a control leads to correlations and thus a possible loss of coherence in the clock. Woods, Silva, and Oppenheim (2016) addressed the question of the coherence cost of such control via clocks and establishes limits on the backaction on the clock, and therefore its resource consumption, in terms of energy and coherence.

# B. Quantum algorithms

The role of coherence in quantum algorithms was discussed by Hillary (2016), with particular focus on the Deutsch-Jozsa algorithm (Deutsch and Jozsa, 1992). This quantum algorithm can decide whether a boolean function is constant or balanced by just one evaluation of the function, while in the classical case the number of evaluations grows exponentially in the number of input bits. As shown by Hillary (2016), coherence is a resource in this protocol in the sense that a smaller amount of coherence in the protocol increases the error of guessing whether the underlying function was constant or balanced.

A similar investigation with respect to the Grover algorithm (Grover, 1997) was performed by Anand and Pati (2016) and Shi et al. (2017). Anand and Pati (2016) studied the relation between coherence and success probability in the analog Grover algorithm, which is a version of the original Grover algorithm based on adiabatic Hamiltonian evolution. It was found that the success probability  $p_{\mathrm{succ}}$  of the algorithm is related to the amount of coherence in the corresponding quantum state as follows (Anand and Pati, 2016):

$$
C _ {l _ {1}} \left(p _ {\text {s u c c}}\right) = 2 \sqrt {p _ {\text {s u c c}} \left(1 - p _ {\text {s u c c}}\right)}, \tag {106}
$$

$$
C _ {r} \left(p _ {\text {s u c c}}\right) = - p _ {\text {s u c c}} \log_ {2} p _ {\text {s u c c}} - \left(1 - p _ {\text {s u c c}}\right) \log_ {2} \left(1 - p _ {\text {s u c c}}\right). \tag {107}
$$

Another important quantum algorithm is known as the DQC1 (Knill and Laflamme, 1998). This quantum algorithm provides an exponential speedup over the best known classical procedure for estimating the trace of a unitary matrix (given as a sequence of two-qubit gates). Interestingly, this algorithm requires vanishingly little entanglement[21] (Datta, Flammia, and Caves, 2005), but a typical instance of DQC1 has nonzero quantum discord (Datta, Shaji, and Caves, 2008). The role of quantum discord for DQC1 was later questioned by Dakić, Vedral, and Brukner (2010), who showed that certain nontrivial instances do not involve any quantum correlations. This issue was further discussed by Datta and Shaji (2011). Thus, the question of which type of quantumness correctly captures the performance of this algorithm remained open. The role of coherence for DQC1 was first studied by Ma et al. (2016) and later by Matera et al. (2016). The latter work indicates that coherence is indeed a suitable figure of merit for this protocol. In particular, Matera et al. (2016) showed that the precision of the algorithm is directly related to the recoverable coherence, defined in Sec. III.L.4.

# C. Quantum metrology

The main goal of quantum metrology (Braunstein and Caves, 1994; Braunstein, Caves, and Milburn, 1996; Giovannetti, Lloyd, and Maccone, 2004, 2006) is to overcome classical limitations in the precise estimation of an unknown parameter  $\varphi$  encoded, e.g., in a unitary evolution  $U_{\varphi} = e^{-i\varphi H}$ . Applications of quantum metrology include phase estimation for accelerometry, optical and gravitational wave interferometry, high precision clocks, navigation devices, magnetometry, thermometry, remote sensing, and superresolution imaging (Paris, 2009; Giovannetti, Lloyd, and Maccone, 2011).

As one can appreciate by the following simple example, quantum coherence plays a fundamental role in this task. For simplicity, let  $H$  be a nondegenerate single-qubit Hamiltonian  $H = E_0|0\rangle\langle 0| + E_1|1\rangle\langle 1|$ . A very simple possibility to estimate  $\varphi$  is to apply the unitary to a single-qubit state  $|\psi\rangle = a|0\rangle + b|1\rangle$ , and to perform a measurement on the final state  $U_{\varphi}|\psi\rangle = ae^{-i\varphi E_0}|0\rangle + be^{-i\varphi E_1}|1\rangle$ . If the probe state  $|\psi\rangle$  has no coherence in the eigenbasis of  $H$  (i.e.,  $a = 0$  or  $b = 0$ ), the final state  $U_{\varphi}|\psi\rangle$  will be the same as  $|\psi\rangle$  up to an irrelevant global phase, i.e., from the final measurement we cannot gain any information about the parameter  $\varphi$ . On the other hand, if  $a$  and  $b$  are both nonzero, it is always possible to extract information about  $\varphi$  via a suitable measurement.

In general, given an initial probe state  $\varrho$  and assuming the probing procedure is repeated  $n$  times, the mean square error  $(\Delta \varphi)^2$  in the estimation of  $\varphi$  is bounded below by the quantum Cramér-Rao bound (Braunstein and Caves, 1994)

$$
\left(\Delta \varphi\right) ^ {2} \geq \frac {1}{n I (\varrho , H)}, \tag {108}
$$

where  $I(\varrho, H)$  is the quantum Fisher information, a quantifier of asymmetry (i.e., of unspeakable coherence) (Marvian and Spekkens, 2016) defined in Eq. (67). As the bound in Eq. (108) is asymptotically achievable for  $n \gg 1$  by means of a suitable optimal measurement, the quantum Fisher information directly quantifies the optimal precision of the estimation procedure and is thus regarded as the main figure of merit in quantum metrology (Paris, 2009; Giovannetti, Lloyd, and Maccone, 2011).

Using only probe states without any coherence or entanglement, the quantum Fisher information can scale at most linearly with  $n$ ,  $I(\varrho, H) \sim n$ . However, starting from a probe state  $\varrho$  with coherence (e.g., the maximally coherent state given by  $a = b = 1 / \sqrt{2}$  in the previous example) and applying  $U_{\varphi}$  sequentially  $n$  times before the final measurement allows one to reach the so-called Heisenberg scaling  $I(\varrho, H) \sim n^2$ , which yields a genuine quantum enhancement in precision (Giovannetti, Lloyd, and Maccone, 2006). In this clear sense, quantum coherence in the form of asymmetry is the primary resource behind the power of quantum metrology.

More generally, Marvian and Spekkens (2016) proved that any function which quantifies the performance of probe states  $\varrho$  in the metrological task of estimating a unitarily encoded parameter  $\varphi$  should be a quantifier of asymmetry with respect to translations  $U_{\varphi}$  induced by the generator  $H$ . Notice that if the parameter  $\varphi$  is identified with time  $t$ , the quantum Fisher information and related quantifiers of asymmetry (C. Zhang et al., 2016), as discussed in Sec. III.K.1, acquire an interpretation as the speed of evolution of the probe state  $\varrho$  under the dynamics  $U_{t}$  generated by  $H$ . This highlights the role of coherence quantifiers in the determination of quantum speed limits as reviewed in Sec. IV.E.

In the absence of noise, the Heisenberg scaling can be equivalently achieved using  $n$  entangled probes in parallel, each subject to one instance of  $U_{\varphi}$  (Huelga et al., 1997; Giovannetti, Lloyd, and Maccone, 2006). A great deal of work has been devoted to characterizing possibilities and limitations for quantum metrology in the presence of various sources of noise, which result in loss of coherence or entanglement of the probes (Huelga et al., 1997; Escher, de Matos Filho, and Davidovich, 2011; Giovannetti, Lloyd, and Maccone, 2011; Chin, Huelga, and Plenio, 2012; Demkowicz-Dobrzański, Kolodynski, and Guta, 2012; Chaves et al., 2013; Demkowicz-Dobrzański and Maccone, 2014; Nichols et al., 2016; Smirne et al., 2016; Braun et al., 2017). Typically the Heisenberg scaling is not retained, except under some error models which allow for the successful implementation of suitable quantum error correcting procedures (Preskill, 2000; Macchiavello et al., 2002; Arrad et al., 2014; Dür et al., 2014; Kessler et al., 2014; Sekatski et al., 2016; Unden et al., 2016).

An alternative investigation on the role of coherence in quantum metrology was carried out by Giorda and Allegra (2016b), where a relation was derived between the quantum Fisher information and the second derivative of the relative entropy of coherence, the latter evaluated with respect to the optimal measurement basis in a (unitary or noisy) parameter estimation process.

# D. Quantum channel discrimination

Quantum coherence also plays a direct role in quantum channel discrimination, a variant of quantum metrology where the task is not to identify the value of an unknown parameter  $\varphi$ , but to distinguish between a set of possible values  $\varphi$  can take. In the case of a binary channel discrimination, in particular, deciding whether a unitary  $U_{\varphi} = e^{-i\varphi H}$  is applied or not to a local probe (i.e., distinguishing between  $U_{\varphi}$  and the identity), the Wigner-Yanase skew information defined in Eq. (65) has been linked to the minimum error probability of the discrimination (Girolami, Tufarelli, and Adesso, 2013; Farace et al., 2014; Girolami, 2014).

More recently, the task of quantum phase discrimination was studied by Napoli et al. (2016) and Piani et al. (2016) (see also Fig. 1, left panel). Consider a  $d$ -dimensional probe and a set of unitary channels  $\{U_{\varphi}\}$  generated by  $H = \sum_{i=0}^{d-1} i|i\rangle \langle i|$ , where  $\{|i\rangle\}$  sets the reference incoherent basis for the probe system and  $\varphi$  can take any of the  $d$  values  $\{2\pi k / d\}_{k=0}^{d-1}$  with uniform probability  $1 / d$ . One such channel acts on the probe, initialized in a state  $\varrho$ , and the goal is to guess which channel instance has occurred (i.e., to identify the correct value of  $\varphi$ ) with the highest probability of success. Using any probe state  $\sigma \in \mathcal{I}$  which is incoherent with respect to the eigenbasis of  $H$ , no information about  $\varphi$  is imprinted on the state and the probability  $p_{\mathrm{suc}}(\sigma)$  of guessing its correct value is simply given by  $1 / d$ , corresponding to a random guess. On the other hand, a probe state  $\varrho$  with coherence in the eigenbasis of  $H$ , accompanied by an optimal measurement at the output, allows one to achieve a better discrimination, leading to a higher probability of success  $p_{\mathrm{suc}}(\varrho) \geq p_{\mathrm{suc}}(\sigma)$ .

The enhancement in the probability of success for this task when exploiting a coherent state  $\varrho$ , compared to the use of any incoherent state  $\sigma \in \mathcal{I}$ , is given exactly by the robustness of coherence of  $\varrho$  defined in Eq. (52) (Napoli et al., 2016; Piani et al., 2016):

$$
\frac {p _ {\text {s u c c}} (\varrho)}{p _ {\text {s u c c}} (\sigma)} = 1 + R _ {C} (\varrho). \tag {109}
$$

This provides a direct operational interpretation for the robustness of coherence  $R_{C}$  in quantum discrimination tasks. Such an interpretation can be extended to more general channel discrimination scenarios (i.e., with nonuniform prior probabilities and including nonunitary incoherent channels) and carries over to the robustness of asymmetry with respect to arbitrary groups (Napoli et al., 2016; Piani et al., 2016).

# E. Witnessing quantum correlations

Recently, several authors tried to find Bell-type inequalities for various coherence quantifiers. In particular, Bu and Wu

(2016) considered quantifiers of coherence of the form  $C(X, Y, \varrho^{AB})$ , where  $X$  and  $Y$  are local observables on the subsystem  $A$  and  $B$ , respectively, and the coherence is considered with respect to the eigenbasis of  $X \otimes Y$ . They found a Bell-type bound for this quantity for all product states  $\varrho^A \otimes \varrho^B$  and showed that the bound is violated for maximally entangled states and a certain choice of observables  $X$  and  $Y$ . In a similar spirit, the interplay between coherence and quantum steering was investigated by Mondal and Mukhopadhyay (2015) and Mondal, Pramanik, and Pati (2017), where steering inequalities for various coherence quantifiers were found, and by X. Hu and Fan (2016) and Hu et al. (2016), where the maximal coherence of steered states was investigated.

As further shown by Girolami and Yadin (2017), detection of coherence can also be used to witness multipartite entanglement. In particular, an experimentally accessible lower bound on the quantum Fisher information (which does not require full state tomography) can serve as a witness for multipartite entanglement, as explicitly demonstrated for mixtures of Greenberger-Horne-Zeilinger states (Girolami and Yadin, 2017). This builds on previous results on detecting different classes of multipartite entanglement using the quantum Fisher information (Pezzé and Smerzi, 2009, 2014; Hyllus et al., 2012; Tóth, 2012; Tóth and Apellaniz, 2014).

# F. Quantum biology and transport phenomena

Transport is fundamental to a wide range of phenomena in the natural sciences and it has long been appreciated that coherence can play an important role for transport, e.g., in the solid state (Deveaud-Plédran, Quattropani, and Schwendimann, 2009; Li et al., 2012). Recently, however, some research efforts have started to investigate the role of coherence in the perhaps surprising arena of "warm, wet, and noisy" biological systems. Motivated in part by experimental observations using ultrafast electronic spectroscopy of light-harvesting complexes in photosynthesis (Engel et al., 2007; Collini et al., 2010) the beneficial interplay of coherent and incoherent dynamics has been identified as a key theme (Mohseni et al., 2008; Plenio and Huelga, 2008; Caruso et al., 2009; Rebentrost, Mohseni, and Aspuru-Guzik, 2009; Rebentrost et al., 2009) in biological transport and more generally in the context of biological function (Huelga and Plenio, 2013). It is now recognized that typically both coherent and noise dynamics are required to achieve optimal performance.

A range of mechanisms to support this claim and understand its origin qualitatively [see Huelga and Plenio (2013) for an overview] has been identified. These include constructive and destructive interference due to coherence and its suppression by decoherence (Caruso et al., 2009) as well as the interaction between electronic and long-lived vibrational degrees of freedom (coherent) (Chin et al., 2010, 2013; Prior et al., 2010; Christensson et al., 2012; Kolli et al., 2012; Womick et al., 2012; O'Reilly and Olaya-Castro, 2014; Roden, Bennett, and Whaley, 2016) in the environment and with a broadband vibrational (incoherent) background (Mohseni et al., 2008; Plenio and Huelga, 2008; Caruso et al., 2009; Rebentrost, Mohseni, and Aspuru-Guzik, 2009; Rebentrost et al., 2009). Nevertheless, the detailed role played

by coherence and coherent dynamics in these settings remains to be unraveled and quantified and it is here where the detailed quantitative understanding of coherence emerging from its resource theory development may be beneficial.

Initially, researchers studied the entanglement properties of states (Caruso et al., 2009; Fassioli and Olaya-Castro, 2010; Sarovar et al., 2010) and evolutions (Caruso et al., 2010) that emerge in biological transport dynamics. It should be noted though that in the regime of application the quantities considered by Sarovar et al. (2010) amount to coherence quantifiers rather than purely entanglement quantifiers. In the studies of the impact of coherence on transport dynamics, formal approaches using coherence and asymmetry quantifiers based on the Wigner-Yanase skew information were used (Vatasescu, 2015, 2016), but the connection to function has remained tenuous so far. It was indeed noted that it may become necessary to separately quantify real and imaginary parts of coherence as these can have significantly different effects on transport (Roden and Whaley, 2016). Another question of interest in this context concerns that of the distinction between classical and quantum coherence (O'Reilly and Olaya-Castro, 2014) and dynamics (Wilde, McCracken, and Mizel, 2009; Li et al., 2012) in biological systems, most notably photosynthetic units.

Finally, note that there are other biological phenomena that are suspected to benefit from coherent and incoherent dynamics, notably magnetoreception in birds (Ritz, Adem, and Schulten, 2000; Cai, Guerreschi, and Briegel, 2010; Gauger et al., 2011), where the role of coherence in the proposed radical pair mechanism was studied on the basis of coherence quantifiers (Kominis, 2015) and the molecular mechanisms underlying olfaction (Turin, 1996). Unlike photosynthesis, however, experimental evidence is still limited and not yet at a stage where conclusions drawn from the quantitative theory of coherence as a resource can be verified.

# G. Quantum phase transitions

Coherence and asymmetry quantifiers have been employed to detect and characterize quantum phase transitions, i.e., changes in the ground state of many-body systems occurring at or near zero temperature and driven purely by quantum fluctuations. The critical points can be identified by witnessing a particular feature in a chosen coherence quantifier, such as a divergence, a cusp, an inflection, or a vanishing point.

Karpat, Cakmak, and Fanchini (2014) and Cakmak, Karpat, and Fanchini (2015) showed that single-spin coherence reliably identifies the second-order quantum phase transition in the thermal ground state of the anisotropic spin-  $1 / 2$ $XY$  chain in a transverse magnetic field. In particular, the single-spin skew information with respect to the Pauli spin-  $x$  operator  $\sigma_{x}$ , as well as its experimentally friendly lower bound which can be measured without state tomography (Girolami, 2014), exhibits a divergence in its derivative at the critical point, even at relatively high temperatures.

Malvezzi et al. (2016) extended the previous analysis to ground states of spin-1 Heisenberg chains. Focusing on the one-dimensional XXZ model, they found that no coherence and asymmetry quantifier (encompassing skew information, relative entropy, and  $l_{1}$  norm) is able to detect the triple point

of the infinite-order Kosterlitz-Thouless transition, while the single-spin skew information with respect to a pair of complementary observables  $\sigma_{x}$  and  $\sigma_z$  can instead be employed to successfully identify both the Ising-like second-order phase transition and the SU(2) symmetry point.

Further applications of coherence and asymmetry quantifiers to detecting quantum phase transitions in fermionic and spin models have been reported by Chen, Cui et al. (2016) and Li and Lin (2016).

# VI. CONCLUSIONS

In this Colloquium we have seen that quantum coherence plays an important role in quantum information theory, quantum thermodynamics, and quantum biology, as well as physics more widely. Similar to entanglement, but even more fundamental, coherence can be regarded as a resource, if the experimenter is limited to quantum operations which cannot create coherence. The latter set of operations is not uniquely specified: in Sec. II we reviewed the main approaches in this direction, their motivation, and their main differences. Most of these approaches have some desirable properties which distinguish them from the other frameworks.

It is instrumental to compare once again the resource theory of coherence to the resource theory of entanglement. The latter has a natural approach which is defined by the set of LOCC operations. This set of operations has a clear physical motivation and several nice properties which make exact evaluation tractable in many relevant situations. In particular, this approach has a golden unit, since any bipartite quantum state can be created via LOCC operations from a maximally entangled state.

In the following, we provide six simple conditions which we believe any physical theory of quantum coherence as a resource should be tested on. These conditions are motivated by recent developments on the resource theories of coherence and entanglement. In particular, we propose that any resource theory of coherence should have a set of free operations  $\mathcal{F}$  with the following properties:

(1) Physical motivation: The set of operations  $\mathcal{F}$  has a well-defined physical justification.  
(2) Postselection: The set  $\mathcal{F}$  allows for postselection, i.e., there is a well-defined prescription for performing multioutcome measurements and obtaining corresponding probabilities and postmeasurement states.  
(3) No coherence creation: The set  $\mathcal{F}$  (including postselection) cannot create coherence from incoherent states.  
(4) Free incoherent states: The set  $\mathcal{F}$  allows one to create any incoherent state from any other state.  
(5) Golden unit: The set  $\mathcal{F}$  allows one to convert the maximally coherent state  $|\Psi_d\rangle$  to any other state of the same dimension.  
(6) No bound coherence: Given many copies of some (coherent) state  $\varrho$ , the set  $\mathcal{F}$  allows one to extract maximally coherent single-qubit states  $|\Psi_{2}\rangle$  at a nonzero rate.

While conditions 2-6 can be tested directly, the first condition seems to be the most demanding. In Table II we list the status of conditions 2-6 for the existing sets MIO, IO, SIO, DIO,

TABLE II. List of alternative frameworks of coherence with respect to our criteria 1-6 provided in the text. For the first criterion we give the corresponding literature reference. Unknown entries are denoted by “?.”  

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>MIO</td><td>Åberg (2006)</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>IO</td><td>Baumgratz, Cramer, and Plenio (2014) and Winter and Yang (2016)</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>SIO</td><td>Winter and Yang (2016) and Yadin et al. (2016)</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>?</td></tr><tr><td>DIO</td><td>Chitambar and Gour (2016b) and Marvian and Spekkens (2016)</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>?</td></tr><tr><td>TIO</td><td>Marvian and Spekkens (2016) and Marvian, Spekkens, and Zanardi (2016)</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td><td>?</td></tr><tr><td>PIO</td><td>Chitambar and Gour (2016b)</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td><td>?</td></tr><tr><td>GIO</td><td rowspan="2">de Vicente and Streltsov (2017)</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>No</td></tr><tr><td>FIO</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>?</td></tr></table>

TIO, PIO, GIO, and FIO, introduced in Sec. II.A.2. In place of the first condition, we give the corresponding literature reference, where suitable motivations can be found for each set. As the table shows, several frameworks of coherence do not fulfill all of our criteria, and several entries still remain open.

We further reviewed in Sec. III the current progress on quantifying coherence and related manifestations of non-classicality in compliance with the underlying framework of resource theories, in particular, highlighting interconnections between different measures and, where possible, their relations to entanglement measures. Several open questions remain to be addressed in these topics as we pointed out throughout the text. The rest of the Colloquium (Secs. IV and V) was dedicated to investigating more physical aspects of coherence in quantum systems and their applications to quantum technologies, many-body physics, biological transport, and thermodynamics. Most of these advances are still at a very early stage, and the operational value of coherence still needs to be pinpointed clearly in many contexts.

We expect that substantial future research will focus on various aspects of coherence in physics, information theory, biology, and other branches of science and engineering. To highlight the ultimate role of quantum coherence as a resource in these and related research fields, we need to reveal new phenomena which can be explained in quantitative terms by the presence of coherence, but cannot be traced back to entanglement, or any other kind of nonclassical resource. We hope that this Colloquium will pave the way toward further breakthroughs in this exciting research direction.

# ACKNOWLEDGMENTS

We thank Tillmann Baumgratz, Manabendra Nath Bera, Paul Boes, Thomas Bromley, Dagmar Bruß, Kaifeng Bu, Eric Chitambar, Marco Cianciaruso, Marcus Cramer, Animesh Datta, Maria García-Díaz, Dario Egloff, Jens Eisert, Heng Fan, Irénée Frérot, Paolo Giorda, Davide Girolami, Gilad Gour, Michal Horodecki, Pawe Horodecki, Susana Huelga,

Hermann Kampermann, Nathan Killoran, Maciej Lewenstein, Iman Marvian, Maurizio Matera, Marco Piani, Swapan Rana, Alexey Rastegin, Bartosz Regula, Tommaso Roscilde, Isabela Almeida Silva, Paolo Solinas, Robert Spekkens, Thomas Theurer, Werner Vogel, Henrik Wilming, Andreas Winter, Dong Yang, Lin Zhang, and Karol Žyczkowski for discussions and feedback on the manuscript. We acknowledge financial support from the European Research Council (StG GQCOP Grant No. 637352 and SyG BioQ Grant No. 319130), the European Commission projects PAPETS and QUCHIP, the Foundational Questions Institute (Grant No. FQXi-RFP-1601), the National Science Center in Poland (POLONEZ UMO2016/21/P/ST2/04054), the Alexander von Humboldt-Foundation, the MINECO (SEVERO OCHOA Grant No. SEV-2015-0522, FISICATEAMO FIS2016-79508-P), the Generalitat de Catalunya (SGR 874 and CERCA Program), and Fundació Privada Cellex. This publication was made possible through the support of a grant from the John Templeton Foundation.

# REFERENCES

Abah,O.,and E.Lutz,2014,Europhys.Lett.106,20001.  
Aberg, J., 2006, arXiv:quant-ph/0612146.  
Aberg, J., 2014, Phys. Rev. Lett. 113, 150402.  
Addis, C., G. Brebner, P. Haikka, and S. Maniscalco, 2014, Phys. Rev. A 89, 024101.  
Adesso, G., T. R. Bromley, and M. Cianciaruso, 2016, J. Phys. A 49, 473001.  
Adesso, G., and F. Illuminati, 2007, J. Phys. A 40, 7821.  
Anand, N., and A. K. Pati, 2016, arXiv:1611.04542.  
Arrad, G., Y. Vinkler, D. Aharonov, and A. Retzker, 2014, Phys. Rev. Lett. 112, 150801.  
Asbóth, J. K., J. Calsamiglia, and H. Ritsch, 2005, Phys. Rev. Lett. 94, 173602.  
Bagan, E., J. A. Bergou, S. S. Cottrell, and M. Hillary, 2016, Phys. Rev. Lett. 116, 160406.  
Bai, Z., and S. Du, 2015, Quantum Inf. Comput. 15, 1355.  
Bartlett, S. D., T. Rudolph, and R. W. Spekkens, 2007, Rev. Mod. Phys. 79, 555.  
Baumgratz, T., M. Cramer, and M. B. Plenio, 2014, Phys. Rev. Lett. 113, 140401.  
Ben Dana, K., M. García Díaz, M. Mejatty, and A. Winter, 2017, arXiv:1704.03710.  
Bennett, C. H., D. P. DiVincenzo, C. A. Fuchs, T. Mor, E. Rains, P. W. Shor, J. A. Smolin, and W. K. Wootters, 1999, Phys. Rev. A 59, 1070.  
Bennett, C. H., D. P. DiVincenzo, J. A. Smolin, and W. K. Wootters, 1996, Phys. Rev. A 54, 3824.  
Bera, M. N., T. Qureshi, M. A. Siddiqui, and A. K. Pati, 2015, Phys. Rev. A 92, 012118.  
Bhattacharya, S., S. Banerjee, and A. K. Pati, 2016, arXiv: 1601.04742.  
Biswas, T., M. García-Díaz, and A. Winter, 2017, arXiv:1701.05051.  
Brandão, F. G. S. L., and G. Gour, 2015, Phys. Rev. Lett. 115, 070503.  
Brandão, F. G. S. L., M. Horodecki, N. H. Y. Ng, J. Oppenheim, and S. Wehner, 2015, Proc. Natl. Acad. Sci. U.S.A. 112, 3275.  
Brandão, F. G. S. L., M. Horodecki, J. Oppenheim, J. M. Renes, and R. W. Spekkens, 2013, Phys. Rev. Lett. 111, 250404.

Brandão, F.G.S.L., M. Piani, and P. Horodecki, 2015, Nat. Commun. 6, 7908.  
Brandao, F. G. S. L., and M. B. Plenio, 2008, Nat. Phys. 4, 873.  
Brandão, F. G. S. L., and M. B. Plenio, 2010, Commun. Math. Phys. 295, 829.  
Braun, D., G. Adesso, F. Benatti, R. Floreanini, U. Marzolino, M. W. Mitchell, and S. Pirandola, 2017, arXiv:1701.05152.  
Braun, D., and B. Georgeot, 2006, Phys. Rev. A 73, 022314.  
Braunstein, S. L., and C. M. Caves, 1994, Phys. Rev. Lett. 72, 3439.  
Braunstein, S. L., C. M. Caves, and G. Milburn, 1996, Ann. Phys. (N.Y.) 247, 135.  
Braunstein, S. L., and P. van Loock, 2005, Rev. Mod. Phys. 77, 513.  
Breuer, H., and F. Petruccione, 2002, The Theory of Open Quantum Systems (Oxford University Press, New York).  
Breuer, H.-P., E.-M. Laine, J. Piilo, and B. Vacchini, 2016, Rev. Mod. Phys. 88, 021002.  
Bromley, T. R., M. Cianciaruso, and G. Adesso, 2015, Phys. Rev. Lett. 114, 210401.  
Bu, K., A. Kumar, L. Zhang, and J. Wu, 2017, Phys. Lett. A 381, 1670.  
Bu, K., U. Singh, and J. Wu, 2016, Phys. Rev. A 93, 042326.  
Bu, K., and J. Wu, 2016, arXiv:1603.06322.  
Bu, K., and C. Xiong, 2016, arXiv:1604.06524.  
Buono, D., G. Nocerino, G. Petrillo, G. Torre, G. Zonzo, and F. Illuminati, 2016, arXiv:1609.00913.  
Cai, J., G. G. Guerreschi, and H. J. Briegel, 2010, Phys. Rev. Lett. 104, 220502.  
Cakmak, B., G. Karpat, and F.F. Fanchini, 2015, Entropy 17, 790.  
Caruso, F., A. W. Chin, A. Datta, S. F. Huelga, and M. B. Plenio, 2009, J. Chem. Phys. 131, 105106.  
Caruso, F., A. W. Chin, A. Datta, S. F. Huelga, and M. B. Plenio, 2010, Phys. Rev. A 81, 062346.  
Chanda, T., and S. Bhattacharya, 2016, Ann. Phys. (Amsterdam) 366, 1.  
Chaves, R., J. B. Brask, M. Markiewicz, J. Kołodyński, and A. Acín, 2013, Phys. Rev. Lett. 111, 120401.  
Chen, J., S. Grogan, N. Johnston, C.-K. Li, and S. Plosker, 2016, Phys. Rev. A 94, 042313.  
Chen, J.-J., J. Cui, Y.-R. Zhang, and H. Fan, 2016, Phys. Rev. A 94, 022112.  
Cheng, S., and M. J. W. Hall, 2015, Phys. Rev. A 92, 042101.  
Chin, A. W., A. Datta, F. Caruso, S. F. Huelga, and M. B. Plenio, 2010, New J. Phys. 12, 065002.  
Chin, A. W., S. F. Huelga, and M. B. Plenio, 2012, Phys. Rev. Lett. 109, 233601.  
Chin, A. W., J. Prior, R. Rosenbach, F. Caycedo-Soler, S. F. Huelga, and M. B. Plenio, 2013, Nat. Phys. 9, 113.  
Chiribella, G., and Y. Yang, 2015, arXiv:1502.00259.  
Chitambar, E., and G. Gour, 2016a, Phys. Rev. A 94, 052336.  
Chitambar, E., and G. Gour, 2016b, Phys. Rev. Lett. 117, 030401.  
Chitambar, E., and G. Gour, 2017, Phys. Rev. A 95, 019902.  
Chitambar, E., and M.-H. Hsieh, 2016, Phys. Rev. Lett. 117, 020402.  
Chitambar, E., A. Streltsov, S. Rana, M. N. Bera, G. Adesso, and M. Lewenstein, 2016, Phys. Rev. Lett. 116, 070402.  
Christensson, N., H. F. Kauffmann, T. Pullerits, and T. Mancal, 2012, J. Phys. Chem. B 116, 7449.  
Cianciaruso, M., T.R. Bromley, W. Roga, R. Lo Franco, and G. Adesso, 2015, Sci. Rep. 5, 10177.  
Coecke, B., T. Fritz, and R. W. Spekkens, 2016, Inf. Comput. 250, 59.  
Coffman, V., J. Kundu, and W. K. Wootters, 2000, Phys. Rev. A 61, 052306.

Collini, E., C. Y. Wong, K. E. Wilk, P. M. G. Curmi, P. Brumer, and G. D. Scholes, 2010, Nature (London) 463, 644.  
Correa, L. A., J. P. Palao, D. Alonso, and G. Adesso, 2014, Sci. Rep. 4, 3949.  
Cwiklinski, P., M. Studziński, M. Horodecki, and J. Oppenheim, 2015, Phys. Rev. Lett. 115, 210403.  
Dakić, B., V. Vedral, and C. Brukner, 2010, Phys. Rev. Lett. 105, 190502.  
Datta, A., S. T. Flammia, and C. M. Caves, 2005, Phys. Rev. A 72, 042316.  
Datta, A., and A. Shaji, 2011, Int. J. Quantum. Inform. 09, 1787.  
Datta, A., A. Shaji, and C. M. Caves, 2008, Phys. Rev. Lett. 100, 050502.  
del Campo, A., I. L. Egusquiza, M. B. Plenio, and S. F. Huelga, 2013, Phys. Rev. Lett. 110, 050403.  
del Rio, L., L. Kraemer, and R. Renner, 2015, arXiv:1511.08818.  
Demkowicz-Dobrzański, R., J. Kolodynski, and M. Guta, 2012, Nat. Commun. 3, 1063.  
Demkowicz-Dobrzański, R., and L. Maccone, 2014, Phys. Rev. Lett. 113, 250801.  
Deutsch, D., and R. Jozsa, 1992, Proc. R. Soc. A 439, 553.  
Deveaud-Plédran, B., A. Quattropani, and P. Schwendimann, 2009, Quantum Coherence in Solid State Systems, International School of Physics Enrico Fermi (IOS Press, Amsterdam).  
de Vicente, J. I., and A. Streltsov, 2017, J. Phys. A 50, 045301.  
DiVincenzo, D., C. Fuchs, H. Mabuchi, J. Smolin, A. Thapliyal, and A. Uhlmann, 1999, in Quantum Computing and Quantum Communications, Lecture Notes in Computer Science, Vol. 1509 (Springer, Berlin/Heidelberg), pp. 247-257.  
Du, S., and Z. Bai, 2015, Ann. Phys. (Amsterdam) 359, 136.  
Du, S., Z. Bai, and Y. Guo, 2015, Phys. Rev. A 91, 052120.  
Du, S., Z. Bai, and Y. Guo, 2017, Phys. Rev. A 95, 029901.  
Dür, W., M. Skotiniotis, F. Frowis, and B. Kraus, 2014, Phys. Rev. Lett. 112, 080801.  
Egloff, D., O. Dahlsten, R. Renner, and V. Vedral, 2015, New J. Phys. 17, 073001.  
Eisert, J., K. Jacobs, P. Papadopoulos, and M. B. Plenio, 2000, Phys. Rev. A 62, 052317.  
Eisert, J., C. Simon, and M. B. Plenio, 2002, J. Phys. A 35, 3911.  
Engel, G. S., T. R. Calhoun, E. L. Read, T.-K. Ahn, T. Mancal, Y.-C. Cheng, R. E. Blakenship, and G. R. Fleming, 2007, Nature (London) 446, 782.  
Escher, B. M., R. L. de Matos Filho, and L. Davidovich, 2011, Nat. Phys. 7, 406.  
Faist, P., J. Oppenheim, and R. Renner, 2015, New J. Phys. 17, 043003.  
Farace, A., A. De Pasquale, L. Rigovacca, and V. Giovannetti, 2014, New J. Phys. 16, 073010.  
Fassioli, F., and A. Olaya-Castro, 2010, New J. Phys. 12, 085006.  
Frérot, I., and T. Roscilde, 2016, Phys. Rev. B 94, 075121.  
García-Díaz, M., D. Egloff, and M. B. Plenio, 2016, Quantum Inf. Comput. 16, 1282.  
Gauger, E. M., E. Rieper, J. J. L. Morton, S. C. Benjamin, and V. Vedral, 2011, Phys. Rev. Lett. 106, 040503.  
Giorda, P., and M. Allegra, 2016a, arXiv:1606.02197.  
Giorda, P., and M. Allegra, 2016b, arXiv:1611.02519.  
Giovannetti, V., S. Lloyd, and L. Maccone, 2004, Science 306, 1330.  
Giovannetti, V., S. Lloyd, and L. Maccone, 2006, Phys. Rev. Lett. 96, 010401.  
Giovannetti, V., S. Lloyd, and L. Maccone, 2011, Nat. Photonics 5, 222.  
Girolami, D., 2014, Phys. Rev. Lett. 113, 170401.

Girolami, D., T. Tufarelli, and G. Adesso, 2013, Phys. Rev. Lett. 110, 240402.  
Girolami, D., and B. Yadin, 2017, Entropy 19, 124.  
Glauber, R. J., 1963, Phys. Rev. 130, 2529.  
Goold, J., M. Huber, A. Riera, L. del Rio, and P. Skrzypczyk, 2016, J. Phys. A 49, 143001.  
Gour, G., I. Marvian, and R. W. Spekkens, 2009, Phys. Rev. A 80, 012307.  
Gour, G., M. P. Müller, V. Narasimhachar, R. W. Spekkens, and N. Y. Halpern, 2015, Phys. Rep. 583, 1.  
Gour, G., and R. W. Spekkens, 2006, Phys. Rev. A 73, 062331.  
Gour, G., and R. W. Spekkens, 2008, New J. Phys. 10, 033023.  
Grover, L. K., 1997, Phys. Rev. Lett. 79, 325.  
Hayden, P. M., M. Horodecki, and B. M. Terhal, 2001, J. Phys. A 34, 6891.  
Henderson, L., and V. Vedral, 2001, J. Phys. A 34, 6899.  
Herbut, F., 2005, J. Phys. A 38, 2959.  
Hillery, M., 2016, Phys. Rev. A 93, 012111.  
Horodecki, M., P. Horodecki, and R. Horodecki, 1998, Phys. Rev. Lett. 80, 5239.  
Horodecki, M., and J. Oppenheim, 2013a, Nat. Commun. 4, 2059.  
Horodecki, M., and J. Oppenheim, 2013b, Int. J. Mod. Phys. B 27, 1345019.  
Horodecki, M., J. Oppenheim, and A. Winter, 2005, Nature (London) 436, 673.  
Horodecki, M., J. Oppenheim, and A. Winter, 2007, Commun. Math. Phys. 269, 107.  
Horodecki, R., M. Horodecki, and J. Oppenheim, 2003, Phys. Rev. A 67, 062104.  
Horodecki, R., P. Horodecki, M. Horodecki, and K. Horodecki, 2009, Rev. Mod. Phys. 81, 865.  
Hu, M.-L., and H. Fan, 2016, Sci. Rep. 6, 29260.  
Hu, X., 2016, Phys. Rev. A 94, 012326.  
Hu, X., and H. Fan, 2016, Sci. Rep. 6, 34380.  
Hu, X., A. Milne, B. Zhang, and H. Fan, 2016, Sci. Rep. 6, 19365.  
Huelga, S.F., C. Macchiavello, T. Pellizzari, A.K. Ekert, M.B. Plenio, and J.I. Cirac, 1997, Phys. Rev. Lett. 79, 3865.  
Huelga, S.F., and M.B. Plenio, 2013, Contemp. Phys. 54, 181.  
Hyllus, P., W. Laskowski, R. Krischek, C. Schwemmer, W. Wieczorek, H. Weinfurter, L. Pezzé, and A. Smerzi, 2012, Phys. Rev. A 85, 022321.  
Janzing, D., P. Wocjan, R. Zeier, R. Geiss, and T. Beth, 2000, Int. J. Theor. Phys. 39, 2717.  
Jonathan, D., and M. B. Plenio, 1999, Phys. Rev. Lett. 83, 3566.  
Kammerlander, P., and J. Anders, 2016, Sci. Rep. 6, 22174.  
Karpat, G., B. Cakmak, and F. F. Fanchini, 2014, Phys. Rev. B 90, 104431.  
Kessler, E. M., I. Lovchinsky, A. O. Sushkov, and M. D. Lukin, 2014, Phys. Rev. Lett. 112, 150802.  
Killoran, N., F. E. S. Steinhoff, and M. B. Plenio, 2016, Phys. Rev. Lett. 116, 080402.  
Kim, M. S., W. Son, V. Bužek, and P. L. Knight, 2002, Phys. Rev. A 65, 032323.  
Knill, E., and R. Laflamme, 1998, Phys. Rev. Lett. 81, 5672.  
Kolli, A., E. J. O Reilly, G. D. Scholes, and A. Olaya-Castro, 2012, J. Chem. Phys. 137, 174109.  
Kominis,I.K.,2015,Mod.Phys.Lett.B29,1530013.  
Korzekwa, K., M. Lostaglio, J. Oppenheim, and D. Jennings, 2016, New J. Phys. 18, 023045.  
Kumar, A., 2017, Phys. Lett. A 381, 991.  
Levi, F., and F. Mintert, 2014, New J. Phys. 16, 033007.  
Lewenstein, M., and A. Sanpera, 1998, Phys. Rev. Lett. 80, 2261.

Li, C.-M., N. Lambert, Y.-N. Chen, G.-Y. Chen, and F. Nori, 2012, Sci. Rep. 2, 885.  
Li, Y.-C., and H.-Q. Lin, 2016, Sci. Rep. 6, 26365.  
Lidar, D., 2014, Adv. Chem. Phys. 154, 295.  
Linden, N., J. A. Smolin, and A. Winter, 2009, Phys. Rev. Lett. 103, 030501.  
Liu, X., Z. Tian, J. Wang, and J. Jing, 2016, Ann. Phys. (Amsterdam) 366, 102.  
Liu, Z.-W., X. Hu, and S. Lloyd, 2017, Phys. Rev. Lett. 118, 060502.  
Lostaglio, M., D. Jennings, and T. Rudolph, 2015, Nat. Commun. 6, 6383.  
Lostaglio, M., D. Jennings, and T. Rudolph, 2017, New J. Phys. 19, 043008.  
Lostaglio, M., K. Korzekwa, D. Jennings, and T. Rudolph, 2015, Phys. Rev. X 5, 021001.  
Louisell, W., 1973, Quantum Statistical Properties of Radiation (J. Wiley, New York).  
Ma, J., B. Yadin, D. Girolami, V. Vedral, and M. Gu, 2016, Phys. Rev. Lett. 116, 160407.  
Macchiavello, C., S. F. Huelga, J. I. Cirac, A. K. Ekert, and M. B. Plenio, 2002, "Decoherence and quantum error correction in frequency standards," in Quantum Communication, Computing, and Measurement 2, edited by P. Kumar, G. M. D'Ariano, and O. Hirota (Springer US, Boston, MA), pp. 337-345.  
Malvezzi, A. L., G. Karpat, B. Çakmak, F. F. Fanchini, T. Debarba, and R. O. Vianna, 2016, Phys. Rev. B 93, 184428.  
Mandel, L., and E. Wolf, 1965, Rev. Mod. Phys. 37, 231.  
Mandelstam, L., and I. Tamm, 1945, J. Phys. USSR 9, 249.  
Mani, A., and V. Karimipour, 2015, Phys. Rev. A 92, 032331.  
Manzano, G., F. Galve, R. Zambrini, and J. M. R. Parrondo, 2016, Phys. Rev. E 93, 052120.  
Margolus, N., and L. B. Levitin, 1998, Physica D (Amsterdam) 120, 188.  
Marvian, I., 2012, Symmetry, Asymmetry and Quantum Information, Ph.D. thesis (University of Waterloo).  
Marvian, I., and S. Lloyd, 2016, arXiv:1608.07325.  
Marvian, I., and R. W. Spekkens, 2013, New J. Phys. 15, 033001.  
Marvian, I., and R. W. Spekkens, 2014a, Nat. Commun. 5, 3821.  
Marvian, I., and R. W. Spekkens, 2014b, Phys. Rev. A 90, 062110.  
Marvian, I., and R. W. Spekkens, 2016, Phys. Rev. A 94, 052324.  
Marvian, I., R. W. Spekkens, and P. Zanardi, 2016, Phys. Rev. A 93, 052331.  
Matera, J.M., D. Egloff, N. Killoran, and M.B. Plenio, 2016, Quantum Sci. Technol. 1, 01LT01.  
Mazzola, L., J. Piilo, and S. Maniscalco, 2010, Phys. Rev. Lett. 104, 200401.  
Miatto, F. M., K. Piche, T. Brougham, and R. W. Boyd, 2015, Phys. Rev. A 92, 062331.  
Misra, A., U. Singh, S. Bhattacharya, and A. K. Pati, 2016, Phys. Rev. A 93, 052335.  
Mitchison, M. T., M. P. Woods, J. Prior, and M. Huber, 2015, New J. Phys. 17, 115013.  
Modi, K., A. Brodutch, H. Cable, T. Paterek, and V. Vedral, 2012, Rev. Mod. Phys. 84, 1655.  
Modi, K., T. Paterek, W. Son, V. Vedral, and M. Williamson, 2010, Phys. Rev. Lett. 104, 080501.  
Mohseni, M., P. Rebentrost, S. Lloyd, and A. Aspuru-Guzik, 2008, J. Chem. Phys. 129, 174106.  
Mondal, D., C. Datta, and S. Sazim, 2016, Phys. Lett. A 380, 689.  
Mondal, D., and C. Mukhopadhyay, 2015, arXiv:1510.07556.  
Mondal, D., T. Pramanik, and A. K. Pati, 2017, Phys. Rev. A 95, 010301.  
Morozova, E. A., and N. N. Čencov, 1991, J. Sov. Math. 56, 2648.

Mukhopadhyay, C., S. Das, S. Bhattacharya, A. Sen De, and U. Sen, 2017, arXiv:1705.04343.  
Napoli, C., T. R. Bromley, M. Cianciaruso, M. Piani, N. Johnston, and G. Adesso, 2016, Phys. Rev. Lett. 116, 150502.  
Narasimhachar, V., and G. Gour, 2015, Nat. Commun. 6, 7689.  
Nichols, R., T. R. Bromley, L. A. Correa, and G. Adesso, 2016, Phys. Rev. A 94, 042101.  
Niedenzu, W., D. Gelbwaser-Klimovsky, A.G. Kofman, and G. Kurizki, 2016, New J. Phys. 18, 083012.  
Nielsen, M. A., 1999, Phys. Rev. Lett. 83, 436.  
Nielsen, M. A., and I. L. Chuang, 2010, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, England).  
Ollivier, H., and W. H. Zurek, 2001, Phys. Rev. Lett. 88, 017901.  
Oppenheim, J., M. Horodecki, P. Horodecki, and R. Horodecki, 2002, Phys. Rev. Lett. 89, 180402.  
O'Reilly, E.J., and A. Olaya-Castro, 2014, Nat. Commun. 5, 3012.  
Oszmaniec, M., A. Grudka, M. Horodecki, and A. Wojcik, 2016, Phys. Rev. Lett. 116, 110403.  
Paris, M. G. A., 2009, Int. J. Quantum. Inform. 07, 125.  
Parker, S., and M. B. Plenio, 2000, Phys. Rev. Lett. 85, 3049.  
Parker, S., and M. B. Plenio, 2002, J. Mod. Opt. 49, 1325.  
Peng, Y., Y. Jiang, and H. Fan, 2016, Phys. Rev. A 93, 032326.  
Peng, Y., Y.-R. Zhang, Z.-Y. Fan, S. Liu, and H. Fan, 2016, arXiv:1608.07950.  
Peres, A., and P.F. Scudo, 2002, arXiv:quant-ph/0201017.  
Petz, D., 1996, Linear Algebra Appl. 244, 81.  
Petz, D., and C. Ghinea, 2011, Quantum Probab. White Noise Anal. 27, 261.  
Pezzé, L., and A. Smerzi, 2009, Phys. Rev. Lett. 102, 100401.  
Pezze, L., and A. Smerzi, 2014, "Atom Interferometry," in Proceedings of the International School of Physics "Enrico Fermi," Course 188, Varenna, edited by G.M. Tino and M.A. Kasevich (IOS Press, Amsterdam), p. 691.  
Piani, M., M. Cianciaruso, T. R. Bromley, C. Napoli, N. Johnston, and G. Adesso, 2016, Phys. Rev. A 93, 042107.  
Piani, M., S. Gharibian, G. Adesso, J. Calsamiglia, P. Horodecki, and A. Winter, 2011, Phys. Rev. Lett. 106, 220403.  
Piani, M., P. Horodecki, and R. Horodecki, 2008, Phys. Rev. Lett. 100, 090502.  
Pires, D. P., L. C. Céleri, and D. O. Soares-Pinto, 2015, Phys. Rev. A 91, 042330.  
Pires, D.P., M. Cianciaruso, L.C. Celeri, G. Adesso, and D.O. Soares-Pinto, 2016, Phys. Rev. X 6, 021031.  
Plenio, M. B., and S. F. Huelga, 2008, New J. Phys. 10, 113019.  
Plenio, M. B., and S. Virmani, 2007, Quantum Inf. Comput. 7, 1.  
Pozzobom, M. B., and J. Maziero, 2017, Ann. Phys. (Amsterdam) 377, 243.  
Preskill, J., 2000, arXiv:quant-ph/0010098.  
Prior, J., A. W. Chin, S. F. Huelga, and M. B. Plenio, 2010, Phys. Rev. Lett. 105, 050404.  
Puchala, Z., L. Pawela, and K. Žyczkowski, 2016, Phys. Rev. A 93, 062112.  
Qi, X., T. Gao, and F. Yan, 2016, arXiv:1610.07052.  
Rabitz, H., R. de Vivie-Riedle, M. Motzkus, and K. Kompa, 2000, Science 288, 824.  
Radhakrishnan, C., M. Parthasarathy, S. Jambulingam, and T. Byrnes, 2016, Phys. Rev. Lett. 116, 150504.  
Rahav, S., U. Harbola, and S. Mukamel, 2012, Phys. Rev. A 86, 043843.  
Rains, E. M., 2001, IEEE Trans. Inf. Theory 47, 2921.

Rana, S., P. Parashar, and M. Lewenstein, 2016, Phys. Rev. A 93, 012110.  
Rastegin, A. E., 2016, Phys. Rev. A 93, 032136.  
Rebentrost, P., M. Mohseni, and A. Aspuru-Guzik, 2009, J. Phys. Chem. B 113, 9942.  
Rebentrost, P., M. Mohseni, I. Kassal, S. Lloyd, and A. Aspuru-Guzik, 2009, New J. Phys. 11, 033003.  
Regula, B., M. Piani, M. Cianciaruso, T. R. Bromley, A. Streltsov, and G. Adesso, 2017, arXiv:1704.04153.  
Ritz, T., S. Adem, and K. Schulten, 2000, Biophys. J. 78, 707.  
Rivas, A., S. F. Huelga, and M. B. Plenio, 2014, Rep. Prog. Phys. 77, 094001.  
Roden, J. J., D. I. Bennett, and K. B. Whaley, 2016, J. Chem. Phys. 144, 245101.  
Roden, J. J., and K. B. Whaley, 2016, Phys. Rev. E 93, 012128.  
Rodriguez-Rosario, C.A., T. Frauenheim, and A. Aspuru-Guzik, 2013, arXiv:1308.1245v1.  
Roga, W., D. Spehner, and F. Illuminati, 2016, J. Phys. A 49, 235301.  
Roßnagel, J., O. Abah, F. Schmidt-Kaler, K. Singer, and E. Lutz, 2014, Phys. Rev. Lett. 112, 030602.  
Ruch, E., 1975, Theor. Chim. Acta 38, 167.  
Ruch, E., and A. Mead, 1976, Theor. Chim. Acta 41, 95.  
Ruch, E., R. Schranner, and T. H. Seligman, 1978, J. Chem. Phys. 69, 386.  
Sarovar, M., A. Ishizaki, G. R. Fleming, and K. B. Whaley, 2010, Nat. Phys. 6, 462.  
Schlosshauer, M., 2005, Rev. Mod. Phys. 76, 1267.  
Scully, M. O., K. R. Chapin, K. E. Dorfman, M. B. Kim, and A. Svidzinsky, 2011, Proc. Natl. Acad. Sci. U.S.A. 108, 15097.  
Sekatski, P., M. Skotiniotis, J. Kołodyński, and W. Dur, 2016, arXiv:1603.08944.  
Shao, L.-H., Z. Xi, H. Fan, and Y. Li, 2015, Phys. Rev. A 91, 042120.  
Shi, H.-L., S.-Y. Liu, X.-H. Wang, W.-L. Yang, Z.-Y. Yang, and H. Fan, 2017, Phys. Rev. A 95, 032307.  
Shor, P. W., 1995, Phys. Rev. A 52, R2493.  
Silva,I.A.,et al.,2016,Phys.Rev.Lett.117,160402.  
Singh, U., M. N. Bera, H. S. Dhar, and A. K. Pati, 2015, Phys. Rev. A 91, 052115.  
Singh, U., M. N. Bera, A. Misra, and A. K. Pati, 2015, arXiv: 1506.08186.  
Singh, U., A. K. Pati, and M. N. Bera, 2016, Mathematics 4, 47.  
Singh, U., L. Zhang, and A. K. Pati, 2016, Phys. Rev. A 93, 032125.  
Situ, H., and X. Hu, 2016, Quantum Inf. Process. 15, 4649.  
Skrzypczyk, P., A. J. Short, and S. Popescu, 2014, Nat. Commun. 5, 4185.  
Smirne, A., J. Kołodyński, S.F. Huelga, and R. Demkowicz-Dobrzański, 2016, Phys. Rev. Lett. 116, 120801.  
Solinas, P., and S. Gasparinetti, 2015, Phys. Rev. E 92, 042150.  
Solinas, P., and S. Gasparinetti, 2016, Phys. Rev. A 94, 052103.  
Sperling, J., and W. Vogel, 2015, Phys. Scr. 90, 074024.  
Steiner, M., 2003, Phys. Rev. A 67, 054305.  
Streltsov, A., 2015, Quantum Correlations Beyond Entanglement and their Role in Quantum Information Theory, SpringerBriefs in Physics (Springer, New York).  
Streltsov, A., E. Chitambar, S. Rana, M. N. Bera, A. Winter, and M. Lewenstein, 2016, Phys. Rev. Lett. 116, 240405.  
Streltsov, A., H. Kampermann, and D. Bruß, 2010, New J. Phys. 12, 123004.  
Streltsov, A., H. Kampermann, S. Wölk, M. Gessner, and D. Bruß, 2016, arXiv:1612.07570.  
Streltsov, A., S. Rana, M. N. Bera, and M. Lewenstein, 2017, Phys. Rev. X 7, 011024.

Streltsov, A., S. Rana, P. Boes, and J. Eisert, 2017, arXiv: 1705.04189.  
Streltsov, A., U. Singh, H. S. Dhar, M. N. Bera, and G. Adesso, 2015, Phys. Rev. Lett. 115, 020403.  
Sudarshan, E. C. G., 1963, Phys. Rev. Lett. 10, 277.  
Taddei, M. M., B. M. Escher, L. Davidovich, and R. L. de Matos Filho, 2013, Phys. Rev. Lett. 110, 050402.  
Tan, K.C., T. Volkoff, H. Kwon, and H. Jeong, 2017, arXiv: 1703.01067.  
Theurer, T., N. Killoran, D. Egloff, and M. B. Plenio, 2017, arXiv: 1703.10943.  
Toth, G., 2012, Phys. Rev. A 85, 022322.  
Toth, G., and I. Apellaniz, 2014, J. Phys. A 47, 424006.  
Turin,L.,1996,Chem.Senses21,773.  
Uhlmann, A., 1998, Open Syst. Inf. Dyn. 5, 209.  
Unden, T., et al., 2016, Phys. Rev. Lett. 116, 230502.  
Uzdin, R., A. Levy, and R. Kosloff, 2015, Phys. Rev. X 5, 031044.  
Vacanti, G., C. Elouard, and A. Auffeves, 2015, arXiv:1503.01974.  
Vaccaro, J. A., F. Anselmi, H. M. Wiseman, and K. Jacobs, 2008, Phys. Rev. A 77, 032114.  
van Dam, W., and P. Hayden, 2003, Phys. Rev. A 67, 060302(R).  
Vatasescu, M., 2015, Phys. Rev. A 92, 042323.  
Vatasescu, M., 2016, Phys. Rev. A 93, 069906.  
Vedral, V., and M. B. Plenio, 1998, Phys. Rev. A 57, 1619.  
Vedral, V., M. B. Plenio, M. A. Rippin, and P. L. Knight, 1997, Phys. Rev. Lett. 78, 2275.  
Vidal, G., and R. Tarrach, 1999, Phys. Rev. A 59, 141.  
Viola, L., E. Knill, and S. Lloyd, 1999, Phys. Rev. Lett. 82, 2417.  
Vogel, W., and J. Sperling, 2014, Phys. Rev. A 89, 052302.  
von Prillwitz, K., L. Rudnicki, and F. Mintert, 2015, Phys. Rev. A 92, 052114.  
Wang, Y.-T., J.-S. Tang, Z.-Y. Wei, S. Yu, Z.-J. Ke, X.-Y. Xu, C.-F. Li, and G.-C. Guo, 2017, Phys. Rev. Lett. 118, 020403.  
Weedbrook, C., S. Pirandola, R. García-Patrón, N.J. Cerf, T.C. Ralph, J.H. Shapiro, and S. Lloyd, 2012, Rev. Mod. Phys. 84, 621.  
Wehrl,A.,1978,Rev.Mod.Phys.50,221.  
Wei, T.-C., and P. M. Goldbart, 2003, Phys. Rev. A 68, 042307.  
Wigner, E. P., and M. M. Yanase, 1963, Proc. Natl. Acad. Sci. U.S.A. 49, 910.  
Wilde, M. M., J. M. McCracken, and A. Mizel, 2009, Proc. R. Soc. A 466, 1347.  
Winter, A., and D. Yang, 2016, Phys. Rev. Lett. 116, 120404.  
Wolf, M. M., J. Eisert, and M. B. Plenio, 2003, Phys. Rev. Lett. 90, 047904.  
Womick, J. M., B. A. West, N. F. Scherer, and A. M. Moran, 2012, J. Phys. B 45, 154016.  
Woods, M. P., R. Silva, and J. Oppenheim, 2016, arXiv:1607.04591.  
Wootters, W. K., 1998, Phys. Rev. Lett. 80, 2245.  
Wu, K.-D., Z. Hou, H.-S. Zhong, Y. Yuan, G.-Y. Xiang, C.-F. Li, and G.-C. Guo, 2017, arXiv:1702.06606.  
Xi, Z., M. Hu, Y. Li, and H. Fan, 2015, arXiv:1510.06473.  
Xi, Z., Y. Li, and H. Fan, 2015, Sci. Rep. 5, 10922.  
Xu, J., 2016, Phys. Rev. A 93, 032111.  
Yadin, B., J. Ma, D. Girolami, M. Gu, and V. Vedral, 2016, Phys. Rev. X 6, 041028.  
Yadin, B., and V. Vedral, 2016, Phys. Rev. A 93, 022122.  
Yao, Y., X. Xiao, L. Ge, and C. P. Sun, 2015, Phys. Rev. A 92, 022112.  
Yu, X.-D., D.-J. Zhang, C.L. Liu, and D.M. Tong, 2016, Phys. Rev. A 93, 060303.

Yu, X.-D., D.-J. Zhang, G. F. Xu, and D. M. Tong, 2016, Phys. Rev. A 94, 060302.  
Yuan, X., H. Zhou, Z. Cao, and X. Ma, 2015, Phys. Rev. A 92, 022124.  
Zanardi, P., G. Styliaris, and L. Campos Venuti, 2017a, Phys. Rev. A 95, 052306.  
Zanardi, P., G. Styliaris, and L. Campos Venuti, 2017b, Phys. Rev. A 95, 052307.  
Zanardi, P., C. Zalka, and L. Faoro, 2000, Phys. Rev. A 62, 030301.  
Zhang, C., et al., 2016, arXiv:1611.02004.  
Zhang, H.-J., B. Chen, M. Li, S.-M. Fei, and G.-L. Long, 2017, Commun. Theor. Phys. 67, 166.

Zhang, L., 2017, J. Phys. A 50, 155303.  
Zhang, L., U. Singh, and A. K. Pati, 2017, Ann. Phys. (Amsterdam) 377, 125.  
Zhang, Y.-J., W. Han, Y.-J. Xia, Y.-M. Yu, and H. Fan, 2015, Sci. Rep. 5, 13359.  
Zhang, Y.-R., L.-H. Shao, Y. Li, and H. Fan, 2016, Phys. Rev. A 93, 012334.  
Zhu, H., Z. Ma, Z. Cao, S.-M. Fei, and V. Vedral, 2017, arXiv: 1704.01935.  
Zurek,W.H.,2000,Ann.Phys.(Berlin)9,855.  
Zurek,W.H.,2003,Rev.Mod.Phys.75,715.  
Zurek,W.H.,2009,Nat.Phys.5,181.