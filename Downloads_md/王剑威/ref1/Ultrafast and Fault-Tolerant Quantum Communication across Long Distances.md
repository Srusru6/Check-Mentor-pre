# Ultrafast and Fault-Tolerant Quantum Communication across Long Distances

Sreraman Muralidharan, $^{1}$  Jungsang Kim, $^{2}$  Norbert Lütkenhaus, $^{3}$  Mikhail D. Lukin, $^{4}$  and Liang Jiang $^{5,*}$

$^{1}$ Department of Electrical Engineering, Yale University, New Haven, Connecticut 06511, USA

$^{2}$ Department of Electrical and Computer Engineering, Duke University, Durham, North Carolina 27708, USA

$^{3}$ Institute of Quantum computing, University of Waterloo, N2L 3G1 Waterloo, Canada

$^{4}$ Department of Physics, Harvard University, Cambridge, Massachusetts 02138, USA

$^{5}$ Department of Applied Physics, Yale University, New Haven, Connecticut 06511, USA

(Received 8 July 2013; revised manuscript received 19 October 2013; published 27 June 2014)

Quantum repeaters (QRs) provide a way of enabling long distance quantum communication by establishing entangled qubits between remote locations. In this Letter, we investigate a new approach to QRs in which quantum information can be faithfully transmitted via a noisy channel without the use of long distance teleportation, thus eliminating the need to establish remote entangled links. Our approach makes use of small encoding blocks to fault-tolerantly correct both operational and photon loss errors. We describe a way to optimize the resource requirement for these QRs with the aim of the generation of a secure key. Numerical calculations indicate that the number of quantum memory bits at each repeater station required for the generation of one secure key has favorable polylogarithmic scaling with the distance across which the communication is desired.

DOI: 10.1103/PhysRevLett.112.250501

PACS numbers: 03.67.Dd, 03.67.Hk, 03.67.Pp

Quantum communication across long distances  $(10^{3} - 10^{4}\mathrm{km})$  can significantly extend the applications of quantum information protocols such as quantum cryptography [1] and quantum secret sharing [2,3] which can be used for the creation of a secure quantum internet [4]. Quantum communication can be carried out by first establishing a remote entangled pair between the sender and the receiver and using teleportation to transmit information faithfully. However, there are two main challenges that have to be overcome. First, fiber attenuation during transmission leads to an exponential decrease in the entangled pair generation rate. Second, several operational errors such as channel errors, gate errors, measurement errors, and quantum memory errors severely degrade the quality of entanglement used for secure key generation. In addition, quantum states cannot be amplified or duplicated deterministically in contrast to classical information [5]. Establishing quantum repeater (QR) stations based on entanglement distribution is the only currently known approach to long-distance quantum communication using conventional optical fibers without exponential penalty in time and resources.

A number of schemes have been proposed for long distance quantum communication using QRs [6-12], most of which could be broadly classified into three classes. The first class of QRs [6-9] reduces the exponential scaling of fiber loss to polynomial scaling by introducing intermediate QR nodes. However, this scheme for long distance quantum communication is relatively slow [13], even after optimization [14], limited by the time associated with two-way classical communication between remote stations required for the entanglement purification process needed to correct operational errors [15]. In contrast, the second class of QRs

introduces quantum encoding and classical error correction to replace the entanglement purification with classical error correction, handling all operational errors [10,16]. As a consequence, the entanglement generation rate further improves from  $1 / O[\mathrm{poly}(L_{\mathrm{tot}})]$  to  $1 / O(\mathrm{poly}[\log (L_{\mathrm{tot}})])$  where  $L_{\mathrm{tot}}$  is the total distance of communication. Recently, the approach to a third type of QRs was proposed, which uses quantum encoding to deterministically correct photon losses [11,12]. By entirely eliminating two-way classical communication between all repeater stations, the third class of QRs promise extremely high key generation rates that can be close to classical communication rates, limited only by the speed of local operations.

Besides the high key generation rate, it is very important to consider the resource requirement and fault-tolerant implementation of QRs. Cluster states can be used for achieving fault-tolerant quantum computation [17-19] and long-range entanglement [20] in the presence of both loss and operation errors. Cluster state based protocols [20] naturally belong to second class of QRs because the preparation of a large cluster state shared by many QR stations uses two-way communications between neighboring stations. In the fault-tolerant surface-code proposal by Fowler et al. [11] (which belongs to the third class QRs), the resource for each station was estimated to scale logarithmically with the distance, while the exact resource overhead was found to be sensitive to the parameters for various imperfections. The proposal by Munro et al. [12] focused on the correction of photon loss errors using quantum parity code (QPC) [21], but did not consider fault tolerance, as perfect gate operations were assumed in their analysis.

In this Letter, we propose a fault-tolerant architecture for the third class of QRs, where a teleportation-based error correction (TEC) protocol [22,23] is employed within each repeater station to correct both operational and photon loss errors using Calderbank-Shor-Steane (CSS) encoding. We quantitatively investigate the optimum resource requirements using a cost function and optimize it for different repeater parameters. A schematic view of the proposed architecture of the third class of QRs is presented in Fig. 1.

Fault-tolerant architecture.-Analogous to fault-tolerant quantum computers [26], fault-tolerant QRs should reliably relay quantum information from one repeater station to another in the presence of various imperfections. Unlike quantum computers, QRs do not require a universal gate set and it is sufficient to have CNOT gates, state initialization and measurement associated with the complementary basis of  $\{|0\rangle ,|1\rangle \}$  and  $\{| + \rangle ,| - \rangle \}$ . However, QRs are confronted by an important challenge from transmission loss, which is less severe in most models of quantum computation. To design the fault-tolerant third class of QRs, we consider the CSS codes for their fault-tolerant properties [26], in particular the compatibility with the TEC protocol that can efficiently correct not only operational errors, but also photon loss errors [22,23]. The  $(n,m)$ -QPC [21] is a class of CSS codes with encoded qubits  $|0\rangle_{L} = \frac{1}{\sqrt{2}} (| + \rangle_{L} + | - \rangle_{L})$  and  $|1\rangle_{L} = \frac{1}{\sqrt{2}} (| + \rangle_{L} - | - \rangle_{L})$ , where  $|\pm \rangle_{L}$  are given by

![](images/359a7bb2c078e4278a76162b31812dc0835a263dae3e65969eebe2e83d7c13d0.jpg)

![](images/316a367defea8f91d53b01627872b41bc2911c69d84e9de5b47db360bb2f3151.jpg)  
FIG. 1 (color online). (a) A schematic view of the third class of QRs showing individual matter qubits in the repeater stations connected by an optical fiber. The quantum state is encoded into an error correcting code with photonic qubits, which are multiplexed and transmitted through the optical fiber to the neighboring repeater station. The quantum state of photonic qubits is transferred to the matter qubits and error correction is performed. After the error correction procedure, the quantum state of the matter qubits is transferred to photonic qubits and transmitted to the next repeater station. This procedure is carried out until the information reaches the receiver. (b) The TEC procedure consists of Bell state preparation and Bell measurement at the encoded level. Each line in the circuit represents an encoding block and the CNOT gate has a transversal implementation for CSS codes. This TEC scheme can be potentially implemented in a cavity QED system [24,25].

$$
| + \rangle_ {L} = \frac {1}{2 ^ {n / 2}} (| 0 0 \dots 0 \rangle_ {1 2 \dots m} + | 1 1 \dots 1 \rangle_ {1 2 \dots m}) ^ {\otimes n},
$$

$$
\left| - \right\rangle_ {L} = \frac {1}{2 ^ {n / 2}} \left(\left| 0 0 \dots 0 \right\rangle_ {1 2 \dots m} - \left| 1 1 \dots 1 \right\rangle_ {1 2 \dots m}\right) ^ {\otimes n}. \tag {1}
$$

The  $(n,m)$ -QPC consists of  $n$  subblocks, and each subblock has  $m$  physical qubits. First, we define the Pauli operators,  $X_{i,j}$ ,  $Y_{i,j}$ ,  $Z_{i,j}$  associated with the  $(i,j)$ th qubit, where  $i = 1,\ldots,n$  is the row (subblock) label and  $j = 1,\ldots,m$  is the column label for the qubit. There is one logical qubit encoded in the  $(n,m)$ -QPC, with logical operators  $\tilde{Z} \equiv \prod_{i=1}^{n} Z_{i,j}$  and  $\tilde{X} \equiv \prod_{j=1}^{m} X_{i,j}$ , where we may choose any  $j = 1,\ldots,m$  for  $\tilde{Z}$  and any  $i = 1,\ldots,n$  for  $\tilde{X}$  [26]. The encoded states  $\{|0\rangle_L, |1\rangle_L, |+\rangle_L, |-\rangle_L\}$  can be prepared fault-tolerantly with suppressed correlated errors [25,27-29]. The encoded state is transmitted via an optical fiber to the neighboring repeater station followed by error correction and transmission to the next repeater station (Fig. 1).

Suppose that each transmitted physical qubit can reach the next QR station with probability  $\eta$ , meanwhile suffering from depolarization errors. We apply TEC [22,23] to correct both photon loss and depolarization errors. The TEC procedure consists of Bell state preparation and Bell measurement at the encoded level [Fig. 1(b)], and both operations can be achieved fault-tolerantly without propagating errors within each encoding block [26]. The Bell measurement of two encoded blocks (received block  $R$  and local block  $S$ ) can be achieved by an encoded CNOT gate followed by measurement of logical operators  $\tilde{X}^R$  and  $\tilde{Z}^S$ . More specifically, it consists of nm pairwise CNOT gates between  $R_{i,j}$  and  $S_{i,j}$ , followed by 2nm individual qubit measurements. Besides erasure errors, TEC can also correct operational errors from qubit depolarization  $(\varepsilon_d)$ , imperfect measurement  $(\varepsilon_m)$ , and noisy quantum gates  $(\varepsilon_g)$ , which can be captured by an effective error probability  $\varepsilon = \varepsilon_d + \varepsilon_g / 2 + 2\varepsilon_m + O(\varepsilon_{d,g,m}^2)$  acting on a single qubit for our fault-tolerant circuit designs [25].

In the presence of photon loss errors, each measurement may have three possible outcomes  $\{+1, -1, 0\}$ . Each qubit  $R_{i,j}$  in the  $R$  block is measured in the  $X$  basis with outcome  $X_{i,j}^{R}$  taking value  $+1$  for qubit state  $|+\rangle$ ,  $-1$  for qubit state  $|-\rangle$ , and  $0$  if the qubit is erased due to transmission loss. Similarly, each qubit  $S_{i,j}$  from the  $S$  block is measured in the  $Z$  basis with outcome  $Z_{i,j}^{S}$  taking value  $+1$  for qubit state  $|0\rangle$ ,  $-1$  for qubit  $|1\rangle$ , and  $0$  if the corresponding qubit in the  $R$  block  $(R_{i,j})$  is erased. The logical measurement outcomes depend on individual qubit measurement outcomes

$$
\tilde {M} _ {X} ^ {R} = \operatorname {s g n} \left[ \sum_ {i = 1} ^ {n} \left(\prod_ {j = 1} ^ {m} X _ {i, j} ^ {R}\right) \right], \quad \tilde {M} _ {Z} ^ {S} = \prod_ {i = 1} ^ {n} \left(\operatorname {s g n} \left[ \sum_ {j = 1} ^ {m} Z _ {i, j} ^ {S} \right]\right),
$$

with three possible values  $\{+1, -1, 0\}$ . Here  $\operatorname{sgn}[\sum \dots]$  is associated with majority voting between  $\{\pm 1\}$ , and  $\prod \dots$  is associated with the product of trinary outcomes. Ideally, in

the absence of errors, the outcomes should be  $\tilde{M}_X^R = \tilde{X}^R$  and  $\tilde{M}_{Z}^{S} = \tilde{Z}^{S}$ , which determine the Pauli frame [22,23] of the encoded block after teleportation. In the presence of errors, however, the outcomes become  $\tilde{M}_X^R = \alpha \tilde{X}^R$  and  $\tilde{M}_{Z}^{S} = \beta \tilde{Z}^{S}$  with  $\alpha ,\beta = +1$  for correct measurement,  $-1$  for incorrect measurement, and 0 for heralded failure of measurement. We obtain the probability distribution [see Fig. 2(a)] [25]  $p_{\alpha ,\beta}\equiv \operatorname *{Pr}\left[\tilde{M}_X^R = \alpha \tilde{X}^R,\tilde{M}_Z^S = \beta \tilde{Z}^S\right]$  which can be used to evaluate the QR performance.

Quantum bit error rate and success probability. We use the probability distribution to compute the success probability and quantum bit error rate (QBER) that characterizes the QR. Since the encoded qubit passes through  $N$  repeater stations, there are  $N$  pairs of measurement outcomes  $(\tilde{M}_X$  and  $\tilde{M}_{Z})$ . The success probability with no heralded failure of measurements is

$$
P _ {\text {s u c c}} = \left(p _ {1, 1} + p _ {1, - 1} + p _ {- 1, 1} + p _ {- 1, - 1}\right) ^ {N}. \tag {2}
$$

Given that all measurement outcomes have no heralded failure, there might be an odd number of incorrect measurements of  $\tilde{M}_X$  (or  $\tilde{M}_Z$ ), which induces an error if the receiver decodes the information by measuring  $\tilde{X}$  (or  $\tilde{Z}$ ) of the received block. We define the QBER at the encoded level of the QR as the ratio of the probability of having an odd number of incorrect measurements of  $\tilde{M}_X$  (or  $\tilde{M}_Z$ ) to the probability of having no heralded failure. The QBER for  $\tilde{X}$  (or  $\tilde{Z}$ ) measurement by the receiver is

$$
Q _ {(X / Z)} = \frac {1}{2} \left[ 1 - \left(\frac {p _ {1 , 1} \pm p _ {1 , - 1} \mp p _ {- 1 , 1} - p _ {- 1 , - 1}}{p _ {1 , 1} + p _ {1 , - 1} + p _ {- 1 , 1} + p _ {- 1 , - 1}}\right) ^ {N} \right]. \tag {3}
$$

Key generation rate. For our QR, the raw key generation rate is  $1 / t_0$ , where  $t_0$  is the time taken for TEC. For simplicity, we may use  $t_0$  as a time unit in our analysis. The raw keys can be converted to secure keys through classical communication protocols involving error correction and privacy amplification [1]. Because of finite success probability and nonvanishing QBER, the asymptotic secure key generation rate is given by [30,31]

![](images/352762a7fe6bede56424af02a0099162026aeda3b4a8e2dcf4c8a3384d33d98f.jpg)  
FIG. 2 (color online). (a) Distribution of possible measurement outcomes. Measurement outcomes in the lighter area  $(p_{1,-1}, p_{-1,1}, p_{-1,-1})$  are logical errors, and outcomes in the darker area  $(p_{\alpha,0}$  and  $p_{0,\beta})$  lead to heralded failure. (b) Contour plot for the key generation rate  $R(n,m)$  (with  $t_0 = 1$ ) across a total distance  $L_{\mathrm{tot}} = 10000\mathrm{km}$  with repeater spacing  $L_0 = 1.5\mathrm{km}$  and  $\varepsilon = 10^{-3}$ . The optimized choice of encoding with minimum cost [see Eq. (5)] is a (13,6) code.

![](images/d0d53982f13e4a872ffca543d862bfb779cd8fc3a28489f65f86202bb0be36a7.jpg)

$$
R = \max  \left[ \frac {1}{t _ {0}} P _ {\text {s u c c}} \{1 - 2 h (Q) \}, 0 \right], \tag {4}
$$

where  $Q = (Q_{X} + Q_{Z}) / 2$  and  $h(Q) = -Q\log_2(Q) - (1 - Q)\log_2(1 - Q)$  is the binary entropy function. In Fig. 2, we show that  $R$  can approach  $1 / t_0$  for reasonable encoding size  $(n\times m)$  with an appropriate repeater spacing  $(L_0)$ , because it is possible to achieve high  $P_{\mathrm{succ}}$  and low  $Q$ . The range of  $(n,m)$  that yields a high key generation rate varies with  $L_0$  and the total distance of communication  $L_{\mathrm{tot}}(= N\times L_0)$ . Hence, we need to optimize the repeater parameters, including the size of encoding block, repeater spacing, and secure key generation rate.

For each secret bit generated by the QR, we should consider the cost of both time and qubit resources [32]: (1) the average time to generate a secret bit is  $1 / R$ , and (2) the total number of memory qubits needed for the QR scheme is  $2mn \times L_{\mathrm{tot}} / L_0$  [33]. We introduce the cost function,  $C$  to be the product of these two factors  $2nm / R \times L_{\mathrm{tot}} / L_0$ , in units of [qubits  $t_0$ /sbit]. Here the rate  $R$  implicitly depends on the control parameters of  $\{n, m, L_0\}$ . For given  $L_{\mathrm{tot}}$ , we can achieve the minimum cost:

$$
C \left(L _ {\mathrm {t o t}}\right) \equiv \min  _ {n, m, L _ {0}} \frac {2 n m}{R} \times \frac {L _ {\mathrm {t o t}}}{L _ {0}}, \tag {5}
$$

among all possible choices of  $(n,m)$ -QPC and repeater spacing  $L_{0}$ . We assume the following imperfections as we search for the optimal scheme: (1) operation error with probability  $\varepsilon$ , and (2) finite photon transmission with probability  $\eta = (1 - p_c)e^{-L_0 / L_{\mathrm{att}}}$  due to fiber attenuation  $(L_{\mathrm{att}} = 20~\mathrm{km})$  and coupling loss  $(p_c)$ .

Numerical search for optimized strategy. We search for optimized choices of  $\{n, m, L_0\}$  for different values of  $L_{\mathrm{tot}}$  with fixed imperfection parameters of  $\{\varepsilon, p_c\}$ . We run a numerical search for  $L_0$  and for a different number of qubits to obtain  $C(L_{\mathrm{tot}})$ , which should increase at least linearly with  $L_{\mathrm{tot}}$ . In Fig. 3, we show the variation of cost coefficient  $(C' = C / L_{\mathrm{tot}})$  with  $L_{\mathrm{tot}}$ , to illustrate the additional overhead associated with  $L_{\mathrm{tot}}$ . The cost coefficient can be interpreted as the resource overhead (qubits  $\times t_0$ ) for the creation of one secret bit over  $1\mathrm{km}$  (with target distance  $L_{\mathrm{tot}}$ ).

For imperfection parameters of  $\varepsilon = 10^{-3}$  and  $p_c = 0$ , the algorithm picks only four different codes up to  $L_{\mathrm{tot}} = 10000\mathrm{km}$ . When the code chosen by the algorithm changes (for example at  $4500\mathrm{km}$  in Fig. 3), the product of  $L_0$  and  $R$  also jumps to an appropriate higher value, so that the cost coefficient varies continuously with  $L_{\mathrm{tot}}$ . In the presence of coupling loss  $p_c < 10\%$ , the optimized values of  $L_0$  is within the range  $1.4 - 2\mathrm{km}$  (Fig. 3) with total loss errors up to  $20\%$ ;  $Rt_0$  is high (0.6-0.85) because of the favorable QBER associated with the chosen codes.

The optimized cost coefficient for different operational error probabilities is shown in Fig. 3. When  $\varepsilon$  decreases below  $10^{-3}$ , the cost coefficient is dominated by photon

![](images/469db2c02943f5724c4c0ab461882bb84b10c3327350c87ff2c739236dd7d563.jpg)

![](images/1c60b572ba949d87c3372c40522a1239b45383630b8037555764b61d17e813cc.jpg)

![](images/e631367586bc2cd21466d54339003c10a9eaa40558a8ed06ccff3c6a97885b1a.jpg)  
FIG. 3 (color online). (a) Cost coefficient  $C'(L_{\mathrm{tot}})$  for different operational errors  $\varepsilon$  with zero coupling loss  $p_c = 0$ , (b) cost coefficient  $C'(L_{\mathrm{tot}})$  for varying  $p_c$  with fixed  $\varepsilon = 10^{-3}$ , (c),(d) optimized encoded block size and repeater spacing for  $\varepsilon = 10^{-3}$  and  $p_c = 0$ .

![](images/2157bb61370b864ed9f5ed99dde9b1dd55ec47b298e16b78ff4ca10917280d95.jpg)

loss errors rather than operational errors, and does not decrease by a significant amount as  $\varepsilon$  decreases further. In a realistic scenario, photons are lost due to finite coupling losses besides fiber attenuation. In Fig. 3, we show that the QR scheme can tolerate coupling losses up to  $10\%$  for a reasonable overhead in the number of qubits. Numerical calculations indicate that the cost coefficient increases by  $O(\mathrm{poly}[\log (L_{\mathrm{tot}})])$  [25]. Table I provide an estimate of the resource requirements of our code under different scenarios.

Experimental considerations.-To implement our QR scheme, it is crucial to fulfill the following two experimental requirements: (1) The coupling loss should be sufficiently low ( $p_c \lesssim 10\%$ ), because if the transmission probability  $\eta < 50\%$ , then the probability that the receiver decodes the logical qubit will be exponentially small [34]. (2) The quantum repeater station should have hundreds of qubits with high fidelity operations. For ion trap systems, a single qubit gate error probability of  $2 \times 10^{-5}$  [37], a two-qubit gate error probability of 0.007 [38], and a measurement error probability of  $10^{-4}$  [39,40] have been demonstrated. There are also promising developments in

TABLE I. Optimized resource requirements for our fault-tolerant QR scheme with  $(n,m)$ -QPC encoding for different coupling losses  $p_c$  and operational error  $\varepsilon$ .  

<table><tr><td>pc</td><td colspan="2">ε</td><td colspan="3">Ltot= 1000 km</td><td colspan="4">Ltot= 10000 km</td></tr><tr><td></td><td></td><td>m</td><td>n</td><td>L0 (km)</td><td>Rt0</td><td>m</td><td>n</td><td>L0 (km)</td><td>Rt0</td></tr><tr><td>0%</td><td>10-4</td><td>4</td><td>7</td><td>1.7</td><td>0.72</td><td>5</td><td>9</td><td>1.3</td><td>0.80</td></tr><tr><td>0%</td><td>10-3</td><td>5</td><td>10</td><td>2.0</td><td>0.74</td><td>6</td><td>13</td><td>1.5</td><td>0.78</td></tr><tr><td>10%</td><td>10-4</td><td>6</td><td>21</td><td>1.6</td><td>0.60</td><td>7</td><td>28</td><td>1.0</td><td>0.57</td></tr><tr><td>10%</td><td>10-3</td><td>7</td><td>31</td><td>1.8</td><td>0.67</td><td>8</td><td>41</td><td>1.2</td><td>0.59</td></tr></table>

microfabricated ion traps for coherent control of hundreds of ion qubits [41].

In addition to these two requirements, efficient downconversion to the telecom wavelength (using similar techniques as described in Ref. [42], where a conversion efficiency of up to  $86\%$  was reported) can be used to minimize fiber attenuation. The collection efficiency of the photon from the ion (enhanced by adequate cavity QED effect [43,44]), wavelength conversion efficiency, and coupling of the resulting photons into the propagating media (fiber) should all be maximized to  $90\%$  levels, which remains an experimental challenge.

The techniques of time and wavelength-division-multiplexing will enable us to transmit multiple photons through a single optical fiber, increasing the communication rate by as much as 4 orders of magnitude (100 wavelengths, with 100 ions transmitting in sequence). The operation of TEC can be achieved with cavity QED systems [24,25]. The performance of the QR scheme introduced here depends crucially on the range of input parameters  $(\varepsilon, p_c, t_0)$ . The key generation rate  $R$  depends on the TEC time of  $t_0$ . Since it is possible to have subnanosecond quantum gates [45,46] with trapped ions, the TEC time will be mostly limited by the relatively slow measurement  $(10 - 100\mu s)$  [47] due to the finite photon scattering rate and collection efficiency, which can be significantly improved by enhancing the ion-cavity coupling strength. For instance, if the TEC time is improved to  $t_0 = 1\mu s$ , a secure key generation rate over  $0.5\mathrm{MHz}$  can be achieved over  $10000\mathrm{km}$  with the (41,8) code for  $\varepsilon = 10^{-3}$ ,  $p_c = 10\%$  and  $L_{0} = 1.2\mathrm{km}$ .

Besides trapped ions, neutral atoms in cavities [48,49], NV centers [50,51], quantum dots [52,53], and Rydberg atoms [54,55] are also promising systems for quantum repeater implementations. Furthermore, with the advance of coherent conversion between optical and microwave photons [56], superconducting qubits may become an attractive candidate to realize our scheme as they can achieve both ultrafast quantum gates and high coupling efficiency.

Summary and outlook.-We have presented a new QR scheme belonging to the third class of QRs, which considers both fault tolerance and small encoding blocks. In comparison with the first and second classes of QR schemes, our QR scheme uses TEC within each QR station to correct both photon loss and operation errors. In particular, our QR scheme can tolerate finite coupling loss  $(p_c \lesssim 10\%)$  and achieve fault-tolerant operation with approximately hundreds of qubits per repeater station. This enables an improved key generation rate that is limited only by local gate operations. Our scheme requires smaller QR spacing compared to the previous classes of QRs and consequently the number of QR stations is higher by roughly an order of magnitude. But it is important to note that the key generation rate increases by more than 3 orders of magnitude, by eliminating the communication time between the repeater stations. In addition, we have

introduced a cost function to optimize the control parameters of our QR scheme, which can potentially be used as a criterion to compare all three classes of QRs as well as to search for more efficient quantum error correcting codes for quantum communication.

This work was supported by the DARPA (Quiness program), NSF, CUA, NBRPC (973 program), Packard Foundation, and Alfred P. Sloan Foundation. We thank Austin Fowler, Steven Girvin, Archana Kamal, Chris Monroe, Bill Munro, David Poulin, and Hong Tang for discussions.

*liang.jiang@yale.edu  
[1] N. Gisin, G. Ribordy, W. Tittel, and H. Zbinden, Rev. Mod. Phys. 74, 145 (2002).  
[2] R. Cleve, D. Gottesman, and H. K. Lo, Phys. Rev. Lett. 83, 648 (1999).  
[3] M. Hillary, V. Buzek, and A. Berthiaume, Phys. Rev. A 59, 1829 (1999).  
[4] H. J. Kimble, Nature (London) 453, 1023 (2008).  
[5] W. K. Wootters and W. H. Zurek, Nature (London) 299, 802 (1982).  
[6] H. J. Briegel, W. Dür, J. I. Cirac, and P. Zoller, Phys. Rev. Lett. 81, 5932 (1998).  
[7] W. Dur, H. J. Briegel, J. I. Cirac, and P. Zoller, Phys. Rev. A 59, 169 (1999).  
[8] L. M. Duan, M. D. Lukin, J. I. Cirac, and P. Zoller, Nature (London) 414, 413 (2001).  
[9] P. van Loock, T.D. Ladd, K. Sanaka, F. Yamaguchi, K. Nemoto, W.J. Munro, and Y. Yamamoto, Phys. Rev. Lett. 96, 240501 (2006).  
[10] L. Jiang, J.M. Taylor, K. Nemoto, W.J. Munro, R. Van Meter, and M.D. Lukin, Phys. Rev. A 79, 032325 (2009).  
[11] A. G. Fowler, D. S. Wang, C. D. Hill, T. D. Ladd, R. Van Meter, and L. C. L. Hollenberg, Phys. Rev. Lett. 104, 180503 (2010).  
[12] W J. Munro, A. M. Stephens, S. J. Devitt, K. A. Harrison, and K. Nemoto, Nat. Photonics 6, 777 (2012); also see arXiv:1306.4137.  
[13] N. Sangouard, C. Simon, H. de Riedmatten, and N. Gisin, Rev. Mod. Phys. 83, 33 (2011).  
[14] L. Jiang, J. M. Taylor, N. Khaneja, and M. D. Lukin, Proc. Natl. Acad. Sci. U.S.A. 104, 17291 (2007).  
[15] C. H. Bennett, G. Brassard, S. Popescu, B. Schumacher, J. A. Smolin, and W. K. Wootters, Phys. Rev. Lett. 76, 722 (1996).  
[16] W. J. Munro, K. A. Harrison, A. M. Stephens, S. J. Devitt, and K. Nemoto, Nat. Photonics 4, 792 (2010).  
[17] M. Varnava, D. E. Browne, and T. Rudolph, Phys. Rev. Lett. 97, 120501 (2006).  
[18] S. D. Barrett and T. M. Stace, Phys. Rev. Lett. 105, 200502 (2010).  
[19] Y. Li, S. D. Barrett, T. M. Stace, and S. C. Benjamin, Phys. Rev. Lett. 105, 250502 (2010).  
[20] R. Raussendorf, S. Bravyi, and J. Harrington, Phys. Rev. A 71, 062313 (2005).

[21] T. C. Ralph, A. J. F. Hayes, and A. Gilchrist, Phys. Rev. Lett. 95, 100501 (2005).  
[22] E. Knill, Nature (London) 434, 39 (2005).  
[23] E. Knill, R. Laflamme, and G. J. Milburn, Nature (London) 409, 46 (2001).  
[24] L. M. Duan and H. J. Kimble, Phys. Rev. Lett. 92, 127902 (2004).  
[25] See Supplemental Material at [http://link.aps.org/supplemental/10.1103/PhysRevLett.112.250501] which includes Refs. [22,24,25,28,29], for a detailed description of the error correction scheme, implementation of TEC, in depth analytical treatment of error correction, fault-tolerant preparation of the encoded Bell pair, details of the optimization algorithm, and the scaling of the cost function with respect to total distance of communication.  
[26] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, England, 2002).  
[27] A.J.F. Hayes, H.L. Haselgrove, A. Gilchrist, and T.C. Ralph, Phys. Rev. A 82, 022323 (2010).  
[28] P. Brooks and J. Preskill, Phys. Rev. A 87, 032310 (2013).  
[29] G.-D. Lin, S.-L. Zhu, R. Islam, K. Kim, M.-S. Chang, S. Korenblit, C. Monroe, and L.-M. Duan, Europhys. Lett. 86, 60004 (2009).  
[30] P. W. Shor and J. Preskill, Phys. Rev. Lett. 85, 441 (2000).  
[31] V. Scarani, H.B. Pasquinucci, N.J. Cerf, M. Dusek, N. Lütkenhaus, and M. Peev, Rev. Mod. Phys. 81, 1301 (2009).  
[32] R. Alléaume, F. Roueff, E. Diamanti, and N. Lütkenhaus, New J. Phys. 11, 075002 (2009).  
[33] There is an overhead of ancillary qubits to enable the fault tolerant preparation of the encoded Bell pair. This overhead depends on the fault tolerant preparation scheme as discussed in Ref. [25]. To fix ideas, we will use the number of memory qubits  $2mn$  in our calculations.  
[34] Our repeater scheme is effectively a sequence of quantum erasure channels with forward-only communication between neighboring repeater stations, which has capacity max  $[0,2\eta -1]$  [35,36]. If  $\eta < 1 / 2$ , the channel capacity vanishes, which implies that the probability of faithful transmission between neighboring repeater stations cannot approach unity, and consequently the probability of faithful transmission over many repeater stations will decrease exponentially with the number of repeater stations.  
[35] C. H. Bennett, D. P. DiVincenzo, and J. A. Smolin, Phys. Rev. Lett. 78, 3217 (1997).  
[36] T.M. Stace, S.D. Barrett, and A.C. Doherty, Phys. Rev. Lett. 102, 200501 (2009).  
[37] K. R. Brown, A. C. Wilson, Y. Colombe, C. Ospelkaus, A. M. Meier, E. Knill, D. Leibfried, and D. J. Wineland, Phys. Rev. A 84, 030303 (2011).  
[38] J. Benhelm, G. Kirchmair, C. F. Roos, and R. Blatt, Nat. Phys. 4, 463 (2008).  
[39] A. H. Myerson, D. J. Szwer, S. C. Webster, D. T. C. Allcock, M. J. Curtis, G. Imreh, J. A. Sherman, D. N. Stacey, A. M. Steane, and D. M. Lucas, Phys. Rev. Lett. 100, 200502 (2008).  
[40] D. B. Hume, T. Rosenband, and D. J. Wineland, Phys. Rev. Lett. 99, 120502 (2007).

[41] C. Monroe and J. Kim, Science 339, 1164 (2013).  
[42] J. S. Pelc, L. Ma, C. R. Phillips, Q. Zhang, C. Langrock, O. Slattery, X. Tang, and M. M. Fejer, Opt. Express 19, 21445 (2011).  
[43] T. Kim, P. Maunz, and J. Kim, Phys. Rev. A 84, 063423 (2011).  
[44] D. Hunger, T. Steinmetz, Y. Colombe, C. Deutsch, T. W. Hänsch, and J. Reichel, New J. Phys. 12, 065038 (2010).  
[45] G. Romero, D. Ballester, Y.M. Wang, V. Scarani, and E. Solano, Phys. Rev. Lett. 108, 120501 (2012).  
[46] W.C. Campbell, J. Mizrahi, Q. Quraishi, C. Senko, D. Hayes, D. Hucul, D.N. Matsukevich, P. Maunz, and C. Monroe, Phys. Rev. Lett. 105, 090502 (2010).  
[47] R. Noek, G. Vrijsen, D. Gaultney, E. Mount, T. Kim, P. Maunz, and J. Kim, arXiv:1304.3511.  
[48] S. Ritter, C. Nölleke, C. Hahn, A. Reiserer, A. Neuzner, M. Uphoff, M. Mcke, E. Figueroa, J. Bochmann, and G. Rempe, Nature (London) 484, 195 (2012).  
[49] J. D. Thompson, T. G. Tiecke, N. P. de Leon, J. Feist, A. V. Akimov, M. Gullans, A. S. Zibrov, V. V. Vuletic, and M. D. Lukin, Science 340, 1202 (2013).

[50] E. Togan, Y. Chu, A.S. Trifonov, L. Jiang, J. Maze, L. Childress, M.V.G.Dutt, A.S. Sorensen, P.R. Hemmer, A.S.Zibrov, and M.D.Lukin, Nature (London) 466, 730 (2010).  
[51] H. Bernien, B. Hensen, W. Pfaff, G. Koolstra, M. S. Blok, L. Robledo, T. H. Taminiau, M. Markham, D. J. Twitchen, L. Childress, and R. Hanson, Nature (London) 497, 86 (2012).  
[52] W.B. Gao, P. Fallahi, E. Togan, J.M. Sanchez, and A. Imamoglu, Nature (London) 491, 426 (2012).  
[53] K.D. Greve, L. Yu, P.L. McMahon, J.S. Pelc, C.M. Natarajan, N.Y. Kim, E. Abe, S. Maier, C. Schneider, M. Kamp, S. Hofling, R.H. Hadfield, A. Forchel, M.M. Fejer, and Y. Yamamoto, Nature (London) 491, 421 (2012).  
[54] T. Peyronel, O. Firstenberg, Q.Y. Liang, S. Hofferberth, A. V. Gorshkov, T. Pohl, M. D. Lukin, and V. Vuletic Nature (London) 488, 57 (2012).  
[55] Y. O. Dudin and A. Kuzmich, Science 336, 887 (2012).  
[56] J. M. Taylor, A. S. Sø rensen, C. M. Marcus, and E. S. Polzik, Phys. Rev. Lett. 107, 273601 (2011).