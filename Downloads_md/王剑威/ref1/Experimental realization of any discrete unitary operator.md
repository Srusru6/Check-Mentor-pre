# Experimental Realization of Any Discrete Unitary Operator

Michael Reck and Anton Zeilinger  
Institut für Experimentalphysik, Universität Innsbruck, Technikerstrasse 25, A-6020 Innsbruck, Austria

Herbert J. Bernstein and Philip Bertani  
Hampshire College and ISIS, Amherst, Massachusetts 01002  
(Received 11 February 1994)

An algorithmic proof that any discrete finite-dimensional unitary operator can be constructed in the laboratory using optical devices is given. Our recursive algorithm factorizes any  $N \times N$  unitary matrix into a sequence of two-dimensional beam splitter transformations. The experiment is built from the corresponding devices. This also permits the measurement of the observable corresponding to any discrete Hermitian matrix. Thus optical experiments with any type of radiation (photons, atoms, etc.) exploring higher-dimensional discrete quantum systems become feasible.

PACS numbers: 42.50.Wm, 03.65.Bz, 42.79.Sz, 42.79.Ta

While it is evident that any lossless experimental setup can be described by a unitary operator, the inverse problem, i.e., the question as to whether an experimental setup exists for any given unitary operator, has been a hitherto unsettled question. In the present Letter, we present a surprisingly simple but general algorithm for the design of an experimental realization of any  $N \times N$  unitary matrix in the laboratory. This, to our knowledge, is the first constructive proof that any discrete unitary operator can be given operational meaning in the real world.

Our experimental realization transforms the  $N$  input states into the  $N$  output states using an arrangement of beam splitters, phase shifters, and mirrors. It should be mentioned that it does not matter what kind of field such an optical multiport is acting upon. We choose photons here for convenience of discussion and because of the fact that high power sources, even for entangled radiation, are available today. Yet we note that it would be equally possible to realize multiports for electrons, neutrons, atoms, or any other type of radiation.

Before going into the details of our proof, we mention that our observation makes a wealth of new experiments possible. Such multistate devices will be used in future quantum computation and quantum information processing schemes.  $N$ -state systems of two and more particles permit the study of novel Einstein-Podolsky-Rosen correlations in higher dimensions [1], which will find practical applications in quantum cryptography using more than two states [2] and in quantum "teleportation" [3]. Going beyond the simple U(2) interferometer allows the construction of optical experiments equivalent to generalized Stern-Gerlach experiments [4] that can be used to study nontrivial properties of spin-one systems [5] and of higher-dimensional spin systems. A multiport can also be used to simulate general spin systems in Bell inequality experiments [6].

Experiments with entangled photons in multidimensional Hilbert spaces have become possible using multi-

port beam splitters [7]. Such higher-dimensional discrete quantum systems show effects which are not observable in simple two-dimensional systems and which are of qualitatively completely different nature as has been shown by Gleason, Bell, Kochen, and Specker [8]. Finally, multiports will generalize the apparatus of the fine experiment by Noh, Fougères, and Mandel [9] to higher dimensions. Thus multiports open the definition and exploration of generalized multimode intensities (including quadratures,  $Q$  functions, and  $P$  functions) [10,11] and phases to experimental investigation.

Independent of and important beyond all practical applications, our observation addresses an old fundamental question in the theory of measurement [12]. This is the question of whether or not an experiment measuring the variable corresponding to any arbitrary Hermitian operator exists. We answer that an analog embodiment using particle beams (photons, neutrons, atoms, etc.) does exist for every Hermitian operator in a finite-dimensional Hilbert space.

The experimental realization of the most general element of  $\mathbf{U}(2)$  is well known [13,14]. The matrix of a lossless beam splitter with a phase shifter at one output port will be used in our proof. It transforms the input state with modes  $(k_{1},k_{2})$  into the output state with modes  $(k_1',k_2')$ ,

$$
\left( \begin{array}{c} k _ {1} ^ {\prime} \\ k _ {2} ^ {\prime} \end{array} \right) = \left( \begin{array}{c c} e ^ {\imath \phi} \sin \omega & e ^ {\imath \phi} \cos \omega \\ \cos \omega & - \sin \omega \end{array} \right) \left( \begin{array}{c} k _ {1} \\ k _ {2} \end{array} \right). \tag {1}
$$

The parameter  $\omega$  describes the reflectivity  $(\sqrt{R} = \sin \omega)$  and transmittance  $(\sqrt{T} = \cos \omega)$  of the beam splitter. The parameter  $\phi$  can be realized as an external phase shifter after the beam splitter. Phases at the input ports can be chosen so that the beam splitter matrix performs any transformation in U(2) [15,16]. A beam splitter with variable reflectivity can be substituted by a Mach-Zehnder interferometer using symmetric 50:50 beam splitters (see Fig. 1).

We now come to our constructive proof. The most

![](images/d53de931c05c776b17aef1a1b3664f163a5e7a2ee911d8ccfe1f4348d4b47091.jpg)  
FIG. 1. A Mach-Zehnder interferometer can be used instead of a variable reflectivity beam splitter as the basic building block of any  $N \times N$  unitary matrix. On the left is one experimental realization of the device using two 50:50 beam splitters, two mirrors, and two phase shifters. The Mach-Zehnder interferometer can be represented by the abstract four-port device on the right. Two parameters  $(\phi, \omega)$  of the transformation  $T$  are set in the device.

![](images/9aba296948c572b9e178f3092879ac7d3a07bccac4fe241df8c90f12356f3f76.jpg)

important observation is that one can set up an experiment equivalent to any  $U(N)$  matrix by using these beam splitter devices such that successive  $\mathrm{U}(2)$  transformations are performed on two-dimensional subspaces of the full  $N$ -dimensional Hilbert space.

The product of matrices is equivalent to setting up experimental devices in sequence. Finding an optical experiment belonging to an arbitrary unitary matrix is therefore completely equivalent to factorizing the unitary matrix into a product of block matrices containing only beam splitter matrices with appropriate phase shifts as defined in Eq. (1). We define a matrix  $T_{pq}$  which is an  $N$ -dimensional identity matrix with the elements  $I_{pp}, I_{pq}, I_{qp}$ , and  $I_{qq}$  replaced by the corresponding beam splitter matrix elements. This matrix performs a unitary transformation on a two-dimensional subspace of the  $N$ -dimensional Hilbert space leaving an  $(N - 2)$ -dimensional subspace unchanged [17]. It can be used to successively make all off-diagonal elements of the given  $N \times N$  unitary matrix zero, a method similar to Gaussian elimination.

The unitary matrix  $U(N)$  is multiplied from the right with a succession of two-dimensional unitary matrices  $T_{Nq}(\omega_{Nq},\phi_{Nq})$  for  $q = N - 1,\ldots ,1$ . The experiment is built up by successively attaching the corresponding beam splitter devices to ports  $N$  and  $q$ . Once all elements of the last row except the one on the diagonal are zero, this row will not be affected by later transformations. Since all transformations are unitary, the last column will then also contain only zeros except on the diagonal:

$$
U (N) \cdot T _ {N, N - 1} \cdot T _ {N, N - 2} \dots T _ {N, 1} = \left( \begin{array}{c c} \framebox {U (N - 1)} & 0 \\ 0 & e ^ {i \alpha} \end{array} \right). \tag {2}
$$

The effective dimension of the matrix  $U$  is thus reduced to  $N - 1$ .

This sequence of transformations can also be viewed as the rotation of an  $N$ -dimensional vector, the last row

(or column) of  $U(N)$ , in an  $N$ -dimensional vector space. These transformations are therefore the experimental realization of a generalized rotation in  $N$  dimensions:

$$
R (N) = T _ {N, N - 1} \dots T _ {N, 1}. \tag {3}
$$

This provides an alternative view of our algorithm. The most general unitary matrix  $U(N)$  can be written as a "stack" of  $N$  orthonormal row vectors in an  $N$ -dimensional Hilbert space:

$$
U (N) = \left( \begin{array}{c} \langle 1 | \\ \langle 2 | \\ \vdots \\ \langle N | \end{array} \right). \tag {4}
$$

The matrix  $R(N)$  "rotates" a unit row vector in  $N$  dimensions into a general  $N$ -dimensional row vector.

$$
\left( \begin{array}{c} 0 \\ 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{array} \right) ^ {T} \cdot R (N) ^ {- 1} = \left( \begin{array}{c} + e ^ {- i \phi_ {1}} \cos \omega_ {1} \\ - e ^ {- i \phi_ {2}} \cos \omega_ {2} \sin \omega_ {1} \\ + e ^ {- i \phi_ {3}} \cos \omega_ {3} \sin \omega_ {2} \sin \omega_ {1} \\ \vdots \\ \mp e ^ {- i \phi_ {N - 1}} \cos \omega_ {N - 1} \dots \sin \omega_ {1} \\ \pm \sin \omega_ {N - 1} \sin \omega_ {N - 2} \dots \sin \omega_ {1} \end{array} \right) ^ {T}. \tag {5}
$$

The parameters  $\omega_{i}$  and  $\phi_{i}$  define general spherical coordinates in  $N$  dimensions. These general coordinates can thus be implemented in an optical experiment using phase shifters and beam splitters.

The sequence of beam splitter transformations or rotations can be applied recursively to the matrix with reduced dimensions. We note that a beam splitter is not necessary if an element already happens to be zero. After the final beam splitter transformation one obtains a diagonal matrix with elements of modulus 1. By attaching appropriate phase shifters, i.e., multiplying with a diagonal matrix  $D$  with elements of modulus 1, we can make the resulting matrix equal to the identity,

$$
U (N) \cdot T _ {N, N - 1} \cdot T _ {N, N - 2} \dots T _ {2, 1} \cdot D = I (N). \tag {6}
$$

The experimental setup thus built of beam splitters and phase shifters is equivalent to the inverse of the original  $N \times N$  unitary matrix. The experiment operated in reverse, i.e., taking the output ports as inputs and reversing time corresponds to the transposed complex conjugate of the inverse matrix and is therefore equivalent to the original unitary matrix:

$$
U (N) = \left(T _ {N, N - 1} \cdot T _ {N, N - 2} \dots T _ {2, 1} \cdot D\right) ^ {- 1}. \tag {7}
$$

This can be easily confirmed by multiplying the calculated beam splitter and phase shift matrices. The experimental setup for a general  $3 \times 3$  unitary matrix is shown in Fig. 2.

Here we notice that our alternative interpretation [Eq. (3)] shows how successive "rotation" matrices with

![](images/7db48de6d782cd432642590e17d885031ca4b944a229a14ab98a6a0b95f7ea32.jpg)  
FIG. 2. Three beam splitter devices  $T_{pq}$  and three additional phase shifters  $\alpha_{i}$  are enough to build any  $3 \times 3$  unitary matrix. Notice that because of operation in reverse the individual device's phase shifts  $\phi_{pq}$  are now at the input ports and the final phase shifters  $\alpha_{i}$  at the output ports.

reduced dimensions  $R(N - 1), R(N - 2), \ldots, R(2)$  can be used to create the most general set of  $N$  mutually orthogonal vectors in  $N$ -dimensional space. The practical implementation of this method involves a triangular array of beam splitters, each diagonal row in the triangle reducing the effective dimension of the Hilbert space by one (see Fig. 3).

Since our algorithm is recursive, the factorization of a unitary matrix into beam splitter and phase shift matrices is valid for any finite dimension. For example, six beam splitters with appropriate phase shifts provide an experiment equivalent to an arbitrary  $4 \times 4$  unitary matrix. The maximum number of beam splitter devices needed to build a general  $N$ -dimensional unitary matrix is  $\binom{N}{2} = \frac{N(N-1)}{2}$ . This number grows only quadratically with  $N$ , giving realistic hope that optical experiments in higher-dimensional Hilbert spaces using multiport beam splitters will be possible in the near future. (We suggest that the optical realization of continuous unitary operators might be achieved by suitable holographic or Fourier-transform optical arrangements.) In fact, our method not only provides an experiment for any matrix in  $\mathrm{U}(\mathbf{N})$ , but also an experimental setup which parametrizes the whole  $N$ -dimensional unitary group.

Once all matrices of  $\mathrm{U}(\mathbf{N})$  can be implemented, it becomes possible to measure the analog of the observable corresponding to any discrete Hermitian matrix  $H$ . Note that such a measurement requires, in general,  $N$  detectors, one for each of the  $N$  orthogonal normalized eigenstates, which correspond to the  $N$  unit eigenvectors of the matrix  $H$ . We denote the eigenvectors as  $|1\rangle, \ldots, |N\rangle$  and the corresponding eigenvalues with  $\{h_1, h_2, \ldots, h_N\}$ , a set of  $N$  real numbers. They do not have to be different; the case of degenerate eigenvalues can be treated in the same way.

The measurement apparatus makes the first detector fire if the input state is  $|1\rangle$ , the second if it is  $|2\rangle$ , etc. In addition the amplitudes for a general input vector  $|\psi \rangle$  whose entries represent the amplitude for a photon to arrive at the respective input port are  $\langle 1|\psi \rangle$  to be detected by the first detector,  $\langle 2|\psi \rangle$  for the second, and  $\langle i|\psi \rangle$  for the  $i$ th. If the  $i$ th detector fires, the measured value of  $H$  equals  $h_i$ . The unitary matrix  $U$  involved in such a measurement must "sort" the incoming amplitude into  $N$  output ports corresponding to the  $N$  eigenstates  $|1\rangle, \ldots, |N\rangle$ . ( $U$  is sometimes called the premeasurement

![](images/f068d39378780ecdd62b32d86b441185bb49c04547c699f0282f6080ec982460.jpg)  
FIG. 3. A triangular array of beam splitters implements any  $N \times N$  unitary matrix as an optical multiport. The beams are solid lines. A suitable beam splitter is at each crossing point of the beams. Phase shifters are at one input of each beam splitter and at the outputs  $(1', \ldots, N')$  of the multiport. Each diagonal row of beam splitters performs a transformation reducing the effective dimension of the Hilbert space by one.

operator.) The measurement apparatus corresponding to the Hermitian matrix  $H$  consists of the experimental embodiment of  $U$  and a set of  $N$  detectors.

The unitary matrix belonging to  $H$  is constructed from the eigenvectors of  $H$  by stacking their dual row vectors  $\langle 1|, \ldots, \langle N|$  in numerical order. This matrix has the same form as  $U(\mathbf{N})$  in Eq. (4). The experiment corresponding to this matrix is constructed using the algorithm presented above.

As an example we choose one matrix from Mermin's version of the Bell-Kochen-Specker theorem. One of the Hermitian operators to be measured is  $\sigma_y\otimes \sigma_x$  , with the matrix representation

$$
H = \left( \begin{array}{c c c c} 0 & 0 & 0 & - i \\ 0 & 0 & - i & 0 \\ 0 & i & 0 & 0 \\ i & 0 & 0 & 0 \end{array} \right). \tag {8}
$$

The corresponding unitary operator is composed of the stacked bra eigenvectors of  $H$ :

$$
\left( \begin{array}{l} \langle h _ {1} = - 1 | \\ \langle h _ {2} = - 1 | \\ \langle h _ {3} = + 1 | \\ \langle h _ {4} = + 1 | \end{array} \right) = \frac {1}{\sqrt {2}} \left( \begin{array}{c c c c} - i & 0 & 0 & 1 \\ 0 & - i & 1 & 0 \\ i & 0 & 0 & 1 \\ 0 & i & 1 & 0 \end{array} \right). \tag {9}
$$

The experimental realization of this matrix can easily be calculated using our algorithm:

<table><tr><td></td><td>ω</td><td>φ</td><td>Note</td></tr><tr><td>T43</td><td colspan="2">exchange</td><td>beams 3 and 4</td></tr><tr><td>T42</td><td>π/4</td><td>π/2</td><td>1:1 beam splitter</td></tr><tr><td>T31</td><td>π/4</td><td>π/2</td><td>1:1 beam splitter</td></tr><tr><td>Phases</td><td colspan="2">α1 = α2 = 0</td><td>α3 = α4 = π</td></tr></table>

The zeros in the matrix reduce the number of beam splitters necessary in the corresponding experiment: transfor

mations  $T_{41}$ ,  $T_{32}$ , and  $T_{21}$  can be skipped. The probability measuring the value  $h_i$  is given by  $|\langle h_i|\psi \rangle|^2$  and is exactly equal to detecting the photon in the output port  $i$ . Thus all the  $4\times 4$  unitary matrices corresponding to the Hermitian matrices used in Mermin's version of the Bell-Kochen-Specker theorem can be realized in simple quantum optical experiments.

Current work in Innsbruck Laboratory aims at building beam splitter analogs of both Kochen-Specker type experiments and experiments studying Einstein-Podolsky-Rosen correlations in higher-dimensional Hilbert spaces. Finally, we should mention another possibly important application in atom lithography, where our results imply that it is possible to realize experimentally any discrete unitary operator acting on an atomic beam. In such an experiment, the equivalent of beam splitters could be suitably arranged laser fields [18]. It follows from the generality of our results that such laser fields can be described using the same formalism as presented above for the photonic beam splitter.

We would like to acknowledge useful discussions with D. M. Greenberger and M. A. Horne. This work was supported by the Fond zur Förderung der Wissenschaftlichen Forschung, Austria, Schwerpunkt Quantenoptik Project No. S06502, and by the U.S. NSF Grant No. PHY 92-13964.

[1] A. Zeilinger, M. Zukowski, M. A. Horne, H. J. Bernstein, and D. M. Greenberger, in Fundamental Aspects of Quantum Theory, edited by J. Anandan (World Scientific, Singapore, 1993).  
[2] A. K. Ekert, Phys. Rev. Lett. 67, 661 (1991).  
[3] C. H. Bennett, G. Brassard, C. Crépeau, R. Jozsa, A. Peres, and W. K. Wootters, Phys. Rev. Lett. 70, 1895 (1993).  
[4] A. R. Swift and R. Wright, J. Math. Phys. 21, 77 (1980).

[5] B. O. Hultgren III and A. Shimony, J. Math. Phys. 18, 381 (1977); C. Ulrich, Diplomathesis, Technical University Vienna, 1993 (unpublished).  
[6] A. Garg and N. Mermin, Phys. Rev. Lett. 49, 901 (1982); 49, 1294 (1982); N. Gisin and A. Peres, Phys. Lett. A 162, 15 (1992); A. Peres, Phys. Rev. A 46, 4413 (1992).  
[7] A. Zeilinger, H. J. Bernstein, D. M. Greenberger, M. A. Horne, and M. Zukowski, in Quantum Control and Measurement, edited by H. Ezawa and Y. Murayama (North-Holland, Amsterdam, 1993), pp. 9-22.  
[8] A. M. Gleason, J. Math. Mech. 6, 885 (1957); J. S. Bell, Rev. Mod. Phys. 38, 447 (1966); S. Kochen and E. Specker, J. Math. Mech. 17, 59 (1967); A. Peres, J. Phys. A. 24, L175 (1991); N. D. Mermin, Rev. Mod. Phys. 65, 803 (1993).  
[9] J. W. Noh, A. Fougères, and L. Mandel, Phys. Rev. Lett. 67, 1426 (1991); Phys. Rev. A 45, 424 (1992); 46, 2840 (1992).  
[10] U. Leonhardt and H. Paul, Phys. Rev. A 47, R2460 (1993); J. Mod. Opt. 40, 1745 (1993); G. S. Agarwal, Opt. Commun. 100, 479 (1993).  
[11] N. G. Walker, J. Mod. Opt. 34, 15 (1987).  
[12] E. P. Wigner, Z. Phys. 133, 101 (1952); E. P. Wigner, Am. J. Phys. 31, 6 (1963); W. E. Lamb, Jr., Phys. Today 22, No. 4, 23 (1969).  
[13] B. Yurke, S. L. McCall, and J. R. Klauder, Phys. Rev. A 33, 4033 (1986).  
[14] A. Zeilinger, Am. J. Phys. 49, 882 (1981); Z. Y. Ou, C. K. Hong, and L. Mandel, Opt. Commun. 63, 118 (1987); S. Prasad, M. O. Scully, and W. Marthiessen, Opt. Commun. 62, 139 (1987); H. Fearn and R. Loudon, J. Opt. Soc. Am. B 6, 917 (1989); R. A. Campos, B. E. A. Saleh, and M. C. Teich, Phys. Rev. A 42, 4127 (1990).  
[15] S. Danakas and P. K. Aravind, Phys. Rev. A 45, 1973 (1992).  
[16] H. J. Bernstein, J. Math. Phys. 15, 1677 (1974).  
[17] F. D. Murnaghan, The Orthogonal and Symplectic Groups (Institute for Advanced Studies, Dublin, 1958).  
[18] P. J. Martin, B. G. Oldaker, A. H. Miklich, and D. E. Pritchard, Phys. Rev. Lett. 60, 515 (1988); J. J. McClelland, R. E. Scholten, E. C. Palm, and R. J. Celotta, Science 262, 877 (1993).

![](images/7c1220f4b8bb6cf9c2d342379c26297919590155851fc6d44fb59919fcfcab65.jpg)  
FIG. 1. A Mach-Zehnder interferometer can be used instead of a variable reflectivity beam splitter as the basic building block of any  $N \times N$  unitary matrix. On the left is one experimental realization of the device using two 50:50 beam splitters, two mirrors, and two phase shifters. The Mach-Zehnder interferometer can be represented by the abstract four-port device on the right. Two parameters  $(\phi, \omega)$  of the transformation  $T$  are set in the device.

![](images/3c6301c9e1d7631468a325b9e2f4f10dee14bf6e478363d46afbfd3c309946a4.jpg)

![](images/a52a3bcad1f7dbd6739e56844f7dc4e4cf891979bb289b1ebfd2ca6189daf3be.jpg)  
FIG. 3. A triangular array of beam splitters implements any  $N \times N$  unitary matrix as an optical multiport. The beams are solid lines. A suitable beam splitter is at each crossing point of the beams. Phase shifters are at one input of each beam splitter and at the outputs  $(1', \dots, N')$  of the multiport. Each diagonal row of beam splitters performs a transformation reducing the effective dimension of the Hilbert space by one.