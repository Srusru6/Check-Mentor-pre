# Colloquium: Topological insulators

M. Z. Hasan*

Joseph Henry Laboratories, Department of Physics, Princeton University, Princeton, New Jersey 08544, USA

C. L. Kane†

Department of Physics and Astronomy, University of Pennsylvania, Philadelphia, Pennsylvania 19104, USA

(Published 8 November 2010)

Topological insulators are electronic materials that have a bulk band gap like an ordinary insulator but have protected conducting states on their edge or surface. These states are possible due to the combination of spin-orbit interactions and time-reversal symmetry. The two-dimensional (2D) topological insulator is a quantum spin Hall insulator, which is a close cousin of the integer quantum Hall state. A three-dimensional (3D) topological insulator supports novel spin-polarized 2D Dirac fermions on its surface. In this Colloquium the theoretical foundation for topological insulators and superconductors is reviewed and recent experiments are described in which the signatures of topological insulators have been observed. Transport experiments on  $\mathrm{HgTe / CdTe}$  quantum wells are described that demonstrate the existence of the edge states predicted for the quantum spin Hall insulator. Experiments on  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$ ,  $\mathrm{Bi}_2\mathrm{Se}_3$ ,  $\mathrm{Bi}_2\mathrm{Te}_3$ , and  $\mathrm{Sb}_2\mathrm{Te}_3$  are then discussed that establish these materials as 3D topological insulators and directly probe the topology of their surface states. Exotic states are described that can occur at the surface of a 3D topological insulator due to an induced energy gap. A magnetic gap leads to a novel quantum Hall state that gives rise to a topological magnetoelectric effect. A superconducting energy gap leads to a state that supports Majorana fermions and may provide a new venue for realizing proposals for topological quantum computation. Prospects for observing these exotic states are also discussed, as well as other potential device applications of topological insulators.

DOI: 10.1103/RevModPhys.82.3045

PACS number(s): 73.20.-r, 73.43.-f, 85.75.-d, 74.90.+n

# CONTENTS

I. Introduction 3045

II. Topological Band Theory 3046

A. The insulating state 3046  
B. The quantum Hall state 3047

1. The TKNN invariant 3047  
2. Graphene, Dirac electrons, and Haldane model 3047  
3. Edge states and the bulk-boundary correspondence 3048

C.  $Z_{2}$  topological insulator 3049  
D. Topological superconductor, Majorana fermions 3050

1. Bogoliubov-de Gennes theory 3050  
2. Majorana fermion boundary states 3051  
3. Periodic Table 3051

III. Quantum Spin Hall Insulator 3052

A. Model system: Graphene 3052  
B. HgTe/CdTe quantum well structures 3053

IV. 3D Topological Insulators 3054

A. Strong and weak topological insulators 3054  
B. The first 3D topological insulator:  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$  3055  
C. Second generation materials:  $\mathrm{Bi}_2\mathrm{Se}_3$ $\mathrm{Bi}_{2}\mathrm{Te}_{3}$  , and  $\mathrm{Sb}_2\mathrm{Te}_3$  3058

V. Exotic Broken Symmetry Surface Phases 3061

A.Quantum Hall effect and topological magnetoelectric effect 3061

1. Surface quantum Hall effect 3061  
2. Topological magnetoelectric effect and axion electrodynamics 3061

B. Superconducting proximity effect 3062

1. Majorana fermions and topological quantum computing 3062  
2. Majorana fermions on topological insulators 3063

VI. Conclusion and Outlook 3064

Acknowledgments 3064

References 3065

# I. INTRODUCTION

A recurring theme in condensed-matter physics has been the discovery and classification of distinctive phases of matter. Often, phases can be understood using Landau's approach, which characterizes states in terms of underlying symmetries that are spontaneously broken. Over the past 30 years, the study of the quantum Hall effect has led to a different classification paradigm based on the notion of topological order (Thouless et al., 1982; Wen, 1995). The state responsible for the quantum Hall effect does not break any symmetries, but it defines a topological phase in the sense that certain fundamental properties (such as the quantized value of the Hall

conductance and the number of gapless boundary modes) are insensitive to smooth changes in material parameters and cannot change unless the system passes through a quantum phase transition.

In the past five years a new field has emerged in condensed-matter physics based on the realization that the spin-orbit interaction can lead to topological insulating electronic phases (Kane and Mele, 2005a, 2005b; Fu, Kane, and Mele, 2007; Moore and Balents, 2007; Roy, 2009b) and on the prediction and observation of these phases in real materials (Bernevig, Hughes, and Zhang, 2006; Fu and Kane, 2007; Konig et al., 2007; Hsieh et al., 2008; Xia, Qian, Hsieh, Wray, et al., 2009; Zhang, Liu, et al., 2009). A topological insulator, like an ordinary insulator, has a bulk energy gap separating the highest occupied electronic band from the lowest empty band. The surface (or edge in two dimensions) of a topological insulator, however, necessarily has gapless states that are protected by time-reversal symmetry. The topological insulator is closely related to the two-dimensional (2D) integer quantum Hall state, which also has unique edge states. The surface (or edge) states of a topological insulator lead to a conducting state with properties unlike any other known one-dimensional (1D) or 2D electronic systems. In addition to their fundamental interest, these states are predicted to have special properties that could be useful for applications ranging from spintronics to quantum computation.

The concept of topological order (Wen, 1995) is often used to characterize the intricately correlated fractional quantum Hall states (Tsui, Stormer, and Gossard, 1982), which require an inherently many-body approach to understand (Laughlin, 1983). However, topological considerations also apply to the simpler integer quantum Hall states (Thouless et al., 1982), for which an adequate description can be formulated in terms of single-particle quantum mechanics. In this regard, topological insulators are similar to the integer quantum Hall effect. Due to the presence of a single-particle energy gap, electron-electron interactions do not modify the state in an essential way. Topological insulators can be understood within the framework of the band theory of solids (Bloch, 1929). It is remarkable that after more than 80 years, there are still treasures to be uncovered within band theory.

In this Colloquium, we review the theoretical and experimental foundations of this rapidly developing field. We begin in Sec. II with an introduction to topological band theory, in which we explain the topological order in the quantum Hall effect and in topological insulators. We also give a short introduction to topological superconductors, which can be understood within a similar framework. A unifying feature of these states is the bulk-boundary correspondence, which relates the topological structure of bulk crystal to the presence of gapless boundary modes. Section III describes the 2D topological insulator, also known as a quantum spin Hall insulator, and discusses the discovery of this phase in  $\mathrm{HgCdTe}$  quantum wells. Section IV is devoted to three-dimensional (3D) topological insulators. We review their

experimental discovery in  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$ , as well as more recent work on "second-generation" materials  $\mathrm{Bi}_2\mathrm{Se}_3$  and  $\mathrm{Bi}_2\mathrm{Te}_3$ . Section V focuses on exotic states that can occur at the surface of a topological insulator due to an induced energy gap. An energy gap induced by a magnetic field or proximity to a magnetic material leads to a novel quantum Hall state along with a topological magnetoelectric effect. An energy gap due to proximity with a superconductor leads to a state that supports Majorana fermions and may provide a new venue for realizing proposals for topological quantum computation. In Sec. VI we conclude with a discussion of new materials, new experiments, and open problems.

Some aspects of this subject have been described in other reviews, including the review of the quantum spin Hall effect by König et al. (2008) and surveys by Moore (2010) and Qi and Zhang (2010).

# II. TOPOLOGICAL BAND THEORY

# A. The insulating state

The insulating state is the most basic state of matter. The simplest insulator is an atomic insulator, with electrons bound to atoms in closed shells. Such a material is electrically inert because it takes a finite energy to dislodge an electron. Stronger interaction between atoms in a crystal leads to covalent bonding. One of the triumphs of quantum mechanics in the 20th century was the development of the band theory of solids, which provides a language for describing the electronic structure of such states. This theory exploits the translational symmetry of the crystal to classify electronic states in terms of their crystal momentum  $\mathbf{k}$ , defined in a periodic Brillouin zone. The Bloch states  $|u_{m}(\mathbf{k})\rangle$ , defined in a single unit cell of the crystal, are eigenstates of the Bloch Hamiltonian  $\mathcal{H}(\mathbf{k})$ . The eigenvalues  $E_{m}(\mathbf{k})$  define energy bands that collectively form the band structure. In an insulator an energy gap separates the occupied valence-band states from the empty conduction-band states. Though the gap in an atomic insulator, such as solid argon, is much larger than that of a semiconductor, there is a sense in which both belong to the same phase. One can imagine tuning the Hamiltonian so as to interpolate continuously between the two without closing the energy gap. Such a process defines a topological equivalence between different insulating states. If one adopts a slightly coarser "stable" topological classification scheme, which equates states with different numbers of trivial core bands, then all conventional insulators are equivalent. Indeed, such insulators are equivalent to the vacuum, which according to Dirac's relativistic quantum theory also has an energy gap (for pair production), a conduction band (electrons), and a valence band (positrons).

Are all electronic states with an energy gap topologically equivalent to the vacuum? The answer is no, and the counterexamples are fascinating states of matter.

# B. The quantum Hall state

The simplest counterexample is the integer quantum Hall state (von Klitzing, Dorda, and Pepper, 1980; Prange and Girvin, 1987), which occurs when electrons confined to two dimensions are placed in a strong magnetic field. The quantization of the electrons' circular orbits with cyclotron frequency  $\omega_{c}$  leads to quantized Landau levels with energy  $\epsilon_{m} = \hbar \omega_{c}(m + 1 / 2)$ . If  $N$  Landau levels are filled and the rest are empty, then an energy gap separates the occupied and empty states just as in an insulator. Unlike an insulator, though, an electric field causes the cyclotron orbits to drift, leading to a Hall current characterized by the quantized Hall conductivity,

$$
\sigma_ {x y} = N e ^ {2} / h. \tag {1}
$$

The quantization of  $\sigma_{xy}$  has been measured to 1 part in  $10^{9}$  (von Klitzing, 2005). This precision is a manifestation of the topological nature of  $\sigma_{xy}$ .

Landau levels can be viewed as a "band structure." Since the generators of translations do not commute with one another in a magnetic field, electronic states cannot be labeled with momentum. However, if a unit cell with area  $2\pi \hbar c / eB$  enclosing a flux quantum is defined, then lattice translations do commute, so Bloch's theorem allows states to be labeled by 2D crystal momentum  $\mathbf{k}$ . In the absence of a periodic potential, the energy levels are simply the  $\mathbf{k}$  independent Landau levels  $E_{m}(\mathbf{k}) = \epsilon_{m}$ . In the presence of a periodic potential with the same lattice periodicity, the energy levels will disperse with  $\mathbf{k}$ . This leads to a band structure that looks identical to that of an ordinary insulator.

# 1. The TKNN invariant

What is the difference between a quantum Hall state characterized by Eq. (1) and an ordinary insulator? The answer, explained by Thouless, Kohmoto, Nightingale, and den Nijs (1982) (TKNN), is a matter of topology. A 2D band structure consists of a mapping from the crystal momentum  $\mathbf{k}$  (defined on a torus) to the Bloch Hamiltonian  $\mathcal{H}(\mathbf{k})$ . Gapped band structures can be classified topologically by considering the equivalence classes of  $\mathcal{H}(\mathbf{k})$  that can be continuously deformed into one another without closing the energy gap. These classes are distinguished by a topological invariant  $n \in \mathbb{Z}$  ( $\mathbb{Z}$  denotes the integers) called the Chern invariant.

The Chern invariant is rooted in the mathematical theory of fiber bundles (Nakahara, 1990), but it can be understood physically in terms of the Berry phase (Berry, 1984) associated with the Bloch wave functions  $|u_{m}(\mathbf{k})\rangle$ . Provided there are no accidental degeneracies when  $\mathbf{k}$  is transported around a closed loop,  $|u_{m}(\mathbf{k})\rangle$  acquires a well defined Berry phase given by the line integral of  $\mathcal{A}_m = i\langle u_m|\nabla_k|u_m\rangle$ . This may be expressed as a surface integral of the Berry flux  $\mathcal{F}_m = \nabla \times \mathcal{A}_m$ . The Chern invariant is the total Berry flux in the Brillouin zone,

![](images/57588d150fe97a058fc0168525cdd378cb4a54b2e14bf20a807005e70e898598.jpg)

![](images/6c2f72e9a5a2c426b5c1953fc184ae53138e02fa9dddfa71f1debad2036fbe1b.jpg)

![](images/a18eadf45943328a188ef735327600e2c2800ba66281aeb6cf1a50ac64536192.jpg)

![](images/402890bb54d2546ce565728584b28392453575744869884950493ece47673c7c.jpg)  
FIG. 1. (Color online) States of matter. (a)-(c) The insulating state. (a) An atomic insulator. (b) A simple model insulating band structure. (d)-(f) The quantum Hall state. (d) The cyclotron motion of electrons. (e) The Landau levels, which may be viewed as a band structure. (c) and (f) Two surfaces which differ in their genus,  $g$ . (c)  $g = 0$  for the sphere and (f)  $g = 1$  for the donut. The Chern number  $n$  that distinguishes the two states is a topological invariant similar to the genus.

![](images/333691f115e7de2771aa50a96019e381830d6a8d7518904da7bdf2df4cb00c3b.jpg)

![](images/dde6405a1c2ccbeac6d009afea73231949e7e4e86107da8c8044fb30f87f3b99.jpg)

$$
n _ {m} = \frac {1}{2 \pi} \int d ^ {2} \mathbf {k} \mathcal {F} _ {m}. \tag {2}
$$

$n_m$  is integer quantized for reasons analogous to the quantization of the Dirac magnetic monopole. The total Chern number, summed over all occupied bands,  $n = \sum_{m=1}^{N} n_m$  is invariant even if there are degeneracies between occupied bands, provided the gap separating occupied and empty bands remains finite. TKNN showed that  $\sigma_{xy}$ , computed using the Kubo formula, has the same form, so that  $N$  in Eq. (1) is identical to  $n$ . The Chern number  $n$  is a topological invariant in the sense that it cannot change when the Hamiltonian varies smoothly. This helps to explain the robust quantization of  $\sigma_{xy}$ .

The meaning of Eq. (2) can be clarified by a simple analogy. Rather than maps from the Brillouin zone to a Hilbert space, consider simpler maps from two to three dimensions, which describe surfaces. 2D surfaces can be topologically classified by their genus  $g$ , which counts the number of holes. For instance, a sphere [Fig. 1(c)] has  $g = 0$ , while a donut [Fig. 1(f)] has  $g = 1$ . A theorem in mathematics due to Gauss and Bonnet (Nakahara, 1990) states that the integral of the Gaussian curvature over a closed surface is a quantized topological invariant, and its value is related to  $g$ . The Chern number is an integral of a related curvature.

# 2. Graphene, Dirac electrons, and Haldane model

A simple example of the quantum Hall effect in a band theory is provided by a model of graphene in a periodic magnetic field introduced by Haldane (1988). We briefly digress here to introduce graphene because it will provide insight into the conception of the 2D quantum spin Hall insulator and because the physics of Dirac electrons present in graphene has important parallels at the surface of a 3D topological insulator.

Graphene is a 2D form of carbon that is of current interest (Novoselov et al., 2005; Zhang et al., 2005; Geim and Novoselov, 2007; Castro Neto et al., 2009). What makes graphene interesting electronically is the fact that the conduction band and valence band touch each other at two distinct points in the Brillouin zone. Near those points the electronic dispersion resembles the linear dispersion of massless relativistic particles, described by the Dirac equation (DiVincenzo and Mele, 1984; Semenoff, 1984). The simplest description of graphene employs a two band model for the  $p_z$  orbitals on the two equivalent atoms in the unit cell of graphene's honeycomb lattice. The Bloch Hamiltonian is then a  $2\times 2$  matrix,

$$
\mathcal {H} (\mathbf {k}) = \mathbf {h} (\mathbf {k}) \cdot \vec {\sigma}, \tag {3}
$$

where  $\vec{\sigma} = (\sigma_x,\sigma_y,\sigma_z)$  are Pauli matrices and  $\mathbf{h}(\mathbf{k})$ $= (h_{x}(\mathbf{k}),h_{y}(\mathbf{k}),0)$ . The combination of inversion  $(\mathcal{P})$  and time-reversal  $(\mathcal{T})$  symmetry requires  $h_z(\mathbf{k}) = 0$  because  $\mathcal{P}$  takes  $h_z(\mathbf{k})$  to  $-h_z(-\mathbf{k})$ , while  $\mathcal{T}$  takes  $h_z(\mathbf{k})$  to  $+h_z(-\mathbf{k})$ . The Dirac points occur because the two components  $\mathbf{h}(\mathbf{k})$  can have point zeros in two dimensions. In graphene they occur at two points,  $\mathbf{K}$  and  $\mathbf{K}' = -\mathbf{K}$ , whose locations at the Brillouin-zone corners are fixed by graphene's rotational symmetry. For small  $\mathbf{q}\equiv \mathbf{k} - \mathbf{K}$ ,  $\mathbf{h}(\mathbf{q}) = \hbar v_F\mathbf{q}$ , where  $v_{F}$  is a velocity, so  $\mathcal{H}(\mathbf{q}) = \hbar v_F\mathbf{q}\cdot \vec{\sigma}$  has the form of a 2D massless Dirac Hamiltonian.

The degeneracy at the Dirac point is protected by  $\mathcal{P}$  and  $\mathcal{T}$  symmetry. By breaking these symmetries the degeneracy can be lifted. For instance,  $\mathcal{P}$  symmetry is violated if the two atoms in the unit cell are inequivalent. This allows  $h_z(\mathbf{k})$  to be nonzero. If  $h_z(\mathbf{k})$  is small, then near  $\mathbf{K}$  [Eq. (3)] becomes a massive Dirac Hamiltonian,

$$
\mathcal {H} (\mathbf {q}) = \hbar v _ {F} \mathbf {q} \cdot \vec {\sigma} + m \sigma_ {z}, \tag {4}
$$

where  $m = h_{z}(\mathbf{K})$ . The dispersion  $E(\mathbf{q}) = \pm \sqrt{|\hbar v_{F}\mathbf{q}|^{2} + m^{2}}$  has an energy gap  $2|m|$ . Note that  $T$  symmetry requires the Dirac point at  $\mathbf{K}'$  to have a mass  $m' = h_{z}(\mathbf{K}')$  with the same magnitude and sign,  $m' = m$ . This state describes an ordinary insulator.

Haldane (1988) imagined lifting the degeneracy by breaking  $\mathcal{T}$  symmetry with a magnetic field that is zero on the average but has the full symmetry on the lattice. This perturbation allows nonzero  $h_z(\mathbf{k})$  and introduces a mass to the Dirac points. However,  $\mathcal{P}$  symmetry requires the masses at  $\mathbf{K}$  and  $\mathbf{K}'$  to have opposite signs,  $m' = -m$ . Haldane showed that this gapped state is not an insulator but rather a quantum Hall state with  $\sigma_{xy} = e^2 / h$ .

This nonzero Hall conductivity can be understood in terms of Eq. (2). For a two level Hamiltonian of the form of Eq. (3) it is well known that the Berry flux (Berry, 1984) is related to the solid angle subtended by the unit vector  $\hat{h} (\mathbf{k}) = \mathbf{h}(\mathbf{k}) / |\mathbf{h}(\mathbf{k})|$ , so that Eq. (2) takes the form

$$
n = \frac {1}{4 \pi} \int d ^ {2} \mathbf {k} \left(\partial_ {k _ {x}} \hat {h} \times \partial_ {k _ {y}} \hat {h}\right) \cdot \hat {h}. \tag {5}
$$

This simply counts the number of times  $\hat{h} (\mathbf{k})$  wraps around the unit sphere as a function of  $\mathbf{k}$ . When the

![](images/b5adc233d2d0a8b8f19b07ad0c615049c9a3ccd3fc61330c462b7cdfdc71caff.jpg)  
FIG. 2. (Color online) The interface between a quantum Hall state and an insulator has chiral edge mode. (a) The skipping cyclotron orbits. (b) The electronic structure of a semi-infinite strip described by the Haldane model. A single edge state connects the valence band to the conduction band.

![](images/653cad37b750cf38b561b5b52e9cb44e13ea66d8afaf917cc305d5880ffbee19.jpg)

masses  $m = m' = 0$ ,  $\hat{h}(\mathbf{k})$  is confined to the equator  $h_z = 0$ , with a unit (and opposite) winding around each of the Dirac points where  $|\mathbf{h}| = 0$ . For small but finite  $m$ ,  $|\mathbf{h}| \neq 0$  everywhere, and  $\hat{h}(\mathbf{K})$  visits the north or south pole, depending on the sign of  $m$ . It follows that each Dirac point contributes  $\pm e^2 / 2h$  to  $\sigma_{xy}$ . In the insulating state with  $m = m'$  the two cancel, so  $\sigma_{xy} = 0$ . In the quantum Hall state they add.

It is essential that there were an even number of Dirac points since otherwise the Hall conductivity would be quantized to a half integer. This is in fact guaranteed by the fermion doubling theorem (Nielssen and Ninomiya, 1983), which states that for a  $T$  invariant system Dirac points must come in pairs. We return to this issue in Sec. IV, where the surface of a topological insulator provides a loophole for this theorem.

# 3. Edge states and the bulk-boundary correspondence

A fundamental consequence of the topological classification of gapped band structures is the existence of gapless conducting states at interfaces where the topological invariant changes. Such edge states are well known at the interface between the integer quantum Hall state and vacuum (Halperin, 1982). They may be understood in terms of the skipping motion electrons execute as their cyclotron orbits bounce off the edge [Fig. 2(a)]. Importantly, the electronic states responsible for this motion are chiral in the sense that they propagate in one direction only along the edge. These states are insensitive to disorder because there are no states available for backscattering—a fact that underlies the perfectly quantized electronic transport in the quantum Hall effect.

The existence of such "one way" edge states is deeply related to the topology of the bulk quantum Hall state. Imagine an interface where a crystal slowly interpolates as a function of distance  $y$  between a quantum Hall state  $(n = 1)$  and a trivial insulator  $(n = 0)$ . Somewhere along the way the energy gap has to vanish because otherwise it is impossible for the topological invariant to change. There will therefore be low energy electronic states bound to the region where the energy gap passes through zero. This interplay between topology and gap

less modes is ubiquitous in physics and has appeared in many contexts. It was originally found by Jackiw and Rebbi (1976) in their analysis of a 1D field theory. Similar ideas were used by Su, Schrieffer, and Heeger (1979) to describe soliton states in polyacetalene.

A simple theory of the chiral edge states based on Jackiw and Rebbi (1976) can be developed using the two band Dirac model (4). Consider an interface where the mass  $m$  at one of the Dirac points changes sign as a function of  $y$ . We thus let  $m \rightarrow m(y)$ , where  $m(y) > 0$  gives the insulator for  $y > 0$  and  $m(y) < 0$  gives the quantum Hall state for  $y < 0$ . Assume  $m' > 0$  is fixed. The Schrödinger equation, obtained by replacing  $\mathbf{q}$  by  $-i\vec{\nabla}$  in Eq. (4), has a simple and elegant exact solution,

$$
\psi_ {q _ {x}} (x, y) \propto e ^ {i q _ {x} x} \exp \left(- \int_ {0} ^ {y} d y ^ {\prime} m \left(y ^ {\prime}\right) d y ^ {\prime} / v _ {F}\right) \binom {1} {1}, \tag {6}
$$

with  $E(q_{x}) = \hbar v_{F}q_{x}$ . This band of states intersects the Fermi energy  $E_{F}$  with a positive group velocity  $dE / dq_{x} = \hbar v_{F}$  and defines a right moving chiral edge mode.

In the 1980s related ideas were applied to narrow gap semiconductors, which can be modeled using a 3D massive Dirac Hamiltonian (Volkov and Pankratov, 1985; Fradkin, Dagotto, and Boyanovsky, 1986). An interface where the Dirac mass changes sign is associated with gapless 2D Dirac fermion states. These share some similarities with the surface states of a 3D topological insulator, but as we shall see in Sec. IV.A there is a fundamental difference. In a separate development, Kaplan (1992) showed that in lattice quantum chromodynamics four-dimensional (4D) chiral fermions could be simulated on a five-dimensional lattice by introducing a similar domain wall. This provided a method for circumventing the doubling theorem (Nielssen and Ninomiya, 1983), which prevented the simulation of chiral fermions on a 4D lattice. Quantum Hall edge states and surface states of a topological insulator evade similar doubling theorems.

The chiral edge states in the quantum Hall effect can be seen explicitly by solving the Haldane model in a semi-infinite geometry with an edge at  $y = 0$ . Figure 2(b) shows the energy levels as a function of the momentum  $k_{x}$  along the edge. The solid regions show the bulk conduction and valence bands, which form continuum states and show the energy gap near  $\mathbf{K}$  and  $\mathbf{K}'$ . A single band, describing states bound to the edge, connects the valence band to the conduction band with a positive group velocity.

By changing the Hamiltonian near the surface the dispersion of the edge states can be modified. For instance,  $E(q_{x})$  could develop a kink so that the edge states intersect  $E_{F}$  three times—twice with a positive group velocity and once with a negative group velocity. The difference,  $N_{R} - N_{L}$ , between the number of right and left moving modes, however, cannot change and is determined by the topological structure of the bulk states. This is summarized by the bulk-boundary correspondence,

![](images/f908e8c63c9bb51f530258245038521ac24d850910f97f2f5bb5e13aed52e0e5.jpg)  
FIG. 3. (Color online) Electronic dispersion between two boundary Kramers degenerate points  $\Gamma_{a} = 0$  and  $\Gamma_{b} = \pi / a$ . In (a) the number of surface states crossing the Fermi energy  $E_{F}$  is even, whereas in (b) it is odd. An odd number of crossings leads to topologically protected metallic boundary states.

![](images/365f954087b6548b1ddc6c51752a84dea0c84f1190469c2b8072e49bd96d6f1e.jpg)

$$
N _ {R} - N _ {L} = \Delta n, \tag {7}
$$

where  $\Delta n$  is the difference in the Chern number across the interface.

# C.  $Z_{2}$  topological insulator

Since the Hall conductivity is odd under  $\mathcal{T}$ , the topologically nontrivial states described in Sec. II.B.3 can only occur when  $\mathcal{T}$  symmetry is broken. However, the spin-orbit interaction allows a different topological class of insulating band structures when  $\mathcal{T}$  symmetry is unbroken (Kane and Mele, 2005a). The key to understanding this new topological class is to examine the role of  $\mathcal{T}$  symmetry for spin  $1/2$  particles.

$\mathcal{T}$  symmetry is represented by an antiunitary operator  $\Theta = \exp (i\pi S_y / \hbar)K$  where  $S_{y}$  is the spin operator and  $K$  is complex conjugation. For spin 1/2 electrons,  $\Theta$  has the property  $\Theta^2 = -1$ . This leads to an important constraint, known as Kramers' theorem, which all eigenstates of a  $\mathcal{T}$  invariant Hamiltonian are at least twofold degenerate. This follows because if a nondegenerate state  $|\chi \rangle$  existed then  $\Theta |\chi \rangle = c|\chi \rangle$  for some constant  $c$ . This would mean  $\Theta^2 |\chi \rangle = |c|^2 |\chi \rangle$ , which is not allowed because  $|c|^2 \neq -1$ . In the absence of spin-orbit interactions, Kramers' degeneracy is simply the degeneracy between up and down spins. In the presence of spin-orbit interactions, however, it has nontrivial consequences.

A  $T$  invariant Bloch Hamiltonian must satisfy

$$
\Theta \mathcal {H} (\mathbf {k}) \Theta^ {- 1} = \mathcal {H} (- \mathbf {k}). \tag {8}
$$

One can classify the equivalence classes of Hamiltonians satisfying this constraint that can be smoothly deformed without closing the energy gap. The TKNN invariant is  $n = 0$ , but there is an additional invariant with two possible values,  $\nu = 0$  or 1 (Kane and Mele, 2005b). The fact that there are two topological classes can be understood by appealing to the bulk-boundary correspondence.

In Fig. 3 we plot analogous to Fig. 2 the electronic states associated with the edge of a  $T$  invariant 2D insulator as a function of the crystal momentum along the edge. Only half of the Brillouin zone  $0 < k_{x} < \pi /a$  is shown because  $\mathcal{T}$  symmetry requires that the other half  $-\pi /a < k < 0$  is a mirror image. As in Fig. 2, the shaded regions depict the bulk conduction and valence bands

separated by an energy gap. Depending on the details of the Hamiltonian near the edge there may or may not be states bound to the edge inside the gap. If they are present, however, then Kramers' theorem requires they are twofold degenerate at the  $\mathcal{T}$  invariant momenta  $k_{x} = 0$  and  $\pi / a$  (which is the same as  $-\pi / a$ ). Away from these special points, labeled  $\Gamma_{a,b}$  in Fig. 3, a spin-orbit interaction will split the degeneracy. There are two ways the states at  $k_{x} = 0$  and  $\pi / a$  can connect. In Fig. 3(a) they connect pairwise. In this case the edge states can be eliminated by pushing all of the bound states out of the gap. Between  $k_{x} = 0$  and  $\pi / a$ , the bands intersect  $E_{F}$  an even number of times. In contrast, in Fig. 3(b) the edge states cannot be eliminated. The bands intersect  $E_{F}$  an odd number of times.

Which of these alternatives occurred depend on the topological class of the bulk band structure? Since each band intersecting  $E_{F}$  at  $k_{x}$  has a Kramers partner at  $-k_{x}$ , the bulk-boundary correspondence relates the number  $N_{K}$  of Kramers pairs of edge modes intersecting  $E_{F}$  to the change in the  $\mathbb{Z}_2$  invariants across the interface,

$$
N _ {K} = \Delta \nu \bmod 2. \tag {9}
$$

We conclude that a 2D topological insulator has topologically protected edge states. These form a unique 1D conductor, whose properties will be discussed in Sec. III. The above considerations can be generalized to 3D topological insulators, discussed in Sec. IV, which have protected surface states.

There are several mathematical formulations of the  $\mathbb{Z}_2$  invariant  $\nu$  (Kane and Mele, 2005b; Fu and Kane, 2006, 2007; Fukui and Hatsugai, 2007; Moore and Balents, 2007; Fukui, Fujiwara, and Hatsugai, 2008; Qi, Hughes, and Zhang, 2008; Roy, 2009a; Wang, Qi, and Zhang, 2010). One approach (Fu and Kane, 2006) is to define a unitary matrix  $w_{mn}(\mathbf{k}) = \langle u_m(\mathbf{k})|\Theta |u_n(-\mathbf{k})\rangle$  built from the occupied Bloch functions  $|u_{m}(\mathbf{k})\rangle$ . Since  $\Theta$  is antiunitary and  $\Theta^2 = -1$ ,  $w^{T}(\mathbf{k}) = -w(-\mathbf{k})$ . There are four special points  $\Lambda_{a}$  in the bulk 2D Brillouin zone where  $\mathbf{k}$  and  $-\mathbf{k}$  coincide, so  $w(\Lambda_{a})$  is antisymmetric. The determinant of an antisymmetric matrix is the square of its Pfaffian, which allows us to define  $\delta_{a} = \mathrm{Pf}[w(\Lambda_{a})] / \sqrt{\mathrm{Det}[w(\Lambda_{a})]}$ $\pm 1$ . Provided  $|u_{m}(\mathbf{k})\rangle$  is chosen continuously throughout the Brillouin zone (which is always possible), the branch of the square root can be specified globally, and the  $\mathbb{Z}_2$  invariant is

$$
(- 1) ^ {\nu} = \prod_ {a = 1} ^ {4} \delta_ {a}. \tag {10}
$$

This formulation can be generalized to 3D topological insulators and involves the eight special points in the 3D Brillouin zone.

The calculation of  $\nu$  is simpler if the crystal has extra symmetry. For instance, if the 2D system conserves the perpendicular spin  $S_{z}$ , then the up and down spins have independent Chern integers  $n_{\uparrow}, n_{\downarrow}$ .  $\mathcal{T}$  symmetry requires

$n_{\uparrow} + n_{\downarrow} = 0$ , but the difference  $n_{\sigma} = (n_{\uparrow} - n_{\downarrow}) / 2$  defines a quantized spin Hall conductivity (Sheng et al., 2006). The  $\mathbb{Z}_2$  invariant is then simply

$$
\nu = n _ {\sigma} \bmod 2. \tag {11}
$$

While  $n_{\uparrow}, n_{\downarrow}$  lose their meaning when  $S_{z}$  nonconserving terms (which are inevitably present) are added,  $\nu$  retains its identity.

If the crystal has inversion symmetry, there is another shortcut to computing  $\nu$  (Fu and Kane, 2007). At the special points  $\Lambda_{a}$  the Bloch states  $u_{m}(\Lambda_{a})$  are also parity eigenstates with eigenvalue  $\xi_{m}(\Lambda_{a}) = \pm 1$ . The  $\mathbb{Z}_2$  invariant then simply follows from Eq. (10) with

$$
\delta_ {a} = \prod_ {m} \xi_ {m} (\Lambda_ {a}), \tag {12}
$$

where the product is over the Kramers pairs of occupied bands. This has proven useful for identifying topological insulators from band-structure calculations (Fu and Kane, 2007; Teo, Fu, and Kane, 2008; Guo and Franz, 2009; Zhang, Liu, et al., 2009; Pesin and Balents, 2010).

# D. Topological superconductor, Majorana fermions

Considerations of topological band theory can also be used to topologically classify superconductors. This is a subject that has seen fascinating recent theoretical developments (Roy, 2008; Schnyder et al., 2008; Kitaev, 2009; Qi, Hughes, et al., 2009). We give an introduction that focuses on the simplest model superconductors. The more general case will be touched on at the end. This section will provide the conceptual basis for topological superconductors and explain the emergence of Majorana fermions in superconducting systems. It will also provide background for Sec. V.B, where we discuss Majorana states in superconductor-topological insulator structures along with possible applications to topological quantum computing.

# 1. Bogoliubov-de Gennes theory

In the BCS mean-field theory of a superconductor the Hamiltonian for a system of spinless electrons may be written in the form (de Gennes, 1966),

$$
H - \mu N = \frac {1}{2} \sum_ {\mathbf {k}} \left(c _ {\mathbf {k}} ^ {\dagger} c _ {- \mathbf {k}}\right) \mathcal {H} _ {\mathrm {B d G}} (\mathbf {k}) \binom {c _ {\mathbf {k}}} {c _ {- \mathbf {k}} ^ {\dagger}}, \tag {13}
$$

where  $c_{\mathbf{k}}^{\dagger}$  is an electron creation operator and  $\mathcal{H}_{\mathrm{BdG}}$  is a  $2\times 2$  block matrix, which in Nambu's notation may be written in terms of Pauli matrices  $\vec{\tau}$  as

$$
\mathcal {H} _ {\mathrm {B d G}} (\mathbf {k}) = \left[ \mathcal {H} _ {0} (\mathbf {k}) - \mu \right] \tau_ {z} + \Delta_ {1} (\mathbf {k}) \tau_ {x} + \Delta_ {2} (\mathbf {k}) \tau_ {y}. \tag {14}
$$

Here,  $\mathcal{H}_0(\mathbf{k})$  is the Bloch Hamiltonian in the absence of superconductivity and  $\Delta = \Delta_{1} + i\Delta_{2}$  is the BCS mean-field pairing potential, which for spinless particles must have odd parity,  $\Delta (-\mathbf{k}) = -\Delta (\mathbf{k})$ . For a uniform system the excitation spectrum of a superconductor is given by the eigenvalues of  $\mathcal{H}_{\mathrm{BdG}}$ , which exhibit a superconducting energy gap. More generally, for spatially dependent  $\mathcal{H}_0$

![](images/52a4f2fa51c81a94df395074f0c49574f138df14d8ab713d7b068a2e2b48e9bb.jpg)  
FIG. 4. (Color online) Boundary states for a topological superconductor (TSC). (a) A 1D superconductor with bound states at its ends. The end state spectrum for (b) an ordinary 1D superconductor and (c) a 1D topological superconductor. (d) A topological 2D superconductor with (e) a chiral Majorana edge mode. (c) A vortex with flux  $\Phi = h / 2e$  is associated with a zero mode.

![](images/fa4b0d15703c31a90cab3a5db801d97e2b67827d34e1e8a2a956470d7c277905.jpg)

and  $\Delta$  the Schrodinger equation associated with  $\mathcal{H}_{\mathrm{BdG}}$  is known as the Bogoliubov-de Gennes (BdG) equation.

Since Eq. (13) has  $c$  and  $c^\dagger$  on both sides there is an inherent redundancy built into the BdG Hamiltonian. For  $\Delta = 0$ ,  $\mathcal{H}_{\mathrm{BdG}}$  includes two copies of  $\mathcal{H}_0$  with opposite sign. More generally,  $\mathcal{H}_{\mathrm{BdG}}$  has an intrinsic particle-hole symmetry expressed by

$$
\Xi \mathcal {H} _ {\mathrm {B d G}} (\mathbf {k}) \Xi^ {- 1} = - \mathcal {H} _ {\mathrm {B d G}} (- \mathbf {k}), \tag {15}
$$

where the particle-hole operator  $\Xi = \tau_{x}K$  satisfies  $\Xi^2 = +1$ . Equation (15) follows from  $\mathcal{H}_0(-\mathbf{k}) = \mathcal{H}_0(\mathbf{k})^*$  and the odd parity of the real  $\Delta (\mathbf{k})$ . It follows that every eigenstate of  $\mathcal{H}_{\mathrm{BdG}}$  with energy  $E$  has a partner at  $-E$ . These two states are redundant because the Bogoliubov quasiparticle operators associated with them satisfy  $\Gamma_E^\dagger = \Gamma_{-E}$ . Thus, creating a quasiparticle in state  $E$  has the same effect as removing one from state  $-E$ .

The particle-hole symmetry constraint (15) has a similar structure to the time-reversal constraint in Eq. (8), so it is natural to consider the classes of BdG Hamiltonians that can be continuously deformed into one another without closing the energy gap. In the simplest case, spinless fermions, the classification can be shown to be  $\mathbb{Z}_2$  in one dimension and  $\mathbb{Z}$  in two dimensions. As in Sec. II.C, this can be most easily understood by appealing to the bulk-boundary correspondence.

# 2. Majorana fermion boundary states

At the end of a 1D superconductor (Kitaev, 2000) there may or may not be discrete states within the energy gap that are bound to the end [Figs. 4(a)-4(c)]. If they are present, then every state at  $+E$  has a partner at  $-E$ . Such finite-energy pairs are not topologically protected because they can simply be pushed out of the energy gap. However, a single unpaired bound state at  $E = 0$  is protected because it cannot move away from  $E = 0$ . The presence or absence of such a zero mode is determined by the  $\mathbb{Z}_2$  topological class of the bulk 1D superconductor.

The Bogoliubov quasiparticle states associated with the zero modes are fascinating objects (Kitaev, 2000;

Read and Green, 2000; Ivanov, 2001; Stern, von Oppen, and Mariani, 2004; Nayak et al., 2008). Due to the particle-hole redundancy the quasiparticle operators satisfy  $\Gamma_0 = \Gamma_0^\dagger$ . Thus, a quasiparticle is its own antiparticle—the defining feature of a Majorana fermion. A Majorana fermion is essentially half of an ordinary Dirac fermion. Due to the particle-hole redundancy, a single fermionic state is associated with each pair of  $\pm E$  energy levels. The presence or absence of a fermion in this state defines a two-level system with energy splitting  $E$ . Majorana zero modes must always come in pairs (for instance, a 1D superconductor has two ends), and a well-separated pair defines a degenerate two-level system, whose quantum state is stored nonlocally. This has profound implications, which we return to in Sec. V.B when discussing the proposal of Kitaev (2003) to use these properties for quantum information processing.

In two dimensions the integer classification  $\mathbb{Z}$  gives the number of chiral Majorana edge modes [Figs. 4(d) and 4(e)], which resemble chiral modes in the quantum Hall effect but for the particle-hole redundancy. A spinless superconductor with  $p_x + ip_y$  symmetry is the simplest model 2D topological superconductor. Such superconductors will also exhibit Majorana bound states at the core of vortices (Caroli, de Gennes, and Matricon, 1964; Volovik, 1999; Read and Green, 2000). This may be understood by considering the vortex to be a hole in the superconductor circled by an edge mode [Fig. 4(d)]. When the flux in the hole is  $h / 2e$  the edge modes are quantized such that one state is exactly at  $E = 0$ .

Majorana fermions have been studied in particle physics for decades but have not been definitively observed (Majorana, 1937; Wilczek, 2009). A neutrino might be a Majorana fermion. Efforts to observe certain lepton number violating neutrinoless double  $\beta$  decay processes may resolve that issue (Avignone, Elliott, and Engel, 2008). In condensed-matter physics, Majorana fermions can arise due to a paired condensate that allows a pair of fermionic quasiparticles to "disappear" into the condensate. They have been predicted in a number of physical systems related to the spinless  $p_x + ip_y$  superconductor, including the Moore-Read state of the  $\nu = 5 / 2$  quantum Hall effect (Moore and Read, 1991; Greiter, Wen, and Wilczek, 1992; Read and Green, 2000),  $\mathrm{Sr}_2\mathrm{RuO}_4$  (Das Sarma, Nayak, and Tewari, 2006), cold fermionic atoms near a Feshbach resonance (Gurarie, Radzihovsky, and Andreev, 2005; Tewari et al., 2007), and 2D structures that combine superconductivity, magnetism, and strong spin-orbit coupling (Lee, 2009; Sato and Fujimoto, 2009; Sau et al., 2010). In Sec. V.B we discuss the prospect for creating Majorana fermion states at interfaces between topological insulators and ordinary superconductors (Fu and Kane, 2008).

# 3. Periodic Table

Topological insulators and superconductors fit together into a rich and elegant mathematical structure that generalizes the notions of topological band theory described above (Schnyder et al., 2008; Kitaev, 2009;

TABLE I. Periodic table of topological insulators and superconductors. The ten symmetry classes are labeled using the notation of Altland and Zirnbauer (1997) (AZ) and are specified by presence or absence of  $T$  symmetry  $\Theta$ , particle-hole symmetry  $\Xi$ , and chiral symmetry  $\Pi = \Xi \Theta$ .  $\pm 1$  and 0 denote the presence and absence of symmetry, with  $\pm 1$  specifying the value of  $\Theta^2$  and  $\Xi^2$ . As a function of symmetry and space dimensionality  $d$ , the topological classifications  $(\mathbb{Z}, \mathbb{Z}_2$ , and 0) show a regular pattern that repeats when  $d \to d + 8$ .  

<table><tr><td colspan="4">Symmetry</td><td colspan="8">d</td></tr><tr><td>AZ</td><td>Θ</td><td>Ξ</td><td>Π</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>A</td><td>0</td><td>0</td><td>0</td><td>0</td><td>Z</td><td>0</td><td>Z</td><td>0</td><td>Z</td><td>0</td><td>Z</td></tr><tr><td>AIII</td><td>0</td><td>0</td><td>1</td><td>Z</td><td>0</td><td>Z</td><td>0</td><td>Z</td><td>0</td><td>Z</td><td>0</td></tr><tr><td>AI</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>Z</td><td>0</td><td>Z2</td><td>Z2</td><td>Z</td></tr><tr><td>BDI</td><td>1</td><td>1</td><td>1</td><td>Z</td><td>0</td><td>0</td><td>0</td><td>Z</td><td>0</td><td>Z2</td><td>Z2</td></tr><tr><td>D</td><td>0</td><td>1</td><td>0</td><td>Z2</td><td>Z</td><td>0</td><td>0</td><td>0</td><td>Z</td><td>0</td><td>Z2</td></tr><tr><td>DIII</td><td>-1</td><td>1</td><td>1</td><td>Z2</td><td>Z2</td><td>Z</td><td>0</td><td>0</td><td>0</td><td>Z</td><td>0</td></tr><tr><td>AII</td><td>-1</td><td>0</td><td>0</td><td>0</td><td>Z2</td><td>Z2</td><td>Z</td><td>0</td><td>0</td><td>0</td><td>Z</td></tr><tr><td>CII</td><td>-1</td><td>-1</td><td>1</td><td>Z</td><td>0</td><td>Z2</td><td>Z2</td><td>Z</td><td>0</td><td>0</td><td>0</td></tr><tr><td>C</td><td>0</td><td>-1</td><td>0</td><td>0</td><td>Z</td><td>0</td><td>Z2</td><td>Z2</td><td>Z</td><td>0</td><td>0</td></tr><tr><td>CI</td><td>1</td><td>-1</td><td>1</td><td>0</td><td>0</td><td>Z</td><td>0</td><td>Z2</td><td>Z2</td><td>Z</td><td>0</td></tr></table>

Schnyder et al., 2009; Ryu et al., 2010). The classes of equivalent Hamiltonians are determined by specifying the symmetry class and the dimensionality. The symmetry class depends on the presence or absence of  $\mathcal{T}$  symmetry (8) with  $\Theta^2 = \pm 1$  and/or particle-hole symmetry (15) with  $\Xi^2 = \pm 1$ . There are ten distinct classes, which are closely related to the classification of random matrices of Altland and Zirnbauer (1997). The topological classifications, given by  $\mathbb{Z}, \mathbb{Z}_2$ , or 0, show a regular pattern as a function of symmetry class and dimensionality and can be arranged into the Periodic Table of topological insulators and superconductors shown in Table I.

The quantum Hall state (class A, no symmetry;  $d = 2$ ), the  $\mathbb{Z}_2$  topological insulators (class AII,  $\Theta^2 = -1$ ;  $d = 2,3$ ), and the  $\mathbb{Z}_2$  and  $\mathbb{Z}$  topological superconductors (class D,  $\Xi^2 = 1$ ;  $d = 1,2$ ) described above are entries in the Periodic Table. There are also other nontrivial entries describing different topological superconducting and superfluid phases. Each nontrivial phase is predicted via the bulk-boundary correspondence to have gapless boundary states. One notable example is superfluid  ${}^{3}\mathrm{He}B$  (Volovik, 2003; Roy, 2008; Schnyder et al., 2008; Nagato, Higashitani, and Nagai, 2009; Qi, Hughes, et al., 2009; Volovik, 2009), in (class DIII,  $\Theta^2 = -1$ ,  $\Xi^2 = +1$ ;  $d = 3$ ) which has a  $\mathbb{Z}$  classification along with gapless 2D Majorana fermion modes on its surface. A generalization of the quantum Hall state introduced by Zhang and Hu (2001) corresponds to the  $d = 4$  entry in class A or AII. There are also other entries in physical dimensions that have yet to be filled by realistic systems. The search is on to discover such phases.

# III. QUANTUM SPIN HALL INSULATOR

The 2D topological insulator is known as a quantum spin Hall insulator. This state was originally theorized to

exist in graphene (Kane and Mele, 2005a) and in 2D semiconductor systems with a uniform strain gradient (Bernevig and Zhang, 2006). It was subsequently predicted to exist (Bernevig, Hughes, and Zhang, 2006) and was then observed (Konig et al., 2007) in  $\mathrm{HgCdTe}$  quantum well structures. In Sec. III.A we introduce the physics of this state in the model graphene system and describe its novel edge states. Section III.B reviews the experiments, which have also been the subject of the review article by Konig et al. (2008).

# A. Model system: Graphene

In Sec. II.B.2 we argued that the degeneracy at the Dirac point in graphene is protected by inversion and  $\mathcal{T}$  symmetry. That argument ignored the spin of the electrons. The spin-orbit interaction allows a new mass term in Eq. (3) with respect to all of graphene's symmetries. In the simplest picture, the intrinsic spin-orbit interaction commutes with the electron spin  $S_{z}$ , so the Hamiltonian decouples into two independent Hamiltonians for the up and down spins. The resulting theory is simply two copies of the model of Haldane (1988) with opposite signs of the Hall conductivity for up and down spins. This does not violate  $\mathcal{T}$  symmetry because time reversal flips both the spin and  $\sigma_{xy}$ . In an applied electric field, the up and down spins have Hall currents that flow in opposite directions. The Hall conductivity is thus zero, but there is a quantized spin Hall conductivity, defined by  $J_x^\uparrow - J_x^\downarrow = \sigma_{xy}^s E_y$  with  $\sigma_{xy}^s = e / 2\pi$  a quantum spin Hall effect. Related ideas were mentioned in earlier work on the planar state of  ${}^3\mathrm{He}$  films (Volovik and Yakovenko, 1989). Since it is two copies of a quantum Hall state, the quantum spin Hall state must have gapless edge states (Fig. 5).

![](images/f19dc5603642470798eadd956f8f5f1913f4a9e870df211ad3cd867e39339d35.jpg)  
FIG. 5. (Color online) Edge states in the quantum spin Hall insulator (QSHI). (a) The interface between a QSHI and an ordinary insulator. (b) The edge state dispersion in the graphene model in which up and down spins propagate in opposite directions.

![](images/56cc5388e3f1dbf96ba662bdfb7c60fb9b6375afdfeb819f216fae07a886beb7.jpg)

The above discussion was predicated on the conservation of spin  $S_{z}$ . This is not a fundamental symmetry, though, and spin nonconserving processes—present in any real system—invalidate the meaning of  $\sigma_{xy}^{s}$ . This brings into question theories that relied on spin conservation to predict an integer quantized  $\sigma_{xy}^{s}$  (Volovik and Yakovenko, 1989; Bernevig and Zhang, 2006; Qi, Wu, and Zhang, 2006), as well as the influential theory of the (nonquantized) spin Hall insulator (Murakami, Nagaosa, and Zhang, 2004). Kane and Mele (2005a) showed that due to  $T$  symmetry the edge states in the quantum spin Hall insulator are robust even when spin conservation is violated because their crossing at  $k = 0$  is protected by the Kramers degeneracy discussed in Sec. II.C. This established the quantum spin Hall insulator as a topological phase.

The quantum spin Hall edge states have the important "spin filtered" property that the up spins propagate in one direction, while the down spins propagate in the other. Such edge states were later termed "helical" (Wu, Bernevig, and Zhang, 2006), in analogy with the correlation between spin and momentum of a particle known as helicity. They form a unique 1D conductor that is essentially half of an ordinary 1D conductor. Ordinary conductors, which have up and down spins propagating in both directions, are fragile because the electronic states are susceptible to Anderson localization in the presence of weak disorder (Anderson, 1958; Lee and Ramakrishnan, 1985). By contrast, the quantum spin Hall edge states cannot be localized even for strong disorder. To see this, imagine an edge that is disordered in a finite region and perfectly clean outside that region. The exact eigenstates can be determined by solving the scattering problem relating incoming waves to those reflected from and transmitted through the disordered region. Kane and Mele (2005a) showed that the reflection amplitude is odd under  $\mathcal{T}$  -roughly because it involves flipping the spin. It follows that unless  $\mathcal{T}$  symmetry is broken, an incident electron is transmitted perfectly across the disordered region. Thus, eigenstates at any energy are extended, and at temperature  $T = 0$  the edge state transport is ballistic. For  $T > 0$  inelastic backscattering processes are allowed, which will, in general, lead to a finite conductivity.

The edge states are similarly protected from the effects of weak electron interactions, though for strong interactions the Luttinger liquid effects lead to a magnetic instability (Wu, Bernevig, and Zhang, 2006; Xu and Moore, 2006). This strong interacting phase is interesting because it will exhibit charge  $e / 2$  quasiparticles similar to solitons in the model of Su, Schrieffer, and Heeger (1979). For sufficiently strong interactions similar fractionalization could be observed by measuring shot noise in the presence of magnetic impurities (Maciejko et al., 2009) or at a quantum point contact (Teo and Kane, 2009).

# B. HgTe/CdTe quantum well structures

Graphene is made out of carbon—a light element with a weak spin-orbit interaction. Though there is disagreement on its absolute magnitude (Huertas-Hernando, Guinea, and Brataas, 2006; Min et al., 2006; Boettger and Trickey, 2007; Yao et al., 2007; Gmitra et al., 2009), the energy gap in graphene is likely to be small. Clearly, a better place to look for this physics would be in materials with strong spin-orbit interactions, made from heavy elements near the bottom of the Periodic Table. To this end, Bernevig, Hughes, and Zhang (2006) (BHZ) had the idea to consider quantum well structures of  $\mathrm{HgCdTe}$ . This paved the way to the experimental discovery of the quantum spin Hall insulator phase.

$\mathrm{Hg}_{1 - x}\mathrm{Cd}_x\mathrm{Te}$  is a family of semiconductors with strong spin-orbit interactions (Dornhaus and Nimtz, 1983); CdTe has a band structure similar to other semiconductors. The conduction-band-edge states have an  $s$  -like symmetry, while the valence-band-edge states have a  $p$  -like symmetry. In  $\mathrm{HgTe}$  the  $p$  levels rise above the  $s$  levels, leading to an inverted band structure. BHZ considered a quantum well structure where  $\mathrm{HgTe}$  is sandwiched between layers of CdTe. When the thickness of the  $\mathrm{HgTe}$  layer is  $d < d_{c} = 6.3\mathrm{nm}$  the 2D electronic states bound to the quantum well have the normal band order. For  $d > d_{c}$  however, the 2D bands invert. BHZ showed that the inversion of the bands as a function of increasing  $d$  signals a quantum phase transition between the trivial insulator and the quantum spin Hall insulator. This can be understood simply in the approximation that the system has inversion symmetry. In this case, since the  $s$  and  $p$  states have opposite parity the bands will cross each other at  $d_{c}$  without an avoided crossing. Thus, the energy gap at  $d = d_{c}$  vanishes. From Eq. (12), the change in the parity of the valence-band-edge state signals a phase transition in which the  $\mathbb{Z}_2$  invariant  $\nu$  changes.

Within a year of the theoretical proposal the Würzburg group, led by Laurens Molenkamp, made the devices and performed transport experiments that showed the first signature of the quantum spin Hall insulator. König et al. (2007) measured the electrical conductance due to the edge states. The low-temperature ballistic edge state transport can be understood within a simple Landauer-Büttiker (Büttiker, 1988) framework in

![](images/cda5bdd9671f707750bb2324a05f3a4df9e71cc4b6e12ef0a15731bfea542a7b.jpg)

![](images/6eed81ef93be36d2cd06ccaaaf1a20377962e485483af055d97f790e24bc3e24.jpg)  
FIG. 7. (Color online) Fermi circles in the surface Brillouin zone for (a) a weak topological insulator and (b) a strong topological insulator. (c) In the simplest strong topological insulator the Fermi circle encloses a single Dirac point.

![](images/b2c5dd7a971684a47999e5cd00cf1cef6293adbd8b05b46f5397aca86ecb810d.jpg)  
FIG. 6. (Color online) Experiments on  $\mathrm{HgTe / CdTe}$  quantum wells. (a) Quantum well structure. (b) As a function of layer thickness  $d$  the 2D quantum well states cross at a band inversion transition. The inverted state is the QSHI, which has helical edge states (c) that have a nonequilibrium population determined by the leads. (d) Experimental two terminal conductance as a function of a gate voltage that tunes  $E_{F}$  through the bulk gap. Sample I, with  $d < d_{c}$ , shows insulating behavior, while samples III and IV show quantized transport associated with edge states. Adapted from Konig et al., 2007.

![](images/698ec6565316ba5e4dc7b463d3fc5d04771dc4b8e8d85ed1a87b07a41caa8803.jpg)

which the edge states are populated according to the chemical potential of the lead that they emanate from. This leads to a quantized conductance  $e^2 / h$  associated with each set of edge states. Figure 6(d) shows the resistance measurements for a series of samples as a function of a gate voltage which tunes the Fermi energy through the bulk energy gap. Sample I is a narrow quantum well that has a large resistance in the gap. Samples II-IV are wider wells in the inverted regime. Samples III and IV exhibit a conductance  $2e^2 / h$  associated with the top and bottom edges. Samples III and IV have the same length  $L = 1 \mu \mathrm{m}$  but different widths  $w = 0.5$  and  $1 \mu \mathrm{m}$ , indicating that transport is at the edge. Sample II ( $L = 20 \mu \mathrm{m}$ ) showed finite temperature scattering effects. These experiments convincingly demonstrate the existence of the edge states of the quantum spin Hall insulator. Subsequent experiments have established the inherently non-local electronic transport in the edge states (Roth et al., 2009).

# IV. 3D TOPOLOGICAL INSULATORS

In the summer of 2006 three theoretical groups independently discovered that the topological characterization of the quantum spin Hall insulator state has a natural generalization in three dimensions (Fu, Kane, and Mele, 2007; Moore and Balents, 2007; Roy, 2009b). Moore and Balents (2007) coined the term "topological insulator" to describe this electronic phase. Fu, Kane, and Mele (2007) established the connection between the bulk topological order and the presence of unique con

![](images/df55337622bd9d560d67bf27405ca69bc727e5ff858d8086d178ec7905f0d1e0.jpg)

ducting surface states. Soon after, this phase was predicted in several real materials (Fu and Kane, 2007), including  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$  as well as strained HgTe and  $\alpha$ -Sn. In 2008, Hsieh et al. (2008) reported the experimental discovery of the first 3D topological insulator in  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$ . In 2009 second-generation topological insulators, including  $\mathrm{Bi}_2\mathrm{Se}_3$ , which has numerous desirable properties, were identified experimentally (Xia, Qian, Hsieh, Wray, et al., 2009) and theoretically (Xia, Qian, Hsieh, Wray, et al., 2009; Zhang, Liu, et al., 2009). In this section we review these developments.

# A. Strong and weak topological insulators

A 3D topological insulator is characterized by four  $\mathbb{Z}_2$  topological invariants  $(\nu_{0};\nu_{1}\nu_{2}\nu_{3})$  (Fu, Kane, and Mele, 2007; Moore and Balents, 2007; Roy, 2009b). They can be most easily understood by appealing to the bulk-boundary correspondence, discussed in Sec. II.C. The surface states of a 3D crystal can be labeled with a 2D crystal momentum. There are four  $\mathcal{T}$  invariant points  $\Gamma_{1,2,3,4}$  in the surface Brillouin zone, where surface states, if present, must be Kramers degenerate [Figs. 7(a) and 7(b)]. Away from these special points, the spin-orbit interaction will lift the degeneracy. These Kramers degenerate points therefore form 2D Dirac points in the surface band structure [Fig. 7(c)]. The interesting question is how the Dirac points at the different  $\mathcal{T}$  invariant points connect to each other. Between any pair  $\Gamma_{a}$  and  $\Gamma_{b}$ , the surface-state structure will resemble either Fig. 3(a) or 3(b). This determines whether the surface Fermi surface intersects a line joining  $\Gamma_{a}$  to  $\Gamma_{b}$  an even or an odd number of times. If it is odd, then the surface states are topologically protected. Which of these two alternatives occurred is determined by the four bulk  $\mathbb{Z}_2$  invariants.

The simplest nontrivial 3D topological insulators may be constructed by stacking layers of the 2D quantum spin Hall insulator. This is analogous to a similar construction for 3D integer quantum Hall states (Kohmoto, Halperin, and Wu, 1992). The helical edge states of the layers then become anisotropic surface states. A possible surface Fermi surface for weakly coupled layers stacked along the  $y$  direction is shown in Fig. 7(a). In this figure a single surface band intersects the Fermi energy between  $\Gamma_{1}$  and  $\Gamma_{2}$  and between  $\Gamma_{3}$  and  $\Gamma_{4}$ , leading to the nontrivial connectivity in Fig. 3(b). This layered state is referred to as a weak topological insulator and has  $\nu_{0}$

$= 0$ . The indices  $(\nu_{1}\nu_{2}\nu_{3})$  can be interpreted as Miller indices describing the orientation of the layers. Unlike the 2D helical edge states of a single layer,  $\mathcal{T}$  symmetry does not protect these surface states. Though the surface states must be present for a clean surface, they can be localized in the presence of disorder. Interestingly, however, a line dislocation in a weak topological insulator is associated with protected 1D helical edge states (Ran, Zhang, and Vishwanath, 2009).

$\nu_{0} = 1$  identifies a distinct phase, called a strong topological insulator, which cannot be interpreted as a descent of the 2D quantum spin Hall insulator.  $\nu_{0}$  determines whether an even or an odd number of Kramers points is enclosed by the surface Fermi circle. In a strong topological insulator the surface Fermi circle encloses an odd number of Kramers degenerate Dirac points. The simplest case, with a single Dirac point [Figs. 7(b) and 7(c)], can be described by the Hamiltonian

$$
\mathcal {H} _ {\text {s u r f a c e}} = - i \hbar v _ {F} \vec {\sigma} \cdot \vec {\nabla}, \tag {16}
$$

where  $\vec{\sigma}$  characterizes the spin. (For a surface with a mirror plane, symmetry requires  $\vec{S} \propto \hat{z} \times \vec{\sigma}$ .)

The surface electronic structure of a topological insulator is similar to graphene, except rather than having four Dirac points (2 valley  $\times 2$  spin) there is just a single Dirac point. This appears to violate the fermion doubling theorem (Nielssen and Ninomiya, 1983) discussed in Sec. II.B.2. The resolution is that the partner Dirac points reside on opposite surfaces.

The surface states of a strong topological insulator form a unique 2D topological metal (Fu and Kane, 2007; Fu, Kane, and Mele, 2007) that is essentially half an ordinary metal. Unlike an ordinary metal, which has up and down spins at every point on the Fermi surface, the surface states are not spin degenerate. Since  $\mathcal{T}$  symmetry requires that states at momenta  $\mathbf{k}$  and  $-\mathbf{k}$  have opposite spin, the spin must rotate with  $\mathbf{k}$  around the Fermi surface, as shown in Fig. 7(b). This leads to a nontrivial Berry phase acquired by an electron going around the Fermi circle.  $\mathcal{T}$  symmetry requires that this phase be 0 or  $\pi$ . When an electron circles a Dirac point, its spin rotates by  $2\pi$ , which leads to a  $\pi$  Berry phase.

The Berry phase has important consequences for the behavior in a magnetic field (to be discussed in Sec. V.A) and for the effects of disorder. In particular, in an ordinary 2D electron gas the electrical conductivity decreases with decreasing temperature, reflecting the tendency toward the Anderson localization in the presence of disorder (Lee and Ramakrishnan, 1985). The  $\pi$  Berry phase changes the sign of the weak localization correction to the conductivity leading to weak antilocalization (Suzuura and Ando, 2002). In fact, the electrons at the surface of a strong topological insulator cannot be localized even for strong disorder as long as the bulk energy gap remains intact (Nomura, Koshino, and Ryu, 2007). In this regard, the situation is similar to the edge states of the quantum spin Hall insulator discussed in Sec. III.A; however, the electron motion on the surface is diffusive rather than ballistic.

![](images/ccab064f66878c5296bd4ac8fea3869231fcbc07998bf8799ec4c34cdc6d5030.jpg)  
FIG. 8. (Color online) Schematic representation of the band structure of  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$ , which evolves from semimetallic behavior for  $x < 0.07$  to semiconducting behavior for  $0.07 < x < 0.22$  and back to semimetallic behavior for  $x > 0.18$ . The conduction and valence bands  $L_{s,a}$  invert at  $x \sim 0.04$ .

The Dirac surface states [Eq. (16)] can be understood in a 3D Dirac theory (Qi, Hughes, and Zhang, 2008) where the Dirac mass changes sign at the surface, analogous to Eq. (6). Such domain-wall states were first discussed for  $\mathrm{Pb}_{1 - x}\mathrm{Sn}_x\mathrm{Te}$  (Volkov and Pankratov, 1985; Fradkin, Dagotto, and Boyanovsky, 1986), which exhibits a band inversion as a function of  $x$ . An appropriate interface where  $x$  changes was predicted to have 2D gapless states. There is an important difference between these interface states and the surface states of a topological insulator, though, because the band inversion in  $\mathrm{Pb}_{1 - x}\mathrm{Sn}_x\mathrm{Te}$  occurs at four equivalent valleys. Since four is even, PbTe and SnTe are both trivial insulators. The interface states are not topologically protected from disorder in the sense discussed above. However, if the valleys can be split by applying uniaxial stress, then the topological insulator can occur in the vicinity of the band inversion transition (Fu and Kane, 2007). Related ideas were also applied to interfaces between HgTe and CdTe (Cade, 1985; Chang et al., 1985; Lin-Liu and Sham, 1985; Pankratov, Pakhomov, and Volkov, 1987). In this case, the band inversion occurs in a single valley, but since HgTe is a zero gap semiconductor, the surface states are not protected. Nonetheless, if the cubic symmetry of the bulk HgTe can be lifted by applying uniaxial stress, a gap can be introduced in HgTe, so the HgTe-CdTe interface will have topologically protected states (Fu and Kane, 2007).

# B. The first 3D topological insulator:  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$

The first 3D topological insulator to be identified experimentally was the semiconducting alloy  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$ , whose unusual surface bands were mapped in an angle-resolved photoemission spectroscopy (ARPES) experiment by a Princeton University group led by Hasan (Hsieh et al., 2008).

Bismuth antimony alloys have long been studied for their thermoelectric properties (Lenoir et al., 1996). Pure bismuth is a semimetal with strong spin-orbit interactions. Its band structure, shown schematically in Fig. 8(a), features conduction and valence bands that overlap, leading to pockets of holes near the  $T$  point in the Brillouin zone and pockets of electrons near the three equivalent  $L$  points. The valence and conduction bands at the  $L$  point, derived from antisymmetric  $(L_{a})$  and symmetric  $(L_{s})$  orbitals, have a small energy gap  $\Delta$ . The

TABLE II. Symmetry labels for the Bloch states at the  $8T$  invariant momenta  $\Lambda_{a}$  for the five valence bands of Bi and Sb.  $\delta_{a}$ 's are given by Eq. (12) and determine the topological class  $(\nu_{0};\nu_{1}\nu_{2}\nu_{3})$  by relations similar to Eq. (10). The difference between Bi and Sb is due to the inversion of the  $L_{s}$  and  $L_{a}$  bands that occurs at  $x\sim 0.04$ .  

<table><tr><td colspan="7">Bi: Class (0;000)</td><td colspan="7">Sb: Class (1;111)</td></tr><tr><td>\( {\Lambda }_{a} \)</td><td></td><td colspan="4">Symmetry label</td><td>\( {\delta }_{a} \)</td><td>\( {\Lambda }_{a} \)</td><td></td><td colspan="4">Symmetry label</td><td>\( {\delta }_{a} \)</td></tr><tr><td>\( {1\Gamma } \)</td><td>\( {\Gamma }_{6}^{ + } \)</td><td>\( {\Gamma }_{6}^{-} \)</td><td>\( {\Gamma }_{6}^{ + } \)</td><td>\( {\Gamma }_{6}^{ + } \)</td><td>\( {\Gamma }_{45}^{ + } \)</td><td>-1</td><td>\( {1\Gamma } \)</td><td>\( {\Gamma }_{6}^{ + } \)</td><td>\( {\Gamma }_{6}^{-} \)</td><td>\( {\Gamma }_{6}^{ + } \)</td><td>\( {\Gamma }_{6}^{ + } \)</td><td>\( {\Gamma }_{45}^{ + } \)</td><td>-1</td></tr><tr><td>\( {3L} \)</td><td>\( {L}_{s} \)</td><td>\( {L}_{a} \)</td><td>\( {L}_{s} \)</td><td>\( {L}_{a} \)</td><td>\( {L}_{a} \)</td><td>-1</td><td>\( {3L} \)</td><td>\( {L}_{s} \)</td><td>\( {L}_{a} \)</td><td>\( {L}_{s} \)</td><td>\( {L}_{a} \)</td><td>\( {L}_{s} \)</td><td>+1</td></tr><tr><td>\( {3X} \)</td><td>\( {X}_{a} \)</td><td>\( {X}_{s} \)</td><td>\( {X}_{s} \)</td><td>\( {X}_{a} \)</td><td>\( {X}_{a} \)</td><td>-1</td><td>\( {3X} \)</td><td>\( {X}_{a} \)</td><td>\( {X}_{s} \)</td><td>\( {X}_{s} \)</td><td>\( {X}_{a} \)</td><td>\( {X}_{a} \)</td><td>-1</td></tr><tr><td>\( {1T} \)</td><td>\( {T}_{6}^{-} \)</td><td>\( {T}_{6}^{ + } \)</td><td>\( {T}_{6}^{-} \)</td><td>\( {T}_{6}^{ + } \)</td><td>\( {T}_{45}^{-} \)</td><td>-1</td><td>\( {1T} \)</td><td>\( {T}_{6}^{-} \)</td><td>\( {T}_{6}^{ + } \)</td><td>\( {T}_{6}^{-} \)</td><td>\( {T}_{6}^{ + } \)</td><td>\( {T}_{45}^{-} \)</td><td>-1</td></tr></table>

states near  $L$  have a nearly linear dispersion that is well described by a  $(3 + 1)$ -dimensional Dirac equation (Wolff, 1964) with a small mass. These facts have been used to explain many peculiar properties of bismuth.

Substituting bismuth with antimony changes the critical energies of the band structure [Fig. 8(b)]. At an Sb concentration of  $x \approx 0.04$ , the gap  $\Delta$  between  $L_{a}$  and  $L_{s}$  closes and a truly massless 3D Dirac point is realized. As  $x$  is further increased this gap reopens with an inverted ordering. For  $x > 0.07$  the top of the valence band at  $T$  moves below the bottom of the conduction band at  $L$ , and the material becomes an insulator. Once the band at  $T$  drops below the valence band at  $L$ , at  $x \sim 0.09$ , the system is a direct-gap insulator with a massive Dirac-like bulk bands. As  $x$  is increased further, the conduction and valence bands remain separated, and for  $x \gtrsim 0.22$  the valence band at a different point rises above the conduction band, restoring the semimetallic state.

Since pure bismuth and pure antimony both have a finite direct band gap, their valence bands can be topologically classified. Moreover, since they have inversion symmetry, Eq. (12) can be used to determine the topological indices. Table II shows the symmetry labels that specify the parity of the Bloch states for the occupied bands at the  $8\mathcal{T}$  invariant points in the bulk Brillouin zone (Liu and Allen, 1995). Fu and Kane (2007) used this information to deduce that bismuth is in the trivial (0;000) class while antimony is in the (1;111) class. Since the semiconducting alloy is on the antimony side of the band inversion transition, it is predicted to inherit the (1;111) class from antimony.

Charge transport experiments, which were successful for identifying the 2D topological insulator (König et al., 2007), are problematic in 3D materials because the signature in the conductivity of the topological character of the surface states is more subtle in three dimensions. Moreover, it is difficult to separate the surface contribution to the conductivity from that of the bulk. ARPES is an ideal tool for probing the topological character of the surface states. ARPES uses a photon to eject an electron from a crystal and then determines the surface or bulk electronic structure from an analysis of the momentum of the emitted electron. High-resolution ARPES performed with modulated photon energy allows for a clear isolation of surface states from that of the bulk 3D band structure because surface states do not disperse along a

direction perpendicular to the surface whereas the bulk states do. Moreover, unlike in a transport experiment, ARPES carried out in a spin resolution mode can, in addition, measure the distribution of spin orientations on the Fermi surface which can be used to estimate the Berry phase on the surface. Spin sensitivity is critically important for probing the existence of spin-momentum locking on the surface expected as a consequence of bulk topological order.

Experiments by Hsieh et al. (2008) probed both the bulk and surface electronic structures of  $\mathrm{Bi}_{0.09}\mathrm{Sb}_{0.91}$  with ARPES. Figure 9(a) shows the ARPES spectrum, which can be interpreted as a map of the energy of the occupied electronic states as a function of momentum along the line connecting  $\bar{\Gamma}$  to  $\bar{M}$  in the projected surface Brillouin zone [Fig. 9(b)]. Bulk energy bands associated with the  $L$  point are observed, which reflect the nearly linear 3D Dirac-like dispersion. The same experiments observed several surface states that span the bulk gap.

The observed surface-state structure of  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$  has similarities with the surface states in pure Bi, which have been studied previously (Patthey, Schneider, and Micklitz, 1994; Agergaard et al., 2001; Ast and Hochst, 2001; Hirahara et al., 2006; Hofmann, 2006). In pure Bi, two bands emerge from the bulk band continuum near  $\bar{\Gamma}$  to form a central electron pocket and an adjacent hole lobe. These two bands result from the spin splitting of a surface state and are thus expected to be singly degenerate. In  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$ , there are additional states near  $\bar{M}$  which play a crucial role.

As explained in Sec. IV.A, Kramers' theorem requires surface states to be doubly degenerate at the  $T$  invariant points  $\bar{\Gamma}$  and each of the three equivalent  $\bar{M}$  points. Such a Kramers point is indeed observed at  $\bar{M}$  approximately  $15\pm 5\mathrm{meV}$  below  $E_{F}$ . As expected for a system with strong spin-orbit interactions, the degeneracy is lifted away from  $\bar{M}$ . The observed surface bands cross the Fermi energy five times between  $\bar{\Gamma}$  and  $\bar{M}$ . This odd number of crossings is analogous to Fig. 3(b) and indicates that these surface states are topologically protected. Accounting for the threefold rotational symmetry and mirror symmetry of the (111) surface, these data show that the surface Fermi surface encloses  $\bar{\Gamma}$  an odd

![](images/e711b28adf76bca7c81e24bd17472d2c9b6082ea7f149b9963ae358b81fe26e5.jpg)

![](images/1d2081d8abc489075be47bd4225268807b696c5bafbf30c7a9643b450c2bc135.jpg)  
FIG. 9. (Color online) Topological surface states in  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$ : (a) ARPES data on the (111) surface of  $\mathrm{Bi}_{0.9}\mathrm{Sb}_{0.1}$  which probes the occupied surface states as a function of momentum on the line connecting the  $\mathcal{T}$  invariant points  $\bar{\Gamma}$  and  $\bar{M}$  in the surface Brillouin zone. Only the surface bands cross the Fermi energy five times. This, along with further detailed ARPES results (Hsieh et al., 2008), establishes that the semiconducting alloy  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$  is a strong topological insulator in the (1;111) class. (b) A schematic of the 3D Brillouin zone and its (111) surface projection. (c) The resistivity of semimetallic pure Bi contrasted with the semiconducting alloy. Adapted from Hsieh et al., 2008.

![](images/ad148edc97e1684a7af27f22e3c676976aa94c0c40aa99d221b8c19d9b520ae6.jpg)

number of times, while it encloses the three equivalent  $\bar{M}$  points an even number of times. This establishes  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$  as a strong topological insulator, with  $\nu_{0} = 1$ . The data are consistent with the predicted (1;111) topological class.

A distinguishing feature of topological insulator surface states is the intimate correlation between spin and momentum they exhibit, which underlies the  $\pi$  Berry phase associated with the Fermi surface. Spin resolved ARPES, shown schematically in Fig. 10(a), is ideally suited to probe this physics. Experiments by Hsieh, Xia, Wray, Qian, et al. (2009b) measured the spin polarization of the surface states. These experiments proved that the surface states are indeed nondegenerate and strongly spin polarized [Fig. 10(b)], providing even more decisive evidence for their topological classification. In addition, the spin-polarization data also established the connectivity of the surface state bands above  $E_{F}$  (which is inaccessible to ARPES), showing that bands labeled 2 and 3 in Fig. 9(a) connect to form a hole pocket. Finally, they directly mapped the spin texture of the Fermi surface, providing the first direct evidence for the  $\pi$  Berry phase by showing that the spin polarization rotates by  $360^{\circ}$  around the central Fermi surface, shown in Fig. 10(c). The measurement of the handedness of this rotation

![](images/fb6f0a816a60aaa0bc003d30b14001fab1dae73cdff7d12ffb72261dc27769fb.jpg)  
FIG. 10. (Color online) Topological spin textures: Spin resolved photoemission directly probes the nontrivial spin textures of the topological insulator surface. (a) A schematic of spin-ARPES measurement setup that was used to measure the spin distribution on the (111) surface Fermi surface of  $\mathrm{Bi}_{0.91}\mathrm{Sb}_{0.09}$ . (b) Spin orientations on the surface create a vortexlike pattern around  $\Gamma$  point. A net Berry phase  $\pi$  is extracted from the full Fermi-surface data. (c) Net polarizations along  $x$ ,  $y$ , and  $z$  directions are shown.  $P_z\sim 0$  suggests that spins lie mostly within the surface plane. Adapted from Hsieh, Xia, Wray, Qian, et al., 2009a, 2009b and Hsieh et al., 2010.

provided even more information about the topological structure by probing a mirror Chern number, which agreed favorably with theory (Teo, Fu, and Kane, 2008).

Spin polarized ARPES also enables a similar characterization of surface states in the metallic regime of the  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$  series. Pure Sb is predicted to have a topologically nontrivial valence band despite the semimetallic band overlap. Hsieh, Xia, Wray, Qian, et al. (2009b) found that the surface states of Sb carry a Berry phase and chirality property predicted by theory (Teo, Fu, and Kane, 2008) that is unlike the conventional spin-orbit metals such as gold, which has zero net Berry phase and no net chirality. Additional compositions of the  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$  series provided further evidence for the topological character of the surface states (Nishide et al., 2010). These results demonstrated that ARPES and spin ARPES are powerful probes of topological order.

As discussed in Sec. IV.A the topological surface states are expected to be robust in the presence of non-magnetic disorder and immune from Anderson localization. The origin of this is the fact that  $\mathcal{T}$  symmetry forbids the backscattering between Kramers pairs at  $\mathbf{k}$  and  $-\mathbf{k}$ . Random alloying in  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$  which is not present in other material families of topological insulators found to date, makes this material system an ideal candidate in which to examine the impact of disorder or random potential on topological surface states. The fact that the 2D states are indeed protected from spin-independent scattering was established by Roushan et al. (2009) by combining results from scanning tunneling spectroscopy and spin ARPES. Figure 11 shows the analysis of the inter

![](images/96b31cdc551057dff9d01cb644ca68af990374e60c17ad9f89afa6fc3ef123ad.jpg)  
a

![](images/c12deb32d77fbc37692b26292c42062b9b6b5a33d8ab379a02b101919f6a5666.jpg)  
b

![](images/62f73512ff6e762e47fedb3a307dc258707d8d7168570232fe7b58cbc46c30df.jpg)  
C

![](images/a4f46a78f8b6cc249b50eea117ca1a7bc4be49cf730b0bfb2af90ad307ba20a4.jpg)  
d  
f

![](images/4a05a258f09555131e0b4b2987d55a6e2d3eaf80b0b3c0f0274a5ac380a4caba.jpg)  
e  
FIG. 11. (Color online) Absence of backscattering: Quasiparticle interference observed at the surface of  $\mathrm{Bi}_{0.92}\mathrm{Sb}_{0.08}$  exhibits the absence of elastic backscattering. (a) Spatially resolved conductance maps of the (111) surface obtained at  $0\mathrm{mV}$  over a  $1000\AA \times 1000\AA$ . (b) Spin-ARPES map of the surface state measured at the Fermi level. The spin textures from spin-ARPES measurements are shown with arrows. (c) Fourier transform scanning tunneling spectroscopy (FT-STS) at  $E_{F}$ . (d) The joint density of states (JDOS) at  $E_{F}$ . (e) The spin-dependent scattering probability (SSP) at  $E_{F}$ . (f) Closeup of the JDOS, FT-STS, and SSP at  $E_{F}$ , along the  $\Gamma - M$  direction. Adapted from Hsieh, Xia, Wray, Qian, et al., 2009b and Roushan et al., 2009.

![](images/c3b24b807f8dd207e22643fffaae095bfb700b82cbc1a3618f83c1ed81629021.jpg)

ference pattern due to scattering at the surface. Figure 11(c) shows the Fourier transform of the observed pattern [Fig. 11(a)], while Figs. 11(d) and 11(e) show the joint density of states computed from the Fermi surface [Fig. 11(b)] with and without a suppression of  $\mathbf{k}$  to  $-\mathbf{k}$  backscattering. The similarity between Figs. 11(c) and 11(e) shows that despite strong atomic scale disorder,  $\mathbf{k}$  to  $-\mathbf{k}$  backscattering is absent. Similar conclusions have emerged from studies of the electronic interference patterns near defects or steps on the surface in other topological insulators (Urazhdin et al., 2004; Zhang, Cheng, et al., 2009; Alpichshev et al., 2010). In graphene there is an approximate version of this protection if the disorder has a smooth potential which does not mix the valleys at  $\mathbf{K}$  and  $\mathbf{K}'$ , but real graphene will become localized with strong disorder (Castro Neto et al., 2009).

# C. Second generation materials:  $\mathrm{Bi}_2\mathrm{Se}_3$ ,  $\mathrm{Bi}_2\mathrm{Te}_3$ , and  $\mathrm{Sb}_2\mathrm{Te}_3$

The surface structure of  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$  was rather complicated and the band gap was rather small. This motivated a search for topological insulators with a larger band gap and simpler surface spectrum. A second generation of 3D topological insulator materials (Moore, 2009), especially  $\mathrm{Bi}_2\mathrm{Se}_3$ , offers the potential for topologically protected behavior in ordinary crystals at room temperature and zero magnetic field. In 2008, work by the Princeton group used ARPES and first-principles calculations to study the surface band structure of  $\mathrm{Bi}_2\mathrm{Se}_3$  and observe the characteristic signature of a topological insulator in the form of a single Dirac cone (Xia, Qian, Hsieh, Wray, et al., 2009). Concurrent theoretical work by Zhang, Liu, et al. (2009) used electronic structure methods to show that  $\mathrm{Bi}_2\mathrm{Se}_3$  is just one of several new large band-gap topological insulators. Zhang, Liu, et al. (2009) also provided a simple tight-binding model to capture the single Dirac cone observed in these materials. Detailed and systematic surface investigations of  $\mathrm{Bi}_2\mathrm{Se}_3$  (Hor et al., 2009; Hsieh, Xia, Qian, Wray, et al., 2009a; Park et al., 2010),  $\mathrm{Bi}_2\mathrm{Te}_3$  (Chen et al., 2009; Hsieh, Xia, Qian, Wray, et al., 2009a, 2009b; Xia, Qian, Hsieh, Shankar, et al., 2009), and  $\mathrm{Sb}_2\mathrm{Te}_3$  (Hsieh, Xia, Qian, Wray, et al., 2009b) confirmed the topological band structure of these three materials. This also explained earlier puzzling observations on  $\mathrm{Bi}_2\mathrm{Te}_3$  (Noh et al., 2008). These works showed that the topological insulator behavior in these materials is associated with a band inversion at  $\mathbf{k} = 0$ , leading to the (1;000) topological class. The (1;000) phase observed in the  $\mathrm{Bi}_2\mathrm{Se}_3$  series differs from the (1;111) phase in  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$  due to its weak topological invariant, which has implications for the behavior of dislocations (Ran, Zhang, and Vishwanath, 2009).

Though the phase observed in the  $\mathrm{Bi}_{2}\mathrm{Se}_{3}$  class has the same strong topological invariant  $\nu_{0} = 1$  as  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_{x}$ , there are three crucial differences that suggest that this series may become the reference material for future experiments. The  $\mathrm{Bi}_{2}\mathrm{Se}_{3}$  surface state is found from ARPES and theory to be a nearly idealized single Dirac cone as seen from the experimental data in Figs. 12, 13, and 16. Second,  $\mathrm{Bi}_{2}\mathrm{Se}_{3}$  is stoichiometric (i.e., a pure compound rather than an alloy such as  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_{x}$ ) and hence can be prepared, in principle, at higher purity. While the topological insulator phase is predicted to be quite robust to disorder, many experimental probes of the phase, including ARPES of the surface band structure, are clearer in high-purity samples. Finally and perhaps most important for applications,  $\mathrm{Bi}_{2}\mathrm{Se}_{3}$  has a large band gap of  $\sim 0.3\mathrm{eV}$  (3600 K). This indicates that in its high-purity form  $\mathrm{Bi}_{2}\mathrm{Se}_{3}$  can exhibit topological insulator behavior at room temperature (Fig. 13) and greatly increases the potential for applications. To understand the likely impact of these new topological insulators, an analogy can be drawn with the early days of high-temperature cuprate superconductivity: the original cuprate superconductor LBCO was quickly superseded by second-generation materials such as YBCO and BSCCO for most applied and scientific purposes.

![](images/afe7d16f49dc854db5b839bff2f9a6b61359a5a740096efd8460cec3aacd1204.jpg)

![](images/4c2841d9b6e5b4c1f1e22d392b0378051f67fa806a63c0768dc12ab95612e1cc.jpg)

![](images/fc8a70d00df610ebfd970ca9f23fedef06a02fbe8a2939df9540d91654888ef7.jpg)  
FIG. 12. (Color online) Helical fermions: Spin-momentum locked helical surface Dirac fermions are hallmark signatures of topological insulators. (a) ARPES data for  $\mathrm{Bi}_{2}\mathrm{Se}_{3}$  reveal surface electronic states with a single spin-polarized Dirac cone. (b) The surface Fermi surface exhibits a chiral left-handed spin texture. (c) Surface electronic structure of  $\mathrm{Bi}_{2}\mathrm{Se}_{3}$  computed in the local-density approximation. The shaded regions describe bulk states, and the lines are surface states. (d) Schematic of the spin-polarized surface-state dispersion in  $\mathrm{Bi}_{2}X_{3}$  (1;000) topological insulators. Adapted from Xia et al., 2008, Hsieh, Xia, Qian, Wray, et al., 2009a, and Xia, Qian, Hsieh, Wray, et al., 2009.

![](images/1fcb4c8454b2a7690b1a2fb1e91c133d5fee688e11bf764fb0fe6e685646c1da.jpg)

All key properties of topological states have been demonstrated for  $\mathrm{Bi}_{2}\mathrm{Se}_{3}$  which has the simplest Dirac cone surface spectrum and the largest band gap. In  $\mathrm{Bi}_{2}\mathrm{Te}_{3}$  the surface states exhibit large deviations from a simple Dirac cone (Fig. 14) due to a combination of smaller band gap  $(0.15\mathrm{eV})$  and a strong trigonal potential (Chen et al., 2009), which can be utilized to explore some aspects of its surface properties (Fu, 2009; Hasan, Lin, and Bansil, 2009). The hexagonal deformation of the surface states is confirmed by scanning tunneling microscopy (STM) measurements (Alpichshev et al., 2010); Fig. 14. Speaking of applications within this class of materials,  $\mathrm{Bi}_{2}\mathrm{Te}_{3}$  is already well known to materials scientists working on thermoelectricity. It is a commonly used thermoelectric material in the crucial engineering regime near room temperature.

Two defining properties of topological insulators—spin-momentum locking of surface states and  $\pi$  Berry phase—can be clearly demonstrated in the  $\mathrm{Bi}_{2}\mathrm{Se}_{3}$  series. The surface states are expected to be protected by  $\mathcal{T}$  symmetry which implies that the surface Dirac node should be robust in the presence of nonmagnetic disorder but open a gap in the presence of  $\mathcal{T}$  breaking perturbations. Magnetic impurities such as Fe or Mn on the surface of  $\mathrm{Bi}_{2}\mathrm{Se}_{3}$  open a gap at the Dirac point [Figs. 15(a) and 15(b)] (Xia et al., 2008; Hsieh, Xia, Qian, Wray, et al., 2009a; Hor, Roushan, et al., 2010; Wray et al., 2010). The magnitude of the gap is likely set by the interaction of Fe ions with the Se surface and the  $\mathcal{T}$  break

![](images/bfc409f34d0acf70b01d98539e5bbd3ec048a9b5e472801965d0d9e7f33977a0.jpg)

![](images/d7aeedebdd5f6794a043f31da3151ac71effa1f0a9db7854093595e811c03766.jpg)  
FIG. 13. (Color online) Room temperature topological order in  $\mathrm{Bi}_2\mathrm{Se}_3$ : (a) Crystal momentum integrated ARPES data near Fermi level exhibit linear falloff of density of states, which combined with the spin-resolved nature of the states suggest that a half Fermi gas is realized on the topological surfaces. (b) Spin-texture map based on spin-ARPES data suggest that the spin chirality changes sign across the Dirac point. (c) The Dirac node remains well defined up a temperature of  $300\mathrm{K}$  suggesting the stability of topological effects up to the room temperature. (d) The Dirac cone measured at a temperature of  $10\mathrm{K}$ . (e) Full Dirac cone. Adapted from Hsieh, Xia, Qian, Wray, et al., 2009a.

ing disorder potential introduced on the surface. Non-magnetic disorder created via molecular absorbent  $\mathrm{NO}_2$  or alkali atom adsorption (K or Na) on the surface leaves the Dirac node intact [Figs. 15(c) and 15(d)] in both  $\mathrm{Bi}_2\mathrm{Se}_3$  and  $\mathrm{Bi}_2\mathrm{Te}_3$  (Hsieh, Xia, Qian, Wray, et al., 2009a; Xia, Qian, Hsieh, Shankar, et al., 2009). These results are consistent with the fact that the topological

![](images/be73e7cc64a06b517bd3e1711630cb2958daf3c4a13660d5fba69218c4eb7b36.jpg)  
FIG. 14. (Color online) Hexagonal warping of surface states in  $\mathrm{Bi}_2\mathrm{Te}_3$ : ARPES and STM studies of  $\mathrm{Bi}_2\mathrm{Te}_3$  reveal a hexagonal deformation of surface states. Fermi-surface evolution with increasing  $n$ -type doping as observed in ARPES measurements. Adapted from Alpichshev et al., 2010.

![](images/a2d6a63169d650606fdc2ddce816df5a3fdb102321daebd4f9aeb97ff2c062e2.jpg)  
FIG. 15. (Color online) Protection by time-reversal symmetry: Topological surface states are robust in the presence of strong nonmagnetic disorder but open a gap in the presence of  $\mathcal{T}$  breaking magnetic impurities and disorder. (a) Magnetic impurity such as Fe on the surface of  $\mathrm{Bi}_2\mathrm{Se}_3$  opens a gap at the Dirac point. The magnitude of the gap is set by the interaction of Fe ions with the Se surface and the  $\mathcal{T}$  breaking disorder potential introduced on the surface. (b) A comparison of surface band dispersion with and without Fe doping. (c) and (d) Nonmagnetic disorder created via molecular absorbent  $\mathrm{NO}_2$  or alkali atom adsorption (K or Na) on the surface leaves the Dirac node intact in both  $\mathrm{Bi}_2\mathrm{Se}_3$  and  $\mathrm{Bi}_2\mathrm{Te}_3$ . Adapted from Hsieh, Xia, Qian, Wray, et al., 2009a, Xia, Qian, Hsieh, Shankar, et al., 2009, and Wray et al., 2010.

surface states are protected by  $\mathcal{T}$  symmetry.

Many of the interesting theoretical proposals that utilize topological insulator surfaces require the chemical potential to lie at or near the surface Dirac point. This is similar to the case in graphene, where the chemistry of carbon atoms naturally locates the Fermi level at the Dirac point. This makes its density of carriers highly tunable by an applied electrical field and enables applications of graphene to both basic science and microelectronics. The surface Fermi level of a topological insulator depends on the detailed electrostatics of the surface and is not necessarily at the Dirac point. Moreover, for naturally grown  $\mathrm{Bi}_2\mathrm{Se}_3$  the bulk Fermi energy is not even in the gap. The observed  $n$ -type behavior is believed to be caused Se vacancies. By appropriate chemical modifications, however, the Fermi energy of both the bulk and the surface can be controlled. This allowed Hsieh, Xia, Qian, Wray, et al. (2009a) to reach the sweet spot in which the surface Fermi energy is tuned to the Dirac point (Fig. 16). This was achieved by doping bulk with a small concentration of Ca, which compensates the Se vacancies, to place the Fermi level within the bulk band gap. The surface was hole doped by exposing the surface to  $\mathrm{NO}_2$  gas to place the Fermi level at the Dirac point.

The main remaining complication with these materials, especially for experimental techniques that (unlike ARPES) do not distinguish directly between bulk and surface states, is that they have some residual conduc

![](images/d82b2af3f97dbf7b96b29e29928966b3bb5fee22d19087b48043db46ac7e912a.jpg)  
FIG. 16. (Color online) Chemical gating a topological surface to the spin-degenerate point: Topological insulator surfaces are most interesting if the chemical potential can be placed at the Dirac node without intercepting any bulk band. This can be achieved in  $\mathrm{Bi}_2\mathrm{Se}_3$  via the chemical tailoring of the surface or using electrical gating methods. (a) Evolution of surface Fermi surface with increasing  $\mathrm{NO}_2$  adsorption on the surface.  $\mathrm{NO}_2$  extracts electrons from the  $\mathrm{Bi}_2\mathrm{Se}_3$  surface leading to an effective hole doping of the material. (b) Chemical gating of the surface can be used to place the chemical potential at the spindegenerate Dirac point. Adapted from Hsieh, Xia, Qian, Wray, et al., 2009a.

tion in the bulk from impurity or self-doping states. Electrical transport measurements on  $\mathrm{Bi}_2\mathrm{Se}_3$  show that doping with a small concentration of Ca leads to insulating behavior. Figure 17(a) shows the resistivity of several samples with varying Ca concentrations. For  $0.002 < x < 0.025$ , the resistivity shows a sharp upturn below  $100\mathrm{K}$  before saturating. The low-temperature resistivity

![](images/166f1b471067e3205d665d63440b40b9ecd1d6318a041bf63159ed0436e617d2.jpg)  
FIG. 17. (Color online) Electrical transport in  $\mathrm{Bi}_{2}\mathrm{Se}_{3}$ . (a) Resistivity for samples of pure  $\mathrm{Bi}_{2}\mathrm{Se}_{3}$  doped with a small concentration of Ca. Increasing the Ca concentration moves the Fermi level from the conduction band into the gap and then to the valence band. Samples with  $0.002 < x < 0.0025$ , labeled G, show insulating behavior below  $100\mathrm{K}$  (Checkelsky et al., 2009). (b)  $\mathrm{Bi}_{2}\mathrm{Se}_{3}$  doped with Cu shows superconducting behavior below  $3.8\mathrm{K}$  for  $x = .12$ . The inset shows the magnetic susceptibility which exhibits the Meissner effect. Adapted from Hor, Williams, et al., 2010 and Wray et al., 2010.

is still too small to be explained by the surface states alone. However, the low-temperature transport exhibits interesting 2D mesoscopic effects that are not completely understood (Checkelsky et al., 2009). Doping  $\mathrm{Bi}_{2}\mathrm{Se}_{3}$  with copper leads to a metallic state that shows superconducting behavior [Fig. 17(b)] below  $3.8\mathrm{K}$  (Wray et al., 2009; Hor, Williams, et al., 2010). This has important ramifications for some of the devices proposed in Sec. IV.

# V. EXOTIC BROKEN SYMMETRY SURFACE PHASES

Now that the basic properties of topological insulators have been established, we may ask what can be done with them. In this section we argue that the unique properties of topological insulator surface and edge states are most dramatic if an energy gap can be induced in them. This can be done by breaking  $\mathcal{T}$  symmetry with an external magnetic field (Fu and Kane, 2007) or proximity to a magnetic material (Qi, Hughes, and Zhang, 2008), by breaking gauge symmetry due to proximity to a superconductor (Fu and Kane, 2008), or by an excitonic instability of two coupled surfaces (Seradjeh, Moore, and Franz, 2009). In this section we review the magnetic and superconducting surface phases.

# A. Quantum Hall effect and topological magnetoelectric effect

# 1. Surface quantum Hall effect

A perpendicular magnetic field will lead to Landau levels in the surface electronic spectrum and the quantum Hall effect. The Landau levels for Dirac electrons are special, however, because a Landau level is guaranteed to exist at exactly zero energy (Jackiw, 1984). This zero Landau level is particle-hole symmetric in the sense that the Hall conductivity is equal and opposite when the Landau level is full or empty. Since the Hall conductivity increases by  $e^2 / h$  when the Fermi energy crosses a Landau level the Hall conductivity is half integer quantized (Zheng and Ando, 2002),

$$
\sigma_ {x y} = (n + 1 / 2) e ^ {2} / h. \tag {17}
$$

This physics has been demonstrated in experiments on graphene (Novoselov et al., 2005; Zhang et al., 2005). However, there is an important difference. In graphene Eq. (17) is multiplied by 4 due to the spin and valley degeneracy of graphene's Dirac points, so the observed Hall conductivity is still integer quantized. At the surface of the topological insulator there is only a single Dirac point. Such a "fractional" integer quantized Hall effect should be a cause for concern because the integer quantized Hall effect is always associated with chiral edge states, which can only be integer quantized. The resolution is the mathematical fact that a surface cannot have a boundary. In a slab geometry shown in Fig. 18(a), the top and bottom surfaces are necessarily connected to each other and will always be measured in parallel (Fu and Kane, 2007), doubling the  $1/2$ . The top and bottom

![](images/840b63bd63c89b728e13749e8c277462fb9970cd49258ab31bf86c6789dc7b77.jpg)  
FIG. 18. (Color online) Surface quantum Hall effect. (a) The Dirac spectrum is replaced by Landau levels in an orbital magnetic field. (b) The top and bottom surfaces share a single chiral fermion edge mode. (c) A thin magnetic film can induce an energy gap at the surface. (d) A domain wall in the surface magnetization exhibits a chiral fermion mode.

can share a single chiral edge state, which carries the integer quantized Hall current.

A related surface quantum Hall effect, called the anomalous quantum Hall effect, can be induced with the proximity to a magnetic insulator. A thin magnetic film on the surface of a topological insulator will give rise to a local exchange field that lifts the Kramers degeneracy at the surface Dirac points. This introduces a mass term  $m$  into the Dirac equation [Eq. (16)], as in Eq. (4). If the  $E_{F}$  is in this energy gap, there is a half integer quantized Hall conductivity  $\sigma_{xy} = e^{2} / 2h$  (Pankratov, 1987), as discussed in Sec. II.B.2. This can be probed in a transport experiment by introducing a domain wall into the magnet. The sign of  $m$  depends on the direction of the magnetization. At an interface where  $m$  changes sign [Fig. 18(d)] there will be a 1D chiral edge state, analogous to unfolding the surface in Fig. 18(b).

# 2. Topological magnetoelectric effect and axion electrodynamics

The surface Hall conductivity can also be probed without the edge states either by optical methods or by measuring the magnetic field produced by surface currents. This leads to an intriguing topological magnetoelectric effect (Qi, Hughes, and Zhang, 2008; Essin, Moore, and Vanderbilt, 2009). Imagine a cylindrical topological insulator with magnetically gapped surface states and an electric field  $\mathbf{E}$  along its axis. The azimuthal surface Hall current  $(e^2 /2h)|\mathbf{E}|$  leads to a magnetic-dipole moment associated with a magnetization  $\mathbf{M} = \alpha \mathbf{E}$ , where the magnetoelectric polarizability is given by  $\alpha = e^{2} / 2h$

A field theory for this magnetoelectric effect can be developed by including a  $\theta$  term in the electromagnetic Lagrangian, which has a form analogous to the theory of axion electrodynamics that has been studied in particle physics contexts (Wilczek, 1987),

$$
\Delta \mathcal {L} = \theta \left(e ^ {2} / 2 \pi h\right) \mathbf {E} \cdot \mathbf {B}. \tag {18}
$$

The field  $\theta$ , which is a dynamical variable in the axion theory, is a constant  $\pi$  in the topological insulator. Importantly, when expressed in terms of the vector potential  $\mathbf{E} \cdot \mathbf{B}$  is a total derivative, so a constant  $\theta$  has no effect on the electrodynamics. However, a gapped interface, across which  $\theta$  changes by  $\Delta \theta$ , is associated with a surface Hall conductivity  $\sigma_{xy} = \Delta \theta e^2 / (2\pi h)$ .

As in the axion theory, the action corresponding to Eq. (18) is invariant under  $\theta \rightarrow \theta + 2\pi$ . Physically, this reflects the fact that an integer quantum Hall state with  $\sigma_{xy} = ne^2 / h$  can exist at the surface without changing the bulk properties (Essin, Moore, and Vanderbilt, 2009). This resembles a similar ambiguity in the electric polarization. Qi, Hughes, and Zhang (2008) showed that since  $\mathbf{E} \cdot \mathbf{B}$  is odd under  $\mathcal{T}$ , only  $\theta = 0$  or  $\pi$  are consistent with  $\mathcal{T}$  symmetry, so  $\theta$  is quantized. By computing the magnetoelectric response perturbatively,  $\theta$  can be computed in a manner similar to the Kubo formula calculation of  $\sigma_{xy}$ .  $\theta / \pi$  is identical to  $\nu_0$ , the invariant characterizing a strong topological insulator.

Observation of the surface currents associated with this magnetoelectric effect will be an important complement to the ARPES experiments. It should be emphasized, however, that despite the topologically quantized status of  $\theta$ , the surface currents are not quantized the way edge state transport currents are quantized in the quantum Hall effect. The surface currents are bound currents, which must be distinguished from other bound currents that may be present. Nonetheless, it may be possible to account for such effects, and signatures of  $\theta$  will be interesting to observe. Qi, Li, et al. (2009) pointed out that a consequence of a nonzero surface  $\sigma_{xy}$  is that an electric charge outside the surface gives rise to a pattern of surface currents that produces a magnetic field the same as that of an image magnetic monopole.

# B. Superconducting proximity effect

Combining topological insulators with ordinary superconductors leads to a correlated interface state that, such as a topological superconductor, is predicted to host Majorana fermion excitations. In this section we begin by reviewing the properties of Majorana fermion excitations and the proposal by Kitaev (2003) to use those properties for fault tolerant quantum information processing. We then describe methods for engineering Majorana fermions in superconductor-topological insulator devices and prospects for their experimental observation.

# 1. Majorana fermions and topological quantum computing

As discussed in Sec. II.D.2, a well-separated pair of Majorana bound states defines a degenerate two-level system—a qubit. Importantly, the quantum information in the qubit is stored nonlocally. The state cannot be measured with a local measurement on one of the bound states. This is crucial because the main difficulty with

![](images/9564d268a450a3cb3fbddf10453ef931a0027bfb90e76144aba711a6220a117b.jpg)  
FIG. 19. (Color online) A simple operation in which two vortices are exchanged. The vortex pairs 12 and 34 are created in the vacuum (zero quasiparticle) state. When they are brought back together they are in an entangled superposition of 0 and 1 quasiparticle states.

making a quantum computer is preventing the system from accidentally measuring itself. The  $2N$  Majorana bound states define  $N$  qubits a quantum memory.

Adiabatically interchanging the vortices or more generally braiding them leads to the phenomenon of non-Abelian statistics (Moore and Read, 1991). Such processes implement unitary operations on the state vector  $|\psi_{a}\rangle \rightarrow U_{ab}|\psi_{b}\rangle$  that generalize the usual notion of Fermi and Bose quantum statistics (Nayak and Wilczek, 1996; Ivanov, 2001). These operations are precisely what a quantum computer is supposed to do. A quantum computation will consist of three steps, depicted in Fig. 19.

(i) Create: If a pair  $i,j$  of vortices is created, they will be in the ground state  $\left|0_{ij}\right\rangle$  with no extra quasiparticle excitations. Creating  $N$  pairs initializes the system.  
(ii) Braid: Adiabatically rearranging the vortices modifies the state and performs a quantum computation.  
(iii) Measure: Bringing vortices  $i$  and  $j$  back together allows the quantum state associated with each pair to be measured.  $|1_{ij}\rangle$  and  $|0_{ij}\rangle$  will be distinguished by the presence or absence of an extra fermionic quasiparticle associated with the pair.

Though the quantum operations allowed by manipulating the Majorana states do not have sufficient structure to construct a universal quantum computer (Freedman, Larsen, and Wang, 2002), the topological protection of the quantum information makes the experimental observation of Majorana fermions and non-Abelian statistics a high priority in condensed-matter physics (Nayak et al., 2008). Current experimental efforts have focused on the  $\nu = 5 / 2$  quantum Hall state, where interferometry experiments (Das Sarma, Freedman, and Nayak, 2005; Stern and Halperin, 2006) can, in principle, detect the non-Abelian statistics predicted for the quasiparticles. Though recent experiments on the quantum Hall effect have shown encouraging indirect evidence for these states (Dolev et al., 2008; Radu et al., 2008; Willett, Pfeiffer, and West, 2009), definitive observation of the Majorana states has remained elusive. In Sec. V.B.2 we describe the possibility of realizing these

states in topological insulator-superconductor structures. The large energy scale associated with the energy gap in  $\mathrm{Bi}_2\mathrm{Se}_3$  may provide an advantage, so the required temperature scale will be limited only by the superconductor.

# 2. Majorana fermions on topological insulators

Consider an interface between a topological insulator and an  $s$  wave superconductor. Due to the superconducting proximity effect, Cooper pairs may tunnel from the superconductor to the surface, leading to an induced superconducting energy gap in the surface states. The resulting 2D superconducting state is different from an ordinary superconductor because the surface states are not spin degenerate and contain only half the degrees of freedom of a normal metal. The superconducting state resembles the spinless  $p_x + ip_y$  topological superconductor discussed in Sec. II.D, which is also based on a spin nondegenerate Fermi surface. Unlike the  $p_x + ip_y$  superconductor, the surface superconductor does not violate  $\mathcal{T}$  symmetry, and its Cooper pairs have even parity. The minus sign required by Fermi statistics is supplied by the  $\pi$  Berry phase of the surface states. Like the  $p_x + ip_y$  superconductor, the surface superconductor will have a zero energy Majorana state bound to a vortex (Fu and Kane, 2008). Similar zero modes were later found for superconducting graphene (Ghaemi and Wilczek, 2007; Bergman and Le Hur, 2009), though those modes were intrinsically doubled. Undoubted Majorana bound states were found earlier by Jackiw and Rossi (1981) in a related field theory model that had an extra chiral symmetry. Interestingly, the Majorana states on a topological insulator emerge as solutions to a 3D BdG theory, so there is a sense in which their non-Abelian statistics is inherently three dimensional (Teo and Kane, 2010).

Majorana states can, in principle, be engineered and manipulated using junctions of superconductors on the surface of a topological insulator (Fu and Kane, 2008). If the phases on three superconductors that meet at a trijunction [Fig. 20(b)] are arranged such that  $(\phi_{1},\phi_{2},\phi_{3}) = (0,2\pi /3,4\pi /3)$ , then a vortex is simulated, and a zero mode will be bound to the junction. If the phases are changed, the zero mode cannot disappear until the energy gap along one of the three linear junctions goes to zero. This occurs when the phase difference across the junction is  $\pi$ . At this point the Majorana bound state moves to the other end of the linear junction. Combining these trijunctions into circuits connected by linear junctions could then allow for the create-braid-measure protocol discussed in Sec. V.B.1 to be implemented. The state of two Majorana modes brought together on a linear junction can be probed by measuring the supercurrent across that junction.

There are many hurdles to overcome before this ambitious proposal can be realized. The first step is finding a suitable superconductor that makes good contact with a topological insulator. Probing the signatures of Majorana fermions and non-Abelian statistics will require

![](images/3d35c0e262c1a1f612a48b219a1f622e2ef8fd817e4bd0b11c335eeb3c67114f.jpg)

![](images/44438f540741a7d1ff6719f70645b12bfe01782bbecbfc813b82e61ecb7542dc.jpg)

![](images/8b544b48b070bdb6c3aa63a892561f53c8f6eac7d42b84492b8ff581ace09b3b.jpg)  
FIG. 20. (Color online) Majorana fermions on topological insulators. (a) A superconducting vortex or antidot with flux  $h / 2e$  on a topological insulator is associated with a Majorana zero mode. (b) A superconducting trijunction on a topological insulator. Majorana modes at the junction can be controlled by adjusting the phases  $\phi_{1,2,3}$ . 1D chiral Majorana modes exist at a superconductor-magnet interface on a topological insulator. (c) A 1D chiral Dirac mode on a magnetic domain wall that splits into two chiral Majorana modes around a superconducting island. When  $\Phi = h / 2e$  interference of the Majorana modes converts an electron into a hole. (d) Majorana modes at a superconductor-magnet junction on a 2D QSHI.

![](images/e31aee05cf33c89c64de56ff584b5b948427e7f89e98a9382cad0f118a2e3c59.jpg)

ingenuity—what makes them good for quantum computing makes them hard to measure. A first step would be to detect the Majorana state at a vortex, antidot, or trijunction by tunneling into it from a normal metal. A signature of the zero mode would be a zero-bias anomaly, which would have a characteristic current-voltage relation (Bolech and Demler, 2007; Law, Lee, and Ng, 2009).

Another venue for Majorana fermions on a topological insulator surface is a linear interface between superconducting and magnetically gapped regions (Fu and Kane, 2008; Tanaka, Yokoyama, and Nagaosa, 2009; Linder et al., 2010). This leads to a 1D chiral Majorana mode, analogous to the edge state of a 2D topological superconductor [Fig. 4(e)]. This can be used to construct a novel interferometer for Majorana fermions (Akhmerov, Nilsson, and Beenakker, 2009; Fu and Kane, 2009b). Figure 20(c) shows a superconducting island surrounded by magnetic regions with a magnetic domain wall. The chiral Dirac fermions on the magnetic domain wall incident from the left split into two chiral Majorana fermions on opposite sides of the superconductor and then recombine. If the superconductor encloses a flux  $\Phi = h / 2e$ , then the Majorana fermions pick up a relative minus sign analogous to the Aharonov-Bohm effect. This has the effect of converting an incident electron into an outgoing hole, with a Cooper pair of electrons absorbed by the superconductor. This could be observed in a three terminal transport setup.

Majorana bound states can also be engineered at the edge of a 2D quantum spin Hall insulator utilizing magnetic and superconducting energy gaps [Fig. 20(d)] (Nilsson, Akhmerov, and Beenakker, 2008; Fu and Kane, 2009a). This and other geometries can, in principle, be used to test the inherent nonlocality of Majorana fermion states (Fu, 2010)

# VI. CONCLUSION AND OUTLOOK

Though the basic properties of topological insulators have been established, the field is at an early stage in its development. There is much work to be done to realize the potential of these new and fascinating materials. In this concluding section we discuss some recent developments and look toward the future.

In the history of condensed-matter physics, the single most important ingredient in the emergence of a new field is the perfection of the techniques for producing high quality materials. For example, the intricate physics of the fractional quantum Hall effect would never have emerged without ultrahigh mobility GaAs. Topological insulator materials need to be perfected so that they actually insulate. There has been substantial progress in this direction. For instance, transport experiments on Ca-doped crystals of  $\mathrm{Bi}_{2}\mathrm{Se}_{3}$  show clear insulating behavior below around  $100\mathrm{K}$  (Checkelsky et al., 2009). However, the electrical resistance saturates at low temperature and the surface currents appear to be overwhelmed by either bulk currents or currents in a layer near the surface. This is a challenging problem because narrow gap semiconductors are very sensitive to doping. Nonetheless, it seems clear that there is ample room for improvement. Thin films produced, for instance, by mechanical exfoliation (as in graphene), or catalytically generated  $\mathrm{Bi}_{2}\mathrm{Se}_{3}$  ribbons and wires (Peng et al., 2010) may be helpful in this regard. A particularly promising new direction is the growth of epitaxial films of  $\mathrm{Bi}_{2}\mathrm{Se}_{3}$  (Zhang et al., 2009, 2010) and  $\mathrm{Bi}_{2}\mathrm{Te}_{3}$  (Li et al., 2009). This has led to the recent observation of Landau quantization in the Dirac surface states (Cheng et al., 2010; Hanaguri et al., 2010). It will be interesting to observe such quantization in a transport study. Present materials pose a challenge due to competition between surface and bulk states (Checkelsky et al., 2009; Taskin and Ando, 2009). The detailed study of the electronic and spin transport properties of the surface states is called for, complemented by a host of other probes, ranging from optics to tunneling spectroscopy.

Another direction for future innovation will be the study of heterostructures involving topological insulators and other materials. In addition to providing a means for protecting and controlling the population of the surface states, such structures could provide a step toward the longer term goal of engineering exotic states, such as Majorana fermions, with the surface states. There are many material problems to be solved in order to find appropriate magnetic and superconducting materials which exhibit the appropriate proximity effects with the surface states, and detailed experiments will be necessary to characterize those states. A recent development along these lines is the discovery of superconductivity in Cu-doped  $\mathrm{Bi}_{2}\mathrm{Se}_{3}$  (Hor, Williams, et al., 2010). One can imagine devices fabricated with techniques of modulation doping that have proved extremely powerful in semiconductor physics. One can also imagine other devices that integrate magnetic materials with topological

insulators to take advantage of the special spin properties of the surface states.

Topological insulating behavior is likely to arise in other classes of materials in addition to the binary compounds  $\mathrm{Bi}_{1 - x}\mathrm{Sb}_x$ ,  $\mathrm{Bi}_2\mathrm{Te}_3$ ,  $\mathrm{Bi}_2\mathrm{Se}_3$ , and  $\mathrm{Sb}_2\mathrm{Te}_3$ . If one expands ones horizon to ternary compounds (or beyond) the possibilities for exotic materials multiply. Candidate materials will be narrow gap semiconductors which include heavy elements. One intriguing class of materials is transition-metal oxides involving iridium. Shitade et al. (2009) predicted that  $\mathrm{Na}_2\mathrm{IrO}_3$  is a weak topological insulator. Pesin and Balents (2010) suggested that certain iridium based pyrochlore compounds may be strong topological insulators. Since these materials involve  $d$  electrons, a crucial issue will be to understand the interplay between strong electron-electron interactions and the spin-orbit interaction. Recent theoretical work predicts topological insulator behavior in ternary Heusler compounds (Chadov et al., 2010; Lin, Wray, Xia, Jia, et al., 2010) and other materials (Lin, Markiewicz, et al., 2010; Lin, Wray, Xia, Xu, et al., 2010; Yan et al., 2010). These are exciting new directions where further theoretical and experimental work is called for.

Topological superconductors present another exciting frontier direction. In addition to observing the surface Majorana modes predicted for  ${}^{3}\mathrm{He}B$  (Chung and Zhang, 2009), it will be interesting to predict and observe electronic topological superconductors, to characterize their surface modes, and to explore their potential utility. To this end there has been recent progress in developing methods to theoretically identify topological superconductors based on their band structure (Fu and Berg, 2010; Qi, Hughes, and Zhang, 2010).

More generally there may be other interesting correlated states related to topological insulators and superconductors. For example, Levin and Stern (2009) showed that a  $\mathcal{T}$  invariant fractional quantum spin Hall state can be topologically stable. This points to a general theoretical problem associated with the topological classification of interacting systems: How do we unify the seemingly different notions of topological order epitomized by Thouless et al. (1982) and by Wen (1995)? The topological field theories studied by Qi, Hughes, and Zhang (2008), as well as connections with string theory (Ryu and Takayanagi, 2010), provide steps in this direction, but a complete theory remains to be developed.

To conclude, recent advances in the physics of topological insulators have been driven by a rich interplay between theoretical insight and experimental discoveries. There is reason for optimism that this field will continue to develop in exciting new directions.

# ACKNOWLEDGMENTS

C.L.K. thanks L. Fu, E. J. Mele, and J. C. Y. Teo for collaboration and NSF Grant No. DMR 0906175 for support. M.Z.H. thanks L. A. Wray for assistance preparing figures, A. Bansil, R. J. Cava, J. G. Checkelsky, J. H. Dil, A. V. Fedorov, Y. S. Hor, D. Hsieh, H. Lin, F. Meier, N. P. Ong, J. Osterwalder, L. Patthey, D. Qian, P.

Roushan, L. A. Wray, Y. Xia, and A. Yazdani for collaborations, and U.S. DOE (Grants No. DE-FG-02-05ER46200, No. AC03-76SF00098, and No. DE-FG02-07ER46352), NSF [Grant No. DMR-0819860 (materials) DMR-1006492], Alfred P. Sloan Foundation, and Princeton University for support.

# REFERENCES

Agergaard, S., C. Sondergaard, H. Li, M. B. Nielsen, S. V. Hoffmann, Z. Li, and Ph. Hofmann, 2001, New J. Phys. 3, 15.  
Akhmerov, A. R., J. Nilsson, and C. W. J. Beenakker, 2009, Phys. Rev. Lett. 102, 216404.  
Alpichshev, Z., J. G. Analytis, J. H. Chu, I. R. Fisher, Y. L. Chen, Z. X. Shen, A. Fang, and A. Kapitulnik, 2010, Phys. Rev. Lett. 104, 016401.  
Altland, A., and M. R. Zirnbauer, 1997, Phys. Rev. B 55, 1142.  
Anderson, P. W., 1958, Phys. Rev. 109, 1492.  
Ast, C. R., and H. Hochst, 2001, Phys. Rev. Lett. 87, 177602.  
Avignone, F. T., S. R. Elliott, and J. Engel, 2008, Rev. Mod. Phys. 80, 481.  
Bergman, D. L., and K. Le Hur, 2009, Phys. Rev. B 79, 184520.  
Bernevig, B. A., T. A. Hughes, and S. C. Zhang, 2006, Science 314, 1757.  
Bernevig, B. A., and S. C. Zhang, 2006, Phys. Rev. Lett. 96, 106802.  
Berry, M. V., 1984, Proc. R. Soc. London, Ser. A 392, 45.  
Bloch, F., 1929, Z. Phys. 52, 555.  
Boettger, J. C., and S. B. Trickey, 2007, Phys. Rev. B 75, 121402(R).  
Bolech, C. J., and E. Demler, 2007, Phys. Rev. Lett. 98, 237002.  
Büttiker, M., 1988, Phys. Rev. B 38, 9375.  
Cade, N. A., 1985, J. Phys. C 18, 5135.  
Caroli, C., P. G. de Gennes, and J. Matricon, 1964, Phys. Lett. 9, 307.  
Castro Neto, A. H., F. Guinea, N. M. R. Peres, K. S. Novoselov, and A. K. Geim, 2009, Rev. Mod. Phys. 81, 109.  
Chadow, S., X. L. Qi, J. Kübler, G. H. Fecher, C. Felser, and S. C. Zhang, 2010, Nature Mater. 9, 541.  
Chang, Y. C., J. N. Schulman, G. Bastard, Y. Guldner, and M. Voos, 1985, Phys. Rev. B 31, 2557.  
Checkelsky, J. G., Y. S. Hor, M. H. Liu, D. X. Qu, R. J. Cava, and N. P. Ong, 2009, Phys. Rev. Lett. 103, 246601.  
Chen, Y. L., J. G. Analytis, J. H. Chu, Z. K. Liu, S. K. Mo, X. L. Qi, H. J. Zhang, D. H. Lu, X. Dai, Z. Fang, S. C. Zhang, I. R. Fisher, Z. Hussain, and Z. X. Shen, 2009, Science 325, 178.  
Cheng, P., C. Song, T. Zhang, Y. Zhang, Y. Wang, J. F. Jia, J. Wang, Y. Wang, B. F. Zhu, X. Chen, X. Ma, K. He, L. Wang, X. Dai, Z. Fang, X. C. Xie, X. L. Qi, C. X. Liu, S. C. Zhang, and Q. K. Xue, 2010, Phys. Rev. Lett. 105, 076801.  
Chung, S. B., and S. C. Zhang, 2009, Phys. Rev. Lett. 103, 235301.  
Das Sarma, S., M. Freedman, and C. Nayak, 2005, Phys. Rev. Lett. 94, 166802.  
Das Sarma, S., C. Nayak, and S. Tewari, 2006, Phys. Rev. B 73, 220502(R).  
de Gennes, P. G., 1966, Superconductivity of Metals and Alloys (Benjamin, New York).  
DiVincenzo, D. P., and E. J. Mele, 1984, Phys. Rev. B 29, 1685.  
Dolev, M., M. Heiblum, V. Umansky, A. Stern, and D. Mahalu, 2008, Nature (London) 452, 829.  
Dornhaus, R., and G. Nimitz, 1983, Narrow Gap Semiconduc

tors, Springer Tracts in Modern Physics Vol. 98 (Springer, Berlin).  
Essin, A. M., J. E. Moore, and D. Vanderbilt, 2009, Phys. Rev. Lett. 102, 146805.  
Fradkin, E., E. Dagotto, and D. Boyanovsky, 1986, Phys. Rev. Lett. 57, 2967.  
Freedman, M. H., M. Larsen, and Z. Wang, 2002, Commun. Math. Phys. 227, 605.  
Fu, L., 2009, Phys. Rev. Lett. 103, 266801.  
Fu, L., 2010, Phys. Rev. Lett. 104, 056402.  
Fu, L., and E. Berg, 2010, Phys. Rev. Lett. 105, 097001.  
Fu, L., and C. L. Kane, 2006, Phys. Rev. B 74, 195312.  
Fu, L., and C. L. Kane, 2007, Phys. Rev. B 76, 045302.  
Fu, L., and C. L. Kane, 2008, Phys. Rev. Lett. 100, 096407.  
Fu, L., and C. L. Kane, 2009a, Phys. Rev. B 79, 161408(R).  
Fu, L., and C. L. Kane, 2009b, Phys. Rev. Lett. 102, 216403.  
Fu, L., C. L. Kane, and E. J. Mele, 2007, Phys. Rev. Lett. 98, 106803.  
Fukui, T., T. Fujiwara, and Y. Hatsugai, 2008, J. Phys. Soc. Jpn. 77, 123705.  
Fukui, T., and Y. Hatsugai, 2007, J. Phys. Soc. Jpn. 76, 053702.  
Geim, A. V., and K. S. Novoselov, 2007, Nature Mater. 6, 183.  
Ghaemi, P., and F. Wilczek, 2007, e-print arXiv:0709.2626.  
Gmitra, M., S. Konschuh, C. Ertler, C. Ambrosch-Draxl, and J. Fabian, 2009, Phys. Rev. B 80, 235431.  
Greiter, M., X. G. Wen, and F. Wilczek, 1992, Nucl. Phys. B 374, 567.  
Guo, H. M., and M. Franz, 2009, Phys. Rev. Lett. 103, 206805.  
Gurarie, V., L. Radzihovsky, and A. V. Andreev, 2005, Phys. Rev. Lett. 94, 230403.  
Haldane, F. D. M., 1988, Phys. Rev. Lett. 61, 2015.  
Halperin, B. I., 1982, Phys. Rev. B 25, 2185.  
Hanaguri, T., K. Igarashi, M. Kawamura, H. Takagi, and T. Sasagawa, 2010, Phys. Rev. B 82, 081305(R).  
Hasan, M. Z., H. Lin, and A. Bansil, 2009, Phys. 2, 108.  
Hirahara, T., T. Nagao, I. Matsuda, G. Bihlmayer, E. V. Chulkov, Y. M. Koroteev, P. M. Echenique, M. Saito, and S. Hasegawa, 2006, Phys. Rev. Lett. 97, 146803.  
Hofmann, Ph., 2006, Prog. Surf. Sci. 81, 191.  
Hor, Y. S., A. Richardella, P. Roushan, Y. Xia, J. G. Checkelsky, A. Yazdani, M. Z. Hasan, N. P. Ong, and R. J. Cava, 2009, Phys. Rev. B 79, 195208.  
Hor, Y. S., P. Roushan, H. Beidenkopf, J. Seo, D. Qu, J. G. Checkelsky, L. A. Wray, Y. Xia, S.-Y. Xu, D. Qian, M. Z. Hasan, N. P. Ong, A. Yazdani, and R. J. Cava, 2010, Phys. Rev. B 81, 195203.  
Hor, Y. S., A. J. Williams, J. G. Checkelsky, P. Roushan, J. Seo, Q. Xu, H. W. Zandbergen, A. Yazdani, N. P. Ong, and R. J. Cava, 2010, Phys. Rev. Lett. 104, 057001.  
Hsieh, D., D. Qian, L. Wray, Y. Xia, Y. S. Hor, R. J. Cava, and M. Z. Hasan, 2008, Nature (London) 452, 970.  
Hsieh, D., Y. Xia, D. Qian, L. Wray, J. H. Dil, F. Meier, J. Osterwalder, L. Patthey, J. G. Checkelsky, N. P. Ong, A. V. Fedorov, H. Lin, A. Bansil, D. Grauer, Y. S. Hor, R. J. Cava, and M. Z. Hasan, 2009a, Nature (London) 460, 1101.  
Hsieh, D., Y. Xia, D. Qian, L. Wray, F. Meier, J. H. Dil, J. Osterwalder, L. Patthey, A. V. Fedorov, H. Lin, A. Bansil, D. Grauer, Y. S. Hor, R. J. Cava, and M. Z. Hasan, 2009b, Phys. Rev. Lett. 103, 146401.  
Hsieh, D., Y. Xia, L. Wray, D. Qian, A. Pal, J. H. Dil, F. Meier, J. Osterwalder, G. Bihlmayer, C. L. Kane, Y. S. Hor, R. J. Cava, and M. Z. Hasan, 2009a, e-print arXiv:0909.5509.  
Hsieh, D., Y. Xia, L. Wray, D. Qian, A. Pal, J. H. Dil, F. Meier,

J. Osterwalder, G. Bihlmayer, C. L. Kane, Y. S. Hor, R. J. Cava, and M. Z. Hasan, 2010, e-print arXiv:1001.1574.  
Hsieh, D., Y. Xia, L. Wray, D. Qian, A. Pal, J. H. Dil, J. Osterwalder, F. Meier, G. Bihlmayer, C. L. Kane, Y. S. Hor, R. J. Cava, and M. Z. Hasan, 2009b, Science 323, 919.  
Huertas-Hernando, D., F. Guinea, and A. Brataas, 2006, Phys. Rev. B 74, 155426.  
Ivanov, D. A., 2001, Phys. Rev. Lett. 86, 268.  
Jackiw, R., 1984, Phys. Rev. D 29, 2375.  
Jackiw, R., and C. Rebbi, 1976, Phys. Rev. D 13, 3398.  
Jackiw, R., and P. Rossi, 1981, Nucl. Phys. B 190, 681.  
Kane, C. L., and E. J. Mele, 2005a, Phys. Rev. Lett. 95, 226801.  
Kane, C. L., and E. J. Mele, 2005b, Phys. Rev. Lett. 95, 146802.  
Kaplan, D. B., 1992, Phys. Lett. B 288, 342.  
Kitaev, A., 2000, e-print arXiv:cond-mat/0010440.  
Kitaev, A., 2003, Ann. Phys. 303, 2.  
Kitaev,A.,2009,AIP Conf.Proc.1134,22.  
Kohmoto, M., B. I. Halperin, and Y. S. Wu, 1992, Phys. Rev. B 45, 13488.  
Konig, M., H. Buhmann, L. W. Molenkamp, T. Hughes, C. X. Liu, X. L. Qi, and S. C. Zhang, 2008, J. Phys. Soc. Jpn. 77, 031007.  
Konig, M., S. Wiedmann, C. Brüne, A. Roth, H. Buhmann, L. W. Molenkamp, X. L. Qi, and S. C. Zhang, 2007, Science 318, 766.  
Laughlin, R. B., 1983, Phys. Rev. Lett. 50, 1395.  
Law, K. T., P. A. Lee, and T. K. Ng, 2009, Phys. Rev. Lett. 103, 237001.  
Lee, P. A., 2009, e-print arXiv:0907.2681.  
Lee, P. A., and T. V. Ramakrishnan, 1985, Rev. Mod. Phys. 57, 287.  
Lenoir, B., A. Dauscher, X. Devaux, R. Martin-Lopez, Y. I. Ravich, H. Scherrer, and S. Scherrer, 1996, Proceedings of the Fifteenth International Conference on Thermoelectrics (IEEE, New York) pp. 1-13.  
Levin, M., and A. Stern, 2009, Phys. Rev. Lett. 103, 196803.  
Li, Y. Y., G. Wang, X. G. Zhu, M. H. Liu, C. Ye, X. Chen, Y. Y. Wang, K. He, L. L. Wang, X. C. Ma, H. J. Zhang, X. Dai, Z. Fang, X. C. Xie, Y. Liu, X. L. Qi, J. F. Jia, S. C. Zhang, and Q. K. Xue, 2009, e-print arXiv:0912.5054.  
Lin, H., R. S. Markiewicz, L. A. Wray, L. Fu, M. Z. Hasan, and A. Bansil, 2010, e-print arXiv:1003.2615.  
Lin, H., L. A. Wray, Y. Xia, S. Jia, R. J. Cava, A. Bansil, and M. Z. Hasan, 2010, Nature Mater. 9, 546.  
Lin, H., L. A. Wray, Y. Xia, S. Y. Xu, S. Jia, R. J. Cava, A. Bansil, and M. Z. Hasan, 2010, e-print arXiv:1004.0999.  
Linder, J., Y. Tanaka, T. Yokoyama, A. Sudbo, and N. Nagaosa, 2010, Phys. Rev. Lett. 104, 067001.  
Lin-Liu, Y. R., and L. J. Sham, 1985, Phys. Rev. B 32, 5561.  
Liu, Y., and R. E. Allen, 1995, Phys. Rev. B 52, 1566.  
Maciejko, J., C. Liu, Y. Oreg, X. L. Qi, C. Wu, and S. C. Zhang, 2009, Phys. Rev. Lett. 102, 256803.  
Majorana, E., 1937, Nuovo Cimento 14, 171.  
Min, H., J. E. Hill, N. A. Sinitsyn, B. R. Sahu, L. Kleinman, and A. H. MacDonald, 2006, Phys. Rev. B 74, 165310.  
Moore, G., and N. Read, 1991, Nucl. Phys. B 360, 362.  
Moore, J. E., 2009, Nat. Phys. 5, 378.  
Moore, J. E., 2010, Nature (London) 464, 194.  
Moore, J. E., and L. Balents, 2007, Phys. Rev. B 75, 121306(R).  
Murakami, S., N. Nagaosa, and S. C. Zhang, 2004, Phys. Rev. Lett. 93, 156804.  
Nagato, Y., S. Higashitani, and K. Nagai, 2009, J. Phys. Soc. Jpn. 78, 123603.

Nakahara, M., 1990, Geometry, Topology and Physics (Hilger, Bristol).  
Nayak, C., S. H. Simon, A. Stern, M. Freedman, and S. Das Sarma, 2008, Rev. Mod. Phys. 80, 1083.  
Nayak, C., and F. Wilczek, 1996, Nucl. Phys. B 479, 529.  
Nielssen, H., and N. Ninomiya, 1983, Phys. Lett. 130B, 389.  
Nilsson, J., A. R. Akhmerov, and C. W. J. Beenakker, 2008, Phys. Rev. Lett. 101, 120403.  
Nishide, A., A. A. Taskin, Y. Takeichi, T. Okuda, A. Kakizaki, T. Hirahara, K. Nakatsuji, F. Komori, Y. Ando, and I. Matsuda, 2010, Phys. Rev. B 81, 041309(R).  
Noh, H. J., H. Koh, S. J. Oh, J. H. Park, H. D. Kim, J. D. Rameau, T. Valla, T. E. Kidd, P. D. Johnson, Y. Hu, and Q. Li, 2008, EPL 81, 57006.  
Nomura, K., M. Koshino, and S. Ryu, 2007, Phys. Rev. Lett. 99, 146806.  
Novoselov, K. S., A. K. Geim, S. V. Morozov, D. Jiang, M. I. Katsnelson, I. V. Grigorieva, S. V. Dubonos, and A. A. Firsov, 2005, Nature (London) 438, 197.  
Pankratov,O.A.,1987,Phys.Lett.A 121,360.  
Pankratov, O. A., S. V. Pakhomov, and B. A. Volkov, 1987, Solid State Commun. 61, 93.  
Park, S. R., W. S. Jung, C. Kim, D. J. Song, C. Kim, S. Kimura, K. D. Lee, and N. Hur, 2010, Phys. Rev. B 81, 041405(R).  
Patthey, F., W. D. Schneider, and H. Micklitz, 1994, Phys. Rev. B 49, 11293.  
Peng, H., K. Lai, D. Kong, S. Meister, Y. Chen, X. L. Qi, S. C. Zhang, Z. X. Shen, and Y. Cui, 2010, Nature Mater. 9, 225.  
Pesin, D. A., and L. Balents, 2010, Nat. Phys. 6, 376.  
Prange, R. E., and S. M. Girvin, 1987, The Quantum Hall Effect (Springer, New York).  
Qi, X. L., T. L. Hughes, S. Raghu, and S. C. Zhang, 2009, Phys. Rev. Lett. 102, 187001.  
Qi, X. L., T. L. Hughes, and S. C. Zhang, 2008, Phys. Rev. B 78, 195424.  
Qi, X. L., T. L. Hughes, and S. C. Zhang, 2010, Phys. Rev. B 81, 134508.  
Qi, X. L., R. Li, J. Zang, and S. C. Zhang, 2009, Science 323, 1184.  
Qi, X. L., Y. S. Wu, and S. C. Zhang, 2006, Phys. Rev. B 74, 085308.  
Qi, X. L., and S. C. Zhang, 2010, Phys. Today 63 (1), 33.  
Radu, P., J. B. Miller, C. M. Marcus, M. A. Kastner, L. N. Pfeiffer, and K. W. West, 2008, Science 320, 899.  
Ran, Y., Y. Zhang, and A. Vishwanath, 2009, Nat. Phys. 5, 298.  
Read, N., and D. Green, 2000, Phys. Rev. B 61, 10267.  
Roth, A., C. Brüne, H. Buhmann, L. W. Molenkamp, J. Maciejko, X. L. Qi, and S. C. Zhang, 2009, Science 325, 294.  
Roushan, P., J. Seo, C. V. Parker, Y. S. Hor, D. Hsieh, D. Qian, A. Richardella, M. Z. Hasan, R. J. Cava, and A. Yazdani, 2009, Nature (London) 460, 1106.  
Roy, R., 2008, e-print arXiv:0803.2868.  
Roy, R., 2009a, Phys. Rev. B 79, 195321.  
Roy, R., 2009b, Phys. Rev. B 79, 195322.  
Ryu, S., A. Schnyder, A. Furusaki, and A. W. W. Ludwig, 2010, New J. Phys. 12, 065010.  
Ryu, S., and T. Takayanagi, 2010, e-print arXiv:1001.0763.  
Sato, M., and S. Fujimoto, 2009, Phys. Rev. B 79, 094504.  
Sau, J. D., R. M. Lutchyn, S. Tewari, and S. Das Sarma, 2010, Phys. Rev. Lett. 104, 040502.  
Schnyder, A. P., S. Ryu, A. Furusaki, and A. W. W. Ludwig, 2008, Phys. Rev. B 78, 195125.  
Schnyder, A. P., S. Ryu, A. Furusaki, and A. W. W. Ludwig,

2009, AIP Conf. Proc. 1134, 10.  
Semenoff, G. W., 1984, Phys. Rev. Lett. 53, 2449.  
Seradjeh, B., J. E. Moore, and M. Franz, 2009, Phys. Rev. Lett. 103, 066402.  
Sheng, D. N., Z. Y. Weng, L. Sheng, and F. D. M. Haldane, 2006, Phys. Rev. Lett. 97, 036808.  
Shitade, A., H. Katsura, J. Kunes, X. L. Qi, S. C. Zhang, and N. Nagaosa, 2009, Phys. Rev. Lett. 102, 256403.  
Stern, A., and B. I. Halperin, 2006, Phys. Rev. Lett. 96, 016802.  
Stern, A., F. von Oppen, and E. Mariani, 2004, Phys. Rev. B 70, 205338.  
Su, W. P., J. R. Schrieffer, and A. J. Heeger, 1979, Phys. Rev. Lett. 42, 1698.  
Suzuura, H., and T. Ando, 2002, Phys. Rev. Lett. 89, 266603.  
Tanaka, Y., T. Yokoyama, and N. Nagaosa, 2009, Phys. Rev. Lett. 103, 107002.  
Taskin, A. A., and Y. Ando, 2009, Phys. Rev. B 80, 085303.  
Teo, J. C. Y., L. Fu, and C. L. Kane, 2008, Phys. Rev. B 78, 045426.  
Teo, J. C. Y., and C. L. Kane, 2009, Phys. Rev. B 79, 235321.  
Teo, J. C. Y., and C. L. Kane, 2010, Phys. Rev. Lett. 104, 046401.  
Tewari, S., S. Das Sarma, C. Nayak, C. Zhang, and P. Zoller, 2007, Phys. Rev. Lett. 98, 010506.  
Thouless, D. J., M. Kohmoto, M. P. Nightingale, and M. den Nijs, 1982, Phys. Rev. Lett. 49, 405.  
Tsui, D. C., H. L. Stormer, and A. C. Gossard, 1982, Phys. Rev. Lett. 48, 1559.  
Urazhdin, S., D. Bilc, S. D. Mahanti, S. H. Tessmer, T. Kyratsi, and M. G. Kanatzidis, 2004, Phys. Rev. B 69, 085313.  
Volkov, B. A., and O. A. Pankratov, 1985, Pis'ma Zh. Eksp. Teor. Fiz. 42, 145 [JETP Lett. 42, 178 (1985)].  
Volovik, G. E., 1999, Pis'ma Zh. Eksp. Teor. Fiz. 70, 601 [JETP Lett. 70, 609 (1999)].  
Volovik, G. E., 2003, The Universe in a Helium Droplet (Clarendon, Oxford).  
Volovik, G. E., 2009, JETP Lett. 90, 587.  
Volovik, G. E., and V. M. Yakovenko, 1989, J. Phys.: Condens. Matter 1, 5263.  
von Klitzing, K., 2005, Philos. Trans. R. Soc. London, Ser. A 363, 2203.  
von Klitzing, K., G. Dorda, and M. Pepper, 1980, Phys. Rev. Lett. 45, 494.  
Wang, Z., X. L. Qi, and S. C. Zhang, 2010, New J. Phys. 12,

065007.  
Wen, X. G., 1995, Adv. Phys. 44, 405.  
Wilczek, F., 1987, Phys. Rev. Lett. 58, 1799.  
Wilczek,F.,2009,Nat.Phys.5,614.  
Willett, R. L., L. N. Pfeiffer, and K. W. West, 2009, Proc. Natl. Acad. Sci. U.S.A. 106, 8853.  
Wolff, P. A., 1964, J. Phys. Chem. Solids 25, 1057.  
Wray, L., S. Xu, J. Xiong, Y. Xia, D. Qian, H. Lin, A. Bansil, Y. Hor, R. J. Cava, and M. Z. Hasan, 2009, e-print arXiv:0912.3341.  
Wray, L., S. Xu, J. Xiong, Y. Xia, D. Qian, H. Lin, A. Bansil, Y. Hor, R. J. Cava, and M. Z. Hasan, 2010, Nat. Phys. (to be published).  
Wu, C., B. A. Bernevig, and S. C. Zhang, 2006, Phys. Rev. Lett. 96, 106401.  
Xia, Y., D. Qian, D. Hsieh, R. Shankar, H. Lin, A. Bansil, A. V. Fedorov, D. Grauer, Y. S. Hor, R. J. Cava, and M. Z. Hasan, 2009, e-print arXiv:0907.3089.  
Xia, Y., D. Qian, D. Hsieh, L. Wray, A. Pal, H. Lin, A. Bansil, D. Grauer, Y. S. Hor, R. J. Cava, and M. Z. Hasan, 2009, Nat. Phys. 5, 398.  
Xia, Y., L. Wray, D. Qian, D. Hsieh, A. Pal, H. Lin, A. Bansil, D. Grauer, Y. S. Hor, R. J. Cava, and M. Z. Hasan, 2008, e-print arXiv:0812.2078.  
Xu, C., and J. E. Moore, 2006, Phys. Rev. B 73, 045322.  
Yan, B., C. X. Liu, H. J. Zhang, C. Y. Yam, X. L. Qi, T. Frauenheim, and S. C. Zhang, 2010, Europhys. Lett. 90, 37002.  
Yao, Y., F. Ye, X. L. Qi, S. C. Zhang, and Z. Fang, 2007, Phys. Rev. B 75, 041401(R).  
Zhang, G., et al., 2009, Appl. Phys. Lett. 95, 053114.  
Zhang, H., C. X. Liu, X. L. Qi, X. Dai, Z. Fang, and S. C. Zhang, 2009, Nat. Phys. 5, 438.  
Zhang, S. C., and J. Hu, 2001, Science 294, 823.  
Zhang, T., P. Cheng, X. Chen, J. F. Jia, X. Ma, K. He, L. Wang, H. Zhang, X. Dai, Z. Fang, X. Xie, and Q. K. Xue, 2009, Phys. Rev. Lett. 103, 266803.  
Zhang, Y., K. He, C. Z. Chang, C. L. Song, L. Wang, X. Chen, J. Jia, Z. Fang, X. Dai, W. Y. Shan, S. Q. Shen, Q. Niu, X. L. Qi, S. C. Zhang, X. Ma, and Q. K. Xue, 2010, Nat. Phys. 6, 712.  
Zhang, Y., Y. W. Tan, H. L. Stormer, and P. Kim, 2005, Nature (London) 438, 201.  
Zheng, Y., and T. Ando, 2002, Phys. Rev. B 65, 245420.