# Using Gaussian Boson Sampling to Find Dense Subgraphs

Juan Miguel Arrazola* and Thomas R. Bromley†  
Xanadu, 372 Richmond Street W, Toronto, Ontario M5V 1X6, Canada

![](images/49cbea7b05b58233cccbc189a6fcbf89e9fb30dd94710528a45e04b87d214178.jpg)

(Received 5 April 2018; revised manuscript received 14 May 2018; published 19 July 2018)

Boson sampling devices are a prime candidate for exhibiting quantum supremacy, yet their application for solving problems of practical interest is less well understood. Here we show that Gaussian boson sampling (GBS) can be used for dense subgraph identification. Focusing on the NP-hard densest  $k$ -subgraph problem, we find that stochastic algorithms are enhanced through GBS, which selects dense subgraphs with high probability. These findings rely on a link between graph density and the number of perfect matchings—enumerated by the Hafnian—which is the relevant quantity determining sampling probabilities in GBS. We test our findings by constructing GBS-enhanced versions of the random search and simulated annealing algorithms and apply them through numerical simulations of GBS to identify the densest subgraph of a 30 vertex graph.

DOI: 10.1103/PhysRevLett.121.030503

Quantum algorithms are often designed with the assumption that they can access the full power of universal quantum computation. However, presently developing quantum devices have limited resource capabilities and are not fault tolerant. Their emergence has motivated a reexamination of methods for designing quantum algorithms, with the focus now on harnessing the computational power of small-scale, noisy quantum computers. Candidate algorithms for near-term devices include quantum simulators for many-body physics [1,2], variational algorithms [3-6], quantum approximate optimization algorithms [7,8], and machine learning on hybrid devices [9-13].

Boson sampling is a limited model of quantum computation given by passing photons through a linear interferometer and observing their output configurations [14]. Significant efforts have been performed to implement boson sampling [15-18], leading to the proposal of related models such as scattershot boson sampling [19-21] and Gaussian boson sampling [22,23] that are more suitable for experimental realizations. Moreover, boson sampling devices are, in principle, capable of performing tasks that cannot be efficiently simulated on classical computers, a feature that has made them a leading candidate for challenging the extended Church-Turing thesis. In fact, the primary objective of implementing boson sampling has so far been to demonstrate quantum supremacy, leaving the real-world application of such devices underdeveloped. A notable exception is the use of Gaussian boson sampling for efficiently calculating the vibronic spectra of molecules, [24-26], which provided the first clue of the usefulness of this platform.

In this work, we show that Gaussian boson sampling (GBS) can be used to enhance classical stochastic algorithms for the densest  $k$ -subgraph (DkS) problem. The DkS problem is NP-Hard [27] and defined through the following

optimization task: given a graph  $G$  with  $n$  vertices, find the subgraph of  $k < n$  vertices with the largest density. Among subgraphs with a fixed number of vertices, the density and the number of edges are equivalent quantities, and we hence refer to both interchangeably throughout this Letter. Beyond its fundamental interest in mathematics and theoretical computer science, the DkS problem has a natural connection to clustering problems with the goal of finding highly correlated subsets of data. Clustering has applications in a wide range of fields such as data mining [28-31], bioinformatics [32,33], and finance [34].

Our approach uses a technique from Ref. [35] to encode a graph into the GBS paradigm. Here, the probability of observing a given photon configuration is proportional to the number of perfect matchings of the corresponding subgraph. We highlight a correspondence between the number of perfect matchings in a subgraph and its density, meaning that a suitably programmed GBS device will prefer to output dense subgraph configurations. Following results in a companion paper [36], we see that this is a form of proportional sampling that can be used to enhance the stochastic element of classical optimization heuristics for the DkS problem. Since no polynomial-time approximation schemes are believed to exist for the DkS problem [37], certain worst-case instances requiring superpolynomial run-time may be best tackled using stochastic algorithms. Our findings are illustrated for a fixed graph, where we introduce GBS-enhanced hybridizations of random search and simulated annealing algorithms. This approach highlights a general principle of using output samples from a GBS device to enhance approximate solutions to optimization problems.

Applying GBS to the DkS problem.-The important concepts of GBS are first briefly reviewed. In GBS, photon-number detection is performed on a multimode Gaussian

state [22,23,38]. For an  $n$ -mode system, we denote the possible outputs of GBS by vectors  $S = (s_1, s_2, \dots, s_n)$ , where  $s_i$  is the number of photons detected in output mode  $i$ . It was shown in Ref. [22] that the probability of observing an output pattern  $S$  is

$$
P (S) = \left| \sigma_ {Q} \right| ^ {- \frac {1}{2}} \frac {\operatorname {H a f} \left(\mathcal {A} _ {S}\right)}{s _ {1} ! s _ {2} ! \cdots s _ {n} !}, \tag {1}
$$

where  $\sigma_{Q} = \sigma +\mathbb{1}_{2n} / 2$ $\sigma$  is the  $(2n\times 2n)$  -dimensional covariance matrix of the  $n$  -mode Gaussian state, and  $\mathcal{A}_S$  is a submatrix of  $\mathcal{A} = (\mathbb{1}_{n}^{0}\mathbb{1}_{0}^{1_n})[\mathbb{1}_{2n} - \sigma_Q^{-1}]$  fixed by  $S$  .The function  $\operatorname {Haf}(\mathcal{A}_S)$  is the Hafnian of  $\mathcal{A}_S$  [39].

Following Ref. [35], given the adjacency matrix  $A$  of an  $n$  vertex graph  $G$ , we set  $\mathcal{A} \coloneqq c(A \oplus A)$ , where  $c < \lambda^{-1}$  and  $\lambda$  is the largest eigenvalue of  $A$ . The resulting covariance matrix is such that its corresponding Gaussian state is pure and can hence be prepared by injecting single-mode squeezed states into a linear optics interferometer [38]. We focus on post-selecting output samples from GBS such that  $s_i \in \{0, 1\}$  and  $\sum_{i} s_i = k$  for a fixed even  $k$ , i.e., the set of samples with even- $k$  photons and where no output mode has more than one photon detected—referred to here as the  $k$  collision-free subspace. The probability of getting such an event from GBS is  $p_{k\mathrm{cf}} \coloneqq p(k \wedge \mathrm{cf}) = p(\mathrm{cf}|k)p(k)$ , where  $p(\mathrm{cf}|k)$  is the collision-free probability given  $k$  photons and  $p(k)$  is the probability of  $k$  photons. Here,  $p(\mathrm{cf}|k)$  is fixed by the size of  $k$  in comparison to  $n$ , and is expected to be close to unity for  $k \ll n$ . On the other hand,  $p(k)$  is controlled by the amount of input squeezing and can be maximized by the user through the choice of  $c$ .

By postselecting on the  $k$  collision-free subspace, the probability of a valid output pattern  $S$  is

$$
P _ {k \mathrm {c f}} (S) = | \sigma_ {Q} | ^ {- \frac {1}{2}} \frac {c ^ {2} | \operatorname {H a f} \left(A _ {S}\right) | ^ {2}}{p _ {k \mathrm {c f}}}, \tag {2}
$$

where  $A_{S}$  is the adjacency matrix corresponding to the subgraph of  $A$  selected by  $S$ . Crucially, the Hafnian of an adjacency matrix is equal to the number of perfect matchings in the corresponding graph, i.e., the number of independent sets of edges in which every vertex of the graph is connected to exactly one edge [39]. Equation (2) hence highlights a remarkable feature: the greater the number of perfect matchings in a subgraph, the more likely its corresponding sample is to be outputted through GBS.

Our next step is to highlight a correspondence between the number of perfect matchings in a graph and its density. Intuitively, a graph with many perfect matchings is expected to contain many edges. This intuition was made quantitative in Ref. [40], where it was shown that the number of perfect matchings in a graph  $G$  with  $2m$  vertices is upper bounded by a monotonically increasing function of the number of edges  $l$ , i.e.,

$$
\mathrm {P M} (G) \leq \left(\left\lfloor \frac {l}{n} \right\rfloor !\right) ^ {\left[ (m - \alpha) / \left\lfloor (l / m) \right\rfloor\right]} \left(\left\lceil \frac {l}{m} \right\rceil !\right) ^ {\left[ (\alpha) / \left\lfloor (l / m) \right\rfloor\right]}, \tag {3}
$$

where  $\alpha \coloneqq l - m\lfloor (l / m)\rfloor$  . Thus, given the number of perfect matchings in a graph with  $k\coloneqq 2m$  vertices, Eq. (3) provides a lower bound to the number of edges in the graph. Figure 1 illustrates the close relationship between the number of perfect matchings and edges of random graphs, highlighting the usefulness of the above bound. This relationship provides a crucial insight: when sampling from the GBS distribution of Eq. (2), the subgraphs that are most likely to appear have high density.

Hence, by programming a GBS device appropriately, it is possible to sample from a distribution that naturally favors dense subgraphs. This is an example of proportional sampling, as described in Ref. [36]. In fact, as can be seen in Fig. 1, the Hafnians of dense graphs can be many orders of magnitude larger than the Hafnians of sparser graphs. For example, the Hafnian of a complete graph of  $k$  vertices is equal to  $(k - 1)!!$ . Through proportional sampling, this means that the probability of finding dense graphs is augmented by a correspondingly large factor. Conversely, graphs with few edges will have either zero or negligible Hafnians, and will therefore almost never be sampled. The combined effect of these features is a GBS distribution that ignores sparse graphs and gives us a much improved chance of discovering the dense ones.

Proportional sampling leads to a simple algorithm for approximately solving the DkS problem for even  $k$ : generate many samples from GBS with  $\mathcal{A} = c(A \oplus A)$  and pick the subgraph with the largest density. For odd  $k$ , one can output  $k + 1$  vertex subgraphs and remove the vertex with the lowest degree. This amounts to an enhanced random search algorithm. However, it is often of interest to

![](images/4393c7fef5aede86206db37ac400362b766c3991b901e237e39f2a41d29c8c9c.jpg)  
FIG. 1. Relationship between the number of perfect matchings and the number of edges for random graphs of  $k = 16$  vertices. The random graphs are generated by adding each possible edge with probability  $p$ . We generate samples for each value of  $p = 0.1, 0.2, \ldots, 1$  for a total of approximately 6000 random graphs, and plot their number of edges against the Hafnian of the adjacency matrix. The dashed line is the lower bound from Eq. (3).

use more advanced stochastic algorithms that also harness the local structure of an optimization landscape to improve beyond random search. We discuss in the following how simulated annealing can be enhanced for solving the DkS problem by using randomness from GBS.

Before doing so, we motivate the use of a physical GBS device for proportional sampling according to Eq. (2). Indeed, since the Hafnian of an adjacency matrix can be classically approximated in polynomial time [41], there exist polynomial-time classical approaches for approximate GBS, such as using rejection sampling or metropolized independent sampling [42,43]. A physical GBS device, on the other hand, requires constant time to output a sample, leading to a polynomial advantage over these classical methods. Moreover, GBS devices can, in principle, have very fast sample rates, limited primarily by detector dead times. We also emphasize the inherent robustness of our approach to noise and imperfections in the device, which may typically degrade the intrinsic bias of GBS but not eliminate it completely.

Enhancing stochastic algorithms through GBS.—There is a varied collection of classical algorithms for finding dense subgraphs, see for example Ref. [44] for a survey. Among these are randomized and deterministic algorithms, each suitable for specific scenarios. Deterministic greedy algorithms can efficiently find subgraphs of large density, but they can be fooled by graphs with special structure. For instance, a widely used algorithm of Charikar [45] relies on iteratively eliminating vertices with the lowest degree, but it is incapable of detecting isolated dense subgraphs. On the other hand, the randomness in stochastic algorithms allows them to avoid being fooled by special graph structure, making them a natural choice when little is known about the graph under consideration. In terms of computational complexity, no polynomial-time approximation scheme exists for solving the Dks problem to constant multiplicative error [37] unless the exponential time hypothesis is false. This means that classes of graphs exist where all known polynomial-time algorithms fail, in which case stochastic algorithms may possibly be preferable.

We show how GBS can be used to enhance stochastic algorithms. These algorithms combine exploration of the problem space with exploitation of local structure. Exploration can be achieved by randomly searching through the space, while exploitation involves tweaking candidate solutions and checking for an improvement. For graph problems, tweaking can be an operation where a candidate subgraph is modified by replacing a random subset of its vertices with other randomly chosen vertices. Classical algorithms employ uniform randomness for exploration and exploitation. However, following Ref. [36], we can use biased randomness from GBS to enhance stochastic algorithms for the DkS problem. Crucially, this improvement is not algorithm specific and

works for any method using exploration and exploitation, regardless of inner details of the routine.

To enhance exploration, one simply samples from the GBS distribution of Eq. (2), as formalized by the routine GBS-Explore in Ref. [36]. For exploitation, we can improve the tweak stage by using GBS to randomly select which vertices of candidate subgraphs to remove and also which ones to replace them with. More precisely, for a subgraph of even  $k$  vertices with adjacency matrix  $A_{S}$ , we perform the following routine GBS-Tweak for a fixed even  $l < k$  denoting the minimum number of vertices to be left untweaked: (1) Generate  $R$  as an  $l$  vertex subgraph of  $S$  with adjacency matrix  $A_{S,R}$  according to the GBS distribution  $P_{l\mathrm{cf}} \sim |\mathrm{Haf}(A_{S,R})|^2$ . Extend  $R$  by picking a uniform random number  $m \in \{0,1,\dots,k - l - 1\}$  of the vertices remaining from  $S$ , along with the corresponding edges. This is the subgraph  $A_{S,\mathrm{keep}}$  that specifies the  $l + m$  vertices to be kept. (2) Generate  $T$  as a  $k - l$  vertex subgraph of  $A$  with adjacency matrix  $A_{T}$  according to the GBS distribution  $P_{(k - l)\mathrm{cf}} \sim |\mathrm{Haf}(A_{T})|^2$ . Reduce  $T$  by randomly rejecting  $m$  of its vertices and corresponding edges. This is the subgraph  $A_{T,\mathrm{replace}}$  that specifies the  $k - l - m$  vertices that will be added to  $A_{S,\mathrm{keep}}$ . If  $A_{S,\mathrm{keep}}$  and  $A_{T,\mathrm{replace}}$  share any vertices, repeat this step. (3) Output the  $k$  vertex subgraph  $A_{S,\mathrm{keep}} \bigcup A_{T,\mathrm{replace}}$ . GBS allows tweaking itself to become exploitative, with a twofold improvement: since  $R$  and  $T$  are likely to be dense subgraphs, their composition should also be dense. We introduce the random parameter  $m$  to vary the number of tweaked vertices.

GBS enhanced exploration and exploitation can be used within stochastic algorithms. Since random search only uses exploration, we discuss another example here. Simulated annealing is a heuristic optimization algorithm that combines elements of random search and hill climbing [46]. Whenever a new subgraph is generated, if its density is larger than the current one, it is retained. If its density is smaller, the new submatrix can still be retained with a probability that depends on the difference between the densities and a temperature parameter. The temperature is initially high and new subgraphs are often accepted, even if they have lower density. This is a feature that can prevent the search from becoming stuck in local minima. As the algorithm progresses, the temperature is lowered and only denser submatrices are kept, leading to an effective hill-climbing behavior. This algorithm is detailed in pseudocode in the Supplemental Material [47].

Example DkS problem.-To illustrate the enhancement to stochastic algorithms provided by GBS, we apply GBS enhanced random search and simulated annealing to the problem of locating a planted subgraph with large density, but whose vertices have low degree compared to the rest of the graph, see Fig. 3. Such low-degree planted graphs are, by construction, hard to find for deterministic algorithms based on vertex degree. These graphs can model the presence of tightly knit but otherwise isolated communities

![](images/acbe1ff2745762a37ed969bb0cb5ec50820eba77afd0840be03a2ffe264948c8.jpg)  
FIG. 2. Performance of random search (left) and simulated annealing (right) algorithms for finding the densest subgraph of 10 vertices in the graph of Fig. 3. The top red curve corresponds to using GBS exploration and (for simulated annealing) GBS tweaking, while the bottom grey curve corresponds to the uniform random counterparts. The solid curves are the averages over 400 repetitions and the error bars represent one standard deviation. The straight horizontal line shows the number of edges, 34, in the dense subgraph found by the algorithm of Ref. [45]. The densest subgraph has 42 edges.

![](images/7bfd350802f2b4d27dca4226c55e3cd5e9a7668169264c30d0a09f0857a36d01.jpg)

in social networks: members of these communities are highly connected to each other (large density) but have few connections in total compared to typical members of the broader network (low degree). Note that more advanced deterministic algorithms can be designed to solve the DkS problem for this family of graphs [48].

To access GBS samples, we use the Hafnian formula of Ref. [49] to perform a brute force simulation of the entire probability distribution, which limits the size of graphs that we can sample from. Our graph was fixed to 30 vertices with a planted subgraph of 10 vertices. The graph was constructed by (i) generating a random graph of 20 vertices with probability  $p = 0.5$  of adding an edge, (ii) creating a random subgraph of 10 vertices with probability  $q = 0.875$  of having an edge, and (iii) selecting 8 vertices at random in both

![](images/09691de01c5f547542b7e4ffb642cd49711b8399f1c9de8d156a1887d6268fa4.jpg)  
FIG. 3. A random graph of 30 vertices with a planted dense subgraph of 10 vertices (highlighted in red with thick edges) [47]. Vertices in the planted subgraph have lower degree than most other vertices in the graph, yet the density of the planted subgraph is the highest. This property prevents degree-based deterministic algorithms from finding the planted subgraph.

graphs and adding an edge between them. The result is shown in Fig. 3, with the adjacency matrix available as Supplemental Material [47]. Here, the planted vertices have a lower average degree than other vertices, leading to a planted graph that is invisible to algorithms based on vertex degree.

Figure 2 illustrates the performance of random search and simulated annealing. The plots each show the results of using GBS and uniform sampling in explore and exploit stages. The results are averaged over 400 repetitions to remove statistical fluctuations, with the standard deviation also included. The simulated annealing parameters are  $T = 0.01$ , with a linear cooling schedule, and  $l = 6$ . Here it is relevant to compare both the performance of simulated annealing over random search and the performance of using GBS over uniform sampling. It is first clear to see that GBS provides an advantage in both cases, illustrating our general findings that GBS is an enhancement for stochastic optimization algorithms. Furthermore, we see that simulated annealing is typically superior to random sampling and extends earlier beyond the region accessible by the deterministic algorithm of Ref. [45] (32 edges). Note, however, that GBS random search is particularly successful in the low sample number regime, outperforming both uniform and GBS simulated annealing for less than 50 samples. This is a remarkable observation given the simplicity of GBS random search.

Discussion.-We have shown that Gaussian boson sampling (GBS) is a useful tool for finding dense subgraphs. This results from the capability of GBS to perform proportional sampling for the canonical problem known as Max-Haf, highlighted in Ref. [36], as well as the link between the number of perfect matchings (given by the Hafnian) and the density of a graph. This allows for tailored stochastic algorithms to be constructed for finding approximate solutions to the densest  $k$ -subgraph (DkS) problem.

It is important to emphasize that in the context of optimization, GBS is best understood as a quantum enhancement of stochastic algorithms. Although accurate deterministic algorithms exist, they can always be fooled under certain circumstances. Indeed, the DkS problem is NP-Hard and there are difficult instances for which no polynomial-time approximation algorithms exist, assuming the exponential time hypothesis [37]. This highlights a situation where stochastic algorithms, and their enhancement through GBS, are expected to be useful. Note that well-performing deterministic algorithms may also be enhanced through GBS by designing randomized versions.

These findings move away from the traditional approach to constructing quantum algorithms of rigorously showing a speedup in comparison to the best known classical algorithms. The heuristics-based approach followed here can instead allow for quantum enhancements to be identified in near-term devices. Overall, further research is needed to fully understand the potential advantages of enhancing stochastic algorithms through GBS when compared to highly optimized classical deterministic algorithms for dense subgraph identification and approximate optimization in general.

The authors thank Alex Arkhipov, Kamil Brádler, Pierre-Luc Dallaire-Demers, Nathan Killoran, Seth Lloyd, Patrick Rebentrost, Christian Weedbrook, and an anonymous referee for valuable discussions.

*juanmiguel@xanadu.ai  
†tom@xanadu.ai  
[1] J. Zhang, G. Pagano, P. W. Hess, A. Kyprianidis, P. Becker, H. Kaplan, A. V. Gorshkov, Z.-X. Gong, and C. Monroe, Nature (London) 551, 601 (2017).  
[2] H. Bernien, S. Schwartz, A. Keesling, H. Levine, A. Omran, H. Pichler, S. Choi, A. S. Zibrov, M. Endres, M. Greiner et al., Nature (London) 551, 579 (2017).  
[3] A. Peruzzo, J. McClean, P. Shadbolt, M.-H. Yung, X.-Q. Zhou, P.J. Love, A. Aspuru-Guzik, and J.L. O'Brien, Nat. Commun. 5, 4213 (2014).  
[4] J.R. McClean, J. Romero, R. Babbush, and A. Aspuru-Guzik, New J. Phys. 18, 023023 (2016).  
[5] N. Moll, P. Barkoutsos, L. S. Bishop, J. M. Chow, A. Cross, D. J. Egger, S. Filipp, A. Fuhrer, J. M. Gambetta, M. Ganzhorn et al., arXiv:1710.01022.  
[6] A. Kandala, A. Mezzacapo, K. Temme, M. Takita, M. Brink, J. M. Chow, and J. M. Gambetta, Nature (London) 549, 242 (2017).  
[7] E. Farhi, J. Goldstone, and S. Gutmann, arXiv:1411.4028.  
[8] E. Farhi and A. W. Harrow, arXiv:1602.07674.  
[9] Z. Li, X. Liu, N. Xu, and J. Du, Phys. Rev. Lett. 114, 140504 (2015).  
[10] D. Riste, M. P. Da Silva, C. A. Ryan, A. W. Cross, A. D. Corcoles, J. A. Smolin, J. M. Gambetta, J. M. Chow, and B. R. Johnson, Quantum Information 3, 16 (2017).  
[11] M. Benedetti, J. Realpe-Gómez, R. Biswas, and A. Perdomo-Ortiz, Phys. Rev. X 7, 041052 (2017).

[12] J. Otterbach, R. Manenti, N. Alidoust, A. Bestwick, M. Block, B. Bloom, S. Caldwell, N. Didier, E. S. Fried, S. Hong et al., arXiv:1712.05771.  
[13] M. Schuld and N. Killoran, arXiv:1803.07128.  
[14] S. Aaronson and A. Arkhipov, in Proceedings of the Forty-Third Annual ACM Symposium on Theory of Computing (ACM, New York, 2011), p. 333.  
[15] J. B. Spring, B. J. Metcalf, P. C. Humphreys, W. S. Kolthammer, X.-M. Jin, M. Barbieri, A. Datta, N. Thomas-Peter, N. K. Langford, D. Kundys et al., Science 339, 798 (2013).  
[16] M. A. Broome, A. Fedrizzi, S. Rahimi-Keshari, J. Dove, S. Aaronson, T. C. Ralph, and A. G. White, Science 339, 794 (2013).  
[17] M. Tillmann, B. Dakić, R. Heilmann, S. Nolte, A. Szameit, and P. Walther, Nat. Photonics 7, 540 (2013).  
[18] A. Crespi, R. Osellame, R. Ramponi, D.J. Brod, E.F. Galvao, N. Spagnolo, C. Vitelli, E. Maiorino, P. Mataloni, and F. Sciarrino, Nat. Photonics 7, 545 (2013).  
[19] A. P. Lund, A. Laing, S. Rahimi-Keshari, T. Rudolph, J. L. O'Brien, and T. C. Ralph, Phys. Rev. Lett. 113, 100502 (2014).  
[20] M. Bentivegna, N. Spagnolo, C. Vitelli, F. Flamini, N. Viggianiello, L. Latmiral, P. Mataloni, D.J. Brod, E.F. Galvão, A. Crespi et al., Sci. Adv. 1, e1400255 (2015).  
[21] L. Latmiral, N. Spagnolo, and F. Sciarrino, New J. Phys. 18, 113008 (2016).  
[22] C. S. Hamilton, R. Kruse, L. Sansoni, S. Barkhofen, C. Silberhorn, and I. Jex, Phys. Rev. Lett. 119, 170501 (2017).  
[23] R. Kruse, C. S. Hamilton, L. Sansoni, S. Barkhofen, C. Silberhorn, and I. Jex, arXiv:1801.07488.  
[24] J. Huh, G. G. Guerreschi, B. Peropadre, J. R. McClean, and A. Aspuru-Guzik, Nat. Photonics 9, 615 (2015).  
[25] W. R. Clements, J. J. Renema, A. Eckstein, A. A. Valido, A. Lita, T. Gerrits, S. W. Nam, W. S. Kolthammer, J. Huh, and I. A. Walmsley, arXiv:1710.08655.  
[26] C. Sparrow, E. Martin-López, N. Maraviglia, A. Neville, C. Harrold, J. Carolan, Y.N. Joglekar, T. Hashimoto, N. Matsuda, J.L. O'Brien et al., Nature (London) 557, 660 (2018).  
[27] U. Feige, D. Peleg, and G. Kortsarz, Algorithmica 29, 410 (2001).  
[28] R. Kumar, P. Raghavan, S. Rajagopalan, and A. Tomkins, Comput. Networks 31, 1481 (1999).  
[29] A. Angel, N. Sarkas, N. Koudas, and D. Srivastava, Proc. VLDB Endowment 5, 574 (2012).  
[30] A. Beutel, W. Xu, V. Guruswami, C. Palow, and C. Faloutsos, in Proceedings of the 22nd International Conference on World Wide Web (ACM, New York, 2013), p. 119.  
[31] J. Chen and Y. Saad, IEEE Trans. Knowledge Data Eng. 24, 1216 (2012).  
[32] E. Fratkin, B. T. Naughton, D. L. Brutlag, and S. Batzoglou, Bioinformatics 22, e150 (2006).  
[33] B. Saha, A. Hoch, S. Khuller, L. Raschid, and X.-N. Zhang, Annual International Conference on Research in Computational Molecular Biology (Springer, Berlin, 2010), p. 456.  
[34] S. Arora, B. Barak, M. Brunnermeier, and R. Ge, Commun. ACM 54, 101 (2011).  
[35] K. Brádler, P.-L. Dallaire-Demers, P. Rebentrost, D. Su, and C. Weedbrook, arXiv:1712.06729.

[36] J. M. Arrazola, T. R. Bromley, and P. Rebentrost, Phys. Rev. A 98, 012322 (2018).  
[37] P. Manurangsi, in Proceedings of the 49th Annual ACM SIGACT Symposium on Theory of Computing (ACM, Montreal, Canada, 2017), p. 954, DOI: 10.1145/3055399.3055412.  
[38] C. Weedbrook, S. Pirandola, R. García-Patron, N. J. Cerf, T. C. Ralph, J. H. Shapiro, and S. Lloyd, Rev. Mod. Phys. 84, 621 (2012).  
[39] A. Barvinok, Combinatorics and Complexity of Partition Functions (Springer, Berlin, 2016), Vol. 274.  
[40] M. Aaghabali, S. Akbari, S. Friedland, K. Markstrom, and Z. Tajfirouz, Eur. J. Combinatorics 45, 132 (2015).  
[41] M. Rudelson, A. Samorodnitsky, and O. Zeitouni, Ann. Probability 44, 2858 (2016).  
[42] A. Neville, C. Sparrow, R. Clifford, E. Johnston, P.M. Birchall, A. Montanaro, and A. Laing, Nat. Phys. 13, 1153 (2017).

[43] J. S. Liu, Stat. Comput. 6, 113 (1996).  
[44] V. E. Lee, N. Ruan, R. Jin, and C. Aggarwal, in Managing and Mining Graph Data (Springer, New York, 2010), p. 303.  
[45] M. Charikar, in International Workshop on Approximation Algorithms for Combinatorial Optimization (Springer, Berlin, 2000), pp. 84-95.  
[46] P. van Laarhoven and E. Aarts, Simulated Annealing: Theory and Applications (Springer, Berlin, 1987), Vol. 37.  
[47] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.121.030503 for simulated annealing pseudocode and the CSV file of the graph adjacency matrix. The densest subgraph is specified by the last 10 entries.  
[48] E. Hazan and R. Krauthgamer, SIAM J. Computing 40, 79 (2011).  
[49] A. Björklund, B. Gupt, and N. Quesada, arXiv:1805.12498.