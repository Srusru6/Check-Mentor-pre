# Gaussian Boson Sampling

Craig S. Hamilton, $^{1,*}$  Regina Kruse, $^{2}$  Linda Sansoni, $^{2}$  Sonja Barkhofen, $^{2}$  Christine Silberhorn, $^{2}$  and Igor Jex $^{1}$

$^{1}$ FNSPE, Czech Technical University in Prague, Brěhová 7, 119 15, Praha 1, Czech Republic

$^{2}$ Integrated Quantum Optics, Universität Paderborn, Warburger Strasse 100, 33098 Paderborn, Germany

(Received 19 April 2017; revised manuscript received 28 August 2017; published 23 October 2017)

Boson sampling has emerged as a tool to explore the advantages of quantum over classical computers as it does not require universal control over the quantum system, which favors current photonic experimental platforms. Here, we introduce Gaussian Boson sampling, a classically hard-to-solve problem that uses squeezed states as a nonclassical resource. We relate the probability to measure specific photon patterns from a general Gaussian state in the Fock basis to a matrix function called the Hafnian, which answers the last remaining question of sampling from Gaussian states. Based on this result, we design Gaussian Boson sampling, a  $\# \mathsf{P}$  hard problem, using squeezed states. This demonstrates that Boson sampling from Gaussian states is possible, with significant advantages in the photon generation probability, compared to existing protocols.

DOI: 10.1103/PhysRevLett.119.170501

Boson sampling has sparked the imagination of theorists and experimentalists since it was introduced by Aaronson and Arkhipov [1]. It demonstrates the power of quantum over classical computation and provides evidence against the extended Church-Turing theorem, without the need for the full power of a universal quantum computer. In photonic Boson sampling,  $N$  single photon Fock states are launched into an  $N^2$ -mode interferometer. Because of bosonic statistics, the probability to measure a specific photon pattern at the output depends upon the permanent of a submatrix of the interferometer unitary. The permanent is in the  $\# \mathbb{P}$  complexity class [2]; therefore, this distribution is difficult to sample from, unless certain computational complexity classes are equivalent, which would have serious consequences for complexity theory.

After this theoretical advance, several experimental groups performed the first demonstrations [3-6]. However, since perfectly deterministic sources of single photons are not available (although recently proof-of-principle Boson sampling experiments with quasideterministic sources have been demonstrated [7-9]), they made use of postselected photon-pair states from probabilistic photon-pair sources (such as two-mode squeezed states) to emulate the single photon input states. This postselected Fock Boson sampling (PFBS), heralding  $N$  single photons from  $N$  probabilistic sources, has an intrinsic exponential cost when scaling to high photon numbers and so cannot efficiently solve the Boson sampling problem. Lund et al. [10] improve the scaling of the generation probability by placing a probabilistic source in each of the  $N^2$  input modes, a protocol known as scattershot Boson sampling (SBS), which is in the same complexity class as Aaronson-Arkhipov Boson sampling (AABS). Recently, another way to improve the generation probability for high photon numbers was proposed by Ref. [11].

All of these schemes make use of Gaussian states but discard their Gaussian nature, as only a specific number of (postselected or heralded) single photons are retained from the complete distribution and the squeezers are driven in a low gain regime (mean photon number  $\langle n\rangle \ll 1$ ). Therefore, from an experimental perspective, it is valuable to investigate the Boson sampling scheme with Gaussian states, appreciating the full Gaussian nature of the input states, which has also applications for the simulation of molecular vibronic spectra [12]. This means lifting the constraint on pure single photon input states and considering squeezed states with a higher gain  $(\langle n\rangle \approx 1)$ . In addition to an experimental interest, the appreciation of the full Gaussian nature also implies a strong theoretical relevance. Is a Boson sampling problem with Gaussian states without the need for heralding in the same complexity class as sampling from single photon input states? This question has not yet been answered in general. Only for the special cases of sampling from a nonlinear-continuous variable quantum state [13] or sampling from a multimode thermal state [14,15] has this question been answered.

In this Letter we answer this question of sampling photons from a general Gaussian state and develop a new protocol we call Gaussian Boson sampling (GBS). Here, we utilize single mode squeezed states (SMSS) as our nonclassical resource, which then enter a linear interferometer and sample the output patterns in the photon number basis. We first derive a new theoretical result that shows the probability to measure a specific photon output distribution from a general Gaussian state can be written in terms of a matrix function, the Hafnian. As the Hafnian is in the  $\# \mathsf{P}$  complexity class, we show that our exact GBS protocol is in  $\# \mathsf{P}$  and argue that an approximate sampling problem with errors is also in the same complexity class. Contrary to the existing protocols, where the sampling matrix is directly given by the unitary of the interferometer, here the sampling matrix absorbs both

$$
A ^ {2 M \times 2 M} = \left( \begin{array}{c c} B & C \\ \hline \\ C ^ {t} & B ^ {*} \end{array} \right) ^ {(b)} \begin{array}{c} K \times \text {S M S S} \\ \downarrow \quad \downarrow \quad \dots \quad \downarrow \\ T _ {\text {G B S}} \\ \boxed {\Downarrow \quad \dots \quad \Downarrow} \end{array}
$$

FIG. 1. (a) Construction of submatrix  $A_{S}$  from  $A$ , where highlighted rows or columns remain. Also shown is the structure of  $A(A_{S})$ , which can be divided into four block matrices. (b)  $K$  SMSS enter a linear interferometer  $T$  and at the output we measure the multimode squeezed state in the Fock state basis ( $K \approx N \ll N^2 = M$ ). The probability of a given pattern  $\bar{n}$  is given by Eq. (11).

the action of the interferometer and the overall shape of the Gaussian input state. We use a coherent superposition of all  $N$ -photon patterns from the Gaussian input and we do not herald an exact input pattern, as opposed to the other protocols where both input and output patterns determine the sampling problem. These two observations loosen the requirement on having single photon Fock states at the input and we are able to retain higher order photon number contributions from the same input mode.

Photocounts from a Gaussian state. Photonic Boson sampling involves sending single photon Fock states into a linear interferometer, described by a matrix  $T$ , which transforms  $M$  input modes into  $M$  output modes. The probability of measuring a certain pattern of photons  $\hat{n} = \otimes_{j}^{M} |n_{j}\rangle \langle n_{j}|$  ( $n_{j}$  photons in output mode  $j$ ) from  $M$  modes of a quantum state  $\hat{\rho}$  is  $\operatorname{Pr}(\bar{n}) = \operatorname{Tr}[\hat{\rho} \hat{n}]$ . For Boson sampling from Fock states  $\operatorname{Pr}(\bar{n})$  depends upon the permanent of a matrix [16]

$$
\Pr (\bar {n}) = \frac {\left| \operatorname {P e r m} \left(T _ {S}\right) \right| ^ {2}}{\bar {n} ! \bar {m} !}, \tag {1}
$$

where  $\bar{m}$  is the input photon pattern,  $\bar{n}! = n_1!n_2!\dots n_M!$ , and  $T_{S}$  is a submatrix of the linear transformation that depends upon where the photons enter and exit the interferometer. Here, we derive a new expression for  $\operatorname*{Pr}(\bar{n})$  from a Gaussian state after passing an  $M$ -dimensional linear interferometer. This state is characterized solely by a  $2M\times 2M$  covariance matrix  $\sigma$  and a displacement vector  $d$  [17],

$$
\sigma_ {i j} = \frac {1}{2} \left\langle \left\{\hat {\xi} _ {i}, \hat {\xi} _ {j} ^ {\dagger} \right\} \right\rangle - d _ {i} d _ {j} ^ {*}, \quad d _ {j} = \left\langle \hat {a} _ {j} \right\rangle ,
$$

where  $\hat{\xi}_j$  run over all  $\hat{a}_j$ ,  $\hat{a}_j^\dagger$  (annihilation and creation operators for a photon in mode  $j$ ) and we assume  $d_j = 0 \forall j$ . The details of this derivation are given in Ref. [18]. Using phase space methods (similar to Refs. [14,19,20]),  $\operatorname*{Pr}(\bar{n})$  becomes the integral of the  $Q$  and  $P$  functions of the state and operator,

$$
\Pr (\bar {n}) = \pi^ {M} \int d ^ {2 M} \alpha Q _ {\hat {\rho}} (\boldsymbol {\alpha}) P _ {\bar {n}} (\boldsymbol {\alpha}), \tag {2}
$$

where  $d^{2M}\alpha = \prod_{j=1}^{M} d\alpha_{j} d\alpha_{j}^{*}$ ,  $Q_{\hat{\rho}}$  is the  $Q$  function of the state and  $P_{\bar{n}}$  is the  $P$  function corresponding to the operator  $\hat{\bar{n}}$ . This analysis leads to

$$
\Pr (\bar {n}) = \frac {1}{\bar {n} ! \sqrt {\left| \sigma_ {Q} \right|}} \prod_ {j = 1} ^ {M} \left(\frac {\partial^ {2}}{\partial \alpha_ {j} \partial \alpha_ {j} ^ {*}}\right) ^ {n _ {j}} e ^ {\frac {1}{2} \alpha_ {v} ^ {t} A \alpha_ {v}} \Bigg | _ {\alpha_ {v} = 0}, \tag {3}
$$

where  $\sigma_{Q} = \sigma +\mathbb{I}_{2M} / 2$ $\alpha_{v} = [\alpha_{1},\dots ,\alpha_{M},\alpha_{1}^{*},\dots ,\alpha_{M}^{*}]^{t}$  and

$$
A = \left( \begin{array}{c c} 0 & \mathbb {I} _ {M} \\ \mathbb {I} _ {M} & 0 \end{array} \right) \left[ \mathbb {I} _ {2 M} - \sigma_ {Q} ^ {- 1} \right]. \tag {4}
$$

Note that  $\sigma$  contains only the modes that are observed (i.e., measured). Any modes that are not observed are traced over to get a reduced covariance matrix. The sampling matrix  $A$  can be divided into four block matrices, shown in Fig. 1, which is a consequence of the initial structure of  $\sigma$ . For simplicity we now focus on  $n_j = \{0,1\}$  (we deal with  $n_j \geq 2$  in Ref. [18]) for a total of  $N$  photons and  $2N$  derivatives (for  $\partial \alpha_j$ ,  $\partial \alpha_j^*$ ). The  $N$  indices of the photons' mode position are written in a vector  $\mu$  of length  $2N$  with entries  $j$  and  $j + M$  per photon. The  $2N$  derivatives select the rows or columns of  $A$  where the photons were measured; the other rows or columns will be discarded. This is illustrated in Fig. 1, where the intersection of the rows and columns where a photon was detected (highlighted in blue) form the entries of the submatrix  $A_S$ . The expansion of the  $2N$  derivatives leads to a summation over all perfect matching permutations (PMP) [21,22] of the vector  $\mu$ . For a general matrix  $A_S$  this is

$$
\Pr (\bar {n}) = \frac {1}{\bar {n} ! \sqrt {| \sigma_ {Q} |}} \sum_ {\mu^ {\prime} \in \mathrm {P M P}} \prod_ {j = 1} ^ {N} A _ {S _ {\mu^ {\prime} (2 j - 1), \mu^ {\prime} (2 j)}}. \tag {5}
$$

The sum over all PMP is exactly the Hafnian of  $A_{S}$ , as defined by Caianiello [23,24]. Finally, we arrive at

$$
\Pr (\bar {n}) = \left| \sigma_ {Q} \right| ^ {- 1 / 2} \operatorname {H a f} \left(A _ {S}\right) / \bar {n}! \tag {6}
$$

This new result relates the probability of a photon pattern  $\bar{n}$  from a general Gaussian state to the Hafnian of a matrix that characterizes that state. This formula applies for any Gaussian state (i.e., any covariance matrix), even if we lift the constraint of  $n_j = \{0,1\}$ . In this case, we repeat rows and columns in  $A_{S}$ , analogously to Ref. [25]. However, multiple photons in the same mode do not contribute to the complexity of calculating  $\operatorname*{Pr}(\bar{n})$  [26]. We discuss the case of multiple photons in the same output mode in more detail in Ref. [18]. We now use this result to develop a Boson sampling protocol for Gaussian states, with squeezing contributions only ( $B \neq 0$ ,  $C = 0$  in Fig. 1).

Gaussian Boson sampling with squeezed states. As the Hafnian is in the #P-complete complexity class [2], we can use Eq. (6) to devise a quantum sampling problem akin to AABS. Whereas the permanent counts the (weighted) number of perfect matchings in a bipartite graph, the Hafnian counts the number of perfect matchings in a general graph (not necessarily bipartite) [27]. Thus, the Hafnian is a more general function than the permanent, which is encapsulated in the formula

$$
\operatorname {P e r m} (G) = \operatorname {H a f} \left( \begin{array}{l l} 0 & G \\ G ^ {t} & 0 \end{array} \right), \tag {7}
$$

where  $G$  is the graph's adjacency matrix. This means that any algorithm or black box that can accurately calculate the Hafnian could also calculate the permanent, which is known to be #P-hard, even to approximate [1]. Currently, there is no known algorithm to efficiently approximate the Hafnian [28,29]. We illustrate GBS with the scenario shown in Fig. 1(b).  $K \times \mathrm{SMSS}(K \leq M)$  enter an  $M$ -mode linear interferometer, described by a Haar random unitary  $T$ , with all modes being measured at the output. The squeezing transformation is described by

$$
S = \left( \begin{array}{l l} \bigoplus_ {j = 1} ^ {M} \cosh r _ {j} & \bigoplus_ {j = 1} ^ {M} \sinh r _ {j} \\ \bigoplus_ {j = 1} ^ {M} \sinh r _ {j} & \bigoplus_ {j = 1} ^ {M} \cosh r _ {j} \end{array} \right) \tag {8}
$$

(four block diagonal matrices [30]) and  $r_j$  is the squeezing parameter of the  $j$ th mode, where at least  $K$  of them are nonzero. The covariance matrix at the output of the interferometer is [31]

$$
\sigma = \frac {1}{2} \left( \begin{array}{c c} T & 0 \\ 0 & T ^ {*} \end{array} \right) S S ^ {\dagger} \left( \begin{array}{c c} T ^ {\dagger} & 0 \\ 0 & T ^ {t} \end{array} \right), \tag {9}
$$

and we arrive at  $A = B\oplus B^{*}$  with

$$
B = T \left(\oplus_ {j = 1} ^ {M} \tanh  r _ {j}\right) T ^ {t}. \tag {10}
$$

The shape of the input squeezed states is encoded in  $\Gamma = \oplus_{j=1}^{M} \tanh r_{j}$ . Using Eq. (6), the probability to measure  $\bar{n}$  (zero or one photon per mode) is then

$$
\Pr (\bar {n}) = \left| \sigma_ {Q} \right| ^ {- 1 / 2} \left| \operatorname {H a f} \left(B _ {S}\right) \right| ^ {2}, \tag {11}
$$

where  $B_{S}$  is the  $N \times N$  submatrix that comprises only the rows and columns where a photon was detected, i.e., the sampled output pattern. Note, that contrary to the sampling schemes from Fock states, we absorb the shape of the Gaussian input state into our sampling matrix  $B$ . Therefore, our scheme is independent of the exact location of the input photons and allows us to retain more than one photon per input mode. Also, note that, due to the nature of squeezed light, we always obtain an even number of photons and for  $N$  odd,  $\operatorname{Pr}(\bar{n}) = 0$ .

Nevertheless, we have to ensure the complexity of the protocol, i.e., making  $B$  complex enough. If we pump  $K(\leq M)$  modes this means that  $B$  in Eq. (10) is a rank  $K$  matrix. It is known that the matrix rank determines the complexity of calculating the permanent [32] and the Hafnian [26]. Therefore, we place a minimal requirement of  $K = N$  SMSS at the input of our interferometer. Additionally, we have to ensure that our set of output patterns must be distinguishable from the uniform distribution with less than exponentially many samples. In Ref. [33], Aaronson and Arkhipov generalized their proof for AABS to input states with coherent superpositions of photons, which include our Gaussian input states.

Approximate GBS.—Since a realistic Boson sampler suffers from unavoidable error sources, we have to consider the problem of approximate sampling. In AABS this problem corresponds to approximating the permanent up to an additive error of matrices with random numbers from the complex normal distribution  $(|GPE|_{\pm}^{2})$  [1]. Aaronson and Arkhipov show that this is in  $BPP^{NP^{\mathcal{O}}}$ , where  $\mathcal{O}$  is an oracle for the AABS. Thus, a fast classical algorithm for  $\mathcal{O}$  would have severe consequences for the polynomial hierarchy. After this main result, Aaronson and Arkhipov introduce the permanent-of-Gaussians conjecture that expects approximate sampling with a multiplicative error  $GPE_{\times}$  in  $\#P$ , and the permanent-anticoncentration conjecture that surmises a polynomial-time equivalence of  $|GPE|_{\pm}^{2}$  and  $GPE_{\times}$ . Provided that these two conjectures hold, then  $P^{\#P} = BPP^{NP}$ , meaning that approximate AABS has to be in  $\#P$  or the polynomial hierarchy collapses. Since the experimental implementations of AABS and GBS are similar they will suffer from the same error sources.

Using the main elements of Aaronson and Arkhipov's hardness proof [1], we give heuristic arguments on how to apply them to the GBS problem, but leave the full proof for future work. Analogously to  $|\mathrm{GPE}|_{\pm}^2$  in Ref. [1] one should be able to formulate an equivalent statement for the Hafnian, i.e.,  $|\mathrm{GHE}|_{\pm}^2$ . A key result from Ref. [1] is that a matrix of independent and identically distributed complex normal entries,  $X$ , can be hidden inside a larger Haar unitary matrix  $T$ . In GBS, we sample the matrix  $T\Gamma T^\dagger$ , Eq. (10). We can choose  $\Gamma$ , the input squeezed states, such that the matrix we are interested in becomes  $XX^t$  (which can be hidden in  $T$ ). Based on this and given an approximate GBS oracle  $\mathcal{O}$ , a combination of Stockmeyer's algorithm and Markov's inequality should yield that  $|\mathrm{GHE}|_{\pm}^2$  is in  $\mathsf{BPP^{NP^o}}$ . As in Ref. [1], we leave open if approximate GBS is in  $\# \mathsf{P}$ . However, we give two conjectures for the Hafnian that place approximate GBS into this complexity class. First, we formulate a Hafnian-of-Gaussians conjecture, i.e., approximating the Hafnian up to multiplicative error  $\mathrm{GHE}_{\times}$  is in  $\# \mathsf{P}$ . This is similar to Aaronson and Arkhipov's permanent-of-Gaussians conjecture. As the Hafnian is a more general function than the permanent [see Eq. (7)], a Hafnian approximation algorithm up to a multiplicative error would also approximate the permanent up to a multiplicative error, justifying our conjecture. Furthermore, we conjecture that the two approximations  $|\mathrm{GHE}|_{\pm}^2$  and  $\mathrm{GHE}_{\times}$  are polynomial-time equivalent, which we believe is justified due to the similar structure of the permanent and the Hafnian. Provided the above conjectures hold and assuming approximate GBS is efficiently solvable by a classical algorithm, then  $\mathsf{P}^{\# \mathsf{P}} = \mathsf{BPP}^{\mathsf{NP}}$  and the polynomial hierarchy collapses.

GBS sampling patterns and generation probability. Because of the nature of Gaussian states the total number of output photons is not fixed. This means that we have to sample all sets of output patterns containing  $N$  photons in

$M$  modes  $\{N\in [0,\infty)$  of size  $C_N = \binom{M}{N}$ , assuming only zero or one photon per output mode}

$$
\begin{array}{l} \{\{p = | \sigma_ {Q} | \} _ {0}, \{p _ {1}, p _ {2}, \dots , p _ {C _ {1}} \} _ {1}, \dots , \{p _ {1}, p _ {2}, \dots , p _ {C _ {N}} \} _ {N}, \dots \} \\ = \{\{P _ {0} \}, \{P _ {1} \}, \{P _ {2} \}, \dots , \{P _ {N} \}, \dots \}, \\ \end{array}
$$

where  $p_j = \operatorname*{Pr}(\bar{n})$  is the probability of a certain output pattern, given by Eq. (11), and  $\{P_N\}$  is the set of all output patterns with  $N$  photons.

Although we can retain more than one photon at the input of our interferometer, the restriction to either zero or one photon per output mode means that we have to exclude multiple photon events at the output. As in the original protocol by Aaronson and Arkhipov, this is satisfied by the size and the nature of the interferometer. The Haarrandom transformation distributes the average photon number into all modes equally (on average), making the mean number of photons per mode  $K\langle n\rangle / M$ . When this is  $\approx 1/N$ , and we consider the photon number distribution in a single output mode, tracing over all other modes, we are left with a thermal state where the ratio between the single- and two-photon components is  $[\mathrm{Pr}(\text{two photons}) / \mathrm{Pr}(\text{one photon})] \approx 0.1$ . Thus, due to the small probability of higher order contributions, it is sufficient to use a low-resolution photon number resolving detector to reduce this error. Note that SBS also has to use photon number resolving detectors to exclude the higher order photon number contributions in the input state preparation. Since there exists no complexity proof for  $N > \sqrt{M}$ , we have to adapt the photon number generation of the SMSS to the dimension  $M$  of the network to ensure the computational hardness of the problem. The probability to generate a total of  $N$  photon pair events ( $2N$  photons) from  $K$  SMSS is given by the negative binomial distribution [34],

$$
P _ {K} (N) = \binom {\frac {K}{2} + N - 1} {N} \operatorname {s e c h} ^ {K} (r) \tanh  ^ {2 N} (r). \tag {12}
$$

The mean photon number of this distribution is  $n_{\mathrm{mean}} = K \sinh^2 (r)$  and the modal number (photon number with highest probability) is  $n_{\mathrm{modal}} = 2 \left[ \frac{K}{2} - 1 \right] \sinh^2 (r)$ . We can either operate in a regime where we focus on the probability of a specific photon number  $N$  and thus choose  $n_{\mathrm{modal}} = N$ , or we consider a range of photon numbers  $[N - c, N]$  (where  $c$  is a small integer) and set the mean photon number to  $n_{\mathrm{mean}} \approx N$ . Recalling our results from the previous section, we need at least  $K \geq N$  SMSS at the input and an interferometer size of  $M \geq N^2$  to saturate the complexity of an  $N$ -photon GBS experiment. In an experimental implementation we can choose one of these two regimes by fixing  $K$  and adjusting the squeezing parameter  $r$  accordingly.

Advantages of GBS.-To demonstrate the advantage of GBS in terms of the photon pair generation probability, we first compare it to existing protocols, which rely on  $N$  probabilistic, postselected photon pair events from  $K$  two-mode squeezed states. Previous protocols are restricted to

one photon pair per squeezeer and the probability to obtain  $N$  single photon pair events from  $K$  two-mode squeezed states follows a binomial distribution,

$$
P _ {\text {P F B S}} (N) = \binom {K} {N} \operatorname {s e c h} ^ {2 K} (r) \tanh  ^ {2 N} (r). \tag {13}
$$

Comparing Eqs. (12) and (13) for  $2N$  photons,  $K$  two-mode squeezed states, and the same squeezing parameter  $r$ , we find that the ratio of these is

$$
\begin{array}{l} P _ {\text {P F B S}} (N) / P _ {\text {G B S}} (N) = \binom {K} {N} / \binom {K + N - 1} {N} \\ \approx \lim  _ {N \rightarrow \infty , K > N} \left(\frac {K - N}{K - 1}\right) ^ {N}. \tag {14} \\ \end{array}
$$

In this regime, GBS has significant experimental advantages over PFBS protocols, as the probability to generate usable photons scales exponentially better. Comparing SBS, which uses  $K = N^2$  two-mode squeezers (with  $\langle n \rangle \approx 1 / N$ ), with GBS, we gain a factor of  $e$  increase in the probability to generate  $N$  photons. Still, an additional advantage of GBS is that we only require a low number of squeezers  $K \approx N \ll N^2 = M$  to saturate the complexity of an  $N$ -photon experiment. Summarizing, we gain a quadratic reduction in the number of required resources compared to SBS and an exponential increase in the generation probability compared to PFBS. In both cases, we gain an additional factor of 2 in the number of generated photons since we do not herald.

Because of the structure of  $A$ , the number of independent entries for the Hafnian is half of the entries in the permanent of AABS or SBS. In terms of computation time (not complexity, as complexity only considers scaling arguments), this means that the calculation of a permanent of an  $N \times N$  matrix is  $O(N2^{N})$ , while the Hafnian can be computed in  $O(2^{N/2})$  time. In order to achieve a comparable runtime for AABS (or SBS) and our GBS, this means that GBS has to consider  $2N$  photons. This however is not a problem, as we already obtain this factor of 2 by eliminating the heralding. The only requirements that we additionally have to fulfil are the size of the network, which now scales as  $4N^{2}$ , a constant increase to SBS, and the number of squeezers  $2N$  to saturate the complexity of the matrix, still a quadratic saving in resources, compared to SBS.

Conclusions.-We introduced Gaussian Boson sampling, which uses the easy-to-achieve experimental resource of squeezed states to implement a Boson sampling problem. We derived a new expression for the output probabilities from a general Gaussian state and showed that they are related to a matrix function called the Hafnian. Calculating the Hafnian is a computationally hard problem, in complexity class  $\# \mathsf{P}$ , and we provided evidence that even approximating a GBS problem is difficult. Our result answers questions in previous work as to the complexity of Boson sampling with Gaussian states [1,12,14] and we provide a detailed discussion of the ideas in this Letter in Ref. [18].

Because of the symmetry of quantum mechanics, we can reverse the problem of GBS and use the same result to classify the problem of a Fock state input to an interferometer with Gaussian-basis measurements [this open problem (4) in Ref. [1] has now been investigated independently by Refs. [35,36]]. Within experimental quantum optics, starting with a squeezed state, using linear optical transformations and postselected measurement outcomes is a very common method to create different families of photonic states. This means that GBS includes other photonic boson sampling protocols as special cases, which can be most readily seen from SBS, as we show in Ref. [18], but also includes other boson sampling problems such as those involving Schrödinger cat states and photon-added (or -subtracted) states [37-39]. Our formalism also allows us to handle the main sources of noise in photonic systems, photon loss and dark counts, in a very natural way as both are Gaussian operations. It is not clear how much loss we can tolerate in our Gaussian Boson sampling protocol to retain the #P complexity of the scheme (as opposed to the BPPNP complexity of thermal states [14]). With this, we believe that GBS will prove to be a powerful tool to study the interplay between losses and complexity in boson sampling protocols.

C. S. H. and I. J. received support from the Grant Agency of the Czech Republic under Grant No. GACR 17-00844S and from Ministerstvo Školství, Mládeže a Tělovýchovy (MSMT) RVO 68407700. This work has received funding from the European Union's Horizon 2020 research and innovation program under the QUCHIP project, Grant No. 641039. The authors would like to thank A. Arkhipov, A. Björklund, S. Rahimi-Keshari, and T. C. Ralph for useful comments.

\*hamilcra@fjfi.cyut.cz  
[1] S. Aaronson and A. Arkhipov, Theory Comput. 9, 143 (2013).  
[2] L. Valiant, Theor. Comput. Sci. 8, 189 (1979).  
[3] M. A. Broome, A. Fedrizzi, S. Rahimi-Keshari, J. Dove, S. Aaronson, T. C. Ralph, and A. G. White, Science 339, 794 (2013).  
[4] M. Tillmann, B. Dakic, R. Heilmann, S. Nolte, A. Szameit, and P. Walther, Nat. Photonics 7, 540 (2013).  
[5] J. B. Spring, B. J. Metcalf, P. C. Humphreys, W. S. Kolthammer, X.-M. Jin, M. Barbieri, A. Datta, N. Thomas-Peter, N. K. Langford, D. Kundys, J. C. Gates, B. J. Smith, P. G. R. Smith, and I. A. Walmsley, Science 339, 798 (2013).  
[6] A. Crespi, R. Osellame, R. Ramponi, D.J. Brod, E.F. Galvão., N. Spagnolo, C. Vitelli, E. Maiorino, P. Mataloni, and F. Sciarrino, Nat. Photonics 7, 545 (2013).  
[7] H. Wang, Y. He, Y.-H. Li, Z.-E. Su, B. Li, H.-L. Huang, X. Ding, M.-C. Chen, C. Liu, J. Qin, J.-P. Li, Y.-M. He, C. Schneider, M. Kamp, C.-Z. Peng, S. Hofling, C.-Y. Lu, and J.-W. Pan, Nat. Photonics 11, 361 (2017).  
[8] Y. He, X. Ding, Z.-E. Su, H.-L. Huang, J. Qin, C. Wang, S. Unsleber, C. Chen, H. Wang, Y.-M. He, X.-L. Wang, W.-J. Zhang, S.-J. Chen, C. Schneider, M. Kamp, L.-X. You, Z.

Wang, S. Hofling, C.-Y. Lu, and J.-W. Pan, Phys. Rev. Lett. 118, 190501 (2017).  
[9] J. Loredo, M. A. Broome, P. Hilaire, O. Gazzano, I. Sagnes, A. Lemaitre, M. P. Almeida, P. Senellart, and A. G. White, Phys. Rev. Lett. 118, 130503 (2017).  
[10] A. P. Lund, A. Laing, S. Rahimi-Keshari, T. Rudolph, J. L. O'Brien, and T. C. Ralph, Phys. Rev. Lett. 113, 100502 (2014).  
[11] S. Barkhofen, T.J. Bartley, L. Sansoni, R. Kruse, C.S. Hamilton, I. Jex, and C. Silberhorn, Phys. Rev. Lett. 118, 020502 (2017).  
[12] J. Huh, G. G. Guerreschi, B. Peropadre, J. R. McClean, and A. Aspuru-Guzik, Nat. Photonics 9, 615 (2015).  
[13] T. Douce, D. Markham, E. Kashefi, E. Diamanti, T. Coudreau, P. Milman, P. van Loock, and G. Ferrini, Phys. Rev. Lett. 118, 070503 (2017).  
[14] S. Rahimi-Keshari, A. P. Lund, and T. C. Ralph, Phys. Rev. Lett. 114, 060501 (2015).  
[15] V. Tamma and S. Laibacher, Phys. Rev. A 90, 063836 (2014).  
[16] S. Scheel, arXiv:quant-ph/0406127v1.  
[17] A. Ferraro, S. Olivares, and M. G. A. Paris, arXiv:quant-ph/0503237v1.  
[18] R. Kruse, C. S. Hamilton, L. Sansoni, S. Barkhofen, I. Jex, and C. Silberhorn, A detailed look at gaussian boson sampling (to be published).  
[19] V. V. Dodonov, O. V. Man'ko, and V. I. Man'ko, Phys. Rev. A 49, 2993 (1994).  
[20] V. V. Dodonov, O. V. Man'ko, and V. I. Man'ko, Phys. Rev. A 50, 813 (1994).  
[21] D. Callan, arXiv:0906.1317v1.  
[22] PMP are permutations  $\mu$  that obey (1)  $\mu(2j - 1) < \mu(2j)$  and (2)  $\mu(2j) < \mu(2(j + 1))\forall j.$  
[23] E. R. Caianiello, Nuovo Cimento 10, 1634 (1953).  
[24] E. R. Caianiello, Combinatorics and Renormalization in Quantum Field Theory (W. A. Benjamin, Inc., New York, 1973).  
[25] S. Aaronson and A. Arkhipov (ACM Press, New York, 2011), p. 333.  
[26] R. Kan, J. Multivariate Anal. 99, 542 (2008).  
[27] H. Minc, Permanents (Addison-Wesley, Reading, MA, 1978).  
[28] P. Sankowski, in Annual Symposium on Theoretical Aspects of Computer Science (Springer, New York, 2003), pp. 427-438.  
[29] A. Björklund, in Proceedings of the Twenty-Third Annual ACM-SIAM Symposium on Discrete Algorithms (SIAM, Philadelphia, 2012), pp. 914–921.  
[30]  $\bigoplus_{j = 1}^{N}A_{j} = A_{1}\oplus A_{2}\dots \oplus A_{N} = \mathrm{diag}(A_{1},A_{2},\ldots ,A_{N}).$  
[31] R. Simon, N. Mukunda, and B. Dutta, Phys. Rev. A 49, 1567 (1994).  
[32] A. I. Barvinok, Math. Oper. Res. 21, 65 (1996).  
[33] S. Aaronson and A. Arkhipov, arXiv:1309.7460v2.  
[34] J.M. Hilbe, Negative Binomial Regression (Cambridge University Press, Cambridge, England, 2011).  
[35] L. Chakhmakhchyan and N.J. Cerf, Phys. Rev. A 96, 032326 (2017).  
[36] A. P. Lund, S. Rahimi-Keshari, and T. C. Ralph, Phys. Rev. A 96, 022301 (2017).  
[37] P. P. Rohde, K. R. Motes, P. A. Knott, J. Fitzsimons, W. J. Munro, and J. P. Dowling, Phys. Rev. A 91, 012342 (2015).  
[38] J. P. Olson, K. P. Seshadreesan, K. R. Motes, P. P. Rohde, and J. P. Dowling, Phys. Rev. A 91, 022317 (2015).  
[39] K. P. Seshadreesan, J. P. Olson, K. R. Motes, P. P. Rohde, and J. P. Dowling, Phys. Rev. A 91, 022334 (2015).