# Memory Effects in Quantum Metrology

Yuxiang Yang*

Institute for Theoretical Physics, ETH Zürich, 8093 Zürich, Switzerland

![](images/58a95df9e2b1b7474fd531e8cb45befa85b9fb8f698743cbc4f3f2cd7757a31f.jpg)

(Received 29 April 2019; published 11 September 2019)

Quantum metrology concerns estimating a parameter from multiple identical uses of a quantum channel. We extend quantum metrology beyond this standard setting and consider the estimation of a physical process with quantum memory, here referred to as a parametrized quantum comb. We present a theoretic framework of metrology of quantum combs, and derive a general upper bound of the comb quantum Fisher information. The bound can be operationally interpreted as the quantum Fisher information of a memoryless quantum channel times a dimensional factor. We then show an example where the bound can be attained up to a factor of 4. With the example and the bound, we show that memory in quantum sensors plays an even more crucial role in the estimation of combs than in the standard setting of quantum metrology.

DOI: 10.1103/PhysRevLett.123.110501

Introduction.-Steady developments in quantum communication and quantum memory allow us to measure a physical quantity with higher precision [1,2]. By harnessing quantum control and ancillary memory qubits, adaptive metrological strategies can improve the performance of sensing even in the presence of noise [3-6].

In standard quantum metrology, the goal is often to estimate identical copies of the same quantum gate, possibly subject to noise [7-9], that are available either in parallel [10] or in arbitrary order [11,12]. With the advance of quantum technologies, however, the focus is transitioning to more complex and realistic settings, where the parameter to estimate is contained in a network or an adaptive physical process [13-16]. In such settings, one would have to deal with a circuit with a complex underlying structure, or in a network equipped with communication channels and memories, which requires a model with a higher-order structure than parametrized quantum gates.

In this Letter, we extend quantum metrology beyond the standard setting of estimating parametrized quantum channels. We consider estimating an unknown parameter from a physical process consisting in  $K$  sequentially arranged parametrized quantum channels interconnected by quantum memory, here referred to as a (parametrized)  $K$  comb. We present a theoretic framework of quantum metrology with such parametrized combs, and derive a general upper bound of the  $K$ -comb quantum Fisher information (QFI). The QFI bound can be operationally interpreted as the quantum Fisher information of a memoryless channel times a dimensional factor that grows exponentially in  $K$ . We then show an example of estimating a protected parameter, where the QFI bound can be attained up to a factor of four, revealing that the best possible precision of estimating a  $K$  comb can decay exponentially with  $K$ . With the example and the QFI bound, we capture the power and the limitation

of memory effects in quantum metrology, previously observed in the discrimination of quantum channels [17]. In particular, memory in quantum sensors plays an even more crucial role in the estimation of quantum combs than in the standard setting of quantum metrology.

Quantum metrology in the presence of memory.-In this Letter, our goal is to estimate an unknown parameter  $\theta$  given access to a quantum machine that has its own memory, which belongs to a family of parametrized quantum machines  $\{\mathcal{N}_{\theta}\}_{\theta \in \Theta}$ . This quantum machine could be, for instance, a quantum circuit with ancillary qubits or a noisy physical process with an inaccessible environment. To show memory effects in quantum metrology in the most straightforward way, we focus on single parameter estimation and  $\Theta \subset \mathbb{R}$ . It is convenient to characterize such a quantum machine  $\mathcal{N}_{\theta}$  by a parametrized quantum comb [18-20]. A quantum comb is mathematically characterized by a positive operator, called the Choi operator [21], that satisfies a series of normalization constraints. More details on quantum combs can be found in the original Letter [18].

As illustrated in Fig. 1, the action of the comb  $\mathcal{N}_{\theta}$  is naturally divided into  $K$  consecutive phases  $P_{1}, P_{2}, \ldots, P_{K}$ . Each phase is connected to the next phase by a quantum memory (or quantum communication, if the phases are spatially separate). For each phase  $P_{n}$ , the comb takes a quantum state from an input port  $P_{n}^{(\mathrm{in})}$ , performs a  $\theta$ -dependent quantum channel jointly on the input and the memory, and produces a quantum state from an output port  $P_{n}^{(\mathrm{out})}$ . From now on, we will refer to it as a (parametrized)  $K$  comb.

In the standard context of quantum gate estimation, one prepares a quantum state and sends it through unknown gates. Here, to estimate a  $K$  comb  $\mathcal{N}_{\theta}$ , we need to connect it to a quantum sensor  $\mathcal{S}$  with memory (hereafter referred to

![](images/5c2b7b14f86152c07255d3c0fbd343bfc879edc1a1487c10f0dd3412efe91e23.jpg)  
FIG. 1. Estimating a  $K$  comb with a sensor. In quantum comb metrology, the goal is to estimate a parameter  $\theta$  from a  $K$  comb  $\mathcal{N}_{\theta}$  consisting of  $K$  phases (plotted in black). For this purpose, one uses a sensor  $\mathcal{S}$  (plotted in blue), which consists of preparing an input state and applying quantum gates in between the phases.

as a sensor), which could be a complex composition of quantum states, gates, memory, and communication channels. Mathematically, the sensor  $S$  is also modeled by a quantum comb, which takes  $P_{m}^{(\mathrm{out})}$  (for  $m \in [K - 1]$ ) as its input ports and  $P_{n}^{(\mathrm{in})}$  (for  $n \in [K]$ ) as well as an ancillary system  $R$  as its output ports. This means that a sensor is such a quantum comb that it "eats" the  $K$  comb  $\mathcal{N}_{\theta}$  and "spits" a quantum state. Formally, this is taken care of by the link product [18-20], which is an operation to composite two combs in a way that any input or output ports sharing the same tag are concatenated. In our case, the link product of the  $K$  comb and the sensor results in a new quantum comb, denoted as  $\mathcal{N}_{\theta} * S$ . As shown in Fig. 1, all ports  $P_{m}^{(\mathrm{out})}$  (for  $m \in [K - 1]$ ) and  $P_{n}^{(\mathrm{in})}$  (for  $n \in [K]$ ) of the  $K$  comb are connected to the corresponding ports of the sensor. Therefore,  $\{\mathcal{N}_{\theta} * S\}_{\theta \in \Theta}$  is in fact a family of quantum states on  $\mathcal{H}_K^{(\mathrm{out})} \otimes \mathcal{H}_R$ . Here  $\mathcal{H}_n^{(\mathrm{out or in})}$  denotes the Hilbert space of  $P_{n}^{(\mathrm{out or in})}$ .

A distinctive difference between quantum comb metrology and quantum gate estimation that makes the former more tricky to deal with is the memory effect of both the sensor and the  $K$  comb. Unlike quantum states that are used to probe parametrized gates, sensors are capable of memorizing the information on  $\theta$  (possibly in the quantum form) at the end of each phase and send refined information back into the  $K$  comb. Similarly, the  $K$  comb is also capable of storing the input from the sensor in its underlying structure and making it interact with future inputs. Our goal is to see the impact of such effects on the best achievable precision.

Physically, the role of the sensor is to extract  $\theta$  from the  $K$  comb and to encode it into a quantum state. The QFI of quantum combs can be defined via the Fisher information of quantum states, by optimizing over all possible sensors:

Definition 1.-The quantum Fisher information of  $\{\mathcal{N}_{\theta}\}$  is defined as

$$
F _ {Q} \left[ \mathcal {N} _ {\theta} \right] := \max  _ {\mathcal {S}} F _ {Q} \left[ \mathcal {N} _ {\theta} * \mathcal {S} \right], \tag {1}
$$

where  $F_{Q}[\rho_{\theta}]$  denotes the QFI of a quantum state  $\rho_{\theta}$  and the maximum is taken over all sensors  $S$  such that  $\mathcal{N}_{\theta} * S$  is a quantum state.

With this definition of the comb QFI, we can apply the quantum Cramér-Rao bound [22-25] and extend it to quantum combs: Denoting by  $\delta \theta [\mathcal{N}_{\theta}]$  the root-mean-square error of estimating  $\theta$  from  $\mathcal{N}_{\theta}$ , we have

$$
\begin{array}{l} \delta \theta [ \mathcal {N} _ {\theta} ] = \min  _ {\mathcal {S}} (\min  _ {\mathcal {M} _ {\hat {\theta}}} \delta \theta [ \mathcal {N} _ {\theta} * \mathcal {S} * \mathcal {M} _ {\hat {\theta}} ]) \\ \geq \min  _ {\mathcal {S}} \left(\frac {1}{\sqrt {\nu F _ {Q} [ \mathcal {N} _ {\theta} * \mathcal {S} ]}}\right) \\ = \frac {1}{\sqrt {\nu F _ {Q} \left[ \mathcal {N} _ {\theta} \right]}}, \tag {2} \\ \end{array}
$$

where in the first step the minimum is taken over all quantum estimators  $\mathcal{M}_{\hat{\theta}}$  that measure the state  $\mathcal{N}_{\theta} * S$  and output an unbiased estimate  $\hat{\theta}$  of  $\theta$ , and  $\nu$  is the number of repetitions of the experiment.

A general upper bound on the comb QFI.-From the above discussion, we can see that the precision of estimating  $\theta$  is determined by the QFI of a  $K$  comb. However, the derivation of the QFI is not easy even for the simplest  $K = 1$  case, when the  $K$  comb is reduced to a quantum channel. A closed-form expression of the QFI was derived only for particular types of quantum channels (see, for instance, Refs. [26-29]). Therefore, it is more sensible to look for an upper bound of the comb QFI so as to see the power and the limitation of metrology with a quantum comb.

In the following, we derive such an upper bound of the comb QFI, which implies a lower bound on the error of parameter estimation from the comb. We will use the abbreviation  $\Psi \coloneqq |\Psi \rangle \langle \Psi|$  of pure state density matrices and denote by  $|\Phi^{+}\rangle$  a maximally entangled state  $(1 / \sqrt{d})\sum_{j}|j\rangle |j\rangle$

First, observe that any sensor can be decomposed as  $S = \Psi_{1}*\mathcal{V}$ , where  $\Psi_{1}\in \mathsf{St}(\mathcal{H}_{1}^{(\mathrm{in})}\otimes \tilde{\mathcal{H}}_{1}^{(\mathrm{in})})$  is a suitable input state (with  $\tilde{\mathcal{H}}_1^{\mathrm{(in)}}\simeq \mathcal{H}_1^{\mathrm{(in)}}$  being a reference system) and  $\nu$  is a quantum comb. An obstacle in determining  $F_{Q}[\mathcal{N}_{\theta}]$  is that the information on  $\theta$  can flow out of  $\mathcal{N}_{\theta}$  via an output port and then back into  $\mathcal{N}_{\theta}$  via subsequent input ports, owing to the memory effect of  $\nu$ . To overcome this obstacle, we use a trick of postselection, which works by noticing that the action of a sensor  $S$  is equivalent to the following probabilistic protocol, as depicted in Fig. 2(a):

1) Send a proper state  $\Psi_{1}$  into the first input port and a maximally entangled state  $\Phi_n^+$  into the  $n$ th input port for  $n > 1$ , with  $|\Phi_n^+\rangle$  being the maximally entangled state on  $\mathcal{H}_n^{(\mathrm{in})} \otimes \tilde{\mathcal{H}}_n^{(\mathrm{in})}$  (with  $\tilde{\mathcal{H}}_n^{(\mathrm{in})} \simeq \mathcal{H}_n^{(\mathrm{in})}$ ).  
2) Feed all but the last of the output ports of  $\mathcal{N}_{\theta}*\Psi_{1}$  into a quantum comb  $\nu$  
3) Perform a Bell test on the  $n$ th output port of  $\mathcal{V}$  and the open end of  $\Phi_n^+$  (for  $n > 1$ ); postselect the outcome  $\Phi_n^+$ .

Notice that we are abusing a bit the notation here, since the quantum comb  $\mathcal{V}$  has different (but isomorphic) output Hilbert spaces from the one in the decomposition of  $S$ .

![](images/9d91412ff2ba380f3234f859ac481e2857add8cd2ff7d0632c206d9559173a0c.jpg)  
(a)

![](images/56f4e6734e370094534e16aa783ce13a2df67b6a79fc17d9d7bfe03eb5eff13b.jpg)  
(b)  
FIG. 2. Bounding the memory effect of  $\mathcal{N}_{\theta}$ . The wires connecting the sensor to the comb  $\mathcal{N}_{\theta}$  can be winded using probabilistic teleportation, as plotted in Fig. 2(a). The QFI of  $\mathcal{N}_{\theta}$  can thus be bounded in terms of the QFI of the quantum state  $\Phi_{\mathcal{N}_{\theta}*\Psi_1}$ , which is depicted in Fig. 2(b).

In view of estimating the parameter  $\theta$ , this probabilistic protocol can be regarded as one step of probabilistic metrology [30-32], where one performs a measurement and postselects one particular outcome to enhance the performance of parameter estimation. The limitation of probabilistic quantum metrology can be made clear via the following equation [ [33], Eq. (30)]: For a family of parametrized quantum states  $\{\rho_{\theta}\}$  and a quantum operation (i.e., a completely positive, trace-nonincreasing linear map)  $\mathcal{M}^{(\mathrm{suc})}$ , we have

$$
F _ {Q} [ \rho_ {\theta} ] \geq p _ {\theta} ^ {(\text {s u c c})} F _ {Q} [ \rho_ {\theta} ^ {(\text {s u c c})} ], \tag {3}
$$

where  $p_{\theta}^{(\mathrm{succ})} \coloneqq \mathrm{Tr}\mathcal{M}^{(\mathrm{succ})}(\rho_{\theta})$  is the success probability of the postselection and  $\rho_{\theta}^{(\mathrm{succ})} \coloneqq \mathcal{M}^{(\mathrm{succ})}(\rho_{\theta}) / p_{\theta}^{(\mathrm{succ})}$  is the output state of  $\mathcal{M}^{(\mathrm{succ})}$ .

In our case, the probability that the teleportation of a  $d$ -dimensional system succeeds without a unitary correction is  $d^{-2}$ . The success probability of the postselection is thus

$$
p _ {\theta} ^ {(\mathrm {s u c c})} = \left(\prod_ {i = 2} ^ {K} d _ {i} ^ {(\mathrm {i n})}\right) ^ {- 2}, \tag {4}
$$

where  $d_i^{(\mathrm{in})}$  is the dimension of the ith output port. The comb QFI is thus bounded as

$$
F _ {Q} \left[ \Phi_ {\mathcal {N} _ {\theta} * \Psi_ {1}} * \mathcal {V} \right] \geq p _ {\theta} ^ {(\text {s u c c})} F _ {Q} \left[ \mathcal {N} _ {\theta} * \mathcal {S} \right], \tag {5}
$$

where  $\Phi_{\mathcal{N}_{\theta}*\Psi_1}$  [see also Fig. 2(b)] is the Choi state [18,21] of  $\mathcal{N}_{\theta}*\Psi_{1}$ , defined as

$$
\Phi_ {\mathcal {N} _ {\theta} * \Psi_ {1}} := \mathcal {N} _ {\theta} * (\Psi_ {1} \otimes \Phi_ {2} ^ {+} \otimes \dots \otimes \Phi_ {K} ^ {+}). \qquad (6)
$$

Moreover, the output ports of  $\mathcal{V}$  are now detached from the input ports of  $\mathcal{N}_{\theta}$  thanks to the postselection. Noticing that data processing does not increase distinguishability ([25], Chap. 6) to maximize the comb QFI we should always take the quantum comb  $\mathcal{V}$  to be a sequence of isometries. Under this condition, we have

$$
F _ {Q} \left[ \Phi_ {\mathcal {N} _ {\theta^ {*}} \Psi_ {1}} * \mathcal {V} \right] = F _ {Q} \left[ \Phi_ {\mathcal {N} _ {\theta^ {*}} \Psi_ {1}} \right]. \tag {7}
$$

Combining Eqs. (4), (5), and (7), we get that the QFI of  $\mathcal{N}_{\theta} * \mathcal{S}$  is bounded by  $\left(\prod_{i=2}^{K} d_i^{(\mathrm{in})}\right)^2$  times the QFI of the quantum state  $\Phi_{\mathcal{N}_{\theta} * \Psi_1}$  [see Fig. 2(b)]. In summary, we derived the following theorem:

Theorem 1.-The QFI of a  $K$  comb  $\mathcal{N}_{\theta}$  is upper bounded as

$$
F _ {Q} \left[ \mathcal {N} _ {\theta} \right] \leq \left(\prod_ {i = 2} ^ {K} d _ {i} ^ {(\text {i n})}\right) ^ {2} \max  _ {\Psi_ {1}} F _ {Q} \left[ \Phi_ {\mathcal {N} _ {\theta} * \Psi_ {1}} \right], \tag {8}
$$

where  $\Phi_{\mathcal{N}_{\theta^{*}}\Psi_{1}}$  is defined in Eq. (6) and the maximum is taken over all  $\Psi_{1}\in \mathsf{St}(\mathcal{H}_{1}^{\mathrm{(in)}}\otimes \tilde{\mathcal{H}}_{1}^{\mathrm{(in)}})$  with  $\tilde{\mathcal{H}}_1^{\mathrm{(in)}}\simeq \mathcal{H}_1^{\mathrm{(in)}}$  being a reference system.

Theorem 1 provides an upper bound on the QFI of an arbitrary quantum comb. The only optimization required in the upper bound (8) is the maximization of the QFI over input states to the first port. Notice that, since the quantum comb  $\mathcal{N}_{\theta} * (\Phi_2^+ \otimes \dots \otimes \Phi_K^+)$  has only one input port, the optimization is equivalent to finding the QFI of a quantum channel.

The QFI term on the right hand side of Eq. (8) is attained by a phase-parallel scheme, namely by feeding a quantum state into each of the input ports and collecting the states from the output ports for measurement. In a phase-parallel scheme, the comb  $\mathcal{N}_{\theta}$  is treated as a quantum channel with a multipartite input. The information on  $\theta$  never flows back into the comb  $\mathcal{N}_{\theta}$ . Therefore, the comb QFI bound (8) shows that the memory effect of a sensor improves the sensitivity of parameter estimation at most by a factor exponential in  $K$ . Note that a phase-parallel scheme is not necessarily local, since a phase of  $\mathcal{N}_{\theta}$  may consist of joint operations on multiple physical nodes in a realistic quantum network.

It is the main objective of quantum metrology to compare different strategies in terms of the asymptotic scalings of their QFIs with respect to the amount of required resources. In the conventional setting of parallel gate estimation [10,34], for instance, the resource is taken to be the number of calls to the parametrized quantum gate. Here in a quantum comb, the resource is quantified by the

number of phases  $K$ . An obvious observation is that the scaling suggested by the bound (8) is distinct from what one encounters when estimating a  $K$  comb that does not have a memory. For instance, if one gets back to the standard context of quantum metrology and considers each phase to be an individual quantum channel  $\mathcal{C}_{\theta}$ , the scaling of the comb QFI is at most the Heisenberg scaling  $K^2$  if one applies a suitable adaptive strategy [35,36], whereas a phase-parallel scheme achieves the standard quantum limit scaling  $K$ . In Eq. (8), in contrast, if all the input dimensions are equal to  $d$ , we get

$$
F _ {Q} \left[ \mathcal {N} _ {\theta} \right] \leq d ^ {2 (K - 1)} F _ {Q} \left[ \mathcal {N} _ {\theta}, \text {p h a s e - p a r a l l e l} \right], \tag {9}
$$

where  $F_{Q}[\mathcal{N}_{\theta}, \text{phase-parallel}]$  corresponds to the optimization term in Eq. (8). Next, we present a scenario of quantum metrology in the presence of memory effects, where the above bound is saturated up to a constant factor.

Estimating a protected parameter. We now consider a scenario where the optimal strategy is exponentially more efficient than the phase-parallel strategy in Eq. (8). As illustrated in Fig. 3, the  $K$  comb  $\mathcal{N}_{\theta}$  in this scenario encodes a parameter  $\theta$  in a unitary gate, and then uses a shield-key system to protect the parameter. We label the first phase as  $A$  and the remaining phases as  $\{B_i\}_{i\in [K - 1]}$ , and we shall use the convention  $\mathcal{U}(\cdot)\coloneqq U(\cdot)U^{\dagger}$  for a unitary. In the first phase, the input state goes through a parametrized unitary  $\nu_{\theta}$  and then it is mixed up with an ancillary state by a shielding unitary  $\mathcal{U}$  sampled with the Haar measure  $dU$  of  $\mathsf{SU}(D)$ . In the nth phase ( $2\leq n\leq K - 1$ ), the comb simply stores the input state and outputs nothing. In the  $K$ th (last) phase, the comb merges the input with all the previously stored states, and performs the key unitary  $\mathcal{U}^{\dagger}$  jointly on all these input states.

Here we consider the case when  $D = \prod_{i=1}^{K-1} d_{A_i^{(\mathrm{out})}}$  is an even number, and  $d_{A^{(\mathrm{in})}} = 2$ . For the dimensions to match, we have  $d_{A_n^{(\mathrm{out})}} = d_{B_n^{(\mathrm{in})}}$  for  $n \in [K-1]$  and

![](images/ce5f10d0193a27e5e3317c41f464c3ed5f26ee374d6a4c629f716e812782500c.jpg)  
FIG. 3. Estimating a protected parameter. An experimenter is to estimate a protected parameter  $\theta$  from a  $K$  comb, consisting of  $K$  blue boxes (whose latent structure is invisible) with input and output ports. The first box performs a parametrized gate  $\mathcal{V}_{\theta}$ , and mixes the resultant state with a fixed state by a random unitary  $\mathcal{U}$  that serves as the shield. Accessing the remaining  $K - 1$  boxes jointly will result in a key unitary  $\mathcal{U}^{\dagger}$ , which recovers the information on  $\theta$ . If the experimenter fails to do so, the information on  $\theta$  will be deteriorated.

$$
D = \prod_ {i = 1} ^ {K - 1} d _ {B _ {i} ^ {\left(\text {i n}\right)}}. \tag {10}
$$

The ancillary system, denoted as  $A^{(\mathrm{anc})}$ , has dimension  $D / 2$ , and we assume its state to be the maximally mixed state.

Denote by  $\Psi$  a quantum state in the Hilbert space of  $A^{(\mathrm{in})}$  and a reference system  $R$  such that the QFI of  $\Psi_{\theta} \coloneqq (\mathcal{V}_{\theta} \otimes \mathcal{I}_R)(\Psi)$ , with  $\mathcal{I}_R$  denoting the identity channel on the reference, achieves the maximum. The optimal scheme is to send (perhaps a part of)  $\Psi$  through the input port  $A^{(\mathrm{in})}$  and then to connect  $A_{n}^{(\mathrm{out})}$  to the corresponding input port  $B_{n}^{(\mathrm{in})}$  for every  $n \in [K - 1]$ . With this approach, the shield  $\mathcal{U}$  cancels out with the key  $\mathcal{U}^{\dagger}$ , and thus the optimal QFI for this comb is

$$
F _ {Q} \left[ \mathcal {N} _ {\theta} \right] = F _ {Q} \left[ \Psi_ {\theta} \right]. \tag {11}
$$

Obviously, the optimal scheme requires a quantum memory in between different phases. We now compare it to the phase-parallel scheme corresponding to the right hand side term of Eq. (8). For this purpose, we need to evaluate  $F_{Q}[\Phi_{\mathcal{N}_{\theta}*}\Psi^{\prime}]$ , which is the QFI of the output state when the comb is fed with the state  $\Psi_A^{(\mathrm{in})}\tilde{A}^{(\mathrm{in})}\otimes$ $\Phi_{B_1^{(\mathrm{in})}\tilde{B}_1^{(\mathrm{in})}}^+\otimes \dots \otimes \Phi_{B_{K - 1}^{(\mathrm{in})}\tilde{B}_{K - 1}^{(\mathrm{in})}}^+.$  For conciseness, we denote by  $B$  the  $K - 1$  phases  $B_{1},\ldots ,B_{K - 1}$ , and the input state can be rewritten as  $\Psi_{A^{(\mathrm{in})}\tilde{A}^{(\mathrm{in})}}^{\prime}\otimes \Phi_{B^{(\mathrm{in})}\tilde{B}^{(\mathrm{in})}}^{+}$  . The output state for this input can be derived by invoking symmetry properties of the comb. Because of the twirling effect of the comb,  $\tilde{A}^{(\mathrm{in})}$  will be partially entangled with a two-dimensional subspace  $B^{(\mathrm{in},1)}$  of  $B^{(\mathrm{in})}$  . Explicitly, the output state reads

$$
\begin{array}{l} \Phi_ {\mathcal {N} _ {\theta} * \Psi} = \left(\frac {\Psi_ {\theta}}{D ^ {2}}\right) _ {B ^ {(\text {i n}, 1)} \tilde {A} ^ {(\text {i n})}} \otimes \Phi_ {A ^ {(\text {t o t})} \tilde {B} ^ {(\text {i n})}} ^ {+} \otimes \pi_ {B ^ {(\text {i n}, 2)}} \\ + \left(\frac {\left(D ^ {2} - 4\right) \rho_ {\Psi^ {\prime}} + 3 \pi_ {\theta , \Psi^ {\prime}} ^ {-}}{D ^ {2}}\right) \tilde {A} ^ {(i n)} B ^ {(i n, 1)} \\ \otimes \pi_ {A ^ {(\mathrm {t o t})} \tilde {B} ^ {(\mathrm {i n})}} ^ {-} \otimes \pi_ {B ^ {(\mathrm {i n}, 2)}}, \tag {12} \\ \end{array}
$$

where  $\pi$  is the maximally mixed state,  $\pi^{-} \coloneqq (I - \Phi^{+}) / (D^{2} - 1)$  for a bipartite system,  $(\rho_{\Psi'})_{AB} \coloneqq (I_A \otimes \mathrm{Tr}_A \Psi') / d_A$  is a  $\theta$ -independent state,  $\pi_{\theta, \Psi'}^{-} \coloneqq (4\rho_{\Psi'} - \Psi'_\theta) / 3$  is a  $\theta$ -dependent state,  $A^{(\mathrm{tot})}$  is the joint system of  $A^{(\mathrm{in})}$  and  $A^{(\mathrm{anc})}$ , and  $B^{(\mathrm{in}, 2)}$  is defined via the decomposition  $B^{(\mathrm{in})} \simeq B^{(\mathrm{in}, 1)} \otimes B^{(\mathrm{in}, 2)}$ . The derivation is left to the Supplemental Material [37].

Next, we apply the convexity of the QFI of states, i.e.,  $F_{Q}[p\rho_{\theta} + (1 - p)\sigma_{\theta}] \leq pF_{Q}[\rho_{\theta}] + (1 - p)F_{Q}[\sigma_{\theta}]$  for two parametrized state families  $\{\rho_{\theta}\}$  and  $\{\sigma_{\theta}\}$  (see, for instance, [25], Chap. 6). Using the convexity and observing that  $\rho_{\Psi'}$  has no QFI, we can bound the QFI of the output state as

$$
\begin{array}{l} F _ {Q} \left[ \Phi_ {\mathcal {N} _ {\theta} * \Psi} \right] \leq \frac {1}{D ^ {2}} F _ {Q} \left[ \Psi_ {\theta} ^ {\prime} \right] + F _ {Q} \left[ \frac {(D ^ {2} - 4) \rho_ {\Psi^ {\prime}} + 3 \pi_ {\theta , \Psi^ {\prime}} ^ {-}}{D ^ {2}} \right] \\ \leq \frac {1}{D ^ {2}} F _ {Q} \left[ \Psi_ {\theta} ^ {\prime} \right] + \frac {3}{D ^ {2}} F _ {Q} \left[ \pi_ {\theta , \Psi^ {\prime}} ^ {-} \right]. \tag {13} \\ \end{array}
$$

We remark that the first inequality is actually an equality since  $\pi^{-}$  and  $\Phi^{+}$  are orthogonal to each other.

Since  $\Psi$  is such an input state that the QFI  $F_{Q}[\Psi_{\theta}]$  attains its maximum, from Eq. (13) we get

$$
F _ {Q} \left[ \Phi_ {\mathcal {N} _ {\theta} * \Psi^ {\prime}} \right] \leq \frac {4}{D ^ {2}} F _ {Q} \left[ \Psi_ {\theta} \right]. \tag {14}
$$

Finally, we get the relation between the QFI of  $\mathcal{N}_{\theta}$  and the QFI of  $\Phi_{\mathcal{N}_{\theta}*\Psi}$  as

$$
F _ {Q} \left[ \mathcal {N} _ {\theta} \right] \geq \frac {1}{4} \left(\prod_ {i = 1} ^ {K - 1} d _ {B _ {i} ^ {(\mathrm {i n})}}\right) ^ {2} F _ {Q} \left[ \Phi_ {\mathcal {N} _ {\theta} * \Psi} \right], \tag {15}
$$

by substituting Eq. (14) and Eq. (10) into Eq. (11). This clearly shows that the bound (8) is tight up to a factor of four for this scenario of estimating a protected phase. Memory effects in quantum metrology are thus manifested by the fact that the optimal adaptive sensor is exponentially more powerful than the phase-parallel sensor.

Conclusion.-We established a framework for quantum comb metrology and showed the effect of memory in quantum metrology. This could be the start of a new research direction, which deals with metrology in a fully quantum network or estimation of non-Markovian processes [39]. Our work also fits the current trend of studying quantum information processing of higher-order structures [40-42]. We conclude with a remark that the quantum combs considered here have definite causal structures, while it was recently shown that interesting phenomena can be observed in quantum communication networks with an indefinite causal structure [43]. It is thus meaningful to ask whether these phenomena extend to metrology, which may be related to probing an unknown spacetime structure.

The author is grateful to Giulio Chiribella, Joseph M. Renes, and anonymous referees for valuable comments, to Masahito Hayashi for discussions, and to Mark Wilde for suggesting references. This work is supported by the Swiss National Science Foundation via the National Center for Competence in Research "QSIT" as well as via Project No. 200020_165843 and by the Hong Kong Research Grant Council through Grant No. 17300918.

[3] W. Dur, M. Skotiniotis, F. Froewis, and B. Kraus, Improved Quantum Metrology Using Quantum Error Correction, Phys. Rev. Lett. 112, 080801 (2014).  
[4] H. Yuan and C.-H. Fred Fung, Optimal Feedback Scheme and Universal Time Scaling for Hamiltonian Parameter Estimation, Phys. Rev. Lett. 115, 110401 (2015).  
[5] P. Sekatski, M. Skotiniotis, J. Kołodyński, and W. Dür, Quantum metrology with full and fast quantum control, Quantum 1, 27 (2017).  
[6] S. Zhou, M. Zhang, J. Preskill, and L. Jiang, Achieving the Heisenberg limit in quantum metrology using quantum error correction, Nat. Commun. 9, 78 (2018).  
[7] B.M. Escher, R.L. de Matos Filho, and L. Davidovich, General framework for estimating the ultimate precision limit in noisy quantum-enhanced metrology, Nat. Phys. 7, 406 (2011).  
[8] J. Kołodyński and R. Demkowicz-Dobrzański, Efficient tools for quantum metrology with uncorrelated noise, New J. Phys. 15, 073043 (2013).  
[9] A.W. Chin, S.F. Huelga, and M.B. Plenio, Quantum Metrology in Non-Markovian Environments, Phys. Rev. Lett. 109, 233601 (2012).  
[10] V. Giovannetti, S. Lloyd, and L. Maccone, Quantum Metrology, Phys. Rev. Lett. 96, 010401 (2006).  
[11] W. van Dam, G. M. D'Ariano, A. Ekert, C. Macchiavello, and M. Mosca, Optimal Quantum Circuits for General Phase Estimation, Phys. Rev. Lett. 98, 090501 (2007).  
[12] Z. Ji, G. Wang, R. Duan, Y. Feng, and M. Ying, Parameter estimation of quantum channels, IEEE Trans. Inf. Theory 54, 5172 (2008).  
[13] P. Komar, E.M. Kessler, M. Bishop, L. Jiang, A.S. Sørensen, J. Ye, and M.D. Lukin, A quantum network of clocks, Nat. Phys. 10, 582 (2014).  
[14] T.J. Proctor, P.A. Knott, and J.A. Dunningham, Multiparameter Estimation in Networked Quantum Sensors, Phys. Rev. Lett. 120, 080501 (2018).  
[15] W. Ge, K. Jacobs, Z. Eldredge, A. V. Gorshkov, and M. Foss-Feig, Distributed Quantum Metrology with Linear Networks and Separable Inputs, Phys. Rev. Lett. 121, 043604 (2018).  
[16] Z. Eldredge, M. Foss-Feig, J. A. Gross, S. L. Rolston, and A. V. Gorshkov, Optimal and secure measurement protocols for quantum sensor networks, Phys. Rev. A 97, 042337 (2018).  
[17] G. Chiribella, G. M. D'Ariano, and P. Perinotti, Memory Effects in Quantum Channel Discrimination, Phys. Rev. Lett. 101, 180501 (2008).  
[18] G. Chiribella, G. M. D'Ariano, and P. Perinotti, Quantum Circuit Architecture, Phys. Rev. Lett. 101, 060401 (2008).  
[19] G. Chiribella, G. M. D'Ariano, and P. Perinotti, Theoretical framework for quantum networks, Phys. Rev. A 80, 022339 (2009).  
[20] A. Bisio, G. Chiribella, G. D'Ariano, and P. Perinotti, Quantum networks: General theory and applications, Acta Phys. Slovaca 61, 273 (2011).  
[21] M.-D. Choi, Completely positive linear maps on complex matrices, Linear Algebra Appl. 10, 285 (1975).  
[22] C. W. Helstrom, Quantum Detection and Estimation Theory (Academic Press, New York, 1976).

[23] A.S. Holevo, Probabilistic and Statistical Aspects of Quantum Theory (North-Holland, Amsterdam, 1982).  
[24] S. L. Braunstein and C. M. Caves, Statistical Distance and the Geometry of Quantum States, Phys. Rev. Lett. 72, 3439 (1994).  
[25] M. Hayashi, Quantum Information Theory (Springer, New York, 2017).  
[26] M. Hayashi, Comparison between the Cramer-Rao and the mini-max approaches in quantum channel estimation, Commun. Math. Phys. 304, 689 (2011).  
[27] R. Demkowicz-Dobrzański and L. Maccone, Using Entanglement Against Noise in Quantum Metrology, Phys. Rev. Lett. 113, 250801 (2014).  
[28] M. Takeoka and M.M. Wilde, Optimal estimation and discrimination of excess noise in thermal and amplifier channels, arXiv:1611.09165.  
[29] S. Pirandola and C. Lupo, Ultimate Precision of Adaptive Noise Estimation, Phys. Rev. Lett. 118, 100502 (2017).  
[30] J. Fiurášek, Optimal probabilistic estimation of quantum states, New J. Phys. 8, 192 (2006).  
[31] G. Chiribella, Y. Yang, and A. Chi-Chih Yao, Quantum replication at the Heisenberg limit, Nat. Commun. 4, 2915 (2013).  
[32] B. Gendra, E. Ronco-Bonvehi, J. Calsamiglia, R. Muñoz-Tapia, and E. Bagan, Quantum Metrology Assisted by Abstention, Phys. Rev. Lett. 110, 100501 (2013).  
[33] J. Combes, C. Ferrie, Z. Jiang, and C. M. Caves. Quantum limits on postselected, probabilistic quantum metrology, Phys. Rev. A 89, 052117 (2014).

[34] V. Giovannetti, S. Lloyd, and L. Maccone, Quantum-enhanced measurements: Beating the standard quantum limit, Science 306, 1330 (2004).  
[35] M. de Burgh and S. D. Bartlett, Quantum methods for clock synchronization: Beating the standard quantum limit without entanglement, Phys. Rev. A 72, 042301 (2005).  
[36] B. L. Higgins, D. W. Berry, S. D. Bartlett, H. M. Wiseman, and G. J. Pryde, Entanglement-free Heisenberg-limited phase estimation, Nature (London) 450, 393 (2007).  
[37] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.123.110501, which contains [38] and the derivation of Eq. (12).  
[38] W. Fulton and J. Harris, Representation Theory: A First Course (Springer Science & Business Media, New York, 2013), Vol. 129.  
[39] F. A. Pollock, C. Rodríguez-Rosario, T. Frauenheim, M. Paternostro, and K. Modi, Non-Markovian quantum processes: Complete framework and efficient characterization, Phys. Rev. A 97, 012127 (2018).  
[40] G. Gour and M. M. Wilde, Entropy of a quantum channel, arXiv:1808.06980.  
[41] X. Yuan, Hypothesis testing and relative entropy of quantum channels, Phys. Rev. A 99, 032317 (2019).  
[42] Z.-W. Liu and A. Winter, Resource theories of quantum channels and the universal role of resource erasure, arXiv: 1904.04201.  
[43] D. Ebler, S. Salek, and G. Chiribella, Enhanced Communication with the Assistance of Indefinite Causal Order, Phys. Rev. Lett. 120, 120502 (2018).