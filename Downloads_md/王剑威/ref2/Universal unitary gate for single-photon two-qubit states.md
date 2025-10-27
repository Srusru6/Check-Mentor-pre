# Universal unitary gate for single-photon two-qubit states

Berthold-Georg Englert, $^{1,2}$  Christian Kurtsiefer, $^{3}$  and Harald Weinfurter $^{1,2}$ $^{1}$ Max-Planck-Institut für Quantenoptik, Hans-Kopfermann-Strasse 1, 85748 Garching, Germany  
 $^{2}$ Abteilung Quantenphysik, Universität Ulm, Albert-Einstein-Allee 11, 89069 Ulm, Germany  
 $^{3}$ Sektion Physik, Universität München, Schellingstraße 4, 80799 München, Germany  
(Received 7 July 2000; published 7 February 2001)

Upon entangling a spatial binary alternative of a photon with its polarization, one can use single photons to study arbitrary 2-qubit states. Sending the photon through a Mach-Zehnder interferometer, equipped with sets of wave plates that change the polarization, amounts to performing a unitary transformation on the 2-qubit state. We show that any desired unitary gate can be realized by a judicious choice of the parameters of the setup and discuss a number of applications. They include the diagnosis of an unknown 2-qubit state, an optical Grover search, and the realization of a thought experiment invented by Vaidman, Aharonov, and Albert.

DOI: 10.1103/PhysRevA.63.032303

PACS number(s): 03.67.-a, 03.65.Ta, 07.60.Ly

# I. INTRODUCTION

Entangled qubits are central to most schemes that have been proposed for quantum communication, quantum information processing, and quantum cryptography (secure key distribution). The basic unit consists of an entangled qubit pair.

Any binary quantum alternative can serve as a qubit and, therefore, different degrees of freedom of one physical object can represent several qubits. One could, for instance, encode some qubits in the motional degrees of freedom of a trapped ion and other qubits in its internal degrees of freedom. In our scheme, both qubits of an entangled pair are physically realized by a single photon: The photon's polarization is one qubit—the "polarization qubit"—and the motional alternative of traveling to the right or to the left is the second qubit—the "spatial qubit."

It is our objective to present an optical model that facilitates experimental studies of qubit pairs as realized by single photons. Such single-photon 2-qubit states were used in a few recent experiments, including a variant of quantum teleportation [1], a remote state preparation [2], demonstrations of simple quantum algorithms [3,4], a quantitative study of wave-particle duality [5], and a test of noncontextual hidden variable theories [6]. Here we go beyond these special applications and consider arbitrary manipulations of such states.

Studying qubit pairs extensively amounts to measuring observables of all kinds. The basic measurement is the detection of the photon in one of four standard states given by combinations of traveling to the right or left and polarized vertically or horizontally. This measurement is easily done, and experimental limitations are only due to imperfections of optical elements (such as polarizing beam splitters) and the efficiency of the single-photon detection. More complicated observables are measured by first transforming the respective four eigenstates to the standard basis states, and then detecting those. Accordingly, being able to perform arbitrary unitary transformations on 2-qubit states is tantamount to being able to measure arbitrary 2-qubit observables.

How this challenge is met, is shown in Sec. II, where we present experimental setups that realize universal unitary gates—for either one of the qubits itself and for both of them

jointly. Then, in Sec. III, we turn to basic applications that include controlled-NOT gates and the measurement of the Bell basis. Advanced applications are discussed in Sec. IV: After dealing with the diagnosis of 2-qubit states and the Grover search, we describe a proposal for a laboratory version of a thought experiment invented by Vaidman, Aharonov, and Albert in 1987. Indeed, their intriguing puzzle largely motivated the paper reported here. We close with a summary and outlook. An appendix contains technical material of a more mathematical nature.

# II. UNIVERSAL UNITARY GATES

# A. Gates for the spatial qubit

The spatial qubit consists of the binary alternative of moving to the right  $(\mathsf{R})$  or to the left  $(\mathsf{L})$ , as indicated in the Mach-Zehnder geometry of Fig. 1. As usual, we use analogs of Pauli's spin operators,

$$
\tau = | L \rangle \langle R |, \quad \tau^ {\dagger} = | R \rangle \langle L |,
$$

$$
\tau_ {1} = \tau + \tau^ {\dagger}, \quad \tau_ {2} = i \tau - i \tau^ {\dagger}, \quad \tau_ {3} = \tau^ {\dagger} \tau - \tau \tau^ {\dagger},
$$

$$
\mathbb {1} _ {\tau} = \tau^ {\dagger} \tau + \tau \tau^ {\dagger}, \tag {1}
$$

so that the unitary action of a symmetric beam splitter is given by

$$
\begin{array}{l} U _ {\mathrm {B S}} = \frac {1}{\sqrt {2}} (| \mathrm {R} \rangle \langle \mathrm {R} | + | \mathrm {L} \rangle \langle \mathrm {L} | + i | \mathrm {R} \rangle \langle \mathrm {L} | + i | \mathrm {L} \rangle \langle \mathrm {R} |) \\ = \frac {1}{\sqrt {2}} \left(\mathbb {1} _ {\tau} + i \tau_ {1}\right). \tag {2} \\ \end{array}
$$

Likewise, the joint action of the mirrors inside the Mach-Zehnder setup is accounted for by the unitary operator

$$
U _ {\text {m i r r}} = - i (| \mathrm {L} \rangle \langle \mathrm {R} | + | \mathrm {R} \rangle \langle \mathrm {L} |) = - i \tau_ {1}, \tag {3}
$$

where the inclusion of a phase factor  $-i$  is a convenient convention because it gives  $U_{\mathrm{BS}}U_{\mathrm{mirr}}U_{\mathrm{BS}} = 1_{\tau}$ , and phase shifters in the R and L branches amount to

$$
U _ {\mathrm {R}} (\phi) = | \mathsf {R} \rangle \mathrm {e} ^ {i \phi} \langle \mathsf {R} | + | \mathsf {L} \rangle \langle \mathsf {L} | = \mathrm {e} ^ {i \phi \tau^ {\dagger} \tau},
$$

$$
U _ {\mathrm {L}} (\phi) = | \mathrm {R} \rangle \langle \mathrm {R} | + | \mathrm {L} \rangle \mathrm {e} ^ {i \phi} \langle \mathrm {L} | = \mathrm {e} ^ {i \phi \tau \tau^ {\dagger}}. \tag {4}
$$

Putting these pieces together, one gets

$$
(| \mathrm {R} \rangle , | \mathrm {L} \rangle) \rightarrow (U _ {\mathrm {M Z}} | \mathrm {R} \rangle , U _ {\mathrm {M Z}} | \mathrm {L} \rangle) = (| \mathrm {R} \rangle , | \mathrm {L} \rangle) \mathcal {U} _ {\mathrm {M Z}} \tag {5}
$$

for the whole Mach-Zehnder interferometer of Fig. 1. The unitary operator

$$
\begin{array}{l} U _ {\mathrm {M Z}} = U _ {\mathrm {R}} \left(\phi_ {2}\right) U _ {\mathrm {B S}} U _ {\mathrm {R}} \left(\varphi_ {1}\right) U _ {\mathrm {L}} \left(\varphi_ {2}\right) U _ {\text {m i r r}} U _ {\mathrm {B S}} U _ {\mathrm {R}} \left(\phi_ {1}\right) \\ = \exp \left(\frac {i}{2} \left(\phi_ {1} + \phi_ {2} + \varphi_ {1} + \varphi_ {2}\right)\right) \exp \left(\frac {i}{2} \phi_ {2} \tau_ {3}\right) \\ \times \exp \left(\frac {i}{2} \left(\varphi_ {1} - \varphi_ {2}\right) \tau_ {2}\right) \exp \left(\frac {i}{2} \phi_ {1} \tau_ {3}\right) \tag {6} \\ \end{array}
$$

is represented by the numerical  $2 \times 2$  matrix

$$
\mathcal {U} _ {\mathrm {M Z}} = \exp \left(\frac {i}{2} \left(\varphi_ {1} + \varphi_ {2}\right)\right) \left( \begin{array}{c c} \exp \left(i \left(\phi_ {1} + \phi_ {2}\right)\right) \cos \frac {\varphi_ {1} - \varphi_ {2}}{2} & \mathrm {e} ^ {i \phi_ {2}} \sin \frac {\varphi_ {1} - \varphi_ {2}}{2} \\ - \mathrm {e} ^ {i \phi_ {1}} \sin \frac {\varphi_ {1} - \varphi_ {2}}{2} & \cos \frac {\varphi_ {1} - \varphi_ {2}}{2} \end{array} \right) \tag {7}
$$

that multiplies the two-component row  $(|\mathsf{R}\rangle ,|\mathsf{L}\rangle)$  in Eq. (5). This matrix is slightly more general than the one in Eq. (1) of Ref. [7].

The latter form in Eq. (6), which is a parametrization in terms of three Eulerian angles  $\phi_{1}$ ,  $\varphi_{1} - \varphi_{2}$ , and  $\phi_{2}$  combined with an over-all phase factor, makes it obvious that any unitary operator for the  $\mathsf{R} / \mathsf{L}$  qubit can be realized by a Mach-Zehnder setup of the kind shown in Fig. 1. Note that  $U_{\mathrm{MZ}} = \mathbb{1}_{\tau}$  if  $\phi_1 = \phi_2 = \varphi_1 = \varphi_2 = 0$ , which is the reason for the conventional phase factor in Eq. (3).

# B. Polarization gates

We regard vertical (v) and horizontal (h) polarization as the basic alternatives of the polarization qubit, and the corresponding Pauli operators are

$$
\sigma = | \mathsf {h} \rangle \langle \mathsf {v} |, \quad \sigma^ {\dagger} = | \mathsf {v} \rangle \langle \mathsf {h} |,
$$

$$
\sigma_ {1} = \sigma + \sigma^ {\dagger}, \quad \sigma_ {2} = i \sigma - i \sigma^ {\dagger}, \quad \sigma_ {3} = \sigma^ {\dagger} \sigma - \sigma \sigma^ {\dagger},
$$

$$
\mathbb {1} _ {\sigma} = \sigma^ {\dagger} \sigma + \sigma \sigma^ {\dagger}. \tag {8}
$$

The photon's polarization is manipulated with the aid of wave plates. A quarter-wave plate (QWP), with its major axis at an angle  $\theta$  to the vertical direction, effects the transition

$$
\left(| \mathrm {v} \rangle , | \mathrm {h} \rangle\right)\rightarrow \left(U _ {\mathrm {Q W P}} (\theta) | \mathrm {v} \rangle , U _ {\mathrm {Q W P}} (\theta) | \mathrm {h} \rangle\right) = \left(| \mathrm {v} \rangle , | \mathrm {h} \rangle\right) \mathcal {U} _ {\mathrm {Q W P}} (\theta), \tag {9}
$$

where the unitary operator  $U_{\mathrm{QWP}}$  is given by

$$
\begin{array}{l} U _ {\mathrm {Q W P}} (\theta) = \mathrm {e} ^ {- i \theta \sigma_ {2}} \mathrm {e} ^ {- i (\pi / 4) \sigma_ {3}} \mathrm {e} ^ {i \theta \sigma_ {2}} \\ = \exp (- i (\pi / 4) [ \sigma_ {1} \sin (2 \theta) + \sigma_ {3} \cos (2 \theta) ]) \\ = \frac {1}{\sqrt {2}} [ 1 _ {\sigma} - i \sigma_ {1} \sin (2 \theta) - i \sigma_ {3} \cos (2 \theta) ], \tag {10} \\ \end{array}
$$

and its  $2\times 2$  matrix representation reads

$$
\mathcal {U} _ {\mathrm {Q W P}} (\theta) = \frac {1}{\sqrt {2}} \left( \begin{array}{c c} 1 - i \cos (2 \theta) & - i \sin (2 \theta) \\ - i \sin (2 \theta) & 1 + i \cos (2 \theta) \end{array} \right). \tag {11}
$$

Likewise, the action of a half-wave plate (HWP) is accounted for by the unitary operator

$$
\begin{array}{l} U _ {\mathrm {H W P}} (\theta) = \left[ U _ {\mathrm {Q W P}} (\theta) \right] ^ {2} \\ = \mathrm {e} ^ {- i \theta \sigma_ {2}} \mathrm {e} ^ {- i (\pi / 2) \sigma_ {3}} \mathrm {e} ^ {i \theta \sigma_ {2}} \\ = - i \left[ \sigma_ {1} \sin (2 \theta) + \sigma_ {3} \cos (2 \theta) \right], \tag {12} \\ \end{array}
$$

represented by the matrix

![](images/76de884357840f09937388b5bed890abb2f5d1be8e670249733ba5c4bd292b2e.jpg)  
FIG. 1. Mach-Zehnder setup that realizes an arbitrary unitary gate for the spatial  $\mathsf{R} / \mathsf{L}$  qubit. There are symmetric beam splitters (BS's) at the entry and exit, and four phase shifters (PS's)—one each in the entry and exit R ports, and two inside the interferometer. Additional PS's in the L ports would be redundant; they could be introduced, either as a supplement or a replacement of the PS's in the R ports, but there is no need for them.

![](images/aacd8d129a52289998d6fe649a86cc99dab1ad704d208d14de72cc06ddda59bf.jpg)  
FIG. 2. By sending a photon through a QWP, then through a HWP, finally through another QWP, its polarization state can be changed unitarily to any other one.

$$
\mathcal {U} _ {\mathrm {H W P}} (\theta) = \left[ \mathcal {U} _ {\mathrm {Q W P}} (\theta) \right] ^ {2} = - i \binom {\cos (2 \theta)} {\sin (2 \theta)} \begin{array}{l l} & \sin (2 \theta) \\ & - \cos (2 \theta) \end{array} . \tag {13}
$$

Particular polarization changes can be done with a single QWP, or a single HWP, or with a QWP and a HWP in succession, and it is familiar [8] that the configuration of Fig. 2, where a HWP is sandwiched by two QWP's, enables one to perform arbitrary changes of the photon's polarization state. This is most easily seen by expressing the net unitary operator in terms of three Eulerian angles,

$$
\begin{array}{l} U _ {\mathrm {p o l}} = U _ {\mathrm {Q W P}} (\gamma) U _ {\mathrm {H W P}} (\beta) U _ {\mathrm {Q W P}} (\alpha) \\ = \exp (- i (\gamma + 3 \pi / 4) \sigma_ {2}) \exp (i (\alpha - 2 \beta + \gamma)) \sigma_ {3} \\ \times \exp (i (\alpha - \pi / 4) \sigma_ {2}). \tag {14} \\ \end{array}
$$

We do not get an over-all phase factor here as there is in Eq. (6), but that does not matter. For example,  $U_{\mathrm{pol}} = \mathbb{1}_{\sigma}$  obtains for  $\alpha = \beta \pm \pi / 2 = \gamma$  since  $U_{\mathrm{QWP}}(\beta \pm \pi / 2) = [U_{\mathrm{QWP}}(\beta)]^{-1}$  and  $\alpha = \beta = \gamma$  gives  $U_{\mathrm{pol}} = -\mathbb{1}_{\sigma}$ . A polarization dependent phase shifter, that is

$$
U _ {\mathrm {p o l}} = | \mathrm {v} \rangle \mathrm {e} ^ {- i \vartheta} \langle \mathrm {v} | + | \mathrm {h} \rangle \mathrm {e} ^ {i \vartheta} \langle \mathrm {h} |, \tag {15}
$$

is realized by the setting  $\alpha = \gamma = \frac{1}{4}\pi$ ,  $\beta = \frac{1}{2}\vartheta - \frac{1}{4}\pi$ .

# C. Arbitrary 2-qubit gates

Unitary gates  $U_{\mathrm{MZ}}$  and  $U_{\mathrm{pol}}$  for manipulations of the  $\mathsf{R} / \mathsf{L}$  qubit and the  $\mathsf{v} / \mathsf{h}$  qubit individually are thus at hand. We now combine them to construct universal gates that process arbitrary 2-qubit states unitarily. This is achieved by a modification of the Mach-Zehnder setup of Fig. 1. In addition to the polarization-independent phase shifters already in place, we let the photon pass through wave-plate combinations of the kind depicted in Fig. 2. The entire setup is then as shown in Fig. 3.

Where we had  $U_{\mathrm{R}}$  and  $U_{\mathrm{L}}$  in the product giving  $U_{\mathrm{MZ}}$  in Eq. (6), we now have corresponding factors in which the phase factors of Eqs. (4) are replaced by unitary operators that affect the polarization—denoted by  $V_{1}$ ,  $V_{2}$  for the entry and exit ports, and by  $V_{\mathrm{R}}$ ,  $V_{\mathrm{L}}$  inside the interferometer. Each of them represents a phase shifter and a set of wave plates, and is therefore of the form (14) multiplied by a phase factor. Thus, the unitary operator  $S$  associated with the 2-qubit gate of Fig. 3 is given by

![](images/fe641c3fe8abfd08b6ab4e241fc2d82f6424a84a2900282d2aa6c2d6148ca81a.jpg)  
FIG. 3. Universal unitary gate for 2-qubit states. In addition to the PS's of Fig. 1, there are now wave plates (WP's) in the QWP/HWP/QWP combination of Fig. 2. Each PS and WP's set is specified by a phase (called  $\phi_{1,2}$  or  $\varphi_{1,2}$  in Fig. 1) and three angles  $\alpha$ ,  $\beta$ , and  $\gamma$  that state the orientations of the WP's, as in Fig. 2.

$$
\begin{array}{l} S = \left(\tau^ {\dagger} \tau V _ {2} + \tau \tau^ {\dagger}\right) U _ {\mathrm {B S}} \left(\tau^ {\dagger} \tau V _ {\mathrm {R}} + \tau \tau^ {\dagger} V _ {\mathrm {L}}\right) \\ \times U _ {\text {m i r r}} U _ {\mathrm {B S}} \left(\tau^ {\dagger} \tau V _ {1} + \tau \tau^ {\dagger}\right), \tag {16} \\ \end{array}
$$

or

$$
S = \tau^ {\dagger} \tau S _ {\mathrm {R R}} + \tau \tau^ {\dagger} S _ {\mathrm {L L}} + \tau S _ {\mathrm {L R}} + \tau^ {\dagger} S _ {\mathrm {R L}} \triangleq \left( \begin{array}{c c} S _ {\mathrm {R R}} & S _ {\mathrm {R L}} \\ S _ {\mathrm {L R}} & S _ {\mathrm {L L}} \end{array} \right) _ {\tau}, \tag {17}
$$

where the  $2\times 2$  matrix refers to the spatial R/L alternative, and the entries of this matrix are

$$
\begin{array}{l} S _ {\mathrm {R R}} = \frac {1}{2} V _ {2} \left(V _ {\mathrm {R}} + V _ {\mathrm {L}}\right) V _ {1}, \\ S _ {\mathrm {L L}} = \frac {1}{2} \left(V _ {\mathrm {R}} + V _ {\mathrm {L}}\right), \\ \end{array}
$$

$$
S _ {\mathrm {R L}} = - \frac {i}{2} V _ {2} \left(V _ {\mathrm {R}} - V _ {\mathrm {L}}\right),
$$

$$
S _ {\mathrm {L R}} = \frac {i}{2} \left(V _ {\mathrm {R}} - V _ {\mathrm {L}}\right) V _ {1}. \tag {18}
$$

The physical significance of these polarization operators is immediate:  $S_{\mathrm{LR}}$ , for instance, accounts for the polarization change associated with photons entering the R port and leaving the L port.

There are no phase shifters or wave plates in the entry and exit L ports. Indeed, one does not need them because the various combinations shown in Fig. 4 are perfectly equivalent. Further configurations become possible when using polarizing beam splitters in the Mach-Zehnder setup. Of course, when it comes to actual experimental realizations, one variant could be more advantageous, for technical reasons, than the others, and then the freedom to choose freely

![](images/6b47d0e26a2bb92e7bfd5dd3fa561f071b7f531f7a2739c33a0e9680cd2d9252.jpg)  
FIG. 4. Equivalent setups involving a symmetric beam splitter and three or four sets of phase shifter and wave plates. The central configuration has polarization-changing and phase-shifting elements in both entry ports and both exit ports. The two top configurations have one empty input port; the two bottom configurations have one empty output port. With corresponding polarization gates, as indicated, each one of the five setups represents the 2-qubit gate  $2^{-1/2}(\tau^{\dagger}\tau R_{2}R_{1} + \tau\tau^{\dagger}L_{2}L_{1} + i\tau L_{2}R_{1} + i\tau^{\dagger}R_{2}L_{1})$ .

among them is handy. For the more theoretical purposes of the present discussion, however, we will confine ourselves to setups of the kind depicted in Fig. 3.

The four operators in Eqs. (18) need not be unitary themselves (and as a rule they are not), but their form is much restricted by the unitary property of  $S$ , which implies the identities

$$
S _ {\mathrm {R R}} ^ {\dagger} S _ {\mathrm {R R}} + S _ {\mathrm {L R}} ^ {\dagger} S _ {\mathrm {L R}} = 1 _ {\sigma},
$$

$$
S _ {\mathrm {R L}} ^ {\dagger} S _ {\mathrm {R L}} + S _ {\mathrm {L L}} ^ {\dagger} S _ {\mathrm {L L}} = \mathbb {1} _ {\sigma},
$$

$$
S _ {\mathrm {R R}} ^ {\dagger} S _ {\mathrm {R L}} + S _ {\mathrm {L R}} ^ {\dagger} S _ {\mathrm {L L}} = 0,
$$

$$
S _ {\mathrm {R L}} ^ {\dagger} S _ {\mathrm {R R}} + S _ {\mathrm {L L}} ^ {\dagger} S _ {\mathrm {L R}} = 0, \tag {19}
$$

the last two being adjoints of each other. Since  $V_{1}$ ,  $V_{2}$ ,  $V_{\mathrm{R}}$ , and  $V_{\mathrm{L}}$  are unitary themselves, Eqs. (19) hold for the operators in Eqs. (18) by construction.

The reverse is also true: For any given unitary 2-qubit operator  $S$  one can find four unitary polarization operators  $V_{1}$ ,  $V_{2}$ ,  $V_{\mathrm{R}}$ , and  $V_{\mathrm{L}}$  such that  $S$  is of the form (17) with (18). To prove this assertion, we must show that Eqs. (18) can be solved for  $V_{1}$ ,  $V_{2}$ ,  $V_{\mathrm{R}}$ , and  $V_{\mathrm{L}}$  provided that the conditions (19) are obeyed.

A first technical step of this proof is given in the Appendix, where we establish that  $S^{\dagger}S = SS^{\dagger} = \mathbb{1}_{\sigma}\mathbb{1}_{\tau}\equiv \mathbb{1}$  implies that the matrix entries of Eq. (17) are of the general form

$$
S _ {\mathrm {R R}} = | \bar {\psi} _ {1} \rangle \cos \vartheta \langle \psi_ {1} | + | \bar {\psi} _ {2} \rangle \cos \theta \langle \psi_ {2} |,
$$

$$
S _ {\mathrm {L L}} = | \bar {\chi} _ {1} \rangle \cos \vartheta \langle \chi_ {1} | + | \bar {\chi} _ {2} \rangle \cos \theta \langle \chi_ {2} |,
$$

$$
i S _ {\mathrm {R L}} = \left| \bar {\psi} _ {1} \right\rangle \sin \vartheta \langle \chi_ {1} | + \left| \bar {\psi} _ {2} \right\rangle \sin \theta \langle \chi_ {2} |,
$$

$$
i S _ {\mathrm {L R}} = \left| \bar {\chi} _ {1} \right\rangle \sin \vartheta \left\langle \psi_ {1} \right| + \left| \bar {\chi} _ {2} \right\rangle \sin \theta \left\langle \psi_ {2} \right|, \tag {20}
$$

where the kets and bras stand for particular sets of polarization states, each set being orthonormal,

$$
\langle \psi_ {j} | \psi_ {k} \rangle = \langle \bar {\psi} _ {j} | \bar {\psi} _ {k} \rangle = \langle \chi_ {j} | \chi_ {k} \rangle = \langle \bar {\chi} _ {j} | \bar {\chi} _ {k} \rangle = \delta_ {j k}, \tag {21}
$$

but with no other a priori relation among them. Each set is specified by four parameters, two of them phases that do not enter the basic projectors. Since only states with the same subscript are paired in Eqs. (20), six relative phases are relevant, so that two of the eight phases can be fixed by a convenient convention. In other words, 14 parameters are needed to specify the various ket-bra products in Eq. (20). Together with the values of  $\vartheta$  and  $\theta$ , there is thus a total of 16 parameters, as there should be.

For given left-hand sides in Eqs. (20), one determines the eigenvalues and eigenstates of  $S_{\mathrm{RR}}^{\dagger}S_{\mathrm{RR}}$  to find  $\vartheta, \theta$ , and the  $\psi$  states (with arbitrary phases). The eigenstates of  $S_{\mathrm{RR}}S_{\mathrm{RR}}^{\dagger}$  then supply the  $\overline{\psi}$  states with well-defined phases relative to the  $\psi$  states, and the eigenstates of  $S_{\mathrm{LL}}^{\dagger}S_{\mathrm{LL}}$  and  $S_{\mathrm{LL}}S_{\mathrm{LL}}^{\dagger}$  yield the  $\chi$  and  $\overline{\chi}$  states, respectively.

As soon as the ingredients of the right-hand sides of Eqs. (20) are at hand, one constructs the four  $V$  operators in accordance with

$$
V _ {1} = \left| \chi_ {1} \right\rangle (\mp i) _ {1} \left\langle \psi_ {1} \right| + \left| \chi_ {2} \right\rangle (\mp i) _ {2} \left\langle \psi_ {2} \right|,
$$

$$
V _ {2} = \left| \bar {\psi} _ {1} \right\rangle (\pm i) _ {1} \langle \bar {\chi} _ {1} | + \left| \bar {\psi} _ {2} \right\rangle (\pm i) _ {2} \langle \bar {\chi} _ {2} |,
$$

$$
V _ {R} = \left| \bar {\chi} _ {1} \right\rangle e ^ {(\mp i) _ {1} \vartheta} \left\langle \chi_ {1} \right| + \left| \bar {\chi} _ {2} \right\rangle e ^ {(\mp i) _ {2} \theta} \left\langle \chi_ {2} \right|,
$$

$$
V _ {\mathrm {L}} = | \bar {\chi} _ {1} \rangle \mathrm {e} ^ {(\pm i) _ {1} \vartheta} \langle \chi_ {1} | + | \bar {\chi} _ {2} \rangle \mathrm {e} ^ {(\pm i) _ {2} \theta} \langle \chi_ {2} |, \tag {22}
$$

where one must use consistently the upper or lower signs of  $i$  in  $(\cdot)_{1}$  and  $(\cdot)_{2}$ , but either one of the four possible sign choices will do.

# III. BASIC APPLICATIONS

# A. Controlled-NOT gate

As a first application, a warm-up problem, we consider controlled-NOT gates. If the  $\mathsf{R} / \mathsf{L}$  qubit controls the  $\mathsf{v} / \mathsf{h}$  qubit, such a gate does nothing to the  $\mathsf{R}$  input, but interchanges  $\mathsf{v} \leftrightarrow \mathsf{h}$  on the  $\mathsf{L}$  branch,

$$
S _ {\text {c n o t}, \tau \rightarrow \sigma} (| \mathrm {R v} \rangle , | \mathrm {R h} \rangle , | \mathrm {L v} \rangle , | \mathrm {L h} \rangle) = (| \mathrm {R v} \rangle , | \mathrm {R h} \rangle , | \mathrm {L h} \rangle , | \mathrm {L v} \rangle), \tag {23}
$$

where the subscript  $\tau \to \sigma$  indicates which is the control qubit  $(\tau)$  and which the target qubit  $(\sigma)$ . Equivalently, we have

$$
S _ {\text {c n o t}, \tau \rightarrow \sigma} = \tau^ {\dagger} \tau \bigr ] _ {\sigma} + \tau \tau^ {\dagger} \sigma_ {1},
$$

$$
S _ {\mathrm {R R}} = \mathbb {1} _ {\sigma}, \quad S _ {\mathrm {L L}} = \sigma_ {1}, \quad S _ {\mathrm {R L}} = S _ {\mathrm {L R}} = 0. \tag {24}
$$

One possibility has the upper signs in Eqs. (22), combined with  $\vartheta = \theta = 0$  and

$$
\begin{array}{l} \left| \bar {\chi} _ {1} \right\rangle = \left| \chi_ {2} \right\rangle = i \left| \psi_ {1} \right\rangle = i \left| \bar {\psi} _ {1} \right\rangle = \left| \mathrm {v} \right\rangle , \\ \left| \bar {\chi} _ {2} \right\rangle = \left| \chi_ {1} \right\rangle = i \left| \psi_ {2} \right\rangle = i \left| \bar {\psi} _ {2} \right\rangle = | h \rangle , \tag {25} \\ \end{array}
$$

so that

$$
V _ {1} = V _ {\mathrm {R}} = V _ {\mathrm {L}} = \sigma_ {1} = i U _ {\mathrm {H W P}} (\pi / 4), \quad V _ {2} = \mathbb {1} _ {\sigma}, \tag {26}
$$

which are easily realized with three HWP's and phase shifters that provide the factor of  $i$ . We note that for a controlled-NOT gate, which interchanges  $\nu \leftrightarrow \mathsf{h}$  on the  $\mathsf{R}$  input but leaves the  $\mathsf{L}$  input unchanged, a single HWP for  $V_{1}$  is sufficient. No other polarization changing elements are needed ( $V_{2} = V_{\mathrm{R}} = V_{\mathrm{L}} = 1_{\sigma}$ ) and thus the Mach-Zehnder interferometer isn't even necessary. This is due to the specific configuration chosen in Fig. 3 where the  $\mathsf{L}$  input is empty by convention and, accordingly, for the gate defined by Eq. (23) a single HWP (plus phase shifter) in the  $\mathsf{L}$  input suffices, too.

If, however, the  $R/L$  qubit is controlled by the  $v/h$  qubit,

$$
S _ {\text {c n o t}, \sigma \rightarrow \tau} = 1 _ {\tau} \sigma^ {\dagger} \sigma + \tau_ {1} \sigma \sigma^ {\dagger},
$$

$$
S _ {\mathrm {R R}} = S _ {\mathrm {L L}} = \sigma^ {\dagger} \sigma , \quad S _ {\mathrm {R L}} = S _ {\mathrm {L R}} = \sigma \sigma^ {\dagger}, \tag {27}
$$

the Mach-Zehnder setup is needed. Here one could use

$$
V _ {1} = - i \mathbb {1} _ {\sigma}, \quad V _ {2} = i \mathbb {1} _ {\sigma},
$$

$$
V _ {\mathrm {R}} = \mathbb {1} _ {\sigma}, \quad V _ {\mathrm {L}} = \sigma_ {3} = i U _ {\mathrm {H W P}} (0), \tag {28}
$$

that is phase shifters in the entry and exit R ports, nothing in the R branch of the interferometer, and a phase shifter plus a HWP in the L branch.

# B. Swapping gate

The defining property of a swapping gate is its effect on a product state,

$$
\begin{array}{l} \left(\left| \mathrm {R} \right\rangle R + \left| \mathrm {L} \right\rangle L\right) \otimes \left(\left| \mathrm {v} \right\rangle v + \left| \mathrm {h} \right\rangle h\right) \\ \rightarrow (\left| \right. \mathrm {R} \left. \right\rangle v + \left| \right. \mathrm {L} \left. \right\rangle h) \otimes (\left| \right. \mathrm {v} \left. \right\rangle R + \left| \right. \mathrm {h} \left. \right\rangle L), \tag {29} \\ \end{array}
$$

where  $R, L$  and  $v, h$  are arbitrary probability amplitudes, so that

$$
S _ {\text {s w a p}} \left(\left| R v \right\rangle , \left| R h \right\rangle , \left| L v \right\rangle , \left| L h \right\rangle\right) = \left(\left| R v \right\rangle , \left| L v \right\rangle , \left| R h \right\rangle , \left| L h \right\rangle\right), \tag {30}
$$

or

$$
S _ {\text {s w a p}} = \frac {1}{2} (1 + \tau_ {1} \sigma_ {1} + \tau_ {2} \sigma_ {2} + \tau_ {3} \sigma_ {3}),
$$

$$
S _ {\mathrm {R R}} = \sigma^ {\dagger} \sigma , \quad S _ {\mathrm {L L}} = \sigma \sigma^ {\dagger}, \quad S _ {\mathrm {R L}} = \sigma , \quad S _ {\mathrm {L R}} = \sigma^ {\dagger}. \tag {31}
$$

That  $S_{\mathrm{swap}}$  interchanges the roles of the qubits is compactly stated by

$$
S _ {\text {s w a p}} \tau_ {k} = \sigma_ {k} S _ {\text {s w a p}} \quad \text {f o r} k = 1, 2, 3, \tag {32}
$$

which can serve as an alternative definition. The choice

$$
\begin{array}{l} V _ {1} = - i \sigma_ {1} = U _ {\mathrm {H W P}} (\pi / 4), \\ V _ {2} = i \sigma_ {1} = U _ {\mathrm {H W P}} (- \pi / 4), \\ V _ {\mathrm {R}} = \mathbb {1} _ {\sigma}, \quad V _ {\mathrm {L}} = - \sigma_ {3} = - i U _ {\mathrm {H W P}} (0), \tag {33} \\ \end{array}
$$

(HWP's at the entry and exit, nothing in the R branch, phase shifter and HWP in the L branch) realizes the swapping gate.

# C. Walsh-Hadamard gate

A Walsh-Hadamard gate turns the states of the standard basis into equal-weight superpositions,

$$
\begin{array}{l} S _ {\mathrm {W H}} (| \mathrm {R v} \rangle , | \mathrm {R h} \rangle , | \mathrm {L v} \rangle , | \mathrm {L h} \rangle) \\ = \left(| R v \rangle , | R h \rangle , | L v \rangle , | L h \rangle\right) \frac {1}{2} \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & - 1 & 1 & - 1 \\ 1 & 1 & - 1 & - 1 \\ 1 & - 1 & - 1 & 1 \end{array} \right), \tag {34} \\ \end{array}
$$

so that

$$
S _ {\mathrm {W H}} = \frac {1}{2} \left(\tau_ {1} + \tau_ {3}\right) \left(\sigma_ {1} + \sigma_ {3}\right),
$$

$$
S _ {\mathrm {R R}} = - S _ {\mathrm {L L}} = S _ {\mathrm {R L}} = S _ {\mathrm {L R}} = \frac {1}{2} \left(\sigma_ {1} + \sigma_ {3}\right). \tag {35}
$$

A simple realization is specified by

$$
V _ {1} = \mathbb {1} _ {\sigma}, \quad V _ {2} = - \mathbb {1} _ {\sigma},
$$

$$
\left. \begin{array}{l} V _ {\mathrm {R}} \\ V _ {\mathrm {L}} \end{array} \right\} = - \frac {1 \pm i}{2} \left(\sigma_ {1} + \sigma_ {3}\right) = - i \mathrm {e} ^ {\pm i \pi / 4} U _ {\mathrm {H W P}} (\pi / 8). \tag {36}
$$

This choice needs nothing in the entry port, a phase shifter in the exit port, and HWP plus phase shifter in each arm of the interferometer.

# D. Bell basis measurement

Another simple application is the measurement of the Bell basis, where we find the 2-qubit photon in one of the four entangled superpositions

$$
\left| B _ {1} \right\rangle = 2 ^ {- 1 / 2} \left(\left| \mathrm {R v} \right\rangle - \left| \mathrm {L h} \right\rangle\right),
$$

$$
\left| B _ {2} \right\rangle = 2 ^ {- 1 / 2} \left(\left| \mathrm {R h} \right\rangle - \left| \mathrm {L v} \right\rangle\right),
$$

$$
\left| B _ {3} \right\rangle = 2 ^ {- 1 / 2} (\left| \mathrm {R h} \right\rangle + \left| \mathrm {L v} \right\rangle),
$$

$$
\left| B _ {4} \right\rangle = 2 ^ {- 1 / 2} \left(\left| \mathrm {R v} \right\rangle + \left| \mathrm {L h} \right\rangle\right). \tag {37}
$$

Since one can detect the states of the standard basis—namely  $|\mathsf{Rv}\rangle$ ,  $|\mathsf{Rh}\rangle$ ,  $|\mathsf{Lv}\rangle$ , and  $|\mathsf{Lh}\rangle$ —with the aid of polarizing beam splitters (PBS's), see Fig. 5, all one needs is a 2-qubit gate

![](images/09b07568752584e367da4741dc16f8bcf5ef5ba728a12a7e5f42ebadea7aa18a.jpg)  
FIG. 5. For a measurement of an arbitrary 2-qubit basis, consisting of the mutually orthogonal states  $|a\rangle$ ,  $|b\rangle$ ,  $|c\rangle$ , and  $|d\rangle$ , one first transforms it to the standard basis with the aid of an appropriate 2-qubit gate. The output is sent through PBS's that reflect vertically polarized photons and transmit horizontally polarized ones. A click of either one of the four photon detectors (symbolized by semicircles) is indicative of the respective input state.

that turns the Bell basis into the standard one,

$$
S _ {\text {B e l l}} \left(\left| B _ {1} \right\rangle , \left| B _ {2} \right\rangle , \left| B _ {3} \right\rangle , \left| B _ {4} \right\rangle\right) = \left(\left| \mathrm {R v} \right\rangle , \left| \mathrm {R h} \right\rangle , \left| \mathrm {L v} \right\rangle , \left| \mathrm {L h} \right\rangle\right). \tag {38}
$$

Thus the ingredients

$$
S _ {\text {B e l l}} = 2 ^ {- 1 / 2} \left(\mathbb {1} _ {\tau} \right\rbrack_ {\sigma} - i \tau_ {2} \sigma_ {1}),
$$

$$
S _ {\mathrm {R R}} = S _ {\mathrm {L L}} = 2 ^ {- 1 / 2} \rbrack_ {\sigma}, \quad S _ {\mathrm {L R}} = - S _ {\mathrm {R L}} = 2 ^ {- 1 / 2} \sigma_ {1} \tag {39}
$$

are required. They are supplied by  $V_{1} = V_{2} = \mathbb{1}_{\sigma}$  in conjunction with

$$
V _ {R} = 2 ^ {- 1 / 2} \left(1 _ {\sigma} - i \sigma_ {1}\right) = U _ {Q W P} (\pi / 4),
$$

$$
V _ {\mathrm {L}} = 2 ^ {- 1 / 2} \left(\mathbb {1} _ {\sigma} + i \sigma_ {1}\right) = U _ {\mathrm {Q W P}} (- \pi / 4), \tag {40}
$$

for example, where one has just two QWP's inside the interferometer, one in each branch, and nothing in the entry and exit ports.

We note that an alternative way—one of many—of measuring the Bell basis is stated by

$$
\begin{array}{l} 2 ^ {- 1 / 2} \left(\tau_ {1} + \tau_ {3}\right) S _ {\text {s w a p}} S _ {\text {c n o t}, \sigma \rightarrow \tau} \left( \right.\left| \right. B _ {4} \left. \right\rangle , \left| \right. B _ {3} \left. \right\rangle , \left| \right. B _ {1} \left. \right\rangle , - \left| \right. B _ {2} \left. \right\rangle\left. \right) \\ = (| \mathrm {R v} \rangle , | \mathrm {R h} \rangle , | \mathrm {L v} \rangle , | \mathrm {L h} \rangle), \tag {41} \\ \end{array}
$$

where the permutation of the Bell states is irrelevant in the present context. This measurement could be realized by a sequence of unitary transformations: first a controlled-NOT gate (with  $\nu / \hbar$  controlling  $\mathsf{R} / \mathsf{L}$ ), then a swapping gate, finally a Walsh-Hadamard gate acting solely on the  $\mathsf{R} / \mathsf{L}$  qubit; each of the three gates would require a Mach-Zehnder interferometer. But rather than having three successive interferometers we can equivalently use a single one, because any unitary 2-qubit gate can be realized by the setup of Fig. 3, as shown in Sec. II C.

# IV. ADVANCED APPLICATIONS

# A. State diagnosis

As pointed out in the Introduction, we can measure any given 2-qubit observable if we manage to detect its eigenstate basis, consisting of the mutually orthogonal 2-qubit states  $|a\rangle$ ,  $|b\rangle$ ,  $|c\rangle$ , and  $|d\rangle$ , say. This is done, see Fig. 5, by mapping it onto the standard basis. And, of course, it doesn't matter if this mapping involves additional phase factors. All one needs are transitions such as  $|a\rangle \langle a| \rightarrow |\mathsf{Rv}\rangle \langle \mathsf{Rv}|$ . In this context it is expedient to introduce two 2-qubit operators in accordance with

$$
A \equiv | a \rangle \langle a | + | b \rangle \langle b | - | c \rangle \langle c | - | d \rangle \langle d |,
$$

$$
B \equiv | a \rangle \langle a | - | b \rangle \langle b | + | c \rangle \langle c | - | d \rangle \langle d |, \tag {42}
$$

so that  $|a\rangle, \ldots, |d\rangle$  are the joint eigenkets of  $A$  and  $B$  with eigenvalues  $A' = B' = +1, \ldots, A' = B' = -1$ , respectively. The essential property of the unitary gate in Fig. 5 is then the mapping of  $A$  and  $B$  onto  $\tau_3$  and  $\sigma_3$ ,

$$
S A = \tau_ {3} S, \quad S B = \sigma_ {3} S. \tag {43}
$$

For example, the operators  $A = -\tau_{1}\sigma_{1}$  and  $B = \tau_{2}\sigma_{2}$  are associated with the Bell basis (37), and one verifies Eq. (43) for  $S_{\mathrm{Bell}}$  of Eq. (38) easily.

Permutation of the basis states  $|a\rangle, \ldots, |d\rangle$  have no effect on the basis as a whole. Therefore, one can interchange the roles of  $A$  and  $B$  in Eq. (43), or replace either one of them by their product  $AB = BA$ . The respective gates are equivalent—either one can be used to measure the basis in question—but some may be simpler to set up than others. This is illustrated by the unitary transformation of Eq. (41), which corresponds to  $A = \tau_1\sigma_1$  and  $B = \tau_3\sigma_3 = (-\tau_1\sigma_1)(\tau_2\sigma_2)$ .

The statistical operator of a general 2-qubit state needs 15 real parameters for its specification (see Ref. [9], for example). The measurement of the probabilities associated with one 2-qubit basis supplies 3 of the 15 parameters. Accordingly, the full diagnosis of the 2-qubit state of interest requires the measurement of at least 5 suitably chosen bases.

A convenient set of such bases is reported in Table I, where each basis is characterized by its  $A, B$  pair. These pairs identify five 2-qubit observables that are pairwise complementary and thus optimal in the sense of Wootters and Fields [10]. In the terminology of Brukner and Zeilinger [11], the five  $A$  and  $B$ 's are "a complete set of five pairs of complementary propositions."

Rather than using a minimal set of this kind, one could of course measure a larger set of observables. This was done by White et al. [12], who produced and studied polarization-entangled photon pairs—two qubits of the  $\nu / \hbar$  kind. To our knowledge, theirs was the first experiment in which a complete characterization of an entangled 2-qubit state was achieved.

TABLE I. A minimal set of five  $A, B$  pairs of 2-qubit observables. By measuring the corresponding 2-qubit bases, one determines all 15 parameters that specify the statistical operator of the given 2-qubit state. The third column shows the unitary gates  $S$  needed for the measurements, see Fig. 5. The last four columns report possible choices for  $V_{1}, V_{2}, V_{\mathrm{R}}$ , and  $V_{\mathrm{L}}$  that realize the respective  $S$ , see Fig. 3. The  $S$  of the first row is the Walsh-Hadamard gate of Eqs. (35);  $\varepsilon$  is a stand-in for  $\frac{1}{2}(1 + i)$ .  

<table><tr><td>A</td><td>B</td><td>S</td><td>V1</td><td>V2</td><td>VR</td><td>VL</td></tr><tr><td>τ1</td><td>σ1</td><td>1/2(τ1+τ3)(σ1+σ3)</td><td>lσ</td><td>-lσ</td><td>-ε(σ1+σ3)</td><td>-ε*(σ1+σ3)</td></tr><tr><td>τ2</td><td>σ2</td><td>1/2(lτ-iτ1)(lσ-iσ1)</td><td>ilσ</td><td>-i lσ</td><td>ε(lσ-iσ1)</td><td>ε*(lσ-iσ1)</td></tr><tr><td>τ3</td><td>σ3</td><td>1</td><td>lσ</td><td>lσ</td><td>lσ</td><td>lσ</td></tr><tr><td>τ1σ2</td><td>τ2σ3</td><td>1/2(l+τ2lσ-i lσ2+i τ2σ2)</td><td>lσ</td><td>lσ</td><td>lσ</td><td>-iσ2</td></tr><tr><td>τ2σ1</td><td>τ3σ2</td><td>1/2(l-i τ2lσ-i τ1σ1-i τ3σ1)</td><td>-i lσ</td><td>σ1</td><td>lσ</td><td>iσ1</td></tr></table>

# B. Grover search

In the present context of entangled 2-qubit states, Grover's problem [13] amounts to the following, see Fig. 6. Grover's gate applies either one of the four unitary operators

$$
G _ {1} = 1 - 2 | \mathrm {R v} \rangle \langle \mathrm {R v} | = \frac {1}{2} (1 - \tau_ {3}) \mathbb {1} _ {\sigma} - \mathbb {1} _ {\tau} \sigma_ {3} - \tau_ {3} \sigma_ {3}),
$$

$$
G _ {2} = 1 - 2 | \mathrm {R h} \rangle \langle \mathrm {R h} | = \frac {1}{2} (1 - \tau_ {3} ] _ {\sigma} + ] _ {\tau} \sigma_ {3} + \tau_ {3} \sigma_ {3}),
$$

$$
G _ {3} = \mathbb {1} - 2 | \mathsf {L v} \rangle \langle \mathsf {L v} | = \frac {1}{2} (\mathbb {1} + \tau_ {3} ] _ {\sigma} - \mathbb {1} _ {\tau} \sigma_ {3} + \tau_ {3} \sigma_ {3}),
$$

$$
G _ {4} = 1 - 2 | \mathrm {L h} \rangle \langle \mathrm {L h} | = \frac {1}{2} \left(\mathbb {I} + \tau_ {3} \mathbb {I} _ {\sigma} + \mathbb {I} _ {\tau} \sigma_ {3} - \tau_ {3} \sigma_ {3}\right) \tag {44}
$$

to any 2-qubit state, and one has to find out which one is actually acting without using the gate more than once.

The solution consists of three steps. First, we send a Rv photon through the Walsh-Hadamard gate of Sec. III C to produce the superposition

$$
\frac {1}{2} \left(\left| R v \right\rangle + \left| R h \right\rangle + \left| L v \right\rangle + \left| L h \right\rangle\right). \tag {45}
$$

Second, this is used as input for Grover's gate, and the output is

$$
\frac {1}{2} \left(- | R v \rangle + | R h \rangle + | L v \rangle + | L h \rangle\right) \quad \text {f o r} G _ {1},
$$

![](images/d1de6f096fe9877197540ceb86b3f9408b6ad4742a2c991d3c17035b936c4c98.jpg)  
FIG. 6. Scheme of an optical implementation of Grover's search among four possibilities. A photon in the 2-qubit state  $|\mathsf{Rv}\rangle$  enters a Walsh-Hadamard gate, then passes through the Grover gate, which performs either  $G_{1}$ ,  $G_{2}$ ,  $G_{3}$ , or  $G_{4}$ . The photon is detected in one of the standard basis states, after being processed by  $S_{G}$ , and each of the four final states corresponds uniquely to one of the four settings of the Grover gate. Such an experiment was performed recently by Kwiat et al. [3].

$$
\frac {1}{2} \left(\left| R v \right\rangle - \left| R h \right\rangle + \left| L v \right\rangle + \left| L h \right\rangle\right) \quad \text {f o r} G _ {2},
$$

$$
\frac {1}{2} \left(\left| R v \right\rangle + \left| R h \right\rangle - \left| L v \right\rangle + \left| L h \right\rangle\right) f o r G _ {3},
$$

$$
\frac {1}{2} \left(\left| R v \right\rangle + \left| R h \right\rangle + \left| L v \right\rangle - \left| L h \right\rangle\right) \quad \text {f o r} G _ {4}. \tag {46}
$$

Third, since these are four mutually orthogonal states, they can be mapped onto the standard basis states, as in Fig. 5, here with the unitary 2-qubit gate appropriate for  $A = -\tau_{3}\sigma_{1}$  and  $B = -\tau_{1}\sigma_{3}$  in Eq. (43), namely,

$$
S _ {\mathrm {G}} = \frac {1}{2} \left(\mathbb {1} - \tau_ {1} \right\rbrack_ {\sigma} - \mathbb {1} _ {\tau} \sigma_ {1} - \tau_ {1} \sigma_ {1}). \tag {47}
$$

Thus, a click of the Rh detector, say, would tell us that  $G_{2}$  was the case.

The choice

$$
i V _ {1} = - i V _ {2} = - V _ {\mathrm {L}} = \mathbb {I} _ {\sigma}, \quad V _ {\mathrm {R}} = \sigma_ {1} \tag {48}
$$

realizes  $S_{\mathrm{G}}$  and thus offers a rather simple single-photon implementation of Grover's search among four possibilities.

We note that Kwiat et al. have already performed an experiment of this kind [3]. These authors also discuss extensions to Grover searches among more than four possibilities.

# C. Vaidman-Aharonov-Albert puzzle

Fitting to the present context, we rephrase the intriguing puzzle introduced by Vaidman, Aharonov, and Albert (VAA) in Ref. [14] (and subsequently generalized by Ben-Menahem [15] and Mermin [16]): Chuck invites Doris to prepare two photons for him, photon 1 vertically polarized and photon 2 in any polarization state she'd like. He'll then perform a polarization measurement on photon 2, thereby measuring either one of the three Pauli operators  $\sigma_{1}$ ,  $\sigma_{2}$ , or  $\sigma_{3}$ , without, however, telling Doris which one of the three complementary measurements is actually done. Since Chuck's measurement destroys photon 2, he promises to mimic an ideal von Neumann measurement by turning the polarization of photon 1 from vertical to the one detected for

photon 2. Thereafter, Doris can measure any property of photon 1 allowed by quantum mechanics. Only after she did the measurement of her choosing, Chuck will tell Doris which one of the three polarization measurements he had performed, and he then challenges her to tell him the outcome of his measurement.

Readers who do not know as yet how Doris can meet Chuck's challenge—thereby doing the seemingly impossible: ascertain the values of three mutually complementary measurements—should try to figure it out themselves before reading on. There is a lesson here about the wonderful things entanglement can do for you.

Doris prepares the two photons in the entangled state

$$
2 ^ {- 1 / 2} \left(\left| (\mathrm {R v}) _ {1} \mathrm {v} _ {2} \right\rangle + \left| (\mathrm {L v}) _ {1} \mathrm {h} _ {2} \right\rangle\right). \tag {49}
$$

As shown in Fig. 7, this is achieved by processing one photon of a polarization-entangled pair emitted by a suitable source [17] in the polarization state

$$
2 ^ {- 1 / 2} \left(\left| v _ {1} v _ {2} \right\rangle + \left| h _ {1} h _ {2} \right\rangle\right). \tag {50}
$$

Upon sending photon 1 through a polarizing beam splitter and rotating the transmitted h polarization to v, the polarization entanglement is turned into an entanglement between the R/L degree of freedom of photon 1 and the v/h degree of freedom of photon 2, as described by the ket vector of Eq. (49). All of this happens during the first stage of the experiment sketched in Fig. 7.

At the second stage, Chuck does one of the three polarization measurements. If he measures  $\sigma_{1}$ , say, finding  $\pm 1$  leaves photon 1 in the state

$$
2 ^ {- 1 / 2} (| \mathrm {R v} \rangle \pm | \mathrm {L v} \rangle), \tag {51}
$$

and the subsequent change of its polarization from  $\mathsf{v}$  to  $\mathsf{v}\pm \mathsf{h}$  puts photon 1 into

$$
\left| 1 _ {\pm} \right\rangle \equiv \frac {1}{2} \left(\left| R v \right\rangle \pm \left| R h \right\rangle \pm \left| L v \right\rangle + \left| L h \right\rangle\right). \tag {52}
$$

Likewise, if Chuck measures  $\sigma_{2}$ , photon 1 will emerge from the second stage in one of the states

$$
\left| 2 _ {\pm} \right\rangle \equiv \frac {1}{2} \left(\left| \mathrm {R v} \right\rangle \pm i \left| \mathrm {R h} \right\rangle \mp i \left| \mathrm {L v} \right\rangle + \left| \mathrm {L h} \right\rangle\right), \tag {53}
$$

and a measurement of  $\sigma_3$  will produce

$$
| 3 _ {+} \rangle \equiv | R v \rangle \quad \text {o r} | 3 _ {-} \rangle \equiv | L h \rangle . \tag {54}
$$

Note that these six states are simply related to the Bell states of Eq. (37),

$$
\left| 1 _ {\pm} \right\rangle = 2 ^ {- 1 / 2} \left(\left| B _ {4} \right\rangle \pm \left| B _ {3} \right\rangle\right),
$$

$$
\left| 2 _ {\pm} \right\rangle = 2 ^ {- 1 / 2} \left(\left| B _ {4} \right\rangle \pm i \left| B _ {2} \right\rangle\right),
$$

$$
\left| 3 _ {\pm} \right\rangle = 2 ^ {- 1 / 2} \left(\left| B _ {4} \right\rangle \pm \left| B _ {1} \right\rangle\right). \tag {55}
$$

At the third stage, Doris measures the VAA basis that consists of the states defined by

![](images/fcbbdf6af5dec6b19c7eca3f559462c3cb1ab718558725c662d41f98b24e7295.jpg)  
FIG. 7. Proposed realization of the Vaidman-Aharonov-Albert thought experiment of Ref. [14]. It involves two photons (circled numbers) and consists of three stages (dashed boxes labeled by boxed-in numbers). In the first stage, Doris prepares two photons for Chuck. She uses polarization-entangled photons from a source of entangled photon pairs (SEPP). Photon 1 moves to the left and passes through a polarizing beam splitter. With a subsequent halfwave plate, Doris converts the transmitted, horizontally polarized, amplitude into vertical polarization. The photons are then no longer entangled in polarization. Instead, the polarization degree of freedom of photon 2 is now entangled with the spatial degree of freedom of photon 1. In the second stage, (a) Chuck measures the polarization of photon 2, either by distinguishing the linear polarizations v and h, or the linear polarizations  $\nu \pm \mathsf{h}$ , or the circular polarizations  $\nu \pm i\mathsf{h}$ . Suitably set wave plates enable him to choose between the three complementary polarization measurements. (b) Chuck then leaves a quantum record of his measurement result by changing the polarization of photon 1 from vertical to the just-detected polarization of photon 2. For this purpose he adjusts two sets of wave plates accordingly. In the third stage, with the aid of an appropriate unitary gate, such as the VAA gate specified by Eqs. (58), Doris measures the VAA basis (56) on photon 1. If Chuck then tells her which one of the three polarization measurements he did at the second stage, Doris can infer, with absolute certainty, the result he obtained.

$$
\left( \begin{array}{c} \langle V A A _ {1} | \\ \langle V A A _ {2} | \\ \langle V A A _ {3} | \\ \langle V A A _ {4} | \end{array} \right) = \frac {1}{2} \left( \begin{array}{c c c c} 1 & - i & 1 & 1 \\ 1 & i & - 1 & 1 \\ - 1 & i & 1 & 1 \\ - 1 & - i & - 1 & 1 \end{array} \right) \left( \begin{array}{c} \langle B _ {1} | \\ \langle B _ {2} | \\ \langle B _ {3} | \\ \langle B _ {4} | \end{array} \right). \tag {56}
$$

TABLE II. Probabilities for Doris's measurement of the VAA basis (at the third stage of Fig. 7) on the various states possibly prepared by Chuck (at the second stage).  

<table><tr><td rowspan="2">Doris 
finds</td><td colspan="6">Chuck prepares</td></tr><tr><td>|1+)</td><td>|1-)</td><td>|2+)</td><td>|2-)</td><td>|3+)</td><td>|3-)</td></tr><tr><td>{VAA1}</td><td>1/2</td><td>0</td><td>1/2</td><td>0</td><td>1/2</td><td>0</td></tr><tr><td>{VAA2}</td><td>0</td><td>1/2</td><td>0</td><td>1/2</td><td>1/2</td><td>0</td></tr><tr><td>{VAA3}</td><td>1/2</td><td>0</td><td>0</td><td>1/2</td><td>0</td><td>1/2</td></tr><tr><td>{VAA4}</td><td>0</td><td>1/2</td><td>1/2</td><td>0</td><td>0</td><td>1/2</td></tr></table>

The corresponding  $A, B$  pair of observables and their product,

$$
\begin{array}{l} A = \left| B _ {1} \right\rangle \left\langle B _ {4} \right| + i \left| B _ {2} \right\rangle \left\langle B _ {3} \right| - i \left| B _ {3} \right\rangle \left\langle B _ {2} \right| + \left| B _ {4} \right\rangle \left\langle B _ {1} \right| \\ = \frac {1}{2} \left(\tau_ {3} \mathbb {1} _ {\sigma} + \mathbb {1} _ {\tau} \sigma_ {3} + \tau_ {1} \sigma_ {2} - \tau_ {2} \sigma_ {1}\right), \\ \end{array}
$$

$$
\begin{array}{l} B = - i \left| B _ {1} \right\rangle \left\langle B _ {2} \right| + i \left| B _ {2} \right\rangle \left\langle B _ {1} \right| + \left| B _ {3} \right\rangle \left\langle B _ {4} \right| + \left| B _ {4} \right\rangle \left\langle B _ {3} \right| \\ = \frac {1}{2} \left(\tau_ {1} \rrbracket_ {\sigma} + \rrbracket_ {\tau} \sigma_ {1} - \tau_ {2} \sigma_ {3} + \tau_ {3} \sigma_ {2}\right), \\ \end{array}
$$

$$
\begin{array}{l} A B = \left| B _ {1} \right\rangle \left\langle B _ {3} \right| + i \left| B _ {2} \right\rangle \left\langle B _ {4} \right| + \left| B _ {3} \right\rangle \left\langle B _ {1} \right| - i \left| B _ {4} \right\rangle \left\langle B _ {2} \right| \\ = \frac {1}{2} \left(- \tau_ {2} \rrbracket_ {\sigma} + \rrbracket_ {\tau} \sigma_ {2} + \tau_ {1} \sigma_ {3} + \tau_ {3} \sigma_ {1}\right) = B A, \tag {57} \\ \end{array}
$$

permute the states of the Bell basis. The measurement of the VAA basis could, for example, employ a 2-qubit gate  $S_{\mathrm{VAA}}$  that maps  $A$  on  $\tau_3$  and  $B$  on  $\sigma_3$ , as in Eq. (43). One realization of this VAA gate is specified by

$$
V _ {1} = i \sigma_ {1} = U _ {\mathrm {H W P}} (- \pi / 4),
$$

$$
V _ {2} = \mathbb {1} _ {\sigma},
$$

$$
\begin{array}{l} V _ {\mathrm {R}} = \frac {1 - i}{\sqrt {8}} \left(\mathbb {1} _ {\sigma} + i \sigma_ {1} + i \sigma_ {2} - i \sigma_ {3}\right) \\ = \mathrm {e} ^ {- i \pi / 4} U _ {\mathrm {Q W P}} (0) U _ {\mathrm {Q W P}} (- \pi / 4), \\ \end{array}
$$

$$
\begin{array}{l} V _ {\mathrm {L}} = \frac {1}{\sqrt {2}} \left(\mathbb {1} _ {\sigma} + i \sigma_ {2}\right) \\ = U _ {\mathrm {Q W P}} (\pi / 4) U _ {\mathrm {Q W P}} (0) U _ {\mathrm {Q W P}} (- \pi / 4), \tag {58} \\ \end{array}
$$

which would need a HWP at the R entry, a phase shifter and two QWP's in one arm, three QWP's in the other arm, and nothing at the exit.

The probabilities listed in Table II are crucial in understanding how Doris infers the result of Chuck's polarization measurement. Suppose, for instance, that the Lv detector clicked, so that Doris found photon 1 in state  $\langle VAA_3|$ . Then Chuck must have found  $+1$  if he measured  $\sigma_{1}$ , and  $-1$  if he measured  $\sigma_{2}$  or  $\sigma_{3}$ . The VAA basis (56) is, of course, chosen such that there are enough entries “0” in Table II.

# V. SUMMARY AND OUTLOOK

We showed how one can manipulate, and thus study, entangled qubit pairs that are physically represented by single photons. One qubit is encoded in the polarization, the other in a spatial alternative of the photon. By purely optical means, one can perform arbitrary unitary transformations on the qubit pair, so that any 2-qubit observable can be measured. Potential applications include the complete diagnosis of the entangled 2-qubit state supplied by some source and the experimental realization of a laboratory version of the Vaidman-Aharonov-Albert thought experiment.

The combined possibilities of performing any desired unitary transformation and of measuring any observable of one's liking enables one to use qubit pairs for other purposes as well. In particular, any unitary 2-qubit gate is equivalent to a four-way interferometer with certain relative phases between the four partial amplitudes of certain strengths. Therefore, a systematic quantitative study of fourway interferometers—that might ask questions concerning wave-particle duality, for example—could be done with single photons and 2-qubit gates of the kinds we discussed above.

Finally, we note that the setup of Fig. 7—the optical realization of the VAA thought experiment—could be used for the purposes of quantum cryptography. Chuck, who would now control stages 1 and 2, sends single photons to Doris, each photon in one of the six 2-qubit product states of Eqs. (55) (which, incidentally, could be produced by different methods as well). Doris, whose equipment would consist of the VAA gate and the photon detectors in stage 3 of Fig. 7, measures the VAA basis for each photon. After receiving public word from Chuck on which one of the three measurements he performed at stage 2a, Doris infers his measurement results. In this way, a random bit sequence is established that can serve as a cryptographic key. These matters are beyond the scope of the present paper and will be discussed elsewhere [18].

# ACKNOWLEDGMENTS

B.G.E. would like to thank Y. Aharonov for highly stimulating and most enjoyable discussions. We are grateful for the insights gained in conversations with H.-J. Briegel.

# APPENDIX: CONCERNING EQUATIONS (20)

Equations (19) state  $S^{\dagger}S = 1$  more explicitly. Likewise  $SS^{\dagger} = 1$  requires

$$
\begin{array}{l} S _ {\mathrm {R R}} S _ {\mathrm {R R}} ^ {\dagger} + S _ {\mathrm {R L}} S _ {\mathrm {R L}} ^ {\dagger} = \mathbb {1} _ {\sigma}, \\ S _ {\mathrm {L R}} S _ {\mathrm {L R}} ^ {\dagger} + S _ {\mathrm {L L}} S _ {\mathrm {L L}} ^ {\dagger} = \mathbb {1} _ {\sigma}, \\ S _ {\text {R R}} S _ {\text {L R}} ^ {\dagger} + S _ {\text {R L}} S _ {\text {L L}} ^ {\dagger} = 0, \\ S _ {\mathrm {L R}} S _ {\mathrm {R R}} ^ {\dagger} + S _ {\mathrm {L L}} S _ {\mathrm {R L}} ^ {\dagger} = 0, \tag {A1} \\ \end{array}
$$

of which the last two are adjoints of each other. We recall that, in a finite-dimensional Hilbert space as is the case here,

the self-adjoint products  $X^{\dagger}X$  and  $XX^{\dagger}$  are unitarily equivalent for any operator  $X$ . When applied to  $X = S_{\mathrm{LR}}$ , the first line in Eqs. (19) and the second line in Eqs. (A1) imply that  $S_{\mathrm{RR}}^{\dagger}S_{\mathrm{RR}}$  and  $S_{\mathrm{LL}}S_{\mathrm{LL}}^{\dagger}$  are unitarily equivalent. Upon denoting their common eigenvalues by  $(\cos \vartheta)^2$  and  $(\cos \theta)^2$ , the eigenkets of  $S_{\mathrm{RR}}^{\dagger}S_{\mathrm{RR}}$  by  $|\psi_{1,2}\rangle$  and those of  $S_{\mathrm{RR}}S_{\mathrm{RR}}^{\dagger}$  by  $|\bar{\psi}_{1,2}\rangle$ , the eigenkets of  $S_{\mathrm{LL}}^{\dagger}S_{\mathrm{LL}}$  by  $|\chi_{1,2}\rangle$ , and those of  $S_{\mathrm{LL}}S_{\mathrm{LL}}^{\dagger}$  by  $|\bar{\chi}_{1,2}\rangle$ , we then arrive at the first two lines of Eq. (20). In doing so, some relative phases have been absorbed in the global phases of the various kets and bras, but there remains the option to redefine them in accordance with

$$
\left| \psi_ {k} \right\rangle \longrightarrow \left| \psi_ {k} \right\rangle \mathrm {e} ^ {i \varphi_ {k}}, \quad \left| \overline {{\psi}} _ {k} \right\rangle \longrightarrow \left| \overline {{\psi}} _ {k} \right\rangle \mathrm {e} ^ {i \varphi_ {k}},
$$

$$
\left| \right. \chi_ {k} \left. \right\rangle\rightarrow \left| \right. \chi_ {k} \left. \right\rangle \mathrm {e} ^ {i \phi_ {k}}, \quad \left| \right. \bar {\chi} _ {k} \left. \right\rangle\rightarrow \left| \right. \bar {\chi} _ {k} \left. \right\rangle \mathrm {e} ^ {i \phi_ {k}}, \tag {A2}
$$

for  $k = 1,2$ , without affecting the first two lines of Eqs. (20).

Next, the second line of Eqs. (20) and the first line of Eqs. (A1) tell us that

$$
\begin{array}{l} S _ {\mathrm {R L}} ^ {\dagger} S _ {\mathrm {R L}} = \mathbb {1} _ {\sigma} - S _ {\mathrm {L L}} ^ {\dagger} S _ {\mathrm {L L}} \\ = \left| \chi_ {1} \right\rangle (\sin \vartheta) ^ {2} \left\langle \chi_ {1} \right| + \left| \chi_ {2} \right\rangle (\sin \theta) ^ {2} \left\langle \chi_ {2} \right|, \\ \end{array}
$$

$$
\begin{array}{l} S _ {\mathrm {R L}} S _ {\mathrm {R L}} ^ {\dagger} = 1 _ {\sigma} - S _ {\mathrm {R R}} S _ {\mathrm {R R}} ^ {\dagger} \\ = \left| \bar {\psi} _ {1} \right\rangle (\sin \vartheta) ^ {2} \left\langle \bar {\psi} _ {1} \right| + \left| \bar {\psi} _ {2} \right\rangle (\sin \theta) ^ {2} \left\langle \bar {\psi} _ {2} \right|, \tag {A3} \\ \end{array}
$$

with the consequence that  $S_{\mathrm{RL}}$  must be of the form

$$
i S _ {\mathrm {R L}} = \left| \bar {\psi} _ {1} \right\rangle \mathrm {e} ^ {- i \alpha} \sin \vartheta \left\langle \chi_ {1} \right| + \left| \bar {\psi} _ {2} \right\rangle \mathrm {e} ^ {- i \beta} \sin \theta \left\langle \chi_ {2} \right|, \tag {A4}
$$

where  $\alpha$  and  $\beta$  are phases that are undetermined as yet. Analogously, the first line of Eqs. (20) and the second line of Eqs. (A1) establish

$$
i S _ {\mathrm {L R}} = \left| \bar {\chi} _ {1} \right\rangle \mathrm {e} ^ {i \alpha} \sin \vartheta \left\langle \psi_ {1} \right| + \left| \bar {\chi} _ {2} \right\rangle \mathrm {e} ^ {i \beta} \sin \theta \left\langle \psi_ {2} \right|, \tag {A5}
$$

where the phase factors are fixed by the third and fourth equations in Eqs. (20) and (A1).

Now, the substitutions (A2) amount to

$$
\alpha \rightarrow \alpha + \varphi_ {1} - \phi_ {1}, \quad \beta \rightarrow \beta + \varphi_ {2} - \phi_ {2}, \tag {A6}
$$

in Eqs. (A4) and (A5). Therefore, the phase factors  $\mathrm{e}^{\mp i\alpha}$  and  $\mathrm{e}^{\mp i\beta}$  can be removed by a suitable redefinition of the kets and bras, and this turns Eqs. (A4) and (A5) into the last two lines of Eqs. (20).

[1] D. Boschi, S. Branca, F. De Martini, L. Hardy, and S. Popescu, Phys. Rev. Lett. 80, 1121 (1998).  
[2] M. Michler, R. Risco-Delgado, H. Bernstein, and H. Weinfurter, Remote State Preparation (Technical Digest, Glasgow, 1998), p. 99.  
[3] P. G. Kwiat, J. R. Mitchell, P. D. D. Schwindt, and A. G. White, J. Mod. Opt. 47, 257 (2000).  
[4] S. Takeuchi, Phys. Rev. A 61, 052302 (2000).  
[5] P. D. D. Schwindt, P. G. Kwiat, and B.-G. Englert, Phys. Rev. A 60, 4285 (1999).  
[6] M. Michler, H. Weinfurter, and M. Zukowski, Phys. Rev. Lett. 84, 5457 (2000).  
[7] M. Reck, A. Zeilinger, H. J. Bernstein, and P. Bertani, Phys. Rev. Lett. 73, 58 (1994).  
[8] Polarized Light (Benchmark Papers in Optics/1), edited by W. Swindell (Dowden, Hutchinson, and Ross, Stroudsburg, 1975).  
[9] N. Metwally and B.-G. Englert, J. Mod. Opt. 47, 2221 (2000).

[10] W. K. Wootters and B. D. Fields, Ann. Phys. (N.Y.) 191, 363 (1989).  
[11] C. Brukner and A. Zeilinger, Phys. Rev. Lett. 83, 3354 (1999).  
[12] A. G. White, D. F. V. James, P. H. Eberhard, and P. G. Kwiat, Phys. Rev. Lett. 83, 3103 (1999).  
[13] L. K. Grover, Phys. Rev. Lett. 79, 325 (1997).  
[14] L. Vaidman, Y. Aharonov, and D. Z. Albert, Phys. Rev. Lett. 58, 1385 (1987).  
[15] S. Ben-Menahem, Phys. Rev. A 39, 1621 (1989).  
[16] N. D. Mermin, Phys. Rev. Lett. 74, 831 (1995).  
[17] Bright and flexible sources of polarization-entangled photon pairs are available. See, e.g., P. G. Kwiat, E. Waks, A. G. White, I. Appelbaum, and P. H. Eberhard, Phys. Rev. A 60, 773 (1999).  
[18] A. Beige, B.-G. Englert, C. Kurtsiefer, and H. Weinfurter (unpublished).