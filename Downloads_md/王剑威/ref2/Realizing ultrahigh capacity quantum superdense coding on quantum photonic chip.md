# Realizing ultrahigh capacity quantum superdense coding on quantum photonic chip

Check for updates

Yuan Li $^{1,8}$ , Huihui Zhu $^{1,8}$ , Wei Luo $^{1}$ , Hong Cai $^{1}$ , Muhammad Faeyz Karim $^{2}$ , Xianshu Luo $^{3}$ , Feng Gao $^{3}$ , Xiang Wu $^{4}$ , Xiaqi Zhou $^{5}$ , Qinghua Song $^{6}$ , Leong Chuan Kwek $^{7}$  & Ai Qun Liu $^{1,2,4}$

Quantum superdense coding provides a compelling solution to enhance the channel capacity compared with classical coding, which plays a vital role in quantum networks. However, the realization of a degenerate high-dimensional entangled state with high fidelity has remained an elusive challenge, limiting improvement in channel capacity. Here, we have demonstrated a 16-mode quantum process photonic chip and experimentally validated a degenerate eight-dimensional quDit entangled state with a fidelity of  $0.973 \pm 0.002$ . Moreover, we propose an efficient Bell state measurement method to distinguish eleven orthogonal Bell states in eight-dimensional quantum superdense coding. Leveraging the high-quality features of our quantum photonic chip, we have achieved an unprecedented channel capacity of  $3.021 \pm 0.003$  bits, highlighting the largest channel capacity to date. Furthermore, our method presents a remarkable quantum advantage over classical schemes, the latter of which can only transmit a maximum of 3 bits in the environment without any noise. Our findings not only open up a new avenue for integrated quantum information processing, but also contribute significantly to the advancement of multidimensional technologies, facilitating the establishment of practical, high-capacity quantum networks.

Quantum superdense coding protocol<sup>1,2</sup> holds immense significance in the realm of quantum communication, providing a highly effective means to improve the channel capacity. In classical communication operating within a two-dimensional space, the maximum channel capacity achievable when transmitting a single particle is restricted to 1 bit. However, in the quantum domain, by leveraging an entangled quantum Bell state shared between Alice and Bob prior to the communication, Alice can locally manipulate her qubit, generating four orthogonal entangled Bell states, and subsequently send her qubit to Bob. Upon receiving the transmitted qubit, Bob can perform a complete Bell state measurement (BSM) to distinguish all four states. Remarkably, this quantum approach enables a channel capacity of 2 bits to be attained even when only a single particle is sent within the quantum system.

Quantum superdense coding has been demonstrated in different systems, including photonic $^{3-7}$ , atomic $^{8}$ , and nuclear systems $^{9}$ . Photons are

particularly well-suited for quantum communication due to their high transmittance speed and low transmittance loss in optical fibers, making them ideal candidates for long-distance communication compared with solid qubits. However, in optical systems, achieving a complete Bell state measurement solely with linear optics is challenging $^{10,11}$ , resulting in experimental channel capacity that is always lower than 2 bits. By combining different degrees of freedom (DoFs), it becomes possible to achieve a complete Bell state measurement for a single DoF, consequently increasing the experimental channel capacity $^{4,5}$ . Since the channel capacity $^{12}$  is only determined by the fidelity of the whole system and the number of distinguishable Bell states, increasing the dimension of the Hilbert space for the quantum entangled state is an effective method. Leveraging the  $N$ -dimensional Bell state enables a maximum channel capacity of  $2\log_2N$  bits when the  $N^2$  orthogonal Bell states are distinguished. Figure 1a shows the realization of the high-dimensional quantum superdense coding protocol, which

$^{1}$ Institute of Quantum Technology (IQT), The Hong Kong Polytechnic University, Hong Kong, China.  $^{2}$ Quantum Science and Engineering Centre (QSec), Nanyang Technological University, Singapore, Singapore.  $^{3}$ Advanced Micro Foundry, Singapore, Singapore.  $^{4}$ School of Information Science and Technology, Fudan University, Shanghai, China.  $^{5}$ State Key Laboratory of Optoelectronic Materials and Technologies and School of Physics, Sun Yat-sen University, Guangzhou, China.  $^{6}$ Tsinghua Shenzhen International Graduate School, Tsinghua University, Shenzhen, China.  $^{7}$ Centre for Quantum Technologies, National University of Singapore, Singapore, Singapore.  $^{8}$ These authors contributed equally: Yuan Li, Huihui Zhu.  $^{\text{e}}$ mail: helen.cai@polyu.edu.hk; faeyz@ntu.edu.sg; zhouxq8@mail.sysu.edu.cn; song.qinghua@sz.tsinghua.edu.cn; aiqun.liu@polyu.edu.hk

![](images/ee34e0c8e6ece2d8f2c8745d866d1ac9d7f34c7747d57b1d07cafc0e49ad16a2.jpg)

![](images/79821b84869e5df5aebc2c7e94d9b1e603f66a65a52831012245fd390dadba7f.jpg)

![](images/cec945109beda49abe093eb82b7b4e253bc8d088d9334cce61b5c7d55698f0dc.jpg)  
Fig. 1 | Quantum photonic chip for the realization of eight-dimensional quantum superdense coding. a The scheme of high-dimensional quantum superdense coding. b A dual-wavelength pump beam is injected into the photonic chip and separated into 16 paths to generate the weak single-mode squeezed states. Through the interference between the squeezed states, eight-dimensional Bell states for two photons (denoted as  $a$  and  $b$ ) are generated. Subsequently, it is injected into a  
16-mode unitary matrix which is composed of 120 MZIs for realizing the Bell state measurement. The heaters are precisely controlled by a current controller. The two photons are then injected into the superconducting nanowire single-photon detectors. Each MZI consists of two phase shifters and two multimode interferometers (MMI) c Photograph of the fabricated quantum photonic chip.

is composed of three parts: (1) the initial step involves generating a degenerate, high-dimensional entangled state between Alice and Bob. The degenerate photon pair sources shared by Alice and Bob are of the same wavelength, enabling the interference between the two photons, which is important to realize the Bell state measurement in the dense coding protocol. (2) Subsequently, Alice performs a local operation on her quDit to prepare the orthogonal, high-dimensional Bell states, which are used for the information encoding process. Then she sends the encoded quDit to Bob. (3) In the final step, Bob carries out a high-dimensional BSM to distinguish among these states after he receives the encoded quDit from Alice.

High-dimensional entanglement has been achieved in various photonic systems, such as paths $^{13,14}$ , orbital angular momentum (OAM) $^{15,16}$ , timebin $^{17}$ , and frequency-bin $^{18}$ . It shows that high-dimensional entangled states hold significant potential in the fundamental research of quantum information processing, particularly in quantum communication $^{19}$ . However, the endeavor to implement large-dimensional systems to enhance the channel capacity of superdense coding further and construct a highly efficient quantum network encounters numerous challenges. The primary challenge lies in mitigating the noise introduced during the preparation of high-dimensional Bell states or the transmission channel, as this noise substantially reduces the achievable channel capacity. In previous research on generating high-dimensional Bell states on photonic chips $^{20-23}$ , the Bell states produced were non-degenerate, meaning that the two photons had different wavelengths. This makes them unsuitable for achieving the perfect interference necessary to distinguish the encoded Bell states. Additionally, a significant challenge is developing robust methods for constructing high-dimensional Bell state measurements that can effectively discriminate most orthogonal Bell states. Therefore, it is crucial to create a high-fidelity, degenerate, high-dimensional entangled state and establish a stable, precise network infrastructure to minimize noise.

With the advancement of quantum-integrated photonic chips, increasingly intricate circuits have been realized, showcasing their potential in quantum information processing[24-26]. However, high-dimensional

superdense coding has yet to be realized. Moreover, conventional bulky optical setup has weaknesses such as poor compatibility, low stability, large size, and poor programmability. Using a silicon-based photonic chip, precise adjustments to each heater enable accurate and high-fidelity qubit operations, thereby providing a viable avenue for realizing high-dimensional quantum superdense coding with high compatibility, stability, compactness, programmability, and large scale.

In this paper, we propose a scheme to realize an eight-dimensional BSM using a 16-mode unitary matrix capable of distinguishing eleven Bell states. Our approach yields a maximum channel capacity of 3.46 bits. Subsequently, a universal programable photonic chip was fabricated with high precision for the eight-dimensional quantum superdense experiment, which comprises a high-dimensional Bell state generation part, an encoding part for Alice, and a BSM part for Bob. Through the implementation of this quantum photonic chip, we performed the high-dimensional dense coding experiment and achieved a channel capacity of  $3.021 \pm 0.003$  bits, which, to the best of our knowledge, is the highest reported capacity thus far. For classical communication in eight-dimensional space, a maximum channel capacity of 3 bits can be achieved only in the environment without any noise when sending one particle. Thus, our proof-of-principle demonstration of high-dimensional quantum superdense coding showcases the quantum advantage over classical coding. This accomplishment holds significant importance for future advancements in high-precision experiments on quantum photonic chips, paving the way for further quantum applications in high-capacity quantum networks and quantum communications.

# Results

# Experimental setup

Here, a large-scale  $16 \times 16$  quantum photonic chip on a silicon platform, has been specifically designed and fabricated for eight-dimensional quantum superdense coding. The quantum photonic chip comprises various essential components, including 16 spirals responsible for generating weak squeezed states through the process of spontaneous four-wave mixing (SFWM), 16

asymmetric MZIs (AMZIs) for filtering the pump beam, 319 multimode interferometer beam splitters, and 272 thermo-optic phase shifters for precise control as shown in Figs. 1b and 1c. The chip is packaged with a combination of optical, electronic, and thermal components, utilizing high-density electrodes mounted to a printed circuit board (PCB) through double-line wire-bonding techniques. A fiber array (FA) is utilized to couple light out of the chip, and a water-cooling temperature controller is integrated beneath the chip for efficient temperature regulation.

Generation of degenerate high-dimensional Bell state. A dual-wavelength pump beam with different wavelengths of  $1546.8\mathrm{nm}$  and  $1553.2\mathrm{nm}$  is illuminated into the quantum photonic chip[24]. The beam is then separated into 16 paths, internally interconnected by 16 spirals in each path. By adjusting the angle of the input MZI, we ensure that the intensities in each path are uniformly distributed. Through the SFWM process in the silicon nano waveguides, 16 single-mode squeezed states at the wavelength of  $1550\mathrm{nm}$  with equal squeezed parameters are generated. The pump beam is then filtered by the AMZIs, ensuring that only the single-mode squeezed state is left. For the adjacent two paths 1 and 2, a two-photon state  $|1\rangle |1\rangle$  is generated at these two paths after passing through a 50:50 beam splitter when the relative phase between the two paths is  $\pi /2$  due to the reverse Hong-Ou-Mandel (HOM) interference (see Supplementary Note 1 for more details). By employing the same method, the other seven  $|1\rangle |1\rangle$  states for the remaining 14 paths are achieved. Due to the coherent superposition of the states, we can obtain an eight-dimensional state  $|\varphi \rangle = (|a_0b_0\rangle +|a_1b_1\rangle +|a_2b_2\rangle +|a_3b_3\rangle +|a_4b_4\rangle +|a_5b_5\rangle +|a_6b_6\rangle +|a_7b_7\rangle)/2\sqrt{2}$ . In this scheme to demonstrate the high-dimensional superdense coding protocol, we choose eleven Bell states that are deterministically distinguished, which are expressed as

$$
\left| \psi_ {0} \right\rangle = \left(\left| a _ {0} b _ {0} \right\rangle - \left| a _ {1} b _ {1} \right\rangle + \left| a _ {2} b _ {2} \right\rangle - \left| a _ {3} b _ {3} \right\rangle + \left| a _ {4} b _ {4} \right\rangle - \left| a _ {5} b _ {5} \right\rangle + \left| a _ {6} b _ {6} \right\rangle - \left| a _ {7} b _ {7} \right\rangle\right) / 2 \sqrt {2}
$$

$$
\left| \psi_ {1} \right\rangle = \left(\left| a _ {0} b _ {0} \right\rangle + \left| a _ {1} b _ {1} \right\rangle - \left| a _ {2} b _ {2} \right\rangle - \left| a _ {3} b _ {3} \right\rangle + \left| a _ {4} b _ {4} \right\rangle + \left| a _ {5} b _ {5} \right\rangle - \left| a _ {6} b _ {6} \right\rangle - \left| a _ {7} b _ {7} \right\rangle\right) / 2 \sqrt {2}
$$

$$
\left| \psi_ {2} \right\rangle = \left(\left| a _ {0} b _ {0} \right\rangle - \left| a _ {1} b _ {1} \right\rangle - \left| a _ {2} b _ {2} \right\rangle + \left| a _ {3} b _ {3} \right\rangle + \left| a _ {4} b _ {4} \right\rangle - \left| a _ {5} b _ {5} \right\rangle - \left| a _ {6} b _ {6} \right\rangle + \left| a _ {7} b _ {7} \right\rangle\right) / 2 \sqrt {2}
$$

$$
\left| \psi_ {3} \right\rangle = \left(\left| a _ {0} b _ {0} \right\rangle + \left| a _ {1} b _ {1} \right\rangle + \left| a _ {2} b _ {2} \right\rangle + \left| a _ {3} b _ {3} \right\rangle - \left| a _ {4} b _ {4} \right\rangle - \left| a _ {5} b _ {5} \right\rangle - \left| a _ {6} b _ {6} \right\rangle - \left| a _ {7} b _ {7} \right\rangle\right) / 2 \sqrt {2}
$$

$$
\left| \psi_ {4} \right\rangle = \left(\left| a _ {0} b _ {0} \right\rangle - \left| a _ {1} b _ {1} \right\rangle + \left| a _ {2} b _ {2} \right\rangle - \left| a _ {3} b _ {3} \right\rangle - \left| a _ {4} b _ {4} \right\rangle + \left| a _ {5} b _ {5} \right\rangle - \left| a _ {6} b _ {6} \right\rangle + \left| a _ {7} b _ {7} \right\rangle\right) / 2 \sqrt {2}
$$

$$
\left| \psi_ {5} \right\rangle = \left(\left| a _ {0} b _ {0} \right\rangle + \left| a _ {1} b _ {1} \right\rangle - \left| a _ {2} b _ {2} \right\rangle - \left| a _ {3} b _ {3} \right\rangle - \left| a _ {4} b _ {4} \right\rangle - \left| a _ {5} b _ {5} \right\rangle + \left| a _ {6} b _ {6} \right\rangle + \left| a _ {7} b _ {7} \right\rangle\right) / 2 \sqrt {2}
$$

$$
\left| \psi_ {6} \right\rangle = \left(\left| a _ {0} b _ {0} \right\rangle - \left| a _ {1} b _ {1} \right\rangle - \left| a _ {2} b _ {2} \right\rangle + \left| a _ {3} b _ {3} \right\rangle - \left| a _ {4} b _ {4} \right\rangle + \left| a _ {5} b _ {5} \right\rangle + \left| a _ {6} b _ {6} \right\rangle - \left| a _ {7} b _ {7} \right\rangle\right) / 2 \sqrt {2}
$$

$$
\left| \psi_ {7} \right\rangle = \left(\left| a _ {0} b _ {4} \right\rangle + \left| a _ {1} b _ {5} \right\rangle + \left| a _ {2} b _ {6} \right\rangle + \left| a _ {3} b _ {7} \right\rangle - \left| a _ {4} b _ {0} \right\rangle - \left| a _ {5} b _ {1} \right\rangle - \left| a _ {6} b _ {2} \right\rangle - \left| a _ {7} b _ {3} \right\rangle\right) / 2 \sqrt {2}
$$

$$
\left| \psi_ {8} \right\rangle = \left(\left| a _ {0} b _ {4} \right\rangle - \left| a _ {1} b _ {5} \right\rangle + \left| a _ {2} b _ {6} \right\rangle - \left| a _ {3} b _ {7} \right\rangle - \left| a _ {4} b _ {0} \right\rangle + \left| a _ {5} b _ {1} \right\rangle - \left| a _ {6} b _ {2} \right\rangle + \left| a _ {7} b _ {3} \right\rangle\right) / 2 \sqrt {2}
$$

$$
\left| \psi_ {9} \right\rangle = \left(\left| a _ {0} b _ {4} \right\rangle + \left| a _ {1} b _ {5} \right\rangle - \left| a _ {2} b _ {6} \right\rangle - \left| a _ {3} b _ {7} \right\rangle - \left| a _ {4} b _ {0} \right\rangle - \left| a _ {5} b _ {1} \right\rangle + \left| a _ {6} b _ {2} \right\rangle + \left| a _ {7} b _ {3} \right\rangle\right) / 2 \sqrt {2}
$$

$$
\left| \psi_ {1 0} \right\rangle = \left(\left| a _ {0} b _ {4} \right\rangle - \left| a _ {1} b _ {5} \right\rangle - \left| a _ {2} b _ {6} \right\rangle + \left| a _ {3} b _ {7} \right\rangle - \left| a _ {4} b _ {0} \right\rangle + \left| a _ {5} b _ {1} \right\rangle + \left| a _ {6} b _ {2} \right\rangle - \left| a _ {7} b _ {3} \right\rangle\right) / 2 \sqrt {2}
$$

To generate the eleven orthogonal high-dimension Bell states, Alice needs to perform the local operations in the state  $|\varphi \rangle$ . By adjusting the

phase shifters to introduce the corresponding phases for the paths  $a_{i}(i = 0,1,\ldots ,7)$ , the Bell states  $|\psi_i\rangle (i = 0,1,2,\dots,6)$  are constructed. For example, by adding the corresponding phases  $\pi$  on paths  $a_{i}(i = 1,3,5,7)$ ,  $|\psi_0\rangle = (|a_0b_0\rangle - |a_1b_1\rangle + |a_2b_2\rangle - |a_3b_3\rangle + |a_4b_4\rangle - |a_5b_5\rangle + |a_6b_6\rangle - |a_7b_7\rangle) / \sqrt{2}$  is generated. However, for constructing the states  $|\psi_i\rangle (i = 7,8,9,10)$ , a two-step process is required. Firstly, we need to rearrange the sequence of the modes  $b$  while keeping modes  $a$  unchanged. The modes  $b$  is labeled as  $b_{4}, b_{5}, b_{6}, b_{7}, b_{0}, b_{1}, b_{2}, b_{3}$ . Secondly, we introduce the corresponding phases of 0 and  $\pi$  to paths  $a_{i}$ $(i = 0,1,\ldots ,7)$ . Consequently, we obtain eleven eight-dimensional Bell states, which represent the encoded states after Alice's local operation.

Performing the high-dimensional Bell state measurement. After preparing the eleven Bell states, we proceed to construct a  $16 \times 16$  matrix denoted as  $U_{16} = U_{2} \otimes U_{2} \otimes U_{2} \otimes U_{2}$  for the high-dimensional Bell state measurement, where  $U_{2} = \left( \begin{array}{cc} 1 & 1 \\ 1 & -1 \end{array} \right) / \sqrt{2}$  (see Supplementary Note 2 for details).  $U_{16}$  is the evolution matrix with the labels  $a_{0},\ldots,a_{7}$ , and  $b_{0},\ldots,b_{7}$  arranged sequentially for both the 16 input and output modes. For the mode sequences  $a_{0}, b_{4},\ldots,a_{3}, b_{7}, a_{4}, b_{0},\ldots,a_{7}, b_{3}$  for  $|\psi_i\rangle (i = 7,8,9)$ , we only need to change the rows  $U_{16}$  according to the input modes sequence which will result in another unitary matrix  $U^{\prime}_{16}$  (see Supplementary Note 3 for details). Considering that our chip is not large enough to realize the protocol directly, we combine the evolution matrix realized by MZIs on Alice's part  $U_{16}$  to construct a new  $16 \times 16$  unitary matrix  $U^{last}_{16}$  (see Supplementary Note 3 for details), which is realized experimentally by the square decomposition[27]. After passing through the unitary matrix  $U^{\prime\prime}_{16}$ , the residual pump beam and other unwanted light are filtered out by the off-chip bandpass filter, leaving the signal photons injected into the single photon detectors (SNSPDs). Because the eleven input Bell states give a totally different coincidence pattern at different outputs, the desired two-photon coincidence events are registered to distinguish them. For the linear optics, the number of the distinguished Bell states with our method for the dimension of  $2^{n}$  is  $2^{n} + 2^{n-1} - 1$ , which is described in Supplementary Note 2.

# Results for high-dimension dense coding

The tomography of eight-dimensional Bell states for quantum superdense coding is experimentally performed as shown in Fig. 2. To initial the process, we carefully prepare the Bell state by entangling them in the path degree. For the eight-dimensional Bell state  $|\varphi \rangle = (|a_0b_0\rangle + |a_1b_1\rangle + |a_2b_2\rangle + |a_3b_3\rangle + |a_4b_4\rangle + |a_5b_5\rangle + |a_6b_6\rangle + |a_7b_7\rangle) / 2\sqrt{2}$ . By precisely adjusting the phases of heaters in our 16-mode photonic chip, we ensure that the eight waveguide modes associated with  $a_i$  ( $i = 0, 1, \ldots, 7$ ) them are matched to the first eight modes in sequential order. Similarly, the modes  $b_i$  ( $i = 0, 1, \ldots, 7$ ) are matched to the last eight modes as shown in Fig. 2a. In order to improve the overall system quality for the quantum superdense coding, the probability for single pair generation ratio via SFWM processing is set as 0.001, which means that the probability of the multipair emission can be neglected (see Supplementary Note 4 for details). An interference visibility of  $0.994 \pm 0.009$  is obtained by testing the interference quality by changing the input phases between the two input squeezed states and injecting them into the 50:50 beam splitters as shown in Fig. 2b. Subsequently, we perform the measurements on modes  $a$  and  $b$  in the joint bases  $\{|a_i\rangle, (|a_i\rangle + |a_j\rangle) / \sqrt{2}, (|a_i\rangle + |a_j\rangle) / \sqrt{2}\}$  ( $i, j = 0, 1, \ldots, 7, i \neq j$ ) and  $\{|b_i\rangle, (|b_i\rangle + |b_j\rangle) / \sqrt{2}, (|b_i\rangle + |b_j\rangle) / \sqrt{2}\}$  ( $i, j = 0, 1, \ldots, 7, i \neq j$ ). This allows us to obtain a total of 4096 data points which is sufficient for us to calculate the fidelity for the high-dimensional Bell state (see Supplementary Note 5 for details). For the eight-dimensional Bell state, the 64-density matrix elements  $\rho_{ii,jj}(i,j = 0, 1, \ldots, 6, 7)$  are important for the calculation of fidelity which can be obtained as shown in Fig. 2c. Similar operations are also performed for 2- and 4-dimensional entangled states (see Supplementary Note 5 for

![](images/65a60f57b7c8e4cfc5e78eb7cbd020eafc56a89d6dc0f2a0abbd57d04c3a205d.jpg)

![](images/7a27ed636f90c2d633d3a14ea7d107d3b9fdc08c9762f6d0b61066b0a4624130.jpg)

![](images/48ae2e0acd55dcf2b0d4b9db0d5b4e6fc93df49c2bf750ebd1a142a116138dea.jpg)

Fig. 2 | Experimental results for matrix tomography of high-dimensional  
![](images/7f2b1d829029dc06051c9bbd812b7bc22bde3ece341607f3e5004e64b5351d40.jpg)  
pair is produced. c The real parts of density matrix elements for calculating the fidelity of the eight-dimensional Bell state are listed. The theoretical values for these elements are 0.125. d The fidelities calculated for two, four, and eight-dimensional Bell states. The uncertainties in the fidelities, extracted from these density matrices, are calculated using a Monte Carlo routine, assuming Poissonian errors.

Fig. 3 | Measured probabilities. Alice sends the eleven four-dimensional Bell states to Bob, and Bob performs a coincidence measurement on the two photons and obtains the probabilities for each input state.  
![](images/9a0fb319dc9c7904f715ebe55d3b68fbb1e491e82bc921747b6dbce4142d58a2.jpg)  
Bell state. a The scheme for performing the tomography process. Modes  $a$  and  $b$  are initially separated and rearranged, and then the measurement of different bases is performed individually. b The generation of a single photon pair by interfering with two weak squeezed states. When the relative phase is set to  $\pi /2$ , a degenerate photon-

details). The fidelities for the constructed Bell states for 2, 4, and 8 dimensions are calculated as  $0.993(2)$ ,  $0.983(2)$  and  $0.973(2)$  as shown in Fig. 2d. The uncertainties in the state fidelity, extracted from these density matrices, are calculated using a Monte Carlo routine assuming Poissonian statistics.

We then prepared the eleven eight-dimensional Bell states  $|\psi_i\rangle (i = 0,1,\dots ,9,10)$ , along with their corresponding BSMs for demonstrating the quantum superdense coding protocol. For each basis, the data acquisition time is set to be  $10\mathrm{min}$  to sample approximately 30,000 counts. The resulting fidelities for each input state are shown in Fig. 3. The average fidelity is calculated as 0.951(1). The channel capacity CC represents the maximum attainable mutual information  $I(x;y)$  for a given set of conditional probabilities  $p(y|x)$ , where  $x$  is the Bell state prepared by Alice and  $y$  is

the state measured by Bob,  $p(x)$  is the generation probability for the state preparation which is set as a constant value of 1/11. This channel capacity is defined as:

$$
C C = \sum_ {y = 0} ^ {1 0} \sum_ {x = 0} ^ {1 0} p (y | x) p (x) \log \left[ \frac {p (y | x)}{\sum_ {x = 0} ^ {1 0} p (y | x) p (x)} \right]
$$

In our experiment, the channel capacity is  $3.021 \pm 0.003$  bits which overcomes the classical maximum channel capacity of 3 bits. Next, we manage to use the quantum photonic chip to transmit a specific picture

![](images/0efef6fd72e18e5c81c6233818c9db9a59273f21b37c0209e5345bafcedad25e.jpg)  
Fig. 4 | Transmitting an eleven-color pie picture using encoded information. The number 0-9 and the background are encoded into  $\left| \psi_0 \right\rangle$  to  $\left| \psi_{10} \right\rangle$  and transmitted from Alice to Bob. a Original eleven-color picture with  $147 \times 154$  pixels. b Image received using quantum superdense coding.  
a

![](images/8d4c20d3caa78070541b3167df3e9c91a48683b31a44e986fdd0cac63110b560.jpg)  
b

![](images/c62ba778d555810ee6fbae978b798bcbbf18a69bed33c7e01f22e7ec59356472.jpg)  
Fig. 5 | Comparison with previous experiments. The calculated channel capacity via different dimensions in previous experiments for quantum superdense coding is listed. The data points for each experiment are accompanied by their respective references. The dashed line represents the theoretical channel capacity using our method, where no photon number resolving detectors and no other degrees of freedom are used.

which consists of about 22,600 pixels. The numbers 0 to 9 and the background are encoded into the eleven high-dimensional Bell states from  $|\psi_0\rangle$  to  $|\psi_{10}\rangle$ . The output-measured results for each input state are recorded by a counter with their respective arriving times. The recovered picture after the noise channel is shown in Fig. 4, exhibiting a fidelity of 0.956(2).

# Discussion

It is worth mentioning that the precise assessment of the channel capacity relies heavily on the quality of the system. To distinguish  $N$  Bell states for a channel capacity of  $\log_2N$ , the noise term for each input state is proportionally increased by a factor of  $N - 1$ . In addition, as the dimensions increase, the fidelity typically decreases because more heaters are required to be controlled precisely. Therefore, in our experiment, we choose eight-dimensional quantum superdense coding as a proof-of-concept demonstration.

In summary, a large-scale, programmable, and universal quantum photonic chip incorporating a degenerate high-dimensional source part and a high-dimensional BSM part is, for the first time, experimentally demonstrated. Significantly, we have attained the implementation of eight-dimensional quantum superdense coding on this quantum photonic chip for demonstrating the quantum advantage. Through precise adjustment of this exceptionally high-quality chip, we have achieved the highest channel capacity to date compared to previous quantum photonic systems as shown in Fig. 5. The utilization of high-dimensional quantum superdense coding holds tremendous importance for a new generation of quantum networks $^{28,29}$ . Our high-dimension dense coding protocol can also be used to

construct a multi-user practical quantum network when every two nodes share high-dimension entangled states (see Supplementary Note 6 for details). Thanks to our reliance on quantum entanglement, we not only augment the channel capacity in comparison to classical coding methods but also guarantee enhanced security similar to the renowned E91 protocol<sup>30</sup>. Moreover, in the context of constructing a quantum network for multiple users<sup>31</sup>, our approach enables enhanced resource efficiency and compatibility with high-dimensional quantum computation<sup>32-34</sup>. Our findings will serve as a catalyst for the improvement of integrated quantum chip technologies and the exploration of high-dimensional entanglement, stimulating further advancements in these pivotal areas.

# Data availability

The data that support the findings of this study are available from the corresponding authors upon reasonable request.

# Code availability

The codes for simulation and data processing are available from the corresponding authors upon reasonable request.

Received: 27 June 2024; Accepted: 7 March 2025

Published online: 18 March 2025

# References

1. Bennett, C. H. & Wiesner, S. J. Communication via one-and two-particle operators on Einstein-Podolsky-Rosen states. Phys. Rev. Lett. 69, 2881-2884 (1992).  
2. Nielsen, M. A. & Chuang, I. L. Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, 2000).  
3. Mattle, K., Weinfurter, H., Kwiat, P. G. & Zeilinger, A. Dense coding in experimental quantum communication. Phys. Rev. Lett. 76, 4656-4659 (1996).  
4. Schuck, C., Huber, G., Kurtsiefer, C. & Weinfurter, H. Complete deterministic linear optics Bell state analysis. Phys. Rev. Lett. 96, 190501 (2006).  
5. Barreiro, J. T., Wei, T. C. & Kwiat, P. G. Beating the channel capacity limit for linear photonic superdense coding. Nat. Phys. 4, 282-286 (2008).  
6. Williams, B. P., Sadlier, R. J. & Humble, T. S. Superdense coding over optical fiber links with complete bell-state measurements. Phys. Rev. Lett. 118, 050501 (2017).  
7. Hu, X. M. et al. Beating the channel capacity limit for superdense coding with entangled ququarts. Sci. Adv. 4, eaat9304 (2018).  
8. Schaetz, T. et al. Quantum dense coding with atomic qubits. Phys. Rev. Lett. 93, 040505 (2004).  
9. Fang, X., Zhu, X., Feng, M., Mao, X. A. & Du, F. Experimental implementation of dense coding using nuclear magnetic resonance. Phys. Rev. A 61, 022307 (2000).

10. Calsamiglia, J. Generalized measurements by linear elements. Phys. Rev. A 65, 030301 (2002).  
11. Grice, W. P. Arbitrarily complete Bell-state measurement using only linear optical elements. Phys. Rev. A 84, 042331 (2011).  
12. Cover, T. M. & Thomas, J. A. Elements of Information Theory (Wiley, New York, 2012).  
13. Schaeff, C. et al. Scalable fiber integrated source for higher-dimensional path-entangled photonic quNits. Opt. Express 20, 16145 (2012).  
14. Hu, X. M. et al. Efficient generation of high-dimensional entanglement through multipath down-conversion. Phys. Rev. Lett. 125.9, 090503 (2020).  
15. Cao, H. et al. Distribution of high-dimensional orbital angular momentum entanglement over a 1 km few-mode fiber. Optica 7, 232-237 (2020).  
16. Krenn, M. et al. Generation and confirmation of a  $(100 \times 100)$ -dimensional entangled quantum system. Proc. Natl. Acad. Sci. USA 111, 6243-6247 (2014).  
17. Riedmatten, H. D., Marcikic, I., Zbinden, H. & Gisin, N. Creating high dimensional entanglement using mode-lockedlasers. Quantum Inf. Comput. 2, 425-433 (2002).  
18. Kues, M. et al. On-chip generation of high-dimensional entangled quantum states and their coherent control. Nature 546, 622-626 (2017).  
19. Cozzolino, D., Lio, B. D., Bacco, D. & Oxenløwe, L. K. High-dimensional quantum communication: benefits, progress, and future challenges. Adv. Quantum Technol. 2, 1900038 (2019).  
20. Wang, J. et al. Multidimensional quantum entanglement with large-scale integrated optics. Science 360.6386, 285-291 (2018).  
21. Carolan, J. et al. QUANTUM OPTICS. Universal linear optics. Science 349.6249, 711-716 (2015).  
22. Qiang, X. et al. Large-scale silicon quantum photonics implementing arbitrary two-qubit processing. Nat. Photon. 12, 534-539 (2018).  
23. Mahmudlu, H. et al. Fully on-chip photonic turnkey quantum source for entangled qubit/qudit state generation. Nat. photonics 17, 518-524 (2023).  
24. Li, Y. et al. Quantum Fredkin and Toffoli gates on a versatile programmable silicon photonic chip. npj Quantum Inf. 8, 112 (2022).  
25. Huang, J. et al. Demonstration of hypergraph-state quantum information processing. Nat. Commun. 15, 2601 (2024).  
26. Zhu, H. H. Laser & Photonics Reviews (Wiley, 2014)  
27. Clements, W. R., Humphreys, P. C., Metcalf, B. J., Kolthammer, W. S. & Walmsley, I. A. Optimal design for universal multiport interferometers. Optica 3, 1460-1465 (2016).  
28. Wu, F., Bai, M. Q., Zhang, Y. C., Liu, R. J. & Mo, Z. W. Cyclic and cyclic controlled quantum teleportation in a high-dimension system. Int. J. Quantum Inf. 18, 2050012 (2020).  
29. Wang, C., Deng, F. G., Li, Y. S., Liu, X. S. & Long, G. L. Quantum secure direct communication with high-dimension quantum superdense coding. Phys. Rev. A 71.4, 044305 (2005).  
30. Ekert, A. K. Quantum cryptography based on Bell's theorem. Lett 67.6, 661-663 (1991).  
31. Liu, X. S., Long, G. L., Tong, D. M. & Li, F. General scheme for superdense coding between multiparties. Phys. Rev. A 65.2, 022304 (2002).  
32. Chi, Y. et al. A programmable audit-based quantum processor. Nat. Commun. 13, 1166 (2022).

33. Wang, Y., Hu, Z., Sanders, B. C. & Kais, S. Qudits and high-dimensional quantum computing. Front. Phys. 8, 589504 (2020).  
34. Zheng, Y. et al. Multichip multidimensional quantum networks with entanglement retrievability. Science 381.6654, 221-226 (2023).

# Acknowledgements

This work was supported by the National Research Foundation (NRF2022-QEP2-02-P16), IMDA and the National Research Foundation Singapore (FCP-NTU-RG-2022-013).

# Author contributions

Y.L. and A.Q.L. jointly conceived the idea. Y.L. performed the numerical simulations and theoretical analysis. Y.L., H.Z., W.L., H.C., F.G., and X.L. did the fabrication and experiments. Y.L., H.Z., X.Z., and L.C.K. were involved in the discussion and data analysis. Y.L., Q.S., A.Q.L., X.Z., and L.C.K. wrote the manuscript. X.W., M.F.K., L.C.K., and A.Q.L. supervised and coordinated all the work. All authors commented on the manuscript.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at

https://doi.org/10.1038/s41534-025-01007-y.

Correspondence and requests for materials should be addressed to Hong Cai, Muhammad Faeyz Karim, Xiaoqi Zhou, Qinghua Song or Ai Qun Liu.

Reprints and permissions information is available at

http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

© The Author(s) 2025