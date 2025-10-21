ARTICLE

Received 13 May 2015 | Accepted 10 Dec 2015 | Published 19 Jan 2016

DOI: 10.1038/ncomms10439

OPEN

# Direct measurement of large-scale quantum states via expectation values of non-Hermitian matrices

Eliot Bolduc<sup>1</sup>, Genevieve Gariepy<sup>1</sup> & Jonathan Leach<sup>1</sup>

In quantum mechanics, predictions are made by way of calculating expectation values of observables, which take the form of Hermitian operators. Non-Hermitian operators, however, are not necessarily devoid of physical significance, and they can play a crucial role in the characterization of quantum states. Here we show that the expectation values of a particular set of non-Hermitian matrices, which we call column operators, directly yield the complex coefficients of a quantum state vector. We provide a definition of the state vector in terms of measurable quantities by decomposing these column operators into observables. The technique we propose renders very-large-scale quantum states significantly more accessible in the laboratory, as we demonstrate by experimentally characterizing a 100,000-dimensional entangled state. This represents an improvement of two orders of magnitude with respect to previous phase-and-amplitude characterizations of discrete entangled states.

One of the current challenges in the field of computing is harnessing the potential processing power provided by quantum devices that exploit entanglement. Experimental research aimed at overcoming this challenge is driven by the production, control and detection of larger and larger entangled quantum states[1-4]. However, the task of characterizing these entangled states quickly becomes intractable as the number of parameters that define a many-body system scales exponentially with the system size. To keep up with the ever-growing quantum state dimensionality, much effort is put into developing efficient characterization methods[5-19].

Quantum state tomography is the process of retrieving the values that define a quantum system. The process typically involves two steps: (i) gathering an informationally complete set of data and (ii) finding the quantum state most consistent with the data set using post-measurement processing such as the algorithm for maximum-likelihood estimation[20]. Many efficient tomographic methods capitalize on the first step by making simplifying assumptions about the state[11-19], thus reducing the number of measurements required to uniquely identify it. In particular, tomography via compressed sensing allows one to efficiently reconstruct quantum states based on the fact that low-rank density matrices, that is, quasi-pure states are sparse in a particular basis[15-17,21]. Compared with assumption-free tomography, compressive sensing provides a square-root improvement on the required number of measurements[10]. This improvement enabled the reconstruction of the density matrices of a six-qubit state[16] and a  $(17\times 17)$ -dimensional state[17], the largest phase-and-amplitude measurement of an entangled state reported to date. Although compressed sensing does not make use of maximum-likelihood estimation, it does require non-trivial post-measurement processing.

Recently, Lundeen et al.19 reported on the direct measurement of a wavefunction using a method that, for the first time, required no complicated post-measurement processing. Their method is based on weak measurements, whereby one weakly couples a quantum system to a pointer state and subsequently performs a few standard strong measurements on the pointer state. The outcome of a weak measurement is known as the 'weak value', and in the conditions exposed in ref. 19, the weak value is proportional to a given state vector coefficient. The method of Lundeen et al. can be used in combination with the assumption that the quantum state at hand is pure, providing the same square-root improvement as compressed sensing. Variations on the original scheme allow measurements of mixed states and increased detection efficiency22-24.

An important contribution of the work by Lundeen et al. was to link the state vector elements to the expectation value of weak measurements. We take a different approach, and point out that the enabling feature that allows access to the complex state vector is not weak measurement but the use of particular non-Hermitian operators. Although weak measurements provide a way to decompose these non-Hermitian operators, it is not the only suitable approach. Moreover, the introduction of weak values in the measurement procedure adds complexity to the experiment and the formalism that links weak values to measurement outcomes involves an approximation that breaks down in a variety of circumstances[24-26].

In this paper, we propose an alternative approach to the direct measurement of quantum states that is exact in the case of pure states, proves to be reliable in the presence of noise, and is consistent with results obtained with well-established tomographic techniques. The key principle of our formalism is to decompose the particular non-Hermitian matrices that yield the complex state vector coefficients using only observables. Our method therefore only requires strong measurements, as in

standard tomography, while maintaining the directness of weak-value-assisted tomography. The simplicity in both the experimental procedure and post-measurement processing renders our method ideally suited for the characterization of large-scale systems, which can be high-dimensional, many-body or both. We begin by developing the theory on which our method is based and then demonstrate the potential of this scheme by experimentally retrieving the complex coefficients of a  $(341 \times 341)$ -dimensional entangled state.

# Results

Theory. Consider a quantum system in a  $d$ -dimensional Hilbert space, whose state vector

$$
| \Psi \rangle = \sum_ {j = 0} ^ {d - 1} c _ {j} | j \rangle \tag {1}
$$

is expanded in the basis  $\{|j\rangle \}$  and where  $c_{j}$  are unknown complex expansion coefficients. To retrieve these coefficients, we introduce the column operators  $\widehat{C}_j = |a\rangle \langle j|$ , where  $|a\rangle$  is an arbitrary reference vector. Each column operator has an expectation value

$$
\langle \widehat {C} _ {j} \rangle = \langle \Psi | a \rangle c _ {j}, \tag {2}
$$

which is proportional to a complex state vector expansion coefficient. Since the value of  $\langle \Psi |a\rangle$  is independent of  $j$ , we can express the state vector in terms of the column operators up to a phase factor:

$$
| \Psi \rangle = \frac {\mathrm {e} ^ {i \phi}}{\nu} \sum_ {j = 0} ^ {d - 1} \langle \widehat {C} _ {j} \rangle | j \rangle , \tag {3}
$$

where  $\nu = |\langle \Psi |a\rangle |$  is a normalization constant. We can ignore the phase factor  $e^{i\phi}$  since it bears no physical significance.

Most column operators  $\widehat{C}_j$  are not Hermitian matrices and are thus not observables. To overcome this apparent constraint, we recognize that any non-Hermitian matrix can be constructed from a complex-weighted sum of Hermitian matrices. Hence, the crucial step to our method is to construct the column operators in terms of measurable quantities:  $\widehat{C}_j = \sum_q w_{jq} \widehat{\mathcal{O}}_{jq}$ , where  $w_{jq}$  are complex weights and  $\widehat{\mathcal{O}}_{jq}$  are observables. As a result, this allows us to retrieve any state vector element with a complex-weighted sum of measurement outcomes:

$$
c _ {j} = \frac {1}{v} \sum_ {q} w _ {j q} \langle \widehat {\mathcal {O}} _ {j q} \rangle . \tag {4}
$$

Equation 4 is an exact definition of the pure state vector that is provided in terms of measurable quantities. The above formalism readily applies to a general class of quantum states, including high-dimensional and many-body systems.

As an example, consider the case of a qubit  $|\Psi \rangle = c_0|0\rangle +c_1|1\rangle$  with  $|a\rangle = |0\rangle$  as the reference vector. The first column operator  $\widehat{C}_0$  is Hermitian and given by the projector  $|0\rangle \langle 0|$ . The second column operator  $\widehat{C}_1 = |0\rangle \langle 1|$  is not Hermitian but can be constructed a number of ways. The first construction—which, as pointed out earlier, is a key part of the weak value formalism—is the complex-weighted sum of Pauli matrices:  $\widehat{C}_1 = (\hat{\sigma}_x + i\hat{\sigma}_y) / 2$ , a decomposition that requires two observables, each of which is made of two projectors or eigenvectors. A second decomposition requiring only three projectors is given by

$$
\widehat {C} _ {1} = \sum_ {q = 0} ^ {2} \frac {2}{3} \mathrm {e} ^ {i 2 \pi q / 3} | s _ {q} \rangle \langle s _ {q} |, \tag {5}
$$

where  $\left| s_{q} \right\rangle = \left( |0\rangle + \mathrm{e}^{i4\pi q / 3} |1\rangle \right) / \sqrt{2}$  are the states onto which the observables  $\widehat{\mathcal{O}}_{1q}$  project. In both cases, the qubit state vector is exactly given by  $|\Psi \rangle = (\langle \widehat{C}_{0} \rangle |0\rangle + \langle \widehat{C}_{1} \rangle |1\rangle) / \langle \widehat{C}_{0} \rangle^{\frac{1}{2}}$ .

Experiment. To demonstrate the power and scalability of our scheme, we apply it to the measurement of a state entangled in greater than 100,000 dimensions. We provide a complete characterization of the spatially entangled two-photon field produced through spontaneous parametric downconversion (SPDC). In general, SPDC can give rise to spatial and frequency correlations between two photons $^{4,27-36}$ . The purity of the spatial part of the full state can only be guaranteed if the two types of correlations are completely decoupled, which can be achieved in the collinear regime $^{27}$ —see Supplementary Note 1 for a theoretical estimation of our system purity. The consequences of applying our scheme to a quantum state with non-unit purity, which is always the case in the presence of noise, will be discussed below.

We express the spatial part of the entangled state in a discrete cylindrical basis of transverse spatial modes. The azimuthal part of the modes is given by  $e^{i\ell \phi}$ , where  $\ell$  is an integer between  $-\infty$  and  $\infty$  and  $\phi$  is the azimuthal angle. This type of phase profile is known to carry  $\ell$  units of orbital angular momentum (OAM). We decompose the radial part of the field with the recently introduced Walsh modes, labelled by the integer  $k$  ranging from 0 to  $\infty$  (ref. 34). The Walsh modes all have the same Gaussian amplitude envelope, but different  $\pi$ -steps radial phase profiles. Combining the OAM modes with the Walsh modes yields a complete basis for coherent two-dimensional images. To perform the characterization of the two-photon spatial field, we consider 31 OAM modes and 11 Walsh modes for each photon. The state vector thus takes the form

$$
| \Phi \rangle = \sum_ {\ell_ {1} = - 1 5} ^ {1 5} \sum_ {k _ {1} = 0} ^ {1 0} \sum_ {\ell_ {2} = 1 5} ^ {- 1 5} \sum_ {k _ {2} = 0} ^ {1 0} c _ {\ell_ {1}, k _ {1}} ^ {\ell_ {2}, k _ {2}} | \ell_ {1}, k _ {1} \rangle | \ell_ {2}, k _ {2} \rangle . \tag {6}
$$

Using the column-operator decomposition described in the Methods section, we sequentially measure all 116,281 coefficients  $c_{\ell_1,k_1}^{\ell_2,k_2}$ , which are shown in Fig. 1a,b. The total Hilbert space dimensionality of this measured state is more than two orders of magnitude larger than any previously reported amplitude-and-phase-characterized discrete entangled state<sup>17</sup>. As a simple verification of the accuracy of our method, we calculate the probabilities associated with each joint mode via the Born rule,  $|c_{\ell_1,k_1}^{\ell_2,k_2}|^2$ , as shown in Fig. 1c. This result is consistent with the directly measured correlation matrix shown in Fig. 1e, showing that we retrieve the correct magnitude of the amplitudes.

To rigorously assess the validity of the directly measured complex quantum state  $|\psi \rangle$ , that is, both the amplitudes and the phases, we compare it to the results obtained through full tomography (that is, assumption-free tomography); see Supplementary Note 2 for details of the algorithm used to retrieve the density matrix. As full tomography cannot be performed on a  $(341\times 341)$ -dimensional entangled state in a reasonable time, we characterize a  $(5\times 5)$ -dimensional subset of the SPDC two-photon state. We perform the comparison in a basis of various OAM modes  $(\ell_1\in \{1, - 1,2, - 2,3\}$ $\ell_{2}\in \{1, - 1,2, - 2, - 3\})$  and a fixed radial Walsh mode  $(k_{1} = k_{2} = 0)$ . The total number of unknown parameters in the corresponding density matrix is equal to 624. After performing the direct measurement procedure in this basis, we record 8,000 random projective measurements that we break into eight sets of 1,000. For each set, we recover a density matrix  $\rho_{\mathrm{exp}}$  and calculate its purity and the fidelity with the directly measured state  $|\psi \rangle$ ; fidelity is defined as  $\sqrt{\langle\psi|\rho_{\mathrm{exp}}|\psi\rangle}$ . On average, the purity calculation yields  $(0.96\pm 0.02)$ , and the fidelity gives  $(0.985\pm 0.004)$ , where the uncertainties correspond to one standard deviation. After reconstruction of a density matrix, we

find that the average error between the measured count rates and the count rates predicted by the density matrix is  $5.5\%$ . This can be explained by shot noise, the pixelated nature of the spatial light modulator (SLM), and the finite aperture of the optical elements. While we expect unit purity, the  $5\%$  noise level accounts for the discrepancy with the measured value.

Simulation with mixed states. The extremely high fidelity between the tomography results  $\rho_{\mathrm{exp}}$  and the directly measured state  $|\psi\rangle$  indicates the validity of our approach for quantum state measurements applied to near pure states. To evaluate our method in the context of mixed states, we perform a series of numerical simulations where we vary the rank, purity and dimension of an unknown state  $\rho_{\mathrm{sim}}$ , where no sources of noise are added to the simulated measurement outcomes. We apply our direct measurement procedure to these states and calculate the fidelity  $|\langle \psi |\psi_{\mathrm{sim}}\rangle|$ , where  $|\psi_{\mathrm{sim}}\rangle$  is the eigenvector of  $\rho_{\mathrm{sim}}$  with the largest eigenvalue. For initial states  $\rho_{\mathrm{sim}}$  with purity  $>0.81$ , we measure a fidelity  $>0.99$  in at least  $99\%$  of the cases. The dependency of this result on the dimensionality of the state is negligible. This result indicates that our direct method enables the extraction of the density matrix primary eigenvector, even for a partially mixed state. Full details of this analysis and the density matrix reconstruction are presented in the Supplementary Note 1.

# Discussion

Knowledge of the amplitude and phase of the state vector elements allows us to perform otherwise inaccessible calculations. As an example, we perform a calculation of the Schmidt decomposition $^{37}$ . This is equivalent to the singular value decomposition for the case of optical transfer matrices. The Schmidt decomposition yields a new joint basis, in which the photons are perfectly correlated and where the joint modes have equal phases, as shown in Fig. 1d. When the Schmidt decomposition is applied to the entire state, we calculate a number of Schmidt modes equal to 142; this represents the effective number of independent joint modes contained within the state (the maximum for a  $(341 \times 341)$ -dimensional state being 341). The Schmidt decomposed two-photon field is a good candidate for the violation of very high-dimensional Bell inequalities $^{29}$ . Further details on the Schmidt decomposition can be found in the Supplementary Note 3.

There are a number of approaches to reducing the necessary cost and effort for measuring large-scale quantum states. These include, but are not limited to, developing technologies for mode sorting $^{38}$  and arbitrary unitary transformations $^{39,40}$ , reducing the required number of measurement settings, and circumventing the requirement for reconstruction procedures. It is clear that there is significant interplay between each of these approaches. The theoretical implementation of an approach that combines the principles of our work with generalized measurements, such as positive operator value measures, is considered in the Supplementary Note 4. The ability to use positive operator value measures in the laboratory relies on the aforementioned technologies. Access to these types of technologies would reduce the overall number of measurement settings to uniquely recover a quantum state. However, such a system requires arbitrary unitary transformations for spatial states, which is in itself an active area of research $^{38-40}$ . Given the limitations of mode sorters for very large dimensions, and the practical nature of projective measurements, our scheme provides a simple and elegant method for the characterization of large-scale quantum states.

Our scheme allows direct access to the complex coefficients that define large-scale quantum states. The main result of our work is a

![](images/8615915854116257aae385e2ce459c7c694f1133416e3bba0c23bfdd35178c93.jpg)  
b Renormalized  $(33\times 33)$  -dimensional subset

![](images/e07ea674b402774229bf94e2196485d46e93321d04cee75457fda4d0c6b8ad12.jpg)  
d Schmidt decomposition

![](images/49beca80ecc335094cdecbb38cc44a22edd70a0751301ddd21cd0ae3d8d50955.jpg)  
C Probabilities calculated from b

![](images/f8265580b86336fa3ab3c37066a41986bd174e51ed62127d7b5f3ea0715f0466.jpg)  
Figure 1 | Measured and calculated properties of the two-photon state. (a) We illustrate the complex state vector coefficients in matrix format. This representation is similar to that of an optical transfer matrix, where the lateral axes correspond to input and output modes. Here, each lateral axis corresponds to the spatial state of one photon of the pair. The OAM values  $\ell$  range from  $-15$  to  $15$ . For a fixed OAM value, the radial index  $k$  ranges from 0 to 10, thus the combined state has  $341 \times 341$  dimensions. The amplitude and phase values of a coefficient are given by the height and colour of a bar, respectively. For clarity, we darken the off-diagonal part. The small subset ( $\mathbf{b}$ ) of the state shows the phase gradient across the diagonal elements, which is typical of a Gouy phase shift, a common property of light passing through focus[43]. The corresponding calculated probability matrix ( $\mathbf{c}$ ) is consistent with the directly measured probabilities ( $\mathbf{e}$ ). Finally, we calculate the Schmidt decomposition ( $\mathbf{d}$ ) of  $\mathbf{b}$ , which gives the joint basis in which the subset can be expressed with the lowest number of modes. The indices  $S_{1}$  and  $S_{2}$  correspond to the states of each photon in this basis.

![](images/d2bacc31cb3cdf262e129d4fcc89dbc06d51e78bd3f1809734d7207338782ee0.jpg)  
e Directly measured probabilities

novel method for retrieving a state vector coefficient with a complex-weighted sum of strong measurement outcomes. One challenge in reconstructing a quantum state from measurement outcomes lies in data processing; our scheme trades the difficulty of data processing for theoretical analysis before the experiment, that is, finding the measurements one has to perform. We anticipate that our work will have an impact on a number of disciplines, for example, quantum parameter estimation, measurement in quantum computing, quantum information and metrology.

# Methods

Experiment. The two-photon field is generated via SPDC with a 405-nm laser diode pumping a 1-mm-long periodically poled KTP (PPKTP) crystal with  $50\mathrm{mW}$  of power. The experimental set-up is shown in Fig. 2. We separate the two photons with a right-angle prism and image the plane of the crystal to a Holoeye SLM with a magnification of  $-10$ . We simultaneously display two holograms, one on each side of the SLM, to control the amplitude and phase profiles of the two photons independently. To make projective measurements of superposition modes, we make use of intensity masking[41]. We image the plane of the SLM with a magnification of  $-1/2,500$  to two single-mode fibres. The combination of the SLM and singles mode fibres allows us to make arbitrary projective measurements. All measurements are performed in coincidence with two single-photon avalanche detectors, with a timing window of  $25\mathrm{ns}$ , an integration time of  $1\mathrm{s}$  for modes

outside the diagonal and  $20\mathrm{s}$  for the diagonal elements  $(\ell_{1} = -\ell_{2}$  and  $k_{1} = k_{2})$  We start an automatic alignment procedure with the SLM every 4 hours to compensate for drift. Including the time it takes to calculate and display a hologram (about 1 s), the entire experiment takes 2 weeks; assumption-free tomography would take more than four centuries at the same acquisition rate. We perform no background subtraction and use the fundamental mode  $(\ell_1 = -\ell_2 = k_1 = k_2 = 0)$  as the reference vector  $|a\rangle$  . The count rate of the fundamental mode is approximately 900 coincidences per second and varies by  $10\%$  over 24-h periods. To correct for long-term drift, we normalize each outcome to the count rate of the fundamental mode, which we measure before the measurement of each column operator. In standard tomography, the calculation of error bounds on the measured state is not a straightforward task42. Here, we can calculate the error bound on a given coefficient with a weighted sum of the detector counts used to retrieve it. For a given state vector coefficient, the errors on the amplitude  $|c_j|$  and phase  $\arg (c_j)$  are both inversely proportional to the overlap  $\nu$  of the reference vector with the quantum state. To minimize the errors, it is important to choose a reference vector that has a high probability of occurrence within the state—the fundamental mode is the most probable one in our case.

Two-body column-operator decomposition. To decompose a given state vector coefficient  $c_{\ell_1,k_1}^{\ell_2,k_2}$  into a set of measurement outcomes, we need to find a projector decomposition of the corresponding column operator  $\widehat{C}_{\ell_1,k_1}^{\ell_2,k_2} = |0,0\rangle \langle \ell_1,k_1| \otimes |0,0\rangle \langle \ell_2,k_2|$ , as in equation 4. We numerically find this column-operator decomposition, that is, the complex weights  $w_{q}$  and the

![](images/686b2fa6896985b8810491eb9697c938b0e31be32af769c8c811cd001c19800b.jpg)  
Figure 2 | Generation and characterization of a two-photon field. The entangled state is produced via SPDC in a PPKTP crystal and spatially separated by a prism. For the state determination stage, the crystal plane is imaged onto a SLM, which is in turn imaged to the input facet of two single-mode fibres. To make a given projective measurement, we display the corresponding joint mode on the SLM and measure the coincidence rate between the two single-photon avalanche diode detectors. The inset shows the five joint holograms that correspond to the column-operator decomposition of  $\widehat{C}_{2,0}^{-2,0}$ . The state vector coefficient  $c_{2,0}^{-2,0}$  is given by  $\frac{4}{5\nu}\sum_q\left\langle \widehat{\mathcal{O}}_q\right\rangle \mathrm{e}^{\mathrm{i}4\pi q / 5}$ , where the expectation value of a given observable is proportional to the measured count rate when displaying the corresponding hologram.

observables  $\widehat{\mathcal{O}}_q$ , using the differential evolution algorithm (see Supplementary Note 5). By inspection, we find that the corresponding analytical form of the state vector coefficients is given by

$$
\widehat {G} _ {\ell_ {1}, k _ {1}} ^ {\ell_ {2}, k _ {2}} = \frac {1}{v} \sum_ {q = 0} ^ {4} \frac {4}{5} e ^ {i 2 \pi q / 5} | s _ {1, q} \rangle \langle s _ {1, q} | \otimes | s _ {2, q} \rangle \langle s _ {2, q} |, \tag {7}
$$

where  $\sqrt{2} |s_{m,q}\rangle = |0,0\rangle +\mathrm{e}^{i4\pi q / 5}|\ell_m,k_m\rangle$  with  $m = \{1,2\}$ , and  $\nu = |\langle \Psi |0,0\rangle |$  is a normalization constant. This decomposition is only valid when the state of any photon is different from the reference vector, that is,  $|\ell_m,k_m\rangle \neq |0,0\rangle$ . Each coefficient measured with the above column-operator decomposition requires five projective measurements, thus explaining the  $5D^2$  scaling, where  $D$  is the Hilbert space dimensionality of a single particle. The protocol scales much more favourably than assumption-free tomography, which requires  $D^4$  projections.

Here, we briefly explain our protocol for measuring the entire SPDC state vector. We measure more than  $99\%$  of the coefficients using the decomposition of equation 7. The remaining column operators are the special cases  $\langle 0,0\rangle \langle \ell_1,k_1|\otimes |0,0\rangle \langle 0,0|$  and  $\langle 0,0\rangle \langle 0,0|\otimes |0,0\rangle \langle \ell_2,k_2|$ , which respectively correspond to a row and a column of the result shown in Fig. 1a. These column operators can be decomposed into only three joint local measurements using the projector  $\langle 0,0\rangle \langle 0,0|$  on one system and a column-operator decomposition similar to that of equation 5 on the other system. Finally, the column operator  $\langle 0,0\rangle \langle 0,0|\otimes |0,0\rangle \langle 0,0|$  is a projector, and its expectation value can be measured in a single experimental configuration.

Full quantum tomography. We perform full tomography with high count rates in order to achieve high accuracy. We set the magnification between the plane of the SLM and that of the single-mode fibres to 1/400. In this condition, we obtain a count rate of approximately 18,000 counts per second for the fundamental mode and integrate over 1 s for each individual projective measurement. The increase in the count rate of the fundamental mode comes at the price of lower count rates for high order modes. Regarding the full tomography measurements, we take an overcomplete set of 1,000 random projective measurements in a  $(5\times 5)$ -dimensional space. To minimize high-frequency components on the SLM, we limit the random superpositions to two-dimensional subsets of the state space.

# References

1. Monz, T. et al. 14-Qubit entanglement: creation and coherence. Phys. Rev. Lett. 106, 130506 (2011).  
2. Yao, X. C. et al. Observation of eight-photon entanglement. Nat. Photon. 6, 225-228 (2012).  
3. Yokoyama, S. et al. Ultra-large-scale continuous-variable cluster states multiplexed in the time domain. Nat. Photon. 7, 982-986 (2013).

4. Krenn, M. et al. Generation and confirmation of a  $(100 \times 100)$ -dimensional entangled quantum system. Proc. Natl Acad. Sci. USA 111, 6243-6247 (2014).  
5. Smith, B. J., Killett, B., Raymer, M. G., Walmsley, I. A. & Banaszek, K. Measurement of the transverse spatial quantum state of light at the single-photon level. Opt. Lett. 30, 3365-3367 (2005).  
6. Bogdanov, Y. I. et al. Statistical estimation of the efficiency of quantum state tomography protocols. Phys. Rev. Lett. 105, 010404 (2010).  
7. Mahler, D. H. et al. Adaptive quantum state tomography improves accuracy quadratically. Phys. Rev. Lett. 111, 183601 (2013).  
8. Teo, Y. S., Reháček, J. & Hradil, Z. Informationally incomplete quantum tomography. Quant. Meas. Quant. Metro 1, 57-83 (2013).  
9. Ferrie, C. Self-guided quantum tomography. Phys. Rev. Lett. 113, 190404 (2014).  
10. Banaszek, K., Cramer, M. & Gross, D. Focus on quantum tomography. New J. Phys. 15, 125020 (2013).  
11. Shabani, A. et al. Efficient measurement of quantum dynamics via compressive sensing. Phys. Rev. Lett. 106, 100401 (2011).  
12. Flammia, S. T., Silberfarb, A. & Caves, C. M. Minimal informationally complete measurements for pure states. Found. Phys. 35, 1985-2006 (2005).  
13. Cramer, M. et al. Efficient quantum state tomography. Nat. Commun. 1, 149 (2010).  
14. Toth, G. et al. Permutationally invariant quantum tomography. Phys. Rev. Lett. 105, 250403 (2010).  
15. Gross, D., Liu, Y.-K., Flammia, S. T., Becker, S. & Eisert, J. Quantum state tomography via compressed sensing. Phys. Rev. Lett. 105, 150401 (2010).  
16. Schwemmer, C. et al. Experimental comparison of efficient tomography schemes for a six-qubit state. Phys. Rev. Lett. 113, 040503 (2014).  
17. Tonolini, F., Chan, S., Agnew, M., Lindsay, A. & Leach, J. Reconstructing high-dimensional two-photon entangled states via compressive sensing. Sci. Rep. 4, 6542 (2014).  
18. Lloyd, S., Mohseni, M. & Rebentrost, P. Quantum principal component analysis. Nat. Phys. 10, 631-633 (2014).  
19. Lundeen, J. S., Sutherland, B., Patel, A., Stewart, C. & Bamber, C. Direct measurement of the quantum wavefunction. Nature 474, 188-191 (2012).  
20. Banaszek, K., D'Ariano, G. M., Paris, M. G. A. & Sacchi, M. F. Maximum-likelihood estimation of the density matrix. Phys. Rev. A 61, 10304 (2000).  
21. Liu, W.-T., Zhang, T., Liu, J.-Y., Chen, P.-X. & Yuan, J.-M. Experimental quantum state tomography via compressed sampling. Phys. Rev. Lett. 108, 170403 (2012).  
22. Bamber, C. & Lundeen, J. S. Observing Dirac's classical phase space analog to the quantum state. Phys. Rev. Lett. 112, 070405 (2014).  
23. Wu, S. State tomography via weak measurements. Sci. Rep. 3, 1193 (2013).  
24. Salvail, J. Z. et al. Full characterization of polarization states of light via direct measurement. Nat. Photon. 7, 1-6 (2013).  
25. Duck, I. M., Stevenson, P. M. & Sudarshan, E. C. G. The sense in which a 'weak measurement' of a spin  $1/2$  particle's spin component yields a value 100. Phys. Rev. A 40, 2112-2117 (1989).  
26. Malik, M. et al. Direct measurement of a 27-dimensional orbital-angular-momentum state vector. Nat. Commun. 5, 3115 (2014).  
27. Osorio, C. I., Valencia, A. & Torres, J. P. Spatiotemporal correlations in entangled photons generated by spontaneous parametric down conversion. New J. Phys. 10, 113012 (2008).  
28. Miatto, F. M., Yao, A. M. & Barnett, S. M. Full characterization of the quantum spiral bandwidth of entangled biphotons. Phys. Rev. A 83, 033816 (2011).  
29. Dada, A. C., Leach, J., Buller, G. S., Padgett, M. J. & Andersson, E. Experimental high-dimensional two-photon entanglement and violations of generalized Bell inequalities. Nat. Phys. 7, 1-4 (2011).  
30. Agnew, M., Leach, J., McLaren, M., Roux, F. S. & Boyd, R. W. Tomography of the quantum state of photons entangled in high dimensions. Phys. Rev. A 84, 062101 (2011).  
31. Leach, J., Bolduc, E., Gauthier, D. J. & Boyd, R. W. Secure information capacity of photons entangled in many dimensions. Phys. Rev. A 85, 060304 (2012).  
32. Salakhutdinov, V. D., Eliel, E. R. & Löffler, W. Full-field quantum correlations of spatially entangled photons. Phys. Rev. Lett. 108, 173604 (2012).  
33. Tasca, D. S. et al. Imaging high-dimensional spatial entanglement with a camera. Nat. Commun. 3, 3:984 (2012).  
34. Geelen, D. & Löffler, W. Walsh modes and radial quantum correlations of spatially entangled photons. Opt. Lett. 38, 4108-4111 (2013).  
35. Mosley, P. J., Lundeen, J. S., Smith, B. J. & Walmsley, I. A. Conditional preparation of single photons using parametric downconversion: a recipe for purity. New J. Phys. 10, 093011 (2008).  
36. Osorio, C. I., Sangouard, N. & Thew, R. T. On the purity and indistinguishability of down-converted photons. J. Phys. B: At. Mol. Opt. Phys. 46, 055501 (2013).

37. Ekert, A. & Knight, P. L. Entangled quantum systems and the Schmidt decomposition. Am. J. Phys. 63, 415-423 (1995).  
38. Berkhout, G. C. G. et al. Efficient sorting of orbital angular momentum states of light. Phys. Rev. Lett. 105, 153601 (2010).  
39. Morizur, J.-F. et al. Programmable unitary spatial mode manipulation. J. Opt. Soc. Am. A Opt. Image Sci. Vis. 27, 2524-2531 (2010).  
40. Miller, D. Reconfigurable add-drop multiplexer for spatial modes. Opt. Express 21, 20220-20229 (2013).  
41. Bolduc, E., Bent, N., Santamato, E., Karimi, E. & Boyd, R. W. Exact solution to simultaneous intensity and phase encryption with a single phase-only hologram. Opt. Lett. 38, 3546-3549 (2013).  
42. Christandl, M. & Renner, R. Reliable Quantum State Tomography. Phys. Rev. Lett. 109, 120403 (2012).  
43. Boyd, R. W. Intuitive explanation of the phase anomaly of focused light beams. J. Opt. Soc. Am. 70, 877-880 (1980).

# Acknowledgements

E.B. and G.G. acknowledge the financial support of the FQRNT, grants #176729 and #173779. J.L. acknowledges the financial support of the Engineering and Physical Sciences Research Council (EPSRC, UK, Grants EP/M006514/1 and EP/M01326X/1). We thank Erik Gauger and George Knee for helpful discussions and feedback.

# Author contributions

E.B. conceived the method. E.B. and G.G. developed the theory. E.B. and J.L. designed and performed the experiment and analysed the data. J.L. provided guidance throughout the project. All authors contributed to the manuscript.

# Additional information

Supplementary Information accompanies this paper at http://www.nature.com/naturecommunications

Competing financial interests: The authors declare no competing financial interests.

Reprints and permission information is available online at http://npg.nature.com/reprintsandpermissions/

How to cite this article: Bolduc, E. et al. Direct measurement of large-scale quantum states via expectation values of non-Hermitian matrices. Nat. Commun. 7:10439 doi: 10.1038/ncomms10439 (2016).

![](images/f344dc2fc772c1a505604a9a84c80abb520bf75d9f8e4f668749a411289cdf3e.jpg)

This work is licensed under a Creative Commons Attribution 4.0 International License. The images or other third party material in this

article are included in the article's Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder to reproduce the material. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/