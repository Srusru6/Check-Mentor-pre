OPEN

# Optimal and scalable entanglement distribution over crossbar quantum networks

Bogdan-Calin Ciobanu, Luca Perju Verzotti & Pantelimon George Popescu

Crossbar networks are a cornerstone of network architectures, capable of operating both as standalone interconnections or as integral switching components in complex, multi-stage systems. The main advantages of crossbar networks are their non-blocking operation and unparalleled minimal latency. With the advent of large scale quantum networks, crossbars might be an important asset towards the Quantum Internet. This study proposes a solution for the problem of distributing entanglement within crossbar quantum networks. Entangled particles are a consumable resource in quantum networks, and are being used by most quantum protocols. By ensuring that nodes within quantum networks are being supplied with entanglement, the reliability and efficiency of the network is maintained. By providing an efficient, scalable framework that can be used to achieve optimal entanglement distribution within crossbar quantum networks, this study offers a theoretical achievement which can be also used for enhancing quantum network performance. An algorithm for selecting an optimal entanglement distribution configuration is proposed and fully tested on realistic possible configurations.

Entanglement<sup>1-3</sup> represents a uniquely quantum phenomena exhibited by systems of particles, and is an essential ingredient for quantum communications<sup>4</sup>. Entangled pairs (e-pairs) enable efficient distributed quantum computing<sup>5-8</sup>, and secure communication via quantum key distribution<sup>9,10</sup> and quantum teleportation<sup>11-14</sup>. The preservation of entanglement fidelity<sup>15</sup> is paramount in quantum communications; it hinges on the system's ability to remain isolated from any environmental interaction. This necessity poses a significant challenge: while e-pairs must be shielded from external influences to maintain high fidelity for transmissions over long distances, they also require precise manipulation and measurement.

The subject of this delicate balancing act are usually photons with polarization-encoded quantum information $^{16-19}$ . For quantum networks, these represent essential, yet exhaustible resources which are consumed during fundamental operations such as quantum teleportation and other protocols. As such, if communicating parties require reliable, sustained transmissions, it is crucial to establish an entanglement resupply system across the network $^{20-22}$ . The most straightforward method would be to physically transport a particle of an e-pair to each of the two nodes in need. This technique significantly reduces entanglement fidelity, as the entangled particles, traveling at best half the distance between nodes, given that the e-pair was generated at an intermediary node midway between the two parties, are susceptible to loss and environmental interference in the lossy transmission mediums $^{23-25}$ . This approach, however, may not be compatible with the extensive network sizes anticipated for the Quantum Internet $^{26-29}$ . The Quantum Internet is envisioned as a global network that interconnects heterogeneous quantum networks, demanding a more scalable solution.

Interconnection networks $^{30,31}$  have a pivotal role in the realm of classical computing and communications, acting as the backbone for data exchange and system integration. In the context of quantum technologies, the importance of interconnection networks is bound to be at least as significant. The interconnections of quantum systems $^{32}$  are tasked with not just the transfer of quantum information, but also with the preservation and manipulation of quantum states. Their development and optimization thus stand as a cornerstone in realizing the full potential of quantum communications and computing. Crossbar interconnection networks in particular hold significant potential due to their unique properties, like their ability to create direct and dynamic connections between inputs and outputs, which can greatly enhance the efficiency of information transmission. This is crucial in quantum computing environments where the rapid and reliable exchange of quantum states is essential.

The objective of this work is to propose and analyze the optimal strategy for distributing entanglement over crossbar quantum networks, as multiple concurrent entanglement requests would have to share the nodes and

Computer Science and Engineering Department, University POLITEHNICA of Bucharest, 60042 Bucharest, Romania.

$\text{念}$  email: pgpopescu@upb.ro

links of the interconnection network. The paper is structured as follows. In Section "Classical interconnection networks" an overview of classical interconnection networks is presented. Through Section "Challenges of concurrent entanglement distribution" entanglement distribution schemes are explored, and solutions for a basic entanglement distribution setup are provided. Section "Optimal entanglement distribution in crossbar quantum networks" describes the optimal method for choosing the entanglement distribution configuration over a crossbar quantum network. In Section "Simulation results and scalability analysis", an explicit algorithm, simulation results and interpretations are presented. The paper ends with conclusions regarding the optimality and scalability of the presented entanglement distribution algorithm.

# Classical interconnection networks

In the context of communication networks, a cornerstone of performance is the seamless and efficient transfer of data between communicating parties. The concept of interconnection networks represents the backbone of data transfer. Interconnection networks (interconnects) are complex topological structures that facilitate data transmission between multiple components. More precisely, an interconnection network is a structured arrangement of communication links and switches, designed to ensure efficient data exchange, minimize latency, or maximize throughput, depending on the chosen interconnection architecture.

Historically speaking, interconnection networks were used in telecommunication networks, namely telephone, to connect individual lines without the need of manual patching. Since then, the principles of interconnection have been adopted into broader applications, such as parallel and grid computing $^{33}$ , optical networks $^{34}$ , and network switching fabrics of the Internet.

The defining characteristic of an interconnection network is its topology. Each topology is designed to suit specific needs and scenarios, and comes with its own advantages and drawbacks<sup>31</sup>. Such topologies include Linear Arrays and Rings, which are among the simplest, with network components connected in a straight line or loop, respectively. These can offer a simple way to route data, but limited scalability. Meshes and Toruses expand upon these topologies, branching out in two or three dimensions, creating grid-like structures, hence improving flexibility. Hypercube topologies are a binary n-dimensional construct, which has a logarithmic diameter, with respect to its number of nodes. Crossbar networks offer direct connections between every input and output, and stand out for their non-blocking nature, although, in practical implementation, this advantage comes with the cost of being resource-intensive in terms of implementation.

In this work, we will focus on the crossbar topology, as it offers unparalleled non-blocking communication, due to its direct connectivity between components. Furthermore, it offers deterministic low latency communication, which is uniform and minimal across all communication scenarios. As this work is purely theoretical, we will not consider the material costs of implementing crossbar networks, although we acknowledge that it is possible they can be high, compared to alternative topologies. However, in Section "Simulation results and scalability analysis", we analyze how our proposed solution might scale by limiting the number of resources needed to interconnect vast amounts of nodes, through the well-known Benes<sup>35</sup> network topology.

As envisioned use cases of crossbar quantum networks for entanglement distribution, such networks may be deployed in order to facilitate quantum communication between arrays of quantum computers or quantum memories. Alternatively, these networks could be used to create a distributed quantum sensing infrastructure, where entanglement would be used in communication between nodes. One other use case for such a crossbar quantum network could be in the backbone of the Quantum Internet. Functions of the Quantum Internet could include applications which have no classical counterpart such as unconditionally secure communications<sup>36</sup>, or quantum teleportation networks.

# Crossbar networks

A crossbar can be defined as a network with N inputs and M outputs, which can serve at most min{N,M} connections concurrently, without having dedicated channels between each input and output. The crossbar consists of shared switching elements that forward the traffic through the network, connected by shared links, as can be seen in Fig. 1a. However, as we have alluded to, this kind of topology is faced with a scalability problem. For an  $N\times M$  crossbar, a total of  $N\times M$  switching elements need to be deployed along  $N + M$  links.

Traffic routing essentially determines how network resources (links and switches) are assigned for message transmissions. Traffic routing through a crossbar network is fairly straightforward. As we can see in Fig. 1b, to send a message from an input, the traffic needs to flow along the row of the input until the row intersects with the column of the output. There, the corresponding switch will route the traffic along the column, until it reaches the output node. This scheme ensures non-blocking communication, regardless of the chosen permutation of inputs and outputs.

Besides scalability in terms of implementation cost, large-scale systems which want to leverage crossbar switches face issues regarding signal integrity due to longer links, and multiple switches placed on the same link. These factors can also create crosstalk or longer propagation delays, potentially affecting the performance and reliability of the interconnection network. A way to mitigate these problems is to use smaller crossbar networks as building blocks for larger, multistage interconnection networks. In multistage interconnection networks traffic needs to pass through multiple crossbar switches before reaching the destination node. Usually, all the crossbar switches used have the same size, and the size of the crossbars alongside the number of stages of the entire interconnection determine different properties of the network. Some examples of such multistage interconnection networks are the previously mentioned, Benes network topologies<sup>35</sup>, Clos networks<sup>37</sup>, and modern topologies such as the Scalable Crossbar Network<sup>38</sup>.

![](images/3baf65d2f089c8e970b044e2a73f14b755f970c218360591f5bf89e246d43822.jpg)  
(a)

![](images/452d1440ce22480bdf0e29300b58819755fcee9327b1034cac1f73582d96bf70.jpg)  
Figure 1. (a) represents a crossbar network topology, and its constituent elements. By convention, on the left side we have the inputs, and at the bottom the outputs. In (b) an example of how routing is performed between inputs and outputs within a crossbar. It should be noted that the number of inputs does not necessarily need to match the number of outputs.  
(b)

# Components of crossbar quantum networks

The realm of quantum computing introduces many complex and intriguing concepts. Envisioning a quantum analog of classical crossbar interconnection networks, we can reach a grid-like architecture of intermediary nodes, connected through links. As this is a quantum network, the aim of such an interconnection network is not to transfer classical information through packets, but rather to transfer quantum information through physical particles.

Quantum information is encoded in a Quantum Bit (qubit). Information that is meant to be transferred along long distances is typically encoded in photons, by means of their polarization, due to several reasons, first of which is the robustness against decoherence that photons exhibit. Inherently, the quantum states are very fragile, and are susceptible to decoherence due to environmental factors. Photons are less sensitive to these interactions compared to other carriers such as more massive particles. This means that they can be used for long distance communication, not only because they travel at the speed of light, but also because they do so with minimal loss of coherence while traveling through the medium. Modern telecommunication networks rely on fiber-optic networks, and polarization-encoded quantum states can be transmitted through these existing links, provided a dark fiber channel is allocated<sup>39</sup>. Lastly, polarization states of photons can be easily prepared, manipulated and measured using commercially available optical elements. This makes it relatively straightforward to perform quantum operations on polarization-encoded qubits.

The links, as stated before, can be optical fiber links, or they can be Free-Space Optical (FSO) - transmission of photons through open air or vacuum. It should be noted that each type of link comes with its own advantages and disadvantages. It should be noted that, regardless of the medium chosen, signal amplification is not possible due to the no-cloning theorem<sup>40</sup>. As such, we need to envision systems where the same photon which left one of the communicating parties is the same photon received by the other party.

Typically, optical fiber links exhibit lower decoherence for the same distance as an FSO link. Longest fiber link channel through which quantum information was transmitted has  $830\mathrm{km}$  between nodes<sup>41</sup>, while the record for a terrestrial FSO link currently is of up to tens of kilometers<sup>25</sup>. This is due to the fact that the atmosphere exhibits fluctuations of its refractive index, which leads to light scattering, diffraction or beam wandering. These effects disturb the quantum state, leading to decoherence. Furthermore, FSO communication is affected by background light (sunlight or artificial sources), as these introduce noise in the quantum state. While error correction procedures have been developed for quantum communications, typically these require a minimal state of coherence to work. While optical fiber exhibits effects such as birefringeance or non-linear effects, these are generally more predictable and have a lesser effect compared to the challenges of FSO transmissions.

An advantage of FSO is that transmissions can be made between a stationary and a moving target, for example, a satellite. Satellite-based quantum communication has achieved significant milestones, with qubits being transmitted between Beijing and Vienna. This is possible do to the fact that the drawbacks associated to terrestrial FSO transmissions - scattering, diffraction or beam wandering, are mostly negated in transmissions above the atmosphere, as these were caused by interactions with air molecules. There has been a significant scientific focus in the area of satellite-based quantum networks as a result of this fact.

The intermediary nodes, should act as the switches of the classical crossbar network. These nodes should be able to perform basic qubit manipulation, as well as being able to generate or measure qubits. Advanced methods such as entanglement purification $^{42,43}$  may be employed within the nodes in order to maximize the fidelity of the entangled pair shared by the two communicating parties at the end. It is of note that entanglement purification typically requires a minimal fidelity in order to function, and works best with e-pairs that already have a high fidelity.

The functional capabilities of the switches (the intermediary nodes) align with the theoretical framework of quantum repeaters $^{44-48}$ , particularly in their ability to execute Bell State Measurements. This foundational operation is critical for quantum entanglement distribution networks, and is the minimum requirement of functionality of the intermediary nodes in the hereby presented scheme. Incorporating fully-fledged quantum repeaters with entanglement purification capabilities into the system architecture would theoretically enhance

the entanglement fidelity across all stages of quantum state distribution, therefore increasing the terminal entanglement fidelity between network nodes.

However, if we are to consider quantum repeaters which can somehow boost the fidelity of entangled photons passing through them (either through entanglement purification or other techniques), we need to consider two possibilities. In case all the links of the crossbar quantum network have an equal number of quantum repeaters along them, such a setup would be perfectly compatible with the proposed scheme. In case there is an unequal number of repeaters within the network, we need to take into account that the repeaters introduce a delay in the transmission. Therefore, a mechanism of storing entangled particles received early until the counterpart from the other link is received needs to be available. This could be achieved by using quantum memories $^{49,50}$ . We will discuss the use of quantum memories in more detail in Section "Challenges of concurrent entanglement distribution".

# Challenges of concurrent entanglement distribution

The possible functions of the Quantum Internet, as diverse as they may be, all have in common the need for entangled particles. These entangled particles are essentials to protocols such as quantum teleportation and quantum key distribution, as they effectively act as a medium of information transmission that is secured by physical laws.

The quantum teleportation protocol enables pairs of communicating parties to exchange quantum information without actually physically moving any quantum states during the course of the communication from one party to the other. This is done by leveraging the peculiar properties of entangled particles, particularly the fact that modifying the state of one of the particles in the entangled pair affects the other particle in a predictable manner, regardless of the space separation between the two particles. This is, however, not a superluminal transfer of information, as 2 bits of classical information need to be transmitted to the receiver, in order to retrieve the correct quantum state that the sender encoded, as it can be seen in the quantum circuit for teleportation, in Fig. 2. During the teleportation procedure, the entangled pair is consumed, (i.e. it is measured), and cannot be reused to perform another information transfer. This means that, for sustained quantum communication between parties by means of quantum teleportation, a way to reliably distribute entangled pairs needs to be in place.

# Existing entanglement distribution protocols

The entanglement distribution protocol detailed in the recent study by Yin et al. represents a significant leap in the pursuit of global quantum communication networks. The protocol proposed harnesses the advantages of satellite platforms to mitigate the signal loss inherent in terrestrial fiber networks, which has been a major bottleneck for long-distance quantum entanglement. By generating entangled photons on a satellite and distributing them to ground stations, the researchers have circumvented the limitations posed by Earth's atmosphere and curvature. The high-fidelity entanglement achieved across distances of up to  $2400\mathrm{km}$  is particularly notable, demonstrating that quantum correlations can be maintained over scales far exceeding traditional fiber-based systems. The approach benefited from cutting-edge technologies, including narrow-beam divergence to reduce photon dispersion and dynamic polarization compensation to counteract the alterations caused by the satellite's motion and atmospheric interference.

In a recent analysis by Viscardi et al. [52] a sophisticated framework for optimizing the distribution of quantum entanglement, a foundational process in the emerging Quantum Internet, is presented. The entanglement distribution challenge is approached by formulating it as a Markov Decision Process, which enables the modeling of decision-making in quantum network nodes, for effective entanglement distribution. The model distinguishes between fixed parameters that depend on the underlying quantum network technology, such as the time horizon for distribution and the probability of successful entangled pair transmission, and design parameters that can be manipulated to achieve desired outcomes, primarily through the reward function. This reward function is pivotal in guiding the decision-making process, ensuring larger distributed cluster sizes and shorter distribution times.

![](images/05e53ec75a292d714f4ba17a26e42ac05061622482062823f751ded54a11964b.jpg)  
Figure 2. Quantum teleportation circuit. Alice begins with a qubit in the  $|\psi >$  state. After acquiring an entangled pair, shared between Alice and Bob, and Alice performing a partial measurement, using 2 classical bits of information, Bob can retrieve the exact state that Alice began with,  $|\psi >$

The Markov Decision Process-based model is concluded to be a valuable tool for quantum network designers, providing a method to adjust and control the entanglement distribution process to meet specific performance benchmarks. This work not only aids in the practical engineering of quantum networks but also contributes to the foundational infrastructure necessary for realizing the Quantum Internet, with implications for secure communications and distributed quantum computing.

Another recent work focused on optimal entanglement distribution over star-shaped topologies<sup>53</sup>. In this work, two primary distribution methodologies have been introduced: symmetrical and asymmetrical approaches. These relate to the way intermediary nodes are allocated for intersecting routes. In order to perform the entanglement distribution within a single transfer cycle, each route can either do it's measurements on odd-numbered nodes, and entangled pair generation on even-numbered, or vice versa. This choice influences the success probability of establishing entanglement between the two terminal nodes.

The findings of this study suggest that the choice of entanglement distribution strategy should be adaptive, depending upon the network's transmission success probabilities, and the complexity of its topology. For example, networks with less reliable transmissions should use the symmetrical approach, where intersecting routes contend over the same intersecting node, is preferable. Alternatively, networks with highly reliable quantum operations should use an asymmetrical approach, which provides simultaneous resolution to multiple entanglement requests, but execute more measurements.

# Simple entanglement distribution between two nodes

In order to describe how we can distribute entanglement through a crossbar quantum network, we first need to define the purpose of the inner nodes of the crossbar. As stated before, these should be able to perform basic qubit manipulation. Namely, they should be able to perform Bell State Measurements (BSM), and be able to generate new entangled pairs.

The purpose of being able to perform Bell State Measurements is to be able to execute the entanglement swapping procedure $^{54,55}$ . Through entanglement swapping, we can effectively make two separate parties share an entangled pair without actually having to physically transport an entangled particle all the way from one party to the other. In the following, we shall consider a chain topology, with each party at the ends of the chain. An ideal application of entanglement swapping would be if two parties supply an entangled particle to a node that is situated at half the distance between the two of them. The node would then perform a BSM on the two particles thus shifting the entanglement to the two particles with whom they were each previously entangled to.

The advantage of such a distribution scheme relies in preserving entanglement fidelity. As the quantum state coherence is affected by environmental factors, so too is the entanglement fidelity of entangled particle pairs. Therefore, by exposing the state a shorter time to external factors, we preserve more of the initial entanglement fidelity. In the example application for entanglement swapping, we are effectively halving the distance the particles need to travel, and fidelity loss scales exponentially with the distance traveled. Thus, we not only end up with a higher fidelity entangled pair in the end, but we are doing so two times faster than by transporting the particle between the two parties (for which we will use a common naming convention - Alice and Bob).

An alternative solution to efficiently transmit an entangled pair to Alice and Bob would be to have a node midway between them. This midway node would generate an entangled pair, and transmit one particle to Alice, and one to Bob. Since the act of measurement itself is imperfect, and can fail, it is natural that we want to minimize such operations in our process to distribute entanglement. Compared to the previous distribution scheme, this one does not involve any measurements, only the entangled pair generation and two transmissions, each with half the distance between Alice and Bob. Therefore, this distribution scheme where we are not performing an entanglement swap is preferable.

It is noteworthy that in these solutions, and in the algorithm proposed in the following sections, we do not consider the usage of a quantum memory. The hereby proposed scheme is a solution where entanglement is generated and transmitted in the least amount of time possible, such that quantum state coherency is exposed to as few environmental factors as possible. Typically, classical crossbar networks are employed in small scales, where the transmission time between nodes is negligible. If, however, we wish to employ a crossbar quantum network over large distances, we would need to account for this transmission time, as well as clock drifts between nodes, and therefore use quantum memories to store entangled particles for the Bell State Measurements.

Regarding the capabilities of the quantum memories used, the coherence time of these quantum memories should be expected to be minimally equivalent to the duration needed for a photon to traverse the network's longest link. If we were to consider longer coherence times for the quantum memories, such that entanglement could be preserved between the operation cycles of the crossbar, there may be more optimal solutions for the distribution of the entanglement. Furthermore, if the capacity of the quantum memories allows for more than one qubit to be stored, this may allow more sophisticated distribution schemes. We consider these scenarios to be open problems in the realm of entanglement distribution. Regarding the fidelity of the quantum memories, ideally these should be as high as possible. However, we acknowledge that quantum state coherence degradation might occur over time in quantum memories, and a trade-off might occur when choosing to serve a stored entangled qubit instead of generating a new one. This aspect should be taken into account in any further scenario that leverages quantum memories.

# Optimal entanglement distribution in crossbar quantum networks

The previously mentioned scenarios only involve three nodes: Alice, Bob, and a midway node which either performs a BSM, or generates entanglement. Transmissions of entanglement are limited by the distance that the photon can travel, as we have stated before. Thus, if Alice and Bob are at a long distance, multiple nodes might need to be placed between them in order to facilitate transmission of quantum information. In this situation,

we need to adapt the aforementioned methods to the situation where there are multiple intermediary nodes between Alice and Bob.

# Efficient entanglement distribution along a chain topology

For both distribution schemes, the simplest way to adapt to multiple intermediary nodes would be to just use the additional nodes as proxies, and still use the midway node as a BSM machine, or as the generator of entanglement. However, these approaches don't solve the problem of distance, as at least one particle would still have to travel more than half the distance between Alice and Bob. A solution would be to alternate between the two aforementioned distribution methods in such a way that no photon would need to pass through more than one link. In Fig. 3, we can observe the ways we can alternate these schemes to form what we will refer to even and odd distribution schemes. An even distribution scheme is one where even-numbered nodes (counting from Alice) generate entanglement, which they transmit bidirectionally towards their adjacent nodes (which are odd-numbered). The odd-numbered nodes then perform Bell State Measurements of these entangled particles. In Fig. 3c and d we can observe such distributions of entanglement where nodes numbered 3 and 5 perform the BSMs. Alternatively, in the odd distribution scheme, as in Fig. 3a and b, odd-numbered nodes generate entanglement, and even-numbered nodes perform the entanglement swapping procedure (nodes 2, 4 and 6 in Fig. 3a, and nodes 2 and 4 in Fig. 3b).

The benefits of such an alternating distribution scheme are manifold. For once, the particles have to travel at most the distance of the longest link in the chain. This would lead to a lower fidelity loss of the entanglement. Another result of this fact is that the entire operation would take as much time as it takes for a photon to travel the distance of the longest link, plus the time it takes to perform the BSM. This would also positively affect the final fidelity of the entangled pair shared by Alice and Bob. Furthermore, we are fully utilizing the qubit-manipulation capacity of the network.

It should be apparent that the choice between an odd and even distribution is a binary one. As we are alternating nodes that perform Bell State Measurements with nodes that generate entanglement, the choice is in fact the operation that the first node will perform: a BSM or e-pair generation. Even though the difference between odd and even distribution is simple, they are not equivalent. As we can observe in Fig. 3b and d, in the cases where the number of intermediary nodes is even, there is indeed no difference in the number of BSM performed in total. However, for an odd number of intermediary nodes, it is preferable to perform an odd distribution, as it would imply one less BSM than the even distribution. This would increase the success rate of the distribution. In the following section, we will explore how these concepts can be applied for a crossbar quantum network, and how to find the optimal distribution scheme for any particular input-output configuration of the crossbar.

The principles of even and odd distributions can be extended and applied within the context of a crossbar architecture as well. For the sake of simplicity of operations, we will consider an  $N \times N$ -sized crossbar, without loss of generality. First, we need to define an operational cycle of the crossbar quantum network. Similar to a classical crossbar, a cycle is represented by the basic unit of time during which information transfer operations are executed. Within each cycle, we can define a tuple of input-output pairs, that describe the way quantum information flows through the crossbar during that cycle.

We will use the following numbering convention for input and output nodes of a crossbar. The input nodes (on the left side of the figures) are numbered starting from 1, top to bottom. The output nodes (at the bottom of the figures), are numbered starting from one, right to left. This convention is important as it will allow us to easily determine the routes which intersect based on the input and output indices. In order to better understand the tuple of input-output pairs, take for example the crossbar in Fig. 4a, for which we would have the following tuple that describes the flow: [(1, 1), (2, 2), (3, 4), (4, 3)]. We may take each input-output pair, and assign a boolean value to it - whether it performs an odd distribution (true), or an even distribution (false). It should be emphasized that the selected assignment convention was adopted arbitrarily and does not carry any inherent significance. An alternative convention could have been equally valid.

![](images/ba095865c870514fb02060ac4ced7b7f526e52427c58c44c1e7415d82f8b3dbe.jpg)  
(a)

![](images/368563fa08bdc7c643d02c5ecfb4670d2f906d65a303a8e97457c793b5b4d1bb.jpg)

![](images/cd076331eaadff6d25a485ef398bfaa512378a3204f4e554e03110f6e37e8dd8.jpg)  
(c)

![](images/e4aff737d5f7364b096e8d088c4ad6c216bf0b10cd6f55f35e3d8ff12defdf6c.jpg)  
Figure 3. Four efficient entanglement distribution possibilities along a chain topology. In (a), there is an odd number of nodes, and we use an odd distribution scheme: nodes 3 and 5 perform the BSMs. Alternatively, in (b), the process of odd distribution is depicted along an even number of nodes, with nodes 3 and 5 performing the BSMs as well. In (c), the less efficient even distribution is used along an odd number of nodes, where nodes 2, 4, and 6 perform the BSMs, and in (d), the even distribution is used along an even number of nodes, with only nodes 2 and 4 performing the BSMs.  
(b)  
(d)

![](images/1605e9170215b14931837dead8a5a9dc46ff57de89c328563fa70870132e6763.jpg)  
(a)

![](images/3f3e67b2ed480820469c688ee64239166083ed5b5a923504fcb2ccc285d45f20.jpg)  
Figure 4. (a) is an example entanglement distribution on a  $4 \times 4$  crossbar where we use the following boolean values to describe the distributions: [false, false, true, true]. In (b), there is an example of a distribution where the used distribution scheme does not work. Since the  $(3,4)$  route uses an odd distribution, and the  $(4,3)$  route uses an even distribution, they would end up using the same node to perform the Bell State Measurement. This would not lead to the desired entanglement distribution.  
(b)

As we can see in Fig. 4b, the choice of whether or not to perform an odd distribution—which would be preferable due to the lower number of BSMs that it would imply, is not trivial. If we assign an odd distribution for every pair, we end up in a state where a single node would need to simultaneously perform a BSM for two separate incoming pairs of particles. This would not lead to the desired effect, as it would not swap the entanglement in the way that was intended. Therefore, we need to find a way to assign the routes an even or odd distribution, in a way such that a node only performs a BSM for one pair at a time.

# Optimal routing scheme for entanglement distribution in crossbar networks

As there are only two possibilities for each input-output pair, it might seem feasible to try out all the possible combinations for fairly small crossbar sizes. Such an approach would be faced a problem - how to determine if a combination is correct. In order to solve this, we need a way to determine whether or not two input-output pairs intersect, and, more importantly, what combinations does their intersection allow.

In order to determine whether or not two input-output pairs intersect, we need only to consider the tuple that describes the flow. For every input-output pair, we will consider all other pairs that have the input index larger than the current one. By looking only at the routes that have their input index higher, we are essentially looking at routes that start from a lower position in the crossbar. Two routes can intersect if the route that starts lower has its' destination further right than the one that starts higher. Effectively, this means that if there are any pairs that have their input index higher than the one we are currently assessing, and have their destination index lower, these two routes intersect, per this numbering convention. In order to efficiently determine which routes intersect, we may sort the tuple by their input index. Afterwards, we start traversing the tuple, and for each pair, we will look at all the next pairs and perform this check. This intersection check would still have an algorithmic complexity of  $\mathcal{O}(n^2)$ , larger than the complexity for sorting the tuple. Note that we only performing the lookup for larger indices, as it is sufficient to detect the intersection once. By looking at all indices, we would detect intersections two times: once from the route that starts above, and once for the route that starts below.

Determining whether or not two routes intersect is not enough however, to be able to check if a boolean combination would satisfy the conditions we imposed earlier. We also need to check what kind of route assignations are possible for the two intersecting routes. In order to determine this, we would need to determine for each route the respective parity of the intersection node. Let us consider two input-output pairs  $(i,j)$  and  $(k,y)$ , with  $i < k$  and  $j > y$ . Based on what we have established, these two routes intersect, and the first route has its input node above the other, as it can be observed in Fig. 5a. The intersection node parity for the  $(i,j)$  route can be calculated using the following formula:  $(n - j + 1 + k - i) \bmod 2$ . There are two parts of this formula. The  $n - j + 1$  is the number of nodes along the horizontal axis, followed by  $k - i$ , which is the number of nodes along the vertical axis. The parity for the  $(k,y)$  route has a simpler formula:  $(n - j + 1) \bmod 2$ , which is just the number of nodes along the horizontal axis.

Based on the parities for the intersection node, we can impose some constraints upon the boolean values assigned for each route. In order to formally define these constraints, we will consider the following convention: the boolean variable  $i$  will be uniquely assigned to route  $(i,j)$ , and will determine whether it will use an even or odd distribution, as previously stated. There are 4 possibilities regarding the parities for the intersection node. If for both routes the node is even, this means that they cannot both use an odd distribution at the same time. This constraint translates to  $(i \lor k)$ . If for route  $(i,j)$  the node is even, and for  $(k,y)$  odd, the first route cannot be odd while the second is even. This constraint can be written as  $(\neg i \lor k)$ . The reverse is true, if for the first route the node is odd, and for the second even, the constraint is  $(i \lor \neg k)$ . If for both routes the node is odd, both cannot use an even distribution, meaning that the constraint is  $(\neg i \lor \neg k)$ . These constraints need to be satisfied for all routes simultaneously - conjoined with an  $\wedge$ . Thus, we have a formula in the conjunctive normal form (CNF).

![](images/b6054f896647f0ed0ca69ae87f3832fc3478d92eaf6dc7d94058a7879047ff6d.jpg)  
Figure 5. In (a) it can be observed that the number of nodes, along both routes, in a horizontal path, is equal to the total number of nodes, minus the destination of the uppermost route. We need to count one extra node, due to the fact that we consider the input node as part of the topology as well. In (b), along a vertical path, the uppermost route has to travel the difference between both input nodes. The node where the path switches should not be counted twice, that is why we subtract 1 from that part of the equation.

![](images/d288bf3d432b3485adcfe4a855dc52d2366e0da8c7925b06d6b0ed3b25c615ae.jpg)

Having an array of booleans and a CNF formula means that this problem falls in the category of 2-satisfiability (2SAT) problems<sup>56</sup>. However, it is not enough to know if an input-output pair tuple is satisfiable, we also need to know the boolean configuration which satisfies the constraints we have imposed. Furthermore, we want optimality in terms of the lowest numbers of Bell State Measurements performed. Thus, we want as many odd distributions as possible. This means that we want a boolean configuration which satisfies the constraints, and has the largest amount of true values.

In canonical form, the problem which we want to solve can be expressed as follows

$$
\text {L e t} \mathbf {d} = \left[ d _ {1}, d _ {2}, \dots , d _ {n} \right] \text {b e a b o o l e n v e c t o r w h e r e} d _ {i} \in \{0, 1 \} \text {f o r a l l} i = 1, 2, \dots , n
$$

$$
f i n d \mathbf {d} \text {t h a t m a x i m i z e s} \mathbf {d} ^ {\top} \mathbf {d}
$$

$$
\text {s u b j e c t} (i \vee k) \text {i f i n t e r s e c t i o n 1 i s e v e n f o r b o t h o r}
$$

$$
(\neg i \vee k) \text {i f i n t e r s e c t i o n 1 i s o d d - e v e n o r}
$$

$$
(i \vee \neg k) \text {i f i n t e r s e c t i o n 1 i f e v e n - o d d o r}
$$

$$
\begin{array}{l} (\neg i \vee \neg k) \text {i f t h e i n t e r s e c t i o n 1 i s o d d f o r b o t h} \\ a n d \end{array} \tag {1}
$$

$$
(i \vee k) \text {i f} 2 \text {i s e v e n f o r b o t h o r}
$$

$$
(\neg i \vee k) \text {i f i n t e r s e c t i o n 2 i s o d d - e v e n o r}
$$

$$
(i \vee \neg k) \text {i f t h e i n t e r s e c t i o n 2 i f e v e n - o d d o r}
$$

$$
\begin{array}{l} (\neg i \lor \neg k) \text {i f i n t e r s e c t i o n 2 i s o d d f o r b o t h} \\ a n d \dots \end{array}
$$

where all conditions are imposed by the way the routes intersect, as described before.

It is noteworthy that the trivial situation where we just want a configuration which satisfies the constraints is easily solvable in linear time by using a directed graph representation of the constraints, the situation where we want to maximize the number of true values is known in literature as a MAX-SAT problem, and its variants, like MAX-2SAT, are NP-hard. Algorithms based on branch-and-bound methods are known to solve MAX-2SAT problems, however, for large problem sizes, the solution may not be exact[57].

# Simulation results and scalability analysis

In Algorithm 1 we present the constraint-building process for finding a boolean configuration which allows concurrency-free entanglement transmission in the crossbar quantum network, by solving the optimization problem described in Eq. 1. We consider a solver object which provides an API for adding constraints, and for solving the problem. The optimality of the solution, in terms of the number of true values, is depending on the solver used, and not on the constraints imposed. As such, the hereby presented algorithm is generally applicable.

```txt
Input :in/out tuple, n  
1 begin  
2 sort in/out tuple by the input of each route  
3 conditions  $\leftarrow []$   
4 for each input in in/out tuple do  
5 for each other pair with input greater than the current one do  
6 if output of the other route is smaller than the current one then  
7 parity1  $\leftarrow (n - output_1 + 1 + input_2 - input_1)$  mod 2  
8 parity2  $\leftarrow (n - output_1 + 1)$  mod 2  
9 if parity1 = 0 and parity2 == 0 then  
10 append  $(\neg i \lor \neg v)$  to conditions  
11 end  
12 else if parity1 = 0 and parity2 = 1 then  
13 append  $(\neg i \lor v)$  to conditions  
14 end  
15 else if parity1 = 1 and parity2 = 0 then  
16 append  $(i \lor \neg v)$  to conditions  
17 end  
18 else if parity1 = 1 and parity2 = 1 then  
19 append  $(i \lor v)$  to conditions  
20 end  
21 end  
22 end  
23 end  
24 configuration  $\leftarrow$  Solve MAX-2SAT for conditions and n boolean variables, maximizing true values  
25 end
```

# Algorithm 1. Optimal distribution configuration over the crossbar

Using the previously presented algorithm, we have simulated all the possible input-output configurations for crossbars up to an  $10 \times 10$  size (the simulations were performed on a machine equipped with an AMD Threadripper 5975WX, 32 cores and with 256GB RAM). Since the number of possible, distinct configurations is  $N! - 1$ , where N is the size of the crossbar, simulating crossbars of larger size would have been an increasingly difficult task.

In the simulation results, there are input-output configurations which are not satisfiable, such as the one in Fig. 6. This means that there is no way to distribute entanglement without having one or more nodes having to perform simultaneous BSMs on more than a pair. Such configurations all follow the same base pattern, which was first found for the  $4 \times 4$  crossbar. We can observe in Fig. 6, how there is no configuration possible where we can avoid having to measure multiple pairs in the same node.

Furthermore, it can be observed in Fig. 7 that the incidence of unsatisfiable configurations greatly increases. Even going from a crossbar of size  $4 \times 4$  to  $7 \times 7$ , the rate of unsatisfiable configurations increases tenfold, going from approx. 0.043 to approx. 0.45. Thus, it can be safely concluded that the usability of non-blocking

![](images/066b618b7df2ccf0577ccd43e37236697e7116eaa9b94d4ce21bc1419b9aca48.jpg)  
(a)

![](images/091ce790db9d64ee3132beb6e98845c7cc1331817f11dedf2c03adea1ecef5a6.jpg)  
(b)

![](images/c0a44d3eadb04a2c4c0ef36fd1b604151418bd0105fb39d4f265f8e127f14fbe.jpg)  
Figure 6. With an input-output configuration of [(1, 4), (2, 3), (3, 2), (4, 1)], it is impossible to find a configuration that wouldn't result in a double measurement in at least one node. In (a), we can observe how, if routes 2 through 4 use an even distribution, the path for route 1 would have 3 consecutive nodes where BSMs are performed by the other routes. In (b), route 4 has 2 consecutive nodes which are used for BSM by routes 2 and 3. In (c), route 3 has two consecutive nodes used, by routes 1 and 2.  
(c)

![](images/4673b632f5cca78483b5bcb522a237aca66584c79b1ddeaf95f649f4c47de552.jpg)  
Figure 7. The rate of unsatisfiable configurations in relation to the size of the crossbar. For crossbars smaller than  $4 \times 4$ , all configurations are satisfiable. The  $4 \times 4$  crossbar has a single unsatisfiable configuration out of the 23 total possible. The rate of unsatisfiability greatly increases afterwards, reaching almost  $50\%$  for a  $7 \times 7$  crossbar.

entanglement distribution algorithms that make use of alternating entanglement swapping patterns are not feasible for crossbars of larger size.

# Overcoming crossbar size limitations

The consequence of this finding is that, even though a crossbar quantum interconnection constructed in the manner described would indeed transfer entanglement within the minimal and deterministic latency, and offer non-blocking communication, it cannot fulfill the basic purpose of the classical crossbar interconnection, that is to offer a channel from every input to every output. If the aim is, however, to provide non-blocking communication with low, but not minimal latency, a multi-stage network, using crossbars up to size  $3 \times 3$  would be feasible, as there are no configurations where those have concurrency over an intersection node.

For example, we could distribute entanglement to any number of quantum nodes, in a non-blocking manner, by using crossbars quantum networks of size  $2 \times 2$ , through a Beneš network. Such a setup would require  $N * \log_2 N - N/2$  intermediary crossbars, totalling  $4N * \log_2 N - 2N$  intermediary nodes. Alternatively, if we were to use a similar scheme, but use crossbars of size  $3 \times 3$ , we would require  $\frac{2}{3} * N \log_3 N - \frac{N}{3}$  crossbars. Since every such crossbar would have 9 intermediary nodes, this leads to a total of  $6N * \log_3 N - 3N$ . We can observe how each of these two solutions compares to a full crossbar between all  $N \times N$  nodes in Fig. 8.

Alternatively, as the Beneš network is a special case of the Clos network, where the crossbars have a  $2 \times 2$  size, we may use crossbars of size  $2 \times 3$ ,  $3 \times 2$ , or  $3 \times 3$ , to construct a non-blocking multi-stage interconnection network, to distribute entanglement.

# Conclusions and future outlook

This paper introduces an approach that addresses a problem not been previously investigated, efficiently distributing entanglement through a crossbar quantum interconnection network. Efficient distribution of entangled particles plays a pivotal role in enhancing quantum communication, where entanglement is a building block for secure data transfer, either through QKD or teleportation. Moreover, in quantum computing, efficient distribution of entanglement is essential for scaling up systems and maintaining coherence across qubits, thereby improving computational capabilities.

We have proposed two different distribution strategies for any route within the crossbar: even distribution and odd distribution. These distribution strategies ensure minimal latency for the entanglement distribution operation, though the odd distribution has a greater success rate, due to one less Bell State Measurement being performed. Choosing the optimal configuration for an operation cycle of the crossbar, is therefore a problem of optimizing the number of odd distributions performed, while satisfying the constraints being placed between individual routes. Namely, intermediary nodes may perform only one BSM at a time. It should be noted that this way of distributing entanglement is not the only one possible, as we are imposing a harsh condition upon the qubits that we are transmitting - they do not remain coherent for more than a crossbar cycle. We are imposing this without losing generality, as operating with coherence times lower than this would be impossible, as they would not even survive the transmission within the links of the crossbar. Thus, protocols where the qubits can be stored within the nodes for multiple cycles can be an interesting research direction.

We have analyzed the capabilities of the distribution strategies over the crossbar quantum network, computing the optimal distribution strategies for all possible scenarios for crossbars up to size  $10 \times 10$ . We have found that there are input-output configurations where it is not possible to distribute entanglement in a non-blocking fashion using the proposed distribution strategies, if the crossbar has a size greater than  $3 \times 3$ . We have concluded

![](images/bdb1ec9f8f48fd0a10264af0836a69f27a5cf8a60aa13231660bd44d500300ce.jpg)  
(a)  
Figure 8. Logarithmic plot of the number of intermediary nodes placed within  $2 \times 2$ -sized crossbars within a Beneš network. It can be observed that for relatively low number of inputs/outputs (approx. 20), a full crossbar would have required less intermediary nodes. However, this would have come at the cost of the impossibility of performing efficient entanglement distribution for certain input-output configurations.

![](images/fa6e3929553474b36fb874365a6f8368d866b9dab21ded9b6503311634e3a303.jpg)  
(b)

that it is possible, albeit not with minimal latency, to construct a non-blocking, scalable, multistage network using crossbars of smaller sizes, which do not exhibit these problems.

As future work, we propose an analysis of optimality in terms of expected time of completion of the entanglement distribution process. Another proposed research direction is entanglement distribution in blocking interconnection networks. Another proposed analysis involves determining the best distribution strategy for qubits that can be stored at intermediary nodes for an unspecified duration in a quantum memory.

# Data availability

The datasets generated during the current study and the complete mathematical calculus will be made available from the corresponding author on reasonable request.

Received: 12 December 2023; Accepted: 15 May 2024

Published online: 22 May 2024

# References

1. Einstein, A., Podolsky, B. & Rosen, N. Can quantum-mechanical description of physical reality be considered complete?. Phys. Rev. 47, 777 (1935).  
2. Yin, J. et al. Bounding the speed of spooky action at a distance. arXiv:1303.0614 (2013).  
3. Horodecki, R., Horodecki, P., Horodecki, M. & Horodecki, K. Quantum entanglement. Rev. Mod. Phys. 81, 865 (2009).  
4. Gisin, N. & Thew, R. Quantum communication. Nat. Photonics 1, 165-171 (2007).  
5. Cacciapuoti, A. S. et al. Quantum internet: Networking challenges in distributed quantum computing. IEEE Netw. 34, 137-143 (2019).  
6. Gyongyosi, L. & Imre, S. A survey on quantum computing technology. Comput. Sci. Rev. 31, 51-71 (2019).  
7. Gill, S. S. et al. Quantum computing: A taxonomy, systematic review and future directions. Softw. Pract. Exp. 52, 66-114 (2022).  
8. Tanasescu, A., Constantinescu, D. & Popescu, P. G. Distribution of controlled unitary quantum gates towards factoring large numbers on today's small-register devices. Sci. Rep. 12, 21310 (2022).  
9. Shor, P. W. & Preskill, J. Simple proof of security of the BB84 quantum key distribution protocol. Phys. Rev. Lett. 85, 441 (2000).  
10. Scarani, V. et al. The security of practical quantum key distribution. Rev. Mod. Phys. 81, 1301 (2009).  
11. Bennett, C. H. et al. Teleporting an unknown quantum state via dual classical and Einstein-Podolsky-Rosen channels. Phys. Rev. Lett. 70, 1895 (1993).  
12. Georgescu, I. 25 years of experimental quantum teleportation. Nat. Rev. Phys. 4, 695-695 (2022).  
13. Parakh, A. Quantum teleportation with one classical bit. Sci. Rep. 12, 3392 (2022).  
14. Ding, Y., Wei, Y., Li, Z. & Jiang, M. Quantum teleportation based on non-maximally entangled graph states. Quantum Inf. Process. 22, 400 (2023).  
15. Nielsen, M. A. The entanglement fidelity and quantum error correction. arXiv:quant-ph/9606012 (1996).  
16. Yao, W., Liu, R.-B. & Sham, L. Theory of control of the spin-photon interface for quantum networks. Phys. Rev. Lett. 95, 030504 (2005).  
17. Brito, S., Canabarro, A., Cavalcanti, D. & Chaves, R. Satellite-based photonic quantum networks are small-world. *Prx Quantum* 2, 010304 (2021).  
18. Lami, L. & Regula, B. No second law of entanglement manipulation after all. Nat. Phys. 19, 184-189 (2023).  
19. Niemietz, D., Farrera, P., Langenfeld, S. & Rempe, G. Nondestructive detection of photonic qubits. Nature 591, 570-574 (2021).  
20. Dai, W., Peng, T. & Win, M. Z. Optimal remote entanglement distribution. IEEE J. Sel. Areas Commun. 38, 540-556 (2020).  
21. Ecker, S. et al. Overcoming noise in entanglement distribution. Phys. Rev. X 9, 041042 (2019).

22. Ciobanu, B.-C., Iancu, V. & Popescu, P. G. Entanglenetsat: A satellite-based entanglement resupply network. IEEE Access 10, 69963-69971 (2022).  
23. Lu, Q.-H. et al. Quantum key distribution over a channel with scattering. Phys. Rev. Appl. 17, 034045 (2022).  
24. Bowen, W. P., Schnabel, R., Lam, P. K. & Ralph, T. C. Experimental investigation of criteria for continuous variable entanglement. Phys. Rev. Lett. 90, 043601 (2003).  
25. Liao, S.-K. et al. Long-distance free-space quantum key distribution in daylight towards inter-satellite communication. Nat. Photonics 11, 509-513 (2017).  
26. Kimble, H. J. The quantum internet. Nature 453, 1023-1030 (2008).  
27. Gyongyosi, L. & Imre, S. Advances in the quantum internet. Commun. ACM 65, 52-63 (2022).  
28. Gyongyosi, L. Dynamics of entangled networks of the quantum internet. Sci. Rep. 10, 12909 (2020).  
29. Gyongyosi, L. & Imre, S. Routing space exploration for scalable routing in the quantum internet. Sci. Rep. 10, 11874 (2020).  
30. Duato, J., Yalamanchili, S. & Ni, L. Interconnection Networks (Morgan Kaufmann, Burlington, 2003).  
31. Xu, J. Topological Structure and Analysis of Interconnection Networks Vol. 7 (Springer Science & Business Media, Berlin, 2013).  
32. Awschalom, D. et al. Development of quantum interconnects (quics) for next-generation information technologies. *Prx Quantum* 2, 017002 (2021).  
33. Zhuge, H. Future interconnection environment. Computer 38, 27-33 (2005).  
34. Kachris, C., Kanonakis, K. & Tomkos, I. Optical interconnection networks in data centers: Recent trends and future challenges. IEEE Commun. Mag. 51, 39-45 (2013).  
35. Beneš, V. E. Mathematical Theory of Connecting Networks and Telephone Traffic (Academic Press, Cambridge, 1965).  
36. Lo, H.-K. & Chau, H. F. Unconditional security of quantum key distribution over arbitrarily long distances. Science 283, 2050-2056 (1999).  
37. Clos, C. A study of non-blocking switching networks. Bell Syst. Tech. J. 32, 406-424 (1953).  
38. Bistouni, F. & Jahanshahi, M. Scalable crossbar network: A non-blocking interconnection network for large-scale systems. J. Supercomput. 71, 697-728 (2015).  
39. Xavier, G., de Faria, G. V., Temporão, G. & Von der Weid, J. Full polarization control for fiber optical quantum communication systems using polarization encoding. Opt. Express 16, 1867-1873 (2008).  
40. Wootters, W. K. & Zurek, W. H. A single quantum cannot be cloned. Nature 299, 802-803 (1982).  
41. Wang, S. et al. Twin-field quantum key distribution over 830-km fibre. Nat. Photonics 16, 154-161 (2022).  
42. Linden, N., Massar, S. & Popescu, S. Purifying noisy entanglement requires collective measurements. Phys. Rev. Lett. 81, 3279 (1998).  
43. Bose, S., Vedral, V. & Knight, P. Purification via entanglement swapping and conserved entanglement. Phys. Rev. A 60, 194 (1999).  
44. Van Meter, R. Quantum Networking (Wiley, Hoboken, 2014).  
45. Pirandola, S. Capacities of repeater-assisted quantum communications. arXiv:1601.00966 (2016).  
46. Van Meter, R., Satoh, T., Ladd, T. D., Munro, W. J. & Nemoto, K. Path selection for quantum repeater networks. Netw. Sci. 3, 82-95 (2013).  
47. Dur, W., Briegel, H.-J., Cirac, J. I. & Zoller, P. Quantum repeaters based on entanglement purification. Phys. Rev. A 59, 169 (1999).  
48. Gyongyosi, L. & Imre, S. Efficient quantum repeaters without entanglement purification. In International Conference on Quantum Information QMI14 (Optica Publishing Group, 2011).  
49. Zhang, W. et al. Quantum secure direct communication with quantum memory. Phys. Rev. Lett. 118, 220501 (2017).  
50. Gyongyosi, L. & Imre, S. Optimizing high-efficiency quantum memory with quantum machine learning for near-term quantum devices. Sci. Rep. 10, 135 (2020).  
51. Yin, J. et al. Satellite-based entanglement distribution over 1200 kilometers. Science 356, 1140-1144 (2017).  
52. Viscardi, M., Illiano, J., Cacciapuoti, A. S. & Caleffi, M. Entanglement distribution in the quantum internet: An optimal decision problem formulation. IEEE QCE23 (2023).  
53. Perju Verzotti, L., Ciobanu, B.-C. & Popescu, P. G. Optimal quantum network decongestion strategies. Sci. Rep. 13, 9834 (2023).  
54. Zukowski, M., Zeilinger, A., Horne, M. A. & Ekert, A. K. "Event-ready-detectors" bell experiment via entanglement swapping. Phys. Rev. Lett. 71 (1993).  
55. Pan, J.-W., Bouwmeester, D., Weinfurter, H. & Zeilinger, A. Experimental entanglement swapping: Entangling photons that never interacted. Phys. Rev. Lett. 80, 3891 (1998).  
56. Krom, M. R. The decision problem for a class of first-order formulas in which all disjunctions are binary. Math. Log. Q. 13, 15-20 (1967).  
57. Asano, T. & Williamson, D. P. Improved approximation algorithms for max sat. J. Algorithms 42, 173-202 (2002).

# Acknowledgements

This work is dedicated to Prof. Nicolae Tapus, on his 75th birthday. This work has been partially supported by RoNaQCI, part of EuroQCI, DIGITAL-2021-QCI-01-DEPLOY-NATIONAL, 101091562.

# Author contributions

Conceptualization: B.C.C. and P.G.P.; methodology: B.C.C. and P.G.P.; validation, B.C.C. and L.P.V.; writing—original draft preparation: B.C.C., L.P.V. and P.G.P.; writing—review and editing: B.C.C., L.P.V. and P.G.P.; supervision: P.G.P.; All authors have read and agreed to the published version of the manuscript.

# Competing interests

The authors declare no competing interests.

# Additional information

Correspondence and requests for materials should be addressed to P.G.P.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/4a4e2a1bf9b74e292a334d3311c79afe6d25432f37ffddcfeabee9cc8f7a16b7.jpg)

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or

format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2024