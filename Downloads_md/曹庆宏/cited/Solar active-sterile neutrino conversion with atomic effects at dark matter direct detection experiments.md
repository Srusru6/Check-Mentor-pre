RECEIVED: December 21, 2021

REVISED: March 18, 2022

ACCEPTED: April 11, 2022

PUBLISHED: May 13, 2022

# Solar active-sterile neutrino conversion with atomic effects at dark matter direct detection experiments

# Shao-Feng Ge, Pedro Pasquini and Jie Sheng

Tsung-Dao Lee Institute (TDLI) & School of Physics and Astronomy (SPA), Shanghai Jiao Tong University (SJTU), Shanghai 200240, China

Key Laboratory for Particle Astrophysics and Cosmology (MOE)

Shanghai Key Laboratory for Particle Physics and Cosmology, Shanghai Jiao Tong University, Shanghai 200240, China

E-mail: gesf@sjtu.edu.cn, ppasquini@sjtu.edu.cn,

shengjie04@sjtu.edu.cn

ABSTRACT: The recent XENON1T excess can be explained by the solar active-sterile neutrino conversion with bound electrons via light mediator. Nevertheless, the atomic effects are usually omitted in the solar neutrino explanations. We systematically establish a second quantization formalism for both bound and ionized electrons to account for the atomic effects. This formalism is of great generality to incorporate various interactions for both neutrino and dark matter scatterings. Our calculation shows that the change in the cross section due to atomic effects can have important impact on the differential cross section. It is necessary to include atomic effects in the low-energy electron recoil signal at dark matter direct detection experiments even for energetic solar neutrinos. With the best-fit values to the XENON1T data, we also project the event rate at PandaX-4T, XENONnT, and LZ experiments.

KEYWORDS: Beyond Standard Model, Neutrino Physics, Solar and Atmospheric Neutrinos

ARXIV EPRINT: 2112.05560

# Contents

1 Introduction 1  
2 Neutrino-electron scattering with atomic effects 2

2.1 Second quantization of bound and ionized electron states 3  
2.2 Atomic effects in neutrino-electron scattering 5

3 Neutrino scattering into a massive sterile neutrino with light mediators 10

3.1 Neutrino scattering with free or bound electrons 10  
3.2 The cross section enhancement from atomic effects 13

4 Experimental constraints 15  
5 Predictions for future DM experiments 19  
6 Conclusions 21

# 1 Introduction

The particle nature and properties of dark matter (DM) can be probed by the direct detection experiments, typically utilizing nuclear or electron recoils [1]. Recently, the XENON1T experiment found an excess in the electron recoil spectrum around  $(2\sim 3)\mathrm{keV}$  [2] which was independently checked by the PandaX-II experiment [3]. Although solar neutrinos can also scatter with electron via the Standard Model (SM) weak interactions, this signal can contribute only  $0.52\%$  of the total events as background and more importantly the electron recoil spectrum is quite flat in the observed keV range [4]. The excess might indicate new physics beyond the SM (BSM) if not the tritium background [5]. Possible explanations include axion or axion-like particles [6-14], elastic [15-25] and inelastic [26-37] scattering between DM and electron, the Migdal effect of DM scattering with nuclei [38], and DM decay [39-41, 41, 42]. Another possibility is sterile neutrino as DM in our galaxy. Either the sterile neutrino DM inelastically scatters with electron into active neutrino and releases its mass as energy in electron recoil [43, 44] or sterile neutrino decays inside the detector to produce a photon signal [45].

In addition, light neutrinos can also provide an explanation. Especially, the Sun is a natural source of energetic neutrino fluxes around Earth. While the SM neutrino interactions can only produce a flat event spectrum, a low energy peak arises if there is a BSM interaction with light mediator. Possible realizations include magnetic dipole moment, charge radius and anapole [3, 46-54], all with the massless photon as mediator. In addition, light scalar [55-57] and vector [55-63] mediators can also achieve the same purpose. It is interesting to observe that only scalar and vector mediators have been used to explain the

low energy peak while the pseudo-scalar one was claimed to be incapable of achieving the goal [56]. However, if neutrino scattering with electron into a massive sterile neutrino in the final state, a light pseudo-scalar mediator can also produce a peak in the low recoil energy [64]. The  $\mathcal{O}(100)\mathrm{keV}$  sterile neutrino can also be applied with dipole magnetic moment interactions to explain the excess [65].

For an  $\mathcal{O}(\mathrm{keV})$  electron recoil energy, the momentum transfer is comparable with the atomic energy of a heavy element such as Xe. The electrons inside atom can no longer be treated as a free particle. Instead, one should use quantum wave functions to describe the electron distribution. It is the electron cloud rather than a single electron particle that participates in the scattering process. This has been extensively explored for the DM scattering with electron in recent years [66-71]. The effect of the initial- and final-state electron wave functions can be summarized into a  $K$ -factor [71] or sometimes  $f$ -factor [66] as function of the momentum transfer  $\mathbf{q}$ . The size of atomic effect is typically  $\mathcal{O}(1)$  and hence not negligible.

Being usually unnoticed, the atomic effect with electron cloud has also been considered in the study of neutrino electromagnetic properties. Since the massless photon is exactly a light mediator, the momentum transfer in neutrino scattering with photon mediation is intrinsically suppressed in the same way as the low energy electron recoil at DM detectors. So the atomic effect cannot be neglected in the study of neutrino electromagnetic properties. For example, the ionization effect due to the neutrino scattering with bound electrons is obtained by considering the binding energy and the initial wave function in light atoms [72, 73]. Later, the effect of atomic potential on the final-state electron is also taken into consideration when calculating the cross section [74-76]. Although the atomic effect was claimed to be small [76], recent studies realize that it is actually not negligible [77, 78]. Even spin effects have been studied very lately [79].

In this work, we study the neutrino scattering with bound electrons into a massive sterile neutrino to explain the observed electron recoil peak at  $(2\sim 3)\mathrm{keV}$  and make projections for the future DM experiments. In section 2, we first summarize the formalism of calculating the neutrino scattering with both free and bound electrons in the language of second quantization. Especially, the bound electron is directly quantized using annihilation and creation operators without involving the inappropriate plane waves or equivalently momentum eigenstates. Section 3 shows the cross section of neutrino electron scattering including the atomic effect and compare it with the free electron scattering case. The results are further used in section 4 to fit the observed data with  $\chi^2$  minimization to constrain the parameter space and the prospect of detecting such signal at future experiments is projected in section 5. Finally we summarize and conclude in section 6.

# 2 Neutrino-electron scattering with atomic effects

As mentioned above, the atomic effects need to be considered in order to make a precise study of the electron recoil signal from DM or neutrino scattering. The initial-state electron is bound inside the atom instead of being free. In contrast, the final-state electron is knocked out of the atom and becomes ionized leaving a recoil signal in the detector. With a recoil

energy around  $(2\sim 3)\mathrm{keV}$ , the ionized electron is not completely free but is subject to the atomic Coulomb potential. One needs to consider the atomic effect for both the initial- and final-state electrons. We first try to establish a unified second quantization description of the bound and ionized states in section 2.1 and then use it to calculate the atomic  $K$ -factor in section 2.2. This formalism of second quantization can accommodate general interactions and apply not just for neutrino but also DM scatterings.

# 2.1 Second quantization of bound and ionized electron states

An electron trapped in the Coulomb potential is no longer a free particle and hence cannot be described by plane wave with fixed momentum. Instead, the conserved variable is the energy eigenvalue including both kinetic energy and Coulomb potential. To be concrete, the bound electron field  $e_B(x)$  is in general a function of spatial coordinates [80],

$$
e _ {B} (x) = \sum_ {n l m} a _ {n l m} e ^ {- i E _ {n l} t} \psi_ {n l m} (\mathbf {x}), \tag {2.1}
$$

where  $a_{nlm}\left(a_{nlm}^{\dagger}\right)$  is the creation (annihilation) operator for the bound state with principal  $(n)$ , angular  $(l)$ , and magnetic  $(m)$  quantum numbers. Since positron never enters our discussion, we can safely omit  $b_{nlm}^{\dagger}$  in (2.1) from the beginning. When acting on the vacuum state  $|0\rangle$ , the creation operator  $a_{nlm}^{\dagger}$  gives the bound state  $|nlm\rangle \equiv a_{nlm}^{\dagger}|0\rangle$ . There is no need to involve the  $\sqrt{2E}$  prefactor that is necessary for a relativistic particle to keep Lorentz covariance but reduces to a constant  $\sqrt{2m}$  and hence can be combined into normalization for a non-relativistic particle. Similarly, we follow the convention of second quantization to define the anti-commutation relations,  $\{a_{nlm}, a_{n'l'm'}^{\dagger}\} = \delta_{nn'} \delta_{ll'} \delta_{mm'}$  and  $\{a_{nlm}, a_{n'l'm'}\} = \{a_{nlm}', a_{n'l'm'}^{\dagger}\} = 0$ . With dimensionless discrete  $\delta$  functions, the creation and annihilation operators are also dimensionless,  $[a_{nlm}] = [a_{nlm}^{\dagger}] = 0$ , and the bound electron field has the same dimension as its wave function,  $[e_B(x)] = [\psi_{nlm}(\mathbf{x})]$ . The normalization condition of the wave function,  $\int \psi_{nlm}^{\dagger}(\mathbf{x}) \psi_{n'l'm'}(\mathbf{x}) d^3\mathbf{x} = \delta_{nn'} \delta_{ll'} \delta_{mm'}$ , fixes the field dimension to be  $[e_B(x)] = 3/2$  which is consistent with quantum field theory (QFT). Although the momentum integration is replaced by a summation  $\sum_{nlm}$ , the second quantized field  $e_B(x)$  is still a linear combination of energy and angular momentum eigenstates. However, the second quantized field  $e_B(x)$  in (2.1) is different from the usual formalism of a free particle in quantum field theory [81] with the evolution phase  $e^{-iE_{nl}t}$  containing only the energy eigenvalue and time dependence while the spatial dependence in the electron wave function  $\psi_{nlm}(\mathbf{x})$  cannot be factorized out as a simple complex phase.

For an ionized electron that is still under the influence of the atomic Coulomb potential, its energy is continuously distributed. The corresponding ionized electron field contains an integration over the asymptotic momentum,

$$
e _ {I} (x) = \sum_ {l m} \int \frac {| \mathbf {p} | ^ {2} d | \mathbf {p} |}{(2 \pi) ^ {3}} a _ {T _ {r} l m} \psi_ {T _ {r} l m} (\mathbf {x}) e ^ {- i T _ {r} t}, \tag {2.2}
$$

without involving a principal quantum number. The asymptotic kinetic energy  $T_{r} \equiv |\mathbf{p}|^{2} / 2m_{e}$  is the one that we can experimentally measure. Comparing with the bound case in (2.1), the only difference is that the energy eigenvalue changes from a discrete principal

quantum number  $n$  to a continuous  $T_{r}$  or equivalently the asymptotic momentum  $|\mathbf{p}|$ . Similar to the summation over discrete variables, the asymptotic momentum is integrated. In other words, the second quantized field  $e_I(x)$  is also a linear combination of energy and angular momentum eigenstates. With one-to-one correspondence between the asymptotic energy  $T_{r}$  and the asymptotic momentum  $|\mathbf{p}|$ , the latter is also a well defined physical quantity. The ionized electron behaves essentially as a free particle when  $|\mathbf{x}| \to \infty$  and its wave function reduces to a plane wave [82]. The direction of the asymptotic momentum can also be used to label an ionized electron in the similar way as its magnitude. The Fourier transformation for the asymptotic state at infinity distance ( $|\mathbf{x}| \to \infty$ ) is,  $\psi(\mathbf{x}) = \int \frac{d^3\mathbf{p}}{(2\pi)^3} \psi(\mathbf{p}) e^{-i\mathbf{p} \cdot \mathbf{x}}$ . However, the DM direct detection experiments cannot tell the directional information and are sensitive to only the magnitude  $|\mathbf{p}|$  or the recoil energy  $T_{r}$ . Namely, the relevant wave function is  $\psi_{T_r}(\mathbf{x}) \equiv \int d\Omega_{\mathbf{p}} \psi(\mathbf{p}) e^{-i\mathbf{p} \cdot \mathbf{x}}$  and the remaining phase space integration is exactly the  $|\mathbf{p}|^2 d|\mathbf{p}|$  used in (2.2),  $\psi(\mathbf{x}) = \int \frac{|\mathbf{p}|^2 d|\mathbf{p}|}{(2\pi)^3} \psi_{T_r}(\mathbf{x})$ . The original anti-commutation relation  $\{a_{\mathbf{plm}}, a_{\mathbf{p}'l'm'}^\dagger\} = (2\pi)^3 \delta_{ll'} \delta_{mm'} \delta^{(3)}(\mathbf{p} - \mathbf{p}')$  reduces to  $\{a_{T_rlm}, a_{T_r'l'm'}^\dagger\} = (2\pi)^3 \delta_{ll'} \delta_{mm'} \delta(|\mathbf{p}| - |\mathbf{p}'|)/|\mathbf{p}|^2$  after integrating away the angular information of the asymptotic momentum  $\mathbf{p}$ . Correspondingly, the operator dimension is,  $[a_{T_rlm}] = -3/2$  and the wave function  $\psi_{T_rlm}(\mathbf{x})$  for ionized state is dimensionless. This is consistent with the wave function normalization,  $\int \psi_{T_rlm}^\dagger(\mathbf{x}) \psi_{T_r'l'm'}(\mathbf{x}) d^3\mathbf{x} = (2\pi)^3 \delta_{ll'} \delta_{mm'} \delta(|\mathbf{p}| - |\mathbf{p}'|)/|\mathbf{p}|^2$  [68]. Using the non-relativistic dispersion relation,  $T_r = |\mathbf{p}|^2 / 2m_e$ , one can prove that,  $\left[\delta(|\mathbf{p}| - |\mathbf{p}'|)/|\mathbf{p}|^2\right] \times |\mathbf{p}|^2 d|\mathbf{p}| = \delta(T_r - T_r') dT_r$  and the normalization condition becomes,  $\int \psi_{T_rlm}^\dagger(\mathbf{x}) \psi_{T_r'l'm'}(\mathbf{x}) d^3\mathbf{x} = (2\pi)^3 \delta_{ll'} \delta_{mm'} \delta(T_r - T_r')$  [82] to make everything consistent. Similar to the bound state, an ionized state  $|T_rlm\rangle \equiv a_{T_rlm}^\dagger |0\rangle$  is created from vacuum by  $a_{T_rlm}^\dagger$  without involving the energy prefactor  $\sqrt{2E}$ .

The wave function can be constructed from the field,  $\langle 0|e_B(x)|nlm\rangle = \psi_{nlm}(\mathbf{x})e^{-iE_nt}$  for the bound state and  $\langle 0|e_I(x)|T_rlm\rangle = \psi_{T_rlm}(\mathbf{x})e^{-iT_rt}$  for the ionized one. In addition to the spatial distribution, the wave function should also contain the spin information. The spinor wave function  $\psi_N(\mathbf{x})$  is a solution of the covariant Dirac equation in the presence of electromagnetic field,  $[i\partial / - m - eA]\psi_N(x) = 0$ , where  $N\equiv (nIm)$  and  $N\equiv (T_{r}lm)$  for the bound and ionized states, respectively. For a stationary energy eigenstate,  $\psi_N(x) = e^{-iE_Nt}\psi_N(\mathbf{x})$ , the time dependence can be removed from the Dirac equation,

$$
\gamma^ {0} [ i \pmb {\gamma} \cdot \pmb {\nabla} + m ] \psi_ {N} (\mathbf {x}) = [ E _ {N} - V (| \mathbf {x} |) ] \psi_ {\mathbf {N}} (\mathbf {x}). \tag {2.3}
$$

For clarity, we have only kept the electric potential  $V(|\mathbf{x}|)$  in the atom as a central force. In the non-relativistic limit, the spatial and spin parts separate into [80],

$$
\psi_ {N, s} (\mathbf {x}) \approx \frac {1}{\sqrt {2}} \left( \begin{array}{c} (1 + i \pmb {\sigma} \cdot \nabla / 2 m _ {e}) f _ {N, s} (\mathbf {x}) \\ (1 - i \pmb {\sigma} \cdot \nabla / 2 m _ {e}) f _ {N, s} (\mathbf {x}) \end{array} \right), \qquad f _ {N, s} (\mathbf {x}) \equiv \phi_ {N} (\mathbf {x}) \xi_ {s}, \qquad (2. 4)
$$

for spin  $s$  and other quantum numbers  $N$ . The information of spatial distribution and spin is represented by the single-valued wave function  $\phi_N(\mathbf{x})$  and the two-component spinor  $\xi_s$ , respectively. The normalization condition can be rewritten in terms of  $\phi_N(\mathbf{x})$ ,  $\int d^3\mathbf{x}\psi_{N,s}^\dagger (\mathbf{x})\psi_{N',s'}(\mathbf{x})\approx \int d^3\mathbf{x}\phi_N^* (\mathbf{x})\phi_{N'}(\mathbf{x}) = 1$ . For a heavy element such as Xenon, the binding energy is typically  $\mathcal{O}(1\sim 10)$  keV. According to the Virial theorem, the electron

kinetic energy is of the same size, which is roughly  $0.1\% \sim 1\%$  of the electron mass,  $m_e \approx 511\mathrm{keV}$ . In other words, the effect of special relativity or spinor structure represented by the gradient expansion is roughly  $0.1\% \sim 1\%$ .

# 2.2 Atomic effects in neutrino-electron scattering

With the second quantization formalism of the bound and ionized states established, we can follow the usual QFT calculation of transition rate and differential distributions. For a general four-fermion coupling  $(\bar{\nu}\Gamma_{\nu}\nu_{s})(\bar{e}\Gamma_{e}e)$  between neutrino and electron, the transition matrix element  $\mathcal{T}$  is,

$$
\mathcal {T} \equiv \int d ^ {4} x d ^ {4} y \langle T _ {r} l ^ {\prime} m ^ {\prime}; \mathbf {p} _ {s} | [ \bar {\nu} (x) \Gamma_ {\nu} \nu_ {s} (x) \phi^ {*} (x) ] [ \bar {e} (y) \Gamma_ {e} e (y) \phi (y) ] | n l m; \mathbf {p} _ {\nu} \rangle , \tag {2.5}
$$

with  $\phi$  generally denoting a mediator with mass  $M$  and  $\mathbf{p}_{\nu}(\mathbf{p}_s)$  is the solar (sterile) neutrino momentum. For generality,  $\Gamma_{\nu},\Gamma_{e}\equiv 1,\gamma_{5},\gamma^{\mu},\gamma_{5}\gamma^{\mu},\sigma^{\mu \nu}$  denote all the possible Lorentz structures. Correspondingly, the mediator  $\phi$  can be a scalar (S), pseudo-scalar (P), vector (V), axial-vector (A), or even tensor particle. The  $\mathcal{T}$  matrix element should also contain coupling constants which are omitted for simplicity. Note that the tensor case is included just for completeness when illustrating the atomic effects but not discussed when being applied to the realistic case of sterile-active neutrino conversion. This is because the tensor current is typically mediated by a spin-2 particle such as the graviton that is beyond the scope of this work. The other types with scalar, pseudo-scalar, or vector mediator will be elaborated in the coming section 3 and section 4.

When acting field operators on the initial  $|nlm,p_{\nu}\rangle \equiv a_{nlm}^{\dagger}a_{\mathbf{p}_{\nu}}^{\dagger}|0\rangle$  and final  $|T_{r}lm,p_{s}\rangle \equiv a_{T_{r}lm}^{\dagger}a_{\mathbf{p}_{s}}^{\dagger}|0\rangle$  states, the  $a_{nlm}$  operator from  $e_B(y)$  annihilates a bound state while the  $a_{T_rlm}^\dagger$  operator from  $\bar{e}_I(y)$  creates an ionized state at position  $\mathbf{y}$ . The  $\mathcal{T}$  matrix becomes,

$$
\mathcal {T} = \bar {u} _ {\nu} (p _ {\nu}) \Gamma_ {\nu} u _ {s} (p _ {s}) \frac {i}{q ^ {2} - M ^ {2}} \int d ^ {4} y e ^ {- i q \cdot y} \overline {{\psi}} _ {T _ {r} l ^ {\prime} m ^ {\prime}} (\mathbf {y}) \Gamma_ {e} \psi_ {n l m} (\mathbf {y}) e ^ {i \Delta E _ {n l} t}, \qquad (2. 6)
$$

after integrating away first the coordinate  $x$  and the momentum transfer  $q$ . The  $x$  integration produces a  $\delta$ -function of four momentum,  $\delta^{(4)}(p_{\nu} - p_{s} - q)$ , to impose energy momentum conservation on the neutrino vertex,  $q = p_{\nu} - p_{s}$ . From the bound and ionized electron fields, one can extract an explicit energy dependence,  $\Delta E_{nl} \equiv T_r - E_{nl}$ , as the exponential factor  $e^{i\Delta E_{nl}t}$ . This allows imposing energy conservation on the electron vertex by integrating away the time component  $y^0$ ,

$$
\begin{array}{l} \mathcal {T} = \frac {i \bar {u} _ {\nu} (p _ {\nu}) \Gamma_ {\nu} u _ {s} (p _ {s})}{q ^ {2} - M ^ {2}} \int d ^ {3} \mathbf {y} e ^ {i \mathbf {q} \cdot \mathbf {y}} \overline {{\psi}} _ {T _ {r} l ^ {\prime} m ^ {\prime}} (\mathbf {y}) \Gamma_ {e} \psi_ {n l m} (\mathbf {y}) \\ \times \delta \left(\Delta E _ {n l} - E _ {\nu} + \sqrt {m _ {s} ^ {2} + \left| \mathbf {p} _ {\nu} \right| ^ {2} + \left| \mathbf {q} \right| ^ {2} - 2 \left| \mathbf {p} _ {\nu} \right\| \mathbf {q} | \cos \theta_ {q v}}\right). \tag {2.7} \\ \end{array}
$$

Together with the  $\delta^{(4)}(p_{\nu} - p_{s} - q)$  function on the neutrino side, energy is conserved both locally and globally while the momentum conservation only applies to the neutrino vertex. This is the key difference between the calculations of the scattering process with free or bound electron. For free electron, the spatial dependence of their wave functions can also

factorize out as exponential factors and the integration  $\int d^4 y$  can impose both energy and momentum conservations. The physical reason behind this is that a bound electron does not have a definite momentum, especially in the coordinate representation. Consequently, we can only get a product of the initial and final wave functions.

Note that the  $\delta_{E} \equiv \delta (\Delta E_{nl} - E_{\nu} + \sqrt{m_{s}^{2} + |\mathbf{p}_{\nu}|^{2} + |\mathbf{q}|^{2}} - 2|\mathbf{p}_{\nu}\| \mathbf{q}|\cos \theta_{qv})$  function in (2.7) for energy conservation can be moved outside of the  $\int d^3\mathbf{y}$  integration since it only depends on energy and momentum. The spatial integration with bound and ionized wave functions,  $A_{e} \equiv \int d^{3}\mathbf{y} e^{i\mathbf{q}\cdot \mathbf{y}}\overline{\psi}_{T_{r}l^{\prime}m^{\prime}}(\mathbf{y})\Gamma_{e}\psi_{nlm}(\mathbf{y})$ , is essentially the source of the atomic  $K$ -factor. Nevertheless, the wave functions  $\psi_{nlm}$  and  $\psi_{T_r l'm'}$  have spinor  $\xi$  that needs to be singled out in order to obtain the  $\mathcal{M}$  matrix element. For a scalar interaction  $(\Gamma_{e} = 1)$ , the electron amplitude  $A_{e}$  divides into two parts,

$$
A _ {e} ^ {S} \equiv \frac {\bar {u} (m _ {e}) u (m _ {e})}{2 m _ {e}} \int d ^ {3} \mathbf {y} e ^ {i \mathbf {q} \cdot \mathbf {y}} \phi_ {T _ {r} l ^ {\prime} m ^ {\prime}} ^ {*} (\mathbf {y}) \phi_ {n l m} (\mathbf {y}), \tag {2.8}
$$

when expanded to the linear order of  $i\nabla f_{N,s}$ . The two-component spinor  $\xi$  that is momentum independent has been reexpressed,  $\bar{u}(m_e)u(m_e) = 2m_e\xi^\dagger \xi$ , in terms of the electron spinor  $u(m_e)$  at rest. The spinor and spatial wave function then factorize into two parts,  $A_e^S \equiv [\bar{u}(m_e)u(m_e)/(2m_e)] \times f_{nlm}^{T_r l'm'}(\mathbf{q})$  where  $f_{nlm}^{T_r l'm'}(\mathbf{q})$  is the so-called atomic form factor [66, 68, 71],

$$
f _ {n l m} ^ {T _ {r} l ^ {\prime} m ^ {\prime}} (\mathbf {q}) \equiv \int d ^ {3} \mathbf {y} e ^ {i \mathbf {q} \cdot \mathbf {y}} \phi_ {T _ {r} l ^ {\prime} m ^ {\prime}} ^ {*} (\mathbf {y}) \phi_ {n l m} (\mathbf {y}). \tag {2.9}
$$

The factorization of the scattering amplitude into two parts, one for the spinor and the other for the atomic form factor, is a generic feature when expanding to the leading order. For all the possible electron bilinears,

$$
A _ {e} ^ {S, P, V, A, T} \equiv \bar {u} (m _ {e}) \left\{\frac {1}{2 m _ {e}}, \frac {\gamma_ {0} \mathbf {q} \cdot \boldsymbol {\gamma} \gamma^ {5}}{4 m _ {e} ^ {2}}, \frac {\gamma^ {0}}{2 m _ {e}}, \frac {\gamma^ {5} \gamma^ {i}}{2 m _ {e}}, \frac {[ \gamma^ {i} , \gamma^ {j} ]}{2 m _ {e}} \right\} u (m _ {e}) f _ {n l m} ^ {T _ {r} l ^ {\prime} m ^ {\prime}} (\mathbf {q}). \tag {2.10}
$$

The key feature here is that the initial- and final-state electrons are not momentum eigenstates or free-particle solution of the Dirac equations. Instead, the bound and ionized spinors are originally a function of the spatial coordinates (2.4). There is no need to involve initial and final momentum for electrons at all. The only momentum that can appear is the momentum transfer  $\mathbf{q}$ . Especially for the pseudo-scalar case, the electron spin or equivalently  $\gamma^i$  with a spatial index is relevant. However, only the inner product  $\mathbf{q} \cdot \boldsymbol{\gamma}$  can appear as a combination to keep the scalar nature of this vertex. This factorization is derived with second quantization for the bound and ionized electron wave functions in a systematic way.

With  $A_{e}$  factorization, the  $\mathcal{T}$  matrix element (2.7) is composed of several contributions,  $\mathcal{T} \equiv \mathcal{M}f_{nlm}^{T_r l'm'}(\mathbf{q})\delta_E$ , where  $\mathcal{M}$  is the scattering matrix element,

$$
\mathcal {M} \equiv \frac {i \bar {u} _ {\nu} (p _ {\nu}) \Gamma_ {\nu} u _ {s} (p _ {s})}{q ^ {2} - M ^ {2}} \bar {u} (m _ {e}) \left\{\frac {1}{2 m _ {e}}, \frac {\gamma_ {0} \mathbf {q} \cdot \boldsymbol {\gamma} \gamma^ {5}}{4 m _ {e} ^ {2}}, \frac {\gamma^ {0}}{2 m _ {e}}, \frac {\gamma^ {5} \gamma^ {i}}{2 m _ {e}}, \frac {[ \gamma^ {i} , \gamma^ {j} ]}{2 m _ {e}} \right\} u (m _ {e}). \qquad (2. 1 1)
$$

Note that  $\mathcal{M}$  is a function of the incoming neutrino momentum  $p_{\nu}$  and the momentum transfer  $\mathbf{q}$  while the sterile neutrino momentum  $p_{s} = p_{\nu} - q$  is a dependent variable.

Following the derivations in the section 4.5 of [81], the scattering cross section with a bound electron can be also expressed in terms of  $\mathcal{M}$ ,

$$
\sigma_ {n l} \equiv \frac {1}{2 l + 1} \int \frac {| {\bf p} | ^ {2} d | {\bf p} |}{(2 \pi) ^ {3}} \int \frac {d ^ {3} {\bf q}}{(2 \pi) ^ {3} 2 E _ {s}} \frac {1}{8 m _ {e} ^ {2} E _ {\nu}} \overline {{{| \mathcal {M} | ^ {2}}}} (2 \pi) \delta_ {E} \sum_ {m, l ^ {\prime} m ^ {\prime}} \left| f _ {n l m} ^ {T _ {r} l ^ {\prime} m ^ {\prime}} ({\bf q}) \right| ^ {2}, \qquad (2. 1 2)
$$

for a single electron target. The prefactor  $1 / (2l + 1)$  accounts for the degenerate electrons with  $m = -l, -l + 1, \dots, l - 1, l$  while  $\overline{|\mathcal{M}|^2} \equiv |\mathcal{M}|^2 / 2$  is averaged over the electron spin. For the high energy solar neutrino that contains mainly the left-handed neutrinos, there is no need to average over the neutrino spin. Since the asymptotic kinetic energy  $T_r = |\mathbf{p}|^2 / 2m_e$  is the one that can be experimentally measured, it is much more convenient to express the phase space integration  $|\mathbf{p}|^2 d|\mathbf{p}| = \frac{1}{2}(2m_e T_r)^{3/2} d\ln T_r$  in terms of  $T_r$ . The original phase space integration for the sterile neutrino momentum  $\mathbf{p}_s$  has also been replaced by the momentum transfer  $\mathbf{q}$  due to momentum conservation of the neutrino vertex. In addition, the combined neutrino and atom system has rotational invariance around the incoming neutrino momentum  $\mathbf{p}_{\nu}$ . So the azimuthal angle of  $\mathbf{q}$  can be integrated away to give  $2\pi$ . The zenith angle  $\theta_{q\nu}$  integration is reduced by the  $\delta_E$  to  $\int \delta_E d\cos \theta_{q\nu} = E_s / E_\nu |\mathbf{q}|$  with  $\cos \theta_{q\nu} = (m_s^2 + |\mathbf{q}|^2 + E_\nu^2 - E_s^2) / 2E_\nu |\mathbf{q}|$ . The allowed range of the scattering angle,  $\cos \theta_{q\nu} \leq 1$ , gives the  $|\mathbf{q}|$  integration range,  $E_\nu - \sqrt{E_s^2 - m_s^2} \leq |\mathbf{q}| \leq E_\nu + \sqrt{E_s^2 - m_s^2}$  with  $E_s = E_\nu - \Delta E_{nl}$ . Putting things together, the differential cross section of the recoil energy  $T_r$  becomes,

$$
\frac {d \sigma_ {n l}}{d T _ {r}} \equiv \frac {1}{T _ {r}} \int \frac {| \mathbf {q} | d | \mathbf {q} |}{4 \pi} \frac {1}{8 m _ {e} ^ {2} E _ {\nu} ^ {2}} \overline {{| \mathcal {M} | ^ {2}}} K _ {n l} (T _ {r}, \mathbf {q}). \tag {2.13}
$$

The atomic effect can now be parameterized as the so-called  $K$ -factor,

$$
K _ {n l} \left(T _ {r}, \mathbf {q}\right) \equiv \frac {1}{2} \frac {\left(2 m _ {e} T _ {r}\right) ^ {3 / 2}}{(2 \pi) ^ {3}} \frac {1}{2 l + 1} \sum_ {m, l ^ {\prime} m ^ {\prime}} \left| f _ {n l m} ^ {T _ {r} l ^ {\prime} m ^ {\prime}} (\mathbf {q}) \right| ^ {2}. \tag {2.14}
$$

The  $1/(2l + 1)$  factor accounts for the average over the initial magnetic quantum number  $m$ . Usually, the direct detection experiments can only distinguish the energy deposit but not the angular quantum numbers  $m$  for the initial- and  $\{l', m'\}$  for the final-state electrons. So these quantum numbers are summed over when defining the  $K$ -factor in (2.14). For completeness, we rewrite the  $K$ -factor more explicitly [67],

$$
K _ {n l} \left(T _ {r}, | \mathbf {q} |\right) = \frac {\left(2 m _ {e} T _ {r}\right) ^ {3 / 2}}{2 (2 \pi) ^ {3}} \sum_ {l ^ {\prime} L} \left(2 l ^ {\prime} + 1\right) \left(2 L + 1\right) \left| \int r ^ {2} d r j _ {L} \left(\left| \mathbf {q} \right| r\right) R _ {T _ {r} l ^ {\prime}} ^ {*} (r) R _ {n l} (r) \right| ^ {2} \binom {l ^ {\prime} L l} {0 0 0} ^ {2}, \tag {2.15}
$$

with the wave functions divided into radial and angular parts,  $\phi_{nlm}(\mathbf{r}) = R_{nl}(r)Y_{lm}(\hat{r})$  and  $\phi_{T_r l'm'}(\mathbf{r}) = R_{T_r l'}(r)Y_{l'm'}(\hat{r})$ . For convenience, the spatial integration variable  $\mathbf{y}$  has been replaced by  $\mathbf{r}$  and  $r$  is radius. The Bessel function  $j_L(|\mathbf{q}|r)$  originates from the exponential  $e^{i\mathbf{q}\cdot \mathbf{y}}$  of (2.9). After integrating over the solid angles, only the radial functions [82]  $R_{nl}$  for the bound and  $R_{T_r l'}$  for the ionized electrons survive. Most importantly, the  $K$ -factor becomes no longer a function of  $\mathbf{q}$  but its magnitude  $|\mathbf{q}|$ .

Note that the normalization of  $K$ -factor varies in literature [66, 68, 71, 83]. In our definition (2.15), the summation over  $m$  and  $m'$  gives a factor of  $2l + 1$  and  $2l' + 1$ , respectively.

That  $2l + 1$  factor has been canceled with the one in (2.14). With this convention, (2.15) defines the average  $K$ -factor for a single electron in the  $nl$  state and (2.13) is the cross section per electron. In principle, the final-state angular quantum number  $l'$  should sum up to infinity. However, in practice the summation is cut off at sufficiently large  $l' \sim \mathcal{O}(100)$  and higher contributions are neglected [71, 83].<sup>1</sup>

To see the basic features of the  $K$ -factor more clearly, let us compare the scattering with free and bound electrons. If the electron is not tightly bound in the atom, or equivalently  $n \to \infty$ , the whole process should reduce to the scattering with a free electron. The differential cross section of the scattering with a free electron is,

$$
\frac {d \sigma^ {0}}{d T _ {r}} = \frac {1}{T _ {r}} \int | \mathbf {q} | ^ {2} d | \mathbf {q} | \frac {\overline {{| \mathcal {M} | ^ {2}}}}{6 4 \pi m _ {e} ^ {2} | \mathbf {p} _ {\nu} | ^ {2}} \delta (| \mathbf {p} | - | \mathbf {q} |) = \frac {| \mathcal {M} | ^ {2}}{3 2 \pi m _ {e} | \mathbf {p} _ {\nu} | ^ {2}}, \tag {2.16}
$$

with  $|\mathbf{p}|^2 = 2m_e T_r$ . For easy comparison, we have kept the momentum transfer integration which can be removed by the  $\delta(|\mathbf{p}| - |\mathbf{q}|)$  function. Comparing (2.16) with (2.13), we can see that the  $K$ -factor reduces to  $|\mathbf{q}|\delta(|\mathbf{p}| - |\mathbf{q}|)/2$  in the free electron scattering limit. For the scattering with a free electron, the two-body phase space reduces to a single integration over either the recoil energy  $T_r$  or equivalently the momentum transfer  $|\mathbf{q}|$ . But for the bound electron case, the phase space has double integration, over  $T_r$  and  $|\mathbf{q}|$  which are no longer correlated. This is because the initial bound electron does not have definite momentum but a distribution. Consequently, the contribution from different momentum transfer should be integrated. Besides  $\overline{\left|\mathcal{M}\right|^2}/32\pi m_e^2 |\mathbf{p}_\nu|^2 T_r$ , the phase space integrations are  $m_e T_r$  and  $\int |\mathbf{q}| K_{nl}(T_r, |\mathbf{q}|) d|\mathbf{q}|$  for the free and bound electron cases, respectively. Assuming constant  $|\mathcal{M}|^2$ , the atomic enhancement can be roughly measured by the ratio between the phase space integrations,  $\int |\mathbf{q}| K_{nl}(T_r, |\mathbf{q}|) d|\mathbf{q}|/m_e T_r$ .

The left panel of figure 1 shows the atomic factor  $|\mathbf{q}|K_{nl}(T_r,|\mathbf{q}|)$  (dashed) and the atomic factor ratio  $|\mathbf{q}|K_{nl}(T_r,|\mathbf{q}|)/m_e T_r$  (solid) as functions of the momentum transfer  $|\mathbf{q}|$ . The curves are narrower for outer shell electrons (larger  $n$ ) and the typical width keeps growing when  $n$  becomes smaller. The half width at the half height  $\sigma_{|\mathbf{q}|} = (50,20,10,4)$  keV for the  $(2p,3p,4p,5p)$  electron can be directly read off from the solid lines. The solid and dashed lines share the same width since the only difference between them is a constant factor. For given electron shell, the width is independent of  $T_r$ . The width is exactly a manifestation of the electron motion inside atom. Pointing in all directions, the initial electron momentum smears the momentum transfer  $|\mathbf{q}|$  and hence the recoil energy  $T_r$ . The larger initial momentum, the larger smearing effect. With binding energy  $|E_b| = (4.53,0.95,0.16,0.012)$  keV for  $(2p,3p,4p,5p)$  orbitals [71], the initial electron momentum can be estimated by non-relativistic dispersion relation,  $|\mathbf{p}_i| \approx \sqrt{2m_e|E_b|} = (68,31,13,3.5)$  keV correspondingly. These numbers roughly match the width read off from the curves. Although the bound electron motion broadens the curves, the central values are largely unaffected, especially for the outer shells. The peak position can be estimated by the momentum transfer  $|\mathbf{q}^{\mathrm{peak}}| \approx \sqrt{2m_e T_r}$  of the free electron scattering. For the three curves of  $T_r = (5,10,20)$  keV, the estimated peak positions are  $|\mathbf{q}^{\mathrm{peak}}| \approx (71,101,143)$  keV

![](images/2b513b4f96e7475f8d12d10a267fa48d957b2a5f66a601614dfafbd03105e703.jpg)  
Figure 1. The left panel shows  $|\mathbf{q}|K_{nl}(T_r,|\mathbf{q}|)$  (dashed) and the phase space ratio  $|\mathbf{q}|K_{nl}(T_r,|\mathbf{q}|)/m_e T_r$  (solid) for the  $2p, 3p, 4p$  and  $5p$  orbitals from top to bottom. Three typical recoil energies  $T_r = 5\mathrm{keV}$  (black),  $10\mathrm{keV}$  (blue), and  $20\mathrm{keV}$  (green) are shown for illustration. The peak locations,  $|\mathbf{q}| = \sqrt{2m_e T_r}$ , estimated from the scattering with a free electron are shown as vertical gray lines. As a function of the electron recoil energy  $T_r$ , the right panel shows the phase space ratio  $\int |\mathbf{q}|K_{nl}(T_r,|\mathbf{q}|)d|\mathbf{q}|/m_e T_r$  for the  $2p$  (black solid),  $3p$  (red dashed),  $4p$  (blue dotted) and  $5p$  (green dash-dotted) orbitals in the Xe atom with solar neutrino energy  $E_\nu = 300\mathrm{keV}$  and the sterile neutrino mass  $m_s = 100\mathrm{keV}$ .

![](images/4d6eb602526df3c7f9b0f10f9fa226cfab6b32ca0243ee4a38fb1a74fd3a8029.jpg)

as indicated by three vertical grey lines from left to right. With larger  $n$ , the peak position becomes closer to the free electron momentum transfer.

The right panel of figure 1 shows the integrated phase space ratio as functions of the recoil energy  $T_{r}$ . The ratio starts from a relatively small value for vanishing  $T_{r}$  and converges to 1 with increasing  $T_{r}$ . This happens because for small  $T_{r}$  the allowed momentum transfer is suppressed to have smaller phase space [66]. In contrast, the electron approaches a free particle to have larger phase space with increasing  $T_{r}$ . For larger  $n$ , the integrated phase space ratio approaches 1 faster, since the electron is less tightly confined to the atom.

The left panel of figure 2 shows the non-zero terms inside the double summation of (2.15) as a function of the angular indices  $(l', L)$  for the  $2p$ ,  $3p$ ,  $4p$ , and  $5p$  orbitals. Those terms violating  $|l' \pm L| = l$  are zero and omitted in the plot for simplicity. With increasing  $n$ , the peak shifts to the right. The  $2p$  curve peaks around  $l' = 5$  and drops to zero at  $l' = 15$ . For comparison, the  $5p$  curve peaks around  $l' = 95$  and is non-zero even for  $l' > 190$ . The exact evaluation of the  $K_{nl}$  factor in (2.15) requires double summation over the principal quantum numbers,  $l'$  and  $L$ , to infinity which is highly time-consuming. To increase efficiency, we cut the summation at large enough  $l_{\mathrm{max}}'$  and  $L_{\mathrm{max}}$  to guarantee precision.

The relative precision can be estimated from the right panel of figure 2. Each curve shows the ratio between the partial sum up to  $(l_{\max}^{\prime}, L_{\max})$  divided by the one up to (200, 201) for the  $2p, 3p, 4p,$  and  $5p$  orbitals. With increasing  $(l_{\max}^{\prime}, L_{\max})$ , the ratio converges to 1. As  $n$  increases, larger  $l_{\max}^{\prime}$  and  $L_{\max}$  are needed. For the  $2p, 3p, 4p,$  and  $5p$  orbitals to achieve sub-percentage precision,  $(l_{\max}^{\prime}, L_{\max})$  needs to be at least (10, 11), (30, 31), (70, 71), and (190, 191), respectively.

The integrand in (2.15) is highly oscillatory and illustrated in figure 3. The top panels show purely the initial bound electron wave functions as a convenient combination

![](images/b54f89561bd99c0e9c4fa9bc12d731eaa9edc2ea6422c80dc47369c4a5aeab42.jpg)  
Figure 2. The left panel shows the non-zero terms of the double summation in (2.15) as a function of  $l^{\prime}, L$ . The right panel shows the fraction between the partial sum for a given set of  $l_{\mathrm{max}}^{\prime}, L_{\mathrm{max}}$  and the total sum with  $l_{\mathrm{max}}^{\prime} = 200$ ,  $L_{\mathrm{max}} = 201$ . In both cases,  $T_r = 30 \mathrm{keV}$  and  $|\mathbf{q}| = \sqrt{2m_e T_r}$ . The lines represent the 2p (black), 3p (red), 4p (blue) and 5p (green) orbitals in the Xe atom.

![](images/d78bdf75581f2f18b4c74d89891d5a7b8f90259b8a9878e60089122ba117ae81.jpg)

$r^2 |R_{nl}|^2$  (black solid) that should appear in normalization integration. While the initial wave functions are quite regular with only one major peak, the final ionized electron wave functions oscillate a lot. This oscillatory behavior clearly appears in the product combination  $r^2 R_{nl}^* R_{Trl'}$  (blue solid). Since the bound and ionized states are orthogonal to each other, the product oscillates symmetrically around the vanishing value so that the integration should also vanish. The third component, the Bessel function  $j_L(|\mathbf{q}|r)$ , enters the atomic form factor to render a nonzero  $K$ -factor (2.15). The full combination  $r^2 R_{nl}^* R_{Trl'}j_L(|\mathbf{q}|r)$  (red dashed) has asymmetric oscillation so that its integration can be nonzero. With larger  $n$ ,  $l$ , and  $T_r$ , the oscillation becomes more frequent. To accurately perform the integration in (2.15), a large number of grid points over  $r$  is necessary. A sub-percentage precision requires 3000 grid points in the range  $r \in [0,10a_0]$  where  $a_0 \equiv 1 / m_e\alpha$  is the Bohr radius.

# 3 Neutrino scattering into a massive sterile neutrino with light mediators

With the second quantization formalism for the atomic effect established in the previous section, we can proceed to calculate the recoil spectrum (2.13) by implementing the concrete scattering matrix element  $|\overline{\mathcal{M}}|^2$  as input from the particle physics side. For the solar neutrino scattering into a massive sterile neutrino in the final state, we first derive the differential cross section in section 3.1 and then show the modification due to atomic effects in section 3.2.

# 3.1 Neutrino scattering with free or bound electrons

The XENON1T excess in the low energy region can be explained by the solar neutrino scattering with electron via a scalar or pseudo-scalar mediator [64].

$$
\mathcal {L} _ {\text {i n t}} \equiv \bar {\nu} \left(y _ {S} ^ {\nu} + \gamma_ {5} y _ {P} ^ {\nu}\right) \phi \nu_ {s} + \bar {e} \left(y _ {S} ^ {e} + \gamma_ {5} y _ {P} ^ {e}\right) e \phi + h. c. \tag {3.1}
$$

![](images/4476af70578617e4e2575cf75597da8a55a1aa5da795f28a48ecca55fa24c941.jpg)  
Figure 3. The oscillatory behavior in the bound and ionized electron wave functions. Each column stands for an individual initial electron level,  $(nl) = 2p$ ,  $3p$ ,  $4p$ , and  $5p$ . The first row is purely for the initial electron radial wave function  $r^2 |R_{nl}|^2$  which appears in the integration for normalization. The next three rows are for the convolution between the initial and final electron radial functions  $r^2 R_{nl}^* R_{Trl'}$  (blue solid) and  $r^2 R_{nl}^* R_{Trl'}j_L(|\mathbf{q}|r)$  with  $L = 0$  (red dashed) for electron recoil energies  $T_r = (5,10,20)\mathrm{keV}$ . For illustration, we take the peak value  $|\mathbf{q}| = \sqrt{2m_e T_r}$  of the momentum transfer. The horizontal axes are in the unit of Bohr radius  $a_0 = 1 / m_e\alpha$ .

In addition to the recoil electron, a massive sterile neutrino appears in the final state. For the scattering with a free electron, the cross section is a function of the recoil energy  $T_{r}$ ,

$$
\text {S c a l a r}: \quad \frac {d \sigma_ {S} ^ {0}}{d T _ {r}} = \frac {\left(y _ {S} ^ {\nu} y _ {S} ^ {e}\right) ^ {2} \left(2 m _ {e} + T _ {r}\right)}{8 \pi E _ {\nu} ^ {2}} \frac {2 m _ {e} T _ {r} + m _ {s} ^ {2}}{\left(2 m _ {e} T _ {r} + m _ {\phi} ^ {2}\right) ^ {2}}, \tag {3.2a}
$$

$$
\text {P s e u d o - S c a l a r :} \quad \frac {d \sigma_ {P} ^ {0}}{d T _ {r}} = \frac {\left(y _ {P} ^ {\nu} y _ {P} ^ {e}\right) ^ {2} T _ {r}}{8 \pi E _ {\nu} ^ {2}} \frac {2 m _ {e} T _ {r} + m _ {s} ^ {2}}{\left(2 m _ {e} T _ {r} + m _ {\phi} ^ {2}\right) ^ {2}}, \tag {3.2b}
$$

In addition to the neutrino energy  $E_{\nu}$ ,  $m_{s}$  and  $m_{\phi}$  are the sterile neutrino and scalar/pseudoscalar mediator masses, respectively. Contrary to the common expectations [56] with massless neutrinos, a massive sterile and a light mediator ( $m_{\phi}^{2} \ll 2m_{e}T_{r} \ll m_{s}^{2}$ ) can introduce  $1 / T_{r}$  enhancement even for the pseudo-scalar mediator [64] by a factor of  $m_{s}^{2} / 2m_{e}T_{r}$ . For a low energy electron recoil signal, such as the XENON1T excess at  $T_{r} \approx (2 \sim 3) \mathrm{keV}$ , the mediator mass should satisfy an upper bound  $m_{\phi} \ll (45 \sim 55) \mathrm{keV}$  to receive enhancement.

For the scattering with a bound electron, the electron part resembles the free case for the scalar-type vertex and receives a momentum insertion for the pseudo-scalar one as

shown in (2.11),

$$
\overline {{| \mathcal {M} _ {S} | ^ {2}}} = \frac {(y _ {S} ^ {\nu} y _ {S} ^ {e}) ^ {2}}{2 (q ^ {2} - m _ {\phi} ^ {2}) ^ {2}} \mathrm {T r} \left[ \not p _ {\nu} (\not p _ {\nu_ {s}} + m _ {s}) \right] \mathrm {T r} \left[ (\not p _ {e} + m _ {e}) (\not p _ {e} ^ {\prime} + m _ {e}) \right], \tag {3.3a}
$$

$$
\overline {{| \mathcal {M} _ {P} | ^ {2}}} = \frac {(y _ {P} ^ {\nu} y _ {P} ^ {e}) ^ {2}}{2 (q ^ {2} - m _ {\phi} ^ {2}) ^ {2}} \frac {1}{4 m _ {e} ^ {2}} \mathrm {T r} \left[ \not p _ {\nu} \gamma_ {5} (\not p _ {\nu_ {s}} + m _ {s}) \gamma_ {5} \right] \mathrm {T r} \left[ (\not p _ {e} + m _ {e}) (\mathbf {q} \cdot \pmb {\gamma}) \gamma_ {5} (\not p _ {e} ^ {\prime} + m _ {e}) (\mathbf {q} \cdot \pmb {\gamma}) \gamma_ {5} \right]. (3. 3 \mathrm {b})
$$

When calculating the trace, we should remember that the spinor for electron  $u(m_e)$  is the one without momentum. But it does not mean this approximation has no information of the electron momentum. Actually, the electron momentum appears as the gradient operator in (2.4), which when acting on the integration will generate the momentum transfer  $\mathbf{q}$ . This is also the origin of  $\mathbf{q} \cdot \boldsymbol{\gamma}$  in the pseudo-scalar matrix element. Putting the scalar and pseudo-scalar cases together, the spin-averaged matrix element is,

$$
\overline {{| \mathcal {M} _ {S , P} | ^ {2}}} = 2 \left(4 m _ {e} ^ {2} | y _ {S} ^ {\nu} y _ {S} ^ {e} | ^ {2} + | \mathbf {q} | ^ {2} | y _ {P} ^ {\nu} y _ {P} ^ {e} | ^ {2}\right) \frac {| \mathbf {q} | ^ {2} + m _ {s} ^ {2} - \Delta E _ {n l} ^ {2}}{(| \mathbf {q} | ^ {2} + m _ {\phi} ^ {2} - \Delta E _ {n l} ^ {2}) ^ {2}}. (3. 4)
$$

Although derived for the bound electron case, (3.4) can reproduce the leading terms of the free electron case (3.2) with the following replacements. The initial electron is at rest and the energy difference is exactly the recoil kinetic energy,  $\Delta E_{nl} = T_r$ , of the final electron. In addition, the momentum transfer magnitude  $|\mathbf{q}|$  is uniquely related to the recoil energy,  $|\mathbf{q}|^2 = T_r^2 + 2m_e T_r$ , due to the on-shell condition of the final-state electron.

On the other hand, a bound electron in the initial state has no definite momentum. There is no way to use the on-shell condition for the final-state ionized electron to correlate the energy change  $\Delta E_{nl} \equiv T_r - E_{nl}$  and the momentum transfer magnitude  $|\mathbf{q}|$ . The differential cross section (2.13) is then an integration over all the possible momentum transfers,

$$
\operatorname {S c a l a r}: \quad \frac {d \sigma_ {S} ^ {n l}}{d T _ {r}} = \frac {\left(y _ {S} ^ {\nu} y _ {S} ^ {e}\right) ^ {2}}{4 \pi E _ {\nu} ^ {2} T _ {r}} \int | \mathbf {q} | d | \mathbf {q} | \frac {| \mathbf {q} | ^ {2} + m _ {s} ^ {2} - \Delta E _ {n l} ^ {2}}{\left(| \mathbf {q} | ^ {2} + m _ {\phi} ^ {2} - \Delta E _ {n l} ^ {2}\right) ^ {2}} K _ {n l} \left(T _ {r}, | \mathbf {q} |\right), \tag {3.5a}
$$

$$
\mathrm {P s e u d o - S c a l a r :} \quad \frac {d \sigma_ {P} ^ {n l}}{d T _ {r}} = \frac {(y _ {P} ^ {\nu} y _ {P} ^ {e}) ^ {2}}{4 \pi E _ {\nu} ^ {2} T _ {r}} \int | \mathbf {q} | d | \mathbf {q} | \frac {| \mathbf {q} | ^ {2}}{4 m _ {e} ^ {2}} \frac {| \mathbf {q} | ^ {2} + m _ {s} ^ {2} - \Delta E _ {n l} ^ {2}}{(| \mathbf {q} | ^ {2} + m _ {\phi} ^ {2} - \Delta E _ {n l} ^ {2}) ^ {2}} K _ {n l} (T _ {r}, | \mathbf {q} |). \quad (3. 5 \mathrm {b})
$$

The similar scenario with a light vector boson mediator can also explain the XENON1T excess [64]. For simplicity, we consider only the situation where  $Z'$  couples to the left-handed neutrino,

$$
\mathcal {L} _ {\text {i n t}} \equiv g _ {L} ^ {\nu} \bar {\nu} \gamma^ {\mu} P _ {L} \nu_ {s} Z _ {\mu} ^ {\prime} + \bar {e} \left(g _ {V} ^ {e} - g _ {A} ^ {e} \gamma_ {5}\right) \gamma^ {\mu} e Z _ {\mu} ^ {\prime}, \tag {3.6}
$$

while the electron coupling can have either vector  $(g_V^e)$  or axial-vector  $(g_A^e)$  current coupling with  $Z'$ . The differential cross section of neutrino scattering with a free electron is,

$$
\frac {d \sigma_ {V , A} ^ {0}}{d T _ {r}} = \frac {\left(g _ {L} ^ {\nu} g _ {V , A} ^ {e}\right) ^ {2}}{4 \pi E _ {\nu} ^ {2}} \frac {4 m _ {e} E _ {\nu} ^ {2} - (2 m _ {e} T _ {r} + m _ {s} ^ {2}) (2 E _ {\nu} \pm m _ {e} - T _ {r})}{\left(2 m _ {e} T _ {r} + m _ {Z ^ {\prime}} ^ {2}\right) ^ {2}}, \tag {3.7}
$$

![](images/246123846df1088524a359e2baaf0c7b9db40751a98e2da2c672698290979762.jpg)  
Figure 4. The differential cross section of  $\nu -e$  scattering with a massive sterile neutrino in the final state and light scalar (left) or pseudo-scalar (right) mediator. The black line is for the scattering with a free electron while the colorful lines are for the bound electrons  $2p$  (solid cyan),  $3p$  (solid yellow),  $4s$  (dashed blue),  $4p$  (solid blue),  $4d$  (dotted blue), and  $5p$  (solid green) of a Xenon atom. In both subplots, the final-state sterile neutrino mass is  $m_{s} = 150\mathrm{keV}$  and the mediator mass is  $m_{\phi} = 20\mathrm{keV}$ .

![](images/849d5d544fc91d6090988a4c7a5d09eb236b05a10e7a38fabc18aa2d2eb41da0.jpg)

where the  $+(-)$  signs are for the vector and axial-vector interactions, respectively. The sterile neutrino mass term  $m_{s}^{2}$  and hence the second term in the numerator can be important only when  $m_{s}$  becomes comparable with the electron mass  $m_{e}$  and the neutrino energy  $E_{\nu}$ . In this paper, we focus on the mass region  $m_{s} \sim \mathcal{O}(100) \mathrm{keV}$ . Then with  $4m_{e}E_{\nu}^{2}$  dominating the numerator, a  $1 / T_{r}^{2}$  enhancement is possible for a light enough mediator,  $m_{Z^{\prime}}^{2} \ll 2m_{e}T_{r}$ . For comparison, the differential cross section of neutrino scattering with a bound electron is,

$$
\frac {d \sigma_ {V , A} ^ {n l}}{d T _ {r}} = \frac {(g _ {L} ^ {\nu} g _ {V , A} ^ {e}) ^ {2}}{4 \pi E _ {\nu} ^ {2} T _ {r}} \int | \pmb {q} | d | \pmb {q} | \frac {4 E _ {\nu} (E _ {\nu} - \Delta E _ {n l}) \mp (| \pmb {q} | ^ {2} + m _ {s} ^ {2} - \Delta E _ {n l} ^ {2})}{(| \pmb {q} | ^ {2} + m _ {Z ^ {\prime}} ^ {2} - \Delta E _ {n l} ^ {2}) ^ {2}} K _ {n l} (T _ {r}, | \mathbf {q} |), \qquad (3. 8)
$$

with  $\mp$  for the vector and axial-vector couplings, respectively.

# 3.2 The cross section enhancement from atomic effects

By implementing the  $K$ -factor elaborated in section 2.2, we obtain the differential cross sections (3.5) and (3.8) for scalar and vector mediators. To see the features clearly, we first evaluate  $d\sigma^{nl} / dT_r$  for the transition of a single initial electron in a given  $nl$  bound state to the ionized electron with recoil energy  $T_r$ , shown as colorful lines in figure 4. For comparison, we also show the free electron case as black solid line. We take the scalar and pseudo-scalar mediators to illustrate the physics picture while the vector case is similar.

The difference is quite significant. Especially, the smearing effect makes the sharp peak much fatter and lower mainly due to the electron motion in the atom. For smaller principal quantum number  $n$ , the reduction is much stronger. One reason is the phase space ratio due to the atomic  $K$ -factor as shown in figure 1. Another factor comes from the scattering matrix element. The electron in the atomic Coulomb potential has a negative binding energy  $E_{b}$  which is exactly  $E_{nl}$ . Intuitively, It is more difficult for an electron with larger binding energy to be recoiled off. If the energy change  $\Delta E_{nl} = T_r - E_{nl}$  in (3.4) dominates, especially for the inner shells, the scattering matrix element can be greatly suppressed.

This is because the momentum transfer peaks at  $|\mathbf{q}| = \sqrt{2m_e T_r}$  with large spread above the peak position as shown in figure 1. So the modification of the differential cross section is a combined result of the  $K$ -factor phase space integration reduction and the scattering matrix element suppression. On the other hand, the electron in outer shells is loosely trapped with marginal suppression and is very similar to the free case.

In addition, the smearing effect extends the spectrum beyond the cut-off. For free electron scattering, the recoil energy is bounded from below,  $T_{r} \geq T_{r}^{-}$  as defined in our earlier paper [64]. A nonzero lower limit  $T_{r}^{-} \approx m_{s}^{4} / 8m_{e}E_{\nu}^{2}$  arises when expanding the sterile neutrino mass to the fourth power. For the  $E_{\nu} = 300\mathrm{keV}$  used to plot the black solid line, the differential cross section vanishes around  $1.7\mathrm{keV}$ . However, bound electrons have distributed momentum in all directions and hence can smear the momentum transfer to extend the recoil energy  $T_{r}$  even down to  $0\mathrm{keV}$ . Furthermore, the  $2p$  or  $3p$  electrons even have a non-zero differential cross section at vanishing  $T_{r}$ . As shown in (2.13), the phase space integration is  $|\mathbf{q}|d|\mathbf{q}|$ . Since the lower limit  $E_{\nu} - \sqrt{(E_{\nu} - \Delta E_{nl})^2 - m_s^2}$  of  $|\mathbf{q}|$  with  $\Delta E_{nl} > 0$  is always nonzero for the scattering of bound electron into an ionized one, the phase space would not disappear even for  $T_{r} = 0\mathrm{keV}$ . This behavior can also explain the sudden drop of the  $5p$  curve when approaching vanishing  $T_{r}$  in figure 1.

Solar neutrino can scatter with electrons of different quantum numbers inside the Xenon atom. For the free electron scattering, the total  $d\sigma / dT_{r}$  is simply  $N_{e} = 54$  times of the differential cross section for a single electron where  $N_{e}$  is the electron number in the Xenon atom. The total cross section for the bound electron scattering is a sum over all the differential cross sections  $d\sigma^{nl} / dT_{r}$ ,

$$
\text {F r e e}: \frac {d \sigma}{d T _ {r}} = 5 4 \times \frac {d \sigma^ {0}}{d T _ {r}}, \quad \text {v s} \quad \text {B o u n d}: \frac {d \sigma_ {A}}{d T _ {r}} = \sum_ {n l} 2 (2 l + 1) \frac {d \sigma^ {n l}}{d T _ {r}}. \tag {3.9}
$$

Of the weight  $2(2l + 1)$ , the factor 2 for the bound case accounts for the two electron spin degrees of freedom with the same  $nlm$  quantum numbers. Note that the summation over the magnetic quantum number  $m$  results in the  $2l + 1$  factor. As illustrated by the blue lines in figure 4, the  $4s$ ,  $4p$ , and  $4d$  curves with the same principal quantum number  $n = 4$  but different angular quantum numbers have similar shapes and amplitudes. More generally, orbitals with the same principal quantum number have roughly the same differential cross sections. The  $n = 5$  orbitals have higher and sharper peaks than the  $n = 4$  ones. However, the electron number of the former,  $2(5s) + 6(5p) = 8$ , is less than half of the later,  $2(4s) + 6(4p) + 10(4d) = 18$ . So the total differential cross section of atomic scattering (thick dashed and solid) in figure 5 is mainly contributed by the  $4s$ ,  $4p$ , and  $4d$  curves (blue) in figure 4. Since the differential cross section  $d\sigma^{nl} / dT_r$  for a single electron is reduced for all  $nl$  quantum numbers, the total result  $d\sigma_A / dT_r$  is also reduced from the free electron case. As shown in the lower panel, the reduction is roughly a factor of 0.5 in the low-energy region ( $T_r \lesssim 5\mathrm{keV}$ ) and gradually recovers to 1 in the high energy region ( $T_r \gtrsim 10\mathrm{keV}$ ) for the scalar or pseudo-scalar mediators. For vector and axial-vector interactions, atomic effects bring the same features.

A key difference between the scalar/pseudo-scalar and vector/axial-vector interactions is that the latter has much larger cross section by almost a factor of  $10 \sim 15$ , as shown

![](images/bf654a97ae9f7f29bc0933008383e5f37ec6fb1b4d332f68f4047c75006a3543.jpg)  
Figure 5. The differential cross section of neutrino scattering with all electrons of Xe atom into a massive sterile neutrino. The left panel shows the case with scalar (red) and pseudo-scalar (blue) mediators. For comparison, we also show the vector mediator case in the right panel with vector (red) and axial vector (blue) couplings. Both panels show the results with free (dotted), bound (dashed), and the shifted one including recombination energies (solid). The enhancement from the free electron scattering cross section is shown as ratio  $R$  in the lower panels for comparison. Since the couplings only appear as overall factor, we adopt  $|y^{\nu}y^{e}| = |g^{\nu}g^{e}| = 1$  for simplicity.

![](images/31ab75509e69f1bffc35895d4c41ff2d3e2410ececd1d1b8d00446928b1043c8.jpg)

in the upper panels of figure 5. As discussed below (3.7), the matrix element part is approximately  $4m_{e}E_{\nu}^{2} / (2m_{e}T_{r} + m_{Z^{\prime}}^{2})^{2}$  for the free electron scattering with vector mediator. For comparison, the scalar case has  $m_{e}(2m_{e}T_{r} + m_{s}^{2}) / (2m_{e}T_{r} + m_{\phi}^{2})^{2}$ . With tiny mediator mass,  $m_{\phi}^{2}, m_{Z^{\prime}}^{2} \ll 2m_{e}T_{r}$ , the difference mainly comes from the numerator part. The ratio between vector and scalar matrix elements is  $4m_{e}E_{\nu}^{2} / m_{e}(2m_{e}T_{r} + m_{s}^{2})$ . We can see that the vector case has a major contribution  $4m_{e}E_{\nu}^{2}$ . With  $E_{\nu} \approx 300\mathrm{keV}$ ,  $m_{s} \approx 150\mathrm{keV}$ , and  $|\mathbf{q}|^2 \sim 2m_{e}T_{r} \approx 3000\mathrm{keV}$ , the vector cross section is naturally enhanced by a factor around 10.

In addition to the free (dotted) and bound (dashed) electron curves, figure 5 also shows the shifted results. This is because the energy deposit  $\Delta E_{nl}$  is not just the electron recoil energy  $T_{r}$  but also the binding energy  $E_{b} = E_{nl}$ . The later is released when an ambient electron is attracted by the positively charged Xenon atom to fill the hole left by the ionized electron [84]. The differential cross section is then shifted to the right as the solid lines. The binding energy is typically  $\mathcal{O}(0.01)\mathrm{keV}$  for outer shells [84] and can be ignored in comparison to the recoil energy. But the binding energy can be as large as  $\mathcal{O}(10)\mathrm{keV}$  for most inner shells and hence seems able to induce significant horizontal shift, the differential cross section  $d\sigma^{nl} / dT_r$  is suppressed by the same large binding energy in the first place as discussed above. So the energy shift does not affect the total differential cross section  $d\sigma /dE_{\mathrm{vis}}$  much as shown in the plot.

# 4 Experimental constraints

The XENON1T Collaboration has recently observed an excess in the electron recoil spectrum around  $(2\sim 3)\mathrm{keV}$  [2]. The experimental data is shown as black points in figure 6 while

![](images/a9d99baaf1b5c51dea77b7f8179ba84a0c314f9890bbe477f3d4f2b0cb90c92e.jpg)  
Figure 6. Total events (black points) and background (red curve) of XENON1T's data, we fit the data by solar neutrino-bound electron scattering with a sterile neutrino in final state, in addition to both scalar (green) and pseudo scalar(blue) mediators. All three parameters  $m_{s}, m_{\phi}, |y_{e}y_{p}|$  are using the best-fitting values.

![](images/22a68a57725a8d7357214d7f48e143bea6d2b6cfb31fc3c0d5ceea4da2772053.jpg)

the total background from radioactive materials present in the detector and solar neutrino scattering is shown as the red curve for comparison. Note that the background is roughly flat and hence can not explain the excess at low energy. It is possible for this excess to arise from some new physics and the data points can be used to constrain the possible new physics model parameters.

In this paper, we give a more detailed evaluation of the constraint on the solar neutrino scattering with electrons into a massive sterile neutrino [64]. The atomic effects are also included to give a realistic result. We use the following  $\chi^2$  function,

$$
\chi^ {2} \equiv \sum_ {i} ^ {\mathrm {b i n s}} \left(\frac {N _ {i} ^ {\mathrm {d a t a}} - (1 + c) N _ {i} ^ {\mathrm {b k g}} - N _ {i} ^ {\mathrm {N P}}}{\sqrt {N _ {i} ^ {\mathrm {d a t a}}}}\right) ^ {2} + \left(\frac {c}{\sigma_ {c}}\right) ^ {2}, \tag {4.1}
$$

to evaluate the best-fit value and sensitivities. The  $\chi^2$  function contains two major contributions: the first term from the data bins and the second is nuisance parameter  $c$  for the background normalization with uncertainty  $\sigma_c = 2.6\%$  [2]. In each bin,  $N_i^{\mathrm{data}}$  is the data point,  $N_i^{\mathrm{bg}}$  the expected background, and  $N_i^{\mathrm{NP}}$  the expected events due to new physics (NP) contribution. For the light mediator case considered in this paper,  $N_i^{\mathrm{NP}}$  is a function of the mediator mass ( $m_{\phi}$  or  $m_{Z'}$ ), the sterile neutrino mass ( $m_s$ ), and couplings ( $|y_{S,P}^\nu y_{S,P}^e|$  or  $|g_{V,A}^\nu g_{V,A}^e|$ ).

On the theoretical side, the event rates are calculated by the convolution of the differential cross-section defined in (3.9) and the solar neutrino flux. We use the  $pp$ -neutrinos since they have the largest flux at low energy [85]. The detector's energy resolution is also taken into account by a Gaussian parametrization with variance given by  $\sigma_{T_r} = a / \sqrt{T_r / \mathrm{keV}} + b$  with  $a = 31.71 \pm 0.65\mathrm{keV}$  and  $b = 0.15 \pm 0.02\mathrm{keV}$  [86]. In addition, the detector efficiency at a given recoil energy  $T_{r}$  is extracted from [2]. Figure 7 shows the best-fit values and exclusion curves obtain by fitting the predicted event numbers  $N_{i}^{\mathrm{NP}}$  with data using (4.1). The left and right panels are obtained by fixing two parameters,  $|y_{S,P}^{\nu}y_{S,P}^{e}|$  and  $m_{\phi}(m_s)$ , and minimizing the  $\chi^2$  function over the remaining  $m_{s}$  ( $m_{\phi}$ ).

![](images/7b02cfc73189a13351de644188b129926d5427d550bcaef89b5800944a2fc0cc.jpg)

![](images/b4b9c32a8cfa73038a3fdf0aa540d3bf57365047b4d95738279838cd976a3000.jpg)

![](images/4848b02074363a77c78c0b36dcad93f39eda2a2f50bccbc9ca3f85ae2fcf4a6e.jpg)  
Figure 7. The XENON1T constraints for scalar (up), pseudo-scalar (bottom) interaction couplings  $|y_{S,P}^{\nu}y_{S,P}^{e}|$  versus  $m_{s}$  (left) and  $m_{\phi}$  (right) at  $1\sigma, 2\sigma,$  and  $3\sigma$  C.L. The black curves are for the free electron approximation and red ones for the bound electron scenario whose best-fit points are indicated with black (free) and red (bound) stars, respectively. The mediator (sterile neutrino) mass  $m_{\phi}(m_s)$  is marginalized over  $0\mathrm{keV} < m_{\phi} < 175\mathrm{keV}$  ( $0\mathrm{keV} < m_s < 250\mathrm{keV}$ ).

![](images/d0481d33b499555d6581c5d089195f57d12856e9c0c693d37a32da501003f18d.jpg)

For comparison, each panel shows both free (black curves) and bound (red areas) electron scenarios. The bound-to-free ratio  $R = 0.5$  for the scalar mediator in figure 5 seems be quite different from 1 and can have significant consequence. However, it is mainly due to the broadening effect of the electron motion inside atom. With detector smearing effect, the sharp peak for the free scattering case would also become broader and lower to more closely resemble the bound case. Consequently, the coupling best-fit value almost does not change. Take the scalar interaction as an example, the coupling best fit marginally shifts from the free electron case  $\left( |y_S^e y_S^\nu | = 5.03 \times 10^{-13} \right)$  to the bound one,  $|y_S^e y_S^\nu | = 5.13 \times 10^{-13}$ . Similarly, the coupling strength changes from  $5.63 \times 10^{-12}$  to  $5.33 \times 10^{-13}$  for pseudo-scalar mediator. The background-only hypothesis  $\left( |y_{S,P}^{e}y_{S,P}^{\nu}| = 0 \right)$  is excluded by more than  $3\sigma$  C.L. for the scalar interaction but is still inside the  $2\sigma$  region for the pseudo-scalar case. This is because the pseudo-scalar interaction has a smooth total differential cross section (blue curves in the left panel of figure 5) and is not as different from the background as the scalar one.

In addition to the DM direct detection, the coupling with electron  $y_{S,P}^{e}$  also receives constraints from other experiments and astrophysical observations. The torsion balance experiments impose a constraint  $|y_{S,P}^{e}| < 10^{-23}$  at  $95\%$  C.L. for the mediator mass below  $4\times 10^{-6}\mathrm{eV}$  [87], which is 10 orders smaller than the current DM direct detection constraints of  $\mathcal{O}(10^{-13})$ . In other words, an ultra-light mediator cannot explain the XENON1T excess. The mediator mass up to  $\mathcal{O}(0.01)\mathrm{eV}$  is also excluded by the Red Giant (RG) and Horizontal Branch (HB) stellar cooling constraint  $|y_{S,P}^{e}| < 10^{-16}$  [88] at  $95\%$  C.L. that is 3 orders smaller than the DM direct detection ones. The Big Bang nucleosynthesis (BBN) constrains the mediator mass above  $10^{-2}\mathrm{eV}$ . The  $\phi$  production in the early Universe increases the relativistic degrees of freedom and accelerates the universe expansion. A faster expansion reduces the deuterium abundance. The  $\phi$  production can only be evaded if  $|y_{S,P}^{e}| < 5\times 10^{-10}$  at  $95\%$  C.L. or  $m_{\phi} > 1$  MeV [89]. For the coupling with neutrino, the meson decay experiments require  $|y_{S,P}^{\nu}| \lesssim 10^{-3}$  if  $m_{s} < m_{\pi}$  [90-93]. Altogether, the combined constraint is  $|y_{S,P}^{e}y_{S,P}^{\nu}| \lesssim 5\times 10^{-13}$  in the mass region  $m_{\phi} > 10^{-2}\mathrm{eV}$  (the gray lines in figure 7). The best-fit value of the scalar case is allowed while the pseudo-scalar one is in tension.

The best-fit value of sterile neutrino mass almost does not change for the scalar interaction, the best fit shifts slightly from  $m_{s} = 147.4 \mathrm{keV}$  to  $128.2 \mathrm{keV}$  after implementing atomic effects. For the pseudo-scalar interaction, the best fit remains almost the same at  $m_{s} = 102.6 \mathrm{keV}$ . In other words, the dependence on the sterile neutrino mass is not sensitive to the atomic effects. Similar feature also applies for the light mediator mass whose best-fit value is  $0 \mathrm{keV}$  in all situations. This is because the propagator contribute a factor  $\propto 1 / (|\mathbf{q}|^{2} - \Delta E_{nl}^{2} + m_{\phi}^{2})^{2}$  in the differential cross section which typically grows with decreasing  $m_{\phi}$  for given  $|\mathbf{q}|^{2}$ . In other words, a smaller mediator mass leads to a higher peak at lower recoil energy which is preferred by the XENON1T data. However, the light mediator mass cannot really be zero due to various constraints [87, 89]. To be on the safe side, we adopt  $m_{\phi} = 10 \mathrm{keV}$  which is still inside the  $1\sigma$  range when predicting the event rates in section 5. A mediator mass of  $10 \mathrm{keV}$  avoids the constraints mentioned before. This modification does not make big difference in the direct detection measurement. To be more concrete, the  $\chi^2$  only increases by 1 and 1.5 for the scalar and pseudo-scalar cases, respectively.

Figure 8 shows the results for vector and axial-vector interactions. We can see that the basic features are similar to the scalar and pseudo-scalar counterparts. The coupling  $|g_V^\nu g_V^e|$  changes from  $1.7 \times 10^{-13}$  to  $1.8 \times 10^{-13}$  for vector while  $|g_A^\nu g_A^e|$  changes from  $1.6 \times 10^{-13}$  to  $1.5 \times 10^{-13}$  for axial vector interactions. This change can also be understood by the combination of bound-to-free cross section ratio and the detector smearing effect in a similar way as the scalar/pseudo-scalar cases above. Both vector and axial-vector interactions can exclude the background-only hypothesis by more than  $3\sigma$ . The best-fit value of sterile neutrino mass is around  $150\mathrm{keV}$  and the mediator mass still prefers a tiny value. Similarly to the scalar and pseudo-scalar cases, we take  $m_{Z'} = 10\mathrm{keV}$  below when making projections for the future experiments.

The most stringent model-independent constraint on the coupling with electron,  $|g_{V,A}^{e}| < 5 \times 10^{-10}$ , also comes from BBN [59]. In the sterile neutrino mass region  $m_{s} < m_{\pi}$ , the leptonic pion decay imposes a bound  $|g_{V,A}^{\nu}| < 0.014$  on the coupling with neutrino [92, 94].

![](images/981c5ec6d65d9ea8ddfed32e26300e08197f03e77e1f4b9bda082548d6a4f6aa.jpg)

![](images/7aee21922ab66483239afd0738340e437befdd754bdf0524b1fba9c4e12882e8.jpg)

![](images/38c6017471c1d38b14bf4b75043da4c81c083bc90be9e75b4103eebe723effd9.jpg)  
Figure 8. The XENON1T constraints for vector (up), axial-vector (bottom) interaction couplings  $|g_{V,A}^{\nu}g_{V,A}^{e}|$  versus  $m_{s}$  (left) and  $m_{\phi}$  (right) at 1,2 and  $3\sigma$  C.L. The same as before, black curves are for free electron approximation and red ones for bound electron scenario. Their best-fit values are indicated with black (free) and red (bound) stars. The mediator (sterile neutrino) mass  $m_{Z'}$  ( $m_{s}$ ) is marginalized over  $0\mathrm{keV} < m_{Z'} < 175\mathrm{keV}$  ( $0\mathrm{keV} < m_{s} < 250\mathrm{keV}$ ).

![](images/4a5c88a5b5932cf17e0d2e9558ca404cb1b940d29c6ce5e6d45854c025cd7800.jpg)

The combined result is  $|g_{V,A}^{e} g_{V,A}^{\nu}| < 7 \times 10^{-12}$ . For both the vector and axial-vector interactions, the best-fit points are well below this constraint. Both cases can escape the constraints. In fact, the bound is one order of magnitude higher than the best-fit points and is not visible in figure 8.

# 5 Predictions for future DM experiments

Although the XENON1T excess can be explained by new physics, the significance is not large enough and there is still no definite conclusion for the DM-electron interaction [2]. Especially, the tritium background is also possible explanation [2, 3]. More data is necessary to obtain a conclusive result. In this section, we use the best-fit values from the current XENON1T data to make prediction for future experiments.

We focus on three major DM direct detection experiments with liquid Xenon target. First, the PandaX-4T experiment [95] that has already started running in 2021 is an upgrade of PandaX-II with a fiducial mass of  $2.8\mathrm{t}$  and a factor of 10 improvement in the sensitivity. Next is the XENONnT experiment [96] upgraded from XENON1T. XENONnT has a fiducial mass of  $4\mathrm{t}$  and can reduce its background by a factor of 6. Finally, the LUX-Zeplin

![](images/29773232447e1019feb52d6e44270171efb96a606da44b7357a2a8a01fc5b59e.jpg)  
Figure 9. Predictions for three future experiments, PandaX-4T (red), XENONnT (blue), and LZ (green). left plot is for scalar (solid) and pseudo-scalar (dashed) interactions while right plot for vector (solid) and axial-vector (dashed) interactions.

![](images/0aa8a30028d7e7e6cc47a340b5b4cd14b719c3787a760216cebe95da14c925c4.jpg)

(LZ) experiment is a combination of two existing experiments LUX [97] and Zeplin-III [98]. Its fiducial mass can reach 5.6 t and also has very low background. In addition, we make predictions with the same efficiency of PandaX-II [99] for PandaX-4T and XENON1T [2] for XENONnT while for LZ the figure 3 of [100] is used.

Figure 9 shows the predicted event rates with atomic effects for future experiments PandaX-4T (red), XENONnT (blue), and LZ (green). The left panel shows the results for scalar (solid) and pseudo-scalar (dashed) interactions while the right panel shows the vector (solid) and axial-vector (dashed) cases. In these predictions, the couplings and the sterile neutrino mass  $m_{s}$  are assigned the best-fit values with the XENON1T data. But the light mediator masses ( $m_{\phi}$  and  $m_{Z'}$ ) take a universal value of  $10\mathrm{keV}$ . With atomic effects, the event rates for scalar, vector and axial-vector interactions have a more conspicuous low energy excess around ( $2 \sim 3$ ) keV. The event rate for the pseudo-scalar interaction gradually increases towards low energy.

Figure 10 shows the expected sensitivity of the scalar, pseudo-scalar (left) and vector, axial-vector (right) couplings as function of the sterile neutrino mass  $m_{s}$ , for the three future DM experiments PandaX-4T, Lux-Zeplin, and XENONnT. Their nominal exposure are 5.6, 15.3, and 20 ton-years, respectively. The results represent a benchmark where the radioactivity background is reduced to a negligible level. Only the irreducible solar neutrino background is considered in the analysis. There is no new physics presenting in the pseudo data. For each  $m_{s}$ , we first fix  $m_{\phi}, m_{Z^{\prime}} = 10 \mathrm{keV}$  to obtain a  $\Delta \chi^{2}$  as function of the coupling constants. From this one-dimensional  $\Delta \chi^{2}$ , we obtain the 95% C.L. limit with  $\Delta \chi^{2} = 3.84$  on couplings as shown in figure 10.

The sensitivity varies among PandaX-4T, XENONnT, and Lux-Zeplin due to different exposure time of 2 years, 5 years, and 1000 days, respectively. All experiments can probe the best-fit values in figure 7 and figure 8. They can also improve the sensitivity by roughly one order of magnitude. For example, the best-fit value of pseudo-scalar interaction is  $5.6 \times 10^{-12}$  at XENON1T and the constraint becomes  $\mathcal{O}(10^{-13})$  in figure 10. With this improvement, the future DM experiments can confirm or falsify the pseudo-scalar explanation to the XENON1T excess.

![](images/464b1eb37d2e7492ad28a77f43e9b9b59b382565a52949118961aac4e1dc0f6a.jpg)  
Figure 10. The PandaX-4T (red), XENONnT (blue), and Lux Zeplin (green) projected  $95\%$  C.L. exclusion curves as a function of the sterile neutrino mass  $m_{s}$ . The left panel is for the scalar (solid) and pseudo-scalar (dashed) mediators while the right panel is for the vector (solid) and axial-vector (dashed) interactions. In all cases, the mediator mass is fixed at  $m_{\phi, Z'} = 10 \mathrm{keV}$ .

![](images/f923dc9abb7370f9927299eeb470b2e13349161b2595a38bd99a2f2d3b57800d.jpg)

# 6 Conclusions

The XENON1T electron recoil excess stimulated various explanations with new physics including solar neutrino scattering with light mediators. Although the atomic effects are commonly considered for those dark matter scenarios, they are omitted in the solar neutrino explanations. In the first part of this work, we establish a systematic second quantization formalism for both the initial-state bound and final-state ionized electrons. This approach introduces the atomic  $K$ -factor in a natural way with general interactions for both neutrino and dark matter scatterings. The  $K$ -factor calculation includes a summation over the final-state angular quantum number  $l'$  to infinity. In practice, one needs to truncate the summation at some maximum value  $l_{\mathrm{max}}'$  and this introduces some calculation error. A sub-percent precision in the atomic  $K$ -factor requires at least  $l_{\mathrm{max}}' = 200$  for the electron recoil energy of  $\mathcal{O}(10)$  keV.

This formalism is then applied to the solar neutrino scattering with bound electrons into a sterile neutrino through scalar, pseudo-scalar, vector, and axial-vector interactions. The atomic effects decrease the cross section by  $1 \sim 5$  times to modify the recoil energy spectrum. Besides, the electron momentum distribution inside atom smears the momentum transfer of scattering. Consequently, the differential cross sections become smoother and broader than the free case. We then use the bound electron scattering scenario to fit the XENON1T excess. The scalar, vector, and axial-vector interactions are preferred over the background-only hypothesis by more than  $3\sigma$  with best-fit coupling constants of  $\mathcal{O}(10^{-13})$ . Meanwhile, the pseudo-scalar case is favored over the background-only hypothesis by less than  $2\sigma$  with a coupling constant of  $\mathcal{O}(10^{-12})$ . In all cases, the best-fit value of sterile neutrino mass is around  $100\mathrm{keV}$ . Our results demonstrate for the first time that the atomic effects can not be ignored when using solar neutrino scattering to explain the XENON1T electron recoil excess.

Finally, we project the signal event rate and sensitivity at PandaX-4T, XENONnT, and LZ. These future experiments improve the sensitivity by roughly one order. The current

best-fit values and the  $1\sigma$  C.L. regions of the scalar, vector, and axial-vector mediators are marginally below the constraints from astrophysics and pion decay. For the pseudo-scalar case, most regions of the parameter space are in tension with the current constraint. With a factor of 10 improvement in sensitivity, the solar active-sterile neutrino conversion with bound electrons via light mediators as an explanation to the XENON1T excess can be tested.

# Acknowledgments

The authors would like to thank Yi-Fan Chen, Timon Emken, Xiao Xue, and Ning Zhou for useful discussions. This work is supported by the Double First Class start-up fund (WF220442604), the Shanghai Pujiang Program (20PJ1407800), National Natural Science Foundation of China (No. 12090064), and Chinese Academy of Sciences Center for Excellence in Particle Physics (CCEPP).

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] M. Schumann, Direct Detection of WIMP Dark Matter: Concepts and Status, J. Phys. G 46 (2019) 103003 [arXiv:1903.03026] [INSPIRE].  
[2] XENON collaboration, Excess electronic recoil events in XENON1T, Phys. Rev. D 102 (2020) 072004 [arXiv:2006.09721] [INSPIRE].  
[3] PANDAX-II collaboration, A Search for Solar Axions and Anomalous Neutrino Magnetic Moment with the Complete PandaX-II Data, Chin. Phys. Lett. 38 (2021) 011301 [Erratum ibid. 38 (2021) 109902] [arXiv:2008.06485] [INSPIRE].  
[4] J. Jeong, J.E. Kim and S. Youn, Electromagnetic properties of neutrinos from scattering on bound electrons in atom, Int. J. Mod. Phys. A 36 (2021) 2150182 [arXiv:2105.01842] [INSPIRE].  
[5] A.E. Robinson, XENON1T observes tritium, arXiv:2006.13278 [INSPIRE].  
[6] F. Takahashi, M. Yamada and W. Yin, XENON1T Excess from Anomaly-Free Axionlike Dark Matter and Its Implications for Stellar Cooling Anomaly, Phys. Rev. Lett. 125 (2020) 161801 [arXiv:2006.10035] [INSPIRE].  
[7] L. Di Luzio, M. Fedele, M. Giannotti, F. Mescia and E. Nardi, Solar axions cannot explain the XENON1T excess, Phys. Rev. Lett. 125 (2020) 131804 [arXiv:2006.12487] [INSPIRE].  
[8] C. Gao, J. Liu, L.-T. Wang, X.-P. Wang, W. Xue and Y.-M. Zhong, Reexamining the Solar Axion Explanation for the XENON1T Excess, Phys. Rev. Lett. 125 (2020) 131806 [arXiv:2006.14598] [INSPIRE].  
[9] J.B. Dent, B. Dutta, J.L. Newstead and A. Thompson, Inverse Primakoff Scattering as a Probe of Solar Axions at Liquid Xenon Direct Detection Experiments, Phys. Rev. Lett. 125 (2020) 131805 [arXiv:2006.15118] [INSPIRE].  
[10] C.A.J. O'Hare, A. Caputo, A.J. Millar and E. Vitagliano, Axion helioscopes as solar magnetometers, Phys. Rev. D 102 (2020) 043019 [arXiv:2006.10415] [INSPIRE].

[11] C. Dessert, J.W. Foster, Y. Kahn and B.R. Safdi, Systematics in the XENON1T data: The 15-keV anti-axion, Phys. Dark Univ. 34 (2021) 100878 [arXiv:2006.16220] [INSPIRE].  
[12] T. Li, The KSVZ Axion and Pseudo-Nambu-Goldstone Boson Models for the XENON1T Excess, arXiv:2007.00874 [INSPIRE].  
[13] P. Athron et al., Global fits of axion-like particles to XENON1T and astrophysical data, JHEP 05 (2021) 159 [arXiv:2007.05517] [INSPIRE].  
[14] C. Han, M.L. López-Ibanez, A. Melis, O. Vives and J.M. Yang, Anomaly-free leptophilic axionlike particle and its flavor violating tests, Phys. Rev. D 103 (2021) 035028 [arXiv:2007.08834] [INSPIRE].  
[15] Y. Chen, M.-Y. Cui, J. Shu, X. Xue, G.-W. Yuan and Q. Yuan, Sun heated MeV-scale dark matter and the XENON1T electron recoil excess, JHEP 04 (2021) 282 [arXiv:2006.12447] [INSPIRE].  
[16] Q.-H. Cao, R. Ding and Q.-F. Xiang, Searching for sub-MeV boosted dark matter from xenon electron direct detection, Chin. Phys. C 45 (2021) 045002 [arXiv:2006.12767] [INSPIRE].  
[17] L. Su, W. Wang, L. Wu, J.M. Yang and B. Zhu, Atmospheric Dark Matter and Xenon1T Excess, Phys. Rev. D 102 (2020) 115028 [arXiv:2006.11837] [INSPIRE].  
[18] G. Paz, A.A. Petrov, M. Tammaro and J. Zupan, Shining dark matter in Xenon1T, Phys. Rev. D 103 (2021) L051703 [arXiv:2006.12462] [INSPIRE].  
[19] K. Nakayama and Y. Tang, Gravitational Production of Hidden Photon Dark Matter in Light of the XENON1T Excess, Phys. Lett. B 811 (2020) 135977 [arXiv:2006.13159] [INSPIRE].  
[20] Y. Jho, J.-C. Park, S.C. Park and P.-Y. Tseng, Leptonic New Force and Cosmic-ray Boosted Dark Matter for the XENON1T Excess, Phys. Lett. B 811 (2020) 135863 [arXiv:2006.13910] [INSPIRE].  
[21] L. Zu, G.-W. Yuan, L. Feng and Y.-Z. Fan, Mirror Dark Matter and Electronic Recoil Events in XENON1T, Nucl. Phys. B 965 (2021) 115369 [arXiv:2006.14577] [INSPIRE].  
[22] L. Delle Rose, G. Hütsi, C. Marzo and L. Marzola, Impact of loop-induced processes on the boosted dark matter interpretation of the XENON1T excess, JCAP 02 (2021) 031 [arXiv:2006.16078] [INSPIRE].  
[23] H. Alhazmi, D. Kim, K. Kong, G. Mohlabeng, J.-C. Park and S. Shin, Implications of the XENON1T Excess on the Dark Matter Interpretation, JHEP 05 (2021) 055 [arXiv:2006.16252] [INSPIRE].  
[24] P. Ko and Y. Tang, Semi-annihilating  $Z_{3}$  dark matter for XENON1T excess, Phys. Lett. B 815 (2021) 136181 [arXiv:2006.15822] [INSPIRE].  
[25] S. Chigusa, M. Endo and K. Kohri, Constraints on electron-scattering interpretation of XENON1T excess, JCAP 10 (2020) 035 [arXiv:2007.01663] [INSPIRE].  
[26] K. Harigaya, Y. Nakai and M. Suzuki, Inelastic Dark Matter Electron Scattering and the XENON1T Excess, Phys. Lett. B 809 (2020) 135729 [arXiv:2006.11938] [INSPIRE].  
[27] M. Baryakhtar, A. Berlin, H. Liu and N. Weiner, Electromagnetic Signals of Inelastic Dark Matter Scattering, arXiv:2006.13918 [INSPIRE].  
[28] H. An and D. Yang, Direct detection of freeze-in inelastic dark matter, Phys. Lett. B 818 (2021) 136408 [arXiv:2006.15672] [INSPIRE].

[29] H.M. Lee, Exothermic dark matter for XENON1T excess, JHEP 01 (2021) 019 [arXiv:2006.13183] [INSPIRE].  
[30] J. Bramante and N. Song, Electric But Not Eclectic: Thermal Relic Dark Matter for the XENON1T Excess, Phys. Rev. Lett. 125 (2020) 161805 [arXiv:2006.14089] [INSPIRE].  
[31] H. An, M. Pospelov, J. Pradler and A. Ritz, New limits on dark photons from solar emission and keV scale dark matter, Phys. Rev. D 102 (2020) 115022 [arXiv:2006.13929] [INSPIRE].  
[32] I.M. Bloch, A. Caputo, R. Essig, D. Redigolo, M. Sholapurkar and T. Volansky, Exploring new physics with  $O(keV)$  electron recoils in direct detection experiments, JHEP 01 (2021) 178 [arXiv:2006.14521] [INSPIRE].  
[33] M. Dutta, S. Mahapatra, D. Borah and N. Sahu, Self-interacting Inelastic Dark Matter in the light of XENON1T excess, Phys. Rev. D 103 (2021) 095018 [arXiv:2101.06472] [INSPIRE].  
[34] H.-J. He, Y.-C. Wang and J. Zheng, GeV-scale inelastic dark matter with dark photon mediator via direct detection and cosmological and laboratory constraints, Phys. Rev. D 104 (2021) 115033 [arXiv:2012.05891] [INSPIRE].  
[35] G. Guo, Y.-L.S. Tsai, M.-R. Wu and Q. Yuan, Elastic and Inelastic Scattering of Cosmic-Rays on Sub-GeV Dark Matter, Phys. Rev. D 102 (2020) 103004 [arXiv:2008.12137] [INSPIRE].  
[36] D. Borah, S. Mahapatra, D. Nanda and N. Sahu, Inelastic fermion dark matter origin of XENON1T excess with muon  $(g - 2)$  and light neutrino mass, Phys. Lett. B 811 (2020) 135933 [arXiv:2007.10754] [INSPIRE].  
[37] J.A. Dror, G. Elor, R. McGehee and T.-T. Yu, Absorption of sub-MeV fermionic dark matter by electron targets, Phys. Rev. D 103 (2021) 035001 [arXiv:2011.01940] [INSPIRE].  
[38] U.K. Dey, T.N. Maity and T.S. Ray, Prospects of Migdal Effect in the Explanation of XENON1T Electron recoil Excess, Phys. Lett. B 811 (2020) 135900 [arXiv:2006.12529] [INSPIRE].  
[39] G. Choi, M. Suzuki and T.T. Yanagida, XENON1T Anomaly and its Implication for Decaying Warm Dark Matter, Phys. Lett. B 811 (2020) 135976 [arXiv:2006.12348] [INSPIRE].  
[40] N.F. Bell, J.B. Dent, B. Dutta, S. Ghosh, J. Kumar and J.L. Newstead, Explaining the XENON1T excess with Luminous Dark Matter, Phys. Rev. Lett. 125 (2020) 161803 [arXiv:2006.12461] [INSPIRE].  
[41] M. Du, J. Liang, Z. Liu, V.Q. Tran and Y. Xue, On-shell mediator dark matter models and the Xenon1T excess, Chin. Phys. C 45 (2021) 013114 [arXiv:2006.11949] [INSPIRE].  
[42] A. Hryczuk and K. Jodlowski, Self-interacting dark matter from late decays and the  $H_0$  tension, Phys. Rev. D 102 (2020) 043024 [arXiv:2006.16139] [INSPIRE].  
[43] S. Shakeri, F. Hajkarim and S.-S. Xue, Shedding New Light on Sterile Neutrinos from XENON1T Experiment, JHEP 12 (2020) 194 [arXiv:2008.05029] [INSPIRE].  
[44] S.-S. Xue, Spontaneous Pecei-Quinn symmetry breaking renders sterile neutrino, axion and  $\chi$  boson to be candidates for dark matter particles, arXiv:2012.04648 [INSPIRE].  
[45] V.V. Khruschov, Interpretation of the XENON1T excess in the model with decaying sterile neutrinos, arXiv:2008.03150 [INSPIRE].  
[46] N.F. Bell, V. Cirigliano, M.J. Ramsey-Musolf, P. Vogel and M.B. Wise, How magnetic is the Dirac neutrino?, Phys. Rev. Lett. 95 (2005) 151802 [hep-ph/0504134] [INSPIRE].

[47] N.F. Bell, M. Gorchtein, M.J. Ramsey-Musolf, P. Vogel and P. Wang, Model independent bounds on magnetic moments of Majorana neutrinos, Phys. Lett. B 642 (2006) 377 [hep-ph/0606248] [INSPIRE].  
[48] O.G. Miranda, D.K. Papoulias, M. Tórtola and J.W.F. Valle, XENON1T signal from transition neutrino magnetic moments, Phys. Lett. B 808 (2020) 135685 [arXiv:2007.01765] [INSPIRE].  
[49] K.S. Babu, S. Jana and M. Lindner, Large Neutrino Magnetic Moments in the Light of Recent Experiments, JHEP 10 (2020) 040 [arXiv:2007.04291] [INSPIRE].  
[50] V. Brdar, A. Greljo, J. Kopp and T. Opferkuch, The Neutrino Magnetic Moment Portal, in 55th Rencontres de Moriond on Electroweak Interactions and Unified Theories, (2021) [arXiv:2105.06846] [INSPIRE].  
[51] Z. Ye, F. Zhang, D. Xu and J. Liu, Unambiguously Resolving the Potential Neutrino Magnetic Moment Signal at Large Liquid Scintillator Detectors, Chin. Phys. Lett. 38 (2021) 111401 [arXiv:2103.11771] [INSPIRE].  
[52] K. Ni, J. Qi, E. Shockley and Y. Wei, Sensitivity of a Liquid Xenon Detector to Neutrino-Nucleus Coherent Scattering and Neutrino Magnetic Moment from Reactor Neutrinos, Universe 7 (2021) 54 [INSPIRE].  
[53] B. Yue, J. Liao and J. Ling, Probing neutrino magnetic moment at the Jinping neutrino experiment, JHEP 08 (2021) 068 [arXiv:2102.12259] [INSPIRE].  
[54] D. Aristizabal Sierra, R. Branada, O.G. Miranda and G. Sanchez Garcia, Sensitivity of direct detection experiments to neutrino magnetic dipole moments, JHEP 12 (2020) 178 [arXiv:2008.05080] [INSPIRE].  
[55] A.N. Khan, Can Nonstandard Neutrino Interactions explain the XENON1T spectral excess?, Phys. Lett. B 809 (2020) 135782 [arXiv:2006.12887] [INSPIRE].  
[56] C. Boehm, D.G. Cerdeno, M. Fairbairn, P.A.N. Machado and A.C. Vincent, Light new physics in XENON1T, Phys. Rev. D 102 (2020) 115013 [arXiv:2006.11250] [INSPIRE].  
[57] I. Alikhanov and E. Paschos, A Light Mediator Relating Neutrino Reactions, Universe 7 (2021) 204 [arXiv:2106.12364] [INSPIRE].  
[58] Z. Chen, T. Li and J. Liao, Constraints on general neutrino interactions with exotic fermion from neutrino-electron scattering experiments, JHEP 05 (2021) 131 [arXiv:2102.09784] [INSPIRE].  
[59] M. Ibe, S. Kobayashi, Y. Nakayama and S. Shirai, Cosmological Constraint on Vector Mediator of Neutrino-Electron Interaction in light of XENON1T Excess, JHEP 12 (2020) 004 [arXiv:2007.16105] [INSPIRE].  
[60] A. Bally, S. Jana and A. Trautner, Neutrino self-interactions and XENON1T electron recoil excess, Phys. Rev. Lett. 125 (2020) 161802 [arXiv:2006.11919] [INSPIRE].  
[61] D. Aristizabal Sierra, V. De Romeri, L.J. Flores and D.K. Papoulias, Light vector mediators facing XENON1T data, Phys. Lett. B 809 (2020) 135681 [arXiv:2006.12457] [INSPIRE].  
[62] M. Lindner, Y. Mambrini, T.B. de Melo and F.S. Queiroz, XENON1T anomaly: A light Z' from a Two Higgs Doublet Model, Phys. Lett. B 811 (2020) 135972 [arXiv:2006.14590] [INSPIRE].  
[63] S. Karmakar and S. Pandey, XENON1T constraints on neutrino non-standard interactions, arXiv:2007.11892 [INSPIRE].

[64] S.-F. Ge, P. Pasquini and J. Sheng, Solar neutrino scattering with electron into massive sterile neutrino, Phys. Lett. B 810 (2020) 135787 [arXiv:2006.16069] [INSPIRE].  
[65] I.M. Shoemaker, Y.-D. Tsai and J. Wyenberg, Active-to-sterile neutrino dipole portal and the XENON1T excess, Phys. Rev. D 104 (2021) 115026 [arXiv:2007.05513] [INSPIRE].  
[66] R. Essig, J. Mardon and T. Volansky, Direct Detection of Sub-GeV Dark Matter, Phys. Rev. D 85 (2012) 076007 [arXiv:1108.5383] [INSPIRE].  
[67] R. Essig, A. Manalaysay, J. Mardon, P. Sorensen and T. Volansky, First Direct Detection Limits on sub-GeV Dark Matter from XENON10, Phys. Rev. Lett. 109 (2012) 021301 [arXiv:1206.2644] [INSPIRE].  
[68] R. Essig, M. Fernandez-Serra, J. Mardon, A. Soto, T. Volansky and T.-T. Yu, Direct Detection of sub-GeV Dark Matter with Semiconductor Targets, JHEP 05 (2016) 046 [arXiv:1509.01598] [INSPIRE].  
[69] B.M. Roberts, V.A. Dzuba, V.V. Flambaum, M. Pospelov and Y.V. Stadnik, Dark matter scattering on electrons: Accurate calculations of atomic excitations and implications for the DAMA signal, Phys. Rev. D 93 (2016) 115037 [arXiv:1604.04559] [INSPIRE].  
[70] R. Essig, T. Volansky and T.-T. Yu, New Constraints and Prospects for sub-GeV Dark Matter Scattering off Electrons in Xenon, Phys. Rev. D 96 (2017) 043017 [arXiv:1703.00910] [INSPIRE].  
[71] R. Catena, T. Emken, N.A. Spaldin and W. Tarantino, Atomic responses to general dark matter-electron interactions, Phys. Rev. Res. 2 (2020) 033195 [arXiv:1912.08204] [INSPIRE].  
[72] G.J. Gounaris, E.A. Paschos and P.I. Porfyriadis, The Ionization of H, He or Ne atoms using neutrinos or anti-neutrinos at keV energies, Phys. Lett. B 525 (2002) 63 [hep-ph/0109183] [INSPIRE].  
[73] G.J. Gounaris, E.A. Paschos and P.I. Porfyriadis, *Electron spectra in the ionization of atoms by neutrinos*, Phys. Rev. D 70 (2004) 113008 [hep-ph/0409053] [INSPIRE].  
[74] M.B. Voloshin, Neutrino scattering on atomic electrons in searches for neutrino magnetic moment, Phys. Rev. Lett. 105 (2010) 201801 [Erratum ibid. 106 (2011) 059901] [arXiv:1008.2171] [INSPIRE].  
[75] K.A. Kouzakov and A.I. Studenikin, Magnetic neutrino scattering on atomic electrons revisited, Phys. Lett. B 696 (2011) 252 [arXiv:1011.5847] [INSPIRE].  
[76] K.A. Kouzakov, A.I. Studenikin and M.B. Voloshin, Neutrino-impact ionization of atoms in searches for neutrino magnetic moment, Phys. Rev. D 83 (2011) 113001 [arXiv:1101.4878] [INSPIRE].  
[77] J.-W. Chen, C.P. Liu, C.-F. Liu and C.-L. Wu, Ionization of hydrogen by neutrino magnetic moment, relativistic muon, and WIMP, Phys. Rev. D 88 (2013) 033006 [arXiv:1307.2857] [INSPIRE].  
[78] J.-W. Chen et al., Atomic ionization of germanium by neutrinos from an ab initio approach, Phys. Lett. B 731 (2014) 159 [arXiv:1311.5294] [INSPIRE].  
[79] I.B. Whittingham, Scattering of low energy neutrinos and antineutrinos by atomic electrons, Phys. Rev. D 105 (2022) 013008 [arXiv:2109.13454] [INSPIRE].  
[80] S. Weinberg, The Quantum theory of fields. Vol. 1: Foundations, Cambridge University Press, Cambridge, U.K. (1995) [DOI] [INSPIRE].

[81] M.E. Peskin and D.V. Schroeder, An Introduction to quantum field theory, Addison-Wesley, Reading, U.S.A. (1995) [INSPIRE].  
[82] H.A. Bethe and E.E. Salpeter, Quantum Mechanics of One- and Two-Electron Atoms, Springer, Berlin, Heidelberg, Germany (1957) [DOI] [INSPIRE].  
[83] Y. Chen et al., Earth Shielding and Daily Modulation from Electrophilic Boosted Dark Matter, arXiv:2110.09685 [INSPIRE].  
[84] M. Szydagis et al., NEST: A Comprehensive Model for Scintillation Yield in Liquid Xenon, 2011 JINST 6 P10002 [arXiv:1106.1613] [INSPIRE].  
[85] N. Vinyoles et al., A new Generation of Standard Solar Models, Astrophys. J. 835 (2017) 202 [arXiv:1611.09867] [INSPIRE].  
[86] XENON collaboration, Energy resolution and linearity of XENON1T in the MeV energy range, Eur. Phys. J. C 80 (2020) 785 [arXiv:2003.03825] [INSPIRE].  
[87] E.G. Adelberger, J.H. Gundlach, B.R. Heckel, S. Hoedl and S. Schlamminger, Torsion balance experiments: A low-energy frontier of particle physics, Prog. Part. Nucl. Phys. 62 (2009) 102 [INSPIRE].  
[88] E. Hardy and R. Lasenby, Stellar cooling bounds on new light particles: plasma mixing effects, JHEP 02 (2017) 033 [arXiv:1611.05852] [INSPIRE].  
[89] K.S. Babu, G. Chauhan and P.S. Bhupal Dev, Neutrino nonstandard interactions via light scalars in the Earth, Sun, supernovae, and the early Universe, Phys. Rev. D 101 (2020) 095029 [arXiv:1912.13488] [INSPIRE].  
[90] P.S. Pasquini and O.L.G. Peres, Bounds on Neutrino-Scalar Yukawa Coupling, Phys. Rev. D 93 (2016) 053007 [Erratum ibid. 93 (2016) 079902] [arXiv:1511.01811] [INSPIRE].  
[91] J.M. Berryman, A. De Gouvêa, K.J. Kelly and Y. Zhang, Lepton-Number-Charged Scalars and Neutrino Beamstrahlung, Phys. Rev. D 97 (2018) 075030 [arXiv:1802.00009] [INSPIRE].  
[92] J.A. Dror, Discovering leptonic forces using nonconserved currents, Phys. Rev. D 101 (2020) 095013 [arXiv:2004.04750] [INSPIRE].  
[93] A. de Gouvêa, P.S.B. Dev, B. Dutta, T. Ghosh, T. Han and Y. Zhang, Leptonic Scalars at the LHC, JHEP 07 (2020) 142 [arXiv:1910.01132] [INSPIRE].  
[94] P. Bakhti and Y. Farzan, Constraining secret gauge interactions of neutrinos by meson decays, Phys. Rev. D 95 (2017) 095008 [arXiv:1702.04187] [INSPIRE].  
[95] PANDAX collaboration, Dark matter direct search sensitivity of the PandaX-4T experiment, Sci. China Phys. Mech. Astron. 62 (2019) 31011 [arXiv:1806.02229] [INSPIRE].  
[96] XENON collaboration, Projected WIMP sensitivity of the XENONnT dark matter experiment, JCAP 11 (2020) 031 [arXiv:2007.08796] [INSPIRE].  
[97] LUX collaboration, Results from a search for dark matter in the complete LUX exposure, Phys. Rev. Lett. 118 (2017) 021303 [arXiv:1608.07648] [INSPIRE].  
[98] D.Y. Akimov et al., WIMP-nucleon cross-section results from the second science run of ZEPLIN-III, Phys. Lett. B 709 (2012) 14 [arXiv:1110.4769] [INSPIRE].  
[99] PANDAX-II collaboration, Dark Matter Results from First 98.7 Days of Data from the PandaX-II Experiment, Phys. Rev. Lett. 117 (2016) 121303 [arXiv:1607.07400] [INSPIRE].  
[100] LUX-ZEPLIN collaboration, Projected WIMP sensitivity of the LUX-ZEPLIN dark matter experiment, Phys. Rev. D 101 (2020) 052002 [arXiv:1802.06039] [INSPIRE].