# Topological photonics

Tomoki Ozawa

Interdisciplinary Theoretical and Mathematical Sciences Program (iTHEMS), RIKEN, Wako, Saitama 351-0198, Japan, Center for Nonlinear Phenomena and Complex Systems, Universite Libre de Bruxelles, CP 231, Campus Plaine, B-1050 Brussels, Belgium, and INO-CNR BEC Center and Dipartimento di Fisica, Universita di Trento, I-38123 Povo, Italy

Hannah M. Price

School of Physics and Astronomy, University of Birmingham, Edgbaston, Birmingham B15 2TT, United Kingdom and INO-CNR BEC Center and Dipartimento di Fisica, Università di Trento, I-38123 Povo, Italy

Alberto Amo

Université de Lille, CNRS, UMR 8523—PhLAM—Laboratoire de Physique des Lasers Atomes et Molécules, F-59000 Lille, France

Nathan Goldman

Center for Nonlinear Phenomena and Complex Systems, Université Libre de Bruxelles, CP 231, Campus Plaine, B-1050 Brussels, Belgium

Mohammad Hafezi

Joint Quantum Institute, Institute for Research in Electronics and Applied Physics, Department of Electrical and Computer Engineering, Department of Physics, University of Maryland, College Park, Maryland 20742, USA

Ling Lu

Institute of Physics, Chinese Academy of Sciences/Beijing National Laboratory for Condensed Matter Physics, Beijing 100190, China and Songshan Lake Materials Laboratory, Dongguan, Guangdong 523808, China

Mikael C. Rechtsman

Department of Physics, The Pennsylvania State University, University Park, Pennsylvania 16802, USA

David Schuster

The James Franck Institute and Department of Physics, University of Chicago, Chicago, Illinois 60637, USA

Jonathan Simon

The James Franck Institute and Department of Physics, University of Chicago, Chicago, Illinois 60637, USA

Oded Zilberberg

Institute for Theoretical Physics, ETH Zurich, 8093 Zurich, Switzerland

Iacopo Carusotto

INO-CNR BEC Center and Dipartimento di Fisica, Università di Trento, I-38123 Povo, Italy

![](images/a3afeaafc0e5ee73b02d417620bc6236e2babf5a0df32d6019a7d487cb524761.jpg)

(published 25 March 2019)

Topological photonics is a rapidly emerging field of research in which geometrical and topological ideas are exploited to design and control the behavior of light. Drawing inspiration from the discovery of the quantum Hall effects and topological insulators in condensed matter, recent advances have shown how to engineer analogous effects also for photons, leading to remarkable phenomena such as the robust unidirectional propagation of light, which hold great promise for applications. Thanks to the flexibility and diversity of photonics systems, this field is also opening up new opportunities to realize exotic topological models and to probe and exploit topological effects in new ways. This article reviews experimental and theoretical developments in topological photonics across a wide range of experimental platforms, including photonic crystals, waveguides, metamaterials, cavities, optomechanics, silicon photonics, and circuit QED. A discussion of how changing the dimensionality and symmetries of photonics systems has allowed for the realization of different topological phases is offered, and progress in understanding the interplay of topology with non-Hermitian effects, such as dissipation, is reviewed. As an exciting perspective, topological photonics can be combined with optical nonlinearities, leading toward new collective phenomena and novel strongly correlated states of light, such as an analog of the fractional quantum Hall effect.

DOI: 10.1103/RevModPhys.91.015006

# CONTENTS

I. Introduction 2  
II. Basic Concepts 5

A. Topological phases of matter 5

1. Integer quantum Hall effect 5  
2.Quantum spin Hall system 9  
3.Topological phases in other dimensions 10  
4.Topological pumping 12  
5. Floquet engineering: Topology through time-periodic modulations 14

B. Features of photonic systems 16

1.Bosonic nature 16  
2. Nonequilibrium nature 16

a. Coherent pumping 17  
b.Incoherent pumping 19  
c. Propagating geometries 19

3. Basics of nonlinear optics 20

III. Topological Photonics in Two Dimensions 22

A. Analog quantum Hall systems in photonics 22

1. Gyromagnetic photonic crystals 23  
2. Propagating geometries 24  
3. Optomechanics 27  
4. Cavity- and circuit-QED systems 27

5. Other proposals 28

a.Topolaritons 28  
b. Dynamical modulation 28

B. Analog quantum spin Hall systems in photonics 29

1. Silicon ring resonator arrays 29  
2.Topologicalrfcircuits 32  
3. Twisted optical resonators 34  
4. Intrinsic spin-orbit interactions for light 36  
5.Bianisotropic metamaterials 36  
6. Photonic structures with crystalline symmetries 37  
7. Other proposals 38

C.Anomalous Floquet topological insulators 39  
topology in gapless photonic systems 40

IV. Topological Photonics in One Dimension 44

A.Topology in 1D chiral systems 44  
B.Topological pumps 45

V. Topological Photonics in Higher Dimensions 46

A. Three-dimensional gapless phases 46

1. Weyl points and helicoid surface states 46  
2. Multi-Weyl and Dirac points 47

3. Nodal lines and surface 47

B. Three-dimensional gapped phases 48

1. 3D Chern crystal 48  
2. One-way fiber 48  
3. Single surface Dirac cone 48  
4. Nonmagnetic designs 49

C. Toward even higher dimensions 49

1. Synthetic dimensions 49  
2. Four-dimensional quantum Hall effect 50

VI. Gain and Loss in Topological Photonics 50

A.Non-Hermitian topological photonics 50  
B. Emergent topology of Bogoliubov modes 51

VII. Topological Effects for Interacting Photons 52

Weak nonlinearities 52  
B. Strong nonlinearities 53

VIII. Conclusion and Perspectives 55

A. Optical isolation and robust transport 55  
B.Quantum emitters and topological laser 56

1.Topological lasers:Theory 56  
2.Topological lasers:Experiments 56

C. Measurement of bulk topological and geometrical properties 57  
D.Topological quantum computing 58

Acknowledgments 58  
References 58

# I. INTRODUCTION

Over the last decade, topological photonics appeared as a rapidly growing field of study. This field aims to explore the physics of topological phases of matter, originally discovered in solid-state electron systems, in a novel optical context. In this review, we attempt to cover the main achievements of topological photonics, beginning from the basic concepts of topological phases of matter and photonics, so that readers can follow our discussion independently of their background.

Topological photonics is rooted in ideas that were first developed to understand topological phases of matter in solid-state physics. This field of research began with the discovery of the integer quantum Hall effect in 1980 (Klitzing, Dorda, and Pepper, 1980; von Klitzing, 1986). In this effect, a two-dimensional electron gas in the presence of a strong perpendicular magnetic field was found to exhibit robust

plateaus in the Hall conductance as a function of the magnetic field at values equal to integer multiples of the fundamental constant  $e^2 / h$ . The far-reaching conceptual consequences of this integer quantum Hall effect were soon highlighted by Thouless et al. (1982) and Kohmoto (1985). These works related the integer appearing in the Hall conductance to a topological invariant of the system, the Chern number, that is an integer-valued quantity which describes the global structure of the wave function in momentum space over the Brillouin zone.

An important insight into the physical meaning of the topological invariant is given by the bulk-edge correspondence (Jackiw and Rebbi, 1976; Hatsugai, 1993a, 1993b; Qi, Wu, and Zhang, 2006): when two materials with different topological invariants are put in contact, there must exist edge states that are spatially localized at the interface at energies that lie within the energy gap of the surrounding bulk materials.

The bulk-edge correspondence can be heuristically understood in the following way: an integer topological invariant of a gapped system cannot change its value under perturbations or deformations of the system, unless the energy gap to excited states is somewhere closed. This implies that when two materials with different topological invariants are put in contact, the energy gap must close somewhere in the interface region, which leads to the appearance in this region of localized states. In a finite-size sample of a topologically nontrivial material, the physical edge of the sample can be considered as an interface between a region with a nonzero topological invariant and the topologically trivial vacuum, guaranteeing the existence of localized states at the system boundary.

In the quantum Hall effect, these edge modes display chiral properties, in the sense that they can propagate only in one direction along the sample boundary but not in the opposite direction. The number of such chiral edge modes that are available at the Fermi energy for electric conduction is proportional to the Hall conductance. Because of the unidirectional nature of the edge states, the edge currents are immune to backscattering, resulting in the precise and robust quantization of the measured Hall conductance (Halperin, 1982; MacDonald and Streda, 1984; Buttiker, 1988).

Interest in the topological physics of electronic systems surged further when a different class of topological phases of matter, now known as the quantum spin Hall systems or  $\mathbb{Z}_2$  topological insulators, was discovered in 2005 (Kane and Mele, 2005a, 2005b; Bernevig, Hughes, and Zhang, 2006; Bernevig and Zhang, 2006; Konig et al., 2007). In these systems, the Chern number is zero but the wave function is characterized by a binary  $(\mathbb{Z}_2)$  topological invariant that can be nonzero and robust in the presence of time-reversal symmetry. Since then, there has been intense investigation in condensed-matter physics into what different topological phases of matter are possible under various symmetries, and what are the physical consequences of this physics (Hasan and Kane, 2010; Qi and Zhang, 2011; Bernevig and Hughes, 2013; Chiu et al., 2016). Besides electronic systems in solid-state materials, topological phases of matter are also being actively studied in other quantum many-body systems, in

particular, liquid helium (Volovik, 2009) and ultracold atomic gases (Cooper, 2008; Dalibard et al., 2011; Goldman et al., 2014; Goldman, Budich, and Zoller, 2016).

Parallel to the growth in the study of topological phases of matter in condensed-matter systems, Haldane and Raghu made the crucial observation that topological band structures are, in fact, a ubiquitous property of waves inside a periodic medium, regardless of the classical or quantum nature of the waves. In their seminal works (Haldane and Raghu, 2008; Raghu and Haldane, 2008), they considered electromagnetic waves in two-dimensional spatially periodic devices embedding time-reversal-breaking magneto-optical elements and showed that the resulting photonic bands would have nontrivial topological invariants. Consequently, they predicted that such photonic systems would support robust chiral states propagating along the edge of the system at frequencies inside the photonic band gap.

Shortly afterward, following a realistic proposal from Wang et al. (2008), the idea of Haldane and Raghu was experimentally implemented using the two-dimensional magneto-optical photonic crystal structure in the microwave domain sketched in Figs. 1(a1) and 1(a2) (Wang et al., 2009): a clear signature of the nontrivial band topology was indeed found in the unidirectionally propagating edge states and in the corresponding nonreciprocal behavior, as illustrated in the simulations of Figs. 1(b) and in the experimental data of Figs. 1(c) and 1(d). More details on this and related following experiments are given in Sec. III.A.

Further progress toward the implementation of such a model in the optical domain and the exploration of other topological models remained however elusive. One major challenge was the absence of a large magneto-optical response in the optical domain. One way to overcome this difficulty is to consider internal degrees of freedom of photons as pseudospins and look for an analogy of quantum spin Hall systems, namely, where the overall time-reversal symmetry is not broken but each pseudospin feels an artificial magnetic field (Hafezi et al., 2011; Umucalilar and Carusotto, 2011; Khanikaev et al., 2013). A second way is to use ideas from the Floquet topological insulators (Oka and Aoki, 2009; Kitagawa, Berg et al., 2010; Lindner, Refael, and Galitski, 2011) known in condensed-matter physics, where temporal modulation is applied to the system to generate an effective time-independent Hamiltonian which breaks time-reversal symmetry (Fang, Yu, and Fan, 2012b). A third way is to employ time-dependent modulation to implement a "topological pump" (Thouless, 1983); this last approach was realized experimentally in photonics in 2012 (Kraus et al., 2012), while the previous two ideas were realized in 2013 by two concurrent experiments (Hafezi et al., 2013; Rechtsman, Zeuner, Plotnik et al., 2013).

Since then there has been great activity in the study of a variety of photonic systems realizing band structures with nontrivial topological invariants, leading to the emerging research field of topological photonics (Lu, Joannopoulos, and Soljacic, 2014, 2016; Khanikaev and Shvets, 2017; X.-C. Sun et al., 2017). Along similar lines, intense theoretical and experimental work has also been devoted to related topological effects in other areas of classical physics, such as in mechanical and acoustic systems. Reviews of the advances of

![](images/48929b7c480bf7d7168d7ff671d6d2fc9cef81f2f26e5d7fd2f1d7b66a5c7e1e.jpg)

![](images/a4f583d825e9087c93607d098cad8825c0d18f2ca37eb75ce4c12e1641725838.jpg)

![](images/c4e25ca6275164ff6a09cbce7dd2bf14f7daaf92212f2f455622c20ae76dbc07.jpg)

![](images/575aee3b3d772bdab4c4bb4e5a73a17e46beb249d1435f04c74313fb4932b5d1.jpg)

![](images/800eac424fdd7fb544bd91104a03ff25e93a392fa318ff3fa25a4f06edb5d331.jpg)  
FIG. 1. (a1) Sketch of the gyromagnetic photonic crystal slab used in the experiments of Wang et al. (2009). The blue dots indicate the ferrite rods which are organized in a two-dimensional square lattice along the  $x - y$  plane and are subject to a magnetic field of  $0.2\mathrm{T}$ . The structure is sandwiched between two parallel copper plates providing confinement along  $z$ . The chiral edge state is located at the boundary of the photonic crystal next to the metal wall. Two dipole antennas A and B serve as feeds and/or probes. Backscattering is investigated by inserting a variable-length metal obstacle between the antennas. (a2) A top view photograph of the actual waveguide with the top plate removed. (b) Theoretical calculations of light propagation on edge states: (b1), (b3) unidirectional, nonreciprocal propagation from antennas A and B, respectively. (b2) The immunity to backscattering against a defect. (c) Reciprocal transmission when the two antennas are located in the bulk. (d) Nonreciprocal transmission via the chiral edge state. Blue and red curves refer to transmission from antenna A to antenna B and vice versa. (e) Projected dispersion of the allowed photonic bands in the bulk (blue and gray) and the chiral edge state (red). The white numbers indicate the Chern number of each band. Adapted from Wang et al., 2009.

![](images/24f4465f53d33557f1d361aa1dcbf479bab3fc86ea1e1873d8427a6661b3e5a7.jpg)

these other fields have been given by Fleury et al. (2015) and Huber (2016).

This review is focused on the recent developments in the study of topological phases of matter in the photonics context. As we shall see in the following, in the last decade, topological ideas have successfully permeated the field of photonics, having been applied to a wide range of different material platforms, arranged in lattices of various dimensionalities, and operating in different regions of the electromagnetic spectrum, from radio waves and microwaves up to visible light. One long term goal of topological photonics is to achieve and control strongly correlated states of photons with topological features such as fractional quantum Hall states. In addition to opening up perspectives for exploring the fundamental physics of

topological phases of matter beyond solid-state systems, topological photonics also offers rich potential applications of these concepts to a novel generation of optoelectronic devices, such as optical isolators and topological lasers.

The structure of this review article is the following. In Sec. II.A, we offer a general review of the main geometrical and topological concepts that have been developed in the study of solid-state electronic systems and that are commonly used in topological photonics. The following Sec. II.B gives a general overview of the specific features that characterize photonic systems in contrast to electronic topological insulators.

In Sec. III, we discuss two-dimensional photonic systems which show topological features. This section is divided into four subsections. In Sec. III.A, we discuss two-dimensional photonic structures which break time-reversal symmetry and hence display physics analogous to integer quantum Hall systems. Relevant photonic systems include gyromagnetic photonic crystals, waveguide arrays, optomechanics, cavity QED, and circuit QED. The following Sec. III.B deals with two-dimensional photonic systems which do not break time-reversal symmetry and hence can be considered as analogs of the quantum spin Hall systems. Systems discussed in this section include silicon ring resonator arrays, radio-frequency circuits, twisted optical resonators, and photonic metamaterials. In Sec. III.C, we review photonic realizations of anomalous Floquet topological systems with waveguide arrays, namely, temporally modulated systems displaying topological features that do not have an analog in static Hamiltonians. Section III.D discusses two-dimensional gapless systems such as honeycomb lattices, whose features can also be understood from topological considerations. Systems discussed in this section include microwave resonators, photo refractive crystals, coupled microlasers, exciton-polariton lattices, and waveguide arrays.

Section IV is devoted to photonic realizations of one-dimensional topological systems. In Sec. IV.A we concentrate on systems with chiral symmetry, such as the Su-Schrieffer-Heeger (SSH) model. In Sec. IV.B we review photonic realizations of topological pumping. Systems of higher dimensionality are then considered in Sec. V. Three-dimensional gapless phases with features originating from topological charges in momentum space, such as Weyl points, are discussed in Sec. V.A. In Sec. V.B, we discuss gapped three-dimensional phases and their topological interface states. The following Sec. V.C presents the concept of synthetic dimensions, which could be used to realize models with an effective spatial dimensionality higher than three, e.g., four-dimensional quantum Hall systems.

In Sec. VI, we discuss photonic systems where gain and loss play an essential role. Such systems are described by non-Hermitian Hamiltonians and do not find a direct counterpart in electronic topological insulators. Section VI.A focuses on the interplay of gain and loss, while the following Sec. VI.B reviews the emergent topology of Bogoliubov modes that arises from parametric down conversion processes.

Section VII is devoted to an overview of the interplay between topology and optical nonlinearities. Theoretical work on nonlinear effects stemming from weak nonlinearities is reviewed in Sec. VII.A, while the following Sec. VII.B highlights the prospect of strong photon-photon interactions

mediated by strong nonlinearities to realize topologically nontrivial strongly correlated states of photons. Some of the future perspectives of the field of topological photonics are finally illustrated in Sec. VIII.

Compared to earlier reviews on topological photonics (Lu, Joannopoulos, and Soljacic, 2014, 2016; Khanikaev and Shvets, 2017; X.-C. Sun et al., 2017), this review aims to be comprehensive, starting from the very basics of topological phases of matter and trying to cover most of the works that have appeared in the last years in relation to topological phases of matter in optical systems in any dimensionality. However, we need to warn the readers that space restrictions force us to leave out many other fields of the optical sciences that relate to topological concepts, e.g., the rich dynamics of optical vortices in singular optics (Dennis, O'Holleran, and Padgett, 2009; Gbur, 2016), the topology underlying knots in complex electromagnetic fields (Arrayas, Bouwmeester, and Trueba, 2017), and the topological ideas underlying bound states in the continuum (Hsu et al., 2016). For all these advances, we refer the readers to the rich specific literature that is available on each of them.

# II. BASIC CONCEPTS

In this section, we introduce general concepts of topological phases of matter and optical and photonic systems that are needed in the following sections. In Sec. II.A, we briefly review the paradigm of topological phases of matter, as it was originally developed in the context of electronic systems in solid-state materials, and illustrate the basic technical and mathematical tools to describe them. Then in Sec. II.B, we review the principal features of photonic systems used for topological photonics, with a special emphasis on their differences and peculiarities as compared to electronic systems.

# A. Topological phases of matter

According to Bloch's theorem, the eigenstates of a quantum particle in a periodic potential are organized into energy bands separated by energy gaps. This band structure determines the metallic or insulating nature of different solid-state materials (Ashcroft and Mermin, 1976). Besides the energy dispersion of the bands, the geometrical structure of the Bloch eigenstates in momentum space can also have an impact on the electronic properties of materials as first discovered by Karplus and Luttinger (1954) and Adams and Blount (1959). This geometrical structure is reflected also in integer-valued global topological invariants associated with each band, as we see later. In spite of their seemingly abstract nature (Simon, 1983), nontrivial values of these topological invariants have observable consequences such as the quantized bulk conductance in the quantum Hall effect and in the emergence of topologically protected edge states located on the physical boundary of the system (Volovik, 2009; Hasan and Kane, 2010; Qi and Zhang, 2011; Bernevig and Hughes, 2013).

This section is devoted to an introduction to the basic concepts of such topological phases of matter.

# 1. Integer quantum Hall effect

The quantum Hall effect is historically the first phenomenon where momentum-space topology was recognized to lead to observable physical phenomena. The integer quantum Hall effect was discovered in a two-dimensional electron gas subject to a strong perpendicular magnetic field by Klitzing, Dorda, and Pepper (1980), who observed a robust quantization of the Hall conductance in units of  $e^2 / h$ , where  $e$  is the charge of an electron and  $h$  is Planck's constant. Soon after, the extremely robust quantization of the Hall conductance was related to the topology of bands in momentum space by Thouless, Kohmoto, Nightingale, and den Nijs (TKNN) (Thouless et al., 1982).

In order to review this landmark result, we first need to introduce the basic geometrical and topological properties of eigenstates in momentum space, such as the local Berry connection and Berry curvature and the global Chern number, respectively. We consider a single-particle Hamiltonian  $\hat{H} (\hat{\mathbf{r}},\hat{\mathbf{p}})$  in generic dimension  $d$  , where  $\hat{\mathbf{r}}$  and  $\hat{\mathbf{p}}$  are, respectively, the position and momentum operators. We assume that the Hamiltonian obeys the spatial periodicity condition  $\hat{H} (\hat{\mathbf{r}} +\mathbf{a}_i,\hat{\mathbf{p}}) = \hat{H} (\hat{\mathbf{r}},\hat{\mathbf{p}})$  , where  $\{\mathbf{a}_i\}$  are a set of  $^d$  lattice vectors. Thanks to the spatial periodicity, one can invoke Bloch's theorem to write the eigenstates as

$$
\psi_ {n, \mathbf {k}} (\mathbf {r}) = e ^ {i \mathbf {k} \cdot \mathbf {r}} u _ {n, \mathbf {k}} (\mathbf {r}), \tag {1}
$$

where  $n$  is the band index and  $\mathbf{k}$  is the crystal momentum defined within the first Brillouin zone. The Bloch state  $u_{n,\mathbf{k}}(\mathbf{r})$  obeys the same periodicity as the original Hamiltonian  $u_{n,\mathbf{k}}(\mathbf{r} + \mathbf{a}_i) = u_{n,\mathbf{k}}(\mathbf{r})$  and is an eigenstate of the Bloch Hamiltonian

$$
\hat {H} _ {\mathbf {k}} \equiv e ^ {- i \mathbf {k} \cdot \hat {\mathbf {r}}} \hat {H} (\hat {\mathbf {r}}, \hat {\mathbf {p}}) e ^ {i \mathbf {k} \cdot \hat {\mathbf {r}}}, \tag {2}
$$

namely,

$$
\hat {H} _ {\mathbf {k}} u _ {n, \mathbf {k}} (\mathbf {r}) = E _ {n} (\mathbf {k}) u _ {n, \mathbf {k}} (\mathbf {r}), \tag {3}
$$

where  $E_{n}(\mathbf{k})$  is the energy dispersion of the nth band (Ashcroft and Mermin, 1976).

The physics of an energy band is captured in part by its dispersion relation  $E_{n}(\mathbf{k})$ , but also by the geometrical properties of how its eigenstates  $u_{n,\mathbf{k}}(\mathbf{r})$  vary as a function of  $\mathbf{k}$  (Karplus and Luttinger, 1954; Adams and Blount, 1959; Resta, 1994, 2011; Nagaosa et al., 2010). This geometry of the eigenstates is encoded by the Berry phase (Pancharatnam, 1956; Berry, 1984; Hannay, 1985), which is defined in the following. Whereas the Berry phase can be defined for a very general parameter space, in our discussion of topological phases of matter we restrict ourselves to the case where the parameters are the crystal momentum  $\mathbf{k} = (k_x, k_y, k_z)$  varying over the first Brillouin zone. Then if one prepares a localized wave packet from states in band  $n$  and makes it adiabatically move along a closed path in momentum space, it will acquire a dynamical phase, determined by the time integral of its  $\mathbf{k}$ -dependent energy, but also a Berry phase (Xiao, Chang, and Niu, 2010)

$$
\gamma = \oint \mathcal {A} _ {n} (\mathbf {k}) \cdot d \mathbf {k}, \tag {4}
$$

that is geometrically determined by an integral over the same momentum-space path, of the Berry connection, defined as

$$
\mathcal {A} _ {n} (\mathbf {k}) \equiv i \langle u _ {n, \mathbf {k}} | \boldsymbol {\nabla} _ {\mathbf {k}} | u _ {n, \mathbf {k}} \rangle . \tag {5}
$$

Note that the definition of the Bloch states via Eq. (3) does not specify the overall phase of  $|u_{n,\mathbf{k}}\rangle$ , so one can freely choose the phase of the Bloch states. Under a gauge transformation  $|u_{n,\mathbf{k}}\rangle \rightarrow e^{i\chi (\mathbf{k})}|u_{n,\mathbf{k}}\rangle$ , the Berry connection is not gauge invariant and transforms as  $\mathcal{A}_n(\mathbf{k})\to \mathcal{A}_n(\mathbf{k}) - \nabla_{\mathbf{k}}\chi (\mathbf{k})$ . However, the single valuedness of  $e^{i\chi (\mathbf{k})}$  at the beginning and end of the path imposes that the Berry phase (4) for a given closed path is gauge invariant modulo  $2\pi$ . Additionally, from the gauge-dependent Berry connection  $\mathcal{A}_n(\mathbf{k})$  one can construct a gauge invariant Berry curvature, which in three dimensions takes the following form:

$$
\boldsymbol {\Omega} _ {n} (\mathbf {k}) = \boldsymbol {\nabla} _ {\mathbf {k}} \times \boldsymbol {\mathcal {A}} _ {n} (\mathbf {k}), \tag {6}
$$

and which encodes the geometrical properties of the  $n$ th band. In two dimensions, the Berry curvature has only one component:

$$
\Omega_ {n} (\mathbf {k}) = i \left(\left\langle \partial_ {k _ {x}} u _ {n, \mathbf {k}} \mid \partial_ {k _ {y}} u _ {n, \mathbf {k}} \right\rangle - \left\langle \partial_ {k _ {y}} u _ {n, \mathbf {k}} \mid \partial_ {k _ {x}} u _ {n, \mathbf {k}} \right\rangle\right). \tag {7}
$$

Importantly, although the Berry curvature is a gauge invariant quantity that is continuously defined over the whole Brillouin zone, the phase of the Bloch states themselves cannot always be chosen to be continuous. Whether this is possible or not depends on the value of a topological invariant of the band, the Chern number, defined as the integral

$$
C _ {n} = \frac {1}{2 \pi} \int_ {\mathrm {B Z}} d ^ {2} k \Omega_ {n} \left(k _ {x}, k _ {y}\right), \tag {8}
$$

over the whole first Brillouin zone. If one can define the phase of the Bloch state, and hence the Berry connection  $\mathcal{A}_n(\mathbf{k})$ , continuously over the whole Brillouin zone, a direct consequence of the definition  $\Omega_n(\mathbf{k}) = \nabla_{\mathbf{k}} \times \mathcal{A}_n(\mathbf{k})$  and of Stokes's theorem is that the Chern number must necessarily be zero. Conversely, having a nonzero Chern number implies that the Bloch state and hence the Berry connection  $\mathcal{A}_n(\mathbf{k})$  cannot be continuously defined.

It is not difficult to see that the Chern number always takes an integer value (Kohmoto, 1985). To this purpose, we divide the integration domain of Eq. (8) into two regions  $S$  and  $S'$  as sketched in Fig. 2. Within  $S$ , we choose a continuous gauge for the Bloch state, giving the Berry connection  $\mathcal{A}_n(\mathbf{k})$ . Similarly, within  $S'$ , we choose a continuous gauge, which yields the Berry connection  $\mathcal{A}_n'(\mathbf{k})$ . Keeping in mind that the first Brillouin zone can be thought of as a torus, thanks to the periodicity of the quasimomentum, we can use Stokes's theorem within  $S$  and  $S'$  and rewrite the Chern number in terms of the line integral along the common boundary  $\partial S = -\partial S'$ ,

![](images/05e6a5943be6bd89405c25806f8c29c153131935736c4309a962ba017bbd2a91.jpg)  
FIG. 2. A schematic illustration of how the Brillouin zone is divided into two parts,  $S$  and  $S'$ . Thanks to the periodicity of the quasimomentum, the two-dimensional Brillouin zone has a toruslike structure, in which top-bottom and left-right edges (purple and red) should be identified.

$$
\begin{array}{l} C _ {n} = \frac {1}{2 \pi} \int_ {S} d ^ {2} k \Omega_ {n} \left(k _ {x}, k _ {y}\right) + \frac {1}{2 \pi} \int_ {S ^ {\prime}} d ^ {2} k \Omega_ {n} \left(k _ {x}, k _ {y}\right) \\ = \frac {1}{2 \pi} \oint_ {\partial S} d \mathbf {r} \cdot \boldsymbol {A} _ {n} (\mathbf {k}) - \frac {1}{2 \pi} \oint_ {\partial S} d \mathbf {r} \cdot \boldsymbol {A} _ {n} ^ {\prime} (\mathbf {k}) \\ = \frac {1}{2 \pi} \left(\gamma - \gamma^ {\prime}\right), \tag {9} \\ \end{array}
$$

where  $\gamma$  and  $\gamma'$  are the Berry phases along the contour  $\partial S$  calculated using  $\mathcal{A}_n(\mathbf{k})$  and  $\mathcal{A}_n(\mathbf{k})'$ , respectively. As the Berry phases are calculated along the same path, they must be equal up to multiples of  $2\pi$ . This in turn implies that the Chern number  $C_n$  must be an integer. Importantly, this integer-valued quantity has a profound topological origin (Avron, Seiler, and Simon, 1983; Simon, 1983; Niu, Thouless, and Wu, 1985), which indicates that its value must remain strictly constant under smooth perturbations that preserve the band gaps separating the band  $n$  to neighboring bands (Avron, Seiler, and Simon, 1983). Fermionic systems in which the fermions completely fill Bloch bands with nonzero Chern numbers are generically termed Chern insulators.

Within linear response theory and ignoring interparticle interactions, one can show that the Hall conductance  $\sigma_{xy}$  of a two-dimensional insulator is (Thouless et al., 1982)

$$
\sigma_ {x y} = - \frac {e ^ {2}}{h} \sum_ {n} C _ {n}, \tag {10}
$$

where the Chern numbers are summed over the  $n$  occupied bands. Since the Chern numbers can take only integers, it follows that the Hall conductance is quantized in units of  $e^2 /h$ . As we shall see shortly, in the simplest case of a uniform two-dimensional electron gas under a strong magnetic field, the energy levels form flat Landau levels, and all the Landau levels have the same Chern number. Therefore the Hall conductance of the integer quantum Hall effect is proportional to the number of occupied Landau levels.

The quantization of the Hall conductance can also be related to the number of modes that propagate unidirectionally around the system, the so-called chiral edge modes. Indeed, each of such edge modes contributes  $-e^2 /h$  to the measured Hall conductance (Halperin, 1982; MacDonald and Streda, 1984; Böttiker, 1988). The existence of such current-carrying edge modes is also constrained by topology, in the sense that the sum of the Chern numbers associated with the occupied bulk bands is equal to the number of edge modes contributing

to the edge current (Hatsugai, 1993a, 1993b; Qi, Wu, and Zhang, 2006). This relationship between a bulk topological invariant, such as the Chern number, and the number of localized edge modes is an example of the bulk-edge correspondence, i.e., a matching between the topological properties defined in the bulk of a material with its boundary phenomena (Bernevig and Hughes, 2013).

While the previous discussions are based on single-particle energy bands in a perfect crystal, the definition of the Chern number can also be generalized to include the effects of interactions and disorder (Niu, Thouless, and Wu, 1985). When the interparticle interactions become very strong, the Hall conductance can become quantized at fractional values of  $e^2 / h$  (Tsui, Stormer, and Gossard, 1982). This is known as the "fractional quantum Hall effect" in which the quantum many-body ground state is strongly correlated and topological. Remarkably, the excitations of such a fractional quantum Hall state can have a fractional charge and possibly even fractional statistics (Laughlin, 1983; Arovas, Schrieffer, and Wilczek, 1984). Progress toward realizing analog fractional quantum Hall states of light is reviewed in Sec. VII.B.

In the rest of this section, we proceed with a detailed discussion of a few important models for integer quantum Hall systems and Chern insulators. We start by considering a two-dimensional electron gas under a strong and uniform magnetic field, which gives rise to Landau levels and to the integer quantum Hall effect (Prange et al., 1989; Yoshioka, 2002). The second example is the Harper-Hofstadter model that is a tight-binding lattice model in a uniform magnetic field (Harper, 1955b; Azbel, 1964; Hofstadter, 1976). The third one is the Haldane model (Haldane, 1988), which is the first example of a Chern insulator model with alternating magnetic flux patterns. We then conclude by illustrating the bulk-edge correspondence on a simple Jackiw-Rebbi model (Jackiw and Rebbi, 1976).

Landau levels: The quantum Hall effect was originally found in a semiconductor heterojunction where electrons are confined to move in a two-dimensional plane (Klitzing, Dorda, and Pepper, 1980). This system can be modeled, to a first approximation, as a two-dimensional electron gas in free space under a constant magnetic field. The single-particle Hamiltonian is

$$
\hat {H} = \frac {\left[ \hat {p} _ {x} - e A _ {x} (\hat {\mathbf {r}}) \right] ^ {2} + \left[ \hat {p} _ {y} - e A _ {y} (\hat {\mathbf {r}}) \right] ^ {2}}{2 m}, \tag {11}
$$

where  $\mathbf{A}(\mathbf{r}) = (A_x(\mathbf{r}), A_y(\mathbf{r}), 0)$  is the magnetic vector potential, associated with the magnetic field  $\mathbf{B} = \nabla_{\mathbf{r}} \times \mathbf{A}(\mathbf{r})$ .

For a given magnetic field, different forms of the vector potential  $\mathbf{A}(\mathbf{r})$  can be chosen. For our case of a constant magnetic field along the  $z$  direction,  $\mathbf{B} = (0,0,B)$ , the two most common choices are the Landau gauge, which keeps translational symmetry along one direction as  $\mathbf{A}(\mathbf{r}) = (-yB,0,0)$  or  $(0,xB,0)$ , and the symmetric gauge  $\mathbf{A}(\mathbf{r}) = (-yB / 2, xB / 2,0)$ , which keeps instead rotational symmetry. Physical observables such as the energy spectrum and the Hall conductance do not depend on the choice of gauge.

The single-particle energy spectrum of this system consists of equally spaced Landau levels of energy

$$
E _ {n} = \hbar \omega_ {c} (n + 1 / 2), \tag {12}
$$

where  $\omega_{c} \equiv |e|B / m$  is the cyclotron frequency and the integer  $n \geq 0$ . For a large system, each Landau level is highly degenerate with a degeneracy equal to the number of unit magnetic fluxes  $\phi_0 = h / |e|$  piercing the system.

Regarding each Landau level as an energy band, the system can be considered as a Chern insulator when the Fermi energy lies within an energy gap. The Chern number is one for any Landau level. Then, from the TKNN formula (10), the Hall conductance is thus proportional to the number of occupied Landau levels, which explains the basic phenomenology of the integer quantum Hall effect.

Harper-Hofstadter model: The next model we consider is the discrete lattice version of the Landau level problem, the Harper-Hofstadter model (Harper, 1955b; Azbel, 1964; Hofstadter, 1976). In tight-binding models, the magnetic vector potential  $\mathbf{A}(\mathbf{r})$  enters as a nontrivial phase of the hopping amplitude between neighboring sites, called the Peierls phase. In the simplest cases, the phase accumulated when hopping from a site at  $\mathbf{r}_1$  to a site at  $\mathbf{r}_2$  can be written in terms of the vector potential as

$$
\Phi_ {\mathbf {r} _ {1} \rightarrow \mathbf {r} _ {2}} = \frac {e}{\hbar} \int_ {\mathbf {r} _ {1}} ^ {\mathbf {r} _ {2}} \mathbf {A} (\mathbf {r}) \cdot d \mathbf {r}, \tag {13}
$$

where the integral is taken along a straight line connecting the two points (Peierls, 1933; Luttinger, 1951).

Choosing for definiteness the Landau gauge along the  $y$  direction,  $\mathbf{A}(\mathbf{r}) = (0,Bx,0)$ , the Hamiltonian of the Harper-Hofstadter model on a square lattice is

$$
\hat {H} = - J \sum_ {x, y} \left(\hat {a} _ {x + a, y} ^ {\dagger} \hat {a} _ {x, y} + e ^ {i 2 \pi \alpha x / a} \hat {a} _ {x, y + a} ^ {\dagger} \hat {a} _ {x, y} + \mathrm {H . c .}\right), \tag {14}
$$

where  $\hat{a}_{x,y}$  is the annihilation operator of a particle at site  $(x,y)$ ,  $J$  is the magnitude of the (isotropic) hopping amplitude, and  $a$  is the lattice spacing. The intensity of the magnetic field in the system is quantified by the parameter  $\alpha$ , obeying  $\alpha \phi_0 = Ba^2$ , which identifies the magnetic flux per plaquette of the lattice in units of the magnetic flux quantum  $\phi_0$ . The main distinction from the Landau level case previously discussed is that in the Hofstadter model there are two competing length scales: the lattice spacing and the magnetic length. As a result, the electron paths interfere to give the fractal energy spectrum as a function of  $\alpha$ , which is widely known as the Hofstadter butterfly and which is plotted in the left panel of Fig. 3. The first experimental demonstration of the Hofstadter butterfly was performed in a microwave waveguide, exploiting the analogy between the transfer matrix governing the transmission of microwaves and the eigenvalue equation of the Harper-Hofstadter model (Kuhl and Stöckmann, 1998).

To get more insight into this spectrum, it is useful to concentrate on cases where  $\alpha$  is a rational number,  $\alpha = p / q$  with  $p$  and  $q$  being co-prime integers. Because of the spatially varying hopping phase, the Hamiltonian breaks the basic periodicity of the square lattice. Periodicity is, however, recovered if we consider a larger unit cell of  $q\times 1$  plaquettes:

![](images/b29a177c12f1154ab3e1b18cef359a024adbed942ff1b8622c550a88043ebd93.jpg)  
FIG. 3. (Left) Energy spectrum of the Harper-Hofstadter model, which is called the Hofstadter butterfly. (Right) The colored Hofstadter butterfly in which the color of each band gap indicates the topological invariant of the gap, given by the sum of the Chern numbers of all bands below. Warm colors indicate a positive topological invariant, whereas the cool colors indicate a negative topological invariant. The horizontal axes are the energies and the vertical axes are the flux  $\alpha$ .

![](images/42a7e4c6326295efaed0c0331681633060bd7ddc5ce9d60d0e11b0b5532afd95.jpg)

this is called the magnetic unit cell (Zak, 1964; Dana, Avron, and Zak, 1985). As the number of bands in lattice models is equal to the number of lattice sites per magnetic unit cell, the Harper-Hofstadter model with  $\alpha = p / q$  has  $q$  bands.

To find the geometrical and topological properties of the model, one can diagonalize the momentum-space Hamiltonian (Harper, 1955b; Azbel, 1964; Hofstadter, 1976)

$$
\begin{array}{l} \hat {H} _ {\mathbf {k}} = - J \sum_ {i = 0} ^ {q} [ \cos (k _ {y} - 2 \pi \alpha) \hat {a} _ {i} (\mathbf {k}) ^ {\dagger} \hat {a} _ {i} (\mathbf {k}) \\ + e ^ {- i k _ {x}} \hat {a} _ {i + 1} (\mathbf {k}) ^ {\dagger} \hat {a} _ {i} (\mathbf {k}) + \mathrm {H . c .} ], \tag {15} \\ \end{array}
$$

where  $i$ , defined mod  $q$ , indicates the site within a magnetic unit cell, and the momentum  $\mathbf{k}$  is chosen within the magnetic Brillouin zone:  $-\pi / q \leq k_x \leq \pi / q$  and  $-\pi \leq k_y \leq \pi$ . An explicit calculation shows that the Chern numbers of all isolated bands of the Harper-Hofstadter model are nonzero and can be found as solutions of a simple Diophantine equation (Thouless et al., 1982). As shown in the right panel of Fig. 3, this model exhibits a rich structure of positive and negative Chern numbers depending on the magnetic flux.

Haldane model: The Haldane model (Haldane, 1988) is the first model system that exhibits a nonzero quantized Hall conductance in a nonuniform magnetic field with a vanishing average flux per plaquette. This model demonstrated that, to obtain the quantum Hall effect, the essential feature required is, in fact, not a net magnetic field but the breaking of time-reversal symmetry. As the Haldane model consists of a honeycomb lattice with suitable hopping amplitudes, it is useful to start by briefly reviewing the physics of a tight-binding model on a honeycomb lattice, which is often used to describe electrons in graphene (Castro Neto et al., 2009) and which has recently been widely implemented in photonics, as we will review in Sec. III.D.

The honeycomb lattice with nearest-neighbor hopping is one of the simplest examples of a system which exhibits Dirac cones in the band structure, namely, linear crossings of the energy dispersion of two neighboring bands. A honeycomb lattice has two lattice sites per unit cell, which gives two bands. These are degenerate at two isolated and inequivalent points in the Brillouin zone, called Dirac points. Around the

Dirac points, the effective Hamiltonian of the two bands takes the following form in the sublattice basis:

$$
\hat {H} _ {D} \approx \hbar v _ {D} \left(q _ {x} \sigma_ {x} + q _ {y} \sigma_ {y}\right), \tag {16}
$$

where  $v_{D} \equiv 3t_{1} / 2$  is called the Dirac velocity, with  $t_1$  being the nearest-neighbor hopping amplitude, and  $(q_x,q_y)$  is the momentum measured from a Dirac point. As a result, the dispersion around the Dirac point is linear,  $E = \pm \hbar v_{D}\sqrt{q_{x}^{2} + q_{y}^{2}}$ , and is referred to as the Dirac cone. A complete plot of the band dispersion is shown in Fig. 4(c).

In order to open an energy gap at Dirac points, one needs to add a term proportional to  $\sigma_z$  in  $\hat{H}_D$ . This can be achieved by either breaking time-reversal symmetry or inversion symmetry, which implies that as long as both time-reversal symmetry and inversion symmetry are preserved the gapless Dirac points are protected (Bernevig and Hughes, 2013).

The key novelty of the Haldane model is to add two more sets of terms to the nearest-neighbor honeycomb lattice model, which open energy gaps at the Dirac cones in complementary

![](images/84849e11615e6c103d1b5f77f024ed31a35855f69a373be7cb4b46fc16c05cd2.jpg)  
(a)

![](images/43aabf245704ccdc531041bd5e61346a8bc4094cb76a36b6d9fdbece418997f1.jpg)  
(b)

![](images/ee820f61f5bada88cc623d867982f74385a4a454398955219de3d8ac46218421.jpg)  
(c)

![](images/ca738ad14955a5f9ca9558d045e9bdb962074674933ccbcf08287671afcca5d1.jpg)  
(d)

![](images/b659c13fdbabe54ab7ade48b8f7f50eb752a9b4192ebf3a5a5f9fdaba66f5a5e.jpg)  
(e)  
FIG. 4. (a) A plaquette of the Haldane model. In addition to the usual nearest-neighbor hoppings, there are also complex next-nearest-neighbor hoppings. For the latter, hopping along the arrows carries a phase of  $\phi$ , whereas the hopping opposite to the arrows carries the opposite phase of  $-\phi$ . (b) The phase diagram of the Haldane model as a function of the next-nearest-neighbor hopping phase  $\phi$  and the sublattice energy difference  $2M$ . (c) Bulk band structure of the honeycomb lattice with nearest-neighbor hopping only. Conical touchings of the bands are Dirac points. (d) Typical bulk band structure of the Haldane model in the presence of a band gap. (e) Typical band structure for a gapless honeycomb lattice with zigzag edges. Flat-band localized edge states (indicated in color) connect between the Dirac cones, with one per edge. (f) Typical band structure with edges on both sides of the system when a topological gap opens. Red and blue lines indicate edge states on left and right edges, respectively.

![](images/679fb6cfa6efadfcf5bb712bdda2c81c3f98b158fb67218041f85fef4c4eeeb4.jpg)  
(f)

ways, by breaking inversion symmetry or time-reversal symmetry. The first set of terms is a constant energy difference  $2M$  between two sublattices, which breaks inversion symmetry. The second set of terms are next-nearest-neighbor hoppings with magnitude  $t_2$  and complex hopping phases breaking time-reversal symmetry, i.e., hopping along the arrows in Fig. 4(a) carries a phase of  $\phi$ , whereas the hopping along the opposite direction carries the opposite phase of  $-\phi$ . While adding the energy difference between sublattices opens a trivial gap, in the sense that the resulting bands are topologically trivial, adding complex next-nearest-neighbor hoppings results in opening a gap with topologically nontrivial bands. This different behavior is due to the breaking of time-reversal symmetry by the complex hopping phases, a necessary condition to obtain a nonzero Chern number (Bernevig and Hughes, 2013). The full topological phase diagram of the Haldane model as a function of the magnitude of the two gap-opening terms is summarized in Fig. 4(b), while an example of the energy band dispersion for a bulk system is shown in Fig. 4(d).

The nontrivial topology of the Haldane model can also be seen from the appearance of chiral-propagating edge states. The gapless dispersion of a finite slab of honeycomb lattice is displayed in Fig. 4(e), to be contrasted with the topologically nontrivial gap of the Haldane model displayed in Fig. 4(f). Along the  $y$  direction the system is taken to be periodic, so the momentum  $k_{y}$  is a good quantum number. In the other  $x$  direction, we have a large but finite-size system with a sharp edge. While the edge states of the unperturbed honeycomb lattice are flat at the energy of the Dirac points [Fig. 4(e)], two propagating edge states appear when a bulk topological gap opens, which traverse the energy gap in opposite directions along opposite edges of the system [Fig. 4(f)]. Propagation of each of these states is therefore unidirectional and is protected by the fact that these edge states are spatially separated, suppressing scattering processes from one edge state into the other.

The Haldane model, and its generalization, has been realized in solid-state systems by Chang et al. (2013), as well as in photonics (Rechtsman, Zeuner, Plotnik et al., 2013) and ultracold atomic gases (Jotzu et al., 2014).

Bulk-edge correspondence: The relationship between a topologically nontrivial band structure and the presence of topologically protected edge states is a very general phenomenon known as the bulk-edge correspondence (Hatsugai, 1993a, 1993b; Qi, Wu, and Zhang, 2006). We now illustrate the bulk-edge correspondence through a simple model. Note that a solid mathematical formulation of this bulk-edge correspondence has been developed based on the index theorem (Callias, 1978; Chiu et al., 2016).

As we have seen in the Haldane model, one can obtain topological bands by adding proper gap-opening terms, proportional to  $\sigma_z$ , to the gapless unperturbed Hamiltonian (16). Looking at the phase diagram of the Haldane model, Fig. 4(b), a topological phase transition can be induced by changing  $M / t_2$  or  $\phi$ . In the Dirac Hamiltonian description, this topological phase transition corresponds to adding a  $\sigma_z$  term and changing the sign of its coefficient (Haldane, 1988; Bernevig and Hughes, 2013). We can therefore model the

interface of two Haldane models with different Chern numbers by considering the following Jackiw-Rebbi Hamiltonian (Jackiw and Rebbi, 1976):

$$
\hat {H} = \hbar v _ {D} \left(q _ {x} \sigma_ {x} + q _ {y} \sigma_ {y}\right) + m (x) \sigma_ {z}, \tag {17}
$$

where the mass term  $m(x)$  varies along the  $x$  direction, obeying  $m(x) < 0$  at  $x < 0$ ,  $m(0) = 0$ , and  $m(x) > 0$  at  $x > 0$ . The gap closes at  $x = 0$ , and the system is divided into two parts with  $m < 0$  and  $m > 0$  with different Chern numbers, which are sketched in Fig. 5 for illustration. Writing the momentum operators in terms of a spatial derivative  $(q_{x,y} = -i\nabla_{x,y})$ , it is straightforward to see that the wave function of the form

$$
\psi (x) \propto e ^ {i k _ {y} y} \exp \left(- \frac {1}{\hbar v _ {D}} \int_ {0} ^ {x} m \left(x ^ {\prime}\right) d x ^ {\prime}\right) \binom {1} {i} \tag {18}
$$

is an eigenstate of the Hamiltonian with the energy  $\hbar v_{D}k_{y}$ . This state  $\psi (x)$  is localized around  $x = 0$ , and has a positive group velocity along the  $y$  direction. As there is no other normalizable state around  $x = 0$  with a negative group velocity, this state is chiral and robust against backscattering. Analogously, edge states around a generic topologically nontrivial system can be understood as interface states between the system and the topologically trivial vacuum (Hasan and Kane, 2010).

# 2. Quantum spin Hall system

In all the models that we have seen so far, time-reversal symmetry was explicitly broken through either the applied magnetic field or the complex hopping phase. When time-reversal symmetry is present, the Berry curvature obeys  $\Omega_{n}(-\mathbf{k}) = -\Omega_{n}(\mathbf{k})$  for nondegenerate bands, implying that the Chern number, which is an integral of the Berry curvature over the Brillouin zone, is necessarily zero. A similar argument also holds for degenerate bands: no Chern bands can be

![](images/fd04973ac8b20853cb909507e9b1928724ec7c8205e3999fc26cd687caddfd16.jpg)  
FIG. 5. A schematic illustration of how the interface of two regions with different topological numbers can host a localized state. The spatial dependence of the mass term  $m(x)$  and the wave function residing at the interface ( $x = 0$ ) are schematically plotted. Sketched on top is the schematic dispersion for values of  $m$  at corresponding positions, showing that the bulk band gap closes when  $m(0) = 0$ .

found in two-dimensional systems preserving time-reversal symmetry (Bernevig and Hughes, 2013).

In 2005, new classes of two-dimensional topological phases were proposed (Kane and Mele, 2005a, 2005b; Bernevig, Hughes, and Zhang, 2006; Bernevig and Zhang, 2006). These models consist of two copies of a Chern insulator, one for each spin, where the magnetic fields acting on two spins are opposite and hence the Chern number for spin up  $C_{\mathrm{up}}$  is opposite to that for spin down  $C_{\mathrm{down}} = -C_{\mathrm{up}}$ . Since the magnetic fields for two spins are opposite, time-reversal symmetry is preserved, and the sum of the Chern numbers for the two spins is zero. In this model, as long as there are no spin-flip processes, the two spin components are uncoupled and independently behave as Chern insulators with opposite Chern numbers  $C_{\mathrm{up,down}}$ . As a result, there are the same number of edge states in the two spin states, but with opposite propagation direction; instead of chiral, the edge states are then called helical.

Even when the spin is not conserved, at least one pair of edge states survives and is topologically protected, as long as time-reversal symmetry holds. This feature is a consequence of Kramers's theorem, which holds in fermionic systems in the presence of time-reversal symmetry. The theorem tells us that if there is a state with energy  $E$  and momentum  $\mathbf{k}$ , there must exist another distinct state with the same energy but with the opposite momentum  $-\mathbf{k}$ . In particular, at time-reversal-symmetric momenta such as  $\mathbf{k} = 0$ , states should be doubly degenerate. As a consequence, when there is a pair of edge states with spin-up and spin-down crossings at  $\mathbf{k} = 0$ , the edge states cannot open a gap, and hence there are topologically protected helical edge states. This is clearly different from a trivial insulator where there are no robust edge states traversing the gap. The topological invariant characterizing the system is given by  $C_{\mathrm{up}} \mod 2$  ( $= C_{\mathrm{down}} \mod 2$ ), which takes values of either 0 (trivial) or 1 (nontrivial), and thus is called the  $\mathbb{Z}_2$  topological invariant. This  $\mathbb{Z}_2$  topological invariant keeps the same value even when spin-mixing terms are added, provided time-reversal symmetry is maintained (Kane and Mele, 2005b; Fu and Kane, 2006; Sheng et al., 2006; Roy, 2009). Such topological phases are called the quantum spin Hall insulators or the  $\mathbb{Z}_2$  topological insulators. The  $\mathbb{Z}_2$  topological insulator has been experimentally realized in HgTe quantum wells (König et al., 2007) following the theoretical proposal (Bernevig, Hughes, and Zhang, 2006). Shortly afterward,  $\mathbb{Z}_2$  topological insulators were found to exist also in three dimensions (Fu, Kane, and Mele, 2007; Moore and Balents, 2007; Qi, Hughes, and Zhang, 2008; Roy, 2009).

One may also envisage an analog of the quantum spin Hall insulators for photons by using, for example, the polarization degree of freedom as pseudospins. However, the bosonic nature of photons forbids the existence of direct photonic analogs of the quantum spin Hall insulators (De Nittis and Lein, 2017). For Kramers's theorem to hold, one needs for the time-reversal operator  $\mathcal{T}$  to be fermionic, which satisfies  $\mathcal{T}^2 = -1$ , while the bosonic time-reversal operator obeys  $\mathcal{T}^2 = +1$ .

However, if there is no coupling between pseudospins, i.e., if there is an extra symmetry in the system, then each pseudospin component can independently behave as a model

with nonzero Chern number and hence shows helical edge states in the presence of the bosonic time-reversal symmetry (Hafezi et al., 2011; Albert, Glazman, and Jiang, 2015). Note however that topological edge states of such systems are not robust against terms coupling different pseudospin states, which would be the photonic analog of time-reversalsymmetry breaking magnetic impurities for electronic  $\mathbb{Z}_2$  topological insulators. Photonic models showing analogs of quantum spin Hall systems with no (or little) couplings between different pseudospin states are reviewed in Sec. III.B.

# 3. Topological phases in other dimensions

We have so far reviewed the topological phases of matter in two dimensions with and without time-reversal symmetries. Generally speaking, in the presence of a given symmetry, one can consider topological phases which are protected as long as the symmetry is preserved, which lead to the concept of the symmetry-protected topological phases. A complete classification of noninteracting fermionic topological phases in any dimension based on the time-reversal, particle-hole, and chiral symmetries is known in the literature (Kitaev, Lebedev, and Feigelman, 2009; Schnyder et al., 2009; Ryu et al., 2010; Teo and Kane, 2010; Chiu et al., 2016).

As the topological band structure is a single-particle property and does not depend on the statistics of the particles, this classification, originally derived for fermionic systems, directly applies to bosonic systems as well, provided the Hamiltonian conserves the number of particles. The situation is in fact different when the number of particles is allowed to change, e.g., in Bogoliubov-de Gennes Hamiltonians of superconductors; in this case the bosonic and fermionic band structures are different. The fermionic case is included in the above-mentioned classification, while the bosonic case is reviewed in Sec. VI.B. We now focus on three specific examples of topological phases of matter in dimensions other than two: one-dimensional Hamiltonians with chiral symmetry, three-dimensional Weyl points, and higher-dimensional quantum Hall systems.

One-dimensional chiral Hamiltonian: One-dimensional Hamiltonians with chiral symmetry can have topologically nontrivial phases characterized by an integer-valued winding number. In noninteracting tight-binding models, chiral symmetry is equivalent to having a bipartite lattice, i.e., a lattice that can be divided into two sublattices with hopping occurring only between different sublattices. When a discrete translational symmetry is present, the Hamiltonian in momentum space can be written in the following generic form (Ryu et al., 2010):

$$
\hat {H} _ {k} = \left( \begin{array}{c c} \mathbf {0} & Q (k) ^ {\dagger} \\ Q (k) & \mathbf {0} \end{array} \right), \tag {19}
$$

where  $Q(k)$  is an  $n \times n$  matrix satisfying  $Q(k) = Q(k + 2\pi / a)$ , each unit cell consists of  $2n$  sites, and  $a$  is again the lattice spacing.

When there is a gap at zero energy, namely,  $\operatorname{det} Q(k) \neq 0$  for any  $k$ , the topology of this Hamiltonian is characterized by the winding number defined through the phase of  $\operatorname{det} Q(k) \equiv |\operatorname{det} Q(k)| e^{i\theta(k)}$  as (Zak, 1989; Kane and Lubensky, 2014)

$$
\mathcal {W} = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi / a} d k \frac {d \theta (k)}{d k}. \tag {20}
$$

The winding number tells us the number of times  $\det Q(k)$  wraps around the origin when plotted in a complex plane as one varies  $k$  along the Brillouin zone. The bulk-boundary correspondence states that the number of zero-energy edge modes on one side of the one-dimensional chain is given by the absolute value of the winding number  $|\mathcal{W}|$  (Ryu and Hatsugai, 2002; Delplace, Ullmo, and Montambaux, 2011). Such zero-energy edge modes are topologically protected in the sense that they remain locked at zero energy even in the presence of chiral-symmetry-preserving perturbations provided the gap remains open.

The prototypical example of a one-dimensional chiral Hamiltonian with nontrivial topology is the SSH model (Su, Schrieffer, and Heeger, 1979), which is a chain with two alternating hopping strengths as sketched in Fig. 6. The system can be divided into two sublattices  $A$  and  $B$ , and the tight-binding Hamiltonian can be written as

$$
\hat {H} _ {\mathrm {S S H}} = \sum_ {x} \left(t \hat {b} _ {x} ^ {\dagger} \hat {a} _ {x} + t ^ {\prime} \hat {a} _ {x + 1} ^ {\dagger} \hat {b} _ {x} + \mathrm {H . c .}\right), \tag {21}
$$

where  $a_{x}$  and  $b_{x}$  are annihilation operators for  $A$  and  $B$  sublattice sites at position  $x$ . The intracell and intercell hoppings are described by the (real) hopping amplitudes  $t$  and  $t'$ , respectively. After a Fourier transformation, one sees that the momentum-space Hamiltonian has the form of Eq. (19) with  $n = 1$  and  $Q(k) = t + t' e^{ik}$ . The system is gapped as long as  $t \neq t'$ , and the corresponding winding numbers are  $\mathcal{W} = 0$  for  $t > t'$  and  $\mathcal{W} = 1$  for  $t < t'$ . Therefore, when the chain is terminated at one end with the final hopping of  $t$ , there exists a zero-energy topological edge state if  $t < t'$  (Ryu and Hatsugai, 2002).

One-dimensional photonic structures with nontrivial topology will be discussed in Sec. IV.

Three-dimensional Weyl points: As briefly introduced, two-dimensional band structures can host Dirac cones, corresponding to gapless points around which bands disperse linearly with respect to the two quasimomenta (16). In three dimensions, the analog of a Dirac point is a Weyl point (Wan et al., 2011; L. Lu et al., 2013; Armitage, Mele, and Vishwanath, 2018): a point degeneracy between two bands which have a linear dispersion in all three directions in momentum space at low energy, as described by the Weyl Hamiltonian:

$$
H _ {W} = \hbar v \left(q _ {x} \sigma_ {x} + q _ {y} \sigma_ {y} + q _ {z} \sigma_ {z}\right), \tag {22}
$$

![](images/a5e82b6f6b247c61b2d804cc0cf88e000aa7df381370ac207b05e7dfece72c1a.jpg)  
FIG. 6. Schematic illustration of the Su-Schrieffer-Heeger (SSH) model. Dashed squares indicate the unit cell of the lattice; each unit cell contains two lattice sites, one belonging to the  $A$  sublattice and the other to the  $B$  sublattice. The lattice terminates on the left-hand side with a complete unit cell.

where  $\mathbf{q} = (q_x, q_y, q_z)$  is the momentum measured relative to the degenerate point and  $v$  is the group velocity, taken here to be locally isotropic.

Close to a Weyl point, the resulting Berry curvature (6) is reminiscent of the magnetic field around a magnetic monopole, where the field can either point outward or inward toward the Weyl point. In analogy with magnetic monopoles, a quantized "charge" can be associated with a Weyl point; this is nothing other than a Chern number calculated by integrating the Berry curvature over a two-dimensional surface enclosing the Weyl point, generalizing Eq. (8). It can also be shown that Weyl points generate only nonzero Berry curvature when either  $\mathcal{P}$  (parity) and/or  $\mathcal{T}$  (time-reversal symmetry) is broken. Consequently, to get Weyl points in a band structure, one can break  $\mathcal{P},\mathcal{T}$ , or both symmetries. The photonic realization of Weyl points and other three-dimensional gapless phases will be discussed in Sec. V.A.

Higher-dimensional quantum Hall systems: The two-dimensional integer quantum Hall effect, previously introduced, is just the first in a family of related quantum Hall phenomena that can exist in higher dimensions (Chiu et al., 2016). Here we briefly review what happens in three or four spatial dimensions, highlighting key differences that emerge due to having odd or even numbers of spatial dimensions.

First, in an odd number of spatial dimensions, the possible quantum Hall responses are closely related to those of a lower-dimensional system, as they are only associated with lower-dimensional topological invariants. In three dimensions, for example, a gapped band can be labeled by a triad of Chern numbers, e.g.  $\left[\mathbf{C}^{(1)}\equiv (C_x^{(1)},C_y^{(1)},C_z^{(1)})\right]$ , where each Chern number is calculated from Eq. (8) by integrating the Berry curvature over a 2D momentum plane orthogonal to the quasimomentum direction indicated (Avron, Seiler, and Simon, 1983). This triad of two-dimensional topological invariants leads to a linear three-dimensional quantum Hall effect, calculated by extending Eq. (10) to three spatial dimensions (Halperin, 1987; Montambaux and Kohmoto, 1990; Kohmoto, Halperin, and Wu, 1992). In the simplest case, such a three-dimensional quantum Hall system could be constructed by stacking 2D quantum Hall systems along a third direction and weakly coupling the layers together (Störmer et al., 1986; Chalker and Dohmen, 1995; Balents and Fisher, 1996; Bernevig et al., 2007). In Sec. V.B, we discuss three-dimensional quantum Hall systems and other gapped 3D topological phases in the context of photonics.

Second, in even numbers of spatial dimensions, such as four dimensions, new types of quantum Hall effect can emerge that are intrinsically associated with that higher dimensionality (Meng, 2003; Prodan and Schulz-Baldes, 2016). These quantum Hall effects can be distinguished from their lower-dimensional cousins as they appear as a higher-order response to perturbing electromagnetic fields and because they are related to topological invariants that vanish in fewer spatial dimensions.

The four-dimensional quantum Hall effect, in particular, was first discussed by Fröhlich and Pedrini (2000) and Zhang and Hu (2001), and later played an important role in understanding time-reversal invariant topological insulators in two and three dimensions through a dimensional-reduction

procedure from four dimensions (Qi, Hughes, and Zhang, 2008). This quantum Hall effect consists of a nonlinear quantized current response in one direction, when perturbative electric and magnetic fields are applied in the other three directions. We assume for simplicity that only one nondegenerate band is occupied and an electromagnetic gauge potential  $\mathbf{A} = (A_0,A_1,A_2,A_3,A_4)$  is applied as a perturbation, where  $A_{0}$  is the electric potential and  $(A_{1},A_{2},A_{3},A_{4})$  is the magnetic vector potential in four dimensions. The current in response to the applied electric field  $E_{\nu}\equiv \partial_{0}A_{\nu} - \partial_{\nu}A_{0}$  and the applied magnetic field  $B_{\rho \sigma}\equiv \partial_{\rho}A_{\sigma} - \partial_{\sigma}A_{\rho}$  is then given by (Price et al., 2015)

$$
j ^ {\mu} = - \frac {e ^ {2}}{h} E _ {\nu} \int_ {\mathrm {B Z}} \Omega^ {\mu \nu} \frac {d ^ {4} k}{(2 \pi) ^ {3}} + \frac {e ^ {3}}{2 h ^ {2}} \varepsilon^ {\mu \nu \rho \sigma} E _ {\nu} B _ {\rho \sigma} C ^ {(2)}, \tag {23}
$$

where  $\mu, \nu, \rho$ , and  $\sigma$  run through spatial indices. The Berry curvature along the  $\mu - \nu$  plane is defined as  $\Omega^{\mu \nu} = \partial_{k_\mu}\mathcal{A}_\nu - \partial_{k_\nu}\mathcal{A}_\mu$  in terms of the usual Berry connection  $\mathcal{A}_{\mu} = i\langle u_k|\partial_{k_\mu}|u_k\rangle$  and the integral is now over the four-dimensional Brillouin zone. Here  $\varepsilon^{\mu \nu \rho \sigma}$  is the 4D Levi-Civita symbol.

The second term in Eq. (23) vanishes in fewer than four spatial dimensions, and so this is the new quantum Hall effect that can emerge in a 4D system. It depends also on a four-dimensional topological invariant (Nakahara, 2003)

$$
C ^ {(2)} = \frac {1}{3 2 \pi^ {2}} \int_ {\mathrm {B Z}} \varepsilon_ {\alpha \beta \gamma \delta} \Omega^ {\alpha \beta} \Omega^ {\gamma \delta} d ^ {4} k, \tag {24}
$$

which is known as the second Chern number. In contrast, the Chern number (8) appearing in the two-dimensional quantum Hall effect is sometimes called the first Chern number. Note that both first and second Chern numbers can be extended to the case of degenerate bands by taking a trace of the integrand over the degenerate bands. The first term in Eq. (23) is a contribution to the current that is reminiscent of the two-dimensional quantum Hall response, where only two directions are involved, and is characterized by the first Chern number in the  $\mu-\nu$  plane; physically, this is similar to the quantum Hall physics of odd dimensions introduced above. Note that when the system possesses time-reversal symmetry, the first term of Eq. (23) vanishes and only the second term remains (Zhang and Hu, 2001). Experimental observations of the four-dimensional quantum Hall effect through topological pumping are discussed in Sec. IV.B, and proposals for directly observing the four-dimensional quantum Hall effect using synthetic dimensions are discussed in Sec. V.C.

# 4. Topological pumping

Topological invariants, such as the first and second Chern numbers defined above, can also lead to a quantization of particle transport in systems which are "pumped" periodically and adiabatically in time. In this section, we introduce the concept of topological pumping by reviewing connections between the Archimedes screw pump and a topological pump in the semiclassical limit. We then discuss how a 1D topological pump can be related to the 2D quantum Hall effect, and how the topological framework developed so far leads to a simple lattice model for a topological pump.

Archimedes screw pump: A pump is a device that moves fluids by mechanical action, i.e., it consumes energy to perform mechanical work by moving the fluid. One of the oldest pumps known to man is the so-called Archimedes screw pump, which is still in use today. In this device, a fluid is pumped by turning a screw-shaped surface inside a cylindrical shaft; see Fig. 7(a). As the screw-shaped surface is made to rotate around its axis, a volume of fluid is collected at one end of the device. It is then pushed along the tube by the rotating helicoid until it pours out at the other end of the device. Ideally, at each full turn of the pump, the collected volume is identical and the fluid is homogeneously transported a unit of distance along the device. Consequently, the screw pump is used as a variable rate feeder to deliver a measured rate or quantity of material in industrial processes.

Let us now adopt a quantum mechanical description of the screw pump. At any given time, the fluid is approximately confined within a series of parabolic potentials; see Fig. 7(a). Assuming that the fluid is noninteracting, it suffices to write the Hamiltonian for a single particle of mass  $m$  in the resulting chain of parabolic potentials

$$
\begin{array}{l} \hat {H} = \frac {\hat {p} _ {x} ^ {2}}{2 m} + V \sum_ {j} [ \hat {x} - x _ {j} (t) ] ^ {2} \theta \left\{\left[ x _ {j - 1} (t) + x _ {j} (t) \right] / 2 \right\} \\ \times \theta \{- [ x _ {j + 1} (t) + x _ {j} (t) ] / 2 \}, \tag {25} \\ \end{array}
$$

![](images/c66a747c501ab9e8e43b89c04941bd88ef40b159193b66009e145cdc8858e762.jpg)  
FIG. 7. (a) Schematic of an Archimedes screw pump, which mechanically transports fluid in the direction of the blue arrow as the helicoidal surface is rotated. In a quantum mechanical treatment, the screw pump can be approximated by a series of parabolic potentials, as indicated by the blue dashed lines. (b) Illustration of the quantum Hall effect for Landau levels; the spectrum is sketched in the Landau gauge on a cylinder, with open boundary conditions along  $x$  and periodic boundary conditions along  $y$ . Each state in a given Landau level is indexed by the transverse momentum  $k_{y}$ , setting the center of the state along  $x$ . As magnetic flux is threaded through the cylinder, an electric field is generated along  $y$  and there is a spectral flow of states along  $x$ , corresponding to the quantum Hall transport. At the system boundaries, the Landau levels bend up in energy, forming chiral-propagating edge states, as expected from the bulk-boundary correspondence. At the left-hand side, the threading of flux means empty states will move down in energy and be filled up from an external reservoir as they cross the Fermi level  $\mu$ . At the right-hand side, states will flow up in energy and particles will be ejected into a reservoir. Signatures of these chiral edge states persist in a 1D topological pump as edge modes that cross the bulk energy gap as the pump parameter is tuned.

![](images/baa2aab9016bd311c4250a0839103ca36f9804dd8fceb5a1823067a1762577ab.jpg)

where  $\hat{x}$  and  $\hat{p}_x$  are the position operator and its conjugate, respectively. The parabolic potentials are characterized by time-dependent minima located at points  $x_{m}(t)$ , with a potential amplitude  $V$ , and equidistant separation  $\Delta x = x_{m+1} - x_m$ . The Heaviside function  $\theta[x]$  cuts the influence of neighboring sites on one another. Neglecting the coupling between neighboring wells, each well hosts the standard harmonic oscillator states of a single particle. Within a pump cycle, the minima can be parametrized as  $x_m(t) = x_{m,0} + U(\varphi(t))\Delta x$ , where  $x_{m,0}$  are some initial positions,  $\varphi(t) = 2\pi t / T_p$  is the periodic pumping parameter, and the displacement satisfies  $U(\varphi + 2\pi) = U(\varphi) + 1$ . After a full period  $T_p$  of the pumping, each minimum moves by one site, and thus the Hamiltonian is invariant. Therefore, the eigenstates of the Hamiltonian are periodic as  $\varphi \rightarrow \varphi + 2\pi$ .

Turning on weak tunnel coupling between the localized states leads to one-dimensional Bloch bands that span the device, with time-dependent Bloch states  $u_{n,k_x,\varphi}(x)$  and Bloch energies  $\omega_{n,k_x,\varphi}$ . In the semiclassical limit, the transport of particles by pumping can generally be captured using the semiclassical equations of motion for a wave packet that is prepared with a well-defined center-of-mass position  $x$  and momentum  $k_x$  in a given instantaneous Bloch band  $n$ . Under adiabatic modulation of the pumping parameter, the wave packet remains in the instantaneous band and evolves with a velocity

$$
\dot {x} _ {n} = \frac {\partial \omega_ {n , k _ {x} , \varphi}}{\partial k _ {x}} + \Omega_ {n} \partial_ {t} \varphi \tag {26}
$$

resulting from the sum of the usual group velocity plus an anomalous velocity term. The latter is determined by the Berry curvature  $\Omega_{n}(k_{x},\varphi) = i(\langle \partial_{\varphi}u_{n}|\partial_{k_{x}}u_{n}\rangle -\langle \partial_{k_{x}}u_{n}|\partial_{\varphi}u_{n}\rangle)$  associated with the instantaneous Bloch states (Karplus and Luttinger, 1954; Xiao, Chang, and Niu, 2010).

Hence, changing the pump parameter  $\varphi$  induces an extra motion of the particle which, depending on the sign of  $\Omega_{n}$ , can be either in the same or in the opposite direction as the motion of the lattice. The resulting displacement of the wave packet after one pump cycle is obtained by integrating  $\dot{x}_n$  and can in principle be arbitrary. As this anomalous particle transport depends on the geometrical Berry curvature, it is often referred to as "geometrical pumping." Experiments along these lines have been performed with cold atoms by H.-I. Lu et al. (2016) and in photonics by Wimmer et al. (2017).

For a filled or homogeneously populated bulk band  $n$ , however, the periodicity of the Bloch energy  $\omega_{n,k_x,\varphi}$  in  $k_x$  around the Brillouin zone guarantees that the group velocity contribution integrates to zero. The displacement per cycle can then be related to the 2D topological first Chern number  $C$  of the pumping process:

$$
C = \frac {1}{2 \pi} \int_ {\mathrm {B Z}} \int_ {0} ^ {2 \pi} \Omega_ {n} \left(k _ {x}, \varphi\right) d \varphi d k _ {x} \tag {27}
$$

whose expression closely resembles Eq. (8) for the Chern number of a band. As the displacement is proportional to this topological invariant, it neither depends on the pumping speed, provided adiabaticity still holds, nor on the specific

lattice parameters as long as band crossings do not occur. Hence, the transport is highly robust against perturbations such as interaction effects or disorder (Niu and Thouless, 1984). For the screw pump potential (25), one intuitively expects the fluid to move along with the moving potential. This is in agreement with our effective Bloch-bands description, where all lowest bands of the system appear with  $C = 1$  corresponding to the displacement by  $\Delta x$  per unit cycle. The situation is of course much richer in the wave mechanics case where the displacement can also be in the opposite direction depending on the sign of  $C$ .

There is a deep connection between the screw pump and the physics of the quantum Hall effect, as suggested by the quantization of the pumped particles per cycle in terms of the topological first Chern number. To explore this further, we start from the Landau-level Hamiltonian introduced in Eq. (11) in the Landau gauge  $\mathbf{A} = (0,xB,0)$ . Then the transverse momentum  $\hbar k_{y}$  is a good quantum number, and, for a given state, the Hamiltonian reduces to that of a shifted 1D harmonic oscillator

$$
\hat {H} _ {\mathrm {L L}} = \frac {\hat {p} _ {x} ^ {2}}{2 m _ {a}} + \frac {1}{2} m \omega_ {c} ^ {2} \left(\hat {x} - \frac {\hbar k _ {y}}{m \omega_ {c}}\right) ^ {2}, \tag {28}
$$

where  $\omega_{c}$  is the cyclotron frequency, and  $x_{c} = \hbar k_{y} / m\omega_{c}$  is the shifted center of the harmonic potential. Comparing this expression with Eq. (25), one can see that a state in a given potential minimum  $j$  in the 1D screw pump is analogous to a state with a given  $k_{y}$  in a 2D Landau level.

In the Landau gauge, we can imagine putting the system on a cylinder, i.e., applying periodic boundary conditions in the  $y$  direction, and threading a magnetic flux through the cylinder. [Note that applying periodic boundary conditions puts  $k_{y}$  on a lattice of discretely allowed values given by the Born-von Karman boundary conditions, analogously to Eq. (25).] This threading of flux generates an electromotive electric field  $E_{y}$  in the  $y$  direction, leading to a Hall response in the  $x$  direction. An adiabatic threading of flux causes continuous evolution of eigenvalues known as the spectral flow (Phillips, 1996; Waterstraat, 2016). The number of states which cross the gap in the positive direction over the flux-threading cycle is equal to the Chern number of the spectral gap  $\sigma_{n}$ . The central position  $x_{c}$  of each eigenstate shifts to that associated with the next allowed value of  $k_{y}$ , similar to how minima move in the screw pump, and in agreement with Laughlin's pumping argument (Laughlin, 1981). Indeed, Landau levels have first Chern numbers  $|C| = 1$  in agreement with the intuition developed from the screw pump.

This analogy shows that the pump parameter  $\varphi$  of the 1D screw pump can be thought of as a threaded magnetic flux and hence a momentum in a perpendicular fictitious dimension; this correspondence can be exploited in a procedure called "dimensional extension" to derive the appropriate higher-dimensional model beginning from the lower-dimensional pump (Qi, Hughes, and Zhang, 2008; Kraus et al., 2012; Kraus and Zilberberg, 2012; Kraus, Ringel, and Zilberberg, 2013; Verbin et al., 2013, 2015; Prodan and Schulz-Baldes, 2016). Finally, as sketched in Fig. 7, the bulk-edge correspondence of the quantum Hall effect can be used to explain

how a topological pump functions with open boundary conditions and couples to particle reservoirs.

Thouless pump and the Hofstadter model: Turning the above analogy around, we can start with a 2D quantum Hall system, such as the Hofstadter model Eq. (14), and obtain the corresponding topological pump. For the Hofstadter model in the Landau gauge, we proceed by Fourier transforming the model only in the  $y$  direction to obtain

$$
\begin{array}{l} \hat {H} = - J \sum_ {x, k _ {y}} \left[ \hat {a} _ {x, k _ {y}} ^ {\dagger} \hat {a} _ {x + a, k _ {y}} + \mathrm {H . c .} \right. \\ + 2 \cos (2 \pi \alpha x / a - k _ {y} a) \hat {a} _ {x, k _ {y}} ^ {\dagger} \hat {a} _ {x, k _ {y}} ]. \tag {29} \\ \end{array}
$$

Then applying the procedure of "dimensional reduction," the momentum along  $y$  is now considered as an external parameter  $\varphi = k_y$ ; this reduces the dimensionality of the Hamiltonian by one dimension by removing the sum over  $k_y$  and making the operators  $k_y$  independent (Thouless, 1983). This 1D model Eq. (29) is then commonly known as the Harper model (Harper, 1955) and will be discussed in detail in Sec. IV.B. This system can be adiabatically pumped by slowly changing the external parameter  $\varphi$  and hence modulating the on-site energy periodically in time. For a filled band insulator, this is known as a Thouless pump (Thouless, 1983), as there is a quantization of particle transport over each pump cycle, as set by the sum over the first Chern numbers of the filled bands.

The main distinction from the Landau-level case discussed above is that in the Hofstadter model there are two competing length scales: the lattice spacing and the magnetic length. As a result, the electron paths interfere to give the fractal Hofstadter butterfly, with a resulting band structure composed of bands with positive and negative Chern numbers. Similarly, in the 1D Thouless pump, the on-site potential imposes a new length scale, and in the resulting band structure, we encounter bands that will pump against the direction in which the potential is moved. This is a purely wave-physics interference effect in contrast to the classical particle picture used to understand the screw pump.

In the lattice configuration realized in the ultracold atomic experiment (Lohse et al., 2016; Nakajima et al., 2016), the lowest energy band had a positive  $C > 0$ . Observing pumping in the opposite direction then required working with higher bands, which was achieved using the atomic gas in strongly nonequilibrium conditions. As reviewed in Sec. IV.B, photonic systems proved to be an ideal platform for realizing topological pumps in more complex and also higher-dimensional geometries.

# 5. Floquet engineering: Topology through time-periodic modulations

After having introduced in the previous section the general concepts of topological bands, we now briefly review the manner by which topological band properties can be generated by subjecting a static system to an external time-periodic drive, an approach which is generally referred to as Floquet engineering, due to its direct relation to the Floquet theorem (Oka and Aoki, 2009; Kitagawa, Berg et al., 2010;

Kitagawa et al., 2011; Lindner, Refael, and Galitski, 2011; Cayssol et al., 2013; Goldman and Dalibard, 2014; Bukov, D'Alessio, and Polkovnikov, 2015; Eckardt, 2017). We will describe how topological properties emerge in this general context and will then briefly discuss how Floquet engineering can be exploited in photonics.

Let us first consider a generic quantum system described by the static Hamiltonian  $\hat{H}_0$ . The aim of Floquet engineering is to modify the band structure of this Hamiltonian, effectively, by subjecting the system to a time-periodic modulation  $\hat{V}(t + T) = \hat{V}(t)$ , where  $T = 2\pi/\Omega$  denotes the period of the drive. In the nontrivial case where  $[\hat{H}_0, \hat{V}(t)] \neq 0$ , the time-evolution operator  $\hat{U}(t, t_0)$ , which is associated with the total time-dependent Hamiltonian  $\hat{H}(t) = \hat{H}_0 + \hat{V}(t)$ , forms an intricate object that one can formally write as a time-ordered integral  $\hat{U}(t, t_0) = \mathcal{T} \exp[-(i/\hbar) \int_{t_0}^t dt' \hat{H}(t')]$ . However, due to the time-periodicity inherent to the system  $\hat{H}(t + T) = \hat{H}(t)$ , this time-evolution operator can be factorized, leading to the more suggestive form (Kiss, Janszky, and Adam, 1994; Rahav, Gilary, and Fishman, 2003; Goldman and Dalibard, 2014; Bukov, D'Alessio, and Polkovnikov, 2015)

$$
\hat {U} (t, t _ {0}) = e ^ {- i \hat {K} _ {\mathrm {k i c k}} (t)} e ^ {- i (t - t _ {0}) \hat {H} _ {\mathrm {e f f}} / \hbar} e ^ {i \hat {K} _ {\mathrm {k i c k}} (t _ {0})}, \tag {30}
$$

where the operator  $\hat{H}_{\mathrm{eff}}$  is time independent, and where  $\hat{K}_{\mathrm{kick}}(t + T) = \hat{K}_{\mathrm{kick}}(t)$  has zero average over a period of the drive. The latter expression (30) indicates that the dynamics of the periodically driven system is essentially ruled by an effective Hamiltonian  $\hat{H}_{\mathrm{eff}}$ , whose properties are potentially distinct from those associated with the initial static Hamiltonian  $\hat{H}_0$ . In addition, the final "kick"  $e^{-i\hat{K}_{\mathrm{kick}}(t)}$  in Eq. (30) reflects the micromotion, namely, the dynamics taking place within each period of the drive. Both the effective Hamiltonian  $\hat{H}_{\mathrm{eff}}$  and the kick operator  $\hat{K}_{\mathrm{kick}}(t)$  result from a rich interplay between the static Hamiltonian  $\hat{H}_0$  and the drive operator  $\hat{V}(t)$ ; these two operators, and hence the time-evolution operator in Eq. (30), can be systematically computed using various perturbative treatments (Goldman and Dalibard, 2014; Bukov, D'Alessio, and Polkovnikov, 2015; Eckardt and Anisimovas, 2015; Goldman et al., 2015; Mikami et al., 2016).

In traditional realizations, Floquet engineering operates in the so-called "high-frequency" regime of the drive  $(\Omega \to \infty)$ ; physically, this corresponds to situations where the period  $T$  sets the shortest time scale in the system (Kitagawa, Berg et al., 2010), and hence, where the micromotion is typically irrelevant. In this regime of the drive, it is instructive to probe the dynamics stroboscopically, namely, by considering discrete observation times  $t_N = NT$ , where  $N$  is an arbitrary integer and  $t_0 = 0$ . Up to a unitary (gauge) transformation, the long-time dynamics is then captured by the stroboscopic time-evolution operator [Eq. (30)]

$$
\hat {\mathcal {U}} (t _ {N}) = e ^ {- i t _ {N} \hat {H} _ {\mathrm {e f f}} / \hbar} = [ e ^ {- i T \hat {H} _ {\mathrm {e f f}} / \hbar} ] ^ {N} = [ \hat {\mathcal {U}} (T) ] ^ {N}. \tag {31}
$$

Hence, in this framework, the relevant dynamics is governed by the Floquet operator  $\hat{\mathcal{U}}(T)$ , or equally, by the effective

Hamiltonian  $\hat{H}_{\mathrm{eff}} = (i\hbar /T)\log \hat{\mathcal{U}} (T)$ . As an important corollary, the topological properties of the system are then entirely dictated by the band structure of the effective Hamiltonian: for a proper choice of the drive protocol  $[\hat{V} (t)]$ , the effective Hamiltonian  $\hat{H}_{\mathrm{eff}}$  can host topological properties, even when the underlying static system  $(\hat{H}_0)$  is trivial. Consequently, in the high-frequency regime  $(\Omega \rightarrow \infty)$ , the topological classification of periodically driven systems is strictly equivalent to that of static systems (Kitagawa, Berg et al., 2010; Lindner, Refael, and Galitski, 2011; Cayssol et al., 2013): topological band theory (Hasan and Kane, 2010; Qi and Zhang, 2011; Bansil, Lin, and Das, 2016) directly applies to the Bloch bands associated with the effective Hamiltonian  $\hat{H}_{\mathrm{eff}}$ , i.e., the so-called "Floquet spectrum."

A simple but important example of such driven-induced topological states is found when analyzing the properties of a particle hopping on a 2D circularly shaken honeycomb lattice (Oka and Aoki, 2009; Rechtsman, Zeuner, Plotnik et al., 2013; Jotzu et al., 2014; Zheng and Zhai, 2014; Eckardt and Anisimovas, 2015; Plekhanov, Roux, and Hur, 2017). In a frame moving with the shaken lattice, the drive takes the form of a time-periodic inertial force  $\mathbf{F}(t)$ , so that the time-dependent Hamiltonian can be written in the form

$$
\hat {H} (t) = - J \sum_ {\langle j, k \rangle} \hat {a} _ {j} ^ {\dagger} \hat {a} _ {k} - \sum_ {j} \mathbf {F} (t) \cdot \mathbf {r} _ {j} \hat {a} _ {j} ^ {\dagger} \hat {a} _ {j}, \tag {32}
$$

where the first term describes hopping between nearest- neighboring sites of the honeycomb lattice, with hopping amplitude  $J$ , where  $\mathbf{F}(t) = F[\cos (\Omega t)\mathbf{e}_x + \sin (\Omega t)\mathbf{e}_y]$  reflects the circular shaking, and where  $\mathbf{r}_j$  denotes the position of site  $j$ . Interestingly, we note that the time-dependent Hamiltonian in Eq. (32) is equivalent to that describing electrons in graphene when the latter is irradiated by a circularly polarized light (Oka and Aoki, 2009; Cayssol et al., 2013); in that case, the force  $\mathbf{F}(t)$  is then directly related to the ac electric field of the radiation. The effective Hamiltonian  $\hat{H}_{\mathrm{eff}}$  associated with the time-dependent Hamiltonian in Eq. (32) can be evaluated using the so-called  $1 / \Omega$  expansion (Goldman and Dalibard, 2014; Bukov, D'Alessio, and Polkovnikov, 2015; Eckardt and Anisimovas, 2015; Goldman et al., 2015; Mikami et al., 2016), which yields

$$
\hat {H} _ {\text {e f f}} \approx - J _ {\text {e f f}} \sum_ {\langle j, k \rangle} \hat {a} _ {j} ^ {\dagger} \hat {a} _ {k} - J _ {\text {e f f}} ^ {\text {N N N}} \sum_ {\langle \langle m, n \rangle \rangle} i ^ {\mathcal {O}} \hat {a} _ {m} ^ {\dagger} \hat {a} _ {n}, \tag {33}
$$

where the first term describes the renormalization of the nearest neighbor hopping term in Eq. (32), with  $J_{\mathrm{eff}} = J\mathcal{J}_0(Fd / \Omega)$ , and where the second term corresponds to a next-nearest-neighbor hopping term, with effective hopping matrix elements  $J_{\mathrm{eff}}^{\mathrm{NNN}}i^{\mathcal{O}} = \pm i(\sqrt{3} J^{2} / \Omega)\mathcal{J}_{1}^{2}(Fd / \Omega)$  whose sign depends on the orientation of the hopping event. Here  $\mathcal{J}_{0,1}$  denote Bessel functions of the first kind and  $d$  is the lattice spacing. Importantly, the effective Hamiltonian in Eq. (33) is equivalent to the Haldane model (Haldane, 1988) introduced in Sec. II.A.1.

In direct analogy with the original Haldane model, the spectrum associated with the effective Hamiltonian (33) displays two Bloch bands with nonzero Chern numbers and

chiral edge states. In this Floquet-engineered context, we note that the time-reversal-symmetry-breaking nature of the Chern bands naturally stems from the chirality of the circular drive. In condensed matter, a driven system exhibiting effective Bloch bands with nonzero Chern numbers is generally called a Floquet Chern insulator. Such a strategy was considered in various physical contexts, ranging from irradiated materials (Oka and Aoki, 2009; Lindner, Refael, and Galitski, 2011; Cayssol et al., 2013) to ultracold atoms in shaken optical lattices (Jotzu et al., 2014; Eckardt, 2017; Flaschner et al., 2018), but it was in fact pioneered in photonic experiments using femtosecond-laser-written lattices (Rechtsman, Zeuner, Plotnik et al., 2013) as reviewed in detail in Sec. III.A.2.

This Floquet-engineering strategy is not restricted to the Haldane model, but can indeed be extended to engineer other toy models of topological matter. For instance, the Harper-Hofstadter model (Hofstadter, 1976) discussed in Sec. II.A.1 [Eq. (14)] can be designed by subjecting a 2D square lattice to a proper time-periodic modulation; various theoretical proposals can be found in different physical contexts, including cold atoms (Kolovsky, 2011; Creffield et al., 2016), ion traps (Bermudez, Schaetz, and Porras, 2011), and photonics (Fang, Yu, and Fan, 2012b). As further discussed in Sec. III.A.5.b, these schemes build on the concept of resonant "modulation-assisted tunneling" (Goldman et al., 2015), where a time-periodic modulation is set on resonance with respect to an intrinsic energy offset between neighboring sites. Cold-atom realizations of the Harper-Hofstadter model, using resonant moving optical potentials, were reported by Aidelsburger et al. (2013, 2015), Miyake et al. (2013), and Tai et al. (2017). More recently, a photonics implementation based on a circuit-QED architecture was described by Roushan et al. (2017b); see Fig. 30 and Sec. VII.B.

The simple topological characterization presented above for the high-frequency regime  $(\Omega \rightarrow \infty)$  breaks down when the period of the drive becomes comparable to other time scales in the problem (e.g., when  $\hbar \Omega$  becomes comparable to the bandwidth of the effective spectrum) (Kitagawa, Berg et al., 2010). Indeed, in that situation, the micromotion becomes crucial and the topological classification based on  $\hat{H}_{\mathrm{eff}}$  only must be revised (Kitagawa, Berg et al., 2010; Rudner et al., 2013; Carpentier et al., 2015; Nathan and Rudner, 2015). In particular, away from the high-frequency regime, topologically protected edge modes are shown to exist even when the topological invariants (e.g., Chern numbers) associated with  $\hat{H}_{\mathrm{eff}}$  are all trivial (Kitagawa, Berg et al., 2010; Rudner et al., 2013). The discovery of such anomalous Floquet topological phases suggested that novel types of topological invariants had to be introduced in order to accurately recover the bulk-edge correspondence in this regime. Such topological invariants (winding numbers) were identified by Kitagawa, Berg et al. (2010), Asbóth (2012), Rudner et al. (2013), Carpentier et al. (2015), Nathan and Rudner (2015), Bi et al. (2017b), and Yao, Yan, and Wang (2017) and were indeed shown to depend on the complete time-evolution operator  $\hat{U}(t, t_0)$ . The crucial role played by the micromotion in this topological characterization (Nathan and Rudner, 2015) indicates a shift of paradigm with respect to the standard topological classification of static systems.

As a final remark, we note that a fruitful approach to Floquet topological physics is offered by the so-called quantum walks (Broome et al., 2010; Kitagawa, Rudner et al., 2010; Kitagawa et al., 2012), where the time-evolution operator of a system is digitally built by repeatedly applying a series of unitary operations  $\hat{U}(T) = \hat{U}_M\hat{U}_{M-1}\dots \hat{U}_2\hat{U}_1$ . Because of the  $T$  periodicity of such quantum walks, their topological classification is equivalent to that of Floquet-engineered systems discussed above (Kitagawa, Rudner et al., 2010, 2012).

As we shall see at multiple places in the course of this review, photonic systems have shown a great potential to implement Floquet techniques in different platforms. This has led to the experimental realization of intriguing Floquet phases (Rechtsman, Zeuner, Plotnik et al., 2013; Bandres, Rechtsman, and Segev, 2016; Bellec et al., 2017; Noh, Huang, Leykam et al., 2017; Roushan et al., 2017b), in particular, anomalous Floquet topological states (F. Gao et al., 2016; Maczewsky et al., 2017; Mukherjee, Spracklen et al., 2017) and topologically protected states in quantum walks (Kitagawa et al., 2012; Cardano et al., 2017).

# B. Features of photonic systems

Historically, the study of topological effects in quantum condensed-matter systems originated from electric conduction experiments measuring the current versus voltage characteristics of two-dimensional electron gases. In these systems, the basic constituents, the electrons, obey Fermi statistics; the topologically nontrivial states arise as the equilibrium state for sufficiently low temperature; and the electric conductivity is measured under weak or moderate external fields that do not dramatically affect the underlying many-body state.

This equilibrium or quasiequilibrium condition is shared by almost all condensed-matter experiments, with a few remarkable exceptions such as Floquet topological insulators (Oka and Aoki, 2009; Inoue and Tanaka, 2010; Lindner, Refael, and Galitski, 2011; Cayssol et al., 2013) and light-induced superconductivity (Fausti et al., 2011). In these systems, new phases of matter are induced by intentionally keeping the system far away from equilibrium by means of some incident electromagnetic radiation.

The situation is fundamentally different in photonic systems for at least two fundamental reasons: (i) the basic constituent, the photon, possibly dressed by some matter excitation into a polariton, obeys bosonic statistics; and (ii) photons can reside in any realistic device only for a finite time and some external driving is needed to inject them into the system. In the next two sections we review the consequences of these remarkable differences. In the last section we review some basic concepts of nonlinear optics and illustrate how a third-order  $\chi^{(3)}$  nonlinearity can be seen as an effective binary interaction between photons, therefore opening the way toward many-body physics using gases of interacting photons (Carusotto and Ciuti, 2013).

# 1. Bosonic nature

As previously introduced, the first key difference between quantum condensed-matter systems, based on electron gases,

and photonic systems is that the basic constituents of the latter are bosonic. In Sec. II.A.2, we have seen how this difference can have an impact already at the single-particle level as Kramer's theorem, which underlies quantum spin Hall physics, holds only in the presence of fermionic time-reversal operators satisfying  $T^2 = -1$ .

At the many-body level, the difference between bosons and fermions is even more apparent as quantum statistics impose a specific symmetry on the many-body wave function under particle exchange: because of the Pauli exclusion principle, a noninteracting gas of fermions at low temperatures fills all states below the Fermi level with just one particle per state, while leaving all higher states empty. In the particular case of insulators, where the Fermi level lies within an energy gap, all valence (conduction) bands are filled (empty), so that integrals over the Brillouin zone naturally appear in the calculations. In contrast, a weakly interacting bosonic system at low temperatures consists of a Bose-Einstein condensate with a macroscopic population of particles accumulated in the single lowest-energy state (Huang, 1987; Pitaevskii and Stringari, 2016). As we see in the course of this section, the picture is made different in optical systems by the presence of losses and/or the propagating nature of photons, so that the ground state of the system is typically a trivial vacuum state: generating and maintaining the photon gas in a state with interesting topological properties then requires injecting light from some external source.

# 2. Nonequilibrium nature

In any realistic optical device, photons are typically subject to a variety of processes that tend to reduce the number of photons present in the device. Depending on the geometry and the materials used, these processes can range from absorptive losses in the underlying material medium, which make the photons simply disappear, to radiative losses and/or a finite propagation time through the system, which result in the emission of light in the surrounding space as propagating radiation. As a consequence, some external pumping mechanism must be introduced to inject and sustain the light field in the device. Except for very specific cases (Rasmussen et al., 2000; Silberberg et al., 2009; Klaers et al., 2010; Hafezi, Adhikari, and Taylor, 2015; Lebreuilly et al., 2017), the resulting state of the light field is thus quite distinct from a thermal equilibrium state.

Given this intrinsically nonequilibrium nature of photonic systems, the ways in which topological effects manifest, as well as the experimental probes and diagnostics that are available, can be completely different in photonic systems compared to condensed-matter setups. For example, the light emitted by the device carries out detailed information on the field distribution and the photon statistics inside the device. Depending on the specific setup, this information can be extracted by imaging the emission in free space, as is typical for planar microcavities, and/or by collecting the emission with local probes such as antennas or waveguides. Different ways of injecting light into the system have also been experimentally used to highlight different properties of topological states.

We now review the main such pumping schemes, highlighting the key general features of each. The impact of the

nonequilibrium condition on specific topological effects is then discussed throughout the following sections, e.g., on non-Hermitian topological photonics in Sec. VI, on the stabilization of many-body phases in Sec. VII.B, and on the measurement of topological invariants in Sec. VIII.C.

# a. Coherent pumping

In a typical coherent pumping scheme, the system is illuminated with an externally incident laser beam or by placing an antenna or an external waveguide in the system's vicinity, so as to inject coherent light at specific spatial locations. Light propagation through the system is then monitored by collecting transmitted and/or scattered light with a second antenna or a detector.

The conceptually simplest theoretical description of such an approach consists of solving Maxwell's equations, including the specific geometrical arrangement of dielectric and magnetic elements and suitable source terms to describe the emitting antenna. Since a complete analytical solution is typically beyond reach, a number of numerical methods have been developed for this task, ranging from the same plane wave expansions used to obtain the band structure, to finite element methods for the time evolution (Joannopoulos et al., 2011). Such techniques were for instance used in the theoretical calculations presented by Wang et al. (2009) and shown in Figs. 1(b), 1(c), and 1(e).

For nonbianisotropic materials with no magnetoelectric coupling, one can eliminate the magnetic field and write Maxwell's equation for a field oscillating at frequency  $\omega$  in the compact form (Wang et al., 2008; Joannopoulos et al., 2011)

$$
\nabla_ {\mathbf {r}} \times [ \boldsymbol {\mu} ^ {- 1} (\mathbf {r}) \nabla_ {\mathbf {r}} \times \mathbf {E} (\mathbf {r}) ] = \omega^ {2} \boldsymbol {\epsilon} (\mathbf {r}) \mathbf {E} (\mathbf {r}), \tag {34}
$$

where  $\mathbf{E}(\mathbf{r})$  is the electric field, and  $\pmb{\mu}(\mathbf{r})$  and  $\pmb{\epsilon}(\mathbf{r})$  are the magnetic permeability and dielectric permittivity tensors, respectively. The gyromagnetic photonic crystals used in the experiment (Wang et al., 2009) and illustrated in Figs. 1(a1) and 1(a2) were characterized by spatially periodic  $\pmb{\mu}(\mathbf{r})$  and  $\pmb{\epsilon}(\mathbf{r})$ , as well as nonvanishing nondiagonal elements of  $\pmb{\mu}$ , which quantify the strength of the gyromagnetic effect. Emission by an antenna can be straightforwardly included in the model just by adding source terms on the right-hand side (rhs) of Eq. (34).

In spatially periodic systems, a basis of solutions of Eq. (34) can be found which satisfies the Bloch theorem just like the Schrödinger equation for electrons in a periodic potential. In particular, these solutions are labeled by the crystal momentum  $\mathbf{k}$  and the band index  $n$  and the role of the Bloch wave function is played here by the electric field  $\mathbf{E}_{n,\mathbf{k}}(\mathbf{r})$ . For a given configuration, the specific form of the photonic Bloch bands and the Bloch wave functions can be obtained with standard photonic techniques reviewed by Joannopoulos et al. (2011).

Given the different form of the wave equation (34) compared to the Schrödinger equation, calculation of the topological invariants for photonic crystals requires some specific work beyond the picture presented in Sec. II.A for electronic systems. While the operator acting on  $\mathbf{E}(\mathbf{r})$  on the left-hand side (lhs) of Eq. (34) is still a Hermitian operator, the eigenvalue problem involves the dielectric permittivity  $\epsilon (\mathbf{r})$

multiplying on the right-hand side. It is then useful to consider the modified scalar product,

$$
\langle \mathbf {E} _ {1} | \mathbf {E} _ {2} \rangle = \int d ^ {2} \mathbf {r} \sum_ {i, j} E _ {1, i} ^ {*} (\mathbf {r}) \epsilon_ {i, j} (\mathbf {r}) E _ {2, j} (\mathbf {r}), \tag {35}
$$

where  $i,j = \{x,y,z\}$ . The Berry connection introduced in Eq. (5) then takes the form (Wang et al., 2008)

$$
\begin{array}{l} \mathcal {A} _ {n} (\mathbf {k}) = i \langle \mathbf {E} _ {n, \mathbf {k}} | \nabla_ {\mathbf {k}} \mathbf {E} _ {n, \mathbf {k}} \rangle \\ = i \int d ^ {2} \mathbf {r} \sum_ {i j} E _ {n, \mathbf {k}, i} ^ {*} (\mathbf {r}) \epsilon_ {i j} (\mathbf {r}) \nabla_ {\mathbf {k}} E _ {n, \mathbf {k}, j} (\mathbf {r}) \tag {36} \\ \end{array}
$$

in terms of the normalized Bloch eigenfunctions  $\mathbf{E}_{n,\mathbf{k}}(\mathbf{r})$  of the photon state of crystal momentum  $\mathbf{k}$  and band index  $n$ . Starting from Eq. (36) for the Berry connection, the geometrical and topological invariants such as the Berry curvature, the Chern number, and the bulk-boundary correspondence display the usual features as reviewed in Sec. II.A; in particular, as before, the Chern number can become nonzero only when the time-reversal symmetry is broken. Of course, equivalent geometrical and topological properties would be found if the Bloch wave function was written in terms of magnetic field after having eliminated the electric one.

While this ab initio technique can be applied in full generality to any photonic structure, a different strategy consists of developing simplified models that are able to capture the main physics, while, at the same time, providing some analytical insight as well as the possibility of extending to quantum optical features. The most celebrated such model, most suitable for discrete systems of coupled resonators, is inspired by the tight-binding picture of solid-state physics (Ashcroft and Mermin, 1976) and is naturally expressed in a quantum language. In the classical optics and photonics literature, it often goes under the name of coupled mode theory, as reviewed by Haus and Huang (1991).

The starting point is an expansion of the electromagnetic field

$$
\mathbf {E} (\mathbf {r}) = \sum_ {j} \mathbf {E} _ {j} (\mathbf {r}) \hat {a} _ {j} + \mathbf {E} _ {j} ^ {*} (\mathbf {r}) \hat {a} _ {j} ^ {\dagger} \tag {37}
$$

onto a basis of localized quantized modes labeled (in the simplest case of single-mode resonators) by the site index  $j$ . The suitably normalized mode profiles  $\mathbf{E}_j(\mathbf{r})$  are obtained as the eigenmodes of Maxwell's equations of eigenfrequency  $\omega_j$ , and the quantum  $\hat{a}_j$  and  $\hat{a}_j^\dagger$  operators, respectively, destroy or create a photon in each resonator  $j$  and satisfy Bose statistics, that is,  $[\hat{a}_j, \hat{a}_{j'}] = 0$  and  $[\hat{a}_j, \hat{a}_{j'}^\dagger] = \delta j, j'$ .

The corresponding Hamiltonian has the form of a collection of independent harmonic oscillators in which tunneling between neighboring sites  $j^{\prime}\rightarrow j$  can be straightforwardly included as hopping terms of amplitude  $J_{j,j'}$ ,

$$
H _ {\mathrm {r e s}} = \sum_ {j} \hbar \omega_ {j} \left[ \hat {a} _ {j} ^ {\dagger} \hat {a} _ {j} + \frac {1}{2} \right] - \sum_ {j, j ^ {\prime}} J _ {j, j ^ {\prime}} \hat {a} _ {j} ^ {\dagger} \hat {a} _ {j ^ {\prime}}. \tag {38}
$$

Pioneering examples of the application of this tight-binding formalism are found in Yariv et al. (1999) and Bayindir, Temelkuran, and Ozbay (2000). If the hopping amplitudes  $J_{j,j'}$  can be made complex, photons behave as if they are experiencing a synthetic magnetic vector potential. The site dependence of the resonator frequency  $\omega_j$  can model an external potential acting on photons.

The main difference between photonic systems and the usual solid-state ones is that photons can radiate away from the resonators into the surrounding empty space, e.g., through the nonperfectly reflecting cavity mirrors. At the level of the Hamiltonian (38), this requires the inclusion of a continuum of radiative modes  $\hat{A}_{\eta}$ , labeled by the index  $\eta$  and satisfying Bose commutation relations. These modes are linearly coupled to the localized resonator modes via terms of the form

$$
\begin{array}{l} H = H _ {\mathrm {r e s}} + \int d \eta \hbar \omega_ {\eta} \hat {A} _ {\eta} ^ {\dagger} \hat {A} _ {\eta} + \\ - \sum_ {j} \int d \eta \left[ \hbar g _ {j, \eta} \hat {A} _ {\eta} ^ {\dagger} \hat {a} _ {j} + \mathrm {H . c .} \right], \tag {39} \\ \end{array}
$$

where  $\omega_{\eta}$  is the frequency of a given radiative mode  $\eta$  and  $g_{j,\eta}$  is the coupling between that radiative mode and the resonator mode  $j$ . As discussed in full detail in quantum optics textbooks (Walls and Milburn, 2006), this Hamiltonian is the starting point of the so-called input-output formulation of the cavity field dynamics in terms of a quantum Langevin equation (Gardiner and Collett, 1985). Under the simplifying assumptions that the different resonators are coupled to independent continua of radiative modes with an approximately constant spectral weight within the frequency range of interest, one can write

$$
i \frac {d \hat {a} _ {j}}{d t} = \omega_ {j} \hat {a} _ {j} - \sum_ {j ^ {\prime}} J _ {j, j ^ {\prime}} \hat {a} _ {j ^ {\prime}} - \frac {i \gamma_ {j}}{2} \hat {a} _ {j} + \hat {A} _ {j} ^ {\mathrm {i n}} (t), \tag {40}
$$

where the radiative damping rate

$$
\gamma_ {j} = 2 \pi | g _ {j, \eta} | ^ {2} \left| \frac {d \omega_ {\eta}}{d \eta} \right| ^ {- 1} \tag {41}
$$

has to be evaluated for the resonant radiative mode such that  $\omega_{\eta} = \omega_{j}$  and the bosonic input operators

$$
\hat {A} _ {j} ^ {\text {i n}} (t) = - \int d \eta g _ {j, \eta} ^ {*} \hat {A} _ {\eta} \tag {42}
$$

include the zero-point quantum noise as well as the incident radiation.

The model can of course be straightforwardly extended to account for loss channels of nonradiative origin. More complex configurations may require including more field components on each site to describe multimode cavities: dissipative terms of different forms, e.g., a nondiagonal damping matrix  $\gamma_{j,j'}$  to describe simultaneous coupling of several sites to the same continuum (Harris, 1989; Chen, Yin, and Elliott, 1990; Cohen-Tannoudji, Dupont-Roc, and

Grynberg, 2008; Ghulinyan et al., 2014), and/or light amplification processes by population-inverted emitters (Gardiner and Zoller, 2004; Walls and Milburn, 2006).

In the most relevant case of a coherent incident field and a quadratic resonator Hamiltonian  $H_{\mathrm{res}}$ , we can replace the operators with  $\mathbb{C}$ -number-valued expectation values  $\alpha_{j}$  that evolve according to the ordinary differential equations

$$
i \frac {d \alpha_ {j}}{d t} = \omega_ {j} \alpha_ {j} - \sum_ {j ^ {\prime}} J _ {j, j ^ {\prime}} \alpha_ {j ^ {\prime}} - \frac {i \gamma_ {j}}{2} \alpha_ {j} + F _ {j} (t), \tag {43}
$$

where the source term  $F_{j}(t) = \langle \hat{A}_{j}^{\mathrm{in}}(t)\rangle$  corresponds to the classical amplitude of the incident field. Techniques to efficiently evaluate the tight-binding parameters from classical transmission and reflection calculations are discussed, e.g., by Hafezi et al. (2011) for coupled ring resonator arrays. More details on other specific systems can be found, e.g., in Bellec et al. (2013a) for microwave resonators, Kruk et al. (2017) for dielectric nanoparticles, and Poddubny et al. (2014) and Downing and Weick (2017) for plasmonic chains. Generalization to spatially continuous systems such as planar microcavities is reviewed by Carusotto and Ciuti (2013).

Apart from the last two terms describing driving and dissipation, this equation (43) has exactly the same form as the Schrödinger equation for noninteracting tight-binding electrons, where the field amplitude  $\alpha_{j}$  plays the role of the discrete electron wave function. This formal equivalence between equations allows one to simulate the single-particle properties of tight-binding models using photonics.

Depending on the specific spatiotemporal shape of the coherent drive  $F_{j}(t)$ , the motion equation (43) can be used to describe various different phenomena such as the time-dependent response to a pulsed excitation or the nonequilibrium steady state under a monochromatic excitation. As a general rule, a coherent drive selectively excites only those modes that are on or close to resonance with the pump frequency spectrum and that have a significant overlap with the pump profile.

For instance, when a monochromatic pump is shone on the bulk of the system, the injected light intensity dramatically depends on whether its frequency corresponds to an allowed energy band or to a band gap. On resonance with a band, a spatially extended and periodic pump can selectively excite Bloch states with specific  $k$  (Bardyn, Huber, and Zilberberg, 2014), while a spatially localized pump generates an outward propagating field up to distances roughly proportional to the group velocity of the excited modes over the total photon decay rate (Ozawa and Carusotto, 2014). Within a forbidden gap, no propagating state is instead available and the spatial light intensity profile will show a sharp exponential decay, typically determined by the distance to the nearest band edge.

When the pump is focused on a system edge, pumping in an energy band will result in light penetrating into the bulk, while pumping in a band gap will concentrate the excitation on edge states, if available. Of course, different modes can be selectively excited by playing with the spatial and/or polarization shape and symmetry of the pump spot.

In more complex geometries, the frequency selectivity of a coherent pump has been used to selectively excite specific

localized modes, ranging from the Landau levels in the nonplanar ring cavity of Schine et al. (2016) to complex Penrose tiling geometries (Vignolo et al., 2016), an approach which may be extended to explore a variety of other interesting cases, including, e.g., the relativistic Landau levels of strained honeycomb lattices and the momentum-space Landau levels that appear under a harmonic confinement, as theoretically studied by, respectively, Salerno et al. (2015) and Berceanu et al. (2016).

# b. Incoherent pumping

Photoluminescence experiments using incoherent pumping are a straightforward but powerful tool to visualize the energy distribution and the structure of the eigenstates of a system. In particular, this approach is routinely used in planar microcavity devices. Using this technique, states in a specific energy range can be isolated by spectrally resolving the emission, and then near- or far-field images recover the spatial profile or the  $k$ -space momentum distribution of modes. In the topological photonics context, this technique was used, e.g., to visualize the relativistic Dirac-like dispersion in honeycomb lattices (Jacqmin et al., 2014) and the corresponding edge states (Milicevic et al., 2015, 2017).

Typical photoluminescence experiments are performed in a low pump power regime where the emission occurs spontaneously and is distributed fairly uniformly across all modes. Ramping up the pump power, experiments can enter a regime where bosonic stimulation and then mode-competition effects conspire to concentrate the emission into a reduced number of modes. For high enough pump power, above the so-called lasing threshold, stimulated emission exceeds losses and a new kind of steady state is achieved: in this state, a strong and coherent light intensity is concentrated into a single mode, which absorbs all pump power and which has an emission linewidth that is dramatically reduced (Gardiner and Zoller, 2004; Walls and Milburn, 2006).

As a rule of thumb, the lasing mode is typically selected by the largest gain condition; attention must however be paid to complex spatial mode deformation effects due to interplay of gain with the nonlinearity and the gain saturation (Tureci, Stone, and Ge, 2007), such as ballistic outward flows (Richard et al., 2005; Wouters, Carusotto, and Ciuti, 2008; Wertz et al., 2010) or solitoniclike self-bound modes (Tanese et al., 2013; Jacqmin et al., 2014). In the topological photonics context, in spite of these complications, ramping the pump power above lasing threshold has been instrumental in resolving small spin-orbit coupling effects in hexagonal chains of micropillar resonators (Sala et al., 2015; Carlon Zambon et al., 2018). On-going advances in topological lasing will be outlined in the concluding Sec. VIII.

# c. Propagating geometries

While both previous schemes are based on a driven-dissipative evolution of the light field, the conservative dynamics of light flowing through so-called "propagating geometries" has been exploited in a number of recent breakthrough experiments in topological photonics, starting from the realization of topological quantum walks in Kitagawa et al. (2012) to Floquet topological insulators in coupled waveguide systems

in Rechtsman, Zeuner, Plotnik et al. (2013) and Berry-phase-induced anomalous transport in Wimmer et al. (2017). Well before these advances, such propagating geometries had already been used to realize a variety of novel phenomena, e.g., spatial lattice solitons (Efremidis et al., 2002; Christodoulides, Lederer, and Silberberg, 2003; Fleischer et al., 2003), two-dimensional Anderson localization (Schwartz et al., 2007; Lahini et al., 2008), and wave dynamics in quasicrystals (Freedman et al., 2006, 2007; Levi et al., 2011; Verbin et al., 2013). All these experiments are based on purely classical properties of light and do not involve any quantum optical feature.

A convenient theoretical description of classical monochromatic light in these systems is based on paraxial diffraction theory (Yariv, 1976; Rosanov, 2002; Boyd, 2008). We start from classical Maxwell's wave equation for light propagating in a source-free, nonmagnetic material of (spatially dependent) dielectric constant  $\varepsilon = \varepsilon(x,y,z)$ :

$$
\nabla \times \nabla \times \mathbf {E} = \varepsilon \left(\frac {\omega}{c}\right) ^ {2} \mathbf {E}, \tag {44}
$$

where  $\mathbf{E}$  is the electric field,  $\omega$  is the light frequency, and  $c$  is the speed of light in vacuum. Using a standard vector identity and the fact that  $\nabla \cdot (\varepsilon \mathbf{E}) = 0$ , we arrive at

$$
- \nabla^ {2} \mathbf {E} = \varepsilon \left(\frac {\omega}{c}\right) ^ {2} \mathbf {E} + \nabla \left(\mathbf {E} \cdot \frac {\nabla \varepsilon}{\varepsilon}\right). \tag {45}
$$

Assuming that the dielectric constant  $\varepsilon(x,y,z) = \varepsilon_0 + \Delta \varepsilon(x,y,z)$  displays relatively small variations from the background value  $\varepsilon_0 = n_0^2$ , and that the length scale of the spatial variation is large compared to the wavelength  $\lambda_0 = 2\pi / k_0 = 2\pi c / n_0\omega$  in the medium, we can neglect the last term coupling the polarization and the orbital degrees of freedom and assume that the two polarizations evolve independently according to a scalar equation. In the experiment of Rechtsman, Zeuner, Plotnik et al. (2013),  $\varepsilon$  varies by  $\Delta \varepsilon \sim 10^{-3}$  on a length scale  $\sim 10\lambda_0$ .

We further assume that light is made to propagate along paraxial directions close to the axis of the waveguides (denoted as the positive  $z$  direction). This guarantees that the wave vector component in the  $z$  direction must be much greater than those in the  $x$  and  $y$  directions ( $k_{0} \simeq k_{z} \gg k_{x,y}$ ). This suggests to write the electric field in the carrier-envelope form

$$
\mathbf {E} (x, y, z) = \hat {\mathbf {e}} \tilde {E} (x, y, z) \exp [ i k _ {0} z ], \tag {46}
$$

where  $\hat{\mathbf{e}}$  is the unit vector in the direction of polarization and  $\tilde{E}$  is a slowly varying function satisfying  $|\nabla \tilde{E} |\ll |k_0\tilde{E} |$ . Plugging this expression into the propagation equation (45), we find that

$$
- \partial_ {z} ^ {2} \tilde {E} - 2 i k _ {0} \partial_ {z} \tilde {E} - \nabla_ {\perp} ^ {2} \tilde {E} + k _ {0} ^ {2} \tilde {E} = \varepsilon \left(\frac {\omega}{c}\right) ^ {2} \tilde {E}, \tag {47}
$$

where the  $\nabla_{\perp}$  operator acts on the transverse  $(x,y)$  plane. We now use the fact that  $\tilde{E}$  varies slowly in the  $z$  direction to

neglect the  $\partial_z^2\tilde{E}$  term from Eq. (47). Using for convenience the refractive index  $n = \sqrt{\varepsilon} = n_0 + \Delta n\simeq n_0 + \Delta \varepsilon /(2n_0)$ , we arrive at the paraxial equation for the diffraction of light through the structure:

$$
i \partial_ {z} \tilde {E} = - \frac {1}{2 k _ {0}} \nabla_ {\perp} ^ {2} \tilde {E} - \frac {k _ {0} \Delta n}{n _ {0}} \tilde {E}. \tag {48}
$$

For a strong enough confinement within the waveguides, the usual tight-binding approximation (Ashcroft and Mermin, 1976) can be performed on the paraxial equation (48), which leads to evolution equations for the field amplitude  $\alpha_{j}$  in each waveguide of the form

$$
i \frac {d \alpha_ {j}}{d z} = k _ {j} ^ {z} \alpha_ {j} - J _ {j, j ^ {\prime}} \alpha_ {j ^ {\prime}}, \tag {49}
$$

where the wave vector  $k_{j}^{z}$  of light propagating inside the waveguide  $j$  is determined by the background index  $n_0$  as well as by the lateral confinement length, while the tunneling matrix  $J_{j,j'}$  depends on the overlap of the evanescent tails of  $j$ ,  $j'$  modes.

The formal similarity of the paraxial propagation equation (48) with the Schrödinger equation of quantum mechanics establishes a close analogy between the diffraction of classical light and the motion of a spinless massive quantum particle, where the diffraction along the  $x - y$  plane sets the particle mass and the refractive index modulation gives the external potential. Note, however, that the role of the temporal coordinate is played here by the propagation direction  $z$ , whose spatial derivative replaces on the lhs of Eq. (48) the usual temporal  $t$  derivative of the Schrödinger equation. As a result, the Floquet approach discussed in Sec. II.A.5 can be implemented in propagating geometries by spatially modulating system properties along the  $z$  direction, as experimentally pioneered by Rechtsman, Zeuner, Plotnik et al. (2013) and reviewed here in Sec. III.A.2.

Going beyond the assumption of monochromaticity, the propagating light can have nontrivial temporal dynamics, such that the physical time  $t$  becomes like a third spatial coordinate, in addition to the  $x, y$  transverse coordinates, and the propagation equation for the slowly varying field  $\tilde{E}(\mathbf{r}, t; z)$  must include an additional kinetic energy term with respect to the temporal direction,

$$
i \frac {\partial \tilde {E}}{\partial z} = - \frac {1}{2 k _ {0}} \nabla_ {\perp} ^ {2} \tilde {E} - \frac {k _ {0} \Delta n}{n _ {0}} \tilde {E} - \frac {1}{2 m _ {t}} \frac {\partial \tilde {E}}{\partial t ^ {2}} \tag {50}
$$

whose masslike coefficient  $m_t^{-1} \equiv -d^2 k / d\omega^2$  [with  $k(\omega) = \omega n(\omega) / c$ ] is proportional to the group velocity dispersion in the medium of frequency-dependent refractive index  $n(\omega)$  (Boyd, 2008).

In order to go beyond the classical light case considered in the above equations, theoretical works (Lai and Haus, 1989a, 1989b; Larre and Carusotto, 2015) have developed a full quantum theory to map the light propagation of quasimonochromatic quantum light onto a standard many-body theory of interacting bosons. In the near future, this reformulation may

be useful in studying the interplay of quantum fluctuations, strong nonlinearities, and topological effects.

As a consequence of the exchanged roles of the  $z$  coordinate and the physical time  $t$ , radiation that propagates through such a device does not provide a real-time monitoring of the field evolution, as is usual for the cavity systems discussed above, but the light that exits from the back interface only offers access to the field state at the end point of the evolution. Correspondingly, extracting spectral information about eigenmodes requires the inclusion of additional elements, such as an extra one-dimensional chain of waveguides that can be used to selectively inject light at one side of the system, according to a  $k_z$  resonance condition (Noh, Huang, Chen, and Rechtsman, 2018). Analogously, the role of the incident field on the front interface of the device is only to set the initial condition of the evolution. The counterpart of these limitations is that such propagating geometries allow us to study time-dependent problems with conservative dynamics, extending in the long run even to quantum many-body physics (Polkovnikov et al., 2011; Larre and Carusotto, 2016).

From an experimental point of view, focusing on works related to topological photonics, it is worth noting that a discrete version of the position-to-time mapping was exploited by Schreiber et al. (2012) to obtain a 2D analog quantum walk by encoding two extra spatial variables in the arrival time of optical pulses. A related quantum walk was used in the experiment (Wimmer et al., 2017) to reconstruct the geometrical Berry curvature of a photonic lattice model from anomalous transport features.

# 3. Basics of nonlinear optics

We conclude this section by reviewing the main aspects of photonic systems with a brief summary of the key concepts of nonlinear optics. In view of the ongoing developments toward the realization of strongly correlated many-photon states in strongly nonlinear systems, as reviewed in Sec. VII.B, we will pay special attention to the reformulation of  $\chi^{(3)}$  Kerr nonlinearities in terms of a binary interaction between photons.

The standard semiclassical description of nonlinear optical processes is based on Maxwell's equations, including nonlinear terms resulting from the nonlinear dependence of the dielectric polarization on the applied field (Boyd, 2008; Butcher and Cotter, 2008). In the most naive form, this reads

$$
P = \chi^ {(1)} E + \chi^ {(2)} E ^ {2} + \chi^ {(3)} E ^ {3} + \dots , \tag {51}
$$

where the linear electric susceptibility  $\chi^{(1)}$  is responsible for the usual refractive index; the second-order susceptibility  $\chi^{(2)}$  gives rise, e.g., to second harmonic generation, optical rectification, and parametric downconversion processes; and the third-order susceptibility  $\chi^{(3)}$  leads to four-wave mixing processes as well as an intensity-dependent refractive index. In the simplest form, this last effect can be reformulated as

$$
n (\mathbf {r}) = n _ {0} + n _ {\mathrm {n l}} | \mathbf {E} (\mathbf {r}) | ^ {2}, \tag {52}
$$

where  $n_0$  is the refractive index in the linear regime, and the  $n_{\mathrm{nl}}$  coefficient, proportional to the  $\chi^{(3)}$  susceptibility,

quantifies the refractive index dependence on the local light intensity.

From the point of view of photons as quantum mechanical particles, such an intensity-dependent refractive index can be reinterpreted in terms of binary interactions between photons, which are mediated by the nonlinear polarization of the underlying medium. This picture of interacting photons was pioneered in the calculation of the effective  $\chi^{(3)}$  third-order nonlinear polarizability of the vacuum arising from the exchange of a virtual electron-positron pair (Heisenberg and Euler, 1936; Karplus and Neuman, 1951), as sketched in the Feynman diagram for photon-photon scattering shown in Fig. 8. Given the large mass  $m_e$  of electrons and positrons as compared to the optical energies, the low-energy cross section of such processes

$$
\sigma \propto \alpha^ {4} \left(\frac {\hbar}{m _ {e} c}\right) ^ {2} \left[ \frac {\hbar \omega}{m _ {e} c ^ {2}} \right] ^ {6} \tag {53}
$$

is very low in vacuo: in the  $\sigma \approx 10^{-68} \mathrm{~m}^2$  range for  $1 \mathrm{eV}$  optical photons. This has made the experimental observation of this physics in vacuo extremely challenging. Given the  $(\hbar \omega)^{6}$  dependence of the scattering cross section, the most natural strategy is to use high energy photons, e.g., in the  $\gamma$ -ray range. The first experimental observation of photon-photon scattering using the electromagnetic fields surrounding ultra-relativistic colliding ions was recently reported by Aaboud et al. (2017).

As compared to the vacuum, condensed-matter media offer the much more accessible option of replacing electron-positron pairs of MeV-ranged mass  $m_{e}$  with electron-hole pairs of eV-ranged rest mass (set by the band gap of the material). According to Eq. (53) the corresponding reduction of the intermediate-state detuning provides a dramatic reinforcement of the cross section by  $\approx 36$  orders of magnitude. This corresponds to a significant value of the nonlinear  $\chi^{(3)}$  polarizability in Eq. (51), which leads to many nonlinear optical phenomena, including the intensity-dependent refractive index of Eq. (52), two-photon absorption, and parametric amplification or oscillation, etc. (Boyd, 2008; Butcher and Cotter, 2008).

Beyond the basic Feynman diagram sketched in Fig. 8, more complex configurations arising in specific materials may offer interesting advantages to experiment, e.g., when photons are dressed by optical transitions in discrete emitters (Noh and Angelakis, 2017) or excitons in solid-state materials (Ciuti et al., 1998), when the collision process occurs via a

![](images/1da956dc8acfb110b0b3462ef0e64e06d7be0fd1b4d8529f6279b4cab3fa6f63.jpg)  
FIG. 8. QED Feynman diagram contributing to photon-photon scattering in vacuum via creation of a virtual electron-positron pair. Wavy lines represent photons and directed arrows represent electrons and positrons.

long-lived biexcitonic bound state (Wouters, 2007; Carusotto, Volz, and Imamoğlu, 2010; Takemura et al., 2014), or when the nonlinearity inherits the long-range character of the interactions between Rydberg states in solid-state (Kazimierczuk et al., 2014) or gaseous media (Saffman, Walker, and Mølmer, 2010; Chang, Vuletic, and Lukin, 2014).

In most media, the third-order  $\chi^{(3)}$ , introduced in Eq. (51), can however be viewed in the many-body language as the result of simple two-photon collisions. This alternative perspective shines new light on basic nonlinear optical phenomena from a novel angle and allows to take advantage of the artillery of many-body techniques originally developed in the context of condensed-matter and nuclear physics to predict new optical effects. In the last decade, the resulting concept of quantum fluids of light (Carusotto and Ciuti, 2013) has led to the experimental observation of a remarkable number of many-body effects in weakly interacting gases of photons, such as Bose-Einstein condensation, superfluidity, and quantum hydrodynamics, etc.

Under the simplifying assumptions that the frequency dependence of  $\chi^{(3)}$  is negligible and that the rotating-wave approximation can be performed, the real part of  $\chi^{(3)}$  provides an interaction Hamiltonian

$$
\hat {H} _ {\text {i n t}} = \frac {g ^ {(3)}}{2} \int d ^ {3} \mathbf {r} \hat {E} ^ {\dagger} (\mathbf {r}) \hat {E} ^ {\dagger} (\mathbf {r}) \hat {E} (\mathbf {r}) \hat {E} (\mathbf {r}), \tag {54}
$$

which is quartic in the electric field operators  $\hat{E} (\mathbf{r})$  and where the amplitude  $g^{(3)}$  is proportional to the real part of the  $\chi^{(3)}$  nonlinearity. The imaginary part gives instead two-body losses from two-photon absorption. The assumption of a spatially and temporally local polarization response of the medium to the applied electric field medium that underlies Eq. (54) is valid in most common silicon- or silica-based materials used for topological photonics in the infrared and visible range (Hafezi et al., 2013; Rechtsman, Zeuner, Plotnik et al., 2013), as well as in Jaynes-Cummings-type lattices embedding strongly detuned emitters (Hoffman et al., 2011; Fitzpatrick et al., 2017). Nonetheless, one must not forget that several other experiments make use of thermal (Vocke et al., 2015), photo refractive (Fleischer et al., 2003; Jia and Fleischer, 2009), or Rydberg-mediated nonlinearities (Saffman, Walker, and Mølmer, 2010; Chang, Vuletic, and Lukin, 2014), whose response may be slow in time and/or long range in space due to heat and charge diffusion effects and to the inherently long-range nature of dipole interactions.

From a quantitative point of view, it is crucial to keep in mind that the optical nonlinearity of most commonly used materials results in very weak interactions between single photons, so that an accurate theoretical description is provided by a mean-field approach. Under this approximation, high-order averages are split into products of the mean field, e.g.,

$$
\langle \hat {E} ^ {\dagger} (\mathbf {r}) \hat {E} (\mathbf {r}) \hat {E} (\mathbf {r}) \rangle \simeq \langle \hat {E} ^ {\dagger} (\mathbf {r}) \rangle \langle \hat {E} (\mathbf {r}) \rangle \langle \hat {E} (\mathbf {r}) \rangle , \tag {55}
$$

and the Heisenberg equation of motion for the field expectation value  $E(\mathbf{r}) = \langle \hat{E} (\mathbf{r})\rangle$  recovers the classical Maxwell's equations including a nonlinear polarization term Eq. (51). Of course, the extremely small intensity of single-photon

nonlinear effects does not preclude that a huge number of photons can collectively have a dramatic impact on the macroscopic optical response to a strong light beam.

Within the mean-field approximation Eq. (55), an intensity-dependent refractive index can be included in the classical equations of motion (43) of the tight-binding formalism described in the previous Sec. II.B.2, by simply adding to the rhs of the motion equation for  $\alpha_{j}$  an additional term of the form

$$
+ \omega_ {\mathrm {n l}} | \alpha_ {j} | ^ {2} \alpha_ {j}, \tag {56}
$$

where the nonlinearity parameter  $\omega_{\mathrm{nl}}$  is proportional (with an opposite sign) to the real part of the  $\chi^{(3)}$  nonlinearity and, typically, inversely proportional to the spatial volume of the optical mode under consideration (Carusotto and Ciuti, 2013). In propagating geometries, instead, an interaction term of the form

$$
- \frac {k _ {0} n _ {\mathrm {n l}}}{n _ {0}} | \tilde {E} (\mathbf {r}) | ^ {2} \tilde {E} (\mathbf {r}) \tag {57}
$$

has to be added to the right-hand side of the paraxial propagation equation (48) for monochromatic light, which then takes the form of a Gross-Pitaveskii equation of dilute Bose-Einstein condensates (Pitaevskii and Stringari, 2016). In both cases, a nonvanishing imaginary part of  $\chi^{(3)}$  and  $n_{\mathrm{nl}}$  in Eqs. (56) and (57) can be included to model saturable absorption, two-photon absorption, or gain saturation effects.

Going beyond the mean-field regime and realizing strongly correlated photon states requires very special materials with extremely strong nonlinearities. Finding such materials is one of the most active research lines in modern nonlinear optics (Carusotto and Ciuti, 2013; Chang, Vuletic, and Lukin, 2014; Roy, Wilson, and Firstenberg, 2017). So far, the most exciting results have been obtained using polaritons in gases of coherently driven atoms with electromagnetically induced transparency (EIT) in Rydberg states (Gorshkov et al., 2011; Peyronel et al., 2012; Firstenberg et al., 2013)-the so-called Rydberg polaritons-or circuit-QED devices, where microwave cavity photons are strongly coupled to a superconducting qubit element (Schoelkopf and Girvin, 2008; You and Nori, 2011; Houck, Tureci, and Koch, 2012; Gu et al., 2017). Even though a complete and quantitative account of the complex features of these optical nonlinearities calls for a more sophisticated theoretical description of the interactions between Rydberg polaritons (Bienias et al., 2014; Jachymski, Bienias, and Buchler, 2016) and of the Josephson dynamics in circuit-QED devices (Bourassa et al., 2012), the simplest form (54) of the interaction Hamiltonian is typically sufficient to capture the main physics.

The quantum Langevin equation for the cavity field dynamics Eq. (40) is also straightforwardly extended to interacting regimes by adding a two-photon interaction term

$$
H _ {\mathrm {n l}} = \sum_ {j} \frac {\hbar \omega_ {\mathrm {n l}}}{2} \hat {a} _ {j} ^ {\dagger} \hat {a} _ {j} ^ {\dagger} \hat {a} _ {j} \hat {a} _ {j}, \tag {58}
$$

to the resonator Hamiltonian  $H_{\mathrm{res}}$ . Actual calculations are often simpler to perform by recasting the input-output

formalism in terms of a master equation for the density matrix  $\hat{\rho}$ . For a coherent drive, the driving and dissipation terms have the form

$$
\begin{array}{l} \frac {d \hat {\rho}}{d t} = - \frac {i}{\hbar} \left[ \hat {H} _ {\mathrm {r e s}} + H _ {\mathrm {n l}} + \sum_ {j} F _ {j} (t) \hat {a} _ {j} ^ {\dagger} + F _ {j} ^ {*} (t) \hat {a} _ {j}, \hat {\rho} \right] \\ + \sum_ {j} \frac {\gamma_ {j}}{2} \left[ 2 \hat {a} _ {j} \hat {\rho} \hat {a} _ {j} ^ {\dagger} - \hat {a} _ {j} ^ {\dagger} \hat {a} _ {j} \hat {\rho} - \hat {\rho} \hat {a} _ {j} ^ {\dagger} \hat {a} _ {j} \right]. \tag {59} \\ \end{array}
$$

Generalization of this approach to incoherent pumps, as discussed in Sec. II.B.2, can be found in quantum optics textbooks (Gardiner and Zoller, 2004; Walls and Milburn, 2006).

As introduced in Sec. II.B.2, a quantum description of light propagation in the propagating geometries crucially requires going beyond the monochromatic light assumption. Among many recent developments in this direction (Gorshkov et al., 2011; Petrosyan, Otterbach, and Fleischhauer, 2011; Bienias et al., 2014; Maghrebi, Gullans et al., 2015; Moos et al., 2015; Gullans et al., 2016), a particularly promising theoretical approach is based on a quantum version of the  $t - z$  mapping. As discussed by Lai and Haus (1989a, 1989b) and Larre and Carusotto (2015), this reformulation leads to a model of interacting bosons, again with the physical roles of time  $t$  and propagation coordinate  $z$  exchanged.

# III. TOPOLOGICAL PHOTONICS IN TWO DIMENSIONS

Having reviewed basic ideas of topological physics and optical and photonic systems in the previous section, we are now in the position to dive into the exciting recent advances of topological photonics. Taking inspiration from the well-known classification of electronic topological insulators (Chiu et al., 2016), the next sections are organized according to the dimensionality and symmetry class to which each topological system belongs.

The present section is focussed on two-dimensional systems, starting from the analog quantum Hall systems that sparked the whole field of topological photonics. In the following sections we then move to quantum spin Hall systems, anomalous Floquet insulators, and, finally, gapless systems such as honeycomb lattices. For each class, we present the principal material platforms that have been developed and the main topological effects that each system has been able to observe.

# A. Analog quantum Hall systems in photonics

In this first section we review two-dimensional photonic systems in which time-reversal symmetry is explicitly broken, so that the topology can be classified in terms of the integervalued (first) Chern number. These systems can be considered as direct photonic analogs of integer quantum Hall states of a two-dimensional electron gas in the presence of an out-of-plane magnetic field.

Our attention is focused on those optical platforms that have led to major experimental advances in the field, namely, gyromagnetic photonic crystals and arrays of coupled waveguides, but we briefly discuss also other platforms that have been theoretically proposed and are presently under

experimental investigation. While most of the experiments focused on the chiral edge modes and the resulting topologically protected one-way propagation, we conclude by briefly reviewing theoretical work in the direction of measuring geometrical and topological properties of the bulk.

# 1. Gyromagnetic photonic crystals

In a nutshell, photonic crystals (Joannopoulos et al., 2011) consist of a spatially periodic arrangement of material elements giving spatially periodic dielectric permittivity  $\epsilon_{ij}(\mathbf{r})$  and magnetic permeability  $\mu_{ij}(\mathbf{r})$  tensors. In such a geometry, one can apply to photons the Bloch theorem originally developed in solid-state physics for electrons in crystalline solids (Ashcroft and Mermin, 1976): photon states organize themselves in allowed bands separated by forbidden gaps and are labeled by their wave vector defined within the first Brillouin zone of the periodic lattice.

Most of the early literature on photonic crystals focused on the possibility of realizing a complete photonic band gap (John, 1987; Yablonovitch, 1987) that could, e.g., suppress spontaneous emission on embedded emitters and, in the presence of defects in the otherwise crystalline order, create strongly localized states. The study of such in-gap states gave rise to a number of exciting developments in view of photonic applications such as high-  $Q$  photonic crystal cavities (Noda, 2016), high-performance, low-noise semiconductor lasers (Painter et al., 1999), and low-loss-waveguides insensitive to bends (Mekis et al., 1996; Lin et al., 1998; Yariv et al., 1999; Bayindir, Temelkuran, and Ozbay, 2000). On the other hand, propagating band states regained major attention when it was realized that photonic bands are not completely characterized by their energy dispersion, but also encode geometrical and topological features, which could lead to photonic analogs of the electronic quantum Hall effect (Haldane and Raghu, 2008).

The seminal proposal of Haldane and Raghu focused on the case of a gyroelectric photonic crystal where a pair of Dirac cones are gapped under a static magnetic field which breaks the time-reversal symmetry (Haldane and Raghu, 2008; Raghu and Haldane, 2008). Soon after, this was followed by a realistic design of a gyromagnetic photonic crystal operating at microwave frequencies and displaying a Chern number of 1 (Chong, Wen, and Soljacic, 2008; Wang et al., 2008). The basic formalism, such as how to define the Berry curvature of photonic bands, was reviewed in Sec. II.B.2.

Experiments (Wang et al., 2009) were performed using the material platform sketched in Fig. 1(a), namely, a periodic array of ferrite rods of vanadium-doped calcium-iron garnet, a material that under a static magnetic field shows strong gyromagnetic properties encoded in the nondiagonal matrix elements of the magnetic tensor  $\mu_{ij}$ . The theoretical dispersion of photonic energy bands for such a system is displayed in Fig. 1(e), which includes labels indicating the Chern number of the different bands.

In the experiment, the photonic crystal slab had of course a finite spatial size and was bounded by a metal wall on one side: since the reflecting gap of the surrounding metal has a topologically trivial nature, the bulk-boundary correspondence predicts that a topologically protected chiral edge mode

appears within the bulk energy gaps of the photonic crystal, as indicated by the red line in the dispersion plot in Fig. 1(e). Since time-reversal symmetry is broken by the external magnetic field, the number of edge states in each gap and their direction of propagation is determined by the sum of the Chern numbers of all lower-lying bands.

The main phenomenological consequence of such chiral edge states is that they support propagation in one direction only, so that backscattering from defects and scatterers is completely suppressed independently of their nature and strength. Since no state is available at the same frequency that propagates in the opposite direction, any wave incident on the defect can only circumnavigate it and then recover its original path along the edge of the system, at most accumulating some phase shift. This remarkable feature is apparent in the numerical simulation shown in Fig. 1(b) and is in stark contrast with standard waveguides where generic defects are responsible for a strong backscattering of light and, therefore, a significantly suppressed transmission.

In contrast to the reciprocal behavior of the bulk visible in Fig. 1(c), the large nonreciprocity of the transmission between a pair of antennas located on the edge shown in Fig. 1(d), as well as its insensitivity to the presence of a metallic scatterer located in between them, was the smoking gun of the nontrivial topology.

Similar experiments were soon performed by other groups (Fu, Liu, and Li, 2010a, 2010b; Fu, Lian et al., 2011; Fu, Liu et al., 2011; Poo et al., 2011, 2012, 2016; Lian et al., 2012a, 2012b; Yang et al., 2013; Li, Wu, Poo, Li et al., 2014; Li, Liu et al., 2014). The many possibilities of these systems to engineer a variety of different band topologies were then explored. For instance, photonic bands with large Chern number bands were theoretically identified by Skirlo, Lu, and Soljacic (2014) by simultaneously gapping multiple pairs of Dirac cones. This prediction was confirmed by the experiment (Skirlo et al., 2015), where the edge-mode profiles were directly scanned and Fourier transformed, so to observe chiral dispersions of Chern numbers ranging from 1 to 4, as illustrated in Fig. 9.

As further features of topological edge states, it was later shown that they can self-guide in air (Ao, Lin, and Chan, 2009; Poo et al., 2011; Liu, Shen, and He, 2012; J. Lu et al., 2013; Li, Wu, Poo, Lin, and Li, 2014; Z. Li et al., 2015), appear in coupled defect cavities (Fang, Yu, and Fan, 2011), have robust local density of states (Asatryan et al., 2013, 2014), be modeled in time domain (Li et al., 2013), self-collimate unidirectionally (Li, Li, and Wu, 2015), be realized in materials of Tellegen magnetoelectric couplings (Jacobs et al., 2015; Ochiai, 2015b; He, Sun et al., 2016; X.-C. Sun et al., 2017), form bulk flat bands (Yang, Wu, and Zhang, 2017a, 2017b), and be immune to disorder in the bulk (Mansha and Chong, 2017; Xiao and Fan, 2017a). Remarkably, while it was previously known that one-way modes can exist on the surfaces of continuous magnetic media (Hartstein et al., 1973; Yu et al., 2008, 2014; Zhang, Li, and Jiang, 2012; Deng et al., 2015; Ochiai, 2015a; Shen et al., 2015; Gangaraj and Hanson, 2017), the topological origin of these modes was only recently unveiled (Silveirinha, 2015, 2016a, 2016b). Topologically robust, zero-dimensional defect states localized on a dislocation in a two-dimensional topological photonic crystal were theoretically predicted and experimentally observed by Li et al. (2018).

![](images/df359eb183b108d505cddbb322a6ba19e4b2b9e77e33c6b53382bcd78096ff23.jpg)  
FIG. 9. Comparison of theoretical and experimental results for the setup shown in Fig. 1(a) for varying magnetic fields. (a) Theoretical topological gap map as a function of the static magnetic field applied. Each band gap is labeled by its gap Chern number, the sum of Chern numbers of the bulk bands below the gap. (b) Calculations of the band and edge state dispersion for a few different values of the magnetic field. (c) Experimental edge dispersions obtained by Fourier transforming the edge-mode profiles containing both intensity and phase information. (d) Experimental bulk transmission as a function of magnetic field and frequency, in agreement with the gap map in (a). Adapted from Skirlo et al., 2015.

From the application point of view, these one-way edge waveguides inspired novel device designs for tunable delays and phase shifts with unity transmission (Wang et al., 2008), reflectionless waveguide bends and splitters (He et al., 2010a, 2010b; Liu et al., 2010; Wang et al., 2013), signal switches (Zang and Jiang, 2011), directional filters (Fu, Liu, and Li, 2010b) and couplers (Wang et al., 2011; Zhu and Jiang, 2011), broadband circulators (Qiu, Wang, and Soljacic, 2011; Zhang et al., 2013), slow-light waveguides (Yang et al., 2013), terahertz circuits (Bahari, Tellez-Limon, and Kante, 2016), photonic pulling force (D. Wang et al., 2015), and other functions (Y. Wu et al., 2017).

Whereas all these experiments were carried out using magneto-optic photonic crystals in the microwave domain, there is a strong push toward extending these ideas toward optical frequencies. In this domain, the magneto-optical effects are typically weaker by at least 2 to 3 orders of magnitude, but the material is continuously being improved (Onbasli et al., 2016) and enhanced (Luo et al., 2016). Even though the resulting topological band gap is correspondingly smaller than that in the microwave range, such a small bandwidth is still enough to provide topological features in narrow-band phenomena such as topological laser operation (Bahari et al., 2017). More details on these very recent developments are given in the outlook Sec. VIII.

# 2. Propagating geometries

In this section, we will discuss an alternative approach that does not make use of magneto-optical effects, thus enabling the realization of a photonic topological system in the optical

frequency range: by using three-dimensional systems (in particular, arrays of optical waveguides) (Szameit and Nolte, 2010), it is possible to use one of the dimensions as a temporal coordinate and thus observe topological protection in the orthogonal plane (Rechtsman, Zeuner, Plotnik et al., 2013). For waveguide arrays, this means breaking inversion symmetry along the direction of propagation  $(z)$  in order to observe chiral edge states in the  $(x,y)$  plane. This is akin to substituting optical activity (i.e., circular birefringence) for the Faraday effect required for the Haldane-Raghu mechanism. In this section, we start by introducing the fundamentals of waveguide arrays and how they may be described as a  $(2 + 1)$ -dimensional system (two spatial dimensions, and one temporal) in which diffraction of optical wave packets substitutes for temporal evolution of quantum mechanical particles. We then describe how such arrays may break  $z$ -reversal symmetry and realize topological protection through the Floquet-engineering approach introduced in Sec. II.A.5. The waveguide array geometry (also called "photonic lattices") has previously been used across different physical systems to realize novel phenomena such as spatial lattice solitons (Efremidis et al., 2002; Christodoulides, Lederer, and Silberberg, 2003; Fleischer et al., 2003), two-dimensional Anderson localization (Schwartz et al., 2007; Lahini et al., 2008), and wave dynamics in quasicrystals (Freedman et al., 2006, 2007; Levi et al., 2011; Verbin et al., 2013), among many others. There is also a proposal for obtaining a non-Abelian braiding phase for photons (Iadecola, Schuster, and Chamon, 2016) by guiding light through zero-energy midgap modes in a two-dimensional host lattice (although braiding of photons would not be of use for quantum computing in the same spirit as the braiding of Majorana fermions).

A typical waveguide array geometry is depicted schematically in Fig. 10(a). The waveguides are fabricated using the direct laser writing method, and their properties are highly dependent on the host material [Fig. 10(b) shows a microscope image of a transverse cross section of the structure]. Next we describe experiments performed in fused silica glass (refractive index  $n = 1.46$  at wavelength  $\lambda = 633 \mathrm{~nm}$ ). The specifics of the fabrication procedure are described in detail elsewhere (Szameit et al., 2007; Szameit and Nolte, 2010). Typical parameters that describe waveguide properties are refractive index increase from the background  $\Delta n \sim 1.0 \times 10^{-3}$ , waveguide radii in the  $x$  and  $y$  directions are  $r_x = 2\mu \mathrm{m}$  and  $r_y = 5\mu \mathrm{m}$ , and their shapes may be described with a hyper-Gaussian functional form  $\Delta n(x,y) = \Delta n_0\exp \left\{-[(x / r_x)^2 + (y / r_y)^2 ]^{\alpha}\right\}$ , with the exponent  $\alpha = 3$  in fused silica glass. In a typical waveguide array experiment, a beam of light is injected at the input facet of the array ( $z = 0$ ) and allowed to propagate through until it exits the array, at which point it is imaged onto a charge-coupled device (CCD) camera. As discussed in Sec. II.B.2.c, it is described by the paraxial equation for the diffraction of light:

$$
i \partial_ {z} \tilde {E} = - \frac {1}{2 k _ {0}} \nabla_ {\perp} ^ {2} \tilde {E} - \frac {k _ {0} \Delta n}{n _ {1}} \tilde {E}, \tag {60}
$$

where  $\tilde{E}$  represents the envelope function of the electric field. Note that the paraxial equation takes the form of a Schrodinger

![](images/823116e68bf95ef08f75da5e9f80e7d98ffbdbeb7fe7dea8191f87ec54cada9c.jpg)

![](images/fada276a07f6f096b8657da22ed1168164e4637d759b95ce09da10a047bfee52.jpg)

![](images/fc830a630a57994fd8ac64064824d07bbf4a2294f7e2162ab9331f53f2e8b537.jpg)  
FIG. 10. (a) Schematic diagram of a honeycomb lattice waveguide array with straight waveguides. Adapted from Rechtsman, Zeuner, Tunnermann et al., 2013. (b) Microscope image of input facet of a honeycomb lattice waveguide array. Adapted from Rechtsman, Plotnik et al., 2013. (c) Schematic of an array of helical waveguides; each waveguide helix has the same radius, period, and phase (i.e., they are all moving in concert). Adapted from Rechtsman, Zeuner, Plotnik et al., 2013.

equation, even though it describes the diffraction of classical light rather than the motion of a massive quantum particle. However, in the usual Schrödinger equation of quantum mechanics, the left side of the equation has a time derivative; here it is a derivative in  $z$ , the spatial coordinate in the propagation direction. Therefore,  $z$  takes the role of a temporal coordinate and the transverse  $(x,y)$  plane takes the role of an artificial two-dimensional material. The diffraction of static continuous wave light therefore emulates the evolution of the wave function of a single quantum mechanical particle.

The structure shown schematically in Fig. 10(a) and in an experimental image in Fig. 10(b) is a honeycomb lattice of waveguides. Each waveguide is single mode, meaning it can be thought of as a potential well with a single bound state. The waveguides are placed at a distance from one another such that the modes of neighboring waveguides can evanescently couple (i.e., "tunnel") between neighbors (typical spacing  $d = 15 \mu \mathrm{m}$ ). This results in a typical hopping parameter (aka, coupling constant) between waveguides of  $J \sim 1 \, \mathrm{cm}^{-1}$ , but this can be tuned by changing the wavelength, waveguide

refractive index, and/or spacing between the waveguides. The length of the sample (which corresponds to the amount of "time," i.e., propagation distance, that the optical wave function can propagate) is typically taken to be on the order  $Z \sim 10 \, \text{cm}$ . Given that this particular array is a honeycomb lattice, the diffraction of photons therefore has a perfect correspondence with the motion of noninteracting electrons in graphene. Honeycomb waveguide arrays were first used to demonstrate optical Dirac physics via the observation of conical diffraction (Peleg et al., 2007).

Since each waveguide acts as an "artificial atom" in the analogy between waveguide arrays and two-dimensional materials, it is possible to employ the tight-binding approximation to Eq. (60), as described in Sec. II.B.2.c. In this approximation, the wave function  $\tilde{E}$  is expanded in a subspace composed of bound modes of each waveguide. Thus, we can write the paraxial equation as

$$
i \partial_ {z} \alpha_ {m} = - \sum_ {\langle m, n \rangle} J _ {m n} \alpha_ {n}, \tag {61}
$$

where  $\alpha_{m}$  is the amplitude of the mode in waveguide  $m$ ,  $J_{mn}$  is the hopping strength between waveguides  $m$  and  $n$ , and the summation is taken over neighboring waveguides (nearest, next-nearest, and so on, as necessary). Here we henceforth assume the tight-binding description due to its ubiquity across other experimental platforms (condensed matter, ultracold atoms, coupled resonators, among others). The bulk and edge band structures of the honeycomb lattice of Fig. 10(a) are shown in Figs. 4(c) and 4(e), assuming nearest-neighbor hopping only. For a discussion of edge band structure, see Sec. III.D. This is exactly the band structure of graphene (Wallace, 1947; Castro Neto et al., 2009) exhibiting Dirac cones—conical touchings between bands at the Brillouin zone corners. We note here this system may be explored beyond the tight-binding limit by performing photonic ab initio simulations by diagonalizing the full continuum Schrödinger equation (60). Most often, continuum simulations yield only minor quantitative corrections to tight binding, but in special cases can reveal profound qualitative differences, including the presence of edge states in regions of the edge Brillouin zone where tight binding predicts none (Plotnik et al., 2014). A rigorous description of continuous topological systems can be found in a series of works by Fefferman and Weinstein (2012, 2014), Fefferman, Lee-Thorp, and Weinstein (2014), and Lee-Thorp et al. (2016).

A key requirement of realizing topologically protected chiral edge states is breaking time-reversal symmetry, as previously described. Since  $z$  acts as a temporal coordinate in waveguide arrays, breaking  $z$ -reversal symmetry can allow for topologically protected edge states in the transverse  $(x,y)$  plane. This is accomplished by using helical, instead of straight, waveguides in a honeycomb waveguide array, as depicted in Fig. 10(c). Similar helical waveguide arrays have been used to demonstrate dynamical localization (Crespi et al., 2013). To describe the diffraction of light through the helical array, we move into a coordinate frame comoving with the helices:  $x \rightarrow x + R\cos \Omega z$ ,  $y \rightarrow y + R\sin \Omega z$ , and  $z \rightarrow z$ . In the new coordinate system, the Laplacian remains unchanged, but the  $z$  derivative transforms as

$$
\partial_ {z} \rightarrow R \Omega [ - \sin (\Omega z) \partial_ {x} + \cos (\Omega z) \partial_ {y} ] + \partial_ {z}. \tag {62}
$$

We now rewrite the  $z$  derivative of Eq. (60) in this new coordinate system and find

$$
i \partial_ {z} \tilde {E} = [ i \nabla_ {\perp} - \mathbf {A} (z) ] ^ {2} \tilde {E} - \frac {k _ {0} \Delta n}{n _ {1}} \tilde {E} + \frac {k _ {0}}{2} R ^ {2} \Omega^ {2} \tilde {E}, \tag {63}
$$

where  $\mathbf{A}(z) = k_0R\Omega (-\sin \Omega z,\cos \Omega z)$  is the vector potential induced by the helical rotation, and the final term in Eq. (63) can be ignored because it is simply proportional to the identity. This vector potential  $\mathbf{A}$  corresponds to a circularly rotating electric field (note that it is curl free, so the corresponding magnetic field is zero). It can be incorporated into Eq. (61) simply by including the appropriate Peierls phase factors in the hopping, namely,  $J_{mn}\rightarrow J_{mn}\exp [-i\mathbf{A}(\mathbf{z})\cdot \mathbf{r}_{mn}]$ , where  $\mathbf{r}_{mn}$  is the vector that connects site  $m$  to site  $n$ . Therefore, the Schrödinger equation (61) is time periodic and must be solved using the machinery of Floquet engineering; see Sec. II.A.5. This equation is perfectly analogous to the Schrödinger equation that describes the motion of electrons in graphene under the influence of circularly polarized classical light; see also Eq. (32) and paragraph below. The rotating field acts to break time-reversal symmetry (actually  $z$ -reversal symmetry,  $z$  being the temporal coordinate), without requiring the presence of a magnetic field (even a fictitious one). This Floquet system precisely maps to the Haldane model (Haldane, 1988) in the high-frequency driving limit; see Eq. (33) for a description of the effective Haldane-like Hamiltonian. The bulk and edge band structures for the Haldane model are shown in Figs. 4(d) and 4(f), respectively; these are qualitatively akin to those of the waveguide array described here. Comparing Figs. 4(c) and 4(e) with 4(d) and 4(f), it can be seen that the helicity acts to break the degeneracy at the Dirac points and open a bulk band gap. In the edge band structure [Fig. 4(f)], edge states are present (these are the two bands crossing the gap), with one localized to the top of the structure and the other localized to the bottom. They are part of a single chiral edge state that flows around the edges.

The topologically protected chiral edge states can be directly observed experimentally. A series of such experiments were performed by Rechtsman, Zeuner, Plotnik et al. (2013), observing perfect transmission around corners and past defects; we highlight one of these in Fig. 11. Here light is injected in the top-left corner of a honeycomb lattice arranged in an equilateral triangle geometry, for a series of samples of increasing helix radius. The optical wave function travels clockwise around the structure, with increasing group velocity as a function of the helix radius (i.e., gauge field strength) until about  $R \sim 8 \mu \mathrm{m}$ , whereupon the group velocity decreases and goes to zero at  $R \sim 16 \mu \mathrm{m}$ . This is quantitatively consistent with the lattice model, which predicts that the band gap opens, and then closes, as a function of increased helix radius (Rechtsman, Zeuner, Plotnik et al., 2013). The high background signal that is observable at  $R = 16 \mu \mathrm{m}$  arises from the bending loss associated with the helicity of the waveguides (this corresponds to the phenomenon of "heating" in condensed-matter Floquet systems). Note that in each case, some bulk modes are excited (i.e., not all light is localized to the edge of the structure). This is attributable to the fact that the

![](images/d12cae7bf60d9bc64284680d71c2949c468a95ce3dee0f8636169f1e42b079ce.jpg)

![](images/fdebdd746a8e5c95cb3543952472042578bd1be9a06480b12acb91a135ffc10e.jpg)

![](images/bc2e6c8d09c47891a90acb9b6c6f4f540c655d932eab43733c8dacb65523cb13.jpg)

![](images/40d291aad3e5c7f0b31356e471b58b47f17b9a8a1861bfc04ee107de15bebde2.jpg)

![](images/995d050c0dc7a04eee3027f3a06f3ab9cbd3743f2cb76d936b86eed7658c2e32.jpg)  
FIG. 11. (a) Microscope image of input facet of waveguide array (Rechtsman, Zeuner, Plotnik et al., 2013). The yellow circle indicates the point of injection of input light. (b)-(f) Output facet of waveguide array after  $10\mathrm{cm}$  of propagation, for different devices with increasing helix radius. The edge states do not backscatter as they turn around the top-right corner, i.e., in (d). Their group velocity increases and then decreases with  $R$ , as predicted from the Floquet lattice model. Significant bending loss can be observed in the background for  $R = 16\mu \mathrm{m}$ . Helix period is  $1\mathrm{cm}$  in all cases.

![](images/0d3ff00b6db5cc24bff092e936cf8ab3608aee50706c3ebc513c30d11d5e2e8a.jpg)

bulk modes have some support at the corner of the structure and are therefore excited along with the edge states when light is injected at the corner waveguide.

Since the advent of topological phenomena in the paraxial geometry, there has been significant progress in this direction. To highlight a few examples, waveguide array geometries have been used either theoretically or experimentally to demonstrate the optical Rashba effect (Plotnik et al., 2016), the photonic anomalous Floquet topological insulator state (Rudner et al., 2013; Bellec et al., 2017; Maczewsky et al., 2017; Mukherjee, Spracklen et al., 2017), topological transitions (Leykam, Rechtsman, and Chong, 2016; Guglielmon et al., 2017), chiral edge states in quasicrystals (in particular, Penrose tilings) (Bandres, Rechtsman, and Segev, 2016), protected zero-dimensional cavity modes in two-dimensional lattices (Noh et al., 2018) (protected modes two dimensions lower than host lattice), type-II Weyl points in three dimensions (Noh, Huang, Leykam et al., 2017), and the topological Anderson insulator (Stutzer et al., 2018), a one-dimensional version of which was realized in an ultracold atomic gas (Meier et al., 2018). Furthermore, Floquet topological insulators were realized in waveguide arrays fabricated with two-photon polymerization in photoresist materials; these were used to demonstrate protection against time-dependent defects (Jorg et al., 2017). Because of the difficulty of breaking time-reversal symmetry in a planar geometry, the paraxial platform described here provides a rich methodology for photonic topological phenomena, including those that incorporate

non-Hermiticity, nonlinearity, and other effects that go beyond solid-state physics. Recently, a state-recycling technique was developed to significantly enhance the effective time scales over which dynamics take place within arrays of coupled optical waveguides (Mukherjee et al., 2018). This scheme consists of placing the photonic lattice into a cavity, which allows the optical state to be reinjected many times into the lattice. This approach also allows one to image real-time (stroboscopic) evolution in photonic lattices, by recording the state of the system after each round-trip.

# 3. Optomechanics

There have also been interesting developments in breaking time-reversal symmetry and implementing synthetic gauge fields in optomechanical systems. In general, the field of optomechanics deals with the coherent interaction between photons and acoustic phonons confined in a cavity or an array, which can be controlled at the single phonon level (Aspelmeyer, Kippenberg, and Marquardt, 2014). This field has generated a lot of excitement due to its potential applications, ranging from sensing to quantum information processing.

In 2012, it was proposed that time-reversal symmetry could be broken in optomechanical resonators, and therefore, one could use them as an optical isolator and nonreciprocal phase shifter (Hafezi and Rabl, 2012). Specifically, a directional laser pump was used to select one circulation direction, such that, consequently, the manifestation of time-reversal breaking could be observed in the nonreciprocal optical response (Ruesink et al., 2016; Shen et al., 2016). One can also switch the role of phonon and photons and study nonreciprocal transport of phonons (Habraken et al., 2012; Stannigel et al., 2012; Fleury et al., 2014; Kim et al., 2017).

More recently, there has been an intriguing proposal for the implementation of synthetic gauge fields in optomechanical crystals (Schmidt et al., 2015). Thanks to the uniformity in their fabrication, optomechanical crystals can form a 1D or 2D array of resonators, with a significant degree of controllability. Initial experimental demonstration of such an approach for a few sites was recently reported by Fang et al. (2017). These advances could lead to the realization of various topological phases in optomechanical crystals (Schmidt et al., 2015) and nonreciprocal baths and amplifiers (Metelmann and Clerk, 2015). Other optomechanical systems to implement synthetic gauge fields include quantum wells (Poshakinskiy and Poddubny, 2017) and superconducting circuits (O'Connell et al., 2010; Gustafsson et al., 2014; Chu et al., 2017; Clark et al., 2017).

# 4. Cavity- and circuit-QED systems

Arrays of cavity- and circuit-QED devices can offer several advantages for exploring topological states of light, including highly controllable geometry and connectivity, as well as the possibility of reaching the regime of strong effective photon-photon interactions. Depending on the material platform and the frequency domain considered, these interactions can be obtained by coupling photons to a variety of emitters, e.g., atoms, chemical impurities in a solid-state material, artificial atoms such as quantum dots, or even superconducting circuits

(Gu et al., 2017). While progress in interacting topological photonics will be discussed in Sec. VII, we introduce here experimental and theoretical advances toward realizing non-interacting analog quantum Hall states in cavity- and circuit-QED related systems.

One approach in this direction relies upon engineering arrays of tunnel-coupled reentrant coaxial microwave cavities, as outlined theoretically by Anderson et al. (2016) and demonstrated experimentally by Owens et al. (2018). In this setup, time-reversal symmetry is broken through the chiral on-site spatial wave function of every fourth resonator, as depicted in Fig. 12. This chiral on-site wave function is engineered through the coupling of a ferrimagnetic yttrium-iron-garnet (YIG) crystal in a magnetic field to the neardegenerate  $P$  modes of a triple-coax cavity. The resulting model corresponds to a Harper-Hofstadter model [Eq. (14)] with an effective magnetic flux per plaquette of  $\alpha = 1 / 4$ . By using a real magnetic field to break time-reversal symmetry, this approach is akin to earlier work (Wang et al., 2009) at room temperature, but allows one to substantially suppress losses by focusing on those topological bands that are dark to the YIG crystals. Measuring and compensating disorder in this system relies upon Hamiltonian tomography techniques based upon one- and two-point network analysis of the lattice (Ma et al., 2017). Forthcoming challenges include extensions of these ideas to higher-dimensional topological circuits and then to strongly interacting systems. For the latter, quality factors need to be significantly higher as could likely be realized using superconducting cavities, and the system will need to be operated in a cryogenic environment where  $\hbar \omega_0 \ll k_B T$ . Specific issues related to the population of strongly correlated states are addressed in Sec. VII.B.

A different strategy to induce an artificial gauge field in a coupled cavity array was proposed by Cho, Angelakis, and Bose (2008). The idea is to trap in each cavity a single atom with two ground states that can be described as a lattice of effective spin  $1/2$  and can thus be mapped onto a lattice of impenetrable bosons. Hopping between neighboring sites is provided by the effective spin-exchange coupling that results from intercavity hopping of virtually excited photons when atoms are optically dressed. The artificial magnetic field is imposed by making the optical dressing field spatially dependent. While this first proposal focused on the fractional quantum Hall regime, similar ideas have since been applied to noninteracting polaritons in a hybrid circuit-QED system (Yang et al., 2012), where a superconducting resonator at each lattice site is coupled to a nitrogen-vacancy center ensemble, whose internal states are dressed by spatially dependent microwave sources.

Another proposal to realize a synthetic magnetic field in a circuit-QED architecture by means of passive circulator elements was proposed by Koch et al. (2010): the circulators mediating the tunnel coupling between resonators are designed to break time-reversal symmetry and can be implemented with simple superconducting circuits, such as three-junction Josephson rings. Extended to a lattice of resonators, this approach could be used to realize a Chern insulator, for example, in a kagome geometry as also further studied by Petrescu, Houck, and Hur (2012). Along these lines, a general strategy to break time-reversal symmetry in a resonator lattice

![](images/8b465b8a8144f3cc797c79d614586750949b7c82f87efb51ea1f36846f6599e3.jpg)  
FIG. 12. (a) Connectivity of a microwave cavity model engineered to realize a Harper-Hofstadter model [Eq. (14)]. Open circles are fundamental-mode resonators exhibiting an  $s$ -like on-site orbital. Blue  $\rightarrow$  orange circles are chiral resonators with a single isolated  $p_x + ip_y$  orbital, employed to induce an effective magnetic flux per plaquette of  $\alpha = 1/4$ . (b) A photograph of the lattice from overhead, with a single four-site magnetic unit cell highlighted in green. Fundamental-mode resonators consist of a single-post coaxial cavity; chiral resonators consist of a three-post cavity where time-reversal symmetry is broken using a yttrium-iron-garnet sphere in a magnetic field. Tunneling between cavities is achieved via a slot cut between them. (c) A cutout side view of the same structure: now evident are aluminum screws threaded into the center post of the fundamental-mode resonators, used to tune their frequencies to degeneracy. (d) Site-resolved measurement of the band structure and edge dispersion of the lattice. Frequencies on the vertical axis are in GHz. From Owens et al., 2018.

by exploiting the magneto-optical effect in the waveguide or resonator elements mediating intersite coupling was discussed for photonic crystal resonator lattices by Fang and Fan (2013b).

# 5. Other proposals

Beyond current experiments, there have been many proposals for alternative routes to breaking time-reversal symmetry in photonics by exploiting light-matter coupling, dynamical modulation, and/or novel lattice elements. As

we now briefly review, these developments may lead to analog quantum Hall effects in a variety of new systems, including microcavity polaritons and different realizations of resonator lattices.

# a. Topolaritons

Microcavity polaritons provide a particularly suitable photonic platform to address the physics of lattices with broken time-reversal symmetry. Polaritons are mixed light-matter quasiparticles arising from the strong coupling between photons and excitons, electron-hole bound pairs, confined in a semiconductor microcavity (Carusotto and Ciuti, 2013). While they are neutral particles, excitons possess a non-negligible magnetic moment arising from the spin of the electron and hole in the pair. Thus, polaritons, via their excitonic component, show significant Zeeman splittings  $(\Delta_{Z})$  when subject to an external magnetic field (Mirek et al., 2017). In this situation, the lowest-energy mode of polaritons confined in a single resonator splits into two states of different emission energy characterized by opposite circular polarizations.

This feature has been exploited in a number of theoretical works to propose a Chern insulator based on a polariton lattice in an external magnetic field (Bardyn et al., 2015; Karzig et al., 2015; Nalitov, Solnyshkov, and Malpuech, 2015; Yi and Karzig, 2016). The combination of the polariton Zeeman splitting and the transverse-electric-transverse-magnetic (TE-TM) splitting  $(\Delta_{\mathrm{TE - TM}})$  characteristic of the photonic part of polaritons (Kavokin, Malpuech, and Glazov, 2005) results in the opening of a topological gap whenever band crossings are present in the spectrum of the lattice. Simultaneously, in finite-size samples, protected chiral edge states emerge at the boundaries, with a chiral direction determined by the sign of the external magnetic field. A prominent example of these topolaritons is a honeycomb lattice of semiconductor micropillars in the presence of an external magnetic field (Nalitov, Solnyshkov, and Malpuech, 2015). In this case, the external magnetic field is expected to open a gap at the Dirac cones with a magnitude given by  $\Delta_Z$  and  $\Delta_{\mathrm{TE - TM}}$ ; the resulting bands acquire a Chern number of  $\mp 2$  or  $\pm 1$  depending on the ratio of these splittings to the nearest-neighbor hopping (Bleu, Solnyshkov, and Malpuech, 2016, 2017a). One of the most attractive features of polaritons is the possibility of combining these topological properties with significant Kerr nonlinearities; more discussion on interacting topological systems is given in Sec. VII. Recently, topolaritons have been experimentally realized in the context of topological lasers (Klembt et al., 2018), which are discussed in more detail in Sec. VIII.

Besides exciton polaritons in suitable semiconductor devices, Jin et al. (2016) recognized that magnetoplasmons arising from the coupling of the electromagnetic field with electron-hole excitations in electronic quantum Hall systems also have nontrivial topological properties. In particular, since magnetoplasmons possess a particle-hole symmetry while breaking time-reversal symmetry, they are a unique example of class D 2D topological systems (Ryu et al., 2010).

# b. Dynamical modulation

A flexible and powerful way to break time-reversal symmetry in both the microwave and optical domain is offered by

the dynamical modulation of the properties of a resonator array. Typically, one dynamically tunes either the resonance frequencies of different cavities (Hayward, Martin, and Greentree, 2012; Minkov and Savona, 2016) or hopping amplitudes (Fang, Yu, and Fan, 2012b). In this approach of modulation-assisted tunneling, a large difference  $\Delta \omega$  in the on-site resonance frequencies between neighboring tight-binding lattice sites initially suppresses particle tunneling. This tunneling can be restored by applying a suitable resonant time-dependent modulation at frequency  $\Delta \omega$ . The phase of the external modulation then appears in the phase of the tunneling amplitudes, simulating the effects of a gauge field on a charged particle. The idea was first introduced by Jaksch and Zoller (2003) and experimentally implemented by Aidsburger et al. (2013) and Miyake et al. (2013) for ultracold gases. A related idea was proposed in a classical mechanical framework by Salerno et al. (2016).

For a suitable spatial dependence of phases in a square geometry, the dynamical resonator array maps directly onto the Harper-Hofstadter model [Eq. (14)]. Although this mapping relies on the rotating wave approximation, nontrivial topological features persist even if the inter-resonator coupling is ultrastrong and the rotating wave approximation breaks down (Yuan and Fan, 2015b). Other choices of the modulation phases can be used to engineer spatially inhomogeneous effective gauge fields (Fang and Fan, 2013a; Lin and Fan, 2014) or effective electric fields (Yuan and Fan, 2015a; Yuan, Xiao, and Fan, 2016) that may also be useful in controlling light. Complex modulations were implemented by Lumer et al. (2018) to realize novel light guiding effects by a spatially dependent gauge field, as proposed by Lin and Fan (2014). Going up in geometrical complexity, nonreciprocal propagation based on interband photonic transitions induced in a waveguide by means of a running-wave-shaped, electrically driven modulation of the refractive index was experimentally demonstrated by Lira et al. (2012). In general, note that dynamical modulation as well as magneto-optical effects could also be exploited to imprint a synthetic magnetic field for photons in a resonator-free implementation, based on a waveguide network (Lin and Fan, 2015).

The actual implementation of the general temporal modulation idea depends on the specific photonic system under consideration. In the infrared and optical domains, the main limitation is posed by the rate at which photonic structures can actually be modulated (e.g., by carrier injection or optomechanics), which is typically significantly lower than the optical frequency itself (GHz versus 100 THz). A resonator lattice with hoppings on the order of the modulation frequency (or lower) is thus required, which in turn imposes stringent bounds on the quality factor of the resonators. In circuit-QED architectures, schemes to dynamically modulate the superconducting circuit elements [e.g., superconducting quantum interference devices (SQUIDs)] used to couple the lattice of resonators together were proposed by Peropadre et al. (2013) and Y.-P. Wang et al. (2015, 2016). As we shall see in more detail in Sec. VII.B, this strategy was employed for a pioneering demonstration of the interplay of magnetic and interaction effects by Roushan et al. (2017b). In propagating geometries based on waveguide arrays, the role of time and the propagation direction are exchanged (see Sec. III.A.2), and

so a suitable "time-dependent" modulation may be realized by spatially varying the refractive index of the medium (Longhi, 2013; Dubček, Lelas et al., 2015). Pioneering experiments along these lines were reported by Rechtsman, Zeuner, Plotnik et al. (2013) and Mukherjee et al. (2015) and are reviewed in Sec. III.A.2.

# B. Analog quantum spin Hall systems in photonics

The second main class of topological photonics systems in 2D are those which preserve time-reversal symmetry for photons and which are analogous to quantum spin Hall systems in condensed matter. In this class of systems, the one-way edge modes are only topologically protected if spin-changing scattering processes can be neglected. Here we provide an in-depth discussion of key systems that have been experimentally realized and also briefly review some promising theoretical proposals.

# 1. Silicon ring resonator arrays

This first section is devoted to a review of the experiments by Hafezi et al. (2013) and Mittal et al. (2014, 2016) using arrays of silicon ring resonators. In these systems, a synthetic magnetic field for photons can be engineered by controlling the differential optical paths, when photons hop between neighboring sites in two opposite directions. A pseudospin-1/2 degree of freedom naturally arises as ring resonators support a pair of degenerate whispering gallerylike modes, propagating in opposite clockwise and counterclockwise directions. As the device does not contain any real magnetic element, time-reversal symmetry imposes the fact that the two spin states experience opposite synthetic magnetic fields, and therefore, the corresponding edge states have opposite chiralities, in direct analogy to quantum spin Hall systems.

We start by explaining how a nonsymmetric phase hopping can be engineered between a pair of optical resonators. By arranging these pairs into a square lattice, one can synthesize a uniform magnetic field. Furthermore, we review the experimental progress in this platform, from imaging topological edge states, demonstration of their robustness in transport observables such as transmission and delay time, and finally measurement of the associated topological invariants. We also discuss the prospect of extension of these ideas in the quantum regime, in particular, in generation of photon pairs and quantum transport of two-photons.

Two-resonator case: As the first step, we show a nonzero hopping phase can be obtained for photons hopping back and forth between a pair of coupled site resonators. As originally proposed by Hafezi et al. (2011), this can be obtained when two neighboring resonators are coupled through a third off-resonant link ring, as sketched in Fig. 13(a). We consider the length of resonators to be  $m\lambda$  where  $2m$  is an even integer and  $\lambda$  is the resonant wavelength. The off-resonant ring link length is set to  $2m\lambda + 3\lambda / 2$  to guarantee that it remains antiresonant. The physics would be analogous for an odd integer, except for the sign of tunneling. Now, if the off-resonant ring link is vertically shifted by  $x$  between site resonators, as shown in Fig. 13(a), the accumulated optical phase during the hopping from one site to the other is asymmetrical, and we achieve the

![](images/535b680d673df2946692537d1fd08c7d68ee7ba85cbb29ce38931759ffe0bda8.jpg)

![](images/9c1c59ba30649e88d9925669e3e630e481ab5086f7c1abc1bf7d32f1b8177e84.jpg)  
FIG. 13. (a) Schematic of the coupling mechanism between two site resonators via an off-resonant link ring. (b) After integrating out the off-resonant link, its asymmetric location leads a nonzero hopping phase  $\phi$  between site resonators. (c) A two-dimensional array of rings realizing the Harper-Hofstadter model for photons. From Hafezi et al., 2011.

desired hopping phase between two sites, given by  $\phi = 4\pi x / \lambda$  as shown in Fig. 13(b).

The formal derivation of this hopping phase was presented by Hafezi et al. (2011) using the input-output formalism (Gardiner and Collett, 1985), which, as discussed in Sec. II.B.2, is equivalent to coupled mode theory in the noninteracting case. An alternative approach using transfer matrices is presented in the supplemental material of Hafezi et al. (2013). We briefly recapitulate the input-output formalism approach. Specifically, the boundary condition for the electric field is given by  $\hat{E}_{\mathrm{i}}^{\mathrm{out}} = \hat{E}_{\mathrm{i}}^{\mathrm{in}} + \sqrt{2\kappa}\hat{a}_{\mathrm{i}}$  where  $\kappa$  is the coupling efficiency and the site index can be left or right,  $\mathrm{i} = R,L$ . Assuming no intrinsic loss in waveguides, the dynamics of each optical resonator is given by  $\dot{\hat{a}}_{\mathrm{i}} = -\kappa \hat{a}_{\mathrm{i}} - \sqrt{2\kappa}\hat{E}_{\mathrm{i}}^{\mathrm{in}}$ . The input of each resonator is related to the output of the other resonator by a propagation phase which depends on the optical length. For our set of parameters,  $\hat{E}_{R(L)}^{\mathrm{in}} = -i\hat{E}_{L(R)}^{\mathrm{out}}\exp (\mp 2\pi i\phi)$ . For counterclockwise modes of the side resonators, as shown in Fig. 13(a), photons acquire a phase proportional to the upper or lower connecting optical lengths, when they hop from left to right and vice versa. If the link ring is positioned asymmetrically, this hopping phase can be different for forward or backward hopping. Specifically, by eliminating the fields in the link rings  $(\hat{E}_R^{\mathrm{in}},\hat{E}_L^{\mathrm{in}},\hat{E}_R^{\mathrm{out}},\hat{E}_L^{\mathrm{out}})$ , the photon dynamics is given by  $\dot{\hat{a}}_{R(L)} = i\kappa \exp (\mp 2\pi i\phi)\hat{a}_{L(R)}$  which is equivalent to having a Hamiltonian

$$
H = - \kappa \hat {a} _ {R} ^ {\dagger} \hat {a} _ {L} \exp (- 2 \pi i \phi) + \mathrm {H . c .} \tag {64}
$$

Note that since the overall length of the link resonators is fixed, to maintain the antiresonance condition, the acquired

phases for forward and backward hops are not independent from each other. Specifically, they are equal in magnitude and opposite in sign. In the general case of an arbitrary off-resonant link ring, the nonzero hopping phases in the forward and backward directions remain opposite in sign to guarantee the Hermiticity of the Hamiltonian. However, if the antiresonancy condition is not met, the resonant frequency of the resonators gets shifted; see the discussion in the supplementary material of Hafezi et al. (2013).

2D lattice: By arranging the resonator in a lattice structure, one can implement an effective uniform magnetic field in the form of the Harper-Hofstadter model, which was discussed in Sec. II.A.1. In particular, we implement the Landau gauge, as in Eq. (14), to obtain the same phase  $\alpha$  over each square plaquette, except that here the  $x - y$  directions are swapped. The phase pattern can be obtained by arranging the positioning of the link rings according to the Landau gauge. Specifically, the link rings responsible for tunneling in the  $y$  direction are symmetrically positioned to get zero hopping phase. In contrast, the link rings for tunneling in the  $x$  direction are asymmetrically positioned, in an increasing order in the  $y$  direction, giving rise to a  $e^{i2\pi \alpha y}$  hopping phase. The scheme is illustrated in Fig. 13(c). As discussed in Sec. II.A.1, for a fixed magnetic field, which is set by the parameter  $\alpha$ , any finite lattice displays bulk and edge bands, the former being organized in the celebrated Hofstadter butterfly, and the latter being located in the gaps of the bulk dispersion.

Experimental setup: The lattice model illustrated in Fig. 13(c) was implemented by Hafezi et al. (2013) using standard silicon-on-insulator technology working in the telecom range at  $\lambda \simeq 1.55\mu \mathrm{m}$ . As illustrated in Fig. 14, high-quality silicon ring resonators with a  $Q$  factor exceeding  $10^{4}$  were fabricated on top of an oxide substrate using deep-UV projection photolithography. The cross section of the waveguides, which form the site resonators and off-resonant link rings, was designed to ensure single-mode propagation of the TE mode. The evanescent coupling between the site resonators and the link rings was controlled by the thickness of the air gaps separating the elements. Because of the surface roughness of the waveguides, a fraction of the light in the resonators scatters orthogonally to the plane and can be captured by a microscope. In addition to transmission measurement through the input and output waveguides coupled to specific site resonators, imaging this scattered light on a CCD camera gives direct information on the spatial profile of the photonic modes. The good quality of the resonators guarantees that the spin-flip-like couplings between clockwise and counterclockwise propagating modes are effectively negligible.

Topologically protected edge states: When the system is excited via the input waveguide with a laser field at a frequency resonant with one of the edge modes, the photons are guided through the edge and exit the system from the output waveguide. Figure 14(b) shows the light propagation clockwise along the edge of the system. The transverse width of the edge state was about one to two resonators, as observed in both experiment and simulation. As a direct manifestation of the topological protection of edge states, when a resonator is removed from the path of an edge state, the

![](images/acbcf7128b36c27a8ffefc531b1359459538b854d2fd399660771632d9f3f6a2.jpg)  
FIG. 14. (a) Sketch of the experimental setup. (b) Spatial intensity profile showing light propagation along the edge of the system. (c) Spatial intensity profile showing routing of light along the edge and around a missing resonator on the edge. (d) SEM image of the system with a missing resonator, intentionally removed in the design. Adapted from Hafezi et al., 2013.

photons route around the missing resonator and then continue their path to the output coupler without being backreflected [Fig. 14(c)].

Beside the spatial imaging the edge states and the qualitative study of their robustness, a more quantitative experimental demonstration of their robustness was reported by Mittal et al. (2014) using the structure described above and sketched in Fig. 14(a). Figure 15 shows the transmission and delay spectra interferometrically measured at the output port for eight different  $8 \times 8$  lattice devices. Overall, the transmission spectra of the different devices show significant fluctuations because of intrinsic fabrication variations in the dimensions of the site resonators and link rings. On closer inspection, one can see that the fluctuations in both the transmission and the delay time are suppressed in the two regions indicated by the red and green shading in Figs. 15(a) and 15(b) corresponding to propagation via edge states in the counterclockwise and clockwise directions along the short and long edges, respectively.

More insight on this physics can be seen in Fig. 15(c), which shows the measured average transmission and its standard

![](images/5264249f736fc7971902886d64fabab44237760a3da8a9599e4a053d4cded93a.jpg)

![](images/ce7e2471cefb05779f948fe3769b02ff91c3d6a9751a39ac99c508e15d12419b.jpg)  
FIG. 15. (a) Measured transmission and (b) delay-time spectra for eight different  $8 \times 8$  lattice devices. The two regions with reduced variance in both the transmission and the delay time are indicated by the red and green shading. A noisy region of propagation through bulk states is indicated by the blue shading. (c) Scaling of the transmission as a function of system size for 2D and 1D devices. Solid markers with error bars are the measured average and standard deviation (65% confidence band) values. Solid lines with shaded areas are the simulated average and standard deviation. Adapted from Mittal et al., 2014.

deviation for a sample of 95 devices. The transmission through the topological edge states of a 2D lattice and the one through the nontopological band of an analogous 1D array (a so-called coupled resonator optical waveguides) are plotted as a function of system size, i.e., the number of resonators traveled from input to output. In both cases, the transmission decays exponentially with system size. However, the decay rate is slower for the topological 2D system compared to the 1D system. The shaded regions are simulation results, using the experimentally estimated parameters, which agree with the experimental observation. In order to differentiate the decay of transmission stemming from resonator losses from the one due to disorder, both resulting in exponential attenuation, the simulated result in the absence of disorder is presented as a dashed line: while losses affect both 2D and 1D systems in the same way, transport through topological edge states of a 2D system appears to be much less disturbed by disorder than the 1D counterpart.

As a further feature of topologically protected edge states, Mittal et al. (2014) experimentally demonstrated how transport in lossy edge states was unambiguously distinguished from tunneling through localized bulk states by considering the statistical distribution of the delay time during propagation. Specifically, the delay distribution for edge states is

approximately Gaussian with a Gaussian width independent of system size, as typical of diffusive transport in one-dimensional systems (Cooper et al., 2010). On the other hand, the distribution for bulk states is asymmetric with the most probable value being less than the average, as typical of transport governed by localization and earlier observed in one-dimensional systems in the microwave domain (Chabanov and Genack, 2001).

Invariant measurement: The hallmark feature of topological physics is the presence of one-way propagating modes at the system boundary, whose chirality is a consequence of topological character of the bulk. Specifically, the bulk-boundary correspondence dictates that the number of chiral edge modes is completely determined by the bulk topological invariant, the Chern number. Following a proposal by Hafezi (2014), the winding number associated with a spectral flow of edge states (see Sec. II.A.4) was experimentally studied by Mittal et al. (2016).

While the transverse conductance experiment usually performed in electronic systems is not applicable to photonic systems, the general spectral flow argument (Laughlin, 1981; Halperin, 1982) is in fact applicable also to this case. To model the spectral flow of a quantum Hall edge of winding number  $k = 1$ , one can consider a linear edge dispersion  $E_{p} = vp$ , where  $E_{p}$  is the energy,  $v$  is the group velocity, and  $p$  is the momentum along the edge. When a gauge flux  $(\theta)$  is coupled to the edge, the momentum is replaced by the covariant momentum, i.e.,  $E_{p} = v(p - q\theta /L)$ , where  $L$  is the length of the edge and  $q$  is the charge of the edge excitations. For noninteracting photons, the synthetic charge can be set to  $q = 1$  so that the corresponding vector potential is simply  $\theta /L$ . For a finite system, quantization of momentum on the edge results in

$$
E _ {n} = \frac {2 \pi v}{L} \left(n - \frac {\theta}{2 \pi}\right), \tag {65}
$$

where  $n$  is an integer. Therefore, the insertion of  $\theta = 2\pi$  flux shifts  $E_{n} \rightarrow E_{n - 1}$ , resulting in a spectral flow.

To experimentally observe and measure this spectral flow, the synthetic gauge field system described above should be supplemented with an extra tunable gauge flux (Mittal et al., 2016). To couple a tunable gauge field to the edges, metallic heaters were fabricated above the link ring waveguides on the lattice edge, as shown in Fig. 16(a). These heaters use the thermo-optic effect to modify the accumulated phase of light propagating through the waveguides and hence result in a gauge flux.

Figure 16(b) shows the measured transmission spectrum as a function of the coupled flux  $\theta$ . Edge states of the outer edge and the bulk states are easily identifiable as bright and dark regions, respectively. As the coupled flux  $\theta$  increases, the energy of the clockwise edge states decreases, whereas the energy of counterclockwise edge states increases. For a  $2\pi$  increase in flux, the edge state resonances move by one resonance to replace the position once held by its neighbor. This flow indicates that the measured winding number is  $k = +1.0(1)$  for the clockwise circulating edge states, and  $k = -1.0(2)$  for the counterclockwise circulating edge states.

Specific theoretical proposals to directly detect the bulk topological invariants without using the edge physics have

![](images/79fc0132c8cbe442c52d8d847e7a24845e242c29af6dd575e889df3ac9f627dd.jpg)

![](images/b2ce378bac4df6889703aeb20189609eb7a5fe36ebe9030be479f8af868205c0.jpg)  
FIG. 16. (a) Sketch of the experimental device (left). The edge states considered in the experiment lie on the outer edge. The tunable gauge field coupled only to the edge states is introduced by fabricating heaters on link rings situated on the lattice edges. SEM image showing heaters fabricated on top of link rings (top right) and schematic of the waveguide cross section showing the ring resonators, the metal heaters, and the metal routing layer (bottom right). (b) Measured transmission as a function of the coupled flux  $\theta$  and the incident laser frequency  $\omega$ . Insets: zoom-in of the edge state bands. Adapted from Mittal et al., 2016.

been suggested by many authors. A short review of the main ones can be found in Sec. VIII.C.

# 2. Topological rf circuits

Radio-frequency (rf) circuits are an excellent substrate for the study of topological band structures and eventually strongly interacting topological phases of matter. Their connectivity can literally be wired in an arbitrary manner, with arbitrary numbers of connections per node and long-range connections, allowing a wide range of exotic band structures to be realized. Furthermore, the physical size of the components is macroscopically large compared to atoms, phonons, and optical photons, enabling easy access for site- and time-resolved measurements. Moreover, topological properties in linear lattice models can be observed at room temperature and in the presence of significant dissipation, despite the fact that there are many thermal photons present. This is a vivid demonstration that topological band structures are the property of waves rather than of quantum mechanical interactions.

Two types of rf topological circuits have been experimentally demonstrated so far; the first type was discussed in Sec. III.A.4 and was used to realize a topological model with time-reversal symmetry breaking and nonzero Chern numbers. The second type of circuit, which is the focus of this section,

employed kHz frequency lumped-element inductors and capacitors to implement a time-reversal invariant topological system (Ningyuan et al., 2015). In this system, it was possible to observe many signature effects of a topological insulator, as well as several features that are difficult or impossible to find in a solid-state material system.

In what follows, we briefly describe the experimental realization of a quantum spin Hall version of the Harper-Hofstadter model (Goldman et al., 2010) with a quarter flux per plaquette that uses only inductors and capacitors; it was subsequently pointed out (Albert, Glazman, and Jiang, 2015) that a minimal circuit model could be realized at a flux per plaquette of  $1/3$ . As shown in Fig. 17, each lattice site in the experimental circuit consisted of two

![](images/30f006ea4f6ce68060847285fb33695ecdf1aed3b5108c26d5619561acc5bf7f.jpg)

![](images/7739f3b487dce3d5583d04625ff34abd3098627fd981764a5c7337bdd20c5279.jpg)  
FIG. 17. (a) Schematic of the experimental circuit used to realize a time-reversal-invariant quantum spin Hall system. In this setup, the periodic structure is composed of inductors and coupling capacitors (black) that are connected by wires (light and dark blue lines). Each lattice site consists of two inductors, labeled  $A$  and  $B$ , corresponding to right and left circularly polarized spins. As a photon hops around a single plaquette (indicated in orange) it accumulates a Berry phase of  $\pi /2$ ; this is engineered by braiding the capacitive couplings, as detailed in (b) and indicated here in green. (b) The synthetic spin-orbit coupling is engineered through the structure of the coupling elements between lattice sites. Each of the four tunneling phases implemented (indicated by the left column of each set of figures) is induced by a particular coupling between inductors (middle column), as described in the corresponding rotation matrix (right column); the signs of the couplings are controlled by whether the + end of one inductor is coupled to the + or - end of the adjacent inductor. (c) The experimental circuit, in which the inductors (black cylinders) are coupled via the capacitors (blue). Inset: Zoom-in on a single plaquette that consists of four adjacent lattice sites. From Ningyuan et al., 2015.

![](images/6c449a203d83fed84f79a9a101dcb47b550d2a135a0d40a69a0ffadb1cd4500a.jpg)

inductors (labeled  $A$  and  $B$ ), allowing for the representation of two pseudospin states. Tunneling between lattice sites was achieved by capacitive coupling, with the sign of the coupling reflected in which ends of the inductors are coupled to one another. Finally, the spin-orbit coupling was implemented by changing, on a site-by-site basis, whether  $A$  was coupled to  $A$ ,  $-A$ ,  $B$ , or  $-B$ .

In more detail, a localized excitation on a single lattice site was represented by rf fields in a  $1 / \sqrt{2} (A\pm iB)$  superposition of the two inductors on the lattice site, where  $+\left(-\right)$  corresponded to spin up (down). Under these conditions, for a spin-up excitation, coupling  $(A,B)\rightarrow (A,B)$  between adjacent lattice sites corresponded to implementing a tunneling phase of  $0^{\circ}$ , while connecting  $(A,B)\to (-A, - B)$  corresponded to a tunneling phase of  $180^{\circ}$ , and  $(A,B)\to \pm (B, - A)$  to a tunneling phase of  $\pm 90^{\circ}$ . Repeating  $(0^{\circ},90^{\circ},180^{\circ}, - 90^{\circ})$  horizontal tunnel couplers every four lattice sites, with all vertical tunnel couplers having a phase of  $0^{\circ}$ , resulted in a Harper-Hofstadter model with a quarter flux per plaquette. Spin-down excitations experienced the opposite Peierls phase and hence the opposite effective flux per plaquette.

It is important to note that this approach transcends the tight-binding regime: instead of a full  $LC$  resonator on each  $A$  and  $B$  site, only an inductor was included. When combined with coupling capacitors, this resulted in a Harper-Hofstadter spin-band structure exhibiting nonzero spin Chern numbers identical to those observed in the analogous tight-binding model; the lack of on-site inductors changes the bandwidths and gaps, but, perhaps surprisingly, does not change the topology of the spin bands. An equivalent construction swaps inductors and capacitors, sending  $\omega \rightarrow \omega_0^2 / \omega$  (with  $\omega_0 \equiv 1 / \sqrt{LC}$ ), in much the same way that swapping inductors and capacitors in the (topologically trivial) 1D lumped-element transmission line converts the transmission line between left and right handed.

By forgoing on-site resonators and using on-site inductors with coupling capacitors, this circuit operates in what can be referred to as a "massless, left-handed" configuration. This requires fewer inductors, which are the primary source of loss and disorder, and provides band gaps of order  $\omega_0$ , making the system less susceptible to disorder than tight-binding approaches with an on-site resonator, where the band gaps are all reduced by the ratio of the on-site capacitance to the coupling capacitance.

Because this approach exhibits tunneling energies comparable to the photon energy  $\omega_0$ , it can be operated with effective quality factors (resulting from inductor loss  $R$ ) of order  $\sim 100$  (characteristic of off-the-shelf room-temperature electronic components), with tunneling still observed over  $\sim 30$  lattice sites within the photon  $1/e$  lifetime; furthermore, a few percent disorder in the components, typical of off-the-shelf electronics, do not induce noticeable backscattering within the photon lifetime. Figures 18(a) and 18(b) show the dynamical evolution of a spin-mixed pulse injected on the edge, as it splits into spin components which move with opposite chiralities.

Because this system is a circuit, its global connectivity is easily modified. Previous work has seen the exploration of Möbius topologies [Figs. 18(c) and 18(d)], with only a single edge (Ningyuan et al., 2015); by connecting the left and right

![](images/91143bc863bc7d73ae1dcef3c0b40c4d533b298f1ae307c407d516b893188ea3.jpg)

![](images/f3c43db246e0c8b590db10c4ae7e82e7ac6fcda7c23a4f4bed5365542e2390cb.jpg)

![](images/bccd6b725f89b21a1433ea6eae7c5e5e2f183fda622dea7c5d7184a0cf537d44.jpg)  
FIG. 18. Time-resolved transport dynamics of the edge modes in the topological circuit, shown in Fig. 17. (a), (b) The spin-resolved time evolution of sites around the edge of a system, following the initial excitation of an  $A$  inductor at the edge. This corresponds, in the pseudospin basis, to an initial localized excitation of  $(\uparrow + \downarrow) / \sqrt{2}$  at a single lattice site. (a) When exciting a topological edge state (at  $145~\mathrm{kHz}$ ), the  $\uparrow$  (red) and  $\downarrow$  (blue) signals propagate around the edge in opposite directions, demonstrating the expected spin-momentum locking. Despite the presence of disorder, two round-trips are visible (as sites 0 and 42 are equivalent). (b) When exciting a nontopological edge state (at  $225~\mathrm{kHz}$ ), disorder immediately leads to backscattering. Inset: The gray arrow indicates the initially excited lattice site, with the edge site numbering convention indicated by the red and blue arrows. (c) Illustration of quantum spin Hall edge states on a Möbius strip (top panel), with arrows indicating the edge propagation direction, and colors representing the spin states. Experimentally, this was realized by imposing the connectivity of a Möbius strip on the circuit (bottom panel), with the printed circuit board shown in orange and the additional external connections colored according to the spin. (d) Spin-resolved detection of edge transport after the excitation of  $\uparrow$ ; the  $\uparrow$  (red) and  $\downarrow$  (blue) signals show the conversion from  $\uparrow$  to  $\downarrow$  as the excitation moves from one edge to the other, with three round-trips being visible. From Ningyuan et al., 2015.

![](images/737a8975bc1c037d20e8eddb04ac06e4a93580a514da377ec8d5a7bcdb1ec1b0.jpg)

edges with a twist and spin flip (c), a Möbius strip geometry is realized, where spinful excitations propagate to the right along the top edge, undergo a spin flip, propagate to the left along the bottom edge, and repeat. Related prospects include for creation of conical defects to explore inter-Landau-level states (Biswas and Son, 2016).

A topoelectrical circuit (Lee et al., 2018) displaying zero-dimensional topological corner midgap states, protected by the bulk spectral gap, reflection symmetries, and a spectral symmetry has also experimentally been realized by

Imhof et al. (2018). A three-dimensional circuit displaying Weyl points was realized by Lu et al. (2019), providing access to the Weyl points and the Fermi arcs as well as to the Berry curvature distribution underlying the quantized chiral charge of the Weyl points. Finally, a microwave network was used by Hu et al. (2015) to measure a topological edge invariant.

# 3. Twisted optical resonators

Exploring Landau-level physics with charge-neutral particles is a persistent goal of the synthetic matter and metamaterial communities, both because learning to create "effective magnetic fields" for charge-neutral particles illuminates the meaning of a magnetic field, and because interacting topological matter in the continuum (fractional quantum Hall phases, for example) admits simpler theoretical description than lattice analogs (fractional Chern insulators).

Proposals to explore Landau-level physics with light rely upon coupling an optical field to a rotating atomic medium (Otterbach et al., 2010) or phase plate (Longhi, 2015) to inject angular momentum. The connection to synthetic magnetic fields may be understood by realizing that sending light through a rotating medium induces an image rotation (Franke-Arnold et al., 2011), thus turning the laboratory frame into a rotating frame. When viewed in a constantly rotating frame, massive particles experience fictitious Coriolis and centrifugal forces  $2m\vec{\Omega} \times \vec{v}$  and  $m\vec{\Omega} \times \vec{\Omega} \times \vec{r} = m|\Omega|^2\vec{r}_\perp$  respectively, where  $\vec{r}$  and  $\vec{v}$  are the particle position and velocity,  $\vec{\Omega}$  is the angular velocity of the rotating frame, and  $m$  is the particle mass. The Coriolis force has the same form as the Lorentz force  $q\vec{v} \times \vec{B}$ , with the identification  $q\vec{B} \equiv m\vec{\Omega}$ . Thus, to investigate Landau-level physics of light in the lab frame, it is only necessary to induce a continuous image rotation on the light and to somehow compensate for the centrifugal force that this rotation applies to the light.

The combination of image rotation and centrifugal-force cancellation was first realized by Schine et al. (2016), using techniques proposed by Sommer and Simon (2016) and depicted in Fig. 19. The image rotation is achieved by directing the light repeatedly through a nonplanar path using a four-mirror optical resonator: akin to a pair of back-to-back dove prisms, this extremely low-loss construction is able to send the light through the nonplanar path thousands of times, inducing an image rotation on each round-trip set by the nonplanarity of the resonator.

To achieve the centrifugal-force cancellation, the mirrors that produce the image rotation are curved to repeatedly focus the light toward the resonator axis. The interplay of wave propagation, reflection off of curved surfaces, and image rotation results in a complex mode structure for such a resonator. Qualitatively, wave propagation in the paraxial limit is equivalent to evolution of a free massive particle and thus imbues the photon with mass; reflection off of the curved mirror surface provides a radial impulse which is proportional to the distance from the resonator axis, providing harmonic trapping, while the resonator twist (nonplanarity) induces the Lorentz and centrifugal forces.

This analogy may be sharpened through 2D  $ABCD$  matrices (Siegman, 1986), or, more intuitively, by treating the repeated passage of the optical field through the resonator

![](images/05f03caf02cde0d49e0f9a648684a9158f693338d6dc59eafaacf0c6c6e12e7f.jpg)  
FIG. 19. Engineering Landau levels for optical photons. Light in an optical resonator behaves as 2D particles in a harmonic trap. (a) When the ray trajectory is followed over many round-trips through a two-mirror resonator, its "hit pattern" in the central plane of the resonator corresponds to the stroboscopic evolution of a classical massive trapped particle. The projection of the eigenmodes of the resonator onto the central plane of the resonator are Hermite Gauss, akin to a quantum harmonic oscillator. (b) When a four-mirror resonator is twisted out of the plane, the ray trajectories undergo a round-trip rotation about the resonator axis, equivalent to Lorentz (Coriolis) and centrifugal forces; when the centrifugal force precisely cancels the harmonic confinement induced by the mirror curvature, the resulting Lorentz force produces Landau levels. (c) A realistic rendering of the four-mirror resonators. From Schine et al., 2016.

![](images/e956f2115d730f63ad035e1cdaa410c48e74370c14d8f59a3fa12b28941b0c73.jpg)

![](images/a96041340a4ad9208a7e6cd9f504c08e60aff9dde565e5fc9152fd52092ce7c7.jpg)

as a periodically driven system (Sommer and Simon, 2016), resulting in an effective "Floquet" Hamiltonian for the optical field in a particular plane of the resonator. The final result is manifolds of degenerate resonator eigenmodes with energies

$$
\frac {E _ {n p q}}{\hbar} = \omega_ {n p q} = n \frac {2 \pi c}{L} + p \omega_ {\text {c y c}}, \tag {66}
$$

where  $c$  is the speed of light in vacuum,  $L$  is the resonator round-trip length, and  $\omega_{\mathrm{cyc}}$  is the effective cyclotron frequency which determines the energy gap between Landau levels. The  $n$  quantum number determines how many wavelengths fit within the resonator longitudinally, or equivalently which Floquet copy we are referring to. Then  $p$  is the Landau-level index, and  $q$  is the angular momentum index of the eigenstate within the Landau level.

Stabilizing the Landau levels against astigmatism: In practice, such resonators are sensitive to mirror astigmatism (due to off-axis incidence of the optical field on the mirrors), which results in different harmonic confinement along the  $x$  and  $y$  axes, and a consequent destabilization of the Landau level. This destabilization may be understood in various ways: (1) astigmatism means that centrifugal force cannot be simultaneously canceled along both the  $x$  and  $y$  axes, and because particles in magnetic fields move along equipotentials, the residual confinement along a single axis guides the particles off to infinity; (2) when the astigmatism is optimally canceled, the residual confining potential takes the form  $x^{2} - y^{2} = r^{2}(e^{i2\theta} + e^{-i2\theta})$  a potential that drives  $\Delta l = \pm 2$  transitions within the degenerate manifold of states comprising the Landau level. This effect has also been observed in rotating atomic gases (Cooper, 2008).

To realize a degenerate Landau level, this astigmatism issue must be addressed. One approach is to engineer a Landau-level-like scenario which does not exhibit states whose angular momenta are separated by  $2\hbar$ ; this is possible by further

twisting the resonator, resulting in a situation where the new "lowest" manifold of degenerate states exhibits only every third unit of angular momentum  $q = 0,3,6,\ldots$ . This new, demonstrably stable system corresponds to a Landau level on a cone with opening angle  $\alpha = \arcsin (1 / 3)$ , which may be understood by realizing that the allowed values of  $q$  support only threefold symmetric light patterns. When a photon leaves a particular third, it reenters that third from the opposite edge, but the dynamics are otherwise that of a planar Landau level. This is precisely how a charged particle behaves when constrained to the surface of a cone, in a  $B$  field normal to the cone's surface. This platform has enabled the first direct measurement of the mean-orbital spin (of the lowest Landau level, see Fig. 20), a

![](images/cf3eb9f1441f53af8541a126a2489d9ec9ff6fbace869b0f79982af44f8dd72f.jpg)  
FIG. 20. Translational invariance of Landau levels and topological dynamics on a conical manifold. The astigmatism-robust Landau levels exhibit a threefold symmetry, manifest in their spectrum by only every third angular momentum state being degenerate  $q = 0,3,6,\ldots$ , or  $q = 1,4,7,\ldots$  or  $q = 2,5,8,\ldots$ . Panels in the top, center, and bottom rows correspond to starting with  $q = 0,1$ , and 2, respectively. Away from the cone tip, the system supports translational invariance, as well as the possibility of generating states with arbitrary angular momentum. Left column: Injection of the two lowest Landau levels centered away from the cone tip: within each group of images, the lower subpanels are for the lowest Landau level, while the upper ones are for the first excited one. In each case, the resonator responds with three copies of the Landau level under consideration: far enough away from the cone tip (right subpanels) the copies are independent of one another. When they are closer (left subpanels), the form of the interference of the copies near the cone tip is sensitive to the initial  $q = 0,1$ , and 2, corresponding to flux threading the tip itself. Right panels: The breaking of translational invariance near the cone tip reflects the Wen-Zee coupling of the lowest Landau level to the geometric curvature of the cone tip; the excess density for the unthreaded cone reflects the mean-orbital spin of the integer quantum Hall state. From Schine et al., 2016.

topological quantum number which quantifies the coupling of density to manifold curvature through the Wen-Zee action (Wen and Zee, 1992).

Time-reversal symmetry breaking is particularly important in interacting systems as collisions between particles in a quantum spin Hall system can induce backscattering which would otherwise be symmetry protected. The twisted optical resonator does not break time-reversal symmetry, and so it must have a hidden spin degree of freedom which when flipped induces the photons to experience the opposite magnetic field. This turns out to arise from the order in which the photon traverses the mirrors of the running-wave twisted resonator. Forward and backward modes exhibit opposite synthetic magnetic fields. To break the degeneracy between them, it is sufficient to differentially couple to the polarization of the modes, which are opposite relative to a fixed axis (although they are the same relative to the direction of propagation). This Faraday-type coupling was recently demonstrated with an optically pumped ensemble in a weak magnetic field (Jia et al., 2018b).

# 4. Intrinsic spin-orbit interactions for light

The fundamental properties of Maxwell's equations lead to an "intrinsic" spin-orbit coupling for light, in contrast to "extrinsic" spin-orbit effects, engineered by the design of photonic materials as discussed in the previous sections. Intrinsic spin-orbit coupling plays an important role on length scales comparable to the wavelength of light and so has attracted attention across photonics, nano-optics, and plasmonics (Bliokh et al., 2015). It can also lead to an analog of the quantum spin Hall effect for light (Bliokh, Smirnova, and Nori, 2015), as we briefly introduce.

In free space, a propagating plane wave has two spin states, given by the left- and right-handed circular polarizations, which have opposite helicities  $\sigma = \pm 1$ . The corresponding spin vector is  $\mathbf{S} = \sigma \mathbf{k} / |\mathbf{k}|$  in units of  $\hbar$  and is aligned with the propagation vector  $\mathbf{k}$ . This is an intrinsic coupling between the orbital and spin degrees of freedom for light, underlying a wide range of phenomena (Bliokh et al., 2015).

When light is strongly confined transverse to its propagation direction, intrinsic spin-orbit coupling can lead to behavior reminiscent of the electronic quantum spin Hall effect (Kavokin, Malpuech, and Glazov, 2005; Leyder et al., 2007; Bliokh, Smirnova, and Nori, 2015; Van Mechelen and Jacob, 2016). In a nutshell, the idea is the following. As a general consequence of Gauss's law in free space,  $\nabla \cdot \mathbf{E} = 0$ , the transversality condition ( $\mathbf{k} \cdot \mathbf{E} = 0$ ) implies that the electric field polarization directly depends on the wave vector  $\mathbf{k}$ . Since the wave vector  $\mathbf{k}$  in the evanescent tail of a confined optical mode has an imaginary component orthogonal to the surface, the polarization acquires a circular component corresponding to a nonvanishing transverse spin component, whose sign changes with the propagation direction (Bliokh and Nori, 2012; Bliokh, Bekshaev, and Nori, 2014).

An analogy can thus be drawn between this so-called "spindirection" (or "spin-momentum") locking of confined optical modes and the spin-momentum locked edge states of a 2D quantum spin Hall system or surface states of a 3D topological insulator. However, a key difference is that the optical modes

are bosonic and so not topologically protected by time-reversal symmetry (Bliokh, Smirnova, and Nori, 2015). Formally, this can be seen by noting that, although a nonzero topological Chern number can be found for each uncoupled helicity state in free space, these Chern numbers are even and so the  $\mathbb{Z}_2$  topological invariant, introduced in Sec. II.A.2, vanishes.

Nevertheless, previous experiments had observed how spin-polarized emitters give rise to a spin-controlled unidirectional excitation of surface or guided modes in a wide range of systems, including metal surfaces (Lee et al., 2012; Rodríguez-Fortuño et al., 2013; O'Connor et al., 2014), optical nanofibers (Mitsch et al., 2014; Petersen, Volz, and Rauschenbeutel, 2014; Sayrin et al., 2015), and waveguides (Le Feber, Rotenberg, and Kuipers, 2015; Söllner et al., 2015). These experiments also show that, despite the lack of topological protection, the spin-direction locking and this optical analog of the quantum spin Hall effect is very robust to system details (Bliokh et al., 2015).

# 5. Bianisotropic metamaterials

In this section, we review how a quantum spin Hall effect for photons can be realized in electromagnetic metamaterials, namely, artificial composite materials containing subwavelength dielectric and/or metallic structures (Liu and Zhang, 2011). The key advantage of such materials is the great flexibility that they offer for engineering the effective dielectric permittivity  $\varepsilon$ , magnetic permeability  $\mu$ , and bianisotropy or magnetoelectric coupling  $\chi$  that appear in the electric and magnetic response to long-wavelength fields,

$$
\left( \begin{array}{c} \mathbf {D} \\ \mathbf {B} \end{array} \right) = \left( \begin{array}{c c} \varepsilon & i \chi \\ - i \chi^ {T} & \mu \end{array} \right) \left( \begin{array}{c} \mathbf {E} \\ \mathbf {H} \end{array} \right). \tag {67}
$$

As first proposed by Khanikaev et al. (2013), a properly designed metamaterial structure can exhibit a quantum spin Hall effect for light, as experimentally evidenced by the presence of topologically robust spin-dependent edge states, analogous to the helical edge states of an electronic topological insulator.

Following the initial theoretical proposal, the first step in this direction is to construct photonic modes which mimic the electron spin-1/2 eigenstates. This can be achieved, for example, through an enforced matching of  $\varepsilon = \mu$  in a metamaterial, ensuring that, in the absence of bianisotropy, the TE- and TM-polarized modes propagate along a 2D metamaterial slab with the same wave numbers, restoring the  $(\mathbf{E},\mathbf{H})\rightarrow (-\mathbf{H},\mathbf{E})$  duality of the electromagnetic field in free space. For a given wave vector  $\mathbf{k}$ , linear combinations  $\psi_{\mathbf{k}}^{+}$  of these degenerate TE and TM modes can be constructed with the special property that  $\psi_{\mathbf{k}}^{+}$  can be transformed into  $\psi_{-\mathbf{k}}^{-}$  by a suitable symmetry operation  $\hat{D}$ , similarly to how an electron's spin is flipped by time-reversal symmetry. Since the square of the transformation satisfies the usual  $\hat{D}^2 = -1$  condition of electronic time reversal, these states can be identified as a pair of photonic pseudospin-1/2 states and show symmetry-protected Kramers doublets for time-reversal symmetric momenta.

The second step required is then to engineer an appropriate bianisotropy or magnetoelectric coupling  $\chi$  (Serdyukov et al., 2001) that generates a strong spin-orbit coupling between the pseudospin states, mimicking that found in a topological insulator. To first order, the effect of a finite  $\chi$  can in fact be recast in reciprocal space as an explicit coupling between photon momentum and polarization  $\mathbf{D} = \epsilon \mathbf{E} + (ic / \omega)\chi \mu^{-1}\mathbf{k}\times \mathbf{E}$  and  $\mathbf{B} = \mu \mathbf{H} + (ic / \omega)\chi^T\epsilon^{-1}\mathbf{k}\times \mathbf{H}$ . While the bianisotropy  $\chi$  of materials found in nature, such as optically active media containing chiral molecules, is typically small, a very large value can be obtained in metamaterial structures containing, for example, split-ring resonators (Pendry et al., 1999; Shelby, Smith, and Schultz, 2001; Marqués, Medina, and Rafii-El-Idrissi, 2002; Li, Aydin, and Ozbay, 2009).

This approach was exploited by Khanikaev et al. (2013) in the design of  $\varepsilon = \mu$  matched metamaterial rods arranged into a "metacrystal" in the form of a hexagonal lattice, which had a significant value of the bianisotropy  $\chi_{xy} = -\chi_{yx}$  terms. In such a hexagonal geometry, the photonic bands host doubly degenerate Dirac points, which are gapped out by the bianisotropy  $\chi$ . Around the gapped Dirac points, the effective low-energy model can then be mapped to the Kane-Mele model for the quantum spin Hall effect (see Sec. II.A.2), where the topological states are protected by the engineered symmetry  $\hat{D}$  of the electromagnetic field in the metamaterial.

Experimentally, the key signature of this photonic quantum spin Hall effect is the appearance of robust polarization-dependent edge states. Such "spin"-polarized transport has been observed for microwave photons by Chen et al. (2014) for a uniaxial hexagonal metacrystal of nonresonant meta- atoms sandwiched between two metallic plates, where the effective bianisotropy arises from field inhomogenities. The topological robustness of such edge modes was also further demonstrated by Slobozhanyuk et al. (2016), who used nearfield imaging in a square lattice of bianisotropic metamolecules to directly show the lack of backscattering around sharp corners.

The following works have shown that topological photonic states displaying the photonic analog of the quantum spin Hall effect can also be realized in an even more simple structure, as recently proposed (Ma et al., 2015) and experimentally realized (Cheng et al., 2016; Lai et al., 2016; Xiao et al., 2016). In this "metawaveguide" setup, a parallel-plate metal waveguide is filled with a hexagonal or triangular lattice of metallic cylinders, which are connected at the top and bottom to the metal plates [see Fig. 21(a)]. The geometry of the cylinders and plates is carefully optimized such that the spectrum contains an overlapping degenerate pair of Dirac cones for the TE and TM modes, allowing for the introduction of photonic pseudospin states. The bianisotropy is then introduced either by allowing a finite air gap between a cylinder and one of the metal plates or by adding an asymmetrically placed collar to the cylinder (Ma et al., 2015). Moving such a metallic collar relative to the metal plates can be understood as changing the sign of the "mass" term that opens up the gaps at the Dirac cones [see Eq. (17)] allowing for the straightforward and reconfigurable engineering of arbitrary topological domain walls. As proposed by Cheng et al. (2016), this could form the basis of a topological

![](images/769c766288b21b848e94ad9db0727aad71adec182f85853fbd41369d47d1c6a6.jpg)  
(a)

![](images/c7f6cb21c08fb0714256d08beb7c179349440675d90d928cef36e55fbebb1a3c.jpg)

![](images/a3553e98946c9f60f2ef2affd802d5c7d9da10e5a6b996d61ca36e1cf3ef902e.jpg)  
Without top plate

![](images/28dbc47dce9b276b6eda618cbf41f2cff91e513d8467a3d723e265d970dd8d54.jpg)  
(b)

![](images/f1914fb20ea242fbbe2483cd8caf63521968f3dd87cc8be2a05dc2e53e54ae0d.jpg)  
(c)  
(d)

![](images/9d6b488f7800978c23a4f8050d21d43fede650f57704dc77894008c3f126f7a2.jpg)  
FIG. 21. (a) (Top) Displacing a metallic collar relative to the two metal plates of a waveguide introduces an effective bianisotropy, coupling the electric and magnetic fields. Shifting a collar from the "down" to "up" position reverses the sign of this term and changes the sign of the "mass" term  $m$  that opens a gap at the Dirac cone, once these rods are arranged into a hexagonal or triangular lattice. (Middle and bottom panels) Photograph of the experiment, in which collars in a triangular array can be moved up and down to create arbitrary and reconfigurable topological domain walls. (b) Configuration of the topological switch where in the red (blue) regions, the metallic collars are always up (down), and where in the green region, the collars are dynamically moved from down to up to change the location of the domain wall. (c), (d) The time-resolved switching of transmission via the edge states through (c) Port 2 and (d) Port 3, with insets illustrating the power flow. Adapted from Cheng et al., 2016.

switch, in which the movement of metallic collars is used to switch the propagation path from one port to another port [see Figs. 21(b)-21(d)].

Recently, these ideas have also been extended to all-dielectric bianisotropic metamaterials (Slobozhanyuk, Mousavi et al., 2017; Slobozhanyuk et al., 2019), which may offer advantages for reducing Ohmic losses, scaling up to optical frequencies, and increasing compatibility with on-chip integration. In these systems, arrays of dielectric disks are carefully designed such that the electric and magnetic dipole modes are degenerate and electromagnetic duality is restored (Slobozhanyuk, Mousavi et al., 2017). The bianisotropy term is then introduced by adding a raised circular notch on one of the flat faces of the disk; when the disks are arranged into a hexagonal or triangular metacrystal, this gaps out the Dirac points, leading to a photonic topological insulator. This has been experimentally realized in the microwave regime for a 2D array of ceramic disks (Slobozhanyuk et al., 2019). Such arrays could also be layered to make a 3D system, analogous to a "weak" 3D topological insulator (Slobozhanyuk et al., 2019), as discussed further in Sec. V.B.

# 6. Photonic structures with crystalline symmetries

As seen, the coupling of electric and magnetic fields in bianisotropic materials requires subwavelength structures that are asymmetric in the direction perpendicular to the plane of

the topological metacrystal. Because of the small size of the features required for their fabrication, their implementation remains challenging for visible and near-infrared wavelengths. A different method to implement an analog of the quantum spin Hall effect for photons in two dimensions was proposed by Wu and Hu (2015). The configuration is based on subwavelength dielectric structures with inversion symmetry with respect to the 2D plane, which is in principle easier to implement experimentally.

The idea is to consider the lowest TM mode of a slab of cylindrical subwavelength dielectric rods surrounded by air and confined between two metallic plates [see Fig. 22(b)]. The rods are arranged in a honeycomb geometry resulting in a photonic Dirac dispersion at  $K$  and  $K^{\prime}$  points. If instead of taking the usual two-sites unit cell of the honeycomb lattice, we consider a hexagonal cluster of rods as the unit cell, the additional band folding translates the Dirac points to the center of the Brillouin zone, resulting in a doubly degenerate Dirac crossing at the  $\Gamma$  point [see Fig. 22(e)]. Solving Maxwell's equations for the lowest TM mode of the slab shows that the in-plane magnetic field distributions of the doubly degenerate lower Dirac bands present a  $p_x$ ,  $p_y$  character, while the upper Dirac bands contain states with  $d_{xy}$ ,  $d_{x^2 - y^2}$  symmetry. Their symmetric and antisymmetric combinations  $p_{\pm}$  and  $d_{\pm}$  constitute a pseudospin basis [Fig. 22(e), red and blue lines, respectively].

When shifting the rods toward the center of the hexagonal clusters, the dispersion shows the opening of a trivial gap at the Dirac point, with the upper and lower bands preserving their symmetry [Figs. 22(a) and 22(d)]. If the rods are pushed away from the center of each cluster a gap opens again, but this time it is the result of a band inversion at the Dirac point, with the new states having  $d / p$  character for the lower and upper bands [Fig. 22(c) and 22(f)] (Wu and Hu, 2015; Xu et al., 2016). The bands now possess nonzero pseudospin Chern numbers, an analog to the case of an electronic  $\mathbb{Z}_2$  topological insulator. If we now consider a ribbon of the topologically nontrivial photonic crystal, on a given edge, two bands of edge states with opposite group velocities traverse

![](images/2a384715f2d844c29e5ea04cfde56ac9122e56820536e48a9577edb1edffdcc4.jpg)  
FIG. 22. (a)-(c) Scheme of the lattice of hexagonal clusters of rods with dielectric constant  $\epsilon_{d}$ . (d)-(f) Energy-momentum dispersion corresponding to (d) contracted, (e) centered-honeycomb, and (f) expanded clusters, showing in the latter case the opening of a topological gap. (b), (d)-(f) From Wu and Hu, 2015.

the gap around the  $\Gamma$  point. The wave functions of each edge band are associated with a specific pseudospin. A similar situation takes place at the interface between two photonic crystals with trivial or nontrivial arrangements.

We can relate these topological features to a photonic pseudoquantum spin Hall effect. Indeed, while Maxwell's equation respects bosonic time-reversal-symmetry operations  $(\mathcal{T}^2 = +1)$ , in the presence of the  $C_{6\nu}$  symmetry, we can construct an antiunitary operator  $\tilde{\mathcal{T}}^2 = (\mathcal{KT})^2 = -1$  in which  $\mathcal{K}$  respects the parity of  $p$  and  $d$  eigenstates with respect to  $\pi / 2$  and  $\pi / 4$  rotations, respectively (Wu and Hu, 2015). This pseudo-time-reversal symmetry provides a Kramers doublet at the expense of keeping the  $C_{6\nu}$  geometry of the lattice. In particular, the breaking of the crystalline order at the edge of the ribbon couples the two pseudospins and results in the opening of a very small gap at the crossing of the edge state bands at the time-reversal symmetric point at the  $\Gamma$  point.

The simplicity of this proposal has triggered its implementation in a wide variety of systems, ranging from acoustics (Yves, Fleury, Lemoult et al., 2017) to phononics (He, Ni et al., 2016; Xia et al., 2017; Brendel et al., 2018). In optics it was implemented for microwaves (Yves, Fleury, Berthelot et al., 2017; Yang, Xu et al., 2018), infrared photons in a photonic crystal slab (Barik et al., 2016, 2018; Anderson and Subramania, 2017; X. Zhu et al., 2018), and metasurfaces (Gorlach et al., 2018). The experiments of Barik et al. (2018) showed that the two pseudospins characterizing each interface state band correspond to opposite circular polarizations of the confined photons. A semiconductor quantum dot embedded in the photonic crystal was used to couple single photons to the topological interface states. In a different configuration, using coupled waveguides, it was shown that the lattice configuration with the nontrivial gap can hold localized zero-dimensional defect states (Noh et al., 2018). All these features open interesting perspectives in views of engineering novel whispering-gallery-mode geometries (Siroki, Huidobro, and Giannini, 2017) or exploring quantum chiral optics (Lodahl et al., 2017).

# 7. Other proposals

Two alternative routes to simulating an artificial gauge field for a coupled optical cavity array were proposed by Umucalar and Carusotto (2011), by harnessing the polarization degree of freedom for light. In the first scheme, a nontrivial tunneling phase between lattice sites is generated by coupling together the orbital and polarization degrees of freedom, through, for example, a suitable embedding of either birefrigent slabs or optically active layers within an array of distributed Bragg reflector microcavities. In the second scheme, photons move in a single planar microcavity, where a suitable periodic lateral patterning of the cavity generates a confining lattice potential but also a position-dependent polarization mixing. As a result, the polarization of a photon then traces a closed loop in polarization space when it evanescently tunnels between lattice wells, and gains a geometrical Berry phase. This effect corresponds to a generalization for evanescent waves of how propagating photons can be imprinted with geometrical Pancharatnam (Pancharatnam, 1956) or Berry phases (Tomita and Chiao, 1986; Chiao et al., 1988). This second

scheme, in particular, offers the potential for reaching the strongly interacting photon regime (see Sec. VII.B), if the lateral patterning is scaled down to the micrometer scale, where the tighter confinement of light within the lattice wells will lead to greatly enhanced photon-photon interactions.

# C. Anomalous Floquet topological insulators

The third main class of 2D topological photonic systems is the so-called anomalous Floquet topological insulators, where unusual topological properties can emerge due to periodically driving the system in time. In this section, we set the focus on the two recent experiments of Maczewsky et al. (2017) and Mukherjee, Spracklen et al. (2017), which realized such topological properties experimentally by designing suitable propagating waveguide arrays for photons.

As already discussed in Sec. II.A.5, topological band structures can be engineered through Floquet engineering, namely, by subjecting a system to a time-periodic modulation. In two dimensions, an emblematic example is provided by the "Floquet Chern insulator," which can be realized by subjecting a honeycomb (graphenelike) lattice to a circular shaking, either produced by a mechanical modulation of the lattice (Rechtsman, Zeuner, Plotnik et al., 2013; Jotzu et al., 2014) or by irradiation (Oka and Aoki, 2009; Lindner, Refael, and Galitski, 2011). In the high-frequency regime of the drive, i.e., when  $\hbar \Omega$  is much larger than any other energy scale in the system, the dynamics is well captured by an effective Hamiltonian, whose band structure (the Floquet spectrum) exhibits Bloch bands with nonzero Chern numbers (Sec. II.A.5). In this high-frequency regime, the topological characterization of the driven system reduces to applying the standard topological band theory to the effective Hamiltonian (i.e., to the Floquet band structure); in particular, the usual bulk-edge correspondence guarantees that a Floquet Chern insulator exhibits chiral edge modes at its boundaries. This approach was pioneered in photonics (Rechtsman, Zeuner, Plotnik et al., 2013), where a 2D honeycomb-shaped array of optical waveguides was circularly modulated along a third spatial direction playing the role of "time."

This simple topological characterization breaks down when the bandwidth of a Floquet Chern insulator approaches  $\hbar \Omega$  (i.e., when the system no longer operates in the high-frequency regime  $\Omega \rightarrow \infty$ ). This can be understood in two ways. First, let us recall that the Floquet spectrum, which is associated with the Floquet operator  $\hat{\mathcal{U}}(T) = e^{-(i/\hbar)T\hat{H}_{\mathrm{eff}}}$ , is only uniquely defined within a Floquet-Brillouin zone  $[- \hbar \Omega/2; \hbar \Omega/2]$ . Consequently, when the effective bandwidth approaches  $\hbar \Omega$ , gap-closing events are possible at the Floquet-Brillouin zone's boundaries (Kitagawa, Berg et al., 2010). This can produce a cancellation of the Chern numbers associated with the Floquet bands, however, and this is a crucial observation, topological chiral edge states can still be present in the inner part of the spectrum. Such a coexistence of chiral edge modes with seemingly trivial Bloch bands, which is in apparent contradiction with the bulk-edge correspondence, is referred to as "anomalous Floquet topological phases" (Rudner et al., 2013), as opposed to the standard Floquet Chern insulators previously discussed. A second, and more fundamental, reason for this breakdown of the usual

topological characterization stems from the fact that the micromotion plays a crucial role as soon as the period of the drive  $T$  no longer sets the shortest time scale in the problem: in the "low-frequency" regime, the dynamics (including the topological nature of the system) cannot possibly be ruled by  $\hat{H}_{\mathrm{eff}}$  only; see Sec. II.A.5. All together, this indicates that the anomalous Floquet topological phase cannot be accurately characterized by the Chern number related to the effective Hamiltonian, but rather by a distinct topological invariant: a "winding number," which fully takes the micromotion into account (Kitagawa, Berg et al., 2010; Rudner et al., 2013; Carpentier et al., 2015; Nathan and Rudner, 2015).

An instructive toy model leading to a dramatic instance of an anomalous Floquet topological phase was introduced by Rudner et al. (2013). In a certain parameter regime, the system simultaneously exhibits a single completely flat Bloch band (with a trivial Chern number) together with a topologically protected chiral edge mode. As represented in Fig. 23(a), the driven system consists of a 2D square lattice, whose allowed hopping events are activated in a sequential and  $T$ -periodic manner: the time-evolution operator describes a four-step quantum walk. One should note that the circular nature of the sequence imprints a chirality to the system, similarly to the circular shaking leading to Floquet Chern insulators in graphene-like lattices (Oka and Aoki, 2009; Lindner, Refael, and Galitski, 2011; Rechtsman, Zeuner, Plotnik et al., 2013; Jotzu et al., 2014); such a chirality is crucial for the emergence of chiral edge modes in the system. The effective (Floquet) band structure of this model is shown in Fig. 23(b) for the extreme case where the activated-hopping amplitude  $J$  is exactly set on resonance  $J = \hbar \Omega$ . The resulting unique (two-degenerate) Bloch band is completely flat, which reflects the fact that the stroboscopic motion, i.e., the motion over each period of the drive  $T$ , is necessarily restricted to closed loops in any region of the bulk. However, as in the quantum Hall effect, such "orbits" reduce to skipped orbits at the boundaries, hence resulting in a chiral edge mode [see Fig. 23(b)]. This simple picture is confirmed by the topological analysis of the model, which associates a nontrivial winding number to the Floquet Bloch band (Rudner et al., 2013).

Recently, two independent experimental teams (Maczewsky et al., 2017; Mukherjee, Spracklen et al., 2017) reported on the realization of this intriguing "Rudner-toy" model, using an array of laser-inscribed coupled waveguides using the technique described by Szameit and Nolte (2010). Both teams considered a 2D array of optical waveguides, defined in the  $x-y$  plane, with a propagation direction  $z$  playing the role of time. As illustrated in Fig. 23(a), the model relies on a sequential activation of neighboring coupling within this 2D square lattice. Maczewsky et al. (2017) and Mukherjee, Spracklen et al. (2017) achieved this goal by spatially modulating the waveguides along the  $z$  direction, in such a way that different pairs of waveguides are locally moved together (to activate the coupling) and then apart (to switch it off); see Fig. 23(c) for a sketch of this protocol. These independent teams implemented two distinct configurations of the model, the activated couplings being homogeneous in Maczewsky et al. (2017), while these were chosen to be inhomogeneous in Mukherjee,

![](images/f416b3eed42a5bfd88d1d2f41089a2462106881e900433b6ad2c1b65c7c6c315.jpg)

![](images/397f0eacb898074fefdec3f9d01f8a666261198d72400011d7c08c0cd5c18ea6.jpg)

![](images/76a19a62fa64d8a0114f1405e723a2e17d1c01a450ee2456d18c7f4dd871c63f.jpg)  
FIG. 23. (a) Sketch of the Rudner et al. toy model for anomalous Floquet topological phases (Rudner et al., 2013), where hopping on a square lattice is activated in a cyclic and time-periodic manner. (b) Energy bands and sketch of the corresponding states in the ideal case where the activated-hopping amplitude  $J$  is exactly set on resonance  $J = \hbar \Omega$ , where  $\Omega$  is the drive frequency. The dispersionless bulk band (blue) corresponds to cyclotron-localized states and is associated with a zero Chern number; dispersive branches (green and red) correspond to propagating edge states (skipped-cyclotron orbits). These edge states are topologically protected by a winding number that takes the full-time evolution (including the micromotion) into account (Nathan and Rudner, 2015). (c) The optical waveguide implementation of Mukherjee, Spracklen et al. (2017), where the sequential activation of neighboring coupling was finely engineered. (d) Experimental evidence for the simultaneous existence of robust propagating edge states and (quasi)localized bulk states. (a), (b) Adapted from Rudner et al., 2013. (c), (d) From Mukherjee, Spracklen et al., 2017.

![](images/d5335b87ea50b7181c19f48c4953ff7b3e9319283597e18c5c28b7c18d5d1bab.jpg)

Spracklen et al. (2017). However, both experiments reached the aforementioned "anomalous" regime of the topological phase diagram, where chiral edge modes are uniquely determined by the nontrivial winding number (Kitagawa, Berg et al., 2010; Rudner et al., 2013; Nathan and Rudner, 2015). Mukherjee, Spracklen et al. (2017) demonstrated the realization of the anomalous Floquet topological phase through a thoughtful study of the activated-coupling strength (which uniquely identified the realized anomalous phase within the topological phase diagram) combined with direct observations of the chiral edge states propagation and bulk localization [see Fig. 23(d)]. This analysis was further validated through numerical simulations based on the theoretical model. Maczewsky et al. (2017) also signaled the anomalous phase by demonstrating the dispersionless nature of the bulk (i.e., the existence of a flat band) and the chiral nature of the edge mode. This latter work also analyzed a topological transition from the anomalous topological phase to a trivial phase (characterized by the absence of edge mode) by designing lattices with decreasing coupling strengths. These two experiments demonstrated the high tunability offered by laser-inscribed photonic crystals in view of designing intriguing toy models and simulating exotic phases of matter.

Various other schemes have been proposed to reach the anomalous regime of Floquet topological systems, which can be applied to a variety of physical platforms (Kitagawa, Berg et al., 2010; Kitagawa, Rudner et al., 2010; Reichl and Mueller, 2014; Leykam, Rechtsman, and Chong, 2016; Quelle et al., 2017). In this broader context, robust localized states, associated with nontrivial winding numbers (Kitagawa, Rudner et al., 2010), were first demonstrated in a photonic

setup realizing a 1D quantum walk (Kitagawa et al., 2012); a similar setup was recently explored in view of directly extracting winding numbers through Zak-phase measurements performed in the bulk (Cardano et al., 2017). Besides, the winding number of 2D anomalous Floquet topological insulators was also measured in a microwave network, using a dimensional-reduction (topological pump) approach (Hu et al., 2015). Finally, the existence of anomalous Floquet edge modes was also shown in a designer surface plasmon structure operating in the microwave regime (F. Gao et al., 2016).

# D. Topology in gapless photonic systems

Another important class of topological systems is gapless photonic lattices with Dirac points. The primary example of this kind is the honeycomb lattice of coupled photonic resonators or waveguides. The Hamiltonian describing the dynamics of photons in these lattices is equivalent to that of  $p_z$  electrons in graphene, giving rise to two bands with linear crossings, at the Dirac points, as illustrated in Fig. 24(d) for a lattice of polariton resonators. In the absence of external fields, spin-orbit coupling, or temporal modulation the system remains ungapped. Nevertheless, this type of lattice presents features that are topological in the sense that they can be related to certain topological invariants or geometrical properties of the system. These features include topological edge states, topological phase transitions, and the emergence of synthetic gauge fields when suitably deforming the lattice.

![](images/c6dc5a83b822d9185df6c668656bec249b4a563bee39a65049f0115411a7583f.jpg)  
Microwave resonators

![](images/c2245a746dc432d97a55d8e6f7e94cf1210703c38cc29ade539c090f5ea2438f.jpg)  
FIG. 24. (a) Image of a honeycomb lattice of microwave resonators with armchair, bearded, and zigzag edges. (b) Measured density of states as a function of microwave frequency  $\nu$ . The peak at the Dirac energy  $\nu_{d}$  indicates the presence of zero-energy states. From Bellec et al., 2014. (c) Scanning electron microscope image of a honeycomb lattice of coupled polariton micropillars. (d) Photoluminescence spectrum measured at the center of the lattice showing Dirac crossings (left), and at the zigzag edge (right), showing a flat band of edge states (pointed by the arrow). From Milicevic et al., 2015. (e) Representation of a lattice of coupled waveguides and (f) measured momentum-space distribution of the transmission through the zigzag and bearded edges. Red lines show the position of the Dirac points. From Plotnik et al., 2014.

![](images/805a7b5503cb48e8dae2097bbc59672f3363950b5bb82b01f2f234dda9ea2fa3.jpg)  
Polariton lattices

![](images/a32a4c8aa65097c5c2228b027cef983b3496639a3ac670a2b912197be7ea08c4.jpg)  
(d)

![](images/b8f56e625d0c6905f3dd68f0f66f66913f5fbc2dfda22e328f90b8b4ccbc15fb.jpg)  
Coupled waveguides

![](images/f677a0ab821d8b97034fac9d99009afb8bb77ba4dd33f22680286bd14a62fcea.jpg)

To analyze these topological properties, let us consider the hopping of the lowest photonic mode of each individual resonator to its nearest neighbor. In the tight-binding approximation with nearest-neighbor hoppings, the Hamiltonian in momentum space is chiral and takes the form of Eq. (19) in the  $A$ ,  $B$  sublattice basis depicted in Fig. 25(h) by green and blue dots. In this case,  $Q(\mathbf{k})$  in Eq. (19) takes the form  $Q(\mathbf{k}) = -t_{1}e^{i\mathbf{k}\cdot \mathbf{R}_{1}} - t_{2}e^{i\mathbf{k}\cdot \mathbf{R}_{2}} - t_{3}e^{i\mathbf{k}\cdot \mathbf{R}_{3}} \equiv |Q(\mathbf{k})|e^{-i\theta (\mathbf{k})}$ , where  $t_{1,2,3}$  are the nearest-neighbor hopping amplitudes and  $\mathbf{R}_{1,2,3}$  are the vectors connecting a site to its three nearest neighbors [see Fig. 25(h)]. For equal hoppings ( $t_{1} = t_{2} = t_{3} \equiv t$ ) the two bands of eigenvalues of the honeycomb Hamiltonian are  $\epsilon (\mathbf{k}) = \pm t|Q(\mathbf{k})|$  (Wallace, 1947), resulting in Dirac-like crossings at the  $K$ ,  $K^{\prime}$  points in the first Brillouin zone. The eigenfunctions are  $|u_{k,\pm}\rangle = (1 / \sqrt{2})(e^{-i\theta (\mathbf{k})},\pm 1)^{\dagger}$ .

The honeycomb Hamiltonian has been implemented in a number of photonic systems including microwave resonators (Bittner et al., 2010; Bellec et al., 2013a), photorefractive crystals (Peleg et al., 2007; Song et al., 2015; Sun et al., 2018), atomic vapor cells (Z. Zhang et al., 2018), coupled microlasers (Nixon et al., 2013), polariton lattices (Kusudo et al., 2013; Jacqmin et al., 2014), and propagating waveguides (Rechtsman, Zeuner, Tünnermann et al., 2013; Plotnik et al., 2014). Some examples are shown in Fig. 24.

The first noticeable feature of the eigenstates is their pseudospin structure, with two components that reflect the underlying  $A$ ,  $B$  interlaced triangular sublattices. The pseudospin structure results in particular scattering properties close to the Dirac cones: using a honeycomb lattice imprinted in a photorefractive medium it was shown that the conical

![](images/71dd18c9c2ecc02566ce909bfbd960ba8e324843bd2052c879d38f9687eb166c.jpg)  
(b)

![](images/a9b6d6a9f4de3e368505f2e3fba9fbea0fa9a58bbcfb40c95c3889d897c0444e.jpg)  
(c)

![](images/20e721e55ce7ecd91dbf95bf7af8dff51468cf6bccb11496db25dfe842539ed4.jpg)  
FIG. 25. Stream plots of  $\theta(k_{\perp}, k_{\parallel})$  in momentum space for zigzag, bearded, and armchair edges, and for different values of the homogeneous strain  $t_1 / t_2$  ( $t_2 = t_3$ ). The colored areas show the regions of  $k_{\parallel}$  in which  $\mathcal{W} = 1$ , corresponding to the presence of edge states. Black solid and dashed lines represent the 1D Brillouin zones in  $k_{\parallel}$  and  $k_{\perp}$ , respectively. (a)-(g), (i) Adapted from Bellec et al., 2014. Red points show the position of the Dirac points. (h) Scheme of the honeycomb lattice and nearest-neighbor hoppings.

![](images/7137ce7fcde82a59b85d59f73257ce06435aba334f16befcbfd7547371feed3f.jpg)  
(e)

![](images/1300331cd3063f7c941da57017c6cbc6d925145d4742dc8d0c16af58f12076a3.jpg)  
(f)

![](images/dced4adb54fdd2f9921069f24490e081134f5e69fabad463ca7044652b8744b2.jpg)

![](images/75b808f538299575a9c231614b720bf9fa52c463caacb187c9dac7443a4e4526.jpg)  
(g)  
(h)

![](images/638976f643483275bf86d7487a3a13bdf48f4b55542ad9b4379a986ebc98e9df.jpg)

![](images/7309ca341e737260f6938b01c9f20fae1d934e7296cbded417aec37a7213a161.jpg)  
(i

diffraction characteristic of Dirac crossings (Peleg et al., 2007) presents an orbital angular momentum  $l = \pm 1$ , depending on whether sublattice  $A$  or  $B$  is excited (Song et al., 2015).

A second relevant feature of the eigenfunctions is their nontrivial Berry phase: if the eigenfunctions are transported adiabatically on a closed loop in momentum space around one of the Dirac points, the eigenfunctions change sign (Castro Neto et al., 2009). In other words, they get a Berry phase of  $\pm \pi$ , the sign being opposite for the  $K$  and  $K^{\prime}$  points. This effect is present even when a gap is opened at the Dirac cones, which can be induced by introducing an on-site energy difference  $\Delta$  between the  $A$  and  $B$  sublattices. In this case, a nonzero Berry curvature extends around the Dirac points. Therefore, if a wave packet is created close to one of the Dirac points and subject to acceleration, the Berry curvature results in an anomalous velocity whose sign depends on the Dirac point around which the wave packet is created (Ozawa and Carusotto, 2014). An efficient way of accelerating the photon wave packet is to design a lattice whose resonators continuously increase in size from one lattice site to the next: the decreasing photon confinement results in an on-site energy gradient. If the photon lifetime is long enough, the force can induce magnetic Bloch oscillations with a displacement perpendicular to the gradient and a direction determined by the Dirac point around which oscillations take place (Cominotti and Carusotto, 2013).

Photonic simulators can also be used to explore other properties of propagating wave packets in a honeycomb lattice. For instance, the chiral symmetry of the honeycomb Hamiltonian is preserved in the presence of a potential step, resulting in phenomena such as Veselago lensing (Cheianov, Fal'ko, and Altshuler, 2007), the Goos-Hänchen effect (Grosche, Szameit, and Ornigotti, 2016), or Klein tunneling (Dreisow et al., 2012; Solnyshkov et al., 2016). Dissipation present, for example, in polariton lattices, does not significantly affect these phenomena (Ozawa et al., 2017). Dirac cones can also be used to tailor the dispersion of photonic structures, even producing "epsilon-near-zero" materials (Huang et al., 2011; Moitra et al., 2013).

Edge states in Dirac systems: One of the characteristics of the honeycomb lattice is the existence of zero-energy edge states in finite-size ribbons (Klein, 1994; Nakada et al., 1996). These edge states are topological in the sense that they are related to the winding properties of the bulk Hamiltonian (Ryu and Hatsugai, 2002). To understand this bulk-edge relation, let us consider a graphene ribbon of finite size in the direction perpendicular to the edge  $(\perp)$ , and infinite in the parallel direction  $(\parallel)$ . By Fourier transforming the real-space Hamiltonian along this axis, we can reduce it to an effective 1D Hamiltonian for each value of  $k_{\parallel}$  (Castro Neto et al., 2009; Delplace, Ullmo, and Montambaux, 2011). This effective 1D chiral Hamiltonian has the same form as the SSH Hamiltonian discussed in Sec. II.A.3, characterized by the complex function  $Q(k_{\perp}, k_{\parallel}) = |Q(k_{\perp}, k_{\parallel})| e^{i\theta(k_{\perp}, k_{\parallel})}$ . We can then apply the topological arguments discussed in Sec. II.A.3. The number of pairs of zero-energy edge states, appearing at the two edges of the ribbon, is thus determined by the winding of  $\theta(k_{\perp}, k_{\parallel})$ , Eq. (20), along the  $k_{\perp}$  direction over the first Brillouin zone (Ryu and Hatsugai, 2002; Delplace, Ullmo, and Montambaux, 2011; Mong and Shivamoggi, 2011):

$$
\mathcal {W} \left(k _ {\parallel}\right) = \frac {1}{2 \pi} \int_ {\mathrm {B Z}} d k _ {\perp} \frac {d \theta \left(k _ {\perp} , k _ {\parallel}\right)}{d k _ {\perp}}. \tag {68}
$$

The information about the specific type of edge is contained in the choice of unit cell dimer and unit vectors when writing down the honeycomb Hamiltonian, such that they allow for the full reconstruction of the lattice (including the edges). Therefore, the information on the edges is reflected in the specific form of  $\theta(k_{\perp}, k_{\parallel})$  when writing down Eq. (19) (Delplace, Ullmo, and Montambaux, 2011). Figures 25(b) and 25(e) show  $\theta(k_{\perp}, k_{\parallel})$  for zigzag and bearded edges, respectively. The colored areas indicate the values of  $k_{\parallel}$  for which  $\mathcal{W} = 1$ , corresponding to the existence of edge states.

The direct access to the wave functions in photonic lattices has been employed to study the local properties of these edge states. Their existence has been evidenced experimentally in lattices of coupled waveguides (Plotnik et al., 2014), microwave resonators (Bittner et al., 2012; Bellec et al., 2014), and polaritons (Milicevic et al., 2015), showing that edge states for zigzag and bearded terminations connect Dirac cones in complementary regions in momentum space [Figs. 25(b) and 25(e)], while armchair terminations do not possess any edge state ( $\mathcal{W} = 0$  for any  $k_{\parallel}$ ).

The topological arguments used to predict the existence of edge states in a honeycomb lattice can be extended to other Hamiltonians, for instance, when more than one mode per site is involved. As long as the system possesses the chiral symmetry, they can be written in the form of Hamiltonian (19). With more than one mode per site,  $Q(\mathbf{k})$  takes the form of a  $n \times n$  matrix whose determinant can be written as  $\det Q(k) \equiv |\det Q(k)|e^{i\theta (k)}$ . The existence of pairs of zero-energy edge states is again given by the winding of  $\theta (\mathbf{k})$  along the momentum direction perpendicular to the edge (Kane and Lubensky, 2014). An example of this kind of chiral Hamiltonian is the  $p$ -orbital version of graphene, in which orbitals with  $p_x$ ,  $p_y$  geometry are considered at each lattice site (Wu et al., 2007). This  $4 \times 4$  orbital Hamiltonian has been implemented in a polariton honeycomb lattice when considering the doubly degenerate first excited states of each coupled micropillar. The spectrum consists of four bands with Dirac crossings, and the presence of zero-energy edge states for different kinds of terminations is well accounted for by the analysis of the winding of  $\theta (\mathbf{k})$  just presented (Milicevic et al., 2017).

Similar arguments can be applied to Dirac Hamiltonians without chiral symmetry, for instance with next-nearest-neighbor hopping or with a staggered potential in the  $A$ ,  $B$  sublattices, both effects giving rise to nonzero diagonal terms in Eq. (19). The presence of edge states can also be determined via winding arguments, but their energy is not necessarily zero (Mong and Shivamoggi, 2011).

Valley Hall edge states: Propagating edge states with weak topological protection can be engineered in lattices with appropriately staggered potentials. The staggered potential between the  $A$ ,  $B$  sublattices  $\Delta$  breaks the inversion symmetry and opens a gap at the Dirac points. By integrating the Berry curvature around each Dirac point, we can define a valley Chern number whose sign is opposite for  $K$  and  $K^{\prime}$  points

(the total Chern number of the band still being zero). If the staggered potential is changed to  $-\Delta$ , the gap is still open but the signs of the valley Chern numbers switch between  $K$  and  $K^{\prime}$  points. When joining two honeycomb semi-infinite ribbons subject to opposite staggered potentials  $\Delta$  and  $-\Delta$ , it has been shown that interface states appear in two bands that traverse the gap (Zhang et al., 2011; Chen and Dong, 2016; Fefferman, Lee-Thorp, and Weinstein, 2016; Goldman et al., 2016; Ma and Shvets, 2016; Bleu, Solnyshkov, and Malpuech, 2017b; Qiu et al., 2017). Indeed, if the  $K$  and  $K^{\prime}$  valleys of the two lattices have opposite valley Chern numbers, the gap needs to close locally at those points at the interface between the two lattices (Ma and Shvets, 2016). This situation is restricted to very specific conditions, for instance, it applies to zigzag interfaces. For this configuration, the propagation of a wave packet in an interface state with a given valley polarization is protected against any perturbation that does not mix the two valleys, i.e., bends of the interface of  $120^{\circ}$ , which preserve the zigzag character of the interface (Chen and Dong, 2016; Ma and Shvets, 2016; X. Wu et al., 2017). Interface states between photonic crystals which exhibit valley Hall and quantum spin Hall effects have also been experimentally demonstrated (Kang et al., 2018).

For armchair interfaces, the breaking of translational symmetry in the direction perpendicular to the interface mixes the  $K$  and  $K^{\prime}$  points of each lattice, and the valley Chern number is not well defined. Similarly, if the gap becomes too large  $(|\Delta |\gtrsim t)$  in zigzag interfaces, the Berry curvatures associated with both valleys overlap. The valley Chern numbers are not well defined anymore and a gap opens in the edge state bands (Noh, Huang, Chen, and Rechtsman, 2018).

Despite the fact that valley Hall edge states are not robust against arbitrary spatial disorder at the interface, they can be used to route photons in photonic structures (X. Wu et al., 2017; Noh, Huang, Chen, and Rechtsman, 2018) and to design delay cavities in Si photonics technologies (Ma and Shvets, 2016). A route to recover topological protection is to use chiral nonlinear excitations (i.e., vortices) as proposed recently for a polariton fluid in a honeycomb lattice (Bleu, Malpuech, and Solnyshkov, 2018).

Effect of strain: The application of strain to an ungapped honeycomb lattice  $(\Delta = 0)$  strongly modifies its spectrum and eigenfunctions and, consequently, its topological properties. We consider two main classes of strain: (i) homogeneous strain, in which hopping is different along different spatial directions  $(t_{1} \neq t_{2} \neq t_{3})$ , and (ii) inhomogeneous strain, in which hopping takes different values at different positions  $[t_{i}(\mathbf{r})]$ . The first case was theoretically studied by Montambaux et al. (2009). They predicted a topological phase transition occurring when one of the three nearest-neighbor hopping amplitudes  $(t_{1})$  is twice as large as the other two  $(t_{2} = t_{3})$ . At the transition point  $(t_{1} = 2t_{2})$ , the two nonequivalent Dirac cones merge and disappear resulting in the opening of a full gap. This transition was first experimentally observed in cold atoms (Tarruell et al., 2012), but it is in photonic lattices where its effect on the existence of edge states has been studied (see Fig. 25). Experiments in lattices of microwave resonators and coupled waveguides (Rechtsman, Plotnik et al., 2013; Bellec et al., 2014) have shown that above the transition point  $(t_{1} > 2t_{2})$ , ribbons with zigzag

terminations contain a flat energy band of edge states covering the whole momentum space, while for bearded boundaries, edge states disappear. For armchair terminations, edge states appear for any value of the unidirectional strain as long as the anisotropy axis is not parallel to the edge, as in Figs. 25(g) and 25(i) (Bellec et al., 2013b, 2014). The existence of edge states in homogeneously strained honeycomb lattices can also be predicted from topological arguments. The Hamiltonian including this kind of strain still possesses the chiral symmetry, and the number of zero-energy edge states is governed by the winding of  $\theta (\mathbf{k})$ . Interestingly, homogeneous strain has been employed to synthesize critically tilted Dirac cones in the orbital  $p$  bands of lattices of coupled micropillars (Miliévić et al., 2018).

The second kind of strain concerns the continuous variation of the hopping over the lattice. Originally studied in the context of electronic graphene, this kind of inhomogeneous strain has been shown to induce a gauge field (Kane and Mele, 1997). If the strain takes the specific trigonal shape  $(u_r, u_\theta) = \beta r^2 (\sin 3\theta, \cos 3\theta)$ , where  $u_r, u_\theta$  are the real-space displacements of the positions of the carbon atoms in polar coordinates, the modified hopping induces a gauge field for electrons at the Dirac cones corresponding to a homogeneous pseudomagnetic field perpendicular to the graphene sheet (Guinea, Katsnelson, and Geim, 2010). In other words, the Hamiltonian describing the time evolution of electrons in the strained lattice can be cast in the form of an unstrained honeycomb Hamiltonian subject to a homogeneous pseudomagnetic field perpendicular to the graphene plane. Note, however, that this field does not break time-reversal symmetry: it has opposite signs at the two Dirac points. Therefore, edge states appearing in the gaps between consecutive Landau levels are associated with propagation on both directions along the edge (Gopalakrishnan, Ghaemi, and Ryu, 2012; Salerno et al., 2017) and backscattering-protected transport is not expected.

Translated to the photonic realm, this configuration provides an efficient way of inducing a pseudomagnetic field acting on photons as if they were charged particles. This precise idea was implemented by Rechtsman, Zeuner, Tunnermann et al. (2013) in a lattice of coupled waveguides by continuously varying their separation (i.e., the nearest-neighbor photon hopping) following the above-mentioned strain configuration. The value of the valley dependent pseudomagnetic field acting on the propagating photons can take effective values of several thousand tesla, much higher than strengths of real magnetic field currently realizable in the laboratory. The main consequence is the emergence of Landau levels in the vicinity of the Dirac points (Castro Neto et al., 2009). Analogously to the effect of a real magnetic field in graphene, the energy of the photonic Landau levels  $n_{L}$  scales as  $\pm \sqrt{n_{L}}$ . This was observed in numerical tight-binding calculations and experimentally via the localization of a wave packet on the edge of a strained lattice (Rechtsman, Zeuner, Tunnermann et al., 2013), attesting to both the presence of flat Landau bands and states localized at the edge emerging from the gauge field.

The trigonal strain discussed so far is not the only way of inducing a homogeneous magnetic field. Salerno et al. (2015)

![](images/8765cc2b0c7cf9d5ab08257350fa14c73adf334e4e121dd6224b8688af5aba2d.jpg)  
FIG. 26. Tight-binding calculation of the level structure of a uniaxially strained photonic graphene ribbon as a function of  $k_{y}$ , perpendicular to the strain direction. The hopping strength along the narrow dimension of the ribbon increases linearly from one edge to the other, resulting in a gauge field for photons. The Dirac points, located at  $k_{y} = 1.2 / a$  with  $a$  being the nearest-neighbor distance, split into Landau levels (red lines). The lowest one,  $n_{L} = 0$  at  $E = 0$ , is flat, while the others have a nonzero group velocity. From Salerno et al., 2015.

showed that linear uniaxial strain along one of the crystallographic directions results in a homogeneous pseudomagnetic field similar to that emerging from trigonal strain. Figure 26 shows the emergence of Landau levels associated with pseudomagnetic fields of opposite sign at the  $K$ ,  $K^{\prime}$  points. The most noticeable feature in this tight-binding calculation is that, except for  $n_{L} = 0$ , the Landau levels are not completely flat. The reason is that the position-dependent hopping results in a local Dirac velocity that varies along the lattice (de Juan, Sturla, and Vozmediano, 2012).

The engineering of Landau levels in photonic structures is particularly interesting in the quest for confined lasing geometries. The possibility of introducing flat gapped bands in the bulk of a photonic lattice, with a high density of states, could be used to fabricate low threshold on-chip lasers. Moreover, the combination of gauge fields with gain and losses provides exciting perspectives on the study of the parity anomaly and sublattice selective lasing (Schomerus and Halpern, 2013).

# IV. TOPOLOGICAL PHOTONICS IN ONE DIMENSION

The previous section was devoted to a review of two-dimensional photonics systems where topological concepts were first investigated. In the present section, we now turn our attention to one-dimensional models in Sec. IV.A and then, in Sec. IV.B, to the topological pumping effects that such systems have been used to study.

# A. Topology in 1D chiral systems

In one dimension, topological phases of matter cannot exist without imposing symmetries on the system (Kitaev, Lebedev, and Feigelman, 2009; Schnyder et al., 2009). An important symmetry in one dimension, which can lead to topological phases, is chiral symmetry, for which the representative one-dimensional topological model is the Su-Schrieffer-Heeger (SSH) model as introduced in Sec. II.A.3.

The first experimental realization of the SSH model and its associated topological edge state in a photonics context was in a

photonic superlattice (Malkova et al., 2009). Since then, the SSH model or related models have been discussed and realized in photonic crystals (Keil et al., 2013; Xiao, Zhang, and Chan, 2014), electromagnetic metamaterials (Tan et al., 2014; Yannopapas, 2014), plasmonic and dielectric nanoparticles (Poddubny et al., 2014; Ling et al., 2015; Sinev et al., 2015; Slobozhanyuk et al., 2015; Slobozhanyuk, Poddubny et al., 2016; Kruk et al., 2017), plasmonic waveguide arrays (Bleckmann et al., 2017; Cherpakova et al., 2018), polariton micropillars (Solnyshkov, Nalitov, and Malpuech, 2016), and coupled optical waveguides (Naz et al., 2018). Lasing in the edge state of the SSH model was recently experimentally observed by St-Jean et al. (2017), Parto et al. (2018), and Zhao et al. (2018). These experiments constitute the first realizations of topological lasers, i.e., lasers which make use of topological edge states as we further discuss in Sec. VIII.B. The interplay between the SSH model and the radiative loss of photons have also been discussed in photonic crystals (Schomerus, 2013; Poshakinskiy et al., 2014), microwave cavity arrays (Poli et al., 2015), and coupled waveguide arrays (Zeuner et al., 2015). The SSH model of optical waveguides with periodic modulation and its edge states have been studied with Floquet theory (B. Zhu et al., 2018). The SSH model has also been realized with electric circuits (Lee et al., 2018), and the Zak phase (Berry phase across the Brillouin zone) has been measured to show its topological nature (Goren et al., 2018). By properly adding loss, the parity-time  $(\mathcal{PT})$  symmetric version of the SSH model was realized by Weimann et al. (2017). A one-dimensional electric circuit has also been shown to exhibit quantized energy transport due to the topological nature of the system in the presence of dissipation (Rosenthal et al., 2018). More details on non-Hermitian topological models are given in Sec. VI.A. There is also a proposal to realize the one-dimensional Jackiw-Rebbi model, introduced in Sec. II.A.1, in a driven slow-light setup (Angelakis, Das, and Noh, 2014), where the zero-energy bound mode can be probed through the transmission spectrum.

Another strategy to realize 1D chiral Hamiltonians with nontrivial topology involves discrete-time quantum walks (Kitagawa, Rudner et al., 2010; Kitagawa, 2012). As discussed in Sec. II.A.5, a discrete-time quantum walk consists of a repeated application of a set of operations represented by a unitary matrix  $\hat{\mathcal{U}}$ . Topological properties of such unitary evolution can be understood analogously to Floquet topological phases by defining an effective Hamiltonian  $\hat{H}_{\mathrm{eff}}$  through  $\hat{\mathcal{U}} = e^{-i\hat{H}_{\mathrm{eff}}T / \hbar}$ . If  $\hat{H}_{\mathrm{eff}}$  has nontrivial topology, its effect can be detected through the discrete-time quantum walk. The great flexibility in choosing a set of operations to realize  $\hat{\mathcal{U}}$  and hence  $\hat{H}_{\mathrm{eff}}$  makes the discrete-time quantum walk a powerful platform to explore topological phases of matter.

A topologically nontrivial discrete-time quantum walk was first experimentally realized by Kitagawa et al. (2012) using single photons going through a series of polarization rotations. In the experiment, a topological bound state between the interface of regions with different winding numbers was observed. Subsequently, Cardano et al. (2015, 2016, 2017) studied the topological invariant of a quantum walk in the orbital angular momentum space and detected the topological transition between different phases. Following the proposal

(Tarasinski, Asbóth, and Dahlhaus, 2014), the topological invariant of a one-dimensional quantum walk was measured and its robustness to disorder was assessed, using a fiber loop architecture based on the time-multiplexing technique (Barkhofen et al., 2017).

# B. Topological pumps

Electric currents are usually generated by applying a voltage across a material, inducing longitudinal charge transport. Using Faraday's induction law, we can similarly generate electric currents via a time-dependent variation of a magnetic flux. In both cases, the longitudinal conductivity is determined by the microscopic details of the material and can take arbitrary values. As seen in Sec. II, the situation is completely different in topological systems, where currents can show quantization effects.

In particular, in topological charge pumps (Thouless, 1983), Faraday's induction law is encoded in an adiabatic cyclic variation of a Hamiltonian potential that mimics the magnetic flux threading in a higher-dimensional topological Chern insulator. Consequently, the charge transport across the system per unit cycle of the pump parameter turns out to be quantized in much the same way that quantized Hall conductance appears in the higher-dimensional static Chern insulator. This feature has drawn much attention for controlled low-current nanoscale device applications (Kouwenhoven et al., 1991).

The first experiments toward the implementation of a topological charge pump were conducted in solid-state systems with demonstrations of quantized charge transport using single electron pumps (Geerligs et al., 1990; Kouwenhoven et al., 1991; Pothier et al., 1991, 1992). The quantization, however, of the pumped charge in these devices relied on simple Coulomb blockade rather than on topological concepts. Later attempts using open mesoscopic systems incorporated geometrical ideas to generate a quasiadiabatic, nonquantized current that is proportional to the area enclosed in parameter space (Spivak, Zhou, and Beal Monod, 1995; Brouwer, 1998; Swtkes et al., 1999; Zhou, Spivak, and Altshuler, 1999; Mottonen, Vartiainen, and Pekola, 2008). The challenge of realizing quantized topological pumping was only recently accomplished using cold atoms in optical superlattices (Lohse et al., 2016; Nakajima et al., 2016).

In this section, we introduce realizations of topological pumps in photonic systems. Unitary photonic topological pumps have been realized using coupled waveguide arrays (Kraus et al., 2012; Verbin et al., 2015), whereas non-Hermitian pumps with exceptional points were realized using microwave cavities (Hu et al., 2015). In both realizations, the experiments focused on states localized at the system's boundary which were directly excited by the incident light. Similar to the aforementioned cold-atom experiments (Lohse et al., 2016; Nakajima et al., 2016) theoretical proposals have addressed the possibility of studying quantized bulk pumping in photonic systems (Mei et al., 2015; Ke et al., 2016). Geometric pumping has been experimentally realized using a fiber loop architecture (Wimmer et al., 2017).

In the following, we focus on the first photonic realizations of topological pumps using waveguide arrays (Kraus et al.,

2012). While it is technologically challenging to modulate the waveguide profile in a way to precisely realize the on-site modulation involved in Thouless' original topological pump model (29), the excellent control in the waveguide spacing achievable with femtosecond laser microfabrication technology (Szameit et al., 2007; Szameit and Nolte, 2010) allowed for the emulation of an off-diagonal pump model where the interwaveguide hopping amplitudes are slowly modified along the propagation axis  $z$  and the light evolves according to the Hamiltonian

$$
\hat {H} _ {\text {o f f}} = - J \sum_ {x} \left[ \left(1 + \frac {2 J _ {x y}}{J} \cos [ 2 \pi \alpha x / a + \phi (z) ]\right) \hat {a} _ {x} ^ {\dagger} \hat {a} _ {x + a} + \mathrm {H . c .} \right], \tag {69}
$$

where  $J$  is the bare hopping amplitude from waveguide  $n$  to waveguide  $n - 1$ ,  $2J_{xy}$  is the amplitude of its  $z$ -dependent modulation (which is equivalent to time-dependent modulation in propagating geometries, cf. Sec. III.A.2), and  $\alpha$  is a spatial modulation frequency; see Fig. 27(a) for an illustration.

The mapping between the 2D quantum Hall effect on a lattice and the 1D pump discussed in Sec. II.A.4 and Eqs. (14) and (29) can be extended beyond the Harper-Hofstadter model (Kraus and Zilberberg, 2012). Performing dimensional extension on Eq. (69), we obtain a 2D tight-binding model where motion along  $x$  occurs via a standard nearest-neighbor hopping in the  $x$  direction and motion along  $y$  occurs only via diagonal hoppings to next-nearest neighbors (Hatsugai and Kohmoto, 1990)

$$
\hat {H} = - J \sum_ {x, y} \left(\hat {a} _ {x + a, y} ^ {\dagger} \hat {a} _ {x, y} + \frac {J _ {x y}}{J} e ^ {i 2 \pi a x / a} \hat {a} _ {x + a, y + a} ^ {\dagger} \hat {a} _ {x, y} + \mathrm {H . c .}\right). \tag {70}
$$

Each plaquette in the model is threaded by  $2\pi \alpha$  flux as in the Harper-Hofstadter model, cf. Eq. (14).

The model (69) is commonly known as the off-diagonal Harper model (Ketoja and Satija, 1997; Jitomirskaya and Marx, 2012). Figure 27(b) depicts its spectrum as a function of  $\phi$ . We observe a characteristic gapped structure with topological modes crossing the gaps as a function of  $\phi$ . These modes are localized at the system's boundary when they are well within the energy gap, while they become spatially extended when they spectrally approach the bulk modes; see the insets of Fig. 27(b).

In the experiment [Fig. 27(c)], light is injected via fiber coupling directly into the left end. The initial  $\phi$  is chosen in a way to support a localized state on this boundary, so that the injected light can directly excite this state. The value of  $\phi$  is then scanned along the propagation axis by correspondingly varying the interwaveguide distances. Depending on the final value of  $\phi$ , the spatial intensity distribution at the output will recover the spatial shape of the wave function of the topological state in different regimes, e.g., either extended over the bulk or even completely localized at the other boundary of the system. Such pumping through the boundary states of the pump highlights the existence of localized states

![](images/2b4e7c9c1b46dc5a4c850f7ccda270a86e04b057f90ae9095c0bf8b4487a0933.jpg)  
(a)

![](images/86b47c8ce1c36fc55059f360ae8fc45e32ab37d05b762d83be90d24b0687ab1f.jpg)  
(c)

![](images/835a844471b0eea29a79902663184758134957e43653d32978664e821b8698c6.jpg)  
(b)  
FIG. 27. Experimental observation of adiabatic pumping via topologically protected boundary states in a photonic waveguide array. (a) An illustration of the adiabatically modulated photonic waveguide array, constructed by slowly varying the spacing between the waveguides along the propagation axis  $z$ . Consequently, the injected light experiences an adiabatically modulated Hamiltonian  $H_{\mathrm{off}}(\phi(z))$  as it propagates and is pumped across the sample. (b) The spectrum of the model Eq. (69) as a function of the phase  $\phi$  for  $t = 40/75$ ,  $2t_{xy} = 0.6$ , and  $b = (1 + \sqrt{5}) / 2$ . In the experiment, a 21-site lattice was used and  $\phi$  was scanned between  $0.35\pi$  and  $1.75\pi$ , marked by arrows (and red dots). The insets depict the spatial density of a boundary eigenstate as a function of the position at three different stages of the evolution: At  $\phi = 0.35\pi$ , the eigenstate is localized on the right boundary. At  $\phi = \pi$ , it is delocalized across the system, while at  $\phi = 1.75\pi$  the state is again localized, but on the left boundary. (c) Experimental results: Light was injected into the rightmost waveguide at  $z = 0$  with  $\phi = 0.35\pi$ . The measured intensity distributions as a function of the position are presented at different stages of the adiabatic evolution, i.e., different propagation distances. It is evident that during the adiabatic evolution, the light initially injected on the rightmost waveguide crosses the lattice from right to left and is finally concentrated on the leftmost waveguides. From Kraus et al., 2012.

on both ends of the system for suitable values of  $\phi$ , in agreement with the pump's bulk-edge correspondence.

Moreover, it also illustrates the fact that the topological boundary mode on one end of the system can be connected to the state localized on the other end through semiadiabatic scanning of  $\phi$  in sufficiently short systems. The latter is an interesting effect that is not implied by the bulk topology of

the system: the bulk topology implies in fact that a quantized number of boundary states will cross the gap on each side of the sample as a function of  $\phi$ , but does not necessarily imply that these states have to be directly connected.

Using the same technology and extending this idea further, a topological pump was realized for an off-diagonal Fibonacci chain. This realization relied on a mapping between quasiperiodic chains and topological pumps (Kraus et al., 2012; Kraus and Zilberberg, 2012; Verbin et al., 2015). Thus, using a two-parameter pumping, the Fibonacci chain was deformed into an off-diagonal Harper model, pumped as above, and deformed back into a Fibonacci chain (Verbin et al., 2015). Furthermore, topological phase transitions between quasiperiodic chains with smooth boundaries were studied using photonic waveguide arrays (Verbin et al., 2013). A study of the spectral flow of edge states across the energy gaps of a Fibonacci quasicrystal was reported by Baboux et al. (2017) by scanning a suitable structural parameter through many copies of a polariton lattice device.

Interestingly, simultaneous realizations of atomic and photonic 2D topological pumps were recently reported. Such pumps were shown to be directly mappable to a 4D quantum Hall system (Kraus, Ringel, and Zilberberg, 2013). While the atomic experiment (Lohse et al., 2018) performed a direct mapping of the Berry curvature by looking at anomalous transport in the bulk of the system, the photonic experiment (Zilberberg et al., 2018) studied the boundary states associated with a second Chern number response using similar methods to those previously discussed.

# V. TOPOLOGICAL PHOTONICS IN HIGHER DIMENSIONS

Having reviewed the photonic realizations of two- and one-dimensional topological models, we now briefly highlight recent and on-going works in higher-dimensional topological systems. In Secs. V.A and V.B, we focus on the study of three-dimensional topological photonics, for which macroscopic photonic crystals and metamaterials operating in the microwave domain have provided the main experimental platform. Then, in Sec. V.C, we discuss topological physics in even higher spatial dimensions, including perspectives in this direction opened up through the concept of "synthetic dimensions."

# A. Three-dimensional gapless phases

# 1. Weyl points and helicoid surface states

As briefly reviewed in Sec. II.A.3, three-dimensional band structures can host Weyl points, corresponding to gapless points around which bands disperse linearly with respect to the three quasimomenta [Eq. (22)]. Each Weyl point can be associated with a topological Chern number, calculated by integrating the Berry curvature over a two-dimensional surface enclosing the Weyl point. It can be shown that Weyl points have Chern numbers of  $\pm 1$  [Fig. 28(a)] and require the breaking of either  $\mathcal{P}$  (parity) and/or  $\mathcal{T}$  (time-reversal) symmetry. If  $\mathcal{T}$  is broken, the minimum number of Weyl points in the band structure is two, whereas, if only  $\mathcal{P}$  is broken, as is typically much easier to implement in experiments, then the minimum number of Weyl points is four. For a strong enough

![](images/a70706fff20a1b8da142f6d005f458d6baf49b9926986141a047d5624dc08ce7.jpg)  
(a) Weyl points

![](images/32c34182058d541a207e0d84393b24750b500edf4b36011c90633f6fa4c1eeab.jpg)

![](images/06941388a2bde0dd533df9a88afdcb675a46391431106a0c026b15c51057345b.jpg)  
(c) Quadratic Weyl  
Double Weyl points

![](images/3536f1b26abc5e5136e5f60036284dae756c8a8d72d4904647a61c9094cdb39b.jpg)  
(d) Spin-1 Weyl

![](images/92e4de9ba5fafbc638c97d24ccb3f25aa5308611e04451b8f60f77178f104ec0.jpg)  
(b) Helicoid surface state  
(e) Charge-2 Dirac  
FIG. 28. (a) Weyl points of opposite Chern numbers (C). (b) Surface dispersion near the projections of a pair of Weyl points with opposite Chern numbers, where the red and blue cones represent the bulk states projection at  $k_{+}$  and  $k_{-}$ . The surface state is plotted using the Riemann sheet of  $\mathrm{Im}(\log [(k - k_{+}) / (k - k_{-})])$  in the complex plane of  $k$ . The green surface arc is an isofrequency contour. (c)-(e) Double-Weyl points of two bands, three bands, and four bands. (f) A Dirac point consists of two Weyl points of opposite Chern numbers. (b) From Fang, Lu et al., 2016. Other panels adapted from T. Zhang et al., 2018.

![](images/7d6f15e123bb735764d68a7da2d3a43aaa3c708a991aca1941bf71f4c32e6e56.jpg)

![](images/25a03dbb6b1500ef4c830cc02c3e7ffb4a9329fda9a77097a88c4a4af57cda4e.jpg)  
(f) Dirac point

tilting of the Weyl cone, the group velocities of the two crossing bands can have the same sign along one direction, in which case one speaks of a type-II Weyl point (Soluyanov et al., 2015).

The topological character of Weyl points is reflected in the appearance of topologically protected states on the surface of the three-dimensional system. These surface states are topologically equivalent to helicoid Riemann surfaces (Fang, Lu et al., 2016; T. Zhang et al., 2018) defined with the two-dimensional surface Brillouin zone as the complex plane, shown in Fig. 28(b). A helicoid surface is a noncompact Riemann surface, which is unbounded in the frequency axis, corresponding to the gapless nature of the Weyl surface state. Locally around each Weyl cone, the surface states can be expressed as  $\omega \propto \mathrm{Im}[\log (k^C)]$ , where  $C$  is the Chern number of the Weyl point. The bulk Weyl points project onto the surface Brillouin zone as poles ( $C > 0$ ) and zeros ( $C < 0$ ) of the multivalued helicoid surface sheets winding around these singularities. Their winding direction is determined by the sign of  $C$ , while the order of the pole or zero is given by  $|C|$ . As shown in Fig. 28(b), the isofrequency contours of the helicoid surface are always open arcs connecting the surface projections of the positive and negative bulk Weyl points. These open surface arcs are known as "Fermi arcs" in Weyl semimetals.

Theoretically, Weyl points were first proposed to appear in double-gyroid photonic crystals, with a breaking of  $\mathcal{P}$  or  $\mathcal{T}$  (L. Lu et al., 2013). Since then, theoretical studies have shown that Weyl points could be realized in optical lattices (Dubček, Kennedy et al., 2015; Roy et al., 2018), photonic superlattices (Bravo-Abad et al., 2015), magnetized plasmas (W. Gao et al., 2016), chiral metamaterials (Gao et al., 2015; Xiao, Lin, and Fan, 2016; Liu et al., 2017), Floquet networks (Ochiai, 2016;

Wang, Zhou, and Chong, 2016), chiral woodpile crystals (Chang et al., 2017), magnetic tetrahedral crystals (Z. Yang et al., 2017), and classical (Luo, Yu, and Weng, 2018) and quantum (Mei et al., 2016) circuits. In an ideal Weyl system, all Weyl points would be frequency isolated and symmetry related at the exact same frequency (Wang, Jian, and Yao, 2016). We also note that ideal Weyl points move the classical free-space scattering laws from dc to the Weyl frequency by design (M. Zhou et al., 2017), and that, after including losses, Weyl points evolve into exceptional lines (Xu, Wang, and Duan, 2017).

Experimentally, Weyl points were demonstrated at microwave frequencies in a double-gyroid photonic crystal (Lu et al., 2015), metallic photonic crystals with multi-Weyl points and surface transport (Chen, Xiao, and Chan, 2016), photonic metamaterials with type-II Weyl points and surface arcs (B. Yang et al., 2017), in lumped-element circuits (Lu et al., 2019), and at optical frequencies in coupled waveguides with type-II Weyl points and surface states (Noh, Huang, Leykam et al., 2017). Synthetic Weyl points in the parameter space of 1D dielectric stacks were also observed by Q. Wang et al. (2017), and ideal Weyl points have been found in a metallic design (B. Yang et al., 2018). In this latter platform, the helicoid surface states of the four Weyl points were experimentally mapped out and were topologically equivalent to a Riemann sheet defined by the Jacobi elliptical function, analytical in the whole double-periodic surface Brillouin zone.

# 2. Multi-Weyl and Dirac points

A Weyl point of nonzero Chern number does not require any symmetry for protection, other than translational symmetry. With an increase of symmetry, multi-Weyl points can stabilize at high-symmetry momenta (Xu et al., 2011; Fang, Yu, and Fan, 2012a; Chen, Xiao, and Chan, 2016; Chang et al., 2017). For example, double-Weyl points (T. Zhang et al., 2018) of Chern number of  $\pm 2$  can form between two bands as a quadratic Weyl point, between three bands as a spin-1 Weyl point, or between four bands as a charge-2 Dirac point, as shown in Figs. 28(c)-28(e). In the latter case, charge 2 refers to the Berry charge (Chern number) of 2, corresponding to the overlapping of Weyl points of the same Chern number. The double-Weyl surface states can be mapped, in the entire Brillouin zone, to the double-periodic Weierstrass elliptic functions: a type of Riemann surface with second-order poles and zeros (T. Zhang et al., 2018).

More generally, a Dirac point in 3D refers to the overlapping of any two Weyl points of opposite Chern numbers, as shown, for example, in Fig. 28(f). Such 3D Dirac points were discussed by L. Lu et al. (2016), H. Wang et al. (2016), Guo et al. (2017, 2018), Slobozhanyuk, Mousavi et al. (2017), and H.-X. Wang et al. (2017). Since a 3D Dirac point has zero Chern number, it does not require the breaking of either  $\mathcal{P}$  or  $\mathcal{T}$ .

# 3. Nodal lines and surface

As well as the above point degeneracies (nodal points), line degeneracies are also important in 3D. Such nodal lines (Fang, Weng et al., 2016) can be protected by  $\mathcal{PT}$  symmetry with  $\pi$  Berry phase, same as the 2D Dirac cones. The nodal lines known so far can be classified into several families, namely,

nodal rings (Burkov, Hook, and Balents, 2011), nodal chains (Bzdusek et al., 2016), nodal links (Yan et al., 2017), and nodal knots (Bi et al., 2017a). In photonics, a nodal ring was proposed in gyroid photonic crystals (L. Lu et al., 2013) and nodal chains were proposed in a face-centered cubic lattice (Kawakami and Hu, 2017) and discovered experimentally in a simple-cubic metallic photonic crystal (Yan et al., 2018). Nodal lines can also exist in two-dimensional photonic crystals (Lin et al., 2017), such as at the zone boundary of two-dimensional lattices with glide reflection symmetry and  $\mathcal{T}$ . Nodal lines can also carry a  $Z_{2}$  charge (Fang et al., 2015).

Nodal surfaces can be protected by screw rotations and  $\mathcal{T}$ . It can even carry nonzero Chern numbers (Xiao and Fan, 2017b).

# B. Three-dimensional gapped phases

Gapping topological degeneracies such as Weyl and Dirac points is the most effective way to obtain 3D band gaps supporting various topological interfacial states. The space-group analysis of photonic bands (Watanabe and Lu, 2018) is helpful for such designs.

# 1.3D Chern crystal

As introduced in Sec. II.A.3, a three-dimensional quantum Hall system is characterized by a triad of first Chern numbers  $\left[\mathbf{C}^{(1)}\equiv \left(C_x^{(1)},C_y^{(1)},C_z^{(1)}\right)\right]$ , as indicated in Fig. 29(a). In such systems, the gapless surface states are unidirectional sheets, whose number and directionality equals the magnitude and sign of the Chern numbers for that surface (Koshino, Aoki,

![](images/14d381ed25d690950ecbca31215abbe27dcc1b82aa75b4508b0552971abe4df1.jpg)  
T-breaking phases  
3D Chern crystal  $(\mathsf{C}^{(1)},\mathsf{C}^{(1)},\mathsf{C}^{(1)})$  surface sheets

![](images/85e62e99cd0729184034cf201126b1a9eb0c17aeea76ab19ece722e9bb62bf17.jpg)  
3D gapped phases  
One-way fiber  $C^{(2)}$  dislocation mode

![](images/d35c6494342754bf56c15321dc257f78137b5d9646cee18156b106fe36d761ff.jpg)  
Single surface Dirac cone (strong phase,  $Z_{2}$ )

![](images/cb2273112a40d9f29b02bf7d4c4f8b1ab81bdbbfbe36b560d53fb0375d949c56.jpg)

![](images/25d4801267f6234e6574406c6684ff30a692dd58a6c20e36d9c021576bc7687f.jpg)  
T-invariant phases  
Two surface Dirac cones (weak phase)  
FIG. 29. List of 3D gapped phases in photonics, in which (a)-(c) require  $\mathcal{T}$  breaking while (d) and (e) do not. (a) Analog of the 3D Chern crystal labeled by the three first Chern numbers. (b) One-way fiber of second Chern number. (c) Single-Dirac cone surface state with a  $\mathbb{Z}_2$  invariant. (d) Two surface Dirac cones similar to those of weak 3D topological insulators. (e) Spatial-symmetry-protected gapless quadratic touchings with a  $\mathbb{Z}_2$  invariant.

![](images/558e691384a3c93987ed42d8230a5ac4734f5b997fc993aeb19ee83c8bdc3dc0.jpg)  
Quadratic degeneracies  $(Z_{2})$

and Halperin, 2002). In the context of photonics, the elementary case of  $\mathbf{C}^{(1)} = (0,0,1)$  was proposed by annihilating a single pair of Weyl points, by supercell coupling, in the magnetic gyroid photonic crystals (Lu, Gao, and Wang, 2018). Note that as first Chern numbers vanish in the presence of time-reversal symmetry, the breaking of  $\mathcal{T}$  is required to realize such gapped topological phases.

# 2. One-way fiber

One-way fiber modes can form along topological line defects in 3D magnetic photonic crystals, illustrated in Fig. 29(b). This was proposed by Bi and Wang (2015) by Dirac mass engineering and designed in the gyroid photonic crystal by Lu, Gao, and Wang (2018). The coupling of two Weyl points of opposite Chern numbers makes a 3D Dirac point, as already introduced. The resulting Dirac Hamiltonian

$$
H _ {D} = \hbar v \left(q _ {x} \sigma_ {x} + q _ {y} \sigma_ {y} + q _ {z} \sigma_ {z} \tau_ {z}\right) + m \tau_ {+} + m ^ {*} \tau_ {-} \tag {71}
$$

has a complex mass term  $m$ , where  $\tau_z$  and  $\tau_{\pm} \equiv (\tau_x \pm i\tau_y) / 2$  are Pauli matrices acting on the valley degrees of freedom. In-plane winding of its argument  $\mathrm{Arg}[m]$  generates a vortex line in 3D supporting a zero mode at the vortex core, topologically protected by the second Chern number  $C^{(2)}$  in the 4D parameter space  $(k_x, k_y, k_z, \theta)$ , where  $\theta$  is the winding angle of  $m$ .

In the photonic context, such a topological defect line inside an otherwise fully gapped gyroid photonic crystal can be obtained by means of a helical winding of the supercell modulation coupling the two Weyl points. Depending on the spatial pitch and the handedness of the helical winding, one-way fiber modes of arbitrary  $C^{(2)}$  can then be readily designed with arbitrary number of one-way modes.

This is in direct contrast with the one-way edge mode in 2D Chern crystals where high Chern numbers are difficult to obtain (Skirlo, Lu, and Soljacic, 2014; Skirlo et al., 2015). Another advantage of the one-way fiber design is that all one-way modes have almost identical group and phase velocities, due to the absence of sharp boundaries.

# 3. Single surface Dirac cone

A single-Dirac-cone surface state, the hallmark of 3D topological insulators (Fu, Kane, and Mele, 2007), can also be realized on the surface of magnetic photonic crystals, as shown by L. Lu et al. (2016) and illustrated in Fig. 29(c). Instead of the Kramers' degeneracy of electrons due to  $\mathcal{T}$ , the double degeneracy in photonics can be replaced by a crystalline symmetry, e.g., glide reflection. On the other hand,  $\mathcal{T}$  has to be broken to split the dispersions in all surface directions away from degeneracy.

The starting point to construct this phase is a pair of 3D Dirac points pinned at the high-symmetry points of the bulk Brillouin zone. By breaking  $\mathcal{T}$  using magnetic materials, the authors gapped the 3D Dirac points and obtained the gapless single-Dirac cone surface states. The topological invariant is  $\mathbb{Z}_2$  (Fu, Kane, and Mele, 2007; Moore and Balents, 2007; Roy, 2009). When the glide reflection symmetry is broken uniformly on the surface, the single-Dirac cone opens a frequency gap. Other than that, the surface state is robust

against arbitrary random disorder, i.e., when the glide symmetry is preserved on average on the surface (Lu, Joannopoulos, and Soljačić, 2016).

# 4. Nonmagnetic designs

The above topological phases with 3D bulk gaps require  $\mathcal{T}$  breaking for highly robust interfacial states. However, the magnetic response is extremely weak toward optical frequencies, which has motivated the search for  $\mathcal{T}$ -invariant designs. One approach has been to search for nonmagnetic designs that mimic weak 3D topological insulators, which can be viewed as stacks of 2D topological insulators. In photonics, this was first proposed for all-dielectric bianisotropic metamaterials (Slobozhanyuk, Mousavi et al., 2017), as introduced in Sec. III.B.5, and has been experimentally realized very recently in a 3D array of bianisotropic metallic split-ring resonators (Yang, Gao et al., 2019).

A second approach to  $\mathcal{T}$ -invariant designs has been to search for systems, where the topological properties are protected instead by crystalline symmetries. The first proposal of such a topological crystalline insulator (Fu, 2011) (see Sec. III.B.6 for the discussion of such states in two dimensions) utilized  $C_4$  rotation symmetry and exhibited double degeneracies at two surface momentum points. This defined a  $\mathbb{Z}_2$  invariant for its surface states to connect gaplessly. At the degenerate point, the dispersion was quadratic due to the  $C_4$  symmetry and  $\mathcal{T}$ . As illustrated in Fig. 29(e), this phase is realizable in photonic crystals (Yannopapas, 2011; Alexandradinata et al., 2014). A concrete design for a tetragonal photonic crystal was also proposed by Ochiai (2017).

# C. Toward even higher dimensions

Topological phases of matter with spatial dimensions of 4 or higher can also be of experimental relevance in photonics. As already introduced in Sec. IV.B, a recent experiment has used topological pumping to probe a four-dimensional quantum Hall system (Zilberberg et al., 2018). In this approach, some of the dimensions are replaced by externally tuned parameters, effectively freezing out the dynamics along these directions. An alternative approach, which could also offer access to the dynamics of particles moving in effectively spatial four dimensions, is based on so-called synthetic dimensions. In this, the key concept is to reinterpret internal degrees of freedom as spanning additional spatial dimensions, so that higher-dimensional lattice models are simulated in lower-dimensional systems. In this section, we first review the development of synthetic dimensions in general, before discussing progress in the exploration of four-dimensional topological systems with photons.

# 1. Synthetic dimensions

There are several different ways to make the effective spatial dimensionality of a lattice system larger than the physical dimensionality of the real space in which the lattice is located. One natural idea for this purpose is to increase the connectivity of the lattice, as proposed by Tsomokos, Ashhab, and Nori (2010) for superconducting qubit circuits, by Jukić and Buljan (2013) for photonic lattices, by Schwartz and Fischer (2013) for

multidimensional laser-mode lattices, and by Graß et al. (2015) for trapped ions. Another strategy that can allow for even greater flexibility is to use the internal degrees of freedom, reinterpreting these as if they label different sites along an additional synthetic dimension in the system, as originally proposed by Boada et al. (2012) in the context of ultracold atomic gases, and later extended by Celi et al. (2014) to allow for complex hoppings along the synthetic direction, and so to realize quantum Hall systems. Methods to create lattice structures more complex than just a square lattice were proposed by Boada et al. (2015), Anisimovas et al. (2016), and Suszalski and Zakrzewski (2016).

The idea of synthetic dimensions was soon experimentally realized in the context of cold atoms by two groups (Mancini et al., 2015; Stuhl et al., 2015), in which a two-dimensional ladder with a magnetic field was simulated using a one-dimensional chain of atoms. The following experiments have then extended the synthetic dimension idea by using the different electronic states of atoms (Livi et al., 2016; Kolkowitz et al., 2017) and discrete states in momentum space (An, Meier, and Gadway, 2017). Furthermore, there are theoretical proposals to use harmonic oscillator eigenstates (Price, Ozawa, and Goldman, 2017) and orbital angular momentum states (Pelegrí et al., 2017) as synthetic dimensions. Typically, the interparticle interaction along the synthetic direction is very long ranged, resulting in a variety of interesting phenomena (Graß, Celi, and Lewenstein, 2014; Zeng, Wang, and Zhai, 2015; Barbarino et al., 2016; Bilitewski and Cooper, 2016; Lacki et al., 2016; Calvanese Strinati et al., 2017; Junemann et al., 2017; Taddia et al., 2017).

In photonics the first proposal for how to implement a synthetic dimension was made by Luo et al. (2015), and later extended by Luo et al. (2017) and X.-F. Zhou et al. (2017), in which different orbital angular momentum states of light, coupled via spatial light modulators, were regarded as the synthetic dimension. This was followed by a proposal in optomechanics (Schmidt et al., 2015), in which photon and phonon degrees of freedom were considered as two lattice sites along the synthetic dimension. Ozawa et al. (2016) and Yuan, Shi, and Fan (2016) have proposed to use different frequency modes of a multimode ring resonator, coupled via external modulation of refractive index, as a synthetic dimension. By modulating a resonator with multiple frequencies, models with any dimensions can also be simulated (Yuan et al., 2018). A synthetic frequency dimension could also be realized in a Raman medium, where the synthetic magnetic field is controlled by the alignment of the two Raman beams (Yuan, Wang, and Fan, 2017). Instead of different frequency modes, the angular coordinate within a ring resonator may be used as a synthetic dimension (Ozawa and Carusotto, 2017), in which the interphoton interaction is local along the synthetic direction, in contrast to extremely long-ranged interactions in other proposals.

There have also been many theoretical proposals for the different physics that could be accessed with synthetic dimensions. In a single resonator with a synthetic dimension, it may be possible to study the edge state of the SSH model (X.-F. Zhou et al., 2017) and Bloch oscillations along the synthetic direction (Yuan and Fan, 2016). In a one-dimensional array of optical cavities with one synthetic

dimension, the effect of topological edge states of two-dimensional Chern insulators may be observed (Luo et al., 2015). Such a topological edge mode can be useful for high-efficiency frequency conversion if there is an edge along the synthetic direction made of frequency modes (Ozawa et al., 2016; Yuan, Shi, and Fan, 2016) and for realizing an optical isolator if an edge is along the spatial direction (Ozawa et al., 2016). A two-dimensional array of resonators could also be augmented by one frequency dimension to realize photonic Weyl points (Lin et al., 2016; B. Y. Sun et al., 2017) or a weak 3D topological insulator (Lin et al., 2018). In the long run, one may expect that the idea of synthetic dimensions could find applications in increasing the complexity of optical networks in photonic devices, also in connection with frequency-multiplexing (Saleh and Teich, 2007) and optical comb (Schwartz and Fischer, 2013; Cai et al., 2017) techniques.

The experimental observation of topologically protected edge states in a photonic lattice with a synthetic dimension was recently pioneered by Lustig et al. (2018). A two-dimensional array of single-mode waveguides was used, with the synthetic dimension being encoded in the modal space of coupled waveguides. This allowed for the generation of a synthetic magnetic field and, thus, of a topologically nontrivial two-dimensional model supporting chiral edge states.

# 2. Four-dimensional quantum Hall effect

As mentioned in Sec. IV.B, a recent photonic experiment has used topological pumping to probe the edge states of a four-dimensional quantum Hall system (Zilberberg et al., 2018), based on the proposal of Kraus, Ringel, and Zilberberg (2013). Concurrently with this experiment, the hallmarks of the quantized bulk response of the 4D quantum Hall effect (23), including the second Chern number, were measured through the topological pumping of a two-dimensional ultracold atomic system (Lohse et al., 2018). By defining the second Chern number in a general parameter space, this topological invariant has also been shown to be experimentally relevant in helically modulated fibers (Lu, Gao, and Wang, 2018), as discussed in Sec. V.B, where the angular coordinate in the cross section of a fiber acts as the fourth parameter, and in ultracold gases, where it was measured over a parameter space spanned by properties of two Raman lasers applied to the system (Sugawa et al., 2018).

The first proposal for observing the full dynamics of a four-dimensional system was presented by Jukić and Buljan (2013), based on using photonic lattices with high connectivity to study four-dimensional solitons. Using a synthetic dimension to directly observe the four-dimensional quantum Hall was then originally proposed in ultracold atomic gases (Price et al., 2015) and soon after extended to photonics (Ozawa et al., 2016). These proposals focused on the four-dimensional tight-binding model (Kraus, Ringel, and Zilberberg, 2013):

$$
\begin{array}{l} \hat {H} = - J \sum_ {\mathbf {r}} \left(\hat {a} _ {\mathbf {r} + a \hat {e} _ {x}} ^ {\dagger} \hat {a} _ {\mathbf {r}} + \hat {a} _ {\mathbf {r} + a \hat {e} _ {y}} ^ {\dagger} \hat {a} _ {\mathbf {r}} \right. \\ + e ^ {i 2 \pi \Phi_ {1} x / a} \hat {a} _ {\mathbf {r} + a \hat {e} _ {z}} ^ {\dagger} \hat {a} _ {\mathbf {r}} + e ^ {i 2 \pi \Phi_ {2} y / a} \hat {a} _ {\mathbf {r} + a \hat {e} _ {w}} ^ {\dagger} \hat {a} _ {\mathbf {r}} + \mathrm {H . c .}), \tag {72} \\ \end{array}
$$

where  $a_{\mathbf{r}}$  is the annihilation operator of a particle at position specified by a four-dimensional vector  $\mathbf{r} = (x, y, z, w)$  with  $w$  being the synthetic direction, and  $a$  being the lattice spacing. The fluxes  $\Phi_1$  and  $\Phi_2$  pierce the  $x-z$  and  $y-w$  planes, respectively. This is a generalization of the two-dimensional Harper-Hofstadter Hamiltonian to a 4D model with magnetic fields applied in two orthogonal planes, breaking time-reversal symmetry. However, unlike in 2D, time-reversal symmetry breaking is not the only route to observing a quantum Hall effect. Instead, 4D topological lattice models have also been proposed that exploit time-reversal-invariant spin-dependent gauge fields (Qi, Hughes, and Zhang, 2008), or lattice connectivity for spinless particles (Price, 2018).

Under the addition of weak electromagnetic perturbations, the filling of a 4D topological energy band would lead to a quantized nonlinear Hall current proportional to the second Chern number of the band (23). However, in contrast to the atomic case, in photonic systems with loss, this current  $j^{\mu}$  is not a direct observable. Instead, it was proposed to extract this topological response from the shift of the center of mass of the photonic steady-state intensity distribution under a monochromatic pump (Ozawa and Carusotto, 2014; Ozawa et al., 2016).

# VI. GAIN AND LOSS IN TOPOLOGICAL PHOTONICS

In this section, we discuss the interplay of gain and loss with topology in photonics. We divide this section into two main parts; in the first, we discuss non-Hermitian topological models with gain and loss, while in the second, we focus on recent works concerning topology in Bogoliubov systems.

# A. Non-Hermitian topological photonics

The study of topological physics with photons allows for the exploration of phenomena inaccessible in the context of condensed matter. A case in point is non-Hermiticity in the form of optical gain and loss. In photonics, gain and loss is much more common than in electrons in solids: gain media are the basis for lasers, and loss of photons is ubiquitous in every photonic device (loss is associated with absorption and surface roughness of a waveguide, for example).

There have thus been a series of works delving into the interplay of non-Hermiticity and topology with a number of disparate aims [including a recent review on the topic by Martinez Alvarez et al. (2018)]. Inspired by a model proposed by Rudner and Levitov (2009), Zeuner et al. (2015) used an optical waveguide array to demonstrate that the winding number of a one-dimensional topological system could be extracted from a non-Hermitian quantum walk. In that work, it was precisely the finite lifetime (induced by optical loss) of the "quantum walker" that allowed for the observation of a topological transition. This amounts to the extraction of a topological number of a Hermitian system using non-Hermiticity, rather than exploring the topological invariants and edge states of non-Hermitian systems per se.

Another direction of non-Hermitian topological photonics is parity-time  $(\mathcal{PT})$  symmetric (Makris et al., 2008; Rüter et al., 2010) topological systems. These are systems with balanced gain and loss such that the Hamiltonian commutes

with the  $\mathcal{PT}$  operator (where  $\mathcal{P}$  represents parity and  $\mathcal{T}$  represents time reversal). It was shown (Bender and Boettcher, 1998) that such systems may exhibit real eigenvalue spectra despite their non-Hermiticity; they have been the basis of a major research effort in photonics due to the possibility of overcoming parasitic loss and absorption in optical devices using gain. Thus,  $\mathcal{PT}$ -symmetric systems allow for the possibility of well-defined bands and gaps and are thus a natural place to start in studying non-Hermitian topological effects. That said, it was shown (Esaki et al., 2011; Hu and Hughes, 2011) that a large class of systems that are  $\mathcal{PT}$  symmetric in the bulk must have edge states that "break"  $\mathcal{PT}$ ; namely, they have complex eigenvalues. Fortunately, under certain conditions, topological edge states with real eigenvalues can be found and have been demonstrated (Weimann et al., 2017). Topological edge states in  $\mathcal{PT}$ -symmetric quantum walks have also been experimentally observed (Xiao et al., 2017). Recent work has examined  $\mathcal{PT}$ -symmetric Hamiltonians in the context of topological superconductors (Kawabata, Ashida et al., 2018).

A number of other unconventional phenomena arise when non-Hermiticity and topology are combined. One example is photonic "tachyonlike" dispersion (Szameit et al., 2011) that was demonstrated in the form of exceptional rings in photonic crystals (Zhen et al., 2015) as well as "Fermi arc"-type states that connect between exceptional points in two-dimensional systems (Kozii and Fu, 2017; Malzard and Schomerus, 2018a; Zhou et al., 2018); a related phenomenon was examined in the context of heavy-fermion systems (Yoshida, Peters, and Kawakami, 2018). "Exceptional rings" arise in three-dimensional topological systems exhibiting Weyl points (Szameit et al., 2011; Xu, Wang, and Duan, 2017), although to date these have not been experimentally realized. The enhancement of topological interface states in one-dimensional systems was proposed (Schomerus, 2013) and demonstrated in the microwave regime (Poli et al., 2015) (along with a related work in optics) (Pan et al., 2018). Furthermore, it was shown that topological states absent when the system is Hermitian can be induced by adding losses (Malzard, Poli, and Schomerus, 2015). The interplay of non-Hermiticity and flat bands has been shown to result in a photonic analog of Aharonov-Bohm caging (Leykam, Flach, and Chong, 2017). Beyond photonic systems, the interplay between non-Hermiticity or dissipation and topology has been explored in a number of theoretical works in varying contexts (Diehl et al., 2011; Bardyn et al., 2012, 2013; Budich and Diehl, 2015; Budich, Zoller, and Diehl, 2015). Finally, two-dimensional topological edge state lasers (Bahari et al., 2017; Bandres et al., 2018; Harari et al., 2018), intrinsically non-Hermitian systems, have been observed recently; thus, it will become increasingly necessary to put on firm ground the complex interplay of non-Hermiticity and topological protection. More details on topological lasers are given in Sec. VIII.B.

Despite this progress, the major challenge of non-Hermitian topological photonics remains the formulation of a general framework akin to that which exists for Hermitian systems. In particular, perhaps the key contemporary question is what is the right topological invariant to consider for a given non-Hermitian Hamiltonian (Esaki et al., 2011; Hu and Hughes, 2011), and what is its relevance to bulk-edge correspondence

(some recent progress has been made in this direction) (Lee, 2016; Leykam et al., 2017; Weimann et al., 2017; Kawabata, Shiozaki, and Ueda, 2018; Shen, Zhen, and Fu, 2018; Yao, Song, and Wang, 2018; Yao and Wang, 2018; Yin et al., 2018)? In this spirit, there has been a recent effort to classify non-Hermitian topological systems (Gong et al., 2018) in the same vein as Hermitian ones. This is certainly not a direct generalization however: it may be the case that the symmetries conventionally associated with the Hermitian case may not be well suited to classify Hamiltonians in the non-Hermitian case. Specifically, recent work has shown that particle-hole and time-reversal symmetries are aspects of the same larger symmetry when Hermiticity is relaxed (Kawabata et al., 2019).

# B. Emergent topology of Bogoliubov modes

Photons under a parametric driving can be described by a Hamiltonian with terms that do not conserve the number of photons. Such number nonconserving bosonic systems can have topological features which are qualitatively different from fermionic topological systems. To understand the origin of the number nonconserving terms, let us consider a photonic cavity whose resonant frequency is  $\omega$  and assume that the cavity is made of optically nonlinear material with a second-order nonlinear susceptibility  $\chi^{(2)}$ . When one pumps the system with frequency  $2\omega$ , the nonlinearity converts the pumped photon into two photons with frequency  $\omega$  in the cavity. Assuming that the pump beam is sufficiently strong and can be treated classically, the effective Hamiltonian describing the cavity takes the following form (Gerry and Knight, 2005):

$$
\hat {H} _ {\text {c a v i t y}} = i \hbar \chi^ {(2)} \left(\beta^ {*} \hat {a} ^ {2} - \beta \hat {a} ^ {\dagger 2}\right), \tag {73}
$$

which does not conserve the number of photons, where  $\hat{a}$  is the annihilation operator of a photon in the cavity and a  $\mathbb{C}$ -number  $\beta$  characterizes the pumping field. Such a cavity can be aligned to form a periodic lattice. The second-quantized momentum-space Hamiltonian of the lattice system can be written in the following form:

$$
\begin{array}{l} \hat {H} _ {\text {l a t t i c e}} = \frac {1}{2} \sum_ {\mathbf {k}} \left( \begin{array}{c c} \hat {\Psi} _ {\mathbf {k}} ^ {\dagger} & \hat {\Psi} _ {- \mathbf {k}} \end{array} \right) H _ {\mathbf {k}} \left( \begin{array}{c} \hat {\Psi} _ {\mathbf {k}} \\ \hat {\Psi} _ {- \mathbf {k}} ^ {\dagger} \end{array} \right), \\ H _ {\mathbf {k}} = \left( \begin{array}{c c} A (\mathbf {k}) & B (\mathbf {k}) \\ B (- \mathbf {k}) ^ {*} & A (- \mathbf {k}) ^ {t} \end{array} \right), \tag {74} \\ \end{array}
$$

where  $\hat{\Psi}_{\mathbf{k}}$  is an  $N$ -component vector of annihilation operators with crystal momentum  $\mathbf{k}$ , and  $N$  is the number of lattice sites per unit cell. The  $N$ -by- $N$  matrix  $A(\mathbf{k})$  is Hermitian and  $B(\mathbf{k})^t = B(-\mathbf{k})$ . The terms due to  $B(\mathbf{k})$  do not conserve the number of photons. At first glance, the Hamiltonian (74) is similar to the Bogoliubov-de Gennes Hamiltonian of superconducting electronic systems. In fact, the Hamiltonian (74) has particle-hole symmetry as in the fermionic Bogoliubov-de Gennes Hamiltonian, and the spectrum is symmetric with respect to the zero of the energy. However, the transformation needed to diagonalize the Hamiltonian is drastically different between bosons and fermions. The fermionic counterpart of  $H_{\mathbf{k}}$  for the Bogoliubov-de Gennes Hamiltonian can be

diagonalized by a unitary matrix to obtain eigenenergies of the systems which are guaranteed to be all real. On the other hand, in order to preserve the bosonic commutation relations, the bosonic Bogoliubov Hamiltonian  $H_{\mathbf{k}}$  should be diagonalized by Bogoliubov transformations which are not a unitary matrix but a paraunitary matrix  $\hat{U}$  obeying  $\hat{U}^{\dagger}(\sigma_z\otimes \mathbb{I}_N)\hat{U} = \sigma_z\otimes \mathbb{I}_N$ . The associated eigenenergies can be complex. These differences imply that the standard wisdom on topological phases of matter known for fermions may not hold for bosonic Bogoliubov Hamiltonians. Because of the possibility of having complex eigenvalues, we also need to pay attention to the possibility of instability.

Bosonic Bogoliubov Hamiltonians appear not only in photonic systems. In fact, the topological properties of such Hamiltonians were first discussed in the context of magnons in ferromagnetic crystals (Shindou, Matsumoto et al., 2013; Shindou, Ohe et al., 2013; Shindou and Ohe, 2014), where analogs of the Chern insulators in bosonic Bogoliubov Hamiltonians were discussed. It was found that the relevant Berry connection of the nth band of the Bogoliubov Hamiltonian is

$$
\mathcal {A} _ {n} (\mathbf {k}) = i \langle u _ {n, \mathbf {k}} | \sigma_ {z} \nabla_ {\mathbf {k}} | u _ {n, \mathbf {k}} \rangle , \tag {75}
$$

where  $|u_{n,\mathbf{k}}\rangle$  is the Bloch state of the nth band. Note the additional  $\sigma_z$  in the definition of the Berry connection. The Berry curvature is then defined as  $\Omega_n = \nabla_{\mathbf{k}} \times \mathcal{A}_n(\mathbf{k})$ . The Chern number calculated by integrating this Berry curvature over the Brillouin zone is guaranteed to be integer and is related to the number of chiral edge modes.

Bogoliubov excitations are typically gapless at zero energy, but there can be gaps between higher energy bands. In exciton polaritons, Bardyn et al. (2016) and Bleu, Solnyshkov, and Malpuech (2016) analyzed the Bogoliubov modes of exciton-polariton condensates and proposed models which have topological edge states at the gaps with nonzero excitation energy. The topological edge states at higher energy gaps of Bogoliubov excitations were also discussed in ultracold atomic gases (Engelhardt and Brandes, 2015; Furukawa and Ueda, 2015; Y. Li et al., 2015; Di Liberto, Hemmerich, and Morais Smith, 2016). In a lattice of photonic cavities under parametric driving, Peano, Houde, Brendel et al. (2016) proposed a model which has a nonzero gap at zero energy. In order to have a stable system, the gap at zero energy cannot have an edge state, so the sum of the Chern numbers of bands at the negative energy is zero, but gaps between higher energy bands can have topological edge states.

A distinctive feature of the bosonic Bogoliubov Hamiltonian (74) is that the eigenenergies can become complex, hence triggering parametric instabilities (Shi, Kimble, and Cirac, 2017). Peano, Houde, Marquardt, and Clerk (2016) proposed a model where the topological edge states become unstable, even though all the bulk modes are stable. Such an unstable edge mode could be used as a traveling wave parametric amplifier. Instability caused by the topological edge modes was also analyzed in the context of ultracold atomic gases (Barnett, 2013; Galilo, Lee, and Barnett, 2015; Engelhardt et al., 2016). The interplay between the topology and the parametric

instability was also discussed in classical harmonic oscillators under periodic driving (Salerno et al., 2016).

Finally, combined with strong optical nonlinearities (see Sec. VII.B), a  $p$ -wave version of parametric driving underlies the proposal in Bardyn and Imamoglu (2012) to obtain Majorana modes in a one-dimensional system of strongly interacting, fermionized photons.

# VII. TOPOLOGICAL EFFECTS FOR INTERACTING PHOTONS

Most of the discussion of the previous sections concerned linear optical systems whose physics can be accurately described in terms of the standard Maxwell's equations including suitable linear dielectric and magnetic susceptibilities. In this regime, photons behave as independent particles. In this section, we focus our attention on the novel features that originate from the interplay of the topology with nonlinear optical effects.

Basing ourselves on the general introduction to the basic nonlinear optics concepts of Sec. II.B.3, the next two Secs. VII.A and VII.B summarize the main effects of an intensity-dependent refractive index in, respectively, the cases of weak and strong nonlinearity. In the former, a classical mean-field description based on Maxwell's equations with a nonlinear polarization term is accurate, while, in the latter, the physics is dominated by quantum optical effects due to the discreteness of the photon. We also note that Sec. VI.B provides a brief review of how parametric processes generated by a  $\chi^{(2)}$  optical nonlinearity can give rise to a rich emergent topological structure for linear Bogoliubov modes.

# A. Weak nonlinearities

For sufficiently weak values of the optical nonlinearities, one can legitimately perform the mean-field approximation of Eq. (55), in which the photons lose their particle character and collectively behave as a macroscopic wave, experiencing effective material properties that depend on the local amplitude of the light field according to the model of classical nonlinear polarization Eq. (51). While some parametric processes generated by a  $\chi^{(2)}$  optical nonlinearity in the topological photonics context were reviewed in Sec. VI.B, in this section we focus on the case of an intensity-dependent refractive index Eq. (52): As reviewed in the following, theoretical works have anticipated that the modification of the refractive index induced by the nonlinearity may have dramatic observable consequences such as modifying the effective topology experienced by the wave.

The first and most natural question of nonlinear topological physics was to understand how solitons (Segev et al., 1992; Eisenberg et al., 1998; Fleischer et al., 2003) or vortices (Kivshar and Agrawal, 2003) are affected by the underlying geometry and topology of the band. This physics has attracted great interest in many fields such as ultracold atomic gases, where relativistic solitons and vortices in honeycomb geometries have been studied by Haddad and Carr (2011, 2015) and Haddad, Weaver, and Carr (2015).

Focusing on optical systems, intense research has been devoted to solitons in either the bulk or the edges of the

Floquet photonic topological insulators of Rechtsman, Zeuner, Plotnik et al. (2013) that were introduced in Sec. III.A.2. The first work in this direction (Lumer et al., 2013b) highlighted different families of long-lived, self-localized wave packets residing in the bulk of the system. Depending on their size, the wave packets may rotate in opposite directions, either following or opposite to the global Floquet modulation of the lattice. Most interestingly, the current profile of a rotationally symmetric six-site wide wave packet can be understood as an edge state residing on the inner boundary of a self-induced effective hole due to the nonlinearity.

The study of the effect of nonlinearity on topological edge states was pioneered by Ablowitz, Curtis, and Zhu (2013) and Ablowitz, Curtis, and Ma (2014; 2015), where the linear edge states of the Floquet bands of the experiment (Rechtsman, Zeuner, Plotnik et al., 2013) were classified as a function of the Floquet modulation parameters and their nonlinear evolution recast in terms of an effective one-dimensional nonlinear Schrödinger-like equation, possibly including higher-order derivative terms. Based on this equation, unidirectionally propagating edge soliton states have been identified: the topological robustness of linear edge states to backscattering translates into an enhanced robustness of edge solitons against higher-order terms. Following works have then analyzed the topological robustness of edge solitons traveling around sharp corners (Ablowitz and Ma, 2015) and developed a general methodology to understand the tight-binding approximation in the context of nonlinear Floquet systems (Ablowitz and Cole, 2017).

Dynamical modulational instabilities of edge states under the effect of nonlinearity and their eventual breakup into a train of solitons has been explored by several authors. Lumer et al. (2016) showed that nonlinear extended edge states of the Floquet system of Rechtsman, Zeuner, Plotnik et al. (2013) are always unstable independently of the sign of their linear dispersion and the actual strength of the nonlinearity. This modulational instability eventually leads to the breakup of the extended wave into solitonlike localized wave packets. Depending on the strength of the nonlinearity, such solitons can extend over many sites along the edge or localize to a single site. For polariton honeycomb lattices, the modulational instability of edge states and the consequent appearance of long-lived quasisoliton edge states were studied by Kartashov and Skryabin (2016), while, for kagome-shaped polariton lattices, topological edge solitons were studied by Gulevich et al. (2017). This latter work also highlighted the wide tunability of the edge soliton group velocity from positive to negative values as well as the robustness of topological edge solitons upon intersoliton collisions.

The idea of nonlinear effects inducing transitions between states with different symmetries was pioneered by Lumer et al. (2013a) with a theoretical study of nonlinearity-induced transitions between  $\mathcal{PT}$ -broken and  $\mathcal{PT}$ -symmetric states in a non-Hermitian system and, then, in Katan et al. (2016) with a theoretical study of the effect of long-range nonlinearities on topological transport. Along these lines, a novel kind of topological solitons was investigated by Leykam and Chong (2016): nonlinear effects locally induce a topological transition in an otherwise topologically trivial lattice and

solitons naturally arise as the edge states at the topological interface. Possible applications of such nonlinearly induced topological transition to optical isolation were explored in different geometries by X. Zhou et al. (2017). A related study in a nonlinear but conservative one-dimensional SSH model was reported by Hadad, Khanikaev, and Alù (2016).

# B. Strong nonlinearities

When nonlinearities are large, the discrete nature of the photons constituting the field starts being important and one has to resort to a fully quantum description. Correspondingly, the physics of these systems is qualitatively different, as they are expected to support strongly correlated states of light that closely resemble their electronic counterparts, e.g., fractional quantum Hall liquids (Carusotto and Ciuti, 2013).

The simplest example of a quantum nonlinear effect is the so-called photon blockade phenomenon (Imamoglu et al., 1997) that occurs in single-mode nonlinear cavities when the single-photon nonlinearity  $\omega_{nl}$  [i.e., the frequency shift experienced by the mode for a single-photon occupation, as introduced in Eq. (58)] exceeds the damping rate  $\gamma$  of the cavity mode. For an incident beam on resonance with the empty cavity mode, a first photon can freely enter the cavity, but a second one will find the effective resonance shifted by  $\omega_{nl}$  and cannot enter until the first has left. In analogy with the Coulomb blockade of electronics, one can think of the first photon blocking the entrance of the second: hence the term photon blockade.

In the last decade or so, photon blockade has been observed in a variety of cavity configurations using different optically nonlinear elements (Birnbaum et al., 2005; Faraon et al., 2008; Lang et al., 2011; Reinhard et al., 2012). In relation to topological photonics, the most promising platforms to combine photon blockade with synthetic gauge fields and/or nontrivial band topologies are the nonplanar cavities containing coherently dressed atomic gases in a Rydberg-EIT configuration and circuit-QED devices embedding strongly nonlinear superconducting elements, as recently pioneered by Jia et al. (2018a, 2018b) and Roushan et al. (2017b), respectively.

The extension of photon blockade to many-cavity configurations so as to obtain complex strongly correlated many-photon states started attracting the interest of researchers in the mid-2000s with several proposals for how to realize Mott-insulator states of light (Greentree et al., 2006; Hartmann, Brandão, and Plenio, 2006; Angelakis, Santos, and Bose, 2007). Along these lines, the first proposal of a quantum Hall effect for light appeared by Cho, Angelakis, and Bose (2008). While all these pioneering works made the quite strong assumption of a quasiequilibrium photon gas, which is able to equilibrate and/or be adiabatically manipulated before disappearing due to losses, specific studies of the consequences of the intrinsically driven-dissipative nature of photon systems appeared just a few years later (Carusotto et al., 2009; Gerace et al., 2009).

The first theoretical study of the interplay of strong interactions with a synthetic gauge field in a driven-dissipative context appeared by Nunnenkamp, Koch, and Girvin (2011), where strongly correlated states of photons in few-sites lattices were highlighted, together with the signatures of such

states in the transmission properties of a device. Soon after, a proposal to generate fractional quantum Hall states of light as a driven-dissipative steady state of a lossy Bose-Hubbard model with nontrivial hopping phases under a coherent pump was reported by Umucalilar and Carusotto (2012). The selective excitation of the desired many-body state can be obtained via the same multiphoton frequency selection mechanism first introduced by Carusotto et al. (2009) for Tonks-Girardeau gases of light. Signatures of the strongly correlated nature of quantum Hall states are then anticipated to transfer to the quantum statistical properties of the emitted light. While the coherent pumping scheme considered by Carusotto et al. (2009) and further investigated by Hafezi, Lukin, and Taylor (2013) is promising for the generation of few-photon quantum Hall states, its performance does not scale up favorably to larger numbers of photons: the frequency selection mechanism loses efficiency as many-photon peaks get spectrally closer, and the effective matrix element of the many-photon transition to the quantum Hall state may be quickly decreasing.

Soon afterward, the coherent pumping scheme was extended to single cylindrical cavity geometries by Umucalilar and Carusotto (2013). In analogy with related research in rotating atomic gases (Cooper, 2008), one can take advantage of the formal similarity between the magnetic Lorentz force and the Coriolis one to study quantum Hall physics in the rotating fluids of light that are generated by a Laguerre-Gauss shaped coherent drive. Serious difficulties of this scheme were quickly pointed out (Grusdt, Otterbach, and Fleischhauer, 2013): any deviation from the perfect rotational symmetry of the cavity would result in a quick spin down of the rotating photon gas, while the spectral detuning between Landau levels prevents the use of narrow-band nonlinear elements such as Rydberg-EIT atoms.

These difficulties have been solved by the twisted optical resonators used in the experiments of Schine et al. (2016) reviewed in Sec. III.B.3. Replacing the mechanical rotation of the fluid of light with a synthetic magnetic field recovers the degeneracy between states in the lowest Landau level and, at the same time, introduces a sizable detuning between states of opposite angular momentum, which prevents the cloud from spinning down. Crucial experimental steps toward the generation of quantum Hall fluids of light in these systems have been recently reported, including the observation of Rydberg cavity polaritons in running-wave resonators (Ningyuan et al., 2016), the use of optically pumped atomic samples to break time reversal and thus suppressing backscattering processes that would otherwise effectively reverse the synthetic gauge field (Jia et al., 2018b), and the use of the ultrastrong photon-photon interactions of Rydberg EIT to get photon blockade in the Gaussian-shaped fundamental mode of a cavity (Jia et al., 2018a).

In the meantime, further theoretical work has anticipated an exotic phase diagram resulting from the short-distance saturation of the Rydberg-Rydberg interaction (Grusdt and Fleischhauer, 2013). On the other hand, since these experiments are exploring quantum Hall physics on the surface of a cone, direct measurement of the properties of anyonic excitations appears to be possible through the density distribution in the vicinity of the cone tip, which will reflect the central charge of the topological fluid (Can et al., 2016). Additional

theoretical work on the many-body aspects of this challenge was presented by Sommer, Buchler, and Simon (2015) and Dutta and Mueller (2018).

Along related directions, fractional quantum Hall states in Jaynes-Cummings-Hubbard lattices were theoretically explored by Hayward, Martin, and Greentree (2012). The possibility of realizing topological models based on the spin dynamics of Rydberg polaritons confined in a widely spaced microcavity array was explored by Maghrebi, Yao et al. (2015). Here hopping between sites does not occur by photon tunneling between neighboring cavities, but rather by dipolar interactions which exchange the spin state of neighboring dark polaritons.

In parallel to these advances with macroscopic optical cavities embedding atoms, the first experimental studies of magnetic effects in a strongly interacting gas of photons were reported by Roushan et al. (2017b) using a circuit-QED architecture with a closed loop three-site geometry. The synthetic magnetic fields are obtained following the theoretical proposal by Fang, Yu, and Fan (2012b), where the hopping phase is determined by the oscillation phase of the temporal modulation needed to compensate the frequency mismatch of neighboring sites. This technique falls within the class of Floquet techniques discussed in Sec. II.A.5 and was pioneered in the cold-atom context by Aidelsburger et al. (2013) and Miyake et al. (2013).

As illustrated in Fig. 30, a directional circulation of photons is the signature of broken time-reversal symmetry. Whereas noninteracting photons would independently rotate as single photons in a direction fixed by the synthetic magnetic field, the effect of strong interactions is manifested in the opposite circulation direction of photon vacancies. A similar inversion of the rotation direction as a consequence of strong interactions was recently reported also in the cold-atom context by Tai et al. (2017).

Thanks to the relatively long lifetime of photons, the experiment (Roushan et al., 2017b) could be performed by

![](images/f848acacbbb070f9cc9c9364a5fe7d1e350b20eb4ac37d6c20cba3aed271446c.jpg)  
(a)  
(b)

![](images/be7bf36d434bcc0d4886dd17f1087e3ceacee98010b3488763edc690ed087068.jpg)  
Single-photon  
$\Phi_B = -\pi /2$

![](images/180f4c5ba643297345aed8adca6de1203207bb2b3d6765b4f14a0d7698aa7c49.jpg)

![](images/a753bf6eeef5d4abc7973a641a07c0c789a51be11e513a7fd483b826eeb2f9d3.jpg)  
Two-photon  
CW circulation

![](images/88e0590753955e000950ef825c7a8f7b0fea42b640eb17b0f295686eae9f8a53.jpg)  
FIG. 30. Upper center and right panels: Sketches of the circulation dynamics of a single- (center) and two-photon (right) state superimposed on the circuit-QED system under consideration. (a) Upper left: Time evolution of the excitation probability in the three  $Q_{1,2,3}$  qubits for a single-photon state at magnetic flux  $\Phi_B = -\pi /2$ . (b) The same for a two-photon case. From Roushan et al., 2017b.

initializing the system in a suitable one- or two-photon Fock state and then following its dynamics in the absence of any pump during the evolution: such an approach is able to directly probe the coherent quantum dynamics, but it is strongly limited by the decay rate of the full many-photon state that typically scales proportionally to the photon number (Milman, Castin, and Davidovich, 2000). As a further important result of Roushan et al. (2017b), the adiabatic generation of a few-body interacting ground state for arbitrary synthetic magnetic flux  $\Phi_B$  was also reported by slowly ramping up  $\Phi_B$  to the desired final value. Roushan et al. (2017a) used this same platform in the presence of a quasiperiodic potential for photons to observe the Hofstadter butterfly of one-photon states and, then, localization effects in the two-photon sector.

This experimental result is all the more promising as several adiabatic protocols to create strongly correlated macroscopic topological states have been theoretically investigated, based on either the melting of Mott-insulator states (Cho, Angelakis, and Bose, 2008) or by a sequence of flux-insertion and then quasihole refilling processes (Grusdt et al., 2014; Letscher, Grusdt, and Fleischhauer, 2015; Ivanov et al., 2018). An interesting proposal to manipulate quantum states of light by means of a generalized Thouless pumping in strongly nonlinear arrays was suggested by Tangpanitanon et al. (2016). One has however to keep in mind that all these adiabatic schemes typically require that the process must be completed in a time scale shorter than the lifetime of the quantum many-body state of interest, a condition that may become extremely demanding for macroscopic photon fluids.

An alternative approach to dynamically stabilize topological many-body states of light against losses without any active intervention from external observers was started by Kapit, Hafezi, and Simon (2014). In a circuit-QED context, this can be achieved using, e.g., the frequency-selective parametric emission from a shadow lattice: refilling of holes occurs at a fast rate as long as it spectrally coincides with the emission bandwidth, while the injection of extra photons on top of the topological state is suppressed via a generalized blockade phenomenon due to the many-body energy gap. In a related proposal (Hafezi, Adhikari, and Taylor, 2015), parametric coupling to a thermal bath was proposed to generate a tunable chemical potential for effectively thermalized light. A conceptually similar idea based on population-inverted two-level systems as frequency-dependent light emitters was investigated by Lebreuilly, Wouters, and Carusotto (2016) and Biella et al. (2017) in the context of Mott-insulator states of light. The significant advantages of replacing the Lorentzian emission spectrum with a more sophisticated square spectrum were pointed out by Lebreuilly et al. (2017). The study of frequency-dependent incoherent pumping schemes applied to the generation of quantum Hall states in the twisted optical resonators of Schine et al. (2016) was discussed by Umucalar and Carusotto (2017). An experimental realization of a dissipatively stabilized Mott insulator of photons was very recently reported by Ma et al. (2019).

In the long run, the application of photonic systems as useful platforms for topological quantum computation crucially requires strongly correlated topological states that support excitations with non-Abelian braiding statistics

(Nayak et al., 2008). A promising candidate for this purpose is the so-called Pfaffian states. Originally predicted in the context of the quantum Hall effect of electrons (Moore and Read, 1991), they can be obtained as the ground state in the presence of suitably engineered three-body interactions. A proposal to put this strategy into practice in a circuit-QED context was presented by Hafezi, Adhikari, and Taylor (2014).

Before concluding, it is worth mentioning a completely different approach to the quantum dynamics of systems of few interacting particles (Kramer and Khomeriki, 2011; Longhi, 2011): in the simplest formulation, the idea is to map the  $x_{1,2}$  spatial coordinates of two quantum particles onto the  $x$ ,  $y$  spatial coordinates of a single particle moving in two dimensions. The two-body interactions are then modeled by letting the  $x_{1} = x_{2}$  line of sites have slightly different linear optical properties. As the dynamics remains at a fully single-particle level, it can be simulated in any of the linear optical devices discussed in the first sections of this review.

Along these lines, physically two-dimensional arrays of waveguides were used by Mukherjee et al. (2016) to show evidence of tunneling processes for two-particle bound states in regimes where single-particle tunneling is instead strongly suppressed. The experiment (Schreiber et al., 2012) demonstrated encoding of the spatial coordinates of a two-dimensional quantum walk into the arrival time of a single optical pulse, with a potential generalization to higher-dimensional configurations.

Recently, the application of this mapping to study the interplay of interactions and topology in the two-particle dynamics of a one-dimensional SSH model was simultaneously proposed in the theoretical works by Di Liberto et al. (2016) and Gorlach and Poddubny (2017). An extension of this work exploiting driven-dissipative effects in resonator arrays was proposed by Gorlach and Di Liberto (2018). While these schemes are naturally transferred to the fermionic sector of the two-particle dynamics by means of the suitably antisymmetric initialization, a proposal to study supersymmetry (SUSY) effects in a light-matter context appeared by Tomka, Pletyukhov, and Gritsev (2015).

# VIII. CONCLUSION AND PERSPECTIVES

In the previous sections we have seen how topological photonics has grown from its first proposal (Haldane and Raghu, 2008; Raghu and Haldane, 2008) into a wide and mature field of research with a number of active exciting directions. In this final section of this review, we aim at summarizing those future developments that are promising for the next future.

# A. Optical isolation and robust transport

Topological photonics may have short-term and midterm technological impact. The most straightforward applications involve the use of topologically protected unidirectional edge states as robust optical delay lines or optically isolating elements as originally discussed by Hafezi et al. (2011). While firm experimental evidence of robust unidirectional propagation is currently available in a number of systems, practical application of these ideas into actual devices is still a subject of active investigation.

In particular, the stringent conditions that an optical isolator device must fulfill to be of practical utility were discussed by Jalas et al. (2013). Different strategies to match the requirements are presently being actively explored using either magnetic elements (Bahari et al., 2017; Solnyshkov, Bleu, and Malpuech, 2018), optical nonlinearities (Khanikaev and Alù, 2015; Shi, Yu, and Fan, 2015), or externally modulated elements (Yu and Fan, 2009; Hua et al., 2016; Fang et al., 2017).

Another exciting direction in view of applications in quantum information processing is to extend these results from classical light fields to quantum optical ones and link with on-going developments in chiral quantum optics (Lodahl et al., 2017). The first step in this direction is to show that the dynamics of externally generated entangled photon pairs inherits the topological protection of single-photon states, as theoretically studied by Mittal, Orre, and Hafezi (2016) and Rechtsman et al. (2016). The emission and robust propagation of single-photon states into chiral edge states was experimentally demonstrated by Barik et al. (2018). A proposal to generate quantum states of light by coupling an array of two-level emitters to a chiral edge state was reported by Ringel, Pletyukhov, and Gritsev (2014): interesting correlations between photons originate when an externally generated few-photon wave packet scatters off the strongly nonlinear emitters.

# B. Quantum emitters and topological laser

One of the most active directions of development to date is the study of the interplay of topology with light emitters and with optical gain, which is expected to offer novel features to be exploited in light sources, amplifiers, and laser devices. Strong motivations supported this study in view of optoelectronic and photonics applications, to improve the performance of topological devices compared to their trivial counterparts.

A detailed study of parametric amplification on the chiral edge states of a two-dimensional Harper-Hofstadter model in the presence of parametric downconversion or spontaneous four-wave mixing emission processes was reported by Peano, Houde, Marquardt, and Clerk (2016). With a suitably chosen pump frequency, amplification can be restricted to the edge states, while bulk modes remain quickly damped as in the passive system. The unidirectional nature of the edge state guarantees that amplification is not only quantum noise limited as in standard parametric amplifiers, but also nonreciprocal and almost perfectly insensitive to disorder. Interesting consequences of the topology on the zero-point quantum fluctuations and on the emission of entangled photon pairs are also pointed out.

The robustness of the generated entangled photon pairs against disorder was specifically studied by Mittal and Hafezi (2017). In particular, it was shown how the generation of entangled photons using spontaneous four-wave mixing into topological states can outperform their topologically trivial counterparts.

# 1. Topological lasers: Theory

Strong activity is presently being devoted to the theoretical and experimental study of laser oscillation in topological systems, the so-called topological lasers. For one-dimensional systems, theoretical explorations of laser operation in

topological states have appeared by Pilozzi and Conti (2016), which focused on a 1D Aubry-Andre-Harper bichromatic photonic crystal, and by Malzard and Schomerus (2018b), which studied a 1D SSH chain of resonators, showing that the topological mode selection can persist even in the presence of nonlinearities.

In two dimensions, topological lasing has been shown to lead to a highly efficient laser operation that remains monomode even well above the threshold and is robust against disorder (Harari et al., 2018). Simulations of the nonlinear wave equation with on-site saturable gain terms of the form

$$
\frac {i}{2} \frac {P _ {j}}{1 + \left| \alpha_ {j} \right| ^ {2} / n _ {\mathrm {s a t}}} \alpha_ {j} \tag {76}
$$

included into the lattice model of Eq. (43) without coherent pumping term  $(F_{j} = 0)$  were performed for both trivial and topological lattice models with a pump profile  $P_{j}$  concentrated on the edge. Gain saturation at high power is modeled by the saturation density  $n_{\mathrm{sat}}$ . In the topologically trivial case, laser operation is not able to exhaust all available gain, because many other modes can easily go above threshold for increasing power, leading to a complex multimode operation. This problem is particularly serious in the presence of disorder, which further suppresses the mode competition effect by spatially localizing modes. In topological lattices, all of these problems turn out to be no longer relevant: the single lasing mode is extended around the whole system perimeter, maintaining a unidirectional flow and a spatially very uniform intensity profile even in the presence of disorder and for high pumping levels well above the threshold. In laser terms, this means a robust monomode operation with a high slope efficiency.

Further theoretical work explicitly including the carrier dynamics in the amplifying solid-state material has pointed out the possibility that the topological laser operation is made dynamically unstable by the interplay of nonlinear frequency shifts and a slow population dynamics (Longhi, Kominis, and Kovanis, 2018). General consequences of the chirality of the lasing mode of topological lasers were investigated by Seclí, 2017, in particular, the appearance of slow relaxation dynamics and the need to distinguish convective and absolute instabilities when studying the laser threshold in different geometries.

# 2. Topological lasers: Experiments

From the experimental point of view, the study of the interplay of lasing with geometrical and topological features was initiated by Sala et al. (2015). In this experiment, the linewidth narrowing effect associated with laser operation was exploited to spectrally resolve the effect of the spin-orbit coupling terms in a hexagonal chain of pillar microcavities. The first examples of a lasing operation in a topological nontrivial system were reported in one-dimensional chains of pillar microcavities (St-Jean et al., 2017), ring resonators (Parto et al., 2018; Zhao et al., 2018), or photonics crystal nanocavity (Ota et al., 2018). In all cases, for suitable pump geometries, a single-mode laser emission occurred into the edge states of the chain.

Recently, lasing in the topological edge states of a time-reversal-breaking two-dimensional photonic crystal embedding magnetic YIG elements was reported by Bahari et al.

(2017). This work made use of a photonic crystal structure where gain is provided by quantum well emitters and time-reversal symmetry is broken by bonding the photonic crystal to a magnetic YIG material. In spite of the small width of the magneto-optically induced band gap, and the comparatively large linewidth of the bulk modes, lasing of modes on the edge was observed.

Soon after, another experiment (Bandres et al., 2018) reported topological laser operation in a topological ring resonator array (as discussed in Sec. III.B.1) embedding, in addition, quantum well emitters that provide optical gain. This setup does not require magnetic elements. By selectively pumping the edge resonators, a highly efficient single-mode emission into the topologically protected edge state was obtained even for gain values high above threshold. The performances of the novel device and the robustness against disorder were benchmarked with an extensive comparison to a topologically trivial laser device. A technique to break the spinlike symmetry between the clockwise and counterclockwise modes of the rings by adding S-bend elements into the resonators was also demonstrated, further reinforcing the unidirectional properties of the emission.

A third experiment reported lasing in chiral edge modes using a hexagonal lattice of microcavity polariton resonators (Klembt et al., 2018). The scheme relies on the sensitivity of exciton polaritons to an external magnetic field to break time-reversal symmetry in the configuration described in Sec. III.A.5.

# C. Measurement of bulk topological and geometrical properties

Topological photonics are also opening new perspectives in the study of topological effects of wide interest for quantum condensed-matter physics. As we have reviewed, a variety of new, possibly high-dimensional lattice configurations are becoming available thanks to the advances in photonic fabrication and manipulation. Furthermore, thanks to the high flexibility of the optical excitation and diagnostic schemes, an intense study is being devoted to the observable consequences of the geometrical and topological concepts: while the topologically protected chiral edge states have been the smoking gun of a nontrivial topology starting from the pioneering work of Wang et al. (2009), the geometrical quantities characterizing the bulk bands are nowadays the subject of active study.

From early studies of transport in electronic systems (Xiao, Chang, and Niu, 2010), it is well known that the Berry curvature enters the semiclassical equations of motion for electrons as a sort of momentum-space magnetic field. The corresponding Lorentz-like force in reciprocal space provides an anomalous velocity term which is responsible, e.g., for the anomalous and integer (Thouless et al., 1982) quantum Hall effects. In the topological photonics context, this idea underlies the experimental reconstruction by Wimmer et al. (2017) of the  $k$ -space distribution of the bulk Berry curvature from the anomalous velocity of a wave packet performing Bloch oscillations under an external force as theoretically proposed by Dudarev et al. (2004), Price and Cooper (2012), and Cominotti and Carusotto (2013).

Application of the anomalous velocity idea to the coherently pumped systems discussed in Sec. II.B.2 was theoretically proposed by Ozawa and Carusotto (2014). In addition to putting forward driven-dissipative versions of the anomalous Hall effects, specific pumping schemes able to equally distribute photons among the different momentum states were identified. In analogy to the classical theory of the integer quantum Hall effect in electronic systems (Thouless et al., 1982; Xiao, Chang, and Niu, 2010) and to recent experiments with ultracold atoms (Aidelsburger et al., 2015), the spatial displacement of the center of mass of the light intensity distribution then provides information on the Chern number of the band. Later works (Price et al., 2015, 2016; Ozawa et al., 2016) have generalized this idea to the second Chern number of four-dimensional lattice models and to the measurement of other geometrical quantities such as the Fubini-Study metric tensor (Ozawa, 2018). On a similar basis, the concept of mean chiral displacement was introduced to measure the winding of a chiral Hamiltonian from real-space measurements (Mondragon-Shem et al., 2014; Cardano et al., 2016; Maffei et al., 2018; Meier et al., 2018). One of the most attractive aspects of this proposal is the possibility of measuring topological invariants in the presence of disorder, which breaks translational symmetry. An alternative scheme to extract the Chern number from the steady-state field amplitude of a small photonic lattice with twisted boundary conditions was discussed by Bardyn, Huber, and Zilberberg (2014). It was also suggested to calculate the full quantum geometric tensor, including the Berry curvature and the Fubini-Study metric, from direct measurements of the photon wave function in radiative photonic systems (Bleu, Solnyshkov, and Malpuech, 2018). Furthermore, dissipation has been used in the context of non-Hermitian systems to probe topological invariants in 1D photonic systems (Rudner and Levitov, 2009; Zeuner et al., 2015), as discussed in Sec. VI.A.

Building on top of the anomalous velocity concept, recent works (Bliokh and Bliokh, 2005; Price, Ozawa, and Carusotto, 2014) undertook the challenge of upgrading the semiclassical equations of motion to a full quantum mechanical theory of quantum particles in the presence of a nonvanishing momentum-space Berry curvature. As an example of application of this theory, the eigenstates of a topologically nontrivial lattice model subject to an additional external harmonic potential can be physically understood as momentum-space Landau levels on the torus-shaped first Brillouin zone, with a degeneracy set by the Chern number of the band (Price, Ozawa, and Carusotto, 2014). A proposal to investigate this physics in a driven-dissipative array of optical cavities with site-dependent resonance frequencies appeared by Berceanu et al. (2016).

Further on-going work in this direction is investigating how the momentum-space magnetic field may lead to momentum-space analogs of the quantum Hall effects (Claassen et al., 2015; Ozawa, Price, and Carusotto, 2015, 2016). In these last works, the minima of the  $k$ -space dispersion play the role of lattice sites, the harmonic trapping provides the momentum-space analog of the kinetic energy, and the Berry curvature of the band plays the role of the magnetic field. Periodic boundary conditions are automatically inherited from the topology of the first Brillouin zone and the phase twist

can be adjusted via the position of the harmonic trap minimum within the unit cell.

# D. Topological quantum computing

A most exciting long term perspective is to use topological photonics devices as a platform for novel quantum information storage and processing tasks that exploit topological effects to protect their operation from external disturbances. A crucial requirement for such topological quantum computing with light appears to be the availability of strongly nonlinear elements to generate and manipulate strongly correlated states of light. The key experimental issues that researchers are facing along this route have been discussed in Sec. VII, together with the promising results that were reported in the last few years. Here we highlight a possible strategy along which this research may develop in the future.

In the presence of suitably tailored optical nonlinearities, the fluid of light can form quantum states, e.g., Pfaffian ones (Hafezi, Adhikari, and Taylor, 2014), that are anticipated to display a manifold of topologically degenerate ground states protected by a finite energy gap and elementary excitations with non-Abelian anyonic statistics. In systems with such properties (Nayak et al., 2008), quantum information can be encoded in the ground state manifold of states and the unitary transforms corresponding to quantum logical operations can be performed by braiding quasiholes around each other. With respect to standard quantum information protocols, quantum computing based on these topological states of matter has the advantage that the states within the topologically degenerate manifold cannot be coupled nor mixed with each other by local disturbances, at least as long as their amplitude is not able to cross the energy gap.

To date, several condensed-matter systems such as quantum Hall states of two-dimensional electrons under strong magnetic fields (Tong, 2016) or Majorana fermions in suitable superconductor-based solid-state nanostructures (Elliott and Franz, 2015) are being seriously considered for this purpose, but to the best of our knowledge no experimental evidence is yet available of anyonic braiding statistics. First proposals taking advantage of the peculiarities of the optical systems to observe anyonic statistics have been recently brought forth (Umucalilar and Carusotto, 2013; Dutta and Mueller, 2018), but a key question that remains open is the degree of robustness of the topologically encoded quantum information against the typical dissipative processes of optical systems. On the other hand, using an all-optical platform will be extremely favorable in view of integration of the quantum processing unit into an optical communication network.

# ACKNOWLEDGMENTS

T. O. was supported by the EUF-FET Proactive grant AQuS (Project No. 640800), the ERC Starting Grant TopoCold, and the Interdisciplinary Theoretical and Mathematical Sciences Program (iTHEMS) at RIKEN. H. M. P. received funding from the Royal Society and from the European Unions Horizon 2020 research and innovation programme under the Marie Sklodowska-Curie grant agreement No. 656093: "SynOptic." A. A. was supported by the ERC grant Honeypol, the EUF-FET

Proactive grant AQUS (Project No. 640800), the French National Research Agency (ANR) project Quantum Fluids of Light (ANR-16-CE30-0021) and the program Labex CEMPI (ANR-11-LABX-0007), the CPER Photonics for Society P4S, and the Métropole Européenne de Lille. N.G. was supported by the FRS-FNRS (Belgium) and by the ERC Starting Grant TopoCold. M.H. acknowledges Sunil Mittal and was supported by AFOSR MURI Grant No. FA95501610323, the Sloan Foundation, and the Physics Frontier Center at the Joint Quantum Institute. L.L. was supported by the National Key R&D Program of China under Grants No. 2017YFA0303800 and No. 2016YFA0302400 and the NSFC under Project No. 11721404. M.C.R. acknowledges the National Science Foundation under Awards No. ECCS-1509546 and No. DMS-1620422, the David and Lucile Packard Foundation, the Charles E. Kaufman Foundation, a supporting organization of the Pittsburgh Foundation, the Office of Naval Research under the YIP program, Grant No. N00014-18-1-2595, and the Alfred P. Sloan Foundation under fellowship No. FG-2016-6418. D.S. and J.S. were supported by the University of Chicago Materials Research Science and Engineering Center, which is funded by the National Science Foundation under Award No. DMR-1420709. This work was supported by ARO Grant No. W911NF-15-1-0397. D.S. acknowledges support from the David and Lucile Packard Foundation. This work was supported by DOE Grant No. DE-SC0010267 and AFOSR Grant No. FA9550-16-1-0323. O.Z. was supported by the Swiss National Science Foundation (SNSF). I.C. acknowledges funding from Provincia Autonoma di Trento, partly through the SiQuro project ("On Silicon Chip Quantum Optics for Quantum Computing and Secure Communications"), from ERC through the QGBE grant, and from the EU-FET Proactive grant AQuS, Project No. 640800 and EU-FET-Open grant MIR-BOSE Project No. 737017.

# REFERENCES

Aaboud, M., et al. (ATLAS Collaboration), 2017, "Evidence for light-by-light scattering in heavy-ion collisions with the ATLAS detector at the LHC," Nat. Phys. 13, 852-858.  
Ablowitz, M. J., and J. T. Cole, 2017, "Tight-binding methods for general longitudinally driven photonic lattices: Edge states and solitons," Phys. Rev. A 96, 043868.  
Ablowitz, M. J., C. W. Curtis, and Y.-P. Ma, 2014, "Linear and nonlinear traveling edge waves in optical honeycomb lattices," Phys. Rev. A 90, 023813.  
Ablowitz, M.J., C.W. Curtis, and Y.-P. Ma, 2015, "Adiabatic dynamics of edge waves in photonic graphene," 2D Mater. 2, 024003.  
Ablowitz, M.J., C.W. Curtis, and Y. Zhu, 2013, “Localized nonlinear edge states in honeycomb lattices,” Phys. Rev. A 88, 013850.  
Ablowitz, M.J., and Y.-P. Ma, 2015, "Strong transmission and reflection of edge modes in bounded photonic graphene," Opt. Lett. 40, 4635-4638.  
Adams, E. N., and E. I. Blount, 1959, "Energy bands in the presence of an external force field II: Anomalous velocities," J. Phys. Chem. Solids 10, 286-303.

Aidsburger, M., M. Atala, M. Lohse, J. T. Barreiro, B. Paredes, and I. Bloch, 2013, "Realization of the Hofstadter Hamiltonian with ultracold atoms in optical lattices," Phys. Rev. Lett. 111, 185301.  
Aidsburger, M., M. Lohse, C. Schweizer, M. Atala, J. T. Barreiro, S. Nascimbène, N. R. Cooper, I. Bloch, and N. Goldman, 2015, "Measuring the Chern number of Hofstadter bands with ultracold bosonic atoms," Nat. Phys. 11, 162-166.  
Albert, V.V., L.I. Glazman, and L. Jiang, 2015, "Topological properties of linear circuit lattices," Phys. Rev. Lett. 114, 173902.  
Alexandradinata, A., C. Fang, M. J. Gilbert, and B. A. Bernevig, 2014, "Spin-orbit-free topological insulators without time-reversal symmetry," Phys. Rev. Lett. 113, 116403.  
Altug, H., D. Englund, and J. Vuckovic, 2006, "Ultrafast photonic crystal nanocavity laser," Nat. Phys. 2, 484-488.  
An, F. A., E. J. Meier, and B. Gadway, 2017, "Direct observation of chiral currents and magnetic reflection in atomic flux lattices," Sci. Adv. 3, e1602685.  
Anderson, B. M., R. Ma, C. Owens, D. I. Schuster, and J. Simon, 2016, "Engineering topological many-body materials in microwave cavity arrays," Phys. Rev. X 6, 041043.  
Anderson, P. D., and G. Subramania, 2017, "Unidirectional edge states in topological honeycomb-lattice membrane photonic crystals," Opt. Express 25, 23293-23301.  
Angelakis, D. G., P. Das, and C. Noh, 2014, "Probing the topological properties of the Jackiw-Rebbi model with light," Sci. Rep. 4, 6110.  
Angelakis, D. G., M. F. Santos, and S. Bose, 2007, "Photon-blockade-induced Mott transitions and xy spin models in coupled cavity arrays," Phys. Rev. A 76, 031805.  
Anisimovas, E., M. Racūnas, C. Sträter, A. Eckardt, I. B. Spielman, and G. Juzeliūnas, 2016, "Semisynthetic zigzag optical lattice for ultracold bosons," Phys. Rev. A 94, 063632.  
Ao, X., Z. Lin, and C. T. Chan, 2009, "One-way edge mode in a magneto-optical honeycomb photonic crystal," Phys. Rev. B 80, 033105.  
Armitage, N. P., E. J. Mele, and A. Vishwanath, 2018, "Weyl and Dirac semimetals in three dimensional solids," Rev. Mod. Phys. 90, 015001.  
Arovas, D., J.R. Schrieffer, and F. Wilczek, 1984, "Fractional statistics and the quantum Hall effect," Phys. Rev. Lett. 53, 722-723.  
Arrayas, M., D. Bouwmeester, and J. L. Trueba, 2017, "Knots in electromagnetism," Phys. Rep. 667, 1-61.  
Asatryan, A. A., L. C. Botten, K. Fang, S. Fan, and R. C. McPhedran, 2013, "Local density of states of chiral Hall edge states in gyrotropic photonic clusters," Phys. Rev. B 88, 035127.  
Asatryan, A. A., L. C. Botten, K. Fang, S. Fan, and R. C. McPhedran, 2014, "Two-dimensional Green's tensor for gyrotropic clusters composed of circular cylinders," J. Opt. Soc. Am. A 31, 2294-2303.  
Asbóth, J. K., 2012, "Symmetries, topological phases, and bound states in the one-dimensional quantum walk," Phys. Rev. B 86, 195414.  
Ashcroft, N.W., and N.D. Mermin, 1976, Solid State Physics (Brooks Cole, USA).  
Aspelmeyer, M., T. J. Kippenberg, and F. Marquardt, 2014, "Cavity optomechanics," Rev. Mod. Phys. 86, 1391.  
Avron, J.E., R. Seiler, and B. Simon, 1983, “Homotopy and quantization in condensed matter physics,” Phys. Rev. Lett. 51, 51-53.  
Azel, M. Y., 1964, "Energy spectrum of a conduction electron in a magnetic field," Sov. Phys. JETP 19, 634-645 [http://www.jetp.ac.ru/cgi-bin/e/index/e/19/3/p634?a=list].

Baboux, F., E. Levy, A. Lemaitre, C. Gomez, E. Galopin, L. Le Gratiet, I. Sagnes, A. Amo, J. Bloch, and E. Akkermans, 2017, "Measuring topological invariants from generalized edge states in polaritonic quasicrystals," Phys. Rev. B 95, 161114.  
Bahari, B., A. Ndao, F. Vallini, A. El Amili, Y. Fainman, and B. Kanté, 2017, "Nonreciprocal lasing in topological cavities of arbitrary geometries," Science 358, 636-640.  
Bahari, B., R. Tellez-Limon, and B. Kanté, 2016, "Topological terahertz circuits using semiconductors," Appl. Phys. Lett. 109, 143501.  
Balents, L., and M. P. A. Fisher, 1996, "Chiral surface states in the bulk quantum Hall effect," Phys. Rev. Lett. 76, 2782-2785.  
Bandres, M. A., M. C. Rechtsman, and M. Segev, 2016, "Topological photonic quasicrystals: Fractal topological spectrum and protected transport," Phys. Rev. X 6, 011016.  
Bandres, M. A., S. Wittek, G. Harari, M. Parto, J. Ren, M. Segev, D. N. Christodoulides, and M. Khajavikhan, 2018, "Topological insulator laser: Experiments," Science 359, eaar4005.  
Bansil, A., H. Lin, and T. Das, 2016, “Colloquium: Topological band theory,” Rev. Mod. Phys. 88, 021004.  
Barbarino, S., L. Taddia, D. Rossini, L. Mazza, and R. Fazio, 2016, "Synthetic gauge fields in synthetic dimensions: Interactions and chiral edge modes," New J. Phys. 18, 035010.  
Bardyn, C.-E., M. A. Baranov, C. V. Kraus, E. Rico, A. Mamolu, P. Zoller, and S. Diehl, 2013, "Topology by dissipation," New J. Phys. 15, 085001.  
Bardyn, C.-E., M. A. Baranov, E. Rico, A. Imamoglu, P. Zoller, and S. Diehl, 2012, "Majorana modes in driven-dissipative atomic superfluids with a zero Chern number," Phys. Rev. Lett. 109, 130402.  
Bardyn, C.-E., and A. Imamoglu, 2012, "Majorana-like modes of light in a one-dimensional array of nonlinear cavities," Phys. Rev. Lett. 109, 253606.  
Bardyn, C.-E., S. D. Huber, and O. Zilberberg, 2014, "Measuring topological invariants in small photonic lattices," New J. Phys. 16, 123013.  
Bardyn, C.-E., T. Karzig, G. Refael, and T.C.H. Liew, 2015, "Topological polaritons and excitons in garden-variety systems," Phys. Rev. B 91, 161413.  
Bardyn, C.-E., T. Karzig, G. Refael, and T. C. H. Liew, 2016, "Chiral Bogoliubov excitations in nonlinear bosonic systems," Phys. Rev. B 93, 020502.  
Barik, S., A. Karasahin, C. Flower, T. Cai, H. Miyake, W. DeGottardi, M. Hafezi, and E. Waks, 2018, "A topological quantum optics interface," Science 359, 666-668.  
Barik, S., H. Miyake, W. DeGottardi, E. Waks, and M. Hafezi, 2016, "Two-dimensionally confined topological edge states in photonic crystals," New J. Phys. 18, 113013.  
Barkhofen, S., T. Nitsche, F. Elster, L. Lorz, A. Gabris, I. Jex, and C. Silberhorn, 2017, "Measuring topological invariants in disordered discrete-time quantum walks," Phys. Rev. A 96, 033846.  
Barnett, R., 2013, "Edge-state instabilities of bosons in a topological band," Phys. Rev. A 88, 063631.  
Bayindir, M., B. Temelkuran, and E. Ozbay, 2000, "Tight-binding description of the coupled defect modes in three-dimensional photonic crystals," Phys. Rev. Lett. 84, 2140.  
Bellec, M., C. Michel, H. Zhang, S. Tzortzakis, and P. Delplace, 2017, "Non-diffracting states in one-dimensional Floquet photonic topological insulators," Europhys. Lett. 119, 14003.  
Bellec, M., U. Kuhl, G. Montambaux, and F. Mortessagne, 2013a, "Tight-binding couplings in microwave artificial graphene," Phys. Rev. B 88, 115437.

Bellec, M., U. Kuhl, G. Montambaux, and F. Mortessagne, 2013b, "Topological Transition of Dirac Points in a Microwave Experiment," Phys. Rev. Lett. 110, 033902.  
Bellec, M., U. Kuhl, G. Montambaux, and F. Mortessagne, 2014, "Manipulation of edge states in microwave artificial graphene," New J. Phys. 16, 113023.  
Bender, C.M., and S. Boettcher, 1998, "Real spectra in non-Hermitian Hamiltonians having P T symmetry," Phys. Rev. Lett. 80, 5243.  
Berceanu, A.C., H.M. Price, T. Ozawa, and I. Carusotto, 2016, "Momentum-space Landau levels in driven-dissipative cavity arrays," Phys. Rev. A 93, 013827.  
Bermudez, A., T. Schaetz, and D. Porras, 2011, "Synthetic gauge fields for vibrational excitations of trapped ions," Phys. Rev. Lett. 107, 150501.  
Bernevig, B. A., and T. L. Hughes, 2013, Topological insulators and topological superconductors (Princeton University Press, Princeton, NJ).  
Bernevig, B. A., T. L. Hughes, S. Raghu, and D. P. Arovas, 2007, "Theory of the three-dimensional quantum Hall effect in graphite," Phys. Rev. Lett. 99, 146804.  
Bernevig, B. A., T. L. Hughes, and S.-C. Zhang, 2006, "Quantum spin Hall effect and topological phase transition in HgTe quantum wells," Science 314, 1757-1761.  
Bernevig, B. A., and S.-C. Zhang, 2006, "Quantum spin Hall effect," Phys. Rev. Lett. 96, 106802.  
Berry, M. V., 1984, “Quantal phase factors accompanying adiabatic changes,” Proc. R. Soc. A 392, 45-57.  
Bi, R., and Z. Wang, 2015, "Unidirectional transport in electronic and photonic Weyl materials by Dirac mass engineering," Phys. Rev. B 92, 241109.  
Bi, R., Z. Yan, L. Lu, and Z. Wang, 2017a, "Nodal-knot semimetals," Phys. Rev. B 96, 201305.  
Bi, R., Z. Yan, L. Lu, and Z. Wang, 2017b, "Topological defects in Floquet systems: Anomalous chiral modes and topological invariant," Phys. Rev. B 95, 161115.  
Biella, A., F. Storme, J. Lebreuilly, D. Rossini, R. Fazio, I. Carusotto, and C. Ciuti, 2017, "Phase diagram of incoherently driven strongly correlated photonic lattices," Phys. Rev. A 96, 023839.  
Bienias, P., S. Choi, O. Firstenberg, M. F. Maghrebi, M. Gullans, M. D. Lukin, A. V. Gorshkov, and H. P. Buchler, 2014, "Scattering resonances and bound states for strongly interacting rydberg polaritons," Phys. Rev. A 90, 053804.  
Bilitewski, T., and N. R. Cooper, 2016, "Synthetic dimensions in the strong-coupling limit: Supersolids and pair superfluids," Phys. Rev. A 94, 023630.  
Birnbaum, K. M., A. Boca, R. Miller, A. D. Boozer, T. E. Northup, and H. J. Kimble, 2005, "Photon blockade in an optical cavity with one trapped atom," Nature (London) 436, 87-90.  
Biswas, R. R., and D. T. Son, 2016, "Fractional charge and inter-Landau-level states at points of singular curvature," Proc. Natl. Acad. Sci. U.S.A. 113, 8636-8641.  
Bittner, S., B. Dietz, M. Miski-Oglu, P. Oria Iriarte, A. Richter, and F. Schäfer, 2010, "Observation of a Dirac point in microwave experiments with a photonic crystal modeling graphene," Phys. Rev. B 82, 014301.  
Bittner, S., B. Dietz, M. Miski-Oglu, and A. Richter, 2012, "Extremal transmission through a microwave photonic crystal and the observation of edge states in a rectangular Dirac billiard," Phys. Rev. B 85, 064301.  
Bleckmann, F., Z. Cherpakova, S. Linden, and A. Alberti, 2017, "Spectral imaging of topological edge states in plasmonic waveguide arrays," Phys. Rev. B 96, 045417.

Bleu, O., G. Malpuech, and D.D. Solnyshkov, 2018, "Robust quantum valley Hall effect for vortices in an interacting bosonic quantum fluid," Nat. Commun. 9, 3991.  
Bleu, O., D. D. Solnyshkov, and G. Malpuech, 2016, "Interacting quantum fluid in a polariton Chern insulator," Phys. Rev. B 93, 085438.  
Bleu, O., D. D. Solnyshkov, and G. Malpuech, 2017a, "Photonic versus electronic quantum anomalous Hall effect," Phys. Rev. B 95, 115415.  
Bleu, O., D. D. Solnyshkov, and G. Malpuech, 2017b, "Quantum valley Hall effect and perfect valley filter based on photonic analogs of transitional metal dichalcogenides," Phys. Rev. B 95, 235431.  
Bleu, O., D. D. Solnyshkov, and G. Malpuech, 2018, "Measuring the quantum geometric tensor in two-dimensional photonic and exciton-polariton systems," Phys. Rev. B 97, 195422.  
Bliokh, K. Y., F. J. Rodríguez-Fortuno, F. Nori, and A. V. Zayats, 2015, "Spin-orbit interactions of light," Nat. Photonics 9, 796-808.  
Bliokh, K. Y., A. Y. Bekshaev, and F. Nori, 2014, "Extraordinary momentum and spin in evanescent waves," Nat. Commun. 5, 3300.  
Bliokh, K. Y., and F. Nori, 2012, "Transverse spin of a surface polariton," Phys. Rev. A 85, 061801.  
Bliokh, K. Y., D. Smirnova, and F. Nori, 2015, "Quantum spin Hall effect of light," Science 348, 1448-1451.  
Bliokh, K. Y., and Y. P. Bliokh, 2005, "Spin gauge fields: From berry phase to topological spin transport and hall effects," Ann. Phys. (Amsterdam) 319, 13-47.  
Boada, O., A. Celi, J. I. Latorre, and M. Lewenstein, 2012, "Quantum simulation of an extra dimension," Phys. Rev. Lett. 108, 133001.  
Boada, O., A. Celi, J. Rodríguez-Laguna, J. I. Latorre, and M. Lewenstein, 2015, "Quantum simulation of non-trivial topology," New J. Phys. 17, 045007.  
Bourassa, J., F. Beaudoin, J.M. Gambetta, and A. Blais, 2012, "Josephson-junction-embedded transmission-line resonators: From Kerr medium to in-line transmon," Phys. Rev. A 86, 013814.  
Boyd, R. W., 2008, Nonlinear Optics (Academic Press, New York).  
Bravo-Abad, J., L. Lu, L. Fu, H. Buljan, and M. Soljacic, 2015, "Weyl points in photonic-crystal superlattices," 2D Mater. 2, 034013.  
Brendel, C., V. Peano, O. Painter, and F. Marquardt, 2018, "Snowflake Topological Insulator for Sound Waves," Phys. Rev. B 97, 020102.  
Broome, M. A., A. Fedrizzi, B. P. Lanyon, I. Kassal, A. Aspuru-Guzik, and A. G. White, 2010, "Discrete single-photon quantum walks with tunable decoherence," Phys. Rev. Lett. 104, 153602.  
Brouwer, P. W., 1998, "Scattering approach to parametric pumping," Phys. Rev. B 58, R10135-R10138.  
Budich, J. C., and S. Diehl, 2015, "Topology of density matrices," Phys. Rev. B 91, 165140.  
Budich, J. C., P. Zoller, and S. Diehl, 2015, "Dissipative preparation of Chern insulators," Phys. Rev. A 91, 042117.  
Bukov, M., L. D'Alessio, and A. Polkovnikov, 2015, "Universal high-frequency behavior of periodically driven systems: from dynamical stabilization to Floquet engineering," Adv. Phys. 64, 139-226.  
Burkov, A. A., M. D. Hook, and L. Balents, 2011, "Topological nodal semimetals," Phys. Rev. B 84, 235126.  
Butcher, P. N., and D. Cotter, 2008, The elements of nonlinear optics, Cambridge Studies in Modern Optics (Cambridge University Press, Cambridge, England).  
Büttiker, M., 1988, "Absence of backscattering in the quantum Hall effect in multiprobe conductors," Phys. Rev. B 38, 9375-9389.  
Bzdusek, T., Q. Wu, A. Ruegg, M. Sigrist, and A. A. Soluyanov, 2016, "Nodal-chain metals," Nature (London) 538, 75-78.

Cai, Y., J. Roslund, G. Ferrini, F. Arzani, X. Xu, C. Fabre, and N. Treps, 2017, "Multimode entanglement in reconfigurable graph states using optical frequency combs," Nat. Commun. 8, 15645.  
Callias, C., 1978, "Axial anomalies and index theorems on open spaces," Commun. Math. Phys. 62, 213-234.  
Calvanese Strinati, M., E. Cornfeld, D. Rossini, S. Barbarino, M. Dalmonte, R. Fazio, E. Sela, and L. Mazza, 2017, "Laughlin-like states in bosonic and fermionic atomic synthetic ladders," Phys. Rev. X 7, 021033.  
Can, T., Y. H. Chiu, M. Laskin, and P. Wiegmann, 2016, "Emergent conformal symmetry and geometric transport properties of quantum Hall states on singular surfaces," Phys. Rev. Lett. 117, 266803.  
Cardano, F., M. Maffei, F. Massa, B. Piccirillo, C. De Lisio, G. De Filippis, V. Cataudella, E. Santamato, and L. Marrucci, 2016, "Statistical moments of quantum-walk dynamics reveal topological quantum transitions," Nat. Commun. 7, 11439.  
Cardano, F., et al., 2015, "Quantum walks and wavepacket dynamics on a lattice with twisted photons," Sci. Adv. 1, e1500087.  
Cardano, F., et al., 2017, "Detection of Zak phases and topological invariants in a chiral quantum walk of twisted photons," Nat. Commun. 8, 15516.  
Carlon Zambon, N., et al., 2018, "Optically controlling the emission chirality of microlasers," arXiv:1806.04590.  
Carpentier, D., P. Delplace, M. Fruchart, and K. Gawedzki, 2015, "Topological Index for Periodically Driven Time-Reversal Invariant 2D Systems," Phys. Rev. Lett. 114, 106806.  
Carusotto, I., D. Gerace, H. E. Tureci, S. De Liberato, C. Ciuti, and A. Imamoglu, 2009, "Fermionized photons in an array of driven dissipative nonlinear cavities," Phys. Rev. Lett. 103, 033601.  
Carusotto, I., T. Volz, and A. Imamoglu, 2010, "Feshbach blockade: Single-photon nonlinear optics using resonantly enhanced cavity polariton scattering from biexciton states," Europhys. Lett. 90, 37001.  
Carusotto, I., and C. Ciuti, 2013, "Quantum fluids of light," Rev. Mod. Phys. 85, 299-366.  
Castro Neto, A. H., F. Guinea, N. M. R. Peres, K. S. Novoselov, and A. K. Geim, 2009, "The electronic properties of graphene," Rev. Mod. Phys. 81, 109-162.  
Cayssol, J., B. Dora, F. Simon, and R. Moessner, 2013, "Floquet topological insulators," Phys. Status Solidi RRL 7, 101-108.  
Celi, A., P. Massignan, J. Ruseckas, N. Goldman, I. B. Spielman, G. Juzeliūnas, and M. Lewenstein, 2014, "Synthetic gauge fields in synthetic dimensions," Phys. Rev. Lett. 112, 043001.  
Chabanov, A. A., and A. Genack, 2001, "Statistics of Dynamics of Localized Waves," Phys. Rev. Lett. 87, 233903.  
Chalker, J. T., and A. Dohmen, 1995, "Three-dimensional disordered conductors in a strong magnetic field: Surface states and quantum Hall plateaus," Phys. Rev. Lett. 75, 4496-4499.  
Chang, C.-Z., et al., 2013, "Experimental observation of the quantum anomalous Hall effect in a magnetic topological insulator," Science 340, 167-170.  
Chang, D. E., V. Vuletic, and M. D. Lukin, 2014, "Quantum nonlinear optics—photon by photon," Nat. Photonics 8, 685-694.  
Chang, M.-L., M. Xiao, W.-J. Chen, and C. T. Chan, 2017, "Multiple Weyl points and the sign change of their topological charges in woodpile photonic crystals," Phys. Rev. B 95, 125136.  
Cheianov, V. V., V. Fal'ko, and B. L. Altshuler, 2007, "The focusing of electron flow and a Veselago lens in graphene p-n junctions," Science 315, 1252-1255.  
Chen, C., Y.-Y. Yin, and D. S. Elliott, 1990, "Interference between optical transitions," Phys. Rev. Lett. 64, 507.  
Chen, W.-J., S.-J. Jiang, X.-D. Chen, B. Zhu, L. Zhou, J.-W. Dong, and C. T. Chan, 2014, "Experimental realization of photonic

topological insulator in a uniaxial metacrystal waveguide," Nat. Commun. 5, 5782.  
Chen, W.-J., M. Xiao, and C. T. Chan, 2016, "Photonic crystals possessing multiple Weyl points and the experimental observation of robust surface states," Nat. Commun. 7, 13038.  
Chen, X.-D., and J.-W. Dong, 2016, "Valley-protected backscattering suppression in silicon photonic graphene," arXiv:1602.03352.  
Cheng, X., C. Jouvaud, X. Ni, S. H. Mousavi, A. Z. Genack, and A. B. Khanikaev, 2016, "Robust reconfigurable electromagnetic pathways within a photonic topological insulator," Nat. Mater. 15, 542-548.  
Cherpakova, Z., C. Jorg, C. Dauer, F. Letscher, M. Fleischhauer, S. Eggert, S. Linden, and G. von Freymann, 2018, "Breakdown of topological protection under local periodic driving," arXiv:1807.02321.  
Chiao, R. Y., A. Antaramian, K. M. Ganga, H. Jiao, S. R. Wilkinson, and H. Nathel, 1988, "Observation of a topological phase by means of a nonplanar Mach-Zehnder interferometer," Phys. Rev. Lett. 60, 1214-1217.  
Chiu, C.-K., J.C.Y. Teo, A.P. Schnyder, and S. Ryu, 2016, "Classification of topological quantum matter with symmetries," Rev. Mod. Phys. 88, 035005.  
Cho, J., D. G. Angelakis, and S. Bose, 2008, "Fractional quantum Hall state in coupled cavities," Phys. Rev. Lett. 101, 246809.  
Chong, Y. D., X.-G. Wen, and M. Soljacic, 2008, "Effective theory of quadratic degeneracies," Phys. Rev. B 77, 235125.  
Christodoulides, D.N., F. Lederer, and Y. Silberberg, 2003, "Discretizing light behaviour in linear and nonlinear waveguide lattices," Nature (London) 424, 817-823.  
Chu, Y., P. Kharel, W. H. Renninger, L. D. Burkhart, L. Frunzio, P. T. Rakich, and R. J. Schoelkopf, 2017, “Quantum acoustics with superconducting qubits,” Science 358, 199–202.  
Ciuti, C., V. Savona, C. Piermarocchi, A. Quattropani, and P. Schwendimann, 1998, "Role of the exchange of carriers in elastic exciton-exciton scattering in quantum wells," Phys. Rev. B 58, 7926-7933.  
Claassen, M., C. H. Lee, R. Thomale, X.-L. Qi, and T. P. Devereaux, 2015, "Position-momentum duality and fractional quantum Hall effect in Chern insulators," Phys. Rev. Lett. 114, 236802.  
Clark, J. B., F. Lecocq, R. W. Simmonds, J. Aumentado, and J. D. Teufel, 2017, "Sideband cooling beyond the quantum backaction limit with squeezed light," Nature (London) 541, 191-195.  
Cohen-Tannoudji, C., J. Dupont-Roc, and G. Grynberg, 2008, Atom Photon Interactions (Wiley-VCH Verlag GmbH, Weinheim, Germany).  
Cominotti, M., and I. Carusotto, 2013, "Berry curvature effects in the Bloch oscillations of a quantum particle under a strong (synthetic) magnetic field," Europhys. Lett. 103, 10001.  
Cooper, M. L., G. Gupta, M. A. Schneider, W. M. J. Green, S. Assefa, F. Xia, Y. A. Vlasov, and S. Mookherjea, 2010, "Statistics of light transport in 235-ring silicon coupled-resonator optical waveguides," Opt. Express 18, 26505-26516.  
Cooper, N. R., 2008, "Rapidly rotating atomic gases," Adv. Phys. 57, 539-616.  
Creffield, C.E., G. Pieplow, F. Sols, and N. Goldman, 2016, "Realization of uniform synthetic magnetic fields by periodically shaking an optical square lattice," New J. Phys. 18, 093013.  
Crespi, A., G. Corrielli, G. Della Valle, R. Osellame, and S. Longhi, 2013, "Dynamic band collapse in photonic graphene," New J. Phys. 15, 013012.  
Dalibard, J., F. Gerbier, G. Juzeliūnas, and P. Öhberg, 2011, "Colloquium: Artificial gauge potentials for neutral atoms," Rev. Mod. Phys. 83, 1523.

Dana, I., Y. Avron, and J. Zak, 1985, "Quantised Hall conductance in a perfect crystal," J. Phys. C 18, L679.  
de Juan, F., M. Sturla, and M. A. H. Vozmediano, 2012, "Space Dependent Fermi Velocity in Strained Graphene," Phys. Rev. Lett. 108, 227205.  
Delplace, P., D. Ullmo, and G. Montambaux, 2011, “Zak phase and the existence of edge states in graphene,” Phys. Rev. B 84, 195452.  
Deng, X., L. Hong, X. Zheng, and L. Shen, 2015, "One-way regular electromagnetic mode immune to backscattering," Appl. Opt. 54, 4608-4612.  
De Nittis, G., and M. Lein, 2017, "Symmetry classification of topological photonic crystals," arXiv:1710.08104.  
Dennis, M. R., K. O'Holleran, and M. J. Padgett, 2009, "Singular optics: optical vortices and polarization singularities," Prog. Opt. 53, 293-363.  
Diehl, S., E. Rico, M. A. Baranov, and P. Zoller, 2011, "Topology by dissipation in atomic quantum wires," Nat. Phys. 7, 971-977.  
DiLiberto,M.,A.Hemmerich,and C.Morais Smith,2016, "Topologicalvarma superfluid in optical lattices,"Phys.Rev.Lett. 117,163001.  
Di Liberto, M., A. Recati, I. Carusotto, and C. Menotti, 2016, "Two-body physics in the Su-Schrieffer-Heeger model," Phys. Rev. A 94, 062704.  
Downing, C. A., and G. Weick, 2017, “Topological collective plasmons in bipartite chains of metallic nanoparticles,” Phys. Rev. B 95, 125426.  
Dreisow, F., R. Keil, A Tünnermann, S. Nolte, S. Longhi, and A. Szameit, 2012, "Klein tunneling of light in waveguide superlattices," Europhys. Lett. 97, 10008.  
Dubček, T., C. J. Kennedy, L. Lu, W. Ketterle, M. Soljacic, and H. Buljan, 2015, "Weyl points in three-dimensional optical lattices: synthetic magnetic monopoles in momentum space," Phys. Rev. Lett. 114, 225301.  
Dubček, T., K. Lelas, D. Jukić, R. Pezer, M. Soljacic, and H. Buljan, 2015, "The Harper-Hofstadter Hamiltonian and conical diffraction in photonic lattices with grating assisted tunneling," New J. Phys. 17, 125002.  
Dudarev, A. M., R. B. Diener, I. Carusotto, and Q. Niu, 2004, "Spin-orbit coupling and Berry phase with ultracold atoms in 2D optical lattices," Phys. Rev. Lett. 92, 153005.  
Dutta, S., and E. J. Mueller, 2018, "Coherent generation of photonic fractional quantum Hall states in a cavity and the search for anyonic quasiparticles," Phys. Rev. A 97, 033825.  
Eckardt, A., and E. Anisimovas, 2015, "High-frequency approximation for periodically driven quantum systems from a Floquet-space perspective," New J. Phys. 17, 093039.  
Eckardt, A., 2017, "Atomic quantum gases in periodically driven optical lattices," Rev. Mod. Phys. 89, 011004.  
Efremidis, N. K., S. Sears, D. N. Christodoulides, J. W. Fleischer, and M. Segev, 2002, "Discrete solitons in photorefractive optically induced photonic lattices," Phys. Rev. E 66, 046602.  
Eisenberg, H. S., Y. Silberberg, R. Morandotti, A. R. Boyd, and J. S. Aitchison, 1998, "Discrete spatial optical solitons in waveguide arrays," Phys. Rev. Lett. 81, 3383.  
Elliott, S. R., and M. Franz, 2015, “Colloquium: Majorana fermions in nuclear, particle, and solid-state physics,” Rev. Mod. Phys. 87, 137–163.  
Engelhardt, G., M. Benito, G. Platero, and T. Brandes, 2016, "Topological instabilities in ac-driven bosonic systems," Phys. Rev. Lett. 117, 045302.  
Engelhardt, G., and T. Brandes, 2015, "Topological Bogoliubov excitations in inversion-symmetric systems of interacting bosons," Phys. Rev. A 91, 053621.

Esaki, K., M. Sato, K.Hasebe, and M. Kohmoto, 2011, "Edge states and topological phases in non-Hermitian systems," Phys. Rev. B 84, 205128.  
Fang, C., Y. Chen, H.-Y. Kee, and L. Fu, 2015, "Topological nodal line semimetals with and without spin-orbital coupling," Phys. Rev. B 92, 081201.  
Fang, C., L. Lu, J. Liu, and L. Fu, 2016, "Topological semimetals with helicoid surface states," Nat. Phys. 12, 936-941.  
Fang, C., H. Weng, X. Dai, and Z. Fang, 2016, "Topological nodal line semimetals," Chin. Phys. B 25, 117106.  
Fang, K., and S. Fan, 2013a, "Controlling the flow of light using the inhomogeneous effective gauge field that emerges from dynamic modulation," Phys. Rev. Lett. 111, 203901.  
Fang, K., and S. Fan, 2013b, "Effective magnetic field for photons based on the magneto-optical effect," Phys. Rev. A 88, 043847.  
Fang, K., J. Luo, A. Metelmann, M. H. Matheny, F. Marquardt, A. A. Clerk, and O. Painter, 2017, "Generalized non-reciprocity in an optomechanical circuit via synthetic magnetism and reservoir engineering," Nat. Phys. 13, 465-471.  
Fang, K., Z. Yu, and S. Fan, 2011, "Microscopic theory of photonic one-way edge mode," Phys. Rev. B 84, 075477.  
Fang, K., Z. Yu, and S. Fan, 2012a, "Photonic Aharonov-Bohm effect based on dynamic modulation," Phys. Rev. Lett. 108, 153901.  
Fang, K., Z. Yu, and S. Fan, 2012b, "Realizing effective magnetic field for photons by controlling the phase of dynamic modulation," Nat. Photonics 6, 782-787.  
Faraon, A., I. Fushman, D. Englund, N. Stoltz, P. Petroff, and J. Vuckovic, 2008, "Coherent generation of non-classical light on a chip via photon-induced tunnelling and blockade," Nat. Phys. 4, 859-863.  
Fausti, D., R.I. Tobey, N. Dean, S. Kaiser, A. Dienst, M.C. Hoffmann, S. Pyon, T. Takayama, H. Takagi, and A. Cavalleri, 2011, "Light-induced superconductivity in a stripe-ordered cuprate," Science 331, 189-191.  
Fefferman, C. L., J. P. Lee-Thorp, and M. I. Weinstein, 2016, "Bifurcations of edge states—topologically protected and non-protected—in continuous 2D honeycomb structures," 2D Mater. 3, 014008.  
Fefferman, C., and M. Weinstein, 2012, "Honeycomb lattice potentials and Dirac points," J. Am. Math. Soc. 25, 1169-1220.  
Fefferman, C. L., J. P. Lee-Thorp, and M. I. Weinstein, 2014, "Topologically protected states in one-dimensional continuous systems and Dirac points," Proc. Natl. Acad. Sci. U.S.A. 111, 8759-8763.  
Fefferman, C. L., and M. I. Weinstein, 2014, "Wave packets in honeycomb structures and two-dimensional Dirac equations," Commun. Math. Phys. 326, 251-286.  
Firstenberg, O., T. Peyronel, Q.-Y. Liang, A. V. Gorshkov, M. D. Lukin, and V. Vuletic, 2013, "Attractive photons in a quantum nonlinear medium," Nature (London) 502, 71-75.  
Fitzpatrick, M., N. M. Sundaresan, A. C. Y. Li, J. Koch, and A. A. Houck, 2017, "Observation of a dissipative phase transition in a one-dimensional circuit QED lattice," Phys. Rev. X 7, 011016.  
Flaschner, N., D. Vogel, M. Tarnowski, B. S. Rem, D.-S. Luhmann, M. Heyl, J. C. Budich, L. Mathey, K. Sengstock, and C. Weitenberg, 2018, "Observation of dynamical vortices after quenches in a system with topology," Nat. Phys. 14, 265-268.  
Fleischer, J. W., M. Segev, N. K. Efremidis, and D. N. Christodoulides, 2003, "Observation of two-dimensional discrete solitons in optically induced nonlinear photonic lattices," Nature (London) 422, 147-150.

Fleury, R., D. Sounas, M.R. Haberman, and A. Alù, 2015, "Nonreciprocal acoustics," Acoustics Today 11, 14-21 [https://acousticstoday.org/issues/2015AT/Summer2015/#?page=16m].  
Fleury, R., D. L. Sounas, C. F. Sieck, M. R. Haberman, and A. Alù, 2014, "Sound isolation and giant linear nonreciprocity in a compact acoustic circulator," Science 343, 516-519.  
Franke-Arnold, S., G. Gibson, R. W. Boyd, and M. J. Padgett, 2011, "Rotary photon drag enhanced by a slow-light medium," Science 333, 65-67.  
Freedman, B., G. Bartal, M. Segev, R. Lifshitz, D. N. Christodoulides, and J. W. Fleischer, 2006, "Wave and defect dynamics in nonlinear photonic quasicrystals," Nature (London) 440, 1166-1169.  
Freedman, B., R. Lifshitz, J.W. Fleischer, and M. Segev, 2007, "Phason dynamics in nonlinear photonic quasicrystals," Nat. Mater. 6, 776-781.  
Frohlich, J., and B. Pedrini, 2000, "New applications of the chiral anomaly," in Mathematical Physics 2000, edited by A. Fokas, A. Grigoryan, T. Kibble, and B. Zegarlinski (Imperial College Press, London, United Kingdom), pp. 9-47.  
Fu, J.-X., J. Lian, R.-J. Liu, L. Gan, and Z.-Y. Li, 2011, "Unidirectional channel-drop filter by one-way gyromagnetic photonic crystal waveguides," Appl. Phys. Lett. 98, 211104-211104.  
Fu, J.-X., R.-J. Liu, L. Gan, and Z.-Y. Li, 2011, "Control and blockage of edge modes in magneto-optical photonic crystals," Europhys. Lett. 93, 24001.  
Fu, J.-X., R.-J. Liu, and Z.-Y. Li, 2010a, "Experimental demonstration of tunable gyromagnetic photonic crystals controlled by dc magnetic fields," Europhys. Lett. 89, 64003.  
Fu, J.-X., R.-J. Liu, and Z.-Y. Li, 2010b, "Robust one-way modes in gyromagnetic photonic crystal waveguides with different interfaces," Appl. Phys. Lett. 97, 041112-041112.  
Fu, L., 2011, "Topological crystalline insulators," Phys. Rev. Lett. 106, 106802.  
Fu, L., and C. L. Kane, 2006, "Time reversal polarization and a  $Z_{2}$  adiabatic spin pump," Phys. Rev. B 74, 195312.  
Fu, L., C. L. Kane, and E. J. Mele, 2007, "Topological insulators in three dimensions," Phys. Rev. Lett. 98, 106803.  
Furukawa, S., and M. Ueda, 2015, "Excitation band topology and edge matter waves in Bose-Einstein condensates in optical lattices," New J. Phys. 17, 115014.  
Galilo, B., D. K. K. Lee, and R. Barnett, 2015, "Selective population of edge states in a 2D topological band system," Phys. Rev. Lett. 115, 245302.  
Gangaraj, S. A. H., and G. W. Hanson, 2017, "Topologically protected unidirectional surface states in biased ferrites: duality and application to directional couplers," IEEE Antennas Wireless Propag. Lett. 16, 449-452.  
Gao, F., et al., 2016, "Probing topological protection using a designer surface plasmon structure," Nat. Commun. 7, 11619.  
Gao, W., M. Lawrence, B. Yang, F. Liu, F. Fang, B. Béri, J. Li, and S. Zhang, 2015, "Topological photonic phase in chiral hyperbolic metamaterials," Phys. Rev. Lett. 114, 037402.  
Gao, W., B. Yang, M. Lawrence, F. Fang, B. Béri, and S. Zhang, 2016, "Photonic Weyl degeneracies in magnetized plasma," Nat. Commun. 7, 12435.  
Gardiner, C. W., and M. J. Collett, 1985, "Input and output in damped quantum systems: Quantum stochastic differential equations and the master equation," Phys. Rev. A 31, 3761-3774.  
Gardiner, C.W., and P. Zoller, 2004, Quantum Noise (Springer-Verlag, Berlin).  
Gbur, G.J., 2016, Singular Optics (CRC Press, Boca Raton, FL).

Geerligs, L. J., V. F. Anderegg, P. A. M. Holweg, J. E. Mooij, H. Pothier, D. Esteve, C. Urbina, and M. H. Devoret, 1990, "Frequency-locked turnstile device for single electrons," Phys. Rev. Lett. 64, 2691-2694.  
Gerace, D., H. E. Tureci, A. Imamoglu, V. Giovannetti, and R. Fazio, 2009, "The quantum-optical Josephson interferometer," Nat. Phys. 5, 281-284.  
Gerry, C., and P. Knight, 2005, Introductory quantum optics (Cambridge University Press, Cambridge, England).  
Ghulinyan, M., F. R. Manzano, N. Prtljaga, M. Bernard, L. Pavesi, G. Pucker, and I. Carusotto, 2014, "Intermode reactive coupling induced by waveguide-resonator interaction," Phys. Rev. A 90, 053811.  
Goldman, N., J. C. Budich, and P. Zoller, 2016, "Topological quantum matter with ultracold gases in optical lattices," Nat. Phys. 12, 639-645.  
Goldman, N., and J. Dalibard, 2014, "Periodically driven quantum systems: Effective Hamiltonians and engineered gauge fields," Phys. Rev. X 4, 031027.  
Goldman, N., J. Dalibard, M. Aidelsburger, and N. R. Cooper, 2015, "Periodically driven quantum matter: The case of resonant modulations," Phys. Rev. A 91, 033632.  
Goldman, N., G. Jotzu, M. Messer, F. Gorg, R. Desbuquois, and T. Esslinger, 2016, "Creating topological interfaces and detecting chiral edge modes in a two-dimensional optical lattice," Phys. Rev. A 94, 043611.  
Goldman, N., I. Satija, P. Nikolic, A. Bermudez, M. A. Martin-Delgado, M. Lewenstein, and I. B. Spielman, 2010, "Realistic time-reversal invariant topological insulators with neutral atoms," Phys. Rev. Lett. 105, 255302.  
Goldman, N., G. Juzeliunas, P. Ohberg, and I. B. Spielman, 2014, "Light-induced gauge fields for ultracold atoms," Rep. Prog. Phys. 77, 126401.  
Gong, Z., Y. Ashida, K. Kawabata, K. Takasan, S. Higashikawa, and M. Ueda, 2018, "Topological phases of non-Hermitian systems," Phys. Rev. X 8, 031079.  
Gopalakrishnan, S., P. Ghaemi, and S. Ryu, 2012, "Non-Abelian SU (2) gauge fields through density wave order and strain in graphene," Phys. Rev. B 86, 081403.  
Goren, T., K. Plekhanov, F. Appas, and K. Le Hur, 2018, "Topological Zak phase in strongly coupled LC circuits," Phys. Rev. B 97, 041106.  
Gorlach, M., and M. Di Liberto, 2018, Phys. Rev. A 98, 063625.  
Gorlach, M. A., X. Ni, D. A. Smirnova, D. Korobkin, D. Zhirihin, A. P. Slobozhanyuk, P. A. Belov, A. Alù, and A. B. Khanikaev, 2018, "Far-field probing of leaky topological states in all-dielectric metasurfaces," Nat. Commun. 9, 909.  
Gorlach, M. A., and A. N. Poddubny, 2017, "Interaction-induced two-photon edge states in an extended hubbard model realized in a cavity array," Phys. Rev. A 95, 033831.  
Gorshkov, A. V., J. Otterbach, M. Fleischhauer, T. Pohl, and M. D. Lukin, 2011, "Photon-photon interactions via Rydberg blockade," Phys. Rev. Lett. 107, 133602.  
Graß, T., A. Celi, and M. Lewenstein, 2014, "Quantum magnetism of ultracold atoms with a dynamical pseudospin degree of freedom," Phys. Rev. A 90, 043628.  
Graß, T., C. Muschik, A. Celi, R. W. Chhajlany, and M. Lewenstein, 2015, "Synthetic magnetic fluxes and topological order in one-dimensional spin systems," Phys. Rev. A 91, 063612.  
Greentree, A. D., C. Tahan, J. H. Cole, and L. C. L. Hollenberg, 2006, "Quantum phase transitions of light," Nat. Phys. 2, 856-861.  
Grosche, S., A. Szameit, and M. Ornigotti, 2016, "Spatial Goos-Hänchen shift in photonic graphene," Phys. Rev. A 94, 063831.

Grusdt, F., and M. Fleischhauer, 2013, "Fractional quantum Hall physics with ultracold Rydberg gases in artificial gauge fields," Phys. Rev. A 87, 043628.  
Grusdt, F., F. Letscher, M. Hafezi, and M. Fleischhauer, 2014, "Topological growing of Laughlin states in synthetic gauge fields," Phys. Rev. Lett. 113, 155301.  
Grusdt, F., J. Otterbach, and M. Fleischhauer, 2013, private communication.  
Gu, X., A. F. Kockum, A. Miranowicz, Y.-x. Liu, and F. Nori, 2017, "Microwave photonics with superconducting quantum circuits," Phys. Rep. 718-719, 1-102.  
Guglielmon, J., S. Huang, K. P. Chen, and M. C. Rechtsman, 2017, "Prediction and realization of a photonic topological phase transition," in CLEO: QELS_Fundamental Science (IEEE, New York), pp. FM2G-6.  
Guinea, F., M. I. Katsnelson, and A. K. Geim, 2010, "Energy gaps and a zero-field quantum Hall effect in graphene by strain engineering," Nat. Phys. 6, 30-33.  
Gulevich, D. R., D. Yudin, D. V. Skryabin, I. V. Iorsh, and I. A. Shelykh, 2017, "Exploring nonlinear topological states of matter with exciton-polaritons: Edge solitons in kagome lattice," Sci. Rep. 7, 1780.  
Gullans, M. J., J. D. Thompson, Y. Wang, Q.-Y. Liang, V. Vuletic, M. D. Lukin, and A. V. Gorshkov, 2016, "Effective field theory for Rydberg polaritons," Phys. Rev. Lett. 117, 113601.  
Guo, Q., B. Yang, L. Xia, W. Gao, H. Liu, J. Chen, Y. Xiang, and S. Zhang, 2017, "Three dimensional photonic Dirac points in metamaterials," Phys. Rev. Lett. 119, 213901.  
Guo, Q., et al., 2018, "Observation of three-dimensional photonic Dirac points and spin-polarized surface arcs," arXiv:1810.02354.  
Gustafsson, M. V., T. Aref, A. F. Kockum, M. K. Ekstrom, G. Johansson, and P. Delsing, 2014, "Propagating phonons coupled to an artificial atom," Science 346, 207-211.  
Habraken, S. J. M., K. Stannigel, M. D. Lukin, P. Zoller, and P. Rabl, 2012, "Continuous mode cooling and phonon routers for phononic quantum networks," New J. Phys. 14, 115004.  
Hadad, Y., A. B. Khanikaev, and A. Alù, 2016, "Self-induced topological transitions and edge states supported by nonlinear staggered potentials," Phys. Rev. B 93, 155112.  
Haddad, L. H., and L. D. Carr, 2011, "Relativistic linear stability equations for the nonlinear Dirac equation in Bose-Einstein condensates," Europhys. Lett. 94, 56002.  
Haddad, L. H., and L. D. Carr, 2015, "The nonlinear dirac equation in Bose-Einstein condensates: vortex solutions and spectra in a weak harmonic trap," New J. Phys. 17, 113011.  
Haddad, L. H., C. M. Weaver, and L. D. Carr, 2015, "The nonlinear dirac equation in Bose-Einstein condensates: I. relativistic solitons in armchair nanoribbon optical lattices," New J. Phys. 17, 063033.  
Hafezi, M., P. Adhikari, and J. M. Taylor, 2015, "Chemical potential for light by parametric coupling," Phys. Rev. B 92, 174305.  
Hafezi, M., 2014, "Measuring topological invariants in photonic systems," Phys. Rev. Lett. 112, 210405.  
Hafezi, M., P. Adhikari, and J. M. Taylor, 2014, "Engineering three-body interaction and Pfaffian states in circuit QED systems," Phys. Rev. B 90, 060503.  
Hafezi, M., E. A. Demler, M. D. Lukin, and J. M. Taylor, 2011, "Robust optical delay lines with topological protection," Nat. Phys. 7, 907-912.  
Hafezi, M., M. D. Lukin, and J. M. Taylor, 2013, "Non-equilibrium fractional quantum Hall state of light," New J. Phys. 15, 063001.  
Hafezi, M., S. Mittal, J. Fan, A. Migdall, and J.M. Taylor, 2013, "Imaging topological edge states in silicon photonics," Nat. Photonics 7, 1001-1005.

Hafezi, M., and P. Rabl, 2012, "Optomechanically induced nonreciprocity in microring resonators," Opt. Express 20, 7672-7684.  
Haldane, F. D. M., 1988, "Model for a quantum Hall effect without Landau levels: Condensed-matter realization of the "parity anomaly"; Phys. Rev. Lett. 61, 2015-2018.  
Haldane, F. D. M., and S. Raghu, 2008, "Possible realization of directional optical waveguides in photonic crystals with broken time-reversal symmetry," Phys. Rev. Lett. 100, 013904.  
Halperin, B. I., 1982, "Quantized Hall Conductance, Current Carrying Edge States and Extended States in 2D Disordered Potential," Phys. Rev. B 25, 2185-2190.  
Halperin, B.I., 1987, "Possible states for a three-dimensional electron gas in a strong magnetic field," Jpn. J. Appl. Phys. 26, 1913.  
Hannay, J. H., 1985, "Angle variable holonomy in adiabatic excursion of an integrable hamiltonian," J. Phys. A 18, 221.  
Harari, G., M. A. Bandres, Y. Lumer, M. C. Rechtsman, Y. D. Chong, M. Khajavikhan, D. N. Christodoulides, and M. Segev, 2018, "Topological insulator laser: Theory," Science 359, eaar4003.  
Harper, P. G., 1955, "Single band motion of conduction electrons in a uniform magnetic field," Proc. Phys. Soc. London Sect. A 68, 874.  
Harris, S. E., 1989, "Lasers without inversion: Interference of lifetime-broadened resonances," Phys. Rev. Lett. 62, 1033-1036.  
Hartmann, M.J., F.G.S.L. Brandao, and M.B. Plenio, 2006, "Strongly interacting polaritons in coupled arrays of cavities," Nat. Phys. 2, 849-855.  
Hartstein, A., E. Burstein, A. A. Maradudin, R. Brewer, and R. F. Wallis, 1973, "Surface polaritons on semi-infinite gyromagnetic media," J. Phys. C 6, 1266.  
Hasan, M. Z., and C. L. Kane, 2010, "Colloquium: Topological insulators," Rev. Mod. Phys. 82, 3045-3067.  
Hatsugai, Y., 1993a, "Chern number and edge states in the integer quantum Hall effect," Phys. Rev. Lett. 71, 3697-3700.  
Hatsugai, Y., 1993b, "Edge states in the integer quantum Hall effect and the Riemann surface of the Bloch function," Phys. Rev. B 48, 11851-11862.  
Hatsugai, Y., and M. Kohmoto, 1990, "Energy spectrum and the quantum Hall effect on the square lattice with next-nearest-neighbor hopping," Phys. Rev. B 42, 8282.  
Haus, H. A., and W. Huang, 1991, “Coupled-mode theory,” Proc. IEEE 79, 1505-1518.  
Hayward, A. L. C., A. M. Martin, and A. D. Greentree, 2012, "Fractional quantum Hall physics in Jaynes-Cummings-Hubbard lattices," Phys. Rev. Lett. 108, 223602.  
He, C., X.-L. Chen, M.-H. Lu, X.-F. Li, W.-W. Wan, X.-S. Qian, R.-C. Yin, and Y.-F. Chen, 2010a, "Left-handed and right-handed one-way edge modes in a gyromagnetic photonic crystal," J. Appl. Phys. 107, 123117.  
He, C., X.-L. Chen, M.-H. Lu, X.-F. Li, W.-W. Wan, X.-S. Qian, R.-C. Yin, and Y.-F. Chen, 2010b, "Tunable one-way cross-waveguide splitter based on gyromagnetic photonic crystal," Appl. Phys. Lett. 96, 111111.  
He, C., X. Ni, H. Ge, X.-C. Sun, Y.-B. Chen, M.-H. Lu, X.-P. Liu, and Y.-F. Chen, 2016, "Acoustic topological insulator and robust oneway sound transport," Nat. Phys. 12, 1124-1129.  
He, C., X.-C. Sun, X.-P. Liu, M.-H. Lu, Y. Chen, L. Feng, and Y.-F. Chen, 2016, "Photonic topological insulator with broken time-reversal symmetry," Proc. Natl. Acad. Sci. U.S.A. 113, 4924-4928.  
Heisenberg, W., and H. Euler, 1936, “Folgerungen aus der diracsen theorie des positrons,” Z. Phys. A 98, 714-732.  
Hoffman, A. J., S. J. Srinivasan, S. Schmidt, L. Spietz, J. Augentado, H. E. Tureci, and A. A. Houck, 2011, "Dispersive photon blockade in a superconducting circuit," Phys. Rev. Lett. 107, 053602.

Hofstadter, D. R., 1976, "Energy levels and wave functions of bloch electrons in rational and irrational magnetic fields," Phys. Rev. B 14, 2239-2249.  
Houck, A. A., H. E. Türedi, and J. Koch, 2012, "On-chip quantum simulation with superconducting circuits," Nat. Phys. 8, 292-299.  
Hsu, C. W., B. Zhen, A. D. Stone, J. D. Joannopoulos, and M. Soljacic, 2016, "Bound states in the continuum," Nat. Rev. Mater. 1, 16048.  
Hu, W., J. C. Pillay, K. Wu, M. Pasek, P. P. Shum, and Y. D. Chong, 2015, "Measurement of a topological edge invariant in a microwave network," Phys. Rev. X 5, 011012.  
Hu, Y. C., and T. L. Hughes, 2011, "Absence of topological insulator phases in non-Hermitian P T-symmetric Hamiltonians," Phys. Rev. B 84, 153101.  
Hua, S., J. Wen, X. Jiang, Q. Hua, L. Jiang, and M. Xiao, 2016, "Demonstration of a chip-based optical isolator with parametric amplification," Nat. Commun. 7, 13657.  
Huang, K., 1987, Statistical Mechanics (Wiley, New York).  
Huang, X., Y. Lai, Z. H. Hang, H. Zheng, and C. T. Chan, 2011, "Dirac cones induced by accidental degeneracy in photonic crystals and zero-refractive-index materials," Nat. Mater. 10, 582-586.  
Huber, S.D., 2016, “Topological mechanics,” Nat. Phys. 12, 621-623.  
Iadecola, T., T. Schuster, and C. Chamon, 2016, "Non-Abelian braiding of light," Phys. Rev. Lett. 117, 073901.  
Imamoğlu, A., H. Schmidt, G. Woods, and M. Deutsch, 1997, "Strongly interacting photons in a nonlinear cavity," Phys. Rev. Lett. 79, 1467-1470.  
Imhof, S., et al., 2018, "Topoelectrical-circuit realization of topological corner modes," Nat. Phys. 14, 925.  
Inoue, J.-i., and A. Tanaka, 2010, "Photoinduced transition between conventional and topological insulators in two-dimensional electronic systems," Phys. Rev. Lett. 105, 017401.  
Ivanov, P. A., F. Letscher, J. Simon, and M. Fleischhauer, 2018, "Adiabatic flux insertion and growing of Laughlin states of cavity Rydberg polaritons," Phys. Rev. A 98, 013847.  
Jachymski, K., P. Bienias, and H. P. Buchler, 2016, "Three-body interaction of Rydberg slow-light polaritons," Phys. Rev. Lett. 117, 053601.  
Jackiw, R., and C. Rebbi, 1976, "Solitons with fermion number  $1/2$ ," Phys. Rev. D 13, 3398-3409.  
Jacobs, D. A., A.E. Miroshnichenko, Y. S. Kivshar, and A. B. Khanikaev, 2015, "Photonic topological Chern insulators based on Tellegen metacrystals," New J. Phys. 17, 125015.  
Jacqmin, T., I. Carusotto, I. Sagnes, M. Abbarchi, D. D. Solnyshkov, G. Malpuech, E. Galopin, A. Lemaitre, J. Bloch, and A. Amo, 2014, "Direct observation of Dirac cones and a flatband in a honeycomb lattice for polaritons," Phys. Rev. Lett. 112, 116402.  
Jaksch, D., and P. Zoller, 2003, "Creation of effective magnetic fields in optical lattices: The Hofstadter butterfly for cold neutral atoms," New J. Phys. 5, 56.  
Jalas, D., et al., 2013, "What is—and what is not—an optical isolator," Nat. Photonics 7, 579-582.  
Jia, N., N. Schine, A. Georgakopoulos, A. Ryou, L. W. Clark, A. Sommer, and J. Simon, 2018a, "A strongly interacting polaritonic quantum dot," Nat. Phys. 14, 550-554.  
Jia, N., N. Schine, A. Georgakopoulos, A. Ryou, A. Sommer, and J. Simon, 2018b, "Photons and polaritons in a broken-time-reversal nonplanar resonator," Phys. Rev. A 97, 013802.  
Jia, S., and J. W. Fleischer, 2009, "Nonlinear light propagation in rotating waveguide arrays," Phys. Rev. A 79, 041804.

Jin, D., L. Lu, Z. Wang, C. Fang, J. D. Joannopoulos, M. Soljačić, L. Fu, and N. X. Fang, 2016, "Topological magnetoplasmon," Nat. Commun. 7, 13486.  
Jitomirskaya, S., and C. A. Marx, 2012, "Analytic quasi-perodic cocycles with singularities and the Lyapunov exponent of extended Harpers model," Commun. Math. Phys. 316, 237-267.  
Joannopoulos, J. D., S. G. Johnson, J. N. Winn, and R. D. Meade, 2011, Photonic crystals: molding the flow of light (Princeton University Press, Princeton, NJ).  
John, S., 1987, "Strong localization of photons in certain disordered dielectric superlattices," Phys. Rev. Lett. 58, 2486-2489.  
Jörg, C., F. Letscher, M. Fleischhauer, and G. von Freymann, 2017, "Dynamic defects in photonic Floquet topological insulators," New J. Phys. 19, 083003.  
Jotzu, G., M. Messer, R. Desbuquois, M. Lebrat, T. Uehlinger, D. Greif, and T. Esslinger, 2014, "Experimental realization of the topological Haldane model with ultracold fermions," Nature (London) 515, 237.  
Jukić, D., and H. Buljan, 2013, "Four-dimensional photonic lattices and discrete tesseract solitons," Phys. Rev. A 87, 013814.  
Jünemann, J., A. Piga, S.-J. Ran, M. Lewenstein, M. Rizzi, and A. Bermudez, 2017, "Exploring interacting topological insulators with ultracold atoms: The synthetic Creutz-Hubbard model," Phys. Rev. X 7, 031057.  
Kane, C. L., and T. C. Lubensky, 2014, "Topological boundary modes in isostatic lattices," Nat. Phys. 10, 39-45.  
Kane, C. L., and E. J. Mele, 1997, "Size, Shape, and Low Energy Electronic Structure of Carbon Nanotubes," Phys. Rev. Lett. 78, 1932-1935.  
Kane, C. L., and E. J. Mele, 2005a, "Quantum spin Hall effect in graphene," Phys. Rev. Lett. 95, 226801.  
Kane, C. L., and E. J. Mele, 2005b, “ $Z_{2}$  topological order and the quantum spin Hall effect,” Phys. Rev. Lett. 95, 146802.  
Kang, Y., X. Ni, X. Cheng, A. B. Khanikaev, and A. Z. Genack, 2018, "Pseudo-spin-valley coupled edge states in a photonic topological insulator," Nat. Commun. 9, 3029.  
Kapit, E., M. Hafezi, and S.H. Simon, 2014, "Induced self-stabilization in fractional quantum Hall states of light," Phys. Rev. X 4, 031039.  
Karplus, R., and J. M. Luttinger, 1954, “Hall effect in ferromagnetics,” Phys. Rev. 95, 1154–1160.  
Karplus, R., and M. Neuman, 1951, "The scattering of light by light," Phys. Rev. 83, 776-784.  
Kartashov, Y. V., and D. V. Skryabin, 2016, "Modulational instability and solitary waves in polariton topological insulators," Optica 3, 1228-1236.  
Karzig, T., C.-E. Bardyn, N.H. Lindner, and G. Refael, 2015, "Topological polaritons," Phys. Rev. X 5, 031001.  
Katan, Y. T., R. Bekenstein, M. A. Bandres, Y. Lumer, P. Yonatan, and M. Segev, 2016, "Induction of topological transport by long ranged nonlinearity," in CLEO: QELS_Fundamental Science (Optical Society of America), pp. FM3A-6.  
Kavokin, A., G. Malpuech, and M. Glazov, 2005, "Optical Spin Hall Effect," Phys. Rev. Lett. 95, 136601.  
Kawabata, K., Y. Ashida, H. Katsura, and M. Ueda, 2018, "Parity-time-symmetric topological superconductor," Phys. Rev. B 98, 085116.  
Kawabata, K., S. Higashikawa, Z. Gong, Y. Ashida, and M. Ueda, 2019, "Topological unification of time-reversal and particle-hole symmetries in non-Hermitian physics," Nat. Commun. 10, 297.  
Kawabata, K., K. Shiozaki, and M. Ueda, 2018, "Non-Hermitian Chern insulator," Phys. Rev. B 98, 165148.

Kawakami, T., and X. Hu, 2017, "Symmetry-guaranteed and accidental nodal-line semimetals in fcc lattice," Phys. Rev. B 96, 235307.  
Kazimierczuk, T., D. Fröhlich, S. Scheel, H. Stolz, and M. Bayer, 2014, "Giant Rydberg excitons in the copper oxide  $\mathrm{Cu}_2\mathrm{O}$ ," Nature (London) 514, 343-347.  
Ke, Y., X. Qin, F. Mei, H. Zhong, Y. S. Kivshar, and C. Lee, 2016, "Topological phase transitions and Thouless pumping of light in photonic waveguide arrays," Laser Photonics Rev. 10, 995-1001.  
Keil, R., J. M. Zeuner, F. Dreisow, M. Heinrich, A. Tünnermann, S. Nolte, and A. Szameit, 2013, "The random mass Dirac model and long-range correlations on an integrated optical platform," Nat. Commun. 4, 1368.  
Ketoja, J. A., and I. I. Satija, 1997, "The re-entrant phase diagram of the generalized Harper equation," J. Phys. Condens. Matter 9, 1123.  
Khanikaev, A. B., and A. Alù, 2015, "Optical isolators: Nonlinear dynamic reciprocity," Nat. Photonics 9, 359-361.  
Khanikaev, A. B., S. H. Mousavi, W.-K. Tse, M. Kargarian, A. H. MacDonald, and G. Shvets, 2013, "Photonic topological insulators," Nat. Mater. 12, 233-239.  
Khanikaev, A. B., and G. Shvets, 2017, "Two-dimensional topological photonics," Nat. Photonics 11, 763.  
Kim, S., X. Xu, J.M. Taylor, and G. Bahl, 2017, "Dynamically induced robust phonon transport and chiral cooling in an optomechanical system," Nat. Commun. 8, 205.  
Kiss, T., J. Janszky, and P. Adam, 1994, "Time evolution of harmonic oscillators with time-dependent parameters: A step-function approximation," Phys. Rev. A 49, 4935-4942.  
Kitaev, A., V. Lebedev, and M. Feigelman, 2009, "Periodic table for topological insulators and superconductors," AIP Conf. Proc., 1134, 22-30.  
Kitagawa, T., 2012, "Topological phenomena in quantum walks: Elementary introduction to the physics of topological phases," Quantum Inf. Process. 11, 1107.  
Kitagawa, T., E. Berg, M. Rudner, and E. Demler, 2010, "Topological characterization of periodically-driven quantum systems," Phys. Rev. B 82, 235114.  
Kitagawa, T., M. A. Broome, A. Fedrizzi, M. S. Rudner, E. Berg, I. Kassal, A. Aspuru-Guzik, E. Demler, and A. G. White, 2012, "Observation of topologically protected bound states in photonic quantum walks," Nat. Commun. 3, 882.  
Kitagawa, T., T. Oka, A. Brataas, L. Fu, and E. Demler, 2011, "Transport properties of nonequilibrium systems under the application of light: Photoinduced quantum Hall insulators without Landau levels," Phys. Rev. B 84, 235108.  
Kitagawa, T., M. S. Rudner, E. Berg, and E. Demler, 2010, "Exploring topological phases with quantum walks," Phys. Rev. A 82, 033429.  
Kivshar, Y. S., and G. Agrawal, 2003, Optical solitons: from fibers to photonic crystals (Academic Press, New York).  
Klaers, J., J. Schmitt, F. Vewinger, and M. Weitz, 2010, “Bose-Einstein condensation of photons in an optical microcavity,” Nature (London) 468, 545–548.  
Klein, D. J., 1994, "Graphitic polymer strips with edge states," Chem. Phys. Lett. 217, 261-265.  
Klembt, S., et al., 2018, "Exciton-polariton topological insulator," Nature (London) 562, 552-556.  
Klitzing, K. v., G. Dorda, and M. Pepper, 1980, "New method for high-accuracy determination of the fine-structure constant based on quantized Hall resistance," Phys. Rev. Lett. 45, 494-497.  
Koch, J., A. A. Houck, K. Le Hur, and S. M. Girvin, 2010, "Time-reversal-symmetry breaking in circuit-QED-based photon lattices," Phys. Rev. A 82, 043811.

Kohmoto, M., 1985, "Topological invariant and the quantization of the Hall conductance," Ann. Phys. (N.Y.) 160, 343-354.  
Kohmoto, M., B. I. Halperin, and Y.-S. Wu, 1992, "Diophantine equation for the three-dimensional quantum Hall effect," Phys. Rev. B 45, 13488-13493.  
Kolkowitz, S., S. L. Bromley, T. Bothwell, M. L. Wall, G. E. Marti, A. P. Koller, X. Zhang, A. M. Rey, and J. Ye, 2017, "Spin-orbit-coupled fermions in an optical lattice clock," Nature (London) 542, 66-70.  
Kolovsky, A. R., 2011, "Creating artificial magnetic fields for cold atoms by photon-assisted tunneling," Europhys. Lett. 93, 20003.  
König, M., S. Wiedmann, C. Brüne, A. Roth, H. Buhmann, L. W. Molenkamp, X.-L. Qi, and S.-C. Zhang, 2007, "Quantum spin Hall insulator state in HgTe quantum wells," Science 318, 766-770.  
Koshino, M., H. Aoki, and B. I. Halperin, 2002, "Wrapping current versus bulk integer quantum Hall effect in three dimensions," Phys. Rev. B 66, 081301.  
Kouwenhoven, L. P., A. T. Johnson, N. C. van der Vaart, C. J. P. M. Harmans, and C. T. Foxon, 1991, "Quantized current in a quantum-dot turnstile using oscillating tunnel barriers," Phys. Rev. Lett. 67, 1626-1629.  
Kozii, V., and L. Fu, 2017, "Non-hermitian topological theory of finite-lifetime quasiparticles: Prediction of bulk Fermi arc due to exceptional point," arXiv:1708.05841.  
Kraus, Y.E., Y. Lahini, Z. Ringel, M. Verbin, and O. Zilberberg, 2012, "Topological states and adiabatic pumping in quasicrystals," Phys. Rev. Lett. 109, 106402.  
Kraus, Y. E., Z. Ringel, and O. Zilberberg, 2013, "Four-dimensional quantum Hall effect in a two-dimensional quasicrystal," Phys. Rev. Lett. 111, 226401.  
Kraus, Y.E., and O. Zilberberg, 2012, "Topological equivalence between the Fibonacci quasicrystal and the Harper model," Phys. Rev. Lett. 109, 116404.  
Kramer, D. O., and R. Khoremeriki, 2011, "Realization of discrete quantum billiards in a two-dimensional optical lattice," Phys. Rev. A 84, 041807.  
Kruk, S., A. Slobozhanyuk, D. Denkova, A. Poddubny, I. Kravchenko, A. Miroshnichenko, D. Neshev, and Y. Kivshar, 2017, "Edge states and topological phase transitions in chains of dielectric nanoparticles," Small 13, 1603190.  
Kuhl, U., and H.-J. Stöckmann, 1998, "Microwave realization of the Hofstadter butterfly," Phys. Rev. Lett. 80, 3232-3235.  
Kusudo, K., N. Y. Kim, A. Löffler, S. Höfling, A. Forchel, and Y. Yamamoto, 2013, "Stochastic formation of polariton condensates in two degenerate orbital states," Phys. Rev. B 87, 214503.  
Lacki, M., H. Pichler, A. Sterdyniak, A. Lyras, V.E. Lembessis, O. Al-Dossary, J.C. Budich, and P. Zoller, 2016, "Quantum hall physics with cold atoms in cylindrical optical lattices," Phys. Rev. A 93, 013604.  
Lahini, Y., A. Avidan, F. Pozzi, M. Sorel, R. Morandotti, D. N. Christodoulides, and Y. Silberberg, 2008, "Anderson localization and nonlinearity in one-dimensional disordered photonic lattices," Phys. Rev. Lett. 100, 013906.  
Lai, K., T. Ma, X. Bo, S. Anlage, and G. Shvets, 2016, "Experimental realization of a reflections-free compact delay line based on a photonic topological insulator," Sci. Rep. 6, 28453.  
Lai, Y., and H. A. Haus, 1989a, “Quantum theory of solitons in optical fibers. I. time-dependent Hartree approximation,” Phys. Rev. A 40, 844–853.  
Lai, Y., and H. A. Haus, 1989b, “Quantum theory of solitons in optical fibers. II. exact solution,” Phys. Rev. A 40, 854–866.

Lang, C., et al., 2011, "Observation of resonant photon blockade at microwave frequencies using correlation function measurements," Phys. Rev. Lett. 106, 243601.  
Larre, P.-É., and I. Carusotto, 2015, "Propagation of a quantum fluid of light in a cavityless nonlinear optical medium: General theory and response to quantum quenches," Phys. Rev. A 92, 043802.  
Larre, P.-É., and I. Carusotto, 2016, "Prethermalization in a quenched one-dimensional quantum fluid of light. intrinsic limits to the coherent propagation of a light beam in a nonlinear optical fiber," Eur. Phys. J. D 70, 45.  
Laughlin, R. B., 1981, "Quantized Hall conductivity in two dimensions," Phys. Rev. B 23, 5632-5633.  
Laughlin, R. B., 1983, "Anomalous quantum hall effect: An incompressible quantum fluid with fractionally charged excitations," Phys. Rev. Lett. 50, 1395-1398.  
Lebreuilly, J., A. Biella, F. Storme, D. Rossini, R. Fazio, C. Ciuti, and I. Carusotto, 2017, "Stabilizing strongly correlated photon fluids with non-Markovian reservoirs," Phys. Rev. A 96, 033828.  
Lebreuilly, J., M. Wouters, and I. Carusotto, 2016, "Towards strongly correlated photons in arrays of dissipative nonlinear cavities under a frequency-dependent incoherent pumping," C.R. Phys. 17, 836-860.  
Lee, C.H., S. Imhof, C. Berger, F. Bayer, J. Brehm, L.W. Molenkamp, T. Kiessling, and R. Thomale, 2018, "Topoelectrical circuits," Communications Physics 1, 39.  
Lee, S.-Y., I.-M. Lee, J. Park, S. Oh, W. Lee, K.-Y. Kim, and B. Lee, 2012, "Role of magnetic induction currents in nanoslit excitation of surface plasmon polaritons," Phys. Rev. Lett. 108, 213907.  
Lee, T. E., 2016, "Anomalous edge state in a non-Hermitian lattice," Phys. Rev. Lett. 116, 133903.  
Lee-Thorp, J. P., I. Vukicevic, X. Xu, J. Yang, C. L. Fefferman, C. W. Wong, and M. I. Weinstein, 2016, "Photonic realization of topologically protected bound states in domain-wall waveguide arrays," Phys. Rev. A 93, 033822.  
Le Feber, B., N. Rotenberg, and L. Kuipers, 2015, "Nanophotonic control of circular dipole emission," Nat. Commun. 6, 6695.  
Letscher, F., F. Grusdt, and M. Fleischhauer, 2015, "Growing quantum states with topological order," Phys. Rev. B 91, 184302.  
Levi, L., M. Rechtsman, B. Freedman, T. Schwartz, O. Manela, and M. Segev, 2011, "Disorder-enhanced transport in photonic quasicrystals," Science 332, 1541-1544.  
Leyder, C., M. Romanelli, J. Ph. Karr, E. Giacobino, T.C.H. Liew, M.M. Glazov, A.V. Kavokin, G. Malpuech, and A. Bramati, 2007, "Observation of the optical spin Hall effect," Nat. Phys. 3, 628-631.  
Leykam, D., K. Y. Bliokh, C. Huang, Y. D. Chong, and F. Nori, 2017, "Edge modes, degeneracies, and topological numbers in non-Hermitian systems," Phys. Rev. Lett. 118, 040401.  
Leykam, D., and Y. D. Chong, 2016, "Edge solitons in nonlinear-photonic topological insulators," Phys. Rev. Lett. 117, 143901.  
Leykam, D., S. Flach, and Y. D. Chong, 2017, "Flat bands in lattices with non-Hermitian coupling," Phys. Rev. B 96, 064305.  
Leykam, D., M. C. Rechtsman, and Y. D. Chong, 2016, "Anomalous topological phases and unpaired Dirac cones in photonic floquet topological insulators," Phys. Rev. Lett. 117, 013902.  
Li, F.-F., H.-X. Wang, Z. Xiong, Q. Lou, P. Chen, R.-X. Wu, Y. Poo, J.-H. Jiang, and S. John, 2018, "Topological light-trapping on a dislocation," Nat. Commun. 9, 2462.  
Li, Q.-B., Z. Li, and R.-x. Wu, 2015, "Bending self-collimated one-way light by using gyromagnetic photonic crystals," Appl. Phys. Lett. 107, 241907.

Li, Q.-B., R.-X. Wu, Y. Yang, and H.-L. Sun, 2013, "Modeling 2D gyromagnetic photonic crystals by modified FDTD method," Chin. Phys. Lett. 30, 074208.  
Li, Y., P. Sengupta, G. G. Batrouni, C. Miniatura, and B. Grémaud, 2015, "Berry curvature of interacting bosons in a honeycomb lattice," Phys. Rev. A 92, 043605.  
Li, Z., K. Aydin, and E. Ozbay, 2009, "Determination of the effective constitutive parameters of bianisotropic metamaterials from reflection and transmission coefficients," Phys. Rev. E 79, 026610.  
Li, Z., R.-x. Wu, Q.-b. Li, and Y. Poo, 2015, "Realization of self-guided unidirectional waveguides by a chain of gyromagnetic rods," Appl. Opt. 54, 1267-1272.  
Li, Z., R.-x. Wu, Y. Poo, Q.-b. Li, R.-j. Liu, and Z.-y. Li, 2014, "An experimental study on the bandwidth and tunability of MSP-based one-way transmission," Appl. Phys. A 117, 451-454.  
Li, Z., R.-x. Wu, Y. Poo, Z.-f. Lin, and Q.-B. Li, 2014, "Fusing electromagnetic one-way edge states to achieve broadband unidirectional wave transmission," J. Opt. 16, 125004.  
Li, Z.-Y., R.-J. Liu, L. Gan, J.-X. Fu, and Ji. Lian, 2014, "Nonreciprocal electromagnetic devices in gyromagnetic photonic crystals," Int. J. Mod. Phys. B 28, 1441010.  
Lian, J., J.-X. Fu, L. Gan, and Z.-Y. Li, 2012a, "Experimental realization of a magnetically tunable cavity in a gyromagnetic photonic crystal," Chin. Phys. Lett. 29, 074208.  
Lian, J., J.-X. Fu, L. Gan, and Z-Y. Li, 2012b, "Robust and disorder-immune magnetically tunable one-way waveguides in a gyromagnetic photonic crystal," Phys. Rev. B 85, 125108.  
Lin, J. Y., N. C. Hu, Y. Jian Chen, C. H. Lee, and X. Zhang, 2017, "Line nodes, Dirac points, and Lifshitz transition in two-dimensional nonsymorphic photonic crystals," Phys. Rev. B 96, 075438.  
Lin, Q., X.-Q. Sun, M. Xiao, S.-C. Zhang, and S. Fan, 2018, “A three-dimensional photonic topological insulator using a two-dimensional ring resonator lattice with a synthetic frequency dimension,” Sci. Adv. 4, eaat2774.  
Lin, Q., and S. Fan, 2014, "Light guiding by effective gauge field for photons," Phys. Rev. X 4, 031031.  
Lin, Q., and S. Fan, 2015, "Resonator-free realization of effective magnetic field for photons," New J. Phys. 17, 075008.  
Lin, Q., M. Xiao, L. Yuan, and S. Fan, 2016, "Photonic Weyl point in a two-dimensional resonator lattice with a synthetic frequency dimension," Nat. Commun. 7, 13731.  
Lin, S.-Y., E. Chow, V. Hietala, P. R. Villeneuve, and J. D. Joannopoulos, 1998, "Experimental demonstration of guiding and bending of electromagnetic waves in a photonic crystal," Science 282, 274-276.  
Lindner, N. H., G. Refael, and V. Galitski, 2011, "Floquet topological insulator in semiconductor quantum wells," Nat. Phys. 7, 490-495.  
Ling, C. W., M. Xiao, C. T. Chan, S. F. Yu, and K. H. Fung, 2015, "Topological edge plasmon modes between diatomic chains of plasmonic nanoparticles," Opt. Express 23, 2021-2031.  
Lira, H., Z. Yu, S. Fan, and M. Lipson, 2012, "Electrically driven nonreciprocity induced by interband photonic transition on a silicon chip," Phys. Rev. Lett. 109, 033901.  
Liu, C., W. Gao, B. Yang, and S. Zhang, 2017, "Disorder-induced topological state transition in photonic metamaterials," Phys. Rev. Lett. 119, 183901.  
Liu, K., L. Shen, and S. He, 2012, "One-way edge mode in a gyromagnetic photonic crystal slab," Opt. Lett. 37, 4110-4112.  
Liu, S., W.Lu, Z. Lin, and S. T. Chui, 2010, "Magnetically controllable unidirectional electromagnetic waveguiding devices designed with metamaterials," Appl. Phys. Lett. 97, 201113.

Liu, Y., and X. Zhang, 2011, “Metamaterials: a new frontier of science and technology,” Chem. Soc. Rev. 40, 2494–2507.  
Livi, L. F., et al., 2016, "Synthetic dimensions and spin-orbit coupling with an optical clock transition," Phys. Rev. Lett. 117, 220401.  
Lodahl, P., S. Mahmoodian, S. Stobbe, A. Rauschenbeutel, P. Schneeweiss, J. Volz, H. Pichler, and P. Zoller, 2017, "Chiral quantum optics," Nature (London) 541, 473-480.  
Lohse, M., C. Schweizer, H. M. Price, O. Zilberberg, and I. Bloch, 2018, "Exploring 4D quantum Hall physics with a 2D topological charge pump," Nature (London) 553, 55.  
Lohse, M., C. Schweizer, O. Zilberberg, M. Aidelsburger, and I. Bloch, 2016, "A Thouless quantum pump with ultracold bosonic atoms in an optical superlattice," Nat. Phys. 12, 350.  
Longhi, S., Y. Kominis, and V. Kovanis, 2018, “Presence of temporal dynamical instabilities in topological insulator lasers,” Europhys. Lett. 122, 14004.  
Longhi, S., 2011, "Photonic Bloch oscillations of correlated particles," Opt. Lett. 36, 3248-3250.  
Longhi, S., 2013, "Effective magnetic fields for photons in waveguide and coupled resonator lattices," Opt. Lett. 38, 3570-3573.  
Longhi, S., 2015, "Synthetic gauge fields for light beams in optical resonators," Opt. Lett. 40, 2941-2944.  
Lu, H.-I., M. Schemmer, L. M. Aycock, D. Genkina, S. Sugawa, and I. B. Spielman, 2016, "Geometrical pumping with a Bose-Einstein condensate," Phys. Rev. Lett. 116, 200402.  
Lu, J., L. Shen, X. Deng, X. Li, and X. Zheng, 2013, "Impact of photonic crystal boundary shape on the existence of one-way edge mode," Appl. Opt. 52, 5216-5220.  
Lu, L., C. Fang, L. Fu, S. G. Johnson, J. D. Joannopoulos, and M. Soljačić, 2016, "Symmetry-protected topological photonic crystal in three dimensions," Nat. Phys. 12, 337-340.  
Lu, L., L. Fu, J. D. Joannopoulos, and M. Soljacic, 2013, "Weyl points and line nodes in gyroid photonic crystals," Nat. Photonics 7, 294-299.  
Lu, L., J. D. Joannopoulos, and M. Soljačić, 2014, “Topological photonics,” Nat. Photonics 8, 821–829.  
Lu, L., J. D. Joannopoulos, and M. Soljacic, 2016, "Topological states in photonic systems," Nat. Phys. 12, 626-629.  
Lu, L., Z. Wang, D. Ye, L. Ran, L. Fu, J. D. Joannopoulos, and M. Soljacic, 2015, "Experimental observation of Weyl points," Science 349, 622-624.  
Lu, L., H. Gao, and Z. Wang, 2018, "Topological one-way fiber of second Chern number," Nat. Commun. 9, 5384.  
Lu, Y., N. Jia, L. Su, C. Owens, G. Juzeliūnas, D. I. Schuster, and J. Simon, 2019, "Probing the Berry curvature and Fermi arcs of a Weyl circuit," Phys. Rev. B 99, 020302.  
Lumer, Y., M. A. Bandres, M. Heinrich, L. Maczewsky, H. Herzig-Sheinfux, A. Szameit, and M. Segev, 2018, "Observation of light guiding by artificial gauge fields," arXiv:1808.10207.  
Lumer, Y., Y. Plotnik, M.C. Rechtsman, and M. Segev, 2013a, "Nonlinearly induced P T transition in photonic systems," Phys. Rev. Lett. 111, 263901.  
Lumer, Y., Y. Plotnik, M. C. Rechtsman, and M. Segev, 2013b, "Self-localized states in photonic topological insulators," Phys. Rev. Lett. 111, 243905.  
Lumer, Y., M. C. Rechtsman, Y. Plotnik, and M. Segev, 2016, "Instability of bosonic topological edge states in the presence of interactions," Phys. Rev. A 94, 021801.  
Luo, K., R. Yu, and H. Weng, 2018, "Topological nodal states in circuit lattice," Research 2018, 6793752.

Luo, X., M. Zhou, J. Liu, T. Qiu, and Z. Yu, 2016, "Magneto-optical metamaterials with extraordinarily strong magneto-optical effect," Appl. Phys. Lett. 108, 131104.  
Luo, X.-W., X. Zhou, C.-F. Li, J.-S. Xu, G.-C. Guo, and Z.-W. Zhou, 2015, "Quantum simulation of 2D topological physics in a 1D array of optical cavities," Nat. Commun. 6, 7704.  
Luo, X.-W., X. Zhou, J.-S. Xu, C.-F. Li, G.-C. Guo, C. Zhang, and Z.-W. Zhou, 2017, "Synthetic-lattice enabled all-optical devices based on orbital angular momentum of light," Nat. Commun. 8, 16097.  
Lustig, E., S. Weimann, Y. Plotnik, Y. Lumer, M. A. Bandres, A. Szameit, and M. Segev, 2018, "Photonic topological insulator in synthetic dimensions," arXiv:1807.01983.  
Luttinger, J. M., 1951, "The effect of a magnetic field on electrons in a periodic potential," Phys. Rev. 84, 814-817.  
Ma, R., C. Owens, A. LaChelle, D. I. Schuster, and J. Simon, 2017, "Hamiltonian tomography of photonic lattices," Phys. Rev. A 95, 062120.  
Ma, R., et al., 2019, "A dissipatively stabilized Mott insulator of photons," Nature (London) 566, 51-57.  
Ma, T., A. B. Khanikaev, S. H. Mousavi, and G. Shvets, 2015, "Guiding electromagnetic waves around sharp corners: Topologically protected photonic transport in metawaveguides," Phys. Rev. Lett. 114, 127401.  
Ma, T., and G. Shvets, 2016, "All-Si valley-Hall photonic topological insulator," New J. Phys. 18, 025012.  
MacDonald, A. H., and P. Streda, 1984, "Quantized Hall effect and edge currents," Phys. Rev. B 29, 1616-1619.  
Maczewsky, L. J., J. M. Zeuner, S. Nolte, and A. Szameit, 2017, "Observation of photonic anomalous Floquet topological insulators," Nat. Commun. 8, 13756.  
Maffei, M., A. Dauphin, F. Cardano, M. Lewenstein, and P. Massignan, 2018, "Topological characterization of chiral models through their long time dynamics," New J. Phys. 20, 013023.  
Maghrebi, M. F., M. J. Gullans, P. Bienias, S. Choi, I. Martin, O. Firstenberg, M. D. Lukin, H. P. Buchler, and A. V. Gorshkov, 2015, "Coulomb bound states of strongly interacting photons," Phys. Rev. Lett. 115, 123601.  
Maghrebi, M. F., N. Y. Yao, M. Hafezi, T. Pohl, O. Firstenberg, and A. V. Gorshkov, 2015, "Fractional quantum Hall states of Rydberg polaritons," Phys. Rev. A 91, 033838.  
Makris, K.G., R. El-Ganainy, D.N. Christodoulides, and Z.H. Musslimani, 2008, "Beam dynamics in P T symmetric optical lattices," Phys. Rev. Lett. 100, 103904.  
Malkova, N., I. Hromada, X. Wang, G. Bryant, and Z. Chen, 2009, "Observation of optical shockley-like surface states in photonic superlattices," Opt. Lett. 34, 1633-1635.  
Malzard, S., C. Poli, and H. Schomerus, 2015, "Topologically protected defect states in open photonic systems with non-Hermitian charge-conjugation and parity-time symmetry," Phys. Rev. Lett. 115, 200402.  
Malzard, S., and H. Schomerus, 2018a, "Bulk and edge-state arcs in non-Hermitian coupled-resonator arrays," Phys. Rev. A 98, 033807.  
Malzard, S., and H. Schomerus, 2018b, "Nonlinear mode competition and symmetry-protected power oscillations in topological lasers," New J. Phys. 20, 063044.  
Mancini, M., et al., 2015, "Observation of chiral edge states with neutral fermions in synthetic Hall ribbons," Science 349, 1510-1513.  
Mansha, S., and Y.D. Chong, 2017, "Robust edge states in amorphous gyromagnetic photonic lattices," Phys. Rev. B 96, 121405.

Marqués, R., F. Medina, and R. Rafii-El-Idrissi, 2002, "Role of bianisotropy in negative permeability and left-handed metamaterials," Phys. Rev. B 65, 144440.  
Martinez Alvarez, V. M., J. E. Barrios Vargas, M. Berdakin, and L. E. F. Foa Torres, 2018, "Topological states of non-Hermitian systems," Eur. Phys. J. Spec. Top. 227, 1295-1308.  
Mei, F., Z.-Y. Xue, D.-W. Zhang, L. Tian, C. Lee, and S.-L. Zhu, 2016, "Witnessing topological Weyl semimetal phase in a minimal circuit-QED lattice," Quant. Sci. Technol. 1, 015006.  
Mei, F., J.-B. You, W. Nie, R. Fazio, S.-L. Zhu, and L. C. Kwek, 2015, "Simulation and detection of photonic Chern insulators in a one-dimensional circuit-QED lattice," Phys. Rev. A 92, 041805.  
Meier, E. J., F. A. An, A. Dauphin, M. Maffei, P. Massignan, T. L. Hughes, and B. Gadway, 2018, "Observation of the topological Anderson insulator in disordered atomic wires," Science 362, 929-933.  
Mekis, A., J. C. Chen, I. Kurland, S. Fan, P. R. Villeneuve, and J. D. Joannopoulos, 1996, "High transmission through sharp bends in photonic crystal waveguides," Phys. Rev. Lett. 77, 3787.  
Meng, G., 2003, "Geometric construction of the quantum Hall effect in all even dimensions," J. Phys. A 36, 9415.  
Metelmann, A., and A.A. Clerk, 2015, “Nonreciprocal photon transmission and amplification via reservoir engineering,” Phys. Rev. X 5, 021025.  
Mikami, T., S. Kitamura, K. Yasuda, N. Tsuji, T. Oka, and H. Aoki, 2016, "Brillouin-Wigner theory for high-frequency expansion in periodically driven systems: Application to Floquet topological insulators," Phys. Rev. B 93, 144307.  
Miliévic, M. T. Ozawa, G. Montambaux, I. Carusotto, E. Galopin, A. Lemaitre, L. Le Gratiet, I. Sagnes, J. Bloch, and A. Amo, 2017, "Orbital Edge States in a Photonic Honeycomb Lattice," Phys. Rev. Lett. 118, 107403.  
Miliévic, M., G. Montambaux, T. Ozawa, I. Sagnes, A. Lemaitre, L. Le Gratiet, A. Harouri, J. Bloch, and A. Amo, 2018, "Tilted and type-III Dirac cones emerging from flat bands in photonic orbital graphene," arXiv:1807.08650.  
Milicevic, M., et al., 2015, "Edge states in polariton honeycomb lattices," 2D Mater. 2, 034012.  
Milman, P., Y. Castin, and L. Davidovich, 2000, "Decoherence as phase diffusion," Phys. Rev. A 61, 063803.  
Minkov, M., and V. Savona, 2016, "Haldane quantum hall effect for light in a dynamically modulated array of resonators," Optica 3, 200-206.  
Mirek, R., M. Król, K. Lekenta, J.-G. Rousset, M. Nawrocki, M. Kulczykowski, M. Matuszewski, J. Szczytko, W. Pacuski, and B. Pietka, 2017, "Angular dependence of giant Zeeman effect for semimagnetic cavity polaritons," Phys. Rev. B 95, 085429.  
Mitsch, R., C. Sayrin, B. Albrecht, P. Schneeweiss, and A. Rauschenbeutel, 2014, "Quantum state-controlled directional spontaneous emission of photons into a nanophotonic waveguide," Nat. Commun. 5, 5713.  
Mittal, S., J. Fan, S. Faez, A. Migdall, J. M. Taylor, and M. Hafezi, 2014, "Topologically robust transport of photons in a synthetic gauge field," Phys. Rev. Lett. 113, 087403.  
Mittal, S., S. Ganeshan, J. Fan, A. Vaezi, and M. Hafezi, 2016, "Measurement of topological invariants in a 2D photonic system," Nat. Photonics 10, 180.  
Mittal, S., and M. Hafezi, 2017, "Topologically robust generation of correlated photon pairs," arXiv:1709.09984.  
Mittal, S., V. V. Orre, and M. Hafezi, 2016, "Topologically robust transport of entangled photons in a 2D photonic system," Opt. Express 24, 15631-15641.

Miyake, H., G. A. Siviloglou, C. J. Kennedy, W. C. Burton, and W. Ketterle, 2013, "Realizing the Harper Hamiltonian with laser-assisted tunneling in optical lattices," Phys. Rev. Lett. 111, 185302.  
Moitra, P., Y. Yang, Z. Anderson, I. I. Kravchenko, D. P. Briggs, and J. Valentine, 2013, "Realization of an all-dielectric zero-index optical metamaterial," Nat. Photonics 7, 791-795.  
Mondragon-Shem, I., T. L. Hughes, J. Song, and E. Prodan, 2014, "Topological Criticality in the Chiral-Symmetric AIII Class at Strong Disorder," Phys. Rev. Lett. 113, 046802.  
Mong, R. S. K, and V. Shivamoggi, 2011, "Edge states and the bulk-boundary correspondence in Dirac Hamiltonians," Phys. Rev. B 83, 125109.  
Montambaux, G., and M. Kohmoto, 1990, "Quantized Hall effect in three dimensions," Phys. Rev. B 41, 11417-11421.  
Montambaux, G., F. Piechon, J.-N. Fuchs, and M. O. Goerbig, 2009, "Merging of Dirac points in a two-dimensional crystal," Phys. Rev. B 80, 153412.  
Moore, G., and N. Read, 1991, "Nonabelions in the fractional quantum Hall effect," Nucl. Phys. B 360, 362-396.  
Moore, J. E., and L. Balents, 2007, "Topological invariants of time-reversal-invariant band structures," Phys. Rev. B 75, 121306.  
Moos, M., M. Honing, R. Unanyan, and M. Fleischhauer, 2015, "Many-body physics of Rydberg dark-state polaritons in the strongly interacting regime," Phys. Rev. A 92, 053846.  
Möttönen, M., J. J. Vartiainen, and J. P. Pekola, 2008, "Experimental determination of the Berry phase in a superconducting charge pump," Phys. Rev. Lett. 100, 177201.  
Mukherjee, S., H. K. Chandrasekharan, P. Ohberg, N. Goldman, and R. R. Thomson, 2018, "State-recycling and time-resolved imaging in topological photonic lattices," Nat. Commun. 9, 4209.  
Mukherjee, S., A. Spracklen, D. Choudhury, N. Goldman, P. Ohberg, E. Andersson, and R. R. Thomson, 2015, "Modulation-assisted tunneling in laser-fabricated photonic Wannier-Stark ladders," New J. Phys. 17, 115002.  
Mukherjee, S., A. Spracklen, M. Valiente, E. Andersson, P. Ohberg, N. Goldman, and R. R. Thomson, 2017, "Experimental observation of anomalous topological edge modes in a slowly driven photonic lattice," Nat. Commun. 8, 13918.  
Mukherjee, S., M. Valiente, N. Goldman, A. Spracklen, E. Andersson, P. Ohberg, and R. R. Thomson, 2016, "Observation of pair tunneling and coherent destruction of tunneling in arrays of optical waveguides," Phys. Rev. A 94, 053853.  
Nagaosa, N., J. Sinova, S. Onoda, A. H. MacDonald, and N. P. Ong, 2010, "Anomalous Hall effect," Rev. Mod. Phys. 82, 1539-1592.  
Nakada, K., M. Fujita, G. Dresselhaus, and M. Dresselhaus, 1996, "Edge state in graphene ribbons: Nanometer size effect and edge shape dependence," Phys. Rev. B 54, 17954-17961.  
Nakahara, M., 2003, Geometry, Topology and Physics (CRC Press, Boca Raton, FL), 2nd ed.  
Nakajima, S., T.Tomita, S. Taie, T. Ichinose, H. Ozawa, L. Wang, M. Troyer, and Y. Takahashi, 2016, "Topological Thouless pumping of ultracold fermions," Nat. Phys. 12, 296.  
Nalitov, A. V., D. D. Solnyshkov, and G. Malpuech, 2015, “Polariton  $\mathbb{Z}$  topological insulator,” Phys. Rev. Lett. 114, 116401.  
Nathan, F., and M. S. Rudner, 2015, "Topological singularities and the general classification of Floquet Bloch systems," New J. Phys. 17, 125014.  
Nayak, C., S. H. Simon, A. Stern, M. Freedman, and S. Das Sarma, 2008, "Non-Abelian anyons and topological quantum computation," Rev. Mod. Phys. 80, 1083-1159.  
Naz, E. S. G., I. C. Fulga, L. Ma, O. G. Schmidt, and J. van den Brink, 2018, "Topological phase transition in a stretchable photonic crystal," Phys. Rev. A 98, 033830.

Ningyuan, J., A. Georgakopoulos, A. Ryou, N. Schine, A. Sommer, and J. Simon, 2016, "Observation and characterization of cavity Rydberg polaritons," Phys. Rev. A 93, 041802.  
Ningyuan, J., C. Owens, A. Sommer, D. Schuster, and J. Simon, 2015, "Time-and site-resolved dynamics in a topological circuit," Phys. Rev. X 5, 021031.  
Niu, Q., and D.J. Thouless, 1984, "Quantised adiabatic charge transport in the presence of substrate disorder and many-body interaction," J. Phys. A 17, 2453.  
Niu, Q., D.J. Thouless, and Y.-S Wu, 1985, "Quantized Hall conductance as a topological invariant," Phys. Rev. B 31, 3372-3377.  
Nixon, M., E. Ronen, A. A. Friesem, and N. Davidson, 2013, "Observing Geometric Frustration with Thousands of Coupled Lasers," Phys. Rev. Lett. 110, 184102.  
Noda, S., 2016, "Photonic-crystal cavities," in Optical Fiber Communication Conference (Optical Society of America), p. Th1K.1.  
Noh, C., and D.G. Angelakis, 2017, "Quantum simulations and many-body physics with light," Rep. Prog. Phys. 80, 016401.  
Noh, J., W. A. Benalcazar, S. Huang, M. J. Collins, K. P. Chen, T. L. Hughes, and M. C. Rechtsman, 2018, "Topological protection of photonic mid-gap defect modes," Nat. Photonics 12, 408-415.  
Noh, J., S. Huang, K. Chen, and M. C. Rechtsman, 2018, "Observation of Photonic Topological Valley-Hall Edge States," Phys. Rev. Lett. 120, 063902.  
Noh, J., S. Huang, D. Leykam, Y. D. Chong, K. P. Chen, and M. C. Rechtsman, 2017, "Experimental observation of optical Weyl points and Fermi arc-like surface states," Nat. Phys. 13, 611-617.  
Nunnenkamp, A., J. Koch, and S. M. Girvin, 2011, "Synthetic gauge fields and homodyne transmission in Jaynes-Cummings lattices," New J. Phys. 13, 095008.  
Ochiai, T., 2015a, "Non-reciprocity and topology in optics: One-way road for light via surface magnon polariton," Sci. Technol. Adv. Mater. 16, 014401.  
Ochiai, T., 2015b, "Time-reversal-violating photonic topological insulators with helical edge states," J. Phys. Soc. Jpn. 84, 054401.  
Ochiai, T., 2016, "Floquet-Weyl and Floquet-topological-insulator phases in a stacked two-dimensional ring-network lattice," J. Phys. Condens. Matter 28, 425501.  
Ochiai, T., 2017, "Gapless surface states originating from accidentally degenerate quadratic band touching in a three-dimensional tetragonal photonic crystal," Phys. Rev. A 96, 043842.  
O'Connell, A. D., et al., 2010, "Quantum ground state and single-phonon control of a mechanical resonator," Nature (London) 464, 697-703.  
O'Connor, D., P. Ginzburg, F. J. Rodríguez-Fortuno, G. A. Wurtz, and A. V. Zayats, 2014, "Spin-orbit coupling in surface plasmon scattering by nanostructures," Nat. Commun. 5, 5327.  
Oka, T., and H. Aoki, 2009, "Photovoltaic Hall effect in graphene," Phys. Rev. B 79, 081406.  
Onbasli, M. C., L. Beran, M. Zahradnik, M. Kučera, R. Antoš, J. Mistrik, G. F. Dionne, M. Veis, and C. A. Ross, 2016, "Optical and magneto-optical behavior of cerium yttrium iron garnet thin films at wavelengths of  $200 - 1770\mathrm{nm}$ ," Sci. Rep. 6, 23640.  
Ota, Y., R. Katsumi, K. Watanabe, S. Iwamoto, and Y. Arakawa, 2018, "Topological photonic crystal nanocavity laser," Commun. Phys. 1, 86.  
Otterbach, J., J. Ruseckas, R. G. Unanyan, G. Juzeliunas, and M. Fleischhauer, 2010, "Effective magnetic fields for stationary light," Phys. Rev. Lett. 104, 033903.  
Owens, C., A. LaChapelle, B. Saxberg, B. M. Anderson, R. Ma, J. Simon, and D. I. Schuster, 2018, "Quarter-flux Hofstadter lattice in

a qubit-compatible microwave cavity array," Phys. Rev. A 97, 013818.  
Ozawa, T., 2018, "Steady-state Hall response and quantum geometry of driven-dissipative lattices," Phys. Rev. B 97, 041108(R).  
Ozawa, T., A. Amo, J. Bloch, and I. Carusotto, 2017, "Klein tunneling in driven-dissipative photonic graphene," Phys. Rev. A 96, 013813.  
Ozawa, T., and I. Carusotto, 2014, "Anomalous and quantum Hall effects in lossy photonic lattices," Phys. Rev. Lett. 112, 133902.  
Ozawa, T., and I. Carusotto, 2017, "Synthetic dimensions with magnetic fields and local interactions in photonic lattices," Phys. Rev. Lett. 118, 013601.  
Ozawa, T., H. M. Price, and I. Carusotto, 2015, "Momentum-space Harper-Hofstadter model," Phys. Rev. A 92, 023609.  
Ozawa, T., H. M. Price, and I. Carusotto, 2016, "Quantum Hall effect in momentum space," Phys. Rev. B 93, 195201.  
Ozawa, T., H. M. Price, N. Goldman, O. Zilberberg, and I. Carusotto, 2016, "Synthetic dimensions in integrated photonics: From optical isolation to four-dimensional quantum Hall physics," Phys. Rev. A 93, 043827.  
Painter, O., R. K. Lee, A. Scherer, A. Yariv, J. D. O'brien, P. D. Dapkus, and I. Kim, 1999, "Two-dimensional photonic band-gap defect mode laser," Science 284, 1819-1821.  
Pan, M., H. Zhao, P. Miao, S. Longhi, and L. Feng, 2018, "Photonic zero mode in a non-Hermitian photonic lattice," Nat. Commun. 9, 1308.  
Pancharatnam, S., 1956, "Generalized theory of interference, and its applications," Proc. Indian Acad. Sci. A 44, 247-262.  
Parto, M., S. Wittek, H. Hodaei, G. Harari, M. A. Bandres, J. Ren, M. C. Rechtsman, M. Segev, D. N. Christodoulides, and M. Khajavikhan, 2018, "Edge-Mode Lasing in 1D Topological Active Arrays," Phys. Rev. Lett. 120, 113901.  
Peano, V., M. Houde, C. Brendel, F. Marquardt, and A. A. Clerk, 2016, "Topological phase transitions and chiral inelastic transport induced by the squeezing of light," Nat. Commun. 7, 10779.  
Peano, V., M. Houde, F. Marquardt, and A. A. Clerk, 2016, "Topological quantum fluctuations and traveling wave amplifiers," Phys. Rev. X 6, 041026.  
Peierls, R., 1933, “Zur theorie des diamagnetismus von leitungsellektronen,” Z. Phys. 80, 763-791.  
Peleg, O., G. Bartal, B. Freedman, O. Manela, M. Segev, and D. N. Christodoulides, 2007, “Conical Diffraction and Gap Solitons in Honeycomb Photonic Lattices,” Phys. Rev. Lett. 98, 103901.  
Pelegri, G., J. Polo, A. Turpin, M. Lewenstein, J. Mompart, and V. Ahufinger, 2017, "Single-atom edge-like states via quantum interference," Phys. Rev. A 95, 013614.  
Pendry, J. B., A. J. Holden, D. J. Robbins, and W. J. Stewart, 1999, "Magnetism from conductors and enhanced nonlinear phenomena," IEEE Trans. Microwave Theory Tech. 47, 2075-2084.  
Peropadre, B., D. Zueco, F. Wulschner, F. Deppe, A. Marx, R. Gross, and J. J. García-Ripoll, 2013, "Tunable coupling engineering between superconducting resonators: From sidebands to effective gauge fields," Phys. Rev. B 87, 134504.  
Petersen, J., J. Volz, and A. Rauschenbeutel, 2014, "Chiral nanophotonic waveguide interface based on spin-orbit interaction of light," Science 346, 67-71.  
Petrescu, A., A. A. Houck, and K. Le Hur, 2012, "Anomalous Hall effects of light and chiral edge modes on the kagome lattice," Phys. Rev. A 86, 053804.  
Petrosyan, D., J. Otterbach, and M. Fleischhauer, 2011, "Electromagnetically induced transparency with Rydberg atoms," Phys. Rev. Lett. 107, 213601.

Peyronel, T., O. Firstenberg, Q.-Y. Liang, S. Hofferberth, A. V. Gorshkov, T. Pohl, M. D. Lukin, and V. Vuletic, 2012, "Quantum nonlinear optics with single photons enabled by strongly interacting atoms," Nature (London) 488, 57-60.  
Phillips, J., 1996, "Self-adjoint Fredholm operators and spectral flow," Can. Math. Bull. 39, 460-467.  
Pilozzi, L., and C. Conti, 2016, "Topological lasing in resonant photonic structures," Phys. Rev. B 93, 195317.  
Pitaevskii, L. P., and S. Stringari, 2016, Bose Einstein condensation and superfluidity (Clarendon Press, Oxford).  
Plekhanov, K., G. Roux, and K. Le Hur, 2017, "Floquet engineering of Haldane Chern insulators and chiral bosonic phase transitions," Phys. Rev. B 95, 045102.  
Plotnik, Y., M. A. Bandres, S. Stützer, Y. Lumer, M. C. Rechtsman, A. Szameit, and M. Segev, 2016, "Analogue of Rashba pseudospin-orbit coupling in photonic lattices by gauge field engineering," Phys. Rev. B 94, 020301.  
Plotnik, Y., et al., 2014, "Observation of unconventional edge states in photonic graphene," Nat. Mater. 13, 57-62.  
Poddubny, A., A. Miroshnichenko, A. Slobozhanyuk, and Y. Kivshar, 2014, "Topological majorana states in zigzag chains of plasmonic nanoparticles," ACS Photonics 1, 101-105.  
Poli, C., M. Bellec, U. Kuhl, F. Mortessagne, and H. Schomerus, 2015, "Selective enhancement of topologically induced interface states in a dielectric resonator chain," Nat. Commun. 6, 6710.  
Polkovnikov, A., K. Sengupta, A. Silva, and M. Vengalattore, 2011, "Colloquium: Nonequilibrium dynamics of closed interacting quantum systems," Rev. Mod. Phys. 83, 863-883.  
Poo, Y., C. He, C. Xiao, M.-H. Lu, R.-X. Wu, and Y.-F. Chen, 2016, "Manipulating one-way space wave and its refraction by time-reversal and parity symmetry breaking," Sci. Rep. 6, 29380.  
Poo, Y., R.-x. Wu, Z. Lin, Y. Yang, and C. T. Chan, 2011, "Experimental realization of self-guiding unidirectional electromagnetic edge states," Phys. Rev. Lett. 106, 093903.  
Poo, Y., R.-x. Wu, S. Liu, Y. Yang, Z. Lin, and S. T. Chui, 2012, "Experimental demonstration of surface morphology independent electromagnetic chiral edge states originated from magnetic plasmon resonance," Appl. Phys. Lett. 101, 081912.  
Poshakinskiy, A. V., and A. N. Poddubny, 2017, "Phonoritonic crystals with a synthetic magnetic field for an acoustic diode," Phys. Rev. Lett. 118, 156801.  
Poshakinskiy, A. V., A. N. Poddubny, L. Pilozzi, and E. L. Ivchenko, 2014, "Radiative topological states in resonant photonic crystals," Phys. Rev. Lett. 112, 107403.  
Pothier, H., P. Lafarge, P. F. Orfila, C. Urbina, D. Esteve, and M. H. Devoret, 1991, "Single electron pump fabricated with ultrasmall normal tunnel junctions," Physica B (Amsterdam) 169, 573-574.  
Pothier, H., P. Lafarge, C. Urbina, D. Esteve, and M. H. Devoret, 1992, "Single-electron pump based on charging effects," Europhys. Lett. 17, 249.  
Prange, R. E., S. M. Girvin, M. E. Cage, K. Klitzing, A. M. Chang, F. Duncan, M. Haldane, R. B. Laughlin, A. M. M. Pruisken, and D. J. Thouless, 1989, The quantum Hall effect (Springer, New York).  
Price, H. M., 2018, “Four-dimensional topological lattices without gauge fields,” arXiv:1806.05263.  
Price, H. M., and N. R. Cooper, 2012, "Mapping the Berry curvature from semiclassical dynamics in optical lattices," Phys. Rev. A 85, 033620.  
Price, H. M., O. Zilberberg, T. Ozawa, I. Carusotto, and N. Goldman, 2015, "Four-dimensional quantum Hall effect with ultracold atoms," Phys. Rev. Lett. 115, 195303.

Price, H. M., T. Ozawa, and I. Carusotto, 2014, "Quantum mechanics with a momentum-space artificial magnetic field," Phys. Rev. Lett. 113, 190403.  
Price, H. M., T. Ozawa, and N. Goldman, 2017, "Synthetic dimensions for cold atoms from shaking a harmonic trap," Phys. Rev. A 95, 023607.  
Price, H. M., O. Zilberberg, T. Ozawa, I. Carusotto, and N. Goldman, 2016, "Measurement of Chern numbers through center-of-mass responses," Phys. Rev. B 93, 245113.  
Prodan, E., and H. Schulz-Baldes, 2016, "Bulk and boundary invariants for complex topological insulators" [https://www.springer.com/la/book/9783319293509].  
Qi, X.-L., T. L. Hughes, and S.-C. Zhang, 2008, “Topological field theory of time-reversal invariant insulators,” Phys. Rev. B 78, 195424.  
Qi, X.-L., Y.-S. Wu, and S.-C. Zhang, 2006, "General theorem relating the bulk topological number to edge states in two-dimensional insulators," Phys. Rev. B 74, 045125.  
Qi, X.-L., and S.-C. Zhang, 2011, "Topological insulators and superconductors," Rev. Mod. Phys. 83, 1057-1110.  
Qiu, P., R. Liang, W. Qiu, H. Chen, J. Ren, Z. Lin, J.-X. Wang, Q. Kan, and J.-Q. Pan, 2017, "Topologically protected edge states in graphene plasmonic crystals," Opt. Express 25, 22587-22594.  
Qiu, W., Z. Wang, and M. Soljacic, 2011, "Broadband circulators based on directional coupling of one-way waveguides," Opt. Express 19, 22248.  
Quelle, A., C. Weitenberg, K. Sengstock, and C. Morais Smith, 2017, "Driving protocol for a Floquet topological phase without static counterpart," New J. Phys. 19, 113010.  
Raghu, S., and F. D. M. Haldane, 2008, "Analogs of quantum-Halleffect edge states in photonic crystals," Phys. Rev. A 78, 033834.  
Rahav, S., I. Gilary, and S. Fishman, 2003, "Effective hamiltonians for periodically driven systems," Phys. Rev. A 68, 013820.  
Rasmussen, K. Ø., T. Cretegny, P. G. Kevrekidis, and N. Gronbech-Jensen, 2000, "Statistical mechanics of a discrete nonlinear system," Phys. Rev. Lett. 84, 3740.  
Rechtsman, M. C., Y. Lumer, Y. Plotnik, A. Perez-Leija, A. Szameit, and M. Segev, 2016, "Topological protection of photonic path entanglement," Optica 3, 925-930.  
Rechtsman, M. C., Y. Plotnik, J. M. Zeuner, D. Song, Z. Chen, A. Szameit, and M. Segev, 2013, "Topological creation and destruction of edge states in photonic graphene," Phys. Rev. Lett. 111, 103901.  
Rechtsman, M. C., J. M. Zeuner, Y. Plotnik, Y. Lumer, D. Podolsky, F. Dreisow, S. Nolte, M. Segev, and A. Szameit, 2013, "Photonic floquet topological insulators," Nature (London) 496, 196-200.  
Rechtsman, M. C., J. M. Zeuner, A. Tünnermann, S. Nolte, M. Segev, and Alexander Szameit, 2013, "Strain-induced pseudomagnetic field and photonic landau levels in dielectric structures," Nat. Photonics 7, 153-158.  
Reichl, M. D., and E. J. Mueller, 2014, "Floquet edge states with ultracold atoms," Phys. Rev. A 89, 063628.  
Reinhard, A., T. Volz, M. Winger, A. Badolato, K. J. Hennessy, E. L. Hu, and A. Imamoglu, 2012, "Strongly correlated photons on a chip," Nat. Photonics 6, 93-96.  
Resta, R., 1994, "Macroscopic polarization in crystalline dielectrics: the geometric phase approach," Rev. Mod. Phys. 66, 899-915.  
Resta, R., 2011, "The insulating state of matter: a geometrical theory," Eur. Phys. J. B 79, 121-137.  
Richard, M., J. Kasprzak, R. Romestain, R. Andre, and L. S. Dang, 2005, "Spontaneous coherent phase transition of polaritons in CdTe microcavities," Phys. Rev. Lett. 94, 187401.

Ringel, M., M. Pletyukhov, and V. Gritsev, 2014, "Topologically protected strongly correlated states of photons," New J. Phys. 16, 113030.  
Rodriguez-Fortuno, F. J., G. Marino, P. Ginzburg, D. O'Connor, A. Martínez, G. A. Wurtz, and A. V. Zayats, 2013, "Near-field interference for the unidirectional excitation of electromagnetic guided modes," Science 340, 328-330.  
Rosanov, N.N., 2002, Spatial hysteresis and optical patterns (Springer, New York).  
Rosenthal, E. I., N. K. Ehrlich, M. S. Rudner, A. P. Higginbotham, and K. W. Lehnert, 2018, "Topological phase transition measured in a dissipative metamaterial," Phys. Rev. B 97, 220301.  
Roushan, P., et al., 2017a, "Spectroscopic signatures of localization with interacting photons in superconducting qubits," Science 358, 1175-1179.  
Roushan, P., et al., 2017b, "Chiral ground-state currents of interacting photons in a synthetic magnetic field," Nat. Phys. 13, 146.  
Roy, D., C.M. Wilson, and O. Firstenberg, 2017, “Colloquium: Strongly interacting photons in one-dimensional continuum,” Rev. Mod. Phys. 89, 021001.  
Roy, R., 2009, "Topological phases and the quantum spin Hall effect in three dimensions," Phys. Rev. B 79, 195322.  
Roy, S., M. Kolodrubetz, N. Goldman, and A. G. Grushin, 2018, "Tunable axial gauge fields in engineered Weyl semimetals: Semiclassical analysis and optical lattice implementations," 2D Mater. 5, 024001.  
Rudner, M. S., and L. S. Levitov, 2009, "Topological transition in a non-Hermitian quantum walk," Phys. Rev. Lett. 102, 065703.  
Rudner, M. S., N. H. Lindner, E. Berg, and M. Levin, 2013, "Anomalous Edge States and the Bulk-Edge Correspondence for Periodically Driven Two-Dimensional Systems," Phys. Rev. X 3, 031005.  
Ruesink, F., M.-A. Miri, A. Alù, and E. Verhagen, 2016, “Nonreciprocity and magnetic-free isolation based on optomechanical interactions,” Nat. Commun. 7, 13662.  
Rüter, C. E., K. G. Makris, R. El-Ganainy, D. N. Christodoulides, M. Segev, and D. Kip, 2010, "Observation of parity-time symmetry in optics," Nat. Phys. 6, 192-195.  
Ryu, S., and Y. Hatsugai, 2002, "Topological origin of zero-energy edge states in particle-hole symmetric systems," Phys. Rev. Lett. 89, 077002.  
Ryu, S., A. P. Schnyder, A. Furusaki, and A. W. W. Ludwig, 2010, "Topological insulators and superconductors: Tenfold way and dimensional hierarchy," New J. Phys. 12, 065010.  
Saffman, M., T.G. Walker, and K. Mølmer, 2010, “Quantum information with rydberg atoms,” Rev. Mod. Phys. 82, 2313.  
Sala, V.G., et al., 2015, "Spin-orbit coupling for photons and polaritons in microstructures," Phys. Rev. X 5, 011034.  
Saleh, B. E. A., and M. C. Teich, 2007, Fundamentals of Photonics, Wiley Series in Pure and Applied Optics (Wiley, New York).  
Salerno, G., T. Ozawa, H. M. Price, and I. Carusotto, 2015, "How to directly observe Landau levels in driven-dissipative strained honeycomb lattices," 2D Mater. 2, 034015.  
Salerno, G., T. Ozawa, H. M. Price, and I. Carusotto, 2016, "Floquet topological system based on frequency-modulated classical coupled harmonic oscillators," Phys. Rev. B 93, 085105.  
Salerno, G., T. Ozawa, H.M. Price, and I. Carusotto, 2017, "Propagating edge states in strained honeycomb lattices," Phys. Rev. B 95, 245418.  
Sayrin, C., C. Junge, R. Mitsch, B. Albrecht, D. O'Shea, P. Schneeweiss, J. Volz, and A. Rauschenbeutel, 2015, "Nanophotonic optical isolator controlled by the internal state of cold atoms," Phys. Rev. X 5, 041036.

Schine, N., A. Ryou, A. Gromov, A. Sommer, and J. Simon, 2016, "Synthetic Landau levels for photons," Nature (London) 534, 671-675.  
Schmidt, M., S. Kessler, V. Peano, O. Painter, and F. Marquardt, 2015, "Optomechanical creation of magnetic fields for photons on a lattice," Optica 2, 635-641.  
Schnyder, A. P., S. Ryu, A. Furusaki, A. W. W Ludwig, V. Lebedev, and M. Feigelman, 2009, "Classification of topological insulators and superconductors," AIP Conf. Proc. 1134, 10-21.  
Schoelkopf, R.J., and S.M. Girvin, 2008, "Wiring up quantum systems," Nature (London) 451, 664-669.  
Schomerus, H., 2013, "Topologically protected midgap states in complex photonic lattices," Opt. Lett. 38, 1912-1914.  
Schomerus, H., and N. Y. Halpern, 2013, "Parity Anomaly and Landau-Level Lasing in Strained Photonic Honeycomb Lattices," Phys. Rev. Lett. 110, 013903.  
Schreiber, A., A. Gábris, P. P. Rohde, K. Laiho, M. Štefanák, V. Potoček, C. Hamilton, I. Jex, and C. Silberhorn, 2012, “A 2D quantum walk simulation of two-particle dynamics,” Science 336, 55–58.  
Schwartz, A., and B. Fischer, 2013, "Laser mode hyper-combs," Opt. Express 21, 6196-6204.  
Schwartz, T., G. Bartal, S. Fishman, and M. Segev, 2007, "Transport and anderson localization in disordered two-dimensional photonic lattices," Nature (London) 446, 52-55.  
Seclí, M., 2017, "Edge State Lasing in a 2D Topological Photonic System," Master's thesis (University of Trento).  
Segev, M., B. Crosignani, A. Yariv, and B. Fischer, 1992, "Spatial solitons in photorefractive media," Phys. Rev. Lett. 68, 923.  
Serdyukov, A., I. Semchenko, S. Tertyakov, and A. Sihvola, 2001, Electromagnetics of bi-anisotropic materials-Theory and Application, Vol. 11 (Gordon and Breach Science Publishers, New York).  
Shelby, R. A., D. R. Smith, and S. Schultz, 2001, "Experimental verification of a negative index of refraction," Science 292, 77-79.  
Shen, H., B. Zhen, and L. Fu, 2018, "Topological band theory for non-Hermitian Hamiltonians," Phys. Rev. Lett. 120, 146402.  
Shen, L., Y. You, Z. Wang, and X. Deng, 2015, "Backscattering-immune one-way surface magnetoplasmons at terahertz frequencies," Opt. Express 23, 950-962.  
Shen, Z., Y.-L. Zhang, Y. Chen, C.-L. Zou, Y.-F. Xiao, X.-B. Zou, F.-W. Sun, G.-C. Guo, and C.-H. Dong, 2016, "Experimental realization of optomechanically induced non-reciprocity," Nat. Photonics 10, 657-661.  
Sheng, D. N., Z. Y. Weng, L. Sheng, and F. D. M. Haldane, 2006, "Quantum spin-Hall effect and topologically invariant Chern numbers," Phys. Rev. Lett. 97, 036808.  
Shi, T., H. J. Kimble, and J. I. Cirac, 2017, "Topological phenomena in classical optical networks," Proc. Natl. Acad. Sci. U.S.A. 114, E8967-E8976.  
Shi, Y., Z. Yu, and S. Fan, 2015, "Limitations of nonlinear optical isolators due to dynamic reciprocity," Nat. Photonics 9, 388-392.  
Shindou, R., R. Matsumoto, S. Murakami, and J.-i. Ohe, 2013, "Topological chiral magnonic edge mode in a magnonic crystal," Phys. Rev. B 87, 174427.  
Shindou, R., and J.-i. Ohe, 2014, "Magnetostatic wave analog of integer quantum Hall state in patterned magnetic films," Phys. Rev. B 89, 054412.  
Shindou, R., J.-i. Ohe, R. Matsumoto, S. Murakami, and E. Saitoh, 2013, "Chiral spin-wave edge modes in dipolar magnetic thin films," Phys. Rev. B 87, 174402.  
Siegman, A. E., 1986, Lasers (University Science Books, Sausalito, CA).

Silberberg, Y., Y. Lahini, Y. Bromberg, E. Small, and R. Morandotti, 2009, "Universal correlations in a nonlinear periodic 1D system," Phys. Rev. Lett. 102, 233904.  
Silveirinha, M. G., 2015, "Chern invariants for continuous media," Phys. Rev. B 92, 125153.  
Silveirinha, M. G., 2016a, "Bulk-edge correspondence for topological photonic continua," Phys. Rev. B 94, 205105.  
Silveirinha, M. G., 2016b, “ $Z_{2}$  topological index for continuous photonic materials,” Phys. Rev. B 93, 075110.  
Simon, B., 1983, “Holonomy, the quantum adiabatic theorem, and Berry's phase,” Phys. Rev. Lett. 51, 2167-2170.  
Sinev, I. S., I. S. Mukhin, A. P. Slobozhanyuk, A. N. Poddubny, A. E. Miroshnichenko, A. K. Samusev, and Y. S. Kivshar, 2015, "Mapping plasmonic topological states at the nanoscale," Nanoscale 7, 11904-11908.  
Siroki, G., P.A. Huidobro, and V. Giannini, 2017, "Topological photonics: From crystals to particles," Phys. Rev. B 96, 041408.  
Skirlo, S. A., L. Lu, Y. Igarashi, Q. Yan, J. Joannopoulos, and M. Soljacic, 2015, "Experimental observation of large Chern numbers in photonic crystals," Phys. Rev. Lett. 115, 253901.  
Skirlo, S. A., L. Lu, and M. Soljacic, 2014, "Multimode one-way waveguides of large Chern numbers," Phys. Rev. Lett. 113, 113904.  
Slobozhanyuk, A., S. H. Mousavi, X. Ni, D. Smirnova, Y. S. Kivshar, and A. B. Khanikaev, 2017, "Three-dimensional all-dielectric photonic topological insulator," Nat. Photonics 11, 130-136.  
Slobozhanyuk, A., A. V. Shchelokova, X. Ni, S. H. Mousavi, D. A. Smirnova, P. A. Belov, A. Alù, Y. S. Kivshar, and A. B. Khanikaev, 2019, “Near-field imaging of spin-locked edge states in all-dielectric topological metasurfaces,” Appl. Phys. Lett. 114, 031103.  
Slobozhanyuk, A. P., A. B. Khanikaev, D. S. Filonov, D. A. Smirnova, A. E. Miroshnichenko, and Y. S. Kivshar, 2016, "Experimental demonstration of topological effects in bianisotropic metamaterials," Sci. Rep. 6, 22270.  
Slobozhanyuk, A. P., A. N. Poddubny, A. E. Miroshnichenko, P. A. Belov, and Y. S. Kivshar, 2015, "Subwavelength topological edge states in optically resonant dielectric structures," Phys. Rev. Lett. 114, 123901.  
Slobozhanyuk, A. P., A. N. Poddubny, I. S. Sinev, A. K. Samusev, Y. F. Yu, A. I. Kuznetsov, A. E. Miroshnichenko, and Y. S. Kivshar, 2016, "Enhanced photonic spin Hall effect with subwavelength topological edge states," Laser Photonics Rev. 10, 656-664.  
Sollner, I., et al., 2015, "Deterministic photon-emitter coupling in chiral photonic circuits," Nat. Nanotechnol. 10, 775-778.  
Solnyshkov, D. D., O. Bleu, and G. Malpuech, 2018, "Topological optical isolator based on polariton graphene," Appl. Phys. Lett. 112, 031106.  
Solnyshkov, D. D., A. V. Nalitov, and G. Malpuech, 2016, "Kibble-zurek mechanism in topologically nontrivial zigzag chains of polariton micropillars," Phys. Rev. Lett. 116, 046402.  
Solnyshkov, D., A. Nalitov, B. Teklu, L. Franck, and G. Malpuech, 2016, "Spin-dependent Klein tunneling in polariton graphene with photonic spin-orbit interaction," Phys. Rev. B 93, 085404.  
Soluyanov, A. A., D. Gresch, Z. Wang, Q. Wu, M. Troyer, X. Dai, and B. A. Bernevig, 2015, "Type-II Weyl semimetals," Nature (London) 527, 495-498.  
Sommer, A., H. P. Buchler, and J. Simon, 2015, "Quantum Crystals and Laughlin Droplets of Cavity Rydberg Polaritons," arXiv:1506.00341.  
Sommer, A., and J. Simon, 2016, "Engineering photonic Floquet Hamiltonians through Fabry-Pérot resonators," New J. Phys. 18, 035008.

Song, D., V. Paltoglou, S. Liu, Y. Zhu, D. Gallardo, L. Tang, J. Xu, M. Ablowitz, N. K. Efremidis, and Z. Chen, 2015, "Unveiling pseudospin and angular momentum in photonic graphene," Nat. Commun. 6, 6272.  
Spivak, B., F. Zhou, and M. T. Beal Monod, 1995, "Mesoscopic mechanisms of the photovoltaic effect and microwave absorption in granular metals," Phys. Rev. B 51, 13226-13230.  
Stannigel, K., P. Komar, S. J. M. Habraken, S. D. Bennett, M. D. Lukin, P. Zoller, and P. Rabl, 2012, "Optomechanical quantum information processing with photons and phonons," Phys. Rev. Lett. 109, 013603.  
St-Jean, P., V. Goblot, E. Galopin, A. Lemaitre, T. Ozawa, L. Le Gratiet, I. Sagnes, J. Bloch, and A. Amo, 2017, "Lasing in topological edge states of a one-dimensional lattice," Nat. Photonics 11, 651.  
Störmer, H. L., J. P. Eisenstein, A. C. Gossard, W. Wiegmann, and K. Baldwin, 1986, "Quantization of the Hall effect in an anisotropic three-dimensional electronic system," Phys. Rev. Lett. 56, 85.  
Stuhl, B. K., H.-I. Lu, L. M. Aycock, D. Genkina, and I. B. Spielman, 2015, "Visualizing edge states with an atomicbose gas in the quantum Hall regime," Science 349, 1514-1518.  
Stützer, S., Y. Plotnik, Y. Lumer, P. Titum, N. H. Lindner, M. Segev, M. C. Rechtsman, and A. Szameit, 2018, "Photonic topological Anderson insulators," Nature (London) 560, 461.  
Su, W.P., J.R. Schrieffer, and A.J. Heeger, 1979, “Solitons in polyacetylene,” Phys. Rev. Lett. 42, 1698-1701.  
Sugawa, S., F. Salces-Carcoba, A.R. Perry, Y. Yue, and I.B. Spielman, 2018, "Second Chern number of a quantum-simulated non-Abelian Yang monopole," Science 360, 1429-1434.  
Sun, B. Y., X. W. Luo, M. Gong, G. C. Guo, and Z. W. Zhou, 2017, "Weyl semimetal phases and implementation in degenerate optical cavities," Phys. Rev. A 96, 013857.  
Sun, X.-C., C. He, X.-P. Liu, M.-H. Lu, S.-N. Zhu, and Y.-F. Chen, 2017, “Two-dimensional topological photonic systems,” Prog. Quantum Electron. 55, 52-73.  
Sun, Y., D. Leykam, S. Nenni, D. Song, H. Chen, Y. D. Chong, and Z. Chen, 2018, "Observation of valley Landau-Zener-Bloch oscillations and pseudospin imbalance in photonic graphene," Phys. Rev. Lett. 121, 033904.  
Suszalski, D., and J. Zakrzewski, 2016, "Different lattice geometries with a synthetic dimension," Phys. Rev. A 94, 033602.  
Swtkes, M., C. M. Marcus, K. Campman, and A. C. Gossard, 1999, "An adiabatic quantum electron pump," Science 283, 1905-1908.  
Szameit, A., F. Dreisow, T. Pertsch, S. Nolte, and A. Tünnermann, 2007, "Control of directional evanescent coupling in fs laser written waveguides," Opt. Express 15, 1579-1587.  
Szameit, A., and S. Nolte, 2010, "Discrete optics in femtosecond-laser-written photonic structures," J. Phys. B 43, 163001.  
Szameit, A., M.C. Rechtsman, O. Bahat-Treidel, and M. Segev, 2011, "P T-symmetry in honeycomb photonic lattices," Phys. Rev. A 84, 021806.  
Taddia, L., E. Cornfeld, D. Rossini, L. Mazza, E. Sela, and R. Fazio, 2017, "Topological fractional pumping with alkaline-earth-like atoms in synthetic lattices," Phys. Rev. Lett. 118, 230402.  
Tai, M. E., A. Lukin, M. Rispoli, R. Schittko, T. Menke, D. Borgnia, P. M. Preiss, F. Grusdt, A. M. Kaufman, and M. Greiner, 2017, "Microscopy of the interacting Harper-Hofstadter model in the two-body limit," Nature (London) 546, 519.  
Takemura, N., S. Trebaol, M. Wouters, M. T. Portella-Oberli, and B. Deveaud, 2014, "Polaritonic Feshbach resonance," Nat. Phys. 10, 500-504.

Tan, W., Y. Sun, H. Chen, and S.-Q. Shen, 2014, "Photonic simulation of topological excitations in metamaterials," Sci. Rep. 4, 3842.  
Tanese, D., et al., 2013, "Polariton condensation in solitonic gap states in a one-dimensional periodic potential," Nat. Commun. 4, 1749.  
Tangpanitanon, J., V.M. Bastidas, S. Al-Assam, P. Roushan, D. Jaksch, and D.G. Angelakis, 2016, "Topological pumping of photons in nonlinear resonator arrays," Phys. Rev. Lett. 117, 213603.  
Tarasinski, B., J. K. Asbóth, and J. P. Dahlhaus, 2014, "Scattering theory of topological phases in discrete-time quantum walks," Phys. Rev. A 89, 042327.  
Tarruell, L., D. Greif, T. Uehlinger, G. Jotzu, and T. Esslinger, 2012, "Creating, moving and merging Dirac points with a Fermi gas in a tunable honeycomb lattice," Nature (London) 483, 302-305.  
Teo, J. C. Y., and C. L. Kane, 2010, "Topological defects and gapless modes in insulators and superconductors," Phys. Rev. B 82, 115120.  
Thouless, D. J., 1983, "Quantization of particle transport," Phys. Rev. B 27, 6083-6087.  
Thouless, D. J., M. Kohmoto, M. P. Nightingale, and M. den Nijs, 1982, "Quantized Hall conductance in a two-dimensional periodic potential," Phys. Rev. Lett. 49, 405-408.  
Tomita, A., and R. Y. Chiao, 1986, "Observation of Berry's topological phase by use of an optical fiber," Phys. Rev. Lett. 57, 937-940.  
Tomka, M., M. Pletyukhov, and V. Gritsev, 2015, "Supersymmetry in quantum optics and in spin-orbit coupled systems," Sci. Rep. 5, 13097.  
Tong, D., 2016, "Lectures on the quantum Hall effect," arXiv:1606.06687.  
Tsomokos, D. I., S. Ashhab, and F. Nori, 2010, "Using superconducting qubit circuits to engineer exotic lattice systems," Phys. Rev. A 82, 052311.  
Tsui, D.C., H.L. Stormer, and A.C. Gossard, 1982, "Two-dimensional magnetotransport in the extreme quantum limit," Phys. Rev. Lett. 48, 1559-1562.  
Tureci, H. E., A. D. Stone, and L. Ge, 2007, “Theory of the spatial structure of nonlinear lasing modes,” Phys. Rev. A 76, 013813.  
Umucalilar, R. O., and I. Carusotto, 2017, "Generation and spectroscopic signatures of a fractional quantum Hall liquid of photons in an incoherently pumped optical cavity," Phys. Rev. A 96, 053808.  
Umucalilar, R. O., and I. Carusotto, 2011, "Artificial gauge field for photons in coupled cavity arrays," Phys. Rev. A 84, 043804.  
Umucalilar, R. O., and I. Carusotto, 2012, "Fractional quantum Hall states of photons in an array of dissipative coupled cavities," Phys. Rev. Lett. 108, 206809.  
Umucalilar, R. O., and I. Carusotto, 2013, “Many-body braiding phases in a rotating strongly correlated photon gas,” Phys. Lett. A 377, 2074–2078.  
Van Mechelen, T., and Z. Jacob, 2016, "Universal spin-momentum locking of evanescent waves," Optica 3, 118-126.  
Verbin, M., O. Zilberberg, Y.E. Kraus, Y. Lahini, and Y. Silberberg, 2013, "Observation of topological phase transitions in photonic quasicrystals," Phys. Rev. Lett. 110, 076403.  
Verbin, M., O. Zilberberg, Y. Lahini, Y. E. Kraus, and Y. Silberberg, 2015, "Topological pumping over a photonic Fibonacci quasicrystal," Phys. Rev. B 91, 064201.  
Vignolo, P., M. Bellec, J. Böhm, A. Camara, J.-M. Gambaudo, U. Kuhl, and F. Mortessagne, 2016, "Energy landscape in a Penrosetiling," Phys. Rev. B 93, 075141.

Vocke, D., T. Roger, F. Marino, E.M. Wright, I. Carusotto, M. Clerici, and D. Faccio, 2015, "Experimental characterization of nonlocal photon fluids," Optica 2, 484-490.  
Volovik, G.E., 2009, The Universe in a Helium Droplet (Oxford University Press, New York).  
von Klitzing, K., 1986, “The quantized Hall effect,” Rev. Mod. Phys. 58, 519-531.  
Wallace, P. R., 1947, “The band theory of graphite,” Phys. Rev. 71, 622-634.  
Walls, D.F., and G. Milburn, 2006, Quantum Optics (Springer-Verlag, Berlin).  
Wan, X., A.M. Turner, A. Vishwanath, and S.Y. Savrasov, 2011, "Topological semimetal and Fermi-arc surface states in the electronic structure of pyrochlore iridates," Phys. Rev. B 83, 205101.  
Wang, D., C. Qiu, P. T. Rakich, and Z. Wang, 2015, "Guide-wave photonic pulling force using one-way photonic chiral edge states," in CLEO: QELS_Fundamental Science (Optical Society of America), pp. FM2D-7.  
Wang, H., L. Xu, H. Y. Chen, and J.-H. Jiang, 2016, "Three-dimensional photonic Dirac points stabilized by point group symmetry," Phys. Rev. B 93, 235155.  
Wang, H., L. Zhou, and Y. D. Chong, 2016, "Floquet Weyl phases in a three-dimensional network model," Phys. Rev. B 93, 144114.  
Wang, H.-X., Y. Chen, Z. H. Hang, H.-Y. Kee, and J.-H. Jiang, 2017, "Type-II Dirac photons," npj Quantum Mater. 2, 54.  
Wang, L., S.-K. Jian, and H. Yao, 2016, "Topological photonic crystal with equiprequency Weyl points," Phys. Rev. A 93, 061801.  
Wang, Q., M. Xiao, H.Liu, S. Zhu, and C.T. Chan, 2017, "Optical interface states protected by synthetic Weyl points," Phys. Rev. X 7, 031032.  
Wang, Y.-P., W. Wang, Z.-Y. Xue, W.-L. Yang, Y. Hu, and Y. Wu, 2015, "Realizing and characterizing chiral photon flow in a circuit quantum electrodynamics necklace," Sci. Rep. 5, 8352.  
Wang, Y.-P., W.-L. Yang, Y. Hu, Z.-Y. Xue, and Y. Wu, 2016, "Detecting topological phases of microwave photons in a circuit quantum electrodynamics lattice," npj Quantum Inf. 2, 16015.  
Wang, Z., Y. D. Chong, J. D. Joannopoulos, and M. Soljacic, 2008, "Reflection-free one-way edge modes in a gyromagnetic photonic crystal," Phys. Rev. Lett. 100, 013905.  
Wang, Z., Y. Chong, J. D. Joannopoulos, and M. Soljačić, 2009, "Observation of unidirectional backscattering-immune topological electromagnetic states," Nature (London) 461, 772-775.  
Wang, Z., L. Shen, Z. Yu, X. Zhang, and X. Zheng, 2013, "Highly efficient photonic-crystal splitters based on one-way waveguiding," J. Opt. Soc. Am. B 30, 173-176.  
Wang, Z., L. Shen, X. Zhang, Y. Wang, Z. Yu, and X. Zheng, 2011, "Photonic crystal cavity with one-way rotating state and its coupling with photonic crystal waveguide," J. Appl. Phys. 110, 043106.  
Watanabe, H., and L. Lu, 2018, "Space Group Theory of Photonic Bands," Phys. Rev. Lett. 121, 263903.  
Waterstraat, N., 2016, "Fredholm operators and spectral flow," arXiv:1603.02009.  
Weimann, S., M. Kremer, Y. Plotnik, Y. Lumer, S. Nolte, K.G. Makris, M. Segev, M.C. Rechtsman, and A. Szameit, 2017, "Topologically protected bound states in photonic parity-timesymmetric crystals," Nat. Mater. 16, 433-438.  
Wen, X.G., and A. Zee, 1992, "Shift and spin vector: New topological quantum numbers for the Hall fluids," Phys. Rev. Lett. 69, 953.  
Wertz, E., et al., 2010, "Spontaneous formation and optical manipulation of extended polariton condensates," Nat. Phys. 6, 860-864.

Wimmer, M., H. M. Price, I. Carusotto, and U. Peschel, 2017, "Experimental measurement of the Berry curvature from anomalous transport," Nat. Phys. 13, 545-550.  
Wouters, M., 2007, "Resonant polariton-polariton scattering in semiconductor microcavities," Phys. Rev. B 76, 045319.  
Wouters, M., I. Carusotto, and C. Ciuti, 2008, "Spatial and spectral shape of inhomogeneous nonequilibrium exciton-polariton condensates," Phys. Rev. B 77, 115340.  
Wu, C., D. Bergman, L. Balents, and S. Das Sarma, 2007, "Flat Bands and Wigner Crystallization in the Honeycomb Optical Lattice," Phys. Rev. Lett. 99, 070401.  
Wu, L.-H., and X. Hu, 2015, "Scheme for achieving a topological photonic crystal by using dielectric material," Phys. Rev. Lett. 114, 223901.  
Wu, X., Y. Meng, J. Tian, Y. Huang, H. Xiang, D. Han, and W. Wen, 2017, "Direct observation of valley-polarized topological edge states in designer surface plasmon crystals," Nat. Commun. 8, 1304.  
Wu, Y., C. Li, X. Hu, Y. Ao, Y. Zhao, and Q. Gong, 2017, "Applications of topological photonics in integrated photonic devices," Adv. Opt. Mater. 5, 1700357.  
Xia, B.-Z., T.-T. Liu, G.-L. Huang, H.-Q. Dai, J.-R. Jiao, X.-G. Zang, D.-J. Yu, S.-J. Zheng, and J. Liu, 2017, "Topological phononic insulator with robust pseudospin-dependent transport," Phys. Rev. B 96, 094106.  
Xiao, B., K. Lai, Y. Yu, T. Ma, G. Shvets, and S. M. Anlage, 2016, "Exciting reflectionless unidirectional edge modes in a reciprocal photonic topological insulator medium," Phys. Rev. B 94, 195427.  
Xiao, D., M.-C. Chang, and Q. Niu, 2010, "Berry phase effects on electronic properties," Rev. Mod. Phys. 82, 1959-2007.  
Xiao, L., et al., 2017, "Observation of topological edge states in parity-time-symmetric quantum walks," Nat. Phys. 13, 1117.  
Xiao, M., and S. Fan, 2017a, "Photonic Chern insulator through homogenization of an array of particles," Phys. Rev. B 96, 100202.  
Xiao, M., and S. Fan, 2017b, "Topologically charged nodal surface," arXiv:1709.02363.  
Xiao, M., Q. Lin, and S. Fan, 2016, "Hyperbolic Weyl point in reciprocal chiral metamaterials," Phys. Rev. Lett. 117, 057401.  
Xiao, M., Z. Q. Zhang, and C. T. Chan, 2014, "Surface impedance and bulk band geometric phases in one-dimensional systems," Phys. Rev. X 4, 021017.  
Xu, G., H. Weng, Z. Wang, X. Dai, and Z. Fang, 2011, "Chern Semimetal and the Quantized Anomalous Hall Effect in  $\mathrm{HgCr_2Se_4}$ ," Phys. Rev. Lett. 107, 186806.  
Xu, L., H.-X. Wang, Y.-D. Xu, H.-Y. Chen, and J.-H. Jiang, 2016, "Accidental degeneracy in photonic bands and topological phase transitions in two-dimensional core-shell dielectric photonic crystals," Opt. Express 24, 18059.  
Xu, Y., S.-T. Wang, and L.-M. Duan, 2017, "Weyl exceptional rings in a three-dimensional dissipative cold atomic gas," Phys. Rev. Lett. 118, 045701.  
Yablonovitch, E., 1987, "Inhibited spontaneous emission in solid-state physics and electronics," Phys. Rev. Lett. 58, 2059-2062.  
Yan, Q., R. Liu, Z. Yan, B. Liu, H. Chen, Z. Wang, and L. Lu, 2018, "Experimental discovery of nodal chains," Nat. Phys. 14, 461.  
Yan, Z., R. Bi, H. Shen, L. Lu, S.-C. Zhang, and Z. Wang, 2017, "Nodal-link semimetals," Phys. Rev. B 96, 041103.  
Yang, B., et al., 2017, "Direct observation of topological surface-state arcs in photonic metamaterials," Nat. Commun. 8, 97.  
Yang, B., et al., 2018, "Ideal Weyl points and helicoid surface states in artificial photonic crystal structures," Science 359, 1013-1016.

Yang, B., T. Wu, and X. Zhang, 2017a, "Engineering topological edge states in two dimensional magnetic photonic crystal," Appl. Phys. Lett. 110, 021109.  
Yang, B., T. Wu, and X. Zhang, 2017b, "Topological properties of nearly flat bands in two-dimensional photonic crystals," J. Opt. Soc. Am. B 34, 831-836.  
Yang, W. L., Z.-q. Yin, Z. X. Chen, S.-P. Kou, M. Feng, and C. H. Oh, 2012, "Quantum simulation of an artificial abelian gauge field using nitrogen-vacancy-center ensembles coupled to superconducting resonators," Phys. Rev. A 86, 012307.  
Yang, Y., Z. Gao, H. Xue, L. Zhang, M. He, Z. Yang, R. Singh, Y. Chong, B. Zhang, and H. Chen, 2019, "Realization of a three-dimensional photonic topological insulator," Nature (London) 565, 622-626.  
Yang, Y., Y. Poo, R.-x. Wu, Y. Gu, and P. Chen, 2013, "Experimental demonstration of one-way slow wave in waveguide involving gyromagnetic photonic crystals," Appl. Phys. Lett. 102, 231113.  
Yang, Y., Y.F. Xu, T. Xu, H.-X. Wang, J.-H. Jiang, X. Hu, and Z. Hang, 2018, "Visualization of a Unidirectional Electromagnetic Waveguide Using Topological Photonic Crystals Made of Dielectric Materials," Phys. Rev. Lett. 120, 217401.  
Yang, Z., M. Xiao, F. Gao, L. Lu, Y. Chong, and B. Zhang, 2017, "Weyl points in a magnetic tetrahedral photonic crystal," Opt. Express 25, 15772-15777.  
Yannopapas, V., 2011, "Gapless surface states in a lattice of coupled cavities: a photonic analog of topological crystalline insulators," Phys. Rev. B 84, 195126.  
Yannopapas, V., 2014, "Dirac points, topological edge modes and nonreciprocal transmission in one-dimensional metamaterial-based coupled-cavity arrays," Int. J. Mod. Phys. B 28, 1441006.  
Yao, S., F. Song, and Z. Wang, 2018, "Non-Hermitian Chern bands and Chern numbers," Phys. Rev. Lett. 121, 136802.  
Yao, S., and Z. Wang, 2018, "Edge states and topological invariants of non-Hermitian systems," Phys. Rev. Lett. 121, 086803.  
Yao, S., Z. Yan, and Z. Wang, 2017, "Topological invariants of Floquet systems: General formulation, special properties, and Floquet topological defects," Phys. Rev. B 96, 195303.  
Yariv, A., 1976, Introduction to optical electronics (Holt, Rinehart and Winston, Inc., New York, NY).  
Yariv, A., Y. Xu, R.K. Lee, and A. Scherer, 1999, "Coupled-resonator optical waveguide: a proposal and analysis," Opt. Lett. 24, 711-713.  
Yi, K., and T. Karzig, 2016, "Topological polaritons from photonic Dirac cones coupled to excitons in a magnetic field," Phys. Rev. B 93, 104303.  
Yin, C., H. Jiang, L. Li, R. Liu, and S. Chen, 2018, "Geometrical meaning of winding number and its characterization of topological phases in one-dimensional chiral non-Hermitian systems," Phys. Rev. A 97, 052115.  
Yoshida, T., R. Peters, and N. Kawakami, 2018, "Non-Hermitian perspective of the band structure in heavy-fermion systems," Phys. Rev. B 98, 035141.  
Yoshioka, D., 2002, The quantum Hall effect (Springer, New York). You, J. Q., and F. Nori, 2011, "Atomic physics and quantum optics using superconducting circuits," Nature (London) 474, 589-597.  
Yu, Z., Z. Wang, L. Shen, and X. Deng, 2014, "One-way electromagnetic mode at the surface of a magnetized gyromagnetic medium," Electron. Mater. Lett. 10, 969-973.  
Yu, Z., and S. Fan, 2009, "Complete optical isolation created by indirect interband photonic transitions," Nat. Photonics 3, 91-94.  
Yu, Z., G. Veronis, Z. Wang, and S. Fan, 2008, "One-way electromagnetic waveguide formed at the interface between a

plasmonic metal under a static magnetic field and a photonic crystal," Phys. Rev. Lett. 100, 023902.  
Yuan, L., and S. Fan, 2015a, "Three-dimensional dynamic localization of light from a time-dependent effective gauge field for photons," Phys. Rev. Lett. 114, 243901.  
Yuan, L., and S. Fan, 2015b, "Topologically nontrivial Floquet band structure in a system undergoing photonic transitions in the ultrastrong-coupling regime," Phys. Rev. A 92, 053822.  
Yuan, L., and S. Fan, 2016, "Bloch oscillation and unidirectional translation of frequency in a dynamically modulated ring resonator," Optica 3, 1014-1018.  
Yuan, L., Y. Shi, and S. Fan, 2016, "Photonic gauge potential in a system with a synthetic frequency dimension," Opt. Lett. 41, 741-744.  
Yuan, L., D.-w. Wang, and S. Fan, 2017, "Synthetic gauge potential and effective magnetic field in a Raman medium undergoing molecular modulation," Phys. Rev. A 95, 033801.  
Yuan, L., M. Xiao, and S. Fan, 2016, "Time reversal of a wave packet with temporal modulation of gauge potential," Phys. Rev. B 94, 140303.  
Yuan, L., M. Xiao, Q. Lin, and S. Fan, 2018, "Synthetic space with arbitrary dimensions in a few rings undergoing dynamic modulation," Phys. Rev. B 97, 104105.  
Yves, S., R. Fleury, T. Berthelot, M. Fink, F. Lemoult, and G. Lerosey, 2017, "Crystalline metamaterials for topological properties at subwavelength scales," Nat. Commun. 8, 16023.  
Yves, S., R. Fleury, F. Lemoult, M. Fink, and G. Lerosey, 2017, "Topological acoustic polaritons: robust sound manipulation at the subwavelength scale," New J. Phys. 19, 075003.  
Zak, J., 1964, "Magnetic translation group," Phys. Rev. 134, A1602-A1606.  
Zak, J., 1989, "Berry's phase for energy bands in solids," Phys. Rev. Lett. 62, 2747-2750.  
Zang, X., and C. Jiang, 2011, "Edge mode in nonreciprocal photonic crystal waveguide: manipulating the unidirectional electromagnetic pulse dynamically," J. Opt. Soc. Am. B 28, 554-557.  
Zeng, T.-S., C. Wang, and H. Zhai, 2015, "Charge pumping of interacting fermion atoms in the synthetic dimension," Phys. Rev. Lett. 115, 095302.  
Zeuner, J. M., M. C. Rechtsman, Y. Plotnik, Y. Lumer, S. Nolte, M. S. Rudner, M. Segev, and A. Szameit, 2015, "Observation of a topological transition in the bulk of a non-Hermitian system," Phys. Rev. Lett. 115, 040402.  
Zhang, F., J. Jung, G. A. Fiete, Q. Niu, and A. H. MacDonald, 2011, "Spontaneous Quantum Hall States in Chirally Stacked Few-Layer Graphene Systems," Phys. Rev. Lett. 106, 156801.  
Zhang, L., D. Yang, K. Chen, T. Li, and S. Xia, 2013, "Design of nonreciprocal waveguide devices based on two-dimensional magneto-optical photonic crystals," Opt. Laser Technol. 50, 195-201.

Zhang, S.-C., and J. Hu, 2001, "A four-dimensional generalization of the quantum Hall effect," Science 294, 823-828.  
Zhang, T., Z. Song, A. Alexandradinata, H. Weng, C. Fang, L. Lu, and Z. Fang, 2018, "Double-Weyl phonons in transition-metal monosilicides," Phys. Rev. Lett. 120, 016401.  
Zhang, X., W. Li, and X. Jiang, 2012, "Confined one-way mode at magnetic domain wall for broadband high-efficiency one-way waveguide, splitter and bender," Appl. Phys. Lett. 100, 041108.  
Zhang, Z., F. Li, G. Malpuech, Y. Zhang, O. Bleu, S. Koniakhin, C. Li, Y. Zhang, M. Xiao, and D. Solnyshkov, 2018, "Particle-like behavior of topological defects in linear wave packets in photonic graphene," arXiv:1806.05540.  
Zhao, H., P. Miao, M. H. Teimourpour, S. Malzard, R. El-Ganainy, H. Schomerus, and L. Feng, 2018, "Topological hybrid silicon microlasers," Nat. Commun. 9, 981.  
Zhen, B., C. W. Hsu, Y. Igarashi, L. Lu, I. Kaminer, A. Pick, S.-L. Chua, J. D. Joannopoulos, and M. Soljačić, 2015, "Spawning rings of exceptional points out of Dirac cones," Nature (London) 525, 354-358.  
Zheng, W., and H. Zhai, 2014, “Floquet topological states in shaking optical lattices,” Phys. Rev. A 89, 061603.  
Zhou, F., B. Spivak, and B. Altshuler, 1999, "Mesoscopic mechanism of adiabatic charge transport," Phys. Rev. Lett. 82, 608-611.  
Zhou, H., C. Peng, Y. Yoon, C. W. Hsu, K. A. Nelson, L. Fu, J. D. Joannopoulos, M. Soljacic, and B. Zhen, 2018, "Observation of bulk Fermi arc and polarization half charge from paired exceptional points," Science 359, 1009-1012.  
Zhou, M., L.Ying, L. Lu, L. Shi, J. Zi, and Z. Yu, 2017, "Electromagnetic scattering laws in Weyl systems," Nat. Commun. 8, 1388.  
Zhou, X.-F., X.-W. Luo, S. Wang, G.-C. Guo, X. Zhou, H. Pu, and Z.-W. Zhou, 2017, "Dynamically manipulating topological physics and edge modes in a single degenerate optical cavity," Phys. Rev. Lett. 118, 083603.  
Zhou, X., Y. Wang, D. Leykam, and Y.D. Chong, 2017, "Optical isolation with nonlinear topological photonics," New J. Phys. 19, 095002.  
Zhu, B., H. Zhong, Y. Ke, X. Qin, A. A. Sukhorukov, Y. S. Kivshar, and C. Lee, 2018, "Topological Floquet edge states in periodically curved waveguides," Phys. Rev. A 98, 013855.  
Zhu, H., and C. Jiang, 2011, "Extraordinary coupling into one-way magneto-optical photonic crystal waveguide," J. Lightwave Technol. 29, 708-713.  
Zhu, X., H.-X. Wang, C. Xu, Y. Lai, J.-H. Jiang, and S. John, 2018, "Topological transitions in continuously deformed photonic crystals," Phys. Rev. B 97, 085148.  
Zilberberg, O., S. Huang, J. Guglielmon, M. Wang, K. P. Chen, Y. E. Kraus, and M. C. Rechtsman, 2018, "Photonic topological boundary pumping as a probe of 4D quantum Hall physics," Nature (London) 553, 59.