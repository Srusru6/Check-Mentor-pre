PHYSICS

# Quantum Walks Through a Waveguide Maze

Compared to classical objects, a quantum object such as a photon will randomly search through a maze in fewer steps.

# Mark Hillery

Two of the major goals of the field of quantum information are to build a quantum computer—one that processes bits of information according to quantum rather than classical rules—and to figure out what to do with one, once you have it. The field that encompasses the latter goal is quantum algorithms. It has not been easy to develop quantum algorithms, but within the past 10 years, a fruitful approach has arisen based on what are known as quantum walks, which in the classical world are the basis for a description of diffusion processes. On page 1500 of this issue, Peruzzo et al. (1) describe a device they have built that substantially improves our ability to perform quantum walks. They used it to follow two photons that are performing a quantum walk along a line.

It is best to approach quantum walks by comparing them with classical random walks. To perform the simplest random walk, begin by flipping a coin, and take one step to the right, when it comes up heads, and one step to the left, when it comes up tails. Repeat this process a num

ber of times, and you will have experienced a random walk (see the figure, panel A). This surprisingly simple process can serve as a model for how the smell from a bottle of perfume diffuses throughout a room, or how a stock price moves up and down. It also serves as the basis for a number of random computer algorithms. Thus, the quantum version of a random walk, a quantum walk, could be used as a basis for quantum algorithms.

Random walks are performed by classical objects, but quantum walks are performed by quantum objects such as photons. Peruzzo et al. start a photon traveling down a channel (waveguide) in an optical medium. This medium has many parallel channels, and the photon can leak from one channel to another.

![](images/5d3659b9c0644b8955158fc4efed02e3eaa3943864686ba942c30c18e3280f7e.jpg)

Walk like a photon. The difference between a classical random walk and a quantum walk is illustrated. (A) After starting at the origin and making a classical random walk of 100 steps, a classical cat is most likely to be found where it started (top). (B) A quantum object starting at the origin and making a quantum walk of 100 steps will most likely be found about 70 steps to the right or to the left of where it started. Here the object is represented by a cat, but in the study by Peruzzo et al., the walkers are two photons. Quantum walks can help speed up search algorithms based on random walks.

These channels serve as the locations in the quantum walk. In other words, we are interested in which channel the photon is located after it has "walked" for a certain amount of time (see the figure, panel B).

The difference between the classical random walk and the quantum walk is a phenomenon known as interference. Quantum objects like photons experience it, whereas classical objects, including people, do not. Suppose the photon can get from one channel to another via two different paths. Each of these paths is assigned a complex number called an amplitude. According to the rules of quantum mechanics, the probability that the photon makes the transition from one channel to the other can be obtained by adding the amplitudes and then squaring the magnitude of this complex number. Thus, each individual path can give a nonzero probability for the photon to transfer channels, but there are no probabilities for the photon to pass through channels.

are circumstances under which the two paths combine such that there is zero chance that this transition occurs. Interference makes the behavior of a quantum walk very different from that of a random walk.

Quantum walks come in two basic types—one in which the movement proceeds in discrete steps, and one in which the movement is continuous (2, 3). Peruzzo et al. examined a continuous quantum walk on a line. Theorists initially studied the behavior of a quantum walk on a line, but went on to look at walks on more complicated structures such as grids,  $n$ -dimensional cubes, and tree graphs (graphs with no closed paths). These structures are collectively called graphs, a graph being just a collection of vertices with edges between them.

The first application of quantum walks was to searches (4). One of the vertices in the graph, called the marked vertex, has different properties than the others, and we would like to find out which vertex it is. What typically happens is that after  $N^{\frac{1}{2}}$  steps, where  $N$  is the number of vertices, the particle making the walk becomes localized on the marked vertex, so we just

look and see where the particle is, and that is the marked vertex. It is also possible to locate marked edges as well as subgraphs within a graph (5). Classically, it would be necessary to check each vertex to see if it is the marked one, which would require  $N$  steps, so quantum walks make the procedure more efficient.

Recently, two quantum algorithms based on quantum walks have been discovered. The first, developed by Ambainis, makes use of a black box that evaluates the output function,  $f(x)$ , for a given input  $x$  (6). The object is to find two different inputs that give the same output, or else reveal that each input gives a different output. Ambainis's quantum algorithm is more efficient than any classical algorithm for the same task. The second, developed by Farhi, Goldstone, and Gutman, can evaluate certain kinds of Boolean formulas (logical statements) more efficiently than can be done on a classical computer (7).

On the experimental side, quantum walks have been performed in a number of different systems, including trapped ions, atoms in optical lattices, and photons. A distinctive feature of the method described by Peruzzo et al. is their use of two walkers, i.e., two photons. They measured quantum correlations between the photons that are stronger than those that can be obtained with phase-averaged classical light. There have been only a few investigations of quantum walks with two walkers, and most of these have focused on the case in which the walkers can undergo statistical correlations, as in the study of Peruzzo et al., but do not interact through forces (for example, as

charged particles might do). Recently, Gamble et al. (8) found that two interacting walkers are more successful at distinguishing nonisomorphic graphs (ones that connect vertices differently) than are noninteracting walkers.

There is still a great deal to be learned about quantum walks. For a single walker, walks on more complicated graphs or simple graphs with defects are possible areas of investigation. Walks with multiple walkers, both the noninteracting and interacting cases, are relatively unexplored. Finally, it is possible that more quantum algorithms will emerge from a better understanding of quantum walks that will enable new ways to

speed up computation.

# References

1. A. Peruzzo, Science 329, 1500 (2010).  
2. D. Aharonov, A. Ambainis, J. Kempe, U. Vazirani, in Proceedings of the 33rd Annual ACM Symposium on Theory of Computing (Association for Computing Machinery, New York, 2001), pp. 50-59.  
3. E. Farhi, S. Gutman, Phys. Rev. A 58, 915 (1998).  
4. N. Shenvi, J. Kempe, K. B. Whaley, Phys. Rev. A 67, 052307 (2003).  
5. M. Hillary, D. Reitzner, V. Buzek, Phys. Rev. A 81, 062324 (2010).  
6. A. Ambainis, SIAM J. Comput. 37, 210 (2007).  
7. E. Farhi, J. Goldstone, S. Gutman, Theory Comput. 4, 169 (2008).  
8. J. K. Gamble, M. Friesen, D. Zhou, R. Joynt, S. N. Coppersmith, http://arxiv.org/abs/1002.3003 (2010).

10.1126/science.1195446

# NEUROSCIENCE

# Should Confidence Be Trusted?

# Hakwan Lau<sup>1,2</sup> and Brian Maniscalco<sup>1</sup>

Imagine two witnesses in a courtroom. One is absolutely sure of her testimony; the other gives opposing testimony, but is less confident. Who would you trust more? All else being equal, we would tend to trust the former, because we believe that judgments made with high confidence are more accurate. This correlation between confidence and accuracy, though often true, unfortunately is not infallible. On page 1541 in this issue, Fleming et al. (1) report a relationship between the brain scans of people obtained by magnetic resonance imaging (MRI) and how seriously we should take their expressed level of confidence.

When analyzing how confidence predicts accuracy, it is desirable to account for the effect of "response bias." For instance, perhaps the witness's high confidence is driven by a brash personality rather than a genuinely accurate memory. The problem of response bias is traditionally addressed by methods such as "signal detection theory," which is an analytic tool that allows us to separate efficacy from bias (2). By applying such techniques (3), one can characterize how well the subject's expressed level of confidence distinguishes between correct and incorrect responses, independent of response bias. This measure of the efficacy of confidence ratings has been called "type 2 performance" to distinguish it from "type 1 performance," which measures how accurately a subject actually identifies a stimulus.

![](images/53b6ffc3eb7627fb7398194c40d52200c396d379d776ff2d0ec99a0ad168b9ce.jpg)  
Confidence ratings. Why does a witness's expressed level of confidence, when giving testimony, affect our judgement of its accuracy?

In other words, high type 2 performance indicates a close relationship between the confidence of the subjects and how accurately they identify the stimulus.

But there is another problem: Type 2 performance is influenced by type 1 performance (3). The intuition is simple: Suppose a subject has great difficulty making accurate judgments about stimuli (such as the orientation of a figure), making many incorrect judgments as well as "fluke" judgments that are correct only by chance. The subject cannot distinguish incorrect judgments from those that are correct only by chance; they all seem like guesses. Thus, some variation in type 2 performance may be attributable merely to the quality of "lower-level" stimulus processing in the brain (i.e., type 1 performance). To isolate this confounding factor, Fleming et al. controlled for type 1 performance by programming a computer to give harder

The ability to monitor the efficacy of one's own perception is associated with differences in the structure of specific brain regions.

trials to the better observers, and easier trials to the poorer observers. The authors still found substantial variability in type 2 performance across 32 observers. Also, structural MRI brain scans revealed that those observers with a high type 2 performance had higher gray matter signal intensity (which implies greater volume or density) in the frontal lobe than the low type 2 performers. The difference was most prominent in the frontal polar areas, but also was apparent in the dorsal lat

eral prefrontal cortex and anterior cingulate cortex. Furthermore, neuronal fibers connecting these regions showed higher signal intensity in the MRI scans.

The results speak to the debated issue (4) of whether type 2 performance reflects genuine metacognition (5)—that is, cognition about another cognitive process, rather than about an external stimulus. For instance, one may argue that confidence ratings in a perceptual task may be made by tracking the strength of the external stimulus, rather than by introspection of the efficacy of the perceptual process (metacognition). However, metacognition is one plausible way in which such confidence ratings can be made, as has been demonstrated by computational modeling (6). The correlation of type 2 performance with structures in the frontal polar region of the brain seems to support the metacognitive account, because this area is at the top of the