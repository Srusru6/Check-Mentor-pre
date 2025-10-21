# Integrated photonic programmable random matrix generator with minimal active components

Check for updates

Kevin Zelaya<sup>1</sup>, Mostafa Honari-Latifpour<sup>1,2</sup> & Mohammad-Ali Miri<sup>1,2</sup>

Random matrices are fundamental in photonic computing because of their ability to model and enhance complex light interactions and signal processing capabilities. In manipulating classical light, random operations are utilized for random projections and dimensionality reduction, which are important for analog signal processing, computing, and imaging. In quantum information processing, random unitary operations are essential to boson sampling algorithms for multiphoton states in linear photonic circuits. Random operations are typically realized in photonic circuits through fixed disordered structures or through large meshes of interferometers with reconfigurable phase shifters, requiring a large number of active components. In this article, we introduce a compact photonic circuit for generating random matrices by utilizing programmable phase modulation layers interlaced with a fixed mixing operator. We show that using only two random phase layers is sufficient for producing output optical signals with a white-noise profile, even for highly sparse input optical signals. We experimentally demonstrate these results using a silicon-based photonic circuit with tunable thermal phase shifters and waveguide lattices as mixing layers. The proposed circuit offers a practical method for generating random matrices for photonic information processing and for applications in data encryption.

The rapid advancements in photonics fabrication techniques and materials science have enabled the deployment of photonic integrated circuits compatible with telecommunication wavelengths in compact on-chip form factors $^{1-3}$ . This allows exploiting the properties of light to perform computational tasks with reduced power consumption, increased bandwidth, and improved reliability. The ability to manipulate light on chip-scale platforms has sparked a plethora of applications across various fields, including telecommunications $^{4}$ , optical neural networks $^{5,6}$  and machine learning $^{7}$ , sensing $^{8}$ , imaging $^{9}$ , and quantum computing $^{10,11}$ . Indeed, extensive research has been developed to deploy programmable photonic integrated circuits capable of real-time tuning. The idea of such devices was first introduced by Reck et al. $^{12}$  for free-space propagation using arrays of beam splitters and phase shifters, which paved the way for compact on-chip solutions based on meshes of Mach-Zehnder interferometers (MZI) $^{2,13-17}$ , as well as recirculating meshes $^{18-20}$ , and multi-plane light conversion and multiport waveguide arrays $^{21-26}$ .

Recently, interlaced architectures that represent arbitrary unitary  $N \times N$  matrices have been explored as alternative candidates to conventional MZI meshes $^{23-25}$ , where arrays of phase shifters and passive mixing layers are

intertwined one after the another. This approach involves the intertwining of  $N + 2$  passive and  $N + 1$  active layers of optical elements, which has demonstrated high flexibility. Specifically, the passive layer responsible for mixing light propagation across all waveguides does not need to follow any specific design as long as its corresponding transfer matrix satisfies a density criterion $^{25}$ . The active elements lie in a layer separated from the passive one, allowing for more flexibility in the phase elements, which can be implemented through microheaters $^{27,28}$ , phase-change materials $^{29}$ , or other technologies.

Along different lines, the implementation of random unitary matrices by purely optical means has found exciting applications $^{30}$ , such as optical encryption in free-space settings $^{31,32}$  and through metasurfaces $^{33,34}$ . Harnessing the random transmission matrix of light in disordered waveguide arrays allows for encoding high-dimensional images into their lower-dimensional representations $^{9,35}$ . This property has been found resourceful in random disordered fibers, where the inherent Anderson localization renders highly localized modes used for high-fidelity transport of intensity patterns and images $^{36-41}$ . Furthermore, random photonic devices have been shown to be an excellent resource for generating operations akin to Haar

$^{1}$ Department of Physics, Queens College of the City University of New York, Queens, NY, 11367, USA.  $^{2}$ Physics Program, The Graduate Center, City University of New York, New York, NY, 10016, USA.  $\boxtimes$  e-mail: mmirilab@gmail.com

random matrices, a fundamental task on boson sampling required in quantum computing tasks $^{42,43}$ .

The present work introduces a programmable, compact, and simple-to-fabricate photonic chip designed to randomize light signals injected into its input. Such a process is achieved by exploiting general interlaced architectures discussed in the literature[24,25] and reducing the corresponding number of elements to an effective minimum without compromising its functionality. Indeed, numerical experiments reveal that only two active layers are required to perform the randomization process with high accuracy. Here, the output randomness is inherited from the random distributions assigned to the phase elements; the quality of the random output is evaluated by comparing it with the typical profile of white noise signals. Although the fabricated chip randomizes both the real and imaginary parts of the input signal, we present a relatively simple scheme in which the random patterns are still measurable with conventional power measurements. The chip capabilities are extended by demultiplexing large signals into smaller sizes without jeopardizing the quality of the random output. Furthermore, a specific application is introduced, where the chip can be used as an all-optical encryption device whose decryption process can be assessed through an equivalent device, the existence of which is guaranteed by the unitary nature of the randomization device.

# Results

# Random architecture model

Photonic integrated circuits (PICs) are rapidly becoming an attractive solution for optical computing applications. Their versatility enables the design of both programmable units $^{25}$  and integrated task-specific operations $^{44,45}$ . Particularly, unitary architectures based on interlaced layers of passive and active optical components have become a common design solution, for they allow for the representation of arbitrary unitary matrices (universality) and have shown to be resilient to manufacturing errors $^{24,46}$ . Experimental realization has been reported $^{47}$ , and further statistical methods for phase retrieval based on intensity measurements are discussed in the literature $^{48}$ .

The fundamental operational principle lies in the propagation of guided modes through waveguides  $\mathbf{E}(\mathbf{r}) = \mathcal{E}(\mathbf{r}_{\perp})e^{i(wt - \beta \mathbf{r}_{\parallel})}\hat{e}_{\perp}$ , with  $\mathcal{E}(\mathbf{r}_{\perp})$  the normalized guided-mode amplitude,  $r_{\parallel}$  and  $\mathbf{r}_{\perp}$  position vectors in the direction parallel and perpendicular to the propagation, respectively,  $\hat{e}_{\perp}$  the unit vector in the perpendicular direction, and  $\beta$  the corresponding mode propagation constant (see Supplementary Material S1 for more details). The electric field of a  $N$ -port device composed of single-mode waveguides, such as the one illustrated in Fig. 1a, writes as the complex-valued vector  $\mathbf{x} = (x_{1},\dots,x_{N})\mathcal{E}(\mathbf{r}_{\perp})$ , with  $x_{i}\in \mathbb{C}^{N}$  carrying information about the intensity and phase of the propagating light. Henceforth, to reduce the notation, the electric field propagating through the device is simply written as  $\mathbf{x}\equiv (x_{1},\dots,x_{N})$ .

In general, universal interlaced architectures are composed of  $M_{1}$  layers of passive mixing components and  $M_{2}$  layers of active elements $^{24,25}$ . Particularly, a universal  $N$ -port unitary device requires  $M_{1} = N + 2$  passive and  $M_{2} = N + 1$  active layers to render any arbitrary unitary optical operation. In turn, for randomization tasks, we require that the output vectors show traces of randomness regardless of the nature of the injected input signal, and thus, not all layers might be needed. That is, we seek the minimum number of layers  $M_{1}$  and  $M_{2}$  so that the output resembles a white noise signal. Indeed, as pointed out in $^{25}$ , the intermediate passive layers do not necessarily require to take any specific form, and layers described by transmission matrices with dense properties render the desired functionality.

In the present design, the  $M$ -layer  $(M_1 = M_2 = M)$  unitary interlaced structure  $\mathcal{U} \in U(N)$  is built based on dense passive layers  $F(\alpha_m) = e^{i\alpha_mH}$ , which rule the wave evolution of light and are described by coupled-mode theory approach[50,51]. Here,  $H$  is a tri-diagonal matrix with components  $H_{n,n+1} = \kappa_n$  for  $n \in \{1, \dots, N-1\}$  and  $\kappa_n$  the corresponding coupling parameter between neighbor waveguides. The device is operated by preparing an

arbitrary input state  $\mathbf{x} \in \mathbb{C}^N$ , the input signal, which is subsequently randomized through the unitary transformation

$$
\mathbf {x} _ {\text {o u t}} = \mathcal {U} \mathbf {x}, \quad \mathcal {U} = P ^ {(M)} F \left(\alpha_ {M}\right) \dots P ^ {(1)} F \left(\alpha_ {1}\right), \quad M \in \{1, 2, 3, 4 \}, \tag {1}
$$

where  $P^{(j)} = \text{diag}(e^{i\phi_1^{(j)}}, \ldots, e^{i\phi_N^{(j)}})$  are unitary diagonal matrices characterizing the programmable phase-mask layers, whereas  $\alpha_j$  are the coupling lengths for each waveguide array, for  $j \in \{1, \ldots, M\}$ .

The randomization process can be achieved with high accuracy by incorporating only two active layers of phase shifters,  $M = 2$ , and no substantial improvement is observed when more layers are included (see discussion below). This effectively reduces the overall size of the final architecture, rendering a low-footprint solution that requires a minimum number of control elements and, thus, is less prone to operational errors. The coupling coefficients defining the waveguide array can be chosen as those of the DFrFT operation using the Jx lattice $^{24,52}$ , homogeneous lattice $^{53}$ , or any random lattice that fulfills the density criterion posed by the Goldilocks principle discussed in $^{25}$  (see Supplementary Materials S2 for examples of dense matrices).

# Experimental setup and measurements

The PIC performing the randomization operation is fabricated on a silicon-on-silica (SOI) platform (see Methods for details). The design relies on coupled waveguides to perform the mixing layer operation and a layer of metal heaters producing the desired phase shift using conventional thermo-optic effects[28]. TE grating couplers are used to externally couple the PIC to the light input source and at the output for the data collection stage. Furthermore, a mechanical polarization controller (PC) is attached to the injection fiber, which is tuned so that maximum power is coupled to the PIC. The device under test (DUT) is the randomization PIC depicted in Fig. 1a, fed by a  $N \times 1$  network switch that splits the quasi-TE0 mode into the desired inputs that encode the optical signal. The heaters producing the phase shift are electronically controlled by a multichannel source measure unit, providing independent control currents of up to  $10\mathrm{mA}$  to each metal heater. Lastly, the output modes are gathered from the output grating couplers and collected at a multiport power meter.

The proposed PIC design is flexible enough to be manufactured in commercial foundries. For the current experimental run, the PIC was designed as a  $5 \times 5$  unitary device (5-port device) in the form of a fully electrically and optically packaged chip (see Fig. 1b-d). The packaging allows for easy and minimum-error light coupling and light-detection processes. Figure 1e summarizes the current experimental setup.

Manufacturing highly dense photonic chips presents challenges due to thermal and optical crosstalk, which become significant design problems when scaling up photonic units. To address this, we reduce the required number of ports of the proposed PIC by demultiplexing the input signal into lower-dimensional vectors, which are then sequentially fed at the input ports. Each input sequence is randomized using phases that are randomly distributed from either a normal or uniform distribution. This results in independent random outputs. Finally, the sequentially randomized outputs are multiplexed back into a higher-dimensional signal. This design choice is two-fold: it helps mitigate errors and reduces the device footprint.

Thus, any input signal  $\mathbf{x} \in \mathbb{R}^{100}$  shall be demuxed into sequences of 5-dimensional vectors,  $\mathbf{x} \in \mathbb{R}^{20 \times 5}$ . Particularly, we consider highly sparse 100-dimensional vectors,  $\mathbf{x} \in \mathbb{R}^{100}$ , whose components are either zero or one so that at least a component with a value of one exists for every demuxed sequence. The zero and one values denote in our experiment the cases when no light is injected and when light is coupled to the corresponding grating coupler, respectively. The distribution of zeros and ones is randomly selected for each sequence in the demuxed signal. The choice of such sparse signals is twofold: they can be implemented straightforwardly with the current setup, and they have poor qualities when it comes to random signals. The latter implies that if random footprints are found at the output of the PIC, it is not due to the random nature of the input signal (see analysis below). Since the PIC output is gathered through a power meter, any phase

![](images/6c440a517dea0541ebcc73347ac86b7e3de364d4e01ab6894a9d9879ab192e02.jpg)

![](images/901ed6964c7e2bc602d5e853517721db2e37173cc0ad4bd6a60e026ca74c15e4.jpg)

![](images/ff56fb8caa4e4767bc61b3ba33c3d25a22107fb14ac2fdecf4ea8ac5cd3745f4.jpg)  
Fig. 1 | Experimental setup and PIC design. a PIC interlaced structure for  $M = 2$  layers. The input optical signal  $\mathbf{x}$  is fed into the PIC, and the randomization phases are programmed by the SMU controller. The processed optical output signal is  $\mathbf{z}$ . For completeness, the fully packaged fabricated chip (b), a microscope image of the photonic circuit area (c), and a SEM capture of the waveguide array section (d) are illustrated. e Experimental setup and operation of the randomization device. Here,  
the programmable photonic integrated circuit performing the randomization is set as the device under test (DUT). In contrast, the phase shifters are the programmable elements of the device, which are externally and individually controlled by a multichannel source measure unit (SMU). The processed light at the output grating couplers is collected through a multiport power meter.

information is washed out during power measurements. Thus, real and imaginary parts of the complex-valued randomized output are not accessible through power detection schemes. Still, traces of randomness can be detected since the power measurements of complex-valued white noise (normally distributed signals) render a Rayleigh distribution instead<sup>54</sup>.

The set of 20 input sparse signals used in the present experiment, the demuxed lower-dimensional signals, and the corresponding measurements at the PIC output are illustrated in Fig. 2a-b. The phase change produced by thermo-optic phase shifters is proportional to the temperature change, which is, in turn, proportional to the current squared or electrical power $^{28}$ s. Thus, three experimental runs are performed, where

the currents in the SMU are programmed in such a way that the corresponding current-squared (phases) follow normal, uniform, and Rayleigh distributions (Fig. 2c). The current-squared values are randomly picked from the interval  $(0,64)mA^{2}$  according to each distribution. The upper current limit of  $8\mathrm{mA}$  has been fixed to avoid overheating on the chip, and it also corresponds to the approximate value at which a full  $2\pi$  phase rotation is achieved. The pre-established set of sparse inputs  $\mathbf{x}^{(n)}$  is fed into the PIC and optically processed according to the current-squared distributions under consideration, rendering the randomized optical signal that is ultimately detected and recorded by the multimode power detector. Since the signal was initially demultiplexed, the optical output is

![](images/d3d1b213fdf9be80fc4b19ad17496cb9383db4298a93254a7c7a1e922ab18901.jpg)  
a

![](images/5638e3b508bca02d28df0eeaf1a3092a59fd832d6057147650e590978813efc0.jpg)  
d

![](images/453c91f5459e4fa661c9b167b773ac95b9a28fb4ecee36d2f610d60cb818035a.jpg)

![](images/e9be573d2a2af9c65a3a8a6f32306af930c1d6e235d17f45f140753b71be65dc.jpg)  
b

![](images/64347cf719d1e4a700027c1140ac43f660ed1509eef4557005656f117e757e5e.jpg)  
e

![](images/96583356691d2b9bccb9afb314cdebbd283c037fb9baebad25c4ccdc23c30946.jpg)  
C

![](images/5257152fc1c5fdf152f98260c564e395105b9d3fc0bc105971594d63a5c90e1c.jpg)  
f

![](images/8c94ae67872930d1fb0e19a856374e3a7bf40c29f571f258aad714b7c99a29ab.jpg)  
Fig. 2 | Experimental run and data processing. a Sequences of testing random pulsed trains  $\mathbf{x}^{(p)}\in \mathbb{R}^{100}$ , for  $p\in \{1,\dots,20\}$ . b The latter are demultiplexed into signals  $\hat{\mathbf{x}}^{(p)}\coloneqq \mathbb{R}^{20\times 5}$ , which are programmed in the  $N\times 1$  switch and injected into the PIC. This produces the randomized demultiplexed signals  $\hat{\mathbf{z}}^{(p)}$ . c In this process, two ensembles of random phases are loaded into the phase shifters through the SMU, which correspondingly powers the metal heaters. Such ensembles are shown as histograms and scatter plots, highlighting the normal (left), uniform (right), and Rayleigh (center) distribution  
profiles.  $\mathbf{d}$  The output processed signals from the PIC are multiplexed back to the vectors  $\mathbf{z}^{(p)}\in \mathbb{R}^{100}$ .  $\mathbf{e - g}$  These outputs are then post-processed to extract the statistical information for normally and uniformly randomized phase distributions using the entropy  $S[|\mathbf{x}|]$  and autocorrelation difference  $\Delta_{\ell}\mathbf{X}[|\mathbf{x}|]$  criteria. For reference purposes, the typical entropy values for normal and uniform distributions are highlighted in yellow and blue, respectively. Likewise, the typical autocorrelation values for the previous distributions are highlighted in red.

![](images/86af4568dc77d735368dc2405b31f723db0ed25552a775851fa0ec783fe2ef1d.jpg)  
g

sequentially gathered in packages of five, the total number of ports, and normalized with respect to the total power in each measurement sequence. The final signal  $\mathbf{x}_{out}^{(n)}$  is then produced by multiplexing all the collected sequences and normalized once again with respect to the maximum so that  $\mathbf{x}_{out,p}^{(n)} \in (0,1]$ . The resulting randomized optical signals are shown in Fig. 2d for all the different current distributions.

The randomness quality of  $\mathbf{x}_{out}^{(n)}$  is assessed by analyzing the statistical properties of the intensity distribution. Ideally, white-noise signals are distributed according to normal distributions. Since we are limited to intensity-based measurements, the statistical analysis is restricted to positive-valued signals. We thus focus on the Rayleigh distribution for our analysis, which is equivalent to the squared of normal distributions, a characteristic more akin to the optical signals under consideration. In turn, uniformly distributed

![](images/921f733891852423e0a986e49574145eeca6886769f4f26408e313c1d52b3dc2.jpg)

![](images/a4e5ff602a9da316d571e52e3486c31783682cb9b75c10e7e6412cdebb84c6e6.jpg)

![](images/8424c27d72210a52534dd12d8151964c1ef98ad32ed4229aa20f18426d545cc4.jpg)

![](images/5c8656e01698323dea60482240b9d6d149c5a076dbde8a43e81636c446b5c221.jpg)  
Fig. 3 | White-noise criteria. a Typical autocorrelation profile for white noise signals. (b) Truncated autocorrelation criterion  $\widetilde{X}[\cdot]$  and (c) Shannon entropy  $(S)$  for ensembles of normal (blue-shaded) and uniform (purple-shaded) distributions as a function of the distribution size  $N$ . d Typical autocorrelation profile (upper panel) and the corresponding finite difference  $\Delta_{\ell}$  of the modulus of white noise signals. The

![](images/13eb630043fcedb26d144e3ffbc0509cd92875690eec1a2e16a65c0c0ccc878b.jpg)  
corresponding truncated autocorrelation criterion (e) and Shannon entropy (f) as a function of the distribution size  $N$ . In (b-c) and (e-f), 1000 random distributions were generated for each  $N$ , from which the mean (solid or dashed line) and standard deviations (shaded area) are computed.

![](images/a906eae3498c6b2ba01ab78b09c01c9f50893f43607b1ccb1aab5fbb985c0c09.jpg)

signals are known to maximize the Shannon entropy[55] and thus are a handy resource for encryption tasks. Consequently, both the Rayleigh and uniform distributions serve as benchmarks against which the randomness of the randomized optical signals can be assessed.

Autocorrelation and Shannon entropy are two complementary metrics that enable the quantification of signal randomness. Autocorrelation is particularly useful for identifying patterns within signals. Typically, random signals exhibit a flat autocorrelation function, while the derivative of the autocorrelation tends to flatten out when examining positive-definite signals. Conversely, Shannon entropy estimates the uncertainty in a signal; that is, lower uncertainty translates to poor prediction of the signal features (see Section 2d for a comprehensive analysis of these criteria). The statistical analysis of the randomized optical signals is shown in Fig. 2e, f for all the current distributions under consideration. In the latter figure, the blue-shaded and yellow-shaded areas highlight the regions where normally and uniformly distributed signals are typically found (refer to Section 2d).

The Shannon entropy values of processed optical signals accumulate in the region between the normal and uniform distributions, with a tendency toward the uniform distribution region. The assessment of randomness is further evaluated through the analysis of the autocorrelation differences, revealing the expected flat profile characteristic of random positive-definite distributions regardless of the current distribution used during the randomization process. Additionally, a quartile-quartile comparison between the optical signals and theoretical distributions is shown in Section S3 of Supplementary Information. The latter is analyzed for a larger dataset of 400 signals, which further reinforces the random distribution character of the processed optical signals, with a tendency toward uniform distributions.

# Randomness estimation

To assess the randomness of the device outputs, some criteria must be established to classify any given signal as random white noise. Although this may be accomplished through several statistical measures. Here we focus on the correlation and entropy properties. The use of two different statistical properties allows for ruling out false positives inherent in either autocorrelation or entropy analysis, as discussed below. White noise signals  $\mathbf{x}$  are known to be uncorrelated to shifted copies of themselves, henceforth called lags and denoted by  $\ell$ . For continuous or infinitely sampled signals, the

autocorrelation of white noise signals  $(\mathbf{X}[\mathbf{x}])$  becomes a single impulse at the lag  $\ell = 0$ ,  $X_{\ell}[\mathbf{x}] = \delta_{\ell,0}$  with  $\delta_{p,q}$  the Kronecker-delta distribution. In turn, for finite discrete signals, the autocorrelation is approximately flat for  $\ell \neq 0$  and peaks to the unity for  $\ell = 0$ . Indeed, Fig. 3a depicts some typical profiles of  $X[\mathbf{x}]$ , for signals  $\mathbf{x} \in \mathbb{R}^N$  normally distributed.

For  $\mathbf{x} \in \mathbb{R}^N$ , the autocorrelation renders a vector  $\mathbf{X}[\mathbf{x}] \in \mathbb{R}^{2N-1}$  which is symmetric around the lag  $\ell = 0$ ; i.e.,  $X_{-\ell}[\mathbf{x}] = X_{\ell}[\mathbf{x}]$ . For  $\ell = 0$ , the autocorrelation reduces to the Euclidean norm of  $\mathbf{x}$ ,  $X_{\ell=0}[\mathbf{x}] = (\mathbf{x}, \mathbf{x}) = \|\mathbf{x}\|^2$ . For normalized signals, the autocorrelation peaks at  $\ell = 0$  to the unity. Thus, throughout the manuscript, all signals analyzed by the autocorrelation are normalized beforehand. Following the autocorrelation symmetric, we focus exclusively on the positive lags  $\ell > 0$  and thus define the truncated autocorrelation

$$
\widetilde {\mathbf {X}} [ \mathbf {x} ] := \left(X _ {1}, \dots , X _ {N - 1}\right), \tag {2}
$$

which contains the minimum relevant statistical information to be processed.

Further insight into the autocorrelation and entropy estimation can be achieved by considering two specific sets of signals, i.e., signals generated from the normal and uniform distribution. The normal distribution is the desired behavior for the randomization process, which provides a benchmark to compare the outputs of the encryption device. The uniform distribution is used as a reference for the entropy analysis, as it provides the maximum bound for the Shannon entropy. To test the behavior of random signals following these distributions, we consider the ensembles  $S^{(n);N} = \{\mathbf{x}^{(n);k,N}\}_{k=1}^{1000}$  and  $S^{(u);N} = \{\mathbf{x}^{(u);k,N}\}_{k=1}^{1000}$  composed of 1000 normal and uniform randomly generated signals, respectively, for different dimensions,  $N = \{5, 10, \dots, 1000\}$ .

The truncated autocorrelation in (2) shall approximate a flat function for white noise signals, which, for  $N$  finite dimension signals, is represented by a vector with an approximate null mean  $(\mu(\widetilde{X}[\mathbf{x}]))$  and a standard deviation  $(\sigma(\widetilde{X}[\mathbf{x}]))$  approaching zero as  $N \to \infty$ . To illustrate the latter, we compute the mean and standard deviation of the truncated autocorrelation of every element in the ensemble as  $S_{X;\mu}^{(n);N} \coloneqq \{\mu(\widetilde{X}[\mathbf{x}^{(n);k,N}])\}_{k=1}^{1000}$  and  $S_{X,\sigma}^{(n);N} \coloneqq \{\sigma(\widetilde{X}[\mathbf{x}^{(n);k,N}])\}_{k=1}^{1000}$ , respectively. In this form, the behavior of the ensemble for each  $N$  is revealed by computing the average of the mean of

$S_{X;\mu}^{(n);N}$  to get the main trend and the mean of  $S_{X;\sigma}^{(n);N}$  for the deviations around the main trend. The latter is shown in the blue-dashed area in Fig. 3b, where the expected tendency of the normal distribution is evident. For completeness, the same analysis was carried out for uniformly distributed signals (green-shaded).

In turn, the Shannon entropy  $S(\mathbf{x})$  of a vector  $\mathbf{x}$  provides a notion of uncertainty for probability distributions (see Methods section). Indeed, although a higher entropy does not necessarily imply higher randomness, one can still define a threshold for the entropy to identify a white-noise signal. For instance, the uniform distribution possesses the higher uncertainty, and thus maximum entropy, among all distributions with compact support[55]. On the other hand, for Kronecker-delta-like distributions, the entropy is minimum (null) as certainty is absolute. Thus, the corresponding entropy shall be lower for a given white noise signal than that of uniform distributions.

By using the previously introduced random ensembles of normal  $(S^{(n);N})$  and uniform  $(S^{(u);N})$  distributions, we can perform a statistical analysis based on the mean and standard deviation of the entropy for each ensemble across different signal sizes  $N$ . These results are depicted in Fig. 3c, where the solid and dashed curves denote the mean for normal and uniform ensembles, respectively. The shaded areas represent the corresponding standard deviations from the mean value for each distribution. The mean entropy is higher for uniform distributions, which is expected, as elements uniformly distributed are all equally likely and possess larger uncertainty.

Thus, a given signal  $\mathbf{x}$  is said to be white noise if the mean  $(\mu (\widetilde{X} [\mathbf{x}]))$  and standard deviation  $(\sigma (\widetilde{X} [\mathbf{x}]))$  of the truncated autocorrelation, and entropy  $S(\mathbf{x})$  all lie in the normal distribution regions depicted in Fig. 3b, c for the corresponding size  $N$ . Note that if  $\mathbf{x} = (0,\dots,1,\dots 0)$ , it follows that  $\mu (\widetilde{X} [\mathbf{x}]) = \sigma (X[\mathbf{x}]) = 0$ , which lies in the white-noise region but is clearly not a random signal. For these reasons and to rule out false positives, both conditions are enforced to conclude about the randomness of the signal in question. Remark that, for  $N\lesssim 15$ , the entropy regions for both normal and uniform distributions are indistinguishable when analyzed using the entropy and autocorrelation criterion; thus, white noise is challenging to assess for relatively small-size signals.

Since the PIC produces optical complex-valued outputs, the white noise criteria shall be applied to the real and imaginary parts. In the current experimental setup, power measurements are gathered at the output, corresponding to the modulus square of the complex electric field, and we thus shall apply an equivalent criterion to the power. For simplicity and without loss of generality, we focus on the modulus  $|\mathbf{x}|$ . It is known that if the real and imaginary parts of  $\mathbf{x}$  are normally distributed with mean zero and standard deviation one, the elements of  $|\mathbf{x}| \coloneqq (|x_1|, \ldots, |x_N|)$  are distributed according to the Rayleigh distribution with scale parameter one<sup>54</sup>. See upper-panel in Fig. 3d. From this, the autocorrelation of the  $|\mathbf{x}|$  becomes linear with respect to the lag  $\ell$  and anti-symmetric around  $\ell = 0$ . Thus, the finite difference of the truncated autocorrelation,  $\Delta_{\ell} \widetilde{X}[|\mathbf{x}|] \coloneqq (X_2 - X_1, \ldots, X_{N-2} - X_{N-1})$ , also renders a flat distribution for  $\ell > 0$ . See lower-panel in Fig. 3d. In this form, an equivalent criterion can be introduced for  $|\mathbf{x}|$  based on  $\Delta_{\ell} \widetilde{X}[|\mathbf{x}|]$  and the entropy  $S(|\mathbf{x}|)$ , which are respectively depicted in Fig. 3e-f. The analysis for the modulus of uniform distributions was excluded in the latter figure, as elements of such a distribution are already positive numbers.

# Device randomness and encryption capabilities

The randomization capabilities of the proposed PIC are tested by first generating a set of input samples  $\{\overline{\mathbf{x}}^n\}_{n=1}^{50}$ , where each sample  $\mathbf{x}^n \in \mathbb{R}^{100}$ , the components of which render a sparse signal generated from a sequence of random randomly placed unit pulses  $\delta_{k,p}$ , with  $\delta_{k,p}$  the Kronecker delta function and  $k, p \in \{1, \dots, N = 100\}$ . See Fig. 4a. Despite the randomness in the generation of input sparse signals, they do not show any trace of white-noise behavior. This is done by testing the entropy and truncated autocorrelation criteria, as shown in Fig. 4b, where the regions where white noise is expected (shaded areas) are highlighted. The entropy of every input

sample lies below the expected values for white noise, whereas the mean and standard deviations deviate from the expected flat distribution for white noise in most cases.

Therefore, a signal is deemed white noise if both entropy and truncated autocorrelation lie around the shaded corresponding regions. The requirement of both simultaneous criteria is better illustrated in sample No. 21, which has a low entropy but a perfect flat autocorrelation. This is because sample No. 21 is a single-unit pulse, the autocorrelation of which is easily proved to be flat, and thus the signal is not white noise, likewise, for other samples with a similar pattern. Thus, given that none of the samples fulfill the randomness criterion, we rule out the possibility that any trace of randomness eventually found at the PIC output is produced due to intrinsic randomness in the generation of input samples.

For the numerical tests performed in this section, the phase elements in each layer of the architecture are independently generated from either a normal or uniform distribution bounded to the interval  $(- \pi, \pi)$ . The corresponding histograms of the random phases used in the encryption process are illustrated in Fig. 4c-d for up to four different layers. The latter allows analyzing the encryption capabilities of the output processed signals  $\widetilde{\mathbf{z}}^n = \mathcal{U}\widetilde{\mathbf{x}}^n$  by inspecting the white noise behavior. To this end, the entropy and truncated autocorrelation are calculated for each sample output  $\widetilde{\mathbf{z}}^n$  using both normal and uniform phases distributions as encryption keys, as illustrated in Fig. 4e-f. Here, the numerical simulations are run considering  $M = 1, 2, 3, 4$  encryption layers to showcase the effects of such added layers. Indeed, the entropy analysis shows that one encryption layer is insufficient to randomize all the input samples, even though the autocorrelation shows an almost flat distribution in each sample. We thus rule out the device with only one phase layer as a potential randomization device.

In turn, when two phase layers are considered, the output of each sample signal produces higher entropy values, with only a few lying outside the region of white noise. Interestingly, the autocorrelation shows a higher standard deviation for normally distributed phases than those outputs encrypted with uniform keys. For more layers  $(M > 2)$ , both the entropy and autocorrelation criteria show no significant improvement as compared to  $M = 2$  layers. This numerical evidence allows for reducing the PIC size to  $M = 2$  layers without impacting random performance in any significant way. For completeness, the real part of the transfer matrices  $\mathcal{U}$  is depicted in Fig. 4g when sweeping the number of layers  $M$  and using the Jx and homogeneous lattices as the passive mixing layers  $F$ . In analogy to the previous analysis, normally (upper panels) and uniformly (lower panels) distributed phases are also used here. It is clear that  $M = 1$  layers produce a transfer matrix resembling the original missing layer  $F$  (see Supplementary Material S1), whereas  $M = 2$  layers wash out any such pattern. In both cases, the transfer matrices associated with uniformly distributed phases show a better random pattern than the normally distributed case. Thus, when operated with uniformly distributed phases, the PIC output produces a better random process.

The randomization PIC can be further exploited to operate as an encryption device. This is done by treating the input signal as the vector to be encrypted, the phase distribution as a set of encryption keys, and the randomized output as the encrypted vector. In this procedure, the phase distribution has to be recorded and stored for subsequent decryption tasks. Indeed, the decryption process can be inverted, as the transformation operator  $\mathcal{U}$  is unitary. Thus, the encrypted signal  $\mathbf{x}_{out}$  can be cast back to its original form by injecting it into either the inverse operator  $\mathcal{U}^{\dagger}$  or by reverting the device ports and using the conjugated phases. This inversion process can be done only if the original sets of phases  $\phi_{n}^{(m)}$  used to randomize the input signal are known. For more details on the inversion process, see Supplementary Materials S2.

The real and imaginary parts of the first 25 normally encrypted samples are shown in Fig. 4g for one and two encryption layers. Here, one can corroborate that one-layer encryption produces signals whose real and imaginary parts tend to pile up around the middle signal component 50 (dashed-rectangle in Fig. 4g), as predicted from the entropy analysis. Indeed,

![](images/44cacfa4c13079824053152d4446681a1f2c473d08b805104335e55019776ae3.jpg)

![](images/7ecbf88b67c07a1d73fda09d95274770aeb43891b351637f4493d3674bac4b0d.jpg)

![](images/e682ee4a94a9ab89b69dd14f789df2b653562a1f89d8393318cf39d5e835fc11.jpg)

![](images/99bc6dfe349c9b8e41cc6fa6733ea197dc696ac076e458515414f940d5ce6a2c.jpg)

![](images/8951d009daffb6831a0b563abdd464ae4f8ed4c41fc545fbc4683f5e4edb593f.jpg)

![](images/5180493e549add895d8a3f19efe5b5c83d5fd3d1659dcd7b2ac9c59d2cccff4f.jpg)

![](images/d36e9514d18ae607d8157fc0da29857581e12ec33ef39a9728add6b6a1d96da0.jpg)

![](images/e82f856eefe67ee1b5320149b72ee8a2c3462c06f34f92fa28c4a8cc041f1aa3.jpg)  
Fig. 4 | Numerical simulations of the device randomness capabilities. a Set of 50 randomized pulsed sample signals  $\mathbf{x}^n$ . b The corresponding values for the Shannon entropy (upper panel) and autocorrelation bars (lower panel). The shaded area denotes the region where white noise is expected. c-d Histograms of randomly generated phase shifters (encryption keys) taken from the normal (c) and uniform (d) distributions in the interval  $(-\pi, \pi]$ . e-f Entropy and truncated autocorrelation criteria for the samples randomized using normally (e) and uniformly (f) distributed  
keys. The random process uses  $M = 1,2,3,4$  random-phase layers.  $\mathbf{g}$  Real part of the transmission matrix  $\mathcal{U}$  in Eq. (1) for  $M = 1,2,3$  layers and considering normally (upper panel) and uniformly (lower panel) distributed phases. For illustration, the Jx and homogeneous lattice were used as the mixing layers  $F$ . h Real and imaginary parts of the first 25 encrypted sample signals using normal keys combined with one (left) and two (right) encryption layers.

such a tendency vanishes when the second encryption layer is added, producing signals spread across all the components. It is worth remarking that, for power measurements, the second phase layer in the architecture in Fig. 1 does not modify the readout at the power detectors. Thus, we can disregard

the latter when performing power measurements. Nevertheless, the proposed PIC is flexible and compatible with phase measurement if the input and data collection stages of the present experimental run are changed by an optical vector analyzer.

![](images/6d91b53676066868e1c7cdf1a60895b9fc444bb1bf6dee222845a4fdc32c9248.jpg)  
Fig. 5 | Random defects and encryption capabilities. (left panel) Real and imaginary parts of the perturbed DFrFT matrix  $F(\delta)$  for  $\delta = 0.05, 0.1, 0.2$ . (Top panel) Testing image  $W$  used for encryption with perturbed DFrFT  $F(\delta)$ . (right panel) The  
corresponding encrypted images. (Bottom panel) Decrypted images using an ideal decryption device  $\mathcal{U}^{\dagger}(\delta = 0)$ .

# Random passive layers

Although the previous construction has shown a compact encryption device that can be scaled down to two phase layers without jeopardizing the encryption capabilities, it is always desirable to design a circuit with fewer elements. So far, the encryption is stored in the phase element, whereas the waveguide is fixed as a well-patterned unitary matrix. Thus, the device randomness can be enhanced by adding disorder into the waveguide arrays. The waveguides cannot be tuned once manufactured, but their pattern highly affects the output. It has been shown in[25] that random matrices generated from the Haar measure serve as passive layers in universal unitary interlaced architectures. The latter means that such matrices are dense enough to shuffle the elements of an input vector and render it into an arbitrary new one, provided that enough layers are available. For the encryption tasks, the encryption two-layered architecture should work when operated with random Haar matrices instead of a predefined lattice model, provided that the former matrices are dense.

The additional random element, namely the passive unitary layer  $F$ , is expected to increase the potential randomness at the encryption device output. To analyze the latter, we add the random symmetric deformation  $R$  to the  $J_{x}$  Hamiltonian  $H$  so that the perturbed encryption device  $\mathcal{U}(\delta)$  and the evolution through the perturbed waveguide array  $F(\delta)$  read, respectively, as

$$
\mathcal {U} (\delta) = P ^ {(2)} F (\delta) P ^ {(1)} F (\delta), \quad F (\delta) = e ^ {i z (H + \delta R)}, \tag {3}
$$

where  $\delta$  the perturbation strength parameter, and  $R\in \mathbb{C}^{N\times N}$  a random matrix with elements taken from the normal distribution with mean  $\mu = 0$  and standard deviation  $\sigma = 1$ ; i.e.,  $\mathcal{N}(\mu = 0,\sigma = 1)$ . Without loss of generality, the perturbation strength is considered as  $\delta >0$ . If the strength parameter  $\delta \ll max(\kappa_n)$ , the deformation can be considered as a perturbation of the original  $J_{x}$  lattice. For larger  $\delta$ , the overall effect of  $R$  will overcome that of  $J_{x}$ , rendering a random matrix. This is handy as we can study the effects of small perturbation on the waveguide array, and also analyze the encryption capabilities of the device when the passive element is random in nature.

To measure the overall effect of the perturbation parameter  $\delta$ , it is more convenient to compute the percentage error introduced to  $F(\delta)$  with respect to the ideal  $J_{x}$  lattice; i.e.,  $E_{F}(\delta) = \left(\| F(\delta) - F\| / \| F\|\right)\times 100\%$ . By considering 100 random perturbations for each  $\delta$ , one finds that, on average, the perturbations  $\delta = 0.05, 0.1, 0.2$  induce errors on  $F$  around  $E_{F} = 15\%, 32\%, 67\%$ , respectively. The overall effect of such perturbations on the real and imaginary parts of  $F(\delta)$  are shown in Fig. 5 (left panel). To test the effects of such perturbation on the encryption and decryption scheme, we consider a multi-stage setup. First, take a  $10\times 10$  pixel image and reshape it into a 100-dimensional one-dimensional vector, which is encrypted using (3) for  $\delta = 0.05, 0.1, 0.2$ , with  $N = 100$ . The encrypted vector is then decrypted using the same keys through the unperturbed decryption device  $\mathcal{U}_{enc}^{\dagger}$ . Indeed, the original source image is recovered when encrypted using  $\delta = 0$ , whereas deviations are expected for  $\delta \neq 0$ . For  $\delta \neq 0$ , the decrypted images show an error due to the defects on the  $F(\delta)$  layers. For instance, for  $\delta = 0.05$

$(E_{F}\approx 15\%)$ , the error in decrypting the image is approximately  $E_{W_{\mathrm{w}}}^{\sim}\approx 20\%$ . Figure 5 (lower panel) shows the real and imaginary parts of the decrypted images, where it is clear that, for  $\delta = 0.05$ , the real part still resembles the source image and the large error is due to the imaginary part components. In turn, for  $\delta \leq 0.1$ , the real part of the decrypted images is indistinguishable.

# Discussion

The randomization PIC has been tested under the proposed demultiplexing scheme, showing the expected performance. Among the potential issues present in the experimental run, the thermal heaters might induce undesired effects due to thermal cross-talk and thermal stabilization. The first effect is not relevant, as the phase shifters are randomly assigned from distributions, and thermal crosstalk will also contribute to the overall random pattern. Despite the latter, a set of pre-programmed phases will induce the same behavior in the PIC. This holds as long as thermal stabilization time is reached, which is the most critical factor in reaching reproducibility. Thus, the experimental data was gathered after allowing a long enough time window  $\tau$  between measurements after powering up all the metal heaters. The proposed PIC is flexible enough to be scaled up to a larger number of channels if so required, the design of which would only require that the transfer matrix of the passive mixing layer  $F$  fulfills the required density criterion[25].

While a single layer of MZIs can be used to independently modulate the amplitude and phase of optical signals in each channel, this approach inevitably leads to power losses through the leakage channel of the MZI, a requirement to produce amplitude modulation. The proposed PIC design overcomes this issue due to the unitary nature of the waveguide arrays used as the passive mixing layers, which produce the required interference that ultimately steers the amplitude modulation without resorting to lossy solutions. This renders a lossless and relatively compact design that depends only on two layers of active elements regardless of the size  $N$  of the optical signal.

The proposed PIC successfully demonstrated the capability to generate the necessary random pattern and encryption features using a two-layer design. Despite adding a third layer not significantly improving the white noise of the encrypted signals, the extra key combinations used in the encryption process make the output more difficult to reverse-engineer without prior knowledge of the keys. In this regard, the proposed design can be adjusted whenever compactness or security is the final goal. There are reports in the literature for all-optical encryption devices in free-space configurations using random phase masks[31,56]. The latter includes a two-lens configuration combined with two statistically independent white noise phase planes, creating an encrypted image. The device introduced in the present work provides an equivalently compact and on-chip solution, which can be further exploited as an optical image encryption technique by following a similar demultiplexing procedure as the one discussed above.

The measurements presented in this work mainly focus on power detection, but this is due to limitations in the experimental setup rather than the performance of the PIC itself. In fact, the proposed PIC is versatile supports phase measurement if an optical vector analyzer is implemented or further interferometry is performed to extract the output phases. Furthermore, the proposed device can work as a versatile and controllable platform for investigating equivalent random and disordered wave systems $^{36,37}$ , where the disorder can be tuned on real-time to induce the desired effects. Recent studies have demonstrated that random photonic devices can serve as an effective tool for producing operations equivalent to Haar-random matrices. This is a crucial requirement for boson sampling in quantum computing tasks $^{42,43}$ . The latter is achieved by changing to other material platforms, such as silicon nitride (Si3N4), which are more suitable for single photon transport. In this regard, the intrinsic nonlinearity of the waveguide core can induce photon entanglement across a waveguide array $^{57}$ .

# Methods

# Material platform

The randomization operation in the photonic integrated circuit (PIC) is carried out using a silicon-on-silica platform. A passive layer, denoted as  $F(\alpha)$ , is implemented using waveguide arrays that, based on the coupled-mode theory, facilitate the unitary wave evolution responsible for mixing a single excitation channel across all the waveguides. The waveguides are constructed with a silicon core (Si) surrounded by a silica cladding (SiO2) with refractive indices of  $n_{Si} = 3.47$  and  $n_{SiO2} = 1.4711$  at room temperature (293 K). In terms of geometry, we have a waveguide with a transverse rectangular shape featuring  $500\mathrm{nm}$  width and  $220\mathrm{nm}$  thickness. This configuration enables the waveguide to support a fundamental quasi-TE0 mode and a quasi-TM mode when operated at  $1550\mathrm{nm}$  wavelengths. The PIC is specifically designed to operate on the quasi-TE0 mode, and 8-degree TE grating couplers are employed to effectively couple the right mode from the injection fiber into the PIC.

For the 5-channel PIC, the waveguide array is designed to exhibit symmetry around the middle waveguide. The spacing between the outermost and middle waveguides is  $233\mathrm{nm}$  and  $210\mathrm{nm}$ , respectively, whereas the coupling length is set to  $62\mu m$ . The phase shifters are implemented using Ti/W alloy as heaters and are connected to the probing pads using bilayer TiW/Al electrical traces. The probing pads are wire-bonded to a PCB for electrical access to the phase shifters.

# Entropy and autocorrelation estimation

While the current experimental setup is designed exclusively for capturing power measurements, the suggested PIC can acquire phase information by adjusting the data collection stage. This would allow for the collection of complex-valued signals, requiring the application of the white-noise criterion to both the real and imaginary parts, as well as the modulus of the signal, such as the case presented in the main text.

Particularly, the autocorrelation  $\ell$  component (lag) of the  $\mathbf{X}[\mathbf{x}]$  is defined as  $X_{\ell}[\mathbf{x}]\coloneqq (T_{\ell}\mathbf{x},\mathbf{x})$ , with  $T_{\ell}$  the translation operator,  $(\mathbf{x},\mathbf{y})$  the Euclidean inner product in  $\mathbb{R}^N$ , and  $\ell \in \{-N - 1,\dots,N - 1\}$  the position of the lagged signal. In turn, to compute the Shannon entropy of either component of the signal,  $\mathbf{x}\in \mathbb{R}^{N}$ , it is first required to extract and normalize the related histograms  $\{p_j\}_{j = 1}^M$  using  $M = \lfloor \sqrt{N}\rfloor$  bins. This allows producing the corresponding probability distribution to compute the Shannon entropy

$$
S = - \sum_ {j = 1} ^ {M} p _ {j} \log_ {2} p _ {j}.
$$

# Noise levels

The thermal noise (Johnson-Nyquist noise) generated in resistors represents an unavoidable noise source that could impact the operation of the metal heaters used for phase control. To obtain some insight on the effects of such noise, we consider RMS thermal power noise for DC signals  $P_{\mathrm{n,RMS}} = 4k_B T \Delta f$ , where  $K_b$  stands for the Boltzmann constant,  $T$  the absolute resistor temperature, and  $\Delta f$  a bandwidth over which the noise is sampled. In turn, the phase-change  $\Delta \phi$  produced in the waveguides is proportional to the power absorbed by the heater  $P_{\mathrm{heater}}$ ; that is,  $\Delta \phi = \alpha P_{\mathrm{heater}}$  with  $\alpha \approx 0.12 \mathrm{rad / mW}$  estimated from experimental measurements. From the latter, the phase error produced by thermal noise can be estimated  $\Delta \phi_{\mathrm{thermal}} = 1.92 \times 10^{-9} \mathrm{rad}$ , where a 1 GHz sampling bandwidth was used. Thus, these thermal fluctuations ultimately produce negligible effects on the accuracy of the phase control produced through the metal heaters.

In turn, the source is a tunable semiconductor laser (Santec TSL-570) operating at a wavelength of  $1550\mathrm{nm}$  with an output power of  $20\mathrm{mW}$ . This laser has a fairly narrow linewidth of  $\Delta f = 200\mathrm{kHz}$  (equivalent to  $\Delta \lambda \approx 1.6\mathrm{pm}$  at  $\lambda = 1550\mathrm{nm}$ ), which corresponds to a phase noise of  $S_{f}(0) = 400\mathrm{kHz}$ . Nevertheless, this is

significantly lower than the device bandwidth that is governed mainly by the bandwidth of the waveguide arrays involved which itself has to do with the frequency dependency of the coupling coefficients. This is shown in Fig. S1d in Supplementary Information S1, illustrating the coupling parameters used in the proposed design over the C-band. In the latter, the inset shows the behavior in the interval  $1550\mathrm{nm} + / - 1\mathrm{nm}$ , highlighting the flat dependence over the laser source wavelength, which renders a uniform response over the generated CW output with such a narrow linewidth.

The nominal relative intensity noise (RIN) of this laser is  $\mathrm{RIN} = \langle (\Delta P)^2\rangle /P^2 = -145\mathrm{dB / Hz}$ , which corresponds to intensity fluctuations ratios of less than  $\Delta P / P\approx 5\times 10^{-5}$ . This is equivalent to  $\Delta P\approx$ $1\mu \mathrm{W}$  at the input of the device which translates to a negligible amount of intensity fluctuation at the output of the device which will not impact the measured stable values of the power at the output of our device. The input power  $(20\mathrm{mW})$  is dropped down by the grating couplers in the input and output, the coupling efficiency of which is  $-7.5\mathrm{dB}$  per coupler, bringing the optical power down to levels around  $600~\mu \mathrm{W}$ . On the other hand, according to the power meter specifications provided by the manufacturer, the detection resolution is  $-80\mathrm{dB}$ $(10\mathrm{nW})$ . The generated optical signal in the output is thus several orders of magnitudes more significant than the power detector resolution. The noise level from the optical source (SNR) is also several orders of magnitude below the output optical signal level. Thus, the magnitude of the randomized optical output is not affected by the noise levels in any significant form.

# Data availability

The data that supports the findings of this study are available from the corresponding author upon reasonable request.

Received: 27 August 2024; Accepted: 15 January 2025

Published online: 04 February 2025

# References

1. Carolan, J. et al. Universal linear optics. Science 349, 711-716 (2015).  
2. Bogaerts, W. et al. Programmable photonic circuits. Nature 586, 207-216 (2020).  
3. Bogaerts, W. & Rahim, A. Programmable photonics: an opportunity for an accessible large-volume pic ecosystem. IEEE J. Sel. Top. Quant. Electron. 26, 1-17 (2020).  
4. Paraiso, T. K. et al. A photonic integrated quantum secure communication system. Nat. Photonics 15, 850-856 (2021).  
5. Shen, Y. et al. Deep learning with coherent nanophotonic circuits. Nat. photonics 11, 441-446 (2017).  
6. Lin, X. et al. All-optical machine learning using diffractive deep neural networks. Science 361, 1004-1008 (2018).  
7. Li, X.-K. et al. High-efficiency reinforcement learning with hybrid architecture photonic integrated circuit. Nat. Commun. 15, 1044 (2024).  
8. Chrostowski, L. et al. Silicon photonic resonator sensors and devices. In Laser Resonators, Microresonators, and Beam Control XIV, 387-402 (SPIE, 2012).  
9. Wang, X. et al. Integrated photonic encoder for low power and high-speed image processing. Nat. Commun. 15, 4510 (2024).  
10. Harris, N. C. et al. Quantum transport simulations in a programmable nanophotonic processor. Nat. Photonics 11, 447-452 (2017).  
11. Wang, M. et al. Topologically protected entangled photonic states. *Nanophotonics* 8, 1327-1335 (2019).  
12. Reck, M., Zeilinger, A., Bernstein, H. J. & Bertani, P. Experimental realization of any discrete unitary operator. Phys. Rev. Lett. 73, 58 (1994).  
13. Miller, D. A. Self-configuring universal linear optical component. Photonics Res. 1, 1-15 (2013).  
14. Miller, D. A. Perfect optics with imperfect components. Optica 2, 747-750 (2015).

15. Clements, W. R., Humphreys, P. C., Metcalf, B. J., Kolthammer, W. S. & Walmsley, I. A. Optimal design for universal multiport interferometers. Optica 3, 1460-1465 (2016).  
16. Hamerly, R., Bandyopadhyay, S. & Englund, D. Accurate self-configuration of rectangular multiport interferometers. Phys. Rev. Appl. 18, 024019 (2022).  
17. Dai, T. et al. A programmable topological photonic chip. Nat. Mater. 23, 928-936 (2024).  
18. Zhuang, L., Roeloffzen, C. G., Hoekman, M., Boller, K.-J. & Lowery, A. J. Programmable photonic signal processor chip for radiofrequency applications. Optica 2, 854-859 (2015).  
19. Pérez, D. et al. Multipurpose silicon photonics signal processor core. Nat. Commun. 8, 636 (2017).  
20. Pérez-López, D., Gutierrez, A. M., Sánchez, E., DasMahapatra, P. & Capmany, J. Integrated photonic tunable basic units using dual-drive directional couplers. Opt. Express 27, 38071-38086 (2019).  
21. Taguchi, Y., Wang, Y., Tanomura, R., Tanemura, T. & Ozeki, Y. Iterative configuration of programmable unitary converter based on few-layer redundant multiplane light conversion. Phys. Rev. Appl. 19, 054002 (2023).  
22. Tanomura, R., Tang, R., Ghosh, S., Tanemura, T. & Nakano, Y. Robust integrated optical unitary converter using multiport directional couplers. J. Lightwave Technol. 38, 60-66 (2020).  
23. Markowitz, M. & Miri, M.-A. Universal unitary photonic circuits by interlacing discrete fractional fourier transform and phase modulation. ArXiv https://doi.org/10.48550/arXiv.2307.07101 (2023).  
24. Markowitz, M., Zelaya, K. & Miri, M.-A. Auto-calibrating universal programmable photonic circuits: hardware error-correction and defect resilience. Opt. Express 31, 37673-37682 (2023).  
25. Zelaya, K., Markowitz, M. & Miri, M.-A. The goldilocks principle of learning unitaries by interlacing fixed operators with programmable phase shifters on a photonic chip. Sci. Rep. 14, 10950 (2024).  
26. Pastor, V. L., Lundeen, J. & Marquardt, F. Arbitrary optical wave evolution with Fourier transforms and phase masks. Opt. Express 29, 38441-38450 (2021).  
27. Harris, N. C. et al. Efficient, compact and low loss thermo-optic phase shifter in silicon. Opt. Express 22, 10487-10493 (2014).  
28. Liu, S. et al. Thermo-optic phase shifters based on silicon-on-insulator platform: state-of-the-art and a review. Front. Optoelectron. 15, 9 (2022).  
29. Ríos, C. et al. Ultra-compact nonvolatile phase shifter based on electrically reprogrammable transparent phase change materials. PhotoniX 3, 26 (2022).  
30. Gigan, S. Imaging and computing with disorder. Nat. Phys. 18, 980-985 (2022).  
31. Refregier, P. & Javidi, B. Optical image encryption based on input plane and fourier plane random encoding. Opt. Lett. 20, 767-769 (1995).  
32. Frauel, Y., Castro, A., Naughton, T. J. & Javidi, B. Resistance of the double random phase encryption against various attacks. Opt. Express 15, 10253-10265 (2007).  
33. Audhkhasi, R. & Povinelli, M. L. Full spectral image encryption in the infrared using an electrically reconfigurable metasurface and a matched detector. Adv. Photonics Res. 5, 2300254 (2024).  
34. Audhkhasi, R., Zhelyeznyakov, M., Brunton, S. & Majumdar, A. Leveraging statistical-spectral correlations of random metasurfaces for steganography and multi-wavelength cryptography. Appl. Opt. 63, G18-G23 (2024).  
35. Miri, M.-A. Integrated random projection and dimensionality reduction by propagating light in photonic lattices. Opt. Lett. 46, 4936-4939 (2021).  
36. Mafi, A., Ballato, J., Koch, K. W. & Schulzgen, A. Disordered anderson localization optical fibers for image transport-a review. J. Lightwave Technol. 37, 5652-5659 (2019).  
37. Mafi, A. & Ballato, J. Review of a decade of research on disordered anderson localizing optical fibers. Front. Phys. 9, 736774 (2021).

38. Cao, H. & Eliezer, Y. Harnessing disorder for photonic device applications. Appl. Phys. Rev. 9, 011309 (2022).  
39. Segev, M., Silberberg, Y. & Christodoulides, D. N. Anderson localization of light. Nat. Photonics 7, 197-204 (2013).  
40. Abouraddy, A. F., Di Giuseppe, G., Christodoulides, D. N. & Saleh, B. E. Anderson localization and colocalization of spatially entangled photons. Phys. Rev. A 86, 040302 (2012).  
41. Dikopoltsev, A. et al. Observation of anderson localization beyond the spectrum of the disorder. Sci. Adv. 8, eabn7769 (2022).  
42. Russell, N. J., Chakhmakhchyan, L., O'Brien, J. L. & Laing, A. Direct dialling ofhaar random unitary matrices.N.J.Phys.19,033007 (2017).  
43. Clementi, M. et al. Programmable frequency-bin quantum states in a nano-engineered silicon device. Nat. Commun. 14, 176 (2023).  
44. Meng, X. et al. Compact optical convolution processing unit based on multimode interference. Nat. Commun. 14, 3000 (2023).  
45. Zelaya, K. & Miri, M.-A. Integrated photonic fractional convolution accelerator. Photonics Res. 12, 1828 (2024).  
46. Taguchi, Y. & Ozeki, Y. Standalone gradient measurement of matrix norm for programmable unitary converters. JOSA B 41, 1425-1431 (2024).  
47. Tang, R., Tanomura, R., Tanemura, T. & Nakano, Y. Ten-port unitary optical processor on a silicon photonic chip. Acs Photonics 8, 2074-2080 (2021).  
48. Kuzmin, S., Dyakonov, I. & Kulik, S. Architecture agnostic algorithm for reconfigurable optical interferometer programming. Opt. Express 29, 38429-38440 (2021).  
49. Yariv, A. & Yeh, P. Photonics: Optical Electronics in Modern Communications 6th edn, Vol. 836 (Oxford university press, 2007).  
50. Huang, W.-P. Coupled-mode theory for optical waveguides: an overview. JOSA A 11, 963-983 (1994).  
51. Cooper, M. L. & Mookherjea, S. Numerically-assisted coupled-mode theory for silicon waveguide couplers and arrayed waveguides. Opt. Express 17, 1583-1599 (2009).  
52. Weimann, S. et al. Implementation of quantum and classical discrete fractional fourier transforms. Nat. Commun. 7, 11027 (2016).  
53. Christodoulides, D. N., Lederer, F. & Silberberg, Y. Discretizing light behaviour in linear and nonlinear waveguide lattices. Nature 424, 817-823 (2003).  
54. Forbes, C., Evans, M., Hastings, N. & Peacock, B. Statistical Distributions (John Wiley & Sons, 2011).  
55. Cover, T. M. Elements of Information Theory (John Wiley & Sons, 1999).  
56. Unnikrishnan, G., Joseph, J. & Singh, K. Optical encryption by double-random phase encoding in the fractional fourier domain. Opt. Lett. 25, 887-889 (2000).  
57. Belsley, A., Pertsch, T. & Setzpfandt, F. Generating path entangled states in waveguide systems with second-order nonlinearity. Opt. Express 28, 28792-28809 (2020).  
58. Boylestad, R. L. & Nashelsky, L. Electronic Devices and Circuit Theory 11th edn (Pearson, 2002).

# Acknowledgements

This project was supported by the U.S. Air Force Office of Scientific Research (AFOSR) Young Investigator Program (YIP) Award# FA9550-22-1-0189, the Defense University Research Instrumentation Program (DURIP) Award# FA9550-23-1-0539, and by the National Science Foundation NSFBSF Award# DMR-2211646.

# Author contributions

M.A.M. conceived the main idea. K.Z wrote the main manuscript text, performed the numerical analysis, and developed the theoretical analysis. M.H.L. designed the photonic integrated circuit, deployed the experimental setup, and conducted the experiment measurements. M.A.M. co-wrote the manuscript and supervised the project. All authors reviewed the manuscript.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s44310-025-00054-9.

Correspondence and requests for materials should be addressed to Mohammad-Ali Miri.

Reprints and permissions information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2025, corrected publication 2025