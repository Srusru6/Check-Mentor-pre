# Optical Resonator Analog of a Two-Dimensional Topological Insulator

G. Q. Liang<sup>1</sup> and Y. D. Chong<sup>1,2,*</sup>

<sup>1</sup>Division of Physics and Applied Physics, School of Physical and Mathematical Sciences, Nanyang Technological University, Singapore, 637371 Singapore

$^{2}$ Centre for Disruptive Photonic Technologies, School of Physical and Mathematical Sciences, Nanyang Technological University, Singapore, 637371 Singapore (Received 24 December 2012; revised manuscript received 4 February 2013; published 14 May 2013)

A lattice of optical ring resonators can exhibit a topological insulator phase, with the role of spin played by the direction of propagation of light within each ring. Unlike the system studied by Hafezi et al., [Nat. Phys. 7, 907 (2011).] topological protection is achieved without fine-tuning the interresonator couplings, which are given the same periodicity as the underlying lattice. The topological insulator phase occurs for strong couplings, when the tight-binding method is inapplicable. Using the transfer matrix method, we derive the band structure and phase diagram, and demonstrate the existence of robust edge states. When gain and loss are introduced, the system functions as a diode for coupled resonator modes.

DOI: 10.1103/PhysRevLett.110.203904

PACS numbers: 42.60.Da, 42.70.Qs, 73.43.-f

The idea that photonic modes can have nontrivial topological properties, like topological states of quantum matter, originated with Haldane and Raghu [1,2], who predicted that a two-dimensional (2D) photonic crystal with broken time-reversal symmetry can support modes analogous to those of a "zero-field" quantum Hall gas [3]. This has been confirmed experimentally, using gyromagnetic photonic crystals operating at microwave frequencies [4-7]. That system's most striking feature is the existence of topologically protected one-way photonic edge states, which could be used for on-chip isolation [4]. However, this is difficult to realize at optical frequencies, where magneto-optic effects are weak. Different systems supporting topological photonic modes have subsequently been proposed [8-17]. In particular, Hafezi et al. [9] studied a lattice of ring resonators, similar to a 2D version of the CROW (coupled resonator optical waveguide) [18], in which the direction of propagation of light within each resonator acts as a twofold "spin" degree of freedom. In the tight-binding (weak-coupling) regime, coupling waveguides can be used to implement spin-conserving hopping between adjacent resonator modes, and phase shifts in these couplers give rise to an effective vector potential in the tight-binding hopping amplitudes, with opposite signs for the two spins. With a choice of phase shifts implementing the Landau gauge (which is aperiodic in the lattice), the effective magnetic field can be made uniform and nonzero, which yields a photonic analog of the integer quantum Hall effect in each spin sector, with a Hofstadter butterfly spectrum [19] and topologically protected edge states. Although the system is reciprocal (time reversal maps the two spin sectors onto each other), and thus cannot be used as a conventional optical isolator, Hafezi et al. suggested that the edge states can serve as robust optical delay lines [9].

The spin-dependent magnetic field in this system is reminiscent of the topological insulator model of Kane

and Mele [20,21], which has attracted major theoretical and experimental interest [22]. However, there is one major difference: the couplings in the Kane-Mele model have the periodicity of the lattice, and decoupling the two spin sectors reduces the model to two zero-field quantum Hall systems [3], with zero net magnetic flux through each unit cell. In the system of Hafezi et al., the couplings are aperiodic and decoupled spin sectors act as integer quantum Hall systems; the tight-binding analysis seemed to imply that the periodic, zero-field system is topologically trivial [9]. Aperiodic couplings also impose a practical design challenge, since a variety of different couplers must be used.

In this Letter, we show that the zero-field resonator lattice supports a topological insulator phase. When the interresonator couplings are tuned to large values beyond the tight-binding regime, the system exhibits one-way edge states, with nonzero  $Z_{2}$  topological invariant [21]; if the two spin sectors are decoupled, each acts as a zero-field system, like the Kane-Mele model [20,21]. The system therefore behaves as a photonic topological insulator. Previously, Khanikaev et al. [16] proposed a different photonic topological insulator, which also did not require aperiodic couplings, using linear combinations of polarization states as the spin analog. However, that system relies on the special properties of metamaterials, whereas the present one uses ordinary dielectric materials and is thus considerably more feasible.

Our calculations rely on the transfer matrix method, which has previously been applied to the CROW [23,24], and has a wider domain of validity for such systems than the tight-binding method [24]. This method also lets us easily study the effects of gain and loss, which can produce behaviors not easily obtainable in electronic topological insulators. We focus on the  $PT$  (parity or time-reversal) symmetric lattice [25], which contains balanced amounts

of gain and loss. Theoretical and experimental studies have shown that  $PT$ -symmetric lattices possess unusual properties, including bifurcations between real and complex bands [26-31]. We show that in a  $PT$ -symmetric photonic topological insulator, one edge state can be amplified while the back-propagating state of the same spin, on the opposite edge, is damped. The lattice thus acts as a robust optical diode for CROW modes.

The resonator lattice is shown schematically in Fig. 1. A ring resonator occupies each site of a square lattice. Its modes have a twofold "spin" corresponding to the propagation direction within the ring. As proposed in Ref. [9] and depicted in Fig. 1(c), waveguides can be used to couple these modes to those on neighboring resonators. For our purposes, it is useful to employ a more abstract representation for this coupling. We first assume no spin mixing—modes couple only to other modes of the same spin—and restrict our attention to a single spin. Let  $n \equiv (x_{n}, y_{n})$  denote a lattice site,  $n + x$  the site one unit in the  $+\hat{x}$  direction, etc. We specify the coupling between the resonators at  $n$  and  $n + x$  with complex numbers  $r_{nx}, r_{nx}', t_{nx}$  and  $t_{nx}'$ ; similarly, we specify the coupling between  $n$  and  $n + y$  by  $r_{ny}, r_{ny}', t_{ny}$ , and  $t_{ny}'$ . These relate the wave amplitudes in the resonator—see Fig. 1(a)—according to

$$
S _ {n x} \left[ \begin{array}{c} a _ {n} \\ b _ {n + x} \end{array} \right] = \left[ \begin{array}{c} d _ {n + x} \\ c _ {n} \end{array} \right], \tag {1}
$$

$$
S _ {n y} \left[ \begin{array}{c} d _ {n} \\ c _ {n + y} \end{array} \right] = \left[ \begin{array}{c} b _ {n + y} \\ a _ {n} \end{array} \right] e ^ {- 2 i \phi},
$$

where

$$
S _ {n \mu} = \left[ \begin{array}{l l} r _ {n \mu} & t _ {n \mu} ^ {\prime} \\ t _ {n \mu} & r _ {n \mu} ^ {\prime} \end{array} \right]. \tag {2}
$$

Here, and in the following, the dummy index  $\mu$  may stand for  $x$  or  $y$ . The parameter  $\phi$  is the phase delay across each

![](images/70b3da8fcdba28e6cd04622a32d5c21cee0c6d1cdbbd69ec59b26f5fd8112cb5.jpg)  
FIG. 1 (color online). (a) Schematic of couplings between neighboring ring resonators showing the wave amplitudes entering into the coupling relations (1). (b) Schematic of the resonator lattice over several periods. (c) Schematic of a coupling waveguide which can produce the couplings shown in (a);  $\{\alpha, \beta, \gamma, \delta\}$  label the wave amplitudes in the waveguides, and  $\{\psi_1, \psi_2\}$  the phase shifts, which are used in the calculation of the coupling coefficients [32].

![](images/71d8762c739c5f504e9bf0b2259a371b76f9b3b8aa8dafa8e5664764c101c443.jpg)

quarter of the ring. The  $S_{n\mu}$ 's, which have the form of scattering matrices, express the most general form of linear spin-conserving coupling between rings. In principle, the coefficients  $\{r_{n\mu}, r_{n\mu}', t_{n\mu}, t_{n\mu}'\}$  can be independently varied by tuning the underlying waveguides [32]. In an experimental system,  $\phi$  and the coupling coefficients would depend on frequency, but here we treat them as independent quantities; when calculating the band structure,  $\phi$  plays the role of frequency [24].

Consider the special case where the coupling coefficients vary between different sites according to

$$
r _ {n \mu} = r _ {\mu} e ^ {i A _ {n} ^ {\mu}}, \quad t _ {n \mu} ^ {\prime} = t _ {\mu} ^ {\prime}, \tag {3}
$$

$$
t _ {n \mu} = t _ {\mu}, \quad r _ {n \mu} ^ {\prime} = r _ {\mu} ^ {\prime} e ^ {- i A _ {n} ^ {\mu}}.
$$

Here,  $A_{n}^{x}$  and  $A_{n}^{y}$  play the role of a magnetic vector potential. These gauge relations generalize those used in Ref. [9], which involved phase differences in tight-binding hopping amplitudes. Suppose the vector potential corresponds to a uniform rational magnetic flux through each unit cell:  $A_{n}^{x} + A_{n + x}^{y} - A_{n + y}^{x} - A_{n}^{y} = 2\pi P / Q$ , where  $P$  and  $Q$  are integers. For  $Q = 1$ , i.e., integer flux through each unit cell, the band structure is the same as in the zero-field ( $A_{n}^{x} = A_{n}^{y} = 0$ ) system. Then the magnetic unit cell coincides with the lattice's unit cell, and there are solutions of the form [19,24]

$$
a _ {n + \mu} = e ^ {i \left(K _ {\mu} + A _ {n} ^ {\mu}\right)} a _ {n}, \quad b _ {n + \mu} = e ^ {i \left(K _ {\mu} + A _ {n} ^ {\mu}\right)} b _ {n}, \tag {4}
$$

where  $K_{\mu}$  is a Bloch wave vector. Combining Eqs. (1)-(4) gives [32]

$$
e ^ {- 4 i \phi} - B e ^ {- 2 i \phi} - C = 0,
$$

$$
B = r _ {x} ^ {\prime} t _ {y} ^ {\prime} e ^ {i K _ {x}} + r _ {x} t _ {y} e ^ {- i K _ {x}} + t _ {x} r _ {y} ^ {\prime} e ^ {i K _ {y}} + t _ {x} ^ {\prime} r _ {y} e ^ {- i K _ {y}},
$$

$$
C = \left(r _ {x} r _ {x} ^ {\prime} - t _ {x} t _ {x} ^ {\prime}\right) \left(r _ {y} r _ {y} ^ {\prime} - t _ {y} t _ {y} ^ {\prime}\right). \tag {5}
$$

As we shall see, for unitary couplings this gives rise to four real bands in the periodic space  $\phi \in [-\pi, \pi]$ : two in  $[- \pi/2, \pi/2]$  from directly solving Eq. (5), and the other two by adding  $\pm \pi$ . This result relies crucially on the fact that in Eq. (3) there is no phase variation in  $t_{n\mu}$  and  $t_{n\mu}$ . The coupler shown in Fig. 1(c) satisfies this condition if the sum of the phase delays on its two arms is kept constant [32]. For noninteger fluxes  $(Q \neq 1)$ , the current approach gives essentially the same results as Ref. [9]: we could impose the Landau gauge  $A_n^x = (P/Q)y_n$  and  $A_n^y = 0$ , and define a  $Q \times 1$  magnetic unit cell for which  $a_{n+Qx} = e^{i(K_x + Py_n)}a_n$  and  $a_{n+y} = e^{iK_y}a_n$ , and similarly for  $b$ . This gives  $4Q$  bands, analogous to Landau levels.

In the remainder of this Letter, we focus on the zero-field (integer flux) system. If the couplings conserve energy, then  $S_{\mu}^{\dagger} = S_{\mu}^{-1}$ . We expect the band structure  $\phi(K_x, K_y)$  to be real (for  $K_x$  and  $K_y$  real), and this is easily proven using the parametrization

$$
r _ {\mu} = \sin \theta_ {\mu} e ^ {i \chi_ {\mu}}, \quad t _ {\mu} ^ {\prime} = - \cos \theta_ {\mu} e ^ {i \left(\varphi_ {\mu} - \xi_ {\mu}\right)}, \tag {6}
$$

$$
t _ {\mu} = \cos \theta_ {\mu} e ^ {i \xi_ {\mu}}, \qquad r _ {\mu} ^ {\prime} = \sin \theta_ {\mu} e ^ {i (\varphi_ {\mu} - \chi_ {\mu})},
$$

where  $\theta_{\mu}\in [0,\pi /2]$  and  $\chi_{\mu},\xi_{\mu},\varphi_{\mu}\in [0,2\pi ]$  Equation (5) then simplifies to  $e^{-4i\tilde{\phi}} + 2iYe^{-2i\tilde{\phi}} - 1 = 0$  , where

$$
Y \equiv \sin \theta_ {x} \cos \theta_ {y} \sin \tilde {K} _ {x} - \cos \theta_ {x} \sin \theta_ {y} \sin \tilde {K} _ {y},
$$

$$
\tilde {\phi} \equiv \phi + \frac {\varphi_ {x} + \varphi_ {y}}{4}, \tag {7}
$$

$$
\tilde {K} _ {x} \equiv K _ {x} + \frac {\varphi_ {x}}{2} - \chi_ {x} + \frac {\varphi_ {y}}{2} - \xi_ {y},
$$

$$
\tilde {K} _ {y} \equiv K _ {y} + \frac {\varphi_ {y}}{2} - \chi_ {y} - \frac {\varphi_ {x}}{2} + \xi_ {x}.
$$

For real  $K_{\mu}$ ,  $|Y| \leq \sin(\theta_x + \theta_y) \leq 1$ , and the bands are

$$
\phi_ {+} = m \pi - \frac {\varphi_ {x} + \varphi_ {y}}{4} + \frac {1}{2} \sin^ {- 1} \left[ Y \left(K _ {\mu}\right) \right], \tag {8}
$$

$$
\phi_ {-} = n \pi - \frac {\varphi_ {x} + \varphi_ {y}}{4} + \frac {1}{2} \left\{\pi - \sin^ {- 1} \left[ Y \left(K _ {\mu}\right) \right] \right\}.
$$

The above calculation also yields the phase diagram. Band-crossing points occur where the inequality saturates:  $\theta_{x} + \theta_{y} = \pi /2$ , or equivalently  $|r_x|^2 +|r_y|^2 = 1$ . This defines a boundary between two insulator phases. To show that one of these phases is topologically nontrivial, we specialize to  $\varphi_{\mu} = \chi_{\mu} = 0$ ,  $\xi_{\mu} = \pi /2$ , and  $\theta_{x} = \theta_{y} = \theta$ , so that

$$
Y = - \frac {1}{2} \sin 2 \theta [ \cos K _ {x} + \cos K _ {y} ]. \tag {9}
$$

The projected band diagram for a semi-infinite strip can be calculated similarly [32], with results shown in Fig. 2.

![](images/802f44f1e751fd7146e154e711dd1304fdc04df7cfee255ca63ff49065574f8f.jpg)  
FIG. 2 (color online). Projected band diagram of a semi-infinite resonator lattice, with ten cells in the  $y$  direction. The spin sectors are decoupled; the model parameters are given by Eq. (6) with  $\varphi_{\mu} = \chi_{\mu} = 0$ ,  $\xi_{\mu} = \pi /2$ , and  $\theta_{x} = \theta_{y} = \theta$ . Band crossing occurs at  $\theta = \pi /4$ , and the system is a topological insulator for  $\theta >\pi /4$ . For  $\theta = 0.4\pi$ , the points labeled  $A$  and  $B$  at  $\phi = \pi /4$  indicate the edge states plotted in Fig. 3.

For  $\theta < \pi /4$ , the system is a trivial insulator; although Fig. 2(a) exhibits edge states for some  $\phi$ , these are two-way edge states, and for each  $\phi$  there are states confined to the same edge at different  $K_{x}$ , with positive as well as negative group velocities. For  $\theta > \pi /4$ , the system is a topological insulator. The edge states span the band gaps, and for the given spin (clockwise) there is a positive velocity upper edge state and a negative velocity lower edge state (Fig. 3). In a real system, where the model parameters depend on the frequency  $\omega$ , the topologically nontrivial band gaps would correspond to frequencies for which  $\theta (\omega) > \pi /4$ . We have verified, using finite-difference time-domain simulations, that this strong-coupling regime can be achieved with realistic resonator and waveguide designs [32].

It is noteworthy that the topological insulator phase occurs only when the interresonator coupling is sufficiently strong. This phase does not appear in the tight-binding analysis, where the zero-field system appears to be topologically trivial [9]. The transfer matrix method, however, accounts for the wave amplitudes at different parts of each ring, which is needed to describe the edge states of the topological insulator phase. Roughly speaking, these edge states move in the same direction in which light propagates inside the upper (lower) half of the uppermost (lowermost) ring resonator of the strip.

Spin mixing can be induced by backscattering within the resonators or waveguides [9]. This lifts the spin degeneracy of the edge states [32], similar to the Rashba term in electronic topological insulators [20,21]. If the couplings remain unitary and reciprocal (i.e., absent radiative loss and magneto-optic disorder), the states on each edge are time-reversed partners, and the resulting band structure has a nonzero  $Z_{2}$  topological invariant [32].

We have studied the effects of incorporating gain and loss into the photonic topological insulator, which yields behaviors that are inaccessible in the electronic system [26]. In particular, we consider here the

![](images/f6f20594f6c4cf04804289638865881a785fecaffeabe42f8cafc85b47418345.jpg)  
FIG. 3 (color online). Semilog plot of edge state intensity versus  $y$  lattice coordinate demonstrating edge confinement. The edge states labeled  $A$  (filled circles) and  $B$  (open circles) have equal  $\phi = \pi /4$ , and occur at  $K_{x} = \mp 1.587$ , respectively. The parameters are the same as in Fig. 2, with  $\theta = 0.4\pi$ . The spins are clockwise, as depicted in Fig. 1. The intensities are defined as the value of  $(|a_n|^2 + |b_n|^2 + |c_n|^2 + |d_n|^2)/4$  in each resonator.

$PT$ -symmetric case, which corresponds to putting "balanced" gain and loss in symmetric regions of the unit cell.  $PT$ -symmetric photonic systems have previously been studied experimentally, e.g., using lossy waveguides [28] and optical fiber systems [31]. In the present system, the transfer matrix method can be adapted to include gain and loss simply by making the coupling matrices nonunitary. Specifically, the matrices obey the  $PT$ -symmetry relation [33-35]

$$
\mathcal {P T} S _ {\mu} \mathcal {P T} = S _ {\mu} ^ {- 1}. \tag {10}
$$

Here,  $\mathcal{P}$  and  $\mathcal{T}$  are parity and time-reversal operators. We choose  $\mathcal{P} = [0,1;1,0]$  and  $\mathcal{T}'$  to be the complex conjugation operator; for the coupler shown in Fig. 1(c), setting  $\psi_{2} = \psi_{1}^{*}$  satisfies Eq. (10). The  $S_{\mu}$ 's can then be parametrized by  $r = |r|e^{i\varphi}$ ,  $t' = -|t|e^{i(\varphi - \varphi')}$ ,  $t = |t|e^{i(\varphi + \varphi')}$ , and  $r' = |r'|e^{i\varphi}$ , where  $|rr'| + |t|^2 = 1$  [36]. For simplicity, we set  $\varphi = 0$  and  $\varphi' = \pi/2$ , so that

$$
r = e ^ {\Gamma} \sin \theta , \quad t ^ {\prime} = i \cos \theta , \tag {11}
$$

$$
t = i \cos \theta , \qquad r ^ {\prime} = e ^ {- \Gamma} \sin \theta ,
$$

where  $\Gamma$  characterizes the amount of gain and loss.

Figure 4 shows the effects of  $PT$ -symmetric gain and loss on the edge states of the photonic topological insulator. We assume no spin mixing;  $\Gamma$  is varied for the  $x$  couplings, while the  $y$  couplings are kept unitary  $(\Gamma = 0)$  [37]. For the bulk bands, Eq. (11) causes  $K_{x}$  to be replaced by  $K_{x} - i\Gamma$  in the solution (9), so that the bands are real for  $K_{x} = m\pi$ ,  $m \in \mathbb{Z}$ , and complex otherwise. The edge states on opposite edges of the semi-infinite strip, which have opposite velocities, acquire the same imaginary component to  $K_{x}$ , and are, respectively, amplified and damped. This has a simple interpretation. The upper edge state's wave amplitude is multiplied by  $r_x$  each time it hops one ring to the right; for  $\Gamma > 0$ ,  $|r_x| > 0$  and hence the state is

![](images/e2c98d3ff4927114a890b259571c637ba37a8563ac319e568a0117ba10c69b81.jpg)  
FIG. 4 (color online). Amplification and damping of edge states in the  $PT$ -symmetric resonator lattice.  $\Gamma$  is the gain-loss parameter defined in Eq. (11). All other parameters are the same as in Fig. 2, with  $\theta = 0.4\pi$ . Both edge states acquire the same value of  $\mathrm{Im}[K_x]$ , so one is damped and the other amplified. Inset: intensity profiles for the lower edge state (filled circles) and upper edge state (open circles) at  $\Gamma = 0.2$ .

amplified. Likewise, the lower edge state is damped by  $r_x'$  with each leftward hop. Previous studies of  $PT$ -symmetric waveguides have shown that modes with different transverse profiles can be selectively amplified and damped [28], but in those waveguides each amplified (damped) mode has a counterpropagating partner which is amplified (damped) by an equal amount. Here, the edge states have no counterpropagating partners of the same spin.

Figure 5 shows the transmittance between waveguides coupled to opposite ends of the finite  $PT$ -symmetric lattice. Left-to-right transmission is amplified, while transmission in the opposite direction is damped. Within the band gaps, the transmission is insensitive to disorder, due to the topological protection on the edge states. In Fig. 5(b), we test the effect of removing this topological protection by performing the calculation with the lattice width reduced to a single unit cell; the resulting transmission is considerably less stable, varying by an order of magnitude for the same values of  $\phi$  [32]. In terms of the underlying waveguides, the system is reciprocal, but it can nonetheless serve as a diode element for CROW modes. Such modes are susceptible to backscattering, even in the absence of spin flipping [9]; this is a particular problem in slow-light applications [38]. A photonic topological insulator can offset the effects of backscattering loss by robustly amplifying forward modes and damping backward modes. Unlike the

![](images/5f6d66234b5b526c166ab2e77ee623e26684747a88218416cdfd0fed69616e9f.jpg)

![](images/bf1d1c6ff6df6ee1ca9e702955c434b9ea22b219dd563b62328f1739d13825f0.jpg)  
FIG. 5 (color). Transmittance across a disordered  $PT$ -symmetric resonator lattice. (a) Schematic. (b) Transmittance from port  $A$  to  $B'$  (blue) for a one unit cell wide lattice, which has no topological protection. (c,d) Transmittance leftward from  $B$  to  $A'$  (red), and rightward from  $A$  to  $B'$  (blue), when the lattice is five unit cells wide as shown in (a). Reflectances are shown in grey. In (b)-(d), the lattice is five cells long, and transmittances are plotted for 20 disorder realizations, where each coupling has random  $\theta$  distributed uniformly in  $[0.2\pi, 0.5\pi]$ . The  $x$  couplings have  $\Gamma = 0.5$ .

![](images/5984aaa6fdef1a78d4b684eb00a008ffb45a72e7878db3e278d7b0e0692ece70.jpg)

![](images/3b847048c4ebf7958ae3a098cf58bd757d40d5f9b56c31f5db9fad5eb7168148.jpg)

$PT$ -symmetric diode of Ref. [39], this device does not require optical nonlinearity.

This research was supported by the Singapore National Research Foundation under Grant No. NRFF2012-02. We thank J. M. Taylor and M. Hafezi for helpful discussions.

*yidong@ntu.edu.sg  
[1] F.D.M. Haldane and S. Raghu, Phys. Rev. Lett. 100, 013904 (2008).  
[2] S. Raghu and F.D.M. Haldane, Phys. Rev. A 78, 033834 (2008).  
[3] F.D.M. Haldane, Phys. Rev. Lett. 61, 2015 (1988).  
[4] Z. Wang, Y.D. Chong, J.D. Joannopoulos, and M. Soljacic, Phys. Rev. Lett. 100, 013905 (2008).  
[5] Z. Wang, Y.D. Chong, J.D. Joannopoulos, and M. Soljacic, Nature (London) 461, 772 (2009).  
[6] J.-X. Fu, R.-J. Liu, and Z.-Y. Li, Appl. Phys. Lett. 97, 041112 (2010).  
[7] J.-X. Fu, J. Lian, R.-J. Liu, L. Gan, and Z.-Y. Li, Appl. Phys. Lett. 98, 211104 (2011).  
[8] J. Koch, A. A. Houck, K. Le Hur, and S. M. Girvin, Phys. Rev. A 82, 043811 (2010).  
[9] M. Hafezi, E. A. Demler, M. D. Lukin, and J. M. Taylor, Nat. Phys. 7, 907 (2011).  
[10] T. Ochiai, Phys. Rev. B 86, 075152 (2012).  
[11] K. Fang, Z. Yu, and S. Fan, Nat. Photonics 6, 782 (2012).  
[12] J. Koch, A. A. Houck, K. Le Hur, and S. M. Girvin, Phys. Rev. A 82, 043811 (2010).  
[13] A. Petrescu, A. A. Houck, and K. Le Hur, Phys. Rev. A 86, 053804 (2012).  
[14] I. Carusotto and C. Ciuti, Rev. Mod. Phys. 85, 299 (2013).  
[15] V. Yannopapas, New J. Phys. 14, 113017 (2012).  
[16] A. B. Khanikaev, S. H. Mousavi, W.-K. Tse, M. Kargarian, A. H. MacDonald, and G. Shvets, Nat. Mater. 12, 233 (2013).  
[17] M.C. Rechtsman, J.M. Zeuner, Y. Plotnik, Y. Lumer, S. Nolte, M. Segev, and A. Szameit, Nature (London) 496, 196 (2013).  
[18] A. Yariv, Y. Xu, R. K. Lee, and A. Scherer, Opt. Lett. 24, 711 (1999).  
[19] D.R. Hofstadter, Phys. Rev. B 14, 2239 (1976).  
[20] C.L. Kane and E.J. Mele, Phys. Rev. Lett. 95, 226801 (2005).

[21] C.L. Kane and E.J. Mele, Phys. Rev. Lett. 95, 146802 (2005).  
[22] J.E. Moore, Nature (London) 464, 194 (2010).  
[23] A. Yariv, IEEE Photonics Technol. Lett. 14, 483 (2002).  
[24] J. K. S. Poon, J. Scheuer, S. Mookherjea, G. T. Paloczi, Y. Huang, and A. Yariv, Opt. Express 12, 90 (2004).  
[25] C.M. Bender and S. Boettcher, Phys. Rev. Lett. 80, 5243 (1998).  
[26] K.G. Makris, R. El-Ganainy, D.N. Christodoulides, and Z.H. Musslimani, Phys. Rev. Lett. 100, 103904 (2008); Phys. Rev. A 81, 063807 (2010).  
[27] Z.H. Musslimani, K.G. Makris, R. El-Ganainy, and D.N. Christodoulides, Phys. Rev. Lett. 100, 030402 (2008); J. Phys. A 41, 244019 (2008).  
[28] A. Guo, G.J. Salamo, M. Volatier-Ravat, V. Aimez, G.A. Siviloglou, and D.N. Christodoulides, Phys. Rev. Lett. 103, 093902 (2009).  
[29] C.E. Ruter, K.G. Makris, R. El-Ganainy, D.N. Christodoulides, M. Segev, and D. Kip, Nat. Phys. 6, 192 (2010).  
[30] A. Szameit, M. C. Rechtsman, O. Bahat-Treidel, and M. Segev, Phys. Rev. A 84, 021806(R) (2011).  
[31] A. Regensburger, C. Bersch, M.-A. Miri, G. Onishchukov, D.N. Christodoulides, and U. Peschel, Nature (London) 488, 167 (2012).  
[32] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevLett.110.203904 for the derivation of the inter-ring coupling coefficients, time-domain simulation results for the edge states, and a detailed calculation of the projected band diagram.  
[33] H. Schomerus, Phys. Rev. Lett. 104, 233601 (2010).  
[34] Y. D. Chong, L. Ge, and A. D. Stone, Phys. Rev. Lett. 106, 093902 (2011).  
[35] L. Ge, Y.D. Chong, and A.D. Stone, Phys. Rev. A 85, 023802 (2012).  
[36] This parametrization differs from that of Ref. [35], which considered symmetric (reciprocal) scattering matrices.  
[37] Adding gain and loss to the  $y$  couplings while keeping the  $x$  couplings unitary causes the projected band structure to remain strictly real, including the edge states.  
[38] F. Morichetti, A. Canciamilla, M. Martinelli, A. Samarelli, R. M. De La Rue, M. Sorel, and A. Mellon, Appl. Phys. Lett. 96, 081112 (2010).  
[39] H. Ramezani, T. Kottos, R. El-Ganainy, and D.N. Christodoulides, Phys. Rev. A 82, 043803 (2010).