# PHYSICAL SCIENCES

# Verifying Heisenberg's error-disturbance relation using a single trapped ion

Fei Zhou, $^{1*}$  Leilei Yan, $^{1,2*}$  Shijie Gong, $^{1,2*}$  Zhihao Ma, $^{3\dagger}$  Jiuzhou He, $^{1,2}$  Taiping Xiong, $^{1,2}$  Liang Chen, $^{1}$  Wanli Yang, $^{1}$  Mang Feng, $^{1,4\dagger}$  Vlatko Vedral $^{5,6,7,8\dagger}$

Heisenberg's uncertainty relations have played an essential role in quantum physics since its very beginning. The uncertainty relations in the modern quantum formalism have become a fundamental limitation on the joint measurements of general quantum mechanical observables, going much beyond the original discussion of the trade-off between knowing a particle's position and momentum. Recently, the uncertainty relations have generated a considerable amount of lively debate as a result of the new inequalities proposed as extensions of the original uncertainty relations. We report an experimental test of one of the new Heisenberg's uncertainty relations using a single  $^{40}\mathrm{Ca}^{+}$ ion trapped in a harmonic potential. By performing unitary operations under carrier transitions, we verify the uncertainty relation proposed by Busch, Lahti, and Werner (BLW) based on a general error-trade-off relation for joint measurements on two compatible observables. The positive operator-valued measure, required by the compatible observables, is constructed by single-qubit operations, and the lower bound of the uncertainty, as observed, is satisfied in a state-independent manner. Our results provide the first evidence confirming the BLW-formulated uncertainty at a single-spin level and will stimulate broad interests in various fields associated with quantum mechanics.

2016 © The Authors, some rights reserved; exclusive licensee American Association for the Advancement of Science. Distributed under a Creative Commons Attribution NonCommercial License 4.0 (CC BY-NC).

# INTRODUCTION

Heisenberg's uncertainty relation (1) is one of the cornerstones in understanding quantum mechanics. In most textbooks, the uncertainty relation is quantified by the standard deviations (SDs) of the measured variables, such as  $\Delta \hat{P}\Delta \hat{Q} \geq \hbar / 2$  (where  $\hbar$  is the Planck constant divided by  $2\pi$ ), with  $\Delta \hat{P}$  and  $\Delta \hat{Q}$  being the SDs of two noncommuting operators  $\hat{P}$  and  $\hat{Q}$ . This definition, which implies that the measurements of  $\hat{P}$  and  $\hat{Q}$  are performed on an ensemble of identically prepared quantum systems, describes a preparation uncertainty (2-4), which is actually different from the original spirit of Heisenberg's idea. A correct understanding of Heisenberg's uncertainty relation should be based on the observer's effect; that is, the accuracy of an approximate position measurement is related to the disturbance of the particle's momentum (1). This is a measurement uncertainty, also called the error-disturbance relation (EDR). For the above defined variables  $\hat{P}$  and  $\hat{Q}$ , which are not restricted to describing the position and momentum of a particle, Heisenberg's EDR, as strictly proven recently (5), is quantified as  $\epsilon (\hat{P})\xi (\hat{Q}) \geq \hbar / 2$ , where  $\epsilon (\hat{P})$  is the measurement error of the observable  $\hat{P}$ , and  $\xi (\hat{Q})$  is the disturbance magnitude of  $\hat{Q}$  induced by the measurement.

Both the preparation uncertainty and the measurement uncertainty (that is, EDR) have been debated for years and generalized to be  $\Delta \hat{P}\Delta Q\geq |\langle [\hat{P},\hat{Q} ]\rangle | / 2$  and  $\epsilon (\hat{P})\xi (\hat{Q})\geq |\langle [\hat{P},\hat{Q} ]\rangle | / 2$  , respectively. Although the former seems uncontroversial (6), which represents the fundamental limit on the measurement statistics for any state preparation, the latter was proven to be incorrect and can be violated experimentally

(7). Following this observation, there has been a considerable amount of lively debate on uncertainty relations as a result of the new inequalities for generalizing original ones (8-14). Ozawa (8, 9), Hall (11), and Branciard (12) independently derived new inequalities for the EDR, which were later experimentally verified with polarized neutrons (15, 16) and photons (17-22).

The EDR implies the impossibility of simultaneously measuring two noncommuting variables to arbitrary precision. That is, a simultaneous measurement, called joint measurement, of  $\hat{P}$  and  $\hat{Q}$  indicates the capability of measuring  $\hat{P}$  without disturbing  $\hat{Q}$ . Recently, Busch, Lahti, and Werner (BLW) have proposed an idea for joint measurements of qubits, by which a general error-trade-off relation is obtained as the uncertainty relation (23, 24). Because the joint measurement is available, one may approximate this joint measurement to the unavailable joint measurement of the other two operators, which follows the spirit of Heisenberg's original idea in 1927, as claimed in the BLW proposal. Specifically, two compatible observables  $\mathcal{C}$  and  $\mathcal{D}$  are defined by Busch et al. (23, 24), which are noncommuting but own common eigenvectors. Because they can be measured jointly,  $\mathcal{C}$  and  $\mathcal{D}$  are used to approximate two incompatible observables  $\mathcal{A}$  and  $\mathcal{B}$ . The BLW scheme aims to find combined approximation errors constrained by the incompatibility degree of the target observables  $\mathcal{A}$  and  $\mathcal{B}$  (See Fig. 1 for a conceptual understanding of the idea.). The combined approximation errors are considered as the worst-case estimate of the inaccuracy, which are defined in the BLW proposal as figures of merit characterizing the performance of the measuring device, rather than the disturbance induced by the measurement. Meanwhile, different from the definition given in previous studies (8, 9, 11, 12), the BLW error-trade-off relation can be state-independent and provides a more reasonable bound of the measurement precision.

# RESULTS

# The system and the scheme

We report experimental verification of Heisenberg's EDR by a single trapped  $^{40}\mathrm{Ca}^{+}$  ion, following the BLW proposal. The atomic ion is confined in a harmonic trap, that is, within the Lamb-Dicke regime of a

linear Paul trap, with an axial frequency of  $\omega_{\mathrm{z}} / 2\pi = 1.01$  MHz and a radial frequency of  $\omega_{\mathrm{r}} / 2\pi = 1.2$  MHz. We encode a qubit into two electronic levels  $|\downarrow\rangle \equiv |S_{1/2}, m_{\mathrm{J}} = +1/2\rangle$  and  $|\uparrow\rangle \equiv |D_{5/2}, m_{\mathrm{J}} = +3/2\rangle$ , where  $m_{\mathrm{J}}$  is the magnetic quantum number (see Fig. 2A). Doppler cooling and resolved-sideband cooling are performed mainly along the axial direction, yielding the final average phonon number  $\bar{n} < 0.1$  along the axial direction with the Lamb-Dicke parameter  $\eta \sim 0.09$ . Together with the optical pumping, the system is initially prepared in  $|\downarrow\rangle$ . We carry out the unitary rotations between the two encoded levels and implement projective measurement on  $|\uparrow\rangle$  by the electron shelving technique (see the Supplementary Materials).

Before presenting our experimental results, we first specify some important points in our experimental scheme. We consider the positive operators  $A_{\pm} = (I \pm \vec{a} \cdot \vec{\sigma}) / 2$  and  $B_{\pm} = (I \pm \vec{b} \cdot \vec{\sigma}) / 2$  regarding  $\mathcal{A}$  and  $\mathcal{B}$ , respectively, where  $\vec{a}$  and  $\vec{b}$  are unit vectors and  $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$  represents a vector associated with the usual Paul matrices. To be jointly measurable, the compatible observables  $\mathcal{C}$  and  $\mathcal{D}$ , as the approximation of  $\mathcal{A}$  and  $\mathcal{B}$ , own the positive operators  $C_{\pm} = (I \pm \vec{c} \cdot \vec{\sigma}) / 2$  and  $D_{\pm} =$

![](images/bbd9f67ac99e3734570278e44c8b1d3f977345c4113db984fced5ce6454a9228.jpg)  
Fig. 1. Conceptual understanding of the BLW scheme for testing Heisenberg's EDR. (A) Conceptual diagram of the BLW proposal. A joint measurement of compatible observables  $\mathcal{C}$  and  $\mathcal{D}$  is carried out as an approximation of the incompatible observables  $\mathcal{A}$  and  $\mathcal{B}$ , respectively. The Wasserstein distances  $\Delta (\mathcal{A},\mathcal{C})^2$  and  $\Delta (\mathcal{B},\mathcal{D})^2$  satisfy the error-trade-off relation. We emphasize that, in our experiment,  $\mathcal{C}$  and  $\mathcal{D}$  cannot be measured directly but can be obtained from the positive operator-valued measure (POVM) operator  $G$ , which is detected experimentally. (B) The Bloch vectors  $\mathbf{a}$ ,  $\mathbf{b}$ ,  $\mathbf{c}$ , and  $\mathbf{d}$ , corresponding to the observables  $\mathcal{A}$ ,  $\mathcal{B}$ ,  $\mathcal{C}$ , and  $\mathcal{D}$ , respectively, are plotted following the implementation steps in our experiment with  $\theta_{\mathrm{in}}$  defined in the text.

![](images/ae4ca9697e2306b097c1d7aaeb0a36090999e73a4873277392b6ff1403045a5e.jpg)  
B

$\left(I \pm \vec{d} \cdot \vec{\sigma}\right) / 2$ , which satisfy  $\| \vec{c} \| \leq 1$ ,  $\| \vec{d} \| \leq 1$ , and  $\| \vec{c} + \vec{d} \| + \| \vec{c} - \vec{d} \| \leq 2$ .

The essential step of our execution is the joint measurement  $G$  on the compatible observables  $\mathcal{C}$  and  $\mathcal{D}$ . In the study of Busch et al. (23),  $G$  is associated with the POVM operators  $G_{\pm, \pm}$  commonly owned by  $C_{\pm}$  and  $D_{\pm}$  with the marginality relation  $C_{\pm} = G_{\pm, +} + G_{\pm, -}$  and  $D_{\pm} = G_{+, \pm} + G_{-, \pm}$ . Generally speaking, the POVM can be achieved in a qubit with the assistance of another auxiliary qubit, implying the requirement of two qubits for implementing the operations. However, in our experiment, we construct the POVMs by single-qubit operations, and thus, the BLW scheme can be verified on a single qubit. To this end, the POVMs constructed are not general but satisfy the restricted condition

$$
\operatorname {r a n k} (G) \equiv 1 \tag {1}
$$

which means that only some special POVMs are achievable in the single-qubit system. The condition also implies that we have to involve a prefactor  $\mathrm{Tr}[G]$  in the measurement of the POVM operator. Besides, in our ion trap system, the projective measurement is performed on  $|\uparrow \rangle$ . Thus, we have to first rotate the POVMs unitarily to be in line with  $|\uparrow \rangle$  before making the measurements.

In a single-qubit system, for each POVM element operator  $G_{\mu,\nu} (\mu,\nu=\pm)$  applied on a density operator  $\rho$ , the measurement result  $p_{\rho}(G_{\mu,\nu})$  and the normalized density operator  $\mathcal{K}_{\rho}(G_{\mu,\nu})$  correspond, respectively, to  $p_{\rho}(G_{\mu,\nu}) = \mathrm{Tr}[G_{\mu,\nu}\rho]$  and  $\mathcal{K}_{\rho}(G_{\mu,\nu}) = \sqrt{G_{\mu,\nu}}\rho\sqrt{G_{\mu,\nu}} /p_{\rho}(G_{\mu,\nu})$  with  $\Sigma_{\mu,\nu}G_{\mu,\nu} = 1$ . To simplify the description below, we rewrite  $G_{\mu,\nu}$  as  $G$  by neglecting the subscripts  $\mu$  and  $\nu$ . Defining a pure-state measurement basis  $|\varphi\rangle$ , we obtain a measurement  $M$  along the same direction as  $|\varphi\rangle$  satisfying  $M \equiv \mathrm{Tr}[M]|\varphi\rangle\langle\varphi|$  and  $\mathrm{Tr}[M] = \mathrm{Tr}[G]$ . If there is a unitary operation  $U$  mapping  $G$  to  $M$  with  $M = UGU^{\dagger}$ , the density operator changes accordingly as  $\rho' = U\rho U^{\dagger}$ . Therefore, we reach important relations as below

$$
p _ {\rho} (G) = \operatorname {T r} [ G ] p _ {\rho^ {\prime}} (| \varphi \rangle \langle \varphi |)
$$

$$
\mathcal {K} _ {\mathfrak {p}} (G) = U ^ {\dagger} \mathcal {K} _ {\mathfrak {p} ^ {\prime}} \left( \right.\left| \right. \varphi \left. \right\rangle \langle \varphi \left. \right|\left. \right) U
$$

which are one-by-one mappings between the POVM and the projective measurement on  $|\varphi \rangle$ . Because no unitary transformation changes the

![](images/c2abc0185b2a01445fa92255c510ff38e68ae9028d7aa9c6e1bb30e409d61bd0.jpg)

![](images/2f4ec7b82a782fcaec7b61931f66792b7f4ca02d6737d5ae317bc26f3479d237.jpg)  
Fig. 2. A single trapped ion manipulated for testing Heisenberg's EDR. (A) Relevant levels of the  $^{40}\mathrm{Ca}^+$  ion and transitions. We encode the qubit in  $|S_{1/2}, m_J = +1/2\rangle$  and  $|D_{5/2}, m_J = +3/2\rangle$  and denote them by  $|\downarrow\rangle$  and  $|\uparrow\rangle$ , respectively. A narrow-line width 729-nm laser couples the two encoded states under carrier transitions. We monitor fluorescence due to spontaneous decay from  $4P_{1/2}$  for qubit readout. (B) Experimental implementation steps and the corresponding states of the system in Bloch sphere. The ion is first laser-cooled close to the vibrational ground state. The experiment starts from the qubit state of  $|\downarrow\rangle$  and evolves to  $|\varphi\rangle$  under the preparation pulse  $U_C(\theta_1, \phi_1)$ , with  $\theta_1 = \arcsin\left[\frac{(1 - \alpha)}{\sqrt{(1 - \alpha)^2 + (1 - \beta)^2}}\right]$  and  $\phi_1 = 0$ . Then, the measurement of the expectation of the observables  $A, B$ , and  $G$  is performed by the measurement pulse  $U_C(0_2, \phi_2)$  (see Table 1 for values), followed by the detection on  $|\uparrow\rangle$ .

rank of an operator, the POVM operator  $G$  can be achieved by a pure-state-relevant positive operator, strictly obeying the condition in Eq. 1.

In our case with a single qubit consisting of the upper level  $|\uparrow \rangle$  and the lower level  $|\downarrow \rangle$ , we assume that  $G = g_{0}I + \vec{g}\cdot \vec{\sigma}$ . Provided that  $\| \vec{g}\|^2 = g_0^2$  is satisfied and the ranks of all the POVM operators are units, the operators can be directly measured by combining a unitary operation and a projective measurement on  $|\uparrow \rangle$ . In addition, the marginality relations between  $G_{\pm ,\pm}$  and  $C_{\pm}$ ,  $D_{\pm}$  imply that the condition of  $\| \vec{g}\|^2 = g_0^2$  is equivalent to  $\| \vec{c} +\vec{d}\| +\| \vec{c} -\vec{d}\| = 2$ , that is,  $1 + \vec{c}\cdot \vec{d} = \| \vec{c} +\vec{d}\|$  and  $1 - \vec{c}\cdot \vec{d} = \| \vec{c} -\vec{d}\|$ , under which finding optimal approximations to  $\mathcal{A}$  and  $\mathcal{B}$  are always available (see the Supplementary Materials). In the trapped ion system, the unitary operators under the government of carrier transitions are accomplished by tuning the evolution time and the laser phase as explained in Fig. 2B. Thus, we obtain the Wasserstein distances (23) between  $\mathcal{A}$ ,  $\mathcal{C}$  and  $\mathcal{B}$ ,  $\mathcal{D}$ , in association with Heisenberg's EDR. Then, we examine the maximal uncertainty for various states of the system and different choices of  $\mathcal{C}$  and  $\mathcal{D}$ .

In our implementation, we consider  $\mathcal{A} = \sigma_y$  with  $A_{\pm} = (I\pm \sigma_y) / 2$  and  $\mathcal{B} = \sigma_z$  with  $B_{\pm} = (I\pm \sigma_z) / 2$ . As the approximation of  $\mathcal{A}$  and  $\mathcal{B}$ , the two compatible observables  $\mathcal{C}$  and  $\mathcal{D}$  can be set as  $C_{\pm} = (I\pm \alpha \sigma_y) / 2$  and  $D_{\pm} = (I\pm \beta \sigma_z) / 2$ , where  $\alpha^2 +\beta^2 = 1$  is satisfied as a result of the requirement for unit rank of the POVMs. In our case,  $C_{\pm}$  and  $D_{\pm}$  are not directly measurable but are obtained from the POVM operators  $G_{+, \pm} = [I + \alpha \sigma_y \pm \beta \sigma_z] / 4$  and  $G_{-, \pm} = [I - \alpha \sigma_y \pm \beta \sigma_z] / 4$ . As clarified below, by using the carrier transition and then making projective measurements on  $|\uparrow\rangle$ , we can achieve measurements of the observables  $A_{\pm}, B_{\pm}$ , and  $G_{\pm, \pm}$ .

In the operations presented below, we define  $\alpha = \sin (\theta_{\mathrm{in}})$  and  $\beta = \cos (\theta_{\mathrm{in}})$  (Fig. 1B). For a state  $\rho$ , the error measure (23, 25) between  $\mathcal{A}$  and  $\mathcal{C}$  is estimated by the Wasserstein distance  $\Delta_{\rho}(\mathcal{A},\mathcal{C})^2$  (see Materials and Methods), and similarly, we have  $\Delta_{\rho}(\mathcal{B},\mathcal{D})^2$  for the difference between  $\mathcal{B}$  and  $\mathcal{D}$ . Heisenberg's EDR for the pair of incompatible observables is determined by maximizing the summation of the two Wasserstein distances over all the possible states of the system with

$$
\begin{array}{l} \Delta (\mathcal {A}, \mathcal {B}) 2 := \max  _ {\rho} \left[ \Delta_ {\rho} (\mathcal {A}, \mathcal {C}) ^ {2} + \Delta_ {\rho} (\mathcal {B}, \mathcal {D}) ^ {2} \right] \\ = 2 \sqrt {(1 - \alpha) ^ {2} + (1 - \beta) ^ {2}} \geq 2 (\sqrt {2} - 1) \tag {2} \\ \end{array}
$$

where the second equality holds when the system is prepared in  $|\varphi\rangle = \cos(\theta_1/2)|\downarrow\rangle - i\sin(\theta_1/2)e^{i\phi_1}|\uparrow\rangle$ , with  $\theta_1$  and  $\phi_1$  defined in Fig. 2B, and the state-independent lower bound  $\Delta_{\mathrm{bl}}(A, B)^2 \coloneqq 2\left(\sqrt{2} - 1\right)$  of the uncertainty is reached at  $\alpha = \beta = 1/\sqrt{2}$ . Equation 2 represents a worst-case estimate of the inaccuracy applicable to all possible states.

# Experimental observation

Under the rotating-wave approximation (see the Supplementary Materials), the Hamiltonian of our case in units of  $\hbar = 1$  is given by  $H_{\mathrm{C}} = \Omega (\sigma_{+}e^{i\phi} + \sigma_{-}e^{-i\phi}) / 2$  (26), where  $\Omega$  is the Rabi frequency representing the laser-ion coupling strength,  $\sigma_{\pm}$  are the usual Pauli operators, and  $\phi$  is the laser phase. As shown in Fig. 2B, the experiment starts from the state  $|\downarrow \rangle$ , and the system evolves under  $U_{\mathrm{C}}(\theta ,\phi)$ , that is,

$$
U _ {\mathrm {C}} (\theta , \phi) = \cos (\theta / 2) I - i \sin (\theta / 2) \left(\sigma_ {x} \cos \phi - \sigma_ {y} \sin \phi\right) \tag {3}
$$

with  $\theta = \Omega t$  determined by the evolution time.

Table 1. Scheme for the measurement pulses in experimental observation of the inaccuracy of the error-trade-off relation for  $\mathcal{A} = \sigma_y$  and  $\mathcal{B} = \sigma_z$ .  

<table><tr><td></td><td>A+</td><td>A-</td><td>B+</td><td>B-</td><td>G+,+</td><td>G+,−</td><td>G−,+</td><td>G−,−</td></tr><tr><td>θ2</td><td>π/2</td><td>π/2</td><td>0</td><td>π</td><td>2 arcs</td><td>2 arcs</td><td>2 arcs</td><td>2 arcs</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>(√1+β)/2</td><td>(√1-β)/2</td><td>(√1+β)/2</td><td>(√1-β)/2</td></tr><tr><td>φ2</td><td>0</td><td>π</td><td>0</td><td>0</td><td>0</td><td>0</td><td>π</td><td>π</td></tr></table>

To verify Heisenberg's EDR, we vary  $\alpha$  and  $\beta$  to reach the maximal Wasserstein distance as in Eq. 2. The first step is to prepare the state  $|\phi\rangle$ . We fix the laser phase  $\phi_1$  and steer the system under  $U_{\mathrm{C}}(\theta_1,\phi_1)$  toward  $|\varphi\rangle$ , which is tuned with the change of  $\alpha$  and  $\beta$  for an optimal value corresponding to the worst-case estimate of inaccuracy. The operation is executed by a 729-nm laser coupling  $|\uparrow\rangle$  and  $|\downarrow\rangle$  for 2 to 3  $\mu$ s (see details in the Supplementary Materials). The second step is to measure the necessary observables  $A_{\pm}, B_{\pm}$ , and  $G_{\pm,\pm}$ , which is achieved by another evolution under  $U_{\mathrm{C}}(\theta_2,\phi_2)$  and then a detection on the state  $|\uparrow\rangle$ . To this end, we first drive the  $|\downarrow\rangle \leftrightarrow |\uparrow\rangle$  transition by the 729-nm laser following the scheme in Table 1. Detection is then made by reapplying the cooling lasers and counting the emitted photons for 4 ms by the photomultiplier tube.

A faithful observation requires a clear understanding of the operational imperfections. From an effective period of Rabi oscillation, we estimate the error of the initial-state preparation to be  $3(1)\%$  and the imperfection in the detection to be  $0.35(2)\%$  (the numbers in parentheses are the SEM). The radial thermal phonons cause a dephasing-like behavior that yields an accumulative deviation in the evolution. All these errors are experimentally determined, and the induced deviation can be corrected. Hence, the Rabi oscillation under a  $\pi / 2$  pulse of  $U_{\mathrm{C}}$  can reach a fidelity of  $99.8(1)\%$  (see the Supplementary Materials), and thus, the observed data of  $A$ ,  $B$ ,  $C$ , and  $D$  demonstrate an excellent agreement with the theoretical prediction. Errors, reflecting the fluctuation due to unstable laser power and magnetic field, are calculated and included in the SD.

Typical experimental data sets of  $\langle A_{\pm}\rangle, \langle B_{\pm}\rangle, \langle C_{\pm}\rangle$ , and  $\langle D_{\pm}\rangle$  are depicted in Fig. 3, which clearly demonstrate no possibility of good approximations of  $\mathcal{C}$  to  $\mathcal{A}$  and  $\mathcal{D}$  to  $\mathcal{B}$ , simultaneously. Provided  $\theta_{\mathrm{in}} \to \pi/2$ , we have  $\mathcal{C} \to \sigma_y$ , indicating the nearly perfect case for  $\mathcal{C}$  approaching  $\mathcal{A}$ . However, in this case, we have  $\mathcal{D} \to I/2$ , implying that we cannot obtain any information about  $\mathcal{B}$ . With  $\theta_{\mathrm{in}}$  away from  $\pi/2$ ,  $\mathcal{D}$  approaches  $\mathcal{B}$ , and meanwhile,  $\mathcal{C}$  turns out to be much different from  $\mathcal{A}$ . The sum of their differences, reflecting the balance between the two differences, reaches the minimum at  $\theta_{\mathrm{in}} = \pi/4$  (see the inset of Fig. 4).

The error-trade-off relation is witnessed in Fig. 4 by the Wasserstein distances  $\Delta (\mathcal{A},\mathcal{C})^2$  and  $\Delta (\mathcal{B},\mathcal{D})^2$ , which are calculated by the experimental data in Fig. 3. The observation fits the theoretical prediction "when one is more precisely measured, the other is more disturbed" very well. One cannot predict both outcomes of two incompatible measurements to arbitrary precision. Because it results from the maximal Wasserstein distances over all the possible states in the system, the observed error-trade-off relation represents the state-independent inaccuracy and reflects the essence of Heisenberg's EDR.

![](images/e4d94f6ae010a5903eb3772fc384c402eaaff5031cf5864913ef093ed62a8ecb.jpg)

![](images/f339a1d2102c3c6152e2c0bef46040bdb55e865795a5416c7dfd7867eb0585f8.jpg)  
Fig. 3. Experimental observation of the inaccuracy of the error-trade-off relation for  $\mathcal{A} = \sigma_y$  and  $\mathcal{B} = \sigma_z$ . (A and B) Experimental values of measuring the positive operators of  $\mathcal{A}$ ,  $\mathcal{B}$ ,  $\mathcal{C}$ , and  $\mathcal{D}$  versus  $\theta_{\mathrm{in}}$ ,  $\langle A_{\pm}\rangle$ ,  $\langle B_{\pm}\rangle$ , and  $\langle G_{\pm, \pm}\rangle$  are directly measured regarding  $\theta_2$  and  $\phi_2$  given in Table 1, whereas  $\langle C_{\pm}\rangle$  and  $\langle D_{\pm}\rangle$  are obtained from  $\langle G_{\pm, \pm}\rangle$  by the marginality relation. The curves represent the results of theoretical prediction. The error bars indicate SD containing the statistical errors of 40,000 measurements for each data point as well as the errors from unstable laser power and fluctuating magnetic field.

Because  $\mathcal{A}$  and  $\mathcal{B}$  in our case are maximally incompatible, the lower bound of the uncertainty can reach  $2\left(\sqrt{2} - 1\right)$ , the minimum in Eq. 2. We plot this lower bound in Fig. 4 by the dashed line tangent to the state-independent curve of the error-trade-off relation. The tangent point implies  $\alpha = \beta = 1 / \sqrt{2}$ . It is worth noting that the error bars, which dominantly resulted from the statistical deviation (due to quantum projection noise), represent the largest valid range of the experimental observation, rather than the true values allowed to be below the theoretically predicted lower bound of the uncertainty. Besides, the error bars here are four times as long as those in Fig. 3, reflecting the maximum possible deviation of statistics in measuring four variables (see Materials and Methods). More measurements can shrink the error bars but could not present new physics with respect to the 40,000 measurements performed here. Moreover, by fixing  $\alpha$  and  $\beta$ , but varying the state  $|\varphi\rangle$ , we can obtain tangent curves below the state-independent curve, which represent the error-trade-off relation with the state dependence. This example, with  $\alpha = \beta = 1 / \sqrt{2}$ , is illustrated in the Supplementary Materials. Furthermore, extending our implementation to other Pauli operators, for example,  $\mathcal{A} = \sigma_x$  and  $\mathcal{B} = \sigma_z$ , is straightforward and will result in the same EDR as simply verified in Fig. 5. For this case, we performed operations for optimal state preparation and measurement largely different from those for  $\mathcal{A} = \sigma_y$  and  $\mathcal{B} = \sigma_z$  (see the Supplementary Materials) but obtained similar EDRs. The similarity indicates the universality of Heisenberg's uncertainty relation.

![](images/ac1a450f768775bc09f3b22e1114e529c28b7eb0076cd163c5913835069a00da.jpg)  
Fig. 4. Experimental observation of the inaccuracy of the error-trade-off relation for  $\mathcal{A} = \sigma_y$  and  $\mathcal{B} = \sigma_z$ . The experimental data (filled squares) are determined by the data in Fig. 3. The solid curve represents the theoretically predicted results of  $\Delta(A, C)^2$  and  $\Delta(B, D)^2$ . The dashed line is plotted for the lower bound  $\Delta_{\mathrm{bl}}(\mathcal{A}, \mathcal{B})^2$  of the uncertainty in theoretical prediction. The inset shows the inaccuracy in variation of  $\theta_{\mathrm{in}}$ . The error bars indicate SD containing the statistical errors of 40,000 measurements for each data point as well as the errors from unstable laser power and fluctuating magnetic field.

# DISCUSSION

Because modern technology has been progressing steadily toward the exploration of much smaller objects, our operations, particularly measurements, confront the ultimate quantum limits. As a result, Heisenberg's uncertainty relation not only bounds the accuracy of the operations available with current laboratory techniques but also helps in understanding the very foundations of quantum mechanics. In quantum information science, the uncertainty relations have already been used to prove the security of quantum key distribution (27) and to explore the influence from quantum memory (28). In this context, the use of information-theoretic definitions, for example, entropic uncertainty relations (29) in terms of information, to quantify the limited information gained on each observable might bring new insights into quantum information theory. On the other hand, more in-depth research on the uncertainty relation may also bring new insights into the foundations of quantum theory, such as a deeper understanding of nonlocality (30, 31).

We note that the BLW idea has stimulated broad interests in further exploring error-trade-off relations, such as the optimal joint measurement in a geometric manner (32) and possible joint measurement for arbitrary observables of finite dimensional systems (33). Because the inequality, as the inaccuracy in the error-trade-off relation, is physically more specific than the measurement uncertainty or the preparation uncertainty, the BLW idea can be readily applied to further checking the security of quantum key distribution and the nonlocality. In addition, the inequality in the BLW scheme is different from other uncertainty relations (8-14). As a result, applying the BLW idea to quantum information science as done for other inequalities, for example, in the studies of Watanabe and Sagawa (34) and Dressel and Nori (34, 35), will help in scrutinizing the lowest bound among various uncertainty relations, which might optimize the available information gained on each qubit.

Our demonstration by a single ultracold trapped ion system is the first evidence to confirm the BLW-formulated error-trade-off relation in a pure quantum system. This is also an essential step toward

![](images/603e9124ab67d9358bff28c9c5dc48bef8e157cc5734bd3bab11c3bdc0bab3e0.jpg)  
Fig. 5. Experimental observation of the inaccuracy of the error-trade-off relation for  $\mathcal{A} = \sigma_x$  and  $\mathcal{B} = \sigma_z$ . The filled squares and the solid curve represent experimental data and theoretically predicted results of  $\Delta (A,C)^2 +\Delta (B,D)^2$ , respectively. The dashed line is plotted for the lower bound. The error bars indicate SD containing the statistical errors of 40,000 measurements for each data point as well as the errors from unstable laser power and fluctuating magnetic field.

understanding fundamental uncertainties of quantum mechanical variables, the prerequisite of exploring limits of ultraprecision measurements. Our experimental scheme is readily applicable to other trapped ion species and single-spin systems for quantum information purposes. The idea of achieving POVMs in a single-ion system will be applied to other quantum tasks, such as accurately testing the inequalities in previous studies (32, 33) at the single-qubit level.

# MATERIALS AND METHODS

# Operation details

In our experiment, we demonstrated variation of the observables with respect to  $\alpha$  and  $\beta$ . Our operations included steering toward the state  $|\varphi\rangle$  by  $U_{\mathrm{C}}(\theta_1,\phi_1)$  and realizing the observables by  $U_{\mathrm{C}}(\theta_2,\phi_2)$ , followed by the detection on the state  $|\uparrow\rangle$ . The step can be mathematically written as

$$
\langle K _ {\pm} \rangle = \operatorname {T r} \left[ K _ {\pm} \right] \cdot \langle \uparrow | U | \downarrow \rangle \langle \downarrow | U ^ {\dagger} | \uparrow \rangle \tag {4}
$$

where  $U = U_{\mathrm{C}}(\theta_2,\phi_2)U_{\mathrm{C}}(\theta_1,\phi_1)$  and  $K = A,B,G$

The trace distance for a pair of observables  $E$  and  $F$ , with  $E_{+} = (e_0I + \vec{e}\cdot \vec{\sigma}) / 2$  ( $E_{-} = I - E_{+}$ ) and  $F_{+} = (f_{0}I + \vec{f}\cdot \vec{\sigma}) / 2$  ( $F_{-} = I - F_{+}$ ) applied on the state  $\rho = (I + \vec{r}\cdot \vec{\sigma}) / 2$ , is given by

$$
\Delta_ {p} (E, F) ^ {2} := 2 \sum_ {i = \pm} \left| p _ {i} ^ {E} - p _ {i} ^ {F} \right| = 2 \left| e _ {0} - f _ {0} + \vec {r} \cdot (\vec {e} - \vec {f}) \right| \tag {5}
$$

where  $p_i^{\mathcal{I}} = \mathrm{Tr}[\rho J_i](J = E,F)$  is the probability distribution. In the qubit case, the trace distance was actually the Wasserstein distance defined in Busch et al. (23) for inaccuracies. Equation 5 shows that the SD of the trace distance was four times that of the  $p_i$  observed.

In our case,  $\Delta_{\mathfrak{p}}(\mathcal{A},\mathcal{C})^2 = 2(1 - \alpha)\bigl |r_y\bigr |$  and  $\Delta_{\mathfrak{p}}(\mathcal{B},\mathcal{D})^{2} = 2(1-\beta)|r_z|$ , where  $r_y = \sin \theta_1\cos \phi_1$  and  $r_z = -\cos \theta_1$  (see the Supplementary Materials). The probability distribution for the observables in the main

text can be measured as in Eq. 4. Heisenberg's EDR is  $\Delta (\mathcal{A},\mathcal{B})^2 \coloneqq \max_{\mathsf{p}}\left[\Delta_{\mathsf{p}}(\mathcal{A},\mathcal{C})^2 +\Delta_{\mathsf{p}}(\mathcal{B},\mathcal{D})^2\right]$ , where the maximum is reached by a state  $|\varphi \rangle$  prepared at  $\theta_{1} = \arcsin \left[(1 - \alpha) / \sqrt{(1 - \alpha)^{2} + (1 - \beta)^{2}}\right]$  and  $\phi_1 = 0$ . Here, we have to mention that the  $\Delta (\mathcal{A},\mathcal{B})^2$  we defined was slightly different from that in Busch et al. (23), which used the summation of the respective maximum of  $\Delta_{\mathfrak{p}}(\mathcal{A},\mathcal{C})^2$  and  $\Delta_{\mathfrak{p}}(\mathcal{B},\mathcal{D})^2$ . We preferred to work with our formulation because of the convenience in experimental implementation.

# Numerical treatments

Numerical simulation was performed to fit the experimental observation and assess the imperfection of experimental execution. The main deviations in our experiment came from two aspects: thermal phonons from the radial direction yielding offsets of Rabi oscillations and imperfection in qubit detection. For the former, an effective mean deviation at different moments could be estimated by means of a fitting method (36, 37). This kind of mean deviation is nearly constant and thus easily corrected. The detection error yielded a mean deviation of  $0.35(2)\%$  and could be calibrated by a practical method (38). The statistical error in our experiment was calculated by the Monte Carlo simulation with a peak value of 0.025. The decay and dephasing times of the qubit were 1.1 s and 2 ms, respectively, whose detrimental effects were negligible during the short periods  $(\sim 8\mu s)$  of our operations. Other possible imperfections could also lead to small errors, such as fluctuations of AC Stack shift due to power instability of the 729-nm laser and the fluctuating magnetic field, which were assessed to be less than  $2\%$  from the Rabi oscillation and included in the SD represented by the error bars.

# SUPPLEMENTARY MATERIALS

Supplementary material for this article is available at http://advances.sciencemag.org/cgi/ content/full/2/10/e1600578/DC1  
section S1. The error-trade-off relation and the joint measurements.  
section S2. Realization of observables in a single trapped ion system.  
section S3. The experimental setup and operations in our system.  
section S4. Imperfections in our experiment.  
section S5. Experimental implementation of incompatible observables  $\mathcal{A} = \sigma_y$  and  $\mathcal{B} = \sigma_z$ . section S6. For other pairs of variables.  
fig. S1. The experimental setup and level scheme.  
fig. S2. The sideband absorption spectra.  
fig. S3. The Rabi oscillation and the deviation.  
fig. S4. Tomography of the superposed state  $(|\downarrow\rangle - i|\uparrow\rangle) / \sqrt{2}$ .  
fig. S5. Experimental values in the state-dependent situation measuring the positive operators.  
fig. S6. Experimental observation of the state-dependent error-trade-off relation for  $\sigma_y$  and  $\sigma_z$ .  
fig. S7. Experimental values in the state-independent situation measuring the positive operators.  
table S1. Operation steps in our experiment for the state-dependent error-trade-off relation.  
table S2. Operation steps in our experiment for the state-independent error-trade-off relation.

# REFERENCES AND NOTES

1. W. Heisenberg, Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik. Z. Phys. 43, 172-198 (1927).  
2. E. H. Kennard, Zur Quantenmechanik einfacher Bewegungstypen. Z. Phys. 44, 326-352 (1927).  
3. H. Weyl, Gruppentheorie und Quantenmechanik (The University of California, 1928), 288 pp.  
4. H. Robertson, The uncertainty principle. Phys. Rev. 34, 163-164 (1929).  
5. P. Busch, P. Lahti, R. F. Werner, Proof of Heisenber's error-disturbance relation. Phys. Rev. Lett. 111, 160405 (2013).  
6. O. Nairz, M. Arndt, A. Zeilinger, Experimental verification of the Heisenberg uncertainty principle for fullerene molecules. Phys. Rev. A 65, 032109 (2002).  
7. L. E. Ballentine, The statistical interpretation of quantum mechanics. Rev. Mod. Phys. 42, 358-381 (1970).

8. M. Ozawa, Universally valid reformulation of the Heisenberg uncertainty principle on noise and disturbance in measurement. Phys. Rev. A 67, 042105 (2003).  
9. M. Ozawa, Uncertainty relations for joint measurements of noncommuting observables. Phys. Lett. A 320, 367-374 (2004).  
10. M. Ozawa, Uncertainty relations for noise and disturbance in generalized quantum measurements. Ann. Phys. 311, 350-416 (2004).  
11. M. J. W. Hall, Prior information: How to circumvent the standard joint-measurement uncertainty relation. Phys. Rev. A 69, 052113 (2004).  
12. C. Branciard, Error-tradeoff and error-disturbance relations for incompatible quantum measurements. Proc. Natl. Acad. Sci. U.S.A. 110, 6742-6747 (2013).  
13. A. Di Lorenzo, Sequential measurement of conjugate variables as an alternative quantum state tomography. Phys. Rev. Lett. 110, 010404 (2013).  
14. K. Fujikawa, Universally valid Heisenberg uncertainty relation. Phys. Rev. A 85, 062117 (2012).  
15. J. Erhart, S. Sponar, G. Sulyok, G. Badurek, M. Ozawa, Y. Hasegawa, Experimental demonstration of a universally valid error-disturbance uncertainty relation in spin measurements. Nat. Phys. 8, 185-189 (2012).  
16. G. Sulyok, S. Sponar, J. Erhart, G. Badurek, M. Ozawa, Y. Hasegawa, Violation of Heisenberg's error-disturbance uncertainty relation in neutron-spin measurements. Phys. Rev. A 88, 022110 (2013).  
17. M. Ringbauer, D. N. Biggerstaff, M. A. Broome, A. Fedrizzi, C. Branciard, A. G. White, Experimental joint quantum measurements with minimum uncertainty. Phys. Rev. Lett. 112, 020401 (2014).  
18. F. Kaneda, S.-Y. Baek, M. Ozawa, K. Edamatsu, Experimental test of error-disturbance uncertainty relations by weak measurement. Phys. Rev. Lett. 112, 020402 (2014).  
19. L. A. Rozema, A. Darabi, D. H. Mahler, A. Hayat, Y. Soudagar, A. M. Steinberg, Violation of Heisenberg's measurement-disturbance relationship by weak measurements. Phys. Rev. Lett. 109, 100404 (2012).  
20. A. P. Lund, H. M. Wiseman, Measuring measurement-disturbance relationships with weak values. New J. Phys. 12, 093011 (2010).  
21. S.-Y. Baek, F. Kaneda, M. Ozawa, K. Edamatsu, Experimental violation and reformulation of the Heisenberg's error-disturbance uncertainty relation. Sci. Rep. 3, 2221 (2013).  
22. M. M. Weston, M. J. W. Hall, M. S. Palsson, H. M. Wiseman, G. J. Pryde, Experimental test of universal complementarity relations. Phys. Rev. Lett. 110, 220402 (2013).  
23. P. Busch, P. Lahti, R. F. Werner, Heisenberg uncertainty for qubit measurements. Phys. Rev. A 89, 012129 (2014).  
24. P. Busch, P. Lahti, R. F. Werner, Colloquium: Quantum root-mean-square error and measurement uncertainty relations. Rev. Mod. Phys. 86, 1261-1281 (2014).  
25. C. Vilani, Optimal Transport: Old and New (Springer-Verlag, 2009), 976 pp.  
26. D. Leibfried, R. Blatt, C. Monroe, D. J. Wineland, Quantum dynamics of single trapped ions. Rev. Mod. Phys. 75, 281-324 (2003).  
27. M. Koashi, Unconditional security of quantum key distribution and the uncertainty principle. J. Phys. Conf. Ser. 36, 98-102 (2006).  
28. M. Berta, M. Christandl, R. Colbeck, J. M. Renes, R. Renner, The uncertainty principle in the presence of quantum memory. Nat. Phys. 6, 659-662 (2010).

29. S. Wehner, A. Winter, Entropic uncertainty relations—A survey. New J. Phys. 12, 025009 (2010).  
30. J. Oppenheim, S. Wehner, The uncertainty principle determines the nonlocality of quantum mechanics. Science 330, 1072-1074 (2010).  
31. M. Tomamichel, E. Hanggi, The link between entropic uncertainty and nonlocality. J. Phys. A Math. Theor. 46, 055301 (2013).  
32. S. Yu, C. H. Oh, Optimal joint measurement of two observables of a qubit. arXiv:1402.3785 (2014).  
33. J. M. Renes, V. B. Scholz, Operationally-motivated uncertainty relations for joint measurability and the error-disturbance tradeoff. arXiv:1402.6711 (2014).  
34. Y. Watanabe, T. Sagawa, M. Ueda, Uncertainty relation revisited from quantum estimation theory. Phys. Rev. A 84, 042121 (2011).  
35. J. Dressel, F. Nori, Certainty in Heisenberg's uncertainty principle: Revisiting definitions for estimation errors and disturbance. Phys. Rev. A 89, 022106 (2014).  
36. U. Poschinger, A. Walther, M. Hettrich, F. Ziesel, F. Schmidt-Kaler, Interaction of a laser with a qubit in thermal motion and its application to robust and efficient readout. Appl. Phys. B 107, 1159-1165 (2012).  
37. S. An, J.-N. Zhang, M. Um, D. Lv, Y. Lu, J. Zhang, Z.-Q. Yin, H. T. Quan, K. Kim, Experimental test of the quantum Jarzynski equality with a trapped-ion system. Nat. Phys. 11, 193-199 (2015).  
38. C. Shen, L.-M. Duan, Correcting detection errors in quantum state engineering through data processing. New J. Phys. 14, 053053 (2012).

Acknowledgments: We thank P. Busch for helpful comments. Funding: This work was supported by the National Fundamental Research Program of China (grant no. 2012CB922102) and the National Natural Science Foundation of China (grant nos. 11274352, 11147153, 11404377, 11274351, 11275131, 11371247, and 11004226). V.V. acknowledges funding from the National Research Foundation (Singapore), the Ministry of Education (Singapore), the Engineering and Physical Sciences Research Council (U.K.), the Templeton Foundation, and the Oxford Martin School. Author contributions: Z.M., L.Y., and M.F. proposed the scheme. F.Z. and M.F. designed the experiment. F.Z., S.G., L.C., J.H., and T.X. performed the experiment. L.Y. implemented the numerical calculation. M.F., V.V., L.Y., F.Z., and W.Y. wrote the paper. All the authors analyzed the data and made discussions. Competing interests: The authors declare that they have no competing interests. Data and materials availability: All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Additional data related to this paper may be requested from the authors.

Submitted 18 March 2016

Accepted 20 September 2016

Published 21 October 2016

10.1126/sciadv.1600578

Citation: F. Zhou, L. Yan, S. Gong, Z. Ma, J. He, T. Xiong, L. Chen, W. Yang, M. Feng, V. Vedral, Verifying Heisenberg's error-disturbance relation using a single trapped ion. Sci. Adv. 2, e1600578 (2016).

This article is publisher under a Creative Commons license. The specific license under which this article is published is noted on the first page.

For articles published under CC BY licenses, you may freely distribute, adapt, or reuse the article, including for commercial purposes, provided you give proper attribution.

For articles published under CC BY-NC licenses, you may distribute, adapt, or reuse the article for non-commercial purposes. Commercial use requires prior permission from the American Association for the Advancement of Science (AAAS). You may request permission by clicking here.

The following resources related to this article are available online at http://advances.sciencemag.org. (This information is current as of October 25, 2016):

Updated information and services, including high-resolution figures, can be found in the online version of this article at: http://advances.sciencemag.org/content/2/10/e1600578.full

Supporting Online Material can be found at: http://advances.sciencemag.org/content/suppl/2016/10/17/2.10.e1600578.DC1

This article cites 34 articles, 2 of which you can access for free at: http://advances.sciencemag.org/content/2/10/e1600578#BIBL