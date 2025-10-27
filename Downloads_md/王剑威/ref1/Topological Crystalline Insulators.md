# Topological Crystalline Insulators

Liang Fu

Department of Physics, Harvard University, Cambridge, Massachusetts 02138, USA

(Received 5 October 2010; revised manuscript received 31 December 2010; published 8 March 2011)

The recent discovery of topological insulators has revived interest in the band topology of insulators. In this Letter, we extend the topological classification of band structures to include certain crystal point group symmetry. We find a class of three-dimensional "topological crystalline insulators" which have metallic surface states with quadratic band degeneracy on high symmetry crystal surfaces. These topological crystalline insulators are the counterpart of topological insulators in materials without spin-orbit coupling. Their band structures are characterized by new topological invariants. We hope this work will enlarge the family of topological phases in band insulators and stimulate the search for them in real materials.

DOI: 10.1103/PhysRevLett.106.106802

PACS numbers: 73.20.-r, 73.43.-f

The topology of band structures is important in the study of topological phases of matter. Historically, the quantization of Hall conductance in the integer quantum Hall effect was explained by the Thouless-Kohmoto-Nightingale- den Nijs integer (also known as Chern number) of occupied energy bands [1]. Recently, the topological classification of spin-orbital coupled band structures with time-reversal symmetry has played a key role in the theoretical prediction of topological insulators [2-4]. The subsequent development of topological band theory [5], combined with realistic band structure calculations, has proven useful in the material search for topological insulators.

Inspired by the discovery of topological insulators, the classification of band structures has been extended to other discrete symmetry classes such as particle-hole symmetry [6-8], which leads to a rich family of topological phases such as topological superconductors [6,9]. More recently, the classification of magnetic insulators with certain magnetic translation symmetry has been studied [10,11]. Finding these phases in real materials is interesting and challenging.

The purpose of this Letter is to extend the classification of band structures in a different direction—to include crystal point group symmetries. We introduce the notion of “topological crystalline insulators,” which cannot be smoothly connected to a trivial atomic insulator when time-reversal  $(T)$  symmetry and certain point group symmetry are respected. Unlike time-reversal symmetry, crystal symmetries can be broken by sample surfaces. As a result, a low-symmetry surface of a topological crystalline insulator does not have robust surface states. This motivates us to study a class of three-dimensional topological crystalline insulators which have fourfold  $(C_4)$  or sixfold  $(C_6)$  rotational symmetry. As we will show, its (001) surface, which preserves the rotational symmetry, supports gapless surface states. These topological crystalline insulators are the counterpart of topological insulators in materials without spin-orbit coupling. Instead, an electron's

orbital degrees of freedom play a role similar to spin. Unlike the linearly dispersing Dirac surface states of topological insulators, the (001) surface states of topological crystalline insulators have quadratic band degeneracy protected by time-reversal and discrete rotational symmetry[12,13].

The outline of this Letter is as follows. First we introduce a simple tight-binding model in a tetragonal crystal with  $C_4$  symmetry. We explicitly show that gapless surface states exist on the (001) crystal face. The topological stability of surface states suggests a nontrivial phase in this model. Next we define a new  $Z_2$  topological invariant for generic time-reversal-invariant band structures with  $C_4$  or  $C_6$  symmetry in three dimensions. This establishes the topological crystalline insulator phase. Finally, we discuss the electronic properties of quadratic surface bands.

Tight-binding model.-Consider a tetragonal lattice with a unit cell of two inequivalent atoms  $A$  and  $B$  along the  $c$  axis, as shown in Fig. 1(a). The 3D crystal can be viewed as a stack of bilayer square lattices in the  $ab$  plane. We now introduce a tight-binding model to describe the band structure of an electron's  $p$  orbitals (or  $d$  orbitals, see the next paragraph). In particular, we are interested in the energy bands derived from  $p_x$  and  $p_y$  orbitals. We assume that these bands do not overlap with the  $p_z$  bands, and construct

![](images/62caa9b78c1c4b300793864f4e212bc7ec222e9af75a2a07e16ac1ddba38bf1b.jpg)  
(a)  
FIG. 1 (color online). (a) Tetragonal lattice with two atoms  $A$  and  $B$  along the  $c$  axis in the unit cell. (b) The Brillouin zone and four high symmetry points.

![](images/1a7844edc68bfa70df8289feae562df04ac4876065156c0c27d1f7fe55a69b5b.jpg)  
(b)

a tight-binding model from Wannier functions with the same symmetry as  $p_x$  and  $p_y$  orbitals. The Hamiltonian  $H$  consists of intralayer hopping  $H^A$  and  $H^B$ , as well as interlayer hopping  $H^{AB}$ :

$$
H = \sum_ {n} H _ {n} ^ {A} + H _ {n} ^ {B} + H _ {n} ^ {A B},
$$

$$
H _ {n} ^ {a} = \sum_ {i, j} t ^ {a} (\mathbf {r} _ {i} - \mathbf {r} _ {j}) \sum_ {\alpha , \beta} c _ {a \alpha} ^ {\dagger} (\mathbf {r} _ {i}, n) e _ {\alpha} ^ {i j} e _ {\beta} ^ {i j} c _ {a \beta} (\mathbf {r} _ {j}, n),
$$

$$
\begin{array}{l} H _ {n} ^ {A B} = \sum_ {i, j} t ^ {\prime} \left(\mathbf {r} _ {i} - \mathbf {r} _ {j}\right) \left[ \sum_ {\alpha} c _ {A \alpha} ^ {\dagger} \left(\mathbf {r} _ {i}, n\right) c _ {B \alpha} \left(\mathbf {r} _ {j}, n\right) + \mathrm {H . c .} \right] \tag {1} \\ + t _ {z} ^ {\prime} \sum_ {i} \sum_ {\alpha} [ c _ {A \alpha} ^ {\dagger} (\mathbf {r} _ {i}, n) c _ {B \alpha} (\mathbf {r} _ {i}, n + 1) + \mathrm {H . c .} ]. \\ \end{array}
$$

Here, each site is specified by  $(n,\mathbf{r},a)$ , where  $n$  labels the bilayer unit cell along the  $c$  axis,  $\mathbf{r} = (x,y)$  labels the  $ab$ -plane coordinate,  $a = A$ ,  $B$  labels the sublattice, and  $\alpha, \beta$  label the  $p_x, p_y$  orbital. Two types of  $p$ -orbital hopping terms appear in  $H$ . The intralayer hopping in  $H^a$  is of  $\sigma$ -bonding type: it depends on the relative orientation of the  $p$  orbital and the hopping direction  $\mathbf{e}^{ij} = (\mathbf{r}_i - \mathbf{r}_j) / |\mathbf{r}_i - \mathbf{r}_j|$ . The interlayer hopping in  $H^{AB}$  is orbital independent. Written in this form, the tight-binding Hamiltonian manifestly preserves crystal symmetries. The hopping amplitudes  $t^a$ ,  $t'$ , and  $t_z'$  between two sites depend on their  $ab$ -plane distance  $\mathbf{r}_i - \mathbf{r}_j$ . Throughout this Letter, we assume spin-orbit coupling is negligible, so that the electron's spin index is omitted.

We emphasize that the form of the Hamiltonian  $H$  is entirely determined by crystal symmetry. Because  $d_{xz,yz}$  orbitals transform in the same way as  $p_{x,y}$  orbitals under  $C_4$ , (1) also applies to materials with these  $d$  orbitals. Therefore, (1) is potentially relevant to a large class of materials including transition metal compounds with  $t_{2g}$  orbitals near Fermi energy.

To obtain a minimal model for topological crystalline insulators, we include the nearest and next-nearest neighbor intralayer hoppings in  $H^{a}$  with the amplitude  $t_1^a$  and  $t_2^a$ , as well as nearest and next-nearest neighbor interlayer hoppings in  $H^{AB}$  with the amplitude  $t_1'$  and  $t_2'$ . The corresponding Bloch Hamiltonian  $H(\mathbf{k})$  is obtained by Fourier transform:

$$
\begin{array}{l} H (\mathbf {k}) = \left( \begin{array}{c c} H ^ {A} (\mathbf {k}) & H ^ {A B} (\mathbf {k}) \\ H ^ {A B \dagger} (\mathbf {k}) & H ^ {B} (\mathbf {k}) \end{array} \right), \\ H ^ {a} (\mathbf {k}) = 2 t _ {1} ^ {a} \left( \begin{array}{c c} \cos k _ {x} & 0 \\ 0 & \cos k _ {y} \end{array} \right) \tag {2} \\ + 2 t _ {2} ^ {a} \left( \begin{array}{c c} \cos k _ {x} \cos k _ {y} & \sin k _ {x} \sin k _ {y} \\ \sin k _ {x} \sin k _ {y} & \cos k _ {x} \cos k _ {y} \end{array} \right), \\ \end{array}
$$

$$
H ^ {A B} (\mathbf {k}) = \left[ t _ {1} ^ {\prime} + 2 t _ {2} ^ {\prime} \left(\cos k _ {x} + \cos k _ {y}\right) + t _ {z} ^ {\prime} e ^ {i k _ {z}} \right] I.
$$

The band structure is shown in Fig. 2(a) for the following set of parameters:  $t_1^A = -t_1^B = 1$ ,  $t_2^A = -t_2^B = 0.5$ ,  $t_1' = 2.5$ ,  $t_2' = 0.5$ ,  $t_z' = 2$ . We have checked that the energy gap is finite everywhere in the Brillouin zone. As long as

![](images/e85c103f2cf6b1a0fdcd6b972cb36b0f35ce0087182bd35c32035513cfb5786e.jpg)

![](images/e30ec222cbe708e947de38d66b344cdbf88a123100539ffc2a9ebe401c78e703.jpg)  
FIG. 2 (color online). (a) Bulk band structure of the tight-binding model along high symmetry lines. (b) Surface states with quadratic band touching exist on (001) face. The tight-binding parameters are shown in the text below Eq. (2).

the energy gap does not close, the system remains in the same topological class within a finite parameter range.

To study surface states, we solve  $H$  in a slab geometry. We find that the existence of gapless surface states crucially depends on the surface termination. Consider the high symmetry (001) surface, which preserves the  $C_4$  symmetry. Here surface states exist and transverse the whole energy gap as shown in Fig. 2, leading to a 2D surface metal. Note that surface states are doubly degenerate at  $\bar{M} = (\pi, \pi)$ : one in  $p_x$  orbital and the other in  $p_y$  orbital. Because  $\bar{M}$  is a fixed point under fourfold rotation, the doublet forms a two-dimensional irreducible real representation of  $C_4$  symmetry, as a result of time-reversal symmetry for electrons without spin-orbit coupling (i.e., spinless fermions). Surface band dispersion near  $\bar{M}$  can be obtained from  $k \cdot p$  theory. We introduce a pseudospin  $\sigma_z = \pm 1$  to label the  $p_x$  and  $p_y$  orbital of the doublet. In this basis,  $C_4$  rotation is represented by  $e^{i\sigma_y\pi/4}$  and time-reversal operator  $T$  is represented by complex conjugation. Up to a gauge transformation, the form of the  $k \cdot p$  Hamiltonian  $\mathcal{H}$  is dictated by symmetry:

$$
\mathcal {H} \left(k _ {x}, k _ {y}\right) = \frac {k ^ {2}}{2 m _ {0}} + \frac {k _ {x} ^ {2} - k _ {y} ^ {2}}{2 m _ {1}} \sigma_ {z} + \frac {k _ {x} k _ {y}}{2 m _ {2}} \sigma_ {x}. \tag {3}
$$

Perturbations which break either  $C_4$  or  $T$  symmetry can open up an energy gap and destroy the protected surface states. This can be seen explicitly by adding a  $C_4$ -breaking term  $M_1k_x\sigma_y + M_2\sigma_z$  or a  $T$ -breaking term  $M\sigma_y$  to  $\mathcal{H}$ . Similar quadratic bands have been recently studied in 2D photonic crystals [12] and fermion models [13]. Our tight-binding model does not have gapless surface states for other surface terminations which break the  $C_4$  symmetry.

When  $T$  and  $C_4$  symmetry are preserved, the surface states shown above are topologically protected. This can be understood by considering the surface band dispersion along  $\bar{\Gamma}\bar{M}$ . Within our model, surface states (if present) must be doubly degenerate at  $\bar{\Gamma}$  and  $\bar{M}$ . As a consequence, there exist two distinct types of surface band connectivity along  $\bar{\Gamma}\bar{M}$ , having an even or odd number of band crossings at Fermi energy, respectively. Surface states with even crossings are fragile: they can be pushed out of the energy gap by changing the surface potential. Surface states with odd crossings have a Fermi surface which encloses  $\bar{\Gamma}$  an odd number of times. They cannot be removed. These two types of surface states imply the existence of two topologically distinct phases of time-reversal-invariant band insulators with fourfold symmetry. The reasoning here closely follows the previous study of topological insulators [14].

$Z_{2}$  topological invariant. We now show that a  $Z_{2}$  topological invariant  $\nu_{0} = 0$ , 1 characterizes the band structure of 3D time-reversal-invariant insulators with fourfold rotation symmetry (without spin-orbit coupling).  $\nu_{0} = 0$  corresponds to a trivial phase adiabatically connected to an atomic insulator.  $\nu_{0} = 1$  corresponds to a topological crystalline insulator which has gapless surface states on the (001) surface.

We start by examining the symmetry property of Bloch wave functions of occupied bands:  $|\psi_{n}(\mathbf{k})\rangle = e^{i\mathbf{k}\cdot \mathbf{r}}|u_{n}(\mathbf{k})\rangle$ , where  $|u_{n}(\mathbf{k})\rangle$  is the cell-periodic eigenstates of the Bloch Hamiltonian  $H(\mathbf{k})\equiv e^{-i\mathbf{k}\cdot \mathbf{r}}He^{i\mathbf{k}\cdot \mathbf{r}}$ . Here the unit cell is chosen to be invariant under  $C_4$  rotation around the  $z$  axis.  $H(\mathbf{k})$  satisfies

$$
H \left(k _ {x}, k _ {y}, k _ {z}\right) = U H \left(k _ {y}, - k _ {x}, k _ {z}\right) U ^ {- 1}, \tag {4}
$$

$$
H (k _ {x}, k _ {y}, k _ {z}) = T H (- k _ {x}, - k _ {y}, - k _ {z}) T ^ {- 1}.
$$

Here the unitary operator  $U = e^{i\hat{L}_z\pi /2}$  implements  $C_4$  rotation within the unit cell  $(\hat{L}_z = xP_y - yP_x$  is angular momentum operator). The antiunitary operator  $T = K$  (complex conjugation) implements time-reversal transformation for spinless fermions, with the property  $T^2 = 1$ . As a result, time-reversal symmetry by itself does not guarantee a twofold degeneracy. However, the combination of time-reversal and fourfold rotational symmetry can lead to protected degeneracies at four special momenta  $\Gamma = (0,0,0)$ ,  $M = (\pi ,\pi ,0)$ ,  $A = (\pi ,\pi ,\pi)$ ,  $Z = (0,0,\pi)$  in the 3D Brillouin zone [Fig. 1(b)]. At such a high symmetry point  $\mathbf{k}_i$ ,  $H(\mathbf{k}_i)$  commutes with  $U$ , so that the energy bands  $|u_{n}(\mathbf{k}_{i})\rangle$  are eigenstates of fourfold rotation with possible eigenvalues  $1, -1, i$  and  $-i$ . Moreover, because  $H(\mathbf{k}_i)$  is real, energy bands at  $\mathbf{k}_i$  with  $\pm i$  eigenvalues are guaranteed to be degenerate, forming a two-dimensional irreducible real representation of  $C_4$ . For example, such doublet bands can derive from  $(p_x,p_y)$  orbitals or  $(d_{xz},d_{yz})$  orbitals. From now on, we consider a set of energy bands  $|u_{n}(\mathbf{k})\rangle$ ,  $n = 1,\dots,2N$ , which are doubly degenerate  $E_{2n - 1}(\mathbf{k}_i) = E_{2n}(\mathbf{k}_i)$  at  $\Gamma$ ,  $M$ ,  $A$ , and  $Z$ . As we will see below, only these doublet bands admit a  $Z_{2}$  classification.

The  $Z_{2}$  topological invariant  $\nu$  is defined in terms of the electron wave functions:

$$
(- 1) ^ {\nu_ {0}} = (- 1) ^ {\nu_ {\Gamma M}} (- 1) ^ {\nu_ {A Z}}, \tag {5}
$$

$$
(- 1) ^ {\nu_ {\mathbf {k} _ {1} \mathbf {k} _ {2}}} = \exp \left(i \int_ {\mathbf {k} _ {1}} ^ {\mathbf {k} _ {2}} d \mathbf {k} \cdot \mathcal {A} _ {\mathbf {k}}\right) \frac {\operatorname {P f} [ w (\mathbf {k} _ {2}) ]}{\operatorname {P f} [ w (\mathbf {k} _ {1}) ]},
$$

$$
\mathcal {A} _ {\mathbf {k}} \equiv - i \sum_ {j} \left\langle u _ {j} (\mathbf {k}) \right| \partial_ {\mathbf {k}} \left| u _ {j} (\mathbf {k}) \right\rangle , \tag {6}
$$

$$
w _ {m n} (\mathbf {k} _ {i}) \equiv \langle u _ {m} (\mathbf {k} _ {i}) | U T | u _ {n} (\mathbf {k} _ {i}) \rangle .
$$

$\mathcal{A}_{\mathbf{k}}$  is the  $U(1)$  Berry connection and  $w(\mathbf{k}_i)$  is an antisymmetric  $U(2N)$  matrix because  $[H(\mathbf{k}_i), UT] = 0$  and  $(UT)^2 = -1$ . Pf stands for the Pfaffian. We now specify the integration path in (6). For  $\nu_{\Gamma M}$ , the integral is along an arbitrary line connecting  $\Gamma$  and  $M$  which lies within the 2D plane  $k_z = 0$  in the Brillouin zone as shown in Fig. 1(b). Likewise, the integration path for  $\nu_{AZ}$  lies in the plane  $k_z = \pi$ .

Both  $\mathcal{A}$  and  $w$  depend on the choice of basis  $|u_{j}(\mathbf{k})\rangle$ , but we now prove that  $\nu_{\mathbf{k}_1\mathbf{k}_2}$  is gauge invariant. Two different bases  $|\tilde{u}_n(\mathbf{k})\rangle$  and  $|u_{n}(\mathbf{k})\rangle$  are related by a  $U(2N)$  gauge transformation:

$$
| \tilde {u} _ {n} (\mathbf {k}) \rangle = \mathcal {G} _ {n m} (\mathbf {k}) | u _ {m} (\mathbf {k}) \rangle , \quad \mathcal {G} \in U (2 N). \tag {7}
$$

This leads to the corresponding gauge transformation of  $\mathcal{A}$  and  $w$ :

$$
\begin{array}{l} \tilde {\mathcal {A}} = \mathcal {A} - i \operatorname {T r} [ \mathcal {G} ^ {- 1} \partial_ {\mathbf {k}} \mathcal {G} ] = \mathcal {A} - i \partial_ {\mathbf {k}} \log (\det [ \mathcal {G} ]) \tilde {w} \\ = G ^ {*} w G ^ {\dagger}. \tag {8} \\ \end{array}
$$

Using the identity  $\mathrm{Pf}[X^T MX] = \operatorname*{det}[X]\mathrm{Pf}[M]$ , it is straightforward to verify that  $\tilde{\nu}_{\mathbf{k}_1\mathbf{k}_2} = \nu_{\mathbf{k}_1\mathbf{k}_2}$  is gauge invariant.

We now further show that  $(-1)^{v_{\mathbf{k}_1\mathbf{k}_2}} = \pm 1$  is a  $Z_{2}$  quantity. It follows from (4) that at the two 2D planes  $k_z = 0$  and  $k_z = \pi$ ,  $H(\mathbf{k})$  has the symmetry property:  $H(\mathbf{k}) = \Xi H(\mathbf{k})\Xi$ ,  $\Xi \equiv U^2 T$ . This allows us to choose a real gauge along the integration path to evaluate (6):

$$
\Xi \left| u _ {m} (\mathbf {k}) \right\rangle = - \left| u _ {m} (\mathbf {k}) \right\rangle . \tag {9}
$$

Because  $\Xi$  is antiunitary,  $\mathcal{A} = 0$  everywhere along the integration path. So in this gauge  $(-1)^{\nu[\mathbf{k}_1,\mathbf{k}_2]}$  reduces to

$$
(- 1) ^ {\nu_ {\mathbf {k} _ {1} \mathbf {k} _ {2}}} = \operatorname {P f} [ w (\mathbf {k} _ {2}) ] / \operatorname {P f} [ w (\mathbf {k} _ {1}) ]. \tag {10}
$$

Because  $|u_{m}(\mathbf{k}_{i})\rangle$  belong to the two-dimensional representation of the  $C_4$  group, we have  $U^2 |u_m(\mathbf{k}_i)\rangle = -|u_m(\mathbf{k}_i)\rangle$  so that the gauge condition (9) at  $\mathbf{k}_i$  is equivalent to  $T|u_{m}(\mathbf{k}_{i})\rangle = |u_{m}(\mathbf{k}_{i})\rangle$  ; i.e., the wave function is real. Under this reality condition, the matrix  $w(\mathbf{k}_i)$  simplifies to

$$
w _ {m n} \left(\mathbf {k} _ {i}\right) = \langle u _ {m} \left(\mathbf {k} _ {i}\right) | U | u _ {n} \left(\mathbf {k} _ {i}\right) \rangle . \tag {11}
$$

Now, by choosing a particular kind of real basis  $|u_{2m}(\mathbf{k}_i)\rangle \equiv U|u_{2m - 1}(\mathbf{k}_i)\rangle$ ,  $w(\mathbf{k}_i)$  reduces to a standard form  $w^0 = \epsilon \oplus \epsilon \oplus \dots \oplus \epsilon$ , which is a direct sum of

$N2\times 2$  Levi-Civita tensors. This means that in a generic real basis,  $w(\mathbf{k}_i)$  can be written as

$$
w \left(\mathbf {k} _ {i}\right) = O ^ {T} \left(\mathbf {k} _ {i}\right) w ^ {0} O \left(\mathbf {k} _ {i}\right), \quad O \left(\mathbf {k} _ {i}\right) \in O (2 N). \tag {12}
$$

So we have

$$
\operatorname {P f} \left[ w \left(\mathbf {k} _ {i}\right) \right] = \det  \left[ O \left(\mathbf {k} _ {i}\right) \right] \operatorname {P f} \left[ w ^ {0} \right] = \det  \left[ O \left(\mathbf {k} _ {i}\right) \right] = \pm 1. \tag {13}
$$

This proves that  $(-1)^{\nu_{\mathbf{k}_1\mathbf{k}_2}} = \pm 1$  is a gauge invariant  $Z_{2}$  quantity. So both  $\nu_{\Gamma M}$  and  $\nu_{AZ}$  are  $Z_{2}$  topological invariants which characterize the band structures in the 2D momentum space  $k_z = 0$  and  $k_z = \pi$ , respectively. Their product  $\nu_0$  is defined for 3D time-reversal-invariant insulators with  $C_4$  symmetry and determines the surface state property: gapless surface states exist on (001) face only when  $\nu_0 = 1$ . This is verified in the tight-binding model (1). The relation between  $\nu_0$  and  $\nu_{\Gamma M}$ ,  $\nu_{AZ}$  is analogous to that of strong and weak  $Z_{2}$  index in 3D topological insulators [15-17].

Generalization to crystals with  $C_6$  symmetry.-The study of topological crystalline insulators with  $C_4$  symmetry can be generalized to hexagonal crystal structures with  $C_6$  symmetry. In that case, (001) surface states have quadratic degeneracy points either at  $\bar{\Gamma}$  or two equivalent  $\bar{K}$ . The topological invariant is similarly defined by Eq. (6) from the electron wave functions on the lines  $\Gamma K$  and  $AH$  in the Brillouin zone. A concrete tight-binding model can be obtained by placing (1) in a layered triangular lattice. The details will be reported elsewhere.

The fact that the above  $Z_{2}$  invariant is only defined for doublet bands illustrates the important interplay between symmetry representation and topology of energy bands in solids, a feature absent in other known classes of topological insulators. We are not aware of a systematic mathematical approach to classifying vector bundles (e.g., electron wave functions over the Brillouin zone) with given representations of group action (e.g.,  $C_4$  rotation) at fixed points (e.g., high symmetry momenta  $\mathbf{k}_i$ ). We hope the concrete topological invariant (6) can stimulate continuing research on topological crystalline insulators with other lattice structures.

The occupied bands of real materials usually have both doubly degenerate and nondegenerate singlet components. Provided that the doublet bands are energetically separable from the singlet ones (i.e., no band crossing between them), the  $Z_{2}$  invariant remains well defined for the former. The coexistence with singlet bands can, in principle, weaken the stability of surface states [18], although this scenario seems unlikely to happen in reality.

Surface states with quadratic degeneracy.-Quadratic degeneracies in 2D band structure have attracted considerable interest recently. The  $k\cdot p$  Hamiltonian (3) is widely used as a low energy approximation for the band structure of bilayer graphene near  $\pm K$  points. However, unlike topological crystalline insulators, the quadratic degeneracy there is not protected by symmetry. Instead, the band

dispersion very close to  $\pm K$  becomes linear due to trigonal warping effects.

Electron interactions can drive 2D bands with quadratic degeneracy into a variety of interesting broken symmetry phases, including quantum anomalous Hall state, nematic phase, etc. [13]. The competition between different ordered phases is of great interest in bilayer graphene. It remains to see what happens in the single-valley quadratic surface states of topological crystalline insulators.

It would be interesting to generalize the concept of topological crystalline insulators to interacting systems. For example, crystal symmetry is known to play an important role in the topological classification of spin liquids [19], spin chains [20], and Mott insulators [21]. A unifying theory of symmetry protected topological phases remains to be developed. We also note that analogs of topological crystalline insulators can be potentially realized in photonic crystals.

Part of this work was done at University of Pennsylvania under the support of NSF Grant No. DMR-0906175. We thank Charlie Kane and Jeffrey Teo for very helpful discussions, and acknowledge support from the Harvard Society of Fellows.

[1] D.J. Thouless et al., Phys. Rev. Lett. 49, 405 (1982).  
[2] M.Z. Hasan and C.L. Kane, Rev. Mod. Phys. 82, 3045 (2010).  
[3] J.E. Moore, Nature (London) 464, 194 (2010).  
[4] X.L. Qi and S.C. Zhang, arXiv:1008.2026.  
[5] L. Fu and C.L. Kane, Phys. Rev. B 76, 045302 (2007).  
[6] A. P. Schynder, S. Ryu, A. Furusaki, and A. W. W. Ludwig, Phys. Rev. B 78, 195125 (2008).  
[7] A. Kitaev, arXiv:0901.2686.  
[8] Y. Ran, arXiv:1006.5454.  
[9] X. L. Qi et al., Phys. Rev. Lett. 102, 187001 (2009); M. M. Salomaa and G. E. Volovik, Phys. Rev. B 37, 9298 (1988); R. Roy, arXiv:0803.2868.  
[10] R. S. K. Mong, A. M. Essin, and J. E. Moore, Phys. Rev. B 81, 245209 (2010).  
[11] See also, e.g., R. Li et al., Nature Phys. 6, 284 (2010).  
[12] Y. D. Chong, X.-G. Wen, and M. Soljacic, Phys. Rev. B 77, 235125 (2008).  
[13] K. Sun et al., Phys. Rev. Lett. 103, 046811 (2009).  
[14] C.L. Kane, Nature Phys. 4, 348 (2008).  
[15] L. Fu, C.L. Kane, and E.J. Mele, Phys. Rev. Lett. 98, 106803 (2007).  
[16] J.E. Moore and L. Balents, Phys. Rev. B 75, 121306(R) (2007).  
[17] R. Roy, Phys. Rev. B 79, 195322 (2009)  
[18] See supplemental material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.106.106802 for a detailed study.  
[19] G. Wen, Phys. Rev. B 65, 165113 (2002).  
[20] Z. C. Gu and X. G. Wen, Phys. Rev. B 80, 155131 (2009); F. Pollmann et al., Phys. Rev. B 81, 064439 (2010).  
[21] H. Yao and S. A. Kivelson, Phys. Rev. Lett. 105, 166402 (2010).