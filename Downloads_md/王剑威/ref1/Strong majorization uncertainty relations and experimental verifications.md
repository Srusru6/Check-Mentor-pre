# ARTICLE OPEN

Check for updates

# Strong majorization uncertainty relations and experimental verifications

Yuan Yuan  $^{1,2,3}$ , Yunlong Xiao  $^{4,5}$ , Zhibo Hou  $^{2,3}$ , Shao-Ming Fei  $^{6,7}$ , Gilad Gour  $^{8,9}$ , Guo-Yong Xiang  $^{2,3}$ , Chuan-Feng Li  $^{2,3}$  and Guang-Can Guo  $^{2,3}$

In spite of enormous theoretical and experimental progress in quantum uncertainty relations, the experimental investigation of the most current, and universal formalism of uncertainty relations, namely majorization uncertainty relations (MURs), has not been implemented yet. A major problem is that previous studies of majorization uncertainty relations mainly focus on their mathematical expressions, leaving the physical interpretation of these different forms unexplored. To address this problem, we employ a guessing game formalism to reveal physical differences between diverse forms of majorization uncertainty relations. Furthermore, we tighten the bounds of MURs by using flatness processes. Finally, we experimentally verify strong MURs in the photonic system to benchmark our theoretical results.

npj Quantum Information (2023)9:65; https://doi.org/10.1038/s41534-023-00736-2

# INTRODUCTION

In the quantum world, measurements allow us to gain information from a system, and the action of measurements on quantum systems is fully embraced in the areas of quantum technologies and quantum information theories. It is therefore of great practical interest to study the limitations and precisions of quantum measurements. In taking the measurements on board, however, it appears that quantum mechanics imposes strict limitation on our ability to specify the precise outcomes from incompatible measurements simultaneously, which is known as Heisenberg uncertainty principle<sup>1</sup>.

In the context of the uncertainty principle, both variance $^{2-12}$  and entropies $^{13-45}$  are by no reason the most adequate to use. The attempt to find all suitable uncertainty measures has triggered the interest of the scientific community in the quest for a better understanding and exploitation of the precisions of quantum measurements. As previously shown in refs. $^{46,47}$ , any eligible candidate of uncertainty measures should be: (i) non-negative; (ii) a function only of the probability vector associated with the measurement outcomes; (iii) invariant under permutations; (iv) nondecreasing under a random relabeling(characterized by the convex hull of permutation matrices). According to these restrict conditions, a qualified uncertainty measure should be a non-negative Schur-concave function, and the majorization uncertainty relations (MURs) arise from the fact that all Schur-concave functions preserve the partial order induced by majorization $^{48-50}$ . Based on the mathematical expressions, the notions of MURs are classified into two categories; that are direct-product MUR (DPMUR) $^{46,51}$  and direct-sum MUR (DSMUR) $^{52,53}$ . In the original work $^{52}$ , the essential differences of mathematical features between DPMUR and DSMUR (i.e. tensor and direct-sum) are compared and analyzed. However, it is fair to say, that our understanding of the physical essences of MURs is still very limited.

In this work, our first contribution, which also reflects the original intention of this work, is to characterize the essential differences of physical features between DPMUR and DSMUR theoretically. More precisely, we show that the difference between these MURs are more than its mathematical expressions, what really matters is the joint uncertainty they represent. DPMUR is identified as a type of spatially-separated joint uncertainty, and meanwhile DSMUR is recognized as a type of temporally-separated joint uncertainty. Despite previous developments on MURs, there is still a gap between their optimal bounds and the ones constructed in refs. $^{46,51-53}$ . Our second contribution is to fill this gap by applying a technique, called the flatness process $^{54}$ , which is also known as a concave envelope in mathematics.

Besides theoretical advancements, the experimentally implementations of quantum uncertainty relations are also already of great interest. Uncertainty relations based on variance and entropies have been successfully realized in various physical systems, including neutronic systems $^{55-57}$ , optical systems $^{22,23,58-64}$ , nitrogen-vacancy centers $^{65}$ , nuclear magnetic resonance $^{66}$ , ion trap $^{67}$ , and so forth. However, an experimental demonstration of the uncertainty relations given by majorization has never been shown. To boost the experimental study of the uncertainty relations, we experimentally verified the tighter majorization uncertainty relations. Thus the third contribution of this work is that we demonstrate the MURs by measuring a qudit state encoded with the path and polarization degrees of freedom of the photon.

# RESULTS

# Direct-product majorization uncertainty relation

We employ guessing games to reveal physical differences between diverse forms of majorization uncertainty relations. The

$^{1}$ School of Physics, East China University of Science and Technology, 200237 Shanghai, China.  $^{2}$ CAS Key Laboratory of Quantum Information, University of Science and Technology of China, 230026 Hefei, China.  $^{3}$ Synergetic Innovation Center of Quantum Information and Quantum Physics, University of Science and Technology of China, 230026 Hefei, China.  $^{4}$ Institute of High Performance Computing, Agency for Science, Technology and Research (A*STAR), 1 Fusionopolis Way, #16-16 Connexis, Singapore 138632, Republic of Singapore.  $^{5}$ Nanyang Quantum Hub, School of Physical and Mathematical Sciences, Nanyang Technological University, Singapore 637371, Singapore.  $^{6}$ School of Mathematical Sciences, Capital Normal University, 100048 Beijing, China.  $^{7}$ Max Planck Institute for Mathematics in the Sciences, 04103 Leipzig, Germany.  $^{8}$ Department of Mathematics and Statistics, University of Calgary, Calgary, AB T2N 1N4, Canada.  $^{9}$ Institute for Quantum Science and Technology, University of Calgary, Calgary, AB T2N 1N4, Canada.  $^{10}$ email: mathxiao123@gmail.com; gyxiang@ustc.edu.cn

![](images/a7c19908e4b77d765427627faf778ae379adef8404a9a8ff14286a41d94c1048.jpg)  
Fig. 1 Schematic illustration of the majorization uncertainty relations in the framework of guessing games. The guessing game for the construction of DPMUR is shown in (a). Bob prepares a two-copy state  $\rho \otimes \rho$  which is unknown to Alice and sends it to Alice. Alice measures the state  $\rho \otimes \rho$  with  $M \otimes N$  and obtains a measurement outcome  $(a, b)$  with  $a = 1, \dots, n$  and  $b = 1, \dots, m$ . The state and measurements are known to Bob, so Bob knows that Alice's measurement outcome in each round is one of the  $mn$  possible outcomes. Bob's goal is to guess Alice's measurement outcome correctly in each round. Each round is independent and the process is the same, except that Bob is allowed to guess the number of measurement outcomes increasing in each round. For example, in the second round ( $k = 2$ ), Bob is allowed to guess two outcomes out of all possible outcomes (as shown in blue in the table) and will win if one of them is Alice's measurement outcome. The guessing game for the construction of DSMUR is shown in (b). Unlike the game for DPMUR, in this game, Bob prepares a one-copy state  $\rho$  and sends it to Alice. Alice measures the state  $\rho$  using either  $M$  or  $N$  depending on the outcome of a random number generator  $R$ , which outputs 0 with probability  $\lambda$  and 1 with probability  $1 - \lambda$ . Thus Alice obtains a measurement outcome  $(0, a)$  or  $(1, b)$  in each round. Bob knows Alice's measurement rules and his goal is to guess Alice's measurement outcome correctly among  $n + m$  possible outcomes. Similarly, in the  $k$ -th round, Bob is allowed to guess  $k$  outcomes out of all possible outcomes and will win if one of them is Alice's measurement outcome.

guessing game for the construction of DPMUR is shown in Fig. 1a. In each round of the game, Bob prepares a two-copy state  $\rho \otimes \rho$  and sends it to Alice (the state is unknown to Alice). Alice measures the state  $\rho \otimes \rho$  with  $M \otimes N$  (the measurement is known to Bob), and  $M, N$  is positive-operator-valued measures (POVMs) composed of  $m$  POVM elements and  $n$  POVM elements, denoted as  $M = \{M_a\}_a (a = 1, \dots, n)$  and  $N = \{N_b\}_b (b = 1, \dots, m)$  respectively. Then Alice obtains a measurement outcome labeled as  $(a, b)$ , which has  $mn$  possible results, as shown in the table in Fig. 1a, where  $a$  denotes the outcome of  $M$  and  $b$  denotes the outcome of  $N$ . Alice obtains a measurement outcome  $(a, b)$  in each round, and Bob's goal is to guess Alice's measurement outcome correctly in each round. Each round is independent, and only the number of measurement outcomes that Bob is allowed to guess increases in each round.

In the first round of the game, Bob is allowed to guess only one possible measurement outcome, and he will win if he guesses correctly. In the  $k$ -th round of the game, Bob is allowed to guess  $k$  possible measurement outcomes, he will win if one of his guesses is Alice's measurement outcome. It can be seen that this game can play up to  $k = nm$  rounds. It is important to highlight that Bob possesses information about the state and measurements Alice will implement during the game. Therefore, Bob has prior information on the possible measurement outcomes and can directly guess the measurement outcome that occurs with the maximum probability. Moreover, since Bob is the party sending the states, he can maximize the probability of winning in each round by sending the particular states. For example, in the first round, the maximum probability for Bob to win is  $\max_{\rho} p_a q_b$ , where the probabilities  $p_a$  and  $p_b$  are written as  $p_a := \operatorname{Tr}(M_a \rho)$  and  $q_b := \operatorname{Tr}(N_b \rho)$ . In the second round, according to the rules, Bob is allowed to guess two outcomes simultaneously and will win if one of his guesses is Alice's measurement outcome. He chooses the two outcomes that occur with the maximum sum of probabilities among all possible outcomes. So the maximum probability for Bob to win in the second round is  $\max_{a,b \in I_2} \sum_{p_a q_b} p_a q_b$ , where  $I_2$  represents the set composed of selecting two outcomes from  $mn$  possible measurement outcomes. Thus in the  $k$ -th round, the

maximum probability for Bob to win can be expressed as

$$
R _ {k} := \max  _ {l _ {k}} \max  _ {\rho} \sum_ {(a, b) \in l _ {k}} p _ {a} q _ {b}, \tag {1}
$$

where  $I_{k} \subset [n] \times [m]$  is a subset of  $k$  distinct pair of indices. Here  $[n] = \{1, \dots, n\}$  is the set of natural numbers ranging from 1 to  $n$ , and  $k \in [mn]$ . According to Eq. (1), it is easy to obtain the following inequalities

$$
\sum_ {(a, b) \in I _ {k}} p _ {a} q _ {b} \leqslant R _ {k}. \quad \forall k \in [ m n ] \tag {2}
$$

A concise approach of expressing the inequalities mentioned above is to use the majorization  $(\prec)^{50}$ ; A probability vector  $\mathbf{x} \in \mathbb{R}^n$  is majorized by  $\mathbf{y} \in \mathbb{R}^n$ , i.e.  $\mathbf{x} < \mathbf{y}$ , if and only if  $\sum_{j=1}^{k} x_j^{\downarrow} \leqslant \sum_{j=1}^{k} y_j^{\downarrow}$  for all  $1 \leqslant k \leqslant n-1$ . Here the down-arrow indicates that the components of the vectors are arranged in a non-increasing order. We write the probability distributions  $p_a$  and  $p_b$  of all results for  $M$  and  $N$  as probability vectors  $\mathbf{p}$  and  $\mathbf{q}$ , respectively. Clearly, the joint uncertainty between  $\mathbf{p}$  and  $\mathbf{q}$  is captured by the maximum probability for Bob to win the game. Now we can abbreviate the Eq. (2) into one inequality

$$
\mathbf {p} \otimes \mathbf {q} \prec r, \tag {3}
$$

with  $\pmb{r} := (R_1, R_2 - R_1, \dots, R_{mn} - R_{mn-1})$ . Consequently, the essence of DPMUR is captured by our framework of guessing game, which demonstrates a spatially-separated joint uncertainty. Note that  $R_k$  can be in general difficult to calculate explicitly, as they involve an optimization problem. The authors of ref. [46] provide us a calculate-friendly bound  $\pmb{t}$ , satisfying  $\mathbf{p} \otimes \mathbf{q} < r < \pmb{t}$ . However, this is not the optimal bound. Mathematically, majorization lattice forms a complete lattice; the optimal bounds for MURs exist. To obtain the optimal bounds, it suffices to perform a standard process (flatness process)  $\mathcal{F}$ . Hence, the implementation of the process  $\mathcal{F}$  on  $\mathbf{p} \otimes \mathbf{q} < r < \pmb{t}$  leads to a relation

$$
\mathbf {p} \otimes \mathbf {q} \prec \mathcal {F} (\boldsymbol {r}) \prec \boldsymbol {r} \prec \mathcal {F} (\boldsymbol {t}) \prec \boldsymbol {t}, \tag {4}
$$

where  $\mathbf{r}$  and  $\mathbf{t}$  are the bounds given in ref. 46. Because of the mathematical properties of flatness process (concave envelope), the vector  $\mathcal{F}(\mathbf{r})$  is optimal. However, a major drawback of  $\mathcal{F}(\mathbf{r})$  is

![](images/4424b2a00d930af3396d19a04e10e7bff94563609b252b2b7f46a4f03d592582.jpg)  
Fig. 2 Experimental setup. In the single-photon source module, the photon pairs generated in spontaneous parametric down-conversion are coupled into single-mode fibers separately. One photon is detected by a single-photon detector (SPD) acting as a trigger. In the state preparation module, a qudit is encoded by four modes of the single photon. H and V denote the horizontal polarization and vertical polarization of the photon, respectively. The subscripts u and d represent the upper and lower spatial modes of the photon, respectively. The half-wave plates  $(\mathsf{H}_1,\mathsf{H}_2)$  and beam displacer (BD1) are used to generate desired qudit state. In the measurement module a, b, the red HWPs with an angle of  $45^{\circ}$  and beam displacers (BDs) comprise the interferometric network to perform the desired measurement; the yellow HWP with an angle of  $0^{\circ}$  are inserted into the middle path to compensate the optical path difference between the upper and lower spatial modes. To realize measurement B shown in Eq. (10), two quarter-wave plates are need to be inserted in device b. Four SPDs correspond to the four outcomes of each measurement. Each SPD is a silicon avalanche photodiode (Si-APD), with a detection efficiency of  $\sim 60\%$ .

![](images/46f4b363b397ab8685f9796eab4c44522e9238a08dd112269d3533ae0ad686ab.jpg)

that the calculation of  $\mathcal{F}(\pmb{r})$  is even harder than  $\pmb{r}$ . But with the help of flatness process, we also obtain an effectively computable bound  $\mathcal{F}(\pmb{t})$ , which is tighter than the original  $\pmb{t}$ . So we obtain a strong DPMUR  $\mathbf{p} \otimes \mathbf{q} \prec \mathcal{F}(\pmb{t}) \prec \pmb{t}$ , and we test this relation experimentally. The construction of  $\pmb{t}$  and the rigorous definition of the flatness process see Supplementary Note 1 for details.

# Direct-sum majorization uncertainty relation

Demonstration of direct-sum majorization uncertainty relation (DSMUR) through the framework of the guessing game is shown in Fig. 1b. In each round of the game, Bob prepares a one-copy state  $\rho$  and sends it to Alice(the state is unknown to Alice). Alice measures the state  $\rho$  with  $M$  or  $N$ . To determine Alice's choice of the measurements, a binary random number generator  $R$  is employed, which outputs the number 0 with probability  $\lambda$ , and the number 1 with probability  $1 - \lambda$ . After receiving 0 from  $R$ , Alice performs the measurement  $M$  and obtains a measurement outcome labeled as  $(0,a)$ , where  $a \in \{1,\dots,n\}$ . Otherwise, she implements  $N$  and obtains a measurement outcome labeled as  $(1,b)$ , where  $b \in \{1,\dots,m\}$ .  $n + m$  possible results  $\{(0,a),(1,b)\}$  are shown in the table in Fig. 1b. Thus Alice obtains a measurement outcome  $(0,a)$  or  $(1,b)$  in each round. Bob knows Alice's measurement rules and the specific form of measurements  $M$  and  $N$ , but he does not know whether Alice performs measurement  $M$  or  $N$  in each round. So he needs to guess Alice's outcome among all possible results.

Same as the previous game for DPMUR, again the goal of Bob is to guess Alice's measurement outcome correctly in each round. Each round is independent, and the number of measurement outcomes that Bob is allowed to guess increases in each round. In the  $k$ -th round of the game, Bob is allowed to guess  $k$  possible measurement outcomes, and he will win if one of his guesses is Alice's measurement outcome. This means that the game can be played up to  $k = n + m$  rounds. Bob's strategy is similar to the previous one. Thus the maximal probability for Bob to win in each round is

round is given by

$$
\begin{array}{l} S _ {k} := \max  _ {| I | + | J | = k} \max  _ {\rho} \sum_ {a \in I \subset [ n ]} (\lambda p _ {a} + (1 - \lambda) q _ {b}) \tag {5} \\ \boldsymbol {b} \in J \subset [ m ] \\ \end{array}
$$

where  $|\cdot|$  denotes the cardinality of  $\cdot$ . There exists an efficient way of computing  $S_{k}$ . Let us define an operator  $G_{c}$  as

$$
G _ {c} (\lambda) := \left\{ \begin{array}{l l} \lambda M _ {c} & 1 \leqslant c \leqslant n, \\ (1 - \lambda) N _ {c - n} & n + 1 \leqslant c \leqslant n + m. \end{array} \right. \tag {6}
$$

Then the quantity  $S_{k}$  becomes

$$
S _ {k} (\lambda) = \max  _ {| I | = k} \lambda_ {1} \left(\sum_ {c \in I \subset [ n + m ]} G _ {c} (\lambda)\right), \tag {7}
$$

where  $\lambda_{1}(\bullet)$  denotes the maximum eigenvalue of the argument. Similarly, we write the relationship between the uncertainty of measurements and Bob's maximum probability of winning the game as the following inequality by using majorization

$$
\lambda \mathbf {p} \oplus (1 - \lambda) \mathbf {q} \prec s (\lambda), \tag {8}
$$

with  $\pmb{s}(\lambda) \coloneqq (S_1(\lambda), S_2(\lambda) - S_1(\lambda), \dots, S_{m+n}(\lambda) - S_{m+n-1}(\lambda))$ . In the framework of DSMUR, classical uncertainty of the random number generator is injected into the guessing game, and as a consequence  $\lambda \pmb{p} \oplus (1 - \lambda) \pmb{q}$  is a hybrid type of uncertainty, mingling both classical and quantum uncertainties. Quite remarkably, the measurements, monitored by  $R$ , can be implemented in the same position but cannot performed simultaneously, and hence  $\lambda \pmb{p} \oplus (1 - \lambda) \pmb{q}$  reveals a temporally-separated joint uncertainty. It should be stressed here that the original DSMUR<sup>52,53</sup> is a special case of our notion by first taking  $\lambda = 1/2$ , and then timing the scalar 2, i.e.  $\pmb{p} \oplus \pmb{q} \prec 2\pmb{s}(1/2)$ .

Let us now consider the DSMUR after flatness process

$$
\lambda \mathbf {p} \oplus (1 - \lambda) \mathbf {q} \prec \mathcal {F} (\mathbf {s} (\lambda)) \prec \mathbf {s} (\lambda). \tag {9}
$$

Unlike the case of DPMUR, the vector  $\mathcal{F}(\pmb {s}(\lambda))$  is optimal and can be calculate explicitly. Moreover, for DSMUR with uniform

![](images/76ff88c2481f2c867d22439c0936d2d24030bb877552232ecccdb9fb9bb74ecc.jpg)

![](images/f297019320bb21965174aa1831c097759425b56982eeba782ecad481cc5474c4.jpg)

![](images/baadf7da6c5a7d9c3dc89d37f7e91c09a4de85ec5dc94ac1749c780035fe3789.jpg)  
Fig. 3 Experimental results of DPMUR and DSMUR with two measurements. Lorenz curves in (a) and (b) show the experimental results for DPMUR and DSMUR with states  $|\psi_{\pi /4,\phi}\rangle$ , and the Lorenz curves in (c) and (d) exhibit DPMUR and DSMUR with states  $|\psi_{\theta ,\pi /4}\rangle$ . Black curves represent the Lorenz curves of previous bounds  $\pmb{t}$  ( $\pmb{s}(1/2)$ ), and the Lorenz curves of our improved bounds  $\mathcal{F}(\pmb{t})$  ( $\mathcal{F}(\pmb{s}(1/2))$ ) are highlighted in red. The dotted lines marked with different colors indicate DPMUR and DSMUR for the state in different parameters. Since the Lorentz curve is plotted by a series of coordinate points  $\{(k,\sum_{i=1}^{k}x_{i})_{k=0}^{n}\}$ , the coordinate axis is not marked with a title. Note that for the measurement and state we choose in the four-dimensional Hilbert space,  $n = 16$  for DPMUR and  $n = 8$  for DSMUR.

![](images/4767138ec165f2279be26b63b4379fe3c4db2e0cf9f8db971aad71cfe28a4347.jpg)

distribution, i.e.  $\lambda = 1/2$ , one can easily show that  $\mathbf{p} \oplus \mathbf{q} \prec 2\mathcal{F}(\mathbf{s}(1/2)) \prec 2\mathbf{s}(1/2)$ . Note that, the flatness process cannot be applied to  $\mathbf{p} \oplus \mathbf{q} \prec 2\mathbf{s}(1/2)$  directly<sup>40,41</sup>, since the results presented in ref. <sup>54</sup> are only designed for probabilities. To accommodate this, a more general lemma is proved in Supplementary Note 3.

# Experimental demonstration

To verify the DPMUR and DSMUR, we experimentally prepare a family of 4-dimensional states with parameters  $\theta$  and  $\phi$ ,  $|\psi_{\theta,\phi}\rangle = \cos\theta\sin\phi|0\rangle + \cos\theta\cos\phi|1\rangle + \sin\theta|2\rangle + 0|3\rangle$ , and perform measurements in the photonic system. Measurements include a setting with a pair of measurements

$$
A = \{\left| 0 \right\rangle , \left| 1 \right\rangle , \left| 2 \right\rangle , \left| 3 \right\rangle \}
$$

$$
\left. \right. \quad \left\{\left(| 0 \rangle - i | 1 \rangle - i | 2 \rangle + | 3 \rangle\right) / 2, \left(| 0 \rangle - i | 1 \rangle + i | 2 \rangle - | 3 \rangle\right) / 2, \right.
$$

$$
B = \left(| 0 \rangle + i | 1 \rangle - i | 2 \rangle - | 3 \rangle\right) / 2, \left(| 0 \rangle + i | 1 \rangle + i | 2 \rangle + | 3 \rangle\right) / 2 \}
$$

(10)

and another one with multi-measurements

$$
C _ {1} = \{\left| 0 \right\rangle , \left| 1 \right\rangle , \left| 2 \right\rangle , \left| 3 \right\rangle \}
$$

$$
C _ {2} = \left\{| 0 \rangle , \frac {| 2 \rangle + | 3 \rangle}{\sqrt {2}}, \frac {| 1 \rangle + | 2 \rangle - | 3 \rangle}{\sqrt {3}}, \frac {2 | 1 \rangle - | 2 \rangle + | 3 \rangle}{\sqrt {6}} \right\} \tag {11}
$$

$$
C _ {3} = \left\{\frac {| 2 \rangle + | 3 \rangle}{\sqrt {2}}, | 1 \rangle , \frac {| 0 \rangle + | 2 \rangle - | 3 \rangle}{\sqrt {3}}, \frac {| 2 | 0 \rangle - | 2 \rangle + | 3 \rangle}{\sqrt {6}} \right\}.
$$

The experimental setup is shown in Fig. 2. It consists of a single-photon source module, a state-preparation module, and a

measurement module. The details of each module are presented in the Methods section.

The probability distributions induced by performing measurements (10) and (11) on state  $\left|\psi_{\theta, \phi}\right\rangle$  are acquired. Since we need to verify the majorization relation between vectors composed of probability distributions, so we use Lorentz curve to show it more intuitively<sup>50</sup>. For an non-negative vector  $\mathbf{x} = (x_i)_{i=1}^n$  with nonincreasing order, the corresponding Lorenz curve  $\mathcal{L}(\mathbf{x})$  is defined as the linear interpolation of the points  $\{(k, \sum_{i=1}^k x_i)_{k=0}^n\}$  with the convention  $(0, 0)$  for  $k = 0$ . Based on Lorenz curves, we have  $\mathcal{L}(\mathbf{x})$  lays everywhere below  $\mathcal{L}(\mathbf{y})$  if and only if  $\mathbf{x} < \mathbf{y}$ . Therefore, we convert the probability vectors  $\mathbf{p} \otimes \mathbf{q}$  and  $\mathbf{p} \oplus \mathbf{q}$  into Lorentz curves  $\mathcal{L}(\mathbf{p} \otimes \mathbf{q})$  and  $\mathcal{L}(\mathbf{p} \oplus \mathbf{q})$ , and then compare them with the Lorentz curves of bounds of majorization uncertainty relations.

Experimental results for verifying the DPMUR and DSMUR with two measurements are shown in Fig. 3. Figure 3a, b show the Lorentz curves of probability vectors for DPMUR and DSMUR by measuring the states  $|\psi_{\pi /4,\phi}\rangle$ , respectively. Figure 3c, d show the Lorenz curves of probability vectors for DPMUR and DSMUR with states  $|\psi_{\theta ,\pi /4}\rangle$ , respectively. For measurements  $A$  and  $B$ , the bound  $\pmb{t}$  for DPMUR, introduced in refs.  $^{46,51}$ , is given by (0.5625, 0.1661, 0.2714). The corresponding Lorenz curve  $\mathcal{L}(\mathbf{t})$  is shown as black curve in Fig. 3a, c. To further improve previous result on DPMUR, we apply the flatness process  $\mathcal{F}$  to the bound  $\pmb{t}$ , and acquire a strong bound  $\mathcal{F}(\pmb {t}) = (0.5625,0.21875,0.21875)$ . The corresponding Lorenz curve  $\mathcal{L}(\mathcal{F}(\pmb {t}))$  is shown as red curve in Fig. 3a, c. According to the rules of the flatness process, the second and third elements of  $\pmb{t}$  are not arranged in descending

![](images/a8c06b2510b75dcef609063c0296e3cae20649aa98dd20d6a27c743ed6780d50.jpg)

![](images/d67d5c035670d01c181f39aead127d4a721480b3aebf1f26dbf8107502144b51.jpg)

![](images/6ecf142e645f4da1b4956a82f8ad9859a9c0c19ca9ba1d379b74f51dcd5d46ba.jpg)  
Fig. 4 Experimental results of DPMUR and DSMUR with three measurements. a, b show the Lorenz curves of probability vectors for DPMUR and DSMUR with states  $|\psi_{\pi,\phi}\rangle$ , respectively. The Lorentz curves of the bounds  $\mathcal{F}(\mathbf{t}')$  and  $\mathcal{F}(\mathbf{s}'(1/3))$  are shown in black curve. c, d show the Shannon entropic uncertainty relations by performing measurements  $C_1, C_2, C_3$  on the states  $|\psi_{\pi,\phi}\rangle$  and  $|\psi_{\theta,\pi/2}\rangle$ , respectively. The curves marked with magenta, green, and blue stand for the Shannon entropy of probability distributions associated with measurements  $C_1, C_2$  and  $C_3$ ; that are  $H(C_1)$ ,  $H(C_2)$  and  $H(C_3)$ , and the red curves represent their sum of uncertainties  $\sum_i H(C_i)$ . The dotted line  $(H(\mathcal{F}(\mathbf{t}')) = 0.7651)$  and solid line  $(H(3\mathcal{F}(\mathbf{s}'(1/3))) = 0.7979)$  show the Shannon entropy of bounds for DPMUR and DSMUR.

![](images/1ab7bcf7b9c42803131c7003af67d299f57dc194330d82f74d4a886dd20b321e.jpg)

order, so the first element of  $\mathcal{F}(\pmb{t})$  is still the first element of  $\pmb{t}$ , and the average of the second and third elements of  $\pmb{t}$  is taken as the second and third elements of  $\mathcal{F}(\pmb{t})$ . Similarly, the bound  $2s(1/2)$  for DSMUR, introduced in ref. [52], is given by (0.5, 0.2071, 0.2929). After flatness process, the improved bound  $\mathcal{F}(s(1/2)) = (0.5, 0.25, 0.25)$  is obtained. The Lorentz curve of improved bound is shown as a red curve, and as a comparison, the Lorentz curve of previous bound as a black curve in Fig. 3b, d. The experimental plots depicted in Fig. 3 confirm the betterments of our bounds by showing that all experimental datum-induced Lorenz curves lay below our bounds  $\mathcal{F}(\pmb{t})$  ( $\mathcal{F}(s(1/2))$ ), and our bounds are under the previous ones  $\pmb{t}$  ( $\pmb{s}(1/2)$ ), which implies that our bound is tighter.

We also verify the DPMUR and DSMUR with three measurements, and the experimental results are shown in Fig. 4. Figure 4a, b show the Lorentz curves of probability vectors for DPMUR and DSMUR by performing measurements (11) on the states  $|\psi_{\pi ,\phi}\rangle$  respectively. For measurements  $C_1,C_2$  and  $C_3,$  the bound  $\mathcal{F}(\pmb {t}^{\prime})$  for DPMUR is given by (0.7773, 0.2227) and the bound  $\mathcal{F}(\pmb {s}'(1 / 3))$  for DSMUR is given by (1, 1, 0.7583, 0.2417)/3, and the Lorenz curves of these bounds marked in black are shown in Fig. 4a, b. We see that the joint uncertainties associated with different parameters  $\phi$  of the states  $|\psi_{\pi ,\phi}\rangle$  are marjorized by our bounds  $\mathcal{F}(\pmb {t}^{\prime})$  and  $\mathcal{F}(\pmb {s}'(1 / 3))$  . Furthermore, entropies are important tools in quantum information theory, and they are closely related to the majorization. From the properties of majorization, it follows the entropic uncertainty relations  $\sum_iH(C_i)\geqslant H(\mathcal{F}(\pmb {t}'))$  and

$\sum_{i}H(C_{i})\geqslant H(3\mathcal{F}(\pmb {s}'(1 / 3)))$  with  $H$  stands for the Shannon entropy. All of this can be seen in Fig. 4c, d.

# DISCUSSION

Our guessing game formalism of MURs enable us to classify DPMUR and DSMUR into spatially-separated and temporally-separated joint uncertainties accordingly, which differs from previous developments and, more important, exhibit the essential differences of physical features between DPMUR and DSMUR theoretically. We also experimentally verify strong MURs in the photonic system. In order to present the majorization relation, we use Lorentz curve to show it more intuitively. The experimental data are in good agreement with the theoretical prediction. The errors in our experiment mainly come from the inaccuracy of angles of the wave plates and the imperfect interference visibility of the interferometer. Furthermore, it is advantageous to apply the techniques of flatness process to tighter the bounds of MURs, and its efficiency is confirmed by our experiment. The existence of MURs provides tremendous flexibility in formulating uncertainty relations, and greatly enhance our understanding of quantum mechanics. Therefore, the guessing game formalism, and tighter bounds, as well as the corresponding experimental investigation presented in this work would deeper our knowledge of the quantum world.

# METHODS

# Experimental setup

The experimental setup used for verifications of DPMUR and DSMUR is shown in Fig. 2. It consists of a single-photon source module, a state-preparation module, and a measurement module. We will introduce the details of each module in this section.

In the single-photon source module, a 80-mW cw laser with a 404-nm wavelength (linewidth = 5 MHz) pumps a type-II beamlike phase-matching beta-barium-borate (BBO,  $6.0 \times 6.0 \times 2.0 \mathrm{~mm}^3$ ,  $\theta = 40.98^\circ$ ) crystal to produce a pair of photons with wavelength  $\lambda = 808 \mathrm{~nm}$ . After being redirected by mirrors and passing through the interference filters (IF,  $\Delta \lambda = 3 \mathrm{~nm}$ ,  $\lambda = 808 \mathrm{~nm}$ ), the photon pairs generated in spontaneous parametric down-conversion are coupled into single-mode fibers separately. One photon is detected by a single-photon detector acting as a trigger. The coincidence counts are approximately  $5 \times 10^3$  per second.

In the state preparation module, we prepare a family of 4-dimensional states with parameters  $\theta$  and  $\phi$ ,  $|\psi_{\theta,\phi}\rangle = \cos\theta \sin\phi|0\rangle + \cos\theta \cos\phi|1\rangle + \sin\theta|2\rangle + 0|3\rangle$ , which is encoded by four modes of a single photon. States  $|0\rangle$  and  $|1\rangle$  are encoded by different polarizations of the photon in the lower mode, and  $|2\rangle$  and  $|3\rangle$  are encoded by polarization of the photon in the upper mode. The beam displacer (BD) causes the vertical polarized photons to be transmitted directly, and the horizontal polarized photons to undergo a 4 mm lateral displacement. When the photon passes through a half-wave plate ( $H_1$ ) with a certain setting angle, it is split by BD1 into two parallel spatial modes—upper and lower modes. Therefore the photon is prepared in the desired state  $|\psi_{\theta,\phi}\rangle$ , with parameters  $\theta$  and  $\phi$  are controlled by the plates  $H_1$  and  $H_2$ , respectively.

In the measurement module, device a is used to realize measurements  $A$  and  $C_1$ . In the presence of quarter-wave plates with an angle of  $45^\circ$ , device b is used to realize measurement  $B$ , and the setting angles of  $H_3 - H_6$  are  $45^\circ$ ,  $0^\circ$ ,  $22.5^\circ$ , and  $22.5^\circ$ . On the other hand, in the absence of quarter-wave plates, device b is exploited to implement measurement  $C_2(C_3)$  when the setting angles of  $H_3 - H_6$  are  $22.5^\circ$ ,  $0^\circ (45^\circ)$ ,  $27.4^\circ$ , and  $0^\circ$ .

# DATA AVAILABILITY

All data not included in the paper and its Supplementary Information are available upon reasonable request from the corresponding authors.

Received: 7 February 2023; Accepted: 21 June 2023; Published online: 08 July 2023

# REFERENCES

1. Heisenberg, W. Über den anschaulichen inhalt der quantentheoretischen kinematik und mechanik. Z. Phys. 43, 172-198 (1927).  
2. Kennard, E. H. Zur quantenmechanik einfacher bewegungstypen. Z. Phys. 44, 326-352 (1927).  
3. Weyl, H. Gruppentheorie und quantenmechanik. Z. Phys. 46, 1-46 (1927).  
4. Robertson, H. P. The uncertainty principle. Phys. Rev. 34, 163 (1929).  
5. Huang, Y. Variance-based uncertainty relations. Phys. Rev. A 86, 024101 (2012).  
6. Maccone, L. & Pati, A. K. Stronger uncertainty relations for all incompatible observables. Phys. Rev. Lett. 113, 260401 (2014).  
7. Xiao, Y., Jing, N., Li-Jost, X. & Fei, S.-M. Weighted uncertainty relations. Sci. Rep. 6, 23201 (2016).  
8. Xiao, Y. & Jing, N. Mutually exclusive uncertainty relations. Sci. Rep. 6, 36616 (2016).  
9. Xiao, Y., Jing, N., Yu, B., Fei, S.-M. & Li-Jost, X. Near-optimal variance-based uncertainty relations. Front. Phys. 10, 846330 (2022).  
10. de Guise, H., Maccone, L., Sanders, B. C. & Shukla, N. State-independent uncertainty relations. Phys. Rev. A 98, 042121 (2018).  
11. Chen, Z.-X., Wang, H., Li, J.-L., Song, Q.-C. & Qiao, C.-F. Tight  $N$ -observable uncertainty relations and their experimental demonstrations. Sci. Rep. 9, 5687 (2019).

12. Xiao, Y., Guo, C., Meng, F., Jing, N. & Yung, M.-H. Incompatibility of observables as state-independent bound of uncertainty relations. Phys. Rev. A 100, 032118 (2019).  
13. Deutsch, D. Uncertainty in quantum measurements. Phys. Rev. Lett. 50, 631 (1983).  
14. Partovi, M. H. Entropic formulation of uncertainty for quantum measurements. Phys. Rev. Lett. 50, 1883 (1983).  
15. Kraus, K. Complementary observables and uncertainty relations. Phys. Rev. D 35, 3070 (1987).  
16. Maassen, H. & Uffink, J. B. M. Generalized entropic uncertainty relations. Phys. Rev. Lett. 60, 1103 (1988).  
17. Ivanovic, I. D. An inequality for the sum of entropies of unbiased quantum measurements. J. Phys. A Math. Gen. 25, L363 (1992).  
18. Sánchez, J. Entropic uncertainty and certainty relations for complementary observables. Phys. Lett. A 173, 233-239 (1993).  
19. Ballester, M. A. & Wehner, S. Entropic uncertainty relations and locking: tight bounds for mutually unbiased bases. Phys. Rev. A 75, 022319 (2007).  
20. Wu, S., Yu, S. & Mølmer, K. Entropic uncertainty relation for mutually unbiased bases. Phys. Rev. A 79, 022104 (2009).  
21. Berta, M., Christandl, M., Colbeck, R., Renes, J. M. & Renner, R. The uncertainty principle in the presence of quantum memory. Nat. Phys. 6, 659-662 (2010).  
22. Li, C.-F., Xu, J.-S., Xu, X.-Y., Li, K. & Guo, G.-C. Experimental investigation of the entanglement-assisted entropic uncertainty principle. Nat. Phys. 7, 752-756 (2011).  
23. Prevedel, R., Hamel, D. R., Colbeck, R., Fisher, K. & Resch, K. J. Experimental investigation of the uncertainty principle in the presence of quantum memory and its application to witnessing entanglement. Nat. Phys. 7, 757-761 (2011).  
24. Huang, Y. Entropic uncertainty relations in multidimensional position and momentum spaces. Phys. Rev. A 83, 052124 (2011).  
25. Tomamichel, M. & Renner, R. Uncertainty relation for smooth entropies. Phys. Rev. Lett. 106, 110506 (2011).  
26. Coles, P. J., Colbeck, R., Yu, L. & Zwolak, M. Uncertainty relations from simple entropic properties. Phys. Rev. Lett. 108, 210405 (2012).  
27. Coles, P. J. & Piani, M. Improved entropic uncertainty relations and information exclusion relations. Phys. Rev. A 89, 022112 (2014).  
28. Kaniewski, J., Tomamichel, M. & Wehner, S. Entropic uncertainty from effective anticommutators. Phys. Rev. A 90, 012332 (2014).  
29. Furrer, F., Berta, M., Tomamichel, M., Scholz, V. B. & Christandl, M. Position-momentum uncertainty relations in the presence of quantum memory. J. Math. Phys. 55, 122205 (2014).  
30. Li, J.-L. & Qiao, C.-F. Reformulating the quantum uncertainty relation. Sci. Rep. 5, 12708 (2015).  
31. Berta, M., Wehner, S. & Wilde, M. M. Entropic uncertainty and measurement reversibility. New J. Phys. 18, 073004 (2016).  
32. Xiao, Y. et al. Strong entropic uncertainty relations for multiple measurements. Phys. Rev. A 93, 042125 (2016).  
33. Xiao, Y., Jing, N., Fei, S.-M. & Li-Jost, X. Improved uncertainty relation in the presence of quantum memory. J. Phys. A Math. Theor. 49, 49LT01 (2016).  
34. Xiao, Y., Jing, N. & Li-Jost, X. Uncertainty under quantum measures and quantum memory. Quantum Inf. Process. 16, 104 (2017).  
35. Coles, P. J., Berta, M., Tomamichel, M. & Wehner, S. Entropic uncertainty relations and their applications. Rev. Mod. Phys. 89, 015002 (2017).  
36. Huang, J.-L., Gan, W.-C., Xiao, Y., Shu, F.-W. & Yung, M.-H. Holevo bound of entropic uncertainty in Schwarzschild spacetime. Eur. Phys. J. C 78, 545 (2018).  
37. Xiao, Y., Xiang, Y., He, Q. & Sanders, B. C. Quasi-fine-grained uncertainty relations. New J. Phys. 22, 073063 (2022).  
38. Chen, Z., Ma, Z., Xiao, Y. & Fei, S.-M. Improved quantum entropic uncertainty relations. Phys. Rev. A 98, 042305 (2018).  
39. Coles, P. J., Katariya, V., Lloyd, S., Marvian, I. & Wilde, M. M. Entropic energy-time uncertainty relation. Phys. Rev. Lett. 122, 100401 (2019).  
40. Li, J.-L. & Qiao, C.-F. Quantum uncertainty relation: the optimal uncertainty relation. Ann. Phys. 531, 1970036 (2019).  
41. Wang, H., Li, J.-L., Wang, S., Song, Q.-C. & Qiao, C.-F. Experimental investigation of the uncertainty relations with coherent light. Quantum Inf. Process. 19, 38 (2019).  
42. Xiao, Y., Fang, K. & Gour, G. The complementary information principle of quantum mechanics. Preprint at https://doi.org/10.48550/arXiv.1908.07694 (2019).  
43. Qian, C., Wu, Y.-D., Ji, J.-W., Xiao, Y. & Sanders, B. C. Multiple uncertainty relation for accelerated quantum information. Phys. Rev. D 102, 096009 (2020).  
44. Xiao, Y., Sengupta, K., Yang, S. & Gour, G. Uncertainty principle of quantum processes. Phys. Rev. Res. 3, 023077 (2021).  
45. Xiao, Y. A Framework for Uncertainty Relations. PhD thesis, Universität Leipzig (2017).  
46. Friedland, S., Gheorghiu, V. & Gour, G. Universal uncertainty relations. Phys. Rev. Lett. 111, 230401 (2013).

47. Narasimhachar, V., Poostindouz, A. & Gour, G. Uncertainty, joint uncertainty, and the quantum uncertainty principle. New J. Phys. 18, 033019 (2016).  
48. Hardy, G. H., Littlewood, J. E. & Polya, G. Some simple inequalities satisfied by convex functions. Messenger Math. 58, 145-152 (1929).  
49. Partovi, M. H. Majorization formulation of uncertainty in quantum mechanics. Phys. Rev. A 84, 052117 (2011).  
50. Marshall, A. W., Olkin, I. & Arnold, B. C. in Inequalities: Theory of Majorization and Its Applications 2nd edn 18-19 (Springer, 2011).  
51. Puchala, Z., Rudnicki, L. & Žyczkowski, K. Majorization entropic uncertainty relations. J. Phys. A Math. Theor. 46, 272002 (2013).  
52. Rudnicki, L., Puchala, Z. & Žyczkowski, K. Strong majorization entropic uncertainty relations. Phys. Rev. A 89, 052115 (2014).  
53. Puchala, Z., Rudnicki, L., Krawiec, A. & Žyczkowski, K. Majorization uncertainty relations for mixed quantum states. J. Phys. A Math. Theor. 51, 175306 (2018).  
54. Cicalese, F. & Vaccaro, U. Supermodularity and subadditivity properties of the entropy on the majorization lattice. IEEE Trans. Inf. Theory 48, 933-938 (2002).  
55. Erhart, J. et al. Experimental demonstration of a universally valid error-disturbance uncertainty relation in spin measurements. Nat. Phys. 8, 185-189 (2012).  
56. Sulyok, G. et al. Violation of Heisenberg's error-disturbance uncertainty relation in neutron-spin measurements. Phys. Rev. A 88, 022110 (2013).  
57. Sulyok, G. et al. Experimental test of entropic noise-disturbance uncertainty relations for spin-1/2 measurements. Phys. Rev. Lett. 115, 030401 (2015).  
58. Rozema, L. A. et al. Violation of Heisenberg's measurement-disturbance relationship by weak measurements. Phys. Rev. Lett. 109, 100404 (2012).  
59. Ringbauer, M. et al. Experimental joint quantum measurements with minimum uncertainty. Phys. Rev. Lett. 112, 020401 (2014).  
60. Kaneda, F., Baek, S.-Y., Ozawa, M. & Edamatsu, K. Experimental test of error-disturbance uncertainty relations by weak measurement. Phys. Rev. Lett. 112, 020402 (2014).  
61. Wang, K. et al. Experimental investigation of the stronger uncertainty relations for all incompatible observables. Phys. Rev. A 93, 052108 (2016).  
62. Zhao, Y.-Y., Kurzyński, P., Xiang, G.-Y., Li, C.-F. & Guo, G.-C. Heisenberg's error-disturbance relations: a joint measurement-based experimental test. Phys. Rev. A 95, 040101(R) (2017).  
63. Liu, Y. et al. Experimental test of error-tradeoff uncertainty relation using a continuous-variable entangled state. npj Quantum Inf. 5, 68 (2019).  
64. Liu, Y., Kang, H., Han, D., Su, X. & Peng, K. Experimental test of error-disturbance uncertainty relation with continuous variables. Photon. Res. 7, A56-A60 (2019).  
65. Ma, W. et al. Experimental demonstration of uncertainty relations for the triple components of angular momentum. Phys. Rev. Lett. 118, 180402 (2017).  
66. Ma, W. et al. Experimental test of Heisenberg's measurement uncertainty relation based on statistical distances. Phys. Rev. Lett. 116, 160405 (2016).  
67. Zhou, F. et al. Verifying Heisenbergs error-disturbance relation using a single trapped ion. Sci. Adv. 2, e1600578 (2016).

# ACKNOWLEDGEMENTS

This work is supported by the National Natural Science Foundation of China (Grants Nos. 12004113, 62222512, 12104439, 12134014, 61905234, 11974335) and Natural Science Foundation of Shanghai (22ZR1418100). Y.X. is supported by A*STAR's

Central Research Fund (CRF UIBR). G.G. acknowledges support from the Natural Sciences and Engineering Research Council of Canada (NSERC). S.-M.F. acknowledges financial support from the National Natural Science Foundation of China (Grant Nos. 12075159 and 12171044), Beijing Natural Science Foundation (Grant No. Z190005), and Academician Innovation Platform of Hainan Province.

# AUTHOR CONTRIBUTIONS

Y.X. and G.G. developed the theoretical framework and analyzed results with S.-M.F.; G.-Y.X. supervised the project; Y.Y., Z.H., and G.-Y.X. designed the experiment and the measurement apparatus; Y.Y. built the instruments, performed the experiment, and collected the data with assistance from Z.H. and G.-Y.X.; Y.Y., H.Z., and G.-Y.X. performed numerical simulations and analyzed the experimental data with assistance from C.F.L. and G.-C.G.; Y.Y., Y.X. and G.-Y.X. prepared and wrote the manuscript.

# COMPETING INTERESTS

The authors declare no competing interests.

# ADDITIONAL INFORMATION

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41534-023-00736-2.

Correspondence and requests for materials should be addressed to Yunlong Xiao or Guo-Yong Xiang.

Reprints and permission information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/b75a2ef391cbace7926ab8dc8ff4f6285e3a998d8bc2a560d05d5963c7c5c52d.jpg)

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing,

adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2023