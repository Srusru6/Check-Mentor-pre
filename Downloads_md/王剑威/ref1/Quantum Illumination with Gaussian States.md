# Quantum Illumination with Gaussian States

Si-Hui Tan, $^{1}$  Baris I. Erkmen, $^{2,*}$  Vittorio Giovannetti, $^{3}$  Saikat Guha, $^{2,\dagger}$  Seth Lloyd, $^{2}$  Lorenzo Maccone, $^{4}$  Stefano Pirandola, $^{2}$  and Jeffrey H. Shapiro $^{2,\ddagger}$

$^{1}$ Department of Physics, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, USA  
 $^{2}$ Research Laboratory of Electronics, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, USA  
 $^{3}$ NEST-CNR-INFM & Scuola Normale Superiore, Piazza dei Cavalieri 7, I-56126, Pisa, Italy  
 $^{4}$ QUIT, Dipartimento di Fisica "A. Volta," Universita' degli studi di Pavia, via Bassi 6, I-27100 Pavia, Italy (Received 2 October 2008; published 18 December 2008)

An optical transmitter irradiates a target region containing a bright thermal-noise bath in which a low-reflectivity object might be embedded. The light received from this region is used to decide whether the object is present or absent. The performance achieved using a coherent-state transmitter is compared with that of a quantum-illumination transmitter, i.e., one that employs the signal beam obtained from spontaneous parametric down-conversion. By making the optimum joint measurement on the light received from the target region together with the retained spontaneous parametric down-conversion idler beam, the quantum-illumination system realizes a 6 dB advantage in the error-probability exponent over the optimum reception coherent-state system. This advantage accrues despite there being no entanglement between the light collected from the target region and the retained idler beam.

DOI: 10.1103/PhysRevLett.101.253601

PACS numbers: 42.50.Dv, 03.67.Hk, 03.67.Mn

Entanglement is a fundamental quantum mechanical resource, with potential applications to Heisenberg-limited precision measurements [1], teleportation [2], and quantum cryptography [3]. Loss and noise, however, can quickly destroy this entanglement. Recently, Lloyd [4], building on the work of Sacchi [5], has shown that "quantum illumination" can reap substantial benefits, from the use of entanglement in target detection, despite the presence of entanglement-destroying loss and noise. In Lloyd's quantum-illumination paradigm, a photonic source creates  $d$ -mode maximally entangled signal and ancilla beams each containing a single photon. The signal beam irradiates a target region containing a very weak thermal-noise bath—with an average of  $b \ll 1$  photons per mode—in which a low-reflectivity ( $\eta \ll 1$ ) object might be embedded. The light received from this region—together with the retained ancilla beam—is then used to decide whether the object is present or absent. Lloyd showed that quantum illumination, with the optimum joint measurement on the received light and the ancilla, achieves an effective signal-to-background ratio of  $\eta d / b$ , whereas optimum quantum reception of light received in response to transmission of a single unentangled photon has a much lower (for  $d \gg 1$ ) signal-to-background ratio of  $\eta / b$ .

The analysis in Ref. [4] was confined, primarily, to the vacuum plus single-photon manifold, wherein at most one photon arrives at the receiver during the measurement interval, regardless of whether the object of interest is absent or present in the target region. Lloyd did briefly describe a microcanonical noise model whose quantum-illumination performance—for multiphoton signal and noise states with the same energy—again showed the factor of  $d$  improvement in the signal-to-background ratio.

However, the microcanonical model is rather restrictive, in that thermal-noise baths are in Gaussian states with Bose-Einstein distributed photon numbers. In this Letter, we will remedy that deficiency by providing a full Gaussian-state treatment of quantum-illumination target detection. Our treatment will employ the exact quantum statistics for the entangled signal and idler beams obtained from continuous-wave (cw) spontaneous parametric downconversion (SPDC) in the absence of pump depletion [6]. It will also use the standard model for the lossy, noisy bosonic channel [7]. We will show that in a very lossy, very noisy environment, a low-brightness quantum-illumination system enjoys a substantial improvement in the effective signal-to-background ratio—which can translate into a very large reduction of the target-detection error probability—in comparison to that achieved by a coherent-state transmitter of the same average photon number. As seen in Ref. [4], this performance advantage accrues to the quantum-illumination system despite there being no entanglement between the light that is received from the target region and the retained idler beam. Quantum illumination thus becomes the first example of an entanglement-based performance gain, in a full bosonic-channel setting, that survives entanglement-killing loss and noise.

Consider an entangled signal and idler mode pair obtained from cw SPDC. This mode pair—with annihilation operators  $\hat{a}_S$  and  $\hat{a}_I$ —is in the entangled state with number-ket representation

$$
| \psi \rangle_ {\mathrm {S I}} = \sum_ {n = 0} ^ {\infty} \sqrt {\frac {N _ {S} ^ {n}}{\left(N _ {S} + 1\right) ^ {n + 1}}} | n \rangle_ {S} | n \rangle_ {I}, \tag {1}
$$

where  $N_{S}$  is the average photon number per mode. In the

quadrature representation,  $|\psi \rangle_{\mathrm{SI}}$  is a zero-mean Gaussian state whose Wigner-distribution covariance matrix is

$$
\boldsymbol {\Lambda} _ {\mathrm {S I}} = \frac {1}{4} \left[ \begin{array}{c c c c} S & 0 & C _ {q} & 0 \\ 0 & S & 0 & - C _ {q} \\ C _ {q} & 0 & S & 0 \\ 0 & - C _ {q} & 0 & S \end{array} \right], \tag {2}
$$

where  $S \equiv 2N_{S} + 1$  and  $C_q \equiv 2\sqrt{N_S(N_S + 1)}$ . Viewed in this way, it is easily seen that  $|\psi\rangle_{\mathrm{SI}}$  has maximally entangled quadratures, because the magnitudes of the nonzero off-diagonal terms  $C_q$  in  $\Lambda_{\mathrm{SI}}$  equal the maximum value allowed by quantum mechanics given the diagonal elements of that matrix. Indeed, the upper limit on the magnitudes of these off-diagonal terms for a classical state, i.e., one with a proper  $P$  representation so that the signal and idler modes are unentangled, is  $C_c \equiv 2N_S$ . Thus, for a low-brightness source for which the average number of photons per mode is very low ( $N_S \ll 1$ ), there is a very strong nonclassical signature in  $\Lambda_{\mathrm{SI}}$  in that  $C_q \gg C_c$  prevails.

Suppose that we transmit the signal mode toward a spatial region that may or may not contain a weakly reflecting target but, in either case, contains a bright thermal-noise bath. Also suppose that the transmitter retains the idler mode, for a subsequent joint measurement to be made with the return from that target region. Under hypothesis  $H_{0}$  (target absent), the annihilation operator for the return from the target region will be  $\hat{a}_{R} = \hat{a}_{B}$ , where  $\hat{a}_{B}$  is in a thermal state with average photon number  $N_{B} \gg 1$ . Under hypothesis  $H_{1}$  (target present), the return-mode's annihilation operator will be  $\hat{a}_{R} = \sqrt{\kappa}\hat{a}_{S} + \sqrt{1 - \kappa}\hat{a}_{B}$ , where  $\kappa \ll 1$  and  $\hat{a}_{B}$  is now in a thermal state with average photon number  $N_{B} / (1 - \kappa)$ . Physically, this represents a very lossy  $(\kappa \ll 1)$  return from the target when it is present, combined with a very strong background contribution  $(N_{B} \gg 1)$  that, at the receiver, is independent of target absence or presence [8].

Under both hypotheses the joint state of the  $\hat{a}_R$  and  $\hat{a}_I$  modes is a zero-mean mixed Gaussian state, with conditional Wigner-distribution covariance matrices given by

$$
\boldsymbol {\Lambda} _ {\mathrm {R I}} ^ {(0)} = \frac {1}{4} \left[ \begin{array}{c c c c} B & 0 & 0 & 0 \\ 0 & B & 0 & 0 \\ 0 & 0 & S & 0 \\ 0 & 0 & 0 & S \end{array} \right] \tag {3}
$$

under  $H_0$  and

$$
\boldsymbol {\Lambda} _ {\mathrm {R I}} ^ {(1)} = \frac {1}{4} \left[ \begin{array}{c c c c} A & 0 & \sqrt {\kappa} C _ {q} & 0 \\ 0 & A & 0 & - \sqrt {\kappa} C _ {q} \\ \sqrt {\kappa} C _ {q} & 0 & S & 0 \\ 0 & - \sqrt {\kappa} C _ {q} & 0 & S \end{array} \right] \tag {4}
$$

under  $H_{1}$ , where  $B \equiv 2N_{B} + 1$  and  $A \equiv 2\kappa N_{S} + B$ . Neither of these conditional states is entangled. This is clearly so when the target is absent, because the bath mode

$\hat{a}_B$  is independent of the idler mode  $\hat{a}_I$ . When the target is present, the lack of entanglement when  $N_B > \kappa$  follows from the magnitude of the off-diagonal elements  $\sqrt{\kappa} C_q$  in  $\Lambda_{\mathrm{RI}}^{(1)}$  falling below the classical-state limit  $2\sqrt{N_S(\kappa N_S + N_B)}$  set by the diagonal elements in that matrix. In other words, the conditional density operators  $\hat{\rho}_{\mathrm{RI}}^{(0)}$  and  $\hat{\rho}_{\mathrm{RI}}^{(1)}$  for the return and idler modes under hypotheses  $H_0$  and  $H_1$  both have proper  $P$  representations and hence can be regarded as classically random mixtures of coherent states.

When the two hypotheses are equally likely, the minimum error-probability decision rule for the quantum-illumination receiver is as follows [9]. Measure  $\hat{\rho}_{\mathrm{RI}}^{(1)} - \hat{\rho}_{\mathrm{RI}}^{(0)}$  and declare the target to be present if a non-negative outcome results; otherwise, declare the target to be absent. Moreover, with  $\{\gamma_{n}^{(+)}\}$  denoting the non-negative eigenvalues of  $\hat{\rho}_{\mathrm{RI}}^{(1)} - \hat{\rho}_{\mathrm{RI}}^{(0)}$ , we have that the error probability of this optimum quantum receiver for the quantum-illumination transmitter is

$$
\Pr (e) = \left(1 - \sum_ {n} \gamma_ {n} ^ {(+)}\right) / 2. \tag {5}
$$

Unfortunately, finding the eigenvalues of  $\hat{\rho}_{\mathrm{RI}}^{(1)} - \hat{\rho}_{\mathrm{RI}}^{(0)}$  is a daunting task, so, as is often done in communication theory, we shall establish bounds on this error probability. Before doing so, however, we pause to introduce two classical-state comparison cases for the quantum-illumination system. The first uses a coherent-state transmitter with average photon number  $N_{S}$ . The second employs signal and idler modes that are in a joint classical state with only the signal being transmitted toward the target region, while the idler is retained for possible use in conjunction with the return mode from the target region. Optimum quantum reception will be assumed for both of these cases, so that they too employ a difference of conditional density operator measurements and have error probabilities given by (5) in terms of the non-negative eigenvalues of their measurement operators.

Based on Ref. [4], which showed that quantum illumination is advantageous at low signal-to-background ratios, and the fact that the off-diagonal elements in  $\Lambda_{\mathrm{SI}}$  asymptotically approach classical-state behavior for  $N_S \gg 1$ , we have chosen to study quantum illumination in the regime wherein  $N_S \ll 1$  and  $N_B \gg 1$ . Only a moment's thought is needed to conclude that the error probability in this operating regime will be very close to  $1/2$  for our quantum-illumination system, as well as for the coherent-state and classical joint-state comparison cases. So, to get to acceptably low error probabilities with the quantum-illumination and coherent-state systems, we will use  $M \gg 1$  identical transmissions of the types described above, in conjunction with optimum joint quantum measurements. Thus, the joint signal-idler state for the quantum-illumination transmitter will be  $\hat{\pmb{\rho}}_{\mathrm{SI}} = \bigotimes_{m=1}^{M} \hat{\rho}_{S_m I_m}$ , where the modal signal-idler

states are zero-mean and jointly Gaussian with the Wigner-distribution covariance matrix from (2), and the coherent-state transmitter will emit  $\otimes_{m=1}^{M}|\sqrt{N_S}\rangle_m$ , where  $\{| \cdot \rangle_m\}$  are the modal coherent states. The description of our general classical-state transmitter will be given later.

At this point, the quantum Chernoff bound [10] comes to our rescue. For optimum quantum discrimination between a pair of equally likely  $M$ -mode conditional density operators  $\hat{\pmb{\rho}}^{(k)} = \otimes_{m=1}^{M} \hat{\rho}_{m}^{(k)}$  for  $k = 0, 1$ , with identical modal states under each hypothesis, viz.,  $\hat{\rho}_{m}^{(k)} = \hat{\rho}^{(k)}$  for  $1 \leq m \leq M$  and  $k = 0, 1$ , the quantum Chernoff bound places the following limit on the error probability:

$$
\Pr (e) \leq \frac {1}{2} e ^ {- M \mathcal {E}} \equiv \frac {1}{2} \left\{\min  _ {0 \leq s \leq 1} \operatorname {t r} \left[ \left(\hat {\rho} ^ {(0)}\right) ^ {s} \left(\hat {\rho} ^ {(1)}\right) ^ {(1 - s)} \right] \right\} ^ {M}. \tag {6}
$$

The bound is exponentially tight; i.e., the error-probability exponent  $-\ln [\operatorname{Pr}(e)] / M$  converges to  $\mathcal{E}$  as  $M \to \infty$ . Its potentially weaker  $s = 1/2$  version, known as the Bhattacharyya bound,

$$
\Pr (e) \leq \frac {1}{2} \left\{\operatorname {t r} \left[ \left(\hat {\rho} ^ {(0)}\right) ^ {1 / 2} \left(\hat {\rho} ^ {(1)}\right) ^ {1 / 2} \right] \right\} ^ {M} \tag {7}
$$

will also be of interest in what follows, because it is more amenable to obtaining analytic results and because it is related to the lower bound on the error probability

$$
\Pr (e) \geq \frac {1}{2} \left(1 - \sqrt {1 - \left\{\operatorname {t r} \left[ \left(\hat {\rho} ^ {(0)}\right) ^ {1 / 2} \left(\hat {\rho} ^ {(1)}\right) ^ {1 / 2} \right] \right\} ^ {2 M}}\right), \tag {8}
$$

which, in general, is not exponentially tight.

Our quantum-illumination and coherent-state transmitters both lead to modal density operators, under each hypothesis, that are Gaussian states. Hence we can use the results of Ref. [11] to evaluate Chernoff or Bhattacharyya bounds. To do so, we need three things: the mean values of the relevant modes— $\hat{a}_R$  for the coherent-state transmitter and  $\hat{a}_R$  and  $\hat{a}_I$  for the quantum-illumination transmitter—under each hypothesis; the conditional Wigner-distribution covariance matrices for these relevant modes; and the symplectic diagonalizations of those conditional Wigner-distribution covariance matrices. The symplectic diagonalization of a  $2K \times 2K$  dimensional covariance matrix  $\Lambda$  consists of a  $2K \times 2K$  dimensional symplectic matrix  $S$  and a symplectic spectrum  $\{\nu_k: 1 \leq k \leq K\}$  that satisfy

$$
S \boldsymbol {\Omega} \boldsymbol {S} ^ {T} = \boldsymbol {\Omega} \equiv \bigoplus_ {k = 1} ^ {K} \left( \begin{array}{l l} 0 & 1 \\ - 1 & 0 \end{array} \right), \tag {9}
$$

$$
\boldsymbol {\Lambda} = \mathbf {S} \operatorname {d i a g} \left(\nu_ {1}, \nu_ {1}, \nu_ {2}, \nu_ {2}, \dots , \nu_ {K}, \nu_ {K}\right) \mathbf {S} ^ {T}, \tag {10}
$$

where  $\mathrm{diag}(\cdot ,\cdot ,\dots ,\cdot)$  denotes a diagonal matrix with the given diagonal elements.

For the coherent-state transmitter, we have that  $\mathrm{tr}(\hat{\rho}^{(0)}\hat{a}_R) = 0$ ,  $\mathrm{tr}(\hat{\rho}^{(1)}\hat{a}_R) = \sqrt{\kappa N_S}$ , and  $\Lambda^{(0)} = \Lambda^{(1)} = \mathrm{diag}(B/4, B/4)$ . It follows that  $S$  is the 2D identity matrix and  $\nu_{1} = B/4$ , so that the results in Ref. [11] lead to the quantum Chernoff bound (which turns out to be the

Bhattacharyya bound)

$$
\begin{array}{l} \Pr (e) _ {\mathrm {C S}} \leq e ^ {- M \kappa N _ {S} \left(\sqrt {N _ {B} + 1} - \sqrt {N _ {B}}\right) ^ {2}} / 2 (11) \\ \approx e ^ {- M \kappa N _ {S} / 4 N _ {B}} / 2, \quad \text {w h e n} \quad N _ {B} \gg 1. (12) \\ \end{array}
$$

Because (11) is also the Bhattacharyya bound, we have

$$
\begin{array}{l} \Pr (e) _ {\mathrm {C S}} \geq \frac {1}{2} \left(1 - \sqrt {1 - e ^ {- 2 M \kappa N _ {S} (\sqrt {N _ {B} + 1} - \sqrt {N _ {B}}) ^ {2}}}\right) (13) \\ \approx e ^ {- M \kappa N _ {S} / 2 N _ {B}} / 4, (14) \\ \end{array}
$$

when  $N_B \gg 1$  and  $M\kappa N_S / 2N_B \gg 1$ . For the quantum-illumination transmitter, the 4D identity matrix is the symplectic matrix needed for the diagonalization of  $\Lambda_{\mathrm{RI}}^{(0)}$ , and

$$
S = \left( \begin{array}{l l} \mathbf {X} _ {+} & \mathbf {X} _ {-} \\ \mathbf {X} _ {-} & \mathbf {X} _ {+} \end{array} \right) \tag {15}
$$

is the symplectic matrix needed to diagonalize  $\Lambda_{\mathrm{RI}}^{(1)}$ . Here  $\mathbf{X}_{\pm} \equiv \mathrm{diag}(x_{\pm}, \pm x_{\pm})$ , with

$$
x _ {\pm} \equiv \sqrt {\frac {A + S \pm \sqrt {(A + S) ^ {2} - 4 \kappa C _ {q} ^ {2}}}{2 \sqrt {(A + S) ^ {2} - 4 \kappa C _ {q} ^ {2}}}}. \tag {16}
$$

The associated symplectic spectra are  $\nu_{1} = B / 4$ ,  $\nu_{2} = S / 4$  under  $H_0$ , and

$$
\nu_ {k} = [ (- 1) ^ {k} (S - A) + \sqrt {(A + S) ^ {2} - 4 \kappa C _ {q} ^ {2}} ] / 8, \tag {17}
$$

for  $k = 1,2$ , under  $H_{1}$ . These diagonalizations can be employed to derive an analytic expression for the Bhattacharyya bound on the error probability achieved

![](images/15b920a6a2f962d3c3a55e3427c350ff663ea8a7249e4e4494114a043d7e508b.jpg)  
FIG. 1 (color online). Upper bounds (solid curves) on the target-detection error probabilities for coherent-state (Chernoff bound) and quantum-illumination (Bhattacharyya bound) transmitters with  $M$  transmitted modes each with  $N_{S} = 0.01$  photons on average when  $\kappa = 0.01$  and  $N_{B} = 20$ . Also shown is the lower bound (dashed curve) for the coherent-state case, which (see below) also applies to all classical-state transmitters with  $\sum_{m=1}^{M}\langle\hat{a}_{S_m}^\dagger\hat{a}_{S_m}\rangle = MN_S$ . For large  $M$ , the classical-state lower bound exceeds the quantum-illumination upper bound.

with quantum illumination. Unfortunately, that expression is far too long to exhibit here. In Fig. 1, we compare the coherent-state system's Chernoff bound from (11) and its lower bound from (13) with the quantum-illumination system's Bhattacharyya bound when  $\kappa = 0.01$ ,  $N_{S} = 0.01$ , and  $N_{B} = 20$ . We see that the quantum-illumination system's error-probability upper bound—at a given  $M$  value—can be orders of magnitude lower than the error-probability lower bound for coherent-state light.

To show that the advantage afforded by quantum illumination extends well beyond the specific example chosen for Fig. 1, we have used an algebraic computation program to obtain the following approximate form for the quantum-illumination transmitter's Bhattacharyya bound when  $\kappa \ll 1$ ,  $N_{s} \ll 1$ , and  $N_{B} \gg 1$ :

$$
\Pr (e) _ {\mathrm {Q I}} \leq e ^ {- M \kappa N _ {S} / N _ {B}} / 2. \tag {18}
$$

Comparing this low-brightness quantum-illumination result to the Chernoff bound for the coherent-state transmitter in the same lossy, noisy environment reveals that the use of entanglement at the transmitter improves the error-probability exponent by a factor of 4, i.e., by  $6\mathrm{dB}$ . One might wonder whether there is some other classical-state source that can match the performance of the quantum-illumination transmitter in this regime. To show that such is not the case, we now develop the perfect-measurement bound on the performance of any classical-state transmitter. Consider the general classical-state (signal and idler) transmitter whose output state is

$$
\hat {\boldsymbol {\rho}} _ {\mathrm {S I}} \equiv \iint \mathbf {d} ^ {2} \boldsymbol {\alpha} _ {S} \mathbf {d} ^ {2} \boldsymbol {\alpha} _ {I} P (\boldsymbol {\alpha} _ {S}, \boldsymbol {\alpha} _ {I}) | \boldsymbol {\alpha} _ {S} \rangle_ {S} | \boldsymbol {\alpha} _ {I} \rangle_ {\mathrm {I S}} \langle \boldsymbol {\alpha} _ {S} | _ {I} \langle \boldsymbol {\alpha} _ {I} |, \tag {19}
$$

where  $\{\left|\pmb {\alpha}_j\right\rangle_j\}$  for  $j = S,I$  are the  $M$  -mode coherent states of the signal and idler and  $P(\pmb {\alpha}_S,\pmb {\alpha}_I)$  is a probability density function over  $\{\pmb {\alpha}_j\colon j = S,I\}$  satisfying  $\sum_{m = 1}^{M}\langle \hat{a}_{S_m}^\dagger \hat{a}_{S_m}\rangle = MN_S$  . Minimum error-probability reception when the signal beam irradiates the target region and a joint measurement is made of the return from the target region and the retained idler is bounded from below by the error probability achieved, using this transmitter, when  $\pmb{\alpha}_{S}$  is known to the receiver. A noisy estimate of  $\pmb{\alpha}_{S}$  can be obtained from heterodyne detection of  $\pmb{\alpha}_{I}$  ; hence, our lower bound is correctly termed a "perfect-measurement" bound. Moreover, given knowledge of  $\pmb{\alpha}_{S}$  , the classicalstate system becomes a coherent-state transmitter, so that (13), convexity, and the average photon-number constraint imply that  $\operatorname *{Pr}(e)_{\mathrm{class}}$  obeys the same lower bound as  $\operatorname *{Pr}(e)_{\mathrm{CS}}$  . Thus, for  $N_B\gg 1$  all classical-state transmitters have error-probability exponents that are at least 3 dB inferior to that of quantum illumination with the same  $\sum_{m = 1}^{M}\langle \hat{a}_{S_m}^\dagger \hat{a}_{S_m}\rangle$  value.

Given that  $N_B = \kappa$  suffices to destroy the entanglement between the  $\hat{a}_{S_m}$  and  $\hat{a}_{R_m}$  modes under hypothesis  $H_1$ , it behooves us to find a physical explanation for the performance gain provided by quantum illumination. In our view, the explanation is as follows. When  $N_S \ll 1$ , the entangled  $\hat{a}_{S_m}$  and  $\hat{a}_{I_m}$  modes have a cross correlation that greatly exceeds what is permitted for a classical state. Although the corresponding cross correlation for  $\hat{a}_{R_m}$  and  $\hat{a}_{I_m}$  when the target is present is within classical bounds, there is no classical input state for  $\hat{a}_{S_m}$  and  $\hat{a}_{I_m}$  of the same average photon number that can produce a close approximation to this output state. Of course, a single-mode transmission with  $N_S \ll 1$ ,  $\kappa \ll 1$ , and  $N_B \gg 1$  cannot yield a low error-probability decision. However, the joint measurement over  $M \gg 1$  such modes can. Moreover, no special joint-state performance enhancement is realized with the coherent-state transmitter, because the product state  $\otimes_{m=1}^{M} |\sqrt{N_S}\rangle_m$  is merely a coherent state  $|\sqrt{MN_S}\rangle$  of a different mode. In summary, we must be careful not to dismiss the value of using entangled resources just because the application scenario is lossy and noisy.

This research was supported by the W.M. Keck Foundation Center for Extreme Quantum Information Theory and by the DARPA Quantum Sensors Program.

*Present address: Jet Propulsion Laboratory, Pasadena, CA 91109, USA.  
†Present address: BBN Technologies, Cambridge, MA 02138, USA.  
$\ddagger$  jhs@mit.edu  
[1] V. Giovannetti, L. Maccone, and S. Lloyd, Science 306, 1330 (2004).  
[2] C. H. Bennett et al., Phys. Rev. Lett. 70, 1895 (1993).  
[3] A.K. Ekert, Phys. Rev. Lett. 67, 661 (1991).  
[4] S. Lloyd, Science 321, 1463 (2008).  
[5] M. F. Sacchi, Phys. Rev. A 71, 062340 (2005); 72, 014305 (2005).  
[6] F.N.C. Wong, J.H. Shapiro, and T. Kim, Laser Phys. 16, 1517 (2006).  
[7] V. Giovannetti, S. Guha, S. Lloyd, L. Maccone, and J. H. Shapiro, Phys. Rev. A 70, 032315 (2004).  
[8] For  $\kappa \ll 1$  there is very little difference in the  $\langle \hat{a}_B^\dagger \hat{a}_B\rangle$  values under  $H_0$  and  $H_{1}$ . These values ensure that a nonvacuum transmitter must be used to detect target presence.  
[9] C.W. Helstrom, Inf. Control 10, 254 (1967).  
[10] K.M.R. Audenaert et al., Phys. Rev. Lett. 98, 160501 (2007); J. Calsamiglia et al., Phys. Rev. A 77, 032311 (2008).  
[11] S. Pirandola and S. Lloyd, Phys. Rev. A 78, 012331 (2008).