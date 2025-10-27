# Modes and states in quantum optics

C. Fabre* and N. Treps†

Laboratoire Kastler Brossel, Sorbonne Université, ENS, CNRS, Collège de France, Campus Pierre et Marie Curie, 75005 Paris, France

![](images/9813bb0054b35c7477eb63311d2357d1eaaf9228917888cd85ec4424506b5429.jpg)

(published 10 September 2020)

A few decades ago, quantum optics stood out as a new domain of physics by exhibiting states of light with no classical equivalent. The first investigations concerned single photons, squeezed states, twin beams, and Einstein-Podolsky-Rosen states, which involve only one or two modes of the electromagnetic field. The study of the properties of quantum light then evolved in the direction of more and more complex and rich situations, involving many modes of the spatial, temporal, frequency, or polarization type. Actually, each mode of the electromagnetic field can be considered as an individual quantum degree of freedom. It is then possible, using the techniques of nonlinear optics, to couple different modes and thus build in a controlled way a quantum network [H. Jeff Kimble, Nature (London) 453, 1023 (2008)] in which the nodes are optical modes, and that is endowed with a strong multipartite entanglement. In addition, such networks can be easily reconfigurable and are subject only to weak decoherence. They indeed open many promising perspectives for optical communications and computation. Because of the linearity of Maxwell equations a linear superposition of two modes is another mode. This means that a "modal superposition principle" exists hand in hand with the regular quantum state superposition principle. The purpose of this review is to show the interest of considering these two aspects of multimode quantum light in a global way. Indeed, using different sets of modes allows one to consider the same quantum state under different perspectives: a given state can be entangled in one basis and factorized in another. It is shown that there exist some properties that are invariant over a change in the choice of the basis of modes. The method of finding the minimal set of modes that are needed to describe a given multimode quantum state is also presented. It is then shown how to produce, characterize, tailor, and use multimode quantum light while also considering the effect of loss and amplification on such light and the modal aspects of the two-photon coincidences. Switching to applications to quantum technologies, this review shows that it is possible to find not only quantum states that are likely to improve parameter estimation but also the optimal modes in which these states "live." Finally, details on how to use such quantum modal networks for measurement-based quantum computation are presented.

DOI: 10.1103/RevModPhys.92.035005

# CONTENTS

I. Introduction 2

II.Description of Classical Multimode Light 3

A. Mode of the electromagnetic field and mode basis: Definitions 3  
B. Hilbert space of modes 3  
C. Different mode bases for the electromagnetic field 3  
D. Transverse and longitudinal modes 4  
E. Modes and classical coherence 5

III. Description of Quantum Multimode Light 6

A. Electric field operator in any mode basis 6  
B. The two sides of quantum optics 7  
C. Single-photon states 7  
D. Multimode quantum states 8  
E.Quantum correlation matrices 8  
F.Mode basis change 9  
G. Intrinsic properties of multimode light states 9

IV. Search for Principal Modes 9  
V. Intrinsic Single-Mode States 10

A. Examples 11

1. Pure single-photon wave packet 11  
2. Single-photon statistical mixture 11  
3. Pure multimode coherent state 11  
4. Coherent state statistical mixture 11  
5. Two-photon pure state 12  
relation with classical optical coherence 12  
imple sufficient conditions for an intrinsic 12   
ngle-mode state

VI. Counting and Determining the Principal Modes 12

A. Case of spatial modes 12  
B. Case of temporal modes 13

VII. Multimode Gaussian States 13

A. Symplectic transformations 13  
B.Wigner function of a Gaussian state 14  
C. Gaussian state decomposition 14

1. Bloch-Messiah reduction 14  
2. Williamson reduction 14  
3.Pure Gaussian state 14  
4.Mixed Gaussian state 15  
5. Intrinsic separability 15

VIII. Multipartite Entanglement 15

IX. Sources of Multimode Nonclassical States 16

A.Mixture of single-mode nonclassical states 16

B. Parametric down-conversion 17

1. Interaction Hamiltonian 17  
2. Different possible modes for entangled states 17  
3.Use of resonant optical cavities 18  
4.Use of pump modes of different shapes 18  
5. Above threshold operation 18

C. Four-wave mixing 19  
D. Multimode lasers 19

X.Detection of Multimode Quantum States 19

A. Direct photodetection 19  
B. Balanced homodyne detection 20

C. Determination of quadrature covariance and coherency matrix elements 20

D. Spectral homodyne and resonator detection 21  
E. Multiplexed detection 21

1. Implementation 21  
2. Multiplexed homodyne signal 22

3. Multiplexed mode discrimination via postprocessing 22

F. Two-photon detection 23

XI. Multimode Amplification and Attenuation 23

A. Effect on squeezing 23  
B. Effect on entanglement 24

XII.Mode Shape Control 24

A.Linear conversion 25  
B.Nonlinear conversion 25

XIII. Mode Optimization in Parameter Estimation 26

XIV. Modes and States in Quantum Information Processing 28

A. Measurement-based quantum computing 28  
B. Cluster states: Concepts and experimental implementation 28  
C.Non-Gaussian cluster states 29

XV. Conclusion 30  
Acknowledgments 30  
Appendix A: Counting Spatial Modes in Laser Beams 30  
Appendix B: Counting Modes in Parametric Down-Converted Light 31  
Appendix C: Modal Dependence of the Coincidence Rate in the Hong-Ou-Mandel Experiment 31  
References 32

# I. INTRODUCTION

Modes of the electromagnetic field have always been an important tool for both theory and applications, helping physicists to describe and use subtle properties of light. For example, optical telecommunications, in an effort to further increase the number of degrees of freedom used to encode information in a single beam of light, was led to the multiplexing of more and more optical modes, successively temporal modes, frequency modes, and transverse modes.

Early research in quantum optics concentrated on simple nonclassical states of light, like single photons, squeezed states, twin beams, and Einstein-Podolsky-Rosen (EPR) states, that involve only one or two modes of the electromagnetic field. Then quantum states involving more and more quantum degrees of freedom were considered. This was implemented either by increasing the size of the Fock state basis in a given mode (which is not the subject of this review) or by increasing the number of modes on which the quantum state extends, with these modes being spatial modes for the study the quantum properties of optical images, or

time-frequency modes to investigate the quantum properties of light pulses.

In addition to the intrinsic interest in exploring further the quantum aspects of light in all of its manifestations, the study of highly multimode quantum light is of significant interest in the perspective of applications in the domains of quantum technologies. For example, to be competitive with present classical computers, the future quantum computer will necessarily make use of quantum states displaying entanglement between many degrees of freedom, and multimode quantum states of light are promising candidates to achieve this goal.

This review aims at characterizing from a general perspective the numerous specific features and interests of multimode quantum light. Indeed, quantum optics, as the child of optics and quantum mechanics, has inherited a double linearity: that of Maxwell equations, for which optical modes form a basis of solutions, and that of quantum mechanics, which involves bases of quantum states. One is naturally led to use two "intertwined" Hilbert spaces to describe multimode quantum light: that of modes and that of quantum states. The properties of single-photon quantum states, for example, are intimately related to the characteristics of the mode in which they are defined.

The specific approach of this review is to consider these two intricate aspects of quantum light on an equal footing. Note that in a given physical system there are many possible bases of optical modes: one has the choice of the basis of modes used to describe it. Using different sets of modes allows us to consider the same quantum state under different perspectives: for example, a given quantum state can be entangled in one basis and factorized in another. One can also derive and use the basis of so-called normal modes or look for "principal modes," which contain most information in the multimode system.

We show later that there exist some properties that are invariant over a change in the choice of the basis of modes, like nonclassicality, negativity of the Wigner function, and total photon number. We also present the method of finding the minimal set of modes that are needed to describe a given multimode quantum state, a tool to reduce the size of the Hilbert space of the system. We describe how to use modal noise correlation matrices to extract principal modes that concentrate and simplify the relevant information over complicated multimode states, especially (but not only) in the case of Gaussian noise. We show that there always exists a mode basis on which multimode entangled Gaussian states, pure or mixed, are separable. We detail the different detection techniques allowing experimentalists to determine such correlation matrices, as well as the ways to generate multimode light and tailor the spatiotemporal shapes of the modes. The effect of loss and of amplification on multimode nonclassical light is also presented. Switching to applications to quantum technologies, we show that it is possible to find not only quantum states that are likely to improve parameter estimation but also the optimal modes in which these states "live." Finally, we show how to use such quantum modal networks for measurement-based quantum computation.

This review deals with both discrete variables and continuous variables, with an emphasis on the latter, i.e., on the properties of quantum field fluctuations. In addition, we do not treat polarization or angular momentum modes, which have been the subject of intense research (Korolkova et al.,

2002; Allen, Barnett, and Padgett, 2016). We do not treat the multimodal aspects of light matter interaction either (Nunn et al., 2008; Afzelius et al., 2009). We are more interested in "scalable" properties, i.e., features that can be readily extended to large numbers of modes, than in two-mode systems. Even with these restrictions, the domain is vast and the object of numerous theoretical and experimental investigations, so we do not claim to present in this review an exhaustive account of it and describe what we consider the most striking features of the domain. There are already a number of papers and books that cover parts of this domain (Simon, Mukunda, and Dutta, 1994; Adesso and Illuminati, 2007a; Grynberg, Aspect, and Fabre, 2010; Braunstein and Pati, 2012; Weedbrook et al., 2012; Adesso, Ragy, and Lee, 2014; Furusawa, 2015; Ou, 2017; Ansari et al., 2018; Bruss and Leuchs, 2019; Korolkova and Leuchs, 2019), but, to our knowledge, no fully comprehensive presentations of it.

# II. DESCRIPTION OF CLASSICAL MULTIMODE LIGHT

In this review, we use the complex representation, or analytical signal,  $E^{(+)}(\boldsymbol{r}, t)$  of a classical electric field, such as the real field  $E(\boldsymbol{r}, t)$ , as a vector equal to  $E^{(+)}(\boldsymbol{r}, t) + (E^{(+)}(\boldsymbol{r}, t))^*$ .

# A. Mode of the electromagnetic field and mode basis: Definitions

We will call mode of the electromagnetic field a vector field  $f_{1}(\boldsymbol{r},t)$  that is a normalized solution of Maxwell equations in vacuum. It satisfies the following three equations:

$$
\left(\Delta - \frac {1}{c ^ {2}} \frac {\partial^ {2}}{\partial t ^ {2}}\right) \boldsymbol {f} _ {1} (\boldsymbol {r}, t) = 0, \quad \nabla \cdot \boldsymbol {f} _ {1} (\boldsymbol {r}, t) = 0, \tag {1}
$$

and, at any time  $t$

$$
\frac {1}{V} \int_ {V} d ^ {3} r | f _ {1} (\boldsymbol {r}, t) | ^ {2} = 1, \tag {2}
$$

with  $V$  the large volume that contains the entire physical system under consideration.

Starting from a given mode, which can have any shape in space and time provided that it fulfills Eq. (2), one can always build an orthonormal mode basis  $\{\pmb{f}_m(\pmb{r},t)\}$  on which one can decompose any solution of the Maxwell equations and which has the function  $\pmb{f}_1(\pmb{r},t)$  as its first element. Another way of generating a mode basis is to constrain the solutions of Maxwell equations by specific boundary conditions, for example, in a resonator.

As we have restricted ourselves to the case where the field of interest is enclosed in a spatial box of size  $V$ , this basis is discrete and can be labeled by a set of integers globally named as  $m$  so that one can write any complex field  $E^{(+)}(r, t)$  as

$$
\boldsymbol {E} ^ {(+)} (\boldsymbol {r}, t) = \sum_ {m} \mathcal {E} _ {m} \boldsymbol {f} _ {m} (\boldsymbol {r}, t), \tag {3}
$$

with, at any time  $t$

$$
\frac {1}{V} \int_ {V} d ^ {3} r \boldsymbol {f} _ {m} ^ {*} (\boldsymbol {r}, t) \cdot \boldsymbol {f} _ {m ^ {\prime}} (\boldsymbol {r}, t) = \delta_ {m m ^ {\prime}}, \tag {4}
$$

with  $\mathcal{E}_m$  the complex amplitudes of the different modes that completely define a given field. It is often useful to consider the field quadratures  $E_{mX}$  and  $E_{mP}$  as the real and imaginary components of  $\mathcal{E}_m$ :

$$
\mathcal {E} _ {m} = E _ {m X} + i E _ {m P}. \tag {5}
$$

# B. Hilbert space of modes

Equation (3) shows that a given solution of Maxwell equations  $\pmb{E}^{(+)}(\pmb{r},t)$  can be considered as a vector belonging to a Hilbert space, called modal space, that we denote with an arrow  $\vec{E}$ :

$$
\vec {E} = \sum_ {m} \mathcal {E} _ {m} \vec {f} _ {m}, \tag {6}
$$

with the sum limited in practice to a finite number of modes  $N$ .  $\vec{f}_m$  is a unit vector in the modal space, i.e., a column vector of zeros except for a 1 at the  $m$ th position.  $\vec{E}$  is therefore the column vector  $(\mathcal{E}_1, \mathcal{E}_2, \ldots)^T$ , with  $T$  denoting the transposition operation in the modal Hilbert space. Note that the modal column vector  $\vec{f}_m$  and the electric field  $f_m(\boldsymbol{r}, t)$ , a function of  $\boldsymbol{r}$  and  $t$ , are two representations of the same physical mode. We thus often denote the mode as  $f_m$ , a notation independent of any representation.

The inner product is defined as

$$
\vec {F} ^ {T *} \cdot \vec {G} = \sum_ {m = 1} ^ {N} \mathcal {F} _ {m} ^ {*} \mathcal {G} _ {m}, \tag {7}
$$

with  $\vec{F}^{T*} = (\vec{F}^T)^*$  the line matrix dual of  $\vec{F}$ . The inner product is also equal to the spatial overlap between the two associated electric fields

$$
\vec {F} ^ {T *} \cdot \vec {G} = \frac {1}{V} \int_ {V} d ^ {3} r \mathbf {F} ^ {*} (\mathbf {r}, t) \cdot \mathbf {G} (\mathbf {r}, t). \tag {8}
$$

Note that the value of the inner product (8) does not depend on time.

In the following, we extend the notation with an arrow to other column vectors of dimension  $N$ , for example,  $\vec{\hat{A}}$ , of components  $\hat{A}_m$  that are quantum operators.  $\vec{\hat{A}}^T$  denotes the corresponding line vector of operators  $\hat{A}_m$ , the transposition operation  $T$  acting only in the modal space, leaving operators unchanged. In the same spirit that  $\vec{\hat{A}}^\dagger$  is the column vector of components  $\hat{A}_m^\dagger$ , the operation denoted by  $\dagger$  is used only for the Hilbert space of quantum operators.

# C. Different mode bases for the electromagnetic field

Now consider a modal unitary transformation  $U$  of complex components  $U_{n}^{m}$ , and define the modal vectors

$$
\vec {g} _ {n} = \sum_ {m = 1} ^ {N} U _ {n} ^ {m} \vec {f} _ {m}. \tag {9}
$$

It is easy to show that they form another complete set of orthonormal modal vectors (with  $\vec{g}_n^{T*} \cdot \vec{g}_{n'} = \delta_{n,n'}$ ), and hence a new basis on which any field can be expanded

$$
\boldsymbol {E} ^ {(+)} (\boldsymbol {r}, t) = \sum_ {n} \mathcal {G} _ {n} \boldsymbol {g} _ {n} (\boldsymbol {r}, t), \quad \vec {E} = \sum_ {n} \mathcal {G} _ {n} \vec {g} _ {n}. \tag {10}
$$

The introduction of modes here has been purely mathematical. It leaves us complete freedom of choice of the unitary transformation  $U$ , and therefore of the mode basis. The most widely used is the basis of plane wave modes, which is easy to handle mathematically but rather unphysical. There are other mode bases that better fit the light source and the optical system under consideration. Let us quote some of them:

- Spatial Hermite-Gauss modes are well suited for beams produced in cavities made of spherical mirrors. Laguerre-Gauss modes carrying orbital angular momentum are used in quantum information processing, in particular, in a quantum key distribution context (Mirhosseini et al., 2015).  
- Temporal or frequency Hermite-Gauss modes provide a convenient orthogonal basis for light pulses of any temporal or spectral shape (Brecht et al., 2015).  
- Tilted plane waves are used to describe "images," i.e., any field configuration in the transverse plane, perpendicular to the main propagation direction (Kolobov, 2006).

The choice of mode basis can be adapted to the detection process:

- The pixel mode basis is useful when one considers imaging devices such as a CCD camera or a photodiode array. It consists of spatial modes of constant value over the pixel area  $\delta x \times \delta x$  and zero outside. Such a basis is orthonormal but not complete.  
- The time bin basis is analogous to the previous one when one replaces space with time and is useful for analyzing temporal sequences.  
- In the same spirit, the frequency band basis consists of frequency bins of width  $\delta \nu$ , which is useful for analyzing broadband sources.  
- The sideband mode basis, consisting of sums of monochromatic frequency modes symmetrically disposed around a carrier frequency, is useful for describing the different Fourier components of a time-dependent signal; see Sec. X.C.

# D. Transverse and longitudinal modes

For simplicity, we now restrict our analysis to the case where the fields of interest are the superposition of plane waves having wave vectors close to a mean value  $\pmb{k}_0$  (paraxial approximation) and frequencies close to a central frequency  $\omega_0 = c|\pmb{k}_0|$  (narrow-band approximation) (Grynberg, Aspect, and Fabre, 2010). To simplify notation, we assume that  $\pmb{k}_0$  is parallel to the  $z$  axis. The electric field can be written as

$$
\boldsymbol {E} ^ {(+)} (\boldsymbol {r}, t) = e ^ {i \left(k _ {0} z - \omega_ {0} t\right)} \sum_ {m} \mathcal {F} _ {m} \boldsymbol {f} _ {m} (\boldsymbol {r}, t), \tag {11}
$$

where  $e^{i(k_0z - \omega_0t)}$  is the carrier plane wave and  $f_{m}(\boldsymbol{r},t)$  are the envelope functions of the different modes, which are slowly varying functions of time at the scale of the optical period and of the position at the scale of the wavelength.

We now further simplify our approach by restricting the set of unitary modal transformations  $U$  to the ones that are factorized in transverse and longitudinal factors; the polarization degree of freedom is unaffected. This allows us to use factorized modes  $f_{m}$ :

$$
\boldsymbol {f} _ {m} (\boldsymbol {r}, t) = \boldsymbol {\epsilon} _ {i} f _ {p} ^ {(T)} (x, y, z) f _ {r} ^ {(L)} (t, z), \tag {12}
$$

where  $\pmb{\epsilon}_i$  ( $i = 1, 2$ ) are two orthogonal polarization unit vectors in the  $x-y$  plane,  $f_p^{(T)}$  is the transverse (or spatial) part of the mode, and  $f_r^{(L)}$  is its longitudinal (or temporal) part, with  $m$  being a short notation for  $(i, p, r)$ .

To build a spatial mode basis, one can use any orthonormal set of functions of  $x$ ,  $y$  in the transverse plane  $f_{p}(x,y)$  provided that they vary slowly on the wavelength scale so that one can use the paraxial approximation. The mode functions  $f_{p}^{(T)}(x,y,z)$  for any value of  $z$  are deduced from their values at  $z = 0$ ,  $f_{p}^{(T)}(x,y,z = 0) = f_{p}(x,y)$  by the Huygens-Fresnel integral accounting for diffraction.

To build a temporal mode basis, one can use any set of functions of time  $t$ ,  $f_{r}(t)$  provided that they satisfy the slowly varying envelope approximation and temporal orthonormality relations with an integration time  $T$  longer than any other characteristic time of the problem. The longitudinal mode functions are then  $f_{r}^{(L)}(t,z) = f_{r}(\tau = t - z / c)$ , describing undistorted pulses in the reference frame propagating at the velocity of light in the  $z$  direction.

The three factors in Eq. (12) correspond to three different kinds of quantum multimode effects: polarization effects, spatial effects, and temporal effects. They appear here as decoupled because of our simplifying assumptions. We do not detail the quantum properties linked to the polarization of light, or, in particular, the modes carrying orbital and polarization angular momentum. They are treated in detail by Korolkova et al. (2002) and Allen, Barnett, and Padgett (2016). In this review we consider a single polarization component, drop the polarization index  $i$ , and work with scalar modes. Such a description in terms of decoupled spatial and temporal modes is convenient when one treats problems in which the temporal shape of light does not modify its transverse properties or when diffraction does not modify the pulse shape. Self-focusing effects, in either space or time, or objects like  $X$  waves (Gatti et al., 2009; Jedrkiewicz et al., 2012) would clearly need a more elaborate approach.

When a single temporal mode  $f_{1}^{(L)}(t,z)$  is involved, the electric field is written as

$$
\boldsymbol {E} ^ {(+)} (\boldsymbol {r}, t) = \epsilon_ {1} e ^ {i (k _ {0} z - \omega_ {0} t)} f _ {1} ^ {(L)} (\tau) \sum_ {p} \mathcal {E} _ {p} f _ {p} ^ {(T)} (\boldsymbol {r}). \tag {13}
$$

Omitting the factor in front of the sum, one defines the transverse electric field as

$$
E _ {T} ^ {(+)} (x, y, z) = \sum_ {p} \mathcal {E} _ {p} f _ {p} ^ {(T)} (x, y, z). \tag {14}
$$

Its Fourier transform in transverse wave vector space  $\tilde{E}_T^{(+)}(k_x,k_y)$  can also be expanded on the basis of  $k_{x}$  and  $k_{y}$  dependent modes  $\tilde{f}_p^{(T)}(k_x,k_y)$ :

$$
\tilde {E} _ {T} ^ {(+)} \left(k _ {x}, k _ {y}\right) = \sum_ {p} \tilde {\mathcal {E}} _ {p} \tilde {f} _ {p} ^ {(T)} \left(k _ {x}, k _ {y}\right). \tag {15}
$$

It is independent of  $z$ , as diffraction does not modify the distribution of transverse wave vectors. Transverse modes are well suited to the description of quantum imaging problems (Kolobov, 2006), i.e., the quantum properties of the transverse distribution of light, for example, quantum correlations between different points of the transverse plane.

In a symmetrical way, when a single spatial mode  $f_{1}^{(T)}(\boldsymbol{r})$  is involved, the electric field is written as

$$
\boldsymbol {E} ^ {(+)} (\boldsymbol {r}, t) = \epsilon_ {1} e ^ {- i \omega_ {0} \tau} f _ {1} ^ {(T)} (\boldsymbol {r}) \sum_ {r} \mathcal {E} _ {r} f _ {r} ^ {(L)} (\tau). \tag {16}
$$

This allows us to define the temporal or longitudinal field as

$$
E _ {L} ^ {(+)} (t, z) = \sum_ {r} \mathcal {E} _ {r} f _ {r} ^ {(L)} (\tau). \tag {17}
$$

Its Fourier transform  $\tilde{E}_L^{(+)}(\omega)$  can be expanded on a basis of frequency modes  $\tilde{f}_r^{(L)}(\omega)$ :

$$
\tilde {E} _ {L} ^ {(+)} (\omega) = \sum_ {r} \tilde {\mathcal {E}} _ {r} \tilde {f} _ {r} ^ {(L)} (\omega). \tag {18}
$$

Temporal and frequency modes are well suited to the quantum description of light pulses and of their correlations. Frequency combs are an important case. They can be expanded on the basis of monochromatic waves of equally spaced frequencies or, in the time domain, as trains of identical pulses equally spaced in time.

# E. Modes and classical coherence

Note that if the classical field under study is totally defined, i.e., perfectly coherent, in both time and space, its normalized spatiotemporal shape can be taken as a first mode of a mode basis, and the decomposition (3) comprises a single term: any perfectly coherent classical field is single mode in essence. This is the case, for example, for a mode-locked laser in which the relative phases between the different frequency modes are fixed.

But in most practical cases the field is not perfectly mastered: it has some degree of randomness or "incoherence" in the form of amplitude and phase fluctuations at any point of space and time. In this situation, the complex coefficients  $\mathcal{E}_m$  in Eq. (3) are stochastic quantities. This is the case, for example, for a multimode cw laser in which the phases of each individual frequency component are randomly fluctuating. The classical fluctuations of the field have no reason to be described by a single fluctuating amplitude  $\mathcal{E}_1$ , so a full decomposition of the form of Eq. (3) is indeed needed, and the degree of coherence of the field is characterized by the probability distributions of the complex amplitudes  $\mathcal{E}_m$  and by the correlations existing between different amplitudes  $\mathcal{E}_m$  and  $\mathcal{E}_{m'}$ .

Among the quantities that are used to characterize the degree of coherence of a classical stochastic field, we

use in this review the following matrices characterizing its fluctuations:

(1) The first-order coherency matrix  $\Gamma^{(1)}$  (Wiener, 1928), defined by

$$
\left(\boldsymbol {\Gamma} ^ {(1)}\right) _ {m, n} = \overline {{\mathcal {E} _ {m} ^ {*} \mathcal {E} _ {n}}}, \quad \boldsymbol {\Gamma} ^ {(1)} = \overline {{\vec {E} \vec {E} ^ {T *}}}, \tag {19}
$$

with the bar indicating an ensemble average. This allows us to determine the cross-correlation function for the field amplitudes (Barakat, 1963):

$$
\begin{array}{l} G ^ {(1)} \left(\boldsymbol {r}, \boldsymbol {r} ^ {\prime}, t, t ^ {\prime}\right) = \overline {{E ^ {(+) *} \left(\boldsymbol {r} ^ {\prime} , t ^ {\prime}\right) E ^ {(+)} (\boldsymbol {r} , t)}} (20) \\ = \sum_ {m, n} \left(\boldsymbol {\Gamma} ^ {(1)}\right) _ {m, n} f _ {m} ^ {*} \left(\boldsymbol {r} ^ {\prime}, t ^ {\prime}\right) f _ {n} (\boldsymbol {r}, t). (21) \\ \end{array}
$$

The coherency matrix has been extensively studied in the context of polarization modes (Réfrégier and Goudail, 2005) and imaging (Yamazoe, 2012).

(2) The quadrature covariance matrix  $\Gamma_{Q}$ . Define

$$
\vec {Q} = \left(E _ {1 X}, E _ {2 X}, \dots , E _ {N X}, E _ {1 P}, E _ {2 P}, \dots , E _ {N P}\right) ^ {T}, \tag {22}
$$

the column vector containing all field quadratures. The quadrature covariance matrix  $\Gamma_{Q}$ , which we refer to in short as the covariance matrix, is the real  $2N\times 2N$  matrix defined on a given mode basis  $\{\vec{f}_n\}$  as

$$
\boldsymbol {\Gamma} _ {Q} = \overline {{\vec {Q} \vec {Q} ^ {T}}}. \tag {23}
$$

It contains all second moments of the different modes  $\overline{E_{mX}^2}$  and  $\overline{E_{mP}^2}$  on the diagonal, and outside the diagonal all quadrature correlations  $\overline{E_{mX}E_{nX}}$ ,  $\overline{E_{mP}E_{nP}}$ , and  $\overline{E_{mX}E_{nP}}$ .

The quadrature covariance matrix is a symmetric real matrix of size  $2N \times 2N$ , where  $N$  is the number of modes, whereas the coherency matrix is Hermitian of size  $N \times N$ . If all of the modes have fluctuations with Gaussian statistics and zero mean, then the quadrature coherence matrix contains all of the physical information about the system, which is not the case for the first-order coherency matrix.

The  $N\times N$  coherency matrix can be deduced from the  $2N\times 2N$  quadrature covariance matrix using the relations

$$
\begin{array}{l} \left(\Gamma^ {(1)}\right) _ {m, n} = \overline {{E _ {m X} E _ {n X}}} + \overline {{E _ {m P} E _ {n P}}} \\ + i \left(\overline {{E _ {m X} E _ {n P}}} - \overline {{E _ {m P} E _ {n X}}}\right). \tag {24} \\ \end{array}
$$

In contrast, one cannot determine the quadrature covariance matrix from the coherency matrix. This matrix gives information about the distribution of energy among the different modes, but not the way that it is distributed between the two quadratures inside a given mode.

# III. DESCRIPTION OF QUANTUM MULTIMODE LIGHT

Now consider quantum fields in vacuum and start with the usual approach of quantum electrodynamics (Cohen-Tannoudji, Dupont Roc, and Grynberg, 1987; Mandel and Wolf, 1995; Grynberg, Aspect, and Fabre, 2010), which consists of introducing the electric field operator in the Heisenberg representation  $\hat{E}^{(+)}(r,t)$  as the quantum extension of the classical complex field  $E^{(+)}(r,t)$ , and expand it to the basis of monochromatic plane wave modes  $\pmb{u}_{\ell}(\pmb {r},t)$ :

$$
\hat {\boldsymbol {E}} ^ {(+)} (\boldsymbol {r}, t) = \sum_ {\ell} \mathcal {E} _ {\ell} ^ {(1)} \hat {a} _ {\ell} \boldsymbol {u} _ {\ell} (\boldsymbol {r}, t),
$$

$$
\boldsymbol {u} _ {\ell} (\boldsymbol {r}, t) = \boldsymbol {\epsilon} _ {\ell} e ^ {i \left(\boldsymbol {k} _ {\ell} \cdot \boldsymbol {r} - \omega_ {\ell} t\right)}, \quad \mathcal {E} _ {\ell} ^ {(1)} = \sqrt {\frac {\hbar \omega_ {\ell}}{2 \varepsilon_ {0} V}}, \tag {25}
$$

where  $\pmb{\epsilon}_{\ell}$  is a unit polarization vector,  $\hat{a}_{\ell}$  is the annihilation operator of a photon in the plane wave mode, and  $\mathcal{E}_{\ell}^{(1)}$  is the single-photon electric field. The set of plane wave modes  $\{\pmb{u}_{\ell}(\pmb{r},t)\}$  satisfies the orthonormality condition (4) and the equal time completeness relation in space domain, valid at any time  $t$ :

$$
\sum_ {\ell} \boldsymbol {u} _ {\ell} ^ {*} (\boldsymbol {r}, t) \cdot \boldsymbol {u} _ {\ell} \left(\boldsymbol {r} ^ {\prime}, t\right) = 2 V \delta^ {(3)} \left(\boldsymbol {r} - \boldsymbol {r} ^ {\prime}\right), \tag {26}
$$

where  $\delta^{(3)}$  is the delta function in three-dimensional space.

Expansion (25) shows that the modal Hilbert space of classical electromagnetic fields can be mapped to a modal Hilbert space of quantum field operators so that one can write

$$
\vec {\hat {E}} = \sum_ {\ell} \mathcal {E} _ {\ell} ^ {(1)} \hat {a} _ {\ell} \vec {u} _ {\ell}. \tag {27}
$$

$\vec{E}$  is thus the column vector of operators  $\mathcal{E}_{\ell}^{(1)}\hat{a}_{\ell}$ . Note that the electric field quantum operator  $\hat{\pmb{E}}^{(+)}(\pmb {r},t)$  in the Heisenberg representation obeys Maxwell equations (1), which form the basis not only of classical electrodynamics but also of quantum electrodynamics.

# A. Electric field operator in any mode basis

We now perform a modal unitary transformation  $U$  on the set of creation operators  $\{\hat{a}_{\ell}^{\dagger}\}$ , yielding a new set of operators  $\{\hat{b}_m^\dagger\}$  given by

$$
\hat {b} _ {m} ^ {\dagger} = \sum_ {\ell} U _ {m} ^ {\ell} \hat {a} _ {\ell} ^ {\dagger}, \quad \vec {b} ^ {\dagger} = U \vec {a} ^ {\dagger}, \tag {28}
$$

where  $\vec{b}^{\dagger}$  and  $\vec{a}^{\dagger}$  are column vectors of components  $\hat{b}_m^\dagger$  and  $\hat{a}_{\ell}^{\dagger}$ . One also has

$$
\hat {a} _ {\ell} = \sum_ {m} U _ {m} ^ {\ell} \hat {b} _ {m}, \quad \vec {\hat {a}} = U ^ {T} \vec {\hat {b}}. \tag {29}
$$

Note that the mode  $\vec{u_l}$ , in its column vector representation, is associated with the single creation operator  $\hat{a}_l^\dagger$ , while the

mode basis  $\{\vec{u}_l\}$  is associated with the column vector of creation operators  $\vec{a}^\dagger$

The unitarity of matrix  $U$  ensures that

$$
[ \hat {b} _ {m}, \hat {b} _ {m ^ {\prime}} ^ {\dagger} ] = \delta_ {m, m ^ {\prime}} \quad \text {o r} \quad \vec {\hat {b}} (\vec {\hat {b}} ^ {\dagger}) ^ {T} - \vec {\hat {b}} ^ {\dagger} (\vec {\hat {b}}) ^ {T} = \mathbb {1} _ {N}, \tag {30}
$$

with  $\mathbb{1}_N$  being the identity matrix of dimension  $N$ . The operators  $\hat{b}_m$  are indeed bosonic operators, and the positive electric field operator in vacuum can now be written as a linear combination of the annihilation operators  $\hat{b}_m$  in a way similar to the decomposition (25) or (27):

$$
\hat {\boldsymbol {E}} ^ {(+)} (\boldsymbol {r}, t) = \sum_ {m} \mathcal {F} _ {m} ^ {(1)} \hat {b} _ {m} \boldsymbol {f} _ {m} (\boldsymbol {r}, t), \quad \vec {\hat {E}} = \sum_ {m} \mathcal {F} _ {m} ^ {(1)} \hat {b} _ {m} \vec {f} _ {m}. \tag {31}
$$

$\hat{b}_m$  is the annihilation operator of one photon in the normalized mode  $\pmb{f}_m(\pmb{r},t)$  (which we write more simply as  $\pmb{f}_m$ ), and the electric field per photon  $\mathcal{F}_m^{(1)}$  is given by

$$
\left(\mathcal {F} _ {m} ^ {(1)}\right) ^ {2} = \sum_ {\ell} \left(\mathcal {E} _ {\ell} ^ {(1)}\right) ^ {2} \left| U _ {m} ^ {\ell} \right| ^ {2}. \tag {32}
$$

The column vector  $\{\vec{f}_m\}$  contains a new set of modes on which the field is expanded. It is related to the plane wave basis by

$$
\vec {f} _ {m} = \frac {1}{\mathcal {F} _ {m} ^ {(1)}} \sum_ {\ell} \mathcal {E} _ {\ell} ^ {(1)} U _ {m} ^ {\ell} \vec {u} _ {\ell}. \tag {33}
$$

We have therefore shown how to write in the most general case the quantum field on any mode set  $\{\vec{f}_m\}$  and how to define the associated annihilation operators  $\hat{b}_m$ . Strictly speaking, because of the presence of the frequency-dependent scaling factor  $\mathcal{E}_{\ell}^{(1)}$  in the sum (33), these new modes are not necessarily orthogonal when their frequency spectrum is broad. They are indeed orthogonal when the unitary modal transformation  $\mathbf{U}$  mixes only plane waves oscillating at nearby frequencies  $\omega \simeq \omega_0$  (the narrow-band approximation studied in Sec. II.D), in which case  $\mathcal{F}_m^{(1)} = \mathcal{E}_{\ell}^{(1)}(\omega_0)$  so that one can simply write

$$
\vec {f} _ {m} = \sum_ {\ell} U _ {m} ^ {\ell} \vec {u} _ {\ell}. \tag {34}
$$

We note that in this case the transformation (34) for the mode shape and the transformation (9) for the creation operators are identical. Using Eq. (34), one easily shows that the completeness relation (26) also holds in this case in the new mode basis.

In a way related to Eq. (5), one can write the field operator (31) in terms of Hermitian dimensionless quadrature operators  $\hat{X}_m$  and  $\hat{P}_m$  in the different modes  $f_m$  such that

$$
\hat {b} _ {m} = (\hat {X} _ {m} + i \hat {P} _ {m}) / 2,
$$

$$
\vec {\hat {E}} = \sum_ {m} \mathcal {F} _ {m} ^ {(1)} \frac {\hat {X} _ {m} + i \hat {P} _ {m}}{2} \vec {f} _ {m},
$$

$$
\hat {X} _ {m} = \hat {b} _ {m} ^ {\dagger} + \hat {b} _ {m}, \quad \hat {P} _ {m} = i (\hat {b} _ {m} ^ {\dagger} - \hat {b} _ {m}), \tag {35}
$$

with  $[\hat{X}_m,\hat{P}_m] = 2i$ . The normalization has been chosen in such a way that the variance of vacuum fluctuations on any quadrature  $\hat{X}_m$  or  $\hat{P}_m$  is 1. We will also use quadrature operators in a rotated phase space  $\hat{X}_{m\phi}$  defined by

$$
\hat {X} _ {m \phi} = \hat {b} _ {m} ^ {\dagger} e ^ {i \phi} + \hat {b} _ {m} e ^ {- i \phi} = \hat {X} _ {m} \cos \phi + \hat {P} _ {m} \sin \phi . \tag {36}
$$

# B. The two sides of quantum optics

Consider again the quantum form of the modal decomposition of the electric field operator in vacuum

$$
\vec {\hat {E}} = \sum_ {m} \mathcal {F} _ {m} ^ {(1)} \hat {b} _ {m} \vec {f} _ {m}. \tag {37}
$$

It comprises the same modal functions  $\vec{f}_m$  as the classical decomposition (6), while the classical complex amplitudes have been replaced by quantum operators. Expression (37) thus exemplifies the intricate dual nature of light: the operatorial part  $\hat{b}_m$  relates it to the Hilbert space of quantum states, its Fock states basis, and their interpretation in terms of particles, while the modal part  $\vec{f}_m$  relates it to classical optics, to the modal Hilbert space of solutions of Maxwell equations, and to the wave aspect of light. These two aspects are intimately mixed (Xiao et al., 2017), as the annihilation operator  $\hat{b}_m$  is defined in the specific mode  $f_m$ , which provides the shape in time and space of the probability of detecting the photons.

A striking example of this intimate relation between modes and operators is provided by the following formula, deduced from Eq. (34), that relates the commutator of annihilation and creation operators  $\hat{b}_f$  and  $\hat{b}_g^\dagger$  associated with any two modes  $f$  and  $g$ , even nonorthogonal, to the overlap integral of these modes

$$
\left[ \hat {b} _ {f}, \hat {b} _ {g} ^ {\dagger} \right] = \frac {1}{V} \int d ^ {3} r \boldsymbol {f} (\boldsymbol {r}, t) \cdot \boldsymbol {g} ^ {*} (\boldsymbol {r}, t) = \vec {f} ^ {T *} \cdot \vec {g}. \tag {38}
$$

These considerations allow us to point out an important and unique feature of quantum optics, its double linearity, that of Maxwell equations and that of quantum mechanics. This allows us, thanks to the possibility of changing mode bases, to consider the same quantum state from different perspectives. This is not the case for other multimode systems like sets of material qubits: linear combinations of modes are other modes, whereas linear combinations of qubits carried by different systems are not simple physical objects.

It is well known that coherence is a fundamental notion for the physical domains involving waves: this is of course the case for classical optics (Goodman, 2015), but also for quantum mechanics. Coherence of matter waves, and more generally coherence in quantum physics, has even been

considered as a basic resource for quantum technologies (Streltsov, Adesso, and Plenio, 2017). The two coherences must not be confounded and must indeed be taken into consideration in a global way in the domain of quantum optics (Glauber, 1963; Mandel and Wolf, 1995). They both play important and intricate roles in multimode quantum optics, as we see more extensively later.

# C. Single-photon states

The bosonic operators  $\hat{b}_m$  allow us to define number operators  $\hat{N}_m = \hat{b}_m^\dagger \hat{b}_m$  and their eigenstates  $|n_m : \pmb{f}_m\rangle$ , where  $n_m$  is an integer, which are the number states in modes  $\pmb{f}_m(\pmb{r}, t)$ .

Call  $|0\rangle$  the vacuum state in the plane wave basis  $\{\pmb{u}_{\ell}\}$ , defined by  $\hat{a}_{\ell}|0\rangle = 0 \forall \ell$ . One has also from Eq. (9) and for all  $m$

$$
\hat {b} _ {m} | 0 \rangle = \sum_ {\ell} U _ {m} ^ {\ell *} \hat {a} _ {\ell} | 0 \rangle = 0. \tag {39}
$$

The same state  $|0\rangle$  is also the vacuum for the new mode basis  $\{f_m\}$ . This allows us to define the quantum state  $|1:f_m\rangle$  of a single-photon state in any mode  $f_{m}$ , and to express it in terms of plane wave single photons as

$$
\left| 1: \boldsymbol {f} _ {m} \right\rangle = \hat {b} _ {m} ^ {\dagger} | 0 \rangle = \sum_ {\ell} U _ {m} ^ {\ell} | 1: \boldsymbol {u} _ {\ell} \rangle . \tag {40}
$$

Note that the same unitary transformation  $U$  is used for the creation operators (9), for the mode shape (34), and for the single-photon state (40).

It is important to stress that a single-photon state  $|1:f_m\rangle$  does not describe a physical object that looks exactly like a classical particle because its properties depend on the mode in which it is defined. Photons are not simply "very small bodies emitted from shining substances" (Newton, 1704); they must instead be considered as the first excitation of mode  $f_{m}$  (Lamb, 1995). If the unitary transform  $U$  mixes modes of different frequencies, then the single-photon state is no longer an eigenstate of the Hamiltonian of energy  $\hbar \omega$ : it describes a nonstationary "single-photon wave packet" (Titulaer and Glauber, 1966); if the unitary transform  $U$  mixes modes of different wave vectors, the single-photon state is no longer an eigenstate of the momentum with eigenvalue  $\hbar \mathbf{k}$ : it describes a more complex single-photon waveform, for example, the dipole mode in which a single photon is spontaneously emitted by an excited atom (Cohen-Tannoudji, Dupont Roc, and Grynberg, 1987).

It is easy to show that one also has, for any two single-photon states associated with any two modes  $\vec{f}$  and  $\vec{g}$ ,

$$
\langle 1: \boldsymbol {f} | 1: \boldsymbol {g} \rangle = \frac {1}{V} \int_ {V} d ^ {3} r \boldsymbol {f} ^ {*} (\boldsymbol {r}, t) \cdot \boldsymbol {g} (\boldsymbol {r}, t) = \vec {f} ^ {T *} \cdot \vec {g}. \tag {41}
$$

When dealing with single-photon states, the quantum inner product is equal to the modal inner product. There is therefore an exact mapping between a single-photon quantum state  $|1:f\rangle$  and the corresponding spatiotemporal mode amplitude  $f(r,t)$  so that it is often convenient to consider  $f$  as the "wave

function" of the single photon (Bialynicki-Birula, 1996; Smith and Raymer, 2007).

It is also easy to derive from Eq. (38) the following useful relation:

$$
\hat {b} _ {\boldsymbol {f}} \left| 1: \boldsymbol {g} \right\rangle = \left(\vec {f} ^ {T *} \cdot \vec {g}\right) | 0 \rangle , \tag {42}
$$

where  $\hat{b}_f$  is the annihilation operator in mode  $f$ .

# D. Multimode quantum states

We can write the most general pure quantum state of light  $|\Psi \rangle$  in a given mode basis as

$$
\begin{array}{l} \left| \Psi \right\rangle = \sum_ {n _ {1}} \dots \sum_ {n _ {m}} \dots C _ {n _ {1}, \dots , n _ {m}, \dots} \left| n _ {1}: f _ {1} \right\rangle \\ \otimes \dots \otimes \left| n _ {m}: f _ {m} \right\rangle \otimes \dots . \tag {43} \\ \end{array}
$$

Knowing that  $|n_m: f_m\rangle = (\sum_{\ell} U_m^\ell \hat{a}_\ell^\dagger)^{n_m}|0\rangle / \sqrt{n_m!}$  and about Eqs. (9) and (29) it is straightforward to write  $|\Psi\rangle$  in terms of number states in any mode basis of our choice. This implies that to characterize a given multimode quantum state we have a new degree of freedom to play with, namely, the choice of mode basis, in addition to the choice of the quantum state basis.

Take as an example a quantum state spanning two modes  $f_{1}$  and  $f_{2}$ . Another possible mode basis consists of the symmetric and antisymmetric combinations  $f_{\pm} = (f_{1} \pm f_{2}) / \sqrt{2}$ . The quantum state

$$
| \psi \rangle = | 1: f _ {1} \rangle \otimes | 1: f _ {2} \rangle \tag {44}
$$

written in the first basis can also be written in the second basis, using Eq. (9), as

$$
| \psi \rangle = (| 2: f _ {+} \rangle \otimes | 0: f _ {-} \rangle - | 0: f _ {+} \rangle \otimes | 2: f _ {-} \rangle) / \sqrt {2}. \tag {45}
$$

$|\psi \rangle$  is therefore factorized in the first mode basis and entangled in the second. The same property holds for the two-mode continuous variable (CV) quantum state  $|\psi^{\prime}\rangle$ , which consists of a product of two equally squeezed vacuum states on basis  $(f_{1}, f_{2})$ . On basis  $(f_{+}, f_{-})$  it is an "EPR entangled state," like the one studied by Einstein, Podolsky, and Rosen (1935). In this context the fact that a quantum state is entangled or not depends on the choice of the mode basis (Thirring et al., 2011). This is due to the fact that the physical system we are interested in does not have a unique physical bipartition into an "Alice" part and a "Bob" part, all possible combinations of modes being treated on an equal footing. One can say that  $|\psi \rangle$ , or  $|\psi^{\prime}\rangle$ , describes an intrinsic quantum resource, which manifests itself as a product of nonclassical states in one basis, and as entanglement in another. In addition, it was shown by Sperling et al. (2019) that some families of states remain entangled for any choice of mode basis.

# E. Quantum correlation matrices

The information about multimodal correlations (Giorgi et al., 2011), classical as well as quantum, is contained in

different matrices. We introduce here the ones that are the quantum extensions of the classical matrices defined in Sec. II.E (Opatny, Korolkova, and Leuchs, 2002; Takase et al., 2019)

(1) The quantum coherency matrix  $\Gamma^{(1)}$  (Wiener, 1928), defined as the extension of the classical one [Eq. (19)], has matrix elements in a given mode basis equal to

$$
\left(\boldsymbol {\Gamma} ^ {(1)}\right) _ {m, n} = \langle \hat {a} _ {m} ^ {\dagger} \hat {a} _ {n} \rangle , \tag {46}
$$

which can be written in a condensed way as  $\Gamma^{(1)} = \langle \vec{a}^{\dagger}\vec{a}^{T}\rangle$

$\Gamma^{(1)}$  is an Hermitian, positive matrix of the Gram type that can be related to the first-order coherence properties of the field (Glauber, 1963; Mandel and Wolf, 1995; Refregier and Goudail, 2005). Its trace gives the mean total number of photons in the state.

(2) The quantum covariance matrix  $\Gamma_{\mathcal{O}}$

We name, in a same way as in Eq. (22),

$$
\vec {Q} = \left(\hat {X} _ {1}, \hat {X} _ {2}, \dots , \hat {X} _ {N}, \hat {P} _ {1}, \hat {P} _ {2}, \dots , \hat {P} _ {N}\right) ^ {T} \tag {47}
$$

as the column vector containing all quadrature operators. The quadrature covariance matrix  $\Gamma_{Q}$  (Simon, Mukunda, and Dutta, 1994) is the real  $2N\times 2N$  matrix defined on a given mode basis  $(\vec{f}_n)$  as

$$
\boldsymbol {\Gamma} _ {Q} = \frac {1}{2} \langle \vec {\hat {Q}} \vec {\hat {Q}} ^ {T} + (\vec {\hat {Q}} \vec {\hat {Q}} ^ {T}) ^ {T} \rangle . \tag {48}
$$

Equation (48) contains all second moments of the quadrature operators  $\langle \hat{X}_m\hat{X}_n\rangle ,\langle \hat{P}_m\hat{P}_n\rangle ,\langle \hat{X}_m\hat{P}_n\rangle$  and  $(\langle \hat{P}_m\hat{X}_n\rangle +\langle \hat{X}_n\hat{P}_m\rangle) / 2$  . This allows us to write in a compact way the following multimode version of the Heisenberg inequality (Simon, Mukunda, and Dutta, 1994):

$$
\boldsymbol {\Gamma} _ {Q} + i \beta = \boldsymbol {\Gamma} _ {Q} + \left( \begin{array}{c c} \emptyset & i \mathbb {1} \\ - i \mathbb {1} & \emptyset \end{array} \right) > 0, \tag {49}
$$

where  $\beta$  is the symplectic form. This relation is invariant under any symplectic transformation and, in particular, under any mode basis change.

Note that the vector  $\vec{Q}$  is of dimension  $2N$ , whereas the modal vectors  $\vec{E}$  and  $\vec{a}$  defined in Secs. II.B and III.A are of dimension  $N$ . We mention the difference when necessary in the following.

The coherency matrix is related to the matrix elements of the quadrature covariance matrix by the following expression, a quantum extension of Eq. (24):

$$
\begin{array}{l} \left(\Gamma^ {(1)}\right) _ {m, n} = \frac {1}{4} \left[ \left\langle \hat {X} _ {m} \hat {X} _ {n} \right\rangle + \left\langle \hat {P} _ {m} \hat {P} _ {n} \right\rangle \right. \\ + i \left(\left\langle \hat {X} _ {m} \hat {P} _ {n} \right\rangle - \left\langle \hat {P} _ {m} \hat {X} _ {n} \right\rangle\right) ]. \tag {50} \\ \end{array}
$$

In particular,

$$
\left(\boldsymbol {\Gamma} ^ {(1)}\right) _ {n, n} = \frac {1}{4} \left[ \left\langle \hat {X} _ {n} ^ {2} \right\rangle + \left\langle \hat {P} _ {n} ^ {2} \right\rangle - 2 \right]. \tag {51}
$$

# F. Mode basis change

The unitary transformation  $U$  that connects one mode basis to another one can be seen in two different ways:

(1) It can be considered as a change of point of view on a given quantum state, in the same way that one can use rotations to see a physical object from different perspectives. This is what we have done so far.  
(2) It can also be considered as a quantum process implemented by a real physical device and modifying the quantum state of the system by a unitary transformation, in the same way that one can rotate the physical object under consideration and keep a fixed point of view.  $U$  corresponds then to an evolution induced by a Hamiltonian that is a linear combination of operators of the form  $\hat{a}_i\hat{a}_j^\dagger$ . It can be shown that this transformation can be implemented by a generalized interferometer that mixes all of the input modes by appropriate beam splitters (Reck et al., 1994).

We use these two aspects of mode changes in the following.

# G. Intrinsic properties of multimode light states

Note that whereas the entanglement and factorization of state  $|\psi \rangle$  [Eq. (44)] depend on the mode basis, the total mean photon number in this state is equal to 2 in the two-mode bases. There are therefore properties that do not depend on a special choice of mode basis and that we call intrinsic. We expect them to have a stronger physical meaning than the properties that depend on this choice (Réfrégier and Goudail, 2005).

We mention here some physical properties that are intrinsic:

- The vacuum state  $|0\rangle$  is the same in any mode basis, as we see in Sec. III.C.  
- The operator total number of photons is defined by

$$
\hat {N} _ {\mathrm {t o t}} = \sum_ {m} \hat {b} _ {m} ^ {\dagger} \hat {b} _ {m} = \vec {b} ^ {\dagger T} \cdot \vec {\hat {b}}. \tag {52}
$$

The unitarity of transformation  $U$  [Eqs. (9) and (29)] implies that

$$
\vec {b} ^ {\dagger} ^ {T} \cdot \vec {\hat {b}} = \vec {a} ^ {\dagger} ^ {T} U ^ {T *} \cdot U \vec {\hat {a}} = \vec {\hat {a}} ^ {\dagger} ^ {T} \cdot \vec {\hat {a}}. \tag {53}
$$

Consequently, the total number of photons is an intrinsic operator.

- Let us define a multimode coherent state as an eigenstate of all annihilation operators  $\hat{b}_m$  in a given mode basis. It is easy to see that this property is also true in any other mode basis. Therefore, this property is intrinsic.  
- The mode basis change is a unitary transformation  $U$  that conserves the commutation relations: it is therefore a special case of symplectic transformation (Arvind et al., 1995). We exploit this feature several times in the following. A first consequence is the invariance of the Wigner function. More precisely, if  $W_{u}(\alpha_{1},\dots,\alpha_{\ell},\dots) = W_{u}(\vec{\alpha})$  is the multimode Wigner function of a given quantum state of light in the phase space of complex coordinates  $\alpha_{1},\ldots ,\alpha_{\ell}$ , spanning over the  $N$  modes  $\{\pmb{u}_{\ell}\}$

and  $W_{f}(\vec{\beta})$  is the Wigner function of the same quantum state written now in the phase space spanning over the modes  $\{f_m\}$ , one has (Simon, Mukunda, and Dutta, 1994)

$$
W _ {f} (\vec {\beta}) = W _ {u} (\vec {\alpha}) \quad \text {w i t h} \quad \vec {\beta} = U \vec {\alpha}. \tag {54}
$$

This means that the values of the Wigner function are the same in both bases, but they occur at different values of the coordinates in phase space. In particular, the sign of the Wigner function is intrinsic. Another intrinsic and additive quantity related to the volume  $N$  of the negative part of the Wigner function is the Wigner logarithmic negativity (Kenfack and Zyczkowski, 2004; Albarelli et al., 2018)

$$
L _ {n w} = \log \left(\int d ^ {N} \alpha \left| W _ {u} (\vec {\alpha}) \right|\right). \tag {55}
$$

Therefore, the quantum properties related to the fact that the Wigner function of some quantum states have negative parts are intrinsic.

A special case of this invariance concerns the value of the Wigner function at the origin, which is related to the parity of the photon number distribution (Royer, 1977). One has  $W_{f}(0) = W_{u}(0)$ , which means that the mean value of the parity operator is an intrinsic quantity.

- The same invariance property is also true for the Glauber-Sudarshan  $P$  function

$$
P _ {f} (\vec {\beta}) = P _ {u} (\vec {\alpha}). \tag {56}
$$

The sign of the  $P$  function is often related to the nonclassicality of the corresponding state (Vogel, 2000). Therefore, the nonclassicality of a state is also intrinsic. Similarly, we have  $P_{f}(0) = P_{u}(0)$ : the probability of being in vacuum state is an intrinsic quantity.

- The purity of a quantum state  $P = \mathrm{Tr}\rho^2$  can be calculated from its Wigner function

$$
P = 2 \pi \int d ^ {N} (\alpha) W _ {u} ^ {2} (\vec {\alpha}) = 2 \pi \int d ^ {N} (\beta) W _ {f} ^ {2} (\vec {\beta}) \tag {57}
$$

(as the Jacobian of the coordinate change is 1). As a result, the purity of a multimode quantum state of light is an intrinsic quantity.

# IV. SEARCH FOR PRINCIPAL MODES

This section is concerned with the following problem, which is not restricted to quantum physics (Comon, 1994; Milione, Nolan, and Alfano, 2015): given a quantum mult-mode state, pure or mixed, is it possible to find a mode basis which simplifies the expression of the quantum state and reduces it to forms that are more suitable to characterize it physically? The modes of this basis will be called principal modes. To this purpose, we will use different correlation matrices, in close analogy with the classical case.

More precisely, we want to find a mode basis that allows us to describe a given pure state  $|\psi \rangle$  as

$$
| \psi \rangle = | \phi_ {p} \rangle \otimes | 0, 0 \dots \rangle \tag {58}
$$

or a mixed state  $\rho$  as

$$
\rho = \rho_ {p} \otimes | 0, 0 \dots \rangle \langle 0, 0 \dots |, \tag {59}
$$

where  $|\phi_p\rangle$  or  $\rho_{p}$  spans a minimal number  $p$  of modes  $f_{1},\ldots ,f_{p}$ .  $p$  is then called the intrinsic number of modes of the corresponding state.

In this basis, characterized by annihilation operators  $\hat{a}_n$ , one has for any  $n > p$

$$
\hat {a} _ {n} | \psi \rangle = 0 \quad \text {o r} \quad \hat {a} _ {n} \rho = 0,
$$

$$
\hat {a} _ {m} ^ {\dagger} \hat {a} _ {n} | \psi \rangle = 0 \quad \text {o r} \quad \hat {a} _ {m} ^ {\dagger} \hat {a} _ {n} \rho = 0. \tag {60}
$$

Equation (60) implies that the matrix elements  $(\Gamma^{(1)})_{m,n}$  of the coherency matrix such that  $m > p$  and  $n > p$  are zero. This property is valid for both pure and mixed states. The coherency matrix  $\Gamma^{(1)}$  consists therefore of a square  $p\times p$  nonzero diagonal submatrix surrounded by zeros. Reciprocally, if  $\Gamma^{(1)}$  has the form that we just described, then  $\forall n > p\langle \hat{a}_n^\dagger \hat{a}_n\rangle = 0$  the mean number of photons in nth mode is zero, which implies that the considered state is the vacuum for all modes with  $n > p$ . The state is therefore a  $p$ -mode state, where  $p$  is simply the rank of the coherency matrix.

Now take a mode basis that we can choose at will, called  $\{\mathbf{g}_{\ell}\}$ , with the associated annihilation operators  $\hat{c}_{\ell}$ . The corresponding coherency matrix  $\Gamma^{(1)} = \langle \vec{c}^{\dagger} \vec{c}^{T} \rangle$  contains a priori many nonzero matrix elements so that the quantum state looks highly multimode. However,  $\Gamma^{(1)}$  is Hermitian and therefore diagonalizable. More precisely, there is a unitary transformation  $V$  that diagonalizes the  $N \times N$  matrix such that

$$
V \Gamma^ {(1)} V ^ {\dagger} = \operatorname {d i a g} \left(n _ {1}, \dots , n _ {p}, 0 \dots\right). \tag {61}
$$

We now introduce the column vector of creation operators in the new basis generated by mode transformation  $V,\hat{d}^{\dagger} = V\hat{c}^{\dagger}$  One has

$$
\operatorname {d i a g} \left(n _ {1}, \dots , n _ {p}, 0 \dots\right) = \langle V \vec {\hat {c}} ^ {\dagger} \vec {\hat {c}} ^ {T} V ^ {T *} \rangle = \langle \vec {\hat {d}} ^ {\dagger} \vec {\hat {d}} ^ {T} \rangle . \tag {62}
$$

We therefore prove that in the mode basis  $\{\vec{h}\}$  of the modal space defined by  $\vec{h} = V\vec{g}$  the first-order covariance matrix is reduced to the subset of the first  $p$  modes and find the right mode basis and the corresponding minimum mode number.

The diagonalization of the  $\Gamma^{(1)}$  matrix directly yields the list of the  $p$  eigenmodes, allowing us to write the quantum state, pure or mixed, in its simplest form. We see when we discuss quantum frequency combs later that the reduction in size of the problem can be drastic, namely, from  $10^5$  frequency modes to a few principal modes. In particular, it is wise to use the set of principal modes if one wants to make the full tomography of a

multimode quantum state, instead of a mode basis with a much larger number of nonempty modes. Note that this procedure is valid for Gaussian and non-Gaussian states; see Sec. VII.

The energy content of the principal modes is given by the corresponding eigenvalue, whereas the absence of off-diagonal terms in this basis implies that the principal modes are mutually incoherent: it is not possible to observe interferences on a linear combination of two principal modes. Often the eigenvalues of the coherency matrix are all nonzero but form a series with decreasing terms. In this case, it is possible to define an effective intrinsic mode number  $\bar{p}$ , which gives the approximate number of the most excited modes. It can be obtained by the same procedure as for the effective Schmidt number. It is defined by

$$
\bar {p} = \frac {\left\langle \sum_ {m} \hat {N} _ {m} \right\rangle^ {2}}{\left\langle \sum_ {m} \hat {N} _ {m} ^ {2} \right\rangle} = \frac {\left(\operatorname {T r} \boldsymbol {\Gamma} ^ {(1)}\right) ^ {2}}{\operatorname {T r} \left[ \left(\boldsymbol {\Gamma} ^ {(1)}\right) ^ {2} \right]}, \tag {63}
$$

with  $\hat{N}_m = \hat{d}_m^\dagger \hat{d}_m$

Note that extracting physically reliable and useful information from the measurement of the noise amplitudes and correlations in a complex physical system by extracting a finite number of principal modes from noise matrices is a well-known procedure in other parts of science and technology (Shah et al., 2005). It would take too long to mention all of them. If one is restricted to recent developments in optics and electromagnetism (Fan and Kahn, 2005), one can mention the MIMO technique (meaning multiple in multiple out) in telecommunication technologies (Winzer and Foschini, 2011) and the control of light propagation in complex media for optical computation purposes (Rotter and Gigan, 2017).

From a given noise matrix experimentally determined by measurements performed on a mode basis appropriate for detection and the computation of principal modes, it is also possible to determine the noise of any physical parameter of the considered system and to get fruitful physical insight into the underlying physical mechanisms. This method has been, in particular, applied to the analysis of mode-locked lasers (Schmeissner et al., 2014).

# V. INTRINSIC SINGLE-MODE STATES

We now focus on the important case where the state  $\rho$  can be reduced to a single-mode state using an appropriate choice of the mode basis  $f_{m}$ , with associated annihilation operators  $\hat{c}_{m}$ .

First assume that the state we are interested in is the pure state  $|\psi \rangle$ . Then  $|\psi \rangle = |\phi_1\rangle \otimes |0,0\dots \rangle$  on mode basis  $f_{m}$ . We know that it has a coherency matrix with a single nonzero eigenvalue, but it can also be characterized using a simpler mathematical property: if one takes a test mode basis  $\pmb{g}_{\ell} = \sum_{p}U_{\ell}^{p}\pmb{f}_{p}$  with associated annihilation operators  $\hat{b}_{\ell}$ , one has for any  $\ell$

$$
\hat {b} _ {\ell} | \psi \rangle = U _ {\ell} ^ {1} \hat {c} _ {1} | \phi_ {1} \rangle \otimes | 0 \rangle . \tag {64}
$$

In a single-mode pure state, all vectors  $\hat{b}_{\ell}|\psi\rangle$  in any test mode basis are proportional to each other. In addition, one can show

(Treps et al., 2005) that this property is also a sufficient condition for being single mode.

Now assume that the state is in the mixed state  $\rho = \rho_{1} \otimes |0\rangle \langle 0|$  on the appropriate mode basis  $\{f_m\}$ . Taking a test mode basis  $\{\pmb{g}_{\ell}\}$ , one has for any  $\ell$

$$
\hat {b} _ {\ell} \rho = U _ {\ell} ^ {1} \hat {c} _ {1} \rho_ {1} \otimes | 0 \rangle \langle 0 |. \tag {65}
$$

In a single-mode mixed state, all operators  $\hat{b}_{\ell}\rho$  are proportional to each other. Here also this property can be shown to be sufficient for being in a single-mode mixed state (Leroyer, 2007).

# A. Examples

# 1. Pure single-photon wave packet

Consider the following state, which is a coherent superposition of single-photon states in different modes:

$$
\left| \Psi_ {1} \right\rangle = \sum_ {m} c _ {m} \left| 1: \boldsymbol {f} _ {m} \right\rangle , \tag {66}
$$

with  $\sum_{m}|c_{m}|^{2} = 1$ , where  $|1:f_m\rangle$  is short notation for a state with one photon in mode  $f_{m}$  and zero in all other modes. This state, often called a single-photon wave packet, is an eigenstate of  $\hat{N}_{\mathrm{tot}}$  with eigenvalue 1. It is actually an intrinsic single-mode state, as all  $\hat{b}_{\ell}|\Psi_1\rangle$  states are proportional to the vacuum state: we have therefore shown that all single-photon states are actually single-mode states.

To find the mode in which the single photon can be found, we introduce the  $\nu_{1}$  mode, given by the same linear combination as Eq. (66) but for modes instead of states:

$$
\boldsymbol {v} _ {1} = \sum_ {m} c _ {m} \boldsymbol {f} _ {m}. \tag {67}
$$

It is a first element of a mode basis  $\{\nu_{n}\}$  that one completes with orthogonal functions. It is easy to show that in this new mode basis the state  $|\Psi_1\rangle$  is written as

$$
| \Psi_ {1} \rangle = | 1: v _ {1} \rangle \otimes | 0, 0 \dots \rangle . \tag {68}
$$

$\nu_{1}$  is indeed the mode in which the single photon lives.

We noted in Eq. (41) the equality between the scalar product of single-photon states and that of the corresponding modes. Such a homomorphism between the mode and state properties for single photons is perhaps the reason why detailed consideration of the multimodal structure of quantum states and its physical consequences has not been the object of many studies by physicists interested in single-photon states.

# 2. Single-photon statistical mixture

Now consider the statistical mixture of single-photon states

$$
\rho_ {1} = \sum_ {m} p _ {m} | 1: f _ {m} \rangle \langle 1: f _ {m} |, \tag {69}
$$

with  $p_m > 0$  and  $\sum_{m} p_m = 1$ . It is not single mode because  $\hat{b}_{m_1}\rho_1 = p_{m_1}|0\rangle \langle 1:f_m|$  are not proportional to each other. One

easily shows that the coherency matrix is diagonal, with eigenvalues that are precisely the statistical coefficients  $p_m$ .

# 3. Pure multimode coherent state

Now consider the multimode coherent state introduced in Sec. III.E, which is an eigenstate of all annihilation operators  $\hat{b}_m$  in a given mode basis. It can therefore be written as a tensor product of coherent states  $|\alpha_m:f_m\rangle$  of eigenvalue  $\alpha_{m}$  in mode  $f_{m}$ :

$$
\left| \Psi_ {1} ^ {\prime} \right\rangle = \left| \alpha_ {1}: f _ {1} \right\rangle \otimes \dots \otimes \left| \alpha_ {m}: f _ {m} \right\rangle \otimes \dots . \tag {70}
$$

This state is single mode, as all  $\hat{a}_{\ell}|\Psi_{1}^{\prime}\rangle$  states are proportional to  $|\Psi_1^\prime \rangle$  itself.

To find the mode, we introduce the  $w_{1}$  mode given by

$$
\boldsymbol {w} _ {1} = \frac {1}{\beta} \sum_ {m} \alpha_ {m} \boldsymbol {f} _ {m}, \tag {71}
$$

with  $|\beta|^2 = \sum_m |\alpha_m|^2$ . It is the first element of a new mode basis  $w_n$ , which one completes again. It is also easy here to show that in this new mode basis the previous multimode coherent state is

$$
\left| \Psi_ {1} ^ {\prime} \right\rangle = \left| \beta : w _ {1} \right\rangle \otimes \left| 0, 0 \dots \right\rangle . \tag {72}
$$

Here the state  $|\Psi_1^{\prime}\rangle$ , which looks highly multimodal in the original basis, is also a simple single-mode coherent state in a more adapted basis.

It is easy to show from Eq. (38) that for any coherent state, written in the basis where it is single mode in mode  $\pmb{g}$ ,

$$
\hat {b} _ {\boldsymbol {f}} | \beta : \boldsymbol {g} \rangle = (\vec {f} ^ {T *} \cdot \vec {g}) \beta | \beta : \boldsymbol {g} \rangle , \tag {73}
$$

where  $\hat{b}_f$  is the annihilation operator in mode  $f$ . Note that this relation is closely analogous to the corresponding expression (42) for single-photon states: the spatial, temporal, and polarization properties of coherent states and single-photon states are often similar.

# 4. Coherent state statistical mixture

Consider now the statistical mixture of coherent states

$$
\rho_ {1} ^ {\prime} = \sum_ {m} p _ {m} | \alpha_ {m}: f _ {m} \rangle \langle \alpha_ {m}: f _ {m} |. \tag {74}
$$

It is not intrinsically single mode because the operators  $\hat{b}_{m_1}\rho_1^\prime$  are not proportional to each other. The coherency matrix is diagonal with eigenvalues  $p_m|\alpha_m|^2$ .

Examples (b) and (d) show that mixed states are "more multimodal" than the corresponding pure states: the inclusion of classical noise in addition to quantum noise increases the number of principal modes involved in the description of the state. Furthermore, one can describe the statistical properties of such mixed states using the classical coherency matrix, i.e., within the framework of classical coherence theory. While this is not unexpected for coherent states, which are often called quasiclassical, it is more noteworthy for single-photon states.

# 5. Two-photon pure state

Finally, we consider the Hong-Ou-Mandel two-photon pure state  $|\Psi^{\prime \prime}\rangle = |1:\pmb{g}_1\rangle |1:\pmb{g}_2\rangle$ . It is a not a single-mode state because  $\hat{a}_{1}|\Psi^{\prime \prime}\rangle = |0:\pmb{g}_{1}\rangle |1:\pmb{g}_{2}\rangle$  and  $\hat{a}_{2}|\Psi^{\prime \prime}\rangle = |1:\pmb{g}_{1}\rangle |0:\pmb{g}_{2}\rangle$  are orthogonal. This means, in particular, that there is no mode basis change, or unitary transformation, which enables us to write it as the single-mode state  $|2:\pmb{g}_1\rangle |0:\pmb{g}_2\rangle$ : two photons in different modes cannot "merge" into a two-photon state in a single output mode of a unitary transformation.

# B. Relation with classical optical coherence

The notion of optical coherence (Glauber, 1963; Mandel and Wolf, 1995; Goodman, 2015) is linked to the ability to observe interference fringes with high visibility. It is characterized by the normalized first-order complex correlation function

$$
g ^ {(1)} \left(\mathbf {r}, \mathbf {r} ^ {\prime}, t, t ^ {\prime}\right) = \frac {G ^ {(1)} \left(\mathbf {r} , \mathbf {r} ^ {\prime} , t , t ^ {\prime}\right)}{\sqrt {G ^ {(1)} \left(\mathbf {r} , \mathbf {r} , t , t\right) G ^ {(1)} \left(\mathbf {r} ^ {\prime} , \mathbf {r} ^ {\prime} , t ^ {\prime} , t ^ {\prime}\right)}}, \tag {75}
$$

where  $G^{(1)}(\mathbf{r}', \mathbf{r}', t', t')$  is as defined in Eq. (20). If  $|g^{(1)}| = 1$ , then interferences are of contrast 1 and the field is said to be perfectly coherent.

The quantum counterpart of  $G^{(1)}$ , where the statistical average represented by the overbar is replaced by a quantum average, is related to the first-order coherency matrix introduced in Eq. (23).

For a single-mode state in mode  $\nu_{1}$ , one has

$$
\langle \hat {E} _ {i} ^ {(+) \dagger} (\mathbf {r}, t) \hat {E} _ {j} ^ {(+)} \left(\mathbf {r} ^ {\prime}, t ^ {\prime}\right) \rangle = \mathcal {E} _ {0} ^ {2} \left(\boldsymbol {\Gamma} ^ {(1)}\right) _ {1, 1} v _ {1 i} ^ {*} (\mathbf {r}, t) v _ {1 j} \left(\mathbf {r} ^ {\prime}, t ^ {\prime}\right), \tag {76}
$$

which is valid for all  $\mathbf{r}$ ,  $t$ ,  $\mathbf{r}'$ ,  $t'$ ,  $i$ , and  $j$ . This implies that  $|g^{(1)}| = 1$  for all  $\mathbf{r}$ ,  $t$ ,  $\mathbf{r}'$ , and  $t'$ . This property does not depend on the quantum state "living" in the mode [except for the energy scaling factor  $(\Gamma^{(1)})_{1,1} = N_{\mathrm{tot}}$ ]. Conversely, if there are two points in space-time  $(\mathbf{r}_0, t_0)$  and  $(\mathbf{r}_0', t_0')$  such that  $|g^{(1)}(\mathbf{r}_0, \mathbf{r}_0', t_0, t_0')| < 1$ , then one can conclude that the state is not intrinsically single mode.

Consequently, perfect optical coherence is not limited to the use of coherent states: the condition of perfect coherence is related to the modal property of the quantum state, more precisely, to the fact that only one electromagnetic mode is not in the vacuum state. It does not depend on the properties of the quantum state defined in this mode. For example, one will be able to see perfect interference fringes with coherent states, which is not unexpected, but also with strongly "incoherent-looking" states such as single-photon states, as noticed by Glauber (1963), or with strongly "quantum-looking" states such as Schrodinger cats. In contrast, this will not be possible with the Hong-Ou-Mandel two-photon state  $|1,1\rangle$ , which is not single mode.

# C. Simple sufficient conditions for an intrinsic single-mode state

The single-mode criteria that were just exposed are not easy to implement experimentally. One possibility is of course to experimentally measure all matrix elements of the quadrature

covariance matrix, which is explained in Sec. X.C. As this is not a simple task, it would be interesting to have at one's disposal a sufficient physical criterion that can be experimentally checked in a simpler way.

The physical meaning of an intrinsic single-mode state is simple: in such a state, all of the physical properties have a spatiotemporal dependence given by  $\nu_{1}$ . As a result, the mean value  $\langle \hat{E}^{(+)}(x,y,z,t)\rangle$  and the standard deviation  $\Delta E^{(+)}(x,y,z,t)$  have the same spatial dependence. In contrast, in nonintrinsic single-mode states, these different quantities may have different spatial variations. Therefore, a rather easy experimental check of whether or not a given quantum state is intrinsically single mode consists of measuring the mean value and the quadrature noise in different areas, in different time windows or in different spectral regions. If the ratio of these two quantities is not constant when one varies the detection area, the time bin, or the frequency band, then one is sure that the state is not intrinsically single mode. Note that this test gives only a sufficient condition: a constant value of the ratio does not imply that the state is single mode. This criterion has been successfully used by different groups in experiments involving spectral (Marin et al., 1995; Spalter et al., 1998) and spatial modes (Hermier et al., 1999; Martinelli et al., 2003; Corzo et al., 2011). For example, Marin et al. (1995) spectrally resolved the intensity noise of a sub-Poissonian laser diode using a spectrometer of variable width. The nonlinear variation of the intensity noise as a function of the number of spectral modes of the diode laser is an indication of the existence of strong anticorrelations between the main longitudinal mode and the weak side modes.

# VI. COUNTING AND DETERMINING THE PRINCIPAL MODES

We now consider more complex quantum states than the intrinsic single-mode ones. The minimum number  $p$  of modes needed to completely describe them and the shape of the corresponding principal modes are important parameters that characterize the system under study. From a mathematical point of view, it can be shown in the case of a pure state that  $p$  is also the dimension of the vector space generated by all vectors  $\hat{b}_m|\Psi \rangle$ , with  $\{\hat{b}_m\}$  the set of annihilation operators associated with a given test mode basis. From a more practical point of view, the best way is to experimentally determine all matrix elements of the coherency matrix, to diagonalize it, and to count the number of nonzero eigenvalues (Morin, Fabre, and Laurat, 2013). This method works for pure and mixed states, and for Gaussian and non-Gaussian states as well.

Counting modes is of course not restricted to quantum optics, and researchers have developed several criteria that have allowed them to find the number of such modes in various situations. It is therefore interesting to compare the different ways of determining the mode number in a multimode system.

# A. Case of spatial modes

We first treat in this section the case of 1D spatial modes. They can be readily extended to 2D spatial modes. In classical optics, the number  $p$  of spatial modes in a light beam of

transverse size  $D$  is usually taken as equal to  $D / d_{c}$ , where  $d_{c}$  is the coherence length (Karny, Lavi, and Kafir, 1983). To compare this value with the one determined in Sec. IV, we need to find a quantum state  $\rho$  describing the same physical situation. A possible state is the following statistical mixture:

$$
\rho = \sum_ {n = 1} ^ {p} p _ {n} \left| \alpha_ {n}: \boldsymbol {w} _ {n} \right\rangle \left\langle \alpha_ {n}: \boldsymbol {w} _ {n} \right|, \tag {77}
$$

with  $\sum p_n = 1$ . The modes  $w_{n}(x)$  are pixel modes for which  $w_{n}(x)$  is equal to  $1 / \sqrt{d_c}$  for  $(n - 1)d_c < x < nd_c$  and zero outside. Their number is precisely  $p$ .  $|\alpha_{n}:w_{n}\rangle$  are coherent states defined in each coherence area. We now apply our quantum counting technique to this state: in such a quantum state the first-order coherency matrix is diagonal in the pixel mode basis because the fluctuations in the different pixel modes are uncorrelated. Its diagonal elements are  $p_n|\langle \alpha_n|\hat{a}_n^\dagger \hat{a}_n|\alpha_n\rangle |^2$ : the number of nonzero diagonal elements is indeed  $D / d_{c}$  so that the classical and quantum approaches lead to the same value of the mode number.

We consider in Appendix A other multimode light sources, such as lasers and parametric down-conversion devices. We show later with a simple example that the number  $p$  of transverse modes in a laser is equal to the  $M$  factor introduced by Siegman (1998), and that it is equal to twice the Schmidt number in the case of parametric down-conversion.

On the experimental side, the spatial structure of the mode of an heralded single photon was recently experimentally determined using a holographic technique (Chrapkiewicz et al., 2016).

# B. Case of temporal modes

The generation of pure single photons is the object of an intense experimental research (Lvovsky et al., 2001; Eisaman et al., 2011). We have seen that, theoretically speaking, pure single photons are always single mode. Experimentally speaking, more than one mode can be populated because of experimental imperfections. It is therefore important to evaluate the number and the exact shape of the temporal modes that are excited. This problem was theoretically considered, for example, by Aichele, Lvovsky, and Schiller (2002). A convenient way to do it is to derive it from the information contained in the temporal coherency matrix, also called in this context the temporal autocorrelation function (Nielsen and Mølmer, 2007), the matrix elements of which are

$$
\left. \left(\boldsymbol {\Gamma} ^ {(1)}\right) _ {n, n ^ {\prime}} = \langle \hat {a} ^ {\dagger} \left(t _ {n}\right) \hat {a} \left(t _ {n ^ {\prime}}\right) \rangle , \right. \tag {78}
$$

where  $t_n$  and  $t_{n'}$  are sampling times of the homodyne signal, taken in large enough quantities to reach a good statistical estimation. The diagonalization of this matrix allows us to know the temporal shapes and the degree of excitation of the different principal modes.

We now present the method used by Morin, Fabre, and Laurat (2013), one of the first fully experimental determinations of the temporal modes of several heralded states, namely, single-photon, two-photon, and coherent state superpositions: one produces by type II parametric

down-conversion weak signal and idler beams. The temporal fluctuations of the signal beam quadrature component are continuously recorded by homodyne detection. When a photon is detected at time  $t_c$  on the idler beam, one postselects the homodyne signal values in  $N/2$  time bins before  $t_c$  and  $N/2$  time bins after  $t_c$ . These data are then averaged over many detected idler photons and used to determine the  $N \times N$  temporal autocorrelation function. If the phase of the local oscillator is random during the accumulation time, it is easy to show that the experimental autocorrelation matrix is directly related to the coherency matrix in the time bin temporal mode basis. Its diagonalization gives the number and the temporal shape of the modes that are not in the vacuum state. If this state is indeed single photon, the matrix has a single eigenstate with a nonzero eigenvalue. Its temporal shape on the  $N$  time bins gives the shape of the mode in which the conditionally generated single photon lives. A similar approach was used by Qin et al. (2015).

Other recently developed techniques use spectral shearing interferometry (Davis et al., 2018) or dual homodyne measurement (Takase et al., 2019). Sum-frequency generation can also be used as a kind of fast correlator that also allows one to determine the number of modes in parametric downconversion (Kopylov et al., 2019).

# VII. MULTIMODE GAUSSIAN STATES

Gaussian states play an important role in continuous variable quantum optics, as they are nonclassical states that are deterministically generated by nonlinear optical processes in which the quantum fluctuations are small compared to the mean values. They also have the practical interest of being completely characterized by the first and second moments of the quadratures [but also of the photon numbers (Vallone, Cariolaro, and Pierobon, 2019)]. In addition, they are promising candidates as building bricks for quantum information and quantum metrology purposes (Weedbrook et al., 2012; Adesso, Ragy, and Lee, 2014).

# A. Symplectic transformations

We again use the compact vectorial notation  $\hat{\vec{Q}}$  defined in Eq. (47) containing the quadrature operators of all  $N$  modes. The usual commutation relations can then be written as

$$
\left[ \hat {Q} _ {\mu}, \hat {Q} _ {\nu} \right] = 2 i \beta_ {\mu , \nu}, \quad \text {w h e r e} \beta = \left( \begin{array}{c c} \emptyset & \mathbb {1} \\ - 1 & \emptyset \end{array} \right). \tag {79}
$$

A symplectic transformation is defined by a  $2N \times 2N$  real matrix  $S$  acting on the quadrature operator column vector  $\hat{\tilde{Q}}$  that preserves the commutation relations (Simon, Sudarshan, and Mukunda, 1988). The set of such transformations is named the symplectic group (Arvind et al., 1995). The condition that commutators are preserved leads to the following condition for a symplectic transformation  $S$ :

$$
S \beta S = \beta . \tag {80}
$$

This group includes all the mode basis change transformations that we have already considered, but it is not limited to these transformations.

# B. Wigner function of a Gaussian state

By definition, a Gaussian state is a state, pure or mixed, that is described by a Gaussian Wigner function. It is, modulo a displacement in phase space, completely described by its covariance matrix  $\Gamma_{Q}$ . Note that not all positive matrices can be used as the covariance matrix of a Gaussian state, as they need to satisfy the generalized Heisenberg inequality (49). In addition, the covariance matrix  $\Gamma_{Q}$  associated with a non-classical (squeezed and/or entangled) quantum state has at least its smallest eigenvalue that is smaller than 1.

The Wigner function is a real quasiprobability distribution over multimode phase space depending on the  $2N$  real quadrature coordinates  $\vec{q}$ . In the case of a Gaussian state of covariance matrix  $\Gamma_{Q}$ , its expression is

$$
W (\vec {q}) = \frac {1}{(2 \pi) ^ {N} \sqrt {\det  \Gamma_ {Q}}} e ^ {- (\vec {q} - \langle \vec {Q} \rangle) ^ {T} \Gamma_ {Q} ^ {- 1} (\vec {q} - \langle \vec {Q} \rangle)}, \tag {81}
$$

with  $\langle \vec{Q}\rangle$  being the phase space displacement mentioned earlier.

The purity  $P$  of a Gaussian state is simply related to the covariance matrix by

$$
P = \frac {1}{\det \Gamma_ {Q}}. \tag {82}
$$

The transformation of the Wigner function under a symplectic transformation  $S$  can be directly calculated using the same approach as in Eq. (54):

$$
W ^ {\prime} \left(\vec {q} ^ {\prime}\right) = W (\vec {q}) \quad \text {w i t h} \quad \vec {q} ^ {\prime} = S \vec {q}. \tag {83}
$$

Hence, a Gaussian state remains Gaussian under symplectic transformation. Moreover, the values of the Wigner function are conserved in the transformation (and, in particular, the negative ones) but found at different points of the phase space. The covariance matrix change under the effect of a symplectic transformation  $S$  is expressed as

$$
\boldsymbol {\Gamma} _ {Q} ^ {\prime} = S \boldsymbol {\Gamma} _ {Q} S ^ {T}. \tag {84}
$$

# C. Gaussian state decomposition

# 1. Bloch-Messiah reduction

Many decompositions of symplectic transformations on subgroups of the symplectic group do exist (Arvind et al., 1995). Within the context of quantum optics, the most relevant one, introduced by Braunstein (2005) is the so-called Bloch-Messiah reduction (Bloch and Messiah, 1962). It is a direct consequence of the singular value decomposition.

Any symplectic  $S$  matrix can be decomposed into three matrices such as

$$
S = O _ {1} K O _ {2}, \tag {85}
$$

where  $O_{1}$  and  $O_{2}$  correspond to mode basis changes. In Eq. (9), a mode basis change was characterized by a unitary modal transformation  $U$  acting on the complex creation operators. The same mode basis change is also characterized by the following real orthogonal matrix  $O$  acting in the real space of quadrature operators:

$$
O = \left( \begin{array}{l l} \operatorname {R e} (U) & \operatorname {I m} (U) \\ - \operatorname {I m} (U) & \operatorname {R e} (U) \end{array} \right), \tag {86}
$$

where  $U = \operatorname{Re}(U) + i\operatorname{Im}(U)$ .  $K$  is a diagonal matrix of the form  $K = \mathrm{diag}(\sigma_1, \sigma_2, \dots, \sigma_N, \sigma_1^{-1}, \sigma_2^{-1}, \dots, \sigma_N^{-1})$ , where  $\sigma_i$  are real and positive numbers. It corresponds to a multimode squeezing operation in a well-defined mode basis.

# 2. Williamson reduction

The evolution of the covariance matrix under symplectic transformations as expressed in Eq. (84) is not a usual diagonalization procedure, and thus the standard spectral theorem does not apply. One can show (Arvind et al., 1995) that a diagonal form of the covariance matrix can always be found under these transformations, a process known as the Williamson reduction, which we expose here. For any covariance matrix  $\Gamma_{\mathbf{Q}}$  associated with a physical quantum state, there exists a symplectic transformation  $S^{\prime}$  such that

$$
S ^ {\prime} \boldsymbol {\Gamma} _ {Q} S ^ {\prime T} = \boldsymbol {\Gamma} _ {W} = \operatorname {d i a g} \left(\kappa_ {1}, \dots , \kappa_ {n}, \kappa_ {1}, \dots , \kappa_ {n}\right), \tag {87}
$$

where  $1 \leq \kappa_{1} \cdots \leq \kappa_{n}$  are called the Williamson eigenvalues. This means that under symplectic transformation, any Gaussian state can be reduced to a collection of independent symmetric thermal states with  $\langle \hat{X}_i^2 \rangle = \langle \hat{P}_i^2 \rangle = \kappa_i$ . Furthermore, because state purity is invariant under symplectic transformation one has  $P = 1 / \Pi_i \kappa_i$ .

Combining the Williamson and Bloch-Messiah reductions (85) and (87), one finds that for any Gaussian state

$$
\boldsymbol {\Gamma} _ {Q} = O _ {1} K O _ {2} \boldsymbol {\Gamma} _ {W} O _ {2} ^ {T} K O _ {1} ^ {T}, \tag {88}
$$

where  $\Gamma_W$  is of the form introduced in Eq. (87).

# 3. Pure Gaussian state

For a pure Gaussian state,  $\Gamma_W$  is the identity matrix. Hence, one can write

$$
\boldsymbol {\Gamma} _ {Q} ^ {\text {p u r e}} = O _ {1} K ^ {2} O _ {1} ^ {T}. \tag {89}
$$

Any pure Gaussian state can then be seen as the result of a mode basis change on a collection of independent pure squeezed states, thus inducing quantum entanglement between the modes (Braunstein, 2005). This property is used, for instance, to construct complex multimode entangled Gaussian states from a set of independent squeezers and a generalized interferometer; see Sec. XII.A.

# 4. Mixed Gaussian state

For general Gaussian mixed states Eq. (88) cannot be simplified; hence, the second basis change  $O_2$  is now physically relevant. Equation (88) has a clear physical meaning: any Gaussian state can be constructed from a generalized factorized thermal state  $\Gamma_W$  with a first basis change  $O_2$  that induces classical correlations between the input modes, which are then fed into a multimode squeezing operation  $K$  and finally mixed again by another basis change  $O_1$ .

The basis changes and the multimode squeezing characteristics can be straightforwardly deduced from the measured covariance matrix. Such a procedure enables us to uncover the modes carrying the quantum properties and those carrying the classical noise. However, one should be careful with associating too much "quantumness" to the  $K$  matrix when it acts on a thermal state. In this case, the multimode squeezing matrix modifies in a phase-dependent way the input classical noise, and the resulting output multimode mixed state can still be classical.

# 5. Intrinsic separability

The notion of separability, which corresponds to the ability to write a quantum state as a statistical superposition of factorized states (Peres, 1996; Li, Fei, and Wang, 2008), is inherently mode basis dependent and we will review its counterpart, entanglement, in Sec. VIII. Separability conditions can be derived from the covariance matrix (Gittsovich et al., 2008). The underlying symplectic geometry of Gaussian states renders possible the study of intrinsic separability, i.e., the question of the possible existence of a mode basis in which a given multimode state is separable (Mancini and Severini, 2006). For pure Gaussian states, this is a direct consequence of Bloch-Messiah decomposition, and the basis in which a multimode Gaussian state is separable is given by Eq. (89). For mixed Gaussian states Eq. (88) does not directly provide the solution, as the symplectic transformation involved is not a basis change. We thus follow here the approach of Walschaers et al. (2017a) to demonstrate the intrinsic separability of any Gaussian state.

One can simply rewrite Eq. (88) by introducing  $\Gamma_{\mathrm{th}} = O_2\Gamma_WO_2^T$ , which is the covariance matrix of a thermal state. A Gaussian state can thus be decomposed as  $\Gamma_G = \Gamma_s + \Gamma_c$  where  $\Gamma_s = O_1K^2 O_1^T$  is a pure multimode squeezed vacuum and  $\Gamma_c = O_1(\Gamma_{\mathrm{th}} - 1)O_1^T$  corresponds to the added noise. Note that  $\Gamma_c$  is a positive symmetric matrix that does not, in general, satisfy the Heisenberg inequality (49) and therefore cannot be associated with a quantum state: it can be seen as a noisy channel randomly displacing the pure state. One can show that the Wigner function of the Gaussian mixed state can be written as the convolution product (Walschaers et al., 2017a)

$$
W _ {G} (\vec {q}) = \int d ^ {2 N} \xi W _ {s} (\vec {q} - \vec {\xi}) p _ {c} (\vec {\xi}), \tag {90}
$$

where

$$
p _ {c} (\vec {\xi}) = \frac {e ^ {- \vec {\xi} ^ {T} \Gamma_ {c} ^ {- 1} \vec {\xi}}}{(2 \pi) ^ {N} \sqrt {\det \Gamma_ {c}}} \tag {91}
$$

is a Gaussian positive and normalized probability distribution and

$$
W _ {s} (\vec {q}) = \frac {e ^ {- \vec {q} ^ {T} \boldsymbol {\Gamma} _ {s} ^ {- 1} \vec {q}}}{(2 \pi) ^ {N} \sqrt {\det \boldsymbol {\Gamma} _ {s}}} \tag {92}
$$

is the Wigner function of a factorized multimode squeezed state. Equation (90) is simply the statistical mixture of displaced pure squeezed vacuum states, all separable in the same basis defined by transformation  $O_{1}$ . Hence, for any Gaussian state (the demonstration here can easily be extended to displaced states) one can find a mode basis, given by Bloch-Messiah-Williamson reduction, in which it is separable.

We stress here this important property of multimode Gaussian states: they are all intrinsically separable, meaning that they can always be "disentangled" in some appropriate mode basis. Note that this basis is not unique.

# VIII. MULTIPARTITE ENTANGLEMENT

Entanglement (Schrodinger, 1935) and nonseparability (Werner, Reinhard, 1989) are basic quantum resources. Their characterization is subtle and still the object of numerous investigations. These have mostly concerned bipartite systems, and entanglement criteria have been introduced (Gühne and Tóth, 2009; Horodecki et al., 2009) in terms of Schmidt number, partial transpose, variances of combinations of quadratures, quadrature matrix eigenvalues, etc. The complexity of the separability problem increases substantially when one studies multipartite systems. In these situations, one has a rapidly increasing number of choices in the bunching of parties on which one searches for a possible factorization (van Loock and Braunstein, 2000). Without going into much detail, we now present a brief overview of the domain, restricting ourselves mostly to results that are scalable to an arbitrary number of partitions.

In addition to being more complex than bipartite entanglement, multipartite entanglement has some specific features:

- Whereas the Schmidt decomposition is a useful tool for pure bipartite states, there is no such simple decomposition in the case of more than two parties in the general case (Acín et al., 2000; Pati, 2000).  
- The  $N$  multimode system can be divided into many different bipartitions, but there are also numerous possibilities of multipartitions in  $K = 3,4,\ldots ,N$  parties. For example, for  $N = 10$  the total number of multipartitions, whatever  $K$ , is 115974. A given state can be entangled for some partitions and not for others, which gives rise to a complex topology of quantum correlations (Menicucci et al., 2006). An important notion is that of "genuine entanglement": one defines a genuinely  $K$ -entangled state as a state that is not a statistical mixture of  $K$ -partite factorized density matrices. Genuine entanglement implies multipartite entanglement for every other partition of the modes. However, if a state does not exhibit this specific kind of entanglement (i.e., is two

separable), no conclusions on other forms of multipartite quantum correlations can be drawn.

- There are in some cases relations between the entanglement measures of the different partitions, which fall under the name of monogamy: in the case of three parties A, B, and C, for example, it has been shown in the cases of qubits (Coffman, Kundu, and Wootters, 2000) and symmetric Gaussian states (Adesso and Illuminati, 2006) that the A-BC entanglement between A and the two other modes is stronger than the sum of the "partial" entanglements A-B and A-C. This property is specific to quantum entanglement, in opposition to the classical correlations, which are not constrained and can be freely shared. This property can be generalized to an arbitrary number of bipartitions.

Multimode entanglement is also present in the case of a bipartition into two parties that are themselves multimode. This is the case, for example, in parametric down-conversion; see Sec. IX.A. If the two-party quantum state is pure its Schmidt decomposition gives the principal Schmidt modes of the system, and the number of terms (the Schmidt number) gives the dimensionality of the system (Law and Eberly, 2004; Gatti et al., 2012). In the general case, as the Schmidt decomposition cannot be extended to more than two parties, a "vector" of Schmidt numbers for all bipartitions is useful for characterizing multipartite pure states (Huber and Vicente, 2013). One can also use in this case a necessary and sufficient entanglement criterion (Gessner, Pezzè, and Smerzi, 2016).

The case of a mixed state  $\rho$  is more difficult to deal with. Theoreticians have introduced various entanglement witnesses for multipartite entanglement, i.e., operators  $\hat{W}$  such that  $\mathrm{Tr}(\rho \hat{W}) < 0$  implies nonseparability. There are simple ones, easy to calculate (Hillary, Dung, and Zheng, 2010) but missing many entangled states, and optimized ones (Hyllus and Eisert, 2006). The method of separability eigenvalues (Sperling and Vogel, 2013) has been used to characterize all partitions of a multipartite-entangled quantum frequency comb (Gerke et al., 2015). In addition to witnesses, one can use in the multipartite case the partial transpose method (Simon, 2000) and define a measure of entanglement in the continuous variable regime in terms of logarithmic negativity (Adesso, Serafini, and Illuminati, 2004). One can also derive simple criteria to detect genuine entanglement (Toscano et al., 2015). Some states appear not to be genuinely entangled, and therefore two separable, and yet exhibit a rich multipartite entanglement structure for multipartitions in more than two parties (Gerke et al., 2016).

The particular case of Gaussian multimode states was thoroughly investigated with the help of symplectic group methods (Adesso and Illuminati, 2007a, 2007c; Franke-Arnold, Gatti, and Treps, 2013) and criteria based on symplectic invariants (Serafini, 2006). Whereas for bipartite Gaussian states the partial transpose criterion is a necessary and sufficient entanglement identifier (Peres, 1996), this is no longer the case for more than two parties: there are multipartite Gaussian states whose entanglement cannot be uncovered by the partial transposition (Werner and Wolf, 2001; DiGuglielmo et al., 2011). The logarithmic negativity, a measure of entanglement, can be directly calculated from

the covariance matrix, as well as the appropriate measure  $E$  that allows us to test the monogamy inequality for continuous variables (Coffman, Kundu, and Wootters, 2000). In addition, the difference  $E(A - BC) - E(A - B) - E(A - C)$  gives some information about higher-order entanglement (Adesso and Illuminati, 2007b). Multipartite steering can be also defined, calculated and used in a monogamy inequality (Xiang et al., 2017). The best way to study the detailed structure of entanglement in a given multimode state is to use criteria that are an extension of the well-known Duan criterion (Duan et al., 2000), detailed by van Loock and Braunstein (2000), van Loock and Furusawa (2003), Teh and Reid (2014), and Toscano et al. (2015) in terms of combinations of different quadrature operators, for example,  $\hat{X}_1 - \sum_i g_i \hat{P}_i$  and  $\hat{P}_1 + \sum_i g_i \hat{X}_i$ . Reconfigurable Gaussian entangled states have been experimentally produced, characterized, and used for quantum information purposes (van Loock and Furusawa, 2003; Menicucci, Flammia, and Pfister, 2008; Yokoyama et al., 2013; Chen, Menicucci, and Pfister, 2014; Titchener, Solntsev, and Sukhorukov, 2016; Cai et al., 2017).

Multipartite entanglement of non-Gaussian states has also been studied, for example, in terms of Mandel matrices that involve normally ordered fourth-order correlations (Ivan et al., 2011). Sufficient conditions for genuine multipartite Gaussian and non-Gaussian states have been derived (Shchukin and van Loock, 2015). For photon-added or photon-subtracted Gaussian states, which are the most studied CV non-Gaussian states, a hierarchy of inseparability criteria can also be used to precisely characterize the entangled state (Levi and Mintert, 2013; Valido, Levi, and Mintert, 2014) and the relations between the negativity of the Wigner function, purity, and entanglement (Walschaers et al., 2017a), involving higher statistical moments of the quadrature operators. The effect of mode-selective photon addition and subtraction on the propagation of entanglement over the quantum network was theoretically studied by Walschaers et al. (2018) and experimentally investigated by Ra et al. (2020). It turns out that the non-Gaussian character induced by photon subtraction does not spread farther than to the next-to-nearest-neighbor node in the cluster graph.

# IX. SOURCES OF MULTIMODE NONCLASSICAL STATES

In this section, to avoid cumbersome presentation we will essentially restrict ourselves to the continuous variable aspects of multimode nonclassical state generation.

# A. Mixture of single-mode nonclassical states

To generate any  $N$ -mode Gaussian state, a possibility is to start from a bunch of independent single-mode squeezed states followed by a linear  $N$ -port interferometer comprising beam splitters and phase shifters (Braunstein, 2005). This is true, in particular, for generating cluster states (Zhang and Braunstein, 2006). It has been shown (Reck et al., 1994) that any modal unitary operator can be constructed using a sequence of beam splitter transformations.

Multipartite entanglement and quantum networks can be created by this technique using a single squeezed state (van Loock and Braunstein, 2000) or several squeezed states

(van Loock, Weedbrook, and Gu, 2007; Armstrong et al., 2012; Su et al., 2014). Integrated optics and multimode fibers have also been used (Mohanty et al., 2017) in conjunction with spatially multiplexed detection of up to eight different spatial modes (Armstrong et al., 2012; Su et al., 2012). In the pulsed regime time delays can be used to mix different pulses in the same beam (Yokoyama et al., 2013). Because single-mode squeezers are now capable of reaching impressive amounts of squeezing of up to  $15\mathrm{dB}$  (Vahlbruch et al., 2016), this technique is attractive from an experimental point of view. Experimental implementations become more and more complex as  $N$  increases and lack flexibility because they are not simply reconfigurable.

# B. Parametric down-conversion

# 1. Interaction Hamiltonian

The most widely employed technique to directly generate, with a single device, multimode nonclassical states is to use twin-photon generation by parametric down-conversion in a nonlinear  $\chi^{(2)}$  crystal; see Chap. 7 of Grynberg, Aspect, and Fabre (2010). Using a discrete mode basis and assuming an undepleted pump, this process is described by the following effective interaction Hamiltonian, obtained by tracing out the degrees of freedom of the nonlinear matter:

$$
\hat {H} = \sum_ {\ell , \ell^ {\prime}} \left(G _ {\ell , \ell^ {\prime}} \hat {a} _ {\ell} ^ {\dagger} \hat {a} _ {\ell^ {\prime}} ^ {\dagger} + G _ {\ell , \ell^ {\prime}} ^ {*} \hat {a} _ {\ell} \hat {a} _ {\ell^ {\prime}}\right), \tag {93}
$$

where  $\hat{a}_{\ell}^{\dagger}$  and  $\hat{a}_{\ell'}^{\dagger}$  are creation operators of photons in modes  $f_{\ell}$  and  $f_{\ell'}$  (which can be either degenerate or nondegenerate) of respective frequencies  $\omega_{\ell}$  and  $\omega_{\ell'}$ .  $G_{\ell, \ell'} = G_{\ell', \ell} = a_{\ell, \ell'} \alpha_p(\omega_{\ell} + \omega_{\ell'})$ , where  $\alpha_p(\omega)$  is the pump field amplitude at frequency  $\omega$  and  $a_{\ell, \ell'}$  is a coefficient that depends on the nonlinear medium and the geometry of the interaction.

The Hamiltonian is a double sum of EPR entangling  $\hat{a}_{\ell}^{\dagger}\hat{a}_{\ell^{\prime}}^{\dagger}$  terms, so one expects entanglement to be generated between all pairs of twin modes for which the joint two-photon matrix  $G$  has significant matrix elements  $G_{\ell ,\ell '}$ . Indeed, in the weak pump approximation ( $G_{\ell ,\ell^{\prime}}\ll 1$ ) and vacuum state input, the state at the output of the crystal will be the entangled highly multimode twin-photon state

$$
\left| \Psi_ {\text {o u t}} \right\rangle = | 0 \rangle - i \frac {L}{\hbar c} \sum_ {\ell , \ell^ {\prime}} G _ {\ell , \ell^ {\prime}} | 1: f _ {\ell} \rangle \otimes | 1: f _ {\ell^ {\prime}} \rangle , \tag {94}
$$

where  $L$  is the crystal length.

(a) If the symmetrical matrix  $G$  is real, one can diagonalize it using an orthogonal transformation  $O$ , which is a special case of mode basis change

$$
O G O ^ {- 1} = \Lambda , \tag {95}
$$

where  $\Lambda$  is a real diagonal matrix of eigenvalues  $\lambda_{i}$ . Therefore, in the eigenmode basis with annihilation operators  $\vec{\hat{b}} = O^T\vec{\hat{a}}$ , the Hamiltonian is written as

$$
\hat {H} = \sum_ {i} \left(\lambda_ {i} \hat {b} _ {i} ^ {2} + \mathrm {H . c .}\right), \tag {96}
$$

where the eigenvalues  $\lambda_{i}$  are real. The eigenmodes are often called supermodes.

(b) If  $G$  is complex, using the Autonne-Takagi factorization method (Siegel, 1943; Cariolaro and Pierobon, 2016; Arzani, Fabre, and Treps, 2018) one can find a unitary matrix  $U$  (hence a mode basis transformation) such that

$$
U G U ^ {T} = \Lambda , \tag {97}
$$

with  $\Lambda$  again a diagonal real non-negative matrix. Using the mode transformation  $\vec{\hat{b}} = U^{\dagger}\vec{\hat{a}}$ , the Hamiltonian can be written in the new basis as in Eq. (96).

In both cases  $\hat{H}$  is in the new basis a sum of squeezing Hamiltonians, which means that the propagation of an initial vacuum state in the nonlinear crystal will lead to a final quantum state that is a tensor product of vacuum squeezed states, with the variance in decibels of the squeezed quadrature  $\hat{X}_i$  in mode  $i$  proportional to the eigenvalue  $\lambda_{i}$  (de Valcarcel et al., 2006; Wasilewski et al., 2006). The number of nonzero eigenvalues (i.e., the rank of the  $G$  matrix) gives the intrinsic number of nonvacuum modes. It turns out that this number is roughly equal to the aspect ratio of the  $G_{\ell ,\ell '}$  matrix (the ratio of its widths in the  $\omega_{\ell} + \omega_{\ell '}$  and  $\omega_{\ell} - \omega_{\ell '}$  directions).

(c) In some instances, such as in type II phase matching, for example, the  $2N \times 2N$  joint two-photon matrix  $G$  can be written in terms of  $N \times N$  block matrices of the form

$$
G = \left( \begin{array}{c c} \mathbb {0} & G _ {s i} \\ G _ {s i} ^ {*} & \mathbb {0} \end{array} \right). \tag {98}
$$

The interaction Hamiltonian is a sum of terms creating one photon in one of the signal modes  $f_{i}^{s}$  and one photon in one of the idler modes  $f_{j}^{i}$ . The singular value decomposition of matrix  $G_{si}$  is written as

$$
U _ {s} G _ {s i} U _ {i} ^ {T} = \Lambda_ {s i}, \tag {99}
$$

where  $U_{s}$  and  $U_{i}$  are unitary mode basis changes in the signal and idler parts of the modal space and  $\Lambda_{si}$  is the real diagonal matrix  $\mathrm{diag}(\lambda_1,\dots,\lambda_N)$ . The singular value decomposition thus generates two sets of  $N$  eigenmodes  $\{\pmb {f}_k^s\}$  and  $\{\pmb {f}_k^i\}$  that are EPR entangled with each other. They are the Schmidt modes (Sharapova et al., 2018) introduced in Sec. VIII. They form a mode basis in the signal and idler parts. One can show (Horoshko et al., 2019) that the eigenvalues of the joint two-photon matrix  $G$  are doubly degenerate, with eigenvectors  $(f_j^s\pm f_j^i) / \sqrt{2}$ , which are therefore both equally squeezed and mutually uncorrelated, with a squeezing factor in decibels proportional to  $\lambda_{j}$ . The number of nonzero terms in the Schmidt decomposition gives the intrinsic dimension of the generated multimode state; see Appendix B.

# 2. Different possible modes for entangled states

The entanglement generated by parametric down-conversion concerns different kinds of modes:

- Polarization modes, which we do not consider in this review.

- Spatial modes (Jedrkiewicz et al., 2004; Law and Eberly, 2004; Walborn et al., 2010), which can be the transverse modes of cavities (Kolobov, 2006) or multimode optical fibers (Jachura et al., 2014). This leads to nonclassical correlations between different parts of an optical image or between two images.  
- Time-frequency modes (Jiang, Treps, and Fabre, 2012), which lead to correlations between different spectral components of the light source.  
- Polarization, spatial, and/or temporal degrees of freedom at the same time, for example, polarization-transverse modes (Gabriel et al., 2011; Jedrkiewicz et al., 2012) and spectral-temporal-transverse modes (Perina, 2016).

Nonlinear effects in nonlinear crystals are usually weak and generate twin-photon states of the form of Eq. (94). If one uses a strong pulsed pump (Sharapova et al., 2018), multimode pulsed twin beams containing more than  $6 \times 10^{5}$  photons have been generated and used to conditionally generate sub-Poissonian light (Iskhakov et al., 2016). To enhance the effect, it is possible to use resonant cavities. We detail this configuration in Sec. IX.B.3.

# 3. Use of resonant optical cavities

Another possibility is to insert the crystal into a resonant cavity. The device is then an optical parametric oscillator (OPO), which produces above some pump threshold bright output beams in the twin modes  $\ell$  and  $\ell^{\prime}$  that are resonant with the cavity. As cavities are actually mode filters, there is often only one couple of twin modes that has such a resonant property, and the OPO generates below threshold a two-mode EPR state, or a squeezed vacuum single-mode state if the twin photons are generated in the same mode  $\ell$ . The squeezing or the entanglement increases more and more when one approaches the oscillation threshold from below.

To produce multimode nonclassical states of larger dimensionality (Lugiato and Gatti, 1993), one can use a cavity that simultaneously resonates on several couples of parametrically generated modes. Below threshold, the generated quantum state is a tensor product of squeezed vacuum states in each "supermode"  $i$ , with a squeezed quadrature noise equal to (Patera et al., 2010)

$$
\Delta X _ {i} ^ {2} = \left(\frac {\lambda_ {1} - r | \lambda_ {i} |}{\lambda_ {1} + r | \lambda_ {i} |}\right) ^ {2}, \tag {100}
$$

where  $r$  is the pump field amplitude normalized to the pump amplitude at threshold. Hence, the squeezing in the first supermode becomes very large when one approaches the threshold from below. All other modes of smaller but nonzero eigenvalue  $\lambda_{i}$  are also squeezed, but by smaller amounts and never perfectly.

If one uses cavities with spherical mirrors, the spatial eigenmodes that are the Hermite-Gauss modes  $\mathrm{TEM}_{pq}$ , cylindrical symmetry leads to  $(p + q)$ -mode degeneracy, which was exploited by Marte et al. (1998) and Lugiato and Marzoli (1995). These modes are entangled by the parametric interaction (Schwob et al., 1998; Lassen et al., 2007; Chalopin et al., 2011). Confocal cavities have a stronger degeneracy and resonate for any spatial mode of symmetrical shape (Martinelli

et al., 2003). Self-imaging cavities are resonant for any transverse shape of the electric field (Lopez et al., 2009).

Cavities are also filters in the spectral domain: they have equally spaced resonant frequencies and enhance not only resonant single frequency modes but also frequency combs: this leaves room for a possibly large number (more than  $10^{5}$  in realistic experimental conditions) of entangled frequency modes.

# 4. Use of pump modes of different shapes

In most experiments, the parametric medium is pumped by a monochromatic field so that the entangled signal and idler modes have to fulfill the relation  $\omega_{\ell} + \omega_{\ell^{\prime}} = \omega_{\mathrm{pump}}$ : one gets a set of independently entangled couples of signal and idler modes, but without any multipartite entanglement. The use of a bichromatic pump (Chen, Menicucci, and Pfister, 2014) allows physicists to greatly enhance, in a well controlled way, the number (up to 60) and the topology of entangled couples of modes: a whole zoology of cluster states (Pysher et al., 2011; Shahrokhshahi and Pfister, 2011) can thus be generated, with applications to measurement-based quantum computation (Menicucci, Flammia, and Pfister, 2008).

One may also use as a pump field an optical frequency comb with the same frequency spacing as the OPO cavity [synchronously pumped OPO (SPOPO)]. If, for example, the pump spectrum has a Gaussian envelope, the spectral shapes of the supermodes are the successive Hermite-Gauss functions (de Valcarcel et al., 2006; Patera et al., 2010). This scheme has been experimentally explored: principal modes have been determined, displaying strong squeezing on several of them (Pinel, Jian et al., 2012; Medeiros de Araujo et al., 2014; Roslund et al., 2014) and multimode entanglement in frequency (Cai et al., 2017) and time (Averchenko et al., 2011). The effective number of modes, as defined in Eq. (63), is of the order of 10. Thus, starting from a mode basis of single frequency modes, the number of which is roughly  $10^{5}$ , one ends up with a modal Hilbert space of a few units, a strong reduction in complexity that is useful, for example, when one wants to make the tomography of the generated state. Shaping the interaction in various ways, like using a spatial light modulator (Pe'er et al., 2005; Patera et al., 2012; Arzani, Fabre, and Treps, 2018), a nonlinear fiber (Finger et al., 2017), a Fabry-Perot cavity (Avella et al., 2014), or optimized poling (Dosseva, Cincio, and Brańczyk, 2016), permits one to modify at will the spectrum of the supermodes and the resulting multipartite entanglement characteristics.

# 5. Above threshold operation

Above threshold the OPO generates "bright" light (i.e., with a nonzero mean value) in the first resonant supermode (the one of largest gain and hence of largest eigenvalue  $\lambda_{1}$ ). When one increases further the pump power above threshold, gain clamping prevents the other modes from oscillating (Fabre et al., 2000), and they remain at a zero mean value. It has been shown that just above threshold the supermodes other than the first one remain in squeezed vacuum states, like just below threshold ones (Chalopin et al., 2010). Well above threshold, the signal and idler modes carry significant energy. Pump depletion cannot be neglected and leads to the onset of a supplementary quantum coupling between the pump mode

and the signal and idler modes. One then has a full three-wave mixing effect (Drummond and Kinsler, 1995), leading to three-mode entanglement between frequency modes, and six-mode entanglement between sideband modes, which have been predicted (Villar et al., 2006) and observed (Barbosa et al., 2018). Note that in this regime the Hamiltonian involves products of three annihilation and/or creation operators and induces an evolution that is not symplectic, which implies a direct generation of a non-Gaussian state and requires a weak oscillation threshold of the OPO (Drummond and Kinsler, 1995).

Above threshold and in the case of degenerate  $\mathrm{TEM}_{01}$  and  $\mathrm{TEM}_{10}$  spatial modes, the SPOPO is predicted to generate bright light in a nonclassical state (Navarrete-Benlloch, Patera, and Valcárcel, 2017) because of a symmetry-breaking effect between the transverse modes.

# C. Four-wave mixing

A drawback of second-order nonlinear effects is that they are weak and exist only in centrosymmetric crystals, which can be grown only in lengths of a few centimeters. This is not the case for media with third-order nonlinearities: nonlinear fibers can accumulate the nonlinear effect over long lengths, and atomic media can display large effects by taking advantage of the proximity of resonances between the pump light and atomic transitions. For such media there is usually no need to insert them into a resonant cavity, and therefore the multimode quantum effects are not hampered by the mode-filtering properties of the cavity.

To produce four-wave mixing effects, one needs the simultaneous presence of two pump beams. In the simple case where one can neglect the change of the quantum state of the medium in the presence of pumping light, assuming single frequency pump beams of amplitudes  $\alpha_{p1}$ ,  $\alpha_{p2}$  and in the undepleted pump regime, the system is described with an interaction Hamiltonian involving only light modes

$$
\hat {H} = \sum_ {\ell , \ell^ {\prime}} \left(A _ {\ell , \ell^ {\prime}} \alpha_ {p 1} \alpha_ {p 2} \hat {a} _ {\ell} ^ {\dagger} \hat {a} _ {\ell^ {\prime}} ^ {\dagger} + \mathrm {H . c .}\right). \tag {101}
$$

Twin photons are therefore created in modes labeled by  $\ell$  and  $\ell^{\prime}$ . Phase matching and energy conservation requirements do not usually completely constrain the couples of twin modes, so the light generated by four-wave mixing is often multimode. The Hamiltonian (101) has the same structure as the parametric Hamiltonian (93), with the same consequences on the generation of twin photons and entangled or squeezed multimode states.

The Kerr effect is a particular case of the four-wave mixing effect. It was one of the first techniques to generate bright squeezed beams using single transverse mode silica fibers (Levenson, Shelby, and Perlmutter, 1985). Its multimode character in the frequency domain has been investigated in the case of a pulsed pump (Opatny, Korolkova, and Leuchs, 2002) and frequency combs (Chembo, 2016). It was shown that a nonlinear variation of squeezing with respect to spectral filtering width, which is evidence of the generation of a multimode state, as explained in Sec. V.C. A complete time-frequency mode analysis was performed by Guo et al. (2015). Here the four-wave mixing characteristics can be

appropriately tailored to meet specific purposes, for example, by adjusting the spectral profile of the twin photons by using a specific pump shape and design of the photonic crystal fiber (Cui, Li, and Zhao, 2012).

In the temporal soliton regime, reached by using short and intense pulses in optical fibers, squeezing (Drummond et al., 1993) and spectral quantum correlations between different parts of the spectrum have been observed (Spälter et al., 1998), whereas in the spatial soliton regime, spatial quantum correlations between different transverse parts of the beam have been predicted (Trep's and Fabre, 2000). Such spatial correlations may actually improve the quantum noise reduction by filtering an appropriate transverse part of the spatial soliton (Mecozzi and Kumar, 1998).

The technique of four-wave mixing in a hot rubidium vapor using two intense pump beams with optimized frequencies, initiated by the NIST group (Boyer, Marino, and Lett, 2008), provides single pass parametric gains of the order of 4 (McCormick et al., 2007). It generates strong multiple correlations (Qin et al., 2014), multimode entanglement with a record value of  $9.2\mathrm{dB}$  (Glorieux et al., 2011) of intensity difference fluctuations below the vacuum level, and localized squeezing (Liu et al., 2011; Embrey et al., 2015). It has been used, for example, to generate entangled images (Boyer, Marino, and Lett, 2008; Boyer et al., 2008). Here pump shaping, implemented simply by using several pump beams of different directions intersecting in the Rb cell, allowed experimentalists to generate multipartite-entangled beams of various topologies (Qin et al., 2014; Wang, Fabre, and Jing, 2017). The effect can be enhanced up to  $9\mathrm{dB}$  by modulating the Rb energy levels using additional lasers (Zhang et al., 2017).

Other kinds of nonlinear devices give rise to different shapes of Schmidt modes. One can use, for example, four-wave mixing in argon-filled hollow core fibers (Finger et al., 2017).

# D. Multimode lasers

Lasers generate light that can be either single mode or multimode depending on the gain spectral profile, the properties of intermode coupling, and the insertion of intracavity mode filters, but most often their nonclassical properties are hidden by the large excess of classical fluctuations in the pumping process responsible for the population inversion. Under certain conditions, when the pump noise is greatly reduced lasers can generate "sub-Poissonian light," i.e., beams of light having intensity fluctuations below the shot noise level. This is achieved by reducing the Johnson noise of the electrical current pumping high efficiency diode lasers. These diode lasers usually emit on several highly anticorrelated frequency modes (Marin et al., 1995). The same characteristics have also been observed in vertical cavity surface emitting lasers, with are characterized by strong correlations between transverse modes (Hermier et al., 1999).

# X. DETECTION OF MULTIMODE QUANTUM STATES

# A. Direct photodetection

The observable  $\hat{N}(\boldsymbol{r}, t)$  associated with photodetection made on a small area around point  $\boldsymbol{r}$  (of dimensions close

to the wavelength) and at time  $t$  on a given beam by a photodetector of unity quantum efficiency is proportional to  $\hat{E}^{(+)}(\boldsymbol {r},t)^{\dagger}\hat{E}^{(+)}(\boldsymbol {r},t)$  (Glauber, 1963; Mollow, 1968). More precisely and expressed in numbers of photon counts, using Eq. (31) one has

$$
\hat {N} (\boldsymbol {r}, t) = \sum_ {n, n ^ {\prime}} \hat {b} _ {n} ^ {\dagger} \hat {b} _ {n ^ {\prime}} f _ {n} ^ {*} (\boldsymbol {r}, t) f _ {n ^ {\prime}} (\boldsymbol {r}, t). \tag {102}
$$

Note that this observable contains crossed terms like  $\hat{b}_n^\dagger \hat{b}_{n'}$ . Its mean value is a linear combination of matrix elements of the coherency matrix  $\hat{\Gamma}^{(1)}$ . The local photodetection signal is therefore sensitive to the correlations between the different modes. These correlations could be extracted by measuring the intensity correlations at the different couples of points in the transverse plane. It is only in the eigenmode basis of the coherency matrix that it appears as a sum of contributions of different modes.

The total photodetection observable  $\hat{N}$  is associated with the signal given by a photodetector of unit quantum efficiency averaged over its transverse surface  $S$ , which is supposed to be much larger than the beam area, and over an aperture time  $T$  that is supposed to be much longer than its duration. We call such a device a bucket detector. It is given by

$$
\hat {N} = \sum_ {n} \hat {b} _ {n} ^ {\dagger} \hat {b} _ {n} \tag {103}
$$

thanks to the mode orthogonality when one integrates over transverse coordinates and longitudinal coordinate  $z = ct$ . The detector counts the total amount of photons present in the beam, which is a quantity independent of the choice of the mode basis, as we saw previously. It does not give us any information about the modal properties of the quantum state.

# B. Balanced homodyne detection

Some of the interest in multimode systems resides in the fact that they are likely to carry in a parallel way much more information than a single-mode system. It is therefore important to find the best way to extract from the multimode system pieces of information about any single mode of interest. Balanced homodyne detection gives precisely this possibility.

Consider the well-known balanced homodyne detection scheme in the context of multimode quantum optics: the beam to measure is combined with a local oscillator (LO) on a  $50\%$  beam splitter. The observable  $\hat{N}_{-}$  associated with the difference between the photodetection signals  $\hat{N}_A$  and  $\hat{N}_B$  recorded by two bucket detectors placed on output beams  $A$  and  $B$  and integrated over transverse space and time can be expressed, using the well-known input-output relations of a beam splitter, as

$$
\begin{array}{l} \hat {N} _ {-} = \hat {N} _ {A} - \hat {N} _ {B} \\ = \sum_ {n} \left(\hat {b} _ {n, A} ^ {\text {i n} \dagger} \hat {b} _ {n, B} ^ {\text {i n}} + \hat {b} _ {n, B} ^ {\text {i n} \dagger} \hat {b} _ {n, A} ^ {\text {i n}}\right). \tag {104} \\ \end{array}
$$

Equation (104) is valid in any mode basis provided that the modes  $\mathbf{f}_{n,A}(\mathbf{r},t)$  and  $\mathbf{f}_{n,B}(\mathbf{r},t)$  forming the mode basis for

beams  $A$  and  $B$  impinging on the beam splitter are matched, meaning that the mode  $\mathbf{f}_{n,A}(\mathbf{r},t)$  associated with  $\hat{b}_{n,A}^{\mathrm{in}}$  is the "mirror mode" of the mode  $\mathbf{f}_{n,B}(\mathbf{r},t)$  associated with  $\hat{b}_{n,B}^{\mathrm{in}}$ , using as a mirror the surface of the beam splitter (symmetrical spatial shapes, identical temporal shapes). One sends on the input beam  $A$  the multimode light state, pure or mixed, that one wants to characterize, and on the input beam  $B$  a single-mode state of light (a local oscillator, or LO), which is made of vacuum in all modes except for a coherent state  $||\alpha |e^{i\phi}\rangle$  in the  $j$ th mode. We now introduce the fluctuation operators of the form  $\delta \hat{O} = \hat{O} -\langle \hat{O}\rangle$ . If the local oscillator intensity  $|\alpha |^2$  is much larger than the vacuum fluctuations and the mean amplitude of the multimode light beam, one can neglect all terms except the ones proportional to  $|\alpha |$ . The fluctuations of the measured homodyne signal are then

$$
\begin{array}{l} \delta \hat {N} _ {-} \simeq | \alpha | \left(\delta \hat {b} _ {j, A} ^ {\mathrm {i n} \dagger} e ^ {i \phi} + \delta \hat {b} _ {j, A} ^ {\mathrm {i n}} e ^ {- i \phi}\right) \\ = | \alpha | (\delta \hat {X} _ {j} \cos \phi + \delta \hat {P} _ {j} \sin \phi) = | \alpha | \delta \hat {X} _ {j \phi}. \tag {105} \\ \end{array}
$$

Equation (105) shows that the balanced homodyne detection setup allows us to access the fluctuations of the quadrature operator  $\delta \hat{X}_{j\phi}$  even if the multimode state under study has comparable or larger components in many other modes: the homodyne detection using bucket detectors is actually a projective measurement on the LO mode.

On the other hand, if the local oscillator is in a mode  $\mathbf{g}_{\mathrm{LO}}(\mathbf{r},t)$  that differs from all modes of the basis  $\{\pmb {f}_n\}$ , one has in the case of a real value of the overlap integral  $\vec{f}_n^{T*}\cdot \vec{g}_{\mathrm{LO}}$  (Bennink and Boyd, 2002)

$$
\langle \delta \hat {N} _ {-} ^ {2} \rangle = | \alpha | ^ {2} \sum_ {n} \left(\vec {f} _ {n} ^ {T *} \cdot \vec {g} _ {\mathrm {L O}}\right) ^ {2} \langle \left(\delta \hat {X} _ {n \phi} ^ {\text {i n}}\right) ^ {2} \rangle . \tag {106}
$$

Shapiro and Shakeel (1997) investigated ways to optimize the LO shape to get the maximum squeezing effect. Polycarpou et al. (2012) analyzed the single temporal mode of a heralded single photon by homodyne detection using a pulse-shaped LO, the spectral-temporal shape of which is then algorithmically optimized to get the maximum overlap.

# C. Determination of quadrature covariance and coherency matrix elements

We show now that it is possible, using a series of homodyne measurements with different shapes of local oscillator modes, to determine all second-order correlation functions characterizing the multimode state of light under study.

First, from the measurement of the homodyne signal variance  $\langle \delta \hat{N}_-^2\rangle$  as a function of the LO phase  $\phi$ , one easily extracts the quadrature variances  $\langle \delta \hat{X}_n^2\rangle$  and  $\langle \delta \hat{P}_n^2\rangle$  as well as the  $X - P$  correlation  $\langle \delta \hat{X}_n\delta \hat{P}_n\rangle$  in mode  $n$ . Then, to determine the correlations between modes  $m$  and  $n$ , one makes another homodyne measurement, now using as the LO mode a combination of the two modes  $f_{\mathrm{LO}} = (f_n + f_m) / \sqrt{2}$ , which gives information about the multimode state projected on this new mode, i.e., on the variances  $V_{Xmn} = \langle (\delta \hat{X}_n + \delta \hat{X}_m)^2\rangle$  and  $V_{Pmn} = \langle (\delta \hat{P}_n + \delta \hat{P}_m)^2\rangle$  and on the correlation  $C_{XPMn} = \langle (\delta \hat{X}_n + \delta \hat{X}_m)(\delta \hat{P}_n + \delta \hat{P}_m) + (\delta \hat{P}_n + \delta \hat{P}_m)(\delta \hat{X}_n + \delta \hat{X}_m)\rangle / 2$ .

The matrix elements of the quadrature covariance matrix are then given by

$$
\left. \right.\left\langle \delta \hat {X} _ {n} \delta \hat {X} _ {m} \right\rangle = \left(V _ {X m n} - \left\langle \delta \hat {X} _ {n} ^ {2} \right\rangle - \left\langle \delta \hat {X} _ {m} ^ {2} \right\rangle\right) / 2
$$

$$
\left. \left\langle \delta \hat {P} _ {n} \delta \hat {P} _ {m} \right\rangle = \left(V _ {P m n} - \left\langle \delta \hat {P} _ {n} ^ {2} \right\rangle - \left\langle \delta \hat {P} _ {m} ^ {2} \right\rangle\right) / 2. \right. \tag {107}
$$

Finally, to evaluate the  $X_{n}P_{m}$  correlations, one uses the same procedure as that used for the  $X_{n}X_{m}$  and  $P_{n}P_{m}$  correlations, but now with another series of homodyne measurements with LO modes  $f^{\prime}_{\mathrm{LO}} = (f_n + if_m) / \sqrt{2}$  including a phase shifted  $f_{m}$  mode.

The matrix elements of the coherency matrix  $\Gamma^{(1)}$  can also be determined from the series of homodyne measurements using Eqs. (107) and (50).

It is thereby possible to get the full correlation matrices using a series of homodyne measurements (for example, one must use 100 choices of different LO modes for ten modes). These measurements must be made sequentially and require therefore that the quantum state generator is stable over the duration of the measurements. The quantum state characterized by this matrix is unfortunately destroyed by the measurement, which prevents this technique from being used in experiments involving conditional measurements, and, in particular, in measurement-based quantum computing.

Note that with the help of a beam splitter and two homodyne detectors at its two outputs it is possible to measure at the same time  $\langle \delta X_j^2\rangle$  and  $\langle \delta P_j^2\rangle$ , but this cannot be done without adding excess noise coming from vacuum fluctuations at the input of the beam splitter, as  $X_{j}$  and  $P_{j}$  are noncommuting quantities that cannot be measured exactly simultaneously. This method is useful for measuring classical noises that are significantly larger than the vacuum fluctuations. One can then extract from these measurements the principal noise modes that govern the dynamics of a classical light source. This has been achieved, in particular, for modelocked lasers (Schmeissner et al., 2014). Note that the excess noise can be avoided by using correlated homodyne measurements (Shchukin and Vogel, 2006).

# D. Spectral homodyne and resonator detection

In the case of stationary light sources (continuous wave or periodic), homodyne detection is often followed by a spectral analysis of the fluctuating signal, which allows us to measure the noise spectral density  $S(\Omega)$  of the homodyne signal fluctuations. For example, when the LO phase  $\phi$  is zero  $S(\Omega)$  is equal to  $S(\Omega) = \langle \delta \hat{X}_{\Omega}^{2}\rangle$ , where

$$
\delta \hat {X} _ {\Omega} = \frac {1}{\sqrt {2 \pi}} \int d t e ^ {i \Omega t} \delta \hat {X} (t). \tag {108}
$$

It is easy to show that this measured signal depends on the properties of sideband modes, which are quasimonochromatic frequency modes at frequency  $\omega_0 \pm \Omega$  (within the frequency bandwidth  $\Delta \Omega$  of the spectrum analyzer), where  $\omega_0$  is the optical carrier frequency and  $\Omega$  is the Fourier analysis frequency, usually in the megahertz range. More precisely, if one calls  $\hat{a}_{\omega}$  the annihilation operator in the frequency mode of frequency  $\omega$ , one has

$$
\delta \hat {X} _ {\Omega} = \hat {a} _ {\omega_ {0} + \Omega} + \hat {a} _ {\omega_ {0} - \Omega}. \tag {109}
$$

A noise spectrum of the homodyne signal, apparently a technique to characterize single-mode fields, actually gives a highly multimode information about couples of sideband modes. For example, squeezing of noise frequency components in a given Fourier frequency range  $(\langle \delta \hat{X}_{\Omega}^{2}\rangle < 1$  for  $\Omega \in [\Omega_1,\Omega_2])$  can actually be seen as  $(\Omega_{2} - \Omega_{1}) / \Delta \Omega$  independent couples of EPR correlated sideband modes.

However, it can be shown that spectral homodyne detection does not give complete information about the sideband modes (Barbosa et al., 2013). More precisely, it measures the properties of the input quantum state partially traced over the mode associated with  $\hat{a}_{\omega_0 + \Omega} - \hat{a}_{\omega_0 - \Omega}$ , which is orthogonal to  $\delta \hat{X}_{\Omega}$ . There is another detection technique, called resonator detection, that gives access to complete information about the frequency modes. It consists of measuring the intensity fluctuations of the beam to analyze after it has been reflected on a slightly off-resonant Fabry-Perot cavity, the length of which is scanned. The off resonance unbalances the two sidebands and reveals a possible asymmetry between them, which is not possible with the homodyne detection. Sideband modes, although close to each other in frequency, can be separated and studied individually using interferometric techniques (Huntington et al., 2005).

# E. Multiplexed detection

# 1. Implementation

Homodyne detection is a destructive measurement that prevents any further processing of the same quantum state, so a "single shot" detection of several observables on the same quantum system, which we call multiplexed detection, is highly desirable, especially if one wants to take advantage of the multimode aspect of the generated light. Multiplexed detection can be simply implemented when the different modes of the light can be spatially separated: one inserts homodyne detection devices into all or some of the different modes (Yukawa et al., 2008; Su et al., 2012, 2014). In this configuration the different measurements do not completely destroy the quantum state. One can also postselect a subset of recorded data to herald a specific quantum state (Aichele, Lvovsky, and Schiller, 2002; Laurat et al., 2003). One can also use the information contained in the measurements to correct by a feed-forward technique a mode that has been left unmeasured, for example, in sub-Poissonian bright beam generation (Mertz et al., 1990) or in teleportation (Furusawa et al., 1998).

When the multimode state is propagating in a single spatial beam, different kinds of multiplexed photodetectors can be used: CCD cameras (Peñina et al., 2012) or photodiode arrays (Beck, 2000; Dawes and Beck, 2001; Armstrong et al., 2012) for spatial modes, and time resolved detectors for temporal modes. They allow one to record the intensity fluctuations on pixels of area  $\delta x^2$ , the time bins of duration  $\delta t$ , and the correlations between the fluctuations of different pixels. In addition, if one inserts a dispersive device like a prism in front of the array detector, one can measure the fluctuations of

different frequency bands of spectral width  $\delta \omega$  (Ferrini et al., 2013).

# 2. Multiplexed homodyne signal

The modes corresponding to the detection scheme just described are the pixels, time bins, and frequency band modes: they are normalized modes  $\mathbf{v}_j(\mathbf{r},t)$  that are zero outside the detection domain (in space, time, or frequency) and constant inside and that we call in a general way bin modes. Consider the set  $(\mathbf{v}_j(\mathbf{r},t))$  of such bin modes, which are not overlapping and which cover the whole detection domain, and the corresponding annihilation operators  $\hat{d}_j$ . Such a detection acts as a low pass filter: the bin modes constitute a complete and orthonormal set of modes in the subspace of electric fields that have an upper limit  $1 / 2\delta x$  in the case of pixels,  $1 / 2\delta t$  in the case of time bins, or  $1 / 2\delta \omega$  in the case of frequency bands. The intensity  $\hat{N}_j$  in terms of photon number recorded on the bin mode labeled by  $j$ , deduced from Eq. (102), is

$$
\hat {N} _ {j} = \hat {d} _ {j} ^ {\dagger} \hat {d} _ {j} \tag {110}
$$

because the other modes vanish on the  $j$ th detector. This relation, without summation over modes, is valid only for operators  $\hat{d}_j^\dagger \hat{d}_j$  defined in the bin-mode basis.

We now consider the balanced homodyne detection setup that uses a single-mode LO in quantum state  $|\Psi_{\mathrm{LO}}\rangle$  and multiplexed detectors instead of bucket detectors. The measurement of the intensity difference between analog pixel-time-frequency bins  $j$  on the two output beams of the beam splitter is now given by, omitting for simplicity the superscript "in",

$$
\delta \hat {N} _ {-, j} \simeq \left\langle \Psi_ {\mathrm {L O}} \right| \hat {d} _ {j, b} \left| \Psi_ {\mathrm {L O}} \right\rangle \delta \hat {b} _ {j, a} ^ {\dagger} + \mathrm {H . c}. \tag {111}
$$

We take as before the LO to be a coherent state  $||\alpha |e^{i\phi}\rangle$  in mode  $\vec{g}_{\mathrm{LO}}$  that is assumed to vary slowly over the extension of a bin. We have seen that it may be also written as a tensor product of coherent states in any other mode basis, including the bin basis. One can show

$$
\langle \Psi_ {\mathrm {L O}} | \hat {d} _ {j, b} | \Psi_ {\mathrm {L O}} \rangle = \left(\vec {v} _ {j} ^ {T *} \cdot \vec {g} _ {\mathrm {L O}}\right) | \alpha | e ^ {i \phi}. \tag {112}
$$

Assuming the modal inner product to be real, one finally has

$$
\delta \hat {N} _ {-, j} \simeq | \alpha | \left(\vec {v} _ {j} ^ {T *} \cdot \vec {g} _ {\mathrm {L O}}\right) \delta \hat {X} _ {j \phi}. \tag {113}
$$

The condition of validity of this expression is that  $|\alpha| (\vec{v}_j^{T*} \cdot \vec{g}_{\mathrm{LO}})$  is large enough in relation to the vacuum fluctuations. Its exact value is taken care of by a proper normalization of the homodyne signal.

A computer memory then stores in parallel the instantaneous different detection signals  $\delta \hat{N}_{-j}$  for all of the bin modes and for a given LO phase  $\phi$ , for example,  $\phi = 0$ , which give access to the  $\hat{X}_j$  quadrature. By a time integration of the square of the fluctuations over a time window  $T$ , one then gets in a single shot all variances  $\langle \delta X_j^2\rangle$ ; by a time integration of the product of the recorded fluctuations  $\delta X_{j}$  and  $\delta X_{j'}$  one gets the cross-correlations  $\langle \delta X_j\delta X_{j'}\rangle$ , i.e., a quarter of the quadrature

covariance matrix. The second moments of the  $P$  quadrature are obtained with a second single shot measurement with a LO phase  $\phi = \pi /2$ . To measure the cross-correlations  $\langle \delta X_j\delta P_{j'}\rangle$  for all  $j'$ , one needs to dephase by  $\pi /2$  the part of the local oscillator that will impinge on bin  $j$  after the beam splitter. This can be done by using a spatial light modulator (SLM) or a phase plate on the LO beam.

If the LO phase  $\phi$  is varied on a timescale shorter than  $T$ , one gets phase averaged correlations, which directly give the value of  $\langle \delta X_{j}\delta X_{j^{\prime}}\rangle +\langle \delta P_{j}\delta P_{j^{\prime}}\rangle$ , i.e., the real part of the coherency matrix.

# 3. Multiplexed mode discrimination via postprocessing

We now consider more generally a multimode quantum state  $|\Psi \rangle$ , described in a given mode basis  $\{\pmb{u}_l\}$ , that one wants to characterize through multiplexed homodyne detection. The question is which set of quadrature operators, and for which mode basis, can be accessed simultaneously for a given measurement scenario. A multipixel homodyne detection performs a measurement in the bin-mode basis  $\{\nu_j\}$ , which is related to the initial mode basis through a modal unitary operator  $U_b$ . This matrix depends on the optical arrangement between the quantum state to be characterized and the detector. It can be adjusted by changing the experimental setup. But for a given setup, shaping the local oscillator and postprocessing on a computer allows for a large variety of quadrature outcomes. In particular, one can do the following:

- Shape the local oscillator impinging on each pixel of the multipixel detector, and thus the modal projection. This induces a change in the bin-mode basis  $\{\nu_{j}\}$  that is measured. This effect can be mathematically included in the matrix  $U_{b}$ .  
- Add a phase shift  $e^{i\psi_j}$  on each bin mode  $\nu_j$ . This is done phase shifting by  $e^{i\psi_j}$  the local oscillator beam impinging on the corresponding pixel of the multipixel detector. We call  $\Delta_{\mathrm{LO}}$  the associated diagonal unitary operation on the modes.  
- Digitally recombine the electronic signals coming from each bin by multiplying them by real gains, which amounts to applying an orthogonal matrix  $O$  to the vector of measured quadratures of modes  $\{v_j\}$ .

We define the mode basis as

$$
\vec {c} _ {n} = \sum_ {l = 1} ^ {N _ {p}} \left(O \Delta_ {\mathrm {L O}} U _ {b}\right) _ {n} ^ {l} \vec {u} _ {l} = \sum_ {l = 1} ^ {N _ {p}} \left(U _ {M P H D}\right) _ {n} ^ {l} \vec {u} _ {l}, \tag {114}
$$

where  $N_{p}$  is the number of pixel detectors. The data processing technique just described allows us to access simultaneously the amplitude quadrature fluctuations in the set of modes  $\{\pmb{c}_n\}$ , even though such modes have not been physically extracted from the multimode beam (Ferrini et al., 2013). This technique is useful for gaining access to the nodes of cluster states that are embedded in the multimode quantum state; see Sec. XIV. It can be shown (Armstrong et al., 2012) that many, but not all, possible modal unitary transformations  $U$  can be emulated using this procedure, namely, those such that  $U_{b}U^{T}UU_{b}^{\dagger} = D$ , where  $D$  is a diagonal matrix with unit modulus complex elements (Ferrini et al., 2013).

Finally, we stress that data processing is not limited to linear combinations of data. Nonlinear combinations can also be performed to implement non-Gaussian operations using feedforward techniques (Miyata et al., 2016).

# F. Two-photon detection

In addition to quantum fluctuation measurements, joint two-photon detection is a privileged tool for revealing the nonclassical properties of a quantum state of light. The observable  $\hat{W} (\boldsymbol {r},t,\boldsymbol{r}^{\prime},t^{\prime})$  associated with the double detection at times  $t$  and  $t^\prime$  made by two detectors A and B at positions  $(\boldsymbol {r},t)$  and  $(\boldsymbol {r}^{\prime},t^{\prime})$  is given by (Glauber, 1963)

$$
\hat {W} (\boldsymbol {r}, t, \boldsymbol {r} ^ {\prime}, t ^ {\prime}) = \hat {E} ^ {(+) \dagger} (\boldsymbol {r}, t) \hat {E} ^ {(+) \dagger} \left(\boldsymbol {r} ^ {\prime}, t ^ {\prime}\right) \hat {E} ^ {(+)} \left(\boldsymbol {r} ^ {\prime}, t ^ {\prime}\right) \hat {E} ^ {(+)} (\boldsymbol {r}, t). \tag {115}
$$

When integrated over time and transverse space, Eq. (115) gives a "total double click" observable equal to

$$
\hat {W} = \sum_ {m _ {A}, m _ {B}} \hat {b} _ {m _ {A}} ^ {A \dagger} \hat {b} _ {m _ {B}} ^ {B \dagger} \hat {b} _ {m _ {A}} ^ {A} \hat {b} _ {m _ {B}} ^ {B}, \tag {116}
$$

which does not depend on the choice of the mode basis and has a mean value that is zero for a single-photon state and equal to the square of the mean photon number for any multimode coherent state (as defined inSec. V.A.3).

We now consider the Hong-Ou-Mandel (HOM) configuration (Hong, Ou, and Mandel, 1987): the two detectors are measuring photon coincidences between the two outputs of a  $50\%$  beam splitter. More details concerning the derivations are provided in Appendix C. We assume in addition that the detectors are "slow" so that they lose the information about the exact arrival time of each photon. We can then use Eq. (115) for a "bucket detector" obtained by integration over times  $t$  and  $t'$ .

(a) We first consider the case where two uncorrelated single photons in modes  $g_{A}$  and  $g_{B}$  impinge on the two input ports of the beam splitter (Bylander, Robert-Philip, and Abram, 2003; Legero et al., 2003; Beugnon et al., 2006; Kaltenbaek et al., 2006). The calculation, which is outlined in Appendix C, yields the following expression for the normalized two-photon detection rate for zero difference between the two-photon paths  $g^{(2)}(0)$ :

$$
\begin{array}{l} g ^ {(2)} (0) = \frac {1}{2} \left(1 - \left| \vec {g _ {A}} ^ {T *} \cdot \vec {g _ {B}} \right| ^ {2}\right) \\ = \frac {1}{2} (1 - | \langle 1: \mathbf {g} _ {A} | 1: \mathbf {g} _ {B} \rangle | ^ {2}). \tag {117} \\ \end{array}
$$

The HOM destructive interference is perfect only when  $|\vec{g}_A^{T*} \cdot \vec{g}_B|^2 = 1$ , implying that  $\vec{g}_A = \vec{g}_B$  within a phase term (Beugnon et al., 2006; Ou, 2017): single photons "coalesce" on the beam splitter only when they are in modes that are strictly identical, for both their space and time dependences. If the modes are orthogonal, one retrieves the classical value  $1/2$  for the normalized coincidence rate.

(b) There is a second physical situation for HOM interference, which was actually the one of the initial experiment (Hong, Ou, and Mandel, 1987), consisting of the use of entangled two-photon states generated by parametric

down-conversion. The calculation is outlined in Appendix C. Using the Schmidt decomposition of the input state one finds that the coincidence rate for the zero path length difference between the two arms vanishes not only when the input quantum state is a product of single-mode states, but also when it is entangled, provided that all Schmidt modes of the parties  $A$  and  $B$  have identical space-time dependences:  $\forall i\vec{g}_A^i = \vec{g}_B^i$ . Such a perfect two-by-two matching for all Schmidt modes of the two beams is achieved when there is total symmetry with respect to the exchange between the signal and idler parts A and B, i.e., when the matrix  $G_{si}$  introduced in Eq. (98) is symmetric.

# XI. MULTIMODE AMPLIFICATION AND ATTENUATION

# A. Effect on squeezing

The quantum aspects of single-mode attenuation and amplification have been studied and understood for a long time (Caves, 1982, 2012): losses, as well as phase-insensitive amplification, lead to a necessary coupling between the considered mode and the outer world, which results in added noise, responsible for a reduction in squeezing and a minimum  $3\mathrm{dB}$  noise penalty in the noise figure of the amplifier. Only phase-sensitive amplifiers are authorized to be noiseless by the laws of quantum mechanics (Marino and Lett, 2012). It is therefore important to see in which respect these properties extend to the multimode case (Lane et al., 1983), considering the fact that many kinds of multimode optical amplifiers have been developed in recent years, for example, erbium-doped fiber amplifiers (Nykolak et al., 1991), parametric amplification in crystals (Allevi et al., 2006) or fibers (Guasoni, 2016), and image amplifiers based on four-wave mixing in atomic vapors (Gigan et al., 2005; Boyer et al., 2008; Ferrini et al., 2014).

In this section, we mainly follow the argument given by Leuchs, Andersen, and Fabre (2006). We restrict ourselves to the case of a phase-insensitive multimode attenuator or amplifier, which is characterized by an intensity multiplicative factor  $P$ , acting on an  $N$ -mode modal space with mode basis  $\vec{f}_m$  and corresponding annihilation operators  $\hat{b}_m$ . At the classical level, the output field  $E^{(+)\mathrm{out}}$  is equal to  $\sqrt{P} E^{(+)\mathrm{in}}$  for any input  $E^{(+)\mathrm{in}}$ . At the quantum level, the corresponding relation for the column vector of annihilation operators in the Heisenberg representation

$$
\vec {\hat {b}} ^ {\text {o u t}} = \sqrt {P} \vec {\hat {b}} ^ {\text {i n}} \tag {118}
$$

cannot be valid, except when  $P = 1$ , because it is not a commutator preserving relation. One therefore needs to introduce a set of  $N'$  ancilla modes characterized by a mode basis  $\vec{g}_n$  and corresponding annihilation operators  $\hat{a}_n$ , which are coupled to the amplifier modes. The actual input-output relation is then written as

$$
\vec {b} ^ {\text {o u t}} = \sqrt {P} \vec {b} ^ {\text {i n}} + \mathcal {L} \vec {a} ^ {\text {i n}} + \mathcal {M} \vec {a} ^ {\text {i n ,} \dagger}, \tag {119}
$$

where  $\mathcal{L}$  and  $\mathcal{M}$  are  $N^{\prime}$  lines and  $N$  column matrices. The canonical commutation relations

$$
[ \vec {\hat {b}} ^ {\text {o u t}}, \vec {\hat {b}} ^ {\dagger \text {o u t}} ] = \mathbf {1} _ {N} \tag {120}
$$

are ensured when

$$
\mathcal {M} \mathcal {M} ^ {\dagger} - \mathcal {L} \mathcal {L} ^ {\dagger} = (P - 1) \mathbf {1} _ {N}. \tag {121}
$$

We now consider the amplifier case  $P > 1$  and define a new column vector of operators

$$
\vec {c} ^ {\text {i n}} = \frac {1}{\sqrt {P - 1}} \left(\mathcal {L} ^ {\dagger} \vec {a} ^ {\text {i n}, \dagger} + \mathcal {M} ^ {\dagger} \vec {a} ^ {\text {i n}}\right). \tag {122}
$$

One deduces from Eq. (121) that

$$
[ \hat {\vec {c}} ^ {\text {i n}}, \vec {\hat {c}} ^ {\text {i n ,} \dagger} ] = \mathbf {1} _ {N} \tag {123}
$$

so that  $\vec{c}^{\mathrm{in}}$  is a column vector of bosonic annihilation operators associated with modes that can be called noise modes. One can finally write

$$
\vec {b} ^ {\text {o u t}} = \sqrt {P} \vec {b} ^ {\text {i n}} + \sqrt {P - 1} \vec {c} ^ {\text {i n ,} \dagger}. \tag {124}
$$

By definition,  $\vec{b}^{\mathrm{out}}$  and  $\vec{b}^{\mathrm{in}}$  are of dimension  $N$ , whereas  $\vec{c}^{\mathrm{in}}$  is of dimension  $N'$ , which implies that  $N' = N$ .

In the attenuator case  $P < 1$  one has similarly

$$
\vec {\hat {b}} ^ {\text {o u t}} = \sqrt {P} \vec {\hat {b}} ^ {\text {i n}} + \sqrt {1 - P} \vec {\hat {d}} ^ {\text {i n}}, \tag {125}
$$

with the operators

$$
\vec {\hat {d}} ^ {\text {i n}} = \frac {1}{\sqrt {1 - P}} \left(\mathcal {L} \vec {\hat {a}} ^ {\text {i n}} + \mathcal {M} \vec {\hat {a}} ^ {\text {i n ,} \dagger}\right) \tag {126}
$$

satisfying the bosonic commutation relations

$$
[ \vec {\hat {d}} ^ {\text {i n}}, \vec {\hat {d}} ^ {\text {i n ,} \dagger} ] = \mathbf {1} _ {N} \tag {127}
$$

and

$$
[ \hat {\vec {d}} ^ {\text {i n}}, \hat {\vec {d}} ^ {\text {i n}} ] = 0. \tag {128}
$$

We therefore find that, in the general case of  $N$ -mode linear optical systems written in any mode basis, there are  $N$  associated ancilla modes that independently bring excess noise to the "useful" modes. These noise modes depend on the physical system considered and are not necessarily associated with optical modes.

If the noise modes are in the vacuum state, one can write a simple relation for the evolution of the coherency matrix, as well as for the quadrature covariance matrix valid in any mode basis and in both the attenuator and amplifier cases:

$$
\boldsymbol {\Gamma} ^ {(1), \text {o u t}} = P \boldsymbol {\Gamma} ^ {(1), \text {i n}} + | P - 1 | \mathbf {1} _ {N}, \tag {129}
$$

$$
\boldsymbol {\Gamma} _ {Q} ^ {\text {o u t}} = P \boldsymbol {\Gamma} _ {Q} ^ {\text {i n}} + | P - 1 | \mathbf {1} _ {2 N}. \tag {130}
$$

As in the single-mode case, an energy gain  $P$  of 2 is enough to bring above shot noise a highly squeezed input state, even a multimode one.

Equation (129) is not valid for a phase-sensitive amplification, for which the 3 dB penalty does not exist. Amplification with reduced added noise has been observed in the case of parametric amplification of optical images (Mosset, Devaux, and Lantz, 2005).

# B. Effect on entanglement

We can now determine whether or not entanglement is preserved under such a linear processing. For bipartite entanglement between modes 1 and 2, we may use the Duan-Mancini criterion (Giovannetti et al., 2003)

$$
\left\langle \left(\frac {\hat {X} _ {1} + \hat {X} _ {2}}{\sqrt {2}}\right) ^ {2} \right\rangle \left\langle \left(\frac {\hat {P} _ {1} - \hat {P} _ {2}}{\sqrt {2}}\right) ^ {2} \right\rangle <   1. \tag {131}
$$

For a maximally entangled EPR input state, the  $X$  quadratures are perfectly anticorrelated, and the  $P$  quadratures are perfectly correlated. This implies that the lhs quantity is zero at the input of the linear device, amplifier, or attenuator. At its output, it is equal, according to Defienne et al. (2016), to  $(P - 1)^{2}$ . This quantity is smaller than 1 whenever  $P < 1$  so that the entanglement survives for any attenuation factor, with a decreasing violation of the inequality when the losses increase. In the amplifier case, the Duan-Mancini criterion is satisfied only when  $P < 2$ : similar to squeezing, entanglement survives only for gains smaller than 2. For energy gain  $P$  greater than 2 the criterion is no longer satisfied. If one assumes that there are no  $X - P$  correlations, then the Duan criterion is necessary and sufficient for Gaussian states, and one is sure that entanglement "dies" for gains higher than 2. Squeezing and entanglement are destroyed equally by amplification and attenuation. This is additional proof that they are indeed two faces of the same physical property, which has two different "avatars" according to the choice of mode basis.

# XII. MODE SHAPE CONTROL

An important property of optical modes is their ability to be shaped at will so as to match as well as possible the spatiotemporal dependence needed in a given application, such as optimized parameter estimation (Sec. XIII), coupling with quantum memories or reconfigurable quantum information processing (Sec. XIV).

Mode shaping can be implemented in different ways:

- As a mode converter, which transforms a given single-mode input to another single-mode output, while keeping unchanged the quantum state defined in the mode.  
- As a mode extractor, which filters a mode of interest from a multimode field, while keeping its quantum properties and its correlations with the not-extracted modes. Such a device would enable us to keep this mode for further use, for example, to correct it in a feedforward scheme. This is easy to do of course when the modes are spatially, spectrally, or temporally separated, with a mutual "distance" large enough to be separable by the current technology, but not when the modes are overlapping.  
- As a mode multiplexer or demultiplexer that converts in a parallel way a set of input modes into an orthonormal

basis of modes that are easy to propagate in a given system and makes the reverse process at its output, while keeping the intrinsic properties of the state, and, in particular, the principal modes and their squeezing performances. As an example in classical optics, in wavelength division multiplexing the different input frequency channels are merged in a single-mode fiber (multiplexing) and are physically separated at its output (demultiplexing) using dispersive devices. An even more advanced concept is a programmable network in which this whole process can be modified at will according to the chosen application.

This domain of optics is active, especially with the recent availability of SLMs, at both the classical and quantum levels. We of course focus on its quantum aspects and concern ourselves with the evolution of the modes, but also with the induced evolution of the quantum state of the system when the modes in which is it defined are converted or distorted by some optical process.

For quantum applications, as losses destroy squeezing and entanglement, the mode shaping must be lossless and conserve energy. If the mode conversion preserves energy and is linear, it conserves the number of photons: an input  $n$ -photon Fock state  $|n:f_{\mathrm{in}}\rangle$  must then be transformed into the same Fock state in the output mode  $|n:g_{\mathrm{out}}\rangle$  for any  $n$ . The conservation of the quantum state in the mode shaping process is therefore true for any input state, because Fock states form a basis of the Hilbert space of quantum states.

In the following we separately describe mode shaping effected by linear optics and nonlinear optics.

# A. Linear conversion

We first consider spatial modes: it has been mathematically proven in the general case (Morizur et al., 2010) that one can convert any input spatial mode to any output spatial mode by using reflections (or transmissions) on two appropriately chosen phase plates separated by free space. One needs a larger, but finite, amount of reflexions on successive phase plates to convert a whole spatial mode basis into another arbitrary mode basis. This can be implemented with low conversion losses (Labroille et al., 2014) in a device called a multiplane light converter (MPLC) with the help of SLMs or phase plates, with the quantum state conserved in the conversion (Morizur et al., 2011). There are of course other linear optical spatial mode converters, but they are useful only for a subset of transformations: lens and free propagation for spatial Fourier transform, telescope for beam magnification, and Babinet-Soleil-Bravais birefringent filter for temporal derivative (Labroille et al., 2013). Fractional Fourier transform allows one to design Laguerre-Gauss mode sorters (Zhou et al., 2017), which combined with an astigmatic mode converter from Hermite-Gauss to Laguerre-Gauss modes consisting of cylindrical lenses (Beijersbergen et al., 1993) can also sort Hermite-Gauss modes (Zhou et al., 2018). Tapered fibers down to nanometer scale (Tong et al., 2003) or photonic lanterns (Fontaine et al., 2012) are also used to manipulate the modes of the fibers. A SLM can also be used to "preform" the mode before it interacts with a random scattering medium to

obtain at its output a well focused beam that has kept its quantum properties (Defienne et al., 2016).

If one now considers time-frequency modes, passive unitary conversion is not possible from a given input frequency mode to a frequency shifted output mode because changing the frequency of light amounts to changing the photon energy. This cannot be done with a passive transformation, whereas in the spatial case changing the direction of propagation of a photon does not change its energy. Therefore, passive unitary frequency mode conversion can involve phase changes only at different frequencies, which are implemented using SLMs inserted between a pair of diffraction gratings and lenses (Weiner, 2011). Such linear devices are also used in a nonunitary way by implementing frequency-dependent losses to shape the light spectrum. These last devices destroy the quantum properties of the quantum state in the CV regime, as shown in Sec. XI, and the probability of single-photon counts in the discrete variable regime. In addition, they will never be able to induce a broadening of the spectrum. This type of lossy filtering technique allows for multiplexing and demultiplexing techniques, for example, for single photons in the multiple spatial modes of a silicon photonic crystal fiber (Carpenter et al., 2013) or temporal modes (Pérez et al., 2015). Long dispersive fibers provide an efficient way to make a wavelength to time mapping of a multimode input light pulse (Chandrasekharan et al., 2017).

Mode extractors are also important tools for handling modes in view of applications: it is possible to filter a given Hermite-Gauss mode by using a Fabry-Perot cavity that transmits one mode and reflects all of the other ones. One also extracts Laguerre-Gauss modes using especially designed phase holograms (Ren et al., 2017). The MPLC device also allows one to multiplex or demultiplex a number of orthogonal spatial modes of the order of 10.

# B. Nonlinear conversion

To include frequency changes in the mode transformation one must rely on nonlinear effects, either in the microwave domain or in the optical domain. We consider as an example sum-frequency generation (SFG) (Andreas, Brecht, and Silberhorn, 2011), which uses a  $\chi^{(2)}$  type II nonlinear medium [Eq. (93)]. It is pumped here by a low frequency gate beam of spectral amplitude  $\alpha_{g}(\omega)$ , treated classically. The corresponding Hamiltonian is

$$
\hat {H} ^ {\prime} = \sum_ {\ell_ {1}, \ell_ {2}} \left(G _ {\ell_ {1}, \ell_ {2}} ^ {\prime} \hat {a} _ {\ell_ {1}} \hat {a} _ {\ell_ {2}} ^ {\prime \dagger} + \mathrm {H . c .}\right), \tag {132}
$$

where  $\hat{a}_{\ell_1}$  is the annihilation operator of input photons in the single frequency mode  $f_{\ell_1}$  of frequency  $\omega_{\ell_1}$  and  $\hat{a}_{\ell_2}'$  is the annihilation operator of SHG photons in the single frequency mode  $f_{\ell_2}'$  of frequency  $\omega_{\ell_2}$ .  $G_{\ell_1,\ell_2}' = a_{\ell_1,\ell_2}'\alpha_g(\omega_{\ell_2} - \omega_{\ell_1})$  is a product of a mode coupling factor  $a_{\ell_1,\ell_2}'$  by the pump amplitude at frequency  $\omega_{\ell_2} - \omega_{\ell_1}$ . This Hamiltonian is a double sum of terms describing transfer processes from mode  $f_{\ell_1}$  to mode  $f_{\ell_2}'$  operating in different spectral ranges. A singular value decomposition of matrix  $G'$  leads to the

following expression of the Hamiltonian, which is analogous to the one describing a beam splitter:

$$
\hat {H} ^ {\prime} = \sum_ {i} \left(\mu_ {i} \hat {b} _ {i} \hat {b} _ {i} ^ {\prime \dagger} + \mathrm {H . c .}\right). \tag {133}
$$

$\hat{b}_i$  and  $\hat{b}_i^\prime$  are, respectively, annihilation operators of photons in Schmidt input mode  $\pmb{g}_i$  and "twin" Schmidt mode  $\pmb{g}_i^\prime$ . The spectral shape of these Schmidt modes depends on the matrix  $G_{\ell_1,\ell_2}^{\prime}$  and therefore on the pump, or gate, spectral shape  $\alpha_g(\omega)$  and on the phase matching properties of the nonlinear crystal. If the gate has a Gaussian shape  $\mathrm{HG}_0$ , the Schmidt modes  $\pmb{g}_i$  and  $\pmb{g}_i^\prime$  are both Hermite-Gauss spectral-temporal modes of the same index  $\mathrm{HG}_i$  (Andreas, Brecht, and Silberhorn, 2011; Ansari et al., 2018). If the group velocities of the input and gate modes are matched, the singular value decomposition leads to a single non-negligible coefficient in the Schmidt sum. More precisely, if the pump is in the mode  $\mathrm{HG}_j$ , then the single input Schmidt mode is also  $\mathrm{HG}_j$ , whereas the SFG Schmidt mode is the Gaussian mode  $\mathrm{HG}_0$  regardless of the pump.

In the last configuration, if the gate is weak and when there is only one term, of index 1, in the sum (133), the evolution operator is written as

$$
\hat {U} = \hat {1} - i \mu_ {1} ^ {\prime} \left(\hat {b} _ {1} \hat {b} _ {1} ^ {\prime \dagger} + \hat {b} _ {1} ^ {\dagger} \hat {b} _ {1} ^ {\prime}\right), \tag {134}
$$

where  $\mu_1' = \mu_1 L / \hbar c$ , with  $L$  the crystal length. If the input state is, for example, a single-photon state  $\pmb{g}_1$ ,  $|1: \pmb{g}_1\rangle$ , the output state  $|\Psi_{\mathrm{out}}\rangle$  is

$$
\left| \Psi_ {\text {o u t}} \right\rangle = \left| 0: \mathbf {g} _ {1} ^ {\prime}, 1: \mathbf {g} _ {1} \right\rangle - i \mu_ {1} ^ {\prime} \left| 1: \mathbf {g} _ {1} ^ {\prime}, 0: \mathbf {g} _ {1} \right\rangle , \tag {135}
$$

where the single photon has been transferred from the Schmidt mode  $\pmb{g}_1$  to the Schmidt twin mode mode at the double frequency  $\pmb{g}_1'$ . If one increases the gate pump beam power but keeps it in the undepleted pump approximation, the input-output relations for the annihilation operators of the input and SHG Schmidt modes are

$$
\hat {b} _ {1} ^ {\text {o u t}} = i \sin \mu_ {1} ^ {\prime} \hat {b} _ {1} ^ {\text {i n}} + \cos \mu_ {1} ^ {\prime} \hat {b} _ {1} ^ {\text {i n}},
$$

$$
\hat {b} _ {1} ^ {\prime \text {o u t}} = \cos \mu_ {1} ^ {\prime} \hat {b} _ {1} ^ {\prime \text {i n}} + i \sin \mu_ {1} ^ {\prime} \hat {b} _ {1} ^ {\text {i n}}. \tag {136}
$$

When  $\mu_i'$  is equal to  $\pi/2$ ,  $\hat{b}_1^{\prime\mathrm{out}} = i\hat{b}_1^{\mathrm{in}}$ . We have here a perfect mode extractor: only one input mode  $g_1$  is perfectly transferred to SHG mode  $g_1'$ , whereas all the other modes are left unchanged by the nonlinear process. One easily changes the mode that is extracted by changing the shape of the pump gate beam. One can therefore extract selectively from a multimode input beam a given Hermite-Gauss mode  $\mathrm{HG}_j$  by using a gate beam precisely in the mode  $\mathrm{HG}_j$ . This device is often called a quantum pulse gate. Note that the model presented here is a simplified one, and that getting an efficiency close to  $100\%$  is not straightforward (Reddy and Raymer, 2018). To get perfect efficiency, one can extract a mode without changing the quantum state that "dwellled" in the input mode and its correlations with the other modes.

Sum-frequency generation through three- and four-wave mixing is an ideal tool for changing the mode of a given quantum state (McKinstrie et al., 2012). It has been implemented mainly for single-photon states and weak coherent states, for example, to shift them from a wavelength range to another with good conversion efficiency (Tanzilli et al., 2005), to select a given mode (spatial or temporal) with efficiencies of the order of  $70\%$  (Benjamin et al., 2014; Reddy and Raymer, 2018) and good fidelity for the output state (McGuinness et al., 2010), or to manipulate specific temporal modes (Reddy, Raymer, and McKinstrie, 2014; Pérez et al., 2015; Ra et al., 2017). Other nonlinear processes, such as frequency down-conversion, can be used to transfer single-photon states (Curtz et al., 2010; Lenhard et al., 2017) in an entanglement preserving way. Cavity QED effects can also be used to shape at will temporal modes of single photons (Morin et al., 2019).

Temporal focusing and imaging of a nonclassical state is an interesting issue (Kolner and Nazarathy, 1989). It can be implemented in a noiseless way using sum-frequency generation (Patera, Horoshko, and Kolobov, 2018) so that squeezing can be preserved by the operation, with a change of the Fourier spectrum of the quantum fluctuations. One can also use electro-optic modulation as a unitary time lens able to compress the spectral width and enhance the peak intensity of single-photon states (Karpinski et al., 2017).

# XIII. MODE OPTIMIZATION IN PARAMETER ESTIMATION

Light is often used as a tool to perform accurate or sensitive measurements of some parameter, such as distance, velocity, time delay, or frequency. We name this parameter  $a$  in a generic way. It is important to know what is the "best light," which will enable us to make the best estimation of  $a$ . We have of course the choice of the quantum state of the light, but also of the spatial and temporal shape of the mode(s) in which this state is defined. To date most attention has been given to the quantum state issue, and there is an extensive literature on its choice (Wiseman and Milburn, 2009; Giovannetti, Lloyd, and Maccone, 2011), which constitutes an important part of the domain of quantum metrology, but much less attention has been given to the mode issue.

To estimate a parameter  $a$  by optical means, one first needs an optical system that generates an  $a$ -dependent beam of light. This light is measured in one way or another, yielding data that are then processed to derive an estimator  $\tilde{a}$  of  $a$ , from which a value of  $a$  is inferred. Generally speaking, the light used in the measurement may be multimodal, the detection may be multiplexed, and the data processing may involve the analog or numerical processing of the measured quantities. We restrict ourselves to nonbiased estimators, in which case the quality of the measurement is evaluated by its "sensitivity," i.e., by the standard deviation  $\Delta a$  of the estimated values of  $a$  around the "true" value of the parameter (which we take for simplicity to be 0), which gives an upper limit to the smallest measurable variation of  $a$ .

We concentrate here on single parameter estimation using pure states, less "noisy" than mixed states, and call  $|\Psi(a)\rangle$  the possibly multimode quantum state of the light that is

submitted to measurement. The quantum Cramér-Rao limit (Helstrom, 1967, 1968, 1969; Braunstein and Caves, 1994) allows us to find the smallest value of the standard deviation  $\Delta a$  of the estimated values optimized over all possible processing procedures of the experimentally recorded data and over all possible optical measurements performed on the  $a$ -dependent beam. But there is to date no known optimization procedure over all possible quantum states of light, and many different researchers have proposed possible nonclassical quantum states giving a quantum advantage in parameter estimation. Note that the mode optimization issue in parameter estimation is related to the problem of state discrimination (Pirandola and Lloyd, 2008).

We restrict ourselves here to the subset of multimode Gaussian states (Pinel, Fade et al., 2012; Pinel, Jian et al., 2012; Pinel et al., 2013; Šafránek, Lee, and Fuentes, 2015; Nichols et al., 2018; Šafránek et al., 2019); see Sec. VII. Such a choice excludes highly nonclassical states like Fock, or entangled number states like the NOON states, but it includes squeezed and EPR entangled states. It has the advantage of comprising the bright coherent states that can be readily experimentally produced with mean photon numbers  $N$  as high as  $10^{15}$ , which is far from the case for Fock or NOON states. Two modes  $u_{\mathrm{mean}}$  and  $u_{\mathrm{det}}$  play an important role in this problem:

$$
u _ {\text {m e a n}} (\mathbf {r}, t, a) = \frac {1}{\mathcal {E} ^ {(1)} \sqrt {N}} \langle \Psi (a) | \hat {E} ^ {(+)} (\mathbf {r}, t) | \Psi (a) \rangle , \tag {137}
$$

$$
u _ {\det } (\mathbf {r}, t) = a _ {0} \frac {\partial}{\partial a} u _ {\text {m e a n}} (\mathbf {r}, t, a) | _ {a = 0}, \tag {138}
$$

where  $\mathcal{E}^{(1)}$  is the single-photon electric field defined in Eq. (25) and  $N$  is the mean photon number.  $a_0$  is the scaling factor necessary to normalize the mode  $u_{\mathrm{det}}$  to 1.  $u_{\mathrm{det}}$ , called the detection mode, characterizes the spatiotemporal distribution of the sensitivity of the optical system to a variation of the parameter. It can be used as the first mode of a new mode basis  $\{\pmb{u}_n\}$ .

The determination of the quantum Cramér-Rao bound  $\Delta a_{\mathrm{QCR}}$  in the case of a Gaussian state with high  $N$  value is simplified, as one can show that the mean value of the field is  $a$  dependent, while its covariance noise matrix  $\Gamma_Q$  is  $a$  independent, which leads to the following result (Pinel, Fade et al., 2012):

$$
\Delta a _ {\mathrm {Q C R}} = \frac {a _ {0}}{2 \sqrt {N}} \Delta_ {\mathrm {d e t}}, \tag {139}
$$

where  $\Delta_{\mathrm{det}}$  is the quantum noise factor given by

$$
\Delta_ {\mathrm {d e t}} = \frac {1}{\sqrt {\left(\Gamma_ {Q} ^ {- 1}\right) _ {u _ {\mathrm {d e t}}}}}, \tag {140}
$$

with  $(\Gamma_{Q}^{-1})_{u_{\mathrm{det}}}$  the first diagonal element of the inverse covariance matrix in the detection mode.

If the noise in this mode is not correlated with all other modes of the basis,  $\Delta_{\mathrm{det}}$  is simply the rms value of the quantum noise of a given quadrature of the detection mode: Eq. (139) shows that the quality of the  $a$  measurement is limited only by the quantum noise in the detection mode. It is

insensitive to the noises in the other modes orthogonal to  $u_{\mathrm{det}}$ . In the general Gaussian illumination case, one can show that the optimal use of resources consists of populating the detection mode with the best squeezing source available, and in that case this mode is not correlated with the other modes (Pinel, Fade et al., 2012).  $\Delta_{\mathrm{det}}$  is equal to 1 when the  $a$ -encoding light quantum state is a coherent state. In this case  $\Delta a_{\mathrm{QCR}} = a_0 / 2\sqrt{N}$ : this is the so-called standard quantum Cramér-Rao limit.  $\Delta_{\mathrm{det}}$  is below this value if one injects a squeezed vacuum state in the detection mode together with an intense coherent state in mode  $u_{\mathrm{mean}}$  (Fabre, Fouet, and Maitre, 2000). Equation (139) implies that injecting squeezed or EPR entangled states in modes other than  $u_{\mathrm{det}}$  would not further decrease the quantum Cramér-Rao bound: a single squeezed state is enough to reach the bound provided that it is put in the right mode, namely, the detection mode (Pinel, Fade et al., 2012). This implies that it is not possible to accumulate the beneficial effects of squeezed states in two different modes for the measurement of a single parameter. Note that  $\Delta a_{\mathrm{QCR}}$  vanishes if one uses an infinitely squeezed vacuum state in the detection mode. Such a state is not physical, as it has an infinite energy. If one imposes a constraint of total finite energy  $N\hbar \omega_0$  equal to the sum of the mean energies of the modes  $u_{\mathrm{mean}}$  and  $u_{\mathrm{det}}$ , the limit scales as  $N^{-3/4}$  (Caves, 1981; Barnett, Fabre, and Maitre, 2003), an intermediate scaling between the standard quantum noise and the  $N^{-1}$  Heisenberg scaling.

It is not enough to find the ultimate limits in parameter estimation. One needs of course to find a way to reach them. Generally speaking, a balanced homodyne detection with a local oscillator put in the detection mode allows one to attain the limit in all configurations (Delaubert et al., 2008), but there are in some cases more convenient ways, for example, determine the  $a$  estimator by computing combinations of photocurrents recorded in different parts of the illumination beam (Treps et al., 2003) or linear combinations of its spectral components using the multiplexed detection outlined in Sec. X.E.

We now apply the approach that we just exposed to the well studied issue of a phase measurement using a Mach-Zehnder interferometer at mid fringe. It involves two input modes  $f_{1}^{\mathrm{in}}$  and  $f_{2}^{\mathrm{in}}$  incident on the first beam splitter, where we consider the usual case of  $f_{2}^{\mathrm{in}}$  as a vacuum mode, and two output modes  $f_{1}^{\mathrm{out}}$  and  $f_{2}^{\mathrm{out}}$  at the output of the second beam splitter. It is straightforward to show that in this configuration  $u_{\mathrm{mean}} = (f_{1}^{\mathrm{out}} + f_{2}^{\mathrm{out}}) / \sqrt{2}$  and  $u_{\mathrm{det}} = (f_{1}^{\mathrm{out}} - f_{2}^{\mathrm{out}}) / \sqrt{2}$ . These output modes correspond, respectively, by backpropagation through the interferometer, precisely to the input modes  $f_{1}^{\mathrm{in}}$  and  $f_{2}^{\mathrm{in}}$ . This implies that the optimized configuration for an interferometric measurement using Gaussian states is to feed mode  $f_{1}^{\mathrm{in}}$  with an intense coherent state, and mode  $f_{2}^{\mathrm{in}}$  with a squeezed vacuum state, a strategy that was found years ago by Caves (1981) and is currently implemented in gravitational wave antennas (Schnabel, 2017). The approach outlined in this section therefore shows once again the optimized character of Caves's configuration and extends it to any optical measurement with multimode Gaussian states. It has been applied to the estimation of various parameters: transverse

displacement and tilt of a  $\mathrm{TEM}_{00}$  light beam (Hsu et al., 2004; Delaubert et al., 2006) (for which the detection mode is the  $\mathrm{TEM}_{01}$  mode), time delay (Lamine, Fabre, and Treps, 2008; Thiel et al., 2016), propagation distance of a light pulse immune from atmospheric perturbations (Jian et al., 2012), mean frequency shift of broadband light, and transverse width of a highly focused beam (Chille et al., 2016). Several experiments have shown that it is indeed possible to go beyond the standard Cramér-Rao bound by using squeezed light in the appropriate detection mode (TrepS et al., 2002; Taylor et al., 2013; Pooser and Lawrie, 2015).

A general problem this approach can be naturally applied to is that of the ultimate resolution in optical imaging, a problem in which diffraction effects induce the existence of the so-called Rayleigh limit. It was first tackled in the case of a coherent light image (Kolobov and Fabre, 2000), and it has been shown that in this case injecting squeezing in appropriate modes (namely, the prolate spheroidal ones) improves the optical resolution below the standard quantum noise (Kolobov, 2008), and that one could further improve the resolution by taking into account the sparsity of the image (Wang, Han, and Kolobov, 2012). It was more recently studied for incoherent illumination, more precisely to derive the ultimate resolution limit on the separation between two  $\mathrm{TEM}_{00}$  incoherent sources (Tsang, Nair, and Lu, 2016). It was shown that the Fisher information contained in the intensity distribution in the image about this separation falls to zero as the separation drops below the Rayleigh limit, and that it is possible to extract more information on the separation (Lupo and Pirandola, 2016; Tsang, Nair, and Lu, 2016), and therefore to increase the accuracy of its estimation beyond the Rayleigh limit, by other measurement strategies (Tsang, 2017). This is a direct extension of the coherent estimation of a beam displacement to the incoherent case, and, in particular, one can make a homodyne measurement with LO in the  $\mathrm{TEM}_{01}$  Hermite-Gauss mode (Yang et al., 2017), project it onto the detection mode that is the combination of two oppositely displaced  $\mathrm{TEM}_{00}$  modes (Paur et al., 2016), or demultiplex the amplitude image on the basis of spatial Hermite-Gauss modes (Tsang, 2017) by measuring the intensity of each Hermite-Gauss mode in the decomposition of the image on such a mode basis. This can be achieved, in particular, using the MPLC device described in Sec. XII. This scheme has been extended to the estimation of the axial separation between two point sources (Zhou et al., 2019) and to the time domain using higher-order Hermite-Gauss temporal modes to distinguish the arrival times of two incoherent ultrashort light pulses (Donohue et al., 2018). Furthermore, once multimode demultiplexing is available, one can use this information to perform a multiparameter estimation, as was recently proposed by Yu and Prasad (2018) and Napoli et al. (2019).

# XIV. MODES AND STATES IN QUANTUM INFORMATION PROCESSING

# A. Measurement-based quantum computing

Multimode light is naturally at the heart of optical approaches to quantum computing, and while the objective

of this review is not to address quantum information processing with light in general, the purpose of this section is to show the interest of using the tools introduced and used in this review for quantum information processing techniques. In this context, even though the circuit-based approach is still the most studied one and qubits can be successfully implemented on frequency bins (Lu et al., 2018), extending wavelength division multiplexing to the quantum domain, we concentrate in this section on a recent paradigm for quantum computing, introduced by Raussendorf and Briegel (2001) as a one-way quantum computer and more commonly called measurement-based quantum computing (MBQC). The idea is to replace the circuit-based approach, where quantum gates are successively applied to the input qubits to perform a given operation, with a scheme where a large specific entangled state is generated and then successive measurements are performed on individual nodes of this state. More specifically, the input state should belong to a given class of graph states, the cluster states, and the result of each measurement is used to correct in a feedforward configuration the resulting state and to choose which observable will be measured in the next step. While first introduced in the qubit approach, MBQC was also extended to the continuous variable domain (Menicucci et al., 2006; Gu et al., 2009) with the advantage that cluster states in that regime can be deterministically generated.

# B. Cluster states: Concepts and experimental implementation

We focus here on the continuous variable approach, where the possibility of generating entanglement between modes through mode basis change allows for efficient and versatile generation of cluster states in which the nodes are precisely the different modes in multimode quantum light. These cluster states can be defined in an operational approach by applying on  $N$  infinitely squeezed states a set of controlled-  $Z\left(C_{z}\right)$  gates defined by  $C_z = e^{i\hat{X}_1\hat{X}_2}$ . This graph state structure is embedded in an adjacency matrix  $V$ , an  $N\times N$  real symmetric matrix such that the multimode  $C_Z$  gate is written as

$$
C _ {z} [ V ] = \prod_ {1 \leq j \leq k \leq N} \exp (i V _ {j k} \hat {X} _ {j} \otimes \hat {X} _ {k}). \tag {141}
$$

In essence, the nonzero elements of  $V$  induce a connection between two nodes of the graph. Usually  $V$  would be a matrix whose elements are either 0 or 1, but one can also have weighted graphs where nonzero elements can differ from 1.

To study a cluster state that can potentially be implemented experimentally, one first has to consider that the input states are finite squeezed states, with the ideal cluster state obtained in the limit of squeezing going to infinity. Then, because the evolution equation (141) corresponds to a quadratic Hamiltonian evolution applied to squeezed states, cluster states remain Gaussian states and can be constructed through symplectic transformations applied to the vacuum. As introduced in Eq. (47), we call  $\hat{\tilde{Q}}_{\mathrm{sqz}}$  the  $2N$  element column vector made of the quadrature operators for the initial squeezed states. One can show that the cluster state quadrature operators are given by (Menicucci et al., 2006)

$$
\begin{array}{l} \vec {\hat {Q}} _ {\mathrm {c l u}} = (C _ {z} [ V ]) ^ {\dagger} \vec {\hat {Q}} _ {\mathrm {s q z}} C _ {z} [ V ] = \left( \begin{array}{c c} \mathbb {1} _ {N} & 0 \\ V & \mathbb {1} _ {N} \end{array} \right) \vec {\hat {Q}} _ {\mathrm {s q z}} \\ = \left( \begin{array}{c c} \mathbb {1} _ {N} & 0 \\ V & \mathbb {1} _ {N} \end{array} \right) K \vec {Q} _ {\text {v a c}}, \tag {142} \\ \end{array}
$$

where  $K = \mathrm{diag}(\sigma_1,\sigma_2,\dots,\sigma_N,\sigma_1^{-1},\sigma_2^{-1},\dots,\sigma_N^{-1})$  is the multimode squeezing matrix, with  $\sigma_{i} > 1$  (we consider input states squeezed on the  $P$  quadrature). One finds that

$$
\lim  _ {\sigma_ {1}, \sigma_ {2}, \dots , \sigma_ {N} \rightarrow \infty} \left\langle \vec {\hat {P}} _ {\mathrm {c l u}} - V \vec {\hat {X}} _ {\mathrm {c l u}} \right\rangle = 0. \tag {143}
$$

The  $N$ -dimensional operator  $\vec{\hat{P}}_{\mathrm{clus}} - V\vec{\hat{X}}_{\mathrm{clus}}$  defines the  $N$  nullifiers associated with the graph and hence governs its structure. It connects the  $P$  quadrature of a node with the  $X$  quadratures of the nodes connected to it. The nullifiers are experimentally measurable quantities. They are often used to assess the quality of a generated cluster state. To show that the experimentally generated state is indeed a cluster state, one needs to demonstrate that the nullifier variances are below the vacuum limit, but also that the graph shows multipartite entanglement as defined in Sec. VIII.

The  $C_z$  gate is hard to implement experimentally, as its symplectic representation is not a simple basis change, but contains squeezing evolution. To bypass this difficulty, one can consider the total evolution from the vacuum state, which is symplectic, and calculate the corresponding Bloch-Messiah decomposition; see Sec. VII.C.1. Being a Gaussian state, any approximated cluster state can be implemented with a multimode squeezeer and a basis change  $O_V$  acting on the vacuum. It was shown (van Loock, Weedbrook, and Gu, 2007) that the unitary matrix  $U$  associated with the basis change  $O_V$  as defined in Eq. (86) is given by the condition  $\mathrm{Re}(U) - V\mathrm{Im}(U) = 0$ . Several experimental groups hence adopted the strategy to generate a set of independent squeezed states and implement the basis change  $O_V$  corresponding to the desired cluster states (Ukai et al., 2011; Su et al., 2012), leading to cluster states with millions of modes (Yokoyama et al., 2013). Note that the  $O_V$  matrix is not unique, and in the case where the input squeezed states do not have the same squeezing level, the obtained nullifier variances depend on the actual  $O_V$  that is used. Hence, optimizing this matrix is important to reach the best cluster state for a given set of resources (Ferrini et al., 2013, 2016).

Being Gaussian and thus the result of a quadratic Hamiltonian, cluster states can also be directly generated by tailoring a nonlinear quadratic interaction instead of being produced from independent parallel squeezers and basis change. For instance, one can use the resonant frequency modes of an OPO as the nodes of the cluster and tailor the entanglement by engineering the pump of the cavity. One can use several single frequency pumps (Menicucci, Flammia, and Pfister, 2008; Shahrokhshahi and Pfister, 2011; Chen, Menicucci, and Pfister, 2014) or a pulse-shaped pump (Arzani, Fabre, and Treps, 2018). It is also possible to cascade  $\chi^{(3)}$  interaction in atomic vapors (Liu et al., 2011; Pooser and Jing, 2014; Qin et al., 2014).

# C. Non-Gaussian cluster states

Cluster states are Gaussian and as such allow only for Gaussian quantum information processing (Weedbrook et al., 2012), which cannot lead to a quantum advantage (Bartlett et al., 2002), a property which can be extended to any positive Wigner function state (Mari and Eisert, 2012). Thus, an ingredient acting on the positivity of the Wigner function is required, which can take the form of a qubic gate (Gu et al., 2009) or a non-Gaussian encoding such as the so-called Gottesman-Kitaev-Preskill (GKP) encoding (Gottesman, Kitaev, and Preskill, 2001), which has been proven to allow for error corrected quantum computing protocols (Menicucci, 2014) with a requirement on squeezing now as low as  $10\mathrm{dB}$  (Fukui et al., 2018). Several proposals for GKP state preparation have also been published (Weigand and Terhal, 2018; Eaton, Nehra, and Pfister, 2019a, 2019b).

In a spirit related to the scope of this review, another possibility is to generate non-Gaussian cluster states that can then be used for universal quantum computing (Sasaki and Suzuki, 2006; Quesada, Arrazola, and Killoran, 2018; Gagatsos and Guha, 2019; Phillips et al., 2019). The most commonly used technique in quantum optics consists of adding or subtracting one or several photons to or from a Gaussian state (Wenger, Tualle-Brouri, and Grangier, 2004; Ourjoumtsev et al., 2007; Parigi et al., 2007; Takahashi et al., 2008). However, the challenge is to render this operation mode selective in a multimode context, a process that we study in the following.

We now consider the Wigner function  $W_{\Gamma}(\vec{q})$  of a Gaussian state with covariance matrix  $\Gamma$ , as defined in Eq. (81). This state can be a multimode entangled state, for instance, that one wishes to degaussify, were it to be for quantum information or quantum metrology purposes. We consider the coherent addition or subtraction of a single photon in a given mode  $\pmb{g}$ , which amounts to the normalized application of the associated creation operator  $\hat{b}_g^\dagger$  or annihilation operator  $\hat{b}_g$ . This mode  $\pmb{g}$  can be any mode of the modal Hilbert space and does not have to be one of the mode bases in which the Gaussian state is described. It can, for instance, be a nonentangled mode but also a mode highly entangled with the rest of the system, such as the node of a cluster state. It can be shown that the Wigner function becomes (Walschaers et al., 2017a)

$$
W ^ {\pm} (\vec {q}) = \frac {1}{2} [ \vec {q} ^ {T *} \Gamma^ {- 1} \mathbf {A} _ {g} ^ {\pm} \Gamma^ {- 1} \vec {q} - \operatorname {T r} (\Gamma^ {- 1} \mathbf {A} _ {g} ^ {\pm}) + 2 ] W _ {\Gamma} (\vec {q}), \tag {144}
$$

where the operator  $\mathbf{A}_g^{\pm}$  is the one amounting to the extra correlations induced by the single-photon subtraction or addition operation that is defined as

$$
\mathbf {A} _ {g} ^ {\pm} = 2 \frac {(\boldsymbol {\Gamma} \pm \mathbb {1}) \mathbf {P} _ {g} (\boldsymbol {\Gamma} \pm \mathbb {1})}{\operatorname {T r} [ (\boldsymbol {\Gamma} \pm \mathbb {1}) \mathbf {P} _ {g} ]}, \tag {145}
$$

where  $\mathbf{P}_g$  is the projector on the subspace associated with mode  $\pmb{g}$ . For instance, when  $\pmb{g}$  is one of the modes of the mode basis,  $\mathbf{P}_g$  reduces to a diagonal matrix with zero everywhere except for the two diagonal elements corresponding to the two quadratures associated with  $\pmb{g}$ , where it is equal to 1. Note that

Eq. (144) is valid for both pure and mixed states, and it can be easily applied to calculate the Wigner function of a subparty of a global state after photon addition or subtraction (Walschaers et al., 2017b). In particular, it can be used to study the negativity of the Wigner function, which is particularly simple in the case of nondisplaced states for which it can be probed in  $\vec{q} = 0$  and amounts to determining the sign of the quantity  $2 - \mathrm{Tr}(\Gamma^{-1}\mathbf{A}_q^{\pm})$ .

As is well known, starting from a pure squeezed state photon subtraction induces negativity, while whatever the input state photon addition induces negativity. The same property does extend to graph states. However, the amount of negativity that is obtained depends more on the purity of the input state than on the quantity of squeezing available. In the multimode scenario, the complexity of this interplay can be examined using the previous formula, in particular, how non-Gaussianity spreads among a graph state, such as a cluster state. It can be shown, for instance, that if one removes a photon from a node of a cluster states, the non-Gaussianity spreads up to two nodes away from the node on which the photon is subtracted (Walschaers et al., 2018). This gives a method to induce fully non-Gaussian cluster states for quantum information purposes. Finally, this formula can also be used to study how entanglement is induced by single-photon operations. Starting from a pure state, one can simply evaluate the purity of the reduced state in a subspace after the single-photon operation. One can use this property to demonstrate that, for instance, the intrinsic separability of Gaussian states as defined in Sec. VII.C.5 does not extend to photon-added or photon-subtracted Gaussian states. The structure of the state after single-photon operation can be fundamentally different from the original Gaussian one, in the sense that for a well chosen mode of single-photon operation the state becomes entangled regardless of the mode basis.

In most experiments heralded single-mode photon subtraction has been implemented using a weakly reflecting beam splitter followed by a photon counter. When it detects a photon, one is sure that one photon has been removed from the transmitted beam. This process cannot be used for mode-selective photon subtraction because the beam splitter and the photon detector do not discriminate between photons of different modes. As a result of this uncertainty the transmitted beam is in a mixed state. To get mode selectivity and significant negativity, Ra et al. (2020) used the process of SFG, which was discussed in Sec. XII in the context of mode conversion. They operated in the weak gate beam case, for which the evolution operator given by Eq. (132) is the same as the one for a weakly reflecting beam splitter, but only for a single Hermite-Gauss input mode, the one that is identical to the Hermite-Gauss mode  $\mathrm{HG}_i$  of the gate beam. None of the other Hermite-Gauss modes are affected by the nonlinear process (Ra et al., 2017). As a result, when one photon is recorded on the  $g_1'$  upconverted mode, one is sure that it has been removed from the  $\mathrm{HG}_i$  mode of the multimode input beam. The process is flexible and can subtract a photon from linear superpositions of modes, from two-mode entangled states, and from cluster states. When the device is fed at its input by the multimode quantum frequency comb described in Sec. IX.B.4, significant levels of negativity are measured in

the different configurations. The spreading of non-Gaussianity just mentioned has also been observed.

Single-mode photon addition can be implemented by parametric amplification in a  $\chi^{(2)}$  nonlinear crystal: upon detecting a photon on the idler mode, one is sure that one photon as been added to the input quantum state of the signal mode (Zavatta, Viciani, and Bellini, 2004). The process has been extended to the photon addition to two temporal modes leading to micro-macro entanglement (Biagi et al., 2018), with the possibility of scalability to a larger number of modes.

# XV. CONCLUSION

We hope to have convinced the reader that considering in a comprehensive way the quantum states and the modes in which they are defined provides interesting insight into many quantum optics issues and efficient ways to generate highly entangled quantum states. Increasing by a large factor the number of modes in an optical system does not pose intractable problems. Modes can be easily manipulated and computer controlled using spatial light modulators so that multimode quantum states with well mastered mode shapes and correlations are promising scalable and reconfigurable carriers or processors of quantum information. Another advantage over the discrete variable approach is that highly entangled multimode states of light such as cluster states are generated in a deterministic, unconditional way regardless of the size of the cluster state. But an important problem remains to be solved concerning the unconditional preparation of multimode non-Gaussian states.

# ACKNOWLEDGMENTS

First, we acknowledge the important contributions of all of the Ph.D. students and postdoctoral researchers that worked successively in the quantum optics group at LKB, and M. Walschaers for the valuable feedback on the manuscript. We thank for the useful discussions our colleagues at the Laboratoire Kastler Brossel A. Bramati, E. Giacobino, S. Gigan, J. Laurat, and C. Salomon, among many others. Discussions with European colleagues in the different groups of European funded projects like QSTRUCT, QUANTIM, and QCUMBER have played a decisive role in the emergence of the concepts described in this review, in particular, S. Barnett, G. de Valcarcel, A. Gatti, Y. Golubev, M. Kolobov, G. Leuchs, L. Lugiato, and G. L. Oppo. We also acknowledge the fruitful discussions during conferences, visits, and cooperative programs with U. Andersen, H. Bachor, A. Furusawa, D. Horoshko, J. Howell, Ping Koy Lam, U. Leonhardt, P. Lett, M. Martinelli, P. Nussenzweig, Z. Y. Ou, O. Pfister, E. Polzik, M. Raymer, A. Sergienko, C. Silberhorn, W. Vogel, I. Walmsley, and many others.

# APPENDIX A: COUNTING SPATIAL MODES IN LASER BEAMS

The number of spatial modes oscillating in a laser is an important parameter to characterize imperfect, non-singlemode laser beams (Karny, Lavi, and Kafir, 1983). The number  $M$ , coming from the "  $M^2$  factor" introduced by Siegman

(Siegman, 1998), is often considered as giving a direct measure of the number of transverse modes. We want to know whether this approach is compatible with the quantum one introduced in this review.

Call  $k$  the wave vector in direction  $x$ . The  $M^2$  factor is defined as

$$
M ^ {2} = \frac {\Delta x \Delta k}{(\Delta x \Delta k) _ {\min }} = 2 \Delta x \Delta k, \tag {A1}
$$

with  $1/2$  the minimum value of the product  $\Delta x\Delta k$  allowed by the Fourier-Heisenberg inequality.

We now take as an example the case of a laser generating an incoherent superposition of  $p$  Hermite-Gauss modes  $h_n(x)$ , with equal probabilities for each one and equal intensities to simplify the discussion. From a quantum mechanical point of view, it is described by the density matrix

$$
\rho = \sum_ {n = 1} ^ {p} \frac {1}{p} | \alpha : h _ {n} \rangle \langle \alpha : h _ {n} |, \tag {A2}
$$

where  $|\alpha \rangle$  is a Glauber coherent state. The same reasoning as in Sec. IV, based on the coherency matrix, tells us that  $\rho$  describes a quantum state having an intrinsic number of modes equal to  $p$ . We want now to know the relation between  $p$  and  $M$ : as the coherency matrix is diagonal in the Hermite-Gauss mode basis, and using the properties of Hermite-Gauss modes, one has

$$
\Delta^ {2} x = \frac {\langle \int d x x ^ {2} \hat {N} \rangle}{\langle \hat {N} \rangle} = \frac {\sum_ {n = 0} ^ {p - 1} \left(| \alpha | ^ {2} / p\right) (2 n + 1) w ^ {2}}{\sum_ {n = 0} ^ {p - 1} | \alpha | ^ {2} / p} \tag {A3}
$$

and

$$
\Delta^ {2} k = \frac {\left\langle \int d x k ^ {2} \hat {N} \right\rangle}{\langle \hat {N} \rangle} = \frac {\sum_ {n = 0} ^ {p - 1} \left(| \alpha | ^ {2} / p\right) (2 n + 1)}{4 w ^ {2} \sum_ {n = 0} ^ {p - 1} | \alpha | ^ {2} / p}. \tag {A4}
$$

Knowing that  $\sum_{n=0}^{p-1}(2n+1) = p^2$ , one finally finds

$$
\Delta^ {2} x = p ^ {2} w ^ {2}, \quad \Delta^ {2} k = \frac {p ^ {2}}{4 w ^ {2}}, \quad \Delta k \Delta x = \frac {p ^ {2}}{2} \tag {A5}
$$

so that  $p$  is indeed equal to  $M$  in this specific case, and close to this value in the general case.

# APPENDIX B: COUNTING MODES IN PARAMETRIC DOWN-CONVERTED LIGHT

The complexity of a bipartite quantum state, in particular, its entanglement properties, is related to the Schmidt number (Guo and Fan, 2013; Dyakonov et al., 2015; Sharapova et al., 2015; Namiki, 2016), i.e., the number of terms in the Schmidt decomposition. We want to know whether the Schmidt number is indeed the mode number calculated from the coherency matrix. We consider only a simple example, namely, a bipartite system in which the two parties A and B are multimode, for example, the two-photon quantum state produced by parametric down-conversion, written in the 1D case as

$$
| \Psi \rangle = \int d k _ {A} d k _ {B} g \left(k _ {A}, k _ {B}\right) | 1: k _ {A} \rangle \otimes | 1: k _ {B} \rangle , \quad (\mathrm {B} 1)
$$

with  $g(k_A, k_B)$  containing the phase matching and pump spatial properties, and  $|1:k_A\rangle$  a single-photon state of party A and wave vector  $k_A$ . Thanks to the Mercer theorem,  $|\Psi\rangle$  can be written as a Schmidt sum

$$
| \Psi \rangle = \sum_ {i = 1} ^ {S} \lambda_ {i} | 1: u _ {A} ^ {i} \rangle \otimes | 1: u _ {B} ^ {i} \rangle \tag {B2}
$$

with  $u_{A}^{i}$  and  $u_{B}^{i}$  orthonormal eigenmodes in parties A and B,  $\lambda_{i}$  the corresponding positive eigenvalue, and  $S$  the so-called Schmidt number.

We call  $\hat{b}_A^i$  and  $\hat{b}_B^{i'}$  the annihilation operators in modes  $u_{A}^{i}$  and  $u_{B}^{i}$ . We now use the property that the mode number is the dimension of the space spanned by the vectors  $\hat{b}_A^i |\Psi \rangle$  and  $\hat{b}_B^{i'}|\Psi \rangle$ . One has

$$
\hat {b} _ {A} ^ {i} | \Psi \rangle = \lambda_ {i} | 1: u _ {B} ^ {i} \rangle , \quad \hat {b} _ {B} ^ {i ^ {\prime}} | \Psi \rangle = \lambda_ {i ^ {\prime}} | 1: u _ {A} ^ {i ^ {\prime}} \rangle . \tag {B3}
$$

All of these vectors are orthogonal, meaning that the dimension of the generated space is  $2S$ . We have therefore shown that the number of modes is twice the Schmidt number.

# APPENDIX C: MODAL DEPENDENCE OF THE COINCIDENCE RATE IN THE HONG-OU-MANDEL EXPERIMENT

We start with Eq. (115) and chose two bases of modes, labeled  $\{f_{m_A}^A\}$  for beam A and  $\{f_{m_B}^B\}$  for beam B, in such a way that the modes of the same index  $(m_A = m_B)$  are "mirror images" of each other with respect to the beam splitter. In this case, one can express simply the corresponding annihilation operators in the function of the operators  $\hat{b}^{A\mathrm{in}}$  and  $\hat{b}^{B\mathrm{in}}$  acting on the state before the beam splitter, which is the factorized state  $|1:g_A,1:g_B\rangle$ :

$$
\hat {b} _ {m} ^ {A} = \frac {1}{\sqrt {2}} \left(\hat {b} _ {m} ^ {\text {A i n}} + e ^ {i \phi} \hat {b} _ {m} ^ {\text {B i n}}\right), \quad \hat {b} _ {m} ^ {B} = \frac {1}{\sqrt {2}} \left(\hat {b} _ {m} ^ {\text {A i n}} - \hat {b} _ {m} ^ {\text {B i n}}\right), \tag {C1}
$$

with the phase term  $e^{i\phi}$  accounting for some delay, or some path difference, between the two arms of the interferometer. Using Eq. (42) and the completeness relation for the mode basis, one gets the following expression for the normalized coincidence rate:

$$
g ^ {(2)} = \frac {1}{2} (1 - | \vec {g} _ {A} \cdot \vec {g} _ {B} | ^ {2} \cos 2 \phi). \tag {C2}
$$

There are therefore no coincidences at zero path difference  $\phi = 0$  when the modes of the two input photons are identical, spatially as well as temporally.

In the second configuration of the HOM interference, the input state generated by parametric down-conversion can be written, as in Appendix B, as the Schmidt sum (B2):

$$
\left| \Psi_ {2} \right\rangle = | 0 \rangle + \sum_ {i = 1} ^ {S} \sqrt {p _ {i}} \left| 1: g _ {A} ^ {i} \right\rangle \otimes \left| 1: g _ {B} ^ {i} \right\rangle , \tag {C3}
$$

with  $\sum_{i}p_{i} = 1$ . Using as previously mode bases that are mirror images of each other, one finds for the normalized coincidence rate at zero delay

$$
g ^ {(2)} (0) = \frac {1}{2} \left[ 1 - \sum_ {i, j} \sqrt {p _ {i} p _ {j}} \left(\vec {g} _ {A} ^ {i} \cdot \vec {g} _ {B} ^ {j}\right) \left(\vec {g} _ {A} ^ {j} \cdot \vec {g} _ {B} ^ {i}\right) ^ {*} \right]. \tag {C4}
$$

The coincidence rate vanishes when  $\vec{g}_A^i = \vec{g}_B^i \forall i$ , i.e., when there is a perfect two-by-two matching for all the Schmidt modes of the two beams. This is achieved when there is total symmetry with respect to the exchange between the signal and idler A and B parts, i.e., when the matrix  $G_{si}$  introduced in Eq. (98) is symmetric.

One can now consider the same problem but with input coherent states of equal amplitudes and phase difference  $\psi$ ,  $|\alpha\rangle$ , and  $|\alpha e^{i\psi}\rangle$ . A calculation analog to the previous one, based on Eq. (73), leads to the following result for  $g^{(2)}(\phi = 0)$ :

$$
g ^ {(2)} (0) = \frac {1}{2} \left(1 - | \bar {g} _ {A} \cdot \vec {g} _ {B} | ^ {2} \cos 2 \psi\right). \tag {C5}
$$

When the two modes are identical, the "HOM dip" is as expected zero for identical or opposite fields and  $1/2$  for incoherent fields. But one also finds a  $100\%$  dip if  $\psi$  randomly takes one of the two values 0 or  $\pi$ , as was recently stressed by Sadana et al. (2018).

# REFERENCES

Acín, A., A. Andrianov, L. Costa, E. Jané, J.I. Latorre, and R. Tarrach, 2000, "Generalized Schmidt Decomposition and Classification of Three-Quantum-Bit States," Phys. Rev. Lett. 85, 1560-1563.  
Adesso, Gerardo, and Fabrizio Illuminati, 2006, "Continuous variable tangle, monogamy inequality, and entanglement sharing in Gaussian states of continuous variable systems," New J. Phys. 8, 15.  
Adesso, Gerardo, and Fabrizio Illuminati, 2007a, "Entanglement in continuous-variable systems: Recent advances and current perspectives," J. Phys. A 40, 7821-7880.  
Adesso, Gerardo, and Fabrizio Illuminati, 2007b, "Strong Monogamy of Bipartite and Genuine Multipartite Entanglement: The Gaussian Case," Phys. Rev. Lett. 99, 150501.  
Adesso, Gerardo, and Fabrizio Illuminati, 2007c, "Bipartite and multipartite entanglement of Gaussian states," in Quantum Information with Continuous Variables of Atoms and Light, edited by N. J. Cerf, G. Leuchs, and E. S. Polzik (Imperial College Press, London), Chap. 1, pp. 1-21.  
Adesso, Gerardo, Sammy Ragy, and Antony R. Lee, 2014, "Continuous variable quantum information: Gaussian states and beyond," Open Syst. Inf. Dyn. 21, 1440001.  
Adesso, Gerardo, Alessio Serafini, and Fabrizio Illuminati, 2004, "Quantification and Scaling of Multipartite Entanglement in Continuous Variable Systems," Phys. Rev. Lett. 93, 220504.  
Afzelius, Mikael, Christoph Simon, Hugues de Riedmatten, and Nicolas Gisin, 2009, "Multimode quantum memory based on atomic frequency combs," Phys. Rev. A 79, 052329.

Aichele, T., A. I. Lvovsky, and S. Schiller, 2002, "Optical mode characterization of single photons prepared by means of conditional measurements on a biphoton state," Eur. Phys. J. D 18, 237-245.  
Albarelli, Francesco, Marco G. Genoni, Matteo G. A. Paris, and Alessandro Ferraro, 2018, "Resource theory of quantum non-Gaussianity and Wigner negativity," Phys. Rev. A 98, 052350.  
Allen, L., S. Barnett, and M. J. Padgett, 2016, Optical Angular Momentum (Taylor & Francis, London).  
Allevi, A., M. Bondani, A. Ferraro, and M.G.A. Paris, 2006, "Classical and quantum aspects of multimode parametric interactions," Laser Phys. 16, 1451-1477.  
Arvind, Biswadeb Dutta, N. Mukunda, and R. Simon, 1995, "The real symplectic groups in quantum mechanics and optics," Pramana 45, 471-497.  
Ansari, V., J.M. Donohue, B. Brecht, and C. Silberhorn, 2018, "Tailoring nonlinear processes for quantum optics with pulsed temporal-mode encodings," Optica 5, 534.  
Armstrong, S., J. F. Morizur, J. Janousek, B. Hage, Nicolas Treps, P. K. Lam, and H. A. Bachor, 2012, "Programmable multimode quantum networks," Nat. Commun. 3, 1026.  
Arzani, Francesco, Claude Fabre, and Nicolas Treps, 2018, "Versatile engineering of multimode squeezed states by optimizing the pump spectral profile in spontaneous parametric down-conversion," Phys. Rev. A 97, 033808.  
Avella, A., M. Gramegna, A. Shurupov, G. Brida, M. Chekhova, and M. Genovese, 2014, "Separable Schmidt modes of a nonseparable state," Phys. Rev. A 89, 023808.  
Averchenko, V. A., Yu. M. Golubev, C. Fabre, and N. Treps, 2011, "Quantum correlations and fluctuations in the pulsed light produced by a synchronously pumped optical parametric oscillator below its oscillation threshold," Eur. Phys. J. D 61, 207-214.  
Barakat, Richard, 1963, "Theory of the coherency matrix for light of arbitrary spectral bandwidth," J. Opt. Soc. Am. 53, 317-323.  
Barbosa, F. A. S., Antonio Sales Coelho, L. F. Muñoz-Martínez, L. Ortiz-Gutiérrez, A. S. Villar, P. Nussenzveig, and M. Martinelli, 2018, "Hexapartite Entanglement in an Above-Threshold Optical Parametric Oscillator," Phys. Rev. Lett. 121, 073601.  
Barbosa, Felipe A. S., Antonio S. Coelho, Katiuscia N. Cassemiro, Paulo Nussenzveig, Claude Fabre, Marcelo Martinelli, and Alessandro S. Villar, 2013, "Beyond Spectral Homodyne Detection: Complete Quantum Measurement of Spectral Modes of Light," Phys. Rev. Lett. 111, 200402.  
Barnett, Stephen M., Claude Fabre, and Agnes Maitre, 2003, "Ultimate quantum limits for resolution of beam displacements," Eur. Phys. J. D 22, 513-519.  
Bartlett, Stephen D., Barry C. Sanders, Samuel L. Braunstein, and Kae Nemoto, 2002, "Efficient Classical Simulation of Continuous Variable Quantum Information Processes," Phys. Rev. Lett. 88, 097904.  
Beck, M., 2000, "Quantum State Measurement with Array Detectors," Phys. Rev. Lett. 84, 5748.  
Beijersbergen, Marco W., Les Allen, H. E. L. O. Van der Veen, and J. P. Woerdman, 1993, "Astigmatic laser mode converters and transfer of orbital angular momentum," Opt. Commun. 96, 123-132.  
Benjamin, Brecht, Andreas Eckstein, Raimund Ricken, Viktor Quiring, Hubertus Suche, Linda Sansoni, and Christine Silberhorn, 2014, "Demonstration of coherent time-frequency Schmidt mode selection using dispersion-engineered frequency conversion," Phys. Rev. A 90, 030302.  
Bennink, Ryan, and Robert Boyd, 2002, "Improved measurement of multimode squeezed light via an eigenmode approach," Phys. Rev. A 66, 053815.

Beugnon, Jérôme, Matthew P. A. Jones, Jos Dingjan, Benoit Darquie, Gaétan Messin, Antoine Browaecs, and Philippe Grangier, 2006, "Quantum interference between two single photons emitted by independently trapped atoms," Nature (London) 440, 779.  
Biagi, Nicola, Luca S Costanzo, Marco Bellini, and Alessandro Zavatta, 2018, "Entangling macroscopic light states by delocalized photon addition," arXiv:1811.10466.  
Bialynicki-Birula, I., 1996, in Progress in Optics, Vol. XXXVI, edited by E. Wolf (Elsevier, Amsterdam), pp. 245-294.  
Bloch, Claude, and Albert Messiah, 1962, "The canonical form of an antisymmetric tensor and its application to the theory of superconductivity," Nucl. Phys. 39, 95-106.  
Boyer, V., A.M. Marino, and P.D. Lett, 2008, "Generation of Spatially Broadband Twin Beams for Quantum Imaging," Phys. Rev. Lett. 100, 143601.  
Boyer, V., A.M. Marino, R.C. Pooser, and P.D. Lett, 2008, "Entangled images from four-wave mixing," Science 321, 544-547.  
Braunstein, Samuel L., 2005, "Squeezing as an irreducible resource," Phys. Rev. A 71, 055801.  
Braunstein, Samuel L., and Carlton M. Caves, 1994, "Statistical Distance and the Geometry of Quantum States," Phys. Rev. Lett. 72, 3439.  
Braunstein, Samuel L., and Arun K. Pati, 2012, Quantum Information with Continuous Variables (Springer Science+Business Media, New York).  
Brecht, B., Dileep V. Reddy, Ch Silberhorn, and M. G. Raymer, 2015, "Photon Temporal Modes: A Complete Framework for Quantum Information Science," Phys. Rev. X 5, 041017.  
Bruss, Dagmar, and Gerd Leuchs, 2019, Quantum Information: From Foundations to Quantum Technology Applications, Vols. I and II (John Wiley & Sons, New York).  
Bylander, J., I. Robert-Philip, and I. Abram, 2003, "Interference and correlation of two independent photons," Eur. Phys. J. D 22, 295-301.  
Cai, Y., J. Roslund, G. Ferrini, F. Arzani, X. Xu, C. Fabre, and Nicolas Treps, 2017, "Multimode entanglement in reconfigurable graph states using optical frequency combs," Nat. Commun. 8, 15645.  
Cariolaro, Gianfranco, and Gianfranco Pierobon, 2016, "Bloch-Messiah reduction of Gaussian unitaries by Takagi factorization," Phys. Rev. A 94, 062109.  
Carpenter, Joel, Chunle Xiong, Matthew J. Collins, Juntao Li, Thomas F. Krauss, Benjamin J. Eggleton, Alex S. Clark, and Jochen Schröder, 2013, "Mode multiplexed single-photon and classical channels in a few-mode fiber," Opt. Express 21, 28794-28800.  
Caves, Carlton, 1981, "Quantum-mechanical noise in an interferometer," Phys. Rev. D 23, 1693-1708.  
Caves, Carlton, 1982, "Quantum limits on noise in linear amplifiers," Phys. Rev. D 26, 1817-1839.  
Caves, Carlton, Joshua Combes, Zhang Jiang, and Shashank Pandey, 2012, "Quantum limits on phase-preserving linear amplifiers," Phys. Rev. A 86, 063802.  
Chalopin, B., F. Scazza, C. Fabre, and N. Treps, 2010, "Multimode nonclassical light generation through the optical-parametric-oscillator threshold," Phys. Rev. A 81, 061804(R).  
Chalopin, Benoit, Francesco Scazza, Claude Fabre, and Nicolas Treps, 2011, "Direct generation of a multi-transverse mode non-classical state of light," Opt. Express 19, 4405-4410.  
Chandrasekharan, Harikumar K., et al., 2017, "Multiplexed single-mode wavelength-to-time mapping of multimode light," Nat. Commun. 8, 14080.

Chembo, Yanne K., 2016, "Quantum dynamics of Kerr optical frequency combs below and above threshold: Spontaneous four-wave mixing, entanglement, and squeezed states of light," Phys. Rev. A 93, 033820.  
Chen, M., N.C. Menicucci, and O. Pfister, 2014, "Experimental Realization of Multipartite Entanglement of 60 Modes of a Quantum Optical Frequency Comb," Phys. Rev. Lett. 112, 120505.  
Chille, Vanessa, Nicolas Treps, Claude Fabre, Gerd Leuchs, Christoph Marquardt, and Andrea Aiello, 2016, "Detecting the spatial quantum uncertainty of bosonic systems," New J. Phys. 18, 093004.  
Chrapkiewicz, Radoslaw, Michal Jachura, Konrad Banaszek, and Wojciech Wasilewski, 2016, "Hologram of a single photon," Nat. Photonics 10, 576.  
Coffman, Valerie, Joydip Kundu, and William K. Wootters, 2000, "Distributed entanglement," Phys. Rev. A 61, 052306.  
Cohen-Tannoudji, C., J. Dupont Roc, and G. Grynberg, 1987, Photons and Atoms: Introduction to Quantum Electrodynamics (Wiley-VCH, Weinheim).  
Comon, Pierre, 1994, "Independent component analysis, a new concept?", Signal Process. 36, 287-314.  
Corzo, Neil, Alberto M. Marino, Kevin M. Jones, and Paul D. Lett, 2011, "Multi-spatial-mode single-beam quadrature squeezed states of light from four-wave mixing in hot rubidium vapor," Opt. Express 19, 21358-21369.  
Cui, Liang, Xiaoying Li, and Ningbo Zhao, 2012, "Spectral properties of photon pairs generated by spontaneous four-wave mixing in inhomogeneous photonic crystal fibers," Phys. Rev. A 85, 023825.  
Curtz, Noel, Rob Thew, Christoph Simon, Nicolas Gisin, and Hugo Zbinden, 2010, "Coherent frequency-down-conversion interface for quantum repeaters," Opt. Express 18, 22099-22104.  
Davis, Alex O. C., Valerian Thiel, Michal Karpinski, and Brian J. Smith, 2018, "Measuring the Single-Photon Temporal-Spectral Wave Function," Phys. Rev. Lett. 121, 083602.  
Dawes, A., and M. Beck, 2001, "Simultaneous quantum-state measurements using array detection," Phys. Rev. A 63, 040101.  
de Valcarcel, G.J., G. Patera, N. Treps, and C. Fabre, 2006, "Multimode squeezing of frequency combs," Phys. Rev. A 74, 061801(R).  
Defienne, Hugo, Marco Barbieri, Ian A. Walmsley, Brian J. Smith, and Sylvain Gigan, 2016, "Two-photon quantum walk in a multimode fiber," Sci. Adv. 2, e1501054.  
Delaubert, V., N. Treps, C. Fabre, H. A. Bachor, and P. Réfrégier, 2008, “Quantum limits in image processing,” Europhys. Lett. 81, 44001.  
Delaubert, Vincent, Nicolas Treps, Mikael Lassen, Charles C. Harb, Claude Fabre, Ping Koy Lam, and Hans A. Bachor, 2006, "TEM<sub>10</sub> homodyne detection as an optimal small-displacement and tilt-measurement scheme," Phys. Rev. A 74, 053823.  
DiGuglielmo, J., A. Samblowski, B. Hage, C. Pineda, J. Eisert, and R. Schnabel, 2011, "Experimental Unconditional Preparation and Detection of a Continuous Bound Entangled State of Light," Phys. Rev. Lett. 107, 240503.  
Donohue, John M., Vahid Ansari, Jaroslav Reháček, Zdenek Hradil, Bohumil Stoklasa, Martin Paur, Luis L. Sánchez-Soto, and Christine Silberhorn, 2018, "Quantum-Limited Time-Frequency Estimation through Mode-Selective Photon Measurement," Phys. Rev. Lett. 121, 090501.  
Dosseva, Annamaria, Łukasz Cincio, and Agata M. Brańczyk, 2016, "Shaping the joint spectrum of down-converted photons through optimized custom poling," Phys. Rev. A 93, 013801.

Drummond, Peter D., and Paul Kinsler, 1995, "Triple correlations in non-degenerate parametric oscillators," Quantum Semiclassical Opt. 7, 727.  
Drummond, P. D., R. M. Shelby, S. R. Friberg, and Y. Yamamoto, 1993, "Quantum solitons in optical fibres," Nature (London) 365, 307-313.  
Duan, L.-M., G. Giedke, J. I. Cirac, and P. Zoller, 2000, "Inseparability Criterion for Continuous Variable Systems," Phys. Rev. Lett. 84, 2722.  
Dyakonov, I. V., P. R. Sharapova, T. Sh. Iskhakov, and G. Leuchs, 2015, "Direct Schmidt number measurement of high-gain parametric down conversion," Laser Phys. Lett. 12, 065202.  
Eaton, Miller, Rajveer Nehra, and Olivier Pfister, 2019a, "Non-Gaussian and Gottesman-Kitaev-Preskill state preparation by photon catalysis," New J. Phys. 21, 113034.  
Eaton, Miller, Rajveer Nehra, and Olivier Pfister, 2019b, "Photon-number-resolving detection for viable Gottesman-Kitaev-Preskill state preparation," in Frontiers in Optics (Optical Society of America, Washington, DC), p. JTu4A.46.  
Eckstein. Andreas, Benjamin Brecht, and Christine Silberhorn, 2011, "A quantum pulse gate based on spectrally engineered sum frequency generation," Opt. Express 19, 13770-13778.  
Einstein, A., B. Podolsky, and N. Rosen, 1935, "Can quantum-mechanical description of physical reality be considered complete?", Phys. Rev. 47, 777-780.  
Eisaman, Matthew D., Jing Fan, Alan Migdall, and Sergey V Polyakov, 2011, "Invited review article: Single-photon sources and detectors," Rev. Sci. Instrum. 82, 071101.  
Embrey, C. S., M. T. Turnbull, P. G. Petrov, and Vincent Boyer, 2015, "Observation of Localized Multi-Spatial-Mode Quadrature Squeezing," Phys. Rev. X 5, 031004.  
Fabre, C., J. B. Fouet, and A. Maitre, 2000, "Quantum limits in the measurement of very small displacements in optical images," Opt. Lett. 25, 76-78.  
Fabre, Claude, Matthias Vaupel, Nicolas Treps, Pierre-François Cohadon, Catherine Schwob, and Agnès Maître, 2000, “C.w. optical parametric oscillators: Single mode or multimode?” C.R. Acad. Sci. Ser. Gen., Ser. 4 1, 553–559.  
Fan, Shanhui, and Joseph M. Kahn, 2005, "Principal modes in multimode waveguides," Opt. Lett. 30, 135-137.  
Ferrini, G., I. Fsaifes, T. Labidi, F. Goldfarb, Nicolas Treps, and F. Bretenaker, 2014, "Symplectic approach to the amplification process in a nonlinear fiber: Role of signal-idler correlations and application to loss management," J. Opt. Soc. Am. B 31, 1627.  
Ferrini, G., J. P. Gazeau, T. Coudreau, C. Fabre, and N. Treps, 2013, "Compact gaussian quantum computation by multi-pixel homodyne detection," New J. Phys. 15, 093015.  
Ferrini, G., J. Roslund, F. Arzani, C. Fabre, and N. Treps, 2016, "Direct approach to Gaussian measurement based quantum computation," Phys. Rev. A 94, 062332.  
Finger, M. A, N. Y. Joly, P. St. J. Russell, and M. V. Chekhova, 2017, "Characterization and shaping of the time-frequency schmidt mode spectrum of bright twin beams generated in gas-filled hollow-core photonic crystal fibers," Phys. Rev. A 95, 053814.  
Fontaine, Nicolas K., Roland Ryf, Joss Bland-Hawthorn, and Sergio G. Leon-Saval, 2012, "Geometric requirements for photonic lanterns in space division multiplexing," Opt. Express 20, 27123-27132.  
Franke-Arnold, Sonja, Alessandra Gatti, and Nicolas Treps, 2013, "High dimensional quantum entanglement," Eur. Phys. J. D 67, 104.  
Fukui, Kosuke, Akihisa Tomita, Atsushi Okamoto, and Keisuke Fujii, 2018, “High-Threshold Fault-Tolerant Quantum

Computation with Analog Quantum Error Correction," Phys. Rev. X 8, 021054.  
Furusawa, Akira, 2015, Quantum States of Light (Springer, New York).  
Furusawa, Akira, Jens Lykke Sorensen, Samuel L. Braunstein, Christopher A. Fuchs, H. Jeff Kimble, and Eugene S. Polzik, 1998, "Unconditional quantum teleportation," Science 282, 706-709.  
Gabriel, C., et al., 2011, "Entangling Different Degrees of Freedom by Quadrature Squeezing Cylindrically Polarized Modes," Phys. Rev. Lett. 106, 060502.  
Gagatsos, Christos N., and Saikat Guha, 2019, "Efficient representation of Gaussian states for multimode non-Gaussian quantum state engineering via subtraction of arbitrary number of photons," Phys. Rev. A 99, 053816.  
Gatti, A., E. Brambilla, L. Caspani, O. Jedrkiewicz, and L. A. Lugiato, 2009, "X Entanglement: The Nonfactorable Spatiotemporal Structure of Biphoton Correlation," Phys. Rev. Lett. 102, 223601.  
Gatti, A., T. Corti, E. Brambilla, and D. Horoshko, 2012, "Dimensionality of the spatiotemporal entanglement of parametric downconversion photon pairs," Phys. Rev. A 86, 053803.  
Gerke, S., J. Sperling, W. Vogel, Y. Cai, J. Roslund, N. Treps, and C. Fabre, 2015, "Full Multipartite Entanglement of Frequency-Comb Gaussian States," Phys. Rev. Lett. 114, 050501.  
Gerke, S., J. Sperling, W. Vogel, Y. Cai, J. Roslund, N. Treps, and C. Fabre, 2016, "Multipartite Entanglement of a Two-Separable State," Phys. Rev. Lett. 117, 110502.  
Gessner, Manuel, Luca Pezzè, and Augusto Smerzi, 2016, "Efficient entanglement criteria for discrete, continuous, and hybrid variables," Phys. Rev. A 94, 020101.  
Gigan, Sylvain, Laurent Lopez, Vincent Delaubert, Nicolas Treps, Claude Fabre, and Agnes Maitre, 2005, "Continuous-wave phase-sensitive parametric image amplification," arXiv:quant-ph/0502116.  
Giorgi, Gian, Bruno Bellomo, Fernando Galve, and Roberta Zambrini, 2011, "Genuine Quantum and Classical Correlations in Multipartite Systems," Phys. Rev. Lett. 107, 190501.  
Giovannetti, Vittorio, Seth Lloyd, and Lorenzo Maccone, 2011, "Advances in quantum metrology," Nat. Photonics 5, 222.  
Giovannetti, Vittorio, Stefano Mancini, David Vitali, and Paolo Tombesi, 2003, "Characterizing the entanglement of bipartite quantum systems," Phys. Rev. A 67, 022320.  
Gittsovich, Oleg, Otfried Gühne, Philipp Hyllus, and Jens Eisert, 2008, “Unifying several separability conditions using the covariance matrix criterion,” Phys. Rev. A 78, 052319.  
Glauber, Roy, 1963, "The quantum theory of optical coherence," Phys. Rev. 130, 2529-2539.  
Glorieux, Quentin, Luca Guidoni, Samuel Guibal, Jean-Pierre Likforman, and Thomas Coudreau, 2011, "Quantum correlations by four-wave mixing in an atomic vapor in a nonamplifying regime: Quantum beam splitter for photons," Phys. Rev. A 84, 053826.  
Goodman, Joseph W., 2015, Statistical Optics (John Wiley & Sons, New York).  
Gottesman, D., A. Kitaev, and J. Preskill, 2001, Phys. Rev. A 64, 012310.  
Grynberg, Gilbert, Alain Aspect, and Claude Fabre, 2010, Introduction to Quantum Optics: From the Semi-classical Approach to Quantized Light (Cambridge University Press, Cambridge, England).

Gu, Mile, Christian Weedbrook, Nicolas Menicucci, Timothy Ralph, and Peter van Loock, 2009, "Quantum computing with continuous-variable clusters," Phys. Rev. A 79, 062318.  
Guasoni, M., 2016, "Wideband multimode parametric amplification in optical fibers," in Photonics and Fiber Technology 2016 (Optical Society of America, Washington, DC), p. 22.  
Gühne, Otfried, and Geza Toth, 2009, "Entanglement detection," Phys. Rep. 474, 1-75.  
Guo, Xueshi, Nannan Liu, Xiaoying Li, and Z. Y. Ou, 2015, "Complete temporal mode analysis in pulse-pumped fiber-optical parametric amplifier for continuous variable entanglement generation," Opt. Express 23, 29369-29383.  
Guo, Yu, and Heng Fan, 2015, "A generalization of Schmidt number for multipartite states," Int. J. Quantum. Inf. 13, 1550025.  
Helstrom, C. W., 1967, "Minimum mean-squared error of estimates in quantum statistics," Phys. Lett. 25A, 101-102.  
Helstrom, Carl, 1968, "The minimum variance of estimates in quantum signal detection," IEEE Trans. Inf. Theory 14, 234-242.  
Helstrom, Carl W., 1969, "Quantum detection and estimation theory," J. Stat. Phys. 1, 231-252.  
Hermier, J.-P., Alberto Bramati, A. Z. Khoury, Elisabeth Giacobino, J.-Ph. Poizat, T. J. Chang, and Ph. Grangier, 1999, "Spatial quantum noise of semiconductor lasers," J. Opt. Soc. Am. B 16, 2140-2146.  
Hillery, Mark, Ho Trung Dung, and Hongjun Zheng, 2010, "Conditions for entanglement in multipartite systems," Phys. Rev. A 81, 062322.  
Hong, C. K., Z. Y. Ou, and L. Mandel, 1987, "Measurement of Subpicosecond Intervals between Two Photons by Interference," Phys. Rev. Lett. 59, 2044-2046.  
Horodecki, Ryszard, Paweł Horodecki, Michal Horodecki, and Karol Horodecki, 2009, "Quantum entanglement," Rev. Mod. Phys. 81, 865-942.  
Horoshko, D. B., L. La Volpe, F. Arzani, N. Treps, C. Fabre, and M. I. Kolobov, 2019, "Bloch-Messiah reduction for twin beams of light" arXiv:1903.06578.  
Hsu, Magnus T. L., Vincent Delaubert, Ping Koy Lam, and Warwick P. Bowen, 2004, "Optimal optical measurement of small displacements," J. Opt. B 6, 495-501.  
Huber, Marcus, and Julio de Vicente, 2013, "Structure of Multidimensional Entanglement in Multipartite Systems," Phys. Rev. Lett. 110, 030501.  
Huntington, E. H., G. N. Milford, C. Robilliard, T. C. Ralph, O. Glöckl, Ulrik L. Andersen, S. Lorenz, and Gerd Leuchs, 2005, "Demonstration of the spatial separation of the entangled quantum sidebands of an optical field," Phys. Rev. A 71, 041802.  
Hyllus, P., and J. Eisert, 2006, "Optimal entanglement witnesses for continuous-variable systems," New J. Phys. 8, 51.  
Iskhakov, T. Sh., V.C. Usenko, U.L. Andersen, R. Filip, M.V. Chekhova, and G. Leuchs, 2016, "Heraldused source of bright multimode mesoscopic sub-Poissonian light," Opt. Lett. 41, 2149-2152.  
Ivan, J., S. Chaturvedi, E. Ercolessi, G. Marmo, G. Morandi, N. Mukunda, and R. Simon, 2011, "Entanglement and nonclassicality for multimode radiation-field states," Phys. Rev. A 83, 032118.  
Jachura, Michal, Michal Karpinski, Czesław Radzewicz, and Konrad Banaszek, 2014, "High-visibility nonclassical interference of photon pairs generated in a multimode nonlinear waveguide," Opt. Express 22, 8624-8632.  
Jedrkiewicz, O., A. Gatti, E. Brambilla, and P. Di. Trapani, 2012, "Experimental Observation of a Skewed  $X$ -Type Spatiotemporal Correlation of Ultrabroadband Twin Beams," Phys. Rev. Lett. 109, 243901.

Jedrkiewicz, O., Y. K. Jiang, E. Brambilla, A. Gatti, M. Bache, L. Lugiato, and P. Di Trapani, 2004, "Detection of Sub-Shot-Noise Spatial Correlation in High-Gain Parametric Down Conversion," Phys. Rev. Lett. 93, 243601.  
Jian, Pu., Olivier Pinel, Claude Fabre, Brahim Lamine, and Nicolas Treps, 2012, "Real-time displacement measurement immune from atmospheric parameters using optical frequency combs," Opt. Express 20, 27133-27146.  
Jiang, Shifeng, Nicolas Treps, and Claude Fabre, 2012, "A time/frequency quantum analysis of the light generated by synchronously pumped optical parametric oscillators," New J. Phys. 14, 043006.  
Kaltenbaek, Rainer, Bibiane Blauensteiner, Marek Zukowski, Markus Aspelmeyer, and Anton Zeilinger, 2006, "Experimental Interference of Independent Photons," Phys. Rev. Lett. 96, 240502.  
Karny, Z., S. Lavi, and O. Kafir, 1983, "Direct determination of the number of transverse modes of a light beam," Opt. Lett. 8, 409-411.  
Karpinski, Michal, Michal Jachura, Laura J. Wright, and Brian J. Smith, 2017, "Bandwidth manipulation of quantum light by an electro-optic time lens," Nat. Photonics 11, 53.  
Kenfack, Anatole, and Karol Žyczkowski, 2004, “Negativity of the Wigner function as an indicator of non-classicality,” J. Opt. B 6, 396.  
Kolner, Brian H., and Moshe Nazarathy, 1989, “Temporal imaging with a time lens,” Opt. Lett. 14, 630-632.  
Kolobov, M., 2006, Ed., Quantum Imaging (Springer-Verlag, Berlin).  
Kolobov, Mikhail, and Claude Fabre, 2000, "Quantum Limits on Optical Resolution," Phys. Rev. Lett. 85, 3789-3792.  
Kolobov, Mikhail I., 2008, "Quantum limits of superresolution for imaging discrete subwavelength structures," Opt. Express 16, 58-66.  
Kopylov, Denis, Kirill Spasibko, Tatiana Murzina, and Maria V. Chekhova, 2019, "Study of broadband multimode light via nonphase-matched sum frequency generation," New J. Phys. 21, 033024.  
Korolkova N., and G. Leuchs, 2019, "Quantum correlations in separable multi-mode states and in classically entangled light," Rep. Prog. Phys. 82, 056001.  
Korolkova, Natalia, Gerd Leuchs, Rodney Loudon, Timothy C. Ralph, and Christine Silberhorn, 2002, "Polarization squeezing and continuous-variable polarization entanglement," Phys. Rev. A 65, 052306.  
Labroille, Guillaume, BertrDenolle, Pu Jian, Philippe Genevaux, Nicolas Treps, and Jean-Francois Morizur, 2014, "Efficient and mode selective spatial mode multiplexer based on multi-plane light conversion," Opt. Express 22, 15599-15607.  
Labroille, Guillaume, Olivier Pinel, Nicolas Treps, and Manuel Joffre, 2013, "Pulse shaping with birefringent crystals: A tool for quantum metrology," Opt. Express 21, 21889-21896.  
Lamb, Willis E., 1995, "Anti-photon," Appl. Phys. B 60, 77-84.  
Lamine, Brahim, Claude Fabre, and Nicolas Treps, 2008, “Quantum Improvement of Time Transfer between Remote Clocks,” Phys. Rev. Lett. 101, 123601.  
Lane, A., P. Tombesi, H.J. Carmichael, and D.F. Walls, 1983, "Quantum statistics of multimode parametric amplification," Opt. Commun. 48, 155-160.  
Lassen, M., V. Delaubert, J. Janousek, K. Wagner, H.-A. Bchor, P. K. Lam, N. Treps, P. Buchhave, C. Fabre, and C. C. Harb, 2007, "Tools for Multimode Quantum Information: Modulation, Detection, and Spatial Quantum Correlations," Phys. Rev. Lett. 98, 083602.

Laurat, Julien, Thomas Coudreau, Nicolas Treps, Agnès Maitre, and Claude Fabre, 2003, "Conditional Preparation of a Quantum State in the Continuous Variable Regime: Generation of a Sub-Poissonian State from Twin Beams," Phys. Rev. Lett. 91, 213601.  
Law, C., and J. Eberly, 2004, "Analysis and Interpretation of High Transverse Entanglement in Optical Parametric Down Conversion," Phys. Rev. Lett. 92, 127903.  
Legero, Thomas, Tatjana Wilk, Axel Kuhn, and Gerhard Rempe, 2003, "Time-resolved two-photon quantum interference," Appl. Phys. B 77, 797-802.  
Lenhard, Andreas, José Brito, Matthias Bock, Christoph Becher, and Jürgen Eschner, 2017, "Coherence and entanglement preservation of frequency-converted heralded single photons," Opt. Express 25, 11187-11199.  
Leroyer, Hadrien, 2007, "Multimode quantum optics and symplectic algebra," master's thesis (Ecole Polytechnique).  
Leuchs, G., U. L. Andersen, and C. Fabre, 2006, "The quantum properties of multimode optical amplifiers revisited," Adv. At. Mol. Opt. Phys. 53, 139-149.  
Levenson, M. D., R. M. Shelby, and S. H. Perlmutter, 1985, "Squeezing of classical noise by nondegenerate four-wave mixing in an optical fiber," Opt. Lett. 10, 514-516.  
Levi, Federico, and Florian Mintert, 2013, "Hierarchies of Multi-partite Entanglement," Phys. Rev. Lett. 110, 150402.  
Li, Ming, Shao-Ming Fei, and Zhi-Xi Wang, 2008, "Separability and entanglement of quantum states based on covariance matrices," J. Phys. A 41, 202002.  
Liu, Cunjin, Jietai Jing, R. C. Pooser, and Weiping Zhang, 2011, "Realization of low frequency and controllable bandwidth squeezing based on a four-wave-mixing amplifier in rubidium vapor," Opt. Lett. 36, 2979-2981.  
Lopez, L., B. Chalopin, A. Rivière de La Souchère, C. Fabre, A. Maitre, and N. Treps, 2009, "Multimode quantum properties of a self-imaging optical parametric oscillator: Squeezed vacuum and Einstein-Podolsky-Rosen-beams generation," Phys. Rev. A 80, 043816.  
Lu, Hsuan-Hao, Joseph M. Lukens, Nicholas A. Peters, Brian P. Williams, Andrew M. Weiner, and Pavel Lougovski, 2018, "Quantum interference and correlation control of frequency-bin qubits," Optica 5, 1455-1460.  
Lugiato, L. A., and A. Gatti, 1993, "Spatial Structure of a Squeezed Vacuum," Phys. Rev. Lett. 70, 3868-3870.  
Lugiato, L. A., and I. Marzoli, 1995, "Quantum spatial correlations in the optical parametric oscillator with spherical mirrors," Phys. Rev. A 52, 4886.  
Lupo, Cosmo, and Stefano Pirandola, 2016, "Ultimate Precision Bound of Quantum and Subwavelength Imaging," Phys. Rev. Lett. 117, 190802.  
Lvovsky, Alexander I., Hauke Hansen, T. Aichele, O. Benson, J. Mlynek, and S. Schiller, 2001, "Quantum State Reconstruction of the Single-Photon Fock State," Phys. Rev. Lett. 87, 050402.  
Mancini, S., and Simone Severini, 2006, "The quantum separability problem for Gaussian states, in Proceedings of the Workshop on Logic, Models and Computer Science (LMCS 2006), Camerino, Italy, edited by F. Corradini and C. Toffalori (Elsevier, New York), pp. 121-131.  
Mandel, Leonard, and Emil Wolf, 1995, Optical Coherence and Quantum Optics (Cambridge University Press, Cambridge, England).  
Mari, A., and J. Eisert, 2012, "Positive Wigner Functions Render Classical Simulation of Quantum Computation Efficient," Phys. Rev. Lett. 109, 230503.

Marin, F., Alberto Bramati, Elisabeth Giacobino, T.-C. Zhang, J.-Ph. Poizat, J.-F. Roch, and Philippe Grangier, 1995, "Squeezing and Intermode Correlations in Laser Diodes," Phys. Rev. Lett. 75, 4606.  
Marino, A.M., and P. Lett, 2012, "Noiseless Optical Amplifier Operating on Hundreds of Spatial Modes," Phys. Rev. Lett. 109, 043602.  
Marte, Monika A. M., H. Ritsch, K. Petsas, Alessandra Gatti, Luigi Lugiato, Claude Fabre, and D. Leduc, 1998, "Spatial patterns in optical parametric oscillators with spherical mirrors: classical and quantum effects," Opt. Express 3, 71-80.  
Martinelli, M., N. Treps, S. Ducci, S. Gigan, A. Maitre, and C. Fabre, 2003, "Experimental study of the spatial distribution of quantum correlations in a confocal optical parametric oscillator," Phys. Rev. A 67, 023808.  
McCormick, C. F., V. Boyer, E. Arimondo, and P. Lett, 2007, "Strong relative intensity squeezing by four-wave mixing in rubidium vapor," Opt. Lett. 32, 178.  
McGuinness, H. J., M. G. Raymer, C. J. McKinstrie, and S. Radic, 2010, "Quantum Frequency Translation of Single-Photon States in a Photonic Crystal Fiber," Phys. Rev. Lett. 105, 093604.  
McKinstrie, C., L. Mejling, M. Raymer, and K. Rottwitt, 2012, "Quantum-state-preserving optical frequency conversion and pulse reshaping by four-wave mixing," Phys. Rev. A 85, 053829.  
Mecozzi, Antonio, and Prem Kumar, 1998, "Sub-Poissonian light by spatial soliton filtering," Quantum Semiclassical Opt. 10, L21-L26.  
Medeiros de Araújo, R., J. Roslund, Y. Cai, G. Ferrini, C. Fabre, and N. Treps, 2014, "Full characterization of a multimode entangled state embedded in an optical frequency comb using pulse shaping," Phys. Rev. A 89, 053828.  
Menicucci, Nicolas, Peter van Loock, Mile Gu, Christian Weedbrook, Timothy Ralph, and Michael Nielsen, 2006, "Universal Quantum Computation with Continuous-Variable Cluster States," Phys. Rev. Lett. 97, 110501.  
Menicucci, Nicolas C., 2014, "Fault-Tolerant Measurement-Based Quantum Computing with Continuous-Variable Cluster States," Phys. Rev. Lett. 112, 120504.  
Menicucci, Nicolas C., Steven T. Flammia, and Olivier Pfister, 2008, "One-Way Quantum Computing in the Optical Frequency Comb," Phys. Rev. Lett. 101, 130501.  
Mertz, J., A. Heidmann, C. Fabre, E. Giacobino, and S. Reynaud, 1990, "Observation of High-Intensity Sub-Poissonian Light Using an Optical Parametric Oscillator," Phys. Rev. Lett. 64, 2897.  
Milione, Giovanni, Daniel A. Nolan, and Robert R. Alfano, 2015, "Determining principal modes in a multimode optical fiber using the mode dependent signal delay method," J. Opt. Soc. Am. B 32, 143-149.  
Mirhosseini, Mohammad, Omar S. Magana-Loaiza, Malcolm N. O'Sullivan, Brandon Rodenburg, Mehul Malik, Martin P. J. Lavery, Miles J. Padgett, Daniel J. Gauthier, and Robert W. Boyd, 2015, "High-dimensional quantum cryptography with twisted light," New J. Phys. 17, 033033.  
Miyata, Kazunori, Hisashi Ogawa, Petr Marek, Radim Filip, Hidehiro Yonezawa, Jun-ichi Yoshikawa, and Akira Furusawa, 2016, "Implementation of a quantum cubic gate by an adaptive nongaussian measurement," Phys. Rev. A 93, 022301.  
Mohanty, Aseema, Mian Zhang, Avik Dutt, Sven Ramelow, Paulo Nussenzveig, and Michal Lipson, 2017, "Quantum interference between transverse spatial waveguide modes," Nat. Commun. 8, 14010.  
Mollow, B. R., 1968, "Quantum theory of field attenuation," Phys. Rev. 168, 1896.

Morin, O., M. Körber, S. Langenfeld, and G. Rempe, 2019, "Deterministic Shaping and Reshaping of Single-Photon Temporal Wave Functions," Phys. Rev. Lett. 123, 133602.  
Morin, Olivier, Claude Fabre, and Julien Laurat, 2013, "Experimentally Accessing the Optimal Temporal Mode of Traveling Quantum Light States," Phys. Rev. Lett. 111, 213602.  
Morizur, J.-F., Seiji Armstrong, Nicolas Treps, Jiri Janousek, and H.-A. Bchor, 2011, "Spatial reshaping of a squeezed state of light," Eur. Phys. J. D 61, 237-239.  
Morizur, Jean-François, Lachlan Nicholls, Pu Jian, Seiji Armstrong, Nicolas Treps, Boris Hage, Magnus Hsu, Warwick Bowen, Jiri Janousek, and Hans-A. Bacher, 2010, "Programmable unitary spatial mode manipulation," J. Opt. Soc. Am. A 27, 2524-2531.  
Mosset, Alexis, Fabrice Devaux, and Eric Lantz, 2005, "Spatially Noiseless Optical Amplification of Images," Phys. Rev. Lett. 94, 223603.  
Namiki, Ryo, 2016, "Schmidt-number benchmarks for continuous-variable quantum devices," Phys. Rev. A 93, 052336-11.  
Napoli, Carmine, Samanta Piano, Richard Leach, Gerardo Adesso, and Tommaso Tufarelli, 2019, "Towards Superresolution Surface Metrology: Quantum Estimation of Angular and Axial Separations," Phys. Rev. Lett. 122, 140505.  
Navarrete-Benlloch, Carlos, Giuseppe Patera, and Germán J. de Valcárcel, 2017, "Noncritical generation of nonclassical frequency combs via spontaneous rotational symmetry breaking," Phys. Rev. A 96, 043801.  
Newton, Isaac, 1704, Opticks (Courier Corporation, London).  
Nichols, Rosanna, Pietro Liuzzo-Scorpo, Paul A. Knott, and Gerardo Adesso, 2018, "Multiparameter Gaussian quantum metrology," Phys. Rev. A 98, 012114.  
Nielsen, Anne E. B., and Klaus Mølmer, 2007, "Multimode analysis of the light emitted from a pulsed optical parametric oscillator," Phys. Rev. A 76, 033832.  
Nunn, J., K. Reim, K.C. Lee, V.O. Lorenz, B.J. Sussman, I.A. Walmsley, and D. Jaksch, 2008, "Multimode Memories in Atomic Ensembles," Phys. Rev. Lett. 101, 260502.  
Nykolak, G., S.A. Kramer, J.R. Simpson, D.J. DiGiovanni, C.R. Giles, and H.M. Presby, 1991, "An erbium-doped multimode optical fiber amplifier," IEEE Photonics Technol. Lett. 3, 1079-1081.  
Opatny, T., N. Korolkova, and G. Leuchs, 2002, "Mode structure and photon number correlations in squeezed quantum pulses," Phys. Rev. A 66, 053813.  
Ou, Zhe Yu, 2017, Quantum Optics for Experimentalists (World Scientific, Singapore).  
Ourjoumtsev, Alexei, Aurelien Dantan, Rosa Tualle-Brouri, and Philippe Grangier, 2007, "Increasing Entanglement between Gaussian States by Coherent Photon Subtraction," Phys. Rev. Lett. 98, 030502.  
Parigi, Valentina, Alessandro Zavatta, Myungshik Kim, and Marco Bellini, 2007, "Probing quantum commutation rules by addition and subtraction of single photons to/from a light field," Science 317, 1890-1893.  
Patera, G., C. Navarrete-Benlloch, G. J. de Valcárcel, and C. Fabre, 2012, "Quantum coherent control of highly multipartite continuous-variable entangled states by tailoring parametric interactions," Eur. Phys. J. D 66, 241.  
Patera, G., N. Treps, C. Fabre, and G.J. de Valcarcel, 2010, "Quantum theory of synchronously pumped type I optical parametric oscillators: Characterization of the squeezed supermodes," Eur. Phys. J. D 56, 123-140.

Patera, Giuseppe, Dmitri B. Horoshko, and Mikhail I. Kolobov, 2018, "Space-time duality and quantum temporal imaging," Phys. Rev. A 98, 053815.  
Pati, Arun K., 2000, "Existence of the Schmidt decomposition for tripartite systems," Phys. Lett. A 278, 118-122.  
Paúr, Martin, Bohumil Stoklasa, Zdenek Hradil, Luis L. Sánchez-Soto, and Jaroslav Rehacek, 2016, "Achieving the ultimate optical resolution," Optica 3, 1144-1147.  
Pe'er, Avi, Barak Dayan, Asher A. Friesem, and Yaron Silberberg, 2005, "Temporal Shaping of Entangled Photons," Phys. Rev. Lett. 94, 073601.  
Peres, Asher, 1996, "Separability Criterion for Density Matrices," Phys. Rev. Lett. 77, 1413.  
Pérez, A.M., P.R Sharapova, S.S Straupe, F.M. Miatto, O.V. Tikhonova, G. Leuchs, and M.V. Chekhova, 2015, "Projective filtering of the fundamental eigenmode from spatially multimode radiation," Phys. Rev. A 92, 053861-10.  
Perina, Jan. 2016, "Spatial, spectral, and temporal coherence of ultraintense twin beams," Phys. Rev. A 93, 013852.  
Perina, Jr., Jan, Martin Hamar, Václav Michalek, and Ondrej Haderka, 2012, "Photon-number distributions of twin beams generated in spontaneous parametric down-conversion and measured by an intensified CCD camera," Phys. Rev. A 85, 023816.  
Phillips, D. S., M. Walschaers, J. J. Renema, I. A. Walmsley, Nicolas Treps, and J. Sperling, 2019, "Benchmarking of Gaussian boson sampling using two-point correlators," Phys. Rev. A 99, 023836.  
Pinel, O., P. Jian, N. Treps, C. Fabre, and D. Braun, 2013, "Quantum parameter estimation using general single-mode Gaussian states," Phys. Rev. A 88, 040102.  
Pinel, Olivier, Julien Fade, Daniel Braun, Pu Jian, Nicolas Treps, and Claude Fabre, 2012, "Ultimate sensitivity of precision measurements with intense Gaussian quantum light: A multimodal approach," Phys. Rev. A 85, 010101.  
Pinel, Olivier, Pu Jian, Renn 'e Medeiros de Ara 'ujo, Jinxia Feng, Beno it Chalopin, Claude Fabre, and Nicolas Treps, 2012, "Generation and Characterization of Multimode Quantum Frequency Combs," Phys. Rev. Lett. 108, 083601.  
Pirandola, Stefano, and Seth Lloyd, 2008, "Computable bounds for the discrimination of Gaussian states," Phys. Rev. A 78, 012331.  
Polycarpou, C., K. N. Cassemiro, G. Venturi, A. Zavatta, and M. Bellini, 2012, "Adaptive Detection of Arbitrarily Shaped Ultrashort Quantum Light States," Phys. Rev. Lett. 109, 053602.  
Pooser, Raphael, and Jietai Jing, 2014, "Continuous-variable cluster-state generation over the optical spatial mode comb," Phys. Rev. A 90, 043841.  
Pooser, Raphael C., and Benjamin Lawrie, 2015, "Ultrasensitive measurement of microcantilever displacement below the shot-noise limit," Optica 2, 393-399.  
Pysher, Matthew, Yoshichika Miwa, Reihaneh Shahrokhshahi, Russell Bloomer, and Olivier Pfister, 2011, "Parallel Generation of Quadripartite Cluster Entanglement in the Optical Frequency Comb," Phys. Rev. Lett. 107, 030505.  
Qin, Zhongzhong, Leiming Cao, Hailong Wang, A.M. Marino, Weiping Zhang, and Jietai Jing, 2014, "Experimental Generation of Multiple Quantum Correlated Beams from Hot Rubidium Vapor," Phys. Rev. Lett. 113, 023602.  
Qin, Zhongzhong, Adarsh S Prasad, Travis Brannan, Andrew MacRae, A. Lezama, and A. I. Lvovsky, 2015, "Complete temporal characterization of a single photon," Light Sci. Appl. 4, e298.  
Quesada, Nicolas, Juan Miguel Arrazola, and Nathan Killoran, 2018, "Gaussian boson sampling using threshold detectors," Phys. Rev. A 98, 062322.

Ra, Young-Sik, Adrien Dufour, Mattia Walschaers, Clement Jacquard, Thibault Michel, Claude Fabre, and Nicolas Treps, 2020, "Non-Gaussian quantum states of a multimode light field," Nat. Phys. 16, 144-147.  
Ra, Young-Sik, Clément Jacquard, Adrien Dufour, Claude Fabre, and Nicolas Treps, 2017, "Tomography of a Mode-Tunable Coherent Single-Photon Subtractor," Phys. Rev. X 7, 031012.  
Raussendorf, Robert, and Hans J. Briegel, 2001, “A One-Way Quantum Computer,” Phys. Rev. Lett. 86, 5188-5191.  
Reck, Michael, Anton Zeilinger, Herbert J. Bernstein, and Philip Bertani, 1994, "Experimental Realization of Any Discrete Unitary Operator," Phys. Rev. Lett. 73, 58-61.  
Reddy, Dileep V., and Michael G. Raymer, 2018, "High-selectivity quantum pulse gating of photonic temporal modes using all-optical Ramsey interferometry," Optica 5, 423-428.  
Reddy, Dileep V., Michael G. Raymer, and Colin J. McKinstrie, 2014, "Efficient sorting of quantum-optical wave packets by temporal-mode interferometry," Opt. Lett. 39, 2924-2927.  
Réfrégier, Philippe, and François Goudail, 2005, "Invariant degrees of coherence of partially polarized light," Opt. Express 13, 6051.  
Ren, Yongxiong, et al., 2017, "Spatially multiplexed orbital-angular-momentum-encoded single photon and classical channels in a free-space optical communication link," Opt. Lett. 42, 4881-4884.  
Roslund, Jonathan, Renne Medeiros de Araujo, Shifeng Jiang, Claude Fabre, and Nicolas Treps, 2014, "Wavelength-multiplexed quantum networks with ultrafast frequency combs," Nat. Photonics 8, 109-112.  
Rotter, Stefan, and Sylvain Gigan, 2017, "Light fields in complex media: Mesoscopic scattering meets wave control," Rev. Mod. Phys. 89, 015005.  
Royer, Antoine, 1977, "Wigner function as the expectation value of a parity operator," Phys. Rev. A 15, 449.  
Sadana, Simanraj, Debadrita Ghosh, Kaushik Joarder, A. Naga Lakshmi, Barry C. Sanders, and Urbasi Sinha, 2018, "Near-  $100\%$  two-photon-like coincidence-visibility dip with classical light and the role of complementarity," arXiv:1810.01297.  
Safranek, Dominik, 2019, "Estimation of Gaussian quantum states," J. Phys. A 52, 035304.  
Safranek, Dominik, Antony R. Lee, and Ivette Fuentes, 2015, "Quantum parameter estimation using multi-mode Gaussian states," New J. Phys. 17, 073016.  
Sasaki, Masahide, and Shigenari Suzuki, 2006, "Multimode theory of measurement-induced non-Gaussian operation on wideband squeezed light: Analytical formula," Phys. Rev. A 73, 043807.  
Schmeissner, Roman, Jonathan Roslund, Claude Fabre, and Nicolas Treps, 2014, "Spectral Noise Correlations of an Ultrafast Frequency Comb," Phys. Rev. Lett. 113, 263906.  
Schnabel, Roman, 2017, "Squeezed states of light and their applications in laser interferometers," Phys. Rep. 684, 1-51.  
Schrödinger, Erwin, 1935, “Discussion of probability relations between separated systems,” Math. Proc. Cambridge Philos. Soc. 31, 555–563.  
Schwob, C., P. F. Cohadon, C. Fabre, M. A. M. Marte, H. Ritsch, A. Gatti, and L. Lugiato, 1998, "Transverse effects and mode couplings in OPOS," Appl. Phys. B 66, 685-699.  
Serafini, Alessio, 2006, “Multimode Uncertainty Relations and Separability of Continuous Variable States,” Phys. Rev. Lett. 96, 110402.  
Shah, A. R., R. C. J. Hsu, A. Tarighat, A. H. Sayed, and B. Jalali, 2005, "Coherent optical MIMO (COMIMO)," J. Lightwave Technol. 23, 2410-2419.  
Shahrokhshahi, Reihaneh, and Olivier Pfister, 2011, "Multipartite entanglement in the optical frequency comb of a depleted-pump

optical parametric oscillator," in CLEO: Applications and Technology (Optical Society of America, Washington, DC), p. JThB26.  
Shapiro, Jeffrey H., and Asif Shakeel, 1997, "Optimizing homodyne detection of quadrature-noise squeezing by local-oscillator selection," J. Opt. Soc. Am. B 14, 232-249.  
Sharapova, P., Angela M. Pérez, Olga V. Tikhonova, and Maria V. Chekhova, 2015, "Schmidt modes in the angular spectrum of bright squeezed vacuum," Phys. Rev. A 91, 043816.  
Sharapova, P. R., O. V. Tikhonova, S. Lemieux, R. W. Boyd, and M. V. Chekhova, 2018, "Bright squeezed vacuum in a nonlinear interferometer: Frequency and temporal Schmidt-mode description," Phys. Rev. A 97, 053827.  
Shchukin, E., and P. van Loock, 2015, "Generalized conditions for genuine multipartite continuous-variable entanglement," Phys. Rev. A 92, 042328.  
Shchukin, E., and W. Vogel, 2006, "Universal Measurement of Quantum Correlations of Radiation," Phys. Rev. Lett. 96, 200403.  
Siegel, C. L., 1943, "Symplectic geometry," Am. J. Math. 65, 1-86.  
Siegman, Anthony E., 1998, "How to (maybe) measure laser beam quality," in Diode Pumped Solid State Lasers: Applications and Issues, edited by Mark W. Dowley (Optical Society of America, Washington, DC), Chap. 17, p. MQ1.  
Simon, R., 2000, "Peres-Horodecki Separability Criterion for Continuous Variable Systems," Phys. Rev. Lett. 84, 2726-2729.  
Simon, R., N. Mukunda, and B. Dutta, 1994, "Quantum-noise matrix for multimode systems:  $U(n)$  invariance, squeezing, and normal forms," Phys. Rev. A 49, 1567-1583.  
Simon, R., E. C. G. Sudarshan, and N. Mukunda, 1988, "Gaussian pure states in quantum mechanics and the symplectic group," Phys. Rev. A 37, 3028-3038.  
Smith, Brian J., and M. G. Raymer, 2007, "Photon wave functions, wave-packet quantization of light, and coherence theory," New J. Phys. 9, 414-414.  
Spälter, S., N. Korolkova, F. König, A. Sizmann, and Gerd Leuchs, 1998, "Observation of Multimode Quantum Correlations in Fiber Optical Solitons," Phys. Rev. Lett. 81, 786.  
Sperling, J., and W. Vogel, 2013, "Multipartite Entanglement Witnesses," Phys. Rev. Lett. 111, 110503.  
Sperling, Jan, Armando Perez-Leija, Kurt Busch, and Christine Silberhorn, 2019, "Mode-independent quantum entanglement for light," Phys. Rev. A 100, 062129.  
Streltsov, Alexander, Gerardo Adesso, and Martin B. Plenio, 2017, "Colloquium: Quantum coherence as a resource," Rev. Mod. Phys. 89, 041003.  
Su, Xiaolong, Yaping Zhao, Shuhong Hao, Xiaojun Jia, Changde Xie, and Kunchi Peng, 2012, "Experimental preparation of eight-partite cluster state for photonic qumodes," Opt. Lett. 37, 5178-5180.  
Su, XiaoLong, XiaoJun Jia, ChangDe Xie, and KunChi Peng, 2014, "Preparation of multipartite entangled states used for quantum information networks," Sci. China Phys. Mech. Astron. 57, 1210-1217.  
Takahashi, Hiroki, Kentaro Wakui, Shigenari Suzuki, Masahiro Takeoka, Kazuhiro Hayasaka, Akira Furusawa, and Masahide Sasaki, 2008, "Generation of Large-Amplitude Coherent-State Superposition via Ancilla-Assisted Photon Subtraction," Phys. Rev. Lett. 101, 233605.  
Takase, Kan, Masanori Okada, Takahiro Serikawa, Shuntaro Takeda, Jun-ichi Yoshikawa, and Akira Furusawa, 2019, "Complete temporal mode characterization of non-Gaussian states by a dual homodyne measurement," Phys. Rev. A 99, 033832.  
Tanzilli, Sebastien, Wolfgang Tittel, Matthaeus Halder, Olivier Alibart, Pascal Baldi, Nicolas Gisin, and Hugo Zbinden, 2005,

"A photonic quantum information interface," Nature (London) 437, 116.  
Taylor, Michael A., Jiri Janousek, Vincent Daria, Joachim Knittel, Boris Hage, Hans-A. Bachor, and Warwick P. Bowen, 2013, "Biological measurement beyond the quantum limit," Nat. Photonics 7, 229-233.  
Teh, R. Y., and M. D. Reid, 2014, "Criteria for genuine  $N$ -partite continuous-variable entanglement and Einstein-Podolsky-Rosen steering," Phys. Rev. A 90, 062337.  
Thiel, Valerian, Pu Jian, Claude Fabre, Nicolas Treps, and Jonathan Roslund, 2016, "Absolute measurement of quantum-limited interferometric displacements," arXiv:1602.02581.  
Thirring, W., R. A. Bertlmann, P. Kohler, and H. Narnhofer, 2011, "Entanglement or separability: The choice of how to factorize the algebra of a density matrix," Eur. Phys. J. D 64, 181-196.  
Titchener, James G., Alexander S. Solntsev, and Andrey A. Sukhorukov, 2016, "Photonic cluster state generation in nonlinear waveguide arrays," in Photonics and Fiber Technology 2016 (ACOFT, BGPP, NP) (Optical Society of America, Washington, DC), p. NTh2A.3.  
Titulaer, U. M., and R. J. Glauber, 1966, “Density operators for coherent fields,” Phys. Rev. 145, 1041–1050.  
Tong, Limin, Rafael R. Gattass, Jonathan B. Ashcom, Sailing He, Jingyi Lou, Mengyan Shen, Iva Maxwell, and Eric Mazur, 2003, "Subwavelength-diameter silica wires for low-loss optical wave guiding," Nature (London) 426, 816.  
Toscano, F., A. Saboia, A. Avelar, and S. Walborn, 2015, "Systematic construction of genuine-multipartite-entanglement criteria in continuous-variable systems using uncertainty relations," Phys. Rev. A 92, 052316.  
TrepS, N., U. Andersen, B. Buchler, P. Lam, A. Maitre, H. A. Bacher, and C. Fabre, 2002, "Surpassing the Standard Quantum Limit for Optical Imaging Using Nonclassical Multimode Light," Phys. Rev. Lett. 88, 203601.  
TrepS, N., V. Delaubert, A. Maitre, J. M. Courty, and C. Fabre, 2005, "Quantum noise in multipixel image processing," Phys. Rev. A 71, 013820.  
Trep, N., and C. Fabre, 2000, "Transverse distribution of quantum fluctuations and correlations in spatial solitons," Phys. Rev. A 62, 033816.  
Trep, Nicolas, Nicolai Grosse, Warwick P. Bowen, Claude Fabre, Hans-A. Bachor, and Ping Koy Lam, 2003, “A quantum laser pointer,” Science 301, 940-943.  
Tsang, Mankei, 2017, "Subdiffraction incoherent optical imaging via spatial-mode demultiplexing," New J. Phys. 19, 023054.  
Tsang, Mankei, Ranjith Nair, and Xiao-Ming Lu, 2016, "Quantum Theory of Superresolution for Two Incoherent Optical Point Sources," Phys. Rev. X 6, 031033.  
Ukai, Ryuji, Noriaki Iwata, Yuji Shimokawa, Seiji C. Armstrong, Alberto Politi, Jun-ichi Yoshikawa, Peter van Loock, and Akira Furusawa, 2011, "Demonstration of Unconditional One-Way Quantum Computations for Continuous Variables," Phys. Rev. Lett. 106, 240504.  
Vahlbruch, Henning, Moritz Mehmet, Karsten Danzmann, and Roman Schnabel, 2016, "Detection of 15 db Squeezed States of Light and Their Application for the Absolute Calibration of Photoelectric Quantum Efficiency," Phys. Rev. Lett. 117, 110801.  
Valido, Antonio A., Federico Levi, and Florian Mintert, 2014, "Hierarchies of multipartite entanglement for continuous-variable states," Phys. Rev. A 90, 052321.  
Vallone, Giuseppe, Gianfranco Cariolaro, and Gianfranco Pierobon, 2019, "Means and covariances of photon numbers in multimode Gaussian states," Phys. Rev. A 99, 023817.

van Loock, P., and Samuel L. Braunstein, 2000, "Multipartite Entanglement for Continuous Variables: A Quantum Teleportation Network," Phys. Rev. Lett. 84, 3482-3485.  
van Loock, Peter, and Akira Furusawa, 2003, "Detecting genuine multipartite continuous-variable entanglement," Phys. Rev. A 67, 052315.  
van Loock, Peter, Christian Weedbrook, and Mile Gu, 2007, "Building Gaussian cluster states by linear optics," Phys. Rev. A 76, 032321.  
Villar, A. S., M. Martinelli, C. Fabre, and P. Nussenzweig, 2006, "Direct Production of Tripartite Pump-Signal-Idler Entanglement in the Above-Threshold Optical Parametric Oscillator," Phys. Rev. Lett. 97, 140504.  
Vogel, Werner, 2000, “Nonclassical States: An Observable Criterion,” Phys. Rev. Lett. 84, 1849–1852.  
Walborn, Stephen P., C.H. Monken, S. Pádua, and P.H. Souto Ribeiro, 2010, "Spatial correlations in parametric downconversion," Phys. Rep. 495, 87-139.  
Walschaers, Mattia, Claude Fabre, Valentina Parigi, and Nicolas Treps, 2017a, "Entanglement and Wigner Function Negativity of Multimode Non-Gaussian States," Phys. Rev. Lett. 119, 183601.  
Walschaers, Mattia, Claude Fabre, Valentina Parigi, and Nicolas Treps, 2017b, "Statistical signatures of multimode single-photon-added and -subtracted states of light," Phys. Rev. A 96, 053835.  
Walschaers, Mattia, Supratik Sarkar, Valentina Parigi, and Nicolas Treps, 2018, "Tailoring Non-Gaussian Continuous-Variable Graph States," Phys. Rev. Lett. 121, 220501.  
Wang, Hailong, Claude Fabre, and Jietai Jing, 2017, "Single-step fabrication of scalable multimode quantum resources using four-wave mixing with a spatially structured pump," Phys. Rev. A 95, 051802.  
Wang, Hui, Shensheng Han, and Mikhail I. Kolobov, 2012, "Quantum limits of super-resolution of optical sparse objects via sparsity constraint," Opt. Express 20, 23235-23252.  
Wasilewski, Wojciech, A. Lvovsky, Konrad Banaszek, and Czesław Radzewicz, 2006, “Pulsed squeezed light: Simultaneous squeezing of multiple modes,” Phys. Rev. A 73, 063819.  
Weedbrook, Christian, Stefano Pirandola, Raul Garcia-Patrón, Nicolas J. Cerf, Timothy C. Ralph, Jeffrey H. Shapiro, and Seth Lloyd, 2012, "Gaussian quantum information," Rev. Mod. Phys. 84, 621-669.  
Weigand, Daniel J., and Barbara M. Terhal, 2018, "Generating grid states from Schrödinger-cat states without postselection," Phys. Rev. A 97, 022341.  
Weiner, Andrew M., 2011, "Ultrafast optical pulse shaping: A tutorial review," Opt. Commun. 284, 3669-3692.  
Wenger, Jérôme, Rosa Tuelle-Brouuri, and Philippe Grangier, 2004, "Non-Gaussian Statistics from Individual Pulses of Squeezed Light," Phys. Rev. Lett. 92, 153601.  
Werner, Reinhard F., and Michael M. Wolf, 2001, "Bound Entangled Gaussian States," Phys. Rev. Lett. 86, 3658.  
Werner, Reinhard, F., 1989, “Quantum states with Einstein-Podolsky-Rosen correlations admitting a hidden-variable model,” Phys. Rev. A 40, 4277.  
Wiener, N., 1928, “Coherency matrices and quantum theory,” J. Math. Phys. (Cambridge, Mass.) 7, 109.  
Winzer, Peter J., and Gerard J. Foschini, 2011, "MIMO capacities and outage probabilities in spatially multiplexed optical transport systems," Opt. Express 19, 16680-16696.  
Wiseman, Howard M., and Gerard J. Milburn, 2009, Quantum Measurement and Control (Cambridge University Press, Cambridge, England).

Xiang, Yu, Ioannis Kogias, Gerardo Adesso, and Qiongyi He, 2017, "Multipartite Gaussian steering: Monogamy constraints and quantum cryptography applications," Phys. Rev. A 95, 010101.  
Xiao, Zhihao, R. Nicholas Lanning, Mi Zhang, Irina Novikova, Eugeniy E. Mikhailov, and Jonathan P. Dowling, 2017, "Why a hole is like a beam splitter: A general diffraction theory for multimode quantum states of light," Phys. Rev. A 96, 023829.  
Yamazoe, Kenji, 2012, "Coherency matrix formulation for partially coherent imaging to evaluate the degree of coherence for image," J. Opt. Soc. Am. A 29, 1529-1536.  
Yang, Fan, Ranjith Nair, Mankei Tsang, Christoph Simon, and Alexander I. Lvovsky, 2017, "Fisher information for far-field linear optical superresolution via homodyne or heterodyne detection in a higher-order local oscillator mode," Phys. Rev. A 96, 063829.  
Yokoyama, Shota, Ryuji Ukai, Seiji C. Armstrong, Chanond Sornphiphatphong, Toshiyuki Kaji, Shigenari Suzuki, Jun-ichi Yoshikawa, Hidehiro Yonezawa, Nicolas C. Menicucci, and Akira Furusawa, 2013, "Optical generation of ultra-large-scale continuous-variable cluster states," Nat. Photonics 7, 982.  
Yu, Zhixian, and Sudhakar Prasad, 2018, "Quantum Limited Superresolution of an Incoherent Source Pair in Three Dimensions," Phys. Rev. Lett. 121, 180504.

Yukawa, Mitsuyoshi, Ryuji Ukai, Peter van Loock, and Akira Furusawa, 2008, "Experimental generation of four-mode continuous-variable cluster states," Phys. Rev. A 78, 012301.  
Zavatta, Alessandro, Silvia Viciani, and Marco Bellini, 2004, "Quantum-to-classical transition with single-photon-added coherent states of light," Science 306, 660-662.  
Zhang, Da, Changbiao Li, Zhaoyang Zhang, Yiqi Zhang, Yanpeng Zhang, and Min Xiao, 2017, "Enhanced intensity-difference squeezing via energy-level modulations in hot atomic media," Phys. Rev. A 96, 043847.  
Zhang, Jing, and Samuel L. Braunstein, 2006, "Continuous-variable Gaussian analog of cluster states," Phys. Rev. A 73, 032318.  
Zhou, Yiyu, Mohammad Mirhosseini, Dongzhi Fu, Jiapeng Zhao, Seyed Mohammad Hashemi Rafsanjani, Alan E. Willner, and Robert W. Boyd, 2017, "Sorting Photons by Radial Quantum Number," Phys. Rev. Lett. 119, 263602.  
Zhou, Yiyu, Jing Yang, Jeremy D. Hassett, Seyed Mohammad Hashemi Rafsanjani, Mohammad Mirhosseini, A. Nick Vamivakas, Andrew N. Jordan, Zhimin Shi, and Robert W. Boyd, 2019, "Quantum-limited estimation of the axial separation of two incoherent point sources," Optica 6, 534-541.  
Zhou, Yiyu, Jiapeng Zhao, Zhimin Shi, Seyed Mohammad Hashemi Rafsanjani, Mohammad Mirhosseini, Ziyi Zhu, Alan E. Willner, and Robert W. Boyd, 2018, "Hermite-Gaussian mode sorter," Opt. Lett. 43, 5263-5266.