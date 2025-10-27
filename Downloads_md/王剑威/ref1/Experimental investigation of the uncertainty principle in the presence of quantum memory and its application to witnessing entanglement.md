# Experimental investigation of the uncertainty principle in the presence of quantum memory and its application to witnessing entanglement

Robert Prevedel<sup>1</sup>, Deny R. Hamel<sup>1</sup>, Roger Colbeck<sup>2</sup>, Kent Fisher<sup>1</sup> and Kevin J. Resch<sup>1</sup>

Heisenberg's uncertainty principle<sup>1</sup> provides a fundamental limitation on the ability of an observer holding classical information to predict the outcome when one of two measurements is performed on a quantum system. However, an observer with access to a particle (stored in a quantum memory) which is entangled with the system generally has a reduced uncertainty: indeed, if the particle and system are maximally entangled, the observer can perfectly predict the outcome of whichever measurement is chosen. This effect has recently been quantified<sup>2</sup> in a new entropic uncertainty relation. Here we experimentally investigate this relation, showing its effectiveness as an efficient entanglement witness. We use entangled photon pairs, an optical delay line serving as a simple quantum memory and fast, active feed-forward. Our results quantitatively agree with the new uncertainty relation. Our technique acts as a witness for almost all entangled states in our experiment as we obtain lower uncertainties than would be possible without the entangled particle<sup>3-5</sup>.

Consider an experiment in which one of two measurements is made on a quantum system. In general, it is not possible to predict the outcomes of both measurements precisely, which leads to uncertainty relations constraining our ability to do so. Such relations lie at the heart of quantum theory and have profound fundamental and practical consequences. They set absolute limits on precision technologies such as metrology and lithography, and also form the basis for new technologies such as quantum cryptography $^6$ .

The first relation of this kind was formulated by Heisenberg for the case of position and momentum<sup>1</sup>. Subsequent work by Robertson<sup>7</sup> and Schrödinger<sup>8</sup> generalized this relation to arbitrary pairs of observables. In particular, Robertson showed that

$$
\Delta R \cdot \Delta S \geq \frac {1}{2} | \langle [ R, S ] \rangle | \tag {1}
$$

where uncertainty is characterized in terms of the standard deviation (denoted  $\Delta R$  for an observable  $R$ ). Heisenberg's uncertainty relation has been subject to several investigations, and previous experiments have come close to the limit it imposes<sup>9-12</sup>.

To link uncertainty relations to classical and quantum information theory, they have recently been recast with the uncertainty quantified by the entropy $^{3,4}$  rather than the standard deviation. One such relation, conjectured by Kraus $^{13}$  and subsequently proven by Maassen and Uffink $^{5}$ , states that for any observables  $R$  and  $S$

$$
H (R) + H (S) \geq \log_ {2} \frac {1}{c} \tag {2}
$$

where  $H(R)$  denotes the Shannon entropy of the probability distribution of the outcomes when  $R$  is measured, and the term  $1 / c$  quantifies the complementarity of the observables. For nondegenerate observables, it is defined by  $c \coloneqq \max_{r,s} |\langle \Psi_r | \Upsilon_s \rangle|^2$ , where  $|\Psi_r\rangle$  and  $|\Upsilon_s\rangle$  are the eigenvectors of  $R$  and  $S$ , respectively. In the Supplementary Information, we briefly explain a key advantage of Maassen and Uffink's reformulation of the uncertainty relation over that of Robertson.

Interestingly, the above relations do not apply to the case of an observer holding quantum information about the measured system. In the extreme case, an observer holding a particle maximally entangled with the quantum system is able to correctly predict the outcome of whichever measurement is chosen. This dramatically illustrates the need for a new uncertainty relation.

The use of entanglement for predicting both outcomes of complementary measurements was suggested by Einstein et al.14 and experimentally demonstrated for the case of position and momentum measurements15-17. A quantification of this effect has recently appeared in the work of Berta et al., who derived a new relation, valid for all measurements with a finite number of outcomes (an equivalent form of this relation had previously been conjectured by Renes and Boileau18). The new relation is

$$
H (R | \mathrm {B}) + H (S | \mathrm {B}) \geq \log_ {2} \frac {1}{c} + H (\mathrm {A} | \mathrm {B}) \tag {3}
$$

where the measurement  $(R$  or  $S)$  is performed on a system, A, and the additional quantum information held by the observer is in B. The Shannon entropy of the outcome distribution is replaced by  $H(R|B)$ , the conditional von Neumann entropy of the postmeasurement state (after  $R$  is measured) given subsystem B. This quantifies the uncertainty about the outcome of a measurement of  $R$  given access to B (see Methods). This relation is a generalization of (2) and features an additional term on the right-hand side (RHS). This term is a measure of how entangled the system A is with the observer's particle, B, expressed through the conditional von Neumann entropy of the joint state,  $\rho_{\mathrm{AB}}$  of A and B before measurement,  $H(\mathrm{A}|\mathrm{B})$ . Note that this quantity can be negative only for entangled states<sup>19</sup>, and in this case lowers the bound on the sum of the uncertainties. In particular, if  $\rho_{\mathrm{AB}}$  is maximally entangled,  $H(\mathrm{A}|\mathrm{B}) = -\log_2d$ , where  $d$  is the dimension of the system. As  $\log_21 / c$  cannot be larger than  $\log_2d$ , the RHS of (3) cannot be greater than zero for a maximally entangled state. In this case, as mentioned previously, the outcome can be correctly predicted if  $R$  is chosen and it can be correctly predicted if  $S$  is chosen, for any observables  $R$  and  $S$ . This illustrates the additional power an observer holding quantum

information about the system has compared to an observer holding classical information.

In this work, we investigate the new inequality of Berta et al. experimentally, using entangled photon states and an optical delay serving as a simple quantum memory. Our experiment is, to the best of our knowledge, the first to study an entropic version of an uncertainty relation. Using entanglement allows us to achieve lower uncertainties about both observables than would be possible with only classical information, over a wide range of experimental settings. Hence, as well as quantitatively demonstrating Berta et al.'s bound, our experiment certifies the presence of entanglement. We discuss the efficiency of this entanglement witness towards the end of this Letter.

To clarify the sense in which an observer holding quantum information can outperform one without, we follow Berta et al.2 and relate uncertainty relations to a game between two parties, Alice and Bob. Bob creates a quantum system and sends it to Alice. He can prepare this system as he likes and, in particular, it can be entangled with another particle which he stores in a quantum memory (a device that maintains the quantum coherence of its content). Alice then performs one of two pre-agreed measurements,  $R$  or  $S$ , chosen at random. She announces the chosen measurement, but not its outcome. Bob's aim is to minimize his uncertainty (as quantified by the conditional von Neumann entropy) about Alice's measurement outcome (see Fig. 1).

In our experiment we realize Berta et al.'s uncertainty game, as shown in Fig. 1. We generate polarization-entangled photon pairs and delay the photon sent to Bob using an optical fibre which acts as a quantum memory. This gives Alice sufficient time ( $\sim 150$  ns in our case) to measure one of the two observables and to communicate her measurement choice to Bob (this is referred to as feed-forward). Our photon pair source $^{20-22}$  can produce an entangled state with high fidelity to

$$
\left| \Phi \right\rangle_ {\mathrm {A B}} = \cos \zeta \left| \mathrm {H} _ {\mathrm {A}} \mathrm {H} _ {\mathrm {B}} \right\rangle + \sin \zeta \left| \mathrm {V} _ {\mathrm {A}} \mathrm {V} _ {\mathrm {B}} \right\rangle \tag {4}
$$

where  $|\mathrm{H}\rangle$  ( $|\mathrm{V}\rangle$ ) denotes a horizontally (vertically) polarized photon and the subscripts label the spatial modes (Alice and Bob). Control over the parameter  $\zeta$  allows us to change the amount of entanglement, characterized by the conditional von Neumann entropy,  $H(\mathrm{A}|\mathrm{B})$ , between the two photons (see Methods). Although, as in any experiment, we are restricted to a finite set of states, we perform measurements on states over a wide range of values of  $\zeta$ .

The results of our experimental investigation are shown in Figs 2 and 3. Two different approaches are used to estimate the left-hand side (LHS) of equation (3). The first is a direct determination of  $H(X|B) + H(Z|B)$  (shown in the figures using blue datapoints) which requires us to experimentally find the reduced density matrix of Bob's photon, conditioned on Alice's measurement choice and outcome[23]. The second is to estimate the entropies by performing a projective measurement on Bob's photon, which allows us to calculate  $H(X|X_{\mathrm{B}}) + H(Z|Z_{\mathrm{B}})$  (where  $X_{\mathrm{B}}$  and  $Z_{\mathrm{B}}$  are the observables measured by Bob—these are the purple datapoints). As  $H(X|B) \leq H(X|X_{\mathrm{B}})$ , this technique will in general lead to a higher estimate of the uncertainty,  $H(X|B) + H(Z|B)$ . Its advantage is that it can be measured directly from the experimental counts without any tomographic reconstruction; this is important for the application as an entanglement witness (discussed below). Figures 2 and 3 show the results of both experimental approaches and we outline the details of the entropy inference in the Methods section.

The difference between the original uncertainty principle, equation (2), and Berta et al.'s relation, equation (3), is most apparent in the case of maximal entanglement and conjugate

![](images/f169c6b2521363a9caef58817a4d49f8c957525c491df1feac97733c07d84678.jpg)  
Figure 1 | Schematic of the experiment. Entangled photon pairs are created using spontaneous parametric down-conversion by pumping a periodically poled KTP crystal (PPKTP) inside a Sagnac interferometer and are subsequently fibre-coupled. Half-wave plates (HWP)  $P$ , A, and B are used to prepare a wide range of polarization-entangled states (see Methods for details). One photon is then distributed to Alice, who measures one of two observables,  $R$  or  $S$  (corresponding to different polarization bases). The observable is randomly selected by a 50/50 beamsplitter (BS) which separates the two polarization-analyser modules. The choice of basis is classically transmitted back to Bob, who in the meantime delays his photon in a 50 m single-mode fibre. A fast Pockels cell (PC; refs 22,31), which performs a bit flip operation ( $\sigma_{x}$ ) when on, in combination with HwPs, allows rapid switching between Bob's two pre-agreed measurement bases. The photons are detected using single-photon counting modules (SPCMs) and coincidence events between Alice's and Bob's detectors are recorded. Here we have depicted the experiment in the case that Bob measures his photon in the same basis as Alice. In some runs of the experiment, we also perform conditional tomography on Bob's photon (see main text). QWP, quarter-wave plate; PBS, polarizing beam splitter.

observables, for example,  $R = X$  (the  $\{|\mathrm{+}\rangle ,|\mathrm{-}\rangle \}$  basis) and  $S = Z$  (the  $\{|H\rangle ,|V\rangle \}$  basis). In this scenario, Bob can always correctly predict the outcome of Alice's measurement, that is,  $H(X|B) + H(Z|B) = 0$ . This would be impossible if Bob did not have a quantum memory, because the RHS of equation (2) has  $\log_21 / c = 1$  for these observables. In fact, for any finite entanglement between Alice's particle and Bob's quantum memory we expect to find lower uncertainties than in the case of no entanglement. This effect can be clearly seen in our experiment (see Fig. 2a), where many datapoints are found in the green shaded region, which indicates uncertainties that are inaccessible without entanglement.

Furthermore, we investigate the new uncertainty relation for other choices of observables. Choosing non-conjugate observables lowers the RHS of both inequalities (2) and (3). In Fig. 3a we chose the relative angle between the observables,  $\omega$ , as  $\omega \approx 0.57(32.5^{\circ})$  which corresponds to  $\log_21 / c = 1 / 2$ . Inequality (3) is not tight in this case, and there is no state of the form (4) for which it is satisfied with equality. This is reflected in Fig. 3, where the tomographic estimate no longer coincides with the Berta et al. bound (as it did in the case of conjugate observables). Here we are also able to witness entanglement by observing lower uncertainties than would be possible without a quantum memory, although the range of entanglement for which the witness succeeds is reduced, as expected. Discrepancies from the ideal, theoretical curves (the blue and purple solid lines in Figs 2 and 3) are mainly due to the

![](images/a25d37c3def2df2c441808142b2326117aedad79011b4845773835749b5dd563.jpg)  
a

![](images/47ebbeb31fd0db4f033c9ea52f77b15593a737da0f1948a2c5a7d2c8d9db6101.jpg)  
b

![](images/5ab3e92771b7624a1647c9f84245a56334d878740a023b0bfec568229934df62.jpg)

![](images/242b7f9160b0596399f43bacf4e1e484f34efd51a038bc8ee603c62462b86cd7.jpg)  
c

![](images/e51573e4e39e4a3a88e3fdffe89ab75932ba1f9797a7bc5457511481c7889508.jpg)  
Figure 2 | Experimental results. In a, we plot the left-hand side (LHS) of the new inequality (3) for the case where  $R = X$  and  $S = Z$ . In this case the relative angle,  $\omega$ , between the observables is  $\omega = \pi /4$ $(45^{\circ})$ . Experimentally, this is achieved by setting the analysers on Alice's side to perform measurements in the  $\{|\uparrow\rangle ,|\downarrow\rangle \}$  and  $\{|H\rangle ,|V\rangle \}$  bases. Varying HWP  $P$  in the source allows us to generate states with a range of entanglement, quantified by  $H(A|B)$  (see Methods). In the plot we use the value of  $H(\mathsf{A}|\mathsf{B})$  inferred from tomography. To calculate the uncertainty  $H(X|B) + H(Z|B)$  we evaluate the entropies of the conditional single-qubit density matrices of Bob's qubit, which we obtain through conditional quantum state tomography (blue dots). We also perform projective measurements on Bob's side and calculate the uncertainty  $H(X|X_{\mathrm{B}}) + H(Z|Z_{\mathrm{B}})$  (purple dots) directly from the obtained coincidence count rates. The green shaded area represents uncertainties that are not achievable without entanglement. Solid lines represent the theoretical predictions for the uncertainties assuming a noise-free experiment, whereas the dashed lines indicate the simulated performance of the experiment. For conjugate observables, the tomographic estimate coincides with equation (3). Note that the uncertainties inferred after measurements on Bob's side can be lower for the slightly mixed states generated by our source than for pure states with the same  $H(\mathsf{A}|\mathsf{B})$ . For the datapoints associated with the highest entanglement we show the corresponding coincidence count rates in  $\mathbf{b}$  and the reconstructed conditional density matrices in  $\mathbf{c}$ . Error bars  $(\sim 10^{-3})$  are too small to be seen. See Methods for details.

![](images/cd1141e600be61d10c0b2de713df026b3991cd0344f997cfd642127889d52858.jpg)  
a

![](images/33cd6959dec27727fb578fdae2129612225e955ab762f011469dc47a5741797d.jpg)  
Figure 3 | Uncertainties for other experimental settings. In a we plot the uncertainty  $H(X|B) + H(Z|B)$  (tomographic estimate) as well as the uncertainty  $H(X|X_{\mathrm{B}}) + H(Z|Z_{\mathrm{B}})$  (measurement estimate), where we fix the relative angle between two measurement bases on Alice's photon at  $\omega \approx 0.57$  ( $32.5^{\circ}$ ). This corresponds to the case where the bound in equation (2) drops to 1/2. Note that here the new uncertainty relation (3) is no longer tight. In b we plot the same uncertainties as in a, but choose a non-maximally entangled state with  $\zeta \approx 0.22$  ( $12.5^{\circ}$ ), which leads to  $H(\mathsf{A}|\mathsf{B}) = 0.47$  (inferred from tomography of the actual state). We then vary  $\omega$ , by fixing  $S = Z$  and varying  $R(\omega)$  from  $0^{\circ}$  to  $45^{\circ}$ . Note that the conditional entropies  $H(R|\mathsf{B})$  and  $H(S|\mathsf{B})$  cannot be negative and so, in the cases where the RHS of (3) is negative, the bound  $H(R|\mathsf{B}) + H(S|\mathsf{B}) \geq 0$  should be used instead.  
b

imperfect entanglement between the photons. Simulations of the experiment, based on the measured fidelities  $(F\approx 0.97)$  of our entangled photon pair source and assuming white noise as the dominant source of imperfection, confirm this (these are the blue and purple dashed lines in Figs 2 and 3).

In Fig. 3b, we investigate the new uncertainty relation for a fixed partially entangled state, varying  $\omega$  and therefore the complementarity of the observables,  $c(\omega)$ . Again we find uncertainties consistent with the new inequality. Further discussion on the optimization of the entangled states and measurements required to

get as close as possible to the bound imposed by the uncertainty principle is included in the Supplementary Information.

We now discuss our experiment and the new inequality in the context of the proposed application as a witness for bipartite entanglement. Uncertainty relations have been used in the past to derive entanglement witnesses[24,25]. The idea in our case is to use equation (3) to bound  $H(\mathrm{A}|\mathrm{B})$ . Whenever  $H(R|\mathrm{B}) + H(S|\mathrm{B}) < \log_21 / c$ , we can conclude that  $H(\mathrm{A}|\mathrm{B}) < 0$ , which is a certificate that  $\rho_{\mathrm{AB}}$  is entangled. This is readily observed in Figs 2 and 3: any datapoint inside the green shaded region indicates the presence of entanglement.

The strongest entanglement witness (in the sense of certifying the smallest amount of entanglement) is for the case of complementary observables. As can be seen in Fig. 2a, the quality of the witness depends on the technique used. In the case that Bob uses the measurement estimate, our experiment detects entanglement for  $H(\mathrm{A}|\mathrm{B}) \leq -0.074 \pm 0.004$ , which is more entanglement (and thus a less sensitive witness) than the analogous bound obtained with tomography,  $H(\mathrm{A}|\mathrm{B}) \leq 0.000 \pm 0.004$ . However, using tomography requires estimation of more parameters (16 versus 8). An even simpler witness can be obtained using only 2 parameters (see Methods), which we find to be only slightly weaker: it detects entanglement for  $H(\mathrm{A}|\mathrm{B}) \leq -0.162 \pm 0.002$  (see Supplementary Fig. S1).

Significantly, the 2 parameters needed for the simpler witness can be obtained using local measurements, making it easily implementable. For systems of local dimension 2, the merits of this are minor when compared to full tomography. However, our technique requires an estimate of only 2 parameters for (bipartite) systems of any size, whereas, for tomography, the number of parameters scales as the square of the dimension of the system, making the tomographic estimate infeasible for larger systems. We further remark that, although one parameter witnesses exist, these usually require measurement of a joint operator, which cannot be directly implemented without bringing both parts of the bipartite state together. In practice, to infer the value of these witness operators, they are often decomposed into locally measurable parts[26-28]. A common technique to generate witness operators is based on the partial transpose, for which it is known that this decomposition must involve at least  $N + 1$  local measurements, where  $N$  is the Schmidt rank of the state in question[27]. For states of the form  $\frac{1}{\sqrt{N}}\sum_{i = 0}^{N - 1}|i\rangle |i\rangle$ , for example, our technique is a significant improvement for large  $N$ .

As future quantum technologies emerge, they will be expected to operate on increasingly large systems. The entanglement witness we have demonstrated offers a practical way to quantitatively assess the quality of such technologies, for example the performance of quantum memories.

Note added in proof. During the preparation of the manuscript, we learned of related work, performed independently by Li et al.[29].

# Methods

Entropy inference. In this section we give an account of how the quantities appearing in equation (3) can be inferred from the data obtained in the experiment. We begin with the mathematical definition of the relevant quantities. For a density matrix  $\rho_{\mathrm{AB}}$ , the von Neumann entropy is defined by  $H(\mathrm{AB}) \coloneqq -\mathrm{Tr}(\rho_{\mathrm{AB}}\log_2\rho_{\mathrm{AB}})$ , which is conveniently calculated from the eigenvalues,  $\{\lambda_i\}$ , of  $\rho_{\mathrm{AB}}$  by  $H(\mathrm{AB}) = H(\{\lambda_i\}) \coloneqq -\sum_i\lambda_i\log_2\lambda_i$ . For a state  $\rho_{\mathrm{AB}}$ , the conditional entropy of A given B is defined as  $H(\mathrm{A}|\mathrm{B}) \coloneqq H(\mathrm{AB}) - H(\mathrm{B})$ , where  $H(\mathrm{B})$  is the von Neumann entropy of the reduced density operator,  $\rho_{\mathrm{B}} \coloneqq \mathrm{Tr}_{\mathrm{A}}\rho_{\mathrm{AB}}$ . The quantity  $H(R|\mathrm{B})$  is the conditional von Neumann entropy of the state

$$
\rho_ {R B} := \sum_ {r} \left(\left| \Psi_ {r} \right\rangle \left\langle \Psi_ {r} \right| \otimes \mathbb {1}\right) \rho_ {A B} \left(\left| \Psi_ {r} \right\rangle \left\langle \Psi_ {r} \right| \otimes \mathbb {1}\right)
$$

where  $R$  corresponds to a measurement on the A system in the orthonormal basis defined by  $\{|\Psi_r\rangle\}$  (this state is to be interpreted as the post-measurement state after  $R$  is measured). It will be convenient to write this in the following form:

$$
\rho_ {R B} = \sum_ {r} p _ {r} | \Psi_ {r} \rangle \langle \Psi_ {r} | \otimes \rho_ {B} ^ {r}
$$

where  $p_r$  is the probability of obtaining outcome  $r$  when  $R$  is measured, and  $\rho_{\mathrm{B}}^r$  is the state of the B system when  $r$  occurs. The relevant entropy can then be calculated using

$$
H (R | B) = H \left(\left\{p _ {r} \right\}\right) + \sum_ {r} p _ {r} H \left(\rho_ {B} ^ {r}\right) - H \left(\sum_ {r} p _ {r} \rho_ {B} ^ {r}\right)
$$

The entropy  $H(S|B)$  can be analogously defined.

The density operators  $\{\rho_{\mathrm{B}}^{r}\}_{r}$  are obtained by performing tomography on the state of the B system conditioned on observable  $R$  giving a particular outcome (see the next section for details). This generates the tomographic estimate of the uncertainty.

Alternatively, we can estimate  $H(R|B)$  by performing a measurement on  $B$  in a basis which we denote by  $R_{\mathrm{B}}$ , with outcome  $r_{\mathrm{B}}$ . As  $H(R|B) \leq H(R|R_{\mathrm{B}})$ , that is, measurements cannot decrease the entropy, we in general obtain a higher uncertainty. The entropy  $H(R|R_{\mathrm{B}})$  can be calculated from the resulting joint probability distribution of both measurements,  $P(r,r_{\mathrm{B}})$ , using  $H(R|R_{\mathrm{B}}) = H(\{P(r,r_{\mathrm{B}})\}) - H(\{P(r_{\mathrm{B}})\})$ . This gives rise to the measurement estimate on the uncertainty.

We also calculate the entropy using the bound  $H(R|R_{\mathrm{B}})\leq -q_R\log_2q_R - (1 - q_R)\log_2(1 - q_R)$  (which comes from Fano's inequality), where  $q_{R}$  is the probability that  $r\neq r_{\mathrm{B}}$ . This gives rise to the Fano estimate on the uncertainty and the entanglement witness requiring estimation of the fewest parameters. See the Supplementary Information for more details.

In the experiment we investigate the uncertainties for two-qubit states with Schmidt coefficients  $\cos \zeta$  and  $\sin \zeta$ . Such states have conditional von Neumann entropy  $H(\mathrm{A}|\mathrm{B}) = -H(\{\cos^2\zeta, \sin^2\zeta\})$ . In the actual experiment,  $H(\mathrm{A}|\mathrm{B})$  is calculated from the two-qubit density matrix (see below).

Experiment. In our experiment, we generate the entangled photon pairs using type-II spontaneous parametric down-conversion. A  $0.7\mathrm{mW}$  diode laser at  $404\mathrm{nm}$  pumps a  $25\mathrm{mm}$  periodically-poled  $\mathrm{KTiOPO_4}$  (PPKTP) crystal in a Sagnac configuration, emitting entangled photons which are subsequently single-mode fibre-coupled after  $3\mathrm{nm}$  bandpass interference filters (IF; ref. 22). Typically, we observe a coincidence rate of  $15\mathrm{kHz}$  directly at the source. A half-wave plate (HWP)  $P$  before the Sagnac interferometer controls the pump polarization and therefore allows us to precisely control  $\zeta$  in equation (4) and hence the entanglement of the generated state. Additional HwPs at the outputs of the fibres rotate the entangled state into the desired Schmidt basis  $|\theta\rangle$  (see Supplementary Information). Photons are detected by single-photon counting modules (SPCM) and their frequencies are recorded using a multichannel logic with a coincidence window of 3 ns.

On Alice's side, two polarization analyser modules, each consisting of a PBS preceded by a QWP and HWP, are separated by a 50/50 beamsplitter. One of them is set to measure in the  $\{|H\rangle ,|V\rangle \}$  basis, whereas the other can be set to measure at some chosen angle in the  $X - Z$  plane, namely  $\{|\omega \rangle ,|\omega^{\perp}\rangle \}$ , where the  $\omega$  in  $|\omega \rangle = \cos \omega |\mathrm{H}\rangle +\sin \omega |\mathrm{V}\rangle$  is the angle of the linear polarization.

The other down-converted photon is meanwhile delayed in a  $50\mathrm{m}$  single-mode optical fibre spool, which is long enough to execute the measurements on Alice's side and communicate (feed-forward) her chosen basis to Bob. Depending on the basis, Bob switches between two analyser bases,  $R$  and  $S$ . This is achieved by using a fast  $\mathrm{RbTiOPO_4}$  (RTP) Pockels cell (PC), aligned so as to perform a  $\sigma_x$  operation[22,31]. HwPs before and after the PC allow one to adapt the switchable analyser bases. Therefore, after passing the PC, Bob's photon is effectively measured in the  $\{| \omega \rangle , | \omega^{\perp} \rangle \}$  ( $| \mathrm{H} \rangle , |\mathrm{V} \rangle \rangle$ ) basis when the PC is on (off).

The experiment itself is performed as follows. At the start of each run, quantum state tomography $^{23}$  is performed on the entangled photon pair. We record coincidences between Alice's reflected arm of the BS and Bob's polarization analyser following the switched off PCs. Coincidence measurements were integrated over 5 s for a tomographically over-complete set of measurements, comprising all combinations of the six eigenstates of  $X$ ,  $Y$ , and  $Z$  on Alice's and Bob's qubit, respectively. Using an iterative technique we reconstruct the density matrix  $\rho_{\mathrm{AB}}^{\mathrm{exp}}$ , from which we infer the conditional entropy  $H(\mathrm{A}|\mathrm{B})$  of our state. We then set the analysers on Alice's side to the  $\{|H\rangle, |V\rangle\}$  ( $|\omega\rangle, |\omega^\perp\rangle$ ) basis in the transmitted (reflected) arm of the BS and perform conditional single-qubit tomography on Bob's photon, from which we calculate  $H(R(\omega)|\mathrm{B}) + H(Z|\mathrm{B})$ . Finally, Bob's analyser is set to the  $\{|H\rangle, |V\rangle\}$  basis, which allows us to calculate  $H(Z|Z_{\mathrm{B}})$  and  $H(R(\omega)|R_{\mathrm{B}}(\omega))$  directly from the coincidence counts. Stepwise repetition of this procedure for varying  $\zeta$  or  $\omega$  leads to the data presented in Figs 2 and 3.

Received 17 January 2011; accepted 13 June 2011; published online 24 July 2011

# References

1. Heisenberg, W. Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik. Z. Phys. 43, 172-198 (1927).  
2. Berta, M., Christandl, M., Colbeck, R., Renes, J. M. & Renner, R. The uncertainty principle in the presence of quantum memory. Nature Phys. 6, 659-662 (2010).  
3. Bialynicki-Birula, I. & Mycielski, J. Uncertainty relations for information entropy in wave mechanics. Commun. Math. Phys. 44, 129-132 (1975).

4. Deutsch, D. Uncertainty in quantum measurements. Phys. Rev. Lett. 50, 631-633 (1983).  
5. Maassen, H. & Uffink, J. B. Generalized entropic uncertainty relations. Phys. Rev. Lett 60, 1103-1106 (1988).  
6. Bennett, C. H. & Brassard, G. Proceedings of IEEE International Conference on Computers, Systems and Signal Processing, Bangalore, India, 175-179 (1984).  
7. Robertson, H. P. The uncertainty principle. Phys. Rev. 34, 163-164 (1929).  
8. Schrödinger, E. Proceedings of The Prussian Academy of Sciences Physics-Mathematical Section Vol. XIX, 296-303 (1930).  
9. Elion, W., Matters, M., Geigenmuller, U. & Mooij, J. Direct demonstration of Heisenberg's uncertainty principle in a superconductor. Nature 371, 594-595 (1994).  
10. Nairz, O., Arndt, M. & Zeilinger, A. Experimental verification of the Heisenberg uncertainty principle for fullerene molecules. Phys. Rev. A 65, 032109 (2002).  
11. LaHaye, M. D., Buu, O., Camarota, B. & Schwab, K. C. Approaching the quantum limit of a nanomechanical resonator. Science 304, 74-77 (2004).  
12. Schliesser, A., Arcizet, O., Riviere, R., Anetsberger, G. & Kippenberg, T. J. Resolved-sideband cooling and position measurement of a micromechanical oscillator close to the Heisenberg uncertainty limit. Nature Phys. 5, 509-514 (2009).  
13. Kraus, K. Complementary observables and uncertainty relations. Phys. Rev. D 35, 3070-3075 (1987).  
14. Einstein, A., Podolsky, B. & Rosen, N. Can quantum-mechanical description of physical reality be considered complete? Phys. Rev. 47, 777-780 (1935).  
15. Ou, Z. Y., Pereira, S. F., Kimble, H. J. & Peng, K. C. Realization of the Einstein-Podolsky-Rosen paradox for continuous variables. Phys. Rev. Lett. 68, 3663-3666 (1992).  
16. Kim, Y-H. & Shih, Y. Experimental realization of Popper's experiment: Violation of the uncertainty principle? Found. Phys. 29, 1849-1861 (1999).  
17. Howell, J. C., Bennink, R. S., Bentley, S. J. & Boyd, R. Realization of the Einstein-Podolsky-Rosen paradox using momentum- and position-entangled photons from spontaneous parametric down conversion. Phys. Rev. Lett. 92, 210403 (2004).  
18. Renes, J. M. & Boileau, J-C. Conjectured strong complementary information tradeoff. Phys. Rev. Lett. 103, 020402 (2009).  
19. Horodecki, R. & Horodecki, P. Quantum redundancies and local realism. Phys. Lett. A 194, 147-152 (1994).  
20. Kim, T., Fiorentino, M. & Wong, F. N. C. Phase-stable source of polarization-entangled photons using a polarization Sagnac interferometer. Phys. Rev. A 73, 012316 (2006).

21. Fedrizzi, A., Herbst, T., Poppe, A., Jennewein, T. & Zeilinger, A. A wavelength-tunable fiber-coupled source of narrowband entangled photons. Opt. Express 15, 15377-15386 (2007).  
22. Biggerstaff, D. N. et al. Cluster state quantum computing enhanced by high-fidelity generalized measurements. Phys. Rev. Lett. 103, 240509 (2009).  
23. James, D., Kwiat, P., Munro, W. & White, A. Measurement of qubits. Phys. Rev. A 64, 52312 (2001).  
24. Hofmann, H. F. & Takeuchi, S. Violation of local uncertainty relations as a signature of entanglement. Phys. Rev. A 68, 032103 (2003).  
25. Gühne, O. Characterizing entanglement via uncertainty relations. Phys. Rev. Lett. 92, 117903 (2004).  
26. Terhal, B. M. Detecting quantum entanglement. Theor. Comp. Sc. 287, 313-335 (2002).  
27. Gühne, O. Detection of entanglement with few local measurements. Phys. Rev. A 66, 062305 (2002).  
28. Gühne, O. & Toth, G. Entanglement detection. Physics Rep. 474, 1-75 (2009).  
29. Li, C-F., Xu, J-S., Xu, X-Y., Li, K. & Guo, G-C. Experimental investigation of the entanglement-assisted entropic uncertainty principle. Nature Phys. doi:10.1038/nphys2047 (2011).  
30. Nielsen, M. A. & Chuang, I. L. Quantum Computation and Quantum Information (Cambridge Univ. Press, 2000).  
31. Prevedel, R. et al. High-speed linear optics quantum computing using active feed-forward. Nature 445, 65-69 (2007).

# Acknowledgements

We thank M. Piani for valuable discussions and the Ontario Ministry of Research and Innovation ERA, QuantumWorks, NSERC, OCE, Industry Canada and CFI for financial support. R.P. acknowledges support by MRI and the Austrian Science Fund (FWF).

# Author contributions

K.J.R., R.P. and R.C. designed the experiment. R.P., D.R.H. and K.F. performed the experiment. R.C. provided theoretical support. R.P. analysed the data. R.P. and R.C. wrote the paper. All authors discussed and contributed to the final version of the manuscript.

# Additional information

The authors declare no competing financial interests. Supplementary information accompanies this paper on www.nature.com/naturephysics. Reprints and permissions information is available online at http://www.nature.com/reprints. Correspondence and requests for materials should be addressed to R.P.