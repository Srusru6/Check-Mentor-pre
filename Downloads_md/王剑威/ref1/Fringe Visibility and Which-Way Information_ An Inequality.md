# Fringe Visibility and Which-Way Information: An Inequality

Berthold-Georg Englert*

Max-Planck-Institut für Quantenoptik, Hans-Kopfermann-Strasse 1, D-85748 Garching, Germany (Received 21 May 1996)

An inequality is derived according to which the fringe visibility in a two-way interferometer sets an absolute upper bound on the amount of which-way information that is potentially stored in a which-way detector. In some sense, this inequality can be regarded as quantifying the notion of wave-particle duality. The derivation of the inequality does not make use of Heisenberg's uncertainty relation in any form. [S0031-9007(96)00950-7]

PACS numbers: 03.65.Bz

Bohr's principle of complementarity [1] states that quantum systems ("quantons" [2] for short) possess properties that are equally real but mutually exclusive. The best known example is what is colloquially termed wave-particle duality. In a loose manner of speaking it is sometimes phrased similarly to the following: Depending on the experimental situation a quanton behaves either like a particle or like a wave.

To be more specific, let us consider a two-way interferometer such as Young's double-slit experiment or a Mach-Zehnder setup. The wavelike property is then documented by well-visible interference fringes, whereas the particlelike property is evident if one can tell along which way the interferometer has been traversed.

The notions of particle and wave are associated with mental pictures that are borrowed from classical (i.e., prequantum) physics. These associations are dangerous because of their obvious limitations. Therefore, "wave-particle duality" should perhaps be abandoned in favor of a more neutral term, such as "interferometric duality" or simply "duality." The general formulation of this concept could read as follows.

Duality.-The observations of an interference pattern and the acquisition of which-way information are mutually exclusive.

The extreme situations "perfect fringe visibility and no which-way information" and "full which-way information and no fringes" are familiar from textbook discussions. But intermediate stages deserve further study.

The objective of this Letter is the derivation of an inequality that quantifies duality by stating to which extent partial fringe visibility and partial which-way knowledge are compatible. The quantitative measure of the fringe visibility is the usual one, and which-way knowledge will be turned into a number with the aid of an approach that is originally due to Wootters and Zurek [3].

At the intermediate stage of the interferometer—between beam splitter and beam merger, see Fig. 1—the two ways can be labeled by quantum numbers  $+1$  and  $-1$ , say. Accordingly, we are invited to describe the relevant degree of freedom of the quanton by analogs of Pauli's spin operators  $\pmb{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ . Prior to

entering the interferometer the quantum is in an initial state that is characterized by the statistical operator

$$
\begin{array}{l} \rho_ {Q} ^ {(i)} = \frac {1 + \mathbf {s} ^ {(i)} \cdot \boldsymbol {\sigma}}{2} \\ = \frac {1}{2} \left(1 + s _ {x} ^ {(i)} \sigma_ {x} + s _ {y} ^ {(i)} \sigma_ {y} + s _ {z} ^ {(i)} \sigma_ {z}\right) \tag {1} \\ \end{array}
$$

with an initial Bloch vector  $\mathbf{s}^{(i)} = \mathrm{tr}_Q\{\pmb {\sigma}\rho_Q^{(i)}\}$ . It is sufficiently general to represent the action of the beam splitter and the beam merger by

$$
\rho_ {Q} \rightarrow \exp \left(- i \frac {\pi}{4} \sigma_ {y}\right) \rho_ {Q} \exp \left(i \frac {\pi}{4} \sigma_ {y}\right),
$$

whereas the phase shifter at the central stage effects

$$
\rho_ {Q} \rightarrow \exp \left(- i \frac {\phi}{2} \sigma_ {z}\right) \rho_ {Q} \exp \left(i \frac {\phi}{2} \sigma_ {z}\right). \tag {2}
$$

Consequently, the interferometer of Fig. 1(a) turns  $\rho_{Q}^{(i)}$  into the final state

$$
\rho_ {Q} ^ {(f)} = \frac {1}{2} (1 + \mathbf {s} ^ {(f)} \cdot \boldsymbol {\sigma}), \tag {3}
$$

with

$$
\begin{array}{l} \mathbf {s} ^ {(f)} = \left(- s _ {x} ^ {(i)}, s _ {y} ^ {(i)} \cos \phi + s _ {z} ^ {(i)} \sin \phi , \right. \\ s _ {y} ^ {(i)} \sin \phi - s _ {z} ^ {(i)} \cos \phi). \\ \end{array}
$$

After the quanton has passed the beam merger, the observable  $\sigma_z$  is measured and the relative frequency with which the value  $-1$  is found reveals the interference pattern,

$$
\begin{array}{l} p _ {\phi} = \operatorname {t r} _ {Q} \left\{\frac {1}{2} (1 - \sigma_ {z}) \rho_ {Q} ^ {(f)} \right\} \\ = \frac {1}{2} \left(1 - s _ {y} ^ {(i)} \sin \phi + s _ {z} ^ {(i)} \cos \phi\right), \\ \end{array}
$$

so that

$$
\mathcal {V} _ {0} = \left[ \left(s _ {y} ^ {(i)}\right) ^ {2} + \left(s _ {z} ^ {(i)}\right) ^ {2} \right] ^ {1 / 2}
$$

is the corresponding a priori fringe visibility.

![](images/e1dfef6c902d97b79a9bf08b8914eb4f48a3207e1bb9b397b89f3bbdfd67ad6b.jpg)

![](images/3b526d9a98e8122a48de69ca8d539c956f5a32a0401749901906402d86a75b0b.jpg)  
FIG. 1. Schematic two-way interferometer. (a) The beam splitter BS distributes the input among the two ways; after the phase shifter PS has acted in its  $\phi$  dependent manner, the beam merger BM recombines the contributions and produces the output. Measurements on the output may either reveal the  $\phi$  dependent interference pattern, or alternatively determine the way that has been taken. (b) When the interferometer is supplemented by a which-way detector WWD, then both the interference pattern may be observed and the which-way information may be acquired, within the limits set by duality.

The probabilities for taking either one of the two ways are

$$
\begin{array}{l} w _ {\pm} = \operatorname {t r} _ {Q} \left\{\frac {1}{2} (1 \pm \sigma_ {z}) \exp \left(- i \frac {\pi}{4} \sigma_ {y}\right) \rho_ {Q} ^ {(i)} \exp \left(i \frac {\pi}{4} \sigma_ {y}\right) \right\} \\ = \operatorname {t r} _ {Q} \left\{\frac {1}{2} (1 \pm \sigma_ {x}) \rho_ {Q} ^ {(f)} \right\} = \frac {1}{2} (1 \mp s _ {x} ^ {(i)}). \tag {4} \\ \end{array}
$$

The magnitude of their difference,

$$
\mathcal {P} = | w _ {+} - w _ {-} | = | s _ {x} ^ {(i)} |,
$$

is the predictability of the ways through the interferometer. This number, which is in the range  $0, \ldots, 1$ , is a quantitative measure of the a priori which-way knowledge. If one bets on the more probable way, then the probability of predicting the way correctly is  $(1 + \mathcal{P}) / 2$ . In particular, if the interferometer is operated symmetrically,  $w_{+} = w_{-} = \frac{1}{2}$  so that  $\mathcal{P} = 0$ , then  $50\%$  of the predictions are right and the other  $50\%$  are wrong. In short, there is nothing predictable about the ways in a symmetric interferometer.

Since the length of the Bloch vector  $\mathbf{s}^{(i)}$  must not exceed unity, one immediately establishes the inequality

$$
\mathcal {P} ^ {2} + \mathcal {V} _ {0} ^ {2} \leq 1. \tag {5}
$$

This observation has been made by Greenberger and Yasin [4]; it is implicitly contained in the work of Wootters and Zurek [3] and also in a paper by Mandel [5]. The measurements by Rauch, Summhammer, and Tuppinger [6], who introduce an asymmetry into a neutron interferometer, are consistent with (5).

Let us consider symmetric interferometers with maximal a priori fringe visibility,

$$
s _ {x} ^ {(i)} = 0, \qquad s _ {z} ^ {(i)} + i s _ {y} ^ {(i)} = e ^ {- i \theta},
$$

which are coupled to another physical system that is meant to serve as a which-way detector as indicated in Fig. 1(b). The detector is initially prepared in a state  $\rho_{D}^{(i)}$  so that the combined system of quantum and detector has an initial statistical operator

$$
\rho^ {(i)} = \rho_ {Q} ^ {(i)} \rho_ {D} ^ {(i)}. \tag {6}
$$

As a result of the interaction between quantum and detector the detector state is altered in accordance with

$$
\rho_ {D} \rightarrow U _ {\pm} ^ {\dagger} \rho_ {D} U _ {\pm} \quad \text {f o r t h e} \sigma_ {z} = \pm 1 \text {w a y},
$$

where  $U_{+}$  and  $U_{-}$  are unitary operators that affect solely the degree(s) of freedom of the detector. Thus what happens at the central stage of the interferometer is now described by the unitary operator

$$
\frac {1 + \sigma_ {z}}{2} e ^ {i \phi / 2} U _ {+} + \frac {1 - \sigma_ {z}}{2} e ^ {- i \phi / 2} U _ {-};
$$

it replaces  $\exp \left(\frac{i}{2}\phi \sigma_z\right)$  of (2).

The initial state (6) is transformed into the final state

$$
\begin{array}{l} \rho^ {(f)} = \frac {1 + \sigma_ {x}}{4} U _ {+} ^ {\dagger} \rho_ {D} ^ {(i)} U _ {+} + \frac {1 - \sigma_ {x}}{4} U _ {-} ^ {\dagger} \rho_ {D} ^ {(i)} U _ {-} \\ - \frac {\sigma_ {z} - i \sigma_ {y}}{4} e ^ {- i (\phi - \theta)} U _ {+} ^ {\dagger} \rho_ {D} ^ {(i)} U _ {-} \\ - \frac {\sigma_ {z} + i \sigma_ {y}}{4} e ^ {i (\phi - \theta)} U _ {-} ^ {\dagger} \rho_ {D} ^ {(i)} U _ {+}, \\ \end{array}
$$

which yields the final states of the quanton and the detector upon tracing over the other degree of freedom. The quanton state is of the form (3) with

$$
s _ {x} ^ {(f)} = 0, \quad s _ {z} ^ {(f)} + i s _ {y} ^ {(f)} = - e ^ {- i (\phi - \theta)} C,
$$

where  $C = \mathrm{tr}_D\{U_+^\dagger \rho_D^{(i)}U_- \}$  is a complex contrast factor. The fringe visibility is therefore given by the magnitude of this number,

$$
\mathcal {V} = | C |. \tag {7}
$$

The final detector state

$$
\begin{array}{l} \rho_ {D} ^ {(f)} = \operatorname {t r} _ {Q} \left\{\rho^ {(f)} \right\} = \frac {1}{2} U _ {+} ^ {\dagger} \rho_ {D} ^ {(i)} U _ {+} + \frac {1}{2} U _ {-} ^ {\dagger} \rho_ {D} ^ {(i)} U _ {-} \\ = \frac {1}{2} \rho_ {D} ^ {(+)} + \frac {1}{2} \rho_ {D} ^ {(-)} \\ \end{array}
$$

is the sum of the two final states corresponding to the two ways, weighted by the fraction of quantons taking the respective way— $50\%$  each in the symmetric interferometer under consideration.

The extraction of the which-way information stored in the detector requires the measurement of a suitable observable  $W$  with eigenvalues  $W'$  and eigenkets  $|W'\rangle$ . We take for granted that the relevant eigenvalues of  $W$  are

not degenerate. Suppose that the eigenvalue  $W'$  has been found. This happens with a relative frequency of

$$
\begin{array}{l} \langle W ^ {\prime} | \rho_ {D} ^ {(f)} | W ^ {\prime} \rangle = \frac {1}{2} \langle W ^ {\prime} | \rho_ {D} ^ {(+)} | W ^ {\prime} \rangle \\ + \frac {1}{2} \langle W ^ {\prime} | \rho_ {D} ^ {(-)} | W ^ {\prime} \rangle , \\ \end{array}
$$

where the two summands refer to the two ways. Extending an idea by Wootters and Zurek [3], we note that the best guess about the way one can thus make is to opt for the way that contributes most to  $\langle W'|\rho_D^{(f)}|W'\rangle$ . In many repeated experiments, this yields a "likelihood" for guessing the way right" that is given by

$$
\begin{array}{l} \mathcal {L} _ {W} = \sum_ {W ^ {\prime}} \operatorname {M a x} \left\{\frac {1}{2} \langle W ^ {\prime} | \rho_ {D} ^ {(+)} | W ^ {\prime} \rangle , \frac {1}{2} \langle W ^ {\prime} | \rho_ {D} ^ {(-)} | W ^ {\prime} \rangle \right\} \\ = \frac {1}{2} + \frac {1}{4} \sum_ {W ^ {\prime}} | \langle W ^ {\prime} | (\rho_ {D} ^ {(+)} - \rho_ {D} ^ {(-)}) | W ^ {\prime} \rangle |. \\ \end{array}
$$

Its calculated value can be checked experimentally if the interferometer is modified such that the actual way is determined rather than the fringe pattern. This can be done, for example, either by removing the beam merger and measuring  $\sigma_z$  or by leaving the beam merger in place and measuring  $\sigma_x$  in the final state  $\rho^{(f)}$ ; these two possibilities correspond to the two traces in (4). Since such a measurement yields also the probabilities  $\langle W'|\rho_D^{(\pm)}|W'\rangle$ , the numerical value of the likelihood  $\mathcal{L}_W$  can be inferred from experimental data.

This value depends on the observable  $W$  that is measured. An unfortunate choice could result in  $\mathcal{L}_W = \frac{1}{2}$ , in which case one could just as well throw dice. The largest value of  $\mathcal{L}_W$  is obtained if the (relevant) eigenkets  $|W^{\prime}\rangle$  of  $W$  are also eigenkets of the difference  $\rho_D^{(+)} - \rho_D^{(-)}$ . Accordingly, there is an absolute optimum for  $\mathcal{L}_W$ , viz.

$$
\mathcal {L} _ {W} \leq \mathcal {L} _ {\text {o p t}} = \frac {1}{2} (1 + \mathcal {D}), \tag {8}
$$

with

$$
\mathcal {D} = \frac {1}{2} \operatorname {t r} _ {D} \left\{\left| \rho_ {D} ^ {(+)} - \rho_ {D} ^ {(-)} \right| \right\}. \tag {9}
$$

In mathematical terms, this number  $\mathcal{D}$  is the distance between  $\rho_D^{(+)}$  and  $\rho_D^{(-)}$  in the trace-class norm; its physical significance is, however, more important:  $\mathcal{D}$  is a quantitative measure of the distinguishability of the ways, i.e., of the amount of which-way information that has become available. The ways cannot be distinguished at all if  $\mathcal{D} = 0$ , and they can be held apart completely if  $\mathcal{D} = 1$ .

The stage is now set for reporting the central result of this Letter. The fringe visibility  $\mathcal{V}$  of (7) and the distinguishability of (9) obey the inequality

$$
\mathcal {D} ^ {2} + \mathcal {V} ^ {2} \leq 1, \tag {10}
$$

which is a fundamental quantitative statement about duality. Of course, it comprises the extreme situations mentioned above inasmuch as  $\mathcal{V} = 1$  implies  $\mathcal{D} = 0$  and  $\mathcal{D} = 1$  implies  $\mathcal{V} = 0$ .

The equal sign holds in (10) always if the detector is prepared in a pure state,

$$
\rho_ {D} ^ {(i)} = | d \rangle \langle d |:
$$

$$
\mathcal {D} = (1 - | \langle d | U _ {-} U _ {+} ^ {\dagger} | d \rangle | ^ {2}) ^ {1 / 2}, \tag {11}
$$

$$
\mathcal {V} = | \langle d | U _ {-} U _ {+} ^ {\dagger} | d \rangle |.
$$

The general proof of the duality relation (10) is based on the triangle inequality for the trace-class norm,

$$
\operatorname {t r} \left\{\left| A + B \right| \right\} \leq \operatorname {t r} \left\{\left| A \right| \right\} + \operatorname {t r} \left\{\left| B \right| \right\},
$$

which holds for all trace-class operators  $A$  and  $B$ . Upon inserting the spectral decomposition of  $\rho_{D}^{(i)}$ ,

$$
\rho_ {D} ^ {(i)} = \sum_ {k} D _ {k} | d _ {k} \rangle \langle d _ {k} |
$$

(with  $D_{k}\geq 0,\sum_{k}D_{k} = 1$  , and  $\langle d_j|d_k\rangle = \delta_{jk}$  , of course), into (9) yields

$$
\begin{array}{l} \mathcal {D} \leq \frac {1}{2} \sum_ {k} D _ {k} \operatorname {t r} _ {D} \left\{ \right.\left| U _ {+} ^ {\dagger} \right| d _ {k} \left. \right\rangle\left\langle \right. d _ {k} \left. \right| U _ {+} - \left. U _ {-} ^ {\dagger} \right| d _ {k} \left. \right\rangle\left\langle \right. d _ {k} \left. \right| U _ {-} | \} \\ = \sum_ {k} D _ {k} (1 - | \langle d _ {k} | U _ {-} U _ {+} ^ {\dagger} | d _ {k} \rangle | ^ {2}) ^ {1 / 2}, \\ \end{array}
$$

where the last step makes use of the pure-state result (11). In conjunction with

$$
\mathcal {V} = \left| \sum_ {k} D _ {k} \langle d _ {k} | U _ {-} U _ {+} ^ {\dagger} | d _ {k} \rangle \right|,
$$

this leads to

$$
\begin{array}{l} \mathcal {D} ^ {2} + \mathcal {V} ^ {2} \leq \sum_ {j, k} D _ {j} D _ {k} \left[ \sqrt {1 - | u _ {j} | ^ {2}} \sqrt {1 - | u _ {k} | ^ {2}} \right. \\ \left. + \frac {1}{2} u _ {j} ^ {*} u _ {k} + \frac {1}{2} u _ {k} ^ {*} u _ {j} \right], \tag {12} \\ \end{array}
$$

where  $u_{k} = \langle d_{k}|U_{-}U_{+}^{\dagger}|d_{k}\rangle$  is a convenient abbreviation. The magnitude of these complex numbers does not exceed unity,  $|u_{k}|\leq 1$ , and therefore  $0\leq [\dots ]\leq 1$  holds for the square brackets in (12). Accordingly, one gets

$$
\mathcal {D} ^ {2} + \mathcal {V} ^ {2} \leq \sum_ {j, k} D _ {j} D _ {k} = [ \operatorname {t r} _ {D} \{\rho_ {D} ^ {(i)} \} ] ^ {2} = 1,
$$

and this closes the case.

It must be emphasized that this proof of the duality relation (10) does not rely on an uncertainty relation of the Heisenberg-Robertson kind [7], i.e.,

$$
\delta X \delta Y \geq \frac {1}{2} | \langle [ X, Y ] \rangle | \tag {13}
$$

for the spreads of two observables  $X$  and  $Y$  and the expectation value of their commutator. One understands why (10) cannot be an uncertainty relation in disguise when noting that really only one observable is involved, not two. This observable  $X$  is identified by  $U_{-}U_{+}^{\dagger} =$

$\exp (iX)$  . Then both the distinguishability  $\mathcal{D}$  and the visibility  $\mathcal{V}$  involve  $X$

$$
\mathcal {D} = \frac {1}{2} \operatorname {t r} _ {D} \left\{\left| \rho_ {D} ^ {(i)} - e ^ {- i X} \rho_ {D} ^ {(i)} e ^ {i X} \right| \right\},
$$

$$
\mathcal {V} = | \mathrm {t r} _ {D} \{\rho_ {D} ^ {(i)} e ^ {i X} \} |,
$$

but no second observable shows up. In conclusion, the duality relation (10) is logically independent of the uncertainty relation (13).

It is equally important to realize that the inequalities (5) and (10) convey utterly different messages despite their great similarity, because the predictability  $\mathcal{P}$  and the distinguishably  $\mathcal{D}$  represent pieces of which-way knowledge of very different kinds. Furthermore, the two inequalities concern different degrees of freedom. In (5) one meets an immediate consequence of the positivity of the statistical operator (1) that specifies the initial state of the quanton. In marked contrast, (10) originates in the quantum properties of the detector. The quantum aspects of the which-way detection enforce duality and thus make sure that the principle of complementarity is not circumvented.

Upon combining (10) with (8) one gets the inequality

$$
\frac {1}{2} \leq \mathcal {L} _ {\mathrm {o p t}} \leq \frac {1}{2} + \frac {1}{2} \sqrt {1 - \mathcal {V} ^ {2}}, \tag {14}
$$

according to which the fringe visibility limits the experimenter's ability of guessing the way right. To begin with, this applies to symmetric interferometers with predictability  $\mathcal{P} = 0$  and a priori visibility  $\mathcal{V}_0 = 1$ . This is no real restriction, however, because asymmetric interferometers can be analyzed in an analogous manner. The fringe visibility is then

$$
\mathcal {V} = | C | \mathcal {V} _ {0}
$$

rather than (7), and the optimal likelihood is given by

$$
\mathcal {L} _ {\mathrm {o p t}} = \frac {1}{2} + \frac {1}{2} \operatorname {t r} _ {D} \{| w _ {+} \rho_ {D} ^ {(+)} - w _ {-} \rho_ {D} ^ {(-)} | \},
$$

which involves the a priori probabilities of the ways [cf. Eq. (4)] and generalizes (8) with (9). The resulting generalization of (14) reads

$$
\begin{array}{l} \frac {1}{2} (1 + \mathcal {P}) \leq \mathcal {L} _ {\mathrm {o p t}} \leq \frac {1}{2} \\ + \frac {1}{2} \sqrt {1 - (1 - \mathcal {P} ^ {2}) (\mathcal {V} / \mathcal {V} _ {0}) ^ {2}} \tag {15} \\ \end{array}
$$

with  $\mathcal{V} \leq \mathcal{V}_0$ . The reasoning that justifies the upper bound is essentially the same as the one for the upper bound in (14), and the lower bound is a consequence of  $\operatorname{tr}\{|A|\} \geq |\operatorname{tr}\{A\}|$ . Since  $\mathcal{P}$  is non-negative and (5)

holds, it is clear that (15) is more stringent than (14). Consequently, (14) applies to asymmetric interferometers as well.

In setups of the kind depicted in Fig. 1(b), the same physical mechanism can be used both for the phase shifting and the which-way detection. There are other schemes, such as Einstein's recoiling-slit proposal [8] or the quantum-optical Ramsey interferometer [9], in which the beam splitter also acts as the which-way detector. For them, the bounds of (14) hold too, but the analysis is somewhat more involved [10].

This work was begun while I was a visitor at the Laboratoire de Physique des Lasers, Université Paris-Nord, in Villetaneuse. I am very grateful for the hospitable environment provided by Christian Miniatura and Jacques Baudon as well as the other members of the group, and I extend my sincerest thanks to the Centre National de la Recherche Scientifique (C.N.R.S.) for supporting my stay so generously.

*Presently at Arbeitsgruppe "Nichtklassisches Licht" der Max-Planck-Gesellschaft an der Humboldt-Universität, Rudower Chausee 5, Gebäude 10.16, D-12484 Berlin, Germany.  
[1] N. Bohr, Naturwissenschaften 16, 245 (1928); Nature (London) 121, 580 (1928). A formulation in mathematical terms that is based on the concept of complementary observables is given by M. O. Scully, B.-G. Englert, and H. Walther, Nature (London) 351, 111 (1991)  
[2] According to J.-M. Lévy-Leblond, Physica (Amsterdam) 151B, 314 (1988), this useful noun, which avoids the usage of either "particle" or "wave," has been coined by M. Bunge.  
[3] W.K. Wootters and W.H. Zurek, Phys. Rev. D 19, 473 (1979).  
[4] D.M. Greenberger and A. Yasin, Phys. Lett. A 128, 391 (1988).  
[5] L. Mandel, Opt. Lett. 16, 1882 (1991). Mandel's "degree of intrinsic indistinguishability" equals  $\mathcal{V}_0 / \sqrt{1 - \mathcal{P}^2}$  in the present notation.  
[6] H. Rauch and J. Summhammer, Phys. Lett. 104A, 44 (1984); J. Summhammer, H. Rauch, and D. Tuppinger, Phys. Rev. A 36, 4447 (1987).  
[7] W. Heisenberg, Z. Phys. 43, 172 (1927); H. P. Robertson, Phys. Rev. 34, 163 (1929).  
[8] N. Bohr, in Albert Einstein: Philosopher-Scientist, edited by P.A. Schilpp (Library of Living Philosophers, Evanston, 1949), pp. 200–241.  
[9] B.-G. Englert, H. Walther, and M.O. Scully, Appl. Phys. B 54, 366 (1992).  
[10] B.-G. Englert, Acta Phys. Slov. 46, 249 (1996).