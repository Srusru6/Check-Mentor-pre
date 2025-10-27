# Robust Creation of Entanglement between Ions in Spatially Separate Cavities

Daniel E. Browne, $^{1}$  Martin B. Plenio, $^{1}$  and Susana F. Huelga $^{2}$

$^{1}$ QOLS, Blackett Laboratory, Imperial College London, London SW7 2BW, United Kingdom  
 $^{2}$ Division of Physics and Astronomy, University of Hertfordshire, Hatfield, Herts AL10 9AB, United Kingdom (Received 26 February 2003; published 4 August 2003)

We present a protocol that allows the generation of a maximally entangled state between individual atoms held in spatially separate cavities. Assuming perfect detectors and neglecting spontaneous emission from the atoms, the resulting idealized scheme is deterministic. Under more realistic conditions, when the atom-cavity interaction departs from the strong coupling regime, and considering imperfect detectors, we show that the scheme is robust against experimental inefficiencies and yields probabilistic entanglement of very high fidelity.

DOI: 10.1103/PhysRevLett.91.067901

PACS numbers: 03.67.Hk

The ability to reliably create entanglement between spatially separated parties is of paramount importance for the actual implementation of any quantum communication protocol [1] and is also a prerequisite for distributed quantum computation [2]. Atoms or ions trapped inside optical resonators provide a promising setup for demonstrating the feasibility of quantum networking, and initial experimental progress has been recently reported [3]. Proposed ion trap quantum gates [4] allow the coherent processing of quantum information stored in long lived electronic states. Indeed, sequential gate operation allowed the first quantum algorithm to be implemented in a linear ion trap [5]. Transferring quantum information between distant sites could be achieved by mapping the electronic degrees of freedom of the ions onto the photonic degrees of freedom of the cavity, which can then be used to transmit the quantum information to a distant site. However, once the photon has left the resonator through one of its mirrors it is not a straightforward task to feed it into another cavity. Ingenious schemes using careful pulse shaping have been devised to achieve this goal [6] but their experimental implementation remains challenging.

A conceptually different approach consists of relaxing the condition that the quantum information is transferred via a photon leaving cavity  $A$  and entering cavity  $B$ . Several schemes have been proposed for the generation entanglement between atoms, by detecting photons in such a way that it is impossible to distinguish from which site they were emitted [7-11]. For example, one could imagine a setting as in Fig. 1, where photons are allowed to leave both cavities and are then mixed on a beam splitter prior to ordinary photon detection. Which-path information is destroyed in the beam splitter, and subsequent detection of a photon can then lead to a projection of the electronic degrees of freedom of the atom (which are entangled with the photonic degrees of freedom) onto some maximally entangled state [8].

In its original formulation, protocol [8] employed sudden excitation of the ions, which, assuming otherwise

perfect experimental conditions, limited its efficiency to  $50\%$ . In addition to that constraint, two further problems would be difficult to overcome in practice. The first and most serious one is that the interaction between an ion and an optical cavity usually takes place within the weak coupling regime, defined by the relationship  $g^2 /\kappa \gamma \ll 1$ . Here  $g$  is the ion-cavity coupling for a relevant set of atomic levels,  $\kappa$  is the decay rate of the optical cavity and  $\gamma$  denotes the spontaneous decay rate on the transition driven by the cavity mode. Within weak coupling, it is very likely that the atom will suffer an incoherent spontaneous emission, resulting in a photon leaving the cavity undetected to the sides before the electronic degree of freedom has been mapped onto the photonic degree of freedom, which severely damages the quantum entanglement that one intends to create.

Additionally, most protocols assume perfect detectors, which in practice are not generally available. This problem is compounded by the fact that in a number of setups for optical cavities the mirrors possess considerable absorption which can be as high as  $50\%$  of the photons that are not reflected from the cavity [12]. Therefore, any proposed scheme aimed to be demonstrated with current technology needs to be highly insensitive to detector

![](images/911e08a6c572aa9c68cfaeeed72dadb4fb74cea6fd759599b5f57b3cb3a2d147.jpg)  
FIG. 1 (color online). We consider a setup in which individual ions are trapped inside two spatially separated optical cavities  $A$  and  $B$ . Photons can leak out of the cavities and are then mixed on a beam splitter BS and subsequently detected by photodetectors  $D_{1}$  and  $D_{2}$ .

inefficiencies. Many of the above problems, such as weak coupling, poor detector efficiencies or absorption in the mirrors, also occur, if one wishes to entangle two ions in a single optical cavity by detecting photons as they leak out of the mirrors. For this setting a number of schemes have been put forward recently; see, e.g., [12,13]. In [12] an entangled state between the ions is prepared conditional on the failure to detect a photon leaking from the cavity. In practice, however, the fidelity of the state decreases very rapidly when one enters the weak coupling limit or when one has imperfect detectors or absorption in the mirrors. The second scheme [14] is more robust within the weak coupling regime, but requires single photon pulses and suffers strong loss of fidelity when faced with imperfect detectors or absorption in the mirrors [15].

In the following we present a scheme to entangle ions trapped individually in spatially separated cavities which (i) succeeds with  $100\%$  probability under ideal conditions, (ii) allows the achievement of high fidelity entanglement outside the strong coupling regime upon the detection of a photon, (iii) is robust against detector inefficiencies and absorption losses in the cavity mirrors, and (iv) can be adapted, with the same efficiency, to entangle ions trapped in a single optical cavity.

The method proposed here has its roots in the scheme presented in [8], where a teleportation protocol between two cavities that employs the leakage of photons through the cavity mirrors was discussed. The same method can also be used to establish entanglement between ions trapped in separate cavities. We briefly describe this approach here to illustrate its limitations and to motivate how to overcome them. Consider the setup depicted in Fig. 1, where each cavity contains a single trapped ion with an internal level structure which is given in Fig. 2. Light that may leak through the cavity mirrors is mixed

![](images/6623af17ca498566c980d238e363447c0e62db1020cff8af09468782f4496499.jpg)  
FIG. 2. Internal level scheme of the ions. A stable entangled state can be created when quantum information is encoded in the lower two levels  $|1\rangle$  and  $|2\rangle$ . These two levels are coupled via the upper level  $|3\rangle$ , employing two fields that have the same large detuning  $\Delta$  on their respective transitions to the upper level  $|3\rangle$ . The  $|1\rangle \leftrightarrow |3\rangle$  transition couples to the cavity mode while the  $|2\rangle \leftrightarrow |3\rangle$  transition is driven by a strong classical field. There may be spontaneous decay from  $|3\rangle$  to levels  $|1\rangle$  and  $|2\rangle$  at rates  $2\gamma_{31}$  and  $2\gamma_{32}$ , respectively.

on a 50/50 beam splitter and subsequently observed by photodetectors. The qubit is represented by the lower two energy levels which are coupled via a far-detuned Raman-like transition. In [8] it was envisaged that the ions are both initially prepared in state  $|2\rangle$ . Then, identical far-detuned classical light pulses are applied to both ions such that, under ideal conditions, the state of the global system is given by

$$
\begin{array}{l} \left| \psi_ {\text {t o t}} \right\rangle = \frac {1}{2} \left[ \left| 2 _ {A}, 2 _ {B} \right\rangle \right| \boldsymbol {v} _ {A}, \left. \boldsymbol {v} _ {B} \right\rangle - \left| 1 _ {A}, 1 _ {B} \right\rangle \left| p _ {A}, p _ {B} \right\rangle \\ + i \left(\left| 2 _ {A}, 1 _ {B} \right\rangle \left| v _ {A}, p _ {B} \right\rangle + \left| 1 _ {A}, 2 _ {B} \right\rangle \left| p _ {A}, v _ {B} \right\rangle\right) ], \tag {1} \\ \end{array}
$$

where  $|\nu_{A}\rangle$  represents the vacuum state in cavity  $A$  and  $|p_B\rangle$  denotes the one-photon Fock state in cavity  $B$ . Following this pulse, one waits to allow photons to leak through the cavity mirrors, mix at the beam splitter, and reach the detectors. If a single click occurs, then the system is projected onto one of the two entangled states  $\{(|2_A,1_B\rangle + |1_A,2_B\rangle) / \sqrt{2}, (|2_A,1_B\rangle - |1_A,2_B\rangle) / \sqrt{2}\}$ . If no photon is detected or two photons are detected, then the ions are projected onto a product state and the procedure has failed.

Apart from the sensitivity of this scheme to losses due to spontaneous emission and detector inefficiencies, the procedure fails even under ideal conditions in  $50\%$  of the cases, due to the high probability of a two-photon detection event, which leaves the ions in a product state. Furthermore, the scheme is not robust to spontaneous decay of the ions (this is particularly relevant in the weak coupling regime) or detector inefficiencies. If spontaneous emission occurs in one of the ions, the photon emitted will escape undetected, and the detection of one photon in the photodetectors after this event will then lead to the generation of the product state  $|1_A, 1_B\rangle$ . Also, if the detector is inefficient, then only one of the photons of a two-photon event, i.e., a failure of the protocol, might be detected.

An additional ingredient can make this scheme highly robust against all these sources of sources. This is achieved by relaxing the condition of sudden excitation of the two ions and replacing it by more gentle driving. In the following we will show that weak driving, under ideal conditions, avoids two-photon detection events and allows the scheme to succeed with arbitrarily high probability (and unit fidelity). The Hamiltonian of the combined ion-cavity system, with ion internal level structure as given in Fig. 2, in a suitable interaction picture and setting  $\hbar = 1$ , a convention we will use throughout this paper, is given by

$$
\begin{array}{l} H = \sum_ {i = A, B} (\Delta | 3 \rangle_ {i i} \langle 3 | + g | 3 \rangle_ {i i} \langle 1 | c _ {i} + g | 1 \rangle_ {i i} \langle 3 | c _ {i} ^ {\dagger} \\ + \Omega | 3 \rangle_ {i i} \langle 2 | + \Omega | 2 \rangle_ {i i} \langle 3 |), \tag {2} \\ \end{array}
$$

where we have assumed that the two ions are subjected to identical laser fields on the  $|2\rangle \leftrightarrow |3\rangle$  transition and that

this laser field has the same detuning as the cavity field that couples to the  $|1\rangle \leftrightarrow |3\rangle$  transition. The annihilation and creation operators for the cavity photons are denoted by  $c_{i}$  and  $c_{i}^{\dagger}$ . The upper level  $|3\rangle$  of both ions can decay to levels  $|1\rangle$  and  $|2\rangle$  with a rate of  $2\gamma_{31}$  and  $2\gamma_{32}$ , respectively. Each of the cavities has a decay rate  $2\kappa$ . The full master equation for the density operator  $\rho$  then takes the form

$$
\begin{array}{l} \dot {\rho} = - i \left(H _ {\text {e f f}} \rho - \rho H _ {\text {e f f}} ^ {\dagger}\right) + 2 \kappa \sum_ {i = A, B} c _ {i} \rho c _ {i} ^ {\dagger} \\ + \sum_ {n = 1, 2} \sum_ {i = A, B} 2 \gamma_ {3 n} | n \rangle_ {i i} \langle 3 | \rho | 3 \rangle_ {i i} \langle n |, \tag {3} \\ \end{array}
$$

with the effective non-Hermitian Hamiltonian

$$
H _ {\text {e f f}} = H - i \kappa \sum_ {i = A, B} c _ {i} ^ {\dagger} c _ {i} - i \left(\gamma_ {3 1} + \gamma_ {3 2}\right) \sum_ {i = A, B} | 3 \rangle_ {i i} \langle 3 |. \tag {4}
$$

This effective Hamiltonian will be used in the quantum jump approach to describe the system dynamics under the condition that neither a spontaneous emission nor a cavity photon has been detected [17].

For the sake of simplicity we now consider the system in the strong coupling limit by setting  $\gamma_{31} = \gamma_{32} = 0$ . We will later relax this condition to show that our method also works in the weak coupling limit. The requirement of weak driving means that the condition  $\frac{g\Omega}{\Delta}\ll \kappa$  is satisfied. Intuitively this implies that the rate of transitions between levels  $|1\rangle$  and  $|2\rangle$  of the ions will be weaker than the cavity decay. This in turn implies that the population in level  $|1\rangle$  of the atoms will be small, unless a photon is detected. Indeed, after adiabatic elimination of the upper level  $|3\rangle$  we obtain that the weak driving dynamics is governed by the new master equation [18],

$$
\dot {\rho} = - i \left(H _ {\mathrm {a d}} \rho - \rho H _ {\mathrm {a d}} ^ {\dagger}\right) + 2 \kappa \sum_ {i = A, B} c _ {i} \rho c _ {i} ^ {\dagger}, \tag {5}
$$

where we have defined

$$
\begin{array}{l} H _ {\mathrm {a d}} = \sum_ {i = A, B} \left[ \frac {g \Omega}{\Delta} (| 2 \rangle_ {i i} \langle 1 | c _ {i} + \mathrm {H . c .}) + \frac {g ^ {2}}{\Delta} | 1 \rangle_ {i i} \langle 1 | \right. \\ \left. + \frac {\Omega^ {2}}{\Delta} | 2 \rangle_ {i i} \langle 2 | - i \kappa c _ {i} ^ {\dagger} c _ {i} \right]. \tag {6} \\ \end{array}
$$

Under the condition that no detection has been registered, the time evolution is governed by  $H_{\mathrm{ad}}$ . Given an initial state  $|2_A, 2_B\rangle |\nu_A, \nu_B\rangle$ , the state of the systems will quickly approach the form

$$
\begin{array}{l} | \psi \rangle = | 2 _ {A}, 2 _ {B} \rangle | v _ {A}, v _ {B} \rangle + x (| 2 _ {A}, 1 _ {B} \rangle | v _ {A}, p _ {B} \rangle \\ + \left| 1 _ {A}, 2 _ {B} \right\rangle \left| p _ {A}, v _ {B} \right\rangle) + O \left(x ^ {2}\right), \tag {7} \\ \end{array}
$$

where  $x \cong -i\frac{g\Omega}{\Delta\kappa}$ . Therefore, the rate  $R$  at which one observes photons in one of the detectors is proportional to  $R \cong 4\kappa (\frac{g\Omega}{\Delta\kappa})^2$ . If one of the photodetectors clicks, then a maximally entangled state has been prepared to a high

precision and one switches off the lasers so that the entangled state is then preserved as the ions decouple from the cavity. The mean time before the first detection event will be

$$
T _ {\mathrm {a v}} \cong \frac {\Delta^ {2} \kappa}{4 (g \Omega) ^ {2}}. \tag {8}
$$

In such a time interval, there is a small probability that two photons are detected; however, this probability scales as  $|x|^{4}2\kappa T_{\mathrm{av}} \cong \frac{1}{2}\left(\frac{g\Omega}{\Delta\kappa}\right)^{2}$  and can therefore be made arbitrarily small in the limit of large detuning. Thus we can prepare a perfectly entangled state with arbitrarily high fidelity if we choose a sufficiently high detuning or sufficiently weak coupling strengths  $g$  and  $\Omega$ . As a consequence, by choosing a detuning that is very large, i.e., driving the  $|1\rangle \leftrightarrow |2\rangle$  transition very slowly, we can ensure that any detection event is linked to a single photon and that therefore the fidelity of the prepared state will be very close to unity. This demonstrates our first claim that the scheme can achieve perfect fidelity and unit success probability.

However, this result is still valid only in the difficult to achieve strong coupling limit as we have so far neglected the effect of finite  $\gamma_{31}$  and  $\gamma_{32}$ . In the following we will show that our scheme achieves, with reasonable success probability, a high fidelity entangled state even outside the strong coupling limit, i.e., where we allow  $\frac{g^2}{\kappa\gamma_{31}} \approx 1$  or even  $\frac{g^2}{\kappa\gamma_{31}} \ll 1$  and  $\gamma_{32}$  is allowed to be nonvanishing. We have performed a numerical simulation for the following choice of parameters:  $\Omega = g$ ,  $\kappa = 10g$ ,  $\gamma_{31} = \gamma_{32} = 0.1g$ , and  $\Delta = 20g$  and a waiting time, i.e., the time one is willing to wait for the first detection, of  $T = 100/g$ , and we obtain a fidelity of  $F = 0.98$  with a success probability of the scheme of  $p \cong 0.1$  which agrees with the analytic success probability  $p_{\mathrm{suc}} \cong (g\Omega/\Delta\kappa)^{2}4\kappa T$ .

The previous considerations still assume that the detection efficiency for photons that leak out of the cavity is unity. However, there are important sources of losses in experiments that make this assumption unrealistic. First, there may be absorption in the mirrors themselves [12], and, second, the detectors may have only a finite efficiency. A scheme that can work in a practical environment should therefore also be robust against detector inefficiencies. Fortunately, the present method exhibits exactly such a robustness. In terms of the detector efficiency  $\eta$  we find that the success probability simply scales linearly as  $p_{\mathrm{suc}} \cong (g\Omega/\Delta\kappa)^{2}4\kappa\eta T$ . With falling detector efficiency, the fidelity of the resulting state will decrease, because it will now contain an admixture from events where two photons have been emitted from the cavities, but only a single one has been detected. Indeed, from this argument one expects a weak linear reduction of the fidelity. In Fig. 3 we have plotted both the success probability and the achieved error (1-fidelity) for fixed  $\Omega = g$ ,  $\kappa = 10g$ ,  $\gamma_{31} = \gamma_{32} = 0.1g$ , and  $\Delta = 20g$ , and a waiting time of

![](images/5676b890b91780b5ab02fbf77b67c989fc046669b176d6efcf71280009bfc454.jpg)  
FIG. 3. The success probability (solid line) and the deviation from unit fidelity are plotted versus the detector efficiency for  $\Omega = g$ ,  $\kappa = 10g$ ,  $\gamma_{31} = \gamma_{32} = 0.1g$ , and  $\Delta = 20g$  and a waiting time of  $T = 100 / g$ . The plot has been obtained from a quantum jump simulation of the exact dynamics given by Eq. (4). Each point is the result of an average over  $10^{6}$  runs of the scheme.

$T = 100 / g$  against the detector efficiency. This figure confirms the approximate analytical formulas presented above and underlines that our scheme is robust against variations in the detector efficiencies.

A further experimental imperfection which must be considered is the presence of "dark counts"; i.e., the detector fires although no light is incident upon it, leading to a loss in fidelity of the state produced. However, in the present scheme, the time window in which a click due to a photon should occur is far shorter than the mean time between dark counts. For example, in [18] a dark count rate of approximately  $1400 \, \mathrm{s}^{-1}$  is reported; thus the mean time between dark counts is on the order of ms. In the optical regime, the atom-cavity coupling  $g$ , detuning  $\Delta$ , cavity decay rate  $\kappa$ , and the coupling with the classical field  $\Omega$  will all be at least on the order of MHz [20]. Thus, using Eq. (8) one can estimate that  $T_{\mathrm{av}}$ , the mean time before a proper click occurs in this scheme, is on the order of  $\mu \mathrm{s}$ , much smaller than the mean time between dark counts.

So far we have considered the case where we wish to entangle two spatially separated ion-cavity systems. However, the above method could also be used to entangle two ions trapped in a single cavity whose decay is monitored by a single photodetector if the system is set up such that the detection of a photon does not provide any information about which ion the photon was emitted from.

In summary, we have presented here an approach that, under ideal conditions, allows for the deterministic generation of perfect entanglement between individual ions

in distant cavities. In the ideal scenario, the unit success probability allows for the generalization of this scheme to the direct implementation of quantum gates. The scheme can be adapted to entangling multiple ions in a single optical cavity. Most importantly, the scheme is robust to realistic experimental imperfections, and, in particular, it allows for the probabilistic generation of high fidelity entanglement when operated within the weak coupling limit and monitored by inefficient detectors.

The authors thank P. L. Knight for helpful advice. This work was supported by the U.S.-Army through Grant No. DAAD 19-02-0161, the Nuffield Foundation, Hewlett Packard Ltd., and the EPSRC.

[1] M. B. Plenio and V. Vedral, Contemp. Phys. 39, 431 (1998); M. A. Nielsen and I. J. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, 2000); M. B. Plenio and V. Vitelli, Contemp. Phys. 42, 25 (2001).  
[2] J. I. Cirac et al., Phys. Rev. A 59, 4249 (1999).  
[3] A. B. Mundt et al., Phys. Rev. Lett. 89, 103001 (2002).  
[4] J. I. Cirac and P. Zoller, Phys. Rev. Lett. 74, 4091 (1995); A. Sorensen and K. Mølmer, Phys. Rev. Lett. 82, 1971 (1999); A. Sorensen and K. Mølmer, Fortschr. Phys. 48, 811 (2000); D. Jonathan, M. B. Plenio, and P. L. Knight, Phys. Rev. A 62, 042307 (2000); D. Jonathan and M. B. Plenio, Phys. Rev. Lett. 87, 127901 (2001).  
[5] S. Gulde et al., Nature (London) 421, 48 (2003).  
[6] J. I. Cirac et al., Phys. Rev. Lett. 78, 3221 (1997).  
[7] C. Cabrillo et al., Phys. Rev. A 59, 1025 (1999).  
[8] S. Bose et al., Phys. Rev. Lett. 83, 5158 (1999).  
[9] I. E. Protsenko et al., Phys. Rev. A 66, 062306 (2002).  
[10] X-L. Feng et al., Phys. Rev. Lett. 90, 217902 (2003).  
[11] C. Simon and W.T.M. Irvine, quant-ph/0303023.  
[12] E. Hinds(private communication).  
[13] M. B. Plenio et al., Phys. Rev. A 59, 2468 (1999); A. Beige et al., J. Mod. Opt. 47, 2583 (2000); E. Jané, M. B. Plenio, and D. Jonathan, Phys. Rev. A 65, R50302 (2002); J. Pachos and H. Walther, Phys. Rev. Lett. 89, 187903 (2002).  
[14] A.S. Sørensen and K. Mølmer, Phys. Rev. Lett. 90, 127903 (2003).  
[15] After completion of this manuscript, a further very promising scheme was suggested by Duan and Kimble [16], which provides high fidelity entanglement in the weak coupling limit and in the presence of inefficient detectors. However, its inherent maximal success rate of  $50\%$  is problematic for attempts to extend the scheme towards the implementation of quantum gates.  
[16] L.-M. Duan and H. J. Kimble, Phys. Rev. Lett. 90, 253601 (2003).  
[17] M. B. Plenio and P. L. Knight, Rev. Mod. Phys. 70, 101 (1998), and references therein.  
[18] T. Pellizzari, Phys. Rev. Lett. 79, 5242 (1997).  
[19] W.T. Buttler et al., Phys. Rev. Lett. 84, 5652 (2000).  
[20] J. McKeever et al., Phys. Rev. Lett. 90, 133602 (2003).