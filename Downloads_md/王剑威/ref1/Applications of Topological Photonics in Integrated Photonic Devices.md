# Applications of Topological Photonics in Integrated Photonic Devices

You Wu, Chong Li, Xiaoyong Hu,* Yutian Ao, Yifan Zhao, and Qihuang Gong

Topological photonics is an emerging field of research, which is inspired by the discovery of topological insulators. The introduction of topology endows traditional photonic systems with brand new properties, including unidirectional propagating edge states and robustness against impurities or defect without backscattering. With the further development of theoretical research on topological photonics, many new photonic devices have been proposed and experimentally demonstrated, showing its broad prospects in constructing high-performance integrated photonic chips. Topology, as a new research perspective in photonics, is expected to bring about remarkable changes to the field of integrated photonic devices and optical interconnection. This review summarizes the fundamental realization principles of topology in photonic systems, comparison of topology in photonics and electronics, applications of topological photonics in integrated photonic devices and related optical effects. Finally, a brief outlook on the challenges and future development direction in the pursuit of the application of topological photonics in integrated photonic devices is provided.

# 1. Introduction

In 2005, Haldane and Raghu introduced topology to photonics, opening up a brand new research direction in the realm of photonics and characterizing the beginning of topological photonics.[1,2] This idea of photonic topological insulators (PTIs) is inspired by the enormous achievements of topological insulators in recent decades, where topology was introduced to characterize the phase of matter in condensed matter physics.[3,4] After the discovery of quantum Hall (QH) effect in 1980, quantum anomalous Hall (QAH) effect, quantum spin Hall (QSH) effect and topological insulators were further discovered, prompting the development and applications of topological insulators.[5-8]

Dr. Y. Wu, Dr. C. Li, Prof. X. Hu, Dr. Y. Ao, Y. Zhao, Prof. Q. Gong

State Key Laboratory for Mesoscopic

Physics & Department of Physics

Collaborative Innovation Center of Quantum Matter

Peking University

Beijing 100871, P. R. China

E-mail: xiaoyonghu@pku.edu.cn

Prof. X. Hu, Prof. Q. Gong

Collaborative Innovation Center of Extreme Optics

Shanxi University

Taiyuan, Shanxi 30006, P. R. China

DOI: 10.1002/adom.201700357

One of the most inspiring characters of topological insulators is the electrical conductivity on the surface without dissipation or backscattering and insulation in the bulk.[3] In topological photonics, a PTI also possesses similar robust edge states. Electromagnetic waves can propagate unidirectionally along the edge of a PTI without backscattering regardless of the presence of disorder or defect.[9] For a long time, researches on photonics mainly take advantage of frequency, wave vector, polarization or phase. However, topology, as a new research perspective in the field of photonics, has enormous potential in future applications in integrated photonic devices and ultrahigh-speed information processing chips.

On the one hand, the most important and fundamental property of unidirectional propagation of light along the edge of two topologically different bulk mate

rials makes it possible to exploit low-loss transmission devices and dispense with optical isolators. On the other hand, the robust topological protection ensures the perfect performance of integrated photonic devices even with the existence of impurities or fabrication imperfections. Based on this idea, many new photonic devices have been developed, many of which are combined with some optical effects such as nonlinear Kerr effect, magneto-optic (MO) effect, magneto-electric coupling and so on.[10-12] By means of these optical effects, more abundant device functions can be produced.

In this review, we discuss the recent progress towards principle and experiment of topological photonics, and most importantly, applications of topological photonics in integrated photonic devices. We begin with a detailed exposition of basic concepts of topological photonics, from intuitively mathematical concept of topology to abstract band topology. Realization principles of photonic topology in different dimensions are discussed in depth, and a comparison of topology in photonic systems and electronic systems is presented. Then we focus on the applications of topological photonic in integrated photonic devices. We present different kinds of photonic devices including light source devices, light transmission devices, optical signal processing devices and other functional devices. Some important optical effects often involved in topological photonics are also discussed in detail. In the last section, we give a brief outlook on the remaining research challenges, development directions, and future prospects of topological photonic devices.

# 2. Basic Concepts and Realization Principles

# 2.1. Basic Principles and Concepts of Topological Photonics

According to Gauss-Bonnet theorem, integrating the Gaussian curvature of a closed surface, one will get an integer characterizing its topological properties. Similarly, performing the integration of the Berry curvature over an energy band of a periodical structure gives the topological invariant, or Chern number, which describes the topological property of an optical system and provides us with a new research perspective. The mathematical expression of Chern number in a two-dimensional (2D) Brillouin zone is written as

$$
C = \frac {1}{2 \pi} \oiint \nabla_ {\mathbf {k}} \times \left\langle u (\mathbf {k}) | i \nabla_ {\mathbf {k}} | u (\mathbf {k}) \right\rangle \cdot d ^ {2} \mathbf {k} \tag {1}
$$

where  $|u(\mathbf{k})\rangle$  is the Bloch wave function of each point on the energy band, and  $\mathbf{k}$  is the Bloch wave vector. Lu et al.[13] made a comparison between the Berry phase and the Aharonov-Bohm (AB) phase and pointed out that the Chern number can be viewed as the number of monopoles of Berry flux inside a closed surface from the similarity of their math formulas.

In layman's terms, the value of an orientable surface's genus is equal to the number of "holes" it has. It is very intuitive that a sphere has genus zero while a torus has genus one. It is obvious that the number of holes remain unchanged under any kind of kneading without cutting or pasting. For example, kneading a dough from a ball to a spoon without any hole, from a donut to a mug with a one-hole handle and so on. The shape has been changed a lot but still maintains the topological equivalence. The topological property is preserved under continuous deformations of a geometry, which implies that this property is robust and global. Since small perturbations will not affect this global property, it can be regarded as the origin of some strong and remarkable physical phenomena, such as robust edge states.

Topological insulators possess the properties such as insulation in the bulk, electrical conductivity on the surface, and moreover, resistance to dissipation and backscattering. The analogy of QH effect in photonic systems was first raised by Haldane and Raghu.[1] They demonstrated that the essential requirement of integer QH effect is broken time-reversal  $(T)$  symmetry rather than Landau-level quantization, thus indicating the possibility of constructing PTIs if  $T$ -symmetry is broken, even though photons and electrons are totally different particles. Since then, topological photonics has developed rapidly and various methods of realizing analogues to such effects in electronics have been put forward, which will be discussed later.

The typical and important physical phenomenon of topological photonics is the special edge state resisting the defects and backscatteringback scattering. Ordinary edge state often appears between two insulators, or equivalently, two structures with energy or frequency gap. In optics, it is well known that light cannot travel in the bulk when its frequency locates in any band gaps. Thus, at an interface between two photonic crystals or any other structures with a band gap, light with forbidden frequency will be limited in the bulk and can only propagate

![](images/ecbf9c98beef3eff13c1979058ebadedc1df191ec484aa0fd9254ec6a04dec78.jpg)

You Wu is a doctoral candidate student of Prof. Xiaoyong Hu at Peking University. He received his B.S. in Physics from Peking University. His current research focuses on the study of mesoscopic optics and nanophotonics.

![](images/2fd659cf87c00da617b05c19e582e2ac9a6230de7aab714adc79f04aed376f28.jpg)

Xiaoyong Hu is the Cheung Kong Professor of Physics at Peking University. He worked as a postdoctoral fellow with Prof. Qihuang Gong at Peking University from 2004 to 2006. Then he joined Prof. Gong's research group. Prof. Hu's current research interests include photonic crystals and nonlinear optics.

![](images/5612d27278f868db46e0f5089abcd9af7cb7b192e6e3eb6de55d740387de60bb.jpg)

Qihuang Gong is the Cheung Kong Professor of Physics at Peking University, China, where he is also the Founding Director of the Institute of Modern Optics. He is a Member of Chinese Academy of Sciences and a Standing Committee member of China Association for Science and Technology. His current research interests are in

ultrafast optics, nonlinear optics, and mesoscopic optical devices for applications.

at the interface, exhibiting the edge state. Furthermore, light travels both directions at the edge as there is nothing different between the left and the right directions. Apparently, backscattering occurs when light comes across a scatterer near the edge, resulting in significant energy loss. Therefore, the novel and remarkable nontrivial topological edge state, with its robust unidirectional ability, has drawn much attention. In brief, the nontrivial topological edge state can take place when there exists bulk band with non-zero Chern number. From the aspect of band structure, trivial edge state whose bulk band gives zero Chern number, corresponding with the circumstance above, is located in the bulk band gap, but the edge band is generally independent of the bulk band with positive and negative slope coexisting. However, when bulk bands between the interface own different topological invariants, a topological phase transition must happen, i.e., a bulk band cannot smoothly link to

another which has a different Chern number. The topological phase transition requires band structures to close at the interface and reopen on the other side. It is this exact topological phase transition that generates the gapless and single-sign slope edge band at the interface, and the sign of edge band slope determines the direction of propagation. Furthermore, the number and the sign of edge state bands depend on the difference of Chern number,  $\Delta C$ , across the interface. In general, the number of the edge bands equals  $\Delta C$ , which is the conclusion from "bulk-edge correspondence".[3,13] These unidirectional edge modes are robust based on the analysis above that the topological invariant is a global property. The Chern number of a bulk band is preserved under local disturbance, so backscattering will not exist backscattering as long as the single-sign edge mode is unchanged. When it comes across a scatterer under this circumstance, light will detour around it.

However, in a general case, photonic crystals or other periodic structures all give zero Chern number. Therefore, acquiring a non-zero Chern number is the key point to design nontrivial topological edge state. A common method is starting from the Dirac point in a 2D dispersion structure, which can be interpreted as a phase transformation point from trivial to nontrivial topology. Parity inversion  $(\mathcal{P})$  symmetry and  $\mathcal{T}$ -symmetry are of vital importance for Dirac points to stably exist in two dimensions. Breaking either  $\mathcal{T}$ -symmetry or  $\mathcal{P}$ -symmetry can make the two bands split apart and gain a non-zero Berry curvature, which is the integrand of the Chern number expression.[2] Furthermore, broken  $\mathcal{P}$ -symmetry makes the Berry curvature an odd function of Bloch wave vector, while broken  $\mathcal{T}$ -symmetry makes it an even function. As a result, the integration gives a non-zero Chern number only under broken  $\mathcal{T}$ -symmetry. Hence breaking  $\mathcal{T}$ -symmetry by constructing special conditions and using various optical effects is a direct way to gain nontrivial edge state. In the next part, we will simply introduce and summarize the method of realizing nontrivial edge state according to the classification by dimension.

# 2.2. Realization Methods of Topological Photonic States

# 2.2.1. One-Dimensional Systems with Localized Edge States

As the analyses are all based on the analogy of topological insulators in QH effect, most theories and methods above to obtain a nontrivial edge state are only applicable to 2D systems. It can be seen apparently from the math expression of Chern number that Berry curvature cannot be defined in one-dimensional (1D) systems as the curl operator becomes invalid. Besides, the boundary of a 1D system is a point thus it cannot support transporting state. Even so, there are still many studies on 1D topological photonics in recent years. These studies can be roughly divided into three types, which originate from the Aubry-Andre or Harper (AAH) model,[14,15] the Kitaev model[16] and the Su-Schrieffer-Heeger (SSH) model.[17-19] AAH model indicates that there exists localization transition in certain quasiperiodic system, which demands an incommensurate potential mimicking disorder in a 1D tight binding model.[20] This quasiperiodic AAH model has been realized in photonic lattices with localization transition experimentally.[21] In fact, the

1D quasiperiodic model can be viewed as the projection of 2D QH effect, and the configuration of waveguide array as the quasicrystal is shown in Figure 1a, where the propagation in the waveguide is an equivalent of time evolution. The researchers observed the topologically protected edge states in this structure and indicated that in this framework, a system of three-dimensional (3D) quasicrystals may exhibit six-dimensional topological properties.[21] Later on, the topological phase transition was observed with the splicing of two topologically distinct quasicrystals,[22] and another configuration by the use of long-range coupled resonant excitations in 1D sequence structure was demonstrated to have radiative topological states under AAH model.[23] Distinguished from AAH model, the Kitaev

![](images/86b3c04e1cbf90511f06b6ac2bafa19c3443f5707557b9ff666b0b4548df657f.jpg)

![](images/d98d3c5f418efc64e709de8ef1f4ff5f72b0922f844dcb1757561af29a28b2f1.jpg)

![](images/f8f762c6434fa4fa2cce27b753cff6da0a3473f626bbb72a3f1770879def62d8.jpg)  
Figure 1. a) Configuration of the photonic quasicrystal, in which the coupling distance slowly varying along the propagation direction and the experiment results of the observation that light injected from the right edge evolved to the lift edge. b) The schematic diagram of a plasmonic zigzag chain, which exhibits different edge modes depending on the polarization of incident light. c) Transmission spectrum of a 1D structure with an interface made up of two simple 1D photonic crystals and band structures of them with Zak phase marked on every band. In the transmission spectrum, there is a peak in the band gap, indicating the appearance of interface state. a) Reproduced with permission.[21] Copyright 2012, American Physical Society. b) Reproduced with permission.[24] Copyright 2014, American Chemical Society. c) Reproduced under the terms of Creative Commons Attribution 3.0 License.[26]

model has been researched mainly on the zigzag chains of nanoparticles in photonic system. Till now, both the metal and dielectric have been investigated to have the Majorana topological edge states.[24,25] The nanoparticles were arranged into the zigzag chain as Figure 1b shows. Different edge modes appear as the polarization of incident wave varies. Noted that there exists connotative relevance among these models since Ganeshan et al. indicated topological properties of the 1D Majorana chain is relevant to topological phase in the commensurate AAH model.[20] The third one, the SSH model, first applied to polyacetylene, has attracted much attention in optics and has brought about many theoretical and experimental results.[26-30] Under this model, the Zak phase is considered to be a topological invariant, which is supposed to be the indication of edge state. Zak phase is given as

$$
\theta_ {\mathrm {z a k}} = \int_ {\text {F B Z u n i t}} [ i \int \varepsilon (z) u _ {\mathbf {k}} ^ {*} (z) \partial_ {\mathbf {k}} u _ {\mathbf {k}} (z) \mathrm {d} z ] \mathrm {d} \mathbf {k} \tag {2}
$$

in 1D photonic crystal, where  $\mathfrak{u}_k(z)$  is the normalized Bloch function of each point on the dispersion curve,  $k$  is the Bloch wave vector and  $z$  is the coordinate in real space, and the range of the outer integration is the first Brillouin zone. Xiao et al.[26] obtained the edge state at the interface of two photonic crystals joint together with distinct Zak phase at two sides by means of adjusting the structure parameters. As a result, a transmission peak appears in the band gap attributed to the existing of edge state, and the result is shown in Figure 1c. Choi et al.[29] expanded this interface mode to multi-frequency and Poli et al.[27] realized an enhanced edge state by introducing absorption in the bulk. Noted that Redondo et al.[30] experimentally studied this kind of topologically protected states and by expanding the 1D configuration to waveguide array, they distinguished the trivial defect states with the topological interface state. In spite of rich physics embodied in 1D system, it could be barely used in device applications without transmission property.

# 2.2.2. Two-Dimensional Systems with Robust Unidirectional Propagating Edge States

2D photonic systems possess much more abundant physics and phenomena, comparing with 1D ones. On account of the existence of the robust unidirectional edge state, it gives a fairly bright prospect of application in traditional photonic device and photonic information processing. Typical classification scheme of the realization methods of 2D PTIs consists of gyromagnetic photonic crystals, coupled resonators and bianisotropic metamaterials.[13] Here, we will briefly introduce these methods and recent researches based on these concepts.

Breaking  $\mathcal{T}$ -symmetry is of vital importance to generate a nontrivial topological edge state. As the MO materials provide a direct way to break  $\mathcal{T}$ -symmetry by introducing gyromagnetic anisotropy, Wang et al.[9,31] successfully obtained the unidirectional edge state based on ferrite rods crystal at microwave frequencies in both numerical simulations and experiments. Under the effect of magnetic field, the magnetic permeability tensor gains an anti-symmetric imaginary off-diagonal terms,

which is the root cause of the breaking of  $\mathcal{T}$ -symmetry. The electromagnetic field distribution is shown in Figure 2a. Owing to the topological protection, it is clear that backscattering is forbidden even with a slab of perfect electrical conductor inserted in the light path. Essentially, the counter-propagation mode is totally nonexistent, and therefore reflection is forbidden here. On this basis, Skirlo et al.[32] proposed a kind of multimode one-way waveguides with large Chern number difference at the interface. They presented that new topological phases were found by simultaneously gapping multiple Dirac and quadratic points in this photonic system. Since large  $\Delta C$  indicates more than one modes are supported, it can be utilized to realize a power splitter by modulating the mode of incident light as shown in Figure 2b. By controlling the height of the metal scatterer inserting beside the point source, light would travel in either of the two channels. Later on, they fabricated this system and detected the phase of edge modes, and by performing the Fourier transform on it, they obtained the dispersion curve, which is in agreement with the calculation results.[33] Besides, Zang et al.[34] put forward another realization to generate a one-way edge state under this framework by employing two equal and opposite magnetic fields on two regions to form the interface where the field flips. The ability of resisting defect was confirmed by the numerical simulation. In addition, all simulations and experiments discussed above applied a metal wall covered and surrounded to confine the microwave and avoid radiation to free space, and the surrounding metal also played the role of a trivial mirror to form an edge. Poo et al.[35] designed a honeycomb magnetic photonic crystal with zigzag edge that can realize a self-guiding unidirectional electromagnetic edge state, which means there is no need for a bounding wall to form the confine. Recently, more researches on this basis are in progress, exploring more methods to design and utilize the robust edge state.[36] However, gyromagnetic photonic crystals cannot be applied to optical frequencies on account of the lack of materials with effective magnetic response at this frequency band.

Configuration with coupled resonators provides a quite different route to design topological edge states. There is larger space to design and tune in a periodic system with coupling. So far, two basic types have been presented recent years in this field, which can be distinguished according to whether  $\mathcal{T}$ -symmetry is broken. A realizable linear system with coupled resonator optical waveguides (CROW) successfully exhibit an edge state without breaking  $\mathcal{T}$ -symmetry at the wavelength of  $1550~\mathrm{nm}$ .[12] By carefully designing parameters to mimic a 2D magnetic tight-binding Hamiltonian, two opposite orientations are distinguished as there is an opposite phase accumulation analogous to the AB phase of electrons. They also acquired the Hofstadter butterfly spectrum to verify the artificial gauge field. By the way, there exist other methods to construct the artificial gauge field in such a coupled lattice system like mimicking the pseudo-spin by polarization.[37] Opposite edge state was observed with positive and negative detuning of resonance frequency. More detailed experiments and discussions are presented in their later articles,[38,39] and the simulation results are shown in Figure 2c. Liang et al.[40] realized a zero-field lattice possessing the topological property based on a CROW system. They demonstrated that such a system can exhibit an edge state without the design of synthetic gauge field by the

![](images/e7d3bf9723c09e8d9d0bb43afd2900f9a6d3aa13ce77d4150a889369ec22bd6d.jpg)  
(a)

![](images/a427c1e1f36e005132a0b4137e3bb7fee437cdcee29bf94dad8fd5ff52b6b269.jpg)  
(d)  
(e)

![](images/b4107a5ed52e93b4ad850f186e1688a56d2b98836e255515a90c8e81cd7b26cf.jpg)  
(b)

![](images/d1e84ed6c0e8c00359bd44938fea7af09c3754dc1f19ef6d578671ee6f10128d.jpg)  
Figure 2. a) The field distribution of the one-way edge state without backscattering when inserting a slab of perfect electrical conductor in the gyromagnetic photonic crystal. b) Schematic diagram of a path choice device. By controlling the metal height inserting beside the light source, different modes can be acquired and propagate along different interfaces. c) The simulation results of the coupled resonant optical waveguides. The upper two are the field distributions of the long edge states with different scale, while the lower two are the bulk states. d) The configuration of helical waveguides to realize the conversion from time modulation to spatial modulation. The propagation along axis  $z$  is equivalent to time evolution. e) Structural map of a bianisotropic metamaterial with an interface of two regions owning opposite bianisotropy coefficients, which is achieved by the different position of the air gap. f) Edge state of configuration in e), indicating that two different pseudo-spin modes propagate along opposite directions. a) Reproduced with permission.[31] Copyright 2008, American Physical Society. b) Reproduced with permission.[32] Copyright 2014, American Physical Society. c) Reproduced with permission.[39] Copyright 2014, American Physical Society. d) Reproduced with permission, Macmillan Publishers Ltd: Nature,[44] copyright 2013. e,f) Reproduced with permission.[49] Copyright 2015, American Physical Society.

![](images/22f39f350d5464eb2724286efb22ed4e455ed11ee02626d2fd5a5a61789a45e7.jpg)  
(c)  
(f)

![](images/666ffa914982419ead5a16b8a33191cdcd3d0d93f76e78a1eba5f0de06f0064b.jpg)

transfer matrix method and numerical simulation. Noted that these two configurations look similar but have entirely different physical origin as the latter requires strong coupling between the site and link resonant, and gives only one certain direction edge state when the pseudo-spin is determined. However, these structures above are  $\mathcal{T}$  invariant, i.e., there exist the time-reversal modes all the time without the  $\mathcal{T}$ -symmetry protection. Even so, it still retains the nontrivial topological properties on account of the physical origin. In detail, if we idealize the coupling and propagation without reflection, a single ring with two orientations can be regarded as a point with two intrinsic spins. In this sense, we could consider the CROW system as a real topological insulator resisting against any disorder, except if it leads to spin flipping. To be more intuitive, Gao et al.[41] constructed this CROW lattice in a surface plasmon polariton (SPP) system. They carried out a great deal of simulations and experiments with different defects to explore the protection property of this system. Their results show that defects like altering or removing a lattice ring can be protected, while defects like gradually decreasing heights of the rods in the defect ring or inserting a metallic block in a ring can destroy the unidirectional edge state due to the introduction of spin flipping as discussed above.

Dynamic modulation based on the coupled resonant scheme is the other method to construct nontrivial topological system with  $T$ -symmetry broken, which is known as Floquet topological insulators. Dynamic modulation in time domain is under

the description of Floquet's theory. Fang et al.[42] first put forward a configuration on the basis of coupled resonant system. They constructed effective magnetic field through applying the time modulation to the coupling constant. In addition, they pointed out that this magnetic field is effective in real space to make photons act as electrons and do circular motion. Not surprisingly, nontrivial topological edge state with robustness appeared under their simulation. Recently, Yuan and Fan[43] carried out a further research. By applying dynamic modulation in the ultrastrong-coupling regime, they gained a one-way edge mode with larger bandwidth and less susceptible to loss. Since there is a lack of effective methods of realizing accurate control of modulation in time dimension, dynamic modulation can be quite difficult to realize in experiment. A new scheme was proposed by Rechtsman et al.[44] by converting the time modulation to spatial modulation. They expanded the resonant sites to helical waveguides, which made the propagation along the coordinate  $z$  behaves as time evolution, which is shown in Figure 2d.[44] On account of the space variation along  $z$ , effective  $\mathcal{T}$ -symmetry was broken and the nontrivial Floquet band emerged. Deservedly, the edge state associated with topological protection appeared and was observed in experiment. Since the configuration is operable to generate topological state, a series of exploration based on this helical waveguide structure was put forward, such as nonlinear self-localized wave packets,[45] unpaired Dirac cones[46] and even Penrose quasicrystals that acquire robust edge modes.[47] Noted that topological transitions

can be also achieved by tuning lattice parameters,[46] there exists large space to design effective and controllable optical devices by nonlinear or other methods.

Since breaking  $\mathcal{T}$ -symmetry by introducing magnetic field or dynamic modulation has its limitation to practical use, recently, more ideas have been proposed to construct a PTI, considering that there are plenty of degrees of freedom for designing photonic materials based on metamaterials and photonic crystals. Bianisotropic metamaterial is a typical example of realizing nontrivial edge state without breaking  $\mathcal{T}$ -symmetry by magnetic field or other means. Khanikaev et al.[48] first put forward a specific configuration of bianisotropic metamaterial to obtain topologically nontrivial states. It comes out that when the electric permittivity  $\varepsilon$  and magnetic permeability  $\mu$  are equal, the transverse electric (TE) mode and the transverse magnetic (TM) mode degenerate. Meanwhile, the TE+TM mode and the TE-TM mode become analogues of spins of electrons. Then by introducing the bianisotropic tensor  $\hat{\chi}$  in metamaterials, which is also known as optical activity, the initial Dirac point opens to form a bandgap with nontrivial edge state emerging at the interface between two metacrystals distinguished by opposite  $\hat{\chi}$ . The edge state dispersion curves with opposite sign slopes correspond to different spin modes. Consequently, the unidirectional propagation property was gained and different pseudo-spin modes travel in opposite directions. Later on, a much simpler structure was demonstrated and gave the same effect with bianisotropic response.[49] The configuration is shown in Figure 2e, where the bianisotropy results from the finite vacuum gap between metallic rods and the metal plate. Therefore, the researchers successfully achieved a robust waveguide utilizing the edge state, as shown in Figure 2f, even if there exist sharp corners. Based on it, reconfigurable interfaces can be realized by controlling the relevant parameter to alter the bianisotropic response of one region from positive to negative, and hence to reconstruct the domain wall.[50] In detail, assume there is an area with controllable bianisotropy and on the two sides of which existing opposite bianisotropic properties so that when the parameter of this area is tuned from one to another, the interface will change at the same time. Nevertheless, in spite of no need for magnetic field or other methods to break  $\mathcal{T}$ -symmetry, there is still a challenge that the requirement of the equality of effective  $\varepsilon$  and  $\mu$  can only be realized at a narrow frequency range, in a general case. To overcome it, Chen et al.[51] proposed that by embedding a metacrystal into a parallel-plate metallic waveguide, a relaxed matching condition can be achieved with a broad frequency range. It should be noted that the robustness of the edge states was observed under their configuration in experiment. In recent time, many new schemes and methods have been proposed to realize topological transition without breaking  $\mathcal{T}$ -symmetry such as using bianisotropic metamaterials and constructing the pseudo-spin. For example, utilizing the angular momentum of the wave function of the out-of-plane electric field in a unit cell of a dielectric photonic crystal to mimic the pseudo-spin can realize topological transition much more simply.[52,53] Besides, chiral molecules of a photonic metacrystal[54] and two kinds of circular polarization of light[55] were also investigated to gain a nontrivial topological state. In 2017, a new concept of valley

photonic crystals was proposed to obtain a series of abundant physical properties including topology, which may provide a new route to explore topological photonics.[56]

# 2.2.3. Three-Dimensional Systems with Particular Weyl Points

Dirac point is of vital concernment to construct topological transition in two dimensions, where broken  $\mathcal{T}$ -symmetry leads to the opening of this degenerate point to two bands with nonzero Chern number. While in 3D system, Dirac point will expand to a line node in momentum space, which has a linear dispersion in two directions, and still, is protected by  $\mathcal{PT}$ -symmetry.[13] More specially, a linear point degeneracy in three directions of two bands comes out as Weyl point. As an extremely particular state, Weyl point was demonstrated to possess very rich physics. One of the most significant features is that the Weyl point itself is robust, since it is the monopole in the closed surface of 3D Brillouin zone.[13] Similar to magnetic monopoles, this monopole corresponds to Chern number which is defined by the integration of Berry flux. Therefore, in other words, a zone containing a Weyl point must correspond to the nonzero Chern number. However, there is no natural material with Weyl point. As a result, the appearance of it completely depends on artificial crystals. Lu and Wang[57-59] have done many researches on gyroid photonic crystals, which are able to gain Weyl points by proper constructing. They first gained the line nodes in systems without  $\mathcal{PT}$ -symmetry breaking, then introduced  $\mathcal{P}$ -symmetry breaking or  $\mathcal{T}$ -symmetry breaking by placing an air-sphere on the asymmetrical position or applying the magnetic field, respectively. In this way, Weyl points could be successfully constructed in pairs and therefore gives rise to nonzero Chern number of a bulk band depending on the sum of the chiralities of Weyl points enclosed by the surface in momentum space.[57] Their team also fabricated the double-gyroid photonic crystal with inversion-breaking, and measured the dispersion spectrum, confirming the appearance of four isolated Weyl points predicted by theoretical analysis.[58] Besides, Wang et al.[59] put forward that by suitable adjustment of the double-gyroid photonic crystal, the four isolated Weyl point can be tuned to equiprequency. They also indicated Weyl points with equiprequency possess many advantageous properties in specific applications, such as selectivity of angular and frequency, invisible cloak and 3D imaging. Very recently, Lu et al.[60] proposed a new scheme by applying alternating magnetization in a 3D photonic crystal, a topological phase with a single Dirac cone appears which is protected not by  $\mathcal{T}$ -symmetry but by the crystal symmetry. It should be noted that this characteristic can never be realized in a 2D system as there is no Kramers degeneracy in boson system. Consequently, this work is hopeful to realize topological insulators in real sense in photonic systems without external field and provide a robust surface state. Beyond this, other configurations were also investigated recently, including those based on the 2D topological state and a 3D topological insulator realized by constructing the third spatial dimension properly.[61,62] On account of the rich physics and more degrees of freedom to operate, there still remains great room to explore 3D systems with hidden novel or even brand new properties. But

considering the difficulty in not only designing but also fabricating, especially that there is not an effective way to fabricate a complex 3D sample in nanoscale for optical frequency, there still exists many challenges to overcome.

# 3. Comparison of Topology in a Photonic System and an Electronic System

Topology is a concept that was first introduced to characterize the phase of matter in condensed matter physics. This is due to the discovery of QH effect and the following development of research on this topic. Based on the previous researches, in 2005 Haldane and Raghu introduced the concept of topology to the realm of photonics,[1] which is the beginning of topological photonics. In this section, we will compare the similarities and differences of topology in electronic systems and photonic systems, according to the realization principle. Since this review concentrates on topological photonics, effects that have no analogues in photonics so far, will not be presented here.

# 3.1. QH State in Electronic and Photonic Systems

QH effect was first discovered in 1980.[5] When a uniform strong magnetic field is applied to a 2D electron system at low temperatures, one obtains discrete Landau levels  $\varepsilon_{m} = \hbar \omega_{c}\left(m + \frac{1}{2}\right)$ ,

where  $\omega_{c}$  is the cyclotron frequency. QH phase brings about some unprecedented properties such as quantized Hall conductivity. In the photonic background, a major concern is the chiral edge state, which exhibits the property of unidirectional propagation and robustness against disorders.

The difference between QH state and ordinary insulator state lies on the famous topological invariant - Chern number,[63] which is associated with the Bloch wave function  $|u(\mathbf{k})\rangle$  (See Equation (1)). The Hamiltonian cannot be tuned smoothly to evolve into another between two systems with different Chern number. In this way the Chern number is a topological invariant that characterize the topology of a system.

The most prominent feature is the gapless conducting edge state at the interface of a bulk insulating material, where the topological invariant changes, such as a QH system and the vacuum. This edge state can only propagate in one direction and is termed "chiral". It can be understood in terms of the skipping motion electrons execute as their cyclotron orbits bounce off the edge,[3] as shown in Figure 3. This edge state is robust against disorder because of the lack of states for backscattering. In this way these edge states are topologically protected. According to the well-known bulk-edge correspondence principle, the number of topological edge states at the interface is determined by  $\Delta C$  between the two systems.

As to the photonic counterpart, many topological photonic systems have been realized intimating the electronic QH state. When two photonic systems with different Chern numbers are connected, unidirectionally propagating photonic edge state will occur at the interface, similar to the electronic case. In QH states, the presence of magnetic field and the intrinsic charge

![](images/a7af02f6cf0c0d7edc5dac7ecf6dba63ad97c0f1b90e0ffb45b0b902cd7c7703.jpg)

![](images/1c487145bc208dc235dabb2f4e44f991f1e56ad502833d5d5a405f05abdf10b5.jpg)  
Figure 3. Illustration of QH state, QSH states and their gapless conducting edge state. a) The skipping cyclotron orbits. b) The electronic band structure of QH state. A single edge state connects the valence band to the conduction band. c) The interface states between ordinary insulator  $(\nu = 0)$  and QSH insulator  $(\nu = 1)$ . d) The electronic band structure of QSH states. A pair of edge states is supported and each state is locked with certain spin and propagates unidirectionally. a-d) Reproduced with permission.[3] Copyright 2010, American Physical Society.

![](images/3cee400c2b6c42dc37cb46131cb5249ecf2065732e8318dc48c8d13bd0b09bdd.jpg)

![](images/8b8f8b8e203ed4c8f8b9b3e63aae7a206e019a8551fa4950ba60789fe4fcf55e.jpg)

of electrons play essential roles in breaking  $\mathcal{T}$ -symmetry. When converting into photonic QH state, this precondition must be achieved, for Berry curvature is an odd function under  $\mathcal{T}$ -symmetry. This leads to zero Chern number when doing integral. Photons are a kind of neutral boson and magnetic field does not influence their motion. By introducing Faraday effect, this obstacle was firstly solved by Haldane.[1] This breaks  $\mathcal{T}$ -symmetry in a different way from electrons but leads to the same result - opening the Dirac cone and consequently obtaining a non-zero Chern number.

There are other ways to realize  $\mathcal{T}$ -symmetry breaking. Another direct analogy of QH states in photonic system was proposed by Fan et al.[42] They realized an effective magnetic field in real space for photons by controlling the phase of dynamic modulation between optical resonators. The phase distribution is set corresponding to the Landau gauge, and an effective vector potential is obtained. In this way, they built a photonic system directly simulating QH states. In another prospective, this could be seen as a mimic of the Floquet topological insulator, a kind of system that is periodically driven and supports robust edge states. Later an experimental realization is achieved by Rechtsman et al.[44] using the third dimension  $z$  instead of  $t$  in a paraxial system.

# 3.2. QSH States in Electronic and Photonic Systems

The QSH state was firstly found in mercury telluride quantum well in 2007.[64] It shares similarities with the QH state, such as insulating in the bulk and supporting conducting edge states at surface. However, QSH states differ from QH states in an

important way. In contrast to the QH state, which requires magnetic field to break  $\mathcal{T}$  -symmetry, the QSH state does not. On the contrary,  $\mathcal{T}$  -symmetry protects the edge states on this occasion.

In 2005, Kane and Mele proposed a new kind of topological band structures in graphene, with  $\mathcal{T}$ -symmetry unbroken.[8] This kind of topological insulators results from spin-orbit interaction, which leads to band inversion. It is characterized by another topological invariant, the  $Z_{2}$  invariant, the name of which is derived from the property that there are only two possible values 0 and 1.

Considering the spin-  $1 / 2$  fermionic nature of electrons, the time-reversal operator has eigenvalue  $\mathcal{T}^2 = -1$ . This leads to Kramers doubling, that the eigenstates of a  $\mathcal{T}$  invariant Hamiltonian are at least twofold degenerate. For each spin there exists an independent Chern number,  $C^\uparrow$  for spin-up states and  $C^\downarrow$  for spin-down states. Under  $\mathcal{T}$ -symmetry, the total Chern number  $C = C^\uparrow + C^\downarrow$  is required to be zero, but the spin Chern number defined as  $C_{\mathrm{spin}} = \frac{1}{2} (C^\uparrow - C^\downarrow)$  can be nonzero.

The  $Z_{2}$  invariant is defined as  $\nu = C_{\mathrm{spin}}$  mod 2. Under their assumptions, spin-orbit interaction could open the Dirac cone of graphene and support a pair of edge states. These edge states are proved to be robust even spin conservation is violated,[8] thus the QSH insulator  $(\nu = 1)$  is determined to be a new topological phase. But for impurities breaking  $\mathcal{T}$ -symmetry or spin rotational symmetry, such as magnetic impurities, the robustness will be destroyed by spin flipping backscattering.[65] Such edge states in QSH insulator possess an unprecedented property. Each edge state is locked with one spin and propagates unidirectionally. For example, in Figure 3c the spin-up electrons can only propagate rightward. Based on this property, QSH insulators can naturally be applied as a spin filter. This characteristic is termed "helical" to be distinguished from "chiral" in QH states.

However, another essential difference between electrons and photons, which prevents the direct analogy of QSH states different from the one in the above section, is the spin degree of freedom. Photons are spin-1 particles, and the eigenvalue  $T^2 = 1$ . Therefore, the Kramers doubling, which plays an essential role in the QSH states does not make sense for a photonic system. Based on this, the first thing to do is to bring pseudospin degree of freedom to a photonic system.

Researchers have created various methods to realize pseudo-spin for photons. With regard to bianisotropic materials,[48] in the frequency range where  $\varepsilon = \mu$ , the TM and TE modes are nearly degenerate and their in-phase and out-of-phase combination could be designated as two pseudo-spins of photon. Another way to realize pseudo-spin is angular momentum of wave function. In a photonic graphene lattice, taking advantage of  $C_6$  group symmetry and combined with the time-reversal nature of Maxwell equations, one could build a pseudo time-reversal operator that could offer Kramers doubling.[52] Through deforming the lattice in an expanding or shrinking way, Dirac cone can be opened with difference spin Chern number and QSH states appear at the interface between these two structures. These realizations can be explained by either spin Chern number, which is closely related to  $Z_{2}$  invariant, or directly understood by spin-orbit coupling and band inversion.

We would like to put further emphasis on another approach realized by Hafezi et al.[12] They realized topologically protected edge states using coupled ring resonators. The clockwise and counterclockwise propagating modes are used to simulate two spins of electrons. In appearance their approach is a realization of photonic QSH states, for that there is a topological edge state for each spin and they propagate in different directions. However, actually the principle they used to realize this topological phase is an analogue of QH states. The key is that this system is divided into two degenerate and non-related subspace according to the pseudo-spin. By controlling the coupling phase between each pair of rings, an AB phase for photon is achieved. This can be regarded as an artificial magnetic field. For a certain pseudo-spin, it is a copy of QH states.

At last we need to point out that one common defect of these various realizations of photonic QSH states is that it is not protected by  $\mathcal{T}$ -symmetry. These realizations need strict control of fabrication to eliminate pseudo-spin mixing disorder. This means these photonic QSH phases are not as robust as the electronic case.

# 3.3. Anomalous Floquet Topological Insulators in Electronic and Photonic Systems

The above mentioned photonic Floquet topological insulator and its electronic counterpart are periodically driven systems or in  $z$ -periodic system. They share similar properties with the static conventional system. The most distinguishing point is that robust edge states can exist even the Chern number is zero.[66,67] Therefore, it is called "anomalous Floquet topological insulator". This phenomenon results from the fact that quasi-energy defined in Floquet system, such as phase, is an angle variable and not bounded below. Rudner et al.[67] gave a hand-waving thought experiment to further explain this phenomenon. Floquet system can be exactly characterized by a new invariant, a winding number derived from the discrete time evolution operator, which is the integral of time evolution over one period. Moreover, they explored its relation to the conventional Chern number.

Photonic Floquet topological insulators were developed from Hafezi's model but differ much from it. In his original tight-binding model context, when the inter-ring coupling coefficient is commensurate, the system seems to be topological trivial, where the effective magnetic field is zero and is similar to the zero flux Haldane model.[68] But a different result could be derived in network model using scattering matrix method. In this frame, a weakly coupled system shows topological trivial phase. By increasing the coupling strength over the threshold  $\theta_{c} = \frac{\pi}{4}$ , chiral edge states will appear while all Chern numbers remain zero, as shown in Figure 4.[40] This result is previous shown by Ho and Chalker[69] to study the effect of disorder in a 2D electron gas system under strong magnetic field.

It is shown that in honeycomb lattice the phase diagram can be more complicated. The system can support topological trivial phase, Chern insulator phase and the anomalous Floquet phase at different area in parameter space. To our best knowledge, this effect is still not developed in photonics yet and further study is required.

![](images/2526b3ddb7dfc1f7e028fcb1fa7f607e4efd4568629f885c8b6e1784bf139b1e.jpg)  
Figure 4. Projected quasienergy band structures for a square lattice network with coupling strength  $\theta$  increasing gradually. The Chiral edge states appear after the coupling strength is larger than  $\theta_{\mathrm{c}} = \pi /4$ . Reproduced with permission.[40] Copyright 2013, American Physical Society.

# 3.4. One-Dimensional Topological System

In 1989, Zak studied Berry curvature for 1D system and proposed the topological invariant Zak phase.[70] It is defined as the integral of Berry connection on the 1D Brillouin zone. In a 1D system the bulk-interface correspondence claims that there will be an interface state between two systems with different Zak phase 0 and  $\pi$ , similar to the 2D Chern insulator. One famous and earliest example is the SSH model for polyacetylene.[71-73] In 2014 Chan et al.[26] investigated its analogue in a 1D photonic system. In the past the existence of interface state is determined by surface impedance condition  $Z_{SL} + Z_{SR} = 0$ , while Chan gives a connection between the conventional surface impedance and the Zak phase of the bulk band structure. Therefore, the existence of edge state can be explained in another view of topology and predicted by the bulk band property. Other kinds of topology in 1D photonic systems, such as the family of AAH models including commensurate or incommensurate models and analogues of Kitaev model and Majorana fermions, showed novel phenomena by considering nonlinear effect or the natural polarization property of photons.[24,74]

# 3.5. Towards 3D Photonic Topological Insulators

In 2006 it is found that the characterization of QSH state in 2D has a natural generalization in 3D case.[75-77] The difference is that the 3D topological insulator is characterized by four topological insulator  $(\nu_{0};\nu_{1}\nu_{2}\nu_{3})$  and divided into weak topological insulator  $(\nu_{0} = 0)$  and strong topological insulator  $(\nu_{0} = 1)$ , determined by the number of Dirac point enclosed by Fermi surface on surface Brillouin zone.[3] A weak topological insulator can be constructed by stacking 2D QSH state layers, while strong topological insulator cannot be interpreted

as descendent from 2D case. In 2016 Khanikaev et al.[78] proposed an analogy of weak topological insulator in an all dielectric photonic crystal. They realized bianisotropy by carefully design and it plays the role of spin-orbit coupling in condensed matter physics, just the same as their previous research in 2D.

Weyl semimetal is a 3D analogue of graphene. Near the so called Weyl point, its dispersion is linear in all three directions.[13] Weyl point has deep relation with topology due to its uncommon properties. Different from Dirac cone, it is required to break  $\mathcal{PT}$ -symmetry to get Weyl points. Every Weyl point is a monopole of Berry flux and carries a nonzero Chern number, so they must generate or annihilate pairwise. This brings absolute robustness to Weyl point. Therefore, a photonic crystal with frequency-isolated Weyl points could have gapless edge states. Lu et al.[57] first proposed a double-gyroid photonic crystal design which shows Weyl points by introducing  $\mathcal{P}$ -symmetry breaking unit cell defect or applying  $\mathcal{T}$ -symmetry

breaking magnetic field to generate off-diagonal term in permittivity tensor.

Topology is always connected with symmetry and researchers began to explore new ways of constituting topology with other symmetries. Using crystal point group symmetry was proved to be a promising way.  $\mathrm{Fu}^{[79]}$  showed a new kind of topological insulator called "Topological Crystalline Insulators", which have metallic surface states with quadratic band degeneracy on high symmetry crystal surfaces. This brings a new way to resolve the problem of lacking Kramers doubling. In analogy of the previous "topological nonsymorphic crystalline insulators,"[80] Lu et al.[60] proposed symmetry protected 3D topological photonic crystal.

# 3.6. Conclusion

In conclusion, the neutral bosonic nature of photon and charged fermionic nature of electron are the determinant difference between topological photonic systems and topological insulators. What researchers have done these years is concentrated on how to bring Kramers doubling and artificial gauge field to photons. In this way, many topological phases have been transferred to photonics. As the cognition of topology is deepening, it is promising that a new topological phase could be discovered in photonic systems.

# 4. Applications of Topological Photonics in Integrated Photonic Devices

Topology, as a new research perspective of photonics, opens a new path to high-performance photonic devices. Similar to topological insulators in electronics, PTIs have shown their

enormous potential in engineering integrated photonic devices with robustness against disorder and high performance compared to conventional photonic devices. Although most experimental demonstrations of PTIs are performed at microwave frequencies due to the restrict of weak magnetic effects,[31,81] or difficulty in fabrication[58] at optical frequencies, quite a few photonic devices have been proposed and are expected to be future realized at optical frequencies and applied on photonic chips. All these novel devices are undoubtedly important basis of optical communication networking, where data are transmitted in the form of optical signals through various nodes. In addition, owing to the unprecedented topological protection, these devices are expected to be much more robust against imperfections and defects.

In this section, we focus on the recent progress in applications of topological photonics in integrated photonic devices, mainly in the following four aspects: light source devices, light transmission devices, optical signal processing devices and other functional devices. Significant device functions and typical approaches to realizing such functions in topological photonic systems will be presented clearly.

# 4.1. Light Source Devices

Laser, first built in 1960, which is also known as light amplification by stimulated emission of radiation, has always been a research hotspot due to its promising applications in many fields owing to its spatial coherence and temporal coherence. Many different kinds of lasers, such as gas lasers, solid-state lasers, fiber lasers, photonic crystal lasers, semiconductor lasers and so on have been designed, produced and widely used. Recent research of a class of light emitters with topological protection paved a new road to low-cost energetically effective integrated laser sources, and was expected to be widely used in the field of optical interconnections, in consideration of integration density and energy efficiency.[82]

In 2016, Pilozzi et al.[10] demonstrated lasing in strongly localized resonances in resonant photonic crystals with optical excitation. Depending on the intrinsic isolation of topologically protected states in resonant systems, the topologically sustained lasers are superior due to its low threshold and without need for population inversion. In addition, almost no gain is needed for laser operation since there exists scarcely any loss. The topological lasing was constructed in chains of two-level systems, where an ultrashort self-induced transparency pulse was utilized to directly excite the topological edge states. Two different configurations were considered, which were uniform structure (US) and Bragg structure (BS) respectively. Both structures are 1D periodic lattice where resonant two-level layers are arranged in a homogenous dielectric bulk. Time evolution of lasing in the BS chain and the US chain is shown in Figure 5a respectively. To be specific, for the BS chain with a gap in the range of  $\approx 120 - 134\mathrm{THz}$ , after a wide-band transient (about 1 ps), only two high-quality factor modes survive. For the US chain, the results are similar and after a transient regime two characteristic peaks survive. This work of lasing with topologically protected states in resonant systems has potential to be applied in laser physics and integrated photonic chips in the future.

# 4.2. Light-Transmission Devices

Transmission of light signals needs a medium, typically a waveguide or fiber, to physically restrict the expansion to the surroundings. In ordinary waveguides, unwanted feedback and loss are mainly caused by backscattering, which will therefore limit large-scale optical integration.[13] However, in a topological photonic system, good news is that the unidirectional edge waveguides could transmit electromagnetic waves without backscattering. Such an ideal property restricts a major source of loss and makes it unnecessary to use optical isolators in topological photonic circuits any more.

# 4.2.1. Directional Optical Waveguide

In 2008, Haldane and Raghu constructed analogues of quantum Hall edge states in photonic crystals made with nonreciprocal media, and showed the possibility of constructing "one-way waveguides" that allowed electromagnetic waves to flow in one direction without backscattering at bends or imperfections.[1] By breaking the  $\mathcal{T}$ -symmetry of hexagonal photonic systems with MO materials, they reported the existence of photonic analogues of the chiral edge states of the integer QH effect along the domain walls.[2]

In 2016, Blanco-Redondo et al.[30] experimentally studied topologically protected states in silicon at the interface between two dimer chains with different Zak phases using SSH model. The connection between dimers was arranged properly in order to produce a short-short defect or long-long defect at the interface. In both cases, the topological transition occurs at the interface between the left and right dimer chains, and a topological defect state emerges in the middle of the band gap. The mode propagating in the waveguides remain exponentially localized at the interface since the transverse propagation constant of this topological defect is zero (Figure 5b). This demonstration of topologically protected light waveguide at telecommunication wavelengths in silicon provides a new paradigm for complementary metal-oxide-semiconductor compatible devices.

# 4.2.2. Slow-Light Waveguide

Slow-light effect has been the subject of extensive research in the last few years, since the slower group velocity can increase light-matter interaction and enhance linear and nonlinear effects. Applications such as optical buffers, modulators, switches and so on have been demonstrated making use of slow light effect in optical telecommunications.[83,84] It is of great significance to combine slow light waveguides with topological nontrivial edge states, and such a configuration enables a lot of possible applications in optical signal processing devices.[85,86]

In 2013, Yang et al.[87] experimentally demonstrated a potential way to realize robust slow-light transmission lines with group index up to 15.6 in microwave regime. The waveguides under consideration were composed of gyromagnetic photonic crystals and a metal cladding (Figure 5c). The property of unidirectional propagation is ascribed to the broken  $T$  -symmetry with an applied magnetic field. From the projected band

![](images/552ba6f3d58ef59535b53c5ea74e2e52af9231f801bfbd4b17d1d121ff54b112.jpg)

![](images/85c0467d3dfdf5647327dd2102d7f9e0559493c0e723e881a15677520cdd872d.jpg)

![](images/23d443e463f7d420ff06bf9107aa7ae776fb4e4ddea829752380223987a6bee6.jpg)  
Figure 5. Light source device and light transmission devices. a) Time evolution of BS (left) and US (right) chain's spectrum. b) Propagation simulations of the input signal propagating through three different structures (two silicon dimer chains connected by a short-short defect, array of equidistant coupled waveguides, and two silicon dimer chains connected by a long-long defect respectively) and infrared images at the output of the structures. c) The waveguide composed of YIG rod array and a metal cladding was sandwiched between two parallel metal plates. The projected band structure of YIG array biased by an applied magnetic field. a) Reproduced with permission.[10] Copyright 2016, American Physical Society. b) Reproduced with permission.[30] Copyright 2016, American Physical Society. c) Reproduced with permission.[87] Copyright 2013, AIP Publishing.

structure (Figure 5c), it is obvious that the slope of the edge bands is flat, which means the group velocity is slow. The group velocity goes to zero at about  $11.6\mathrm{GHz}$ , so that it will enhance the optical nonlinear effects and light-matter interactions. Moreover, according to their experimental measurements, at a certain frequency point  $f_{\mathrm{c}}$  the phase velocity is infinite while the group velocity is finite, thus the electromagnetic waves will go through the waveguide without phase variation, which could be widely used in metamaterial devices.[88,89]

In 2015, Chen et al.[90] proposed a scheme that the material dispersion could be immune in a kind of photonic topological metacrystal with staggered bianisotropy. A nontrivial topological band gap with a large Chern number was confirmed in such dispersion-immune photonic topological metacrystals, producing pseudo-spin-momentum locked edge states. A potential application as slow-light waveguide was discussed, which was constructed by capping the triangular staggered photonic metacrystals with the trivial gap material. By simply moving the first row of the rods, the pseudo-spin-momentum locked edge dispersion in the first lowest band gap becomes flat near a certain frequency. A much slower group velocity and larger group

index could be achieved by further shifting the position of the second row of rods, or by adjusting the radius of the first two rows of rods.

# 4.2.3. One-Way Fiber

In 2016, Lu et al.[91] proposed a topological one-way fiber without scattering or reflection based on a 3D double-gyroid topological photonic crystal. By annihilating two Weyl points through supercell modulation in a magnetic double-gyroid, a photonic analogue of the 3D quantum Hall phase with a nonzero first Chern number  $(C_1)$  was obtained. When the modulation is helixes, one-way fiber modes could propagate along the winding axis, and at the same time the number of modes is determined by the spatial frequency of the helix. Moreover, due to the topological protection by the second Chern number  $(C_2)$  in the 4D parameter space, modes in these one-way fibers have nearly identical group and phase velocities. Comparing with conventional fibers, loss is ultralow in topological one-way fiber due to the absence of Rayleigh scattering. Besides,

Mie scattering can also be suppressed mostly so that fiber loss can be lowered further. In the proposed one-way fiber, stimulated Brillouin scattering threshold, which is the major limit of the signal-to-noise ratio and transmission distance, could also be lifted. Furthermore, Raman scattering (backward portion) and Fresnel reflections are inhibited too, which means fiber isolators are no longer necessary. The topological fibers can be realized at microwave frequencies or terahertz wavelengths using gyromagnetic materials, and at optical frequencies using gyroelectrical materials.

# 4.3. Optical Signal Processing Devices

Optical signal processing has been a quite attractive field in these years for its potentials in breaking the fundamental limits of semiconductor-based electronics caused by interconnection delays and large heat generation.[92-94] Compared with semiconductor electronic circuits, photonic circuits enables very high processing speed, high capacity and low loss, owing to the characteristics of photons as information carriers.[95] As a hotspot in recent researches, many optical signal processing devices have been designed, while most of them are based on the four optical domains of amplitude, phase, polarization, and wavelength.[96] However, when combined with topology, these devices are expected to have more compact structures and higher performance.

# 4.3.1. Optical Switching

Optical logic gates are essential components of on-chip ultrafast optical networks and integrated logic computing chips,[97] and can be cascaded to realize various functions in optical signal processing. Logical operation is essentially the operation of Boolean value "0" and "1" (or "OFF" and "ON" states). In this sense, optical switching can be seen as the foundation of any complex logic operations, because optical switching can perform the function of control cutting-off (or putting-through) of the signal light. In other words, it possesses the ON/OFF conversion function.[98,99] Recently, many researches have revealed the possibility of realizing optical switching using PTIs.

In 2016, Leykam et al.[11] theoretically proposed an optical switching based on strongly self-localized edge solitons which propagated unidirectionally along the lattice edge in a PTI. They constructed a photonic Floquet lattice of coupled helical waveguides, which were arrayed in a square lattice in the  $x - y$  plane in a Kerr nonlinear medium (Figure 6a). It turns out that whether the photonic band structure is topologically trivial or nontrivial is decided by the interwaveguide couplings in the linear optics regime.[46] A class of moving lattice edge solitons can arise due to the topological nontrivial phase, while in the topological trivial phase the solitons appear to be "embedded". In a topologically nontrivial lattice, upon increasing the input power  $P$ , the Kerr nonlinearity induces self-focusing, and solitonic propagation along the edge of the lattice could be observed. At a critical power  $P_{c}$ , the soliton becomes localized to almost a single site. In contrast to the solitons found in the nontrivial lattice, those in a topologically trivial lattice were only

observed near a specific power  $P_{\mathrm{es}}$ , which were introduced by the local Kerr nonlinearity. However, in both lattices, the solitons were able to move around corners without backscattering. A nonlinear optical switching was performed based on the discover above. A moving edge soliton and a stationary gap soliton which was produced by exciting a waveguide one-unit-cell away from the edge were initialized with the relative phase  $\Delta \varphi$  and both had the input power  $P = P_{\mathrm{c}}$ . The result of collision shows strong dependence on  $\Delta \varphi$ .[100,101] Since the peak intensities on the edge and bulk sites at  $z = 5Z$  after the collision vary with  $\Delta \varphi$ , certain choices of  $\Delta \varphi$  could almost completely destroy one of the solitons, which could be used to constitute an optical switching device, as shown in Figure 6a.

In the same year, another topological switching was implemented by Cheng et al.[50] based on the reconfigurability of the synthetic gauge field. A subset of the copper posts (positions highlighted by the green color in Figure 6b) on one of the sides of the structure was attached and glued to the triangularly shaped plastic sheet, which was moved by a computer-controlled motorized arm, thereby changing the position of the collars inside the metacrystal. Therefore, the topological states of the domain could be automatically switched between two distinct topological configurations. The electromagnetic radiation could be carried by the topological edge states from Port 1 to Port 2 or Port 3, which was decided by the configuration selected. As a result, by simply moving the collars in the green region to the up or down positions using an attached computer-controlled motorized arm, a topological optical switching was experimentally demonstrated (Figure 6b).

# 4.3.2. Circulators

An optical circulator is a nonreciprocal multi-port (at least three ports) device, in which, under ideal conditions, light entering any given port is transmitted completely to the subsequent port. Besides, if some of the light enters Port 1 is reflected, it will not come back to Port 1, but instead it will exit from Port 3 (if there are three ports). Considering the property of topologically protected unidirectional transmission in a topological nontrivial system, it is very easy and natural to construct a high-performance compact circulator.

In 2011, Qiu et al.[102] proposed a new type of circulator which was based on directional coupling between one-way photonic chiral edge states and conventional two-way waveguides. The conventional resonator-based circulators were inherently narrow-band, and the operational bandwidth was limited by the MO constants.[103] By using the topological one-way waveguides, a broadband optical circulator with a small device dimension on the order of tens of wavelengths was successfully constructed. A fundamental design of a three-port circulator is shown in Figure 6c, where a section of the one-way waveguide is placed in the vicinity of a two-way waveguide in parallel. In such system, light entering Port 1 will be completely transferred to the one-way waveguide through the directional waveguide-coupler under a certain set of conditions, and therefore the light will be transmitted to Port 2 totally. Similarly, light entering Port 2 will be completely transmitted to Port 3, and that entering Port 3 will be transmitted to Port 1 since the

![](images/a59420f41a2427f88a4cf038a2e2cbb5e024aff8a9cce98989e44959823ff3a2.jpg)

![](images/e043ed0bcc9e3ad814ee4e392ec5f0397fff49a6d6e41572f26cc57808470922.jpg)

![](images/2af5b64bb9043434261960a391faf0de585ce3cd6543b23eea7204bb7b66df38.jpg)

![](images/1b0b9580bef5672e7290f2b79eabfcba6809b4282da0a85a1bea406ba80692c3.jpg)  
Figure 6. Optical signal processing devices. a) Schematic of a photonic lattice of helical waveguides forming a square lattice in the  $x - y$  plane. Optical switching by bulk-edge soliton collisions. Intensity profiles at  $z = 0$  before the collision, and at  $z = 5Z$  (i.e. after five helix cycles) after the collision. Postcollision peak intensities in the bulk and edge waveguides versus the relative phase  $\Delta \varphi$  of the inputs. b) Demonstration of reconfigurable topological switch and its time-resolved dynamics. c) Schematics of three-port and four-port optical circulators based on one-way waveguides, with the port number illustrated and the power transport in the waveguide coupler. d) Linear response of the topological amplifier. a) Reproduced with permission.[11] Copyright 2016, American Physical Society. b) Reproduced with permission.[50] Copyright 2016, Macmillan Publishers. c) Reproduced with permission.[102] Copyright 2011, OSA Publishing. d) Reproduced under the terms of Creative Commons Attribution 3.0 License.[104]

![](images/04068ee6ae06850e7d437e807260b1ba0ecb4c80809cc72f7d7d5d40ce1f4d77.jpg)

![](images/75bda6f1ad1f9378613022af63b4b78611912758480b7d4e52afd76a6ec4f5c2.jpg)

backward propagating mode can't be coupled to the directional waveguide. The transmission spectra between these ports over a range of frequencies near the center frequency is also presented, where the sum of the transmission to Port 2 and Port 3 remains close to 1, proving that this circulator has very low loss. A four-port circulator can also be produced by cascading two three-port circulators through Port 2, with the similar principle as that of a three-port circulator, which is shown in Figure 6c. Such circulators could be realized by designing a waveguide coupler in 2D gyromagnetic photonic crystals, for example, yttrium iron garnet (YIG), where photonic chiral edge states are supported at the interface between the gyromagnetic photonic crystal and a nonmagnetic photonic crystal. An additional two-way waveguide could be introduced by creating a line defect one lattice constant away from the interface.

# 4.3.3. Travelling Wave Amplifier

As a practical device that amplifies an optical signal directly, a travelling wave amplifier or optical amplifier is important in

optical communication. In 2016, Peano et al.[104] proposed a topologically protected, nonreciprocal, quantum-limited amplifier as well as a source of chiral squeezed light in their research of an unusual spatially dependent modification of vacuum fluctuations. In a considered situation where parametric driving was introduced to a system where photons hop on a lattice in the presence of a synthetic gauge field, the researchers realized an exotic situation where all bulk modes were stable, but the topologically protected chiral edge modes were unstable. One useful application of their realization of such unstable topological edge modes is a new kind of topologically protected, phase-sensitive, quantum-limited amplifier in a finite-size array of nanocavities coupled to simple waveguides, which serve as amplifier input-output ports. The linear response of the amplifier was investigated numerically in Figure 6d. Any signals injected from the input port can propagate chirally through the output port and will be amplified or deamplified depending on its phase. Besides, the power gain for the amplified signal quadrature is flat over a large bandwidth, corresponding to the frequency range over which the edge state dispersion is purely linear. At the same time, any signals incident upon the output

port are not able to reach the input port, since they will be dumped into the sink port entirely. Furthermore, this strongly nonreciprocal amplifying behavior is of topological origin and is therefore robust against disorder.

# 4.4. Other Functional Devices

Except from the above mentioned lasers, waveguides, fibers, filters, switches, and so on, many functional devices are also necessary in signal control and processing systems and have been realized using PTIs both theoretically and experimentally in recent years.

# 4.4.1. Power Splitter and Filter

In 2010, He et al.[105] reported a design of a tunable one-way cross-waveguide splitter based on the edge modes of

gyromagnetic photonic crystal with broken  $\mathcal{T}$  -symmetry by applying an external dc magnetic field. The splitter is able to control the edge modes by central electro-optical rod due to the coupling between one-way edge modes and defect modes.[106] As shown in Figure 7a, a  $45^{\circ}$  tilted square-lattice alumina photonic crystal is used to restrict the edge modes near the interface. By inserting an alumina rod as a switch at the center, a  $50\%$  splitter is realized. In the second bandgap, there are two different defect modes according to frequency, which are totally downside transmission or totally upside transmission respectively. Besides, according to their simulation results, it is quite easy to control the pathway from one port to another by altering the radius or refractive index of the central rod. A tunable one-way splitter could be constructed by applying external electric field with an optic-electric material inserted in the center. Furthermore, by inserting some nonlinear medium, an all-optical tunable one-way splitter can be realized.[107] At the same time, by reversing the direction of external applied magnetic field or fixing the operational

![](images/54d973b8ed8a6d0c6eb50a3c15816fe6347fa0a8552612ee110c48542aca46ec.jpg)

![](images/04c8c78bc7fbea85a74591d425a98b783f0a8cf5f1acce4bbc5596685dcd76df.jpg)

![](images/fc62466a749d5d258cc829348649ad96569663f0278dc0b42277e97cb256d7be.jpg)

![](images/c45672b68a3efd9da24bcca82eed70ccb9d85a4ad262dea15baee7915b0790ec.jpg)  
Figure 7. a) Illustration of totally upside propagation by only left source in one-way cross-waveguide splitter and a  $50\%$  splitter by inserting a rod at the center. b) Power-dependent filtering by a narrow channel. The intensity profile at  $z = 8Z$  is plotted for the linear limit  $P \to 0$  (upper left figure) and the nonlinear regime at  $P = 0.55$  MW (lower left figure). The input light is injected uniformly on four waveguides marked by green circles, and the lattice boundary is marked by blue dashes. Transmittance through the channel (defined as the total intensity on the edge sites to the right of the channel) versus input power  $P$  (right figure). c) Schematic of the photonic structure of an optical isolator and the backward transmission as a function of the array length. d) Schematic of a QSH PTI and photonic time-delay lines based on detour-type defects. e) Non-obstructing large photon antennas due to spin-cloaking. a) Reproduced with permission.[105] Copyright 2010, AIP Publishing. b) Reproduced with permission.[11] Copyright 2016, American Physical Society. c) Reproduced with permission.[109] Copyright 2015, OSA Publishing. d) Reproduced under the terms of Creative Commons Attribution 4.0 International License.[111] e) Reproduced with permission[48] Copyright 2012, Macmillan Publishers.

![](images/47e7e85ffe1fb2b19689a72acd8c58a689f26fa19539fe6a5936cabddf07a58d.jpg)

frequency in the third gap, the input ports and output ports can be reversed.

Another application of a continuously tunable power splitter was demonstrated by Skirlo et al.[81] in 2014. They reported the implementation of bulk bands with multiple pairs of Dirac cones and multiple quadratic points, while simultaneous opening of these point degeneracies generated Chern numbers of large magnitudes. Significantly, several transport channels are topologically protected in this multimode one-way waveguides and it could be used to construct a topological one-way circuit.[108] At the junction between three bulk domains, one-way edge states merge together or branch off, enabling new device functionalities as signal splitters (Figure 2b) immune to backscattering from manufacturing imperfections. In their simulations, a linear combination of two one-way modes was excited by a monofrequency point source placed inside the left waveguide which was formed by the metal and  $C = 2$  domain. A metal scatterer forces the one-way modes to scatter into each other and changes their amplitudes and phases, since backscattering is forbidden. The power splitting between channels 1 and 2 is controlled by the height of the metal scatterer and the efficiency is  $100\%$  due to the lack of reflection or absorption. It's worth noting that this design is possible only when the metal scatterer is in a multimode waveguide. These implementations are experimentally realizable at microwave frequencies using a common microwave gyromagnetic material yttrium iron garnet.

In 2015, Chen et al.[90] proposed a pseudo-spin-polarized topologically protected power splitter. The power splitter was constructed by capping the triangular staggered photonic metacrystal with the gap material. A harmonic line  $H_{z}$  source with a constant amplitude and a harmonic line  $E_{z}$  source with a changing amplitude were excited at the same spot on the left corner of the splitter. By changing  $E_{z}$ , pseudo-spin-polarized modes with different ratios were excited such that the power flow could be automatically selective to propagate along either the upper or lower waveguide port. To be more specific, when  $E_{z}$  changes from  $-1$  to  $1$ , the source changes to be pseudo-spin-up, and consequently, the flow of light is manipulated from port 2 to port 1. Furthermore, their simulation results confirm that this power splitter is robust despite the presence of defects, owing to the topological protection.

In 2016, Leykam et al.[11] demonstrated selective filtering depending on the propagation of solitons through a narrow channel in a Floquet lattice of coupled helical waveguides. To realize a power-dependent filter, a one-unit-cell-wide narrow channel was used to connect two wider strips (Figure 7b). In the linear regime, the edge states can't transmit through the channel and are instead diverted, because of the absence of topological protection when there is a significant spatial overlap of modes on opposite edges. Increasing the input power  $P$  will cause the formation of a soliton that is sufficiently strongly localized to pass through the channel. Specifically, as  $P$  increases from 0 to  $0.55\mathrm{MW}$ , the transmittance exhibits an 8.6-fold variation, as shown in Figure 7b.

In 2016, Cheng et al.[50] proposed a broadband spin-locked wave-division in topological junctions, based on their design of a reconfigurable topological metacryystal. The reconfigurable topological structure was formed between two parallel copper

plates through which holes were drilled to support a periodic triangular array of copper rods with ring collars. By moving some of the rods up or down to touch either the upper or lower copper plate, arbitrarily shaped boundaries between the two topologically distinct domains can be created, and at the same time, the  $\sigma_{z}$  symmetry can be reduced and lead to an effect analogue of spin-orbit coupling. In a considered configuration of two domain walls crossing in the center of the structure, for the spin-down state, the left and right walls support only outward propagation, whereas the top and bottom walls support only inward propagation. For the spin-up state, the situation reversed. Therefore, for example, if the spin-down mode excited from the bottom Port 1 reaches the junction, transmission through the Port 3 will be suppressed since the spin-up edge state cannot be excited because of the mismatch in the spin configuration. However, in a non-topological structure, the transmission through the Port 3 should be comparable to that through Ports 2 and 4. Consequently, the topological character of the splitting at the four-port junction leads to the observed broadband spin-locked wave-division.

# 4.4.2. Optical Isolator

In order to prevent unwanted feedback into some parts of an optical system, an optical isolator, or optical diode, is widely used since it only allows the transmission of light in one certain direction. It is unnecessary to use an isolator in a topological photonic system, while itself could be used to construct an optical isolator. In 2015, El-Ganainy et al.[109] introduced a new type of optical isolator based on dissipative finite SSH waveguide arrays with broken  $\mathcal{T}$  -symmetry which supported topological edge states at one end of the structure. A magnetic garnet film was deposited only on the first waveguide element (Figure 7c), and under the application of a transverse external static magnetic field, the TM optical mode of this waveguide would experience different propagation constants in the forward and backward propagation directions.[110] According to their simulation results,  $92\%$  of the optical intensity launched in the leftmost waveguide can propagate into the output. On the other hand, the backward propagation state is not localized, and any backward propagating light into the leftmost waveguide interacts with the collective delocalized optical modes of the array and suffers significant optical losses. Isolation ratios (defined as the power ratio between the return power into waveguide 1 and the forward transmission of the device) better than  $-50~\mathrm{dB}$  between forward and backward propagating light was achieved after a propagation distance of  $24 / \kappa_{s}$ , where  $\kappa_{s}$  is the coupling coefficient (Figure 7c). By the way, this high isolation ratio can be achieved for a device length of about  $7\mathrm{mm}$  with the working wavelength at  $1.55\mu \mathrm{m}$ .

# 4.4.3. Time-Delay Line

In 2011, Hafezi et al.[12] illustrated that 2D arrays of CROW could be used to design a robust photonic delay line. The system comprised optical ring microresonators that supported degenerate clockwise and counter-clockwise modes, which

could be considered as two components of a pseudo-spin. The lengths of the upper and lower branches of the waveguide differs from each other, so that a photon will acquire a different phase when it hops from the left to the right resonator from that when it hops in the opposite direction. In this system, the  $T$ -symmetry is not broken explicitly, but instead the degenerate modes behave analogously to spins with spin-orbit coupling in the electronic QSH effect. In both the photonic quantum Hall system and a conventional 1D CROW system, the delay time is proportional to the number of resonators involved in the transport. However, In the quantum Hall system, the transport can be either performed along the long or short edge of the system, depending on the input frequency. When introducing disorders, the transmission of conventional CROW system is perturbed and the noise increases. In contrast, in the 2D quantum Hall system, the forward- and backward-going edge state have different energies and are topologically protected against disorder.

In 2016, Lai et al.[111] experimentally realized a reflection-free compact delay line based on a PTI. They introduced a photonic analogue of spin-orbital interaction to emulate the QSH effect. As shown in Figure 7d, the QSH PTI was comprised of a parallel-plate metal waveguide sandwiching a periodically arranged hexagonal array of metallic cylinders attached to one of the two metal plates and separated by a finite gap from the opposite plate. The Chern number is reversed across the wall between two QSH PTIs domains with the rods attached to the opposite plates. To emulate a time-delay line, a large sharply edged scattering defect is inserted into the path of surface electromagnetic waves. A detour-type lattice defect will introduce a time delay[112]

$$
\tau = \frac {1}{2 \pi} \left(\frac {\partial \varphi_ {\mathrm {d e f}}}{\partial f} - \frac {\partial \varphi_ {s t r}}{\partial f}\right) \tag {3}
$$

where  $\varphi_{\mathrm{str}}(f)$  and  $\varphi_{\mathrm{def}}(f)$  are the phases of the transmitted EM waves for the straight and defect-interrupted interfaces. The time delay can be indefinitely increased by stacking multiple detour defects (Figure 7d). For example, two detours produce twice the delay time for the transmitted topologically protected surface electromagnetic waves, with no decrease in the bandwidth because of the lack of interaction between adjacent defects due to topological protection. The key advantage of topologically protected delay lines is their compactness: topologically protected surface electromagnetic waves can make sharp turns into tightly-packed phase-delaying detours without any backscattering. Furthermore, based on this design of phase-delay defects, a variety of applications can be generated, including frequency-division multiplexing and terahertz wave generation.[113,114]

# 4.4.4. Examples of Complex Functional Devices

In 2013, Khanikaev et al.[48] theoretically demonstrated a photonic analogue of a topological insulator using suitably designed metamaterials without the application of external magnetic fields or breaking of  $\mathcal{T}$ -symmetry. One surprising practical application is that the spin-degenerate metamaterials and PTIs can enable the placement of multiple non-obscuring

radiation sources in close proximity of each other. As shown in Figure 7e, a slab of spin-degenerate metamaterial is embedded inside a vacuum cavity and the cavity interrupts the interface between topologically trivial and non-trivial metacrystals. The embedded antenna seems to be spin-cloaked (invisible) when illuminated by spin-polarized surface waves launched by an antenna from the left. At the same time, the antenna itself can efficiently excite any of these two modes either selectively or simultaneously.

In 2016, Wang et al.[59] constructed a quadratic bands touching in double-gyroid photonic crystal with both  $\mathcal{P}$ - and  $T$ -symmetries. By breaking the  $\mathcal{P}$ -symmetry, they split the quadratic bands touching and obtained four symmetry-related Weyl points. Such topological photonic crystals with a minimal number of four equiprequency Weyl points may pave the way to future applications including angular selectivity, frequency selectivity, invisibility cloaking, 3D imaging, and large-volume single-mode lasers and to topological phenomena such as topological Imbert-Fedorov shift.

# 5. Optical Effects in PTIs

PTIs derive from the conventional electronic topological insulators and result in lots of similarities. However, the topological physics embedded in photonic system inevitably involves various optical effects, which not only provide the basis of realization methods but also extend the possibility of theory and application. In this section, we talk about some optical effects that are particularly important for the PTIs and some optical phenomena that could extend the prospect of PTIs. Three subsections are brought below. The first subsection talks about the MO effect which is also the first scheme of PTIs' realization. We will start from the constitutive relation and the reciprocity of complex materials to give an instituted view of PTIs' realization. Then a specific review of the MO material's application in PTIs is followed. The MO material in PTIs research involves the gyroelectric material and the gyromagnetic material. The second subsection discusses the magneto-electric coupling effect, which is always called bi-isotropy (or bi-anisotropy) property. It is still convenient to enter from the constitutive relation and the intrinsic reciprocity of material. Two typical kinds of material with magneto-electric coupling are Tellegen medium and Pasteur medium. The former has non-reciprocity and the latter is reciprocal. The reciprocal Pasteur medium cannot break the  $T$ -symmetry but is possible to mimic QSH effect by using the magneto-electric coupling. In the last subsection, we give a brief review about other optical phenomena such as surface plasmon and optical nonlinearity, which bring many new phenomena and advantages when combined with the topological physics.

# 5.1. Magneto-Optical Effect

# 5.1.1. The Constitutive Relation of a Complex Material

It is often too complicated to solve an electromagnetic problem from the precise dynamics of the system, which contains the dynamics of free/bound charges and currents. Instead, the

approximated way is to find the macroscopic relationship of specific fields, and in optics that is, using a constitutive equation to relate the fields  $\mathbf{D}$  and  $\mathbf{B}$  and the fields  $\mathbf{E}$  and  $\mathbf{H}$ . The constitutive relation to describe the optical property of a complex material could be written as:

$$
\left( \begin{array}{l} \mathbf {D} \\ \mathbf {B} \end{array} \right) = \mathbf {M} \left( \begin{array}{c} \mathbf {E} \\ \mathbf {H} \end{array} \right) \tag {4}
$$

Specifically, in the command of Hermitian form of the matrix  $\mathbf{M}$ , it could be displayed as:

$$
\mathbf {M} = \left( \begin{array}{c c} \varepsilon & \chi \\ \chi^ {\dagger} & \mu \end{array} \right) \tag {5}
$$

where  $\varepsilon, \mu$  and  $\chi$  are the permittivity tensor of the medium, the permeability tensor, and coupling term respectively. By the way, Equation (5) is based on the lossless condition, which means the diagonal elements of permittivity and permeability tensor are real ones. Here,  $\pmb{\varepsilon}^{\dagger} = \pmb{\varepsilon}$ ,  $\pmb{\mu}^{\dagger} = \pmb{\mu}$ . If the response of the material is independent of the direction of the electromagnetic wave polarization, which means the off-diagonal elements of  $\mathbf{M}$  are all zero, it is called an isotropic medium. However, it is an anisotropic medium if this situation is not satisfied. The simplest situation is isotropic medium without bianisotropic effect, i.e.,  $\pmb{\varepsilon}$  and  $\pmb{\mu}$  are both diagonal matrix and  $\pmb{\chi}$  is zero matrix. When  $\pmb{\chi}$  is none-zero matrix, which means  $\mathbf{D}$  or  $\mathbf{B}$  is affected by the intrinsic  $\mathbf{E}$  and  $\mathbf{H}$  fields simultaneously, it is called bi-isotropy ( $\pmb{\chi}$  is a diagonal matrix) or bi-anisotropy ( $\pmb{\chi}$  is not a diagonal matrix). The prefix "bi" indicates the coupling between the electric and magnetic fields, which is the so-called magneto-electric coupling.

The QH effect's optical analogue problem can start from solving the Maxwell normal-mode problem in loss-free linear media with spatially periodic structure, which can also be seen as a generalized self-consistent Hermitian eigenproblem, somewhat different from the standard Hermitian eigenproblem.[1] A matrix form of the generalized Hermitian eigen-equation of Maxwell problem could be written as:

$$
i \left( \begin{array}{c c} 0 & \nabla \times \\ - \nabla \times & 0 \end{array} \right) \left( \begin{array}{l} \mathbf {E} \\ \mathbf {H} \end{array} \right) = \omega \left( \begin{array}{c c} \varepsilon & \chi \\ \chi^ {\dagger} & \mu \end{array} \right) \left( \begin{array}{l} \mathbf {E} \\ \mathbf {H} \end{array} \right) \tag {6}
$$

Corresponding to the idea of QAH effect, a reasonable way to realize PTIs is breaking the  $T$ -symmetry, which contains intrinsic (originated from the reciprocity of material) and external (such as external modulation) ways. Besides of the classification from the view of isotropy, the optical property of a complex material could also be inspected in the view of reciprocity. The reciprocity notion directly indicates the symmetry of a medium with respect to the time-reversal operation. Using the time-reversal operator  $T$  to describe the reciprocity:

$$
T = \left( \begin{array}{c c} 1 & 0 \\ 0 & - 1 \end{array} \right) K \tag {7}
$$

$K$  is the complex conjugation  $(\star)$ . Therefore, a reciprocal material should simultaneously satisfy the relationships:  $\pmb{\varepsilon}^{\star} = \pmb{\varepsilon}$ ,  $\pmb{\mu}^{\star} = \pmb{\mu}$  and  $\chi = -\chi^{\star}$ .

# 5.1.2. Realizing PTIs with MO Material

From the previous subsection, we know that in the view of constitutive relationship, a MO material does not care about the magneto-electric coupling and for simplicity, we consider  $\pmb{x}$  to be zero. MO effects contain all the phenomena where photons' behavior is affected by an external quasistatic magnetic field such as Faraday effect, Voigt effect, MO Kerr effect, Zeeman effect and Quadratic magnetic rotation (QMR) effect. The classical kind of MO material, the so-called gyrootropic material, includes gyroelectric medium and gyromagnetic medium. Their constitutive relationship can be displayed as:

$$
\bullet \quad \text {g y r o e l e c t r i c :} \quad \varepsilon = \left( \begin{array}{c c c} \varepsilon_ {1} & i \varepsilon_ {2} & 0 \\ - i \varepsilon_ {2} & \varepsilon_ {1} & 0 \\ 0 & 0 & \varepsilon_ {3} \end{array} \right), \quad \boldsymbol {\mu} = \mu \tag {8}
$$

$$
\text {· g y r o m a g n e t i c :} \quad \boldsymbol {\mu} = \left( \begin{array}{c c c} \mu_ {1} & i \mu_ {2} & 0 \\ - i \mu_ {2} & \mu_ {1} & 0 \\ 0 & 0 & \mu_ {3} \end{array} \right), \quad \varepsilon = \varepsilon
$$

The quantity  $\varepsilon_{2}$  is proportional to the magnetic field and the absolute value would be smaller than the quantity  $\varepsilon_{1}$ . It is the part  $i\varepsilon_{2}$  leads the permittivity tensor to be  $\mathcal{T}$ -symmetry broken, which means,  $K\varepsilon \neq \varepsilon$ . Similarly, the part  $i\mu_{2}$  leads the permeability tensor to be non-reciprocal. Gyromagnetic property is always appeared in ferrite material such as  $\mathrm{Fe}_3\mathrm{O}_4$ ,  $\mathrm{Y}_3\mathrm{Fe}_5\mathrm{O}_{12}$  (YIG) and andradite garnet  $(\mathrm{Ca}_3\mathrm{Fe}_2\mathrm{Si}_3\mathrm{O}_{12})$ . YIG could also be doped with other rare earth elements: Re, Gd, Bi, La, etc.

In 1988, Haldane[68] proposed a model now called QAH effect, suggested that the QH effect can also be realized in a band structure with  $\mathcal{T}$ -symmetry breaking, without Landau-level as the base, and the bands acquire non-zero Chern numbers. This opened a new field of topological physics and lighted up the later work of optical analogue of the QAH effect in photonic crystals. The first discussion using MO effect to realize PTIs in theory that taken by Raghu and Haldane[2] about the relationship of photonic topological property and  $\mathcal{T}$ -symmetry breaking was just based on the gyroelectric form, operating at the Dirac points of TE mode in a hexagonal rods lattice photonic crystal, as shown in Figure 8a. Haldane and Raghu[1,2] showed that in the photonic crystals, the "Hall effect of light" derived from the  $\mathcal{T}$ -symmetry breaking rather than the  $\mathcal{P}$ -symmetry breaking. While Wang et al.[9,31] pointed out that in realistic gyroelectric materials, the  $\mathcal{T}$ -symmetry breaking strength is always very weak. The Voigt parameter, i.e., the quantity ratio of off-diagonal to on-diagonal elements of the permittivity tensor, which could represent the strength of  $\mathcal{T}$ -symmetry breaking, is at most  $10^{-3}$  order. However, the ferrite material with gyromagnetic property could have a considerable  $\mathcal{T}$ -symmetry breaking strength. The Voigt parameter  $V = |\mu_2| / |\mu_1|$  could be of order 1. They constructed a 2D square-lattice vanadium-doped calcium-iron-garnet (VCIG; TCI ceramics NG-1850) rods photonic crystal to demonstrate in simulation the one-way propagating TM edge mode and removed the restriction of the Dirac points requirement, as shown in Figure 8b. The topological Chern numbers in such photonic crystal could be nontrivial, and the complex propagation constant is  $0.359 + 0.0001i$  corresponding to a decay length of thousands crystal periods. Even considering the dispersion

of the VCIG ferrite rods, it is no influence on the suppression of the backscattering. In experiments, they realized the one-way transmission at the VCIG ferrite rods 2D square-lattice platform working at  $4.5\mathrm{GHz}$  frequency, showing the robustness (backscatter transmission could be lower than 5 orders of magnitude) from disorder even if a metallic plate scatter was inserted.

After the work of Wang's group, many works were followed with the gyromagnetic photonic crystal platform.[32,33,35,87,105,108,115-120] Despite the theory and simulation works, several experiment works[33,35,87,116,118,119] were also reported. Li et al.[119] experimentally explored the one-way chiral edge states in a line defect waveguide surrounded by nonmagnetic  $\mathrm{Al}_{2}\mathrm{O}_{3}$  rods and gyromagnetic YIG rods.  $\mathrm{Al}_{2}\mathrm{O}_{3}$  rods photonic crystal was utilized to confine the edge state from radiating to the vacuum state. It showed that the forward-propagating waves had a relative small change to the variation of the waveguide width while the backward-propagating waves were very sensitive to the width. They also found that if a side point defect of the photonic crystal coupled with the line defect waveguide in the nontrivial gyromagnetic topological system, the backward mode can be completely coupled in the cavity while the forward mode is only slightly influenced by the cavity in the transmissivity, as shown in Figure 8c.[118] Such system could be utilized to develop the conventional add/drop filter to the unidirectional filter. Wu et al.[35] furtherly developed the gyromagnetic YIG topological system to be a honeycomb lattice, of which the zigzag boundary could self-guide the one-way chiral edge states without confinement cladding design. It still performed a five orders of magnitude ratio of the forward/backward transmission, as shown in Figure 8d. They also showed that the one-way waveguide consisted of 2D square-lattice YIG photonic crystal cladding with a metal wall exhibited good slow light effect with group index up to 2000 in simulation and to 15.6 in experiment.[87] Skirlo, Lu and Soljacic[32] showed to us in theory that the QAH phase could be more than one mode, up to a Chern number 4 (Figure 8e). By increasing the symmetry of the system, Dirac point degeneracies can come in large multiples and modulating the multiple symmetry-unrelated point degeneracies to occur in the same frequency range can leads to larger  $T$ -symmetry breaking strength with all the Berry fluxes of the same sign. This idea was realized experimentally in 2015. Still using the ferrimagnetic garnet rods photonic crystals, they observed the gap Chern number from 1 to 4, and demonstrated that combining different gap Chern number routes ( $C_{gap} = 1$ , 2 in the letter) topological one-way circuit can be implemented with more than 5 orders of magnitude unidirectional ration, as shown in Figure 8f.[33]

The MO effect is the earliest one utilized to realize PTIs and plentiful works have been followed. The intrinsic  $\mathcal{T}$ -symmetry breaking of MO material provides good robustness in one-way transmission. The mature preparation technology of ferrite YIG vastly promotes the study of PTIs. However, they are limited in the microwave frequency range, thus restricting the application size, and the utilization of other MO material has not been found.

# 5.2. Magneto-Electric Coupling

At the beginning of this section, we mentioned the magnetoelectric coupling in the presence of  $\chi$  within the constitutive equation. For convenience, we call such medium as "bi."

material considering none about isotropy or anisotropy. The "bi-" material always appears in some artificial metamaterial, which performs a different property from conventional materials. The magneto-electric coupling, which induces the field  $\mathbf{D}$  variance both by  $\mathbf{E}$  and  $\mathbf{H}$ , should be distinguished from the MO response, however. They are all affected by magnetic fields, while the "bi-" medium emphasizes the effect that the permittivity tensor  $\varepsilon$  changed by an external dc magnetic field, and the  $\mathbf{D}$  of latter one could be motivated by the intrinsic magnetic field of lights (the same relationship applied to the  $\mathbf{B}$  field). In the "bi-" medium, the coupling term  $\chi$  could decompose into two terms  $\varsigma + i\kappa$ , where both  $\varsigma$  and  $\kappa$  are real-component tensors. Then the constitutive equation is:

$$
\left( \begin{array}{c} \mathbf {D} \\ \mathbf {B} \end{array} \right) = \left( \begin{array}{c c} \varepsilon & \varsigma + i \kappa \\ \varsigma^ {\dagger} - i \kappa^ {\dagger} & \mu \end{array} \right) \left( \begin{array}{c} \mathbf {E} \\ \mathbf {H} \end{array} \right) \tag {9}
$$

$\varsigma$  is a non-reciprocity parameter and  $\kappa$  is a chirality parameter. Corresponding to the reciprocal condition mentioned above, it is non-reciprocal medium when  $\varsigma$  is non-zero. In specific situation, when  $\kappa$  is zero and  $\varsigma$  is non-zero, such non-reciprocal medium is termed as Tellegen medium. In another specific situation, when  $\kappa$  is non-zero and  $\varsigma$  is zero, such reciprocal medium is termed as Pasteur medium, in which the chirality of a propagating photon would be changed. If  $\chi$  is zero, and the term  $\varepsilon$  or  $\mu$  has a nonreal element within it, the medium also displays non-reciprocity. We will now talk about the PTIs utilizing the magneto-electric coupling in Tellegen and Pasteur medium respectively.

# 5.2.1. Tellegen Material: A Non-Reciprocal "Bi-" Material

First, considering the intrinsic non-reciprocal Tellegen material, which has magnetoelectric coupling. It is also an alternative route to the PTIs using the intrinsic non-reciprocity besides the MO medium. The Tellegen material breaks the  $\mathcal{T}$  symmetry due to the existence of the real coupling parameter  $\pmb{\varsigma}$ . It is first proposed by B. D. H. Tellegen[121] in the system of circuit network and nowadays introduced in optical fields. It could be found in naturally medium[122-126] (ferrimagnet such as  $\mathrm{GaFeO_3}$ , and antiferromagnet such as  $\mathrm{Cr_2O_3}$ ) or be constructed as an artificial material with metamaterial.[55,127,128] The nonreciprocal response in Tellegen photonic crystals without external magnetic fields had been proved and the spectral asymmetry  $\omega (\mathbf{k})\neq \omega (-\mathbf{k})$  was showed.[129] Zhang et al.[126] proposed a topological magnetic insulator consisted of antiferromagnet and showed the magnetic fluctuations in it couple to the electromagnetic fields like the axion field. Khanikaev et al.[128] designed an artificial Tellegen-type bianisotropic metacrystal consisted of an ac magnetic dipole and a double-wire metamolecule. They calculated the  $|C_{gap}|$  largest to be 2 in a hexagonal lattice and the robust one-way transmission was displayed at the boundary of two 2D metacrystals with opposite sign of coupling parameters  $\pmb{\varsigma}$ . Besides, they pointed out that using chiral antennas and split-rings, it is possible to realize such system in microwave domain. In the same year 2015, Chen et al.[55] proposed another Tellegen bianisotropic scheme utilizing piezoelectric and piezomagnetic superlattice constituents in 2D square lattices, as

![](images/dcdf4acad03a1586e751d562e5c9db02a0727ea94c46f74c96b8eabda75f17e5.jpg)  
(a)

![](images/521f7e18e9b46704cf5f93a1261be0a3a5365120256b2b8c40319ed155c91c82.jpg)  
(b)  
(e)

![](images/4cdf0e9bc9cf6b42234a8e873d9e770dd316ed71ca407b255526b7e3800f0cee.jpg)  
(c)  
(f)

![](images/b06e4f70d981f77a27b983e8589605f7f6b388261c3f18317dea65c535dbe0b2.jpg)  
(d)

![](images/5014e76ef205eafe94d18afc3ca25f378a26ac80cf21a11735a9ddb8f612f753.jpg)

![](images/28ab9983c6cd14ebddb74c7d40835b11cf15c68b6a10aaa8c8ae2f9526591e37.jpg)  
Figure 8. The MO effects in PTIs. a) The Dirac point appears in the TE band of 2D hexagonal gyroelectric crystals. b) PTIs by gyromagnetic photonic crystal. The up panel is picture of 2D square-lattice YIG photonic crystal and the down panel demonstrates in simulation that one-way propagating TM edge mode immune to obstacle. c) One way add/drop filter based on the gyromagnetic PTIs. d) Honey-comb gyromagnetic PTIs without metal cladding. The insect figure shows the edge state transmitting with good one-way property. e) Topological gap map in theory shows the Chern number distribution with different rod radius and frequency. The Chern number can reach as high as 4. d) Using gyromagnetic material YIG photonic crystals, large Chern numbers were observed. a) Reproduced with permission.[1] Copyright 2008, American Physical Society. b) Reproduced with permission.[9] Copyright 2009; Macmillan Publishers. c) Reproduced with the permission.[118] Copyright 2011, AIP Publishing. d) Reproduced with permission.[35] Copyright 2011, American Physical Society. e) Reproduced with permission.[32] Copyright 2014, American Physical Society. f) Reproduced with permission.[33] Copyright 2015, American Physical Society.

shown in Figure 9a. Similar to the QSH effect, they proposed a photonic pseudospin-orbital coupling effect which could break  $\mathcal{T}$ -symmetry. Using a new state base with left circular polarization (LCP) and right circular polarization (RCP) to mimic the electronic spin states, and construct a new pseudo  $\mathcal{T}$ -symmetry operator:  $\mathcal{T}_p = \mathcal{T}_b\tau_x = \tau_zK\tau_x = i\tau_yK$ , they successfully get a fermion-like symmetry  $\mathcal{T}_p^2 = -1$  in the bosonic system ( $T_b^2 = 1$  in the conventional bosonic system). In this system, the Tellegen parameter was designed as anisotropic form:

$$
\varsigma = \left( \begin{array}{c c c} 0 & - A _ {1} e _ {1 4} m _ {1 5} & 0 \\ A _ {1} e _ {1 4} m _ {1 5} & 0 & 0 \\ 0 & 0 & 0 \end{array} \right) \tag {10}
$$

while  $e_{14}$  and  $m_{15}$  are piezoelectric coefficient and piezomagnetic coefficient respectively. In such system, the various kinds of robustness were checked, including dielectric, Tellegen, chiral,  $T_p$  invariant impurities. It shows the former two impurities would hybrid the edge state and one-way transmission could not be held, while the chiral impurities would perturb the edge state but kept the one-way property. Besides, the  $T_p$  invariant impurities would not disturb anything.

# 5.2.2. Pasteur Material: A Reciprocal "Bi-" Material

Another kind of "bi-" material is the Pasteur medium, with the magneto-electric coupling coefficient  $\chi$  only consisting of

imaginary part  $\kappa$  and has no intrinsic  $\mathcal{T}$  broken mechanism. Topological system compose of such material is one kind of time-reversal-invariant topological system (other  $\mathcal{T}$ -invariant system could be realized by building gauge magnetic fields with coupling ring resonators network[12,38,40,130] or building a new topological phase transition at the boundary of two  $C_6$  symmetry 2D photonic crystals[52]). In most optics literature, the Pasteur medium were always directly called bianisotropic medium and it was a hot topic as the role of realizing the effective negative refractive index or left-handed (LH) material utilizing the metamaterial, for example, comprised of the split-ring resonators (SRRs), both in the microwave and the optical frequency.[131-140] Either of electric or magnetic field can excite both electric and magnetic dipoles inside the material. These dipoles can be parallel or orthogonal to the exciting field component, leading to a rich variety of cases. When the induced dipole vectors are perpendicular to the exciting fields, negative refractive index may be generated with asymmetry reflectance. Natural medium has very little bianisotropic term, i.e. magnetic-electric coupling performs too weak,  $|\kappa| \ll 1$ , and therefore it is attractive to use metamaterial to construct a giant magnetic-electric couple. An early formation to get LH material is coupling two concentric split metal ring resonators in opposite direction as shown in Figure 9b. In the TE driven fields, i.e. the magnetic fields H perpendicular to the ring face, an electromotive force is induced by the H in two rings. While two splits open in different direction, opposite

charge is stored in upper (or lower) part of the two rings, in that case two distributed capacitances are formed. In other words, driven  $\mathrm{H}_{\mathrm{z}}$  induces a perpendicular polarizability  $\mathrm{D_y}$ . The similar situation occurs when SRRs are driven by an  $\mathrm{E_y}$  field. Effective magnetic pole is induced for the induced current in rings. Marques et al.[141] carefully considered the behavior of the particle proving that the SRR should act not only as a magnetic dipole, but also as an electric dipole and gave the relationships:

$$
p _ {x} = \alpha_ {x x} ^ {e e} E _ {x} ^ {e x t}
$$

$$
p _ {\gamma} = \alpha_ {\gamma \gamma} ^ {e e} E _ {\gamma} ^ {e x t} + i \alpha_ {\gamma z} ^ {e m} B _ {z} ^ {e x t}
$$

$$
m _ {z} = - i \alpha_ {y z} ^ {e m} E _ {\gamma} ^ {e x t} + \alpha_ {z z} ^ {m m} B _ {z} ^ {e x t} \tag {11}
$$

Chen et al.[133] proposed a practical method to retrieve the bianisotropic term in square SRRs by measuring the  $S$  parameters. They concluded the detailed effective parameters and

dispersion relationships in the variable modes (from TE1 to TE3 and TM1 to TM3). Similar bianisotropic term retrieve method was also demonstrated in coupled circle split rings and wire line/ring platforms.[41] A brief tutorial review for the relationship of bianisotropic metamaterial and negative refractive index could be found in Reference 142.[142]

PTI physics with Pasteur bianisotropy was first proposed by Khanikaev et al.,[48] who realized that when TM mode and TE mode are degenerate, hybridizing the two modes into  $\Psi^{\pm} = \Psi_{TE} \pm \Psi_{TM}$  could be seen as photonic Kramers partners like spin up/down in fermions. Asymmetry SRRs metamaterial were used to design as the bianisotropic medium, and 2D hexagonal lattices were constructed to generate the graphen-like Dirac points, Figure 9c. Hybridizing needs modes degenerate and the Bloch vector should satisfy:  $q_{TE} = q_{TM}$ , which means the constitutive tensor of permittivity and permeability should also be equal:  $\pmb{\varepsilon} = \pmb{\mu}$ . The magnetic-electric coupling actually is the same as the spin-orbit coupling in the conventional topological system. In such system, the photonic Hamiltonians could be written as:

![](images/bc2957f4de5ef9cff6c560e1a051c27071456982c0fe17ea4127663a906f86c7.jpg)

![](images/3d2185ca2e9a92d4e98fc1d0a38c99fa1a7567bb2c1dbb32aa63fb2fb88debe0.jpg)

![](images/9682492e735920ebc2c06abf892b750e7334d77c92973772b6b40547a9ad339b.jpg)

![](images/551977e84e9210c8f93a0c118c92df99efa14bf3bbceba0023153e4900b9dfd1.jpg)  
Figure 9. The magneto-electric coupling in PTIs. a) PTIs based on 2D square superlattice of Pasteur material. The Pasteur response derives from the piezoelectric and piezomagnetic stacks. b) A classical setup of SRR to construct a Pasteur medium. c) PTIs consists of SRR arrays. The magneto-electric coupling could open the gap around the Dirac point and the hybrid states of TE/TM modes would represent the new Kramers partners. d) PTI constructed with Pasteur response meta-structure of metal "gyro" and "star" patterns. e) The magneto-electric coupling of Pasteur honey-comb photonic crystals could generate the valley Hall effect. a) Reproduced with permission.[55] Copyright 2016, National Academy of Sciences. b) Reproduced with permission.[141] Copyright 2002, American Physical Society. c) Reproduced with permission.[48] Copyright 2013, Macmillan Publishers. d) Reproduced with permission.[51] Copyright 2014, Macmillan Publishers. e) Reproduced with permission.[143] Copyright 2016, Macmillan Publishers.

![](images/a67e9b2884d354f90864b649cd8a19a7579d472c75863e868e46f01231fbab07.jpg)

$$
H _ {\pm} (\delta \mathbf {k}) = v _ {D} \left(\tau_ {z} \sigma_ {x} \delta k _ {x} + \sigma_ {\gamma} \delta k _ {\gamma}\right) \pm \zeta \tau_ {z} \sigma_ {z} \tag {12}
$$

$\delta \mathbf{k}$  is the deviation from  $\mathrm{K}(\mathrm{K}^{\prime})$  points of the Brillouin zone where the Dirac points just locate at.  $\zeta$  is the spin-orbit coupling term which is proximate to the coupling  $\kappa$ . When the coupling  $\kappa$  does not exist, the upper/ lower bulk bands cross and Dirac points appear. Then make the magnetic-electric coupling raised, bulk bands separate and topological phase differs to each other. At the boundary of two non-zero  $\kappa$  bianisotropic medium, opposite  $\kappa$  signs of two medium indicate opposite topological phase distribution, in that case topological phase transition generates when crossing the boundary. They pointed out that as long as the bianisotropic term  $\kappa$  was large enough the impurities caused by  $\varepsilon / \mu$  mis-matching could be suppressed to some degree. This method to approach photonic topological insulators is also an analog of the QSH effect with  $T$  invariant. Chen et al.[51] experimentally realized the Pasteur bianisotropic topological insulators in the microwave frequency near 3 GHz. Similarly hybridizing the TE/TM modes, however the SRRs were replaced by meta-atoms consisting of metal "gyro" and "star" patterns as shown in Figure 9d. They satisfied the  $\varepsilon / \mu$  matching condition by embedding the non-bianisotropic and non-resonant metacrystal into the Pasteur bianisotropic metacrystal. Then another bianisotropic metamaterial scheme called the "bed-of-nails" structure was proposed based on the photonic Kramers partners of hybrid TE/TM modes the same with precedent works.[49,50] Shvets et al.[49] demonstrated in simulation that the topological edge state could be guided around sharp corners without reflection, structure plotted in Figure 2e. Khanikaev et al.[50] experimentally realized a reconfigurable topological insulator at 20 GHz using metal rods and collars. By moving up or down the collars, the bianisotropic term could be controlled even with sign change, thus reconfigure the boundary waveguide routes in the topological platform. The experimental results showed that the cross-talk between different ports could be lower than  $10^{-3}$ . Recently, a new view of the bianisotropic topological insulator, photonic valley Hall effect, was proposed by Dong et al.[143] The similar structure with Pasteur bianisotropic units embedded into 2D hexagonal honeycomb lattices, however, the crystals parts with opposite parameter  $\kappa$  sign were not jointed with a boundary. They placed every rod adjacent to the opposite  $\kappa$  rod alternatively, thus the bands around K and K' seperated and the new pseudo-spin states could be routed in the different directions, shown in Figure 9e.

In conclusion, the Tellegen scheme with intrinsic non-reciprocity could potentially offer a stronger robustness, without external magnetic fields compared with the MO material. However, large coupling strength of natural medium in optical frequency is not easy and the metamaterial alternative faces the difficulty in technique. The reports of PTIs using the Tellegen material are rather few and no experiment has been realized. Realizing PTIs using Pasteur material constructed by metamaterial is more and more popular in these years for the avoidance of breaking  $\mathcal{T}$  -symmetry, also called  $\mathcal{T}$  -invariance PTIs. The magneto-electric coupling plays an important role in hybridizing degenerated states into photonic Kramers partners to mimic the QSH effect. Both theory and experiment reports are taken in large numbers and got intensive attention and the

valley Hall effect also showed a potential bright prospect in new application of PTIs. The difficulty is the experimental realization in visible frequency has not been achieved for the limitation of the state of art.

# 5.3. Others

There are other optical effects, which play an assistance role more or less in the realization and application of photonic topological physics. We will take a brief talk about the optical effects in the following such as SPP, Mie scattering and optical nonlinearity. The SPP is a polariton based on interaction processes between photonic radiation and free electrons at metallic interfaces. The energy of photons is conversed in a new electromagnetic form, which can propagate along the metallic surface with the free electrons oscillation. The SPP does not radiate into the vacuum environment for the momentum of SPP does not match with the one of vacuum photon. While in the nanostructures not the broad surface compared with wavelength, the plasmon (so-called surface plasmon resonance, SPR) could be coupled with vacuum photon based on the collective electrons resonance and the field would be localized. When the metal nanoparticles are placed nearby, the SPR in one nanoparticle would couple with the neighbor one. In the realization of photonic SSH model which belongs to 1D topological physics, the coupling between SPRs in the nanoparticles chain could take the place of the electrons bonding of the polyacetylene in the original SSH model.[17,24,144,145] After that, Slobozhanyuk et al.[25] proposed a dielectric scheme to mimic the coupling between SPRs by employing the magnetic Mie scattering resonances in the dielectric nanoparticles, which needed not suffer from the metallic losses. Similarly, using the Mie scattering resonance in ferrite cylinder arrays to mimic the SPP in metallic counterpart, a new photonic band gap called magnetic surface plasmon induced resonant gap was displayed.[146,147] In such resonant band gap of MO cylinder arrays, the topological edge states behaved with more robustness and size reduction, compared to that based on the regular band gap.[116] Optical nonlinearity is a wide field contains many optical phenomena. It originates from the nonlinear constitutive relationship  $\mathbf{P} = \pmb{\varepsilon}_0(\pmb{\varepsilon}^{(1)}\mathbf{E} + \pmb{\varepsilon}^{(2)}\mathbf{E}^2 + \pmb{\varepsilon}^{(3)}\mathbf{E}^3 + \dots)$ . The optical nonlinearity has no direct relationship with the realization of topological insulators but is related to the application of it. Here we simply show some reports of the combining of the photonic topology and optical Kerr effect, which is the third order nonlinearity corresponding to the  $\pmb{\varepsilon}^{(3)}\mathbf{E}^3$  term. The optical Kerr effect can be easily displayed as the formula,  $n = n_0 + |\mathbf{E}|^2 3\varepsilon^{(3)} / (8n_0)$ , and derives the phenomena such as self-focusing, self-phase modulation, optical solitons. Lumer et al.[45] showed that when replacing the linear helical waveguide units with the Kerr type nonlinear ones in the Floquet PTIs, the self-localized wave packets, solitons, as a new topological edge states form could unidirectional transport on the edge. And a new domain could be formed by nonlinearly inducing defect so that construct an "inner edge". Hadad et al.[148] demonstrated that in the third-order Kerr nonlinearities in SSH arrays self-trapping edge states also exist and locally depend on the effective environment induced by the nonlinearity. Hu et al.[149] reported an unidirectional

transmission in a 1D Kerr type nonlinear photonic crystal heterostructure, based on the unidirectional topological phase transition inducing by optical Kerr effect.

The surface plasmon makes the PTIs to be smaller size for the intensive localized property. Mie scattering makes the metallic losses reduced and the optical nonlinear provide a wider stage for photonic topological physics. These various optical effects can obviously increase the choices of PTIs platform and the potential applications of them.

# 6. Discussion and Outlook

Recent years have seen profound achievements in the whole field of topological photonics, including in the aspects of principles, experimental realizations and applications in devices. As a mathematical concept initially, topology was introduced to electronics and condensed state physics, leading to great achievements in topological insulators. In recent years, topological photonics springs up quickly and makes great breakthroughs in both principle and experiment. The novel and robust property of unidirectional propagation immune to defects and impurities is fascinating and PTIs have the potential to be applied to engineer photonic devices. The topological property is related to the bulk band of a periodic system, where Chern number, a topological invariant, is used to describe the system's topology. When an interface between two topologically distinct systems is formed, which means the two systems have different Chern number, a topological phase transition will happen, generating gapless unidirectional edge states. The number of topological edge states is determined by  $\Delta C$  across the interface. To construct a topologically nontrivial system often needs special design and external conditions. In 1D, 2D and 3D systems, different models and methods have been developed respectively. Although many concepts in topological photonics are analogues of that in topological electronics, it should not be ignored that the bosonic and fermionic nature of photon and electron are the determinant difference between PTIs and electronic topological insulators.

Based on the development of topological photonics in recent years, many photonic devices have been theoretically proposed and experimentally implemented. Light source is indispensable in optical networking. By use of strongly localized resonances in resonant photonic crystals, topologically sustained lasers are expected to be used as on-chip light source in the future. Traditionally, waveguides and fibers are used as light transmission medium, while backscattering often leads to unwanted loss. Topological systems, however, can fundamentally solve this problem due to unidirectional propagation with robustness regardless of defects. Directional optical waveguides and fibers have been demonstrated in different topological systems and slow light effect can be observed further. In optical communication networks, optical signals need to be processed effectively with high processing speed, high capacity and low loss. Topological photonics provides a new approach to realizing these device functions, including optical switching, circulators, travelling wave amplifier, power splitter, filter, optical isolator, time-delay line and so on. Typically, the realization of these devices usually needs additional optical

effects, for example, optical Kerr effect, MO effect and magneto-electric coupling.

There still exist tremendous challenges that have to be faced with. First, how to bring Kramers doubling and artificial gauge field to photon in a way that is easy to realize at optical frequency still needs further study. The second challenge is that most of the experimental demonstrations of topological photonic systems were performed at microwave frequency and the device size was too large to be integrated on chip. A large portion of experimentally feasible designs of topological photonic systems took use of gyromagnetic materials or complicated 3D structures. A corollary is that it is almost impossible to construct such topological photonic system in shorter wavelength using the same materials or 3D structures as that used in a microwave system, since most materials' magnetic response is very weak at optical frequencies and it is a great challenge to engineer complicated micro- and nanoscale 3D structures at the present stage. Current reports of implementations of photonic topology at optical frequencies are sparse and are far from being usable in integrated devices. In addition, on-chip integration is another critical problem to be solved, while the geometric dimension of most devices are too large to be integrated. The third challenge is in relation to applications in devices. In practical applications, performance indexes have to be considered and compared meticulously, while the performance index of some topological photonic devices are inferior to that of their topologically trivial counterparts. The above-mentioned challenges also point out the important development directions of integrated topological photonic devices. The first development direction is to construct topological photonic systems at optical frequency in a realizable condition. The second development direction is to perform the device functions in optical frequencies, which is impossible without further development of implementation principles of topological photonic systems. New optical materials and simple structures remain exploitation, instead of normal gyromagnetic materials and complex structures. The third development direction is towards higher performance indexes, including low power consumption, high efficiency and multi-wavelength operation in a single photonic topological device. From this perspective, the introduction of more optical effects may prompt more high-performance integrated photonic devices based on topological photonics. The fourth development direction is the pursuit of small device dimension and the possibility of on-chip integration.

At last, we would like to discuss the recent progress of topology in other bosonic systems. The development of topological photonics also inspired and pushed forward the research of topology in other bosonic systems, such as mechanical systems, acoustics and phononics, which are different presences of physical vibration at different frequency region. For macroscopic system, phononic crystal offers a perfect platform to realized topologically protected sonic wave. These methods including breaking  $\mathcal{T}$  symmetry in analogy to QH effect by introducing circulating media,[150-152] gyroscope inertial effect[153] or rotating the whole system,[154] and utilizing group symmetry to build pseudo spin[155] or wring up pendula appropriately[156] in analogy to QSH effect. At the same time, acoustic Floquet topological insulator,[157] acoustic anomalous Floquet topological insulator[158,159] and other approaches such as controlling

inter- and intra-cell coupling strength to build a 2D analogue of SSH model[160] are also demonstrated. For nanoscale system, phononic topological properties have been explored in biological systems,[161] optical mechanical systems,[162] transition-metal monosilicides material family[163] and further research is required.

# Acknowledgements

This work was supported by the 973 Program of China under Grant Nos. 2013CB328704 and 2014CB921003, and the National Natural Science Foundation of China under Grant Nos. 61475003, 11134001, 11121091, 11527901, and 90921008. Y.W. and C.L. contributed equally to this work.

# Conflict of Interest

The authors declare no conflict of interest.

# Keywords

integrated photonic devices, optical effects, photonic topological insulators

Received: April 13, 2017

Revised: June 4, 2017

Published online:

[1] F. D. M. Haldane, S. Raghu, Phys. Rev. Lett. 2008, 100, 013904.  
[2] S. Raghu, F. D. M. Haldane, Phys. Rev. A 2008, 78, 033834.  
[3] M. Z. Hasan, C. L. Kane, Rev. Mod. Phys. 2010, 82, 3045.  
[4] X. L. Qi, S. C. Zhang, Rev. Mod. Phys. 2011, 83, 1057.  
[5] K. v. Klitzing, G. Dorda, M. Pepper, Phys. Rev. Lett. 1980, 45, 494.  
[6] Y. Zhang, Y. W. Tan, H. L. Stormer, P. Kim, Nature 2005, 438, 201.  
[7] R. B. Laughlin, Phys. Rev. Lett. 1983, 50, 1395.  
[8] C. L. Kane, E. J. Mele, Phys. Rev. Lett. 2005, 95, 226801.  
[9] Z. Wang, Y. Chong, J. D. Joannopoulos, M. Soljacic, Nature 2009, 461, 772.  
[10] L. Pilozzi, C. Conti, Phys. Rev. B 2016, 93, 195317.  
[11] D. Leykam, Y. D. Chong, Phys. Rev. Lett. 2016, 117, 143901.  
[12] M. Hafezi, E. A. Demler, M. D. Lukin, J. M. Taylor, Nat. Phys. 2011, 7, 907.  
[13] L. Lu, J. D. Joannopoulos, M. Soljacic, Nat. Photonics 2014, 8, 821.  
[14] S. Aubry, G. Andre, Ann. Isr. Phys. Soc. 1980, 3, 133.  
[15] P. G. Harper, Proc. Phys. Soc. London Sect. A 1955, 68, 874.  
[16] A. Y. Kitaev, Phys.-Usp. 2001, 44, 131.  
[17] W. P. Su, J. R. Schrieffer, A. J. Heeger, Phys. Rev. Lett. 1979, 42, 1698.  
[18] W. P. Su, J. R. Schrieffer, A. J. Heeger, Phys. Rev. B 1980, 22, 2099.  
[19] A. J. Heeger, S. Kivelson, J. R. Schrieffer, W. P. Su, Rev. Mod. Phys. 1988, 60, 781.  
[20] S. Ganeshan, K. Sun, S. D. Sarma, Phys. Rev. Lett. 2013, 110, 180403.  
[21] Y. E. Kraus, Y. Lahini, Z. Ringel, M. Verbin, O. Zilberberg, Phys. Rev. Lett. 2012, 109, 106402.  
[22] M. Verbin, O. Zilberberg, Y. E. Kraus, Y. Lahini, Y. Silberberg, Phys. Rev. Lett. 2013, 110, 076403.  
[23] A. V. Poshakinskiy, A. N. Poddubny, L. Pilozzi, E. L. Ivchenko, Phys. Rev. Lett. 2014, 112, 107403.

[24] A. Poddubny, A. Miroshnichenko, A. Slobozhanyuk, Y. Kivshar, ACS Photonics 2014, 1, 101.  
[25] A. P. Slobozhanyuk, A. N. Poddubny, A. E. Miroshnichenko, P. A. Belov, Y. S. Kivshar, Phys. Rev. Lett. 2015, 114, 123901.  
[26] M. Xiao, Z. Q. Zhang, C. T. Chan, Phys. Rev. X 2014, 4, 021017.  
[27] C. Poli, M. Bellec, U. Kuhl, F. Mortessagne, H. Schomerus, Nat. Commun. 2015, 10, 7710.  
[28] X. Huang, Y. Yang, Z. H. Hang, Z. Q. Zhang, C. T. Chan, Phys. Rev. B 2016, 93, 085415.  
[29] K. H. Choi, C. W. Ling, K. F. Lee, Y. H. Tsang, K. H. Fung, Opt. Lett. 2016, 41, 1644.  
[30] A. B. Redondo, I. Andonegui, M. J. Collins, G. Harari, Y. Lumer, M. C. Rechtsman, B. J. Eggleton, M. Segev, Phys. Rev. Lett. 2016, 116, 163901.  
[31] Z. Wang, Y. D. Chong, J. D. Joannopoulos, M. Soljacic, Phys. Rev. Lett. 2008, 100, 013905.  
[32] S. A. Skirlo, L. Lu, M. Soljačić, Phys. Rev. Lett. 2014, 113, 113904.  
[33] S. A. Skirlo, L. Lu, Y. Igarashi, Q. H. Yan, J. Joannopoulos, M. Soljačić, Phys. Rev. Lett. 2015, 115, 253901.  
[34] X. F. Zang, C. Jiang, J. Opt. Soc. Am. B 2011, 28, 554.  
[35] Y. Poo, R. X. Wu, Z. Lin, Y. Yang, C. T. Chan, Phys. Rev. Lett. 2011, 106, 093903.  
[36] B. Yang, T. Wu, X. D. Zhang, Appl. Phys. Lett. 2017, 10, 021109.  
[37] R. O. Umucalilar, I. Carusotto, Phys. Rev. A 2011, 84, 043804.  
[38] M. Hafezi, S. Mittal, J. Fan, A. Migdall, J. M. Taylor, Nat. Photonics 2013, 7, 1001.  
[39] S. Mittal, J. Fan, S. Faez, A. Migdall, J. M. Taylor, M. Hafezi, Phys. Rev. Lett. 2014, 113, 087403.  
[40] G. Q. Liang, Y. D. Chong, Phys. Rev. Lett. 2013, 110, 203904.  
[41] F. Gao, Z. Gao, X. Shi, Z. Yang, X. Lin, H. Xu, J. D. Joannopoulos, M. Soljačić, H. Chen, L. Lu, Y. Chong, B. Zhang, Nat. Commun. 2016, 7, 11619.  
[42] K. Fang, Z. Yu, S. Fan, Nat. Photonics 2012, 6, 782.  
[43] L. Q. Yuan, S. H. Fan, Phys. Rev. A 2015, 92, 053822.  
[44] M. C. Rechtsman, J. M. Zeuner, Y. Plotnik, Y. Lumer, D. Podolsky, F. Dreisow, S. Nolte, M. Segev, A. Szameit, Nature 2013, 496, 196.  
[45] Y. Lumer, Y. Plotnik, M. C. Rechtsman, M. Segev, Phys. Rev. Lett. 2013, 111, 243905.  
[46] D. Leykam, M. C. Rechtsman, Y. D. Chong, Phys. Rev. Lett. 2016, 117, 013902.  
[47] M. A. Bandres, M. C. Rechtsman, M. Segev, Phys. Rev. X. 2016, 6, 011016.  
[48] A. B. Khanikaev, S. H. Mousavi, W. K. Tse, M. Kargarian, A. H. MacDonald, G. Shvets, Nat. Mater. 2013, 12, 233.  
[49] T. Ma, A. B. Khanikaev, S. H. Mousavi, G. Shvets, Phys. Rev. Lett. 2015, 114, 127401.  
[50] X. Cheng, C. Jouvaud, X. Ni, S. H. Mousavi, A. Z. Genack, A. B. Khanikaev, Nat. Mater. 2016, 15, 542.  
[51] W. J. Chen, S. J. Jiang, X. D. Chen, B. C. Zhu, L. Zhou, J. W. Dong, C. T. Chan, Nat. Commun. 2014, 5, 5782.  
[52] L. H. Wu, X. Hu, Phys. Rev. Lett. 2015, 114, 223901.  
[53] S. Barik, H. Miyake, W. DeGottardi, E. Waks, M. Hafezi, New J. Phys. 2016, 18, 113013.  
[54] M. Goryachev, M. E. Tobar, Phys. Rev. Applied 2016, 6, 064006.  
[55] C. He, X. C. Sun, X. P. Liu, M. H. Lu, Y. Chen, L. Feng, Y. F. Chen, PNAS 2016, 113, 4924.  
[56] J. W. Dong, X. D. Chen, H. Zhu, Y. Wang, X. Zhang, Nat. Mater. 2017, 16, 298.  
[57] L. Lu, L. Fu, J. D. Joannopoulos, M. Soljačić, Nat. Photonics 2013, 7, 294.  
[58] L. Lu, Z. Wang, D. Ye, L. Ran, L. Fu, J. D. Joannopoulos, M. Soljacic, Science 2015, 349, 622.  
[59] L. Y. Wang, S. K. Jian, H. Yao, Phys. Rev. A 2016, 93, 061801.  
[60] L. Lu, C. Fang, L. Fu, S. G. Johnson, J. D. Joannopoulos, M. Soljačić, Nat. Phys. 2016, 12, 337.

[61] W. J. Chen, M. Xiao, C. T. Chan, Nat. Commun. 2016, 7, 13038.  
[62] A. Slobozhanyuk, S. H. Mousavi, X. Ni, D. Smirnova, Y. S. Kivshar, A. B. Khanikaev, Nat. Photonics 2016, 11, 130.  
[63] D. J. Thouless, M. Kohmoto, M. P. Nightingale, M. den Nijs, Phys. Rev. Lett. 1982, 49, 405.  
[64] M. König, S. Wiedmann, C. Brüne, A. Roth, H. Buhmann, L. W. Molenkamp, X. L. Qi, S. C. Zhang, Science 2007, 318, 766.  
[65] X. L. Qi, S. C. Zhang, Phys. Today 2010, 63, 33.  
[66] T. Kitagawa, E. Berg, M. Rudner, E. Demler, Phys. Rev. B 2010, 82, 235114.  
[67] M. S. Rudner, N. H. Lindner, E. Berg, M. Levin, Phys. Rev. X 2013, 3, 031005.  
[68] F. D. M. Haldane, Phys. Rev. Lett. 1998, 61, 2015.  
[69] C. M. Ho, J. T. Chalker, Phys. Rev. B 1996, 54, 8708.  
[70] J. Zak, Phys. Rev. Lett. 1989, 62, 2747.  
[71] W. P. Su, J. R. Schrieffer, A. J. Heeger, Phys. Rev. Lett. 1979, 42, 1698.  
[72] W. P. Su, J. R. Schrieffer, A. J. Heeger, Phys. Rev. B 1980, 22, 2099.  
[73] A. J. Heeger, S. Kivelson, J. R. Schrieffer, W. P. Su, Rev. Mod. Phys. 1988, 60, 781.  
[74] N. Malkova, I. Hromada, X. Wang, G. Bryant, Z. Chen, Opt. Lett. 2009, 34, 1633.  
[75] L. Fu, C. L. Kane, E. J. Mele, Phys. Rev. Lett. 2007, 98, 106803.  
[76] J. E. Moore, L. Balents, Phys. Rev. B 2007, 75, 121306.  
[77] R. Roy, Phys. Rev. B 2009, 79, 195322.  
[78] A. Slobozhanyuk, S. H. Mousavi, X. Ni, D. Smirnova, Y. S. Kivshar, A. B. Khanikaev, Nat. Photonics 2017, 11, 130.  
[79] L. Fu, Phys. Rev. Lett. 2011, 106, 106802.  
[80] C. X. Liu, R. X. Zhang, B. K. VanLeeuwen, Phys. Rev. B 2014, 90, 085304.  
[81] S. A. Skirlo, L. Lu, M. Soljačić, Phys. Rev. Lett. 2014, 113, 113904.  
[82] Z. Zhou, B Yin, J. Michel, Light Sci. Appl. 2015, 4, e358.  
[83] T. Baba, Nat. Photonics 2008, 2, 465.  
[84] T. F. Krauss, Nat. Photonics 2008, 2, 448.  
[85] C. F. Ouyang, Z. Q. Xiong, F. Y. Zhao, B. Q. Dong, X. H. Hu, X. H. Liu, J. Zi, Phys. Rev. A 2011, 84, 015801.  
[86] E. Yablonovitch, Nature 2009, 461, 744.  
[87] Y. Yang, Y. Poo, R. Wu, Y. Gu, P. Chen, Appl. Phys. Lett. 2013, 102, 231113.  
[88] S. Yun, Z. H. Jiang, Q. Xu, Z. W. Liu, D. H. Werner, T. S. Mayer, ACS Nano 2012, 6, 4475.  
[89] F. M. Liu, X. Q. Huang, C. T. Chan, Appl. Phys. Lett. 2012, 100, 071911.  
[90] X. D. Chen, Z. L. Deng, W. J. Chen, J. R. Wang, J. W. Dong, Phys. Rev. B 2015, 92, 014210.  
[91] L. Lu, Z. Wang, arXiv:1611.01998v1 (Nov. 2016).  
[92] R. Kirchain, L. Kimerling, Nat. Photonics 2007, 1, 303.  
[93] H. Wei, Z. Wang, X. Tian, M. Käll, H. Xu, Nat. Commun. 2011, 2, 387.  
[94] N. Engheta, Science 2007, 317, 1698.  
[95] W. Zhao, D. Ju, Y. Jiang, Plasmonics 2015, 10, 311.  
[96] A. E. Willner, S. Khaleghi, M. R. Chitgarha, O. F. Yilmaz, J. Lightwave Technol. 2014, 32, 660.  
[97] Z. Chai, X. Hu, F. Wang, X. Niu, J. Xie, Q. Gong, Adv. Optical Mater. 2017, 5, 1600665.  
[98] J. Clark, G. Lanzani, Nat. Photonics 2010, 4, 438.  
[99] X. Hu, P. Jiang, C. Ding, H. Yang, Q. Gong, Nat. Photonics 2008, 2, 185.  
[100] G. I. Stegeman, M. Segev, Science 1999, 286, 1518.  
[101] J. Cuevas, J. C. Eilbeck, Phys. Rev. A 2006, 358, 15.  
[102] W. Qiu, Z. Wang, M. Soljacic, Opt. Express 2011, 19, 22248.  
[103] Z. Wang, S. Fan, Opt. Lett. 2005, 30, 1989.  
[104] V. Peano, M. Houde, F. Marquardt, A. A. Clerk, Phys. Rev. X 2016, 6, 041026.

[105] C. He, X. L. Chen, M. H. Lu, X. F. Li, W. W. Wan, X. S. Qian, R. C. Yin, Y. F. Chen. Appl. Phys. Lett. 2010, 96, 111111.  
[106] Z. Yu, G. Veronis, Z. Wang, S. Fan, Phys. Rev. Lett. 2008, 100, 023902.  
[107] M. F. Yanik, S. Fan, M. Soljačić, J. D. Joannopoulos, Opt. Lett. 2003, 28, 2506.  
[108] Z. Wang, L. Shen, Z. Yu, X. Zhang, X. Zheng, J. Opt. Soc. Am. B 2013, 30, 173.  
[109] R. El-Ganainy, M. Levy, Opt. Lett. 2015, 40, 5275.  
[110] H. Yokoi, Y. Shoji, T. Mizumoto, Jpn. J. Appl. Phys. 2004, 43, 5871.  
[111] K. Lai, T. Ma, X. Bo, S. Anlage, G. Shvets, Sci. Rep. 2016, 6, 28453.  
[112] P. Sebbah, O. Legrand, A. Genack, Phys. Rev. E 1999, 59, 2406.  
[113] N. J. Karl, R. W. McKinney, Y. Monnai, R. Mendis, D. M. Mittleman, Nat. Photonics 2015, 9, 717.  
[114] S. Bhattacharjee, J. H. Booske, C. L. Kory, D. W. van der Weide, S. Limbach, S. Gallagher, A. Stevens, M. Genack, J. Welter, M. Lopez, R. M. Gilgenbach, J. Wohlbier, R. L. Ives, M. E. Read, R. Divan, D. C. Mancini, IEEE T. Plasma Sci. 2004, 32, 1002.  
[115] Q. B. Li, R. X. Wu, Y. Yang, H. L. Sun, Chinese Phys. Lett. 2013, 30, 74208.  
[116] J. Lian, J. X. Fu, L. Gan, Z. Y. Li, Phys. Rev. B 2012, 85, 125108.  
[117] K. Liu, L. Shen, S. He, Opt. Lett. 2012, 37, 4110.  
[118] J. X. Fu, J. Lian, R. J. Liu, L. Gan, Z. Y. Li, Appl. Phys. Lett. 2011, 98, 211104.  
[119] J. X. Fu, R. J. Liu, Z. Y. Li, Appl. Phys. Lett. 2010, 97, 41112.  
[120] C. He, X. L. Chen, M. H. Lu, X. F. Li, W. W. Wan, X. S. Qian, R. C. Yin, Y. F. Chen, J. Appl. Phys. 2010, 107, 123117.  
[121] B. D. H. Tellegen, Philips Res. Rep. 1948, 3, 81.  
[122] G. L. J. a. Rikken, C. Strohm, P. Wyder, Phys. Rev. Lett. 2002, 89, 133005.  
[123] B. B. Krichevtysov, V. V Pavlov, R. V Pisarev, V. N. Gridnev, J. Phys. Cond. Mat. 1993, 5, 8233.  
[124] J. H. Jung, M. Matsubara, T. Arima, J. P. He, Y. Kaneko, Y. Tokura, Phys. Rev. Lett. 2004, 93, 37403.  
[125] M. Kubota, T. Arima, Y. Kaneko, J. P. He, X. Z. Yu, Y. Tokura, Phys. Rev. Lett. 2004, 92, 137401.  
[126] R. Li, J. Wang, X. L. Qi, S. C. Zhang, Nat. Phys. 2010, 6, 284.  
[127] S. A. Tretyakov, S. I. Maslovski, I. S. Nefedov, A. J. Viitanen, P. A. Belov, A. Sanmartin, Electromagnetics 2003, 23, 665.  
[128] D. A. Jacobs, A. E. Miroshnichenko, Y. S. Kivshar, A. B. Khanikaev, New J. Phys. 2015, 17, 125015.  
[129] F. R. Prudência, S. A. Matos, C. R. Paiva, Phys. Rev. A 2015, 91, 63821.  
[130] S. Mittal, S. Ganeshan, J. Fan, A. Vaezi, M. Hafezi, Nat. Photonics 2016, 10, 180.  
[131] D. R. Smith, N. Kroll, Phys. Rev. Lett. 2000, 85, 2933.  
[132] D. R. Smith, J. B. Pendry, M. C. K. Wiltshire, Science 2004, 305, 788.  
[133] X. Chen, B. I. Wu, J. A. Kong, T. M. Grzegorczyk, Phys. Rev. E 2005, 71, 46610.  
[134] D. R. Smith, J. Gollub, J. J. Mock, W. J. Padilla, D. Schurig, J. Appl. Phys. 2006, 100, 24507.  
[135] W. J. Padilla, D. N. Basov, D. R. Smith, Mater. Today 2006, 9, 28.  
[136] V. M. Shalaev, Nat. Photonics 2007, 1, 41.  
[137] C. M. Soukoulis, S. Linden, M. Wegener, Science 2007, 315, 47.  
[138] S. Zhang, Y.-S. Park, J. Li, X. Lu, W. Zhang, X. Zhang, Phys. Rev. Lett. 2009, 102, 23901.  
[139] Z. Li, K. Aydin, E. Ozbay, Phys. Rev. E 2009, 79, 26610.  
[140] S. Xiao, V. P. Drachev, A. V. Kildishev, X. Ni, U. K. Chettiar, H. K. Yuan, V. M. Shalaev, Nature 2010, 466, 735.  
[141] R. Marqués, F. Medina, R. Rafi-El-Idrissi, Phys. Rev. B 2002, 65, 144440.  
[142] C. E. Kriegler, M. S. Rill, S. Linden, M. Wegener, IEEE J. Sel. Top. Quantum Electron. 2010, 16, 367.

[143] J. Dong, X. Chen, H. Zhu, Y. Wang, X. Zhang, Nat. Mater. 2017, 16, 298.  
[144] C. W. Ling, M. Xiao, C. T. Chan, S. F. Yu, K. H. Fung, Opt. Express 2015, 23, 2021.  
[145] S. Kruk, A. Slobozhanyuk, D. Denkova, A. Poddubny, I. Kravchenko, A. Miroshnichenko, D. Neshev, Y. Kivshar, Small 2017, 1603190.  
[146] S. Liu, J. Du, Z. Lin, R. X. Wu, S. T. Chui, Phys. Rev. B 2008, 78, 155101.  
[147] S. Liu, W. Lu, Z. Lin, S. T. Chui, Appl. Phys. Lett. 2010, 97, 201113.  
[148] Y. Hadad, A. B. Khanikaev, A. Alù, Phys. Rev. B 2016, 93, 155112.  
[149] C. Li, X. Hu, H. Yang, Q. Gong, AIP Adv. 2017, 7, 25203.  
[150] Z. Yang, F. Gao, X. Shi, X. Lin, Z. Gao, Y. Chong, B. Zhang, Phys. Rev. Lett. 2015, 114, 114301.  
[151] A. B. Khanikaev, R. Fleury, S. H. Mousavi, A. Alù, Nat. Commun. 2015, 6, 8260.  
[152] Z. Chen, Y. Wu, Phys. Rev. Appl. 2016, 5, 054021.  
[153] P. Wang, L. Lu, K. Bertoldi, Phys. Rev. Lett. 2015, 115, 104302.

[154] T. Kariyado, Y. Hatsugai, Sci. Rep. 2015, 5, 18107.  
[155] C. Brendel, V. Peano, O. Painter, F. Marquardt, arXiv:1701.06330v1. arXiv.org e-Print archive (accessed Jan. 2017).  
[156] R. Süsstrunk, S. D. Huber, Science 2015, 349, 6243.  
[157] R. Fleury, A. B. Khanikaev, A. Alù, Nat. Commun. 2015, 7, 11744.  
[158] Q. Wei, Y. Tian, S. Zuo, Y. Cheng, X. Liu. Phys. Rev. B 2017, 95, 094305.  
[159] Y. Peng, C. Qin, D. Zhao, Y. Shen, X. Xu, M. Bao, H. Jia, X. Zhu, Nat. Commun. 2016, 7, 13368.  
[160] X. Ni, M. A. Gorlach, A. Alu, A. B. Khanikaev, New J. Phys. 2017, 19, 055002.  
[161] E. Prodan, C. Prodan, Phys. Rev. Lett. 2009, 103, 248101.  
[162] V. Peano, C. Brendel, M. Schmidt, F. Marquardt, Phys. Rev. X 2015, 5, 031011.  
[163] T. Zhang, Z. Song, A. Alexandradinata, H. Weng, C. Fang, L. Lu, Z. Fang, arXiv:1705.07244v1. arXiv.org e-Print archive (accessed May 2017).