# A universal programmable Gaussian boson sampler for drug discovery

Received: 16 December 2022

Accepted: 1 September 2023

Published online: 12 October 2023

![](images/28c623a52ebb9ffb058f84d97db031d5ec3bf9a6cdbd60d8683be34f40ce6cb8.jpg)

Check for updates

Shang Yu  $^{1,2,3,4,7}$ , Zhi-Peng Zhong  $^{1,7}$ , Yuhua Fang  $^{5,7}$ , Raj B. Patel  $^{2}$ , Qing-Peng Li  $^{1}$ , Wei Liu  $^{3,4}$ , Zhenghao Li  $^{2}$ , Liang Xu  $^{1}$ , Steven Sagona-Stophel  $^{2}$ , Ewan Mer  $^{2}$ , Sarah E. Thomas  $^{2}$ , Yu Meng  $^{3,4}$ , Zhi-Peng Li  $^{3,4}$ , Yuan-Ze Yang  $^{3,4}$ , Zhao-An Wang  $^{3,4}$ , Nai-Jie Guo  $^{3,4}$ , Wen-Hao Zhang  $^{3,4}$ , Geoffrey K. Tranmer  $^{5}$ , Ying Dong  $^{1}$ , Yi-Tao Wang  $^{3,4}$ , Jian-Shun Tang  $^{3,4,6}$ , Chuan-Feng Li  $^{3,4,6}$ , Ian A. Walmsley  $^{2}$  & Guang-Can Guo  $^{3,4,6}$

Gaussian boson sampling (GBS) has the potential to solve complex graph problems, such as clique finding, which is relevant to drug discovery tasks. However, realizing the full benefits of quantum enhancements requires large-scale quantum hardware with universal programmability. Here we have developed a time-bin-encoded GBS photonic quantum processor that is universal, programmable and software-scalable. Our processor features freely adjustable squeezing parameters and can implement arbitrary unitary operations with a programmable interferometer. Leveraging our processor, we successfully executed clique finding on a 32-node graph, achieving approximately twice the success probability compared to classical sampling. As proof of concept, we implemented a versatile quantum drug discovery platform using this GBS processor, enabling molecular docking and RNA-folding prediction tasks. Our work achieves GBS circuitry with its universal and programmable architecture, advancing GBS toward use in real-world applications.

Quantum computing technology has developed rapidly in recent years $^{1-7}$ , and an exponential 'speed-up' compared to classical methods has been experimentally demonstrated for certain algorithms $^{4,5,7-9}$ . Quantum sampling tasks, like boson sampling $^{10-12}$ , have proven to be challenging to solve within a reasonable time frame on classical computers, but can be implemented and solved efficiently on photonic processors $^{1,13}$ . As a variant of boson sampling, Gaussian boson sampling (GBS) $^{14}$  uses squeezed light to encode and carry the input states, making the method easier to scale. The method shows great capacity to demonstrate quantum advantage in optical systems $^{5,7}$ .

The prospect of achieving quantum advantage has motivated the discovery of several real-world applications, such as dense graph searching $^{15,16}$ , molecular vibronic spectra calculations $^{6,17}$  and molecular docking $^{18}$ . For these tasks, a GBS device should be programmable and scalable to a large number of modes $^{5,6}$ ; however, achieving such capability is a challenging task $^{16}$  due to the experimental complexity involved in preparing the large number of individually addressable input states and phase-shifters necessary to achieve universal programmmability $^{5,6}$ .

Time-bin encoding of Gaussian states is an effective means of achieving scale and programmmability $^{7,16,19-21}$ . First, it is resource efficient because only one squeezed source and one detector are required $^{16}$ .

![](images/ca2339001913de4a3f78ac4d99401e5847eb748d0b7142f0b4e2b12b9542f3c0.jpg)  
a  
b

![](images/5ac937e2808dce10114c5547e33f3e1833fb92f176468a62bf016019af97fb54.jpg)

![](images/06905b8e35ba66d2050593d733c460197bbb7330769f9238c00b887751cf1d44.jpg)  
c  
Fig. 1|Implementation, verification and application of Abacus. a, The GBS machine consists of four main parts: (1) squeezed-state preparation, (2) QPU, (3) QuSAM and (4) detection. The red lines represent the squeezed-light signal, while the dark red arrows indicate the direction of the signal light within the QPU loop. For clarity, the control system, which includes three arbitrary waveform generators and a control computer, is not shown. The abbreviations indicate PBS, half-wave plate (HWP), right-angle prism mirrors (RAP), roof prism mirror (RF), cylindrical lens (CL), beam splitter (BS) and time-to-digital converter (TDC). b, GBS results, probability distribution of all 496 two-photon detection events in a 32-mode experiment. The horizontal axis numbering represents a methodical ordering by  $(i,j)$  from 0 to  $C_2^{32} - 1$  ( $C_k^n = n! / (k!(n - k)!$ ), corresponding to the detection of a photon in output mode  $(i,j)$ . c, GBS results, probability distribution of all 1,820 four-photon detection events in a 16-mode experiment. The horizontal axis numbering represents a methodical ordering by  $(i,j,k,l)$  from 0 to  $C_4^{16} - 1$ , corresponding to the detection of a photon in output mode  $(i,j,k,l)$ .

![](images/492f41f605bd2a0ccd285019efb91b40fb5f2f21767b4fe0100e56b0bce6fbb4.jpg)  
d  
d, Finding the maximum weighted clique in a 32-node graph. The probabilities of the six-node cliques in the graph  $\mathcal{G}^{32}$  are shown at the bottom with box-and-whisker plots. The corresponding graph is shown above; the labels beside the nodes denote the corresponding order and the weight of the nodes is represented by their size. The statistics are calculated from ten individual experiments, each with around 300 samples. The wide blue boxes of varying shades, and the red box, symbolize the GBS experimental results. The lower and upper limits of the 'whisker' denote the minimum and maximum values (excluding outliers), respectively; and the horizontal black (or white) lines inside the boxes indicate the median value. The shaded regions denote the cliques identified through GBS results, with the red-shaded regions representing the maximum weighted cliques. The classical uniform sampling results are portrayed by slim yellow boxes of varying shades. In a few cases, outlier data are displayed as circles that match the color of the corresponding box. The diagram shows that the GBS machine can identify the maximum weighted clique with a higher success rate.

Second, time-bin operation provides phase stability and exhibits losses comparable with other approaches[22]. Time-bin interferometers show flexibility in reconfiguration because they can realize arbitrary-dimension linear transformations with the same setup. Recently, quantum computational advantage has been demonstrated with a programmable time-bin-encoded GBS machine[7], though in that research, universality was sacrificed to avoid the accumulation of loss.

This prompts us to consider a universal and programmable time-bin GBS machine that can fulfill various practical tasks. The GBS algorithm can potentially be applied to many important problems and enhance their solution, for example, the complete subgraph (clique) finding task $^{23,24}$ . Some structure-based drug design methods, like molecular docking or protein folding prediction, can be interpreted as equivalent to the problem of finding the maximum weighted clique in their corresponding graph models $^{18,25,26}$ . Hence, a universal, programmable, GBS machine equipped with freely adjustable squeezers and interferometer can be utilized for these tasks and extend the range of practical applications based on graph theory. Inspired by this prospect, in this work we built a scalable, universal and programmable time-bin GBS machine, making a stride toward using GBS in drug discovery applications.

# Results

# Programmable GBS machine and sampling results

The GBS machine, named 'Abacus', comprises four primary components: a tunable squeezed-state source for precise light state control $^{27-30}$ ; a quantum processing unit based on the architecture of Clements et al. $^{31}$  that ensures stable, programmable quantum information processing $^{32}$ ; a quantum sequential access memory with a 180-meter optical fiber designed for efficient data storage and cyclic operations; and a detection module featuring superconducting nanowire single-photon detectors (SNSPDs) for collision-free photon measurements. Further details are provided in the Methods section 'Details about the programmable GBS machine', as well as in Supplementary Information Sections 1 and 2.

As illustrated in Fig. 1a, this time-bin-encoded GBS machine enables us to expand the number of modes arbitrarily and freely set the required squeezing parameters, denoted as  $r_i$ , and linear transformation matrix for the tasks with a series of electro-optic modulators (EOMs). Thus, this universal and programmable architecture supports the running of arbitrary GBS circuits on this machine. As a concrete example, benefitting from these features, the adjacency matrix  $\mathcal{A}$  of a graph  $\mathcal{G}$  can be encoded into this GBS machine by decomposing  $\mathcal{L}(\mathcal{A})$  (Laplacian of the adjacency matrix of graph  $\mathcal{G}$ ) after a suitable re-scaling, as shown in the inset of Fig. 1a.

The validation of Abacus is demonstrated by the sampling results from running two random GBS circuits with different dimensions. The normalized photon sampling distribution probabilities are shown in Fig. 1b,c. In Fig. 1b, a 32-mode random interferometer is chosen, and only four squeezers are turned on, with  $r_{1-3,32} = 2.23$ . The statistical

results of all two-photon detection events are plotted, and the total variation distance between experimental and theoretical results is 0.054. Similarly, the four-photon distribution pattern is shown in Fig. 1c, conducted on a 16-mode GBS with all 16 squeezers turned on and  $r_{\mathrm{max}} = 1.8$  (here, the total variation distance is 0.175). We also use the modified likelihood ratio test introduced in ref. 33 to exclude the thermal state and distinguishable photon hypotheses; these details can be found in Supplementary Information Section 2G. These results show that Abacus can perform the sampling tasks with high fidelity.

# Finding the maximum weighted clique with GBS

Not only can GBS be used to demonstrate quantum advantage in the laboratory $^{5,7}$  as a near-term specific-function quantum computer, it can also be used in solving certain problems in real-world applications. Here, we use Abacus to solve max clique decision problems, which are NP-hard (non-deterministic polynomial time) problems in graph theory and play a crucial role in many applications $^{25}$ .

Clique refers to all the maximal complete subgraphs in a graph  $\mathcal{G}$ ; the clique-finding problem has a complexity which scales exponentially with the number of nodes. Here, we use Abacus to find the maximum weighted clique in a graph. A 32-node weighted graph  $\mathcal{G}^{32}$  is artificially constructed here (details are shown in Supplementary Information Sections 3 and 4), and the essential step is encoding  $\mathcal{G}^{32}$  onto our GBS machine. Using the method introduced in refs. 18,24, we perform Takagi-Autonne decomposition to the Laplacian of graph  $\mathcal{G}^{32}$ , with appropriate re-scaling, and obtain the unitary operation  $U$  and the squeezing parameters  $r_i$ , which are required to be programmed on the GBS (Methods). Then, we control the acoustic-optical modulator chopper with an arbitrary waveform generator to pump the periodically polled potassium titanyl phosphate (ppKTP) waveguide with 32 sequential pulses. EOMO is used to adjust  $r_i$  for each time bin, and  $U$ , the unitary operation, is achieved by adjusting the input voltages of EOM1 and EOM2 in the time-bin interferometer. After mapping  $\mathcal{G}^{32}$  onto Abacus, around 300 five (or more)-photon sampling results are collected in each experiment. Using these sampling data, we can find the cliques with nodes corresponding to the 30-time postprocessed sampling results (see details in Methods). Figure 1d displays all six-node cliques and their corresponding probabilities. The maximum weighted clique stands out as the most probable among them. In comparison to classical sampling with the same postprocessing iterations, GBS demonstrates a substantially higher probability of successfully finding the maximum weighted clique, approximately twice as much. This indicates that GBS can perform the clique-finding task with high efficiency<sup>18</sup>.

# Molecular docking with GBS

If the graph is constructed according to an actual system occupying the network structure, the clique-finding task then could be utilized to find the optimal subset corresponding to the maximum weighted clique. Recent research shows that the information of the best docking orientation of the protein-ligand complex can be predicted by the

Fig. 2 | Molecular docking and RNA-folding prediction results obtained with Abacus. a, The docking pair of PARP-CQ (see text). Abacus is encoded with a 24-node BIG and finds the maximum weighted clique, using 347 sample data and 100-iteration local searches. b, Another 28-node BIG constructed by the complex of TACE-TS (see text), using 254 sample data and 10 iterations. In a and b the colored spheres denote the pharmacophore points we considered in the experiment (cyan: hydrogen-bond acceptor, HA, ha; blue: hydrogen-bond donor, HD, hd; yellow: negative charge, NC; orange: aromatic, AR, ar; and we use capital letters to represent pharmacophore points in the protein and lowercase letters to represent pharmacophore points in the ligand.) The sphere meshes in the ligands are other possible pharmacophore points but are not considered in our experiments. The shaded region in panels a and b denotes the maximum weighted cliques, as determined by the experimental results. All the cliques found from GBS experiments are shown in the pie charts; the maximum weighted

cliques in both cases have a major proportion in the experimental results obtained from QIVS. More details are found in Supplementary Information Sections 5 and 6. c,d, The GBS-based RNA-folding prediction results for two RNA sequences (in c, accession no. AH003339; in d, accession no. AB041850). The max weighted cliques are highlighted in colored regions; they represent the most likely folding structures. The four colored circles (A, G, U, C) in the RNA structure represent the four different bases and the gray dashed lines represent the false negative base-pair matching. The colors of nodes within the clique, outlined by solid black lines, correspond to the predicted stems (base-pairs with matching shadow colors) in the RNA folding structure. For example, in c, the yellow node corresponds to the predicted stem with base-pairs 10-25, 11-24, 12-23 and 13-22. The cliques encircled by dashed pink (c) and yellow lines (d) represent other folding structures, though they are less accurate. More details are shown in Supplementary Information Section 7.

maximum weighted clique of a corresponding binding interaction graph (BIG), which is a weighted graph constructed based on docking modes between ligand and receptor $^{18}$ . In the BIG, the weighted nodes represent the interacting pharmacophore pairs weighted by potential, and the edges represent the compatible contacts

(Methods). By encoding the BIG on Abacus, we can solve molecular docking problems by finding the maximum weighted clique in the  $\mathrm{BIG}^{18,34}$ , as we demonstrated in Fig. 1d.

To demonstrate the capability of GBS in solving molecular docking problems, we build a quantum inverse virtual screening (QIVS)

![](images/b54521565a022e4e806394aedd8959f558d671ba0f8ba1e0cbc77c37cf0e8931.jpg)  
a

![](images/3858932cfe8c3baf1e1dd3ed8a07246e4317f6a6a712ac100ccc0f665aed3ccc.jpg)  
b

![](images/c63fa295d23f2be76797bedb4c00fd986ec32e61d70657b3cda772bebfb8c7dd.jpg)  
C

![](images/95d9962660aaaf5abadf08dbf6aa0efb3766728c9a939465b64dc968c02c6ea7.jpg)  
d

platform based on Abacus and use two pairs of protein-ligand complexes with different drug properties to demonstrate the ability of QIVS in drug design and verified the practicability of the platform. In the first case (Fig. 2a), a 28-node BIG  $\mathcal{G}_{\mathrm{PARP - CQ}}^{28}$  is constructed based on the Poly (ADP-Ribose) polymerase-1 (PARP) and an 8-chloroquinazolinone-based inhibitor (PARP-CQ), which is a promising candidate for anticancer drugs[35-37] and for some central nervous system diseases such as Parkinson's and Alzheimer's diseases[38,39]. The structures of ligand and protein and their BIG are shown in Fig. 2a. By encoding  $\mathcal{G}_{\mathrm{PARP - CQ}}^{28}$  onto Abacus, we collect the sampling results and find the associated cliques with postprocessing (that is, shrink and local search)[18]. The pie chart in Fig. 2a shows all the cliques we find with GBS experiments, where each sector corresponds to one of the various cliques with corresponding weights. The maximum weighted clique (with seven nodes and weight  $= 6.8144$ ) occupies the major proportion. This demonstrates we can use Abacus to find the best binding pose (Fig. 2a, right side) of this complex with a high success rate.

In the second case (Fig. 2b), we use the complex of tumor necrosis factor (TNF) converting enzyme (TACE) and thiomorpholine sulfonamide hydroxamate inhibitor (TACE-TS) $^{40}$ , which are involved in inflammatory diseases $^{41}$ . Aromatic pharmacophore points are included and, in order to increase the accuracy of the docking results, an improved algorithm is used. Considering the fact that the interaction strength between various pharmacophore points may create some behavior differences, the variable distance is used to compare the distance between different points when we construct the 24-node BIG  $\mathcal{G}_{\mathrm{TACE-TS}}^{24}$ . GBS experiments then are performed by programming the circuit with another set of polarization rotation  $(\theta_{i})$ , phase shift  $(\varphi_{i})$  and  $r_i$ . We find 11 cliques in the sampling results; and six of them (maximum size  $N = 9$ ) appear with relatively high probabilities. The protein-ligand docking position suggested by the maximum weighted clique (with weight  $(w) = 4.5657$ ) is shown on the right in Fig. 2b. Compared with the method used by Banchi et al. $^{18}$ , the improved method we proposed here obtains a more accurate binding pose result; the detailed comparison analysis is shown in the Supplementary Information Sections 5 and 6.

Although there is relatively high loss in the experiment, the maximum weighted clique can still be found with a high success probability through postprocessing, which is robust with regard to noise<sup>18</sup>. The above results, predicted by GBS experiments, agree well with the outcomes obtained from the corresponding co-crystal structures, which can be found by reviewing complex structures within a certain distance  $(\tau)$  to each other<sup>40,42,43</sup>, through their entries in the Protein Data Bank (PDB) for PARP1 (PDB entry no. 7ONR) and TACE (PDB entry no. 2A8H).

# GBS for RNA-folding prediction

The molecular docking process relies heavily on the protein structure, and the fact is that many pathogenic proteins associated with human diseases cannot be targeted by conventional small-molecule drugs or biomacromolecules $^{44}$ . In recent years, nucleic acid drugs have received attention in the pharmaceutical field as a potential solution to overcome the limitations of existing target drugs and to treat previously untargeted diseases. Predicting RNA structures has become an important task in discovering these nucleic acid drugs, as it can aid in identifying potential drug targets and predicting small-molecule-drugs' interactions with RNA molecules $^{45}$ . However, predicting RNA structures by calculation has proven difficult, as only a few RNA structures are known. Nevertheless, exciting work in protein and RNA structure prediction has emerged recently, with artificial intelligence technology being particularly prominent $^{45,46}$ . Quantum computational technology also has great potential to solve this folding prediction task $^{47,48}$ . However, no solution to this problem has yet been experimentally demonstrated on devices that can exhibit quantum computational advantages (such as GBS devices) due to their programmability limitations.

Using our universal programmable GBS device Abacus, we use a method, inspired by Tang et al.26, for predicting RNA sequence folding. This approach involves modeling the RNA sequence as a weighted full stem graph (WFSG) and then encoding it into our universal programmable GBS device. The WFSG captures all possible folding information of the RNA sequence, where each node represents a possible stem in the sequence, and the edges indicate the co-existence between them26. The weight of each node corresponds to the length of the stem it represents. Then, the RNA-folding prediction can be obtained by finding the maximum weighted cliques in WFSG26. To demonstrate the effectiveness of our GBS machine in solving this problem, we conducted two experiments with different RNA fragments on Abacus; the results are shown in Fig. 2c,d.

In the first example, we predicted the secondary structure of an RNA sequence (accession no.: AH003339) by encoding the corresponding 32-node WFSG into Abacus. We found two maximum weighted cliques, and the Matthews correlation coefficient (MCC) of the best one (shown in light orange shadow in Fig. 2c) reached 0.953, which outperforms FOLD $^{49}$  (best case) and RNAProbing $^{50}$ , with MCC values of only 0.864 and 0.934, respectively. In the second experiment, we use the RNA sequence of the organism Alanine (accession no.: ABO41850) and encoded its corresponding WFSG, which had 31 nodes, into Abacus by modifying the control program. The best prediction with MCC = 1.00 among the two results is shown in Fig. 2d, and it is more accurate than those obtained by other methods, with FOLD achieving MCC = 0.870 and RNAProbing achieving MCC = 0.914. Details of the true reference folding and other information are provided in Supplementary Information Section 7.

# Discussion

The scalability and programmability of our universal GBS machine enable its utilization in real-world applications, as demonstrated in this work. The ability to program arbitrary graphs demonstrates that drug discovery tasks, such as molecular docking or RNA-folding prediction, can be performed efficiently by a purpose-built quantum computer. However, unequivocal quantum computational advantage $^{5,7}$  has not been realized in our experiments due to photon loss. Although the question of whether GBS can outperform improved classical algorithms or quantum-inspired algorithms remains open $^{51}$ , and the potential for GBS to demonstrate computational advantages also relies on the properties of the encoded graph, we remain optimistic about scaling Abacus to several hundred modes using the 'multicore encoding' and 'distributed computing' methods. This scalability holds the potential to unlock quantum advantages in some specific real-world applications. Additionally, it is crucial to consider practical applications that encompass more complex protein structures, larger pharmacophore points and longer RNA sequences, which also necessitate the use of such a large-scale GBS machine. For a comprehensive discussion on scaling our GBS machine by minimizing loss and utilizing the multicore encoding and distributed computing methods, refer to Supplementary Information Section 8. Apart from offering programmability and universality, this work presents a promising hardware solution for the near-term industrial implementation of quantum computing in the biopharmaceutical industry. It also paves the way for diverse real-world applications in the future.

# Methods

# Details about the programmable GBS machine

The GBS machine shown in Fig. 1a, which we named Abacus, can be divided into four main parts: (1) Tunable squeezed-state source. The pump light from a mode-locked pulsed laser (80 MHz, 773 nm,  $\sim 150$  fs) is reduced in repetition rate to 40 MHz by an acoustic-optic modulator. The electro-optic modulator (EOMO) and polarization beam splitter (PBS) are used to adjust the pump energy of each pulse. This controls the squeezing degree  $(r_i)$  of the squeezed vacuum states in each time

bin. The spectral mode of the pump light is modulated by a spatial light modulator, two gratings and two cylindrical lenses (CLs). Then, spectrally uncorrelated two-mode squeezed light is generated by pumping a 10-mm-long ppKTP waveguide $^{27-29}$ . Following interference at a 50:50 beamsplitter, a series of individually addressable single-mode squeezed states can be efficiently prepared $^{30}$ . (2) Quantum processing unit (QPU). The single-mode squeezed states are then sent into a time-bin interferometer, which is programmed for a specific unitary operation. This is achieved according to Clements' architecture $^{31}$ , which is realized by a group of Mach-Zehnder interferometers consisting of two high-speed optical switches EOMa and EOMb, a 7.5 m delay line (to combine or separate two adjacent time bins) and a linear transformation  $T(\theta, \varphi) = \left( \begin{array}{cc} e^{i\varphi} \cos \theta & -\sin \theta \\ e^{i\varphi} \sin \theta & \cos \theta \end{array} \right)$ , where  $\varphi$  represents the phase shift and  $\theta$  denotes the polarization rotation, these are achieved by EOM1 and EOM2, respectively. Since the optical path before and after  $T(\theta, \varphi)$  passes through the same low-loss free-space delay line, the phase stability of the setup is well guaranteed, and the non-uniform loss expected in the fiber-loop scheme $^{32}$  is mitigated. (3) Quantum sequential access memory (QuSAM). In each loop of evolution, the quantum memory is achieved by a 180-meter-long optical fiber delay line. The QuSAM ensures that the last time bin has completed the operation in one cycle before the first time bin enters into the next cycle. With a 4f beam-shaper system, we can efficiently couple the light from free space into single-mode optical fiber and realize a low-loss time-bin memory (with total efficiency of  $-94\%$ ) by reshaping the spatial mode of the beam. (4) Detection module. SNSPDs are used to detect the single-photon events, since our experiments are performed in the collision-free space. To avoid the issue of the SNSPD dead-time ( $\lesssim 50$  ns) being longer than the time interval between two adjacent time bins (25 ns), we use another EOM to separate two adjacent time bins and use two SNSPDs for detection. The throughput of each round-trip in the system is approximately  $82\%$ . In the case of Fig. 1b, the average count rate of two-fold events is 45 counts per second, and in the case of Fig. 1c, the four-fold average count rate is 24 counts per second, which are calculated from  $10^{7}$  samples in 10 min (the repetition rate of each individual sampling experiment is 20 kHz). More details are provided in Supplementary Information Section 2.

This GBS machine has two main advantages compared with previous works: First, universal operation is possible since both the squeezers and arbitrary unitary matrices can be programmed on the time-bin interferometer. This makes it suitable not only for molecular docking of various molecules but also for other applications. Our architecture also provides flexibility in scaling to many modes via the control software. Compared to previous work $^{5,7}$ , our GBS setup supports adjustments to all the parameters:  $n$  squeezing parameters  $r_i$  and  $n(n - 1)/2$  parameters for an arbitrary  $U$ . Our time-bin-encoding GBS setup is resource-efficient for scaling up. Specifically, when the number of modes increases, we do not need to add more squeezed-light sources. Independent of the number of modes we required in experiments, two analog EOMs (that is, EOM1 and EOM2) assisted with two light-switch EOMs (that is, EOMa and EOMb) are sufficient to realize any linear transformation. A resource advantage is also exhibited in the detection. As we discussed in the main text and Supplementary Information Section 2E, two SNSPDs are enough for collecting the ~30-mode GBS samples.

Second, non-uniform loss in previous time-bin interferometer implementations appears across different time-bin modes, and this limits the ability to perform an arbitrary unitary operation<sup>32</sup>. In this setup, we use a free-space delay line with transmittance 0.995 to greatly reduce the non-uniform loss. Thus, the mitigated non-uniform loss and dispersion-free features in our setup can better exhibit universality. The time-bin-encoded GBS scheme is intrinsically phase stable<sup>20</sup>. As shown in Fig. 1a, since every time bin goes through the same path, the slow phase fluctuations (caused by mechanical vibrations, temperature

drifts or other unpredictable environmental noise) can be neglected compared to the high sampling rate where a sample is obtained in  $50~\mu \mathrm{s}$ . The  $7.5\mathrm{m}$  free-space delay line is isolated from the environment to ensure that the phase between two adjacent time bins can be stable for up to  $5\mathrm{min}$ . This is enough for collecting  $10^{6}$  samples within  $1\mathrm{min}$ .

# Mapping a graph onto GBS

As for a loopless, undirected and vertex-weighted graph  $\mathcal{G}$ , the corresponding adjacency matrix  $\mathcal{A}$  is a symmetric  $(0,1)$ -matrix, where the vertex weights are given by  $\omega_{i}$ , and the entries are  $\mathcal{A}_{ii} = \omega_i$ ,  $\mathcal{A}_{ij} = 1$  if there is an edge between vertex  $i$  and  $j$  and  $\mathcal{A}_{ij} = 0$  if otherwise. After finding the adjacency matrix  $\mathcal{A}$  of a graph, then the key step to encode the graph  $\mathcal{G}$  onto GBS machine is connecting  $\mathcal{A}$  with the sampling matrix  $A$  through some proper transformation (the inset in Fig. 1a provides an example possibility).

For a pure Gaussian state, the sampling matrix  $A$  can be written as  $B \oplus B^{\prime}$ ; then the Hafnian  $\mathrm{Haf}(A)$  can be expressed as  $\mathrm{Haf}(B \oplus B^{\prime}) = |\mathrm{Haf}(B)|^{2}$ . Thus, the output probability of obtaining the sampling pattern  $s$  can be expressed as

$$
\Pr (s) = \frac {\left| \mathrm {H a f} \left(B _ {s}\right) \right| ^ {2}}{n _ {1} ! n _ {2} ! \cdots n _ {N} ! \sqrt {\det (\sigma + \mathbb {I} / 2)}}. \tag {1}
$$

An immediate idea is to replace  $B$  here with the adjacency matrix  $\Omega (\mathcal{D} - \mathcal{A})\Omega$ , where  $\Omega$  is a diagonal matrix with elements  $(\Omega_{ii} = \omega_i)$  and  $\mathcal{D}$  is the degree matrix of  $\mathcal{A}$  defined as  $\mathcal{D}_{ii} = \sum_{j}\mathcal{A}_{ij}$ . However, this does not work, since the eigenvalues of  $B$  should be within the interval [0, 1), such that the covariance matrix of the pure Gaussian state is positive definite[24]. From an experimental point of view, this restriction is because the eigenvalues of  $B$  denote the brightness of squeezing sources in the experiment. We can decompose the symmetric matrix  $B$  as[52]

$$
B = U \oplus_ {i} ^ {N} \tanh  \left(r _ {i}\right) U ^ {T}, \tag {2}
$$

where  $U$  is the unitary matrix applied in experiments and  $r_i$  denotes the squeezing parameters for the vacuum states, as shown in Supplementary Information Fig. 1a. Thus, the value of eigenvalues  $\tanh(r_i)$  should be between 0 and 1, and 1 cannot be reached because that would correspond to infinite brightness.

To satisfy this condition, we can rescale  $\mathcal{A}$  by carefully choosing the parameters  $c$  and  $\alpha$  when we add the weight of each vertex to the adjacency matrix:

$$
\mathcal {A} ^ {\prime} = \Omega (\mathcal {D} - \mathcal {A}) \Omega , \tag {3}
$$

where  $\Omega$  is a diagonal matrix with elements  $\Omega_{ii} = c(1 + \alpha \omega_i)$ . By choosing parameters  $c$  and  $\alpha$  suitably, we can obtain an  $\mathcal{A}'$  with the correct spectrum. Additionally, we also can maximize the maximum input photon number in the experiment over the choice of  $c$  and  $\alpha$ . The  $\mathcal{D}$  matrix is introduced so that the  $\mathcal{A}'$  matrix is positive definite<sup>18</sup>. But when GBS is operated in the collision-free subspace,  $\mathcal{D}$  will not affect the results of Haf  $(\mathcal{A}')$  and, according to Banchi et al.<sup>18</sup>, Haf  $(\mathcal{A}') = \operatorname*{det}(\Omega) \operatorname*{Haf}(\mathcal{A})$ . More details can be found in Supplementary Information Section 3.

# Constructing the adjacency matrix of a BIG

Inverse virtual screening is a structure-based approach to find potential drug targets for a given drug or active small molecule by calculation. For known drugs, inverse virtual screening technology can do the drug repositioning and provide reference for the study of new drug effects and drug side effects $^{53}$ . For active small molecules, inverse virtual screening technology can predict their potential targets, identify their therapeutic potential in diseases and provide direction for the later transformation and mechanism research of active compounds $^{54,55}$ .

If the graph is constructed according to an actual system occupying the network structure, the clique-finding task then could be utilized to find the optimal subset corresponding to the maximum weighted clique. Recent research shows that the information of the best docking orientation of the protein-ligand complex can be predicted by the maximum weighted clique of a corresponding  $\mathrm{BIG^{18}}$ . In the docking scheme of bioactive molecules, the BIG is a weighted graph constructed based on docking modes between ligand and receptor. In the BIG, the weighted nodes represent the interacting pharmacophore pairs weighted by potential and the edges represent the compatible contacts.

The edge generation in a BIG is determined by comparing the distances between the pharmacophore points on the ligand  $(D_{\mathrm{L}}^{x - x})$  and binding  $(D_{\mathrm{P}}^{x - x})$  sites. This is illustrated in boxes 1 and 2 of Supplementary Information Fig. 21. Each possible contact is represented by a vertex in BIG, and the corresponding weight is determined by the contact potential (shown in Supplementary Information Fig. 23). A BIG with only weighted vertices is illustrated in box 3 in Supplementary Information Fig. 21.

While the geometric distances between two contacts should normally be approximately the same on both the ligand and the binding site, they can exhibit some degree of flexibility[18]. A pair of contacts, for example, (C, a) and (B, c), is considered a  $\tau$ -flexible contact pair if the difference between the distances of the pharmacophore points on the ligand (corresponding to vertices 'C' and 'B') and the distances of the pharmacophore points on the binding site (corresponding to vertices 'a' and 'c') is within  $\tau + 2\varepsilon$ , as depicted in Supplementary Information Fig. 21. The constants  $\tau$  and  $\varepsilon$  describe the flexibility constant and interaction distance, respectively, and they determine which edges appear in the BIG, as shown in boxes 4 and 5 in Supplementary Information Fig. 21.

It should be noted that, in the work of Banchi et al. $^{18}$ ,  $\tau$  and  $\varepsilon$  are set as constants for simplicity, as discussed above. However, more accurate methods can account for the changeable flexibility of the ligand and receptor $^{18,56}$ .  $\tau$  and  $\varepsilon$  are no longer set as constants and can vary according to the various pharmacophore points in the contacts.

By encoding the BIG on Abacus, we can solve molecular docking problems by finding the maximum weighted clique $^{18,34}$  in the BIG, as we demonstrated, with results shown in Fig. 2.

To better demonstrate the capability of Abacus in solving molecular docking problems, we build a QIVS platform, as shown in Supplementary Information Fig. 22. Inverse virtual screening (IVS) is a technology for finding potential drug targets for a given drug or small active molecule by calculations, and it has been applied to identifying targets, research on side effects and drug repurposing[57,58]. In such a computer-aided drug design method as IVS, a large amount of computational resources are usually required, since a huge number of proteins in the database need to be screened by this docking program to identify potential targets for a given ligand, with a run-time that scales with the size of the ligands and receptors.

Unlike the classical IVS, we replace the traditional molecular docking process with GBS and achieve a more efficient and accurate QIVS. According to the selected ligand and potential proteins, a corresponding BIG,  $g_{\mathrm{BIG}}$ , is constructed (shown in Supplementary Information Fig. 22) and is then encoded into the GBS machine. The best binding pose can be determined by finding the maximum weighted clique of this graph  $g_{\mathrm{BIG}}$  (ref. 18), a task for which our programmable Abacus is well suited. More details can be found in Supplementary Information Section 5.

# Postprocessing method with 'Shrinking' and 'Local search'

The presence of various types of noise in the experiments affects the probability of the maximum weighted clique obtained from the raw experimental data. In some cases, the subgraph obtained may not even be a clique. Certain types of noise are unavoidable in experiments (for example, photon loss), in which case we can use the raw experimental data as a seed which can be input to a postprocessing algorithm to

generate cliques at a high-rate. The postprocessing method introduced in Banchi et al. $^{18}$  is very useful for this purpose. We briefly review the postprocessing method and discuss how we use it in our experiments.

We use 'Greedy Shrinking' to ensure the subgraph obtained from the raw GBS data is a clique by removing the nodes based on the degree and weight of the nodes until it forms a clique. To obtain the maximum weighted clique, which usually occurs with a larger number of nodes, we perform an expansion with a 'Local search'. This expands the clique by adding neighboring nodes within several iterations of the algorithm to generate the largest clique. This is represented as the 'Postprocessing' module in Supplementary Information Fig. 22. Strawberry Fields<sup>59</sup> is used to perform the postprocessing. Further details can be found in the work of Banchi et al.<sup>18</sup>

# Further scaling by reducing loss

In our experiment, simultaneously achieving universality and programmmability comes at the cost of loss, which increases with the circuit depth or, more specifically, the number of cycles. This relatively large loss exists in our GBS machine prohibits demonstration of quantum computational advantage. Although we mainly focus on the mapping of GBS to real-world applications in this work, with further developments toward low-loss optical components, realization of quantum advantage should be possible in the future.

Loss in Abacus can be reduced by various methods. Loss in the experiment mainly comes from (1) the coupling loss from the ppKTP waveguide to single-mode fiber, (2) insertion loss caused by EOMs, (3) the limited coupling efficiency from free space to QuSAM and (4) the limited detection efficiency of SNSPDs. Particularly, for the EOM insertion loss (2) and the limited QuSAM coupling efficiency (3), due to the characteristics of our free-space loop architecture, the total loss will increase exponentially with the loss inside the loop. Therefore, when the number of modes is large, small improvements to these sources of loss will greatly improve the overall loss.

First, for the coupling loss from the ppKTP waveguide to single-mode fiber, mode shaping techniques may be applied to match the spatial mode of light from the ppKTP waveguide to that of the fiber, potentially improving the coupling efficiency to greater than 0.9 (ref. 60). Second, the insertion loss of EOMs or other optical elements is unavoidable. However, an EOM with a shorter and lower loss crystal—driven by a higher-gain amplifier—could be used. Combining the actions of EOM1 and EOM2 into an integrated EOM operation will further reduce the loss experienced upon reflection and absorption at the end faces. Transmission has been shown to reach higher than 0.99 after optimizing the  $\mathrm{EOM^7}$ . Third, the coupling efficiency from free space to QuSAM can be improved up to  $-0.97$  by using a 4f or 8f imaging systems through spherical lenses and graded-index lens fiber couplers (see Madsen et al. ). In addition, a Herriott long-distance delay line can be used as a quantum memory for minimizing the loss[61]. Finally, the detection efficiency can be improved with the latest generation of nanowire detectors with detection efficiencies at  $1,550\mathrm{nm}$  of up to 0.95. Through these methods to minimize the loss, the single-loop transmission can potentially reach  $-90\%$ . Thus, our GBS setup can be extended to at least 60 modes (for example, a 60-mode GBS experiment will have total transmission efficiency of  $-0.12\%$  found from the product of the several involved transmission efficiencies, as  $0.90^{61}$  (loop efficiency, to the loop-count power)  $\times 0.9$  (coupling efficiency from ppKTP to fiber)  $\times 0.944$  (filter after ppKTP induce)  $\times 0.93$  (coupling efficiency from QPU to fiber)  $\times 0.973$  (transmission of demultiplexer)  $\times 0.95$  (detection efficiency of SNSPDs).

# Implement displacement and photon-number resolving detection in time-domain GBS

Displacement operation  $D(\alpha)$  is entirely feasible to include in Abacus. To achieve this, the photon source module needs to be rebuilt, which involves incorporating an optical parametric oscillator after

the mode-locked laser (Chameleon) to generate a  $1,550\mathrm{nm}$  laser. This laser is subsequently split into two separate paths. In one path, the light serves as the pump for generating squeezed states. In the other path, the light is utilized as a coherent state to achieve the displacement operation. The addition of a delay line ensures that the coherent state and squeezed state reach the beamsplitter simultaneously, enabling optimal interference at the output. Two EOMs facilitate the program-mability of the amplitude and phase of the displacement operation. For more detailed information, please refer to Supplementary Information Section 2H.

Our time-domain GBS machine Abacus can also implement photon-number resolving detection with a transition edge sensor (TES). The TES initially needs to be cooled below its transition temperature of approximately  $100\mathrm{mK}$  and then heated back to its transition temperature by applying a bias current[62]. To maintain the TES at this temperature, it should be operated inside a dilution refrigerator. After a photon absorption event, it takes approximately  $5\mu \mathrm{s}$  for the TES to return to its original temperature. Therefore, the repetition rate of TES detectors is usually limited to around  $100 - 300\mathrm{kHz}$ . This necessitates the installation of a demultiplexer in our time-domain GBS setup. To address this limitation for a time-domain GBS machine, a demultiplexer needs to be installed. By employing a loop structure, it is straightforward to implement a nine-channel demultiplexer using a single EOM. The EOM enables us to manipulate the polarization of photons in each time bin, thereby determining whether they exit the system through PBSs or undergo internal reflection and remain within the loop. The design corresponding to this approach is depicted in Supplementary Information Fig. 15, and further detailed information can be found in Supplementary Information Section 2l.

# Pharmacophore points selection

The selection of PARP-PARPi pharmacophore points—where PARPi refers to PARP inhibitors, including the PARP-CQ we used as shown in Fig. 2a—is according to previous research focused on PARP-PARPi relationships $^{63,64}$ . These articles have demonstrated important amino acid residues from the protein and functional groups from the inhibitor that will influence the efficacy of the protein-ligand interactions. We choose some of them for the GBS machine due to the size of the experiment.

The selection of pharmacophore points in this work is typically based on prior knowledge from experimental studies, structural analysis or computational modeling of similar PARP-PARPi complexes. The selection of pharmacophore points, such as hydrogen-bond acceptors and donors, negative charges, pi-pinteraction and aromatic ring in the PARP-PARPi complex is based on their known importance in the interaction between the protein, PARP and the ligand. These pharmacophore characteristics play a crucial role in the binding affinity and specificity of ligands to protein targets.

Hydrogen-bond interactions are important for stabilizing the protein-ligand complex. Such an interaction occurs between the hydrogen atom of the ligand and a hydrogen-bond acceptor or donor group on the protein. These pi-pi interactions contribute to the overall binding strength and specificity by forming specific and directional interactions; they involve the stacking of aromatic rings in the ligand and the protein. These interactions are driven by the pi electrons present in the aromatic systems and contribute to the stability of the complex. Such pi-pi-interactions are often found in protein-ligand interactions and can enhance binding affinity. Some articles have reviewed pharmacophores in a PARP inhibitor, and in those studies the nicotinamide component is considered as a hydrogen-bond donor and acceptor, as well as being a part of pi-pi interaction with the tyrosine residue $^{63}$ .

Aromatic rings are frequently present in ligands and proteins and can participate in various types of interactions, including pi-pi stacking, hydrophobic interactions and van der Waals interactions. Aromatic rings provide a hydrophobic surface that can interact with

complementary hydrophobic regions in the protein, contributing to the overall binding affinity. The aromatic ring at the tail of the compound is also critical, and we take it as a pharmacophore as well<sup>42</sup>.

Negative charges, represented by negatively charged atoms or functional groups, also play a major role in the PARP-PARPi complex. Such a negative charge can interact with positively charged residues on the protein, like arginine or lysine, through electrostatic interactions, and these interactions can also contribute to the stability of the complex and enhance ligand binding.

# Classical combinatorial optimization methods

In Supplementary Information Section 9, we discuss more details about the classical or quantum-inspired approaches like genetic algorithms, quantum approximate optimization algorithm, quantum annealing and digital annealer, which also can be used to realize clique finding and other similar tasks.

# Data availability

Source data are provided with this paper. The experimental data used in this paper are also publicly available in a Zenodo repository at https://doi.org/10.5281/zenodo.8306628 with a citable release at ref. 65.

# Code availability

The codes used to generate the corresponding adjacency matrices in Fig. 2a-d, analyze experimental data and implement the Bron-Kerbosch and Maximum Clique algorithms for result verification are available at https://doi.org/10.5281/zenodo.8284043 with a citable release at ref. 66.

# References

1. Spring, B. J. et al. Boson sampling on a photonic chip. Science 339, 798-801 (2013).  
2. Barends, R. et al. Digitized adiabatic quantum computing with a superconducting circuit. Nature 534, 222-226 (2016).  
3. Mohseni, M. et al. Commercialize quantum technologies in five years. Nature 543, 171-174 (2017).  
4. Arute, F. et al. Quantum supremacy using a programmable superconducting processor. Nature 574, 505-210 (2019).  
5. Zhong, H.-S. et al. Quantum computational advantage using photons. Science 370, 1460-1463 (2020).  
6. Arrazola, J. M. et al. Quantum circuits with many photons on a programmable nanophotonic chip. Nature 591, 54-60 (2021).  
7. Madsen, L. S. et al. Quantum computational advantage with programmable photonic processor. Nature 606, 75-81 (2022).  
8. Zhang, J. et al. Observation of a many-body dynamical phase transition with a 53-qubit quantum simulator. Nature 551, 601-604 (2017).  
9. Bernien, H. et al. Probing many-body dynamics on a 51-atom quantum simulator. Nature 551, 579-584 (2017).  
10. Tillmann, M. et al. Experimental boson sampling. Nature Photon. 7, 540-544 (2013).  
11. Brod, D. J. et al. Photonic implementation of boson sampling: a review. Adv. Photon. 1, 034001 (2019).  
12. Lund, A. P. et al. Boson sampling from a Gaussian state. Phys. Rev. Lett. 113, 100502 (2014).  
13. Wang, H. et al. High-efficiency multiphoton boson sampling. Nat. Photonics 6, 361-365 (2017).  
14. Hamilton, C. S. et al. Gaussian boson sampling. Phys. Rev. Lett. 119, 170501 (2017).  
15. Arrazola, J. M. & Bromley, T. R. Using Gaussian boson sampling to find dense subgraphs. Phys. Rev. Lett. 121, 030503 (2018).  
16. Sempere-Llagostera, S., Patel, R. B., Walmsley, I. A. & Kolthammer, W. S. Experimentally finding dense subgraphs using a time-bin encoded Gaussian boson sampling device. Phys. Rev. X 12, 031045 (2022).

17. Huh, J., Guerreschi, G. G., Peropadre, B., McClean, J. R. & Aspuru-Guzik, A. Boson sampling for molecular vibronic spectra. Nature Photon. 9, 615-620 (2015).  
18. Banchi, L., Fingerhuth, M., Babej, T., Ing, C. & Arrazola, J. M. Molecular docking with Gaussian boson sampling. Science Advances 6, eaax1950 (2020).  
19. Motes, K. R., Gilchrist, A., Dowling, J. P. & Rohde, P. P. Scalable boson sampling with time-bin encoding using a loop-based architecture. Phys. Rev. Lett. 113, 120501 (2014).  
20. He, Y. et al. Time-bin-encoded boson sampling with a single-photon device. Phys. Rev. Lett. 118, 190501 (2017).  
21. Deshpande, A. et al. Quantum computational advantage via high-dimensional Gaussian boson sampling. Sci. Adv. 8, eabi7894 (2022).  
22. Qi, H., Helt, L. G., Su, D., Vernon, Z., & Brádler, K. Linear multiport photonic interferometers: loss analysis of temporally-encoded architectures. Preprint at https://arxiv.org/abs/1812.07015 (2018).  
23. Plummer, M. D. Well-covered graphs: a survey. Quaest. Math. 16, 253-287 (1993).  
24. Brádler, K., Dallaire-Demers, P.-L., Rebentrost, P., Su, D. & Weedbrook, C. Gaussian boson sampling for perfect matchings of arbitrary graphs. Phys. Rev. A 98, 032310 (2018).  
25. Karp, R. M. Reducibility among combinatorial problems. in Complexity of Computer Computations. The IBM Research Symposia Series (eds. Miller, R. E. et al.) 85-103 (Springer, 1972).  
26. Tang, M., Hwang, K. & Kang, S. H. StemP: a fast and deterministic stem-graph approach for RNA secondary structure prediction. IEEE/ACM Trans. Comput. Biol. Bioinform. https://doi.org/10.1109/TCBB.2023.3253049 (2023).  
27. Eckstein, A., Christ, A., Mosley, P. J. & Silberhorn, C. Highly efficient single-pass source of pulsed single-mode twin beams of light. Phys. Rev. Lett. 106, 013603 (2011).  
28. Harder, G. et al. Single-mode parametric-down-conversion states with 50 photons as a source for mesoscopic quantum optics. Phys. Rev. Lett. 116, 143601 (2016).  
29. Bell, B. A., Thekkadath, G. S., Ge, R., Cai, X. & Walmsley, I. A. Testing multi-photon interference on a silicon chip. Opt. Express 27, 35646 (2019).  
30. Lvovsky, A. I., Squeezed light. Preprint at https://arxiv.org/pdf/1401.4118 (2016).  
31. Clements, W. R., Humphreys, P. C., Metcalf, B. J., Kolthammer, W. S. & Walmsley, I. A. Optimal design for universal multiport interferometers. Optica 12, 1460-1465 (2016).  
32. Motes, K. R., Dowling, J. P., Gilchrist, A. & Rohde, P. P. Simple scheme for universal linear-optics quantum computing with constant experimental complexity using fiber loops. Phys. Rev. A 92, 052319 (2015).  
33. Spagnolo, N. et al. Experimental validation of photonic boson sampling. Nature Photon. 8, 615-620 (2015).  
34. Kuhl, F. S., Crippen, G. M. & Friesen, D. K. A combinatorial algorithm for calculating ligand binding. J. Comput. Chem. 5, 24-34 (1984).  
35. Powell, C. et al. Pre-clinical and clinical evaluation of PARP inhibitors as tumour-specific radiosensitisers. Cancer Treat. Rev. 36, 566-575 (2010).  
36. Lu, Y. et al. Double-barreled gun: combination of PARP inhibitor with conventional chemotherapy. Pharmacol. Therapeut. 188, 168-175 (2018).  
37. Tangutoori, S., Baldwin, P. & Sridhar, S. PARP inhibitors: a new era of targeted therapy. Maturitas 81, 5-9 (2015).  
38. Olsen, A. L. & Feany, M. B. PARP inhibitors and Parkinson's disease. New Engl. J. Med. 380, 492-494 (2019).  
39. Martire, S., Mosca, L. & d'Erme, M. PARP-1 involvement in neurodegeneration: a focus on Alzheimer's and Parkinson's diseases. Mech. Ageing Dev. 146, 53-64 (2015).

40. Levin, J. I. et al. Acetylenic TACE inhibitors. Part 3: thiomorpholine sulfonamide hydroxamates. Bioorg. Med. Chem. Lett. 16, 1605-1609 (2006).  
41. Chemaly, M. et al. Role of tumour necrosis factor alpha converting enzyme (TACE/ADAM17) and associated proteins in coronary artery disease and cardiac events. Arch. Cardiovas. Dis. 110, 700-711 (2017).  
42. Johannes, J. W. et al. Discovery of 5-4-[(7-ethyl-6-oxo-5, 6-dihydro-1, 5-naphthyridin-3-yl) methyl] piperazin-1-yl-N-methylpyridine-2-carboxamide (AZD5305): a PARP1-DNA trapper with high selectivity for PARP1 over PARP2 and other PARPs. J. Med. Chem. 64, 14498-14512 (2021).  
43. Berman, H., Henrick, K. & Nakamura, H. Announcing the worldwide protein data bank. Nat. Struct. Mol. Biol. 10, 980-980 (2003).  
44. Santos, R. et al. A comprehensive map of molecular drug targets. Nat. Rev. Drug Discov. 16, 19-34 (2017).  
45. Townshend, R. J. L. et al. Geometric deep learning of RNA structure. Science 373, 1047-1051 (2021).  
46. Jumper, J. et al. Highly accurate protein structure prediction with AlphaFold. Nature 596, 583-589 (2021).  
47. Emani, P. S. et al. Quantum computing at the frontiers of biological sciences. Nat. Methods 18, 701-709 (2021).  
48. Zaborniak, T. et al. A QUBO model of the RNA folding problem optimized by variational hybrid quantum annealing. In 2022 IEEE International Conference on Quantum Computing and Engineering (QCE) 174-185 (IEEE, 2022).  
49. Mathews, D. H. et al. Incorporating chemical modification constraints into a dynamic programming algorithm for prediction of RNA secondary structure. Proc. Natl Acad. Sci. USA 101, 7287-7292 (2022).  
50. Wirecki, T. K. et al. RNAProbe: a web server for normalization and analysis of RNA structure probing data. *Nucleic Acids Res.* **48**, 292-299 (2020).  
51. Oh, C., Lim, Y., Wong, Y., Fefferman, B. & Jiang, L. Quantum-inspired classical algorithm for molecular vibronic spectra. Preprint at https://arxiv.org/abs/2202.01861 (2022).  
52. Kruse, R. et al. Detailed study of Gaussian boson sampling. Phys. Rev. A 100, 032326 (2019).  
53. Kharkar, P. S., Warrier, S. & Gaud, R. S. Reverse docking: a powerful tool for drug repositioning and drug rescue. Future Med. Chem. 6, 333-342 (2014).  
54. Bhattacharjee, B. & Chatterjee, J. Identification of proapoptopic, anti-inflammatory, anti-proliferative, anti-invasive and antiangiogenic targets of essential oils in cardamom by dual reverse virtual screening and binding pose analysis. Asian Pac. J. Cancer P. 14, 3735-3742 (2013).  
55. Carvalho, D. et al. Structural evidence of quercetin multi-target bioactivity: a reverse virtual screening strategy. Eur. J. Pharm. Sci. 106, 393-403 (2017).  
56. Dias, R. & de Azevedo Jr, W. F. Molecular docking algorithms. Curr. Drug Targets 9, 1040-1047 (2008).  
57. Rognan, D. Structure-based approaches to target fishing and ligand profiling. Mol. Inform. 29, 176-187 (2010).  
58. Koutsoukas, A. et al. From in silico target prediction to multi-target drug design: current database, methods, and application. J. Proteomics 74, 2554-2574 (2011).  
59. Killoran, N. et al. Strawberry Fields: a software platform for photonic quantum computing. Quantum 3, 129 (2019).  
60. Sun, B. et al. On-chip beam rotators, polarizers and adiabatic mode converters through low-loss waveguides with variable cross-sections. Light Sci. Appl. 11, 214 (2022).  
61. Enomoto, Y., Yonezu, K., Mitsuhashi, Y., Takase, K. & Takeda, S. Programmable and sequential Gaussian gates in a loop-based single-mode photonic quantum processor. Sci. Adv. 7, eabj6624 (2021).

62. Irwin, K. An application of electrothermal feedback for high resolution cryogenic particle detection. Appl. Phys. Lett. 66, 1998-2000 (1995).  
63. Kumar, C., Lakshmi, P. T. V. & Arunachalam, A. Structure based pharmacophore study to identify possible natural selective PARP-1 trapper as anti-cancer agent. Comput. Biol. Chem. 80, 314-323 (2019).  
64. Zandarashvili, L. et al. Structural basis for allosteric PARP-1 retention on DNA breaks. Science 368, eaax6367 (2020).  
65. Yu, S. et al. Data for the paper titled 'A universal programmable Gaussian boson sampler for drug discovery'. Zenodo https://doi.org/10.5281/zenodo.8306628 (2023).  
66. Yu, S. et al. Codes for the paper titled 'A universal programmable Gaussian boson sampler for drug discovery'. Zenodo https://doi.org/10.5281/zenodo.8308479 (2023).

# Acknowledgements

S. Yu would like to express special gratitude to M. Tang and S. Kang for their assistance with RNA-folding prediction methods. We thank Q. Wang, B. Bell, Z. Jia, X. Xu, Z. Liu and A. Zhang for the helpful discussions, and S. Sempere-Llagostera for providing useful feedback on the manuscript. This work was supported by Engineering and Physical Sciences Research Council and Quantum Computing and Simulation Hub (T001062), UK Research and Innovation Future Leaders Fellowship (MR/W011794/1), EU Horizon 2020 Marie Sklodowska-Curie Innovation Training Network (no. 956071, 'AppQInfo'), International Postdoctoral Exchange Fellowship Program 2022 (no. PC2022049), Innovation Program for Quantum Science and Technology (no. 2021ZD0301200), China Postdoctoral Science Foundation funded projects (no. 2020M681949), the National Natural Science Foundation of China (nos. 11821404, 12174370 and 12174376), the Youth Innovation Promotion Association of Chinese Academy of Sciences (no. 2017492) and the Fok Ying-Tong Education Foundation (no. 171007).

# Author contributions

S.Y. and J.-S.T. designed the experiment with input from R.B.P. S.Y. built the experimental setup with the help of Q.-P.L., R.B.P., L.X., Y.M., Z.-P.L., Y.-Z.Y., Z.-A.W., N.-J.G., W.-H.Z. and Y.-T.W. Z.-P.Z. developed the control system for the programmable hardware. Y.F. and G.K.T. designed the molecular docking scheme. S.Y. designed and built the squeezed-light source with the help of Y.-T.W. and R.B.P. S.Y. and Y.F. completed data

analysis with the help of W.L., J.-S.T., R.B.P. and I.A.W. S.Y., J.-S.T., Y.-T.W., S.S.-S. and Y.D. designed the further-scaling method with the help of Z.L. S.Y. and Y.F. prepared the manuscript with the help of R.B.P., Y.D., J.-S.T., Y.-T.W., Z.L., E.M., S.E.T., C.-F.L., I.A.W. and G.-C.G. All authors discussed the results and reviewed the manuscript.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s43588-023-00526-y.

Correspondence and requests for materials should be addressed to Shang Yu, Raj B. Patel, Yi-Tao Wang, Jian-Shun Tang or Chuan-Feng Li.

Peer review information Nature Computational Science thanks Leonardo Banchi and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. Primary Handling Editor: Jie Pan, in collaboration with the Nature Computational Science team.

Reprints and permissions information is available at

www.nature.com/reprints.

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2023