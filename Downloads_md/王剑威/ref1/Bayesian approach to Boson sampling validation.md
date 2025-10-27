# Bayesian approach to Boson sampling validation

Marco Bentivegna*, Nicolò Spagnolo* and Chiara Vitelli*†

$^{*}$ Dipartimento di Fisica, Sapienza Università di Roma, Piazza Aldo Moro 5, I-00185 Roma, Italy

†Center of Life NanoScience @ La Sapienza, Istituto Italiano di Tecnologia,

Viale Regina Elena, 255, I-00185 Roma, Italy

Daniel J. Brod

Instituto de Fisica, Universidade Federal Fluminense,

Av. Gal. Milton Tavares de Souza  $s / n$

Niterói, RJ 24210-340, Brazil

Andrea Crespi

Istituto di Fotonica e Nanotechnologie,

Consiglio Nazionale delle Ricerche (IFN-CNR),

Piazza Leonardo da Vinci 32, I-20133 Milano, Italy

Dipartimento di Fisica, Politecnico di Milano,

Piazza Leonardo da Vinci 32, I-20133 Milano, Italy

Fulvio Flamini

Dipartimento di Fisica, Sapienza Università di Roma,

Piazzale Aldo Moro 5, I-00185 Roma, Italy

Roberta Ramponi

Istituto di Fotonica e Nanotechnologie,

Consiglio Nazionale delle Ricerche (IFN-CNR),

Piazza Leonardo da Vinci 32, I-20133 Milano, Italy

Dipartimento di Fisica, Politecnico di Milano,

Piazza Leonardo da Vinci 32, I-20133 Milano, Italy

Paolo Mataloni

Dipartimento di Fisica, Sapienza Università di Roma,

Piazzale Aldo Moro 5, I-00185 Roma, Italy

Roberto Osellame

Istituto di Fotonica e Nanotechnologie,

Consiglio Nazionale delle Ricerche (IFN-CNR),

Piazza Leonardo da Vinci 32, I-20133 Milano, Italy

Dipartimento di Fisica, Politecnico di Milano, Piazza Leonardo da Vinci 32, I-20133 Milano, Italy

Ernesto F. Galvão

Instituto de Fisica, Universidade Federal Fluminense, Av. Gal. Milton Tavares de Souza s/n, Niterói, RJ 24210-340, Brazil

Fabio Sciarrino

Dipartimento di Fisica, Sapienza Università di Roma, Piazzale Aldo Moro 5, I-00185 Roma, Italy fabio.sciarrino@uniroma1.it

Received 29 September 2014  
Accepted 9 December 2014  
Published 10 February 2015

The Boson sampling problem consists in sampling from the output probability distribution of a bosonic Fock state, after it evolves through a linear interferometer. There is strong evidence that Boson sampling is computationally hard for classical computers, while it can be solved naturally by bosons. This has led it to draw increasing attention as a possible way to provide experimental evidence for the quantum computational supremacy. Nevertheless, the very complexity of the problem makes it hard to exclude the hypothesis that the experimental data are sampled from a different probability distribution. By exploiting integrated quantum photonics, we have carried out a set of three-photon Boson sampling experiments and analyzed the results using a Bayesian approach, showing that it represents a valid alternative to currently used methods. We adopt this approach to provide evidence that the experimental data correspond to genuine three-photon interference, validating the results against fully and partially-distinguishable photon hypotheses.

Keywords: Quantum simulation; boson sampling; integrated photonics.

# 1. Introduction

The large efforts towards the development of quantum simulators and, in the long term, of quantum computers are motivated by the so-called "Feynman's Conjecture", which states that general quantum phenomena are exponentially hard to simulate by classical computers. In this perspective, quantum devices would be able to break a central dogma of computer science, the extended Church-Turing thesis (ECT): Any effective calculation (i.e. any calculation performed in reasonable time by any physical process) can be efficiently simulated by a (classical) Turing machine.

The first hint of the possibility of falsifying the ECT can be searched in the superposition principle lying at the heart of quantum mechanics. In order to simulate an  $N$ -particle system, one would need to know the probabilities to find the particles at some specific positions  $x_{1}, x_{2}, \ldots, x_{N}$ . In a discretized space of  $M$  points, this would lead to  $M^{N}$  possible configurations. For quantum particles, one should consider all the possible quantum superpositions, requiring an exponential overhead in the number of particles to simulate. Furthermore, the dynamic behavior of quantum

systems is by itself believed to be hard to simulate, holding at the same time the promise to solve otherwise intractable computational problems. The main example is given by the time needed to factorize a large number, exponentially increasing with the number size for a classical computer, but only polynomially for a quantum computer performing Shor's algorithm.<sup>4</sup>

This is evidence of sorts that the ECT is violated by quantum computation. Nevertheless, there is still no experimental evidence against the ECT, and the number of controllable qubits which can be realized in practice is expected, in the near future, to remain much lower than what needed for factoring a large integer. This is why scientists have started to look at non-universal quantum computers able to outperform classical devices in specific tasks for which there is evidence of computational hardness.

# 2. The Boson Sampling Problem

Recently, Aaronson and Arkhipov introduced the so-called Boson sampling problem. Consider an  $m \times n$  complex-valued matrix  $A$  ( $m \geq n$ ), whose columns are orthonormal. We define  $\Phi_{m,n}$  as the set of possible strings of  $m$  non-negative integers  $T = t_1, t_2, \ldots, t_m$  which sum up to  $n$ . Each of these strings  $T$  defines a  $n \times n$  unitary matrix  $A_T$ , composed repeating  $t_k$  times the  $k$ th row of  $A$ , where  $k$  goes from 1 to  $m$ . Typically,  $\Phi_{m,n}$  is required to contain strings which are composed only of 0 and 1 (the so-called collision-free scheme, for reasons that will soon become obvious). The Boson sampling problem consists of sampling from the probability distribution over  $\Phi_{m,n}$  given by the following formula:

$$
P (S) = \frac {\left| \operatorname {p e r} \left(A _ {T}\right) \right| ^ {2}}{t _ {1} ! t _ {2} ! , \dots , t _ {m} !}. \tag {1}
$$

The permanent of an  $n\times n$  matrix  $A$  is given by:

$$
\operatorname {p e r} (A) = \sum_ {\sigma \in S _ {n}} \prod_ {i = 1} ^ {n} a _ {i, \sigma (i)}, \tag {2}
$$

where  $S_{n}$  contains all permutations of the integers  $1,2,\ldots ,n$ . We see the permanent is defined similarly to the determinant, but with plus signs only, for all permutations in the summation.

# 2.1. Boson sampling and computational complexity

The calculation of the permanent of an arbitrary complex matrix is a  $\# P$ -complete computational problem.6,7 While the well-known  $NP$  class consists of solving problems for which a solution can be verified efficiently by a classical computer,  $\# P$  problems consist of counting the number of solutions for a given  $NP$  problem, which is often a much harder task. Thus, being complete for the  $\# P$  class means that

permanent calculation is among the hardest  $\# P$  problems, and consequently believed to be much harder than any  $NP$  problem. Despite the fact that the probabilities defining the Boson sampling problem in Eq. (1) are given by permanents, the hardness of the Boson sampling problem itself is not  $\# P$ -complete — in other words, the ability to solve the Boson sampling problem (as, we will see, linear-optical experiments naturally do) does not imply the ability to efficiently estimate the individual permanents themselves, since these quantities will be typically exponentially small. Nonetheless, Aaronson and Arkhipov<sup>5</sup> have used the  $\# P$ -completeness of the permanent, plus a few technical conjectures, to show that an efficient classical algorithm for the Boson sampling problem would contradict long-standing conjectures regarding the structure of complexity classes, and thus is considered extremely unlikely.

# 2.2. Physical implementation by linear optics

In 2001, Knill, Laflamme and Milburn proved that universal quantum computation can in principle be performed using only linear optics, single-photon sources and detectors, and effective nonlinearities induced by measurements. Boson sampling is a problem that can be solved by linear optics in a natural way, with the advantage of not requiring adaptive measurements. Indeed, the Boson sampling problem was proposed with linear optics in mind; its abstract mathematical formulation can be directly mapped into a problem solvable by the evolution of  $n$  non-interacting bosons distributed on  $m$  paths of a linear interferometer.

Consider a unitary transformation  $U$ , described by an  $m \times m$  matrix, acting on the Fock state of  $n$  identical bosons distributed on  $m$  spatial modes. Here we will limit ourselves to the collision-free case, corresponding to a number of photons and modes which results, with a high probability, in at most one photon per output mode. Hence the initial state  $(S)$  and final state  $(T)$  can be described by a string of zeroes and ones of length  $m$ , and which sum up to  $n$ . The transition amplitude between  $S$  and  $T$  is given by the formula:

$$
\langle T | U | S \rangle = \frac {\mathrm {p e r} (U _ {S , T})}{\sqrt {s _ {1} ! s _ {2} ! , \ldots , s _ {n} !} \sqrt {t _ {1} ! t _ {2} ! , \ldots , t _ {n} !}}. \qquad \qquad (3)
$$

In summary, sending  $n$  photons through a  $m$ -mode linear optical interferometer and collecting the output with single photon detectors is equivalent to sampling from the distribution given by Eq. (1). The  $m \times n$  complex matrix  $A$  defined at the beginning to describe the Boson sampling problem is a submatrix of the  $m \times m$  unitary matrix describing the whole interferometer, given by the  $n$  columns corresponding to the input modes. The protocol is naturally efficient in the sense that the required resources scale polynomially with  $m$  and  $n$ .

Considering the complexity related to the calculation of the permanent, it turns out that in the regime  $n \simeq 20 - 30$ ,  $m \simeq 400$  the complexity of the system is so high

that a quantum device would start to outperform a classical computer in the task of solving the Boson sampling problem. $^{5}$  Few small-scale implementations of Boson sampling have been provided recently, demonstrating the in-principle feasibility of the problem with current technology. $^{9-12}$  Theoretical investigations on error tolerances, $^{13,14}$  scalability of sources implementation $^{15}$  or alternative architectures $^{16}$  have been performed as well.

# 3. Experimental Apparatus for the Realization of the Boson Sampling Experiment

As demonstrated in Ref. 17, an arbitrary linear transformation of a photonic Fock state can be implemented using only beamsplitters and phaseshifters, assembled in an interferometric structure of complexity rapidly increasing with size. A natural solution for this problem is given by integrated optical circuits, which have already shown great advantages with respect to the standard bulk approach in several recent experiments.[18-22] We successfully implemented a 3-photon Boson sampler using a 7-mode and a 9-mode linear interferometer on a glass chip. Multimode integrated interferometers with seven modes and nine modes were fabricated in glass chips by femtosecond laser writing[23,24] with layout as in Refs. 12 and 25. To inscribe the waveguides, laser pulses with  $220\mathrm{nJ}$  energy, 300 fs duration and  $1\mathrm{MHz}$  repetition rate emitted at  $1030\mathrm{nm}$  by an Yb:KYW cavity dumped oscillator were focused through a 0.6 NA microscope objective  $170\mu \mathrm{m}$  under the sample surface. The sample was translated at constant speed, drawing in the three dimensions the desired waveguide paths into a boro-aluminosilicate glass (EAGLE2000, Corning Inc.). The fabricated waveguides yield single mode behavior at  $800\mathrm{-nm}$  wavelength, with about  $0.5\mathrm{dB / cm}$  propagation losses.

Four photons were produced in the pulsed regime at  $785\mathrm{nm}$  exploiting the second order parametric down conversion process,[26,27] by pumping a 2-mm long BBO crystal with a  $392.5\mathrm{-nm}$  wavelength pump field. Typical count rates of the source were around  $250,000\mathrm{Hz}$  for the four signals,  $40,000\mathrm{Hz}$  for the two-fold coincidences and  $20\mathrm{Hz}$  for the four-fold coincidences. One of the photons, adopted as a trigger, was filtered by 3-nm interference filters, coupled into a single-mode fiber and detected by a single-photon counting detector. Regarding the other three photons, spectral filtering by 3-nm interference filters, single-mode fiber coupling, polarization compensation, and propagation through different delay lines was performed before coupling into the chips. The radiation coming out of the chip was collected into multimode fibers connected to single photon counting detectors (see Fig. 1). Four-fold coincidences between the three-photon state and the trigger signal were acquired by an electronic system consisting of a timing circuit driven by the trigger signal controlling both the conditioning input circuit and the four-fold coincidences discrimination and detection circuit. The circuit generates the handshake signal sent to the National PCI-6503 board used for recognizing the pattern.

![](images/d14549d3c367c10f23e44d769f47fcd8414f8f331da06461493b85ea2e86be2a.jpg)  
Fig. 1. Experimental implementation of Boson sampling (SHG: second harmonic generation, PDC: parametric down conversion, HWP: half waveplate, IF: interference filter, PBS: polarizing seamsplitter, APD: avalanche photodiode).

# 4. Validation of Boson Sampling Data

As was first highlighted in Ref. 28, the high complexity of simulating Boson sampling might conceivably result in the impossibility to recognize, at least in an efficient way, whether a data sample has been provided by a genuine Boson sampler or by some kind of cheater. We now discuss two different ways to perform a validation of Boson sampling data.

# 4.1. Row-norm estimator

The first example addresses the task of successfully distinguishing Boson sampling data from a uniform distribution over the set of possible output events. This can be done in a computationally efficient way using a statistical test developed by Aaronson and Arkhipov.[29] The test relies on the calculation of a quantity called Row-Norm estimator (RNE), defined as the product of the norm-2 moduli of the rows of  $A_{T}$  (see Sec. 2). As proved theoretically in Ref. 29 and experimentally demonstrated in Ref. 31, this estimator works because it presents enough correlation with the  $U_{S}$  permanent to allow efficient distinction of Boson sampling data from random samples, but not enough to provide a good estimate for the permanents themselves. The

test proceeds as follows: for each observed event  $T$ , the RNE is calculated for the corresponding matrix  $A_{T}$ . Then, for each event, a counter  $C$  is increased by one if the RNE for that event is greater than a threshold  $(n / m)^{n}$ , and decreased otherwise. The correlation between the values of the RNE and the output probabilities, which exists under the Boson sampling hypothesis but not under the uniform distribution one, guarantees that a set of true Boson sampling data will display typically higher values of the RNE, causing the counter  $C$  to grow on average. In fact, an almost monotonic increase (decrease) of  $C$  for Boson sampling (uniform) data allows to distinguish the two hypotheses with a constant number of events; experimentally, this was achieved with as few as 100 events.

The RNE test, however, has some intrinsic limitations. It can be shown<sup>5</sup> that an experiment analogous to Boson sampling that uses only distinguishable photons has a surprisingly similar description — specifically, its probability distribution is also given in terms of permanents, with the main difference being that the matrix  $U_{S,T}$  in Eq. (3) is replaced by a corresponding matrix  $|U|_{S,T}^2$  constructed by taking element-wise modulus squared on  $U_{S,T}$ . This difference, however, is fundamental, since the permanent of a matrix of non-negative entries can be approximated classically in polynomial time, and thus using distinguishable photons completely removes the non-classical computational power of the model. This also limits the RNE test, since it uses only the modulus of the matrix elements of  $U_{S,T}$ , and thus is insensitive to the distinction between the distinguishable and indistinguishable regimes by definition.

# 4.2. The Bayesian approach

One immediate issue with the uniform distribution is that it uses no information about the interferometer unitary  $U$ , which weakens the case for considering it a good candidate for an alternative hypothesis. This motivates the study of more general validation tests. In a recent work[31] we make use of a likelihood ratio test,[30] modified by including thresholds and a shot-by-shot evaluation, to rule out the hypothesis that the photons are distinguishable. Global coalescence effects[32] can be also used for this purpose, while experimental tests involving specific interferometers[33] or single-mode homodyne detection[34] can provide evidence against even more sophisticated models. On the statistical analysis' side, a number of tests on the two-photon correlation at the output of the interferometer have been proposed as evidence of genuine bosonic interference.[35] Here we propose the application of a Bayesian probabilistic analysis to the task of validating against the uniform distribution, and also against other distributions which use knowledge about the unitary  $U$ .

The Bayesian analysis works as follows. Before the experiment is performed, equal a priori probabilities are assigned to two different hypotheses,  $Q$ , which is the Boson sampling hypothesis, and  $R$ , which is an alternative hypothesis. For each sampled event  $x$ , let  $q_{x}$  be the corresponding probability associated to it under hypothesis  $Q$ , and  $r_{x}$  the corresponding probability under hypothesis  $R$ . Then by Bayes'

M. Bentivegna et al.

theorem, we get

$$
\frac {P (Q \mid N _ {\mathrm {e v e n t s}})}{P (R \mid N _ {\mathrm {e v e n t s}})} = \prod_ {x = 1} ^ {N _ {\mathrm {e v e n t s}}} \left(\frac {q _ {x}}{r _ {x}}\right) = \mathcal {X}. \tag {4}
$$

On the rhs of this equation, the numerator  $P(N_{\mathrm{events}}|Q) = \prod_x q_x$  is the conditional probability of obtaining a specific set of events  $\{k_x\}$  of size  $N_{\mathrm{events}}$  for a Boson sampler  $Q$ , and analogously for the alternative hypothesis  $R$  in the denominator:  $P(N_{\mathrm{events}}|R) = \prod_x r_x$ . Intuitively, the lhs of this equation corresponds to our degree of confidence in hypothesis  $Q$  over hypothesis  $R$ . If hypothesis  $Q$  corresponds to a better description of the observed data, than we will consistently observe events for which  $q_x > r_x$ , and the fraction will increase, indicating that hypothesis  $Q$  has a higher probability of corresponding to the data than hypothesis  $R$ . The probability assigned to hypothesis  $Q$  can then be written as

$$
P _ {\mathrm {i n d}} \equiv P (Q | N _ {\mathrm {e v e n t s}}) = \frac {1}{\mathcal {N}} \prod_ {x = 1} ^ {N _ {\mathrm {e v e n t s}}} \left(\frac {q _ {x}}{r _ {x}}\right), \tag {5}
$$

where  $\mathcal{N} = \mathcal{X} + 1$  is a normalization factor over both the considered hypotheses. The normalization factor  $\mathcal{N}$  is calculated so as to ensure that  $P(Q|N_{\mathrm{events}}) + P(R|N_{\mathrm{events}}) = 1$ .

The main advantage of the Bayesian approach is that it allows to perform validation tests against a large set of alternative hypotheses, since no additional assumption is required for the alternative sampler  $R$ .

# 4.3. Experimental application of the Bayesian approach to different alternative hypotheses

The alternatives to genuine Boson sampling that we are considering are the uniform distribution hypothesis U, the fully-distinguishable photons distribution  $D$ , and the partially-distinguishable PD. The latter corresponds to the case in which the interferometer is sampled by three photons, where only two are indistinguishable. For each event  $x$ , characterized by an input state  $S$  with photons in modes  $(i,j,k)$  and an output state  $T$  with photons in mode  $(l,m,n)$ , the different probabilities associated with the Boson sampling  $(q_x)$  or alternative hypotheses  $(u_x,d_x$  and  $p_x$  for hypotheses U, D and PD, respectively) are obtained as follows.

In the ideal Boson sampling case, the probabilities  $q_{x}$  are obtained by the distribution defined in Eq. (1). In our experiment, we took into account that one of the photons presents a lower degree of indistinguishability. This can be modeled as an input state which is an incoherent mixture of the form  $\rho = c^{2}|1_{i},1_{j},1_{k}\rangle \langle 1_{i},1_{j},1_{k}| + (1 - c^{2})|1_{i},1_{j}\rangle \langle 1_{i},1_{j}|\otimes |1_{k}\rangle \langle 1_{k}|$ , where  $c = 0.63$  in our case (see Ref. 9). In our implementation,  $k = 4$  for the 7-mode chip with input state (3,4,5), while  $k = 5$  for the 7-mode chip and 9-mode chip with input state (4,5,6).

For hypothesis D, describing fully distinguishable photons, the probabilities are calculated simply as  $d_{x} = \mathrm{per}(|U|_{S,T}^{2})$ , which results from summing probabilities, instead of amplitudes, corresponding to different paths of each photon (see Sec. 4.1). For hypothesis PD, describing an input where modes  $(i,j)$  contain identical photons and mode  $k$  contain a third photon distinguishable from the first two, the probability is given by  $p_{x} = \sum |\mathrm{per}(U_{S_{i,j},T_{l,m}})|^{2}|U_{k,n}|^{2}$ , which is a (classical) combination of two-photon interference terms and a single photon probability, and where the sum is performed over all permutations of the output indices  $(l,m,n)$ . Finally, for hypothesis U, the probabilities  $u_{x}$  are simply the uniform distribution over the possible (collision-free) configurations of  $n$  photons in  $m$  modes.

We have tested the performance of the Bayesian test in validating experimental Boson sampling data. The results are shown in Fig. 2 for the validation against the uniform distribution, and in Fig. 3 against the distribution of fully-distinguishable photons. In the first case, the Bayesian analysis reaches a  $95\%$  confidence level after  $\sim 30 - 40$  events for the 7-mode chip and after  $\sim 50$  events for the 9-mode chip. To validate against the fully-distinguishable hypothesis (Fig. 3), the test needs

![](images/db9e934bb753f1e591afed79fab62cbffbd0f997caa9bcfbb88a1e816542003d.jpg)  
(a)

![](images/98d7757862036e1939a550369b5a6c826550417aa79a986d28156bfbd089d080.jpg)  
(b)

![](images/8c28f4fa463a3f8c724c5c7a10c985918e95e354885a5fe42ea4a51b96490e10.jpg)  
(c)  
Fig. 2. (Color online) Bayesian update of the probability assigned to the Boson Sampling hypothesis, for experimental Boson Sampling data (blue) and for uniformly generated outputs (red), as a function of data set size  $N_{\mathrm{events}}$ . (a) 7-mode interferometer, input state  $(3,4,5)$ . (b) 7-mode interferometer, input state  $(4,5,6)$ . (c) 9-mode interferometer, input state  $(4,5,6)$ . Solid lines: experimental data taken with indistinguishable photons. Dashed lines: numerical simulation of data sampled from a uniform distribution. Shaded regions:  $1\sigma$  confidence intervals for experimental data (indistinguishable photons) or numerical simulations (uniform distribution). To take into account statistical fluctuations, lines and regions are obtained by averaging over 100 random reorderings of the whole data sets.

![](images/99740555d4a4cc278a8ebe28429e30a07851851fab5171231d26d5284e2556f5.jpg)

![](images/ff2811495ae1ea746bd84f7f347f7cfbdc308b9b3e5b144a85c7e8defbcae76b.jpg)

![](images/7ea29534dec68bb314780c6a8f701e572d6dc9054b20e819542ae2a48e9db3ee.jpg)  
Fig. 3. (Color online) Bayesian update of the probability assigned to the Boson Sampling hypothesis, for experimental Boson Sampling data (blue) and for data obtained from inputs of distinguishable photons (red), as a function of data set size  $N_{\mathrm{events}}$ . (a) 7-mode interferometer, input state (3,4,5). (b) 7-mode interferometer, input state (4,5,6). (c) 9-mode interferometer, input state (4,5,6). Solid lines: experimental data taken with indistinguishable photons. Dashed lines: experimental data taken with distinguishable photons. Shaded regions:  $1\sigma$  confidence intervals for experimental data. To take into account statistical fluctuations, lines and regions are obtained by averaging over 100 random reorderings of the whole data sets.

$\sim 200$  [7-mode chip, input  $(3,4,5)]$ ,  $\sim 250$  [7-mode chip, input  $(4,5,6)]$  and  $\sim 450$  [9-mode chip, input  $(4,5,6)]$  events. For a performance comparison, an RNE-analysis and an adapted likelihood ratio test (with thresholds, and a counting variable instead of the product of the probability ratios), which we reported in Ref. 31, required  $\sim 100$  events and  $\sim 100 - 200$  events to reach a  $95\%$  confidence level against, respectively, the uniform and the distinguishable photon hypotheses.[31]

Finally, in Fig. 4 we report the results of the validation against the partially-distinguishable case. For three-photon input, the distinguishable photon can be injected in one of the three possible input ports  $(i,j,k)$ . We then performed the validation test against all the three different choices of the distinguishable particle. In this case, validation is obtained for sample sizes of  $\sim 800$  [7-mode chip, input  $(3,4,5)]$ ,  $\sim 500$  [7-mode chip, input  $(4,5,6)]$  and  $\sim 800$  [9-mode chip, input  $(4,5,6)]$ . This analysis strengthens the validation process with respect to Ref. 31, since it provides a stronger indication that the experimental data correspond to three-photon interference events, ruling out the hypothesis that only two of the three photons are indistinguishable.

![](images/ccdd36c220ba395d5f11ec759dac3206ae473a7d01559800058c07a195410e48.jpg)

![](images/cc02a4e33bf7aa7ae7f602766997638745dcb7f394d1d772e5590af85c56fec7.jpg)

![](images/5bcab60490b4969a2842738b5400ec2c1d5b2ee5c4633724092e25291e37f48e.jpg)

![](images/6533c1faef86d47e22c742c3b0d84d6e89a86447e3e243c628242a7ddebb5489.jpg)

![](images/293a3530e3ce2e2ecdcebcd36f08d8ec38b50964b87e57c6e936a4125445cd0d.jpg)

![](images/3a1c810b27bc4d8908322c6265736ab75438aa52432059174e0027cc77b1a462.jpg)

![](images/f45d5b0876638f5f3919feaf16c92a4f8c4301fff69f9d75eeed454ab73aa053.jpg)  
Fig. 4. (Color online) Bayesian update of the probability assigned to the Boson Sampling hypothesis, for experimental Boson Sampling data (blue) and for simulations with input of partially distinguishable photons (green), as a function of data set size  $N_{\mathrm{events}}$ . (a)-(c) 7-mode interferometer, input state (3, 4, 5). (d)-(f) 7-mode interferometer, input state (4, 5, 6). (g)-(i) 9-mode interferometer, input state (4, 5, 6). Solid lines: experimental data taken with indistinguishable photons. Dashed lines: numerical simulations of data taken with one distinguishable photon. Which photon is distinguishable in each simulation is specified in each panel. Shaded regions:  $1\sigma$  confidence intervals for experimental data (indistinguishable photons) or numerical simulations (partially distinguishable sampler). To take into account statistical fluctuations, lines and regions are obtained by averaging over 100 random reorderings of the whole data sets.

![](images/3bc44aa388d9034e3b2f26f311638fb9930be5b2d6e69d76cf87a6c3ad2dfe2e.jpg)

![](images/5165b9941707ce3ca9b1cbb4252fa13b301853158e7ebf37548156d5882d1f80.jpg)

# 5. Discussion and Conclusion

The Bayesian approach turned out to require a sample size smaller by a factor of two than the one required by the RNE-based test, for validating against a uniform distribution in the regime of a small number of photons  $n$ . The amount of data needed by the Bayesian approach to validate against the Distinguishable Sampler is larger by a factor of two than the required sample for the modified likelihood ratio test with thresholds and a counting variable, used in Ref. 31. It is worth noting that the Bayesian analysis is not computationally efficient in  $n$ , since it requires the calculation of permanents of  $n \times n$  matrices. Still, these methods are expected to require a feasible computational effort even in the complexity regime where a quantum device

would start to outperform a classical computer. Indeed, for the validation we do not need to calculate the whole expected probability distribution over all the possible  $\binom{m}{n}$  output states, but just  $k$  permanents of  $n\times n$  matrices, with  $k$  of the order of 100. We further applied the Bayesian approach to validate Boson sampling data with respect to the case in which only two of the three photons are indistinguishable. These results provide evidence of genuine three-photon interference in the performed experiments.

In conclusion, we have applied a Bayesian approach to the problem of validating a set of real Boson sampling data against different alternative distributions, one of them uniform, and the others corresponding to a fake Boson sampler working with fully-distinguishable particles or with only two indistinguishable photons out of the three used. The test has been shown to require less data than the RNE-test in a low-complexity regime, and has proven to be a versatile and feasible alternative to pre-existing methods for the validation against non-trivial distributions.

# Acknowledgments

This work was supported by the European Research Council ERC-Starting Grant 3D-QUEST (3D-Quantum Integrated Optical Simulation; grant agreement no. 307783): http://www.3dquest.eu, by Progettó d'Ateneo SUPERCONTINUUM (Generation and characterization of supercontinuum laser sources for bio-spectroscopy and quantum optics), by PRIN (Programmi di ricerca di rilevante interesse nazionale) project AQUASIM (Advanced Quantum Simulation and Metrology) and by the Brazilian National Institute for Science and Technology of Quantum Information (INCT-IQ/CNPq).

# References

1. R. P. Feynman, Int. J. Theoretical Phys. 6 (1982) 467.  
2. S. Aaronson, Quantum Computing Since Democritus (Cambridge University Press, 2013).  
3. B. Gard et al., Phys. Rev. A 89 (2014) 022328.  
4. P. W. Shor, SIAM J. Comput. (1997).  
5. S. Aaronson and A. Arkhipov, The computational complexity of linear optics, Proceedings of the 43rd Annual ACM Symposium on Theory of Computing, San Jose (2011).  
6. L. G. Valiant, The Complexity of Computing the Permanent, Theoretical Computer Science (Elsevier, 1979).  
7. S. Aaronson and A. Arkhipov, arXiv:1109.1674 [quant-ph] (2011).  
8. E. Knill, R. Laflamme and G. J. Milburn, Nature 409 (2001) 4652.  
9. M. Broome et al., Science 339 (2013) 794.  
10. J. Spring et al., Science 339 (2013) 798.  
11. M. Tillmann et al., Nature Photon. 7 (2013) 540.  
12. A. Crespi et al., Nature Photon. 7 (2013) 545.  
13. A. Leverrier and R. García-Patron, arXiv:1309.4687 [quant-ph] (2013).  
14. P. Rohde and T. Ralph, Phys. Rev. A 85 (2012) 022332.  
15. K. Motes et al., Phys. Rev. A 88 (2013) 063822.  
16. K. Motes et al., Phys. Rev. Lett. 113 (2014) 120501.

17. M. Reck et al., Phys. Rev. Lett. 73 (1994) 58.  
18. A. Politi et al., Science 325 (2009) 1221.  
19. A. Peruzzo et al., Science 329 (2010) 1500.  
20. L. Sansoni et al., Phys. Rev. Lett. 108 (2012) 010502.  
21. B. Metcalf et al., Nature Commun. 4 (2013) 1356.  
22. A. Politi et al., Science 320 (2008) 646.  
23. R. Osellame et al., J. Opt. Soc. Am. B 20 (2003) 1559.  
24. R. Gattass and E. Mazur, Nature Photon. 2 (2008) 219.  
25. N. Spagnolo et al., Phys. Rev. Lett. 111 (2013) 130503.  
26. D. Burnham and D. Weinberg, Phys. Rev. Lett. 25 (1970) 84.  
27. P. Kwiat et al., Phys. Rev. Lett. 75 (1995) 4337.  
28. C. Gogolin et al., arXiv:1306.3995 [quant-ph] (2013).  
29. S. Aaronson and A. Arkhipov, arXiv:1309.7460 [quant-ph] (2013).  
30. T. M. Cover and J. A. Thomas, Elements of Information Theory, Chapter 12, 2nd edn. (Wiley-Interscience, 2006).  
31. N. Spagnolo et al., Nature Photon. 8 (2014) 615.  
32. J. Carolan et al., Nature Photon. 8 (2014) 621.  
33. M. Tichy et al., Phys. Rev. Lett. 113 (2014) 020502.  
34. L. Aolita et al., arXiv:1407.4817 [quant-ph] (2014).  
35. M. Walschaers et al., arXiv:1410.8547 [quant-ph] (2014).