# PHYSICS

# Observing momentum disturbance in double-slit "which-way" measurements

Ya Xiao $^{1,2,3}$ , Howard M. Wiseman $^{4*}$ , Jin-Shi Xu $^{1,2*}$ , Yaron Kedem $^{5}$ , Chuan-Feng Li $^{1,2*}$ , Guang-Can Guo $^{1,2}$

Making a "which-way" measurement (WWM) to identify which slit a particle goes through in a double-slit apparatus will reduce the visibility of interference fringes. There has been a long-standing controversy over whether this can be attributed to an uncontrollable momentum transfer. Here, by reconstructing the Bohmian trajectories of single photons, we experimentally obtain the distribution of momentum change. For our WWM, the change we see is not a momentum kick that occurs at the point of the WWM, but rather one that nonclassically accumulates during the propagation of the photons. We further confirm a quantitative relation between the loss of visibility consequent on a WWM and the total (late-time) momentum disturbance. Our results emphasize the role of the Bohmian momentum in giving an intuitive picture of wave-particle duality and complementarity.

Copyright © 2019  
The Authors, some  
rights reserved;  
exclusive licensee  
American Association  
for the Advancement  
of Science. No claim to  
original U.S. Government  
Works. Distributed  
under a Creative  
Commons Attribution  
NonCommercial  
License 4.0 (CC BY-NC).

# INTRODUCTION

The single-particle Young's double-slit experiment is the quintessential example of the wave-particle duality of quantum mechanics (1, 2). If one performs a position measurement to determine which slit a quantum particle traverses (particle-like property), then the interference pattern (wave-like property) is damaged. The more "which-way" information one obtains, the lower the visibility of the interference fringes (3-6). However, there has been a vigorous debate on whether the which-way measurement (WWM) destroys interference by disturbing the momentum of the particle (7-12).

Opposite conclusions were obtained by two research groups. In 1991, Scully, Englert, and Walther (SEW) (7) proposed a WwM scheme to prove that one can perform a position measurement with sufficient precision to identify which slit the particle goes, without apparently disturbing its momentum at all. They attributed the loss of visibility to the correlations between particles and the detectors. However, soon after, Storey, Tan, Collett, and Walls (STCW) (8) provided a general formalism, which appeared to show that the detection of path information necessarily involves some momentum transfer to the particles. A careful analysis (11) resolved this contradiction by showing that SEW and STCW were using different concepts of momentum transfer: "classical" and "quantum," respectively. That is, their analyses were complementary. SEW's scheme could not be explained by a classical probability distribution for momentum kicks, while the STCW theorem did correctly establish that there must be a nonzero probability amplitude for a momentum change of the expected size.

To study the paradigm of particle-wave duality in more depth, we need a more robust way to quantify the momentum disturbance. Neither SEW nor STCW gave such a measure for general situations. The difficulty is that we cannot unambiguously determine the momentum change to the quantum particle if the particle is not initially in a momentum eigenstate, which is the situation we face in a two-slit experi

ment. Bohmian mechanics, however, offers a way to solve this difficulty, as it posits that a particle has a definite position and momentum at all times and hence follows a deterministic trajectory (13, 14). The Bohmian probability distribution for momentum transfer was introduced in (15) and showed to be well suited to characterizing the momentum transfers in a WWM, both classical (immediate) and quantum (delayed) (15). It is a true probability distribution and, moreover, can be experimentally observed using established techniques (16-18). This means that it is possible to experimentally explore the relation between the size of the momentum disturbance and the degree of visibility loss in a WWM.

In this work, we sent a triggered single photon through a birefringent double-slit apparatus and reconstructed its Bohmian trajectories using the technique of weak measurement (16-20). Then, we obtained the distribution of Bohmian momentum transfer to the particle in a WWM by comparing all the photon's trajectories in the free case and disturbed (WWM) case. We showed that the momentum change gradually accumulates during the propagation of the photons, which is negligible at short times. We further demonstrated the mean of the absolute value of the total (late-time) Bohmian momentum transfer  $\langle |p|\rangle_T^B$  to be larger than  $2\hbar /(\pi D)$ , where  $D$  is the center distance between the two slits. By implementing partial WWMs experimentally, we found that this mean and the visibility satisfy the inequality  $\langle |p|\rangle_T^B\geq (1 - V)2\hbar /(\pi D)$ . That is, increasing the momentum disturbance to the particle in a WWM is observed to be accompanied by a decreasing of the visibility of the interference fringes, thus quantitatively demonstrating wave-particle duality.

# RESULTS

# Bohmian momentum disturbance

According to Bohmian mechanics (13, 14), an individual particle has a definite position  $x$  and momentum  $p(x)$  (see also section SI in the Supplementary Materials). The Bohmian particle's momentum is determined by its position. It can be obtained experimentally by performing a weak measurement of the quantum mechanical momentum operator  $\hat{p}$ , post-selecting on finding it at position  $x$ , and averaging the result over many repetitions. This yields

$$
p (x) = \operatorname {R e} \left[ p _ {w} (x) \right] \tag {1}
$$

where  $p_w(x) = \langle x|\hat{p} |\psi \rangle /\langle x|\psi \rangle$  is the weak value of the momentum operator (21-25). Note that for a scalar nonrelativistic wave function

defined as  $\psi (x) = \sqrt{\rho(x)} e^{iS(x) / \hbar}$ , with  $\rho$  and  $S$  real, the above definition conforms to the original definition of the Bohmian momentum as  $p(x) = \nabla S(x)$  (13). Applying the above theory to photons might seem problematic (26) since electromagnetic waves correspond to particles with zero rest mass. However, we use a monochromatic beam, with  $x$  being the transverse position of the photon. This is well described by the nonrelativistic Schrödinger equation for a particle of mass  $m = h / (\lambda c)$ , where  $c$  is the speed of light and  $\lambda$  is the wavelength. Then, we can reconstruct the motion of this effective nonrelativistic particle using its position and velocity  $\nu (x) = p(x) / m$  (16-18).

In our experiment, we create an effective transverse wave function for the photon that is a superposition of two paths:  $\psi^{\phi}(x) = [f_u(x) + e^{i\phi}f_d(x)] / \sqrt{2}$ . Here,  $\phi$  is the relative phase between the paths, while  $f_{u(d)}(x) = (w\sqrt{2\pi})^{-1 / 2}e^{-(x\mp D / 2)^2 /w^2}$  is the Gaussian wave packet, with a waist of  $w$ , of the upper (lower) path, and  $D\gg w$ . An ideal WWM creates a two-component entangled state, correlating the path of the particle with orthogonal basis states of a probe. Measuring this probe in a different complementary basis realizes a quantum eraser (27). After the strong measurement, conditioned on the outcome, the wave function of the system (and its Bohmian particles) evolves independent of the measurement apparatus (14). In Bohmian mechanics, the details of the momentum change depend on the basis in which the WWM is measured because of the theory's nonlocality, as illustrated in (17, 18). The minimum momentum disturbance occurs when the two outcomes of the quantum eraser measurement project the system state into  $\psi^0$  and  $\psi^{\pi}$ , respectively (15). That is, the particle is still in a superposition of its two paths, only with different relative phases, which, when summed, wash out the interference pattern.

We create the above superpositions and consider an ensemble of Bohmian trajectories starting at  $N$  transverse positions  $x_{i}(z_{1})$ , where  $z_{1}$  represents the initial plane. By reconstructing each trajectory forward, as described above, to plane  $z_{j}$ , we can obtain an ensemble of new transverse photon positions  $x_{i}^{z_{j}}$  and transverse photon momenta  $p^{\phi}(x_{i}^{z_{j}})$ . The change in the Bohmian momentum for this single trajectory, as a consequence of inducing a phase  $\phi \neq 0$ , is then calculated as  $p_{i} = p^{\phi}(x_{i}^{z_{j}}) - p^{0}(x_{i}^{z_{j}})$ . By summing over all initial positions  $i$ , with the appropriate weights, the momentum disturbance distribution can be obtained (15)

$$
P _ {z _ {j}} ^ {\phi} (p) = \frac {1}{M} \sum_ {i = 2} ^ {N - 1} \wp \left(x _ {i} \left(z _ {1}\right)\right) \delta \left(p - p _ {i}\right) \tag {2}
$$

where  $M$  is a factor that ensures  $\int_{-\infty}^{\infty}P_{z_j}^{\phi}(p)dp = 1$  and  $\wp (x_i(z_1)) = |\psi^{\phi}(x_i(z_1))|^2 (x_{i + 1}^{z_1} - x_{i - 1}^{z_1}) / 2$ . To obtain a smooth distribution with a finite ensemble size  $M$ , we approximate  $\delta (p - p_i)$  by a Gaussian distribution of SD  $\sigma = 0.1\hbar /D$ . The Bohmian momentum disturbance distribution  $P_{z_j}^B (p)$  up to plane  $z_{j}$  due to the WWM can then be calculated as

$$
P _ {z _ {j}} ^ {B} (p) = \eta^ {0} P _ {z _ {j}} ^ {0} (p) + \eta^ {\pi} P _ {z _ {j}} ^ {\pi} (p) \tag {3}
$$

where  $\eta^0 (\eta^\pi)$  represents the weight of the case  $\phi = 0$ $(\phi = \pi)$ , with  $\eta^0 +\eta^\pi = 1$ . A WWM with perfect path distinguishability corresponds to  $\eta^0 = \eta^\pi = 1/2$ . The total momentum disturbance distribution,  $P_T^B (p)$ , is when  $z_{j}$  is in the far field.

We can quantify the momentum disturbance by

$$
\langle | p | \rangle_ {z _ {j}} ^ {B} = \int P _ {z _ {j}} ^ {B} (p) | p | d p \tag {4}
$$

It was shown theoretically (15) that, for WWMs achieving only partial distinguishability, resulting in a nonzero fringe visibility  $V$ , the total mean absolute momentum disturbance is bounded below

$$
\langle | p | \rangle_ {T} ^ {B} \geq \frac {2 \hbar}{\pi D} (1 - V) \tag {5}
$$

This relates the loss of interference in a WWM to the particle's momentum change. Moreover, the WWM that achieves this bound corresponds to that in Eq. 3, with  $\eta^0 = (1 + V) / 2$ .

# Experimental setup and results

Figure 1 shows our experimental setup. The generation of heralded signal photons is described in section SII of the Supplementary Materials. The signal photon is separated by a beam displacer into its horizontally and vertically polarized components, separated by about  $3\mathrm{mm}$ . By rotating the polarization of one of these beams and compensating the difference in their optical paths, they become distinguishable only by their transverse location, describable by a wave function  $[f_u(x) + e^{i\phi}f_d(x)] / \sqrt{2}$ . In our experiment, we simulate the quantum eraser WWM by inducing the relative phases  $\phi = 0$  or  $\phi = \pi$  by rotating half-wave plate 1 (HWP1) to  $22.5^{\circ}$  or  $67.5^{\circ}$ , respectively.

The signal photon is then sent to the transverse momentum (or velocity) measurement setup, which consists of a 0.7-mm-thick piece of calcite with its optic axis in the  $xz$  plane oriented at  $42^{\circ}$  to the  $z$  axis, followed by a quarter wave plate and a beam displacer. The photon's position  $x_{k}^{z_{j}}$  at the  $z_{j}$  plane is recorded by the pixels of the intensified charge-coupled device (ICCD) camera (Andor iStar 334), which is triggered by the electronic signal from the detection of the idler photon. The weak value of the transverse momentum is obtained from many runs by

$$
\langle p \left(x _ {k} ^ {z _ {j}}\right) \rangle_ {w} = \frac {h}{\lambda \zeta} \arcsin \left(\frac {N _ {R _ {k}} ^ {j} - N _ {L _ {k}} ^ {j}}{N _ {R _ {k}} ^ {j} + N _ {L _ {k}} ^ {j}}\right) \tag {6}
$$

where  $1 / \zeta = 1 / 336$  is the measured dimensionless coupling strength (18) and  $N_{R_k(L_k)}^j$  is the photon count corresponding to the right-hand

![](images/39de7045ca121668a3349b2a45ee9009893ebdedd2817700b859f70f82c19d4c.jpg)  
Fig. 1. Experimental setup. Heralded signal photons (SPs) are separated into two paths by a beam displacer (BD 30). A half-wave plate HWP1 is used to change the relative phase between these two paths, while HWP2 is used to make the polarization of both paths the same. A birefringent crystal (PC) is inserted into one of the paths to compensate the difference in the optical length. The photon is prepared in the diagonal polarization state by HWP3 and then goes through a thin calcite crystal to perform weak measurement. The optic axis of the calcite crystal is in the  $xz$  plane oriented at  $42^{\circ}$  to the  $z$  axis. A quarter wave plate (QWP) and a beam displacer (BD 40) are used to detect the polarization of the photon. A combination of three lenses, L1 (plano-convex), L2 (aspherical and moveable), and L3 (plano-convex cylindrical), is used to image different planes on the intensified charge-coupled device (ICCD) camera.

(left-hand) circular polarization. From this, we obtain the transverse Bohmian velocity as  $\nu (x_k^{z_j}) = \langle p(x_k^{z_j})\rangle_w / m$ . A system of three lenses (L1, L2, and L3), with the middle lens translatable in the  $z$  direction, allows us to vary  $z_{j}$  from the near field  $(z_{1} = 1.445\mathrm{m})$  to the far field  $(z_{117} = 8.612\mathrm{m})$ .

By measuring the transverse momenta or velocities (weakly) and positions (strongly) at a sequence of different imaging planes, we reconstruct the photon's Bohmian trajectories. For computational convenience, we follow the method in (18) to reconstruct the trajectories via  $x_{k}^{z_{j + 1}} = x_{k}^{z_{j}} + (z_{j + 1} - z_{j})\nu (x_{k}^{z_{j}}) / \sqrt{c^{2} - \nu^{2}(x_{k}^{z_{j}})}$ , but this is practically identical to the formula using the transverse momentum,  $x_{k}^{z_{j}} + (z_{j + 1} - z_{j})p(x_{k}^{z_{j}}) / mc$ . Note that although the weak measurement crystal is at a fixed position, the evolution of the effective wave function, described by Schrödinger's equation with the system of lenses acting as quadratic potentials, ensures that our method yields the weak value of transverse momentum at any desired  $z$  plane. Thus, as in (16), we rely upon knowledge of the Schrödinger evolution in this refocusing part of the apparatus, but note that we do not make use of any knowledge of the wave function itself in obtaining the Bohmian momenta and paths.

In the experiment, we consider 198 initial positions  $x_{i}(z_{1})$ , with 99 for each slit. The initial positions are chosen to equally sample the Gaussian distribution of  $|\psi(x)|^2$  across each slit (see Materials and Methods for details). The weak value of the transverse momentum at  $z_{117} = 8.612 \, \mathrm{m}$  is shown in Fig. 2A as a function of  $x$  and for both phases  $\phi$ . The relative phase difference of  $\pi$  yields the complementary pattern in momenta. Figure 2B shows the reconstructed trajectories beginning at the same place (two places are chosen:  $x = \pm 1.02 \, \mathrm{mm}$ ) for the two phases. For  $\phi = 0$ , the trajectories converge to form the zero-order fringe, while for  $\phi = \pi$ , they diverge toward the two first-order fringes.

Following all the trajectories, we can obtain the Bohmian momentum disturbance distribution  $P_{z_j}^{\phi}(p)$  and the mean absolute momentum disturbance  $\langle |p| \rangle_{z_j}^B$  at different planes  $z_j$  using Eqs. 2 and 4, respectively. The latter as a function of  $z$  is shown in Fig. 3A, with  $\eta^0 = \eta^\pi = 1/2$ . This shows that the momentum disturbance is not a momentum kick that occurs at the point of the WWM (15). Rather, it gradually accumulates during the propagation of the photons. This delayed Bohmian momentum disturbance is characteristic of a nonclassical momentum disturbance as defined in (11).

![](images/595ddcbc09c038d1775a6b341995382205d4dcdc75893a29c9f04cef7cd0a43c.jpg)  
Fig. 2. Experimental velocities and trajectories. (A) The weak value of the transverse velocities or momenta  $(v / c = \lambda p / h)$  at  $z_{117} = 8.612\mathrm{m}$ . The red squares and blue dots represent experimental data with the relative phase  $\phi$  being 0 and  $\pi$ , respectively. (B) Trajectories beginning at the same initial condition,  $x = \pm 1.02\mathrm{mm}$ , for  $\phi = 0$  (red) and  $\phi = \pi$  (blue). The trajectories are reconstructed from 117 imaging planes. If a trajectory locates on a point that is not at the center of a pixel, then a cubic spline interpolation between neighboring momentum values is used.

![](images/4e5ba5d2da666b2e4484476197181f168b6f59ec01b854a658b0d61c5d8050fb.jpg)

To further demonstrate the difference, Fig. 3B compares the total Bohmian momentum disturbance distribution  $P_{z_1}^{\phi}(p)$  at the last plane  $(z_{117} = 8.612\mathrm{m})$  with that at the first plane  $(z_{1} = 1.445\mathrm{m})$  (inset). The two peaks in  $P_{z_{117}}^{\pi}(p)$  at  $p \approx \pm 3\hbar /(2D)$  are the dominant contribution to the mean absolute Bohmian momentum disturbance. They are almost absent from  $P_{z_1}^{\pi}(p)$ , since in the near field, there has not been sufficient time for the wave function to develop the different phase gradients for the different  $\phi$  that guide the Bohmian photons. The lack of any immediate disturbance to the Bohmian momentum from our WWM reflects the fact that the moments of the far-field momentum distribution are unchanged by this type of WWM (15, 28, 29).

We also look at the trade-off between the mean absolute momentum disturbance  $\langle |p|\rangle_T^B$  and the visibility  $V$  by changing the relative weight of the cases of  $\phi = 0$  and  $\phi = \pi$ . This corresponds to WWMs with partial information, allowing a nonzero visibility  $V$  to remain. The results are shown in Fig. 4. The increase in the momentum disturbance as the visibility is reduced is observed and always exceeds the theoretical bound of inequality (5). The methods to estimate the fringe visibility  $V$  can be found in Materials and Methods.

For the WWM we implement, this bound should be achievable. However, this bound is calculated considering an infinite number of initial positions at the plane  $z = 0$ , whereas in our experiment, we have 198 initial positions at the plane  $z_{1} = 1.445 \mathrm{~m}$ . Thus, to compare with our experiment, we also calculate  $V$  and, in the framework of Bohmian mechanics,  $\langle |p| \rangle_{z_{117}}^{B}$ , but using the Gaussian approximation to the  $\delta$ -function to get  $P_{z_{117}}^{B}(p)$  and using the same experimental conditions (117 image planes from  $z_{1} = 1.445 \mathrm{~m}$  to  $z_{117} = 8.612 \mathrm{~m}$  with 198 initial

![](images/35dd05f26bfc8758ea46d5719fc43aa70d7a1291b720b5e2a1daa8145d93cb7a.jpg)

![](images/02a84ff4163ca02af3a4a280902bd59752785dea467ddc6ef809db245e337d47.jpg)  
Fig. 3. Bohmian momentum disturbance, in units of  $\hbar / D$ , for the photons subject to a minimally disturbing WWM with  $\eta^0 = \eta^\pi = 1/2$ . (A) The mean absolute momentum disturbance  $\langle |p| \rangle_z^B$  as a function of the propagation distance  $z$ . The nonclassicality of the momentum change is evident from the fact that it accrues gradually during propagation from near to far field. (B) Complete distribution of the Bohmian momentum disturbance at the last plane and the first plane (inset). Red is for  $\phi = 0$  and blue for  $\phi = \pi$ .

![](images/8f4e7a72b3d37fbbc9a2b4ab3fcf4a3f33e184b306ad545a22fd33562924bc59.jpg)  
Fig. 4. The relationship between the total mean absolute momentum disturbance  $\langle |\pmb{p}| \rangle_{\mathbf{z}}^{\mathbf{B}}$  (in units of  $h / D$ ) and fringe visibility  $\mathbf{V}$ . The blue dots represent the experimental data for various partial WWMs kinds of measurements in the plane  $z_{117} = 8.612 \, \mathrm{m}$ . The red solid line represents the theoretical prediction (5) under ideal conditions. The black dashed line represents the theoretical prediction, calculated with the same experimental conditions. Error bars are estimated from the counting statistics.

positions). The result is the black dashed line and now agrees well with the experimental results. In this case, there is a predicted nonzero total mean absolute momentum  $\langle |p|\rangle_z^B$  even for the case of no WWM ( $V = 1$ ). This simply reflects the SD ( $\sigma = 0.1\hbar /D$ ) of the Gaussian distribution, which we use to approximate the  $\delta$ -function when calculating the Bohmian momentum disturbance distribution.

# DISCUSSION

In this work, we used the Bohmian probability distribution (15) to experimentally quantify the momentum disturbance arising from a WWM, which destroys (or partially destroys) two-slit interference. In particular, we measured the mean of the absolute value of the Bohmian momentum disturbance  $\langle |p| \rangle_{z_j}^B$ . In the far field, the results we obtained are consistent with the theoretical inequality  $\langle |p| \rangle_T^B \geq (1 - V) 2\hbar / (\pi D)$ , where  $V$  is the remaining visibility when the WWM is only partial. We also show that  $\langle |p| \rangle_{z_j}^B$  in the near field is small and acquires its far-field value gradually as the photon travels longitudinally. This is characteristic (15) of a momentum disturbance, which is nonclassical (11, 30). It is not an artifact of the Bohmian picture with its nonlocal "quantum potential." For example, a WWM achieved by a phase change that increases linearly with transverse should give rise to a local momentum kick, taking place at the position of the WWM (15). This is a topic that could be addressed in future experiments.

Last, we note that there are other methods to characterize the momentum transfer (28, 29)—the latter having been realized experimentally (31)—which also reflect the difference between classical and nonclassical momentum disturbance. While the momentum disturbance distributions in these methods have the advantage of being independent of the basis used for reading out the WWM device, they are not true probability distributions: They take negative values for nonclassical cases. By contrast, in our experiment, we measured a family of true probability distributions, which quantitatively captured the relationship between momentum disturbance and fringe visibility and which also enabled us to show the nonclassicality of that disturbance quantitatively for the first time. Thus, treating the momentum as an element of reality in Bohmian mechanics arguably provides the most useful method to understand the change of photon's momentum in a WWM. Moreover, it gives an intuitive picture of part of the "uncontrollable change in the

momentum" (1), which enforces complementarity: Although Bohmian dynamics is fully deterministic, the momentum transfer experienced by a particle depends on its initial position within the wave function, and that cannot be controlled by the experimenter.

# MATERIALS AND METHODS

# The selection of initial transverse positions  $x_{i}(z_{1})$

The probability distributions of the signal photon in the up and down paths at  $z_{1}$  plane were represented as  $P_{u}(x) = |f_{u}(x)|^{2}$  and  $P_{d}(x) = |f_{d}(x)|^{2}$ , respectively. One hundred ninety-eight trajectories are reconstructed in the experiment, with 99 for each beam. The initial transverse positions  $x_{i}(z_{1})$  of each beam were chosen to satisfy  $A_{i} = \int_{-\infty}^{x_{i}(z_{1})}P_{u(d)}(x)dx = i / 100$  with  $i\in \{1,2\dots 99\}$ .

# Estimation of the interference visibility  $V$

The intensities detected in the ICCD camera are denoted as  $N_{k}^{0}(z_{j})$  and  $N_{k}^{\pi}(z_{j})$  at the position  $x_{k}$  at  $z_{j}$  plane for the relative phase being 0 and  $\pi$ , respectively. The probabilities of these two cases are denoted as  $\eta^{0}$  and  $\eta^{\pi}$ , respectively. The total intensity at  $z_{j}$  plane can be calculated as  $N_{k}(z_{j}) = \eta^{0}N_{k}^{0}(z_{j}) + \eta^{\pi}N_{k}^{\pi}(z_{j})$ , with  $\eta^{0} + \eta^{\pi} = 1$ . The minimum intensities of the first-order interference are denoted as  $N_{1}$  and  $N_{2}$ , respectively. The maximum intensity of the zero-order interference is denoted as  $N_{3}$ . The visibility  $V$  was then calculated as  $V = \frac{N_{3} - (N_{1} + N_{2}) / 2}{N_{3} + (N_{1} + N_{2}) / 2}$ .

For the comparison between experiment and theory (black dashed line in Fig. 4), the visibility was further theoretically estimated with the same experimental conditions in the framework of quantum theory. The intensity distribution was calculated as  $I = \eta^0 |\psi^0 (x_k^{z_j})|^2 +\eta^\pi |\psi^\pi (x_k^{z_j})|^2$ . The visibility  $V$  could then be obtained as  $V = (I_{\mathrm{max}} - I_{\mathrm{min}}) / (I_{\mathrm{max}} + I_{\mathrm{min}})$ , where  $I_{\mathrm{max}}$  and  $I_{\mathrm{min}}$  represent the zero-order maximum intensity and first-order minimum intensity, respectively.

# SUPPLEMENTARY MATERIALS

Supplementary material for this article is available at http://advances.sciencemag.org/cgi/ content/full/5/6/eaav9547/DC1

Section SI. Momentum in Bohmian mechanics and related theories

Section SII. Single photon generation

Fig. S1. Experimental setup for single-photon generation.

References (32-34)

# REFERENCES AND NOTES

1. W. Heisenberg, Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik. Z. Phys. 43, 172-198 (1927).  
2. N. Bohr, The quantum postulate and the recent development of atomic theory. Nature 121, 580-590 (1928).  
3. W. K. Wootters, W. H. Zurek, Complementarity in the double-slit experiment: Quantum nonseparability and a quantitative statement of Bohr's principle. Phys. Rev. D 19, 473-484 (1979).  
4. D. M. Greenberger, A. Yasin, Simultaneous wave and particle knowledge in a neutron interferometer. Phys. Lett. A 128, 391-394 (1988).  
5. G. Jaeger, A. Shimony, L. Vaidman, Two interferometric complementarities. Phys. Rev. A 51, 54-67 (1995).  
6. B.-G. Englert, Fringe visibility and which-way information: An inequality. Phys. Rev. Lett. 77, 2154-2157 (1996).  
7. M. O. Scully, B.-G. Englert, H. Walther, Quantum optical tests of complementarity. Nature 351, 111-116 (1991).  
8. P. Storey, S. M. Tan, M. Collett, D. F. Walls, Path detection and the uncertainty principle. Nature 367, 626-628 (1994).  
9. B.-G. Englert, M. O. Scully, H. Walther, Complementarity and uncertainty. Nature 375, 367-368 (1995).  
10. E. P. Storey, S. M. Tan, M. J. Collett, D. F. Walls, Complementarity and uncertainty. Nature 375, 368 (1995).

11. H. M. Wiseman, F. Harrison, Uncertainty over complementarity? Nature 377, 584 (1995).  
12. S. Durr, T. Nonn, G. Rempe, Origin of quantum-mechanical complementarity probed by a "which-way" experiment in an atom interferometer. Nature 395, 33-37 (1998).  
13. D. Bohm, A suggested interpretation of the quantum theory in terms of "hidden" variables. I. Phys. Rev. 85, 166-179 (1952).  
14. D. Bohm, A suggested interpretation of the quantum theory in terms of "hidden" variables. II. Phys. Rev. 85, 180-193 (1952).  
15. H. M. Wiseman, Bohmian analysis of momentum transfer in welcher Weg measurements. Phys. Rev. A 58, 1740-1756 (1998).  
16. S. Kocsis, B. Braverman, S. Ravets, M. J. Stevens, R. P. Mirin, L. K. Shalm, A. M. Steinberg, Observing the average trajectories of single photons in a two-slit interferometer. Science 332, 1170-1173 (2011).  
17. D. H. Mahler, L. Rozema, K. Fisher, L. Vermeyden, K. J. Resch, H. M. Wiseman, A. Steinberg, Experimental nonlocal and surreal Bohmian trajectories. Sci. Adv. 2, e1501466 (2016).  
18. Y. Xiao, Y. Kedem, J.-S. Xu, C.-F. Li, G.-C. Guo, Experimental nonlocal steering of Bohmian trajectories. Opt. Express 25, 14463-14472 (2017).  
19. H. M. Wiseman, Grounding Bohmian mechanics in weak values and Bayesianism. New J. Phys. 9, 165 (2007).  
20. D. Durr, S. Goldstein, N. Zanghi, On the weak measurement of velocity in Bohmian mechanics. J. Stat. Phys. 134, 1023-1032 (2009).  
21. Y. Aharonov, D. Z. Albert, L. Vaidman, How the result of a measurement of a component of the spin of a spin-1/2 particle can turn out to be 100. Phys. Rev. Lett. 60, 1351-1354 (1988).  
22. A. G. Kofman, S. Ashhab, F. Nori, Nonperturbative theory of weak pre- and post-selected measurements. Phys. Rep. 520, 43-133 (2012).  
23. J. Dressel, M. Malik, F. M. Miatto, A. N. Jordan, R. W. Boyd, *Colloquium: Understanding quantum weak values: Basics and applications.* Rev. Mod. Phys. **86**, 307–316 (2014).  
24. B. Tamir, E. Cohen, Introduction to weak measurements and weak values. Quanta 2, 7-17 (2013).  
25. Y. Aharonov, E. Cohen, A. C. Elitzur, Foundations and applications of weak quantum measurements. Phys. Rev. A 89, 052105 (2014).  
26. R. Flack, B. J. Hiley, Weak values of momentum of the electromagnetic field: average momentum flow lines, not photon trajectories. arXiv:1611.06510 (2016).  
27. M. O. Scully, K. Druhl, Quantum eraser: A proposed photon correlation experiment concerning observation and "delayed choice" in quantum mechanics. Phys. Rev. A 25, 2208-2213 (1982).

28. H. M. Wiseman, F. E. Harrison, M. J. Collett, S. M. Tan, D. F. Walls, R. B. Killip, Nonlocal momentum transfer in welcher Weg measurements. Phys. Rev. A 56, 55-75 (1997).  
29. H. M. Wiseman, Directly observing momentum transfer in twin-slit "which-way" experiments. Phys. Lett. A 311, 285-291 (2003).  
30. Y. Aharonov, H. Pendleton, A. Petersen, Modular variables in quantum theory. Int. J. Theor. Phys. 2, 213-230 (1969).  
31. R. Mir, J. S. Lundeen, M. W. Mitchell, A. M. Steinberg, J. L. Garretson, H. M. Wiseman, A double-slit 'which-way' experiment on the complementarity-uncertainty debate. New J. Phys. 9, 287 (2007).  
32. D. Durr, S. Goldstein, N. Zanghhi, Quantum Physics Without Quantum Philosophy (Springer, 2013).  
33. A. Valentini, On Galilean and Lorentz invariance in pilot-wave dynamics. Phys. Lett. A 228, 215-222 (1997).  
34. P. R. Holland, The Quantum Theory of Motion (Cambridge Univ. Press, 1993).

Acknowledgments: We thank A. Steinberg for the helpful discussion. Funding: This work was supported by the National Key Research and Development Program of China (grant nos. 2016YFA0302700 and 2017YFA0304100), the National Natural Science Foundation of China (grant nos. 61725504, 61327901, 11774335, and 11821404), Anhui Initiative in Quantum Information Technologies (grant nos. AHY060300 and AHY020100), the Key Research Program of Frontier Sciences, CAS (grant no. QYZDY-SSW-SLH003), and the Fundamental Research Funds for the Central Universities (grant nos. WK2470000020 and WK2470000026).

Competing interests: The authors declare that they have no competing interests. Author contributions: J.-S.X. and C.-F.L. designed the experiment with the discussion of Y.K. Y.X. performed the experiment. H.M.W. constructed the theoretical model and assisted Y.X. in analyzing the results. Y.X., H.M.W., and J.-S.X. wrote the manuscript. J.-S.X., C.-F.L., and G.-C.G. supervised the project. All authors read the paper and discussed the experimental results. Data and materials availability: All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Additional data related to this paper may be requested from the authors.

Submitted 5 November 2018

Accepted 10 May 2019

Published 14 June 2019

10.1126/sciadv.aav9547

Citation: Y. Xiao, H. M. Wiseman, J.-S. Xu, Y. Kedem, C.-F. Li, G.-C. Guo, Observing momentum disturbance in double-slit "which-way" measurements. Sci. Adv. 5, eaav9547 (2019).

# Science Advances

Observing momentum disturbance in double-slit "which-way" measurements

Ya Xiao, Howard M. Wiseman, Jin-Shi Xu, Yaron Kedem, Chuan-Feng Li and Guang-Can Guo

Sci Adv 5 (6), eaav9547.

DOI: 10.1126/sciadv.aav9547

# ARTICLE TOOLS

http://advances.sciencemag.org/content/5/6/eaav9547

# SUPPLEMENTARY MATERIALS

http://advances.sciencemag.org/content/suppl/2019/06/10/5.6.eaav9547.DC1

# REFERENCES

This article cites 31 articles, 2 of which you can access for free http://advances.sciencemag.org/content/5/6/eaav9547#BIBL

# PERMISSIONS

http://www.sciencemag.org/help/reprints-and-permissions

Use of this article is subject to the Terms of Service