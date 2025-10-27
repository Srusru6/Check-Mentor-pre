# QUANTUM MECHANICS AS QUANTUM MEASURE THEORY

RAFAEL D. SORKIN

Department of Physics, Syracuse University, Syracuse, NY 13244-1130, USA

Received 21 September 1994

The additivity of classical probabilities is only the first in a hierarchy of possible sum rules, each of which implies its successor. The first and most restrictive sum rule of the hierarchy yields measure theory in the Kolmogorov sense, which is appropriate physically for the description of stochastic processes such as Brownian motion. The next weaker sum rule defines a generalized measure theory which includes quantum mechanics as a special case. The fact that quantum probabilities can be expressed "as the squares of quantum amplitudes" is thus derived in a natural manner, and a series of natural generalizations of the quantum formalism is delineated. Conversely, the mathematical sense in which classical physics is a special case of quantum physics is clarified. The present paper presents these relationships in the context of a "realistic" interpretation of quantum mechanics.

An attitude toward quantum mechanics which is suitable for quantum gravity in general, and for its application to cosmology in particular, is not so easy to find. Understanding the early universe requires us to reason about a time in the distant past in which observers in the ordinary sense of the word can hardly have been present. For such a situation, a philosophically "realistic" attitude toward quantum mechanics would seem to be more effective than one based on operators which must find their physical meaning in terms of "measurements". If the reality in question is taken to be something with a "space-time" character (such as a Lorentzian four-geometry, or some more fundamental discrete structure like a causal set),<sup>a</sup> then the simplest description of its dynamics will be directly in terms of probabilities of space-time alternatives, rather than indirectly in terms of operators and Hilbert spaces. For this reason, the mathematics of the "sum-over-histories" is more akin to measure theory than to (say) lattice theory or the theory of  $W^{*}$ -algebras. Quantum dynamics in such a formulation appears as a kind of generalization of the theory of stochastic processes, rather than (directly) of classical mechanics.

# E-mail: rdsorkin@mailbox.syr.edu

<sup>a</sup>Quantum gravity seems to demand a "space-time approach" for more than one reason, including the need to incorporate topology-change,<sup>1</sup> and the evident impossibility of making sense of continuous Hamiltonian evolution for a discrete structure such as a causal set (for the latter see e.g. Ref. 2).

To an untutored mind, however, the formal rules of the path-integral scheme, could seem unnatural and contrived. Why are probabilities squares of amplitudes; why are they expressed most naturally in terms of pairs of paths rather than individual paths? (cf. Refs. 3-6) We will see that a possible answer to this question emerges if one places quantum mechanics in a still more general context by asking whether quantum probabilities preserve any of the additivity of classical ones. Let us begin by considering, not the ubiquitous two-slit diffraction experiment, but a generalization which I will call the three-slit experiment.

# 1. The Three-Slit Experiment

Imagine an experiment in which an electron (say) passes through any one of the three slits and impinges on an array of detectors. Imagine that you record the diffraction pattern with all three slits open, and then repeat the procedure with some of the slits blocked off. In all, you can obtain in this way a total of eight diffraction patterns. Now superimpose the eight patterns, using a plus sign when an odd number (3 or 1) of the slits were open, and a minus sign when an even number (2 or 0) were open. What will be the result? Remarkably, you will always get zero, as can be straightforwardly demonstrated. Were the electron a classical particle, you would also get zero, since each of the three slits would contribute twice with a positive sign and twice with a negative one. In this sense, quantum randomness preserves something of the classical additivity of probabilities.

One can go further and imagine diffraction experiments with four or more slits. For each case beyond two slits the analogous superposition will again yield zero, but it turns out that these subsequent relations yield nothing new, each of them being logically contained in the three-slit relation. I will describe this hierarchy of sum rules more carefully below, but first I want to sketch the interpretive framework in which I would propose to situate them.

# 2. "Quantum Materialism" and the Quantum Measure

In accord with the above introductory remarks, we do not want to base the interpretation of the generalized probabilities we will be dealing with on some undefined concept of "measurements made by human observers". Instead I would propose a framework in which the ontology or "kinematics" and the dynamics or "laws of motion" are as sharply separated from each other as they are in classical physics (see Refs. 4, 5 and 7). In fact I will take the attitude that the ontology of quantum mechanics is identical to that of classical realism (in a space-time mode), according to which the world is a single "history". How this "history" is actually structured is for the scientists to find out, and the chosen kinematics has varied from theory to theory. According to the choice one has made, the world might be described as a collection of world lines, a space-time-geometry (= diffeomorphism equivalence

class of Lorentzian metrics), a causal set, or something else. But in any case, all meaningful statements of fact can by assumption be reduced to assertions about this one existing history. Notions such as state-vectors and observables never appear, except for the sake of computational convenience. $^c$

Where quantum theory differs from classical mechanics (in this view) is in its dynamics, which of course is stochastic rather than deterministic. As such, the theory functions by furnishing probabilities for sets of histories. More formally, it associates to a set  $A$  of histories a non-negative real number  $|A|$ , which I will call its quantum measure  $|A|$ ; and it is this measure that enters into the sum rules we will be concerned with.

In the two-slit experiment, for example, the probability that a particular detector will register the arrival of the electron is (proportional to) the measure  $|C|$  of the set  $C$  of all electron world lines which in fact pass close enough to that detector to trigger it. When we contemplate also blocking off one or the other slit, there are (for a fixed detector) three sets of histories to consider: the set  $A$  of histories which arrive at the detector after traversing the "first" slit, the corresponding set  $B$  for the "second" slit, and the original set  $C = A$  II  $B$ , the disjoint union of  $A$  and  $B$ . It is of course characteristic of quantum probability that the interference term

$$
I (A, B) := | A \mathrm {I I} B | - | A | - | B |
$$

between the slits is not zero. The surprising thing (once one has gotten used to the fact of interference itself) is that this violation of the classical probability sum rules is in a certain sense so mild, since the corresponding sum rule for three alternatives remains valid.

In any case, the important thing from the standpoint of interpretation is that the electron follows one and only one path, not somehow two at once. If probabilities are involved, it is only because the path is not determined in advance, just as it is initially undetermined in a classical stochastic process.

Given the failure of the sum rule  $I(A, B) = 0$ , it is clear that quantum probabilities cannot be interpreted in the same manner as that of classical ones in terms of (actual or fictitious) ensemble frequencies. How they should be interpreted is a question to which I will return briefly below, and more at length elsewhere. Here, my main purpose is to discuss the sum rules themselves.

# 3. Quantum Measure Theory and Its Generalizations

What ordinarily makes it difficult to regard quantum mechanics as in essence a modified form of probability theory, is the peculiar fact that it works with complex

"amplitudes" rather than directly with probabilities, the former being more like square roots of the latter. To put this peculiarity in context, consider the following series of symmetric set-functions, which generalize the interference term  $I(A,B)$  introduced above. (Notice that all the sets  $A, B, C, \ldots$  which occur here are mutually disjoint.)

$$
I _ {1} (A) \equiv | A |,
$$

$$
I _ {2} (A, B) \equiv | A \mathrm {I I} B | - | A | - | B |,
$$

$$
I _ {3} (A, B, C) \equiv | A \mathrm {I I} B \mathrm {I I} C | - | A \mathrm {I I} B | - | B \mathrm {I I} C | - | A \mathrm {I I} C | + | A | + | B | + | C |,
$$

or in general,

$$
\begin{array}{l} I _ {n} \left(A _ {1}, A _ {2}, \dots , A _ {n}\right) \equiv | A _ {1} \text {I I} A _ {2} \text {I I} \dots A _ {n} | - \sum | (n - 1) \text {s e t s} | \\ + \sum | (n - 2) \text {s e t s} | \dots \pm \sum_ {j = 1} ^ {n} | A _ {j} |. \tag {1} \\ \end{array}
$$

These expressions are related sequentially in a simple manner expressed by the following lemma, whose straightforward inductive proof will be given elsewhere.

Lemma.  $I_{n+1}(A_0, A_1, A_2, \ldots, A_n) = I_n(A_0 \text{ II } A_1, A_2, \ldots, A_n) - I_n(A_0, A_2, \ldots, A_n)$

$$
- I _ {n} \left(A _ {1}, A _ {2}, \dots , A _ {n}\right).
$$

For each  $n$  one obtains a possible sum rule by setting  $I_{n}$  to zero. It is an immediate consequence of the lemma that the  $n$ th such sum rule entails the  $(n + 1)$ st. Hence the sum rules form a hierarchy of ever decreasing strength. The first sum rule in the hierarchy,  $I_{1} = 0$ , trivializes the measure and is therefore uninteresting. The second expresses precisely the additivity of classical measure theory, or equivalently the additivity of classical probabilities, when they are regarded as set-measures in the Kolmogorov manner. Accordingly, the third sum rule,  $I_{3}(A, B, C) \equiv 0$ , defines a generalization of measure theory which preserves most, but not all, of the additivity of classical probabilities. This is the level of quantum measure theory. The fourth and higher sum rules define still more general forms of measure theory, which may be regarded as natural extensions of quantum mechanics.

A second immediate consequence of the lemma is the fact that  $I_{n+1}$  vanishes if and only if  $I_n$  is "additive" in each argument, given the mutual disjointness of all its arguments. Thus each sum rule is associated with a kind of multilinearity (really multi-additivity) of the function which measures the failure of the next stronger sum rule to hold. At the quantum level, specifically, we learn that  $I_2$  is bi-additive, and we will see that the peculiar quadratic relationship between quantum amplitudes and probabilities corresponds directly to this feature of  $I_2$ . In the next generalization beyond the quantum level, tri-additivity would take the place of bi-additivity and (insofar as something like a quantum state-space were relevant at all) some sort of trilinear form associated to  $I_3$  would presumably replace the familiar inner product

of quantum Hilbert space. In what follows, however we will limit ourselves to the quantum case as defined by the  $n = 3$  sum rule,

$$
\left. \right.\left| A \mathrm {I I} B \mathrm {I I} C \right| - \left| A \mathrm {I I} B \right| - \left| B \mathrm {I I} C \right| - \left| A \mathrm {I I} C \right| + \left| A \right| + \left| B \right| + \left| C \right| = 0. \tag {2}
$$

Given this sum rule, we can, as just pointed out, conclude immediately from the lemma that  $I_{2}$  is bi-additive in the sense that

$$
I (A \amalg B, C) = I (A, C) + I (B, C), \tag {3}
$$

whenever  $A, B$  and  $C$  are mutually disjoint. (Henceforth, I will usually omit the subscript '2' from 'I2'). Full bi-additivity of  $I$ , however would require this same equality even when  $C$  overlaps  $A$  or  $B$ , a situation in which  $I$  has not even been defined. This raises the obvious question whether we can extend the definition of  $I(A, B)$  to general arguments in such a way as to preserve its bi-additivity.

Supposing such an extension has been made, consider the combination  $I(A \amalg B, A \amalg B)$ . Expanding it out via bi-additivity and rearranging, we find that, for disjoint subsets  $A$  and  $B$ ,

$$
2 I (A, B) = I (A \mathrm {I I} B, A \mathrm {I I} B) - I (A, A) - I (B, B),
$$

which, on comparison with the defining equation for  $I_{2}$ , strongly suggests the identification

$$
I (X, X) = 2 | X |. \tag {4}
$$

If we adopt this as the value of  $I$  on equal arguments, then its value for arbitrary arguments is completely determined by bi-additivity; and a short computation which will appear elsewhere confirms that the resulting definition of  $I(A,B)$  is self-consistent. The end result is that  $I$  can be expressed in terms of the quantum measure  $|\cdot|$  in several equivalent forms, of which two are the following:

$$
\begin{array}{l} I (A, B) = | A \cup B | + | A \cap B | - | A \backslash B | - | B \backslash A |, \tag {5} \\ I (A, B) = | A \Delta B | + | A | + | B | - 2 | A \backslash B | - 2 | B \backslash A |. \\ \end{array}
$$

(In these equations the symbol  $\backslash$  denotes set-theoretic difference and  $\Delta$  denotes symmetric difference.)

We thus conclude that any generalized measure obeying the quantum sum rule (2) can be expressed in the form  $|X| = I(X, X) / 2$ , where  $I$  is the bi-additive, real valued set function of (5). Conversely, we could begin with such a set-function whose diagonal values are all non-negative, and use it to define a quantum measure  $|\cdot|$  obeying the sum rule (2). This is what is normally done, with  $I$  taken to be what Ref. 9 would call (twice the real part of) the "decoherence functional". The postulate that quantum probabilities should be derived from such a bi-additive function can thus be replaced by the assumption that they obey the fundamental sum rule (2).

For completeness, let me conclude this section by sketching the way that the ordinary nonrelativistic quantum mechanics of point particles fits into this framework. Also, since none of our discussion has attempted to address the measure-theoretic technicalities associated with continuous spaces of histories, let me pretend that the set of all possible particle paths has finite cardinality. Then the measure of any set  $A = \{x,y,\ldots ,z\}$  of paths can be formally expressed as  $|A| = " (1 / 2 ) I ( x + y + \dots +z,x + y + \dots +z)"$ , which is to be evaluated by expanding out the sums via bilinearity and interpreting  $I(x,y)$  as  $I(\{x\} ,\{y\})$ . To complete the construction we must take  $I(x,y)$  to be essentially  $e^{-iS(x)}e^{iS(y)} + (\text{complex conjugate})$ , where  $S(x)$  is the action of the path  $x$ .

Actually the true expression is somewhat more complicated than this, and requires the introduction of a "truncation time"  $T$  lying to the future of the span of time to which the properties defining  $A$  refer. The actual rule then involves paths truncated to time  $T$ , and the expression for  $I(x,y)$  acquires a delta-function which "ties together" the final end points of the truncated paths. With the convention that  $x$  and  $y$  now represent such truncated paths,  $|A|$  is given finally as the sum over all  $x$  and  $y$  belonging to  $A$  of the expression,

$$
I (x, y) = \delta (x (T), y (T)) e ^ {- i S (x)} e ^ {i S (y)} + (\text {c o m p l e x c o n j u g a t e}).
$$

The import of this rule can also be rendered by the statement that the measure  $|A|$  of a set of trajectories is the norm-squared of the wave function which is produced at time  $T$  by restricting the path-sum to the set of paths belonging to  $A$ . This last statement is recognizably the standard quantum probability rule, as expressed in sum-over-histories language.

# 4. Final Remarks on Interpretation and Some Open Questions

Although we have succeeded in tracing the main traits of the quantum formalism to the fundamental sum rule (2) for the quantum measure, we have only raised, without settling, the question of how this measure or "quantum probability" is to be interpreted physically. That question entrains far too many issues for a short manuscript to deal with, but the present paper would be incomplete without at least some indication of an answer.

With a frequency interpretation of the measure unavailable, it is natural to adopt the attitude that locates the predictive content of a (classical or quantum) probabilistic theory in the assertion that events of sufficiently small measure, for all practical purposes, do not occur at all: they are precluded events in the language of Ref. 10. The meaning of the measure, then, would be that the true history will not (or "almost never") belong to a precluded set  $A$ . The trouble with this rule is that, if used without the requisite tact, it leads to mutually conflicting predictions. In Feynman's well-known exposition of the two-slit experiment, for example, the partition of the histories which properly comes into play depends on what question we are asking, and not all questions can be simultaneously valid.

Here, asking a question is not something "mental", but something "material" like putting a detector in place, and paradox is avoided because the questions leading to conflicting preclusions are not all realizable within a single experiment.

However satisfactory such a resolution might be for most practical purposes, it threatens to bring back the same subjectivity and human-centeredness which we have been at pains to reject. We can retain objectivity, I believe, by abstracting from the idea of measurement, the idea of correlation, and limiting the application of preclusion to situations where an appropriate type of correlation occurs. Briefly, the idea is that, when variables pertaining to spacelike-separated regions become correlated (in the sense that the correlation-breaking possibilities correspond to sets of histories of small or zero measure), then the failure of the correlation is precluded. (For example, if one of a pair of electrons with anti-correlated spins traverses the “ $\sigma_z = +1$ ” beam of a Stern-Gerlach analyzer, then the other must traverse the “ $\sigma_z = -1$ ” beam of its analyzer, assuming these events are space-like separated.) Moreover, we predict in such a situation that, if one of the correlated possibilities  $P$  is itself of negligible measure, then it is also precluded (i.e. we predict that the true history almost certainly does not belong to  $P$ ). Notice that these predictions are statements about the history itself, not just about “what we would find if we observed the variables in question”.

The double predictive principle just enunciated seems sufficient for using quantum mechanics in the way we use it, without leading to any obvious contradictions. Unfortunately it does lead to some unobvious contradictions, but all those that I know of can be excluded by a small refinement of the predictive scheme. The refinement in question, and further details of the resulting prescription will be discussed in Ref. 8. Here there is space only to raise a few further questions which are naturally suggested by the preceding development.

The first question is whether some further axiom of general validity can or should be added to our basic sum rule (2). It is a feature of standard quantum mechanics (and also of classical probability theory) that the measure of a set of histories  $A$  is unaltered when a disjoint set of measure zero is adjoined to it; in particular the union of two disjoint sets of measure zero will also have zero measure. Since this property is natural, and turns out to be important for the analysis of Ref. 8, it appears reasonable to adopt it as a further condition on the measure  $|\cdot|$ . (For a related proposal in the language of "decoherence" see Ref. 11.)

A second question is whether there is a sense in which a process governed by quantum measure theory can be called Markovian. With the idea of amplitude not taken for granted, it is not obvious that the answer is yes, but if it is, then it would be interesting to find necessary and sufficient conditions in terms of  $I(\cdot, \cdot)$  for a quantum measure to be Markovian. Such conditions ought to clarify what makes ordinary quantum mechanics special among possible solutions of (2), and might suggest novel generalizations of Hamiltonian evolution as well.

A third question is whether the introduction of the "truncation time"  $T$  in the previous section was really needed. In the classical theory of stochastic processes,

such a truncation of the histories is unnecessary, and the similarity of that theory to the present formulation offers hope of avoiding it in "quantum stochastic mechanics" as well. Success in this could be crucial for quantum gravity, which lacks any background time with respect to which truncation could be carried out (see however Ref. 4).

The asking of these last two questions highlights the fact that not all of the somewhat elaborate details of the construction of  $I(A, B)$  in the previous section are included in the simple sum rule (2). Some of them are related instead to the Markovian character of nonrelativistic quantum mechanics, and beyond that, to the unitary evolution it embodies. However, non-unitary and non-Markovian evolution is the rule in open systems (e.g. systems coupled to "reservoirs"), so that the greater generality of what we have here called "quantum measure theory" already has important application. Moreover, it appears unlikely that unitarity will have fundamental meaning for quantum gravity, and one may suspect that something at least as general as full quantum measure theory will be needed for that theory, if not some still more general dynamical framework, perhaps corresponding to one of the higher sum rules described in this letter.

Finally, let us return for a moment to the three-slit experiment with which we began. If some more general form of dynamics than quantum mechanics is at work in nature, it should show itself in a failure of the sum rule (2) for which the three-slit discussion is a prototype. Thus, any situation in which three distinct alternatives can interfere offers a potential "null test" of the validity of quantum mechanics. It might be worthwhile looking for experimentally realizable situations of this type where, unlike with ordinary diffraction, the satisfaction of the test is not already a foregone conclusion.

In conclusion, I would like to thank the participants in the Syracuse Relativity Tea for stimulating comments on these topics and R. B. Salgado in particular for suggesting the most appropriate formulation of the lemma utilized above. This research was partly supported by NSF grant PHY 9307570.

# References

1. R. D. Sorkin, “Consequences of space-time topology”, in Proc. of the Third Canadian Conference on General Relativity and Relativistic Astrophysics, Victoria, Canada, May 1989, eds. A. Coley, F. Cooperstock and B. Tupper (World Scientific, 1990), pp. 137-163.  
2. L. Bombelli, J. Lee, D. Meyer and R. D. Sorkin, Phys. Rev. Lett. 59, 521 (1987); R. D. Sorkin, "Space-time and causal sets", in Relativity and Gravitation: Classical and Quantum, Proc. of the SILARG VII Conference, Cocoyoc, Mexico, December, 1990, eds. J. C. D'Olivo, E. Nahmad-Achar, M. Rosenbaum, M. P. Ryan, L. F. Urrutia and F. Zertuche (World Scientific, 1991), pp. 150-173.  
3. I. Bialynicki-Birula, "Transition amplitudes versus transition probabilities and a reduplication of space-time", in Quantum Concepts in Space and Time, eds. R. Penrose and C. J. Isham (Clarendon, 1986), pp. 226-235.  
4. R. D. Sorkin, "On the role of time in the sum-over-histories framework for gravity",

in Proc. of the Conf. on The History of Modern Gauge Theories, Logan, Utah, July, 1987; to be published in Int. J. Theor. Phys. (1994, to appear).  
5. Sinha, Sukanya and R. D. Sorkin, “A sum-over-histories-account of an EPR(B) experiment”, Found. Phys. Lett. 4, 303 (1991).  
6. R. D. Sorkin, "Problems with causality in the sum-over-histories framework for quantum mechanics", in *Conceptual Problems of Quantum Gravity*, Osgood Hill, Massachusetts, May, 1988 (Birkhäuser, 1991), pp. 217-227.  
7. R. D. Sorkin, "Forks in the road, on the way to quantum gravity", talk presented at the Brill-Misner Fest, College Park, Maryland 1993, Syracuse University preprint SU-GP-93-12-2.  
8. R. D. Sorkin, in preparation.  
9. J. B. Hartle, "The quantum mechanics of cosmology", in Quantum Cosmology and Baby Universes: Proceedings of the 1989 Jerusalem Winter School for Theoretical Physics, eds. S. Coleman et al. (World Scientific, 1991).  
10. R. Geroch, "The Everett interpretation", Nous 18, 617 (1984).  
11. C. J. Isham, "Quantum logic and the histories approach to quantum theory", Imperial College preprint Imperial/TP/92-93/39, (gr-qc/9308006).