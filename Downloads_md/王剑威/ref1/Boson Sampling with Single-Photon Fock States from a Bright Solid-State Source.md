# Boson Sampling with Single-Photon Fock States from a Bright Solid-State Source

J. C. L boreo, $^{1,*}$  M. A. Broome, $^{2}$  P. Hilaire, $^{3,4}$  O. Gazzano, $^{3,5}$  I. Sagnes, $^{3}$  A. Lemaitre, $^{3}$  M. P. Almeida, $^{1}$  P. Senellart, $^{3,6}$  and A. G. White $^{1}$

<sup>1</sup>Centre for Engineered Quantum Systems, Centre for Quantum Computation and Communication Technology, School of Mathematics and Physics, University of Queensland, Brisbane, Queensland 4072, Australia

$^{2}$ Centre of Excellence for Quantum Computation and Communication Technology, School of Physics, University of New South Wales, Sydney, New South Wales 2052, Australia

$^{3}$ CNRS-C2N Centre de Nanosciences et de Nanotechnologies, Université Paris-Sud, Université Paris-Saclay, 91460 Marcoussis, France

<sup>4</sup>Université Paris Diderot-Paris 7, 75205 Paris CEDEX 13, France

$^{5}$ Joint Quantum Institute, National Institute of Standards and Technology, University of Maryland, Gaithersburg, Maryland 20899, USA

$^{6}$ Département de Physique, Ecole Polytechnique, Université Paris-Saclay, F-91128 Palaiseau, France (Received 14 March 2016; revised manuscript received 24 September 2016; published 28 March 2017)

A boson-sampling device is a quantum machine expected to perform tasks intractable for a classical computer, yet requiring minimal nonclassical resources as compared to full-scale quantum computers. Photonic implementations to date employed sources based on inefficient processes that only simulate heralded single-photon statistics when strongly reducing emission probabilities. Boson sampling with only single-photon input has thus never been realized. Here, we report on a boson-sampling device operated with a bright solid-state source of single-photon Fock states with high photon-number purity: the emission from an efficient and deterministic quantum dot-micropillar system is demultiplexed into three partially indistinguishable single photons, with a single-photon purity  $1 - g^{(2)}(0)$  of  $0.990 \pm 0.001$ , interfering in a linear optics network. Our demultiplexed source is between 1 and 2 orders of magnitude more efficient than current heralded multiphoton sources based on spontaneous parametric down-conversion, allowing us to complete the boson-sampling experiment faster than previous equivalent implementations.

DOI: 10.1103/PhysRevLett.118.130503

Introduction.-A core tenet of computer science is the Extended Church-Turing thesis, which states that all computational problems that are efficiently solvable by physically realistic machines are efficiently simulatable with classical resources. In 2011, Aaronson and Arkhipov introduced boson sampling, a quantum protocol for efficiently sampling the output of a multimode bosonic interferometer [1-5]: a problem apparently intractable with classical computation. When scaled to many bosons this model of intermediate-i.e., nonuniversal-quantum computation will provide the strongest evidence against the Extended Church-Turing thesis.

The most experimentally accessible boson is the photon, thus serving in the initial experimental implementations of boson sampling [6-11]. These earlier assays are well short of the numbers of single photons required to probe the Extended Church-Turing thesis: scalable photonic technology is required. The three core technologies needed for scalable quantum photonics are single-photon sources [12-16], large interferometric networks, with current integrated and programmable technology [11,17-19], and efficient photon detection, with demonstrated number resolution [20,21], and efficiencies of up to  $95\%$  [22].

To date, boson-sampling implementations employed photons obtained from spontaneous parametric downconversion, for which output is far from ideal single-photon

Fock states,  $|\psi \rangle = |1\rangle$ , instead producing primarily vacuum with a small admixture of pairs of photons,  $|\psi \rangle = \sqrt{1 - |\lambda|^2}\sum_{n = 0}^{\infty}\lambda^n |nn\rangle$ , where  $|\lambda| \ll 1$ . A nonheralded  $2n$ -photon source can be built by using  $n$  down-converters, but it can only be used in specific protocols where the impact of higher photon numbers is minimized [23]; alternatively, it can be operated as a heralded  $n$ -photon source by detecting  $n$  photons—one from each down-converter—to herald the presence of their  $n$  single-photon partners. Multiphoton rates for state-of-the-art pulsed down-conversion sources [24-27], pumped at a standard  $80\mathrm{MHz}$  repetition rate, range from  $\sim 300\mathrm{kHz}$  for 2 photons—thus, yielding heralded single photons at that rate—down to  $\sim 3\mathrm{mHz}$  for 8 photons—accordingly, 4 heralded single photons at that rate. For as little as 6 heralded single photons, the rate ( $\sim 1$  per year) becomes less than the detection rate of gravitational waves [28].

Recent progress with time-multiplexing schemes [29] can potentially increase these heralded multiphoton rates in future experiments. Using down-conversion to manipulate many single photons remains, however, challenging to date, which has prevented the scaling of boson sampling to larger photon numbers. In an effort to lessen this hurdle, an extended version of the protocol—named randomized [4],

or "Scattershot" [10], boson sampling—exploits heralding to obtain an algorithmic enhancement, by a binomial factor, in the number of valid inputs to the protocol: boson sampling then becomes scalable with probabilistic, but heralded, down-conversion sources.

Quantum dots in photonic structures [30-34] have been recently shown to produce long streams of indistinguishable single photons with large emission yields [35,36]. Efficient temporal-to-spatial demultiplexing of these sources will enable multiphoton experiments at scales heretofore impossible. Here we implement a bosonsampling device operated with a bright demultiplexed source of three highly pure single-photon Fock states from the emission of a deterministic quantum dot-micropillar system [31]. The high source brightness allows us to implement multiphoton sources markedly more efficient than their down-conversion counterparts, completing the boson-sampling protocol faster than in previous implementations. Our results prove solid-state sources an appealing candidate to constitute the basis for future quantum photonics, in particular for the implementation of boson sampling with larger photon numbers.

Source of multiple single-photon Fock states.-Laser pulses with a repetition rate of  $R_{L} = 80 \mathrm{MHz}$  and wavelength centred at  $905 \mathrm{~nm}$  provide quasiresonant excitation of an InGaAs quantum dot deterministically coupled to a micropillar cavity, which itself is housed in an optically accessible cryostat (Cryo) system at  $13 \mathrm{~K}$ . See Refs. [31,35] for a detailed description of this quantum dot-micropillar system. An optimized collection efficiency results in a record probability per pump pulse of finding a spectrally

isolated single photon at the output of a single-mode fiber—an absolute brightness—of up to  $\eta_0 = 0.14$ . As a result, our core source generates up to  $\sim 11$  MHz of single photons, modulo detector efficiencies, from which  $3.6\mathrm{MHz}$  are detected with an avalanche photodiode (APD) of  $32\%$  quantum efficiency [35]. The absolute brightness depends on the laser pump power  $P$  according to  $\eta = \eta_0(1 - e^{-P / P_0})$ , with  $P_0 = 150~\mu \mathrm{W}$  the saturation power. Under quasiresonant excitation, single-photon sources based on nongated quantum dots are subject to small and random frequency jitter—known as spectral diffusion—due to charges near the solid-state emitter [37,38]. This results in the emission of photons with partial indistinguishability, which in our case is around  $50\% -70\%$  depending on the exact pump conditions [35]. We choose to operate our source at  $P = 1.2P_{0}$ , at which point it exhibits a single-photon purity  $1 - g^{(2)}(0)$  of  $0.990\pm 0.001$ , where  $g^{(2)}(0) = 0$  holds for an ideal  $|n\rangle = |1\rangle$  Fock state. Our source remains highly pure even at high pump powers, with a purity of  $0.976\pm 0.001$  at  $3P_{0}$ ; see the Supplemental Material [39].

Temporal to spatial demultiplexing of the source could be achieved with an active—temporally varying—switcher, such that each of  $n$  consecutive single photons is routed into a different spatial channel, resulting in a scalable method to demultiplex  $n$  events from a one-photon source into one event of an  $n$ -photon source. A simpler alternative is to implement a passive demultiplexer as depicted in Fig. 1(a). Here, photon routing occurs by using an array of  $n - 1$  chained beam splitters with tuned transmittances as to evenly distribute, with probability  $1 / n$ , each single-photon

![](images/4bdfdded90aef84884f8d77398086b1d2b73625cca59370fa365d567dd28cf1e.jpg)  
FIG. 1. Experimental setup. (a) A dichroic mirror (DM), and a  $0.85\mathrm{nm}$  FWHM bandpass filter (BP) isolate single-photon emission at  $932\mathrm{nm}$  from the  $905\mathrm{nm}$  excitation laser, which is then collected by a single-mode fiber (SMF). A passive demultiplexer composed of beam splitters with tunable transmittances—half-wave plates (HWP), and polarizing beam splitters (PBS)—and compensating delay lines of  $12.5\mathrm{ns}$  probabilistically converts three consecutive single photons into separate spatial modes at the input of the boson-sampling circuit. The  $6\times 6$  linear network is composed of polarizers (Pol), half-wave plates, a  $3\times 3$  nonpolarizing fiber beam splitter (FBS), and polarizing fiber beam splitters (PFBS). Six APDs are used to record two- and threefold correlation measurements to sample from the output distribution of the boson-sampling device. (b)-(d) Detected and generated  $n$ -photon rates obtained directly from the demultiplexed source. The generated rates include a factor of  $(1/0.3)^n$  to describe our source modulo detector efficiencies ( $30\%$  in average for the used APDs). The four-photon count rates are obtained from the demultiplexer in (a) with an extra tunable beam splitter. Curves are fits to  $c_{\max}^{(n)}(1 - e^{-P / P_0})^n$ , with  $c_{\max}^{(2)} = 186.4\mathrm{kHz}$ ,  $c_{\max}^{(3)} = 2202\mathrm{Hz}$ , and  $c_{\max}^{(4)} = 8.8\mathrm{Hz}$ , denoting maximum  $n$ -photon generated rates.

into one of  $n$  possible outputs. The high absolute brightness in our core source allows us to readily operate two-, three-, and four-photon sources with this method. Figures 1(b)-1(d) show the detected, and generated—corrected for detector efficiencies—count rates of our demultiplexed  $n$ -photon source:  $n$  single photons in the same temporal mode at the output of  $n$  single-mode fibers.

To estimate the efficiency of our source, we define the  $n$ -photon probability per trial,  $p_{\mathrm{pt}}^{(n)} = c_{\mathrm{gen}}^{(n)} / R_{\mathrm{trial}}$ , the probability of generating a spectrally isolated  $n$ -photon event, at the output of  $n$  single-mode fibers, per experimental attempt. Here,  $c_{\mathrm{gen}}^{(n)}$  is the  $n$ -photon generated rate, and  $R_{\mathrm{trial}}$  is the "trial" rate. This allows us to compare multiphoton sources from different systems based solely on their efficiency, irrespective of external parameters, such as detector efficiencies, and pump rates. For an explicit comparison, we compute  $p_{\mathrm{pt}}^{(n)}$  for various partially heralded three-photon sources used in previous boson-sampling experiments; see Fig. 2. Our solid-state based three-photon source is more efficient than its down-conversion counterparts by one to two orders of magnitude; see Supplemental Material [39] for details on this comparison. Note that this is achieved using a nonscalable—scaling as  $1 / n^n$  probabilistic demultiplexer. We thus expect our  $n$ -photon efficiency to increase superexponentially  $(\propto n^n)$  with an active demultiplexer.

Boson sampling with solid-state photon sources.—Using this method, 2 and 3 partially indistinguishable single

![](images/5240756a562361383f6d5d80d210639dd3d91045c2feaa093aafe189786a9dcf.jpg)  
FIG. 2. Multiphoton source efficiency.  $n$ -photon probability per trial,  $p_{\mathrm{pt}}^{(n)}$ , for our two-, three-, and four-photon source taken at  $1.2P_0$  (solid blue, red, and green circles), and at  $3P_0$  (dashed blue, red, and green circles). The  $p_{\mathrm{pt}}^{(n)}$  is estimated for various down-conversion three-photon sources (gray and orange circles) employed in previous boson-sampling experiments. The Scattershot algorithm (S.S.) [4,10] results in an effective enhancement of  $p_{\mathrm{pt}}^{(n)}$  (orange circles) for its specific protocol. Our three-photon source is between 1 to 2 orders of magnitude more efficient than the down-conversion cases. Note that only partial heralding was employed in all down-conversion implementations. A fully heralded  $n$ -photon source, a necessary condition to produce true single-photon Fock state statistics with down-conversion, is thus further orders of magnitude less efficient than our sources.

photons are used as inputs into the boson-sampling  $6 \times 6$  linear network  $\mathcal{L}$ , consisting of 3 spatial- and 2 polarization-encoded modes; see Fig. 1(a). The relative temporal delay between photons is fine-tuned to erase their temporal distinguishability, and the use of polarizing fiber beam splitters ensures that they are indistinguishable in polarization.

We first input  $N = 2$  single photons, and characterize the  $M = 6$ -mode  $\mathcal{L}$  network—in general, a nonunitary transfer matrix due to inevitable optical losses—using the method described in Ref. [40]; see the Supplemental Material [39]. Following the theoretical model developed in Ref. [41], 2 photons with a degree of indistinguishability quantified by  $\mathcal{I}$ , entering  $\mathcal{L}$  in inputs  $\{i,j\}$  and exiting from outputs  $\{k_1,k_2\}$  lead to a twofold coincidence probability:

$$
p ^ {(2)} = \left(\frac {1 + \mathcal {I}}{2}\right) | \operatorname {p e r} (\bar {\mathcal {L}}) | ^ {2} + \left(\frac {1 - \mathcal {I}}{2}\right) | \det  (\bar {\mathcal {L}}) | ^ {2}, \tag {1}
$$

given by the permanent (per) and determinant (det) of the submatrix  $\bar{\mathcal{L}}$  formed with rows  $i, j$  and columns  $k_{1}, k_{2}$  of  $\mathcal{L}$ . Note that Eq. (1) reduces to the well-known formula  $p^{(2)} = |\mathrm{per}(\bar{\mathcal{L}})|^2$  in the ideal case of perfect indistinguishability, i.e.,  $\mathcal{I} = 1$ .

We measured all  $\binom{M}{N} = 15$  outputs in which photons exit  $\mathcal{L}$  in different modes, so-called no-collision events. Peak areas in temporal-correlation measurements at these outputs allow us to extract—in a single experimental run—both the sampling distribution resulting from the boson sampler—that is, with partially indistinguishable photons—and that of a (classical) distinguishable sampler arising from completely distinguishable particles. Given an output configuration  $k$ , coincidences detected under the area  $A_{k}^{0}$  around zero delay  $\Delta t = 0$  are subject to two-photon interference: they determine the boson sampler distribution by measuring  $\bar{p}_{k}^{(2)} = A_{k}^{0}$ . Conversely, photons leading to coincidences around  $\Delta t = \pm l \times (12.5 \mathrm{~ns})$ , for  $l$  integer, do not interfere, and one would expect that these distributions contain information of a classical sampler. Indeed, following Ref. [35], one can deduce that the distinguishable sampler distribution is measured via  $\bar{p}_{k}^{(2)}(0) = 2A_{k}^{r} - A_{k}^{n} - A_{k}^{p}$ , where  $A_{k}^{r}$  is a reference area (average in gray peaks),  $A_{k}^{n}$  is the reduced area at negative  $\Delta t$  (left orange peak), and  $A_{k}^{p}$  is the reduced area at positive  $\Delta t$  (right orange peak) as shown in Fig. 3(a). Measuring only no-collision events, however, does not provide access to the entire output distribution; thus, to obtain probabilities we normalize the measured distributions to the corresponding theoretical prediction according to Eq. (1)—that is, the sum of experimentally obtained probabilities within the no-collision subspace is matched to that as in theory, and, given a two-photon input  $\{i,j\}$ ,  $\mathcal{I}_{i,j}$  is extracted from the measured output distribution; see Supplemental Material [39].

Figure 3(b) shows our two-photon boson-sampling results. Experimental distributions for the boson sampler

![](images/9aa853504be242b0b95184b3f5ba13474c1f80992140076ff00bc38115575fc1.jpg)

![](images/670d8e2fbf39a9e2bd2580a356f9ae2248c34e8def782343d70597f847e8e722.jpg)

![](images/516d40344c10f6e8b1abfeb5cf5bfb39f33dcc128f9811ff60758e6c388a25ea.jpg)

![](images/e5a36a54a7c4a383366f68157a09c3db55e29dd47fff82b79cd44abd3ee290f7.jpg)  
FIG. 3. Two-photon boson sampling. (a) Temporal-correlation measurements at no-collision outputs for 2 photons entering at different inputs. Coincidences around  $\Delta t = 0$  (blue peaks) result from two-photon interference and are thus governed by Eq. (1). The position of reduced areas (orange peaks) indicates the temporal distance in emission from the quantum dot: For inputs  $\{1,2\}$ , and  $\{2,3\}$ , photons were emitted after one laser repetition rate  $1 / R_{L} = 12.5$  ns; thus, reduced areas appear at  $\pm 1 / R_{L}$ ; similarly, appearing at  $\pm 25$  ns for  $\{1,3\}$ , with photons emitted separated by 2 laser repetition rates. Coincidences outside  $\Delta t = 0$  (orange peaks and grey peaks) involve noninterfering photons, thus contain only classical information. (b) Coincidences at zero delay from the 15 no-collision outputs give the distribution of the boson sampler (blue bars), with theoretical distributions (empty bars) given by  $\mathcal{I}_{1,2} = 0.520$ ,  $\mathcal{I}_{2,3} = 0.540$ , and  $\mathcal{I}_{1,3} = 0.643$ , for their respective input; whereas coincidences outside zero delay determine that of the distinguishable sampler (red bars), with theoretical distribution (empty bars) obtained by assuming zero indistinguishability in Eq. (1). Note that strong output configurations in the classical sampler tend to have a larger reduction when observed in the boson sampler. A complete sampled distribution is obtained with  $10\mathrm{min}$  integration time; and, in average, a total of  $\sim 40000$  twofold events are collected for any given distribution. Error bars (small light-colored bars) are deduced from assuming Poissonian statistics in detected events.

![](images/0cf00b9c99a8d605154925c10382d55440dfd6ff04fdc23829789eaa91c87871.jpg)

![](images/058434f6db2a5c46425b7f7b38b989f05e759f07d019961c68a6eab0b2b22541.jpg)

(blue bars) are shown for 3 different two-photon inputs, and their theoretical distributions (empty bars) are obtained with pairwise indistinguishabilities  $\mathcal{I}_{1,2} = 0.520$ ,  $\mathcal{I}_{2,3} = 0.540$ , and  $\mathcal{I}_{1,3} = 0.643$ , respectively, in agreement with independently measured indistinguishabilities via two-photon interference on a  $2 \times 2$  beam splitter; see Supplemental Material [39]. For the distinguishable sampler (red bars), the theoretical distribution (empty bars) is calculated by using  $\mathcal{I}_{i,j} = 0$ ,  $\forall i, j$  in Eq. (1). To quantify the agreement between theory and experiment, we employ the statistical fidelity  $\mathcal{F} = \sum_{i} \sqrt{p_{i}^{\mathrm{th}} p_{i}^{\mathrm{exp}}}$  between normalized theoretical and experimental distributions. For our two-photon boson sampling, we find an average fidelity of  $\bar{\mathcal{F}} = 0.9984 \pm 0.0007$  across the six sampled distributions in Fig. 3(b), where the error here is 1 standard deviation among the six fidelity values.

We now tune the source to input  $N = 3$  single photons into the  $\{1,2,3\}$  mode. In this case, the probability of detecting a threefold coincidence at outputs of  $\mathcal{L}$  is [41]

$$
p ^ {(3)} = t _ {6} ^ {\dagger} \left(\mathbb {I} + \sum_ {i \neq j} \rho_ {i, j} \mathcal {I} _ {i, j} + \tilde {\rho} \prod_ {i \neq j} \sqrt {\mathcal {I} _ {i , j}}\right) t _ {6}, \tag {2}
$$

with  $\mathbb{I}$ , the  $6\times 6$  identity operator;  $t_6$  is a six-component quantity that depends on the permanent, determinant, and immanants of  $3\times 3$  submatrices  $\mathcal{T}$ ; and the  $\rho_{i,j}$ , and  $\tilde{\rho}$  matrices are as explicitly defined in the Supplemental Material [39]. Equation (2) reduces to  $p^{(3)} = |\mathrm{per}(\mathcal{T})|^2$  in the ideal case of perfect indistinguishability between all particles, i.e.,  $\mathcal{I}_{i,j} = 1$ ,  $\forall i$ ,  $j$ .

Verifying the output distribution of a boson-sampling device involves calculating a number of (modulus squared) matrix permanents. This task is in general computationally hard to implement efficiently on a classical computer. The complete result of a large-scale boson-sampling machine is thus likely to be, even in principal, unverifiable. It has been even argued that a large-scale boson-sampling experiment will fail to distinguish its data from the (trivial) uniform distribution—i.e., one in which every output configuration is equally probable [42]. In light of this, some methods have been proposed and demonstrated for the validation of boson sampling: circumstantial evidence is provided to support that a boson-sampling machine is indeed functioning according to the laws of quantum mechanics, by ruling out that the experimentally obtained data originate from, e.g., the uniform distribution, or a sampler with distinguishable particles [11,43-45].

![](images/0e7d28b96309db4104a30bf0bc381e4520f4904302d513578924f08d92b6575a.jpg)  
FIG. 4. Three-photon boson sampling. (a) A total of 20 no-collision threefold simultaneous coincidences are recorded to obtain the boson-sampler distribution (blue bars); the theoretical distribution (empty bars) is obtained from Eq. (2) and by using the previously determined pairwise indistinguishability parameters. Error bars (light-colored bars) are deduced from Poissonian statistics in measured events. We apply the validation of boson-sampling protocol against the uniform sampler (b), and distinguishable sampler (c). A counter (blue dots) is updated for every threefold event and at any point a positive value validates the data as being obtained from a boson sampler as opposed to either a uniform or distinguishable sampler; see Supplemental Material [39]. The final data set contains a total of 6725 threefold events collected in  $9\mathrm{h}$ , that is  $\sim 1000$  per  $80\mathrm{min}$ , a faster rate than in previous boson-sampling experiments.

![](images/5b42b65d23d78ed71f6482890ef58ef1ca7c74db2a6f03faa3a58371b360ef0f.jpg)

![](images/ff35dab403a68e5494078c238c04ad30acc012d31873a2f4a53a32caa68161e3.jpg)

Figure 4 shows our experimental results for the three-photon boson sampler. In Fig. 4(a), the previously determined two-photon indistinguishabilities  $\mathcal{I}_{i,j}$  are used as input for the theoretical distribution (empty bars) according to Eq. (2), and experimental probabilities (blue bars) are obtained by measuring the  $\binom{M}{N}=20$  threefold simultaneous—i.e., around  $\Delta t=0$  coincidences for nocollision events normalized to the theoretical prediction. We find the three-photon boson-sampling fidelity  $\mathcal{F}=0.997\pm0.006$ , where the error here results from propagated Poissonian statistics. In Figs. 4(b), 4(c), we apply the validation of the boson-sampling protocol to our data. We record threefold coincidences in steps of 30 sec, in which time a counter is updated. For each detected threefold coincidence, the counter is either increased or decreased in one unit, and it is designed, see Supplemental Material [39], such that after an experimental run a positive value validates the data as obtained from the boson sampler distribution, whereas a negative counter indicates it originates from the uniform sampler, see Fig. 4(b), or the distinguishable sampler, see Fig. 4(c). We observed overall increasing positive counters, thus validating our boson-sampling device by ruling out the alternative hypotheses.

Note that aside from these validation protocols, the increasing interest in resolving the quantum or classical nature of, in general, quantum optical experiments has recently resulted in more general approaches to identify when a device can be efficiently simulated by classical means [46].

Discussion.-We experimentally demonstrated multiphoton interference with a highly efficient solid-state source: a boson-sampling device implemented with single-photon Fock states emitted by a deterministic quantum dot-micropillar system. A temporal to spatial demultiplexing scheme resulted in multiphoton sources between one to two orders of magnitude more efficient than their downconversion versions, which allowed us to complete the boson-sampling protocol faster than in previous experiments

[6-9]. An active source demultiplexing would further boost our multiphoton efficiency superexponentially—with the number of photons—potentially enabling boson sampling with larger photon numbers.

Furthermore, we directly observed the effect of partial distinguishability: Our results follow closely the sampling of permanents and immanants of matrices with contributions modulated by photon indistinguishability. Moreover, by exploiting temporal-correlation measurements we showed that both classical and quantum two-photon sampling distributions can be obtained simultaneously, which can be readily extended to multifold temporal-dependent measurements in a larger boson-sampling experiment. Potentially, this could motivate new validation protocols exploiting statistics that include this temporal degree of freedom.

The impact of partial distinguishability in boson sampling has been studied theoretically [41,47-49], and reported experimentally [41]. However, identifying experimentally this property in isolation is challenging. Previous experiments with down-conversion exhibit photon statistics polluted by higher-order terms [23], which can be mistakenly interpreted as decreased photon indistinguishability. In fact, in many cases these higher-order terms, and not photon distinguishability, are the main cause of performance degradation in down-conversion-based protocols [50,51]. The pathway to maximize indistinguishability in efficient solid-state sources is well known: resonant excitation of the quantum-dot results in near-optimal values of photon indistinguishability [33,34], in which case the obtained output distributions will be close to the sampling of only permanents—functions belonging to the class of #P-hard problems, in which the main complexity arguments of boson sampling apply.

We believe our results pave the way to the forthcoming advent of quantum-dot based quantum photonics, in which a future boson-sampling implementation with efficiently demultiplexed and resonantly pumped solid-state sources may finally see the Extended Church-Turing thesis put to serious test.

This work was partially supported by the Centre for Engineered Quantum Systems (Grant No. CE110001013), the Centre for Quantum Computation and Communication Technology (Grant No. CE110001027), the Asian Office of Aerospace Research and Development (Grant No. FA2386-13-1-4070), by the ERC Starting Grant No. 277885 QDCQED, the French Agence Nationale pour la Recherche (ANR DELIGHT, ANR USSEPP), the French RENATECH network, the Labex NanoSaclay. A. G. W. acknowledges support from a UQ Vice-Chancellor's Research and Teaching Fellowship. J. C. L., M. P. A., and A. G. W. thank Devon Biggerstaff for experimental assistance, and the team from the Austrian Institute of Technology for kindly providing time-tagging modules. J. C. L. thanks Saleh Rahimi-Keshari, Marco Bentivegna, Fabio Sciarrino, and Max Tillmann for valuable discussions.

Note added.—After this Letter was submitted, we became aware of related works [52,53].

*Corresponding author. juan.loredo1@gmail.com

[1] S. Aaronson and A. Arkhipov, Proc. ACM Symp. Theory Computing, San Jose, CA, (2011), p333.  
[2] S. Aaronson, Proc. R. Soc. A 467, 3393 (2011).  
[3] C. Shen, Z. Zhang, and L.-M. Duan, Phys. Rev. Lett. 112, 050504 (2014).  
[4] A. P. Lund, A. Laing, S. Rahimi-Keshari, T. Rudolph, J. L. OBrien, and T. C. Ralph, Phys. Rev. Lett. 113, 100502 (2014).  
[5] J. Huh, G. G. Guerreschi, B. Peropadre, J. R. McClean, and A. Aspuru-Guzik, Nat. Photonics 9, 615 (2015).  
[6] M. A. Broome, A. Fedrizzi, S. Rahimi-Keshari, J. Dove, S. Aaronson, T. C. Ralph, and A. G. White, Science 339, 794 (2013).  
[7] J. B. Spring et al., Science 339, 798 (2013).  
[8] M. Tillmann, B. Dakic, R. Heilmann, S. Nolte, A. Szameit, and P. Walther, Nat. Photonics 7, 540 (2013).  
[9] A. Crespi, R. Osellame, R. Ramponi, D.J. Brod, E.F. Galvão, N. Spagnolo, C. Vitelli, E. Maiorino, P. Mataloni, and F. Sciarrino, Nat. Photonics 7, 545 (2013).  
[10] M. Bentivegna et al., Sci. Adv. 1, e1400255 (2015).  
[11] J. Carolan et al., Science 349, 711 (2015).  
[12] P. G. Kwiat, E. Waks, A. G. White, I. Appelbaum, and P. H. Eberhard, Phys. Rev. A 60, R773 (1999).  
[13] T. Pittman, B. Jacobs, and J. Franson, Opt. Commun. 246, 545 (2005).  
[14] T. M. Babinec, B. J. M. Hausmann, M. Khan, Y. Zhang, J. R. Maze, P. R. Hemmer, and M. Loncar, Nat. Nanotechnol. 5, 195 (2010).  
[15] Z. Yuan et al., Science 295, 102 (2002).  
[16] C. Santori, D. Fattal, J. Vučković, G. S. Solomon, and Y. Yamamoto, Nature (London) 419, 594 (2002).  
[17] A. Politi, M. J. Cryan, J. G. Rarity, S. Yu, and J. L. O'Brien, Science 320, 646 (2008).  
[18] B.J. Smith, D. Kundys, N. Thomas-Peter, P.G.R. Smith, and I.A. Walmsley, Opt. Express 17, 13516 (2009).

[19] A. Crespi, R. Ramponi, R. Osellame, L. Sansoni, I. Bongioanni, F. Sciarrino, G. Vallone, and P. Mataloni, Nat. Commun. 2, 566 (2011).  
[20] A. J. Miller, S. W. Nam, J. M. Martinis, and A. V. Sergienko, Appl. Phys. Lett. 83, 791 (2003).  
[21] A. Divochiy et al., Nat. Photonics 2, 302 (2008).  
[22] A. E. Lita, A. J. Miller, and S. W. Nam, Opt. Express 16, 3032 (2008).  
[23] J.-W. Pan, Z.-B. Chen, C.-Y. Lu, H. Weinfurter, A. Zeilinger, and M. Zukowski, Rev. Mod. Phys. 84, 777 (2012).  
[24] X.-C. Yao, T.-X. Wang, P. Xu, H. Lu, G.-S. Pan, X.-H. Bao, C.-Z. Peng, C.-Y. Lu, Y.-A. Chen, and J.-W. Pan, Nat. Photonics 6, 225 (2012).  
[25] B.J. Metcalf et al., Nat. Commun. 4, 1356 (2013).  
[26] C. Zhang, Y.F. Huang, Z. Wang, B.H. Liu, C.F. Li, and G.C. Guo, Phys. Rev. Lett. 115, 260402 (2015).  
[27] J. C. Loredo, M. P. Almeida, R. DiCandia, J. S. Pedernales, J. Casanova, E. Solano, and A. G. White, Phys. Rev. Lett. 116, 070503 (2016).  
[28] B. P. Abbott et al., Phys. Rev. Lett. 116, 061102 (2016).  
[29] F. Kaneda, B. G. Christensen, J. J. Wong, H. S. Park, K. T. McCusker, and P. G. Kwiat, Optica 2, 1010 (2015).  
[30] P. Lodahl, A. Floris van Driel, I. S. Nikolaev, A. Irman, K. Overgaag, D. Vanmaeelbergh, and W. L. Vos, Nature (London) 430, 654 (2004).  
[31] O. Gazzano, S. Michaelis de Vasconcellos, C. Arnold, A. Nowak, E. Galopin, I. Sagnes, L. Lanco, A. Lemaitre, and P. Senellart, Nat. Commun. 4, 1425 (2013).  
[32] P. Lodahl, S. Mahmoodian, and S. Stobbe, Rev. Mod. Phys. 87, 347 (2015).  
[33] X. Ding et al., Phys. Rev. Lett. 116, 020401 (2016).  
[34] N. Somaschi et al., Nat. Photonics 10, 340 (2016).  
[35] J. C. Loredo et al., Optica 3, 433 (2016).  
[36] H. Wang et al., Phys. Rev. Lett. 116, 213601 (2016).  
[37] A. V. Kuhlmann, J. Houel, A. Ludwig, L. Greuter, D. Reuter, A. D. Wieck, M. Poggio, and R. J. Warburton, Nat. Phys. 9, 570 (2013).  
[38] S. Unsleber, D. P. S. McCutcheon, M. Dambach, M. Lermer, N. Gregersen, S. Hofling, J. Mork, C. Schneider, and M. Kamp, Phys. Rev. B 91, 075413 (2015).  
[39] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevLett.118.130503 for data of single-photon purity; description of the probability per trial; estimation of count rates; measured transfer matrix; discussion of pairwise indistinguishabilities; three-photon interference formula; and description of the validation protocols.  
[40] S. Rahimi-Keshari, M. A. Broome, R. Fickler, A. Fedrizzi, T.C. Ralph, and A.G. White, Opt. Express 21, 13450 (2013).  
[41] M. Tillmann, S. H. Tan, S. E. Stoeckl, B. C. Sanders, H. deGuise, R. Heilmann, S. Nolte, A. Szameit, and P. Walther, Phys. Rev. X 5, 041015 (2015).  
[42] C. Gogolin, M. Kliesch, L. AOLita, and J. Eisert, arXiv: 1306.3995.  
[43] S. Aaronson and A. Arkhipov, arXiv:1309.7460.  
[44] N. Spagnolo et al., Nat. Photonics 8, 615 (2014).  
[45] J. Carolan et al., Nat. Photonics 8, 621 (2014).  
[46] S. Rahimi-Keshari, T.C. Ralph, and C.M. Caves, Phys. Rev. X 6, 021039 (2016).

[47] V. S. Shchesnovich, Phys. Rev. A 91, 013844 (2015).  
[48] M. C. Tichy, Phys. Rev. A 91, 022316 (2015).  
[49] V. Tamma and S. Laibacher, Phys. Rev. Lett. 114, 243601 (2015).  
[50] T. J. Weinhold et al., arXiv:0808.0794.

[51] M. Barbieri, T. J. Weinhold, B. P. Lanyon, A. Gilchrist, K. J. Resch, M. P. Almeida, and A. G. White, J. Mod. Opt. 56, 209 (2009).  
[52] Y. He et al., arXiv:1603.04127.  
[53] H. Wang et al., arXiv:1612.06956.