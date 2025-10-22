# Decoherence, correlation, and entanglement in a pair of coupled quantum dissipative oscillators

A. K. Rajagopal and R. W. Rendell  
Naval Research Laboratory, Washington, D.C. 20375-5320  
(Received 5 September 2000; published 18 January 2001)

A pair of coupled quantum dissipative oscillators, serving as a model for a nanosystem, is described here by the Lindblad equation. Its dynamic evolution is shown to exhibit the features of decoherence (spatial extent of quantum behavior), correlation (spatial scale over which the system localizes to its physical dimensions), and mixed-state entanglement (or inseparability, a special quantum feature in the case of pure states making its appearance first in bipartite systems) as a function of the coupling constants of the Lindblad equation. One interesting feature of this calculation is that the mixed-state separable entanglement may exhibit revivals in time. An initially inseparable entangled state need not remain so for all time and may exhibit regions of separable entanglement. Interpreting the parameters of the Lindblad theory as environmental features in certain experimental situations gives us clues as to the possible control of decoherence, correlation, and nature of entanglement.

DOI: 10.1103/PhysRevA.63.022116

PACS number(s): 03.65.Ud, 03.67.-a

# I. INTRODUCTION

A prototypical model of many physical systems is often a pair of coupled quantum dissipative oscillators. This model embodies the physical ideas of decoherence, correlation, entanglement, etc. associated with quantum systems. In particular, quantum entanglement (inseparability) shows up for the first time when we consider a two-oscillator system. This is the continuous variable version of the two-qubit system. The continuum version is of considerable interest both experimentally and theoretically. Only recently were its inseparability criteria worked out [1,2]. For systems in a mixed quantum state, described by a density matrix, the notion of entanglement is different (separable and inseparable) from the existence of pure entangled (inseparable) states that produce nonclassical phenomena. This is especially pertinent in discussing quantum nanometric systems here with an oscillatorlike model that are usually imbedded in other systems, so that a suitable description of the environmental effects may be described in terms of the parameters of such a model.

The purpose of this paper is to exhibit this model in general terms of a Gaussian density matrix containing all the above elements. The "ambiguity function" defined as the Fourier transform in the center-of-mass coordinate of the density matrix is found to lead to solutions of the suitably constructed Lindblad quantum dissipative oscillators. We use the solution so obtained in estimating the various physical features mentioned above. An important feature of the Lindblad theory is that we can obtain a mixed state from a pure state and vice versa. We restate this property finally, as a conclusion about possible control of decoherence and entanglement in nanometric systems, by varying the coupling constants appearing in the Lindblad equation [3].

We begin by giving a brief account of the density matrix and its two associated functions—the Wigner and ambiguity functions—and their salient properties. A quick survey of the Gaussian forms for these functions and the corresponding interpretations and significance of the coefficients in terms of the concepts of decoherence, correlation, entanglement, and uncertainty relation are also given. The Lindblad equation

for the density matrix of a pair of coupled dissipative oscillators is set up and solved using this parametrized Gaussian form. The implications of such analysis for possible practical nanometric systems are indicated.

The Lindblad theory [3] gives a formally exact quantum dynamical equation for the time-dependent density matrix, possessing desirable properties of preserving hermiticity, trace-class property (conservation of probability), and positivity of the underlying density matrix and including the possibility of passage from pure state to mixed state and vice versa. This formalism is most often used to describe the effects of environment on a system under investigation, and so the dissipative effects are considered to be due to the interaction of the system with its environment. The theory is, however, general enough for cases in which one may not be able to differentiate clearly between the system and the environment, as may happen in nanometric systems embedded in other similar nanosystems (or as in cosmological situations, which do not concern us here). The theory has recently been applied to study practical applications in condensed-matter physics and chemistry where one can clearly identify the system and its environment (often termed heat bath). Describing the dissipative mechanism in this manner gives the impression that one may be able to derive a Lindblad-type equation from such a starting point. This often entails approximations such as the Markoff scheme, in which there is no short time memory and weak interaction between the system and the environment. This procedure gives one an approximate measure of the interaction constants appearing in the Lindblad formulation. In this paper, we take the Lindblad parameters as phenomenological, and we postpone a separate investigation of their basic interpretation to a later communication. It may be mentioned that master-equation-type formalisms are often considered for describing dissipative effects, but they usually violate the basic principles by not preserving positivity or probability conservation or both. A general framework for dealing with a single dissipative harmonic oscillator in this theory was given by Isar et al. [4], from which they were able to derive several existing models of dissipation as special cases. In view of its importance and

due to the lack of methods to solve the Lindblad equation, an action principle was constructed recently [5] as a possible avenue for obtaining approximate solutions. For a discussion of some aspects of decoherence and dissipation using the Lindblad formalism, we may refer to several articles in the book by Giulini et al. [6], in particular the articles by Joos therein. The solution of the Lindblad equation for the density matrix of a single dissipative oscillator has been studied before using the Gaussian ansatz for the Wigner function and the density matrix [7,8]. These give rise to complicated coupled equations for the coefficients appearing in the Gaussian ansatz. We present here the solution for a two-oscillator system in terms of the Gaussian ansatz for the ambiguity function, which yields linear equations for the coefficients, which are then solved in a straightforward way. A similar analysis for the single-oscillator case has also been examined recently by us [9].

In the literature, we often find (a) theoretical proposals for future experiments [10-12] and (b) preliminary experiments [13-15] on simple coherent systems such as quantum dots, trapped ions, and nuclear spins using magnetic resonance to examine issues of decoherence, entanglement, and their control. There was also a recent experimental investigation of controlling the decoherence by coupling to engineered reservoirs [16]. This is done by laser fields, which can change the interaction between a trapped ion and the reservoir. In this paper, we discuss some of these in the same exploratory spirit. In view of the interpretation given for the Lindblad equation as a way of understanding the effects of a reservoir on a given system, the present paper is a contribution towards this understanding. It should be noted that decoherence arises from mutual interactions within the system as well as with reservoirs with which it may be in contact. In this paper, we study the latter aspect. Similarly, the quantum entanglement is in general an intrinsic quantum property of multiparticle systems and is not a feature of interaction. However, this property can be affected by interaction with a reservoir also. As will be demonstrated here, we exhibit this aspect by explicitly examining the reservoir effects both when the system is initially disentangled (separable) and when it is entangled (inseparable). It is in this sense that the effects of environment on decoherence and entanglement in the system are studied in this work.

In Sec. II, we give the general theoretical framework including the general Lindblad equation for the density matrix as well as the corresponding equation for the ambiguity function. In Sec. III, we introduce the Gaussian ambiguity function and the associated density matrix along with the derivation of physical quantities associated with correlation, decoherence, and entanglement. In Sec. IV, we describe the simplified model of an entangled Gaussian due to Simon [1], but in our language. In Sec. V, we construct a dynamical model based on a simplified form for the Lindblad equation given in Sec. II, and we present and interpret its solution in graphical form using the Gaussian ansatz. In Appendix A, we give the equations for the coefficients in the Gaussian ansatz for the two-oscillator system in the most general choice of the Lindblad equation. In Appendix B, we give the

explicit solution of these equations in a simplified model given in Sec. V.

# II. GENERAL THEORETICAL FRAMEWORK

For simplicity of presentation, we consider the pair of oscillators as a single, two-dimensional system. If  $x$  stands for the first system,  $A$ , and  $y$  for the second,  $B$ , we denote them together by a two-dimensional vector  $\vec{r} \equiv (x,y)$ . We define the time-dependent density matrix in the usual way:

$$
\langle \vec {r} | \rho (t) | \vec {r} ^ {\prime} \rangle = \langle \vec {r} ^ {\prime} | \rho (t) | \vec {r} \rangle^ {*} (\text {h e r m i t i c i t y}),
$$

$$
\operatorname {T r} \rho (t) = \int d ^ {2} \vec {r} \langle \vec {r} | \rho (t) | \vec {r} \rangle = 1 (\text {t r a c e c l a s s}), \tag {1}
$$

$$
\int \int d ^ {2} \vec {r} d ^ {2} \vec {r} ^ {\prime} \phi^ {*} (\vec {r}) \langle \vec {r} | \rho (t) | \vec {r} ^ {\prime} \rangle \phi (\vec {r} ^ {\prime}) \geqslant 0
$$

(positive semidefiniteness).

Here the asterisk stands for complex conjugate. We define the center of mass and relative coordinates,  $\vec{r} +\vec{r}^{\prime} = 2\vec{R}$ $\vec{r} -\vec{r}^{\prime} = \vec{\mathbf{r}}$  , and define the density matrix in the form

$$
\left\langle \vec {R} + \frac {1}{2} \vec {\mathbf {r}} \right| \rho (t) | \vec {R} - \frac {1}{2} \vec {\mathbf {r}} \rangle \equiv \rho (\vec {R}, \vec {\mathbf {r}}; t). \tag {2}
$$

Throughout, we use units where the Planck constant  $\hbar = 1$ . The "ambiguity function"  $A(\vec{Q},\vec{\mathbf{r}};t)$  is defined as the Fourier transform of the density matrix with respect to  $\vec{R}$ , and the "Wigner function"  $f(\vec{R},\vec{p};t)$  is defined as the Fourier transform with respect to  $\vec{\mathbf{r}}$ , as follows:

$$
\begin{array}{l} \rho (\vec {R}, \vec {\mathbf {r}}; t) = \int \frac {d ^ {2} \vec {Q}}{(2 \pi) ^ {2}} e ^ {- i \vec {Q} \cdot \vec {R}} A (\vec {Q}, \vec {\mathbf {r}}; t) \\ = \int \frac {d ^ {2} \vec {p}}{(2 \pi) ^ {2}} e ^ {- i \vec {p} \cdot \vec {\mathbf {r}}} f (\vec {R}, \vec {p}; t). \tag {3} \\ \end{array}
$$

The properties listed in Eq. (1) are reflected as the corresponding properties of the two functions defined above as follows:

$$
A ^ {*} (\vec {Q}, \vec {\mathbf {r}}; t) = A (- \vec {Q}, - \vec {\mathbf {r}}; t), \quad f ^ {*} (\vec {R}, \vec {p}; t) = f (\vec {R}, \vec {p}; t), \tag {3a}
$$

and the normalization condition

$$
A (\vec {Q} = 0, \vec {\mathbf {r}} = 0; t) = 1 = \int \int \frac {d ^ {2} \vec {R} d ^ {2} \vec {p}}{(2 \pi) ^ {2}} f (\vec {R}, \vec {p}; t). \tag {3b}
$$

Also

$$
f (\vec {R}, \vec {p}; t) = \int d ^ {2} \vec {\mathbf {r}} \int \frac {d ^ {2} \vec {Q}}{(2 \pi) ^ {2}} e ^ {- i \vec {Q} \cdot \vec {R}} e ^ {i \vec {p} \cdot \vec {\mathbf {r}}} A (\vec {Q}, \vec {\mathbf {r}}; t). \tag {3c}
$$

We first observe that there are ten independent covariances (correlations) among the variables of the two systems,

which can all be expressed in terms of the various derivatives of the ambiguity function. Here we express these ten covariances of interest that make up the basic uncertainty relations that characterize the system as follows:

$$
\begin{array}{l} \langle R _ {i} R _ {j} \rangle = \int \int \frac {d ^ {2} \vec {R} d ^ {2} \vec {p}}{(2 \pi) ^ {2}} R _ {i} R _ {j} f (\vec {R}, \vec {p}; t) \\ = - \frac {\partial^ {2}}{\partial Q _ {i} \partial Q _ {j}} A (\vec {Q}, \vec {\mathbf {r}}; t) \Bigg | _ {0}, \\ \end{array}
$$

$$
\langle p _ {i} p _ {j} \rangle = \int \int \frac {d ^ {2} \vec {R} d ^ {2} \vec {p}}{(2 \pi) ^ {2}} p _ {i} p _ {j} f (\vec {R}, \vec {p}; t) = - \left. \frac {\partial^ {2}}{\partial \mathbf {r} _ {i} \partial \mathbf {r} _ {j}} A (\vec {Q}, \vec {\mathbf {r}}; t) \right| _ {0}, \tag {4}
$$

$$
\langle R _ {i} p _ {j} \rangle = \int \int \frac {d ^ {2} \vec {R} d ^ {2} \vec {p}}{(2 \pi) ^ {2}} R _ {i} p _ {j} f (\vec {R}, \vec {p}; t) = \frac {\partial^ {2}}{\partial Q _ {i} \partial \mathbf {r} _ {j}} A (\vec {Q}, \vec {\mathbf {r}}; t) \Bigg | _ {0}.
$$

In the above,  $i,j$  go over the two system variables,  $x,y$ . Here all the derivatives of the function  $A(\vec{Q},\vec{\mathbf{r}};t)$  are evaluated at  $\vec{Q} = 0 = \vec{\mathbf{r}}$ .

The Lindblad equation for the density matrix of a dissipative quantum system is

$$
i \partial_ {t} \hat {\rho} = [ \hat {H}, \hat {\rho} ] - \frac {i}{2} \sum_ {m, n} h _ {n m} (\hat {L} _ {m} \hat {L} _ {n} \hat {\rho} + \hat {\rho} \hat {L} _ {m} \hat {L} _ {n} - 2 \hat {L} _ {n} \hat {\rho} \hat {L} _ {m}). \tag {5}
$$

Here  $\partial_t = \partial/\partial t$  is the time derivative operator. The first term on the right-hand side is the commutator of the Hamiltonian operator of the system  $\hat{H}$  representing the usual unitary Hamiltonian evolution, the second term is the nonunitary

evolution governed by a suitably chosen set of Hermitian Lindblad operators  $\{\hat{L}_n\}$ , and  $h_{nm}$  are  $c$ -number Hermitian matrix elements to be chosen appropriately to suit the physics of the problem at hand. These properties guarantee the hermiticity of the density matrix, and its positivity is assured if the  $c$ -number matrix is positive semidefinite. For simplicity of presentation, in this paper we choose the Hamiltonian to be that of two noninteracting effective oscillators representing the system under consideration:

$$
H = \frac {\omega_ {A}}{2} \left(\hat {p} _ {x} ^ {2} + \hat {x} ^ {2}\right) + \frac {\omega_ {B}}{2} \left(\hat {p} _ {y} ^ {2} + \hat {y} ^ {2}\right). \tag {6}
$$

The position and its conjugate momentum operators of each system obey the usual canonical commutation rules, and because the two systems are independent, the operators belonging to the separate systems commute between them. We choose the four Hermitian operators, the position and momentum operators for the two oscillators for the set of  $\{\hat{L}_n\}$  operators, and the 16  $c$ -number Hermitian coefficients are left unspecified to keep the development general. We also choose for simplicity of presentation the position and momentum variables in dimensionless form so that all the Lindblad parameters have dimensions of energy (recall that we use units with the usual Planck constant chosen to be unity). The time variable is similarly chosen to be dimensionless,  $\tau$ , by introducing an energy variable,  $\lambda$ . They may be chosen later to suit the specific problem at hand at a later stage. Thus,

$$
\hat {L} _ {1} = \hat {x}, \quad \hat {L} _ {2} = \hat {y}, \quad \hat {L} _ {3} = \hat {p} _ {x}, \quad \hat {L} _ {4} = \hat {p} _ {y}. \tag {7}
$$

And, we choose for the dissipative part the following most general form:

$$
\begin{array}{l} \sum_ {m, n} h _ {n m} (\hat {L} _ {m} \hat {L} _ {n} \hat {\rho} + \hat {\rho} \hat {L} _ {m} \hat {L} _ {n} - 2 \hat {L} _ {n} \hat {\rho} \hat {L} _ {m}) \equiv \sum_ {m, n} h _ {n m} (\hat {L} _ {m} \hat {L} _ {n} \hat {\rho} + \dots) \\ = h _ {1 1} \left(\hat {x} ^ {2} \hat {\rho} + \dots\right) + h _ {3 3} \left(\hat {p} _ {x} ^ {2} \hat {\rho} + \dots\right) + h _ {2 2} \left(\hat {y} ^ {2} \hat {\rho} + \dots\right) + h _ {4 4} \left(\hat {p} _ {y} ^ {2} \hat {\rho} + \dots\right) + h _ {1 2} \left(\hat {x} \hat {y} \hat {\rho} + \dots\right) \\ + h _ {1 2} ^ {*} (\hat {y} \hat {x} \hat {\rho} + \dots) + h _ {1 3} (\hat {x} \hat {p} _ {x} \hat {\rho} + \dots) + h _ {1 3} ^ {*} (\hat {p} _ {x} \hat {x} \hat {\rho} + \dots) + h _ {1 4} (\hat {x} \hat {p} _ {y} \hat {\rho} + \dots) \\ + h _ {1 4} ^ {*} (\hat {p} _ {y} \hat {x} \hat {\rho} + \dots) + h _ {2 3} (\hat {y} \hat {p} _ {x} \hat {\rho} + \dots) + h _ {2 3} ^ {*} (\hat {p} _ {x} \hat {y} \hat {\rho} + \dots) + h _ {2 4} (\hat {y} \hat {p} _ {y} \hat {\rho} + \dots) \\ + h _ {2 4} ^ {*} \left(\hat {p} _ {y} \hat {y} \hat {\rho} + \dots\right) + h _ {3 4} \left(\hat {p} _ {x} \hat {p} _ {y} \hat {\rho} + \dots\right) + h _ {3 4} ^ {*} \left(\hat {p} _ {y} \hat {p} _ {x} \hat {\rho} + \dots\right). \tag {8} \\ \end{array}
$$

Introducing the notations  $h_{ij} = h_{ij}^{(r)} + ih_{ij}^{(i)}$  for  $i \neq j$ , and for  $i = j$ $h_{ii}$  are real,  $\partial_x = \partial /\partial x$ , etc., the Lindblad equation in the coordinate representation is found to be (overdot denoting time derivative)

$$
\begin{array}{l} i \lambda \partial_ {\tau} \langle \vec {r} _ {1} | \hat {\rho} | \vec {r} _ {2} \rangle = \frac {1}{2} \{- \omega_ {A} (\partial_ {x _ {1}} ^ {2} - \partial_ {x _ {2}} ^ {2}) + \omega_ {A} (x _ {1} ^ {2} - x _ {2} ^ {2}) - \omega_ {B} (\partial_ {y _ {1}} ^ {2} - \partial_ {y _ {2}} ^ {2}) + \omega_ {B} (y _ {1} ^ {2} - y _ {2} ^ {2}) \} \langle \vec {r} _ {1} | \hat {\rho} | \vec {r} _ {2} \rangle - \frac {i}{2} \{h _ {1 1} (x _ {1} - x _ {2}) ^ {2} - h _ {3 3} (\partial_ {x _ {1}} + \partial_ {x _ {2}}) ^ {2} \\ + h _ {2 2} (y _ {1} - y _ {2}) ^ {2} - h _ {4 4} (\partial_ {y _ {1}} + \partial_ {y _ {2}}) ^ {2} + 2 h _ {1 2} ^ {(r)} (x _ {1} - x _ {2}) (y _ {1} - y _ {2}) + 2 i h _ {1 2} ^ {(i)} (x _ {1} y _ {2} - x _ {2} y _ {1}) - 2 i h _ {1 3} ^ {(r)} (x _ {1} - x _ {2}) (\partial_ {x _ {1}} + \partial_ {x _ {2}}) \\ - 2 h _ {1 3} ^ {(i)} (1 + x _ {2} \partial_ {x _ {1}} + x _ {1} \partial_ {x _ {2}}) - 2 i h _ {1 4} ^ {(r)} (x _ {1} - x _ {2}) (\partial_ {y _ {1}} + \partial_ {y _ {2}}) - 2 h _ {1 4} ^ {(i)} (x _ {2} \partial_ {y _ {1}} + x _ {1} \partial_ {y _ {2}}) - 2 i h _ {2 3} ^ {(r)} (y _ {1} - y _ {2}) (\partial_ {x _ {1}} + \partial_ {x _ {2}}) \\ - 2 h _ {2 3} ^ {(i)} \left(y _ {2} \partial_ {x _ {1}} + y _ {1} \partial_ {x _ {2}}\right) - 2 i h _ {2 4} ^ {(r)} \left(y _ {1} - y _ {2}\right) \left(\partial_ {y _ {1}} + \partial_ {y _ {2}}\right) - 2 h _ {2 4} ^ {(i)} \left(1 + y _ {2} \partial_ {y _ {1}} + y _ {1} \partial_ {y _ {2}}\right) - 2 h _ {3 4} ^ {(r)} \left(\partial_ {x _ {1}} + \partial_ {x _ {2}}\right) \left(\partial_ {y _ {1}} + \partial_ {y _ {2}}\right) \\ + 2 i h _ {3 4} ^ {(i)} \left(\partial_ {x _ {1}} \partial_ {y _ {2}} - \partial_ {y _ {1}} \partial_ {x _ {2}}\right) \} \langle \vec {r} _ {1} | \hat {\rho} | \vec {r} _ {2} \rangle . \tag {9} \\ \end{array}
$$

In terms of the center of mass and relative coordinates introduced in Eq. (2), we derive the equation obeyed by the ambiguity function:

$$
\begin{array}{l} \lambda \partial_ {\tau} A (\vec {Q}, \vec {\mathbf {r}}) = \{\omega_ {A} (- \mathbf {r} _ {1} \partial_ {Q _ {1}} + Q _ {1} \partial_ {r _ {1}}) + \omega (- \mathbf {r} _ {2} \partial_ {Q _ {2}} + Q _ {2} \partial_ {r _ {2}}) \} A (\vec {Q}, \vec {\mathbf {r}}) - \frac {1}{2} \{h _ {1 1} \mathbf {r} _ {1} ^ {2} + h _ {3 3} Q _ {1} ^ {2} + h _ {2 2} \mathbf {r} _ {2} ^ {2} + h _ {4 4} Q _ {2} ^ {2} + 2 h _ {1 2} ^ {(r)} \mathbf {r} _ {1} \mathbf {r} _ {2} \\ + 2 h _ {1 2} ^ {(i)} (\mathbf {r} _ {1} \partial_ {Q _ {2}} - \mathbf {r} _ {2} \partial_ {Q _ {1}}) - 2 h _ {1 3} ^ {(r)} \mathbf {r} _ {1} Q _ {1} + 2 h _ {1 3} ^ {(i)} (Q _ {1} \partial_ {Q _ {1}} + \mathbf {r} _ {1} \partial_ {\mathbf {r} _ {1}}) - 2 h _ {1 4} ^ {(r)} \mathbf {r} _ {1} Q _ {2} + 2 h _ {1 4} ^ {(i)} (Q _ {2} \partial_ {Q _ {1}} + \mathbf {r} _ {1} \partial_ {\mathbf {r} _ {2}}) - 2 h _ {2 3} ^ {(r)} \mathbf {r} _ {2} Q _ {1} \\ - 2 h _ {2 3} ^ {(i)} \left(\mathbf {r} _ {2} \partial_ {\mathbf {r} _ {1}} - Q _ {1} \partial_ {Q _ {2}}\right) - 2 h _ {2 4} ^ {(r)} \mathbf {r} _ {2} Q _ {2} + 2 h _ {2 4} ^ {(i)} \left(Q _ {2} \partial_ {Q _ {2}} + \mathbf {r} _ {2} \partial_ {\mathbf {r} _ {2}}\right) + 2 h _ {3 4} ^ {(r)} Q _ {1} Q _ {2} + 2 h _ {3 4} ^ {(i)} \left(Q _ {2} \partial_ {\mathbf {r} _ {1}} - Q _ {1} \partial_ {\mathbf {r} _ {2}}\right) \} A (\vec {Q}, \vec {\mathbf {r}}). \tag {10} \\ \end{array}
$$

In the next section, we examine the Gaussian structure of the ambiguity function and give in detail the various physical implications of such a function.

# III. AMBIGUITY FUNCTION, DENSITY MATRIX, AND THEIR SIGNIFICANCE

The most general Gaussian form for the density matrix is defined by choosing  $A(\vec{Q},\vec{\mathbf{r}};t)$  in the following form with time-dependent coefficients (all dimensionless in our notation) with zero mean values  $\vec{R}$  and  $\vec{p}$ :

$$
\begin{array}{l} A (\vec {Q}, \vec {\mathbf {r}}; t) = \exp - \frac {1}{2} \left[ \mathbf {r} _ {i} A _ {i j} (t) \mathbf {r} _ {j} + \mathbf {r} _ {i} B _ {i j} (t) Q _ {j} \right. \\ + Q _ {i} B _ {j i} (t) \mathbf {r} _ {j} + Q _ {i} C _ {i j} (t) Q _ {j} ] \\ = \exp - \frac {1}{2} \left\{\left(\mathbf {r} ^ {T} Q ^ {T}\right) \left( \begin{array}{l l} \underline {{A}} & \underline {{B}} \\ \underline {{B}} ^ {T} & C \end{array} \right) \left( \begin{array}{l} \mathbf {r} \\ Q \end{array} \right) \right\}. \tag {11} \\ \end{array}
$$

Here  $i, j$  run from 1 to 2, and we use the convention that the repeated indices are summed. The second expression in the above is in terms of a convenient partitioned matrix notation, and the superscript  $T$  stands for transposition. In this section, we suppress the time dependence, but in the next section, when we consider the solution of the Lindblad equation, we exhibit this explicitly.

From Eqs. (4) and (11), we obtain

$$
\left\langle R _ {i} R _ {j} \right\rangle = C _ {i j}, \quad \left\langle p _ {i} p _ {j} \right\rangle = A _ {i j}, \quad \left\langle R _ {i} p _ {j} \right\rangle = B _ {j i}, \tag {12}
$$

and condition (3a) imposes the following requirements on the coefficients in Eq. (11), which are seen to be satisfied by virtue of the above identification while condition (3b) is fulfilled by construction:

$A_{ij}, C_{ij}$  are real, symmetric and  $B_{ij} (\neq B_{ji})$  is real. (13)

$A_{ii}, C_{ii} > 0$ ,  $\operatorname{sgn}(B_{ii})$  nonspecific.

Introducing the matrix notation for the vector denoted now as a column vector and the coefficients  $A, B, C$  as matrices, Eq. (11) may be expressed in a compact form:

$$
\begin{array}{l} A (\vec {Q}, \vec {\mathbf {r}}; t) = \exp - \frac {1}{2} [ \vec {\mathbf {r}} ^ {T} A (t) \vec {\mathbf {r}} + \vec {\mathbf {r}} ^ {T} \underline {{B}} (t) \vec {Q} \\ + \vec {Q} ^ {T} \underline {{B}} ^ {T} \vec {\mathbf {r}} + \vec {Q} ^ {T} \underline {{C}} (t) \vec {Q} ]. \tag {14} \\ \end{array}
$$

Then we deduce the density matrix from Eq. (3):

$$
\begin{array}{l} \rho (\vec {R}, \vec {r}) = \frac {1}{2 \pi \sqrt {\det  (C)}} \\ \times \exp - \frac {1}{2} \left\{(\vec {R} ^ {T}, \vec {\mathbf {r}} ^ {T}) \left( \begin{array}{c c} \underline {{C}} ^ {- 1} & - i \underline {{E}} \\ - i \underline {{E}} ^ {T} & \underline {{\alpha}} \end{array} \right) \left( \begin{array}{l} \vec {R} \\ \vec {\mathbf {r}} \end{array} \right) \right\}, \tag {15} \\ \end{array}
$$

where  $\underline{E} = \underline{C}^{-1}\underline{B}^T$  and  $\underline{\alpha}\equiv \underline{A} -\underline{D} = \underline{A} -\underline{B}\underline{C}^{-1}\underline{B}^{T}$  .Here

$$
\underline {{C}} ^ {- 1} = (\det  \underline {{C}}) ^ {- 1} \left( \begin{array}{c c} C _ {2 2} & - C _ {1 2} \\ - C _ {1 2} & C _ {1 1} \end{array} \right), \quad \underline {{B}} ^ {T} = \left( \begin{array}{l l} B _ {1 1} & B _ {2 1} \\ B _ {1 2} & B _ {2 2} \end{array} \right). \tag {16}
$$

It is to be noted that the matrix  $D$  is symmetric upon explicit calculation.

The Wigner function is found to be

$$
\begin{array}{l} f _ {w} (\vec {R}, \vec {p}) = \frac {1}{\sqrt {\det  (C)} \sqrt {\det  (\underline {{\alpha}})}} \exp \left\{- \frac {1}{2} \left[ (\vec {R} ^ {T}, \vec {p} ^ {T}) \right. \right. \\ \left. \times \left( \begin{array}{c c} \underline {{E}} \underline {{\alpha}} ^ {- 1} \underline {{A}} \underline {{B}} ^ {T ^ {- 1}} & - \underline {{E}} \underline {{\alpha}} ^ {- 1} \\ - \underline {{\alpha}} ^ {- 1} \underline {{E}} ^ {T} & \underline {{\alpha}} ^ {- 1} \end{array} \right) \left( \begin{array}{l} \vec {R} \\ \vec {p} \end{array} \right) \right] \}. \tag {17} \\ \end{array}
$$

The reduced density matrices for the two subsystems separately are obtained by the trace operation. We thus obtain the marginal density matrix of system  $A$ :

$$
\begin{array}{l} \rho_ {1} \left(R _ {t}, \mathbf {r} _ {1}; t\right) = \left(2 \pi C _ {1 1}\right) ^ {- 1 / 2} \times \exp \left[ - \left(2 C _ {1 1}\right) ^ {- 1} \right. \\ \times \left(R _ {1} ^ {2} - 2 i B _ {1 1} R _ {1} \mathbf {r} _ {1} + \left(A _ {1 1} C _ {1 1} - B _ {1 1} ^ {2}\right) \mathbf {r} _ {1} ^ {2}\right) ]. \tag {18} \\ \end{array}
$$

A similar calculation shows the reduced density matrix of the second system to be

$$
\begin{array}{l} \rho_ {2} \left(R _ {2}, \mathbf {r} _ {2}; t\right) = \left(2 \pi C _ {2 2}\right) ^ {- 1 / 2} \times \exp \left[ - \left(2 C _ {2 2}\right) ^ {- 1} \right. \\ \times \left(R _ {2} ^ {2} - 2 i B _ {2 2} R _ {2} \mathbf {r} _ {2} + \left(A _ {2 2} C _ {2 2} - B _ {2 2} ^ {2}\right) \mathbf {r} _ {2} ^ {2}\right) ]. \tag {19} \\ \end{array}
$$

It is worth pointing out that these marginal density matrices of the subsystems do not contain remnants from the original two-system density matrix. This aspect becomes even more transparent in subsequent discussion of the uncertainty principle obeyed by the respective correlations of positions and their conjugate momenta.

Following the discussion given by us for the single dissipative oscillator system [9], we deduce the length scales of correlation and decoherence in the subsystems. The correlation length defines the physical extent of the system, which is therefore given by the spatial decay of the diagonal element of the density matrix in coordinate space. This is obtained by setting  $x = 0$  in Eqs. (18) and (19). On the other hand, the decoherence length is defined as the spatial decay of the off-diagonal part of the density matrix in coordinate space. This is obtained by setting  $R = 0$  in Eqs. (18) and (19). This is a measure of the persistence of quantum behavior on a spatial scale. Thus,

$$
\left\langle x ^ {2} \right\rangle_ {A} = C _ {1 1} = d _ {A} ^ {2} (\operatorname {c o r r .}),
$$

$$
\Omega_ {A} ^ {2} = \left(A _ {1 1} C _ {1 1} - B _ {1 1} ^ {2}\right) = \frac {(1 + \xi_ {A})}{4 (1 - \xi_ {A})} \geqslant 1 / 4, \tag {20a}
$$

$$
d _ {A} ^ {2} (\operatorname {d e c o h .}) = \left\langle x ^ {2} \right\rangle_ {A} / 2 \Omega_ {A} ^ {2},
$$

and

$$
\left\langle y ^ {2} \right\rangle_ {B} = C _ {2 2} = d _ {B} ^ {2} (\operatorname {c o r r .}),
$$

$$
\Omega_ {B} ^ {2} = \left(A _ {2 2} C _ {2 2} - B _ {2 2} ^ {2}\right) = \frac {(1 + \xi_ {B})}{4 (1 - \xi_ {B})} \geqslant 1 / 4, \tag {20b}
$$

$$
d _ {B} ^ {2} (\operatorname {d e c o h .}) = \left\langle y ^ {2} \right\rangle_ {B} / 2 \Omega_ {B} ^ {2}.
$$

$\xi_{A,B}$  are the mixed-state parameters of the two single oscillator systems. We now employ a parametrization of a bipartite Gaussian given by Simon [1] and construct the associated ambiguity function and the density matrix of the system.

The equations obeyed by  $A_{ij}$ ,  $B_{ij}$ , and  $C_{ij}$  in Eq. (11) when substituted in Eq. (10) are given in Appendix A. We observe that all these coefficients are coupled, implying that correlation, decoherence, and entanglement are all dynamically coupled and influence each other. In Sec. V, we introduce a simplified model to illustrate the main features of these couplings by means of numerical analysis of the solutions.

# IV. A SIMPLE MODEL BASED ON SIMON'S WORK

We now consider a canonical parametrization of the two-variable Gaussian density matrix derived from Simon's [1] work, which has all the features of entanglement, decoher

ence, etc. It consists in the following choice of the correlations:

$$
\begin{array}{l} \langle x ^ {2} \rangle = a _ {1}, \quad \langle p _ {x} ^ {2} \rangle = b _ {1}, \quad \langle y ^ {2} \rangle = a _ {2}, \quad \langle p _ {y} ^ {2} \rangle = b _ {2}, \tag {21} \\ \langle x y \rangle = a _ {1 2}, \quad \langle p _ {x} p _ {y} \rangle = b _ {1 2}. \\ \end{array}
$$

All others are zero.

Some basic inequalities are obeyed by these quantities following from the Schwarz and Heisenberg inequalities:

$$
a _ {1} a _ {2} - a _ {1 2} ^ {2} \equiv K _ {A} \geqslant 0, \quad b _ {1} b _ {2} - b _ {1 2} ^ {2} \equiv K _ {B} \geqslant 0, \quad \text {S c h w a r z}, \tag {22}
$$

$$
a _ {1} b _ {1} \equiv \Omega_ {A} ^ {2} \geqslant \frac {1}{4}, \quad a _ {2} b _ {2} \equiv \Omega_ {B} ^ {2} \geqslant \frac {1}{4}, \quad \text {H e i s e n b e r g .} \tag {23}
$$

The above are for the individual oscillator systems. The bipartite Heisenberg inequality and the condition for separable entanglement derived from Simon's work read as

$$
a _ {1 2} b _ {1 2} \leqslant 2 K _ {A} K _ {B} - \frac {1}{8}, \quad \text {H e i s e n b e r g}, \tag {24a}
$$

$$
\left| a _ {1 2} b _ {1 2} \right| \leqslant 2 K _ {A} K _ {B} - \frac {1}{8}, \quad \text {e n t a n g l e m e n t / s e p a r a b i l i t y}. \tag {24b}
$$

Without giving the details, it is straightforward to verify the following expression for the density matrix associated with the Simon model specified by Eq. (21):

$$
\begin{array}{l} \left\langle \vec {R} + \frac {1}{2} \vec {r} \right| \rho_ {S} \left| \vec {R} - \frac {1}{2} \vec {r} \right\rangle \\ = \frac {1}{2 \pi \left(K _ {A}\right) ^ {1 / 2}} \exp \{- \frac {1}{2} \left[ \left(x ^ {2} b _ {1} + 2 x y b _ {1 2} + y ^ {2} b _ {2}\right) \right. \\ \left. + K _ {A} ^ {- 1} \left(X ^ {2} a _ {2} - 2 X Y a _ {1 2} + Y ^ {2} a _ {1}\right) \right] \}. \tag {25} \\ \end{array}
$$

Here  $x = (x_{1} - x_{2})$ ,  $y = (y_{1} - y_{2})$ ,  $X = \frac{1}{2}(x_{1} + x_{2})$ , and  $Y = \frac{1}{2}(y_{1} + y_{2})$ .

From this we have the reduced density matrices of  $A$  and  $B$  subsystems, which are found to be both mixed-state density matrices:

$$
\begin{array}{l} \langle x _ {1} | \rho_ {S, A} | x _ {2} \rangle = \frac {1}{(2 \pi a _ {1}) ^ {1 / 2}} \exp \left\{- \frac {1}{2} \left[ \left(b _ {1} + \frac {1}{4 a _ {1}}\right) x _ {1} ^ {2} \right. \right. \\ \left. \left. + \left(b _ {1} + \frac {1}{4 a _ {1}}\right) x _ {2} ^ {2} - 2 x _ {1} x _ {2} \left(b _ {1} - \frac {1}{4 a _ {1}}\right) \right] \right\}, \tag {26} \\ \end{array}
$$

$$
\begin{array}{l} \langle y _ {1} | \rho_ {S, B} | y _ {2} \rangle = \frac {1}{(2 \pi b _ {2}) ^ {1 / 2}} \exp \left\{- \frac {1}{2} \left[ \left(b _ {2} + \frac {1}{4 a _ {2}}\right) y _ {1} ^ {2} \right. \right. \\ \left. \left. + \left(b _ {2} + \frac {1}{4 a _ {2}}\right) y _ {2} ^ {2} - 2 y _ {1} y _ {2} \left(b _ {2} - \frac {1}{4 a _ {2}}\right) \right] \right\}. \tag {27} \\ \end{array}
$$

The expressions for Eqs. (26) and (27) with  $x_{1} = x_{2}$  and  $y_{1} = y_{2}$ , respectively, lead to the identification of correlation

lengths while those with  $x_{1} = -x_{2}$  and  $y_{1} = -y_{2}$ , respectively, lead to the identification of decoherence lengths in the subsystems:

$$
d _ {S, A} ^ {2} (\operatorname {c o r r .}) = a _ {1}, \quad d _ {S, A} ^ {2} (\operatorname {d e c o h .}) = 1 / 4 b _ {1},
$$

$$
(2 8) \tag {28}
$$

$$
d _ {S, B} ^ {2} (\operatorname {c o r r .}) = a _ {2}, \quad d _ {S, B} ^ {2} (\operatorname {d e c o h .}) = 1 / 4 b _ {2}.
$$

The mixed-state lengths in these subsystems are identified to be the coefficients of the products  $x_{1}x_{2}$  and  $y_{1}y_{2}$ , respectively, in Eqs. (26) and (27):

$$
d _ {S, A} ^ {2} (\operatorname {m i x}) = 4 a _ {1} / \left(4 \Omega_ {A} ^ {2} - 1\right), \quad d _ {S, B} ^ {2} (\operatorname {m i x}) = 4 a _ {2} / \left(4 \Omega_ {B} ^ {2} - 1\right). \tag {29}
$$

Similar analysis of the composite system density matrix given by Eq. (25) leads to correlation and decoherence lengths:

$$
\begin{array}{l} d _ {S, A B} ^ {2} (A - \operatorname {c o r r .}) = K _ {A} / a _ {2} = d _ {S, A} ^ {2} (\operatorname {c o r r .}) - a _ {1 2} ^ {2} / a _ {2}, \\ d _ {S, A B} ^ {2} (A - \operatorname {d e c o h .}) = 1 / 4 b _ {1} = d _ {A} ^ {2} (\operatorname {d e c o h .}), \\ \end{array}
$$

(30)

$$
d _ {S, A B} ^ {2} (B - \text {c o r r .}) = K _ {A} / a _ {1} = d _ {S, B} ^ {2} (\text {c o r r .}) - a _ {1 2} ^ {2} / a _ {1},
$$

$$
d _ {S, A B} ^ {2} (B - \operatorname {d e c o h .}) = 1 / 4 b _ {2} = d _ {B} ^ {2} (\operatorname {d e c o h .}).
$$

The coefficients of the products  $xy$  and  $XY$  in Eq. (25) indicate the entanglement features in the composite system, which we define here as entanglement lengths:

$$
E _ {S, A B} ^ {2} = 1 / b _ {1 2} \quad \text {a n d} \quad \widetilde {E} _ {S, A B} ^ {2} = K _ {A} / a _ {1 2}. \tag {31}
$$

Equation (24) representing the Heisenberg inequality for the bipartite system may be written then in the form

$$
E _ {S, A B} ^ {- 2} \widetilde {E} _ {S, A B} ^ {- 2} \leqslant \left(\frac {1}{4 K _ {A}} + 2 K _ {B}\right). \tag {32}
$$

In the next section, we develop a model of the two-oscillator system based on the above-simplified parametrization of the Simon model as the given input at initial time in solving the Lindbad equation. This will exhibit how the Lindblad parameters can influence the entanglement features of the bipartite system.

# V. A DYNAMICAL MODEL—SOLUTION OF THE LINDBLAD EQUATION

The dynamical model described here serves to illustrate how the solution of the Lindblad equation exhibits time evolution in the initially specified correlation functions given by the Simon model. This model indicates how one may control the parameters specifying the decoherence and entanglement by a suitable choice of the interactions introduced in the Lindblad equation. In the general equations (A1)-(A10), we define our model by keeping only the following Lindblad interaction constants and all others are set equal to zero:

$h_{ii}$ $i = 1,2,3,4$  real part of  $h_{12}$  and both real

$$
\text {a n d i m a r g i n a r y p a r t s o f} h _ {1 3}, h _ {2 4}. \tag {33}
$$

The  $h_{ii}$ 's and the real parts of  $h_{13}, h_{24}$  serve as driving forces in the two systems, whereas the imaginary parts of  $h_{13}, h_{24}$  give rise to damping of the two oscillators. And  $h_{12}^{(r)}$  serves as the driving force for the entanglement in the system. This choice of the Lindblad parameters simplifies the coupled equations in Eq. (12) in such a way that the two oscillators  $A$  and  $B$  are not coupled to each other but are governed by their own individual parameters. Thus their individual decoherence and correlation features are preserved even in this simple model. Also, the entanglement features appear here as four coupled equations for the cross-correlation functions with their own friction forces. The following set of coupled, linear equations describes this simplified model:

$$
\lambda \partial_ {\tau} A _ {1 1} = - 2 \omega_ {A} B _ {1 1} - 2 h _ {1 3} ^ {(i)} A _ {1 1} + h _ {1 1},
$$

$$
\lambda \partial_ {\tau} B _ {1 1} = \omega_ {A} A _ {1 1} - \omega_ {A} C _ {1 1} - 2 h _ {1 3} ^ {(i)} B _ {1 1} - h _ {1 3} ^ {(r)}, \tag {34}
$$

$$
\lambda \partial_ {\tau} C _ {1 1} = 2 \omega_ {A} B _ {1 1} - 2 h _ {1 3} ^ {(i)} C _ {1 1} + h _ {3 3};
$$

$$
\lambda \partial_ {\tau} A _ {2 2} = - 2 \omega_ {B} B _ {2 2} - 2 h _ {2 4} ^ {(i)} A _ {2 2} + h _ {2 2},
$$

$$
\lambda \partial_ {\tau} B _ {2 2} = \omega_ {B} A _ {2 2} - \omega_ {B} C _ {2 2} - 2 h _ {2 4} ^ {(i)} B _ {2 2} - h _ {2 4} ^ {(r)}, \tag {35}
$$

$$
\lambda \partial_ {\tau} C _ {2 2} = 2 \omega_ {B} B _ {2 2} - 2 h _ {2 4} ^ {(i)} C _ {2 2} + h _ {4 4};
$$

$$
\lambda \partial_ {\tau} A _ {1 2} = - \omega_ {A} B _ {2 1} - \omega_ {B} B _ {1 2} - (h _ {1 3} ^ {(i)} + h _ {2 4} ^ {(i)}) A _ {1 2} + h _ {1 2} ^ {(r)},
$$

$$
\lambda \partial_ {\tau} B _ {1 2} = \omega_ {B} A _ {1 2} - \omega_ {A} C _ {1 2} - \left(h _ {1 3} ^ {(i)} + h _ {2 4} ^ {(i)}\right) B _ {1 2},
$$

(36)

$$
\lambda \partial_ {\tau} B _ {2 1} = \omega_ {A} A _ {1 2} - \omega_ {B} C _ {1 2} - \left(h _ {1 3} ^ {(i)} + h _ {2 4} ^ {(i)}\right) B _ {2 1},
$$

$$
\lambda \partial_ {\tau} C _ {1 2} = \omega_ {A} B _ {1 2} + \omega_ {B} B _ {2 1} - \left(h _ {1 3} ^ {(i)} + h _ {2 4} ^ {(i)}\right) C _ {1 2}.
$$

Equations (34) and (35) are the respective equations for the oscillators  $A$  and  $B$ , respectively, and are the same as those solved in the RWR-AKR [9] paper for a single dissipative oscillator. Equations (36), on the other hand, are the equations coupling the two oscillators, representing entanglement. These being coupled first-order differential equations in time, we specify the initial conditions as in the Simon model:

$$
A _ {1 1} (\tau = 0) = b _ {1}, \quad B _ {1 1} (\tau = 0) = 0, \quad C _ {1 1} (\tau = 0) = a _ {1},
$$

$$
A _ {2 2} (\tau = 0) = b _ {2}, \quad B _ {2 2} (\tau = 0) = 0, \quad C _ {2 2} (\tau = 0) = a _ {2},
$$

$$
A _ {1 2} (\tau = 0) = b _ {1 2}, \quad B _ {1 2} (\tau = 0) = 0, \quad B _ {2 1} (\tau = 0) = 0, \tag {37}
$$

$$
C _ {1 2} (\tau = 0) = a _ {1 2}.
$$

These equations are solved by the method of Laplace transformation incorporating the initial conditions given by Eqs. (37). The time dependences of the coefficients  $A_{12},B_{12}$  given by Eqs. (36) are of interest to us as they represent the evo

lution of entanglement of the two oscillators. In Appendix B, we give the exact analytical solutions of these equations. The numerical display of these results will be described presently. We should remark here that this simple model does not compromise the general features of the system, as will be evident from the foregoing discussion.

It may be worth noting that the above initial conditions and their time evolutions governed by Eqs. (34)-(36) may be expressed neatly as the evolution of the covariance matrices as follows:

$$
A _ {S} (\tau = 0) = \left(\begin{array}{c c}a _ {1}&0\\0&b _ {1}\end{array}\right)\rightarrow A _ {S} (\tau) = \left(\begin{array}{c c}C _ {1 1}&B _ {1 1}\\B _ {1 1}&A _ {1 1}\end{array}\right), \tag {38}
$$

$$
B _ {S} (\tau = 0) = \left(\begin{array}{c c}a _ {2}&0\\0&b _ {2}\end{array}\right)\rightarrow B _ {S} (\tau) = \left(\begin{array}{c c}C _ {2 2}&B _ {2 2}\\B _ {2 2}&A _ {2 2}\end{array}\right), \tag {39}
$$

$$
C _ {S} (\tau = 0) = \left(\begin{array}{c c}a _ {1 2}&0\\0&b _ {1 2}\end{array}\right)\rightarrow C _ {S} (\tau) = \left(\begin{array}{c c}C _ {1 2}&B _ {1 2}\\B _ {2 1}&A _ {1 2}\end{array}\right). \tag {40}
$$

From Appendix B, we note how these evolutions come about explicitly.

In this form, the Simon inequalities given in Eqs. (24a) and (24b) are now written in the form

$$
\begin{array}{l} (\det A _ {S}) (\det B _ {S}) + \left(\frac {1}{4} - \det C _ {S}\right) ^ {2} - \operatorname {t r} \left(A _ {S} J C _ {S} J B _ {S} J C _ {S} ^ {T} J\right) \\ \geqslant \frac {1}{4} (\det A _ {S} + \det B _ {S}), \quad \text {H e i s e n b e r g}, \tag {41a} \\ \end{array}
$$

$$
\begin{array}{l} \left(\det A _ {S}\right) \left(\det B _ {S}\right) + \left(\frac {1}{4} - \det C _ {S}\right) ^ {2} - \operatorname {t r} \left(A _ {S} J C _ {S} J B _ {S} J C _ {S} ^ {T} J\right) \\ \geqslant \frac {1}{4} (\det A _ {S} + \det B _ {S}), \quad \text {e n t a n g l e m e n t / s e p a r a b i l i t y}. \tag {41b} \\ \end{array}
$$

Here  $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$  and  $C_S^T$  is the transposed matrix of  $C_S$ . The Schwarz and Heisenberg inequalities for the  $A$  and  $B$  systems are

$$
\begin{array}{l} C _ {1 1} C _ {2 2} - C _ {1 2} ^ {2} \equiv K _ {A} \geqslant 0, \quad A _ {1 1} A _ {2 2} - A _ {1 2} ^ {2} \equiv K _ {B} \geqslant 0, \quad \text {S c h w a r z}, (42) \\ \det  A _ {S} \equiv \Omega_ {A} ^ {2} = A _ {1 1} C _ {1 1} - B _ {1 1} ^ {2} \geqslant \frac {1}{4}, \\ \det  B _ {S} \equiv \Omega_ {B} ^ {2} = A _ {2 2} C _ {2 2} - B _ {2 2} ^ {2} \geqslant \frac {1}{4}, \quad \text {H e i s e n b e r g .} (43) \\ \end{array}
$$

As is pointed out by Simon [1], it is sufficient to examine the sign of the  $\operatorname{det} C_S$  to determine whether one has separable entanglement (if the sign is negative) or not (if the sign is zero or positive). In the numerical work presented here for the simplified model worked out in Appendix B, we deduce analytically an important result for asymptotically large times. In fact, we have

$$
\begin{array}{l} \det C _ {S} (\tau = \infty) = \left(\frac {h _ {1 2} ^ {(r)}}{\omega_ {A} [ \Gamma^ {2} + (1 + r) ^ {2} ] [ \Gamma^ {2} + (1 - r) ^ {2} ]}\right) ^ {2} \\ \times \left\{\left(r - 1\right) \Gamma^ {4} + \Gamma^ {2} \left(r ^ {3} - r ^ {2} + 2 r - 2\right) \right. \\ - (r ^ {2} - r + 1) \}. \tag {44} \\ \end{array}
$$

This result, it should be noted, is independent of the initial conditions. For finite times, however, a more complicated calculation needs to be made, which will be presented graphically in this paper. Corresponding to the graphical presentations, we give here the results for two typical cases.

Case (i):  $r = 1$  (equivalent oscillators). We find from Eq. (44)

$$
\det C _ {S} (\tau = \infty) <   0. \tag {45a}
$$

Case (ii):  $r \neq 1$  (inequivalent oscillators). In this case, depending on the values of  $r$  and  $\Gamma$ , we may have

$$
\det  C _ {S} (\tau = \infty) > 0 \quad \text {a n d} \quad \det  C _ {S} (\tau = \infty) <   0. \tag {45b}
$$

These results show that irrespective of the initial conditions, for a suitable choice of Lindblad parameters we can get a separable entangled or an inseparable entangled state.

We now present detailed calculations of the time evolution of decoherence and entanglement with given initial conditions. We choose  $\lambda = \omega_{A}$  and use position and momentum variables in dimensionless form so that all Lindblad parameters have dimensions of energy and the dimensionless time variables is  $\tau = \omega_{A}t$ . The choice of the parameters for the initial conditions must be consistent with Eqs. (22), (23), (24a) and (24b). We choose here two special choices for purposes of illustration with minimum uncertainty values  $a_1 = b_1 = \frac{1}{2}$ ,  $a_2 = b_2 = \frac{1}{2}$ : (a) Initially separable entangled state with  $a_{12} = 0 = b_{12}$ , (b) initially inseparable entangled state with  $a_{12} = \frac{1}{2} = -b_{12}$ . From Eqs. (45a) and (45b), we deduce that one may get a separable entangled or an inseparable entangled state in both of these situations for a suitable choice of the Lindblad parameters, which are chosen to preserve the positive signs of the mean-square displacements and momenta of the two oscillators. We focus on the case of inequivalent oscillators by choosing their frequencies to be different (the frequency of oscillator  $B$  is chosen here to be three times faster than that of  $A$ ) but all other parameters were chosen to be the same for convenient presentation of the results. Their values are given in the caption of Fig. 1, and are kept the same in calculating all other system characteristics.

In Fig. 1, we display the mean-square momentum of the two subsystems as a function of the dimensionless time  $\tau$ . Since we assumed the two oscillators to be in their minimum uncertainty states, they both begin at the same value (0.5) initially and evolve according to the solution given in Appendix B, Eq. (B3), and its counterpart. They approach their respective asymptotes for large times, the  $B$  oscillator approaching it much earlier than the  $A$ . This is due to the fact that the decay constants are chosen to be the same for both the systems.

In Fig. 2, we present the subsystem decoherence lengths defined by Eqs. (20a) and (20b) and the solutions given in Appendix B. It is interesting to note that as in the case of momenta in Fig. 1, the decoherence length crosses the  $A$

![](images/e703412789b8846a2f64359749ff65e66e52a6f6531ddefb01715af620fc5b5e.jpg)  
FIG. 1. Subsystem mean-square momentum  $\langle p_x^2\rangle$  for oscillator  $A$  and  $\langle p_y^2\rangle$  for oscillator  $B$  in dimensionless units, using the solutions in Appendix B with  $\lambda = \omega_{A}$  and  $\Gamma_{A} = \Gamma_{B} = 0.25$ ,  $r = \omega_{B} / \omega_{A} = 3$ ,  $h_{11} = h_{33} = h_{13}^{(r)} = 1$ ,  $h_{22} = 2$ ,  $h_{44} = 4$ , and  $a_1 = b_1 = a_2 = b_2 = 0.5$ .

system value for times of about 0.6, and approach their asymptotic values for large times (for times larger than 5 in this figure). This is because the decoherence length is a ratio of similarly decaying quantities.

Figure 3 represents the oscillator pair correlations involving positions and momenta of the two systems. These are important in determining the dynamic evolution of entanglement. In Fig. 3(a), the initial values for these are chosen to be zero, which corresponds to case (a) above when the system is initially separable entangled. Figure 3(b), on the other hand, is for the case when they are initially inseparable entangled. They both oscillate in approximately opposite phase, the second case exhibiting more oscillations than the first. They change their signs a few times before reaching, albeit slowly, their respective asymptotic values.

Finally, Fig. 4 displays the time evolution of the determinant constructed from the solutions given by Eqs. (B4)-(B7) of Appendix B. This is a signature of 'entanglement' of the systems  $A$  and  $B$ . The curve (a) is for the initially inseparable

![](images/74765dd22667fc3b02a19793ec4ad687b175559f46e0cab6d101d186e27651b7.jpg)  
FIG. 2. Subsystem decoherence lengths with the same parameters as in Fig. 1.

![](images/1fa53346db8d94ad0ef066fd38108a01364bdf2c8ae663561fa68bc32d32400c.jpg)

![](images/040597e73ff9a0011b2c412ff3ccb629be33ffbd79214a47a1654857495ee3e1.jpg)  
FIG. 3. Oscillator pair correlations with the same parameters as in Fig. 1 and (a)  $a_{12} = 0 = b_{12}$  (separable entangled initial state); (b)  $a_{12} = 0.5 = -b_{12}$  (inseparable entangled initial state).

entangled case, whereas curve (b) is for the initially separable entangled case. They both show oscillations about zero values, exhibiting "revival" of entanglement as time progresses. This also clearly shows that the entanglement property changes over time, a feature worth emphasizing.

![](images/389e4a77b993b3eeed2e9fcd9573c04fc540345a2526ca2f5b0d13fe0650e079.jpg)  
FIG. 4. Evolution of the determinant of the covariance matrix  $C_s$  [Eq. (40)], the sign of which determines whether the state is inseparably entangled ( $< 0$ ) or separably entangled ( $\geqslant 0$ ), with the same parameters as in Fig. 1 and (a)  $a_{12} = 0 = b_{12}$  (separable entangled initial state); (b)  $a_{12} = 0.5 = -b_{12}$  (inseparable entangled initial state).

What was initially separable entangled may become inseparable entangled some time later and vice versa and this characteristic may change several times over a period of time. This implies that in actual experiment, such an oscillation in entanglement may provide windows where such properties are either to be preferred or avoided. It should be remarked that these features of the simplified model are retained more or less in the forms presented here when one considers more general equations given in Appendix A. The only point to be noted is that the decoherence and entanglement influence each other in this more general setting, which was not the case in the model discussed here.

# VI. CONCLUDING REMARKS

One of the important consequences of the Lindblad theory is that one can obtain a mixed state from an initial pure state and vice versa. In this paper, in particular, we demonstrate another aspect of this feature by showing that we can obtain an inseparable entangled state from an initially separable entangled state. This feature allows us to reinterpret it as a manipulation of the entanglement by means of the parameters of the theory, which in turn is a manifestation of the environment or other elements of the system. Manipulation of decoherence is also possible, as is clear from our example. Interpreting the Lindblad parameters as the parameters associated with the environment, we note that the model calculation given here implies that important features of decoherence and entanglement may be manipulated by suitable change in the environment. In the experimental situations presented in Refs. [13-15], for example, simple coherent systems such as quantum dots, trapped ions, and nuclear spins are studied in an attempt to realize these features and their possible control. There is also a recent experimental investigation [16] of controlling the decoherence of trapped ions by laser fields that can change the interaction between the trapped ion and the reservoir. The same technique may possibly be employed to investigate the control of entanglement. We hope to investigate possible determinations of the Lindblad parameters in terms of interactions between the environment Hamiltonian and the system of interest, thus providing a microscopic picture of such phenomena in realistic situations.

# ACKNOWLEDGMENTS

Both authors were supported in part by the Office of Naval Research. We also thank Dr. Peter Reynolds of the Office Naval Research for supporting this research.

# APPENDIX A: DYNAMICAL EQUATIONS FOR THE MATRIX ELEMENTS

The equations for the coefficients in the Gaussian ansatz, Eq. (11), are obtained when substituted in Eq. (10). Here we arrange them in three sets: the first corresponds to the oscillator  $A$ , the second to the oscillator  $B$ , while the third set corresponds to the interaction between the two oscillators,

$$
\lambda \partial_ {\tau} A _ {1 1} = - 2 \omega_ {A} B _ {1 1} - 2 h _ {1 3} ^ {(i)} A _ {1 1} - 2 h _ {1 2} ^ {(i)} B _ {1 2} - 2 h _ {1 4} ^ {(i)} A _ {1 2} + h _ {1 1}, \tag {A1}
$$

$$
\begin{array}{l} \lambda \partial_ {\tau} B _ {1 1} = \omega_ {A} A _ {1 1} - \omega_ {A} C _ {1 1} - 2 h _ {1 3} ^ {(i)} B _ {1 1} + h _ {3 4} ^ {(i)} A _ {1 2} - 2 h _ {2 3} ^ {(i)} B _ {1 2} \\ - h _ {1 4} ^ {(i)} B _ {2 1} - h _ {1 2} ^ {(i)} C _ {1 2} - h _ {1 3} ^ {(r)}, \tag {A2} \\ \end{array}
$$

$$
\lambda \partial_ {\tau} C _ {1 1} = 2 \omega_ {A} B _ {1 1} - 2 h _ {1 3} ^ {(i)} C _ {1 1} + 2 h _ {3 4} ^ {(i)} B _ {2 1} - 2 h _ {2 3} ^ {(i)} C _ {1 2} + h _ {3 3}; \tag {A3}
$$

$$
\begin{array}{l} \lambda \partial_ {\tau} A _ {2 2} = - 2 \omega_ {B} B _ {2 2} - 2 h _ {2 4} ^ {(i)} A _ {2 2} + 2 h _ {2 3} ^ {(i)} A _ {1 2} + 2 h _ {1 2} ^ {(i)} B _ {2 1} + h _ {2 2}, (A4) \\ \lambda \partial_ {\tau} B _ {2 2} = \omega_ {B} A _ {2 2} - \omega_ {B} C _ {2 2} - 2 h _ {2 4} ^ {(i)} B _ {2 2} + h _ {3 4} ^ {(i)} A _ {1 2} + h _ {2 3} ^ {(i)} B _ {1 2} \\ - h _ {1 4} ^ {(i)} B _ {2 1} + h _ {1 2} ^ {(i)} C _ {1 2} - h _ {2 4} ^ {(r)}, (A5) \\ \end{array}
$$

$$
\lambda \partial_ {\tau} C _ {2 2} = 2 \omega_ {B} B _ {2 2} - 2 h _ {2 4} ^ {(i)} C _ {2 2} - 2 h _ {3 4} ^ {(i)} B _ {1 2} - 2 h _ {1 4} ^ {(i)} C _ {1 2} + h _ {4 4}; \tag {A6}
$$

$$
\begin{array}{l} \lambda \partial_ {\tau} A _ {1 2} = - \omega_ {A} B _ {2 1} - \omega_ {B} B _ {1 2} - \left(h _ {1 3} ^ {(i)} + h _ {2 4} ^ {(i)}\right) A _ {1 2} + h _ {2 3} ^ {(i)} A _ {1 1} \\ - h _ {1 4} ^ {(i)} A _ {2 2} + h _ {1 2} ^ {(i)} B _ {1 1} - h _ {1 2} ^ {(i)} B _ {2 2} + h _ {1 2} ^ {(r)}, \tag {A7} \\ \end{array}
$$

$$
\begin{array}{l} \lambda \partial_ {\tau} B _ {1 2} = \omega_ {B} A _ {1 2} - \omega_ {A} C _ {1 2} - \left(h _ {1 3} ^ {(i)} + h _ {2 4} ^ {(i)}\right) B _ {1 2} - h _ {3 4} ^ {(i)} A _ {1 1} \\ - h _ {1 4} ^ {(i)} B _ {1 1} - h _ {1 4} ^ {(i)} B _ {2 2} - h _ {1 2} ^ {(i)} C _ {2 2} - h _ {1 4} ^ {(r)}, \tag {A8} \\ \end{array}
$$

$$
\begin{array}{l} \lambda \partial_ {\tau} B _ {2 1} = \omega_ {A} A _ {1 2} - \omega_ {B} C _ {1 2} - \left(h _ {1 3} ^ {(i)} + h _ {2 4} ^ {(i)}\right) B _ {2 1} - h _ {3 4} ^ {(i)} A _ {2 2} \\ + h _ {2 3} ^ {(i)} B _ {1 1} - h _ {2 3} ^ {(i)} B _ {2 2} - h _ {1 2} ^ {(i)} C _ {1 1} + h _ {2 3} ^ {(r)}, \tag {A9} \\ \end{array}
$$

$$
\begin{array}{l} \lambda \partial_ {\tau} C _ {1 2} = \omega_ {A} B _ {1 2} + \omega_ {B} B _ {2 1} - \left(h _ {1 3} ^ {(i)} + h _ {2 4} ^ {(i)}\right) C _ {1 2} - h _ {3 4} ^ {(i)} B _ {1 1} \\ + h _ {3 4} ^ {(i)} B _ {1 1} - h _ {1 4} ^ {(i)} C _ {1 1} - h _ {2 3} ^ {(i)} C _ {2 2} + h _ {3 4} ^ {(r)}. \tag {A10} \\ \end{array}
$$

We note that these equations are coupled to each other in an interesting way. The equations for the  $A$  and  $B$  oscillators are coupled to each other via their interactions introduced in the Lindblad evolution. This implies that in this model, the correlations and decoherence in the two oscillators are influenced by the entanglement between the two due to the dissipative processes contained in the Lindblad formulation. The stationary solutions of these equations are obtained by setting to zero all the time derivatives in the left sides of these equations. They are also the solutions approached for asymptotically large times. In a simplified model given in the text, we consider a decoupled set of equations, which do not compromise the final results but serve the purpose of illustrating how these influences come about and how one may control these important features of the quantum oscillator pair. In Appendix B, explicit solutions of the equations are presented.

# APPENDIX B: SOLUTIONS OF EQS. (34)-(36)

The solution for the  $A$ -oscillator equations [Eq. (34)] is

$$
\begin{array}{l} A _ {1 1} (\tau) = \frac {1}{2} b _ {1} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \left[ 1 + \cos 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right] + \frac {1}{2} a _ {1} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \left[ 1 - \cos 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right] \\ + \frac {\left(h _ {1 1} / \omega_ {A}\right)}{\Gamma_ {A} \left(\Gamma_ {A} ^ {2} + 4\right)} \left\{\Gamma_ {A} ^ {2} \left(1 - \frac {e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}}}{2} \left[ 1 + \cos 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right]\right) + 2 \left(1 - e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}}\right) + \Gamma_ {A} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \sin 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right\} \\ + \frac {\left(h _ {3 3} / \omega_ {A}\right)}{2 \Gamma_ {A} \left(\Gamma_ {A} ^ {2} + 4\right)} \left\{- \Gamma_ {A} ^ {2} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \left[ 1 - \cos 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right] + 4 \left(1 - e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}}\right) - 2 \Gamma_ {A} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \sin 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right\} \\ + \frac {\left(h _ {1 3} ^ {(r)} / \omega_ {A}\right)}{\left(\Gamma_ {A} ^ {2} + 4\right)} \left\{2 \left[ 1 - e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \cos 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right] - \Gamma_ {A} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \sin 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right\}, \tag {B1} \\ \end{array}
$$

$$
\begin{array}{l} B _ {1 1} (\tau) = \frac {\left(b _ {1} - a _ {1}\right)}{2} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \sin 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) + \frac {\left[ \left(h _ {1 1} - h _ {3 3}\right) / \omega_ {A} \right]}{\left(\Gamma_ {A} ^ {2} + 4\right)} \left\{1 - e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \left[ \cos 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) + \frac {1}{2} \Gamma_ {A} \sin 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right] \right\} \\ - \frac {\left(h _ {1 3} ^ {(r)} / \omega_ {A}\right)}{\left(\Gamma_ {A} ^ {2} + 4\right)} \left\{\Gamma_ {A} \left[ 1 - e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \cos 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right] - 2 e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \sin 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right\}, \tag {B2} \\ \end{array}
$$

$$
\begin{array}{l} C _ {1 1} (\tau) = \frac {1}{2} a _ {1} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \left[ 1 + \cos 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right] + \frac {1}{2} b _ {1} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \left[ 1 - \cos 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right] \\ + \frac {\left(h _ {1 1} / \omega_ {A}\right)}{2 \Gamma_ {A} \left(\Gamma_ {A} ^ {2} + 4\right)} \left\{- \Gamma_ {A} ^ {2} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \left[ 1 - \cos 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right] + 4 \left(1 - e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}}\right) - 2 \Gamma_ {A} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \sin 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right\} \\ + \frac {\left(h _ {3 3} / \omega_ {A}\right)}{2 \Gamma_ {A} \left(\Gamma_ {A} ^ {2} + 4\right)} \left\{\Gamma_ {A} ^ {2} \left[ 1 - e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \cos 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right] + \left(\Gamma_ {A} ^ {2} + 4\right) \left(1 - e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}}\right) + 2 \Gamma_ {A} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \sin 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right\} \\ + \frac {\left(h _ {1 3} ^ {(r)} / \omega_ {A}\right)}{\left(\Gamma_ {A} ^ {2} + 4\right)} \left\{- 2 \left[ 1 - e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \cos 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right] + \Gamma_ {A} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma_ {A}} \sin 2 \tau \left(\frac {\omega_ {A}}{\lambda}\right) \right\}. \tag {B3} \\ \end{array}
$$

In the above expressions, we have set  $\Gamma_A = 2h_{13}^{(i)} / \omega_A$ . The solution for the  $B$  oscillator [Eq. (37)] is obtained by the substitutions  $1\rightarrow 2$ ,  $3\rightarrow 4$ , and  $A\rightarrow B$  in the above expressions.

We now give the solution to Eq. (36). Here we set  $\Gamma = (\Gamma_A + r\Gamma_B) / 2$  and  $r = \omega_{B} / \omega_{A}$ :

$$
\begin{array}{l} A _ {1 2} (\tau) = b _ {1 2} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma} \cos \tau \left(\omega_ {A} / \lambda\right) \cos \tau \left(\omega_ {B} / \lambda\right) + a _ {1 2} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma} \sin \tau \left(\omega_ {A} / \lambda\right) \sin \tau \left(\omega_ {B} / \lambda\right) \\ + \left(\frac {h _ {1 2} ^ {(r)}}{\omega_ {A}}\right) \Gamma \frac {\left(\Gamma^ {2} + 1 + r ^ {2}\right)}{\left[ \Gamma^ {2} + (1 + r) ^ {2} \right] \left[ \Gamma^ {2} + (1 - r) ^ {2} \right]} - \left(\frac {h _ {1 2} ^ {(r)}}{\omega_ {A}}\right) \frac {\Gamma e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma}}{2} \left\{\frac {\cos \tau \left(\omega_ {A} + \omega_ {B}\right) / \lambda}{\Gamma^ {2} + (1 + r) ^ {2}} + \frac {\cos \tau \left(\omega_ {A} - \omega_ {B}\right) / \lambda}{\Gamma^ {2} + (1 - r) ^ {2}} \right\} \\ + \left(\frac {h _ {1 2} ^ {(r)}}{\omega_ {A}}\right) \frac {e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma}}{2} \left\{\frac {(1 + r) \sin \tau \left(\omega_ {A} + \omega_ {B}\right) / \lambda}{\Gamma^ {2} + (1 + r) ^ {2}} - \frac {(1 - r) \sin \tau \left(\omega_ {A} - \omega_ {B}\right) / \lambda}{\Gamma^ {2} + (1 - r) ^ {2}} \right\}, \tag {B4} \\ \end{array}
$$

$$
\begin{array}{l} B _ {1 2} (\tau) = \frac {b _ {1 2} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma}}{4} \left\{\sin \tau \left[ \omega_ {A} (1 + r) / \lambda \right] + \sin \tau \left[ \omega_ {A} (1 - r) / \lambda \right] \right\} - \frac {a _ {1 2} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma}}{2} \left[ \frac {3}{(1 + r)} \sin \tau \left[ \omega_ {A} (1 + r) / \lambda \right] \right. \\ + \frac {1}{(1 - r)} \sin \tau \left[ \omega_ {A} (1 - r) / \lambda \right] + \left(\frac {h _ {1 2} ^ {(r)}}{\omega_ {A}}\right) \frac {\left(\Gamma^ {2} + 1 + r ^ {2} - r\right)}{\left[ \Gamma^ {2} + (1 + r) ^ {2} \right] \left[ \Gamma^ {2} + (1 - r) ^ {2} \right]} \\ - \left(\frac {h _ {1 2} ^ {(r)}}{\omega_ {A}}\right) \frac {3 e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma}}{4 (1 + r) \left[ \Gamma^ {2} + (1 + r) ^ {2} \right]} \left\{\Gamma \sin \tau \omega_ {A} (1 + r) / \lambda + (1 + r) \cos \tau \omega_ {A} (1 + r) / \lambda \right\} \\ - \left(\frac {h _ {1 2} ^ {(r)}}{\omega_ {A}}\right) \frac {e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma}}{4 (1 - r) \left[ \Gamma^ {2} + (1 - r) ^ {2} \right]} \left\{\Gamma \sin \tau \omega_ {A} (1 - r) / \lambda + (1 - r) \cos \tau \omega_ {A} (1 - r) / \lambda \right\}, \tag {B5} \\ \end{array}
$$

$$
\begin{array}{l} B _ {2 1} (\tau) = \frac {b _ {1 2} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma}}{4 (1 + r)} \left[ \frac {(2 + r)}{(1 + r)} \sin \tau \left[ \omega_ {A} (1 + r) / \lambda \right] + \frac {(2 - r)}{(1 - r)} \sin \tau \left[ \omega_ {A} (1 - r) / \lambda \right] \right] \\ - \frac {a _ {1 2} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma}}{2} \left\{\sin \tau \left[ \omega_ {A} (1 + r) / \lambda \right] + \sin \tau \left[ \omega_ {A} (1 - r) / \lambda \right] \right\} + \left(\frac {h _ {1 2} ^ {(r)}}{\omega_ {A}}\right) \frac {\left(\Gamma^ {2} + 1\right)}{\left[ \Gamma^ {2} + (1 + r) ^ {2} \right] \left[ \Gamma^ {2} + (1 - r) ^ {2} \right]} \\ - \left(\frac {h _ {1 2} ^ {(r)}}{\omega_ {A}}\right) \frac {(2 + r) e ^ {- \tau (\omega_ {A} / \lambda) \Gamma}}{4 (1 + r) [ \Gamma^ {2} + (1 + r) ^ {2} ]} \{- \Gamma \sin \tau \omega_ {A} (1 + r) / \lambda + (1 + r) \cos \tau \omega_ {A} (1 + r) / \lambda \} \\ - \left(\frac {h _ {1 2} ^ {(r)}}{\omega_ {A}}\right) \frac {(2 - r) e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma}}{4 (1 - r) \left[ \Gamma^ {2} + (1 - r) ^ {2} \right]} \{- \Gamma \sin \tau \omega_ {A} (1 - r) / \lambda + (1 - r) \cos \tau \omega_ {A} (1 - r) / \lambda \}, \tag {B6} \\ \end{array}
$$

$$
\begin{array}{l} C _ {1 2} (\tau) = a _ {1 2} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma} \cos \tau \left(\omega_ {A} / \lambda\right) \cos \tau \left(\omega_ {B} / \lambda\right) + b _ {1 2} e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma} \sin \tau \left(\omega_ {A} / \lambda\right) \sin \tau \left(\omega_ {B} / \lambda\right) \\ + \left(\frac {h _ {1 2} ^ {(r)}}{\omega_ {A}}\right) \Gamma \frac {r}{[ \Gamma^ {2} + (1 + r) ^ {2} ] [ \Gamma^ {2} + (1 - r) ^ {2} ]} + \left(\frac {h _ {1 2} ^ {(r)}}{\omega_ {A}}\right) \frac {e ^ {- \tau (\omega_ {A} / \lambda) \Gamma}}{4 [ \Gamma^ {2} + (1 + r) ^ {2} ]} \left\{\Gamma \cos \tau \omega_ {A} (1 + r) / \lambda - (1 + r) \sin \tau \omega_ {A} (1 + r) / \lambda \right\} \\ - \left(\frac {h _ {1 2} ^ {(r)}}{\omega_ {A}}\right) \frac {e ^ {- \tau \left(\omega_ {A} / \lambda\right) \Gamma}}{4 \left[ \Gamma^ {2} + (1 - r) ^ {2} \right]} \left\{\Gamma \cos \tau \omega_ {A} (1 - r) / \lambda - (1 - r) \sin \tau \omega_ {A} (1 - r) / \lambda \right\}. \tag {B7} \\ \end{array}
$$

These expressions are numerically evaluated for a certain choice of parameters and are displayed in graphical form in the figures. Their significance is then elucidated in terms of some of the experimental situations being examined that were mentioned in the Introduction.

[1] R. Simon, Phys. Rev. Lett. 84, 2726 (2000).  
[2] L. M. Duan, G. Giedke, J. I. Cirac, and P. Zoller, Phys. Rev. Lett. 84, 2722 (2000).  
[3] G. Lindblad, Commun. Math. Phys. 48, 119 (1976); see also V. Gorini, A. Kassakowski, and E. C. G. Sudarshan, J. Math. Phys. 17, 821 (1976).  
[4] A. Isar, A. Sandulescu, and W. Scheid, Phys. Rev. E 60, 6371 (1999).  
[5] A. K. Rajagopal, Phys. Lett. A 228, 66 (1997).  
[6] D. Giulini, E. Joos, C. Kieffer, J. Kupsch, I.-O. Stamatescu, and H. D. Zeh, Decoherence and the Appearance of a Classical World in Quantum Theory (Springer-Verlag, New York, 1996).  
[7] O. Eboli, R. Jackiw, and So-Young Pi, Phys. Rev. D 37, 3557 (1988).  
[8] A. K. Rajagopal, Phys. Lett. A 246, 237 (1998).  
[9] R. W. Rendell and A. K. Rajagopal, Phys. Lett. A (to be

published), e-print quant-ph/0008099.  
[10] J. I. Cirac and P. Zoller, Nature (London) 404, 579 (2000).  
[11] T. Tanamoto, Phys. Rev. A 61, 022305 (2000).  
[12] D. Loss and E. V. Sukhorukov, Phys. Rev. Lett. 84, 1035 (2000).  
[13] G. Chen, N. H. Bonadeo, D. G. Steel, D. Gammon, D. S. Katzer, D. Park, and L. J. Sham, Science 289, 1906 (2000).  
[14] C. A. Sackett, D. Kleiplinski, B. E. King, C. Langer, V. Meyer, C. J. Myatt, M. Rowe, Q. A. Turchette, W. M. Itano, D. J. Wineland, and C. Monroe, Nature (London) 404, 256 (2000).  
[15] I. L. Chuang, L. M. K. Vandersypen, X. Zhou, D. W. Leung, and S. Lloyd, Nature (London) 393, 143 (1998).  
[16] C. J. Myatt, B. E. King, Q. A. Turchette, C. A. Sackett, D. Kleiplinski, W. M. Itano, C. Monroe, and D. J. Wineland, Nature (London) 403, 269 (2000).