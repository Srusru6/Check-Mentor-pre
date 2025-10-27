# Surface Code Quantum Communication

Austin G. Fowler, $^{1}$  David S. Wang, $^{1}$  Charles D. Hill, $^{1}$  Thaddeus D. Ladd, $^{2,3,*}$

Rodney Van Meter, $^{4}$  and Lloyd C. L. Hollenberg $^{1}$

<sup>1</sup>Centre for Quantum Computer Technology, School of Physics, University of Melbourne, Parkville, Victoria 3010, Australia

$^{2}$ National Institute of Informatics, 2-1-2 Hitotsubashi, Chiyoda-ku, Tokyo 101-8430, Japan

<sup>3</sup>Edward L. Ginzton Laboratory, Stanford University, Stanford, California, 94305-4088, USA

$^{4}$ Faculty of Environment and Information Studies, Keio University, Fujisawa 252-0882, Japan

(Received 4 February 2010; published 6 May 2010)

Quantum communication typically involves a linear chain of repeater stations, each capable of reliable local quantum computation and connected to their nearest neighbors by unreliable communication links. The communication rate of existing protocols is low as two-way classical communication is used. By using a surface code across the repeater chain and generating Bell pairs between neighboring stations with probability of heralded success greater than 0.65 and fidelity greater than 0.96, we show that two-way communication can be avoided and quantum information can be sent over arbitrary distances with arbitrarily low error at a rate limited only by the local gate speed. This is achieved by using the unreliable Bell pairs to measure nonlocal stabilizers and feeding heralded failure information into post-transmission error correction. Our scheme also applies when the probability of heralded success is arbitrarily low.

DOI: 10.1103/PhysRevLett.104.180503

PACS numbers: 03.67.Hk, 03.67.Pp

Long-range communication of quantum states is difficult as such states cannot be copied [1,2]. Current research into long-range quantum communication focuses on quantum repeaters [3] making use of entanglement purification [4] and entanglement swapping [5]. Entanglement purification requires slow two-way classical communication, resulting in the quantum communication rate decreasing polynomially with distance. Furthermore, the communication error rate  $p_c$  is at best comparable to the error rate  $p_g$  of gates within repeaters. If qubits have a finite coherence time, requesting a constant  $p_c$  as the distance increases results in a finite maximum communication distance. Arbitrarily rapid and reliable communication over arbitrary distances is not possible using only entanglement purification and swapping.

Initial work incorporating error correction into quantum communication resulted in non-fault-tolerant schemes [6,7] capable of correcting small numbers of errors. Recently, the first steps towards fault-tolerant quantum communication were taken [8]; however, entanglement purification was still used between neighboring quantum repeaters, fundamentally limiting the communication rate to hundreds of logical qubits per second. A quantum communication protocol requiring very little two-way classical communication has been developed concurrent with this work [9].

We show that, using surface code quantum error correction (QEC) [10-12], two-way classical communication can be avoided provided we can create Bell pairs between neighboring stations with heralded success probability  $S_B \gtrsim 0.65$  and fidelity  $F \gtrsim 0.96$ . This means communication can proceed at a rate independent of the classical communication time between repeater stations. Given local quantum gates with  $p_g \ll 0.75\%$ , we show how to

communicate logical qubits over arbitrary distances with arbitrarily low  $p_c$  at a rate limited only by the local gate speed. The number of qubits per repeater increases only logarithmically and the quantum communication rate decreases only logarithmically with communication distance. If the probability of heralded success is less than 0.65 and Bell pairs between neighboring stations with fidelity no less than 0.92 are generated only every  $T_B$  seconds, we show that the logarithmic resource scaling remains and the communication rate through  $N$  links is proportional to  $[T_B\log^2 (N / p_c)]^{-1}$ .

To describe our quantum communication protocol, we must describe surface codes and this in turn requires the notion of stabilizers [13]. A stabilizer of  $|\Psi \rangle$  is an operator  $M$  such that  $M|\Psi \rangle = |\Psi \rangle$ . For example,  $Z|0\rangle = |0\rangle$ . Given any set of commuting operators  $\{M_i\}$ , a state  $|\Psi \rangle$  exists stabilized by  $\{M_i\}$ .

Surface codes exist on lattices of the form shown in Fig. 1. Data qubits are represented by open circles. We define a set of commuting operators on data qubits by associating ZZZZ (XXXX) with each face (vertex). If the  $|\Psi \rangle$  stabilized by these operators suffers errors, becoming  $|\bar{\Psi}\rangle$ , then local to these errors we obtain equations of the form  $M|\bar{\Psi}\rangle = -|\bar{\Psi}\rangle$ . Measuring whether the qubits are in the  $+1$  or  $-1$  eigenstate of each stabilizer thus gives us information about the errors in the lattice. Measuring a stabilizer requires a sequence of six gates. This information can be used to reliably correct the errors provided the error rates of initialization, CNOT, measurement, and memory, which here we take to be equal at rate  $p_g$ , are all less than approximately  $0.75\%$  [11,12,14]. Logical operators  $X_L$  ( $Z_L$ ) are chains of single-qubit  $X$  ( $Z$ ) operators that commute with every  $Z$  ( $X$ ) stabilizer and link the top (left) boundary to the bottom (right). The distance  $d$  of the code

![](images/379f31586c1237173c01f85bc9854f3ad6a4201eceba9d35ec662703de95a2fa.jpg)  
FIG. 1 (color online). A surface code logical qubit. Stabilizers ZZZZ (XXXX) are associated with the data qubits (open circles) around each face (vertex). Syndrome qubits (dots) measure stabilizers using the indicated sequences of gates. Logical operators  $Z_{L}$ ,  $X_{L}$  connect opposing boundaries.

is the number of single-qubit operators in the shortest logical operator.

We now describe our communication protocol, initially restricting ourselves to moving a logical qubit from the left end to the right end of a single monolithic array of qubits with the ability to perform local gates. Given an arbitrary surface code logical qubit  $|\Psi_L\rangle$  at the left end of the array, an uninitialized region of qubits  $|\Psi \rangle$  in the middle and a surface code logical qubit  $|0_L\rangle$  at the right end,  $|\Psi_L\rangle$  can be fault-tolerantly teleported to the location of  $|0_L\rangle$  by the following procedure. First, the uninitialized region is initialized [Fig. 2(a)]. Second, the syndrome qubits across the entire lattice are interacted with their neighbors [Fig. 2(b)]. This begins the process of increasing the size of the logical qubit to cover the entire lattice. Third, the measurement pattern shown in Fig. 2(c) completes one round of stabilizer measurement. The interaction pattern of Fig. 2(b) is executed a total of  $d$  times, interleaved with the measurement pattern of Fig. 2(c). This process is standard surface code QEC. During the rounds of error correction, the logical qubit information becomes reliably distributed across the entire lattice. Finally, after the  $d$ th round of interaction, the measurement pattern shown in Fig. 2(d) is applied. These measurements effectively cut off a large piece of the logical qubit without revealing information about the value being transmitted, faithfully leaving the logical qubit in the unmeasured region.

All measurement results are simply sent to the destination end of the lattice, not processed during transmission. The final round of measurements prepares the lattice for the transmission of the next logical qubit. Assuming each interacting quantum gate takes  $T_{g}$  seconds and each measurement  $T_{m}$  seconds, a logical qubit can be transmitted every  $(4T_{g} + T_{m})d$  seconds. The scaling of  $d$  and values required for practical communication will be discussed

![](images/f226bc1e1d61cecae04f7e0e87c00cde45fd13df342f7d710e2892a18da3b649.jpg)

![](images/e329fcfbea7db33abeb09342a79df6b9702169bd1d57eec8db41f8f8ef2244fb.jpg)

![](images/3ae4b904d48ade4150e7f825b16d8834c9d35308ef536b2bc791f1783682e43c.jpg)

![](images/8db58e081ff6eb34856df6064a20e92577b2b09e244d2a2c2737ff6008bd5696.jpg)  
FIG. 2. Monolithic surface code quantum communication. (a) Monolithic lattice of qubits with source logical qubit  $|\Psi_L\rangle$ , initial measurement pattern for the intermediate region, and destination area initialized to  $|0_L\rangle$ . (b) Circuits used in parallel to prepare for stabilizer measurement. Numbers indicate the timing of gates. (c) Intermediate stabilizer measurements. (d) Final stabilizer measurement and communicated state.

later after the full communication scheme has been described.

The processing of measurement results related to  $X$  and  $Z$  stabilizers occurs independently. Errors result in stabilizer measurements changing. Error chains change stabilizer measurements only at the end points. A good approximation of the most likely pattern of errors corresponding to a given set of stabilizer measurement changes is one in which every change is connected by a chain of errors to another change or lattice boundary such that the total number of errors is a minimum. A classical algorithm, the minimum weight perfect matching algorithm [15], can find such a pattern efficiently, in time growing polylogarithmically with the volume of the lattice when parallel processing is used [16,17]. Error correction fails when the corrections actually create error chains connecting pairs of opposing boundaries. With careful calculation of the distance between changes, a minimum of  $\lfloor (d + 1) / 2 \rfloor$  errors must occur before failure is possible, implying  $p_c$  decreases exponentially with  $d$ .

When communicating over a large physical distance, the fundamental entanglement resource is expected to be Bell

![](images/cfafe0b6baeb1d19a009f826edabd10ef6346523b765499d331c33dda376f44c.jpg)  
FIG. 3. Repeater-based surface code quantum communication. The qubit pattern in each quantum repeater (ovals) is for  $d = 3$ . The pattern width is independent of  $d$ .

pairs created over fiber links kilometers in length. The monolithic lattice described above can be broken into pieces connected by Bell pairs as shown in Fig. 3. Stabilizers spanning the communication link can be measured using the approach shown in Fig. 4. We temporarily ignore heralded failure to entangle, which is discussed below. The left half of each Bell pair can be measured before the right half even reaches its destination. The rate of the scheme thus remains unchanged—one logical qubit every  $(4T_{g} + T_{m})d$  seconds. Latency is, however, introduced as the qubits in any given repeater station are not initialized until the first photons arrive from the left. For many ranges of parameters, a given repeater will have finished working and sending photons before the next repeater receives its first photons.

The scheme's maximum tolerable Bell pair error rate is of critical importance. Let us temporarily assume that all gates within repeater nodes are perfect and Bell pairs are subject to depolarizing errors. We shall continue to ignore heralded failure to entangle for the moment. A probability  $p_B$  of depolarizing error on a Bell pair means that the errors  $IX, IY, IZ, XI, XX, XY, XZ, YI, YX, YY, YZ, ZI, ZX, ZY, ZZ$  each occur with probability  $p_B / 15$ . Using the Bell pair stabilizers  $XX$  and  $ZZ$ , these errors are equivalent to  $II$  with probability  $p_B / 5$  and  $IX, IY, IZ$  with equal probability  $4p_B / 15$ .

After correction, nontrivial combinations of  $X(Z)$  errors form a chain that runs from the top spatial (temporal) boundary to the bottom spatial (temporal) boundary. Given this symmetry, and the fact that the different types of errors are processed independently, we focus on  $IX$

![](images/bc92da8758ad9511fd18ed00558204936d248a10c917e7ea95a07d5ef32518c8.jpg)  
FIG. 4. If the probability of heralded success is sufficiently high, qubit  $A$  can be interacted with its neighboring data qubits and measured before the entangling pulse or photon even reaches its destination. Error correction takes care of heralded failures, including loss during transmission.

errors, which occur on any given Bell pair with probability  $p_X = 8p_B / 15$ . Referring to the Bell pairs numbered 1 to  $2d - 1$  in Fig. 3,  $IX$  errors on odd pairs induce an  $X$  error on the data qubit to their left whereas on even pairs the result is an incorrect stabilizer measurement.

These errors can be visualized as the bonds of a  $d \times t$  2D square lattice. The error rate  $p_X$  is too high when, after correction, the probability of having a chain of errors along the  $d$  dimension increases with  $d$ . For  $t = 1$ , we have a repetition code, implying  $p_X < 0.5$  is correctable. For  $t = d$ , we have a surface code with perfect syndrome measurement implying  $p_X \lesssim 0.1$  [12]. The equivalent values of  $p_B$  are 15/16 and approximately 0.2.

We simulated a pair of repeater nodes with perfect gates and an independent stochastic error model of depolarized Bell pairs for verification (Fig. 5). Note the expected crossover at  $p_B = 15 / 16 \sim 0.94$ . Significant growth of the time to failure with  $d$  occurs for  $p_B \lesssim 0.2$ , as expected. Rapid growth occurs for  $p_B \sim 0.1$ , equivalent to a fidelity  $F$  of the entangled state  $\rho$  with respect to the desired Bell state  $|\Phi^{+}\rangle$  of 0.92 since  $F = \langle \Phi^{+}|\rho |\Phi^{+}\rangle = 1 - 4p / 5$  for depolarized Bell pairs.

Loss during transmission can be modeled as measurement in an unknown basis. Loss is easier to tolerate than depolarizing noise as the failure to measure the transmitted pulse or photon gives the location of the error. This can be seen in the simulation results of Fig. 6, which shows efficient handling of  $40\% - 45\%$  loss. Note that no code can handle more than  $50\%$  loss as this would violate the no-cloning theorem [1,2].

The probability of logical error after  $d$  stabilizer measurements,  $p_{\mathrm{link}}$ , is shown in Fig. 7 versus  $p_B$  and loss  $p_{\mathrm{loss}}$ . For  $35\%$  loss and  $5\%$  error  $(F = 0.96)$ , increasing  $d$  by 30 decreases  $p_{\mathrm{link}}$  by a factor of 10. The exponential decrease of  $p_{\mathrm{link}}$  with  $d$  implies the probability of communication error  $p_c$  through  $N$  links decreases exponentially with  $d$ . Doubling  $N$  requires halving  $p_{\mathrm{link}}$ , so  $d$  increases logarithmically as  $N$  increases.

![](images/53929823a94204c67aee769e5664abc5bfbd23b1c3f63afd835c0b85c8d22d76.jpg)  
FIG. 5 (color online). Average number of error correction rounds before logical failure versus Bell pair error rate  $p_B$  and code distance. Inset: Magnification of high  $p_B$  region.

![](images/f3799409d8f339a5154bb8bc1fe4a390bdcf9aecc3c6cb9fc4fdc820aba4c774.jpg)  
FIG. 6 (color online). Average number of error correction rounds before logical failure versus loss and code distance.

mically with  $N$  for fixed  $p_c$ . In brief,  $d = O(\log (N / p_c))$ . Sending data through  $10^{4}$  repeaters with an overall error of  $10^{-6}$  error would require  $d \sim 300$ , corresponding to of order  $10^{3}$  qubits per repeater. Each repeater takes time  $d(4T_g + T_m) / (1 - p_{\mathrm{loss}})$  to send a logical qubit. Long-range, high fidelity MHz communication can thus be achieved provided  $300(4T_g + T_m) / 0.65 \sim 1~\mu \mathrm{s}$ , meaning  $\sim 2$  ns gates.

Permitting repeaters to have a nonzero local gate error rate  $p_{g}$  will only have significant impact if it is close to the threshold error rate of approximately  $p_{g}^{\mathrm{th}} = 0.75\%$  [14]. An error rate 1 or 2 orders of magnitude below this will not significantly change the above results.

To summarize, provided the Bell pair depolarizing error rate is less than approximately  $10\%$  ( $F \gtrsim 0.92$ ), utilizing surface code QEC enables the practical fault-tolerant quantum communication of logical qubits over an arbitrary number of links  $N$  with arbitrarily low overall communication error rate  $p_c$  given  $O(\log (N / p_c))$  qubits per repeater. If the rate of loss is high, the communication rate is inversely proportional to the time  $T_B$  required to suc

![](images/2eb4c30095842e68e5087a0a907d8e5ac6ec1b34ab429f8b1406667db819fffa.jpg)  
FIG. 7 (color online). Probability of logical error per link for a variety of loss and Bell error rates.

cessfully create a single Bell pair and the number of Bell pairs used to link neighboring repeaters which is itself proportional to the square of the number of qubits per repeater giving a rate of  $\left[T_B\log^2 (N / p_c)\right]^{-1}$ . If the loss is below approximately  $35\%$  and  $F\gtrsim 0.96$ , only one-way classical communication is required and of order  $10^{3}$  qubits per repeater and nanosecond gates enables one to send logical qubits at a MHz rate with  $10^{-6}$  error through  $10^{4}$  links—sufficient in principle to reach the opposite side of the planet.

We acknowledge helpful discussions with Bill Munro, Simon Devitt, Ashley Stephens, and Sean Barrett. A. G. F., D. S. W., C. D. H., L. L. C. H. acknowledge support from the Australian Research Council, the Australian Government, and the U.S. National Security Agency (NSA) and the Army Research Office (ARO) under Contract No. W911NF-08-1-0527. R. V. acknowledges support from JSPS. T. D. L. was partially supported by the National Science Foundation CCF-0829694, MEXT, and NICT.

*Present address: HRL Laboratories, LLC, 3011 Malibu Canyon Road, Malibu, CA 90265, USA.  
[1] D. Dieks, Phys. Lett. A 92, 271 (1982).  
[2] W.K. Wootters and W.H. Zurek, Nature (London) 299, 802 (1982).  
[3] H.-J. Briegel, W. Dür, J. I. Cirac, and P. Zoller, Phys. Rev. Lett. 81, 5932 (1998).  
[4] C.H. Bennett et al., Phys. Rev. Lett. 76, 722 (1996).  
[5] M. Zukowski, A. Zeilinger, M. A. Horne, and A. K. Ekert, Phys. Rev. Lett. 71, 4287 (1993).  
[6] S. Perseguers, L. Jiang, N. Schuch, F. Verstraete, M.D. Lukin, J.I. Cirac, and K.G.H. Vollbrecht, Phys. Rev. A 78, 062324 (2008).  
[7] S. Perseguers, Phys. Rev. A 81, 012310 (2010).  
[8] L. Jiang, J.M. Taylor, K. Nemoto, W.J. Munro, R. Van Meter, and M.D. Lukin, Phys. Rev. A 79, 032325 (2009).  
[9] W.J. Munro, K.A. Harrison, A. Stephens, S. Devitt, and K. Nemoto, arXiv:0910.4038.  
[10] S.B. Bravyi and A.Y. Kitaev, arXiv:quant-ph/9811052.  
[11] A.G. Fowler, A.M. Stephens, and P. Groszkowski, Phys. Rev. A 80, 052312 (2009).  
[12] D. S. Wang, A. G. Fowler, A. M. Stephens, and L. C. L. Hollenberg, Quantum Inf. Comput. 10, 456 (2010).  
[13] D. Gottesman, Ph.D. thesis, Caltech, 1997, arXiv:quant-ph/9705052.  
[14] R. Raussendorf and J. Harrington, Phys. Rev. Lett. 98, 190504 (2007).  
[15] W. Cook and A. Rohe, INFORMS J. Comput. 11, 138 (1999).  
[16] S.J. Devitt, A.G. Fowler, T. Tilma, W.J. Munro, and K. Nemoto, arXiv:0906.0415 [Int. J. Quantum. Inform. (to be published)].  
[17] G. Duclos-Cianci and D. Poulin, Phys. Rev. Lett. 104, 050504 (2010).