# QUANTUM COMPUTING

# Generation of time-domain-multiplexed two-dimensional cluster state

Warit Asavanant<sup>1</sup>, Yu Shiozawa<sup>1</sup>, Shota Yokoyama<sup>2</sup>, Baramee Charoensombutamon<sup>1</sup>, Hiroki Emura<sup>1</sup>, Rafael N. Alexander<sup>3</sup>, Shuntaro Takeda<sup>1,4</sup>, Jun-ichi Yoshikawa<sup>1</sup>, Nicolas C. Menicucci<sup>5</sup>, Hidehiro Yonezawa<sup>2</sup>, Akira Furusawa<sup>1*</sup>

Entanglement is the key resource for measurement-based quantum computing. It is stored in quantum states known as cluster states, which are prepared offline and enable quantum computing by means of purely local measurements. Universal quantum computing requires cluster states that are both large and possess (at least) a two-dimensional topology. Continuous-variable cluster states—based on bosonic modes rather than qubits—have previously been generated on a scale exceeding one million modes, but only in one dimension. Here, we report generation of a large-scale two-dimensional continuous-variable cluster state. Its structure consists of a 5- by 1240-site square lattice that was tailored to our highly scalable time-multiplexed experimental platform. It is compatible with Bosonic error-correcting codes that, with higher squeezing, enable fault-tolerant quantum computation.

Quantum computers promise applications beyond what is possible with their classical counterparts (1). Recent work has produced advances in quantum computing with stationary matter qubits such as superconducting systems (2), ion trap systems (3), and silicon-based systems (4). With access to both high-quality qubits and high-fidelity quantum gates, it is thus believed that a small-scale quantum computer is within reach. In order to bring these platforms to the scale at which they become useful, efforts [for example, (5)] have been made to address the difficulties of preparing, interfacing, addressing, and tuning large numbers of qubits. However, a technological leap will be necessary to achieve a scalable quantum computer along these lines.

In the light of this, we sought a more direct path to scalability. Rather than sequentially preparing and interfacing qubits, one can prepare a large-scale quantum resource state whose constituent quantum systems (such as qubits or modes) are interconnected in advance. Provided that this resource—known as a cluster state (6)—has the required structure and scale, then quantum computing can proceed by means of purely local (single-site) quantum measurements. This paradigm is known as measurement-based quantum computation (MBQC) (7, 8). The scale of the cluster state

typically determines the number of possible computational steps. Its structure—codified as a graph that describes the entanglement properties of the state—determines which logic gates can be implemented with local measurements. For example, a cluster state corresponding to multiple disjoint one-dimensional (1D) graphs (Fig. 1A) can be used to implement multistep computations, with teleportation along the length of the cluster state being analogous to time evolution along a single circuit wire. However, the absence of connections between wires makes this state incapable of generating entanglement between inputs on separate wires, and hence, this resource is insufficient for universal quantum computing. A 2D square lattice graph (Fig. 1B) possesses connectivity in two directions, allowing for time evolution through teleportation in one direction and the multi-input unitary evolution (that generates entanglement) between inputs through connections in the other direction. It enables universal quantum computing by means of local measurements and hence is a universal resource state for MBQC.

Finding a universal resource state that is experimentally feasible (so that it can be generated on a large scale) is therefore of paramount importance to the development of a universal measurement-based quantum computer. Cluster states based on bosonic modes—known as continuous-variable cluster states (8)—can be generated deterministically by using compact quantum optics experiments (9). Despite several theoretical proposals for generating universal continuous-variable cluster states [for example, (9-12)], until now the current state-of-the-art experimental demonstrations have been limited to either small-scale (few-system) cluster states (13) or to the generation of large-scale 1D cluster states, which are insufficient for multi-input MBQC (14-16). Generation of even moderately sized

2D cluster states by using discrete variables (qubits) has also never been reported.

In this work, we report the generation of a large-scale universal continuous-variable cluster state. The scalability of our experimental method stems from using a time-domain multiplexing (TDM) architecture for continuous-variable (CV) optical systems (9). Optical CV quantum information is encoded within continuous-valued quadratures  $\hat{x}_k$  and  $\hat{p}_k$  that satisfy  $[\hat{x}_j,\hat{p}_k] = ih\delta_{jk}$  and correspond to the complex electric field amplitudes of optical modes residing in temporally localized wave packets. An unlimited number of modes can be continuously and deterministically prepared from a few sources and then transformed into a continuous-variable cluster state through the repeated use of a circuit made of only a small number of optical components. Entanglement in the resulting state can be observed from correlations in quadrature values of different temporal modes. In this way, we generate and verify a universal cluster state with a 5- by 1240-site 2D square lattice structure, with the possibility of further extension along both lattice dimensions by several orders of magnitude in the near future by use of current technology.

Our method generates a continuous-variable cluster state from four squeezed light sources and a linear optical network consisting of five beam splitters and two delay lines (Fig. 1C). After single-mode squeezed states leave each optical parametric oscillator (OPO), they are converted to two-mode squeezed states by beam splitter 1 and beam splitter 2 and then a four-mode entangled state by beam splitter 3. Next, the delay lines multiplex these in time so that they form a 2D (but still disconnected) grid layout with cylindrical boundary conditions. Last, beam splitter 4 and beam splitter 5 produce additional connections, resulting in a continuous cylindrical structure (Fig. 1D) [as shown for the case in which  $N = 30$ ]. A more detailed description of this generation procedure can be found in (17), section SM2. The surface of this cylinder consists of sites (macronodes) that are arranged in a 2D square lattice whose temporal modes (micronodes) are connected in a nontrivial way (Fig. 1E). The delay between temporal modes arriving at each detector is set by the shorter delay  $\Delta t$ . The longer delay line  $N\Delta t$  controls the circumference length ( $N$  sites) of the cylinder. Therefore, our method can generate arbitrarily long 2D cluster states, and only the length of the long delay line needs to be increased to extend the circumferential dimension. One limitation on  $N$  is that  $N\Delta t$  must be below the coherence time of the light source.

Relative to the 1D case (14, 15), generating a 2D cluster state requires a more complex network of beam splitters. This is further complicated by stabilization issues and additional optical

losses that arise from requiring the longer delay line  $N\Delta t$  and adjustment issues that arise from the constraint that the length ratio of the two optical delay lines must be an integer. The former can be addressed by instead shortening the length of each temporal-mode wave packet, which allows us to make the cluster state using delay lines with shorter lengths. We achieved this by developing broadband squeezed light sources, broadband homodyne detectors, and control systems (18). With this, we reduced the width of the wave packet from  $\sim 160$  ns in (14, 15) to  $\Delta t = 40$  ns. Regarding the latter issue, the current setup was designed

so that the lengths of two optical delay lines can be easily measured and adjusted (17) while keeping the number of the optical components the same or less than that in the previous proposals (9, 10). We picked  $N = 5$  for experimental demonstration.

To implement universal CV quantum computation, we require the ability to perform arbitrary multimode Gaussian operations and at least one non-Gaussian operation (19). Although it is possible to map the structure of our 2D square lattice cluster state to the more standard square lattice [whose methodology for implementing MBQC is known (8)], such a

mapping introduces excessive noise (20). We have noticed that a similar experiment of generating a 2D cluster state has recently been reported (21), although the methodology to avoid such a mapping has not been developed for their cluster state yet. Here, we describe a more efficient method to use our cluster state without such mapping. The structure of multimode Gaussian quantum circuits that can be implemented with our resource state by means of local homodyne measurements is shown in Fig. 2A. The number of input modes  $N$  is equal to the circumference length, and each gate is implemented by means of teleportation

![](images/e58d40de670a774ec6ae88580d1b341728b4a6f4112ad06bd9ed1d4ff7d3463d.jpg)

![](images/d1f136da1b0c262f566c883ad0845eabd08ceea248ed88c45f551633a047b8b5.jpg)

![](images/0c0a437e3d9f3a4715b39dbcb78c6d0cb80c349be0fc98b4a3e307983ce2d690.jpg)  
Fig. 1. MBQC and 2D cluster state. (A and B) Abstract illustration of MBQC. (A) One-input MBQC by using 1D cluster state. (B) Universal multi-input MBQC using 2D cluster state. Each colored circle represents a mode, and each link represents quantum entanglement. (C) Schematic of our experimental setup for the 2D cluster state. OPO, optical parametric oscillator; BS, beam splitter; ODL, optical delay line;  $\Delta t$ , time interval between adjacent wave packets;  $N$ , integer corresponding to number of inputs that 2D cluster states can take in computation; HD, homodyne detector. All beam splitters are 50:50. (D and E) 2D cluster state. (D) Example for the case in which  $N = 30$ .  
(E) Zoom in of the state. The representations of states make use of the simplified graphical calculus (9). Each small node (small colored sphere) of the graph, which we call a micronode, represents a localized wave packet at each temporal index. Four micronodes at each temporal index  $k$  can be grouped into a single site (large gray sphere), called a macronode. The links and their colors represent how micronodes are entangled. The 2D cluster state has a helical graph structure, with  $N$  macronodes on every single turn of the helix. For actual experimental demonstration, we use  $N = 5$ . Full descriptions are given in (17).

along the length of the cylindrical cluster state. Further details for how to implement multimode Gaussian operations are given in (17), section SM6. Non-Gaussian operations can be implemented by replacing homodyne-C or homodyne-D with cubic-phase ancilla assisted measurement (10). When implementing an encoded qubit-level computation by means of the Gottesman-Kitaev-Preskill (GKP) error correction scheme for CV cluster states (10, 22-24), the only non-Gaussian resource required for both universal and fault-tolerant quantum computing is GKP logical  $|0\rangle$  states, which can be inserted into the cluster state at regular intervals (25), and no measurements other than homodyne measurement are required.

An  $n$ -mode Gaussian pure state  $|\psi \rangle$  can be efficiently characterized by a list of  $n$ -independent linear nullifiers, which are linear combinations of the quadrature operators that have  $|\psi \rangle$  as their mutual zero-eigenspace. Nullifiers also play an important role in verifying genuine

multipartite inseparability for experimentally generated states that can be generated from two-mode squeezed states by means of a sequence of beam splitters (10). Such states are approximately nullified by linear combinations of quadratures that are either all of position- or momentum-type. By measuring these operators, if the states are sufficiently highly squeezed, then genuine multipartite inseparability can be verified with the van Loock-Furusawa criterion.

Our state can be characterized in this way by measuring

$$
\begin{array}{l} \hat {\delta} _ {k} ^ {(x, 1)} = \hat {x} _ {k} ^ {A} + \hat {x} _ {k} ^ {B} - \frac {1}{\sqrt {2}} \left(- \hat {x} _ {k + 1} ^ {A} + \hat {x} _ {k + 1} ^ {B} + \right. \\ \left. \hat {x} _ {k + N} ^ {C} + \hat {x} _ {k + N} ^ {D}\right) \tag {1} \\ \end{array}
$$

$$
\begin{array}{l} \hat {\delta} _ {k} ^ {(p, 1)} = \hat {p} _ {k} ^ {A} + \hat {p} _ {k} ^ {B} + \frac {1}{\sqrt {2}} \left(- \hat {p} _ {k + 1} ^ {A} + \hat {p} _ {k + 1} ^ {B} + \right. \\ \left. \hat {p} _ {k + N} ^ {C} + \hat {p} _ {k + N} ^ {D}\right) \tag {2} \\ \end{array}
$$

$$
\begin{array}{l} \delta_ {k} ^ {(x, 2)} = \hat {x} _ {k} ^ {C} - \hat {x} _ {k} ^ {D} - \frac {1}{\sqrt {2}} \left(- \hat {x} _ {k + 1} ^ {A} + \hat {x} _ {k + 1} ^ {B} - \right. \\ \left. \hat {x} _ {k + N} ^ {C} - \hat {x} _ {k + N} ^ {D}\right) \tag {3} \\ \end{array}
$$

$$
\begin{array}{l} \hat {\delta} _ {k} ^ {(p, 2)} = \hat {p} _ {k} ^ {C} - \hat {p} _ {k} ^ {D} + \frac {1}{\sqrt {2}} \left(- \hat {p} _ {k + 1} ^ {A} + \hat {p} _ {k + 1} ^ {B} - \right. \\ \left. \hat {p} _ {k + N} ^ {C} - \hat {p} _ {k + N} ^ {D}\right) \tag {4} \\ \end{array}
$$

where  $\hat{x}_k^j$  and  $\hat{p}_k^j$  are quadrature operators at temporal mode index  $k$  and at spatial index  $j$ . Shown in Fig. 3 are the quadrature values and quantum correlations of quadratures corresponding to each type of nullifier of the first 50 temporal mode indices. These quadrature values are obtained by processing the time-domain electrical signal from each homodyne detector and taking appropriate linear combinations. We observed strong correlations between quadrature values from different temporal modes, which are qualitative evidences of quantum entanglement of our states. By

![](images/a2c9191738ad89472027fb1b4baf00a89fc08c617d6ec2c3617a39fab25c942d.jpg)  
Fig. 2. Quantum computation with our cluster state. (A) Equivalent quantum circuit that is implemented when our state is used. We show the case for five inputs in which 40 light modes (10 temporal mode indices) of 2D cluster states are used. The number in each box is the index of the measured temporal modes. (B and C) The circuit is composed of multiple

![](images/4ba031b91a5feeebc423d5b7dd85faa317ab85f52343baa0c767dbbe615fbf22.jpg)

![](images/40307773cc197b665c20e5a1ccc050134aecec3f8f29086205968668c72c5e9a.jpg)

![](images/2427cc94c89082be6519a54b0eefeb4953d01a4b306befd4a7fd8c611d510cea.jpg)

![](images/ef6e48b367e619056f60fbbdd3ad3e18ed88a2dde91b23ad7d957031ed66173e.jpg)  
Fig. 3. Quadrature values and four types of quadrature correlations of the first 50 temporal mode indices. (A and B) Single-shot quadrature values of  $\hat{x}_k^j$  and  $\hat{p}_k^j$  obtained by processing time-domain signals from homodyne detector-  $j$  ( $j = A, B, C, D$ ). (C to F) Correlations of quadrature values corresponding to  $\hat{\delta}_{k}^{(x,1)}$ ,  $\hat{\delta}_{k}^{(p,1)}$ ,  $\hat{\delta}_{k}^{(x,2)}$ , and  $\hat{\delta}_{k}^{(p,2)}$ , respectively. Although the quadrature values measured at each

![](images/9e347a3130bd228b63d24c477a9ce19b9cb53a98546b3605a288d71ff8665771.jpg)  
quantum teleporters: (B) one-mode operation and (C) two-mode operation. Two-mode operations can be turned off by selecting the same measurement basis for HD-A and HD-B. Classical feed-forward does not have to be implemented immediately after homodyne measurements and can be delayed to the end of the computation for Gaussian-only computations.

![](images/20b049d7616e7065086129da4b661922126af3d2e23fc02e337cf7b11ffcc46c.jpg)  
homodyne detector seemed to be just fluctuating randomly around zero, we observed four types of strong quantum correlations between six quadrature values with different temporal mode index  $k$  and spatial index  $j$ . The quadrature values are plotted by using the unit at which variance of the vacuum state is equal to 1.

![](images/f89efcfd117a43142b2b1a263a8c5580e916e69666ae51f349218cb4adaaefdd.jpg)

![](images/9272a4c623ff52be4771430d1f97db134c9bdf2713734c4962266bdb7487dd21.jpg)

![](images/2aa1e18f4c88a6218b5d15c7f83af31ba0e485dd69ee28be9dbf59681cad0bc6.jpg)  
Fig. 4. Verification of generated cluster state for 24,960 temporal modes. (A to D) Measurement results for each type of nullifier:  $\hat{\delta}_k^{(x,1)}$ ,  $\hat{\delta}_k^{(p,1)}$ ,  $\hat{\delta}_k^{(x,2)}$ , and  $\hat{\delta}_k^{(p,2)}$ , respectively. Black points indicate measured variances of shot noise, which are used as reference levels. Blue points indicate measured variances of nullifiers. Purple regions indicate regions where the variances of the nullifiers are below  $-4.5$  dB compared with shot noise, which indicate entanglement. The variances of four types of nullifiers satisfied quantum inseparability criteria up to  $k = 6240$  corresponding to  $4 \times 6240 = 24,960$  temporal modes.

![](images/62f2f8130c03fd8be745b84ddd5326f03c938a89760b495296b1c4eae4238a9b.jpg)

![](images/0930b870cf01f92140741e6b5d89b57d6d64530f43e12a87ce8fa9103b898a1f.jpg)

![](images/56bc2f8b8879ef2f06eca335232ece19d0d51f89bffed5226f967621d222e819.jpg)

applying the van Loock-Furusawa criterion, we verified the 2D entanglement structure of the state if we observed that the variances of all the nullifiers were below  $-4.5\mathrm{dB}$  compared with shot noise (17).

The measurement results for each nullifier type for each temporal mode index  $k$  are shown in Fig. 4. All nullifiers were observed to be below  $-4.5\mathrm{dB}$  for up to  $k = 6240$ . Because there are four micronodes at each temporal index  $k$ , the states we verified possess 24,960 micronodes. Because one macronode (or one site) consists of four micronodes and we used  $N = 5$ , the structure of the state we verified is a 5- by 1248-site 2D square lattice with cylindrical boundary conditions. The means of the variances for each type of nullifier are  $-4.82 \pm 0.06\mathrm{dB}$ ,  $-5.34 \pm 0.06\mathrm{dB}$ ,  $-4.81 \pm 0.06\mathrm{dB}$ , and  $-4.93 \pm 0.06\mathrm{dB}$ , respectively. These values are limited by the original squeezing level from the squeezed light sources, optical losses and fluctuations in the optical system, and electrical noises from homodyne detectors and are in good agreement with the experimental parameters. Statistical errors are the main contributors to the error bars, which can be arbitrarily decreased by increasing the number of events used for calculating the nullifiers. There are no corrections for experimental imperfections, and the nullifiers do not degrade with the increasing  $k$ , suggesting that  $k$  can be arbitrarily large.

Thus, we have proposed and verified the generation of a universal resource state for MBQC. Using this cluster state for large-scale MBQC requires a few additional steps. First, because the delay line ratio  $N = 5$  sets the number of inputs in the effective quantum circuit, this must be increased. Second, because finite squeezing level sets the noise level when cluster states are used in MBQC (20), the squeezing level must be improved to be above the fault-tolerant threshold (22). It is possible to increase the delay line ratio by increasing the bandwidth of the squeezed light source, which

reduces wave packet size, and development of a low-loss optical delay line. Even with currently available technology (26, 27), we expect a number of the input modes on the order of  $10^{4}$  to be achievable, and if we consider the ultimate limit set by coherence time of the light source, the number of the input modes could be potentially increased to  $\sim 10^{10}$  modes by use of a narrow-linewidth laser (28). Regarding improvement of the squeezing level to above the fault-tolerant threshold, the squeezing level of our cluster state can potentially reach  $-15\mathrm{dB}$  with the state-of-the-art squeezed light source (29), which begins to be within reach of the known thresholds (-15 to -17 dB) for fault tolerance in this architecture by using particular quantum-error-correcting codes (30). Moreover, it has recently been shown that it is possible to further relax the threshold to about  $-10\mathrm{dB}$  with analog quantum error correction and postselection (23). Therefore, we believe that demonstration of our cluster state provides a feasible way toward realization of a practical quantum computer.

# REFERENCES AND NOTES

1. M. A. Nielsen, I. L. Chuang, Quantum Computation and Quantum Information (Cambridge Univ. Press, 2000).  
2. J. M. Gambetta, J. M. Chow, M. Steffen, npj Quantum Inf. 3, 2 (2017).  
3. K. R. Brown, J. Kim, C. Monroe, npj Quantum Inf. 2, 16034 (2016).  
4. F. A. Zwanenburg et al., Rev. Mod. Phys. 85, 961-1019 (2013).  
5. M. Veldhorst, H. G. J. Enink, C. H. Yang, A. S. Dzurak, Nat. Commun. 8, 1766 (2017).  
6. H. J. Briegel, R. Raussendorf, Phys. Rev. Lett. 86, 910-913 (2001).  
7. R. Raussendorf, H. J. Briegel, Phys. Rev. Lett. 86, 5188-5191 (2001).  
8. N. C. Menicucci et al., Phys. Rev. Lett. 97, 110501 (2006).  
9. N. C. Menicucci, Phys. Rev. A 83, 062314 (2011).  
10. R. N. Alexander, S. Yokoyama, A. Furusawa, N. C. Menicucci, Phys. Rev. A 97, 032302 (2018).  
11. R. N. Alexander et al., Phys. Rev. A 94, 032327 (2016).  
12. A. L. Grimsmo, A. Blais, npj Quantum Inf. 3, 20 (2017).  
13. M. Yukawa, R. Ukai, P. van Loock, A. Furusawa, Phys. Rev. A 78, 012301 (2008).  
14. J. Yoshikawa et al., APL Photonics 1, 060801 (2016).  
15. S. Yokoyama et al., Nat. Photonics 7, 982-986 (2013).  
16. M. Chen, N. C. Menicucci, O. Pfister, Phys. Rev. Lett. 112, 120505 (2014).  
17. Materials and methods are available as supplementary materials.

18. Y. Shiozawa et al., Phys. Rev. A 98, 052311 (2018).  
19. S. Lloyd, S. L. Braunstein, Phys. Rev. Lett. 82, 1784-1787 (1999).  
20. R. N. Alexander, S. C. Armstrong, R. Ukai, N. C. Menicucci, Phys. Rev. A 90, 062324 (2014).  
21. M. V. Larsen, X. Guo, C. R. Breum, J. S. Neergaard-Nielsen, U. L. Andersen, Science 366, 369-372 (2019).  
22. N. C. Menicucci, Phys. Rev. Lett. 112, 120504 (2014).  
23. K. Fukui, A. Tomita, A. Okamoto, K. Fujii, Phys. Rev. X 8, 021054 (2018).  
24. D. Gottesman, A. Kitaev, J. Preskill, Phys. Rev. A 64, 012310 (2001).  
25. B. Q. Baragiola, G. Pantaleoni, R. N. Alexander, A. Karanjai, N. C. Menicucci, All-Gaussian universality and fault tolerance with the Gottesman-Kitaev-Preskill code. arXiv:1903.00012 [quant-ph] (2019).  
26. S. Ast, M. Mehmet, R. Schnabel, Opt. Express 21, 13572-13579 (2013).  
27. J. Aasi et al., Nat. Photonics 7, 613-619 (2013).  
28. L. Wu et al., Sci. Rep. 6, 24969 (2016).  
29. H. Vahlbruch, M. Mehmet, K. Danzmann, R. Schnabel, Phys. Rev. Lett. 117, 110801 (2016).  
30. B. W. Walshe, L. J. Mensen, B. Q. Baragiola, N. C. Mencucci, Phys. Rev. A 100, 010301 (2019).

# ACKNOWLEDGMENTS

Funding: This work was partly supported by the Japan Society for the Promotion of Science (JSPS) KAKENHI (grant 18H05207), UTokyo Foundation, donations from Nichia Corporation, and the Australian Research Council Centre of Excellence for Quantum Computation and Communication Technology (project CE170100012). W.A. acknowledges financial support from JSPS. Y.S. acknowledges financial support from the Advanced Leading Graduate Course for Photon Science (ALPS). B.C. acknowledges financial support from the Program of Excellence in Photon Science (XPS). R.N.A. is supported by National Science Foundation grant PHY-1630114. Author contributions: W.A. and Y.S. planned and designed the experiment. S.Y., S.T., J.Y., H.Y., and A.F. supervised this project. R.N.A., N.C.M., W.A., and S.Y. formulated the theory for this experiment. Y.S. and W.A. designed the actual optical system. W.A. conceived the method for stabilizing the experimental system and performed analysis necessary for experimental realization. W.A., Y.S., and H.E. built the experimental system. W.A., Y.S., and B.C. conducted the experiment and obtained the experimental data. Y.S., B.C., W.A., and S.Y. performed the data analysis. W.A. wrote the manuscript with assistance from Y.S., B.C., S.Y., R.N.A., S.T., J.Y., N.C.M., H.Y., and A.F. Competing financial interests: The authors declare no competing financial interests. Data and materials availability: All data are available in the manuscript or the supplementary materials.

# SUPPLEMENTARY MATERIALS

science.sciencemag.org/content/366/6463/373/suppl/DC1 Materials and Methods

Supplementary Text

Figs. S1 to S11

References (31-37)

4 June 2019; accepted 25 September 2019

10.1126/science.aay2645

# Generation of time-domain-multiplexed two-dimensional cluster state

Warit Asavanant, Yu Shiozawa, Shota Yokoyama, Baramee Charoensombutamon, Hiroki Emura, Rafael N. Alexander, Shuntaro Takeda, Jun-ichi Yoshikawa, Nicolas C. Menicucci, Hidehiro Yonezawa and Akira Furusawa

Science 366 (6463), 373-376.

DOI: 10.1126/science.aay2645

# Generating large-scale cluster states

The development of a practical quantum computer requires universality, scalability, and fault tolerance. Although much progress is being made in circuit platforms in which arrays of qubits are addressed and manipulated individually, scale-up of such systems is experimentally challenging. Asavanant et al. and Larsen et al. explore an alternative route: measurement-based quantum computation, which is a platform based on the generation of large-scale cluster states. As these are optically prepared and easier to handle (one simply performs local measurements on each individual component of the cluster state), such a platform is readily scalable and fault tolerant. The topology of the cluster state ensures that the approach meets the requirements for quantum computation.

Science, this issue p. 373, p. 369

# ARTICLE TOOLS

http://science.sciencemag.org/content/366/6463/373

# SUPPLEMENTARY MATERIALS

http://science.sciencemag.org/content/suppl/2019/10/16/366.6463.373.DC1

# REFERENCES

This article cites 36 articles, 1 of which you can access for free http://science.sciencemag.org/content/366/6463/373#BIBL

# PERMISSIONS

http://www.sciencemag.org/help/reprints-and-permissions

Use of this article is subject to the Terms of Service