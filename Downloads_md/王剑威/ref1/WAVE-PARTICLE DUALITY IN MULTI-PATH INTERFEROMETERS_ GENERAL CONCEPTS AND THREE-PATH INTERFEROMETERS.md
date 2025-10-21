# WAVE-PARTICLE DUALITY IN MULTI-PATH INTERFEROMETERS: GENERAL CONCEPTS AND THREE-PATH INTERFEROMETERS

BERTHOLD-GEORG ENGLERT*,†,§, DAGOMIR KASZLIKOWSKI*,†,¶, LEONG CHUAN KWEK*,†,‡,∥ and WEI HUI CHEE*,**

*Department of Physics, National University of Singapore, Singapore 117542

†Centre for Quantum Technologies,

National University of Singapore, Singapore 117543

$^{\ddagger}$ Nanyang Technological University,

National Institute of Education, Singapore 259756

$^\mathrm{g}phyebg@nus.edu.sg$

phykd@nus.edu.sg

lckwek@nie.edu.sg,phyklc@nus.edu.sg

**yuniesan@yahoo.com.sg

Received 1 October 2007

For two-path interferometers, the which-path predictability  $\mathcal{P}$  and the fringe visibility  $\mathcal{V}$  are familiar quantities that are much used to talk about wave-particle duality in a quantitative way. We discuss several candidates that suggest themselves as generalizations  $P$  of  $\mathcal{P}$  for multi-path interferometers, and treat the case of three paths in considerable detail. To each choice for the path knowledge  $P$ , the interference strength  $V$  — the corresponding generalization of  $\mathcal{V}$  — is found by a natural, operational procedure. In experimental terms, it amounts to finding those equal-weight superpositions of the path amplitudes which maximize  $P$  for the emerging intensities. Mathematically speaking, one needs to identify a certain optimum one among the Fourier transforms of the state of the interfering quantum object. Wave-particle duality is manifest, inasmuch as  $P = 1$  implies  $V = 0$  and  $V = 1$  implies  $P = 0$ , whatever definition is chosen. The possible values of the pair  $(P,V)$  are restricted to an area with corners at  $(P,V) = (0,0)$ ,  $(P,V) = (1,0)$ , and  $(P,V) = (0,1)$ , with the shape of the border line from  $(1,0)$  to  $(0,1)$ , depending on the particular choice for  $P$  and the induced definition of  $V$ .

Keywords: Interferometers; wave-particle duality; path knowledge; interference strength.

PACS Number(s): 03.65.Ta, 07.60.Ly

# 1. Introduction

Einstein's wave-particle duality is arguably the most familiar phenomenon resulting from Bohr's principle of complementarity. $^{a}$  The intense debate between these two

protagonists, of which Bohr's essay on the occasion of Einstein's 70th birthday is the best known public record, $^{3}$  continues to be the object of scholarly studies, $^{4}$  but there is, of course, rather widespread agreement by now on what used to be controversial issues then.

In the late 1920s and early 1930s, discussions of wave-particle duality focused on the extreme situations where only the particle aspects are present, or only the wave aspects. As natural as this focus may have been then, it does not do full justice to the subject, as it ignores the intermediate situations in which both aspects of an atomic system coexist within the boundaries that nature imposes by the laws of quantum mechanics.

The compromises that she permits are well-understood in the context of two-path interferometers, where various inequalities quantify to which extent wave and particle properties can be observed simultaneously. The historical example of the Bohr-Einstein debate — Einstein's version of Young's double-slit interferometer, with a recoiling first single slit — is familiar textbook material, but its literal realization has not been achieved yet.

What has become experimental reality, however, are analogous two-path interferometers of various kinds: for photons, $^{9,15-21}$  neutrons, $^{7,22}$  and atoms. $^{23-25}$  They enable quantitative studies of wave-particle duality, in which the said inequalities are tested. $^c$  As expected, it is consistently found that the inequalities are obeyed, and not a single violation has been reported.

The basic inequality reads

$$
\mathcal {P} ^ {2} + \mathcal {V} ^ {2} \leq 1; \tag {1}
$$

all others can be derived from it with more or less sophisticated arguments.5 Here, the predictability  $\mathcal{P}$  quantifies the particle aspects: the a priori odds for guessing the path right are given by  $1 / 2(1 + \mathcal{P})$ , and the visibility  $\mathcal{V}$  is simply the standard fringe visibility, the quantitative measure for the wave aspect.

It is our primary objective in this paper to introduce, and discuss, the generalization to multi-path interferometers, with a particular emphasis on three-path interferometers, where most features are already present in their generic forms. To this end, we shall not employ Durr's strategy of Ref. 26, who aimed at generalizations of  $\mathcal{P}$  and  $\mathcal{V}$  such that the equal sign in (1) continues to apply for all pure states propagating through an  $n$ -path interferometer, as it does for two-path interferometers. Rather, we consider a few possible choices for a generalization of  $\mathcal{P}$  that suggest themselves and identify the corresponding generalization of  $\mathcal{V}$  in, so we think, a natural way.

Our present effort is not the first of its kind. We have already mentioned Durr's work,[26] which is quite substantial, and an earlier discussion, rather brief and with

no definite conclusions, is contained in Ref. 12. We explore suggestions for generalizing  $\mathcal{P}$  from both. By contrast, the recent approach by Luis,[27] who is motivated by the experiment of Ref. 25, does not fit into our strategy; put tersely, he is concerned with "this-path information" whereas we care about "which-path information."

Here is a brief outline. After presenting our general strategy in Sec. 2, we illustrate matters in the simple situation of two-path interferometers in Sec. 3. This is followed by a detailed study of three-path interferometers in Sec. 4, which exhibit the generic features of multi-path interferometers. Four-path interferometers and multi-path interferometers are then briefly dealt with in Sec. 5. We close with a summary.

# 2. General Considerations

# 2.1. Operating an interferometer in particle mode or wave mode

In the most general terms, a  $n$ -path interferometer consists of an initial preparation stage and a final probing stage, see Fig. 1. It is convenient to describe the state of the interfering system between the stages by a  $n \times n$  density matrix,

$$
\varrho = \left( \begin{array}{c c c c} \varrho_ {1 1} & \varrho_ {1 2} & \dots & \varrho_ {1 n} \\ \varrho_ {2 1} & \varrho_ {2 2} & \dots & \varrho_ {2 n} \\ \vdots & & \ddots & \vdots \\ \varrho_ {n 1} & & \dots & \varrho_ {n n} \end{array} \right), \quad \varrho \geq 0, \quad \operatorname {t r} \{\varrho \} = 1. \tag {2}
$$

Of course, the diagonal entries  $\varrho_{11},\varrho_{22},\ldots ,\varrho_{nn}$  are the probabilities of finding the system in the 1st, 2nd,..., nth path, respectively. These probabilities are experimentally available by operating the interferometer in the particle mode of Fig. 1(a).

The wave mode of Fig. 1(b) probes the off-diagonal elements in (2). The unitary  $n \times n$  matrix  $F$  of the Fourier transformation,

$$
\varrho \rightarrow \tilde {\varrho} = F \varrho F ^ {\dagger}, \quad F ^ {\dagger} = F ^ {- 1}, \tag {3}
$$

is such that all its matrix elements are of the same absolute size,

$$
\left| F _ {j k} \right| = \frac {1}{\sqrt {n}}, \tag {4}
$$

for which

$$
F _ {j k} = \left(F ^ {- 1}\right) _ {k j} ^ {*} = \frac {1}{\sqrt {n}} \mathrm {e} ^ {\mathrm {i} 2 \pi j k / n} \mathrm {e} ^ {\mathrm {i} \phi_ {j} + \mathrm {i} \varphi_ {k}} \tag {5}
$$

is the generic example, where  $\phi_j$  and  $\varphi_k$  are arbitrary phases. If  $\phi_j = 0$  and  $\varphi_k = 0$  for all  $j$  and  $k$ , we obtain the matrix of the standard discrete Fourier transformation. The resulting probability of the  $m$ th detector to click is

$$
\tilde {\varrho} _ {m m} = \left(F \varrho F ^ {\dagger}\right) _ {m m} = \frac {1}{n} + \sum_ {j \neq k} F _ {m j} \varrho_ {j k} F _ {m k} ^ {*} \tag {6}
$$

![](images/4c3479fedf9ac54947e34d9d12027d5ac003f14fd931a36d425954e202fee2e3.jpg)  
(a)

![](images/f09459df999d0d70651e04422459d4329391da07fac6cc640530efc69cd15e0d.jpg)  
(b)  
Fig. 1. The two stages of a  $n$ -path interferometer: preparation stage and probing stage, and the two modes of operation: particle mode and wave mode. Left side: At the preparation stage, the incoming intensity (usually only one input port is used) is distributed over all paths by a "generalized beam splitter" or nitter, which is the  $n$ -port version of the entry beam splitter of the common two-path interferometers. A symmetric nitter is unbiased and assigns equal intensity to all paths (analogous to a symmetric 50:50 beam splitter), but it is more general to allow for a biased transformation (an asymmetric beam splitter in the case of  $n = 2$ ), so that the intensity may vary from one path to the next. Right side: (a) In particle mode (top), the probing just amounts to detecting the path, a click of detector  $D_{m}$  indicating that the  $m$ th path was the case. (b) In wave mode (bottom), the probing stage uses a Fourier transformation, that is: a symmetric nitter, in front of the detectors, so that all paths contribute equally to the intensity in each of the  $n$  output ports. In principle, any arbitrary Fourier transformation is to be considered, but in practice a suitably chosen set of  $n$  transformations suffice, each characterized by the values of the relative phases between the amplitudes of the paths. The differences in the probabilities that the various detectors  $D_{1}, D_{2}, \ldots, D_{n}$  respond result only from these relative phases. Taken together, the probabilities constitute the potentially complicated interference pattern, in their dependence on those relative phases.

in general, and

$$
\tilde {\varrho} _ {m m} = \frac {1}{n} + \frac {1}{n} \sum_ {j \neq k} \mathrm {e} ^ {\mathrm {i} 2 \pi m (j - k) / n} \mathrm {e} ^ {\mathrm {i} (\varphi_ {j} - \varphi_ {k})} \varrho_ {j k} \tag {7}
$$

in particular for the generic  $F$  of (5), where the phases  $\phi_j$  are irrelevant in this context.

We must not fail to note that, as a consequence of the defining property (4) of the general Fourier transform, the two modes of operation in Fig. 1 are complementary. For, if the path is certain in particle mode, that is:  $\varrho_{mm} = \delta_{mm'}$  if the  $m'$ th

path is the case, then all detectors will click with equal probability in wave mode:  $\tilde{\varrho}_{mm} = 1 / n$ . And conversely, if  $\tilde{\varrho}_{mm} = \delta_{mm'}$  for one Fourier transform in Fig. 1(b), then  $\varrho_{mm} = 1 / n$  follows, so that all paths are found with equal probability in Fig. 1(a).

# 2.2. Fourier matrices

What is hinted at in Eq. (5) can be carried out for any Fourier matrix,

$$
F = \left( \begin{array}{c c c c} \mathrm {e} ^ {\mathrm {i} \phi_ {1}} & 0 & \dots & 0 \\ 0 & \mathrm {e} ^ {\mathrm {i} \phi_ {2}} & \dots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & & \dots & \mathrm {e} ^ {\mathrm {i} \phi_ {n}} \end{array} \right) \frac {1}{\sqrt {n}} \left( \begin{array}{c c c c} \cdot & \dots & \dots & 1 \\ \vdots & \ddots & & 1 \\ \vdots & & \ddots & \vdots \\ 1 & 1 & \dots & 1 \end{array} \right) \left( \begin{array}{c c c c} \mathrm {e} ^ {\mathrm {i} \varphi_ {1}} & 0 & \dots & 0 \\ 0 & \mathrm {e} ^ {\mathrm {i} \varphi_ {2}} & \dots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & & \dots & \mathrm {e} ^ {\mathrm {i} \varphi_ {n}} \end{array} \right), \tag {8}
$$

where the input phases  $\varphi_{k}$  and the output phases  $\phi_{j}$  are pulled out such that the central Fourier matrix has elements  $1 / \sqrt{n}$  in the  $n$ th row and the  $n$ th column. Only  $n - 1$  of these  $2n$  phases are relevant because the  $\tilde{\varrho}_{mm}$ s do not involve the output phases  $\phi_{k}$ , and the option to redefine all phases jointly in accordance with

$$
\phi_ {j} \rightarrow \phi_ {j} + \alpha , \quad \varphi_ {k} \rightarrow \varphi_ {k} - \alpha \quad (\alpha \text {a r b i t r a r y}) \tag {9}
$$

can be used to set, say,  $\varphi_{n} = 0$  by convention.

For  $n = 2$ , this gives a unique central Fourier matrix,

$$
F = \frac {1}{\sqrt {2}} \left( \begin{array}{c c} - 1 & 1 \\ 1 & 1 \end{array} \right), \tag {10}
$$

and for  $n = 3$ , there are two possible central Fourier matrices,

$$
F = \frac {1}{\sqrt {3}} \left( \begin{array}{c c c} \mathrm {e} ^ {\mathrm {i} 2 \pi / 3} & \mathrm {e} ^ {- \mathrm {i} 2 \pi / 3} & 1 \\ \mathrm {e} ^ {- \mathrm {i} 2 \pi / 3} & \mathrm {e} ^ {\mathrm {i} 2 \pi / 3} & 1 \\ 1 & 1 & 1 \end{array} \right) \text {a n d} F = \frac {1}{\sqrt {3}} \left( \begin{array}{c c c} \mathrm {e} ^ {- \mathrm {i} 2 \pi / 3} & \mathrm {e} ^ {\mathrm {i} 2 \pi / 3} & 1 \\ \mathrm {e} ^ {\mathrm {i} 2 \pi / 3} & \mathrm {e} ^ {- \mathrm {i} 2 \pi / 3} & 1 \\ 1 & 1 & 1 \end{array} \right), \tag {11}
$$

but these two are equivalent for our purposes because they differ only by a permutation of rows, that is: of the output channels, which can be compensated for by a re-labeling of the detectors in Fig. 1(b).

For  $n = 4$ , we have a one-parametric family of possible central Fourier matrices,

$$
F = \frac {1}{2} \left( \begin{array}{c c c c} \mathrm {e} ^ {\mathrm {i} t} & - 1 & - \mathrm {e} ^ {\mathrm {i} t} & 1 \\ - 1 & 1 & - 1 & 1 \\ - \mathrm {e} ^ {\mathrm {i} t} & - 1 & \mathrm {e} ^ {\mathrm {i} t} & 1 \\ 1 & 1 & 1 & 1 \end{array} \right) \quad \text {w i t h a r b i t r a r y r e a l} t, \tag {12}
$$

supplemented by those matrices that one obtains by permutations of columns that cannot be undone by permuting rows. The Fourier matrix of (5) corresponds to  $t = \pi / 2$ , and  $t = 0$  in conjunction with permuting the 2nd and 3rd rows gives the tensor product of the  $2 \times 2$  matrix in Eq. (10) with itself.

For  $n = 5$ , the situation is similar to that for  $n = 3$ , as there is essentially only one central Fourier matrix, the standard one of (5). Unfortunately, this is not true for other prime values of  $n$ . For example, there are five inequivalent choices for  $n = 7$ . And for composite values of  $n$ , we have continuous families of central Fourier matrices, as illustrated above for  $n = 4 = 2 \times 2$ ; more about this at the website of Ref. 28.

Our choice of terminology to refer to all matrices with the property (4) as Fourier matrices is not everybody's convention. Some authors speak of Hadamard matrices instead, thus generalizing the real Hadamard matrices of combinatorics which have  $\pm 1$  as matrix elements — such as the  $2 \times 2$  matrix in Eq. (10) or the  $t = 0$  version of the  $4 \times 4$  matrix in Eq. (12) — to complex matrices, and our central Fourier matrices of (8) are called dephased Hadamard matrices. Unfortunately, the general parameterization of all Fourier or Hadamard  $n \times n$  matrices is not known for arbitrary values of  $n$ . A concise guide is Ref. 29, and a catalog of known cases up to  $n = 16$  is available at the website mentioned, in a truly commendable effort, by Žyczkowski and Tadej, where one also finds an extensive list of references on the subject.

From the point of view of quantum physics, the elements of a Fourier matrix are the transition amplitudes between two mutually unbiased bases. Accordingly, the particle-mode and the wave-mode operation of the  $n$ -path interferometer in Fig. 1 realize the measurements of a pair of complementary observables, as we noted at the end of Sec. 2.1. In this context, one usually encounters Fourier transformations, and this prompted our choice of terminology.

# 2.3. Quantification of the path knowledge

Path knowledge is knowledge about the probabilities for detector clicks in Fig. 1(a), that is: knowledge about the diagonal elements of the density matrix  $\varrho$  in (2). In view of the normalization of  $\varrho$  to unit trace, one needs  $n - 1$  real parameters to specify all  $\varrho_{mm}$ . For example, the real and imaginary parts of the complex numbers  $z_{1}, z_{2}, \ldots, z_{n - 1}$  that are defined by

$$
z _ {k} = \sum_ {m = 1} ^ {n} \mathrm {e} ^ {\mathrm {i} 2 \pi k m / n} \varrho_ {m m} = z _ {n - k} ^ {*} \tag {13}
$$

may serve this purpose. Clearly, then, there cannot be a unique universal way of quantifying path knowledge by a single number (except for  $n = 2$ ), and various numerical measures will be justifiable. To a considerable extent, it thus remains a matter of taste or convenience for which of them to opt, unless particular circumstances leave no choice.

We shall regard any continuous function  $P(\mathrm{diag}\varrho) \equiv P(\varrho_{11},\varrho_{22},\ldots ,\varrho_{nn})$  of the diagonal elements of  $\varrho$  as an acceptable measure of path knowledge, and thus as a valid generalization of the two-path predictability  $\mathcal{P}$ , if it meets these natural criteria:

(a)  $P = 1$  if  $\varrho_{mm} = 1$  for one  $m$ , i.e. if the path is certain, and only then.  
(b)  $P = 0$  if  $\varrho_{mm} = 1 / n$  for all  $m$ , i.e. if the path is completely uncertain.  
(c)  $P$  must be invariant under permutations of the diagonal elements of  $\varrho$ .  
(d)  $P$  must be convex, that is:

$$
P (\operatorname {d i a g} \varrho) \leq (1 - \lambda) P (\operatorname {d i a g} \varrho_ {1}) + \lambda P (\operatorname {d i a g} \varrho_ {2}) \tag {14}
$$

with  $\varrho = (1 - \lambda)\varrho_{1} + \lambda \varrho_{2}$  and  $0\leq \lambda \leq 1$  holds for any two density matrices  $\varrho_{1}$  and  $\varrho_{2}$ .

(e) Any degradation of the  $\varrho_{mm}$ , that is: the increase of a smaller one at the expense of a larger one, must not increase the value of  $P$ .

Property (14e) is actually implied by property (14d), but we list it nevertheless because it is a weaker version of Durr's fourth criterion, at Eq. (1.14) in Ref. 26, which requires "should decrease" rather than "must not increase." The other properties are equivalent to Durr's.

# 2.3.1. First example: Betting on the path

In Eq. (1), we recalled that the standard predictability  $\mathcal{P}$  of two-path interferometers is essentially the odds for guessing the way right. More generally, then, a path-knowledge function  $P(\mathrm{diag}\varrho)$  can be associated with a given set of betting rules, and this will serve as our first example.

Whereas there is really only one kind of bet for  $n = 2$ , there is a variety of possible bets in  $n$ -path interferometers. We consider bets of the following construction.

If you guess the path right on the 1st try, you win  $g_{1} = 1$  unit. If your 1st guess is wrong, but your 2nd is right, you win  $g_{2}$  units.

And so forth: if you need  $m$  guesses, you win  $g_{m}$  units, and if all

your  $n - 1$  guesses are wrong, you win  $g_{n}$  units (which will be a negative amount, so that you actually lose).

The amount won should be the larger, the fewer guesses you need, and a random guess should have a neutral overall return. These natural requirements impose the restrictions

$$
1 = g _ {1} > g _ {2} \geq g _ {3} \geq \dots \geq g _ {n}, \quad \sum_ {m = 1} ^ {n} g _ {m} = 0. \tag {16}
$$

The optimal betting strategy is clearly to first bet on the most likely path, then on the second most likely, and so on. On average, the gain is then

$$
P _ {\text {b e t}} = \sum_ {m = 1} ^ {n} g _ {m} p _ {m}, \tag {17}
$$

where the  $p_m$ s are the  $\varrho_{mm}$ s in descending order,

$$
\left\{p _ {1}, p _ {2}, \dots , p _ {n} \right\} = \left\{\varrho_ {1 1}, \varrho_ {2 2}, \dots , \varrho_ {n n} \right\}, \quad p _ {1} \geq p _ {2} \geq \dots \geq p _ {n} \geq 0. \tag {18}
$$

By construction,  $P_{\mathrm{bet}}$  meets the criteria (14a-e), and so  $P_{\mathrm{bet}}$  is an acceptable numerical measure of path knowledge. It is, in fact, the relevant measure if the bet specified by the choice of  $g_{m}$ s is the operational procedure for verifying someone's claim that he has such knowledge.

A particularly simple case is the "one-guess bet," specified by  $g_{1} = 1$ ,  $g_{2} = g_{3} = \dots = g_{n} = -1 / (n - 1)$ , for which

$$
\begin{array}{l} P _ {\mathrm {b e t}} ^ {(1 \mathrm {g u e s s})} = \frac {n}{n - 1} p _ {1} - \frac {1}{n - 1} \\ = \frac {n}{n - 1} \max  _ {m} \left\{\varrho_ {m m} \right\} - \frac {1}{n - 1}. \tag {19} \\ \end{array}
$$

This is the proposal that is briefly discussed in Appendix C of Ref. 12. Equally natural is the "linear bet,"

$$
P _ {\text {b e t}} ^ {(\text {l i n})} = \frac {n + 1}{n - 1} - \frac {2}{n - 1} \sum_ {m = 1} ^ {n} m p _ {m}, \tag {20}
$$

that has  $g_{m} = (n + 1 - 2m) / (n - 1)$ . Harkening back to the remark after (14), we note that the linear bet meets Durr's stronger requirement that any degradation should decrease  $P$ , whereas the one-guess bet does so only for  $n = 2$ .

# 2.3.2. Second example: Normalized purity

As a second example, we consider Durr's proposal of Ref. 26, who constructs a path-knowledge function  $P(\mathrm{diag}\varrho)$  from the so-called "purity" of the probability distribution, essentially the sum of the squared path probabilities. Durr's path-knowledge function is

$$
P _ {\text {p u r}} = \left(\frac {n}{n - 1} \sum_ {m = 1} ^ {n} \varrho_ {m m} ^ {2} - \frac {1}{n - 1}\right) ^ {\frac {1}{2}}, \tag {21}
$$

which is properly normalized to meet requirements (14a) and (14b).

# 2.3.3. Third example: Normalized Shannon entropy

From the Shannon entropy $^{30}$  associated with the probability distribution  $\mathrm{diag}\varrho$

$$
S (\operatorname {d i a g} \varrho) = - \sum_ {m = 1} ^ {n} \varrho_ {m m} \log \varrho_ {m m} \tag {22}
$$

one can construct yet another path-knowledge function. This approach was regarded as the natural one by the authors of Refs. 6 and 9 in the context of two-path interferometers, but was found less appealing for  $n$ -path interferometers by the authors of Refs. 12 and 26.

Upon proper normalization to meet requirements (14a) and (14b), the entropic measure of path knowledge is given by

$$
P _ {\text {e n t}} = \frac {1}{\log n} \sum_ {m = 1} ^ {n} \varrho_ {m m} \log \left(n \varrho_ {m m}\right). \tag {23}
$$

Whereas the binary logarithm is usually understood in Eq. (22), it does not matter which base value is chosen in Eq. (23).

# 2.3.4. Fourth example: Rényi-type measures

It is worth mentioning that, as a generalization of both the purity measure in Eq. (21) and the entropic measure in Eq. (23), one could employ the Rényi-type measures that are defined by

$$
P _ {\text {R e n}} ^ {(\lambda)} = \left(\frac {n ^ {\lambda}}{n ^ {\lambda} - n} \sum_ {m = 1} ^ {n} \varrho_ {m m} ^ {\lambda} - \frac {n}{n ^ {\lambda} - n}\right) ^ {\frac {1}{\lambda}} \tag {24}
$$

where  $\lambda$  is a positive parameter. We recover the purity measure for  $\lambda = 2$  and the entropic measure in the limit  $\lambda \to 1$ ,

$$
P _ {\text {R e n}} ^ {(2)} = P _ {\text {p u r}}, \quad P _ {\text {R e n}} ^ {(1)} \equiv P _ {\text {R e n}} ^ {(\lambda \rightarrow 1)} = P _ {\text {e n t}}, \tag {25}
$$

and intermediate  $\lambda$  values interpolate between  $P_{\mathrm{pur}}$  and  $P_{\mathrm{ent}}$ .

There are also the limits  $\lambda \to \infty$  and  $\lambda \to 0$ , both of which are peculiar. We have

$$
P _ {\text {R e n}} ^ {(\infty)} \equiv P _ {\text {R e n}} ^ {(\lambda \rightarrow \infty)} = \left\{\begin{array}{l l}p _ {1}&\text {i f} n p _ {1} > 1,\\0&\text {i f} n p _ {1} = 1,\end{array}\right. \tag {26}
$$

for  $\lambda \to \infty$ , and

$$
P _ {\text {R e n}} ^ {(0)} \equiv P _ {\text {R e n}} ^ {(\lambda \rightarrow 0)} = \left\{\begin{array}{l l}1&\text {i f} p _ {1} = 1,\\0&\text {i f} p _ {1} <   1,\end{array}\right. \tag {27}
$$

for  $\lambda \to 0$ . For both, the value of  $p_1 = \max_m \{\varrho_{mm}\}$  matters solely, which makes  $P_{\mathrm{Ren}}^{(\infty)}$ , and to a much lesser extent, also  $P_{\mathrm{Ren}}^{(0)}$ , somewhat similar to  $P_{\mathrm{bet}}^{(1 \text{ guess})}$ .

We are not examining these Rényi-type measures in the situations of  $n = 2$  and  $n = 3$  that are dealt with in Secs. 3 and 4, but will offer a few comments on the limiting measures  $P_{\mathrm{Ren}}^{(\infty)}$  and  $P_{\mathrm{Ren}}^{(0)}$  for arbitrary  $n$  values in Sec. 6.

# 2.4. Quantification of the tendency for interference

Rather than introducing independent numerical measures for the strength of the interference between the paths, we derive the corresponding wave quantity from the given particle quantity, that is: the given path-knowledge function  $P(\mathrm{diag}\varrho)$ . Since we are thus constructing generalizations of the two-path visibility  $\mathcal{V}$ , the letter  $V$  will be used for these measures of the tendency for interference.

After the Fourier transformation in Fig. 1(b), we have the density matrix  $\tilde{\varrho} = F\varrho F^{\dagger}$  and  $P(\mathrm{diag}\tilde{\varrho})$  telling us how much path knowledge is available in the transformed state. As the explicit expression (6) for the diagonal elements of  $\tilde{\varrho}$  shows, the value of  $P(\mathrm{diag}\tilde{\varrho})$  depends crucially on the off-diagonal elements of the density matrix  $\varrho$ , but not at all on the diagonal elements that yield the value of  $P(\mathrm{diag}\varrho)$ . Further, the particular choice for  $F$  enters  $P(\mathrm{diag}\tilde{\varrho})$ , and so its value will be rather small for some Fourier transformations and particularly large for others.

Accordingly, with the intention of quantifying the joint size of the off-diagonal elements of  $\varrho$  in a fitting manner, we define  $V(\mathrm{offdiag}\varrho)$  as the largest value that  $P(\mathrm{diag}\varrho)$  can attain,

$$
V (\text {o f f d i a g} \varrho) = \max  _ {F} P \left(\text {d i a g} \left\{F \varrho F ^ {\dagger} \right\}\right), \tag {28}
$$

where the maximum is sought in the set of all Fourier matrices  $F$ , that is: all unitary matrices that obey Eq. (4). Harkening back to the remark at the end of Sec. 2.2, we note that the maximization in Eq. (28) is over all measurements of observables that are complementary to the path observable of Fig. 1(a). Accordingly, this way of quantifying the interference strength has an unambiguous operational meaning.

As a consequence of the optimization in Eq. (28), the properties (14) of  $P(\mathrm{diag}\varrho)$  have their counterparts for  $V(\mathrm{offdiag}\varrho)$ , namely

(a)  $V = 0$  if  $\varrho_{mm} = 1$  for one  $m$ , i.e. if the path is certain.  
(b)  $V = 1$  is only possible if  $\varrho_{mm} = 1 / n$  for all  $m$ , i.e. if the path is completely uncertain, and only then.  
(c)  $V$  is invariant under permutations of the path labels.  
(d)  $V$  is convex, that is:

$$
V \left(\text {o f f d i a g} \varrho\right) \leq (1 - \lambda) V \left(\text {o f f d i a g} \varrho_ {1}\right) + \lambda V \left(\text {o f f d i a g} \varrho_ {2}\right) \tag {29}
$$

with  $\varrho = (1 - \lambda)\varrho_{1} + \lambda \varrho_{2}$  and  $0\leq \lambda \leq 1$  holds for any two density matrices  $\varrho_{1}$  and  $\varrho_{2}$ .

(e) A degradation of the  $\varrho_{jk}$ s ( $j \neq k$ ), that is: a reduction in size, cannot increase the value of  $V$ .

The maximum in Eq. (28) is crucial in establishing the convexity (29d); if instead we took a single Fourier matrix  $F$  in Eq. (28), or a too-small subset of Fourier matrices, the resulting interference-strength measure  $V$  would not be convex and, therefore, would be of rather limited use.

Clearly, then, for each set of betting rules in Sec. 2.3.1, there is an interference-strength measure  $V_{\mathrm{bet}}$  derived from the corresponding path-knowledge measure

$P_{\mathrm{bet}}$ . In particular, we have  $V_{\mathrm{bet}}^{(1 \text{ guess})}$  and  $V_{\mathrm{bet}}^{(\mathrm{lin})}$  paired with  $P_{\mathrm{bet}}^{(1 \text{ guess})}$  of Eq. (20) and  $P_{\mathrm{bet}}^{(\mathrm{lin})}$  of Eq. (21), respectively. And likewise, we have  $V_{\mathrm{pur}}$  associated with Durr's  $P_{\mathrm{pur}}$  of Sec. 2.3.2, and also an entropic  $V_{\mathrm{ent}}$  that goes with  $P_{\mathrm{ent}}$  of Sec. 2.3.3.

Each  $P, V$  pair can be used to study the compromises intermediate between the extreme situations of "particle aspect only" ( $P = 1$  and  $V = 0$ ) and "wave aspect only" ( $V = 1$  and  $P = 0$ ). Qualitatively, the same picture emerges for all  $P, V$  pairs: owing to the complementarity of the particle and wave modes of operation (recall the remark at the end of Sec. 2.1), the two aspects are mutually exclusive — if  $P = 1$ , then surely  $V = 0$ , and vice versa. In a  $P, V$  diagram, the extremal points  $(P, V) = (1,0)$  and  $(P, V) = (0,1)$  are connected by a (curved) line, which together with the straight lines to  $(P, V) = (0,0)$  encloses the area of all possible pairs of  $P, V$  values. The shape of the line from  $(P, V) = (1,0)$  to  $(P, V) = (0,1)$  and other quantitative details depend on the specific choice for the path-knowledge function  $P(\mathrm{diag}\varrho)$  and the induced interference-strength measure  $V(\mathrm{offdiag}\varrho)$ .

# 3. Two-Path Interferometers: Qubits

In Sec. 2, we have emphasized consistently, and somewhat pedantically, that the various path-knowledge functions  $P(\mathrm{diag}\varrho)$  involve only the diagonal elements of  $\varrho$ , and the corresponding interference-strength measures  $V(\mathrm{offdiag}\varrho)$  involve only the off-diagonal elements. But from now on, we shall simplify the notation and simply write  $P(\varrho)$  and  $V(\varrho)$ .

For a first illustration, and to make contact with familiar notions, we now consider the particularly simple situation of two-path interferometers. Then, the interfering object constitutes a binary quantum alternative, or qubit. The familiar expressions for the predictability  $\mathcal{P}$  and visibility  $\mathcal{V}$ ,

$$
\mathcal {P} = \left| \varrho_ {1 1} - \varrho_ {2 2} \right|, \quad \mathcal {V} = 2 \left| \varrho_ {1 2} \right|, \tag {30}
$$

are quite simply related to the elements of the  $2 \times 2$  density matrix,

$$
\varrho_ {\text {b i t}} = \left( \begin{array}{c c} \varrho_ {1 1} & \varrho_ {1 2} \\ \varrho_ {2 1} & \varrho_ {2 2} \end{array} \right), \tag {31}
$$

and the basic inequality (1) is an immediate consequence of the normalization of  $\varrho_{\mathrm{bit}}$  to unit trace  $(\varrho_{11} + \varrho_{22} = 1)$  and its positivity  $(\varrho_{12}\varrho_{21}\leq \varrho_{11}\varrho_{22})$

The  $n = 2$  versions of the path-knowledge measures introduced in Sec. 2.3 are simple monotonic functions of the predictability,

$$
P _ {\mathrm {b e t}} = P _ {\mathrm {p u r}} = \mathcal {P},
$$

$$
P _ {\text {e n t}} = \frac {1}{\log 4} \left[ (1 + \mathcal {P}) \log (1 + \mathcal {P}) + (1 - \mathcal {P}) \log (1 - \mathcal {P}) \right], \tag {32}
$$

and the implied interference-strength measures of Sec. 2.4 are the same functions of the visibility,

$$
V _ {\mathrm {b e t}} = V _ {\mathrm {p u r}} = \mathcal {V},
$$

$$
V _ {\text {e n t}} = \frac {1}{\log 4} \left[ (1 + \mathcal {V}) \log (1 + \mathcal {V}) + (1 - \mathcal {V}) \log (1 - \mathcal {V}) \right]. \tag {33}
$$

For each of these  $P, V$  pairs, pure states maximize the value of  $P$  for given  $V$ , and the value of  $V$  for given  $P$ . This observation is an immediate consequence of (1), where the equal sign applies to pure states.

To trace the border curve that connects  $(P,V) = (1,0)$  with  $(P,V) = (0,1)$ , it is quite sufficient to consider the projector matrices

$$
\varrho_ {\text {b i t , p u r e}} = \binom {\cos \vartheta} {\sin \vartheta} (\cos \vartheta , \sin \vartheta) \quad \text {w i t h} 0 \leq \vartheta \leq \frac {1}{4} \pi \tag {34}
$$

because any other pure-state density matrix differs from one of these  $\varrho_{\mathrm{bit,pures}}$  at most by a permutation and a phase transformation, which are irrelevant in the present context. For both the "bet" pair and the "pur" pair, the border curve is the quarter circle labeled a in Fig. 2. For the "ent" pair, the border is drawn by the concave curve b, which appears to be at odds with the convexity of  $P_{\mathrm{ent}}$  and  $V_{\mathrm{ent}}$  but in fact, is not.

![](images/fb93ebf7d558f5a968d0bcc576c8ddff9966c018924eeaea8cd604a849afe9d1.jpg)  
Fig. 2. Possible values for the path-knowledge measure  $P$  and the interference-strength measure  $V$  in two-path interferometers. Curve a is the quarter-circle border line for  $(P, V) = (P_{\mathrm{bet}}, V_{\mathrm{bet}})$  and  $(P, V) = (P_{\mathrm{pur}}, V_{\mathrm{pur}})$ , curve b is the border line for  $(P, V) = (P_{\mathrm{ent}}, V_{\mathrm{ent}})$ . Pure-state values are on the respective border curves, mixed-state values are inside the area with corners at  $(P, V) = (0, 0)$ ,  $(P, V) = (1, 0)$ , and  $(P, V) = (0, 1)$ . The shaded rectangle has the top-right corner on curve b; see text.

To justify this assertion, we consider the qubit in an arbitrary mixed state, so that

$$
\varrho_ {1 1} \varrho_ {2 2} > 0 \quad \text {a n d} \quad \varrho_ {1 2} = \varepsilon \sqrt {\varrho_ {1 1} \varrho_ {2 2}} \quad \text {w i t h} | \varepsilon | <   1 \tag {35}
$$

in Eq. (31). Now, we write  $\varepsilon = |\varepsilon | \mathrm{e}^{\mathrm{i}\alpha}$  and define  $\lambda = (1 + |\varepsilon|)/2$ . Then

$$
\begin{array}{l} \varrho_ {\mathrm {b i t}} = \lambda \left( \begin{array}{c c} \varrho_ {1 1} & \mathrm {e} ^ {\mathrm {i} \alpha} \sqrt {\varrho_ {1 1} \varrho_ {2 2}} \\ \mathrm {e} ^ {- \mathrm {i} \alpha} \sqrt {\varrho_ {1 1} \varrho_ {2 2}} & \varrho_ {2 2} \end{array} \right) + (1 - \lambda) \left( \begin{array}{c c} \varrho_ {1 1} & - \mathrm {e} ^ {\mathrm {i} \alpha} \sqrt {\varrho_ {1 1} \varrho_ {2 2}} \\ - \mathrm {e} ^ {- \mathrm {i} \alpha} \sqrt {\varrho_ {1 1} \varrho_ {2 2}} & \varrho_ {2 2} \end{array} \right) \\ \equiv \lambda \varrho_ {\mathrm {b i t}} ^ {(1)} + (1 - \lambda) \varrho_ {\mathrm {b i t}} ^ {(2)}. \tag {36} \\ \end{array}
$$

The two pure-state density matrices thus introduced,  $\varrho_{\mathrm{bit}}^{(1)}$  and  $\varrho_{\mathrm{bit}}^{(2)}$ , have the same predictability and visibility, namely  $\mathcal{P} = \left|\varrho_{11} - \varrho_{22}\right|$  and  $\mathcal{V} = 2\sqrt{\varrho_{11}\varrho_{22}}$ . Therefore, they also have the same  $P,V$  pair of values, irrespective of whether we chose the "bet" pair, or the "pur" pair, or the "ent" pair. The convexity of  $P(\varrho)$  and  $V(\varrho)$  then implies

$$
P \left(\varrho_ {\text {b i t}}\right) \leq P ^ {(1, 2)}, \quad V \left(\varrho_ {\text {b i t}}\right) \leq V ^ {(1, 2)}, \tag {37}
$$

where  $P^{(1,2)}$  and  $V^{(1,2)}$  are the common values of  $\varrho_{\mathrm{bit}}^{(1)}$  and  $\varrho_{\mathrm{bit}}^{(2)}$ . This says that, in Fig. 2, the point  $\left(P(\varrho_{\mathrm{bit}}), V(\varrho_{\mathrm{bit}})\right)$  is inside the rectangle with  $0 \leq P \leq P^{(1,2)}$ ,  $0 \leq V \leq V^{(1,2)}$ . For an exemplary pair  $P^{(1,2)}, V^{(1,2)}$  on curve  $\mathsf{b}$ , this rectangle is shaded in Fig. 2. Clearly, it is wholly inside the area bounded by the axes and curve  $\mathsf{b}$ .

# 4. Three-Path Interferometers: Qutrits

Somewhat more interesting than two-path interferometers are three-path interferometers, in which the interfering object is a ternary quantum alternative, or  $qutrit$ .<sup>h</sup> Here we have a  $3 \times 3$  density matrix

$$
\varrho_ {\text {t r i t}} = \left( \begin{array}{c c c} \varrho_ {1 1} & \varrho_ {1 2} & \varrho_ {1 3} \\ \varrho_ {2 1} & \varrho_ {2 2} & \varrho_ {2 3} \\ \varrho_ {3 1} & \varrho_ {3 2} & \varrho_ {3 3} \end{array} \right) \tag {38}
$$

that is normalized to unit trace  $(\varrho_{11} + \varrho_{22} + \varrho_{33} = 1)$  and is positive, so that the restrictions

$$
\operatorname {t r} \left\{\varrho_ {\text {t r i t}} ^ {2} \right\} \leq 1, \quad \det  \left\{\varrho_ {\text {t r i t}} \right\} \geq 0 \tag {39}
$$

apply. Since phase transformations,

$$
\varrho_ {j k} \rightarrow \mathrm {e} ^ {\mathrm {i} \left(\varphi_ {j} - \varphi_ {k}\right)} \varrho_ {j k} \tag {40}
$$

turn a given  $\varrho_{\mathrm{trit}}$  into an equivalent one, we can adjust the complex phases of the off-diagonal elements such that

$$
\varrho_ {1 2} = \left| \varrho_ {1 2} \right| \mathrm {e} ^ {\frac {1}{3} \mathrm {i} \theta}, \quad \varrho_ {2 3} = \left| \varrho_ {2 3} \right| \mathrm {e} ^ {\frac {1}{3} \mathrm {i} \theta}, \quad \varrho_ {3 1} = \left| \varrho_ {3 1} \right| \mathrm {e} ^ {\frac {1}{3} \mathrm {i} \theta}, \tag {41}
$$

with a common phase factor  $\exp (\mathrm{i}\theta /3)$  that, for the given off-diagonal elements, is determined by the phase-invariant product

$$
\varrho_ {1 2} \varrho_ {2 3} \varrho_ {3 1} = \left| \varrho_ {1 2} \varrho_ {2 3} \varrho_ {3 1} \right| \mathrm {e} ^ {\mathrm {i} \theta}. \tag {42}
$$

With the convention that  $\theta = 0$  if  $\varrho_{12}\varrho_{23}\varrho_{31} = 0$  and  $-\pi < \theta \leq \pi$  otherwise, the value of  $\theta$  is unique.

For  $n = 3$ , there is essentially only one complex number in the set of Eq. (13), namely  $z_{1} = z_{2}^{*} \equiv z$ , explicitly given by

$$
z = q \varrho_ {1 1} + q ^ {2} \varrho_ {2 2} + \varrho_ {3 3}, \tag {43}
$$

where

$$
q \equiv \mathrm {e} ^ {\mathrm {i} 2 \pi / 3} = \frac {- 1 + \mathrm {i} \sqrt {3}}{2} \tag {44}
$$

is the basic cubic root of unity, for which

$$
q ^ {3} = 1, \quad q ^ {2} = q ^ {*} = q ^ {- 1}, \quad 1 + q + q ^ {2} = 0 \tag {45}
$$

are noteworthy identities. One can regard  $z$  as the average of  $q$ ,  $q^2$  and  $q^3 = 1$  that refers to the weights  $\varrho_{11}$ ,  $\varrho_{22}$ ,  $\varrho_{33}$ , respectively. Accordingly, when represented as points in Gauss's complex plane, the possible values of  $z$  are inside the equilateral triangle that has its corners at  $1$ ,  $q$ , and  $q^2$ .

The identities (45) are used, for example, when expressing the diagonal elements of  $\varrho_{\mathrm{trit}}$  in terms of  $z$ ,

$$
\left. \begin{array}{l} \varrho_ {1 1} = \frac {1}{3} \left(1 + q ^ {2} z + q z ^ {*}\right) \\ \varrho_ {2 2} = \frac {1}{3} \left(1 + q z + q ^ {2} z ^ {*}\right) \\ \varrho_ {3 3} = \frac {1}{3} \left(1 + z + z ^ {*}\right) \end{array} \right\} \quad \text {o r} \quad \varrho_ {k k} = \frac {1}{3} + \frac {2}{3} \operatorname {R e} \left(q ^ {- k} z\right). \tag {46}
$$

And, as a basic check of consistency, we note that  $\operatorname{tr}\{\varrho_{\mathrm{trit}}\} = 1$  is immediate.

Similarly, the diagonal elements  $\tilde{\varrho}_{mm}$  of the Fourier transformed density matrix  $\tilde{\varrho}_{\mathrm{trit}} = F\varrho_{\mathrm{trit}}F^{\dagger}$  can be expressed in terms of the corresponding complex number

$$
Z = \mathrm {e} ^ {\mathrm {i} \varphi_ {1}} \varrho_ {1 2} \mathrm {e} ^ {- \mathrm {i} \varphi_ {2}} + \mathrm {e} ^ {\mathrm {i} \varphi_ {2}} \varrho_ {2 3} \mathrm {e} ^ {- \mathrm {i} \varphi_ {3}} + \mathrm {e} ^ {\mathrm {i} \varphi_ {3}} \varrho_ {3 1} \mathrm {e} ^ {- \mathrm {i} \varphi_ {1}}, \tag {47}
$$

where the phases  $\varphi_{j}$  are those of Eqs. (5) and (7). Explicitly, we have

$$
\tilde {\varrho} _ {m m} = \frac {1}{3} + \frac {2}{3} \operatorname {R e} (q ^ {- m} Z) \tag {48}
$$

as the analog of (46).

# 4.1. Pure qutrit states

The generic form of the density matrix for a pure qutrit state is

$$
\varrho_ {\text {t r i t , p u r e}} = \left( \begin{array}{c c c} p _ {1} & \sqrt {p _ {1} p _ {2}} & \sqrt {p _ {1} p _ {3}} \\ \sqrt {p _ {2} p _ {1}} & p _ {2} & \sqrt {p _ {2} p _ {3}} \\ \sqrt {p _ {3} p _ {1}} & \sqrt {p _ {3} p _ {2}} & p _ {3} \end{array} \right) = \binom {\sqrt {p _ {1}}} {\sqrt {p _ {2}}} (\sqrt {p _ {1}}, \sqrt {p _ {2}}, \sqrt {p _ {3}}) \tag {49}
$$

with  $p_1 \geq p_2 \geq p_3 \geq 0$  by convention and  $p_1 + p_2 + p_3 = 1$  by normalization. There are four families of pure states that are of particular importance, characterized by

Family Ia:  $p_2 = p_3$

Family Ib:  $(p_1 - p_3)^2 + 3p_2 = 1$  Family II:

Family II:  $p_1 = p_2$ ;

Family III:  $p_3 = 0$ .

Families Ia and Ib have the states of full path knowledge ( $p_1 = 1$ ,  $p_2 = p_3 = 0$ ) and of full interference strength ( $p_1 = p_2 = p_3 = 1/3$ ) as limiting cases. The latter is also a member of Family II, whereas the former is in Family III. The respective other limit of  $p_1 = p_2 = 1/2$ ,  $p_3 = 0$ , is a common member of Families II and III. These matters are summarized by the schematic diagram

$$
\begin{array}{c} \left[ p _ {1}, p _ {2}, p _ {3} \right] = \left[ \frac {1}{3}, \frac {1}{3}, \frac {1}{3} \right] \\ P = 0, V = 1 \\ \text {I a o r I b} \\ \left[ p _ {1}, p _ {2}, p _ {3} \right] = \left[ \frac {1}{2}, \frac {1}{2}, 0 \right] \\ P <   1, V <   1 \end{array} \tag {51}
$$

which shows how the families (50) interpolate between the particular limiting pure states.

In Fig. 3, the families of (50) trace out the borders in the  $P, V$  diagram within which the  $P, V$  values of all pure qutrit states are located. Despite the obvious differences, all four plots have certain basic features in common: there is a smooth outer border, and the inner border consists of two smooth pieces with a cusp where they are joined. Note in particular that, in marked contrast to the two-path case, not all pure states give an optimal compromise between  $P$  and  $V$ , only the ones on the outer border achieve this.

The cusp for the pure state with  $p_1 = p_2 = 1/2$ ,  $p_3 = 0$ , the common state of families II and III, is at

$$
(P, V) = \left\{ \begin{array}{l} \left(\frac {1}{4}, \frac {1}{2}\right) \text {f o r t h e o n e - g u e s s b e t o f F i g . 3 (a)}, \\ \left(\frac {1}{2}, \frac {1}{\sqrt {3}}\right) \text {f o r t h e l i n e a r - g u e s s b e t o f F i g . 3 (b)}, \\ \left(\frac {1}{2}, \frac {1}{2}\right) \text {f o r t h e p u r i t y m e a s u r e o f F i g . 3 (c)}, \\ \left(1 - \log_ {3} 2, \frac {1}{3} \log_ {3} 2\right) \text {f o r t h e e n t r o p i c m e a s u r e o f F i g . 3 (d)}. \end{array} \right. \tag {52}
$$

![](images/6ebae496547d355c1b87c2c2be378d3e8b1b2c6a931f38d868a72fa1d4a4bb2e.jpg)

![](images/2696869d9b0dbe2a480fc1a6283c357ad1dcd9ee4ecf949024880e50dca243dc.jpg)

![](images/ce29d0cb4a444663c576c9ac50a11e2687a839ebf3fd96a94fe36acf6d0777c0.jpg)  
(a)  
(c)

![](images/e86948ca08c80fb402b3431151d3bd282d7e122bed1171db40581e5200bad74f.jpg)  
(b)  
Fig. 3. The  $P, V$  values of all pure qutrit states are located in the shaded areas or on the solid lines enclosing them. The four plots refer to quantifying path knowledge (a) by the one-guess bet, (b) by the linear bet, (c) by the purity measure, and (d) by the entropic measure. In all cases, the inner borders are traced out by families II and III of (51), whereas family Ia resides on the outer border for (a), (c), and (d) but not for the linear-bet case (b), for which family Ib makes up the outer border.  
(d)

The outer border is formed by family Ia, except for the linear-guess bet of Fig. 3(b) where the state of family Ib resides on the outer border. We now proceed to take a look at the various measures for the path knowledge and the implied measures for the interference strength, in order to justify these remarks.

# 4.1.1. One-guess bet

The path knowledge associated with the one-guess bet, see (19), is

$$
P _ {\text {b e t}} ^ {(1 \text {g u e s s})} = \frac {3}{2} p _ {1} - \frac {1}{2}, \tag {53}
$$

and the corresponding measure for the interference strength is

$$
V _ {\text {b e t}} ^ {(1 \text {g u e s s})} = \sqrt {p _ {1} p _ {2}} + \sqrt {p _ {2} p _ {3}} + \sqrt {p _ {3} p _ {1}}, \tag {54}
$$

as the maximization required by Eq. (28) is an optimization of the phase factors in Eq. (47), which is easily carried out. We find the borders by maximizing and minimizing  $V_{\mathrm{bet}}^{(1 \text{ guess})}$  for a given value of  $P_{\mathrm{bet}}^{(1 \text{ guess})}$ , that is:

$$
\begin{array}{l} p _ {1} \text {g i v e n}; p _ {2} \text {i n t h e r a n g e} \frac {1}{2} (1 - p _ {1}) \leq p _ {2} \leq \min  \{p _ {1}, 1 - p _ {1} \}; \\ p _ {3} = 1 - p _ {1} - p _ {2}; \text {t h e n} \\ \frac {\partial}{\partial p _ {2}} V _ {\text {b e t}} ^ {(1 \text {g u e s s})} = - \frac {(\sqrt {p _ {2}} - \sqrt {p _ {3}}) (\sqrt {p _ {1}} + \sqrt {p _ {2}} + \sqrt {p _ {3}})}{2 \sqrt {p _ {2} p _ {3}}} \leq 0, \tag {55} \\ \end{array}
$$

so that  $V_{\mathrm{bet}}^{(1 \text{ guess})}$  is largest when  $p_2$  is smallest, and smallest when  $p_2$  is largest.

Therefore, we have  $p_2 = p_3$  on the outer border (family Ia), and  $p_1 = p_2$  on the inner border if  $p_1 \leq 1/2$  (family II) as well as  $p_2 = 1 - p_1$  on the inner border if  $p_1 \geq 1/2$  (family III). In geometrical terms, the outer border is (an arc of) the ellipse

$$
2 \left(P + V - \frac {1}{2}\right) ^ {2} + (P - V) ^ {2} = \frac {3}{2}, \tag {56}
$$

with the center at  $P = V = 1/4$ , the major axis of length  $\sqrt{3}$  on the line  $V + P = 1/2$  and the minor axis of length  $\sqrt{3/2}$  on the line  $V = P$ .

# 4.1.2. Linear bet

According to Eq. (20), we have the path knowledge

$$
P _ {\text {b e t}} ^ {(\text {l i n})} = p _ {1} - p _ {3} \tag {57}
$$

for the linear betting strategy. Several steps are needed to find the corresponding  $V_{\mathrm{bet}}^{(\mathrm{lin})}$ . First, we recall the remark after Eq. (9) and set  $\varphi_2 = 0$  in

$$
Z = \sqrt {p _ {1} p _ {2}} \mathrm {e} ^ {\mathrm {i} \varphi_ {1}} + \sqrt {p _ {2} p _ {3}} \mathrm {e} ^ {- \mathrm {i} \varphi_ {3}} + \sqrt {p _ {3} p _ {1}} \mathrm {e} ^ {\mathrm {i} (\varphi_ {3} - \varphi_ {1})}. \tag {58}
$$

Second, we note that the replacements  $\varphi_{1}\rightarrow \varphi_{1} + 2\pi /3$ $\varphi_3\to \varphi_3 - 2\pi /3$  amount to  $Z\to qZ$  and thus permute the  $\tilde{\varrho}_{mm}$ s of Eq. (48) cyclically. Therefore, it is

permissible to assume that  $\left|\tilde{\varrho}_{11} - \tilde{\varrho}_{22}\right|$  is the difference of the largest and the smallest of the  $\tilde{\varrho}_{mm}$ , so that

$$
\begin{array}{l} V _ {\mathrm {b e t}} ^ {(\mathrm {l i n})} = \frac {2}{\sqrt {3}} \max  _ {\varphi_ {1}, \varphi_ {3}} | \operatorname {I m} (Z) | \\ = \frac {2}{\sqrt {3}} \max  _ {\varphi_ {1}, \varphi_ {3}} \left\{\sqrt {p _ {1} p _ {2}} \sin \varphi_ {1} - \sqrt {p _ {2} p _ {3}} \sin \varphi_ {3} + \sqrt {p _ {3} p _ {1}} \sin (\varphi_ {3} - \varphi_ {1}) \right\}. \tag {59} \\ \end{array}
$$

Third, we perform the required maximization over  $\varphi_{1}$  and  $\varphi_{3}$  and arrive at

$$
\begin{array}{l} V _ {\mathrm {b e t}} ^ {(\mathrm {l i n})} = \frac {2}{\sqrt {3}} \sqrt {p _ {1} p _ {2} + p _ {2} p _ {3} + p _ {3} p _ {1} + 2 y + 3 y ^ {2}}, \\ \text {w h e r e} y \geq 0 \text {s o l v e s} 2 y ^ {3} + y ^ {2} = p _ {1} p _ {2} p _ {3}. \tag {60} \\ \end{array}
$$

If an explicit expression is needed for  $y$ , then

$$
y = \frac {\cos (3 \vartheta)}{6 \cos \vartheta} \quad \text {w i t h} \cos (3 \vartheta) = \sqrt {2 7 p _ {1} p _ {2} p _ {3}} \tag {61}
$$

is perhaps the most convenient.

We now search for the largest value of  $V_{\mathrm{bet}}^{\mathrm{(lin)}}$  for a given value of  $P_{\mathrm{bet}}^{\mathrm{(lin)}}$ , where the difference  $P \equiv p_1 - p_3$  is fixed. The permissible values of  $p_2$  are then in the range

$$
\frac {1}{3} (1 - P) \leq p _ {2} \leq \left\{ \begin{array}{l l} \frac {1}{3} (1 + P) & \text {f o r} P \leq \frac {1}{2}, \\ 1 - P & \text {f o r} P \geq \frac {1}{2}. \end{array} \right. \tag {62}
$$

If  $p_2$  equals its lower bound, the state is in family Ia; at the upper bounds, we have family II or III, respectively.

We note that  $\mathrm{d}p_{1} = \mathrm{d}p_{3} = -\mathrm{d}p_{2} / 2$  , with the consequence

$$
\frac {\mathrm {d}}{\mathrm {d} p _ {2}} V _ {\text {b e t}} ^ {(\text {l i n}) ^ {2}} = \frac {1}{3 y} \left[ (1 - 3 p _ {2}) (1 - p _ {2} + 2 y) - P ^ {2} \right]. \tag {63}
$$

At the bounds on  $p_2$  in (62), we thus have

$$
\frac {\mathrm {d}}{\mathrm {d} p _ {2}} V _ {\text {b e t}} ^ {(\text {l i n})} > 0 \text {a t}
$$

$$
\begin{array}{l} \mathrm {d} p _ {2} \\ \text {a n d} \frac {\mathrm {d}}{\mathrm {d} p _ {2}} V _ {\text {b e t}} ^ {(\text {l i n})} <   0 \text {a t t h e u p p e r b o u n d s .} \end{array} \tag {64}
$$

Therefore,  $V_{\mathrm{bet}}^{(\mathrm{lin})}$  has local minima for families Ia, II and III. The smaller value is always obtained for the upper bounds in (62), as one can verify after first observing that

$$
\text {l o w e r b o u n d :} \quad p _ {1} = \frac {1}{3} (1 + 2 P), p _ {2} = p _ {3} = \frac {1}{3} (1 - P),
$$

$$
2 y ^ {2} + p _ {1} y = p _ {1} p _ {3};
$$

$$
\begin{array}{l} \text {u p p e r b o u n d} P \leq \frac {1}{2}: \quad p _ {1} = p _ {2} = \frac {1}{3} (1 + P), \quad p _ {3} = \frac {1}{3} (1 - 2 P), \tag {65} \\ 2 y ^ {2} + p _ {3} y = p _ {1} p _ {3}; \\ \end{array}
$$

$$
\text {u p p e r b o u n d f o r} P \geq \frac {1}{2}: \quad p _ {1} = P, p _ {2} = 1 - P, p _ {3} = 0, y = 0;
$$

so that families II and III trace out the inner borders, indeed.

Further, Eq. (63) implies that  $V_{\mathrm{bet}}^{(\mathrm{lin})}$  is maximal at the intermediate  $p_2$  value that obeys

$$
(1 - 3 p _ {2}) (1 - p _ {2} + 2 y) = P ^ {2} \tag {66}
$$

with  $y$  from Eq. (60). Therefore, the pure state with

$$
p _ {1} = \frac {1}{6} (1 + P) (2 + P), \quad p _ {2} = \frac {1}{3} (1 - P ^ {2}), \tag {67}
$$

$$
p _ {3} = \frac {1}{6} (1 - P) (2 - P), \quad y = \frac {1}{6} (1 - P ^ {2}),
$$

maximizes  $V_{\mathrm{bet}}^{\mathrm{(lin)}}$  for given  $P = P_{\mathrm{bet}}^{\mathrm{(lin)}}$ . Indeed, the outer border of Fig. 3(b) is traced by family Ib of (50). And since  $V_{\mathrm{bet}}^{\mathrm{(lin)}} = \sqrt{1 - P^2}$  for the pure states specified by (67), the outer border is the quarter circle

$$
P ^ {2} + V ^ {2} = 1. \tag {68}
$$

# 4.1.3. Purity

It is a matter of inspection to verify that the path-knowledge function of Sec. 2.3.2 is given by the modulus of  $z$ ,

$$
P _ {\text {p u r}} = | z |. \tag {69}
$$

It follows that the induced interference-strength measure is

$$
V _ {\text {p u r}} = \max  _ {\varphi_ {j}} \left\{| Z | \right\} = \left| \varrho_ {1 2} \right| + \left| \varrho_ {2 3} \right| + \left| \varrho_ {3 1} \right|, \tag {70}
$$

because the maximal value of  $|Z|$  is obtained when the phases  $\varphi_j$  are just the ones that exhibit the common phase factor  $\exp(\mathrm{i}\theta / 3)$  of (41). These equations apply to pure or mixed states.

We note that, although  $P_{\mathrm{pur}}$  is Durr's path knowledge function of Ref. 26, the corresponding interference strength  $V_{\mathrm{pur}}$  of Eq. (70) is not the one suggested by Durr, which is

$$
\bar {V} _ {\text {p u r}} = \sqrt {3 \left(\left| \varrho_ {1 2} \right| ^ {2} + \left| \varrho_ {2 3} \right| ^ {2} + \left| \varrho_ {3 1} \right| ^ {2}\right)}. \tag {71}
$$

Therefore, Durr's pair  $P_{\mathrm{pur}}, \overline{V}_{\mathrm{pur}}$  does not fit into the general strategy of Sec. 2. Rather than linking  $V$  to  $P$  by Eq. (28), his choice is such that

$$
P ^ {2} + V ^ {2} = \frac {3}{2} \operatorname {t r} \left\{\varrho_ {\mathrm {t r i t}} ^ {2} \right\} - \frac {1}{2} \leq 1 \tag {72}
$$

by construction. The equal sign holds for all pure states, as it does in Eq. (1).

For pure states, Eqs. (69) and (70) give

$$
P _ {\text {p u r}} = \sqrt {1 - 3 \left(p _ {1} p _ {2} + p _ {2} p _ {3} + p _ {3} p _ {1}\right)}, \tag {73}
$$

$$
V _ {\mathrm {p u r}} = \sqrt {p _ {1} p _ {2}} + \sqrt {p _ {2} p _ {3}} + \sqrt {p _ {3} p _ {1}}.
$$

We note the coincidence that  $P_{\mathrm{pur}} = P_{\mathrm{bet}}^{(1 \text{ guess})}$  and  $V_{\mathrm{pur}} = V_{\mathrm{bet}}^{(1 \text{ guess})}$  on the outer border, traced out by family Ia, so that the outer border for the purity measures is also the ellipse (56) of the one-guess bet.

# 4.1.4. Entropy

For the pure qutrit states of (49), the entropic measures for path knowledge and interference strength are

$$
P _ {\text {e n t}} = \frac {1}{\log 3} \left[ p _ {1} \log \left(3 p _ {1}\right) + p _ {2} \log \left(3 p _ {2}\right) + p _ {3} \log \left(3 p _ {3}\right) \right] \tag {74}
$$

and

$$
V _ {\text {e n t}} = \frac {1}{\log 3} \left[ \tilde {p} _ {1} \log \left(3 \tilde {p} _ {1}\right) + \tilde {p} _ {2} \log \left(3 \tilde {p} _ {2}\right) + \tilde {p} _ {3} \log \left(3 \tilde {p} _ {3}\right) \right] \tag {75}
$$

with

$$
\tilde {p} _ {1} = \frac {1}{3} + \frac {2}{3} \left(\sqrt {p _ {1} p _ {2}} + \sqrt {p _ {2} p _ {3}} + \sqrt {p _ {3} p _ {1}}\right), \tag {76}
$$

$$
\tilde {p} _ {2} = \tilde {p} _ {3} = \frac {1}{3} - \frac {1}{3} \left(\sqrt {p _ {1} p _ {2}} + \sqrt {p _ {2} p _ {3}} + \sqrt {p _ {3} p _ {1}}\right).
$$

It turns out that, here too, the states of families II and III form the inner borders, while the states of family Ia make up the outer border once more. Accordingly,

$$
P _ {\mathrm {e n t}} = \frac {1}{3 \log 3} \left[ (1 + 2 u) \log (1 + 2 u) + 2 (1 - u) \log (1 - u) \right],
$$

$$
V _ {\text {e n t}} = \frac {1}{3 \log 3} \left[ (1 + 2 v) \log (1 + 2 v) + 2 (1 - v) \log (1 - v) \right], \tag {77}
$$

$$
\mathrm {w i t h} (u - v) ^ {2} + 2 \left(u + v - \frac {1}{2}\right) ^ {2} = \frac {3}{2} \mathrm {f o r} 0 \leq u, v \leq 1
$$

is a convenient parameterization of the outer border in Fig. 3(d). Note that the parameters  $u, v$  have values on the ellipse of (56).

# 4.2. Outer borders

The outer borders found for the four cases that are examined in Secs. 4.1.1-4.1.4 are shown in Fig. 4. The possible values for  $P$  and  $V$  are restricted to the area bounded by the respective outer border and the axes. Of the four choices, the smallest area is that for the entropic quantities, and the largest area is the quarter-circle of the linear bet.

But this is not the absolutely largest area. It is indeed possible to have permissible  $P, V$  pairs almost everywhere inside the square  $0 \leq P, V \leq 1$ . To demonstrate

![](images/8ab248d80d29f3f2d3711adff461584fcf36d3b81729536f38cfaef8f45c2a91.jpg)  
Fig. 4. The outer borders of the shaded areas in Fig. 3. For Figs. 3(a) and 3(c) we have curve a&c, the ellipse of Eq. (56). Curve b is the circle of Eq. (68), the outer border in Fig. 3(b). For the entropic measures of Fig. 3(d), the  $P, V$  values of (77) are shown as curve d.

this point, we consider a general bet, for which

$$
P _ {\text {b e t}} = p _ {1} + g _ {2} p _ {2} - (1 + g _ {2}) p _ {3} \quad \text {w i t h} 1 > g _ {2} \geq - \frac {1}{2}, \tag {78}
$$

and the pure qutrit state specified by

$$
\varrho_ {\text {t r i t}} = \frac {1}{2} \left( \begin{array}{c c c} 1 & - 1 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right), \tag {79}
$$

so that  $p_1 = p_2 = 1/2$ ,  $p_3 = 0$  and

$$
P _ {\text {b e t}} = \frac {1}{2} (1 + g _ {2}). \tag {80}
$$

For either one of the two  $3 \times 3$  Fourier matrices in (11) we have  $F\varrho_{\mathrm{trit}}F^{\dagger} = \varrho_{\mathrm{trit}}$ , implying

$$
\frac {1}{2} \left(1 + g _ {2}\right) \leq V _ {\mathrm {b e t}} <   1. \tag {81}
$$

By now choosing  $g_{2}$  sufficiently close to, but less than unity, we can push  $(P_{\mathrm{bet}}, V_{\mathrm{bet}})$  as close to the corner  $(P, V) = (1, 1)$  as we wish. As a consequence of criterion (14a), the limiting value  $g_{2} = 1$  is not permitted in (16); if it were, it would realize a bet on two of the three paths versus the third. In practice, however, a  $g_{2}$  value that is rather

close to 1 will implement such a 2-of-3 bet quite well, and then the two dominating paths can interfere with almost full strength, even when almost perfect 2-of-3 path knowledge is at hand.

For the pure qutrit states of (49), we have

$$
P _ {\mathrm {b e t}} \rightarrow 1 - 3 p _ {3}
$$

$$
\text {a n d} V _ {\mathrm {b e t}} \rightarrow \left\{\begin{array}{c l}1&\text {i f} \sqrt {p _ {1}} \leq \sqrt {p _ {2}} + \sqrt {p _ {3}},\\2 \left(\sqrt {p _ {1} p _ {2}} - \sqrt {p _ {2} p _ {3}} + \sqrt {p _ {3} p _ {1}}\right)&\text {i f} \sqrt {p _ {1}} \geq \sqrt {p _ {2}} + \sqrt {p _ {3}},\end{array}\right. \tag {82}
$$

in the limit  $g_2 \to 1$ . Clearly, all states with  $p_1 = p_2$ , those of family II in (50), have  $V_{\mathrm{bet}} = 1$  in this limit, so that the outer border is given by

$$
\max  \{P, V \} = 1, \tag {83}
$$

and the whole area of the square  $0 \leq P, V \leq 1$  is covered.

# 5. Four-Path Interferometers: Ququarts

In an interferometer with four paths, the interfering object is a quaternary quantum alternative or ququart. As a consequence of the parameter  $t$  in the  $4 \times 4$  Fourier matrix (12) and the nonequivalence of column permutations and row permutations, the analysis of four-path interferometers is much more involved than that of interferometers with two or three paths, and has not been carried out in full as yet. We shall therefore be brief and only discuss two issues: two conjectures, one disproven by a counter example and the other undecided, and a recent analysis of a four-path interferometer with the tools of two-path interferometry.

# 5.1. Linear bet: One conjecture rejected, another proposed

Whereas the border lines in the  $P, V$ -diagram are different, as a rule, for two-path and three-path interferometers, it is remarkable that we have the same quarter-circle border for the linear bet in Figs. 2 and 4. It is tempting to conjecture that the linear bet values of  $(P, V)$  are in the quarter-circle area  $P^2 + V^2 \leq 1$  also in the case of four-path interferometers, or perhaps even quite generally for  $n$ -path interferometers. This conjecture is, however, false as can be demonstrated by the following counter example.[33]

Consider the pure-case  $4 \times 4$  density matrix

$$
\varrho = \left( \begin{array}{l} \sqrt {p _ {4}} \\ \sqrt {p _ {3}} \\ \sqrt {p _ {2}} \\ \sqrt {p _ {1}} \end{array} \right) (\sqrt {p _ {4}}, \sqrt {p _ {3}}, \sqrt {p _ {2}}, \sqrt {p _ {1}}) \tag {84}
$$

with the path probabilities

$$
p _ {1} = \frac {1}{1 0} G ^ {- 4}, \quad p _ {2} = \frac {1}{1 0} G ^ {- 2}, \quad p _ {3} = \frac {1}{1 0} G ^ {2}, \quad p _ {4} = \frac {1}{1 0} G ^ {4}, \tag {85}
$$

where  $G = (\sqrt{5} - 1) / 2$  is the golden ratio. The  $t = 0$  Fourier matrix (12) yields  $\tilde{\varrho} = \varrho$ , so that  $V_{\mathrm{bet}}^{(\mathrm{lin})}(\varrho) \geq P_{\mathrm{bet}}^{(\mathrm{lin})}(\tilde{\varrho}) = P_{\mathrm{bet}}^{(\mathrm{lin})}(\varrho) = \sqrt{5 / 9}$ , and

$$
P _ {\text {b e t}} ^ {(\text {l i n}) ^ {2}} + V _ {\text {b e t}} ^ {(\text {l i n}) ^ {2}} \geq \frac {1 0}{9} > 1 \tag {86}
$$

for this  $\varrho$

There is numerical evidence, but no clear-cut demonstration of the case as yet, that the linear-bet border is traced out by pure states with density matrices of the form (84) with

$$
\sqrt {p _ {1} / p _ {2}} = \sqrt {p _ {3} / p _ {4}} = \mathrm {e} ^ {\vartheta}, \quad \sqrt {p _ {3} / p _ {1}} = \sqrt {p _ {4} / p _ {2}} = \tanh  \frac {\theta}{2}
$$

where  $4\sinh \vartheta \sinh \theta = 1$  (87)

and the optimal Fourier transform being the  $t = 1$  version of Eq. (12). Then we have

$$
\sqrt {\tilde {p} _ {1} / \tilde {p} _ {2}} = \sqrt {\tilde {p} _ {3} / \tilde {p} _ {4}} = \mathrm {e} ^ {\theta}, \quad \sqrt {\tilde {p} _ {3} / \tilde {p} _ {1}} = \sqrt {\tilde {p} _ {4} / \tilde {p} _ {2}} = \tanh  \frac {\vartheta}{2}, \tag {88}
$$

which are reciprocal to the relations in (87), and

$$
P _ {\text {b e t}} ^ {(\text {l i n})} = \frac {1}{3} \tanh  \vartheta + \frac {2}{3} \operatorname {s e c h} \theta , \quad V _ {\text {b e t}} ^ {(\text {l i n})} = \frac {1}{3} \tanh  \theta + \frac {2}{3} \operatorname {s e c h} \vartheta \tag {89}
$$

parametrize the thus conjectured border line. Figure 5 shows that, except for  $(P,V) = (1,0)$  and  $(P,V) = (0,1)$ , all values of (89) have  $P_{\mathrm{bet}}^{(\mathrm{lin})^2} + V_{\mathrm{bet}}^{(\mathrm{lin})^2} > 1$ . The values of (85) and (86) are obtained for  $\sinh \vartheta = \sinh \theta = 1/2$ .

# 5.2.  $4 \neq 2 \times 2$

In a recent interesting series of papers, including Refs. 34-36, there is a claim that one can violate the duality relation (1), thereby "cheating on complementarity" in this manner; see Ref. 34, for instance. Of course, Bohr's Principle of Complementarity, $^{\mathrm{j}}$  the fundamental principle of quantum kinematics, remains untouched: in fact, the authors of Refs. 34-36 are relying on it in their analysis, as all arguments which invoke the quantum formalism do.

![](images/4ebcd289f39fa543f5871f3a2e7301b159a6072879cd60d005fb349a81f3f0bb.jpg)  
Fig. 5. Possible values for the path-knowledge measure  $P$  and the interference-strength measure  $V$  in four-path interferometers. Curve a is the conjectured border line for  $(P, V) = (P_{\mathrm{bet}}^{\mathrm{(lin)}}, V_{\mathrm{bet}}^{\mathrm{(lin)}})$  that is traced out by (89), and curve b is the quarter circle  $P^2 + V^2 = 1$ .

More importantly, the thought experiment in question — a Mach-Zehnder (MZ) set-up traversed by a qubit, so that the spatial binary alternative of the MZ geometry and the internal qubit together make up a ququart — is a four-path interferometer to which the two-path relation (1) does not apply. When applying it nevertheless, by letting the path knowledge refer solely to the arms of the MZ set-up, the actual paths of the four-path interferometer are grouped into two pairs, and we have a 2-of-4 bet, similar to the 2-of-3 bet discussed in Sec. 4.2.

The situation is then that of a limiting four-path bet with  $g_{1} = 1$ ,  $g_{4} = -1$ , and  $1 > g_{2} = -g_{3} \rightarrow 1$ , and it is easy to have both  $P$  and  $V$  close to unity. But this has no bearing on (1) or any other relation for two-path interferometers, and poses no challenge to complementarity.

An analysis of the ququart MZ set-up as a four-path interferometer with the methodology introduced in Sec. 2 would be of great interest. In the scheme proposed in Refs. 34-36, where the particle that traverses the MZ interferometer is endowed with "intraparticle translational-internal entanglement," there are fixed relations between the phases  $\phi_1,\ldots ,\phi_4$  of the four (or possibly more) path amplitudes, and it is unclear how to achieve the full flexibility required in Eq. (28). If the four paths are implemented by having polarized photons in the two arms of a MZ interferometer, the particle mode and the wave mode of Fig. 1 can be realized by known and rather simple tools. $^{38}$

# 6.  $n$ -Path Interferometers: Qunits

In a multi-path interferometer with  $n$  paths, the generic situation of Fig. 1, the interfering object is a  $n$ -fold quantum alternative, or qunit. Little is known about the possible  $(P,V)$  values for qunits. We can only offer some observations about path knowledge measures that solely involve  $p_1$ , and put on record an unproven conjecture about the pair  $(P_{\mathrm{ent}},V_{\mathrm{ent}})$  of entropic measures that is suggested by a pattern observed for qubits and qutrits, and by some numerical evidence.

# 6.1. Entropic measures: A conjecture

The conjecture is this: the border lines for the entropic measures for path knowledge and interference strength are traced out by the pure states whose  $n \times n$  density matrices are of the form

$$
\varrho = \left( \begin{array}{c} \sqrt {p _ {2}} \\ \sqrt {p _ {2}} \\ \vdots \\ \sqrt {p _ {2}} \\ \sqrt {p _ {1}} \end{array} \right) (\sqrt {p _ {2}}, \sqrt {p _ {2}}, \dots , \sqrt {p _ {2}}, \sqrt {p _ {1}}) \quad \text {w i t h} p _ {1} + (n - 1) p _ {2} = 1, \tag {90}
$$

and the optimal Fourier matrix is the standard one of Eqs. (5)-(7) with  $\varphi_{j} = 0$ . Then  $\tilde{\varrho}$  has the same form with  $p_1$  and  $p_2$  replaced by

$$
\tilde {p} _ {1} = \frac {1}{n} \left(\sqrt {p _ {1}} + (n - 1) \sqrt {p _ {2}}\right) ^ {2} \quad \text {a n d} \quad \tilde {p} _ {2} = \frac {1}{n} \left(\sqrt {p _ {1}} - \sqrt {p _ {2}}\right) ^ {2}, \tag {91}
$$

respectively. The identities

$$
n p _ {1} + n \tilde {p} _ {1} - 2 \sqrt {n p _ {1} \tilde {p} _ {1}} = n - 1, \quad n p _ {2} + n \tilde {p} _ {2} + 2 \sqrt {n p _ {2} \tilde {p} _ {2}} = 1 \tag {92}
$$

exhibit the reciprocal nature of the mappings  $(p_1,p_2)\leftrightarrow (\tilde{p}_1,\tilde{p}_2)$

Thus surmising that these pure states are on the border of the  $(P_{\mathrm{ent}}, V_{\mathrm{ent}})$  values in the  $P, V$ -diagram, we obtain the border lines of Fig. 6(a). For moderate  $n$  values, the border lines are very similar to the  $n = 2$  line in Fig. 2 and the  $n = 3$  line in Fig. 4, whereas we get the straight line  $P_{\mathrm{ent}} + V_{\mathrm{ent}} = 1$  in the limit of  $n \to \infty$ .

The conjectured border lines of Fig. 6(a) have the remarkable feature that the area of permissible  $(P_{\mathrm{ent}}, V_{\mathrm{ent}})$  values decreases from  $n = 2$  to  $n = 10$

![](images/7a6e01f3e6dd4f65f8f677197dba0138fdb1a3ba7df402db22ea8349d240f5eb.jpg)  
(a)

![](images/701c6af310106205418aaba90b8c4d84d4a28c5aca5991aa75e9cc1e2970fdc6.jpg)  
(b)  
Fig. 6. Conjectured border lines for the entropic measures for path knowledge and interference strength in multi-path interferometers. The top plot (a) shows the border lines associated with (90) and (91), whereby curve a is for  $n = 2$ , curve b for  $n = 10$ , curve c for  $n = 10^7$ , and curve d for  $n \to \infty$ . The bottom plot (b) shows the symmetric  $P = V$  values for  $n = 2, 3, \ldots, 20$  and confirms that the smallest value is found for  $n = 10$ .

and then increases. This is illustrated by the plot in Fig. 6(b) which shows, for  $n = 2,3,\ldots ,20$ , the symmetric values

$$
P _ {\mathrm {e n t}} = V _ {\mathrm {e n t}} = \log_ {n} \frac {\sqrt {n}}{2} + \frac {1}{\sqrt {n}} \log_ {n} (\sqrt {n} + 1) \tag {93}
$$

that one gets for

$$
p _ {1} = \tilde {p} _ {1} = \frac {\sqrt {n} + 1}{2 \sqrt {n}}, \quad p _ {2} = \tilde {p} _ {2} = \frac {1}{2 \sqrt {n} (\sqrt {n} + 1)}, \tag {94}
$$

with the right-hand side of Eq. (93) equal to 0.394845, 0.394820, and 0.394827 for  $n = 9, 10,$  and 11, respectively. We leave it at that.

# 6.2. Measures based solely on  $p_1 = \max_m \{\varrho_{mm}\}$

In (19), (26) and (27), we encounter path knowledge measures that involve only  $p_1 = \max_m\{\varrho_{mm}\}$ : the measure of the one-bet guess  $P_{\mathrm{bet}}^{(1\mathrm{guess})}$  and the extreme limits  $P_{\mathrm{Ren}}^{(\infty)}$  and  $P_{\mathrm{Ren}}^{(0)}$  of the Rényi-type measures. For these, it is clear that the pure states of (90)-(92) maximize  $V$  for given  $P$ , and  $P$  for given  $V$ .

Another way of writing the first identity in (92),

$$
n \left(p _ {1} + \tilde {p} _ {1} - 1\right) ^ {2} + \frac {n}{n - 1} \left(p _ {1} - \tilde {p} _ {1}\right) ^ {2} = 1, \tag {95}
$$

gives us the border lines for  $P_{\mathrm{bet}}^{(1 \text{ guess})}$  and  $P_{\mathrm{Ren}}^{(\infty)}$ . In the case of the one-guess bet, we have  $P = (np_1 - 1) / (n - 1)$  and  $V = (n\tilde{p}_1 - 1) / (n - 1)$ , and it follows that the border line is an arc of the ellipse

$$
\frac {(n - 1) ^ {2}}{n} \left(P + V - \frac {n - 2}{n - 1}\right) ^ {2} + \frac {n - 1}{n} (P - V) ^ {2} = 1. \tag {96}
$$

As it should, this is the ellipse of Eq. (56) for  $n = 3$ , and the circle  $P^2 + V^2 = 1$  for  $n = 2$ . The ellipse of Eq. (96) is centered at  $P = V = (n - 2) / (2n - 2)$ ; its major axis of length  $\sqrt{2n / (n - 1)}$  is on the line  $V + P = (n - 2) / (n - 1)$ , and the minor axis of length  $\sqrt{2n} / (n - 1)$  is on the line  $P = V$ .

In the case of the Rényi-type measure for  $\lambda \to \infty$ , it is  $P = p_1$  and  $V = \tilde{p}_1$  except when  $p_1 = 1, \tilde{p}_1 = 1/n$  or  $p_1 = 1/n, \tilde{p}_1 = 1$ , and we have the arc with  $P > 1/n$  and  $V > 1/n$  of the ellipse

$$
n (P + V - 1) ^ {2} + \frac {n}{n - 1} (P - V) ^ {2} = 1 \tag {97}
$$

as part of the border line. The straight lines with  $P \leq 1/n$  and  $V = 1$  or  $P = 1$  and  $V \leq 1/n$  complete the border line, but the points on these straight segments are not permitted, except for the corners at  $(P, V) = (1,0)$  and  $(P, V) = (0,1)$ .

In the limit  $n \to \infty$ , the straight line  $P + V = 1$  is the border for  $(P_{\mathrm{bet}}^{(\mathrm{1~guess})}, V_{\mathrm{bet}}^{(\mathrm{1~guess})})$  and  $(P_{\mathrm{Ren}}^{(\infty)}, V_{\mathrm{Ren}}^{(\infty)})$ . The same line is conjectured above for  $(P_{\mathrm{ent}}, V_{\mathrm{ent}})$  for  $n \to \infty$ .

By contrast, matters are quite simple in the  $\lambda \rightarrow 0$  limit of the Rényi-type measures. All permissible values for  $(P_{\mathrm{Ren}}^{(0)}, V_{\mathrm{Ren}}^{(0)})$  have either  $P_{\mathrm{Ren}}^{(0)} = 0$  or  $V_{\mathrm{Ren}}^{(0)} = 0$ .

# 7. Summary

We have presented a systematic way of quantifying path knowledge and interference strength in multi-path interferometers. The quantitative measures for particle aspects (path knowledge) and wave aspects (interference strength) have a clear operational meaning, and are naturally linked to each other. This systematic link, which

exploits general Fourier transformations, distinguishes our approach from earlier attempts.

Since there is no unique procedure for assigning a single number to the path knowledge when there are more than two paths, we have discussed several self-suggesting definitions of the path-knowledge measure  $P$  and the induced interference-strength measure  $V$ . As a consequence of wave-particle duality,  $P = 1$  implies  $V = 0$  and  $V = 1$  implies  $P = 0$  for all choices, but the range of values allowed for the pair  $(P,V)$  depends on the particular choice.

We have illustrated our approach with the familiar example of two-path interferometers and a thorough analysis of three-path interferometers, and have given glimpses at four-path interferometers and general multi-path interferometers. This sets the stage for further studies.

Perhaps the most important step to be taken now is an investigation of the multi-path analog of the transition from predictability to distinguishability in two-path interferometers. We will report from this front in due course.

# Acknowledgments

BGE is grateful for the hospitality extended to him by Christian Miniatura at the Institut Nonlineaire de Nice in 2005 and 2007, where part of this work was carried out. We acknowledge support by A*STAR Temasek Grant 012-104-0040 and by NUS Grant R-144-000-179-112. The Centre for Quantum Technologies is a Research Centre of Excellence funded by the Ministry of Education and the National Research Foundation of Singapore.

# References

1. A. Einstein, Ann. Physik 17 (1905) 132 [English translation in Ref. 39].  
2. N. Bohr, Die Naturwissenschaften 16 (1928) 245, English Version: Nature 121 (1928) 580; the latter is reprinted in Ref. 40.  
3. N. Bohr, Discussions with Einstein on epistemological problems in atomic physics, in Albert Einstein: Philosopher-Scientist, ed. P. A. Schilpp (Library of Living Philosophers, Evanston, 1949) [reprinted in Ref. 40].  
4. C. Held, Die Bohr-Einstein-Debatte (Schoeningh, Paderborn, 1998).  
5. B.-G. Englert and J. A. Bergou, Opt. Commun. 179 (2000) 337.  
6. W. K. Wootters and W. H. Zurek, Phys. Rev. D 19 (1979) 473.  
7. H. Rauch and J. Summhammer, Phys. Lett. A 104 (1984) 44.  
8. R. Glauber, Ann. N. Y. Acad. Sci. 480 (1986) 336.  
9. P. Mittelstaedt, A. Prieur and R. Schieder, Found. Phys. 17 (1987) 891.  
10. D. M. Greenberger and A. Yasin, Phys. Lett. A 128 (1988) 391.  
11. L. Mandel, Opt. Lett. 16 (1991) 1882.  
12. G. Jaeger, A. Shimony and L. Vaidman, Phys. Rev. A 51 (1995) 54.  
13. B.-G. Englert, Phys. Rev. Lett. 77 (1996) 2154.  
14. B.-G. Englert, Z. Naturforsch. 54a (1999) 11.  
15. J. Baldzuhn, E. Mohler and W. Martienssen, Z. Phys. B 77 (1989) 347.  
16. J. Baldzuhn and W. Martienssen, Z. Phys. B 82 (1991) 309.  
17. P. D. D. Schwindt, P. G. Kwiat and B.-G. Englert, Phys. Rev. A 60 (1999) 4285.

18. P. G. Kwiat, P. D. D. Schwindt and B.-G. Englert, What does a quantum eraser erase?, in *Mysteries*, *Puzzles*, and *Paradoxes in Quantum Mechanics*, ed. R. Bonifacio (CP461, The American Institute of Physics, 1999).  
19. A. Trifonov, G. Björk, J. Söderholm and T. Tsegaye, Eur. Phys. J. D 18 (2002) 251.  
20. S. P. Walborn, M. O. T. Cunha, S. Pádua and C. H. Monken, Phys. Rev. A 65 (2002) 033818.  
21. G. J. Pryde, J. L. O'Brien, A. G. White, S. D. Bartlett and T. C. Ralph, Phys. Rev. Lett. 92 (2004) 190402.  
22. J. Summhammer, H. Rauch and D. Tuppinger, Phys. Rev. A 36 (1987) 4447.  
23. S. Durr, T. Nonn and G. Rempe, Nature 395 (1998) 33.  
24. S. Durr, T. Nonn and G. Rempe, Phys. Rev. Lett. 81 (1998) 5705.  
25. M. Mei and M. Weitz, Phys. Rev. Lett. 86 (2001) 559.  
26. S. Durr, Phys. Rev. A 64 (2001) 042113.  
27. A. Luis, J. Phys. A: Math. Gen. 34 (2001) 8597.  
28. K. Žyczkowski and W. Tadej, http://chaos.if.uj.edu.pl/~karol/hadamard/.  
29. W. Tadej and K. Zyczkowski, Open Syst. Inform. Dyn. 13 (2006) 133.  
30. C. E. Shannon, Bell Syst. Tech. J. 27 (1948) 623.  
31. E. V. Moreva, G. A. Maslennikov, S. S. Straupe and S. P. Kulik, Phys. Rev. Lett. 97 (2006) 023602.  
32. http://www.worldwideschool.org/library/books/tech/computers/TheHackers DictionaryofComputerJargon/chap42.html.  
33. W. H. Chee, Quantitative wave-particle duality in higher dimensions (unpublished thesis, Singapore, 2005).  
34. G. Kurizki, N. Bar-Gill, J. Clausen, M. Kolar and T. Opatrný, Quant. Inform. Processing 5 (2006) 463.  
35. N. Bar-Gill and G. Kurizki, Phys. Rev. Lett. 97 (2006) 230402.  
36. M. Kolar, T. Opatrny, N. Bar-Gill, N. Erez and G. Kurizki, New J. Phys. 9 (2007) 129.  
37. B.-G. Englert, *Lectures on Quantum Mechanics*, Perturbed Evolution (World Scientific, Singapore, 2006).  
38. B.-G. Englert, C. Kurtsiefer and H. Weinfurter, Phys. Rev. A 63 (2001) 032303.  
39. D. ter Haar, The Old Quantum Theory (Pergamon Press, Oxford and New York, 1967).  
40. J. A. Wheeler and W. H. Zurek (eds.), Quantum Theory and Measurement (Princeton University Press, Princeton, 1983).