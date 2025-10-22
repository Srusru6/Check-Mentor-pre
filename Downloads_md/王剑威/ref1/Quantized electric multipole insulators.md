# TOPOLOGICAL MATTER

# Quantized electric multipole insulators

Wladimir A. Benalcazar, $^{1}$  B. Andrei Bernevig, $^{2}$  Taylor L. Hughes $^{1*}$

The Berry phase provides a modern formulation of electric polarization in crystals. We extend this concept to higher electric multipole moments and determine the necessary conditions and minimal models for which the quadrupole and octupole moments are topologically quantized electromagnetic observables. Such systems exhibit gapped boundaries that are themselves lower-dimensional topological phases. Furthermore, they host topologically protected corner states carrying fractional charge, exhibiting fractionalization at the boundary of the boundary. To characterize these insulating phases of matter, we introduce a paradigm in which "nested" Wilson loops give rise to topological invariants that have been overlooked. We propose three realistic experimental implementations of this topological behavior that can be immediately tested. Our work opens a venue for the expansion of the classification of topological phases of matter.

Topological phases of matter can give rise to sharply quantized physical quantities, such as (i) charge polarization  $P_{1}$  in crystals, with either charge conjugation or inversion symmetry (1-3); (ii) Hall conductance  $\sigma_{xy}$  in two-dimensional (2D) integer quantum Hall or Chern insulator systems (4-6); and (iii) magnetoelectric polarizability  $P_{3}$  in 3D time-reversal invariant or inversion symmetric topological insulators (2, 3, 7, 8). These response coefficients can be elegantly expressed as quantized topological invariants in terms of the Berry phase vector potential  $\mathcal{A}$

$$
P _ {1} = - \frac {e}{2 \pi} \int_ {B Z} \operatorname {T r} [ \mathcal {A} ] \tag {1}
$$

$$
\sigma_ {x y} = - \frac {e ^ {2}}{2 \pi h _ {B Z}} \int \operatorname {T r} [ d \mathcal {A} + i \mathcal {A} \wedge \mathcal {A} ] \tag {2}
$$

$$
P _ {3} = - \frac {e ^ {2}}{4 \pi h} \int_ {B Z} \operatorname {T r} \left[ \mathcal {A} \wedge d \mathcal {A} + \frac {2 i}{3} \mathcal {A} \wedge \mathcal {A} \wedge \mathcal {A} \right] \tag {3}
$$

where  $BZ$  in Eqs. 1 to 3 is the Brillouin zone in one, two, and three spatial dimensions, respectively, and  $\mathcal{A}$  has components  $[\mathcal{A}_i(k)]^{mn} = -i\langle u_k^m |\partial_{k_i}|u_k^n\rangle$ , where  $|u_{k}^{n}\rangle$  is the Bloch function of band  $n$  and  $m,n$  run only over occupied energy bands.

The forms of  $\sigma_{xy}$  and  $P_{3}$  are natural mathematical generalizations of  $P_{1}$  to higher dimensions. However, there is no theory for the natural physical generalizations of the dipole polarization  $P_{1}$  to higher electric multipole moments in crystalline insulators. Here, we provide a generalization of the polarization Eq. 1 to higher multipole moments. These higher moments can also be of topological origin and are quantized by certain crystalline symmetries. We explain this

quantization by introducing a paradigm for topological invariants based on nested Wilson loops. Our bulk topological invariants determine the properties of gapped but possibly nontrivial boundaries and allow us to use robust topological phenomena to provide a definition of a "boundary of a boundary." The physical manifestation of our multipole moments is twofold: (i) fractional corner charges (but not edge or surface) that are quantized to  $\pm e / 2$  in the presence of certain symmetries, and (ii) edge-localized electric currents as the result of adiabatic deformations that preserve inversion symmetry. Classically, the primitive dipole, quadrupole, and octupole moments of a continuum, volume charge density  $\rho (r)$  are defined as  $p_i = \int d^3 r\mathsf{P}(r)r_i$ $q_{ij} = \int d^3 r\mathsf{P}(r)r_ir_j$  and  $o_{ijk} = \int d^3 r\mathsf{P}(r)r_ir_k$  (9). In the modern theory of polarization in crystals, the dipole moment  $p_i$  is a Berry phase of the bulk electron states (Eq. 1) and manifests itself through the presence of surface charge. Higher moments generate a cascade of observable properties, for which the current theory of polarization is not sufficient. We derive the electromagnetic properties of a 2D insulator with a square shape and a 3D insulator with a cubic shape, having only a nonvanishing quadrupole moment  $q_{xy}$  or octupole moment  $o_{xyz}$ , respectively [the derivation and general formulation are provided in (10), Sec. 1], obtaining, respectively

$$
p _ {j} ^ {\mathrm {e d g e} \alpha} = n _ {i} ^ {\alpha} q _ {i j}, Q ^ {\mathrm {c o r n e r} \alpha , \beta} = n _ {i} ^ {\alpha} n _ {j} ^ {\beta} q _ {i j} \tag {4}
$$

$$
q _ {j k} ^ {\text {f a c e} \alpha} = n _ {i} ^ {\alpha} o _ {i j k},
$$

$$
p _ {k} ^ {\text {h i n g e} \alpha , \beta} = n _ {i} ^ {\alpha} n _ {j} ^ {\beta} o _ {i j k},
$$

$$
Q ^ {\text {c o r n e r} \alpha , \beta , \gamma} = n _ {i} ^ {\alpha} n _ {j} ^ {\beta} n _ {k} ^ {\gamma} o _ {i j k}, \tag {5}
$$

where repeated indices are summed over. Here,  $p_j^{\mathrm{edge}\alpha}$  are the edge tangential polarizations per unit length on the square,  $p_j^{\mathrm{hinge}\alpha,\beta}$  are the hinge tangential polarizations per unit length on the cube,  $q_{jk}^{\mathrm{face}\alpha}$  are the surface quadrupoles per unit area of the cube, and  $Q^{\mathrm{comer}\alpha,\beta}$  and  $Q^{\mathrm{comer}\alpha,\beta,\gamma}$  are the charges localized on the corners of the square and cube, respectively. The Greek letters  $\alpha,\beta,\gamma = \pm x$ ,  $\pm y$ ,  $\pm z$  label the surfaces of the square/cube, with

outward pointing unit normal vectors  $n_i^\alpha = s_\alpha \delta_i^{|\alpha|}$  where the sign  $s_{\alpha = \pm} = \pm 1$  encodes the direction. Hinges and corners are associated with the intersection of multiple surfaces and hence have more than one associated surface label and normal vector; the only nonvanishing contributions occur for  $\alpha \neq \beta \neq \gamma$ . These properties are represented pictorially in Fig. 1, A and B.

Despite the connection between bulk electric moments and their boundary surface properties, we can illustrate the bulk nature of the quadrupole moment by drawing a distinction between systems with edge polarizations induced by a bulk quadrupole moment  $q_{xy}$  and those with boundary polarizations in the absence of a bulk quadrupole. For the second case, consider an unpolarized 2D insulator with  $q_{xy} = 0$  that has tangent edge polarizations per unit length following the same pattern as in Fig. 1A (but where in general we could have  $|p_y^{\mathrm{edge} + x}| \neq |p_x^{\mathrm{edge} + y}|$ ). In this configuration,  $Q^{\mathrm{comer} + x, + y} = p_y^{\mathrm{edge} + x} + p_x^{\mathrm{edge} + y}$  (notice that all of these quantities have units of charge), which is just the induced charge from the two independent edge polarizations converging to the corner or diverging from it. Now, suppose that instead we have a bulk unpolarized system with  $q_{xy} \neq 0$ . According to Eq. 4, this moment induces tangent edge polarizations and corner charges of equal magnitude,  $|p_x^{\mathrm{edge} + y}| = |p_y^{\mathrm{edge} + x}| = |Q^{\mathrm{comer} + x, + y}| = |q_{xy}|$ , and with the pattern shown in Fig. 1A. Crucially, the corner charge is not the sum of the two boundary polarizations; it is not the result of edge phenomena alone. Instead, both edge polarizations and corner charge are boundary manifestations of the bulk. In a system without bulk polarization but with both quadrupole moment and (bulk-independent) edge polarizations, the quadrupole moment determines exactly how much the corner charge differs from the sum of the tangent edge polarizations according to  $Q^{\mathrm{comer} + x, + y} - P_y^{\mathrm{edge} + x} - P_x^{\mathrm{edge} + y} = -q_{xy}$ , where the upper-case  $P^{\mathrm{edge}a}$  is the total edge polarization on edge  $a$  regardless of its physical origin.

We will now show that the quadrupole and octupole moments can be defined in crystals and are quantized by the presence of reflection symmetries.

# Model with quantized quadrupole moment

Heuristically, a 2D crystal with a quantized quadrupole moment should have two properties: (i) at least two occupied bands and (ii) symmetries that quantize the bulk quadrupole moment and bulk dipole moment—the latter made to vanish. We expect (i) because canonical quadrupoles are built from two canceling dipole moments, and two occupied bands are needed to generate nonvanishing, individual dipoles, but a total canceling dipole [(10), Sec. 1]. Regarding (ii), moments that are odd under a symmetry must naively vanish, but in following with the usual quantization paradigm of  $P_{1}$  (1-3) and  $P_{3}$  (2, 3, 7, 8), these moments can more generally satisfy, for example,  $P_{1} = -P_{1} \mod e$  (in 1D), which has a nonvanishing solution  $P_{1} = \pm e / 2$  when a lattice is introduced (11, 12). For (ii), we will enforce reflection symmetries  $M_{x} \colon x \to -x$  and  $M_{y} \colon y \to -y$ .

![](images/5f2c01319387f250b8e807d06d01909fb86ed3f98628a577036aa43eb4f0854a.jpg)  
A

![](images/36b0dd38182e7ce223d8e7b2240438fcafc210dc0eb5241d3553ce4ea1a48246.jpg)  
B

Fig. 1. Quadrupole and octupole moments. (A and B) Classical continuum and (C and D) quantum mechanical crystalline theories. (A) Bulk quadrupole moment  $q_{xy}$  and its boundary polarizations  $p_i$  and corner charges Q. (B) Bulk octupole moment  $o_{xyz}$  and its surface quadrupoles  $q_{ij}$ , hinge polarizations  $p_i$ , and corner charges Q. (C) Tight binding model with quantized quadrupole moment  $q_{xy}$ .  $\gamma, \lambda$  represent two hopping strengths, and dashed lines represent hopping terms with negative signs. The topological phase occurs when  $|\gamma / \lambda| < 1$ .  
C  
D  
![](images/f424ba48d7be1613c87a9c64f05575b0451bc050ac0aa7acb5c1810655496c33.jpg)  
Numbers indicate basis for  $\Gamma$ -matrices (Eq. 6). (D) Tight binding model with quantized octupole moment  $o_{xyz}$ . Each square plaquette in each direction contains  $\pi$ -flux; one of the bonds on each square has a negative sign (Eq. 18). In (D),  $\gamma = 0$  for simplicity.

![](images/65aa433b682500a1a4ec62a33a153c35741f967e899816f2f477fa17e9a9fc27.jpg)

As our first model, let us consider the 4-band insulator with Bloch Hamiltonian

$$
\begin{array}{l} h ^ {q} (k, \delta) = [ \gamma + \lambda \cos (k _ {x}) ] \Gamma_ {4} + \lambda \sin (k _ {x}) \Gamma_ {3} + \\ [ \gamma + \lambda \cos (k _ {y}) ] \Gamma_ {2} + \lambda \sin (k _ {y}) \Gamma_ {1} + \delta \Gamma_ {0} \tag {6} \\ \end{array}
$$

which can represent an insulator with a quadrupole moment. Here,  $\Gamma_0 = \tau_3\sigma_0$ ,  $\Gamma_k = -\tau_2\sigma_k$ , and  $\Gamma_4 = \tau_1\sigma_0$ , for  $k = 1, 2$ , and 3;  $\tau, \sigma$  are Pauli matrices for the degrees of freedom within a unit cell, and we will choose lattice constants  $a_{x,y} = 1$  throughout. This model, shown in Fig. 1C along with the basis of the  $\Gamma$ -matrices, represents spinless electrons on a square lattice, having  $\pi$ -flux per plaquette and with bond dimerization in the  $x$  and  $y$  directions.  $h^q(k, 0)$  has energies  $E = \pm \sqrt{2\lambda^2 + 2\gamma^2 + 2\lambda\gamma[\cos(k_x) + \cos(k_y)]}$ , each of which is twofold degenerate. An energy gap exists unless  $\gamma/\lambda \pm 1$  (Fig. 2A). Hence, at halffilling, with two electrons per cell, it is an insulator. A phase transition occurs at  $\gamma/\lambda = 1$  ( $\gamma/\lambda = -1$ ), with a bulk energy gap closing at the  $M = (\pi, \pi)[\Gamma = (0, 0)]$  point of the BZ. When  $\delta = 0$ ,  $h^q$  has reflection symmetries  $\hat{m}_i h^q(k) m_i^\dagger = h^q(M_i k)$  for  $i = x, y$ , where  $\hat{m}_x = \tau_1\sigma_3$ ,  $\hat{m}_y = \tau_1\sigma_1$ , and  $M_x(k_x, k_y) = (-k_x, k_y)$ ,  $M_y(k_x, k_y) = (k_x, -k_y)$ . These symmetries quantify both components of the polarization and, as we will see, the quadrupole moment  $q_{xy}$ . Being topological and symmetry-protected, this quantization is robust with respect to the spatial displacement of the internal degrees of freedom of the unit cell that preserve the reflection symmetries [(10), Sec. 10]. To obtain a nontrivial topological quadrupole, however, it is crucial that  $\hat{m}_x$  and  $\hat{m}_y$  do not commute [(10), Sec. 8]. For our model, they satisfy  $\{\hat{m}_x, \hat{m}_y\} = 0$

because the reflection symmetry is only preserved up to a gauge transformation [(10), Sec. 9]. Because of its simple form, this model also preserves time-reversal (TR) and charge-conjugation (CC) symmetries, with  $\Theta = K$  and  $C = \Gamma_0K$  as the TR and CC operators, as well as  $C_4$  symmetry  $\hat{r}_4h^q (k)r_4^\dagger = h^q (R_4k)$  up to a gauge transformation, with

$$
\hat {r} _ {4} = \left( \begin{array}{c c} 0 & \sigma_ {0} \\ - i \sigma_ {y} & 0 \end{array} \right)
$$

and  $R_{4}$  the rotation of the momentum by  $\pi /2$  However, these symmetries are not necessary for our discussion and could be removed without affecting the conclusions. When  $\delta \neq 0$  ,the model breaks charge conjugation, both reflections, and  $C_4$  symmetries but preserves inversion symmetry. This leaves the polarization quantized; however, it does break the symmetries required to quantize the quadrupole moment. For most of our discussion, we will only tune  $\delta$  infinitesimally away from O in order to fix the sign of  $q_{xy}$

In the gapped phases of  $h^q$ , the polarization and Chern number are zero, and we confirm that generically, there are no gapless edge states. However, in the phase  $|\gamma/\lambda| < 1$  we found that the insulator has a quantized boundary polarization, tangent to the edge, of magnitude  $\pm e/2$ , and quantized corner charges  $\pm e/2$  (Figs. 1A and 2, B and D). Together, these are a defining signature of a quantized bulk quadrupole moment  $q_{xy} = \pm e/2$  (Eq. 4). On the other hand, for  $|\gamma/\lambda| > 1$  both the corner charges and boundary polarizations vanish. Thus, we denote the phase  $|\gamma/\lambda| < 1$  as the nontrivial quadrupole phase and  $|\gamma/\lambda| > 1$  as the trivalent quadrupole phase.

the trivial quadrupole phase. Associated with the corner charges observed in the nontrivial phase is the existence of four, corner-localized, energy-degenerate, mid-gap modes when  $\delta = 0$  (Fig. 2A, red lines). At half filling, the negative energy bulk bands and two of the four corner modes are filled. An infinitesimal shift of  $\delta$  suffices to split the degeneracy of the corner modes by the on-site potential  $\delta \Gamma_0$ . The sign of  $\delta$  determines whether the corner modes on one diagonal or the other are filled, resulting in an electron density pattern, as shown in Fig. 2B. If we account for a charge of  $+2e$  per unit cell stemming from atomic contributions, the overall charge density is essentially zero in the bulk, with  $\pm e / 2$  fractional charges exponentially localized at the corners in the limit  $\delta \rightarrow 0$ .

The edge polarization in a quadrupole is a subtle feature. When it changes in space or time, it leads to observables that will be discussed in more detail below. We now characterize the quantized edge polarization of the symmetry-protected quadrupole phase. We consider a cylinder geometry by connecting either the top and bottom edges or left and right edges of our model. The remaining  $x$ -normal edge preserves  $M_y$  symmetry, and the remaining  $y$ -normal edge preserves  $M_x$  symmetry. As a starting point, we will describe the edge polarization in the simple limit  $\gamma = 0$  (Fig. 2C). On each edge, there is a localized 1D, two-band, gapped insulator (at halffilling) with reflection symmetry. The 1D polarization of such a system, which lies tangent to the edge, is quantized in units of  $e/2$  and signals a boundary topological insulator phase. The edge polarization remains quantized even after departing from the  $\gamma = 0$  limit. In Fig. 2D, we show the results of calculations of the spatially resolved polarization [a similar characterization is provided in (I3)] for several values of  $|\gamma/\lambda|$  (we assume the edge unit cells are identical to the bulk and not relaxed or reconstructed). We found that if  $\gamma/\lambda = 0$ , the quantized polarization of  $\pm e/2$  is exactly localized on the edge, but as  $|\gamma/\lambda| \rightarrow 1$  the polarization, although still exactly quantized, penetrates into the bulk exponentially slowly as determined by the bulk gap. This protection by the bulk gap is clear evidence that the edge polarization is caused by the topology of the bulk and is not just an edge property. Indeed, we found that the edge polarization exactly vanishes after the bulk phase transition, just as we saw the corner-localized modes disappear in a system with full open boundaries. In all cases, the total polarization vanishes because opposite edges have opposite polarization.

This topologically nontrivial edge polarization implies the existence of topological corner states. Because the topology is protected by spatial symmetry, spatial defects such as corners create an effective edge for the boundary topological insulator and hence form the boundary of the boundary. The edge phases that converge at a corner are both topological, and crucially, the corner-localized topological mode is a simultaneous end state of the two boundary topological insulators that meet at that corner, and not a conventional domain

![](images/4d89fce0b9b0361184e4bfd7505f8bd5ee04602e7beb820d4302a4930c0b5df1.jpg)

![](images/37adff3ea9187c09c837e83827a00d7f903909543659c06e8b1c3a2800a57b18.jpg)

![](images/db64982c4da4113c2c8739e5e7599d05a833d6077ff1b4e6786e7ba851ba9bb2.jpg)  
Fig. 2. Properties of quadrupole insulator with the Bloch Hamiltonian in Eq. 6. (A) Energy spectrum for a system with open boundary conditions in  $x$  and  $y$  as a function of  $\gamma / \lambda$ . Red lines correspond to four energy-degenerate, corner-localized states. (B) Electronic charge density in the nontrivial phase (here,  $\lambda = 1$ ,  $\delta = \gamma = 10^{-3}$  on a square lattice with 20 sites per side). (C) Lattice with open boundaries along  $x$  and periodic boundaries along  $y$  at  $\gamma = 0$ . Its edges (with blue and red hoppings) are 1D nontrivial topological insulators. (D) Tangential polarization along  $y$  as a function of lattice sites along  $x$  for the geometric configuration in (C), but for three values of  $\gamma / \lambda$ . For  $\gamma / \lambda = 0.5$ , the integrated polarization over half of the lattice width is still  $\pm e / 2$ .

![](images/327901382812c7193cafefa7c00ab952c3320fea2776d212e202b4ee28b55f71.jpg)

wall mode trapped between a topological and trivial phase [(10), Sec. 2].

# Nested Wilson loops

As seen above, a bulk topological quadrupole moment  $q_{xy}$  generates a topologically polarized edge when the system is cut parallel to either the  $x$  or  $y$  directions. To formulate this as a bulk property, we consider the Wilson loop operators in the  $x$  and  $y$  directions:  $\mathcal{W}_{x,k}$  or  $\mathcal{W}_{y,k}$ , where  $k = (k_x, k_y)$  is the starting point of the loop (Fig. 3A). A crystal with  $N_{\mathrm{orb}}$  degrees of freedom per unit cell and  $N_{\mathrm{occ}}$  occupied energy bands has the occupied Bloch functions  $|u_k^n\rangle$  for  $n = 1 \dots N_{\mathrm{occ}}$ , with components  $[u_k^n ]^\alpha$  for  $\alpha = 1 \dots N_{\mathrm{orb}}$ . We define  $[F_{x,k}]^{mn} = \langle u_{k + \Delta k_x}^m |u_k^n\rangle$ , for  $\Delta k_{x} = (2\pi /N_{x},0)$ , where  $N_{x}$  is the number of lattice sites along  $x$ . Hence,  $\mathcal{W}_{x,k} = F_{x,k + N_x\Delta k_x} \dots F_{x,k + \Delta k_x}F_{x,k}$ , and similarly for  $\mathcal{W}_{y,k}$ . We define a Wannier Hamiltonian  $H_{\mathcal{W}_z(k)}$  of the  $x$  edge via

$$
\mathcal {W} _ {x, k} \equiv e ^ {i H _ {\mathcal {V} _ {x}} (k)} \tag {7}
$$

which has been shown (14) to be adiabatically connected to the physical Hamiltonian of the

edge, and which we use to characterize the boundary topology.

$H_{\mathcal{W}_x(k)}$  has eigenvalues  $2\pi \mathrm{v}_x^j (k_y), j = 1\dots N_{\mathrm{occ}}$  that only depend on the coordinate  $k_{y}$  of the Wilson loop starting point [and vice versa for the eigenvalues of  $H_{\mathcal{W}_y(k)}$  of the  $y$  edge]. With fully periodic boundary conditions, the Wilson loop for our model diagonalizes as

$$
\mathcal {W} _ {x, k} = \sum_ {j = \pm} | v _ {x, k} ^ {j} \rangle e ^ {2 \pi i v _ {x} ^ {j} (k _ {y})} \langle v _ {x, k} ^ {j} | \tag {8}
$$

where the eigenstates  $|\nu_{x,k}^{j}\rangle$ ,  $j = 1,2$ , have components  $[\nu_{x,k}^{j}]^{n}$ ,  $n = 1,2$ . It is well known that the Wannier centers are proportional to the phases  $\nu_{x}^{j}(k_{y})$  of these eigenvalues (11, 12, 15-19). Because of the  $x\rightarrow -x$  reflection symmetry,  $\nu_{x}^{-}(k_{y}) = -\nu_{x}^{+}(k_{y})$  mod1 (20) [(10), Sec. 6]; for convention, we chose  $\nu_{x}^{-}(k_{y})\in [0,1 / 2]$ . Crucially, in our model, unlike previously characterized topological insulators (17-23), the Wannier centers of the two occupied bands do not touch at any point over the entire range  $k_{y}\in (-\pi ,\pi ]$  (Fig. 3B, red lines). Thus,  $H_{\mathcal{V}_{X^{\prime}}}$  is gapped, and we refer to the spectra  $\nu_{x}^{\pm}(k_{y})$  as being two Wannier bands, and to their separation as the Wannier gap.

The Wannier bands are defined over the 1D BZ  $k_{y}\in (-\pi ,\pi ]$  and they obey the identification  $\mathrm{v}_x^j\equiv \mathrm{v}_x^j\bmod 1$

The key feature of our construction is that, being gapped, the Wannier bands can carry their own topological invariants. These can be evaluated by calculating nested Wilson loops, as follows. Let us start by defining the Wannier band subspaces

$$
\left| w _ {x, k} ^ {\pm} \right\rangle = \sum_ {n = 1, 2} \left| u _ {k} ^ {n} \right\rangle \left[ v _ {x, k} ^ {\pm} \right] ^ {n} \tag {9}
$$

which provide a natural splitting of our original pair of occupied energy bands, which were necessarily degenerate in energy at the special points in the BZ [because of  $\{\hat{m}_x,\hat{m}_y\} = 0]$  into two separate single-band subspaces (we generalize this formalism to arbitrary numbers of occupied energy bands and Wannier bands in (10), Secs. 4, 5, and 6)]. If we define  $F_{y,k}^{\pm} = \langle w_{x,k + \Delta k_y}^{\pm}|w_{x,k}^{\pm}\rangle$  where  $\Delta k_y = (0,2\pi /N_y)$  and  $N_{y}$  is the number of lattice sites along  $y$ , the nested Wilson loops along  $k_{y}$  in the Wannier bands  $\nu_{x}^{\pm}$  are

$$
\tilde {\mathcal {W}} _ {y, k _ {x}} ^ {\pm} = F _ {y, k + N _ {y} \Delta k _ {y}} ^ {\pm} \dots F _ {y, k + \Delta k _ {y}} ^ {\pm} F _ {y, k} ^ {\pm} \tag {10}
$$

and their associated polarizations are

$$
\begin{array}{l} p _ {y} ^ {\nu_ {x} ^ {\pm}} = - \frac {i}{2 \pi N _ {x}} \sum_ {k _ {x}} \log \left[ \tilde {\mathcal {W}} _ {y, k _ {x}} ^ {\pm} \right] \\ = \left\{ \begin{array}{l l} 0 & \frac {| \gamma |}{| \lambda |} > 1 \\ 1 / 2 & \frac {| \gamma |}{| \lambda |} <   1 \end{array} \right. \tag {II} \\ \end{array}
$$

The polarization of  $1/2$  along  $y$  implies that the Wannier Hamiltonian of the  $x$  edge  $H_{\mathcal{W}_x(k)}$  is a topological insulator when  $|\gamma/\lambda| < 1$ , which is in agreement with our findings in the numerical simulation of our model (Fig. 2, C and D). Although the full subspace of occupied energy bands has trivial polarization along  $y$ , each of the separate Wannier band subspaces has nonvanishing polarization. In the thermodynamic limit, the polarization of the Wannier bands is

$$
p _ {y} ^ {\nu_ {x} ^ {\pm}} = - \frac {1}{(2 \pi) ^ {2}} \int_ {B Z} \tilde {\mathcal {A}} _ {y, k} ^ {\pm} d ^ {2} k \tag {12}
$$

where

$$
\tilde {\mathcal {A}} _ {y, k} ^ {\pm} = - i \langle w _ {x, k} ^ {\pm} | \partial_ {k y} | w _ {x, k} ^ {\pm} \rangle \tag {13}
$$

is the Berry potential over Wannier band  $\mathbf{v}_{x}^{\pm}$ , respectively. In (10), Secs. 4 and 5, we provide more formal details of these expressions, as well as their relation with lattice position operators projected into the energy or Wannier-band subspaces.

# Symmetry constraints and quantization

To obtain a well-defined quadrupole moment, we require a crystal with a vanishing bulk polarization—hence, inversion-symmetric (1). To quantize the quadrupole moment, we want to preserve reflection symmetries as well. Under

![](images/c5b10a6d353baed938de06ce96bc000cf41137895b41331940276f139dfbf75d.jpg)  
A

![](images/1c8249f06657f1b41e6eb8bcb27a2a6caba66097b5f916f107ee0daf574b704b.jpg)  
B

![](images/7ac361e8da9f2e1077469ff564af8f996cc1952dfe4aec58bbe193ba038e469d.jpg)  
C

![](images/36416ae6dd3d731f24cdfe0ec24918993a036895fb0ac2ca2813c91aa258da9e.jpg)

![](images/1a3a9cfe71f0aee4ad881227618bc5f87a3a0a7d1e31091d984adb6eb0ac4d31.jpg)  
Fig. 3. Wannier bands for quadrupole insulator and quantized dipole pumping. (A) Wilson loop  $\mathcal{W}_{x,k}$  along  $k_{x}$  at starting point  $k$  over the 2D Brillouin zone. (B) Construction of Wannier bands  $\nu_{x}^{+}(k_{y})$  (marked red) for Bloch Hamiltonian in Eq. 6 by means of Wilson loop diagonalization. (C) Flow of Wannier centers during adiabatic pumping. Wannier centers crossing the Wannier gap have wave functions localized at edges. (D) Wannier-sector polarization as a function of adiabatic parameter for the pumping in (C). There is no change between  $t = \pi$  and  $t = 2\pi$ . (E) Pattern of electric current during this pumping process.

![](images/817b997dca2c7a0db7704e7b1fc3daf483ec23e249c4417bfc546ccbd5a32715.jpg)  
E

![](images/8573b9bce1f8faf02f6fe63f61c65604b9f477818aeff0c2075298f03d3e727d.jpg)  
D

![](images/b44918adcaaee1c04c9d477476bb369cd59ec50daa1d245d71503a137213a76f.jpg)

reflections  $x\to -x(M_x)$  , and  $y\rightarrow -y$ $(M_y)$  ,and inversion  $(x,y)\rightarrow (-x, - y)(\mathcal{I})$  , the polarization of the Wannier-band subspace obeys

$$
p _ {y} ^ {\mathrm {v} _ {x} ^ {+}} \stackrel {M _ {x}} {=} p _ {y} ^ {\mathrm {v} _ {x} ^ {-}}, p _ {y} ^ {\mathrm {v} _ {x} ^ {+}} \stackrel {M _ {y}} {=} - p _ {y} ^ {\mathrm {v} _ {x} ^ {+}}, p _ {y} ^ {\mathrm {v} _ {x} ^ {+}} \stackrel {\mathcal {I}} {=} - p _ {y} ^ {\mathrm {v} _ {x} ^ {-}} \bmod 1 \tag {14}
$$

[(10), Sec. 6]. Hence, the Wannier-sector polarizations  $p_y^{\nu_x}$  and  $p_x^{\nu_y}$  (calculated from  $H_{\mathcal{W}_x}$  and  $H_{\mathcal{W}_y}$ , respectively) take quantized values

$$
p _ {y} ^ {\mathrm {v} _ {x} ^ {\pm}}, p _ {x} ^ {\mathrm {v} _ {y} ^ {\pm}} \stackrel {\mathcal {T}, M _ {x}, M _ {y}} {=} 0 \text {o r} 1 / 2 \tag {15}
$$

when the constraints due to all three symmetries are satisfied. Hence, the most general classification of the Wannier band topology is  $\mathbb{Z}_2\times \mathbb{Z}_2$  with the nontrivial quadrupole state corresponding to the class with symmetry-protected invariants  $(p_y^{\tilde{v}_y},p_x^{\tilde{v}_x}) = (1 / 2,1 / 2)$ . The phases with  $(p_y^{\tilde{v}_y},p_x^{\tilde{v}_x}) = (1 / 2,0)$  or  $(0,1 / 2)$  can be reached by allowing for separate  $x$  and  $y$  hopping parameters  $\lambda_{x},\lambda_{y}$  in Eq.6 and tuning one or the other outside the topological regime,  $|\lambda_i / \gamma | > 1$ . The  $(1 / 2,0)$  and  $(0,1 / 2)$  phases have vanishing quadrupole moment. Hence, in the presence of the quantizing symmetries  $M_{x},M_{y}$  and  $\mathcal{I}$ , the quadrupole invariant  $q_{xy}$  can be identified in terms of these quantities as

$$
q _ {x y} = 2 e p _ {x} ^ {\mathrm {v} _ {y} ^ {\prime}} p _ {y} ^ {\mathrm {v} _ {x} ^ {\prime}} = 0 \text {o r} e / 2 \tag {16}
$$

A transition between the quadrupole phase  $(1/2, 1/2)$  and, for example, the  $(1/2, 0)$  phase is not marked by a closing of the 2D bulk energy gap. Instead, the transition occurs through a bulk-driven energy gap closing in the 1D edge Hamiltonian parallel to the  $y$  axis [a transition on the physical edge not driven by the bulk is not enough because the interior region would still be in the  $(1/2, 1/2)$  phase and thus the boundary of the quadrupole would just recede]. Enforcing  $C_4$  symmetry reduces the classification of the Wannier bands to  $\mathbb{Z}_2$ , and the quadrupole invariant  $q_{xy}$  can be identified as  $q_{xy} = p_y^{\nu_x} = p_x^{\nu_y} = 0$  or  $e/2$ .

These relations can simplify the formula for the corner charge:  $Q^{\mathrm{corner} + x, + y} = p_y^{\mathrm{edge} + x} + p_x^{\mathrm{edge} + y} - q_{xy} = e - q_{xy}$ , which is determined by the bulk quadrupole moment. Transitions between the trivial and quadrupole  $C_4$ -symmetric phases do close the 2D bulk energy gap, as seen in Fig. 2 A.

# Edge currents and quantized dipole pumping

In crystals, corner charges alone do not imply the existence of a quadrupole moment [a counterexample is provided in (10), Sec. 11]. There must exist concomitant edge polarizations satisfying  $Q^{\mathrm{corner} + x, + y} - P_y^{\mathrm{edge} + x} - P_x^{\mathrm{edge} + y} = -q_{xy}$ . Although the edge polarization itself is not an observable quantity, changes in polarization over space or

time are, as they amount to localized charge or charge current, respectively. Thus, even in the absence of corners or other edge inhomogeneities, changes in bulk quadrupole moments over time manifest as (globally) inversion-symmetric, edge-localized currents. In contrast, currents caused by changes in bulk polarization are distributed in the bulk and are induced by breaking inversion symmetry (otherwise, the bulk polarization is locked).

An illustration of such a process is given by the family of Hamiltonians parameterized as  $h_t^q \equiv (\sin t)h^q (k,0) + (\cos t)\Gamma_0$  for  $0\leq t\leq \pi$  and  $h_t^q \equiv (\sin t)(\Gamma_2 + \Gamma_4) + (\cos t)\Gamma_0$  for  $\pi \leq t\leq 2\pi$ . The parameter  $t$  represents the time over which the instantaneous Hamiltonian is adiabatically deformed. Along this entire process, inversion symmetry as well as both the bulk and edge energy gaps are maintained. We enforced the first property in order to lock the bulk polarization to vanish, and the second property for adiabaticity. Electronic transport occurs during the first half of the cycle (the second half of the cycle has only on-site terms that connect two trivial Hamiltonians and therefore cause no transport). In the calculation of Wannier values  $\nu_{x}$  as a function of  $t$  for  $0\leq t\leq \pi$  (Fig. 3C, left) the  $x$  direction is periodic, but the  $y$  direction is open. At each  $t$ , we diagonalize the Hamiltonian  $h_t^q (k_x,y)$  and use the subspace of  $2N_y$  occupied bands as a function of  $k_{x}$  to perform the Wilson loop along  $x$ . The resulting  $2N_y$  Wannier centers are all 0 (mod1) at  $t = 0$ , where the Hamiltonian is  $\Gamma_0$ , which is a trivial insulator. As  $t$  progresses, a pair of Wannier centers with corresponding eigenstates localized at the edges separate from the "bulk" Wannier centers (dark blue lines), approaching the value of  $\nu_{x} = 1 / 2$  at  $t = \pi /2$  (at the symmetry-protected quadrupole phase). Aside from the edge-localized Wannier centers, the bulk Wannier centers remain gapped, which is in agreement with Fig. 3B. For  $t > \pi /2$ , the edge Wannier centers move away from 1/2 toward a value of 0, but toward its neighboring unit cell (Fig. 3C, left). At  $t = \pi$ , all Wannier centers become 0 again as the system becomes a trivial insulator. The second half of the cycle then connects the two trivial insulators  $h_\pi^q = -\Gamma_0$ , with  $h_0^q = \Gamma_0$  via on-site, gap-preserving terms that do not induce any transport. Thus, the net effect is that electrons are pumped along the edge by one unit cell to the left on the top edge, and by one unit cell to the right on the bottom edge. For the same cycle, but with open boundaries along  $x$  and periodic along  $y$ , the Wannier centers along  $y$  are shown in Fig. 3C, right. In both cases, transport is quantized. This quantization is captured by the winding of the Wannier-sector polarization

$$
\Delta q _ {x y} = e \int_ {0} ^ {2 \pi} d t \frac {\partial}{\partial t} p _ {x ^ {\prime}} ^ {\mathrm {v} _ {y} ^ {\pm}} (t) = e \tag {17}
$$

as shown in Fig. 3D. The overall charge transport along horizontal and vertical edges is not that of a circulating current; rather, it follows the pattern shown schematically in Fig. 3E and amounts to

![](images/88f7af287cabfbceadf4c9c33c91f09f6735ae9932d6e0ac15bc236194ce17e4.jpg)  
Fig. 4. Proposal for the experimental realization of a crystalline quadrupole by using ultracold atoms in an optical lattice. Following (24), a Hofstader model can be created by mutually orthogonal standing optical waves in which an ultracold gas is held. A period-2 superlattice (dimerization) can be induced in the xy plane by two additional orthogonal optical waves at double the in-plane wavelengths of the optical lattice. A magnetic field gradient and an additional pair of running wave beams give rise to a tunable flux on the plaquettes.

![](images/6c5c5677fdd4538659b618f9556dd5ca625f64cdb4fe15f8a8a6e5f0af299a26.jpg)

![](images/947a3599f662f3e275ebaccd079768571b53104367e599b0244ab730f2ffed28.jpg)  
Fig. 5. Proposal for realization of quadrupole in a photonic crystal. (A) Effective negative hoppings are achieved by introducing auxiliary waveguides (at center) and fine-tunneling the refractive indices on each individual waveguide. (B) Photonic crystal lattice with nontrivial quadrupole moment. (C) Density of states for a lattice as in (B) with 16 by 16 unit cells and  $d_{\lambda} = 20 \, \mu \mathrm{m}$ ,  $d_{\gamma} = 30 \, \mu \mathrm{m}$ . For these distances, the auxiliary modes are sufficiently detuned and do not affect the quadrupole topological structure at lower energies.

# Fig. 6. 3D insulator with a quantized octupole moment  $o_{xyz}$ . (A)

Hopping terms in the Hamiltonian of Eq. 18.  $\gamma, \lambda$  (shown in left, right, respectively) represent two hopping strengths, and dashed lines represent hopping terms with negative signs. Unit cells are shown in orange boxes. The topological phase occurs when  $|\gamma / \lambda| < 1$ . Numbers indicate basis for  $\Gamma'$ -matrices. (B) Charge density in the topological phase. Corner charges are  $\pm e/2$  relative to background charge. (C) Wannier bands obtained by successively calculating the Wilson loop along  $z$ , then nested Wilson loop along  $y$ , and last, along  $x$ . Each of the 2D Wannier bands

determined by  $\mathcal{W}_{z,k}$  have a nontrivial quadrupole moment  $q_{xy} = \pm e / 2$ , and each of the 1D Wannier bands determined from  $\tilde{\mathcal{W}}_{y,k}$  have a nontrivial polarization  $p_x = \pm e / 2$ .

![](images/55f21704955fd2c7210390363150de604b920a4ca593d5f51a420dc62aed34ab.jpg)

![](images/a33a2b541ab9d9c8e9c9210f0cbab569981b5ffee9a5df10a04bfb65bf364aea.jpg)

pumping a quantum of dipole moment through the bulk of the insulator.

# Proposals for the experimental realizations of the quantized quadrupole moment

We now describe three systems in which the quadrupole topology can be realized and its signatures can be measured.

# Cold atoms in optical lattices

The quadrupole moment can be realized straightforwardly in a system of ultracold atoms in an optical lattice. Our model in Eq. 6 can be constructed from a square lattice Hofstadter model with  $\pi$ -flux per plaquette, with the addition of a superimposed superlattice (Fig. 4). It has already been experimentally demonstrated that such a dimerized lattice in the  $xy$  plane can coexist with a uniform effective flux per plaquette that is fully tunable (24). The effective flux is achieved by first inhibiting the tunneling along the horizontal direction via a linear magnetic gradient that generates a uniform energy offset  $\Delta$  between neighboring sites. The tunneling is resonantly restored by using a pair of far-detuned running wave beams with a frequency difference of  $\omega = \omega_{1} - \omega_{2} = \Delta /h$ . This causes an on-site modulation with spatially dependent phases along the direction of the magnetic gradient (Fig. 4,  $x$  direction). If the

beams are orthogonal, and with a wavevectors  $\mathrm{k}_1\cong$ $\mathrm{k}_2 = 2\pi /\lambda_K,$  then the phases acquired along the horizontal hoppings are  $\varphi_{m,n} = \pi /\lambda_K(\lambda_xm + \lambda_yn)$  where  $(m,n)$  labels the lattice site. Because the phases are acquired only along the horizontal direction, a phase of  $\pi$  per plaquette is obtained by fixing the value of  $\lambda_K$  and  $\lambda_{y}$  to  $\lambda_K = \lambda_y\rightarrow \varphi_{\mathrm{plaquette}} =$ $\pi$  . Although in (24)  $\varphi_{\mathrm{plaqette}}$  was tuned to  $\pi /2$  ,a value of  $\varphi_{\mathrm{plaqette}} = \pi$  has been achieved in a similar setup in (25). As such, this system meets all the requirements to realize the quadrupole model.

# Atom-optics

A second promising direction with cold atoms uses stimulated, two-photon Bragg transitions between free-particle plane-wave momentum states of a Bose-Einstein condensate to mimic electronic tight binding models (26, 27). Essentially, the local atomic orbitals of a tight binding model are replaced by a plane-wave basis. The creation of effective 1D tight binding models, including a 1D topological chain, in a  $^{87}\mathrm{Rb}$  Bose-Einstein condensate was demonstrated in (27, 28). By programming acousto-optic modulators, the amplitude and phases of the laser-induced couplings between momentum states can be precisely controlled. The method can be extended to higher dimensions (26), and the dimerized  $\pi$ -flux lattice needed for our quadrupole model can be generated similarly by using the acousto-optic modulators to tune the amplitudes and phases of the appropriate coupling terms.

# Photonic crystals

Laser-written photonic crystals in fused silica have recently been used to simulate a variety of tight-binding lattice models (29-31). Until recently, our model could not have been easily created in such systems because of the necessity for hoppings with opposite signs that encode the  $\pi$ -flux. However, the construction of a negative coupler was proposed and experimentally demonstrated in (32). To switch from a coupling amplitude  $\lambda$  to  $-\lambda$  between two coupled waveguides, an extra waveguide with on-site energy (which is proportional to the local index of refraction)  $\Delta = (\lambda')^2 / \lambda - \lambda$  is inserted at equal distance in between the two original waveguides, and an on-site potential  $\delta = \lambda$  is added to the two original waveguides (Fig. 5A). Here,  $\lambda'$  is the hopping amplitude between the extra waveguide and an original waveguide. This coupler approximates an effective two-waveguide coupler with negative hopping in its tight-binding approximation as  $\lambda' / \lambda \rightarrow \infty$ . Using this development, a quadrupole model can be achieved by the dimerized waveguide arrangement shown in Fig. 5B. Because the waveguides are evanescently coupled with one another, the hopping amplitude between two waveguides decreases exponentially with their separation  $\lambda \propto e^{-\kappa d_{\lambda}}$ . Thus, the transition between trivial and topological phases is achieved by simply varying the separations  $d_{\lambda}$  and  $d_{\gamma}$ , with the transition point occurring at  $d_{\lambda} = d_{\gamma}$ .

We simulated a 16 by 16 unit-cell photonic lattice as in Fig. 5B [details are provided in (10), Sec. 12]. For a judicious choice of parameters (10),

$\lambda > \gamma$ , and hence the photonic crystal is in the topological phase. This is manifest in the four degenerate, mid-gap energy modes in the density of states (Fig. 5C), which we verified are exponentially localized at the corners. The states localized at the auxiliary waveguides are well separated in energy from those that determine the quadrupole topology. To probe this phase experimentally, a corner waveguide can be illuminated, and its diffusion into neighboring waveguides can be tracked. In particular, in the trivial phase, we expect the initial beam to spread into the bulk, whereas in the topological phase, the beams are expected to remain confined to the corner.

# Model with quantized octupole moment

A simple, minimal model in 3D with quantized octupole moment has Bloch Hamiltonian (Fig. 6A)

$$
\begin{array}{l} \hbar_ {\delta} ^ {0} (k) = \lambda \sin (k _ {y}) \Gamma_ {1} ^ {\prime} + \lambda \cos (k _ {y}) \Gamma_ {2} ^ {\prime} + \\ \lambda \sin (k _ {x}) \Gamma_ {3} ^ {\prime} + \lambda \cos (k _ {x}) \Gamma_ {4} ^ {\prime} + \\ \lambda \sin \left(k _ {z}\right) \Gamma_ {5} ^ {\prime} + \lambda \cos \left(k _ {z}\right) \Gamma_ {6} ^ {\prime} + \delta \Gamma_ {0} ^ {\prime} \tag {18} \\ \end{array}
$$

where  $\Gamma_{i}^{\prime} = \sigma_{3}\otimes \Gamma_{i}$  for  $i = 0,1,2,3,\Gamma_4^\prime = \sigma_1\otimes I_{4\times 4},$ $\Gamma_5^{\prime} = \sigma_{2}\otimes I_{4\times 4}$  and  $\Gamma_6^{\prime} = i\Gamma_0^{\prime}\Gamma_1^{\prime}\Gamma_2^{\prime}\Gamma_3^{\prime}\Gamma_4^{\prime}\Gamma_5^{\prime}$  . This insulator has two energy bands, each of which is fourfold degenerate. At half filling, and with  $\delta = 0$  the insulator has a quantized octupole moment  $o_{xyz} = \pm e / 2$  when  $\gamma /\lambda \in (-1,1)$  . The quantized moment is protected by the presence of all three reflection symmetries and inversion symmetry. For  $\delta \neq 0$  , the crystal has tetrahedral symmetry and the octupole moment loses its quantization, whereas  $p_{x,y,z}$  and  $q_{xy,yz,xz}$  retain theirs. An infinitesimal value  $\delta \neq 0$  is used in the fully open, cubic geometry of Fig. 6B to slightly split the degeneracy of the eight, mid-gap, corner localized states. This generates charges  $\pm e / 2$  localized at the corners in an octupolar pattern.

To characterize the bulk topology, we calculated the Wilson loop along the  $i$ th direction ( $i = x, y$ , or  $z$ ), and our model generates gapped 2D Wannier bands in the orthogonal  $jk$  plane in momentum space (Fig. 6C). Each Wannier band is twofold degenerate and has a nontrivial quadrupole topology with a quantized  $q_{jk}$  moment. We characterized the quadrupole topology by calculating the nested Wilson loop along the  $j$ th direction over one set of the 2D Wannier bands. This further split the twofold degenerate 2D bands into nondegenerate, gapped 1D Wannier bands (Fig. 6C). We then calculated a final nested Wilson loop in the  $k$ th direction and found a value of  $-1$  in the nontrivial octupole phase [10], Sec. 13]. In the nontrivial phase with  $o_{xyz} = \pm e/2$ , this result is independent of the order  $ijk$ . Physically, this hierarchy of Wilson loops implies that the corner charges are manifestations of bound, surface quadrupole moments. The surface quadrupoles meet at the hinges of the cube, giving rise to bound charge polarizations; last, the polarizations converge/diverge from the corners, giving the bound charge density. Because the topology is protected by spatial symmetries, these sharp

interfaces allow us to generate boundaries on the boundary to uncover the surface topology.

# REFERENCES AND NOTES

1. J. Zak, Phys. Rev. Lett. 62, 2747-2750 (1989).  
2. T. L. Hughes, E. Prodan, B. A. Bernevig, Phys. Rev. B 83, 245132 (2011).  
3. A. M. Turner, Y. Zhang, R. S. Mong, A. Vishwanath, Phys. Rev. B 85, 165120 (2012).  
4. K. Klitzing, G. Dorda, M. Pepper, Phys. Rev. Lett. 45, 494-497 (1980).  
5. D. Thouless, M. Kohmoto, M. Nightingale, M. Den Nijs, Phys. Rev. Lett. 49, 405-408 (1982).  
6. F. D. Haldane, Phys. Rev. Lett. 61, 2015-2018 (1988).  
7. X.-L. Qi, T. L. Hughes, S.-C. Zhang, Phys. Rev. B 78, 195424 (2008).  
8. A. M. Essin, J. E. Moore, D. Vanderbilt, Phys. Rev. Lett. 102, 146805 (2009).  
9. R. E. Raab, O. L. De Lange, Multipole Theory in Electromagnetism: Classical, quantum, and symmetry aspects, with applications: Classical, quantum, and symmetry aspects, with applications (OUP Oxford, 2004).  
10. Materials and methods are available as supplementary materials.  
11. R. D. King-Smith, D. Vanderbilt, Phys. Rev. B 47, 1651-1654 (1993).  
12. D. Vanderbilt, R. D. King-Smith, Phys. Rev. B 48, 4442-4455 (1993).  
13. Y. Zhou, K. M. Rabe, D. Vanderbilt, Phys. Rev. B 92, 041102 (2015).  
14. L. Fidkowski, T. S. Jackson, I. Klich, Phys. Rev. Lett. 107, 036601 (2011).  
15. S. Kivelson, Phys. Rev. B 26, 4269-4277 (1982).  
16. N. Marzari, D. Vanderbilt, Phys. Rev. B 56, 12847-12865 (1997).  
17. S. Coh, D. Vanderbilt, Phys. Rev. Lett. 102, 107603 (2009).  
18. R. Yu, X. L. Qi, A. Bernevig, Z. Fang, X. Dai, Phys. Rev. B 84, 075119 (2011).  
19. X.-L. Qi, Phys. Rev. Lett. 107, 126803 (2011).  
20. A. Alexandradinata, X. Dai, B. A. Bernevig, Phys. Rev. B 89, 155114 (2014).  
21. A. Alexandradinata, B. A. Bernevig, Phys. Rev. B 93, 205104 (2016).  
22. Z. Wang, A. Alexandradinata, R. J. Cava, B. A. Bernevig, Nature 532, 189-194 (2016).  
23. A. Alexandradinata, Z. Wang, B. A. Bernevig, Phys. Rev. X 6, 021008 (2016).  
24. M. Aidsburger et al., Phys. Rev. Lett. 111, 185301 (2013).  
25. H. Miyake, G. A. Siviloglou, C. J. Kennedy, W. C. Burton, W. Ketterle, Phys. Rev. Lett. 111, 185302 (2013).  
26. B. Gadway, Phys. Rev. A 92, 043606 (2015).  
27. E. J. Meier, F. A. An, B. Gadway, Phys. Rev. A 93, 051602 (2016).  
28. E. J. Meier, F. A. An, B. Gadway, Nat. Commun. 7, 13986 (2016).  
29. M. C. Rechtsman et al., Nature 496, 196-200 (2013).  
30. M. C. Rechtsman et al., Phys. Rev. Lett. 111, 103901 (2013).  
31. Y. Plotnik et al., Nat. Mater. 13, 57-62 (2014).  
32. R. Keil et al., Phys. Rev. Lett. 116, 213901 (2016).

# ACKNOWLEDGMENTS

We thank C. Fang and A. Soluyanov for useful discussions and B. Gadway for useful discussions and for pointing us to (31). W.A.B. and T.L.H. thank the U.S. National Science Foundation under grant DMR-1351895 and the Sloan Foundation for support. B.A.B. acknowledges support from U.S. Department of Energy grant DE-SC0016239, NSF EAGER grant DMR-1643312, Simons Investigator award ONR - N00014-14-1-0330, Army Research Office Multidisciplinary University Research Initiative grant W911NF-12-1-0461, NSF-Materials Research Science and Engineering Center grant DMR-1420541, and the Packard Foundation and Schmidt Fund for Innovative Research.

# SUPPLEMENTARY MATERIALS

www.sciencemag.org/content/357/6346/61/suppl/DC1

Materials and Methods

Supplementary Text

Figs. S1 to S15

Tables S1 and S2

References (33-35)

25 July 2016; accepted 2 June 2017

10.1126/science.aah6442

# Quantized electric multipole insulators

Wladimir A. Benalcazar, B. Andrei Bernevig and Taylor L. Hughes

Science 357 (6346), 61-66.

DOI: 10.1126/science.aah6442

# Corner-dwelling topological states

Computing the electric polarization of a crystal is surprisingly tricky, but it can be tackled with the help of a topological concept, the so-called Berry phase. Extensions to higher multiple moments, such as quadrupole and octupole, are even trickier. Benalcazar et al. built a theoretical framework for dealing with these moments in certain types of solids. In the presence of some crystalline symmetries, the quadrupole moment is quantized, and the corners of the system play host to fractionally charged, topologically protected states. These predictions may be testable in cold atom and photonic systems.

Science, this issue p. 61

# ARTICLE TOOLS

http://science.sciencemag.org/content/357/6346/61

# SUPPLEMENTARY MATERIALS

http://science.sciencemag.org/content/suppl/2017/07/06/357.6346.61.DC1

# REFERENCES

This article cites 33 articles, 0 of which you can access for free http://science.sciencemag.org/content/357/6346/61#BIBL

# PERMISSIONS

http://www.sciencemag.org/help/reprints-and-permissions

Use of this article is subject to the Terms of Service