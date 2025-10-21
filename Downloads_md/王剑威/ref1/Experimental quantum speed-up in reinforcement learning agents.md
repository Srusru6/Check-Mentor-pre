# Experimental quantum speed-up in reinforcement learning agents

https://doi.org/10.1038/s41586-021-03242-7

Received: 12 August 2020

Accepted: 15 January 2021

Published online: 10 March 2021

Check for updates

V. Saggio $^{1\boxtimes}$ , B. E. Asenbeck $^{1}$ , A. Hamann $^{2}$ , T. Strömberg $^{1}$ , P. Schiansky $^{1}$ , V. Dunjko $^{3}$ , N. Friis $^{4}$ , N. C. Harris $^{5}$ , M. Hochberg $^{6}$ , D. Englund $^{5}$ , S. Wölck $^{2,7}$ , H. J. Briegel $^{2,8}$  & P. Walther $^{1,9\boxtimes}$

As the field of artificial intelligence advances, the demand for algorithms that can learn quickly and efficiently increases. An important paradigm within artificial intelligence is reinforcement learning<sup>1</sup>, where decision-making entities called agents interact with environments and learn by updating their behaviour on the basis of the obtained feedback. The crucial question for practical applications is how fast agents learn<sup>2</sup>. Although various studies have made use of quantum mechanics to speed up the agent's decision-making process<sup>3,4</sup>, a reduction in learning time has not yet been demonstrated. Here we present a reinforcement learning experiment in which the learning process of an agent is sped up by using a quantum communication channel with the environment. We further show that combining this scenario with classical communication enables the evaluation of this improvement and allows optimal control of the learning progress. We implement this learning protocol on a compact and fully tunable integrated nanophotonic processor. The device interfaces with telecommunication-wavelength photons and features a fast active-feedback mechanism, demonstrating the agent's systematic quantum advantage in a setup that could readily be integrated within future large-scale quantum communication networks.

Rapid advances in the field of machine learning and in general artificial intelligence (AI) are paving the way towards intelligent algorithms and automation. An important paradigm within AI is reinforcement learning (RL), where decision-making entities called 'agents' interact with an environment, 'learning' to achieve a goal via feedback<sup>1</sup>. Whenever the agent performs well (that is, makes the right decision), the environment rewards its behaviour, and the agent uses this information to progressively increase the likelihood of accomplishing its task. In this sense, an agent 'learns' by 'reinforcement'. RL has applications in many sectors, from robotics<sup>5,6</sup> to the healthcare domain<sup>7</sup>, to brain-like computing simulation<sup>8</sup> and neural network implementations<sup>6,9</sup>. In addition, the celebrated AlphaGo algorithm<sup>10</sup>, which is able to beat even the most skilled human players at the game of Go, employs RL.

At the same time, quantum technologies have experienced remarkable progress<sup>11</sup>. At the heart of quantum mechanics lies the superposition principle, dictating that even the simplest, two-dimensional quantum system is described by a continuum of infinitely many possible choices via a state vector  $|\psi \rangle = \alpha |0\rangle + \beta |1\rangle$  with the complex numbers  $\alpha$  and  $\beta$  satisfying  $|\alpha|^2 + |\beta|^2 = 1$ , while only two possible states,  $|0\rangle$  and  $|1\rangle$ , exist classically. Advantageous RL algorithms<sup>12,13</sup> inspired by quantum mechanics have been successful in aiding problems in quantum information processing, for example, decoding of errors<sup>14-16</sup>, quantum feedback<sup>17</sup>, adaptive code-design<sup>18</sup>, quantum-state reconstruction<sup>19</sup>

and even the design of quantum experiments $^{20,21}$ . Conversely, quantum technologies have enabled quadratically faster decision-making processes for RL agents via the quantization of their internal hardware $^{3,4,22,23}$ .

In all of these applications, agent and environment interact entirely classically. Here we consider a novel RL setting where they can also interact quantumly, formally via a quantum channel<sup>2</sup>. We therefore introduce a quantum-enhanced hybrid agent capable of quantum as well as classical information transfer. This makes it possible to achieve and quantify a quantum speed-up in the agent's learning time with respect to RL based solely on classical interaction.

We realize this protocol using a fully programmable nanophotonic processor interfaced with photons at telecommunication wavelengths. The setup enables the implementation of active-feedback mechanisms, thus proving suitable for demonstrations of RL algorithms. Moreover, such photonic platforms hold the potential of integrating RL quantum speed-ups in future quantum networks owing to the photons' telecommunication wavelengths. A long-standing goal in the development of quantum communication lies in establishing a form of 'quantum internet $^{24,25}$ , a highly interconnected network able to distribute and manipulate quantum states via optical links. We therefore envisage AI and RL to play important roles in future quantum networks, including a potential quantum internet, much in the same way that AI forms integral part of the internet today.

<sup>1</sup>University of Vienna, Faculty of Physics, Vienna Center for Quantum Science and Technology (VCQ), Vienna, Austria. <sup>2</sup>Institut für Theoretische Physik, Universität Innsbruck, Innsbruck, Austria. <sup>3</sup>LIACS, Leiden University, Leiden, The Netherlands. <sup>4</sup>Institute for Quantum Optics and Quantum Information - IQOQI Vienna, Austrian Academy of Sciences, Vienna, Austria. <sup>5</sup>Research Laboratory of Electronics, Massachusetts Institute of Technology, Cambridge, MA, USA. <sup>6</sup>Nokia Corporation, New York, NY, USA. <sup>7</sup>Deutsches Zentrum für Luft- und Raumfahr t e.V. (DLR), Institut für Quantentechnologien, Ulm, Germany. <sup>8</sup>Fachbereich Philosophie, Universität Konstanz, Konstanz, Germany. <sup>9</sup>Christian Doppler Laboratory for Photonic Quantum Computer, Faculty of Physics, University of Vienna, Vienna, Austria. <sup>10</sup>e-mail: valeria.saggio@univie.ac.at; philip.walther@univie.ac.at

![](images/ed723b0a8012c1f0c9d7014cee80dcac84ef4472e18ad7cba8fa0197a17e5968.jpg)  
a

![](images/8afeff7ca236f26241eefc3dfec7187f8f69342486c2b0b019f94eaff04e3c37.jpg)  
b

![](images/649333508ae6b7f556a2f412261c3f332ca92ca3efbce945cf9f42ff9d070956.jpg)  
C  
Fig. 1|Schematic of a learning agent. a, An agent interacts with an environment by receiving perceptual input  $s_i$  and outputting actions  $a_i$ . When the correct  $a_i$  is chosen, the environment issues a reward  $r$  that the agent uses to enhance its performance in the next round of interaction. b, Agent and environment interacting classically, that is, using a classical channel, where communication is only possible via a fixed preferred basis (for example, vertical or horizontal photon polarization). c, Agent and environment interacting via a quantum channel, where arbitrary superposition states are exchanged.

# Quantum-enhanced RL

The conceptual idea of RL is shown in Fig. 1a. A decision-making entity called an agent interacts with an environment by receiving perceptual input ('percepts')  $s_i$ , and outputting specific 'actions'  $a_i$  accordingly, at a certain time step  $i$ . Different 'rewards'  $r$  issued by the environment for correct combinations of percepts and actions incentivize agents to improve their decision-making, and thus to learn<sup>1</sup>.

Although RL has already been shown amenable to quantum enhancements, the interaction has so far been restricted exclusively to classical communication, meaning that signals can only be composed from a fixed, discrete alphabet. For signals carried by quantum systems (for example, single photons considered here) this corresponds to a fixed preferred basis, for example, 'vertical' or 'horizontal' photon polarization, as shown in Fig. 1b.

In general, it has been shown that granting agents access to quantum hardware (while still considering classical communication) does not reduce the learning time, although it allows actions to be output quadratically faster $^{3,4}$ . To achieve reductions in learning times, quantum communication becomes necessary.

We therefore consider an environment and a quantum-enhanced hybrid agent with access to internal quantum (as well as classical) hardware interacting by exchanging quantum states  $|a_i\rangle, |s_i\rangle$  and  $|r\rangle$ , representing actions  $a_i$ , percepts  $s_i$  and rewards  $r$ , respectively. Such agents may behave 'classically', that is, use a classical channel, or 'quantumly', meaning that communication is no longer limited to a fixed preferred basis, but allows for exchanges of arbitrary superpositions via a quantum channel, as shown in Fig. 1c. In general, agents react to (sequences of) percepts  $|s_{i-1}\rangle$  with (sequences of) actions  $|a_i\rangle$  according to a policy  $\pi(a_i|s_{i-1})$  that is updated during the learning process via classical control.

Within this framework, we focus on so-called deterministic strictly epochal (DSE) learning scenarios, also called episodic instead of

epochal<sup>1</sup>. Here 'epochs' consist of strings of perceptrs  $\mathbf{s} = (s_0, \dots, s_{L-1})$  with fixed  $s_0$ , actions  $\mathbf{a} = (a_1, \dots, a_L)$  of fixed length  $L$ , and a final reward  $r$ , and both  $\mathbf{s} = \mathbf{s}(\mathbf{a})$  and  $r = r(\mathbf{a})$  are completely determined by  $\mathbf{a}$ . Therefore, no explicit representation of the percepts is required in our experiment (Methods). A non-trivial feature of the DSE scenario is that the effective behaviour of the environment can be modelled via a unitary  $U_E$  (ref. 2) on the action and reward registers A and R as

$$
U _ {\mathrm {E}} | \mathbf {a} \rangle_ {\mathrm {A}} | 0 \rangle_ {\mathrm {R}} = \left\{ \begin{array}{l} | \mathbf {a} \rangle_ {\mathrm {A}} | 1 \rangle_ {\mathrm {R}} \text {i f} r (\mathbf {a}) > 0 \\ | \mathbf {a} \rangle_ {\mathrm {A}} | 0 \rangle_ {\mathrm {R}} \text {i f} r (\mathbf {a}) = 0 \end{array} . \right. \tag {1}
$$

$U_{\mathrm{E}}$  is similar to a generalized controlled-NOT gate such that in case of rewarded action sequences  $(r(\mathbf{a}) > 0)$ , the reward state is flipped.  $U_{\mathrm{E}}$  can therefore be used to perform a quantum search for such sequences.

A hybrid agent can choose between quantum and classical behaviour in each epoch. In classical epochs, the agent prepares the state  $|\mathbf{a}\rangle_{\mathrm{A}}|0\rangle_{\mathrm{R}}$  where a is determined by sampling from a classical probability distribution  $p(\mathbf{a})$  determined by its policy  $\pi$ . With a winning probability

$$
\varepsilon = \sin^ {2} (\xi) = \sum_ {\{\mathbf {a} \mid r (\mathbf {a}) > 0 \}} p (\mathbf {a}), \tag {2}
$$

with  $\xi \in [0, 2\pi]$ , the agent receives a reward and updates its policy according to a rule, presented in equation (4), based on projective simulation[26] (see also Methods). In quantum epochs, the following steps are performed:

(1) The agent prepares the state  $|\psi \rangle_{\mathrm{A}}| - \rangle_{\mathrm{R}}$ , with  $|\psi \rangle_{\mathrm{A}} = \sum_{\mathbf{a}} \sqrt{p(\mathbf{a})} |\mathbf{a}\rangle_{\mathrm{A}} = \cos(\xi)|\ell\rangle_{\mathrm{A}} + \sin(\xi)|w\rangle_{\mathrm{A}}$ , and sends it to the environment.  $|w\rangle_{\mathrm{A}}$  and  $|\ell\rangle_{\mathrm{A}}$  are superpositions of all winning (rewarded) and losing (non-rewarded) action sequences, respectively, and  $| - \rangle_{\mathrm{R}} = (|0\rangle_{\mathrm{R}} - |1\rangle_{\mathrm{R}})/\sqrt{2}$ .  
(2) The environment applies  $U_{\mathrm{E}}$  from equation (1) to  $|\psi \rangle_{\mathrm{A}}| - \rangle_{\mathrm{R}}$ , flipping the sign of the winning state:

$$
U _ {\mathrm {E}} | \psi \rangle_ {\mathrm {A}} | - \rangle_ {\mathrm {R}} = [ \cos (\xi) | \ell \rangle_ {\mathrm {A}} - \sin (\xi) | w \rangle_ {\mathrm {A}} ] | - \rangle_ {\mathrm {R}}, \tag {3}
$$

and returns the resulting state to the agent.

(3) The agent performs a reflection  $U_{\mathrm{R}} = 2|\psi \rangle \langle \psi |_{\mathrm{A}} - \mathbb{1}_{\mathrm{A}}$  over the initial state  $|\psi \rangle_{\Delta}$ .

The last step leads to amplitude amplification similar to Grover's algorithm $^{27}$  and thus to an increased probability  $\sin^2 (3\xi)$  (ref.  $^{28}$ ) to find rewarded action sequences (Methods). In our experiment, the hybrid agent performs a single query (and thus a single step of amplitude amplification) during a quantum epoch. However, the general framework allows for multiple steps of amplitude amplification in consecutive quantum epochs.

While quantum epochs lead to an increased winning probability, they do not reveal the reward (or corresponding percept sequence, in general). The reward can be determined only via classical test epochs, where the obtained action sequence is used as input. Thus, the hybrid agent alternates between quantum and classical test epochs, updating its policy every time a reward is obtained after a test epoch. Such agents accomplish their task of finding winning action sequences faster, and hence learn faster than entirely classical agents. This approach allows us to quantify the speed-up in learning time, which is not possible in the general setting discussed in ref.2. The learning speed-up manifests in a reduced average learning time  $\langle T\rangle_{\mathrm{Q}}$ , that is, the average number of epochs necessary to achieve a certain winning probability  $P_{\mathrm{L}}$ . In general, a quadratic improvement can be achieved if the maximal number of coherent interactions between agent and environment scales with the problem size (Methods).

# Experimental implementation

Quantized RL protocols can be compactly realized using state-of-the-art photonic technology[29]. Nowadays, integrated photonic platforms hold

![](images/d78951f11144543987970dbde17ea46d4e8b5077c3cf861dafa16c414b673528.jpg)

![](images/ee38f03ecd22637ea3e544d2766efd117f19711fa007cb9d97f0233e831d7201.jpg)  
the desired computation. It is then detected, in coincidence with the photon in D0, either in detector D1 or in D2/D3 after the agent plays the classical/quantum strategy (see Fig. 3 for more details). The coincidence events are recorded with a custom-made TTM. Different areas of the processor are assigned to either the agent or the environment, which can perform a Grover-like quantum search to look for rewarded action sequences in quantum epochs. The bottom part of the figure represents the Grover quantum circuit, where  $H$  indicates Hadamard gates creating quantum superpositions and  $n$  represents the number of target qubits. The agent has access to a classical control that updates its policy.

![](images/73fcb8c7fe16025fd3748954d651bb5c49f0fabdae01b53952cdb7fb1af61670.jpg)  
Fig. 2 | Experimental setup. a, Single programmable unit consisting of an MZI equipped with two fully tunable phase shifters, one internal allowing for a scan of the output distribution over  $\theta \in [0,2\pi]$ , and one external dictating the relative phase  $\phi \in [0,2\pi]$  between the two output modes. This makes the MZI act as a fully tunable beam splitter and allows for coherent implementation of sequences of quantum gates. b, Image of a single MZI in the processor. The third phase shifter in the bottom arm of the interferometer is not used. c, Overview of the setup. A single-photon source generates single-photon pairs at telecommunication wavelength. One photon is sent to a single-photon detector D0, while the other one is coupled into the processor and undergoes

the advantage of providing scalable architectures where many elementary components can be accommodated on small devices $^{30}$ . Here we use a programmable nanophotonic processor comprising 26 waveguides fabricated to form 88 Mach-Zehnder interferometers (MZIs). An MZI is equipped with two configurable phase shifters as shown in Fig. 2a, b, and acts as a tunable beam splitter. Information is spatially encoded onto two orthogonal modes  $|0\rangle = (1,0)^{\mathrm{T}}$  and  $|1\rangle = (0,1)^{\mathrm{T}}$ , which constitute the computational basis (T indicates the transpose).

As illustrated in Fig. 2c, pairs of single photons are generated (at telecommunication wavelengths) from a single-photon source. One photon is coupled into a waveguide and then detected by single-photon detectors D1, D2 or D3, while the other one is sent to D0 for heralding (that is, clicks in detectors D1, D2 or D3 are registered in coincidence with clicks in D0). The detectors are superconducting nanowires with efficiencies of up to

roughly  $90\%$  (see Methods for experimental details). The processor is divided into three regions, where the first and last are assigned to the agent, and the middle region to the environment, to carry out, in quantum epochs, steps1-3 listed above. The agent is further equipped with a classical control mechanism (a feedback loop) that updates its learning policy.

In our experiment, we represent the winning and losing action states  $|w\rangle_{\mathrm{A}}$  and  $|\ell \rangle_{\mathrm{A}}$  by a single qubit via  $|1\rangle_{\mathrm{A}} = |w\rangle_{\mathrm{A}}$  and  $|0\rangle_{\mathrm{A}} = |\ell \rangle_{\mathrm{A}}$ , and use another qubit to encode the reward  $(|0\rangle_{\mathrm{R}}, |1\rangle_{\mathrm{R}})$ . This results in a four-level system, where each level is a waveguide in our processor, as shown in Fig. 3. The winning probability for the agent is initially set to  $\varepsilon = \sin^2(\xi) = 0.01$ , representing a single rewarded action sequence out of 100. After a single photon is coupled into the mode  $|0_{\mathrm{A}}0_{\mathrm{R}}$ , the agent creates the state  $|\psi\rangle_{\mathrm{A}} = (\cos(\xi)|0\rangle_{\mathrm{A}} + \sin(\xi)|1\rangle_{\mathrm{A}})|0\rangle_{\mathrm{R}}$  by applying a unitary  $U_{\mathrm{P}}$ . Next, it can decide to play classically or quantum mechanically.

![](images/378ee95c2d40585d4613e8f40409c886a3c8b39cda861050caeb80d8454416d9.jpg)

![](images/5b072dabe6bc1a5000b5b8f74cf01d74208b5f4a67f7e29befdcffa163dfaaa0.jpg)  
Fig. 3 | Circuit implementation. a, b, One photon is coupled into the  $|0_{\mathrm{A}}0_{\mathrm{R}}\rangle$  waveguide and undergoes different operators depending on whether a classical (a) or a quantum (b) epoch is implemented. The waveguides  
highlighted in yellow show the photon's possible paths. Identity gates are represented by straight waveguides. Only the part of the processor needed for the computation is illustrated.

![](images/a0c96526efe3ed76f44de74ce5d413e00b81b80ca53ece1cd079cb6b1ca384cf.jpg)

![](images/f61c18d9b2f324396f48c5e7a456075860ea5d1cfc07e4314729e158c6460876.jpg)

![](images/a029a9ce88c2b6f669e112975ef4a61802b44978a044e37d54ed7dc1182eb3ba.jpg)  
Fig. 4 | Behaviour of the average reward  $\eta$  for different learning strategies. The solid line represents the theoretical data simulated with  $n = 10,000$  agents, while the dots represent the experimental data measured with  $n = 165$  agents. The shaded regions indicate the errors associated with each single data point. a,  $\eta$  of agents playing a quantum (blue) or classical (orange) strategy. b, c,  $\eta$  accounting for rewards obtained only every second epoch in the quantum strategy (b), compared with the case where the reward is distributed  
over the two epochs needed to acquire it (c). The error bars represent the standard errors. d, Comparison between the classical (orange) and combined (green) strategy, where an advantage over the classical strategy is visible. Here the agents stop the quantum strategy at their best performance (at  $\varepsilon = 0.396$ ) and continue playing classically. The inset shows the point where agents playing the quantum strategy reach the winning probability  $P_{\mathrm{L}} = 0.37$ , after  $\langle T\rangle_{\mathrm{Q}} = 100$  epochs.

In a classical strategy, the environment flips the reward qubit only if the action qubit is in the winning state via  $U_{\mathrm{E}}$  (Fig. 3a). Next, the photon is coupled out and detected in either D1 or D2 with probability  $\cos^2 (\xi)$  and  $\sin^2 (\xi)$ , respectively. If D2 is triggered (that is, the agent has been rewarded), a feedback mechanism updates the policy  $\pi$  by updating the winning probability  $\varepsilon_{j}$  after having obtained  $j$  rewards as

$$
\varepsilon_ {j} = \frac {1 + 2 j}{1 0 0 + 2 j}. \tag {4}
$$

$\pi$  is related to  $p(\mathbf{a})$ , and therefore to  $\varepsilon$ , via equation (5) (Methods).

In a quantum strategy, after the reward qubit is rotated to  $| - \rangle_{\mathrm{R}}$  via two operators  $U_{\mathrm{H0}}$  and  $U_{\mathrm{H1}}$ , the environment acts as an oracle via  $U_{\mathrm{E}}$  as in equation (3). Consecutively, the agent reverses the effect of  $U_{\mathrm{H0}}$  and  $U_{\mathrm{H1}}$ , and performs the reflection  $U_{\mathrm{R}}$  (Fig. 3b). Measuring in the computational basis of the action register then leads to the detection of a rewarded action sequence with increased probability  $\sin^2(3\xi)$  in D3. For practical reasons, the classical test epoch is implemented only in software (Methods). The update rule remains the same as in the classical case.

In general, any Grover-like algorithm faces a drop in amplitude amplification after the optimal point is reached. As different agents will reach this optimal point in different epochs, one can identify the probability  $\varepsilon = 0.396$  until which it is beneficial for all agents to use a quantum strategy, as they will observe more rewards than in the classical strategy on average (Methods). When this probability is surpassed, it is advantageous to switch to an entirely classical strategy. This combined strategy thus avoids the typical amplitude amplification drop without introducing additional overheads in terms of experimental resources.

# Results

At the end of each classical epoch, we record outcomes 1 and 0 for the rewarded and non-rewarded behaviour, respectively, obtaining a

binary sequence whose length equals the number of played epochs in the classical learning strategy and half of the number of played epochs in the quantum strategy (as here two epochs, quantum and classical test, are needed to obtain the reward). For a fair comparison between these scenarios, in the quantum strategy, the reward is distributed (that is, averaged) over the quantum and classical test epochs. The reward is then averaged over different independent agents. Figure 4 shows this average reward  $\eta$  for the different learning strategies.

The theoretical data are simulated for  $n = 10,000$  agents and the experimental data obtained from  $n = 165$ . Figure 4a visualizes the quantum improvement originating from the use of amplitude amplification compared with a purely classical strategy. For completeness, the comparison between not distributing and distributing the reward over two epochs in the quantum strategy is shown in Fig. 4b, c.

When  $\varepsilon = 0.396$ ,  $\eta$  for the quantum strategy starts decreasing, as visible in Fig. 4a. Our setup allows the agents to choose the favourable strategy by switching from quantum to classical when the latter becomes advantageous. This combined strategy outperforms the purely classical scenario, as shown in Fig. 4d. As previously discussed, a certain winning probability  $P_{\mathrm{L}}$  has to be defined to quantify the learning time. Choosing  $P_{\mathrm{L}} = 0.37$  (note however, that any probability below  $\varepsilon = 0.396$  can be chosen), the learning time  $\langle T\rangle$  for  $P_{\mathrm{L}}$  decreases from  $\langle T\rangle_{\mathrm{C}} = 270$  in the classical strategy to  $\langle T\rangle_{\mathrm{Q}} = 100$  in the combined strategy. This implies a reduction of  $63\%$ , which fits well to the theoretical values  $T_{\mathrm{C}}^{\mathrm{theory}} = 293$  and  $T_{\mathrm{Q}}^{\mathrm{theory}} = 97$ , accounting for small experimental imperfections.

In general, hybrid agents can experience a quadratic speed-up in their learning time if arbitrary numbers of coherent Grover iterations can be performed, even if the number of rewarded actions is unknown<sup>31</sup>.

# Conclusions

We have demonstrated an RL protocol where an agent can boost its performance by allowing quantum communication with the

environment. This enables a quantum speed-up in its learning time and optimal control of the learning process. Emerging photonic technology provides the advantages of compactness, tunability and low-loss communication, thus proving suitable for RL algorithms where active-feedback mechanisms, even over long distances, need to be implemented. Future scaled-up implementations of our protocol rely on a linearly increasing number of waveguides with the action space size when considering action sequences of length  $L = 1$ , and the use of just a single photon. In this case, a learning task with  $N$  different actions requires a processor with  $2N$  modes, while  $3N + 1$  or maximally  $\frac{\pi}{4}\sqrt{N} (3N + 1)$  gates are needed for a single or multiple rounds of amplitude amplification, respectively. In general, multiple photons will be required to deal with a combinatorially big space of action sequences of arbitrary length  $L$ . We envision our protocol to aid specifically in problems where frequent search is needed, for example, network routing problems, where, for instance, tens of qubits, waveguides and detectors would be employed to represent search spaces of  $10^{4}$  elements. In general, the development of superconducting detectors, on-demand single-photon sources[32] or the large-scale integration of artificial atoms within photonic circuits[33] suggest substantial steps towards scalable multiphoton applications. Although photonic architectures are particularly suitable for such learning algorithms, our theoretical background is applicable to different platforms, for example, trapped ions or superconducting qubits. Here future realizations can feature the implementation of agent and environment as spatially separated systems, and a light-matter quantum interface for coherent exchange between them[24,34].

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41586-021-03242-7.

1. Sutton, R. S. & Barto, A. G. Reinforcement Learning: An Introduction (MIT Press, 1998).  
2. Dunjko, V., Taylor, J. M. & Briegel, H. J. Quantum-enhanced machine learning. Phys. Rev. Lett. 117, 130501 (2016).  
3. Paparo, G. D., Dunjiko, V., Makmal, A., Martin-Delgrado, M. A. & Briegel, H. J. Quantum speedup for active learning agents. Phys. Rev. X 4, 031002 (2014).  
4. Sriarunothai, T. et al. Speeding-up the decision making of a learning agent using an ion trap quantum processor. Quantum Sci. Technol. 4, 015014 (2019).  
5. Johannink, T. et al. Residual reinforcement learning for robot control. In 2019 International Conference on Robotics and Automation (ICRA) 6023-6029 (IEEE, 2019).  
6. Tjandra, A., Sakti, S. & Nakamura, S. Sequence-to-aequence ASR optimization via reinforcement learning. In 2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) 5829-5833 (IEEE, 2018).

7. Komorowski, M., Celi, L. A., Badawi, O., Gordon, A. C. & Faisal A. A. The artificial intelligence clinician learns optimal treatment strategies for sepsis in intensive care. Nat. Med. 24, 1716-1720 (2018).  
8. Thakur, C. S. et al. Large-scale neuromorphic spiking array processors: a quest to mimic the brain. Front. Neurosci. 12, 891 (2018).  
9. Steinbrecher, G. R., Olson, J. P., England, D. & Carolan, J. Quantum optical neural networks. npj Quantum Inf. 5, 60 (2019).  
10. Silver, D. et al. Mastering the game of Go without human knowledge. Nature 550, 354-359 (2017).  
11. Arute, F. et al. Quantum supremacy using a programmable superconducting processor. Nature 574, 505-510 (2019).  
12. Dong, D., Chen, C., Li, H. & Tarn, T.-J. Quantum reinforcement learning. IEEE Trans. Syst. Man Cybern. B 38, 1207-1220 (2008).  
13. Dunjko, V. & Briegel, H. J. Machine learning & artificial intelligence in the quantum domain: a review of recent progress. Rep. Prog. Phys. 81, 074001 (2018).  
14. Baireuther, P., O'Brien, T. E., Tarasinski, B. & Beenakker, C. W. J. Machine-learning-assisted correction of correlated qubit errors in a topological code. Quantum 2, 48 (2018).  
15. Breuckmann, N. P. & Ni, X. Scalable neural network decoders for higher dimensional quantum codes. Quantum 2, 68-92 (2018).  
16. Chamberland, C., & Ronagh, P., Deep neural decoders for near term fault-tolerant experiments. Quant. Sci. Technol. 3, 044002 (2018).  
17. Fösel, T., Tighineanu, P., Weiss, T. & Marquardt, F. Reinforcement learning with neural networks for quantum feedback. Phys. Rev. X 8, 031084 (2018).  
18. Poulsen Nautrup, H., Delfosse, N., Dunjko, V., Briegel, H. J. & Friis, N. Optimizing quantum error correction codes with reinforcement learning. Quantum 3, 215 (2019).  
19. Yu, S. et al. Reconstruction of a photonic qubit state with reinforcement learning. Adv. Quantum Technol. 2, 1800074 (2019).  
20. Krenn, M., Malik, M., Fickler, R., Lapkiewicz, R. & Zeilinger, A. Automated search for new quantum experiments. Phys. Rev. Lett. 116, 090405 (2016).  
21. Melnikov, A. A. et al. Active learning machine learns to create new quantum experiments. Proc. Natl Acad. Sci. USA 115, 1221-1226 (2018).  
22. Dunjko, V., Friis, N. & Briegel, H. J. Quantum-enhanced deliberation of learning agents using trapped ions. New J. Phys. 17, 023006 (2015).  
23. Jerbi, S., Poulsen Nautrup, H., Trenkwalder, L. M., Briegel, H. J. & Dunjko, V. A framework for deep energy-based reinforcement learning with quantum speed-up. Preprint at https://arxiv.org/abs/1910.12760 (2019).  
24. Kimble, H. J. The quantum internet. Nature 453, 1023-1030 (2008).  
25. Cacciapotti, A. S. et al. Quantum internet: networking challenges in distributed quantum computing. IEEE Netw. 34, 137-143 (2020).  
26. Briegel, H. J. & De las Cuevas, G. Projective simulation for artificial intelligence. Sci. Rep. 2, 400 (2012).  
27. Grover, L. K. Quantum mechanics helps in searching for a needle in a haystack. Phys. Rev. Lett. 79, 325-328 (1997).  
28. Nielsen, M. A. & Chuang, I. L. Quantum Computation and Quantum Information (Cambridge Univ. Press, 2000).  
29. Flamini, F. et al. Photonic architecture for reinforcement learning. New. J. Phys. 22, 045002 (2020).  
30. Harris, N. C. et al. Quantum transport simulations in a programmable nanophotonic processor. Nat. Photon. 11, 447-452 (2017).  
31. Boyer, M., Brassard, G., Hoyer, P. & Tappa, A. Tight bounds on quantum searching. Fortschr. Phys. 46, 493-505 (1998).  
32. Senellart, P., Solomon, G. & White, A. High-performance semiconductor quantum-dot single-photon sources. Nat. Nanotechnol. 12, 1026-1039 (2017).  
33. Wan, N. H. et al. Large-scale integration of artificial atoms in hybrid photonic circuits. Nature 583, 226-231 (2020).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2021

# Article

# Methods

# Quantum enhancement in RL agents

Here we present an explicit method for combining a classical agent with quantum amplitude amplification. Introducing a feedback loop between classical policy update and quantum amplitude amplification, we are able to determine achievable improvements in sample complexity, and thus in learning time. In addition, the final policy of our agent has properties similar to those of the underlying classical agent, leading to a comparable behaviour as discussed in more detail in A.H. et al. (manuscript in preparation; which is dedicated to discussing the theoretical background of the hybrid agent more specifically).

In the following, we focus on simple DSE environments, where the interaction between the agent and the environment is structured into epochs. Each epoch starts with the same percept  $s_0$ , and at each time step  $i$  an action-percept pair  $(a_i, s_i)$  is exchanged. Many interesting environments are epochal, for example, in applications of RL to quantum physics[21,35-37] or popular problems such as playing Go[10]. At the end of each epoch, after  $L$  action-percept pairs are communicated, the agent receives a reward  $r \in \{0, 1\}$ . The rules of the game are deterministic and time independent, such that performing a specific action  $a_i$  after receiving a percept  $s_{i-1}$  always leads to the same following percept  $s_i$ .

The behaviour of an agent is determined by its policy described by the probability  $\pi(a_i | s_{i-1})$  to perform the action  $a_i$  given the percept  $s_{i-1}$ . In deterministic settings, the percept  $s_i$  is completely determined by all previously performed actions  $a_1, \dots, a_i$  such that  $\pi(a_i | s_{i-1}) = \pi(a_i | a_1, \dots, a_{i-1})$ . Thus, the behaviour of the agent within one epoch is described by action sequences  $\mathbf{a} = (a_1, \dots, a_l)$  and their corresponding probabilities

$$
p (\mathbf {a}) = \prod_ {i = 1} ^ {L} \pi \left(a _ {i} \mid a _ {1}, \dots , a _ {i - 1}\right). \tag {5}
$$

Our learning agent uses a policy based on projective simulation $^{26}$ , where each action sequence  $\mathbf{a}$  is associated with a weight factor  $h(\mathbf{a})$  initialized to  $h = 1$ . Its policy is defined via the probability distribution

$$
p (\mathbf {a}) = \frac {h (\mathbf {a})}{\sum_ {\mathbf {a} ^ {\prime}} h \left(\mathbf {a} ^ {\prime}\right)}. \tag {6}
$$

In our experiment, the initial winning probability  $\varepsilon$  is given by

$$
\varepsilon = \sum_ {\{\mathbf {a} | r (\mathbf {a}) > 0 \}} p (\mathbf {a}) = \frac {\sum_ {\{\mathbf {a} | r (\mathbf {a}) > 0 \}} h (\mathbf {a})}{\sum_ {\{\mathbf {a} \}} h (\mathbf {a})} \tag {7}
$$

and is set to 1/100. If the agent has chosen the sequence  $\mathbf{a}$ , it updates the corresponding weight factor via

$$
h (\mathbf {a}) \rightarrow h (\mathbf {a}) + \lambda r (\mathbf {a}), \tag {8}
$$

where  $\lambda = 2$  in our experiment and  $r(\mathbf{a}) = 1$  (0) if  $\mathbf{a}$  is rewarded (non-rewarded). Thus, the winning probability after the agent has found  $j$  rewards is given by equation (4). In general, the update method for quantum-enhanced agents is not limited to projective simulation and can be used to enhance any classical learning scenario, provided that  $p(\mathbf{a})$  exists and that the update rule is solely based on the observed rewards. We generalize the given learning problem to the quantum domain by encoding different action sequences  $\mathbf{a}$  into orthogonal quantum states  $|\mathbf{a}\rangle$  defining our computational basis. In addition, we create a fair unitary oracular variant of the environment $^2$ , whose effective behaviour on the action register can be described by  $\widetilde{U}_{\mathrm{E}}$  as

$$
\widetilde {U} _ {\mathrm {E}} | \mathbf {a} \rangle = \left\{ \begin{array}{l l} - | \mathbf {a} \rangle & \text {i f} r (\mathbf {a}) > 0 \\ | \mathbf {a} \rangle & \text {i f} r (\mathbf {a}) = 0. \end{array} \right. \tag {9}
$$

The unitary oracle  $\widetilde{U}_{\mathrm{E}}$  can be used to perform, for instance, a Grover search or amplitude amplification for rewarded action sequences by performing Grover iterations

$$
U _ {\mathrm {G}} = (2 | \psi) \langle \psi | - 1) \tilde {U} _ {\mathrm {E}} \tag {10}
$$

on an initial state  $|\psi \rangle$ . A quantum-enhanced agent with access to  $\widetilde{U}_{\mathrm{E}}$  can thus find rewarded action sequences faster than a corresponding classical agent defined by the same initial policy  $\pi (a_{i}|s_{i - 1})$  and update rules.

In general, the optimal number  $k$  of Grover iterations  $U_{\mathrm{G}}^{k}|\psi\rangle$  depends on the winning probability  $\varepsilon$  via  $k \propto 1/\sqrt{\varepsilon}$  (ref. [27]). In the following, we assume that  $\varepsilon$  is known at least to a good approximation. This is, for instance, possible if the number of rewarded action sequences is known. However, a similar agent can also be developed if  $\varepsilon$  is unknown by adapting methods from ref. [31] as described in A.H. et al. (manuscript in preparation).

Description of the agent. A quantum-enhanced hybrid agent is constructed via the following steps:

(1) Given the classical probability distribution  $p(\mathbf{a})$ , determine the winning probability  $\varepsilon = \sin^2 (\xi)$  based on the current policy and prepare the quantum state in the action register:

$$
| \psi \rangle = \sum_ {\{\mathbf {a} \}} \sqrt {p (\mathbf {a})} | \mathbf {a} \rangle \tag {11}
$$

$$
= \cos (\xi) | \ell \rangle + \sin (\xi) | w \rangle . \tag {12}
$$

Here the quantum states

$$
| \ell \rangle \propto \sum_ {\left\{\mathbf {a} \mid r (\mathbf {a}) = 0 \right\}} \sqrt {p (\mathbf {a})} | \mathbf {a} \rangle , \tag {13}
$$

$$
| w \rangle \propto \sum_ {\left\{\mathbf {a} \mid r (\mathbf {a}) > 0 \right\}} \sqrt {p (\mathbf {a})} | \mathbf {a} \rangle , \tag {14}
$$

contain all losing and winning components, respectively. In our experiment, we identify  $| \ell \rangle \cong | 0 \rangle$  and  $| w \rangle \cong | 1 \rangle$ . The task assigned to the agent is to (learn to) perform the winning sequences  $| w \rangle$  via policy update. This translates to a maximization of the obtained reward.

(2) Apply the optimal number  $k(\sqrt{\varepsilon})$  of Grover iterations leading to

$$
| \psi^ {\prime} \rangle = U _ {G} ^ {k} | \psi \rangle , \tag {15}
$$

and perform a measurement in the computational basis on  $|\psi^{\prime \prime}\rangle$  to determine a test action sequence a.

(3) Play one classical epoch by using the test sequence  $\mathbf{a}$  determined in step 2 and obtain the corresponding percept sequence  $\mathbf{s}(\mathbf{a})$  and the reward  $r(\mathbf{a})$ .  
(4) Update  $\varepsilon$ , and thus the classical policy  $\pi$ , using the rule in equation (4).

There exists a limit  $P$  on  $\varepsilon$  determining whether it is more advantageous for the agent to perform  $k$  Grover iterations with  $k(\sqrt{\varepsilon}) \geq 1$  or sample directly from  $p(\mathbf{a})$  (therefore  $k(\sqrt{\varepsilon}) = 0$ ) to determine  $\mathbf{a}$ . In the latter case, the agent would interact only classically (as in step 3) with the environment.

After each epoch, a classic agent receives a reward with probability  $\sin^2 (\xi)$ . A quantum-enhanced agent can instead use one epoch to either perform one Grover iteration (step 2) or to determine the reward of a given test sequence  $\mathbf{a}$  (step 3). After  $k$  Grover iterations, the winning probability is  $\sin^2 [(2k + 1)\xi]$  (ref. [28]; see next section). Thus, for  $k = 1$ , the agent receives a reward after every second epoch with probability  $\sin^2 (3\xi)$ . Therefore, we define the expected average reward of an agent playing a classical strategy as  $\eta_{\mathrm{C}} = \sin^2 (\xi)$  and of an agent playing a quantum

strategy with  $k = 1$  as  $\eta_{\mathrm{Q}} = \sin^2 (3\xi) / 2$ . For  $\varepsilon < P, \eta_{\mathrm{Q}} > \eta_{\mathrm{C}}$ , meaning that the quantum strategy proves advantageous over the classical case. However, as soon as  $\eta_{\mathrm{Q}} = \eta_{\mathrm{C}}$  (at  $P = 0.396$ ), a classical agent starts outperforming a quantum-enhanced agent that still performs Grover iterations.

Determining the winning probability  $\varepsilon$  exactly as in the example presented here is not always possible. In general, additional information such as the number of possible solutions and model building helps to perform this task. Note that a  $P$  smaller than 0.396 should be chosen if  $\varepsilon$  can only be estimated up to some range. To circumvent this problem, methods like Grover search with unknown reward probability<sup>31</sup> or fixed-point search<sup>38</sup> can be used to determine whether and how many steps of amplitude amplification should be performed (A.H. et al., manuscript in preparation).

Enhancement of the winning probability. After a quantum epoch, the amplitude  $\sin (\xi)$  of the winning state  $|w\rangle$  increases to  $\sin (3\xi)$ . Here we derive this result. The projections onto the winning and losing subspaces are given by  $\mathrm{Pr}_{\boldsymbol{w}} = \sum_{\{\mathbf{a} | r(\mathbf{a}) > 0\}} |\mathbf{a}\rangle \langle \mathbf{a}|$  and  $\mathrm{Pr}_{\ell} = \sum_{\{\mathbf{a} | r(\mathbf{a}) = 0\}} |\mathbf{a}\rangle \langle \mathbf{a}|$ , respectively, which are orthogonal and sum to identity. Therefore, the initial state (12) can be decomposed into a normalized winning  $|w\rangle \propto \mathrm{Pr}_{\boldsymbol{w}}|\psi\rangle$  and losing  $|\ell\rangle \propto \mathrm{Pr}_{\ell}|\psi\rangle$  component, and the unitary (10) implementing one Grover iteration can be written as

$$
U _ {\mathrm {G}} = (2 | \psi \rangle \langle \psi | - 1) \left(\Pr_ {\ell} - \Pr_ {w}\right). \tag {16}
$$

Now, let us investigate the effect of  $U_{\mathrm{G}}$  on an arbitrary real superposition

$$
| s \rangle = \sin (\alpha) | w \rangle + \cos (\alpha) | \ell \rangle \tag {17}
$$

in the plane spanned by  $|w\rangle$  and  $|\ell \rangle$ . Using the trigonometric addition theorems, the application of one Grover iteration to  $|s\rangle$

$$
U _ {\mathrm {G}} | s \rangle = \sin (\alpha + 2 \xi) | w \rangle + \cos (\alpha + 2 \xi) | \ell \rangle \tag {18}
$$

can be identified as a rotation of  $2\xi$  in the plane. Assuming  $\alpha = \xi$ , we therefore find the amplitude of  $|w\rangle$  to be  $\sin (3\xi)$ , and thus obtain a winning probability  $\sin^2 (3\xi)$ . Implementing  $k$  Grover iterations leads to  $\sin^2 [(2k + 1)\xi]$ .

Learning time. We define the learning time  $T$  as the number of epochs an agent needs on average to reach a certain winning probability  $P_{\mathrm{L}}$ . The hybrid agent can reach  $P$  with fewer epochs on average than its classical counterpart. However, once both reach  $P$ , they need on average the same number of epochs to reach  $P = \Delta_{P}$  where  $\Delta_{P}$  is a certain value satisfying  $0 \leq \Delta_{P} < 1 - P$ . Therefore, we choose  $P_{\mathrm{L}} \leq P$  to quantify the achievable improvement of a hybrid agent compared with its classical counterpart. In our experiment, we choose  $P_{\mathrm{L}} = 0.37$  to define the learning time.

Let  $l_{j} = \{\mathbf{a}_{1},\dots ,\mathbf{a}_{j}\}$  be a time-ordered list of all the rewarded action sequences an agent has found until it reaches  $P_{\mathrm{L}}$ . Note that the actual policy  $\pi_{j}$ , and thus  $p_j$ , of our agents depend only on the list  $l_{j}$  of observed rewarded action sequences, and this is independent of whether they have found them via classical sampling or quantum amplitude amplification. As a result, a classical agent and its quantum-enhanced hybrid version are described by the same policy  $\pi (l_{j})$  and behave similarly if they have found the same rewarded action sequences. However, the hybrid agent finds them faster.

In general, the actual policy and overall winning probability might depend on the rewarded action sequences that have been found. Thus, the number  $J$  of observed rewarded action sequences necessary to learn might vary. However, this is not the case for the experiment reported here. In our case, the learning time can be determined via

$$
T (J) = \sum_ {j = 0} ^ {J - 1} t _ {j}, \tag {19}
$$

where  $t_j$  determines the number of epochs necessary to find the next rewarded sequence  $\mathbf{a}_{j+1}$  after it has observed  $j$  rewards. For a purely classical agent, the average time is given by

$$
\left\langle t _ {j} \right\rangle_ {\mathrm {C}} = \frac {1}{\varepsilon_ {j}}. \tag {20}
$$

This time is quadratically reduced to

$$
\langle t _ {j} \rangle_ {\mathrm {Q}} = \frac {\alpha}{\sqrt {\varepsilon_ {j}}} \tag {21}
$$

for the hybrid agent. Here  $\alpha$  is a parameter depending only on the number of epochs needed to create one oracle query  $\widetilde{U}_{\mathrm{E}}$  (ref. 2) and on whether  $\varepsilon_{j}$  is known. In the case considered here, we find  $\alpha = \pi /4$ . As a consequence, the average learning time for the hybrid agent is given by

$$
\langle T (J) \rangle_ {\mathrm {Q}} = \sum_ {j = 0} ^ {J - 1} \frac {\alpha}{\sqrt {\varepsilon_ {j}}} \leq \alpha \sqrt {J} \sqrt {\langle T (J) \rangle_ {\mathrm {C}}}, \tag {22}
$$

where we used the Cauchy-Schwarz inequality and equations (19) and (20). The classical learning time typically scales with  $\langle T\rangle_{\mathbb{C}}\propto A^{K}$  for a learning problem with episode length  $K$  and the choice between  $A$  different actions in each step. The number  $J$  depends on the specific policy update and sometimes also on the list  $l_{j}$  of observed rewarded action sequences. For an agent sticking with the first rewarded action sequence, we would find  $J = 1$ . However, typical learning agents are more explorative, and common scalings are  $J\propto K$  such that we find

$$
\langle T (J) \rangle_ {\mathrm {Q}} \propto \sqrt {\log (\langle T (J) \rangle_ {\mathrm {C}})} \sqrt {\langle T (J) \rangle_ {\mathrm {C}}} \tag {23}
$$

for these cases. This is equivalent to a quasi-quadratic speed-up in the learning time if arbitrary numbers of Grover iterations can be performed.

In more general settings, there exist several possible  $l_{j}$  with different length  $J$  such that the learning time  $\langle T(J) \rangle$  needs to be averaged over all possible  $l_{j}$ , which again leads to a quadratic speed-up in learning time (A.H. et al., manuscript in preparation).

Limited coherent evolutions. In general, all near-term quantum devices allow for coherent evolution only for a limited time and are thus limited to a maximal number of Grover iterations. For winning probabilities  $\varepsilon = \sin^2 (\xi)$  with  $(2k + 1)\xi \leq \pi /2$ , performing  $k$  Grover iterations leads to the highest probability of finding a rewarded action.

Again, we assume that the actual policy of an agent depends on only the number of observed rewards an agent has found. As a consequence, the average time a hybrid agent limited to  $k$  Grover iterations needs to achieve the winning probability  $P < \sin^2 [\pi /(4k + 2)]$  is given by

$$
\langle T (J, k) \rangle_ {\mathrm {Q}} = \sum_ {j = 0} ^ {J - 1} \frac {\alpha_ {0} k + 1}{\sin^ {2} [ (2 k + 1) \xi_ {j} ]}, \tag {24}
$$

with  $\alpha_0$  determining the number of epochs necessary to create one oracle query  $\widetilde{U}_{\mathrm{E}}$ . For  $\alpha_0 = 1, k \gg 1$  and  $(2k + 1)\xi_j \ll \pi / 2$ , we can approximate the learning time for the hybrid agent via

$$
\langle T (J, k) \rangle_ {\mathrm {Q}} \approx \sum_ {j = 0} ^ {J - 1} \frac {1}{4 k \varepsilon_ {j}} = \frac {\langle T (J) \rangle_ {\mathrm {C}}}{4 k}, \tag {25}
$$

where we used  $\sin (x)\approx x$  for  $x\ll 1$ . In general, it can be shown (A.H. et al., manuscript in preparation) that the winning probability  $P_{k} = \sin^{2}\left[\pi /(4k + 2)\right]$  can be reached by a hybrid agent limited to  $k$  Grover iterations in a time

$$
\langle T (k) \rangle_ {\mathrm {Q}} \leq \gamma \frac {\langle T \rangle_ {\mathrm {C}}}{k}, \tag {26}
$$

where  $\gamma$  is a factor depending on the specific setting.

In our case, equation (24) can be used to compute the lower bound for the average quantum learning time, with  $\alpha_0 = k = 1$ . For the classical strategy, equation (20), together with equation (19), is used. Thus, given  $P_{\mathrm{L}} = 0.37$ , the predictions for the learning time in our experiment are  $T_{\mathrm{Q}}^{\mathrm{theory}} = 97$  and  $T_{\mathrm{C}}^{\mathrm{theory}} = 293$ .

# Experimental details

A continuous-wave laser (Coherent Mira HP) is used to pump a single-photon source producing photon pairs in the telecommunication-wavelength band. The laser light has a central wavelength of  $789.5\mathrm{nm}$  and pumps the single-photon source at a power of approximately  $100\mathrm{mW}$ . The source is a periodically poled  $\mathrm{KTiOPO_4}$  nonlinear crystal placed in a Sagnac interferometer[39,40], where the emission of single photons occurs via a type-II spontaneous parametric down-conversion process. The crystal (produced by Raicol) is  $30\mathrm{mm}$  long, set to a temperature of  $25^{\circ}\mathrm{C}$ , has a poling period of  $46.15\mu \mathrm{m}$  and is quasi-phase matched for degenerate emission of photons at  $1,570\mathrm{nm}$  when pumping with coherent laser light at  $785\mathrm{nm}$ . As the processor is calibrated for a wavelength of  $1,580\mathrm{nm}$ , we shift the wavelength of the laser light to  $789.75\mathrm{nm}$  to produce one photon at  $1,580\mathrm{nm}$  (that is then coupled into the processor) and another one at  $1,579\mathrm{nm}$  (the heralding photon).

The processor is a silicon-on-insulator type, designed by the Quantum Photonics Laboratory at the Massachusetts Institute of Technology (MIT) $^{30}$ . Each programmable unit on the device acts as a tunable beam splitter implementing the unitary

$$
U _ {\theta , \phi} = \left( \begin{array}{c c} \mathrm {e} ^ {\mathrm {i} \phi} \sin \frac {\theta}{2} & \mathrm {e} ^ {\mathrm {i} \phi} \cos \frac {\theta}{2} \\ \cos \frac {\theta}{2} & - \sin \frac {\theta}{2} \end{array} \right), \tag {27}
$$

where  $\theta$  and  $\phi$  are the internal and external phases shown in Fig. 2a, b, set via thermo-optical phase shifters controlled by a voltage supply. The achievable precision for phase settings is higher than  $250\mu \mathrm{rad}$ . The bandwidth of the phase shifters is around  $130\mathrm{kHz}$ . The waveguides, spatially separated from one another by  $25.4\mu \mathrm{m}$ , are designed to admit one linear polarization only. The high contrast in refractive index between the silicon and silica (the insulator) allows for waveguides with very small bend radius (less than  $15\mu \mathrm{m}$ ), thus enabling high component density (in our case 88 MZIs) on small areas (in our case,  $4.9\times 2.4\mathrm{mm}$ ). Given the small dimensions, the in-(out-)coupling is realized with the help of  $\mathrm{Si}_3\mathrm{N}_4 - \mathrm{SiO}_2$  waveguide arrays (produced by Lionix International), that shrink (and enlarge) the  $10 - \mu \mathrm{m}$  optical fibres' mode to match the  $2 - \mu \mathrm{m}$  mode size of the waveguides in the processor. The total input-output loss is around  $7\mathrm{dB}$ . The processor is stabilized to a temperature of  $28^{\circ}\mathrm{C}$  and calibrated at  $1,580\mathrm{nm}$  for optimal performance. To reduce the black-body radiation emission due to the heating of the phase shifters when voltage is applied, wavelength division multiplexers with a transmission peak centred at  $1,571\mathrm{nm}$  and bandwidth of  $13\mathrm{nm}$  are used before the photons are sent to the detectors. In our processor, two external phase shifters in the implemented circuits were not responding to the supplied voltage. These defects were accounted for by employing an optimization procedure.

The single-photon detectors are multi-element superconducting nanowires (produced by Photon Spot) with efficiencies up to  $90\%$  in the telecommunication-wavelength band. They have a dark count rate of about 100 counts per second, low timing jitter (hundreds of picoseconds) and a reset time  $< 100$  ns (ref. 41). Coincidence events are those detection events registered in DO and at the output of the processor that fall into a temporal window of 1.3 ns (the coincidence window), and are found using a time tagging module (TTM). In more detail, to

record coincidences and then update the agent's policy accordingly, the following steps are performed in the classical/quantum strategy (after initially setting  $h_w = \sum_{\{\mathbf{a} | r(\mathbf{a}) > 0\}} h(\mathbf{a}) = 1$  and  $h_\ell = \sum_{\{\mathbf{a} | r(\mathbf{a}) = 0\}} h(\mathbf{a}) = 99$  such that  $\varepsilon = 0.01$ ).

(1) The TTM records the time tags for photons in D0, D1 and D2/D3.  
(2) A Python script converts the time tags into arrival times, and it iterates through them until it finds a coincidence event between either D0 and D1, or D0 and D2/D3.  
(3) If a coincidence event between D0 and D1 (or D0 and D2/D3) is first found, a 0 (1) is sent to another Python script controlling the MZIs' phase shifters operating on a different computer. If a 0 is sent, the ratio  $\varepsilon = h_w / (h_\ell + h_w)$  remains unchanged. If a 1 is sent,  $h_w$  is updated as  $h_w + 2$ , which follows the update in equation (4). In the quantum strategy, this step also includes the implementation of a classical test epoch.

Implementing classical test epochs on hardware would require 'testing' the measured action state, that is, using the measured action sequence as input and making the environment act via  $U_{\mathrm{E}}$ , thus leading to detection of a reward  $|0\rangle_{\mathrm{R}}$  or  $|1\rangle_{\mathrm{R}}$ . However, since this simple circuit works in very close agreement with theoretical predictions (its visibility exceeds 0.99), this part has been implemented in software only.

The update rate is about  $1\mathrm{Hz}$  for both the classical and quantum epochs, and can be reduced up to the phase shifters' bandwidth.

# Data availability

All the datasets used in the current work are available on Zenodo at https://doi.org/10.5281/zenodo.4327211.

34. Northup, T. E. & Blatt, R. Quantum information transfer using photons. Nat. Photon. 8, 356-363 (2014).  
35. Denil, M. et al. Learning to perform physics experiments via deep reinforcement learning. Proc. Int. Conf. on Learning Representations (2017).  
36. Bukov, M. et al. Reinforcement learning in different phases of quantum control. Phys. Rev. X 8, 031086 (2018).  
37. Poulsen Nautrup, H. et al. Operationally meaningful representations of physical systems in neural networks. Preprint at https://arxiv.org/abs/2001.00593 (2020).  
38. Yoder, T. J., Low, G. H. & Chuang, I. L. Fixed-point quantum search with an optimal number of queries. Phys. Rev. Lett. 113, 210501 (2014).  
39. Kim, T., Fiorentino, M. & Wong, F. N. C. Phase-stable source of polarization-entangled photons using a polarization Sagnac interferometer. Phys. Rev. A 73, 012316 (2006).  
40. Saggio, V. et al. Experimental few-copy multipartite entanglement detection. Nat. Phys. 15, 935-940 (2019).  
41. Marsili, F. et al. Detecting single infrared photons with  $93\%$  system efficiency. Nat. Photon. 7, 210-214 (2013).

Acknowledgements We thank L. A. Rozema, I. Alonso Calafell and P. Jenke for help with the detectors. A.H. acknowledges support from the Austrian Science Fund (FWF) through the project P 30937-N27. V.D. acknowledges support from the Dutch Research Council (NWO/OCW), as part of the Quantum Software Consortium programme (project number O24.003.037). N.F. acknowledges support from the Austrian Science Fund (FWF) through the project P 31339-N27. H.J.B. acknowledges support from the Austrian Science Fund (FWF) through SFB BeyondC F7102, the Ministerium für Wissenschaft, Forschung, und Kunst Baden-Württemberg (Az. 33-7533-30-10/41/1) and the Volkswagen Foundation (Az. 97721). P.W. acknowledges support from the research platform TURIS, the European Commission through ErBeStA (no. 800942), HiPhoP (no. 731473), UNIQORN (no. 820474), EPIQUS (no. 899368), and AppQInfo (no. 956071), from the Austrian Science Fund (FWF) through CoQuS (W1210-N25), BeyondC (F 7113) and Research Group (FG 5), and Red Bull GmbH. The MIT portion of the work was supported in part by AFOSR award FA9550-16-1-0391 and NTT Research.

Author contributions V.S. and B.E.A. implemented the experiment and performed data analysis. A.H., V.D., N.F., S.W. and H.J.B. developed the theoretical idea. T.S. and P.S. provided help with the experimental implementation. N.C.H., M.H. and D.E. designed the nanophotonic processor. V.S., S.W. and P.W. supervised the project. All the authors contributed to writing the paper.

Competing interests The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41586-021-03242-7.  
Correspondence and requests for materials should be addressed to V.S. or P.W.  
Peer review information Nature thanks Vojtěch Havlíček, Lucas Lamata and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. Peer reviewers reports are available.  
Reprints and permissions information is available at http://www.nature.com/reprints.